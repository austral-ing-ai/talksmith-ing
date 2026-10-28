---
source_file: pix2pix-isola-2017
source_type: web-capture
ingested_at: 2026-08-14
---

# Image-to-Image Translation with Conditional Adversarial Networks — pix2pix (arXiv:1611.07004) — página de abstract

## Provenance
- Original location: `research/web/pix2pix-isola-2017/`
- Format: web-capture (arXiv `abs` page; `page.md` + `original.html` + `assets/`)
- URL: https://arxiv.org/abs/1611.07004
- Author / source (if known): Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, Alexei A. Efros (UC Berkeley, BAIR)
- Date of original (if known): enviado 21 nov 2016; última revisión 26 nov 2018 (v3). CVPR 2017.
- Fetched at: 2026-08-14T17:03:10Z (HTTP 200, 42.344 bytes)
- **Rol en la Clase 9 — encuadre importante:** igual que StyleGAN, esta fuente **no es tema central**. Entra como parte del **"antes"** contra el que la clase contrasta la difusión (slides 26, 27, 31): la generación condicional *antes* de que el condicionamiento fuera texto libre. Registrar con ese rol.

## Key claims

- **Autores:** Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, Alexei A. Efros. **Año:** 2016 (v1) / 2018 (v3). **Venue:** **CVPR 2017** (declarado en el campo `Comments`). **arXiv ID:** arXiv:1611.07004 [cs.CV]. **DOI:** 10.48550/arXiv.1611.07004.
- Investigan las **redes adversarias condicionales** como **solución de propósito general** al problema de traducción imagen-a-imagen.
- **La idea clave:** estas redes no sólo aprenden **el mapeo** de imagen de entrada a imagen de salida — **aprenden también la función de pérdida** con que se entrena ese mapeo.
- **Consecuencia:** el mismo enfoque genérico se puede aplicar a problemas que tradicionalmente habrían requerido **formulaciones de pérdida muy distintas**.
- Demostrado en: **sintetizar fotos a partir de mapas de etiquetas**, **reconstruir objetos a partir de mapas de bordes**, y **colorizar imágenes**, entre otras tareas.
- Evidencia de adopción: desde la publicación del software pix2pix, **muchísimos usuarios de internet (varios de ellos artistas) publicaron sus propios experimentos**, mostrando amplia aplicabilidad y facilidad de adopción **sin ajuste de parámetros**.
- **Cierre programático:** "As a community, we no longer hand-engineer our mapping functions, and this work suggests we can achieve reasonable results without hand-engineering our loss functions either."

## Definitions and terminology

- **Traducción imagen-a-imagen (*image-to-image translation*).** La familia de problemas: dada una imagen de entrada, producir una imagen de salida correspondiente. Bordes → objeto, etiquetas → foto, gris → color.
- **Red adversaria condicional (cGAN).** El método. **El abstract no define el mecanismo adversarial** — no menciona discriminador, ni el juego entre generador y discriminador. Otra vez, como en StyleGAN, la definición de GAN falta en el corpus.
- **Aprender la función de pérdida.** "These networks not only learn the mapping from input image to output image, but also learn a loss function to train this mapping." Es la contribución conceptual del paper y la frase más citable: en lugar de diseñar a mano un criterio de "esta salida está bien", el discriminador lo aprende.
- **Condicionamiento por imagen.** Distinción central para el contraste del deck: en pix2pix, **el condicionamiento es una imagen** (un mapa de bordes, un mapa de etiquetas). En Stable Diffusion, **el condicionamiento es texto**, inyectado por cross-attention. Los dos son generación condicional; cambia radicalmente la interfaz y quién puede usarla.

### Contraste con difusión — el punto que le interesa a la clase

- **pix2pix necesita pares alineados.** Para entrenar hace falta un corpus de entrada-salida emparejado píxel a píxel (el mapa de bordes *y* la foto correspondiente). Eso limita el método a dominios donde ese corpus existe o se puede fabricar. La difusión con texto se entrena sobre pares imagen-caption sueltos de la web (ver `laion-5b-schuhmann-2022.web.md`), que son órdenes de magnitud más fáciles de conseguir.
- **Un modelo por tarea.** pix2pix es "propósito general" en el sentido de que la *misma receta* sirve para muchas tareas, pero cada tarea necesita su propio entrenamiento. Un modelo de difusión condicionado por texto cubre muchas tareas con un solo conjunto de pesos.
- **La interfaz.** Para usar pix2pix hay que dibujar un mapa de bordes o de etiquetas. Para usar Stable Diffusion hay que escribir una frase. Ese cambio de interfaz explica buena parte de la masificación, y es probablemente el punto más claro que la slide 26/27/31 puede hacer con esta fuente.
- **Lo que pix2pix anticipa:** la idea de "condicionar la generación" es la misma; el paper de difusión latente la generaliza cuando dice "general conditioning inputs such as text or bounding boxes". pix2pix es el escalón anterior de esa escalera, no un callejón sin salida.

