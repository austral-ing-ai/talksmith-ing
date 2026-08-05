---
source_file: arxiv-2001-08361-scaling-laws
source_type: web-capture
ingested_at: 2026-08-05
---

# Scaling Laws for Neural Language Models (arXiv:2001.08361) — página de abstract

## Provenance
- Ubicación original: `research/web/arxiv-2001-08361-scaling-laws/`
- Formato: captura web (`original.html` 43.365 bytes + `page.md` 7.573 bytes + `assets/`)
- URL: https://arxiv.org/abs/2001.08361
- Autores: Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child,
  Scott Gray, Alec Radford, Jeffrey Wu, Dario Amodei
- Fecha del original: enviado el **23 de enero de 2020** (v1, única versión)
- Capturado el: 2026-08-05T12:19:24Z · HTTP 200
- **Alcance de la captura: solo la página de abstract.** No se capturó el PDF ni el cuerpo del paper.

## Key claims

- Los autores estudian **leyes de escala empíricas** para el rendimiento de modelos de lenguaje
  medido sobre la **pérdida de entropía cruzada** (cross-entropy loss).
- La pérdida escala como **ley de potencia** con tres variables: **tamaño del modelo**, **tamaño del
  dataset** y **cantidad de cómputo** usado para entrenar.
- Algunas de esas tendencias abarcan **más de siete órdenes de magnitud**.
- Otros detalles arquitectónicos —**ancho o profundidad de la red**— tienen **efectos mínimos**
  dentro de un rango amplio. Es decir: lo que manda es la escala, no la forma.
- Ecuaciones simples gobiernan (a) la dependencia del **sobreajuste** respecto del cociente
  tamaño-de-modelo / tamaño-de-dataset, y (b) la dependencia de la **velocidad de entrenamiento**
  respecto del tamaño del modelo.
- Estas relaciones permiten determinar la **asignación óptima de un presupuesto fijo de cómputo**.
- **Los modelos más grandes son significativamente más eficientes en muestras** (*more
  sample-efficient*). En consecuencia, el entrenamiento óptimo en términos de cómputo consiste en
  **entrenar modelos muy grandes sobre una cantidad de datos relativamente modesta y detenerse
  bastante antes de la convergencia**.

## Definitions and terminology

- **Scaling law / ley de escala**: relación de ley de potencia entre una métrica de rendimiento y una
  variable de recursos (parámetros, datos, cómputo).
- **Cross-entropy loss**: la métrica de rendimiento sobre la que se miden las leyes; no es una
  métrica de tarea sino de predicción del siguiente token.
- **Sample efficiency**: cuánto rendimiento se extrae por unidad de datos vistos. El hallazgo central
  es que crece con el tamaño del modelo.
- **Compute-efficient training**: régimen de entrenamiento que maximiza rendimiento por unidad de
  cómputo. Según el paper, implica modelos grandes, datos modestos y parada temprana.
- **Overfitting / sobreajuste**: acá tratado como función del cociente modelo/dataset, no como
  fenómeno cualitativo.

## Evidence and examples

- Tendencias que abarcan **más de siete órdenes de magnitud** (la única cuantificación explícita del
  abstract).
- Metadatos bibliográficos:
  - **Comments:** 19 páginas, **15 figuras**
  - **Subjects:** Machine Learning (cs.LG); Machine Learning (stat.ML)
  - **DOI:** https://doi.org/10.48550/arXiv.2001.08361
  - **Licencia:** arXiv non-exclusive distribution license 1.0
  - **Trackbacks:** 15 blog links
  - Historial: v1, jueves 23 de enero de 2020, 03:59:20 UTC (1.520 KB). **Versión única.**
    Enviado por Samuel McCandlish.

## Inconsistencies / open questions

