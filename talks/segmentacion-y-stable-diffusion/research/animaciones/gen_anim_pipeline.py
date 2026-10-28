#!/usr/bin/env python3
"""Animación del pipeline de inferencia de Stable Diffusion (grupo "pipeline").

Salida en ../../images/:
  pipeline-sd-en-vivo.gif   recorrido completo: prompt -> tokenizer -> CLIP ->
                            embedding 77x768; seed -> latente 64x64x4; bucle de
                            denoising (U-Net + scheduler) con contador t = 50..1;
                            VAE decoder -> imagen 512x512x3
  pipeline-sd-en-vivo.png   cuadro final fijo (respaldo para PDF)

Todo es sintético (numpy): la imagen "un faro rojo junto al mar" se dibuja con
máscaras, el latente 64x64x4 es una codificación lineal de esa imagen (luminancia,
dos diferencias de color y detalle), y la trayectoria del latente es la de DDIM con
el schedule de SD (betas "scaled linear" 0.00085 -> 0.012, 1000 timesteps, 50 pasos)
usando como predicción de ruido el ruido verdadero (U-Net ideal).

Uso: ~/miniconda3/bin/python3 gen_anim_pipeline.py   (numpy, matplotlib, pillow;
el python3 del sistema no tiene numpy). ~1 min. ANIM_SOLO=5,40,-1 y
ANIM_DEBUG_DIR=<carpeta> renderizan solo esos estados, para revisar el layout.
"""
import os
import sys

import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import gen_animaciones_conv as base  # noqa: E402  (estilo y helpers de GIF)

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402
from PIL import Image  # noqa: E402

TINTA, ROJO, ROJO_CLARO = base.TINTA, base.ROJO, base.ROJO_CLARO
RELLENO, GRIS_MEDIO = base.RELLENO, base.GRIS_MEDIO
OUT = base.OUT
W, H, DPI = 16, 9, 100
PX_W, PX_H = W * DPI, H * DPI
ROSA_BUCLE = "#FCF1F2"
BORDE_GRIS = "#CFC8C6"

PROMPT = "un faro rojo junto al mar"
PROMPT_LINEAS = ("«un faro rojo", "junto al mar»")

# ------------------------------------------------------------------ datos
def imagen_faro(n=512):
    """Imagen sintética 512x512x3 en [0,1] coherente con el prompt."""
    yy, xx = np.mgrid[0:n, 0:n] / n
    img = np.zeros((n, n, 3))
    hor = 0.58
    # cielo: celeste arriba, cálido cerca del horizonte
    t = np.clip(yy / hor, 0, 1)[..., None]
    arriba = np.array([0.42, 0.66, 0.90])
    abajo = np.array([0.98, 0.84, 0.66])
    img[:] = arriba * (1 - t ** 1.6) + abajo * t ** 1.6
    # sol
    d = np.hypot(xx - 0.24, yy - 0.40)
    sol = np.clip((0.075 - d) / 0.006, 0, 1)[..., None]
    img = img * (1 - sol) + np.array([1.0, 0.93, 0.62]) * sol
    # mar
    mar = yy > hor
    prof = np.clip((yy - hor) / (1 - hor), 0, 1)
    ola = 0.035 * np.sin(2 * np.pi * (xx * 9 + yy * 40)) * (1 - prof)
    col_mar = (np.array([0.20, 0.44, 0.66]) * (1 - prof[..., None])
               + np.array([0.06, 0.20, 0.38]) * prof[..., None])
    img[mar] = (col_mar + ola[..., None])[mar]
    # reflejo del sol
    refl = mar & (np.abs(xx - 0.24) < 0.05 * (1 - prof) + 0.01) & \
        (np.sin(2 * np.pi * yy * 60) > 0.3)
    img[refl] = img[refl] * 0.4 + np.array([1.0, 0.90, 0.60]) * 0.6
    # roca / islote
    roca = (((xx - 0.70) / 0.26) ** 2 + ((yy - 0.74) / 0.16) ** 2 < 1) & \
        (yy > 0.60)
    img[roca] = np.array([0.30, 0.27, 0.25]) + 0.08 * (yy[roca] - 0.6)[:, None]
    # torre del faro (tronco de cono) con franjas blancas
    y_top, y_bot = 0.24, 0.64
    tt = (yy - y_top) / (y_bot - y_top)
    semi = 0.040 + 0.030 * tt
    torre = (np.abs(xx - 0.70) < semi) & (yy > y_top) & (yy < y_bot)
    franja = (np.floor(tt * 5) % 2 == 1)
    sombra = 0.82 + 0.18 * ((xx - 0.70) < 0)
    rojo = np.array([0.84, 0.10, 0.16])
    blanco = np.array([0.97, 0.96, 0.94])
    c_torre = np.where(franja[..., None], blanco, rojo) * sombra[..., None]
    img[torre] = c_torre[torre]
    # linterna y techo
    lint = (np.abs(xx - 0.70) < 0.036) & (yy > 0.18) & (yy < 0.24)
    img[lint] = np.array([1.0, 0.92, 0.45])
    techo = (yy > 0.12) & (yy < 0.18) & \
        (np.abs(xx - 0.70) < 0.050 * (yy - 0.12) / 0.06)
    img[techo] = np.array([0.22, 0.20, 0.20])
    galeria = (np.abs(xx - 0.70) < 0.052) & (yy > 0.235) & (yy < 0.25)
    img[galeria] = np.array([0.22, 0.20, 0.20])
    # haz de luz
    ang = np.arctan2(yy - 0.21, xx - 0.70)
    haz = (np.abs(ang - np.pi) < 0.10) & (xx < 0.66) & (yy < hor)
    img[haz] = img[haz] * 0.55 + np.array([1.0, 0.97, 0.80]) * 0.45
    # suavizado leve (anti-alias)
    pil = Image.fromarray((np.clip(img, 0, 1) * 255).astype(np.uint8))
    pil = pil.resize((n * 2, n * 2), Image.BICUBIC).resize((n, n),
                                                           Image.LANCZOS)
    return np.asarray(pil) / 255.0


