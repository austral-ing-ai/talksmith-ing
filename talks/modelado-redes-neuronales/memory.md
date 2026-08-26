# memory.md — modelado-redes-neuronales

**Current step:** 8 (Learnings) — iteración post-render, complete
**Awaiting:** — (pendiente aparte y ya crítico: el blocker de duración)
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

## 2026-08-19 — Step 5/6/7 — ronda 17
- Status: complete
- Asks log:
  - 2026-08-19 — "'El canal no es espacial... y se puede reordenar' ¿no es verdad si es un DNN?"
- What was decided: La objeción era parcialmente correcta y valía la corrección. La afirmación sobre el dato es cierta (el canal no tiene vecindad, alto y ancho sí), pero la card decía "se puede reordenar sin cambiar nada" sin decir respecto de qué. El contraste solo tiene consecuencias contra una Conv2D, que trata alto y ancho como espacio al deslizar el mismo kernel; en un Dense sobre la imagen aplanada no hay ningún eje espacial y todas las posiciones son reordenables, las espaciales incluidas. La card pasó a decir que el canal es el único de los tres reordenable, y las notas del orador incorporan el matiz completo con los números del corpus: kernel 3x3 sobre RGB son 27 pesos y no 9; RGB 224x224 aplanada son 150.528 entradas y 38,5M de parámetros en la primera capa contra 896 de un Conv2d(3,32,3).
- El matiz refuerza la tesis de la clase en vez de debilitarla: que un Dense no distinga ejes es exactamente por qué es la arquitectura equivocada para una imagen.
- Key inputs: draft.md, corpus/chat.md.md (líneas 30, 81, 161, 296: el eje de canales y los conteos de parámetros).
- Files created/modified: draft.md, final.md, output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md

## 2026-08-19 — Step 5/6/7 — ronda 18
- Status: complete
- Asks log:
  - 2026-08-19 — "Acá no estamos explicando redes convolucionales. Hablar de muchas capas produce ruido."
  - 2026-08-19 — "El apilada no está bien."
- What was decided: (a) Se sacó todo lo convolucional de la 1.2. La card de señal ya no menciona Conv 1D y la de RGB ya no habla de reordenar, que era la afirmación que obligaba a explicar Conv2D para tener sentido; las notas perdieron el párrafo de kernels, pesos compartidos y conteos de parámetros que yo mismo había agregado la ronda anterior. En el mazo entero solo queda una mención a convolución, la columna "Arquitectura" de la tabla de la 2.1, que es un nombre por fila y no una explicación. Se agregó una línea que declara el alcance: el resto de la clase trabaja sobre el caso tabular. (b) "Tres matrices apiladas" era un error, no una imprecisión: apilar sugiere profundidad, o sea un tercer eje espacial, que es justo la confusión que la card quería corregir. Y el diagrama las dibujaba apiladas con desfase. Ahora la card dice "la misma grilla, con tres números en cada píxel" y el diagrama muestra una sola grilla, igual que la de escala de grises, con un píxel ampliado que guarda R, G y B. El paralelismo entre los dos paneles hace el punto sin texto.
- Aprendizaje de proceso: en la ronda 17 respondí una objeción del presentador agregando precisión técnica a las notas, y esa precisión se salió del alcance de la clase. La respuesta correcta a "esto no es del todo cierto" no siempre es explicar más; acá era sacar la afirmación que no se podía sostener sin material de otra clase.
- Files created/modified: draft.md, final.md, images/s1-2-1-formas-de-tensor.{svg,png}, output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md

## 2026-08-19 — Step 5/6/7 — ronda 19
- Status: complete
- Asks log:
  - 2026-08-19 — "Pero si son tres números en el mismo píxel, ¿no se puede modelar la red?"
  - 2026-08-19 — "Confirmá esto con documentación formal sobre cómo modelar esto en un NN."
- What was decided: La pregunta quedó anticipada en las notas del orador, y la verificación contra documentación encontró un error en mi primera respuesta. Yo había dicho "se aplana" como si fuera automático y no lo es: una capa densa opera solo sobre el último eje. Keras: "If the input to the layer has a rank greater than 2, Dense computes the dot product between the inputs and the kernel along the last axis of the inputs". PyTorch nn.Linear: "Output: (*, H_out) where all but the last dimension are the same shape as the input". Aplanar es una capa explícita, Flatten() o nn.Flatten().
- Verificación empírica en el venv de missions/clase3: Dense(32) sobre (8,224,224,3) sin aplanar devuelve (8,224,224,32) con 128 parámetros, que es kernel (3,32) más bias; con Flatten() antes devuelve (8,32) con 4.816.928, que es kernel (150.528,32) más bias.
- El hallazgo confirma la card en vez de contradecirla: el framework, por defecto, trata el eje de canal como el eje de variables, o sea que "tres columnas de una tabla" no es una analogía pedagógica sino lo que Keras hace literalmente. También valida el número del corpus: los 38,5M eran con 256 unidades (150.528 x 256 + 256 = 38.535.424).
- Fuentes: https://keras.io/api/layers/core_layers/dense/ , https://keras.io/api/layers/reshaping_layers/flatten/ , https://docs.pytorch.org/docs/2.13/generated/torch.nn.Linear.html
- Files created/modified: draft.md, final.md, output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md
- Pending open questions: las citas de Keras y PyTorch están en las notas del orador pero no en el corpus. Si se quieren como fuente formal de la Talk, habría que ingerir las dos páginas de documentación en la Colecta.

## 2026-08-20 — Step 5/6/7 — ronda 20: enfoque MLP
- Status: complete
- Asks log:
  - 2026-08-20 — "¿Nueva presentación o retomar una existente?" → Retomar `modelado-redes-neuronales`
  - 2026-08-20 — "¿Por dónde arrancamos?" → "Retomemos en draft" → volver al borrador (Revisión)
- Estado al reabrir: draft.md sin feedback pendiente (46 viñetas cerradas, cero `[open]`), 40 diapositivas en 6 secciones + conclusiones, 10 diagramas, final.md y el mazo HTML al día desde la ronda 19.
- Pending open questions: las de la sección `Open questions` de draft.md, sin cambios — duración (40 diapositivas para 90 min), citas de Keras/PyTorch fuera del corpus, sección 5 sin fuente, estratificación/partición temporal sin fuente, dos directivas `generate-image` sin cumplir.
- 2026-08-20 — Instrucción del presentador: la clase se enfoca en **MLP**. Sale el vocabulario de "tensor" del mazo (confuso). Diapositiva nueva después de la 1.4 que cubra el input como vector de features, la tabla tipo de dato → codificación, dimensionalidad fija, escala y one-hot contra embedding, más el contraste MLP/CNN/RNN-Transformer y la definición de MLP. Las diapositivas 1.2 a 1.5 (con la nueva como 1.5) tienen que dar ese framing.
- Tensión detectada: la instrucción reabre el contraste de arquitecturas que la ronda 18 había sacado por ruidoso. Vale la reapertura porque el propósito cambió — antes era una digresión, ahora es lo que justifica declarar el alcance MLP. Aplica la regla de la ronda 16: la instrucción más reciente gana.
- Solapamiento a resolver: la 2.1 ya tiene una tabla de seis familias de estructura con su arquitectura. Con el framing nuevo quedarían dos tablas diciendo casi lo mismo. Ask abierto.
- What was decided: La clase pasa a declarar su alcance en la sección 1 y a llamarse "Modelado de un Multi-Layer Perceptron (MLP)". Cinco cambios. (1) Salió el vocabulario de tensor del mazo entero (tesis, goal de la sección 1, título y apertura de la 1.1, la 2.2 y el título de la 2.6); en su lugar "una fila de números". (2) La 1.2 pasó de "Cómo se ve un tensor" a "La forma del input la decide la arquitectura": contrasta MLP, CNN y RNN/Transformer sobre el mismo ejemplo de 28x28, define qué es un MLP y declara el alcance. (3) Diapositiva nueva 1.5 "El vector de entrada, una posición por feature", después de la neurona: feature por posición, largo fijo, tabla tipo de dato a codificación, y escala y one-hot contra embedding apuntando a la sección 2. Las activaciones ocultas pasaron a 1.6. (4) La 1.3 abre con "Diseñar un MLP" y la 1.4 dejó de apuntar a "la diapositiva que sigue", que con la 1.5 en el medio habría quedado mintiendo. (5) La 2.1 se recortó al caso tabular y su tabla de seis familias de estructura quedó archivada en Cut material, porque con el framing nuevo quedaban tres tablas solapadas.
- Reapertura consciente de la ronda 18: aquella ronda sacó lo convolucional de la sección 1 por ruidoso y esta lo reintroduce. Vale porque el propósito cambió: antes era una digresión, ahora es lo que justifica declarar el alcance. Regla de la ronda 16, la instrucción más reciente gana.
- Key inputs: draft.md completo; corpus/chat.md.md §2 (familias de estructura y su arquitectura natural), §3 (codificación), §4 (umbrales ≤15 one-hot / ≥50 embedding), §5 (z-score media 0 desvío 1). El ejemplo de MNIST 28x28 con 784 posiciones lo aportó el presentador y no está en el corpus; queda marcado así en el campo Sources de las dos diapositivas y en Open questions.
- Diagramas: se dibujó s1-2-1-formas-de-input (tres arquitecturas sobre el mismo dato de 28x28, con el panel MLP en acento), se borró s1-2-1-formas-de-tensor y se renombró s1-5-1-activaciones-ocultas a s1-6-1. Los otros diez se reusaron sin volver a renderizar. Desvío del contrato: la crítica del diagrama la hice yo por inspección del PNG en vez de despachar el subagente diagram-critic, porque la sesión tiene el Agent tool deshabilitado. validate_svg ok, audit_aspect ok (imbalance 2.12x sobre un umbral de 2.5x).
- Bookkeeping: se espejaron al backlog las 5 viñetas de esta ronda más 16 rezagadas de rondas anteriores que nunca se habían espejado. find-closed-unmirrored queda en cero.
- Render: html-strict, 42 diapositivas. La primera pasada avisó que la 2.1 no entraba en la grilla editorial (cuerpo de 170 caracteres contra ~140); se le sacó el formato editorial y se acortaron las tres cards, y la segunda pasada salió limpia. Auditorías degenerate_enum, field_coverage e image_coverage en verde.
- Files created/modified: draft.md, final.md, images/s1-2-1-formas-de-input.{svg,png}, images/s1-6-1-activaciones-ocultas.* (renombrados), output/slide-model.json, output/html/index.html, /index.html, config/feedback-backlog.md
- Pending open questions: las dos directivas generate-image (1.1 y 6.1) siguen sin cumplir, esta sesión tampoco tiene generación de imágenes. El framing MLP y el ejemplo de MNIST no están en el corpus; si se los quiere anclar hay que sumar la exploración en la Colecta. Duración: 34 diapositivas de contenido para 90 minutos.


## 2026-08-21 — Step 5 — ronda 21: pérdida y backpropagation
- Status: complete
- Asks log:
  - 2026-08-21 — "¿Nueva presentación o retomar una existente?" → Retomar `modelado-redes-neuronales`
  - 2026-08-21 — "¿Qué tan fina va la sección de loss functions?" → Opción 1, por familia
  - 2026-08-21 — "¿Qué tan fina va la sección de backpropagation?" → Comprensiva (opción 2)
  - 2026-08-21 — "¿Propongo los recortes para volver a 90 minutos?" → sin responder, queda abierto
- Estado al reabrir: el encabezado de memory.md decía Step 8 awaiting_presenter, arrastrado de una sesión anterior; la última entrada real era la ronda 20 (Step 5/6/7). El presentador pidió procesar feedback, así que la sesión entró por Revisión y el encabezado quedó corregido.
- Entradas de esta ronda: 4 viñetas escritas en draft.md más 2 instrucciones dadas en chat (backpropagation y la cita de apertura), que se registraron como viñetas antes de aplicarlas.
- What was decided:
  (1) **Diapositiva 1.3 nueva, "Qué es un MLP"** — la definición salió del cuerpo de la 1.2 y quedó sola como cita a pantalla completa. La 1.2 se queda con el contraste de las tres arquitecturas y la declaración de alcance. Las 1.3 a 1.6 corrieron a 1.4 a 1.7.
  (2) **Sección 5 nueva, "La función de pérdida"**, seis diapositivas: la cita de apertura, qué es una loss (loss/cost/objective y la diferenciabilidad), regresión con MSE/MAE/Huber en una sola, BCE, cross-entropy, y las especializadas en tabla. Las tres de regresión van juntas porque el punto es el contraste y se ve en un solo dibujo. El bloque archivado "Activación y loss se eligen juntas" volvió al mazo repartido entre la 5.4 y la 5.5.
  (3) **Sección 6 nueva, "Cómo aprende la red: backpropagation"**, siete diapositivas: ciclo forward/backward, la función de coste, la regla de la cadena, el delta, la propagación hacia atrás, el paso de actualización, y batch contra época.
  (4) **La lista de decisiones de diseño de la 1.4** perdió "El overfitting" y ganó "La función de pérdida". Para no dejar dos cards diciendo lo mismo, "La salida" dejó de mencionar la loss y "El error" pasó a ser explícitamente la medición del modelo ya entrenado.
  (5) **Tabla de la 2.6**: el encabezado lo cambió el presentador a mano; la bajada decía "La columna dice floats, no neuronas" y pasó a "La última columna cuenta floats, no neuronas". El párrafo de faltantes que el presentador borró quedó archivado en Cut material y su contenido sobrevive en las notas del orador.
- Reuso de la biblioteca de conocimiento: las cinco imágenes de fórmulas de `knowledge-library/backpropagation/` (función de coste, regla de la cadena, delta de salida, delta oculto, paso de actualización) se copiaron a `images/bp-*.png` y se referencian directas, sin volver a renderizarlas. La sexta imagen del tema, el diagrama forward/backward, tenía párrafos en inglés y **no** se reusó: se reemplazó por un ASCII propio en español, que además deja espacio para la mecánica de batches. Es el primer reuso cross-Talk de este repo.
- Decisión de notación: las secciones 5 y 6 usan `y` para la predicción y `t` para el objetivo, que es lo que traen las imágenes reusadas y lo que los alumnos ya vieron en `intro-redes-neuronales`. El corpus usa `y − ŷ`. Las dos son estándar y no se pueden mezclar; queda anotado en Open questions con el costo de revertir (reescribir las fórmulas de la sección 5 y volver a dibujar las cinco imágenes).
- Tensión resuelta: la sección 6.2 deriva sobre la L2 con el factor ½ mientras la 5.3 escribe MSE sin él. Las notas del orador de la 6.2 lo explican (una constante positiva no mueve el mínimo, el ½ está para que la derivada quede limpia) porque un alumno lo iba a notar.
- Aporte propio marcado: la mecánica de batches (6.7) se apoya en el corpus solo para el manejo `(B,n)` y para que el batch size sea hiperparámetro; el resto, incluido el ejemplo aritmético de 10.000 filas con batch 100, es construido para la clase y está declarado en Sources.
- Verificación numérica: −log(0,80) = 0,22 y −log(0,05) = 3,00 (logaritmo natural), las tres probabilidades del diagrama suman 1,00; Huber con d = 1 castiga 0,5, 1,5 y 9,5 para errores de 1, 2 y 10, contra 1, 4 y 100 de MSE y 1, 2 y 10 de MAE. Todos recomputados antes de escribirlos.
- Key inputs: draft.md completo; corpus/chat.md.md (§1 loss/cost/objective y batches, §8 catálogo de outputs y detalles de implementación, §4 gradiente ralo); knowledge-library/backpropagation/index.md y sus imágenes.
- Files created/modified: draft.md, config/feedback-backlog.md, images/bp-funcion-de-coste.png, images/bp-regla-de-la-cadena.png, images/bp-delta-salida.png, images/bp-delta-oculta.png, images/bp-paso-de-actualizacion.png
- Verificación estructural: cero viñetas sin cerrar, cero `[open]`, find-closed-unmirrored en cero, 38 fences balanceadas, cero referencias de imagen rotas.
- Pending open questions: **la duración es ahora el problema más serio del mazo.** 48 diapositivas de contenido contra 34 antes de esta ronda; a dos minutos por diapositiva son 96 minutos sin una sola pregunta. Hay que recortar o partir la clase en dos, y el presentador todavía no decidió. Candidatas anotadas en Open questions. Siguen abiertas la notación y/t, la atribución de la cita de la 5.1, y las dos directivas generate-image sin cumplir.

## 2026-08-21 — Step 6 (Pulido) y Step 7 (Render) — ronda 21
- Status: complete
- Asks log:
  - 2026-08-21 — "¿Pulir y renderizar, o proponer recortes primero?" → "Vamos a pulir y generar el HTML"
- Diagramas: 16 bloques ASCII en final.md. **10 se reusaron sin volver a dibujar** (sello de digest intacto). **6 se renderizaron**: los 5 nuevos más s1-2-1-formas-de-input, que la ronda 20 había dejado sin sellar y por eso volvía a entrar en cada pasada.
- Renombre por corrimiento de secciones: 7 juegos de archivos (.svg/.png/.ascii más su companion de crítica) pasaron a su id nuevo — s1-4-1 a s1-5-1, s1-6-1 a s1-7-1, s5-1-2 a s7-1-2, s5-2-1 a s7-2-1, s5-7-1 a s7-7-1, s6-2-1 a s8-2-1, s6-3-1 a s8-3-1. Renombrar en vez de re-renderizar preserva el sello, así que los 7 entraron como "sin cambios".
- Diagramas nuevos: penalización de MSE/MAE/Huber, penalización de BCE, reparto de cross-entropy, ciclo forward-backward, batches contra época. Tres limpios en la primera pasada; dos necesitaron una revisión (una por una etiqueta apretada, dos por encuadre que el audit de aspecto marcó). Ninguno quedó sin resolver.
- **Desvío de contrato registrado en los 5 logs de crítica:** la revisión visual la hizo el propio diagram-illustrator leyendo el PNG de `.critique/`, sin despachar el subagente diagram-critic ciego, porque la sesión tiene instrucción explícita de no invocar subagentes salvo pedido del presentador. Vale menos que una crítica independiente y está dicho en cada log.
- Corrección numérica detectada durante el pulido: las notas de la 5.5 decían que con 0,05 la penalización "se multiplica por catorce"; el cociente real es 3,00 / 0,22 = 13,4. Se corrigió a "por más de trece" en draft.md y se rehizo la copia a final.md antes de seguir. Es la única escritura sobre draft.md después de cerrar la Revisión, y fue para arreglar un número que yo mismo había puesto mal.
- Imágenes reusadas de la biblioteca: las 5 de fórmulas de backpropagation entraron como refs directas a `images/bp-*.png`, sin pasar por el pipeline de ASCII.
- Limpieza de final.md: 16 fences reescritas a refs de imagen, 16 refs .svg reescritas a .png (auditoría de extensiones en verde, cero .svg/.webp/.avif/.heic), cero `[open]` que rescatar, 58 bloques de Presenter feedback quitados (48 de diapositiva, 10 de sección/agenda).
- Sin cumplir: las dos directivas `generate-image` (1.1 y 8.1). Esta sesión tampoco tiene generación de imágenes.
- Render: html-strict. El modelo pasó de 42 a **58 diapositivas** (cubierta, 8 divisores de sección, contenido y conclusiones). Se reconstruyó el slide-model a partir del de la ronda 20: se insertaron la cita del MLP, las 6 de la sección de pérdida y las 7 de backpropagation, se reescribieron las cards de la 1.4 y las 7 viñetas de conclusiones, se corrigió el encabezado de la tabla de la 2.6 y se retiró de esa diapositiva el destacado de faltantes que el presentador había borrado.
- Nota de render: las 16 SVG se inlinean como vector aunque final.md las referencie como .png; el build resuelve el hermano .svg. Las 5 imágenes de la biblioteca van embebidas como PNG en base64.
- Auditorías: degenerate_enum, field_coverage e image_coverage en verde. La primera pasada avisó que la 1.4 no entraba en la grilla editorial (cuerpo de 126 caracteres contra ~100); se acortaron las cards de "La función de pérdida" y "El error" en el modelo y la segunda pasada salió limpia.
- Pendiente cosmético heredado: el ícono 'remove_red_eye' no resuelve y cae a 'info'. Viene de rondas anteriores.
- Files created/modified: final.md, draft.md (una corrección numérica), images/ (5 SVG+PNG nuevos, 7 juegos renombrados, 5 PNG de la biblioteca), images/.critique/ (5 logs), output/slide-model.json, output/html/index.html, /index.html
- Pending open questions: la duración sigue sin resolverse y ahora el mazo renderiza 58 diapositivas. Siguen abiertas la notación y/t, la atribución de la cita de la 5.1 y las dos imágenes de ambiente.