## Evidence and examples

- **El abstract no contiene un solo número.** Ni métricas, ni tamaños de dataset, ni resoluciones, ni conteo de usuarios.
- Tareas demostradas: **foto desde mapa de etiquetas**, **objeto desde mapa de bordes**, **colorización**.
- Evidencia de adopción declarada de forma **anecdótica**: "a large number of internet users (many of them artists) have posted their own experiments with our system". Sin cifras.
- Afirmación de usabilidad: resultados razonables **sin ajuste de parámetros** ("without the need for parameter tweaking").
- Sitio del proyecto: `https://phillipi.github.io/pix2pix/`.
- Tres versiones entre nov 2016 y nov 2018 — el paper se siguió actualizando dos años después de CVPR 2017.

### Verificación de cifras del deck

El deck no cita cifras de pix2pix entre las que este encargo pide verificar, y esta fuente no ofrece ninguna. Todo número sobre pix2pix que aparezca en el deck viene de otro lado.

## Inconsistencies / open questions

1. **La página capturada trae solo el abstract.** Lo que la clase necesitaría y no está:
   - **Las figuras de resultados** — las tiras de "entrada → salida" (bordes → cartera, mapa → foto aérea, blanco y negro → color) que son lo único que comunica de verdad qué hace pix2pix. Sin ellas, el paper no se puede mostrar, sólo contar.
   - El diagrama de la arquitectura: **generador U-Net** y **discriminador PatchGAN**. Detalle notable para esta clase en particular: **pix2pix usa U-Net como generador**, la misma arquitectura del bloque de segmentación (ver `unet-ronneberger-2015.web.md`). Es un puente elegante entre las dos mitades del deck, y el abstract no lo menciona.
   - Los **datasets** usados (Cityscapes, fachadas CMP, mapas, edges2shoes).
   - Las **métricas de evaluación** (AMT perceptual studies, FCN-score).
2. **Ninguna definición de GAN en todo el corpus.** Igual que en `stylegan-karras-2019.web.md`: si el deck contrasta GANs con difusión, el mecanismo adversarial no está explicado en ninguna fuente disponible.
3. **La evidencia de adopción es anecdótica.** "A large number of internet users" no es una medición. Es un argumento de popularidad en un abstract académico, y conviene citarlo como tal.
4. **La frase de cierre es una declaración programática, no un resultado.** "As a community, we no longer hand-engineer our mapping functions, and this work suggests we can achieve reasonable results without hand-engineering our loss functions either." Es retórica —buena, y muy citable como cierre de la slide de contraste— pero no está demostrada por ningún experimento del abstract.
5. **Requisito de pares alineados no declarado.** El abstract vende el método como "general-purpose solution" sin mencionar su restricción más fuerte: hace falta un dataset emparejado. Es justamente la limitación que motivó a los mismos autores a publicar CycleGAN un año después. Un público desprevenido sale del abstract con una idea inflada del alcance.
6. **Fecha ambigua.** El preprint es de 2016, la conferencia de 2017, la última revisión de 2018. La convención "pix2pix (2017)" que usa el deck refiere a CVPR y es la correcta, pero conviene ser consistente si el deck ordena cronológicamente.

## Images / diagrams

La captura de una página `abs` de arXiv **no incluye ninguna figura del paper** — no trae ninguno de los ejemplos de traducción. Los tres archivos guardados son cromo del sitio, copiados a la carpeta compañera por completitud.

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

> We investigate conditional adversarial networks as a general-purpose solution to image-to-image translation problems. These networks not only learn the mapping from input image to output image, but also learn a loss function to train this mapping. This makes it possible to apply the same generic approach to problems that traditionally would require very different loss formulations. We demonstrate that this approach is effective at synthesizing photos from label maps, reconstructing objects from edge maps, and colorizing images, among other tasks. Indeed, since the release of the pix2pix software associated with this paper, a large number of internet users (many of them artists) have posted their own experiments with our system, further demonstrating its wide applicability and ease of adoption without the need for parameter tweaking. As a community, we no longer hand-engineer our mapping functions, and this work suggests we can achieve reasonable results without hand-engineering our loss functions either.

**Metadatos de la página, verbatim:**

> Computer Science > Computer Vision and Pattern Recognition
> arXiv:1611.07004 (cs)
> [Submitted on 21 Nov 2016 (v1), last revised 26 Nov 2018 (this version, v3)]
> Title: Image-to-Image Translation with Conditional Adversarial Networks
> Authors: Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, Alexei A. Efros
> Comments: Website: https://phillipi.github.io/pix2pix/, CVPR 2017
> Subjects: Computer Vision and Pattern Recognition (cs.CV)
> Cite as: arXiv:1611.07004 [cs.CV]
> https://doi.org/10.48550/arXiv.1611.07004
