#!/usr/bin/env python3
"""Entrenamiento de un VAE de juguete, para la Talk
"segmentacion-y-stable-diffusion".

  vae-entrenamiento.gif / .png
      imagen x (16x16) -> encoder -> mu, sigma -> z = mu + sigma*eps (eps
      sorteado de N(0, I)) -> decoder -> x_hat -> pérdida
      ||x - x_hat||^2 + beta*KL -> backward (el gradiente cruza z gracias a la
      reparametrización) -> actualización -> épocas.

Modelo real y chico en numpy (MLP 256 -> 64 -> 2+2 | 2 -> 64 -> 256), entrenado
con SGD de a una imagen sobre 96 formas sintéticas (círculo, cuadrado,
triángulo, cruz en 24 tamaños). Gradientes analíticos verificados contra
diferencias finitas. El primer paso que se muestra en detalle es el primer
paso real del entrenamiento.

Mismo dibujo que vae-en-vivo.gif (gen_anim_clip-vae.py, importado sin
modificarlo). Uso:  python3 gen_train_vae.py
"""
import importlib.util
import os
import sys

import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from gen_animaciones_conv import (  # noqa: E402
    capturar, guardar_gif, TINTA, ROJO, RELLENO, GRIS_MEDIO, OUT)

_spec = importlib.util.spec_from_file_location(
    "gen_anim_clip_vae", os.path.join(AQUI, "gen_anim_clip-vae.py"))
cv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cv)
lienzo, preparar, mezcla, caja, rect = (cv.lienzo, cv.preparar, cv.mezcla,
                                        cv.caja, cv.rect)
txt, flecha, pie, imagen, suave = cv.txt, cv.flecha, cv.pie, cv.imagen, cv.suave
sobre_camino, div_rgb, BORDE, ROSA = (cv._sobre_camino, cv._div_rgb, cv.BORDE,
                                      cv.ROSA)

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import to_rgb  # noqa: E402
from matplotlib.patches import Circle, Ellipse  # noqa: E402

# =========================================================================
# Modelo
# =========================================================================
S = 16                                   # imágenes de 16x16
D, HID, DZ = S * S, 64, 2
FORMAS = ["círculo", "cuadrado", "triángulo", "cruz"]
MARCAS = ["o", "s", "^", "P"]
BETA, ETA, EPOCAS = 1.0, 0.002, 1000
EJ = 12                                  # el ejemplo: círculo mediano
MUESTRA = [12, 36, 60, 84]               # una de cada forma, mismo tamaño
SNAPS = [1, 3, 10, 30, 100, 200, 400, 1000]


def forma(k, r, n=S, sub=4):
    """Forma k de 'radio' r, centrada, con bordes suavizados (supermuestreo)."""
    m = n * sub
    yy, xx = (np.mgrid[0:m, 0:m] + 0.5) / sub - n / 2
    if k == 0:
        a = xx ** 2 + yy ** 2 < r ** 2
    elif k == 1:
        a = (np.abs(xx) < r * 0.85) & (np.abs(yy) < r * 0.85)
    elif k == 2:
        h = 1.8 * r
        y0 = -h * 0.55
        a = (yy > y0) & (yy < y0 + h) & \
            (np.abs(xx) < (yy - y0) / h * r * 1.05)
    else:
        g = max(r * 0.33, 1.0)
        a = ((np.abs(xx) < g) & (np.abs(yy) < r)) | \
            ((np.abs(yy) < g) & (np.abs(xx) < r))
    return a.reshape(n, sub, n, sub).mean((1, 3))


def dataset(por_forma=24):
    X, y = [], []
    for k in range(4):
        for r in np.linspace(3.0, 7.0, por_forma):
            X.append(forma(k, r).ravel())
            y.append(k)
    return np.array(X), np.array(y)


def init(rng):
    return dict(
        W1=rng.normal(0, 1 / np.sqrt(D), (HID, D)), b1=np.zeros(HID),
        Wm=rng.normal(0, 1 / np.sqrt(HID), (DZ, HID)), bm=np.zeros(DZ),
        Wl=rng.normal(0, 0.1 / np.sqrt(HID), (DZ, HID)), bl=np.zeros(DZ),
        W3=rng.normal(0, 1 / np.sqrt(DZ), (HID, DZ)), b3=np.zeros(HID),
        W4=rng.normal(0, 1 / np.sqrt(HID), (D, HID)), b4=np.zeros(D))


def forward(P, x, eps):
    """encoder -> (mu, log sigma^2) -> z = mu + sigma*eps -> decoder."""
    h = np.tanh(P["W1"] @ x + P["b1"])
    mu = P["Wm"] @ h + P["bm"]
    lv = P["Wl"] @ h + P["bl"]                       # log sigma^2
    sg = np.exp(0.5 * lv)
    z = mu + sg * eps                                # reparametrización
    g = np.tanh(P["W3"] @ z + P["b3"])
    xh = 1 / (1 + np.exp(-(P["W4"] @ g + P["b4"])))
    rec = np.sum((x - xh) ** 2)
    kl = 0.5 * np.sum(mu ** 2 + sg ** 2 - 1 - lv)    # KL(N(mu,sg^2) || N(0,I))
    return dict(h=h, mu=mu, lv=lv, sg=sg, eps=eps, z=z, g=g, xh=xh, rec=rec,
                kl=kl, L=rec + BETA * kl)