- **La captura no contiene el paper.** Las **15 figuras** —que son justamente las curvas de ley de
  potencia, el material gráfico más citado de este trabajo— **no están acá**. Para usarlas hay que
  traer el PDF (`/pdf/2001.08361`) o el TeX source (`/src/2001.08361`) por separado. Esta captura no
  ofrece HTML experimental.
- El abstract **no da ninguna ecuación ni exponente**. Las "ecuaciones simples" que menciona quedan
  fuera de la captura.
- El abstract **no cuantifica** qué es "una cantidad de datos relativamente modesta" ni cuán antes de
  la convergencia conviene detenerse.
- **Tensión con literatura posterior (fuera de esta fuente):** la recomendación de "modelos muy
  grandes sobre datos modestos" fue revisada por trabajos posteriores sobre asignación
  compute-óptima. La captura no la registra porque es de 2020 y no tiene revisiones. Si la
  presentación contrasta ambos regímenes, necesita una fuente adicional; **este registro no la
  contiene**.
- Versión única sin revisiones en más de seis años: la fuente está congelada en enero de 2020.
- El `page.md` mezcla contenido con navegación de arXiv (arXivLabs, recomendadores, herramientas
  bibliográficas). Ruido de extracción.

## Images / diagrams

Las 4 imágenes descargadas son **cromo del sitio arXiv**, no figuras del paper. Copiadas a la
carpeta companion por completitud; sin valor expositivo.

- `arxiv-2001-08361-scaling-laws.web/images/arxiv-logo-primary-light.svg`
  - Provenance: `research/web/arxiv-2001-08361-scaling-laws/assets/`; origen
    `https://arxiv.org/static/base/1.0.1/images/arxiv-logo-primary-light.svg`; alt = "archive"
  - Depiction: logotipo de arXiv (versión clara), cabecera del sitio.
  - Why it matters: no aplica. Cromo del sitio.
- `arxiv-2001-08361-scaling-laws.web/images/smileybones-small.svg`
  - Provenance: `assets/`; origen `https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg`; alt vacío
  - Depiction: ícono decorativo del banner "arXiv is now an independent nonprofit".
  - Why it matters: no aplica. Cromo del sitio.
- `arxiv-2001-08361-scaling-laws.web/images/bibsonomy.png`
  - Provenance: `assets/`; origen `https://arxiv.org/static/browse/0.3.4/images/icons/social/bibsonomy.png`; alt = "BibSonomy"
  - Depiction: ícono social de BibSonomy en la sección "Bookmark".
  - Why it matters: no aplica. Cromo del sitio.
- `arxiv-2001-08361-scaling-laws.web/images/reddit.png`
  - Provenance: `assets/`; origen `https://arxiv.org/static/browse/0.3.4/images/icons/social/reddit.png`; alt = "Reddit"
  - Depiction: ícono social de Reddit en la sección "Bookmark".
  - Why it matters: no aplica. Cromo del sitio.

**Las 15 figuras del paper no fueron capturadas.**

## Raw / preserved excerpts

Abstract completo, verbatim:

> Abstract:We study empirical scaling laws for language model performance on the cross-entropy loss. The loss scales as a power-law with model size, dataset size, and the amount of compute used for training, with some trends spanning more than seven orders of magnitude. Other architectural details such as network width or depth have minimal effects within a wide range. Simple equations govern the dependence of overfitting on model/dataset size and the dependence of training speed on model size. These relationships allow us to determine the optimal allocation of a fixed compute budget. Larger models are significantly more sample-efficient, such that optimally compute-efficient training involves training very large models on a relatively modest amount of data and stopping significantly before convergence.

Bloque bibliográfico, verbatim:

> Comments: 19 pages, 15 figures Subjects: Machine Learning (cs.LG); Machine Learning (stat.ML) Cite as: arXiv:2001.08361 [cs.LG] (or arXiv:2001.08361v1 [cs.LG] for this version) https://doi.org/10.48550/arXiv.2001.08361

Lista de autores, verbatim y en orden:

> Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, Dario Amodei
