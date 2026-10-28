#!/usr/bin/env python3
"""Animación del ENTRENAMIENTO de Stable Diffusion (grupo "sd").

Salida en ../../images/:
  sd-entrenamiento.gif   un paso de entrenamiento completo y después muchos:
                         par (imagen, texto) -> VAE encoder y CLIP congelados ->
                         z0 64x64x4 y embedding 77x768; se sortean t y ε;
                         z_t = √ᾱ_t·z0 + √(1−ᾱ_t)·ε; la U-Net predice ε̂;
                         L = ‖ε − ε̂‖²; backward solo hasta la U-Net; SGD;
                         repetición con otros pares y otros t; un paso con el
                         texto vacío (classifier-free guidance)
  sd-entrenamiento.png   cuadro final fijo (respaldo para PDF)

Mismo dibujo de bloques que pipeline-sd-en-vivo.gif (gen_anim_pipeline.py, del que
se importan helpers y la imagen del faro sin modificarlo).

Qué es real y qué es de juguete (todo en numpy, calculado):
- schedule: el de SD (betas "scaled linear" 0,00085 -> 0,012, T = 1000).
- "VAE encoder" congelado: un encoder lineal fijo 512x512x3 -> 64x64x4 (bloques
  de 8x8: luminancia, dos diferencias de color y detalle), el mismo de la
  animación del pipeline, con normalización fija para todo el dataset.
- "CLIP" congelado: a cada token le corresponde un vector fijo de 768; el texto
  queda en 77x768 (<inicio>, palabras, <fin> y relleno).
- U-Net de juguete, entrenada de verdad con SGD sobre 4 pares:
      ε̂ = c1(t)·z_t − c2(t)·W·ē
  ē = promedio de los vectores de los tokens del texto (sin el relleno),
  W de 16.384x768 (arranca en cero), [log c1, log c2] = MLP(sinusoides de t).
  Los gradientes analíticos se verifican por diferencias finitas.
- en una fracción de los pasos el texto se reemplaza por "" (texto vacío). El
  corpus de la Talk no da el número de esa fracción, así que la imagen no lo dice;
  el juguete usa P_VACIO.

Uso: ~/miniconda3/bin/python3 gen_train_sd.py   (numpy, matplotlib, pillow; el
python3 del sistema no tiene numpy). ANIM_SOLO=5,40,-1 y ANIM_DEBUG_DIR=<carpeta>
renderizan solo esos estados, para revisar el layout.
"""
import os
import sys
import zlib

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")    # vectores chicos: un hilo es más rápido
import numpy as np  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import gen_animaciones_conv as base  # noqa: E402  (estilo y captura)
import gen_anim_pipeline as pipe  # noqa: E402     (helpers de dibujo, faro)

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Arc, FancyBboxPatch, Rectangle  # noqa: E402

TINTA, ROJO, ROJO_CLARO = base.TINTA, base.ROJO, base.ROJO_CLARO
RELLENO, GRIS_MEDIO = base.RELLENO, base.GRIS_MEDIO
BORDE_GRIS = pipe.BORDE_GRIS
OUT = base.OUT
PX_W, PX_H = pipe.PX_W, pipe.PX_H
FPS = pipe.FPS

PASOS = 1500          # pasos de entrenamiento del juguete
P_VACIO = 0.15        # fracción de pasos con texto vacío (no se muestra)
ETA_W, ETA_T = 30.0, 0.02
SEED = 3
T_UNO = 517           # timestep del primer paso que se muestra


# =========================================================================
# datos
# =========================================================================
N = 512


def img_circulo(n=N):
    yy, xx = np.mgrid[0:n, 0:n] / n
    r = np.hypot(xx - 0.5, yy - 0.5)
    d = np.clip((0.28 - r) / 0.004, 0, 1)[..., None]
    fondo = np.array([0.94, 0.93, 0.92])
    rojo = np.array([0xD7, 0x19, 0x2A]) / 255
    return fondo * (1 - d) + rojo * d


def img_montanas(n=N):
    yy, xx = np.mgrid[0:n, 0:n] / n
    t = np.clip(yy / 0.7, 0, 1)[..., None]
    img = np.array([0.55, 0.75, 0.95]) * (1 - t) + \
        np.array([0.95, 0.85, 0.70]) * t
    d = np.hypot(xx - 0.70, yy - 0.28)
    s = np.clip((0.11 - d) / 0.005, 0, 1)[..., None]
    img = img * (1 - s) + np.array([1.0, 0.85, 0.30]) * s
    m1 = yy > 0.30 + 1.2 * np.abs(xx - 0.32)
    m2 = yy > 0.45 + 1.0 * np.abs(xx - 0.78)
    img[m2] = np.array([0.42, 0.45, 0.50])
    img[m1] = np.array([0.30, 0.33, 0.38])
    img[m1 & (yy < 0.42)] = np.array([0.97, 0.97, 0.98])
    img[yy > 0.86] = np.array([0.35, 0.55, 0.30])
    return img


def img_cuadrado(n=N):
    yy, xx = np.mgrid[0:n, 0:n] / n
    img = np.ones((n, n, 3)) * np.array([0.94, 0.93, 0.92])
    q = (np.abs(xx - 0.5) < 0.26) & (np.abs(yy - 0.5) < 0.26)
    img[q] = np.array([0.15, 0.35, 0.75])
    return img


# (texto, líneas para la caja, imagen)
PARES = [
    ("un faro rojo junto al mar", ("«un faro rojo", "junto al mar»"),
     pipe.imagen_faro()),
    ("un círculo rojo", ("«un círculo", "rojo»"), img_circulo()),
    ("un sol sobre montañas", ("«un sol sobre", "montañas»"), img_montanas()),
    ("un cuadrado azul", ("«un cuadrado", "azul»"), img_cuadrado()),
]
for _t, _l, _im in PARES:
    assert _im.shape == (512, 512, 3)


def canales(img):
    """Encoder lineal fijo (el de la animación del pipeline): 512x512x3 ->
    64x64x4 = luminancia, r-g, (r+g)/2-b y detalle, por bloques de 8x8."""
    p = img.reshape(64, 8, 64, 8, 3).mean((1, 3))
    r, g, b = p[..., 0], p[..., 1], p[..., 2]
    lum = (r + g + b) / 3
    blur = (np.roll(lum, 1, 0) + np.roll(lum, -1, 0) + np.roll(lum, 1, 1)
            + np.roll(lum, -1, 1)) / 4
    return np.stack([lum, r - g, (r + g) / 2 - b, lum - blur], -1)


