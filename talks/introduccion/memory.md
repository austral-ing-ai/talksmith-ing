# memory.md — introduccion

**Current step:** 8 — Learnings awaiting_presenter
**Awaiting:** 2026-08-05 — "Confirmar las cuatro preguntas de la diapositiva de Slido contra el evento real, y decidir la promoción a la biblioteca compartida. Sigue pendiente la cifra del cuello blanco en la diapositiva 10."
**Topic:** Introducción, normas de trabajo y encuadre inicial de la materia.
**Folder:** talks/introduccion/
**Started:** 2026-08-03

---

## Talk briefing

La primera presentacion va a ser introducion, normas de trabajo, etc.

---

## 2026-08-03 — Step 1 (Frame)
- Status: complete
- Asks log:
  - 2026-08-03 — "¿De qué trata esta primera presentación? Contame todo lo que te parezca relevante: contenido, objetivo y cualquier idea que ya tengas." → "La primera presentacion va a ser introducion, normas de trabajo, etc."
  - 2026-08-03 — "Para esta presentación propongo estas carpetas: introduccion-a-la-materia / bienvenida-y-normas-de-trabajo / clase-inaugural. ¿Cuál preferís?" → "introduccion"
- What was decided: Presentación inaugural sobre la introducción a la materia y las normas de trabajo, en la carpeta `introduccion`.
- Key inputs: "La primera presentacion va a ser introducion, normas de trabajo, etc."
- Files created/modified: talks/introduccion/memory.md; talks/introduccion/research/{articles,llm-chats,web,corpus}/; talks/introduccion/images/; talks/introduccion/output/
- Pending open questions: none

## 2026-08-03 — Step 2 (Collect)
- Status: complete
- Asks log:
  - 2026-08-03 19:40 — "Elegí cómo querés aportar material para la presentación y avisame cuando hayas terminado." → "Usaremos un PPTX de IA para Biomedicina como referencia estructural, adaptándolo para Ingeniería de Software."
  - 2026-08-03 19:40 — "Subí el archivo PPTX de referencia a research/articles/ y avisame cuando esté listo para procesar." → "Listo. Trabajemos en esto. No perdamos contenido ahora, busquemos traducir esto a Ingeneria."
- What was decided: Usar el PPTX de IA para Biomedicina como referencia estructural, preservando sus secciones y diapositivas para adaptarlo a Ingeniería de Software.
- Key inputs: Clase-1-AI-for-BIO-Fundamento.pptx
- Files created/modified: talks/introduccion/research/articles/Clase-1-AI-for-BIO-Fundamento.pptx
- Pending open questions: none

## 2026-08-03 — Step 3 (Corpus)
- Status: complete
- Asks log:
  - 2026-08-03 19:40 — "¿Querés que procese ahora las 186 imágenes extraídas, continúe solo con el texto o lo dejemos para más adelante?" → "Sí, procesarlas ahora."
- What was decided: El PPTX de referencia se incorporó íntegramente como corpus estructural para una adaptación 1:1 hacia Ingeniería de Software.
- Key inputs: Clase-1-AI-for-BIO-Fundamento.pptx; 45 diapositivas; 186 recursos visuales extraídos y catalogados.
- Files created/modified: talks/introduccion/research/corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md; talks/introduccion/research/corpus/Clase-1-AI-for-BIO-Fundamento.pptx/images/
- Pending open questions: none

## 2026-08-03 — Step 4 (Draft)
- Status: complete
- Asks log:
  - 2026-08-03 20:13 — "¿Cómo querés llamar a esta clase?" → "Inteligencia General Generativa: curso, reglas y fundamentos"
  - 2026-08-03 20:13 — "¿Cuándo se dicta esta clase?" → "Agosto de 2026"
  - 2026-08-03 20:13 — "¿Cómo querés encarar el borrador?" → "Copia exacta de la presentación original, ajustada a Ingeniería de Software y sin reducir el contenido."
  - 2026-08-03 20:13 — "Revisá el borrador completo y avisame qué cambios querés aplicar o si está listo para pasar a revisión final." → "pasalo a polish"
- What was decided: Mantener una adaptación 1:1, sin reducir contenido, de las 45 diapositivas del PPTX de IA para Biomedicina hacia Ingeniería de Software.
- Key inputs: Clase-1-AI-for-BIO-Fundamento.pptx; corpus estructural de 45 diapositivas y 186 recursos visuales.
- Files created/modified: talks/introduccion/draft.md
- Pending open questions: detalles definitivos de logística, evaluación y cronograma de la materia, si difieren de los placeholders conservados de la presentación de referencia.

## 2026-08-03 — Step 5 (Review)
- Status: complete
- Asks log:
  - 2026-08-03 20:23 — El presentador pidió pasar directamente a Polish.
- What was decided: No hubo una ronda adicional de comentarios; se preservó el texto completo del borrador para respetar la instrucción de no reducir contenido.
- Key inputs: talks/introduccion/draft.md
- Files created/modified: none
- Pending open questions: none

## 2026-08-03 — Step 5 (Review, revisión semántica)
- Status: revision_in_progress
- Asks log:
  - 2026-08-03 — "Anota en draft.html con los estilos que queremos. Estas más cerca del análisis del draft.md que en el polish que lo va a inferir." → Se interpretó `draft.html` como `draft.md`, la fuente de análisis que acepta directivas explícitas de plantilla y layout.
  - 2026-08-03 — "Revisa si el pptx tenía comments y extraelos. No lo perdamos." → El paquete no contiene comentarios de PowerPoint; se extrajeron por separado las notas del orador no vacías.
- What was decided: Anotar las 45 diapositivas de `draft.md` con una plantilla semántica explícita y, cuando corresponde, con `layout`. Los timelines de ambas historias quedaron fijados como `timeline`; los formatos con imágenes, figuras, columnas, comparaciones y separadores ya no quedan librados a la inferencia de Polish/FILL.
- Key inputs: `draft.md`; las 45 diapositivas renderizadas del PPTX original; catálogo de plantillas `html-strict`.
- Files created/modified: `talks/introduccion/draft.md`; `talks/introduccion/research/corpus/Clase-1-AI-for-BIO-Fundamento.pptx.comments.md`; `talks/introduccion/research/corpus/Clase-1-AI-for-BIO-Fundamento.pptx.speaker-notes.md`.
- Validation: 45 diapositivas H2 y 45 directivas `template`; 4 directivas `layout`; 0 comentarios legacy/modern en el PPTX; 16 diapositivas con notas del orador preservadas.
- Pending open questions: revisar visualmente la selección de estilos antes de trasladarla a `final.md` y regenerar `slide-model.json`/HTML. Las referencias visuales todavía deben reconectarse para que las plantillas con imágenes puedan llenarse correctamente.

## 2026-08-03 — Step 6 (Polish)
- Status: complete
- What was decided: Se creó `final.md` a partir de `draft.md`, manteniendo el borrador intacto. Se retiraron los 52 campos de feedback editorial vacíos para producir la versión de presentación.
- Key inputs: talks/introduccion/draft.md
- Files created/modified: talks/introduccion/final.md
- Validation: 45 diapositivas; 0 bloques ASCII; 0 directivas de imágenes generativas; 0 campos de Presenter feedback restantes.
- Pending open questions: ninguna.

### Regeneración posterior a la revisión semántica
- Status: complete
- What was decided: Regenerar `final.md` desde el `draft.md` anotado, conservar las 45 directivas de plantilla y conectar 11 recursos visuales del PPTX original en las diapositivas que requieren imágenes.
- Files created/modified: `talks/introduccion/final.md`; 11 recursos bajo `talks/introduccion/images/`.
- Validation: 45 diapositivas H2; 45 directivas `template`; 11 referencias visuales; 0 campos `Presenter feedback`; 0 diagramas ASCII o imágenes generativas pendientes.

## 2026-08-03 — Step 7 (Render)
- Status: revision_planning
- Asks log:
  - 2026-08-03 20:23 — "El acabado está listo. ¿Querés renderizar la presentación como deck HTML o saltear el renderizado por ahora?" → "string-hml" (interpretado como `html-strict`).
