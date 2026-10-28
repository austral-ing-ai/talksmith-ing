---
source_file: clip-radford-2021
source_type: web-capture
ingested_at: 2026-08-14
---

# Learning Transferable Visual Models From Natural Language Supervision — CLIP (arXiv:2103.00020) — página de abstract

## Provenance
- Original location: `research/web/clip-radford-2021/`
- Format: web-capture (arXiv `abs` page; `page.md` + `original.html` + `assets/`)
- URL: https://arxiv.org/abs/2103.00020
- Author / source (if known): Alec Radford, Jong Wook Kim et al. (OpenAI) — 12 autores
- Date of original (if known): 26 feb 2021 (v1, única versión)
- Fetched at: 2026-08-14T17:03:10Z (HTTP 200, 44.839 bytes)
- Rol en la Clase 9: el modelo que conecta texto e imagen — es el text encoder de Stable Diffusion y el origen de la afirmación de la **slide 42**, que tiene un error de atribución de parámetros.

## Key claims

- **Autores:** Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever. **Año:** 2021. **Venue:** preprint arXiv — la página **no declara venue** (el paper se presentó en ICML 2021, dato que no está en la captura). **arXiv ID:** arXiv:2103.00020 [cs.CV, cs.LG]. **DOI:** 10.48550/arXiv.2103.00020.
- **El problema:** los sistemas de visión de estado del arte se entrenan para predecir **un conjunto fijo y predeterminado de categorías**. Esa supervisión restringida limita su generalidad: para cualquier concepto visual nuevo hace falta más datos etiquetados.
- **La alternativa:** aprender directamente del **texto crudo sobre las imágenes**, que es una fuente de supervisión mucho más amplia.
- **La tarea de preentrenamiento:** predecir **qué caption va con qué imagen**. Simple, eficiente y escalable, sobre un dataset de **400 millones de pares (imagen, texto)** recolectados de internet.
- Después del preentrenamiento, **el lenguaje natural se usa para referirse a conceptos visuales aprendidos (o describir nuevos)**, habilitando **transferencia zero-shot** a tareas posteriores.
- Evaluado en **más de 30 datasets** de visión: OCR, reconocimiento de acciones en video, geolocalización, clasificación de grano fino.
- **Resultado emblemático:** iguala la exactitud del **ResNet-50 original en ImageNet en modo zero-shot**, sin usar ninguno de sus **1,28 millones de ejemplos de entrenamiento**.
- Liberan código y pesos preentrenados.

## Definitions and terminology

- **Preentrenamiento contrastivo.** "The simple pre-training task of predicting which caption goes with which image." Es exactamente la definición operativa del aprendizaje contrastivo de CLIP: dado un lote de imágenes y un lote de captions, aprender a aparear correctamente. **El abstract nunca usa la palabra "contrastive"** ni describe la matriz de similitudes N×N, ni la pérdida InfoNCE, ni la temperatura aprendida. La idea está; el vocabulario técnico no.
- **Espacio compartido imagen-texto.** **Ausente del abstract.** El concepto que la clase necesita —dos encoders que proyectan a un mismo espacio vectorial donde la similitud coseno mide correspondencia semántica— **no se enuncia en la página capturada**. Lo que sí está es su consecuencia observable: "natural language is used to reference learned visual concepts", que sólo tiene sentido si existe tal espacio compartido. La clase enseña el mecanismo; la fuente sólo respalda el efecto.
- **Transferencia zero-shot.** Aplicar el modelo a una tarea nueva sin ningún ejemplo de entrenamiento de esa tarea, escribiendo las clases como texto. Bien respaldado por el abstract.
- **Text encoder / image encoder (dos torres).** **Ausentes del abstract.** No se describe la arquitectura de dos torres, ni cuáles son (ResNet o ViT del lado visual, Transformer del lado texto), ni sus tamaños.
- **77 tokens / 77×768.** **Ausentes del abstract.** Ver la verificación de cifras.
- **ViT-L/14.** **Ausente del abstract.** La nomenclatura de variantes no aparece; tampoco está definida en la captura de ViT (ver `vit-dosovitskiy-2020.web.md`).

