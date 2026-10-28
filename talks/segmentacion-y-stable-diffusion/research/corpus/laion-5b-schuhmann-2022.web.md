---
source_file: laion-5b-schuhmann-2022
source_type: web-capture
ingested_at: 2026-08-14
---

# LAION-5B: An open large-scale dataset for training next generation image-text models (arXiv:2210.08402) — página de abstract

## Provenance
- Original location: `research/web/laion-5b-schuhmann-2022/`
- Format: web-capture (arXiv `abs` page; `page.md` + `original.html` + `assets/`)
- URL: https://arxiv.org/abs/2210.08402
- Author / source (if known): Christoph Schuhmann et al. (LAION, colaboración abierta) — 16 autores
- Date of original (if known): 16 oct 2022 (v1, única versión). NeurIPS 2022, track de Datasets and Benchmarks.
- Fetched at: 2026-08-14T17:03:10Z (HTTP 200, 45.225 bytes)
- Rol en la Clase 9: los datos sobre los que se entrenó Stable Diffusion. Es la fuente que explica de dónde salieron las imágenes.

## Key claims

- **Autores:** Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, Patrick Schramowski, Srivatsa Kundurthy, Katherine Crowson, Ludwig Schmidt, Robert Kaczmarczyk, Jenia Jitsev. **Año:** 2022. **Venue:** **NeurIPS 2022**, 36ª conferencia, track de **Datasets and Benchmarks**. **arXiv ID:** arXiv:2210.08402 [cs.CV, cs.AI, cs.LG]. **DOI:** 10.48550/arXiv.2210.08402.
- Arquitecturas como **CLIP y DALL-E probaron la utilidad de entrenar con grandes volúmenes de datos imagen-texto ruidosos**, sin depender de las etiquetas precisas y caras de la supervisión unimodal estándar.
- Esos modelos mostraron generación guiada por texto, transferencia a tareas posteriores, y **clasificación zero-shot con robustez notable fuera de distribución**.
- **El problema:** estudiar el entrenamiento y las capacidades de estos modelos requiere datasets de **miles de millones** de pares imagen-texto, y **hasta ese momento ninguno de ese tamaño estaba disponible abiertamente** para la comunidad.
- **LAION-5B:** un dataset de **5.850 millones de pares imagen-texto filtrados con CLIP**, de los cuales **2.320 millones son de idioma inglés**.
- Demuestran **replicación y fine-tuning exitosos** de modelos fundacionales —**CLIP, GLIDE y Stable Diffusion**— usando el dataset.
- Aportan además: **índices de vecinos más cercanos**, una **interfaz web mejorada** para explorar el dataset y generar subconjuntos, y **puntajes de detección de marca de agua, contenido NSFW y contenido tóxico**.

## Definitions and terminology

- **Filtrado con CLIP (*CLIP-filtered*).** El criterio de construcción del dataset: se conservan los pares imagen-texto cuya similitud según CLIP supera un umbral. Es una idea con un giro notable —se usa un modelo entrenado con datos web para filtrar los datos web con los que se entrenará el próximo modelo— que el abstract enuncia sin comentar. El **umbral concreto no aparece** en la página capturada.
- **Datos ruidosos vs. etiquetas precisas.** El contraste que estructura el argumento: "large amounts of noisy image-text data, without relying on expensive accurate labels used in standard vision unimodal supervised learning". Es la justificación económica de todo el paradigma imagen-texto, y sirve para explicarle a un público biomédico —acostumbrado a la anotación experta— por qué estos modelos se entrenan de otra manera.
- **Robustez fuera de distribución (*out-of-distribution robustness*).** Propiedad que el abstract atribuye a los modelos entrenados así.
- **Índices de vecinos más cercanos.** Estructuras que permiten buscar dentro del dataset por similitud de embedding.
- **Puntajes de detección (watermark, NSFW, tóxico).** Metadatos por muestra, no filtros aplicados: el dataset **los provee**, no los remueve. Distinción importante.
- **Democratizar la investigación.** El encuadre explícito del paper: "To address this problem and democratize research on large-scale multi-modal models".

