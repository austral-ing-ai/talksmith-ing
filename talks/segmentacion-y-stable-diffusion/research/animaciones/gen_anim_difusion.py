#!/usr/bin/env python3
"""Animaciones de difusión de la Talk "segmentacion-y-stable-diffusion".

  difusion-en-vivo.gif (+ .png)  forward con schedule lineal de betas (T=1000)
                                 y reverse con un predictor de ruido condicionado
  unet-sd-en-vivo.gif  (+ .png)  la U-Net de Stable Diffusion con cross-attention
                                 activándose nivel por nivel

Todo es sintético (numpy). Reusa estilo y helpers de gen_animaciones_conv.py.
Uso:  python3 gen_anim_difusion.py [difusion-en-vivo|unet-sd-en-vivo]
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_animaciones_conv import (  # noqa: E402
    plt, TINTA, ROJO, RELLENO, GRIS_MEDIO, W, H, DPI, OUT, capturar,
    guardar_gif)
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

PX_W, PX_H = W * DPI, H * DPI
GRIS_BORDE = "#CFC8C6"


def figura():
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    return fig, ax


def lienzo(ax):
    ax.clear()
    ax.set_xlim(0, PX_W)
    ax.set_ylim(PX_H, 0)
    ax.axis("off")


def caja(ax, x, y, w, h, ec=TINTA, fc="white", lw=2, z=3, r=12):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle=f"round,pad=0,rounding_size={r}",
                                ec=ec, fc=fc, lw=lw, zorder=z))


def flecha(ax, xa, ya, xb, yb, color=TINTA, lw=2, z=4, ms=20):
    ax.annotate("", xy=(xb, yb), xytext=(xa, ya), zorder=z,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                mutation_scale=ms, shrinkA=0, shrinkB=0))


def titulo(ax, x, y, negrita, resto, fs=24):
    t = ax.text(x, y, negrita, fontsize=fs, fontweight="bold", color=TINTA,
                va="bottom")
    r = ax.figure.canvas.get_renderer()
    bb = t.get_window_extent(renderer=r)
    ax.text(x + bb.width, y, resto, fontsize=fs, color=TINTA, va="bottom")


def pie(ax, texto, fs=22):
    ax.text(PX_W / 2, PX_H - 46, texto, ha="center", va="center",
            fontsize=fs, color=TINTA)


# =========================================================================
# 1. difusion-en-vivo.gif
# =========================================================================
T = 1000
BETAS = np.linspace(1e-4, 0.02, T)          # schedule lineal (DDPM)
ALFA_BAR = np.cumprod(1 - BETAS)
HITOS = [0, 100, 250, 500, 750, 1000]      # x(t) que se muestran
TH = 150                                   # lado de cada miniatura (px)
X0_MARGEN = 60
GAP = (PX_W - 2 * X0_MARGEN - len(HITOS) * TH) / (len(HITOS) - 1)
XS = [X0_MARGEN + i * (TH + GAP) for i in range(len(HITOS))]
Y_FWD, Y_REV = 88, 393
# fila del predictor, centrada como grupo: condición → predictor → ruido
_CW, _G1, _PW, _G2, _ES = 270, 64, 340, 80, 120
_X = PX_W / 2 - (_CW + _G1 + _PW + _G2 + _ES) / 2
COND = dict(x=_X, y=670, w=_CW, h=90)
PRED = dict(x=_X + _CW + _G1, y=660, w=_PW, h=110)
EPS = dict(x=PRED["x"] + _PW + _G2, y=655, s=_ES)


def _difusion_datos():
    n = 64
    yy, xx = np.mgrid[0:n, 0:n] + 0.5
    r = np.hypot(xx - 32, yy - 32)
    disco = np.clip(17.5 - r, 0, 1)[..., None]           # borde suave
    fondo = np.array([0.94, 0.93, 0.92])
    rojo = np.array([0xD7, 0x19, 0x2A]) / 255
    img = fondo * (1 - disco) + rojo * disco
    x0 = img * 2 - 1                                     # escala [-1, 1]
    rng = np.random.default_rng(11)
    xs = np.empty((T + 1, n, n, 3), np.float32)
    xs[0] = x0
    for t in range(1, T + 1):                            # paso a paso, real
        b = BETAS[t - 1]
        xs[t] = np.sqrt(1 - b) * xs[t - 1] + np.sqrt(b) * rng.standard_normal(
            (n, n, 3))
    # ruido total presente en x(t): lo que una predicción perfecta devolvería
    ab = np.concatenate([[1.0], ALFA_BAR])
    eps = np.zeros_like(xs)
    for t in range(1, T + 1):
        eps[t] = (xs[t] - np.sqrt(ab[t]) * x0) / np.sqrt(1 - ab[t])
    return xs, eps, ab


def _a_rgb(x):
    return np.clip((x + 1) / 2, 0, 1)


def _ruido_rgb(e):
    return np.clip(0.5 + e / 5, 0, 1)


def _difusion_dibujar(ax, xs, eps, ab, fwd_hasta, fwd_activo=None, t_fwd=None,
                      rev_desde=None, rev_activo=None, t_rev=None,
                      final=False, texto_pie=None):
    """fwd_hasta: cantidad de miniaturas forward completas (desde la izq.).
    rev_desde: índice del hito más a la izquierda ya reconstruido en reverse
    (None = la fila reverse todavía no empezó)."""
    lienzo(ax)
    # títulos de fila
    titulo(ax, X0_MARGEN, Y_FWD - 22, "Forward", ": agregar ruido (entrenamiento)")
    ax.text(PX_W - X0_MARGEN, Y_FWD - 24,
            "schedule lineal: β de 0,0001 a 0,02 · T = 1000 pasos",
            fontsize=19, color=GRIS_MEDIO, va="bottom", ha="right")
    titulo(ax, X0_MARGEN, Y_REV - 22, "Reverse", ": quitar ruido (inferencia)")
    ax.text(PX_W - X0_MARGEN, Y_REV - 24, "cada miniatura: 64×64×3",
            fontsize=19, color=GRIS_MEDIO, va="bottom", ha="right")

    def miniatura(i, y, t, activo, etiqueta_t=None):
        x = XS[i]
        if t is None:
            ax.add_patch(Rectangle((x, y), TH, TH, fc=RELLENO, ec=GRIS_BORDE,
                                   lw=1.6, zorder=2))
        else:
            ax.imshow(_a_rgb(xs[t]), extent=(x, x + TH, y + TH, y),
                      interpolation="nearest", zorder=2)
            ax.add_patch(Rectangle((x, y), TH, TH, fill=False,
                                   ec=ROJO if activo else TINTA,
                                   lw=4 if activo else 1.8, zorder=3))
        tt = HITOS[i] if etiqueta_t is None else etiqueta_t
        nombre = "x0" if tt == 0 else ("xT" if tt == T else f"x{tt}")
        col = ROJO if activo else (TINTA if t is not None else GRIS_MEDIO)
        ax.text(x + TH / 2, y + TH + 10, nombre, ha="center", va="top",
                fontsize=22, fontweight="bold", color=col)
        if tt == 0:
            sub = "imagen limpia"
        elif tt == T:
            sub = "ruido puro"
        else:
            sub = f"señal {np.sqrt(ab[tt]):.2f}".replace(".", ",")
        ax.text(x + TH / 2, y + TH + 44, sub, ha="center", va="top",
                fontsize=19, color=col if activo else GRIS_MEDIO)

    def seg(i, y, hacia_izq, color, lw):
        xa = XS[i] + TH + 8
        xb = XS[i + 1] - 8
        if hacia_izq:
            xa, xb = xb, xa
        flecha(ax, xa, y + TH / 2, xb, y + TH / 2, color=color, lw=lw,
               ms=24 if lw > 2.5 else 20)

    # ---- fila forward
    for i in range(len(HITOS)):
        if i < fwd_hasta:
            miniatura(i, Y_FWD, HITOS[i], False)
        elif fwd_activo is not None and i == fwd_activo:
            miniatura(i, Y_FWD, t_fwd, True, etiqueta_t=t_fwd)
        else:
            miniatura(i, Y_FWD, None, False)
    for i in range(len(HITOS) - 1):
        act = fwd_activo is not None and i + 1 == fwd_activo
        hecho = i + 1 < fwd_hasta
        seg(i, Y_FWD, False, ROJO if act else (TINTA if hecho else GRIS_BORDE),
            3.5 if act else 2)

    # ---- fila reverse
    for i in range(len(HITOS)):
        if rev_desde is not None and i >= rev_desde:
            miniatura(i, Y_REV, HITOS[i], False)
        elif rev_activo is not None and i == rev_activo:
            miniatura(i, Y_REV, t_rev, True, etiqueta_t=t_rev)
        else:
            miniatura(i, Y_REV, None, False)
    for i in range(len(HITOS) - 1):
        act = rev_activo is not None and i == rev_activo
        hecho = rev_desde is not None and i >= rev_desde
        seg(i, Y_REV, True, ROJO if act else (TINTA if hecho else GRIS_BORDE),
            3.5 if act else 2)

    # ---- predictor, condición y ruido predicho
    en_rev = rev_desde is not None
    vivo = rev_activo is not None
    c_borde = ROJO if vivo else (TINTA if en_rev else GRIS_BORDE)
    c_txt = TINTA if en_rev else GRIS_MEDIO
    caja(ax, COND["x"], COND["y"], COND["w"], COND["h"],
         ec=TINTA if en_rev else GRIS_BORDE, lw=2)
    ax.text(COND["x"] + COND["w"] / 2, COND["y"] + 28, "condición c",
            ha="center", va="center", fontsize=21, fontweight="bold",
            color=c_txt)
    ax.text(COND["x"] + COND["w"] / 2, COND["y"] + 63, "«un círculo rojo»",
            ha="center", va="center", fontsize=20,
            color=ROJO if vivo else c_txt)
    caja(ax, PRED["x"], PRED["y"], PRED["w"], PRED["h"], ec=c_borde,
         lw=4 if vivo else 2, fc="white")
    ax.text(PRED["x"] + PRED["w"] / 2, PRED["y"] + 38, "predictor de ruido",
            ha="center", va="center", fontsize=22, fontweight="bold",
            color=ROJO if (vivo or final) else c_txt)
    ax.text(PRED["x"] + PRED["w"] / 2, PRED["y"] + 78, "condicionado en c",
            ha="center", va="center", fontsize=20, color=c_txt)
    yc = PRED["y"] + PRED["h"] / 2
    flecha(ax, COND["x"] + COND["w"] + 6, yc, PRED["x"] - 6, yc,
           color=TINTA if en_rev else GRIS_BORDE, lw=2.2)
    flecha(ax, PRED["x"] + PRED["w"] + 6, yc, EPS["x"] - 8, yc,
           color=ROJO if vivo else (TINTA if en_rev else GRIS_BORDE), lw=2.2)
    s = EPS["s"]
    t_eps = max(t_rev, 1) if vivo else (HITOS[1] if final else None)
    if t_eps is not None and t_eps > 0:
        ax.imshow(_ruido_rgb(eps[t_eps]), extent=(EPS["x"], EPS["x"] + s,
                                                   EPS["y"] + s, EPS["y"]),
                  interpolation="nearest", zorder=2)
        ax.add_patch(Rectangle((EPS["x"], EPS["y"]), s, s, fill=False,
                               ec=ROJO if vivo else TINTA, lw=3 if vivo else 1.8,
                               zorder=3))
    else:
        ax.add_patch(Rectangle((EPS["x"], EPS["y"]), s, s, fc=RELLENO,
                               ec=GRIS_BORDE, lw=1.6, zorder=2))
    ax.text(EPS["x"] + s / 2, EPS["y"] + s + 10, "predicción del ruido",
            ha="center", va="top", fontsize=19,
            color=ROJO if vivo else c_txt)

    # conexión del predictor con el paso activo de la fila reverse
    if vivo or final:
        i = rev_activo if vivo else 0
        xm = (XS[i] + TH + XS[i + 1]) / 2
        yb = Y_REV + TH + 88
        xp = PRED["x"] + PRED["w"] / 2
        col = ROJO
        ax.plot([xp, xp], [PRED["y"], yb], color=col, lw=3, zorder=4)
        ax.plot([xp, xm], [yb, yb], color=col, lw=3, zorder=4)
        flecha(ax, xm, yb, xm, Y_REV + TH / 2 + 14, color=col, lw=3, ms=24)
    if texto_pie:
        pie(ax, texto_pie)


def _f(v):
    return f"{v:.2f}".replace(".", ",")


def difusion_en_vivo(por_tramo=9, quietos=3, fps=10, pausa_s=3.0, png=True):
    xs, eps, ab = _difusion_datos()
    fig, ax = figura()
    frames = []
    _difusion_dibujar(ax, xs, eps, ab, fwd_hasta=1,
                      texto_pie="x0: una imagen sintética de 64×64×3, sin "
                                "ruido")
    frames += [capturar(fig)] * 8
    # forward: cada tramo recorre los pasos intermedios de verdad
    for i in range(1, len(HITOS)):
        ts = np.linspace(HITOS[i - 1], HITOS[i], por_tramo + 1)[1:].round()
        for t in ts.astype(int):
            _difusion_dibujar(
                ax, xs, eps, ab, fwd_hasta=i, fwd_activo=i, t_fwd=t,
                texto_pie=f"forward, paso t = {t}: x(t) = √(1−β)·x(t−1) + √β·ε,"
                          f" con ε gaussiano nuevo · queda señal "
                          f"{_f(np.sqrt(ab[t]))}")
            frames.append(capturar(fig))
        frames += [frames[-1]] * quietos
    _difusion_dibujar(ax, xs, eps, ab, fwd_hasta=len(HITOS), rev_desde=5,
                      texto_pie="xT: ruido puro, la misma forma 64×64×3. "
                                "La inferencia arranca de acá")
    frames += [capturar(fig)] * 8
    # reverse: el predictor estima el ruido y se resta, de xT a x0
    for i in range(len(HITOS) - 2, -1, -1):
        ts = np.linspace(HITOS[i + 1], HITOS[i], por_tramo + 1)[1:].round()
        for t in ts.astype(int):
            tt = max(t, 1)
            _difusion_dibujar(
                ax, xs, eps, ab, fwd_hasta=len(HITOS), rev_desde=i + 1,
                rev_activo=i, t_rev=t if t > 0 else 0,
                texto_pie=f"reverse, paso t = {tt}: el predictor recibe x(t), t "
                          f"y c, estima el ruido y se resta una parte → "
                          f"x({tt - 1})")
            frames.append(capturar(fig))
        frames += [frames[-1]] * quietos
    _difusion_dibujar(ax, xs, eps, ab, fwd_hasta=len(HITOS), rev_desde=0,
                      final=True,
                      texto_pie="forward agrega ruido paso a paso; reverse "
                                "lo quita con la predicción, guiada por c")
    frames.append(capturar(fig))
    if png:
        fig.savefig(os.path.join(OUT, "difusion-en-vivo.png"), dpi=DPI,
                    facecolor="white")
    plt.close(fig)
    guardar_gif(frames, os.path.join(OUT, "difusion-en-vivo.gif"), fps=fps,
                pausa_s=pausa_s, colores=96)
    return frames


# =========================================================================
# 2. unet-sd-en-vivo.gif
# =========================================================================
# niveles de la U: resolución -> (y del centro, lado del bloque en px)
U_NIVEL = {64: (145, 110), 32: (290, 88), 16: (415, 68), 8: (530, 54)}
U_BUS_Y = 612                  # bus de cross-attention, debajo de la U
# bloques en orden de cómputo: (rol, resolución, canales, x del centro)
U_BLOQUES = [("encoder", 64, 320, 350), ("encoder", 32, 640, 515),
             ("encoder", 16, 1280, 670), ("fondo", 8, 1280, 800),
             ("decoder", 16, 1280, 930), ("decoder", 32, 640, 1085),
             ("decoder", 64, 320, 1250)]
U_T = 500                                   # timestep del ejemplo
TOKENS = ["<inicio>", "un", "círculo", "rojo", "<fin>", "relleno ×72"]
CHIP_W, CHIP_H, CHIP_GAP, CHIP_Y = 168, 76, 16, 648
STACK_S, STACK_OFF = 100, 8
COL_IZQ, COL_DER = 140, PX_W - 140


def _chip_x(i):
    total = len(TOKENS) * CHIP_W + (len(TOKENS) - 1) * CHIP_GAP
    return PX_W / 2 - total / 2 + i * (CHIP_W + CHIP_GAP)


def _norm(a):
    a = a - a.min()
    return 0.08 + 0.84 * a / max(a.max(), 1e-9)


def _pool(a, r):
    k = a.shape[0] // r
    return a.reshape(r, k, r, k).mean((1, 3))


def _unet_datos():
    rng = np.random.default_rng(23)
    n = 64
    yy, xx = np.mgrid[0:n, 0:n] + 0.5
    r = np.hypot(xx - 32, yy - 32)
    disco = np.clip(17.5 - r, 0, 1)
    # latente "limpio" sintético de 4 canales (patrones suaves distintos)
    z0 = np.stack([disco, 1 - disco * 0.6 + 0.2 * np.sin(xx / 9),
                   disco * np.cos(yy / 11), 0.5 * np.sin((xx + yy) / 13)])
    z0 = (z0 - z0.mean((1, 2), keepdims=True)) / z0.std((1, 2), keepdims=True)
    eps = rng.standard_normal((4, n, n))
    ab = np.cumprod(1 - BETAS)[U_T - 1]
    zt = np.sqrt(ab) * z0 + np.sqrt(1 - ab) * eps     # latente ruidoso en t
    # mapas de features (un canal representativo por bloque), sintéticos
    mapas = []
    for j, (rol, res, _c, _x) in enumerate(U_BLOQUES):
        w = rng.standard_normal(4)
        base = np.tensordot(w, zt, 1)
        if rol == "decoder" or rol == "fondo":
            alfa = {8: 0.2, 16: 0.4, 32: 0.65, 64: 0.85}[res]
            base = (1 - alfa) * np.tanh(base) + alfa * np.tensordot(
                rng.standard_normal(4), eps, 1)
        mapas.append(_norm(np.tanh(_pool(base, res))))
    # embedding del prompt: 77 x 768 (sintético) y una tira para dibujar
    emb = rng.standard_normal((77, 768))
    tiras = [_norm(emb[i if i < 5 else 5].reshape(24, 32).mean(1))
             for i in range(len(TOKENS))]
    # pesos de atención: softmax sobre los 77 tokens de valores sintéticos,
    # distintos por bloque; el relleno (72 tokens) se agrupa en un chip
    base_s = np.array([2.4, 0.9, 2.1, 1.9, 1.1] + [-2.4] * 72)
    pesos = []
    for _ in U_BLOQUES:
        s = base_s.copy()
        s[:5] += 0.75 * rng.standard_normal(5)
        s[5:] += 0.3 * rng.standard_normal(72)
        p = np.exp(s - s.max())
        p /= p.sum()
        pesos.append(np.concatenate([p[:5], [p[5:].sum()]]))
    return zt, eps, mapas, tiras, pesos


PIES_CONV = [
    "conv de entrada: 64×64×4 → 64×64×320 (el timestep t se suma a las "
    "features de cada bloque)",
    "downsample + conv: 64×64×320 → 32×32×640 (la resolución baja a la mitad)",
    "downsample + conv: 32×32×640 → 16×16×1280",
    "downsample + conv: 16×16×1280 → 8×8×1280, el fondo de la U",
    "upsample + skip (se concatenan las features del encoder) + conv: "
    "8×8 → 16×16×1280",
    "upsample + skip + conv: 16×16×1280 → 32×32×640",
    "upsample + skip + conv: 32×32×640 → 64×64×320",
]


def _dims(j):
    _rol, res, c, _x = U_BLOQUES[j]
    return f"{res}×{res}×{c}"


def _unet_dibujar(ax, datos, hechos, activo=None, fase=None, f=0.0,
                  salida=0.0, final=False, texto_pie=None):
    """hechos: bloques ya calculados. activo: índice del bloque en curso.
    fase: 'conv' (f = fracción revelada) o 'attn' (f en [0, 1]).
    salida: fracción revelada del ruido predicho (0 = vacío).

    Ruteo sin cruces: las etiquetas de dimensiones van del lado de afuera de
    la U (las de 64×64 arriba, la del fondo encima del bloque), así el borde
    inferior de cada bloque queda libre. Las líneas de cross-attention suben
    en vertical desde cada token a un bus horizontal debajo de la U, viajan
    por el bus hasta la columna del bloque activo y suben por un tronco."""
    zt, eps, mapas, tiras, pesos = datos
    lienzo(ax)
    gris = GRIS_MEDIO
    for x, txt in ((COL_IZQ, "entradas"), (COL_DER, "salida")):
        ax.text(x, 46, txt, ha="center", va="center", fontsize=21, color=gris)
    ax.text(600, 205, "encoder", ha="center", va="center", fontsize=21,
            color=gris)
    ax.text(PX_W - 600, 205, "decoder", ha="center", va="center",
            fontsize=21, color=gris)

    def pila(xc, yc, canales, cmap, frac=1.0, borde=TINTA, lw=1.8):
        n = len(canales)
        x0 = xc - (STACK_S + STACK_OFF * (n - 1)) / 2
        y0 = yc - STACK_S / 2 + STACK_OFF * (n - 1) / 2
        for k in range(n - 1, -1, -1):
            xk, yk = x0 + k * STACK_OFF, y0 - k * STACK_OFF
            img = canales[k].copy()
            if frac < 1:
                filas = int(round(img.shape[0] * frac))
                img[filas:] = np.nan
            ax.add_patch(Rectangle((xk, yk), STACK_S, STACK_S, fc=RELLENO,
                                   ec="none", zorder=2 + (n - k) * 0.01))
            if frac > 0:
                ax.imshow(img, extent=(xk, xk + STACK_S, yk + STACK_S, yk),
                          cmap=cmap, vmin=-3, vmax=3, interpolation="nearest",
                          zorder=2 + (n - k) * 0.01)
            ax.add_patch(Rectangle((xk, yk), STACK_S, STACK_S, fill=False,
                                   ec=borde if frac > 0 else GRIS_BORDE,
                                   lw=lw, zorder=2.05 + (n - k) * 0.01))
        return x0, y0

    # ---- entradas
    yc_in = U_NIVEL[64][0]
    y_lab = yc_in + STACK_S / 2 + STACK_OFF * 1.5 + 10
    x0, _ = pila(COL_IZQ, yc_in, list(zt), "Greys")
    ax.text(COL_IZQ, y_lab, "latente ruidoso", ha="center",
            va="top", fontsize=21, fontweight="bold", color=TINTA)
    ax.text(COL_IZQ, y_lab + 34, "64×64×4", ha="center",
            va="top", fontsize=20, color=TINTA)
    caja(ax, COL_IZQ - 88, 332, 176, 76)
    ax.text(COL_IZQ, 354, "timestep", ha="center", va="center", fontsize=20,
            fontweight="bold", color=TINTA)
    ax.text(COL_IZQ, 387, f"t = {U_T}", ha="center", va="center", fontsize=20,
            color=TINTA)
    # ---- salida
    c_sal = ROJO if 0 < salida < 1 else TINTA
    pila(COL_DER, yc_in, list(eps), "Greys", frac=salida,
         borde=c_sal, lw=3.5 if 0 < salida < 1 else 1.8)
    ax.text(COL_DER, y_lab, "ruido predicho", ha="center",
            va="top", fontsize=21, fontweight="bold",
            color=ROJO if salida > 0 else gris)
    ax.text(COL_DER, y_lab + 34, "64×64×4", ha="center",
            va="top", fontsize=20, color=TINTA if salida > 0 else gris)
    ax.text(COL_DER, 370, "misma forma\nque el latente", ha="center",
            va="center", fontsize=19, color=gris, linespacing=1.25)

    # ---- geometría de bloques
    def geo(j):
        _rol, res, _c, xc = U_BLOQUES[j]
        yc, s = U_NIVEL[res]
        return xc, yc, s

    # skip connections (encoder j -> decoder 6-j)
    for j in range(3):
        xa, ya, sa = geo(j)
        xb, _yb, sb = geo(6 - j)
        act = activo == 6 - j and fase == "conv"
        col = ROJO if act else gris
        ax.plot([xa + sa / 2 + 12, xb - sb / 2 - 14], [ya, ya],
                ls=(0, (6, 5)), color=col, lw=3 if act else 1.8, zorder=1.5)
        ax.annotate("", xy=(xb - sb / 2 - 4, ya), xytext=(xb - sb / 2 - 16, ya),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=1.8,
                                    mutation_scale=18), zorder=1.5)
        ax.text(800, ya - 8, "skip", ha="center", va="bottom", fontsize=18,
                color=col)

    # flechas del camino principal (nunca por el borde inferior)
    def camino(j, color, lw):
        xe, ye, se = geo(0)
        if j == 0:
            flecha(ax, x0 + STACK_S + STACK_OFF * 3 + 8, ye,
                   xe - se / 2 - 6, ye, color=color, lw=lw)
            flecha(ax, COL_IZQ + 88 + 6, 360, xe - se / 2 - 6, ye + 32,
                   color=color, lw=lw)
            return
        xa, ya, sa = geo(j - 1)
        xb, yb, sb = geo(j)
        if j <= 2:     # bajando: borde derecho -> techo del siguiente
            p = (xa + sa / 2 + 4, ya + sa / 2 - 14)
            q = (xb - sb / 4, yb - sb / 2 - 5)
        elif j == 3:   # al fondo: borde derecho -> techo del fondo
            p = (xa + sa / 2 + 4, ya + sa / 2 - 12)
            q = (xb - sb / 4, yb - sb / 2 - 5)
        elif j == 4:   # desde el fondo: techo -> borde izquierdo
            p = (xa + sa / 4, ya - sa / 2 - 5)
            q = (xb - sb / 2 - 5, yb + sb / 2 - 12)
        else:          # subiendo: techo -> borde izquierdo del siguiente
            p = (xa + sa / 4, ya - sa / 2 - 5)
            q = (xb - sb / 2 - 4, yb + sb / 2 - 14)
        flecha(ax, *p, *q, color=color, lw=lw)

    for j in range(len(U_BLOQUES)):
        listo = j < hechos
        act = j == activo
        camino(j, ROJO if (act and fase == "conv") else
               (TINTA if (listo or act) else GRIS_BORDE),
               3.4 if (act and fase == "conv") else 2)
    xs_, ys_, ss_ = geo(6)
    flecha(ax, xs_ + ss_ / 2 + 6, ys_,
           COL_DER - (STACK_S + STACK_OFF * 3) / 2 - 8, ys_,
           color=ROJO if 0 < salida < 1 else (TINTA if salida else GRIS_BORDE),
           lw=3.4 if 0 < salida < 1 else 2)

    # bloques y etiquetas (del lado de afuera de la U)
    for j, (rol, res, c, xc) in enumerate(U_BLOQUES):
        _x, yc, s = geo(j)
        listo = j < hechos
        act = j == activo
        x, y = xc - s / 2, yc - s / 2
        for k in (2, 1):
            ax.add_patch(Rectangle((x + 5 * k, y - 5 * k), s, s, fc="white",
                                   ec=GRIS_BORDE if not (listo or act)
                                   else "#BDB5B2", lw=1.2, zorder=3))
        ax.add_patch(Rectangle((x, y), s, s, fc=RELLENO, ec="none", zorder=3.1))
        if listo or act:
            img = mapas[j].copy()
            if act and fase == "conv":
                filas = int(round(res * f))
                img = img.astype(float)
                img[filas:] = np.nan
            ax.imshow(img, extent=(x, x + s, y + s, y), cmap="Greys",
                      vmin=0, vmax=1, interpolation="nearest", zorder=3.2)
        ax.add_patch(Rectangle((x, y), s, s, fill=False,
                               ec=ROJO if act else (TINTA if listo
                                                    else GRIS_BORDE),
                               lw=3.5 if act else 1.8, zorder=3.3))
        estilo = dict(fontsize=18, fontweight="bold" if act else "normal",
                      linespacing=1.05, zorder=5,
                      color=ROJO if act else (TINTA if listo else gris))
        if res == 64:          # arriba del bloque
            ax.text(xc, y - 16, f"{res}×{res}×{c}", ha="center",
                    va="bottom", **estilo)
        elif rol == "fondo":   # a la izquierda del bloque
            ax.text(x - 10, yc, f"{res}×{res}\n×{c}\nfondo", ha="right",
                    va="center", **estilo)
        elif rol == "encoder":  # a la izquierda
            ax.text(x - 10, yc, f"{res}×{res}\n×{c}", ha="right",
                    va="center", **estilo)
        else:                  # decoder: a la derecha (pasada la pila)
            ax.text(x + s + 20, yc, f"{res}×{res}\n×{c}", ha="left",
                    va="center", **estilo)

    # ---- tokens del prompt
    p_act = pesos[activo] if (activo is not None and fase == "attn") else None
    cxs = [_chip_x(i) + CHIP_W / 2 for i in range(len(TOKENS))]
    for i, tok in enumerate(TOKENS):
        cx = _chip_x(i)
        resalta = p_act is not None
        caja(ax, cx, CHIP_Y, CHIP_W, CHIP_H, ec=ROJO if resalta else TINTA,
             lw=2.4 if resalta else 1.8, r=10)
        ax.text(cx + CHIP_W / 2, CHIP_Y + 24, tok, ha="center", va="center",
                fontsize=18, color=TINTA,
                fontweight="bold" if i in (2, 3) else "normal")
        ax.imshow(tiras[i][None, :], extent=(cx + 15, cx + CHIP_W - 15,
                                              CHIP_Y + 62, CHIP_Y + 46),
                  cmap="Greys", vmin=0, vmax=1, interpolation="nearest",
                  zorder=4, aspect="auto")
        if p_act is not None:
            ax.text(cx + CHIP_W / 2, CHIP_Y + CHIP_H + 8,
                    f"{p_act[i]:.2f}".replace(".", ","), ha="center",
                    va="top", fontsize=20, fontweight="bold", color=ROJO)
    ax.text(PX_W / 2, CHIP_Y + CHIP_H + 48,
            "embedding del prompt: 77 tokens × 768 (CLIP)", ha="center",
            va="top", fontsize=20, color=TINTA)

    # ---- cross-attention: token -> bus -> tronco -> bloque activo
    y_bus = U_BUS_Y
    if p_act is not None:
        xb, yb, sb = geo(activo)
        y_top = yb + sb / 2 + 3
        grosor = lambda w: 1.0 + 13.0 * w  # noqa: E731  proporcional al peso
        kw = dict(color=ROJO, alpha=0.85, solid_capstyle="butt", zorder=2.5)
        for i, w in enumerate(p_act):       # verticales de cada token
            ax.plot([cxs[i], cxs[i]], [CHIP_Y - 2, y_bus], lw=grosor(w), **kw)
        # bus: el grosor de cada tramo es la suma de los pesos que lo cruzan
        puntos = sorted(set(cxs + [xb]))
        for a, b in zip(puntos[:-1], puntos[1:]):
            m = (a + b) / 2
            flujo = sum(w for cx, w in zip(cxs, p_act)
                        if (cx < m < xb) or (xb < m < cx))
            if flujo > 0:
                ax.plot([a, b], [y_bus, y_bus], lw=grosor(flujo), **kw)
        # tronco: la suma ponderada (los pesos suman 1) sube al bloque
        ax.plot([xb, xb], [y_bus, y_top + 14], lw=grosor(1.0), **kw)
        flecha(ax, xb, y_top + 16, xb, y_top, color=ROJO, lw=3, z=2.6, ms=30)
        ax.add_patch(plt.Circle((xb, y_bus), 17, fc="white", ec=ROJO, lw=2.5,
                                zorder=6))
        ax.text(xb, y_bus + 1, "Σ", ha="center", va="center", fontsize=19,
                fontweight="bold", color=ROJO, zorder=7)
        # puntos que recorren el camino (tamaño proporcional al peso)
        u = f / 0.6
        if 0 <= u <= 1:
            for i, w in enumerate(p_act):
                ruta = [(cxs[i], CHIP_Y - 2), (cxs[i], y_bus), (xb, y_bus)]
                ax.plot(*_sobre_ruta(ruta, u), "o", ms=6 + 26 * w,
                        color=ROJO, mec="white", mew=1.5, zorder=6.5)
        elif f > 0.6:
            v = (f - 0.6) / 0.4
            ax.plot(xb, y_bus - 17 - (y_bus - 17 - y_top) * v, "o", ms=26,
                    color=ROJO, mec="white", mew=1.5, zorder=6.5)
    if final:   # como en la lámina: un bus que sube a cada nivel
        xs_b = [geo(j)[0] for j in range(len(U_BLOQUES))]
        ax.plot([min(xs_b + cxs), max(xs_b + cxs)], [y_bus, y_bus],
                color=ROJO, lw=3,
                zorder=2.5, solid_capstyle="butt")
        for cx in cxs:
            ax.plot([cx, cx], [CHIP_Y - 2, y_bus], color=ROJO, lw=2,
                    zorder=2.5)
        for j in range(len(U_BLOQUES)):
            xb, yb, sb = geo(j)
            flecha(ax, xb, y_bus, xb, yb + sb / 2 + 3, color=ROJO,
                   lw=3, z=2.5, ms=22)
    if texto_pie:
        pie(ax, texto_pie, fs=21)


def _sobre_ruta(ruta, u):
    """Punto a una fracción u (0..1) del largo de una polilínea."""
    pts = np.array(ruta, float)
    seg = np.hypot(*np.diff(pts, axis=0).T)
    total = seg.sum()
    if total == 0:
        return pts[0]
    d = u * total
    for k, L in enumerate(seg):
        if d <= L or k == len(seg) - 1:
            t = 0 if L == 0 else min(d / L, 1)
            return pts[k] + (pts[k + 1] - pts[k]) * t
        d -= L


PIE_ATTN = ("cross-attention: calcula pesos entre las features y cada "
            "token y suma la información ponderada")


def unet_sd_en_vivo(conv_n=6, attn_n=11, quietos=2, fps=10, pausa_s=3.0,
                    png=True):
    datos = _unet_datos()
    for p in datos[4]:
        assert abs(p.sum() - 1) < 1e-9
    fig, ax = figura()
    frames = []
    _unet_dibujar(ax, datos, hechos=0,
                  texto_pie=f"entradas: latente ruidoso 64×64×4, timestep "
                            f"t = {U_T} y embedding del prompt 77×768")
    frames += [capturar(fig)] * 14
    for j in range(len(U_BLOQUES)):
        for k in range(1, conv_n + 1):
            _unet_dibujar(ax, datos, hechos=j, activo=j, fase="conv",
                          f=k / conv_n, texto_pie=PIES_CONV[j])
            frames.append(capturar(fig))
        for k in range(attn_n):
            _unet_dibujar(ax, datos, hechos=j, activo=j, fase="attn",
                          f=k / (attn_n - 1),
                          texto_pie=PIE_ATTN)
            frames.append(capturar(fig))
        frames += [frames[-1]] * quietos
    for k in range(1, 9):
        _unet_dibujar(ax, datos, hechos=7, salida=k / 8,
                      texto_pie="conv de salida: 64×64×320 → 64×64×4, el ruido "
                                "predicho tiene la forma del latente")
        frames.append(capturar(fig))
    frames += [frames[-1]] * 4
    _unet_dibujar(ax, datos, hechos=7, salida=1.0, final=True,
                  texto_pie="el prompt entra por cross-attention en cada "
                            "nivel de la U, bajando y subiendo")
    frames.append(capturar(fig))
    if png:
        fig.savefig(os.path.join(OUT, "unet-sd-en-vivo.png"), dpi=DPI,
                    facecolor="white")
    plt.close(fig)
    guardar_gif(frames, os.path.join(OUT, "unet-sd-en-vivo.gif"), fps=fps,
                pausa_s=pausa_s, colores=64)
    return frames


TAREAS = {"difusion-en-vivo": difusion_en_vivo,
          "unet-sd-en-vivo": unet_sd_en_vivo}

if __name__ == "__main__":
    for nombre in (sys.argv[1:] or TAREAS):
        TAREAS[nombre]()
