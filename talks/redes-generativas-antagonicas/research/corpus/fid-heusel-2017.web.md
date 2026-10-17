---
source_file: fid-heusel-2017
source_type: web-capture
ingested_at: 2026-08-14
---

# GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium — el paper de FID (Heusel et al., 2017) — página abstract de arXiv

## Provenance
- Original location: `research/web/fid-heusel-2017/`
- Format: html (captura web de `talksmith:ingest` — `page.md` + `original.html` + `assets/`)
- Author / source (if known): Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, Sepp Hochreiter — Institute of Bioinformatics, JKU Linz (la afiliación no figura en la captura; el repo `bioinf-jku` la delata) — arXiv
- Date of original (if known): enviado el 26 de junio de 2017 (v1), última revisión 12 de enero de 2018 (v6, la capturada). Captura: 2026-08-14T17:02:59Z, HTTP 200, URL `https://arxiv.org/abs/1706.08500`

## Key claims

- **Ojo con el título: el paper no es "el paper de FID".** Es el paper del TTUR (*two time-scale update rule*); FID entra como herramienta de evaluación necesaria para medir lo que el TTUR mejora. La clase lo cita por FID, y está bien, pero la cita correcta es esta y el título es el que es.
- **Planteo**: las GANs son excelentes generando imágenes realistas con modelos complejos donde la máxima verosimilitud es inviable, **pero la convergencia del entrenamiento GAN todavía no había sido probada.**
- **Proponen el TTUR**: una **tasa de aprendizaje individual para el discriminador y para el generador**, con descenso de gradiente estocástico sobre funciones de pérdida GAN arbitrarias.
- **Prueban, usando teoría de aproximación estocástica, que el TTUR converge bajo supuestos suaves a un equilibrio de Nash local estacionario.** Es la primera garantía de convergencia del corpus.
- **La convergencia se extiende a Adam**, para el cual prueban que sigue la dinámica de una **bola pesada con fricción** y por lo tanto prefiere mínimos planos del paisaje objetivo.
- **Introducen la "Fréchet Inception Distance" (FID)** para evaluar el desempeño de las GANs en generación de imágenes, **explícitamente porque captura mejor que el Inception Score la similitud entre imágenes generadas y reales.** Frase verbatim: *"which captures the similarity of generated images to real ones better than the Inception Score."*
- **Resultados**: el TTUR mejora el aprendizaje de DCGANs e Improved Wasserstein GANs (WGAN-GP), superando al entrenamiento GAN convencional en CelebA, CIFAR-10, SVHN, LSUN Bedrooms y el One Billion Word Benchmark.

Datos bibliográficos para la cita:
- Autores: Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, Sepp Hochreiter
- Año: 2017
- arXiv ID: **arXiv:1706.08500 [cs.LG]** (v6)
- DOI: `https://doi.org/10.48550/arXiv.1706.08500`
- Materias: Machine Learning (cs.LG); Machine Learning (stat.ML)
- **Journal reference (impresa en la página, a diferencia de las demás capturas): Advances in Neural Information Processing Systems 30 (NIPS 2017).**
- Implementaciones: `https://github.com/bioinf-jku/TTUR`

## Definitions and terminology

**Qué mide exactamente FID** — el deck (slide 50) llama a FID e IS "aproximaciones imperfectas" sin explicar por qué. Esto es lo que la captura sí permite afirmar, y dónde termina:

