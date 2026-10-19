"""Piezas "limpias" de los diagramas de Slanted Land (estilo de diagrama del deck).

Grillas 2×2, nodos, flechas con <marker> en userSpaceOnUse, etiquetas con halo blanco.
Las personas y caras NO van acá: esas se dibujan a mano con sketch.py.
"""
import math

INK = "#3B3535"      # texto y trazos por defecto
DARK = "#1F1E1E"     # títulos, bordes fuertes
NODE = "#3B3535"     # relleno de neuronas
RED = "#DA1B2E"      # peso positivo / Big / +
BLUE = "#1F5FAD"     # peso negativo / small / -
GREEN = "#2E8540"    # bias / any / z
FONT = "Helvetica, Arial, sans-serif"


def gray(v):
    """0 = blanco, 1 = negro."""
    c = round(255 * (1 - v))
    return f"#{c:02x}{c:02x}{c:02x}"


def fmt(v):
    return f"{v:g}"


class Canvas:
    def __init__(self, w, h, title, desc):
        self.w, self.h = w, h
        self.title, self.desc = title, desc
        self.defs = {}
        self.body = []

    def add(self, s):
        self.body.append(s)

    def marker(self, color, size):
        mid = f"ah-{color.lstrip('#')}-{int(size)}"
        if mid not in self.defs:
            self.defs[mid] = (
                f'<marker id="{mid}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="{size:.0f}" '
                f'markerHeight="{size:.0f}" markerUnits="userSpaceOnUse" orient="auto">'
                f'<path d="M0,0 L10,5 L0,10 z" fill="{color}"/></marker>')
        return mid

    def svg(self, extra_defs=""):
        out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
               f'width="{self.w}" height="{self.h}" font-family="{FONT}">',
               f"<title>{self.title}</title>", f"<desc>{self.desc}</desc>"]
        if self.defs or extra_defs:
            out.append("<defs>" + "".join(self.defs.values()) + extra_defs + "</defs>")
        out.append(f'<rect width="{self.w}" height="{self.h}" fill="#ffffff"/>')
        out += self.body
        out.append("</svg>")
        return "\n".join(out)

    def save(self, path, extra_defs=""):
        open(path, "w").write(self.svg(extra_defs))

    # ---------- primitivas ----------
    def text(self, x, y, s, size, color=INK, anchor="middle", weight="normal", italic=False):
        st = ' font-style="italic"' if italic else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{color}" text-anchor="{anchor}" '
                 f'font-weight="{weight}"{st}>{s}</text>')

    def halo_text(self, x, y, s, size, color, pad=6):
        """Etiqueta centrada en (x, y) con un rectángulo blanco detrás, para cortar la línea."""
        w = len(s) * size * 0.58 + 2 * pad
        h = size * 0.95
        self.add(f'<rect x="{x - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" fill="#ffffff"/>')
        self.text(x, y + size * 0.36, s, size, color)

    def grid(self, x, y, vals, cell, numbers=True, font=None, border=None):
        font = font or cell * 0.34
        border = border or max(3, cell * 0.035)
        for i, v in enumerate(vals):
            gx, gy = x + (i % 2) * cell, y + (i // 2) * cell
            self.add(f'<rect x="{gx:.1f}" y="{gy:.1f}" width="{cell}" height="{cell}" fill="{gray(v)}"/>')
            if numbers:
                tc = "#ffffff" if v >= 0.5 else INK
                self.text(gx + cell / 2, gy + cell / 2 + font * 0.36, fmt(v), font, tc)
        self.add(f'<line x1="{x + cell}" y1="{y}" x2="{x + cell}" y2="{y + 2 * cell}" stroke="{DARK}" stroke-width="{border * 0.5:.1f}"/>')
        self.add(f'<line x1="{x}" y1="{y + cell}" x2="{x + 2 * cell}" y2="{y + cell}" stroke="{DARK}" stroke-width="{border * 0.5:.1f}"/>')
        self.add(f'<rect x="{x}" y="{y}" width="{2 * cell}" height="{2 * cell}" fill="none" stroke="{DARK}" stroke-width="{border:.1f}"/>')

    def node(self, cx, cy, r, label=None, size=None, italic=False):
        self.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{NODE}"/>')
        if label is not None:
            size = size or r * 0.8
            self.text(cx, cy + size * 0.36, label, size, "#ffffff", italic=italic)

    def arrow_line(self, p, q, color, width, head, r_from=0, r_to=0):
        """Flecha recta de p a q; recorta los radios de los nodos y deja la punta sobre el borde."""
        dx, dy = q[0] - p[0], q[1] - p[1]
        d = math.hypot(dx, dy)
        ux, uy = dx / d, dy / d
        a = (p[0] + ux * r_from, p[1] + uy * r_from)
        tip = (q[0] - ux * r_to, q[1] - uy * r_to)
        b = (tip[0] - ux * head * 0.3, tip[1] - uy * head * 0.3)
        m = self.marker(color, head)
        self.add(f'<path d="M{a[0]:.1f},{a[1]:.1f} L{b[0]:.1f},{b[1]:.1f}" stroke="{color}" stroke-width="{width}" '
                 f'fill="none" marker-end="url(#{m})"/>')
        return a, tip

    def arrow_curve(self, p, c1, c2, q, color, width, head):
        """Bézier cúbica de p a q; la punta cae exactamente en q."""
        dx, dy = q[0] - c2[0], q[1] - c2[1]
        d = math.hypot(dx, dy)
        ux, uy = dx / d, dy / d
        b = (q[0] - ux * head * 0.3, q[1] - uy * head * 0.3)
        m = self.marker(color, head)
        self.add(f'<path d="M{p[0]:.1f},{p[1]:.1f} C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {b[0]:.1f},{b[1]:.1f}" '
                 f'stroke="{color}" stroke-width="{width}" fill="none" stroke-linecap="round" marker-end="url(#{m})"/>')

    def slider(self, x0, x1, y, value, value_label=None, dot_r=16, font=40, tick=18):
        """Deslizador 0..1 para z: línea con topes, 0 y 1 abajo, punto verde en el valor."""
        self.add(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{DARK}" stroke-width="5"/>')
        for x in (x0, x1):
            self.add(f'<line x1="{x}" y1="{y - tick}" x2="{x}" y2="{y + tick}" stroke="{DARK}" stroke-width="5"/>')
        self.text(x0, y + tick + font * 1.05, "0", font, DARK)
        self.text(x1, y + tick + font * 1.05, "1", font, DARK)
        dx = x0 + (x1 - x0) * value
        self.add(f'<circle cx="{dx:.1f}" cy="{y}" r="{dot_r}" fill="{GREEN}"/>')
        if value_label:
            self.text(dx, y - dot_r - 14, value_label, font, GREEN)


def point_on_line(p, q, t):
    return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)


# ---------- piezas compartidas entre figuras ----------

def weight_panel(cv, cx, title, vals, tags, cell=160, top=190):
    """Grilla 2×2 con título y cuatro etiquetas de peso en las esquinas (compacto: la grilla manda).

    tags: lista de 4 (texto_o_simbolo, color, tamaño_de_fuente) en orden TL, TR, BL, BR.
    Un texto "+" o "-" se dibuja como geometría (no como glifo).
    """
    gx0, gy0 = cx - cell, top
    gx1, gy1 = cx + cell, top + 2 * cell
    cv.text(cx, top - 50, title, 80, DARK)
    cv.grid(gx0, gy0, vals, cell, font=60)
    tw, th = 130, 110
    ty_top, ty_bot = top - 165, gy1 + 50
    spec = [
        (gx0 - 45 - tw, ty_top, "right", (gx0 - 2, gy0 - 10)),
        (gx1 + 45, ty_top, "left", (gx1 + 2, gy0 - 10)),
        (gx0 - 45 - tw, ty_bot, "right", (gx0 - 2, gy1 + 10)),
        (gx1 + 45, ty_bot, "left", (gx1 + 2, gy1 + 10)),
    ]
    for (label, color, fs), (bx, by, side, corner) in zip(tags, spec):
        cv.add(f'<rect x="{bx}" y="{by}" width="{tw}" height="{th}" fill="{color}"/>')
        mx, my = bx + tw / 2, by + th / 2
        if label == "+":
            k, t = 30, 10
            cv.add(f'<rect x="{mx - k}" y="{my - t / 2}" width="{2 * k}" height="{t}" fill="#ffffff"/>')
            cv.add(f'<rect x="{mx - t / 2}" y="{my - k}" width="{t}" height="{2 * k}" fill="#ffffff"/>')
        elif label == "-":
            k, t = 24, 10
            cv.add(f'<rect x="{mx - k}" y="{my - t / 2}" width="{2 * k}" height="{t}" fill="#ffffff"/>')
        else:
            cv.text(mx, my + fs * 0.36, label, fs, "#ffffff")
        sx = bx + tw if side == "right" else bx
        start = (sx, my)
        down = corner[1] > my
        c1 = (sx + (30 if side == "right" else -30), my)
        c2 = (corner[0], corner[1] + (-40 if down else 40))
        cv.arrow_curve(start, c1, c2, corner, color, 5, 30)


# Geometría de la red del Discriminador (sin escalar). Entradas: TL→n1, TR→n2, BL→n3, BR→n4.
D_CELL = 170
D_GRID = (100, 280)
D_NX = 820
D_NY = [80, 270, 460, 650]
D_BIAS = (820, 860)
D_OUT = (1320, 450)
D_R = 48
D_W = [("+1", RED, 7, 34), ("-1", BLUE, 4, 26), ("-1", BLUE, 4, 26), ("+1", RED, 7, 34)]


def discriminator(cv, vals, ox=0, oy=0, out_label=None, weight_labels=True, bias_label=True):
    """Dibuja la red completa del Discriminador con origen (ox, oy). Devuelve el centro del nodo de salida."""
    def P(x, y):
        return (ox + x, oy + y)
    gx, gy = P(*D_GRID)
    c = D_CELL
    cv.grid(gx, gy, vals, c, font=62)
    nodes = [P(D_NX, y) for y in D_NY]
    bias = P(*D_BIAS)
    out = P(*D_OUT)
    # flechas curvas negras: de cada píxel a su neurona de entrada
    tl_top = (gx + c / 2, gy - 8)
    tr_top = (gx + 1.5 * c, gy - 8)
    bl_bot = (gx + c / 2, gy + 2 * c + 8)
    br_bot = (gx + 1.5 * c, gy + 2 * c + 8)
    ang = math.radians(195)
    e1 = (nodes[0][0] + D_R * math.cos(ang), nodes[0][1] + D_R * math.sin(ang))
    cv.arrow_curve(tl_top, (tl_top[0] + 20, gy - 260), (nodes[0][0] - 380, nodes[0][1] - 60), e1, DARK, 5, 30)
    e2 = (nodes[1][0] + D_R * math.cos(ang), nodes[1][1] + D_R * math.sin(ang))
    cv.arrow_curve(tr_top, (tr_top[0] + 70, gy - 110), (nodes[1][0] - 200, nodes[1][1] - 50), e2, DARK, 5, 30)
    a3 = math.radians(145)
    e3 = (nodes[2][0] + D_R * math.cos(a3), nodes[2][1] + D_R * math.sin(a3))
    cv.arrow_curve(bl_bot, (bl_bot[0] + 60, gy + 2 * c + 230), (nodes[2][0] - 260, nodes[2][1] + 280), e3, DARK, 5, 30)
    a4 = math.radians(185)
    e4 = (nodes[3][0] + D_R * math.cos(a4), nodes[3][1] + D_R * math.sin(a4))
    cv.arrow_curve(br_bot, (br_bot[0] - 10, gy + 2 * c + 200), (nodes[3][0] - 260, nodes[3][1] - 20), e4, DARK, 5, 30)
    # pesos hacia la salida
    for n, (lab, col, w, head) in zip(nodes, D_W):
        a, tip = cv.arrow_line(n, out, col, w, head, r_from=D_R, r_to=D_R)
        if weight_labels:
            lx, ly = point_on_line(a, tip, 0.3)
            cv.halo_text(lx, ly, lab, 64, col)
    a, tip = cv.arrow_line(bias, out, GREEN, 4, 26, r_from=D_R, r_to=D_R)
    if weight_labels:
        lx, ly = point_on_line(a, tip, 0.35)
        cv.halo_text(lx, ly, "-1", 64, GREEN)
    for n in nodes:
        cv.node(*n, D_R)
    cv.node(*bias, D_R, "1", 46)
    if bias_label:
        cv.text(bias[0] - D_R - 22, bias[1] + 22, "Bias", 62, DARK, anchor="end")
    cv.node(*out, D_R, out_label)
    return out