## 2026-08-21 — Step 5 (Review — ronda tardía sobre Step 8)
- Status: complete
- Asks log: none (bullet inequívoco, no requirió resolución)
- What was decided: Se quitó la segunda línea de la diapositiva 3 ("Qué es un MLP"): "Es la arquitectura más simple que merece el nombre de red neuronal, y sigue siendo el bloque final de muchas CNN." La diapositiva queda como cita pura con la definición del MLP. La tercera nota del orador apuntaba a "la segunda línea"; se reescribió para no referenciar texto ausente, conservando el contenido.
- Key inputs: pedido del presentador en chat.
- Files created/modified: draft.md (contenido + notas + bullet [closed] en Presenter feedback de la sección 3), final.md (mismo cambio aplicado en sitio), output/slide-model.json, output/html/index.html
- Pending open questions: none

## 2026-08-21 — Step 5 (Review — segunda ronda tardía) + Step 6 (Polish)
- Status: complete
- Asks log: none (los cuatro bullets eran inequívocos; el respaldo documental se resolvió con búsqueda, no con pregunta)
- What was decided: Reescritura completa de la sección 6 (backpropagation), que pasó de 7 a 10 diapositivas.
  - **Corrección de fondo.** La frase de apertura de la vieja 6.1 decía que el backward "ajusta cada peso", y es falso. Se fijó la regla editorial de la sección en el Goal: el backward produce valores intermedios que se acumulan; `W` y `b` cambian una sola vez, al cerrar el batch. Se barrieron las siete diapositivas viejas contra esa regla (6.2 frase, bullets y ASCII; 6.3 la loss es de una fila y se deriva el promedio del batch; 6.4 los tres factores como valores intermedios; 6.5 δ como valor intermedio que no sobrevive al batch; 6.6 lo que viaja son deltas; 6.7 el paso condicionado al cierre del batch más bullet nuevo; 6.8 acumulador y vaciado explícitos).
  - **6.1 nueva** — "Entrenar es buscar el mínimo de una función": superficie de error, arranque al azar, pasos que se acortan, mínimo marcado.
  - **6.9 nueva** — "El ciclo completo, batch a batch": ciclo de vida entero en un diagrama, acumular arriba / aplicar abajo / volver al batch siguiente.
  - **6.10 nueva** — "Qué mirar cuando esto se entrena": tabla síntoma-causa-perilla (5 filas) + gradiente que se desvanece, que explota, orden de las perillas y una por vez.
- Key inputs: **Respaldo documental agregado (pedido explícito).** PyTorch *Optimizing Model Parameters* (el bucle zero_grad / backward / step y "Gradients by default add up; to prevent double-counting, we explicitly zero them at each iteration"); Keras `Model.fit` (`batch_size` = "Number of samples per gradient update", definición de época); CS231n *Optimization* (paso en dirección negativa del gradiente; el gradiente del minibatch como aproximación del completo) y *Backpropagation*; Google ML Crash Course (descenso por gradiente como búsqueda de los pesos de menor loss); Pascanu, Mikolov y Bengio 2013 (desvanecimiento, explosión y recorte de norma); Keras `Adam` (`learning_rate` 0.001, `clipnorm`, `global_clipnorm`).
- **Hallazgo sobre las fuentes:** el presentador pidió reusar "un par de gráficos de la presentación de introducción" para la idea del mínimo. Se revisó `talks/intro-redes-neuronales` y **no existe ese gráfico**: sus imágenes del tema son fórmulas (coste L2, regla de la cadena, delta, paso de actualización) y están en inglés; la idea del valle aparece solo en prosa como la analogía de la pelota. Los cuatro diagramas de esta ronda son propios y en español.
- Files created/modified: draft.md (sección 6 completa + 4 bullets [closed] + Open questions de duración); final.md (regenerado desde draft.md por Polish); images/ — 4 SVG+PNG nuevos (`s6-1-1-descenso-al-minimo`, `s6-2-1-ciclo-forward-backward`, `s6-8-1-batches-y-epoca`, `s6-9-1-ciclo-batch-a-batch`) con sus sidecars `.ascii` y sus companions en `.critique/`; se purgaron por `gc` los dos stems huérfanos del numerado viejo (`s6-1-1-ciclo-forward-backward`, `s6-7-1-batches-y-epoca`).
- Nota de entorno: `cairosvg` no está instalado en el Python del sistema. Se rasterizó con un venv temporal en el scratchpad de la sesión. Si esto se repite en cada Polish, conviene un venv estable en el repo.
- Pending open questions: (1) **Duración: 51 diapositivas para 90 minutos**, contra 48 antes de esta ronda. Es el problema más serio del mazo y la decisión es del presentador (recortar o partir en dos). (2) Estilo de render por elegir; el deck HTML publicado quedó desactualizado.

## 2026-08-21 — Revisión Composer (scope=full) + fixes + Polish
- Status: complete
- Asks log:
  - 2026-08-21 — "Antes de moverte a html-strict. Que el editor revise en forma critica el contenido de la presentacion" → punch-list de 2 blockers, 6 majors, 1 minor
  - 2026-08-21 — "¿Cómo seguimos?" (4 opciones) → **Opción 2: aplicar todo menos la duración, incluida la tesis reescrita**
- What was decided: se aplicaron los 6 majors, el minor y el blocker de tesis. El blocker de duración queda abierto por decisión del presentador.
  - **Tesis (blocker).** El `Claim` decía "tres lugares" mientras 1.4 enumera seis decisiones y el mazo tiene ocho secciones; pérdida y backpropagation (16 diapositivas, 31% de la clase) quedaban fuera. Ahora: cuatro lugares de decisión, backpropagation declarado mecanismo y no decisión, medir y regularizar como cierre.
  - **L6 en la sección 6.** "Se acumula durante el batch y se aplica al cerrarlo" estaba como contenido visible en 6.2, 6.7, 6.8 y 6.9. Repartido por dueño: 6.2 enuncia, 6.7 aritmética del paso, 6.8 conteo, 6.9 ensamblado. Dos bloques a `Cut material`.
  - **L6 en 6.10.** Las filas de overfitting y de normalización repetían 8.1, 2.3 y las notas de 6.7; pasaron a puntero seco.
  - **Matemática contra API en 6.9.** El diagrama descompone `g += grad` por fila; en código `loss.backward()` es uno por batch y la suma es vectorizada. Aclaración agregada a las notas del orador.
  - **Títulos.** H1 de la sección 6 (36 → `Backpropagation`) y de la 8 (28 → `Overfitting`); ocho H2 sobre 40 caracteres reescritos. Ahora el mazo entero está dentro del presupuesto.
  - **Notas del orador.** Recortadas 6.1, 6.8, 6.9 y 6.10. Quedan 22 diapositivas sobre las 120 palabras, todas anteriores a esta ronda.
  - **L8, "gradiente".** Se usaba en 1.7 y 2.3 antes de definirse en 6.1; se agregó la glosa en su primer uso visible.
- **Override registrado:** la sección 6 queda en 10 diapositivas contra el ~8 de `principles.md`. Fusionar 6.4 con 6.5 rompe el presupuesto de densidad (dos imágenes de fórmula más seis bullets) y partir la sección agrega una divisoria a un mazo ya largo. El defecto cuesta menos que cualquiera de los dos remedios.
- Files created/modified: draft.md (tesis, sección 6, títulos, notas, Cut material, Open questions, 2 bullets [closed]); final.md (regenerado); dos SVG con `<title>` actualizado (s6-1-1, s1-2-1).
- Pending open questions: (1) **Duración, sin resolver y es el blocker.** 51 diapositivas para 90 minutos; las notas solas suman ~6.060 palabras, unos 50 minutos de narración pura sin preguntas ni transiciones ni los tres quizzes. (2) 22 diapositivas con notas sobre presupuesto, ligadas a lo mismo. (3) Render por disparar.

## 2026-08-21 — Step 7 (Render, html-strict)
- Status: complete
- Asks log:
  - 2026-08-21 — "¿Qué estilo de render?" → **html-strict**
  - 2026-08-21 — "Revisa si el mapping de slide al style es el mejor" / "Me gustaría explorar si es posible más diversidad" → auditoría de clasificación antes del FILL
- What was decided: se re-hizo el FILL entero desde `final.md` y se corrigió el mapeo. **Diagnóstico:** el modelo anterior mandaba 22 de 58 diapositivas a `content+cards+image`; dos de ellas eran el antipatrón que el catálogo nombra explícitamente (una tabla con imagen compartida colapsada en cards, que pierde la alineación por fila). El resto no era error de clasificación sino monocultivo de la fuente: casi toda diapositiva es "lead + un diagrama + 3 o 4 cards etiquetadas", y con esa forma la regla dispara bien.
- **Hallazgo clave del catálogo:** `design` + `media` son del *stage*, no de la plantilla, así que **cualquier** plantilla puede llevar el diagrama. La imagen nunca es motivo para elegir `content+cards+image`; el orden del discriminador pone `process` y `stat` **antes**. Eso desbloqueó la diversidad sin perder ningún diagrama.
- Reclasificaciones: 1.2 y 1.7 y 8.1 → `value-columns` (la tabla es el contenido); 1.4 (el lead dice "en este orden"), 1.5, 6.2, 6.4, 6.9 y C.2 (checklist, learnings L3) → `process`; 7.1 → `stat` (los números son el contenido).
- **Bug encontrado y corregido:** la 8.1 llevaba la imagen de la 8.2 duplicada (`s8-2-1-curvas-overfitting.png` en dos diapositivas seguidas). En `final.md` la 8.1 no tiene imagen. Quitada.
- Ajustes de densidad: 1.7 pasó de 4 columnas a 3 (fórmula y rango fusionadas) para conservar el diagrama sin que se apreten las celdas.
- Mapeo final (61 diapositivas): content+cards+image 16, concept-breakdown 12, value-columns 9, section-agenda 8, process 6, quiz 3, quote 2, stat 1, concept-columns 1, code-example 1, divider 1, closing-cta 1. **De 10 plantillas distintas a 12, y la dominante bajó de 38% a 26%.**
- Files created/modified: output/slide-model.json (re-FILL completo + sello de frescura), output/html/index.html, index.html raíz.
- Auditorías: `degenerate_enum` ok, `field_coverage` ok, `image_coverage` ok, render sin warnings.
- Pending open questions: el blocker de duración sigue abierto (51 diapositivas de contenido para 90 minutos).

## 2026-08-21 — Step 5 (Review, tercera ronda) + Polish + Render
- Status: complete (queda una pregunta abierta de ubicación)
- Asks log:
  - 2026-08-21 — "'La forma la decide la arquitectura' … debería ser datos de una tabla, imagen, señal, imagen RGB. Y dependiendo del dato cambia la arquitectura" / "Revisa ese slide y el ASCII"
  - 2026-08-21 — "Mover slide 7 después del slide 5" → aclarado por el presentador: era "Una neurona, en una línea" (posición 7 del deck renderizado, contando la portada), y el slide 5 es el quote "Qué es un MLP"
  - 2026-08-21 — "Quiero decir, 'Una neurona, en una línea' quedaría mejor como bullets numerados"
  - 2026-08-21 — "Borrar 'One-hot contra embedding: …'"
  - 2026-08-21 — "'Las activaciones ocultas' debería moverse a una sección Capas ocultas y agregar un par de slides con recomendaciones" → **pendiente de decidir dónde va la sección**
- What was decided:
  - **1.2 invirtió la causalidad.** De 'La forma la decide la arquitectura' (una imagen de 28x28 contra tres arquitecturas) a **'El dato decide la arquitectura'**: cuatro tipos de dato (tabla, señal 1D, imagen en grises, imagen RGB), su forma natural y la arquitectura que les corresponde. Diagrama rehecho de cero en cuatro paneles; el acento rojo está en el pill de MLP, que es el alcance de la clase. Se respetaron los tres [closed] previos: no se explica la convolución, RGB no son matrices apiladas sino tres números en el mismo píxel, y la declaración de alcance cierra la diapositiva.
  - **Reordenada la sección 1.** 'Una neurona, en una línea' pasó de la 5 a la 4, justo detrás del quote 'Qué es un MLP'; 'Lo que hay que diseñar' pasó a la 5. El orden ahora es definir el MLP, mostrar su átomo, y después la agenda de decisiones. Renombrado el diagrama `s1-5-1-neurona` → `s1-4-1-neurona`, y actualizadas las referencias cruzadas (notas de 6.10 y dos entradas de Open questions apuntaban a la vieja 1.4).
  - **La neurona pasó a bullets numerados** (cuatro pasos sin etiqueta, que el renderer numera) en vez de tres cards etiquetadas.
  - **Borrado el anticipo de one-hot contra embedding** en 'Una posición por variable'. El texto que el presentador citó estaba en el modelo como *highlight*, no como bullet del cuerpo: por eso lo veía en el deck y no en el borrador. Aprovechando el pase, 'El largo no cambia' salió de las cards de la tabla (donde estaba mezclado con las filas de tipos de dato) y pasó a highlight.
- Files created/modified: draft.md, final.md, images/s1-2-1-formas-de-input.{svg,png,ascii} (rehecho), images/s1-4-1-neurona.* (renombrado), output/slide-model.json, output/html/index.html.
- Pending open questions: (1) **Dónde va la sección Capas ocultas.** (2) El blocker de duración, sin resolver, y la sección nueva lo empeora (+3 diapositivas).

## 2026-08-21 — Step 5 (cuarta ronda: dos cambios estructurales) + Polish + Render
- Status: complete
- Asks log:
  - 2026-08-21 — "¿Dónde va la sección Capas ocultas?" (3 opciones) → **opción 1: al final, justo antes de Overfitting**
  - 2026-08-21 — "Mover 'La diferencia sutil…' y 'Augmentation solo en train…' a un slide Does and don'ts y expandir con tips claves"
- What was decided:
  - **Sección 8 nueva, Capas ocultas**, entre 'Medir un clasificador' y 'Overfitting' (que pasó a 9). Tres diapositivas: 'Cuántas capas y cuánto ancho' (nueva), 'Las activaciones ocultas' (movida desde la 1.7) y 'Cómo arrancan los pesos' (nueva). Tapa un agujero real: 'Lo que hay que diseñar' promete seis decisiones y la sexta era la única sin sección. Las dos nuevas salen del corpus (§ arquitectura: 1–3 capas para tabular, ancho potencia de 2 decreciente, tabla de punto de partida por cantidad de datos, el procedimiento de mirar el error de train; § normalización: el efecto multiplicativo c^10, Xavier/He eligen Var(W) para c≈1). La sección 1 quedó en 6 diapositivas.
  - **Diapositiva 3.5 'Qué hacer y qué no'**, cierre de la sección 3, plantilla `pros-cons`. Los dos puntos citados se movieron ahí y se sumaron cinco tips nuevos (partir antes de explorar, partir por grupo, fijar la semilla y guardar el split, no re-partir cuando el número no cierra, no confiar en el default de `train_test_split`). Se cuidó no repetir 3.3 ni 3.4: esas explican los modos de falla, esta da las reglas operativas.
- **Nota de plantilla:** `pros-cons` toma `pros`/`cons` como **listas planas de strings** (las une con ' · ') más `pro_label`/`con_label`. No acepta items con cuerpo. Por eso la 3.5 quedó glanceable —siete líneas cortas— y las explicaciones bajaron a las notas del orador, que es lo que pide `principles.md`.
- **Falso positivo de auditoría:** `field_coverage` reporta `pro_label`/`con_label` como campos ignorados en `pros-cons`, pero el template los consume y el deck los renderiza correctamente ('Qué hacer' / 'Qué no hacer' en vez de los defaults 'Ventajas' / 'Riesgos'). Es la lista de campos de la auditoría la que está desactualizada, no la diapositiva. No tocar.
- Renombres de diagramas: `s8-2-1-curvas-overfitting`→`s9-2-1`, `s8-3-1-objetivo-l2`→`s9-3-1`, `s1-7-1-activaciones-ocultas`→`s8-2-1` (en ese orden, para evitar colisión de stems).
- Referencias cruzadas actualizadas: nota de la 5.2 y fila de la tabla de 6.10 apuntaban a la vieja sección 8 (Overfitting), ahora 9; la 1.4 ya no dice "al cierre de esta sección" sino "en la sección 8".
- Mapeo final (65 diapositivas): content+cards+image 17, concept-breakdown 13, value-columns 9, section-agenda 9, process 6, quiz 3, quote 2, y una cada uno de pros-cons, stat, concept-columns, code-example, divider y closing-cta. **13 plantillas distintas.**
- Pending open questions: **el blocker de duración pasó de serio a crítico.** 54 diapositivas de contenido para 90 minutos; las notas suman 6.706 palabras, ~52 minutos de narración pura sin preguntas, sin transiciones y sin los tres quizzes. Hay que recortar o partir la clase en dos.

## 2026-08-21 — Fix de la diapositiva 1.2 (revision de densidad)
- Status: complete
- Asks log: 2026-08-21 — "Revisa el slide 4 que quedo mal." (posicion 4 del deck renderizado, contando la portada = 'El dato decide la arquitectura')
- Diagnostico: la diapositiva llevaba **el diagrama de cuatro paneles y una tabla de 3x4 que decia lo mismo**, mas el lead y el remate de alcance. Cuatro bloques contra el presupuesto de `principles.md` (un callout, un table-or-diagram, un bloque de apoyo). Con el diseno en banda el diagrama quedaba en una franja angosta y sus etiquetas ilegibles.
- Fix: **se retiro la tabla**, que era duplicacion dentro de la misma diapositiva, y se archivo en `Cut material`. El matiz que solo estaba ahi (en una imagen importa que pixel esta al lado de cual) paso a las notas del orador. Plantilla de `value-columns` a `content-image`, diseno `banded`, sin `facts`: el diagrama se queda con todo el ancho.
- **El fix se hizo en la fuente, no en el modelo del render.** Es lo que manda `principles.md` en *Pipeline discipline*: una diapositiva sobrecargada es un defecto de Step 4 que aparece tarde, y arreglarlo achicando en el renderer garantiza que vuelva en el proximo render.
- Files created/modified: draft.md (tabla retirada, lead y remate acortados, notas ampliadas, bullet [closed], entrada en Cut material), final.md, output/slide-model.json, output/html/index.html.

