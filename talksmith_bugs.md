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
  seen: 10
  plugin_version: visto en 0.87.0; reverificado en 0.88.0 → 0.89.2 y en 0.97.0 — persiste
    (el status vive una sola vez, en el encabezado de la entrada)

- id: BUG-20261004-11
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

- id: BUG-20261004-12
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

- id: BUG-20261004-13
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

- id: BUG-20261004-14
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
- id: BUG-20261004-01
  status: ABIERTO
  date: 2026-10-04
  talk: agentes-y-multiagentes
  step: 2 (Collect)
  where: skills/ingest/fetch.py vs skills/ingest/SKILL.md → *Boundaries* ("No paywall bypass")
  what: SKILL.md dice que ante un 403 / 401 / HTML de paywall "that's what gets saved", pero
    fetch.py aborta ante cualquier HTTP error y no guarda nada. Spec y script se contradicen
  context: plugin 1.0.3, VSCode. Captura de un artículo de Medium entregado por el presentador
    en el briefing del Step 1
  expected: carpeta research/web/<folder>/ con original.html + metadata.yaml (http_status: 403),
    según SKILL.md
  actual: "error: fetch failed: HTTP Error 403: Forbidden" — exit 1, sin carpeta
  repro: python3 skills/ingest/fetch.py "https://medium.com/@datadivaai/building-a-react-langgraph-agent-the-future-of-reasoning-centric-ai-workflows-bf270cc756fa" --talk-path talks/<Talk>/ --folder-name test
  impact: minor — la fuente se pudo capturar por un espejo (freedium-mirror.cfd); se agregó
    canonical_url a metadata.yaml a mano para conservar la URL original
  workaround: re-capturar vía un lector espejo y anotar la URL canónica en metadata.yaml
  suggested_fix: SUGGESTION, unverified — o bien alinear SKILL.md con el comportamiento real
    ("un HTTP error aborta sin guardar"), o bien que fetch.py guarde el cuerpo del error con su
    http_status. Podría valer además un flag --canonical-url para capturas vía espejo, así
    metadata.yaml no hay que editarlo a mano
  seen: 1
  plugin_version: 1.0.3

