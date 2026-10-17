---
source_file: dcgan-radford-2015
source_type: web-capture
ingested_at: 2026-08-14
---

# Unsupervised Representation Learning with Deep Convolutional GANs (Radford et al., 2015) — página abstract de arXiv

## Provenance
- Original location: `research/web/dcgan-radford-2015/`
- Format: html (captura web de `talksmith:ingest` — `page.md` + `original.html` + `assets/`)
- Author / source (if known): Alec Radford, Luke Metz, Soumith Chintala — arXiv
- Date of original (if known): enviado el 19 de noviembre de 2015 (v1), última revisión 7 de enero de 2016 (v2, la capturada). Captura: 2026-08-14T17:02:50Z, HTTP 200, URL `https://arxiv.org/abs/1511.06434`

## Key claims

- **Introducen una clase de CNNs llamada DCGAN** (*deep convolutional generative adversarial networks*) "que tienen ciertas restricciones arquitectónicas" y son un candidato fuerte para el aprendizaje no supervisado.
- **El objetivo declarado del paper no es generar imágenes lindas, sino cerrar la brecha entre el éxito de las CNNs en aprendizaje supervisado y el aprendizaje no supervisado.** El título lo dice: *Unsupervised Representation Learning*. La clase suele leer DCGAN como "la GAN con convoluciones"; el paper se presenta a sí mismo como un paper de representaciones.
- **El par adversarial convolucional aprende una jerarquía de representaciones, de partes de objetos a escenas**, tanto en el generador como en el discriminador — y lo muestran con "convincing evidence" entrenando sobre varios datasets de imágenes.
- **Reutilizan las características aprendidas para tareas nuevas**, demostrando su aplicabilidad como representaciones de imagen de propósito general. Es decir: el discriminador entrenado sin etiquetas sirve como extractor de features.
- Es el eslabón del linaje donde las GANs pasan de MLPs a convoluciones, y donde aparece el recetario de estabilidad que todos copiaron después.

Datos bibliográficos para la cita:
- Autores: Alec Radford, Luke Metz, Soumith Chintala
- Año: 2015 (arXiv v1) / 2016 (ICLR)
- arXiv ID: **arXiv:1511.06434 [cs.LG]** (v2)
- DOI: `https://doi.org/10.48550/arXiv.1511.06434`
- Materias: Machine Learning (cs.LG); Computer Vision and Pattern Recognition (cs.CV)
- Venue: el campo Comments dice **"Under review as a conference paper at ICLR 2016"**. DBLP lo lista bajo `conf/iclr/iclr2016.html#RadfordMC15`, es decir, terminó publicado en **ICLR 2016**. Ojo: la página de arXiv congela el estado "under review"; el venue final surge del listado de DBLP que la misma captura enlaza.

## Definitions and terminology

- **DCGAN**: GAN cuyo generador y discriminador son redes convolucionales profundas sujetas a un conjunto de restricciones arquitectónicas (*architectural constraints*). El abstract nombra las restricciones pero **no las enumera** — la lista concreta (sin capas fully-connected, batch normalization, ReLU en el generador salvo la salida con tanh, LeakyReLU en el discriminador, strided convolutions en lugar de pooling) está en la Sección 3 del paper, **no en esta captura**.
- **Convoluciones transpuestas**: el mecanismo con el que el generador sube de resolución desde el vector latente. **No aparecen nombradas en esta captura** — el abstract no las menciona. La fuente del corpus que sí las nombra explícitamente, en español y a nivel didáctico, es `aws-que-es-una-gan.web.md` ("el generador utiliza convoluciones transpuestas para aumentar la distribución de los datos"). Si la clase define el término, esa es la cita honesta; para la definición técnica hay que ir al PDF de DCGAN.
- **Recetas de estabilidad**: en esta captura aparecen solo como "certain architectural constraints" y, en boca de AWS, como "directrices de arquitectura para hacer que la capacitación sea más estable". Mismo cuidado que arriba.
- **Jerarquía de representaciones (hierarchy of representations)**: de partes de objetos a escenas. Es el hallazgo interpretativo del paper.
- **Representaciones de imagen de propósito general (general image representations)**: features del discriminador reutilizables en tareas supervisadas.

