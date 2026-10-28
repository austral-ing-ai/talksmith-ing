#!/usr/bin/env python3
"""Animaciones de CLIP y del VAE de Stable Diffusion para la Talk
"segmentacion-y-stable-diffusion".

  clip-en-vivo.gif / .png   batch de 4 pares -> encoders -> matriz 4x4 de
                            similitudes -> épocas de entrenamiento contrastivo
  vae-en-vivo.gif / .png    imagen 512x512x3 -> encoder -> latente 64x64x4 ->
                            decoder -> imagen reconstruida 512x512x3

Todo es sintético (numpy). Reusa paleta y helpers de gen_animaciones_conv.py
(sin modificarlo). Uso:  python3 gen_anim_clip-vae.py [clip|vae ...]
"""
import os
import sys

import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from gen_animaciones_conv import (  # noqa: E402
    capturar, guardar_gif, TINTA, ROJO, RELLENO, GRIS_MEDIO, OUT, W, H, DPI)

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import to_rgb  # noqa: E402
from matplotlib.patches import (  # noqa: E402
    Circle, FancyBboxPatch, Rectangle, Polygon)
from matplotlib.path import Path  # noqa: E402
from PIL import Image, ImageFilter  # noqa: E402

BORDE = "#D9D3D1"
ROSA = "#FBE3E5"


# --- helpers de dibujo (coordenadas en px, y hacia abajo) ------------------
def lienzo():
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    return fig, ax


def preparar(ax):
    ax.clear()
    ax.set_xlim(0, 1600)
    ax.set_ylim(900, 0)
    ax.axis("off")


def mezcla(c1, c2, t):
    a, b = np.array(to_rgb(c1)), np.array(to_rgb(c2))
    t = float(np.clip(t, 0, 1))
    return tuple(a + (b - a) * t)


def caja(ax, x, y, w, h, fc="white", ec=TINTA, lw=2.0, r=10, z=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw, zorder=z))


def rect(ax, x, y, w, h, fc="white", ec=TINTA, lw=1.5, z=3, ls="-"):
    ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=lw, zorder=z,
                           ls=ls))


def txt(ax, x, y, s, size=20, color=TINTA, bold=False, ha="center",
        va="center", z=6, **kw):
    ax.text(x, y, s, fontsize=size, color=color,
            fontweight="bold" if bold else "normal", ha=ha, va=va, zorder=z,
            **kw)


def flecha(ax, x0, y0, x1, y1, color=GRIS_MEDIO, lw=2.2, z=1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), zorder=z,
                arrowprops=dict(arrowstyle="-|>,head_length=0.7,head_width=0.4",
                                color=color, lw=lw, shrinkA=0, shrinkB=0))


def pie(ax, s):
    txt(ax, 800, 862, s, size=22)


def imagen(ax, arr, x, y, w, h, alpha=1.0, z=4, interp="nearest"):
    ax.imshow(arr, extent=(x, x + w, y + h, y), zorder=z, alpha=alpha,
              interpolation=interp, aspect="auto",
              cmap="gray" if arr.ndim == 2 else None, vmin=0, vmax=1)


def suave(t):
    t = float(np.clip(t, 0, 1))
    return t * t * (3 - 2 * t)


# =========================================================================
# 1. CLIP en vivo
# =========================================================================
TEXTOS = ["perro en la playa", "gato en un sofá", "sol sobre montañas",
          "auto en la ruta"]
N, D = 4, 8
C, G = 116, 8                       # celda de la matriz y separación
MX, MY = 1050, 300                  # esquina de la matriz
ROWS = [MY + i * (C + G) for i in range(N)]
COLS = [MX + j * (C + G) for j in range(N)]
TXT_Y = [126, 168, 210, 252]        # textos del batch (arriba del panel)
FOTO_X = 248                        # miniaturas (abajo del panel)


def _clip_imagenes(n=120):
    yy, xx = np.mgrid[0:n, 0:n] / n
    ims = []
    # perro en la playa: cielo, mar, arena, perro
    a = np.where(yy < 0.45, 0.88 - 0.1 * yy, 0.62)
    a[(yy >= 0.45) & (yy < 0.58)] = 0.45
    a[yy >= 0.58] = 0.80 - 0.1 * (yy[yy >= 0.58] - 0.58)
    cuerpo = ((xx - 0.48) / 0.20) ** 2 + ((yy - 0.70) / 0.09) ** 2 < 1
    cab = (xx - 0.72) ** 2 + (yy - 0.58) ** 2 < 0.075 ** 2
    patas = ((np.abs(xx - 0.36) < 0.025) | (np.abs(xx - 0.60) < 0.025)) & \
        (yy > 0.70) & (yy < 0.86)
    oreja = (np.abs(xx - 0.76) < 0.03) & (yy > 0.50) & (yy < 0.62)
    cola = (np.abs(yy - (0.62 + 0.8 * (xx - 0.28))) < 0.025) & \
        (xx > 0.20) & (xx < 0.30)
    a[cuerpo | cab | patas | oreja | cola] = 0.22
    ims.append(a)
    # gato en un sofá
    b = np.full((n, n), 0.90)
    sofa = (yy > 0.52) & (yy < 0.86) & (xx > 0.08) & (xx < 0.92)
    resp = (yy > 0.36) & (yy < 0.56) & (xx > 0.14) & (xx < 0.86)
    b[resp] = 0.58
    b[sofa] = 0.66
    b[(yy > 0.86) & (yy < 0.94) & ((np.abs(xx - 0.16) < 0.03) |
                                   (np.abs(xx - 0.84) < 0.03))] = 0.4
    cab = (xx - 0.42) ** 2 + (yy - 0.40) ** 2 < 0.085 ** 2
    o1 = (yy < 0.36) & (yy > 0.24) & (np.abs(xx - 0.36) < 0.04 * (yy - 0.24) / 0.12)
    o2 = (yy < 0.36) & (yy > 0.24) & (np.abs(xx - 0.48) < 0.04 * (yy - 0.24) / 0.12)
    cu = ((xx - 0.55) / 0.17) ** 2 + ((yy - 0.52) / 0.09) ** 2 < 1
    b[cab | o1 | o2 | cu] = 0.18
    ims.append(b)
    # sol sobre montañas
    c = 0.92 - 0.25 * yy
    sol = (xx - 0.50) ** 2 + (yy - 0.30) ** 2 < 0.13 ** 2
    c[sol] = 0.98
    c[((xx - 0.50) ** 2 + (yy - 0.30) ** 2 >= 0.13 ** 2) &
      ((xx - 0.50) ** 2 + (yy - 0.30) ** 2 < 0.15 ** 2)] = 0.55
    m1 = yy > 0.95 - 1.3 * (0.42 - np.abs(xx - 0.30))
    m2 = yy > 0.95 - 1.1 * (0.45 - np.abs(xx - 0.74))
    c[m2] = 0.50
    c[m1] = 0.30
    ims.append(c)
    # auto en la ruta
    d = np.where(yy < 0.55, 0.90, 0.40)
    d[(yy > 0.74) & (yy < 0.77) & ((xx * 10) % 2 < 1)] = 0.95
    car = (yy > 0.48) & (yy < 0.66) & (xx > 0.18) & (xx < 0.82)
    techo = (yy > 0.34) & (yy <= 0.48) & (xx > 0.32) & (xx < 0.66)
    vent = (yy > 0.37) & (yy < 0.47) & (xx > 0.36) & (xx < 0.62) & \
        (np.abs(xx - 0.49) > 0.015)
    d[car | techo] = 0.15
    d[vent] = 0.80
    for cx in (0.32, 0.68):
        d[(xx - cx) ** 2 + (yy - 0.66) ** 2 < 0.075 ** 2] = 0.05
        d[(xx - cx) ** 2 + (yy - 0.66) ** 2 < 0.03 ** 2] = 0.7
    ims.append(d)
    return ims


