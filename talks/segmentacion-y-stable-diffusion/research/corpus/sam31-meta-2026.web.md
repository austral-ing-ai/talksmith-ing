---
source_file: sam31-meta-2026
source_type: web-capture
ingested_at: 2026-08-14
---

# SAM 3.1: Faster and More Accessible Real-Time Video Detection and Tracking With Multiplexing and Global Reasoning — blog de Meta AI

## Provenance
- Original location: `research/web/sam31-meta-2026/`
- Format: web-capture (post de blog corporativo; `page.md` + `original.html` + `assets/`)
- URL: https://ai.meta.com/blog/segment-anything-model-3/
- Author / source (if known): Meta AI (post institucional, sin firma individual). © Meta 2026.
- Date of original (if known): **27 de marzo de 2026** (actualización SAM 3.1). El post original de lanzamiento de SAM 3 es anterior (noviembre de 2025) y quedó embebido debajo de la actualización. Tiempo de lectura declarado: 15 minutos.
- Fetched at: 2026-08-14T17:03:10Z (HTTP 200, 216.624 bytes de HTML)
- Rol en la Clase 9: la fuente más extensa del conjunto (~35.000 caracteres de `page.md`) y **la única no académica**. Es un **anuncio de producto**, no un paper: mezcla resultados técnicos con posicionamiento comercial, integración en Instagram/Facebook y llamados a la acción. Hay que tratarla como tal.

## Key claims

### Actualización SAM 3.1 (27 de marzo de 2026)

- SAM 3.1 se presenta como **"drop-in replacement" de SAM 3**: reemplazo directo, sin cambios de integración.
- La novedad es el ***object multiplexing***: el modelo **sigue hasta 16 objetos en un solo forward pass**.
- Efecto declarado: **duplica la velocidad de procesamiento** en videos con una cantidad media de objetos, subiendo el throughput de **16 a 32 frames por segundo en una sola GPU H100**.
- Consecuencia práctica: seguimiento de objetos en tiempo real en videos complejos **reduciendo el requerimiento de GPU**, lo que "hace viables aplicaciones de alto desempeño en hardware más chico y accesible".
- Explicación del mecanismo: antes **cada objeto requería su propio pase dedicado**; con multiplexing todos los objetos rastreados se procesan juntos, **eliminando cómputo redundante y cuellos de botella de memoria**. Meta llama a esto ***global reasoning*** y afirma que además **mejora la exactitud en escenas concurridas**.
- Se liberan: checkpoint de SAM 3.1 en Hugging Face (`facebook/sam3.1`), actualizaciones al codebase de SAM 3 y al research paper, y el modelo actualizado en el Playground.

### Lanzamiento original de SAM 3

- SAM 3 es **un modelo unificado de detección, segmentación y seguimiento** en imágenes y video, usando prompts de **texto, ejemplar y visuales**.
- Se libera con **checkpoints, datasets de evaluación y código de fine-tuning**.
- Se lanza el **Segment Anything Playground**, plataforma para que cualquiera pruebe los modelos sin conocimiento técnico.
- Integración de producto: efectos en **Edits** (la app de creación de video de Instagram), experiencias en **Vibes** (app de Meta AI) y en meta.ai; y la función **"View in Room" de Facebook Marketplace** (con SAM 3D).
- En paralelo se libera **SAM 3D** (reconstrucción 3D de objetos y humanos desde una sola imagen).
- Con Conservation X Labs y Osa Conservation lanzan **SA-FARI**, dataset público de video para monitoreo de fauna.
- **Capacidad central: *promptable concept segmentation*** — encontrar y segmentar **todas** las instancias de un concepto definido por un prompt de texto o de ejemplar.
- El problema que ataca: los modelos tradicionales trabajan con **un conjunto fijo de etiquetas de texto**. Pueden segmentar "person", pero fallan con conceptos matizados como "the striped red umbrella".
- **Ganancia declarada: 2× sobre los sistemas existentes** en el benchmark SA-Co, en imagen y en video.
- Arquitectura: encoders de texto e imagen del **Meta Perception Encoder**; detector basado en **DETR**; tracker construido sobre el **memory bank y memory encoder de SAM 2**.
- Velocidad de SAM 3: **30 milisegundos por imagen con más de 100 objetos detectados en una GPU H200**. En video la latencia **escala con la cantidad de objetos**, sosteniendo desempeño casi en tiempo real para **~5 objetos concurrentes**.
- **SAM 3 Agent**: un MLLM que usa SAM 3 como herramienta, propone frases nominales, analiza las máscaras devueltas e itera. **Sin entrenar en datos de referring/reasoning segmentation**, supera trabajos previos en ReasonSeg y OmniLabel.

