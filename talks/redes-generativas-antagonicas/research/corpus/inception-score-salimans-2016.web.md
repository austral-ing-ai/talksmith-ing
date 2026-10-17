---
source_file: inception-score-salimans-2016
source_type: web-capture
ingested_at: 2026-08-14
---

# Improved Techniques for Training GANs — el paper del Inception Score (Salimans et al., 2016) — página abstract de arXiv

## Provenance
- Original location: `research/web/inception-score-salimans-2016/`
- Format: html (captura web de `talksmith:ingest` — `page.md` + `original.html` + `assets/`)
- Author / source (if known): Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, Xi Chen — OpenAI (afiliación no visible en la captura) — arXiv
- Date of original (if known): enviado el 10 de junio de 2016 (v1, única versión). Captura: 2026-08-14T17:02:59Z, HTTP 200, URL `https://arxiv.org/abs/1606.03498`

## Key claims

- **Igual que con FID: el título no dice "Inception Score".** El paper es un compendio de técnicas para entrenar GANs; el Inception Score aparece dentro como la métrica que proponen para evaluar el realismo de las muestras. **El abstract ni siquiera lo nombra.** Ver *Inconsistencies*.
- **Presentan un conjunto de características arquitectónicas y procedimientos de entrenamiento nuevos** aplicados al marco GAN. (En el paper: *feature matching*, *minibatch discrimination*, *historical averaging*, *one-sided label smoothing*, *virtual batch normalization*. **Ninguno de esos nombres está en la captura.**)
- **Dos aplicaciones en foco**: aprendizaje semi-supervisado, y generación de imágenes que los humanos encuentren visualmente realistas.
- **Declaración de objetivo poco habitual y muy citable**: *"Unlike most work on generative models, our primary goal is not to train a model that assigns high likelihood to test data, nor do we require the model to be able to learn well without using any labels."* Es decir, renuncian explícitamente a la verosimilitud como criterio de éxito — el mismo movimiento conceptual que hace SRGAN al abandonar el MSE.
- **Estado del arte en clasificación semi-supervisada en MNIST, CIFAR-10 y SVHN.**
- **Validación con humanos**: la calidad de las imágenes generadas se confirma con un **test de Turing visual**. El modelo genera muestras de MNIST que **los humanos no pueden distinguir de datos reales**, y muestras de CIFAR-10 que producen una **tasa de error humana del 21,3 %**.
- **Presentan muestras de ImageNet con resolución sin precedentes** y muestran que sus métodos permiten aprender características reconocibles de las clases de ImageNet.

Datos bibliográficos para la cita:
- Autores: Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, Xi Chen
- Año: 2016
- arXiv ID: **arXiv:1606.03498 [cs.LG]** (v1)
- DOI: `https://doi.org/10.48550/arXiv.1606.03498`
- Materias: Machine Learning (cs.LG); Computer Vision and Pattern Recognition (cs.CV); Neural and Evolutionary Computing (cs.NE)
- Venue: la página **no** declara *journal reference* ni Comments. El paper se presentó en NIPS 2016, pero **eso no está en esta captura**.
- Nota de continuidad para el linaje: **Goodfellow firma este paper y el fundacional; Radford firma este y DCGAN.** Es literalmente el mismo grupo de gente dos años después.

## Definitions and terminology

**Qué mide exactamente el Inception Score** — junto con `fid-heusel-2017.web.md`, esto es lo que la slide 50 necesita:

- **Inception Score (IS)**: **el término no aparece en esta captura.** El abstract habla de "imágenes que los humanos encuentran visualmente realistas" y de un test de Turing visual, pero no nombra la métrica. La definición formal está en la Sección 4 del paper.
- **Lo que sí se puede afirmar desde acá, y que es la diferencia clave con FID**: el IS **se calcula únicamente sobre las muestras generadas**, pasándolas por una red Inception preentrenada. No mira el conjunto de datos reales en ningún momento. FID sí (ver `fid-heusel-2017.web.md`). De ahí que un generador pueda tener buen IS produciendo imágenes nítidas y variadas que **no se parecen a los datos de entrenamiento** — y el IS no lo detecta. Esa es la crítica que motiva FID un año después, y está enunciada en el abstract de Heusel et al.: FID *"captures the similarity of generated images to real ones better than the Inception Score"*.
- **Las dos cosas que el IS combina** (que las imágenes sean clasificables con confianza — calidad — y que las clases predichas estén repartidas — diversidad) **no están en esta captura**. Es la lectura estándar de la métrica, pero hay que citarla del paper.
- **Test de Turing visual (visual Turing test)**: evaluación en la que jueces humanos intentan distinguir muestras generadas de datos reales. Definido por su uso, no por su procedimiento. Es la contraparte humana de las métricas automáticas.
- **Tasa de error humana (human error rate)**: la fracción de veces que el juez humano se equivoca. **21,3 % en CIFAR-10.** Un 50 % sería indistinguible; 21,3 % significa que los humanos todavía acertaban bastante.
- **Aprendizaje semi-supervisado (semi-supervised learning)**: entrenar con pocas etiquetas y muchos datos sin etiquetar. Es la mitad del paper que la clase suele ignorar.
- **Mode collapse (colapso de modos)**: **el término no aparece en esta captura.** Es el problema que ataca la *minibatch discrimination* de este paper, y el concepto que la clase reutiliza. Ninguna de las 14 fuentes de `research/web/` lo define explícitamente. Lo más cercano que ofrece el corpus es la "competencia insana entre generador y discriminador" (*unhealthy competition*) de `progan-progressive-growing-karras-2018.web.md` y el énfasis de ProGAN en la **variación** de las muestras — que es la propiedad que el colapso de modos destruye. Si el deck define mode collapse, la definición no sale de este corpus.

