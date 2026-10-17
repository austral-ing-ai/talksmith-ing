---
source_file: serrano-gans-lab
source_type: web-capture
ingested_at: 2026-08-14
---

# Labs — Generative Adversarial Networks (Luis Serrano Academy) — el origen real del ejemplo "Slanted Land"

## Provenance
- Original location: `research/web/serrano-gans-lab/`
- Format: html (captura web de `talksmith:ingest` — `page.md` + `original.html` + `assets/`)
- Author / source (if known): **Luis Serrano** — Luis Serrano Academy (`serrano.academy`). Autor de *Grokking Machine Learning* (Manning) y del canal de YouTube `@SerranoAcademy`. Perfiles enlazados desde la página: LinkedIn `luisgserrano`, YouTube `@SerranoAcademy`, Twitter `@SerranoAcademy`.
- Date of original (if known): la página no lleva fecha. El notebook vive en `github.com/luisguiserrano/gans`. Captura: 2026-08-14T17:03:00Z, HTTP 200, URL `https://www.serrano.academy/deep-learning/gans-lab`

## Key claims

- **La página es la lección "Labs - Generative Adversarial Networks"**, dentro del Capítulo 2 ("Generative Neural Networks") del curso gratuito *Deep Learning and Neural Networks* de Luis Serrano.
- **Ofrece un laboratorio ejecutable: "Lab 1: Training a GAN from scratch".** Descripción verbatim: *"In this lab, you'll build a simple Generative Adversarial Network, and train it to generate faces of people in Slanted Land."*
- **El notebook es `GANs_in_Slanted_Land.ipynb`**, alojado en `github.com/luisguiserrano/gans` y enlazado para abrirse directamente en Google Colab:
  `https://colab.research.google.com/github/luisguiserrano/gans/blob/master/GANs_in_Slanted_Land.ipynb`
- **"Slanted Land" es el mundo didáctico de Serrano**, no un ejemplo genérico del campo: caras de 2×2 píxeles con una diagonal de luz, sobre las que se entrena una GAN mínima escrita a mano. La imagen `gans-better.jpg` de esta misma captura lo muestra (ver *Images*).
- **El material forma parte de un curso estructurado**, no de un video suelto. La estructura completa, extraída de `original.html`, está preservada en *Raw / preserved excerpts*: tres capítulos, catorce lecciones. La lección de GANs (`Generative Adversarial Networks (GANS)`) es la que precede a este laboratorio.

## Definitions and terminology

- **Slanted Land**: el mundo ficticio de Serrano donde "las caras" son imágenes de 2×2 píxeles con un patrón diagonal. La reducción extrema es deliberada: con 4 píxeles se puede seguir a mano la aritmética del generador y del discriminador, que es el objetivo pedagógico. **Es el ejemplo que la clase usa (slides 18 y 37).**
- **"Training a GAN from scratch"**: en el sentido de escribir generador y discriminador a mano, sin framework de deep learning. Ese es el punto del laboratorio.
- La página **no** define GAN, generador, discriminador ni espacio latente. Es la página del laboratorio, no la de la lección teórica (que es una entrada distinta del mismo capítulo, `Generative Adversarial Networks (GANS)`, **no capturada**).

## Evidence and examples

- **Recurso ejecutable y citable**: el notebook `GANs_in_Slanted_Land.ipynb`, abierto en Colab con un click. Es, junto con los repos de CycleGAN/pix2pix y AdaIN, uno de los pocos materiales del corpus que el alumno puede correr.
- **Repositorio de origen**: `github.com/luisguiserrano/gans`.
- **Contexto curricular** (de `original.html`): el laboratorio es la tercera de seis lecciones del Capítulo 2, entre "Generative Adversarial Networks (GANS)" y "Stable Diffusion".
- **Otros recursos del autor** enlazados desde el pie: el libro *Grokking Machine Learning* y el canal de YouTube.

## Inconsistencies / open questions

- **[Punto 1 del encargo] Error de atribución confirmado en la slide 18.** El deck atribuye el video del ejemplo Slanted Land a **"Rowel Atienza"**. El video es de **Luis Serrano** (YouTube `8L11aMN5KY8`). Esta captura lo cierra: el ejemplo Slanted Land, el notebook `GANs_in_Slanted_Land.ipynb` y el repositorio `luisguiserrano/gans` son todos de Luis Serrano, publicados en su propio sitio y bajo su propio dominio (`serrano.academy`), como parte de su curso de deep learning.
  Agravantes y atenuantes del error, para que quede completo:
  - **El deck se contradice a sí mismo**: la slide 37 cita correctamente a Luis Serrano por el mismo material. La 18 y la 37 no pueden ser las dos correctas.
  - **De dónde puede venir la confusión**: Rowel Atienza es un autor real del campo (*Advanced Deep Learning with Keras* / *with TensorFlow 2 and Keras*, Packt), con material de GANs propio. No tiene relación con Slanted Land.
  - **Corrección recomendada**: en la slide 18, atribuir el video a Luis Serrano y, si se quiere dar el material ejecutable, enlazar este laboratorio (`https://www.serrano.academy/deep-learning/gans-lab`) o el notebook de Colab directamente.
