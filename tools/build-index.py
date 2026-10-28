#!/usr/bin/env python3
"""Genera index.html (la portada de GitHub Pages) desde las tablas del README.

Lista las clases en orden de dictado —número, fecha, tema y presentaciones— y los
trabajos prácticos. La fuente de verdad es el README: para cambiar el índice, se
edita la tabla de "## Clases" (o la de entregas) y se vuelve a correr:

    python3 tools/build-index.py

El archivo generado no lleva la marca de Talksmith, así que el render de
md-to-deck lo respeta y escribe su propio listado en talksmith-index.html.
"""

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://austral-ing-ai.github.io/talksmith-ing/"
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def tabla(readme: str, titulo: str) -> list[list[str]]:
    """Filas de la primera tabla Markdown que sigue al encabezado `titulo`."""
    seccion = readme.split(titulo, 1)[1]
    filas = []
    for linea in seccion.splitlines():
        if linea.startswith("|"):
            celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
            if not set("".join(celdas)) <= set("-: "):
                filas.append(celdas)
        elif filas:
            break
    return filas[1:]  # sin el encabezado


def relativo(url: str) -> str:
    """Los links del README apuntan al sitio publicado; en la página van relativos."""
    url = url.removeprefix(SITE)
    if url.startswith("talks/") and url.endswith("/output/html/"):
        url += "index.html"
    return url


def links(celda: str) -> str:
    encontrados = LINK.findall(celda)
    if not encontrados:
        return '<span class="pend">Próximamente</span>'
    return "".join(
        f'<a class="deck" href="{html.escape(relativo(u))}">{html.escape(t)}</a>'
        for t, u in encontrados
    )


def en_linea(texto: str) -> str:
    """Negritas y links de una línea del README, en HTML."""
    out, pos = [], 0
    for m in re.finditer(r"\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)]+)\)", texto):
        out.append(html.escape(texto[pos:m.start()]))
        if m.group(1) is not None:
            out.append(f"<strong>{en_linea(m.group(1))}</strong>")
        else:
            out.append(f'<a href="{html.escape(relativo(m.group(3)))}">{html.escape(m.group(2))}</a>')
        pos = m.end()
    out.append(html.escape(texto[pos:]))
    return "".join(out)


def calendario(readme: str) -> str:
    """La lista de "## Calendario académico" del README, con sus sub-ítems."""
    seccion = readme.split("## Calendario académico", 1)[1].split("\n## ", 1)[0]
    items: list[tuple[str, list[str]]] = []
    for linea in seccion.splitlines():
        if linea.startswith("- "):
            items.append((linea[2:].strip(), []))
        elif linea.lstrip().startswith("- ") and items:
            items[-1][1].append(linea.strip()[2:].strip())
    filas = []
    for texto, subs in items:
        sub = "".join(f"<li>{en_linea(t)}</li>" for t in subs)
        filas.append(f"      <li>{en_linea(texto)}{'<ul>' + sub + '</ul>' if sub else ''}</li>")
    return "\n".join(filas)


def main() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    perfil = (ROOT / "config" / "profile.md").read_text(encoding="utf-8")
    materia = perfil.split("## Subject", 1)[1].strip().splitlines()[0]
    titulo = re.sub(r"\s+", " ", re.split(r"\s*—", materia)[0]).strip()  # "Inteligencia Artificial Generativa (AI Gen)"

    clases = []
    for numero, fecha, tema, presentacion in tabla(readme, "## Clases"):
        if tema.lower().startswith("sin clase"):
            clases.append(f"""      <li class="clase libre">
        <div class="num">—</div>
        <div class="info">
          <p class="fecha">{html.escape(fecha)}</p>
          <p class="tema">{html.escape(tema)}</p>
        </div>
      </li>""")
            continue
        clases.append(f"""      <li class="clase">
        <div class="num">{html.escape(numero)}</div>
        <div class="info">
          <p class="fecha">{html.escape(fecha)}</p>
          <p class="tema">{html.escape(tema)}</p>
          <div class="decks">{links(presentacion)}</div>
        </div>
      </li>""")

    tps = []
    for numero, clase, fecha, consigna in tabla(readme, "## Calendario de entregas"):
        tps.append(f"""      <li class="tp">
        <span class="tpnum">TP {html.escape(numero)}</span>
        <span class="tpfecha">Clase {html.escape(clase)} · {html.escape(fecha)}</span>
        <span class="tpdeck">{links(consigna)}</span>
      </li>""")

    pagina = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Clases · {html.escape(titulo)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600&display=swap" rel="stylesheet">
<style>
:root {{
  --bg: #faf9f7; --fg: #1f1e1e; --muted: #6b6560; --line: #e4dfda;
  --card: #ffffff; --accent: #da1b2e; --pend: #a39d97;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --bg: #161515; --fg: #f0eeec; --muted: #a39d97; --line: #2e2b29;
    --card: #1f1d1c; --accent: #ff4d5e; --pend: #6b6560;
  }}
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0; background: var(--bg); color: var(--fg);
  font: 16px/1.5 'IBM Plex Sans', system-ui, sans-serif;
}}
main {{ max-width: 860px; margin: 0 auto; padding: 48px 16px 64px; }}
header {{ display: flex; align-items: center; gap: 16px; margin-bottom: 8px; }}
header img {{ height: 48px; width: auto; }}
h1 {{ font-size: 1.75rem; line-height: 1.2; margin: 0; }}
.sub {{ color: var(--muted); margin: 0 0 32px; }}
h2 {{ font-size: 1.1rem; margin: 40px 0 12px; color: var(--muted); font-weight: 600;
     text-transform: uppercase; letter-spacing: .06em; }}