def backward(P, x, eps):
    f = forward(P, x, eps)
    dxh = 2 * (f["xh"] - x)                          # dL/dx_hat
    da4 = dxh * f["xh"] * (1 - f["xh"])
    G = {"W4": np.outer(da4, f["g"]), "b4": da4}
    da3 = (P["W4"].T @ da4) * (1 - f["g"] ** 2)
    G["W3"], G["b3"] = np.outer(da3, f["z"]), da3
    dz = P["W3"].T @ da3                             # dL/dz
    dmu = dz * 1.0 + BETA * f["mu"]                  # dz/dmu = 1
    dsg = dz * eps + BETA * (f["sg"] - 1 / f["sg"])  # dz/dsigma = eps
    dlv = dsg * 0.5 * f["sg"]
    G["Wm"], G["bm"] = np.outer(dmu, f["h"]), dmu
    G["Wl"], G["bl"] = np.outer(dlv, f["h"]), dlv
    da1 = (P["Wm"].T @ dmu + P["Wl"].T @ dlv) * (1 - f["h"] ** 2)
    G["W1"], G["b1"] = np.outer(da1, x), da1
    f.update(dxh=dxh, dz=dz, dmu=dmu, dsg=dsg)
    return f, G


def verificar_gradiente(P, x, eps):
    """assert: gradiente analítico == diferencias finitas centradas."""
    _, G = backward(P, x, eps)
    rng = np.random.default_rng(0)
    h = 1e-6
    for k in P:
        for _ in range(6):
            idx = tuple(int(rng.integers(0, s)) for s in P[k].shape)
            Pp = {q: v.copy() for q, v in P.items()}
            Pm = {q: v.copy() for q, v in P.items()}
            Pp[k][idx] += h
            Pm[k][idx] -= h
            num = (forward(Pp, x, eps)["L"] - forward(Pm, x, eps)["L"]) / (2 * h)
            assert abs(num - G[k][idx]) < 1e-5 * max(1.0, abs(num)), \
                (k, idx, num, G[k][idx])


def entrenar():
    X, y = dataset()
    n = len(X)
    rng = np.random.default_rng(3)
    P = init(rng)
    eps0 = rng.standard_normal(DZ)                   # el ε del paso 1
    verificar_gradiente(P, X[EJ], eps0)
    ev = np.random.default_rng(99).standard_normal((n, DZ))
    ev[EJ] = eps0                                    # ε fijo para evaluar

    def evaluar(P):
        fs = [forward(P, X[i], ev[i]) for i in range(n)]
        return (np.mean([f["rec"] for f in fs]),
                np.mean([f["kl"] for f in fs]),
                np.array([f["mu"] for f in fs]),
                np.array([fs[i]["xh"] for i in MUESTRA]))

    def foto(P, ep):
        f, G = backward(P, X[EJ], eps0)
        rec, kl, mus, xhs = evaluar(P)
        return dict(f=f, G=G, W1=P["W1"].copy(), W4=P["W4"].copy(), ep=ep,
                    mus=mus, xhs=xhs, rec_m=rec, kl_m=kl)

    hist = [evaluar(P)[:2]]
    fotos = {0: foto(P, 0)}
    f0, G0 = backward(P, X[EJ], eps0)
    P1 = {k: P[k] - ETA * G0[k] for k in P}
    L_post = forward(P1, X[EJ], eps0)["L"]           # L de x tras el paso 1
    for ep in range(1, EPOCAS + 1):
        orden = rng.permutation(n)
        if ep == 1:                                  # el paso 1 es el ejemplo
            orden = [EJ] + [i for i in orden if i != EJ]
        for j, i in enumerate(orden):
            e = eps0 if (ep == 1 and j == 0) else rng.standard_normal(DZ)
            _, G = backward(P, X[i], e)
            for k in P:
                P[k] = P[k] - ETA * G[k]
            if ep == 1 and j == 0:
                assert all(np.allclose(P[k], P1[k]) for k in P)
        hist.append(evaluar(P)[:2])
        if ep in SNAPS:
            fotos[ep] = foto(P, ep)
    hist = np.array(hist)
    tot = hist[:, 0] + BETA * hist[:, 1]
    assert tot[-1] < 0.15 * tot[0], tot[[0, -1]]
    assert hist[-1, 1] > hist[0, 1]                  # el KL sube desde ~0
    # el gradiente del ejemplo se apaga con el entrenamiento
    gn = [np.linalg.norm(fotos[e]["G"]["W4"]) for e in (0, SNAPS[-1])]
    assert gn[1] < 0.3 * gn[0], gn
    return dict(X=X, y=y, eps0=eps0, fotos=fotos, hist=hist, L_post=L_post)




# =========================================================================
# Dibujo  (coordenadas en px, y hacia abajo; simétrico respecto de x = 800)
# =========================================================================
Y0, Y1, YC = 80, 320, 200                # cajas del pipeline
IMG_Y, IMG_S, IN_X, OUT_X = 110, 180, 40, 1380
ENC, LAT, DEC = (255, 545), (580, 1020), (1055, 1345)
# interior: encoder = tiras a la izquierda, capa oculta a la derecha;
# decoder espejado (el dato fluye tira -> capa en el encoder y al revés)
E_TIRA, E_GRID = (268, 420), (436, 532)
D_GRID, D_TIRA = (1068, 1164), (1180, 1332)
GRID_Y = (104, 200)
TIRA_W, TIRA_G = (106, 140), (166, 200)
# latente
CEL_X = (616, 682, 748)
MU_Y, SG_Y, EP_Y = (106, 146), (180, 220), (252, 292)
OP = (772, 872)
Z_X = (886, 949, 1012)
KL_X = 762                               # bajada del gradiente del KL
BELL_C, BELL_W, BELL_B, BELL_H = 670, 72, 388, 40
# fórmula y paneles
F_Y, V_Y, E_Y = 440, 478, 505
PAN_T = 544
CURVA = (125, 495, 570, 760)
LOG_MIN, LOG_MAX = 0.03, 100.0
REC_X0, REC_C, REC_G = 630, 64, 28
REC_Y = (566, 642)
PL = (1150, 1370, 562, 782)              # plano latente (x0, x1, y0, y1)
PL_R = 3.6                               # rango de ejes del plano latente
ROT_Y = 814

TINTA_RGB = np.array(to_rgb(TINTA))


