# memory.md — modelado-redes-neuronales

**Current step:** complete
**Topic:** Diseño y modelado de una red neuronal — entradas/salidas, matriz de confusión, overfitting y regularización L2
**Folder:** talks/modelado-redes-neuronales/
**Started:** 2026-08-18

---

## Talk briefing

quiero crear una nueva presentacion que va a cubrir aspectos del diseno y input, output de una red neuronal. Como se modela, red de confusion y overfitting y L2.

---

## 2026-08-18 — Step 1 (Frame)
- Status: in_progress
- Asks log:
  - 2026-08-18 — "¿Nueva presentación o retomar una existente?" → Nueva
  - 2026-08-18 — "¿Qué buscás con esta clase? + candidatos de nombre de carpeta" → Eligió carpeta `modelado-redes-neuronales` (opción 3); detalle de objetivos pendiente
  - 2026-08-18 — "Nombre de carpeta (kebab-case)" → modelado-redes-neuronales
- What was decided: Nueva presentación sobre diseño/modelado de una red neuronal (input/output, matriz de confusión, overfitting, L2). Carpeta `modelado-redes-neuronales`.
- Key inputs: Briefing verbatim (arriba). Profile completo (Español, 90 min, estudiantes de Ing. de Software).
- Files created/modified: talks/modelado-redes-neuronales/ (tree), memory.md
- Pending open questions: Objetivos finos de la clase sin detallar; nivel de la audiencia (intro vs. profundización) por confirmar en Step 4.

## 2026-08-18 — Step 2 (Collect)
- Status: complete
- Asks log:
  - 2026-08-18 — "¿Cómo querés traer material? (4 canales)" → Soltó 1 archivo en research/llm-chats/ y dijo "listo"
- What was decided: 1 fuente aportada (chat.md), avanzar a corpus.
- Key inputs: research/llm-chats/chat.md — guía de referencia "Modelado de inputs y outputs en redes neuronales" (~1070 líneas, sin imágenes).
- Files created/modified: research/llm-chats/chat.md (aportado por el presentador)
- Pending open questions: none

## 2026-08-18 — Step 3 (Corpus)
- Status: complete
- Asks log: none
- What was decided: 1 registro de corpus creado (chat-export), sin imágenes que procesar.
- Key inputs: chat.md → registro losless con las 13 secciones.
- Files created/modified: research/corpus/chat.md.md, research/corpus/chat.md/images/ (companion vacío)
- Pending open questions: **La fuente NO cubre matriz de confusión** (mencionada en el briefing) — gap a cubrir en Step 4 con conocimiento del agente o fuente extra.

## 2026-08-18 — Step 4 (Draft)
- Status: complete
- Asks log:
  - 2026-08-18 — "class, date, y modo de borrador (A/B/C)" → Modo B; class y date se defaultearon (class="Diseño de redes neuronales: del dato a la predicción", date="a definir") para no bloquear, ajustables en Review
- What was decided: Borrador completo end-to-end (Modo B) desde el corpus + conocimiento del área para la matriz de confusión. 6 secciones + Conclusiones, ~25 slides para 90 min. Revisión interna (Composer scope=full) aplicada: títulos de sección/slide dentro de presupuesto, slide 5.1 dividida (tenía tabla+diagrama), estilo anti-slop y sin em-dashes. Verificado contra learnings.md L1–L7 (respetados).
- Key inputs: corpus/chat.md.md (secciones 1,2,3,5,6 + conclusiones); conocimiento del área (sección 4, matriz de confusión — no en corpus).
- Files created/modified: draft.md
- Pending open questions: (1) Sección 4 sin fuente en corpus — sumar fuente propia si se quiere anclar números. (2) Duración: sección 2 cargada; candidatas a recorte 4.4 y 6.2. (3) class/date por confirmar.

## 2026-08-18 — Step 5 (Review)
- Status: complete
- Asks log:
  - 2026-08-18 — "Revisá draft.md y dejá bullets de feedback / avisá cuando esté listo" → "Hay introduccion a matriz de confusion cobierto?" (consulta, respondida: sí, sección 4; no viene del corpus) + "Listo, dalo por completo y generá la presentación"
- What was decided: Presentador aprobó el borrador sin bullets de feedback. draft.md congelado.
- Key inputs: ninguna edición; consulta sobre cobertura de matriz de confusión (sección 4, desde conocimiento del área).
- Files created/modified: ninguno (sin ronda de feedback)
- Pending open questions: none

## 2026-08-18 — Step 6 (Polish)
- Status: complete
- Asks log: none (paso automático)
- What was decided: cp draft.md → final.md; 5 diagramas ASCII dibujados a SVG y validados (viewBox ok); fences reemplazadas por refs de imagen; campos Presenter feedback quitados (33 bloques); sin [open] que rescatar. Dos pistas de plantilla corregidas en final.md (1.1 y 4.1). Sin cairosvg/PNG (no hace falta para HTML).
- Key inputs: final.md, 5 SVGs en images/.
- Files created/modified: final.md, images/s1-3-1-neurona.svg, images/s2-4-1-one-hot.svg, images/s4-2-1-matriz-confusion.svg, images/s5-2-1-curvas-overfitting.svg, images/s6-1-1-objetivo-l2.svg
- Pending open questions: none

## 2026-08-18 — Step 7 (Render)
- Status: complete
- Asks log:
  - 2026-08-18 — "Formato de render (pptx-strict / pptx-free-form / html-strict / skip)" → html-strict (único viable: Cowork no disponible para .pptx)
