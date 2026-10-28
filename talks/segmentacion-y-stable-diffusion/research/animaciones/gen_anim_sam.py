#!/usr/bin/env python3
"""Animaciones de SAM y SAM 2 para la Talk "segmentacion-y-stable-diffusion".

  sam-en-vivo.gif / .png    el image encoder corre una vez; cada prompt pasa
                            solo por el prompt encoder y el mask decoder
  sam2-en-vivo.gif / .png   video frame a frame con memory attention,
                            memory encoder y memory bank

Escenas sintéticas (numpy). Dimensiones de SAM (Kirillov et al. 2023): imagen
1024×1024×3, parches de 16×16 → embedding 64×64×256, máscara de 256×256 que se
escala a 1024×1024. SAM 2 (Ravi et al. 2024): mismo embedding de 64×64×256,
memoria proyectada a 64 canales, el banco guarda el frame con prompt y los 6
frames más recientes.

Uso:  python3 gen_anim_sam.py [sam-en-vivo] [sam2-en-vivo]
Estilo e importación de helpers desde gen_animaciones_conv.py (no se edita).
"""
import os
import sys

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402
from PIL import Image  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_animaciones_conv import (  # noqa: E402
    TINTA, ROJO, RELLENO, GRIS_MEDIO, W, H, DPI, OUT, capturar, conv2)

BORDE = "#D9D2D0"
APAGADO = "#B9B2B0"
PX_W, PX_H = W * DPI, H * DPI
SCRATCH = os.environ.get("ANIM_SCRATCH")


# -------------------------------------------------------------------------
# GIF con duraciones por cuadro (misma cuantización que gen_animaciones_conv)
# -------------------------------------------------------------------------
def guardar_gif_dur(frames, durs, ruta, colores=64):
    # fusionar cuadros consecutivos idénticos sumando la duración
    fr, du = [], []
    for f, d in zip(frames, durs):
        if fr and np.array_equal(np.asarray(fr[-1]), np.asarray(f)):
            du[-1] += d
        else:
            fr.append(f)
            du.append(d)
    muestra = fr[:: max(1, len(fr) // 10)] + [fr[-1]]
    ancho, alto = fr[0].size
    mosaico = Image.new("RGB", (ancho, alto * len(muestra)))
    for i, f in enumerate(muestra):
        mosaico.paste(f, (0, alto * i))
    paleta = mosaico.quantize(colors=colores, method=Image.Quantize.MEDIANCUT)
    pal_rgb = np.array(paleta.getpalette()[: 3 * colores]).reshape(-1, 3)
    for hexcol in ("#FFFFFF", TINTA, ROJO):
        c = np.array([int(hexcol[i:i + 2], 16) for i in (1, 3, 5)])
        pal_rgb[np.argmin(((pal_rgb - c) ** 2).sum(1))] = c
    plano = [int(v) for v in pal_rgb.ravel()]
    pal_f = pal_rgb.astype(np.int32)

    def mapear(f):
        a = np.asarray(f, dtype=np.int32)
        clave = (a[..., 0] << 16) | (a[..., 1] << 8) | a[..., 2]
        unicos, inv = np.unique(clave, return_inverse=True)
        rgb = np.stack([unicos >> 16, (unicos >> 8) & 255, unicos & 255], 1)
        idx = ((rgb[:, None, :] - pal_f[None]) ** 2).sum(2).argmin(1)
        p = Image.fromarray(idx[inv].reshape(clave.shape).astype(np.uint8), "P")
        p.putpalette(plano)
        return p

    pal = [mapear(f) for f in fr]
    pal[0].save(ruta, save_all=True, append_images=pal[1:],
                duration=[int(d) for d in du], loop=0, optimize=True,
                disposal=1)
    print(f"{ruta}  {os.path.getsize(ruta) / 1e6:.2f} MB  {len(pal)} cuadros"
          f"  {sum(du) / 1000:.1f} s")


# -------------------------------------------------------------------------
# Primitivas de dibujo (ejes en píxeles, y hacia abajo)
# -------------------------------------------------------------------------
def figura():
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    return fig, ax


def lienzo(ax):
    ax.clear()
    ax.set_xlim(0, PX_W)
    ax.set_ylim(PX_H, 0)
    ax.axis("off")


def caja(ax, x, y, w, h, titulo, sub=None, estado="idle", fs=24, fs_sub=19,
         sub2=None):
    """estado: idle (gris), activo (rojo lleno), hecho (gris con borde rojo),
    apagado (texto gris claro)."""
    fc, ec, ct, cs, lw = RELLENO, BORDE, TINTA, "#4A4645", 2.0
    if estado == "activo":
        fc, ec, ct, cs, lw = ROJO, ROJO, "white", "white", 2.0
    elif estado == "hecho":
        ec, lw = ROJO, 3.0
    elif estado == "apagado":
        ct, cs = APAGADO, APAGADO
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,"
                                "rounding_size=14", fc=fc, ec=ec, lw=lw,
                                zorder=3))
    lineas = [(titulo, fs, "bold", ct)]
    if sub:
        lineas.append((sub, fs_sub, "normal", cs))
    if sub2:
        lineas.append((sub2, fs_sub, "bold", cs))
    alto = [fs * 1.45 if i == 0 else fs_sub * 1.45 for i in range(len(lineas))]
    yy = y + h / 2 - sum(alto) / 2
    for (txt, f, wgt, col), a in zip(lineas, alto):
        ax.text(x + w / 2, yy + a / 2, txt, ha="center", va="center",
                fontsize=f, fontweight=wgt, color=col, zorder=4)
        yy += a


def flecha(ax, a, b, color=TINTA, lw=2.2, ms=20, ls="-", zorder=2):
    ax.annotate("", xy=b, xytext=a, zorder=zorder,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                mutation_scale=ms, shrinkA=0, shrinkB=0,
                                linestyle=ls))


