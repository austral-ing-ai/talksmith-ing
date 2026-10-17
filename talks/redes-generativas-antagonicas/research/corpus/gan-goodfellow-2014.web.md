---
source_file: gan-goodfellow-2014
source_type: web-capture
ingested_at: 2026-08-14
---

# Generative Adversarial Networks (Goodfellow et al., 2014) — página abstract de arXiv

## Provenance
- Original location: `research/web/gan-goodfellow-2014/`
- Format: html (captura web de `talksmith:ingest` — `page.md` + `original.html` + `assets/`)
- Author / source (if known): Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio — arXiv (Université de Montréal)
- Date of original (if known): enviado el 10 de junio de 2014 (v1, única versión). Captura: 2026-08-14T17:02:50Z, HTTP 200, URL `https://arxiv.org/abs/1406.2661`

## Key claims

- **Es el paper fundacional.** Propone un marco para estimar modelos generativos mediante un *proceso antagónico* en el que se entrenan dos modelos simultáneamente: un generador `G` que captura la distribución de los datos, y un discriminador `D` que estima la probabilidad de que una muestra venga de los datos de entrenamiento y no de `G`.
- **El objetivo del generador es hacer errar al discriminador.** El procedimiento de entrenamiento de `G` consiste en maximizar la probabilidad de que `D` se equivoque.
- **El marco es un juego minimax de dos jugadores.** Esa es la frase exacta del abstract: *"This framework corresponds to a minimax two-player game."*
- **Existe una solución única en el espacio de funciones arbitrarias**: `G` recupera la distribución de los datos de entrenamiento y `D` vale 1/2 en todas partes. Es decir, el equilibrio es el punto en el que el discriminador ya no puede hacer mejor que tirar una moneda.
- **Todo el sistema se entrena con backpropagation** cuando `G` y `D` son perceptrones multicapa. No hacen falta cadenas de Markov ni redes de inferencia aproximada desenrolladas, ni durante el entrenamiento ni durante la generación de muestras — este es el argumento de venta frente a las máquinas de Boltzmann y los modelos basados en energía de la época.
- Los experimentos demuestran el potencial del marco mediante evaluación cualitativa y cuantitativa de las muestras generadas.

Datos bibliográficos para la cita:
- Autores: 8 (Goodfellow, Pouget-Abadie, Mirza, Xu, Warde-Farley, Ozair, Courville, Bengio)
- Año: 2014
- arXiv ID: **arXiv:1406.2661 [stat.ML]** (v1)
- DOI: `https://doi.org/10.48550/arXiv.1406.2661`
- Materias: Machine Learning (stat.ML); Machine Learning (cs.LG)
- Venue: la página de arXiv **no** declara *journal reference*. El paper se publicó en NIPS 2014, pero **esa información no está en esta captura** — no la tomes de acá.

## Definitions and terminology

- **Generador (`G`)**: modelo generativo que "captura la distribución de los datos" (*captures the data distribution*).
- **Discriminador (`D`)**: modelo discriminativo que "estima la probabilidad de que una muestra venga de los datos de entrenamiento y no de `G`" (*estimates the probability that a sample came from the training data rather than G*).
- **Proceso antagónico / adversarial process**: el esquema de entrenamiento simultáneo de ambas redes con objetivos opuestos.
- **Juego minimax de dos jugadores (minimax two-player game)**: la formalización teórica del entrenamiento. Este es el término que la clase reutiliza cuando habla del "juego" entre generador y discriminador. Ojo con la lectura: el abstract lo enuncia como *correspondencia* ("corresponds to"), no como metáfora didáctica.
- **Equilibrio / solución única**: `p_g = p_datos` y `D = 1/2` en todo punto. Es la definición formal de "el discriminador ya no distingue", que el deck y la página de AWS enuncian en prosa.
- El abstract **no** usa las palabras *latent space*, *espacio latente*, *ruido* ni *z*. El vector de ruido `z` aparece en el cuerpo del paper, que esta captura no contiene.

## Evidence and examples

- La captura es únicamente la **página de abstract** de arXiv. No trae figuras, tablas ni resultados numéricos: no hay valores de log-verosimilitud, ni datasets nombrados, ni comparaciones.
- El único dato de impacto visible en la página es un contador de **"59 blog links"** (trackbacks de arXiv). No es una métrica de citas.
- Enlaces de texto completo disponibles en la captura: PDF (`/pdf/1406.2661`), HTML experimental (`/html/1406.2661v1`), TeX source (`/src/1406.2661`).
- Índices externos enlazados: NASA ADS, Google Scholar, Semantic Scholar.

## Inconsistencies / open questions

