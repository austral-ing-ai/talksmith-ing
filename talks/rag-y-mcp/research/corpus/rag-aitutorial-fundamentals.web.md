---
source_file: rag-aitutorial-fundamentals
source_type: web-capture
ingested_at: 2026-08-14
---

# RAG Fundamentals (AI Tutorial)

## Provenance
- Original location: `research/web/rag-aitutorial-fundamentals/`
- Format: html (página de documentación, sitio Mintlify). Texto tomado de `page.md` (~7.500 caracteres, 11 encabezados). Extracción limpia y completa.
- URL: https://aitutorial.dev/rag/fundamentals
- Autor / fuente: **aitutorial.dev**, sección "Retrieval Augmented Generation (RAG)". Sin autor firmante, sin fecha, sin bibliografía. Mismo sitio y mismos logos (CDN `digibee-1a4db0d2`, probablemente Digibee) que `agents-aitutorial-tool-selection.web.md` y `rag-aitutorial-reranking.web.md`.
- Fecha del original: no declarada. `fetched_at`: 2026-08-14T16:56:59Z.
- HTTP status: 200.

**Naturaleza de la fuente.** Tutorial comercial. Su valor para la clase no está en la evidencia (no aporta ninguna) sino en la **arquitectura**: es la fuente del pipeline RAG de cuatro etapas que el deck usa, y la que enuncia la fórmula de RRF en la forma en que el deck la muestra.

## Key claims

- **El problema que RAG resuelve es el límite de conocimiento (*knowledge boundary problem*).** Los LLM sólo saben lo que estaba en su entrenamiento; ante una pregunta sobre datos privados o recientes, o alucinan o admiten que no saben.
- **ChatGPT no es un LLM puro, y eso confunde a los alumnos.** Es la observación pedagógica más útil de la página: si probás la misma pregunta en ChatGPT quizás obtengas una respuesta real, pero es porque tiene herramientas incorporadas (navegación web, intérprete de código) que buscan datos en vivo. *"Under the hood, it's doing exactly what we're about to build."* La diferencia es el control: con ChatGPT no controlás qué se busca, en qué fuentes se confía, ni qué contexto se usa.
- **RAG son tres pasos.** RETRIEVE → AUGMENT → GENERATE. *"That's it. Everything else — chunking, embeddings, reranking, hybrid search — is about making each step better."*
- **El pipeline de producción tiene cuatro etapas, no tres.** Recuperación rápida → fusión de rankings (RRF) → reranking (cross-encoder) → generación.
- **La justificación del pipeline multi-etapa es un compromiso de velocidad contra precisión.** Los métodos rápidos procesan 100K+ documentos en milisegundos; los cross-encoders sólo manejan ~100 documentos en tiempo razonable. La solución es filtrar con los rápidos y rankear con el preciso.
- **La justificación de RRF es la complementariedad.** La búsqueda léxica es buena en coincidencias exactas de palabras clave; la vectorial captura similitud semántica. Correrlas en paralelo y fusionar da lo mejor de ambas.
- **RAG frente a fine-tuning es un argumento de costo y actualización**: reentrenar es caro y lento de actualizar; con RAG "just update your document store — no retraining needed".
- **La auditabilidad es un beneficio de primera clase**, no un detalle: cada respuesta enlaza a documentos fuente específicos.
- **El prototipo simple es explícitamente insuficiente para producción.** La página enumera sus seis carencias (ver `Evidence and examples`).

## Definitions and terminology

**Knowledge boundary problem.** El nombre que la página le pone al hecho de que el modelo sólo conoce sus datos de entrenamiento. *"This is the knowledge boundary problem, and RAG is how production systems solve it."*

**RAG, en su forma mínima (verbatim):**

```
1. RETRIEVE  →  Find relevant documents for the user's question
2. AUGMENT   →  Insert those documents into the prompt as context
3. GENERATE  →  Have the LLM answer using only the provided context
```

Nótese el "**using only the provided context**": la restricción de fundamentación está dentro de la definición, no es un extra.

**Reciprocal Rank Fusion (RRF) — como la enuncia esta página.** Verbatim: *"RRF combines ranked lists by assigning each document a score based on its rank position across all retrievers: `score = Σ 1/(k + rank)` — documents that appear high in multiple lists bubble to the top."*

