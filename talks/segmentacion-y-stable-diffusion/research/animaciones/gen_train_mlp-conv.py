#!/usr/bin/env python3
"""Animaciones de ENTRENAMIENTO de la red densa y del kernel convolucional
(Talk "segmentacion-y-stable-diffusion").

  mlp-entrenamiento.gif (+ .png)   MLP real de juguete 64 -> 16 -> 12 -> 10
                                   sobre dígitos sintéticos de 8x8, entrenado
                                   con entropía cruzada y descenso por
                                   gradiente: dato y objetivo one-hot ->
                                   forward -> pérdida -> backward capa por capa
                                   -> promedio del mini-batch -> actualización
                                   -> 40 pasos con la pérdida bajando
  conv-entrenamiento.gif (+ .png)  un kernel 3x3 que arranca al azar y se
                                   entrena por descenso de gradiente para que
                                   su feature map iguale al mapa de bordes
                                   verticales de la grilla 7x7 de
                                   conv2d-kernel.gif; ∂L/∂kernel se acumula
                                   posición por posición

Todo se calcula con numpy: los gradientes son analíticos y se verifican
contra diferencias finitas con asserts. Reusa paleta y helpers de
gen_animaciones_conv.py y gen_anim_mlp-emb.py (que no se modifican).

Uso:  python3 gen_train_mlp-conv.py [mlp-entrenamiento|conv-entrenamiento]
      CUADROS_DIR=<carpeta> guarda cuadros de verificación.
"""
import importlib.util
import os
import sys

import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from gen_animaciones_conv import (  # noqa: E402
    plt, TINTA, ROJO, ROJO_CLARO, RELLENO, GRIS_MEDIO, W, H, DPI, OUT,
    capturar, guardar_gif)
from matplotlib.collections import LineCollection  # noqa: E402
from matplotlib.colors import to_rgb  # noqa: E402
from matplotlib.patches import (  # noqa: E402
    Circle, FancyBboxPatch, Polygon, Rectangle)
from PIL import Image, ImageDraw, ImageFont  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "gen_anim_mlp_emb", os.path.join(AQUI, "gen_anim_mlp-emb.py"))
_mlpemb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mlpemb)
gris_rgb, hex_rgb = _mlpemb.gris_rgb, _mlpemb.hex_rgb
FUENTE_B = _mlpemb.FUENTE_B

PX_W, PX_H = W * DPI, H * DPI
GRIS_LINEA = "#DDD7D5"
BORDE = "#CFC8C6"
TINTA_DIV = "#3A3A3A"
CUADROS = os.environ.get("CUADROS_DIR")


# --- helpers de dibujo (px, y hacia abajo) ---------------------------------
def figura():
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    return fig, ax


def lienzo(ax):
    ax.clear()
    ax.set_xlim(0, PX_W)
    ax.set_ylim(PX_H, 0)
    ax.axis("off")


def txt(ax, x, y, s, size=20, color=TINTA, bold=False, ha="center",
        va="center", z=6, **kw):
    ax.text(x, y, s, fontsize=size, color=color, ha=ha, va=va, zorder=z,
            fontweight="bold" if bold else "normal", **kw)


def rect(ax, x, y, w, h, fc="white", ec=TINTA, lw=1.5, z=3, ls="-",
         alpha=1.0):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=lw, zorder=z,
                           ls=ls, alpha=alpha))


def pie(ax, texto, color=TINTA, negrita=False):
    txt(ax, PX_W / 2, PX_H - 42, texto, size=22, color=color, bold=negrita)


def div_rgb(M, escala):
    """Diverge: negativo gris oscuro, 0 blanco, positivo rojo (escala fija)."""
    t = np.clip(np.asarray(M, float) / (escala + 1e-12), -1, 1)[..., None]
    blanco = np.ones(3)
    rojo, tinta = np.array(to_rgb(ROJO)), np.array(to_rgb(TINTA_DIV))
    return np.where(t >= 0, blanco + t * (rojo - blanco),
                    blanco + (-t) * (tinta - blanco))


def mezcla(c1, c2, t):
    a, b = np.array(to_rgb(c1)), np.array(to_rgb(c2))
    return tuple(a + (b - a) * float(np.clip(t, 0, 1)))


def guardar_gif_atomico(frames, ruta, **kw):
    """guardar_gif sobre un temporal y rename: si el proceso se corta, el GIF
    anterior queda intacto en vez de quedar a medio escribir."""
    tmp = ruta[:-4] + ".tmp.gif"
    guardar_gif(frames, tmp, **kw)
    os.replace(tmp, ruta)


def guardar_png_atomico(fig, ruta):
    tmp = ruta[:-4] + ".tmp.png"
    fig.savefig(tmp, dpi=DPI, facecolor="white")
    os.replace(tmp, ruta)


def suave(t):
    t = float(np.clip(t, 0, 1))
    return t * t * (3 - 2 * t)


def coma(v, d=2):
    s = f"{v:.{d}f}".replace(".", ",").replace("-", "−")
    return "0," + "0" * d if s in ("−0," + "0" * d,) else s


def digito8(caracter, lado=8, tam=10, esc=16):
    """Dígito sintético de lado×lado en [0,1] (tinta = 1): la letra se dibuja
    a 16× y se promedia por bloques (sin desenfoque extra, más nítido que el
    helper de gen_anim_mlp-emb.py a 8×8)."""
    im = Image.new("L", (lado * esc, lado * esc), 0)
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(FUENTE_B, tam * esc)
    bb = d.textbbox((0, 0), caracter, font=f)
    x = (lado * esc - (bb[2] - bb[0])) / 2 - bb[0]
    y = (lado * esc - (bb[3] - bb[1])) / 2 - bb[1]
    d.text((x, y), caracter, fill=255, font=f)
    a = np.asarray(im.resize((lado, lado), Image.BOX), float) / 255
    return np.clip(a / a.max(), 0, 1)


# =========================================================================
# 1. mlp-entrenamiento.gif
# =========================================================================
MT_ETA = 0.2
MT_PASOS = 40
MT_SEMILLA = 29
MT_INIT = 1.5                              # ×(inicialización de He)
MT_C = 3                                   # el dígito que se sigue en detalle
MT_TAM = (64, 16, 12, 10)


def _mt_forward(P, X):
    W1, b1, W2, b2, W3, b3 = P
    z1 = X @ W1.T + b1
    h1 = np.maximum(z1, 0)
    z2 = h1 @ W2.T + b2
    h2 = np.maximum(z2, 0)
    z3 = h2 @ W3.T + b3
    p = np.exp(z3 - z3.max(1, keepdims=True))
    p /= p.sum(1, keepdims=True)
    return dict(z1=z1, h1=h1, z2=z2, h2=h2, z3=z3, p=p)


