#!/usr/bin/env python3
"""Genera las animaciones y figuras de convolución de la Talk
"segmentacion-y-stable-diffusion".

Todas las señales e imágenes son sintéticas (numpy). Salida en ../../images/:

  conv1d-filtrado.gif        kernel de promedio móvil suavizando audio con ruido
  conv1d-detector-voz.gif    energía local con umbral que detecta tramos de voz
  conv1d-largo-variable.png  el mismo kernel sobre audios de 2 s y de 5 s
  conv2d-kernel.gif          kernel 3x3 de bordes recorriendo una grilla 7x7
  conv2d-bordes.png          Sobel vertical y horizontal sobre una imagen sintética
  fcn-dimensiones.png        recorrido de tensores de un FCN-32s (VGG16, 224x224)
  fcn-en-vivo.gif            el mismo FCN construyéndose etapa por etapa
  unet-dimensiones.png       la U de una U-Net con padding (256x256), con skips
  unet-en-vivo.gif           la misma U-Net construyéndose etapa por etapa

Uso:  python3 gen_animaciones_conv.py [nombre ...]   (sin argumentos genera todo)
Requiere numpy, matplotlib y pillow.
"""
import os
import sys

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle, ConnectionPatch  # noqa: E402
from PIL import Image  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(AQUI, "..", "..", "images"))

# --- Estilo común ---------------------------------------------------------
TINTA = "#222222"
ROJO = "#D7192A"
ROJO_CLARO = "#F6C9CD"
RELLENO = "#F1EDEC"
GRIS_MEDIO = "#8A8583"
W, H, DPI = 16, 9, 100          # 1600 x 900 px
FPS = 13
PAUSA_S = 1.2

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 20,
    "axes.edgecolor": TINTA,
    "axes.labelcolor": TINTA,
    "xtick.color": TINTA,
    "ytick.color": TINTA,
    "axes.linewidth": 1.4,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})

RNG = np.random.default_rng(7)


def limpiar(ax, ejes=("left", "bottom")):
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(s in ejes)


def capturar(fig):
    fig.canvas.draw()
    return Image.fromarray(np.asarray(fig.canvas.buffer_rgba())[..., :3].copy())