- What was decided: Deck HTML (html-strict, Reveal.js) renderizado. Toolchain: venv en scratchpad con jinja2/markupsafe; slide-model.json FILLeado a mano (30 slides + portada = 33 render); model_freshness stamp; build_html.py. Sin avisos tras corregir 2 slides editorial→grid. Los 5 SVGs quedaron inlineados. pptx NO disponible (sin Cowork).
- Key inputs: output/slide-model.json, output/html/index.html, index.html (raíz).
- Files created/modified: output/slide-model.json, output/html/index.html, /index.html (índice raíz)
- Pending open questions: pptx pendiente si en el futuro hay Cowork; entorno de render usa venv en scratchpad (jinja2).

## 2026-08-18 — Step 8 (Learnings)
- Status: complete
- Asks log:
  - 2026-08-18 — "Promover esta Talk a la biblioteca de conocimiento compartida" → omitido al cerrar por pedido del presentador.
- What was decided: Se volvió a Draft para procesar 6 observaciones; se cerraron y registraron en el backlog. Se reabrió el flujo completo, se rehízo final.md y se renderizó html-strict. La Talk queda cerrada sin promoción a biblioteca.
- Key inputs: Feedback del presentador sobre foco tabular, ejemplos, activaciones, eliminación de una slide y un quiz de precisión/recall. Se detectaron dos oportunidades de imagen atmosférica; quedaron como directivas porque esta sesión no tenía capacidad de generación disponible.
- Files created/modified: draft.md, final.md, images/ (diagrama de matriz actualizado y sidecars), output/slide-model.json, output/html/index.html, config/feedback-backlog.md, /index.html.
- Pending open questions: Las dos directivas de imagen se pueden generar al reabrir esta Talk en una sesión con capacidad de imágenes.

## 2026-08-18 — Step 7 (Render) — re-render html-strict
- Status: complete
- Asks log: none (pedido directo: "completa la generacion de strict html para modelado")
- What was decided: Re-render limpio de html-strict tras confirmar que slide-model.json seguía fresco (sha256 == final.md; freshness check [fresh]). 33 slides. Se eliminó SVG huérfano images/s4-2-1-matriz-confusion.svg (final.md ahora referencia s4-3-1). Dos íconos inferidos ('email', 'remove_red_eye') sin entrada en el set → fallback a 'info' (cosmético, por diseño del renderer).
- Key inputs: output/slide-model.json (fresco), final.md.
- Files created/modified: output/html/index.html, output/html/.render.json, /index.html (raíz); eliminado images/s4-2-1-matriz-confusion.svg.
- Pending open questions: los 2 íconos fallback quedan como 'info'; para el glifo exacto habría que ajustar el wording de esas cards o aliasar en el plugin.

## 2026-08-19 — Step 2 (Collect) — fuente nueva
- Status: complete
- Asks log:
  - 2026-08-19 — "Ingestar https://medium.com/data-science/train-validation-and-test-sets-72cb40cba9e7" (pedido directo, sin ask previo)
- What was decided: Se capturó el artículo de Tarang Shah sobre train/validation/test como respaldo de la sección nueva que pide el feedback de la diapositiva 2.6.
- Key inputs: research/web/train-validation-test-sets/ (page.md cuerpo completo, original.html verbatim, 9 assets).
- Files created/modified: research/web/train-validation-test-sets/{metadata.yaml, original.html, page.md, assets/}
- Pending open questions: el fetcher no resuelve `srcset`, así que las dos figuras reales del artículo se bajaron a mano (hero + "A visualization of the splits"). Los otros 7 assets son avatares de Medium sin valor editorial.

## 2026-08-19 — Step 3 (Corpus) — registro incremental
- Status: complete
- Asks log: none
- What was decided: Registro nuevo para la captura web, Phase 1 (bytes en disco + stubs). El registro previo chat.md.md quedó intacto.
- Key inputs: research/web/train-validation-test-sets/page.md + original.html + metadata.yaml.
- Files created/modified: research/corpus/train-validation-test-sets.web.md, research/corpus/train-validation-test-sets.web/images/ (9 archivos)
- Pending open questions: Phase 2 (transcripción) sin correr para las 2 figuras reales; los 7 avatares quedaron descritos como chrome y no necesitan Phase 2.

## 2026-08-19 — Step 5 (Review) — ronda 2
- Status: complete
- Asks log:
  - 2026-08-19 — "Alcance de 'Borremos esta seccion' + ubicación de la sección nueva" → el presentador no respondió la pregunta; mandó dos fuentes más y "usá esta info para enriquecer la sección nueva", así que se avanzó bajo los supuestos recomendados (borrar solo la diapositiva 2.6; sección nueva entre "Modelar la entrada" y "Modelar la salida"), declarados en el reporte.
  - 2026-08-19 — "La tabla Test Set vs. Training Set vs. Validation Set deberia estar" → aplicado como diapositiva 3.2.