def pie(ax, texto):
    ax.text(PX_W / 2, PX_H - 46, texto, ha="center", va="center",
            fontsize=24, color=TINTA)


def a_rgb(gris):
    return np.repeat(gris[..., None], 3, 2)


def superponer(rgb, mascara, alfa, color=ROJO):
    c = np.array([int(color[i:i + 2], 16) for i in (1, 3, 5)]) / 255
    out = rgb.copy()
    out[mascara] = (1 - alfa) * out[mascara] + alfa * c
    return out


def contorno(ax, mascara, x0, y0, lado, color=ROJO, lw=2.4, ls="-", z=6):
    n = mascara.shape[0]
    g = np.linspace(x0, x0 + lado, n)
    gy = np.linspace(y0, y0 + lado, n)
    ax.contour(g, gy, mascara.astype(float), levels=[0.5], colors=[color],
               linewidths=lw, linestyles=ls, zorder=z)


def suavizar(img, veces=2):
    for _ in range(veces):
        img = conv2(img, np.ones((3, 3)) / 9)
    return img


def pool(a, f):
    r = a.shape[0] // f
    return a.reshape(r, f, r, f).mean((1, 3))


def mapa_rgb(a, fondo=None):
    """Activación [0,1] -> blanco..tinta (alto = oscuro)."""
    blanco = np.ones(3)
    tinta = np.array([0x22, 0x22, 0x22]) / 255
    rgb = blanco + a[..., None] * 0.88 * (tinta - blanco)
    return rgb


def prisma(ax, x, y, lado, ddx, ddy, rgb, borde=TINTA, lw=1.8, capas=6,
           alfa=1.0, z=3):
    """Bloque con profundidad (pila de canales): cara frontal = un canal."""
    c_top, c_lado, c_capa = "#E6E0DE", "#D3CBC8", "#BDB5B2"
    top = [(x, y), (x + lado, y), (x + lado + ddx, y - ddy), (x + ddx, y - ddy)]
    lado_p = [(x + lado, y), (x + lado, y + lado),
              (x + lado + ddx, y + lado - ddy), (x + lado + ddx, y - ddy)]
    ax.add_patch(plt.Polygon(top, closed=True, fc=c_top, ec=borde, lw=lw * .8,
                             zorder=z, alpha=alfa))
    ax.add_patch(plt.Polygon(lado_p, closed=True, fc=c_lado, ec=borde,
                             lw=lw * .8, zorder=z, alpha=alfa))
    for j in range(1, capas):
        f = j / capas
        ax.plot([x + f * ddx, x + lado + f * ddx], [y - f * ddy, y - f * ddy],
                color=c_capa, lw=0.9, zorder=z + 0.1, alpha=alfa)
        ax.plot([x + lado + f * ddx] * 2, [y - f * ddy, y + lado - f * ddy],
                color=c_capa, lw=0.9, zorder=z + 0.1, alpha=alfa)
    ax.imshow(rgb, extent=(x, x + lado, y + lado, y), interpolation="nearest",
              zorder=z + 0.2, alpha=alfa)
    ax.add_patch(Rectangle((x, y), lado, lado, fill=False, ec=borde, lw=lw,
                           zorder=z + 0.3, alpha=alfa))


# =========================================================================
# 1. sam-en-vivo.gif
# =========================================================================
N_SAM = 512                       # resolución de trabajo de la escena


def _sam_escena():
    n = N_SAM
    yy, xx = np.mgrid[0:n, 0:n] / n
    img = 0.93 - 0.10 * yy                                # cielo
    suelo = yy > 0.70
    img[suelo] = 0.70 - 0.05 * (yy[suelo] - 0.7)

    def tri(ax_, ay, bx, by, cx, cy):
        d = lambda x1, y1, x2, y2: (xx - x2) * (y1 - y2) - (x1 - x2) * (yy - y2)
        s1, s2, s3 = d(ax_, ay, bx, by), d(bx, by, cx, cy), d(cx, cy, ax_, ay)
        return ~(((s1 < 0) | (s2 < 0) | (s3 < 0))
                 & ((s1 > 0) | (s2 > 0) | (s3 > 0)))

    pared = (xx > 0.08) & (xx < 0.38) & (yy > 0.48) & (yy < 0.76)
    techo = tri(0.04, 0.49, 0.23, 0.30, 0.42, 0.49)
    puerta = (xx > 0.19) & (xx < 0.27) & (yy > 0.60) & (yy < 0.76)
    casa = pared | techo
    tronco = (xx > 0.525) & (xx < 0.565) & (yy > 0.52) & (yy < 0.78)
    copa = ((xx - 0.545) / 0.11) ** 2 + ((yy - 0.42) / 0.14) ** 2 < 1
    arbol = tronco | copa
    carro_c = (xx > 0.66) & (xx < 0.95) & (yy > 0.69) & (yy < 0.80)
    cabina = (xx > 0.71) & (xx < 0.88) & (yy > 0.61) & (yy < 0.70)
    ruedas = (((xx - 0.72) ** 2 + (yy - 0.81) ** 2) < 0.035 ** 2) | \
        (((xx - 0.89) ** 2 + (yy - 0.81) ** 2) < 0.035 ** 2)
    auto = carro_c | cabina | ruedas

    def nube(cx, cy, s):
        m = np.zeros_like(xx, bool)
        for dx, dy, r in ((-0.06, 0.01, 0.045), (0, -0.015, 0.06),
                          (0.065, 0.01, 0.045), (0.0, 0.025, 0.045)):
            m |= ((xx - cx - dx * s) ** 2 + (yy - cy - dy * s) ** 2) < (r * s) ** 2
        return m

    nubes = nube(0.24, 0.14, 1.0) | nube(0.78, 0.22, 0.85)
    img[nubes] = 0.995
    img[casa] = 0.48
    img[techo] = 0.30
    img[puerta] = 0.20
    img[copa] = 0.36
    img[tronco] = 0.24
    img[carro_c | cabina] = 0.40
    img[cabina & (yy > 0.63) & (yy < 0.69) & (np.abs(xx - 0.795) > 0.01)] = 0.80
    img[ruedas] = 0.12
    img = suavizar(img, 1)
    objetos = {"casa": casa, "árbol": arbol, "auto": auto, "nubes": nubes}
    # bordes de las nubes para que se lean sobre el cielo
    borde_n = (suavizar(nubes.astype(float), 2) > 0.05) & ~nubes
    img[borde_n] = np.minimum(img[borde_n], 0.80)
    return np.clip(img, 0, 1), objetos