- What was decided: Renderizar como deck HTML estricto. Para mantener la copia exacta de 45 diapositivas, la portada sintetizada representa la diapositiva 1 y las diapositivas 2–45 conservan el orden del PPTX de referencia.
- Key inputs: talks/introduccion/final.md
- Files created/modified: talks/introduccion/output/slide-model.json; talks/introduccion/output/html/index.html
- Validation: 45 diapositivas HTML; el modelo coincide con `final.md`; sin campos de contenido ignorados ni recursos visuales omitidos.
- Feedback posterior al render:
  - 2026-08-03 — "¿Por qué no hay iconos en ningún lado? Sea ej. 6." → El modelo usó solo `content-text` (37) y `statement` (7); no activó ninguna plantilla con iconos.
  - 2026-08-03 — "Los títulos que no estén en upper case." → Se normalizaron 21 títulos completamente en mayúsculas en `draft.md`, `final.md` y el render HTML.
  - 2026-08-03 — "El formato de los slides originales frente a esto tiene mucha diferencia. Si falta soporte en los style, detalla los cambios y los vamos planificando." → Se inició un análisis de brechas entre el PPTX de referencia y `html-strict`.
  - 2026-08-03 — "Una Breve Historia (Parte 2) es un timeline y esto está soportado. Hay un gap muy grande claramente en el draft.html." → Confirmado: el catálogo exige `timeline` cuando hay dos o más etiquetas de fecha, pero el modelo emitió `content-text`. Se reordenó el plan para reconstruir primero todo el FILL semántico y evaluar estilos solamente después.
  - 2026-08-03 — Se volvió a Step 5 para anotar explícitamente los estilos en `draft.md`. `final.md`, `slide-model.json` y el HTML actual quedan intencionalmente desactualizados hasta completar la revisión semántica.
- Hallazgos de formato: el PPTX contiene 706 formas, 121 imágenes y 33 diapositivas con imágenes; `final.md` no referencia ninguna imagen. Parte de la brecha corresponde a una clasificación incompleta y parte a layouts/variantes que no existen en el catálogo HTML.
- Pending open questions: confirmar el inicio de la reconstrucción completa del modelo semántico de las 45 diapositivas antes de tocar el repertorio de estilos.

### Regeneración `html-strict` posterior a la revisión semántica
- Status: awaiting_presenter_review
- What was decided: Reconstruir el modelo desde `final.md`, preservando una salida de 45 diapositivas: portada sintetizada a partir de la diapositiva 1 y 44 diapositivas de contenido correspondientes a las diapositivas 2–45 del PPTX original.
- Files created/modified: `talks/introduccion/output/slide-model.json`; `talks/introduccion/output/html/index.html`.
- Validation: 45 diapositivas HTML; 3 timelines; 19 concept-breakdowns con iconos; 11 imágenes incluidas; modelo vigente respecto de `final.md`; sin enumeraciones degeneradas, campos ignorados ni imágenes omitidas.
- Visual review note: la revisión automatizada del archivo local confirmó estructura y cobertura; la captura directa del navegador quedó bloqueada por la política de URLs `file://`. Revisar especialmente las diapositivas densas 31, 43 y 44, que preservan cuatro columnas aunque el catálogo recomienda hasta tres.
- Pending open questions: ajustes visuales que surjan de la revisión del presentador.

### Revisión posterior del contenido
- 2026-08-03 — "Borra Fuente de referencia: el PPTX original usa ejemplos de impacto sectorial; esta versión los traslada a Ingeniería de Software." → Se eliminó de la diapositiva 8, se registró la resolución en `draft.md` y se regeneraron `final.md`, `slide-model.json` y el HTML.
- Validation: la frase no aparece en `final.md`, el modelo ni el HTML; la presentación conserva 45 diapositivas.

### Revisión posterior del estilo
- 2026-08-03 — La diapositiva de apertura de fundamentos necesitaba un estilo tipo quote o similar. Se eligió `statement`: el texto no es una cita atribuida, por lo que `quote` sería semánticamente incorrecto.
- What changed: título principal `Inteligencia General Generativa`; subtítulo `Clase 1: Fundamentos, modelos y ecosistema actual`.
- Validation: el HTML usa `data-kind="statement"` y conserva 45 diapositivas.

### Regeneración con formato editorial
- 2026-08-03 — Se actualizó Talksmith y se aplicó `<!-- format: editorial -->` sólo a las slides cuyos conceptos caben en una composición plana sin reducir contenido.
- What changed: diapositivas 12, 16, 24, 26, 27, 28 y 29 usan una grilla editorial sin tarjetas; las enumeraciones más densas conservan su formato anterior para evitar recortes o reducción de legibilidad.
- Validation: `final.md` no conserva campos de feedback; el modelo coincide con `final.md`; 44 slides de contenido más la portada sintetizada producen 45 slides HTML; 7 bloques editoriales; cobertura de campos e imágenes completa.

## 2026-08-03 — Step 8 (Learnings)
- Status: deferred_until_render_acceptance
- What was decided: No hay feedback acumulado ni candidatos de conformidad estricta que puedan promoverse como aprendizaje reutilizable.
- Key inputs: config/learnings.md; config/feedback-backlog.md; config/strict-learnings.md (ausentes, sin entradas).
- Files created/modified: none
- Pending open questions: decidir si se promueve esta presentación a la biblioteca de conocimiento compartida.

### Regeneración `html-strict` — 2026-08-04
- Status: complete
- Asks log:
  - 2026-08-04 — "Regeneremos introduccion html-strict" → Re-render solicitado explícitamente con estilo `html-strict`; no hizo falta preguntar el estilo.
- What was decided: Re-renderizar el deck desde el modelo vigente. `final.md` no cambió desde el último FILL (sha256 7acec772…), así que el modelo pasó el control de frescura y se re-ejecutó solo el paso mecánico de render.
- Key inputs: `talks/introduccion/final.md`; `talks/introduccion/output/slide-model.json`; 13 recursos en `images/`; `config/logo.png`.
- Files created/modified: `talks/introduccion/output/html/index.html`.
- Validation: frescura del modelo ok; 0 enumeraciones degeneradas; 0 campos ignorados por plantilla; 0 referencias de imagen omitidas. Salida: 52 diapositivas, 13 imágenes embebidas, 47 paneles de notas del orador, 145 iconos vectoriales, 76 iconos en caché. Render byte-idéntico al anterior (3.359.733 bytes) — confirma determinismo.
- Nota de entorno: el render corrió en el contenedor de sesión (los scripts del plugin no están montados en la carpeta local) y el `index.html` se escribió de vuelta en el disco del presentador.
- Pending open questions: ajustes visuales que surjan de la revisión del presentador — siguen abiertas las diapositivas densas 31, 43 y 44 (cuatro columnas donde el catálogo recomienda hasta tres).

## 2026-08-04 — Step 5 (Review) + re-render `html-strict`
- Status: complete
- Asks log:
  - 2026-08-04 — "Borrar 'Fuente de referencia: el PPTX original organiza estos riesgos a partir de la guía de la OMS…'" → Eliminada de la diapositiva 9 (Problemas actuales de la IA en software).
  - 2026-08-04 — "Borrar 'el PPTX original presenta' en todos lados" → Eliminada la referencia de la diapositiva 10 (El riesgo macroeconómico y la transición abrupta); única aparición de esa frase.
  - 2026-08-04 — "Conceptos clave el titulo es -> LLMs, Foundation Models y Multimodal" → Título reemplazado; se retiró el subtítulo que pasó a duplicarlo.
  - 2026-08-04 — "Lo mismo que '¿Por qué son relevantes los Foundation Models?'" → Título reemplazado por su subtítulo, "IA Tradicional vs. Foundation Models"; subtítulo retirado.
- What was decided: Se purgan del contenido visible las referencias editoriales al PPTX de origen, y dos diapositivas de la sección Modelos Fundacionales promueven su subtítulo a título. Las citas externas legítimas (McKinsey, Stanford HAI) se conservan.
- Key inputs: `draft.md`; `final.md`; `output/slide-model.json`.
- Files created/modified: `talks/introduccion/draft.md` (4 bullets `[closed]`); `talks/introduccion/final.md`; `talks/introduccion/output/slide-model.json`; `talks/introduccion/output/html/index.html`.
- Validation: modelo re-sellado contra `final.md` (c709216f…); 0 enumeraciones degeneradas; 0 campos ignorados; 0 imágenes omitidas. Salida: 52 diapositivas, 13 imágenes, 47 paneles de notas; 0 apariciones de "Fuente de referencia" y de los títulos viejos en el deck.
- Pending open questions:
  - Queda una mención visible al PPTX de origen en la diapositiva "Escala, datos y poder de cómputo": "La tabla conserva el orden de magnitud del PPTX original para explicar por qué muchos equipos consumen modelos existentes en vez de entrenarlos desde cero." No coincide con la frase pedida; decisión del presentador.
  - Diapositivas densas 31, 43 y 44 (cuatro columnas donde el catálogo recomienda hasta tres).

