#!/usr/bin/env python3
"""Animaciones de la sección 1 (red densa y embeddings) de la Talk
"segmentacion-y-stable-diffusion".

  mlp-en-vivo.gif (+ .png)         una imagen 28x28 se aplana en 784 valores y
                                   pasa capa densa por capa densa hasta las 10
                                   clases; cierre: una imagen 32x32 (1024
                                   valores) no entra en las 784 entradas
  embeddings-en-vivo.gif (+ .png)  imagen, texto y audio pasan por su encoder,
                                   salen como vectores de largo fijo y se
                                   proyectan a un espacio común 2D

Todo es sintético (numpy + PIL). Reusa estilo y helpers de
gen_animaciones_conv.py (que no se modifica).
Uso:  python3 gen_anim_mlp-emb.py [mlp-en-vivo|embeddings-en-vivo]
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_animaciones_conv import (  # noqa: E402
    plt, TINTA, ROJO, RELLENO, GRIS_MEDIO, W, H, DPI, OUT, capturar,
    guardar_gif)
from matplotlib.patches import (  # noqa: E402
    Circle, FancyBboxPatch, Polygon, Rectangle)
from matplotlib.collections import LineCollection  # noqa: E402
from PIL import Image, ImageDraw, ImageFilter, ImageFont  # noqa: E402

PX_W, PX_H = W * DPI, H * DPI
GRIS_BORDE = "#CFC8C6"
GRIS_LINEA = "#DDD7D5"
ROJO_SUAVE = "#F6C9CD"
FUENTE_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
CUADROS = os.environ.get("CUADROS_DIR")      # para verificación


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


def pie(ax, texto, color=TINTA, negrita=False):
    ax.text(PX_W / 2, PX_H - 46, texto, ha="center", va="center",
            fontsize=22, color=color, fontweight="bold" if negrita else None)


def encabezado(ax, x, linea1, linea2, color=TINTA, linea3=None):
    ax.text(x, 56, linea1, ha="center", va="center", fontsize=22,
            fontweight="bold", color=color)
    ax.text(x, 90, linea2, ha="center", va="center", fontsize=20,
            color=color if color == ROJO else GRIS_MEDIO)
    if linea3:
        ax.text(x, 120, linea3, ha="center", va="center", fontsize=18,
                color=GRIS_MEDIO)


def gris_rgb(v):
    """0 -> blanco, 1 -> tinta."""
    v = np.clip(np.asarray(v, float), 0, 1)[..., None]
    blanco = np.ones(3)
    tinta = np.array([0x22, 0x22, 0x22]) / 255
    return blanco * (1 - v) + tinta * v


def hex_rgb(h):
    return np.array([int(h[i:i + 2], 16) for i in (1, 3, 5)]) / 255


def digito(caracter, lado, tam, dx=0, dy=0):
    """Dígito sintético en escala de grises [0,1] (tinta = 1)."""
    esc = 8
    im = Image.new("L", (lado * esc, lado * esc), 0)
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(FUENTE_B, tam * esc)
    bb = d.textbbox((0, 0), caracter, font=f)
    x = (lado * esc - (bb[2] - bb[0])) / 2 - bb[0] + dx * esc
    y = (lado * esc - (bb[3] - bb[1])) / 2 - bb[1] + dy * esc
    d.text((x, y), caracter, fill=255, font=f)
    im = im.resize((lado, lado), Image.LANCZOS).filter(
        ImageFilter.GaussianBlur(0.5))
    a = np.asarray(im, float) / 255
    return np.clip(a / a.max(), 0, 1)


# =========================================================================
# 1. mlp-en-vivo.gif
# =========================================================================
M_PX = 8.5                         # píxeles de pantalla por píxel de imagen
M_IMG_CX, M_YC = 180, 400          # centro de la imagen
M_SX0, M_SX1 = 390, 430            # columna del vector de entrada
M_SY0 = 160
M_SLOT = 480                       # alto que ocupan las 784 entradas
M_X1, M_X2, M_XO = 700, 990, 1270  # columnas de neuronas
M_R = 15
M_N1, M_N2 = 16, 12                # neuronas dibujadas (de 128 y 64)
M_YS1 = np.linspace(M_SY0 + 10, M_SY0 + M_SLOT - 10, M_N1)
M_YS2 = np.linspace(M_SY0 + 45, M_SY0 + M_SLOT - 45, M_N2)
M_YSO = np.linspace(M_SY0 + 70, M_SY0 + M_SLOT - 70, 10)
M_FUENTES = np.linspace(M_SY0 + 4, M_SY0 + M_SLOT - 4, 32)
M_BAR_X0, M_BAR_MAX = 1338, 170
M_PIES = {
    "intro": "imagen de 28×28 píxeles: 784 números entre 0 y 1",
    "aplanar": "aplanar: la imagen se lee fila por fila → vector de "
               "28 · 28 = 784 valores",
    "c1": "capa densa 1: cada neurona = ReLU(suma ponderada de las 784 "
          "entradas + sesgo) → 128 valores",
    "c2": "capa densa 2: cada neurona suma ponderadamente las 128 salidas "
          "anteriores → 64 valores",
    "out": "salida: 10 neuronas, una por dígito, cada una sobre las 64 "
           "anteriores → 10 valores",
    "softmax": "softmax: los 10 valores pasan a probabilidades; "
               "la mayor (dígito 3) es la clase",
    "otra": "otra imagen: 32×32 píxeles = 1024 valores",
    "aplanar2": "aplanada da 1024 valores, pero la capa densa 1 tiene "
                "pesos para 784",
    "fin": "la capa densa solo acepta entradas de largo fijo: 1024 ≠ 784",
}


def _mlp_datos():
    img28 = digito("3", 28, 22)
    img32 = digito("5", 32, 25)
    rng = np.random.default_rng(3)
    x = img28.ravel()
    w1 = rng.standard_normal((128, 784)) * 0.09
    h1 = np.maximum(w1 @ x + 0.1 * rng.standard_normal(128), 0)
    w2 = rng.standard_normal((64, 128)) / np.sqrt(128)
    h2 = np.maximum(w2 @ h1, 0)
    w3 = rng.standard_normal((10, 64)) / np.sqrt(64)
    z = w3 @ h2
    # pesos ilustrativos: se fuerza que la clase correcta (3) sea la mayor
    z = 0.6 * (z - z.mean()) / (z.std() + 1e-9)
    z[3] += 4.2
    p = np.exp(z - z.max())
    p /= p.sum()
    sel1 = np.linspace(0, 127, M_N1).astype(int)
    sel2 = np.linspace(0, 63, M_N2).astype(int)
    a1 = h1[sel1] / h1[sel1].max()
    a2 = h2[sel2] / h2[sel2].max()
    ao = (z - z.min()) / (z.max() - z.min())
    assert img28.size == 784 and img32.size == 1024 and p.argmax() == 3
    return dict(img28=img28, img32=img32, a1=a1, a2=a2, ao=ao, p=p)


def _mlp_dibujar(ax, D, etapa, filas=0, n1=0, n2=0, no=0, probs=0.0,
                 cerrar=False, filas2=0, marca=False, texto_pie=None):
    """etapa: nombre del pie. filas: filas de la 28x28 ya aplanadas.
    n1/n2/no: neuronas ya calculadas por capa (la última, en rojo si la etapa
    es esa capa). probs: fracción de crecimiento de las barras (0..1).
    cerrar: fase de la imagen 32x32; filas2: sus filas aplanadas."""
    lienzo(ax)
    activa = {"c1": ("c1", n1), "c2": ("c2", n2), "out": ("out", no)}.get(
        etapa, (None, 0))

    # ---------- encabezados
    lado_img = 32 if cerrar else 28
    encabezado(ax, M_IMG_CX, "imagen",
               f"{lado_img}×{lado_img} píxeles",
               color=ROJO if cerrar else TINTA)
    encabezado(ax, (M_SX0 + M_SX1) / 2, "entrada",
               "1024 valores" if cerrar and filas2 > 0 else "784 valores",
               color=ROJO if cerrar and filas2 > 0 else TINTA)
    encabezado(ax, M_X1, "capa densa 1", "128 neuronas",
               linea3="(se dibujan 16)")
    encabezado(ax, M_X2, "capa densa 2", "64 neuronas",
               linea3="(se dibujan 12)")
    encabezado(ax, (M_XO - M_R + M_BAR_X0 + M_BAR_MAX) / 2, "salida",
               "10 clases", linea3="probabilidad por clase")

    # ---------- imagen
    img = D["img32"] if cerrar else D["img28"]
    n = img.shape[0]
    lado = n * M_PX
    ix0, iy0 = M_IMG_CX - lado / 2, M_YC - lado / 2
    ax.imshow(gris_rgb(img), extent=(ix0, ix0 + lado, iy0 + lado, iy0),
              interpolation="nearest", zorder=2)
    ax.add_patch(Rectangle((ix0, iy0), lado, lado, fill=False, ec=TINTA,
                           lw=1.6, zorder=3))
    for k in range(1, n):                      # grilla tenue de píxeles
        ax.plot([ix0 + k * M_PX] * 2, [iy0, iy0 + lado], color="#BBBBBB",
                lw=0.35, zorder=2.5, alpha=0.6)
        ax.plot([ix0, ix0 + lado], [iy0 + k * M_PX] * 2, color="#BBBBBB",
                lw=0.35, zorder=2.5, alpha=0.6)

    # ---------- vector de entrada (columna)
    paso = M_SLOT / 784
    hechas = filas2 if cerrar else filas
    nvals = n * n
    vec = img.ravel()
    largo_total = nvals * paso if (cerrar and filas2 > 0) else M_SLOT
    col = np.tile(hex_rgb(RELLENO), (max(nvals, 784), 1))
    col[: hechas * n] = gris_rgb(vec[: hechas * n])
    col = col[: (nvals if (cerrar and filas2 > 0) else 784)]
    ax.imshow(col[:, None, :], extent=(M_SX0, M_SX1, M_SY0 + largo_total,
                                       M_SY0),
              interpolation="nearest", aspect="auto", zorder=2)
    ax.add_patch(Rectangle((M_SX0, M_SY0), M_SX1 - M_SX0, M_SLOT, fill=False,
                           ec=TINTA, lw=1.8, zorder=4))
    if cerrar and filas2 > 0:
        y784 = M_SY0 + M_SLOT
        hechas_v = min(hechas * n, nvals)
        if hechas_v > 784:                     # lo que sobra, en rojo
            yb = M_SY0 + hechas_v * paso
            ax.add_patch(Rectangle((M_SX0, y784), M_SX1 - M_SX0, yb - y784,
                                   fc=ROJO, alpha=0.35, ec="none", zorder=3))
            ax.add_patch(Rectangle((M_SX0, y784), M_SX1 - M_SX0, yb - y784,
                                   fill=False, ec=ROJO, lw=2.6, zorder=4))
        ax.plot([M_SX0 - 14, M_SX1 + 14], [y784, y784], color=ROJO, lw=2.4,
                ls="--", zorder=5)
        ax.text(M_SX0 - 22, y784, "784", ha="right", va="center",
                fontsize=20, color=ROJO, fontweight="bold")
        if marca:
            yf = M_SY0 + nvals * paso
            ax.text(M_SX0 - 22, yf, "1024", ha="right", va="center",
                    fontsize=20, color=ROJO, fontweight="bold")
            ax.text(M_SX1 + 28, (y784 + yf) / 2,
                    "240 valores de más:\nla capa densa 1 no tiene "
                    "pesos para ellos", ha="left", va="center", fontsize=20,
                    color=ROJO, linespacing=1.25)
    else:
        ax.text((M_SX0 + M_SX1) / 2, M_SY0 + M_SLOT + 36, "N = 784, fijo",
                ha="center", va="center", fontsize=21, color=ROJO,
                fontweight="bold")

    # ---------- aplanado: fila activa → tramo del vector
    if 0 < hechas and ((not cerrar and filas < 28) or
                       (cerrar and filas2 < n)):
        r = hechas - 1
        ry0, ry1 = iy0 + r * M_PX, iy0 + (r + 1) * M_PX
        sy0, sy1 = M_SY0 + r * n * paso, M_SY0 + (r + 1) * n * paso
        fuera = cerrar and (r + 1) * n > 784
        ax.add_patch(Polygon([(ix0 + lado, ry0), (M_SX0, sy0), (M_SX0, sy1),
                              (ix0 + lado, ry1)], closed=True, fc=ROJO,
                             alpha=0.22, ec="none", zorder=3))
        ax.add_patch(Rectangle((ix0, ry0), lado, M_PX, fill=False, ec=ROJO,
                               lw=2.6, zorder=5))
        ax.add_patch(Rectangle((M_SX0, sy0), M_SX1 - M_SX0, sy1 - sy0,
                               fill=False, ec=ROJO, lw=2.6 if not fuera else 3,
                               zorder=5))

    # ---------- conexiones
    def conexiones(xa, ys_a, xb, ys_b, activa_j=None):
        segs = [[(xa, ya), (xb, yb)] for yb in ys_b for ya in ys_a]
        ax.add_collection(LineCollection(segs, colors=GRIS_LINEA, lw=0.6,
                                         zorder=1))
        if activa_j is not None:
            yb = ys_b[activa_j]
            act = [[(xa, ya), (xb, yb)] for ya in ys_a]
            ax.add_collection(LineCollection(act, colors=ROJO, lw=1.3,
                                             alpha=0.75, zorder=1.5))

    def j_activa(nombre, k):
        return k - 1 if activa[0] == nombre and k > 0 else None

    conexiones(M_SX1, M_FUENTES, M_X1 - M_R, M_YS1, j_activa("c1", n1))
    conexiones(M_X1 + M_R, M_YS1, M_X2 - M_R, M_YS2, j_activa("c2", n2))
    conexiones(M_X2 + M_R, M_YS2, M_XO - M_R, M_YSO, j_activa("out", no))

    # ---------- neuronas
    def capa(x, ys, acts, k, nombre):
        for j, y in enumerate(ys):
            if j < k:
                es_activa = activa[0] == nombre and j == k - 1
                if es_activa:
                    fc, ec, lw = ROJO, ROJO, 2.4
                else:
                    v = 0.12 + 0.75 * acts[j]
                    fc, ec, lw = gris_rgb(v), TINTA, 1.6
            else:
                fc, ec, lw = "white", TINTA, 1.6
            ax.add_patch(Circle((x, y), M_R, fc=fc, ec=ec, lw=lw, zorder=4))

    capa(M_X1, M_YS1, D["a1"], n1, "c1")
    capa(M_X2, M_YS2, D["a2"], n2, "c2")
    capa(M_XO, M_YSO, D["ao"], no, "out")

    # ---------- salida: dígitos y barras de probabilidad
    gana = int(np.argmax(D["p"]))
    for d, y in enumerate(M_YSO):
        roja = probs > 0 and d == gana
        ax.text(M_XO + 34, y, str(d), ha="center", va="center", fontsize=20,
                color=ROJO if roja else TINTA,
                fontweight="bold" if roja else None)
        ax.add_patch(Rectangle((M_BAR_X0, y - 10), M_BAR_MAX, 20,
                               fc=RELLENO, ec="none", zorder=2))
        if probs > 0:
            L = M_BAR_MAX * D["p"][d] * probs
            ax.add_patch(Rectangle((M_BAR_X0, y - 10), max(L, 1.5), 20,
                                   fc=ROJO if roja else GRIS_MEDIO,
                                   ec="none", zorder=3))
            if roja and probs >= 1:
                ax.text(M_BAR_X0 + L + 10, y, f"{D['p'][d]:.0%}",
                        ha="left", va="center", fontsize=20, color=ROJO,
                        fontweight="bold", zorder=6,
                        bbox=dict(fc="white", ec="none", pad=1.5))
    if True:
        ax.plot([M_BAR_X0, M_BAR_X0], [M_YSO[0] - 18, M_YSO[-1] + 18],
                color=TINTA, lw=1.4, zorder=3)

    if texto_pie:
        fin = etapa == "fin"
        pie(ax, texto_pie, color=ROJO if fin else TINTA, negrita=fin)


def mlp_en_vivo(fps=12, pausa_s=3.0):
    D = _mlp_datos()
    fig, ax = figura()
    frames = []

    def toma(rep=1, **kw):
        _mlp_dibujar(ax, D, **kw)
        f = capturar(fig)
        frames.extend([f] * rep)

    toma(10, etapa="intro", texto_pie=M_PIES["intro"])
    for r in range(1, 29):
        toma(etapa="aplanar", filas=r, texto_pie=M_PIES["aplanar"])
    toma(4, etapa="aplanar", filas=28, texto_pie=M_PIES["aplanar"])
    for k in range(1, M_N1 + 1):
        toma(etapa="c1", filas=28, n1=k, texto_pie=M_PIES["c1"])
    toma(4, etapa="c1+", filas=28, n1=M_N1, texto_pie=M_PIES["c1"])
    for k in range(1, M_N2 + 1):
        toma(etapa="c2", filas=28, n1=M_N1, n2=k, texto_pie=M_PIES["c2"])
    toma(4, etapa="c2+", filas=28, n1=M_N1, n2=M_N2, texto_pie=M_PIES["c2"])
    for k in range(1, 11):
        toma(etapa="out", filas=28, n1=M_N1, n2=M_N2, no=k,
             texto_pie=M_PIES["out"])
    toma(2, etapa="out+", filas=28, n1=M_N1, n2=M_N2, no=10,
         texto_pie=M_PIES["out"])
    for s in np.linspace(0.15, 1, 7):
        toma(etapa="softmax", filas=28, n1=M_N1, n2=M_N2, no=10, probs=s,
             texto_pie=M_PIES["softmax"])
    toma(14, etapa="softmax", filas=28, n1=M_N1, n2=M_N2, no=10, probs=1,
         texto_pie=M_PIES["softmax"])
    toma(9, etapa="otra", cerrar=True, texto_pie=M_PIES["otra"])
    for r in range(2, 33, 2):
        toma(etapa="aplanar2", cerrar=True, filas2=r,
             texto_pie=M_PIES["aplanar2"])
    toma(4, etapa="aplanar2", cerrar=True, filas2=32,
         texto_pie=M_PIES["aplanar2"])
    _mlp_dibujar(ax, D, etapa="fin", cerrar=True, filas2=32, marca=True,
                 texto_pie=M_PIES["fin"])
    frames.append(capturar(fig))
    ruta_png = os.path.join(OUT, "mlp-en-vivo.png")
    fig.savefig(ruta_png, dpi=DPI, facecolor="white")
    plt.close(fig)
    guardar_gif(frames, os.path.join(OUT, "mlp-en-vivo.gif"), fps=fps,
                pausa_s=pausa_s, colores=48)
    print(f"{len(frames)} cuadros, {(len(frames) - 1) / fps + pausa_s:.1f} s")
    if CUADROS:
        for i in (5, 25, 60, 95, 125):
            if i < len(frames):
                frames[i].save(os.path.join(CUADROS, f"mlp-{i:03d}.png"))
        frames[-1].save(os.path.join(CUADROS, "mlp-final.png"))
    return frames


# =========================================================================
# 2. embeddings-en-vivo.gif
# =========================================================================
E_D = 512                                   # largo del embedding
E_YS = [262, 477, 692]                      # centro de cada fila
E_IN_CX = 160                               # columna de entrada
E_ENC_X0, E_ENC_X1 = 310, 690               # zona de los encoders
E_VX0, E_CELDA, E_VGAP = 728, 32, 6         # vector: e1 e2 e3 … ed
E_PANEL = (975, 150, 1555, 775)             # x0, y0, x1, y1
E_CENT = {"perro": (1190, 360), "auto": (1405, 625)}  # centros en pantalla
E_MOD_PESO = 0.22                           # cuánto separa la modalidad
E_MOD = ["imagen", "texto", "audio"]
E_CONCEPTOS = ["perro", "auto"]
E_ETIQ = {("perro", 0): "foto de perro", ("perro", 1): "«un perro»",
          ("perro", 2): "ladrido", ("auto", 0): "foto de auto",
          ("auto", 1): "«un auto»", ("auto", 2): "ruido de motor"}
E_MARCA = {0: "s", 1: "o", 2: "^"}
# bloques de cada encoder: (ancho, alto) y el pie de esa operación
E_IMG_BLOQ = [(18, 130), (24, 102), (32, 78), (42, 56), (42, 38)]
E_IMG_PIES = [
    "bloque conv 1: 224×224×3 → 112×112×64",
    "bloque conv 2: 112×112×64 → 56×56×128",
    "bloque conv 3: 56×56×128 → 28×28×256",
    "bloque conv 4: 28×28×256 → 14×14×512",
    "bloque conv 5: 14×14×512 → 7×7×512; promedio global → vector de 512",
]
E_AUD_BLOQ = [(130, 22), (96, 40), (62, 60)]
E_AUD_PIES = [
    "conv 1D: 16 000 muestras × 1 canal → 4 000 pasos × 128 canales",
    "conv 1D: 4 000 × 128 → 1 000 pasos × 256 canales",
    "conv 1D: 1 000 × 256 → 250 × 512; promedio en el tiempo → vector "
    "de 512",
]
E_TXT_PIES = [
    "tokenizar: «un perro» → 2 tokens, cada uno un vector de 512",
    "transformer: atención entre los tokens → un vector de 512 para la "
    "frase",
]
E_PIES = {
    "intro": "imagen, texto y audio: tres entradas distintas, un encoder "
             "para cada una",
    "proy": "proyección: cada vector de 512 es un punto del espacio común "
            "(acá, dibujado en 2D)",
    "auto": "otro significado (auto): foto, texto y ruido de motor pasan por "
            "los mismos encoders",
    "auto-proy": "sus tres vectores caen juntos, en otra zona del espacio",
    "fin": "significado parecido → vectores cercanos, porque los encoders\n"
           "se entrenaron juntos para alinear las modalidades (como CLIP)",
}


def _emb_dibujos():
    """Miniaturas sintéticas (perro, auto) en escala de grises [0,1]."""
    esc, n = 4, 130
    L = n * esc

    def lienzo_p():
        im = Image.new("L", (L, L), 0)
        return im, ImageDraw.Draw(im)

    def e(d, cx, cy, rx, ry, v):
        d.ellipse([(cx - rx) * esc, (cy - ry) * esc, (cx + rx) * esc,
                   (cy + ry) * esc], fill=int(v * 255))

    im, d = lienzo_p()                       # perro de frente
    e(d, 34, 60, 15, 34, 0.85)               # orejas caídas
    e(d, 96, 60, 15, 34, 0.85)
    e(d, 65, 66, 36, 40, 0.45)               # cabeza
    e(d, 65, 90, 22, 17, 0.18)               # hocico claro
    e(d, 50, 58, 5, 6, 0.95)                 # ojos
    e(d, 80, 58, 5, 6, 0.95)
    e(d, 65, 81, 9, 6, 0.95)                 # nariz
    d.line([65 * esc, 87 * esc, 65 * esc, 97 * esc], fill=242, width=2 * esc)
    d.arc([55 * esc, 90 * esc, 75 * esc, 102 * esc], 20, 160, fill=242,
          width=2 * esc)
    perro = np.asarray(im.resize((n, n), Image.LANCZOS), float) / 255

    im, d = lienzo_p()                       # auto de costado
    d.rounded_rectangle([10 * esc, 62 * esc, 120 * esc, 92 * esc],
                        radius=10 * esc, fill=int(0.7 * 255))
    d.polygon([(34 * esc, 63 * esc), (46 * esc, 40 * esc), (88 * esc, 40 * esc),
               (102 * esc, 63 * esc)], fill=int(0.7 * 255))
    d.polygon([(42 * esc, 61 * esc), (50 * esc, 46 * esc), (64 * esc, 46 * esc),
               (64 * esc, 61 * esc)], fill=int(0.12 * 255))
    d.polygon([(69 * esc, 61 * esc), (69 * esc, 46 * esc), (85 * esc, 46 * esc),
               (95 * esc, 61 * esc)], fill=int(0.12 * 255))
    e(d, 36, 92, 12, 12, 0.95)
    e(d, 96, 92, 12, 12, 0.95)
    e(d, 36, 92, 5, 5, 0.3)
    e(d, 96, 92, 5, 5, 0.3)
    auto = np.asarray(im.resize((n, n), Image.LANCZOS), float) / 255
    return {"perro": perro, "auto": auto}


def _emb_audios():
    rng = np.random.default_rng(5)
    n = 400
    t = np.arange(n)
    ladr = 0.04 * rng.standard_normal(n)
    for a in (40, 170, 300):                  # tres ladridos cortos
        u = np.arange(70)
        env = np.exp(-u / 18) * (1 - np.exp(-u / 3))
        ladr[a:a + 70] += env * (0.8 * np.sin(2 * np.pi * u / 6.5)
                                 + 0.4 * rng.standard_normal(70))
    motor = (0.35 * np.sin(2 * np.pi * t / 11) * (1 + 0.35 * np.sin(
        2 * np.pi * t / 90)) + 0.08 * rng.standard_normal(n))
    return {"perro": ladr / np.abs(ladr).max(),
            "auto": motor / np.abs(motor).max()}


def _emb_vectores():
    rng = np.random.default_rng(21)
    conc = {c: rng.standard_normal(E_D) for c in E_CONCEPTOS}
    modal = [rng.standard_normal(E_D) for _ in E_MOD]
    V = {}
    for c in E_CONCEPTOS:
        for m in range(3):
            v = conc[c] + E_MOD_PESO * modal[m] + 0.12 * rng.standard_normal(
                E_D)
            V[(c, m)] = v / np.linalg.norm(v)
    claves = list(V)
    X = np.array([V[k] for k in claves])
    Xc = X - X.mean(0)
    _, _, vt = np.linalg.svd(Xc, full_matrices=False)
    P = Xc @ vt[:2].T                          # PCA a 2D (real)
    # transformación de semejanza (rotación + escala uniforme + traslación):
    # conserva las proporciones de distancias de la proyección
    a, b = P[:3].mean(0), P[3:].mean(0)
    A, B = np.array(E_CENT["perro"], float), np.array(E_CENT["auto"], float)
    ang = np.arctan2(*(B - A)[::-1]) - np.arctan2(*(b - a)[::-1])
    esc = np.linalg.norm(B - A) / np.linalg.norm(b - a)
    R = esc * np.array([[np.cos(ang), -np.sin(ang)],
                        [np.sin(ang), np.cos(ang)]])
    P = (P - a) @ R.T + A
    pos = {k: P[i] for i, k in enumerate(claves)}
    cos = {(a_, b_): float(V[a_] @ V[b_]) for a_ in claves for b_ in claves}
    assert min(cos[(("perro", i), ("perro", j))] for i in range(3)
               for j in range(3)) > max(cos[(("perro", i), ("auto", j))]
                                        for i in range(3) for j in range(3))
    return V, pos


def _emb_datos():
    V, pos = _emb_vectores()
    return dict(img=_emb_dibujos(), aud=_emb_audios(), V=V, pos=pos)


def _emb_dibujar(ax, D, conc="perro", enc=None, vec=None, puntos=(),
                 vuelo=(), grupos=0.0, entrada_activa=(), texto_pie=None,
                 pie_rojo=False):
    """enc[r] = (pasos hechos, paso activo o None); vec[r] = (concepto,
    fracción de celdas llenas); puntos = claves ya ubicadas; vuelo = lista
    de (clave, t en 0..1); grupos = progreso de los círculos finales."""
    lienzo(ax)
    enc = enc or [(0, None)] * 3
    vec = vec or [(None, 0)] * 3

    encabezado(ax, E_IN_CX, "entrada", "tres modalidades")
    encabezado(ax, (E_ENC_X0 + E_ENC_X1) / 2, "encoder", "uno por modalidad")
    vx_c = E_VX0 + (3 * (E_CELDA + E_VGAP) + 30 + E_CELDA) / 2
    encabezado(ax, vx_c, "embedding", f"d = {E_D}", color=ROJO)
    encabezado(ax, (E_PANEL[0] + E_PANEL[2]) / 2, "espacio común",
               "proyección a 2D")
    # sin entrenamiento conjunto, encoders independientes no caerían cerca
    ax.text((E_ENC_X0 + E_VX0 + 4 * (E_CELDA + E_VGAP) + 30) / 2, 126,
            "encoders entrenados juntos para compartir el espacio",
            ha="center", va="center", fontsize=18, color=ROJO)

    for r, yc in enumerate(E_YS):
        roja = r in entrada_activa
        ec_in = ROJO if roja else TINTA
        lw_in = 3 if roja else 1.8
        # ---------- entrada
        ax.text(E_IN_CX, yc - 92, E_MOD[r], ha="center", va="center",
                fontsize=20, color=ROJO if roja else TINTA,
                fontweight="bold" if roja else None)
        if r == 0:
            s = 130
            im = D["img"][conc]
            fondo = hex_rgb(RELLENO)
            rgb = fondo * (1 - im[..., None]) + hex_rgb(TINTA) * im[..., None]
            ax.imshow(rgb, extent=(E_IN_CX - s / 2, E_IN_CX + s / 2,
                                   yc + s / 2, yc - s / 2), zorder=2,
                      interpolation="bilinear")
            ax.add_patch(Rectangle((E_IN_CX - s / 2, yc - s / 2), s, s,
                                   fill=False, ec=ec_in, lw=lw_in, zorder=3))
            x_sal = E_IN_CX + s / 2
        elif r == 1:
            caja(ax, E_IN_CX - 85, yc - 32, 170, 64, ec=ec_in, lw=lw_in,
                 fc=RELLENO)
            ax.text(E_IN_CX, yc, f"«un {conc}»", ha="center", va="center",
                    fontsize=22, color=TINTA, zorder=5)
            x_sal = E_IN_CX + 85
        else:
            caja(ax, E_IN_CX - 85, yc - 50, 170, 100, ec=ec_in, lw=lw_in,
                 fc="white")
            a = D["aud"][conc]
            xs = np.linspace(E_IN_CX - 75, E_IN_CX + 75, a.size)
            ax.plot(xs, yc - 40 * a, color=TINTA, lw=1.1, zorder=4)
            x_sal = E_IN_CX + 85
        hechos, activo = enc[r]
        en_curso = hechos > 0 or activo is not None
        flecha(ax, x_sal + 8, yc, E_ENC_X0 - 10, yc,
               color=ROJO if roja or activo == 0 else GRIS_MEDIO,
               lw=2.4 if roja else 1.8, ms=18)

        # ---------- encoder
        titulos = ["encoder convolucional", "encoder de texto",
                   "encoder de audio"]
        ax.text((E_ENC_X0 + E_ENC_X1) / 2, yc - 92, titulos[r], ha="center",
                va="center", fontsize=20,
                color=ROJO if activo is not None else TINTA,
                fontweight="bold" if activo is not None else None)

        def estilo(i):
            if activo == i:
                return ROJO_SUAVE, ROJO, 2.8
            if i < hechos:
                return "#D9D2D0", TINTA, 1.6
            return RELLENO, GRIS_BORDE, 1.6

        if r == 0:
            bloques = E_IMG_BLOQ
            gap = (E_ENC_X1 - E_ENC_X0 - sum(w for w, _ in bloques)) / (
                len(bloques) - 1)
            x = E_ENC_X0
            for i, (w, h) in enumerate(bloques):
                fc, ec, lw = estilo(i)
                ax.add_patch(Rectangle((x, yc - h / 2), w, h, fc=fc, ec=ec,
                                       lw=lw, zorder=3))
                if i < len(bloques) - 1:
                    flecha(ax, x + w + 4, yc, x + w + gap - 4, yc,
                           color=ROJO if activo == i + 1 else GRIS_MEDIO,
                           lw=1.6, ms=14)
                x += w + gap
        elif r == 1:
            tok_x0, tok_w = E_ENC_X0, 84
            ys_tok = [yc - 30, yc + 30]
            fc, ec, lw = estilo(0)
            for yt, palabra in zip(ys_tok, ["un", conc]):
                caja(ax, tok_x0, yt - 22, tok_w, 44, ec=ec, fc=fc, lw=lw,
                     r=8, z=4)
                ax.text(tok_x0 + tok_w / 2, yt, palabra, ha="center",
                        va="center", fontsize=20, color=TINTA, zorder=5)
            bx0 = tok_x0 + tok_w + 40
            fc, ec, lw = estilo(1)
            caja(ax, bx0, yc - 62, E_ENC_X1 - bx0, 124, ec=ec, fc=fc, lw=lw)
            ax.text((bx0 + E_ENC_X1) / 2, yc - 24, "transformer",
                    ha="center", va="center", fontsize=21, color=TINTA,
                    zorder=5)
            ax.text((bx0 + E_ENC_X1) / 2, yc + 22, "atención\nentre tokens",
                    ha="center", va="center", fontsize=18, linespacing=1.1,
                    color=GRIS_MEDIO if activo != 1 else ROJO, zorder=5)
            col = ROJO if activo == 1 else GRIS_MEDIO
            for yt in ys_tok:
                flecha(ax, tok_x0 + tok_w + 4, yt, bx0 - 4, yt, color=col,
                       lw=2 if activo == 1 else 1.6, ms=14)
        else:
            bloques = E_AUD_BLOQ
            gap = (E_ENC_X1 - E_ENC_X0 - sum(w for w, _ in bloques)) / (
                len(bloques) - 1)
            x = E_ENC_X0
            for i, (w, h) in enumerate(bloques):
                fc, ec, lw = estilo(i)
                ax.add_patch(Rectangle((x, yc - h / 2), w, h, fc=fc, ec=ec,
                                       lw=lw, zorder=3))
                if i < len(bloques) - 1:
                    flecha(ax, x + w + 4, yc, x + w + gap - 4, yc,
                           color=ROJO if activo == i + 1 else GRIS_MEDIO,
                           lw=1.6, ms=14)
                x += w + gap

        # ---------- vector de salida
        c_vec, frac = vec[r]
        flecha(ax, E_ENC_X1 + 6, yc, E_VX0 - 8, yc,
               color=ROJO if (frac > 0 and frac < 1) else GRIS_MEDIO,
               lw=1.8, ms=16)
        xs_c = [E_VX0 + i * (E_CELDA + E_VGAP) for i in range(3)]
        x_ult = xs_c[-1] + E_CELDA + 34
        xs_c.append(x_ult)
        llenas = int(round(frac * 4))
        if c_vec is not None:
            v = D["V"][(c_vec, r)]
            vals = [v[0], v[1], v[2], v[-1]]
        for i, xc in enumerate(xs_c):
            if c_vec is not None and i < llenas:
                g = 1 / (1 + np.exp(-vals[i] * 28))
                fc = gris_rgb(0.1 + 0.8 * g)
                ec = ROJO if frac < 1 else TINTA
            else:
                fc, ec = "white", GRIS_BORDE
            ax.add_patch(Rectangle((xc, yc - E_CELDA / 2), E_CELDA, E_CELDA,
                                   fc=fc, ec=ec, lw=1.8, zorder=4))
        ax.text(xs_c[2] + E_CELDA + 17, yc + 2, "…", ha="center",
                va="center", fontsize=20, color=TINTA)
        for i, nom in enumerate(["e1", "e2", "e3", f"e{E_D}"]):
            ax.text(xs_c[i] + E_CELDA / 2, yc + E_CELDA / 2 + 16, nom,
                    ha="center", va="center", fontsize=18, color=GRIS_MEDIO)

    # ---------- espacio común
    x0, y0, x1, y1 = E_PANEL
    caja(ax, x0, y0, x1 - x0, y1 - y0, ec=GRIS_BORDE, fc="white", lw=2,
         z=1, r=16)
    for gx in np.linspace(x0 + 40, x1 - 40, 6):
        ax.plot([gx, gx], [y0 + 20, y1 - 20], color="#F4F1F0", lw=1,
                zorder=1.2)
    for gy in np.linspace(y0 + 40, y1 - 40, 7):
        ax.plot([x0 + 20, x1 - 20], [gy, gy], color="#F4F1F0", lw=1,
                zorder=1.2)

    pos = D["pos"]
    cent = {c: np.mean([pos[(c, m)] for m in range(3)], 0)
            for c in E_CONCEPTOS}

    def punto(clave, xy, color, tam=15):
        ax.plot([xy[0]], [xy[1]], marker=E_MARCA[clave[1]], ms=tam,
                color=color, mec="white", mew=1.5, zorder=8,
                linestyle="none")

    radio = {}
    for c in E_CONCEPTOS:
        pts = np.array([pos[(c, m)] for m in range(3)])
        radio[c] = np.max(np.linalg.norm(pts - cent[c], axis=1)) + 34

    def y_etiquetas(c):
        """y de las etiquetas de un grupo, separadas al menos 34 px."""
        orden = sorted(range(3), key=lambda m: pos[(c, m)][1])
        ys = [pos[(c, m)][1] for m in orden]
        for k in range(1, 3):
            ys[k] = max(ys[k], ys[k - 1] + 34)
        corr = np.mean([pos[(c, m)][1] for m in orden]) - np.mean(ys)
        return {m: y + corr for m, y in zip(orden, ys)}

    for clave in puntos:
        c, m = clave
        xy = pos[clave]
        punto(clave, xy, TINTA)
        yl = y_etiquetas(c)[m]
        lado = 1 if c == "perro" else -1      # perro: a la derecha
        xl = cent[c][0] + lado * (radio[c] + 14)
        ax.plot([xy[0] + lado * 12, xl - lado * 6], [xy[1], yl],
                color=GRIS_BORDE, lw=1, zorder=7)
        ax.text(xl, yl, E_ETIQ[clave], ha="left" if lado > 0 else "right",
                va="center", fontsize=19, color=TINTA, zorder=9)

    for clave, t in vuelo:
        r = clave[1]
        a = np.array([x_ult + E_CELDA + 6, E_YS[r]])
        b = pos[clave]
        t_e = 1 - (1 - t) ** 2
        p = a + (b - a) * t_e
        ax.plot([a[0], p[0]], [a[1], p[1]], color=ROJO, lw=1.8, ls="--",
                zorder=7, alpha=0.8)
        punto(clave, p, ROJO, tam=17)

    if grupos > 0:
        for c, color in (("perro", ROJO), ("auto", GRIS_MEDIO)):
            th = np.linspace(0, 2 * np.pi * grupos, 120) - np.pi / 2
            ax.plot(cent[c][0] + radio[c] * np.cos(th),
                    cent[c][1] + radio[c] * np.sin(th), color=color, lw=2.4,
                    ls="--", zorder=6)
        if grupos >= 1:
            a, b = cent["perro"], cent["auto"]
            u = (b - a) / np.linalg.norm(b - a)
            pa, pb = a + u * (radio["perro"] + 10), b - u * (radio["auto"] + 10)
            ax.annotate("", xy=pb, xytext=pa, zorder=7,
                        arrowprops=dict(arrowstyle="<|-|>", color=TINTA,
                                        lw=2, mutation_scale=20,
                                        shrinkA=0, shrinkB=0))
            mm = (pa + pb) / 2
            nrm = np.array([-u[1], u[0]])          # perpendicular
            if nrm[0] > 0:
                nrm = -nrm
            ax.text(mm[0] + 34 * nrm[0], mm[1] + 34 * nrm[1], "lejos",
                    ha="right", va="center", fontsize=21, color=TINTA,
                    fontweight="bold", zorder=9)
            ax.text(a[0], a[1] - radio["perro"] - 14,
                    "cerca: mismo significado", ha="center", va="bottom",
                    fontsize=20, color=ROJO, fontweight="bold", zorder=9)

    if texto_pie and "\n" in texto_pie:          # pie de dos líneas
        ax.text(PX_W / 2, PX_H - 74, texto_pie, ha="center", va="center",
                fontsize=22, linespacing=1.3,
                color=ROJO if pie_rojo else TINTA,
                fontweight="bold" if pie_rojo else None)
    elif texto_pie:
        pie(ax, texto_pie, color=ROJO if pie_rojo else TINTA,
            negrita=pie_rojo)


def embeddings_en_vivo(fps=12, pausa_s=3.0):
    D = _emb_datos()
    fig, ax = figura()
    frames = []
    enc = [(0, None)] * 3
    vec = [(None, 0)] * 3
    puntos = []

    def toma(rep=1, **kw):
        _emb_dibujar(ax, D, **kw)
        f = capturar(fig)
        frames.extend([f] * rep)

    toma(10, enc=enc, vec=vec, texto_pie=E_PIES["intro"])
    pasos = {0: (len(E_IMG_BLOQ), E_IMG_PIES, 4),
             1: (2, E_TXT_PIES, 7),
             2: (len(E_AUD_BLOQ), E_AUD_PIES, 5)}
    for r in range(3):
        n_pasos, pies, por_paso = pasos[r]
        toma(3, enc=enc, vec=vec, puntos=puntos, entrada_activa=(r,),
             texto_pie=pies[0])
        for i in range(n_pasos):
            enc = enc[:r] + [(i, i)] + enc[r + 1:]
            toma(por_paso, enc=enc, vec=vec, puntos=puntos,
                 texto_pie=pies[i])
        enc = enc[:r] + [(n_pasos, None)] + enc[r + 1:]
        for k in range(1, 5):
            vec = vec[:r] + [("perro", k / 4)] + vec[r + 1:]
            toma(enc=enc, vec=vec, puntos=puntos, texto_pie=pies[-1])
        clave = ("perro", r)
        for t in np.linspace(0.12, 1, 8):
            toma(enc=enc, vec=vec, puntos=puntos, vuelo=[(clave, t)],
                 texto_pie=E_PIES["proy"])
        puntos = puntos + [clave]
        toma(5, enc=enc, vec=vec, puntos=puntos, texto_pie=E_PIES["proy"])

    # segundo significado: los tres a la vez
    enc_v = [(0, None)] * 3
    vec_v = [(None, 0)] * 3
    toma(6, conc="auto", enc=enc_v, vec=vec_v, puntos=puntos,
         entrada_activa=(0, 1, 2), texto_pie=E_PIES["auto"])
    for f in range(5):
        enc_v = [(min(f, len(E_IMG_BLOQ) - 1), min(f, len(E_IMG_BLOQ) - 1)),
                 (min(f // 3, 1), min(f // 3, 1)),
                 (min(f * 3 // 5, 2), min(f * 3 // 5, 2))]
        toma(2, conc="auto", enc=enc_v, vec=vec_v, puntos=puntos,
             texto_pie=E_PIES["auto"])
    enc_v = [(len(E_IMG_BLOQ), None), (2, None), (len(E_AUD_BLOQ), None)]
    for k in range(1, 5):
        vec_v = [("auto", k / 4)] * 3
        toma(conc="auto", enc=enc_v, vec=vec_v, puntos=puntos,
             texto_pie=E_PIES["auto"])
    claves = [("auto", m) for m in range(3)]
    for t in np.linspace(0.12, 1, 9):
        toma(conc="auto", enc=enc_v, vec=vec_v, puntos=puntos,
             vuelo=[(c, t) for c in claves], texto_pie=E_PIES["auto-proy"])
    puntos = puntos + claves
    toma(6, conc="auto", enc=enc_v, vec=vec_v, puntos=puntos,
         texto_pie=E_PIES["auto-proy"])

    # cierre: vuelve la fila del perro y se marcan los grupos
    vec_p = [("perro", 1)] * 3
    for g in np.linspace(0.15, 1, 7):
        toma(enc=enc_v, vec=vec_p, puntos=puntos, grupos=g,
             texto_pie=E_PIES["fin"], pie_rojo=True)
    _emb_dibujar(ax, D, enc=enc_v, vec=vec_p, puntos=puntos, grupos=1,
                 texto_pie=E_PIES["fin"], pie_rojo=True)
    frames.append(capturar(fig))
    fig.savefig(os.path.join(OUT, "embeddings-en-vivo.png"), dpi=DPI,
                facecolor="white")
    plt.close(fig)
    guardar_gif(frames, os.path.join(OUT, "embeddings-en-vivo.gif"), fps=fps,
                pausa_s=pausa_s, colores=48)
    print(f"{len(frames)} cuadros, {(len(frames) - 1) / fps + pausa_s:.1f} s")
    if CUADROS:
        for i in (8, 30, 60, 95, 125, 145):
            if i < len(frames):
                frames[i].save(os.path.join(CUADROS, f"emb-{i:03d}.png"))
        frames[-1].save(os.path.join(CUADROS, "emb-final.png"))
    return frames


TAREAS = {
    "mlp-en-vivo": mlp_en_vivo,
    "embeddings-en-vivo": embeddings_en_vivo,
}

if __name__ == "__main__":
    for nombre in (sys.argv[1:] or TAREAS):
        TAREAS[nombre]()