- **FID (Fréchet Inception Distance)**: definida en el abstract únicamente por su propósito — **"captura la similitud de las imágenes generadas con las reales"**. Es decir: **compara la distribución de las imágenes generadas contra la distribución de las imágenes reales.** Necesita **las dos** distribuciones.
- **La mecánica** (features de una red Inception, ajuste de una gaussiana a cada conjunto, distancia de Fréchet entre las dos gaussianas — de ahí el nombre) **no está en esta captura**: el abstract solo da el nombre y el propósito. El nombre mismo es la pista: *Fréchet* es la distancia entre distribuciones, *Inception* es de dónde salen las features.
- **La diferencia esencial con el Inception Score, que es lo que el deck necesita**: **FID mira las imágenes reales; el Inception Score no.** El IS se calcula únicamente sobre las muestras generadas (ver `inception-score-salimans-2016.web.md`); FID las compara contra un conjunto de referencia real. Por eso FID detecta que un generador produce imágenes nítidas y variadas **pero distintas de los datos**, y el IS no puede.
- **Corolario práctico para la slide 50**: FID **más bajo es mejor** (es una distancia); el Inception Score **más alto es mejor** (es una divergencia esperada). Van en direcciones opuestas. Esto no está dicho en la captura, pero se deduce sin esfuerzo de que una sea una distancia entre distribuciones.
- **TTUR (two time-scale update rule)**: dos tasas de aprendizaje, una por red. Nombre y definición del abstract.
- **Equilibrio de Nash local estacionario (stationary local Nash equilibrium)**: el punto de convergencia que prueban. Es la formalización rigurosa del "equilibrio" que Goodfellow enuncia como `D = 1/2` y que AWS describe en prosa.
- **Bola pesada con fricción (heavy ball with friction)**: la dinámica que prueban para Adam; explica su preferencia por mínimos planos.
- **Mínimos planos (flat minima)**: mínimos de la función objetivo con curvatura baja alrededor, asociados a mejor generalización. Hochreiter, uno de los autores, es quien introdujo el concepto en los 90.

## Evidence and examples

- **Datasets nombrados — cinco, y es el registro más rico del corpus en este punto: CelebA, CIFAR-10, SVHN, LSUN Bedrooms y el One Billion Word Benchmark.** Nótese que el último es de **texto**, no de imágenes: el TTUR se evalúa también fuera de visión.
- **Arquitecturas sobre las que se evalúa**: DCGAN (ver `dcgan-radford-2015.web.md`) e Improved Wasserstein GAN (WGAN-GP).
- **Resultado**: el TTUR supera al entrenamiento GAN convencional en los cinco conjuntos. **Sin valores numéricos de FID en la captura.**
- **Código**: `https://github.com/bioinf-jku/TTUR` — la implementación de referencia de FID que después usó toda la comunidad.
- **Venue impreso**: NIPS 2017 (NeurIPS 30). Es la única captura del corpus con *journal reference* explícita.

## Inconsistencies / open questions

- **[Punto 4 del encargo] Cinco datasets nombrados: CelebA, CIFAR-10, SVHN, LSUN Bedrooms, One Billion Word Benchmark.** Se registra explícitamente porque el deck argumenta sobre datasets en cuatro slides sin nombrar ni uno. Este es el mejor contraejemplo del corpus junto con `progan-…` y `inception-score-…`: hasta una métrica se valida contra conjuntos nombrados.
- **"Aproximaciones imperfectas" (slide 50) sin fundamentar.** El deck califica así a FID e IS y no explica por qué. Lo que **esta captura sí habilita a decir**: (a) FID nació explícitamente como corrección al Inception Score, por lo que el propio paper que la introduce está afirmando que la métrica anterior era insuficiente — la imperfección es parte del linaje, no una opinión externa; (b) FID compara distribuciones vía features de una red Inception preentrenada en ImageNet, y **esa dependencia es la fuente de su imperfección** (mide "parecido a los datos según lo que ImageNet considera relevante"). El punto (b) **no está en la captura** — el abstract no describe la mecánica. Si el deck quiere sostener "imperfectas" con rigor, hace falta el paper, o mejor, la literatura crítica posterior (Barratt & Sharma 2018 sobre IS; los trabajos sobre el sesgo del estimador de FID), **que no está en este corpus**.
- **El paper no es sobre FID.** Si el deck lo cita como "Heusel et al., el paper de FID", la referencia funciona pero el título va a sorprender a cualquiera que lo abra. Vale la aclaración de una línea.
- **Sin valores numéricos**: el abstract dice "outperforming" sin cifras. Si el deck muestra una tabla de FID, no sale de acá.
- **Gap de extracción**: sin la definición formal de FID, sin las tablas comparativas, sin las pruebas de convergencia. Todo en el PDF.

