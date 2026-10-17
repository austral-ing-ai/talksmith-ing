---
source_file: sam-kirillov-2023
source_type: web-capture
ingested_at: 2026-08-14
---

# Segment Anything — SAM (Kirillov et al., 2023) — página abstract de arXiv

## Provenance
- Original location: `research/web/sam-kirillov-2023/`
- Format: html (captura web de `talksmith:ingest` — `page.md` + `original.html` + `assets/`)
- Author / source (if known): Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao, Chloe Rolland, Laura Gustafson, Tete Xiao, Spencer Whitehead, Alexander C. Berg, Wan-Yen Lo, Piotr Dollár, Ross Girshick (12 autores; Meta AI Research, afiliación no visible en la captura) — arXiv
- Date of original (if known): enviado el 5 de abril de 2023 (v1, única versión). Captura: 2026-08-14T17:02:59Z, HTTP 200, URL `https://arxiv.org/abs/2304.02643`
- **Por qué está en el corpus**: la slide 6 lo nombra en la línea de tiempo generativa. No pertenece al linaje de GANs.

## Key claims

- **Presentan el proyecto Segment Anything (SA): una tarea nueva, un modelo nuevo y un dataset nuevo para segmentación de imágenes.** Los tres a la vez, y esa es la forma del paper.
- **Usando su modelo dentro de un bucle de recolección de datos, construyeron el dataset de segmentación más grande hasta la fecha "por lejos": más de 1.000 millones de máscaras sobre 11 millones de imágenes licenciadas y respetuosas de la privacidad.** El bucle modelo↔datos es el mecanismo: el modelo ayuda a etiquetar, los datos mejoran el modelo.
- **El modelo está diseñado y entrenado para ser *promptable***, de modo que transfiere **zero-shot** a distribuciones de imágenes y tareas nuevas.
- **Desempeño zero-shot "impresionante", con frecuencia competitivo o incluso superior a resultados previos completamente supervisados.**
- **Liberan modelo (SAM) y dataset (SA-1B)** en `https://segment-anything.com`, para fomentar la investigación en modelos fundacionales para visión por computadora.

Datos bibliográficos para la cita:
- Autores: 12 (Kirillov et al.)
- Año: 2023
- arXiv ID: **arXiv:2304.02643 [cs.CV]** (v1)
- DOI: `https://doi.org/10.48550/arXiv.2304.02643`
- Materias: Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
- Venue: la página **no** declara *journal reference*. Comments solo enlaza el sitio del proyecto. (Se presentó en ICCV 2023, pero **eso no está en la captura**.)

## Definitions and terminology

- **Promptable segmentation**: el modelo recibe una indicación (un punto, una caja, un texto, una máscara aproximada) y devuelve la máscara correspondiente. Es lo que traslada el paradigma de *prompting* de los LLMs a la segmentación. El abstract lo enuncia como propiedad de diseño ("designed and trained to be promptable"), sin detallar los tipos de prompt.
- **Zero-shot transfer**: aplicar el modelo a distribuciones de imágenes y tareas no vistas en entrenamiento, sin reentrenar ni ajustar.
- **Modelo fundacional para visión (foundation model for computer vision)**: la ambición declarada del proyecto — un modelo base reutilizable, análogo a lo que los LLMs son para texto.
- **SA-1B**: el dataset. 1.000 millones de máscaras, 11 millones de imágenes.
- **SAM (Segment Anything Model)**: el modelo.
- **Nada de este vocabulario es de GANs.** No hay generador, discriminador, entrenamiento adversarial, espacio latente ni juego minimax. SAM es un modelo **discriminativo** de segmentación, no generativo.

## Evidence and examples

- **Más de 1.000 millones de máscaras** (*over 1 billion masks*).
- **11 millones de imágenes**, descritas como licenciadas y respetuosas de la privacidad.
- **Dataset nombrado: SA-1B.** Y es el único caso del corpus donde el dataset es la contribución central del paper.
- Desempeño zero-shot competitivo o superior a métodos completamente supervisados en numerosas tareas — **sin métricas ni números concretos en la captura**.
- Sitio del proyecto con modelo y datos: `https://segment-anything.com`.
- Peso de la subida: 14.399 KB.

## Inconsistencies / open questions