## Definitions and terminology

- **Vocabulario abierto (*open vocabulary*).** Esta es **la mejor definición explícita del término en todo el corpus**: "SAM 3 accepts text prompts — **open-vocabulary short noun phrases** — and image exemplar prompts, **eliminating the constraints of fixed label sets**." Contrastada además con el estado previo: "Traditional models often focus on object segmentation with a fixed set of text labels, restricting their ability to address the full spectrum of user requests". El abstract de arXiv de SAM 3 expresa la idea pero no usa la expresión; si la clase define vocabulario abierto, la cita va acá.
- **Promptable concept segmentation (PCS).** "Finding and segmenting **all instances** of a concept defined by a text or exemplar prompt."
- **Concept prompts vs. visual prompts.** El post separa explícitamente dos familias: **concept prompts** (frases nominales simples, ejemplares en imagen) y **visual prompts** (máscaras, cajas y puntos, "which were introduced in SAM 1 and SAM 2"). Esta distinción es más limpia que la del abstract y es directamente utilizable en clase para narrar la evolución SAM 1 → SAM 3.
- **Data engine.** "A scalable data engine that leverages SAM 3, human annotators, and AI models in the loop." Descrito con detalle: un pipeline de modelos de IA (incluido un captioner basado en **Llama**) mina imágenes y video, genera captions, las parsea en etiquetas de texto y crea máscaras iniciales ("candidates"); humanos y anotadores de IA verifican y corrigen; el bucle retroalimenta el entrenamiento. **Es la explicación de data engine más completa del corpus** — los abstracts de SAM 1 y SAM 2 nombran el concepto sin desarrollarlo.
- **Anotadores de IA.** Modelos **Llama 3.2v** entrenados específicamente para igualar o superar la exactitud humana en tareas de anotación: verificar si una máscara es de alta calidad, o si todas las instancias de un concepto están enmascaradas exhaustivamente.
- **Ontología de conceptos.** "A dictionary of concepts and their relationships based on Wikipedia", usada para mapear etiquetas de texto a un espacio conceptual compartido y aumentar la cobertura de conceptos poco frecuentes.
- **Banco de memoria (memory bank).** Confirmación explícita del linaje: "The memory bank and memory encoder used in **SAM 2** is the basis for the **Tracker** component" de SAM 3. Es el mejor respaldo textual del corpus para el término que la clase usa al explicar SAM 2.
- **Masklet.** "SAM 3 tracks every object with a **SAM 2-style masklet**" — la máscara con identidad que persiste a lo largo del video. El término no aparece en el abstract de SAM 2; acá sí.
- **Object multiplexing / global reasoning.** Los dos términos que SAM 3.1 acuña: procesar hasta 16 objetos en un solo forward pass (multiplexing) razonando sobre todos a la vez en lugar de por separado (global reasoning).
- **Presence head.** No se menciona en el post (sí en el abstract de arXiv). Cada fuente cubre una parte distinta de la arquitectura.
- **Métricas nombradas.** El post —vía la figura de resultados— nombra y cuantifica **cinco métricas de evaluación**: **cgF1**, **pHOTA**, **J&F**, **mIoU** y **gIoU**. El propio texto glosa la primera: cgF1 es "a measure of how well the model can recognize and localize concepts".

## Evidence and examples

### Cifras de SAM 3.1
- **16 objetos** por forward pass (multiplexing).
- **16 → 32 fps** en una sola **H100**: duplicación del throughput en videos con cantidad media de objetos.

### Cifras de SAM 3
- **Más de 4 millones de conceptos únicos** en el training set del data engine.
- Aceleración de anotación: **~5× más rápido que humanos en prompts negativos** y **36% más rápido en prompts positivos**, incluso en dominios de grano fino.
- Delegar tareas en anotadores de IA **más que duplica el throughput** frente a un pipeline sólo humano.
- **30 ms por imagen** con **más de 100 objetos** detectados en **H200**.
- Casi tiempo real para **~5 objetos concurrentes** en video (SAM 3, antes del multiplexing de 3.1).
- Preferencia de usuarios: **~3 a 1** a favor de SAM 3 sobre OWLv2, la línea base más fuerte.
- **SA-FARI**: más de **10.000 videos de cámaras trampa**, más de **100 especies**, anotados con cajas y máscaras **para cada animal en cada frame**.