- What was decided: Se cerraron las 6 observaciones de la ronda. (1.1) definición de tensor al inicio y el bullet "Por eso codificar mal es fatal" renombrado a "El error de codificación entra silencioso". (2.1) tabla a cinco columnas con definición propia, tres ejemplos por fila, Secuencia corregida y párrafo que la separa de Señal. (2.2) párrafo sobre lo que promete un float (diferencias comparables, magnitud que escala vía W·x). (2.3) reordenada a definición → datos → efecto → recetas. (2.6) reemplazada: sale μ y σ, entra "De la variable al tensor: la tabla de decisiones" con doce filas desde el corpus. Sección 3 nueva "Partir el dataset" con cuatro diapositivas; secciones 3–6 renumeradas a 4–7, agenda, arco narrativo y ocho referencias cruzadas actualizadas.
- Key inputs: draft.md (6 bloques de feedback), config/learnings.md L1–L7, corpus/chat.md.md §3 §4 §6, corpus/train-validation-test-sets.web.md, corpus/train-test-split-roboflow.web.md.
- Files created/modified: draft.md (~25 → ~29 diapositivas), memory.md
- Pending open questions: (1) barrido definición-primero sobre todo el mazo, que el presentador marcó como patrón general y quedó sin responder; (2) Phase 2 de las 7 figuras pendientes en los dos registros web nuevos; (3) duración: la sección nueva suma cuatro diapositivas a un mazo que ya estaba justo para 90 min; (4) estratificación y partición temporal en la slide 3.4 van sin fuente, como aporte del docente.

## 2026-08-19 — Step 2/3 (Collect + Corpus) — segunda fuente
- Status: complete
- Asks log:
  - 2026-08-19 — "Ingest: https://blog.roboflow.com/train-test-split/" (pedido directo)
- What was decided: Se capturó el post de Roboflow, que cubre justo los huecos del de Medium: ratios concretos (70/20/10, 80/10/10), tabla comparativa de los tres conjuntos, regla de augmentation, errores típicos, código de sklearn y el intercambio de cross-validation. Registro Phase 1 con 6 imágenes en el companion.
- Key inputs: research/web/train-test-split-roboflow/page.md (extracción limpia y completa).
- Files created/modified: research/web/train-test-split-roboflow/, research/corpus/train-test-split-roboflow.web.md, research/corpus/train-test-split-roboflow.web/images/
- Pending open questions: la fuente está escrita para visión por computadora y es contenido de marketing de Roboflow; ambas cosas quedaron anotadas en el registro y en Open questions del borrador. Phase 2 sin correr para 5 de las 6 imágenes.

## 2026-08-19 — Step 5 (Review) — ronda 3
- Status: complete
- Asks log:
  - 2026-08-19 — "Lo que quise decir es que en los cards veo que se empieza definiendo ejemplo y no se define. No veo consistencia." (aclaración del comentario general de la ronda 2)
  - 2026-08-19 — "Agregue tambien mas ffeedback." → dos bullets en la 5.1
  - 2026-08-19 — "El quiz deberia estar despues de presentar el slide 'La matriz de confusión'" → corregido por el propio presentador en el mensaje siguiente
  - 2026-08-19 — "el quiz deberia ir despues de 'Precision, recall y F1'. Sino se usan los terminos sin explicarlos." + "Agregar 1 caso ms"
- What was decided: (a) Regla de card fijada para todo el mazo (etiqueta nombra, oración siguiente define, ejemplo después) y barrido de las seis diapositivas que no la cumplían: 1.3, 2.3, 2.5, 4.3, 7.1, 7.3. Registrada a nivel Agenda. (b) 5.1 reescrita con la fórmula de accuracy en bloque propio, ejemplo de 10.000 transacciones y diagrama ASCII nuevo que enfrenta accuracy 99% contra 0 de 100 fraudes; se retiró la plantilla `stat`. (c) El quiz pasó de 5.2 a 5.4, con cuarto caso (churn) que justifica F1; "La matriz de confusión" y "Precision, recall y F1" subieron a 5.2 y 5.3; goal de sección y referencia cruzada de accuracy actualizadas.
- Key inputs: draft.md, config/learnings.md L1–L7, skills/desrobotizar.
- Files created/modified: draft.md, memory.md
- Pending open questions: (1) el diagrama nuevo de la 5.1 y el de la 3.1 se suman a los 5 que ya había, así que Polish va a dibujar 7; (2) duración: el mazo quedó en ~29 diapositivas para 90 min; (3) sigue sin confirmarse el supuesto de la ronda 2 (borrar solo la 2.6, sección nueva en el lugar 3); (4) Phase 2 de las 7 imágenes pendientes en los dos registros web.

## 2026-08-19 — Step 5 (Review) — ronda 4
- Status: complete
- Asks log:
  - 2026-08-19 — "Revisa mas comentarios" → dos bullets nuevos, en 5.3 y 5.5
- What was decided: (a) 5.3: la card de F1 abre con la fórmula 2·(P·R)/(P+R) y define la media armónica por contraste con el promedio común, con el par 0.9 / 0.5 (promedio 0.70, F1 0.64) y el caso degenerado de recall 0. Notas del orador ampliadas con el argumento del clasificador que marca todo. (b) 5.5: la diapositiva hacía dos cosas a la vez y esa era la fuente de confusión. El umbral pasa a ser el centro con un diagrama ASCII del eje de probabilidad y tres posiciones de umbral, que reemplaza dos cards; quedan dos cards en vez de cuatro y la matriz N×N baja a una línea de cierre. Texto reducido a poco menos de la mitad.
- Key inputs: draft.md, config/learnings.md L1–L7.
- Files created/modified: draft.md, memory.md
- Pending open questions: (1) Polish tiene que dibujar 8 diagramas, no 5: se sumaron partición (3.1), desbalance (5.1) y umbral (5.5); (2) mazo en ~29 diapositivas para 90 min, candidatas de recorte actualizadas en Open questions; (3) sigue sin confirmarse el supuesto de la ronda 2 (borrar solo la 2.6, sección nueva en el lugar 3); (4) Phase 2 de las 7 imágenes pendientes en los registros web.

