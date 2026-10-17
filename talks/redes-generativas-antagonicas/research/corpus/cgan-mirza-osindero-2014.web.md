---
source_file: cgan-mirza-osindero-2014
source_type: web-capture
ingested_at: 2026-08-14
---

# Conditional Generative Adversarial Nets (Mirza & Osindero, 2014) — página abstract de arXiv

## Provenance
- Original location: `research/web/cgan-mirza-osindero-2014/`
- Format: html (captura web de `talksmith:ingest` — `page.md` + `original.html` + `assets/`)
- Author / source (if known): Mehdi Mirza, Simon Osindero — arXiv
- Date of original (if known): enviado el 6 de noviembre de 2014 (v1, única versión). Captura: 2026-08-14T17:02:50Z, HTTP 200, URL `https://arxiv.org/abs/1411.1784`

## Key claims

- **La cGAN es la versión condicional de la GAN**, y se construye "simplemente alimentando con los datos `y` sobre los que queremos condicionar tanto al generador como al discriminador". El abstract subraya esa simplicidad: *"can be constructed by simply feeding the data, y, we wish to condition on to both the generator and discriminator"*. Es el punto que la clase necesita — el condicionamiento no cambia la arquitectura, cambia la entrada de **las dos** redes.
- **Demuestran generación de dígitos MNIST condicionada por etiqueta de clase.** Este es el caso de uso canónico: en vez de "generame un dígito", "generame un 7".
- **Ilustran cómo el modelo podría usarse para aprender un modelo multimodal**, y dan ejemplos preliminares de una aplicación a *image tagging* en la que el enfoque genera etiquetas descriptivas que no forman parte de las etiquetas de entrenamiento.
- El paper se apoya explícitamente en Goodfellow et al. 2014 (referencia [8] en su propio abstract), que es `gan-goodfellow-2014.web.md` en este corpus. El linaje del deck (slide 39) está bien puesto en este eslabón.

Datos bibliográficos para la cita:
- Autores: Mehdi Mirza, Simon Osindero
- Año: 2014
- arXiv ID: **arXiv:1411.1784 [cs.LG]** (v1)
- DOI: `https://doi.org/10.48550/arXiv.1411.1784`
- Materias: Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (stat.ML)
- Venue: la página **no** declara *journal reference* ni comentario de conferencia. El paper nunca pasó por revisión formal — es un preprint de arXiv, y así hay que citarlo. DBLP lo lista como `journals/corr/MirzaO14`.

## Definitions and terminology

- **Condicionamiento (conditioning)**: alimentar información adicional `y` a ambas redes. El abstract nombra la variable con la letra `y`; la clase usa "etiqueta" o "condición".
- **Etiqueta de clase (class label)**: el tipo concreto de `y` usado en el experimento de MNIST. Es la instancia mínima de condicionamiento y la que conviene usar para explicarlo.
- **Modelo multimodal (multi-modal model)**: en el uso del paper, un modelo que mapea una entrada a **múltiples** salidas válidas — el caso de *image tagging*, donde una imagen admite varias etiquetas correctas. No confundir con "multimodal" en el sentido actual de texto+imagen+audio; en 2014 la palabra significa otra cosa, y la clase debería evitar la ambigüedad si cita este paper.
- **Image tagging**: generar etiquetas descriptivas para una imagen, incluidas etiquetas fuera del vocabulario de entrenamiento.
- El abstract **no** define espacio latente ni ruido `z`; hereda la formulación de Goodfellow et al.

## Evidence and examples

- **MNIST condicionado por clase**: el único resultado explícito del abstract ("We show that this model can generate MNIST digits conditioned on class labels"). Es también **el único dataset nombrado** en esta captura.
- **Image tagging**: descrito como "preliminary examples", con esa cautela textual. Si la clase lo menciona, conviene conservar el calificativo — los propios autores no lo presentan como resultado sólido.
- No hay tablas, métricas ni comparaciones en la captura: es la página `abs/`, no el paper.

## Inconsistencies / open questions

- **Dataset nombrado: MNIST.** Anotado deliberadamente, porque el deck argumenta sobre datasets en cuatro slides sin nombrar ni uno. Este es uno de los pocos registros del corpus donde la fuente sí nombra el suyo, y es además el más didáctico: MNIST es lo que hace visible qué significa "condicionar por etiqueta".
- **Estatus editorial**: es un preprint sin venue. Si el deck lo pone en una tabla de linaje junto a papers de CVPR/ICLR/NeurIPS, la columna "venue" no debería inventarle uno.
- **"Multimodal" es un falso amigo temporal** (ver *Definitions*): en 2014 designa salidas múltiples para una misma entrada, no modalidades de datos distintas. Riesgo real de malinterpretación en clase.
- **Gap de extracción**: la captura no contiene la formulación del objetivo condicional ni la Figura 2 (la grilla de dígitos por clase), que es justamente la imagen que la clase querría proyectar. Hay que ir al PDF.

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

> Abstract: Generative Adversarial Nets [8] were recently introduced as a novel way to train generative models. In this work we introduce the conditional version of generative adversarial nets, which can be constructed by simply feeding the data, y, we wish to condition on to both the generator and discriminator. We show that this model can generate MNIST digits conditioned on class labels. We also illustrate how this model could be used to learn a multi-modal model, and provide preliminary examples of an application to image tagging in which we demonstrate how this approach can generate descriptive tags which are not part of training labels.

Bloque bibliográfico verbatim:

> Computer Science > Machine Learning
> **arXiv:1411.1784** (cs) [Submitted on 6 Nov 2014]
> Title: Conditional Generative Adversarial Nets
> Authors: Mehdi Mirza, Simon Osindero
> Subjects: Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (stat.ML)
> Cite as: arXiv:1411.1784 [cs.LG] (or arXiv:1411.1784v1 [cs.LG] for this version)
> https://doi.org/10.48550/arXiv.1411.1784

> Submission history
> From: Mehdi Mirza
> **[v1]** Thu, 6 Nov 2014 22:33:22 UTC (643 KB)

> DBLP - CS Bibliography
> listing | bibtex — Mehdi Mirza, Simon Osindero
> https://dblp.uni-trier.de/db/journals/corr/corr1411.html#MirzaO14