### Números de benchmark (de la figura de resultados; transcripción completa en `## Images / diagrams`)
- **Concept Segmentation, imágenes, SA-Co Gold (cgF1):** Human 72,8 · SAM 3 **53,9** · OWLv2 24,6 · Gemini 2.5 Pro 13,0.
- **Concept Segmentation, video, SA-Co SA-V (pHOTA):** Human 70,5 · SAM 3 **58,0** · LLMDet + SAM3 Tracker 30,1 · GLEE 11,8.
- **Visual Segmentation, video, SA-V test (J&F):** SAM 3 **84,4** · SeC 81,7 · SAM2Long 81,2 · SAM 2.1 L 78,4.
- **Visual Segmentation, imágenes, SA-37 (mIoU a 3 clics):** SAM 3 **81,3** · SAM 2.1 L 80,3 · SAM 1 H 77,0.
- **Counting, CountBench (Accuracy):** SAM 3 **93,8** · Molmo-72B 92,4 · Gemini 2.5 Pro 92,4 · Qwen-VL-72B 86,7.
- **Reasoning Segmentation, ReasonSeg Test (gIoU):** SAM 3 + Gemini 2.5 Pro **74,0** · LISA-13B (LLaVA1.5) 61,3 · X-SAM (Phi-3-3.8b) 57,8 · RSVP (GPT-4o) 55,4.

### Verificación de cifras del deck

- **"Marzo 2026" para SAM 3.1 — CIERRA exactamente.** El post está fechado **27 de marzo de 2026** y abre con "***Update March 27, 2026***". Corroboración independiente: la v2 del paper de SAM 3 en arXiv se subió el **28 de marzo de 2026** (ver `sam3-carion-2025.web.md`), un día después del anuncio. La fecha del deck es correcta y verificable por dos caminos.
- **Métrica de evaluación — esta fuente cubre el hueco del deck.** El deck da 22 slides de segmentación sin definir Dice ni IoU. La figura de resultados de este post nombra y cuantifica cinco métricas, entre ellas **mIoU** (81,3 para SAM 3 a 3 clics sobre SA-37) y **gIoU** (74,0 en ReasonSeg). Es material listo para la slide de métricas que el deck no tiene. Dice sigue sin aparecer en ninguna fuente del corpus.
- La cifra del **"~95% del cómputo"** del image encoder de SAM (slide 20) tampoco aparece acá — este post no descompone el costo de inferencia de SAM 1. Ver `sam-kirillov-2023.web.md`.

## Inconsistencies / open questions

1. **Es un anuncio de producto, no un paper — y el registro se nota.** Frases como "incredible adoption", "we're pleased to introduce", "a significant boost", "we can't wait to see how people use it" conviven con números de benchmark. Buena parte del post es posicionamiento comercial: Instagram Edits, Vibes, Facebook Marketplace, Playground, ofertas de trabajo. Al citarlo en clase conviene separar explícitamente **lo medido** (fps, cgF1, latencia) de **lo declarado** (adopción, facilidad de uso, impacto). A diferencia de un abstract de arXiv, nada de esto pasó por revisión de pares.
2. **A diferencia de las 13 páginas `abs`, acá el problema no es que falte contenido: el post es rico y trae figuras reales.** El hueco es otro — **no hay tablas completas, ni condiciones experimentales, ni desvíos estándar, ni descripción del protocolo de evaluación**. "16 a 32 fps" no dice qué resolución de video, qué largo, ni qué significa "medium number of objects". El "2×" y el "~5× más rápido en negativos" carecen de intervalo de confianza. Para la clase alcanza; para sostener una afirmación fuerte, no.
3. **SAM 3 sigue muy por debajo del humano en su propia tarea insignia.** La figura lo muestra sin disimulo: **53,9 vs 72,8 de cgF1** en imágenes (74% del desempeño humano) y **58,0 vs 70,5 de pHOTA** en video. El texto del post elige el encuadre "doubles the accuracy of existing systems" —cierto respecto de OWLv2 (24,6) y de LLMDet+SAM3 Tracker (30,1)— y no menciona la brecha con el humano, que la figura sí expone. **La misma figura sostiene los dos relatos.** Es un ejemplo didáctico excelente de cómo se elige una línea base.
4. **La ganancia sobre SAM 2 en segmentación visual es marginal.** J&F 84,4 vs 81,7 de SeC y 81,2 de SAM2Long; mIoU 81,3 vs 80,3 de SAM 2.1 L. El salto grande de SAM 3 está en la tarea nueva (conceptos), no en la vieja. El post dice "matching or exceeding the state-of-the-art performance of previous models like SAM 2", lo cual es honesto, pero la palabra "step change" que usa antes aplica sólo a concept segmentation.
5. **El benchmark es propio.** SA-Co lo construyó Meta, con un data engine que usa SAM 3 en el bucle, y sobre él SAM 3 duplica a los competidores. No es descalificante —el dataset se liberó— pero es autoevaluación y conviene decirlo.
6. **Gemini 2.5 Pro obtiene 13,0 de cgF1**, un número llamativamente bajo para un modelo fundacional puntero. El post no explica cómo se lo evaluó ni si la comparación es justa para un modelo que no fue diseñado para emitir máscaras. Sí lo reporta como el mejor o empatado en CountBench (92,4) y como componente del mejor resultado en ReasonSeg (74,0 junto a SAM 3), lo que sugiere que el 13,0 mide más un desajuste de formato de salida que una falta de capacidad.
7. **Contradicción aparente entre las dos mitades del post, resuelta cronológicamente.** La sección de limitaciones de SAM 3 dice: "the cost of SAM 3 inference **scales linearly with the number of objects** being tracked. Each object is processed separately... **without inter-object communication**. Incorporating shared object-level contextual information could aid in improving efficiency". Cuatro meses después, la actualización de SAM 3.1 anuncia exactamente eso — multiplexing y global reasoning. **No es una contradicción: es la hoja de ruta cumpliéndose dentro del mismo documento**, y como tal es una narrativa muy usable en clase.
8. **Limitaciones declaradas de SAM 3, relevantes para un público biomédico.** El post admite que SAM 3 **falla en conceptos de grano fino fuera de dominio en modo zero-shot**, y da como ejemplo explícito **"platelet"** (plaqueta), "especially in niche visual domains involving **medical or scientific imagery**". Es la advertencia más pertinente de todo el corpus para la Clase 9: el modelo fundacional de segmentación no funciona de entrada en imágenes médicas. La mitigación que ofrece Meta es fine-tuning con pocos datos anotados, cuyo código liberan. Si el deck presenta SAM como solución lista para biomedicina, esta cita lo matiza.
9. **Segunda limitación:** SAM 3 **no soporta frases largas y complejas** ("the second to last book from the right on the top shelf"); sólo prompts cortos de vocabulario abierto ("a hardcover book"). El rodeo es acoplarlo a un MLLM (SAM 3 Agent).
10. **Extracción:** `page.md` se usó como entrada de texto sin caer a `original.html` — trae los ~35.000 caracteres del cuerpo con títulos. Dos cosas del original no sobrevivieron limpias: (a) los **videos** están perdidos — el post referencia al menos uno ("The prompt 'hands' is used in this video showing SAM 3 Aria Gen 2 output.") cuyo archivo no se capturó; (b) algunos encabezados quedaron mal nivelados (párrafos de la sección de limitaciones convertidos en `##`) y el pie de página aparece triplicado. Ninguna de las dos cosas afecta al contenido de fondo.