def guardar_gif(frames, ruta, fps=FPS, pausa_s=PAUSA_S, colores=48):
    """Paleta común (cuantizada sobre una muestra de cuadros) y loop infinito."""
    muestra = frames[:: max(1, len(frames) // 8)] + [frames[-1]]
    ancho, alto = frames[0].size
    mosaico = Image.new("RGB", (ancho, alto * len(muestra)))
    for i, f in enumerate(muestra):
        mosaico.paste(f, (0, alto * i))
    paleta = mosaico.quantize(colors=colores, method=Image.Quantize.MEDIANCUT)
    # fijar los colores de marca exactos (blanco, tinta, rojo) en la paleta
    pal_rgb = np.array(paleta.getpalette()[: 3 * colores]).reshape(-1, 3)
    for hexcol in ("#FFFFFF", TINTA, ROJO):
        c = np.array([int(hexcol[i:i + 2], 16) for i in (1, 3, 5)])
        pal_rgb[np.argmin(((pal_rgb - c) ** 2).sum(1))] = c
    plano = [int(v) for v in pal_rgb.ravel()]
    pal_f = pal_rgb.astype(np.int32)

    def mapear(f):
        # vecino más cercano exacto (el de Pillow redondea y corre el blanco)
        a = np.asarray(f, dtype=np.int32)
        clave = (a[..., 0] << 16) | (a[..., 1] << 8) | a[..., 2]
        unicos, inv = np.unique(clave, return_inverse=True)
        rgb = np.stack([unicos >> 16, (unicos >> 8) & 255, unicos & 255], 1)
        idx = ((rgb[:, None, :] - pal_f[None]) ** 2).sum(2).argmin(1)
        p = Image.fromarray(idx[inv].reshape(clave.shape).astype(np.uint8), "P")
        p.putpalette(plano)
        return p

    pal = [mapear(f) for f in frames]
    dur = [int(1000 / fps)] * len(pal)
    dur[-1] = int(pausa_s * 1000)
    pal[0].save(ruta, save_all=True, append_images=pal[1:], duration=dur,
                loop=0, optimize=True, disposal=1)
    print(f"{ruta}  {os.path.getsize(ruta) / 1e6:.2f} MB  {len(pal)} cuadros")


# =========================================================================
# 1. conv1d-filtrado.gif
# =========================================================================
def conv1d_filtrado():
    n, k = 160, 9
    t = np.arange(n)
    limpia = np.sin(2 * np.pi * t / 80) + 0.45 * np.sin(2 * np.pi * t / 37)
    x = limpia + 0.38 * RNG.standard_normal(n)
    pesos = np.ones(k) / k
    y = np.convolve(x, pesos, mode="same")
    m = k // 2
    centros = list(range(m, n - m, 2)) + [n - m - 1]

    fig = plt.figure(figsize=(W, H), dpi=DPI)
    ax1 = fig.add_axes([0.07, 0.56, 0.70, 0.36])
    axk = fig.add_axes([0.83, 0.60, 0.14, 0.26])
    ax2 = fig.add_axes([0.07, 0.10, 0.70, 0.36])
    ylim = (-2.6, 2.6)
    for ax in (ax1, ax2):
        ax.set_xlim(-2, n + 1)
        ax.set_ylim(*ylim)
        ax.set_yticks([])
        ax.set_xticks([])
        limpiar(ax, ("bottom",))
        ax.axhline(0, color=RELLENO, lw=1.5, zorder=0)
    ax1.plot(t, x, color=TINTA, lw=1.8)
    ax1.text(0, 2.75, "Entrada: audio con ruido", fontsize=24, color=TINTA,
             va="bottom")
    ax2.text(0, 2.75, "Salida: audio filtrado", fontsize=24, color=ROJO,
             va="bottom")
    ax2.set_xlabel("tiempo", fontsize=20)

    # panel del kernel
    axk.bar(np.arange(k), pesos, color=ROJO, width=0.75)
    axk.set_ylim(0, 0.2)
    axk.set_xlim(-0.8, k - 0.2)
    axk.set_xticks([])
    axk.set_yticks([])
    limpiar(axk, ("bottom",))
    axk.text(k / 2 - 0.5, 0.215, "Kernel", ha="center", va="bottom",
             fontsize=24, color=ROJO, fontweight="bold")
    axk.text(k / 2 - 0.5, -0.03, "9 pesos = 1/9\n(promedio móvil)",
             ha="center", va="top", fontsize=19, color=TINTA)

    ventana = Rectangle((0, ylim[0] + 0.1), k, ylim[1] - ylim[0] - 0.2,
                        facecolor=ROJO, alpha=0.13, edgecolor=ROJO, lw=2.5)
    ax1.add_patch(ventana)
    puntos_v, = ax1.plot([], [], "o", color=ROJO, ms=6)
    perfil, = ax1.plot([], [], color=ROJO, lw=3, drawstyle="steps-mid")
    salida, = ax2.plot([], [], color=ROJO, lw=2.8)
    punto_s, = ax2.plot([], [], "o", color=ROJO, ms=11)

    frames, con = [], None
    for c in centros:
        lo, hi = c - m, c + m + 1
        ventana.set_x(lo - 0.5)
        puntos_v.set_data(t[lo:hi], x[lo:hi])
        # perfil de pesos dibujado al pie de la ventana
        perfil.set_data(np.arange(lo, hi), ylim[0] + 0.25 + pesos * 4.0)
        salida.set_data(t[m:c + 1], y[m:c + 1])
        punto_s.set_data([c], [y[c]])
        if con is not None:
            con.remove()
        con = ConnectionPatch(xyA=(c, ylim[0] + 0.1), coordsA=ax1.transData,
                              xyB=(c, y[c]), coordsB=ax2.transData,
                              color=ROJO, lw=2, ls="--")
        fig.add_artist(con)
        frames.append(capturar(fig))
    # pausa final: resultado completo, sin ventana
    ventana.set_visible(False)
    puntos_v.set_data([], [])
    perfil.set_data([], [])
    punto_s.set_data([], [])
    con.remove()
    ax2.plot(t, limpia, color=GRIS_MEDIO, lw=1.2, ls=":", zorder=0)
    frames.append(capturar(fig))
    plt.close(fig)
    guardar_gif(frames, os.path.join(OUT, "conv1d-filtrado.gif"))


# =========================================================================
# 2. conv1d-detector-voz.gif
# =========================================================================
def conv1d_detector_voz():
    n, k = 420, 31
    t = np.arange(n)
    x = 0.07 * RNG.standard_normal(n)
    for a, b in ((90, 170), (260, 360)):
        u = np.arange(b - a)
        env = np.sin(np.pi * u / (b - a)) ** 0.6
        x[a:b] += env * (0.9 * np.sin(2 * np.pi * u / 9)
                         + 0.35 * np.sin(2 * np.pi * u / 4.3))
    pesos = np.ones(k) / k
    e = np.convolve(x ** 2, pesos, mode="same")
    umbral = 0.12
    m = k // 2
    centros = list(range(m, n - m, 4)) + [n - m - 1]
    detect = e > umbral

    fig = plt.figure(figsize=(W, H), dpi=DPI)
    ax1 = fig.add_axes([0.07, 0.57, 0.70, 0.34])
    axk = fig.add_axes([0.83, 0.61, 0.14, 0.24])
    ax2 = fig.add_axes([0.07, 0.10, 0.70, 0.36])
    ax1.set_xlim(-3, n + 3)
    ax2.set_xlim(-3, n + 3)
    ax1.set_ylim(-1.45, 1.45)
    emax = e.max() * 1.15
    ax2.set_ylim(0, emax)
    for ax in (ax1, ax2):
        ax.set_xticks([])
        ax.set_yticks([])
        limpiar(ax, ("bottom",))
    ax1.axhline(0, color=RELLENO, lw=1.5, zorder=0)
    ax1.plot(t, x, color=TINTA, lw=1.3)
    ax1.text(0, 1.52, "Entrada: audio", fontsize=24, color=TINTA, va="bottom")
    ax2.text(0, emax * 1.03, "Salida: energía local", fontsize=24, color=ROJO,
             va="bottom")
    ax2.set_xlabel("tiempo", fontsize=20)
    ax2.axhline(umbral, color=TINTA, lw=2, ls=(0, (6, 4)))
    ax2.text(n + 2, umbral, "umbral", fontsize=20, color=TINTA, va="bottom",
             ha="right")

    axk.bar(np.arange(k), pesos, color=ROJO, width=0.8)
    axk.set_ylim(0, 0.045)
    axk.set_xlim(-1, k)
    axk.set_xticks([])
    axk.set_yticks([])
    limpiar(axk, ("bottom",))
    axk.text(k / 2, 0.048, "Kernel", ha="center", va="bottom", fontsize=24,
             color=ROJO, fontweight="bold")
    axk.text(k / 2, -0.006, "ventana sobre\nla señal al cuadrado",
             ha="center", va="top", fontsize=19, color=TINTA)

    ventana = Rectangle((0, -1.4), k, 2.8, facecolor=ROJO, alpha=0.13,
                        edgecolor=ROJO, lw=2.5)
    ax1.add_patch(ventana)
    salida, = ax2.plot([], [], color=ROJO, lw=2.8)
    punto_s, = ax2.plot([], [], "o", color=ROJO, ms=11)
    sombras, textos = [], []

    def tramos(hasta):
        d = detect.copy()
        d[hasta + 1:] = False
        d[:m] = False
        res, ini = [], None
        for i, v in enumerate(d):
            if v and ini is None:
                ini = i
            if not v and ini is not None:
                res.append((ini, i))
                ini = None
        if ini is not None:
            res.append((ini, hasta + 1))
        return res

    frames, con = [], None
    for c in centros:
        ventana.set_x(c - m - 0.5)
        salida.set_data(t[m:c + 1], e[m:c + 1])
        punto_s.set_data([c], [e[c]])
        for s in sombras + textos:
            s.remove()
        sombras, textos = [], []
        for a, b in tramos(c):
            sombras.append(ax2.axvspan(a, b, color=ROJO_CLARO, alpha=0.75,
                                       zorder=0, lw=0))
            sombras.append(ax1.axvspan(a, b, color=ROJO_CLARO, alpha=0.55,
                                       zorder=0, lw=0))
            if b - a > 25:
                textos.append(ax2.text((a + b) / 2, emax * 0.88, "voz",
                                       ha="center", fontsize=24, color=ROJO,
                                       fontweight="bold"))
        if con is not None:
            con.remove()
        con = ConnectionPatch(xyA=(c, -1.4), coordsA=ax1.transData,
                              xyB=(c, e[c]), coordsB=ax2.transData,
                              color=ROJO, lw=2, ls="--")
        fig.add_artist(con)
        frames.append(capturar(fig))
    ventana.set_visible(False)
    punto_s.set_data([], [])
    con.remove()
    frames.append(capturar(fig))
    plt.close(fig)
    guardar_gif(frames, os.path.join(OUT, "conv1d-detector-voz.gif"))


# =========================================================================
# 3. conv1d-largo-variable.png
# =========================================================================
def conv1d_largo_variable():
    fs = 50                                  # muestras por segundo (didáctico)
    pesos = np.array([1, 2, 3, 4, 3, 2, 1], float)
    pesos /= pesos.sum()
    k, m = len(pesos), len(pesos) // 2

    def audio(dur, semilla):
        r = np.random.default_rng(semilla)
        tt = np.arange(int(dur * fs)) / fs
        s = (np.sin(2 * np.pi * 0.9 * tt) + 0.5 * np.sin(2 * np.pi * 2.3 * tt + 1)
             + 0.35 * r.standard_normal(tt.size))
        return tt, s

    t2, a2 = audio(2, 3)
    t5, a5 = audio(5, 4)
    y2 = np.convolve(a2, pesos, mode="same")
    y5 = np.convolve(a5, pesos, mode="same")

    fig = plt.figure(figsize=(W, H), dpi=DPI)
    izq, ancho = 0.05, 0.66
    filas = [0.76, 0.555, 0.30, 0.085]
    alto = 0.16
    axs = [fig.add_axes([izq, f, ancho, alto]) for f in filas]
    for ax in axs:
        ax.set_xlim(-0.05, 5.05)
        ax.set_ylim(-2.6, 2.6)
        ax.set_yticks([])
        limpiar(ax, ("bottom",))
        ax.tick_params(labelsize=18)
        ax.set_xticks([0, 1, 2, 3, 4, 5])
        ax.set_xticklabels([])
    axs[3].set_xticklabels(["0 s", "1 s", "2 s", "3 s", "4 s", "5 s"])

    axs[0].plot(t2, a2, color=TINTA, lw=1.6)
    axs[1].plot(t2, y2, color=ROJO, lw=2.6)
    axs[2].plot(t5, a5, color=TINTA, lw=1.6)
    axs[3].plot(t5, y5, color=ROJO, lw=2.6)
    # el eje inferior solo llega hasta donde llega cada señal
    for ax, dur in ((axs[0], 2), (axs[1], 2)):
        ax.spines["bottom"].set_bounds(0, dur)
    for ax, txt, col in ((axs[0], "Audio de 2 s", TINTA),
                         (axs[1], "salida: 2 s", ROJO),
                         (axs[2], "Audio de 5 s", TINTA),
                         (axs[3], "salida: 5 s", ROJO)):
        ax.text(0, 2.75, txt, fontsize=22, color=col, va="bottom",
                fontweight="bold" if col == TINTA else "normal")

    # misma ventana roja sobre ambas entradas
    posiciones = ((axs[0], 1.2, a2), (axs[2], 3.4, a5))
    centros_fig = []
    for ax, tc, _ in posiciones:
        ax.add_patch(Rectangle((tc - (m + 0.5) / fs, -2.5), k / fs, 5.0,
                               facecolor=ROJO, alpha=0.15, edgecolor=ROJO,
                               lw=2.5))
        centros_fig.append((ax, tc))

    # panel del kernel
    axk = fig.add_axes([0.80, 0.42, 0.16, 0.22])
    axk.bar(np.arange(k), pesos, color=ROJO, width=0.75)
    axk.set_xticks([])
    axk.set_yticks([])
    axk.set_ylim(0, pesos.max() * 1.15)
    limpiar(axk, ("bottom",))
    axk.text(k / 2 - 0.5, pesos.max() * 1.22, "Kernel", ha="center",
             va="bottom", fontsize=24, color=ROJO, fontweight="bold")
    fig.text(0.88, 0.37, "mismo kernel,\nmismos pesos", ha="center", va="top",
             fontsize=22, color=TINTA)
    for ax, tc in centros_fig:
        fig.add_artist(ConnectionPatch(
            xyA=(0.80, 0.53), coordsA="figure fraction",
            xyB=(tc + (m + 0.5) / fs, 0), coordsB=ax.transData,
            arrowstyle="-|>", mutation_scale=22, color=ROJO, lw=2,
            connectionstyle="arc3,rad=0.0", shrinkB=6))
    fig.savefig(os.path.join(OUT, "conv1d-largo-variable.png"), dpi=DPI,
                facecolor="white")
    plt.close(fig)
    ruta = os.path.join(OUT, "conv1d-largo-variable.png")
    print(f"{ruta}  {os.path.getsize(ruta) / 1e6:.2f} MB")


# =========================================================================
# 4. conv2d-kernel.gif
# =========================================================================
def conv2d_kernel():
    entrada = np.array([
        [0, 1, 0, 5, 9, 9, 8],
        [1, 0, 0, 6, 9, 8, 9],
        [0, 0, 1, 5, 8, 9, 9],
        [0, 1, 0, 6, 9, 9, 8],
        [1, 0, 0, 5, 9, 8, 9],
        [0, 0, 1, 6, 8, 9, 9],
        [0, 1, 0, 5, 9, 9, 9],
    ])
    kern = np.array([[-1, 0, 1]] * 3)
    salida = np.zeros((5, 5), int)
    for i in range(5):
        for j in range(5):
            salida[i, j] = int((entrada[i:i + 3, j:j + 3] * kern).sum())

    fig = plt.figure(figsize=(W, H), dpi=DPI)
    cel = 0.085                                # lado de celda en fracción de alto
    asp = H / W

    def eje_grilla(x0, y0, nf, nc):
        ax = fig.add_axes([x0, y0, nc * cel * asp, nf * cel])
        ax.set_xlim(0, nc)
        ax.set_ylim(nf, 0)
        ax.axis("off")
        return ax

    y_in = 0.20
    xk, xo = 0.43, 0.665
    ax_in = eje_grilla(0.045, y_in, 7, 7)
    ax_k = eje_grilla(xk, y_in + 2 * cel, 3, 3)
    ax_o = eje_grilla(xo, y_in + cel, 5, 5)

    def gris(v):
        g = 1 - 0.62 * v / 9
        return (g, g, g * 0.985)

    for i in range(7):
        for j in range(7):
            v = entrada[i, j]
            ax_in.add_patch(Rectangle((j, i), 1, 1, facecolor=gris(v),
                                      edgecolor="white", lw=2))
            ax_in.text(j + 0.5, i + 0.52, str(v), ha="center", va="center",
                       fontsize=24, color=TINTA if v < 7 else "white",
                       fontweight="bold")
    for i in range(3):
        for j in range(3):
            v = kern[i, j]
            ax_k.add_patch(Rectangle((j, i), 1, 1, facecolor="white",
                                     edgecolor=ROJO, lw=2.5))
            ax_k.text(j + 0.5, i + 0.52, f"{v:+d}" if v else "0", ha="center",
                      va="center", fontsize=24, color=ROJO, fontweight="bold")
    celdas_o = {}
    for i in range(5):
        for j in range(5):
            r = Rectangle((j, i), 1, 1, facecolor="white", edgecolor="#CFC9C7",
                          lw=2)
            ax_o.add_patch(r)
            tx = ax_o.text(j + 0.5, i + 0.52, "", ha="center", va="center",
                           fontsize=24, color=TINTA, fontweight="bold")
            celdas_o[i, j] = (r, tx)

    fig.text(0.045 + 7 * cel * asp / 2, y_in + 7 * cel + 0.03,
             "Entrada (imagen)", ha="center", fontsize=26, color=TINTA)
    fig.text(xk + 3 * cel * asp / 2, y_in + 5 * cel + 0.03, "Kernel 3×3",
             ha="center", fontsize=26, color=ROJO, fontweight="bold")
    fig.text(xk + 3 * cel * asp / 2, y_in + 2 * cel - 0.025,
             "detecta bordes\nverticales", ha="center", va="top", fontsize=19,
             color=TINTA)
    fig.text(xo + 5 * cel * asp / 2, y_in + 6 * cel + 0.03, "Feature map",
             ha="center", fontsize=26, color=ROJO)
    fig.text(0.62, y_in + 3.5 * cel, "→", ha="center", va="center",
             fontsize=48, color=GRIS_MEDIO)
    fig.text(0.405, y_in + 3.5 * cel, "×", ha="center", va="center",
             fontsize=40, color=GRIS_MEDIO)

    ventana = Rectangle((0, 0), 3, 3, facecolor=ROJO, alpha=0.18,
                        edgecolor=ROJO, lw=5)
    ax_in.add_patch(ventana)
    cuenta = fig.text(0.5, 0.09, "", ha="center", fontsize=30, color=TINTA)

    frames, por_celda = [], 3
    previa = None
    for i in range(5):
        for j in range(5):
            ventana.set_xy((j, i))
            if previa is not None:
                r, tx = celdas_o[previa]
                r.set_facecolor(RELLENO)
                r.set_edgecolor("#CFC9C7")
                r.set_linewidth(2)
                tx.set_color(TINTA)
            r, tx = celdas_o[i, j]
            r.set_facecolor(ROJO_CLARO)
            r.set_edgecolor(ROJO)
            r.set_linewidth(4)
            tx.set_text(str(salida[i, j]))
            tx.set_color(ROJO)
            cuenta.set_text(f"suma de (entrada × kernel) = {salida[i, j]}")
            img = capturar(fig)
            frames.extend([img] * por_celda)
            previa = (i, j)
    # pausa final: mapa completo, sin ventana
    r, tx = celdas_o[previa]
    r.set_facecolor(RELLENO)
    r.set_edgecolor("#CFC9C7")
    r.set_linewidth(2)
    tx.set_color(TINTA)
    ventana.set_visible(False)
    for (i, j), (r, tx) in celdas_o.items():
        if salida[i, j] >= 20:
            r.set_facecolor(ROJO_CLARO)
            tx.set_color(ROJO)
    cuenta.set_text("los valores altos marcan dónde está el borde")
    frames.append(capturar(fig))
    plt.close(fig)
    guardar_gif(frames, os.path.join(OUT, "conv2d-kernel.gif"), fps=12,
                pausa_s=1.6, colores=32)


# =========================================================================
# 5. conv2d-bordes.png
# =========================================================================
def conv2(img, k):
    """Correlación 2D 'same' con borde replicado (como en las CNN)."""
    p = np.pad(img, 1, mode="edge")
    out = np.zeros_like(img)
    for di in range(3):
        for dj in range(3):
            out += k[di, dj] * p[di:di + img.shape[0], dj:dj + img.shape[1]]
    return out


def conv2d_bordes():
    n = 256
    yy, xx = np.mgrid[0:n, 0:n] / n
    img = 0.25 + 0.30 * xx + 0.10 * yy                     # degradé de fondo
    circ = (xx - 0.32) ** 2 + (yy - 0.36) ** 2 < 0.19 ** 2
    img[circ] = 0.92 - 0.25 * yy[circ]                     # círculo con degradé
    rect = (xx > 0.52) & (xx < 0.86) & (yy > 0.56) & (yy < 0.86)
    img[rect] = 0.08
    img = conv2(conv2(img, np.ones((3, 3)) / 9), np.ones((3, 3)) / 9)  # antialias
    sob_v = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], float)   # bordes verticales
    sob_h = sob_v.T                                                 # bordes horizontales
    bv = np.abs(conv2(img, sob_v))
    bh = np.abs(conv2(img, sob_h))
    escala = max(bv.max(), bh.max())

    fig = plt.figure(figsize=(W, H), dpi=DPI)
    lado = 0.50
    w = lado * H / W
    gap = (1 - 0.08 - 3 * w) / 2
    xs = [0.04, 0.04 + w + gap, 0.04 + 2 * (w + gap)]
    y0 = 0.31
    paneles = [(img, "Imagen", None, TINTA),
               (bv / escala, "Kernel de bordes verticales", sob_v, ROJO),
               (bh / escala, "Kernel de bordes horizontales", sob_h, ROJO)]
    for x0, (dat, etq, kk, col) in zip(xs, paneles):
        ax = fig.add_axes([x0, y0, lado * H / W, lado])
        ax.imshow(dat, cmap="gray", vmin=0, vmax=1, interpolation="lanczos")
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_color(TINTA if kk is None else ROJO)
            s.set_linewidth(1.6 if kk is None else 3)
        cx = x0 + lado * H / W / 2
        fig.text(cx, y0 - 0.035, etq, ha="center", va="top", fontsize=21,
                 color=col, fontweight="bold" if kk is not None else "normal")
        if kk is not None:
            # matriz del kernel debajo de la etiqueta
            axk = fig.add_axes([cx - 0.055, 0.03, 0.11, 0.11 * W / H * 0.75])
            axk.set_xlim(0, 3)
            axk.set_ylim(3, 0)
            axk.axis("off")
            for i in range(3):
                for j in range(3):
                    v = int(kk[i, j])
                    axk.add_patch(Rectangle((j, i), 1, 1, facecolor="white",
                                            edgecolor=ROJO, lw=1.5))
                    axk.text(j + 0.5, i + 0.55, f"{v:+d}" if v else "0",
                             ha="center", va="center", fontsize=18,
                             color=ROJO, fontweight="bold")
        if kk is not None:
            # flecha desde la imagen
            fig.text(x0 - gap / 2, y0 + lado / 2, "→", ha="center",
                     va="center", fontsize=30, color=GRIS_MEDIO)
    ruta = os.path.join(OUT, "conv2d-bordes.png")
    fig.savefig(ruta, dpi=DPI, facecolor="white")
    plt.close(fig)
    print(f"{ruta}  {os.path.getsize(ruta) / 1e6:.2f} MB")


