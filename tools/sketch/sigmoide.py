"""Redibujo vectorial de la curva sigmoid del slide 25 (AIG4B Clase 8).

La curva se calcula punto a punto con σ(x) = 1/(1+e^−x); el punto marcado es σ(1) ≈ 0.73.
Salida: talks/redes-generativas-antagonicas/images/sigmoide.svg
"""
import math
from pathlib import Path

from _metrics import width

OUT = Path(__file__).resolve().parents[2] / "talks/redes-generativas-antagonicas/images/sigmoide.svg"
INK, DARK, RED, RULE = "#3B3535", "#1F1E1E", "#DA1B2E", "#D8D2CE"
SERIF = "'Times New Roman', Times, serif"

W, H = 1000, 470
X0, Y0 = 495, 390          # origen
SX, SY = 108, 300          # px por unidad
XMIN, XMAX = -4.2, 4.2


def px(x):
    return X0 + SX * x


def py(y):
    return Y0 - SY * y


def sig(x):
    return 1 / (1 + math.exp(-x))


def main():
    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" fill="{INK}">')
    o.append('<title>Función sigmoid</title>')
    o.append('<desc>Redibujo del slide 25: curva sigmoid σ(x) = 1/(1+e^-x) calculada punto a punto, con el punto x = 1 marcado en 0.73 y guías punteadas.</desc>')
    o.append('<defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="14" viewBox="0 0 16 14" refX="16" refY="7" orient="auto-start-reverse">'
             f'<path d="M0,0 L16,7 L0,14 z" fill="{INK}"/></marker></defs>')
    o.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')

    # asíntota y = 1 (punteada, a la derecha, como en el original)
    o.append(f'<path d="M{px(1.9):.1f},{py(1):.1f} H{px(XMAX):.1f}" stroke="{INK}" stroke-width="1.6" stroke-dasharray="3 6" fill="none"/>')

    # ejes
    o.append(f'<path d="M{px(XMIN) - 6:.1f},{Y0} H{px(XMAX) + 14:.1f}" stroke="{INK}" stroke-width="2" fill="none" marker-start="url(#ah)" marker-end="url(#ah)"/>')
    o.append(f'<path d="M{X0},{Y0 + 6} V{py(1) - 52:.1f}" stroke="{INK}" stroke-width="2" fill="none" marker-end="url(#ah)"/>')
    o.append(f'<path d="M{X0 - 8},{py(1):.1f} H{X0 + 8}" stroke="{INK}" stroke-width="2"/>')
    o.append(f'<text x="{X0 - 18}" y="{py(1) + 11:.1f}" font-size="30" text-anchor="end">1</text>')

    # curva
    n = 240
    a, b = XMIN + 0.3, XMAX
    pts = [(px(a + (b - a) * i / n), py(sig(a + (b - a) * i / n))) for i in range(n + 1)]
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    o.append(f'<path d="{d}" stroke="{DARK}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

    # guías punteadas y puntos
    s1 = sig(1)
    o.append(f'<path d="M{X0},{py(s1):.1f} H{px(1):.1f} V{Y0}" stroke="{RED}" stroke-width="2" stroke-dasharray="7 5" fill="none"/>')
    o.append(f'<circle cx="{X0}" cy="{py(s1):.1f}" r="10" fill="{RED}"/>')
    o.append(f'<circle cx="{px(1):.1f}" cy="{Y0}" r="10" fill="{RED}"/>')
    o.append(f'<text x="{X0 - 22}" y="{py(s1) + 32:.1f}" font-size="32" text-anchor="end" fill="{DARK}">0.73</text>')
    o.append(f'<text x="{px(1):.1f}" y="{Y0 + 50}" font-size="32" text-anchor="middle" fill="{DARK}">1</text>')

    # fórmula σ(x) = 1 / (1 + e^-x)
    fs = 40
    fx, fy = 60, 175
    lhs = "σ(x) = "
    o.append(f'<text x="{fx}" y="{fy + 13}" font-family="{SERIF}" font-style="italic" font-size="{fs}" fill="{DARK}">σ(<tspan>x</tspan>) =</text>')
    left = fx + width("σ(x) =", fs, "serif-italic") + 14
    w_den = width("1 + ", fs, "serif") + width("e", fs, "serif-italic")
    wd = w_den + width("−x", fs * 0.62, "serif-italic") + 1
    rule_w = wd + 16
    cx = left + rule_w / 2
    o.append(f'<path d="M{left:.1f},{fy:.1f} h{rule_w:.1f}" stroke="{DARK}" stroke-width="2.2"/>')
    o.append(f'<text x="{cx:.1f}" y="{fy - 12}" font-family="{SERIF}" font-size="{fs}" text-anchor="middle" fill="{DARK}">1</text>')
    dx = cx - wd / 2
    o.append(f'<text x="{dx:.1f}" y="{fy + 42}" font-family="{SERIF}" font-size="{fs}" fill="{DARK}">1 + <tspan font-style="italic">e</tspan></text>')
    o.append(f'<text x="{dx + w_den + 4:.1f}" y="{fy + 26}" font-family="{SERIF}" font-style="italic" font-size="{fs * 0.62:.0f}" fill="{DARK}">−x</text>')

    o.append('</svg>')
    OUT.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