## 2026-08-21 — Perdida de un cambio por buffer viejo del editor + fix definitivo de la 1.2
- Status: complete
- Asks log:
  - 2026-08-21 — "Revisa si se perdio el cambio" → auditoria de los 13 cambios de la sesion contra draft.md, final.md y el deck
  - 2026-08-21 — "El problema es el texto del alcance de la clase. deja solo el diagrama en el slide"
- **Hallazgo de proceso, importante para futuras sesiones.** El fix de densidad de la 1.2 se aplico a las 15:25 y se perdio: `draft.md` volvio a escribirse **a las 18:04** desde un buffer viejo del editor del presentador, con la tabla de nuevo y el lead sin acortar. Las otras 53 diapositivas quedaron intactas, porque el buffer era posterior a todo lo demas y solo anterior a ese ultimo fix. **Regla practica: cuando el presentador tiene `draft.md` abierto en el IDE, cualquier escritura del agente puede quedar pisada por un guardado del editor.** Conviene pedirle que cierre o recargue el archivo antes de una ronda de edicion, y verificar `mtime` de draft.md contra la hora de la ultima escritura del agente antes de dar un cambio por aplicado.
- **Falsos positivos de la auditoria, para no volver a alarmarse:** buscar el texto eliminado en `draft.md` da positivo porque el log de `Presenter feedback` **cita el texto retirado verbatim** en el bullet `[closed]`. Es el audit trail funcionando. Hay que buscar en el contenido vivo (fuera de los bullets de feedback y fuera de `Cut material`), no en el archivo entero.
- Fix definitivo de la 1.2: **queda solo el diagrama**. Se retiro la tabla de 3x4 (archivada en Cut material) y el presentador ya habia retirado a mano el parrafo de alcance (tambien archivado). La diapositiva quedo en titulo, lead y diagrama a pantalla completa, plantilla `image-full`. Lo que decia la tabla y no dice el dibujo (la vecindad en imagenes, el orden en senales) y la declaracion de alcance pasaron a las notas del orador; el alcance sigue visible en el pill de MLP acentuado del diagrama.
- Files created/modified: draft.md, final.md, output/slide-model.json, output/html/index.html.

## 2026-08-21 — Reconstruccion de la 1.6 (slide 8) y correccion de fondo
- Status: complete
- Asks log:
  - 2026-08-21 — "Tomando el slide 4, reconstruir la 8 que muestre como esos diagramas se mapean a nodes de entrada"
  - 2026-08-21 — "Creo que imagen RGB no esta bien porque cada uno se mapea a una arquitectura distinta, y asi en un caso en realidad se preserva y no se aplana" / "en caso de imagen RGB se mapean dejando las matrices, y de ahi que MLP no sirve"
  - 2026-08-21 — "Seria importante en el diagrama marcar tambien que tipo de arquitectura es cada una para evitar confusiones"
- **Correccion de fondo, marcada por el presentador.** La primera version del diagrama aplanaba los cuatro casos por igual, y eso era falso: **aplanar es un requisito del MLP, no del dato**. La diapositiva anterior (1.2) dice que cada dato tiene su arquitectura natural, y esta la contradecia mostrando senal, imagen y RGB como columnas de nodos sueltos. Una CNN conserva la grilla y el canal; una RNN conserva el orden.
- Version final: el eje del diagrama es **que recibe la red**. Tabla, 13 nodos sueltos que el MLP toma tal cual. Senal, una secuencia de 300 pasos en orden. Imagen en grises, una matriz intacta. RGB, **tres matrices de 28x28 una por canal, dibujadas una al lado de la otra** (nunca apiladas ni con tercer eje espacial, per el [closed] previo). Cada panel lleva su **pill de arquitectura** igual que el diagrama de la 1.2, con MLP en rojo como unico acento. El conteo de nodos que se habia pedido bajo al pie, como el precio de aplanar los tres ultimos: 300, 784 y 2.352 entradas sueltas, y lo que eso borra.
- Se retiro la tabla 'Tipo de dato / Como se convierte en input' (archivada en Cut material): era un anticipo mas pobre de la 2.6 'La tabla de decisiones', que recorre el mismo eje con diez filas y ademas dice cuantos floats ocupa cada codificacion. Duplicacion L6.
- Plantilla `content-image` con diseno `banded`, siguiendo la leccion de la 1.2: un solo bloque visual mas los destacados, nunca diagrama y tabla juntos.
- **Trampa que volvio a aparecer:** el caracter U+22EE (elipsis vertical) rasteriza como tofu con cairosvg, per la regla de glifos Unicode de `diagram-style.md`. Se reemplazo por tres circulos dibujados. Verificado que ningun otro SVG del mazo usa glifos de ese grupo.
- Files created/modified: draft.md, final.md, images/s1-6-1-nodos-de-entrada.{svg,png,ascii}, output/slide-model.json, output/html/index.html.

## 2026-08-21 — La 1.6 (slide 8), version final: el traspaso al modelo
- Status: complete
- Asks log:
  - 2026-08-21 — "Deberia verse como la matriz y como pasa al modelo que toma el input"
  - 2026-08-21 — "El del MLP quedo bien, el resto no"
  - 2026-08-21 — "Seria importante marcar tambien que tipo de arquitectura es cada una"
- What was decided: el diagrama paso de cuatro paneles en dos filas a **cuatro filas de traspaso**, con dos columnas rotuladas, EL DATO y EL MODELO QUE LO TOMA. La correccion que pedia el presentador: en la version anterior solo la fila de la tabla mostraba el traspaso (dato mas flecha mas nodos) y las otras tres se quedaban en el dato, sin llegar al modelo. Ahora las cuatro cruzan, con la leyenda del traspaso sobre la flecha, y del lado derecho **se dibuja el modelo con la forma de su entrada**: el MLP con sus tres capas y los rotulos entrada, ocultas y salida; la RNN con tres pasos encadenados; la CNN con la grilla entera; y la CNN de RGB con las tres matrices juntas. Cada bloque lleva su pill de arquitectura adentro y el del MLP es el unico acentuado.
- El costo de aplanar (300, 784 y 2.352 entradas sueltas) quedo en el pie, separado por una regla.
- El ASCII de `draft.md` se reescribio para reflejar el diagrama nuevo, no solo el SVG: la fuente y el dibujo dicen lo mismo.
- **Aprendizaje de proceso que conviene recordar:** cuando el presentador pide un diagrama de traspaso, el eje util no es "que forma tiene el dato" sino "que recibe el modelo". La primera version fallo por quedarse del lado del dato en tres de los cuatro casos.
- Files created/modified: draft.md, final.md, images/s1-6-1-nodos-de-entrada.{svg,png,ascii}, output/slide-model.json, output/html/index.html.

## 2026-08-21 — Fix de encuadre en el diagrama de la 1.6
- Status: complete
- Asks log: 2026-08-21 — "Fijate que el texto de CNN en imagen de grises esta fuera de la caja."
- Diagnostico: el pill de CNN de la fila de imagen en grises estaba en y=386 con alto 22, y la caja del modelo termina en y=406: se salia dos pixeles por abajo. Ademas estaba en una posicion distinta a la del pill de la fila de RGB, asi que las cuatro filas no leian parejas.
- Fix: el pill paso a x=616 y=375, que es el mismo margen inferior y el mismo borde derecho que usa la fila de RGB.
- Se agrego un chequeo programatico que recorre todos los rect del SVG y verifica que ninguno se salga de su bloque contenedor. Dio limpio en las cuatro filas. **Conviene repetirlo en cualquier diagrama con cajas anidadas antes de dar por bueno el render:** el validador de SVG comprueba el viewBox y el aspecto, no el encuadre de los elementos entre si.
- Files created/modified: images/s1-6-1-nodos-de-entrada.{svg,png}, output/html/index.html.

## 2026-08-21 — Alineacion de los pills de arquitectura en la 1.6
- Status: complete
- Asks log: 2026-08-21 — "Fijate tambien que queden realmente tal vez como solapado en el borde el tipo de red o derecha abajo para MLP y RNN/CNN 1D"
- Diagnostico: los cuatro pills estaban en posiciones distintas. Los dos CNN ya estaban abajo a la derecha, pero el de MLP estaba al medio del bloque con su leyenda al lado, y el de RNN al medio a la izquierda. Ademas la leyenda del MLP ("un nodo por / variable ya codificada") arrancaba en x=592 y se pasaba del borde derecho del bloque.
- Fix: se unifico en **abajo a la derecha** para los cuatro, que es donde ya estaban los CNN, con el mismo par de margenes: 22 px del borde derecho y 9 px del inferior. Verificado programaticamente fila por fila. La leyenda del MLP se corrio a x=524 y se rebalanceo en dos lineas para que entre en el bloque.
- Se descarto la variante de pill solapando el borde: los CNN ya definian el patron de adentro-abajo-derecha y cambiarlo obligaba a mover tres para acomodar uno.
- Files created/modified: images/s1-6-1-nodos-de-entrada.{svg,png}, output/html/index.html.

## 2026-08-21 — Diagrama de la 1.6, version aprobada: procesamiento por partes
- Status: complete — el presentador aprobo ("Perfecto")
- Asks log:
  - 2026-08-21 — "En CNN el concepto de sliding estaria bueno modelarlo"
  - 2026-08-21 — "En las matrices una caja que muestre que se procesa de partes"
  - 2026-08-21 — "Creo que en el caso de senal es realmente una matriz de una linea, un vector"
  - 2026-08-21 — "Pero cuando pasa al CNN se toma de slices"
  - 2026-08-21 — "Perfecto. Genera el index ahora."
- What was decided: tres cambios sobre el diagrama de traspaso.
  1. **La senal paso de cajas sueltas a una matriz de una sola fila** (una tira con divisiones), rotulada "1 x 300: una matriz de una sola fila, o sea un vector". Mas preciso, y empareja las cuatro filas: ahora son todas matrices salvo la de la tabla.
  2. **Se modelo el recorrido por partes en las tres filas no-MLP**: ventana en rojo con la posicion actual en linea llena y las siguientes punteadas, mas flecha de recorrido debajo. En la senal es un slice de pasos consecutivos; en grises una ventana sobre la grilla; en RGB la misma ventana en el mismo punto de los tres canales, unidas por linea punteada.
  3. **El contraste quedo explicito del lado del MLP**, que ahora dice "los toma todos a la vez". Ese es el eje del diagrama: el MLP procesa todo junto, los otros tres recorren.
- Se mantuvo el limite del [closed] previo sobre convoluciones: se muestra **que** la ventana recorre, nunca **como** se calcula una convolucion.
- El ASCII de `draft.md` se reescribio junto con el SVG, asi que fuente y dibujo dicen lo mismo.
- Files created/modified: draft.md, final.md, images/s1-6-1-nodos-de-entrada.{svg,png,ascii}, output/slide-model.json, output/html/index.html, index.html (raiz).

## 2026-08-21 — Acronimos por su significado, simetria 4/8, y diagrama de house pricing en la 2.1
- Status: complete
- Asks log:
  - 2026-08-21 — "Pone no CNN o MLP o RNN en los graficos sino lo que significa"
  - 2026-08-21 — "Tal vez seria bueno seguir el layout del slide 8 en vez de cajas" / "Me refiero al slide 4 como para que queden simetricos"
  - 2026-08-21 — "La frase sobre el paso de la columna al numero se puede borrar, ya se explico antes"
  - 2026-08-21 — "Poner una imagen al costado del slide 10 que muestre la representacion visual con el caso que seguimos de house pricing"
- What was decided:
  - **Acronimos fuera de los dos diagramas.** MLP pasa a "Perceptron multicapa", CNN a "Red convolucional", RNN / CNN 1D a "Red recurrente o convolucional 1D". Tambien en el pie del diagrama de la 1.6. **El pedido tiene fundamento tecnico:** el diagrama de la 1.2 usaba los tres acronimos y la definicion de MLP recien llega en la 1.3, o sea la diapositiva siguiente. Es exactamente el caso de `learnings.md` L8, un termino tecnico usado antes de definirse.
  - **El diagrama de la 1.2 se rehizo con el layout de la 1.6** para que el par se lea igual: cabecera de dos columnas, cuatro filas, bloque a la derecha, pill abajo a la derecha, acento rojo en la fila tabular. Se diferencian por la columna derecha: la 1.2 responde **que forma tiene** (cuantos ejes) y la 1.6 responde **que recibe el modelo** y como lo procesa.
  - **2.1**: se retiro el parrafo de cierre sobre el paso de columna a numero (archivado en Cut material); la 1.6 ya lo muestra con numeros y la seccion 2 entera es ese desarrollo. En su lugar lleva un diagrama al costado (`split-right`) con el caso de house pricing: la misma tabla de casas dos veces con las dos primeras columnas intercambiadas, el remate "es el mismo dato", y el contraste de que en una imagen mover un pixel si cambia el dato. Es la ilustracion literal de lo que la diapositiva afirma.
  - Plantilla de 2.1 corregida de `concept-breakdown` a `content+cards+image`: el catalogo exige `images == 0` para concept-breakdown, y la diapositiva ahora tiene diagrama.
- Files created/modified: draft.md, final.md, images/s1-2-1-formas-de-input.{svg,png,ascii} (rehecho), images/s1-6-1-nodos-de-entrada.{svg,png}, images/s2-1-1-orden-de-columnas.{svg,png,ascii} (nuevo), output/slide-model.json, output/html/index.html, index.html raiz.

## 2026-08-21 — Notebook de acompanamiento: tipos de dato y sus conversiones
- Status: complete
- Asks log (la forma final salio de seis pedidos sucesivos):
  - "Creemos un notebook que muestre realmente una red simple pero que ejemplifique el slide 15 y los tipos de datos y sus conversiones" (slide 15 = 2.6 'La tabla de decisiones')
  - "Para el dataset, graba un file en disco. No generamos codigo en la notebook que es confuso"
  - "Tipo por tipo mostremos que es lo que se deberia hacer. Mostrar un arreglo con los valores de ese tipo es suficiente"
  - "Explicamos caso por caso con una red neuronal que procesa solo un parametro y infiere el precio" / "Despues al final podemos combinar todo"
  - "La seccion 0 Preparacion no parece necesaria" / "Usa keras simple por mas que sea algo repetitivo"
  - "Dejemos todo en el CSV, carguemos lo que se esta buscando e imprimamos en un bloque que se vea lo que se cargo y el precio" / "En SGD sin normalizar seria bueno mostrar un grafico con la comparacion" / "El bloque que hace SGD y SGD no normalizado, partilo"
- Entregable: `missions/clase3/tipos-de-datos.ipynb` (57 celdas, ejecutado, 3 figuras), `missions/clase3/casas.csv` (2000 filas, 22 columnas) y `missions/clase3/generar-casas.py`.
- Forma final: diez secciones, una por fila de la tabla de decisiones. Cada una **carga del CSV su columna y su precio**, imprime el bloque cargado, muestra `valor -> floats`, y entrena una red que recibe solo esa variable. Donde hay forma incorrecta, entrena la misma red con esa forma y compara. Keras plano en cada celda, sin helpers, a pedido. La seccion 11 combina todo con el precio completo.
- **Decision de diseno clave: el CSV trae dos clases de precio.** `precio` (completo, ruido 18.000) y diez columnas `precio_solo_*` (el aporte aislado de cada variable, ruido 4.000). Sin eso los experimentos por variable no discriminan: con el precio completo los metros cuadrados tapan a todas las demas y ningun efecto chico se distingue. El piso de los experimentos aislados es ~$3.200, y las codificaciones correctas llegan justo ahi.
- **Decision de alcance:** el dataset es sintetico y NO es el de la mision. `mission.md` dice que encontrar las trampas de codificacion en `house-prices-extended.csv` es trabajo del alumno; un notebook que resolviera esa tabla seria la solucion servida.
- Hallazgos al calibrar, que valen para futuras versiones:
  - Con `Adam(0.001)` y pocas epocas las redes minimas **no llegan** a un target de ~200 partiendo de cero. Con `Adam(0.01)` y 300 epocas convergen sin escalar el target.
  - **La normalizacion no se demuestra con una sola variable ni con Adam.** Hacen falta dos variables de escalas distintas compitiendo, y SGD: sin normalizar la red se queda exactamente en el baseline ($50.983 contra baseline $50.984), con z-score baja a $3.191. Con Adam la diferencia casi desaparece ($3.238 contra $3.098), y eso quedo escrito como matiz honesto.
  - **El identificador unico no memoriza si entra como numero** (train ≈ test ≈ baseline: no aporta nada). Memoriza cuando entra **como categoria con embedding**: train $0, test $36.594 contra baseline $3.762. El notebook muestra los dos casos.
- Resultado de cierre: la entrada suma 28 floats y coincide con la tabla; MAE $16.550 contra un piso de $14.362; con todo mal codificado (mismas escalas, semantica equivocada) sube 50%.

## 2026-08-21 — Notebook: tipos declarados al cargar, y la seccion 2 a 10 epocas
- Status: complete
- Asks log:
  - 2026-08-21 — "Reducir tal vez en numerica con magnitud a 10 epochs para ver la convergencia lenta"
  - 2026-08-21 — "Tal vez al cargar la matriz realizar tambien todas las conversiones de string al tipo que corresponde para no tener que hacerlo de nuevo"
- What was decided:
  - **`read_csv` con `dtype=` explicito**, y una markdown nueva que dice por que: media tabla de decisiones se escribe ahi. Tres declaraciones que ya son decisiones de modelado: `codigo_postal` como `category` y no como entero (pandas lo leeria `int64` sin protestar); `estado` como categoria **ordenada** con `pd.Categorical(..., ordered=True)`, porque el orden lo pone el dominio y no los datos; `barrio` y `tipo_vivienda` como `category`, que ya traen su lista de valores y su indice entero.
  - Las secciones dejaron de reconstruir diccionarios: usan `.cat.codes`, `.cat.categories`. Para tratar el codigo postal como numero ahora hay que forzar `.astype("int64")`, y eso mismo es una senal.
  - **Distincion que quedo escrita en el codigo:** declarar el tipo al cargar dice *que es* cada columna; los diccionarios que el modelo usa son *parametros* y siguen saliendo solo del train (seccion 11).
  - Seccion 2 pasa a **10 epocas** para que se vea la convergencia lenta, mas una celda nueva que repite a 300 para contestar la pregunta obvia.
- **Correccion de texto importante:** a 10 epocas la version sin normalizar no queda "pegada al baseline" sino **muy por encima** ($154.275 contra un baseline de $50.984): la red arranca cerca de cero y todavia esta subiendo hacia el rango del precio. El texto decia lo contrario y se corrigio. A 300 epocas si queda clavada en el baseline ($50.983 contra $50.984), que es el remate.
- Files created/modified: missions/clase3/tipos-de-datos.ipynb (60 celdas, 3 figuras), y el generador del notebook en el scratchpad de la sesion.