## Images / diagrams


  - Depiction: logotipo de arXiv en versión clara, SVG vectorial de 246.98 × 111.12, siete trazados agrupados. Texto convertido a curvas.
  - Why it matters: branding del sitio, sin valor de contenido.
  - Transcribed text: (el logo dibuja "arXiv"; sin texto seleccionable). `alt="archive"`.
  - Depiction: ícono decorativo "smileybones" de arXiv, SVG de 612×639 construido enteramente con polígonos de estética pixel-art en gris `#999`: cuatro grupos angulares en las esquinas (huesos estilizados) que enmarcan una carita. Aparece en el pie del sitio, en el bloque de donaciones/branding de arXiv.
  - Why it matters: chrome de UI. Sin relación con el paper ni con FID. Se registra solo porque es el único asset que distingue esta captura de las otras diez de arXiv.
  - Transcribed text: `<title>smileybones-standard-small</title>`. Sin otro texto. `alt=""` (vacío en el HTML original — decorativo por declaración propia).
  - Depiction: ícono social de BibSonomy, 16×16 px, huesos cruzados en rojo.
  - Why it matters: chrome de UI.
  - Transcribed text: ninguno. `alt="BibSonomy"`.
  - Depiction: ícono social de Reddit, 16×16 px, mascota Snoo en naranja y blanco.
  - Why it matters: chrome de UI.
  - Transcribed text: ninguno. `alt="Reddit"`.

## Raw / preserved excerpts

Abstract completo, verbatim (inglés original). **La oración sobre FID es la cita para la slide 50:**

> Abstract: Generative Adversarial Networks (GANs) excel at creating realistic images with complex models for which maximum likelihood is infeasible. However, the convergence of GAN training has still not been proved. We propose a two time-scale update rule (TTUR) for training GANs with stochastic gradient descent on arbitrary GAN loss functions. TTUR has an individual learning rate for both the discriminator and the generator. Using the theory of stochastic approximation, we prove that the TTUR converges under mild assumptions to a stationary local Nash equilibrium. The convergence carries over to the popular Adam optimization, for which we prove that it follows the dynamics of a heavy ball with friction and thus prefers flat minima in the objective landscape. For the evaluation of the performance of GANs at image generation, we introduce the "Fréchet Inception Distance" (FID) which captures the similarity of generated images to real ones better than the Inception Score. In experiments, TTUR improves learning for DCGANs and Improved Wasserstein GANs (WGAN-GP) outperforming conventional GAN training on CelebA, CIFAR-10, SVHN, LSUN Bedrooms, and the One Billion Word Benchmark.

Bloque bibliográfico verbatim:

> Computer Science > Machine Learning
> **arXiv:1706.08500** (cs) [Submitted on 26 Jun 2017 (v1), last revised 12 Jan 2018 (this version, v6)]
> Title: GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium
> Authors: Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, Sepp Hochreiter
> Comments: Implementations are available at: https://github.com/bioinf-jku/TTUR
> Subjects: Machine Learning (cs.LG); Machine Learning (stat.ML)
> Cite as: arXiv:1706.08500 [cs.LG] (or arXiv:1706.08500v6 [cs.LG] for this version)
> https://doi.org/10.48550/arXiv.1706.08500
> **Journal reference: Advances in Neural Information Processing Systems 30 (NIPS 2017)**

> Submission history
> From: Martin Heusel
> **[v1]** Mon, 26 Jun 2017 17:45:23 UTC (9,117 KB)
> **[v2]** Tue, 27 Jun 2017 15:06:08 UTC (9,116 KB)
> **[v3]** Wed, 28 Jun 2017 16:36:56 UTC (4,192 KB)
> **[v4]** Thu, 13 Jul 2017 09:15:29 UTC (4,201 KB)
> **[v5]** Wed, 8 Nov 2017 16:25:21 UTC (5,435 KB)
> **[v6]** Fri, 12 Jan 2018 14:05:44 UTC (5,435 KB)