- id: BUG-20261004-02
  status: ABIERTO
  date: 2026-10-04
  talk: agentes-y-multiagentes
  step: 5.5 (live HTML view)
  where: orchestrator.md → Step 5.5 ítem 2 vs skills/md-to-deck/SKILL.md → Step 1.6
  what: las dos specs se contradicen sobre si el FILL de la vista `--draft` corre un
    slide-classifier-critic por slide. El orquestador dice que sí ("one classifier-critic per
    slide"); SKILL.md Step 1.6 dice "Skip this step for the `--draft` live view"
  context: plugin 1.0.3, VSCode. Primer live view del Talk, 52 slides de draft.md
  expected: una sola regla para la vista --draft
  actual: se siguió al orquestador → 51 critics despachados (≈10 min) para una vista que
    SKILL.md declara sin critique
  repro: leer las dos secciones citadas
  impact: minor — costo/tiempo; el render salió bien
  workaround: seguir al orquestador
  suggested_fix: SUGGESTION, unverified — decidir una de las dos y alinear la otra. Si la
    vista draft es "rough", probablemente lo coherente sea saltear critics y bajar la frase del
    orquestador a "una pasada FILL completa"
  seen: 1
  plugin_version: 1.0.3

- id: BUG-20261004-03
  status: ABIERTO
  date: 2026-10-04
  talk: agentes-y-multiagentes
  step: 5.5 (live HTML view)
  where: skills/md-to-deck (catálogo de templates + templates/html/image-full.j2 + content-image.j2 + audits/field_coverage.py)
  what: no hay convención para un slide cuya cara es solo un fence ```ascii (diagrama
    pendiente de Polish) en un FILL --draft. La regla has_code → code-example lo volvería
    slide de código; image-full solo acepta image:{src} porque image-full.j2 llama
    embed_img(s.image) y no el macro smedia, así que no puede dibujar un panel {code}.
    Además content-image.j2 dice en su comentario que un slide solo-imagen "is a legitimate
    content-image", mientras schema, catálogo y field_coverage.py exigen lead o facts y
    dicen que esa forma es image-full
  context: 4 critics (slides 3.2, 6.1, 6.6, C.2) pidieron reclasificar a image-full; no se
    pudo aplicar en --draft
  expected: algún template catálogo-correcto que renderice un diagrama ASCII solo en --draft
  actual: se dejaron como content-image sin columna de texto (stand_in_for: image-full);
    field_coverage reporta advisories en 1.2, 6.1, C.2
  repro: FILL de draft.md slide 6.1 (un fence ascii + una línea de fuentes) — ningún
    template es a la vez correcto según el catálogo y renderizable
  impact: minor — la vista draft se ve bien; el FILL final (con SVGs) debería clasificar
    image-full
  workaround: content-image como stand-in, con traza que nombra image-full
  suggested_fix: SUGGESTION, unverified — que image-full.j2 renderice vía smedia, o
    documentar la convención draft en SKILL.md; y alinear el comentario de content-image.j2
    con el contrato de campos
  seen: 1
  plugin_version: 1.0.3

- id: BUG-20261004-04
  status: ABIERTO
  date: 2026-10-04
  talk: agentes-y-multiagentes
  step: 5.5 (live HTML view)
  where: skills/md-to-deck/audits/field_coverage.py vs audits/_model.py
  what: _model.py documenta que las claves con prefijo `_` son metadata a excluir, pero
    field_coverage.py solo exime nombres específicos
  context: el FILL usó una clave de trabajo `_key`
  expected: `_key` ignorada por la auditoría
  actual: reportada como "ignored → _key"
  repro: agregar "_key": "1.1" a cualquier slide de slide-model.draft.json y correr field_coverage
  impact: cosmetic
  workaround: quitar la clave antes de auditar
  suggested_fix: SUGGESTION, unverified — que field_coverage filtre k.startswith("_")
  seen: 1
  plugin_version: 1.0.3

- id: BUG-20261004-05
  status: ABIERTO
  date: 2026-10-04
  talk: agentes-y-multiagentes
  step: 6 (Polish)
  where: config/diagram-style.md (lista de glifos que dibujan caja vacía) + skills/ascii-to-svg/rasterize.py
  what: "∈" (U+2208) se rasteriza como caja vacía con las fuentes que dicta diagram-style.md, y
    la guía no lo advierte
  context: diagramas s1-6-1 y s1-7-1 (notación formal de agente: a_t ∈ A, o_t ∈ O)
  expected: el símbolo visible en el PNG, o una advertencia en diagram-style.md
  actual: caja vacía. Workarounds del illustrator: tspan con 'Arial Unicode MS' (s1-6-1);
    Menlo primero en la pila (s1-7-1), lo cual contradice la regla de que Menlo es una trampa
    (guion ancho) — inocuo solo porque esas etiquetas no tienen guiones
  repro: <text font-family="Helvetica, Arial, sans-serif">a ∈ A</text> rasterizado con
    rasterize.py → caja vacía
  impact: minor — resuelto con workaround
  suggested_fix: SUGGESTION, unverified — sumar símbolos matemáticos (∈, ∉, ⊂, …) a la lista
    de glifos problemáticos y nombrar una fuente que los tenga, o indicar dibujarlos como path
  seen: 1
  plugin_version: 1.0.3

- id: BUG-20261004-06
  status: ABIERTO
  date: 2026-10-04
  talk: agentes-y-multiagentes
  step: 6 (Polish)
  where: config/diagram-style.md ("One focal element per diagram, never more") vs agents/editor.md (ascii-note `emphasize:`)
  what: la guía de estilo prohíbe más de un elemento focal, pero el Editor escribe líneas
    `emphasize:` que nombran dos, y el illustrator las obedece
  context: s4-1-1, s4-4-1, s6-1-1 salieron con dos elementos rojos; el critic los aprobó
  expected: una regla única
  actual: las dos specs se contradicen
  repro: ver los ascii-note de esos tres bloques en draft.md
  impact: minor
  suggested_fix: SUGGESTION, unverified — que editor.md limite `emphasize:` a un elemento, o
    que diagram-style.md permita dos con condiciones explícitas
  seen: 1
  plugin_version: 1.0.3

- id: BUG-20261004-07
  status: ABIERTO
  date: 2026-10-04
  talk: agentes-y-multiagentes
  step: 6 (Polish)
  where: agents/diagram-critic.md — chequeo de idioma (#11)
  what: el critic solo recibe ascii_note y slide_title, así que no puede saber que un término en
    inglés es deliberado (términos de arte del deck: "tools", "loop")
  context: s4-1-1 quedó con defecto "no resuelto" por "tools"; s1-6-1 cambió "loop" → "lazo",
    rompiendo la consistencia con la prosa del slide (el orquestador lo revirtió a mano en el SVG)
  expected: el critic respeta los términos de arte del deck
  actual: pide traducirlos; el contrato trata su veredicto como autoritativo
  repro: render de un bloque cuyo texto incluye "tools" en un deck en español
  impact: minor — produce cambios no deseados o defectos falsos
  suggested_fix: SUGGESTION, unverified — pasarle al critic una lista de términos de arte
    (p. ej. derivada del ascii-note o de un campo del frontmatter), o la prosa del slide
  seen: 1
  plugin_version: 1.0.3

- id: BUG-20261004-08
  status: ABIERTO
  date: 2026-10-04
  talk: agentes-y-multiagentes
  step: 7 (Render)
  where: skills/md-to-deck/templates/html/image-full.j2 vs schemas/slide-model.md (`source`) + catálogo ("image_only → image-full")
  what: image-full descarta todos los highlights, incluida la línea de fuente, aunque el schema
    define `source` como chrome del slide fijado al borde inferior. Una imagen + una cita no
    tiene destino sin pérdida
  context: slides 6.1 y 6.6 (diagrama + "Kore.ai, oct-2025 (act. jul-2026)")
  expected: image-full muestra la fuente abajo
  actual: el renderer ignora el highlight y field_coverage lo marca; la cita terminó en la
    línea bajo el título
  repro: FILL de final.md 6.1 como image-full con highlights:[{kind:source,…}]
  impact: minor — la cita queda visible pero fuera de lugar
  suggested_fix: SUGGESTION, unverified — que image-full renderice hl-source al pie y sumar
    `highlights` a sus campos permitidos
  seen: 1
  plugin_version: 1.0.3

- id: BUG-20261004-09
  status: ABIERTO
  date: 2026-10-04
  talk: agentes-y-multiagentes
  step: 7 (Render)
  where: skills/md-to-deck/SKILL.md (referencias, *Failure modes*, Step 1.6 vs "No critique loop") + config/pptx-styles/slide-templates.md
  what: documentación desactualizada / autocontradictoria:
    (a) SKILL.md referencia skills/md-to-deck/pptx-render.md, que no existe en 1.0.3;
    (b) *Failure modes* lista "[pptx 0/8] FAILED: style: invocation parameter missing …; do
        not default" y "value not a directory under config/pptx-styles/", contradiciendo la
        tabla de parámetros (style default = default; estilos en templates/html/styles/*.css),
        y escribe esa ruta relativa a la raíz del plugin cuando es skills/md-to-deck/templates/html/styles/;
    (c) dice "No critique loop … single-pass GENERATE" y a la vez define Step 1.6 (critique por
        slide); el párrafo de diversidad dice "CONTROL is audit-none, FEEDBACK is no-critique";
    (d) el catálogo usa todavía `format: list` (líneas ~224, ~763, ~832–841) aunque el mismo
        archivo dice que `list` está retirado; value-columns menciona `image` + `layout` y el
        schema dice que `layout` ya no se lee;
    (e) docstring de html_style._vector_twin dice que final.md trae refs .svg; Polish escribe .png
        (el renderer igual sube a SVG)
  context: render final del Talk
  expected: docs consistentes con el código
  actual: lo descripto; ningún impacto en el deck
  repro: leer las secciones citadas; ls skills/md-to-deck/pptx-render.md
  impact: cosmetic/doc — confunde a quien ejecuta el skill
  suggested_fix: SUGGESTION, unverified — pasada de limpieza de SKILL.md y del catálogo
  seen: 1
  plugin_version: 1.0.3

- id: BUG-20261004-10
  status: ABIERTO
  date: 2026-10-04
  talk: agentes-y-multiagentes (detectado; las filas son de modelado-redes-neuronales)
  step: 8 (Learnings) — scan del backlog
  where: config/feedback-backlog.md (escrito por skills/feedback-cycle mirror-row) + Step 8 "Move" (editor)
  what: dos problemas de integridad en el backlog:
    (a) en las filas #99–#114 (modelado-redes-neuronales) los `tags:` no corresponden al
        `feedback:` de la misma fila — parecen corridos de lugar (p. ej. "Movelo como una nota
        abajo" con [missing-definition, card-wording]; "Borrar 'El lote…'" con
        [factual-correction, add-source]);
    (b) el Move del Step 8 copió a feedback-processed.md las filas de L8–L10 pero no las sacó
        del backlog; y las filas de evidencia de L1–L7 nunca se movieron
  context: análisis de patrones recurrentes del Step 8; los conteos por tag salen inflados o
    mal asignados
  expected: (a) tags alineados con su fila; (b) filas promovidas fuera del backlog
  actual: lo descripto
  repro: (a) comparar feedback vs tags en esas filas; (b) grep de los textos de
    feedback-processed.md en feedback-backlog.md
  impact: degraded — el scan de recurrencias por tag no es confiable; hubo que agrupar por texto
  suggested_fix: SUGGESTION, unverified — (a) worth checking whether mirror-row toma los tags
    por índice de una lista desfasada cuando se procesan varias filas en una ronda; (b) que el
    Move sea un "move" real (append + delete) vía el helper, con un chequeo de que ninguna fila
    de processed siga en el backlog
  seen: 1
  plugin_version: visto en 1.0.3 (las filas son de rondas anteriores; versión de origen desconocida)