## 2026-08-19 — Step 6 (Polish)
- Status: complete
- Asks log: none (paso automático)
- What was decided: cp draft.md → final.md. 8 bloques ASCII renderizables (el noveno, la fórmula de accuracy en la 5.1, quedó como bloque de código sin mapear, que es lo correcto). Tres triplets renombrados por la renumeración de secciones (s4-3-1→s5-2-1 matriz, s5-2-1→s6-2-1 curvas, s6-1-1→s7-1-1 L2): los sidecars quedaron byte-idénticos, así que los 5 SVG viejos se reusaron sin redibujar. Se dibujaron 3 nuevos (partición 3.1, desbalance 5.1, umbral 5.5), los tres validados y auditados (márgenes parejos, fondo blanco). Se armó un venv en el scratchpad con cairosvg y jinja2, así que esta vez sí hay los 8 PNG deliverables. final.md: 8 refs reescritas de .svg a .png, 34 bloques de Presenter feedback quitados, sin [open] que rescatar, gc sin huérfanos.
- Key inputs: draft.md congelado, config/diagram-style.md, sidecars .ascii.
- Files created/modified: final.md, images/ (8 .svg + 8 .ascii + 8 .png; 3 triplets renombrados)
- Pending open questions: las 2 directivas generate-image (slides 1.1 y 6.1) siguen sin cumplir, esta sesión no tiene capacidad de generación de imágenes. Las slides conservan su texto.

## 2026-08-19 — Step 7 (Render)
- Status: complete
- Asks log:
  - 2026-08-19 — "pasar a final y luego generar strict-html" → html-strict (elegido por el presentador en el mismo pedido)
- What was decided: slide-model.json re-FILLeado desde cero para la estructura nueva: 38 diapositivas más portada (eran 33). Nuevas: la tabla de decisiones 2.6 (value-columns de 12 filas), las 4 de "Partir el dataset", y el separador de sección. Reescritas: 1.1, 1.3, 2.1, 2.2, 2.3, 2.5, 4.3, 5.1, 5.3, 5.4 (quiz con cuarto caso), 5.5, 7.1, 7.3. Auditorías degenerate_enum, field_coverage e image_coverage en verde. Dos avisos de desborde en grillas editoriales (2.1 y 2.5) corregidos acortando los bodies; re-render limpio. Los 9 huecos de imagen quedaron con SVG inlineado (el renderer canjea el .png por su gemelo vectorial), sin placeholders vacíos.
- Key inputs: final.md, slide-model.json de la corrida anterior como base para lo no modificado.
- Files created/modified: output/slide-model.json, output/html/index.html (588 KB), output/html/.render.json, /index.html (índice raíz)
- Pending open questions: un ícono inferido ('remove_red_eye') no existe en el set y cae a 'info'; es cosmético. El .pptx sigue sin poder generarse (no hay Cowork), pero ahora los PNG existen, así que el día que haya Cowork el render no arranca de cero.

## 2026-08-19 — Step 8 (Learnings)
- Status: in_progress
- Asks log:
  - 2026-08-19 — "Promover L8 (definir antes de ejemplificar) / con cambios / saltear" → Promover tal cual
  - 2026-08-19 — "Promover esta Talk a la biblioteca de conocimiento compartida" → pendiente
- What was decided: Las 16 observaciones de las cuatro rondas se espejaron al backlog con etiquetas. Dos etiquetas cruzaron el umbral de 3 y decían lo mismo: missing-definition (4) y definition-before-example (3), las siete de esta Talk. Se promovió **L8 — Definir antes de ejemplificar, en cada card**, con la regla de card (etiqueta nombra, oración define, ejemplo después), la extensión a consistencia gramatical de etiquetas dentro de una diapositiva, y el chequeo de leer solo las negritas seguidas. Se creó config/feedback-processed.md (no existía) y se movieron las 6 filas que la sustentan con promoted_to: L8.
- Key inputs: config/feedback-backlog.md (81 filas antes, 75 después), config/learnings.md L1–L7.
- Files created/modified: config/learnings.md (L8), config/feedback-processed.md (nuevo, 6 filas), config/feedback-backlog.md
- Pending open questions: sin candidatos de conformidad strict (config/strict-learnings.md no existe). Falta la decisión de biblioteca compartida. Otras etiquetas con 3 o más (template-selection, content-addition, slide-title, new-slide) ya están cubiertas por L1–L7 o no son promovibles porque describen el tipo de edición, no una regla.

## 2026-08-19 — Step 5 (Review) — ronda 5, reabierta después de Render
- Status: complete
- Asks log:
  - 2026-08-19 — "Volver a draft" → dos comentarios nuevos en draft.md
  - 2026-08-19 — "¿Fusionar Regularización y L2 con Overfitting, o dejarlas separadas?" → pendiente
- What was decided: Se aplicó el primero. La diapositiva 1.2 pasó de "La mitad de la arquitectura no se elige" a "Lo que hay que diseñar": cinco aspectos en orden de sección (entrada, dataset, salida, error, overfitting), con el contraste original como remate al pie y el desglose viejo archivado en Cut material. Sin números de sección en el contenido visible, a propósito, porque la otra decisión pendiente puede renumerar.
- Key inputs: draft.md, config/learnings.md L1–L8.
- Files created/modified: draft.md, memory.md
- Pending open questions: (1) el comentario sobre Regularización y L2 tiene dos lecturas opuestas y quedó [open]; (2) final.md, slide-model.json y el deck HTML son de antes de este cambio, hay que rehacer Polish y Render al cerrar la ronda; (3) sigue pendiente la biblioteca compartida.