# =========================================================================
# 6-7. FCN-32s por dentro: fcn-dimensiones.png y fcn-en-vivo.gif
# =========================================================================
# Recorrido de tensores de un FCN-32s sobre VGG16 con entrada 224x224.
# Cada bloque es un prisma: el lado de la cara crece con la resolución (escala
# log comprimida, para que el 7x7 se lea) y el espesor con log2(canales).
# La cara frontal NO es la imagen achicada: es UN canal de features calculado
# con numpy (bordes orientados al principio; respuestas cada vez más gruesas y
# concentradas en el gato al profundizar). En el 7x7x512 se saca el vector de
# una celda (el embedding de esa región) y la conv 1x1 se muestra como la misma
# capa densa 512 -> 21 aplicada celda por celda.
FCN_ETAPAS = [
    # (resolución, canales, dimensiones, descripción, operación, rótulo de cara)
    (224, 3, "224×224\n×3", "imagen", None, None),
    (112, 64, "112×112\n×64", "conv\n+ pool", "conv 3×3 + max pool 2×2",
     "1 de 64 canales"),
    (56, 128, "56×56\n×128", "conv\n+ pool", "conv 3×3 + max pool 2×2",
     "1 de 128"),
    (28, 256, "28×28\n×256", "conv\n+ pool", "conv 3×3 + max pool 2×2",
     "1 de 256"),
    (14, 512, "14×14\n×512", "conv\n+ pool", "conv 3×3 + max pool 2×2",
     "1 de 512"),
    (7, 512, "7×7\n×512", "conv\n+ pool", "conv 3×3 + max pool 2×2",
     "1 de 512"),
    (7, 21, "7×7\n×21", "conv 1×1\n(en vez de\ncapa densa)\n21 clases",
     "conv 1×1", "canal gato"),
    (224, 21, "224×224\n×21", "upsampling\n×32 (conv\ntraspuesta)",
     "upsampling ×32", None),
    (224, 1, "224×224", "máscara\n(argmax:\n1 clase\npor píxel)", "argmax",
     None),
]
FCN_PIES = {
    0: "Entrada: una imagen de 224×224 píxeles con 3 canales (RGB)",
    1: "224×224 → 112×112: 64 filtros buscan bordes; el pooling divide la"
       " resolución por 2",
    2: "112×112 → 56×56: 128 canales combinan bordes en esquinas y contornos",
    3: "56×56 → 28×28: 256 canales responden a partes: patas, cola, cuerpo",
    4: "28×28 → 14×14: cada canal es menos imagen y más «acá hay parte de gato»",
    5: "14×14 → 7×7: cinco poolings, 224 / 2⁵ = 7",
    "rf": "7×7: las celdas están a 32 píxeles de distancia; cada una ve una"
          " zona de unos 200 píxeles",
    "emb": "cada posición guarda un vector que describe qué hay en su región",
    6: "conv 1×1 = la misma capa densa aplicada a cada posición: 512 → 21"
       " puntajes",
    7: "upsampling ×32 (7 × 32 = 224): el canal gato vuelve al tamaño"
       " original, con bordes borrosos",
    8: "argmax: una clase por píxel, pero el contorno sale grueso y borroso",
}
FCN_LADO, FCN_YC, FCN_TESELAS, FCN_MIN = 170, 292, 7, 60
FCN_CELDA = (3, 3)                       # la celda del medio cae sobre el gato
FCN_N_VEC, FCN_GATO = 10, 8              # entradas dibujadas; índice de "gato"
SLICE = "#BDB5B2"


def _suavizar(a, sigma):
    """Gaussiana separable con borde replicado (numpy puro)."""
    r = int(3 * sigma) + 1
    x = np.arange(-r, r + 1)
    k = np.exp(-x ** 2 / (2 * sigma ** 2))
    k /= k.sum()
    p = np.pad(a, r, mode="edge")
    p = np.apply_along_axis(lambda v: np.convolve(v, k, "valid"), 0, p)
    return np.apply_along_axis(lambda v: np.convolve(v, k, "valid"), 1, p)


def _maxpool(a, f):
    r = a.shape[0] // f
    return a.reshape(r, f, r, f).max((1, 3))


def _meanpool(a, f):
    r = a.shape[0] // f
    return a.reshape(r, f, r, f).mean((1, 3))


def _norm99(a):
    a = np.maximum(a, 0)
    return np.clip(a / (np.percentile(a, 99.5) + 1e-9), 0, 1)


def _features(img, gato):
    """Tres canales plausibles por etapa de FCN, ya a la resolución de cada
    etapa (max pool 2^k). Lo oscuro de la cara = activación alta."""
    E = _features_crudos(img, gato)
    return {k: [_norm99(_maxpool(m, 2 ** k)) for m in ms] for k, ms in E.items()}


def _features_crudos(img, gato):
    """Tres mapas por etapa (1 = bordes orientados, 2 = esquinas y contorno,
    3 = partes: patas/cola, manchas, 4-5 = respuestas gruesas sobre el gato),
    a resolución completa; cada red los lleva a su resolución."""
    n = img.shape[0]
    I = 1 - img                                       # el gato da alto
    g = gato.astype(float)
    sob = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], float)
    diag = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]], float)
    d2x = np.array([[0, 0, 0], [1, -2, 1], [0, 0, 0]], float)
    lap = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], float)
    sx, sy, sd = conv2(I, sob), conv2(I, sob.T), conv2(I, diag)
    ax_, ay_ = _suavizar(np.abs(sx), 2), _suavizar(np.abs(sy), 2)

    def ridge_v(sig):          # barras verticales finas: patas, cola
        return np.maximum(-conv2(_suavizar(I, sig), d2x), 0)

    def ridge_h(sig):
        return np.maximum(-conv2(_suavizar(I, sig), d2x.T), 0)

    def blob(sig):             # manchas grandes: cuerpo, cabeza
        return np.maximum(-conv2(_suavizar(I, sig), lap), 0) * sig ** 2

    patas = ridge_v(3)
    E = {
        1: [np.maximum(sx, 0), np.maximum(sy, 0), np.maximum(sd, 0)],
        2: [ax_ * ay_, _suavizar(np.abs(sx) + np.abs(sy), 3),
            np.maximum(conv2(_suavizar(I, 3), sob.T), 0)],
        3: [patas, blob(9), ridge_h(4)],
        4: [_suavizar(g, 9) * (0.4 + _suavizar(patas, 6) / (patas.max() + 1e-9)
                                * 4), blob(15), _suavizar(patas, 7)],
        5: [_suavizar(g, 16), blob(22), _suavizar(patas, 14)],
    }
    return E


