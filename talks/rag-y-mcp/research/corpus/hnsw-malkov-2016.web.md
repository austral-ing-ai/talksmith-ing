---
source_file: hnsw-malkov-2016
source_type: web-capture
ingested_at: 2026-08-14
---

# Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs (Malkov & Yashunin, arXiv:1603.09320)

## Provenance
- Original location: `research/web/hnsw-malkov-2016/`
- Format: html (página de abstract de arXiv, no el PDF del paper).
- URL: https://arxiv.org/abs/1603.09320
- Autor / fuente: Yu. A. Malkov y D. A. Yashunin.
- Fecha del original: enviado el 30 de marzo de 2016 (v1); última revisión 14 de agosto de 2018 (v4, la capturada). Comentarios del paper: 13 páginas, 15 figuras. Categorías: cs.DS (principal), cs.CV, cs.IR, cs.SI. DOI: 10.48550/arXiv.1603.09320.
- `http_status`: 200 · `fetched_at`: 2026-08-14T16:57:34Z.
- **Alcance de la captura**: `talksmith:ingest` capturó la página `/abs/` de arXiv, que contiene el abstract completo, autores, fechas e historial de versiones, pero **no el cuerpo del paper**. Todo lo que sigue proviene del abstract. Los detalles algorítmicos (parámetros `M`, `efConstruction`, `ef`, el heurístico de selección de vecinos, los benchmarks contra FAISS/Annoy/NMSLIB) están en el PDF, que no se capturó.

## Key claims

Todos verificables contra el abstract verbatim (ver *Raw / preserved excerpts*):

- **HNSW es un enfoque para búsqueda aproximada de K vecinos más cercanos basado en grafos navigable small world con jerarquía controlable.**
- **La solución es completamente basada en grafos**, sin necesidad de estructuras de búsqueda adicionales. Esto la distingue de la mayoría de las técnicas de grafos de proximidad, que sí requieren una estructura extra para la etapa de búsqueda gruesa (*coarse search stage*).
- **La construcción es incremental y multicapa**: se construye un conjunto jerárquico de grafos de proximidad (capas) sobre subconjuntos anidados de los elementos almacenados.
- **La capa máxima en la que aparece un elemento se elige al azar con una distribución de probabilidad de decaimiento exponencial.** Este es el mecanismo que produce la jerarquía y el que hace que HNSW se parezca a una skip list.
- **La separación de escalas es la clave del rendimiento.** Al asignar las capas de esa manera, los enlaces quedan separados por su escala de distancia característica; empezar la búsqueda desde la capa superior y aprovechar esa separación mejora el rendimiento respecto de NSW y **permite un escalado de complejidad logarítmico**.
- **Un heurístico adicional para seleccionar los vecinos del grafo de proximidad aumenta significativamente el rendimiento con recall alto y en datos muy agrupados (*highly clustered*).** Es el caso relevante para corpus de dominio (por ejemplo, documentos biomédicos, donde muchos chunks son casi idénticos).
- **HNSW supera con claridad a los enfoques open-source previos del estado del arte que trabajan sólo con vectores** (*"vector-only approaches"*), y funciona como índice general de espacios métricos, no sólo euclidiano.
- **La similitud con la estructura de skip list permite una implementación distribuida y balanceada de forma directa.**

## Definitions and terminology

**ANN / búsqueda aproximada de K vecinos más cercanos.** El problema que resuelve HNSW: dado un vector de consulta, encontrar los `K` vectores más cercanos del índice, aceptando una probabilidad de error a cambio de tiempo sublineal. Es la operación que ejecuta la rama vectorial de un retriever híbrido en RAG. El abstract la nombra como *"approximate K-nearest neighbor search"*.

**NSW (Navigable Small World).** La estructura previa sobre la que HNSW construye: un grafo de proximidad con propiedades de "mundo pequeño" (caminos cortos entre nodos cualesquiera). HNSW le agrega jerarquía controlable.

