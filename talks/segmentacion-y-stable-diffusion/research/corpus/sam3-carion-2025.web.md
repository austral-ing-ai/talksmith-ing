---
source_file: sam3-carion-2025
source_type: web-capture
ingested_at: 2026-08-14
---

# SAM 3: Segment Anything with Concepts (arXiv:2511.16719) — página de abstract

## Provenance
- Original location: `research/web/sam3-carion-2025/`
- Format: web-capture (arXiv `abs` page; `page.md` + `original.html` + `assets/`)
- URL: https://arxiv.org/abs/2511.16719
- Author / source (if known): Nicolas Carion et al. (Meta Superintelligence Labs / FAIR) — 38 autores
- Date of original (if known): enviado 20 nov 2025; **última revisión 28 mar 2026 (v2)**
- Fetched at: 2026-08-14T17:03:10Z (HTTP 200, 46.329 bytes)
- Rol en la Clase 9: el estado del arte del bloque de segmentación — vocabulario abierto, prompts de texto. La v2 de marzo 2026 es la que incorpora SAM 3.1.

## Key claims

- **Autores:** Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath, Ronghang Hu, Didac Suris, Chaitanya Ryali, Kalyan Vasudev Alwala, Haitham Khedr, Andrew Huang, Jie Lei, Tengyu Ma, Baishan Guo, Arpit Kalla, Markus Marks, Joseph Greer, Meng Wang, Peize Sun, Roman Rädle, Triantafyllos Afouras, Effrosyni Mavroudi, Katherine Xu, Tsung-Han Wu, Yu Zhou, Liliane Momeni, Rishi Hazra, Shuangrui Ding, Sagar Vaze, Francois Porcher, Feng Li, Siyuan Li, Aishwarya Kamath, Ho Kei Cheng, Piotr Dollár, Nikhila Ravi, Kate Saenko, Pengchuan Zhang, Christoph Feichtenhofer. **Año:** 2025 (v1) / 2026 (v2). **Venue:** preprint arXiv — la página **no declara venue** (no hay campo `Comments`). **arXiv ID:** arXiv:2511.16719 [cs.CV, cs.AI]. **DOI:** 10.48550/arXiv.2511.16719.
- SAM 3 es un **modelo unificado que detecta, segmenta y sigue objetos** en imágenes y videos **a partir de *concept prompts***.
- Un *concept prompt* se define como: **una frase nominal corta** (p. ej. "yellow school bus"), **un ejemplar en imagen**, o una combinación de ambos.
- La tarea nueva se llama **Promptable Concept Segmentation (PCS)**: toma esos prompts y devuelve máscaras de segmentación **e identidades únicas** para todas las instancias que coinciden.
- Construyen un **data engine escalable** que produce un dataset de alta calidad con **4 millones de etiquetas de concepto únicas**, incluyendo **negativos difíciles** (*hard negatives*), sobre imágenes y videos.
- Arquitectura: **un detector a nivel de imagen y un tracker de video basado en memoria que comparten un único backbone**. Reconocimiento y localización se **desacoplan** mediante una ***presence head***, que sube la exactitud de detección.
- **SAM 3 duplica la exactitud de los sistemas existentes** en PCS tanto en imagen como en video, y mejora las capacidades previas de SAM en tareas de segmentación visual.
- Liberan SAM 3 junto con el nuevo benchmark **SA-Co (Segment Anything with Concepts)**.

## Definitions and terminology

- **Vocabulario abierto (*open vocabulary*).** Es el concepto que la clase toma de acá, aunque el abstract **no usa la expresión "open vocabulary"** literalmente: la expresa por su contenido — prompts que son "short noun phrases", no etiquetas de una lista fija. La formulación explícita del término sí está en el post de Meta: "SAM 3 accepts text prompts — open-vocabulary short noun phrases — and image exemplar prompts, eliminating the constraints of fixed label sets" (ver `sam31-meta-2026.web.md`). Si la clase define vocabulario abierto, conviene citar el post, no el abstract.
- **Concept prompt.** "Either short noun phrases (e.g., 'yellow school bus'), image exemplars, or a combination of both." Definición literal y completa en el abstract.
- **Promptable Concept Segmentation (PCS).** "Takes such prompts and returns segmentation masks and unique identities for all matching object instances." Nótese el "**all**": la tarea es exhaustiva — hay que encontrar *todas* las instancias, no una. Y "unique identities" arrastra el eje temporal: es segmentación de instancias con seguimiento.
- **Hard negatives.** Conceptos que **no** están presentes en la imagen o el video, incluidos deliberadamente en el dataset para que el modelo aprenda a no alucinar detecciones.
- **Presence head.** Componente que desacopla el reconocimiento ("¿está este concepto en la imagen?") de la localización ("¿dónde exactamente?"). El abstract dice que sube la exactitud de detección pero **no explica cómo funciona**.
- **Backbone compartido.** Detector de imagen + tracker de video sobre un único backbone. El post de Meta detalla lo que el abstract calla: los encoders de texto e imagen vienen del Meta Perception Encoder, el detector se basa en DETR, y el tracker hereda el memory bank de SAM 2.
- **SA-Co.** El benchmark liberado para PCS.

## Evidence and examples

