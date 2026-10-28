---
source_file: sam2-ravi-2024
source_type: web-capture
ingested_at: 2026-08-14
---

# SAM 2: Segment Anything in Images and Videos (arXiv:2408.00714) — página de abstract

## Provenance
- Original location: `research/web/sam2-ravi-2024/`
- Format: web-capture (arXiv `abs` page; `page.md` + `original.html` + `assets/`)
- URL: https://arxiv.org/abs/2408.00714
- Author / source (if known): Nikhila Ravi et al. (Meta FAIR) — 18 autores
- Date of original (if known): enviado 1 ago 2024; última revisión 28 oct 2024 (v2)
- Fetched at: 2026-08-14T17:03:10Z (HTTP 200, 43.343 bytes)
- Rol en la Clase 9: el salto de imagen a video — introduce el banco de memoria, el concepto que la clase usa para explicar cómo se mantiene la identidad de un objeto entre frames.

## Key claims

- **Autores:** Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman Rädle, Chloe Rolland, Laura Gustafson, Eric Mintun, Junting Pan, Kalyan Vasudev Alwala, Nicolas Carion, Chao-Yuan Wu, Ross Girshick, Piotr Dollár, Christoph Feichtenhofer. **Año:** 2024. **Venue:** preprint arXiv; el campo `Comments` sólo enlaza `https://ai.meta.com/sam2` (el paper se presentó luego en ICLR 2025, dato **no** presente en la página). **arXiv ID:** arXiv:2408.00714 [cs.CV, cs.AI, cs.LG]. **DOI:** 10.48550/arXiv.2408.00714.
- SAM 2 es un **modelo fundacional para segmentación visual promptable en imágenes y videos** — unifica los dos dominios en un solo modelo.
- Construyen un **data engine** que mejora modelo y datos vía interacción con usuarios, y con él recolectan **el mayor dataset de segmentación de video hasta la fecha**.
- Arquitectura: **un transformer simple con memoria en streaming (*streaming memory*) para procesamiento de video en tiempo real**. Es el "banco de memoria" de la clase.
- **En video: mejor exactitud usando 3× menos interacciones** que los enfoques previos.
- **En imagen: más preciso y 6× más rápido** que SAM 1.
- Liberan modelo principal, dataset, código de entrenamiento y demo.

## Definitions and terminology

- **Banco de memoria / memoria en streaming.** "Our model is a simple transformer architecture with streaming memory for real-time video processing." El abstract nombra el mecanismo y su propósito (procesar video en tiempo real, frame a frame, sin ver el video completo) pero **no describe sus partes**: ni el *memory encoder*, ni el *memory bank* de frames recientes y frames con prompt, ni el módulo de *memory attention* que condiciona el frame actual sobre lo almacenado. La clase enseña esa estructura interna; no sale de esta página. El post de Meta sobre SAM 3 (`sam31-meta-2026.web.md`) sí confirma explícitamente que "the memory bank and memory encoder used in SAM 2 is the basis for the Tracker component" de SAM 3 — esa frase es el mejor respaldo textual disponible en el corpus para el término *banco de memoria*.
- **Promptable visual segmentation (PVS).** La tarea que SAM 2 define, extendiendo la segmentación promptable de SAM 1 al eje temporal. El abstract usa la frase "promptable visual segmentation in images and videos" sin desarrollarla.
- **Data engine.** Acá sí aparece el término explícito: "We build a data engine, which improves model and data via user interaction". Es el mismo mecanismo que SAM 1 describía sin nombrar.
- **Masklet.** **Ausente del abstract.** El término que SAM 2 acuña para la máscara que persiste a lo largo del tiempo (una máscara con identidad, extendida sobre frames) no aparece en la página capturada. Sí aparece en el post de Meta sobre SAM 3, que habla de "a SAM 2-style masklet".
- **SA-V.** El dataset de video liberado. El abstract lo menciona como "the largest video segmentation dataset to date" pero **no lo nombra SA-V ni da su tamaño** (ni cantidad de videos, ni de masklets).

## Evidence and examples

