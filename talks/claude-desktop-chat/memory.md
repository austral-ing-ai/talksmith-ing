# memory.md — claude-desktop-chat

**Current step:** 7 — Render complete (html-strict, re-corrido con el plugin 0.74.1) awaiting_presenter
**Awaiting:** 2026-08-01 — deck repulido y re-rendido con el plugin **0.74.1**, sin tocar contenido. `output/html/index.html`: 33 laminas, **2,66 MB** (bajo de 3,3 MB porque los 12 diagramas ahora van como SVG vector inline). Awaiting: la duracion, que sigue en **65 min contra un bloque de 60** (en la parte 2 el presentador decidio que el tiempo no era restriccion; aca no lo dijo), y el paso 8 (Learnings).
**Mode:** C (Presenter Outline) — heredado del Talk combinado del que salió esta mitad.
**Topic:** Claude Desktop, la superficie de chat: el chat que la audiencia ya usa a diario, su límite de memoria de entrenamiento, los conectores que lo abren al mundo real del usuario, Schedule para que trabaje solo, y la parte 1 de la misión de Faro resuelta enteramente dentro del chat.
**Folder:** talks/claude-desktop-chat/
**Started:** 2026-07-31

---

## Talk briefing

Parte 1 de un par de clases para el Master in Management (MiM) del IAE Business School. Sale de partir en dos el Talk combinado de 120 minutos que vivía en `talks/claude-cowork/`. Esta mitad se queda en la superficie de chat de Claude Desktop: encuadre del problema y del catálogo de herramientas de Claude, el chat que responde de memoria de entrenamiento, los conectores como concepto transversal a todas las IAs (incluidos Claude in Chrome y el cuidado de prompt injection), Schedule, y la placa de misión parte 1. La parte 2 (Claude Cowork, archivos .md, Projects, Skills, Subagentes, la placa de misión parte 2 y las Conclusions) queda en `talks/claude-cowork/`, con class "Claude Cowork".

---

## 2026-07-31 — Split del Talk combinado (Step 5, Review)

- Status: complete
- What was decided: el presentador decidió partir la clase de 120 minutos en dos clases independientes. Esta carpeta (`claude-desktop-chat`, class "Claude Desktop - Chat") toma las secciones 1 a 5 del deck original. Encuadre elegido para el trabajo editorial: **mínimo mecánico**, sin slides nuevas. No se agregó slide de cierre ni de repaso; la clase termina en la placa de misión parte 1, que ya funciona como cierre.
- Qué heredó de la carpeta original:
  - 5 secciones contiguas (1 Introducción · 2 Claude Chat (Desktop) · 3 Conectores · 4 Schedule · 5 La misión · parte 1), 18 slides, numeración contigua dentro de cada sección.
  - 13 bloques ASCII con sus `ascii-note`, 2 referencias de imagen (`images/connectors_directory.png`, `images/connector_browser.png`) y 2 directivas `generate-image` (slides 1.1 y 1.2).
  - La carpeta `images/` completa y el corpus (`research/corpus/agentic-ai-deck.zip.md`, `research/corpus/mision - auto.zip.md`), copiados tal cual.
  - Frontmatter con `class: "Claude Desktop - Chat"` y `duration: 60 min (a confirmar)` ya ajustados por el script de split.
- Qué se reescribió en esta pasada:
  - **Thesis** (Claim + Why it matters): ahora describe solo esta clase (chat de memoria → conectores → Schedule) y cierra apuntando a la segunda clase. Salieron las promesas de Cowork, Projects, Skills, Subagentes, archivos .md y "delegar resultados".
  - **Agenda**: el `Narrative arc` pasó de narrar once secciones a narrar cinco, en el mismo párrafo denso de la casa; la lista `Sections (in delivery order)` quedó 1:1 con los cinco H1.
  - **Open questions**: se podaron las entradas exclusivas de la parte 2 (screenshots de la interfaz de Cowork y el stub de la slide 6.5, slash commands de Skills 9.2-9.3, subagentes a pedido, audit trail de Conclusions.2, carpeta `skills/` de la misión, banner DEMO TIME de 6.5, piezas borradas el 2026-07-30, locality de Live Artifacts, y las URLs de round 3 que no son de esta mitad). Se conservaron las que tocan chat, conectores, Claude in Chrome, Schedule y el sourcing de Gemini, con los números de slide verificados contra este archivo (3.2, 3.3, 4.1 siguen apuntando bien). Se agregaron tres entradas nuevas: duración a confirmar, asides sin renderizar, y la nota del split con el puntero a la carpeta hermana.
  - **Cut material**: quedaron solo los dos ítems cortados de estas cinco secciones (detalles internos de Claude Code, con el puntero corregido a la slide 1.4; y el detalle mecánico del Schedule de Cowork, con la referencia corregida a la sección 4). Se agregó una entrada que aclara que el material de la parte 2 se mudó, no se cortó.
  - **Referencias cruzadas**: 11 arreglos en las cinco secciones (13 referencias distintas), más 2 punteros corregidos en `# Cut material`. Todo lo que apuntaba a secciones 6-11 o a las Conclusions ahora apunta a "la segunda clase" / "la clase de Cowork". Los más notables: slide 1.2 (bullet de contenido del camino, Sources y notes), slide 1.4 (dos bullets de contenido, el `ascii-note`, Sources y dos pasajes de las notes), slide 4.2 (las notes que anticipaban la sección 6 de Cowork sobre archivos locales) y slide 5.1 (las notes que mandaban la parte 2 "más adelante" y proponían una pausa a mitad de clase; ahora cierran la clase).
  - Las referencias internas que siguen siendo válidas se dejaron intactas: "Sección 3" en 2.2, "sección 4" en 3.9, "la sección 5" para el reveal de Faro en 3.8, "slide 3.7" en 3.1.