## Images / diagrams

Esta es la única captura del conjunto con **figuras reales**: cuatro PNG de contenido y seis SVG de cromo. Todas las imágenes están en la carpeta compañera.

### Figuras de contenido

- `sam31-meta-2026.web/images/658783005_976222541732621_4396625680307590489_n.png` (1920×1080, PNG con alfa)
  - **Depiction:** diagrama comparativo sobre fondo negro, partido por una línea vertical. **Izquierda, rotulado "SAM 3.1 — Single computation for all objects":** un flujo vertical descendente. Arriba, tres miniaturas del mismo frame de video en el instante **T−1**, cada una con un animal distinto resaltado (un cerdito en rosa, un perro en azul, otro animal en verde agua) agrupadas en un recuadro. Bajan a una caja **"Mux"**, que produce **un único frame** con los tres animales enmascarados a la vez en sus tres colores. Ese frame entra a la caja **"SAM 3.1"**, sale otro frame único con las tres máscaras, pasa por una caja **"Demux"** y se abre de nuevo en tres miniaturas separadas en el instante **T**. **Derecha, rotulado "SAM 3 — Separate computations for each object":** tres columnas independientes y paralelas; cada una toma su miniatura de T−1, la pasa por su propia caja **"SAM 3"** y produce su miniatura de T. Tres cajas SAM 3, tres pasadas.
  - **Why it matters:** es la figura que explica el multiplexing de un vistazo, y es la mejor imagen del corpus para la idea de "un solo forward pass para N objetos" frente a "N pasadas". Traduce el número abstracto (16→32 fps) a una diferencia estructural visible: tres cajas contra una. Directamente reutilizable en la slide de SAM 3.1.
  - **Transcribed text:** "T−1" · "Mux" · "SAM 3.1" · "Demux" · "T" (columna izquierda) · "SAM 3.1 / Single computation for all objects" · "SAM 3 / Separate computations for each object" · "T−1" · "SAM 3" ×3 · "T" (columna derecha).

