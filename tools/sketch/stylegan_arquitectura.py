"""Redibujo vectorial del diagrama de arquitectura de StyleGAN del slide 41 (AIG4B Clase 8).

Mapping Network f (Normalise + 8 FC) -> w en W -> bloques A (estilo) que entran a cada Ada IN de la
Synthesis Network g; Noise entra por los bloques B; la salida 1024 X 1024 y las imágenes reales
(Downscaling) van al ProGan Discriminator, cuya Loss vuelve como Training.
Coordenadas tomadas del original; paleta del deck en lugar del verde original.
Salida: talks/redes-generativas-antagonicas/images/stylegan-arquitectura.svg
"""
from pathlib import Path

OUT = Path(__file__).resolve().parents[2] / "talks/redes-generativas-antagonicas/images/stylegan-arquitectura.svg"
INK, DARK, RED, CARD, RULE = "#3B3535", "#1F1E1E", "#DA1B2E", "#F2EEEE", "#D8D2CE"
SERIF = "'Times New Roman', Times, serif"


def box(x, y, w, h, fill=CARD, stroke=RULE, rx=4):
    s = f' stroke="{stroke}" stroke-width="1.5"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{s}/>'


def label(x, y, t, size=21, bold=True, fill=DARK, anchor="middle", rot=None):
    fw = ' font-weight="bold"' if bold else ""
    tr = f' transform="rotate({rot} {x} {y})"' if rot is not None else ""
    return f'<text x="{x}" y="{y}" font-size="{size}"{fw} text-anchor="{anchor}" fill="{fill}"{tr}>{t}</text>'


def bar(x, y, w, h, t, size=21):
    return box(x, y, w, h, fill=INK, stroke=None, rx=2) + label(x + w / 2, y + h / 2 + size * 0.36, t, size, fill="#ffffff")


def plus(cx, cy, r=9):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#ffffff" stroke="{DARK}" stroke-width="1.6"/>'
            f'<path d="M{cx - r + 3},{cy} H{cx + r - 3} M{cx},{cy - r + 3} V{cy + r - 3}" stroke="{DARK}" stroke-width="1.6"/>')


def arrow(d, dashed=False, mid="ah"):
    da = ' stroke-dasharray="7 6"' if dashed else ""
    return f'<path d="{d}" stroke="{DARK}" stroke-width="1.8" fill="none"{da} marker-end="url(#{mid})"/>'