- **4 millones de etiquetas de concepto únicas** en el dataset del data engine.
- **Duplica ("doubles") la exactitud** de los sistemas existentes en PCS, en imagen y en video. El abstract **no dice sobre qué métrica** — el post de Meta sí: cgF1 en imágenes sobre SA-Co Gold, pHOTA en video sobre SA-Co SA-V.
- Mejora sobre las capacidades previas de SAM en tareas de segmentación visual — **sin números en el abstract**.
- **38 autores**: es un paper de escala industrial, no un trabajo de laboratorio pequeño. Vale como dato de contexto sobre el costo de producir estos modelos.

### Verificación de cifras del deck

- **Fecha "Marzo 2026" de SAM 3.1 — CIERRA, y esta fuente lo corrobora por un camino independiente.** La página `abs` registra "last revised **28 Mar 2026** (this version, v2)": la revisión del paper de SAM 3 que incorpora SAM 3.1 se subió el 28 de marzo de 2026. El anuncio de Meta es del **27 de marzo de 2026** (ver `sam31-meta-2026.web.md`), es decir el día anterior. Ambas fechas caen en marzo de 2026 y son mutuamente consistentes: blog el 27, revisión del paper el 28.
- Todos los números de SAM 3 que el deck pudiera querer (2× de mejora, 4 M de conceptos) están respaldados acá; los valores absolutos por benchmark **no** están en el abstract y hay que tomarlos de la figura de resultados del post de Meta.

## Inconsistencies / open questions

1. **La página capturada trae solo el abstract.** Lo que la clase necesitaría y no está:
   - **El diagrama de arquitectura** (backbone compartido, detector, tracker, presence head) — la imagen que explicaría el salto SAM 2 → SAM 3.
   - La **explicación de la presence head**: se afirma que mejora la detección, no se dice por qué.
   - Los **valores absolutos** de los benchmarks: "doubles the accuracy" es un multiplicador sin base. Los números están en el post de Meta y en el cuerpo del paper.
   - La composición de **SA-Co** (subconjuntos Gold, SA-V, tamaños, protocolo de anotación).
   - El detalle del **data engine** con anotadores humanos y de IA — que el post de Meta sí cubre en prosa y en figura.
   - **Qué cambió entre v1 (nov 2025) y v2 (mar 2026)**: la página registra que hay dos versiones pero **no incluye ninguna nota de cambios**. Que la v2 sea del 28 de marzo de 2026 y el anuncio de SAM 3.1 del 27 sugiere fuertemente que la v2 incorpora SAM 3.1, pero la página no lo afirma. Es una inferencia razonable, no un hecho documentado en la fuente.
2. **La página no declara venue.** No hay campo `Comments`. Cualquier atribución de conferencia que haga el deck no sale de acá.
3. **Métrica de evaluación:** otra vez, el abstract habla de "accuracy" sin nombrar métrica. El hueco del deck (22 slides de segmentación sin Dice ni IoU) se repite. La fuente del corpus que rompe el patrón es la figura de resultados del post de Meta, que nombra y cuantifica cinco métricas distintas.
4. **"Doubles the accuracy of existing systems"** es una afirmación de marketing enunciada en un abstract académico. Cierra contra los números del post (cgF1 53,9 de SAM 3 vs 24,6 de OWLv2 en SA-Co Gold: 2,2×; pHOTA 58,0 vs 30,1 de LLMDet+SAM3 Tracker en SA-Co SA-V: 1,9×), pero el abstract no da al lector ninguna forma de comprobarlo.

## Images / diagrams

La captura de una página `abs` de arXiv **no incluye ninguna figura del paper**. Los tres archivos guardados son cromo del sitio, copiados a la carpeta compañera por completitud.

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

> We present Segment Anything Model (SAM) 3, a unified model that detects, segments, and tracks objects in images and videos based on concept prompts, which we define as either short noun phrases (e.g., "yellow school bus"), image exemplars, or a combination of both. Promptable Concept Segmentation (PCS) takes such prompts and returns segmentation masks and unique identities for all matching object instances. To advance PCS, we build a scalable data engine that produces a high-quality dataset with 4M unique concept labels, including hard negatives, across images and videos. Our model consists of an image-level detector and a memory-based video tracker that share a single backbone. Recognition and localization are decoupled with a presence head, which boosts detection accuracy. SAM 3 doubles the accuracy of existing systems in both image and video PCS, and improves previous SAM capabilities on visual segmentation tasks. We open source SAM 3 along with our new Segment Anything with Concepts (SA-Co) benchmark for promptable concept segmentation.

**Metadatos de la página, verbatim:**

> Computer Science > Computer Vision and Pattern Recognition
> arXiv:2511.16719 (cs)
> [Submitted on 20 Nov 2025 (v1), last revised 28 Mar 2026 (this version, v2)]
> Title: SAM 3: Segment Anything with Concepts
> Authors: Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath, Ronghang Hu, Didac Suris, Chaitanya Ryali, Kalyan Vasudev Alwala, Haitham Khedr, Andrew Huang, Jie Lei, Tengyu Ma, Baishan Guo, Arpit Kalla, Markus Marks, Joseph Greer, Meng Wang, Peize Sun, Roman Rädle, Triantafyllos Afouras, Effrosyni Mavroudi, Katherine Xu, Tsung-Han Wu, Yu Zhou, Liliane Momeni, Rishi Hazra, Shuangrui Ding, Sagar Vaze, Francois Porcher, Feng Li, Siyuan Li, Aishwarya Kamath, Ho Kei Cheng, Piotr Dollár, Nikhila Ravi, Kate Saenko, Pengchuan Zhang, Christoph Feichtenhofer
> Subjects: Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)
> Cite as: arXiv:2511.16719 [cs.CV]
> https://doi.org/10.48550/arXiv.2511.16719
