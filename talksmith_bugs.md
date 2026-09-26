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

## polish-images: el SKILL.md documenta `--final` y `-o/--output` para `scan`, pero el CLI no los acepta (2026-09-26)

- **Contexto:** Talk `talks/como-se-entrena-un-llm2`, Step 6 (Polish), paso 1b (Image-Illustrator), Talksmith 1.0.0.
- **expected:** según la tabla de flags de `skills/polish-images/SKILL.md` (líneas 65 y 69), `--final` vale para "every subcommand" y `--output` / `-o` para `scan` · `annotate`.
- **actual:** `polish_images.py scan --help` muestra `usage: polish_images scan [-h] [--format {json,human}] [--language LANGUAGE] final_path`: `final.md` es posicional y la salida va solo a stdout. Pasar `--final`, `-o` u `--output` a `scan` termina con exit 2. El rol se recuperó usando el posicional y redirigiendo stdout.
- **Repro:** `python3 ${CLAUDE_PLUGIN_ROOT}/skills/polish-images/polish_images.py scan --final talks/<Talk>/final.md -o /tmp/scan.json` → exit 2 (argparse).
- **suggested_fix:** probablemente convenga alinear uno con otro: agregar `--final` / `-o` a `scan` en el parser (como ya tienen los demás subcomandos), o corregir la tabla del SKILL.md. Vale revisar si `polish-ascii` tiene la misma divergencia, ya que comparte la forma.

## Diagram-Illustrator: vuelve a devolver el turno con renders en curso (2026-09-26)

- **Contexto:** Talk `talks/como-se-entrena-un-llm`, Step 6 (Polish), paso 1, Talksmith 1.0.0 (`agents/diagram-illustrator.md`). 15 bloques ASCII.
- **expected:** que el rol no cierre el turno mientras haya un dispatch pendiente (el contrato de finalización que se agregó en 0.100.0 para BUG-20260901-13).
- **actual:** escribió los 15 sidecars, lanzó 5 renders en background y devolvió un reporte "DIAGRAM PASS INCOMPLETE" con 0 renderizados, 5 en curso y 10 sin empezar. El propio reporte dice que se lo "hizo devolver" y que su spec se lo prohíbe. Aviso: el reporte fue honesto (armado desde `ls images/`, no reclamó nada), así que esa parte del fix funciona; lo que no se sostiene es "no cerrar el turno".
- **Repro:** unknown — visto una vez en esta versión; el trigger parece ser el mismo patrón de dispatch en background con renders de varios minutos.
- **suggested_fix:** posiblemente el runtime cierre el turno de un subagente cuando todos sus hijos están en background, más allá de lo que diga la spec; valdría la pena que el rol espere a cada hijo en foreground (o con un bucle de espera explícito) en vez de confiar en la instrucción.

## polish-ascii: `scan` ignora los bloques bajo un H1 no numerado (p. ej. `# Apertura`) (2026-09-26)

- **Contexto:** mismo Talk y paso. `final.md` tiene una sección de apertura sin número (`# Apertura`, como la sección "Repaso" de la clase 8) con un bloque ASCII en las líneas 56–70.
- **expected:** que `scan` devuelva los 15 bloques ASCII de `final.md`.
- **actual:** devolvió 14. Solo trata como secciones con láminas a los H1 numerados, `Agenda` y `Conclusions`, así que el bloque de la apertura queda "sin lámina" y se omite en silencio. El rol lo agregó a mano al plan (`sa-1-1`); en la próxima pasada el `scan` lo va a volver a omitir, así que el control de digest no lo cubre.
- **Repro:** un `final.md` con `# Apertura` (sin número) que contenga `## 1. …` con un bloque ```` ```ascii ````; correr `polish_ascii.py scan` y contar los bloques.
- **suggested_fix:** probablemente convenga que el scanner compartido (`skills/_shared/_context.py`) trate cualquier H1 que no sea de metadatos (Thesis, Agenda, Open questions, Cut material) como sección con láminas, o que al menos avise cuando encuentra una fence `ascii` fuera de una lámina en lugar de omitirla.

## md-to-deck: el FILL rellena con nombres de plantilla y formatos retirados que el propio borrador pide (2026-09-26)

- **Contexto:** Talk `talks/como-se-entrena-un-llm2`, Step 7 (Render, HTML), Talksmith 1.0.0. El Editor escribió pistas `<!-- template: comparison -->` (dos láminas) y `<!-- format: list -->` (una) en el borrador durante Step 4, siguiendo `agents/editor.md` → *Draft with the slide taxonomy in mind*.
- **expected:** que las pistas que el Editor puede escribir sean nombres vigentes del catálogo `config/pptx-styles/slide-templates.md`.
- **actual:** `comparison` y `format: list` están retirados; el FILL tuvo que traducirlos a mano (`comparison` → columnas lado a lado o pros/contras según el contenido; `list` → grilla), porque de otro modo la lámina cae en la plantilla de respaldo. El Editor no tiene cómo saber qué nombres están vigentes.
- **Repro:** un `draft.md` con `<!-- template: comparison -->` bajo un `##`; correr FILL + `audits/template_diversity.py` y ver la lámina marcada como fallback si no se la traduce.
- **suggested_fix:** probablemente convenga que la lista de valores válidos de `template:` / `format:` viva en un solo lugar que lean tanto el Editor como el FILL, y que el FILL (o un audit) avise explícitamente "pista retirada: X → usar Y" en lugar de depender de que el LLM lo note.
