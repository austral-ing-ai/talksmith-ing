---
source_file: imagen-saharia-2022
source_type: web-capture
ingested_at: 2026-08-14
---

# Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding — Imagen (arXiv:2205.11487) — página de abstract

## Provenance
- Original location: `research/web/imagen-saharia-2022/`
- Format: web-capture (arXiv `abs` page; `page.md` + `original.html` + `assets/`)
- URL: https://arxiv.org/abs/2205.11487
- Author / source (if known): Chitwan Saharia, William Chan et al. (Google Research, Brain Team) — 14 autores
- Date of original (if known): 23 may 2022 (v1, única versión)
- Fetched at: 2026-08-14T17:03:10Z (HTTP 200, 43.825 bytes)
- Rol en la Clase 9: la alternativa contemporánea a Stable Diffusion. Sirve para mostrar que la difusión latente no era el único camino, y para el contraste de diseño: **Imagen usa un LLM de texto puro (T5) donde Stable Diffusion usa CLIP**.

## Key claims

- **Autores:** Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily Denton, Seyed Kamyar Seyed Ghasemipour, Burcu Karagol Ayan, S. Sara Mahdavi, Rapha Gontijo Lopes, Tim Salimans, Jonathan Ho, David J Fleet, Mohammad Norouzi. **Año:** 2022. **Venue:** preprint arXiv — la página **no declara venue** (el paper se presentó luego en NeurIPS 2022, dato ausente de la captura). **arXiv ID:** arXiv:2205.11487 [cs.CV, cs.LG]. **DOI:** 10.48550/arXiv.2205.11487.
- Imagen es un **modelo de difusión de texto a imagen** con un grado de fotorrealismo "sin precedentes" y comprensión profunda del lenguaje.
- Se apoya en dos patas: **modelos de lenguaje transformer grandes** para entender el texto, y **modelos de difusión** para generar imagen de alta fidelidad.
- **El hallazgo central del paper:** los **LLM genéricos preentrenados sólo con texto (por ejemplo T5)** son "sorprendentemente efectivos" para codificar texto destinado a síntesis de imágenes.
- **Y el corolario, que es lo verdaderamente interesante:** **agrandar el modelo de lenguaje mejora tanto la fidelidad de las muestras como la alineación imagen-texto mucho más que agrandar el modelo de difusión de imagen**. Dicho de otro modo: para generar mejores imágenes conviene invertir en entender mejor el texto.
- **Resultado:** **FID de 7,27 en COCO**, estado del arte, **sin haber entrenado nunca sobre COCO**. Evaluadores humanos consideran las muestras de Imagen a la par de los datos reales de COCO en alineación imagen-texto.
- Introducen **DrawBench**, un benchmark exigente para modelos de texto a imagen.
- En DrawBench, evaluadores humanos **prefieren Imagen** sobre VQ-GAN+CLIP, los modelos de difusión latente y DALL-E 2, tanto en calidad de muestra como en alineación con el texto.

## Definitions and terminology

- **Text-to-image por difusión.** El encuadre general del bloque de generación del deck.
- **Encoder de texto congelado y genérico.** Aunque el abstract no usa la palabra "frozen", la idea es explícita: un LLM "pretrained on text-only corpora" se usa tal cual para codificar el prompt. Es el contraste de diseño con CLIP, que se entrena específicamente sobre pares imagen-texto. **Punto pedagógico:** los dos caminos funcionan. Stable Diffusion condiciona con un encoder multimodal (CLIP); Imagen condiciona con un encoder unimodal de texto (T5). Que el segundo funcione tan bien —o mejor— es un resultado contraintuitivo que vale la pena señalar en clase.
- **Escalado asimétrico.** "Increasing the size of the language model in Imagen boosts both sample fidelity and image-text alignment much more than increasing the size of the image diffusion model." Es la frase más citable del abstract y la que mejor resume por qué el paper importó.
- **FID (Fréchet Inception Distance).** Métrica de calidad de generación que el abstract reporta (7,27 en COCO) **sin definir**. Es, junto al mean IU de FCN, uno de los pocos números de métrica del corpus.
- **Alineación imagen-texto (*image-text alignment*).** Cuánto se corresponde la imagen generada con el prompt. Se evalúa con jueces humanos.
- **DrawBench.** El benchmark que el paper introduce.
- **Difusión en cascada / superresolución.** **Ausente del abstract.** La arquitectura real de Imagen —un modelo base de 64×64 seguido de dos etapas de superresolución por difusión hasta 1024×1024— **no se menciona**. Es justamente lo que lo distingue de la difusión latente: Imagen trabaja **en espacio de píxeles con cascada**, no en un espacio latente comprimido. Ese contraste, que es el más interesante para la clase, no está respaldado por la captura.

## Evidence and examples