## 2026-08-21 — Layout de la 1.2 y una regresion encontrada en el modelo
- Status: complete
- Asks log: 2026-08-21 — "Recargar el plugin" / "Slide 'El dato decide la arquitectura'" / "revisar que el diagrama mejor vaya a la derecha y luego el texto" / "No parece el layout ser el correcto"
- **Plugin:** unica version instalada, `talksmith` 0.83.4, spec del 2026-08-12 16:51. Cache y marketplace **identicos** (`cmp` sin diferencias), repo en `32adc17`. No habia nada nuevo que cargar. Para traer una version mas nueva hace falta `/plugin update talksmith` del lado del presentador.
- **Diagnostico del layout, que era de proporciones y no de plantilla.** Los diagramas de las diapositivas 4 y 8 del deck tienen viewBox 720x570, o sea **ratio 1.26**, casi cuadrado, contra un lienzo de **1.78**. El resto de los diagramas del mazo va de 2.0 a 4.0. Con `image-full` una imagen de 1.26 queda limitada por la altura y ocupa alrededor del 55% del ancho, dejando dos franjas vacias a los costados. **Un diagrama casi cuadrado pide ir al costado del texto, no a pantalla completa.**
- Fix: la 1.2 paso a `content-image` con diseno `split-right` (diagrama a la derecha) y tres lineas cortas a la izquierda, escritas nuevas. No se recupero la tabla archivada en Cut material: eso volveria a sobrecargarla, que fue el defecto original.
- **Regresion encontrada de paso, no introducida por este cambio.** El modelo del deck traia dos diapositivas alteradas fuera de mis ediciones:
  - **'La matriz de confusion' con `template: matrix`**, una plantilla **que no existe** en el catalogo. El render la mandaba a `fallback` y la diapositiva **habia perdido su diagrama**. Restaurada a `content+cards+image` con `split-right`, sus cuatro cards (TP, FP, FN, TN) y su imagen.
  - **'El 99% de accuracy'** tenia `cards` y `stats` a la vez bajo `content+cards+image`, que no dibuja `stats`. Se retiro el campo huerfano.
- **Aprendizaje:** el warning `unknown template ... -> fallback` de `build_html.py` es el unico que delata una plantilla inventada, y se pierde facil si se filtra la salida del render. Conviene grepear siempre por `warning|unknown|fallback` despues de renderizar, no solo por la linea final.
- Verificado tras el fix: 0 diapositivas en fallback, `image_coverage` ok, `degenerate_enum` ok.

## 2026-08-21 — Icono de Train, slides 19 y 20 rotas, y rename del notebook
- Status: complete
- Asks log:
  - 2026-08-21 — "El icono de Train es de entrenar no de tren"
  - 2026-08-21 — "Todo se aprende solo del train la imagen no se esta renderizando" / "El slide 19 y 20"
  - 2026-08-21 — "renombrar tipos-de-datos a input-data-types y el csv que tambien tenga el mismo nombre"
  - 2026-08-21 — "Generar datos no parece ser necesario, ya se genero el file y lo usamos siempre"
- **Icono.** La card 'Train' de 'Un dataset, tres trabajos distintos' recibia el icono automatico `train`, que es una locomotora. El picker de iconos resuelve por texto y ahi la palabra es ambigua en ingles. Se fijo `icon: "model_training"` explicito en el modelo; verificado que se cacheo `model_training.outlined.svg` en lugar de `train.outlined.svg`. **Las cards aceptan `icon` explicito**, es la salida para cualquier otro caso ambiguo.
- **Segunda tanda de la misma regresion del modelo.** Las diapositivas 19 y 20 del deck (3.3 y 3.4) tenian `media: {code, language}`, una forma **inventada**: el schema solo acepta `{src, alt}`. El resultado era una media vacia con `design: split-right`, o sea media pantalla en blanco y el codigo sin dibujarse. Es el mismo tipo de error que el `template: matrix` de la ronda anterior.
  - 19 'Todo se aprende solo del train' -> `code-example` con `code` + `language` + tres `explanation`. El bloque MAL/BIEN es el contenido de esa diapositiva, asi que el codigo manda.
  - 20 'Los errores que arruinan la medicion' -> `concept-breakdown` sin la media rota. Ahi los cinco errores son el contenido y el snippet es secundario.
- **Rename:** `tipos-de-datos.ipynb` -> `input-data-types.ipynb`, `casas.csv` -> `input-data-types.csv`. Se elimino `generar-casas.py` por pedido del presentador: el CSV ya esta generado y es el que se usa siempre. La procedencia (dataset sintetico, aporte por variable, ruido 18.000 en el precio completo y 4.000 en los aislados) paso al markdown del notebook, para que no se pierda al sacar el script.
- **Regla que conviene fijar:** despues de cada render hay que grepear la salida por `warning|unknown|fallback`, y ademas revisar que ninguna diapositiva tenga `media` sin `src`. Las dos regresiones de hoy eran invisibles en el deck salvo por un hueco en blanco.


## 2026-08-24 — Slide 15 (2.6 La tabla de decisiones): fuera la bajada de floats, entra "¿Qué es?"
- Status: complete
- Asks log:
  - 2026-08-24 — "borrar 'La última columna cuenta floats, no neuronas: ...'" y "agregar en slide 15 en la tabla una descripción de los tipos de datos. No es claro qué es por ejemplo 'Numérica con magnitud' vs 'Numérica con cola larga'"
- What was decided:
  - **Se quitó el highlight `definition` de la 2.6** (el párrafo floats-no-neuronas) del modelo del deck y el párrafo equivalente de `final.md` y `draft.md`. **No se tocaron las notas del orador**, que ya traían la misma explicación como respuesta preparada por si alguien pregunta; era una redundancia entre diapositiva y notas y quedó solo en las notas.
  - **Columna nueva `¿Qué es?`** insertada en segundo lugar (entre `Variable` y `Ejemplo`), once celdas de 3 a 5 palabras. El problema que resolvía era exactamente el par que marcó el presentador: "Numérica con magnitud" → *Número en un rango parejo* contra "Numérica con cola larga" → *Número con pocos valores enormes*. El resto sigue el mismo eje: ordinal *con orden, sin distancia*; nominal baja/alta *pocas* contra *muchas*; código *etiqueta escrita como número*; identificador *distinto en cada fila*.
  - Las descripciones se escribieron cortas a propósito: `.chead`/`.crow` es un grid de columnas iguales (`repeat(var(--cc),1fr)`), así que pasar de 4 a 5 columnas le saca 20% de ancho a cada una. Una descripción de una línea larga habría empujado el `.cfit` a achicar toda la tabla.
- Nota de layout: la bajada dice "la columna del medio es la única decisión" y sigue siendo cierta — con 5 columnas la del medio es literalmente `Codificación`.
- Files created/modified: draft.md, final.md, output/slide-model.json (re-stampeado con `model_freshness.py stamp`), output/html/index.html, index.html raíz.
- Verificado: render sin `warning|unknown|fallback`, `--cc:5` con los 5 encabezados, y 0 ocurrencias del párrafo borrado en el HTML.
- **Falsa alarma que conviene dejar escrita.** Marqué como rotas las diapositivas 'Cuántas capas y cuánto ancho' y 'El resto del arsenal, y cuál usar' porque tienen `media` sin `src`, aplicando la regla del 2026-08-21. **No están rotas: las dos dibujan su tabla.** Ver la entrada de correccion de abajo.

## 2026-08-24 — Correccion: `media` sin `src` ya no es sintoma de nada (plugin 0.84.0)
- Status: complete
- **La regla del 2026-08-21 quedo vencida el mismo dia que se escribio.** Decia: "revisar que ninguna diapositiva tenga `media` sin `src`". Era cierta contra el plugin **0.83.4**, donde `media` solo aceptaba `{src, alt}` y cualquier otra forma dejaba media pantalla en blanco. El plugin instalado hoy es **0.84.0**, y `_macros.j2` (mtime 2026-08-21 23:08, cinco minutos despues de aquel render) trae `smedia`, un macro **polimorfico** que despacha por forma:
  - `{src, alt}` → imagen
  - `{code, language?}` → panel de codigo `.codebox.mcode`
  - `{columns:[{header,cells}]}` → grilla `.compare.mtable`
  Y `_design()` ademas asciende `column-*`/`bleed` a `split-*` cuando la media es codigo o tabla, para no recortar algo que hay que leer.
- **Consecuencia:** las dos diapositivas con `media: {columns: [...]}` **renderizan bien** — verificado, dos `.compare.mtable` con `--cc:2` dentro de `.smedia`, en la mitad derecha de un `split-right`. Cards a la izquierda, tabla de apoyo a la derecha, que era la intencion original del autor.
- **Regla nueva, que reemplaza a la vieja:** despues de renderizar seguir grepeando la salida por `warning|unknown|fallback`, que sigue siendo el unico delator de una plantilla inventada. **No** chequear `media` sin `src`: hoy `{code}` y `{columns}` son formas legitimas. Lo que si es sintoma es `media` que no sea ninguna de las tres formas (ni `src`, ni `code`, ni `columns`) — ahi `build_html.py` avisa "the slide carries no media to place" y degrada el design a `full`.
- **Aprendizaje de fondo:** una regla de diagnostico escrita contra una version del renderer caduca cuando el renderer gana una capacidad. Vale anotar la version contra la que se escribio. La del 2026-08-21 no la tenia y por eso sobrevivio a su utilidad.

## 2026-08-24 — Fuera la nota de augmentation en 'Los tres, lado a lado'
- Status: complete
- Asks log:
  - 2026-08-24 — "Borrar 'Augmentation solo en train. Validación y test se quedan con los datos originales. El preprocesamiento, en cambio, se aplica a los tres.'"
- What was decided: se quitó el highlight `note` de la diapositiva **'Los tres, lado a lado'** (2.2). Era un resto: el 2026-08-21 el presentador pidió mover esa línea y 'La diferencia sutil…' a la diapositiva 'Qué hacer y qué no'; el movimiento se aplicó en `final.md`/`draft.md` pero **el modelo del deck se quedó con las dos**, así que la línea seguía apareciendo en el HTML aunque el markdown ya no la tuviera.
- **No se tocó nada de la 2.5 'Qué hacer y qué no'**, que es donde la regla vive ahora: sigue el ítem `Augmentation solo en train` en la columna *Qué hacer* y sigue su desarrollo completo en las notas del orador (con la distinción contra preprocesamiento, que es la parte que se confunde). Tampoco se tocó la fila `Augmentation | Sí | No | No` de la tabla, que dice lo mismo en forma de dato.
- **Resto del mismo tipo, todavía en pie:** el highlight `important` 'La diferencia sutil está entre validación y test…' sigue en el modelo de la 2.2 y tampoco está en `final.md`. Es la otra mitad de aquel pedido de mover. Queda a la espera de que el presentador decida.
- **Patrón que conviene mirar:** cuando una edición mueve contenido entre diapositivas, hay que aplicarla en `final.md`/`draft.md` **y** en `output/slide-model.json`. El markdown y el modelo pueden divergir sin que ningún chequeo avise: `model_freshness` compara hashes de archivo completo, no contenido diapositiva por diapositiva, y un re-stamp la da por buena.
- Files created/modified: output/slide-model.json, output/html/index.html, index.html raíz.
- Verificado: render sin `warning|unknown|fallback`, 0 ocurrencias de la frase en el HTML.

## 2026-08-24 — Fuera cross-validation de 'Los errores que arruinan la medición'
- Status: complete
- Asks log:
  - 2026-08-24 — "Borrar 'Cross-validation, y cuándo paga / K-fold entrena k veces reservando una porción distinta y promedia...'"
- What was decided: se borró la quinta card de la diapositiva **2.4 'Los errores que arruinan la medición'**, y su viñeta equivalente en `final.md` y `draft.md`. La diapositiva queda con cuatro errores.
- **Por qué encajaba mal, más allá del pedido:** la diapositiva se llama *los errores* y su bajada dice "ninguno lanza una excepción, todos devuelven una métrica mejor que la real". Cross-validation no es un error ni infla ninguna métrica: es una técnica alternativa. Era la única card que no cumplía la promesa del título.
- Se recortaron además las dos referencias de fuente que apuntaban sólo a esa card (`§12 Cross-validation` de roboflow y `§4 Cross-validation` de train-validation-test-sets), y con eso la segunda fuente sale entera de la línea de Sources de esa diapositiva. **El material sigue en el corpus**, sólo deja de estar citado acá.
- Las notas del orador no se tocaron: 'los dos del medio son aporte propio' seguía apuntando a estratificación y series de tiempo, que con cuatro cards siguen siendo la 2 y la 3.
- Files created/modified: final.md, draft.md, output/slide-model.json (re-stampeado), output/html/index.html, index.html raíz.
- Verificado: render sin `warning|unknown|fallback`, 0 ocurrencias de 'Cross-validation' en el HTML.

## 2026-08-24 — Fuera el argumento de diferenciabilidad en 'Qué es una función de pérdida'
- Status: complete
- Asks log:
  - 2026-08-24 — "Borrar 'Accuracy no la tiene: es un conteo, salta de a escalones. Por eso accuracy se reporta y nunca se optimiza. Notación de acá en adelante'"
  - 2026-08-24 — pregunta al presentador: la cita cruzaba dos bloques distintos → eligió **borrar solo la parte de accuracy y conservar la notación**.
- **Por qué hubo que preguntar.** En `final.md` son **dos párrafos separados** ('Diferenciable o no sirve' y 'Notación de acá en adelante'), pero el modelo del deck los tenía **fusionados en un solo highlight `important`**. El texto citado empezaba a mitad del primero y terminaba al principio del segundo, así que borrar literal la selección dejaba las dos mitades rotas. Es otra divergencia markdown/modelo del mismo tipo que la del 2026-08-24 en 'Los tres, lado a lado'.
- **Por qué la notación no se podía perder:** `y` y `t` los usan las fórmulas de 'Regresión: MSE, MAE y Huber' (`L = (y − t)²`, `L = |y − t|`), 'Clasificación binaria: BCE' (`L = −[t·log(y) + (1 − t)·log(1 − y)]`) y 'El delta' (`y − t`). Sin esa línea las fórmulas quedan con símbolos sin presentar.
- What was decided: el párrafo 'Diferenciable o no sirve…' salió de `final.md`, `draft.md` y del modelo. El highlight quedó con **solo** la notación, y pasó de `important` a `note` porque una convención de símbolos no es el remate de la diapositiva.
- **El punto de accuracy no se perdió**: las notas del orador lo desarrollan más largo que la diapositiva ("la razón por la que no entrenamos directamente sobre accuracy... es que accuracy no tiene derivada. Se entrena sobre un sustituto derivable y se mide con lo que importa"), y anticipan que la brecha reaparece en la sección de métricas.
- Files created/modified: final.md, draft.md, output/slide-model.json (re-stampeado), output/html/index.html, index.html raíz.
- Verificado: render sin `warning|unknown|fallback`; 0 ocurrencias de 'salta de a escalones' y 1 de 'Notación de acá en adelante' en el HTML.

## 2026-08-24 — Todo el mazo pasa de PyTorch a Keras
- Status: complete
- Asks log:
  - 2026-08-24 — "No hablemos de PyTorch, los ejemplos estan usando Keras. Actualiza eso en todos lados"
- **Contexto que fija la decisión:** el notebook `missions/clase3/input-data-types.ipynb` usa **Keras 3** (`import keras`, `from keras import layers`, `keras.Sequential`, `keras.optimizers`), no `tf.keras`. Las llamadas nuevas se escribieron con ese estilo.
- Cambios en diapositivas (los cinco que se ven en pantalla):
  - **BCE.** `BCEWithLogitsLoss` → `BinaryCrossentropy(from_logits=True)`, y el título de la card pasó de 'La sigmoide ya viene adentro' a **'La sigmoide va en un solo lado'**. No es cosmética: en PyTorch la loss con logits es la recomendada y la sigmoide efectivamente *viene* adentro; **en Keras `from_logits` es opcional y su default es `False`**, así que la afirmación original habría sido falsa. La regla que sí se sostiene en Keras es que activación y `from_logits` no van las dos.
  - **Predecir con logits.** `torch.sigmoid(model(x))` → `keras.ops.sigmoid(model(x))`.
  - **Cross-entropy multiclase.** `CrossEntropyLoss` → `CategoricalCrossentropy(from_logits=True)`, con la variante `SparseCategoricalCrossentropy` nombrada para etiquetas enteras.
  - **L2.** `Adam(params, weight_decay=1e-4)` → `layers.Dense(64, kernel_regularizer=regularizers.l2(1e-4))`, que es la forma idiomática en Keras y además es la que coincide con el `J = cost + λ·Σw²` de la diapositiva.
  - **Dropout.** `nn.Dropout(0.2)` → `layers.Dropout(0.2)`.
- **Una card cambió de contenido, no de nombre de API.** 'El bug clásico' decía *olvidar `model.eval()` deja dropout activo en inferencia*. **Ese bug no existe en Keras:** `fit` activa dropout y `predict`/`model(x)` lo apagan solos. Traducir la frase habría sido inventar un problema. Pasó a **'En Keras no hay que acordarse'**, que dice lo mismo al revés y agrega la salida real: para MC dropout hay que pedir `model(x, training=True)`. Las notas del orador acompañan.
- **El bucle de entrenamiento (notas de 'El ciclo completo, batch a batch').** Estaba anclado a `optimizer.zero_grad()` / `loss.backward()` / `optimizer.step()`. En Keras esas tres líneas viven adentro de `model.fit`; el anclaje pasó al bucle abierto a mano: el *gradient tape* graba (acumular), `tape.gradient(loss, model.trainable_weights)` cierra la cuenta, `optimizer.apply_gradients(...)` aplica. **Se perdió a propósito el cuarto paso**, vaciar: cada tape arranca limpio, así que el error de no vaciar es de otros frameworks y quedó dicho como tal.
- **Fuentes tocadas.** Se borraron las dos citas a *PyTorch, Optimizing Model Parameters* (diapositivas 4.5 y 4.9): sostenían la afirmación "los gradientes se suman por defecto", que ya no se hace. En su lugar entró *Keras, Writing a training loop from scratch* <https://keras.io/guides/writing_a_training_loop_from_scratch/>, **sin cita textual** porque no se verificó contra la página. Y en la 1.2 se recortó la mitad PyTorch de la cita doble sobre el aplanado; la de Keras alcanza sola para la afirmación.
- **Lo que NO se tocó, a propósito:**
  - **El corpus.** `research/corpus/chat.md.md` es PyTorch de punta a punta (§8, §10 y todos los bloques de código). Es una fuente: reescribirla sería falsificarla. Donde una línea de Sources nombraba `BCEWithLogitsLoss` para describir qué trae el corpus, se reescribió en términos neutros ("la loss que recibe logits"), que sigue siendo fiel.
  - **`# Cut material` de `final.md`** (dos líneas con `BCEWithLogitsLoss` y `torch.sigmoid`) y el log de feedback cerrado de `draft.md` (~línea 170). Son archivos históricos de decisiones pasadas. **Si alguna vez se rescata ese material, hay que traducirlo antes de volver a ponerlo en una diapositiva.**
- Verificado: 0 ocurrencias de `PyTorch`, `torch.`, `model.eval`, `BCEWithLogits` y `CrossEntropyLoss` en el HTML renderizado.

## 2026-08-24 — Dos diagramas redibujados
- Status: complete
- Asks log:
  - 2026-08-24 — "Borrar del grafico 'un eje por cada peso de la red…'. Asi el grafico toma mas importancia" → corregido enseguida: **"Deja el texto en realidad, ponelo como una especie de titulo del grafico"**
  - 2026-08-24 — "En el slide 35 en vez de usar cajas, seria bueno que se vea como una especie de nodos que representan la red neuronal"