def tinta_img(v, n=S):
    """[0,1] -> RGB de blanco a tinta (formas oscuras sobre blanco)."""
    a = np.clip(v.reshape(n, n), 0, 1)[..., None]
    return 1 + a * (TINTA_RGB - 1)


def num(v, d=2):
    v = 0.0 if abs(v) < 0.5 * 10 ** -d else v
    return f"{v:.{d}f}".replace(".", ",").replace("-", "−")


def miles(n):
    return f"{n:,}".replace(",", ".")


def celdas(ax, x0s, y, vals, *, alpha=1.0, act=False, gris=False, size=16):
    for k in range(len(x0s) - 1):
        xa, xb = x0s[k], x0s[k + 1]
        if vals is None or alpha <= 0:
            fc = "white"
        elif gris:
            fc = mezcla("white", RELLENO, alpha)
        else:
            fc = mezcla("white", ROSA, alpha)
        rect(ax, xa, y[0], xb - xa, y[1] - y[0], fc=fc,
             ec=ROJO if act else (GRIS_MEDIO if gris else TINTA),
             lw=3 if act else 1.4, z=5)
        if vals is not None and alpha > 0:
            ax.text((xa + xb) / 2, (y[0] + y[1]) / 2, num(vals[k]),
                    fontsize=size, color=TINTA, ha="center", va="center",
                    zorder=7, alpha=alpha)


def tira(ax, x, y, M, esc, alpha=1.0, ec=TINTA, lw=1.2, ls="-"):
    if alpha > 0:
        imagen(ax, div_rgb(M, esc), x[0], y[0], x[1] - x[0], y[1] - y[0],
               alpha=alpha, interp="antialiased")
    rect(ax, x[0], y[0], x[1] - x[0], y[1] - y[0], fc="none", ec=ec, lw=lw,
         z=6, ls=ls)


def grid8(ax, x, y, v, alpha=1.0, act=False):
    rect(ax, x[0], y[0], x[1] - x[0], y[1] - y[0], fc="white", ec="none",
         z=3)
    if alpha > 0:
        imagen(ax, div_rgb(v.reshape(8, 8), 1.0), x[0], y[0], x[1] - x[0],
               y[1] - y[0], alpha=alpha)
    rect(ax, x[0], y[0], x[1] - x[0], y[1] - y[0], fc="none",
         ec=ROJO if act else TINTA, lw=3 if act else 1.3, z=6)


def campana(ax, eps_vis, alpha_ticks, rojo):
    xs = np.linspace(-2.6, 2.6, 120)
    px = BELL_C + xs * BELL_W / 2.6
    py = BELL_B - BELL_H * np.exp(-xs ** 2 / 2)
    ax.fill_between(px, py, BELL_B, color=RELLENO, zorder=2)
    ax.plot(px, py, color=GRIS_MEDIO, lw=2, zorder=3)
    ax.plot([BELL_C - BELL_W - 6, BELL_C + BELL_W + 6], [BELL_B, BELL_B],
            color=GRIS_MEDIO, lw=1.4, zorder=3)
    if eps_vis is not None and alpha_ticks > 0:
        c = ROJO if rojo else TINTA
        for e in eps_vis:
            e = float(np.clip(e, -2.6, 2.6))
            xx = BELL_C + e * BELL_W / 2.6
            yy = BELL_B - BELL_H * np.exp(-e ** 2 / 2)
            ax.plot([xx, xx], [BELL_B, yy - 5], color=c, lw=3, zorder=4,
                    alpha=alpha_ticks)
            ax.add_patch(Circle((xx, yy - 5), 6, fc=c, ec="white", lw=1.2,
                                zorder=5, alpha=alpha_ticks))
    txt(ax, BELL_C + BELL_W + 38, 352, "ε ~ N(0, I)", size=19, bold=True,
        ha="left", color=ROJO if rojo else TINTA)
    txt(ax, BELL_C + BELL_W + 38, 378, "sorteo nuevo en cada paso", size=15,
        ha="left", color=GRIS_MEDIO)


def particulas(ax, cam, t, n=5, r=9):
    for q in range(n):
        tq = t - 0.045 * q
        if 0 < tq < 1:
            x, y = sobre_camino(cam, tq)
            ax.add_patch(Circle((x, y), r - q, fc=ROJO, ec="white", lw=1.2,
                                alpha=1 - 0.15 * q, zorder=12))


def medir(ax, s, size, bold):
    t = ax.text(0, -100, s, fontsize=size,
                fontweight="bold" if bold else "normal")
    w = t.get_window_extent(ax.figure.canvas.get_renderer()).width
    t.remove()
    return w


def formula_x(ax):
    """Posición x de cada pieza de la fórmula (centrada en 800)."""
    piezas = [("L", True), ("  =  ", False), ("‖x − x̂‖²", True),
              ("  +  ", False), ("β · KL( N(μ, σ²) ‖ N(0, I) )", True)]
    anchos = [medir(ax, p, 26, b) for p, b in piezas]
    xs = [800 - sum(anchos) / 2]
    for w in anchos[:-1]:
        xs.append(xs[-1] + w)
    return piezas, xs, anchos