def _clip_datos():
    """Embeddings sintéticos por época y la matriz de similitudes (coseno)."""
    rng = np.random.default_rng(11)
    q, _ = np.linalg.qr(rng.standard_normal((D, D)))
    T0 = q[:, :N].T                                   # textos casi ortogonales
    I0 = rng.standard_normal((N, D))
    I0 /= np.linalg.norm(I0, axis=1, keepdims=True)

    def nrm(v):
        return v / np.linalg.norm(v, axis=1, keepdims=True)

    alfas = [0.0, 0.20, 0.36, 0.55, 0.75, 0.93]
    Ts, Is, Ss = [], [], []
    for a in alfas:
        T = nrm(T0 + 0.20 * a * I0)                   # ambos encoders aprenden
        I = nrm((1 - a) * I0 + a * T0 + 0.05 * a * (1 - a) *
                rng.standard_normal((N, D)))
        Ts.append(T)
        Is.append(I)
        Ss.append(I @ T.T)
    return Ts, Is, Ss


def _vec_color(v):
    """Componente del embedding -> color: negativo tinta, positivo rojo."""
    t = float(np.clip(v / 0.75, -1, 1))
    return mezcla("white", ROJO, t) if t >= 0 else mezcla("white", TINTA, -t)


def _celda_color(i, j, v):
    if i == j:
        return mezcla(ROSA, ROJO, np.clip(v, 0, 1))
    return mezcla(RELLENO, "#8A8583", np.clip(v, 0, 0.8) / 0.8)


def _vector(ax, x, y, vals, alpha=1.0):
    """Fila de D cuadraditos de 13 px."""
    for k, v in enumerate(vals):
        fc = mezcla("white", _vec_color(v), alpha)
        rect(ax, x + 13 * k, y, 13, 22, fc=fc, ec=BORDE, lw=0.8, z=5)


def _clip_dibujar(ax, ims, T, I, S, *, txt_on=-1, img_on=-1, t_vec=1.0,
                  n_T=0, n_I=0, n_celdas=0, celda_act=None, epoca=None,
                  entrenando=False, pulso=None, pesos_on=False, footer=""):
    preparar(ax)
    # ---- panel del batch: textos arriba, fotos abajo ----
    act_t = txt_on >= 0
    act_i = img_on >= 0
    caja(ax, 40, 40, 426, 758, fc="white", ec=BORDE, lw=1.8, r=14, z=1)
    txt(ax, 60, 74, "batch de N = 4 pares", size=18, color=GRIS_MEDIO,
        ha="left")
    ax.plot([60, 446], [292, 292], color=BORDE, lw=1.5, ls=(0, (6, 5)),
            zorder=1)
    rend = ax.figure.canvas.get_renderer()
    for k in range(N):
        y = TXT_Y[k]
        roja = k == txt_on
        txt(ax, 64, y, f"{k + 1}", size=18, bold=True,
            color=ROJO if roja else GRIS_MEDIO, ha="left")
        t = ax.text(92, y, f"“{TEXTOS[k]}”", fontsize=19,
                    color=ROJO if roja else TINTA,
                    fontweight="bold" if roja else "normal", ha="left",
                    va="center", style="italic", zorder=6)
        x_fin = t.get_window_extent(rend).x1
        flecha(ax, x_fin + 8, y, 556, 221 + (k - 1.5) * 18,
               color=ROJO if roja else GRIS_MEDIO,
               lw=2.6 if roja else 1.8)
    for k in range(N):
        yc = ROWS[k] + C / 2
        roja = k == img_on
        txt(ax, FOTO_X - 16, yc, f"foto {k + 1}", size=18,
            bold=roja, color=ROJO if roja else GRIS_MEDIO, ha="right")
        imagen(ax, ims[k], FOTO_X, yc - 50, 100, 100, interp="bilinear")
        rect(ax, FOTO_X, yc - 50, 100, 100, fc="none",
             ec=ROJO if roja else TINTA, lw=3.5 if roja else 1.4, z=5)
        flecha(ax, FOTO_X + 104, yc, 556, 545 + (k - 1.5) * 30,
               color=ROJO if roja else GRIS_MEDIO,
               lw=2.6 if roja else 1.8)
    # ---- encoders ----
    act_t = act_t or pesos_on
    act_i = act_i or pesos_on
    caja(ax, 560, 185, 250, 72, fc=ROSA if act_t else RELLENO,
         ec=ROJO if act_t else TINTA, lw=3 if act_t else 2)
    txt(ax, 685, 221, "text encoder", size=22, bold=True,
        color=ROJO if act_t else TINTA)
    caja(ax, 560, 470, 250, 150, fc=ROSA if act_i else RELLENO,
         ec=ROJO if act_i else TINTA, lw=3 if act_i else 2)
    txt(ax, 685, 545, "image\nencoder", size=22, bold=True,
        color=ROJO if act_i else TINTA, linespacing=1.2)
    if pesos_on:
        for yy in (288, 652):
            txt(ax, 685, yy, "✓ pesos actualizados", size=18, bold=True,
                color=ROJO)
    if epoca is not None and epoca >= 1:
        txt(ax, 685, 378, "se entrenan los dos\nencoders a la vez",
            size=18, bold=entrenando, linespacing=1.3,
            color=ROJO if entrenando else TINTA)
    ct = ROJO if act_t else GRIS_MEDIO
    # ---- cabeceras T ----
    caja(ax, 1042, 162, 504, 112, fc="white", ec=BORDE, lw=1.8, r=12, z=1)
    flecha(ax, 812, 221, 1038, 221, color=ct, lw=2.4 if act_t else 2.2)
    txt(ax, 1294, 140, "T = embeddings de texto", size=18, color=GRIS_MEDIO)
    for j in range(N):
        x = COLS[j]
        lleno = j < n_T
        act = (celda_act is not None and celda_act[1] == j) or j == txt_on
        rect(ax, x, 172, C, 92, fc="white", ec=ROJO if act else TINTA,
             lw=3 if act else 1.6, z=4)
        txt(ax, x + C / 2, 197, f"T{j + 1}", size=20, bold=True,
            color=ROJO if act else TINTA)
        if lleno or j == txt_on:
            _vector(ax, x + 6, 226, T[j], alpha=t_vec if j == txt_on else 1)
    # ---- cabeceras I ----
    caja(ax, 898, 292, 140, 504, fc="white", ec=BORDE, lw=1.8, r=12, z=1)
    txt(ax, 968, 818, "I = embeddings de imagen", size=17, color=GRIS_MEDIO)
    for i in range(N):
        y = ROWS[i]
        lleno = i < n_I
        act = (celda_act is not None and celda_act[0] == i) or i == img_on
        rect(ax, 906, y, 124, C, fc="white", ec=ROJO if act else TINTA,
             lw=3 if act else 1.6, z=4)
        txt(ax, 968, y + 36, f"I{i + 1}", size=20, bold=True,
            color=ROJO if act else TINTA)
        if lleno or i == img_on:
            _vector(ax, 916, y + 66, I[i], alpha=t_vec if i == img_on else 1)
        c = ROJO if i == img_on else GRIS_MEDIO
        flecha(ax, 812, 545 + (i - 1.5) * 30, 902, y + C / 2, color=c,
               lw=2.6 if i == img_on else 1.8)
    # ---- matriz ----
    orden = [(i, j) for i in range(N) for j in range(N)]
    for idx, (i, j) in enumerate(orden):
        x, y = COLS[j], ROWS[i]
        if idx < n_celdas:
            v = S[i, j]
            fc = _celda_color(i, j, v)
            oscuro = (i == j and v > 0.45) or (i != j and v > 0.55)
            rect(ax, x, y, C, C, fc=fc, ec=ROJO if i == j else BORDE,
                 lw=3 if i == j else 1.2, z=3)
            v_txt = 0.0 if abs(v) < 0.005 else v
            txt(ax, x + C / 2, y + C / 2 + 4, f"{v_txt:+.2f}".replace(".", ","),
                size=21, bold=i == j, color="white" if oscuro else TINTA)
            txt(ax, x + 8, y + 16, f"I{i + 1}·T{j + 1}", size=12,
                color="white" if oscuro else GRIS_MEDIO, ha="left")
            if entrenando:
                if i == j:
                    txt(ax, x + C - 12, y + 18, "▲", size=15,
                        color="white" if oscuro else ROJO)
                else:
                    txt(ax, x + C - 12, y + 18, "▼", size=15, color=TINTA)
        else:
            rect(ax, x, y, C, C, fc="white", ec=BORDE, lw=1.2, z=3)
        if celda_act == (i, j):
            rect(ax, x - 3, y - 3, C + 6, C + 6, fc="none", ec=ROJO, lw=5,
                 z=7)
    # ---- pulso de backward: de la matriz a los dos encoders ----
    if pulso is not None:
        caminos = [[(1294, 300), (1294, 221), (816, 221)],
                   [(1046, 544), (902, 544), (816, 545)]]
        for cam in caminos:
            for k, atras in enumerate((0.0, 0.07, 0.14)):
                x, y = _sobre_camino(cam, max(pulso - atras, 0))
                ax.add_patch(Circle((x, y), 13 - 3.5 * k, fc=ROJO,
                                    ec="white", lw=1.5, alpha=1 - 0.3 * k,
                                    zorder=9))
    # ---- leyenda y época ----
    rect(ax, 540, 52, 26, 26, fc=ROJO, ec=ROJO, z=5)
    txt(ax, 578, 65, "diagonal = pares reales: acercar", size=19,
        bold=True, ha="left")
    rect(ax, 1150, 52, 26, 26, fc=RELLENO, ec=BORDE, z=5)
    txt(ax, 1188, 65, "resto = pares falsos: alejar", size=19, ha="left")
    ex = 572
    if epoca is None:
        txt(ax, ex, 702, "época 0", size=26, bold=True, ha="left")
        txt(ax, ex, 746, "(sin entrenar)", size=18, ha="left",
            color=GRIS_MEDIO)
    else:
        dg = np.mean(np.diag(S))
        rs = (S.sum() - np.trace(S)) / (N * N - N)
        dg, rs = (0.0 if abs(v) < 0.005 else v for v in (dg, rs))
        txt(ax, ex, 702, f"época {epoca}", size=26, bold=True,
            color=ROJO if entrenando else TINTA, ha="left")
        txt(ax, ex, 746, f"media diagonal {dg:+.2f}".replace(".", ","),
            size=18, ha="left", color=ROJO)
        txt(ax, ex, 778, f"media resto {rs:+.2f}".replace(".", ","),
            size=18, ha="left")
    pie(ax, footer)


