"""SVG de "Cálculo del score": Faces y Noise con pesos + (rojo) en la diagonal principal y - (azul) en la secundaria."""
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from slanted import BLUE, RED, Canvas, weight_panel  # noqa: E402

W, H = 1440, 690


def main(path):
    cv = Canvas(W, H, "Pesos más y menos",
                "Grillas Faces (1, 0 / 0, 1) y Noise (0.25, 1 / 0.5, 0.75), cada una con un peso + en rojo en las "
                "esquinas de la diagonal principal y un peso - en azul en las de la secundaria.")
    plus, minus = ("+", RED, 0), ("-", BLUE, 0)
    tags = [plus, minus, minus, plus]
    weight_panel(cv, 352, "Faces", (1, 0, 0, 1), tags)
    weight_panel(cv, 1088, "Noise", (0.25, 1, 0.5, 0.75), tags)
    cv.save(path)


if __name__ == "__main__":
    main(sys.argv[1])