def dibujar(ax, DT, s, esc, *, act=None, a_h=1.0, a_ms=(1.0, 1.0),
            eps_vis="fijo", a_tick=1.0, a_z=1.0, a_g=1.0, a_xh=1.0,
            loss_n=3, b_t=None, g_alpha=(0.0, 0.0), formula=False,
            W_t=None, L_post=None, curva_n=1, footer="", rotulo=None):
    """Un cuadro. act: etapa en rojo ('in', 'enc', 'eps', 'z', 'dec', 'out',
    'loss', 'back', 'upd', 'ep'). b_t: avance del backward (0..1)."""
    preparar(ax)
    f, G = s["f"], s["G"]
    sW1, sW4, sG1, sG4 = esc
    W1 = s["W1"] if W_t is None else W_t[0]
    W4 = s["W4"] if W_t is None else W_t[1]
    back = act == "back"
    bt = -1.0 if b_t is None else b_t
    entrena = act in ("back", "upd", "ep") or formula
    # ---------------- entrada ----------------
    x = DT["X"][EJ]
    imagen(ax, tinta_img(x), IN_X, IMG_Y, IMG_S, IMG_S)
    rojo_x = act in ("in", "loss")
    rect(ax, IN_X, IMG_Y, IMG_S, IMG_S, fc="none",
         ec=ROJO if rojo_x else TINTA, lw=4 if rojo_x else 1.6, z=6)
    txt(ax, IN_X + IMG_S / 2, 344, "x · 16×16", size=24, bold=True)
    txt(ax, IN_X + IMG_S / 2, 374, "es el objetivo", size=17,
        color=ROJO if act == "in" else GRIS_MEDIO, bold=act == "in")
    flecha(ax, IN_X + IMG_S + 4, YC, ENC[0] - 4, YC,
           color=ROJO if act == "enc" else GRIS_MEDIO)
    # ---------------- encoder / decoder ----------------
    for (x0, x1), nombre, clave in ((ENC, "encoder", "enc"),
                                    (DEC, "decoder", "dec")):
        activo = act == clave or entrena
        caja(ax, x0, Y0, x1 - x0, Y1 - Y0, fc=ROSA if activo else RELLENO,
             ec=ROJO if activo else TINTA, lw=3 if activo else 1.8, r=16,
             z=1)
        txt(ax, (x0 + x1) / 2, 50, nombre, size=26, bold=True,
            color=ROJO if act == clave else TINTA)
        txt(ax, (x0 + x1) / 2, 298, "se entrena", size=18, bold=True,
            color=ROJO, style="italic")
        if formula:
            txt(ax, (x0 + x1) / 2, 256, "W ← W − η · ∂L/∂W", size=18,
                bold=True, color=ROJO)
        enc = clave == "enc"
        tx, gx = (E_TIRA, E_GRID) if enc else (D_TIRA, D_GRID)
        M = W1 if enc else W4.T                      # tiras de 64 x 256
        Gm = G["W1"] if enc else G["W4"].T
        sM, sG = (sW1, sG1) if enc else (sW4, sG4)
        ga = g_alpha[0] if enc else g_alpha[1]
        txt(ax, tx[0], 92, "W  256 → 64" if enc else "W  64 → 256",
            size=15, bold=True, ha="left")
        tira(ax, tx, TIRA_W, M, sM, ec=ROJO if formula else TINTA,
             lw=3 if formula else 1.2)
        txt(ax, tx[0], 154, "∂L/∂W", size=15, bold=True, ha="left",
            color=ROJO if ga > 0 else GRIS_MEDIO)
        tira(ax, tx, TIRA_G, Gm, sG, alpha=ga,
             ec=ROJO if ga > 0 else BORDE, lw=2 if ga > 0 else 1.2,
             ls="-" if ga > 0 else "--")
        if ga > 0:
            nrm = np.linalg.norm(G["W1"] if enc else G["W4"])
            ax.text((tx[0] + tx[1]) / 2, 216, f"‖∂L/∂W‖ = {num(nrm, 1)}",
                    fontsize=14, fontweight="bold", color=ROJO, ha="center",
                    va="center", zorder=8, alpha=ga)
        hv = f["h"] if enc else f["g"]
        a = a_h if enc else a_g
        grid8(ax, gx, GRID_Y, hv, alpha=a, act=act == clave and a < 1)
        txt(ax, (gx[0] + gx[1]) / 2, 214, "capa oculta", size=13,
            color=GRIS_MEDIO)
        txt(ax, (gx[0] + gx[1]) / 2, 230, "64 valores", size=13,
            color=GRIS_MEDIO)
    flecha(ax, E_TIRA[1] + 1, 152, E_GRID[0] - 2, 152, lw=1.4)
    flecha(ax, D_GRID[1] + 1, 152, D_TIRA[0] - 2, 152, lw=1.4)
    # ---------------- latente ----------------
    caja(ax, LAT[0], Y0, LAT[1] - LAT[0], Y1 - Y0, fc="white", ec=ROJO,
         lw=3, r=16, z=1)
    txt(ax, 800, 50, "latente", size=26, bold=True, color=ROJO)
    for yy in ((MU_Y[0] + MU_Y[1]) / 2, YC):
        flecha(ax, ENC[1] + 4, yy, LAT[0] - 4, yy,
               color=ROJO if act == "enc" else GRIS_MEDIO)
    ms_back = back and bt >= 0.62
    for etq, yy, vals, a in (("μ", MU_Y, f["mu"], a_ms[0]),
                             ("σ", SG_Y, f["sg"], a_ms[1])):
        roja = (act == "enc" and a > 0) or ms_back
        txt(ax, 598, (yy[0] + yy[1]) / 2, etq, size=24, bold=True,
            color=ROJO if roja else TINTA)
        celdas(ax, CEL_X, yy, vals, alpha=a, act=roja)
    # ε y su sorteo
    if isinstance(eps_vis, str):                      # "fijo"
        ev = f["eps"]
    else:
        ev = eps_vis
    txt(ax, 598, (EP_Y[0] + EP_Y[1]) / 2, "ε", size=24, bold=True,
        color=ROJO if act == "eps" else GRIS_MEDIO)
    celdas(ax, CEL_X, EP_Y, ev, alpha=0.0 if ev is None else 1.0,
           act=act == "eps", gris=True)
    campana(ax, ev, a_tick if ev is not None else 0, rojo=act == "eps")
    flecha(ax, BELL_C, BELL_B - BELL_H - 10, BELL_C, EP_Y[1] + 4,
           color=ROJO if act == "eps" else GRIS_MEDIO, lw=2)
    # operador z = mu + sigma*eps
    z_back = back and 0.40 <= bt
    op_act = act == "z" or z_back
    caja(ax, OP[0], SG_Y[0], OP[1] - OP[0], SG_Y[1] - SG_Y[0],
         fc=ROSA if op_act else "white", ec=ROJO if op_act else TINTA,
         lw=3 if op_act else 1.6, r=8, z=4)
    txt(ax, (OP[0] + OP[1]) / 2, YC, "μ + σ·ε", size=16, bold=True,
        color=ROJO if op_act else TINTA)
    for (xa, ya), (xb, yb) in (((CEL_X[2] + 3, 126), (OP[0] - 3, YC - 12)),
                               ((CEL_X[2] + 3, YC), (OP[0] - 3, YC)),
                               ((CEL_X[2] + 3, 272), (OP[0] - 3, YC + 12))):
        flecha(ax, xa, ya, xb, yb, lw=1.5,
               color=ROJO if act == "z" else GRIS_MEDIO)
    flecha(ax, OP[1] + 2, YC, Z_X[0] - 2, YC, lw=1.6,
           color=ROJO if act == "z" else GRIS_MEDIO)
    txt(ax, (Z_X[0] + Z_X[2]) / 2, 164, "z", size=24, bold=True,
        color=ROJO if act in ("z", "dec") or z_back else TINTA)
    celdas(ax, Z_X, SG_Y, f["z"], alpha=a_z, act=act == "z" or z_back)
    nx = (OP[0] + Z_X[2]) / 2 + 6
    if act == "z":
        txt(ax, nx, 256, "z = μ + σ·ε", size=18, bold=True, color=ROJO)
        txt(ax, nx, 284, "el azar entra por ε", size=15)
    if z_back:
        a = float(np.clip((bt - 0.40) / 0.06, 0, 1))
        for yy, s_, kw in ((250, "∂z/∂μ = 1   ∂z/∂σ = ε",
                            dict(fontweight="bold", color=ROJO)),
                           (274, "el gradiente cruza z", dict(color=ROJO)),
                           (296, "(reparametrización)",
                            dict(color=GRIS_MEDIO))):
            ax.text(nx, yy, s_, fontsize=15, ha="center", va="center",
                    zorder=8, alpha=a, **kw)
    flecha(ax, LAT[1] + 4, YC, DEC[0] - 4, YC,
           color=ROJO if act == "dec" else GRIS_MEDIO)
    # ---------------- salida ----------------
    flecha(ax, DEC[1] + 4, YC, OUT_X - 4, YC,
           color=ROJO if act == "out" else GRIS_MEDIO)
    resid = back and bt < 0.40
    if resid:
        imagen(ax, div_rgb(f["dxh"].reshape(S, S), 1.0), OUT_X, IMG_Y,
               IMG_S, IMG_S)
    elif a_xh > 0:
        imagen(ax, tinta_img(f["xh"]), OUT_X, IMG_Y, IMG_S, IMG_S,
               alpha=a_xh)
    out_act = act in ("out", "loss") or resid
    rect(ax, OUT_X, IMG_Y, IMG_S, IMG_S, fc="none",
         ec=ROJO if out_act else TINTA, lw=4 if out_act else 1.6, z=6)
    if resid:
        txt(ax, OUT_X + IMG_S / 2, 344, "∂L/∂x̂ = 2(x̂ − x)", size=17,
            bold=True, color=ROJO)
        txt(ax, OUT_X + IMG_S / 2 + 4, 372, "rojo sobra · negro falta",
            size=13, color=GRIS_MEDIO)
    else:
        txt(ax, OUT_X + IMG_S / 2, 344, "x̂ · 16×16", size=24, bold=True)
        txt(ax, OUT_X + IMG_S / 2, 374, "reconstrucción", size=18,
            color=GRIS_MEDIO)
    # ---------------- pérdida ----------------
    piezas, xs, anchos = formula_x(ax)
    cen = [x0 + w / 2 for x0, w in zip(xs, anchos)]
    col = [TINTA] * 5
    if act == "loss":
        col[2] = ROJO if loss_n >= 1 else TINTA
        col[4] = ROJO if loss_n >= 2 else TINTA
        col[0] = ROJO if loss_n >= 3 else TINTA
    if back:
        col[2] = ROJO
        col[4] = ROJO if bt >= 0.40 else TINTA
        col[0] = ROJO
    for (p, b), x0, c in zip(piezas, xs, col):
        txt(ax, x0, F_Y, p, size=26, bold=b, color=c, ha="left")
    if loss_n >= 1:
        txt(ax, cen[2], V_Y, num(f["rec"]), size=21,
            color=ROJO if (act == "loss" and loss_n == 1) else TINTA)
        txt(ax, cen[2], E_Y, "reconstrucción", size=15, color=GRIS_MEDIO)
    if loss_n >= 2:
        txt(ax, cen[3], V_Y, "+", size=21)
        txt(ax, cen[4], V_Y, f"{num(BETA, 0)} × {num(f['kl'])}", size=21,
            color=ROJO if (act == "loss" and loss_n == 2) else TINTA)
        txt(ax, cen[4], E_Y, "KL = ½ Σ (μ² + σ² − 1 − ln σ²),  β = 1",
            size=15, color=GRIS_MEDIO)
    if loss_n >= 3:
        txt(ax, cen[1], V_Y, "=", size=21)
        txt(ax, cen[1] - 18, V_Y, num(f["L"]), size=22, bold=True,
            color=ROJO, ha="right")
    if L_post is not None:
        txt(ax, cen[1] - 18, E_Y, f"tras el paso: {num(L_post)}", size=15,
            bold=True, color=ROJO, ha="right")
    # ---------------- backward ----------------
    if back:
        y_r = 412
        x_v = (DEC[1] + OUT_X) / 2                   # entre decoder y x̂
        ruta_x = [(cen[2] + 30, F_Y - 20), (cen[2] + 52, y_r), (x_v, y_r),
                  (x_v, 262), (OUT_X - 1, 262)]
        ruta_dec = [(OUT_X - 1, 262), (x_v, 240), (x_v, YC),
                    (DEC[1], YC), ((D_TIRA[0] + D_TIRA[1]) / 2, 183),
                    ((D_GRID[0] + D_GRID[1]) / 2, 152), (DEC[0], YC),
                    (Z_X[2], YC), (Z_X[0], YC), (OP[1], YC), (OP[0], YC)]
        ruta_kl = [(KL_X, F_Y - 22), (KL_X, 163)]
        enc_in = [(LAT[0], None), (ENC[1], None),
                  ((E_GRID[0] + E_GRID[1]) / 2, 152),
                  ((E_TIRA[0] + E_TIRA[1]) / 2, 183)]
        ruta_mu = [(OP[0], YC), (CEL_X[2], 126), (CEL_X[0], 126)] + \
            [(xx, 126 if yy is None else yy) for xx, yy in enc_in]
        ruta_sg = [(OP[0], YC), (CEL_X[0], YC)] + \
            [(xx, YC if yy is None else yy) for xx, yy in enc_in]
        lin = dict(color=ROJO, lw=2, zorder=10, alpha=0.55)
        ax.plot(*zip(*ruta_x[:-1]), **lin)
        flecha(ax, *ruta_x[-2], *ruta_x[-1], color=ROJO, lw=2, z=10)
        if bt >= 0.40:
            ax.plot([KL_X, KL_X], [F_Y - 22, 126], color=ROJO, lw=2,
                    ls=(0, (5, 4)), zorder=10)
            for yy in (126, YC):
                flecha(ax, KL_X, yy, CEL_X[2] + 3, yy, color=ROJO, lw=2,
                       z=10)
        if bt < 0.62:
            particulas(ax, ruta_x + ruta_dec[1:], bt / 0.62)
        if 0.40 <= bt < 0.62:
            particulas(ax, ruta_kl, (bt - 0.40) / 0.22)
        if bt >= 0.62:
            u = (bt - 0.62) / 0.38
            particulas(ax, ruta_mu, u)
            particulas(ax, ruta_sg, u)
    # ---------------- paneles ----------------
    _paneles(ax, DT, s, act=act, curva_n=curva_n)
    pie(ax, footer)
    if rotulo:
        txt(ax, 800, ROT_Y, rotulo, size=17, color=GRIS_MEDIO,
            style="italic")