**Grafo jerárquico navegable / Hierarchical NSW.** Estructura multicapa donde cada capa es un grafo de proximidad sobre un subconjunto anidado de los elementos. La capa 0 contiene todos los elementos; cada capa superior contiene un subconjunto cada vez más chico. Cita del abstract: *"Hierarchical NSW incrementally builds a multi-layer structure consisting from hierarchical set of proximity graphs (layers) for nested subsets of the stored elements."*

**Asignación aleatoria de capa con decaimiento exponencial.** *"The maximum layer in which an element is present is selected randomly with an exponentially decaying probability distribution."* Es el sorteo que define la jerarquía: la mayoría de los elementos vive sólo en la capa 0, unos pocos suben. Sin este sorteo no hay jerarquía y el algoritmo degenera en NSW.

**Separación de escalas (*scale separation*).** Consecuencia de la asignación por capas: los enlaces de las capas altas cubren distancias largas y los de las capas bajas, distancias cortas. La búsqueda arranca arriba (saltos largos, para acercarse rápido a la región correcta) y baja (saltos cada vez más finos, para refinar). Es la analogía directa con una skip list, y es la mejor forma de explicarlo en clase: *"Starting search from the upper layer together with utilizing the scale separation boosts the performance compared to NSW and allows a logarithmic complexity scaling."*

**Heurístico de selección de vecinos (*heuristic for selecting proximity graph neighbors*).** Regla para decidir a qué vecinos conectar un elemento nuevo, distinta de "conectarse simplemente a los `M` más cercanos". El abstract sólo afirma su efecto — mejora el rendimiento con recall alto y en datos muy agrupados — sin describirla; la descripción está en el cuerpo del paper, que no se capturó.

**Índice de espacio métrico general.** El abstract lo describe como *"general metric space search index"*: no está atado a distancia euclidiana ni a coseno, funciona con cualquier métrica. Relevante si la clase quiere mencionar que el mismo índice sirve para embeddings normalizados (coseno) y no normalizados (L2, producto interno).

**Complejidad logarítmica.** Lo que HNSW consigue y NSW no. El abstract dice *"allows a logarithmic complexity scaling"*, sin dar la constante ni el régimen de validez.

## Evidence and examples

El abstract capturado **no contiene números**: no hay tablas de recall vs. QPS, ni comparación cuantitativa contra baselines, ni tamaños de dataset. Lo único que afirma cuantitativamente es cualitativo — *"able to strongly outperform previous opensource state-of-the-art vector-only approaches"*.

Metadatos que sí sirven como evidencia de peso e impacto de la fuente:
- Publicado en arXiv en marzo de 2016, con cuatro versiones hasta agosto de 2018. El tamaño del envío creció de 1.613 KB (v1) a 2.575 KB (v4), lo que sugiere ampliación sustancial del material experimental entre versiones.
- 13 páginas, 15 figuras.
- La página registra 3 *blog links* (trackbacks) y entradas en NASA ADS, Google Scholar, Semantic Scholar y DBLP.
- Clasificado simultáneamente en estructuras de datos (cs.DS), visión por computadora (cs.CV), recuperación de información (cs.IR) y redes sociales y de información (cs.SI) — señal de que el algoritmo se adoptó transversalmente.

**Si la clase necesita cifras de rendimiento de HNSW (recall@10, QPS, uso de memoria, valores típicos de `M` y `ef`), esta captura no las tiene.** Habría que capturar el PDF (`https://arxiv.org/pdf/1603.09320`) o citar la documentación de una implementación (hnswlib, FAISS, pgvector, Qdrant).

## Inconsistencies / open questions