def _sobre_camino(cam, t):
    """Punto a fracción t (0..1) del largo de una poligonal."""
    pts = np.array(cam, float)
    seg = np.hypot(*np.diff(pts, axis=0).T)
    d = float(np.clip(t, 0, 1)) * seg.sum()
    for (a, b), L in zip(zip(pts[:-1], pts[1:]), seg):
        if d <= L:
            return a + (b - a) * (d / L)
        d -= L
    return pts[-1]


def clip_en_vivo(fps=12, pausa_s=3.0):
    ims = _clip_imagenes()
    Ts, Is, Ss = _clip_datos()
    fig, ax = lienzo()
    fr = []

    def cap(**kw):
        _clip_dibujar(ax, ims, **kw)
        fr.append(capturar(fig))

    T0, I0, S0 = Ts[0], Is[0], Ss[0]
    base = dict(T=T0, I=I0, S=S0)
    for _ in range(14):
        cap(**base, footer="Un batch de N = 4 pares reales (imagen, descripción)")
    for k in range(N):
        for f in range(6):
            cap(**base, txt_on=k, t_vec=suave((f + 1) / 4), n_T=k,
                footer=f"text encoder: “{TEXTOS[k]}” → vector T{k + 1} "
                       "(acá 8 números; en CLIP, 512 o 768)")
    for k in range(N):
        for f in range(6):
            cap(**base, img_on=k, t_vec=suave((f + 1) / 4), n_T=N, n_I=k,
                footer=f"image encoder: foto {k + 1} → vector I{k + 1}, "
                       "en el mismo espacio que los T")
    orden = [(i, j) for i in range(N) for j in range(N)]
    for idx, (i, j) in enumerate(orden):
        for _ in range(2):
            cap(**base, n_T=N, n_I=N, n_celdas=idx + 1, celda_act=(i, j),
                epoca=0,
                footer=f"similitud(I{i + 1}, T{j + 1}) = producto punto de "
                       "los vectores normalizados → matriz 4×4")
    for _ in range(8):
        cap(**base, n_T=N, n_I=N, n_celdas=16, epoca=0,
            footer="Antes de entrenar: la diagonal no se distingue del resto")
    for e in range(1, len(Ss)):
        prev = dict(T=Ts[e - 1], I=Is[e - 1], S=Ss[e - 1], n_T=N, n_I=N,
                    n_celdas=16, epoca=e, entrenando=True)
        for f in range(7):
            cap(**prev, pulso=(f + 1) / 7,
                footer="backward: el gradiente de la pérdida contrastiva "
                       "vuelve a los dos encoders")
        for _ in range(3):
            cap(**prev, pesos_on=True,
                footer="Se actualizan los pesos del text encoder y del "
                       "image encoder")
        for f in range(9):
            t = suave((f + 1) / 9)
            T = (1 - t) * Ts[e - 1] + t * Ts[e]
            I = (1 - t) * Is[e - 1] + t * Is[e]
            S = (1 - t) * Ss[e - 1] + t * Ss[e]
            cap(T=T, I=I, S=S, n_T=N, n_I=N, n_celdas=16, epoca=e,
                entrenando=True, pesos_on=f < 3,
                footer="Con los pesos nuevos: sube la diagonal (pares "
                       "reales) y baja el resto (pares falsos)")
        for _ in range(2):
            fr.append(fr[-1])
    _clip_dibujar(ax, ims, T=Ts[-1], I=Is[-1], S=Ss[-1], n_T=N, n_I=N,
                  n_celdas=16, epoca=len(Ss) - 1,
                  footer="Entrenado: cada imagen queda cerca de su descripción "
                         "y lejos de las demás")
    fr.append(capturar(fig))
    plt.close(fig)
    fr[-1].save(os.path.join(OUT, "clip-en-vivo.png"))
    guardar_gif(fr, os.path.join(OUT, "clip-en-vivo.gif"), fps=fps,
                pausa_s=pausa_s, colores=128)
    return fr