## 2026-08-19 — Step 5/6/7 — cierre de la ronda 5
- Status: complete
- Asks log:
  - 2026-08-19 — "¿Fusionar Regularización y L2 con Overfitting, o dejarlas separadas?" → la primera, fusionar
- What was decided: Se fusionaron las secciones 6 y 7 en "Overfitting y regularización" (6 diapositivas: 2 de diagnóstico, 4 de tratamiento). Las cuatro de regularización se renumeraron 7.1–7.4 a 6.3–6.6; agenda, arco narrativo y tres referencias cruzadas actualizadas. El triplet del diagrama de L2 se renombró s7-1-1 a s6-3-1, así que Polish lo reusó sin redibujar: los 8 diagramas quedaron intactos. Polish y Render rehechos de punta a punta. El mazo pasó de 38 a 37 diapositivas y de 7 secciones a 6.
- Key inputs: draft.md, plan2.json, slide-model.json.
- Files created/modified: draft.md, final.md, images/s6-3-1-objetivo-l2.{ascii,svg,png}, output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md
- Pending open questions: (1) al espejar el feedback aparecieron 6 duplicados, porque las filas promovidas a feedback-processed.md dejan de estar en el backlog y find-closed-unmirrored las vuelve a listar; se quitaron a mano, pero conviene recordarlo la próxima vez que se promueva algo; (2) sigue pendiente la biblioteca compartida; (3) el ícono 'remove_red_eye' sigue cayendo a 'info'.

## 2026-08-19 — Step 5/6/7 — ronda 6
- Status: complete
- Asks log:
  - 2026-08-19 — "Agreguemos esto como un item pero podemos poner una nota" (sobre el remate de la 1.2)
- What was decided: El remate al pie de la 1.2 pasó a ser el sexto ítem de la lista ("Las capas y las neuronas. No están en la lista. Eso sí se elige, y es lo que menos importa del diseño") y el detalle numérico (1 a 3 capas ocultas, ancho en potencias de 2 decreciente, ReLU salvo motivo) bajó a una nota al pie, que en el modelo es un highlight kind: note. Polish y Render rehechos; los 8 diagramas se reusaron sin redibujar. Sigue en 37 diapositivas.
- Key inputs: draft.md, slide-model.json.
- Files created/modified: draft.md, final.md, output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md
- Pending open questions: sigue pendiente la promoción a la biblioteca compartida. Volvieron a aparecer los 6 duplicados de espejado (mismo problema de find-closed-unmirrored contra filas ya promovidas); se quitaron otra vez.

## 2026-08-19 — Step 5/6/7 — ronda 7
- Status: complete
- Asks log:
  - 2026-08-19 — "Movelo como una nota abajo" (el bloque "Por qué no es opcional" de la 2.3)
- What was decided: El argumento del gradiente bajó de párrafo destacado arriba de las recetas a nota al pie de la diapositiva 2.3; en el modelo pasó de highlight kind definition / position top a kind note al pie. La apertura de la diapositiva queda solo con la definición de normalizar. Polish y Render rehechos, los 8 diagramas reusados. Sigue en 37 diapositivas.
- Key inputs: draft.md, slide-model.json.
- Files created/modified: draft.md, final.md, output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md
- Defecto encontrado y corregido: las cuatro diapositivas de la sección 3, que escribí yo al crear la sección, nunca llevaron campo `### Presenter feedback`. El schema lo pide en toda diapositiva de draft.md. La consecuencia fue concreta: al archivar este comentario, la búsqueda del campo saltó a la diapositiva siguiente que sí lo tenía y la observación quedó registrada en 4.1 en vez de 3.1. Se agregó el campo a las cuatro y se corrigió la fila del backlog. strip_feedback pasó de quitar 33 bloques a 37, que confirma el arreglo.
- Pending open questions: sigue pendiente la promoción a la biblioteca compartida.

## 2026-08-19 — Step 5/6/7 — ronda 8
- Status: complete
- Asks log:
  - 2026-08-19 — "Borrar la card Proporciones de la 3.1, ya está en el ASCII"
- What was decided: Se retiró la card "Proporciones de arranque" de la diapositiva 3.1; los 70/20/10 ya los dibuja el diagrama y la card los repetía (L6). Lo que la card decía y el diagrama no dice pasó a las notas del orador: el 80/10/10 para datasets de decenas de miles, y el piso de unos pocos cientos de ejemplos, que ya estaba anotado. La diapositiva queda con tres cards, una por conjunto, alineadas con los tres bloques del diagrama. Polish y Render rehechos, 8 diagramas reusados.
- Key inputs: draft.md, slide-model.json.
- Files created/modified: draft.md, final.md, output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md
- Pending open questions: sigue pendiente la promoción a la biblioteca compartida.

## 2026-08-19 — Step 5/6/7 — ronda 9
- Status: complete
- Asks log:
  - 2026-08-19 — "Reprocesar el feedback" → dos comentarios nuevos en la 4.1, los dos pidiendo ver la forma de las funciones
