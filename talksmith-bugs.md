# Talksmith bugs

> Inconsistencies and malfunctions **Talksmith itself** hit while running this working
> directory's workflow — not feedback about the talk. Written by Talksmith, append-only;
> safe to edit or prune by hand. Every entry carries context, a repro (or an explicit
> "unknown"), and — where offered — a **suggested** fix: a hypothesis from the session,
> never a verified diagnosis. Format: `schemas/talksmith-bugs.md`.
> Worth reporting upstream: https://github.com/veigap/talksmith/issues

## Entries

<!-- Talksmith appends entries below this line, newest at the bottom. -->
- id: BUG-20261017-13
  status: open
  date: 2026-10-17
  talk: redes-generativas-antagonicas
  step: 7 (Render)
  where: skills/md-to-deck/build_html.py + html_style.py (marca data-dense / "too small to read")
  what: el aviso de "demasiado chico para leer" no aparece en un render solo-HTML: build_html.py no
    imprime nada y la marca data-dense existe solo en la página viva y en los exports PDF/.pptx.
    Además el porcentaje cambia según cuántos ítems estén revelados (slide 5: 54% sin revelar, 59% con todo)
  repro: render HTML de un deck con slides densos y buscar el aviso en la salida de build_html.py
  impact: degraded — hubo que inspeccionar el DOM slide por slide para encontrar 17 slides afectados
  suggested_fix: SUGGESTION, unverified — medir con todos los fragments visibles y listar los slides en la salida del build
  seen: 1
  plugin_version: 1.3.1

- id: BUG-20261017-14
  status: open
  date: 2026-10-17
  talk: redes-generativas-antagonicas
  step: 7 (Render)
  where: skills/md-to-deck/html_style.py (fit pass: título y lead excluidos del achique)
  what: el encabezado (título + lead) nunca se achica; en diseños de columna angosta un título que
    se parte en dos líneas más un lead largo dejan al cuerpo al 45% de su tamaño
  repro: deck GANs slides 18 y 43
  impact: degraded — son los slides más ilegibles del deck
  suggested_fix: SUGGESTION, unverified — incluir el lead (o un tope de alto del encabezado) en el fit
  seen: 1
  plugin_version: 1.3.1

- id: BUG-20261028-01
  status: open
  date: 2026-10-28
  talk: agentes-y-multiagentes
  step: 6 (Polish) — pasada de diagramas animados
  where: skills/ascii-to-svg (validate_svg / animate_svg / audit_aspect) — ningún chequeo de texto agregado
  what: el SVG de un render incluyó texto que no está ni en el ASCII ni en la nota
  expected: el SVG lleva solo labels del bloque ASCII, de la nota (terms/animation) o del contexto del slide
  actual: el primer render de s6-3-1 (orquestador-workers) agregó "loop propio" en las tres cajas de
    worker. Ningún script lo detectó; lo marcó el crítico ciego, y solo porque la palabra era inglés.
    Se corrigió en la revisión.
  repro: unknown — es un comportamiento no determinista del render; la entrada fue el bloque de la slide 6.3
    con su nota animation: de 2026-10-28
  impact: degraded — un label inventado podría llegar al deck si está en el idioma de la charla
  suggested_fix: SUGGESTION, unverified — un chequeo por script que compare los <text> del SVG con los
    tokens del ASCII + nota + contexto y avise ante palabras nuevas
  seen: 1
  plugin_version: 1.4.0

- id: BUG-20261028-04
  status: open
  note: parcial en 1.6.4 — el brief ya tiene lugar documentado (editor.md: bloque ```ascii de
    documentación bajo la imagen + su ascii-note con intent/animation; image-note no existe). Sigue
    abierto: la pasada de animación del Step 6 solo cubre diagramas renderizados, así que un SVG
    hecho a mano se anima invocando animate-svg a mano y nada lo reaplica si se redibuja.
  date: 2026-10-28
  talk: redes-generativas-antagonicas
  step: fuera de banda (análisis de animación, Talk en Step 7)
  where: agents/editor.md → ASCII diagrams (`animation:`) + skills/ascii-to-svg/animate_svg.py
  what: la animación solo tiene lugar en el pipeline a través de la `ascii-note` de un bloque ```ascii. Un Talk
    con SVGs hechos a mano (importados) no tiene dónde declarar sus beats
  expected: un lugar declarado para los beats de un SVG que no sale de ASCII (p. ej. una nota junto a la imagen)
    que Polish vuelva a aplicar después de un redibujo
  actual: animate_svg.py sí funciona sobre un SVG cualquiera con `<g data-beat="N">` (se probó en una copia de
    ciclo-lote.svg: exit 0, "animation: 6 beats"), y el deck lo reproduce. Pero los beats quedan solo en el SVG,
    y si alguien redibuja el archivo se pierden sin aviso
  repro: en talks/redes-generativas-antagonicas (sin bloques ```ascii), buscar en editor.md o en el SKILL.md de
    ascii-to-svg cómo animar images/ciclo-lote.svg: no hay ruta documentada
  impact: degraded — la animación de figuras hechas a mano se puede hacer, pero ningún paso la registra ni la reaplica
  suggested_fix: SUGGESTION, unverified — aceptar un comentario `<!-- image-note: animation: … -->` después de una
    imagen SVG en draft.md, que el diagram-illustrator le pase a animate_svg.py en Polish
  seen: 1
  plugin_version: 1.4.1

- id: BUG-20261028-07
  status: open
  date: 2026-10-28
  talk: redes-generativas-antagonicas
  step: 6 (Polish) — pasada de animación
  where: plugin instalado (cache 1.4.1) vs checkout del marketplace (más nuevo) → skills/animate-svg/SKILL.md
  what: el CLAUDE.md del repo manda leer el spec desde marketplaces/talksmith, que estaba adelante del plugin
    instalado (1.4.1). Al actualizar a 1.5.1 en medio de la pasada, el contrato de animate-svg cambió (de editar
    `<stem>.svg` en el lugar a escribir `<stem>.anim.svg` y apuntar la slide a `<stem>.anim.png`), y
    `claude plugin marketplace update` re-clonó el directorio con subagentes trabajando sobre él
  expected: que el spec cargado y los scripts sean de la misma versión, o una advertencia cuando difieren
  actual: 3 animaciones se migraron a mano a la nueva estructura; las otras 5 las migraron sus subagentes al releer
    el SKILL. Sin pérdida de trabajo
  repro: comparar `git -C ~/.claude/plugins/marketplaces/talksmith log -1` con la versión en installed_plugins.json
  impact: degraded — dos contratos de archivos en la misma pasada
  suggested_fix: SUGGESTION, unverified — que el stub de CLAUDE.md prefiera `installPath` de installed_plugins.json
    y avise si el marketplace está adelante
  seen: 1
  plugin_version: 1.4.1 → 1.5.1
