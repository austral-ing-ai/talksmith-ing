"""SVG de "El mundo de Slanted Land": gente inclinada (a mano), pantallas 2x2 y una red de una capa (limpias)."""
import random
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from sketch import ellipse_pts, rotate, stroke  # noqa: E402
from slanted import DARK, Canvas  # noqa: E402

W, H = 1720, 560
LEAN = -52           # la gente de Slanted Land se inclina hacia atrás


def person(fx, ground, hair, rnd):
    """Figura de palitos parada en (fx, ground), dibujada derecha y luego inclinada desde los tobillos."""
    out = []
    ax, ay = 0, -12                       # tobillos (pivote de la inclinación)

    def P(pts):
        return [(x + fx, y + ground) for x, y in rotate(pts, ax, ay, LEAN)]

    # piernas: un lazo largo y finito, con la línea que separa las dos piernas
    out.append(stroke(P([(-5, -12), (-13, -80), (-19, -160), (-15, -203), (0, -214), (15, -204), (19, -160),
                         (13, -80), (6, -12)]), rnd, amp=1.4, width=4.4))
    out.append(stroke(P([(0, -16), (1, -70), (2, -120)]), rnd, amp=1.0, width=3.1, passes=1))
    # torso y cuello
    out.append(stroke(P([(0, -214), (2, -270), (0, -334)]), rnd, amp=1.2, width=4.4))
    # brazos
    out.append(stroke(P([(0, -318), (-26, -282), (-44, -238), (-50, -222)]), rnd, amp=1.2, width=4.1))
    out.append(stroke(P([(0, -318), (30, -288), (52, -262), (60, -244)]), rnd, amp=1.2, width=4.1))
    # cabeza y cara
    hx, hy = P([(0, -372)])[0]
    out.append(stroke(ellipse_pts(hx, hy, 25, 38, LEAN, rnd=rnd, overshoot=0.1), rnd, amp=1.0, width=4.4))
    for ex, ey in ((-9, -382), (9, -384)):
        out.append(stroke(P([(ex, ey), (ex + 1, ey + 3)]), rnd, amp=0.4, width=5.8, passes=1))
    out.append(stroke(P([(-9, -362), (0, -355), (9, -362)]), rnd, amp=0.6, width=3.7, passes=1))
    # pelo
    if hair == 0:       # dos rulos tipo antena
        out.append(stroke(P([(-8, -408), (-20, -430), (-30, -428), (-28, -440), (-14, -446)]), rnd, width=3.7))
        out.append(stroke(P([(8, -409), (18, -432), (32, -440)]), rnd, width=3.7))
    else:               # pelo largo que vuela hacia atrás y un mechón que cae
        out.append(stroke(P([(6, -410), (30, -404), (52, -388), (76, -382), (96, -388)]), rnd, width=3.7))
        out.append(stroke(P([(-18, -398), (-38, -378), (-44, -350), (-34, -330)]), rnd, width=3.7))
        out.append(stroke(P([(14, -404), (34, -392), (48, -372)]), rnd, width=3.1))
    # zapatos: dos óvalos chatos apoyados en el piso, sin inclinar
    out.append(stroke(ellipse_pts(fx - 6, ground - 2, 46, 9, 0, rnd=rnd, overshoot=0.08), rnd, amp=0.9, width=4.1))
    out.append(stroke(ellipse_pts(fx + 30, ground + 3, 46, 9, 0, rnd=rnd, overshoot=0.08), rnd, amp=0.9, width=4.1))
    return "\n".join(out)


def monitor(cv, cx):
    x0, x1, y0, y1 = cx - 190, cx + 190, 60, 330
    cv.add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="16" fill="{DARK}"/>')
    sx0, sx1, sy0, sy1 = x0 + 20, x1 - 20, y0 + 20, y1 - 20
    cv.add(f'<rect x="{sx0}" y="{sy0}" width="{sx1 - sx0}" height="{sy1 - sy0}" fill="#ffffff"/>')
    cv.add(f'<rect x="{cx - 3}" y="{sy0}" width="6" height="{sy1 - sy0}" fill="{DARK}"/>')
    cv.add(f'<rect x="{sx0}" y="{(sy0 + sy1) / 2 - 3}" width="{sx1 - sx0}" height="6" fill="{DARK}"/>')
    cv.add(f'<path d="M{cx - 30},{y1} L{cx + 30},{y1} L{cx + 40},{y1 + 72} L{cx - 40},{y1 + 72} z" fill="{DARK}"/>')
    cv.add(f'<rect x="{cx - 80}" y="{y1 + 68}" width="160" height="16" rx="3" fill="{DARK}"/>')


def network(cv, cx):
    r_in, r_out = 42, 48
    ins = [(cx - 100, y) for y in (85, 200, 315)]
    out = (cx + 110, 200)
    for n in ins:
        cv.arrow_line(n, out, DARK, 5, 28, r_from=r_in, r_to=r_out)
    for n in ins:
        cv.node(*n, r_in)
    cv.node(*out, r_out)


def main(path):
    rnd = random.Random(19)
    cv = Canvas(W, H, "El mundo de Slanted Land",
                "Tres piezas: gente de Slanted Land dibujada a mano, dos figuras de palitos muy inclinadas hacia atrás; "
                "un monitor con la pantalla dividida en 2×2 píxeles; y el ícono de una red neuronal de una capa, tres "
                "neuronas que apuntan a una.")
    cv.add(person(390, 392, 0, rnd))
    cv.add(person(700, 392, 1, rnd))
    monitor(cv, 1030)
    network(cv, 1480)
    cv.text(400, 505, "Slanted people", 54, DARK)
    cv.text(1030, 505, "2x2 screens", 54, DARK)
    cv.text(1480, 440, "1-layer", 54, DARK)
    cv.text(1480, 505, "Neural network", 54, DARK)
    cv.save(path)


if __name__ == "__main__":
    main(sys.argv[1])
