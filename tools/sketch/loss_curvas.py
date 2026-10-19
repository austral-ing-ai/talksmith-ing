"""Redibujo vectorial de los dos gráficos de pérdida del slide 31 (AIG4B Clase 8).

Izquierda: y = −ln(x) (Discriminador ante imagen real). Derecha: y = −ln(1 − x)
(imagen falsa). Las curvas se calculan punto a punto. Barras roja (High error) y
verde (Low error) en x = 0.25 y x = 0.75, como en el original.
Salida: talks/redes-generativas-antagonicas/images/loss-curvas.svg
"""
import math
from pathlib import Path

from _metrics import width

OUT = Path(__file__).resolve().parents[2] / "talks/redes-generativas-antagonicas/images/loss-curvas.svg"
INK, DARK, RED, GREEN = "#3B3535", "#1F1E1E", "#DA1B2E", "#2E7D32"
SERIF = "'Times New Roman', Times, serif"
W, H = 1000, 900
SX, SY = 190, 185


class Panel:
    def __init__(self, ox, oy):
        self.ox, self.oy = ox, oy

    def p(self, x, y):
        return self.ox + SX * x, self.oy - SY * y


def axes(o, pn, xmin, xmax, ymin, ymax, xlabels, minor_from, zero_dx=-16):
    x0, _ = pn.p(xmin, 0)
    x1, _ = pn.p(xmax, 0)
    _, yb = pn.p(0, ymin)
    _, yt = pn.p(0, ymax)
    o.append(f'<path d="M{x0:.1f},{pn.oy} H{x1:.1f}" stroke="{DARK}" stroke-width="2.4"/>')
    o.append(f'<path d="M{pn.ox},{yb:.1f} V{yt:.1f}" stroke="{DARK}" stroke-width="2.4" marker-end="url(#ah)"/>')
    # ticks x cada 0.25
    k = minor_from
    while k <= 1.0001:
        tx, _ = pn.p(k, 0)
        big = abs(k - round(k)) < 1e-6
        h = 10 if big else 6
        if abs(k) > 1e-6:
            o.append(f'<path d="M{tx:.1f},{pn.oy - h} V{pn.oy + h}" stroke="{DARK}" stroke-width="2.4"/>')
        k += 0.25
    for v, lab in xlabels:
        tx, _ = pn.p(v, 0)
        dx = zero_dx if v == 0 else 0
        o.append(f'<text x="{tx + dx:.1f}" y="{pn.oy + 44}" text-anchor="middle">{lab}</text>')
    # ticks y cada 0.2, rótulos 1, 2, 3
    for i in range(1, int(round(ymax * 5)) + 1):
        v = i / 5
        _, ty = pn.p(0, v)
        big = i % 5 == 0
        h = 10 if big else 6
        o.append(f'<path d="M{pn.ox - h},{ty:.1f} H{pn.ox + h}" stroke="{DARK}" stroke-width="2.4"/>')
        if big:
            o.append(f'<text x="{pn.ox - 22}" y="{ty + 10:.1f}" text-anchor="end">{i // 5}</text>')


def curve(o, pn, f, a, b, n=300):
    pts = [pn.p(a + (b - a) * i / n, f(a + (b - a) * i / n)) for i in range(n + 1)]
    o.append(f'<path d="M' + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) +
             f'" stroke="{DARK}" stroke-width="3" fill="none" stroke-linejoin="round"/>')


def bar(o, pn, x, f, color):
    bx, by = pn.p(x, f(x))
    o.append(f'<path d="M{bx:.1f},{pn.oy} V{by:.1f}" stroke="{color}" stroke-width="5"/>')