_CH = [canales(im) for _t, _l, im in PARES]
MU = np.mean([c.mean((0, 1)) for c in _CH], 0)          # normalización fija
SD = np.sqrt(np.mean([((c - MU) ** 2).mean((0, 1)) for c in _CH], 0))
Z0 = [(c - MU) / SD for c in _CH]
assert all(z.shape == (64, 64, 4) and z.size == 16_384 for z in Z0)

BETAS = np.linspace(0.00085 ** 0.5, 0.012 ** 0.5, 1000) ** 2   # SD
ABAR = np.cumprod(1 - BETAS)                                   # ᾱ_t, t=1..1000


def ab(t):
    return ABAR[t - 1]


def vec_token(tok, d=768):
    rng = np.random.default_rng(zlib.crc32(tok.encode()))
    return rng.standard_normal(d)


def tokens(texto):
    return ["<inicio>"] + texto.split() + ["<fin>"]


def embedding(texto):
    """'CLIP' congelado de juguete: 77x768 (tokens + relleno)."""
    tk = tokens(texto)
    filas = [vec_token(t) for t in tk] + \
        [vec_token("<relleno>")] * (77 - len(tk))
    E = np.array(filas)
    assert E.shape == (77, 768)
    return E, len(tk)


def e_media(texto):
    E, n = embedding(texto)
    return E[:n].mean(0)


CLAVES = [p[0] for p in PARES] + [""]          # índice 4 = texto vacío
EBM = np.array([e_media(k) for k in CLAVES])   # 5 x 768


def tira_emb(texto):
    """Tira de 12x77 para dibujar el embedding (12 de las 768 dimensiones)."""
    E, _n = embedding(texto)
    return np.tanh(E[:, ::64][:, :12].T * 0.8)


# =========================================================================
# U-Net de juguete: ε̂ = c1(t)·z_t − c2(t)·W·ē
# =========================================================================
def phi(t):
    per = 4000 / 2 ** np.arange(6)                  # periodos 4000 ... 125
    w = 2 * np.pi / per
    return np.concatenate([np.sin(t * w), np.cos(t * w),
                           [np.log(t) / 7 - 0.5, np.sqrt(t / 1000) - 0.5]])


NF = len(phi(1))
# muestra fija de W y de ∂L/∂W para dibujar: 14 posiciones del latente x 24
# dimensiones del embedding
_R = np.random.default_rng(5)
FILAS_W = np.sort(_R.choice(16_384, 14, replace=False))
COLS_W = np.sort(_R.choice(768, 24, replace=False))


class UNetJuguete:
    def __init__(self, seed=0):
        rng = np.random.default_rng(seed)
        self.A = rng.standard_normal((32, NF)) * 0.7
        self.a0 = np.zeros(32)
        self.B = rng.standard_normal((2, 32)) * 0.05
        self.b0 = np.array([np.log(0.1), np.log(0.5)])
        # W (16.384 x 768) arranca en cero y cada paso de SGD le suma
        # -η·outer(∂L/∂m, ē); como ē es uno de 5 vectores, W = M·EBM exacto.
        self.M = np.zeros((16_384, len(CLAVES)))

    def W_muestra(self):
        return self.M[FILAS_W] @ EBM[:, COLS_W]

    def forward(self, zt, t, c):
        f = phi(t)
        h = np.tanh(self.A @ f + self.a0)
        g = np.exp(self.B @ h + self.b0)          # c1, c2
        e = EBM[c]
        m = self.M @ (EBM @ e)                    # W·ē
        eh = g[0] * zt.ravel() - g[1] * m
        return eh, dict(f=f, h=h, g=g, m=m, e=e, z=zt.ravel())

    @staticmethod
    def perdida(eh, eps):
        r = eh - eps.ravel()
        return (r ** 2).mean()                    # L = ‖ε − ε̂‖² (MSE)

    def gradientes(self, zt, t, c, eps):
        eh, k = self.forward(zt, t, c)
        r = eh - eps.ravel()
        L = (r ** 2).mean()
        d = 2 * r / r.size                        # ∂L/∂ε̂
        dlg = np.array([d @ k["z"], -(d @ k["m"])]) * k["g"]
        gr = dict(B=np.outer(dlg, k["h"]), b0=dlg)
        dpre = (self.B.T @ dlg) * (1 - k["h"] ** 2)
        gr["A"] = np.outer(dpre, k["f"])
        gr["a0"] = dpre
        gr["dm"] = -k["g"][1] * d                 # ∂L/∂(W·ē);  ∂L/∂W = dm ⊗ ē
        return L, gr, eh, k

    def actualizar(self, gr, c, eta_w, eta_t):
        """SGD: W ← W − η·∂L/∂W (y lo mismo para la MLP de t)."""
        self.M[:, c] -= eta_w * gr["dm"]
        for n in ("A", "a0", "B", "b0"):
            setattr(self, n, getattr(self, n) - eta_t * gr[n])


def verificar_gradientes():
    """Diferencias finitas contra los gradientes analíticos."""
    rng = np.random.default_rng(3)
    mod = UNetJuguete()
    mod.M = rng.standard_normal(mod.M.shape) * 0.02
    eps = rng.standard_normal((64, 64, 4))
    t = 300
    zt = np.sqrt(ab(t)) * Z0[1] + np.sqrt(1 - ab(t)) * eps
    L, gr, _eh, k = mod.gradientes(zt, t, 1, eps)
    h = 1e-6
    for n, idx in (("A", (3, 5)), ("a0", (7,)), ("B", (1, 4)), ("b0", (0,))):
        P = getattr(mod, n)
        P[idx] += h
        Lp = mod.perdida(mod.forward(zt, t, 1)[0], eps)
        P[idx] -= 2 * h
        Lm = mod.perdida(mod.forward(zt, t, 1)[0], eps)
        P[idx] += h
        num = (Lp - Lm) / (2 * h)
        assert abs(num - gr[n][idx]) < 1e-6 * max(1, abs(num)), (n, num)
    # ∂L/∂W_ij = dm_i · ē_j : perturbar W_ij cambia m_i en ±h·ē_j
    for i, j in ((100, 3), (9000, 700)):
        eh0, k0 = mod.forward(zt, t, 1)
        def L_con(delta):
            m = k0["m"].copy()
            m[i] += delta * k0["e"][j]
            return mod.perdida(k0["g"][0] * k0["z"] - k0["g"][1] * m, eps)
        num = (L_con(h) - L_con(-h)) / (2 * h)
        ana = gr["dm"][i] * k0["e"][j]
        assert abs(num - ana) < 1e-9 + 1e-5 * abs(ana), (i, j, num, ana)
    return True