- Nota sobre la placa de misión: el ASCII de la slide 5.1 era byte-idéntico al de la vieja slide 11.1 (placa gemela). Ahora viven en Talks distintos, así que la restricción de gemelas ya no aplica dentro de un mismo archivo. El ASCII de 5.1 se dejó exactamente como estaba.
- Key inputs: `draft.md` post-split (794 líneas), `talks/claude-cowork/memory.md` (formato del header y de las entradas), `config/profile.md`.
- Files created/modified: `talks/claude-desktop-chat/draft.md` (Thesis, Agenda, Open questions, Cut material, referencias cruzadas), `talks/claude-desktop-chat/memory.md` (nuevo).
- Verificación: frontmatter parsea, `class: "Claude Desktop - Chat"`; 26 líneas de fence = 13 bloques ASCII, sin cambios; las 2 referencias de imagen resuelven en `images/`; las 2 citas de corpus resuelven en `research/corpus/`; secciones 1-5 contiguas y slides contiguas dentro de cada una; la Agenda coincide 1:1 con los H1; 18 campos `### Presenter feedback` y 7 `**Presenter feedback:**`, todos vacíos, 0 `[open]` y 0 `[closed]`; suma de "Tiempo objetivo" = **50 min** sobre 18 slides.
- Pending open questions:
  - Duración real de la clase sin confirmar. El frontmatter dice `60 min (a confirmar)` y los tiempos objetivo suman ~50 min sin Q&A ni pausa.
  - Polish (Step 6) y Render (Step 7) nunca corrieron para esta carpeta: no existen `final.md` ni `output/`. Los SVG y PNG en `images/` vienen del Polish del Talk combinado; hay que re-correr Polish desde cero contra este `draft.md`.
  - Las 2 directivas `generate-image` de las slides 1.1 y 1.2 siguen sin imagen: la sesión del último Polish no tenía capacidad de generación de imágenes.
  - Los ítems heredados de vigencia de fuentes (nube de Schedule beta desde julio 2026, planes pagos de Claude in Chrome, sourcing de Gemini en 3.3) siguen abiertos en `# Open questions`.

---

## 2026-07-31 — Polish (Step 6)

- Status: complete
- What was decided: primera corrida de Polish para esta carpeta. `final.md` se derivó de `draft.md` por copia byte a byte y desde ahí todo el trabajo fue mecánico —SVGs, referencias de imagen, rescate de feedback y stripping— sin reescribir prosa. `draft.md` quedó congelado y se verificó al cierre que su md5 no cambió (`d7f75b62df0a8b21262aed83d5006ab7`).
- Pasada de diagramas (diagram-illustrator, previa a esta mitad editorial): 13 bloques ASCII, los 13 render-driving, 12 reusados por stamp y 1 re-renderizado (`s1-4-1`, el ASCII de las cuatro herramientas que se reescribió en el split). 0 fallidos, 0 documentation-only.
- **Fences inlineadas:** `polish_ascii.py cleanup` reescribió las 13 fences ```` ```ascii ```` a referencias de imagen con su eco `<!-- ascii-source: -->`, dejando cada `<!-- ascii-note: -->` en su lugar. 0 saltadas por falta de mapping. Verificado: **0 fences de cualquier tipo sobreviven** en `final.md` (741 líneas).
- **Referencias consolidadas:** las 13 referencias nuevas se reescribieron de `.svg` a su companion `.png` por la regla Keynote-safe; los `.svg` quedan en disco como fuente de verdad. Las 2 capturas heredadas (`connectors_directory.png`, `connector_browser.png`) ya cumplían y no se tocaron. Total: **15 referencias**, todas bajo `images/`, todas `.png`, todas resuelven en disco, 0 extensiones prohibidas (`.svg` / `.webp` / `.avif` / `.heic`).
- **Rescate de feedback:** `feedback_cycle.py rescue-open` reportó *no [open] bullets to rescue*, como se esperaba —los campos de feedback de este Talk están vacíos por decisión permanente del presentador (0 `[open]`, 0 `[closed]`).
- **Stripping de feedback:** `strip_feedback.py` sacó los **25 bloques** de `Presenter feedback` de `final.md` (18 `### Presenter feedback` a nivel slide + 7 `**Presenter feedback:**` en Thesis, Agenda y los 5 headers de sección; 0 bullets legacy). Verificado: 0 ocurrencias del string en `final.md`, y la garantía de línea en blanco antes de cada `---` se cumple en los 23 bordes de slide/sección (el único `---` sin línea en blanco delante es el cierre del frontmatter, que es correcto). `draft.md` conserva los 25 campos intactos y vacíos para futuras rondas de review.
- **Garbage collection de `images/`:** la carpeta arrastraba 128 archivos del deck combinado, con varias tripletas viejas que difieren de las vivas solo por slug (`s2-1-1-chat-solo-vs-conectores` vs la viva `s3-1-1-...`, `s1-1-1-chat-de-fabrica` vs `s2-1-1-...`, `s2-5-1-conector-dos-direcciones` vs `s3-2-1-...`, `s2-2-1-memoria-vs-busqueda` vs `s3-3-1-...`). Se corrió `polish_ascii.py gc` primero en dry-run y se auditó la lista contra las referencias vivas: 0 solapamientos con archivos referenciados, 0 colisiones de stem, y las 2 capturas del presentador ausentes de la lista. Recién ahí se aplicó. **29 tripletas huérfanas, 87 archivos borrados; 128 → 41** (13 diagramas × 3 + 2 capturas). Nota operativa: el primer `--apply` falló con `Operation not permitted` porque el mount FUSE de Cowork bloquea `unlink`; hubo que habilitar borrado en la carpeta antes de re-correrlo.
- **Asides sin renderizar:** siguen las **2 directivas reales** `<!-- generate-image: right | ... -->` en las slides 1.1 y 1.2, sin imagen. El image-illustrator devolvió `unavailable`: esta sesión no tiene capacidad de generación de imágenes. Se dejaron en su lugar a propósito —son comentarios HTML, renderizan inocuas, y su descripción es la clave de idempotencia de una futura pasada. (Hay una tercera aparición del string `generate-image` en `# Open questions`, pero es prosa que documenta el pendiente, no una directiva.)
- Nota de estilo: **`config/diagram-style.md` no existe en este subject repo**, así que la pasada de diagramas corrió con las reglas visuales estándar que trae el plugin. Si el presentador quiere fijar paleta o convenciones propias, ese archivo es el lugar.
- Key inputs: `draft.md` (congelado), el plan de render anotado del diagram-illustrator, skills `talksmith:polish-ascii` y `talksmith:feedback-cycle`.
- Files created/modified: `talks/claude-desktop-chat/final.md` (nuevo), `talks/claude-desktop-chat/images/` (87 archivos huérfanos podados), `talks/claude-desktop-chat/memory.md`.
- Verificación de cierre: frontmatter parsea, `class: "Claude Desktop - Chat"`; 0 fences; 15 referencias válidas sin extensiones prohibidas; 0 `Presenter feedback` en `final.md` y 25 en `draft.md`; md5 de `draft.md` sin cambios; 5 secciones y 18 slides, con los encabezados idénticos a los de `draft.md`.
- Pending open questions:
  - Las 2 directivas `generate-image` de las slides 1.1 y 1.2 siguen pendientes. Re-correr el paso de image-illustrator en una sesión con generación de imágenes, o borrarlas.
  - Duración real de la clase sin confirmar (sigue de la entrada anterior).
  - Step 7 (Render) nunca corrió: `output/` sigue vacío.

