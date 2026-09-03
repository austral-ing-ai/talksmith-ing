---
source_file: research/web/attention-is-all-you-need/
source_type: web-capture
ingested_at: 2026-08-14
---

# Attention Is All You Need (arXiv:1706.03762) — página de abstract

## Provenance
- Original location: `research/web/attention-is-all-you-need/`
- Format: web-capture (`page.md` extraído de `original.html`; assets en `assets/`)
- URL: https://arxiv.org/abs/1706.03762
- Título de la captura: `[1706.03762] Attention Is All You Need`
- HTTP status: 200 · byte_size: 43644
- fetched_at: 2026-08-14T16:38:23Z
- Author / source (if known): Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin (Google Brain / Google Research / Univ. of Toronto — la afiliación no aparece en la página de abstract)
- Date of original (if known): enviado el 12 de junio de 2017 (v1); última revisión 2 de agosto de 2023 (v7, la versión capturada)
- Identificadores: arXiv:1706.03762 [cs.CL] · DOI https://doi.org/10.48550/arXiv.1706.03762
- Materias: Computation and Language (cs.CL); Machine Learning (cs.LG)
- Comentarios del autor en arXiv: "15 pages, 5 figures"

## Key claims

Las afirmaciones siguientes salen todas del abstract, que es lo único de contenido sustantivo que trae la página capturada.

- **El punto de partida que el paper viene a romper**: los modelos dominantes de transducción de secuencias eran redes recurrentes o convolucionales complejas, en configuración *encoder-decoder*, y los mejores además conectaban encoder y decoder mediante un mecanismo de atención. La atención existía, pero como accesorio de la recurrencia.
- **La propuesta**: una arquitectura de red nueva y simple, el **Transformer**, basada *únicamente* en mecanismos de atención, que prescinde por completo de recurrencia y de convoluciones ("dispensing with recurrence and convolutions entirely"). Este es exactamente el giro que la clase resume como "cambió todo".
- **Doble ganancia, no compromiso**: los experimentos en dos tareas de traducción automática muestran modelos superiores en calidad *y a la vez* más paralelizables y con tiempo de entrenamiento significativamente menor. La paralelización es la consecuencia directa de eliminar la recurrencia: sin dependencia secuencial, la secuencia entera se procesa de una.
- **Resultado en WMT 2014 inglés→alemán**: 28.4 BLEU, mejorando los mejores resultados existentes —incluidos *ensembles*— por más de 2 BLEU.
- **Resultado en WMT 2014 inglés→francés**: 41.8 BLEU, nuevo estado del arte para modelo único, tras 3.5 días de entrenamiento sobre ocho GPUs — "a small fraction of the training costs of the best models from the literature".
- **Generalización fuera de traducción**: el Transformer se aplica con éxito a *English constituency parsing*, tanto con datos de entrenamiento abundantes como limitados. Es decir, la arquitectura no está atada a la tarea de traducción.
- **Sobre encoder + decoder** (relevante para la slide 27 del deck): el paper original efectivamente presenta el Transformer en configuración encoder + decoder — el abstract lo enmarca dentro del paradigma de "sequence transduction models ... in an encoder-decoder configuration" y propone la arquitectura para ese escenario de traducción. La afirmación complementaria de la clase, que los LLMs modernos (GPT, LLaMA, Claude) usan solo decoder, **no proviene de este paper ni de esta captura**: es posterior a 2017 y hay que sostenerla con otra fuente.

## Definitions and terminology

La página de abstract nombra pocos términos y define aún menos. Lo que sí queda anclado:

- **Transformer** — la arquitectura propuesta; descrita en el abstract como "a new simple network architecture ... based solely on attention mechanisms".
- **Sequence transduction model** — modelo que convierte una secuencia de entrada en una secuencia de salida (traducción, parsing). El término encuadra el problema.
- **Encoder-decoder configuration** — el esquema de dos bloques (uno que codifica la entrada, otro que genera la salida) que era el estándar previo y que el Transformer adopta, cambiándole el motor interno.
- **Attention mechanism** — mencionado como lo que los mejores modelos previos usaban para conectar encoder y decoder, y como el único componente sobre el que se apoya el Transformer.
- **Parallelizable** — propiedad que el abstract reivindica explícitamente frente a la recurrencia.
- **BLEU** — métrica de calidad de traducción automática usada para reportar los resultados (la página no la define).

**Advertencia para el uso en clase**: los términos *self-attention*, *multi-head attention*, *positional encoding*, *scaled dot-product attention*, *layer normalization* y *masked attention* — que son el vocabulario que la clase reutiliza — **no aparecen en esta captura**. Están en el cuerpo del paper, no en el abstract. Ver `Inconsistencies / open questions`.

## Evidence and examples

| Tarea | Métrica reportada | Comparación declarada |
|---|---|---|
| WMT 2014 English→German | 28.4 BLEU | > 2 BLEU sobre los mejores resultados previos, incluidos ensembles |
| WMT 2014 English→French | 41.8 BLEU | nuevo estado del arte para modelo único |
| English constituency parsing | sin número en el abstract | "generalizes well", con datos abundantes y limitados |