def entrenar(guardar=None):
    """Entrena la U-Net de juguete paso a paso (un par por paso). Es
    determinístico: con guardar = {pasos} se repite la misma corrida y se
    guarda lo necesario para dibujar esos pasos."""
    rng = np.random.default_rng(SEED)
    mod = UNetJuguete()
    log = []
    fotos = {}
    for s in range(PASOS):
        dec = 0.5 * (1 + np.cos(np.pi * s / PASOS)) * 0.9 + 0.1
        i = int(rng.integers(4))
        t = int(rng.integers(1, 1001))
        eps = rng.standard_normal((64, 64, 4))
        vacio = s > 0 and rng.random() < P_VACIO
        if s == 0:
            i, t = 0, T_UNO
        c = 4 if vacio else i
        zt = np.sqrt(ab(t)) * Z0[i] + np.sqrt(1 - ab(t)) * eps
        W_antes = mod.W_muestra()
        L, gr, eh, k = mod.gradientes(zt, t, c, eps)
        assert np.isfinite(L)
        dW = np.outer(gr["dm"][FILAS_W], EBM[c][COLS_W])
        mod.actualizar(gr, c, ETA_W * dec, ETA_T * dec)
        log.append((i, t, vacio, L))
        if guardar is not None and s not in guardar:
            continue
        fotos[s] = dict(i=i, t=t, vacio=vacio, L=L, eps=eps, zt=zt,
                        eh=eh.reshape(64, 64, 4), W0=W_antes, dW=dW,
                        W1=mod.W_muestra(), gnorm=np.linalg.norm(gr["dm"]) *
                        np.linalg.norm(EBM[c]))
    # el primer par otra vez, con la U-Net ya entrenada (mismo t, mismo ε)
    f0 = fotos[0]
    L, gr, eh, k = mod.gradientes(f0["zt"], f0["t"], 0, f0["eps"])
    final = dict(f0, L=L, eh=eh.reshape(64, 64, 4), W0=mod.W_muestra(),
                 W1=mod.W_muestra(),
                 dW=np.outer(gr["dm"][FILAS_W], EBM[0][COLS_W]),
                 gnorm=np.linalg.norm(gr["dm"]) * np.linalg.norm(EBM[0]))
    return mod, log, fotos, final


def elegir_pasos(log):
    """Pasos que se muestran en la repetición rápida (todos reales)."""
    def cerca(objetivo, cond):
        orden = sorted(range(len(log)), key=lambda s: abs(s - objetivo))
        for s in orden:
            i, t, vac, _L = log[s]
            if cond(i, t, vac):
                return s
        raise ValueError(objetivo)
    usados = set()

    def toma(obj, cond):
        s = cerca(obj, lambda i, t, v: cond(i, t, v) and not v)
        usados.add(s)
        return s
    reps = [toma(2, lambda i, t, v: i != 0 and 300 < t < 800),
            toma(12, lambda i, t, v: t < 150),          # t chico
            toma(60, lambda i, t, v: t > 870),          # t grande
            toma(250, lambda i, t, v: i == 3 and 250 < t < 700),
            toma(700, lambda i, t, v: i == 2 and t < 200),
            toma(1150, lambda i, t, v: i == 1 and 350 < t < 700)]
    vac = cerca(1350, lambda i, t, v: v and i == 0 and 350 < t < 650)
    return reps, vac


# =========================================================================
# dibujo
# =========================================================================
def div_rgb(M, escala):
    """Mapa divergente fijo: rojo positivo, tinta negativo, blanco cero."""
    v = np.clip(M / escala, -1, 1)[..., None]
    blanco = np.ones(3)
    rojo = np.array([0xD7, 0x19, 0x2A]) / 255
    tinta = np.array([0x22, 0x22, 0x22]) / 255
    return np.where(v >= 0, blanco + v * (rojo - blanco),
                    blanco + (-v) * 0.85 * (tinta - blanco))


def gris(e):
    return np.repeat(np.clip(0.5 + 0.22 * e, 0, 1)[..., None], 3, 2)


def calor(err, vmax=2.0):
    """(ε − ε̂)² promedio en los 4 canales -> blanco..rojo, escala fija."""
    v = np.clip(err / vmax, 0, 1)[..., None]
    rojo = np.array([0xD7, 0x19, 0x2A]) / 255
    return np.ones(3) + v * (rojo - np.ones(3))


def vista(lat):
    return pipe.vista_rgb(lat, (MU, SD))


