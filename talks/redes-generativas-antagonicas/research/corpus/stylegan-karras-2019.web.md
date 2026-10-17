---
source_file: stylegan-karras-2019
source_type: web-capture
ingested_at: 2026-08-14
---

# A Style-Based Generator Architecture for GANs — StyleGAN (Karras, Laine & Aila) — página abstract de arXiv

## Provenance
- Original location: `research/web/stylegan-karras-2019/`
- Format: html (captura web de `talksmith:ingest` — `page.md` + `original.html` + `assets/`)
- Author / source (if known): Tero Karras, Samuli Laine, Timo Aila — NVIDIA (la afiliación no figura en la captura; sí en el paper) — arXiv
- Date of original (if known): **enviado el 12 de diciembre de 2018 (v1)**; v2 el 6 de febrero de 2019; **última revisión 29 de marzo de 2019 (v3, la capturada), marcada "CVPR 2019 final version"**. Captura: 2026-08-14T17:02:50Z, HTTP 200, URL `https://arxiv.org/abs/1812.04948`

## Key claims

- **Proponen una arquitectura de generador alternativa, tomada prestada de la literatura de transferencia de estilo** (*borrowing from style transfer literature*). Ese préstamo es exactamente `adain-huang-belongie-2017.web.md` en este corpus: AdaIN es el mecanismo que StyleGAN importa.
- **La arquitectura produce una separación automática y no supervisada entre atributos de alto nivel y variación estocástica.** Los ejemplos son del propio abstract: pose e identidad cuando se entrena con caras humanas (alto nivel) frente a pecas y pelo (estocástico).
- **Permite control específico por escala de la síntesis** (*intuitive, scale-specific control*). Esto es lo que sostiene el *style mixing*: intervenir en unas escalas y no en otras.
- **Mejora el estado del arte en métricas tradicionales de calidad de distribución** (léase FID, aunque el abstract no la nombra), **con mejores propiedades de interpolación y mejor desenredo (disentanglement) de los factores latentes de variación.**
- **Proponen dos métricas automáticas nuevas** para cuantificar calidad de interpolación y desenredo, aplicables a cualquier arquitectura de generador. (En el paper son *perceptual path length* y *linear separability*; **esos nombres no aparecen en esta captura**.)
- **Introducen un dataset nuevo de caras humanas, "altamente variado y de alta calidad".** El abstract **no lo nombra**. Es FFHQ (Flickr-Faces-HQ), pero ese nombre **no está en la captura** — si el deck lo usa, hay que citarlo del paper, no de este registro.

Datos bibliográficos para la cita:
- Autores: Tero Karras, Samuli Laine, Timo Aila
- Año: 2018 (arXiv v1) / **2019 (CVPR)**
- arXiv ID: **arXiv:1812.04948 [cs.NE]** (v3)
- DOI: `https://doi.org/10.48550/arXiv.1812.04948`
- Materias: Neural and Evolutionary Computing (cs.NE); Machine Learning (cs.LG); Machine Learning (stat.ML)
- Venue: Comments dice **"CVPR 2019 final version"**.

## Definitions and terminology

Lo que la clase reutiliza — con la advertencia de qué está y qué no está en esta captura:

- **Arquitectura basada en estilo (style-based generator)**: sí está, es el título y el eje del abstract.
- **Control específico por escala (scale-specific control)**: sí está. Es la base conceptual del *style mixing*.
- **Separación de atributos de alto nivel vs. variación estocástica**: sí está, con los ejemplos pose/identidad vs. pecas/pelo.
- **Desenredo (disentanglement) de factores latentes de variación**: sí está, junto con "mejores propiedades de interpolación".
- **Mapping network** (la red de 8 capas que transforma `z` en `w`), **el espacio intermedio `w`**, **AdaIN como capa de inyección de estilo**, y **style mixing** como técnica de regularización nombrada: **ninguno de estos cuatro términos aparece en esta captura.** Están en el cuerpo del paper. Para AdaIN, la fuente primaria del corpus es `adain-huang-belongie-2017.web.md`, que sí lo define en detalle.
- **Progressive growing**: **no aparece en esta captura, y no es de este paper.** Ver *Inconsistencies*, punto 2.

## Evidence and examples