def _sam_embedding(img, obj):
    """UN canal de 64×64 (de 256): manchas difusas sobre los objetos, de
    distinta intensidad, más una respuesta débil a bordes horizontales. No es
    la imagen achicada: cada celda es una posición del embedding."""
    f = N_SAM // 64
    pesos = {"casa": 1.0, "auto": 0.75, "árbol": 0.35, "nubes": 0.15}
    m = np.zeros((64, 64))
    for k, w in pesos.items():
        m += w * pool(obj[k].astype(float), f)
    for _ in range(9):
        m = conv2(m, np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16)
    p = pool(img, f)
    sob_h = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], float)
    b = np.abs(conv2(p, sob_h))
    b = b / (b.max() + 1e-9)
    for _ in range(2):
        b = conv2(b, np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16)
    b = b / (b.max() + 1e-9)
    a = 0.85 * m / m.max() + 0.25 * b
    a += 0.025 * np.random.default_rng(3).standard_normal(a.shape)
    a = np.clip(a, 0, None)
    return a / a.max()


CELDA = (39, 13)                    # fila, columna de la celda resaltada
VECTOR = np.random.default_rng(11).random(16)


# geometría
IMG_X, IMG_Y, IMG_L = 50, 120, 440
ENC = (545, 120, 330, 170)          # x, y, w, h  image encoder
EMB_L, EMB_DX, EMB_DY = 140, 40, 28
EMB = (ENC[0] + ENC[2] / 2 - (EMB_L + EMB_DX) / 2, 395)
CHIPS_X0, CHIP_W, CHIP_H, CHIP_GAP, CHIPS_Y = 920, 148, 76, 10, 120
_CH_C = CHIPS_X0 + (4 * CHIP_W + 3 * CHIP_GAP) / 2
PENC = (_CH_C - 250, 270, 500, 110)        # prompt encoder
DEC = (780, 590, 520, 110)          # mask decoder
OUTM = (1385, 575, 140)             # máscara de salida (x, y, lado)

PROMPTS = [
    # (chip, objeto, pie)
    ("clic", "casa", "Prompt 1 · clic sobre la casa: prompt encoder + mask "
                     "decoder, el embedding se reutiliza"),
    ("caja", "árbol", "Prompt 2 · caja alrededor del árbol: otra vez solo "
                      "las dos piezas livianas"),
    ("máscara", "auto", "Prompt 3 · máscara aproximada sobre el auto: el "
                        "decoder la ajusta al borde real"),
    ("texto", "nubes", "Prompt 4 · texto \"nube\" (desde SAM 3): devuelve "
                       "todas las nubes de la imagen"),
]


