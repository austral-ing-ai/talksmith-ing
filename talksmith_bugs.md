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
  status: ABIERTO (verificado 2026-09-01, plugin 0.97.0) — `${CLAUDE_PLUGIN_ROOT}` sigue vacio en
    este runtime y los comandos /plugin siguen sin existir. Es del entorno, no de una version del plugin.
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

- id: BUG-20260828-06
  status: PARCIAL — cerrada la mitad que importaba, en 0.98.0. `scan` ahora devuelve una lista
    `rendered` con los bloques que una pasada anterior ya renderizo (el eco `<!-- ascii-source: -->`),
    con `image_ref`, `svg_present`, `stamped` y el payload recuperado, y los reporta en la salida
    humana. Corrido sobre este mismo Talk enumera los 12 y marca justo el que motivo esta entrada:
    `s4-1-1-tres-niveles-razonamiento` — importado con su PNG y sin SVG en images/.
    Sigue ABIERTO el resto del "expected": no decide por sello si corresponde re-renderizar, y a
    proposito. El rewrite borra el `ascii-note` de final.md y el sello se tomo sobre payload + nota,
    asi que un digest recalculado marcaria como cambiado todo diagrama que alguna vez tuvo nota.
    Presencia y sellado es lo que el archivo puede afirmar; re-renderizar es decision del rol.
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

- id: BUG-20260901-12
  date: 2026-09-01
  talk: talks/prompting
  step: 6 (Polish) — paso 1, cierre
  where: skills/polish-ascii/polish_ascii.py — subcomando `cleanup`
  what: dos problemas en el mismo subcomando.
    (a) **Descarta el `alt` del plan anotado.** El plan lleva el texto de accesibilidad que el rol
    autorizo —"Mapa de desambiguacion: las cuatro cosas distintas que se llaman thinking y donde
    vive cada una"— y `cleanup` lo ignora, generando el alt desde el slug del archivo
    ("Mapa desambiguacion thinking"): sin acentos, sin contenido, inutil para un lector de pantalla.
    Es una perdida de accesibilidad silenciosa.
    (b) **Sale con codigo 3 y un error falso.** Reporto
    `error: stale plan — s8-1-1 line 2328 no longer opens an ASCII fence` habiendo reescrito
    correctamente los 15 bloques, s8-1-1 incluido. Un exit no-cero sobre una operacion que si
    funciono es peligroso en un pipeline que encadena pasos
  context: re-corrida de Polish sobre un deck de 67 laminas con 15 diagramas, despues de rehacer
    una seccion entera. Verificado a mano: los 15 fences quedaron reescritos y todas las refs resuelven
  expected: que el alt del plan se respete, y que el exit code refleje el resultado real
  suggested-fix (hipotesis, no verificada): (a) usar `alt` del plan cuando esta presente y caer al
    slug solo si falta; (b) revisar la deteccion de "stale": parece comparar contra numeros de linea
    calculados antes de la reescritura de los bloques anteriores, que ya corrieron las lineas

- id: BUG-20260901-13
  date: 2026-09-01
  talk: talks/prompting
  step: 6 (Polish) — paso 1
  where: agents/diagram-illustrator.md — coordinacion del rol
  what: el rol cierra su turno antes de terminar, de forma reproducible. Ocurrio **dos veces en la
    misma Talk**, en el mismo punto: extrae los sidecars, prepara los argumentos, anuncia que los
    renders "estan corriendo en paralelo" y termina el turno. En la primera pasada quedaron 12
    sidecars y 0 SVG; en la segunda, 4 SVG dibujados pero sin sellar ni referenciar.
    Al reintentar, ademas, su reescritura piso el trabajo de un agente de render que ya habia
    terminado y validado el mismo archivo: el patron "dispatch en background + reintento" no tiene
    proteccion contra doble escritura del mismo destino
  context: los renders tardan entre 6 y 8 minutos cada uno; el rol cierra antes de que reporten
  expected: que el rol espere a sus renders y complete sellado, inyeccion de refs y reporte
  actual: hay que retomarlo por mensaje una o dos veces; los pasos deterministas (annotate, stamp,
    cleanup) terminan corriendose desde el orquestador
  suggested-fix (hipotesis, no verificada): que el rol escriba a disco por item apenas cada render
    vuelve, en vez de acumular y reportar al final; y que antes de escribir un destino verifique si
    ya existe con sello valido, para no pisar el trabajo de un dispatch previo