- `sam31-meta-2026.web/images/581932231_2350994468688058_5091902097566884080_n.png` (2252×844, PNG con alfa)
  - **Depiction:** diagrama de flujo del **data engine de SAM 3**, sobre fondo blanco, en dos filas. Fila superior, de izquierda a derecha: un panel gris agrupa dos entradas, **"Media Pool"** (ícono de reproductor) y **"Ontology"** (ícono de grafo de nodos); de ahí una flecha va a la caja celeste **"Mine data"**, luego a **"Propose NPs"**, luego a **"Propose mask"** —que lleva embebida una etiqueta blanca **"SAM 3"**— y finalmente a una foto de una flor con dos máscaras superpuestas (una amarilla, una celeste), rotulada abajo **"Flower"** y a la derecha **"Candidates"**. Una flecha baja hacia la fila inferior, al panel **"AI verifiers" (celeste) / "Human verifiers" (rosa)**. De ahí salen dos caminos: **"Pass"**, una flecha larga que retorna hacia la izquierda por el borde inferior; y **"Fail"**, que va a una foto rotulada **"Incomplete masks" / "Flower"** con la máscara amarilla sobrante, y de ahí a la caja rosa **"Correct"**, que produce la foto final rotulada **"Final annotations" / "Flower"** con sólo las máscaras correctas en celeste. Una flecha punteada sube desde los verificadores hasta la caja "Propose mask", cerrando el bucle de reentrenamiento. Abajo a la izquierda, una **leyenda**: cuadrado celeste = "AI model", cuadrado rosa = "Human", flecha llena = "Label", flecha punteada = "Train".
  - **Why it matters:** es la única representación visual del *data engine* en todo el corpus, y resuelve el concepto que los abstracts de SAM 1 y SAM 2 nombran sin explicar. El código de color (celeste = IA, rosa = humano) muestra de un golpe dónde queda el humano en el bucle: sólo en verificación y corrección. La flecha punteada "Train" cierra el círculo que hace que el modelo mejore los datos que lo entrenan. Excelente para la slide del data engine.
  - **Transcribed text:** "SAM 3 data engine" (título) · "Media Pool" · "Ontology" · "Mine data" · "Propose NPs" · "Propose mask" · "SAM 3" · "Flower" · "Candidates" · "AI verifiers" · "Human verifiers" · "Pass" · "Fail" · "Incomplete masks" · "Flower" · "Correct" · "Final annotations" · "Flower" · leyenda: "AI model" · "Human" · "Label" · "Train".

- `sam31-meta-2026.web/images/581946541_823890960270664_7677762648668518257_n.png` (1920×981, PNG con alfa)
  - **Depiction:** panel de **seis gráficos de barras horizontales** sobre fondo negro, en dos columnas y tres filas, separados por finas líneas divisorias. Cada panel tiene un título con la tarea, el dataset y la métrica entre paréntesis; las barras de las líneas base están en blanco y gris, y la barra de SAM 3 siempre en **azul**, con el valor numérico al final de cada barra.
  - **Why it matters:** **es la figura más valiosa del corpus para el hueco de métricas del deck.** Nombra cinco métricas distintas de evaluación —cgF1, pHOTA, J&F, mIoU, gIoU— cada una atada a una tarea y un dataset concretos, y las cuantifica. Además incluye una línea base **"Human"** en los dos primeros paneles, lo que permite mostrar en clase la brecha real que sigue existiendo (53,9 vs 72,8). Y sirve como caso de lectura crítica: la misma figura sostiene el titular "duplicamos a los sistemas existentes" y la observación "seguimos 19 puntos por debajo del humano".
  - **Transcribed text (completa, panel por panel):**
    - Panel 1 — "Concept Segmentation (Text → Masks) in Images on SA-Co Gold (cgF1 metric)": Human 72.8 · OWLv2 24.6 · Gemini 2.5 Pro 13.0 · **SAM 3 53.9**.
    - Panel 2 — "Concept Segmentation (Text → Masklets) in Video on SA-Co SA-V (pHOTA metric)": Human 70.5 · GLEE 11.8 · LLMDet + SAM3 Tracker 30.1 · **SAM 3 58.0**.
    - Panel 3 — "Visual Segmentation (Mask → Masklet) in video on SA-V test (J&F metric)": SAM2Long 81.2 · SeC 81.7 · SAM 2.1 L 78.4 · **SAM 3 84.4**.
    - Panel 4 — "Visual Segmentation (Point → Mask) in images on SA-37 (MIoU at 3 clicks)": SAM 1 H 77.0 · SAM 2.1 L 80.3 · **SAM 3 81.3**.
    - Panel 5 — "Counting in images on CountBench (Accuracy)": Qwen-VL-72B 86.7 · Molmo-72B 92.4 · Gemini 2.5 Pro 92.4 · **SAM 3 93.8**.
    - Panel 6 — "Reasoning Segmentation (Long text → Mask) in images on ReasonSeg Test (gIoU)": RSVP (GPT-4o) 55.4 · X-SAM (Phi-3-3.8b) 57.8 · LISA-13B (LLaVA1.5) 61.3 · **SAM 3 + GEMINI 2.5 PRO 74.0**.