---

## 2026-07-31 — Slide de cierre (Step 5, Review reabierto)

- Status: complete
- What was decided: el presentador pidió una lámina de conclusiones que resuma lo visto. Revierte la decisión del split, que había cerrado la clase en la placa de misión sin recap. Se agregó un bloque `# Conclusions` con **una sola slide**, después de `# 5. La misión · parte 1` y antes de `# Open questions`, siguiendo el patrón del Talk hermano (bloque no numerado, sin "Goal of this section" y sin `**Presenter feedback:**` a nivel bloque).
- La slide: `## 1. Qué nos llevamos de esta clase` (30 caracteres, bajo el techo de 40). Cinco bullets que recorren el arco real del deck: el chat de memoria con sus tres límites, los conectores que lo sacan del aislamiento y además actúan, los dos casos más la división out of the box / externos por MCP, Schedule con la pregunta de dónde corre, y la parte 1 de la misión con el puente a la segunda clase. Sin claims nuevos: todo lo afirmado ya está sourceado en su slide de origen, y `### Sources` lo declara en el estilo de slide organizativa que el deck ya usa (1.1, 1.2).
- **Sin diagrama, por decisión:** el arco de cuatro beats es una secuencia de etiquetas, no una forma. Un ASCII de cuatro cajas en fila repetiría los bullets sin agregar información, y la slide ya tiene la densidad tope. El deck queda en 13 bloques ASCII, sin cambios.
- Efectos colaterales corregidos: el `Narrative arc` de la Agenda cerraba la clase en la placa de misión, ahora menciona el repaso de cierre; las Speaker notes de 5.1 afirmaban ser "la última lámina de la clase", que ya es falso, y ahora anuncian el repaso que viene. La lista `Sections (in delivery order)` NO se tocó: Conclusions no es una sección numerada.
- Key inputs: pedido del presentador vía chat; `talks/claude-cowork/draft.md` (patrón estructural del bloque `# Conclusions`); `config/profile.md`; skill `talksmith:desrobotizar` aplicada a la prosa nueva.
- Files created/modified: `talks/claude-desktop-chat/draft.md`, `talks/claude-desktop-chat/memory.md`, `config/feedback-backlog.md`.
- Verificación: YAML parsea, `class: "Claude Desktop - Chat"`; 26 líneas de fence = 13 bloques pareados, sin bloques nuevos; las 2 referencias de imagen resuelven; secciones 1-5 contiguas e intactas, Conclusions con exactamente 1 slide; Agenda 1:1 con los cinco H1 numerados; 19 `### Presenter feedback` y 7 `**Presenter feedback:**`, todos vacíos, 0 `[open]` y 0 `[closed]`; suma de "Tiempo objetivo" = **53 min** sobre 19 slides.
- Pending open questions:
  - `final.md` y `output/` quedaron desactualizados a propósito: no incluyen la slide nueva. Re-correr Polish (Step 6) y Render (Step 7).
  - Duración real de la clase sin confirmar: 53 min contra `duration: 60 min (a confirmar)`.
  - Las 2 directivas `generate-image` de las slides 1.1 y 1.2 siguen pendientes.