### Continuación de la ronda — 2026-08-04
- Asks log:
  - 2026-08-04 — "Deja el titulo 'Modelos de propósito general'… Y un pequeño highlight de cada uno." → Título acortado (la fecha queda en las notas del orador) y las siete descripciones genéricas reemplazadas por un rasgo diferenciador de ≤64 caracteres cada una.
  - 2026-08-04 — "Hay varios cards que tiene un numero. Ej: 46. Sería mejor usar el que numera como estilo." → Cuatro diapositivas pasaron de `concept-breakdown` a `process`: 'Cómo vamos a trabajar', 'Entregables de clase', 'Contenidos de la Materia' y 'Conclusiones Clave' (la 46, el ejemplo señalado). El ordinal ahora lo dibuja el estilo y se retiró del texto.
- What was decided: Los ordinales son cromo del renderer, no contenido — se aplicó la regla del catálogo de plantillas. La diapositiva de conclusiones queda como lista numerada de una columna, sin etiquetas artificiales.
- Validation: primer render avisó que el formato `editorial` con 7 conceptos no soporta cuerpos de 115 caracteres (~70 entran); se acortaron y el render volvió limpio. Salida final: 52 diapositivas, 13 imágenes, 47 paneles de notas, 0 apariciones de los títulos viejos ni de "Fuente de referencia".
- Riesgo abierto: los rasgos diferenciadores de los siete modelos son afirmaciones de posicionamiento (cerrado vs. pesos abiertos, costo, contexto), no especificaciones verificadas — la búsqueda web sobre versiones de agosto de 2026 sólo devolvió agregadores de baja calidad. Conviene que el presentador los valide antes de dictar la clase.

## 2026-08-04 — Step 5 (Review) — trabajo final y composición de equipos
- Status: complete
- Asks log:
  - 2026-08-04 — "En el Trabajo práctico final, agreguemos que lo vamos a mencionar a mitad de cuatrimestre. Confirmar si no estaba ya ahí." → Verificado: no estaba. Se agregó la línea a la diapositiva 15.
  - 2026-08-04 — "Los grupos tiene que ser 2 personas de sistemas + 2 datos." → Actualizadas las diapositivas 14 y 15 con la misma redacción.
- What was decided:
  - La consigna del trabajo final se anuncia en la diapositiva 15 con "La consigna completa se presenta a mitad de cuatrimestre.", dentro del bloque "Equipo y alcance". Se descartó abrir un cuarto bloque "Cuándo se presenta": la diapositiva usa `concept-breakdown` con `format: grid` y un cuarto concepto la empuja a cuatro columnas, el patrón que el catálogo desaconseja y que ya quedó registrado como riesgo abierto en las diapositivas densas 31, 43 y 44. El anuncio también pertenece al alcance, así que el bloque existente lo absorbe sin forzar la semántica.
  - La composición del equipo queda en una sola redacción para las dos diapositivas: "Se trabaja en equipos de cuatro personas: dos de Ingeniería en Sistemas y dos de Ciencia de Datos." La diapositiva 15 conserva intacta la línea siguiente sobre continuidad del equipo entre los trabajos prácticos y el final.
  - Corrección dentro de la misma ronda: el presentador confirmó los nombres de carrera y "Sistemas"/"Datos" pasaron a "Ingeniería en Sistemas"/"Ciencia de Datos" en el contenido de las dos diapositivas y en las dos `Resolution:`. La frase mide 98 caracteres, por debajo de las líneas más largas que ya cargaban esas diapositivas (110 en la 14, 113 en la 15), así que ninguna tarjeta necesitó una versión corta.
- Key inputs: feedback del presentador en el chat (no escrito en el archivo); `talks/introduccion/draft.md`.
- Files created/modified: `talks/introduccion/draft.md` (2 líneas de contenido modificadas, 1 línea de contenido agregada, 3 bullets `[closed]` con `Resolution:` en las diapositivas 14 y 15).
- Validation:
  - Antes de editar, "mitad" no aparecía ninguna vez en las 2344 líneas del draft. Confirmado el pedido del presentador de verificar que no estuviera.
  - Después de editar, la frase de composición aparece en las líneas 582 y 626 con texto byte a byte idéntico; sin discrepancia entre las diapositivas 14 y 15. Cero residuos de "dos de Sistemas" o "dos de Datos" en el draft.
  - La diapositiva 15 mantiene tres bloques de concepto: "Equipo y alcance", "Entregables" y "Evaluación".
  - Prosa nueva pasada por `desrobotizar`, incluidas las reglas propias del presentador: sin em-dashes, sin adverbios en -mente, sin adjetivos de relleno, registro impersonal como el resto del deck.
- Pending open questions:
  - `final.md`, `output/slide-model.json` y el HTML quedaron desactualizados respecto de `draft.md`. Hay que rehacer Step 6 (Polish) y Step 7 (Render) para que los cambios lleguen al deck.
  - Los tres bullets no se replicaron en `config/feedback-backlog.md`; la ronda anterior del 2026-08-04 tampoco lo hizo. Conviene decidir si se recupera el espejo antes de Step 8.
  - Sigue abierto: diapositivas densas 31, 43 y 44 (cuatro columnas donde el catálogo recomienda hasta tres).

## 2026-08-04 — Step 6 (Polish) + Step 7 (Render `html-strict`)
- Status: complete
- Asks log:
  - 2026-08-04 — "Rehacer Polish y Render para que los cambios de la ronda de Review lleguen al deck." → Ejecutados los dos pasos sobre `talks/introduccion/`.
- What was decided:
  - Polish quedó reducido a su mínimo: el Talk no tiene diagramas ASCII ni SVG (0 bloques con fence, 0 referencias `.svg`), así que no corrieron las etapas de `polish-ascii` ni de consolidación de imágenes. Tampoco había bullets `[open]` que rescatar, de modo que el paso se limitó a derivar `final.md` desde `draft.md` y quitar los campos `Presenter feedback`.
  - `final.md` se actualizó como edición quirúrgica de 3 líneas sobre el archivo existente en lugar de reescribirlo entero, y después se verificó que el resultado coincide con el derivado mecánico del draft sin los campos de feedback (`diff -B` limpio, sin diferencias fuera de líneas en blanco).
  - En el render solo se tocaron dos entradas de `output/slide-model.json`: la diapositiva 14 (`Entregables de clase`, plantilla `process`, paso "Equipo") y la 15 (`Trabajo final`, plantilla `concept-breakdown` con `format: grid`, tarjeta "Equipo y alcance").
- Key inputs: `talks/introduccion/draft.md` (76.325 bytes); `talks/introduccion/final.md`; `talks/introduccion/output/slide-model.json`; 13 recursos en `images/`; `config/logo.png`.
- Files created/modified: `talks/introduccion/final.md`; `talks/introduccion/output/slide-model.json`; `talks/introduccion/output/html/index.html`.
- Validation:
  - `final.md`: 71.031 bytes, sha256 `8e243a8d10fc…`, 0 apariciones de "Presenter feedback". Los tres cambios de la ronda de Review llegaron al archivo (líneas 536 y 573 con la composición del equipo, línea 579 con la consigna a mitad de cuatrimestre).
  - Modelo re-sellado contra `final.md`. Las tres auditorías previas al render en verde: `degenerate_enum` ok, `field_coverage` ok, `image_coverage` ok.
  - Render `build_html.py --talk talks/introduccion`: 52 diapositivas, 13 imágenes embebidas, `output/html/index.html` de 3.350.242 bytes.
  - Captura headless de las dos diapositivas afectadas: ambas renderizan completas y sin desborde (`scrollHeight == clientHeight` en la tarjeta más densa).
- Riesgo estético anotado: la tarjeta "Equipo y alcance" de la diapositiva 15 quedó en 302 caracteres, contra 176 y 100 de sus dos hermanas en la misma grilla de tres. Entra sin recorte, pero si más adelante se le suma texto conviene revisar el balance o partir el concepto.
- Notas de entorno:
  - El render corrió en el contenedor de sesión (los scripts del plugin no están montados en la carpeta local) y `final.md`, `slide-model.json` e `index.html` se escribieron de vuelta al disco del presentador.
  - El montaje de staging del contenedor devolvió una copia desactualizada de `draft.md` (la versión previa a la ronda de Review, mismo path, 75.205 bytes) aunque el archivo en disco ya pesaba 76.325. Se resolvió trabajando directo sobre la carpeta montada y copiando a un nombre nuevo para forzar un staging fresco. Para futuras rondas: no confiar en un re-staging del mismo path dentro de la misma sesión.
  - Quedaron dos archivos temporales de sincronización en `talks/introduccion/_to_delete/`: `final.sync.md` y `slide-model.sync.json`. Los borra el presentador cuando quiera.