- `sam31-meta-2026.web/images/581933839_2354830958311462_3570444330690080691_n.png` (1920×1271, PNG con alfa)
  - **Depiction:** fotografía apaisada de un caballo negro de tiro caminando de perfil hacia la izquierda sobre un campo de pasto verde, con árboles desenfocados al fondo. **El único elemento segmentado es el cabestro (la cabezada de cuero) que rodea el hocico y la cabeza del animal, resaltado con una máscara magenta/rosa translúcida** que sigue con precisión las correas y las hebillas. Sobre el tercio inferior de la imagen, un globo de texto semitransparente con un ícono de lupa con destello a la izquierda contiene la consulta.
  - **Why it matters:** ilustra **SAM 3 Agent** y la *reasoning segmentation*: el prompt no nombra el objeto ("cabestro"), lo describe por su función, y el sistema tiene que razonar para llegar a la máscara correcta. Es el salto conceptual que separa "segmentar lo que nombro" de "segmentar lo que describo", y muestra visualmente por qué SAM 3 solo no alcanza y necesita un MLLM encima. La máscara además está sobre una pieza fina y de topología complicada (correas delgadas, huecos), lo que exhibe la calidad de segmentación mejor que un objeto compacto.
  - **Transcribed text:** "Horses can be trained to follow commands and be controlled while being ridden. What object in the picture is used for controlling and guiding a horse?"

### Cromo del sitio

Seis SVG sin valor didáctico, copiados a la carpeta compañera por completitud.

- `sam31-meta-2026.web/images/meta-logo-primary_standardsize.svg` — **Depiction:** logotipo institucional de Meta (el símbolo de lazo/infinito seguido de la palabra "Meta"), en la barra de navegación superior. Generado con Adobe Illustrator, viewBox 496×100. **Why it matters:** nada; identifica al emisor del post. **Transcribed text:** "Meta" (atributo `alt`: "Meta").
- `sam31-meta-2026.web/images/335682312_964107378293184_3093631164486164913_n.svg` — **Depiction:** ícono social circular de 30×30 px del pie de página; en el marcado acompaña el enlace a `facebook.com/aiatmeta`. **Why it matters:** nada. **Transcribed text:** ninguno (sin `alt`).
- `sam31-meta-2026.web/images/336009607_1870102080040414_6753977241281150924_n.svg` — **Depiction:** ícono social circular de 30×30 px del pie de página; acompaña el enlace a `twitter.com/aiatmeta`. **Why it matters:** nada. **Transcribed text:** ninguno (sin `alt`).
- `sam31-meta-2026.web/images/336289415_1541032296405649_2165099305308791297_n.svg` — **Depiction:** ícono social circular de 30×30 px del pie de página; acompaña el enlace a `linkedin.com/showcase/aiatmeta`. **Why it matters:** nada. **Transcribed text:** ninguno (sin `alt`).
- `sam31-meta-2026.web/images/335648731_142576991793348_7786819189843639239_n.svg` — **Depiction:** ícono social circular de 30×30 px del pie de página; acompaña el enlace a `youtube.com/@aiatmeta`. **Why it matters:** nada. **Transcribed text:** ninguno (sin `alt`).
- `sam31-meta-2026.web/images/87524316_2677189655726266_6338721200264445952_n.svg` — **Depiction:** no es un ícono sino un **separador vertical**: un trazo fino de 10×74 px que dibuja una línea divisoria entre columnas del pie de página. **Why it matters:** nada; es decoración de maquetación. **Transcribed text:** ninguno.

## Raw / preserved excerpts

**Actualización SAM 3.1 — texto completo, verbatim (inglés):**

> ***Update March 27, 2026:***
>
> We've seen incredible adoption of SAM 3 over the last few months, and during that time, we've been working behind the scenes on updates to improve video processing efficiency. Today, we're pleased to introduce SAM 3.1.
>
> As a drop-in replacement for SAM 3, our updated model delivers a significant boost in video processing efficiency by introducing object multiplexing, which allows the model to track up to 16 objects in a single forward pass. This innovation doubles the processing speed for videos with a medium number of objects, increasing throughput from 16 to 32 frames per second on a single H100 GPU. As a result, SAM 3.1 enables real-time object tracking in complex videos while reducing overall GPU resource requirements, making high-performance applications feasible on smaller, more accessible hardware.
>
> This improvement comes from a shift in how the model handles multiple objects. Previously, each object required its own dedicated pass, but with multiplexing, SAM 3.1 processes all tracked objects together, eliminating redundant computation and memory bottlenecks. This global reasoning approach streamlines performance and enhances accuracy in crowded scenes.

