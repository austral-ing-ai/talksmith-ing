#!/usr/bin/env python3
"""Entrenamiento de un modelo de segmentación (vale para FCN y U-Net), para la
Talk "segmentacion-y-stable-diffusion".

  segmentacion-entrenamiento.gif / .png

Modelo de juguete REAL en numpy: una U-Net chica (8 -> 16 -> 32 canales, con
max pool, up-conv 2x2 y skip connections, 14.265 pesos) entrenada con
cross-entropy por píxel y descenso por gradiente (W <- W - eta * dL/dW, un par
por paso). Los gradientes son analíticos y se verifican contra diferencias
finitas. Datos: el mismo gato de perfil de fcn-en-vivo / unet-en-vivo
(_gato de gen_animaciones_conv.py, sin modificar ese archivo), llevado a 64x64,
más 19 variaciones (espejo, corrimiento, contraste, ruido).

Uso:  python3 gen_train_segmentacion.py      (DBG_DIR=<carpeta> guarda cuadros)
"""
import os
import sys

import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from gen_animaciones_conv import (  # noqa: E402
    _gato, _meanpool, _grises, _rojos, capturar, guardar_gif, TINTA, ROJO,
    RELLENO, GRIS_MEDIO, GRIS_TOP, GRIS_LADO, ROJO_TOP, ROJO_LADO, SLICE, OUT,
    W, H, DPI)

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import to_rgb  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon  # noqa: E402

ROSA = "#FBE3E5"
R = 64                      # resolución del modelo de juguete
N_AUG = 19                  # variaciones además de la imagen original
ETA = 0.05
EPOCAS = 30
SEMILLA = 1
E_DET = 5                   # época del paso que se muestra en detalle
LMAX = 2.0                  # escala fija del mapa de pérdida


def fmt(v, d=2):
    return f"{v:.{d}f}".replace(".", ",")


# =========================================================================
# Datos
# =========================================================================
def datos():
    img, gato = _gato(256)
    x0 = _meanpool(img, 4)
    y0 = (_meanpool(gato.astype(float), 4) > 0.5).astype(float)
    rng = np.random.default_rng(3)
    X, Y = [x0], [y0]
    for _ in range(N_AUG):
        x, y = x0.copy(), y0.copy()
        if rng.random() < 0.5:
            x, y = x[:, ::-1], y[:, ::-1]
        dy, dx = rng.integers(-6, 7, 2)
        x = np.roll(x, (dy, dx), (0, 1))
        y = np.roll(y, (dy, dx), (0, 1))
        a, b = rng.uniform(0.8, 1.2), rng.uniform(-0.12, 0.12)
        x = np.clip((x - 0.5) * a + 0.5 + b, 0, 1)
        x = x + rng.normal(0, 0.04, x.shape)
        X.append(x)
        Y.append(y)
    return np.array(X)[..., None], np.array(Y)


# =========================================================================
# U-Net de juguete en numpy (forward y backward analítico)
# =========================================================================
def conv_f(X, Wm, b):
    B, h, w, C = X.shape
    Xp = np.pad(X, ((0, 0), (1, 1), (1, 1), (0, 0)))
    P = np.lib.stride_tricks.sliding_window_view(Xp, (3, 3), axis=(1, 2))
    P = P.reshape(B * h * w, C * 9)
    return (P @ Wm + b).reshape(B, h, w, -1), P


def conv_b(dO, P, Wm, shp):
    B, h, w, C = shp
    d = dO.reshape(-1, dO.shape[-1])
    dW, db = P.T @ d, d.sum(0)
    dP = (d @ Wm.T).reshape(B, h, w, C, 3, 3)
    dXp = np.zeros((B, h + 2, w + 2, C))
    for i in range(3):
        for j in range(3):
            dXp[:, i:i + h, j:j + w, :] += dP[..., i, j]
    return dXp[:, 1:-1, 1:-1, :], dW, db