## Evidence and examples

Este registro y `progan-…` son los dos con números concretos y citables:

- **Tasa de error humana del 21,3 % en muestras de CIFAR-10** — el número más citable del registro y el único estudio con jueces humanos, junto con el MOS de SRGAN, en todo el corpus.
- **Muestras de MNIST que los humanos no pueden distinguir de datos reales** — afirmación cualitativa fuerte, sin porcentaje.
- **Estado del arte en clasificación semi-supervisada en MNIST, CIFAR-10 y SVHN.**
- **Muestras de ImageNet "con resolución sin precedentes"** (para 2016) y aprendizaje de características reconocibles de las clases.
- **Datasets nombrados — cuatro: MNIST, CIFAR-10, SVHN, ImageNet.**
- Peso de la subida: 5.720 KB.

## Inconsistencies / open questions

- **[Punto 5 del encargo] Este es el registro más cercano a la afirmación de la slide 43** ("los neurorradiólogos no distinguen en estudios ciegos"), y sirve para mostrar exactamente qué le falta a esa afirmación. Salimans et al. **sí hicieron** un estudio ciego con humanos y reportan un número concreto: **21,3 % de tasa de error en CIFAR-10**, con la aclaración de que en MNIST los jueces no distinguían. La slide 43 afirma algo estructuralmente parecido pero **sobre neurorradiólogos e imágenes médicas, sin cita, sin número, sin tamaño de muestra y sin protocolo**. Ninguna de las 14 fuentes de este corpus respalda esa afirmación — ni esta, que es la que más se le parece, ni `srgan-ledig-2017.web.md` con su test MOS (fotografías naturales, sin médicos). Si la clase la conserva, necesita fuente propia; si no la consigue, el número de Salimans et al. es un sustituto honesto y verificable, con el cambio de dominio explicitado.
- **[Punto 4 del encargo] Cuatro datasets nombrados: MNIST, CIFAR-10, SVHN, ImageNet.** Se registra porque el deck argumenta sobre datasets en cuatro slides sin nombrar ninguno.
- **El paper se cita por una métrica que su abstract no nombra.** Igual que Heusel et al. con FID, pero peor: acá el término "Inception Score" **no aparece en toda la captura**. Este registro **no alcanza** para definir el IS; sirve para atribuirlo, fecharlo y ubicarlo. La definición hay que sacarla del PDF, Sección 4.
- **Las cinco técnicas de entrenamiento que dan título al paper no están nombradas en la captura.** Si el deck habla de *feature matching* o *minibatch discrimination*, no salen de acá.
- **Mode collapse no está definido en ninguna fuente del corpus** (ver *Definitions*). Es un hueco real para la clase, no solo para este registro.
- **Sin venue impreso**: NIPS 2016 no figura en la página.
- **Riesgo interpretativo del 21,3 %**: es la tasa de error **de los humanos al juzgar**, no una métrica de calidad del modelo. Un 50 % sería el techo (indistinguible). Presentar el 21,3 % como "los humanos se equivocaron una de cada cinco veces" es correcto; presentarlo como "el modelo es 78,7 % realista" no lo es.

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

Abstract completo, verbatim (inglés original). **La oración del visual Turing test y el 21,3 % es la cita para contrastar con la slide 43:**

> Abstract: We present a variety of new architectural features and training procedures that we apply to the generative adversarial networks (GANs) framework. We focus on two applications of GANs: semi-supervised learning, and the generation of images that humans find visually realistic. Unlike most work on generative models, our primary goal is not to train a model that assigns high likelihood to test data, nor do we require the model to be able to learn well without using any labels. Using our new techniques, we achieve state-of-the-art results in semi-supervised classification on MNIST, CIFAR-10 and SVHN. The generated images are of high quality as confirmed by a visual Turing test: our model generates MNIST samples that humans cannot distinguish from real data, and CIFAR-10 samples that yield a human error rate of 21.3%. We also present ImageNet samples with unprecedented resolution and show that our methods enable the model to learn recognizable features of ImageNet classes.

Bloque bibliográfico verbatim:

> Computer Science > Machine Learning
> **arXiv:1606.03498** (cs) [Submitted on 10 Jun 2016]
> Title: Improved Techniques for Training GANs
> Authors: Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, Xi Chen
> Subjects: Machine Learning (cs.LG); Computer Vision and Pattern Recognition (cs.CV); Neural and Evolutionary Computing (cs.NE)
> Cite as: arXiv:1606.03498 [cs.LG] (or arXiv:1606.03498v1 [cs.LG] for this version)
> https://doi.org/10.48550/arXiv.1606.03498

> Submission history
> From: Ian Goodfellow
> **[v1]** Fri, 10 Jun 2016 22:53:35 UTC (5,720 KB)