def _ylog(v, y0, y1):
    t = (np.log10(np.clip(v, LOG_MIN, LOG_MAX)) - np.log10(LOG_MIN)) / \
        (np.log10(LOG_MAX) - np.log10(LOG_MIN))
    return y1 - (y1 - y0) * t


def _paneles(ax, DT, s, *, act, curva_n):
    ep_act = act == "ep"
    # ---- curva de pérdida (escala log) ----
    x0, x1, y0, y1 = CURVA
    hist = DT["hist"]
    txt(ax, (x0 + x1) / 2 - 15, PAN_T, "pérdida por época (escala log)",
        size=17, bold=True, color=ROJO if ep_act else TINTA)
    ax.plot([x0, x0, x1], [y0, y1, y1], color=TINTA, lw=1.4, zorder=3)
    for v, etq in ((0.1, "0,1"), (1, "1"), (10, "10"), (100, "100")):
        yy = _ylog(v, y0, y1)
        ax.plot([x0 - 5, x0], [yy, yy], color=TINTA, lw=1.2, zorder=3)
        ax.plot([x0, x1], [yy, yy], color=RELLENO, lw=1, zorder=2)
        txt(ax, x0 - 10, yy, etq, size=14, ha="right", color=GRIS_MEDIO)
    for e in (0, 500, 1000):
        xx = x0 + (x1 - x0) * e / EPOCAS
        ax.plot([xx, xx], [y1, y1 + 5], color=TINTA, lw=1.2, zorder=3)
        txt(ax, xx, y1 + 20, miles(e), size=14, color=GRIS_MEDIO)
    txt(ax, x1 + 8, y1, "época", size=15, color=GRIS_MEDIO, ha="left")
    n = max(1, curva_n)
    px = x0 + (x1 - x0) * np.arange(n) / EPOCAS
    rec, kl = hist[:n, 0], BETA * hist[:n, 1]
    for serie, c, lw, ls in ((rec, TINTA, 1.8, "-"),
                             (kl, GRIS_MEDIO, 2.0, (0, (4, 3))),
                             (rec + kl, ROJO, 2.6, "-")):
        py = _ylog(serie, y0, y1)
        if n == 1:
            ax.plot(px, py, "o", color=c, ms=7, zorder=6)
        else:
            ax.plot(px, py, color=c, lw=lw, ls=ls, zorder=5 if c == ROJO
                    else 4)
            ax.plot(px[-1:], py[-1:], "o", color=c, ms=6, zorder=6)
    for k, (c, ls, etq) in enumerate(((ROJO, "-", "L"),
                                      (TINTA, "-", "reconstrucción"),
                                      (GRIS_MEDIO, (0, (4, 3)), "β·KL"))):
        yy = y1 - 70 + 24 * k
        ax.plot([x1 - 168, x1 - 138], [yy, yy], color=c, ls=ls,
                lw=2.6 if c == ROJO else 2, zorder=5)
        txt(ax, x1 - 130, yy, etq, size=15, ha="left",
            color=ROJO if c == ROJO else TINTA, bold=c == ROJO)
    # ---- reconstrucciones ----
    txt(ax, 800, PAN_T, f"reconstrucciones · época {miles(s['ep'])}",
        size=17, bold=True, color=ROJO if ep_act else TINTA)
    for j, i in enumerate(MUESTRA):
        xx = REC_X0 + j * (REC_C + REC_G)
        for yy, v in ((REC_Y[0], DT["X"][i]), (REC_Y[1], s["xhs"][j])):
            imagen(ax, tinta_img(v), xx, yy, REC_C, REC_C)
            es_ej = i == EJ
            rect(ax, xx, yy, REC_C, REC_C, fc="none",
                 ec=ROJO if es_ej else TINTA, lw=2.6 if es_ej else 1.2, z=6)
        txt(ax, xx + REC_C / 2, REC_Y[1] + REC_C + 17, FORMAS[j], size=13,
            color=GRIS_MEDIO)
    txt(ax, REC_X0 - 14, REC_Y[0] + REC_C / 2, "x", size=20, bold=True,
        ha="right")
    txt(ax, REC_X0 - 14, REC_Y[1] + REC_C / 2, "x̂", size=20, bold=True,
        ha="right")
    txt(ax, 800, REC_Y[1] + REC_C + 44, "z = μ + σ·ε, con ε fijo",
        size=13, color=GRIS_MEDIO, style="italic")
    # ---- plano latente ----
    X0, X1, Y0p, Y1p = PL
    cx, cy = (X0 + X1) / 2, (Y0p + Y1p) / 2
    k_px = (X1 - X0) / (2 * PL_R)
    txt(ax, (X0 + X1) / 2 + 60, PAN_T, "plano latente: μ de cada imagen",
        size=17, bold=True, color=ROJO if ep_act else TINTA)
    rect(ax, X0, Y0p, X1 - X0, Y1p - Y0p, fc="white", ec=BORDE, lw=1.2, z=2)
    ax.plot([X0, X1], [cy, cy], color=BORDE, lw=1, zorder=2)
    ax.plot([cx, cx], [Y0p, Y1p], color=BORDE, lw=1, zorder=2)
    ax.add_patch(Circle((cx, cy), k_px, fc="none", ec=GRIS_MEDIO, lw=1.4,
                        ls=(0, (4, 3)), zorder=3))
    txt(ax, X1 - 6, cy - 12, "z₁", size=14, color=GRIS_MEDIO, ha="right")
    txt(ax, X0 - 6, Y0p + 8, "z₂", size=14, color=GRIS_MEDIO, ha="right")
    mus = np.clip(s["mus"], -PL_R + 0.08, PL_R - 0.08)
    y = DT["y"]
    for k in range(4):
        m = mus[y == k]
        ax.scatter(cx + m[:, 0] * k_px, cy - m[:, 1] * k_px, marker=MARCAS[k],
                   s=30 if MARCAS[k] != "P" else 42, c=TINTA, alpha=0.75,
                   linewidths=0, zorder=5)
    mu, sg = s["f"]["mu"], s["f"]["sg"]
    ex, ey = cx + mu[0] * k_px, cy - mu[1] * k_px
    ax.add_patch(Ellipse((ex, ey), 2 * sg[0] * k_px, 2 * sg[1] * k_px,
                         fc=mezcla("white", ROJO, 0.18), ec=ROJO, lw=1.6,
                         alpha=0.85, zorder=6))
    ax.scatter([ex], [ey], marker="o", s=70, c=ROJO, edgecolors="white",
               linewidths=1.2, zorder=7)
    lx = X1 + 34
    for k in range(4):
        yy = Y0p + 22 + 32 * k
        ax.scatter([lx], [yy], marker=MARCAS[k],
                   s=56 if MARCAS[k] != "P" else 76, c=TINTA, zorder=5)
        txt(ax, lx + 16, yy, FORMAS[k], size=15, ha="left")
    yy = Y0p + 22 + 32 * 4 + 6
    ax.add_patch(Ellipse((lx, yy), 24, 18, fc=mezcla("white", ROJO, .18),
                         ec=ROJO, lw=1.4, zorder=5))
    ax.scatter([lx], [yy], marker="o", s=36, c=ROJO, zorder=6)
    txt(ax, lx + 16, yy, "x: μ ± σ", size=15, ha="left", color=ROJO)
    yy += 34
    ax.add_patch(Circle((lx, yy), 11, fc="none", ec=GRIS_MEDIO, lw=1.4,
                        ls=(0, (3, 2)), zorder=5))
    txt(ax, lx + 16, yy, "N(0, I)", size=15, ha="left", color=GRIS_MEDIO)