def codificar(img512):
    """'Encoder' lineal ilustrativo: 512x512x3 -> 64x64x4 (bloques de 8x8)."""
    p = img512.reshape(64, 8, 64, 8, 3).mean((1, 3))
    r, g, b = p[..., 0], p[..., 1], p[..., 2]
    lum = (r + g + b) / 3
    a = r - g
    bb = (r + g) / 2 - b
    blur = (np.roll(lum, 1, 0) + np.roll(lum, -1, 0) + np.roll(lum, 1, 1)
            + np.roll(lum, -1, 1)) / 4
    det = lum - blur
    ch = np.stack([lum, a, bb, det], -1)
    mu, sd = ch.mean((0, 1)), ch.std((0, 1)) + 1e-9
    return (ch - mu) / sd, (mu, sd)


def vista_rgb(lat, stats):
    """Vista previa lineal del latente (64x64x3), la inversa exacta para x0."""
    mu, sd = stats
    ch = lat * sd + mu
    lum, a, bb = ch[..., 0], ch[..., 1], ch[..., 2]
    s = 3 * lum
    b = (s - 2 * bb) / 3
    rg = s - b
    r = (rg + a) / 2
    g = (rg - a) / 2
    return np.clip(np.stack([r, g, b], -1), 0, 1)


def schedule_sd():
    betas = np.linspace(0.00085 ** 0.5, 0.012 ** 0.5, 1000) ** 2
    abar = np.cumprod(1 - betas)
    # paso s = 50..1  ->  timestep T = 20*(s-1)+1  (981, 961, ..., 1)
    ab = {s: abar[20 * (s - 1) + 1] for s in range(1, 51)}
    ab[0] = 1.0
    return ab


def tira_embedding(rng):
    return np.tanh(rng.standard_normal((12, 77)) * 0.9)