- **La página es fina en contenido teórico.** `page.md` tiene 1.521 caracteres, casi todos de navegación. **No se aplicó el fallback a `original.html`** (el criterio es <400 caracteres o cero encabezados, y esta página tiene 1.521 y varios encabezados), pero la extracción de texto de `original.html` da apenas 1.485 caracteres — la página es genuinamente delgada, no es un fallo del extractor. Todo el contenido sustantivo del laboratorio está **dentro del notebook**, que no fue capturado. Lo único que `original.html` aportó de más y `page.md` perdió es la **estructura del curso**, preservada abajo.
- **Nivel de la fuente**: material didáctico, no fuente primaria de investigación. Perfecto para lo que la clase lo usa (la intuición del juego generador/discriminador con un ejemplo mínimo); no citable para afirmaciones técnicas ni para resultados.
- **Sin fecha de publicación**: la página no la trae. Si el deck necesita fechar la referencia, hay que ir al historial del repositorio de GitHub.

## Images / diagrams

- `serrano-gans-lab.web/images/gans-better.jpg`
  - Depiction: **la imagen de Slanted Land.** Composición en blanco y negro, sobre fondo blanco, con dos filas. Arriba, dos caras dibujadas a mano con trazo suelto, ambas inclinadas en diagonal: cuerpos ovalados alargados, ojos como pequeños corazones o círculos, y unas patitas finas — los habitantes de Slanted Land. Abajo, dos grillas de 2×2 celdas: la de la izquierda en blanco y negro puro (negro arriba-izquierda, blanco arriba-derecha, blanco abajo-izquierda, negro abajo-derecha), la de la derecha con los mismos cuatro cuadrantes pero en escala de grises (gris oscuro, blanco, gris claro, gris medio). Es decir: **el dibujo "artístico" arriba, y abajo su representación real como imagen de cuatro píxeles**, primero binaria y después continua.
  - Why it matters: **es la prueba visual de que Slanted Land es de Luis Serrano.** Y explica de un vistazo el ejemplo entero: las "caras" de Slanted Land son imágenes de 2×2 píxeles con una diagonal más clara; eso es lo que la GAN del laboratorio aprende a generar. La grilla en grises de la derecha es la salida del generador — valores continuos que aproximan el patrón diagonal, en vez de blanco y negro perfectos. Si la clase usa el ejemplo (slides 18 y 37), esta es la imagen que lo sostiene y la fuente que hay que citar.
  - Transcribed text: ninguno. La imagen no contiene texto.
- `serrano-gans-lab.web/images/SERRANO.ACADEMY.+3.png`
  - Depiction: logotipo de Luis Serrano Academy. Arriba, un isotipo geométrico formado por dos cuadrados superpuestos con esquinas recortadas — uno rojo (arriba a la derecha) y uno negro (abajo a la izquierda) — que dejan un cuadrado blanco en el centro. Debajo, el nombre en tipografía sans-serif pesada: "Luis" en negro, "Serrano" en rojo, "Academy" en negro.
  - Why it matters: es la marca del sitio y, en el contexto del error de atribución de la slide 18, **es evidencia de autoría**: el material vive bajo la marca personal de Luis Serrano. Aparece dos veces en el HTML (cabecera y menú), deduplicada por el ingestor a un solo archivo.
  - Transcribed text: **"Luis Serrano Academy"**. `alt="Luis Serrano Academy"`.

## Raw / preserved excerpts

Contenido completo de la lección, verbatim de `page.md`:

> Chapter 2 - Generative Neural Networks
>
> # Labs - Generative Adversarial Networks
>
> https://colab.research.google.com/github/luisguiserrano/gans/blob/master/GANs_in_Slanted_Land.ipynb
>
> #### [Lab 1: Training a GAN from scratch](https://colab.research.google.com/github/luisguiserrano/gans/blob/master/GANs_in_Slanted_Land.ipynb)
>
> In this lab, you'll build a simple Generative Adversarial Network, and train it to generate faces of people in Slanted Land.

Estructura completa del curso, extraída de `original.html` (se preserva porque `page.md` la perdió y ubica el laboratorio en su contexto pedagógico):

> Deep Learning and Neural Networks
>
> **Chapter 1 - Predictive Neural Networks — 4 Lessons**
> Neural Networks
> Labs - Neural Networks
> Convolutional Neural Networks
> Recurrent Neural Networks
>
> **Chapter 2 - Generative Neural Networks — 6 Lessons**
> Denoising and Variational Autoencoders
> Generative Adversarial Networks (GANS)
> Labs - Generative Adversarial Networks   ← esta página
> Stable Diffusion
> Restricted Boltzmann Machines (RBMs)
> Hopfield Networks
>
> **Chapter 3: Math Foundations of Neural Networks — 4 Lessons**
> Universal Approximation Theorem
> Stone-Weierstrass Theorem
> Kolmogorov-Arnold Networks
> Kolmogorov-Arnold Theorem

Pie del sitio, verbatim:

> LEARN — Learning Hub, Supervised Learning, Unsupervised Learning, Deep Learning, Large Language Models, Reinforcement Learning for LLMs
> FOR ORGANIZATIONS — Speaking & Consulting, Let's Connect
> RESOURCES — Grokking Machine Learning Book, YouTube Channel

Enlaces del autor, verbatim del encabezado:

> https://www.linkedin.com/in/luisgserrano/
> http://youtube.com/@SerranoAcademy
> https://twitter.com/SerranoAcademy
