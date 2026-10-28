#!/usr/bin/env python3
"""Animaciones de ENTRENAMIENTO de SAM y SAM 2 para la Talk
"segmentacion-y-stable-diffusion".

  sam-entrenamiento.gif / .png   (a) entrenamiento promptable con prompts
                                 simulados: de la máscara verdadera sale un
                                 punto, forward por los tres módulos, pérdida
                                 focal + dice, backward a los tres, y rondas
                                 con clics correctores sacados de la zona de
                                 error. (b) el data engine, como esquema.
  sam2-entrenamiento.gif / .png  un clip con su máscara verdadera por frame,
                                 prompts solo en algunos frames, pérdida
                                 sumada sobre los frames y backward que
                                 atraviesa memory attention y memory encoder.

Los dos modelos son DE JUGUETE y reales: PyTorch en float64 sobre CPU,
imágenes sintéticas propias, gradientes de autograd verificados contra
diferencias finitas, pérdidas que bajan de verdad. Mantienen los nombres de
los bloques de SAM / SAM 2, no sus tamaños.

Datos del corpus usados en rótulos: SA-1B = 11 M de imágenes y más de 1.000 M
de máscaras (sam-kirillov-2023); SA-V = el dataset de video de SAM 2
(sam2-ravi-2024, sam31-meta-2026). La proporción entre focal y dice del paper
de SAM no está en el corpus: el juguete usa L = L_focal + L_dice.

Uso:  python3 gen_train_sam.py [sam-entrenamiento] [sam2-entrenamiento]
Importa helpers de gen_anim_sam.py y gen_animaciones_conv.py (no se editan).
"""
import os
import sys

import numpy as np
import torch
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle  # noqa: E402
from PIL import Image  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_animaciones_conv import (  # noqa: E402
    TINTA, ROJO, RELLENO, GRIS_MEDIO, OUT, capturar)
from gen_anim_sam import (  # noqa: E402
    BORDE, APAGADO, PX_W, PX_H, guardar_gif_dur, figura, lienzo, flecha,
    pie, a_rgb, superponer, contorno, prisma, mapa_rgb)

torch.set_default_dtype(torch.float64)
torch.set_num_threads(4)
SCRATCH = os.environ.get("ANIM_SCRATCH")
GRIS_TXT = "#4A4645"


def guardar_atomico(frames, durs, final, nombre):
    """GIF y PNG a archivos temporales y después rename: si el proceso se
    corta, el archivo anterior queda intacto."""
    gif = os.path.join(OUT, nombre + ".gif")
    png = os.path.join(OUT, nombre + ".png")
    tmp_gif = os.path.join(OUT, f".{nombre}.parcial.gif")
    tmp_png = os.path.join(OUT, f".{nombre}.parcial.png")
    guardar_gif_dur(frames, durs, tmp_gif, colores=96)
    final.save(tmp_png)
    with Image.open(tmp_gif) as g:              # comprobar que se lee
        assert g.n_frames > 10, g.n_frames
    os.replace(tmp_gif, gif)
    os.replace(tmp_png, png)
    print(f"{gif}  {os.path.getsize(gif) / 1e6:.2f} MB")


# =========================================================================
# Modelo de juguete de SAM (común a las dos animaciones)
# =========================================================================
class Toy:
    """SAM de juguete sobre imágenes de n×n en grises.

    image encoder  : conv 3×3 con C canales + tanh        -> E (C, n, n)
    prompt encoder : token = embedding del tipo + PE(punto)·Wp   (D)
    mask decoder   : logit(x) = b + v·E(x)
                     + Σ_k [ ψ(x − p_k)·(t_k Q)                 (forma)
                             + (t_k·w_g) Σ_c u_c E_c(x) E_c(p_k) ]  (aspecto)
    ψ: 81 bumps gaussianos fijos sobre el desplazamiento x − p_k.
    """
    C, D, F, G = 6, 8, 8, 9
    TIPOS = {"pos": 0, "neg": 1, "tl": 2, "br": 3}

    def __init__(self, n):
        self.n = n
        yy, xx = np.mgrid[0:n, 0:n]
        dt = torch.get_default_dtype()
        self.XT = torch.tensor(((xx + 0.5) / n).ravel(), dtype=dt)
        self.YT = torch.tensor(((yy + 0.5) / n).ravel(), dtype=dt)
        c = np.linspace(-0.6, 0.6, self.G)
        cx, cy = np.meshgrid(c, c)
        self.CX = torch.tensor(cx.ravel(), dtype=dt)
        self.CY = torch.tensor(cy.ravel(), dtype=dt)
        self.SIG = 0.09

    @staticmethod
    def gamma(px, py):
        a = np.pi
        return torch.tensor([np.sin(a * px), np.cos(a * px), np.sin(a * py),
                             np.cos(a * py), np.sin(2 * a * px),
                             np.cos(2 * a * px), np.sin(2 * a * py),
                             np.cos(2 * a * py)],
                            dtype=torch.get_default_dtype())

    def psi(self, px, py):
        dx = (self.XT - px)[:, None] - self.CX[None]
        dy = (self.YT - py)[:, None] - self.CY[None]
        return torch.exp(-(dx ** 2 + dy ** 2) / (2 * self.SIG ** 2))

    def init(self, seed):
        g = torch.Generator().manual_seed(seed)
        C, D, F, J = self.C, self.D, self.F, self.G ** 2

        def r(*s, sc=0.1):
            return (torch.randn(*s, generator=g) * sc).requires_grad_()
        return dict(Ke=r(C, 1, 3, 3, sc=0.8), be=r(C, sc=0.3),
                    et=r(4, D, sc=0.3), Wp=r(F, D, sc=0.1),
                    Q=r(D, J, sc=0.1), wg=r(D, sc=0.1), u=r(C, sc=0.3),
                    v=r(C, sc=0.1), b=torch.zeros(1).requires_grad_())

    MODULOS = {"enc": ("Ke", "be"), "pr": ("et", "Wp"),
               "dec": ("Q", "wg", "u", "v", "b")}

    def encoder(self, P, img):
        x = torch.as_tensor(img, dtype=torch.get_default_dtype())[None, None]
        x = torch.nn.functional.pad(x, (1, 1, 1, 1), mode="replicate")
        return torch.tanh(torch.nn.functional.conv2d(x, P["Ke"], P["be"]))[0]

    def token(self, P, tipo, px, py):
        return P["et"][self.TIPOS[tipo]] + self.gamma(px, py) @ P["Wp"]

    def decoder(self, P, E, prompts):
        n, C = self.n, self.C
        Ef = E.reshape(C, -1)
        logit = P["b"] + P["v"] @ Ef
        for tipo, (px, py) in prompts:
            t = self.token(P, tipo, px, py)
            logit = logit + self.psi(px, py) @ (t @ P["Q"])
            ix, iy = min(int(px * n), n - 1), min(int(py * n), n - 1)
            logit = logit + (t @ P["wg"]) * ((P["u"] * E[:, iy, ix]) @ Ef)
        return logit.reshape(n, n)

    def forward(self, P, img, prompts):
        return self.decoder(P, self.encoder(P, img), prompts)


AL, GA = 0.25, 2.0                  # focal loss: α y γ del juguete


def perdida(logit, y):
    y = torch.as_tensor(y, dtype=logit.dtype)
    p = torch.sigmoid(logit)
    pt = p * y + (1 - p) * (1 - y)
    at = AL * y + (1 - AL) * (1 - y)
    lf = (-at * (1 - pt) ** GA * torch.log(pt.clamp_min(1e-12))).mean()
    ld = 1 - (2 * (p * y).sum() + 1) / (p.sum() + y.sum() + 1)
    return lf, ld, lf + ld


def iou(a, b):
    return (a & b).sum() / max((a | b).sum(), 1)