- **FID 7,27 en COCO**, estado del arte, **zero-shot** (sin entrenar sobre COCO). El número más duro del abstract.
- Jueces humanos ubican a Imagen **a la par de los datos reales de COCO** en alineación imagen-texto.
- Comparaciones lado a lado en **DrawBench** contra **VQ-GAN+CLIP, Latent Diffusion Models y DALL-E 2**: los evaluadores prefieren Imagen en ambas dimensiones.
- LLM nombrado explícitamente: **T5**.
- Sitio de resultados: `https://imagen.research.google/`.

### Verificación de cifras del deck

El deck no cita cifras de Imagen entre las que este encargo pide verificar. Queda disponible y verificado el **FID 7,27 zero-shot en COCO**. Nota: si el deck compara Imagen con Stable Diffusion, conviene recordar que la comparación de DrawBench es contra "Latent Diffusion Models" (el paper de Rombach), **no** contra Stable Diffusion, que se lanzó tres meses después de este preprint.

## Inconsistencies / open questions

1. **La página capturada trae solo el abstract.** Lo que la clase necesitaría y no está:
   - **El diagrama de la cascada** (T5 congelado → difusión 64×64 → superresolución 256×256 → superresolución 1024×1024). Sin él no se puede mostrar el contraste arquitectónico con la difusión latente, que es la razón principal para incluir Imagen en el deck.
   - Las **curvas de escalado** que respaldan la afirmación central (modelo de lenguaje más grande > modelo de difusión más grande).
   - La técnica de ***dynamic thresholding*** que Imagen introduce para poder usar escalas de guidance altas sin quemar la imagen — directamente relevante para el bloque de classifier-free guidance del deck.
   - Los **resultados de DrawBench** desagregados por categoría.
   - La sección de **limitaciones e impacto social**, que en Imagen es notable: Google **no liberó ni el modelo ni una demo pública** por preocupaciones de sesgo y uso indebido. Ese hecho —un modelo de estado del arte deliberadamente no publicado— es un contraste fuerte con Stable Diffusion, que se liberó completo tres meses después, y no aparece en la captura.
   Todo eso está en el PDF (`https://arxiv.org/pdf/2205.11487`), no capturado.
2. **"Unprecedented degree of photorealism"** es una afirmación superlativa en la primera oración de un abstract académico, sostenida después por un solo FID y por preferencias humanas sobre un benchmark que el propio paper creó.
3. **DrawBench es del propio paper.** Imagen gana en el benchmark que Imagen introdujo. Es práctica común y el benchmark se publicó, pero conviene decirlo al mostrar el resultado.
4. **El contraste latente vs. píxeles no está en el abstract.** El motivo por el cual la clase incluiría a Imagen —que resuelve el mismo problema por un camino arquitectónico opuesto al de Stable Diffusion— requiere información que la captura no trae.
5. **La página no declara venue.** Si el deck cita "NeurIPS 2022", el dato es correcto pero no proviene de esta fuente.

## Images / diagrams

La captura de una página `abs` de arXiv **no incluye ninguna figura del paper** — no trae el diagrama de la cascada ni ninguna imagen generada. Los tres archivos guardados son cromo del sitio, copiados a la carpeta compañera por completitud.

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

> We present Imagen, a text-to-image diffusion model with an unprecedented degree of photorealism and a deep level of language understanding. Imagen builds on the power of large transformer language models in understanding text and hinges on the strength of diffusion models in high-fidelity image generation. Our key discovery is that generic large language models (e.g. T5), pretrained on text-only corpora, are surprisingly effective at encoding text for image synthesis: increasing the size of the language model in Imagen boosts both sample fidelity and image-text alignment much more than increasing the size of the image diffusion model. Imagen achieves a new state-of-the-art FID score of 7.27 on the COCO dataset, without ever training on COCO, and human raters find Imagen samples to be on par with the COCO data itself in image-text alignment. To assess text-to-image models in greater depth, we introduce DrawBench, a comprehensive and challenging benchmark for text-to-image models. With DrawBench, we compare Imagen with recent methods including VQ-GAN+CLIP, Latent Diffusion Models, and DALL-E 2, and find that human raters prefer Imagen over other models in side-by-side comparisons, both in terms of sample quality and image-text alignment. See https://imagen.research.google/ for an overview of the results.

**Metadatos de la página, verbatim:**

> Computer Science > Computer Vision and Pattern Recognition
> arXiv:2205.11487 (cs)
> [Submitted on 23 May 2022]
> Title: Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding
> Authors: Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily Denton, Seyed Kamyar Seyed Ghasemipour, Burcu Karagol Ayan, S. Sara Mahdavi, Rapha Gontijo Lopes, Tim Salimans, Jonathan Ho, David J Fleet, Mohammad Norouzi
> Subjects: Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)
> Cite as: arXiv:2205.11487 [cs.CV]
> https://doi.org/10.48550/arXiv.2205.11487