- **`s6-1-1-descenso-al-minimo`** (4.1 'Buscar el mínimo de una función'). La línea *'un eje por cada peso de la red: el dibujo muestra uno, un MLP real tiene millones'* estaba al pie en gris chico. Pasó **arriba, como título**: 14 px, negrita, `#3B3535` (la tinta por defecto de `diagram-style.md`), y todo el dibujo bajó 22 px con un `translate`. El `viewBox` no cambió, así que la diapositiva no se re-acomoda.
- **`s6-2-1-ciclo-forward-backward`** (4.2 'Entrenar es un ciclo de dos movimientos'). Las tres cajas `[ capa 1 ] [ capa 2 ] [ salida ]` pasaron a **12 nodos en cuatro capas** (entrada 3, capa 1 = 4, capa 2 = 4, salida 1) unidos todos con todos por 32 aristas finas. El riel rojo del backward sube ahora a cada capa por debajo de su nodo más bajo. `viewBox` de 700×300 a **700×330** para que la red respire; sigue siendo apaisado y sigue entrando en el `split-right`.
- **Nota sobre el ancho de la entrada:** se dibujaron 3 nodos de entrada aunque el resto del mazo insiste en que la capa de entrada no calcula nada. Es coherente: son posiciones del vector, igual que en `s1-6-1-nodos-de-entrada`. Por eso tampoco le llega flecha roja de backward — no hay pesos antes de ella.
- **Los dos sidecars `.ascii` se actualizaron y los SVG se re-sellaron** con el `talksmith-ascii-sha256` del sidecar nuevo, así que un futuro Polish los ve al día y no los redibuja. Los bloques `ascii-source` de `final.md` y las fences ```ascii de `draft.md` quedaron en sincronía (ojo: **`final.md` escapa `>` como `&gt;`** dentro del comentario, si no cerraría el comentario HTML; `draft.md` no escapa nada).
- **Los `.png` quedaron viejos y no importa para el HTML.** `html_style.py` resuelve un `_vector_twin`: si el modelo pide `images/x.png` y existe `images/x.svg`, **inlinea el SVG** e ignora el PNG. Por eso los 24 `media.src` del modelo apuntan a `.png` y el deck igual muestra vectores. **Sí importaría para un render `.pptx`**, que usaría los PNG viejos. Regenerarlos necesita `cairosvg`, y **no hay cairo en esta máquina** (`find_library('cairo')` da None, no hay `rsvg-convert` ni `inkscape`).
- Verificado en el HTML: 12 `<circle>` y 32 `<line>` en el diagrama del ciclo, y el título nuevo presente en el del descenso.

## 2026-08-24 — La sección 6 deja de contradecir a la sección 5 sobre la loss
- Status: complete
- Asks log:
  - 2026-08-24 — "'L = ½ Σᵢ (yᵢ − tᵢ)²' no depende realmente de la funcion de perdida elegida?"
  - 2026-08-24 — "Slides anteriores introdujimos el concepto que dependiendo de lo que sea el resultado hay loss function que se debe elegir"
- **La incoherencia, que era real.** La sección 5 enseña que la loss la fija la salida (lineal→MSE, sigmoide→BCE, softmax→cross-entropy) y que activación y loss no se eligen por separado. La sección 6 después deriva todo sobre `L = ½Σ(y−t)²` **sin decirlo en pantalla**: la aclaración vivía solo en las notas del orador de 4.3 y 4.5. Un alumno atento la agarra.
- **Peor: la imagen de 4.5 mostraba el par prohibido.** `δⱼ = (yⱼ − tⱼ)·yⱼ(1−yⱼ)` es L2 con sigmoide de salida — la deducción clásica de los libros (Nielsen) y exactamente el par que la sección 5 dice que no se usa. Con el par correcto ese `y(1−y)` **no está**: se cancela.
- **La matemática que ordena todo esto** (vale dejarla escrita porque es el remate del tema): con los tres pares correctos el delta de la capa de salida da `y − t` en los tres casos.
  - lineal + MSE: `∂L/∂y = y−t`, `∂y/∂a = 1`
  - sigmoide + BCE: `∂L/∂y = (y−t)/[y(1−y)]`, `∂y/∂a = y(1−y)` → se cancelan
  - softmax + cross-entropy: idem, `δ = y − t`
- Qué se cambió:
  - **4.3 'El número que hay que derivar'.** La bajada pasó a decir que la loss la fija la salida y que L2 es el caso de trabajo. Highlight `note` nuevo: cambiar de loss cambia **un solo factor** de la cadena; el resto del backward es idéntico para cualquier loss diferenciable. **La fórmula L2 se queda** — es la deducción clásica y ahora está encuadrada.
  - **4.5 'El delta'.** El párrafo sobre `y(1−y)` como derivada de la sigmoide se reemplazó por la simplificación a `y − t`, y el highlight subió de `note` a `important` porque es el remate. Notas del orador reescritas con la cuenta de la cancelación y con la explicación de por qué los libros traen la otra fórmula.
  - **Imagen redibujada:** `images/bp-delta-salida.svg` (nuevo). Arriba la forma general `δⱼ = ∂L/∂yⱼ · ∂yⱼ/∂aⱼ` con los dos factores rotulados; abajo, en una banda, la simplificación `δⱼ = yⱼ − tⱼ` en rojo. El crédito en Sources dice ahora que la `s34` de la biblioteca se redibujó para esta Talk.
- **Detalle de plomería que costó un render de más.** El SVG nuevo **no se usaba** aunque estuviera al lado del PNG. `html_style._vector_twin` solo cambia un `.png` por su `.svg` si puede probar que lo generó Talksmith: o existe el sidecar `.ascii`, o el SVG trae el comentario `talksmith-ascii-sha256`. Es a propósito, para no pisar un `chart.png` del presentador con un `chart.svg` ajeno que comparta nombre. Se resolvió escribiendo el sidecar `.ascii` y sellando el SVG con el sha del sidecar. **Regla: un SVG nuevo puesto a mano al lado de un PNG no se usa hasta que tenga sidecar o sello.**
- **El `.png` viejo quedó con la fórmula contradictoria.** Para el HTML no importa (gana el SVG), pero **un render `.pptx` mostraría la fórmula vieja**. Regenerarlo necesita cairosvg, que no está instalado. Además el SVG nuevo usa `∂` (U+2202): en el navegador se ve bien, pero si algún día se pasa por cairosvg hay que verificar que no salga tofu, como advierte `diagram-style.md` para los símbolos.
- Files created/modified: final.md, draft.md, output/slide-model.json (re-stampeado), images/bp-delta-salida.svg (nuevo), images/bp-delta-salida.ascii (nuevo), output/html/index.html, index.html raíz.
- Verificado: render sin `warning|unknown|fallback`; los seis textos nuevos presentes en el HTML y la imagen nueva inlineada.

## 2026-08-24 — La 4.3 arranca por la regla y baja al ejemplo del precio
- Status: complete
- Asks log (tres pasadas sobre la misma bajada, y la tercera es la que quedó):
  - 2026-08-24 — "'L2 es el caso de trabajo, no la única loss'. Que significa?" → *caso de trabajo* era un calco de *worked example* y no se entiende en castellano.
  - 2026-08-24 — "Tal vez mejor en vez de decir 'clásica' decir, supongamos que tenemos que obtener el precio de una casa. La función de pérdida sería..."
  - 2026-08-24 — "Es mas claro decir, hay que derivar la funcion de perdida y este es un ejemplo."
- **Forma final de la bajada:** *"Lo que hay que derivar es **la función de pérdida**, y cuál es la fija la tarea. Tomemos un ejemplo: si la red predice el precio de una casa, la salida es una neurona lineal y la loss es el error cuadrático."*
- **El orden es el punto, no la redacción.** Las tres versiones decían lo mismo; la que funciona **abre por la regla general y marca el ejemplo como ejemplo**. Las dos anteriores abrían por el caso particular ("la clásica es el error cuadrático" / "supongamos una casa"), y ahí el alumno no tiene forma de saber si L2 es una elección de la clase o una propiedad del algoritmo.
- **El ejemplo del precio no es nuevo en el mazo:** ya está en la 5.1 ('para predecir un precio la tarea pide una neurona sin activación... y sobre esa salida van MSE, MAE o Huber') y es el del notebook `input-data-types`. Sirve como cadena de consecuencias: predecimos un precio → salida lineal → error cuadrático. Nadie eligió la loss a mano. Eso quedó escrito en las notas del orador.
- El highlight pasó a cargar la invariancia, que es el dato que la bajada ya no dice: **'El algoritmo no cambia con la loss'** más los dos contraejemplos (BCE, cross-entropy) y el hecho de que cambiaría un solo factor.
- Files created/modified: final.md, draft.md, output/slide-model.json (re-stampeado), output/html/index.html, index.html raíz.

## 2026-08-24 — 'Ojo con la escala' se borra: la 4.8 ya lo dice, y mejor
- Status: complete
- Asks log:
  - 2026-08-24 — "'Ojo con la escala…' creo que debería ir más adelante. Tal vez una sección al final de cosas a tener en cuenta. Fijate si hay muchas notas de estas repartidas en esta sección."
- **Auditoría de la sección 6 (Backpropagation), 10 diapositivas de contenido, 12 recuadros:** 6.1 important · 6.2 note · 6.3 note + **warning** · 6.4 important · 6.5 important · 6.6 important · 6.7 ninguno · 6.8 important · 6.9 important · 6.10 note + note + important. **El 'Ojo con la escala' era el único `warning` de toda la sección**, así que no había un enjambre de advertencias: los otros once recuadros son el remate de su propia diapositiva, no salvedades sueltas.
- **La diapositiva de cierre que el presentador imaginaba ya existe:** 6.10 'Qué mirar cuando esto se entrena', creada el 2026-08-21 por un pedido casi idéntico ("agregar un slide al final con cosas prácticas a tener en cuenta"). Y **está llena**: tabla de 3 columnas × 5 filas más tres recuadros. Meter ahí una cuarta salvedad la rompe.
- **Por qué se borró en vez de moverse.** La 4.8 'Batch y época no son lo mismo' ya dice exactamente eso, en su card `Batch`: *"Las `B` filas hacen el forward a la vez con los mismos pesos, se promedia su loss, y ese promedio es lo que se deriva"*. Mover el recuadro habría sido duplicarlo. Además el recuadro estaba en 4.3, **cinco diapositivas antes de que se introduzca el batch**: era una referencia hacia adelante a un concepto que la audiencia todavía no tenía.
- **Esto respeta un reparto que ya estaba decidido.** El 2026-08-21 se auditó la repetición de "se acumula durante el batch y se aplica al cerrarlo", que aparecía en cuatro diapositivas, y se repartió por dueño: **6.2 lo enuncia, 6.7 se queda con la aritmética del paso, 6.8 con el conteo, 6.9 con el ensamblado.** El 'Ojo con la escala' de 6.3 se había colado fuera de ese reparto y le pisaba el tema a 6.8.
- **Regla que sale de acá:** antes de mover una salvedad, buscar quién es su dueño en el reparto. Si el dueño ya la dice, la salvedad de la otra diapositiva no se muda: se borra.
- La 4.3 queda con un solo recuadro, 'El algoritmo no cambia con la loss', que es el que le corresponde.
- Files created/modified: final.md, draft.md, output/slide-model.json (re-stampeado), output/html/index.html, index.html raíz.

## 2026-08-24 — La definición de `a` entra al gráfico de la regla de la cadena
- Status: complete
- Asks log:
  - 2026-08-24 — "Agregar Derivar a = Σ xᵢwᵢ + b en el grafico del slide 37 para que no se pierda."
- **El diagnóstico era correcto.** La definición vivía **solo en el texto** del tercer bullet de 4.4 ('Es la entrada que multiplicaba a ese peso, nada más. Derivar `a = Σ xᵢwᵢ + b` respecto de uno de sus pesos deja la entrada que lo acompañaba'). El gráfico mostraba `∂aⱼ/∂wᵢⱼ` sin decir nunca qué es `a`, y ese es justo el factor que no se deduce solo.
- **Imagen nueva:** `images/bp-regla-de-la-cadena.svg`. Arriba la cadena de cuatro fracciones igual que la original; abajo, en una banda, **`aⱼ = Σᵢ xᵢ wᵢⱼ + bⱼ` en rojo**, con la bajada 'la suma ponderada, lo que la unidad calcula antes de activar'. El rojo es el único acento de ese diagrama, que es lo que pide `diagram-style.md`.
- Se le puso sidecar `.ascii` y sello `talksmith-ascii-sha256`, sin los cuales `_vector_twin` **no habría usado el SVG** (misma trampa que con el delta, ver la entrada de más arriba de hoy).
- Notas del orador: se agregó un párrafo al principio que dice que la definición ya está en pantalla y que conviene señalarla **antes** de recorrer los tres factores, porque el tercero solo se entiende si se ve que `a` es una suma de productos.
- El crédito en Sources dice ahora que la `s33` de la biblioteca se redibujó para esta Talk.
- **Van dos imágenes de la biblioteca redibujadas hoy** (`bp-delta-salida` y `bp-regla-de-la-cadena`). Las dos siguen teniendo su `.png` viejo al lado, con el contenido anterior: irrelevante para el HTML, **incorrecto para un futuro `.pptx`**.
- Files created/modified: images/bp-regla-de-la-cadena.svg (nuevo), images/bp-regla-de-la-cadena.ascii (nuevo), final.md, draft.md, output/slide-model.json (re-stampeado), output/html/index.html, index.html raíz.

## 2026-08-24 — El gráfico de la cadena, segunda pasada: sin caja y con espaciado exacto
- Status: complete
- Asks log:
  - 2026-08-24 — "Revisar el espaciado del grafico. Mismo `aj = ∑i xi wij + bj` no es necesario ponerlo en una caja, pareceria que tiene la misma importancia que el resto."
- **Las dos observaciones eran correctas y la segunda es la de fondo.** La banda con fondo y borde le daba a la definición el mismo peso visual que a la cadena, y son cosas distintas: la cadena es el contenido de la diapositiva, la definición es apoyo. Ahora va **sin caja, debajo, más chica**, con una bajada gris de una línea. El acento rojo se sacó del todo: el diagrama no tiene foco de color, que es correcto porque no hay un elemento que compita.
- **El espaciado estaba mal por una razón concreta y vale anotarla.** La primera versión posicionaba cada fracción con anchos de texto **estimados a ojo** en Helvetica, y las barras no coincidían con el texto. Se rehízo en **`'DejaVu Sans Mono', monospace`**, donde todo glifo avanza igual, así que numerador, denominador y barra se calculan exacto. Es además la familia que `diagram-style.md` reserva para notación tipo código.
- **Los subíndices bajaron a letras adyacentes** (`∂wij`, `∂yj`, `∂aj`, `aj = ∑i xi wij + bj`), que es como los escribió el presentador en su pedido. La versión con subíndices Unicode reales (U+1D62, U+2C7C) se descartó: **U+2C7C no está garantizado en DejaVu Sans Mono**, y un glifo faltante rompe la grilla monoespaciada además de arriesgar tofu, justo lo que advierte `diagram-style.md`. Los únicos dos no-ASCII que quedaron son `∂` y `∑`, ambos presentes en la familia.
- Verificado: en el SVG inlineado queda **un solo `<rect>`**, el fondo blanco.

## 2026-08-24 — El gráfico de la cadena, tercera pasada: título arriba y lienzo ajustado
- Status: complete
- Asks log:
  - 2026-08-24 — "'el efecto total es el producto de tres efectos parciales' tal vez más como título. Hay mucho espacio en blanco debido al texto y este 'la suma ponderada: lo que la unidad calcula antes de activar'"
- **Dos cambios, y el segundo es el que importa.** La línea de arriba pasó a **título**: mayúscula inicial, 14 px, negrita, `#3B3535` — el mismo tratamiento que se le dio hoy al gráfico del descenso, así que los dos diagramas de fórmula del mazo se encabezan igual.
- **El espacio en blanco no era del layout de la diapositiva, era del lienzo del SVG.** El `viewBox` seguía en 700×230 después de haberle sacado la banda con fondo, o sea que la altura estaba dimensionada para un elemento que ya no existía. Bajó a **700×185** y las dos prosas se acortaron ('la suma ponderada: lo que la unidad calcula antes de activar' → 'la suma ponderada, antes de la activación'). Ratio 3.8, que es el de la imagen original de la biblioteca.
- **Regla que sale de acá, y ya van dos veces hoy:** cuando se le saca un elemento a un SVG hay que **volver a ajustar el `viewBox`**. Un lienzo más alto que el contenido no se ve en el XML pero en la diapositiva aparece como una franja vacía, porque el render escala la imagen por su caja, no por su tinta.

## 2026-08-24 — El gráfico de la cadena, cuarta pasada: la proporción era el problema
- Status: complete
- Asks log:
  - 2026-08-24 — "'El efecto total...' debería ser un título más arriba y tal vez con fuente más grande. Al estar muy a la izquierda hace que las formulas sean muy chicas."
- **El diagnóstico del presentador apuntaba al síntoma correcto por la razón correcta, aunque el culpable no era el título sino la proporción del lienzo.** Con 700×185 (ratio 3.8) el render escala la imagen **por el ancho** dentro de la media de un `split-right`; el alto resultante es chico y toda la tipografía de adentro sale diminuta. El título largo pegado a la izquierda era lo que mantenía el lienzo tan ancho.
- **Fix:** lienzo de **466×248 (ratio 1.88)**, ajustado al contenido, y todo adentro más grande — fracciones de 20 a **30 px**, definición de 17 a **22**, título centrado en **16 px negrita**. El título se acortó a *'El efecto total es el producto de tres factores'* para que entre en el ancho nuevo sin forzarlo.
- **Este es el mismo fenómeno que la entrada del 2026-08-21 sobre la 1.2**, pero al revés. Aquella decía: un diagrama casi cuadrado (1.26) en `image-full` deja franjas a los costados. Esta dice: **una tira ancha (3.8) en `split-right` achica la tipografía**. La regla completa es una sola: **la proporción del `viewBox` tiene que parecerse a la de la caja donde va a caer.** Media de `split-right` es más o menos 16:9, así que un diagrama que va ahí conviene cerca de 1.7–1.9.
- **Cómo verificarlo sin abrir el navegador:** `grep viewBox` sobre el SVG y dividir. Si el ratio pasa de 2.5 y el diagrama va en un `split-*`, la tipografía va a salir chica.

## 2026-08-24 — Los índices se leían como parte del nombre de la variable
- Status: complete
- Asks log:
  - 2026-08-24 — "Que es j en el indice? Ojo que no se esta viendo como subindices"
- **Dos defectos y los dos eran míos.**
  - **Los subíndices no eran subíndices.** En la pasada anterior había bajado `wᵢⱼ` a letras pegadas (`wij`) para esquivar dos trampas: los codepoints Unicode de subíndice (U+2C7C, el de la `j`, no está garantizado en DejaVu Sans Mono) y la regla de `diagram-style.md` contra `<tspan>` dentro de texto centrado. **La salida fue peor que las dos trampas juntas**: `wij` se lee como una variable llamada así, no como *el peso de i a j*. Ahora van con `<tspan>` de cuerpo menor y `dy`, o sea subíndices de verdad.
  - **Cómo se resolvió la regla del `tspan`.** Esa regla es una advertencia de **cairosvg**, que apila las corridas en la misma x cuando el `<text>` está centrado. Se esquiva **anclando a la izquierda** y calculando la x de cada fracción a mano: en monoespaciada los anchos son exactos (avance = 0,6 em), así que centrar a mano es trivial y el `tspan` queda seguro en los dos renderizadores.
  - **`j` no estaba definido en ninguna parte.** Ni en el gráfico ni en el texto de la diapositiva. Se sumó una línea gris al pie: *'j es la unidad; i, la entrada que llega a ella'*.
- Lienzo final **427×258 (1,65)**. La cuarta pasada lo había dejado en 466×248; achicar el ancho al contenido real lo acerca más a la caja donde cae.
- **Pendiente del mismo tipo, no tocado:** los otros diagramas de la sección siguen anchos para un `split-right` — `bp-delta-salida` 2,33 y `s6-2-1-ciclo-forward-backward` 2,12. El del delta además tiene fórmula adentro, así que sufre lo mismo que sufría este.