---

## 2026-07-31 — La slide de cierre pasa de summary a wrap-up (Step 5, refinamiento de la entrada anterior)

- Status: complete
- What was decided: el presentador refinó el pedido de la entrada anterior: "más que un summary, un wrap-up". La slide que había quedado enumeraba una sección por bullet, en orden, y leía como índice en pasado. Se reescribió para que conteste "¿y ahora qué?" en vez de "¿qué vimos?". La slide sigue siendo una sola, en el mismo lugar; no se agregó ni se movió nada.
- Título: `## 1. Qué nos llevamos de esta clase` → `## 1. El lunes: qué hacer con esto` (28 caracteres). El título viejo anunciaba un repaso; el nuevo ancla el cierre en la acción y sigue el patrón de dos puntos que ya usan varias slides del deck.
- Content: de cinco bullets (uno por sección) a **cuatro**, uno por beat de cierre. (1) La idea que se llevan: el chat consulta información actual y ejecuta acciones sobre mail y agenda, con configuración y sin instalar nada ni escribir código. (2) Lo accionable esta semana: activar la búsqueda, conectar mail y agenda, dejar programado un trabajo recurrente. (3) El cuidado, como última palabra del tema y no como bullet enterrado: ninguna acción que importe se ejecuta sin aprobación humana, y Anthropic documenta el prompt injection como riesgo abierto que no es cero. (4) Hacia dónde sigue: la segunda clase retoma este chat extendido y sigue en Claude Cowork, sobre carpetas y archivos. Sin claims nuevos: los cuatro puntos ya están sourceados en 2.1, 3.2, 3.3, 3.6, 3.8, 4.1 y 5.1; `### Sources` no cambió y mantiene el estilo de slide organizativa.
- Prosa bajo `desrobotizar`, incluido `references/reglas-propias.md`. Tres reglas propias mordieron y cambiaron la redacción respecto del borrador natural: la fórmula de transformación "deja de X y pasa a Y" (que era literalmente cómo venía formulado el beat) se reemplazó por el estado nuevo dicho plano; la etiqueta autorreferente tipo "la idea que ordena todo" se cortó del bullet y quedó solo en las notas del orador; el registro de slide se mantuvo impersonal ("la cuenta que ya está en uso" en vez de "la cuenta que ya tienen"), con la segunda persona reservada a las Speaker notes. Sin em dashes.
- **Sigue sin diagrama**, por la misma razón de la entrada anterior y con más fuerza: cuatro etiquetas en fila no son una forma. El deck queda en 13 bloques ASCII, sin cambios.
- Speaker notes reescritas de repaso a cierre: arrancan diciendo explícitamente que la lámina no vuelve sobre el temario, recorren los cuatro beats en orden, marcan la advertencia como última palabra del tema (con puntero a 3.6 si alguien pide detalle) y cierran con el puente a Cowork y la consigna antes del Q&A. `Tiempo objetivo: ~3 min` sin cambio, así que el total del deck sigue en **53 min** sobre 19 slides.
- Vecindad revisada: el `Narrative arc` de la Agenda cerraba con "un repaso corto de las cuatro piezas de la clase", que ya no describe la lámina; ahora describe el cierre en cuatro tiempos. Las Speaker notes de 5.1 decían "la siguiente recorre lo que se vio"; ahora dicen "la siguiente dice qué hacer el lunes con lo visto". `Sections (in delivery order)` sin tocar.
- Key inputs: pedido del presentador vía chat; `draft.md` slides 2.1, 3.2, 3.6, 4.1, 5.1 (verificación de que no hubiera claims nuevos); skill `talksmith:desrobotizar` + `references/reglas-propias.md`.
- Files created/modified: `talks/claude-desktop-chat/draft.md`, `talks/claude-desktop-chat/memory.md`, `config/feedback-backlog.md`.
- Verificación 8/8 PASS: YAML parsea con `class: "Claude Desktop - Chat"`; 26 líneas de fence = 13 bloques pareados, sin cambio; las 2 referencias de imagen resuelven; Conclusions con exactamente 1 slide y secciones 1-5 intactas; 19 `### Presenter feedback` + 7 `**Presenter feedback:**`, todos vacíos, 0 `[open]` / 0 `[closed]`; título de 28 caracteres; suma de "Tiempo objetivo" = 53 min sobre 19 slides; sin em dashes en la prosa nueva.
- Pending open questions:
  - `final.md` y `output/` siguen desactualizados a propósito. Re-correr Polish (Step 6) y Render (Step 7).
  - Duración real sin confirmar: 53 min contra `duration: 60 min (a confirmar)`.
  - Las 2 directivas `generate-image` de las slides 1.1 y 1.2 siguen pendientes.

---

## 2026-07-31 — Reestructura en 7 secciones (Step 5, ronda de 14 bullets)

