"""Redibujo vectorial del slide 36 (AIG4B Clase 8): el error del Discriminador.

Generador (rojo): z en [0, 1] y Bias alimentan cuatro nodos σ que producen la imagen 2x2
(0.25, 1 / 0.5, 0.75). Discriminador (azul): cuatro entradas + Bias hacia σ, que da 0.68.
Quería 0, así que Error = -ln(1-0.68). Coordenadas tomadas del original.
Salida: talks/redes-generativas-antagonicas/images/error-discriminador.svg
"""
import math
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "talks/redes-generativas-antagonicas/images/error-discriminador.svg"
INK, DARK, RED, BLUE, GREEN, NODE = "#3B3535", "#1F1E1E", "#DA1B2E", "#1F5BAA", "#3A9A45", "#3B3535"
SERIF = "'Times New Roman', Times, serif"
R = 44


def marker(mid, color, w=20, h=16):
    return (f'<marker id="{mid}" markerUnits="userSpaceOnUse" markerWidth="{w}" markerHeight="{h}" viewBox="0 0 {w} {h}" '
            f'refX="{w - 1}" refY="{h / 2}" orient="auto"><path d="M0,0 L{w},{h / 2} L0,{h} z" fill="{color}"/></marker>')


def edge(p, q, color, mid, r1=R, r2=R, width=4):
    (x1, y1), (x2, y2) = p, q
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    return (f'<path d="M{x1 + ux * r1:.1f},{y1 + uy * r1:.1f} L{x2 - ux * (r2 + 1):.1f},{y2 - uy * (r2 + 1):.1f}" '
            f'stroke="{color}" stroke-width="{width}" marker-end="url(#{mid})"/>')


def node(x, y, label="", r=R, fs=44, sigma=False):
    s = f'<circle cx="{x}" cy="{y}" r="{r}" fill="{NODE}"/>'
    if sigma:
        s += f'<text x="{x}" y="{y + fs * 0.28:.1f}" font-family="{SERIF}" font-style="italic" font-size="{fs}" text-anchor="middle" fill="#ffffff">σ</text>'
    elif label:
        s += f'<text x="{x}" y="{y + fs * 0.36:.1f}" font-size="{fs}" text-anchor="middle" fill="#ffffff">{label}</text>'
    return s


def main():
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="18 6 2016 962" font-family="Helvetica, Arial, sans-serif" fill="#1F1E1E">',
         '<title>El error del Discriminador</title>',
         '<desc>Redibujo del slide 36: el Generador (rojo) toma z y un Bias y produce una imagen 2x2 (0.25, 1, 0.5, 0.75); '
         'el Discriminador (azul) la recibe con su propio Bias y su sigmoid da 0.68. Quería 0: Error = -ln(1-0.68).</desc>',
         '<defs>' + marker("ar", RED) + marker("ab", BLUE) + marker("ak", DARK, 24, 20) + '</defs>',
         '<rect x="18" y="6" width="2016" height="962" fill="#ffffff"/>']

    # títulos
    o.append(f'<text x="543" y="92" font-size="72" text-anchor="middle" fill="{RED}">Generator</text>')
    o.append(f'<text x="1465" y="84" font-size="72" text-anchor="middle" fill="{BLUE}">Discriminator</text>')

    # slider de z
    o.append(f'<path d="M60,287 H283 M60,270 V304 M283,270 V304" stroke="{DARK}" stroke-width="5" fill="none"/>')
    o.append(f'<circle cx="108" cy="287" r="19" fill="{GREEN}"/>')
    o.append('<text x="170" y="258" font-size="54" text-anchor="middle">z</text>')
    o.append('<text x="62" y="360" font-size="54" text-anchor="middle">0</text>')
    o.append('<text x="273" y="360" font-size="54" text-anchor="middle">1</text>')

    # Generador
    gz, gb = (340, 305), (340, 568)
    sig = [(745, 170), (745, 333), (745, 497), (745, 660)]
    for s in sig:
        o.append(edge(gz, s, RED, "ar"))
        o.append(edge(gb, s, RED, "ar"))
    o.append(node(*gz, "z", fs=48))
    o.append(node(*gb, "1", fs=48))
    o.append('<text x="340" y="690" font-size="56" text-anchor="middle">Bias</text>')
    for s in sig:
        o.append(node(*s, sigma=True, fs=56))

    # imagen 2x2
    cells = [(873, 300, "0.25", "#D9D9D9", DARK), (1022, 300, "1", "#000000", "#ffffff"),
             (873, 407, "0.5", "#A6A6A6", DARK), (1022, 407, "0.75", "#4A4A4A", "#ffffff")]
    for x, y, t, f, c in cells:
        o.append(f'<rect x="{x}" y="{y}" width="149" height="107" fill="{f}"/>')
        o.append(f'<text x="{x + 74.5}" y="{y + 73}" font-size="54" text-anchor="middle" fill="{c}">{t}</text>')
    o.append(f'<rect x="873" y="300" width="298" height="214" fill="none" stroke="#000000" stroke-width="7"/>')
    o.append('<path d="M1022,300 V514 M873,407 H1171" stroke="#000000" stroke-width="5"/>')

    # Discriminador
    din = [(1300, 170), (1300, 333), (1300, 497), (1300, 660)]
    dbias, dout = (1300, 828), (1668, 497)
    curves = [
        "M935,296 C960,180 1050,100 1140,102 C1190,104 1230,120 1257,145",
        "M1080,292 C1100,230 1130,186 1170,187 C1220,190 1250,250 1265,300",
        "M940,532 C960,610 1010,690 1100,678 C1170,668 1240,600 1272,532",
        "M1097,532 C1095,620 1110,720 1170,722 C1210,723 1240,710 1262,697",
    ]
    for d in curves:
        o.append(f'<path d="{d}" stroke="{DARK}" stroke-width="5" fill="none" marker-end="url(#ak)"/>')
    for p in din + [dbias]:
        o.append(edge(p, dout, BLUE, "ab", r2=62))
    for p in din:
        o.append(node(*p))
    o.append(node(*dbias, "1", fs=48))
    o.append('<text x="1300" y="940" font-size="56" text-anchor="middle">Bias</text>')
    o.append(node(*dout, r=62, sigma=True, fs=80))

    o.append('<text x="1855" y="530" font-size="92" text-anchor="middle">0.68</text>')
    o.append(f'<text x="1763" y="262" font-size="60" text-anchor="middle" fill="{BLUE}">Want 0</text>')
    o.append(f'<text x="1765" y="340" font-size="60" text-anchor="middle" fill="{BLUE}">Error = -ln(1-0.68)</text>')
    o.append('</svg>')
    OUT.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
