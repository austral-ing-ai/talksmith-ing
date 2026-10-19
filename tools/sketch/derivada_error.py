"""Redibujo vectorial del slide 37 (AIG4B Clase 8): la derivada del error del Discriminador.

Izquierda: imagen 2x2 (1, 0 / 0, 1) -> entradas x1..x4 -> pesos w1..w4 (rojo) y bias b (azul) -> σ.
Derecha: Prediction, Loss function y Derivatives, compuestas como texto posicionado
(fracciones apiladas con raya, subíndices como nodos <text> más chicos y desplazados).
Cada pieza es un <text> anclado a la izquierda y de un solo estilo; los anchos salen de
las métricas reales de Times New Roman / Helvetica (_metrics.py).
Salida: talks/redes-generativas-antagonicas/images/derivada-error.svg
"""
import math
from pathlib import Path

from _metrics import width

OUT = Path(__file__).resolve().parents[2] / "talks/redes-generativas-antagonicas/images/derivada-error.svg"
INK, DARK, RED, BLUE, NODE = "#3B3535", "#1F1E1E", "#B8231B", "#1F5BAA", "#3B3535"
SERIF = "'Times New Roman', Times, serif"
FAMILY = {"serif": SERIF, "serif-italic": SERIF, "sans": "Helvetica, Arial, sans-serif"}
S = 44            # cuerpo de las fórmulas
SUB = 0.66        # escala de subíndices / superíndices

# ---------------------------------------------------------------- motor de fórmulas
# Un "item" es una tupla; measure() da su ancho y render() emite SVG en (x, baseline).
#   ("t", texto, cara, color)        texto al cuerpo S
#   ("_", texto, cara, color)        subíndice
#   ("^", texto, cara, color)        superíndice
#   ("/", [items num], [items den], color_raya)   fracción apilada
#   ("sum", "4", "j=1")              sumatoria con límites
#   ("sp", ancho)                    espacio


def T(s, color=DARK):
    return ("t", s, "serif", color)


def I(s, color=DARK):
    return ("t", s, "serif-italic", color)


def sub(s, color=DARK, face="serif"):
    return ("_", s, face, color)


def frac(num, den, color=DARK):
    return ("/", num, den, color)


def sp(w):
    return ("sp", w)


def measure(it, size):
    k = it[0]
    if k == "t":
        return width(it[1], size, it[2])
    if k in "_^":
        return width(it[1], size * SUB, it[2]) + size * 0.04
    if k == "/":
        return max(seq_w(it[1], size), seq_w(it[2], size)) + size * 0.3
    if k == "sum":
        return max(width("Σ", size * 1.45, "serif"), width(it[2], size * 0.7, "serif")) + size * 0.06
    if k == "sp":
        return it[1]
    raise ValueError(k)


def seq_w(items, size):
    return sum(measure(i, size) for i in items)


def text(x, y, s, size, face, color):
    style = ' font-style="italic"' if face == "serif-italic" else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FAMILY[face]}"{style} font-size="{size:.1f}" '
            f'fill="{color}">{s}</text>')


def render(items, x, y, size, out):
    for it in items:
        k = it[0]
        w = measure(it, size)
        if k == "t":
            # los espacios de borde se colapsan al renderizar: se convierten en desplazamiento
            body = it[1].strip()
            lead = width(it[1][: len(it[1]) - len(it[1].lstrip())], size, it[2])
            out.append(text(x + lead, y, body, size, it[2], it[3]))
        elif k == "_":
            out.append(text(x + size * 0.02, y + size * 0.24, it[1], size * SUB, it[2], it[3]))
        elif k == "^":
            out.append(text(x + size * 0.02, y - size * 0.42, it[1], size * SUB, it[2], it[3]))
        elif k == "/":
            axis = y - size * 0.27
            nw, dw = seq_w(it[1], size), seq_w(it[2], size)
            out.append(f'<path d="M{x + size * 0.06:.1f},{axis:.1f} h{w - size * 0.12:.1f}" stroke="{it[3]}" stroke-width="{size * 0.05:.1f}"/>')
            render(it[1], x + (w - nw) / 2, axis - size * 0.24, size, out)
            render(it[2], x + (w - dw) / 2, axis + size * 0.92, size, out)
        elif k == "sum":
            big = size * 1.45
            gw = width("Σ", big, "serif")
            cx = x + w / 2
            out.append(text(cx - gw / 2, y + size * 0.16, "Σ", big, "serif", DARK))
            ls = size * 0.7
            uw = width(it[1], ls, "serif")
            out.append(text(cx - uw / 2, y - size * 1.0, it[1], ls, "serif", DARK))
            var, rest = it[2].split("=")
            lw = width(var, ls, "serif-italic") + width("=" + rest, ls, "serif")
            out.append(text(cx - lw / 2, y + size * 0.95, var, ls, "serif-italic", DARK))
            out.append(text(cx - lw / 2 + width(var, ls, "serif-italic"), y + size * 0.95, "=" + rest, ls, "serif", DARK))
        x += w
    return x