- Status: complete
- What was decided: el presentador dejó 14 bullets de feedback en `draft.md` más dos pedidos por chat. Tres de ellos se pisaban sobre el esqueleto (renombrar la sección 2 a "Context augmentation", borrarla y mandar su slide a Connectors, y elevar Web search y Claude in Chrome a secciones propias). Se le ofrecieron tres esqueletos y eligió la **opción 1: Context augmentation como paraguas conceptual**, con Web search, Connectors y Claude in Chrome como secciones hermanas después de ella.
- **Estructura nueva (7 secciones, 22 slides, 59 min):** 1 Introducción (6) · 2 Context augmentation (2) · 3 Web search (2) · 4 Connectors (6) · 5 Claude in Chrome (2) · 6 Schedule (2) · 7 La misión parte 1 (1) · Conclusions (1). Antes: 5 secciones, 19 slides, 53 min.
- **Slides nuevas (4):** `1.5 Claude Desktop Chat` (mismo producto en dos empaquetados; diferencias periféricas; foco en aspectos avanzados; nota de que el core común hace que todo aplique también a Cowork). `1.6 El chat en Claude Desktop` (lámina de pantalla con `chat-home.png`). `3.2 La búsqueda en pantalla` (lámina de pantalla con `websearch.png`). `4.5 Buscar, conectar y autorizar` (salió de partir la vieja 3.8, que apilaba dos capturas en una sola lámina: el layout que el presentador marcó como malo se resolvió con una imagen por slide).
- **Slide reescrita:** `1.3 Quién es Anthropic` pasó de dos bullets a las cuatro cajas que dictó el presentador (Qué es / Por qué existe / Cómo se estructura / Qué la distingue), como items etiquetados. Las URLs de Constitutional AI, RSP y AUP se citaron sin fetch verificado en esta ronda y quedaron como open question.
- **Concepto agregado:** in-context learning entra como cuarto bullet de `2.1` y como el concepto que da nombre a la sección. Es lo que hace que "Context augmentation" sea un paraguas real y no solo un título: si el prompt es la única palanca, las dos secciones siguientes son las dos formas de llenarlo.
- **Slide cortada:** `Cuidado: prompt injection` (ex 3.6), por pedido del presentador vía chat. No se borró: el contenido completo, su ASCII y su fuente están en `# Cut material`, y el tema sobrevive en dos lugares proyectables o decibles — las Speaker notes de `5.1` (párrafo propio, con las tres prácticas y el "el riesgo no es cero" textual) y el tercer bullet de la lámina de cierre, que ahora cita el artículo de seguridad directamente. Riesgo asumido y registrado en Open questions: si en el ensayo el cuidado queda flojo, la lámina se repone desde Cut material.
- **Rename global:** "conectores" → "Connectors" en todo el deck (thesis, agenda, títulos, Content, ASCII, Sources, Speaker notes). Verificado: 0 ocurrencias de "conector/conectores" fuera de los bullets de feedback verbatim. En las secciones 2 y 3 el término se evita a propósito: el presentador pidió introducirlo recién en la sección 4, así que 2.2 nombra la segunda vía como "conectar el chat a los sistemas del usuario".
- Prosa nueva bajo `talksmith:desrobotizar` + `references/reglas-propias.md`. Reglas que mordieron: sin em dashes (los bullets nuevos usan coma o punto), registro impersonal en láminas con la segunda persona reservada a Speaker notes, sin minimizadores de fricción (la 4.5 dice "buscar, conectar y autorizar" y no "con un clic"), sin etiquetas autorreferentes.
- Key inputs: los 14 bullets de `Presenter feedback` en `draft.md`; dos pedidos por chat (borrar la slide de prompt injection; elegir el esqueleto); `config/profile.md`; `images/` para confirmar que `chat-home.png` y `websearch.png` existían antes de referenciarlas.
- Files created/modified: `talks/claude-desktop-chat/draft.md`, `talks/claude-desktop-chat/memory.md`, `config/feedback-backlog.md` (14 filas espejadas).
- Verificación: YAML parsea con `class: "Claude Desktop - Chat"`; 12 bloques ASCII con fences pareados; 7 secciones con slides contiguos y numeración reiniciada por sección; la lista `Sections (in delivery order)` es 1:1 con los H1 numerados; las 4 referencias de imagen resuelven contra `images/`; 14 bullets `[closed]` con sus 14 `Resolution:`, 0 `[open]`, 0 sin espejar en el backlog; suma de "Tiempo objetivo" = 59 min sobre 22 slides.
- Pending open questions:
  - Duración: 59 min contra `duration: 60 min (a confirmar)`. Ya no hay margen para Q&A ni pausa; confirmar el bloque real.
  - `final.md` y `output/` desactualizados a propósito. Re-correr Polish (Step 6) y, si se quiere, Render (Step 7).
  - Las 2 directivas `generate-image` de las slides 1.1 y 1.2 siguen pendientes.
  - Fuentes de las cuatro cajas de Anthropic (1.3) sin fetch verificado.
  - Qué diferencias concretas nombrar entre Claude web y Claude Desktop (1.5).
  - Prompt injection sin lámina propia: decisión a revisar después del ensayo.

---

## 2026-07-31 — Segunda ronda de review (5 bullets) y reordenamiento del cierre