- Pending open questions (siguen abiertas):
  - Diapositivas densas 31, 43 y 44 (cuatro columnas donde el catálogo recomienda hasta tres).
  - Los rasgos diferenciadores de los siete modelos de propósito general son afirmaciones de posicionamiento sin verificar contra fuentes.
  - Queda una mención al PPTX de origen en la diapositiva "Escala, datos y poder de cómputo".
  - Los bullets de feedback de las rondas del 2026-08-04 no están espejados en `config/feedback-backlog.md`. Hay que decidirlo antes de Step 8.


## 2026-08-05 — Step 5 (Review) — ronda de 10 comentarios
- Status: complete
- Asks log:
  - 2026-08-05 — "Volvamos a la presentacion de introduccion a draft." → Resume del Talk `introduccion` en Step 5.
  - 2026-08-05 — "Aplica los comentarios." → Se aplicaron los 10 bullets abiertos que el presentador había escrito en `draft.md`.
- What was decided:
  - Diapositiva 2: el cuerpo pasó a las dos preguntas de apertura ("¿Por qué eligieron esta materia?" / "¿Qué esperan llevarse de la cursada?"). Se retiró la línea "Inteligencia General Generativa", que repetía el título del curso. La imagen de bienvenida se conserva.
  - Diapositiva 4: las tres fotos de docentes se redimensionaron a 500 px de alto conservando el aspect ratio (paulo 810x674 -> 601x500; marco 1154x1154 -> 500x500; claudio 300x300 -> 500x500). Claudio es el único que se amplía; el original de 300 px es la mejor copia disponible. Los archivos previos están en el historial de git.
  - Diapositiva 5: el concepto "El futuro ya está disponible" pasó a "Impacto en todas las ciencias", con dos ejemplos concretos (ingeniero químico, contador) y un cierre sobre qué aporta el ingeniero de software.
  - Diapositiva 6: se repuso el enlace de McKinsey. Salió de los hipervínculos del propio PPTX de referencia (`ppt/slides/_rels/slide6.xml.rels`), no de una búsqueda web.
  - Diapositiva 8: se agregó un quinto concepto, "Redefinición de roles y responsabilidades". La grilla pasa de 4 a 5 tarjetas.
  - Diapositiva 9: título "Problemas actuales de la IA en software" -> "Limitaciones de la IA Generativa".
  - Diapositiva 10: el PPTX no tiene hipervínculo en esa diapositiva, pero sí una línea de fuente en el texto ("Citrini Research - The 2028 Global Intelligence Crisis"); se repuso con el enlace https://www.citriniresearch.com/p/2028gic. La verificación mostró que el contenido SÍ se había cambiado respecto del original, así que se restauraron el título ("El riesgo macroeconómico y el colapso del consumo"), "La crisis global de inteligencia 2028", el PIB fantasma, el 50%/70% del cuello blanco y la cadena de la espiral deflacionaria. La pregunta de debate y la entrada sugerida del PPTX se movieron a las notas del orador.
  - Diapositivas 13 y 15: el estilo pedido ("bullets numerados") es `process` con pasos planos, que el catálogo renderiza como lista numerada de una sola columna con chip de número. La 13 pasó de 4 tarjetas con etiqueta a 7 líneas cortas; la 15 pasó de `concept-breakdown` + `format: grid` a `process`, con la lead intacta y 8 pasos planos. Se retiraron las etiquetas de agrupación (Equipo y alcance / Entregables / Evaluación) porque una lista numerada no las admite.
  - Diapositiva "Evaluación": la línea Importante ya estaba última en el contenido; el render la subía porque el FILL la clasificó como `important` en `position: top`. Corresponde `position: bottom` en `output/slide-model.json`. Todavía no se aplicó: el modelo se re-sella en Step 7.
- Key inputs: `talks/introduccion/draft.md`; `research/articles/Clase-1-AI-for-BIO-Fundamento.pptx` (hipervínculos y texto de las diapositivas 6 y 10); catálogo `config/pptx-styles/slide-templates.md`.
- Files created/modified: `talks/introduccion/draft.md` (10 bullets `[closed]` con `Resolution:`); `config/feedback-backlog.md` (10 filas nuevas + 12 filas retroactivas); `talks/introduccion/images/docente-{paulo-veiga,marco-sorondo,claudio-righetti}.*`.
- Validation:
  - 47 diapositivas H2 antes y después; 47 directivas `template`. Cero bullets abiertos al cerrar la ronda.
  - `find-closed-unmirrored` en verde: se espejaron también los 12 bullets `[closed]` de las rondas del 2026-08-04 que habían quedado sin fila en el backlog. Esa pregunta abierta queda cerrada antes de Step 8.
  - Prosa nueva escrita bajo `desrobotizar`, incluidas las reglas propias (registro impersonal en slides, sin em-dash, sin adverbios en -mente, sin hendidas de revelación).
- Nota de concurrencia: el presentador editó `draft.md` durante la ronda (timeline de "Una Breve Historia" reestructurado por año y 3 bullets nuevos). Se resolvió con un merge a tres bandas (`git merge-file`) contra el snapshot base, sin conflictos: los cambios del presentador viven arriba de la línea 840 y los de esta ronda por debajo de la 750. Regla para próximas rondas: snapshot antes de editar y merge antes de escribir, nunca sobrescribir el archivo del presentador.
- Pending open questions:
  - Tres comentarios nuevos sin aplicar, llegados durante esta ronda: (1) "Buscar que otro slide formay podriamos usar. Son dos conceptos que se enotrodice."; (2) "De la teoría a la intuición es realmente un lead title"; (3) "Mejorar y expander los presenter notes con mas detalles."
  - `final.md`, `output/slide-model.json` y el HTML quedaron desactualizados respecto de `draft.md`. Falta rehacer Step 6 (Polish) y Step 7 (Render).
  - Al re-sellar el modelo en Step 7: la diapositiva "Evaluación" necesita `position: bottom` en su highlight, y la 8 pasa a 5 tarjetas (verificar que no caiga en 4 columnas).
  - Siguen abiertas: diapositivas densas 31, 43 y 44; los rasgos de los siete modelos de propósito general sin verificar; la mención al PPTX de origen en "Escala, datos y poder de cómputo".


## 2026-08-05 — Step 5 (Review) — segunda ronda, 4 comentarios
- Status: complete
- Asks log:
  - 2026-08-05 — "Applica los nuevos cambios y vamos a seguir iterando." → Se aplicaron los 4 bullets que el presentador había escrito durante la ronda anterior.
- What was decided:
  - Diapositiva "2. ¿Qué es la Inteligencia Artificial?": pasó de `single-point` a `concept-columns`. La diapositiva introduce dos conceptos (Intuición / Un poco más formal) y el catálogo asigna `concept-columns` a 2-4 términos explicados en paralelo, cada columna autónoma y sin estructura de filas compartida. `single-point` exige exactamente un ítem etiquetado, así que la clasificación anterior estaba mal. Se corrigieron "Intuicion" -> "Intuición" y "Un Poco mas Formal" -> "Un poco más formal".
  - "De la teoría a la intuición" queda como lead, arriba de las columnas. La atribución a Russell & Norvig pasó de una línea con em-dash dentro del cuerpo a una línea de fuente al pie.
  - Diapositiva "3. Una Breve Historia (Parte 1)", entrada 1997: se reemplazó el cuerpo por el resumen que escribió el presentador (3½-2½, primer match completo ganado al campeón mundial, 200M de posiciones por segundo, sin aprendizaje). El texto anterior decía "primera victoria de la IA sobre el mejor humano", impreciso: Deep Blue ya había ganado una partida suelta en 1996 y Kasparov ganó ese match 4-2.
  - Mismas diapositiva, notas del orador: se reorganizaron por hito y se ampliaron de ~1.900 a ~7.400 caracteres. Se conservó todo el material previo, incluido el que estaba suelto y sin formato (máquina universal de Turing, problema de la parada, juego de la imitación, definición de sistema experto, la línea "Deap blue - IA = búsqueda + poder de cómputo + heurísticas"). Se sumaron 1936 y 1969 como hitos de contexto, fechas y publicaciones (Mind 1950, Nature 1986, Bell System Technical Journal 1948), los sistemas expertos concretos (MYCIN, DENDRAL, XCON) y ganchos de discusión para la clase.
  - Limpieza dentro de la misma diapositiva: la entrada de 1950 tenía "Test de turing ?" pegado al final del cuerpo, una nota al margen del presentador que se estaba proyectando. El cuerpo ahora explica el juego de la imitación y la pregunta quedó desarrollada en las notas.