def line(items, x, y, out, size=S, center=False):
    if center:
        x -= seq_w(items, size) / 2
    return render(items, x, y, size, out)


# ---------------------------------------------------------------- red de la izquierda
def marker(mid, color, w=22, h=18):
    return (f'<marker id="{mid}" markerUnits="userSpaceOnUse" markerWidth="{w}" markerHeight="{h}" viewBox="0 0 {w} {h}" '
            f'refX="{w - 1}" refY="{h / 2}" orient="auto"><path d="M0,0 L{w},{h / 2} L0,{h} z" fill="{color}"/></marker>')


def sans_label(out, cx, cy, base, idx, color, size=48):
    """Rótulo tipo x1 / w1 en sans: letra + subíndice, centrado en (cx, cy) con fondo blanco."""
    wb = width(base, size, "sans")
    wi = width(idx, size * 0.62, "sans") if idx else 0
    tw = wb + wi + 2
    x0 = cx - tw / 2
    out.append(f'<rect x="{x0 - 6:.1f}" y="{cy - size * 0.55:.1f}" width="{tw + 12:.1f}" height="{size * 1.05:.1f}" fill="#ffffff"/>')
    out.append(f'<text x="{x0:.1f}" y="{cy + size * 0.26:.1f}" font-size="{size}" fill="{color}">{base}</text>')
    if idx:
        out.append(f'<text x="{x0 + wb + 2:.1f}" y="{cy + size * 0.42:.1f}" font-size="{size * 0.62:.1f}" fill="{color}">{idx}</text>')


def network(out):
    out.append(f'<text x="510" y="138" font-size="100" text-anchor="middle" fill="{DARK}">Discriminator</text>')
    # flechas curvas desde la imagen a las entradas (se dibujan antes que la grilla)
    curves = [
        ("M138,446 C150,330 215,262 300,250 C420,232 520,240 597,258", (290, 256), "1"),
        ("M340,444 C380,405 420,392 470,397 C520,402 560,418 600,437", (474, 398), "2"),
        ("M135,686 C165,760 215,812 300,815 C420,818 530,760 604,694", (278, 812), "3"),
        ("M315,686 C318,770 380,830 460,842 C520,850 560,855 597,860", (474, 845), "4"),
    ]
    for d, *_ in curves:
        out.append(f'<path d="{d}" stroke="{DARK}" stroke-width="5" fill="none" marker-end="url(#ak)"/>')
    for _, (cx, cy), i in curves:
        sans_label(out, cx, cy, "x", i, DARK)
    # imagen 2x2
    for x, y, t, f, c in [(58, 452, "1", "#000000", "#ffffff"), (208, 452, "0", "#ffffff", "#000000"),
                          (58, 560, "0", "#ffffff", "#000000"), (208, 560, "1", "#000000", "#ffffff")]:
        out.append(f'<rect x="{x}" y="{y}" width="150" height="108" fill="{f}"/>')
        out.append(f'<text x="{x + 75}" y="{y + 72}" font-size="52" text-anchor="middle" fill="{c}">{t}</text>')
    out.append('<rect x="58" y="452" width="300" height="216" fill="none" stroke="#000000" stroke-width="8"/>')

    nodes = [(643, 268), (643, 462), (643, 662), (643, 862)]
    bias, sig = (643, 1063), (1112, 650)
    r = 45
    labels = [(787, 378), (762, 515), (760, 666), (788, 800)]
    for k, (p, lab) in enumerate(zip(nodes + [bias], labels + [(808, 925)])):
        (x1, y1), (x2, y2) = p, sig
        L = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        col = RED if k < 4 else BLUE
        mid = "ar" if k < 4 else "ab"
        out.append(f'<path d="M{x1 + ux * r:.1f},{y1 + uy * r:.1f} L{x2 - ux * (r + 1):.1f},{y2 - uy * (r + 1):.1f}" '
                   f'stroke="{col}" stroke-width="4" marker-end="url(#{mid})"/>')
        # el rótulo se apoya sobre la arista: proyectamos su x sobre la recta
        lx = lab[0]
        ly = y1 + (lx - x1) / (x2 - x1) * (y2 - y1)
        if k < 4:
            sans_label(out, lx, ly, "w", str(k + 1), col)
        else:
            sans_label(out, lx, ly, "b", "", col, size=54)
    for x, y in nodes:
        out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{NODE}"/>')
    out.append(f'<circle cx="{bias[0]}" cy="{bias[1]}" r="{r}" fill="{NODE}"/>')
    out.append(f'<text x="{bias[0]}" y="{bias[1] + 14}" font-size="38" text-anchor="middle" fill="#ffffff">1</text>')
    out.append(f'<text x="522" y="1082" font-size="50" text-anchor="middle" fill="{DARK}">Bias</text>')
    out.append(f'<circle cx="{sig[0]}" cy="{sig[1]}" r="{r}" fill="{NODE}"/>')
    out.append(f'<text x="{sig[0]}" y="{sig[1] + 18}" font-family="{SERIF}" font-style="italic" font-size="68" text-anchor="middle" fill="#ffffff">σ</text>')