def verificar_gradiente(fn, P, nombres, eps=1e-6, tol=1e-6):
    """Compara autograd con diferencias centradas en 3 entradas por tensor."""
    for v in P.values():
        v.grad = None
    fn().backward()
    for nm in nombres:
        W = P[nm]
        idx = [0, W.numel() // 2, W.numel() - 1]
        for i in idx:
            with torch.no_grad():
                w0 = W.view(-1)[i].item()
                W.view(-1)[i] = w0 + eps
                lp = fn().item()
                W.view(-1)[i] = w0 - eps
                lm = fn().item()
                W.view(-1)[i] = w0
            num = (lp - lm) / (2 * eps)
            ana = W.grad.view(-1)[i].item()
            assert abs(num - ana) < tol * max(1.0, abs(num)), (nm, i, num, ana)
    for v in P.values():
        v.grad = None
    return True


# =========================================================================
# 1. sam-entrenamiento
# =========================================================================
N1 = 32
ETA1 = 0.3
PASOS1 = 2000
PASO_LUPA = 260                    # el paso que se muestra de cerca
RONDAS = 3


def _escena(rng, n=N1):
    yy, xx = np.mgrid[0:n, 0:n]
    XN, YN = (xx + 0.5) / n, (yy + 0.5) / n
    img = 0.84 - 0.06 * YN + 0.015 * rng.standard_normal((n, n))
    grises = rng.permutation([0.16, 0.30, 0.44, 0.58])[:3]
    masks, ocup = [], np.zeros((n, n), bool)
    for g in grises:
        m = None
        for _ in range(60):
            tipo = rng.integers(3)
            cx, cy = rng.uniform(0.2, 0.8, 2)
            a, b = rng.uniform(0.10, 0.21, 2)
            if tipo == 0:
                mm = ((XN - cx) / a) ** 2 + ((YN - cy) / b) ** 2 < 1
            elif tipo == 1:
                mm = (np.abs(XN - cx) < a) & (np.abs(YN - cy) < b * 0.8)
            else:
                mm = ((YN - cy < b) & (YN - cy > -b)
                      & (np.abs(XN - cx) < a * (YN - cy + b) / (2 * b)))
            if mm.sum() > 30 and (mm & ocup).sum() < 0.15 * mm.sum():
                m = mm
                break
        if m is None:
            continue
        img[m] = g + 0.02 * rng.standard_normal(m.sum())
        masks = [k & ~m for k in masks]
        masks.append(m)
        ocup |= m
    masks = [m for m in masks if m.sum() >= 20]
    return np.clip(img, 0, 1), masks


def _px(n, x, y):
    return ((x + 0.5) / n, (y + 0.5) / n)


def _prompt_inicial(rng, m, n=N1, forzar=None):
    ys, xs = np.nonzero(m)
    if forzar == "pos" or (forzar is None and rng.random() < 0.5):
        i = rng.integers(len(xs))
        return [("pos", _px(n, xs[i], ys[i]))]
    x0, x1 = xs.min() / n, (xs.max() + 1) / n
    y0, y1 = ys.min() / n, (ys.max() + 1) / n
    w, h = x1 - x0, y1 - y0
    return [("tl", (x0 + rng.normal(0, .05 * w), y0 + rng.normal(0, .05 * h))),
            ("br", (x1 + rng.normal(0, .05 * w), y1 + rng.normal(0, .05 * h)))]


def _clic_corrector(rng, pred, m, n=N1):
    """Un punto uniforme de la zona de error: positivo si cae en un falso
    negativo, negativo si cae en un falso positivo."""
    fn, fp = m & ~pred, ~m & pred
    ys, xs = np.nonzero(fn | fp)
    if len(xs) == 0:
        return None
    i = rng.integers(len(xs))
    return ("pos" if fn[ys[i], xs[i]] else "neg", _px(n, xs[i], ys[i]))


def _eta1(paso):
    """η del juguete: 0,3 hasta el paso 1.000, después baja."""
    return ETA1 if paso < 1000 else (0.1 if paso < 1500 else 0.03)


def _sgd(P, eta):
    with torch.no_grad():
        for v in P.values():
            v -= eta * v.grad


def _ronda(T, P, img, m, prompts, eta, guardar=False):
    for v in P.values():
        v.grad = None
    logit = T.forward(P, img, prompts)
    lf, ld, L = perdida(logit, m)
    L.backward()
    info = None
    if guardar:
        info = dict(prompts=list(prompts), prob=torch.sigmoid(logit)
                    .detach().numpy(), lf=lf.item(), ld=ld.item(),
                    L=L.item(),
                    W={k: v.detach().numpy().copy() for k, v in P.items()},
                    g={k: v.grad.detach().numpy().copy()
                       for k, v in P.items()})
    _sgd(P, eta)
    if guardar:
        info["W1"] = {k: v.detach().numpy().copy() for k, v in P.items()}
    return logit.detach().numpy() > 0, L.item(), info


def _entrenar_sam(lupa=None, ck_cada=40):
    """Entrena el juguete. lupa = (img, m, prompt0, semilla_clics): el
    ejemplo que se usa en el paso PASO_LUPA (y se guarda con detalle)."""
    T = Toy(N1)
    rng = np.random.default_rng(0)
    datos = [_escena(rng) for _ in range(400)]
    P = T.init(1)
    hist, cks, det, ini = [], {}, None, None
    for paso in range(PASOS1):
        if paso % ck_cada == 0:
            cks[paso] = {k: v.detach().clone() for k, v in P.items()}
        if paso == PASO_LUPA and lupa is not None:
            img, m, pr, sem = lupa
            r2 = np.random.default_rng(sem)
            det, prompts = [], list(pr)
            for _ in range(RONDAS):
                pred, L, info = _ronda(T, P, img, m, prompts, ETA1, True)
                info["iou"] = iou(info["prob"] > 0.5, m)
                det.append(info)
                c = _clic_corrector(r2, pred, m)
                info["clic"] = c
                prompts = prompts + [c]
            hist.append(det[0]["L"])
            continue
        img, ms = datos[rng.integers(len(datos))]
        m = ms[rng.integers(len(ms))]
        prompts = _prompt_inicial(rng, m)
        for r in range(RONDAS):
            pred, L, _ = _ronda(T, P, img, m, prompts, _eta1(paso))
            if r == 0:
                hist.append(L)
            c = _clic_corrector(rng, pred, m)
            if c is None:
                break
            prompts = prompts + [c]
        if paso == PASO_LUPA - 1:
            ini = {k: v.detach().clone() for k, v in P.items()}
    cks[PASOS1] = {k: v.detach().clone() for k, v in P.items()}
    return T, np.array(hist), cks, det, ini


def _buscar_lupa():
    """Elige el ejemplo del paso de cerca: un punto en un objeto que en la
    ronda 1 sale mal y que los clics correctores arreglan."""
    _, _, _, _, ini = _entrenar_sam(None)
    T = Toy(N1)
    mejores = []
    for s in range(400):
        rng = np.random.default_rng(5000 + s)
        img, ms = _escena(rng)
        for j, m in enumerate(ms):
            if m.sum() < 45:
                continue
            ys, xs = np.nonzero(m)
            # punto bien adentro: el más cercano al centroide
            k = np.argmin((xs - xs.mean()) ** 2 + (ys - ys.mean()) ** 2)
            pr = [("pos", _px(N1, xs[k], ys[k]))]
            for sem in range(3):
                P = {k_: v.detach().clone().requires_grad_()
                     for k_, v in ini.items()}
                r2 = np.random.default_rng(sem)
                prompts, ious, Ls, clics = list(pr), [], [], []
                for _ in range(RONDAS):
                    pred, L, info = _ronda(T, P, img, m, prompts, ETA1, True)
                    ious.append(iou(info["prob"] > 0.5, m))
                    Ls.append(L)
                    c = _clic_corrector(r2, pred, m)
                    if c is None:
                        break
                    clics.append(c)
                    prompts = prompts + [c]
                if len(ious) < RONDAS:
                    continue
                ok = (0.3 < ious[0] < 0.62 and ious[1] > ious[0] + 0.12
                      and ious[2] > ious[1] + 0.02 and ious[2] > 0.72
                      and Ls[0] > Ls[1] > Ls[2])
                if ok:
                    tipos = [c[0] for c in clics[:2]]
                    mejores.append((ious[2] - ious[0], s, j, sem, ious,
                                    Ls, tipos))
    mejores.sort(reverse=True)
    return mejores


# El ejemplo del paso de cerca (elegido con _buscar_lupa): escena 5000+273,
# objeto 1 (el triángulo), punto más cercano al centroide, clics con semilla 0
LUPA_ESCENA, LUPA_OBJ, LUPA_SEM = 273, 1, 0
CK_RAPIDOS = [320, 360, 400, 480, 560, 640, 760, 880, 1000, 1160, 1320,
              1480, 1640, 1800, 2000]
VENTANA = 50                        # media móvil de la curva


def _cache(nombre, fn, version):
    if SCRATCH:
        os.makedirs(SCRATCH, exist_ok=True)
        ruta = os.path.join(SCRATCH, f"cache-{nombre}.pt")
        if os.path.exists(ruta):
            d = torch.load(ruta, weights_only=False)
            if d.get("version") == version:
                return d["datos"]
        d = fn()
        torch.save({"version": version, "datos": d}, ruta)
        return d
    return fn()


def _sam_datos():
    img, ms = _escena(np.random.default_rng(5000 + LUPA_ESCENA))
    m = ms[LUPA_OBJ]
    ys, xs = np.nonzero(m)
    k = np.argmin((xs - xs.mean()) ** 2 + (ys - ys.mean()) ** 2)
    pr = [("pos", _px(N1, xs[k], ys[k]))]
    T = Toy(N1)
    # verificación de gradientes en el ejemplo, con pesos al azar
    P0 = T.init(1)
    verificar_gradiente(lambda: perdida(T.forward(P0, img, pr + [
        ("neg", (0.3, 0.7)), ("tl", (0.2, 0.2)), ("br", (0.6, 0.8))]),
        m)[2], P0, list(P0))
    T, hist, cks, det, _ = _entrenar_sam((img, m, pr, LUPA_SEM))
    rap = []
    for c in CK_RAPIDOS:
        P = {k_: v.detach().clone().requires_grad_()
             for k_, v in cks[c].items()}
        logit = T.forward(P, img, pr)
        lf, ld, L = perdida(logit, m)
        L.backward()
        rap.append(dict(paso=c, prob=torch.sigmoid(logit).detach().numpy(),
                        lf=lf.item(), ld=ld.item(), L=L.item(),
                        W={k_: v.detach().numpy().copy()
                           for k_, v in P.items()},
                        g={k_: v.grad.numpy().copy() for k_, v in P.items()}))
    mm = np.convolve(hist, np.ones(VENTANA) / VENTANA, mode="valid")
    return dict(img=img, m=m, pr=pr, hist=hist, media=mm, det=det, rap=rap)


# --- vistas de los pesos de cada módulo ----------------------------------
def _vista(mod, d):
    if mod == "enc":
        return d["Ke"].reshape(6, 9)
    if mod == "pr":
        return np.vstack([d["et"], d["Wp"]])            # 12×8
    return d["Q"]                                        # 8×81


def _div_rgb(M, escala):
    """Divergente: negativo tinta, 0 blanco, positivo rojo (escala fija)."""
    t = np.clip(M / (escala + 1e-12), -1, 1)[..., None]
    blanco = np.ones(3)
    rojo = np.array([0xD7, 0x19, 0x2A]) / 255
    tinta = np.array([0x3A, 0x3A, 0x3A]) / 255
    return np.where(t >= 0, blanco + t * (rojo - blanco),
                    blanco + (-t) * (tinta - blanco))


def _norma(mod, g):
    return float(np.sqrt(sum((g[k] ** 2).sum() for k in Toy.MODULOS[mod])))


def _fmt(x, d=2):
    return f"{x:.{d}f}".replace(".", ",")


def caja_mod(ax, x, y, w, h, titulo, sub, *, activa=False, fs=22,
             fs_sub=18, estado="entrena"):
    """Módulo entrenable: borde rojo + 'se entrena'. Activa: relleno rosado."""
    if estado == "entrena":
        fc = "#FBE1E4" if activa else RELLENO
        ec, lw, ct = ROJO, 4.0 if activa else 2.6, ROJO if activa else TINTA
    elif estado == "sin_pesos":
        fc = "#FBE1E4" if activa else "white"
        ec, lw, ct = ROJO if activa else GRIS_MEDIO, 2.0, TINTA
    else:                                            # apagado
        fc, ec, lw, ct = "white", BORDE, 1.8, APAGADO
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,"
                                "rounding_size=14", fc=fc, ec=ec, lw=lw,
                                zorder=3, ls="--" if estado == "sin_pesos"
                                else "-"))
    ax.text(x + w / 2, y + 28, titulo, ha="center", va="center", fontsize=fs,
            fontweight="bold", color=ct, zorder=4)
    if sub:
        ax.text(x + w / 2, y + 56, sub, ha="center", va="center",
                fontsize=fs_sub, color=GRIS_TXT if estado != "apagado"
                else APAGADO, zorder=4)
    if estado == "entrena":
        ax.text(x + 4, y - 6, "se entrena", ha="left", va="bottom",
                fontsize=17, fontweight="bold", color=ROJO, zorder=4)
    elif estado == "sin_pesos":
        ax.text(x + 4, y - 6, "sin pesos", ha="left", va="bottom",
                fontsize=17, color=GRIS_MEDIO, zorder=4)


def heat(ax, M, x, y, w, h, z=5, borde=TINTA, lw=1.4, alfa=1.0):
    ax.imshow(M, extent=(x, x + w, y + h, y), interpolation="nearest",
              zorder=z, alpha=alfa, aspect="auto")
    ax.add_patch(Rectangle((x, y), w, h, fill=False, ec=borde, lw=lw,
                           zorder=z + 0.1))


