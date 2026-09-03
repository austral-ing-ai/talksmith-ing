---
source_file: rag-lewis-2020
source_type: web-capture
ingested_at: 2026-08-14
---

# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (Lewis et al., arXiv:2005.11401 / NeurIPS 2020)

## Provenance
- Original location: `research/web/rag-lewis-2020/`
- Format: html (página de abstract de arXiv, no el PDF del paper).
- URL: https://arxiv.org/abs/2005.11401
- Autores: Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela (12 autores; Facebook AI Research / University College London / New York University en la afiliación del paper original).
- Fecha del original: enviado el 22 de mayo de 2020 (v1); última revisión 12 de abril de 2021 (v4, la capturada). **Aceptado en NeurIPS 2020.** Categorías: cs.CL (principal), cs.LG. DOI: 10.48550/arXiv.2005.11401.
- `http_status`: 200 · `fetched_at`: 2026-08-14T16:57:34Z.
- **Alcance de la captura**: es la página `/abs/` de arXiv — abstract completo, autoría, fechas, historial de versiones. **No incluye el cuerpo del paper**: no hay tablas de resultados, ni la arquitectura DPR + BART, ni las cifras de Natural Questions / TriviaQA / WebQuestions. Este es *el* paper que acuñó el término RAG, así que sirve como cita canónica de origen; para números hay que ir al PDF.

## Key claims

Todos verificables contra el abstract verbatim (ver *Raw / preserved excerpts*):

- **Los modelos de lenguaje preentrenados almacenan conocimiento factual en sus parámetros** y alcanzan el estado del arte cuando se los ajusta finamente en tareas de NLP posteriores. Este es el punto de partida, no la crítica.
- **Pero su capacidad de acceder y manipular ese conocimiento con precisión es limitada**, y por eso en tareas intensivas en conocimiento su rendimiento queda por detrás de arquitecturas específicas de la tarea. Esta es la formulación original y precisa del problema que la clase suele resumir como "el modelo alucina".
- **Dos problemas abiertos identificados explícitamente: dar procedencia a las decisiones del modelo y actualizar su conocimiento del mundo.** Trazabilidad y actualización, no sólo exactitud. Es la mejor justificación de RAG para un contexto biomédico, donde citar la fuente no es opcional.
- **La propuesta: combinar memoria paramétrica y memoria no paramétrica.** Un modelo preentrenado con un mecanismo de acceso diferenciable a memoria explícita no paramétrica puede resolver el problema, pero hasta entonces sólo se había investigado para tareas extractivas. RAG lo extiende a generación.
- **Instanciación concreta**: la memoria paramétrica es un modelo seq2seq preentrenado; la memoria no paramétrica es **un índice vectorial denso de Wikipedia**, accedido con un recuperador neuronal preentrenado. Esta es la arquitectura original: retriever denso + generador seq2seq, entrenados en conjunto con una receta de fine-tuning de propósito general.
- **Se comparan dos formulaciones de RAG**: una que condiciona sobre los mismos pasajes recuperados a lo largo de toda la secuencia generada (RAG-Sequence), y otra que puede usar pasajes distintos por cada token (RAG-Token). Distinción fina que casi nunca aparece en las presentaciones de RAG y que puede ser un buen detalle de color.
- **Resultados reportados en el abstract**: estado del arte en **tres tareas de QA de dominio abierto**, superando tanto a modelos seq2seq puramente paramétricos como a arquitecturas específicas de recuperar-y-extraer.
- **En tareas de generación de lenguaje, los modelos RAG generan lenguaje más específico, más diverso y más factual** que un baseline seq2seq puramente paramétrico del estado del arte.

## Definitions and terminology

**Retrieval-Augmented Generation (RAG).** El término se acuña aquí. Definición del abstract: *"models which combine pre-trained parametric and non-parametric memory for language generation"*. Nótese que en la definición original RAG es **una receta de fine-tuning de propósito general para una clase de modelos**, no una arquitectura de aplicación (*"We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG)"*). El uso actual de "RAG" — un pipeline de chunking + embeddings + búsqueda + prompt, sin entrenar nada — es una deriva posterior del término. Vale la pena decirlo en clase: cuando alguien dice "RAG" hoy, casi nunca se refiere a lo que este paper hizo.

**Memoria paramétrica.** El conocimiento almacenado en los pesos del modelo. Cita: *"Large pre-trained language models have been shown to store factual knowledge in their parameters"*.

**Memoria no paramétrica.** Conocimiento almacenado fuera de los pesos, en una estructura consultable. En este paper: *"a dense vector index of Wikipedia, accessed with a pre-trained neural retriever"*.

**Mecanismo de acceso diferenciable.** *"Pre-trained models with a differentiable access mechanism to explicit non-parametric memory"* — la recuperación forma parte del grafo de cómputo y se puede entrenar de punta a punta. Es la diferencia técnica de fondo con un pipeline de RAG moderno, donde el retriever es una caja negra externa al modelo.

**Tareas intensivas en conocimiento (*knowledge-intensive NLP tasks*).** Las tareas donde el rendimiento depende de hechos concretos que el modelo debe conocer o consultar, y donde los LLM puros quedan por detrás de arquitecturas especializadas.