# =========================================================================
# 2. VAE en vivo
# =========================================================================
def _vae_imagen(n=512):
    yy, xx = np.mgrid[0:n, 0:n] / n
    img = np.zeros((n, n, 3))
    cielo_a, cielo_b = np.array(to_rgb("#A9BDCB")), np.array(to_rgb("#EEF2F4"))
    img[:] = cielo_a + (cielo_b - cielo_a) * np.clip(yy / 0.55, 0, 1)[..., None]
    # sol con anillo
    r = np.hypot(xx - 0.78, yy - 0.18)
    img[r < 0.075] = to_rgb("#F3E3B5")
    img[(r >= 0.075) & (r < 0.085)] = to_rgb("#E9C987")

    def poli(pts):
        return Path(pts).contains_points(
            np.c_[xx.ravel(), yy.ravel()]).reshape(n, n)

    img[poli([(-0.05, 0.62), (0.22, 0.28), (0.45, 0.62)])] = to_rgb("#7D8C99")
    img[poli([(0.25, 0.62), (0.55, 0.22), (0.90, 0.62)])] = to_rgb("#5F6E7C")
    img[poli([(0.47, 0.30), (0.55, 0.22), (0.62, 0.30)])] = to_rgb("#F4F4F4")
    img[poli([(0.65, 0.62), (0.88, 0.36), (1.10, 0.62)])] = to_rgb("#8797A3")
    # pasto con textura fina
    pasto = yy >= 0.60
    tono = 0.5 + 0.5 * np.sin(2 * np.pi * xx * 90 + 9 * yy) * \
        np.sin(2 * np.pi * yy * 70)
    verde = np.array(to_rgb("#7E9A6A"))
    img[pasto] = (verde * (0.85 + 0.25 * tono[..., None]))[pasto]
    # camino
    cam = poli([(0.40, 1.01), (0.62, 1.01), (0.53, 0.66), (0.49, 0.66)])
    img[cam] = to_rgb("#CDBFA8")
    # casa
    pared = (xx > 0.10) & (xx < 0.38) & (yy > 0.56) & (yy < 0.80)
    img[pared] = to_rgb("#EFE6D6")
    img[poli([(0.07, 0.57), (0.24, 0.42), (0.41, 0.57)])] = to_rgb(ROJO)
    # tejas: líneas finas en el techo
    techo = poli([(0.07, 0.57), (0.24, 0.42), (0.41, 0.57)])
    img[techo & ((yy * 512) % 9 < 1.5)] = to_rgb("#9E1220")
    for x0 in (0.14, 0.28):
        v = (xx > x0) & (xx < x0 + 0.07) & (yy > 0.61) & (yy < 0.69)
        img[v] = to_rgb("#3B4A57")
        marco = v & ((np.abs(xx - (x0 + 0.035)) < 0.004) |
                     (np.abs(yy - 0.65) < 0.004))
        img[marco] = to_rgb("#F7F2EA")
    img[(xx > 0.215) & (xx < 0.265) & (yy > 0.68) & (yy < 0.80)] = \
        to_rgb("#6B4B3A")
    # cerca: postes finos
    cerca = (yy > 0.74) & (yy < 0.86) & (xx > 0.45) & \
        ((xx * 512) % 16 < 3.5)
    tabla = (xx > 0.45) & ((np.abs(yy - 0.77) < 0.005) |
                           (np.abs(yy - 0.83) < 0.005))
    img[cerca | tabla] = to_rgb("#F7F2EA")
    # árbol
    copa = np.hypot((xx - 0.92) / 0.06, (yy - 0.60) / 0.09) < 1
    hojas = 0.5 + 0.5 * np.sin(xx * 300) * np.sin(yy * 260)
    img[copa] = (np.array(to_rgb("#4C6B45")) * (0.8 + 0.35 *
                                                hojas[..., None]))[copa]
    img[(np.abs(xx - 0.92) < 0.01) & (yy > 0.68) & (yy < 0.76)] = \
        to_rgb("#5A4032")
    return np.clip(img, 0, 1)


def _pool(a, f):
    r = a.shape[0] // f
    if a.ndim == 3:
        return a.reshape(r, f, r, f, a.shape[2]).mean((1, 3))
    return a.reshape(r, f, r, f).mean((1, 3))


def _resize(a, n, metodo=Image.BICUBIC):
    if a.ndim == 2:
        return np.asarray(Image.fromarray(
            (np.clip(a, 0, 1) * 255).astype(np.uint8)).resize((n, n), metodo)
        ) / 255.0
    return np.asarray(Image.fromarray(
        (np.clip(a, 0, 1) * 255).astype(np.uint8)).resize((n, n), metodo)
    ) / 255.0


def _rob(a):
    lo, hi = np.percentile(a, [2, 98])
    return np.clip((a - lo) / (hi - lo + 1e-9), 0, 1)


def _zs(a):
    return np.clip(0.5 + (a - a.mean()) / (4 * a.std() + 1e-9), 0, 1)


def _norm(a):
    return (a - a.min()) / (a.max() - a.min() + 1e-9)


def _vae_datos():
    img = _vae_imagen()
    gris = img @ np.array([0.299, 0.587, 0.114])
    enc = [_pool(gris, 2), _pool(gris, 4), _pool(gris, 8)]    # 256,128,64
    p = _pool(img, 8)                                          # 64x64x3
    y = p @ np.array([0.299, 0.587, 0.114])
    blur = np.asarray(Image.fromarray((y * 255).astype(np.uint8)).filter(
        ImageFilter.GaussianBlur(2))) / 255.0
    lat = [_rob(y), _zs(p[..., 0] - p[..., 1]),
           _zs(p[..., 2] - 0.5 * (p[..., 0] + p[..., 1])),
           1 - 0.85 * _rob(np.abs(y - blur))]
    # reconstrucción: buena pero no perfecta; se borronea el detalle fino
    # (pasto, tejas, cerca), como en un VAE real con factor 8
    up = _resize(p, 512)
    suav = np.asarray(Image.fromarray((img * 255).astype(np.uint8)).filter(
        ImageFilter.GaussianBlur(2.2))) / 255.0
    rec = 0.55 * suav + 0.45 * up
    rec = np.asarray(Image.fromarray((rec * 255).astype(np.uint8)).filter(
        ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))) / 255.0
    rgris = rec @ np.array([0.299, 0.587, 0.114])
    dec = [_resize(rgris, 128), _resize(rgris, 256)]
    assert img.shape == (512, 512, 3) and img.size == 786_432
    assert all(m.shape == (64, 64) for m in lat) and 4 * 64 * 64 == 16_384
    assert 786_432 // 16_384 == 48
    return img, enc, lat, rec, dec


# geometría (simétrica respecto de x = 800)
V_Y, V_S = 205, 250                  # imágenes de entrada / salida
IN_X, OUT_X = 50, 1300
ENC = (340, 730)                     # caja del encoder
DEC = (870, 1260)
LAT_X, LAT_S, LAT_G = 764, 72, 8     # latente: 4 mapas apilados
ENC_B = [(405, 100), (535, 76), (665, 56)]    # (centro x, lado)
DEC_B = [(935, 56), (1065, 76), (1195, 100)]
ENC_L = ["256×256", "128×128", "64×64"]
DEC_L = ["128×128", "256×256", "512×512"]
BAR = (200, 1400, 684, 44)           # x0, x1, y, alto


def fmt(n):
    return f"{int(round(n)):,}".replace(",", ".")