- **Costo de entrenamiento** (el dato más citable de la clase): 3.5 días sobre ocho GPUs para el modelo de inglés→francés, descrito como una fracción pequeña del costo de los mejores modelos de la literatura. La página no dice qué GPUs eran ni el costo absoluto.
- **Tamaño del paper**: 15 páginas, 5 figuras (campo *Comments* de arXiv). Las 5 figuras — entre ellas el diagrama de arquitectura que todo el mundo reproduce — **no están en esta captura**.
- **Huella del paper**: la página lista 123 *blog links* (trackbacks) registrados por arXiv, y siete versiones publicadas entre junio de 2017 y agosto de 2023. Sirve como señal indirecta de impacto, no como evidencia técnica.

## Inconsistencies / open questions

- **La captura es la página de abstract, no el paper.** arXiv `/abs/` trae metadatos + abstract y nada más. Todo lo que la clase quiera decir sobre el mecanismo interno — cómo se calcula la atención, qué son las cabezas múltiples, cómo se codifica la posición sin recurrencia, el diagrama de bloques — **no está en este corpus**. Hay que traerlo del PDF (`/pdf/1706.03762`), de la versión HTML experimental, o de otra fuente.
- **La afirmación "decoder-only" de la slide 27 no tiene respaldo aquí.** El paper es de 2017; GPT, LLaMA y Claude son posteriores. Si la slide la mantiene, necesita otra cita.
- **La página no reporta afiliaciones ni venue formal.** El Transformer se publicó en NIPS 2017, pero el campo *Journal ref* de arXiv está vacío en esta captura — no hay campo `Comments` que mencione la conferencia (a diferencia de las capturas de ELMo y GRU, que sí la traen). Si el deck cita "NIPS 2017", el dato viene de fuera del corpus.
- **Versión capturada = v7 (2023).** El abstract puede diferir en detalles menores del v1 de 2017. Los números BLEU son los mismos que circulan históricamente, pero conviene saber que se está citando una revisión tardía.
- La captura no discute limitaciones, costo de inferencia, escalado ni longitud de contexto — temas que la clase probablemente toque.

## Images / diagrams

La página no trae ninguna figura del paper. Los tres archivos que arrastró la captura son elementos de interfaz de arXiv, no contenido. Se conservan por completitud del corpus; **ninguno tiene valor didáctico para el deck**.



## Raw / preserved excerpts

**Abstract, verbatim (inglés, tal como aparece en la captura):**

> Abstract:The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

**Encabezado bibliográfico, verbatim:**

> # Computer Science > Computation and Language
>
> **arXiv:1706.03762** (cs)  [Submitted on 12 Jun 2017 ([v1](https://arxiv.org/abs/1706.03762v1)), last revised 2 Aug 2023 (this version, v7)]
>
> # Title:Attention Is All You Need
>
> Authors:Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin

**Bloque de metadatos, verbatim:**

> Comments: 15 pages, 5 figures Subjects: Computation and Language (cs.CL); Machine Learning (cs.LG) Cite as: [arXiv:1706.03762](https://arxiv.org/abs/1706.03762) [cs.CL] (or [arXiv:1706.03762v7](https://arxiv.org/abs/1706.03762v7) [cs.CL] for this version) [https://doi.org/10.48550/arXiv.1706.03762](https://doi.org/10.48550/arXiv.1706.03762) Focus to learn more  arXiv-issued DOI via DataCite

**Historial de versiones, verbatim:**

> From: Llion Jones
> **[v1]** Mon, 12 Jun 2017 17:57:34 UTC (1,102 KB)
> **[v2]** Mon, 19 Jun 2017 16:49:45 UTC (1,125 KB)
> **[v3]** Tue, 20 Jun 2017 05:20:02 UTC (1,125 KB)
> **[v4]** Fri, 30 Jun 2017 17:29:30 UTC (1,124 KB)
> **[v5]** Wed, 6 Dec 2017 03:30:32 UTC (1,124 KB)
> **[v6]** Mon, 24 Jul 2023 00:48:54 UTC (1,124 KB)
> **[v7]** Wed, 2 Aug 2023 00:41:18 UTC (1,124 KB)

**Enlaces de acceso al texto completo (lo que la captura *no* bajó):**

> - [View PDF](/pdf/1706.03762)
> - [HTML (experimental)](https://arxiv.org/html/1706.03762v7)
> - [TeX Source](/src/1706.03762)

**Referencia DBLP, verbatim:**

> [listing](https://dblp.uni-trier.de/db/journals/corr/corr1706.html#VaswaniSPUJGKP17) | [bibtex](https://dblp.uni-trier.de/rec/bibtex/journals/corr/VaswaniSPUJGKP17)

**Señal de impacto, verbatim:**

> ### [123 blog links](/tb/1706.03762)
