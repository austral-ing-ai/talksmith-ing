"""SVG del ciclo completo: Generador (rojo) produce (0.25, 1 / 0.5, 0.75) y el Discriminador (azul) da σ = 0.68."""
import math
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from slanted import BLUE, DARK, RED, Canvas  # noqa: E402

W, H = 2010, 1030
R = 52


def main(path):
    cv = Canvas(W, H, "Generador y Discriminador",
                "A la izquierda, el Generador (en rojo): z, elegido con un deslizador de 0 a 1, y un Bias de valor 1 conectados "
                "a cuatro neuronas σ. En el centro, la imagen 2×2 que produce (0.25, 1 / 0.5, 0.75). A la derecha, el "
                "Discriminador (en azul): cuatro neuronas de entrada y un Bias conectados a una neurona σ que da 0.68.")
    cv.text(540, 100, "Generator", 86, RED)
    cv.text(1480, 92, "Discriminator", 86, BLUE)
    # generador
    cv.slider(40, 270, 315, 0.22, dot_r=19, font=58)
    cv.text(158, 268, "z", 66, DARK)
    z, bias = (345, 330), (345, 600)
    gys = [195, 362, 530, 697]
    gn = [(750, y) for y in gys]
    for src in (z, bias):
        for n in gn:
            cv.arrow_line(src, n, RED, 3.5, 24, r_from=R, r_to=R)
    cv.node(*z, R, "z", 54)
    cv.node(*bias, R, "1", 48)
    cv.text(bias[0], bias[1] + R + 74, "Bias", 64, DARK)
    for n in gn:
        cv.node(*n, R, "σ", 62, italic=True)
    # imagen generada
    c = 150
    gx, gy = 880, 330
    cv.grid(gx, gy, (0.25, 1, 0.5, 0.75), c, font=62)
    # discriminador
    dn = [(1320, y) for y in (195, 362, 530, 697)]
    db = (1320, 868)
    out = (1690, 530)
    ang = math.radians(195)
    def edge(n, deg):
        a = math.radians(deg)
        return (n[0] + R * math.cos(a), n[1] + R * math.sin(a))
    cv.arrow_curve((gx + c / 2, gy - 8), (gx + 60, 40), (1150, 110), edge(dn[0], 200), DARK, 5, 30)
    cv.arrow_curve((gx + 1.5 * c, gy - 8), (1120, 170), (1270, 170), edge(dn[1], 245), DARK, 5, 30)
    cv.arrow_curve((gx + c / 2, gy + 2 * c + 8), (gx + 110, 820), (1200, 720), edge(dn[2], 125), DARK, 5, 30)
    cv.arrow_curve((gx + 1.5 * c, gy + 2 * c + 8), (1095, 860), (1180, 830), edge(dn[3], 160), DARK, 5, 30)
    del ang
    for n in dn + [db]:
        cv.arrow_line(n, out, BLUE, 3.5, 24, r_from=R, r_to=68)
    for n in dn:
        cv.node(*n, R)
    cv.node(*db, R, "1", 48)
    cv.text(db[0], db[1] + R + 74, "Bias", 64, DARK)
    cv.node(*out, 68, "σ", 80, italic=True)
    cv.text(out[0] + 92, out[1] + 37, "0.68", 104, DARK, anchor="start")
    cv.save(path)


if __name__ == "__main__":
    main(sys.argv[1])