**Punto crítico: esta página nunca dice cuánto vale `k`.** Da la fórmula y nada más. El deck usa `k = 60` como default sin explicarlo (slide 27) y no lo saca de acá. La justificación del `k = 60` está en el paper de Cormack — ver `rrf-cormack-2009.web.md`, sección *Definitions and terminology*, donde consta que 60 se fijó en una investigación piloto sobre los tópicos TREC 351-400, resultó "near-optimal" en esa corrida, y que los propios autores aclaran que *"the choice was not critical"*. Si una slide muestra la fórmula de esta página y el `k=60`, está mezclando dos fuentes y debe citar las dos.

**Cross-encoder.** La página lo usa como sinónimo de "modelo de reranking preciso": un modelo más exacto que analiza cada candidato en profundidad. No explica la diferencia arquitectónica con un bi-encoder (que es lo que hace cara la operación: el cross-encoder procesa el par consulta-documento junto, y por eso no se puede precomputar el índice). Esa carencia es la misma en `rag-aitutorial-reranking.web.md`.

**First-pass retrieval / recall vs. precision.** La etapa 1 prioriza **recall** sobre precisión ("cast a wide net", 10-50 candidatos por método); la etapa 3 prioriza **precisión** sobre velocidad (top 3-5).

**Hybrid search (búsqueda híbrida).** Correr léxica y vectorial en paralelo. La página la nombra en la lista de carencias del prototipo ("No lexical/vector hybrid search") y la asume en el pipeline, pero no la define formalmente.

**Grounding / context engineering.** Diseño del prompt para que la generación quede atada al contexto recuperado, más formato de citas y manejo del caso "contexto insuficiente".

**Recall@k y NDCG.** Métricas de recuperación que menciona en el framework de evaluación. **Faithfulness y relevance**: métricas de generación. No define ninguna.

## Evidence and examples

**Tabla "When You Need RAG" (verbatim, reconstruida — en `page.md` llegó como una tira de texto sin separadores de columna):**

| Escenario | Por qué falla el LLM solo | Qué agrega RAG |
|---|---|---|
| **Data freshness** | Los datos de entrenamiento tienen fecha de corte; el modelo no sabe nada posterior | Recupera datos actuales de fuentes vivas |
| **Proprietary data** | Tus documentos internos, bases de datos y APIs nunca estuvieron en el entrenamiento | Conecta el LLM a tu base de conocimiento privada |
| **Accuracy & citations** | El modelo puede alucinar respuestas plausibles pero incorrectas | Restringe la generación a hechos recuperados, con citas de fuente |
| **Cost** | Hacer fine-tuning con datos nuevos es caro y lento de actualizar | Basta actualizar el almacén de documentos — sin reentrenar |
| **Auditability** | No podés rastrear por qué el modelo dijo algo | Cada respuesta enlaza a documentos fuente específicos |

**Las seis limitaciones del prototipo (verbatim):**

> - No error handling
> - No caching (repeated queries waste money)
> - No retrieval quality measurement
> - Single-stage retrieval (accuracy suffers)
> - No lexical/vector hybrid search
> - No metadata or filtering

**El diagrama ASCII del pipeline de cuatro etapas (verbatim).** Es el activo más reutilizable de la página y aparece **idéntico** en `rag-aitutorial-reranking.web.md`:

```
+------------------+
│    User Query    │
+------------------+
        |
        v
+------------------+
│  Stage 1:        │
│  Fast Retrieval  │  ← Get 10-50 candidates per method
│  (Lexical/Vector)│     (prioritize recall over precision)
+------------------+
        |
        v
+------------------+
│  Stage 2:        │
│  Rank Fusion     │  ← Merge results from multiple retrievers
│  (RRF)           │     into a single ranked list
+------------------+
        |
        v
+------------------+
│  Stage 3:        │
│  Reranking       │  ← Narrow to top 3-5 precisely
│  (Cross-Encoder) │     (prioritize precision over speed)
+------------------+
        |
        v
+------------------+
│  Stage 4:        │
│  LLM Generation  │  ← Use retrieved context to generate
│  (GPT-4/Claude)  │     grounded response
+------------------+
        |
        v
+------------------+
│    Response      │
+------------------+
```

**Los cinco componentes de un RAG de producción (verbatim, resumido):**

1. **Document Processing Pipeline** — estrategia de chunking (tamaño, solapamiento), extracción de metadatos (título, fecha, fuente), filtrado por calidad.
2. **Multi-Stage Retrieval** — primera pasada rápida y amplia (léxica y vectorial en paralelo), fusión con RRF, reranking con cross-encoders.
3. **Context Engineering** — diseño del prompt para fundamentación, formato de citas, manejo de contexto insuficiente.
4. **Evaluation Framework** — métricas de recuperación (Recall@k, NDCG), de generación (faithfulness, relevance), depuración por componente.
5. **Observability** — monitoreo de calidad de recuperación, seguimiento de latencia, costo por consulta.