class Escena(pipe.Escena):
    # geometría (px, y hacia abajo)
    TXT = (50, 310, 40, 160)
    CLIP = (370, 660, 40, 160)
    EMB = (720, 900, 40, 160)
    IMG = (80, 280, 235, 435)
    VAE = (370, 660, 285, 385)
    Z0 = (720, 860, 265, 405)
    MAS = (920, 335)
    ZT = (980, 1120, 265, 405)
    UNET = (1180, 1550, 40, 470)
    TBOX = (990, 1150, 470, 560)
    EPS = (845, 595)                # x0, y0 de la pila de ε
    CARTA, OFF = 110, 12
    LOSS_Y = (600, 705)
    CARDS = [(1195, 1300), (1318, 1423), (1441, 1546)]
    CURVA = (100, 740, 580, 770)    # x0, x1, y0 (arriba), y1 (abajo)
    WPAN = (1202, 1357, 258, 368)   # panel de W
    GPAN = (1375, 1530, 258, 368)   # panel de ∂L/∂W
    XG = 1432                       # columna del gradiente (L -> ∂L/∂W)

    def __init__(self, log, escala_dW, escala_W):
        self.log = log
        self.Ls = np.array([x[3] for x in log])
        # media móvil de los últimos 150 pasos (la línea roja de la curva)
        cs = np.concatenate([[0], np.cumsum(self.Ls)])
        k = np.arange(1, len(self.Ls) + 1)
        ini = np.maximum(0, k - 150)
        self.ema = (cs[k] - cs[ini]) / (k - ini)
        self.esc_dW = escala_dW
        self.esc_W = escala_W

    # ---- primitivas extra -------------------------------------------------
    def candado(self, ax, x, y, s=24, col=GRIS_MEDIO):
        """Candado con el cuerpo en (x, y) arriba-izquierda, ancho s."""
        ax.add_patch(FancyBboxPatch((x, y), s, s * 0.78,
                                    boxstyle="round,pad=0,rounding_size=3",
                                    fc=col, ec=col, lw=1, zorder=7))
        ax.add_patch(Arc((x + s / 2, y), s * 0.66, s * 0.9, theta1=0,
                         theta2=180, color=col, lw=3.2, zorder=7))
        ax.plot([x + s / 2], [y + s * 0.4], "o", color="white", ms=3.5,
                zorder=8)

    def pila(self, ax, x0, y0, L, o, lat, on=False):
        for k in range(4):            # la carta 0 adelante
            j = 3 - k
            xx, yy = x0 + j * o, y0 + (3 - j) * o
            self.imagen(ax, gris(lat[..., j]), xx, xx + L, yy, yy + L,
                        z=4 + k * 0.01)
            ax.add_patch(Rectangle((xx, yy), L, L, fill=False,
                                   ec=ROJO if (on and j == 0) else TINTA,
                                   lw=3 if (on and j == 0) else 1.4,
                                   zorder=4.005 + k * 0.01))

    def vacia(self, ax, x0, x1, y0, y1):
        ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fc="white",
                               ec=BORDE_GRIS, lw=1.5, ls=(0, (5, 4)),
                               zorder=2))

    def grad(self, ax, pts, prog=1.0, z=8):
        """Camino del gradiente (rojo, punteado) recorrido hasta prog."""
        pts = np.array(pts, float)
        seg = np.hypot(*np.diff(pts, axis=0).T)
        tot = seg.sum()
        d = prog * tot
        out = [pts[0]]
        for k, Lk in enumerate(seg):
            if d >= Lk:
                out.append(pts[k + 1])
                d -= Lk
            else:
                out.append(pts[k] + (pts[k + 1] - pts[k]) * d / Lk)
                break
        out = np.array(out)
        ax.plot(out[:, 0], out[:, 1], color=ROJO, lw=3, ls=(0, (4, 3)),
                zorder=z, solid_capstyle="butt")
        if 0 < prog < 1:
            ax.plot(*out[-1], "o", ms=15, color=ROJO, mec="white", mew=2,
                    zorder=z + 0.5)
        elif prog >= 1:
            a, b = out[-2], out[-1]
            ax.annotate("", xy=b, xytext=a + (b - a) * 0.999 - (b - a) /
                        max(np.hypot(*(b - a)), 1) * 16, zorder=z,
                        arrowprops=dict(arrowstyle="-|>", color=ROJO, lw=3,
                                        mutation_scale=22, shrinkA=0,
                                        shrinkB=0))

    def corte(self, ax, x, y):
        s = 13
        for sg in (1, -1):
            ax.plot([x - s, x + s], [y - s * sg, y + s * sg], color=ROJO,
                    lw=5, zorder=9, solid_capstyle="round")

    # ---- escena -------------------------------------------------------------
    def dibujar(self, st):
        fig = plt.figure(figsize=(16, 9), dpi=100)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, PX_W)
        ax.set_ylim(PX_H, 0)
        ax.axis("off")
        act = st.get("activos", set())
        fl = st.get("flechas", set())
        par = PARES[st.get("par", 0)]
        vacio = st.get("vacio", False)
        f = st.get("foto")          # datos del paso que se dibuja

        # ------------------------------------------------ texto -> CLIP -> emb
        x0, x1, y0, y1 = self.TXT
        ym = (y0 + y1) / 2
        on = "txt" in act
        if on:
            self.halo(ax, x0, x1, y0, y1)
        self.caja(ax, x0, x1, y0, y1, "white", ROJO if (on or vacio) else
                  TINTA, lw=3.5 if (on or vacio) else 2.4, r=50)
        cx = (x0 + x1) / 2
        if vacio:
            self.texto(ax, cx, y0 + 34, "texto vacío", fs=19,
                       fontweight="bold", color=ROJO)
            self.texto(ax, cx, y0 + 80, "«»", fs=26, color=ROJO)
        else:
            self.texto(ax, cx, y0 + 30, "texto", fs=19, fontweight="bold")
            self.texto(ax, cx, y0 + 64, par[1][0], fs=19, style="italic")
            self.texto(ax, cx, y0 + 96, par[1][1], fs=19, style="italic")

        def congelada(xr, yr, titulo, sub, nombre):
            x0, x1 = xr
            y0, y1 = yr
            on = nombre in act
            if on:
                self.halo(ax, x0, x1, y0, y1)
            self.caja(ax, x0, x1, y0, y1, RELLENO, TINTA if on else
                      BORDE_GRIS, lw=3 if on else 2.0)
            cx, ym = (x0 + x1) / 2, (y0 + y1) / 2
            self.texto(ax, cx, ym - 20, titulo, fs=20, fontweight="bold")
            self.candado(ax, cx - 72, ym + 8, s=22)
            self.texto(ax, cx - 40, ym + 20, sub, fs=18, color=GRIS_MEDIO,
                       ha="left")

        congelada(self.CLIP[:2], self.CLIP[2:], "CLIP text encoder",
                  "congelado", "clip")
        x0, x1, y0, y1 = self.EMB
        on = "emb" in act
        self.caja(ax, x0, x1, y0, y1, "white", ROJO if on else BORDE_GRIS,
                  lw=3 if on else 2.0, ls=(0, (5, 4)))
        self.texto(ax, (x0 + x1) / 2, y0 + 24, "embedding", fs=19)
        cols = st.get("emb_cols", 77)
        tira = np.ones((12, 77, 3)) * np.array([0xF1, 0xED, 0xEC]) / 255
        if cols > 0:
            v = tira_emb("" if vacio else par[0])[:, :cols]
            pos = np.clip(v, 0, 1)[..., None]
            neg = np.clip(-v, 0, 1)[..., None]
            r_ = np.array([0xD7, 0x19, 0x2A]) / 255
            t_ = np.array([0x22, 0x22, 0x22]) / 255
            tira[:, :cols] = 1 + pos * (r_ - 1) + neg * 0.8 * (t_ - 1)
        self.imagen(ax, tira, x0 + 16, x1 - 16, y0 + 44, y0 + 80)
        ax.add_patch(Rectangle((x0 + 16, y0 + 44), x1 - x0 - 32, 36,
                               fill=False, ec=BORDE_GRIS, lw=1, zorder=5))
        self.texto(ax, (x0 + x1) / 2, y0 + 100, "77 × 768", fs=20,
                   family="DejaVu Sans Mono", color=ROJO if on else TINTA)
        self.flecha(ax, [(self.TXT[1], ym), (self.CLIP[0] - 2, ym)],
                    "t-c" in fl)
        self.flecha(ax, [(self.CLIP[1], ym), (self.EMB[0] - 2, ym)],
                    "c-e" in fl)
        ux0, ux1, uy0, uy1 = self.UNET
        self.flecha(ax, [(self.EMB[1], ym), (ux0 - 3, ym)], "e-u" in fl)

        # ------------------------------------------------ imagen -> VAE -> z0
        ix0, ix1, iy0, iy1 = self.IMG
        icx = (ix0 + ix1) / 2
        self.texto(ax, icx, iy0 - 20, "imagen 512×512×3", fs=18,
                   family="DejaVu Sans Mono", color=TINTA)
        self.imagen(ax, par[2], ix0, ix1, iy0, iy1, interp="antialiased")
        ax.add_patch(Rectangle((ix0, iy0), ix1 - ix0, iy1 - iy0, fill=False,
                               ec=ROJO if "img" in act else TINTA,
                               lw=3 if "img" in act else 1.6, zorder=5))
        self.texto(ax, icx, iy1 + 26, "par del dataset", fs=17,
                   color=GRIS_MEDIO)
        congelada(self.VAE[:2], self.VAE[2:], "VAE encoder", "congelado",
                  "vae")
        vym = (self.VAE[2] + self.VAE[3]) / 2
        self.flecha(ax, [(ix1 + 4, vym), (self.VAE[0] - 2, vym)], "i-v" in fl)
        zx0, zx1, zy0, zy1 = self.Z0
        self.flecha(ax, [(self.VAE[1], vym), (zx0 - 3, vym)], "v-z" in fl)

        def latente(rect, lat, nombre, rotulo):
            x0, x1, y0, y1 = rect
            on = nombre in act
            if on:
                self.halo(ax, x0, x1, y0, y1)
            if lat is None:
                self.vacia(ax, x0, x1, y0, y1)
            else:
                self.imagen(ax, vista(lat), x0, x1, y0, y1)
                ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0,
                                       fill=False, ec=ROJO if on else TINTA,
                                       lw=3 if on else 1.6, zorder=5))
            cx = (x0 + x1) / 2
            self.texto(ax, cx - 4, y1 + 22, rotulo, fs=20,
                       fontweight="bold", color=ROJO if on else TINTA,
                       ha="right")
            self.texto(ax, cx + 4, y1 + 22, "64×64×4", fs=18,
                       family="DejaVu Sans Mono", ha="left")

        z0 = Z0[st.get("par", 0)] if st.get("z0_on") else None
        latente(self.Z0, z0, "z0", "z0")
        ztl = f["zt"] if (f is not None and st.get("zt_on")) else None
        latente(self.ZT, ztl, "zt", "z_t")
        # suma
        mx, my = self.MAS
        on = "mas" in act
        ax.add_patch(plt.Circle((mx, my), 22, fc="white",
                                ec=ROJO if on else TINTA, lw=3 if on else 2,
                                zorder=5))
        self.texto(ax, mx, my - 1, "+", fs=24, fontweight="bold",
                   color=ROJO if on else TINTA)
        self.flecha(ax, [(zx1, my), (mx - 24, my)], "z-m" in fl)
        self.flecha(ax, [(mx + 22, my), (self.ZT[0] - 3, my)], "m-t" in fl)
        self.flecha(ax, [(self.ZT[1], my), (ux0 - 3, my)], "t-u" in fl)

        # fórmula (arriba de z0 ... z_t)
        fx = (zx0 + self.ZT[1]) / 2
        on = "formula" in act
        self.texto(ax, fx, 200, "z_t = √ᾱ_t · z0 + √(1−ᾱ_t) · ε", fs=20,
                   color=ROJO if on else TINTA,
                   fontweight="bold" if on else "normal")
        if f is not None and st.get("t_on"):
            a = ab(f["t"])
            s2 = (f"t = {f['t']}:  {np.sqrt(a):.2f} · z0 + "
                  f"{np.sqrt(1 - a):.2f} · ε").replace(".", ",")
            self.texto(ax, fx, 234, s2, fs=19, color=TINTA)

        # ------------------------------------------------ sorteo: t y ε
        tx0, tx1, ty0, ty1 = self.TBOX
        on = "t" in act
        if on:
            self.halo(ax, tx0, tx1, ty0, ty1)
        self.caja(ax, tx0, tx1, ty0, ty1, "white", ROJO if on else TINTA,
                  lw=3 if on else 2)
        tv = st.get("t_mostrar")
        self.texto(ax, (tx0 + tx1) / 2, ty0 + 28,
                   "t" if tv is None else f"t = {tv}", fs=21,
                   fontweight="bold", family="DejaVu Sans Mono",
                   color=ROJO if on else TINTA)
        self.texto(ax, (tx0 + tx1) / 2, ty0 + 64, "de 1 a 1000", fs=16,
                   color=GRIS_MEDIO)
        self.flecha(ax, [(tx1, ty0 + 45), (ux0 + 40, ty0 + 45),
                         (ux0 + 40, uy1 + 3)], "t-u2" in fl)
        ex, ey = self.EPS
        L_, o = self.CARTA, self.OFF
        ancho = L_ + 3 * o
        on = "eps" in act
        if f is not None and st.get("eps_on"):
            self.pila(ax, ex, ey, L_, o, f["eps"], on)
        else:
            for k in range(4):
                j = 3 - k
                xx, yy = ex + j * o, ey + (3 - j) * o
                ax.add_patch(Rectangle((xx, yy), L_, L_, fc=RELLENO,
                                       ec=BORDE_GRIS, lw=1.4,
                                       zorder=4 + k * 0.01))
        ecx = ex + ancho / 2
        self.texto(ax, ecx, ey + ancho + 26, "ε ~ N(0, I)", fs=20,
                   fontweight="bold" if on else "normal",
                   color=ROJO if on else TINTA)
        self.texto(ax, ecx, ey + ancho + 58, "64×64×4", fs=18,
                   family="DejaVu Sans Mono")
        # ε -> suma (sube) y ε -> pérdida (objetivo)
        self.flecha(ax, [(mx, ey - 2), (mx, my + 24)], "e-m" in fl)
        ly0, ly1 = self.LOSS_Y
        lyc = (ly0 + ly1) / 2
        self.flecha(ax, [(ex + ancho + 4, lyc), (self.CARDS[0][0] - 3, lyc)],
                    "e-l" in fl)

        # ------------------------------------------------ U-Net
        on = "unet" in act
        if on:
            self.halo(ax, ux0, ux1, uy0, uy1)
        self.caja(ax, ux0, ux1, uy0, uy1, "#FDF3F4" if on else "white", ROJO,
                  lw=4 if on else 3, r=18, z=1.5)
        self.texto(ax, ux0 + 24, uy0 + 38, "U-Net", fs=25,
                   fontweight="bold", color=ROJO, ha="left")
        self.caja(ax, ux1 - 192, ux1 - 20, uy0 + 19, uy0 + 57, ROJO, ROJO,
                  lw=1, r=17, z=6)
        self.texto(ax, ux1 - 106, uy0 + 38, "se entrena", fs=18,
                   fontweight="bold", color="white")
        self.texto(ax, ux0 + 24, uy0 + 84, "(z_t, t, embedding) → ε̂", fs=19,
                   ha="left")
        self.texto(ax, ux0 + 24, uy0 + 114, "de juguete, en numpy", fs=16,
                   ha="left", color=GRIS_MEDIO, style="italic")
        on = "upd" in act
        self.texto(ax, ux0 + 24, uy0 + 160, "SGD:  W ← W − η·∂L/∂W",
                   fs=20,
                   color=ROJO if on else TINTA, ha="left")
        # paneles W y ∂L/∂W (una muestra de 14 x 24 de W, 16.384 x 768)
        wx0, wx1, wy0, wy1 = self.WPAN
        gx0, gx1, gy0, gy1 = self.GPAN
        self.texto(ax, (wx0 + wx1) / 2, wy0 - 20, "W", fs=20,
                   fontweight="bold", color=ROJO if "Wup" in act else TINTA)
        self.texto(ax, (gx0 + gx1) / 2, gy0 - 20, "∂L/∂W", fs=20,
                   fontweight="bold", color=ROJO if "dW" in act else TINTA)
        Wm = st.get("W")
        Wm = np.zeros((14, 24)) if Wm is None else Wm
        self.imagen(ax, div_rgb(Wm, self.esc_W), wx0, wx1, wy0, wy1)
        ax.add_patch(Rectangle((wx0, wy0), wx1 - wx0, wy1 - wy0, fill=False,
                               ec=ROJO if "Wup" in act else TINTA,
                               lw=3 if "Wup" in act else 1.4, zorder=5))
        dW = st.get("dW")
        if dW is None:
            ax.add_patch(Rectangle((gx0, gy0), gx1 - gx0, gy1 - gy0,
                                   fc="white", ec=BORDE_GRIS, lw=1.5,
                                   ls=(0, (5, 4)), zorder=2))
        else:
            self.imagen(ax, div_rgb(dW, self.esc_dW), gx0, gx1, gy0, gy1)
            ax.add_patch(Rectangle((gx0, gy0), gx1 - gx0, gy1 - gy0,
                                   fill=False, ec=ROJO, lw=3 if "dW" in act
                                   else 1.6, zorder=5))
        if st.get("gnorm") is not None:   # a la derecha del camino del grad.
            xn = (self.XG + 8 + gx1) / 2
            self.texto(ax, xn, gy1 + 22, "‖∂L/∂W‖", fs=15, color=ROJO)
            self.texto(ax, xn, gy1 + 46,
                       f"{st['gnorm']:.3f}".replace(".", ","), fs=15,
                       color=ROJO, fontweight="bold")
        self.texto(ax, (wx0 + wx1) / 2, wy1 + 22, "muestra de", fs=15,
                   color=GRIS_MEDIO)
        self.texto(ax, (wx0 + wx1) / 2, wy1 + 46, "16.384 × 768", fs=15,
                   color=GRIS_MEDIO)

        # ------------------------------------------------ pérdida
        nombres = [("ε", "objetivo"), ("ε̂", "predicho"),
                   ("(ε − ε̂)²", "error")]
        ucx = (ux0 + ux1) / 2
        self.flecha(ax, [(ucx, uy1), (ucx, ly0 - 3)], "u-l" in fl)
        on = "loss" in act
        for k, (cx0, cx1) in enumerate(self.CARDS):
            arr = None
            if f is not None:
                if k == 0 and (st.get("eps_card") or "e-l" in fl):
                    arr = gris(f["eps"][..., 0])
                elif k == 1 and st.get("eh_on"):
                    arr = gris(f["eh"][..., 0])
                elif k == 2 and st.get("loss_on"):
                    arr = calor(((f["eps"] - f["eh"]) ** 2).mean(-1))
            if arr is None:
                self.vacia(ax, cx0, cx1, ly0, ly1)
            else:
                self.imagen(ax, arr, cx0, cx1, ly0, ly1)
                ax.add_patch(Rectangle((cx0, ly0), cx1 - cx0, ly1 - ly0,
                                       fill=False, ec=ROJO if (on and k == 2)
                                       else TINTA, lw=3 if (on and k == 2)
                                       else 1.4, zorder=5))
            self.texto(ax, (cx0 + cx1) / 2, ly1 + 20, nombres[k][0], fs=19,
                       color=TINTA, fontweight="bold")
            self.texto(ax, (cx0 + cx1) / 2, ly1 + 44, nombres[k][1], fs=15,
                       color=GRIS_MEDIO)
        lx = (self.CARDS[0][0] + self.CARDS[2][1]) / 2
        if st.get("loss_on") and f is not None:
            self.texto(ax, lx, ly1 + 84,
                       f"L = ‖ε − ε̂‖² = {f['L']:.3f}".replace(".", ","),
                       fs=24, fontweight="bold", color=ROJO if on else TINTA)
        else:
            self.texto(ax, lx, ly1 + 84, "L = ‖ε − ε̂‖²", fs=24,
                       fontweight="bold", color=BORDE_GRIS)

        # ------------------------------------------------ curva de pérdida
        self.curva(ax, st.get("hasta", 0), st.get("punto", True))

        # ------------------------------------------------ backward
        bw = st.get("bw", {})
        if bw:
            p1 = bw.get("loss", 0)
            if p1 > 0:
                self.grad(ax, [(self.XG, ly1 + 62), (self.XG,
                                                     self.GPAN[3] + 4)], p1)
            p2 = bw.get("in", 0)
            if p2 > 0:
                self.grad(ax, [(ux0, ym + 26), (self.EMB[1] + 6, ym + 26)],
                          p2)
                self.grad(ax, [(ux0, my + 26), (self.ZT[1] + 6, my + 26)],
                          p2)
            p3 = bw.get("frz", 0)
            if p3 > 0:
                self.grad(ax, [(self.EMB[0], ym + 26),
                               (self.CLIP[1] + 22, ym + 26)], p3)
                self.grad(ax, [(self.ZT[0], my + 26), (mx + 24, my + 26)],
                          p3)
                self.grad(ax, [(mx - 24, my + 26), (zx1 + 6, my + 26)], p3)
                self.grad(ax, [(zx0, my + 26),
                               (self.VAE[1] + 22, my + 26)], p3)
            if bw.get("cortes"):
                self.corte(ax, self.CLIP[1] + 14, ym + 26)
                self.corte(ax, self.VAE[1] + 14, my + 26)

        if st.get("pie"):
            self.texto(ax, PX_W / 2, 856, st["pie"], fs=21)
        fr = base.capturar(fig)
        plt.close(fig)
        return fr

    def curva(self, ax, hasta, punto=True):
        x0, x1, y0, y1 = self.CURVA
        ymax = 1.2
        ax.plot([x0, x0], [y0 - 6, y1], color=TINTA, lw=1.6, zorder=3)
        ax.plot([x0, x1], [y1, y1], color=TINTA, lw=1.6, zorder=3)
        self.texto(ax, x0 - 62, (y0 + y1) / 2, "L", fs=22, fontweight="bold",
                   ha="center")
        for v in (0.5, 1.0):
            yv = y1 - (y1 - y0) * v / ymax
            ax.plot([x0 - 6, x0], [yv, yv], color=TINTA, lw=1.4)
            self.texto(ax, x0 - 12, yv, f"{v:.1f}".replace(".", ","), fs=15,
                       ha="right", color=GRIS_MEDIO)
        self.texto(ax, x0 - 12, y1, "0", fs=15, ha="right", color=GRIS_MEDIO)
        self.texto(ax, x1, y1 + 24, f"paso {PASOS}".replace("1500", "1.500"),
                   fs=15, ha="right", color=GRIS_MEDIO)
        self.texto(ax, (x0 + x1) / 2, y1 + 24, "pasos de entrenamiento →",
                   fs=16, color=GRIS_MEDIO)
        self.texto(ax, x1, y0 - 18,
                   "SD 1.x real: pares de LAION · U-Net de ~860 M parámetros",
                   fs=15, ha="right", color=GRIS_MEDIO)
        if hasta <= 0:
            return
        n = hasta
        xs = x0 + (x1 - x0) * np.arange(n) / (PASOS - 1)
        ys = y1 - (y1 - y0) * np.clip(self.Ls[:n], 0, ymax) / ymax
        ax.plot(xs, ys, "o", ms=2.2, color="#C9C2C0", zorder=3.5,
                mec="none")
        ye = y1 - (y1 - y0) * np.clip(self.ema[:n], 0, ymax) / ymax
        ax.plot(xs, ye, color=ROJO, lw=3, zorder=4)
        if punto:
            ax.plot(xs[-1], ys[-1], "o", ms=10, color=ROJO, mec="white",
                    mew=2, zorder=5)