def _mt_perdida(P, X, Y):
    p = _mt_forward(P, X)["p"]
    return -np.mean(np.log((p * Y).sum(1)))


def _mt_grad(P, X, Y, f):
    """Backward analítico de la entropía cruzada promedio sobre las filas."""
    n = len(X)
    d3 = (f["p"] - Y) / n                          # δ de la salida
    d2 = (d3 @ P[4]) * (f["z2"] > 0)               # regla de la cadena
    d1 = (d2 @ P[2]) * (f["z1"] > 0)
    g = [d1.T @ X, d1.sum(0), d2.T @ f["h1"], d2.sum(0), d3.T @ f["h2"],
         d3.sum(0)]
    return dict(d3=d3 * n, d2=d2 * n, d1=d1 * n, g=g)


def _mt_datos():
    imgs = np.array([digito8(str(d)) for d in range(10)])    # 8x8 en [0,1]
    X = imgs.reshape(10, 64) - 0.5                   # píxeles centrados en 0
    Y = np.eye(10)
    rng = np.random.default_rng(MT_SEMILLA)
    k = MT_INIT
    P = [rng.normal(0, k * np.sqrt(2 / 64), (16, 64)), np.full(16, 0.05),
         rng.normal(0, k * np.sqrt(2 / 16), (12, 16)), np.full(12, 0.05),
         rng.normal(0, k * np.sqrt(1 / 12), (10, 12)), np.zeros(10)]

    # --- verificación de gradientes contra diferencias finitas -----------
    eps = 1e-6
    for Xs, Ys in ((X, Y), (X[MT_C:MT_C + 1], Y[MT_C:MT_C + 1])):
        g = _mt_grad(P, Xs, Ys, _mt_forward(P, Xs))["g"]
        rng_c = np.random.default_rng(1)
        for k, A in enumerate(P):
            for _ in range(6):
                idx = tuple(rng_c.integers(0, s) for s in A.shape)
                Pp = [a.copy() for a in P]
                Pm = [a.copy() for a in P]
                Pp[k][idx] += eps
                Pm[k][idx] -= eps
                num = (_mt_perdida(Pp, Xs, Ys) -
                       _mt_perdida(Pm, Xs, Ys)) / (2 * eps)
                assert abs(num - g[k][idx]) < 1e-6 + 1e-5 * abs(num), \
                    (k, idx, num, g[k][idx])

    est = []
    for s in range(MT_PASOS + 1):
        fb = _mt_forward(P, X)
        gb = _mt_grad(P, X, Y, fb)
        f3 = _mt_forward(P, X[MT_C:MT_C + 1])
        g3 = _mt_grad(P, X[MT_C:MT_C + 1], Y[MT_C:MT_C + 1], f3)
        est.append(dict(
            P=[a.copy() for a in P], p=fb["p"],
            L=-np.mean(np.log(fb["p"][np.arange(10), np.arange(10)])),
            h1=f3["h1"][0], h2=f3["h2"][0], p3=f3["p"][0],
            L3=-np.log(f3["p"][0, MT_C]),
            d3=g3["d3"][0], d2=g3["d2"][0], d1=g3["d1"][0],
            g3=[g3["g"][0], g3["g"][2], g3["g"][4]],
            gb=[gb["g"][0], gb["g"][2], gb["g"][4]]))
        P = [a - MT_ETA * gg for a, gg in zip(P, gb["g"])]   # W ← W − η·∂L/∂W

    Ls = [e["L"] for e in est]
    assert all(b < a for a, b in zip(Ls, Ls[1:])), "la pérdida no baja"
    assert est[-1]["p3"][MT_C] > 0.8 > 0.15 > est[0]["p3"][MT_C]
    assert (est[-1]["p"].argmax(1) == np.arange(10)).all()
    assert X.shape[1] == 8 * 8 == MT_TAM[0]
    assert [a.shape for a in est[0]["P"][::2]] == [(16, 64), (12, 16),
                                                   (10, 12)]
    # escalas FIJAS (las del paso 0): el gradiente se apaga si L baja
    esc = dict(
        a1=max(e["h1"].max() for e in est),
        a2=max(e["h2"].max() for e in est),
        d=[np.abs(est[0][k]).max() for k in ("d1", "d2", "d3")],
        g=[0.8 * np.abs(est[0]["gb"][i]).max() for i in range(3)])
    return dict(imgs=imgs, X=X, est=est, esc=esc)


# --- geometría -------------------------------------------------------------
MT_PX = 25                                   # px de pantalla por píxel
MT_IMG = (80, 245)                           # esquina sup. izq. de la imagen
MT_SX0, MT_SX1 = 395, 435                    # columna de entrada
MT_SY0, MT_SLOT = 150, 390
MT_X = (710, 995, 1280)                      # capa 1, capa 2, salida
MT_R = 11.5
MT_YS = (np.linspace(162, 528, 16), np.linspace(184, 506, 12),
         np.linspace(210, 480, 10))
MT_FUENTES = MT_SY0 + (np.arange(64) + 0.5) * MT_SLOT / 64
MT_LBL_X, MT_BAR_X0, MT_BAR_MAX = 1312, 1336, 140
MT_YC_X = 1530                               # columna del objetivo y
MT_HM_W, MT_HM_Y, MT_HM_H = 250, 606, 144    # heatmaps de ∂L/∂W
MT_HM_CX = ((MT_SX1 + MT_X[0]) / 2, (MT_X[0] + MT_X[1]) / 2,
            (MT_X[1] + MT_X[2]) / 2)
MT_TH = (70, 606, 50, 12, 84)                # miniaturas: x0, y0, lado, gap,
#                                              salto de fila
MT_LP = (1422, 1335, 1555, 694, 784)         # panel L: cx, curva x0 x1 y0 y1


