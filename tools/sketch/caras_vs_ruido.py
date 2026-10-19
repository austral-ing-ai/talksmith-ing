"""SVG de "Caras vs. ruido": barra de grises 0..1 y dos filas de grillas 2×2 (Faces / Noise)."""
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from slanted import DARK, Canvas  # noqa: E402

W, H = 1290, 975
CELL = 140
FACES = [(0.75, 0, 0, 0.75), (1, 0.25, 0.25, 0.75), (1, 0, 0, 1), (0.75, 0, 0.25, 0.75)]
# La cuarta grilla de ruido aparece cortada en el original: se ven 1, 1 (arriba), 0 y 0.75 (abajo).
NOISE = [(0.25, 0, 1, 0.75), (0.25, 1, 0.5, 0.75), (0.75, 0.5, 0.75, 0), (1, 1, 0, 0.75)]


def main(path):
    cv = Canvas(W, H, "Caras vs. ruido",
                "Escala de grises de 0 (blanco) a 1 (negro). Fila Faces: cuatro grillas 2×2 con la diagonal "
                "principal oscura. Fila Noise: cuatro grillas 2×2 con valores sin patrón.")
    # barra de grises arriba, centrada sobre las grillas
    bx0, bx1 = 400, 890
    grad = ('<linearGradient id="g01" x1="0" y1="0" x2="1" y2="0">'
            '<stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#000000"/></linearGradient>')
    cv.add(f'<rect x="{bx0}" y="24" width="{bx1 - bx0}" height="70" fill="url(#g01)" stroke="{DARK}" stroke-width="2"/>')
    cv.text(bx0, 158, "0", 60, DARK)
    cv.text(bx1, 158, "1", 60, DARK)
    # cada fila con su rótulo arriba (más compacto que a la izquierda: deja grillas más grandes en la slide)
    gx0, gap = 25, 40
    for label, data, top in (("Faces", FACES, 280), ("Noise", NOISE, 675)):
        cv.text(gx0, top - 26, label, 64, DARK, anchor="start")
        for k, vals in enumerate(data):
            cv.grid(gx0 + k * (2 * CELL + gap), top, vals, CELL, font=54)
    cv.save(path, grad)


if __name__ == "__main__":
    main(sys.argv[1])