def _fcn_datos():
    """Imagen sintética (el gato de perfil), un canal por etapa (y dos más
    para barajar), el vector de cada celda del 7x7 y los puntajes de clase."""
    img, gato = _gato(224)
    can = _features(img, gato)
    g = gato.astype(float)
    # FCN generoso: se queda con las celdas donde el gato ocupa más de ~28%
    prob7 = np.clip(_meanpool(g, 32) * 1.8, 0, 1)
    up = np.clip(np.asarray(Image.fromarray(prob7.astype(np.float32), "F")
                            .resize((224, 224), Image.BILINEAR)), 0, 1)
    # vector de cada celda: proyección fija de las features locales
    bordes = _norm99(_meanpool(np.abs(conv2(1 - img, np.array(
        [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], float))), 32))
    loc = np.stack([c for c in can[5]] + [prob7, bordes, np.ones((7, 7))], -1)
    rng = np.random.default_rng(11)
    A = rng.normal(0, 1.4, (FCN_N_VEC, loc.shape[-1]))
    vec = 1 / (1 + np.exp(-(loc @ A.T)))                       # (7, 7, 10)
    otros = rng.uniform(0.02, 0.22, (7, 7, 21))
    scores = otros.copy()
    scores[..., 0] = 1 - prob7                                 # fondo
    scores[..., FCN_GATO] = prob7                              # gato
    return dict(img=img, gato=gato, can=can, prob7=prob7, up=up,
                mask=(up > 0.5).astype(float), vec=vec, scores=scores)


def _leyenda_mascara(ax, x, y, paso=31):
    """Leyenda de la máscara: rojo = gato, blanco = fondo, guiones = contorno."""
    lado = 19
    filas = (("gato", dict(fc=ROJO, ec=ROJO)),
             ("fondo", dict(fc="white", ec=TINTA)),
             ("contorno real", None))
    for j, (txt, estilo) in enumerate(filas):
        yc = y + j * paso
        if estilo:
            ax.add_patch(Rectangle((x, yc - lado / 2), lado, lado, lw=1.4,
                                   zorder=6, **estilo))
        else:
            ax.plot([x - 3, x + lado + 3], [yc, yc], color=TINTA, lw=1.8,
                    ls="--", zorder=6)
        ax.text(x + lado + 10, yc, txt, ha="left", va="center", fontsize=19,
                color=TINTA)


_BLANCO = np.ones(3)
_ROJO_RGB = np.array([0xD7, 0x19, 0x2A]) / 255
_TINTA_RGB = np.array([0x22, 0x22, 0x22]) / 255
_RELLENO_RGB = np.array([0xF1, 0xED, 0xEC]) / 255


def _grises(a):
    return _BLANCO + a[..., None] * 0.85 * (_TINTA_RGB - _BLANCO)


def _rojos(a):
    return _BLANCO + a[..., None] * (_ROJO_RGB - _BLANCO)


def _fcn_cara(D, i, canal=0):
    """Contenido RGB de la cara frontal del bloque i."""
    if i == 0:
        return np.repeat(D["img"][..., None], 3, 2)
    if i <= 5:
        return _grises(D["can"][i][canal])
    return _rojos({6: D["prob7"], 7: D["up"], 8: D["mask"]}[i])


def _fcn_geometria():
    """Posición x de cada bloque, con huecos iguales entre ranuras."""
    lados = [FCN_MIN + (FCN_LADO - FCN_MIN) * np.log2(r / 7) / 5
             for r, *_ in FCN_ETAPAS]
    prof = [4 + 9 * np.log2(c) if c > 1 else 4 for _, c, *_ in FCN_ETAPAS]
    dxs = [0.36 * d for d in prof]
    dys = [0.62 * d for d in prof]
    # ancho de ranura = max(bloque, etiqueta); las etiquetas se miden
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    rend = fig.canvas.get_renderer()
    ranuras = []
    for (r, c, dim, desc, *_), s, dx in zip(FCN_ETAPAS, lados, dxs):
        t1 = fig.text(0, 0, dim, fontsize=22, fontweight="bold",
                      linespacing=1.05)
        t2 = fig.text(0, 0, desc, fontsize=20, linespacing=1.15)
        wl = max(t1.get_window_extent(rend).width,
                 t2.get_window_extent(rend).width)
        ranuras.append(max(s + dx, wl))
    plt.close(fig)
    margen = 40
    hueco = (W * DPI - 2 * margen - sum(ranuras)) / (len(ranuras) - 1)
    assert hueco > 18, f"no entran las etiquetas (hueco = {hueco:.0f} px)"
    xs, x = [], margen
    for rw, s, dx in zip(ranuras, lados, dxs):
        xs.append(x + (rw - (s + dx)) / 2)       # bloque centrado en su ranura
        x += rw + hueco
    return lados, dxs, dys, xs, hueco