## Evidence and examples

- **400 millones de pares (imagen, texto)** recolectados de internet — el dato de escala del paper.
- **Más de 30 datasets** de visión evaluados.
- Tareas nombradas: **OCR, reconocimiento de acciones en video, geolocalización, clasificación de grano fino**.
- **Iguala al ResNet-50 original en ImageNet zero-shot**, sin usar los **1,28 M** de ejemplos de entrenamiento de ImageNet. Es el número más citable del abstract.
- Código y pesos: `https://github.com/OpenAI/CLIP`.

### Verificación de cifras del deck

- **"400 M de pares imagen-texto" — CIERRA exactamente.** El abstract dice "a dataset of 400 million (image, text) pairs collected from the internet". Sin matices.

- **Slide 42 — "CLIP ViT-L/14 de OpenAI (123M parámetros)": IMPRECISO. El número corresponde sólo al text encoder.**
  Desglose correcto de `CLIP ViT-L/14`:
  | Componente | Parámetros |
  |---|---|
  | Text encoder (Transformer, 12 capas, ancho 768) | **≈ 123,7 M** |
  | Image encoder / torre visual (ViT-L/14, 24 capas, ancho 1024) | **≈ 303,2 M** |
  | **Modelo completo** | **≈ 428 M** (427,6 M) |
  Los **123 M de la slide son el text encoder**, no el modelo. El modelo completo pesa **~428 M**, es decir **3,5 veces más**.
  **Por qué la confusión es comprensible —y por qué igual conviene corregirla.** En Stable Diffusion **sólo se usa el text encoder de CLIP**: la torre visual se descarta, porque lo que hace falta es convertir el prompt en embeddings que alimenten el cross-attention del U-Net. Así que "123M" **es el número correcto para lo que Stable Diffusion efectivamente carga**. El error está en la etiqueta: no es "CLIP ViT-L/14 (123M)" sino "**el text encoder de CLIP ViT-L/14 (123M de los 428M del modelo completo)**". Dicho así, además, la slide gana: explica por qué el nombre menciona una variante de ViT (`L/14`) que refiere a una torre visual que Stable Diffusion ni siquiera usa — que es una pregunta que un alumno atento va a hacer.
  **Salvedad de trazabilidad:** ninguno de estos conteos está en la página capturada. El abstract **no reporta ningún número de parámetros**. La corrección es verificable (tabla 21 del paper de CLIP; la tarjeta de `openai/clip-vit-large-patch14` en Hugging Face reporta 427.616.513 parámetros totales, 123.650.304 de text encoder y 303.179.776 de vision encoder), pero **no contra el corpus actual**. Si la slide corregida cita un número, conviene que cite esa fuente y no el paper.

- **"77 tokens y 77×768" — NO CIERRAN CONTRA ESTA FUENTE.** El abstract no menciona longitud de contexto ni dimensiones de embedding. Los valores son correctos para CLIP ViT-L/14 —longitud de contexto fija de **77 tokens** (incluidos los tokens de inicio y fin), ancho del transformer de texto de **768**, de donde sale la matriz de **77×768** que Stable Diffusion pasa al cross-attention— pero su respaldo está en el código y la configuración de CLIP, no en la página capturada. Nótese la coherencia interna: el 768 de "77×768" es el mismo 768 que hace que el text encoder pese 123 M. Los dos números de la slide 42 describen el mismo objeto.

## Inconsistencies / open questions

1. **La página capturada trae solo el abstract.** Lo que la clase necesitaría y no está:
   - **La figura 1** — el diagrama del preentrenamiento contrastivo (la matriz N×N de similitudes con la diagonal como positivos) y el de clasificación zero-shot vía plantillas de texto. Es la imagen que explica CLIP.
   - La **tabla de variantes y conteos de parámetros** — justo lo que haría falta para respaldar (o corregir) la slide 42.
   - La **longitud de contexto de 77 tokens** y el ancho de 768.
   - La descripción del **espacio de embedding compartido** y de la similitud coseno.
   - El detalle de **WIT**, el dataset de 400 M, y cómo se construyó.
   - Las **limitaciones** que el propio paper documenta (desempeño pobre en tareas de conteo, en clasificación de grano fino especializada y en dígitos manuscritos; sesgos sociales medidos).
   Todo eso está en el PDF (`https://arxiv.org/pdf/2103.00020`), no capturado.
