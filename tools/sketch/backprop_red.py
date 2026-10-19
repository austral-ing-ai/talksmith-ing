"""Redibujo vectorial del diagrama de backpropagation del slide 32 (AIG4B Clase 8).

Red feed-forward 2 -> 3 -> 3 -> 1 (nodos azules, aristas negras) con una flecha roja de
ajuste (sube / baja) sobre cada peso, el recuadro "Error plot" y los rótulos
"Prediction" / "Error". Coordenadas tomadas del original.
Salida: talks/redes-generativas-antagonicas/images/backprop-red.svg
"""
import math
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "talks/redes-generativas-antagonicas/images/backprop-red.svg"
INK, DARK, RED, BLUE = "#3B3535", "#1F1E1E", "#DA1B2E", "#3A7BBF"
R = 46

N = {
    "i1": (378, 413), "i2": (378, 707),
    "a1": (713, 257), "a2": (713, 560), "a3": (713, 877),
    "b1": (1080, 257), "b2": (1080, 560), "b3": (1080, 877),
    "o": (1397, 560),
}
# (origen, destino, x donde va la flecha roja, sentido)
EDGES = [
    ("i1", "a1", 505, "up"), ("i1", "a2", 595, "down"), ("i1", "a3", 567, "up"),
    ("i2", "a1", 595, "down"), ("i2", "a2", 595, "up"), ("i2", "a3", 505, "down"),
    ("a1", "b1", 897, "down"), ("a1", "b2", 820, "up"), ("a1", "b3", 935, "down"),
    ("a2", "b1", 935, "down"), ("a2", "b2", 830, "up"), ("a2", "b3", 935, "up"),
    ("a3", "b1", 935, "down"), ("a3", "b2", 830, "up"), ("a3", "b3", 897, "up"),
    ("b1", "o", 1250, "up"), ("b2", "o", 1200, "down"), ("b3", "o", 1250, "down"),
]


def block_arrow(cx, cy, direction):
    hw, hh, sw, sh = 32, 32, 12, 32   # media cabeza, alto cabeza, medio fuste, alto fuste
    s = -1 if direction == "up" else 1
    tip = cy + s * (hh + sh) / 2
    base = tip - s * hh
    end = base - s * sh
    return (f'<path d="M{cx},{tip:.1f} L{cx + hw},{base:.1f} L{cx + sw},{base:.1f} L{cx + sw},{end:.1f} '
            f'L{cx - sw},{end:.1f} L{cx - sw},{base:.1f} L{cx - hw},{base:.1f} z" fill="{RED}"/>')


def main():
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="302 30 1605 923" font-family="Helvetica, Arial, sans-serif" fill="#1F1E1E">',
         '<title>Backpropagation</title>',
         '<desc>Redibujo del slide 32: red 2-3-3-1 con nodos azules; cada peso lleva una flecha roja que indica si se ajusta hacia arriba o hacia abajo; '
         'el error de la predicción se ve en la curva en U del recuadro Error plot.</desc>',
         '<defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="24" markerHeight="20" viewBox="0 0 24 20" refX="23" refY="10" orient="auto">'
         f'<path d="M0,0 L24,10 L0,20 z" fill="{DARK}"/></marker>'
         '<marker id="ahs" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="14" viewBox="0 0 16 14" refX="15" refY="7" orient="auto">'
         f'<path d="M0,0 L16,7 L0,14 z" fill="{DARK}"/></marker></defs>',
         '<rect x="302" y="30" width="1605" height="923" fill="#ffffff"/>']

    arrows = []
    for a, b, ax, d in EDGES:
        (x1, y1), (x2, y2) = N[a], N[b]
        L = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        sx, sy = x1 + ux * (R + 2), y1 + uy * (R + 2)
        ex, ey = x2 - ux * (R + 2), y2 - uy * (R + 2)
        o.append(f'<path d="M{sx:.1f},{sy:.1f} L{ex:.1f},{ey:.1f}" stroke="{DARK}" stroke-width="4" marker-end="url(#ah)"/>')
        t = (ax - x1) / (x2 - x1)
        arrows.append(block_arrow(ax, y1 + t * (y2 - y1), d))
    o.extend(arrows)
    for x, y in N.values():
        o.append(f'<circle cx="{x}" cy="{y}" r="{R}" fill="{BLUE}"/>')

    # recuadro Error plot
    ox, oy = 1452, 325
    o.append(f'<path d="M{ox},{oy + 4} V62" stroke="{DARK}" stroke-width="2.5" marker-end="url(#ahs)"/>')
    o.append(f'<path d="M{ox - 4},{oy} H1878" stroke="{DARK}" stroke-width="2.5" marker-end="url(#ahs)"/>')
    pts = []
    for i in range(61):
        x = 1456 + (1852 - 1456) * i / 60
        if x <= 1655:
            y = 268 - 158 * ((1655 - x) / 199) ** 2
        else:
            y = 268 - 168 * ((x - 1655) / 197) ** 2
        pts.append(f"{x:.1f},{y:.1f}")
    o.append(f'<path d="M{" L".join(pts)}" stroke="{DARK}" stroke-width="4.5" fill="none" stroke-linecap="round"/>')
    o.append('<text x="1648" y="383" font-size="50" text-anchor="middle">Error plot</text>')

    o.append('<text x="1700" y="602" font-size="82" text-anchor="middle">Prediction</text>')
    o.append('<text x="1700" y="708" font-size="44" text-anchor="middle">Error</text>')
    o.append('</svg>')
    OUT.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