## 2026-08-24 — La regla de la cadena, dibujada sobre la red; y auditoría de subíndices
- Status: complete
- Asks log:
  - 2026-08-24 — "Crear otro diagrama al lado del que está, vamos a reemplazar el texto (1,2,3) de la izquierda por una visualización de una red donde veamos visualmente Wi,j etc"
  - 2026-08-24 — "En realidad podrías poner el texto que está en 1, 2 y 3 abajo de cada uno de los componentes. Va a ser más fácil leerlo."
  - 2026-08-24 — "Revisar en todas las imágenes el uso correcto de subíndices."
- **La 4.4 cambió de forma.** Dejó de ser `process` con tres pasos escritos y pasó a **`image-full`** con un solo diagrama compuesto (770×365, ratio 2.11, que es lo que pide un `design: full`). Los tres bullets desaparecieron de la diapositiva y su detalle pasó entero a las notas del orador.
- **Qué muestra el diagrama.** A la izquierda, el camino real: tres entradas → nodo de suma `Σ` → nodo de activación `f` → caja `L`, con la conexión `wᵢⱼ` **en rojo** (el peso que se deriva) y `aⱼ` / `yⱼ` rotulando las flechas intermedias. Debajo, tres corchetes numerados **③②①** de izquierda a derecha, cada uno con su frase en prosa **debajo del número**. A la derecha, la regla de la cadena con **los mismos números** sobre sus tres factores.
- **Por qué esto es mejor que los bullets:** la fórmula deja de ser notación y pasa a describir un recorrido que se ve. Y el orden de cálculo (de derecha a izquierda) se lee solo, porque ① queda pegado a `L`.
- **La leyenda al pie no funcionaba.** El primer intento puso las tres frases en una fila al pie del dibujo; el presentador marcó que debajo de cada componente se lee mejor, y tenía razón: obligaba a saltar del número a la leyenda y volver.
- **Auditoría de subíndices, 22 SVGs.** Dos con índices escritos como letras pegadas: `s1-4-1-neurona` (`x1 x2 x3`) y el propio `bp-regla-de-la-cadena` de la pasada anterior. Los dos corregidos con `<tspan>` de cuerpo menor y `dy`. `s9-3-1-objetivo-l2` usa `w²` con el carácter de superíndice real, que está bien. **Chequeo reproducible:** `grep -o '>[^<]*\b[wxyaδz][ij0-9]\{1,2\}\b[^<]*<' images/*.svg` — hoy da 0.
- **Hallazgo grande de la auditoría de proporciones.** Se leyó `theme.css`: un `d-split` es `grid-template-columns: 1fr 1fr` con `column-gap`, o sea la media queda en **media pantalla de ancho por casi todo el alto**. La caja resultante tiene proporción **≈1,28**, no apaisada. **Nueve de los dieciséis diagramas del mazo son más anchos que su caja** y por eso su tipografía sale chica:
  `s3-1-1` 3,31 · `s1-4-1` 2,83 · `s9-3-1` 2,62 · `s7-1-2` 2,60 · `s6-8-1` 2,26 · `s2-4-1` 2,27 · `s6-2-1` 2,12 · `s7-7-1` 2,02 · `s6-1-1` 1,94.
  Ya están al día `bp-delta-salida` (1,28) y `bp-regla-de-la-cadena` (2,11 en `full`).
- **Regla, ahora con número:** `split-*`/`column-*` piden **≈1,3**; `full` pide **≈1,8–2,2**. Verificable sin navegador cruzando el `viewBox` con el `design` del modelo.

## 2026-08-24 — La 4.4 no renderizaba la imagen: `image-full` lee `image`, no `media`
- Status: complete
- Asks log:
  - 2026-08-24 — "Revisar slide 37 que no se renderiza la imagen"
- **La causa.** Al pasar la diapositiva a `image-full` dejé la imagen en `media`, pero **`image-full.j2` emite `embed_img(s.image)`**, no la media del stage. Sin `image` el helper devuelve el marcador vacío: media diapositiva con la palabra `image` y nada más. **Ningún aviso del build**: `_REQUIRES` acepta `("image","media")` como alternativas, así que el modelo pasaba la validación mientras la plantilla miraba el campo que no estaba.
- **Por qué `image-full` era además la plantilla equivocada.** Emite su propio `.stage` para sacar el padding, y a propósito **no dibuja la banda de highlights**. O sea que aun arreglando el campo, el recuadro 'Los tres factores son valores intermedios: ningún peso se movió todavía' se perdía en silencio.
- **La solución, que estaba en el CSS.** `content-image` con `design: split-right` y **sin `facts`**. `theme.css` trae tres reglas hechas justo para esto: `.stage.d-split:has(.cfit:not(:has(*)))` colapsa la grilla a una columna, esconde `.cbody` y le da a `.smedia` el `grid-column: 1/-1`. Resultado: **la imagen ocupa el ancho completo igual que con `image-full`, y la banda de highlights se conserva**. El comentario de `content-image.j2` lo dice: una diapositiva que lleva sólo una imagen es un `content-image` legítimo.
- **Regla:** para una imagen a todo el ancho **que además tenga recuadro**, `content-image` sin `facts`, no `image-full`. `image-full` es para la imagen sola.
- **Y una trampa de verificación que casi me come.** Mi primer chequeo buscó el título con `h.find('La regla de la cadena')` y cayó en la mención del título **dentro de las notas del orador de la diapositiva anterior**, así que dio todo `False` sobre una diapositiva equivocada. **Para verificar una diapositiva en el HTML hay que partir por `<section class="slide"` y buscar `<h2 class="stitle">…</h2>`**, no el texto suelto.
- Verificado: `data-kind="content-image"`, SVG inlineado, sin placeholder, `.cfit` vacío (imagen a todo el ancho), recuadro presente, 11 nodos y los tres rótulos en su lugar.

## 2026-08-24 — La 4.4, a imagen completa de verdad
- Status: complete
- Asks log:
  - 2026-08-24 — "Imagen quedó al costado. Fijate de ponerla como full"
- **El colapso por CSS existe pero no alcanzó.** `theme.css` sí trae `.stage.d-split:has(.cfit:not(:has(*)))` — verificado en el HTML emitido, la regla viaja. Aun así la imagen no ocupaba el ancho: con la banda de highlights comiendo alto, la fila del grid queda baja y un SVG limitado por `max-height:100%` se dibuja angosto y centrado. **Depender de ese colapso es frágil; `image-full` es explícito.**
- **Cambio:** plantilla `image-full`, campo **`image`** (que es el que la plantilla lee, no `media`), `design: full`. Emite `.iffill` de borde a borde, sin `d-split`.
- **El recuadro no se perdió: se mudó adentro del dibujo.** `image-full` no dibuja banda de highlights a propósito, así que 'Los tres son valores intermedios… Ningún peso se movió todavía' pasó a ser el pie del SVG, separado por una línea fina, con la segunda frase en negrita. En una diapositiva cuyo cuerpo entero es la imagen, eso está mejor ahí que en una banda aparte. El párrafo equivalente salió de `final.md` y `draft.md`.
- Lienzo de 770×365 a **770×412** (ratio 1,87) para hacerle lugar al pie, que sigue en el rango bueno para `full`.
- Verificado: `data-kind="image-full"`, `.iffill` presente, sin `d-split`, SVG inlineado, sin placeholder y con el cierre adentro.

## 2026-08-24 — `j` en el diagrama de la cadena es una unidad de SALIDA, no oculta
- Status: complete
- Asks log:
  - 2026-08-24 — "'j es la unidad' supongo que es el hidden layer?"
- **La pregunta destapó una imprecisión del dibujo.** El rótulo decía 'j es la unidad', a secas, pero el dibujo manda `yⱼ` **directo a `L`**, y eso solo es cierto en la **capa de salida**. Para una unidad oculta la loss no depende de `yⱼ` de forma directa: depende a través de todas las unidades de la capa siguiente, y por eso el primer factor deja de ser inmediato.
- **Por qué importaba corregirlo:** la diapositiva siguiente-siguiente, 'Propagar el delta hacia atrás', abre justamente con *'¿contra qué se compara una unidad oculta? Contra nada'* y separa capa de salida de capas ocultas. Un alumno que tomara el dibujo como general iba a chocar de frente con esa diapositiva.
- **Fix:** el rótulo pasó a **'j es una unidad de salida; i, lo que entra a ella'**, más una segunda línea que hace de puente: **'si j fuera oculta cambia el factor 1: ver la que sigue'**. La estructura de tres factores no cambia, y decirlo así convierte la ambigüedad en un anticipo.
- Notas del orador: se agregó la respuesta preparada para cuando alguien haga esta misma pregunta en clase, marcándola como buen puente hacia la propagación del delta.
- **Lo que vale recordar del método:** el dibujo era correcto pero incompleto, y el hueco solo se ve cruzándolo con lo que promete otra diapositiva. Un diagrama nuevo conviene leerlo contra las dos o tres diapositivas que lo rodean, no solo contra la suya.

## 2026-08-24 — El diagrama de la cadena se encuadra, y qué son las `x`
- Status: complete
- Asks log:
  - 2026-08-24 — "Borrá 'j es una unidad de salida…' y 'si j fuera oculta…'. Tal vez aclarar que esto es mirando la salida. x1 y x2 es notación correcta? Porque si hay más de una capa eso serían activaciones?"
- **El encuadre subió al encabezado.** Las dos líneas de leyenda salieron y en su lugar hay un subtítulo bajo el título: **'mirando desde una unidad de salida j'**. Dice lo mismo que las dos líneas juntas, pero antes de que el ojo entre al dibujo en vez de después.
- **La observación sobre `x` era correcta y no estaba resuelta.** Si `j` no está en la primera capa, lo que entra no es el dato: son las salidas de la capa anterior. Muchos textos usan por eso otro símbolo (`a` con superíndice de capa), **pero en este mazo `a` ya está tomada por la suma ponderada** (`aⱼ = Σ xᵢ wᵢⱼ + bⱼ`), y `y` está tomada por la predicción. Renombrar habría roto la notación de dos secciones.
- **Decisión:** se deja `x` y se aclara al costado, en el hueco que dejaron las líneas borradas: *'x es lo que entra a j: el dato si j está en la primera capa, si no la salida de la capa anterior'*. Es honesto, no toca la notación del resto, y contesta la pregunta en el lugar donde aparece.
- Notas del orador: quedó la aclaración de notación y la formulación 'parado sobre una unidad', que es la que hace que la recursión del backward no suene mágica.
- **Regla de notación para esta Talk, por si vuelve a aparecer:** `a` = suma ponderada (pre-activación), `y` = salida / predicción, `t` = objetivo, `x` = lo que entra a la unidad, `w` = peso, `b` = bias, `δ` = sensibilidad del error respecto de `a`. `i` indexa lo que entra, `j` la unidad.

## 2026-08-24 — Revisión crítica del gráfico de la cadena: cuatro defectos, uno grave
- Status: complete
- Asks log:
  - 2026-08-24 — "Revisá en forma crítica el gráfico si estamos confundiendo algo."
- **(1) GRAVE — `a` significaba dos cosas opuestas en el mismo mazo.** La sección 1 (diapositiva 'La neurona' y la de activaciones ocultas) enseña `z = W·x + b` como **pre-activación** y `a` como **la salida** de la activación. La sección 6 venía usando `aⱼ` para **la suma ponderada**, o sea justo lo contrario. Un alumno que compare las dos diapositivas encuentra la misma letra en los dos extremos de la neurona.
  - **Origen:** se heredó de las imágenes de `knowledge-library/backpropagation`, que escriben `∂yⱼ/∂aⱼ`. No lo introduje yo, pero mi diagrama nuevo lo volvió visible porque dibuja una neurona con `Σ` y `f`, igual que la 1.4.
  - **Fix:** la sección 6 pasa a **`z`**. Costó dos archivos y nada más: el símbolo solo vivía en `bp-regla-de-la-cadena.svg` y `bp-delta-salida.svg`; **la prosa de la sección nunca escribe la letra, dice 'la suma ponderada'**. Por eso se renombró la sección 6 y no la 1, que usa `z` en tres lugares.
  - **Notación fijada para la Talk:** `z` suma ponderada · `y` salida / predicción · `t` objetivo · `x` lo que entra a la unidad · `w` peso · `b` bias · `δ` sensibilidad del error respecto de `z` · `i` indexa lo que entra · `j` la unidad. **`a` no se usa en la sección 6.**
- **(2) Los índices se mezclaban.** Las entradas eran `x₁ x₂ x₃` y los pesos `w₁ⱼ`, **`wᵢⱼ`**, `w₃ⱼ`: un índice genérico metido entre dos concretos, que hace preguntarse si `i` vale 2. Pasaron a **`x₁ xᵢ xₙ`** y **`w₁ⱼ wᵢⱼ wₙⱼ`**, que es la forma de siempre para señalar 'una genérica entre muchas'.
- **(3) Se había perdido la definición que el presentador pidió explícitamente.** El 2026-08-24 pidió sumar `a = Σ xᵢwᵢ + b` "para que no se pierda"; al redibujar el gráfico con la red la saqué sin querer, y el bias no quedaba en ningún lado. Volvió como **`zⱼ = ∑ᵢ xᵢ wᵢⱼ + bⱼ`** en el panel derecho. **Lección: cuando se redibuja un diagrama desde cero hay que releer los pedidos previos sobre ese mismo diagrama.**
- **(4) La caja del error decía solo `L`.** La loss compara contra el objetivo, y el diagrama de la 4.2 ya escribe `L(y, t)`. Pasó a **`L(yⱼ, tⱼ)`**.
- Además el `∂wᵢⱼ` del denominador de la izquierda va ahora en rojo, igual que la conexión de la red: ata las dos mitades sin una línea de texto que lo explique, y eso reemplazó al cartel 'el peso que derivamos es el rojo de la izquierda'.
- Verificado en el HTML: 0 ocurrencias de `∂a` en los dos diagramas, `∂z` presente, definición con bias, `L(yⱼ,tⱼ)` y los índices nuevos.

## 2026-08-24 — Diapositiva nueva 4.5 'Qué vale cada factor'
- Status: complete
- Asks log:
  - 2026-08-24 — el presentador pasó una captura con la notación de 3Blue1Brown (`∂C₀/∂w⁽ᴸ⁾ = ∂z⁽ᴸ⁾/∂w⁽ᴸ⁾ · ∂a⁽ᴸ⁾/∂z⁽ᴸ⁾ · ∂C₀/∂a⁽ᴸ⁾`, con `∂C₀/∂a⁽ᴸ⁾ = 2(a⁽ᴸ⁾ − y)`, `σ'(z⁽ᴸ⁾)` y `a⁽ᴸ⁻¹⁾`) y pidió "agregar luego un slide con esto, creo que sumariza el cálculo".
- **Se agregó el contenido, NO la notación.** La captura choca de frente con la del mazo en tres puntos y copiarla habría reintroducido justo la confusión que se acababa de arreglar:
  - **`y` significa el objetivo ahí y la predicción acá.** Es la colisión peor, y ya figuraba como pregunta abierta del mazo (el corpus usa `y − ŷ`).
  - **`L` es el índice de capa ahí y la loss acá.**
  - **`a` es la activación de salida ahí**, y acá la sección 6 acaba de estandarizar `z` = suma ponderada, `y` = salida.
  - Además su `2(a − y)` sale de un coste sin el factor ½; el mazo sí lo lleva, así que acá el factor da la diferencia limpia.
- **Contenido de la diapositiva nueva** (`## 5. Qué vale cada factor`, entre 'La regla de la cadena' y 'El delta'): los tres factores resueltos en la notación de la Talk — `∂L/∂yⱼ = yⱼ − tⱼ`, `∂yⱼ/∂zⱼ = f'(zⱼ)`, `∂zⱼ/∂wᵢⱼ = xᵢ` — con los **mismos números ①②③** del dibujo de la diapositiva anterior, y el producto de los tres en rojo como remate.
- **Por qué hacía falta igual, más allá del pedido:** los tres valores estaban **solo en las notas del orador** desde que la 4.4 pasó a ser el dibujo de la red y perdió sus viñetas. Esta diapositiva los devuelve a la pantalla.
- Las notas del orador traen **la tabla de traducción a 3Blue1Brown**, para cuando un alumno llegue con esa versión.
- Nuevo diagrama `images/bp-factores-resueltos.svg` (440×368, ratio 1,20, que es lo que pide un `split-right`). **No tiene `.png`**, así que el modelo apunta directo al `.svg`: sin PNG existente, `_resolve_img` falla antes de que `_vector_twin` pueda entrar y sale el placeholder. **Regla: un diagrama nuevo sin PNG se referencia como `.svg`; el gemelo vectorial solo funciona cuando el `.png` existe.**
- **Costo:** la sección 6 pasa de 10 a **11 diapositivas** y el mazo de 51 a 52. La duración ya era el problema más serio del mazo (102 minutos estimados contra 90), así que esto lo empeora un poco. Se avisó al presentador.
- Renumeradas las diapositivas 5 a 10 de la sección a 6 a 11 en `final.md` y `draft.md`.

## 2026-08-24 — Las barras de fracción: un bug de conteo que arrastraban los tres diagramas
- Status: complete
- Asks log:
  - 2026-08-24 — "Revisar por qué quedó como una línea de división muy grande en los términos"
- **La causa raíz, que valía la pena encontrar.** Los generadores calculaban el ancho de cada texto con `len(cadena)`, pero las cadenas llevan **entidades HTML**: `"&#8706;L"` mide 8 caracteres y dibuja **2 glifos**. El ancho salía cuatro veces más grande, y como la x se calcula `centro - ancho/2`, **las fracciones quedaban corridas a la izquierda** además de con barras que no les correspondían.
- **Lo que se veía era el síntoma menor.** La barra ancha se notaba; el desfase de hasta 62 px entre el texto y su barra, no tanto, y estaba en los tres diagramas de fórmula.
- **Un intento de reparación automática empeoró las cosas** antes de arreglarlas: emparejaba cada texto con la barra más cercana **en Y**, y con cuatro fracciones a la misma altura eso las asignaba al azar. Se descartó y se regeneraron los tres SVG desde cero con una función `frac()` común que cuenta glifos (`&#\d+;` = 1) y dimensiona la barra como `max(numerador, denominador) + 8`.
- **Chequeo reproducible**, que ahora da 0 en los tres archivos: emparejar cada texto con la barra más cercana **en X** (no en Y), y exigir desfase < 1,5 px y sobrante entre 6 y 12 px sobre el **más ancho** de numerador y denominador. Ojo: exigir ese sobrante sobre *cada* línea da falsos positivos, porque un numerador angosto sobre un denominador ancho es tipografía correcta.
- **Lección de método:** un generador que calcula posiciones a partir de longitudes de cadena tiene que medir **glifos**, no caracteres, apenas aparece una entidad, un `<tspan>` o un acento escapado. Y conviene escribir el verificador con una regla distinta a la del generador; si comparten el error, los dos mienten igual.

## 2026-08-24 — Fuera la diapositiva 'El delta', y fuera la notación δ del mazo entero
- Status: complete
- Asks log:
  - 2026-08-24 — "Slide 39 y 38 son lo mismo. Confirmalo. Pero si es así, nos quedamos con el 38"
  - 2026-08-24 — al confirmarle que **no** eran duplicadas: "estoy de acuerdo el fusionar" + "borramos la notación en slide 39 que agrupaba" + "el slide 40 vas a tener que actualizarlo"
