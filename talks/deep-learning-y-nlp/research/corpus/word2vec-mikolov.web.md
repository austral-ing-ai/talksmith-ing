---
source_file: research/web/word2vec-mikolov/
source_type: web-capture
ingested_at: 2026-08-14
---

# Efficient Estimation of Word Representations in Vector Space (arXiv:1301.3781) — página de abstract

## Provenance
- Original location: `research/web/word2vec-mikolov/`
- Format: web-capture (`page.md` extraído de `original.html`; assets en `assets/`)
- URL: https://arxiv.org/abs/1301.3781
- Título de la captura: `[1301.3781] Efficient Estimation of Word Representations in Vector Space`
- HTTP status: 200 · byte_size: 40906
- fetched_at: 2026-08-14T16:38:23Z
- Author / source (if known): Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean (Google — la afiliación no figura en la página de abstract)
- Date of original (if known): enviado el 16 de enero de 2013 (v1); última revisión 7 de septiembre de 2013 (v3, la versión capturada)
- Identificadores: arXiv:1301.3781 [cs.CL] · DOI https://doi.org/10.48550/arXiv.1301.3781
- Materias: Computation and Language (cs.CL)
- Comentarios del autor en arXiv: (campo vacío — no hay número de páginas ni venue declarado)

## Key claims

Todo lo sustantivo de esta captura está en el abstract; el resto de la página es navegación de arXiv.

- **La propuesta**: dos arquitecturas de modelo nuevas para computar representaciones vectoriales continuas de palabras a partir de conjuntos de datos muy grandes. Este es el paper que la clase cita como "Word2Vec" — el nombre comercial no aparece en el abstract, sólo las dos arquitecturas.
- **Cómo se evalúa la calidad**: mediante una tarea de *similitud entre palabras*, comparando contra las técnicas previas de mejor rendimiento, basadas en distintos tipos de redes neuronales.
- **El resultado doble**: mejoras grandes en exactitud *a un costo computacional mucho menor*. El paper no compra precisión con cómputo; gana en las dos dimensiones a la vez.
- **La cifra concreta**: menos de un día para aprender vectores de palabras de alta calidad sobre un conjunto de 1.600 millones de palabras.
- **Estado del arte**: los vectores obtenidos dan rendimiento estado-del-arte en el conjunto de prueba propio de los autores para medir similitudes sintácticas *y* semánticas. La distinción sintáctico/semántico es de los autores y es la que sostiene los ejemplos de analogías que la clase suele mostrar.
- **Lo que respalda la slide 16 / 18** ("primer método que aprende embeddings automáticamente", "una palabra se define por la compañía que tiene"): el abstract respalda la primera mitad de forma *indirecta* — habla de "computing continuous vector representations of words from very large data sets" aprendidas, no diseñadas a mano, y de una mejora grande sobre las técnicas neuronales previas. Pero **no reclama ser el primero**, y de hecho se compara explícitamente contra métodos neuronales anteriores, es decir, reconoce que había predecesores. La formulación distribucional ("una palabra se define por la compañía que tiene", la hipótesis de Firth) **no aparece en el abstract**.
- **Lo que respalda la slide 28** ("promedia vectores de contexto"; "explícitamente *no* es un modelo de lenguaje"): **el abstract no dice ninguna de las dos cosas.** El promediado de vectores de contexto es la mecánica de la arquitectura CBOW, descrita en el cuerpo del paper. Y el abstract nunca contrasta Word2Vec con un modelo de lenguaje. Ambas afirmaciones son correctas respecto del paper completo, pero no se pueden citar contra esta captura. Ver `Inconsistencies / open questions`.

## Definitions and terminology

- **Continuous vector representations of words** — la formulación del abstract para lo que la clase llama *embeddings*: representar cada palabra como un vector denso en un espacio continuo.
- **Model architecture** — el abstract propone "two novel model architectures"; no las nombra en el texto capturado.
- **Word similarity task** — la tarea de evaluación: medir cuán bien los vectores capturan la cercanía entre palabras.
- **Syntactic and semantic word similarities** — la doble dimensión de la evaluación: relaciones de forma (plural, conjugación) y relaciones de significado (capital-de, género).
- **Computational cost** — eje explícito de comparación contra los métodos previos.

**Advertencia para el uso en clase**: los nombres **CBOW** (*Continuous Bag-of-Words*) y **skip-gram**, que son el vocabulario que la clase reutiliza, **no aparecen en esta captura** — el abstract dice "two novel model architectures" sin nombrarlas. Tampoco aparecen *hierarchical softmax*, *negative sampling*, *word analogy*, ni la aritmética vectorial (`rey − hombre + mujer ≈ reina`). Todo eso está en el cuerpo del paper.

## Evidence and examples