2. **La slide 42 atribuye al modelo completo el conteo del text encoder.** Detalle arriba. Es la imprecisión concreta a corregir en el deck: **123 M es el text encoder; el modelo completo son ~428 M**.
3. **"400 million pairs collected from the internet"** se enuncia sin detallar procedencia, filtrado ni licencias. El paper de LAION (`laion-5b-schuhmann-2022.web.md`) existe en buena medida como respuesta a esa opacidad: el dataset de CLIP nunca se liberó. Es un contraste que la clase puede aprovechar.
4. **Ningún número de parámetros en el abstract.** Cualquier afirmación de tamaño de modelo que haga el deck no proviene de esta fuente.
5. **La página no declara venue.** Si el deck cita "ICML 2021", el dato es correcto pero no sale de acá.
6. **El puente CLIP → Stable Diffusion no está en esta fuente.** Que Stable Diffusion use el text encoder de CLIP ViT-L/14, y sólo el text encoder, es un hecho central del deck y no aparece ni acá ni en el abstract de difusión latente. Es una conexión sin respaldo en el corpus.

## Images / diagrams

La captura de una página `abs` de arXiv **no incluye ninguna figura del paper** — no trae el diagrama del preentrenamiento contrastivo. Los tres archivos guardados son cromo del sitio, copiados a la carpeta compañera por completitud.

  - **Depiction:** logotipo institucional de arXiv en la barra superior del sitio (vectorial, tema claro).
  - **Why it matters:** nada. Cromo de navegación.
  - **Transcribed text:** "arXiv" (atributo `alt`: "archive").
  - **Depiction:** ícono de 16×16 px de BibSonomy — grafo de nodos gris con el nodo central en magenta.
  - **Why it matters:** nada. Botón de marcador.
  - **Transcribed text:** ninguno (atributo `alt`: "BibSonomy").
  - **Depiction:** ícono de 18×18 px de Reddit — mascota "Snoo" en gris con ojos rojos.
  - **Why it matters:** nada. Botón de compartir.
  - **Transcribed text:** ninguno (atributo `alt`: "Reddit").

## Raw / preserved excerpts

**Abstract completo, verbatim (inglés):**

> State-of-the-art computer vision systems are trained to predict a fixed set of predetermined object categories. This restricted form of supervision limits their generality and usability since additional labeled data is needed to specify any other visual concept. Learning directly from raw text about images is a promising alternative which leverages a much broader source of supervision. We demonstrate that the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch on a dataset of 400 million (image, text) pairs collected from the internet. After pre-training, natural language is used to reference learned visual concepts (or describe new ones) enabling zero-shot transfer of the model to downstream tasks. We study the performance of this approach by benchmarking on over 30 different existing computer vision datasets, spanning tasks such as OCR, action recognition in videos, geo-localization, and many types of fine-grained object classification. The model transfers non-trivially to most tasks and is often competitive with a fully supervised baseline without the need for any dataset specific training. For instance, we match the accuracy of the original ResNet-50 on ImageNet zero-shot without needing to use any of the 1.28 million training examples it was trained on. We release our code and pre-trained model weights at https://github.com/OpenAI/CLIP.

**Metadatos de la página, verbatim:**

> Computer Science > Computer Vision and Pattern Recognition
> arXiv:2103.00020 (cs)
> [Submitted on 26 Feb 2021]
> Title: Learning Transferable Visual Models From Natural Language Supervision
> Authors: Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever
> Subjects: Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)
> Cite as: arXiv:2103.00020 [cs.CV]
> https://doi.org/10.48550/arXiv.2103.00020