def _vae_dibujar(ax, datos, *, n_enc=0, n_lat=0, n_dec=0, out_a=0.0,
                 act=None, t_act=1.0, valor=786_432, ratio=False,
                 formula="512 × 512 × 3 = 786.432", footer=""):
    img, enc, lat, rec, dec = datos
    preparar(ax)
    yc = V_Y + V_S / 2
    # entrada
    imagen(ax, img, IN_X, V_Y, V_S, V_S, interp="antialiased")
    rect(ax, IN_X, V_Y, V_S, V_S, fc="none",
         ec=ROJO if act == "in" else TINTA, lw=4 if act == "in" else 1.6, z=6)
    txt(ax, IN_X + V_S / 2, V_Y + V_S + 54, "512×512×3", size=24, bold=True)
    txt(ax, IN_X + V_S / 2, V_Y + V_S + 90, "imagen", size=20,
        color=GRIS_MEDIO)
    # encoder / decoder
    for (x0, x1), nombre, nota, bloques, labs, n_on, clave, mapas in (
            (ENC, "encoder", "solo en entrenamiento", ENC_B, ENC_L, n_enc,
             "enc", enc),
            (DEC, "decoder", "en inferencia", DEC_B, DEC_L, n_dec, "dec",
             dec + [None])):
        activo = act is not None and act.startswith(clave)
        caja(ax, x0, V_Y - 25, x1 - x0, V_S + 50,
             fc=ROSA if activo else RELLENO, ec=ROJO if activo else TINTA,
             lw=3 if activo else 1.8, r=16, z=1)
        txt(ax, (x0 + x1) / 2, V_Y - 58, nombre, size=26, bold=True,
            color=ROJO if activo else TINTA)
        txt(ax, (x0 + x1) / 2, yc + 116, nota, size=19,
            color=GRIS_MEDIO, style="italic")
        for b, ((cx, s), lab) in enumerate(zip(bloques, labs)):
            x, y = cx - s / 2, yc - s / 2 - 14
            on = b < n_on
            es_act = act == f"{clave}{b}"
            if on or es_act:
                a = t_act if es_act else 1.0
                m = mapas[b]
                if m is None:                       # último bloque del decoder
                    m = rec @ np.array([0.299, 0.587, 0.114])
                imagen(ax, m, x, y, s, s, alpha=a,
                       interp="nearest" if s < m.shape[0] else "antialiased")
            rect(ax, x, y, s, s, fc="none" if (on or es_act) else "white",
                 ec=ROJO if es_act else TINTA, lw=3.5 if es_act else 1.4,
                 z=5)
            txt(ax, cx, yc + 64, lab,
                size=18, bold=es_act, color=ROJO if es_act else TINTA)
        for b in range(len(bloques) - 1):
            xa = bloques[b][0] + bloques[b][1] / 2 + 4
            xb = bloques[b + 1][0] - bloques[b + 1][1] / 2 - 4
            flecha(ax, xa, yc - 14, xb, yc - 14, color=GRIS_MEDIO, lw=1.8,
                   z=4)
    # flechas entre etapas
    flecha(ax, IN_X + V_S + 4, yc, ENC[0] - 4, yc,
           color=ROJO if act == "enc0" else GRIS_MEDIO)
    flecha(ax, 733, yc, 756, yc, color=ROJO if act == "lat" else GRIS_MEDIO)
    flecha(ax, 845, yc, 867, yc, color=ROJO if act == "dec0" else GRIS_MEDIO)
    flecha(ax, DEC[1] + 4, yc, OUT_X - 4, yc,
           color=ROJO if act == "out" else GRIS_MEDIO)
    # latente
    alto = 4 * LAT_S + 3 * LAT_G
    ly0 = yc - alto / 2
    for c in range(4):
        y = ly0 + c * (LAT_S + LAT_G)
        if c < n_lat:
            imagen(ax, lat[c], LAT_X, y, LAT_S, LAT_S)
        es_act = act == "lat" and c == n_lat - 1
        rect(ax, LAT_X, y, LAT_S, LAT_S, fc="none" if c < n_lat else "white",
             ec=ROJO if es_act else TINTA,
             lw=3.5 if es_act else 1.4, z=5)
    rect(ax, LAT_X - 6, ly0 - 6, LAT_S + 12, alto + 12, fc="none", ec=ROJO,
         lw=3 if n_lat else 1.2, z=5)
    txt(ax, 800, V_Y - 58, "latente", size=24, bold=True, color=ROJO)
    txt(ax, 800, V_Y + V_S + 54, "64×64×4", size=24, bold=True, color=ROJO)
    txt(ax, 800, V_Y + V_S + 90, "4 canales", size=20, color=GRIS_MEDIO)
    # salida
    if out_a > 0:
        imagen(ax, rec, OUT_X, V_Y, V_S, V_S, alpha=out_a,
               interp="antialiased")
    rect(ax, OUT_X, V_Y, V_S, V_S, fc="none" if out_a > 0 else "white",
         ec=ROJO if act == "out" else TINTA, lw=4 if act == "out" else 1.6,
         z=6)
    txt(ax, OUT_X + V_S / 2, V_Y + V_S + 54, "512×512×3", size=24, bold=True)
    txt(ax, OUT_X + V_S / 2, V_Y + V_S + 90, "reconstruida", size=20,
        color=GRIS_MEDIO)
    # barra de compresión
    x0, x1, by, bh = BAR
    rect(ax, x0, by, x1 - x0, bh, fc=RELLENO, ec=BORDE, lw=1.2, z=2)
    largo = (x1 - x0) * valor / 786_432
    rect(ax, x0, by, max(largo, 3), bh, fc=ROJO, ec=ROJO, lw=1, z=3)
    txt(ax, 800, by - 34, f"{fmt(valor)} valores", size=30, bold=True,
        color=ROJO if valor < 700_000 else TINTA)
    txt(ax, 800, by + bh + 32, formula, size=20, color=GRIS_MEDIO)
    if ratio:
        txt(ax, x0 + max(largo, 3) + 18, by + bh / 2, "÷ 48", size=28,
            bold=True, color=ROJO, ha="left")
    pie(ax, footer)


def vae_en_vivo(fps=10, pausa_s=3.0):
    datos = _vae_datos()
    fig, ax = lienzo()
    fr = []

    def cap(**kw):
        _vae_dibujar(ax, datos, **kw)
        fr.append(capturar(fig))

    for _ in range(14):
        cap(act="in", footer="Entrada: imagen RGB de 512×512 píxeles × 3 "
                             "canales = 786.432 valores")
    pies_enc = ["bloque 1 del encoder: convoluciones y bajada de resolución, "
                "512 → 256",
                "bloque 2: 256 → 128; menos píxeles, más canales de features",
                "bloque 3: 128 → 64; cada posición cubre un parche de 8×8 "
                "píxeles"]
    for b in range(3):
        for f in range(10):
            cap(n_enc=b, act=f"enc{b}", t_act=suave((f + 1) / 6),
                footer=pies_enc[b])
    for c in range(4):
        for f in range(7):
            t = (c * 7 + f + 1) / 28
            v = 786_432 + (16_384 - 786_432) * suave(t)
            cap(n_enc=3, n_lat=c + 1, act="lat", valor=v,
                formula="64 × 64 × 4 = 16.384" if t > 0.5 else
                "512 × 512 × 3 = 786.432",
                footer=f"Latente: el encoder produce 4 canales de 64×64 "
                       f"(canal {c + 1} de 4)")
    for _ in range(14):
        cap(n_enc=3, n_lat=4, act="lat", valor=16_384, ratio=True,
            formula="64 × 64 × 4 = 16.384",
            footer="786.432 → 16.384 valores: el latente es 48 veces más "
                   "chico que la imagen")
    pies_dec = ["bloque 1 del decoder: sube la resolución, 64 → 128",
                "bloque 2: 128 → 256",
                "bloque 3: 256 → 512; vuelve a 3 canales de color"]
    for b in range(3):
        for f in range(10):
            cap(n_enc=3, n_lat=4, n_dec=b, act=f"dec{b}",
                t_act=suave((f + 1) / 6), valor=16_384,
                formula="64 × 64 × 4 = 16.384", footer=pies_dec[b])
    for f in range(16):
        t = suave((f + 1) / 12)
        v = 16_384 + (786_432 - 16_384) * t
        cap(n_enc=3, n_lat=4, n_dec=3, out_a=t, act="out", valor=v,
            formula="512 × 512 × 3 = 786.432" if t > 0.5 else
            "64 × 64 × 4 = 16.384",
            footer="decoder(encoder(imagen)) ≈ imagen: se pierde algo del "
                   "detalle fino (cerca, tejas, ventanas)")
    _vae_dibujar(ax, datos, n_enc=3, n_lat=4, n_dec=3, out_a=1.0,
                 valor=16_384, ratio=True, formula="64 × 64 × 4 = 16.384",
                 footer="La U-Net opera sobre el latente de 16.384 valores; "
                        "el decoder lo devuelve a píxeles")
    fr.append(capturar(fig))
    plt.close(fig)
    fr[-1].save(os.path.join(OUT, "vae-en-vivo.png"))
    guardar_gif(fr, os.path.join(OUT, "vae-en-vivo.gif"), fps=fps,
                pausa_s=pausa_s, colores=128)
    return fr


