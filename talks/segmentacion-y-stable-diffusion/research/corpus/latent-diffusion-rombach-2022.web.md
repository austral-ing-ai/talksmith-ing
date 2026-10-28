---
source_file: latent-diffusion-rombach-2022
source_type: web-capture
ingested_at: 2026-08-14
---

# High-Resolution Image Synthesis with Latent Diffusion Models (arXiv:2112.10752) — página de abstract

## Provenance
- Original location: `research/web/latent-diffusion-rombach-2022/`
- Format: web-capture (arXiv `abs` page; `page.md` + `original.html` + `assets/`)
- URL: https://arxiv.org/abs/2112.10752
- Author / source (if known): Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, Björn Ommer (LMU München / IWR Heidelberg — grupo CompVis)
- Date of original (if known): enviado 20 dic 2021; última revisión 13 abr 2022 (v2). CVPR 2022.
- Fetched at: 2026-08-14T17:03:10Z (HTTP 200, 43.929 bytes)
- Rol en la Clase 9: **el paper de Stable Diffusion**. Es la columna vertebral del bloque de generación — el espacio latente, el cross-attention y la reducción de cómputo salen de acá.

## Key claims

- **Autores:** Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, Björn Ommer. **Año:** 2021 (v1) / 2022 (v2). **Venue:** CVPR 2022. **arXiv ID:** arXiv:2112.10752 [cs.CV]. **DOI:** 10.48550/arXiv.2112.10752.
- Los modelos de difusión (DMs) descomponen la formación de la imagen en una **aplicación secuencial de autoencoders de denoising** y alcanzan el estado del arte en síntesis.
- Su formulación **admite un mecanismo de guiado para controlar la generación sin reentrenar** — es el gancho directo hacia classifier-free guidance.
- **El problema:** operar directamente en el **espacio de píxeles** hace que optimizar un DM potente consuma **cientos de días de GPU**, y que la inferencia sea cara por las evaluaciones secuenciales.
- **La solución:** aplicar la difusión **en el espacio latente de autoencoders preentrenados potentes**. Esto permite entrenar con recursos limitados sin perder calidad ni flexibilidad.
- Es el primer trabajo que alcanza **"un punto casi óptimo entre reducción de complejidad y preservación de detalle"**, subiendo mucho la fidelidad visual.
- **Introduciendo capas de cross-attention** en la arquitectura, los DMs se convierten en generadores flexibles para **entradas de condicionamiento generales** — texto o cajas delimitadoras — y la síntesis en alta resolución pasa a ser posible de forma convolucional.
- Resultados: nuevo estado del arte en **inpainting**, y desempeño muy competitivo en generación incondicional, síntesis semántica de escenas y superresolución, **reduciendo significativamente el costo computacional** frente a los DMs en píxeles.

## Definitions and terminology

- **Espacio latente.** "We apply them in the latent space of powerful pretrained autoencoders." La definición operativa que la clase usa: en vez de difundir sobre los píxeles, se difunde sobre la representación comprimida que produce el encoder de un autoencoder ya entrenado. El abstract enuncia el movimiento con total claridad.
- **Factor de downsampling (f).** **Ausente del abstract.** La notación `f` (f=4, f=8, f=16…) que parametriza cuánto comprime el autoencoder, y con ella las dimensiones concretas del latente, **no aparece en la página capturada**. El abstract habla en cualitativo ("complexity reduction", "detail preservation") sin dar un solo número. Esto es central para verificar la cifra del deck (ver abajo).
- **Cross-attention.** "By introducing cross-attention layers into the model architecture, we turn diffusion models into powerful and flexible generators for general conditioning inputs such as text or bounding boxes." Es el término mejor respaldado del bloque de difusión: aparece literal en el abstract, con su propósito explícito (inyectar condicionamiento arbitrario, incluido texto). El abstract **no explica el mecanismo** (queries desde el latente, keys/values desde el embedding de texto).
- **Autoencoder de denoising.** El abstract encuadra a los DMs como "a sequential application of denoising autoencoders" — útil como definición de una línea para abrir el bloque.
- **Mecanismo de guiado sin reentrenar.** "Their formulation allows for a guiding mechanism to control the image generation process without retraining." Es el puente hacia `classifier-free-guidance-ho-2022.web.md`, aunque el abstract no nombra classifier-free guidance.
- **Síntesis convolucional en alta resolución.** El modelo puede generar a resoluciones mayores que las de entrenamiento aplicándose de forma convolucional.

## Evidence and examples

- **"Hundreds of GPU days"** — el costo de entrenar DMs en espacio de píxeles. Es el número (aproximado) que motiva todo el paper.
- Tareas donde alcanza estado del arte o resultados competitivos: **inpainting** (SOTA), generación incondicional, **síntesis semántica de escenas**, **superresolución**.
- "Significantly reducing computational requirements compared to pixel-based DMs" — **sin cuantificar** en el abstract.
- Código: `https://github.com/CompVis/latent-diffusion`.

### Verificación de cifras del deck

