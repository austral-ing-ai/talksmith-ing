"""SVG del Discriminador evaluando la cara prototipo (1,0/0,1): σ(1) = 0.73, con el gráfico de la sigmoide."""
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from slanted import BLUE, DARK, INK, Canvas, discriminator  # noqa: E402

W, H = 1910, 940


def sigmoid_plot(cv):
    """Gráfico de σ(x) = 1 / (1 + e^-x), marcando σ(1) = 0.73."""
    ox, oy = 1580, 324          # origen: eje y en x=ox, eje x en y=oy
    sx, sy = 52, 240             # px por unidad
    xl, xr = 1130, 1875
    def X(x):
        return ox + x * sx
    def Y(s):
        return oy - s * sy
    m = cv.marker(INK, 22)
    cv.add(f'<path d="M{xl + 8},{oy} L{xr - 8},{oy}" stroke="{INK}" stroke-width="3" marker-end="url(#{m})" marker-start="url(#{m}s)"/>')
    cv.add(f'<path d="M{ox},{oy + 12} L{ox},{Y(1) - 40}" stroke="{INK}" stroke-width="3" marker-end="url(#{m})"/>')
    cv.add(f'<line x1="{xl}" y1="{Y(1):.1f}" x2="{xr}" y2="{Y(1):.1f}" stroke="{INK}" stroke-width="2.5" stroke-dasharray="6 7"/>')
    pts = []
    x = (xl - ox) / sx
    while x <= (xr - 14 - ox) / sx:
        pts.append(f"{X(x):.1f},{Y(1 / (1 + math.exp(-x))):.1f}")
        x += 0.1
    cv.add(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{DARK}" stroke-width="6"/>')
    s1 = 1 / (1 + math.exp(-1))
    cv.add(f'<line x1="{ox}" y1="{Y(s1):.1f}" x2="{X(1)}" y2="{Y(s1):.1f}" stroke="{INK}" stroke-width="2.5" stroke-dasharray="6 7"/>')
    cv.add(f'<line x1="{X(1)}" y1="{Y(s1):.1f}" x2="{X(1)}" y2="{oy}" stroke="{INK}" stroke-width="2.5" stroke-dasharray="6 7"/>')
    cv.add(f'<circle cx="{ox}" cy="{Y(s1):.1f}" r="11" fill="{BLUE}"/>')
    cv.add(f'<circle cx="{X(1)}" cy="{oy}" r="11" fill="{BLUE}"/>')
    cv.text(ox - 20, Y(s1) + 15, "0.73", 44, INK, anchor="end")
    cv.text(X(1), oy + 52, "1", 44, INK)
    cv.text(ox + 16, Y(1) - 40 + 16, "1", 44, INK, anchor="start")
    # fórmula: σ(x) = 1 / (1 + e^-x)
    fy = 190
    cv.text(1130, fy + 17, "σ(x) =", 50, INK, anchor="start", italic=True)
    fc = 1360
    cv.text(fc, fy - 14, "1", 46, INK)
    cv.add(f'<line x1="{fc - 74}" y1="{fy}" x2="{fc + 84}" y2="{fy}" stroke="{INK}" stroke-width="3"/>')
    cv.text(fc - 74, fy + 54, "1 + e", 46, INK, anchor="start", italic=True)
    cv.text(fc + 40, fy + 32, "-x", 34, INK, anchor="start", italic=True)


def main(path):
    cv = Canvas(W, H, "Discriminador con la cara",
                "La cara prototipo (1, 0 / 0, 1) pasa por la red del Discriminador, con pesos +1, -1, -1, +1 y bias -1; "
                "la salida es σ(1) = 0.73. Arriba, el gráfico de la sigmoide σ(x) = 1 / (1 + e^-x) marca el punto (1, 0.73).")
    out = discriminator(cv, (1, 0, 0, 1), ox=-40, oy=0)
    cv.text(out[0] + 80, out[1] + 30, "σ(1) = 0.73", 84, DARK, anchor="start")
    sigmoid_plot(cv)
    m = cv.marker(INK, 22)
    # punta de flecha invertida para el extremo izquierdo del eje x
    cv.defs[m + "s"] = (f'<marker id="{m}s" viewBox="0 0 10 10" refX="3" refY="5" markerWidth="22" markerHeight="22" '
                        f'markerUnits="userSpaceOnUse" orient="auto"><path d="M10,0 L0,5 L10,10 z" fill="{INK}"/></marker>')
    cv.save(path)


if __name__ == "__main__":
    main(sys.argv[1])