# =========================================================================
# 3. CLIP: un paso de entrenamiento de cerca (modelo chico, cuentas reales)
# =========================================================================
VOCAB = ["perro", "playa", "gato", "sofá", "sol", "montañas", "auto", "ruta",
         "en", "un", "sobre", "la"]
TAU = 0.07
ETA = 0.001
PASOS = 11                           # 1 paso en detalle + 10 rápidos


def _ce_datos():
    """Modelo chico de CLIP en numpy.

    text encoder : x_txt (promedio one-hot de las palabras, 12) -> W_t (8x12)
                   -> L2. Cada columna de W_t es el embedding de una palabra,
                   así que W_t·x_txt = promedio de los embeddings del texto.
    image encoder: x_img (imagen 8x8 en grises, estandarizada, 64) -> W_i
                   (8x64) -> L2.
    Pérdida      : entropía cruzada simétrica de CLIP sobre logits = S / τ.
    Gradientes analíticos, verificados contra diferencias finitas.
    """
    Xt = np.zeros((N, len(VOCAB)))
    for k, t in enumerate(TEXTOS):
        ws = t.split()
        for w in ws:
            Xt[k, VOCAB.index(w)] += 1 / len(ws)
    ims = _clip_imagenes()
    px = np.array([im.reshape(8, 15, 8, 15).mean((1, 3)) for im in ims])
    Xi = px.reshape(N, 64)
    Xi = (Xi - Xi.mean(1, keepdims=True)) / Xi.std(1, keepdims=True)
    Y = np.eye(N)

    def paso(Wt, Wi):
        Zt, Zi = Xt @ Wt.T, Xi @ Wi.T
        nt = np.linalg.norm(Zt, axis=1, keepdims=True)
        ni = np.linalg.norm(Zi, axis=1, keepdims=True)
        T, I = Zt / nt, Zi / ni
        S = I @ T.T
        lg = S / TAU
        Pr = np.exp(lg - lg.max(1, keepdims=True))
        Pr /= Pr.sum(1, keepdims=True)
        Pc = np.exp(lg - lg.max(0, keepdims=True))
        Pc /= Pc.sum(0, keepdims=True)
        Li = -np.mean(np.log(np.diag(Pr)))
        Lt = -np.mean(np.log(np.diag(Pc)))
        dS = ((Pr - Y) / N + (Pc - Y) / N) / 2 / TAU
        dI, dT = dS @ T, dS.T @ I
        dZi = (dI - I * (I * dI).sum(1, keepdims=True)) / ni
        dZt = (dT - T * (T * dT).sum(1, keepdims=True)) / nt
        return dict(T=T, I=I, S=S, Pr=Pr, Pc=Pc, Li=Li, Lt=Lt,
                    L=(Li + Lt) / 2, gWt=dZt.T @ Xt, gWi=dZi.T @ Xi)

    rng = np.random.default_rng(27)
    Wt = rng.normal(0, 0.04, (8, len(VOCAB)))
    Wi = rng.normal(0, 0.03, (8, 64))
    # verificación del gradiente por diferencias finitas
    f0 = paso(Wt, Wi)
    eps = 1e-6
    for W, g, cual in ((Wt, f0["gWt"], 0), (Wi, f0["gWi"], 1)):
        for (a, b) in ((0, 0), (3, 5), (7, W.shape[1] - 1)):
            Wp, Wm = W.copy(), W.copy()
            Wp[a, b] += eps
            Wm[a, b] -= eps
            args_p = (Wp, Wi) if cual == 0 else (Wt, Wp)
            args_m = (Wm, Wi) if cual == 0 else (Wt, Wm)
            num = (paso(*args_p)["L"] - paso(*args_m)["L"]) / (2 * eps)
            assert abs(num - g[a, b]) < 1e-6 * max(1, abs(num)), (cual, a, b)
    estados = []
    for k in range(PASOS + 1):
        f = paso(Wt, Wi)
        f.update(Wt=Wt.copy(), Wi=Wi.copy())
        estados.append(f)
        Wt = Wt - ETA * f["gWt"]
        Wi = Wi - ETA * f["gWi"]
    Ls = [e["L"] for e in estados]
    assert all(b < a for a, b in zip(Ls, Ls[1:])), Ls
    return Xt, px, estados


def _div_rgb(M, escala):
    """Matriz -> RGB divergente: negativo tinta, 0 blanco, positivo rojo."""
    t = np.clip(M / (escala + 1e-12), -1, 1)[..., None]
    blanco = np.ones(3)
    rojo, tinta = np.array(to_rgb(ROJO)), np.array(to_rgb("#3A3A3A"))
    return np.where(t >= 0, blanco + t * (rojo - blanco),
                    blanco + (-t) * (tinta - blanco))


# geometría
CE_TX, CE_IX = (315, 845), (315, 845)          # cajas de los encoders (x)
CE_TY, CE_IY = (25, 410), (430, 815)           # (y)
HM_W_X, HM_G_X, HM_ANCHO = 448, 656, 176       # heatmaps W y ∂L/∂W
HM_T_Y, HM_T_ALTO = 108, 288                   # 12 filas de 24
HM_I_Y, HM_I_ALTO = 512, 288                   # 64 filas
CAP_Y = [158, 223, 288, 353]
FOTO_Y = [513, 591, 669, 747]
SC, SG, SX, SY = 70, 4, 995, 300               # matriz S
SM_C, SM_G, SM_X = 40, 3, 1346                 # matrices softmax
SMF_Y, SMC_Y = 100, 580
CURVA = (1345, 1540, 404, 488)                 # x0, x1, y0, y1


def _ce_celdas(x0, y0, c, g):
    return [[(x0 + j * (c + g), y0 + i * (c + g)) for j in range(N)]
            for i in range(N)]