def _mt_dibujar(ax, D, e, *, filas=8, n=(16, 12, 10), activa=None,
                probs=1.0, ver_y=True, sel=True, perdida=0, delta=(0, 0, 0),
                back=None, g_filas=(0, 0, 0), gmix=0.0, lote=0, lote_p=False,
                update=0.0, formula_upd=False, curva_n=0, paso=None,
                texto_pie="", pie_rojo=False, eg=None):
    """n: neuronas ya calculadas en el forward (capa 1, capa 2, salida).
    activa: capa del forward en curso ('c1','c2','out').
    delta: neuronas con δ ya asignado (capa 1, capa 2, salida); back: capa del
    backward en curso (0, 1, 2). g_filas: filas visibles de ∂L/∂W por capa.
    gmix: 0 = gradiente del «3», 1 = promedio del mini-batch.
    lote: miniaturas ya procesadas en la escena del promedio.
    eg: estado del que salen los gradientes (por defecto, e); en la
    actualización se muestra el gradiente que se está aplicando."""
    lienzo(ax)
    est, esc = D["est"], D["esc"]
    p3 = e["p3"]

    # ---------- encabezados
    def encab(x, l1, l2, l3=None, rojo3=False):
        txt(ax, x, 50, l1, size=22, bold=True)
        txt(ax, x, 84, l2, size=20, color=GRIS_MEDIO)
        if l3:
            txt(ax, x, 114, l3, size=18, color=ROJO if rojo3 else GRIS_MEDIO,
                bold=rojo3)
    encab(180, "imagen", "8×8 píxeles")
    encab((MT_SX0 + MT_SX1) / 2, "entrada", "64 valores")
    se = "W₁ · se entrena", "W₂ · se entrena", "W₃ · se entrena"
    encab(MT_X[0], "capa densa 1", "16 neuronas", se[0], True)
    encab(MT_X[1], "capa densa 2", "12 neuronas", se[1], True)
    encab((MT_X[2] - MT_R + MT_YC_X + 14) / 2, "salida", "10 clases", se[2],
          True)

    # ---------- imagen
    img = D["imgs"][MT_C]
    ix0, iy0 = MT_IMG
    lado = 8 * MT_PX
    ax.imshow(gris_rgb(img), extent=(ix0, ix0 + lado, iy0 + lado, iy0),
              interpolation="nearest", zorder=2)
    rect(ax, ix0, iy0, lado, lado, fc="none", ec=ROJO if sel else TINTA,
         lw=3 if sel else 1.6, z=4)
    for k in range(1, 8):
        ax.plot([ix0 + k * MT_PX] * 2, [iy0, iy0 + lado], color="#BBBBBB",
                lw=0.5, zorder=2.5, alpha=0.6)
        ax.plot([ix0, ix0 + lado], [iy0 + k * MT_PX] * 2, color="#BBBBBB",
                lw=0.5, zorder=2.5, alpha=0.6)
    txt(ax, ix0 + lado / 2, iy0 + lado + 32, "etiqueta: 3", size=20,
        color=ROJO if sel else TINTA, bold=True)

    # ---------- vector de entrada
    paso_v = MT_SLOT / 64
    col = np.tile(hex_rgb(RELLENO), (64, 1))
    col[: filas * 8] = gris_rgb(img.ravel()[: filas * 8])
    ax.imshow(col[:, None, :], extent=(MT_SX0, MT_SX1, MT_SY0 + MT_SLOT,
                                       MT_SY0),
              interpolation="nearest", aspect="auto", zorder=2)
    rect(ax, MT_SX0, MT_SY0, MT_SX1 - MT_SX0, MT_SLOT, fc="none", lw=1.8, z=4)
    if 0 < filas < 8 or activa == "aplanar":
        r = filas - 1
        ry0, ry1 = iy0 + r * MT_PX, iy0 + (r + 1) * MT_PX
        sy0, sy1 = MT_SY0 + r * 8 * paso_v, MT_SY0 + (r + 1) * 8 * paso_v
        ax.add_patch(Polygon([(ix0 + lado, ry0), (MT_SX0, sy0),
                              (MT_SX0, sy1), (ix0 + lado, ry1)], closed=True,
                             fc=ROJO, alpha=0.22, ec="none", zorder=3))
        rect(ax, ix0, ry0, lado, MT_PX, fc="none", ec=ROJO, lw=2.6, z=5)
        rect(ax, MT_SX0, sy0, MT_SX1 - MT_SX0, sy1 - sy0, fc="none", ec=ROJO,
             lw=2.6, z=5)

    # ---------- conexiones
    xs_izq = (MT_SX1, MT_X[0] + MT_R, MT_X[1] + MT_R)
    xs_der = (MT_X[0] - MT_R, MT_X[1] - MT_R, MT_X[2] - MT_R)
    ys_izq = (MT_FUENTES, MT_YS[0], MT_YS[1])
    for c in range(3):
        segs = [[(xs_izq[c], ya), (xs_der[c], yb)] for yb in MT_YS[c]
                for ya in ys_izq[c]]
        ax.add_collection(LineCollection(segs, colors=GRIS_LINEA, lw=0.6,
                                         zorder=1))
        if update > 0:
            ax.add_collection(LineCollection(segs, colors=ROJO, lw=0.7,
                                             alpha=0.55 * update, zorder=1.2))
    nombres = ("c1", "c2", "out")
    for c in range(3):
        if activa == nombres[c] and n[c] > 0:          # abanico del forward
            yb = MT_YS[c][n[c] - 1]
            act = [[(xs_izq[c], ya), (xs_der[c], yb)] for ya in ys_izq[c]]
            ax.add_collection(LineCollection(act, colors=ROJO, lw=1.3,
                                             alpha=0.75, zorder=1.5))
    if back is not None and back < 2 and delta[back] > 0:   # abanico backward
        c = back
        ya = MT_YS[c][delta[c] - 1]
        act = [[(MT_X[c] + MT_R, ya), (MT_X[c + 1] - MT_R, yb)]
               for yb in MT_YS[c + 1]]
        ax.add_collection(LineCollection(act, colors=ROJO, lw=1.4,
                                         alpha=0.8, zorder=1.5))

    # ---------- neuronas
    acts = (e["h1"] / esc["a1"], e["h2"] / esc["a2"], p3)
    deltas = (e["d1"], e["d2"], e["d3"])
    for c in range(3):
        for j, y in enumerate(MT_YS[c]):
            ec, lw = TINTA, 1.6
            if j < delta[c]:
                fc = tuple(div_rgb(deltas[c][j], esc["d"][c]))
                if back == c and j == delta[c] - 1:
                    ec, lw = ROJO, 3.2
            elif j < n[c]:
                if activa == nombres[c] and j == n[c] - 1:
                    fc, ec, lw = ROJO, ROJO, 2.4
                else:
                    fc = tuple(gris_rgb(0.12 + 0.75 * min(acts[c][j], 1)))
            else:
                fc = "white"
            ax.add_patch(Circle((MT_X[c], y), MT_R, fc=fc, ec=ec, lw=lw,
                                zorder=4))

    # ---------- salida: dígitos, p (softmax) y objetivo y
    yo = MT_YS[2]
    txt(ax, MT_BAR_X0 + MT_BAR_MAX / 2, yo[0] - 36, "p", size=20, bold=True)
    if ver_y:
        txt(ax, MT_YC_X, yo[0] - 36, "y", size=20, bold=True, color=ROJO)
    for d, y in enumerate(yo):
        roja = d == MT_C and (perdida > 0 or ver_y)
        txt(ax, MT_LBL_X, y, str(d), size=19, color=ROJO if roja else TINTA,
            bold=roja)
        rect(ax, MT_BAR_X0, y - 10, MT_BAR_MAX, 20, fc=RELLENO, ec="none",
             z=2)
        if probs > 0:
            L = MT_BAR_MAX * p3[d] * probs
            rect(ax, MT_BAR_X0, y - 10, max(L, 1.5), 20,
                 fc=ROJO if d == MT_C else GRIS_MEDIO, ec="none", z=3)
        if ver_y:
            uno = d == MT_C
            rect(ax, MT_YC_X - 14, y - 14, 28, 28, fc=ROJO if uno else "white",
                 ec=ROJO if uno else BORDE, lw=1.4, z=3)
            txt(ax, MT_YC_X, y + 1, "1" if uno else "0", size=18,
                color="white" if uno else GRIS_MEDIO, bold=uno)
    ax.plot([MT_BAR_X0] * 2, [yo[0] - 18, yo[-1] + 18], color=TINTA, lw=1.4,
            zorder=3)
    if probs >= 1:
        yy = yo[MT_C]
        L = MT_BAR_MAX * p3[MT_C]
        if L > 70:                       # barra larga: el valor va adentro
            txt(ax, MT_BAR_X0 + L - 6, yy, coma(p3[MT_C]), size=18,
                ha="right", color="white", bold=True, z=7)
        else:
            txt(ax, MT_BAR_X0 + L + 8, yy, coma(p3[MT_C]), size=18,
                ha="left", color=ROJO, bold=True, z=7,
                bbox=dict(fc="white", ec="none", pad=1.0, alpha=0.85))

    # ---------- heatmaps de ∂L/∂W (escala fija)
    nombres_w = (("∂L/∂W₁", "16 × 64"), ("∂L/∂W₂", "12 × 16"),
                 ("∂L/∂W₃", "10 × 12"))
    for c in range(3):
        x0 = MT_HM_CX[c] - MT_HM_W / 2
        eg_ = e if eg is None else eg
        G = (1 - gmix) * eg_["g3"][c] + gmix * eg_["gb"][c]
        visible = g_filas[c] > 0
        if formula_upd:
            titulo = f"W{'₁₂₃'[c]} ← W{'₁₂₃'[c]} − η·∂L/∂W{'₁₂₃'[c]}"
            txt(ax, MT_HM_CX[c], MT_HM_Y - 20, titulo, size=18, color=ROJO)
        else:
            nom, dims = nombres_w[c]
            txt(ax, MT_HM_CX[c], MT_HM_Y - 20, f"{nom}  ({dims})", size=19,
                bold=True, color=ROJO if visible else GRIS_MEDIO)
        if visible:
            rgb = np.ones(G.shape + (3,))
            nf = g_filas[c]
            rgb[:nf] = div_rgb(G[:nf], esc["g"][c])
            ax.imshow(rgb, extent=(x0, x0 + MT_HM_W, MT_HM_Y + MT_HM_H,
                                   MT_HM_Y),
                      interpolation="nearest", aspect="auto", zorder=2)
            filas_tot = G.shape[0]
            if back == c and delta[c] == nf:
                hy = MT_HM_H / filas_tot
                rect(ax, x0 - 2, MT_HM_Y + (nf - 1) * hy - 1, MT_HM_W + 4,
                     hy + 2, fc="none", ec=ROJO, lw=2.6, z=6)
            if nf == filas_tot:
                norma = f"‖∂L/∂W{'₁₂₃'[c]}‖ = {coma(np.linalg.norm(G))}"
                txt(ax, MT_HM_CX[c], MT_HM_Y + MT_HM_H + 24, norma, size=18,
                    color=ROJO, bold=True)
        rect(ax, x0, MT_HM_Y, MT_HM_W, MT_HM_H, fc="none",
             ec=ROJO if visible else BORDE, lw=2 if visible else 1.4,
             ls="-" if visible else "--", z=5)
    if any(g_filas):
        txt(ax, MT_HM_CX[1], MT_HM_Y + MT_HM_H + 58,
            "escala fija: rojo +, gris −, blanco 0", size=18,
            color=GRIS_MEDIO)

    # ---------- mini-batch
    tx0, ty0, tl, tg, tdy = MT_TH
    txt(ax, tx0 + (5 * tl + 4 * tg) / 2, MT_HM_Y - 20, "mini-batch: 10 dígitos",
        size=19, bold=True)
    for d in range(10):
        fx = tx0 + (d % 5) * (tl + tg)
        fy = ty0 + (d // 5) * tdy
        ax.imshow(gris_rgb(D["imgs"][d]), extent=(fx, fx + tl, fy + tl, fy),
                  interpolation="nearest", zorder=2)
        es3 = d == MT_C and sel
        hecho = 0 < lote and (d < lote or d == MT_C)
        activo = lote > 0 and d == lote - 1 and d != MT_C
        ec = ROJO if (es3 or activo) else (TINTA if not hecho else ROJO)
        lw = 3 if es3 or activo else (1.2 if not hecho else 1.8)
        rect(ax, fx, fy, tl, tl, fc="none", ec=ec, lw=lw, z=4)
        if lote_p:
            rect(ax, fx, fy + tl + 5, tl, 8, fc=RELLENO, ec="none", z=3)
            rect(ax, fx, fy + tl + 5, tl * e["p"][d, d], 8, fc=ROJO,
                 ec="none", z=4)
    if lote_p:
        txt(ax, tx0 + (5 * tl + 4 * tg) / 2, MT_HM_Y + MT_HM_H + 24,
            "barra: p(dígito correcto)", size=18, color=GRIS_MEDIO)

    # ---------- panel de la pérdida
    cx, cx0, cx1, cy0, cy1 = MT_LP
    if perdida >= 1:
        txt(ax, cx, MT_HM_Y - 20, "L = −log p(3)", size=21, bold=True,
            color=ROJO)
    if perdida >= 2:
        txt(ax, cx, MT_HM_Y + 14,
            f"= −log {coma(p3[MT_C])} = {coma(e['L3'])}", size=20,
            color=ROJO)
    if perdida >= 3:
        txt(ax, cx, MT_HM_Y + 50, f"mini-batch: L = {coma(e['L'])}",
            size=18, color=TINTA)
    ax.plot([cx0, cx0, cx1], [cy0, cy1, cy1], color=TINTA, lw=1.4, zorder=3)
    txt(ax, cx0 - 8, cy0 + 4, "L", size=18, color=GRIS_MEDIO, ha="right")
    txt(ax, cx1, cy1 + 20, "paso" if paso is None else f"paso {paso}",
        size=18, color=GRIS_MEDIO, ha="right")
    if curva_n:
        Ls = [s["L"] for s in est]
        lmax = Ls[0] * 1.05
        xs = [cx0 + (cx1 - cx0) * k / MT_PASOS for k in range(curva_n)]
        ys = [cy1 - (cy1 - cy0) * Lv / lmax for Lv in Ls[:curva_n]]
        ax.plot(xs, ys, color=ROJO, lw=2.5, zorder=4)
        ax.plot(xs[-1:], ys[-1:], "o", color=ROJO, ms=6, zorder=5)

    if texto_pie:
        pie(ax, texto_pie, color=ROJO if pie_rojo else TINTA,
            negrita=pie_rojo)


def mlp_entrenamiento(fps=12, pausa_s=3.0):
    D = _mt_datos()
    est = D["est"]
    e0, e1, eF = est[0], est[1], est[-1]
    fig, ax = figura()
    frames = []

    def toma(rep=1, e=e0, **kw):
        _mt_dibujar(ax, D, e, **kw)
        f = capturar(fig)
        frames.extend([f] * rep)

    p0 = coma(e0["p3"][MT_C])
    nada = dict(filas=0, n=(0, 0, 0), probs=0)
    # 1. dato y objetivo
    pie_dato = ("modelo de juguete en numpy: un «3» de 8×8 y su objetivo "
                "one-hot y (1 en la clase 3)")
    toma(6, ver_y=False, sel=False, texto_pie=pie_dato, **nada)
    toma(8, texto_pie=pie_dato, **nada)
    # 2. forward
    pie_ap = "forward: la imagen se aplana en 8 · 8 = 64 valores (píxel − 0,5)"
    for r in (2, 4, 6, 8):
        toma(1 if r < 8 else 3, filas=r, n=(0, 0, 0), probs=0,
             activa="aplanar", texto_pie=pie_ap)
    pies_fw = ("forward: capa densa 1 = ReLU(W₁·x + b₁) → 16 valores",
               "forward: capa densa 2 = ReLU(W₂·h₁ + b₂) → 12 valores",
               "forward: salida = W₃·h₂ + b₃ → 10 valores")
    for c, tot in enumerate((16, 12, 10)):
        for k in range(2, tot + 1, 2):
            nn = [16, 12, 10][:c] + [k] + [0, 0, 0][c + 1:]
            toma(1, n=tuple(nn[:3]), probs=0, activa=("c1", "c2", "out")[c],
                 texto_pie=pies_fw[c])
        toma(2, n=tuple(([16, 12, 10][:c + 1] + [0, 0])[:3]), probs=0,
             texto_pie=pies_fw[c])
    pie_sm = f"softmax: los 10 valores pasan a probabilidades p; p(3) = {p0}"
    for s in np.linspace(0.25, 1, 4):
        toma(1, probs=s, texto_pie=pie_sm)
    toma(8, texto_pie=pie_sm)
    # 3. pérdida
    pie_l = (f"pérdida: entropía cruzada L = −log p(3) = −log {p0} = "
             f"{coma(e0['L3'])}")
    toma(4, perdida=1, texto_pie=pie_l)
    toma(14, perdida=2, texto_pie=pie_l)
    # 4. backward, capa por capa (regla de la cadena)
    base = dict(perdida=2)
    pies_bw = ("backward: en la salida δ₃ = p − y; ∂L/∂W₃ = δ₃ · h₂ᵀ",
               "regla de la cadena: δ₂ = (W₃ᵀ·δ₃) ⊙ ReLU′ → ∂L/∂W₂ = δ₂ · h₁ᵀ",
               "regla de la cadena: δ₁ = (W₂ᵀ·δ₂) ⊙ ReLU′ → ∂L/∂W₁ = δ₁ · xᵀ")
    for k in range(2, 11, 2):
        toma(1, delta=(0, 0, k), back=2, g_filas=(0, 0, k),
             texto_pie=pies_bw[0], **base)
    toma(7, delta=(0, 0, 10), g_filas=(0, 0, 10), texto_pie=pies_bw[0],
         **base)
    for k in range(2, 13, 2):
        toma(1, delta=(0, k, 10), back=1, g_filas=(0, k, 10),
             texto_pie=pies_bw[1], **base)
    toma(9, delta=(0, 12, 10), g_filas=(0, 12, 10), texto_pie=pies_bw[1],
         **base)
    for k in range(2, 17, 2):
        toma(1, delta=(k, 12, 10), back=0, g_filas=(k, 12, 10),
             texto_pie=pies_bw[2], **base)
    toma(9, delta=(16, 12, 10), g_filas=(16, 12, 10), texto_pie=pies_bw[2],
         **base)
    # 5. mini-batch: promedio de los 10 gradientes
    todo = (16, 12, 10)
    pie_mb = ("lo mismo con los 10 dígitos del mini-batch: L y ∂L/∂W son el "
              "promedio de los 10")
    for k in range(2, 11, 2):
        toma(1, delta=todo, g_filas=todo, lote=k, perdida=2,
             texto_pie=pie_mb)
    for t in np.linspace(0, 1, 6):
        toma(1, delta=todo, g_filas=todo, lote=10, gmix=suave(t),
             perdida=3, texto_pie=pie_mb)
    toma(8, delta=todo, g_filas=todo, lote=10, gmix=1, perdida=3,
         curva_n=1, paso=0, texto_pie=pie_mb)
    # 6. actualización
    p1 = coma(e1["p3"][MT_C])
    pie_up = (f"actualización: W ← W − η·∂L/∂W en las 3 capas (η = "
              f"{coma(MT_ETA, 1)}); p(3) pasa de {p0} a {p1}")
    for t in np.linspace(0, 1, 5):
        toma(1, g_filas=todo, gmix=1, perdida=3, update=suave(t),
             formula_upd=True, curva_n=1, paso=0, texto_pie=pie_up)
    toma(4, e=e1, eg=e0, g_filas=todo, gmix=1, perdida=3, update=1,
         formula_upd=True, curva_n=2, paso=1, texto_pie=pie_up)
    for t in np.linspace(1, 0, 4):
        toma(1, e=e1, eg=e0, g_filas=todo, gmix=1, perdida=3, update=t,
             formula_upd=True, curva_n=2, paso=1, texto_pie=pie_up)
    toma(5, e=e1, eg=e0, g_filas=todo, gmix=1, perdida=3, formula_upd=True,
         curva_n=2, paso=1, texto_pie=pie_up)
    # 7. muchos pasos rápidos
    for s in range(2, MT_PASOS + 1):
        e = est[s]
        toma(2 if s <= 6 else 1, e=e, g_filas=todo, gmix=1, perdida=3,
             lote_p=True, curva_n=s + 1, paso=s,
             texto_pie=(f"se repite forward → pérdida → backward → "
                        f"actualización: paso {s} de {MT_PASOS}, "
                        f"L = {coma(e['L'])}"))
    # cierre (cuadro fijo)
    pie_fin = (f"Tras {MT_PASOS} pasos: L del mini-batch baja de "
               f"{coma(e0['L'])} a {coma(eF['L'])} y p(3) sube de {p0} a "
               f"{coma(eF['p3'][MT_C])}")
    _mt_dibujar(ax, D, eF, g_filas=todo, gmix=1, perdida=3, lote_p=True,
                curva_n=MT_PASOS + 1, paso=MT_PASOS, texto_pie=pie_fin)
    frames.append(capturar(fig))
    guardar_png_atomico(fig, os.path.join(OUT, "mlp-entrenamiento.png"))
    plt.close(fig)
    guardar_gif_atomico(frames, os.path.join(OUT, "mlp-entrenamiento.gif"),
                        fps=fps, pausa_s=pausa_s, colores=96)
    print(f"{len(frames)} cuadros, {(len(frames) - 1) / fps + pausa_s:.1f} s")
    return frames


# =========================================================================
# 2. conv-entrenamiento.gif
# =========================================================================
# Entrada 7x7 con dos formas (barra horizontal y bloque), elegida para que los
# 25 parches de 3x3 determinen el kernel: con la grilla de conv2d-kernel.gif
# todas las filas son casi iguales y solo quedan fijadas las sumas por
# columna, así que el kernel no podría converger a [-1 0 +1] por fila.
CV_ENTRADA = np.array([
    [0, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 0],
    [1, 8, 8, 8, 8, 1, 1],
    [1, 9, 8, 9, 9, 0, 1],
    [1, 0, 1, 0, 1, 9, 8],
    [0, 1, 0, 0, 1, 8, 9],
    [0, 1, 0, 0, 0, 9, 8],
], float)
CV_KBORDES = np.array([[-1, 0, 1]] * 3, float)   # bordes verticales
CV_ETA = 0.006
CV_PASOS = 60
CV_SEMILLA = 11


def fmt(v, d):
    s = f"{v:.{d}f}"
    if float(s) == 0:
        s = s.lstrip("-")
    return s.replace(".", ",").replace("-", "−")


def _cv_conv(img, k):
    """Correlación 2D 'valid' (lo que hace una capa convolucional)."""
    n = img.shape[0] - k.shape[0] + 1
    return np.array([[(img[i:i + 3, j:j + 3] * k).sum() for j in range(n)]
                     for i in range(n)])


def _cv_datos():
    img = CV_ENTRADA
    obj = _cv_conv(img, CV_KBORDES)
    assert obj.shape == (5, 5) and 7 - 3 + 1 == 5
    pos = [(i, j) for i in range(5) for j in range(5)]

    def perdida(k):
        return np.mean((_cv_conv(img, k) - obj) ** 2)

    def gradiente(k):
        """∂L/∂kernel acumulado posición por posición (lo que se anima)."""
        y = _cv_conv(img, k)
        g = np.zeros((3, 3))
        parciales = []
        for (i, j) in pos:
            e = y[i, j] - obj[i, j]
            g = g + 2 / 25 * e * img[i:i + 3, j:j + 3]
            parciales.append((e, g.copy()))
        return g, parciales

    k = np.random.default_rng(CV_SEMILLA).normal(0, 0.5, (3, 3))
    # verificación: suma por posiciones = forma vectorial = diferencias finitas
    g0, _ = gradiente(k)
    X = np.array([img[i:i + 3, j:j + 3].ravel() for (i, j) in pos])
    gv = 2 / 25 * X.T @ (X @ k.ravel() - obj.ravel())
    assert np.allclose(g0.ravel(), gv)
    eps = 1e-6
    for a in range(3):
        for b in range(3):
            kp, km = k.copy(), k.copy()
            kp[a, b] += eps
            km[a, b] -= eps
            num = (perdida(kp) - perdida(km)) / (2 * eps)
            assert abs(num - g0[a, b]) < 1e-6 + 1e-6 * abs(num), (a, b)

    est = []
    for s in range(CV_PASOS + 1):
        g, parciales = gradiente(k)
        est.append(dict(k=k.copy(), y=_cv_conv(img, k), L=perdida(k), g=g,
                        parciales=parciales))
        k = k - CV_ETA * g                      # kernel ← kernel − η·∂L/∂k
    Ls = [e["L"] for e in est]
    assert all(b < a for a, b in zip(Ls, Ls[1:])), "la pérdida no baja"
    assert np.abs(est[-1]["k"] - CV_KBORDES).max() < 0.05
    return dict(img=img, obj=obj, pos=pos, est=est,
                esc_g=np.abs(est[0]["g"]).max())


# --- geometría (px, y hacia abajo) -----------------------------------------
# Fila de arriba: entrada × kernel → feature map, y la pérdida a la derecha.
# Fila de abajo: ∂L/∂kernel ← (salida − objetivo), con la cuenta a la derecha.
# La entrada ocupa las dos filas: la usan el forward y el gradiente.
CV_IN = (50, 213, 58)                 # x0, y0, celda de la entrada 7x7
CV_K = (500, 82, 100)                 # kernel 3x3
CV_G = (500, 478, 100)                # ∂L/∂kernel 3x3
CV_F = (850, 66, 64)                  # feature map 5x5
CV_O = (850, 466, 64)                 # objetivo 5x5
CV_TIT = (32, 441)                    # y de los títulos de cada fila
CV_P = 1370                           # centro del panel de la derecha
CV_CURVA = (1215, 1545, 222, 352)     # x0, x1, y0, y1
CV_INFO_Y = 478                       # primera línea de la cuenta
CV_ESC_MAPA = 27.0                    # escala fija de feature map y objetivo


def _cv_grilla(ax, x0, y0, c, M, escala, d, *, size=19, vacias=None):
    nf, nc = M.shape
    for i in range(nf):
        for j in range(nc):
            x, y = x0 + j * c, y0 + i * c
            if vacias is not None and not vacias[i, j]:
                rect(ax, x, y, c, c, fc="white", ec=BORDE, lw=1.4, z=3)
                continue
            v = M[i, j]
            rect(ax, x, y, c, c, fc=tuple(div_rgb(v, escala)), ec="white",
                 lw=2, z=3)
            col = "white" if abs(v) / escala > 0.55 else TINTA
            txt(ax, x + c / 2, y + c / 2 + 1, fmt(v, d), size=size, bold=True,
                color=col)


def _cv_dibujar(ax, D, e, *, n_y=25, ventana=None, celda=None, ver_L=False,
                n_acc=0, acc_on=False, k_vis=None, upd=False,
                curva_n=0, paso=None, info=None, final=False, texto_pie="",
                pie_rojo=False, eg=None, celda_obj=True):
    """n_y: celdas del feature map ya calculadas. ventana: (i, j) de la ventana
    sobre la entrada. celda: (i, j) resaltada en salida (y objetivo).
    n_acc: posiciones ya sumadas en ∂L/∂kernel (25 = gradiente completo).
    k_vis: kernel a mostrar (para interpolar la actualización).
    eg: estado del que sale ∂L/∂kernel (en la actualización, el que se aplicó).
    info: líneas (texto, tamaño, negrita, color) de la cuenta de abajo."""
    lienzo(ax)
    img, obj = D["img"], D["obj"]
    k = e["k"] if k_vis is None else k_vis
    y = _cv_conv(img, k) if k_vis is not None else e["y"]
    t_arr, t_aba = CV_TIT

    # ---------- entrada 7x7 (escala de grises como conv2d-kernel.gif)
    x0, y0, c = CV_IN
    txt(ax, x0 + 3.5 * c, y0 - 32, "Entrada (imagen 7×7)", size=22)
    txt(ax, x0 + 3.5 * c, y0 + 7 * c + 30, "no se entrena", size=18,
        color=GRIS_MEDIO)
    for i in range(7):
        for j in range(7):
            v = img[i, j]
            g = 1 - 0.62 * v / 9
            rect(ax, x0 + j * c, y0 + i * c, c, c, fc=(g, g, g * 0.985),
                 ec="white", lw=2, z=3)
            txt(ax, x0 + j * c + c / 2, y0 + i * c + c / 2 + 1, str(int(v)),
                size=22, bold=True, color=TINTA if v < 7 else "white")
    if ventana is not None:
        i, j = ventana
        rect(ax, x0 + j * c, y0 + i * c, 3 * c, 3 * c, fc=ROJO, ec="none",
             z=4, alpha=0.18)
        rect(ax, x0 + j * c, y0 + i * c, 3 * c, 3 * c, fc="none", ec=ROJO,
             lw=5, z=5)
    x_in1 = x0 + 7 * c

    # ---------- kernel
    kx, ky, kc = CV_K
    txt(ax, kx + 1.5 * kc, t_arr, "Kernel 3×3", size=21, bold=True,
        color=ROJO)
    txt(ax, kx + 1.5 * kc, t_arr + 29,
        "≈ [−1  0  +1] por fila" if final else "se entrena",
        size=18, bold=True, color=ROJO)
    _cv_grilla(ax, kx, ky, kc, k, 1.0, 2, size=20)
    rect(ax, kx, ky, 3 * kc, 3 * kc, fc="none", ec=ROJO, lw=4.5 if upd else 3,
         z=5)
    txt(ax, (x_in1 + kx) / 2, ky + 1.5 * kc, "×", size=34, color=GRIS_MEDIO)
    txt(ax, (kx + 3 * kc + CV_F[0]) / 2, ky + 1.5 * kc, "→", size=34,
        color=GRIS_MEDIO)

    # ---------- feature map y objetivo
    fx, fy, fc_ = CV_F
    txt(ax, fx + 2.5 * fc_, t_arr, "Feature map (salida)", size=21,
        bold=True)
    vacias = np.zeros((5, 5), bool)
    vacias.ravel()[:n_y] = True
    _cv_grilla(ax, fx, fy, fc_, y, CV_ESC_MAPA, 0, size=18, vacias=vacias)
    ox, oy, oc = CV_O
    txt(ax, ox + 2.5 * oc, t_aba, "Objetivo: bordes verticales", size=21,
        bold=True)
    _cv_grilla(ax, ox, oy, oc, obj, CV_ESC_MAPA, 0, size=18)
    if celda is not None:
        i, j = celda
        for (gx, gy, gc) in ((CV_F, CV_O) if celda_obj else (CV_F,)):
            rect(ax, gx + j * gc, gy + i * gc, gc, gc, fc="none", ec=ROJO,
                 lw=4, z=6)

    # ---------- ∂L/∂kernel (escala fija: la del paso 0)
    gx, gy, gc = CV_G
    activo = n_acc > 0
    txt(ax, gx + 1.5 * gc, t_aba, "∂L/∂kernel", size=21, bold=True,
        color=ROJO if activo else GRIS_MEDIO)
    if activo:
        G = (e if eg is None else eg)["parciales"][n_acc - 1][1]
        _cv_grilla(ax, gx, gy, gc, G, D["esc_g"], 1)
        rect(ax, gx, gy, 3 * gc, 3 * gc, fc="none", ec=ROJO,
             lw=3.5 if acc_on else 2, z=5)
        if n_acc == 25:
            txt(ax, gx + 1.5 * gc, gy + 3 * gc + 28,
                "suma de las 25 posiciones", size=18, color=GRIS_MEDIO)
    else:
        rect(ax, gx, gy, 3 * gc, 3 * gc, fc="none", ec=BORDE, lw=1.4,
             ls="--", z=5)
    txt(ax, (gx + 3 * gc + CV_O[0]) / 2, gy + 1.5 * gc, "←", size=34,
        color=ROJO if acc_on else GRIS_MEDIO)

    # ---------- panel de la pérdida
    col_L = ROJO if ver_L else GRIS_MEDIO
    txt(ax, CV_P, t_arr, "pérdida (MSE)", size=21, bold=True,
        color=ROJO if ver_L else TINTA)
    txt(ax, CV_P, 82, "L = promedio de las 25", size=18, color=col_L)
    txt(ax, CV_P, 110, "(salida − objetivo)²", size=18, color=col_L)
    if ver_L:
        txt(ax, CV_P, 164, f"L = {fmt(e['L'], 2)}", size=30, bold=True,
            color=ROJO)
    c0, c1, r0, r1 = CV_CURVA
    ax.plot([c0, c0, c1], [r0, r1, r1], color=TINTA, lw=1.4, zorder=3)
    txt(ax, c0 - 8, r0 + 4, "L", size=18, color=GRIS_MEDIO, ha="right")
    txt(ax, c1, r1 + 22, "paso" if paso is None else f"paso {paso}",
        size=18, color=GRIS_MEDIO, ha="right")
    if curva_n:
        Ls = [s["L"] for s in D["est"]]
        xs = [c0 + (c1 - c0) * q / CV_PASOS for q in range(curva_n)]
        ys = [r1 - (r1 - r0) * Lv / (Ls[0] * 1.05) for Lv in Ls[:curva_n]]
        ax.plot(xs, ys, color=ROJO, lw=2.5, zorder=4)
        ax.plot(xs[-1:], ys[-1:], "o", color=ROJO, ms=6, zorder=5)
    if info:
        for q, (linea, tam, neg, col) in enumerate(info):
            txt(ax, CV_P, CV_INFO_Y + 40 * q, linea, size=tam, bold=neg,
                color=col)

    if texto_pie:
        pie(ax, texto_pie, color=ROJO if pie_rojo else TINTA,
            negrita=pie_rojo)


def conv_entrenamiento(fps=12, pausa_s=3.0):
    D = _cv_datos()
    est, pos, obj = D["est"], D["pos"], D["obj"]
    e0, e1, eF = est[0], est[1], est[-1]
    fig, ax = figura()
    frames = []

    def toma(rep=1, e=e0, **kw):
        _cv_dibujar(ax, D, e, **kw)
        f = capturar(fig)
        frames.extend([f] * rep)

    eta_s = fmt(CV_ETA, 3)
    regla = [("actualización:", 19, True, ROJO),
             ("kernel ← kernel", 19, True, ROJO),
             ("− η · ∂L/∂kernel", 19, True, ROJO),
             (f"η = {eta_s}", 18, False, TINTA)]
    # 1. dato y objetivo
    pie_0 = ("modelo de juguete en numpy: un kernel 3×3 al azar tiene que "
             "reproducir el objetivo")
    toma(14, n_y=0, texto_pie=pie_0)
    # 2. forward: la ventana recorre la entrada
    pie_fw = ("forward: el kernel recorre la imagen; cada posición da una "
              "celda del feature map")
    for q, (i, j) in enumerate(pos):
        toma(1, n_y=q + 1, ventana=(i, j), celda=(i, j), celda_obj=False,
             texto_pie=pie_fw)
    toma(6, texto_pie=pie_fw)
    # 3. pérdida
    pie_l = (f"pérdida: error cuadrático medio entre salida y objetivo, "
             f"L = {fmt(e0['L'], 2)}")
    toma(16, ver_L=True, curva_n=1, paso=0, texto_pie=pie_l)
    # 4. gradiente: se acumula en las 25 posiciones
    pie_g = ("backward: ∂L/∂kernel se acumula en las 25 posiciones donde se "
             "aplicó el kernel")
    for q, (i, j) in enumerate(pos):
        err, _ = e0["parciales"][q]
        o_s = fmt(obj[i, j], 0)
        if obj[i, j] < 0:                 # «6,1 − (−1)», no «6,1 − −1»
            o_s = f"({o_s})"
        info = [(f"posición {q + 1} de 25", 19, True, TINTA),
                ("salida − objetivo", 18, False, TINTA),
                (f"= {fmt(e0['y'][i, j], 1)} − {o_s} = {fmt(err, 1)}", 18,
                 False, TINTA),
                ("∂L/∂kernel +=", 19, True, ROJO),
                (f"(2/25) · ({fmt(err, 1)}) · ventana", 18, False, ROJO)]
        toma(5 if q < 3 else 1, ventana=(i, j), celda=(i, j), ver_L=True,
             n_acc=q + 1, acc_on=True, curva_n=1, paso=0, info=info,
             texto_pie=pie_g)
    toma(10, ver_L=True, n_acc=25, curva_n=1, paso=0, texto_pie=pie_g,
         info=[("∂L/∂kernel =", 19, True, ROJO),
               ("(2/25) · Σ (salida − objetivo)", 18, False, ROJO),
               ("· ventana", 18, False, ROJO),
               ("en las 25 posiciones", 18, False, TINTA)])
    # 5. actualización
    pie_u = (f"actualización: kernel ← kernel − η · ∂L/∂kernel (η = {eta_s}); "
             f"L pasa de {fmt(e0['L'], 1)} a {fmt(e1['L'], 1)}")
    for t in np.linspace(0, 1, 8):
        kv = e0["k"] + suave(t) * (e1["k"] - e0["k"])
        toma(1, ver_L=True, n_acc=25, k_vis=kv, upd=True, curva_n=1, paso=0,
             info=regla, texto_pie=pie_u)
    toma(12, e=e1, eg=e0, ver_L=True, n_acc=25, upd=True, curva_n=2,
         paso=1, info=regla, texto_pie=pie_u)
    # 6. muchos pasos
    for s in range(2, CV_PASOS + 1):
        e = est[s]
        toma(2 if s <= 8 else 1, e=e, ver_L=True, n_acc=25, curva_n=s + 1,
             paso=s, info=regla,
             texto_pie=(f"se repite forward → pérdida → gradiente → "
                        f"actualización: paso {s} de {CV_PASOS}"))
    # cierre (cuadro fijo)
    _cv_dibujar(ax, D, eF, ver_L=True, n_acc=25, curva_n=CV_PASOS + 1,
                paso=CV_PASOS, info=regla, final=True,
                texto_pie="en una CNN nadie diseña los kernels: se aprenden",
                pie_rojo=True)
    frames.append(capturar(fig))
    guardar_png_atomico(fig, os.path.join(OUT, "conv-entrenamiento.png"))
    plt.close(fig)
    guardar_gif_atomico(frames, os.path.join(OUT, "conv-entrenamiento.gif"),
                        fps=fps, pausa_s=pausa_s, colores=64)
    print(f"{len(frames)} cuadros, {(len(frames) - 1) / fps + pausa_s:.1f} s")
    return frames


TAREAS = {"mlp-entrenamiento": mlp_entrenamiento,
          "conv-entrenamiento": conv_entrenamiento}

if __name__ == "__main__":
    for nombre in (sys.argv[1:] or TAREAS):
        frs = TAREAS[nombre]()
        if CUADROS:
            os.makedirs(CUADROS, exist_ok=True)
            n = len(frs)
            for k, i in enumerate((12, 60, 100, 130, 160, 200, n - 1)):
                if i < n:
                    frs[i].save(os.path.join(CUADROS, f"{nombre}-{k}.png"))