- **La confirmación, que era el pedido real.** No eran la misma: la 4.5 resolvía los tres factores y la 4.6 le ponía **nombre** (`δ`) a la agrupación de los dos primeros y traía el argumento de eficiencia. Se solapaban en mostrar ① y ②. **Y borrar la 4.6 sin más rompía la 4.7**, que es enteramente sobre δ.
- **Decisión del presentador: se va la diapositiva y se va la letra griega de todo el mazo.**
- **Cómo se resolvió la recursión sin δ.** El nombre existe justamente porque la propagación hacia atrás lo necesita. En vez de inventar otro símbolo se usó **la palabra que el mazo ya usaba: la culpa**. La 4.6 pasó a llamarse 'Propagar la culpa hacia atrás' y su fórmula es `culpa(j) = ( ∑ₖ culpa(k) · wⱼₖ ) · f'(zⱼ)`.
  - **Beneficio colateral:** la imagen vieja `bp-delta-oculta.png` escribía `δⱼ = (∑ₖ δₖ wⱼₖ)·yⱼ(1−yⱼ)`, con la derivada de la sigmoide incrustada — el mismo defecto que se había arreglado en el delta de salida. La nueva `bp-culpa-oculta.svg` usa `f'(zⱼ)` genérico y dibuja además las tres unidades `k` que le devuelven culpa a `j`.
- **Lo que la 4.5 absorbió de la borrada:** una cuarta viñeta y una llave en el diagrama que agrupa ① y ② con el rótulo *'se calcula una vez por unidad'*, más el número que lo justifica (una capa de 512×256 tiene 131.072 pesos y se resuelve con 256 cuentas). Es el argumento de eficiencia sin el nombre.
- **Barrido completo de δ:** además de las dos diapositivas, aparecía suelto en 'Entrenar es un ciclo de dos movimientos', en 'El ciclo completo, batch a batch' y —lejos de la sección— en la nota de normalización de la 2.3, que escribía `∂J/∂wⱼ = δ · xⱼ` **sin haber definido δ** (estaba a cuatro secciones de distancia). Los cuatro reescritos. Verificado: **0 ocurrencias de δ en el HTML**.
- La sección 6 vuelve a **10 diapositivas** y el mazo a 51: la que se agregó hoy y la que se borró se compensan.
- **Quedaron huérfanos** `images/bp-delta-salida.svg/.ascii/.png` y `images/bp-delta-oculta.png`. No se borraron; no los referencia nadie.

## 2026-08-24 — El acumulador tiene la forma de W, y ahora se ve
- Status: complete
- Asks log:
  - 2026-08-24 — "debería explicar que `g += grad` es por elemento de W. El gráfico está bien, creo que sería bueno usar notación de índice wᵢⱼ para ser claro en eso"
- **El defecto era real y silencioso.** El diagrama de 'El ciclo completo, batch a batch' escribía `g += grad`, `g = g/B`, `W = W − η·g` y `b = b − η·g`. Sin índices, `g` se lee como **un solo número** para toda la red, cuando en realidad hay **un casillero por peso**. Y el `b = b − η·g` usaba el mismo `g` para los pesos y para los bias, que directamente es falso: el bias tiene su propio gradiente.
- **Fix en el diagrama:** `gᵢⱼ += ∂L/∂wᵢⱼ` en el acumulador, con la bajada *'un casillero por peso: g tiene la forma de W'*; y el bloque de aplicación pasa a `gᵢⱼ = gᵢⱼ / B`, `wᵢⱼ = wᵢⱼ − η·gᵢⱼ`, `gᵢⱼ = 0`, con *'lo mismo para cada bias'* en vez de la fórmula equivocada.
- También se reescribió la viñeta de la diapositiva y se agregó a las notas del orador la precisión, marcada como algo que conviene decir **antes** de que un alumno lo pregunte.

## 2026-08-24 — Diapositiva nueva 4.5 'Una capa más atrás'
- Status: complete
- Asks log:
  - 2026-08-24 — el presentador pasó la cadena de cinco factores de 3Blue1Brown (`∂C₀/∂w⁽ᴸ⁻¹⁾ = ∂z⁽ᴸ⁻¹⁾/∂w⁽ᴸ⁻¹⁾ · ∂a⁽ᴸ⁻¹⁾/∂z⁽ᴸ⁻¹⁾ · ∂z⁽ᴸ⁾/∂a⁽ᴸ⁻¹⁾ · ∂a⁽ᴸ⁾/∂z⁽ᴸ⁾ · ∂C₀/∂a⁽ᴸ⁾`): "el 37 muestra un nivel y mostrar que el cálculo re-usa parte del cálculo anterior".
- **Traducida a la notación del mazo, otra vez.** Ahí el nivel de capa va en un superíndice `(L)`; acá se lee en los **índices de las unidades**: `h` entra a la oculta `i`, e `i` entra a la de salida `j`. La cadena queda `∂L/∂wₕᵢ = ∂L/∂yⱼ · ∂yⱼ/∂zⱼ · ∂zⱼ/∂yᵢ · ∂yᵢ/∂zᵢ · ∂zᵢ/∂wₕᵢ`, en el **mismo orden loss-primero** que ya usa la 4.4, no en el orden peso-primero de la captura.
- **Lo que hace que la diapositiva valga:** un recuadro rojo sobre los **dos primeros** factores, con el rótulo *'ya calculado para la unidad j'*. Son literalmente los mismos de la 4.4. Al lado, *'lo único nuevo: tres factores más'*. Eso convierte la regla de la cadena en un algoritmo: bajar una capa **estira** la cadena, no la rehace.
- **Y explica el orden del algoritmo**, que hasta ahora se afirmaba sin justificar: de adelante hacia atrás habría que rehacer la cola por cada peso; de atrás para adelante cada capa hereda el trabajo de la siguiente. De ahí sale el nombre. Es el puente natural a 'Propagar la culpa hacia atrás'.
- **Decisión de dibujo:** con dos capas no entran cuatro nodos (`Σ` y `f` por unidad, como en la 4.4), así que cada unidad se dibuja como **una caja con `Σ → f` adentro**. Se pierde el detalle de los dos pasos, que la 4.4 ya mostró, y se gana el poder mostrar dos capas.
- Las notas del orador traen la traducción a 3Blue1Brown, igual que las de 'Qué vale cada factor'.
- Nuevo `images/bp-una-capa-mas-atras.svg` (800×400, ratio 2.0, `image-full`).
- **Costo:** sección 6 a **11 diapositivas**, mazo a 52. Sumado a que hoy ya se agregó 'Qué vale cada factor' y se borró 'El delta', el neto del día es +1. El blocker de duración sigue abierto y empeorando.

## 2026-08-24 — 'Una capa más atrás' con neuronas, y tres encabezados de tabla en blanco
- Status: complete
- Asks log:
  - 2026-08-24 — "No uses cajas, sino más que sean neuronas en…" (mensaje cortado)
  - 2026-08-24 — "Hay un término que está vacío."
- **Las cajas pasaron a neuronas.** Cada unidad vuelve a dibujarse como **dos círculos**, la suma ponderada `Σ` y la activación `f`, igual que en la 4.4, con una **llave debajo** que los agrupa y los rotula ('unidad oculta i', 'unidad de salida j'). Así los cuatro valores intermedios quedan sobre los cables: `zᵢ`, `yᵢ`, `zⱼ`, `yⱼ`. La versión con cajas los escondía adentro. Lienzo 800×410.
- **El 'término vacío' no estaba en ninguna fórmula.** Se auditaron los cinco diagramas con fracciones extrayendo numeradores, denominadores y separadores por fila: las seis fracciones de 'Una capa más atrás', las cuatro de 'La regla de la cadena', las tres de 'Qué vale cada factor' y la de la culpa están **completas y bien apareadas**.
- **Lo que sí estaba vacío eran tres celdas de encabezado**, encontradas escaneando el modelo por strings en blanco: la **primera columna** de las tablas de 'Categóricas: one-hot contra embedding', 'Los tres, lado a lado' y 'L1 contra L2' tenía `header: ""`. Es la columna del factor, y dejarla sin título deja **una celda en blanco arriba a la izquierda**. Las tres pasaron a **'Criterio'**.
- **Divergencia markdown/modelo, otra vez:** solo una de las tres tablas existe como tabla en `final.md` (la de Train/Validación/Test); las otras dos son prosa en el markdown y se volvieron `columns` recién en el FILL del deck. Por eso el arreglo va en el modelo y solo una línea cambia en el markdown.
- **Chequeo reproducible que salió de acá:** escanear el modelo por campos string vacíos, y el HTML por `<span></span>`, `<li></li>`, `<p></p>` y `<text></text>` vacíos. Hoy da 0 en todos.

## 2026-08-24 — 'Qué vale cada factor' antes de 'Una capa más atrás'
- Status: complete
- Asks log:
  - 2026-08-24 — "Rotar el slide 38 con el 39."
- Orden nuevo de la sección: **4.4 La regla de la cadena → 4.5 Qué vale cada factor → 4.6 Una capa más atrás → 4.7 Propagar la culpa**.
- **El orden nuevo es mejor y conviene dejar dicho por qué.** 'Una capa más atrás' resalta dos factores con el rótulo *'ya calculado para la unidad j'*. Puesta **antes** de saber cuánto valen, esa promesa es abstracta; puesta **después**, el alumno puede señalar los dos números concretos (`yⱼ − tⱼ` y `f'(zⱼ)`) que acaba de ver. La secuencia queda: cuáles son los factores → cuánto vale cada uno → qué pasa una capa más atrás → cómo se propaga.
- Se ajustó la bajada de 'Una capa más atrás', que decía *'La diapositiva anterior siguió un peso que llega directo a la unidad de salida'* y con el intercambio dejaba de ser cierto: ahora dice *'Hasta acá seguimos un peso que llega directo…'*. También sus notas del orador, que ahora nombran los dos valores concretos en vez de referirse a 'la anterior'.
- **Al mover diapositivas hay que releer las referencias relativas.** 'La diapositiva anterior', 'la que sigue', 'como vimos recién' se rompen en silencio: ningún chequeo las mira.

## 2026-08-24 — Borrada 'Propagar la culpa hacia atrás'
- Status: complete
- Asks log:
  - 2026-08-24 — "Borrar slide 40." (confirmada la identidad antes de tocar: deck 40 = modelo 38 = 'Propagar la culpa hacia atrás')
- **Se solapaba de verdad con la diapositiva nueva.** 'Una capa más atrás' ya muestra que la cadena se estira, que la cola se reusa y por qué el recorrido va de atrás para adelante. Lo que la borrada aportaba y no estaba en ningún otro lado era **una sola cosa: que una unidad oculta alimenta a VARIAS de la capa siguiente, así que su culpa es la suma** de lo que le devuelve cada una, ponderada por el peso de conexión.
- **Ese punto se rescató**, no se perdió: una línea nueva al pie del diagrama de 'Una capa más atrás' (*'si la unidad alimenta a varias, se suma su aporte a cada una'*), un párrafo en el markdown, y en las notas del orador la analogía del jefe repartiendo culpa más la justificación del nombre del algoritmo.
- **Divergencia que se encontró de paso, y era mía.** 'Una capa más atrás' es `image-full`, plantilla que **solo dibuja título, bajada e imagen**. Sus cuatro viñetas y el párrafo de cierre vivían en `final.md` y **nunca llegaban a la pantalla** desde que creé la diapositiva. Se movieron a `### Speaker notes`, que es donde ese material sirve, y ahora markdown y deck dicen lo mismo.
  - **Regla:** al elegir `image-full` hay que mover a notas todo lo que no sea bajada o imagen. La plantilla no avisa: descarta el resto en silencio.
- La sección 6 queda en **10 diapositivas** y el mazo en 51, igual que al empezar el día pese a todo lo que se movió.
- **Huérfanos nuevos:** `images/bp-culpa-oculta.svg/.ascii` (dibujada hoy para la diapositiva que se acaba de borrar) y `images/bp-delta-oculta.png`. Sin referencias; no se borraron.

## 2026-08-24 — Optimizada 'Qué mirar cuando esto se entrena' (deck 43), y auditoría de referencias entre secciones
- Status: complete
- Asks log:
  - 2026-08-24 — "Revisar si slide 43 se puede optimizar"
- **Dos defectos reales, encontrados auditando todas las referencias cruzadas del mazo:**
  - **Puntero vencido.** La fila 'Train baja y validación sube' mandaba a la **Sección 8**, que es *Capas ocultas*. Overfitting es la **Sección 9**. Lo mismo en la card 'Objective' de la 4.1 ('los términos de regularización… aparecen en la sección 8'). Las dos corregidas.
  - **Referencias temporales invertidas.** Las notas de esta diapositiva y las de 'La regla de la cadena' hablaban de las activaciones ocultas como algo *ya visto* ('ya lo vieron en la diapositiva de las activaciones ocultas', 'ya apareció dos veces'). Pero **Capas ocultas es la sección 8 y Backpropagation la 6**: todavía no pasó. Reescritas como anuncio hacia adelante.
- **Optimización de densidad.** La diapositiva tenía una grilla de 3×5 **más tres bandas de highlight**, todo compitiendo por el mismo alto; el ajuste automático achicaba todo. Las dos bandas de 'el gradiente que se desvanece' y 'el que explota' **repetían lo que la columna del medio de la tabla ya dice**, así que pasaron a las notas del orador. Queda **una sola banda: 'Las perillas, en orden de impacto'**, que según las propias notas es *el mensaje principal* de la diapositiva y estaba enterrada como tercera.
- **Lo que NO se tocó:** las filas 4 y 5 siguen siendo punteros secos a otras secciones. Fue una decisión deliberada del 2026-08-21 para que no se confundan con problemas de gradiente.
- **Divergencia markdown/modelo, y esta vez el markdown tenía razón:** `final.md` ya decía 'Sección 9' mientras el modelo del deck decía 'Sección 8'. O sea que el deck mostraba el número equivocado aunque el outline estuviera bien.
- **Chequeo reproducible que sale de acá:** extraer del modelo todas las apariciones de `[Ss]ecci[oó]n \d+` con su contexto y cruzarlas contra la lista real de secciones (`grep '^# ' final.md`). Verifica de una el número **y** el tiempo verbal, que es donde estaban los dos errores.

## 2026-08-24 — Borrada la sección 9 completa (Overfitting)
- Status: complete
- Asks log:
  - 2026-08-24 — "Borrar toda la seccion de Overfitting"
- **Se retiraron 8 entradas del modelo:** la divisoria más siete diapositivas — el diagnóstico en dos números, sesgo contra varianza, L2, L1 contra L2, dropout, el resto del arsenal, y cuál usar según el caso.
- **Se avisó una vez, y sigue valiendo:** *overfitting y L2 estaban en el briefing original* ("como se modela, red de confusion y overfitting y L2"). La clase deja de cubrir dos de los cuatro temas pedidos al arrancar. La decisión es del presentador y la razón es de peso: el mazo venía en ~102 minutos contra 90.
- **Todo el texto quedó archivado verbatim en `# Cut material`**, con una nota que dice qué referencias había que reparar si se recupera.
- **Hallazgo importante encontrado al borrar: las dos diapositivas de Conclusiones estaban etiquetadas `section: "Overfitting"`.** Un borrado por sección se las habría llevado puestas, y además **mostraban la píldora 'Overfitting' en pantalla**, que era un error viejo y visible. Pasaron a `Conclusiones`.
- **Referencias entrantes reparadas** (todas apuntaban a una sección que ya no existe):
  - card *Objective* de 5.1: 'aparece en la sección 9' → se quitó el puntero.
  - fila de 6.10: el puntero `Sección 9` pasó a un remedio de verdad, **'Regularizar, o parar antes'**, para que la fila no quede sin respuesta.
  - notas de 2.5 y 3.4: los dos 'puente hacia overfitting' se reescribieron sin nombrar la sección.
  - notas de 8.3: cargaban el `Goal of this section` de Overfitting; se quitó.
  - Agenda y `deck.sections`: sale la entrada 9.
- **El mazo queda en 46 diapositivas de contenido, o sea unos 92 minutos a dos minutos por diapositiva.** El blocker de duración, que venía siendo el problema más serio desde el 2026-08-21, queda prácticamente resuelto.
- **Huérfanas ahora:** `s9-2-1-curvas-overfitting`, `s9-3-1-objetivo-l2`, más las tres de la ronda anterior. No se borraron.

## 2026-08-25 — Diapositiva 2.1: se quitó el contraste con la imagen del diagrama
- Status: complete
- Asks log:
  - 2026-08-25 — "Borrar el texto 'en una imagen, en cambio, mover un píxel sí cambia el dato' y el separador. Es redundante"
- **Era la tercera vez que se decía lo mismo en la misma diapositiva.** El cuerpo ya cierra con "En una imagen sí se la quitaría, porque ahí la posición del píxel es parte del dato", y las notas del orador lo repiten. El diagrama lo decía una vez más, abajo de todo y separado por una regla horizontal, o sea con el peso visual de un remate.
- **Qué se tocó:** el separador (`<path>` a y=344) y las dos líneas de texto salieron del SVG; el lienzo bajó de 380×400 a 380×342 para que no quedara aire muerto; se regeneraron `images/s2-1-1-orden-de-columnas.png` (1200×1080) y su copia de crítica. Se sincronizó el `ascii-source` en `final.md` **y** en `draft.md`, el `.ascii` de `images/`, y el hash `talksmith-ascii-sha256` del SVG. Del `ascii-note` salió el matiz "el contraste final con la imagen va en tono secundario", que ya no aplica.
- **Pendiente para el presentador:** el deck HTML de `output/html/index.html` lleva las imágenes embebidas en base64, así que sigue mostrando la versión vieja hasta que se vuelva a renderizar.

## 2026-08-25 — Diapositiva 2.4: el embedding no es la matriz, es una fila
- Status: complete
- Asks log:
  - 2026-08-25 — "Slide 13 es confuso. A que se refiere que el embedding es una matrix si lo que la red toma son solo vectores?" → opción 1 (reordenar el bullet y ampliar el diagrama)
- **La contradicción era real y la diapositiva se la buscaba sola.** El bullet abría con "una tabla de `k × d` floats entrenable", que se lee como input, y recién cerraba con el dato que la desarma ("un embedding de dimensión 24 usa 24 floats"). Contra la tesis de la clase — la red ve una fila de números — el arranque del bullet suena a que entra una matriz.
- **El punto que faltaba decir:** la tabla `k × d` es un **parámetro**, con el mismo estatus que la `W` del panel de one-hot; lo que entra al vector es **una fila**, `d` floats, elegida por el índice de la categoría.
- **Bullet reordenado:** ahora abre con "aporta al vector `d` floats, no `k`" y después explica de dónde salen. El párrafo de cierre arranca con "las dos matrices tienen el mismo estatus" antes de la equivalencia con la capa lineal sin sesgo, que ya estaba.
- **Diagrama rehecho en dos filas** (`s2-4-1-one-hot`, 680×372, antes 680×300, solo one-hot). Idea de diseño: **el rojo marca lo que entra al vector y el gris lo que es peso**, así que la respuesta a la pregunta está en el color, sin texto. Fila 1 one-hot, las cuatro celdas en rojo y `W` en gris; fila 2 embedding, las tres celdas de la fila en rojo y la tabla `k × d` en gris con su primera fila marcada y una flecha hacia las celdas. Remate al costado: "en los dos casos la matriz es un peso de la red, no una entrada".
- **Notas del orador:** la pregunta quedó anticipada con su respuesta, más el matiz de que con embedding la multiplicación por el one-hot se saltea y se busca la fila directo — la misma cuenta, más barata.
- **Sincronizado:** `final.md`, `draft.md`, `images/s2-4-1-one-hot.ascii`, el SVG con su hash, y los dos PNG (1200×656). El alt de la imagen pasó de "One-hot selecciona una columna de W" a "Lo que entra al vector contra lo que es peso de la red".
- **Pendiente para el presentador:** `output/html/index.html` y `output/slide-model.json` siguen con la versión vieja de esta diapositiva y de la 2.1 hasta que se vuelva a renderizar.