**Cifras concretas que sí da la página** (son pocas y todas son órdenes de magnitud, no mediciones):

- Etapa 1: **10-50 candidatos por método**.
- Etapa 3: reducir a **top 3-5**.
- Métodos rápidos: **100K+ documentos en milisegundos**.
- Cross-encoders: **~100 documentos** en tiempo razonable.

**Fuente de datos del ejemplo**: un archivo JSON (`assets/company_docs.json`), con la aclaración de que podría venir de cualquier lado — base de datos, API, CMS, scraper — y que el patrón RAG no cambia.

## Inconsistencies / open questions

1. **La página es notablemente prudente con la latencia, y eso contrasta con el deck.** Su sección "Latency in practice" está redactada casi enteramente en condicional y con descargos: *"varies by system"*, *"implementation-, scale-, and hardware-dependent"*, *"Production systems typically target interactive end-to-end latency budgets on available hardware"*. **No da un solo número de latencia.** El deck, en cambio, presenta en la slide 22 latencias concretas (100-500 ms para búsqueda semántica) y costos por consulta (~$0,0001, ~$0,002-0,015) sin fuente. Esas cifras **no salen de acá** — esta página se negó explícitamente a darlas.
2. **La fórmula de RRF viene sin `k`.** Ver `Definitions and terminology`. Es la brecha más importante entre esta fuente y lo que el deck necesita.
3. **No hay ninguna cifra de calidad.** Ni "85-92 % de relevancia" ni nada parecido. La página no reporta un solo resultado experimental propio ni ajeno. Cualquier número de calidad del deck no viene de acá.
4. **"Cross-encoder" se usa sin definirse.** Se lo presenta como "un modelo más preciso" sin explicar por qué es lento (procesa el par consulta-documento junto, no admite índice precomputado). Un alumno que salga de esta página sabe que hay que usarlo, pero no por qué cuesta.
5. **El código no se extrajo.** La página dice "Try asking the model about private company data" y "The company documents live in a JSON file" pero los bloques de código de la implementación básica no aparecen en `page.md` — probablemente se renderizan en pestañas o componentes interactivos de Mintlify que el extractor no desplegó. **Esto es una pérdida real de extracción**: la sección "Basic RAG Implementation" quedó como prosa sin su código. `original.html` (460 KB) podría tenerlo embebido; no se verificó.
6. **Solapamiento casi total con `rag-aitutorial-reranking.web.md`.** El diagrama de cuatro etapas, la justificación del multi-etapa y la fórmula de RRF son los mismos en ambas páginas. Al citar, conviene usar `fundamentals` para el "por qué RAG" y `reranking` para el detalle de las etapas, y no citar ambas por lo mismo.
7. **El framework de evaluación se enumera y no se desarrolla.** Recall@k, NDCG, faithfulness y relevance aparecen como nombres en una lista. Si la clase promete un bloque de evaluación (y la agenda del deck lo promete), esta fuente no lo cubre.

## Images / diagrams

Dos assets, ambos el logotipo del sitio. **La página no contiene ninguna imagen de contenido**: el pipeline de cuatro etapas es un bloque de texto ASCII, no un gráfico. Si el deck muestra ese pipeline como diagrama, es de elaboración propia (o rehecho a partir del ASCII de esta página, que es la lectura más probable).

### `rag-aitutorial-fundamentals.web/images/logo-light-full.svg`
- **Provenance**: `https://mintcdn.com/digibee-1a4db0d2/.../logo/logo-light-full.svg`, `alt="light logo"`. 50.354 bytes. Byte por byte idéntico al de las otras dos capturas de aitutorial.dev.
- **Depiction**: logotipo vectorial de "AI Tutorial" para fondo claro.
- **Why it matters**: nada para la clase. Marca del sitio.
- **Transcribed text**: sin cadena de texto extraíble del vector; corresponde a la marca "AI Tutorial".

### `rag-aitutorial-fundamentals.web/images/logo-dark-full.svg`
- **Provenance**: ídem, `alt="dark logo"`. 50.236 bytes.
- **Depiction**: el mismo logotipo, invertido para fondo oscuro.
- **Why it matters**: ninguna.
- **Transcribed text**: ídem.

## Raw / preserved excerpts

**Encabezado (verbatim):**