# ------------------------------------------------------------------ dibujo
class Escena:
    # columnas y bandas (px, y hacia abajo)
    BANDA = (40, 160)
    PROMPT = (50, 300)
    TOK = (345, 545)
    CLIP = (590, 890)
    EMB = (935, 1110)
    CONT = (1150, 1550)
    BUCLE = (345, 1110, 200, 800)
    LAT = (385, 565, 425, 605)        # latente x_t dentro del bucle
    UNET = (640, 1080, 250, 370)
    EPS = (800, 920, 455, 575)
    SCHED = (640, 1080, 640, 760)
    SEED = (95, 265, 290, 350)
    PILA = (78, 392)                  # x0, y0 de la pila de 4 canales
    CARTA, OFF = 150, 18
    IMG = (1170, 1530, 230, 590)
    VAE = (1150, 1550, 650, 760)

    def __init__(self):
        rng = np.random.default_rng(42)          # la "seed"
        self.img = imagen_faro()
        self.x0, self.stats = codificar(self.img)
        self.eps = rng.standard_normal((64, 64, 4))
        self.ab = schedule_sd()
        self.emb = tira_embedding(np.random.default_rng(768))

    def latente(self, s):
        """Latente tras llegar al paso s (s=50: ruido puro; s=0: final)."""
        a = self.ab[s]
        return np.sqrt(a) * self.x0 + np.sqrt(1 - a) * self.eps

    # -- primitivas --------------------------------------------------------
    def caja(self, ax, x0, x1, y0, y1, fc, ec, lw=2.0, ls="-", r=14, z=2):
        ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0,
                                    boxstyle=f"round,pad=0,rounding_size={r}",
                                    fc=fc, ec=ec, lw=lw, ls=ls, zorder=z))

    def halo(self, ax, x0, x1, y0, y1):
        for pad, al in ((14, 0.35), (7, 0.6)):
            ax.add_patch(FancyBboxPatch(
                (x0 - pad, y0 - pad), x1 - x0 + 2 * pad, y1 - y0 + 2 * pad,
                boxstyle=f"round,pad=0,rounding_size={14 + pad}",
                fc=ROJO_CLARO, ec="none", alpha=al, zorder=1))

    def flecha(self, ax, pts, on=False, lw=2.2):
        col = ROJO if on else TINTA
        lw = 3.4 if on else lw
        xs, ys = zip(*pts)
        if len(pts) > 2:
            ax.plot(xs[:-1], ys[:-1], color=col, lw=lw, zorder=3,
                    solid_capstyle="butt")
        ax.annotate("", xy=pts[-1], xytext=pts[-2], zorder=3,
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=lw,
                                    mutation_scale=24, shrinkA=0, shrinkB=0))

    def texto(self, ax, x, y, s, fs=19, **kw):
        kw.setdefault("ha", "center")
        kw.setdefault("va", "center")
        kw.setdefault("color", TINTA)
        ax.text(x, y, s, fontsize=fs, zorder=6, **kw)

    def imagen(self, ax, arr, x0, x1, y0, y1, interp="nearest", z=4):
        ax.imshow(arr, extent=(x0, x1, y1, y0), interpolation=interp,
                  zorder=z, aspect="auto")

    # -- escena completa ----------------------------------------------------
    def dibujar(self, st):
        fig = plt.figure(figsize=(W, H), dpi=DPI)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, PX_W)
        ax.set_ylim(PX_H, 0)
        ax.axis("off")
        act = st.get("activos", set())
        fin = st.get("final", False)
        ym = sum(self.BANDA) / 2
        y0b, y1b = self.BANDA

        # ---------------- banda del texto ----------------
        x0, x1 = self.PROMPT
        on = "prompt" in act
        if on:
            self.halo(ax, x0, x1, y0b, y1b)
        self.caja(ax, x0, x1, y0b, y1b, "white", ROJO if on else TINTA,
                  lw=3.5 if on else 2.4, r=55)
        self.texto(ax, (x0 + x1) / 2, y0b + 30, "prompt", fs=19,
                   fontweight="bold")
        nch = st.get("prompt_chars", len(PROMPT) + 2)
        l1, l2 = PROMPT_LINEAS
        t1 = l1[:nch]
        t2 = l2[:max(0, nch - len(l1))]
        self.texto(ax, (x0 + x1) / 2, y0b + 64, t1 if t1 else " ", fs=19,
                   style="italic")
        self.texto(ax, (x0 + x1) / 2, y0b + 96, t2 if t2 else " ", fs=19,
                   style="italic")

        def caja_pieza(nombre, xr, titulo, sub, gris=True):
            x0, x1 = xr
            on = nombre in act
            if on:
                self.halo(ax, x0, x1, y0b, y1b)
            fc = RELLENO if gris else "white"
            self.caja(ax, x0, x1, y0b, y1b, fc,
                      ROJO if on else BORDE_GRIS, lw=3.5 if on else 2.0)
            self.texto(ax, (x0 + x1) / 2, ym - 20, titulo, fs=20,
                       fontweight="bold", color=ROJO if on else TINTA)
            self.texto(ax, (x0 + x1) / 2, ym + 22, sub, fs=18)

        caja_pieza("tok", self.TOK, "tokenizer",
                   "77 tokens" if st.get("tok_hecho") else "texto → ids",
                   gris=False)
        caja_pieza("clip", self.CLIP, "CLIP text encoder", "~123M parámetros",
                   gris=True)
        # (el título va en dos líneas; subtítulo abajo)
        # embedding: caja punteada con la tira de valores
        x0, x1 = self.EMB
        on = "emb" in act
        self.caja(ax, x0, x1, y0b, y1b, "white", ROJO if on else BORDE_GRIS,
                  lw=3 if on else 2.0, ls=(0, (5, 4)))
        self.texto(ax, (x0 + x1) / 2, y0b + 24, "embedding", fs=19)
        cols = st.get("emb_cols", 77)
        tira = np.ones((12, 77, 3)) * np.array([0xF1, 0xED, 0xEC]) / 255
        if cols > 0:
            v = self.emb[:, :cols]
            blanco = np.ones(3)
            r_ = np.array([0xD7, 0x19, 0x2A]) / 255
            t_ = np.array([0x22, 0x22, 0x22]) / 255
            pos = np.clip(v, 0, 1)[..., None]
            neg = np.clip(-v, 0, 1)[..., None]
            tira[:, :cols] = blanco + pos * (r_ - blanco) + neg * 0.8 * (
                t_ - blanco)
        self.imagen(ax, tira, x0 + 18, x1 - 18, y0b + 44, y0b + 80)
        ax.add_patch(Rectangle((x0 + 18, y0b + 44), x1 - x0 - 36, 36,
                               fill=False, ec=BORDE_GRIS, lw=1, zorder=5))
        self.texto(ax, (x0 + x1) / 2, y0b + 100, "77 × 768", fs=20,
                   family="DejaVu Sans Mono", color=ROJO if on else TINTA)

        fl = st.get("flechas", set())
        self.flecha(ax, [(self.PROMPT[1], ym), (self.TOK[0] - 2, ym)],
                    "p-t" in fl)
        self.flecha(ax, [(self.TOK[1], ym), (self.CLIP[0] - 2, ym)],
                    "t-c" in fl)
        self.flecha(ax, [(self.CLIP[1], ym), (self.EMB[0] - 2, ym)],
                    "c-e" in fl)

        # ---------------- contador (arriba a la derecha) ----------------
        x0, x1 = self.CONT
        cnt = st.get("t")
        self.caja(ax, x0, x1, y0b, y1b, "white",
                  ROJO if "cont" in act else BORDE_GRIS,
                  lw=3 if "cont" in act else 2.0)
        if cnt is None:
            s1, col = "t = 50", BORDE_GRIS
            s2 = "el bucle todavía no arrancó"
        elif cnt == 0:
            s1, col = "t = 1  ✓", TINTA
            s2 = "50 de 50 pasos hechos"
        else:
            s1, col = f"t = {cnt}", ROJO
            s2 = f"paso {51 - cnt} de 50"
        self.texto(ax, (x0 + x1) / 2, ym - 16, s1, fs=34, fontweight="bold",
                   color=col, family="DejaVu Sans Mono")
        self.texto(ax, (x0 + x1) / 2, ym + 34, s2, fs=18, color=GRIS_MEDIO
                   if cnt is None else TINTA)

        # ---------------- columna izquierda: seed + latente inicial ------
        x0, x1, y0, y1 = (*self.SEED[:2], *self.SEED[2:])
        on = "seed" in act
        if on:
            self.halo(ax, x0, x1, y0, y1)
        self.caja(ax, x0, x1, y0, y1, "#F8D7DA", ROJO if on else "#F0A9B0",
                  lw=3 if on else 2, r=30)
        self.texto(ax, (x0 + x1) / 2, (y0 + y1) / 2, "seed = 42", fs=19,
                   fontweight="bold")
        cx = (x0 + x1) / 2
        self.flecha(ax, [(cx, y1), (cx, self.PILA[1] - 4)], "s-r" in fl)
        nc = st.get("cartas", 4)
        px, py = self.PILA
        L, o = self.CARTA, self.OFF
        for k in range(4):        # la carta 0 adelante
            j = 3 - k
            xx, yy = px + j * o, py + (3 - j) * o
            self.caja(ax, xx, xx + L, yy, yy + L, RELLENO, BORDE_GRIS, lw=1.5,
                      r=2, z=2 + k * 0.01)
            if j < nc:
                g = np.clip(0.5 + 0.22 * self.eps[..., j], 0, 1)
                self.imagen(ax, np.repeat(g[..., None], 3, 2), xx, xx + L,
                            yy, yy + L, z=4 + k * 0.01)
                ax.add_patch(Rectangle((xx, yy), L, L, fill=False, ec=TINTA,
                                       lw=1.4, zorder=4.005 + k * 0.01))
        ytxt = py + L + 3 * o + 34
        self.texto(ax, px + (L + 3 * o) / 2, ytxt, "latente inicial", fs=19)
        self.texto(ax, px + (L + 3 * o) / 2, ytxt + 34, "64×64×4", fs=20,
                   family="DejaVu Sans Mono",
                   color=ROJO if "seed" in act else TINTA)
        self.texto(ax, px + (L + 3 * o) / 2, ytxt + 68,
                   "ruido de una normal", fs=17, color=GRIS_MEDIO)

        # ---------------- bucle de denoising ----------------
        bx0, bx1, by0, by1 = self.BUCLE
        self.caja(ax, bx0, bx1, by0, by1, ROSA_BUCLE, ROJO, lw=3, r=22, z=0.5)
        self.texto(ax, bx0 + 22, by0 + 28, "Bucle de denoising  (~50 pasos)",
                   fs=19, fontweight="bold", color=ROJO, ha="left")
        # entrada del latente inicial al bucle
        lx0, lx1, ly0, ly1 = self.LAT
        lyc = (ly0 + ly1) / 2
        self.flecha(ax, [(px + L + 3 * o + 2, lyc), (lx0 - 3, lyc)],
                    "r-l" in fl)
        # latente x_t
        on = "lat" in act
        lat = st.get("lat")
        if on:
            self.halo(ax, lx0, lx1, ly0, ly1)
        ax.add_patch(Rectangle((lx0, ly0), lx1 - lx0, ly1 - ly0, fc="white",
                               ec=BORDE_GRIS, lw=1.5, ls=(0, (5, 4)),
                               zorder=2))
        if lat is not None:
            self.imagen(ax, vista_rgb(lat, self.stats), lx0, lx1, ly0, ly1)
            ax.add_patch(Rectangle((lx0, ly0), lx1 - lx0, ly1 - ly0,
                                   fill=False, ec=ROJO if on else TINTA,
                                   lw=3 if on else 1.6, zorder=5))
        lcx = (lx0 + lx1) / 2
        self.texto(ax, lcx, ly0 - 60, "latente x_t", fs=19,
                   fontweight="bold" if on else "normal",
                   color=ROJO if on else TINTA)
        self.texto(ax, lcx, ly0 - 27, "64×64×4", fs=20,
                   family="DejaVu Sans Mono")
        xret = lx0 + 40                      # vuelta del bucle (entra abajo)
        self.texto(ax, xret + 18, ly1 + 22, "vista decodificada", fs=16,
                   color=GRIS_MEDIO, ha="left")

        # U-Net
        ux0, ux1, uy0, uy1 = self.UNET
        on = "unet" in act
        if on:
            self.halo(ax, ux0, ux1, uy0, uy1)
        if on or fin:
            self.caja(ax, ux0, ux1, uy0, uy1, ROJO, ROJO, lw=2.5)
            ct, cs = "white", "white"
        else:
            self.caja(ax, ux0, ux1, uy0, uy1, ROJO_CLARO, "#E58E97", lw=2)
            ct, cs = ROJO, TINTA
        ucx = (ux0 + ux1) / 2
        self.texto(ax, ucx, uy0 + 38, "U-Net predice el ruido", fs=21,
                   fontweight="bold", color=ct)
        self.texto(ax, ucx, uy0 + 84, "(latente, t, embedding)", fs=19,
                   color=cs)
        # embedding -> U-Net
        ex = sum(self.EMB) / 2
        self.flecha(ax, [(ex, y1b), (ex, uy0 - 3)], "e-u" in fl)
        # latente -> U-Net
        uyc = (uy0 + uy1) / 2
        xq = (lx1 + ux0) / 2
        self.flecha(ax, [(lx1, ly0 + 30), (xq, ly0 + 30), (xq, uyc),
                         (ux0 - 3, uyc)], "l-u" in fl)
        # ε̂
        ex0, ex1, ey0, ey1 = self.EPS
        ecx = (ex0 + ex1) / 2
        self.flecha(ax, [(ecx, uy1), (ecx, ey0 - 3)], "u-e" in fl)
        on = "eps" in act
        ax.add_patch(Rectangle((ex0, ey0), ex1 - ex0, ey1 - ey0, fc="white",
                               ec=BORDE_GRIS, lw=1.5, ls=(0, (5, 4)),
                               zorder=2))
        if st.get("eps_on"):
            g = np.clip(0.5 + 0.22 * self.eps[..., 0], 0, 1)
            self.imagen(ax, np.repeat(g[..., None], 3, 2), ex0, ex1, ey0, ey1)
            ax.add_patch(Rectangle((ex0, ey0), ex1 - ex0, ey1 - ey0,
                                   fill=False, ec=ROJO if on else TINTA,
                                   lw=3 if on else 1.6, zorder=5))
        eyc = (ey0 + ey1) / 2
        self.texto(ax, ex1 + 22, eyc - 32, "ruido", fs=19, ha="left",
                   color=ROJO if on else TINTA,
                   fontweight="bold" if on else "normal")
        self.texto(ax, ex1 + 22, eyc, "predicho ε̂", fs=19, ha="left",
                   color=ROJO if on else TINTA,
                   fontweight="bold" if on else "normal")
        self.texto(ax, ex1 + 22, eyc + 34, "64×64×4", fs=19,
                   ha="left", family="DejaVu Sans Mono")
        # scheduler
        sx0, sx1, sy0, sy1 = self.SCHED
        self.flecha(ax, [(ecx, ey1), (ecx, sy0 - 3)], "e-s" in fl)
        on = "sched" in act
        if on:
            self.halo(ax, sx0, sx1, sy0, sy1)
        self.caja(ax, sx0, sx1, sy0, sy1, "white", ROJO if on else BORDE_GRIS,
                  lw=3.5 if on else 2.0)
        scx = (sx0 + sx1) / 2
        self.texto(ax, scx, sy0 + 38, "scheduler resta el ruido", fs=21,
                   fontweight="bold", color=ROJO if on else TINTA)
        self.texto(ax, scx, sy0 + 84, "→ latente un poco más limpio", fs=19)
        # scheduler -> latente (vuelta del bucle)
        syc = (sy0 + sy1) / 2
        self.flecha(ax, [(sx0, syc), (xret, syc), (xret, ly1 + 3)],
                    "s-l" in fl)

        # ---------------- salida: VAE + imagen ----------------
        vx0, vx1, vy0, vy1 = self.VAE
        vyc = (vy0 + vy1) / 2
        self.flecha(ax, [(sx1, vyc), (vx0 - 3, vyc)], "s-v" in fl)
        self.texto(ax, vx0 + 8, (self.IMG[3] + vy0) / 2, "al terminar",
                   fs=16, color=GRIS_MEDIO, style="italic", ha="left")
        on = "vae" in act
        if on:
            self.halo(ax, vx0, vx1, vy0, vy1)
        self.caja(ax, vx0, vx1, vy0, vy1, RELLENO, ROJO if on else BORDE_GRIS,
                  lw=3.5 if on else 2.0)
        vcx = (vx0 + vx1) / 2
        self.texto(ax, vcx, vy0 + 36, "VAE decoder", fs=21, fontweight="bold",
                   color=ROJO if on else TINTA)
        self.texto(ax, vcx, vy0 + 78, "latente final → imagen", fs=18)
        ix0, ix1, iy0, iy1 = self.IMG
        self.flecha(ax, [(vcx, vy0), (vcx, iy1 + 3)], "v-i" in fl)
        icx = (ix0 + ix1) / 2
        self.texto(ax, icx, iy0 - 20, "imagen  512×512×3", fs=20,
                   family="DejaVu Sans Mono",
                   color=ROJO if on else TINTA)
        ax.add_patch(Rectangle((ix0, iy0), ix1 - ix0, iy1 - iy0, fc="white",
                               ec=BORDE_GRIS, lw=1.8, ls=(0, (6, 5)),
                               zorder=2))
        frac = st.get("img_frac", 0.0)
        if frac <= 0:
            self.texto(ax, icx, (iy0 + iy1) / 2,
                       "los píxeles aparecen\nrecién al decodificar", fs=17,
                       color=GRIS_MEDIO, linespacing=1.3)
        else:
            filas = int(round(512 * frac))
            arr = np.ones((512, 512, 4))
            arr[..., :3] = self.img
            arr[filas:, :, 3] = 0
            self.imagen(ax, arr, ix0, ix1, iy0, iy1, interp="antialiased")
            if frac < 1:
                yl = iy0 + (iy1 - iy0) * frac
                ax.plot([ix0, ix1], [yl, yl], color=ROJO, lw=3, zorder=6)
            ax.add_patch(Rectangle((ix0, iy0), ix1 - ix0, iy1 - iy0,
                                   fill=False, ec=TINTA, lw=1.8, zorder=5))

        # ---------------- pie ----------------
        if st.get("pie"):
            self.texto(ax, PX_W / 2, 852, st["pie"], fs=21)
        fr = base.capturar(fig)
        plt.close(fig)
        return fr


