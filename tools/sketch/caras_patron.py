"""SVG de "Los datos reales: caras con patrón": 4 caras de Slanted Land a mano + sus 2×2."""
import random
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from sketch import INK, ellipse_pts, rotate, stroke  # noqa: E402

W, H = 1000, 500
FACE_SCALE = 1.3
CELL = 76          # lado de cada píxel de la grilla
TILT = -38           # todo en Slanted Land se inclina
# valores de las cuatro caras (tabla "Faces" de slide 21): 0 = blanco, 1 = negro
FACES = [(0.75, 0, 0, 0.75), (1, 0.25, 0.25, 0.75), (1, 0, 0, 1), (0.75, 0, 0.25, 0.75)]


def gray(v):
    c = round(255 * (1 - v))
    return f"#{c:02x}{c:02x}{c:02x}"


def face(cx, cy, style, rnd):
    out = []
    # contorno: óvalo alargado e inclinado
    out.append(stroke(ellipse_pts(cx, cy, 30, 66, TILT, rnd=rnd), rnd, amp=1.2, width=2.4))
    def R(pts):
        return rotate(pts, cx, cy, TILT)
    # ojos: dos puntos cortos
    for ex in (-11, 11):
        out.append(stroke(R([(cx + ex, cy - 18), (cx + ex + 1.5, cy - 15)]), rnd, amp=0.6, width=3.2, passes=1))
    # nariz en v y boca
    out.append(stroke(R([(cx + 2, cy - 6), (cx - 4, cy + 6), (cx + 4, cy + 7)]), rnd, amp=0.8, width=1.8, passes=1))
    out.append(stroke(R([(cx - 9, cy + 24), (cx, cy + 29), (cx + 10, cy + 23)]), rnd, amp=0.9, width=2, passes=2))
    # pelo: distinto en cada cara
    if style == 0:      # un rulo arriba
        out.append(stroke(R([(cx - 4, cy - 64), (cx - 10, cy - 80), (cx + 2, cy - 88), (cx + 8, cy - 78), (cx, cy - 72)]), rnd, width=2))
        out.append(stroke(R([(cx - 20, cy - 54), (cx - 34, cy - 62), (cx - 38, cy - 52)]), rnd, width=1.8))
    elif style == 1:    # mechón largo que cae al costado
        out.append(stroke(R([(cx - 14, cy - 60), (cx - 30, cy - 36), (cx - 36, cy + 6), (cx - 30, cy + 40), (cx - 40, cy + 58)]), rnd, width=1.9))
        out.append(stroke(R([(cx + 18, cy - 58), (cx + 34, cy - 66), (cx + 46, cy - 56)]), rnd, width=1.8))
    elif style == 2:    # moño con rulos
        for i in range(3):
            ox = -12 + 12 * i
            out.append(stroke(ellipse_pts(*R([(cx + ox, cy - 74)])[0], 7, 6, 0, n=12, rnd=rnd), rnd, amp=0.7, width=1.7))
        out.append(stroke(R([(cx - 26, cy - 52), (cx - 34, cy - 30)]), rnd, width=1.6))
        out.append(stroke(R([(cx + 24, cy - 54), (cx + 32, cy - 32)]), rnd, width=1.6))
        # pestañas
        for ex in (-11, 11):
            out.append(stroke(R([(cx + ex - 4, cy - 24), (cx + ex - 1, cy - 28)]), rnd, amp=0.4, width=1.2, passes=1))
            out.append(stroke(R([(cx + ex + 3, cy - 24), (cx + ex + 5, cy - 28)]), rnd, amp=0.4, width=1.2, passes=1))
        # piernitas que asoman abajo
        for lx in (-8, 8):
            out.append(stroke(R([(cx + lx, cy + 64), (cx + lx - 2, cy + 84), (cx + lx + 6, cy + 86)]), rnd, width=1.6))
    else:               # pelo largo con varias hebras
        for i, ox in enumerate((0, 6, 12)):   # hebras que caen por fuera del contorno, del lado izquierdo
            out.append(stroke(R([(cx - 18 + ox, cy - 62), (cx - 36 - ox / 2, cy - 30), (cx - 42 - ox / 2, cy + 14), (cx - 36 - ox, cy + 58)]), rnd, width=1.5))
    return "\n".join(out)


def grid(x, y, vals, size=46):
    out = []
    for i, v in enumerate(vals):
        gx, gy = x + (i % 2) * size, y + (i // 2) * size
        out.append(f'<rect x="{gx}" y="{gy}" width="{size}" height="{size}" fill="{gray(v)}"/>')
    out.append(f'<rect x="{x}" y="{y}" width="{2 * size}" height="{2 * size}" fill="none" stroke="{INK}" stroke-width="3"/>')
    out.append(f'<line x1="{x + size}" y1="{y}" x2="{x + size}" y2="{y + 2 * size}" stroke="{INK}" stroke-width="1.5"/>')
    out.append(f'<line x1="{x}" y1="{y + size}" x2="{x + 2 * size}" y2="{y + size}" stroke="{INK}" stroke-width="1.5"/>')
    return "\n".join(out)


def main(path):
    rnd = random.Random(7)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">',
             "<title>Los datos reales: caras con patrón</title>",
             "<desc>Cuatro caras de Slanted Land dibujadas a mano, todas inclinadas, y debajo de cada una su versión en 2×2 píxeles: "
             "los píxeles de la diagonal oscuros, los otros claros.</desc>",
             f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
    for k in range(4):
        cx = 125 + k * 250
        cy = 128
        parts.append(f'<g transform="translate({cx},{cy}) scale({FACE_SCALE}) translate({-cx},{-cy})">')
        parts.append(face(cx, cy, k, rnd))
        parts.append("</g>")
        parts.append(grid(cx - CELL, 300, FACES[k], size=CELL))
    parts.append("</svg>")
    open(path, "w").write("\n".join(parts))


if __name__ == "__main__":
    main(sys.argv[1])