**Planteo del problema y definición de vocabulario abierto, verbatim:**

> Linking language to specific visual elements in images or videos is a major challenge in computer vision. Traditional models often focus on object segmentation with a fixed set of text labels, restricting their ability to address the full spectrum of user requests, which frequently involve segmenting concepts not present in predefined lists. This means that existing models can segment frequent concepts like "person," but struggle with more nuanced concepts like "the striped red umbrella".
>
> SAM 3 overcomes these limitations by introducing the promptable concept segmentation capability: finding and segmenting all instances of a concept defined by a text or exemplar prompt. SAM 3 accepts text prompts — open-vocabulary short noun phrases — and image exemplar prompts, eliminating the constraints of fixed label sets.

**Data engine, verbatim:**

> We address this challenge by creating a scalable data engine that leverages SAM 3, human annotators, and AI models in the loop, which allows dramatic speed-ups in annotation — approximately 5x faster than humans on negative prompts (concepts not present in the image/video) and 36% faster for positive prompts even in challenging fine-grained domains. This hybrid human and AI system enabled us to create a large and diverse training set with over 4 million unique concepts.
>
> A pipeline of AI models, including SAM 3 and systems such as a Llama-based captioner, automatically mine images and videos, generate captions, parse the captions into text labels, and create initial segmentation masks, which are shown as "candidates" in the above figure.
>
> Human and AI annotators then verify and correct these proposals, yielding a feedback loop that rapidly scales dataset coverage while continuously improving data quality. AI annotators are based on Llama 3.2v models that were specifically trained to match or surpass human accuracy on annotation tasks, such as verifying if a mask is high quality, or if all instances of a concept are exhaustively masked in an image.
>
> By delegating some human annotation tasks to AI annotators, we more than double the throughput compared to a human-only annotation pipeline. AI annotators also automatically filter out easy examples, focusing valuable human annotation effort on the most challenging cases where the current version of SAM 3 fails. We also leverage a concept ontology — a dictionary of concepts and their relationships based on Wikipedia — to map text labels into a shared concept space and increase the coverage of less frequent concepts in the data.

**Arquitectura, verbatim:**

> The SAM 3 model architecture also builds on many previous AI advancements from Meta. The text and image encoders in SAM 3 are from the Meta Perception Encoder, an open source model we shared in April that enables the building of more advanced computer vision systems that can assist people in everyday tasks, such as image recognition and object detection. Using the Meta Perception Encoder enabled us to achieve a significant leap in performance compared to previous encoder choices. The detector component is based on the DETR model, which was the first to use transformers for object detection. The memory bank and memory encoder used in SAM 2 is the basis for the Tracker component. We also used several open source components, including datasets, benchmarks, and model improvements, to advance our work.

**Resultados, verbatim:**

> We achieve a step change in concept segmentation performance in images (measured on SA-Co Gold subset) and videos (on SA-Co Video), with SAM 3 doubling cgF1 scores (a measure of how well the model can recognize and localize concepts) relative to existing models. SAM 3 consistently outperforms both foundational models like Gemini 2.5 Pro and strong specialist baselines such as GLEE, OWLv2, and LLMDet. In studies, users prefer SAM 3 outputs over the strongest baseline, OWLv2, approximately three to one. We also achieve state-of-the-art results on the SAM 2 visual segmentation tasks (mask-to-masklet, point-to-mask), matching or exceeding the state-of-the-art performance of previous models like SAM 2. Furthermore, we see notable gains on challenging benchmarks like zero-shot LVIS (not shown) and object counting (shown on CountBench).
>
> This excellent performance comes with fast inference — SAM 3 runs in 30 milliseconds for a single image with more than 100 detected objects on an H200 GPU. In video, the inference latency scales with the number of objects, sustaining near real-time performance for approximately five concurrent objects.
>
> We also show that a multimodal large language model (MLLM) that uses SAM 3 as a tool, called SAM 3 Agent, can segment more complex text queries such as, "What object in the picture is used for controlling and guiding a horse?" The MLLM proposes noun phrase queries to prompt SAM 3 and analyzes the returned masks, iterating until the masks are satisfactory. Without training on any referring expression segmentation or reasoning segmentation data, SAM 3 Agent surpasses prior work on challenging free-text segmentation benchmarks that require reasoning, such as ReasonSeg (shown above) and OmniLabel.

**Limitaciones — la sección más relevante para un público biomédico, verbatim:**

