---
source_file: progan-progressive-growing-karras-2018
source_type: web-capture
ingested_at: 2026-08-14
---

# Progressive Growing of GANs for Improved Quality, Stability, and Variation — ProGAN (Karras et al., 2018) — página abstract de arXiv

## Provenance
- Original location: `research/web/progan-progressive-growing-karras-2018/`
- Format: html (captura web de `talksmith:ingest` — `page.md` + `original.html` + `assets/`)
- Author / source (if known): Tero Karras, Timo Aila, Samuli Laine, Jaakko Lehtinen — NVIDIA (la afiliación no figura en la captura) — arXiv
- Date of original (if known): enviado el 27 de octubre de 2017 (v1), última revisión 26 de febrero de 2018 (v3, la capturada), marcada "Final ICLR 2018 version". Captura: 2026-08-14T17:02:50Z, HTTP 200, URL `https://arxiv.org/abs/1710.10196`

## Key claims

- **Este es el paper del crecimiento progresivo. No StyleGAN.** El abstract abre: *"We describe a new training methodology for generative adversarial networks. The key idea is to grow both the generator and discriminator progressively: starting from a low resolution, we add new layers that model increasingly fine details as training progresses."*
- **El crecimiento progresivo es una metodología de entrenamiento, no una arquitectura.** El abstract lo dice literalmente ("a new training methodology"). Distinción que vale para la clase: no se cambia el modelo, se cambia el cronograma con el que se lo entrena.
- **Doble beneficio declarado: acelera el entrenamiento y lo estabiliza mucho** (*"This both speeds the training up and greatly stabilizes it"*), lo que permite producir imágenes de calidad sin precedentes.
- **Resultado insignia: imágenes de CelebA a 1024²** (1024×1024 píxeles). Es el número que cambió la percepción pública de lo que las GANs podían hacer con caras.
- **Proponen una forma simple de aumentar la variación de las imágenes generadas** y alcanzan un **inception score récord de 8.80 en CIFAR-10 no supervisado.**
- **Describen varios detalles de implementación importantes para desincentivar la "competencia insana" entre generador y discriminador** (*unhealthy competition*). Este es el vocabulario del propio paper para el problema de inestabilidad del entrenamiento adversarial.
- **Sugieren una métrica nueva para evaluar resultados de GANs**, tanto en calidad de imagen como en variación.
- **Contribución adicional: construyen una versión de mayor calidad del dataset CelebA** (CelebA-HQ; el nombre "CelebA-HQ" **no** aparece en la captura, sí "a higher-quality version of the CelebA dataset").

Datos bibliográficos para la cita:
- Autores: Tero Karras, Timo Aila, Samuli Laine, Jaakko Lehtinen
- Año: 2017 (arXiv v1) / **2018 (ICLR)**
- arXiv ID: **arXiv:1710.10196 [cs.NE]** (v3)
- DOI: `https://doi.org/10.48550/arXiv.1710.10196`
- Materias: Neural and Evolutionary Computing (cs.NE); Machine Learning (cs.LG); Machine Learning (stat.ML)
- Venue: Comments dice **"Final ICLR 2018 version"** — **ICLR 2018**.

## Definitions and terminology

- **Progressive growing (crecimiento progresivo)**: metodología de entrenamiento en la que generador y discriminador crecen en paralelo — se arranca en baja resolución y se **agregan capas nuevas** que modelan detalles cada vez más finos a medida que avanza el entrenamiento. Definición verbatim del abstract, y la única definición primaria de este término en todo el corpus.
- **Competencia insana entre generador y discriminador (unhealthy competition)**: el término del paper para la dinámica adversarial que descarrila el entrenamiento. Emparenta con **mode collapse** pero no es lo mismo, y el abstract **no usa la expresión "mode collapse"** — en este corpus, la fuente que ataca el colapso de modos de frente es `inception-score-salimans-2016.web.md` (minibatch discrimination).
- **Variación (variation)**: en el vocabulario de este paper, la diversidad de las muestras generadas. Aparece en el título, y es la cara opuesta del colapso de modos.
- **Inception score**: usado acá como métrica de referencia, con un valor concreto. Su definición primaria está en `inception-score-salimans-2016.web.md`.
- **CelebA-HQ**: la versión de mayor calidad de CelebA que construyen. Nombrada en la captura solo como "a higher-quality version of the CelebA dataset".

## Evidence and examples

Este es, junto con `fid-heusel-2017`, el registro más rico en números concretos del corpus:

- **CelebA a 1024² (1024×1024 px)** — resolución de las imágenes generadas.
- **Inception score de 8.80 en CIFAR-10 no supervisado**, presentado como récord al momento de publicación.
- **Datasets nombrados: CelebA y CIFAR-10.** Explícitos en el abstract.
- Contribución de dataset: una versión de mayor calidad de CelebA.
- Peso de la subida: 29.114 KB (v1) → 27.891 KB (v3). Paper muy cargado de figuras; ninguna en la captura.

