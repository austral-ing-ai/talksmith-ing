# memory.md — modelado-redes-neuronales

**Current step:** 5 (Review) — awaiting_presenter
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

