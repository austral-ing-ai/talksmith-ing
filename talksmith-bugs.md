# Talksmith bugs

> Inconsistencies and malfunctions **Talksmith itself** hit while running this working
> directory's workflow — not feedback about the talk. Written by Talksmith, append-only;
> safe to edit or prune by hand. Every entry carries context, a repro (or an explicit
> "unknown"), and — where offered — a **suggested** fix: a hypothesis from the session,
> never a verified diagnosis. Format: `schemas/talksmith-bugs.md`.
> Worth reporting upstream: https://github.com/veigap/talksmith/issues

## Entries

<!-- Talksmith appends entries below this line, newest at the bottom. -->
- id: BUG-20260826-01
  status: open
  note: reverificado 2026-09-04, plugin 0.100.0 — `${CLAUDE_PLUGIN_ROOT}` sigue vacio en
    este runtime y los comandos /plugin siguen sin existir. Es del entorno, no de una version del
    plugin, y ninguna version puede cerrarlo.
    De las dos mitades del suggested_fix, la (a) ya estaba hecha: el paso 1 del stub tiene una
    comprobacion explicita ("deberias ver el encabezado de la spec; si no, leela ahora"), no una
    nota al pie. La (b) se hizo en 0.100.0: el stub ahora nombra las dos rutas canonicas del
    install en vez de mandar a buscarlas con find, y dice que se anote la raiz una sola vez porque
    todos los scripts que el flujo llama por ruta cuelgan de ella. **Requiere re-correr
    `/talksmith:init`** en cada working directory para que llegue.
    Dato util verificado hoy: el install de esta maquina esta en
    `~/.claude/plugins/marketplaces/talksmith` y es un clon de este mismo repo, sincronizado con
    el arbol de trabajo. O sea que una edicion en el repo llega al runtime sin push y sin
    reinstalar — solo hace falta abrir sesion nueva.
  date: 2026-08-26
  talk: -
  step: 0 (arranque de sesión)
  where: CLAUDE.md línea 13 — @-import `@${CLAUDE_PLUGIN_ROOT}/orchestrator.md` sin expandir
  what: el @-import del CLAUDE.md no expande, así que la spec del orquestador no llega al
    contexto y hay que leerla por ruta absoluta en cada arranque. Los comandos de gestión de
    plugins (/plugin, /plugin update, /reload-plugins) tampoco existen en este runtime.
    Los skills y subagentes talksmith:* SÍ quedan registrados en la sesión — el registro del
    plugin funciona; lo único roto es la expansión del @-import y los comandos /plugin
  context: sesión de Claude Code sobre este working directory, cualquier paso, corriendo en la
    extensión de VSCode. settings.json declara "enabledPlugins": {"talksmith@talksmith": true};
    known_marketplaces.json registra talksmith con installLocation y autoUpdate true; el clon
    está sano, limpio y al día. Nada mal configurado del lado del usuario.
    Reverificado a lo largo de una sesión entera y de cuatro actualizaciones del plugin
    (0.87.0 → 0.88.0 → 0.89.0 → 0.89.1 → 0.89.2): el import no expandió ni una sola vez, y
    ninguna de las actualizaciones lo tocó ni podía tocarlo — no es del plugin
  expected: CLAUDE.md paso 1 dice que el @-import deja orchestrator.md en contexto — el
    encabezado "Talksmith — Presenter Agent (orchestrator spec)" debería verse en el bloque
    claudeMd, sin ninguna lectura adicional
  actual: el bloque claudeMd del contexto muestra el CLAUDE.md tal cual, sin la spec embebida
    echo ${CLAUDE_PLUGIN_ROOT} devuelve vacío en Bash
    ls ~/.claude/plugins/config.json — no existe
    /plugin, /plugin update, /reload-plugins — "isn't available in this environment"
    en cambio, el roster de la sesión SÍ lista los skills talksmith:{init,ingest,ascii-to-svg,
    polish-ascii,polish-images,md-to-deck,feedback-cycle,generate-image,desrobotizar,pptx-*}
    y los subagentes talksmith:{editor,composer,librarian,diagram-illustrator,image-illustrator,
    global-librarian,diagram-critic,slide-classifier-critic}
  repro: abrir una sesión en este working directory y buscar el encabezado de la spec en el
    contexto de CLAUDE.md; correr echo ${CLAUDE_PLUGIN_ROOT}
  impact: degraded — el flujo corre completo, pero cada arranque depende de que el orquestador
    detecte que la spec falta y la lea por ruta absoluta. Si no lo detecta, corre sin spec.
    Los skills se invocan por nombre en vez de por slash command
  workaround: leer orchestrator.md por ruta absoluta —
    ~/.claude/plugins/marketplaces/talksmith/orchestrator.md (o cache/talksmith/talksmith/<versión>/) —
    e invocar los skills por nombre en vez de por slash command. Los scripts que se llaman por
    ruta (build_html.py, model_freshness.py, audits/*.py) cuelgan de esa misma raíz
  suggested_fix: SUGGESTION, unverified — el fallback ya está documentado en el CLAUDE.md y
    funciona; lo que falla es que el agente tiene que acordarse de verificar. Vale la pena
    (a) que la verificación del paso 1 sea una comprobación explícita y no una nota al pie, y
    (b) que el CLAUDE.md nombre la ruta canónica del marketplace, para no tener que buscarla
    con find en cada arranque. Del lado del usuario no hay nada que hacer: abrir el mismo
    directorio en el CLI de Claude Code debería expandir el import solo
  seen: 10
  plugin_version: visto en 0.87.0; reverificado en 0.88.0 → 0.89.2 y en 0.97.0 — persiste
    (el status vive una sola vez, en el encabezado de la entrada)

- id: BUG-20261017-10
  status: open
  date: 2026-10-17
  talk: redes-generativas-antagonicas
  step: 7 (Render)
  where: skills/md-to-deck/templates/html/theme.css (~línea 295, .cards con 3 hijos) vs schemas/slide-model.md y catálogo ("3 → a row")
  what: un set de 3 tarjetas se dibuja 2+1 (la tercera ocupa todo el ancho abajo), contra lo que
    dicen el schema y el catálogo
  repro: deck GANs, slide 5 "¿Por qué importa en ingeniería?" (concept-breakdown con 3 ítems)
  impact: cosmetic
  suggested_fix: SUGGESTION, unverified — `.cards:has(>.ccard:nth-child(3):last-child){grid-template-columns:repeat(3,1fr)}` y quitar el span de la tercera
  seen: 1
  plugin_version: 1.3.1

- id: BUG-20261017-11
  status: open
  date: 2026-10-17
  talk: redes-generativas-antagonicas
  step: 7 (Render)
  where: skills/md-to-deck/templates/html/theme.css (.numrow{grid-template-columns:repeat(3,1fr)}) — template `process`
  what: los pasos numerados usan una grilla fija de 3 columnas: 4 pasos → 3+1 y 5 pasos → 3+2,
    con celdas vacías (misma clase de defecto que `.figs` corregido en 1.3.0)
  repro: deck GANs slide 33 "Backpropagation: el procedimiento paso a paso" (4 pasos); slides 16 y 51 (5 pasos)
  impact: cosmetic
  suggested_fix: SUGGESTION, unverified — columnas por cantidad (4 → 2×2 o 4 en fila, 5 → 5 en fila o 3+2 centrado)
  seen: 1
  plugin_version: 1.3.1

- id: BUG-20261017-12
  status: open
  date: 2026-10-17
  talk: redes-generativas-antagonicas
  step: 7 (Render)
  where: skills/md-to-deck/audits/template_diversity.py (mensaje [format-flat])
  what: el mensaje nombra todavía el formato retirado `list` ("(grid/row/list/editorial)")
  repro: cualquier deck donde todos los concept-breakdown usen grid
  impact: cosmetic (doc)
  suggested_fix: SUGGESTION, unverified — quitar `list` del mensaje
  seen: 1
  plugin_version: 1.3.1

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