def callout(o, pn, x, label, color, box_x, box_y, side="right"):
    """Etiqueta en caja de color + flecha curva hasta el pie de la barra."""
    fs = 30
    w = width(label, fs) + 28
    h = 48
    o.append(f'<rect x="{box_x:.1f}" y="{box_y:.1f}" width="{w:.1f}" height="{h}" fill="{color}"/>')
    o.append(f'<text x="{box_x + w / 2:.1f}" y="{box_y + 34:.1f}" text-anchor="middle" font-size="{fs}" fill="#ffffff">{label}</text>')
    bx, _ = pn.p(x, 0)
    sx = box_x + w if side == "right" else box_x + w / 2
    sy = box_y + h / 2 if side == "right" else box_y
    ty = pn.oy + 14
    if side == "right":
        d = f"M{sx:.1f},{sy:.1f} C{sx + (bx - sx) * 0.75:.1f},{sy:.1f} {bx:.1f},{sy - 20:.1f} {bx:.1f},{ty:.1f}"
    else:
        d = f"M{sx:.1f},{sy:.1f} C{sx:.1f},{sy - 30:.1f} {bx:.1f},{sy - 25:.1f} {bx:.1f},{ty:.1f}"
    o.append(f'<path d="{d}" stroke="{color}" stroke-width="3" fill="none" marker-end="url(#ah-{color[1:]})"/>')


def formula(o, x, y, parts, fs=42):
    """parts: lista de (texto, cursiva). Texto anclado a la izquierda; los tspans avanzan."""
    spans = "".join(f'<tspan font-style="italic">{t}</tspan>' if it else t for t, it in parts)
    o.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{SERIF}" font-size="{fs}" fill="{DARK}" xml:space="preserve">{spans}</text>')


def marker(mid, color):
    return (f'<marker id="{mid}" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="14" viewBox="0 0 16 14" '
            f'refX="15" refY="7" orient="auto"><path d="M0,0 L16,7 L0,14 z" fill="{color}"/></marker>')


def main():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="10 22 {W} 866" font-family="Helvetica, Arial, sans-serif" font-size="32" fill="{INK}">',
         '<title>Funciones de pérdida</title>',
         '<desc>Redibujo del slide 31: a la izquierda y = -ln(x), a la derecha y = -ln(1 - x), ambas sobre [0, 1]. '
         'Barras roja (High error) y verde (Low error) en x = 0.25 y x = 0.75.</desc>',
         '<defs>' + marker("ah", DARK) + marker("ah-" + RED[1:], RED) + marker("ah-" + GREEN[1:], GREEN) + '</defs>',
         f'<rect x="10" y="22" width="{W}" height="866" fill="#ffffff"/>']

    # Panel izquierdo: y = −ln(x)
    L = Panel(240, 660)
    axes(o, L, -1.1, 1.1, -0.3, 3.3, [(-1, "-1"), (0, "0"), (1, "1")], -1.0)
    f1 = lambda x: -math.log(x)
    curve(o, L, f1, math.exp(-3.3), 1.07)
    bar(o, L, 0.25, f1, RED)
    bar(o, L, 0.75, f1, GREEN)
    formula(o, *L.p(0.40, 1.85), [("y", True), (" = − ln(", False), ("x", True), (")", False)])
    formula(o, *L.p(-0.45, 1.35), [("y", True)])
    callout(o, L, 0.25, "High error", RED, 45, 730)
    callout(o, L, 0.75, "Low error", GREEN, 95, 810)

    # Panel derecho: y = −ln(1 − x)
    R = Panel(780, 660)
    axes(o, R, -0.45, 1.1, -0.3, 3.3, [(0, "0"), (1, "1")], -0.25, zero_dx=20)
    f2 = lambda x: -math.log(1 - x)
    curve(o, R, f2, -0.3, 1 - math.exp(-3.3))
    bar(o, R, 0.25, f2, GREEN)
    bar(o, R, 0.75, f2, RED)
    fx, fy = R.p(-0.36, 2.7)
    wf = width("y = − ln(1 − x)", 42, "serif")
    formula(o, fx - wf, fy, [("y", True), (" = − ln(1 − ", False), ("x", True), (")", False)])
    formula(o, *R.p(-0.45, 1.35), [("y", True)])
    callout(o, R, 0.25, "Low error", GREEN, 575, 730)
    callout(o, R, 0.75, "High error", RED, 690, 815, side="top")

    o.append('</svg>')
    OUT.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
