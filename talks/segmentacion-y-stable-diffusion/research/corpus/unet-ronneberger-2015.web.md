---
source_file: unet-ronneberger-2015
source_type: web-capture
ingested_at: 2026-08-14
---

# U-Net: Convolutional Networks for Biomedical Image Segmentation (arXiv:1505.04597) — página de abstract

## Provenance
- Original location: `research/web/unet-ronneberger-2015/`
- Format: web-capture (arXiv `abs` page; `page.md` + `original.html` + `assets/`)
- URL: https://arxiv.org/abs/1505.04597
- Author / source (if known): Olaf Ronneberger, Philipp Fischer, Thomas Brox (Universidad de Friburgo)
- Date of original (if known): 18 may 2015 (v1, única versión). Aceptado condicionalmente en MICCAI 2015.
- Fetched at: 2026-08-14T17:03:10Z (HTTP 200, 41.947 bytes)
- Rol en la Clase 9: la arquitectura de segmentación que nació en imágenes biomédicas — la fuente más alineada con el público del curso (biomedicina).

## Key claims

- **Autores:** Olaf Ronneberger, Philipp Fischer, Thomas Brox. **Año:** 2015. **Venue:** MICCAI 2015 (aceptado condicionalmente al momento del preprint). **arXiv ID:** arXiv:1505.04597 [cs.CV]. **DOI:** 10.48550/arXiv.1505.04597.
- Contra el consenso de que entrenar redes profundas exige "many thousand annotated training samples", el paper presenta una red y una **estrategia de entrenamiento apoyada fuertemente en data augmentation** para exprimir las pocas muestras anotadas disponibles. Este es el argumento que hace a U-Net relevante para biomedicina: los datos anotados son caros y escasos.
- **Arquitectura de dos ramas:** un *contracting path* que captura contexto y un *expanding path* simétrico que permite localización precisa. Es la definición de encoder-decoder que la clase reutiliza.
- La red se entrena **end-to-end desde muy pocas imágenes** y supera al método previo (una red convolucional de ventana deslizante) en el desafío ISBI de segmentación de estructuras neuronales en pilas de microscopía electrónica.
- Con la misma red entrenada sobre microscopía de luz transmitida (contraste de fase y DIC), **ganaron el ISBI cell tracking challenge 2015 por amplio margen** en esas categorías.
- **Velocidad:** segmentar una imagen de 512×512 toma **menos de un segundo** en una GPU reciente (2015).
- Implementación (sobre Caffe) y redes entrenadas disponibles públicamente.

## Definitions and terminology

- **Encoder-decoder (contracting / expanding path).** "The architecture consists of a contracting path to capture context and a symmetric expanding path that enables precise localization." Los dos términos del abstract son literalmente el encoder y el decoder que la clase enseña: el contracting path comprime y gana contexto semántico; el expanding path recupera resolución y precisión de localización. La palabra "simétrico" es la que justifica la forma de U del nombre.
- **Skip connections.** **Ausente del abstract.** El abstract nombra la simetría de los dos caminos pero **no menciona las conexiones de salto** que copian los mapas de features del encoder al decoder al mismo nivel de resolución — que es el mecanismo por el que el expanding path logra la "precise localization". Si la clase enseña U-Net por sus skip connections (y lo hace), esa parte no está respaldada por la página capturada: vive en la figura 1 del paper, que la captura no trae.
- **Data augmentation.** "Relies on the strong use of data augmentation to use the available annotated samples more efficiently." Aumentación como sustituto de volumen de datos anotados.
- **Segmentación biomédica.** El dominio del paper: estructuras neuronales en microscopía electrónica, células en microscopía de luz transmitida (contraste de fase, DIC).

## Evidence and examples

- **ISBI challenge** — segmentación de estructuras neuronales en pilas de microscopía electrónica: supera al mejor método previo (red convolucional de ventana deslizante). **Sin número en el abstract.**
- **ISBI cell tracking challenge 2015** — ganado "by a large margin" en las categorías de contraste de fase y DIC. **Sin número en el abstract.**
- **512×512 en menos de un segundo** en GPU de 2015. Es el único número duro del abstract, y es de velocidad, no de calidad.
- Código y pesos: `http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net`.
- Envío único: v1, 18 may 2015, 1.385 KB.