def _ce_dibujar(ax, datos, e, *, fase=0, act_txt=-1, act_img=-1, n_T=4,
                n_I=4, n_S=4, n_fil=0, n_col=0, ver_L=False, part=None,
                g_alpha=0.0, W_t=None, W_i=None, formula=False, curva_n=0,
                paso_n=None, footer="", escalas=None):
    Xt, px, est = datos
    preparar(ax)
    sWt, sWi, gsWt, gsWi = escalas
    Wt = e["Wt"] if W_t is None else W_t
    Wi = e["Wi"] if W_i is None else W_i
    # ---- entradas ----
    txt(ax, 40, 100, "textos", size=18, color=GRIS_MEDIO, ha="left")
    for k in range(N):
        roja = k == act_txt
        ws = TEXTOS[k].split()
        corte = 2 if len(ws) == 4 else 2
        dos = f"“{' '.join(ws[:corte])}\n{' '.join(ws[corte:])}”"
        txt(ax, 40, CAP_Y[k], dos, size=18, style="italic", ha="left",
            color=ROJO if roja else TINTA, bold=roja, linespacing=1.15)
        flecha(ax, 200, CAP_Y[k], CE_TX[0] - 3, CAP_Y[k],
               color=ROJO if roja else GRIS_MEDIO, lw=2.4 if roja else 1.6)
    txt(ax, 40, 484, "imágenes 8×8", size=18, color=GRIS_MEDIO, ha="left")
    for k in range(N):
        roja = k == act_img
        y = FOTO_Y[k]
        txt(ax, 138, y + 32, f"foto {k + 1}", size=18,
            color=ROJO if roja else GRIS_MEDIO, bold=roja, ha="right")
        imagen(ax, px[k], 150, y, 64, 64)
        rect(ax, 150, y, 64, 64, fc="none", ec=ROJO if roja else TINTA,
             lw=3.5 if roja else 1.4, z=5)
        flecha(ax, 220, y + 32, CE_IX[0] - 3, y + 32,
               color=ROJO if roja else GRIS_MEDIO, lw=2.4 if roja else 1.6)
    # ---- encoders ----
    for nombre, (x0, x1), (y0, y1), W, esc, g, gesc, hy, halto, act, \
            clave in (
            ("text encoder", CE_TX, CE_TY, Wt.T, sWt, e["gWt"].T, gsWt,
             HM_T_Y, HM_T_ALTO, act_txt >= 0, "t"),
            ("image encoder", CE_IX, CE_IY, Wi.T, sWi, e["gWi"].T, gsWi,
             HM_I_Y, HM_I_ALTO, act_img >= 0, "i")):
        activo = act or formula or g_alpha > 0.99 and fase == 3
        caja(ax, x0, y0, x1 - x0, y1 - y0, fc=ROSA if activo else RELLENO,
             ec=ROJO if activo else TINTA, lw=3 if activo else 1.8, r=14,
             z=1)
        txt(ax, x0 + 14, y0 + 36, nombre.replace(" ", "\n"), size=20,
            bold=True, ha="left", color=ROJO if activo else TINTA,
            linespacing=1.1)
        if formula:
            txt(ax, x1 - 16, y0 + 30, "W ← W − η · ∂L/∂W", size=19,
                bold=True, color=ROJO, ha="right")
        filas = W.shape[0]
        txt(ax, HM_W_X + HM_ANCHO, hy - 18,
            f"W  ({filas} × 8)", size=18, bold=True, ha="right")
        txt(ax, HM_G_X + HM_ANCHO / 2, hy - 18, "∂L/∂W", size=18,
            bold=True, color=ROJO if g_alpha > 0 else GRIS_MEDIO)
        imagen(ax, _div_rgb(W, esc), HM_W_X, hy, HM_ANCHO, halto)
        rect(ax, HM_W_X, hy, HM_ANCHO, halto, fc="none",
             ec=ROJO if formula else TINTA, lw=3.5 if formula else 1.4, z=5)
        if g_alpha > 0:
            # escala FIJA (la del paso 0): el gradiente se apaga al bajar L
            imagen(ax, _div_rgb(g, gesc), HM_G_X, hy, HM_ANCHO,
                   halto, alpha=g_alpha)
            norma = f"‖∂L/∂W‖ = {np.linalg.norm(g):.1f}".replace(".", ",")
            ax.text(HM_G_X + HM_ANCHO / 2, hy + halto - 18, norma,
                    fontsize=16, fontweight="bold", color=ROJO, ha="center",
                    va="center", zorder=8, alpha=g_alpha,
                    bbox=dict(boxstyle="round,pad=0.25", fc="white",
                              ec=ROJO, lw=1.2, alpha=0.92 * g_alpha))
        rect(ax, HM_G_X, hy, HM_ANCHO, halto, fc="none",
             ec=ROJO if g_alpha > 0 else BORDE, lw=2 if g_alpha > 0 else 1.4,
             ls="-" if g_alpha > 0 else "--", z=5)
        if clave == "t":
            for r, w in enumerate(VOCAB):
                yy = hy + (r + 0.5) * halto / filas
                usada = act_txt >= 0 and w in TEXTOS[act_txt].split()
                txt(ax, HM_W_X - 10, yy, w, size=17 if len(w) < 8 else 16,
                    ha="right", color=ROJO if usada else TINTA, bold=usada)
                if usada:
                    rect(ax, HM_W_X - 2, hy + r * halto / filas - 1,
                         HM_ANCHO + 4, halto / filas + 2, fc="none", ec=ROJO,
                         lw=2.5, z=6)
        else:
            ax.plot([HM_W_X - 12] * 2, [hy + 2, hy + halto - 2],
                    color=GRIS_MEDIO, lw=1.6, zorder=5)
            for yy in (hy + 2, hy + halto - 2):
                ax.plot([HM_W_X - 18, HM_W_X - 12], [yy, yy],
                        color=GRIS_MEDIO, lw=1.6, zorder=5)
            txt(ax, HM_W_X - 26, hy + halto / 2, "64\npíxeles", size=18,
                ha="right", color=TINTA, linespacing=1.2)
            if act_img >= 0:
                rect(ax, HM_W_X - 3, hy - 3, HM_ANCHO + 6, halto + 6,
                     fc="none", ec=ROJO, lw=3, z=6)
    # ---- vectores y matriz S ----
    celdas = _ce_celdas(SX, SY, SC, SG)
    flecha(ax, CE_TX[1] + 4, 220, SX + 8, 238,
           color=ROJO if act_txt >= 0 else GRIS_MEDIO)
    flecha(ax, CE_IX[1] + 4, 650, 936, SY + 4 * (SC + SG) - 22,
           color=ROJO if act_img >= 0 else GRIS_MEDIO)
    for j in range(N):
        cx = SX + j * (SC + SG) + SC / 2
        txt(ax, cx, 178, f"T{j + 1}", size=18, bold=True,
            color=ROJO if j == act_txt else TINTA)
        for d in range(8):
            fc = _vec_color(e["T"][j, d]) if j < n_T else "white"
            rect(ax, cx - 9, 196 + 11 * d, 18, 11, fc=fc, ec=BORDE, lw=0.6,
                 z=5)
    for i in range(N):
        cy = SY + i * (SC + SG) + SC / 2
        txt(ax, 884, cy, f"I{i + 1}", size=18, bold=True, ha="right",
            color=ROJO if i == act_img else TINTA)
        for d in range(8):
            fc = _vec_color(e["I"][i, d]) if i < n_I else "white"
            rect(ax, 892 + 11 * d, cy - 9, 11, 18, fc=fc, ec=BORDE, lw=0.6,
                 z=5)
    for i in range(N):
        for j in range(N):
            x, y = celdas[i][j]
            if i < n_S:
                v = e["S"][i, j]
                fc = _celda_color(i, j, v)
                osc = (i == j and v > 0.45) or (i != j and v > 0.55)
                rect(ax, x, y, SC, SC, fc=fc, ec=ROJO if i == j else BORDE,
                     lw=2.5 if i == j else 1, z=3)
                vv = 0.0 if abs(v) < 0.005 else v
                txt(ax, x + SC / 2, y + SC / 2, f"{vv:.2f}".replace(".", ","),
                    size=17, bold=i == j, color="white" if osc else TINTA)
            else:
                rect(ax, x, y, SC, SC, fc="white", ec=BORDE, lw=1, z=3)
    sxm = SX + (4 * SC + 3 * SG) / 2
    txt(ax, sxm, SY + 4 * (SC + SG) + 22, "S = coseno(Iᵢ, Tⱼ)", size=18,
        bold=True)
    txt(ax, sxm, SY + 4 * (SC + SG) + 52,
        "logits = S / τ,  τ = 0,07", size=18, color=GRIS_MEDIO)
    # ---- softmax por filas y por columnas ----
    for titulo, sub, y0, P, n_on, fila in (
            ("softmax", "por filas", SMF_Y, e["Pr"], n_fil, True),
            ("softmax", "por columnas", SMC_Y, e["Pc"], n_col, False)):
        cx = SM_X + (4 * SM_C + 3 * SM_G) / 2
        col = ROJO if fase == 2 and n_on and n_on < 4 else TINTA
        txt(ax, cx, y0 - 46, titulo, size=18, bold=True, color=col)
        txt(ax, cx, y0 - 20, sub, size=18, bold=True, color=col)
        cel = _ce_celdas(SM_X, y0, SM_C, SM_G)
        for i in range(N):
            for j in range(N):
                x, y = cel[i][j]
                on = (i if fila else j) < n_on
                p = P[i, j]
                fc = mezcla("white", ROJO if i == j else "#6E6866",
                            p) if on else "white"
                rect(ax, x, y, SM_C, SM_C, fc=fc, ec=BORDE, lw=0.8, z=3)
                if i == j:
                    rect(ax, x - 1.5, y - 1.5, SM_C + 3, SM_C + 3, fc="none",
                         ec=ROJO, lw=2.5, z=4)
        flecha(ax, SX + 4 * (SC + SG) + 2, SY + (2 if fila else 290),
               SM_X - 6, y0 + 85, color=GRIS_MEDIO, lw=1.6)
    if n_fil >= 4:
        txt(ax, SM_X + 84, SMF_Y + 192, f"L_img = {e['Li']:.2f}".replace(
            ".", ","), size=18, color=TINTA)
    if n_col >= 4:
        txt(ax, SM_X + 84, SMC_Y + 192, f"L_txt = {e['Lt']:.2f}".replace(
            ".", ","), size=18, color=TINTA)
    txt(ax, SM_X + 84, 326, "L = ½ (L_img + L_txt)", size=17,
        color=GRIS_MEDIO)
    if ver_L:
        txt(ax, SM_X + 84, 362, f"L = {e['L']:.2f}".replace(".", ","),
            size=26, bold=True, color=ROJO)
    # ---- curva de pérdida ----
    x0, x1, y0, y1 = CURVA
    ax.plot([x0, x0, x1], [y0, y1, y1], color=TINTA, lw=1.4, zorder=3)
    Ls = [s["L"] for s in est]
    lmax = Ls[0] * 1.08
    if curva_n:
        xs = [x0 + (x1 - x0) * k / PASOS for k in range(curva_n)]
        ys = [y1 - (y1 - y0) * L / lmax for L in Ls[:curva_n]]
        ax.plot(xs, ys, color=ROJO, lw=2.5, zorder=4)
        ax.plot(xs, ys, "o", color=ROJO, ms=5, zorder=5)
    txt(ax, x1, y1 + 18, "paso" if paso_n is None else f"paso {paso_n}",
        size=17, color=GRIS_MEDIO, ha="right")
    txt(ax, x0 - 8, y0 + 6, "L", size=17, color=GRIS_MEDIO, ha="right")
    # ---- partículas del backward ----
    if part is not None:
        cs = SX + 2 * (SC + SG)
        ce = SY + 2 * (SC + SG)
        lx = SM_X + 84
        caminos = [
            [(lx, 362), (lx, SMF_Y + 84), (cs, ce), (cs, 240),
             (HM_G_X + HM_ANCHO / 2, HM_T_Y + HM_T_ALTO / 2)],
            [(lx, 362), (lx, SMC_Y + 84), (cs, ce), (936, ce),
             (HM_G_X + HM_ANCHO / 2, HM_I_Y + HM_I_ALTO / 2)]]
        for cam in caminos:
            for q in range(5):
                tq = part - 0.06 * q
                if 0 < tq < 1:
                    x, y = _sobre_camino(cam, tq)
                    ax.add_patch(Circle((x, y), 9 - q, fc=ROJO, ec="white",
                                        lw=1.2, alpha=1 - 0.15 * q, zorder=9))
    pie(ax, footer)