- **[Punto 5 del encargo] Dice 0.9524 vs 0.9459 (slide 5).** Esta es la fuente del corpus que más se le acerca — el coeficiente de Dice es **la** métrica de segmentación, y SAM es **el** paper de segmentación del corpus. Pero: **esta captura no contiene ningún valor de Dice, ni ninguna otra métrica numérica.** El abstract habla de desempeño zero-shot "impresionante" y "competitivo" sin una sola cifra. Ninguna de las 14 fuentes de `research/web/` respalda el par 0.9524 / 0.9459. Si la slide 5 lo conserva, hace falta la fuente original: qué modelos se comparan, sobre qué dataset, con qué protocolo, y de qué publicación salen los números. Dos valores de Dice a cuatro decimales sin contexto no son verificables ni interpretables — una diferencia de 0.0065 puede ser ruido de partición, y sin desvío estándar ni tamaño de muestra no hay forma de saberlo.
- **SAM no es una GAN, ni un modelo generativo.** Es un modelo de segmentación. Si la línea de tiempo generativa de la slide 6 lo lista junto a GANs, VAEs, difusión y LLMs, está mezclando categorías. Hay una lectura defendible — 2023 como el año en que los "modelos fundacionales" llegaron a visión, y SAM como hito de esa ola — pero conviene que la slide diga eso y no lo deje sugerido. Mismo cuidado, por otra razón, que con `adain-huang-belongie-2017.web.md`.
- **[Punto 4 del encargo] Dataset nombrado: SA-1B, con sus dos números (1.000 M de máscaras, 11 M de imágenes).** Se registra porque el deck argumenta sobre datasets en cuatro slides sin nombrar ninguno, y este paper es el argumento más fuerte posible a favor de nombrarlos: **su contribución principal ES el dataset**. Si la clase quiere un ejemplo de por qué el dataset importa tanto como la arquitectura, es este.
- **Sin venue impreso** en la captura.
- **Gap de extracción**: sin figuras, sin métricas, sin la descripción del *data engine* de tres etapas. Todo en el PDF y en el sitio del proyecto.

## Images / diagrams

La captura solo trajo chrome de la interfaz de arXiv. Ninguna imagen del paper.

  - Depiction: logotipo de arXiv en versión clara, SVG vectorial de 246.98 × 111.12, siete trazados agrupados. Texto convertido a curvas.
  - Why it matters: branding del sitio, sin valor de contenido.
  - Transcribed text: (el logo dibuja "arXiv"; sin texto seleccionable). `alt="archive"`.
  - Depiction: ícono social de BibSonomy, 16×16 px, huesos cruzados en rojo.
  - Why it matters: chrome de UI.
  - Transcribed text: ninguno. `alt="BibSonomy"`.
  - Depiction: ícono social de Reddit, 16×16 px, mascota Snoo en naranja y blanco.
  - Why it matters: chrome de UI.
  - Transcribed text: ninguno. `alt="Reddit"`.

## Raw / preserved excerpts

Abstract completo, verbatim (inglés original):

> Abstract: We introduce the Segment Anything (SA) project: a new task, model, and dataset for image segmentation. Using our efficient model in a data collection loop, we built the largest segmentation dataset to date (by far), with over 1 billion masks on 11M licensed and privacy respecting images. The model is designed and trained to be promptable, so it can transfer zero-shot to new image distributions and tasks. We evaluate its capabilities on numerous tasks and find that its zero-shot performance is impressive -- often competitive with or even superior to prior fully supervised results. We are releasing the Segment Anything Model (SAM) and corresponding dataset (SA-1B) of 1B masks and 11M images at https://segment-anything.com to foster research into foundation models for computer vision.

Bloque bibliográfico verbatim:

> Computer Science > Computer Vision and Pattern Recognition
> **arXiv:2304.02643** (cs) [Submitted on 5 Apr 2023]
> Title: Segment Anything
> Authors: Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao, Chloe Rolland, Laura Gustafson, Tete Xiao, Spencer Whitehead, Alexander C. Berg, Wan-Yen Lo, Piotr Dollár, Ross Girshick
> Comments: Project web-page: https://segment-anything.com
> Subjects: Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
> Cite as: arXiv:2304.02643 [cs.CV] (or arXiv:2304.02643v1 [cs.CV] for this version)
> https://doi.org/10.48550/arXiv.2304.02643

> Submission history
> From: Alexander Kirillov
> **[v1]** Wed, 5 Apr 2023 17:59:46 UTC (14,399 KB)