## 2026-08-25 — Step 7 (Render) — html-strict, re-render
- Status: complete
- Asks log:
  - 2026-08-25 — "regenerar el html-strict"
- **FILL dirigido, no un re-fill del mazo entero.** Solo cambiaron dos diapositivas, así que se actualizaron esas dos en `output/slide-model.json` y se volvió a sellar contra `final.md`. Un re-fill completo habría vuelto a clasificar 47 diapositivas de contenido que el presentador ya revisó, con riesgo de churn y sin ganancia. Por lo mismo se salteó el paso 1.6 (classify-review): ninguna clasificación cambió.
- **Lo que se corrigió en el modelo, que el markdown no cubría:** la tabla de la 2.4 tenía en pantalla la fila "Qué es → Una tabla de `k × d` floats entrenable", que era **la fuente literal de la confusión** y vivía solo en el modelo del deck, no en `final.md`. La tabla pasó de 4 filas a 5, encabezada por **"Qué entra al vector"** (`k` floats contra `d` floats, una fila) y seguida de **"Qué es esa matriz"** (`W` y la tabla `k × d`, las dos pesos de la red). El segundo takeaway pasó a ser "La matriz nunca es la entrada". Las notas se levantaron verbatim de `final.md`, que antes estaban condensadas.
- **Audits en verde:** `degenerate_enum` ok, `field_coverage` ok, `image_coverage` ok, `template_diversity` sin `fallback` (11 plantillas sobre 47 diapositivas de contenido; el `[no-alternative]` de 47/47 es previo y viene de que el modelo se escribió sin trazas `_choice`).
- **Render:** 57 diapositivas → `output/html/index.html`, más la portada del directorio raíz. Los dos diagramas entran **inlineados como SVG vectorial**, no como PNG: el renderer resuelve la referencia `.png` a su compañero `.svg`. Verificado que las cadenas viejas ("cada categoría selecciona su propia columna de pesos en W", "mover un píxel") ya no están y las nuevas sí.
- **Ruido conocido, no bloqueante:** tres iconos (`remove_red_eye`, `check_circle_outline`, `signal_wifi_statusbar_connected_no_internet_4`) no resuelven contra el catálogo de Material Symbols y caen a `info`. Es previo a este render.

## 2026-08-25 — Atribuciones con link
- Status: complete
- Asks log:
  - 2026-08-25 — "Revisar que todas las notas como 'Fuente: Roboflow…' tengan link"
- **Barrido del mazo entero**, no solo del ejemplo citado: `final.md`, `draft.md` y `output/slide-model.json`, buscando atribuciones por palabra clave (Fuente, Adaptado, Basado en, et al, años entre paréntesis) y por nombre de fuente conocida (Roboflow, Keras, Stanford, CS231n, arXiv, Google, Russell, Norvig, Bishop, Goodfellow, Medium…).
- **Resultado: una sola atribución llegaba a pantalla**, la de la 3.4, y estaba sin link. Ahora lleva los dos títulos enlazados.
- **La atribución vivía solo en el modelo del deck, no en `final.md`** — la había escrito el FILL de un render anterior. Un re-fill completo la habría perdido. Se agregó el párrafo `Fuente:` al final del Content de la 3.4 en `final.md` **y** en `draft.md`, así queda en la fuente y sobrevive cualquier render.
- **Las dos citas se verificaron contra las capturas de `research/web/`, no de memoria**, y aparecieron tres correcciones:
  - **Autor faltante.** El artículo de Roboflow es de **Jacob Solawetz**, dato que estaba en el registro del corpus y no en la cita.
  - **Título desactualizado.** La página se llama hoy *"Train, Validation, Test Split Explained (with Ratios)"*; la cita usaba el título viejo. Con link, el título tiene que coincidir con lo que se abre.
  - **Medium devuelve 403 y puede tener muro de pago.** Se enlazó el **original del propio autor** (`tarangshah.com`, HTTPS, 200, sin muro), que el registro del corpus ya tenía anotado. Para una clase donde los alumnos hacen clic, importa.
- **Los dos links verificados con una petición real:** Roboflow 200, tarangshah.com 200.
- **Hallazgo abierto:** hay **5 diapositivas más** cuyo bloque `### Sources` tiene URLs externas (Google ML Crash Course, CS231n ×3, Keras ×4, el paper de Pascanu/Mikolov/Bengio en arXiv) y que **no muestran ninguna atribución en pantalla**. No se tocaron: agregarlas es contenido nuevo, no el pedido. Decisión del presentador.

## 2026-08-25 — Diapositiva 5.7 nueva: Los términos de regularización
- Status: complete
- Asks log:
  - 2026-08-25 — "Agregar al final de funcion de perdida un slide con esta definicion [términos de regularización, L1/L2/Elastic Net/Dropout]"
- **Dónde encaja, y por qué encaja bien.** La 5.2 define `objective` como "el cost más los términos de regularización, cuando las hay" y hasta hoy esa era una promesa sin cobrar: la sección que la respondía era la 9, borrada el 2026-08-24 por presupuesto de tiempo. La 5.7 cierra ese hilo dentro de la misma sección. Se le agregó el puntero explícito a la card `Objective` de la 5.2, en `final.md` y en el modelo.
- **Plantilla `content+cards+image`**, `split-right`: lead con la definición, cuatro cards (L2, L1, Elastic Net, Dropout) y el diagrama al costado. Se descartó `value-columns` porque Dropout no tiene fórmula, así que las cuatro filas no se leen a través de factores compartidos — son atributos heterogéneos, que el catálogo manda a cards. El `_choice` quedó registrado con los candidatos y el motivo de cada descarte; es el único slide del mazo que lleva traza.
- **Diagrama nuevo `s5-7-1-objetivo-regularizacion`** (680×296): `J = cost + λ · R(w)` con las dos llaves anotadas, en la gramática visual del `s9-3-1-objetivo-l2` que quedó huérfano al borrar la sección 9, pero en **forma general** en vez de específica de L2, que es lo que la diapositiva necesita. El acento rojo va en el término de penalización, que es lo que la diapositiva agrega.
- **Bug de inserción, encontrado y corregido.** El ancla que usé para insertar cayó en el **penúltimo** párrafo de las notas de la 5.6, no en el último, así que dos párrafos de "Las especializadas" (el de cuantiles y el de ranking/supervivencia) quedaron colgados dentro de la 5.7. Se devolvieron a su diapositiva. **Lección: al insertar una diapositiva al final de una sección, anclar en el separador `---` o en el encabezado siguiente, nunca en un párrafo de prosa.**
- **Duración — el blocker vuelve a moverse en la dirección equivocada.** El mazo pasa de 47 a **48 diapositivas de contenido**, o sea ~96 minutos a dos minutos por diapositiva, contra un presupuesto de 90. El 2026-08-24 se había bajado a ~92 borrando la sección 9 entera, y esta diapositiva **restituye parte de ese material** (L2, L1, dropout) en forma condensada: una diapositiva donde antes había siete. Es un buen canje, pero el excedente vuelve a existir y es decisión del presentador.
- Audits en verde; render 58 diapositivas.

## 2026-08-25 — Diapositiva 5.4 (BCE): lead partido y una card retirada
- Status: complete
- Asks log:
  - 2026-08-25 — "Partir 'Salida de una neurona con sigmoide… Siempre queda un solo término vivo.' y poner parte de este texto como desc con el resto"
  - 2026-08-25 — "Borra 'La sigmoide va en un solo lado'. Y todo el texto que tiene."
- **Otra vez el mismo patrón: el texto vivía en el modelo del deck, no en `final.md`.** El `lead` cargaba tres cosas en un párrafo — el setup, la fórmula y cómo se lee la fórmula — porque el FILL de un render anterior concatenó lo que en `final.md` eran tres bloques separados.
- **El corte se eligió por consistencia con las hermanas de sección, no a ojo.** La 5.5 (cross-entropy) lleva setup más fórmula corta en el lead y el detalle en las cards; la 5.3 (MSE/MAE/Huber) pone las fórmulas en las cards. La 5.4 era la única con las tres cosas juntas. Ahora el lead queda en setup más fórmula y "Con `t = 1` sobrevive el primero…" pasó a ser la primera card, **Siempre queda un solo término vivo**, con la frase de por qué (`t` vale 0 o 1, el otro término se multiplica por cero) que antes solo estaba en las notas.
- **Card retirada:** "La sigmoide va en un solo lado", entera y con su texto. Archivada verbatim en `# Cut material` con nota de qué queda colgando.
- **Dos referencias quedan sin apoyo visible y no se tocaron** (es contenido, decisión del presentador): la card que sigue, "Con logits crudos hay que convertir al predecir", da por explicado qué es un logit crudo, y eso lo explicaba la card retirada; y el párrafo de notas sobre el error de la doble sigmoide se quedó sin anclaje en pantalla.
- La 5.4 queda en 3 cards. Audits en verde; render 58 diapositivas.

## 2026-08-25 — Notebook de la capa de salida, y links a los dos desde el mazo
- Status: complete
- Asks log:
  - 2026-08-25 — "De la misma manera que generamos input-data-types y un sample, generemos también uno para el output" → "¿Podemos usar el mismo dataset de casas?" → "Tal vez en vez de predecir el precio tenemos que predecir algo distinto" → "Hacé un link en la presentación tanto al input como al output"
- **La corrección del presentador mejoró el diseño.** La primera versión inventaba un universo paralelo de casas. Reusar `input-data-types.csv` y **dar vuelta el rol del precio** — de respuesta a entrada — convierte el notebook en la demostración literal de la tesis: mismas 2000 casas, misma matriz de 118 floats, siete tareas distintas, y lo único que se mueve es la última capa.
- **Entregables:** `missions/clase3/output-layer-types-gen.py` (generador reproducible que deriva los objetivos del CSV de entrada), `output-layer-types.csv`, `build_output_notebook.py` (el notebook se escribe desde un script, no a mano) y `output-layer-types.ipynb`, 39 celdas, ejecutado y con las 8 figuras adentro.
- **Siete secciones, una por familia de salida**, cada una con la forma incorrecta entrenada al lado: continuo (MSE contra Huber), conteo (lineal+MSE contra softplus+Poisson), binaria (lineal+MSE contra sigmoide+BCE), multiclase (número redondeado contra softmax+CE), multi-etiqueta (softmax contra N sigmoides), rango (promedio contra pinball) y distribución (sigma constante contra NLL gaussiana).
- **Lo que más trabajo dio, y es la parte que importa: la primera corrida enseñaba mentiras.** En cuatro secciones la forma "incorrecta" ganaba o empataba. No se maquilló ninguna: se diagnosticó cada una y se arregló la causa.
  - **Conteo y regresión:** la señal era demasiado débil frente al ruido. Se retuneó el generador (`mu_dias` de 46−13·atractivo a 60−30·atractivo, lambda de visitas con más rango) hasta que el baseline quedó 2,8× el piso teórico.
  - **Binaria:** sigmoide+MSE contra sigmoide+BCE da **empate real** en este problema, y forzar un ganador habría sido falsear. Se cambió el contraste por el que sí es cierto y demostrable: **lineal+MSE contra sigmoide+BCE**, donde la incorrecta devuelve 17 valores fuera de [0,1] que no son probabilidades.
  - **Distribución:** la sigma aprendida salía plana. Dos causas: la heterocedasticidad estaba atada al precio, que ya entraba en la señal de la media, y la NLL sobreajustaba achicando sigma hasta memorizar los residuos de train. Se ató la sigma a `tipo_vivienda` — una variable que **no** entra en la media, así que es señal separable — y esa sección lleva su propia receta con dropout y paciencia 60. Ahora aprende 13,8 / 14,6 / 17,2 / 25,7 días contra los 5 / 11 / 18 / 30 generados: comprime los extremos pero el orden y la magnitud relativa salen, y el notebook lo dice así en vez de exagerar.
  - **Todo el notebook pasó a early stopping con `restore_best_weights`.** Sin eso varias secciones comparaban dos redes sobreajustadas, y el resultado decía más sobre cuánto memorizaron que sobre la loss.
- **Honestidad donde no cierra:** los cuantiles quedan en P10 15,7% y P90 81,0% contra el 10/90 pedido. Está escrito en el notebook como limitación, no tapado: el contraste que importa sigue siendo que el promedio cubre 47,7% cuando se lo usa para prometer una fecha.
- **Links en el mazo, en tres lugares:** diapositiva nueva **9.3 "Los notebooks de la clase"** (`closing-cta`, con GitHub y Colab para cada uno), más una referencia en contexto en la **2.6** (tabla de decisiones → notebook de entrada) y en la **4.1** (catálogo de salidas → notebook de salida). Los links de GitHub se verificaron con petición real: el repo es público y el notebook de entrada devuelve 200.
- **Pendiente del presentador:** `output-layer-types.ipynb` **todavía no está pusheado**, así que su link va a dar 404 hasta el próximo push. El de entrada ya funciona.
- **Duración:** el mazo pasa a 49 diapositivas de contenido, ~98 minutos contra 90.

## 2026-08-26 — "Percentiles" en vez de "cuantiles", y el `k` de la 4.1
- Status: complete
- Asks log:
  - 2026-08-26 — "No usemos Cuantiles (P10/50/90) sino hablemos de percentiles"
  - 2026-08-26 — "¿Por qué el slide 23 dice k salidas si en realidad se están modelando 3? Confirmar esto"
- **Renombre completo**, no solo donde saltaba a la vista: 7 en `final.md`, 7 en `draft.md`, 6 en el modelo del deck, 2 en el generador del dataset y 9 en el notebook. Se dejó `np.quantile` sin tocar: es la API de numpy, no vocabulario de la clase. También se dejó **pinball** como nombre de la loss, en vez de "quantile loss", que habría reintroducido el término por la puerta de atrás.
- **El `k` era una inconsistencia real, y confirmada.** La fila decía "Percentiles (P10, P50, P90)" y en la columna Neuronas ponía `k`. Pero la fila **ya eligió cuáles son**: son tres, así que el número es 3. Ahora dice **"3, uno por percentil"**.
- **La distinción que hace que valga la pena arreglarlo, y que quedó en las notas del orador:** en esa tabla `N` aparece donde el número **lo pone el problema** (cuántas clases hay, cuántos tags), y en la fila del rango **lo pone quien modela** — con P50 y P95 solos serían 2. Es la única fila donde el número es una decisión y no un dato, y escribir `k` ahí tapaba justamente eso.
- Mismo arreglo en el notebook: el título de la sección 6 pasó de "k neuronas lineales" a "una neurona por percentil", la tabla final dice 3, y se agregó una nota al pie que explica qué es fijo, qué lo pone el problema y qué lo pone quien modela.
- Deck re-renderizado, audits en verde. Notebook re-ejecutado, 40 celdas, sin errores.

## 2026-08-26 — Diapositiva 5.7 nueva: Percentiles, la pinball loss
- Status: complete
- Asks log:
  - 2026-08-26 — "Creemos un slide con Pinball loss, similar a los anteriores, después del 32. Lo importante acá es mostrar cómo en realidad se entrena con un valor y la función de pérdida es lo que define el resto"
- **El ángulo que pidió el presentador es el mejor de la sección y conviene registrarlo:** la loss no *mide* el error, lo **define**. Hasta la 5.6 la sección se podía leer como "elegimos la fórmula que mejor mide la distancia". Acá se ve que la fórmula además elige **qué estadístico** va a terminar aprendiendo el modelo. El dataset trae un número por fila y ninguna columna dice cuál es el P90; el P90 aparece porque la loss empuja ahí.
- **La correspondencia loss-estadístico es el contenido:** el minimizador de MSE es el promedio, el de MAE la mediana, el de pinball con `q` el percentil `q`. Y el corolario que ordena: **MAE es pinball con `q = 0,5`** — no son dos losses, es una familia con un parámetro. Eso además explica hacia atrás por qué MAE es robusta y MSE no, que ya se había visto en la 5.3.
- **Diagrama `s5-7-1-pinball`** (900×400), en la gramática visual del `s5-3-1-penalizacion-regresion`: dos paneles con la misma V, simétrica a la izquierda (q=0,5) y con pendiente 0,1 contra 0,9 a la derecha (q=0,9). El remate al pie es la tesis: el dato de entrenamiento es el mismo número en los dos casos.
- **Se pisó la trampa del manual de estilo y se corrigió:** los `<tspan>` en línea dentro de un `<text text-anchor="middle">` salieron desplazados en el render, exactamente como advierte `diagram-style.md`. Se reemplazaron por líneas propias ("el mínimo cae en la" / "MEDIANA" en dos renglones), que además lee mejor.
- **Renumeración:** la de regularización pasó de 5.7 a 5.8, y se actualizó el puntero de la card `Objective` de la 5.2, que la nombraba por número.
- La diapositiva quedó **en la posición 33**, justo después de la 32 como se pidió. Audits en verde; deck en 60 diapositivas, 49 de contenido, ~98 minutos.

## 2026-08-26 — "Los términos de regularización" se muda a la sección 6
- Status: complete
- Asks log:
  - 2026-08-26 — "Mover 'Los términos de regularización', ¿realmente tiene sentido al final de backpropagation?" → sí, pero no al final del todo: entra como 6.10, **antes** del checklist
- **El argumento que decide, y conviene tenerlo escrito:** un término de regularización **se define** en la función de costo pero **actúa** en el paso de actualización. En la sección 5, antes de que existan el gradiente y el paso, "penalizar pesos grandes" es una afirmación que el alumno no puede cobrar. Después de la 6.7 sí: el gradiente de `λΣw²` es `2λw`, o sea que el paso le resta a cada peso una fracción de sí mismo — que es literalmente el *decay* de weight decay.
- **La ubicación exacta importa y no es "al final".** Se puso **antes** de "Qué mirar cuando esto se entrena", no después, por dos razones. Esa diapositiva es el clímax de la sección, la que las notas describen como la que los alumnos van a fotografiar, y ponerle algo detrás la debilita. Y su fila **"train baja y validación sube → Regularizar, o parar antes"** era **el único renglón del checklist cuya acción no se explicaba en la sección**: ahora apunta a la diapositiva inmediatamente anterior.
- **La diapositiva se reescribió, no se mudó y ya.** Mudarla sin tocarla habría desperdiciado el motivo de la mudanza. El lead ahora dice por qué está ahí, y las cards de L2 y L1 pasaron de describir el efecto a mostrar el mecanismo: `2λw` contra `λ·signo(w)`, y por qué el segundo llega a clavar pesos en cero y el primero no. Dropout quedó explícitamente marcado como el que **no** toca el gradiente.
- **Renumeración y punteros:** sección 5 queda en 7 diapositivas (cierra con la pinball), sección 6 pasa a 11. El diagrama se renombró de `s5-7-1-objetivo-regularizacion` a `s6-10-1-...`. El puntero de la card `Objective` de la 5.2 dejó de nombrar un número de diapositiva — ahora dice "la sección 6 muestra cuáles son, una vez que el gradiente esté sobre la mesa", que sobrevive a la próxima renumeración.
- **Chequeo de referencias cruzadas corrido sobre todo el mazo:** 16 menciones a secciones, todas apuntan a una sección que existe. Ninguna quedó apuntando a la 9, que está borrada.
