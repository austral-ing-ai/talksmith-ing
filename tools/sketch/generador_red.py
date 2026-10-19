"""SVG del Generador: z = 0.7 → pesos ±1 + bias → σ(±1.7) → grilla 2×2 (0.85, 0.15 / 0.15, 0.85)."""
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from slanted import BLUE, DARK, RED, Canvas, point_on_line  # noqa: E402

W, H = 1940, 1050
R = 50
Z = (420, 430)
BIAS = (420, 870)
NX = 920
NY = [210, 430, 650, 870]
OUT = [("1.7", RED, "0.85"), ("-1.7", BLUE, "0.15"), ("-1.7", BLUE, "0.15"), ("1.7", RED, "0.85")]
SIGN = [("+1", RED), ("-1", BLUE), ("-1", BLUE), ("+1", RED)]
T_Z = [0.4, 0.4, 0.45, 0.28]      # dónde va la etiqueta sobre cada línea (para que no se pisen)
T_B = [0.22, 0.45, 0.55, 0.55]


def main(path):
    cv = Canvas(W, H, "Generador",
                "El Generador recibe z = 0.7 (deslizador de 0 a 1) y un Bias de valor 1, los conecta con pesos +1, -1, -1, +1 "
                "a cuatro neuronas sigmoide: σ(1.7) = 0.85, σ(-1.7) = 0.15, σ(-1.7) = 0.15 y σ(1.7) = 0.85, que forman la "
                "imagen 2×2 (0.85, 0.15 / 0.15, 0.85).")
    cv.text(90, 110, "Generator", 92, DARK, anchor="start")
    cv.slider(40, 260, Z[1], 0.7, "0.7", dot_r=20, font=58)
    cv.text(150, 610, "z", 88, DARK)
    nodes = [(NX, y) for y in NY]
    labels = []
    for src, ts in ((Z, T_Z), (BIAS, T_B)):
        for n, (lab, col), t in zip(nodes, SIGN, ts):
            red = col == RED
            a, tip = cv.arrow_line(src, n, col, 5 if red else 3.5, 32 if red else 24, r_from=R, r_to=R)
            labels.append((point_on_line(a, tip, t), lab, col))
    for (x, y), lab, col in labels:
        cv.halo_text(x, y, lab, 62, col, pad=4)
    # neuronas
    cv.node(*Z, R)
    cv.node(*BIAS, R, "1", 46)
    cv.text(BIAS[0], BIAS[1] + R + 70, "Bias", 62, DARK)
    for n, (v, col, res) in zip(nodes, OUT):
        cv.node(*n, R)
        # σ(v) = res, con v coloreado (texto alineado a la izquierda: los tspan avanzan bien)
        cv.add(f'<text x="{NX + 74}" y="{n[1] + 23}" font-size="66" fill="{DARK}" text-anchor="start">'
               f'σ(<tspan fill="{col}">{v}</tspan>) = {res}</text>')
    # grilla de salida
    c = 160
    gx, gy = 1580, 470
    cv.grid(gx, gy, (0.85, 0.15, 0.15, 0.85), c, font=64)
    # flechas de cada neurona a su píxel: gruesas para los valores altos
    cv.arrow_curve((NX + 35, NY[0] - 36), (1080, 30), (1560, 150), (gx + c / 2, gy - 10), DARK, 13, 56)
    cv.arrow_curve((NX + 40, NY[1] - 30), (1120, 260), (1700, 280), (gx + 1.5 * c, gy - 10), DARK, 4, 28)
    cv.arrow_curve((NX + 40, NY[2] + 30), (1150, 830), (1560, 880), (gx + c / 2, gy + 2 * c + 10), DARK, 4, 28)
    cv.arrow_curve((NX + 35, NY[3] + 36), (1200, 1110), (1700, 1010), (gx + 1.5 * c, gy + 2 * c + 10), DARK, 13, 56)
    cv.save(path)


if __name__ == "__main__":
    main(sys.argv[1])