def _sam_cuadro(ax, img, obj, emb, *, enc_t=0.0, enc_estado="idle",
                n_hechos=0, activo=None, fase=None, f=0.0, texto_pie=None,
                cont_enc=0, cont_dec=0):
    """activo: índice del prompt en curso. fase en {'glifo','penc','dec',
    'mask'} y f su avance [0,1]."""
    lienzo(ax)
    # ---- imagen con máscaras --------------------------------------------
    rgb = a_rgb(img)
    for i in range(n_hechos):
        rgb = superponer(rgb, obj[PROMPTS[i][1]], 0.38)
    if activo is not None and fase == "mask":
        rgb = superponer(rgb, obj[PROMPTS[activo][1]], 0.62 * f)
    ax.imshow(rgb, extent=(IMG_X, IMG_X + IMG_L, IMG_Y + IMG_L, IMG_Y),
              interpolation="bilinear", zorder=1)
    ax.add_patch(Rectangle((IMG_X, IMG_Y), IMG_L, IMG_L, fill=False,
                           ec=TINTA, lw=1.8, zorder=5))
    ax.text(IMG_X + IMG_L / 2, IMG_Y - 16, "imagen", ha="center", va="bottom",
            fontsize=24, fontweight="bold", color=TINTA)
    ax.text(IMG_X + IMG_L / 2, IMG_Y + IMG_L + 14, "1024×1024×3", ha="center",
            va="top", fontsize=22, fontweight="bold", color=TINTA)
    for i in range(n_hechos):
        contorno(ax, obj[PROMPTS[i][1]], IMG_X, IMG_Y, IMG_L, lw=1.8)

    # parches del ViT mientras corre el encoder
    if 0 < enc_t < 1:
        filas = int(64 * enc_t)
        c = IMG_L / 64
        ax.add_patch(Rectangle((IMG_X, IMG_Y), IMG_L, filas * c, fc=ROJO,
                               alpha=0.16, ec="none", zorder=4))
        for k in range(0, 65, 4):
            ax.plot([IMG_X + k * c] * 2, [IMG_Y, IMG_Y + IMG_L], color=ROJO,
                    lw=0.7, alpha=0.45, zorder=4)
            ax.plot([IMG_X, IMG_X + IMG_L], [IMG_Y + k * c] * 2, color=ROJO,
                    lw=0.7, alpha=0.45, zorder=4)
        ax.add_patch(Rectangle((IMG_X, IMG_Y + filas * c), IMG_L, c * 4,
                               fc=ROJO, alpha=0.35, ec=ROJO, lw=2, zorder=4))

    # glifo del prompt en curso (y los anteriores en gris)
    def glifo(i, color, alfa=1.0):
        tipo = PROMPTS[i][0]
        X = lambda u: IMG_X + u * IMG_L
        if tipo == "clic":
            ax.plot([X(0.30)], [X(0.0) - IMG_X + IMG_Y + 0.62 * IMG_L], "o",
                    ms=17, mfc=color, mec="white", mew=3, zorder=7,
                    alpha=alfa)
        elif tipo == "caja":
            ax.add_patch(Rectangle((X(0.415), IMG_Y + 0.26 * IMG_L),
                                   0.26 * IMG_L, 0.54 * IMG_L, fill=False,
                                   ec=color, lw=3.2, ls="--", zorder=7,
                                   alpha=alfa))
        elif tipo == "máscara":
            th = np.linspace(0, 2 * np.pi, 80)
            r = 1 + 0.10 * np.sin(3 * th) + 0.06 * np.cos(5 * th)
            xs = X(0.80) + 0.13 * IMG_L * r * np.cos(th)
            ys = IMG_Y + 0.72 * IMG_L + 0.09 * IMG_L * r * np.sin(th)
            ax.fill(xs, ys, fc=color, alpha=0.30 * alfa, ec=color, lw=3,
                    ls="--", zorder=7)
        elif tipo == "texto":
            ax.text(IMG_X + IMG_L - 14, IMG_Y + IMG_L - 14, "“nube”",
                    ha="right", va="bottom", fontsize=26, fontweight="bold",
                    color="white", zorder=8, alpha=alfa,
                    bbox=dict(boxstyle="round,pad=0.35", fc=color, ec="none",
                              alpha=alfa))

    if activo is not None:
        glifo(activo, ROJO)

    # ---- image encoder -------------------------------------------------
    ex, ey, ew, eh = ENC
    flecha(ax, (IMG_X + IMG_L + 8, ey + eh / 2), (ex - 6, ey + eh / 2),
           color=ROJO if enc_estado == "activo" else TINTA,
           lw=3 if enc_estado == "activo" else 2.2)
    caja(ax, ex, ey, ew, eh, "image encoder", "ViT · pesado",
         estado=enc_estado, sub2=None)
    # barra de progreso dentro de la caja
    bx, by, bw, bh = ex + 30, ey + eh - 44, ew - 60, 18
    activo_enc = enc_estado == "activo"
    ax.add_patch(Rectangle((bx, by), bw, bh, fc="white" if activo_enc else
                           "white", ec="white" if activo_enc else BORDE,
                           lw=1.5, zorder=5))
    ax.add_patch(Rectangle((bx, by), bw * enc_t, bh,
                           fc=TINTA if activo_enc else ROJO, ec="none",
                           zorder=6))
    ax.text(ex + ew / 2, ey + eh + 12,
            f"ejecuciones: {cont_enc}", ha="center", va="top", fontsize=22,
            fontweight="bold", color=ROJO if cont_enc else GRIS_MEDIO)

    # ---- embedding: bloque 64×64×256, cara = un canal ------------------
    emx, emy = EMB
    flecha(ax, (ex + ew / 2, ey + eh + 48), (ex + ew / 2, emy - EMB_DY - 6),
           color=ROJO if enc_estado == "activo" else TINTA,
           lw=3 if enc_estado == "activo" else 2.2)
    e_rgb = mapa_rgb(emb)
    if enc_t < 1:
        filas = int(64 * enc_t)
        e_rgb[filas:] = np.array([0xF1, 0xED, 0xEC]) / 255
    reusa = activo is not None and fase == "dec"
    prisma(ax, emx, emy, EMB_L, EMB_DX, EMB_DY, e_rgb,
           borde=ROJO if reusa else TINTA, lw=3.5 if reusa else 1.8, capas=8)
    c = EMB_L / 64
    for k in range(8, 64, 8):                # grilla de posiciones
        ax.plot([emx + k * c] * 2, [emy, emy + EMB_L], color="white",
                lw=0.6, alpha=0.7, zorder=3.25)
        ax.plot([emx, emx + EMB_L], [emy + k * c] * 2, color="white",
                lw=0.6, alpha=0.7, zorder=3.25)
    ax.text(emx - 14, emy + EMB_L / 2, "1 de 256\ncanales", ha="right",
            va="center", fontsize=17, color="#4A4645", linespacing=1.15)
    tx = emx + EMB_L + EMB_DX + 72
    ax.text(tx, emy + 22, "embedding", ha="left", va="center", fontsize=22,
            fontweight="bold", color=TINTA)
    ax.text(tx, emy + 50, "64×64×256", ha="left", va="center", fontsize=22,
            color=TINTA)
    if enc_t >= 1:
        # una celda, sacada como vector de 256 números
        fr, fc = CELDA
        cx, cy = emx + (fc + 0.5) * c, emy + (fr + 0.5) * c
        ax.add_patch(Rectangle((cx - 5, cy - 5), 10, 10, fill=False, ec=ROJO,
                               lw=2.4, zorder=6))
        vx, vy, vw, vh = emx + EMB_L + EMB_DX + 22, emy + 2, 20, 8.6
        for j, v in enumerate(VECTOR):
            ax.add_patch(Rectangle((vx, vy + j * vh), vw, vh,
                                   fc=mapa_rgb(np.array(v)), ec="white",
                                   lw=0.6, zorder=5))
        ax.add_patch(Rectangle((vx, vy), vw, vh * len(VECTOR), fill=False,
                               ec=ROJO, lw=2.2, zorder=6))
        ax.plot([cx + 5, vx], [cy, vy + vh * len(VECTOR) / 2], color=ROJO,
                lw=1.8, ls="--", zorder=6)
        ax.text(tx, emy + 90, "una celda =", ha="left", va="center",
                fontsize=18, color=ROJO)
        ax.text(tx, emy + 114, "embedding de esa", ha="left", va="center",
                fontsize=18, color=ROJO)
        ax.text(tx, emy + 138, "región (256 números)", ha="left",
                va="center", fontsize=18, color=ROJO)

    # ---- chips de prompt + prompt encoder -------------------------------
    for i, (tipo, _, _) in enumerate(PROMPTS):
        x = CHIPS_X0 + i * (CHIP_W + CHIP_GAP)
        est = "activo" if activo == i else ("hecho" if i < n_hechos else
                                            "idle")
        caja(ax, x, CHIPS_Y, CHIP_W, CHIP_H, tipo,
             "desde SAM 3" if tipo == "texto" else None, estado=est, fs=19,
             fs_sub=15)
        cx = x + CHIP_W / 2
        tx = PENC[0] + PENC[2] * (0.14 + 0.24 * i)
        caliente = activo == i and fase in ("penc",)
        flecha(ax, (cx, CHIPS_Y + CHIP_H + 4), (tx, PENC[1] - 6),
               color=ROJO if caliente else TINTA, lw=3 if caliente else 1.8,
               ms=16)
    chips_ancho = 4 * CHIP_W + 3 * CHIP_GAP
    ax.text(CHIPS_X0 + chips_ancho / 2, CHIPS_Y - 16, "prompts",
            ha="center", va="bottom", fontsize=24, fontweight="bold",
            color=TINTA)
    pe_est = "activo" if (activo is not None and fase == "penc") else "idle"
    caja(ax, *PENC, "prompt encoder", "liviano · tokens de 256",
         estado=pe_est)

    # ---- mask decoder ---------------------------------------------------
    dx, dy, dw, dh = DEC
    d_est = "activo" if (activo is not None and fase == "dec") else "idle"
    caliente = activo is not None and fase == "dec"
    flecha(ax, (emx + EMB_L / 2, emy + EMB_L + 4), (emx + EMB_L / 2 + 40,
                                                    dy - 6),
           color=ROJO if caliente else TINTA, lw=3 if caliente else 2.2)
    flecha(ax, (PENC[0] + PENC[2] / 2, PENC[1] + PENC[3] + 4),
           (dx + dw * 0.72, dy - 6), color=ROJO if caliente else TINTA,
           lw=3 if caliente else 2.2)
    caja(ax, dx, dy, dw, dh, "mask decoder", "liviano", estado=d_est)
    ax.text(dx + dw / 2, dy + dh + 12, f"ejecuciones: {cont_dec}",
            ha="center", va="top", fontsize=22, fontweight="bold",
            color=ROJO if cont_dec else GRIS_MEDIO)

    # ---- máscara de salida ----------------------------------------------
    ox, oy, ol = OUTM
    sale = activo is not None and fase == "mask"
    flecha(ax, (dx + dw + 6, dy + dh / 2), (ox - 8, oy + ol / 2),
           color=ROJO if sale else TINTA, lw=3 if sale else 2.2)
    if sale or n_hechos:
        idx = activo if sale else n_hechos - 1
        m = pool(obj[PROMPTS[idx][1]].astype(float), 2) > 0.5   # 256×256
        rgb_m = np.ones((256, 256, 3))
        rgb_m = superponer(rgb_m, m, 1.0 if sale else 0.75)
        ax.imshow(rgb_m, extent=(ox, ox + ol, oy + ol, oy),
                  interpolation="nearest", zorder=4)
    ax.add_patch(Rectangle((ox, oy), ol, ol, fill=False, ec=TINTA, lw=1.8,
                           zorder=5))
    ax.text(ox + ol / 2, oy - 12, "máscara", ha="center", va="bottom",
            fontsize=22, fontweight="bold", color=TINTA)
    ax.text(ox + ol / 2, oy + ol + 12, "256×256\n→ 1024×1024",
            ha="center", va="top", fontsize=19, color=TINTA, linespacing=1.15)

    if texto_pie:
        pie(ax, texto_pie)