def _fcn_dibujar(ax, D, geo, completos, activa=None, t=0.0, pie=None,
                 canales=None, celda=None, crece=0.0, densa=False, op=None,
                 ventana=True):
    """completos: cuántos bloques están terminados. activa: índice del bloque
    que se está construyendo (t en [0,1] = fracción de celdas reveladas).
    canales: {bloque: canal visible}. celda/crece/densa: el vector de una
    celda del 7x7x512 (crece de 0 a 1 al desplegarse) y la capa densa 512->21.
    """
    lados, dxs, dys, xs, hueco = geo
    canales = canales or {}
    ax.clear()
    ax.set_xlim(0, W * DPI)
    ax.set_ylim(H * DPI, 0)
    ax.axis("off")
    yc = FCN_YC
    y_dim = yc + FCN_LADO / 2 + 48
    n_tes = FCN_TESELAS ** 2

    def caja(i):
        return xs[i], yc - lados[i] / 2, lados[i], dxs[i], dys[i]

    def prisma(i, contenido_rgb, rojo):
        x0, y0, s, dx, dy = caja(i)
        borde = ROJO if rojo else TINTA
        c_top = "#F3C7CB" if rojo else "#E6E0DE"
        c_lado = "#EBA9AF" if rojo else "#D3CBC8"
        top = [(x0, y0), (x0 + s, y0), (x0 + s + dx, y0 - dy), (x0 + dx, y0 - dy)]
        lado = [(x0 + s, y0), (x0 + s, y0 + s), (x0 + s + dx, y0 + s - dy),
                (x0 + s + dx, y0 - dy)]
        ax.add_patch(plt.Polygon(top, closed=True, fc=c_top, ec=borde, lw=1.6,
                                 zorder=2))
        ax.add_patch(plt.Polygon(lado, closed=True, fc=c_lado, ec=borde,
                                 lw=1.6, zorder=2))
        # "pila de feature maps": líneas de corte a lo largo del espesor
        c = FCN_ETAPAS[i][1]
        nl = 0 if c < 3 else min(9, int(np.log2(c)))
        for j in range(1, nl):
            f = j / nl
            ax.plot([x0 + f * dx, x0 + s + f * dx], [y0 - f * dy, y0 - f * dy],
                    color=borde if rojo else SLICE, lw=0.9, zorder=3,
                    alpha=0.6 if rojo else 1)
            ax.plot([x0 + s + f * dx, x0 + s + f * dx],
                    [y0 - f * dy, y0 + s - f * dy],
                    color=borde if rojo else SLICE, lw=0.9, zorder=3,
                    alpha=0.6 if rojo else 1)
        ax.imshow(contenido_rgb, extent=(x0, x0 + s, y0 + s, y0),
                  interpolation="nearest", zorder=4)
        ax.add_patch(Rectangle((x0, y0), s, s, fill=False, ec=borde,
                               lw=3 if rojo else 1.8, zorder=5))

    def etiqueta(i):
        x0, y0, s, dx, dy = caja(i)
        cx = x0 + (s + dx) / 2
        rojo = i == 6
        ax.text(cx, y_dim, FCN_ETAPAS[i][2], ha="center", va="top",
                fontsize=22, fontweight="bold", color=ROJO if rojo else TINTA,
                linespacing=1.05)
        ax.text(cx, y_dim + 80, FCN_ETAPAS[i][3], ha="center", va="top",
                fontsize=20, color=ROJO if rojo else GRIS_MEDIO,
                linespacing=1.15)
        cara = FCN_ETAPAS[i][5]
        if cara:     # qué canal muestra la cara
            ax.text(x0 + s / 2, y0 + s + 7, cara, ha="center", va="top",
                    fontsize=18, color=ROJO if rojo else GRIS_MEDIO,
                    style="italic", linespacing=1.0)
        if i == 7:   # qué muestra la cara de este bloque, arriba del prisma
            ax.text(cx, y0 - dy - 12, "canal de la clase gato",
                    ha="center", va="bottom", fontsize=19, color=ROJO)
        if i == 8:
            _leyenda_mascara(ax, min(cx - 72, W * DPI - 260), y_dim + 232)

    def flecha(i, color, lw):
        xa = xs[i - 1] + lados[i - 1] + dxs[i - 1] + 5
        xb = xs[i] - 5
        ax.annotate("", xy=(xb, yc), xytext=(xa, yc), zorder=6,
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                    mutation_scale=22 if lw > 2 else 18,
                                    shrinkA=0, shrinkB=0))

    def flechita(p0, p1):
        ax.annotate("", xy=p1, xytext=p0, zorder=8,
                    arrowprops=dict(arrowstyle="-|>", color=TINTA, lw=1.6,
                                    mutation_scale=16, shrinkA=0, shrinkB=0))

    def vector(cel, crece, densa):
        """Columna del 7x7x512 -> vector de 512 -> capa densa -> 21 puntajes."""
        r, c = cel
        x5, y5, s5, dx5, dy5 = caja(5)
        cs = s5 / 7
        fx, fy = x5 + c * cs, y5 + r * cs
        k = min(1.0, crece * 2)          # primero crece el tubo en profundidad
        bx, by = fx + k * dx5, fy - k * dy5
        ax.add_patch(Rectangle((fx, fy), cs, cs, fc=ROJO, alpha=0.55,
                               ec=ROJO, lw=2.5, zorder=8))
        for ox, oy in ((0, 0), (cs, 0), (cs, cs), (0, cs)):
            ax.plot([fx + ox, bx + ox], [fy + oy, by + oy], color=ROJO, lw=1.8,
                    zorder=8)
        ax.add_patch(Rectangle((bx, by), cs, cs, fill=False, ec=ROJO, lw=1.8,
                               zorder=8))
        if crece <= 0.5:
            return
        # el vector, desplegado arriba del bloque
        xv = x5 - 22                     # arriba, entre el 14x14 y el 7x7
        alto, y_top, ancho = 15, 34, 18
        y_bot = y_top + FCN_N_VEC * alto
        n_vis = int(round(FCN_N_VEC * min(1.0, (crece - 0.5) * 2)))
        ax.plot([bx + cs / 2, xv], [by, y_bot + 3], color=ROJO, lw=1.8,
                ls="--", zorder=8)
        valores = D["vec"][r, c]
        for j in range(FCN_N_VEC):
            yj = y_bot - (j + 1) * alto          # se llena de abajo hacia arriba
            if j >= n_vis:
                continue
            if j == 4:                            # "..." en el medio: son 512
                ax.text(xv, yj + alto / 2, "⋮", ha="center", va="center",
                        fontsize=18, color=ROJO, zorder=9)
                continue
            ax.add_patch(Rectangle((xv - ancho / 2, yj), ancho, alto,
                                   fc=_grises(np.array([valores[j]]))[0],
                                   ec=ROJO, lw=1.3, zorder=9))
        if n_vis >= FCN_N_VEC:
            ax.text(xv - ancho / 2 - 12, (y_top + y_bot) / 2,
                    "vector de 512 =\nembedding de\nesa región", ha="right",
                    va="center", fontsize=19, color=ROJO, linespacing=1.15)
        if not densa:
            return
        bx0, bw, by0, bh = xv + ancho / 2 + 26, 150, 70, 80
        ax.add_patch(Rectangle((bx0, by0), bw, bh, fc="white", ec=TINTA,
                               lw=1.8, zorder=9))
        ax.text(bx0 + bw / 2, by0 + bh / 2, "la misma\ncapa densa\n512 → 21",
                ha="center", va="center", fontsize=18, color=TINTA,
                linespacing=1.1, zorder=10)
        flechita((xv + ancho / 2 + 3, by0 + bh / 2), (bx0 - 2, by0 + bh / 2))
        xs_ = bx0 + bw + 22
        hs, ws = 7, 16
        flechita((bx0 + bw + 2, by0 + bh / 2), (xs_ - 3, by0 + bh / 2))
        sc = D["scores"][r, c]
        for j in range(21):
            col = (_rojos(np.array([sc[j]]))[0] if j == FCN_GATO
                   else _grises(np.array([sc[j]]))[0])
            ax.add_patch(Rectangle((xs_, y_top + j * hs), ws, hs, fc=col,
                                   ec=ROJO if j == FCN_GATO else GRIS_MEDIO,
                                   lw=0.8, zorder=9))
        ax.text(xs_ + ws + 8, y_top - 2, "21 puntajes", ha="left", va="top",
                fontsize=18, color=TINTA, zorder=9)
        ax.text(xs_ + ws + 8, y_top + (FCN_GATO + 0.5) * hs, "← gato",
                ha="left", va="center", fontsize=18, color=ROJO, zorder=9)
        # y va a parar a la misma celda del 7x7x21
        x6, y6, s6, _, _ = caja(6)
        c6 = s6 / 7
        ax.plot([xs_ + ws / 2, x6 + (c + 0.5) * c6],
                [y_top + 21 * hs + 3, y6 + r * c6], color=ROJO, lw=1.8,
                ls="--", zorder=8)
        ax.add_patch(Rectangle((x6 + c * c6, y6 + r * c6), c6, c6, fill=False,
                               ec=ROJO, lw=2.5, zorder=8))

    hasta = completos if activa is None else activa
    for i in range(hasta):
        prisma(i, _fcn_cara(D, i, canales.get(i, 0)), i == 6)
        etiqueta(i)
        if i == 8:   # contorno real del gato sobre la máscara: se ve el error
            x0, y0, s, _, _ = caja(8)
            ax.contour(np.linspace(x0, x0 + s, 224), np.linspace(y0, y0 + s, 224),
                       D["gato"].astype(float), levels=[0.5], colors=[TINTA],
                       linewidths=1.6, linestyles="--", zorder=6)
        if i >= 1:
            flecha(i, GRIS_MEDIO, 1.8)

    cel_activa = celda
    if activa is not None:
        i = activa
        res = FCN_ETAPAS[i][0]
        k = res // FCN_TESELAS
        revel = int(round(n_tes * t))
        rgb = _fcn_cara(D, i, canales.get(i, 0)).copy()
        oculto = np.ones((res, res), bool)
        for q in range(revel):
            a, b = divmod(q, FCN_TESELAS)
            oculto[a * k:(a + 1) * k, b * k:(b + 1) * k] = False
        rgb[oculto] = _RELLENO_RGB
        prisma(i, rgb, i == 6)
        flecha(i, ROJO, 3.2)
        q = max(revel - 1, 0)
        a, b = divmod(q, FCN_TESELAS)
        if i == 6:
            cel_activa = (a, b)          # la capa densa recorre las celdas
        elif ventana:
            # ventana (kernel) sobre la cara frontal del bloque de origen
            x0, y0, s0, _, _ = caja(i - 1)
            c = s0 / FCN_TESELAS
            ax.add_patch(Rectangle((x0 + b * c, y0 + a * c), c, c, fc=ROJO,
                                   alpha=0.25, ec="none", zorder=7))
            ax.add_patch(Rectangle((x0 + b * c, y0 + a * c), c, c, fill=False,
                                   ec=ROJO, lw=3, zorder=7))
        # y la tesela que se está escribiendo en el destino
        x1, y1, s1, _, _ = caja(i)
        c1 = s1 / FCN_TESELAS
        if revel > 0:
            ax.add_patch(Rectangle((x1 + b * c1, y1 + a * c1), c1, c1,
                                   fill=False, ec=ROJO, lw=2.5, zorder=7))
        if t >= 1:
            etiqueta(i)
    if cel_activa is not None:
        vector(cel_activa, crece, densa)
    if op:
        ax.text(45, 24, op, ha="left", va="top", fontsize=26, color=ROJO,
                fontweight="bold")

    # llave del encoder, cuando ya están las 5 etapas conv+pool
    if hasta >= 6:
        xa = xs[1]
        xb = xs[5] + lados[5] + dxs[5]
        yb = y_dim + 158
        ax.plot([xa, xa, xb, xb], [yb, yb + 14, yb + 14, yb], color=TINTA,
                lw=1.8)
        xm = (xa + xb) / 2
        ax.plot([xm, xm], [yb + 14, yb + 26], color=TINTA, lw=1.8)
        ax.text(xm, yb + 34, "encoder: la resolución baja ×2 por etapa,\n"
                "los canales suben", ha="center", va="top", fontsize=21,
                color=TINTA, linespacing=1.2)
    if pie:
        ax.text(W * DPI / 2, H * DPI - 44, pie, ha="center", va="center",
                fontsize=22, color=TINTA)


def _fcn_figura():
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    return fig, ax


def fcn_dimensiones():
    assert 224 // 2 ** 5 == 7 and 7 * 32 == 224
    D = _fcn_datos()
    geo = _fcn_geometria()
    fig, ax = _fcn_figura()
    _fcn_dibujar(ax, D, geo, completos=9, celda=FCN_CELDA, crece=1.0,
                 densa=True)
    ruta = os.path.join(OUT, "fcn-dimensiones.png")
    fig.savefig(ruta, dpi=DPI, facecolor="white")
    plt.close(fig)
    print(f"{ruta}  {os.path.getsize(ruta) / 1e6:.2f} MB")


def _fcn_cuadros(D, geo, fig, ax, por_etapa=10):
    """Genera (nombre, cuadro) del ciclo completo de fcn-en-vivo."""
    def foto(**kw):
        _fcn_dibujar(ax, D, geo, **kw)
        return capturar(fig)

    yield "inicio", [foto(completos=1, pie=FCN_PIES[0])] * 5
    for i in range(1, 6):
        op = FCN_ETAPAS[i][4]
        for f in range(1, por_etapa + 1):
            yield f"e{i}", [foto(completos=i, activa=i, t=f / por_etapa,
                                 pie=FCN_PIES[i], op=op)]
        # barajar: la cara es UNO de muchos canales
        for k in (1, 2):
            yield f"e{i}-canal{k}", [foto(completos=i + 1, pie=FCN_PIES[i],
                                          canales={i: k}, op=op)] * 2
    yield "rf", [foto(completos=6, pie=FCN_PIES["rf"])] * 8
    for f in range(1, 9):
        yield "emb", [foto(completos=6, pie=FCN_PIES["emb"], celda=FCN_CELDA,
                           crece=f / 8)]
    yield "emb-quieto", [foto(completos=6, pie=FCN_PIES["emb"],
                              celda=FCN_CELDA, crece=1.0)] * 6
    n6 = 14
    for f in range(1, n6 + 1):
        yield "c1x1", [foto(completos=6, activa=6, t=f / n6, pie=FCN_PIES[6],
                            crece=1.0, densa=True, op="conv 1×1")]
    yield "c1x1-quieto", [foto(completos=7, pie=FCN_PIES[6], celda=FCN_CELDA,
                               crece=1.0, densa=True, op="conv 1×1")] * 3
    for i in (7, 8):
        for f in range(1, por_etapa + 1):
            yield f"e{i}", [foto(completos=i, activa=i, t=f / por_etapa,
                                 pie=FCN_PIES[i], celda=FCN_CELDA, crece=1.0,
                                 densa=True, op=FCN_ETAPAS[i][4])]
        yield f"e{i}-quieto", [foto(completos=i + 1, pie=FCN_PIES[i],
                                    celda=FCN_CELDA, crece=1.0, densa=True,
                                    op=FCN_ETAPAS[i][4])] * 3
    yield "final", [foto(completos=9, celda=FCN_CELDA, crece=1.0, densa=True)]


def fcn_en_vivo(fps=12, pausa_s=3.0):
    D = _fcn_datos()
    geo = _fcn_geometria()
    fig, ax = _fcn_figura()
    frames = []
    for _, fs in _fcn_cuadros(D, geo, fig, ax):
        frames += fs
    plt.close(fig)
    guardar_gif(frames, os.path.join(OUT, "fcn-en-vivo.gif"), fps=fps,
                pausa_s=pausa_s, colores=64)
    return frames


# =========================================================================
# 8-9. U-Net por dentro: unet-dimensiones.png y unet-en-vivo.gif
# =========================================================================
# U-Net con padding (variante usual), entrada 256x256x1. Mismo estilo y misma
# imagen sintética que FCN. Lado de la cara: escala log comprimida en la
# resolución; espesor: log2(canales). La U es espejo exacto alrededor de un eje
# vertical que pasa por el bottleneck. Los bloques de concatenación muestran el
# espesor partido: adelante en rojo lo copiado por el skip, atrás en gris lo
# subido desde abajo.
UN_FILAS = {0: 150, 1: 332, 2: 476, 3: 615, 4: 745}
UN_TES = 4                                  # teselas por lado al construir
GRIS_TOP, GRIS_LADO = "#E6E0DE", "#D3CBC8"
ROJO_TOP, ROJO_LADO = "#F3C7CB", "#EBA9AF"


def _un_lado(r):
    return 46 + 40 * np.log2(r / 16) / 4         # 16 -> 46 px, 256 -> 86 px


def _un_prof(c):
    return 4 if c < 2 else 4 + 6 * np.log2(c)