- Key inputs: `talks/introduccion/draft.md`; catálogo `config/pptx-styles/slide-templates.md` (familia "Aligned columns" y ficha `concept-columns`).
- Files created/modified: `talks/introduccion/draft.md` (4 bullets `[closed]`); `config/feedback-backlog.md` (4 filas nuevas).
- Validation: 47 diapositivas H2 y 47 directivas `template` antes y después; 0 bullets abiertos; `find-closed-unmirrored` en verde. `draft.md` pasó de 80.223 a 85.960 bytes, casi todo en notas del orador.
- Pending open questions:
  - Verificar en el render que `concept-columns` con dos columnas entra sin recorte, y decidir si una de las dos lleva `emphasis`.
  - `final.md`, `output/slide-model.json` y el HTML siguen desactualizados. Falta Step 6 (Polish) y Step 7 (Render).
  - Al re-sellar el modelo: "Evaluación" necesita `position: bottom` en su highlight; la diapositiva 8 pasó a 5 tarjetas.
  - Siguen abiertas: diapositivas densas 31, 43 y 44; los rasgos de los siete modelos de propósito general sin verificar; la mención al PPTX de origen en "Escala, datos y poder de cómputo".


## 2026-08-05 — Step 5 (Review) — tercera ronda + ingesta de fuentes
- Status: complete
- Asks log:
  - 2026-08-05 — "Procesa mas cambios." → Se aplicaron los 3 bullets nuevos de la diapositiva "5. Una Breve Historia (Parte 2)".
  - 2026-08-05 — "Asegurate que todos los links que referencia esten ingestados." → Auditoría de las 12 URLs de `draft.md` más 3 arXiv citados por ID sin URL.
- What was decided:
  - Nueva diapositiva 6, "Move 37", después de la Breve Historia (Parte 2). El video que pidió el presentador es "Move 37!! Lee Sedol vs AlphaGo Match 2", del canal Daniel Estrada. Plantilla `single-point`: prosa de contexto más un punto emfatizado, con el enlace al video al pie. La diapositiva cierra con la frase que el presentador pidió como summary, sobre el conocimiento estratégico que generó el self-play. La frase se puso acá y no en la Parte 2 porque es el remate del argumento de esta diapositiva; se mueve si el presentador prefiere.
  - Notas del orador de la Parte 2: reorganizadas por hito y ampliadas de ~1.000 a ~5.900 caracteres, conservando todo el material previo sobre AlexNet y Transformers. Se sumaron los números de Watson (2.880 núcleos POWER7, 16 TB, el error "Toronto"), los de AlexNet (15,3% vs 26,2% de error top-5, dos GTX 580), la arquitectura de AlphaGo (red de política + red de valor + MCTS) y tres reparos de precisión: AlphaGo sí entrenó con partidas humanas (fue AlphaGo Zero el que no), el costo cuadrático de la atención, y que los 100 millones de usuarios de ChatGPT son una estimación de UBS cuyo récord Threads le quitó en julio de 2023.
  - Ingesta: de las 15 fuentes referenciadas, 2 ya estaban en el corpus. Se capturaron 11 nuevas con `talksmith:ingest` y el rol Librarian construyó un registro por cada una. Dos no se pudieron traer: McKinsey (timeout de lectura, dos intentos) y `platform.openai.com/docs/api-reference/models/object` (HTTP 403). Las carpetas parciales se borraron; no quedaron restos.
- Key inputs: `draft.md`; endpoint oEmbed público de YouTube para identificar el video; catálogo de plantillas.
- Files created/modified: `talks/introduccion/draft.md` (48 diapositivas, 3 bullets `[closed]`, 4 entradas nuevas en Open questions); `config/feedback-backlog.md` (3 filas); `research/web/` (11 carpetas nuevas); `research/corpus/` (11 registros nuevos + carpetas companion con 37 imágenes).
- Validation: 48 diapositivas H2 y 48 directivas `template`; 0 bullets abiertos; `find-closed-unmirrored` en verde. Las 2 capturas previas (`arxiv-2604-24827-ikp`, `linkedin-gpt-5-5-parameter-estimate`) sobrevivieron intactas al desempaquetado.
- Hallazgos de la ingesta que afectan contenido ya escrito:
  - **Citrini Research es ficción especulativa declarada.** Abre con "What follows is a scenario, not a prediction", se publicó el 22 de febrero de 2026 y está escrito como un memo fechado en junio de 2028. La diapositiva 10 lo cita. Además la cifra del cuello blanco no coincide: la fuente dice 50% del empleo y **75%** del gasto discrecional; la diapositiva proyecta 70%. Queda en Open questions, sin tocar el contenido, porque el presentador había pedido fidelidad al PPTX original.
  - `anthropic-docs-welcome`: la captura trae nomenclatura de modelos inusual y menciona un modelo sin clasificadores de seguridad. Sin verificar y sin uso en ninguna diapositiva. Registrado como no citable hasta confirmarlo con otra fuente.
  - `meta-llama-4`: la página tiene 16 meses, compara contra modelos ya superados y no publica números. No sirve como referencia de estado del arte.
  - `alibaba-qwen-doc`: el benchmark que destaca es interno y circular (compara contra un kernel de la propia Alibaba).
  - Los tres arXiv capturaron solo la página de abstract, sin figuras. Si hace falta el diagrama del Transformer o las curvas de Kaplan, hay que traer los PDFs aparte.
  - 14 de las 37 imágenes copiadas quedaron con `<!-- pending: process_images -->`: 10 gráficos de Citrini, 3 de Moonshot y la cabecera de Meta. Correr la Fase 2 del Librarian si se van a usar.
- Nota de transferencia: 118 archivos nuevos se pasaron al disco del presentador como un solo `.tgz` (14 MB) desempaquetado con `device_bash`, en lugar de 118 entregas individuales. Sirve como patrón para futuras ingestas grandes.
- Pending open questions:
  - Decidir qué hacer con la cifra y el encuadre de la diapositiva 10.
  - "Codificar a entrenar" en la diapositiva de AlexNet parece una frase truncada. Definir redacción.
  - `final.md`, `output/slide-model.json` y el HTML siguen desactualizados. Falta Step 6 y Step 7, ahora con 48 diapositivas en vez de 47.
  - Al re-sellar el modelo: "Evaluación" necesita `position: bottom`; la diapositiva 8 pasó a 5 tarjetas; verificar `concept-columns` a dos columnas en "¿Qué es la Inteligencia Artificial?".
  - Siguen abiertas: diapositivas densas 31, 43 y 44; los rasgos de los siete modelos de propósito general sin verificar; la mención al PPTX de origen en "Escala, datos y poder de cómputo".


## 2026-08-05 — Step 5.5 (vista HTML en vivo)
- Status: complete
- Asks log:
  - 2026-08-05 — "Guarda el research." → Los archivos ya estaban en disco. El commit lo hizo el presentador desde su máquina (`9f783a6 WIP`, 371 archivos de research incluidos).
  - 2026-08-05 — "Genera un preview en html para poder ver como estamos." → Render `html-strict --draft` desde `draft.md`.
- What was decided:
  - El FILL se hizo incremental, no desde cero: se partió del `slide-model.json` vigente (52 entradas, revisado en varias rondas) y se re-FILLearon solo las 4 secciones que cambiaron (Bienvenidos, ¿Por qué esta materia?, Logística, Fundamento de AI), en paralelo, una por agente. Las 5 secciones restantes se copiaron intactas. Resultado: 53 entradas.
  - `deck.title` y `deck.class` se alinearon con el frontmatter que editó el presentador: título "Inteligencia Artificial Generativa (AI Gen)" y clase "Clase 1: Bienvenidos / Introducción". Se limpió el doble espacio y se sacó "- Universidad Austral" del título, que ya vive en `institution`.