# ------------------------------------------------------------------ guion
PIES = {
    "prompt": "Entrada: el prompt es texto libre; todavía no hay ningún tensor.",
    "tok": "Tokenizer: el texto se parte en tokens y se completa hasta 77 posiciones.",
    "clip": "CLIP text encoder: cada uno de los 77 tokens pasa a un vector de 768 → 77×768.",
    "seed": "La seed fija el azar: latente inicial 64×64×4 muestreado de una normal.",
    "unet": "U-Net: entra (latente 64×64×4, t, embedding 77×768), sale el ruido predicho ε̂ 64×64×4.",
    "sched": "Scheduler: resta ε̂ escalado según t → nuevo latente, mismo tamaño 64×64×4.",
    "rep": "Se repite con t bajando: mismo tensor 64×64×4, cada paso con menos ruido.",
    "vae": "VAE decoder: latente final 64×64×4 → imagen 512×512×3 (×8 por lado, 4 → 3 canales).",
    "fin": "CLIP corre una vez, U-Net + scheduler ~50 veces, VAE decoder una vez.",
}
FPS = 12


def guion(esc):
    """Lista de (estado, cuántos cuadros a FPS dura)."""
    frames = []

    def add(st, seg=None, n=None):
        k = n if n is not None else max(1, int(round(seg * FPS)))
        frames.append((st, k))

    # 0. prompt que se tipea
    total = len(PROMPT_LINEAS[0]) + len(PROMPT_LINEAS[1])
    for c in range(0, total + 1, 2):
        add(dict(activos={"prompt"}, prompt_chars=c, emb_cols=0, cartas=0,
                 pie=PIES["prompt"]), n=1)
    add(dict(activos={"prompt"}, emb_cols=0, cartas=0, pie=PIES["prompt"]),
        seg=0.5)
    # 1. tokenizer
    add(dict(activos={"tok"}, flechas={"p-t"}, emb_cols=0, cartas=0,
             pie=PIES["tok"]), seg=0.5)
    add(dict(activos={"tok"}, flechas={"p-t"}, tok_hecho=True, emb_cols=0,
             cartas=0, pie=PIES["tok"]), seg=0.8)
    # 2. CLIP -> embedding (se llena columna a columna)
    for c in np.linspace(0, 77, 13).astype(int):
        add(dict(activos={"clip", "emb"}, flechas={"t-c", "c-e"},
                 tok_hecho=True, emb_cols=c, cartas=0, pie=PIES["clip"]), n=1)
    add(dict(activos={"clip", "emb"}, flechas={"t-c", "c-e"}, tok_hecho=True,
             cartas=0, pie=PIES["clip"]), seg=0.7)
    # 3. seed -> latente inicial (cartas una por una) -> entra al bucle
    for nc in range(0, 5):
        add(dict(activos={"seed"}, flechas={"s-r"}, tok_hecho=True,
                 cartas=nc, pie=PIES["seed"]), seg=0.25)
    add(dict(activos={"seed", "lat"}, flechas={"r-l"}, tok_hecho=True,
             lat=esc.latente(50), pie=PIES["seed"]), seg=0.6)

    # 4. bucle: pasos representativos, cada vez más rápidos
    pasos = [50, 40, 30, 20, 12, 6, 3, 1]
    durs = [2.4, 1.5, 0.95, 0.75, 0.6, 0.5, 0.42, 0.42]
    base_st = dict(tok_hecho=True)
    for i, (s, d) in enumerate(zip(pasos, durs)):
        siguiente = pasos[i + 1] if i + 1 < len(pasos) else 0
        lat = esc.latente(s)
        pie_u = PIES["unet"] if i < 2 else PIES["rep"]
        pie_s = PIES["sched"] if i < 2 else PIES["rep"]
        # U-Net
        add(dict(base_st, activos={"unet", "cont"}, t=s, lat=lat,
                 flechas={"l-u", "e-u"}, pie=pie_u), seg=d * 0.35)
        # sale ε̂
        add(dict(base_st, activos={"unet", "eps", "cont"}, t=s, lat=lat,
                 eps_on=True, flechas={"u-e"}, pie=pie_u), seg=d * 0.2)
        # scheduler: el contador baja pasando por los valores intermedios
        intermedios = list(range(s - 1, siguiente - 1, -1))
        nfr = max(2, int(round(d * 0.45 * FPS)))
        idx = np.linspace(0, len(intermedios) - 1, nfr).round().astype(int)
        for q in idx:
            v = intermedios[q]
            add(dict(base_st, activos={"sched", "lat", "eps", "cont"}, t=v,
                     lat=esc.latente(v), eps_on=True, flechas={"e-s", "s-l"},
                     pie=pie_s), n=1)
    # 5. VAE decoder
    lat0 = esc.latente(0)
    for f in np.linspace(0, 1, 16):
        add(dict(base_st, activos={"vae"}, t=0, lat=lat0, eps_on=True,
                 flechas={"s-v", "v-i"}, img_frac=f, pie=PIES["vae"]), n=1)
    add(dict(base_st, activos={"vae"}, t=0, lat=lat0, eps_on=True,
             flechas={"s-v", "v-i"}, img_frac=1.0, pie=PIES["vae"]), seg=0.7)
    # final fijo (pausa)
    st_fin = dict(base_st, final=True, t=0, lat=lat0, eps_on=True,
                  img_frac=1.0, pie=PIES["fin"])
    frames.append((st_fin, 1))
    return frames