def main():
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -8 1238 634" font-family="Helvetica, Arial, sans-serif" fill="#1F1E1E">',
         '<title>Arquitectura de StyleGAN</title>',
         '<desc>Redibujo del slide 41: el vector latente pasa por la Mapping Network (Normalise y 8 capas FC) y da w en W; '
         'cada bloque A lleva ese estilo a una capa Ada IN de la Synthesis Network g, que parte de una constante 4X4X512, '
         'suma ruido por los bloques B y sube de resolución hasta 1024 X 1024. El ProGan Discriminator compara esa salida '
         'con imágenes reales reducidas (Downscaling); la Loss vuelve como Training.</desc>',
         '<defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="10" viewBox="0 0 11 10" refX="11" refY="5" orient="auto">'
         f'<path d="M0,0 L11,5 L0,10 z" fill="{DARK}"/></marker></defs>',
         '<rect x="-4" y="-8" width="1238" height="634" fill="#ffffff"/>']

    # marco del generador y rótulo lateral
    o.append(f'<rect x="44" y="62" width="784" height="548" fill="none" stroke="{INK}" stroke-width="1.6"/>')
    o.append(label(30, 540, "Generator", 24, rot=-90))

    # vector latente -> Normalise
    o.append(box(42, 8, 644, 42))
    o.append(label(364, 38, "Random Vector (Latent Code) (512 X 1)", 24))
    o.append(f'<path d="M168,50 V72" stroke="{DARK}" stroke-width="1.8"/>')
    o.append(box(95, 72, 150, 38))
    o.append(label(170, 99, "Normalise", 23))

    # Mapping Network f
    for i, t in enumerate(["Mapping", "Network", "f"]):
        o.append(label(52, 138 + 26 * i, t, 22, bold=False, anchor="start", fill=INK))
    o.append(arrow("M170,110 V184"))
    o.append(box(100, 186, 148, 296))
    for i in range(8):
        o.append(bar(108, 194 + 36 * i, 132, 28, "FC"))
    o.append(arrow("M174,482 V530"))

    # w en W (foco)
    o.append(box(100, 532, 148, 48, fill=RED, stroke=None, rx=6))
    o.append(f'<text x="138" y="565" font-family="{SERIF}" font-style="italic" font-weight="bold" font-size="28" fill="#ffffff">w</text>')
    # símbolo "pertenece a" dibujado como trazo (el glifo no está en todas las fuentes)
    o.append('<path d="M181,546 H173 A8,9 0 0 0 173,564 H181 M165,555 H180" stroke="#ffffff" stroke-width="2.6" fill="none" stroke-linecap="round"/>')
    o.append(f'<text x="188" y="565" font-family="{SERIF}" font-style="italic" font-weight="bold" font-size="28" fill="#ffffff">W</text>')

    # Synthesis Network g
    o.append(label(466, 84, "Synthesis Network 'g'", 23))
    o.append(box(350, 92, 236, 192))
    o.append(box(350, 288, 236, 222))
    # columna vertebral de cada bloque
    o.append(f'<path d="M466,128 V250 M466,320 V476" stroke="{DARK}" stroke-width="1.6"/>')
    rows1 = [(100, "Const (4X4X512)"), (154, "Ada IN"), (196, "Conv 3X3"), (250, "Ada IN")]
    rows2 = [(292, "Upsample"), (330, "Const (4X4X512)"), (384, "Ada IN"), (422, "Conv 3X3"), (476, "Ada IN")]
    for y, t in rows1 + rows2:
        o.append(bar(358, y, 216, 28, t))
    plus_y = [141, 237, 371, 463]
    for y in plus_y:
        o.append(plus(466, y))

    # estilos A
    ada_y = [168, 264, 398, 490]
    for y in ada_y:
        o.append(f'<path d="M248,556 L284,{y} H292" stroke="{DARK}" stroke-width="1.6" fill="none"/>')
        o.append(box(291, y - 16, 36, 32))
        o.append(label(309, y + 8, "A", 23))
        o.append(arrow(f"M326,{y} H357"))

    # ruido B
    o.append(label(778, 110, "Noise", 23))
    xs = [800, 792, 784, 776]
    for x, y in zip(xs, plus_y):
        o.append(f'<path d="M{x},120 V{y} H{x - 1}" stroke="{DARK}" stroke-width="1.6" fill="none"/>')
        o.append(arrow(f"M{x},{y} H668"))
        o.append(box(628, y - 16, 40, 32))
        o.append(label(648, y + 8, "B", 23))
        o.append(arrow(f"M628,{y} H476"))

    # salida
    o.append(arrow("M466,510 V522"))
    o.append(box(352, 524, 232, 26))
    o.append(label(468, 543, "....", 23))
    o.append(arrow("M466,550 V566"))
    o.append(box(352, 568, 232, 38))
    o.append(label(468, 595, "1024 X 1024", 23))

    # ProGan Discriminator
    o.append(label(1020, 176, "ProGan Discriminator", 23))
    o.append(box(933, 188, 146, 216))
    o.append(box(940, 195, 30, 200, fill=INK, stroke=None, rx=2))
    o.append(label(962, 295, "(1024 X 1024)", 19, fill="#ffffff", rot=-90))
    for x, w in [(977, 18), (1001, 16), (1022, 11), (1060, 11)]:
        o.append(box(x, 195, w, 200, fill=INK, stroke=None, rx=2))
    o.append(label(1041, 290, "...", 23))
    o.append(arrow("M828,297 H931"))

    # imágenes reales -> Downscaling
    o.append(box(848, 482, 108, 94))
    for dx, dy in [(10, -8), (0, 0)]:
        o.append(f'<rect x="{872 + dx}" y="{512 + dy}" width="62" height="44" fill="#ffffff" stroke="{INK}" stroke-width="1.6"/>')
    o.append(f'<path d="M876,550 L892,532 L904,544 L914,536 L930,550 z" fill="{INK}"/><circle cx="917" cy="522" r="5" fill="{INK}"/>')
    o.append(f'<path d="M890,482 V320 H931" stroke="{DARK}" stroke-width="1.8" fill="none" marker-end="url(#ah)"/>')
    o.append(label(877, 400, "Downscaling", 22, rot=-90))

    # Loss y entrenamiento
    o.append(box(1124, 266, 94, 56))
    o.append(label(1171, 303, "Loss", 24))
    o.append(arrow("M1196,266 V132 H831", dashed=True))
    o.append(arrow("M1171,322 V516 H1006 V407", dashed=True))
    o.append(label(1092, 503, "Training", 23))

    o.append('</svg>')
    OUT.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