def _gato(n):
    """Gato de perfil caminando hacia la izquierda: cuerpo horizontal, cuatro
    patas, orejas grandes, hocico y cola larga curvada hacia arriba. Sirve a FCN
    y a U-Net; se lee como animal aunque esté muy pixelado."""
    yy, xx = (np.mgrid[0:n, 0:n] + 0.5) / n

    def elipse(cx, cy, rx, ry, ang=0.0):
        c, s_ = np.cos(ang), np.sin(ang)
        u = (xx - cx) * c + (yy - cy) * s_
        v = -(xx - cx) * s_ + (yy - cy) * c
        return (u / rx) ** 2 + (v / ry) ** 2 < 1

    def tri(p1, p2, p3):
        d = lambda a, b: (xx - b[0]) * (a[1] - b[1]) - (a[0] - b[0]) * (yy - b[1])
        s1, s2, s3 = d(p1, p2), d(p2, p3), d(p3, p1)
        return ~(((s1 < 0) | (s2 < 0) | (s3 < 0)) & ((s1 > 0) | (s2 > 0) | (s3 > 0)))

    def trazo(puntos, grosor):
        """Banda de ancho 2*grosor alrededor de una poligonal."""
        dmin = np.full(xx.shape, np.inf)
        for (x1, y1), (x2, y2) in zip(puntos[:-1], puntos[1:]):
            vx, vy = x2 - x1, y2 - y1
            t = np.clip(((xx - x1) * vx + (yy - y1) * vy) / (vx * vx + vy * vy),
                        0, 1)
            dmin = np.minimum(dmin, np.hypot(xx - x1 - t * vx, yy - y1 - t * vy))
        return dmin < grosor

    cuerpo = elipse(0.53, 0.56, 0.27, 0.115)            # largo y bajo
    pecho = elipse(0.30, 0.52, 0.09, 0.10)
    cuello = elipse(0.25, 0.45, 0.075, 0.085, ang=-0.5)
    cabeza = elipse(0.19, 0.36, 0.095, 0.090)           # redonda
    nariz = elipse(0.105, 0.385, 0.022, 0.026)          # hocico casi plano
    orejas = (tri((0.115, 0.33), (0.13, 0.17), (0.20, 0.285))   # grandes,
              | tri((0.175, 0.28), (0.24, 0.155), (0.265, 0.31)))  # juntas
    patas = np.zeros_like(cuerpo)
    # cortas y gruesas, con un leve paso de caminata
    for x_top, x_pie in ((0.31, 0.29), (0.39, 0.41), (0.66, 0.64), (0.74, 0.77)):
        patas |= trazo([(x_top, 0.60), (x_pie, 0.80)], 0.032)
        patas |= elipse(x_pie - 0.012, 0.805, 0.040, 0.022)      # pata
    # cola larga y gruesa en signo de pregunta
    cola = trazo([(0.77, 0.53), (0.84, 0.47), (0.885, 0.38), (0.895, 0.28),
                  (0.875, 0.20), (0.83, 0.165), (0.785, 0.185), (0.775, 0.22)],
                 0.030)
    gato = cuerpo | pecho | cuello | cabeza | nariz | orejas | patas | cola
    bigotes = trazo([(0.115, 0.40), (0.015, 0.365)], 0.0045) | \
        trazo([(0.115, 0.405), (0.012, 0.41)], 0.0045) | \
        trazo([(0.115, 0.41), (0.02, 0.455)], 0.0045)
    img = 0.86 - 0.14 * yy + 0.05 * xx
    img[gato] = 0.22 + 0.10 * yy[gato]
    img[bigotes & ~gato] = 0.35                     # solo en la imagen
    ojo = elipse(0.165, 0.345, 0.014, 0.017)
    img[ojo] = 0.80
    img = conv2(conv2(img, np.ones((3, 3)) / 9), np.ones((3, 3)) / 9)
    return img, gato


UN_CELDA = (8, 8)          # celda del bottleneck que se despliega (sobre el gato)


