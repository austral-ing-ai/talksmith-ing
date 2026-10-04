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
  status: ABIERTO (reverificado 2026-09-04, plugin 0.100.0) — `${CLAUDE_PLUGIN_ROOT}` sigue vacio en
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
  seen: 8
  plugin_version: visto en 0.87.0; reverificado en 0.88.0 → 0.89.2 y en 0.97.0 — persiste
    (el status vive una sola vez, en el encabezado de la entrada)

- id: BUG-20261004-01
  date: 2026-10-04
  talk: sistemas-multiagente
  step: 2 (talksmith:ingest, fetch.py)
  where: skills/ingest/fetch.py — extracción de imágenes (solo <img src>)
  what: ingest no captura las figuras de papers en HTML de arXiv/ar5iv que vienen como SVG en <object> o fuera de <img>
  context: captura de 9 papers vía ar5iv.labs.arxiv.org/html/<id> y arxiv.org/html/<id> (multiagent-debate-2023, autogen-2023, metagpt-2023, chatdev-2023, mixture-of-agents-2024, agentless-2024, mast-why-mas-fail-2025, magentic-one-2024, openai-five-2019 — a este último le faltan 37 figuras, entre ellas la Fig. 1); el librarian lo detectó en Step 3
  expected: SKILL.md de ingest — "Resolves every <img src> to an absolute URL and downloads it into assets/"; el librarian espera tener en assets/ las figuras del paper
  actual: multiagent-debate-2023 quedó con 1 imagen de 26 figuras; en total el librarian tuvo que bajar a mano 53 figuras desde las URLs de original.html. Agentless, MAST (Fig. 1, 4, 5, 8-11) y Magentic-One (Fig. 3a/b, 4a) quedaron solo con el caption
  repro: python3 skills/ingest/fetch.py https://ar5iv.labs.arxiv.org/html/2305.14325 --talk-path talks/<T>/ --folder-name x ; contar archivos en research/web/x/assets/ contra las figuras del paper
  impact: degraded
  workaround: el librarian descargó las figuras desde las URLs de original.html; las que no tenían URL quedaron solo con caption
  suggested_fix: SUGGESTION, unverified — probablemente alcance con recorrer también <object data>, <embed src>, <source srcset> y <image href> de SVG inline, y resolver srcset tomando la URL de mayor resolución
  seen: 1
  status: open
  plugin_version: 1.0.0

- id: BUG-20261004-02
  date: 2026-10-04
  talk: sistemas-multiagente
  step: 5.5 (md-to-deck RENDER, text-coverage check)
  where: skills/md-to-deck/build_html.py — aviso de cobertura de texto (audits/text_coverage.py)
  what: falso notes-drop cuando un separador de sección y una lámina de contenido comparten título
  context: render --draft; sección 7 "Cómo fallan" y su lámina 7.1 también titulada "Cómo fallan"; la 7.1 sí lleva sus notas en el modelo
  expected: el chequeo empareja cada bloque de notas del draft con su lámina de origen
  actual: "[notes-drop] slide 45 "Cómo fallan" — source has notes, model carries no `notes`" (la 45 es el separador, sin notas por diseño)
  repro: draft con una sección y una lámina del mismo título, notas solo en la lámina; build_html.py --draft
  impact: cosmetic
  workaround: ninguno; aviso ignorado
  suggested_fix: SUGGESTION, unverified — emparejar por posición o por id de lámina en vez de por título
  seen: 2
  status: open
  plugin_version: 1.0.0

- id: BUG-20261004-03
  date: 2026-10-04
  talk: sistemas-multiagente
  step: 5.5 (md-to-deck FILL)
  where: catálogo de templates de md-to-deck — quote/statement fijados por el autor y set de tarjetas con dos imágenes
  what: (a) una lámina con `quote` o `statement` fijado por el autor pierde sus bullets, porque esos templates no renderizan highlights; (b) no hay template para un set de tarjetas con dos imágenes compartidas; (c) el editor escribió `<!-- template: table -->`, que no es un template válido
  context: draft.md 1.1 (quote + 2 bullets → 3 text-drops), 5.7 (statement + 3 bullets, ~24 palabras sobre un tope de ~16), 5.4 (dos diagramas de Cognition, solo entra uno), 3.9 (hint "table")
  expected: el editor solo fija templates que pueden contener el cuerpo de la lámina y que existen en el catálogo
  actual: "[text-drop] draft.md:57 (content) "Agente: percibe y actúa" — "Tampoco software: un termostato o un insecto también entran." [50% of its words are in the model]"
  repro: lámina con `<!-- template: quote -->` y bullets debajo; FILL + build_html.py --draft
  impact: degraded
  workaround: 5.7 bullets plegados en el sub; 3.9 mapeado a value-columns; 5.4 con una sola imagen
  suggested_fix: SUGGESTION, unverified — que el editor valide los hints contra el catálogo al escribirlos y avise cuando el cuerpo excede lo que el template fijado puede mostrar
  seen: 1
  status: open
  plugin_version: 1.0.0

- id: BUG-20261004-04
  date: 2026-10-04
  talk: sistemas-multiagente
  step: 5.5 (md-to-deck RENDER, formateo de texto)
  where: skills/md-to-deck/build_html.py — formateador de texto inline (cursiva con *)
  what: un asterisco escapado (\*) en el texto se interpreta como apertura de cursiva
  context: notas de la lámina 1.2 con "P\* ... P\*" (secuencia de percepciones P*)
  expected: \* se renderiza como un asterisco literal, como en Markdown
  actual: "P\* … P\*" sale como "P\<i>…</i>"
  repro: una lámina con el texto `P\* y P\*` en el cuerpo o las notas; FILL + build_html.py --draft
  impact: cosmetic
  workaround: en el modelo se escribió P* sin barra (un * suelto se renderiza literal)
  suggested_fix: SUGGESTION, unverified — tratar \* como escape antes de aplicar la regla de cursiva
  seen: 1
  status: open
  plugin_version: 1.0.0