- **La captura es sólo la página de abstract, no el paper.** Es la limitación principal de este registro. Todo lo operativo — parámetros `M` / `efConstruction` / `ef`, el heurístico de selección de vecinos, el pseudocódigo, los 15 gráficos de recall-vs-tiempo — está fuera del material capturado. Cualquier slide que hable de "cómo tunear HNSW" no se puede citar contra este registro.
- **Fecha ambigua en el nombre de la carpeta.** La carpeta dice `hnsw-malkov-2016` y el envío original es de 2016, pero **la versión capturada es la v4 de agosto de 2018**, que es la que suele citarse (y la que corresponde a la publicación en IEEE TPAMI, 2020). Si el deck cita "Malkov & Yashunin, 2016", es defendible (fecha del preprint original) pero conviene ser consciente de la diferencia.
- **El abstract no menciona las desventajas de HNSW** que sí importan en producción y que la clase podría querer nombrar: consumo de memoria alto (el grafo vive en RAM), costo de construcción del índice, y dificultad para borrar elementos. Nada de eso está en la fuente capturada; no se puede atribuir al paper.
- **"Strongly outperform previous opensource state-of-the-art vector-only approaches"** es una afirmación comparativa sin los baselines nombrados en el abstract. Los competidores concretos (Annoy, FLANN, FAISS-IVF, etc.) aparecen en el cuerpo del paper.
- **No hay conexión con RAG en la fuente.** Es un paper de estructuras de datos de 2016/2018. El vínculo "HNSW es lo que corre adentro de tu vector store" es de la clase.

## Images / diagrams

Tres assets, todos cromo de la interfaz de arXiv. Ninguno tiene contenido técnico: **el abstract page no incluye las 15 figuras del paper**.



## Raw / preserved excerpts

**Abstract (verbatim, inglés — la fuente completa de contenido técnico de esta captura):**

> We present a new approach for the approximate K-nearest neighbor search based on navigable small world graphs with controllable hierarchy (Hierarchical NSW, HNSW). The proposed solution is fully graph-based, without any need for additional search structures, which are typically used at the coarse search stage of the most proximity graph techniques. Hierarchical NSW incrementally builds a multi-layer structure consisting from hierarchical set of proximity graphs (layers) for nested subsets of the stored elements. The maximum layer in which an element is present is selected randomly with an exponentially decaying probability distribution. This allows producing graphs similar to the previously studied Navigable Small World (NSW) structures while additionally having the links separated by their characteristic distance scales. Starting search from the upper layer together with utilizing the scale separation boosts the performance compared to NSW and allows a logarithmic complexity scaling. Additional employment of a heuristic for selecting proximity graph neighbors significantly increases performance at high recall and in case of highly clustered data. Performance evaluation has demonstrated that the proposed general metric space search index is able to strongly outperform previous opensource state-of-the-art vector-only approaches. Similarity of the algorithm to the skip list structure allows straightforward balanced distributed implementation.

**Metadatos bibliográficos (verbatim):**

> Computer Science > Data Structures and Algorithms
> arXiv:1603.09320 (cs)
> [Submitted on 30 Mar 2016 (v1), last revised 14 Aug 2018 (this version, v4)]
> Title: Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs
> Authors: Yu. A. Malkov, D. A. Yashunin
> Comments: 13 pages, 15 figures
> Subjects: Data Structures and Algorithms (cs.DS); Computer Vision and Pattern Recognition (cs.CV); Information Retrieval (cs.IR); Social and Information Networks (cs.SI)
> Cite as: arXiv:1603.09320 [cs.DS] (or arXiv:1603.09320v4 [cs.DS] for this version)
> https://doi.org/10.48550/arXiv.1603.09320

**Historial de versiones (verbatim):**

> From: Yury Malkov A
> [v1] Wed, 30 Mar 2016 19:29:44 UTC (1,613 KB)
> [v2] Sat, 21 May 2016 07:27:25 UTC (1,590 KB)
> [v3] Sun, 30 Jul 2017 12:07:54 UTC (2,481 KB)
> [v4] Tue, 14 Aug 2018 19:29:07 UTC (2,575 KB)