def clip_entrenamiento(fps=12, pausa_s=3.0):
    datos = _ce_datos()
    Xt, px, est = datos
    escalas = (max(np.abs(s["Wt"]).max() for s in est) * 0.8,
               max(np.abs(s["Wi"]).max() for s in est) * 0.8,
               np.abs(est[0]["gWt"]).max() * 0.7,      # escala fija de
               np.abs(est[0]["gWi"]).max() * 0.7)      # ∂L/∂W: la del paso 0
    fig, ax = lienzo()
    fr = []
    e0 = est[0]

    def cap(e=e0, **kw):
        _ce_dibujar(ax, datos, e, escalas=escalas, **kw)
        fr.append(capturar(fig))

    pie_fw = ("forward: cada encoder proyecta su entrada a 8 dimensiones y "
              "normaliza; S compara cada I con cada T")
    for _ in range(8):
        cap(n_T=0, n_I=0, n_S=0, footer="Un paso de entrenamiento, con "
            "cuentas reales: 2 encoders lineales y un batch de 4 pares")
    for k in range(N):
        for _ in range(5):
            cap(fase=1, act_txt=k, n_T=k + 1, n_I=0, n_S=0, footer=pie_fw)
    for k in range(N):
        for _ in range(5):
            cap(fase=1, act_img=k, n_I=k + 1, n_S=0, footer=pie_fw)
    for i in range(N):
        for _ in range(2):
            cap(fase=1, n_S=i + 1, footer=pie_fw)
    pie_l = ("pérdida: softmax por filas (imagen → textos) y por columnas "
             "(texto → imágenes); objetivo: la diagonal")
    for i in range(N):
        for _ in range(3):
            cap(fase=2, n_fil=i + 1, footer=pie_l)
    for i in range(N):
        for _ in range(3):
            cap(fase=2, n_fil=4, n_col=i + 1, footer=pie_l)
    for _ in range(12):
        cap(fase=2, n_fil=4, n_col=4, ver_L=True, curva_n=1, paso_n=0,
            footer=pie_l)
    pie_b = ("backward: el gradiente de la pérdida se propaga a los pesos "
             "de los dos encoders")
    base = dict(n_fil=4, n_col=4, ver_L=True, curva_n=1, paso_n=0)
    for f in range(26):
        t = (f + 1) / 22
        cap(fase=3, part=t, g_alpha=float(np.clip((t - 0.85) / 0.15, 0, 1)),
            footer=pie_b, **base)
    for _ in range(8):
        cap(fase=3, g_alpha=1.0, footer=pie_b, **base)
    pie_u = (f"actualización: W ← W − η·∂L/∂W en los dos encoders "
             f"(η = {ETA:g})".replace(".", ","))
    e1 = est[1]
    for f in range(18):
        t = suave((f + 1) / 12)
        cap(fase=4, g_alpha=1.0, formula=True,
            W_t=(1 - t) * e0["Wt"] + t * e1["Wt"],
            W_i=(1 - t) * e0["Wi"] + t * e1["Wi"], footer=pie_u, **base)
    for s in range(1, PASOS + 1):
        e = est[s]
        for f in range(7):
            cap(e, fase=5, n_fil=4, n_col=4, ver_L=True, curva_n=s + 1,
                paso_n=s, g_alpha=1.0, formula=f < 3,
                footer=f"Se repite forward → pérdida → backward → "
                       f"actualización: paso {s} de {PASOS}, "
                       f"L = {e['L']:.2f}".replace(".", ","))
    eF = est[-1]
    dg0, dgF = np.mean(np.diag(e0["S"])), np.mean(np.diag(eF["S"]))
    _ce_dibujar(ax, datos, eF, escalas=escalas, n_fil=4, n_col=4, ver_L=True,
                curva_n=PASOS + 1, paso_n=PASOS, g_alpha=1.0,
                footer=f"Tras {PASOS} pasos: L baja de {e0['L']:.2f} a "
                       f"{eF['L']:.2f} y la diagonal de S sube de {dg0:.2f} "
                       f"a {dgF:.2f}".replace(".", ","))
    fr.append(capturar(fig))
    plt.close(fig)
    fr[-1].save(os.path.join(OUT, "clip-entrenamiento.png"))
    guardar_gif(fr, os.path.join(OUT, "clip-entrenamiento.gif"), fps=fps,
                pausa_s=pausa_s, colores=128)
    return fr


TAREAS = {"clip": clip_en_vivo, "vae": vae_en_vivo,
          "clip-entrenamiento": clip_entrenamiento}

if __name__ == "__main__":
    for nombre in (sys.argv[1:] or TAREAS):
        frames = TAREAS[nombre]()
        dbg = os.environ.get("DBG_DIR")
        if dbg:
            os.makedirs(dbg, exist_ok=True)
            n = len(frames)
            for k, i in enumerate((10, n // 3, n // 2, (3 * n) // 4, n - 1)):
                frames[i].save(os.path.join(dbg, f"{nombre}-{k}.png"))