def sam_en_vivo(fps=12):
    img, obj = _sam_escena()
    emb = _sam_embedding(img, obj)
    fig, ax = figura()
    frames, durs = [], []
    ms = 1000 / fps

    def add(n=1, **kw):
        _sam_cuadro(ax, img, obj, emb, **kw)
        fr = capturar(fig)
        for _ in range(n):
            frames.append(fr)
            durs.append(ms)

    base = dict(texto_pie="Entrada: una imagen de 1024×1024×3, todavía sin "
                          "codificar")
    add(14, **base)
    # image encoder: lento, una vez
    n_enc = 40
    for k in range(1, n_enc + 1):
        add(1, enc_t=k / n_enc, enc_estado="activo",
            texto_pie="image encoder (ViT): parches de 16×16 → embedding "
                      "64×64×256. Es lo caro")
    pie_listo = ("El embedding queda guardado: el image encoder no vuelve "
                 "a correr")
    add(14, enc_t=1, enc_estado="hecho", cont_enc=1, texto_pie=pie_listo)
    # prompts: rápidos
    for i in range(len(PROMPTS)):
        kw = dict(enc_t=1, enc_estado="hecho", cont_enc=1, n_hechos=i,
                  activo=i, texto_pie=PROMPTS[i][2])
        add(6, fase="glifo", cont_dec=i, **kw)
        add(4, fase="penc", cont_dec=i, **kw)
        add(4, fase="dec", cont_dec=i + 1, **kw)
        for k in range(1, 6):
            add(1, fase="mask", f=k / 5, cont_dec=i + 1, **kw)
        add(9, fase="mask", f=1.0, cont_dec=i + 1, **kw)
    # cuadro final
    _sam_cuadro(ax, img, obj, emb, enc_t=1, enc_estado="hecho", cont_enc=1,
                n_hechos=4, cont_dec=4,
                texto_pie="1 pasada del image encoder, 4 del mask decoder: "
                          "una máscara por prompt")
    final = capturar(fig)
    frames.append(final)
    durs.append(3200)
    plt.close(fig)
    ruta = os.path.join(OUT, "sam-en-vivo.gif")
    guardar_gif_dur(frames, durs, ruta)
    final.save(os.path.join(OUT, "sam-en-vivo.png"))
    if SCRATCH:
        os.makedirs(SCRATCH, exist_ok=True)
        for nombre, i in (("sam-inicio", 0), ("sam-encoder", 30),
                          ("sam-medio", 95)):
            frames[min(i, len(frames) - 1)].save(
                os.path.join(SCRATCH, nombre + ".png"))
        final.save(os.path.join(SCRATCH, "sam-final.png"))