- Status: complete
- What was decided: sobre el deck ya reestructurado, el presentador dejó 5 bullets más y editó a mano dos títulos. El deck pasa a **25 slides / 65 min**, que es el problema abierto que deja esta ronda.
- **Curación (4.3):** los out of the box están curados por Anthropic. Entró como bullet propio en el Content, como línea nueva en el ASCII (`CURADOS por Anthropic` / `SIN curacion`), en las Speaker notes y en la cita de Sources, que lo deriva por contraste del "not been verified by Anthropic" del artículo de custom connectors. Es lo que sostiene el criterio de confianza que la slide ya enunciaba, así que dejó de ser un aparte y pasó a ser la razón.
- **Dos slides nuevas al final de la sección 4:** `4.7 Agregar un external connector` (captura `custom-connector.png`, más el flujo de alta: URL del servidor MCP y credenciales) y `4.8 Dónde buscar servidores MCP publicados` (la tabla de cinco directorios que dictó el presentador). Se separaron en dos láminas en vez de meter captura y tabla juntas, siguiendo la lección de layout de la ronda anterior. Las cinco fuentes de la tabla son de terceros y quedaron sin verificar.
- **Slide nueva 6.2 `Dónde vive el Schedule`** con `schedule.png`; la vieja 6.2 pasó a 6.3.
- **Conclusiones movidas delante de la sección 7.** El orden de cierre ahora es Schedule → Conclusions → placa de la misión. Efectos colaterales corregidos: las Speaker notes de Conclusions ya no dicen "cerrar antes del Q&A" sino que anuncian la placa; las de la placa ya no anuncian una lámina de cierre posterior; el `Narrative arc` se reescribió con el orden nuevo; la cita de Sources de Conclusions pasó de "secciones 2 a 7" a "2 a 6".
- **Placa de misión vaciada.** Pedido: "acá borrar todo y solo mencionar que vamos a trabajar en la mission, es un slide que da pie a mostrar". Quedó la placa ASCII más una línea. Los tres bullets de Faro no se perdieron: bajaron a Speaker notes, que ahora encuadran la lámina como pie para mostrar la consigna en vivo.
- **Ediciones a mano del presentador, respetadas tal cual:** sección 7 renombrada `La mission` y slide 5.1 renombrada `Que es Claude in Chrome ?`. La lista `Sections (in delivery order)` se sincronizó al heading verbatim; la ortografía quedó anotada en Open questions para que él decida.
- Key inputs: 5 bullets de `Presenter feedback`; `images/` para confirmar que `custom-connector.png` y `schedule.png` existían antes de referenciarlas.
- **Nota operativa (para futuras sesiones remotas):** la copia staged de `draft.md` bajo `/mnt/user-data/uploads/` quedó cacheada con el contenido viejo y `find-open` devolvió los bullets de la ronda anterior. La salida fue copiar el archivo a un nombre nuevo en el disco del presentador y stagear ese. Si los bullets detectados no coinciden con lo que el presentador dice haber escrito, sospechar del caché antes que del archivo. Además, un bullet indentado con un espacio (` - texto`) no lo detecta `find-open`: hay que normalizarlo a columna 0.
- Files created/modified: `talks/claude-desktop-chat/draft.md`, `talks/claude-desktop-chat/memory.md`, `config/feedback-backlog.md` (5 filas más, 19 en total para este Talk).
- Verificación: 12 bloques ASCII con fences pareados; 7 secciones con numeración contigua; agenda 1:1 con los headings; las 6 referencias de imagen resuelven; 19 bullets `[closed]` con sus 19 `Resolution:`, 0 `[open]`, 0 sin espejar; Conclusions precede a la sección 7.
- Pending open questions:
  - **Duración: 65 min sobre 25 slides contra un bloque de 60.** Candidatas a recorte anotadas en `# Open questions` del draft, por orden: 4.8 (tabla de directorios, es material para repartir), 1.6 y 3.2 (láminas de pantalla reemplazables por demo en vivo).
  - Los cinco directorios MCP de 4.8, sin verificar online.
  - Ortografía de "La mission" y "Que es Claude in Chrome ?".
  - `final.md` y `output/` desactualizados; re-correr Polish.
  - Las 2 directivas `generate-image` de 1.1 y 1.2 siguen pendientes.

---

## 2026-07-31 — Step 6 (Polish)

- Status: complete
- What was decided: `final.md` derivado de `draft.md` (25 slides) con los 12 diagramas renderizados. `draft.md` no se tocó, así que Polish sigue siendo re-corrible.
- **12 bloques ASCII → 12 SVG + 12 PNG companion.** Todos con slug nuevo acorde a la numeración de secciones de esta ronda (`s1-4-1`, `s2-1-1`, `s3-1-1`, `s4-1-1`, `s4-2-1`, `s4-3-1`, `s4-6-1`, `s5-1-1`, `s5-2-1`, `s6-1-1`, `s6-3-1`, `s7-1-1`). Los 39 archivos del Polish anterior, con los slugs viejos, se movieron a `_to_delete/images-polish-anterior/` porque ya no los referencia nada.
- **Dos diagramas necesitaron segunda pasada.** `s1-4-1`: el rótulo "misma base técnica" estaba sobre un parche blanco que partía el corchete en dos, así que el lazo Code-Cowork no leía como lazo; se redibujó con línea continua. `s2-1-1`: la lista "lo que NO ve" era texto suelto y dejaba una franja muerta a la derecha; pasó a panel.
- **`s4-3-1`** salió con el contraste de curación como remate: dos banners del mismo tamaño, "CURADOS por Anthropic" en tarjeta con borde y "SIN curación" en rojo sólido. **`s7-1-1`** salió como placa divisoria, sin cajas ni flechas.
- **Limpieza de `final.md`:** 12 fences reescritos a referencias de imagen con su `ascii-source` preservado; los 12 refs `.svg` reescritos a `.png` (Keynote no embebe SVG); 0 extensiones prohibidas; 0 bullets `[open]` para rescatar; 34 bloques de `Presenter feedback` eliminados (25 H3 + 9 de párrafo).
- **Los dos asides `generate-image` (slides 1.1 y 1.2) siguen sin imagen**, por segunda vez: esta sesión tampoco tenía capacidad de generación de imágenes. Las directivas quedaron en su lugar, las slides conservan su texto y no rompen el render.
- **Caveat de proceso:** el crítico visual ciego no se pudo lanzar en esta sesión (el entorno no expuso la herramienta), así que la revisión de los 12 diagramas la hizo el mismo agente que los dibujó. Los dos defectos de arriba se encontraron y corrigieron así, pero fue autorrevisión y no revisión independiente. El rastro por diagrama quedó en `images/.critique/<nombre>.md`. Conviene que el presentador mire las 12 imágenes antes del render.
- Key inputs: `draft.md` (25 slides); `config/diagram-style.md` del plugin; `cairosvg` + `Pillow` instalados en la sesión para la rasterización.
- Files created/modified: `talks/claude-desktop-chat/final.md` (nuevo), `talks/claude-desktop-chat/images/` (12 SVG + 12 PNG + 12 sidecars `.ascii`), `talks/claude-desktop-chat/memory.md`.
- Verificación: 0 campos `Presenter feedback`, 0 stamps, 0 fences ASCII sin renderizar; 18 referencias de imagen, todas `.png` y todas resolviendo contra `images/` en el disco del presentador; 12 `ascii-source` preservados; línea en blanco antes de cada `---`; 7 secciones / 25 slides; frontmatter intacto.
- Pending open questions:
  - Duración: 65 min sobre 25 slides contra un bloque de 60. Sin resolver.
  - Step 7 (Render) sin correr: `output/` sigue vacío.
  - Los dos asides `generate-image`, pendientes por segunda vez.
  - Los cinco directorios MCP de la slide 4.8, sin verificar online.
  - `.gitignore`: conviene agregar `talks/*/images/.critique/`.