**RAG-Sequence vs. RAG-Token.** Las dos formulaciones comparadas: *"one which conditions on the same retrieved passages across the whole generated sequence, the other can use different passages per token"*. El abstract no las nombra con esas etiquetas — los nombres vienen del cuerpo del paper — pero las describe inequívocamente.

**Arquitecturas de recuperar-y-extraer (*retrieve-and-extract*).** El baseline específico de la tarea que RAG supera: sistemas que recuperan pasajes y extraen un span de texto como respuesta, en vez de generarla.

**Procedencia (*provenance*).** El término que el paper usa para trazabilidad: *"providing provenance for their decisions ... remain open research problems"*.

## Evidence and examples

El abstract **no contiene cifras**. Las afirmaciones cuantitativas son comparativas y cualitativas:

- Estado del arte en **tres tareas de QA de dominio abierto** (no se nombran en el abstract; en el paper son Natural Questions, TriviaQA y WebQuestions).
- Supera a *"parametric seq2seq models"* y a *"task-specific retrieve-and-extract architectures"*.
- En generación, produce lenguaje *"more specific, diverse and factual"* que un baseline seq2seq del estado del arte, sin dar la métrica ni el margen.

Metadatos de peso e impacto:
- **Aceptado en NeurIPS 2020** (declarado en el campo `Comments`).
- Cuatro versiones entre mayo de 2020 y abril de 2021. El tamaño creció de 698 KB (v1) a 767 KB (v2) y se mantuvo estable en v3 y v4.
- La página de arXiv registra **13 blog links** (trackbacks), contra 3 de HNSW — señal cuantificable de la difusión del paper fuera del ámbito académico.
- Hay versión HTML experimental y TeX source disponibles en arXiv, además del PDF.
- Doce autores, entre ellos Douwe Kiela, Sebastian Riedel y Wen-tau Yih.

**Si la clase quiere citar cifras concretas de RAG (exact match en NQ, mejoras sobre T5/BART, tamaño del índice de Wikipedia, cantidad de pasajes recuperados `k`), esta captura no las tiene.** Habría que capturar `https://arxiv.org/pdf/2005.11401`.

## Inconsistencies / open questions

- **La captura es sólo el abstract, no el paper.** Ninguna cifra, tabla o figura del trabajo original está disponible en este registro. Es el límite duro de lo que se puede citar contra esta fuente.
- **Deriva semántica del término "RAG".** El paper define RAG como una receta de fine-tuning con retriever diferenciable entrenado junto al generador. La clase (y la industria) usa "RAG" para el patrón *retrieve → augment → generate* con componentes desacoplados y sin entrenamiento. Ambos usos son legítimos, pero **atribuirle al paper de Lewis el pipeline moderno de chunking + vector store + prompt es un salto que la fuente no sostiene**. Vale la pena señalarlo si el deck cita a Lewis 2020 junto a un diagrama de pipeline de LangChain.
- **El abstract no menciona chunking, embeddings de propósito general, reranking, búsqueda híbrida ni RRF.** Nada del pipeline de producción moderno está acá. La rama léxica (BM25) y la fusión de rankings vienen de otras fuentes del corpus.
- **La comparación RAG-Sequence vs. RAG-Token no se resuelve en el abstract**: dice que se comparan las dos formulaciones, no cuál gana.
- **Fecha del nombre de carpeta vs. versión capturada.** La carpeta dice `rag-lewis-2020` y el envío original es de mayo de 2020 (correcto para citar), pero la versión capturada es la **v4 de abril de 2021**.
- **El corpus no paramétrico del paper es Wikipedia.** Para una clase de biomedicina, la analogía relevante (PubMed, guías clínicas, historia clínica institucional) es una extrapolación de la clase; el paper sólo validó sobre Wikipedia.

## Images / diagrams

Tres assets, todos cromo de la interfaz de arXiv — los mismos tres que trajo la captura de HNSW. **La página de abstract no incluye ninguna figura del paper** (en particular, no incluye la Figura 1 con la arquitectura RAG, que es la que un deck querría).



## Raw / preserved excerpts

**Abstract (verbatim, inglés — el texto fundacional de RAG, para citar en la slide de origen):**

> Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory can overcome this issue, but have so far been only investigated for extractive downstream tasks. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) -- models which combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, the other can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set the state-of-the-art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.

**Metadatos bibliográficos (verbatim):**

> Computer Science > Computation and Language
> arXiv:2005.11401 (cs)
> [Submitted on 22 May 2020 (v1), last revised 12 Apr 2021 (this version, v4)]
> Title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
> Authors: Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, Douwe Kiela
> Comments: Accepted at NeurIPS 2020
> Subjects: Computation and Language (cs.CL); Machine Learning (cs.LG)
> Cite as: arXiv:2005.11401 [cs.CL] (or arXiv:2005.11401v4 [cs.CL] for this version)
> https://doi.org/10.48550/arXiv.2005.11401

**Historial de versiones (verbatim):**

> From: Patrick Lewis
> [v1] Fri, 22 May 2020 21:34:34 UTC (698 KB)
> [v2] Mon, 7 Dec 2020 16:23:06 UTC (767 KB)
> [v3] Mon, 29 Mar 2021 10:12:16 UTC (767 KB)
> [v4] Mon, 12 Apr 2021 15:42:18 UTC (767 KB)