- What was decided: Dos diapositivas nuevas, las dos con diagrama propio. (1.4) "Las activaciones ocultas, y cómo se ven": definición de qué es una activación oculta, tabla de las cuatro candidatas con fórmula, rango y cuándo, diagrama con las cuatro formas y cierre sobre la saturación, que es la razón por la que ganó ReLU. La card de la 1.3 dejó de adelantar la respuesta y ahora apunta acá. (4.2) "Cómo se ven las cuatro": el complemento visual de la tabla de la 4.1, con lineal, sigmoide y softplus como curvas y softmax como reparto entre clases, que es lo que realmente es. Las diapositivas 4.2 y 4.3 se renumeraron a 4.3 y 4.4.
- Key inputs: draft.md, corpus/chat.md.md §1 y §8.
- Files created/modified: draft.md, final.md, images/s1-4-1-activaciones-ocultas.{ascii,svg,png}, images/s4-2-1-activaciones-salida.{ascii,svg,png}, output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md
- Defecto corregido durante el dibujo: en las dos primeras versiones la sigmoide cruzaba el eje horizontal hacia abajo, o sea tomaba valores negativos, que una sigmoide nunca tiene. Se rebajó el eje de esos paneles al 0 real y se marcó el techo en 1 con línea punteada. La auditoría de aspecto pidió recortar el viewBox de s1-4-1 y se aplicó el recorte sugerido.
- Pending open questions: el mazo pasó de 37 a 39 diapositivas para 90 minutos, y ya venía justo. Es lo primero a mirar en el ensayo. Sigue pendiente la promoción a la biblioteca compartida.

## 2026-08-19 — Step 5/6/7 — ronda 10
- Status: complete
- Asks log:
  - 2026-08-19 — Tres pedidos sobre la diapositiva 1.2: reescribir la card del error, renombrar "Las capas y las neuronas" a "# Capas & # Neuronas", y mover overfitting al final
- What was decided: La card "El error" nombraba accuracy y la matriz de confusión, que recién se definen en la sección 5: en la diapositiva 2 no significaban nada. Ahora define el error en sus propios términos, la distancia entre lo predicho y lo que pasó, y que resumirla en un número es una decisión de diseño. Es L8 aplicada a una card que reenviaba a términos sin definir. La card de capas se renombró a "# Capas & # Neuronas" y, al dejar de titularse como negación, dejó de ser el remate: el cuerpo pasó a describirla como un aspecto más, el único que se elige libremente y el que menos impacto tiene. Overfitting quedó último.
- Ajustes de coherencia que arrastró el reorden: el encabezado decía "cinco decisiones" y ahora dice seis; la nota al pie decía "las cinco de arriba" y ahora dice "las otras cinco"; las notas del orador decían "cada viñeta es una sección" y ahora dicen "casi cada viñeta", porque la de capas no lo es. Sin esos tres arreglos la diapositiva habría quedado mintiendo.
- Key inputs: draft.md, config/learnings.md L8.
- Files created/modified: draft.md, final.md, output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md
- Pending open questions: 39 diapositivas para 90 minutos, ajustado. Sigue pendiente la promoción a la biblioteca compartida.

## 2026-08-19 — Step 5/6/7 — ronda 11
- Status: complete
- Asks log:
  - 2026-08-19 — "Partir mal: explicar un poco cada boxed"
  - 2026-08-19 — "Mover Un catálogo para elegir sin dudar antes de Cómo se ven las cuatro y La capa de salida"
  - 2026-08-19 — "Cómo se ven las cuatro: que tenga un layout equivalente a la de input"
  - 2026-08-19 — "Dos formas de modelar mal la salida: borrar este slide"
- What was decided: (a) Las cinco cards de "Partir mal" pasaron a tres líneas cada una en draft.md, con el patrón qué es, por qué infla la métrica, qué se hace en su lugar. En el modelo van condensadas porque el renderer rechazó `format: list` (avisa que un conjunto etiquetado siempre se lee como grilla) y la grilla no tolera cuerpos de 260 caracteres. (b) La sección 4 quedó catálogo, capa de salida, cómo se ven las cuatro: primero el mapa completo de tarea a salida, después el detalle de la activación y recién ahí su forma. (c) Se rehízo el diagrama de las activaciones de salida con el mismo layout de cuatro paneles que el de las ocultas, mismo viewBox y misma retícula, y softmax pasó de bloque aparte a cuarto panel con barras chicas. La diapositiva pasó de content-image con facts a content+cards+image con cuatro cards, igual que la 1.4. (d) Se borró "Dos formas de modelar mal la salida", archivada completa en Cut material con sus notas del orador.
- Key inputs: draft.md, corpus/chat.md.md §8.
- Files created/modified: draft.md, final.md, images/s4-3-1-activaciones-salida.{ascii,svg,png} (renombrado desde s4-2-1 y redibujado), output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md
- Pending open questions: el mazo bajó de 39 a 38 diapositivas. Sigue pendiente la promoción a la biblioteca compartida.

## 2026-08-19 — Step 5/6/7 — ronda 12
- Status: complete
- Asks log:
  - 2026-08-19 — "Agregar en Precision, recall y F1 en cada box una descripcion de lo que es" + "'Importa...' deberia tener un espacio de la descripcion"
- What was decided: La diapositiva 5.3 pasó de cuatro cards de párrafo corrido a plantilla de columnas con tres zonas por métrica. Arriba el nombre y la pregunta en castellano que responde: precisión, de todo lo que marcó, ¿cuánto era de verdad?; recall, de todo lo que había, ¿cuánto encontró?; F1, ¿y si las dos importan parecido? Debajo la fórmula y el comportamiento. Y aparte, con su propio espacio, el "Importa cuando". La tensión entre precisión y recall bajó a nota al pie. Es L8 llevada a la estructura visual: la etiqueta nombra, la primera línea define en lenguaje llano, la fórmula viene después y el caso de uso queda separado.
- Key inputs: draft.md, schemas/slide-model.md (concept-columns con label, body, text_label, text, example).
- Files created/modified: draft.md, final.md, output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md
- Nota de estilo: la primera redacción usaba guiones largos para separar el nombre de la pregunta; se reemplazaron por punto, que es la regla 11 de desrobotizar.
- Pending open questions: sigue pendiente la promoción a la biblioteca compartida.