def kernels(ax, K, x, y, lado, gap, escala, borde=TINTA, lw=1.2):
    """6 kernels 3×3 en una grilla de 2×3."""
    for i in range(6):
        fx, fy = x + (i % 3) * (lado + gap), y + (i // 3) * (lado + gap)
        heat(ax, _div_rgb(K[i].reshape(3, 3), escala), fx, fy, lado, lado,
             borde=borde, lw=lw)


def glifo(ax, tipo, x, y, ms=15, z=9, alfa=1.0):
    """Clic positivo: punto rojo con +. Negativo: punto tinta con −."""
    col = ROJO if tipo == "pos" else TINTA
    ax.plot([x], [y], "o", ms=ms, mfc=col, mec="white", mew=2.4, zorder=z,
            alpha=alfa)
    ax.text(x, y + 0.5, "+" if tipo == "pos" else "−", ha="center",
            va="center", fontsize=ms * 0.95, fontweight="bold",
            color="white", zorder=z + 0.1, alpha=alfa)


def rayado(ax, err, x0, y0, lado, color=TINTA, lw=1.3, z=6):
    n = err.shape[0]
    c = lado / n
    segs = []
    for (i, j) in zip(*np.nonzero(err)):
        segs.append([(x0 + j * c, y0 + (i + 1) * c), (x0 + (j + 1) * c,
                                                       y0 + i * c)])
    if segs:
        from matplotlib.collections import LineCollection
        ax.add_collection(LineCollection(segs, colors=color, linewidths=lw,
                                         zorder=z))


# --- geometría ------------------------------------------------------------
S_IMG = (60, 74, 190)                     # x, y, lado
S_GT = (60, 376, 190)
S_ENC = (300, 70, 290, 226)
S_PR = (300, 352, 290, 226)
S_DEC = (640, 210, 260, 226)
S_PRED = (955, 230, 190)
S_LOSS = (1192, 70, 368, 302)
S_CURVA = (1240, 440, 1550, 565)          # x0, y0, x1, y1 (ejes)
S_BAND_Y = 630
S_NODOS = [("SAM propone", "máscaras"), ("anotadores", "las corrigen"),
           ("más datos", "anotados"), ("se reentrena", "SAM")]
S_NODO_W, S_NODO_H, S_NODO_Y = 290, 76, 654


def _nodos_x():
    gap = 70
    total = 4 * S_NODO_W + 3 * gap
    x0 = (PX_W - total) / 2
    return [x0 + i * (S_NODO_W + gap) for i in range(4)], gap


def _sam_dibujar(ax, D, st, esc):
    lienzo(ax)
    img, m = D["img"], D["m"]
    fase = st.get("fase")
    f = st.get("f", 1.0)
    prompts = st.get("prompts", [])
    act = st.get("activos", ())
    # ---- imagen ------------------------------------------------------
    x, y, l = S_IMG
    ax.imshow(a_rgb(img), extent=(x, x + l, y + l, y),
              interpolation="nearest", zorder=1)
    ax.add_patch(Rectangle((x, y), l, l, fill=False, ec=TINTA, lw=1.8,
                           zorder=5))
    ax.text(x + l / 2, y - 12, "imagen", ha="center", va="bottom",
            fontsize=21, fontweight="bold", color=TINTA)
    ax.text(x + l / 2, y + l + 8, "32×32", ha="center", va="top",
            fontsize=17, color=GRIS_TXT)
    n = N1
    c = l / n
    for k, (tipo, (px, py)) in enumerate(prompts):
        glifo(ax, tipo, x + px * l, y + py * l, ms=13)
    # ---- máscara verdadera + prompt sampleado ------------------------
    x, y, l = S_GT
    rgb = superponer(np.ones((n, n, 3)), m, 0.85)
    ax.imshow(rgb, extent=(x, x + l, y + l, y), interpolation="nearest",
              zorder=1)
    ax.add_patch(Rectangle((x, y), l, l, fill=False, ec=TINTA, lw=1.8,
                           zorder=5))
    ax.text(x + l / 2, y - 10, "máscara\nverdadera", ha="center",
            va="bottom", fontsize=21, fontweight="bold", color=TINTA,
            linespacing=1.05)
    for k, (tipo, (px, py)) in enumerate(prompts):
        glifo(ax, tipo, x + px * l, y + py * l, ms=13)
    if fase == "dato" and st.get("pulso") is not None:
        px, py = D["pr"][0][1]
        r = 8 + 40 * st["pulso"]
        ax.add_patch(Circle((x + px * l, y + py * l), r, fill=False, ec=ROJO,
                            lw=3, alpha=1 - st["pulso"], zorder=8))

    # ---- flechas forward ---------------------------------------------
    def col(clave):
        return ROJO if clave in act else TINTA

    def lw_(clave):
        return 3.4 if clave in act else 2.2
    ex, ey, ew, eh = S_ENC
    px_, py_, pw, ph = S_PR
    dx, dy, dw, dh = S_DEC
    qx, qy, ql = S_PRED
    flecha(ax, (S_IMG[0] + S_IMG[2] + 8, ey + eh / 2 + 4),
           (ex - 8, ey + eh / 2 + 4), color=col("a_img"), lw=lw_("a_img"))
    flecha(ax, (S_GT[0] + S_GT[2] + 8, py_ + ph / 2 + 4),
           (px_ - 8, py_ + ph / 2 + 4), color=col("a_pr"), lw=lw_("a_pr"))
    flecha(ax, (ex + ew + 6, ey + eh / 2 + 4), (dx - 8, dy + 70),
           color=col("a_enc"), lw=lw_("a_enc"))
    flecha(ax, (px_ + pw + 6, py_ + ph / 2 + 4), (dx - 8, dy + dh - 70),
           color=col("a_prd"), lw=lw_("a_prd"))
    flecha(ax, (dx + dw + 6, dy + dh / 2), (qx - 8, dy + dh / 2),
           color=col("a_dec"), lw=lw_("a_dec"))
    flecha(ax, (qx + ql + 6, dy + dh / 2), (S_LOSS[0] - 8, S_LOSS[1] +
                                             S_LOSS[3] - 60),
           color=col("a_loss"), lw=lw_("a_loss"))

    # ---- backward: flechas rojas punteadas en sentido contrario --------
    bw = st.get("bwd", 0.0)              # 0..1 avance del gradiente
    if bw > 0:
        tramos = [((S_LOSS[0] - 8, S_LOSS[1] + S_LOSS[3] - 32),
                   (qx + ql + 8, dy + dh / 2 + 26)),
                  ((qx - 8, dy + dh / 2 + 26), (dx + dw + 8,
                                                dy + dh / 2 + 26)),
                  ((dx - 8, dy + 100), (ex + ew + 8, ey + eh / 2 + 34)),
                  ((dx - 8, dy + dh - 40), (px_ + pw + 8,
                                            py_ + ph / 2 + 34))]
        hitos = [0.0, 0.3, 0.55, 0.55]
        for (a, b), h0 in zip(tramos, hitos):
            t = np.clip((bw - h0) / 0.3, 0, 1)
            if t <= 0:
                continue
            bb = (a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))
            flecha(ax, a, bb, color=ROJO, lw=3.2, ms=18, ls=(0, (4, 3)),
                   zorder=7)
        if bw < 1:
            pass

    # ---- módulos -------------------------------------------------------
    W, g = st["W"], st.get("g")
    ga = st.get("g_alpha", 0.0)
    ga_mod = st.get("g_alpha_mod", {"enc": ga, "pr": ga, "dec": ga})
    for mod, (bx, by, bwd, bh), tit, sub in (
            ("enc", S_ENC, "image encoder", "conv 3×3 → 32×32×6"),
            ("pr", S_PR, "prompt encoder", "punto → token de 8"),
            ("dec", S_DEC, "mask decoder", "→ logits 32×32")):
        caja_mod(ax, bx, by, bwd, bh, tit, sub, activa=mod in act,
                 fs=21)
        Wv = _vista(mod, W)
        gv = _vista(mod, g) if g is not None else np.zeros_like(Wv)
        a_g = ga_mod.get(mod, 0.0)
        borde_g = ROJO if a_g > 0 else BORDE
        if mod == "dec":
            hx, hw = bx + 20, bwd - 40
            ax.text(hx, by + 86, "W  (8×81)", ha="left", va="center",
                    fontsize=17, color=TINTA, zorder=6)
            heat(ax, _div_rgb(Wv, esc["W"][mod]), hx, by + 98, hw, 34)
            ax.text(hx, by + 150, "∂L/∂W", ha="left", va="center",
                    fontsize=17, fontweight="bold",
                    color=ROJO if a_g > 0 else GRIS_MEDIO, zorder=6)
            ax.add_patch(Rectangle((hx, by + 162), hw, 34, fc="white",
                                   ec="none", zorder=4.9))
            if a_g > 0:
                heat(ax, _div_rgb(gv, esc["g"][mod]), hx, by + 162, hw, 34,
                     borde=ROJO, lw=1.8, alfa=a_g)
            else:
                ax.add_patch(Rectangle((hx, by + 162), hw, 34, fill=False,
                                       ec=BORDE, lw=1.4, zorder=5))
            ny = by + 216
            nx = bx + bwd / 2
        else:
            lx, rx, hy = bx + 26, bx + 160, by + 104
            ax.text(lx + 52, by + 88, "W", ha="center", va="center",
                    fontsize=18, color=TINTA, zorder=6)
            ax.text(rx + 52, by + 88, "∂L/∂W", ha="center", va="center",
                    fontsize=18, fontweight="bold",
                    color=ROJO if a_g > 0 else GRIS_MEDIO, zorder=6)
            if mod == "enc":
                kernels(ax, W["Ke"].reshape(6, 9), lx, hy, 31, 5,
                        esc["W"][mod])
                if a_g > 0:
                    gK = (g["Ke"].reshape(6, 9) if g is not None
                          else np.zeros((6, 9)))
                    for i in range(6):
                        fx = rx + (i % 3) * 36
                        fy = hy + (i // 3) * 36
                        heat(ax, _div_rgb(gK[i].reshape(3, 3),
                                          esc["g"][mod]), fx, fy, 31, 31,
                             borde=ROJO, lw=1.4, alfa=a_g)
                else:
                    for i in range(6):
                        fx = rx + (i % 3) * 36
                        fy = hy + (i // 3) * 36
                        ax.add_patch(Rectangle((fx, fy), 31, 31, fill=False,
                                               ec=BORDE, lw=1.2, zorder=5))
            else:
                heat(ax, _div_rgb(Wv, esc["W"][mod]), lx, hy, 104, 67)
                if a_g > 0:
                    heat(ax, _div_rgb(gv, esc["g"][mod]), rx, hy, 104, 67,
                         borde=ROJO, lw=1.8, alfa=a_g)
                else:
                    ax.add_patch(Rectangle((rx, hy), 104, 67, fill=False,
                                           ec=BORDE, lw=1.4, zorder=5))
            ny = by + 200
            nx = rx + 52
        if a_g > 0 and g is not None:
            ax.text(nx, ny, f"‖∂L/∂W‖ = {_fmt(_norma(mod, g))}",
                    ha="center", va="center", fontsize=17, fontweight="bold",
                    color=ROJO, alpha=a_g, zorder=6)

    # ---- máscara predicha ---------------------------------------------
    prob = st.get("prob")
    ax.text(qx + ql / 2, qy - 12, "máscara predicha", ha="center",
            va="bottom", fontsize=20, fontweight="bold", color=TINTA)
    rgb = np.ones((n, n, 3))
    if prob is not None:
        a = st.get("prob_alpha", 1.0)
        rgb = superponer(rgb, np.ones((n, n), bool), 0)
        c_ = np.array([0xD7, 0x19, 0x2A]) / 255
        rgb = 1 - (a * prob)[..., None] * (1 - c_)
    ax.imshow(rgb, extent=(qx, qx + ql, qy + ql, qy),
              interpolation="nearest", zorder=1)
    contorno(ax, m, qx, qy, ql, color=TINTA, lw=2.0, ls="--", z=7)
    ax.add_patch(Rectangle((qx, qy), ql, ql, fill=False, ec=TINTA, lw=1.8,
                           zorder=5))
    if prob is not None and st.get("error"):
        err = (prob > 0.5) != m
        rayado(ax, err, qx, qy, ql, lw=1.4, z=6)
    for tipo, (px, py) in st.get("prompts_pred", prompts):
        glifo(ax, tipo, qx + px * ql, qy + py * ql, ms=13)
    nuevo = st.get("clic_nuevo")
    if nuevo is not None:
        tipo, (px, py) = nuevo
        r = 8 + 34 * st.get("pulso_c", 1.0)
        ax.add_patch(Circle((qx + px * ql, qy + py * ql), r, fill=False,
                            ec=ROJO, lw=3, alpha=1 - st.get("pulso_c", 1.0),
                            zorder=8))
        glifo(ax, tipo, qx + px * ql, qy + py * ql, ms=13)
    # leyenda bajo el panel
    ly = qy + ql + 12
    ax.plot([qx + 2, qx + 30], [ly + 11, ly + 11], color=TINTA, lw=2,
            ls="--")
    ax.text(qx + 38, ly + 11, "verdadera", ha="left", va="center",
            fontsize=17, color=GRIS_TXT)
    if st.get("error"):
        ax.add_patch(Rectangle((qx + 2, ly + 34), 26, 18, fill=False,
                               ec=TINTA, lw=1.2))
        rayado(ax, np.ones((1, 1), bool), qx + 2, ly + 30, 22, lw=1.4)
        ax.text(qx + 38, ly + 43, "zona de error", ha="left", va="center",
                fontsize=17, color=GRIS_TXT)
    rot = st.get("rotulo_pred")
    if rot:
        ax.text(qx + ql / 2, ly + 86, rot, ha="center", va="center",
                fontsize=19, fontweight="bold", color=ROJO,
                linespacing=1.2)

    # ---- pérdida -------------------------------------------------------
    lx, ly_, lw__, lh = S_LOSS
    L = st.get("L")
    ax.add_patch(FancyBboxPatch((lx, ly_), lw__, lh, boxstyle="round,pad=0,"
                                "rounding_size=14", fc="white",
                                ec=ROJO if fase in ("loss",) else BORDE,
                                lw=3.4 if fase == "loss" else 2.0, zorder=2))
    ax.text(lx + 20, ly_ + 28, "pérdida", ha="left", va="center",
            fontsize=22, fontweight="bold", color=TINTA, zorder=4)
    ax.text(lx + lw__ - 18, ly_ + 28, "(del juguete)", ha="right",
            va="center", fontsize=16, color=GRIS_MEDIO, zorder=4)
    fx = lx + 20
    ax.text(fx, ly_ + 74, r"$L_{focal} = -\frac{1}{N}\sum\,\alpha_t"
            r"\,(1-p_t)^{\gamma}\,\log p_t$", ha="left",
            va="center", fontsize=17, color=TINTA, zorder=4)
    ax.text(fx, ly_ + 122, r"$L_{dice} = 1 - \dfrac{2\,\sum p\,y}"
            r"{\sum p + \sum y}$", ha="left", va="center", fontsize=18,
            color=TINTA, zorder=4)
    ax.text(fx, ly_ + 172, r"$L = L_{focal} + L_{dice}$", ha="left",
            va="center", fontsize=19, color=TINTA, zorder=4)
    ax.text(fx, ly_ + 202, "p: predicha · y: verdadera", ha="left",
            va="center", fontsize=15, color=GRIS_MEDIO, zorder=4)
    if L is not None:
        la = st.get("L_alpha", 1.0)
        ax.text(fx, ly_ + 236, f"{_fmt(L['lf'])} + {_fmt(L['ld'])}",
                ha="left", va="center", fontsize=19, color=TINTA,
                alpha=la, zorder=4)
        ax.text(fx, ly_ + 274, f"L = {_fmt(L['L'])}", ha="left",
                va="center", fontsize=30, fontweight="bold", color=ROJO,
                alpha=la, zorder=4)

    # ---- curva --------------------------------------------------------
    x0, y0, x1, y1 = S_CURVA
    mm = D["media"]
    ymax = 1.0
    ax.plot([x0, x0, x1], [y0, y1, y1], color=TINTA, lw=1.6, zorder=3)
    ax.text(x0 - 6, y1, "0", ha="right", va="center", fontsize=15,
            color=GRIS_MEDIO)
    ax.text(x0 - 6, y0 + 30, "1", ha="right", va="center", fontsize=15,
            color=GRIS_MEDIO)
    ax.text(x1, y1 + 8, "paso 2.000", ha="right", va="top", fontsize=16,
            color=GRIS_MEDIO)
    ax.text((x0 + x1) / 2, y0 - 10, f"L, media de {VENTANA} pasos",
            ha="center", va="bottom", fontsize=17, color=GRIS_TXT)
    hasta = st.get("curva_hasta", PASO_LUPA)
    k = max(1, hasta - VENTANA + 1)
    xs = x0 + (np.arange(k) + VENTANA - 1) / PASOS1 * (x1 - x0)
    ysv = y1 - mm[:k] / ymax * (y1 - y0 - 30)
    ax.plot(xs, ysv, color=ROJO, lw=2.4, zorder=4)
    ax.plot([xs[-1]], [ysv[-1]], "o", ms=8, color=ROJO, zorder=5)
    ax.text(xs[-1] + 4, ysv[-1] - 10, f"paso {hasta:,}".replace(",", "."),
            ha="left" if hasta < 1500 else "right", va="bottom",
            fontsize=16, color=ROJO, fontweight="bold", zorder=5)

    # ---- actualización ------------------------------------------------
    upd = st.get("upd", 0.0)
    if upd > 0:
        ax.text((dx + qx + ql) / 2, 586, "actualización:  W ← W − η·∂L/∂W"
                f"   (η = {_fmt(ETA1, 1)})", ha="center", va="center",
                fontsize=21, fontweight="bold", color=ROJO, alpha=upd,
                zorder=6)

    # ---- data engine (esquema) -----------------------------------------
    ek = st.get("engine")             # None: apagado; -1: todo; 0..3 nodo
    xs_n, gap = _nodos_x()
    on = ek is not None
    tc = TINTA if on else APAGADO
    t_ = ax.text(xs_n[0], S_BAND_Y, "data engine", ha="left",
                 va="center", fontsize=22, fontweight="bold", color=tc)
    bb = t_.get_window_extent(renderer=ax.figure.canvas.get_renderer())
    ax.text(bb.x1 + 10, S_BAND_Y + 1, "(esquema, no calculado)", ha="left",
            va="center", fontsize=18, color=GRIS_MEDIO if on else APAGADO)
    ax.text(xs_n[-1] + S_NODO_W, S_BAND_Y + 1,
            "SA-1B: 11 M imágenes, más de 1.000 M máscaras", ha="right",
            va="center", fontsize=19, fontweight="bold",
            color=ROJO if on else APAGADO)
    yb = S_NODO_Y
    for i, (t1, t2) in enumerate(S_NODOS):
        xn = xs_n[i]
        activo = on and (ek == i or ek == -1)
        caliente = on and ek == i
        fc = "#FBE1E4" if caliente else (RELLENO if on else "white")
        ec = ROJO if caliente else (BORDE if not on else GRIS_MEDIO)
        ax.add_patch(FancyBboxPatch((xn, yb), S_NODO_W, S_NODO_H,
                                    boxstyle="round,pad=0,rounding_size=14",
                                    fc=fc, ec=ec, lw=3.4 if caliente else 1.8,
                                    zorder=3))
        ct = (ROJO if caliente else TINTA) if on else APAGADO
        ax.text(xn + S_NODO_W / 2, yb + 25, t1, ha="center", va="center",
                fontsize=21, fontweight="bold", color=ct, zorder=4)
        ax.text(xn + S_NODO_W / 2, yb + 53, t2, ha="center", va="center",
                fontsize=21, fontweight="bold", color=ct, zorder=4)
        if i < 3:
            caliente_f = on and ek == i
            flecha(ax, (xn + S_NODO_W + 6, yb + S_NODO_H / 2),
                   (xs_n[i + 1] - 6, yb + S_NODO_H / 2),
                   color=ROJO if caliente_f else (TINTA if on else APAGADO),
                   lw=3.2 if caliente_f else 2.0, ms=18)
    # vuelta: del nodo 4 al nodo 1 por abajo
    yr = yb + S_NODO_H + 34
    cv = on and ek == 3
    colv = ROJO if cv else (TINTA if on else APAGADO)
    a4 = xs_n[3] + S_NODO_W / 2
    a1 = xs_n[0] + S_NODO_W / 2
    ax.plot([a4, a4, a1], [yb + S_NODO_H + 6, yr, yr], color=colv,
            lw=3.2 if cv else 2.0, zorder=2, solid_capstyle="round")
    flecha(ax, (a1, yr), (a1, yb + S_NODO_H + 6), color=colv,
           lw=3.2 if cv else 2.0, ms=18)
    ax.text((a1 + a4) / 2, yr, "  SAM mejor → propone mejores máscaras  ",
            ha="center", va="center", fontsize=19, color=colv,
            fontweight="bold" if cv else "normal", zorder=4,
            bbox=dict(fc="white", ec="none", pad=2))
    if st.get("pie"):
        pie(ax, st["pie"])


def _escalas(D):
    W, g = {}, {}
    todos = [d["W"] for d in D["det"]] + [r["W"] for r in D["rap"]]
    for mod in ("enc", "pr", "dec"):
        W[mod] = max(np.abs(_vista(mod, w)).max() for w in todos) * 0.8
        g[mod] = np.abs(_vista(mod, D["det"][0]["g"])).max() * 0.7
    return dict(W=W, g=g)


def sam_entrenamiento(fps=12):
    D = _cache("sam1", _sam_datos, "v2")
    esc = _escalas(D)
    det, rap = D["det"], D["rap"]
    fig, ax = figura()
    frames, durs = [], []
    ms = 1000 / fps

    def add(n=1, **st):
        _sam_dibujar(ax, D, st, esc)
        fr = capturar(fig)
        for _ in range(n):
            frames.append(fr)
            durs.append(ms)

    d0 = det[0]
    pr0 = d0["prompts"]
    base = dict(W=d0["W"], curva_hasta=PASO_LUPA)
    # 0-1 dato y objetivo
    add(6, fase=None, pie="Un paso de entrenamiento de cerca, el 260 de "
        "2.000 · modelo de juguete, cuentas reales", **base)
    p_dato = ("Dato: imagen + máscara verdadera de un objeto; de la máscara "
              "se samplea un prompt, un punto adentro")
    for k in range(8):
        add(1, fase="dato", pulso=k / 8, pie=p_dato,
            prompts=pr0 if k > 3 else [], **base)
    add(6, fase="dato", prompts=pr0, pie=p_dato, **base)
    # 2 forward
    p_fw = ("forward: image encoder (32×32×6) + prompt encoder (token de "
            "8) → mask decoder → máscara 32×32")
    kw = dict(prompts=pr0, pie=p_fw, **base)
    add(5, fase="fwd", activos=("a_img", "a_pr", "enc", "pr"), **kw)
    add(5, fase="fwd", activos=("a_enc", "a_prd", "dec"), **kw)
    for k in range(1, 6):
        add(1, fase="fwd", activos=("a_dec",), prob=d0["prob"],
            prob_alpha=k / 5, **kw)
    add(6, fase="fwd", prob=d0["prob"], **kw)
    # 3 pérdida
    p_l = (f"pérdida: focal + dice entre la máscara predicha y la "
           f"verdadera → L = {_fmt(d0['L'])}")
    kw = dict(prompts=pr0, prob=d0["prob"], pie=p_l, **base)
    add(5, fase="loss", activos=("a_loss",), **kw)
    for k in range(1, 5):
        add(1, fase="loss", L=d0, L_alpha=k / 4, **kw)
    add(8, fase="loss", L=d0, error=True, **kw)
    # 4 backward
    p_b = ("backward: el gradiente vuelve por el mask decoder y llega a los "
           "pesos de los tres módulos")
    kw = dict(prompts=pr0, prob=d0["prob"], L=d0, error=True, g=d0["g"],
              pie=p_b, **base)
    nb = 15
    for k in range(1, nb + 1):
        t = k / nb
        add(1, fase="bwd", bwd=t, g_alpha_mod={
            "dec": float(np.clip((t - 0.3) / 0.2, 0, 1)),
            "enc": float(np.clip((t - 0.75) / 0.2, 0, 1)),
            "pr": float(np.clip((t - 0.75) / 0.2, 0, 1))}, **kw)
    add(6, fase="bwd", bwd=1.0, g_alpha=1.0, **kw)
    # 5 actualización
    p_u = (f"actualización: W ← W − η·∂L/∂W en los tres módulos "
           f"(η = {_fmt(ETA1, 1)})")
    for k in range(1, 7):
        t = k / 6
        Wt = {kk: (1 - t) * d0["W"][kk] + t * d0["W1"][kk] for kk in d0["W"]}
        add(1, fase="upd", upd=min(1, 2 * t), W=Wt, prompts=pr0,
            prob=d0["prob"], L=d0, error=True, g=d0["g"], g_alpha=1.0,
            curva_hasta=PASO_LUPA, pie=p_u)
    add(6, fase="upd", upd=1.0, W=d0["W1"], prompts=pr0, prob=d0["prob"],
        L=d0, error=True, g=d0["g"], g_alpha=1.0, curva_hasta=PASO_LUPA,
        pie=p_u)
    # 6 rondas con clic corrector
    for r in (1, 2):
        dp, dr = det[r - 1], det[r]
        clic = dp["clic"]
        tipo_err = ("falso positivo → clic negativo" if clic[0] == "neg"
                    else "falso negativo → clic positivo")
        p_c = (f"ronda {r + 1}: clic corrector sampleado en la zona de error "
               f"({tipo_err})")
        kw = dict(W=dp["W1"], curva_hasta=PASO_LUPA, prompts=dp["prompts"],
                  prompts_pred=dp["prompts"], L=dp, error=True)
        for k in range(1, 6):
            add(1, fase="clic", prob=dp["prob"], clic_nuevo=clic,
                pulso_c=k / 5, pie=p_c, **kw)
        add(4 if r == 1 else 2, fase="clic", prob=dp["prob"],
            clic_nuevo=clic, pulso_c=1.0, pie=p_c, **kw)
        pr_r = dr["prompts"]
        p_r = (f"ronda {r + 1}: se repite con {len(pr_r)} prompts: forward, "
               f"pérdida, backward, actualización")
        kw2 = dict(W=dr["W"], curva_hasta=PASO_LUPA, prompts=pr_r,
                   prompts_pred=pr_r, pie=p_r)
        add(2, fase="fwd", activos=("a_img", "a_pr", "enc", "pr", "a_enc",
                                    "a_prd", "dec"), prob=dp["prob"],
            **kw2)
        for k in range(1, 4):
            add(1, fase="fwd", activos=("a_dec",), prob=(1 - k / 3) *
                dp["prob"] + k / 3 * dr["prob"], **kw2)
        add(3, fase="loss", prob=dr["prob"], L=dr, error=True,
            rotulo_pred=f"ronda {r + 1}: L {_fmt(dp['L'])} → "
                        f"{_fmt(dr['L'])}", **kw2)
        for k in range(1, 6):
            add(1, fase="bwd", bwd=k / 5, prob=dr["prob"], L=dr,
                error=True, g=dr["g"], g_alpha=k / 6,
                rotulo_pred=f"ronda {r + 1}: L {_fmt(dp['L'])} → "
                            f"{_fmt(dr['L'])}", **kw2)
        kw2["W"] = dr["W1"]
        add(4 if r == 1 else 8, fase="upd", upd=1.0, prob=dr["prob"], L=dr,
            error=True, g=dr["g"], g_alpha=1.0,
            rotulo_pred=f"ronda {r + 1}: L {_fmt(dp['L'])} → "
                        f"{_fmt(dr['L'])}", **kw2)
    # 7 muchos pasos
    pr_ini = det[0]["prompts"]
    for i, rp in enumerate(rap):
        add(2 if i < len(rap) - 1 else 5, fase="rapido", W=rp["W"],
            prompts=pr_ini, prompts_pred=pr_ini, prob=rp["prob"], L=rp,
            g=rp["g"], g_alpha=1.0, curva_hasta=rp["paso"],
            rotulo_pred="este ejemplo, 1 prompt\n(paso "
                        + f"{rp['paso']:,}".replace(",", ".") + ")",
            pie=f"Muchos pasos con otros ejemplos y prompts: la L media "
                f"baja; este ejemplo, de {_fmt(det[0]['L'])} a "
                f"{_fmt(rap[-1]['L'])}")
    # 8 data engine
    rf = rap[-1]
    fin = dict(W=rf["W"], prompts=pr_ini, prompts_pred=pr_ini,
               prob=rf["prob"], L=rf, g=rf["g"], g_alpha=1.0,
               curva_hasta=PASOS1,
               rotulo_pred="este ejemplo, 1 prompt\n(paso 2.000)")
    p_e = ("data engine (esquema): SAM propone, anotadores corrigen, más "
           "datos, se reentrena SAM")
    add(4, engine=-1, pie=p_e, **fin)
    for vuelta in range(2):
        for i in range(4):
            add(5 if vuelta == 0 else 2, engine=i, pie=p_e, **fin)
    # final
    _sam_dibujar(ax, D, dict(engine=-1, pie="Prompts simulados y clics "
                             "correctores entrenan a SAM; el data engine "
                             "armó SA-1B", **fin), esc)
    final = capturar(fig)
    frames.append(final)
    durs.append(3200)
    plt.close(fig)
    guardar_atomico(frames, durs, final, "sam-entrenamiento")
    print("L por ronda:", [round(d["L"], 3) for d in det],
          "IoU:", [round(d["iou"], 2) for d in det],
          "rápidos:", [round(r["L"], 3) for r in rap])
    if SCRATCH:
        for nombre, i in (("s1-dato", 16), ("s1-loss", 50), ("s1-bwd", 62),
                          ("s1-upd", 78), ("s1-ronda2", 92),
                          ("s1-ronda3", 124), ("s1-rapido", 150),
                          ("s1-engine", 178)):
            frames[min(i, len(frames) - 1)].save(
                os.path.join(SCRATCH, nombre + ".png"))
        final.save(os.path.join(SCRATCH, "s1-final.png"))
    return frames


# =========================================================================
# 2. sam2-entrenamiento
# =========================================================================
N2, NF = 24, 8
OPT2 = ("adam", 0.02)               # optimizador del juguete de video
ETA2 = OPT2[1]
SC_ATT = 1.0
PASOS2 = 1500
PASO_LUPA2 = 0                      # el paso de cerca: el primero
PROMPT_FRAMES = (0, 6)              # frames con prompt en el clip de cerca


class Toy2(Toy):
    """SAM 2 de juguete: el Toy de imagen + memoria.

    memory encoder  : M_t = tanh(F_t·Wm + p_t·wm + bm)          (n², 4)
    memory attention: F_t = E_t + softmax(q kᵀ/√6) v · Wo
                      q = [E_t, PE]·Wq, k = [M_s, PE]·Wk, v = M_s·Wv
    memory bank     : guarda M del frame 1 y de los 6 más recientes (sin
                      pesos). El decoder trabaja sobre F_t.
    """
    Cm, dk = 4, 6
    MODULOS = {"enc": ("Ke", "be"), "pr": ("et", "Wp"),
               "dec": ("Q", "wg", "u", "v", "b"),
               "att": ("Wq", "Wk", "Wv", "Wo"), "menc": ("Wm", "wm", "bm")}

    def __init__(self, n):
        super().__init__(n)
        yy, xx = np.mgrid[0:n, 0:n]
        X, Y = (xx + .5).ravel() / n, (yy + .5).ravel() / n
        self.PE = torch.stack([self.gamma(a, b) for a, b in zip(X, Y)])

    def init(self, seed):
        P = super().init(seed)
        g = torch.Generator().manual_seed(seed + 99)
        C, Cm, dk = self.C, self.Cm, self.dk

        def r(*s, sc=0.1):
            return (torch.randn(*s, generator=g) * sc).requires_grad_()
        P.update(Wm=r(C, Cm, sc=0.3), wm=r(Cm, sc=0.5), bm=r(Cm, sc=0.1),
                 Wq=r(C + 8, dk, sc=0.3), Wk=r(Cm + 8, dk, sc=0.3),
                 Wv=r(Cm, Cm, sc=0.3), Wo=r(Cm, C, sc=0.1))
        return P

    def clip_forward(self, P, imgs, prompts, traza=False):
        n, C = self.n, self.C
        banco, idx, logits, mems = [], [], [], []
        for t, img in enumerate(imgs):
            E = self.encoder(P, img)
            Ef = E.reshape(C, -1).T
            if banco:
                Mem = torch.cat(banco, 0)
                PEm = self.PE.repeat(len(banco), 1)
                q = torch.cat([Ef, self.PE], 1) @ P["Wq"]
                k = torch.cat([Mem, PEm], 1) @ P["Wk"]
                v = Mem @ P["Wv"]
                a = torch.softmax(q @ k.T / np.sqrt(self.dk), 1)
                Ff = Ef + (a @ v) @ P["Wo"]
            else:
                Ff = Ef
            lg = self.decoder(P, Ff.T.reshape(C, n, n), prompts.get(t, []))
            logits.append(lg)
            p = torch.sigmoid(lg).reshape(-1, 1)
            M = torch.tanh(Ff @ P["Wm"] + p * P["wm"] + P["bm"])
            banco.append(M)
            idx.append(t)
            banco, idx = banco[:1] + banco[1:][-6:], idx[:1] + idx[1:][-6:]
            if traza:
                mems.append(M.detach().numpy().reshape(n, n, self.Cm))
        return (logits, mems) if traza else logits


def perdida_clip(logits, ms):
    Ls = [perdida(lg, m) for lg, m in zip(logits, ms)]
    return Ls, sum(x[2] for x in Ls)


def _clip(rng, n=N2, nf=NF, fijo=None):
    """Dos pelotas y un poste; el objetivo es una de las dos. fijo: la
    escena de la animación de inferencia (pelota que cruza detrás del poste
    y otra quieta arriba a la derecha)."""
    yy, xx = np.mgrid[0:n, 0:n]
    XN, YN = (xx + .5) / n, (yy + .5) / n
    fondo = 0.92 - 0.12 * YN
    fondo[YN > 0.72] = 0.74
    if fijo:
        p0, grises, objetivo = 0.50, [0.28, 0.48], 0
        bolas = [(0.12, 0.16, 0.84, 0.60, 0.22), (0.10, 0.80, 0.80, 0.26,
                                                   0.0)]
    else:
        p0 = rng.uniform(0.38, 0.55)
        grises = list(rng.permutation([0.28, 0.48]))
        bolas = []
        for k in range(2):
            r = rng.uniform(0.10, 0.13)
            if k == 0:
                x0, x1 = (0.14, 0.86) if rng.random() < .5 else (0.86, 0.14)
            else:
                x0 = rng.uniform(0.12, 0.88)
                x1 = x0 + rng.uniform(-0.25, 0.25)
            bolas.append((r, x0, x1, rng.uniform(0.3, 0.62),
                          rng.uniform(-0.2, 0.2)))
        objetivo = rng.integers(2)
    poste = (XN > p0) & (XN < p0 + 0.10) & (YN > 0.10)
    imgs, ms = [], []
    for t in range(nf):
        img = fondo + 0.012 * rng.standard_normal((n, n))
        mk = []
        for k, (r, x0, x1, y0, arco) in enumerate(bolas):
            s = t / (nf - 1)
            cx, cy = x0 + (x1 - x0) * s, y0 - arco * np.sin(np.pi * s)
            b = ((XN - cx) ** 2 + (YN - cy) ** 2) < r ** 2
            img[b] = grises[k] + 0.015 * rng.standard_normal(b.sum())
            mk.append(b)
        mk[0] = mk[0] & ~mk[1]
        img[poste] = 0.15
        imgs.append(np.clip(img, 0, 1))
        ms.append(mk[objetivo] & ~poste)
    return imgs, ms


def _prompts_clip(rng, ms, n=N2):
    ys, xs = np.nonzero(ms[0])
    k = np.argmin((xs - xs.mean()) ** 2 + (ys - ys.mean()) ** 2)
    pr = {0: [("pos", _px(n, xs[k], ys[k]))]}
    if rng.random() < 0.5:
        t = int(rng.integers(1, NF))
        ys, xs = np.nonzero(ms[t])
        if len(xs) > 4:
            i = rng.integers(len(xs))
            pr[t] = [("pos", _px(n, xs[i], ys[i]))]
    return pr


def _init2(T, seed=3):
    """Pesos iniciales; q y k más grandes para que la atención no arranque
    uniforme."""
    P = T.init(seed)
    g = torch.Generator().manual_seed(5)
    with torch.no_grad():
        P["Wq"].copy_(torch.randn(P["Wq"].shape, generator=g) * SC_ATT)
        P["Wk"].copy_(torch.randn(P["Wk"].shape, generator=g) * SC_ATT)
    return P


def _sam2_datos():
    rng = np.random.default_rng(1)
    datos = []
    while len(datos) < 300:
        imgs, ms = _clip(rng)
        if ms[0].sum() >= 12:
            datos.append((imgs, ms))
    vimgs, vms = _clip(np.random.default_rng(77), fijo=True)
    vpr = {}
    for t in PROMPT_FRAMES:
        ys, xs = np.nonzero(vms[t])
        k = np.argmin((xs - xs.mean()) ** 2 + (ys - ys.mean()) ** 2)
        vpr[t] = [("pos", _px(N2, xs[k], ys[k]))]
    # verificación de gradientes en float64: clip corto, todos los módulos
    T64 = Toy2(N2)
    P64 = _init2(T64)
    verificar_gradiente(lambda: perdida_clip(
        T64.clip_forward(P64, vimgs[:3], {0: vpr[0], 2: [("neg", (.8, .3))]}),
        vms[:3])[1], P64, list(P64))
    # entrenamiento en float32 (mismo modelo, más rápido)
    torch.set_default_dtype(torch.float32)
    T = Toy2(N2)
    P = _init2(T)
    opt = (torch.optim.Adam(list(P.values()), lr=OPT2[1])
           if OPT2[0] == "adam" else None)

    def mirar(P, paso):
        Pc = {k: v.detach().clone().requires_grad_() for k, v in P.items()}
        lgs, mems = T.clip_forward(Pc, vimgs, vpr, traza=True)
        Ls, L = perdida_clip(lgs, vms)
        L.backward()
        return dict(paso=paso, probs=[torch.sigmoid(x).detach().numpy()
                                      for x in lgs], mems=mems,
                    Lt=[x[2].item() for x in Ls], L=L.item(),
                    W={k: v.detach().numpy().copy() for k, v in Pc.items()},
                    g={k: v.grad.numpy().copy() for k, v in Pc.items()})
    hist, rap = [], []
    ck = set([0, 20, 40, 70, 100, 140, 200, 260, 340, 440, 560, 700, 860,
              1020, 1200, 1350, PASOS2])
    for paso in range(PASOS2 + 1):
        if paso in ck:
            rap.append(mirar(P, paso))
        if paso == PASOS2:
            break
        if paso == PASO_LUPA2:
            imgs, ms, pr = vimgs, vms, vpr
        else:
            imgs, ms = datos[rng.integers(len(datos))]
            pr = _prompts_clip(rng, ms)
        for v in P.values():
            v.grad = None
        Ls, L = perdida_clip(T.clip_forward(P, imgs, pr), ms)
        L.backward()
        if opt is None:
            _sgd(P, OPT2[1])
        else:
            opt.step()
        hist.append(L.item())
        if paso == PASO_LUPA2:
            W1 = {k: v.detach().numpy().copy() for k, v in P.items()}
    torch.set_default_dtype(torch.float64)
    hist = np.array(hist)
    mm = np.convolve(hist, np.ones(VENTANA) / VENTANA, mode="valid")
    return dict(imgs=vimgs, ms=vms, pr=vpr, hist=hist, media=mm, rap=rap,
                W1=W1)


# --- dibujo de SAM 2 ------------------------------------------------------
V_L, V_GAP = 122, 14
V_X0 = 110
V_Y1, V_Y2 = 62, 262                     # filas: video+verdadera, predicha
V2_FT = (50, 494, 90)                     # miniatura del frame t
V2_IE = (172, 478, 240, 122)
V2_MA = (478, 478, 290, 122)
V2_MD = (834, 478, 240, 122)
V2_PE = (1130, 478, 256, 122)
V2_ME = (850, 672, 256, 122)
V2_MB = (50, 672, 720, 148)
V2_LOSS = (1225, 40, 330, 372)
V2_CURVA = (1190, 692, 1545, 790)


def _v_x(i):
    return V_X0 + i * (V_L + V_GAP)


def _vista2(mod, d):
    if mod == "enc":
        return d["Ke"].reshape(6, 9)
    if mod == "pr":
        return np.vstack([d["et"], d["Wp"]]).T
    if mod == "dec":
        return d["Q"]
    if mod == "att":
        return np.vstack([d["Wq"], d["Wk"]]).T
    return np.vstack([d["Wm"], d["wm"][None], d["bm"][None]]).T


def _norma2(mod, g):
    return float(np.sqrt(sum((g[k] ** 2).sum()
                             for k in Toy2.MODULOS[mod])))


def _caja2(ax, mod, geo, titulo, sub, st, esc):
    x, y, w, h = geo
    act = mod in st.get("activos", ())
    caja_mod(ax, x, y, w, h, titulo, None, activa=act, fs=18)
    if sub:
        ax.text(x + w / 2, y + 50, sub, ha="center", va="center",
                fontsize=16, color=GRIS_TXT, zorder=4)
    W, g = st["W"], st.get("g")
    a_g = st.get("g_alpha_mod", {}).get(mod, st.get("g_alpha", 0.0))
    hx, hw = x + 52, w - 70
    y1, y2 = y + 46, y + 72
    ax.text(x + 16, y1 + 9, "W", ha="left", va="center", fontsize=16,
            color=TINTA, zorder=6)
    heat(ax, _div_rgb(_vista2(mod, W), esc["W"][mod]), hx, y1, hw, 18,
         lw=1.0)
    ax.text(x + 16, y2 + 9, "∂L", ha="left", va="center", fontsize=16,
            fontweight="bold", color=ROJO if a_g > 0 else GRIS_MEDIO,
            zorder=6)
    ax.add_patch(Rectangle((hx, y2), hw, 18, fc="white", ec="none",
                           zorder=4.9))
    if a_g > 0 and g is not None:
        heat(ax, _div_rgb(_vista2(mod, g), esc["g"][mod]), hx, y2, hw,
             18, borde=ROJO, lw=1.6, alfa=a_g)
        ax.text(x + w / 2, y + h - 16, f"‖∂L/∂W‖ = {_fmt(_norma2(mod, g))}",
                ha="center", va="center", fontsize=15, fontweight="bold",
                color=ROJO, alpha=a_g, zorder=6)
    else:
        ax.add_patch(Rectangle((hx, y2), hw, 18, fill=False, ec=BORDE,
                               lw=1.0, zorder=5))


def _sam2_dibujar(ax, D, st, esc):
    lienzo(ax)
    imgs, ms, pr = D["imgs"], D["ms"], D["pr"]
    fase = st.get("fase")
    t = st.get("t")
    act = st.get("activos", ())
    gt_a = st.get("gt_alpha", 0.0)
    n_pred = st.get("n_pred", 0)
    probs = st.get("probs")
    n_L = st.get("n_L", 0)
    Lt = st.get("Lt")
    # ---- fila 1: video + máscara verdadera ------------------------------
    ax.text(V_X0, V_Y1 - 14, "video y máscara verdadera",
            ha="left", va="bottom", fontsize=20, fontweight="bold",
            color=TINTA)
    ax.text(_v_x(7) + V_L, V_Y1 - 14, "SAM 2 real · datos: SA-V, videos con "
            "máscaras por frame", ha="right", va="bottom", fontsize=16,
            color=GRIS_MEDIO)
    for i in range(NF):
        x = _v_x(i)
        rgb = a_rgb(imgs[i])
        if gt_a > 0:
            rgb = superponer(rgb, ms[i], 0.75 * gt_a)
        ax.imshow(rgb, extent=(x, x + V_L, V_Y1 + V_L, V_Y1),
                  interpolation="nearest", zorder=1)
        cur = t == i and fase in ("fwd",)
        ax.add_patch(Rectangle((x, V_Y1), V_L, V_L, fill=False,
                               ec=ROJO if cur else TINTA,
                               lw=4.5 if cur else 1.5, zorder=5))
        ax.text(x + V_L / 2, V_Y1 + V_L + 6, f"t = {i + 1}", ha="center",
                va="top", fontsize=18, fontweight="bold" if cur else
                "normal", color=ROJO if cur else TINTA)
        if st.get("prompts_on") and i in pr:
            for tipo, (px, py) in pr[i]:
                glifo(ax, tipo, x + px * V_L, V_Y1 + py * V_L, ms=12)
    # ---- fila 2: máscara predicha y pérdida por frame -------------------
    ax.text(V_X0, V_Y2 - 14, "máscara predicha y pérdida de cada frame",
            ha="left", va="bottom", fontsize=20, fontweight="bold",
            color=TINTA)
    leg_x = _v_x(7) + V_L
    ax.plot([leg_x - 148, leg_x - 120], [V_Y2 - 26, V_Y2 - 26], color=TINTA,
            lw=2, ls="--")
    ax.text(leg_x, V_Y2 - 26, "verdadera", ha="right", va="center",
            fontsize=16, color=GRIS_TXT)
    c_ = np.array([0xD7, 0x19, 0x2A]) / 255
    for i in range(NF):
        x = _v_x(i)
        rgb = np.ones((N2, N2, 3))
        if probs is not None and i < n_pred:
            rgb = 1 - probs[i][..., None] * (1 - c_)
        ax.imshow(rgb, extent=(x, x + V_L, V_Y2 + V_L, V_Y2),
                  interpolation="nearest", zorder=1)
        contorno(ax, ms[i], x, V_Y2, V_L, color=TINTA, lw=1.6, ls="--", z=7)
        cur = t == i and fase == "fwd"
        ax.add_patch(Rectangle((x, V_Y2), V_L, V_L, fill=False,
                               ec=ROJO if cur else TINTA,
                               lw=4.5 if cur else 1.5, zorder=5))
        if Lt is not None and i < n_L:
            ax.text(x + V_L / 2, V_Y2 + V_L + 6, f"L{i + 1} = "
                    f"{_fmt(Lt[i])}", ha="center", va="top", fontsize=17,
                    fontweight="bold", color=ROJO, alpha=st.get("L_alpha",
                                                               1.0))
    # BPTT: el gradiente vuelve hacia frames anteriores
    bw = st.get("bwd", 0.0)
    yb = V_Y2 + V_L + 44
    if bw > 0:
        xa, xb = _v_x(7) + V_L / 2, _v_x(0) + V_L / 2
        tt = np.clip(bw / 0.6, 0, 1)
        flecha(ax, (xa, yb), (xa + tt * (xb - xa), yb), color=ROJO, lw=3,
               ms=18, ls=(0, (4, 3)), zorder=7)
        ax.text((xa + xb) / 2, yb - 2, "  el gradiente vuelve a los frames "
                "anteriores a través de la memoria  ", ha="center",
                va="center", fontsize=17, color=ROJO, fontweight="bold",
                alpha=float(tt), zorder=8,
                bbox=dict(fc="white", ec="none", pad=1))

    # ---- arquitectura ---------------------------------------------------
    tv = t if t is not None else (0 if n_pred == 0 else NF - 1)
    fx, fy, fl = V2_FT
    ax.imshow(a_rgb(imgs[tv]), extent=(fx, fx + fl, fy + fl, fy),
              interpolation="nearest", zorder=1)
    ax.add_patch(Rectangle((fx, fy), fl, fl, fill=False, ec=TINTA, lw=1.6,
                           zorder=5))
    ax.text(fx + fl / 2, fy - 8, f"frame {tv + 1}", ha="center",
            va="bottom", fontsize=19, fontweight="bold", color=TINTA)
    if tv in pr and st.get("prompts_on"):
        for tipo, (px, py) in pr[tv]:
            glifo(ax, tipo, fx + px * fl, fy + py * fl, ms=10)

    def col(k):
        return ROJO if k in act else TINTA
    ie, ma, md, pe, me, mb = V2_IE, V2_MA, V2_MD, V2_PE, V2_ME, V2_MB
    cy = ie[1] + ie[3] / 2
    flecha(ax, (fx + fl + 6, cy), (ie[0] - 6, cy), color=col("enc"))
    flecha(ax, (ie[0] + ie[2] + 6, cy), (ma[0] - 6, cy), color=col("att"))
    flecha(ax, (ma[0] + ma[2] + 6, cy), (md[0] - 6, cy), color=col("dec"))
    con_p = tv in pr
    flecha(ax, (pe[0] - 6, cy), (md[0] + md[2] + 6, cy),
           color=ROJO if "pr" in act else (TINTA if con_p else APAGADO))
    # decoder -> máscara predicha del frame t
    if t is not None and fase == "fwd":
        xm = _v_x(t) + V_L / 2
        caliente = "dec" in act
        ax.annotate("", xy=(xm, V_Y2 + V_L + 34), xytext=(md[0] + md[2] - 40,
                                                         md[1] - 6),
                    arrowprops=dict(arrowstyle="-|>", color=ROJO if caliente
                                    else GRIS_MEDIO, lw=2.6 if caliente
                                    else 1.6, mutation_scale=18,
                                    shrinkA=0, shrinkB=0,
                                    connectionstyle="arc3,rad=0.0"),
                    zorder=6)
    # decoder -> memory encoder -> bank -> attention
    flecha(ax, (md[0] + md[2] - 30, md[1] + md[3] + 8),
           (md[0] + md[2] - 30, me[1] - 8), color=col("menc"))
    ax.text(md[0] + md[2] - 18, (md[1] + md[3] + me[1]) / 2,
            "máscara + features", ha="left", va="center", fontsize=16,
            color=GRIS_TXT)
    ya = me[1] + me[3] / 2
    g_ = "guardar" in act
    flecha(ax, (me[0] - 6, ya), (mb[0] + mb[2] + 6, ya), color=ROJO,
           lw=3.6 if g_ else 2.2)
    ax.text((me[0] + mb[0] + mb[2]) / 2, ya - 8, "se\nguarda", ha="center",
            va="bottom", fontsize=15, color=ROJO, linespacing=1.0,
            fontweight="bold" if g_ else "normal")
    xa = ma[0] + ma[2] / 2
    lee = "att" in act
    flecha(ax, (xa, mb[1] - 6), (xa, ma[1] + ma[3] + 6), color=ROJO,
           lw=3.6 if lee else 2.2)
    ax.text(xa - 12, (mb[1] + ma[1] + ma[3]) / 2 - 10, "condiciona el "
            "frame siguiente", ha="right", va="center", fontsize=16,
            color=ROJO, fontweight="bold" if lee else "normal")
    # backward: flechas rojas punteadas en sentido contrario
    if bw > 0:
        tramos = [((md[0] - 8, cy + 26), (ma[0] + ma[2] + 8, cy + 26), 0.15),
                  ((ma[0] - 8, cy + 26), (ie[0] + ie[2] + 8, cy + 26), 0.35),
                  ((md[0] + md[2] + 8, cy + 26), (pe[0] - 8, cy + 26), 0.15),
                  ((xa + 26, ma[1] + ma[3] + 8), (xa + 26, mb[1] - 8), 0.35),
                  ((mb[0] + mb[2] + 8, ya + 26), (me[0] - 8, ya + 26), 0.55)]
        for a, b, h0 in tramos:
            tt = np.clip((bw - h0) / 0.25, 0, 1)
            if tt > 0:
                flecha(ax, a, (a[0] + tt * (b[0] - a[0]),
                               a[1] + tt * (b[1] - a[1])), color=ROJO,
                       lw=3, ms=16, ls=(0, (4, 3)), zorder=7)
    _caja2(ax, "enc", ie, "image encoder", None, st, esc)
    _caja2(ax, "att", ma, "memory attention", None, st, esc)
    _caja2(ax, "dec", md, "mask decoder", None, st, esc)
    _caja2(ax, "pr", pe, "prompt encoder", None, st, esc)
    _caja2(ax, "menc", me, "memory encoder", None, st, esc)
    ax.text(V2_LOSS[0] + V2_LOSS[2], V2_LOSS[1] + V2_LOSS[3] + 12,
            "prompt solo en\nlos frames 1 y 7", ha="right", va="top",
            fontsize=16, color=GRIS_TXT, linespacing=1.1)
    # memory bank (sin pesos) con las memorias guardadas
    bx, by, bw_, bh = mb
    caja_mod(ax, bx, by, bw_, bh, "", None, activa="att" in act,
             estado="sin_pesos")
    ax.text(bx + 18, by + 20, "memory bank", ha="left", va="center",
            fontsize=20, fontweight="bold", color=TINTA, zorder=4)
    ax.text(bx + bw_ - 18, by + 20, "frame 1 + 6 recientes · 1 de 4 "
            "canales", ha="right", va="center", fontsize=16, color=GRIS_TXT,
            zorder=4)
    banco = st.get("banco", [])
    mems = st.get("mems")
    sl, ddx, ddy, sp = 50, 12, 8, 97
    sx0 = bx + (bw_ - (7 * sp - (sp - sl - ddx))) / 2
    fy = by + 44
    for s_ in range(7):
        xs_ = sx0 + s_ * sp
        ax.add_patch(Rectangle((xs_, fy), sl, sl, fc="white", ec=BORDE,
                               lw=1.2, ls="--", zorder=4))
    for s_, fi in enumerate(banco[:7]):
        xs_ = sx0 + s_ * sp
        if mems is not None:
            prisma(ax, xs_, fy, sl, ddx, ddy, mapa_rgb(mems[fi]),
                   borde=ROJO if s_ == 0 else TINTA,
                   lw=2.4 if s_ == 0 else 1.4, capas=4, z=5)
        ax.text(xs_ + (sl + ddx) / 2, fy + sl + 4, f"memoria\nframe {fi + 1}",
                ha="center", va="top", fontsize=14, linespacing=1.05,
                color=ROJO if s_ == 0 else TINTA, zorder=6)

    # ---- pérdida ---------------------------------------------------------
    lx, ly, lw_, lh = V2_LOSS
    ax.add_patch(FancyBboxPatch((lx, ly), lw_, lh, boxstyle="round,pad=0,"
                                "rounding_size=14", fc="white",
                                ec=ROJO if fase == "loss" else BORDE,
                                lw=3.4 if fase == "loss" else 2.0, zorder=2))
    ax.text(lx + 20, ly + 28, "pérdida", ha="left", va="center", fontsize=22,
            fontweight="bold", color=TINTA, zorder=4)
    ax.text(lx + lw_ - 18, ly + 28, "(del juguete)", ha="right",
            va="center", fontsize=16, color=GRIS_MEDIO, zorder=4)
    ax.text(lx + 20, ly + 72, "por frame:", ha="left", va="center",
            fontsize=17, color=GRIS_TXT, zorder=4)
    ax.text(lx + 20, ly + 104, r"$L_t = L_{focal,t} + L_{dice,t}$",
            ha="left", va="center", fontsize=19, color=TINTA, zorder=4)
    ax.text(lx + 20, ly + 146, "sumada en los 8 frames:", ha="left",
            va="center", fontsize=17, color=GRIS_TXT, zorder=4)
    ax.text(lx + 20, ly + 196, r"$L = \sum_{t=1}^{8}\, L_t$", ha="left",
            va="center", fontsize=21, color=TINTA, zorder=4)
    Ltot = st.get("L")
    if Ltot is not None:
        ax.text(lx + 20, ly + 262, f"L = {_fmt(Ltot)}", ha="left",
                va="center", fontsize=32, fontweight="bold", color=ROJO,
                alpha=st.get("Ltot_alpha", 1.0), zorder=4)
    upd = st.get("upd", 0.0)
    if upd > 0:
        ax.text(lx + 20, ly + 310, "optimizador: Adam", ha="left",
                va="center", fontsize=21, fontweight="bold", color=ROJO,
                alpha=upd, zorder=4)
        ax.text(lx + 20, ly + 342, "usa ∂L/∂W en los 5 módulos", ha="left",
                va="center", fontsize=17, color=ROJO, alpha=upd, zorder=4)

    # ---- curva -----------------------------------------------------------
    x0, y0, x1, y1 = V2_CURVA
    mm = D["media"]
    ymax = float(mm.max()) * 1.05
    ax.plot([x0, x0, x1], [y0, y1, y1], color=TINTA, lw=1.6, zorder=3)
    ax.text(x0 - 8, y0, "L", ha="right", va="top", fontsize=18,
            color=GRIS_TXT)
    ax.text(x1, y1 + 6, f"paso {PASOS2:,}".replace(",", "."), ha="right",
            va="top", fontsize=15, color=GRIS_MEDIO)
    ax.text(x1, y0 - 10, f"media de {VENTANA} pasos", ha="right",
            va="bottom", fontsize=15, color=GRIS_TXT)
    hasta = st.get("curva_hasta", 0)
    k = hasta - VENTANA + 1
    if k >= 1:
        xs = x0 + (np.arange(k) + VENTANA - 1) / PASOS2 * (x1 - x0)
        ysv = y1 - mm[:k] / ymax * (y1 - y0)
        ax.plot(xs, ysv, color=ROJO, lw=2.2, zorder=4)
        ax.plot([xs[-1]], [ysv[-1]], "o", ms=7, color=ROJO, zorder=5)
    else:
        ax.plot([x0], [y0 + 4], "o", ms=7, color=ROJO, zorder=5)
    if k >= 1:
        px_, py_ = xs[-1], ysv[-1]
    else:
        px_, py_ = x0, y0 + 4
    ax.text(px_ + (6 if hasta < 1100 else -6), py_ - 8,
            f"paso {hasta:,}".replace(",", "."),
            ha="left" if hasta < 1100 else "right", va="bottom",
            fontsize=15, color=ROJO, fontweight="bold", zorder=5)
    if st.get("pie"):
        pie(ax, st["pie"])


def mapa_rgb2(a):
    blanco = np.ones(3)
    tinta = np.array([0x22, 0x22, 0x22]) / 255
    return blanco + a[..., None] * 0.88 * (tinta - blanco)


def _escalas2(D):
    W, g = {}, {}
    todos = [r["W"] for r in D["rap"]]
    for mod in Toy2.MODULOS:
        W[mod] = max(np.abs(_vista2(mod, w)).max() for w in todos) * 0.8
        g[mod] = np.abs(_vista2(mod, D["rap"][0]["g"])).max() * 0.7
    return dict(W=W, g=g)


def _memorias(D):
    """Recalcula las memorias (n, n, 4) de cada paso de control con sus
    pesos y elige UN canal: el más correlacionado con la máscara verdadera
    en el último paso. Escala fija [-1, 1] -> [0, 1] para todos los pasos."""
    torch.set_default_dtype(torch.float32)
    T = Toy2(N2)
    todas = []
    for rp in D["rap"]:
        P = {k: torch.tensor(v) for k, v in rp["W"].items()}
        with torch.no_grad():
            lgs, mems = T.clip_forward(P, D["imgs"], D["pr"], traza=True)
        for lg, pb in zip(lgs, rp["probs"]):
            assert np.allclose(torch.sigmoid(lg).numpy(), pb, atol=1e-4)
        todas.append(mems)
    torch.set_default_dtype(torch.float64)
    ms = np.array([m.ravel() for m in D["ms"]], float)
    fin = todas[-1]
    corr = []
    for c in range(Toy2.Cm):
        v = np.array([m[..., c].ravel() for m in fin])
        corr.append(np.corrcoef(v.ravel(), ms.ravel())[0, 1])
    c = int(np.argmax(np.abs(corr)))
    sg = np.sign(corr[c])
    for rp, mems in zip(D["rap"], todas):
        rp["mems"] = [np.clip((sg * m[..., c] + 1) / 2, 0, 1) for m in mems]
    return c, corr[c]


def sam2_entrenamiento(fps=12):
    D = _cache("sam2", _sam2_datos, "v1")
    canal, rc = _memorias(D)
    print(f"canal de memoria mostrado: {canal} (corr. con la máscara "
          f"{rc:+.2f})")
    esc = _escalas2(D)
    rap = D["rap"]
    r0 = rap[0]
    fig, ax = figura()
    frames, durs = [], []
    ms_ = 1000 / fps

    def add(n=1, **st):
        _sam2_dibujar(ax, D, st, esc)
        fr = capturar(fig)
        for _ in range(n):
            frames.append(fr)
            durs.append(ms_)

    base = dict(W=r0["W"], curva_hasta=0)
    add(10, pie="Primer paso de entrenamiento, un clip de 8 frames · modelo "
        "de juguete, cuentas reales", **base)
    p_d = ("Dato: un clip con la máscara verdadera de cada frame; prompt "
           "solo en los frames 1 y 7")
    for k in range(1, 7):
        add(1, gt_alpha=k / 6, prompts_on=k > 3, pie=p_d, **base)
    add(10, gt_alpha=1.0, prompts_on=True, pie=p_d, **base)
    # forward frame a frame
    banco = []
    kw = dict(gt_alpha=1.0, prompts_on=True, probs=r0["probs"],
              mems=r0["mems"], **base)
    for t in range(NF):
        con_p = t in D["pr"]
        p_f = (f"forward, frame {t + 1}: image encoder → memory attention "
               f"(lee el banco) → mask decoder")
        if con_p:
            p_f = (f"forward, frame {t + 1}: image encoder → memory attention "
                   f"→ mask decoder + prompt")
        if t == 0:
            p_f = ("forward, frame 1: image encoder → mask decoder + prompt "
                   "(el banco está vacío)")
        rep = 3 if t == 0 else 2
        b = tuple(banco)
        add(rep, fase="fwd", t=t, activos=("enc",), n_pred=t, banco=b,
            pie=p_f, **kw)
        add(rep, fase="fwd", t=t, activos=("att",) if banco else ("enc",),
            n_pred=t, banco=b, pie=p_f, **kw)
        add(rep, fase="fwd", t=t, activos=("dec", "pr") if con_p else
            ("dec",), n_pred=t + 1, banco=b, pie=p_f, **kw)
        banco = banco + [t]
        banco = banco[:1] + banco[1:][-6:]
        add(rep - 1 if t else rep, fase="fwd", t=t, activos=("menc",
                                                             "guardar"),
            n_pred=t + 1, banco=tuple(banco), pie=p_f, **kw)
    # pérdida por frame
    p_l = ("pérdida: focal + dice por frame contra la máscara verdadera, "
           f"sumada: L = {_fmt(r0['L'])}")
    kw = dict(gt_alpha=1.0, prompts_on=True, probs=r0["probs"],
              mems=r0["mems"], n_pred=NF, banco=tuple(banco), Lt=r0["Lt"],
              **base)
    for k in range(1, NF + 1):
        add(1, fase="loss", n_L=k, pie=p_l, **kw)
    for k in range(1, 5):
        add(1, fase="loss", n_L=NF, L=r0["L"], Ltot_alpha=k / 4, pie=p_l,
            **kw)
    add(8, fase="loss", n_L=NF, L=r0["L"], pie=p_l, **kw)
    # backward
    p_b = ("backward: el gradiente también entrena memory attention y "
           "memory encoder")
    kw.update(n_L=NF, L=r0["L"], g=r0["g"])
    nb = 22
    for k in range(1, nb + 1):
        tt = k / nb
        add(1, fase="bwd", bwd=tt, g_alpha_mod={
            "dec": float(np.clip((tt - 0.10) / 0.15, 0, 1)),
            "pr": float(np.clip((tt - 0.25) / 0.15, 0, 1)),
            "att": float(np.clip((tt - 0.30) / 0.15, 0, 1)),
            "enc": float(np.clip((tt - 0.55) / 0.15, 0, 1)),
            "menc": float(np.clip((tt - 0.70) / 0.15, 0, 1))}, pie=p_b,
            **kw)
    add(10, fase="bwd", bwd=1.0, g_alpha=1.0, pie=p_b, **kw)
    # actualización
    p_u = ("actualización: optimizador Adam, con ∂L/∂W, en los cinco "
           "módulos a la vez")
    W1 = D["W1"]
    for k in range(1, 9):
        tt = k / 8
        Wt = {kk: (1 - tt) * r0["W"][kk] + tt * W1[kk] for kk in W1}
        st = dict(kw)
        st.update(W=Wt, upd=min(1, 2 * tt), g_alpha=1.0, pie=p_u)
        add(1, **st)
    st = dict(kw)
    st.update(W=W1, upd=1.0, g_alpha=1.0, pie=p_u)
    add(8, **st)
    # muchos pasos
    for i, rp in enumerate(rap[1:]):
        add(2 if i < len(rap) - 2 else 6, gt_alpha=1.0, prompts_on=True,
            probs=rp["probs"], mems=rp["mems"], n_pred=NF, n_L=NF,
            banco=tuple(banco), Lt=rp["Lt"], L=rp["L"], W=rp["W"],
            g=rp["g"], g_alpha=1.0, curva_hasta=rp["paso"],
            pie=f"Muchos pasos con otros clips: en este clip L baja de "
                f"{_fmt(r0['L'])} a {_fmt(rp['L'])}")
    rf = rap[-1]
    _sam2_dibujar(ax, D, dict(gt_alpha=1.0, prompts_on=True,
                              probs=rf["probs"], mems=rf["mems"],
                              n_pred=NF, n_L=NF, banco=tuple(banco),
                              Lt=rf["Lt"], L=rf["L"], W=rf["W"], g=rf["g"],
                              g_alpha=1.0, curva_hasta=PASOS2,
                              pie="Pérdida sumada en los 8 frames; tras "
                                  "1.500 pasos sigue a la pelota, pero se "
                                  "cuela la otra"),
                  esc)
    final = capturar(fig)
    frames.append(final)
    durs.append(3200)
    plt.close(fig)
    guardar_atomico(frames, durs, final, "sam2-entrenamiento")
    print("L por paso de control:", [(r["paso"], round(r["L"], 2))
                                     for r in rap])
    if SCRATCH:
        for nombre, i in (("s2-dato", 22), ("s2-fwd", 60), ("s2-loss", 100),
                          ("s2-bwd", 118), ("s2-upd", 140),
                          ("s2-rapido", 160)):
            frames[min(i, len(frames) - 1)].save(
                os.path.join(SCRATCH, nombre + ".png"))
        final.save(os.path.join(SCRATCH, "s2-final.png"))
    return frames


TAREAS = {"sam-entrenamiento": sam_entrenamiento,
          "sam2-entrenamiento": sam2_entrenamiento}

if __name__ == "__main__":
    for nombre in (sys.argv[1:] or TAREAS):
        TAREAS[nombre]()