- Ejemplos concretos que da el abstract, útiles para explicar la separación de atributos: **pose e identidad** como atributos de alto nivel; **pecas y pelo** como variación estocástica. Son los ejemplos de los propios autores y funcionan bien en clase.
- Mejora del estado del arte en "traditional distribution quality metrics" — **sin ningún número en la captura**. No hay valores de FID.
- Dos métricas nuevas propuestas, sin nombre ni valor en la captura.
- Un dataset nuevo de caras, sin nombre en la captura.
- Peso de la subida: 22.070 KB — el paper es masivo en figuras; ninguna llegó a la captura.

## Inconsistencies / open questions

- **[Punto 3 del encargo] Contradicción de fecha dentro del propio deck.** La slide 40 dice "StyleGAN (2018)" y la slide 41 dice "NVIDIA, 2019". Las dos son defendibles y por eso el conflicto se resuelve, no se corrige a ciegas. Los datos duros de esta captura:
  - **arXiv v1: 12 de diciembre de 2018** — de ahí sale el "2018" de la slide 40.
  - **arXiv v3: 29 de marzo de 2019**, con Comments **"CVPR 2019 final version"** — de ahí sale el "2019" de la slide 41.
  - **Publicación en conferencia: CVPR 2019.**
  Recomendación para la tabla de linaje: fijar un criterio único (o "año de arXiv" o "año de publicación") y aplicarlo a todas las filas. Si el criterio es publicación, StyleGAN es **2019** y las dos slides deben decir 2019. Si el criterio es arXiv, es 2018 — pero entonces DCGAN es 2015 y ProGAN es 2017, no 2018, y la tabla cambia en varias filas a la vez.
- **[Punto 2 del encargo] El deck le atribuye a StyleGAN el *progressive growing*.** No es de StyleGAN. El *progressive growing* es de **Karras et al. 2018, "Progressive Growing of GANs" (arXiv:1710.10196, ICLR 2018)** — mismo primer autor, paper anterior y distinto. El asiento completo del error está en `progan-progressive-growing-karras-2018.web.md`. Se deja la referencia cruzada acá porque es en este registro donde el lector del deck va a buscar. Nota atenuante honesta: StyleGAN **sí usa** progressive growing (su generador se construye sobre el de ProGAN), así que la afirmación "StyleGAN entrena con crecimiento progresivo" es cierta; la que es falsa es "StyleGAN **introdujo** el crecimiento progresivo".
- **El dataset nuevo no está nombrado en la captura.** Se anota bajo el punto 4 del encargo (el deck no nombra ni un dataset): acá la fuente sí tiene uno propio y hasta lo presenta como contribución, pero el abstract lo deja anónimo. FFHQ es el nombre correcto y hay que sacarlo del paper.
- **Gap de extracción**: sin figuras, sin la Figura 1 (comparación de arquitectura tradicional vs. basada en estilo) ni la grilla de style mixing, que es el material visual que la clase querría.

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

> Abstract: We propose an alternative generator architecture for generative adversarial networks, borrowing from style transfer literature. The new architecture leads to an automatically learned, unsupervised separation of high-level attributes (e.g., pose and identity when trained on human faces) and stochastic variation in the generated images (e.g., freckles, hair), and it enables intuitive, scale-specific control of the synthesis. The new generator improves the state-of-the-art in terms of traditional distribution quality metrics, leads to demonstrably better interpolation properties, and also better disentangles the latent factors of variation. To quantify interpolation quality and disentanglement, we propose two new, automated methods that are applicable to any generator architecture. Finally, we introduce a new, highly varied and high-quality dataset of human faces.

Bloque bibliográfico verbatim — **preservado porque es la prueba documental de la contradicción de fechas del deck**:

> Computer Science > Neural and Evolutionary Computing
> **arXiv:1812.04948** (cs) [Submitted on 12 Dec 2018 (v1), last revised 29 Mar 2019 (this version, v3)]
> Title: A Style-Based Generator Architecture for Generative Adversarial Networks
> Authors: Tero Karras, Samuli Laine, Timo Aila
> Comments: CVPR 2019 final version
> Subjects: Neural and Evolutionary Computing (cs.NE); Machine Learning (cs.LG); Machine Learning (stat.ML)
> Cite as: arXiv:1812.04948 [cs.NE] (or arXiv:1812.04948v3 [cs.NE] for this version)
> https://doi.org/10.48550/arXiv.1812.04948

> Submission history
> From: Samuli Laine
> **[v1]** Wed, 12 Dec 2018 13:59:43 UTC (22,070 KB)
> **[v2]** Wed, 6 Feb 2019 14:58:00 UTC (22,070 KB)
> **[v3]** Fri, 29 Mar 2019 11:08:46 UTC (22,071 KB)