## Evidence and examples

- **5.850 millones (5,85 B) de pares imagen-texto** filtrados con CLIP — el total.
- **2.320 millones (2,32 B) en inglés** — el subconjunto en idioma inglés.
- Modelos replicados o ajustados con el dataset: **CLIP, GLIDE, Stable Diffusion**.
- Recursos liberados: índices de vecinos más cercanos, interfaz web de exploración y generación de subconjuntos, puntajes de watermark/NSFW/toxicidad.
- Página de anuncio: `https://laion.ai/laion-5b-a-new-era-of-open-large-scale-multi-modal-datasets/`. OpenReview: `https://openreview.net/forum?id=M3Y74vmsMcY`.

### Verificación de cifras del deck

El deck no cita cifras de LAION entre las que este encargo pide verificar. Dos números quedan disponibles y verificados por si la clase los necesita: **5,85 B** de pares totales y **2,32 B** en inglés. Advertencia de precisión: si el deck dice "Stable Diffusion se entrenó con 5.000 millones de imágenes", el número es incorrecto — Stable Diffusion se entrenó sobre **subconjuntos filtrados** de LAION (del orden de cientos de millones a ~2 B según la etapa), no sobre los 5,85 B completos. El abstract dice que Stable Diffusion se replicó "usando el dataset", sin especificar qué subconjunto.

## Inconsistencies / open questions

1. **La página capturada trae solo el abstract.** Lo que la clase necesitaría y no está:
   - El **umbral de similitud CLIP** usado para filtrar y la descripción del pipeline de recolección (Common Crawl, extracción de `alt` text, deduplicación).
   - La **distribución por idiomas** más allá del corte inglés / no inglés.
   - La **sección de consideraciones éticas y limitaciones**, que en este paper es sustancial y es precisamente lo que un público biomédico —sensible a procedencia de datos y consentimiento— querría oír.
   - Las **estadísticas de contenido problemático** que los puntajes de NSFW/toxicidad revelan.
   - La composición exacta de los subconjuntos con los que se entrenó Stable Diffusion.
   Todo eso está en el PDF (`https://arxiv.org/pdf/2210.08402`), no capturado.
2. **El dataset es de enlaces, no de imágenes.** LAION-5B distribuye **URLs y metadatos**, no los archivos de imagen. Esto tiene dos consecuencias que el abstract no menciona y que importan: el dataset se degrada con el tiempo a medida que los enlaces mueren, y la responsabilidad legal sobre el contenido queda en una zona gris. Es una limitación estructural invisible en la captura.
3. **Los puntajes de NSFW y toxicidad se proveen, no se aplican.** El abstract dice "we provide ... detection scores for watermark, NSFW, and toxic content detection". Es un dataset que **etiqueta** contenido problemático y deja el filtrado a quien lo use. Presentarlo como "un dataset limpio" sería incorrecto.
4. **Contexto que la clase debería conocer aunque no esté en la fuente:** en diciembre de 2023 una auditoría del Stanford Internet Observatory encontró material de abuso sexual infantil en LAION-5B, y LAION retiró temporalmente el dataset para depurarlo, republicándolo luego como Re-LAION-5B. Nada de esto está en la página capturada (es de 2022) y **no hay fuente en el corpus que lo respalde**, pero es información relevante si la clase presenta a LAION como el ejemplo virtuoso de datos abiertos. Marcar como pendiente de fuente si se decide mencionarlo.
5. **Tensión no resuelta en la propia lógica del dataset:** se usa CLIP —entrenado sobre 400 M de pares web no auditados y no liberados (ver `clip-radford-2021.web.md`)— para filtrar el dataset abierto que reemplazaría a esos datos cerrados. Los sesgos de CLIP se propagan por construcción a LAION. El abstract no lo comenta.
6. **Licencia:** la página incluye el distintivo **CC BY 4.0** (a diferencia de las otras doce capturas de arXiv, que llevan la licencia no exclusiva de distribución de arXiv). Detalle menor pero real de esta fuente.