---

## 2026-07-31 — Step 7 (Render, html-strict)

- Status: complete
- What was decided: el presentador eligió el deck HTML compartible. Salió `output/html/index.html`, un Reveal.js autocontenido de 3,3 MB con las 21 imágenes embebidas en base64, las fuentes IBM Plex inlineadas y cero referencias externas. 33 láminas: portada + 7 separadores de sección + 25 slides.
- **`slide-model.json` (32 slides + portada), clasificación por familia:** `content+cards+image` para las slides con diagrama y cards (11), `concept-breakdown` para los sets etiquetados sin imagen (5), `icon-list` para los dos slides de apertura, `content-image` para las cinco láminas de pantalla, `section-agenda` para los 7 separadores.
- **Dos correcciones tras mirar las capturas renderizadas.** (1) Tres slides que había clasificado como `content-image` con varios `facts` salieron como viñetas planas, que es exactamente lo que el invariante del catálogo prohíbe (cards, nunca bullets): `Buscar, conectar y autorizar`, `Agregar un external connector` y `¿Dónde corre? Local o nube` pasaron a `content+cards+image` con cards etiquetadas. (2) En la slide de directorios MCP, la etiqueta `github.com/modelcontextprotocol/servers` desbalanceaba la grilla; quedó `modelcontextprotocol/servers` con "En GitHub" en el cuerpo.
- **Extensiones: se usaron los `.png`, no los `.svg`.** El skill prefiere inlinear SVG como vector, pero Polish ya había reescrito las refs de `final.md` a `.png` por la regla Keynote-safe, y `image_coverage` compara literal. Se filló con `.png` para que el audit pase; los PNG son rasterizaciones a 2x y se ven nítidos proyectados.
- **Bug encontrado en `strip_feedback.py`:** en los bloques de feedback a nivel párrafo (`**Presenter feedback:**`) elimina la etiqueta y el bullet `[closed]` pero deja huérfana la línea de continuación `  Resolution: …`. Quedaron 3 sueltas en `final.md` (secciones 2, 4 y 5), visibles como texto en el cuerpo. Se removieron a mano antes del render. **Si se re-corre Polish, revisar esto de nuevo.**
- Key inputs: `final.md`; `config/pptx-styles/slide-templates.md` (catálogo de clasificación); `schemas/slide-model.md` (contrato de campos); `config/logo.png` (portada); Playwright + Chromium para las capturas de verificación.
- Files created/modified: `talks/claude-desktop-chat/output/html/index.html`, `talks/claude-desktop-chat/output/slide-model.json`, `talks/claude-desktop-chat/final.md` (3 líneas huérfanas removidas), `talks/claude-desktop-chat/memory.md`.
- Verificación: los tres audits del modelo pasan (`degenerate_enum`, `field_coverage`, `image_coverage`); 33 secciones Reveal; 26 paneles de notas del orador; 0 referencias externas a `images/`; portada con logo IAE, título, clase, autores y fecha; se revisaron 20 láminas renderizadas en captura.
- Pending open questions:
  - Duración: 65 min sobre 25 slides contra un bloque de 60. Sigue sin resolver y es lo único que bloquea.
  - Step 8 (Learnings) sin correr.
  - Los dos asides `generate-image` de 1.1 y 1.2, pendientes por segunda vez.
  - Los cinco directorios MCP de 4.8, sin verificar online.
  - El bug de `strip_feedback.py` con los bloques de feedback a nivel párrafo.

---

## 2026-08-01 — Re-Polish + Re-Render con el plugin 0.74.1 (sin tocar contenido)

