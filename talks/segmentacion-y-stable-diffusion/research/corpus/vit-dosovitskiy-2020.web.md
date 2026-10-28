---
source_file: vit-dosovitskiy-2020
source_type: web-capture
ingested_at: 2026-08-14
---

# An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (arXiv:2010.11929) — página de abstract

## Provenance
- Original location: `research/web/vit-dosovitskiy-2020/`
- Format: web-capture (arXiv `abs` page; `page.md` + `original.html` + `assets/`)
- URL: https://arxiv.org/abs/2010.11929
- Author / source (if known): Alexey Dosovitskiy et al. (Google Research, Brain Team) — 12 autores
- Date of original (if known): enviado 22 oct 2020; última revisión 3 jun 2021 (v2, versión *camera-ready* de ICLR)
- Fetched at: 2026-08-14T17:03:10Z (HTTP 200, 41.949 bytes)
- Rol en la Clase 9: la pieza de infraestructura compartida. El ViT es el image encoder de SAM y la torre visual de CLIP — aparece a los dos lados del deck, en el bloque de segmentación y en el de difusión.

## Key claims

- **Autores:** Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby. **Año:** 2020 (v1) / 2021 (v2). **Venue:** ICLR 2021 (el campo `Comments` dice "ICLR camera-ready version"). **arXiv ID:** arXiv:2010.11929 [cs.CV, cs.AI, cs.LG]. **DOI:** 10.48550/arXiv.2010.11929.
- El Transformer ya era el estándar de facto en NLP, pero en visión la atención se usaba **junto a** las CNN o para reemplazar componentes puntuales **manteniendo la estructura convolucional**.
- Tesis del paper: **esa dependencia de las CNN no es necesaria**. Un transformer puro aplicado directamente a **secuencias de parches de imagen** funciona muy bien en clasificación.
- La condición es la escala: **preentrenado con grandes cantidades de datos** y transferido a benchmarks medianos o chicos (ImageNet, CIFAR-100, VTAB), el Vision Transformer (ViT) alcanza resultados excelentes frente a CNN de estado del arte.
- Y lo hace **requiriendo sustancialmente menos recursos de cómputo para entrenar**.

## Definitions and terminology

- **Vision Transformer (ViT).** El nombre del modelo. El abstract lo introduce sin desarmarlo.
- **Parches de imagen como tokens.** "A pure transformer applied directly to sequences of image patches". Es el concepto que sostiene el título: una imagen se corta en parches (16×16 píxeles, según el título) y cada parche se trata como una palabra en una secuencia. El abstract **no explica** el embedding lineal de parches, ni el token de clase, ni el embedding posicional.
- **Nomenclatura ViT-L/14, ViT-B/16, ViT-H.** **Ausente del abstract.** La convención `ViT-<tamaño>/<lado del parche>` — que la clase necesita para hablar de "CLIP ViT-L/14" y del "ViT-H" de SAM — no aparece en la página capturada. Está en la tabla 1 del paper, fuera de la captura.
- **Preentrenamiento a escala + transferencia.** El régimen de dos etapas que hace funcionar al ViT: preentrenar en un corpus grande, ajustar en la tarea chica.

## Evidence and examples

- Benchmarks nombrados: **ImageNet, CIFAR-100, VTAB**.
- "Substantially fewer computational resources to train" — afirmación comparativa **sin cifra** en el abstract.
- Código de fine-tuning y modelos preentrenados: `https://github.com/google-research/vision_transformer`.
- Nota de errata en el propio campo `Comments`: la versión ICLR corrige **un error en el cálculo de exaFLOPs de la Figura 5 y la Tabla 6**, aclarando que el desempeño relativo de los modelos "basically no se ve afectado". Vale la pena registrarlo: es un ejemplo honesto de corrección post-publicación en un paper canónico.

### Verificación de cifras del deck

El deck no cita cifras de ViT entre las que este encargo pide verificar. Lo que sí conviene anotar es que la nomenclatura **ViT-L/14** que el deck usa en la slide 42 (para CLIP) **no está definida en esta fuente**, así que si la clase la explica, la explicación no tiene respaldo documental en el corpus actual.

## Inconsistencies / open questions

1. **La página capturada trae solo el abstract.** Lo que la clase necesitaría y no está:
   - **La figura 1** — el diagrama de partición en parches, embedding lineal, embedding posicional y pila de transformer. Es la imagen que explica "an image is worth 16x16 words" de un vistazo.
   - La **tabla de variantes** (ViT-Base / Large / Huge; tamaños de parche 14, 16, 32) con parámetros, capas y ancho de cada una — necesaria para cualquier conteo de parámetros, incluido el de la slide 42 sobre CLIP.
   - Los **números concretos** de exactitud y de costo de entrenamiento que respaldan el "substantially fewer computational resources".
   - La discusión sobre el **sesgo inductivo** que las CNN tienen y los transformers no (localidad, equivarianza a traslación), que es el argumento de fondo del "hace falta mucho dato".
2. **"Substantially fewer computational resources" sin número**, y con una errata reconocida justamente en el cálculo de FLOPs de una de las figuras que lo respaldan. La afirmación es citable pero merece atenuarse.
3. **Condición de escala fácil de perder.** El abstract dice claramente "when pre-trained on large amounts of data". Presentar al ViT como superior a las CNN sin esa condición invierte el resultado del paper: sin datos masivos, el ViT rinde peor.
4. **El puente hacia SAM y CLIP no está en esta fuente.** Que el image encoder de SAM sea un ViT-H y que la torre visual de CLIP sea un ViT-L/14 son hechos que la clase usa, pero ninguno aparece acá ni en los abstracts de SAM o CLIP. Es una conexión que el deck hace por fuera del corpus.

## Images / diagrams

La captura de una página `abs` de arXiv **no incluye ninguna figura del paper** — no trae el diagrama de parches. Los tres archivos guardados son cromo del sitio, copiados a la carpeta compañera por completitud.

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

> While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited. In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure in place. We show that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks. When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision Transformer (ViT) attains excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train.

**Metadatos de la página, verbatim:**

> Computer Science > Computer Vision and Pattern Recognition
> arXiv:2010.11929 (cs)
> [Submitted on 22 Oct 2020 (v1), last revised 3 Jun 2021 (this version, v2)]
> Title: An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale
> Authors: Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby
> Comments: Fine-tuning code and pre-trained models are available at https://github.com/google-research/vision_transformer. ICLR camera-ready version with 2 small modifications: 1) Added a discussion of CLS vs GAP classifier in the appendix, 2) Fixed an error in exaFLOPs computation in Figure 5 and Table 6 (relative performance of models is basically not affected)
> Subjects: Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
> Cite as: arXiv:2010.11929 [cs.CV]
> https://doi.org/10.48550/arXiv.2010.11929