## 2026-08-19 — Step 5/6/7 — ronda 13
- Status: complete
- Asks log:
  - 2026-08-19 — "¿Por qué cuando la seleccioné no se marcó la correcta en el quiz?"
  - 2026-08-19 — "El problema del quiz es que deberían ser 3 quiz, con la pregunta y luego seleccionar precisión o recall"
  - 2026-08-19 — "¿Qué es la matriz N×N?"
- What was decided: (a) El quiz no marcaba nada por dos razones: al moverlo de lugar le saqué el campo `correct`, y de fondo los cuatro casos estaban cargados como opciones de una única pregunta de opción múltiple cuando cada uno tenía su propia respuesta. (b) Se partió en tres diapositivas de quiz, una por caso, cada una con pregunta propia y opciones reales: spam con precisión, enfermedad grave con recall, churn con F1 y tres opciones. Ahora hay una sola respuesta correcta por diapositiva y el renderer la resalta al avanzar; verificado, tres opciones marcadas como correctas en el HTML. El caso de fraude no quedó como quiz porque no tiene respuesta única y pasó a las notas del orador de la tercera. (c) "La matriz N×N" estaba en el título de una diapositiva y solo se explicaba en una línea al pie: L8 al revés. La diapositiva pasó a "El umbral, y qué pasa con más de dos clases" y la línea de cierre define de verdad la matriz (fila por clase real, columna por clase predicha, diagonal de aciertos, celdas fuera de la diagonal como confusiones concretas). El diagrama del umbral se renombró de s5-5-1 a s5-7-1.
- Key inputs: draft.md, schemas/slide-model.md (quiz con options y correct), templates/html/quiz.j2.
- Files created/modified: draft.md, final.md, images/s5-7-1-umbral.{ascii,svg,png} (renombrado), output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md
- Pending open questions: el mazo pasó de 38 a 40 diapositivas para 90 minutos. Ya venía justo y esto lo estira más; es lo primero a cronometrar en el ensayo. Sigue pendiente la promoción a la biblioteca compartida.

## 2026-08-19 — Step 5/6/7 — ronda 14
- Status: complete
- Asks log:
  - 2026-08-19 — "Enfoquémonos solo a 2 clases. Y poner solo una nota al final."
- What was decided: La sección 5 queda binaria de punta a punta. La diapositiva 5.7 pasó a "El umbral, una perilla de negocio" y el bloque de multiclase, que ocupaba un párrafo entero, se redujo a una nota de dos líneas al pie: la matriz crece a una fila por clase real y una columna por clase predicha, precisión y recall se calculan por clase, la idea no cambia. El ejemplo del clasificador de dígitos quedó en las notas del orador, marcado como "no lo desarrolles salvo que lo pidan". El goal de la sección declara ahora explícitamente el alcance binario.
- Key inputs: draft.md.
- Files created/modified: draft.md, final.md, output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md
- Defecto de proceso: en el primer intento el reemplazo del goal falló porque el texto tenía "el quiz obliga a elegir cuál duele en cuatro casos" y yo buscaba una variante. El script aborta antes de escribir cuando un reemplazo no matchea, así que el borrador quedó intacto pero el modelo ya se había actualizado por separado: quedaron desincronizados un momento. Conviene tocar borrador y modelo en el mismo script, o verificar el sha del stamp después de cada ronda.
- Pending open questions: 40 diapositivas para 90 minutos. Sigue pendiente la promoción a la biblioteca compartida.

## 2026-08-19 — Step 8 (Learnings) — cierre
- Status: complete
- Asks log:
  - 2026-08-19 — "Promover esta Talk a la biblioteca de conocimiento compartida" → sí
- What was decided: Se creó knowledge-library/, que no existía, con cinco temas nuevos curados desde los tres registros del corpus, final.md y los diez diagramas. Los temas se organizaron por materia y no por sección de la clase: codificacion-de-variables, particion-del-dataset, metricas-de-clasificacion, activaciones-y-capa-de-salida, overfitting-y-regularizacion. Cada uno con index.md, frontmatter con sources, y su propia carpeta images/ autocontenida. Las diez imágenes se copiaron en svg y png a la carpeta del tema que las usa; los sidecars .ascii no, porque la biblioteca guarda artefactos renderizados y el fuente queda recuperable desde el Talk.
- Curación, no copia: se dejó afuera el andamiaje de diapositivas (agenda, orden de secciones, notas del orador, feedback) y se conservaron los conceptos, la evidencia y los enlaces de vuelta a los registros del corpus por ruta relativa. Se agregaron enlaces cruzados entre los cinco temas donde el contenido se apoya mutuamente.
- Advertencias de procedencia que se propagaron a la biblioteca: metricas-de-clasificacion no tiene fuente en el corpus y sus números son ilustrativos; los ratios 70/20/10 son recomendación de Roboflow y no un estudio; estratificación y partición temporal son aporte del docente sin fuente detrás.
- Files created/modified: knowledge-library/{codificacion-de-variables, particion-del-dataset, metricas-de-clasificacion, activaciones-y-capa-de-salida, overfitting-y-regularizacion}/{index.md, images/} — 5 index.md, 20 archivos de imagen, 492 KB.
- Verificación: todas las referencias de imagen resuelven dentro de la carpeta del tema, todos los enlaces relativos al corpus del Talk existen, y todos los enlaces entre temas existen.
- Pending open questions: ninguna. El Talk queda cerrado.

## 2026-08-19 — retoque post-cierre
- Status: complete
- Asks log:
  - 2026-08-19 — "Última modificación: a definir, poner la fecha de hoy"