def _un_datos():
    """Un canal de features por bloque, con el mismo gato que FCN. En el
    decoder, lo subido sale borroso y lo copiado por el skip es exactamente el
    mapa fino del encoder."""
    img, gato = _gato(256)
    E = _features_crudos(img, gato)
    g = gato.astype(float)

    def subir(a, r):
        return np.clip(np.asarray(Image.fromarray(a.astype(np.float32), "F")
                                  .resize((r, r), Image.BILINEAR)), 0, 1)

    m = {"in": np.repeat(img[..., None], 3, 2)}
    for clave, k, f in (("e0", 1, 1), ("e1", 2, 2), ("e2", 3, 4), ("e3", 4, 8),
                        ("b", 5, 16)):
        for j, mapa in enumerate(E[k]):
            mm = _norm99(_maxpool(mapa, f) if f > 1 else mapa)
            m[clave if j == 0 else f"{clave}#{j}"] = _grises(mm)
    for e, a in (("e0", "a0"), ("e1", "a1"), ("e2", "a2"), ("e3", "a3"),
                 ("b", "b1")):
        m[a] = m[f"{e}#1"]                       # la primera conv del nivel
    prob = _meanpool(g, 16)                      # lo que "sabe" el bottleneck
    for nivel, r in ((3, 32), (2, 64), (1, 128), (0, 256)):
        up = subir(prob, r)
        m[f"u{nivel}"] = _grises(up)             # lo subido: borroso
        m[f"c{nivel}"] = m[f"e{nivel}"]          # lo copiado: el mapa fino
        prob = np.clip(0.3 * up + 0.7 * _meanpool(g, 256 // r), 0, 1)
        prob = np.clip((prob - 0.5) * 1.4 + 0.5, 0, 1)
        m[f"o{nivel}"] = _grises(prob)
    m["k"] = _rojos(prob)
    m["m"] = _rojos((prob > 0.5).astype(float))
    # vector de cada celda del bottleneck: proyección fija de features locales
    loc = np.stack([_norm99(_maxpool(x, 16)) for x in E[5]]
                   + [_meanpool(g, 16), np.ones((16, 16))], -1)
    A = np.random.default_rng(5).normal(0, 1.4, (FCN_N_VEC, loc.shape[-1]))
    m["vec"] = 1 / (1 + np.exp(-(loc @ A.T)))
    return m, gato


# Cada nivel es un par de prismas pegados a cada lado del eje: en el encoder
# las dos conv 3x3 (a, e); en el decoder la concatenación y la conv (c, o).
# (clave, resolución, canales, fila)
UN_BLOQUES = [
    ("in", 256, 1, 0), ("a0", 256, 64, 0), ("e0", 256, 64, 0),
    ("a1", 128, 128, 1), ("e1", 128, 128, 1),
    ("a2", 64, 256, 2), ("e2", 64, 256, 2),
    ("a3", 32, 512, 3), ("e3", 32, 512, 3),
    ("b1", 16, 1024, 4), ("b", 16, 1024, 4),
    ("c3", 32, 1024, 3), ("o3", 32, 512, 3),
    ("c2", 64, 512, 2), ("o2", 64, 256, 2),
    ("c1", 128, 256, 1), ("o1", 128, 128, 1),
    ("c0", 256, 128, 0), ("o0", 256, 64, 0),
    ("m", 256, 1, 0),
]
UN_SKIPS = [("e0", "c0"), ("e1", "c1"), ("e2", "c2"), ("e3", "c3")]
UN_FLECHAS = [  # (origen, destino, tipo) en el orden en que se construyen
    ("in", "a0", "h"), ("a0", "e0", "par"), ("e0", "a1", "baja"),
    ("a1", "e1", "par"), ("e1", "a2", "baja"), ("a2", "e2", "par"),
    ("e2", "a3", "baja"), ("a3", "e3", "par"), ("e3", "b1", "al_fondo"),
    ("b1", "b", "par"), ("b", "c3", "del_fondo"), ("c3", "o3", "par"),
    ("o3", "c2", "sube"), ("c2", "o2", "par"), ("o2", "c1", "sube"),
    ("c1", "o1", "par"), ("o1", "c0", "sube"), ("c0", "o0", "par"),
    ("o0", "m", "h"),
]
# etiqueta de cada nivel: (dims, segundo renglón, rótulo de cara)
UN_ROTULOS = {
    "in": ("256×256\n×1", "imagen", None),
    "a0": ("256×256\n×64", None, "1 de 64"),
    "a1": ("128×128×128", None, "1 de 128"),
    "a2": ("64×64×256", None, "1 de 256"),
    "a3": ("32×32×512", None, "1 de 512"),
    "b1": ("16×16×1024", "bottleneck", "1 de 1024"),
    "o3": ("32×32×512", "concat: ×1024", "1 de 512"),
    "o2": ("64×64×256", "concat: ×512", "1 de 256"),
    "o1": ("128×128×128", "concat: ×256", "1 de 128"),
    "o0": ("256×256\n×64", None, "1 de 64"),       # espejo de a0
    "m": ("256×256", "máscara", None),
    "m:k": ("256×256\n×C clases", None, "canal gato"),
}
UN_EJE = 800                      # eje vertical de la U (centro del lienzo)
UN_D = {0: 430, 1: 343, 2: 256, 3: 170}    # distancia de cada nivel al eje
UN_PAR, UN_PUNTA = 6, 128         # entre prismas de un nivel; imagen/máscara-U


def _un_geometria():
    G = {}
    for clave, r, c, fila in UN_BLOQUES:
        s, d = _un_lado(r), _un_prof(c)
        G[clave] = dict(s=s, dx=0.5 * d, dy=0.3 * d, y=UN_FILAS[fila], x=0.0)

    def w(k):
        return G[k]["s"] + G[k]["dx"]

    A = UN_EJE
    for n in range(4):
        a, e, c, o = f"a{n}", f"e{n}", f"c{n}", f"o{n}"
        x0 = A - UN_D[n] - (w(a) + UN_PAR + w(e)) / 2       # espejo exacto:
        G[a]["x"], G[e]["x"] = x0, x0 + w(a) + UN_PAR       # mismo centro a
        x0 = A + UN_D[n] - (w(c) + UN_PAR + w(o)) / 2       # cada lado del eje
        G[c]["x"], G[o]["x"] = x0, x0 + w(c) + UN_PAR
    x0 = A - (w("b1") + UN_PAR + w("b")) / 2
    G["b1"]["x"], G["b"]["x"] = x0, x0 + w("b1") + UN_PAR
    # imagen y máscara: simétricas en las dos puntas de arriba
    G["m"]["x"] = G["o0"]["x"] + w("o0") + UN_PUNTA
    G["in"]["x"] = 2 * A - (G["m"]["x"] + w("m"))
    assert G["in"]["x"] >= 40 and G["m"]["x"] + w("m") <= W * DPI - 40, \
        (G["in"]["x"], G["m"]["x"] + w("m"))
    # las flechas entre niveles son verticales: tienen que caer en el bloque
    for a, b in (("e0", "a1"), ("e1", "a2"), ("e2", "a3")):
        cx = G[a]["x"] + G[a]["s"] / 2
        assert G[b]["x"] + 6 < cx < G[b]["x"] + G[b]["s"] - 6, (a, b)
    for a, b in (("o3", "c2"), ("o2", "c1"), ("o1", "c0")):
        cx = G[a]["x"] + G[a]["s"] / 2
        assert G[b]["x"] + 6 < cx < G[b]["x"] + G[b]["s"] - 6, (a, b)
    return G


def _leyenda_horizontal(ax, x_der, y):
    """gato / fondo / contorno real en un renglón, alineado a la derecha."""
    items = (("gato", "rojo"), ("fondo", "blanco"), ("contorno real", "guion"))
    anchos = (108, 120, 190)
    x = x_der - sum(anchos)
    for (txt, tipo), an in zip(items, anchos):
        if tipo == "guion":
            ax.plot([x, x + 22], [y, y], color=TINTA, lw=1.8, ls="--")
        else:
            ax.add_patch(Rectangle((x + 1, y - 9), 18, 18, lw=1.4,
                                   fc=ROJO if tipo == "rojo" else "white",
                                   ec=ROJO if tipo == "rojo" else TINTA))
        ax.text(x + 30, y, txt, ha="left", va="center", fontsize=19,
                color=TINTA)
        x += an


def _un_dibujar(ax, m, gato, G, hechos, activa=None, t=0.0, estado=None,
                pie=None, op=None, canales=None, crece=0.0):
    """hechos: claves de bloques terminados. estado: {'c3': 'sube'} cuando el
    bloque de concatenación solo tiene la parte subida (todavía sin skip), y
    {'m': 'k'} cuando la punta muestra la salida de la conv 1x1 (antes del
    argmax). canales: {bloque: canal visible}. crece: despliegue (0 a 1) del
    vector de una celda del bottleneck."""
    estado = estado or {}
    canales = canales or {}
    ax.clear()
    ax.set_xlim(0, W * DPI)
    ax.set_ylim(H * DPI, 0)
    ax.axis("off")
    info = {b[0]: b for b in UN_BLOQUES}

    def cara_rgb(k):
        if k == "m":
            return m["k"] if estado.get("m") == "k" else m["m"]
        j = canales.get(k)
        return m[f"{k}#{j}"] if j else m[k]

    def caja(k):
        g = G[k]
        return g["x"], g["y"] - g["s"] / 2, g["s"], g["dx"], g["dy"]

    def prisma(k, rgb, mitad=None):
        x0, y0, s, dx, dy = caja(k)
        es_concat = k.startswith("c") and mitad != "sube"
        tramos = [(0, 1, GRIS_TOP, GRIS_LADO)]
        if es_concat:
            tramos = [(0, 0.5, ROJO_TOP, ROJO_LADO), (0.5, 1, GRIS_TOP, GRIS_LADO)]
        elif mitad == "sube":
            tramos = [(0.5, 1, GRIS_TOP, GRIS_LADO)]
        for f0, f1, ct, cl in tramos[::-1]:
            ax0, ay0 = f0 * dx, f0 * dy
            ax1, ay1 = f1 * dx, f1 * dy
            top = [(x0 + ax0, y0 - ay0), (x0 + s + ax0, y0 - ay0),
                   (x0 + s + ax1, y0 - ay1), (x0 + ax1, y0 - ay1)]
            lado = [(x0 + s + ax0, y0 - ay0), (x0 + s + ax0, y0 + s - ay0),
                    (x0 + s + ax1, y0 + s - ay1), (x0 + s + ax1, y0 - ay1)]
            ec = ROJO if ct == ROJO_TOP else TINTA
            ax.add_patch(plt.Polygon(top, closed=True, fc=ct, ec=ec, lw=1.4,
                                     zorder=2))
            ax.add_patch(plt.Polygon(lado, closed=True, fc=cl, ec=ec, lw=1.4,
                                     zorder=2))
        c = info[k][2]
        nl = 0 if c < 3 else min(9, int(np.log2(c)))
        f_ini = 0.5 if mitad == "sube" else 0
        for j in range(1, nl):
            f = j / nl
            if f <= f_ini:
                continue
            col = ROJO if (es_concat and f < 0.5) else SLICE
            ax.plot([x0 + f * dx, x0 + s + f * dx], [y0 - f * dy, y0 - f * dy],
                    color=col, lw=0.8, zorder=3, alpha=0.7)
            ax.plot([x0 + s + f * dx] * 2, [y0 - f * dy, y0 + s - f * dy],
                    color=col, lw=0.8, zorder=3, alpha=0.7)
        if mitad == "sube":   # la cara visible está atrás: a mitad del espesor
            x0, y0 = x0 + 0.5 * dx, y0 - 0.5 * dy
        # si la cara tiene menos píxeles que el mapa, se filtra (si no, los
        # bordes finos desaparecen al achicar)
        ax.imshow(rgb, extent=(x0, x0 + s, y0 + s, y0), zorder=4,
                  interpolation="nearest" if info[k][1] <= s else "antialiased")
        ax.add_patch(Rectangle((x0, y0), s, s, fill=False,
                               ec=ROJO if es_concat else TINTA, lw=1.8, zorder=5))

    def etiqueta(k):
        clave = "m:k" if (k == "m" and estado.get("m") == "k") else k
        if clave not in UN_ROTULOS:
            return
        dims, seg, cara = UN_ROTULOS[clave]
        x0, y0, s, dx, dy = caja(k)
        renglones = [(dims, dict(fontsize=20, fontweight="bold", color=TINTA))]
        if seg:
            renglones.append((seg, dict(fontsize=19, color=TINTA if k == "b1"
                                        else GRIS_MEDIO)))
        if cara:
            renglones.append((cara, dict(fontsize=18, style="italic",
                                         color=ROJO if clave == "m:k"
                                         else GRIS_MEDIO)))
        alto = 26
        n_lin = sum(t_.count("\n") + 1 for t_, _ in renglones)
        fila = info[k][3]
        if fila == 0:                    # fila de arriba: debajo del bloque
            xc, ha, y = x0 + s / 2, "center", y0 + s + 8
        else:                            # a los costados, del lado de afuera
            y = y0 + s / 2 - alto * n_lin / 2
            xc, ha = ((x0 - 14, "right") if k.startswith(("a", "b"))
                      else (x0 + s + dx + 14, "left"))
        for texto, estilo in renglones:
            nl = texto.count("\n") + 1
            ax.text(xc, y, texto, ha=ha, va="top", linespacing=0.95,
                    **estilo)
            y += alto * nl

    def flecha(a, b, tipo, color, lw):
        if tipo == "par":
            return
        xa, ya, sa, dxa, dya = caja(a)
        xb, yb, sb, dxb, dyb = caja(b)
        if tipo == "h":
            p0, p1 = (xa + sa + dxa + 6, ya + sa / 2), (xb - 6, yb + sb / 2)
        elif tipo == "baja":            # vertical, del piso al techo
            cxa = xa + sa / 2
            p0, p1 = (cxa, ya + sa + 4), (cxa, yb - dyb - 4)
        elif tipo == "sube":
            cxa = xa + sa / 2
            p0, p1 = (cxa, ya - dya - 4), (cxa, yb + sb + 4)
        elif tipo == "al_fondo":        # diagonal hacia el bottleneck
            p0, p1 = (xa + sa / 2, ya + sa + 4), (xb + sb * 0.3, yb - dyb - 4)
        else:                           # del_fondo: espejo de la anterior
            p0, p1 = (xa + sa * 0.7, ya - dya - 4), (xb + sb / 2, yb + sb + 4)
        ax.annotate("", xy=p1, xytext=p0, zorder=6,
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                    mutation_scale=20, shrinkA=0, shrinkB=0))
        if b == "m":                    # arriba de la flecha y de los bloques
            ax.text((p0[0] + p1[0]) / 2, yb - dyb - 8, "conv 1×1\n+ argmax",
                    ha="center", va="bottom", fontsize=18, color=GRIS_MEDIO,
                    linespacing=1.05, zorder=10)

    def skip(a, b, color, lw, con_texto=True):
        xa, ya, sa, dxa, _ = caja(a)
        xb, yb, sb, _, _ = caja(b)
        x1, x2, y = xa + sa + dxa + 6, xb - 6, ya + sa / 2
        ax.annotate("", xy=(x2, y), xytext=(x1, y), zorder=6,
                    arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                    mutation_scale=24, shrinkA=0, shrinkB=0))
        if con_texto:
            txt = "skip: copiar y concatenar"
            if x2 - x1 < 200:
                txt = "skip:\ncopiar y\nconcatenar"
            elif x2 - x1 < 340:
                txt = "skip: copiar\ny concatenar"
            ax.text((x1 + x2) / 2, y - 8, txt, ha="center", va="bottom",
                    fontsize=19, color=ROJO, linespacing=1.05,
                    fontweight="bold" if lw > 3 and txt.count("\n") < 2
                    else "normal")

    def vector_b(crece):
        """Celda del bottleneck -> tubo en profundidad -> vector de 1024."""
        r, c = UN_CELDA
        x0, y0, s, dx, dy = caja("b")
        cs = s / 16
        fx, fy = x0 + c * cs, y0 + r * cs
        k_ = min(1.0, crece * 2)
        bx, by = fx + k_ * dx, fy - k_ * dy
        ax.add_patch(Rectangle((fx - 1, fy - 1), cs + 2, cs + 2, fc=ROJO,
                               ec=ROJO, lw=2, zorder=8))
        for ox, oy in ((0, 0), (cs, 0), (cs, cs), (0, cs)):
            ax.plot([fx + ox, bx + ox], [fy + oy, by + oy], color=ROJO, lw=1.6,
                    zorder=8)
        if crece <= 0.5:
            return
        alto, ancho = 11, 16
        xv = x0 + s + dx + 58
        y_top = G["b"]["y"] - FCN_N_VEC * alto / 2
        y_bot = y_top + FCN_N_VEC * alto
        n_vis = int(round(FCN_N_VEC * min(1.0, (crece - 0.5) * 2)))
        ax.plot([bx + cs / 2, xv - ancho / 2 - 2], [by + cs / 2, y_bot - 20],
                color=ROJO, lw=1.6, ls="--", zorder=8)
        valores = m["vec"][r, c]
        for j in range(FCN_N_VEC):
            if j >= n_vis:
                continue
            yj = y_bot - (j + 1) * alto
            if j == 4:
                ax.text(xv, yj + alto / 2, "⋮", ha="center", va="center",
                        fontsize=16, color=ROJO, zorder=9)
                continue
            ax.add_patch(Rectangle((xv - ancho / 2, yj), ancho, alto,
                                   fc=_grises(np.array([valores[j]]))[0],
                                   ec=ROJO, lw=1.2, zorder=9))
        if n_vis >= FCN_N_VEC:
            ax.text(xv + ancho / 2 + 12, (y_top + y_bot) / 2,
                    "vector de 1024 =\nembedding de\nesa región", ha="left",
                    va="center", fontsize=19, color=ROJO, linespacing=1.15)

    # flechas ya recorridas
    vivos = set(hechos) | ({activa} if activa else set())
    for a, b, tipo in UN_FLECHAS:
        if a in hechos and b in vivos:
            roja = b == activa and op not in ("concatenar", "argmax")
            flecha(a, b, tipo, ROJO if roja else GRIS_MEDIO, 3 if roja else 1.8)
    for a, b in UN_SKIPS:
        if b == activa and op == "concatenar":
            skip(a, b, ROJO, 4.5)
        elif b in hechos and estado.get(b) != "sube":
            skip(a, b, ROJO, 2.4)

    # bloques
    for k in [b[0] for b in UN_BLOQUES]:
        if k in hechos and k != activa:
            if estado.get(k) == "sube":       # sin skip todavía: sin etiqueta
                prisma(k, m["u" + k[1]], "sube")
                continue
            prisma(k, cara_rgb(k))
            etiqueta(k)
            if k == "m" and estado.get("m") != "k":
                x0, y0, s, _, _ = caja("m")
                ax.contour(np.linspace(x0, x0 + s, 256),
                           np.linspace(y0, y0 + s, 256), gato.astype(float),
                           levels=[0.5], colors=[TINTA], linewidths=1.4,
                           linestyles="--", zorder=6)
    if activa:
        k = activa
        res = info[k][1]
        if op == "up-conv 2×2":
            dest, base, mitad = m["u" + k[1]], None, "sube"
        elif op == "concatenar":
            dest, base, mitad = m[k], m["u" + k[1]], None
        elif op == "conv 1×1":
            dest, base, mitad = m["k"], None, None
        elif op == "argmax":
            dest, base, mitad = m["m"], m["k"], None
        else:
            dest, base, mitad = cara_rgb(k), None, None
        rgb = dest.copy()
        q = int(round(UN_TES ** 2 * t))
        lado_t = res // UN_TES
        oculto = np.ones((res, res), bool)
        for i in range(q):
            a, b = divmod(i, UN_TES)
            oculto[a * lado_t:(a + 1) * lado_t, b * lado_t:(b + 1) * lado_t] = False
        rgb[oculto] = (base[oculto] if base is not None else _RELLENO_RGB)
        prisma(k, rgb, mitad)
        if t >= 1 and op != "up-conv 2×2":
            if k == "m":
                estado = dict(estado, m="k" if op == "conv 1×1" else None)
            etiqueta(k)
        # ventana roja sobre el bloque de origen y tesela en el destino
        if op == "concatenar":
            src = [a for a, b in UN_SKIPS if b == k][0]
        elif op == "argmax":
            src = "m"
        else:
            src = [a for a, b, _ in UN_FLECHAS if b == k][0]
        a_, b_ = divmod(max(q - 1, 0), UN_TES)
        xs_, ys_, ss_, _, _ = caja(src)
        c = ss_ / UN_TES
        ax.add_patch(Rectangle((xs_ + b_ * c, ys_ + a_ * c), c, c, fc=ROJO,
                               alpha=0.25, ec=ROJO, lw=3, zorder=7))
        xd, yd, sd, dxd, dyd = caja(k)
        if mitad == "sube":
            xd, yd = xd + 0.5 * dxd, yd - 0.5 * dyd
        c = sd / UN_TES
        if q > 0:
            ax.add_patch(Rectangle((xd + b_ * c, yd + a_ * c), c, c, fill=False,
                                   ec=ROJO, lw=2.5, zorder=7))
    if crece > 0:
        vector_b(crece)
    if op:
        ax.text(UN_EJE, 12, op.replace(" + ", "\n+ "), ha="center", va="top",
                fontsize=24, color=ROJO, fontweight="bold", linespacing=1.05)

    # rótulos fijos
    ax.text(45, 838, "U-Net con padding (variante usual)", ha="left",
            va="center", fontsize=18, color=GRIS_MEDIO)
    if any(c in hechos and estado.get(c) != "sube" for c in ("c0", "c1", "c2",
                                                            "c3")):
        ax.text(W * DPI - 45, 838, "rojo: canales copiados por el skip · gris:"
                " canales subidos", ha="right", va="center", fontsize=18,
                color=GRIS_MEDIO)
    if "m" in hechos and estado.get("m") != "k":
        _leyenda_horizontal(ax, W * DPI - 45, 26)
    # encoder / decoder adentro de los brazos de la U
    y_txt = (UN_FILAS[0] + UN_FILAS[1]) / 2 - 12
    if "e3" in hechos:
        x = G["e0"]["x"] + G["e0"]["s"] + G["e0"]["dx"] + 34
        ax.text(x, y_txt, "encoder:\nbaja la resolución,\nsuben los canales",
                ha="left", va="center", fontsize=20, color=TINTA,
                linespacing=1.15)
    if "o0" in hechos:
        x = G["c0"]["x"] - 34
        ax.text(x, y_txt, "decoder:\nvuelve a subir\nla resolución",
                ha="right", va="center", fontsize=20, color=TINTA,
                linespacing=1.15)
    if pie:
        ax.text(W * DPI / 2, H * DPI - 22, pie, ha="center", va="center",
                fontsize=22, color=TINTA)