def pool_f(X):
    B, h, w, C = X.shape
    Xr = X.reshape(B, h // 2, 2, w // 2, 2, C).transpose(0, 1, 3, 5, 2, 4)
    Xr = Xr.reshape(B, h // 2, w // 2, C, 4)
    idx = Xr.argmax(-1)
    return np.take_along_axis(Xr, idx[..., None], -1)[..., 0], idx


def pool_b(dO, idx, shp):
    B, h, w, C = shp
    z = np.zeros((B, h // 2, w // 2, C, 4))
    np.put_along_axis(z, idx[..., None], dO[..., None], -1)
    z = z.reshape(B, h // 2, w // 2, C, 2, 2).transpose(0, 1, 4, 2, 5, 3)
    return z.reshape(B, h, w, C)


def up_f(X, Wu, b):          # up-conv 2x2 con paso 2
    B, h, w, _ = X.shape
    return np.einsum("bijk,acko->biajco", X, Wu).reshape(B, 2 * h, 2 * w, -1) + b


def up_b(dO, X, Wu):
    B, h, w, _ = X.shape
    d = dO.reshape(B, h, 2, w, 2, -1)
    return (np.einsum("biajco,acko->bijk", d, Wu),
            np.einsum("bijk,biajco->acko", X, d), d.sum((0, 1, 2, 3, 4)))


CONVS = [("e1", 1, 8), ("e2", 8, 16), ("b", 16, 32), ("d2", 32, 16),
         ("d1", 16, 8)]
GRUPOS = {"e1": ["e1"], "e2": ["e2"], "b": ["b"], "d2": ["u2", "d2"],
          "d1": ["u1", "d1", "o"]}


def init():
    rng = np.random.default_rng(SEMILLA)
    p = {}
    for k, ci, co in CONVS:
        p[k + ".W"] = rng.normal(0, np.sqrt(2 / (9 * ci)), (9 * ci, co))
        p[k + ".b"] = np.zeros(co)
    p["u2.W"] = rng.normal(0, np.sqrt(2 / 32), (2, 2, 32, 16))
    p["u2.b"] = np.zeros(16)
    p["u1.W"] = rng.normal(0, np.sqrt(2 / 16), (2, 2, 16, 8))
    p["u1.b"] = np.zeros(8)
    p["o.W"] = rng.normal(0, np.sqrt(1 / 8), (8, 1))
    p["o.b"] = np.zeros(1)
    return p


def forward(p, X):
    c = {"X": X}
    z, c["P_e1"] = conv_f(X, p["e1.W"], p["e1.b"])
    c["z_e1"], c["e1"] = z, np.maximum(z, 0)
    q1, c["i1"] = pool_f(c["e1"])
    c["q1"] = q1
    z, c["P_e2"] = conv_f(q1, p["e2.W"], p["e2.b"])
    c["z_e2"], c["e2"] = z, np.maximum(z, 0)
    q2, c["i2"] = pool_f(c["e2"])
    c["q2"] = q2
    z, c["P_b"] = conv_f(q2, p["b.W"], p["b.b"])
    c["z_b"], c["b"] = z, np.maximum(z, 0)
    k2 = np.concatenate([c["e2"], up_f(c["b"], p["u2.W"], p["u2.b"])], -1)
    c["k2"] = k2
    z, c["P_d2"] = conv_f(k2, p["d2.W"], p["d2.b"])
    c["z_d2"], c["d2"] = z, np.maximum(z, 0)
    k1 = np.concatenate([c["e1"], up_f(c["d2"], p["u1.W"], p["u1.b"])], -1)
    c["k1"] = k1
    z, c["P_d1"] = conv_f(k1, p["d1.W"], p["d1.b"])
    c["z_d1"], c["d1"] = z, np.maximum(z, 0)
    c["logit"] = (c["d1"] @ p["o.W"] + p["o.b"])[..., 0]
    return c


def ce(logit, Y):
    """cross-entropy binaria por píxel, estable: -[y log p + (1-y) log(1-p)]"""
    return np.maximum(logit, 0) - Y * logit + np.log1p(np.exp(-np.abs(logit)))


def backward(p, c, Y):
    g, a = {}, {}
    pr = 1 / (1 + np.exp(-c["logit"]))
    dz = (pr - Y) / Y.size                           # dL/dlogit
    g["o.W"] = c["d1"].reshape(-1, 8).T @ dz.reshape(-1, 1)
    g["o.b"] = np.array([dz.sum()])
    a["d1"] = dz[..., None] * p["o.W"][:, 0]
    dk1, g["d1.W"], g["d1.b"] = conv_b(a["d1"] * (c["z_d1"] > 0), c["P_d1"],
                                       p["d1.W"], c["k1"].shape)
    a["e1_skip"] = dk1[..., :8]
    a["d2"], g["u1.W"], g["u1.b"] = up_b(dk1[..., 8:], c["d2"], p["u1.W"])
    dk2, g["d2.W"], g["d2.b"] = conv_b(a["d2"] * (c["z_d2"] > 0), c["P_d2"],
                                       p["d2.W"], c["k2"].shape)
    a["e2_skip"] = dk2[..., :16]
    a["b"], g["u2.W"], g["u2.b"] = up_b(dk2[..., 16:], c["b"], p["u2.W"])
    dq2, g["b.W"], g["b.b"] = conv_b(a["b"] * (c["z_b"] > 0), c["P_b"],
                                     p["b.W"], c["q2"].shape)
    a["e2"] = a["e2_skip"] + pool_b(dq2, c["i2"], c["e2"].shape)
    dq1, g["e2.W"], g["e2.b"] = conv_b(a["e2"] * (c["z_e2"] > 0), c["P_e2"],
                                       p["e2.W"], c["q1"].shape)
    a["e1"] = a["e1_skip"] + pool_b(dq1, c["i1"], c["e1"].shape)
    _, g["e1.W"], g["e1.b"] = conv_b(a["e1"] * (c["z_e1"] > 0), c["P_e1"],
                                     p["e1.W"], c["X"].shape)
    return g, a


def verificar_gradiente(p, X, Y):
    c = forward(p, X)
    g, _ = backward(p, c, Y)
    rng = np.random.default_rng(1)
    eps = 1e-5
    errores = []
    for k in p:
        for _ in range(3):
            idx = tuple(int(rng.integers(0, s)) for s in p[k].shape)
            old = p[k][idx]
            p[k][idx] = old + eps
            lp = ce(forward(p, X)["logit"], Y).mean()
            p[k][idx] = old - eps
            lm = ce(forward(p, X)["logit"], Y).mean()
            p[k][idx] = old
            num = (lp - lm) / (2 * eps)
            rel = abs(num - g[k][idx]) / max(1e-9, abs(num) + abs(g[k][idx]))
            errores.append(rel)
            # tolerancia holgada solo por los quiebres de ReLU y max pool
            assert rel < 2e-2, (k, idx, num, g[k][idx])
    assert np.median(errores) < 1e-4, np.median(errores)


def metricas(pr, y):
    P, Yb = pr > 0.5, y > 0.5
    inter = (P & Yb).sum()
    return inter / max(1, (P | Yb).sum()), 2 * inter / max(1, P.sum() + Yb.sum())


def _canal(A, y, f):
    """Canal más correlacionado (en valor absoluto) con la máscara."""
    yy = _meanpool(y, f) if f > 1 else y
    mejores = []
    for j in range(A.shape[-1]):
        a = A[..., j]
        if a.std() < 1e-9:
            mejores.append(0)
            continue
        mejores.append(abs(np.corrcoef(a.ravel(), yy.ravel())[0, 1]))
    return int(np.argmax(mejores))


BLOQUES = ["e1", "e2", "b", "d2", "d1"]
FACTOR = {"e1": 1, "e2": 2, "b": 4, "d2": 2, "d1": 1}


def _foto(p, X0, Y0, canales):
    """Estado del par original con los pesos p (forward + backward)."""
    c = forward(p, X0)
    g, a = backward(p, c, Y0)
    pr = 1 / (1 + np.exp(-c["logit"][0]))
    l = ce(c["logit"][0], Y0[0])
    iou, dice = metricas(pr, Y0[0])
    caras = {}
    for k in BLOQUES:
        m = c[k][0][..., canales[k]]
        caras[k] = np.clip(m / (np.percentile(m, 99.5) + 1e-9), 0, 1)
    grads = {k: np.abs(a[k][0]).sum(-1) for k in BLOQUES}
    grads["e1_skip"] = np.abs(a["e1_skip"][0]).sum(-1)
    grads["e2_skip"] = np.abs(a["e2_skip"][0]).sum(-1)
    normas = {k: np.sqrt(sum((g[n + ".W"] ** 2).sum() + (g[n + ".b"] ** 2).sum()
                             for n in GRUPOS[k])) for k in BLOQUES}
    return dict(p=pr, l=l, L=l.mean(), iou=iou, dice=dice, caras=caras,
                grads=grads, normas=normas)


def entrenar():
    X, Y = datos()
    p = init()
    verificar_gradiente(p, X[:2], Y[:2])
    pesos, p_desp = [], None
    for ep in range(EPOCAS + 1):
        pesos.append({k: v.copy() for k, v in p.items()})
        if ep == EPOCAS:
            break
        orden = np.concatenate(
            [[0], np.random.default_rng(100 + ep).permutation(len(X) - 1) + 1])
        for paso, i in enumerate(orden):     # un par por paso
            c = forward(p, X[i:i + 1])
            g, _ = backward(p, c, Y[i:i + 1])
            for k in p:
                p[k] -= ETA * g[k]
            if ep == E_DET and paso == 0:       # el paso que se muestra
                p_desp = {k: v.copy() for k, v in p.items()}
    # canal de cada cara: el más parecido a la máscara en la época mostrada
    cd = forward(pesos[E_DET], X[:1])
    canales = {k: _canal(cd[k][0], Y[0], FACTOR[k]) for k in BLOQUES}
    fotos = []
    for ep, w in enumerate(pesos):
        f = _foto(w, X[:1], Y[:1], canales)
        f["ep"] = ep
        fotos.append(f)
    despues = _foto(p_desp, X[:1], Y[:1], canales)
    despues["ep"] = E_DET
    assert despues["L"] < fotos[E_DET]["L"], "el paso detallado no baja L"
    Ls = [f["L"] for f in fotos]
    assert Ls[-1] < 0.1 * Ls[0] and fotos[-1]["iou"] > 0.9, (Ls[-1], Ls[0])
    n_pesos = sum(v.size for v in p.values())
    return X, Y, fotos, despues, n_pesos


# =========================================================================
# Dibujo (coordenadas en px, y hacia abajo)
# =========================================================================
IMG = 210
XA = 45                          # columna A: imagen y máscara
YT, YB = 95, 582                 # banda de arriba / de abajo (y0 de imágenes)
CY_T, CY_B = YT + IMG / 2, YB + IMG / 2
XC = 1070                        # columna C: p y mapa de pérdida
XCC = XC + IMG / 2
UB = (282, 1042, 36, 528)        # caja de la U-Net
FB = (300, 1030, YB + 4, YB + IMG)   # caja de la fórmula
XD0, XD1 = 1318, 1558            # columna D
XDC = (XD0 + XD1) / 2
G_L = (1362, 1540, 100, 196)     # gráfico de L  (x0, x1, y0, y1)
G_I = (1362, 1540, 252, 348)     # gráfico de IoU

GEO = {   # cara: lado, canales, centro
    "e1": dict(s=110, c=8, cx=392, cy=CY_T, n="enc 1", d="64×64×8"),
    "e2": dict(s=80, c=16, cx=460, cy=365, n="enc 2", d="32×32×16"),
    "b": dict(s=56, c=32, cx=662, cy=452, n="bottleneck", d="16×16×32"),
    "d2": dict(s=80, c=16, cx=864, cy=365, n="dec 2", d="32×32×16"),
    "d1": dict(s=110, c=8, cx=932, cy=CY_T, n="dec 1", d="64×64×8"),
}
for _g in GEO.values():
    _prof = 4 + 6 * np.log2(_g["c"])
    _g.update(x0=_g["cx"] - _g["s"] / 2, y0=_g["cy"] - _g["s"] / 2,
              dx=0.5 * _prof, dy=0.3 * _prof)


# flechas del forward (y caminos del gradiente, recorridos al revés)
def _caminos():
    e1, e2, b, d2, d1 = (GEO[k] for k in BLOQUES)
    return {
        "x_e1": [(XA + IMG + 6, CY_T), (e1["x0"] - 6, CY_T)],
        "e1_e2": [(440, e1["y0"] + e1["s"] + 4),
                  (440, e2["y0"] - e2["dy"] - 4)],
        "e2_b": [(e2["cx"], e2["y0"] + e2["s"] + 4), (e2["cx"], b["cy"]),
                 (b["x0"] - 6, b["cy"])],
        "b_d2": [(b["x0"] + b["s"] + b["dx"] + 6, b["cy"]), (d2["cx"], b["cy"]),
                 (d2["cx"], d2["y0"] + d2["s"] + 4)],
        "d2_d1": [(890, d2["y0"] - d2["dy"] - 4), (890, d1["y0"] + d1["s"] + 4)],
        "d1_p": [(d1["x0"] + d1["s"] + d1["dx"] + 6, CY_T), (XC - 6, CY_T)],
        "skip1": [(e1["x0"] + e1["s"] + e1["dx"] + 6, CY_T), (d1["x0"] - 6, CY_T)],
        "skip2": [(e2["x0"] + e2["s"] + e2["dx"] + 6, e2["cy"]),
                  (d2["x0"] - 6, d2["cy"])],
        "p_l": [(XCC, YT + IMG + 72), (XCC, YB - 46)],
        "y_f": [(XA + IMG + 6, CY_B), (FB[0] - 5, CY_B)],
        "f_l": [(FB[1] + 5, CY_B), (XC - 6, CY_B)],
    }


CAM = _caminos()


def preparar(ax):
    ax.clear()
    ax.set_xlim(0, W * DPI)
    ax.set_ylim(H * DPI, 0)
    ax.axis("off")


def txt(ax, x, y, s, size=19, color=TINTA, bold=False, ha="center",
        va="center", z=8, **kw):
    ax.text(x, y, s, fontsize=size, color=color, ha=ha, va=va, zorder=z,
            fontweight="bold" if bold else "normal", **kw)


def linea(ax, pts, color=GRIS_MEDIO, lw=2.2, z=3):
    xs, ys = zip(*pts)
    if len(pts) > 2:
        ax.plot(xs[:-1], ys[:-1], color=color, lw=lw, zorder=z,
                solid_capstyle="butt", solid_joinstyle="miter")
    ax.annotate("", xy=pts[-1], xytext=pts[-2], zorder=z,
                arrowprops=dict(arrowstyle="-|>,head_length=0.7,head_width=0.35",
                                color=color, lw=lw, shrinkA=0, shrinkB=0))


def punto_en(pts, t):
    """Posición a una fracción t del largo de la poligonal pts."""
    pts = np.array(pts, float)
    seg = np.hypot(*np.diff(pts, axis=0).T)
    d = np.clip(t, 0, 1) * seg.sum()
    for (a, b), s in zip(zip(pts[:-1], pts[1:]), seg):
        if d <= s:
            return a + (b - a) * d / max(s, 1e-9)
        d -= s
    return pts[-1]


def particula(ax, pts, t):
    """Punto rojo con estela, recorriendo pts (ya en el sentido del viaje)."""
    if not 0 < t <= 1:
        return
    for k, (dt, r, al) in enumerate(((0.0, 8, 1.0), (0.07, 6, 0.55),
                                     (0.14, 4.5, 0.3))):
        if t - dt <= 0:
            continue
        x, y = punto_en(pts, t - dt)
        ax.add_patch(plt.Circle((x, y), r, fc=ROJO, ec="none", alpha=al,
                                zorder=12 - k))


def imagen(ax, rgb, x0, y0, s, z=4):
    ax.imshow(rgb, extent=(x0, x0 + s, y0 + s, y0), zorder=z,
              interpolation="nearest")


def mezclar(a, b, t):
    return a + (b - a) * float(np.clip(t, 0, 1))


def revelar(rgb, t, fondo=None):
    """Revela por filas de arriba hacia abajo (t de 0 a 1)."""
    out = rgb.copy()
    k = int(round(out.shape[0] * np.clip(t, 0, 1)))
    out[k:] = np.array(to_rgb(RELLENO)) if fondo is None else fondo[k:]
    return out


def prisma(ax, k, cara, borde=TINTA, activo=False):
    gg = GEO[k]
    x0, y0, s, dx, dy = gg["x0"], gg["y0"], gg["s"], gg["dx"], gg["dy"]
    ct, cl = (ROJO_TOP, ROJO_LADO) if activo else (GRIS_TOP, GRIS_LADO)
    ec = ROJO if activo else TINTA
    top = [(x0, y0), (x0 + s, y0), (x0 + s + dx, y0 - dy), (x0 + dx, y0 - dy)]
    lado = [(x0 + s, y0), (x0 + s, y0 + s), (x0 + s + dx, y0 + s - dy),
            (x0 + s + dx, y0 - dy)]
    ax.add_patch(Polygon(top, closed=True, fc=ct, ec=ec, lw=1.4, zorder=2))
    ax.add_patch(Polygon(lado, closed=True, fc=cl, ec=ec, lw=1.4, zorder=2))
    nl = int(np.log2(gg["c"]))
    for j in range(1, nl):
        f = j / nl
        ax.plot([x0 + f * dx, x0 + s + f * dx], [y0 - f * dy] * 2,
                color=ROJO if activo else SLICE, lw=0.8, zorder=3, alpha=0.7)
        ax.plot([x0 + s + f * dx] * 2, [y0 - f * dy, y0 + s - f * dy],
                color=ROJO if activo else SLICE, lw=0.8, zorder=3, alpha=0.7)
    imagen(ax, cara, x0, y0, s)
    ax.add_patch(Rectangle((x0, y0), s, s, fill=False, ec=borde,
                           lw=3.2 if borde == ROJO else 1.8, zorder=5))


def etiqueta_bloque(ax, k):
    gg = GEO[k]
    x0, y0, s, dx, dy = gg["x0"], gg["y0"], gg["s"], gg["dx"], gg["dy"]
    if k in ("e1", "d1"):
        xc = x0 + (s + dx) / 2
        txt(ax, xc, y0 - dy - 38, gg["n"], size=19, bold=True)
        txt(ax, xc, y0 - dy - 13, gg["d"], size=18)
    elif k == "e2":
        txt(ax, x0 - 12, gg["cy"] - 14, gg["n"], size=19, bold=True, ha="right")
        txt(ax, x0 - 12, gg["cy"] + 14, gg["d"], size=18, ha="right")
    elif k == "d2":
        xr = x0 + s + dx + 12
        txt(ax, xr, gg["cy"] - 14, gg["n"], size=19, bold=True, ha="left")
        txt(ax, xr, gg["cy"] + 14, gg["d"], size=18, ha="left")
    else:
        txt(ax, x0 + (s + dx) / 2, y0 + s + 20,
            f"{gg['n']}  {gg['d']}", size=18)


# barras de ‖∂L/∂W‖ en el centro de la U (orden de llegada del backward)
BAR_ORDEN = ["d1", "d2", "b", "e2", "e1"]
BAR_X0, BAR_X1, BAR_Y0, BAR_DY = 618, 735, 252, 21
CENTRO_X = 655


def barras(ax, normas, escala, llenado, pulso=0.0):
    for i, k in enumerate(BAR_ORDEN):
        f = llenado.get(k, 0.0)
        if f <= 0:
            continue
        y = BAR_Y0 + i * BAR_DY
        txt(ax, BAR_X0 - 10, y, GEO[k]["n"], size=17, ha="right")
        largo = (BAR_X1 - BAR_X0) * min(1, normas[k] / escala) * min(1, f)
        ax.add_patch(Rectangle((BAR_X0, y - 7), BAR_X1 - BAR_X0, 14,
                               fc="white", ec="#D9D3D1", lw=1, zorder=6))
        ax.add_patch(Rectangle((BAR_X0, y - 7), max(largo, 1.5), 14,
                               fc=ROJO, ec="none", zorder=7,
                               alpha=1 - 0.5 * pulso))
        if f >= 1:
            txt(ax, BAR_X1 + 8, y, fmt(normas[k], 3), size=17, ha="left",
                color=ROJO)


def curvas(ax, fotos, hasta, ep_actual):
    for (x0, x1, y0, y1), clave, tope, nombre in (
            (G_L, "L", 0.7, "L"), (G_I, "iou", 1.0, "IoU")):
        ax.plot([x0, x0, x1], [y0 - 6, y1, y1], color=TINTA, lw=1.4,
                zorder=5)
        txt(ax, x0 - 10, (y0 + y1) / 2, nombre, size=18, ha="right")
        txt(ax, x0 - 8, y1 - 2, "0", size=16, ha="right", color=GRIS_MEDIO)
        if clave == "iou":
            ax.plot([x0, x1], [y0, y0], color=GRIS_MEDIO, lw=1, ls=":",
                    zorder=4)
            txt(ax, x1 + 6, y0, "1", size=16, ha="left", color=GRIS_MEDIO)
        if hasta < 0:
            continue
        xs = [x0 + (x1 - x0) * f["ep"] / EPOCAS for f in fotos[:hasta + 1]]
        ys = [y1 - (y1 - y0) * min(1, f[clave] / tope)
              for f in fotos[:hasta + 1]]
        ax.plot(xs, ys, color=TINTA, lw=2, zorder=6)
        ax.plot(xs[-1], ys[-1], "o", color=ROJO, ms=9, zorder=7)
    x0, x1, _, y1 = G_I
    txt(ax, x0, y1 + 20, "0", size=16, color=GRIS_MEDIO)
    txt(ax, x1, y1 + 20, str(EPOCAS), size=16, color=GRIS_MEDIO)
    txt(ax, (x0 + x1) / 2, y1 + 22, "época", size=17, color=GRIS_MEDIO)
    txt(ax, XDC, 56, f"época {ep_actual} de {EPOCAS}", size=20, bold=True)


def dibujar(ax, D, *, foto, fase=0, fw=None, fw_activo=None, p_t=0.0,
            l_t=0.0, f_alpha=0.0, sondas=False, ver_L=False, curva_hasta=-1,
            grad=None, grad_t=None, bar_fill=None, part=(), activo_p=False,
            update_t=-1.0, foto2=None, pie=""):
    """fase 0 dato · 1 forward · 2 pérdida · 3 backward · 4 actualización ·
    5 épocas. fw: {bloque: fracción revelada de la activación}. grad: {bloque:
    'skip'|'total'} y grad_t: {bloque: fracción revelada del gradiente}."""
    preparar(ax)
    fw = fw or {}
    grad, grad_t, bar_fill = grad or {}, grad_t or {}, bar_fill or {}
    X, Y = D["X"], D["Y"]
    gris = np.array(to_rgb(RELLENO))
    entrena = fase in (3, 4)
    mz = (update_t - 0.25) / 0.4 if (foto2 is not None and update_t >= 0) \
        else -1.0                                      # mezcla hacia W'

    # --- caja de la U-Net (se entrena) ------------------------------------
    ax.add_patch(FancyBboxPatch((UB[0], UB[2]), UB[1] - UB[0], UB[3] - UB[2],
                                boxstyle="round,pad=0,rounding_size=12",
                                fc=ROSA if entrena else "white", ec=ROJO,
                                lw=2.6 if entrena else 2.0, zorder=0))
    txt(ax, UB[0] + 16, UB[2] + 22,
        f"U-Net de juguete · {D['n_pesos']:,} pesos".replace(",", "."),
        size=19, bold=True, ha="left")
    txt(ax, UB[1] - 16, UB[2] + 22, "se entrena", size=19, bold=True,
        color=ROJO, ha="right")
    nota = ("caras: 1 canal", "por bloque") if fase <= 2 and not grad else \
        ("caras: |∂L/∂·|", "escala fija")
    txt(ax, UB[0] + 16, UB[3] - 46, nota[0], size=17, color=GRIS_MEDIO,
        ha="left")
    txt(ax, UB[0] + 16, UB[3] - 21, nota[1], size=17, color=GRIS_MEDIO,
        ha="left")

    # --- flechas ---------------------------------------------------------
    destino = {"x_e1": "e1", "e1_e2": "e2", "e2_b": "b", "b_d2": "d2",
               "d2_d1": "d1", "d1_p": "p"}
    for nombre, dest in destino.items():
        on = fase == 1 and fw_activo == dest
        linea(ax, CAM[nombre], color=ROJO if on else GRIS_MEDIO,
              lw=3.2 if on else 2.2)
    for nombre, dest, debajo in (("skip1", "d1", False), ("skip2", "d2", True)):
        on = fase == 1 and fw_activo == dest
        pts = CAM[nombre]
        linea(ax, pts, color=ROJO, lw=4.2 if on else 2.6)
        txt(ax, (pts[0][0] + pts[1][0]) / 2, pts[0][1] + (23 if debajo else -22),
            "skip: concatenar", size=18, color=ROJO, bold=on)

    # --- bloques ---------------------------------------------------------
    for k in BLOQUES:
        n = R // FACTOR[k]
        cara = np.tile(gris, (n, n, 1))
        if k in fw:
            cara = revelar(_grises(foto["caras"][k]), fw[k])
        if k in grad:
            gm = foto["grads"]["%s_skip" % k if grad[k] == "skip" else k]
            gr = _rojos(np.clip(gm / D["g_escala"][k], 0, 1))
            cara = revelar(gr, grad_t.get(k, 1.0), fondo=cara)
        on = (fase == 1 and fw_activo == k) or \
            (fase == 3 and 0 < grad_t.get(k, 0) < 1)
        prisma(ax, k, cara, borde=ROJO if on else TINTA, activo=on)
        etiqueta_bloque(ax, k)

    # --- centro de la U: ‖∂L/∂W‖ o la regla de actualización ---------------
    if fase in (3, 4) and bar_fill:
        if fase == 4:
            txt(ax, CENTRO_X, 226, "W ← W − η · ∂L/∂W", size=22, bold=True,
                color=ROJO)
        else:
            txt(ax, CENTRO_X, 226, "‖∂L/∂W‖ por capa", size=19, color=ROJO)
        pulso = 0.5 * (1 - np.cos(2 * np.pi * update_t * 3)) \
            if fase == 4 and 0 <= update_t < 0.67 else 0.0
        barras(ax, foto["normas"], D["n_escala"], bar_fill, pulso=pulso)
    elif fase == 5:
        txt(ax, CENTRO_X, 262, "W ← W − η · ∂L/∂W", size=22, bold=True)
        txt(ax, CENTRO_X, 298, f"η = {fmt(ETA)} · un par por paso", size=18,
            color=GRIS_MEDIO)

    # --- columna A: imagen y máscara -------------------------------------
    resalta = fase == 0
    txt(ax, XA, YT - 12, "imagen x", size=20, bold=True, ha="left",
        va="bottom")
    imagen(ax, np.repeat(np.clip(X[0, ..., 0], 0, 1)[..., None], 3, 2), XA, YT,
           IMG)
    ax.add_patch(Rectangle((XA, YT), IMG, IMG, fill=False,
                           ec=ROJO if resalta else TINTA,
                           lw=3.2 if resalta else 1.6, zorder=5))
    txt(ax, XA + IMG / 2, YT + IMG + 20, "64×64, 1 canal", size=18,
        color=GRIS_MEDIO)
    txt(ax, XA + IMG / 2, 384, f"+ {N_AUG} pares más", size=18,
        color=GRIS_MEDIO)
    lado, sep = 33, 6
    for j, i in enumerate((1, 2, 3)):
        x = XA + j * (2 * lado + 2 + sep) + 2
        imagen(ax, np.repeat(np.clip(X[i, ..., 0], 0, 1)[..., None], 3, 2),
               x, 406, lado)
        imagen(ax, _rojos(Y[i]), x + lado + 2, 406, lado)
        for xx in (x, x + lado + 2):
            ax.add_patch(Rectangle((xx, 406), lado, lado, fill=False,
                                   ec=GRIS_MEDIO, lw=1, zorder=5))
    txt(ax, XA, YB - 12, "máscara verdadera y", size=20, bold=True,
        ha="left", va="bottom")
    imagen(ax, _rojos(Y[0]), XA, YB, IMG)
    ax.add_patch(Rectangle((XA, YB), IMG, IMG, fill=False,
                           ec=ROJO if resalta else TINTA,
                           lw=3.2 if resalta else 1.6, zorder=5))
    txt(ax, XA, YB + IMG + 26, "datos: pares imagen–máscara anotados a mano"
        " (U-Net 2015: 30 imágenes)", size=17, color=GRIS_MEDIO, ha="left")

    # --- columna C: p y mapa de pérdida -----------------------------------
    txt(ax, XCC, YT - 12, "probabilidad p", size=20, bold=True, va="bottom")
    if p_t > 0:
        rgb = _rojos(foto["p"])
        if mz >= 0:
            rgb = mezclar(rgb, _rojos(foto2["p"]), mz)
        imagen(ax, revelar(rgb, p_t), XC, YT, IMG)
        if p_t >= 1:
            ax.contour(np.linspace(XC, XC + IMG, R), np.linspace(YT, YT + IMG, R),
                       Y[0], levels=[0.5], colors=[TINTA], linewidths=1.3,
                       linestyles="--", zorder=6)
    else:
        ax.add_patch(Rectangle((XC, YT), IMG, IMG, fc=RELLENO, ec="none",
                               zorder=3))
    rojo_p = activo_p or (fase == 1 and fw_activo == "p")
    ax.add_patch(Rectangle((XC, YT), IMG, IMG, fill=False,
                           ec=ROJO if rojo_p else TINTA,
                           lw=3.2 if rojo_p else 1.6, zorder=7))
    txt(ax, XCC, YT + IMG + 20, "conv 1×1 + sigmoide", size=17,
        color=GRIS_MEDIO)
    ax.plot([XCC - 90, XCC - 62], [YT + IMG + 48] * 2, color=TINTA, lw=1.6,
            ls="--", zorder=6)
    txt(ax, XCC - 54, YT + IMG + 48, "contorno de y", size=17,
        color=GRIS_MEDIO, ha="left")

    txt(ax, XCC, YB - 12, "pérdida por píxel ℓ", size=20, bold=True,
        va="bottom")
    if l_t > 0:
        lm = foto["l"]
        if mz >= 0:
            lm = mezclar(lm, foto2["l"], mz)
        imagen(ax, revelar(_grises(np.clip(lm / LMAX, 0, 1)), l_t,
                           fondo=np.ones((R, R, 3))), XC, YB, IMG)
    else:
        ax.add_patch(Rectangle((XC, YB), IMG, IMG, fc=RELLENO, ec="none",
                               zorder=3))
    ax.add_patch(Rectangle((XC, YB), IMG, IMG, fill=False, ec=TINTA, lw=1.6,
                           zorder=7))
    txt(ax, XCC, YB + IMG + 24, "negro: ℓ ≥ 2", size=17, color=GRIS_MEDIO)
    on = fase == 2 and l_t < 1
    linea(ax, CAM["p_l"], color=ROJO if on else GRIS_MEDIO, lw=3 if on else 2.2)

    # --- caja de la fórmula -----------------------------------------------
    if f_alpha > 0:
        al = float(np.clip(f_alpha, 0, 1))
        ax.add_patch(FancyBboxPatch((FB[0], FB[2]), FB[1] - FB[0],
                                    FB[3] - FB[2],
                                    boxstyle="round,pad=0,rounding_size=12",
                                    fc="white", ec=TINTA, lw=1.8, zorder=1,
                                    alpha=al))
        linea(ax, CAM["y_f"], color=ROJO if on else GRIS_MEDIO,
              lw=3 if on else 2.2)
        linea(ax, CAM["f_l"], color=ROJO if on else GRIS_MEDIO,
              lw=3 if on else 2.2)
        txt(ax, FB[0] + 22, FB[2] + 24, "cross-entropy en cada píxel i",
            size=20, bold=True, ha="left", alpha=al)
        txt(ax, (FB[0] + FB[1]) / 2, FB[2] + 66,
            r"$\ell_i = -\,[\;y_i\,\log p_i \;+\; (1-y_i)\,\log(1-p_i)\;]$",
            size=24, alpha=al)
        txt(ax, FB[0] + 22, FB[2] + 180,
            "L = promedio de los 64 × 64 = 4.096 valores de ℓ", size=19,
            ha="left", alpha=al)
    if sondas:
        for (fi, co), color, yl, nombre in D["sondas"]:
            c = IMG / R
            for x0, y0 in ((XC, YT), (XC, YB), (XA, YB)):
                ax.add_patch(Rectangle((x0 + co * c - 4, y0 + fi * c - 4),
                                       c + 8, c + 8, fill=False, ec=color,
                                       lw=2.6, zorder=9))
            ax.add_patch(Rectangle((FB[0] + 24, yl - 8), 16, 16, fill=False,
                                   ec=color, lw=2.6, zorder=9))
            pv, lv = foto["p"][fi, co], foto["l"][fi, co]
            if mz >= 0:
                pv = mezclar(pv, foto2["p"][fi, co], mz)
                lv = mezclar(lv, foto2["l"][fi, co], mz)
            txt(ax, FB[0] + 52, yl,
                f"{nombre}: y = {int(Y[0][fi, co])}, p = {fmt(pv)}  →  "
                f"ℓ = {fmt(lv)}", size=19, ha="left")

    # --- columna D: curvas y números ---------------------------------------
    curvas(ax, D["fotos"], curva_hasta, foto["ep"])
    if ver_L:
        fo = foto2 if mz >= 1 else foto
        txt(ax, XDC, YB + 32, f"L = {fmt(fo['L'], 3)}", size=32, bold=True,
            color=ROJO)
        if mz >= 1:
            txt(ax, XDC, YB + 72, f"antes: {fmt(foto['L'], 3)}", size=18,
                color=ROJO)
        txt(ax, XDC, YB + 108, f"IoU = {fmt(fo['iou'])}", size=22)
        txt(ax, XDC, YB + 142, f"Dice = {fmt(fo['dice'])}", size=19)
        txt(ax, XDC, YB + 180, "(máscara: p > 0,5)", size=17,
            color=GRIS_MEDIO)

    for pts, t in part:
        particula(ax, pts, t)
    if pie:
        txt(ax, W * DPI / 2, 866, pie, size=21)


def segmentacion_entrenamiento(fps=12, pausa_s=3.0):
    X, Y, fotos, despues, n_pesos = entrenar()
    fd = fotos[E_DET]
    # escalas FIJAS: las del paso detallado
    g_escala = {k: np.percentile(fd["grads"][k], 99.5) + 1e-12 for k in BLOQUES}
    n_escala = max(fd["normas"].values()) * 1.1
    # sondas: el píxel de borde del gato con más pérdida y uno del fondo
    y0 = Y[0]
    borde = (y0 > 0.5) & ((np.roll(y0, 1, 0) < 0.5) | (np.roll(y0, -1, 0) < 0.5)
                          | (np.roll(y0, 1, 1) < 0.5) | (np.roll(y0, -1, 1) < 0.5))
    # (de los de borde mal clasificados en la época mostrada, el que más mejora
    # al final: un ejemplo típico, no el píxel imposible de la punta de la oreja)
    mejora = np.where(borde & (fd["l"] > 1.0), fd["l"] - fotos[-1]["l"], -9)
    sa = np.unravel_index(np.argmax(mejora), y0.shape)
    sb = (54, 8)
    assert y0[sb] < 0.5 and y0[sa] > 0.5
    D = dict(X=X, Y=Y, fotos=fotos, n_pesos=n_pesos, g_escala=g_escala,
             n_escala=n_escala,
             sondas=[(sa, ROJO, FB[2] + 108, "píxel de borde"),
                     (sb, TINTA, FB[2] + 140, "píxel de fondo")])
    print(f"pesos {n_pesos}  L ép.0 {fotos[0]['L']:.3f}  L ép.{E_DET} "
          f"{fd['L']:.3f} -> {despues['L']:.3f}  final {fotos[-1]['L']:.3f}  "
          f"IoU {fotos[0]['iou']:.2f} -> {fotos[-1]['iou']:.2f}")
    print("sonda borde", sa, fd["p"][sa], fd["l"][sa], " fondo", sb,
          fd["p"][sb], fd["l"][sb])
    print("suma |dL/da| ép.", E_DET, {k: round(float(fd["grads"][k].sum()), 3)
                                      for k in BLOQUES},
          "final", {k: round(float(fotos[-1]["grads"][k].sum()), 3)
                    for k in BLOQUES})

    fig = plt.figure(figsize=(W, H), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    fr = []

    def cap(n=1, **kw):
        kw.setdefault("foto", fd)
        dibujar(ax, D, **kw)
        fr.extend([capturar(fig)] * n)

    # 1. el dato
    cap(12, fase=0, pie="Un par de entrenamiento: la imagen x y su máscara"
        " verdadera y (rojo = gato)")
    # 2. forward
    pie_fw = ("forward (modelo de juguete en numpy): la imagen recorre la"
              " U-Net y sale p")
    fw = {}
    for k in BLOQUES:
        for f in range(1, 6):
            fw[k] = f / 5
            cap(fase=1, fw=dict(fw), fw_activo=k, pie=pie_fw)
    for f in range(1, 7):
        cap(fase=1, fw=fw, fw_activo="p", p_t=f / 6, pie=pie_fw)
    cap(6, fase=1, fw=fw, p_t=1, pie=f"p = probabilidad de «gato» en cada"
        f" píxel; en la época {E_DET} todavía es una mancha tenue")
    # 3. pérdida
    pie_l = ("pérdida: cross-entropy en cada píxel; alta en los bordes y donde"
             " p se aleja de y")
    base = dict(fw=fw, p_t=1)
    for f in range(1, 5):
        cap(fase=2, f_alpha=f / 4, pie=pie_l, **base)
    for f in range(1, 11):
        cap(fase=2, f_alpha=1, l_t=f / 10, pie=pie_l, **base)
    cap(12, fase=2, f_alpha=1, l_t=1, sondas=True, pie=pie_l, **base)
    cap(12, fase=2, f_alpha=1, l_t=1, sondas=True, ver_L=True,
        curva_hasta=E_DET, pie=f"L = promedio de ℓ sobre los 4.096 píxeles"
        f" = {fmt(fd['L'], 3)}", **base)
    base = dict(fw=fw, p_t=1, f_alpha=1, l_t=1, sondas=True, ver_L=True,
                curva_hasta=E_DET)
    # 4. backward
    pie_b = ("backward: el gradiente vuelve capa por capa, por el decoder,"
             " los skips y el encoder")
    tramos = [  # (camino, inicio, fin) en cuadros; los caminos se invierten
        ("p_l", 0, 6), ("d1_p", 6, 10), ("d2_d1", 12, 16), ("skip1", 12, 20),
        ("b_d2", 20, 25), ("skip2", 20, 28), ("e2_b", 29, 34),
        ("e1_e2", 36, 40)]
    llegada = {  # bloque: [(cuadro, tipo de gradiente)]
        "d1": [(10, "total")], "d2": [(16, "total")],
        "e1": [(20, "skip"), (40, "total")], "b": [(25, "total")],
        "e2": [(28, "skip"), (34, "total")]}
    barra_ini = {"d1": 10, "d2": 16, "b": 25, "e2": 34, "e1": 40}
    for f in range(48):
        part = [(CAM[c][::-1], (f - a) / (b - a)) for c, a, b in tramos
                if a < f <= b]
        grad, grad_t = {}, {}
        for k, eventos in llegada.items():
            for t0, tipo in eventos:
                if f >= t0:
                    grad[k] = tipo
                    grad_t[k] = min(1.0, (f - t0 + 1) / 4)
        bars = {k: min(1.0, (f - t0 + 1) / 4) for k, t0 in barra_ini.items()
                if f >= t0}
        cap(fase=3, grad=grad, grad_t=grad_t, bar_fill=bars, part=part,
            activo_p=f >= 5, pie=pie_b, **base)
    # 5. actualización (un paso de descenso por gradiente, con este par)
    grad_full = {k: "total" for k in BLOQUES}
    bars_full = {k: 1.0 for k in BLOQUES}
    pie_u = (f"actualización: W ← W − η·∂L/∂W, η = {fmt(ETA)}; L de este par:"
             f" {fmt(fd['L'], 3)} → {fmt(despues['L'], 3)}")
    for f in range(24):
        cap(fase=4, grad=grad_full, bar_fill=bars_full, update_t=f / 16,
            foto2=despues, pie=pie_u, **base)
    # 6. épocas rápidas: caras = |∂L/∂·| con la escala fija del paso mostrado
    base5 = dict(fw={k: 1.0 for k in BLOQUES}, grad=grad_full, p_t=1,
                 f_alpha=1, l_t=1, sondas=True, ver_L=True)
    for e in range(E_DET + 1, EPOCAS + 1):
        fo = fotos[e]
        n = 3 if e < E_DET + 6 else 2 if e < 20 else 1
        cap(n, fase=5, foto=fo, curva_hasta=e,
            pie=f"Se repite: {N_AUG + 1} pasos por época · época {e},"
                f" L = {fmt(fo['L'], 3)}, IoU = {fmt(fo['iou'])}", **base5)
    f0, fF = fotos[0], fotos[-1]
    cap(1, fase=5, foto=fF, curva_hasta=EPOCAS,
        pie=f"Tras {EPOCAS} épocas: L baja de {fmt(f0['L'])} a {fmt(fF['L'])}"
            f" y el IoU sube a {fmt(fF['iou'])} · FCN se entrena igual",
        **base5)
    plt.close(fig)
    # escritura atómica: se escribe al lado y se reemplaza al final
    png = os.path.join(OUT, "segmentacion-entrenamiento.png")
    gif = os.path.join(OUT, "segmentacion-entrenamiento.gif")
    fr[-1].save(png + ".tmp.png")
    guardar_gif(fr, gif + ".tmp.gif", fps=fps, pausa_s=pausa_s, colores=96)
    os.replace(png + ".tmp.png", png)
    os.replace(gif + ".tmp.gif", gif)
    print(f"{len(fr)} cuadros, {len(fr) / fps + pausa_s:.1f} s por ciclo")
    return fr


if __name__ == "__main__":
    frames = segmentacion_entrenamiento()
    dbg = os.environ.get("DBG_DIR")
    if dbg:
        os.makedirs(dbg, exist_ok=True)
        n = len(frames)
        for i in (8, 40, 72, 100, 125, 140, 160, 185, n - 1):
            if i < n:
                frames[i].save(os.path.join(dbg, f"cuadro-{i:03d}.png"))