- **Latente 64×64×4 y "48× menos información" — NO CIERRAN CONTRA ESTA FUENTE.** Ninguno de los dos números aparece en la página capturada. El abstract no da dimensiones de latente, ni factor de compresión, ni resolución de entrada. **La aritmética, sin embargo, es exacta**: para una imagen RGB de 512×512 se tienen 512 × 512 × 3 = **786.432** valores; para un latente de 64×64×4 se tienen 64 × 64 × 4 = **16.384**; el cociente es **786.432 / 16.384 = 48,0 exactamente**. Así que el "48×" del deck es correcto y no es un redondeo: es el resultado exacto para la configuración de Stable Diffusion (autoencoder con factor de downsampling f=8 y 4 canales latentes, entrada 512×512).
  **Precisiones necesarias:** (a) el número describe la **configuración concreta de Stable Diffusion**, no el paper de difusión latente en general — el paper evalúa varios factores de downsampling (f=1 hasta f=32) y ninguno es "el" latente; (b) es una razón de **cantidad de valores**, no de bits ni de "información" en sentido estricto — llamarlo "48× menos información" es una licencia didáctica aceptable pero no es una medida de entropía; (c) al pasar de 3 canales a 4, la reducción espacial es de 8×8 = 64×, y el canal extra la baja a 48×. Ese detalle suele confundirse.
  **Recomendación:** el par 64×64×4 / 48× es defendible y útil, pero atribuirlo a este paper es incorrecto. Corresponde a la configuración de Stable Diffusion, y su respaldo documental **no está en el corpus**: haría falta la tarjeta del modelo de Stable Diffusion o la sección 4 del paper (tabla de factores f), ninguna capturada.

## Inconsistencies / open questions

1. **La página capturada trae solo el abstract.** Lo que la clase necesitaría y no está:
   - **El diagrama de arquitectura (figura 3)** — encoder ε, espacio latente, U-Net de denoising, decoder D, y el bloque de condicionamiento τ_θ conectado por cross-attention. Es la imagen central del bloque de generación del deck.
   - **La tabla de factores de downsampling** (f=1, 2, 4, 8, 16, 32) con su compromiso entre calidad y velocidad — la única fuente posible para justificar por qué f=8 y por qué el latente es 64×64×4.
   - Las **dimensiones concretas** del latente para cada configuración.
   - El **mecanismo del cross-attention** (de dónde salen queries, keys y values).
   - Los **números de FID** y de costo de entrenamiento que respaldan "significantly reducing computational requirements".
   Todo eso está en el PDF (`https://arxiv.org/pdf/2112.10752`), no capturado.
2. **"Latent diffusion" no es lo mismo que "Stable Diffusion".** El paper es de CompVis (LMU/Heidelberg) y precede al lanzamiento de Stable Diffusion (agosto de 2022), que es una instancia concreta entrenada por Stability AI sobre LAION con un text encoder de CLIP. Casi todos los números que el deck asocia a "difusión latente" (64×64×4, 77 tokens, guidance 7,5) son en realidad de **Stable Diffusion**, no de este paper. Vale la pena que la clase haga la distinción explícita, porque es exactamente el punto donde se cuelan las imprecisiones.
3. **El texto como condicionamiento aparece casi al pasar.** El abstract lo menciona en una subordinada ("general conditioning inputs such as text or bounding boxes"). Este paper no es un paper de texto-a-imagen: es un paper de eficiencia de difusión que *habilita* el texto-a-imagen. Presentarlo como "el paper de la generación por texto" invierte el énfasis del original.
4. **"Near-optimal point between complexity reduction and detail preservation"** es una afirmación fuerte sin métrica en el abstract. ¿Óptimo respecto de qué criterio?
5. **"Hundreds of GPU days"** carece de referencia: ¿qué modelo, qué GPU, qué resolución? Es un orden de magnitud retórico.

## Images / diagrams

La captura de una página `abs` de arXiv **no incluye ninguna figura del paper** — no trae el diagrama de arquitectura. Los tres archivos guardados son cromo del sitio, copiados a la carpeta compañera por completitud.

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

> By decomposing the image formation process into a sequential application of denoising autoencoders, diffusion models (DMs) achieve state-of-the-art synthesis results on image data and beyond. Additionally, their formulation allows for a guiding mechanism to control the image generation process without retraining. However, since these models typically operate directly in pixel space, optimization of powerful DMs often consumes hundreds of GPU days and inference is expensive due to sequential evaluations. To enable DM training on limited computational resources while retaining their quality and flexibility, we apply them in the latent space of powerful pretrained autoencoders. In contrast to previous work, training diffusion models on such a representation allows for the first time to reach a near-optimal point between complexity reduction and detail preservation, greatly boosting visual fidelity. By introducing cross-attention layers into the model architecture, we turn diffusion models into powerful and flexible generators for general conditioning inputs such as text or bounding boxes and high-resolution synthesis becomes possible in a convolutional manner. Our latent diffusion models (LDMs) achieve a new state of the art for image inpainting and highly competitive performance on various tasks, including unconditional image generation, semantic scene synthesis, and super-resolution, while significantly reducing computational requirements compared to pixel-based DMs. Code is available at https://github.com/CompVis/latent-diffusion .

**Metadatos de la página, verbatim:**

> Computer Science > Computer Vision and Pattern Recognition
> arXiv:2112.10752 (cs)
> [Submitted on 20 Dec 2021 (v1), last revised 13 Apr 2022 (this version, v2)]
> Title: High-Resolution Image Synthesis with Latent Diffusion Models
> Authors: Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, Björn Ommer
> Comments: CVPR 2022
> Subjects: Computer Vision and Pattern Recognition (cs.CV)
> Cite as: arXiv:2112.10752 [cs.CV]
> https://doi.org/10.48550/arXiv.2112.10752