## Inconsistencies / open questions

- **[Punto 2 del encargo] Error de atribución del deck: el *progressive growing* NO es de StyleGAN.** El deck se lo atribuye a StyleGAN (slides 40-43). La fuente correcta es **este** paper: Karras, Aila, Laine & Lehtinen, *Progressive Growing of GANs for Improved Quality, Stability, and Variation*, **arXiv:1710.10196, ICLR 2018**. La prueba está en la primera línea del abstract, preservada verbatim más abajo: *"We describe a new training methodology... The key idea is to grow both the generator and discriminator progressively."*
  Detalles que hacen el error comprensible y que conviene tener a mano si alguien pregunta en clase:
  - **Mismo primer autor** (Tero Karras) y equipo casi idéntico (Laine y Aila están en los dos; Lehtinen solo en ProGAN).
  - **StyleGAN sí usa progressive growing**: su generador se construye sobre el de ProGAN. Por eso la frase "StyleGAN entrena con crecimiento progresivo" es correcta y la frase "StyleGAN introdujo el crecimiento progresivo" es falsa. La corrección es de atribución, no de contenido técnico.
  - **Cronología**: ProGAN es de octubre 2017 (arXiv) / ICLR 2018; StyleGAN es de diciembre 2018 (arXiv) / CVPR 2019. Un año largo de diferencia.
  - Corolario para la tabla de la slide 39: si ProGAN no está en la tabla, el deck no solo atribuye mal una técnica — le falta una fila del linaje.
- **[Punto 4 del encargo] Datasets nombrados: CelebA y CIFAR-10.** Se registra explícitamente porque el deck argumenta sobre datasets en cuatro slides sin nombrar ninguno. Este registro es el mejor contraejemplo disponible: la fuente primaria no solo nombra sus datasets, **construye uno** y lo declara como contribución. Es exactamente el nivel de especificidad que le falta al deck.
- **Año en la tabla de linaje**: arXiv 2017, ICLR 2018. El nombre de la carpeta (`…-karras-2018`) usa el año de publicación. Si la tabla del deck usa año de arXiv para otras filas, hay una inconsistencia de criterio (ver `stylegan-karras-2019.web.md`).
- **Gap de extracción**: la captura no trae la Figura 1 (el esquema del crecimiento por etapas, 4×4 → 1024×1024), que es la figura que explica el paper de un vistazo y la que la clase debería proyectar. Está en el PDF.
- **La "métrica nueva" propuesta no está nombrada** en la captura (es la *sliced Wasserstein distance* sobre pirámides laplacianas, según el paper). Si el deck habla de métricas (slide 50), esta es una tercera métrica del mismo período que ni FID ni IS cubren.

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

Abstract completo, verbatim (inglés original). **Las dos primeras oraciones son la prueba documental de la atribución correcta del progressive growing:**

> Abstract: We describe a new training methodology for generative adversarial networks. The key idea is to grow both the generator and discriminator progressively: starting from a low resolution, we add new layers that model increasingly fine details as training progresses. This both speeds the training up and greatly stabilizes it, allowing us to produce images of unprecedented quality, e.g., CelebA images at 1024^2. We also propose a simple way to increase the variation in generated images, and achieve a record inception score of 8.80 in unsupervised CIFAR10. Additionally, we describe several implementation details that are important for discouraging unhealthy competition between the generator and discriminator. Finally, we suggest a new metric for evaluating GAN results, both in terms of image quality and variation. As an additional contribution, we construct a higher-quality version of the CelebA dataset.

Bloque bibliográfico verbatim:

> Computer Science > Neural and Evolutionary Computing
> **arXiv:1710.10196** (cs) [Submitted on 27 Oct 2017 (v1), last revised 26 Feb 2018 (this version, v3)]
> Title: Progressive Growing of GANs for Improved Quality, Stability, and Variation
> Authors: Tero Karras, Timo Aila, Samuli Laine, Jaakko Lehtinen
> Comments: Final ICLR 2018 version
> Subjects: Neural and Evolutionary Computing (cs.NE); Machine Learning (cs.LG); Machine Learning (stat.ML)
> Cite as: arXiv:1710.10196 [cs.NE] (or arXiv:1710.10196v3 [cs.NE] for this version)
> https://doi.org/10.48550/arXiv.1710.10196

> Submission history
> From: Samuli Laine
> **[v1]** Fri, 27 Oct 2017 15:28:35 UTC (29,114 KB)
> **[v2]** Fri, 3 Nov 2017 14:39:27 UTC (29,114 KB)
> **[v3]** Mon, 26 Feb 2018 15:33:34 UTC (27,891 KB)