# =========================================================================
# 2. sam2-en-vivo.gif
# =========================================================================
N_V = 256
N_FR = 8


def _sam2_video():
    """Pelota que cruza de izquierda a derecha, pasa detrás de un poste y
    hay otra pelota igual quieta (distractor)."""
    n = N_V
    yy, xx = np.mgrid[0:n, 0:n] / n
    fondo = 0.92 - 0.12 * yy
    piso = yy > 0.72
    fondo[piso] = 0.74
    poste = (xx > 0.53) & (xx < 0.62) & (yy > 0.10)
    frames, mascaras = [], []
    dist_c = (0.80, 0.30)
    for t in range(N_FR):
        cx = 0.16 + t * (0.64 / (N_FR - 1))
        cy = 0.60 - 0.22 * np.sin(np.pi * t / (N_FR - 1))
        pel = ((xx - cx) ** 2 + (yy - cy) ** 2) < 0.095 ** 2
        dist = ((xx - dist_c[0]) ** 2 + (yy - dist_c[1]) ** 2) < 0.075 ** 2
        img = fondo.copy()
        img[dist] = 0.42
        img[pel] = 0.30
        franja = pel & (np.abs((xx - cx) + (yy - cy)) < 0.025)
        img[franja] = 0.62
        img[poste] = 0.18
        visible = pel & ~poste
        frames.append(np.clip(suavizar(img, 1), 0, 1))
        mascaras.append(visible)
    # memoria de cada frame (memory encoder): UN canal de 32×32 de los 64;
    # alto donde está el objeto enmascarado, débil en los bordes del frame
    sob = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], float)
    mems = []
    for img, m in zip(frames, mascaras):
        a = pool(m.astype(float), N_V // 32)
        for _ in range(6):
            a = conv2(a, np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16)
        p = pool(img, N_V // 32)
        b = np.hypot(conv2(p, sob), conv2(p, sob.T))
        b = conv2(b, np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16)
        a = 0.9 * (a / (a.max() + 1e-9)) ** 0.7 + 0.22 * b / (b.max() + 1e-9)
        mems.append(np.clip(a / a.max(), 0, 1))
    return frames, mascaras, mems


# geometría SAM 2
FS_L, FS_GAP, FS_Y = 140, 30, 40
FS_X0 = (PX_W - (N_FR * FS_L + (N_FR - 1) * FS_GAP)) / 2
P_Y, P_H = 280, 110                        # fila del pipeline
TH = 110                                   # miniaturas frame t / máscara t
_ANCHOS = [TH, 280, 340, 280, TH]
_G = (PX_W - 2 * 80 - sum(_ANCHOS)) / 4
_XS = [80 + sum(_ANCHOS[:i]) + i * _G for i in range(5)]
FT_X = _XS[0]
IE = (_XS[1], P_Y, 280, P_H)
MA = (_XS[2], P_Y, 340, P_H)
MD = (_XS[3], P_Y, 280, P_H)
MT_X = _XS[4]
PE = (MD[0] + MD[2] / 2 - 155, 445, 310, 92)
ME = (PX_W - 50 - 310, 635, 310, 100)
SLOTS, SLOT_L, SLOT_PITCH = 7, 76, 124
SLOT_DX, SLOT_DY = 16, 11
MB_W = 24 + SLOTS * SLOT_PITCH + 24
MB = (160, 580, MB_W, 212)


def _sam2_cuadro(ax, frs, mks, t, fase, f=0.0, banco=(), texto_pie=None,
                 hechos=0, final=False, mems=None):
    """t: frame en curso (0..7). fase in {'enc','att','dec','menc','guardar',
    'prompt', None}. banco: lista de índices de frame guardados."""
    lienzo(ax)
    # ---- tira de frames --------------------------------------------------
    for i in range(N_FR):
        x = FS_X0 + i * (FS_L + FS_GAP)
        rgb = a_rgb(frs[i])
        if i < hechos or (i == t and fase in ("dec", "menc", "guardar")):
            rgb = superponer(rgb, mks[i], 0.6)
        ax.imshow(rgb, extent=(x, x + FS_L, FS_Y + FS_L, FS_Y),
                  interpolation="bilinear", zorder=1)
        actual = (i == t) and not final
        ax.add_patch(Rectangle((x, FS_Y), FS_L, FS_L, fill=False,
                               ec=ROJO if actual else TINTA,
                               lw=4.5 if actual else 1.5, zorder=5))
        ax.text(x + FS_L / 2, FS_Y + FS_L + 8, f"t = {i + 1}", ha="center",
                va="top", fontsize=20, fontweight="bold" if actual else
                "normal", color=ROJO if actual else TINTA)
        if i == 0:                               # el clic del frame 1
            ax.plot([x + FS_L * 0.16], [FS_Y + FS_L * 0.60], "o", ms=11,
                    mfc=ROJO, mec="white", mew=2.5, zorder=7)
    ax.text(FS_X0 - 16, FS_Y + FS_L / 2, "video", ha="right", va="center",
            fontsize=22, fontweight="bold", color=TINTA, rotation=90)

    t_vis = N_FR - 1 if final else t
    # ---- frame t ---------------------------------------------------------
    ty = P_Y + P_H / 2 - TH / 2
    ax.imshow(a_rgb(frs[t_vis]), extent=(FT_X, FT_X + TH, ty + TH, ty),
              interpolation="bilinear", zorder=1)
    ax.add_patch(Rectangle((FT_X, ty), TH, TH, fill=False,
                           ec=ROJO if fase == "enc" else TINTA,
                           lw=3 if fase == "enc" else 1.8, zorder=5))
    if t_vis == 0:
        ax.plot([FT_X + TH * 0.16], [ty + TH * 0.60], "o", ms=10, mfc=ROJO,
                mec="white", mew=2.5, zorder=7)
    ax.text(FT_X + TH / 2, ty - 10, f"frame {t_vis + 1}", ha="center",
            va="bottom", fontsize=22, fontweight="bold", color=TINTA)

    def est(nombre):
        return "activo" if (fase == nombre and not final) else "idle"

    cy = P_Y + P_H / 2
    fs_c = 22
    flecha(ax, (FT_X + TH + 6, cy), (IE[0] - 6, cy),
           color=ROJO if fase == "enc" else TINTA)
    caja(ax, *IE, "image encoder", "→ 64×64×256", estado=est("enc"), fs=fs_c)
    flecha(ax, (IE[0] + IE[2] + 6, cy), (MA[0] - 6, cy),
           color=ROJO if fase == "att" else TINTA)
    lee = len(banco) > 0
    caja(ax, *MA, "memory attention",
         ("lee del memory bank" if lee or final else "memoria vacía"),
         estado=est("att"), fs=fs_c)
    flecha(ax, (MA[0] + MA[2] + 6, cy), (MD[0] - 6, cy),
           color=ROJO if fase == "dec" else TINTA)
    caja(ax, *MD, "mask decoder", estado=est("dec"), fs=fs_c)
    flecha(ax, (MD[0] + MD[2] + 6, cy), (MT_X - 6, cy),
           color=ROJO if fase == "dec" else TINTA)
    # máscara t
    hay_m = fase in ("dec", "menc", "guardar") or final
    rgb = np.ones((N_V, N_V, 3))
    if hay_m:
        rgb = superponer(rgb, mks[t_vis], 1.0)
    ax.imshow(rgb, extent=(MT_X, MT_X + TH, ty + TH, ty),
              interpolation="nearest", zorder=1)
    ax.add_patch(Rectangle((MT_X, ty), TH, TH, fill=False, ec=TINTA, lw=1.8,
                           zorder=5))
    ax.text(MT_X + TH / 2, ty - 10, f"máscara {t_vis + 1}", ha="center",
            va="bottom", fontsize=22, fontweight="bold", color=TINTA)

    # ---- prompt encoder (solo frame 1) ----------------------------------
    con_prompt = (t == 0) or final
    pe_est = "activo" if (fase == "prompt" and not final) else \
        ("idle" if con_prompt else "apagado")
    caja(ax, *PE, "prompt encoder",
         "clic en el frame 1" if con_prompt else "sin prompt",
         estado=pe_est, fs=22, fs_sub=18)
    flecha(ax, (PE[0] + PE[2] / 2, PE[1] - 4),
           (PE[0] + PE[2] / 2, P_Y + P_H + 6),
           color=ROJO if fase == "prompt" else (TINTA if con_prompt
                                                else APAGADO))

    # ---- memory encoder --------------------------------------------------
    mx = MT_X + TH / 2
    flecha(ax, (mx, ty + TH + 6), (mx, ME[1] - 6),
           color=ROJO if fase == "menc" else TINTA)
    caja(ax, *ME, "memory encoder", "→ 64×64×64", estado=est("menc"),
         fs=fs_c)

    # ---- memory bank: bloques de memoria (no miniaturas del frame) -------
    bx, by, bw, bh = MB
    bank_act = fase == "att" and lee and not final
    ax.add_patch(FancyBboxPatch((bx, by), bw, bh, boxstyle="round,pad=0,"
                                "rounding_size=14", fc=RELLENO,
                                ec=ROJO if bank_act else BORDE,
                                lw=4 if bank_act else 2, zorder=2))
    ax.text(bx + 24, by + 16, "memory bank", ha="left", va="top",
            fontsize=fs_c, fontweight="bold", color=TINTA, zorder=4)
    ax.text(bx + bw - 24, by + 20, "frame con prompt + 6 recientes",
            ha="right", va="top", fontsize=18, color="#4A4645", zorder=4)
    sy = by + 72

    def slot_x(s_):
        return bx + 24 + s_ * SLOT_PITCH + (SLOT_PITCH - SLOT_L - SLOT_DX) / 2

    for s_ in range(SLOTS):
        ax.add_patch(Rectangle((slot_x(s_), sy), SLOT_L, SLOT_L, fc="white",
                               ec=BORDE, lw=1.5, ls="--", zorder=3))
    # slot 0: frame con prompt; slots 1..6: recientes en orden
    if banco:
        orden = [banco[0]] + list(banco[1:])[-6:]
        for s_, fi in enumerate(orden):
            sx = slot_x(s_)
            nuevo = (fase == "guardar" and fi == t and not final)
            a = f if nuevo else 1.0
            rojo = s_ == 0 or nuevo
            prisma(ax, sx, sy, SLOT_L, SLOT_DX, SLOT_DY, mapa_rgb(mems[fi]),
                   borde=ROJO if rojo else TINTA, lw=3 if rojo else 1.5,
                   capas=4, alfa=max(a, 0.05), z=4)
            ax.text(sx + (SLOT_L + SLOT_DX) / 2, sy + SLOT_L + 8,
                    f"memoria\nframe {fi + 1}", ha="center", va="top",
                    fontsize=16, color=ROJO if s_ == 0 else TINTA,
                    linespacing=1.1, zorder=5, alpha=max(a, 0.05))
    # memory encoder → bank ("se guarda")
    g = fase == "guardar" and not final
    ya = ME[1] + ME[3] / 2
    flecha(ax, (ME[0] - 6, ya), (bx + bw + 6, ya), color=ROJO,
           lw=3.8 if g else 2.4)
    ax.text((ME[0] + bx + bw) / 2, ya - 10, "se guarda", ha="center",
            va="bottom", fontsize=19, color=ROJO,
            fontweight="bold" if g else "normal")
    # bank → memory attention ("condiciona el frame siguiente")
    at = fase == "att" and lee and not final
    xa = MA[0] + MA[2] / 2
    flecha(ax, (xa, by - 6), (xa, P_Y + P_H + 6), color=ROJO,
           lw=3.8 if at else 2.4)
    ax.text(xa - 16, (by + P_Y + P_H) / 2, "condiciona\nel frame\nsiguiente",
            ha="right", va="center", fontsize=19, color=ROJO,
            linespacing=1.15, fontweight="bold" if at else "normal")

    if texto_pie:
        pie(ax, texto_pie)


def sam2_en_vivo(fps=12):
    frs, mks, mems = _sam2_video()
    fig, ax = figura()
    frames, durs = [], []
    ms = 1000 / fps

    def add(n=1, **kw):
        _sam2_cuadro(ax, frs, mks, mems=mems, **kw)
        fr = capturar(fig)
        for _ in range(n):
            frames.append(fr)
            durs.append(ms)

    banco = []
    for t in range(N_FR):
        b = tuple(banco)
        if t == 0:
            add(8, t=0, fase=None, banco=b,
                texto_pie="Frame 1: el único con prompt, un clic sobre la "
                          "pelota")
            add(5, t=0, fase="enc", banco=b, hechos=t,
                texto_pie="image encoder: frame de 1024×1024×3 → "
                          "64×64×256")
            add(5, t=0, fase="prompt", banco=b, hechos=t,
                texto_pie="prompt encoder: el clic dice cuál es el objeto")
            add(4, t=0, fase="att", banco=b, hechos=t,
                texto_pie="memory attention: el banco todavía está vacío")
            add(6, t=0, fase="dec", banco=b, hechos=t,
                texto_pie="mask decoder: sale la máscara de la pelota")
            add(4, t=0, fase="menc", banco=b, hechos=t,
                texto_pie="memory encoder: máscara + features → memoria "
                          "64×64×64")
            banco.append(t)
            for k in range(1, 4):
                add(1, t=0, fase="guardar", f=k / 3, banco=tuple(banco),
                    hechos=t, texto_pie="La memoria del frame 1 se guarda en "
                                        "el memory bank")
            add(4, t=0, fase="guardar", f=1, banco=tuple(banco), hechos=t,
                texto_pie="La memoria del frame 1 se guarda en el memory "
                          "bank")
            continue
        if t == 1:
            p_att = ("Frame 2, sin prompt: memory attention lee del banco "
                     "dónde estaba la pelota")
        elif t in (3, 4):
            p_att = (f"Frame {t + 1}: la pelota pasa detrás del poste; la "
                     "memoria la sigue igual")
        elif t == 2:
            p_att = ("Frame 3: hay otra pelota parecida, pero la memoria "
                     "dice cuál es la nuestra")
        else:
            p_att = (f"Frame {t + 1}: memory attention cruza el frame con "
                     f"{len(b)} memorias guardadas")
        pie_dec = p_att
        add(3, t=t, fase="enc", banco=b, hechos=t, texto_pie=p_att)
        add(4, t=t, fase="att", banco=b, hechos=t, texto_pie=p_att)
        add(4, t=t, fase="dec", banco=b, hechos=t, texto_pie=pie_dec)
        add(2, t=t, fase="menc", banco=b, hechos=t, texto_pie=pie_dec)
        banco.append(t)
        pie_g = pie_dec
        if len(banco) > 7:
            pie_g = (f"Banco lleno: entra la memoria del frame {t + 1}, sale "
                     f"la del frame {banco[-7] + 1}; el frame 1 se queda")
        for k in range(1, 3):
            add(1, t=t, fase="guardar", f=k / 2, banco=tuple(banco),
                hechos=t, texto_pie=pie_g)
        add(6 if len(banco) > 7 else 2, t=t, fase="guardar", f=1,
            banco=tuple(banco), hechos=t, texto_pie=pie_g)
    # final
    _sam2_cuadro(ax, frs, mks, mems=mems, t=N_FR - 1, fase=None,
                 banco=tuple(banco),
                 hechos=N_FR, final=True,
                 texto_pie="Un solo clic en el frame 1: la memoria sigue a la "
                           "pelota los 8 frames")
    final = capturar(fig)
    frames.append(final)
    durs.append(3200)
    plt.close(fig)
    guardar_gif_dur(frames, durs, os.path.join(OUT, "sam2-en-vivo.gif"))
    final.save(os.path.join(OUT, "sam2-en-vivo.png"))
    if SCRATCH:
        os.makedirs(SCRATCH, exist_ok=True)
        for nombre, i in (("sam2-inicio", 10), ("sam2-medio", 75),
                          ("sam2-oclusion", 85)):
            frames[min(i, len(frames) - 1)].save(
                os.path.join(SCRATCH, nombre + ".png"))
        final.save(os.path.join(SCRATCH, "sam2-final.png"))


TAREAS = {"sam-en-vivo": sam_en_vivo, "sam2-en-vivo": sam2_en_vivo}

if __name__ == "__main__":
    for nombre in (sys.argv[1:] or TAREAS):
        TAREAS[nombre]()