# =========================================================================
# Animación
# =========================================================================
def vae_entrenamiento(fps=12, pausa_s=3.0):
    cache = os.environ.get("VAE_CACHE")              # solo para iterar el dibujo
    if cache and os.path.exists(cache):
        import pickle
        with open(cache, "rb") as fh:
            DT = pickle.load(fh)
    else:
        DT = entrenar()
        if cache:
            import pickle
            with open(cache, "wb") as fh:
                pickle.dump(DT, fh)
    fotos, eps0 = DT["fotos"], DT["eps0"]
    s0 = fotos[0]
    esc = (max(np.abs(fo["W1"]).max() for fo in fotos.values()) * 0.6,
           max(np.abs(fo["W4"]).max() for fo in fotos.values()) * 0.6,
           np.abs(s0["G"]["W1"]).max() * 0.6,       # escalas FIJAS de ∂L/∂W:
           np.abs(s0["G"]["W4"]).max() * 0.6)       # las del paso 1
    fig, ax = lienzo()
    fr = []

    def cap(s=s0, **kw):
        dibujar(ax, DT, s, esc, **kw)
        fr.append(capturar(fig))

    pre = dict(a_h=0.0, a_ms=(0.0, 0.0), eps_vis=None, a_z=0.0, a_g=0.0,
               a_xh=0.0, loss_n=0)
    # 1. dato y objetivo
    for _ in range(11):
        cap(act="in", **pre,
            footer="Dato: una imagen x de 16×16; el objetivo es la misma x "
                   "(modelo de juguete en numpy)")
    # 2. encoder
    pie_enc = ("encoder: x (256 valores) → capa oculta (64) → μ y σ, "
               "2 valores cada uno")
    for k in range(15):
        cap(act="enc", **{**pre, "a_h": suave((k + 1) / 5),
                          "a_ms": (suave((k - 4) / 4), suave((k - 8) / 4))},
            footer=pie_enc)
    base = {**pre, "a_h": 1.0, "a_ms": (1.0, 1.0)}
    # 3. sorteo de ε y reparametrización
    rng_vis = np.random.default_rng(5)               # solo la animación del
    for k in range(12):                              # sorteo; el ε real es eps0
        ev = rng_vis.standard_normal(2) if k < 8 else eps0
        cap(act="eps", **{**base, "eps_vis": ev},
            footer="se sortea ε ~ N(0, I): dos valores nuevos de la normal "
                   "estándar")
    for k in range(12):
        cap(act="z", **{**base, "eps_vis": "fijo", "a_z": suave((k + 1) / 4)},
            footer="reparametrización: z = μ + σ·ε; el azar queda en ε, "
                   "fuera del camino de los pesos")
    base = {**base, "eps_vis": "fijo", "a_z": 1.0}
    # 4. decoder
    for k in range(14):
        cap(act="dec" if k < 7 else "out",
            **{**base, "a_g": suave((k + 1) / 5), "a_xh": suave((k - 5) / 5)},
            footer="decoder: z (2 valores) → capa oculta (64) → x̂ de 16×16")
    base = {**base, "a_g": 1.0, "a_xh": 1.0}
    # 5. pérdida
    pies_l = ["pérdida, término 1: reconstrucción ‖x − x̂‖², suma de los "
              "256 errores al cuadrado",
              "término 2: β·KL, cuánto se aleja N(μ, σ²) de N(0, I); "
              "acá β = 1",
              "L = reconstrucción + β·KL, para esta imagen"]
    for n_l, rep in ((1, 8), (2, 9), (3, 8)):
        for _ in range(rep):
            cap(act="loss", **{**base, "loss_n": n_l}, footer=pies_l[n_l - 1])
    base = {**base, "loss_n": 3}
    # 6. backward
    pie_b1 = ("backward: el gradiente va de L a x̂, atraviesa el decoder y "
              "llega a sus pesos")
    pie_b2 = ("cruza z = μ + σ·ε hacia μ y σ, suma el del término KL "
              "y llega al encoder")
    nb = 44
    for k in range(nb):
        t = (k + 1) / nb
        g_dec = float(np.clip((t - 0.24) / 0.10, 0, 1))
        g_enc = float(np.clip((t - 0.90) / 0.10, 0, 1))
        cap(act="back", **base, b_t=t, g_alpha=(g_enc, g_dec),
            footer=pie_b1 if t < 0.40 else pie_b2)
    for _ in range(6):
        cap(act="back", **base, b_t=1.0, g_alpha=(1.0, 1.0),
            footer="∂z/∂μ = 1 y ∂z/∂σ = ε: el sorteo no corta el camino del "
                   "gradiente")
    # 7. actualización
    W0 = (s0["W1"], s0["W4"])
    W1n = (s0["W1"] - ETA * s0["G"]["W1"], s0["W4"] - ETA * s0["G"]["W4"])
    pie_u = (f"actualización: W ← W − η·∂L/∂W en encoder y decoder "
             f"(η = {num(ETA, 3)}); L de esta x baja")
    for k in range(16):
        t = suave((k + 1) / 8)
        Wt = tuple((1 - t) * a + t * b for a, b in zip(W0, W1n))
        cap(act="upd", **base, g_alpha=(1.0, 1.0), formula=True, W_t=Wt,
            L_post=DT["L_post"] if k >= 5 else None, footer=pie_u)
    # 8. épocas
    tot = DT["hist"][:, 0] + BETA * DT["hist"][:, 1]
    for ep in SNAPS:
        for k in range(6):
            cap(fotos[ep], act="ep", **base, g_alpha=(1.0, 1.0),
                curva_n=ep + 1, formula=k < 2,
                footer=f"Se repite con las 96 imágenes, una por paso: época "
                       f"{miles(ep)} de {miles(EPOCAS)}, L promedio = "
                       f"{num(tot[ep], 1)}")
    # 9. cuadro final (pausa)
    dibujar(ax, DT, fotos[EPOCAS], esc, **base, g_alpha=(1.0, 1.0),
            curva_n=EPOCAS + 1,
            footer=f"Tras {miles(EPOCAS)} épocas: L baja de {num(tot[0], 1)} "
                   f"a {num(tot[-1], 1)} y las cuatro formas se separan en el "
                   f"latente",
            rotulo="En Stable Diffusion, el VAE se entrena antes y por "
                   "separado de la U-Net; después queda congelado")
    fr.append(capturar(fig))
    plt.close(fig)
    # escritura atómica: archivo temporal en la misma carpeta + rename, para
    # que un corte a mitad de camino no deje un GIF o PNG vacío
    png = os.path.join(OUT, "vae-entrenamiento.png")
    gif = os.path.join(OUT, "vae-entrenamiento.gif")
    tmp_png, tmp_gif = png + ".tmp.png", gif + ".tmp.gif"
    fr[-1].save(tmp_png)
    guardar_gif(fr, tmp_gif, fps=fps, pausa_s=pausa_s, colores=128)
    assert os.path.getsize(tmp_gif) > 0 and os.path.getsize(tmp_png) > 0
    os.replace(tmp_png, png)
    os.replace(tmp_gif, gif)
    print(f"{gif}  {os.path.getsize(gif) / 1e6:.2f} MB")
    return fr


if __name__ == "__main__":
    frames = vae_entrenamiento()
    dbg = os.environ.get("DBG_DIR")
    if dbg:
        os.makedirs(dbg, exist_ok=True)
        n = len(frames)
        for i in [int(a) for a in os.environ.get(
                "DBG_FR", f"10,30,60,{n // 2},{n - 30},{n - 1}").split(",")]:
            frames[i].save(os.path.join(dbg, f"vae-entrenamiento-{i:03d}.png"))