# =========================================================================
# guion
# =========================================================================
def guion(esc, fotos, final, reps, paso_vacio):
    frames = []

    def add(st, seg=None, n=None):
        k = n if n is not None else max(1, int(round(seg * FPS)))
        frames.append((st, k))

    f1 = fotos[0]
    a1 = ab(f1["t"])
    base_st = dict(par=0)
    P = {
        "par": "Dato de entrenamiento: un par (imagen, texto) del dataset.",
        "enc": "Congelados: CLIP (texto → embedding 77×768) y VAE encoder "
               "(imagen 512×512×3 → z0 64×64×4).",
        "t": "Se sortean un timestep t entre 1 y 1000 y un ruido ε ~ N(0, I) "
             "de 64×64×4.",
        "zt": (f"Schedule de SD: ᾱ_{f1['t']} = {a1:.3f}  →  z_t = "
               f"{np.sqrt(a1):.2f}·z0 + {np.sqrt(1 - a1):.2f}·ε, "
               f"latente con ruido 64×64×4.").replace(".", ","),
        "unet": "U-Net (la única que se entrena): entra (z_t, t, embedding), "
                "sale ε̂ 64×64×4.",
        "loss": (f"Pérdida: L = ‖ε − ε̂‖², el error cuadrático medio entre el "
                 f"ruido real y el predicho: {f1['L']:.3f}").replace(".", ","),
        "bw": "Backward: el gradiente va de L a ε̂ y de ahí a los pesos W de "
              "la U-Net.",
        "corte": "El gradiente se corta en CLIP y en el VAE: están congelados, "
                 "no se actualizan.",
        "upd": "Actualización (SGD): W ← W − η·∂L/∂W. Solo cambia la U-Net, "
               "y un paso la mueve poco.",
        "rep": "Se repite con otros pares y otros t: un juguete en numpy de "
               "4 pares, entrenado de verdad.",
        "vacio": "Texto vacío: así aprende también la predicción sin "
                 "condición. Pasa en una fracción de los pasos.",
    }

    def st_paso(fo, par, **kw):
        d = dict(par=par, foto=fo, z0_on=True, zt_on=True, t_on=True,
                 eps_on=True, eh_on=True, loss_on=True, t_mostrar=fo["t"],
                 eps_card=True,
                 vacio=fo["vacio"])
        d.update(kw)
        return d

    # 1. el par
    add(dict(base_st, activos={"txt", "img"}, emb_cols=0, foto=f1,
             pie=P["par"]), seg=0.7)
    # 1b. texto -> CLIP -> embedding  y  imagen -> VAE -> z0 (a la vez)
    for c in np.linspace(0, 77, 6).astype(int):
        add(dict(base_st, activos={"clip", "emb", "vae"},
                 flechas={"t-c", "c-e", "i-v"}, emb_cols=c, foto=f1,
                 pie=P["enc"]), n=1)
    add(dict(base_st, activos={"clip", "emb", "vae", "z0"},
             flechas={"t-c", "c-e", "i-v", "v-z"}, z0_on=True, foto=f1,
             pie=P["enc"]), seg=1.0)
    # 2. sorteo de t (gira) y de ε
    rng = np.random.default_rng(4)
    for v in list(rng.integers(1, 1001, 5)):
        add(dict(base_st, activos={"t"}, z0_on=True, foto=f1, t_mostrar=int(v),
                 pie=P["t"]), n=1)
    add(dict(base_st, activos={"t", "eps"}, z0_on=True, foto=f1,
             t_mostrar=f1["t"], eps_on=True, pie=P["t"]), seg=0.7)
    # 2b. mezcla -> z_t
    add(dict(base_st, activos={"formula", "mas", "zt"},
             flechas={"z-m", "e-m", "m-t"}, z0_on=True, foto=f1,
             t_mostrar=f1["t"], eps_on=True, t_on=True, zt_on=True,
             pie=P["zt"]), seg=1.5)
    ok = dict(z0_on=True, foto=f1, t_mostrar=f1["t"], eps_on=True, t_on=True,
              zt_on=True)
    # 3. U-Net
    add(dict(base_st, **ok, activos={"unet"}, flechas={"e-u", "t-u", "t-u2"},
             pie=P["unet"]), seg=0.5)
    add(dict(base_st, **ok, activos={"unet"}, flechas={"u-l"}, eh_on=True,
             pie=P["unet"]), seg=0.7)
    # 4. pérdida
    add(dict(base_st, **ok, activos={"loss"}, flechas={"e-l", "u-l"},
             eh_on=True, loss_on=True, pie=P["loss"]), seg=1.4)
    ok.update(eh_on=True, loss_on=True, eps_card=True)
    # 5. backward: L -> ∂L/∂W ; después hacia las entradas, y se corta
    for p in np.linspace(0.15, 1, 5):
        add(dict(base_st, **ok, activos={"loss"}, bw=dict(loss=p),
                 pie=P["bw"]), n=1)
    add(dict(base_st, **ok, activos={"dW"}, bw=dict(loss=1), dW=f1["dW"],
             gnorm=f1["gnorm"], pie=P["bw"]), seg=0.7)
    for p in np.linspace(0.2, 1, 4):
        add(dict(base_st, **ok, activos={"dW"}, bw=dict(loss=1, **{"in": p}),
                 dW=f1["dW"], gnorm=f1["gnorm"], pie=P["corte"]), n=1)
    for p in np.linspace(0.25, 1, 4):
        add(dict(base_st, **ok, activos={"dW"},
                 bw=dict(loss=1, frz=p, **{"in": 1}),
                 dW=f1["dW"], gnorm=f1["gnorm"], pie=P["corte"]), n=1)
    add(dict(base_st, **ok, activos={"dW", "clip", "vae"},
             bw=dict(loss=1, frz=1, cortes=True, **{"in": 1}),
             dW=f1["dW"], gnorm=f1["gnorm"], pie=P["corte"]), seg=1.1)
    # 5b. actualización
    add(dict(base_st, **ok, activos={"upd", "Wup"}, W=f1["W1"], dW=f1["dW"],
             gnorm=f1["gnorm"], hasta=1, pie=P["upd"]), seg=1.1)

    # 6. repetición rápida (pasos reales, cada vez más adelante)
    for s in reps:
        fo = fotos[s]
        add(st_paso(fo, fo["i"], activos={"unet", "loss"},
                    flechas={"e-u", "t-u", "t-u2", "u-l", "e-l"},
                    W=fo["W1"], dW=fo["dW"], gnorm=fo["gnorm"],
                    hasta=s + 1, bw=dict(loss=1), pie=P["rep"]), seg=0.42)
    # la curva corre hasta el paso del texto vacío
    for h in np.linspace(reps[-1] + 1, paso_vacio, 4)[1:].astype(int):
        fo = fotos[reps[-1]]
        add(st_paso(fo, fo["i"], activos={"loss"}, W=fo["W1"], dW=fo["dW"],
                    gnorm=fo["gnorm"], hasta=int(h), pie=P["rep"]), n=1)
    # 7. un paso con el texto vacío
    fo = fotos[paso_vacio]
    add(st_paso(fo, fo["i"], activos={"txt", "emb", "unet"},
                flechas={"c-e", "e-u", "t-c"}, W=fo["W0"],
                hasta=paso_vacio, pie=P["vacio"]), seg=0.6)
    add(st_paso(fo, fo["i"], activos={"loss"}, flechas={"u-l", "e-l"},
                W=fo["W1"], dW=fo["dW"], gnorm=fo["gnorm"], bw=dict(loss=1),
                hasta=paso_vacio + 1, pie=P["vacio"]), seg=1.5)
    # final fijo: el primer par otra vez, con la U-Net entrenada
    pie_fin = (f"Tras 1.500 pasos, el mismo par con el mismo t y el mismo ε: "
               + f"L baja de {f1['L']:.2f} a {final['L']:.3f}"
               .replace(".", ","))
    st_fin = st_paso(final, 0, activos=set(), W=final["W1"], dW=final["dW"],
                     gnorm=final["gnorm"], hasta=PASOS, punto=False,
                     bw=dict(loss=1, frz=1, cortes=True, **{"in": 1}),
                     pie=pie_fin + ".")
    # la curva termina ya con el estado final, y después la pausa
    for h in np.linspace(paso_vacio + 1, PASOS, 5)[1:-1].astype(int):
        add(dict(st_fin, hasta=int(h)), n=1)
    frames.append((st_fin, 1))
    return frames


