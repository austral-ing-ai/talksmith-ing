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
  where: ~/.claude/plugins/ — no existe config.json; `${CLAUDE_PLUGIN_ROOT}` sin definir
  what: el marketplace está clonado y registrado, pero el plugin no está habilitado, así que
    el @-import del CLAUDE.md no carga la spec y no hay skills talksmith:* ni slash commands
  context: sesión de Claude Code sobre este repo, cualquier paso. known_marketplaces.json
    registra talksmith con installLocation e autoUpdate true; el clon está sano y al día
  expected: CLAUDE.md paso 1 dice que el @-import deja `orchestrator.md` en contexto, y la
    spec ofrece `/talksmith:ingest` y el resto de los skills como parte del flujo
  actual: `echo ${CLAUDE_PLUGIN_ROOT}` devuelve vacío; `ls ~/.claude/plugins/config.json`
    no existe; `/plugin`, `/plugin update` y `/reload-plugins` responden
    "isn't available in this environment"
  repro: abrir una sesión en este working directory y correr `echo ${CLAUDE_PLUGIN_ROOT}`
  impact: degraded — el flujo corre por el fallback de rutas absolutas, pero ningún skill
    ni slash command está disponible
  workaround: leer `orchestrator.md` por ruta absoluta desde marketplaces/talksmith/, e
    invocar build_html.py / model_freshness.py / audits/*.py por ruta absoluta
  suggested_fix: SUGGESTION, unverified — el CLAUDE.md documenta el fallback de lectura de la
    spec, pero no advierte que los skills quedan inaccesibles aunque la spec cargue bien.
    Una línea ahí ahorraría el diagnóstico. Del lado del usuario, `/plugin install talksmith@talksmith`
    en un entorno donde el comando exista
  seen: 4
  status: open
  plugin_version: 0.87.0

- id: BUG-20260826-02
  date: 2026-08-26
  talk: modelado-redes-neuronales
  step: 6 (Polish) — auditorías de cobertura
  where: skills/md-to-deck/audits/{block_coverage,notes_coverage,text_coverage}.py — emparejado por título
  what: ninguna diapositiva de plantilla `quote` puede emparejar nunca, porque el esquema no
    le da campo `title` a `quote`, y las tres auditorías emparejan por título
  context: mazo de 62 diapositivas con dos slides `quote` — "Qué es un MLP" (final.md:130) y
    "Qué es, en el fondo, la IA" (final.md:794). Las dos están correctamente en el modelo y
    se renderizan bien; el audit igual las reporta como ausentes
  expected: schemas/slide-model.md lista `quote` con campos requeridos `quote` y opcionales
    `attribution` / `section` — sin `title`. Una auditoría de cobertura no debería marcar
    como faltante una diapositiva que sí está en el modelo
  actual: `audit_notes_coverage: 0 notes-drop(s), 2 unmatched slide(s) [source(final.md)]`
    `  [unmatched] line 130 "Qué es un MLP" — no rendered slide with matching title`
    `  [unmatched] line 794 "Qué es, en el fondo, la IA" — no rendered slide with matching title`
  repro: python3 audits/notes_coverage.py output/slide-model.json --source final.md
    sobre cualquier mazo que tenga una diapositiva de plantilla quote
  impact: cosmetic — no afecta el deliverable, pero mete ruido permanente en la salida del
    audit y entrena a ignorar los "unmatched", que es donde aparecería un faltante real
  workaround: verificar a mano que las dos son `quote` y descartar el reporte
  suggested_fix: SUGGESTION, unverified — emparejar las `quote` por su texto (el campo
    `quote`, que en final.md es el blockquote) o por posición dentro de la sección, en vez
    de por título. Alternativamente, excluir del universo auditado las plantillas que el
    esquema define sin `title`
  seen: 1
  status: open
  plugin_version: 0.87.0

- id: BUG-20260826-03
  date: 2026-08-26
  talk: modelado-redes-neuronales
  step: 6 (Polish) — paso FILL
  where: paso FILL de md-to-deck — campo `notes` del modelo
  what: el FILL resume las notas del orador en vez de copiarlas, y en el resumen se pierden
    frases que contestan preguntas que las propias notas plantean
  context: 42 líneas de notas ausentes en 27 diapositivas de un mazo de 62. Caso testigo,
    "Precision, recall y F1": la nota de final.md plantea "si preguntan por qué media armónica
    y no promedio" y la contesta; el modelo conservaba la pregunta y no la respuesta
  expected: la spec del contrato de dos archivos prohíbe la pérdida de contenido, y las notas
    no compiten por espacio en pantalla, así que no hay motivo para comprimirlas
  actual: final.md — "La armónica no lo permite, porque tiende al más chico de los dos."
    modelo — la oración no aparece; tampoco el truco mnemotécnico de columna contra fila,
    ni la advertencia de no reportar F1 solo
  repro: python3 audits/text_coverage.py final.md output/slide-model.json
    y filtrar las filas con where == "notes"
  impact: degraded — el presentador da la clase leyendo estas notas; una nota amputada le
    saca la respuesta de la mano justo cuando un alumno pregunta
  workaround: fusión manual final.md -> modelo en las 27 diapositivas, conservando además los
    6 párrafos que solo existían en el modelo y devolviéndolos a final.md. notes-drops: 42 -> 0
  suggested_fix: SUGGESTION, unverified — que el FILL copie `notes` verbatim desde final.md
    en vez de reescribirlas. Y que text_coverage corra con --strict sobre where == "notes",
    donde el heurístico de ventana literal casi no da falsos positivos, a diferencia del
    cuerpo, donde el FILL sí reestructura con legitimidad
  seen: 1
  status: open
  plugin_version: 0.87.0
