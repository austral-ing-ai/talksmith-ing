"""SVG del Discriminador evaluando la imagen de ruido (0.25,1/0.5,0.75): σ(-0.5) = 0.37."""
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from slanted import DARK, Canvas, discriminator  # noqa: E402

W, H = 1910, 940


def main(path):
    cv = Canvas(W, H, "Discriminador con ruido",
                "La imagen de ruido (0.25, 1 / 0.5, 0.75) pasa por la red del Discriminador, con pesos +1, -1, -1, +1 "
                "y bias -1; la salida es σ(-0.5) = 0.37.")
    out = discriminator(cv, (0.25, 1, 0.5, 0.75), ox=-40, oy=0)
    cv.text(out[0] + 80, out[1] + 30, "σ(-0.5) = 0.37", 84, DARK, anchor="start")
    cv.save(path)


if __name__ == "__main__":
    main(sys.argv[1])
