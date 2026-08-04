# memory.md — introduccion

**Current step:** 7 — Render awaiting_presenter_review
**Awaiting:** 2026-08-03 — "Revisar el HTML regenerado con el nuevo modelo semántico y marcar ajustes visuales por diapositiva."
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