def main():
    assert verificar_gradientes()
    _mod, log, _f, _fin = entrenar(guardar={0})
    reps, vac = elegir_pasos(log)
    mod, log2, fotos, final = entrenar(guardar={0, vac, *reps})
    assert [x[:3] for x in log2] == [x[:3] for x in log]
    f1 = fotos[0]
    esc_dW = 0.5 * np.abs(f1["dW"]).max()    # escala FIJA: la del paso 1
    esc_W = 0.5 * np.abs(final["W1"]).max()
    esc = Escena(log, esc_dW, esc_W)
    print("L paso 1 = %.3f, final = %.4f" % (f1["L"], final["L"]))
    print("‖∂L/∂W‖ paso 1 = %.4f, final = %.4f" % (f1["gnorm"],
                                                   final["gnorm"]))
    print("pasos mostrados:", [(s, log[s][:2], round(log[s][3], 3))
                               for s in reps], "vacío:", vac, log[vac])
    g = guion(esc, fotos, final, reps, vac)
    dbg = os.environ.get("ANIM_DEBUG_DIR")
    solo = os.environ.get("ANIM_SOLO")
    if solo:
        os.makedirs(dbg, exist_ok=True)
        for i in [int(x) for x in solo.split(",")]:
            i = i % len(g)
            esc.dibujar(g[i][0]).save(os.path.join(dbg, f"estado-{i:03d}.png"))
        print(f"{len(g)} estados")
        return
    cuadros = [(esc.dibujar(st), k) for st, k in g]
    # escritura atómica: se arma en un temporal y se reemplaza al final
    ruta = os.path.join(OUT, "sd-entrenamiento.gif")
    tmp = os.path.join(OUT, ".sd-entrenamiento.tmp.gif")
    pipe.guardar_gif(cuadros, tmp)
    os.replace(tmp, ruta)
    tmp_png = os.path.join(OUT, ".sd-entrenamiento.tmp.png")
    cuadros[-1][0].save(tmp_png, format="PNG")
    os.replace(tmp_png, os.path.join(OUT, "sd-entrenamiento.png"))
    if dbg:
        os.makedirs(dbg, exist_ok=True)
        n = len(cuadros)
        for i in (0, n // 5, n // 3, n // 2, int(n * 0.7), n - 12, n - 1):
            cuadros[i][0].save(os.path.join(dbg, f"cuadro-{i:03d}.png"))


if __name__ == "__main__":
    main()