- **3× menos interacciones** para igualar o superar la exactitud previa en segmentación de video.
- **6× más rápido** que SAM 1 en segmentación de imagen, y más preciso.
- "Largest video segmentation dataset to date" — **sin cifra**.
- Liberación de modelo, dataset, código de entrenamiento y demo.

### Verificación de cifras del deck

El deck no atribuye cifras específicas a SAM 2 entre las que este encargo pide verificar. Los dos multiplicadores del abstract (3× menos interacciones, 6× más rápido) están disponibles y verificados si la clase quisiera usarlos. Nota de precisión: el "6× más rápido" es **contra SAM 1 en imágenes**, no contra nada en video; y el "3× menos interacciones" es **en video**. Confundir los dominios de esos dos multiplicadores es el error fácil.

## Inconsistencies / open questions

1. **La página capturada trae solo el abstract.** Lo que la clase necesitaría y no está:
   - **El diagrama de arquitectura con el banco de memoria** (memory encoder, memory bank, memory attention) — la imagen que explica por qué SAM 2 puede seguir un objeto entre frames.
   - El **tamaño del dataset SA-V** (videos, masklets, horas) y hasta su nombre.
   - El término **masklet** y su definición.
   - Los **números absolutos de benchmark** (J&F sobre SA-V, MOSE, DAVIS, YouTube-VOS) — el abstract sólo da multiplicadores relativos.
   - La **latencia en FPS** del procesamiento en streaming.
   Todo eso está en el PDF (`https://arxiv.org/pdf/2408.00714`), no capturado.
2. **Multiplicadores sin línea base explícita.** "3x fewer interactions than prior approaches" no dice cuáles son esos enfoques previos ni sobre qué benchmark; "6x faster" no dice en qué hardware ni con qué tamaño de modelo. Son cifras citables pero débiles fuera de contexto.
3. **Métrica de evaluación:** el abstract habla de "better accuracy" sin nombrar ninguna métrica. Nuevo caso del hueco del deck (22 slides de segmentación sin Dice ni IoU): la métrica canónica de segmentación de video, **J&F**, es la que corresponde acá y no aparece. Sí aparece cuantificada en la figura de resultados del post de Meta (`sam31-meta-2026.web.md`: SAM 3 84,4 en J&F sobre SA-V test).
4. **Venue no declarado** en la página: si el deck cita "ICLR 2025", el dato es correcto pero no proviene de esta fuente.

## Images / diagrams

La captura de una página `abs` de arXiv **no incluye ninguna figura del paper** — en particular, no trae el diagrama del banco de memoria. Los tres archivos guardados son cromo del sitio, copiados a la carpeta compañera por completitud.

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

> We present Segment Anything Model 2 (SAM 2), a foundation model towards solving promptable visual segmentation in images and videos. We build a data engine, which improves model and data via user interaction, to collect the largest video segmentation dataset to date. Our model is a simple transformer architecture with streaming memory for real-time video processing. SAM 2 trained on our data provides strong performance across a wide range of tasks. In video segmentation, we observe better accuracy, using 3x fewer interactions than prior approaches. In image segmentation, our model is more accurate and 6x faster than the Segment Anything Model (SAM). We believe that our data, model, and insights will serve as a significant milestone for video segmentation and related perception tasks. We are releasing our main model, dataset, as well as code for model training and our demo.

**Metadatos de la página, verbatim:**

> Computer Science > Computer Vision and Pattern Recognition
> arXiv:2408.00714 (cs)
> [Submitted on 1 Aug 2024 (v1), last revised 28 Oct 2024 (this version, v2)]
> Title: SAM 2: Segment Anything in Images and Videos
> Authors: Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman Rädle, Chloe Rolland, Laura Gustafson, Eric Mintun, Junting Pan, Kalyan Vasudev Alwala, Nicolas Carion, Chao-Yuan Wu, Ross Girshick, Piotr Dollár, Christoph Feichtenhofer
> Comments: Website: https://ai.meta.com/sam2
> Subjects: Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
> Cite as: arXiv:2408.00714 [cs.CV]
> https://doi.org/10.48550/arXiv.2408.00714