- **Cifras del deck que esta fuente NO respalda (slide 12).** La clase afirma "70K+ citas" para este paper y le atribuye a Yann LeCun una cita elogiosa ("la idea más interesante de los últimos diez años en machine learning" o similar). **Ninguna de las dos cosas aparece en esta captura**, ni en ninguna de las otras trece del corpus. La página de arXiv no muestra conteo de citas; muestra 59 trackbacks de blogs y links a Google Scholar / Semantic Scholar, que sí llevan a conteos, pero esos conteos **no fueron capturados**. Para sostener el "70K+" hay que citar Google Scholar con fecha de consulta, y para la cita de LeCun hay que dar la fuente primaria (la respuesta de LeCun en Quora, 2016) — de lo contrario ambas quedan como afirmaciones sin respaldo en el material de la clase.
- **Ninguna de las 14 fuentes de `research/web/` respalda las cifras sueltas del deck**: Dice 0.9524 vs 0.9459 (slide 5), "+30% de precisión" (46), "los neurorradiólogos no distinguen en estudios ciegos" (43), "70K+ citas" (12) y la cita de LeCun (12). El asiento detallado de cada una queda en el registro más cercano (`sam-kirillov-2023.web.md` para el Dice, `aws-que-es-una-gan.web.md` para el +30%, `inception-score-salimans-2016.web.md` para el estudio ciego), pero conviene dejarlo dicho acá, en el registro raíz del linaje: **el deck no tiene fuente para ninguna de ellas.**
- **Gap de extracción**: la captura es la página `abs/`, no el paper. Si la clase quiere citar la formulación exacta del objetivo minimax (la ecuación con `E[log D(x)] + E[log(1 - D(G(z)))]`), el Algoritmo 1, o la Figura 1, hay que ir al PDF — no están en este registro.
- **El deck no nombra ningún dataset** pese a argumentar sobre datasets en cuatro slides. Este paper tampoco nombra datasets en su abstract, así que no sirve para cerrar ese hueco. Las fuentes que sí los nombran son `progan-…`, `fid-heusel-2017`, `inception-score-salimans-2016`, `cgan-…` y `sam-kirillov-2023`.

## Images / diagrams

La captura solo trajo chrome de la interfaz de arXiv. Ninguna imagen del paper.

  - Depiction: logotipo de arXiv en versión clara, SVG vectorial de 246.98 × 111.12, siete trazados en un grupo llamado "Primary Darkmode". Sin texto embebido en `<text>` — la palabra "arXiv" está convertida a curvas.
  - Why it matters: nada, es branding del sitio. Sirve solo como marca de procedencia de la captura.
  - Transcribed text: (el logo dibuja la palabra "arXiv"; no hay texto seleccionable en el archivo). `alt="archive"`.
  - Depiction: ícono social de BibSonomy, 16×16 px, dos huesos cruzados en rojo sobre fondo transparente.
  - Why it matters: chrome de UI, sin valor de contenido.
  - Transcribed text: ninguno. `alt="BibSonomy"`.
  - Depiction: ícono social de Reddit, 16×16 px, la mascota Snoo (cara redonda con antena) en naranja y blanco.
  - Why it matters: chrome de UI, sin valor de contenido.
  - Transcribed text: ninguno. `alt="Reddit"`.

## Raw / preserved excerpts

Abstract completo, verbatim (inglés original):

> Abstract: We propose a new framework for estimating generative models via an adversarial process, in which we simultaneously train two models: a generative model G that captures the data distribution, and a discriminative model D that estimates the probability that a sample came from the training data rather than G. The training procedure for G is to maximize the probability of D making a mistake. This framework corresponds to a minimax two-player game. In the space of arbitrary functions G and D, a unique solution exists, with G recovering the training data distribution and D equal to 1/2 everywhere. In the case where G and D are defined by multilayer perceptrons, the entire system can be trained with backpropagation. There is no need for any Markov chains or unrolled approximate inference networks during either training or generation of samples. Experiments demonstrate the potential of the framework through qualitative and quantitative evaluation of the generated samples.

Bloque bibliográfico verbatim:

> Statistics > Machine Learning
> **arXiv:1406.2661** (stat) [Submitted on 10 Jun 2014]
> Title: Generative Adversarial Networks
> Authors: Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio
> Subjects: Machine Learning (stat.ML); Machine Learning (cs.LG)
> Cite as: arXiv:1406.2661 [stat.ML] (or arXiv:1406.2661v1 [stat.ML] for this version)
> https://doi.org/10.48550/arXiv.1406.2661

> Submission history
> From: Ian Goodfellow
> **[v1]** Tue, 10 Jun 2014 18:58:17 UTC (1,257 KB)