## Evidence and examples

- "Training on various image datasets" — el abstract afirma haber entrenado en varios datasets **sin nombrar ninguno**. (En el paper son LSUN Bedrooms, Imagenet-1k y un dataset de caras; **eso no está en la captura** y no debe citarse desde este registro.)
- Evidencia cualitativa: la jerarquía de representaciones aprendida en generador y discriminador.
- Evidencia cuantitativa: uso de las features aprendidas en tareas nuevas. Sin números en la captura.
- Peso de la subida: 9.027 KB en v1 y 9.028 KB en v2 — un paper cargado de figuras, ninguna de las cuales llegó a esta captura.

## Inconsistencies / open questions

- **Gap de extracción severo para lo que la clase quiere.** El deck usa DCGAN para hablar de convoluciones transpuestas y de recetas de estabilidad, y **ninguna de las dos cosas está en el abstract**. Este registro sirve para fechar, atribuir y ubicar el paper en el linaje; no alcanza para sostener las afirmaciones técnicas finas. Para eso: PDF, Sección 3 ("Approach and Model Architecture").
- **Datasets: el abstract dice "various image datasets" y no nombra ninguno.** Se anota porque es exactamente el mismo silencio que tiene el deck en sus cuatro slides sobre datasets. Acá la fuente primaria tampoco ayuda; hay que ir al paper o apoyarse en `progan-…`, `fid-heusel-2017` o `inception-score-salimans-2016`, que sí nombran los suyos.
- **Venue ambiguo en la captura**: "Under review as a conference paper at ICLR 2016" no es lo mismo que "publicado en ICLR 2016". El listado de DBLP en la misma página resuelve la ambigüedad a favor de ICLR 2016.
- **Año en la tabla de linaje**: arXiv 2015, ICLR 2016. Si la tabla de la slide 39 usa una sola columna de año, conviene fijar el criterio (fecha de arXiv) y aplicarlo igual a todas las filas — el mismo problema aparece de forma aguda en `stylegan-karras-2019.web.md`.

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

> Abstract: In recent years, supervised learning with convolutional networks (CNNs) has seen huge adoption in computer vision applications. Comparatively, unsupervised learning with CNNs has received less attention. In this work we hope to help bridge the gap between the success of CNNs for supervised learning and unsupervised learning. We introduce a class of CNNs called deep convolutional generative adversarial networks (DCGANs), that have certain architectural constraints, and demonstrate that they are a strong candidate for unsupervised learning. Training on various image datasets, we show convincing evidence that our deep convolutional adversarial pair learns a hierarchy of representations from object parts to scenes in both the generator and discriminator. Additionally, we use the learned features for novel tasks - demonstrating their applicability as general image representations.

Bloque bibliográfico verbatim:

> Computer Science > Machine Learning
> **arXiv:1511.06434** (cs) [Submitted on 19 Nov 2015 (v1), last revised 7 Jan 2016 (this version, v2)]
> Title: Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks
> Authors: Alec Radford, Luke Metz, Soumith Chintala
> Comments: Under review as a conference paper at ICLR 2016
> Subjects: Machine Learning (cs.LG); Computer Vision and Pattern Recognition (cs.CV)
> Cite as: arXiv:1511.06434 [cs.LG] (or arXiv:1511.06434v2 [cs.LG] for this version)
> https://doi.org/10.48550/arXiv.1511.06434

> Submission history
> From: Alec Radford
> **[v1]** Thu, 19 Nov 2015 22:50:32 UTC (9,027 KB)
> **[v2]** Thu, 7 Jan 2016 23:09:39 UTC (9,028 KB)

> DBLP - CS Bibliography
> listing | bibtex — Alec Radford, Luke Metz, Soumith Chintala
> https://dblp.uni-trier.de/db/conf/iclr/iclr2016.html#RadfordMC15