- Status: complete
- Encargo del presentador: repulir y re-rendir con el plugin nuevo **sin tocar el contenido**, y **verificar que todos los bugs conocidos quedaran procesados**.
- **Polish: 0 diagramas re-renderizados.** Los 12 bloques ASCII se reusaron por digest — el ASCII no cambio desde que se dibujaron. Los 12 sidecars `.ascii` se habian perdido de `images/` y quedaron **regenerados y guardados**, asi que el proximo Polish vuelve a tener la fuente en disco.
- **`final.md`: 18 refs — 12 diagramas en `.svg` + 6 capturas en `.png`.** Antes las 18 eran `.png`. Es el cambio de mayor impacto visual: los diagramas ahora entran al HTML como **vector inline** y no como raster, asi que se leen nitidos proyectados a cualquier tamano.
- **`image-full` (0.73.0) aplicado a 3 laminas**, que antes eran `content-image` con media lamina vacia o con prosa de relleno: **1.6 «El chat en Claude Desktop»**, **3.2 «La busqueda en pantalla»** (el modelo viejo le habia fabricado un `fact` que solo repetia el alt-text) y **7.1 «La mision, parte 1»**. Las otras dos `content-image` (4.4 «El directorio de Connectors» y 6.2 «Donde vive el Schedule») **se quedan** porque tienen prosa propia.
- **`layout: image-left` en 2 laminas** donde el diagrama carga informacion que el texto ya no repite: 3.1 «La misma pregunta, dos modos de responder» y 6.3 «Donde corre? Local o nube». **`position: top` en 1**: la definicion de Schedule en 6.1, que es de la que dependen los dos items que siguen.
- **0.74.0:** 1.1 y 1.2 pasaron de `icon-list` a `concept-breakdown` + `format: list` — markup byte-identico, solo se moderniza la clasificacion.
- **Render: 33 laminas, 2,66 MB**, con `<!doctype html>`, `<html lang="es">`, `<head>` y `<body>` explicitos (arreglo de 0.74.1: antes era un fragmento suelto que el navegador levantaba en quirks mode y que cualquier preview que lo embebiera podia romper).
- **Los tres audits del modelo (`degenerate_enum`, `field_coverage`, `image_coverage`) en ok.**

### Verificacion de los bugs conocidos, uno por uno

| Bug | Estado |
|---|---|
| `strip_feedback.py` deja huerfanas las lineas `  Resolution: …` de los bloques a nivel parrafo | **REPRODUCIDO** (3 lineas, en las secciones 2, 4 y 5) y **limpiado**. **No esta arreglado en 0.74.1** — ver la causa exacta abajo. |
| Refs a `.png` en vez de `.svg` | **Resuelto.** 12 `.svg` + 6 `.png`, todas resuelven contra `images/`. |
| Laminas de captura con media lamina vacia | **Resuelto** con `image-full` en 3 laminas. |
| HTML sin doctype / `<head>` / `<body>` | **Resuelto** por 0.74.1. |
| Fences ASCII sin renderizar | **0.** |
| Campos `Presenter feedback` en `final.md` | **0** (25 H3 + 9 de parrafo strippeados). |
| Linea en blanco antes de cada `---` | **ok** (el unico match es el cierre del frontmatter, falso positivo). |
| Refs de imagen rotas | **0** sobre 18. |

### Bug del plugin, sin arreglar — causa exacta

`skills/feedback-cycle/strip_feedback.py`, la rama `_PARA_FEEDBACK` (aprox. lineas 89-110): el barrido avanza mientras la linea sea bullet o blanco y **corta en la primera linea que no es ninguna de las dos**. Una resolucion que envuelve en una **linea de continuacion indentada** (`  Resolution: …`, indentada pero sin `-` adelante) no matchea `_BULLET`, asi que el bucle corta ahi y la continuacion sobrevive. La rama H3 no tiene el problema porque corta por heading. **Arreglo sugerido:** seguir consumiendo mientras `_indent(lines[j]) > 0` y la linea no sea heading ni `---`, no solo mientras sea bullet.

- Files created/modified: `final.md`, `output/slide-model.json`, `output/html/index.html`, `images/` (12 sidecars `.ascii` nuevos), `memory.md`. **`draft.md` no se toco.**
- Pending open questions:
  - **Duracion: 65 min contra 60.** Sin resolver.
  - **Las 3 directivas `generate-image`** siguen sin cumplir, por tercera vez: la sesion no expone generacion de imagenes. Las laminas conservan su texto y el render no se rompe.
  - Los cinco directorios MCP de la lamina 4.8, sin verificar online.
  - El bug de `strip_feedback.py` de arriba, para llevar al plugin.
  - Step 8 (Learnings) sin correr.

### Re-render `html-strict` — 2026-08-04
- Status: complete
- Asks log:
  - 2026-08-04 — "Regenera chat" → Interpretado como esta Talk (`claude-desktop-chat`); se re-renderizó el deck `html-strict`.
- What was decided: `final.md` no cambió desde el último FILL, así que el modelo pasó el control de frescura y se re-ejecutó sólo el render. Se corrigió en el modelo un valor de formato retirado (`format: list` en 'El problema: horas que se van en trabajo manual' y 'Cómo lo vamos a atacar'), que el renderer venía degradando a `grid` con aviso; ahora queda explícito.
- Files created/modified: `talks/claude-desktop-chat/output/html/index.html`; `talks/claude-desktop-chat/output/slide-model.json`.
- Validation: 32 diapositivas; 10 imágenes raster, 94 gráficos vectoriales inline, 26 paneles de notas; 0 enumeraciones degeneradas, 0 campos ignorados, 0 imágenes omitidas; 0 avisos en el render final.
- Nota de entorno: el render corrió en el contenedor de sesión y el `index.html` se escribió de vuelta en el disco del presentador.
- Pending open questions: sigue abierta la duración (65 min contra un bloque de 60) y el paso 8 (Learnings), sin correr.
