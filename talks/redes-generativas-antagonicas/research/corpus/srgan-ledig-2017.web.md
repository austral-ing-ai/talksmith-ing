---
source_file: srgan-ledig-2017
source_type: web-capture
ingested_at: 2026-08-14
---

# Photo-Realistic Single Image Super-Resolution Using a GAN — SRGAN (Ledig et al., 2017) — página abstract de arXiv

## Provenance
- Original location: `research/web/srgan-ledig-2017/`
- Format: html (captura web de `talksmith:ingest` — `page.md` + `original.html` + `assets/`)
- Author / source (if known): Christian Ledig, Lucas Theis, Ferenc Huszar, Jose Caballero, Andrew Cunningham, Alejandro Acosta, Andrew Aitken, Alykhan Tejani, Johannes Totz, Zehan Wang, Wenzhe Shi (11 autores; equipo de Twitter/Magic Pony) — arXiv
- Date of original (if known): enviado el 15 de septiembre de 2016 (v1), última revisión 25 de mayo de 2017 (v5, la capturada). Captura: 2026-08-14T17:02:50Z, HTTP 200, URL `https://arxiv.org/abs/1609.04802`

## Key claims

- **El problema que atacan**: cómo recuperar el detalle fino de textura al super-resolver con factores de escala grandes. Lo plantean como "un problema central que sigue mayormente sin resolver" pese a los avances en precisión y velocidad.
- **El diagnóstico es sobre la función objetivo, no sobre la arquitectura.** "El comportamiento de los métodos de super-resolución basados en optimización está principalmente dirigido por la elección de la función objetivo." El trabajo previo minimizaba el error cuadrático medio de reconstrucción.
- **La crítica al MSE es la idea exportable a la clase**: las estimaciones que minimizan MSE tienen **alto PSNR pero carecen de detalles de alta frecuencia y son perceptualmente insatisfactorias** — fallan en igualar la fidelidad que uno espera de la resolución alta. Traducción para el aula: *una métrica de píxel puede subir mientras la imagen empeora a la vista*. Es el mismo argumento que después justifica FID e IS como métricas de distribución.
- **SRGAN es, según los autores, el primer marco capaz de inferir imágenes naturales foto-realistas para factores de ampliación 4×.**
- **Proponen una función de pérdida perceptual (perceptual loss) compuesta por una pérdida antagónica (adversarial loss) y una pérdida de contenido (content loss).** La adversarial empuja la solución hacia la variedad de imágenes naturales usando un discriminador entrenado para diferenciar imágenes super-resueltas de fotos reales; la de contenido está motivada por similitud perceptual **en lugar de similitud en el espacio de píxeles**.
- **La red es una red residual profunda** capaz de recuperar texturas foto-realistas de imágenes fuertemente submuestreadas en benchmarks públicos.
- **Validación con humanos**: un test extensivo de *mean opinion score* (MOS) muestra ganancias "enormemente significativas" en calidad perceptual. Los MOS de SRGAN están **más cerca de los de las imágenes originales de alta resolución que de los de cualquier método del estado del arte**.

Datos bibliográficos para la cita:
- Autores: 11 (Ledig et al.)
- Año: 2016 (arXiv v1) / 2017 (CVPR y v5)
- arXiv ID: **arXiv:1609.04802 [cs.CV]** (v5)
- DOI: `https://doi.org/10.48550/arXiv.1609.04802`
- Materias: Computer Vision and Pattern Recognition (cs.CV); Machine Learning (stat.ML)
- Venue: el campo Comments dice **"19 pages, 15 figures, 2 tables, accepted for oral presentation at CVPR"** — CVPR 2017, presentación oral. La captura no imprime el año del CVPR; se deduce de la fecha de la v5 (mayo 2017).

## Definitions and terminology

- **Pérdida perceptual (perceptual loss)**: en este paper, la suma de *adversarial loss* + *content loss*. La clase suele usar "pérdida perceptual" como sinónimo de "pérdida de contenido en el espacio de features"; el paper la define como el compuesto de las dos. Vale la precisión si el deck define el término.
- **Pérdida antagónica (adversarial loss)**: empuja la solución hacia la variedad (*manifold*) de imágenes naturales mediante el discriminador.
- **Pérdida de contenido (content loss)**: motivada por similitud perceptual en lugar de similitud en el espacio de píxeles. (En el paper es la distancia entre mapas de features de una VGG preentrenada; **el nombre "VGG loss" no aparece en esta captura**.)
- **Variedad de imágenes naturales (natural image manifold)**: el conjunto de imágenes que parecen fotos reales. Metáfora geométrica que el paper usa literalmente.
- **PSNR (peak signal-to-noise ratio)**: métrica de píxel que el paper usa como ejemplo de métrica que engaña. Nombrada en el abstract.
- **MOS (mean opinion score)**: puntaje promedio de opinión, evaluación **con jueces humanos**. Es la contra-métrica del paper y la única evaluación humana rigurosa que aparece en todo este corpus junto con el *visual Turing test* de `inception-score-salimans-2016.web.md`.
- **4× upscaling factor**: el factor de ampliación en el que reclaman la primicia.

## Evidence and examples

