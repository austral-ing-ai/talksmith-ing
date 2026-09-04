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

- id: BUG-20260901-13
  status: RESUELTO en 0.100.0. Confirmado primero lo que reportaste: `agents/diagram-illustrator.md`
    no se habia tocado desde 0.98.1. Ahora el rol lleva un contrato de finalizacion explicito, y las
    dos mitigaciones que mediste quedaron escritas en la spec. (1) No cierra el turno mientras haya
    un dispatch pendiente. (2) Escribe el log de cada bloque apenas ese bloque vuelve, en vez de
    acumular en contexto y escribir al final, asi un turno cortado deja estado parcial coherente en
    disco y no nada. (3) Arma el reporte listando `images/`, no de memoria: un bloque que no esta en
    disco se reporta `failed`, no `rendered` — es el chequeo que convierte un corte silencioso en uno
    visible, y es tu "verifica con ls antes de contestar". (4) No pisa un destino cuyo sello ya
    coincide con su sidecar, que es la proteccion contra doble escritura del reintento. Y tu otra
    mitigacion quedo como regla: si el pase ya fue retomado una vez, la ventana baja a 1 y va bloque
    por bloque. Es el unico lugar donde el 5 fijo cede, y cede por medicion, no por prudencia.
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