- What was decided: El campo `date` del frontmatter pasó de "a definir" a 2026-08-19, en draft.md y en deck.date del modelo. Es el campo que el renderer rotula "Última modificación" en la portada. Polish y Render rehechos; los 10 diagramas se reusaron.
- Nota: según el schema ese campo es la fecha de dictado de la clase, y el renderer lo muestra como última modificación. Si el dictado no es hoy, es el mismo campo el que hay que cambiar.
- Files created/modified: draft.md, final.md, output/slide-model.json, output/html/index.html, /index.html

## 2026-08-19 — Step 5/6/7 — ronda 15
- Status: complete
- Asks log:
  - 2026-08-19 — "En la tabla de neuronas para el input hay una tabla. ¿Es eso correcto?"
  - 2026-08-19 — "Leí que el input realmente no son neuronas"
- What was decided: La tabla de decisiones tenía cuatro problemas y se corrigieron todos. (1) `k` y `d` se usaban en cinco filas sin definirse; ahora se definen en la bajada. (2) "Con faltantes" no era un tipo de variable sino un modificador que se cruza con todas las filas, y su "1 + 1" solo valía para una variable numérica: con un barrio en one-hot son k + 1. Salió de la tabla y pasó a un párrafo propio. (3) "Fecha 2 + 1" asumía un solo ciclo; pasó a "2 por ciclo + 1". (4) La columna se llamaba "Neuronas" y es incorrecto: la capa de entrada no tiene pesos ni calcula nada, es el vector en sí, y la primera que hace `z = W·x + b` más activación es la primera capa oculta. Pasó a llamarse "Floats", que además es el término con el que abre la sección, y se agregó la explicación de la distinción. Se corrigieron también el goal de la sección 2 y el cierre de la diapositiva, que decían "cantidad de neuronas de entrada".
- El encabezado "Neuronas" del catálogo de salida (sección 4) no se tocó: ahí sí son neuronas de verdad.
- Key inputs: draft.md, corpus/chat.md.md §1 y §3.
- Files created/modified: draft.md, final.md, output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md
- Pending open questions: la referencia a "neuronas de entrada" que quedó en Cut material es de contenido archivado y no se tocó a propósito.

## 2026-08-19 — Step 5/6/7 — ronda 16: revisión crítica completa
- Status: complete
- Asks log:
  - 2026-08-19 — "Revisá toda la presentación con espíritu crítico buscando inconsistencias" → 13 hallazgos
  - 2026-08-19 — "Aplicá todo, usá criterio más claro"
  - 2026-08-19 — "Agregar después de 'La red no ve el problema, ve un tensor' cómo son estos tensores: señal 1D, imagen con un color, RGB y el input. Un slide con ASCII."
- Hallazgos y resolución: (1) Un comentario del presentador había quedado sin procesar por estar escrito sin espacio después del guion, y pedía partir la 5.7 para mostrar la matriz N×N, o sea lo contrario de la instrucción posterior de enfocarse en dos clases. Criterio aplicado: la instrucción más reciente gana. (2) La 2.6 se contradecía a sí misma, decía "floats, no neuronas" y seis líneas después "se suma una neurona"; el término estaba mal en cinco lugares más (2.2, 2.4 ×2 y ASCII, 2.5). Todos a float o posición del vector. (3) La tesis no mencionaba la partición del dataset, que es un sexto de la clase; reescrita a tres lugares de decisión. (4) El goal de la sección 4 prometía una diapositiva borrada. (5) La 4.3 decía "la tabla del catálogo dice el rango" y el rango está en la 4.2, no en el catálogo. (6) La 4.2 decía que las cuatro representaciones viven en una misma diapositiva y sus notas describían los dibujos, que desde la partición están en la 4.3. (7) El goal de la sección 1 prometía una diapositiva reemplazada y no mencionaba las activaciones ocultas. (8) Open questions tenía cuatro datos viejos (29 diapositivas, sección 4, slide 5.5, 8 diagramas). (9) Anglicismo "slide" en cuatro lugares. (10) Referencia colgada en las notas de la 1.4 a una cuenta de parámetros que no existe en el mazo. (11) La sección 5 y su diapositiva 5.2 se llamaban igual; la sección pasó a "Medir un clasificador". (12) Faltaba el separador entre la 2.2 y la 2.3. (13) La conclusión decía "cuatro ideas, una por sección troncal" con seis secciones y sin cubrir la partición; se agregó el bullet y se corrigió el conteo.
- Diapositiva nueva: 1.2 "Cómo se ve un tensor", con un diagrama de los cuatro casos (tabular, señal 1D, imagen gris, RGB) con su shape, de un eje a tres, más la dimensión de lote. Cuatro cards y el canal RGB marcado como eje no espacial. Las diapositivas 1.2 a 1.4 pasaron a 1.3 a 1.5 y los diagramas de la neurona y las activaciones ocultas se renombraron en consecuencia.
- Key inputs: draft.md completo, corpus/chat.md.md §2.
- Files created/modified: draft.md, final.md, images/s1-2-1-formas-de-tensor.{ascii,svg,png} nuevo, s1-4-1-neurona.* y s1-5-1-activaciones-ocultas.* renombrados, output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md
- Verificación: cero usos incorrectos de "neurona" para el input, cero anglicismos "slide", 12 huecos de imagen con SVG inlineado y ninguno vacío, auditorías en verde.
- Pending open questions: 41 diapositivas para 90 minutos. Es el punto abierto más serio y está anotado en Open questions con las candidatas a recortar.