- **Factor 4×**: el número concreto y citable — "the first framework capable of inferring photo-realistic natural images for 4x upscaling factors".
- **Test MOS**: descrito como extensivo, con "hugely significant gains". La captura **no trae el valor numérico** del MOS ni el tamaño de la muestra de evaluadores; están en el paper (Tabla 2 según el campo Comments: 2 tablas).
- **Benchmarks públicos**: mencionados de forma genérica, **sin nombrar Set5, Set14 ni BSD100**. Ver *Inconsistencies*.
- Estructura del paper según Comments: 19 páginas, 15 figuras, 2 tablas.
- Historial de versiones largo (v1 sep-2016 → v5 may-2017), con salto de tamaño de 5.466 KB a 8.200 KB entre v2 y v3: el paper creció bastante en la revisión.

## Inconsistencies / open questions

- **Este es el registro que más se acerca a la afirmación del deck sobre evaluación humana** — slide 43: "los neurorradiólogos no distinguen en estudios ciegos". SRGAN sí hizo un estudio con humanos (MOS), pero **sobre fotografías naturales, no sobre imágenes médicas, y con radiólogos en ninguna parte**. Ninguna de las 14 fuentes de este corpus respalda la afirmación de la slide 43. El asiento principal de esa cifra queda en `inception-score-salimans-2016.web.md` (que sí midió una tasa de error humana concreta); acá se deja constancia de que SRGAN **no** es la fuente que la respalda, por más que sea el paper "con estudio perceptual" del linaje.
- **Datasets no nombrados**: "public benchmarks", sin más. Mismo silencio que el deck. No sirve para cerrar el hueco de datasets.
- **Gap de extracción**: sin números de MOS, sin PSNR/SSIM comparativos, sin las 15 figuras. La comparación visual SRResNet vs SRGAN vs bicúbica — que es lo que uno proyectaría en clase — hay que sacarla del PDF.
- **Año del venue no impreso**: la captura dice "accepted for oral presentation at CVPR" sin año. Es CVPR 2017; conviene verificarlo antes de ponerlo en la tabla del linaje.
- **Tensión conceptual que vale la pena marcar en clase**: el paper *baja* el PSNR a propósito para subir la calidad percibida. Si el deck presenta SRGAN como "mejor super-resolución" sin explicar ese trade-off, se pierde justamente lo que hace interesante al paper.

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

> Abstract: Despite the breakthroughs in accuracy and speed of single image super-resolution using faster and deeper convolutional neural networks, one central problem remains largely unsolved: how do we recover the finer texture details when we super-resolve at large upscaling factors? The behavior of optimization-based super-resolution methods is principally driven by the choice of the objective function. Recent work has largely focused on minimizing the mean squared reconstruction error. The resulting estimates have high peak signal-to-noise ratios, but they are often lacking high-frequency details and are perceptually unsatisfying in the sense that they fail to match the fidelity expected at the higher resolution. In this paper, we present SRGAN, a generative adversarial network (GAN) for image super-resolution (SR). To our knowledge, it is the first framework capable of inferring photo-realistic natural images for 4x upscaling factors. To achieve this, we propose a perceptual loss function which consists of an adversarial loss and a content loss. The adversarial loss pushes our solution to the natural image manifold using a discriminator network that is trained to differentiate between the super-resolved images and original photo-realistic images. In addition, we use a content loss motivated by perceptual similarity instead of similarity in pixel space. Our deep residual network is able to recover photo-realistic textures from heavily downsampled images on public benchmarks. An extensive mean-opinion-score (MOS) test shows hugely significant gains in perceptual quality using SRGAN. The MOS scores obtained with SRGAN are closer to those of the original high-resolution images than to those obtained with any state-of-the-art method.

Bloque bibliográfico verbatim:

> Computer Science > Computer Vision and Pattern Recognition
> **arXiv:1609.04802** (cs) [Submitted on 15 Sep 2016 (v1), last revised 25 May 2017 (this version, v5)]
> Title: Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network
> Authors: Christian Ledig, Lucas Theis, Ferenc Huszar, Jose Caballero, Andrew Cunningham, Alejandro Acosta, Andrew Aitken, Alykhan Tejani, Johannes Totz, Zehan Wang, Wenzhe Shi
> Comments: 19 pages, 15 figures, 2 tables, accepted for oral presentation at CVPR, main paper + some supplementary material
> Subjects: Computer Vision and Pattern Recognition (cs.CV); Machine Learning (stat.ML)
> Cite as: arXiv:1609.04802 [cs.CV] (or arXiv:1609.04802v5 [cs.CV] for this version)
> https://doi.org/10.48550/arXiv.1609.04802

> Submission history
> From: Christian Ledig
> **[v1]** Thu, 15 Sep 2016 19:53:07 UTC (5,466 KB)
> **[v2]** Mon, 19 Sep 2016 17:22:44 UTC (5,467 KB)
> **[v3]** Mon, 21 Nov 2016 18:30:18 UTC (8,200 KB)
> **[v4]** Thu, 13 Apr 2017 14:25:44 UTC (8,198 KB)
> **[v5]** Thu, 25 May 2017 11:25:41 UTC (8,200 KB)