> SAM 3 struggles to generalize to fine-grained out-of-domain concepts in a zero-shot manner, such as identifying specific terms that require domain knowledge like "platelet," especially in niche visual domains involving medical or scientific imagery. We experimented with strategies to extend the capability of SAM 3 and found that the model quickly adapts to new concepts and visual domains when fine-tuned on small quantities of annotated data. As part of our code release, we're sharing fine-tuning approaches that the community can leverage to adapt SAM 3 for their use cases. We're also partnering with Roboflow to enable people to annotate data, fine-tune, and deploy SAM 3 for their particular needs.
>
> Additionally, while SAM 3 performs well with short open-vocabulary prompts, such as "a hardcover book," the model doesn't support longer, complex phrases like, "the second to last book from the right on the top shelf." However, when paired with multimodal large language models, the model can be trained to support longer, more complex descriptions including cases that require reasoning.
>
> When applied to video, SAM 3 tracks every object with a SAM 2-style masklet, which means the cost of SAM 3 inference scales linearly with the number of objects being tracked. Each object is processed separately, utilizing only shared per-frame embeddings, without inter-object communication. Incorporating shared object-level contextual information could aid in improving efficiency and model performance in complex scenes with many visually similar objects.

**Takeaways del lanzamiento de SAM 3, verbatim:**

> - We're announcing Meta Segment Anything Model 3 (SAM 3), a unified model for detection, segmentation, and tracking of objects in images and video using text, exemplar, and visual prompts.
> - As part of this release, we're sharing SAM 3 model checkpoints, evaluation datasets, and fine-tuning code.
> - We're also introducing Segment Anything Playground, a new platform that makes it easy for anyone to understand the capabilities of SAM and experiment with cutting-edge AI models for creative media modification.
> - In Edits, Instagram's video creation app, SAM 3 will soon enable new effects that creators can apply to specific people or objects in their videos. New creation experiences enabled by SAM 3 will also be coming to Vibes on the Meta AI app and meta.ai on the web.
> - Separately, we're sharing SAM 3D, a suite of open source models, code, and data for 3D objects and human reconstruction from a single image, setting a new standard for grounded 3D reconstruction in physical world scenarios.
> - SAM 3 and SAM 3D are powering Facebook Marketplace's new View in Room feature, helping people visualize the style and fit of home decor items, like a lamp or a table, in their spaces before purchasing.
> - Together with our partners at Conservation X Labs and Osa Conservation, we're also launching a first-of-its-kind, publicly available video dataset for wildlife monitoring using SAM 3.

**Aplicaciones científicas, verbatim:**

> SAM 3 is already being applied for use cases in scientific fields. For example, Meta collaborated with Conservation X Labs and Osa Conservation to combine on-the-ground wildlife monitoring with SAM 3 to build an open dataset of research-ready, raw video footage. The publicly available SA-FARI dataset includes over 10,000 camera trap videos of more than 100 species, annotated with bounding boxes and segmentation masks for every animal in each frame. FathomNet is a unique research collaboration led by MBARI that is working to advance AI tools for ocean exploration. Segmentation masks and a new instance segmentation benchmark tailored for underwater imagery are now available to the marine research community via the FathomNet Database. SA-FARI and FathomNet can be used by the broader AI community to develop innovative new ways to discover, monitor, and conserve wildlife on land and in the ocean.

**Prompts y modalidades, verbatim:**

> SAM 3 supports a variety of prompt modalities, including both concept prompts such as simple noun phrases and image exemplars, as well as visual prompts, such as masks, boxes, and points, which were introduced in SAM 1 and SAM 2. This increases the flexibility and usability of segmentation, particularly for concepts that are rare or hard to describe with text alone.
>
> SAM 3 excels at segmenting objects described by short noun phrases, reflecting common user intent in interactive and natural settings. Our model can also be used as a perception tool for multimodal large language models to segment objects described by more complex prompts, such as: "people sitting down, but not holding a gift box in their hands."
>
> Overall, SAM 3 delivers a 2x gain over existing systems in both image and video on our promptable concept segmentation benchmark, SA-Co, and improves upon previous SAM capabilities in interactive visual segmentation tasks.

**Enlaces de descarga listados en el post:**

> SAM 3.1 Model Checkpoint — https://huggingface.co/facebook/sam3.1
> SAM 3 Codebase — https://github.com/facebookresearch/sam3
> SAM 3 Research Paper — https://arxiv.org/abs/2511.16719
> Explore the Playground — https://www.aidemos.meta.com/segment-anything
> SA-Co Dataset — https://github.com/facebookresearch/sam3/blob/main/README.md#sa-co-dataset
> SA-FARI Dataset — https://www.conservationxlabs.com/sa-fari