UN_PASOS = [  # (destino, operación, pie)
    ("a0", "conv 3×3", "conv 3×3 con padding: 64 filtros buscan bordes; la"
     " resolución no cambia (256×256)"),
    ("e0", "conv 3×3", "conv 3×3 con padding: 64 filtros buscan bordes; la"
     " resolución no cambia (256×256)"),
]
for _n, (_ri, _pie) in enumerate((
        (128, "256 → 128: el pooling divide la resolución por 2; 128 canales"
              " combinan bordes"),
        (64, "128 → 64: 256 canales responden a partes: patas, cola, cuerpo"),
        (32, "64 → 32: cada canal es menos imagen y más «acá hay parte de"
             " gato»"),
        (16, "bottleneck 16×16×1024: sabe qué hay, pero perdió dónde están"
             " los bordes")), 1):
    _a, _e = (f"a{_n}", f"e{_n}") if _n < 4 else ("b1", "b")
    UN_PASOS += [(_a, "max pool 2×2 + conv 3×3", _pie), (_e, "conv 3×3", _pie)]
for _n, (_r, _cs, _co) in zip((3, 2, 1, 0), ((32, 1024, 512), (64, 512, 256),
                                            (128, 256, 128), (256, 128, 64))):
    UN_PASOS += [
        (f"c{_n}", "up-conv 2×2", f"up-conv 2×2: {_r // 2} → {_r}, los mapas"
         " suben de resolución pero salen borrosos"),
        (f"c{_n}", "concatenar", "el skip trae los bordes finos que el encoder"
         f" había perdido: {_cs // 2} + {_cs // 2} = {_cs} canales"),
        (f"o{_n}", "2× conv 3×3", "conv 3×3: mezcla qué hay (lo subido) con"
         f" dónde está (lo copiado), {_cs} → {_co}"),
    ]
UN_PASOS += [
    ("m", "conv 1×1", "conv 1×1: la misma capa densa en cada píxel, 64 canales"
     " → C clases"),
    ("m", "argmax", "argmax: una clase por píxel, con bordes nítidos: patas y"
     " cola incluidas"),
]
UN_PIE_EMB = ("cada posición del bottleneck guarda un vector de 1024 que"
              " describe qué hay en su región")


def unet_dimensiones():
    assert 256 // 2 ** 4 == 16
    m, gato = _un_datos()
    G = _un_geometria()
    fig, ax = _fcn_figura()
    _un_dibujar(ax, m, gato, G, hechos=[b[0] for b in UN_BLOQUES], crece=1.0)
    ruta = os.path.join(OUT, "unet-dimensiones.png")
    fig.savefig(ruta, dpi=DPI, facecolor="white")
    plt.close(fig)
    print(f"{ruta}  {os.path.getsize(ruta) / 1e6:.2f} MB")


def _un_cuadros(m, gato, G, fig, ax, por_paso=5):
    """Genera (nombre, cuadros) del ciclo completo de unet-en-vivo."""
    def foto(**kw):
        _un_dibujar(ax, m, gato, G, **kw)
        return capturar(fig)

    hechos, estado, crece = ["in"], {}, 0.0
    yield "inicio", [foto(hechos=hechos, pie="Entrada: una imagen de 256×256"
                          " píxeles, 1 canal")] * 5
    for n, (dest, op, pie) in enumerate(UN_PASOS):
        est = dict(estado)
        for f in range(1, por_paso + 1):
            yield f"{n:02d}-{dest}", [foto(hechos=hechos, activa=dest,
                                           t=f / por_paso, estado=est, pie=pie,
                                           op=op, crece=crece)]
        if op == "up-conv 2×2":
            estado[dest] = "sube"
        elif op == "concatenar":
            estado.pop(dest, None)
        elif op == "conv 1×1":
            estado["m"] = "k"
        elif op == "argmax":
            estado.pop("m", None)
        if dest not in hechos:
            hechos.append(dest)
        if not dest.startswith("a") and dest != "b1":
            yield f"{n:02d}-{dest}-quieto", [foto(hechos=hechos, estado=estado,
                                                  pie=pie, op=op, crece=crece)]
        if dest in ("e0", "e1", "e2", "e3", "b"):   # la cara es 1 de muchos
            for j in (1, 2):
                yield f"{n:02d}-{dest}-canal{j}", [foto(
                    hechos=hechos, estado=estado, pie=pie, op=op,
                    canales={dest: j}, crece=crece)] * 2
        if dest == "b":
            for f in range(1, 9):
                yield "emb", [foto(hechos=hechos, estado=estado, pie=UN_PIE_EMB,
                                   crece=f / 8)]
            crece = 1.0
            yield "emb-quieto", [foto(hechos=hechos, estado=estado,
                                      pie=UN_PIE_EMB, crece=1.0)] * 5
    yield "final", [foto(hechos=[b[0] for b in UN_BLOQUES], crece=1.0)]


def unet_en_vivo(fps=12, pausa_s=3.0):
    m, gato = _un_datos()
    G = _un_geometria()
    fig, ax = _fcn_figura()
    frames = []
    for _, fs in _un_cuadros(m, gato, G, fig, ax):
        frames += fs
    plt.close(fig)
    guardar_gif(frames, os.path.join(OUT, "unet-en-vivo.gif"), fps=fps,
                pausa_s=pausa_s, colores=64)
    return frames


TAREAS = {
    "conv1d-filtrado": conv1d_filtrado,
    "conv1d-detector-voz": conv1d_detector_voz,
    "conv1d-largo-variable": conv1d_largo_variable,
    "conv2d-kernel": conv2d_kernel,
    "conv2d-bordes": conv2d_bordes,
    "fcn-dimensiones": fcn_dimensiones,
    "fcn-en-vivo": fcn_en_vivo,
    "unet-dimensiones": unet_dimensiones,
    "unet-en-vivo": unet_en_vivo,
}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for nombre in (sys.argv[1:] or TAREAS):
        TAREAS[nombre]()