- Files created/modified: `talks/introduccion/output/slide-model.draft.json`; `talks/introduccion/output/html/index.html`.
- Validation: guard de frescura sellado contra `draft.md` (ca4c5a1f…, 95.163 bytes); render de 53 diapositivas; 0 errores de consola. Capturas headless de las 10 diapositivas que cambiaron, revisadas una por una.
- Verificación visual, diapositiva por diapositiva:
  - "Cómo vamos a trabajar" y "Trabajo final": la lista numerada de una columna sale como la pidió el presentador, chip de número más línea.
  - "Evaluación": la línea Importante quedó en la banda inferior.
  - "¿Qué es la Inteligencia Artificial?": las dos columnas entran cómodas, con la fuente al pie y el remate arriba de ella.
  - Timelines Parte 1 y Parte 2: el año como etiqueta funciona mucho mejor que la numeración anterior. La Parte 1 con siete entradas queda ajustada contra el borde inferior.
  - "Transformación en Ingeniería de Software": las 5 tarjetas caen en 3+2, no en 4 columnas.
  - "Move 37": entra completa. La etiqueta del punto y su cuerpo se renderizan en el mismo párrafo, así que se leen corridos.
- Pending open questions (nuevas de esta vuelta):
  - Timeline Parte 1: siete entradas rozan el borde inferior. Evaluar partir en dos o acortar descripciones.
  - "Move 37": la etiqueta en negrita y el cuerpo van pegados en un párrafo. Ver si conviene reformular la etiqueta o el arranque del cuerpo.


## 2026-08-05 — Step 6 (Polish)
- Status: complete
- Asks log:
  - 2026-08-05 — "Move a polish." → Ejecutado Step 6 completo sobre `talks/introduccion/`.
- What was decided: Polish quedó otra vez en su mínimo. El Talk no tiene diagramas ASCII (0 bloques) ni directivas `generate-image` (0), así que no corrieron las etapas de dibujo ni de revisión visual. Las nueve referencias de imagen ya apuntaban a `images/` y todas existen en disco, así que la consolidación no tuvo nada que copiar. No había bullets `[open]` que rescatar. El paso se redujo a derivar `final.md` desde `draft.md` y quitar los campos de trabajo.
- Key inputs: `talks/introduccion/draft.md` (95.163 bytes, sha256 ca4c5a1f091f…, sin cambios del presentador desde el preview).
- Files created/modified: `talks/introduccion/final.md` (84.270 bytes, era 71.043).
- Validation:
  - 48 diapositivas H2 y 48 directivas `template` en `final.md`, idénticas a `draft.md`; 9 secciones H1.
  - Strip: 48 campos H3 `### Presenter feedback` y 11 en forma de párrafo. Cero apariciones de "Presenter feedback", `[closed]` u `[open]` en `final.md`.
  - Cero bloques ASCII, cero referencias con extensión prohibida (.svg/.webp/.avif/.heic).
  - Las nueve referencias `images/...` resuelven a archivos existentes.
  - El guard de línea en blanco antes de cada `---` pasa: el único caso sin línea previa es el cierre del frontmatter YAML en la línea 10, que es correcto.
  - `# Open questions` y `# Cut material` sobreviven en `final.md`.
- Pending open questions: las mismas de la ronda anterior. `output/slide-model.json` y el HTML de `output/html/` corresponden al preview de `draft.md`; Step 7 tiene que re-FILLear contra `final.md`.


## 2026-08-05 — Step 7 (Render `html-strict`)
- Status: complete
- Asks log:
  - 2026-08-05 — "Render this Talk as which format?" → "html-strict".
- What was decided: el modelo no se re-FILLeó desde cero. `final.md` difiere de `draft.md` solo en los campos de trabajo, que el FILL ignora por contrato, así que se promovió `slide-model.draft.json` a `slide-model.json` y se re-selló contra `final.md`. Se verificó la equivalencia con un diff de contenido: la única diferencia es el párrafo de cuatro líneas sobre Deep Blue que el presentador había pegado debajo de un bullet de feedback, que el strip retiró como corresponde.
- Key inputs: `talks/introduccion/final.md` (84.270 bytes, sha256 ec9ca141aadf…); `slide-model.draft.json`; 13 recursos en `images/`; `config/logo.png`.
- Files created/modified: `talks/introduccion/output/slide-model.json`; `talks/introduccion/output/html/index.html`.
- Validation:
  - Guard de frescura sellado y verificado contra `final.md`.
  - Las tres auditorías en verde: `degenerate_enum` sin enumeraciones de un solo ítem, `field_coverage` con todos los campos poblados consumidos por su plantilla, `image_coverage` con todas las referencias de `final.md` presentes en el modelo.
  - Salida: 53 diapositivas más portada, 47 paneles de notas del orador, 10 imágenes, 57 enlaces activos. Cero errores de consola.
  - Chequeo de fugas sobre el texto renderizado: cero apariciones de "Presenter feedback", `[closed]`, `[open]` y "Resolution:".
  - Portada verificada por captura: título, institución, clase, autoría, fecha y logo de Austral en su lugar.
- Pending open questions: las de siempre, más las dos estéticas del preview (timeline Parte 1 ajustado contra el borde; etiqueta y cuerpo pegados en Move 37).


## 2026-08-05 — Step 5 → 6 → 7 (diapositiva de preguntas en vivo)
- Status: complete
- Asks log:
  - 2026-08-05 — "Agregar un slide con 4 que va ser conjunto de preguntas en vivo: https://app.sli.do/event/s7Ccr6C4awbUzRW1RpH19c" → Nueva diapositiva 5 al cierre de la sección Bienvenidos.
  - 2026-08-05 — "Grabar el documento en disco." → draft.md, final.md, modelo, deck y corpus escritos a la carpeta local.
- What was decided:
  - **Ubicación**: al final de la sección Bienvenidos, después de "Antes que nada…". Así no hubo que renumerar ninguna diapositiva existente, y el recorrido queda bienvenida → qué es esto → qué se llevan → quiénes somos → ahora hablan ustedes.
  - **Plantilla `process` con pasos planos**: la misma lista numerada de una columna que el presentador eligió para Logística. Cuatro preguntas numeradas, con la lead arriba y el enlace al evento en una banda `important` al pie, para que la URL se lea grande y sea clickeable.
  - **Las cuatro preguntas son propuesta editorial.** Las dos primeras reproducen las que ya abren la diapositiva 2. Las otras dos (uso actual de herramientas de IA, preocupación sobre el futuro profesional) las escribí yo. Slido no expone las preguntas configuradas en el evento, así que hay que confirmarlas contra el panel del presentador: si no coinciden, la diapositiva proyecta preguntas que la audiencia no encuentra al entrar.
  - Las notas del orador explican cuándo correrla, cómo proyectarla y cómo reutilizar las respuestas: la tercera pregunta calibra el ritmo de los módulos de prompts, la cuarta se retoma en la diapositiva de limitaciones y en la del riesgo macroeconómico.
- Key inputs: URL del evento de Slido.
- Files created/modified: `talks/introduccion/draft.md` (97.185 bytes, 49 diapositivas); `talks/introduccion/final.md` (85.816); `config/feedback-backlog.md` (1 fila); `research/web/slido-preguntas-en-vivo/`; `research/corpus/slido-preguntas-en-vivo.web.md`; `output/slide-model.json`; `output/html/index.html`.
- Validation:
  - Ingesta: Slido responde 200 pero es una app de una sola página, así que `page.md` se reescribió a mano y el registro de corpus deja constancia de que las preguntas del evento no se pueden capturar.
  - Polish: 49 campos H3 de feedback y 11 de sección retirados; 0 fugas de campos de trabajo en `final.md`.
  - Render: las tres auditorías en verde; 54 diapositivas; 48 paneles de notas; el enlace a Slido sale como `<a>` clickeable; 0 errores de consola.
  - Captura headless de la diapositiva nueva: las cuatro preguntas entran sin recorte y la banda del enlace queda al pie.
- Pending open questions:
  - **Confirmar las cuatro preguntas contra el evento de Slido antes de la clase**, y verificar que el enlace siga vivo.
  - La diapositiva 2 sigue abriendo con dos de las cuatro preguntas. Si la repetición molesta, se puede dejar la 2 solo como bienvenida.
  - Las de siempre: la cifra del cuello blanco en la diapositiva 10; el timeline Parte 1 ajustado contra el borde; etiqueta y cuerpo pegados en Move 37; "Codificar a entrenar" truncado.