### Verificación de cifras del deck

El deck no cita cifras de U-Net. La observación relevante corre al revés y está en el punto 2 de la sección siguiente.

## Inconsistencies / open questions

1. **La página capturada trae solo el abstract.** Falta todo lo que la clase efectivamente muestra de U-Net:
   - **La figura 1 — el diagrama en U.** Es *la* imagen de este paper: los bloques del contracting path, el cuello, el expanding path y las flechas grises horizontales de las skip connections con las dimensiones de cada mapa de features (572×572 → 32×32 → 388×388). Sin ella, la captura no permite explicar la arquitectura visualmente.
   - La descripción de las **skip connections** (copia y recorte de los mapas del encoder hacia el decoder).
   - La **función de pérdida ponderada por bordes** que separa células pegadas — una de las contribuciones más citadas del paper.
   - Las tablas de resultados del ISBI con sus métricas (warping error, rand error, IoU).
   Todo eso está en el PDF (`https://arxiv.org/pdf/1505.04597`), no capturado.
2. **Métrica de evaluación — el hueco del deck.** El deck enseña 22 slides de segmentación sin definir Dice ni IoU. Sobre esta fuente hay que ser preciso: **el abstract de U-Net no reporta ninguna métrica numérica de calidad**. Dice "outperforms the prior best method" y "won ... by a large margin", que son afirmaciones de ranking, no mediciones. Los números de IoU / warping error del ISBI están en el cuerpo del paper, fuera de la captura. La fuente del conjunto que **sí** publica una métrica de segmentación con número en la página capturada es FCN (**62,2% mean IU**, ver `fcn-long-2015.web.md`); y el post de Meta trae una figura con cinco métricas nombradas y cuantificadas (cgF1, pHOTA, J&F, mIoU, gIoU — ver `sam31-meta-2026.web.md`). Para poner Dice en el deck —la métrica estándar en segmentación médica, y la que este público esperaría— hace falta una fuente que hoy no está en el corpus.
3. **Afirmación no cuantificada:** "requires many thousand annotated training samples" se presenta como consenso del campo sin cita ni cifra. Es retórica de introducción, no un dato.
4. **Deriva temporal del hardware:** "less than a second on a recent GPU" refiere a una GPU de 2015. Citar ese número hoy sin contexto sugiere una comparación de velocidad que ya no tiene sentido.

## Images / diagrams

La captura de una página `abs` de arXiv **no incluye ninguna figura del paper** — en particular, no trae el diagrama en U. Los tres archivos de imagen guardados son cromo del sitio, copiados a la carpeta compañera por completitud.

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

> There is large consent that successful training of deep networks requires many thousand annotated training samples. In this paper, we present a network and training strategy that relies on the strong use of data augmentation to use the available annotated samples more efficiently. The architecture consists of a contracting path to capture context and a symmetric expanding path that enables precise localization. We show that such a network can be trained end-to-end from very few images and outperforms the prior best method (a sliding-window convolutional network) on the ISBI challenge for segmentation of neuronal structures in electron microscopic stacks. Using the same network trained on transmitted light microscopy images (phase contrast and DIC) we won the ISBI cell tracking challenge 2015 in these categories by a large margin. Moreover, the network is fast. Segmentation of a 512x512 image takes less than a second on a recent GPU. The full implementation (based on Caffe) and the trained networks are available at http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net .

**Metadatos de la página, verbatim:**

> Computer Science > Computer Vision and Pattern Recognition
> arXiv:1505.04597 (cs)
> [Submitted on 18 May 2015]
> Title: U-Net: Convolutional Networks for Biomedical Image Segmentation
> Authors: Olaf Ronneberger, Philipp Fischer, Thomas Brox
> Comments: conditionally accepted at MICCAI 2015
> Subjects: Computer Vision and Pattern Recognition (cs.CV)
> Cite as: arXiv:1505.04597 [cs.CV]
> https://doi.org/10.48550/arXiv.1505.04597

**Historial de envíos:**

> From: Olaf Ronneberger
> [v1] Mon, 18 May 2015 11:28:37 UTC (1,385 KB)