## Images / diagrams

La captura de una página `abs` de arXiv **no incluye ninguna figura del paper**. Los cuatro archivos guardados son cromo del sitio, copiados a la carpeta compañera por completitud.

  - **Depiction:** logotipo institucional de arXiv en la barra superior del sitio (vectorial, tema claro).
  - **Why it matters:** nada. Cromo de navegación.
  - **Transcribed text:** "arXiv" (atributo `alt`: "archive").
  - **Depiction:** distintivo de licencia Creative Commons de 80×15 px, fondo negro con el logo circular "CC" en blanco seguido de las letras "BY".
  - **Why it matters:** marginal, pero es el **único archivo con contenido informativo entre todo el cromo de las trece capturas de arXiv**: indica que este preprint está bajo **CC BY 4.0**, licencia más permisiva que la licencia no exclusiva de arXiv que llevan las otras doce. Si el deck reprodujera material del paper, esta es la única de las trece fuentes académicas cuya licencia lo permite explícitamente.
  - **Transcribed text:** "CC BY".
  - **Depiction:** ícono de 16×16 px de BibSonomy — grafo de nodos gris con el nodo central en magenta.
  - **Why it matters:** nada. Botón de marcador.
  - **Transcribed text:** ninguno (atributo `alt`: "BibSonomy").
  - **Depiction:** ícono de 18×18 px de Reddit — mascota "Snoo" en gris con ojos rojos.
  - **Why it matters:** nada. Botón de compartir.
  - **Transcribed text:** ninguno (atributo `alt`: "Reddit").

## Raw / preserved excerpts

**Abstract completo, verbatim (inglés):**

> Groundbreaking language-vision architectures like CLIP and DALL-E proved the utility of training on large amounts of noisy image-text data, without relying on expensive accurate labels used in standard vision unimodal supervised learning. The resulting models showed capabilities of strong text-guided image generation and transfer to downstream tasks, while performing remarkably at zero-shot classification with noteworthy out-of-distribution robustness. Since then, large-scale language-vision models like ALIGN, BASIC, GLIDE, Flamingo and Imagen made further improvements. Studying the training and capabilities of such models requires datasets containing billions of image-text pairs. Until now, no datasets of this size have been made openly available for the broader research community. To address this problem and democratize research on large-scale multi-modal models, we present LAION-5B - a dataset consisting of 5.85 billion CLIP-filtered image-text pairs, of which 2.32B contain English language. We show successful replication and fine-tuning of foundational models like CLIP, GLIDE and Stable Diffusion using the dataset, and discuss further experiments enabled with an openly available dataset of this scale. Additionally we provide several nearest neighbor indices, an improved web-interface for dataset exploration and subset generation, and detection scores for watermark, NSFW, and toxic content detection. Announcement page https://laion.ai/laion-5b-a-new-era-of-open-large-scale-multi-modal-datasets/

**Metadatos de la página, verbatim:**

> Computer Science > Computer Vision and Pattern Recognition
> arXiv:2210.08402 (cs)
> [Submitted on 16 Oct 2022]
> Title: LAION-5B: An open large-scale dataset for training next generation image-text models
> Authors: Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, Patrick Schramowski, Srivatsa Kundurthy, Katherine Crowson, Ludwig Schmidt, Robert Kaczmarczyk, Jenia Jitsev
> Comments: 36th Conference on Neural Information Processing Systems (NeurIPS 2022), Track on Datasets and Benchmarks. OpenReview: https://openreview.net/forum?id=M3Y74vmsMcY
> Subjects: Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
> Cite as: arXiv:2210.08402 [cs.CV]
> https://doi.org/10.48550/arXiv.2210.08402
> Licencia: CC BY 4.0