# ---------------------------------------------------------------- fórmulas
def formulas(out):
    head = lambda x, y, s: out.append(f'<text x="{x}" y="{y}" font-size="38" text-anchor="middle" fill="{DARK}">{s}</text>')
    CX = 1540

    head(CX, 96, "Prediction")
    pred = [I("D"), T("("), I("x"), T(") = "), I("σ"), T("(")]
    for i in "1234":
        pred += [I("x"), sub(i), I("w", RED), sub(i, RED)]
        if i != "4":
            pred.append(T("+"))
    pred += [T(" + "), I("b", BLUE), T(")")]
    line(pred, CX, 150, out, center=True)

    head(CX, 222, "Loss function (error) from images")
    line([I("E"), T(" = − ln("), I("D"), T("("), I("x"), T("))")], CX, 274, out, center=True)

    head(CX, 352, "Derivatives")

    dE, dD = [T("∂"), I("E")], [T("∂"), I("D")]
    dwi = [T("∂"), I("w"), sub("i", face="serif-italic")]
    dEw_red = frac([T("∂", RED), I("E", RED)], [T("∂", RED), I("w", RED), sub("i", RED, "serif-italic")], RED)
    dot = [T(" · ")]
    eq = [T(" = ")]
    m1_Dx = frac([T("−1")], [I("D"), T("("), I("x"), T(")")])
    sumterm = [("sum", "4", "j=1"), sp(4), I("x"), sub("j", face="serif-italic"), I("w"), sub("j", face="serif-italic"), T(" + "), I("b"), T(")")]
    xi = [I("x"), sub("i", face="serif-italic")]
    one_minus_D = [T("[1 − "), I("D"), T("("), I("x"), T(")]")]

    X0 = 1190
    yA = 445
    xe = line([dEw_red] + eq + [frac(dE, dD)] + dot + [frac(dD, dwi)], X0, yA, out)
    xeq = X0 + measure(dEw_red, S)   # columna del "="

    yB = 570
    lineB = eq + [m1_Dx] + dot + [I("σ"), T("(")] + sumterm + [T("[1 − "), I("σ"), T("(")] + sumterm + [T("]")] + xi
    line(lineB, xeq, yB, out)

    yC = 690
    line(eq + [m1_Dx] + dot + [I("D"), T("("), I("x"), T(")")] + one_minus_D + xi, xeq, yC, out)

    yD = 785
    line(eq + [T("− ")] + one_minus_D + xi, xeq, yD, out)

    yE = 900
    dEb = frac([T("∂", BLUE), I("E", BLUE)], [T("∂", BLUE), I("b", BLUE)], BLUE)
    line([dEb] + eq + [frac(dE, dD)] + dot + [frac(dD, [T("∂"), I("b")])] + eq + [T("− ")] + one_minus_D, X0, yE, out)
    return seq_w(lineB, S) + xeq


# Escalas: la red se reduce y las fórmulas se agrandan para que el texto se lea en el slide
# (el original las tenía al mismo cuerpo que la red, ilegibles a media pantalla).
# El espaciado vertical de las fórmulas es más compacto que en el original para que todo
# entre en un lienzo ~2:1, que es la caja que el slide le da a la imagen.
NET_K, NET_DY = 0.75, 75
F_K, F_DX, F_DY = 1.1, -345, -45


def main():
    net, fx = [], []
    network(net)
    right = formulas(fx)
    vw = F_DX + right * F_K + 32
    vh = 1010
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="20 0 {vw - 20:.0f} {vh}" font-family="Helvetica, Arial, sans-serif" fill="{DARK}">',
         '<title>Derivada del error del Discriminador</title>',
         '<desc>Redibujo del slide 37: red del Discriminador (imagen 2x2, entradas x1 a x4, pesos w1 a w4, bias b, sigmoid) '
         'y las fórmulas: predicción D(x), función de pérdida E = -ln(D(x)) y sus derivadas respecto de cada peso y del bias.</desc>',
         '<defs>' + marker("ak", DARK, 26, 22) + marker("ar", RED) + marker("ab", BLUE) + '</defs>',
         f'<rect x="20" y="0" width="{vw - 20:.0f}" height="{vh}" fill="#ffffff"/>',
         f'<g transform="translate(0 {NET_DY}) scale({NET_K})">'] + net + ['</g>',
         f'<g transform="translate({F_DX} {F_DY}) scale({F_K})">'] + fx + ['</g>', '</svg>']
    OUT.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(OUT, "ancho", round(vw))


if __name__ == "__main__":
    main()