| Dato | Valor reportado en el abstract |
|---|---|
| Tamaño del corpus de entrenamiento | 1.600 millones de palabras (1.6 billion words) |
| Tiempo de entrenamiento | menos de un día |
| Ganancia de exactitud | "large improvements in accuracy" (sin número) |
| Costo computacional | "much lower" (sin número) |
| Similitudes sintácticas y semánticas | rendimiento estado-del-arte en el test set propio de los autores |

- **La captura no trae ni una sola cifra de exactitud.** "Large improvements" y "much lower computational cost" son las únicas caracterizaciones. Si el deck quiere un porcentaje concreto, no está acá.
- **Peso del envío**: v1 pesaba 16 KB, v2 y v3 pesan 48 KB — un paper corto y sin figuras pesadas, consistente con un trabajo de 12 páginas.
- **Huella del paper**: 67 *blog links* (trackbacks) registrados por arXiv; tres versiones entre enero y septiembre de 2013.

## Inconsistencies / open questions

- **La captura es la página de abstract, no el paper.** Todo lo que la clase quiera decir sobre *cómo funciona* Word2Vec — CBOW promediando los vectores de contexto, skip-gram prediciendo el contexto desde la palabra, la ventana deslizante, las analogías vectoriales — **no está en este corpus**. Hay que traerlo del PDF (`/pdf/1301.3781`) o de otra fuente.
- **La afirmación "es el primero" (slide 16) es más fuerte de lo que el abstract respalda.** El propio abstract se compara con "the previously best performing techniques based on different types of neural networks": había métodos neuronales antes. Word2Vec es el que *popularizó* los embeddings aprendidos y los hizo baratos, no el que los inventó. Si la slide dice "primer método", conviene matizarla o citarla contra otra fuente.
- **"No es un modelo de lenguaje" (slide 28) no sale de acá.** Es una distinción pedagógicamente valiosa y verdadera, pero el abstract no la hace; ni siquiera menciona la expresión *language model*. Necesita otra cita o presentarse como aclaración del docente.
- **"Una palabra se define por la compañía que tiene"** es la hipótesis distribucional de Firth (1957), no una frase de este paper. No aparece en la captura.
- **El campo `Comments` está vacío** — a diferencia de las capturas de ELMo (NAACL 2018) y GRU (EMNLP 2014), esta no declara venue. El trabajo se presentó en el workshop de ICLR 2013, pero ese dato **no está en el corpus**.
- La captura no dice nada sobre las limitaciones que la clase sí necesita nombrar para motivar ELMo y los Transformers: un vector fijo por palabra, sin sensibilidad al contexto, y por lo tanto incapaz de manejar polisemia.

## Images / diagrams

La página no trae ninguna figura del paper. Los tres archivos capturados son cromo de interfaz de arXiv — idénticos byte a byte a los de las otras tres capturas de arXiv de este corpus. Se conservan por completitud; **ninguno tiene valor didáctico**.



## Raw / preserved excerpts

**Abstract, verbatim (inglés, tal como aparece en la captura):**

> Abstract:We propose two novel model architectures for computing continuous vector representations of words from very large data sets. The quality of these representations is measured in a word similarity task, and the results are compared to the previously best performing techniques based on different types of neural networks. We observe large improvements in accuracy at much lower computational cost, i.e. it takes less than a day to learn high quality word vectors from a 1.6 billion words data set. Furthermore, we show that these vectors provide state-of-the-art performance on our test set for measuring syntactic and semantic word similarities.

**Encabezado bibliográfico, verbatim:**

> # Computer Science > Computation and Language
>
> **arXiv:1301.3781** (cs)  [Submitted on 16 Jan 2013 ([v1](https://arxiv.org/abs/1301.3781v1)), last revised 7 Sep 2013 (this version, v3)]
>
> # Title:Efficient Estimation of Word Representations in Vector Space
>
> Authors:Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean

**Bloque de metadatos, verbatim:**

> Subjects: Computation and Language (cs.CL) Cite as: [arXiv:1301.3781](https://arxiv.org/abs/1301.3781) [cs.CL] (or [arXiv:1301.3781v3](https://arxiv.org/abs/1301.3781v3) [cs.CL] for this version) [https://doi.org/10.48550/arXiv.1301.3781](https://doi.org/10.48550/arXiv.1301.3781) Focus to learn more  arXiv-issued DOI via DataCite

**Historial de versiones, verbatim:**

> From: Tomas Mikolov
> **[v1]** Wed, 16 Jan 2013 18:24:43 UTC (16 KB)
> **[v2]** Thu, 7 Mar 2013 21:40:37 UTC (48 KB)
> **[v3]** Sat, 7 Sep 2013 00:30:40 UTC (48 KB)

**Enlaces de acceso al texto completo (lo que la captura *no* bajó):**

> - [View PDF](/pdf/1301.3781)
> - [HTML (experimental)](https://arxiv.org/html/1301.3781v3)

**Señal de impacto, verbatim:**

> ### [67 blog links](/tb/1301.3781)