## 2026-08-05 — Step 5 (Review) — recorte de logística y una negrita
- Status: complete
- Asks log:
  - 2026-08-05 — Borrar "La nota final combina los entregables con el proyecto final." → Diapositiva 13.
  - 2026-08-05 — Borrar "Las reglas y la ponderación se publican antes de la primera entrega." → Diapositiva 13.
  - 2026-08-05 — Borrar "La cátedra orienta el alcance, la evidencia y la forma de evaluar el resultado." → Diapositiva 15.
  - 2026-08-05 — Borrar "La evaluación considera el resultado y la capacidad de justificarlo con evidencia técnica." → Diapositiva 15.
  - 2026-08-05 — Marcar en negrita "sus posibilidades de éxito en un objetivo dado" → Diapositiva "¿Qué es la Inteligencia Artificial?".
- What was decided:
  - "Cómo vamos a trabajar" bajó de 7 a 5 pasos y "Trabajo final" de 8 a 6. Las cuatro líneas retiradas duplicaban lo que ya cubren la diapositiva "Evaluación" (40% entregables / 60% trabajo final) y la propia consigna. Las cuatro quedaron archivadas en `# Cut material` con su fecha y motivo, no se borraron en silencio.
  - La negrita se aplicó solo en el cuerpo de la columna "Un poco más formal". En las notas del orador la cita de Russell & Norvig queda corrida, sin marcas.
- Files created/modified: `talks/introduccion/draft.md`; `final.md`; `config/feedback-backlog.md` (5 filas); `output/slide-model.json`; `output/html/index.html`.
- Validation:
  - 49 diapositivas H2 y 49 directivas `template` antes y después; 0 bullets abiertos; `find-closed-unmirrored` en verde.
  - Modelo re-sellado; las tres auditorías en verde; render de 54 diapositivas sin errores de consola.
  - Chequeo sobre el texto renderizado: las cuatro líneas retiradas aparecen 0 veces en el deck. La negrita se verificó por captura.
- Pending open questions: sin cambios respecto de la ronda anterior.


## 2026-08-05 — Step 5 (Review) — reconstrucción de la Taxonomía de Problemas
- Status: complete
- Asks log:
  - 2026-08-05 — "Revisa que esta inconsistente que Predicción es el unico que tiene slide seperador. Hacelo para todos."
  - 2026-08-05 — "Revisar si '¿Qué tipos de problemas resuelve la IA?' lo copiaste en forma erroneal del pptx." → La diapositiva de resumen estaba **bien copiada**; el problema era el resto de la sección.
  - 2026-08-05 — El presentador eligió la opción 1: restaurar la sección completa.
- What was decided:
  - **Diagnóstico.** El PPTX dedica una diapositiva por familia (24 a 30). El borrador había comprimido seis de las siete en una sola cada una. La única que conservó la estructura del PPTX fue Predicción, partida en separadora + detalle, y de ahí venía la inconsistencia que marcó el presentador. La compresión había perdido los hitos con sus fechas y cifras, las sub-descripciones de cada problema típico, las listas de herramientas y las arquitecturas.
  - **Reconstrucción.** La sección pasó de 9 a 15 diapositivas: la de resumen (intacta, verificada contra la diapositiva 23) más siete pares de separadora `statement` y detalle `concept-breakdown`. Las de detalle se renumeraron 2 a 8 y se retitularon "Ejemplos de problemas de <familia>", siguiendo el patrón que ya tenía Predicción.
  - **Hitos restaurados con sus cifras:** AlexNet 2012 (error 10% menor que el segundo), ResNet 2015 (3,57% contra 5% humano), Word2Vec 2013 (Rey − Hombre + Mujer ≈ Reina), AlphaGo 2016 4-1 y AlphaZero 2017 en menos de 24 horas, DeepMind 2016 (40% menos de consumo en los data centers de Google), Deep Blue 1997 sin aprendizaje automático, ChatGPT noviembre de 2022.
  - **Adaptación a Ingeniería de Software** en los ejemplos de biomedicina y agro del PPTX (cultivos, enfermedades, cosecha, moléculas). Los hitos históricos quedaron intactos por ser hechos.
  - Dos diapositivas pasaron de `format: editorial` a `format: grid` porque el render avisó que los cuerpos no entraban: "Ejemplos de problemas de percepción" (164 caracteres contra ~100 de presupuesto) y "Ejemplos de problemas de búsqueda y planificación" (109). Con tarjetas entran completas y no hubo que recortar texto.
- Key inputs: texto verbatim de las diapositivas 23 a 30 del PPTX de referencia.
- Files created/modified: `draft.md`; `final.md`; `config/feedback-backlog.md`; `output/slide-model.json`; `output/html/index.html`.
- Validation: 55 diapositivas H2 y 55 directivas `template` en el markdown; el deck sale con 60 más portada; 54 paneles de notas; las tres auditorías en verde; cero avisos del render tras el cambio a `grid`; cero errores de consola. Captura de un par separadora + detalle revisada a ojo.
- Pending open questions:
  - El hito de Predicción quedó con la cifra del PPTX ("error un 10% menor que el segundo lugar"). El de la Breve Historia (Parte 1) usa 15,3% contra 26,2% de error top-5, que es la formulación precisa. Conviene unificar.
  - La sección ahora tiene 15 diapositivas de las 60 del deck. Vale revisar si entra en los 90 minutos o si parte de ella pasa a material de consulta.
  - Las de siempre: la cifra del cuello blanco en la diapositiva del riesgo macroeconómico; "Codificar a entrenar" truncado; timeline Parte 1 ajustado contra el borde; etiqueta y cuerpo pegados en Move 37.


## 2026-08-05 — Cierre de pendientes menores + escaneo de Step 8
- Status: complete
- Asks log:
  - 2026-08-05 — "Completa lo pendiente." → Se cerraron los cuatro retoques que no dependían de una decisión del presentador y se corrió el escaneo de Step 8.
- What was decided:
  - **"Codificar a entrenar"** (Breve Historia Parte 2, hito 2012) quedó redactado completo: "el ingeniero de visión ya no escribe los detectores a mano, los aprende la red".
  - **Hito de AlexNet unificado.** La diapositiva de Predicción usaba la formulación del PPTX ("error un 10% menor que el segundo lugar") y la Breve Historia las cifras precisas. Las dos usan ahora 15,3% de error top-5 contra 26,2% del segundo. Las notas de Predicción señalan que la cifra se repite en la otra diapositiva.
  - **Cuello blanco.** La cifra pasó de 70% a 75%, que es la que trae Citrini, y la línea abre con "En el escenario" para que se lea como parte del escenario hipotético y no como dato observado. Es la corrección mínima defendible: no inventa una fuente real ni borra el contenido que el presentador pidió preservar.
  - **Move 37.** La etiqueta del punto cierra con punto, así el render la separa del cuerpo en vez de encadenarlos en una sola oración.
  - **Timeline Parte 1:** revisado por captura. Siete entradas entran con margen inferior; queda denso pero no desborda. No se tocó.
- Files created/modified: `draft.md`; `final.md`; `config/feedback-backlog.md` (4 filas); `output/slide-model.json`; `output/html/index.html`.
- Validation: 60 diapositivas más portada; tres auditorías en verde; frescura verificada; cero errores de consola. Verificación sobre el `textContent` del deck renderizado (no `innerText`, que solo devuelve la diapositiva visible y había dado lecturas vacías): 0 apariciones de las cuatro líneas borradas en rondas anteriores, 0 de "Codificar a entrenar", 0 de la formulación vieja del hito, 0 de "70% del gasto", y 0 de cualquier campo de trabajo.
- **Escaneo de Step 8 (Learnings):** 45 filas en el backlog. Nueve etiquetas recurren tres veces o más, contra la lectura anterior de que ninguna llegaba al umbral: `template-selection` (9), `numbered-list` (6), `content-addition` (6), `slide-title` (5), `content-fidelity` (5), `remove-redundancy` (4), `remove-editorial-reference` (3), `new-slide` (3), `external-source` (3). `config/learnings.md` no existe todavía, así que una promoción lo crearía. La decisión de qué promover quedó en manos del presentador.
- Pending open questions (las que sí dependen del presentador):
  - Confirmar las cuatro preguntas de la diapositiva de Slido contra el evento real.
  - Decidir si las 15 diapositivas de la Taxonomía entran en los 90 minutos.
  - Elegir qué patrones del backlog se promueven a `config/learnings.md` y si el Talk se promueve a la biblioteca compartida.


## 2026-08-05 — Decisión: el tiempo no acota el contenido
- Status: complete
- Asks log:
  - 2026-08-05 — "Ignora el tiempo." → La duración deja de ser un criterio para recortar contenido en este Talk.
