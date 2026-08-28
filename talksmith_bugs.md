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
  seen: 7
  status: open
  plugin_version: visto en 0.87.0; reverificado en 0.88.0, 0.89.0, 0.89.1 y 0.89.2 — persiste

- id: BUG-20260828-01
  date: 2026-08-28
  talk: talks/prompting
  step: 6 (Polish) — preparación
  where: skills/polish-ascii/polish_ascii.py — subcomando `scan`, heurístico legacy de detección
  what: el heurístico marca como diagrama ASCII renderizable cualquier fence que contenga
    `->`, `|` o `+--`. En un deck sobre prompting eso barre los fences de código común:
    prompts de ejemplo, Python, JSON y XML. 14 de 16 bloques detectados eran falsos positivos.
    Sin intervención, Step 6 los habría rasterizado a SVG, destruyendo código legible
  context: draft.md de 74 slides con abundante código de ejemplo. Detectado por el rol editor
    durante la preparación de Polish, antes de correr el paso
  expected: que `scan` distinga un diagrama de caja de un fence de código
  actual: 16 detecciones, 2 legítimas
  workaround: se antepuso `<!-- ascii-render: documentation-only -->` a cada fence sin tag
  suggested-fix (hipótesis, no verificada): tratar un fence sin lenguaje declarado como
    documentation-only por defecto; o exigir al menos dos clases distintas de glifo de caja
    más un ratio alfabético bajo antes de aceptar el bloque como renderizable

- id: BUG-20260828-02
  date: 2026-08-28
  talk: talks/prompting
  step: 3 (Corpus) — consumido en Step 4
  where: research/corpus/AIG4B-Clase-3-Prompting.md.md — sección Inconsistencies, ítem #18
  what: el registro del librarian afirma que "Fable 5 no corresponde a ningún modelo Anthropic
    conocido" y lo lista como dato a corregir. Fable 5 sí existe (claude-fable-5), y la tarifa
    que declaraba el deck era correcta. Un editor que actúe sobre esa nota borra un dato bueno
  context: el librarian catalogó 36 inconsistencias del PPTX original; ésta es falsa
  expected: que una afirmación de "modelo inexistente" se verifique antes de escribirse
  actual: afirmación categórica sin verificar, heredada por el draft
  suggested-fix (hipótesis, no verificada): que el librarian valide nombres de modelo Claude
    contra la skill `claude-api` antes de declararlos desconocidos, o que rebaje el ítem a
    pregunta abierta en vez de aserción

- id: BUG-20260828-03
  date: 2026-08-28
  talk: talks/prompting
  step: 4 (Draft)
  where: research/corpus/AIG4B-Clase-3-Prompting.md.md — sección `Raw / preserved excerpts`,
    ítems [11] y [35]
  what: la sección se rotula como preservación verbatim del original, y el spec del rol editor
    manda reponer desde ahí el texto que el PPTX dejó truncado. Pero [11] y [35] están
    truncados igual que el draft: no hay versión completa que reponer. La promesa del rótulo
    no se cumple, y el editor queda sin salida prescrita
  context: dos slides con frases cortadas a mitad ("...lo cual incre", "...de medium a high,")
  expected: que `Raw / preserved excerpts` contenga el párrafo completo, o declare que no lo hay
  actual: contiene el mismo fragmento truncado, sin marca de que lo está
  suggested-fix (hipótesis, no verificada): rotular esos excerpts como
    "(truncado en el original, sin versión completa disponible)" para que el editor sepa que
    tiene que cerrar la frase con criterio propio en vez de buscar una fuente que no existe

- id: BUG-20260828-04
  date: 2026-08-28
  talk: talks/prompting
  step: 5 (Review) / 8 (Learnings)
  where: skills/feedback-cycle — subcomando `find-closed-unmirrored`
  what: no distingue los bullets de feedback que escribió el presentador de los cierres que
    autoró el editor como registro de sus propios cambios. Reporta los 52 como pendientes de
    espejar al backlog cross-Talk, cuando la mayoría son bitácora interna de la Talk y no
    corresponden al backlog
  context: pase de edición masivo que cerró 52 bullets, casi todos autogenerados
  expected: que solo los bullets de origen presentador cuenten para el mirror
  actual: los cuenta todos
  suggested-fix (hipótesis, no verificada): marcar el autor del bullet al crearlo
    (presentador vs. editor) y filtrar por eso en `find-closed-unmirrored`

- id: BUG-20260828-05
  date: 2026-08-28
  talk: talks/prompting
  step: 6 (Polish) — paso 1, rasterizado
  where: skills/ascii-to-svg — dependencia `cairosvg` no declarada ni verificada
  what: el primer render falló al rasterizar el SVG a PNG porque `cairosvg` no estaba
    instalado en el intérprete activo. Sin PNG entregable no hay build de PPTX, así que el
    paso se corta a mitad y deja SVGs sueltos sin su contraparte
  context: 12 diagramas a renderizar; libcairo de Homebrew ya estaba presente, faltaba solo
    el binding de Python. El intérprete activo resultó ser el venv de missions/clase3
  expected: que la skill verifique sus dependencias antes de empezar, o que declare el
    requisito de forma que el fallo sea legible desde el primer intento
  actual: falla en el momento de rasterizar, después de generar el SVG
  workaround: se instaló cairosvg 2.9.0 en el intérprete activo y se reintentó
  suggested-fix (hipótesis, no verificada): chequeo de dependencias al inicio de la skill,
    con mensaje accionable; o degradar a "SVG sin PNG" avisando en el reporte en vez de cortar

- id: BUG-20260828-06
  date: 2026-08-28
  talk: talks/prompting
  step: 6 (Polish) — paso 1, inventario
  where: skills/polish-ascii/polish_ascii.py — subcomando `scan`
  what: un bloque `ascii-source` preexistente que ya viene en forma renderizada (con su PNG
    hermano pero sin `.svg`) no entra en el inventario del scan. Queda invisible: nunca se
    re-renderiza ni se reporta como pendiente. En esta Talk el bloque de los tres niveles de
    razonamiento, importado de otra Talk, quedó fuera de los 26 bloques enumerados
  context: slide importada de talksmith-mim/talks/hiperparametros-ai, que llegó con su
    ascii-source y su PNG ya generado en la Talk de origen
  expected: que el inventario incluya todo bloque ascii-source, y decida por sello de
    idempotencia si corresponde re-renderizar
  actual: el bloque no aparece en la enumeración; no rompe nada ahora, pero si el ASCII se
    edita el render nunca se actualiza
  suggested-fix (hipótesis, no verificada): que `scan` enumere por presencia de `ascii-source`
    y no por ausencia de render, marcando el estado (renderizado / pendiente / huérfano)