ol {{ list-style: none; margin: 0; padding: 0; }}
.clase {{
  display: grid; grid-template-columns: 56px 1fr; gap: 16px;
  padding: 16px; margin-bottom: 8px; background: var(--card);
  border: 1px solid var(--line); border-radius: 10px;
}}
.clase.libre {{ background: transparent; border-style: dashed; padding: 10px 16px; }}
.clase.libre .tema {{ color: var(--muted); font-weight: 400; margin: 0; }}
.clase.libre .num {{ color: var(--pend); }}
.num {{ font-size: 1.6rem; font-weight: 600; color: var(--accent); text-align: center; line-height: 1.2; }}
.fecha {{ margin: 0; color: var(--muted); font-size: .9rem; }}
.tema {{ margin: 2px 0 8px; font-weight: 600; }}
.decks {{ display: flex; flex-wrap: wrap; gap: 8px; }}
a.deck {{
  display: inline-block; padding: 4px 12px; border-radius: 999px;
  border: 1px solid var(--accent); color: var(--accent); text-decoration: none; font-size: .92rem;
}}
a.deck:hover {{ background: var(--accent); color: var(--card); }}
.pend {{ color: var(--pend); font-size: .92rem; }}
.tp {{
  display: grid; grid-template-columns: 64px 1fr; gap: 4px 16px; align-items: center;
  padding: 12px 16px; border-bottom: 1px solid var(--line);
}}
.tpnum {{ font-weight: 600; color: var(--accent); grid-row: span 2; }}
.tpfecha {{ color: var(--muted); font-size: .9rem; }}
.tpdeck {{ display: flex; flex-wrap: wrap; gap: 4px 16px; }}
.tp a.deck {{ border: 0; padding: 0; }}
.tp a.deck:hover {{ background: none; text-decoration: underline; color: var(--accent); }}
.cal {{ list-style: none; margin: 0; padding: 0; }}
.cal > li {{ padding: 10px 16px; border-bottom: 1px solid var(--line); }}
.cal strong {{ font-weight: 600; }}
.cal ul {{ margin: 6px 0 0; padding-left: 20px; color: var(--muted); }}
.cal a {{ color: var(--accent); }}
.ayuda {{ color: var(--muted); font-size: .9rem; margin-top: 40px; }}
kbd {{ border: 1px solid var(--line); border-radius: 4px; padding: 0 5px; font-size: .85rem; }}
</style>
</head>
<body>
<main>
  <header>
    <img src="config/logo.png" alt="Universidad Austral">
    <h1>{html.escape(titulo)}</h1>
  </header>
  <p class="sub">Universidad Austral · Ingeniería de Software · clases en orden de dictado, los miércoles.</p>

  <h2>Clases</h2>
  <ol>
{chr(10).join(clases)}
  </ol>

  <h2>Trabajos prácticos</h2>
  <ol>
{chr(10).join(tps)}
  </ol>

  <h2>Calendario</h2>
  <ul class="cal">
{calendario(readme)}
  </ul>

  <p class="ayuda">En cada presentación: <kbd>→</kbd> <kbd>←</kbd> para avanzar, <kbd>Esc</kbd> para ver todas las diapositivas, <kbd>F</kbd> pantalla completa y <kbd>S</kbd> notas del orador.</p>
</main>
</body>
</html>
"""
    (ROOT / "index.html").write_text(pagina, encoding="utf-8")
    print(f"index.html: {len(clases)} clases, {len(tps)} trabajos prácticos")


if __name__ == "__main__":
    main()
