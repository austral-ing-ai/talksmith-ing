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
  seen: 11
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

- id: BUG-20261028-02
  status: open
  date: 2026-10-28
  talk: agentes-y-multiagentes
  step: 6 (Polish)
  where: agents/diagram-illustrator.md — despacho de las tandas de render/crítica
  what: la spec pide despachar cada tanda con `run_in_background: false`, parámetro que la herramienta Agent
    de este entorno (extensión de VS Code) no tiene; los subagentes vuelven siempre de forma asíncrona
  expected: un mecanismo de despacho en primer plano que exista en la herramienta
  actual: el ilustrador mandó cada tanda en un mensaje y esperó todos los resultados antes de seguir; funcionó,
    pero no como lo describe la spec
  repro: correr el Step 6 desde la extensión de VS Code y comparar el schema de la herramienta Agent con la spec
  impact: cosmetic — no hubo efecto en el resultado
  suggested_fix: SUGGESTION, unverified — describir el contrato como "esperar todos los resultados de la tanda
    antes de la siguiente" en vez de nombrar un parámetro de la herramienta
  seen: 1
  plugin_version: 1.4.0

- id: BUG-20261028-03
  status: open
  date: 2026-10-28
  talk: agentes-y-multiagentes
  step: 6 (Polish)
  where: agents/diagram-illustrator.md — rutas de scripts
  what: la spec tiene fija la ruta `~/.claude/plugins/cache/talksmith/talksmith/1.4.0/...` en vez de la raíz
    del plugin
  expected: rutas relativas a `${CLAUDE_PLUGIN_ROOT}` (o a la raíz resuelta en el arranque)
  actual: esta sesión usó la raíz marketplaces (`~/.claude/plugins/marketplaces/talksmith`). Las dos son 1.4.0,
    así que no hubo diferencia, pero la ruta fija se va a desactualizar en la próxima versión
  repro: grep "cache/talksmith/talksmith/1.4.0" agents/diagram-illustrator.md
  impact: degraded — en una versión futura puede llamar a scripts de una versión vieja
  suggested_fix: SUGGESTION, unverified — reemplazar la ruta fija por `${CLAUDE_PLUGIN_ROOT}`
  seen: 1
  plugin_version: 1.4.0

- id: BUG-20261028-04
  status: open
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

- id: BUG-20261028-05
  status: open
  date: 2026-10-28
  talk: redes-generativas-antagonicas
  step: 6 (Polish) — contrato de referencias de imagen
  where: agents/editor.md → Step 6 (b) (refs solo .png/.jpg) vs md-to-deck (inlinea .svg)
  what: el spec del Editor exige refs .png/.jpg en final.md, pero este Talk mantiene 20 refs .svg a pedido del
    presentador (memory.md 2026-10-17), 6 de ellas sin PNG gemelo (bce-dos-casos, ciclo-lote, loss-curva-real,
    loss-curva-falsa, stylegan-simple, qr-pytorch-gans)
  expected: que el spec y el pre-flight de md-to-deck digan si las refs .svg están permitidas
  actual: el render las maneja (inlinea el SVG en el deck y lo rasteriza para el .pptx), pero la auditoría del
    Step 6 (b) las marcaría como fallas. La excepción no está documentada
  repro: grep -c '\.svg)' talks/redes-generativas-antagonicas/final.md; comparar con editor.md Step 6 (b)
  impact: cosmetic — el resultado es correcto; el riesgo es que un Polish futuro las "arregle" a .png y pierda la animación
  suggested_fix: SUGGESTION, unverified — documentar las refs .svg como permitidas (y necesarias para que haya
    animación en el deck) en editor.md Step 6 (b) y en el pre-flight de md-to-deck
  seen: 1
  plugin_version: 1.4.1

- id: BUG-20261028-06
  status: open
  date: 2026-10-28
  talk: redes-generativas-antagonicas
  step: 6 (Polish) — animación de diagramas hechos a mano
  where: agents/editor.md línea ~141 (bullet `animation:`) vs skills/animate-svg/SKILL.md
  what: editor.md dice "The same section works in the `<!-- image-note: … -->` under a hand-drawn diagram", pero
    ningún script ni otro spec define `image-note` (grep en el plugin 1.5.1: una sola mención). Para el presentador
    esa clave no existe; la convención es el bloque ```ascii con su `<!-- ascii-note: -->`
  expected: una sola convención documentada para la nota de un diagrama hecho a mano
  actual: este Talk usó `image-note` siguiendo esa línea; se migró a un bloque ```ascii de documentación (la slide ya
    tiene imagen → documentation_only) + `ascii-note` con intent/animation. polish-ascii scan los ve: 8 bloques,
    documentation_only: true, nota adjunta
  repro: grep -rn "image-note" ~/.claude/plugins/marketplaces/talksmith
  impact: cosmetic — confunde al autor del draft; nada lee la clave
  suggested_fix: SUGGESTION, unverified — reemplazar la frase por un puntero a *Optional ASCII alongside an image
    link*: un bloque ```ascii de documentación + su ascii-note es la forma de anotar un diagrama hecho a mano
  seen: 1
  plugin_version: 1.5.1

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