def guardar_gif(cuadros, ruta, colores=256, pausa_s=3.0):
    """Como base.guardar_gif, pero cada estado es UN cuadro del GIF con su
    duración (no se repiten cuadros idénticos): más liviano y más rápido."""
    imgs = [c for c, _ in cuadros]
    dur = [int(round(1000 * k / FPS)) for _, k in cuadros]
    dur[-1] = int(pausa_s * 1000)
    muestra = imgs[:: max(1, len(imgs) // 10)] + [imgs[-1]]
    ancho, alto = imgs[0].size
    mosaico = Image.new("RGB", (ancho, alto * len(muestra)))
    for i, f in enumerate(muestra):
        mosaico.paste(f, (0, alto * i))
    paleta = mosaico.quantize(colors=colores, method=Image.Quantize.MEDIANCUT)
    pal_rgb = np.array(paleta.getpalette()[: 3 * colores]).reshape(-1, 3)
    for hexcol in ("#FFFFFF", TINTA, ROJO, RELLENO):
        c = np.array([int(hexcol[i:i + 2], 16) for i in (1, 3, 5)])
        pal_rgb[np.argmin(((pal_rgb - c) ** 2).sum(1))] = c
    plano = [int(v) for v in pal_rgb.ravel()]
    pal_f = pal_rgb.astype(np.int32)

    def mapear(f):
        a = np.asarray(f, dtype=np.int32)
        clave = (a[..., 0] << 16) | (a[..., 1] << 8) | a[..., 2]
        unicos, inv = np.unique(clave, return_inverse=True)
        rgb = np.stack([unicos >> 16, (unicos >> 8) & 255, unicos & 255], 1)
        idx = np.empty(len(rgb), np.int64)
        for j in range(0, len(rgb), 4096):
            blk = rgb[j:j + 4096]
            idx[j:j + 4096] = ((blk[:, None, :] - pal_f[None]) ** 2).sum(2) \
                .argmin(1)
        p = Image.fromarray(idx[inv].reshape(clave.shape).astype(np.uint8),
                            "P")
        p.putpalette(plano)
        return p

    pal = [mapear(f) for f in imgs]
    pal[0].save(ruta, save_all=True, append_images=pal[1:], duration=dur,
                loop=0, optimize=True, disposal=1)
    total = sum(dur) / 1000
    print(f"{ruta}  {os.path.getsize(ruta) / 1e6:.2f} MB  {len(pal)} cuadros"
          f"  {total:.1f} s")


def main():
    esc = Escena()
    g = guion(esc)
    dbg = os.environ.get("ANIM_DEBUG_DIR")
    solo = os.environ.get("ANIM_SOLO")          # índices a renderizar (prueba)
    if solo:
        os.makedirs(dbg, exist_ok=True)
        for i in [int(x) for x in solo.split(",")]:
            i = i % len(g)
            esc.dibujar(g[i][0]).save(os.path.join(dbg, f"estado-{i:03d}.png"))
        print(f"{len(g)} estados")
        return
    cuadros = [(esc.dibujar(st), k) for st, k in g]
    ruta = os.path.join(OUT, "pipeline-sd-en-vivo.gif")
    guardar_gif(cuadros, ruta)
    cuadros[-1][0].save(os.path.join(OUT, "pipeline-sd-en-vivo.png"))
    if dbg:
        os.makedirs(dbg, exist_ok=True)
        n = len(cuadros)
        for i in (0, n // 5, n // 3, n // 2, int(n * 0.7), n - 20, n - 1):
            cuadros[i][0].save(os.path.join(dbg, f"cuadro-{i:03d}.png"))


if __name__ == "__main__":
    main()
