"""SVG del Discriminador como red: grilla (1,0/0,1) → 4 entradas → salida, pesos +1/-1/-1/+1 y bias -1."""
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from slanted import Canvas, discriminator  # noqa: E402

W, H = 1370, 940


def main(path):
    cv = Canvas(W, H, "Discriminador como red",
                "La grilla 2×2 de la cara prototipo (1, 0 / 0, 1) alimenta cuatro neuronas de entrada, conectadas a "
                "una neurona de salida con pesos +1 (rojo), -1, -1 (azul) y +1 (rojo); un nodo Bias de valor 1 "
                "aporta con peso -1 (verde).")
    discriminator(cv, (1, 0, 0, 1), ox=-40, oy=0)
    cv.save(path)


if __name__ == "__main__":
    main(sys.argv[1])