- What was decided:
  - Se retiró de `# Open questions` la línea que pedía decidir qué diapositivas mostrar dentro de los 90 minutos y cuáles dejar como material de consulta. La pregunta ya no aplica.
  - Las dos notas de ritmo de los timelines dejaron de recomendar qué saltear. Ahora solo señalan qué hitos dan más para desarrollar, sin presupuesto de minutos: Parte 1 marca 1950, 1958 y 1997; Parte 2 marca 2012, 2016, 2017 y 2026. De paso la de la Parte 2 pasó de decir seis entradas a ocho, que es lo que tiene desde que se sumaron 2025 y 2026.
  - El campo `duration: "90 minutos"` del frontmatter **no se tocó**: viene del perfil de la materia y describe la clase, no un límite editorial.
  - **Regla para futuras rondas de este Talk: no proponer recortes por duración.** La densidad se evalúa por legibilidad de cada diapositiva, no por cuántas entran en la clase.
- Files created/modified: `draft.md`; `final.md`; `output/slide-model.json`; `output/html/index.html`.
- Validation: 60 diapositivas; frescura verificada; render limpio.
- Pending open questions: quedan dos, las dos del presentador — confirmar las cuatro preguntas contra el evento de Slido, y elegir qué patrones del backlog se promueven a `config/learnings.md` (más la promoción del Talk a la biblioteca compartida).


## 2026-08-05 — Step 6 (Polish) — dos diagramas ASCII para Percepción y Representación
- Status: complete
- Asks log:
  - 2026-08-05 — "Para cada uno de los slides Representación/Percepción genera un ASCCI chart que explique el concepto. Idealmente, que tengan consistencia entre ellos."
- What was decided:
  - Los diagramas van en las **separadoras**, no en las diapositivas de detalle: la separadora carga la definición y ahí el esquema explica el concepto, mientras que las de detalle ya están llenas con seis tarjetas y tres highlights.
  - **Gramática compartida a propósito**: tres columnas rotuladas ENTRADA / MODELO / SALIDA, cajas del mismo ancho, la misma flecha y un pie por columna. Percepción va de señal cruda a estructura nombrada; Representación, de símbolos sueltos a un espacio de vectores. Proyectadas una después de la otra se leen como dos instancias del mismo esquema.
  - En la caja de SALIDA de Representación la distancia está dibujada: rey y reina cerca unidos por un tie rojo rotulado "cerca", banana lejos con tie gris rotulado "lejos". Esa distancia es el punto del diagrama.
  - Las dos diapositivas pasaron de `statement` a **`image-full`**: primero se probó `content-image`, pero el diagrama quedaba comprimido en media columna. Con `image-full` el esquema ocupa el ancho y el párrafo de expansión se movió a las notas del orador, que es donde el presentador lo narra.
- Files created/modified: `draft.md`; `final.md`; `config/feedback-backlog.md`; `output/slide-model.json`; `output/html/index.html`; `images/s5-2-1-percepcion-senal-a-simbolos.{ascii,svg,png}`; `images/s5-3-1-representacion-espacio-vectores.{ascii,svg,png}`.
- Validation:
  - `validate_svg` y `audit_aspect` en verde en los dos. Consistencia verificada estructuralmente por diff de los SVG: mismo viewBox, mismos tres paneles 220×152 en las mismas x, mismo marker de flecha, mismas baselines. Los dos PNG salen 1800×800.
  - Tres auditorías del render en verde; 60 diapositivas; cero errores de consola. Revisión visual de los dos PNG y de las dos diapositivas renderizadas.
- **Hallazgos del rol Diagram-Illustrator, que conviene arreglar en el plugin:**
  1. **Bug de `slide_id` en `polish_ascii.py`.** El regex `H2_SLIDE` solo matchea encabezados numerados (`## 3. Título`). Las separadoras sin número no incrementan el contador y **heredan el id y el título del slide numerado anterior**. Por eso los diagramas salieron con ids `s5-2-1` y `s5-3-1` en vez de los esperados, y hubo que corregir a mano los `slide_title` del plan antes de renderizar para que los SVG no se dibujaran con el título equivocado. Riesgo latente: si más adelante se agrega un bloque ASCII a `## 2.` o `## 3.` de esa sección, va a colisionar de nombre.
  2. **La crítica ciega no corrió.** Un subagente no puede despachar otro subagente en esta sesión, así que el `diagram-critic` quedó sin ejecutar y los bloques figuran `critique_unavailable` en `images/.critique/`. El rol no sustituyó la crítica por su propio juicio, que es lo correcto. La revisión visual la hice yo sobre los PNG.
  3. **`cairosvg` no estaba instalado** en el contenedor; el rol lo instaló por la vía documentada del skill. Si el contenedor se recrea hay que repetirlo.
- Pending open questions: sin cambios — confirmar las preguntas contra el evento de Slido, y decidir las promociones de Step 8.


## 2026-08-05 — Diagramas: la taxonomía completa + Modelos Fundacionales
- Status: complete
- Asks log:
  - 2026-08-05 — "Que otro slide podriamos agregar un diagrama?" → Se propuso un orden; el presentador eligió empezar por la taxonomía.
  - 2026-08-05 — "En vez de crear un nuevo slide, ponelo en el slide que introduce el tema. Ej: Predicción, que es el slide 30."
  - 2026-08-05 — "Primero hagamos consistencia en la taxonomia de problemas."
  - 2026-08-05 — "Propongo que cada vez que se presenta un tipo de 'problemas resuelve', confirmar que hay un slide que lo define y un ASCII chart en el mismo. Luego el slide de ejemplos." → Promovido a `config/learnings.md` como **L1**.
  - 2026-08-05 — "Me gusta agregar en ASCCI para LLMs, Foundation Models y Multimodal como sugeriste."
- What was decided:
  - **Las siete separadoras de la taxonomía tienen diagrama.** Se sumaron cinco a las dos que ya estaban: Predicción, Decisión Secuencial, Búsqueda / Planificación, Razonamiento Simbólico y Generación. Ninguna diapositiva nueva: el diagrama va en la que ya introducía cada familia.
  - **La forma del diagrama sigue al concepto, no al layout.** Predicción, Percepción, Representación y Generación usan la tubería de tres columnas ENTRADA / MODELO / SALIDA. Decisión Secuencial es un lazo cerrado agente ⇄ entorno con las flechas rotuladas en los dos sentidos. Búsqueda es un árbol de estados con el camino resaltado. Razonamiento es una cadena hechos → reglas → conclusión. La consistencia la sostienen el lienzo, los márgenes, la tipografía, el tratamiento de cajas y el acento rojo reservado a un solo elemento por diagrama.
  - **Modelos Fundacionales estrena diapositiva de definición** al inicio de la sección, con un diagrama de contención: LLM y MULTIMODAL dentro de la caja de FOUNDATION MODEL, y MODELO DE LENGUAJE al lado como linaje más viejo y más amplio. La sección no tenía apertura, así que crearla es lo que pide la regla L1; la de cuatro columnas quedó intacta como detalle. Si el presentador prefiere fusionarlas, se revierte en una edición.
  - **`config/learnings.md` creado**, con L1 (el par definición + diagrama, después ejemplos) y L2 (el diagrama va en la diapositiva que ya introduce el tema, no en una nueva). Es el primer archivo de aprendizajes del repositorio, así que aplica desde la próxima clase.
- Files created/modified: `draft.md`; `final.md`; `config/feedback-backlog.md`; **`config/learnings.md` (nuevo)**; `output/slide-model.json`; `output/html/index.html`; seis tríos `.ascii`/`.svg`/`.png` en `images/`.
- Validation: 56 diapositivas H2; deck de 61 más portada; las tres auditorías en verde; `validate_svg` y `audit_aspect` ok en los seis nuevos; cero fences ASCII y cero referencias `.svg` en `final.md`; cero errores de consola; cero fugas de campos de trabajo. Los seis PNG revisados a ojo uno por uno.
- Riesgo conocido: la **crítica visual ciega no corrió en ninguno** de los ocho diagramas. Un subagente no puede despachar otro en esta sesión, así que el `diagram-critic` quedó como `critique_unavailable` y la revisión la hice yo mirando los PNG. Queda anotado en `images/.critique/`.
- Bug del plugin confirmado dos veces: `polish_ascii.py` corre el `slide_title` un lugar cuando la sección tiene separadoras sin numerar, porque `H2_SLIDE` solo matchea encabezados numerados. El rol lo corrigió a mano antes de cada render. Vale arreglarlo en el plugin.
- Pending open questions: sin cambios.