> The core RAG pattern and how it works
>
> LLMs only know what they were trained on. RAG bridges this gap by retrieving relevant data and injecting it into the prompt. This page covers the core pattern and a production pipeline.

**"Why RAG?" (verbatim):**

> LLMs are powerful — but they have a fundamental limitation: **they only know what they were trained on.** Ask an LLM about your company's Q4 revenue, yesterday's incident report, or a document you uploaded last week, and it will either hallucinate an answer or admit it doesn't know. This is the **knowledge boundary problem**, and RAG is how production systems solve it.

**"The Problem RAG Solves" — el pasaje sobre ChatGPT (verbatim, el más aprovechable para la clase):**

> Try asking the model about private company data — it simply doesn't have it: If you try this same question in ChatGPT, you might get a real answer — but that's because ChatGPT is not a pure LLM. It has built-in tools (web browsing, code interpreter, etc.) that fetch live data behind the scenes. Under the hood, it's doing exactly what we're about to build: retrieving external data and injecting it into the prompt. The difference is that you don't control the retrieval pipeline — ChatGPT decides what to search, which sources to trust, and what context to use. Building your own RAG gives you full control over these decisions.

**"The Simplest RAG: Three Lines of Logic" (verbatim):**

> At its core, RAG is just three steps:
>
> ```
> 1. RETRIEVE  →  Find relevant documents for the user's question
> 2. AUGMENT   →  Insert those documents into the prompt as context
> 3. GENERATE  →  Have the LLM answer using only the provided context
> ```
>
> That's it. Everything else — chunking, embeddings, reranking, hybrid search — is about making each step better. Let's start with the simplest working version.

**"Basic RAG Implementation" (verbatim):**

> The company documents live in a JSON file (`assets/company_docs.json`), but they could come from anywhere — a database, an API, a CMS, a web scraper. The RAG pattern is the same regardless of the data source. This prototype works but has clear limitations:
>
> - No error handling
> - No caching (repeated queries waste money)
> - No retrieval quality measurement
> - Single-stage retrieval (accuracy suffers)
> - No lexical/vector hybrid search
> - No metadata or filtering
>
> We'll fix these throughout the module.

**"The Real-Life RAG Pipeline" (verbatim):**

> Production RAG systems go beyond "search + LLM." They use a carefully designed multi-stage pipeline where each stage solves a distinct problem.

**"Why Multi-Stage Retrieval?" (verbatim, completo):**

> **The Fundamental Trade-off:**
>
> - Fast retrieval methods (lexical, vector) can process 100K+ documents in milliseconds
> - Accurate ranking methods (cross-encoders) can only handle ~100 documents in reasonable time
> - Solution: Use fast methods to filter, fuse their results, then use an accurate method to rank
>
> **Why Rank Fusion (RRF)?**
>
> - Different retrieval methods have different strengths — lexical search excels at exact keyword matches, while vector search captures semantic similarity
> - Running both in parallel and then merging the results with **Reciprocal Rank Fusion (RRF)** gives you the best of both worlds
> - RRF combines ranked lists by assigning each document a score based on its rank position across all retrievers: `score = Σ 1/(k + rank)` — documents that appear high in multiple lists bubble to the top
> - This fused list is then passed to the cross-encoder reranker for precise scoring
>
> **Latency in practice (varies by system):**
>
> - First-pass retrieval returns a small candidate set quickly (implementation-, scale-, and hardware-dependent).
> - RRF merging is near-instant — it's just arithmetic over rank positions.
> - Cross-encoder reranking narrows to top results but adds additional latency.
> - Production systems typically target interactive end-to-end latency budgets on available hardware.

**"Production RAG: Key Components" (verbatim):**

> A production RAG system needs:
>
> 1. **Document Processing Pipeline**
>    - Chunking strategy (size, overlap)
>    - Metadata extraction (title, date, source)
>    - Quality filtering
>
> 2. **Multi-Stage Retrieval**
>    - First-pass: Fast, broad recall (lexical and vector in parallel)
>    - Rank fusion: Merge results from multiple retrievers via RRF
>    - Reranking: Slow, precise scoring with cross-encoders
>
> 3. **Context Engineering**
>    - Prompt design for grounding
>    - Citation formatting
>    - Handling insufficient context
>
> 4. **Evaluation Framework**
>    - Retrieval metrics (Recall@k, NDCG)
>    - Generation metrics (faithfulness, relevance)
>    - Component-level debugging
>
> 5. **Observability**
>    - Retrieval quality monitoring
>    - Latency tracking
>    - Cost per query
