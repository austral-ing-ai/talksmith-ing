"""SVG de "¿qué píxeles importan?": Faces (1,0/0,1) con pesos Big/small y Noise con pesos any."""
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from slanted import BLUE, GREEN, RED, Canvas, weight_panel  # noqa: E402

W, H = 1440, 690


def main(path):
    cv = Canvas(W, H, "Pesos Big y small",
                "Grilla Faces (1, 0 / 0, 1) con etiquetas Big en rojo sobre la diagonal principal y small en azul "
                "sobre la secundaria; grilla Noise (0.25, 1 / 0.5, 0.75) con etiquetas any en verde en las cuatro esquinas.")
    big, small = ("Big", RED, 64), ("small", BLUE, 44)
    any_ = ("any", GREEN, 46)
    weight_panel(cv, 352, "Faces", (1, 0, 0, 1), [big, small, small, big])
    weight_panel(cv, 1088, "Noise", (0.25, 1, 0.5, 0.75), [any_] * 4)
    cv.save(path)


if __name__ == "__main__":
    main(sys.argv[1])
