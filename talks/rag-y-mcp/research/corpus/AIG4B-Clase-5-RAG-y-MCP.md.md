---
source_file: AIG4B-Clase-5-RAG-y-MCP.md
source_type: article
ingested_at: 2026-08-14
---

# AIG4B — Clase 5: Retrieval-Augmented Generation (RAG) & Model Context Protocol (MCP)

## Provenance
- Original location: `research/articles/AIG4B-Clase-5-RAG-y-MCP.md` (+ carpeta de medios `research/articles/AIG4B-Clase-5-RAG-y-MCP-media/`) — **staging retirado el 2026-09-03**: era una copia byte a byte de `images/` de este mismo registro, verificada sobre los 198 archivos. El original sigue en `talksmith-aig4b`.
- Format: Markdown — extracción 1:1 de un deck PowerPoint. El binario original (`AIG4B-Clase-5-RAG-y-MCP.pptx`, 2,0 MB) vive en la raíz del Talk, fuera de `research/`.
- Author / source (if known): Autor consignado en la slide 1: **«Paulo Veiga / Marcos Sanchez Sorondo»**. El despacho de ingesta atribuye el deck original a Marcos Sorondo. Materia: *Inteligencia Artificial Generativa Aplicada en Biomedicina* (AIG4B), Universidad Austral.
- Date of original (if known): slide 1 — «Última Modificación: Abril, 2026».
- Extensión: 64 slides, 1957 líneas de Markdown, 42 bloques de tabla (150 filas), 122 colocaciones de imagen (64 imágenes únicas) y 75 SVG originales.
- **Notas del orador: NINGUNA.** Verificado sobre el `.pptx`: existen los 64 archivos `notesSlide*.xml`, pero los 64 están vacíos de texto real. El deck no trae ni una línea de guion del presentador — todo lo que se sabe de la clase es lo que está impreso en las slides.

### Mapa de secciones (según la etiqueta `Sección:` de cada slide)

| Slides | Sección declarada |
|---|---|
| 1–2 | (portada + agenda, sin etiqueta) |
| 3–7 | RAG: FUNDAMENTOS |
| 8 | (agenda) |
| 9–24 | RAG: BÚSQUEDA Y RECUPERACIÓN |
| 25 | (agenda) |
| 26–28 | RAG: RERANKING Y PRECISIÓN |
| 29 | MCP: ARQUITECTURA Y USO ← etiqueta equivocada, la slide es de reranking |
| 30 | (agenda) |
| 31–32 | RAG: CHUNKING, METADATOS Y RERANKING |
| 33 | (agenda) |
| 34–39 | RAG: EVALUACIÓN, SEGURIDAD Y PATRONES AVANZADOS |
| 40 | (agenda) |
| 41–44 | MCP: FUNDAMENTOS |
| 45 | (agenda) |
| 46–55 | MCP: ARQUITECTURA Y USO |
| 56 | (agenda) |
| 57–61 | MCP: DISEÑO DE HERRAMIENTAS |
| 62–64 | MCP: FUNDAMENTOS ← repiten literalmente las slides 41, 42 y 43 |

Ocho slides no tienen título: 7, 15, 20, 27, 28, 50, 52, 57.

---

## Key claims

Recorrido en orden de las 64 slides. Las tablas del deck se preservan como tablas Markdown, sin resumir.

### Slide 1 — Portada
Inteligencia Artificial Generativa Aplicada en Biomedicina. **Clase 5: Retrieval-Augmented Generation (RAG) & Model Context Protocol (MCP)**. Autor: Paulo Veiga / Marcos Sanchez Sorondo. Última Modificación: Abril, 2026. Logo de la Universidad Austral (`slide-01-1.png`).

### Slide 2 — Agenda (primera de ocho renditions)
Ocho bloques temáticos:

1. **RAG: Fundamentos** — Qué es RAG, por qué lo necesitamos y arquitectura básica.
2. **RAG: Búsqueda y Recuperación** — Búsqueda vectorial, léxica, semántica e híbrida. Bases de datos y flujo completo.
3. **RAG: Reranking y Precisión** — Recuperación en dos etapas, cross-encoders, Reciprocal Rank Fusion y optimización de precisión.
4. **RAG: Chunking y Metadatos** — Fragmentación de documentos, estrategias de chunking y metadatos esenciales.
5. **RAG: Evaluación y Seguridad** — «Riesgos y evaluacion» (sic, sin tilde).
6. **MCP: Fundamentos** — Qué es MCP, historia, protocolo JSON-RPC y comparativa con HTTP/GraphQL.
7. **MCP: Arquitectura y Uso** — Ciclo de vida, multi-servidor, ecosistema, casos de uso con Claude y cómo conectar servidores.
8. **MCP: Diseño de Herramientas** — Selección de herramientas, routing jerárquico, grupos por contexto, diferenciación y analytics en producción.

### Slide 3 — ¿Qué es RAG?
> «RAG combina lo mejor de dos mundos: el razonamiento de los LLMs con el conocimiento actualizado de bases de datos externas.»

| Recuperador | LLM | Base de conocimiento |
|---|---|---|
| Busca información relevante en fuentes externas | Razona y genera la respuesta con el contexto recuperado | Documentos, artículos y guías clínicas actualizadas |

### Slide 4 — «Los cuatro pasos de RAG»
El título anuncia cuatro pasos; la tabla presenta tres.

| RETRIEVE · Recuperar | AUGMENT · Aumentar | GENERATE · Generar |
|---|---|---|
| Encontrar documentos relevantes para la consulta del usuario dentro de la base de conocimiento del sistema. | Insertar los documentos recuperados en el prompt como contexto adicional que el modelo puede utilizar. | El LLM responde usando únicamente el contexto proporcionado, fundamentando y citando su respuesta. |

> «Esta arquitectura crea un ciclo virtuoso donde la recuperación informa la generación, y el sistema aprende a mejorar ambos procesos simultáneamente.»

### Slide 5 — ¿Cuándo necesitás RAG?
Cinco motivadores. Los cuatro primeros en tabla; el quinto (Auditabilidad) queda suelto en la extracción.

| Datos actualizados | Datos propietarios | Precisión y citas | Costo |
|---|---|---|---|
| Los datos de entrenamiento tienen fecha de corte. RAG recupera datos actuales desde fuentes en tiempo real. | Tus documentos internos y APIs nunca estuvieron en el entrenamiento. RAG conecta el LLM a tu base de conocimiento privada. | El modelo puede alucinar respuestas incorrectas. RAG restringe la generación a hechos recuperados con citas de fuentes. | El fine-tuning es caro y lento. Con RAG solo actualizás tu repositorio de documentos — sin reentrenamiento. |

**Auditabilidad** — «No podés rastrear por qué el modelo dijo algo. RAG enlaza cada respuesta a documentos fuente específicos.»

### Slide 6 — Ejemplo Básico de RAG
«Tutorial interactivo: implementación paso a paso de un pipeline RAG con LangChain». Botón «Haz clic aquí» enlazado a `https://aitutorial.dev/rag/fundamentals`.

### Slide 7 — (sin título) Pipeline de RAG en producción
Cadena: **Consulta Usuario → Recuperación Rápida → Reranking Cross-Encoder → Generación LLM**.

| Procesamiento de documentos | Recuperación en dos etapas | Ingeniería de contexto | Evaluación continua |
|---|---|---|---|
| Chunking, extracción de metadatos y filtrado de calidad. | Primera pasada rápida seguida de reranking preciso. | Diseño de prompts, formato de citas y manejo de contexto insuficiente. | Métricas de retrieval (Recall@k, NDCG) y generación (faithfulness). |

**Observabilidad** — «Monitoreo de calidad, latencia y coste por consulta en tiempo real.»

### Slide 8 — Agenda (1 ✓)
Primera rendición donde el ítem 5 cambia de redacción: pasa a «RAG: Evaluación, Seguridad y Patrones Avanzados — Métricas clave, LLM-as-Judge, riesgos, GraphRAG, Agentic RAG y RAG Multimodal».

### Slide 9 — Fuentes de conocimiento

| Documentos no estructurados | Bases de datos estructuradas |
|---|---|
| PDFs, artículos científicos, guías clínicas, informes. La fuente más común en biomedicina. | Registros clínicos, bases de datos relacionales, ontologías médicas (SNOMED, ICD-10). |

| APIs y fuentes en tiempo real | Código y datos técnicos |
|---|---|
| Datos de mercado, feeds de noticias, resultados de búsqueda web, APIs REST. | Repositorios de código, logs de sistemas, datos de sensores, registros de laboratorio. |

> «La calidad y cobertura de las fuentes determina directamente la calidad de las respuestas RAG. Garbage in, garbage out.»

### Slide 10 — Estructuras de Bases de Datos
Comparativa índice invertido vs. base vectorial, con vendors:

| Índice Invertido | Base de Datos Vectorial |
|---|---|
| BM25 / Keywords | Embeddings semánticos |
| búsqueda por palabras exactas<br>alta velocidad en consultas exactas<br>ideal para terminología especializada (ICD-10, SKUs, términos legales) | captura significado y contexto semántico<br>búsqueda por similitud entre conceptos<br>soporta búsquedas multilenguaje |
| Mejor para: Búsqueda exacta y filtrado por keywords | Mejor para: Búsqueda semántica y lenguaje natural |
| Vendors: Elasticsearch · OpenSearch · Apache Solr · Typesense | Vendors: Pinecone · Weaviate · Qdrant · Chroma · pgvector |

Tercera columna (extraída como bullets sueltos): **Búsqueda Híbrida — BM25 + Vectorial**
- combina precisión léxica con comprensión semántica
- reranking para fusionar resultados
- estándar en sistemas RAG de producción
- Mejor para: Sistemas RAG en producción ⭐
- Vendors: Elasticsearch · Weaviate · Azure AI Search · MongoDB Atlas

> «La elección entre ambas estrategias —o su combinación— depende del tipo de consulta y la naturaleza del corpus documental disponible.»

### Slide 11 — Ejemplo Básico de RAG (repite slide 6)
Mismo botón, mismo enlace `https://aitutorial.dev/rag/fundamentals`.

### Slide 12 — ¿Cómo funciona un Índice Invertido?
Cuatro pasos (en la extracción aparecen desordenados: títulos primero, cuerpos después).

1. **Ingesta de documentos** — «Se reciben los documentos de texto. Ej: Doc1: "el gato come pescado", Doc2: "el perro come carne", Doc3: "el gato y el perro"»
2. **Tokenización y normalización** — «Cada documento se divide en tokens (palabras). Se aplica lowercase, eliminación de stopwords ("el", "y") y stemming. Resultado: Doc1→[gato, come, pescado], Doc2→[perro, come, carne], Doc3→[gato, perro]»
3. **Construcción del índice** — «Se crea un mapa invertido: cada término apunta a los documentos que lo contienen. Ej: "gato" → [Doc1, Doc3] · "come" → [Doc1, Doc2] · "perro" → [Doc2, Doc3]»
4. **Consulta (Query)** — «El usuario busca "gato perro". El índice devuelve la intersección: Doc3 (contiene ambos). Ranking por frecuencia/BM25.»

> «BM25 extiende este modelo con ponderación por frecuencia de término (TF) e infrecuencia en el corpus (IDF), mejorando el ranking de resultados.»

### Slide 13 — TF-IDF: Term Frequency × Inverse Document Frequency
> 💡 «Idea: Un término es importante si aparece mucho en un documento... pero no si aparece en todos los documentos.»

| TF (Term Frequency) | IDF (Inverse Document Frequency) |
|---|---|
| TF responde: ¿Qué tan frecuente es este término en este documento? | IDF responde: ¿Qué tan raro es este término en todo el corpus? |

Fórmulas tal como aparecen:
- `TF(t, d) = count(t in d) / total_terms(d)`
- `IDF(t) = log(N / df(t))`
- `TF-IDF(t, d) = TF(t, d) × IDF(t)`

Glosario del deck: `t` = un término específico («t = "leucemia", t = "gato", t = "el"»); `d` = un documento del corpus; `N` = número total de documentos («si tenemos 10.000 artículos médicos, N = 10.000»); `df(t)` = documentos donde aparece t («"leucemia" aparece en 200 documentos → df("leucemia") = 200»).

Ejemplos: «"gato" aparece 3 veces en un doc de 100 palabras → TF = 0.03»; «"el", "de" → IDF ≈ 0. "leucemia" → IDF alto.»

> ⚠️ «Limitación: TF-IDF no satura — un término que aparece 100 veces vale 100x más que uno que aparece 1 vez. → BM25 resuelve esto.»

### Slide 14 — TF-IDF en acción: Ejemplo visual
El corpus de juguete que se usa en toda la unidad:

| Doc 1 | Doc 2 | Doc 3 |
|---|---|---|
| el gato come pescado fresco<br>5 tokens | el perro come carne y hueso<br>6 tokens | el gato y el perro son amigos<br>7 tokens |

Índice invertido con scores TF-IDF (la extracción parte la tabla en dos y deja «gato» como bullets sueltos):

| Término | En docs | TF (Doc1) | IDF | TF-IDF |
|---|---|---|---|---|
| el | Doc1, Doc2, Doc3 | 2/5=0.40 | log(3/3)=0.00 | 0.00 (stopword) |
| gato | Doc1, Doc3 | 1/5=0.20 | log(3/2)=0.18 | 0.04 |
| come | Doc1, Doc2 | 1/5=0.20 | log(3/2)=0.18 | 0.04 |
| pescado | Doc1 | 1/5=0.20 | log(3/1)=0.48 | 0.10 ⭐ |
| fresco | Doc1 | 1/5=0.20 | log(3/1)=0.48 | 0.10 ⭐ |

Lecturas del deck: «"el" aparece en los 3 docs → IDF = log(3/3) = 0 → score 0. Las stopwords se eliminan solas.» · «"gato" aparece en 2/3 docs → IDF bajo → score bajo. Es común en el corpus.» · «"pescado" y "fresco" solo en Doc1 → IDF alto → score alto. Son los términos más discriminativos.»

> 💡 «El índice invertido es como el índice de un libro: vas directo al término y te dice en qué documentos aparece y con qué relevancia.»

### Slide 15 — (sin título) TF-IDF: De la búsqueda al ranking de documentos
Cuatro etapas: **Query del usuario → Lookup en el índice → Cálculo de scores TF-IDF → Ranking y entrega al LLM**.

- Query: «¿Qué documentos hablan de pescado fresco?» → se tokeniza igual que los docs: `[pescado, fresco]`
- Lookup: «"pescado" → [Doc1], "fresco" → [Doc1]. Intersección: Doc1 ✓»
- Scores: «Doc1: TF-IDF("pescado") = 0.22, TF-IDF("fresco") = 0.22, Score total = 0.44 🥇»
- Ranking: «Se ordenan docs por score descendente. Doc1 (0.44) → top resultado. Se inyecta como contexto en el prompt RAG.»

| Score | Contenido | Cálculo | Documento | Entregado al LLM |
|---|---|---|---|---|
| 0.44 ✅ | «el gato come pescado fresco» | TF("pescado",Doc1) = 1/5 = 0.20<br>IDF("pescado") = log(3/1) = 1.10<br>TF("fresco",Doc1) = 1/5 = 0.20<br>IDF("fresco") = log(3/1) = 1.10<br>Score = (0.20×1.10) + (0.20×1.10) = 0.44 ✅ | Doc 1 | ✅ Sí (top resultado) |
| 0.00 ❌ | «el perro come carne y hueso» | TF("pescado",Doc2) = 0 → 0.00<br>TF("fresco",Doc2) = 0 → 0.00<br>Score = 0.00 ❌ | Doc 2 | ❌ No (sin match) |
| 0.00 ❌ | «el gato y el perro son amigos» | TF("pescado",Doc3) = 0 → 0.00<br>TF("fresco",Doc3) = 0 → 0.00<br>Score = 0.00 ❌ | Doc 3 | ❌ No (sin match) |

> 💡 «El índice TF-IDF actúa como el "motor de búsqueda" del pipeline RAG: convierte millones de documentos en una lista ordenada de candidatos relevantes en milisegundos, antes de que el LLM genere la respuesta.»

### Slide 16 — Ejemplo Indice Invertido
Botón enlazado a `https://aitutorial.dev/rag/fundamentals` (mismo destino que slides 6, 11, 21).

### Slide 17 — ¿Cómo funciona la búsqueda vectorial?
1. **Conversión a vectores** — «Transforma el texto en representaciones numéricas multidimensionales mediante modelos de embeddings entrenados para capturar semántica.»
2. **Cálculo de similitud** — «Mide la distancia o similitud semántica entre vectores usando métricas como similitud coseno o distancia euclidiana.»
3. **Recuperación inteligente** — «Encuentra documentos relevantes aunque no contengan las palabras exactas de la consulta, entendiendo la intención subyacente.»

> «Permite búsquedas más flexibles y contextuales, entendiendo la intención real detrás de las consultas del usuario.»

### Slide 18 — Embeddings: Convirtiendo texto en vectores
> 💡 «Idea: Las palabras con significado similar deben estar cerca en el espacio vectorial. "gato" y "felino" deben ser vecinos. "gato" y "automóvil" deben estar lejos.»

- **¿Qué es un embedding?** «Un embedding convierte texto en un punto en un espacio de N dimensiones.»
- **Entrenamiento contrastivo** — «El modelo aprende que frases con significado similar deben producir vectores cercanos. Se entrena con millones de pares (pregunta, respuesta relevante).»
- **Dimensionalidad** — «Los vectores tienen entre 384 y 3072 dimensiones. Más dimensiones = más capacidad semántica, pero más costo de almacenamiento y cómputo.»
- **Multilingüe** — «Los modelos multilingües mapean "cat" (inglés) y "gato" (español) a vectores cercanos — la búsqueda funciona entre idiomas sin traducción.»
- **Modelos populares:** `text-embedding-3-small` (OpenAI), `all-MiniLM-L6-v2` (open source), `embed-multilingual-v3` (Cohere).

```
"gato"   → [0.82, -0.31, 0.54, 0.12, ...]  (384 dims)
"felino" → [0.79, -0.28, 0.51, 0.15, ...]  (384 dims)
"perro"  → [0.71, -0.22, 0.48, 0.09, ...]  (384 dims)
"auto"   → [-0.12, 0.65, -0.33, 0.87, ...] (384 dims)
```

> 💡 «El embedding captura semántica, no sintaxis. "No puedo iniciar sesión" y "olvidé mi contraseña" producen vectores muy cercanos aunque no compartan ninguna palabra.»

### Slide 19 — Similitud Coseno: Midiendo cercanía semántica
> 💡 «Idea: No nos importa el tamaño del vector, sino su dirección. Dos textos son similares si apuntan en la misma dirección en el espacio vectorial.»

```
cos(θ) = (A · B) / (||A|| × ||B||)

Where:
- A · B = producto punto (suma de productos elemento a elemento)
- ||A|| = magnitud del vector A (raíz de suma de cuadrados)
- Resultado: entre -1 (opuestos) y 1 (idénticos)
```

- **Ángulo, no distancia** — «cos(0°) = 1 → idénticos. cos(90°) = 0 → sin relación. cos(180°) = -1 → opuestos. Usamos el ángulo entre vectores, no su distancia absoluta.»
- **Invariante a la longitud** — «"gato" y "El gato doméstico es un felino" producen vectores de distinto tamaño pero dirección similar → similitud alta. Esto es clave para comparar chunks de distinto largo.»
- **Alternativas:** «Distancia euclidiana: más intuitiva pero sensible a la magnitud. Producto punto: más rápido, usado en ANN (Approximate Nearest Neighbors) para escala.»

| Par de términos | Similitud coseno | Interpretación |
|---|---|---|
| "gato" vs "felino" | 0.91 | Muy similares ✅ |
| "gato" vs "perro" | 0.76 | Relacionados |
| "gato" vs "auto" | 0.12 | Sin relación ❌ |
| Query vs Doc1 | 0.87 | Alta relevancia ⭐ |

> 💡 «En producción, la búsqueda exacta de vecinos más cercanos es O(n) — demasiado lenta para millones de vectores. Se usan índices ANN (HNSW, IVF) que sacrifican un poco de precisión por velocidad sub-lineal.»

### Slide 20 — (sin título) Búsqueda Vectorial: De la query al ranking de documentos
Cuatro etapas: **Query del usuario → Búsqueda ANN → Score de similitud coseno → Ranking y entrega al LLM**.

- «"¿Qué animales comen pescado?" → se convierte en embedding: [0.81, -0.29, 0.52, ...]»
- «Se buscan los K vectores más cercanos en la base de datos vectorial usando índice HNSW o IVF. Sub-lineal en tiempo.»
- «Se calcula cos(θ) entre el vector de la query y cada candidato recuperado.»
- «Los documentos se ordenan por similitud descendente. Los top-K se inyectan como contexto en el prompt RAG.»

| Score coseno | Contenido | Documento | Entregado al LLM |
|---|---|---|---|
| 0.91 | "el gato come pescado fresco" | Doc 1 | ✅ Sí — alta similitud semántica |
| 0.43 | "el gato y el perro son amigos" | Doc 3 | ❌ No — menciona animales pero no alimentación |
| 0.21 | "el perro come carne y hueso" | Doc 2 | ❌ No — alimentación pero no pescado |

> «A diferencia de TF-IDF, Doc1 es recuperado aunque la query no contenga exactamente "gato" ni "pescado" — la similitud semántica captura la intención.»

> 💡 «Ventaja clave sobre TF-IDF: "infarto de miocardio" y "ataque al corazón" tienen similitud coseno ~0.89 → el sistema vectorial los conecta. TF-IDF los trataría como documentos completamente distintos.»

### Slide 21 — Ejemplo Busqueda Semantica
Botón a `https://aitutorial.dev/rag/fundamentals`.

### Slide 22 — Estrategias de búsqueda: Léxica vs Semántica vs Híbrida
Tabla comparativa central del bloque RAG, con costos y latencias:

| Búsqueda Léxica | Búsqueda Semántica | Búsqueda Híbrida |
|---|---|---|
| BM25 / Keywords | Embeddings / Vectores | Léxica + Semántica |
| ✓ Rápida, precisa en términos exactos, sin GPU<br>✗ No reconoce sinónimos ni abstracciones<br>Ideal: Códigos ICD-10, terminología legal<br>Coste: ~$0.0001/query | ✓ Sinónimos, multilenguaje, relaciones conceptuales<br>✗ Más lenta (100-500ms), requiere GPU<br>Ideal: Papers académicos, FAQs, help desk<br>Coste: ~$0.001-0.01/query | ✓ Mejor cobertura, 85-92% relevancia<br>✗ Mayor complejidad, requiere tuning de pesos<br>Ideal: Producción general, consultas biomedicina<br>Coste: ~$0.002-0.015/query |

### Slide 23 — Flujo completo de RAG
Cinco pasos: **Consulta → Vectorizar → Búsqueda VDB → Recuperar doc → Generar respuesta.**

> «El sistema completo trabaja en milisegundos para proporcionar respuestas precisas y fundamentadas en datos verificables, sin importar el tamaño del corpus.»

### Slide 24 — El desafío del tamaño del contexto

| Límite de tokens | Documentos extensos | Solución RAG |
|---|---|---|
| Los LLMs tienen un límite máximo de tokens que pueden procesar simultáneamente en una consulta. Superar este límite produce errores o truncado de información. | Documentos largos o múltiples fuentes de información pueden exceder fácilmente ese límite técnico, especialmente en corpus biomédicos. | RAG selecciona inteligentemente solo la información más relevante para incluir en el contexto, optimizando el uso de la ventana disponible. |

### Slide 25 — Agenda (1 ✓, 2 ✓)

### Slide 26 — ¿Qué es el Reranking?
> 💡 «La recuperación rápida encuentra candidatos pero los rankea mal. El reranking filtra el ruido y se queda solo con los documentos verdaderamente relevantes.»

| Etapa 1: Recuperación rápida (Recall) | Etapa 2: Reranking (Precision) |
|---|---|
| Objetivo: No perder documentos relevantes — red amplia | Objetivo: Quedarse solo con los mejores — filtrar el ruido |
| Método: BM25 léxico + búsqueda vectorial en paralelo | Método: Cross-encoder analiza cada candidato en profundidad |
| Resultado: top-50 candidatos recuperados rápidamente | Resultado: top-3 a top-5 documentos de alta precisión |
| Trade-off: rápido pero incluye ruido e irrelevantes | Trade-off: más lento pero mucho más preciso en relevancia |

Embudo numérico del deck: **100K+ docs** (corpus total, lo maneja la búsqueda rápida) → **50** (candidatos tras Stage 1) → **5** (resultado final tras Reranking ⭐).

> 💡 «¿Por qué funciona? Los retrievers rápidos son buenos encontrando candidatos pero malos rankeándolos. Los cross-encoders son excelentes rankeando pero demasiado lentos para miles de documentos. Combinados: velocidad + precisión.»

### Slide 27 — (sin título) Pipeline completo: Retrieval + RRF + Reranking
> «El pipeline combina recuperación léxica y semántica en paralelo, fusiona los resultados con RRF, y aplica un cross-encoder para quedarse con los top-5 más precisos.»

1. **Recuperación en paralelo** — «BM25 léxico + búsqueda vectorial corren simultáneamente. Cada uno retorna top-50 candidatos.»
2. **Reciprocal Rank Fusion (RRF)** — «Fusiona los dos rankings en uno solo. RRF(d) = Σ 1/(k + rank(d)). Penaliza documentos que aparecen tarde en ambas listas.»
3. **Cross-Encoder Reranking** — «Analiza cada par (query, documento) en profundidad. Mucho más preciso que bi-encoders. Reduce de top-50 a top-5.»
4. **Contexto al LLM** — «Los top-5 documentos de alta precisión se inyectan en el prompt. Mejor contexto → mejor respuesta.»

Fórmula y esquema de entrada, verbatim:

```
RRF(d) = Σ 1 / (k + rank_i(d))   [k=60 por defecto]

input:  "[CLS] query [SEP] documento [SEP]"
output: score de relevancia (0 a 1)
```

| Documento | Rank BM25 | Rank Vectorial | RRF Score |
|---|---|---|---|
| Doc A | 1 | 3 | 0.032 |
| Doc B | 5 | 1 | 0.032 |
| Doc C | 2 | 8 | 0.028 |

Sobre el cross-encoder: «Analiza la interacción entre query y documento · Mucho más preciso que similitud coseno · Modelos: Cohere Rerank, BGE-Reranker, ms-marco-MiniLM · Limitación: O(n) — no escala a millones de docs». Y: «RRF es robusto: no requiere normalizar scores de distintas fuentes.»

> 💡 «Tips de producción: mantener el pool de candidatos en 20-100 docs y el top_k final en 3-5. Correr BM25 y vectorial en paralelo. Loggear latencia y costo por consulta.»

### Slide 28 — (sin título) 🤔 ¿Por qué concatenar query + documento en el ranking con embeddings?
> «Un bi-encoder embeddea query y documento por separado y compara vectores. Un cross-encoder los lee juntos y entiende la relación entre ambos. Esa diferencia lo cambia todo.»

| Bi-encoder: embeddings separados | Cross-encoder: query + doc juntos |
|---|---|
| Así funciona la búsqueda vectorial clásica. | Así funciona el reranker — lee ambos a la vez. |
| embed(query) → vector A → [0.81, -0.29, 0.52, ...]<br>embed(documento) → vector B → [0.79, -0.28, 0.51, ...]<br>score: cos(A, B) = 0.91 | Input al modelo: query + separador + documento (texto completo)<br>Procesamiento: Transformer atiende cada token de la query contra cada token del doc<br>Output: score de relevancia entre 0 y 1 |
| ✓ Escalable — O(1) por doc en query time. Los embeddings de documentos se pre-computan y almacenan. Solo se embeddea la query en tiempo real. Ideal para millones de docs. | ✓ Ve la interacción completa — El modelo puede detectar que *pescado* en el documento responde directamente a la pregunta sobre alimentación de animales en la query. |
| ✗ Pierde el contexto conjunto — El embedding de la palabra *banco* es el mismo sin importar si la query habla de dinero o de un río. No ve la interacción entre ambos textos. | ✓ Mucho más preciso — Distingue matices imposibles para el coseno: negaciones, contexto, ambigüedad léxica. Modelos: Cohere Rerank, BGE-Reranker, ms-marco-MiniLM. |
| ✗ Precisión limitada en reranking — Bueno para recuperar candidatos, pero no suficientemente preciso para decidir cuál de los top-50 es realmente el más relevante. | ✗ No escala solo — O(n) por query. Requiere una inferencia completa por cada par. Con 100K docs sería inviable. Por eso se usa solo sobre los top-50 candidatos del Stage 1. |

> 💡 «La concatenación es la clave: al pasarle query y documento juntos al Transformer, el mecanismo de atención puede relacionar directamente cada palabra de la pregunta con cada palabra del documento. Eso es lo que el coseno entre vectores separados nunca puede hacer.»

### Slide 29 — Ejemplo de Ranking
Botón enlazado a `https://aitutorial.dev/rag/reranking`. La slide está etiquetada *Sección: MCP: ARQUITECTURA Y USO* pese a ser el cierre del bloque de reranking.

### Slide 30 — Agenda (1 ✓, 2 ✓)

### Slide 31 — Técnicas de chunking: Fragmentación de documentos
> «El chunking divide documentos extensos en fragmentos manejables. La tensión fundamental: fragmentos pequeños (100-200 tokens) mejoran la precisión pero pierden contexto; fragmentos grandes (1000+) mantienen contexto pero diluyen la señal de recuperación.»

| Tamaño fijo | Semántico |
|---|---|
| Divide por cantidad de tokens con overlap configurable. Simple y predecible, pero puede cortar oraciones en puntos inapropiados. | Respeta límites de párrafos y secciones. Ofrece mejor coherencia semántica aunque produce tamaño variable. |
| **Estructura-aware** | **Con metadatos** |
| Usa la jerarquía del documento (headers, secciones). Ideal para documentos técnicos, APIs y guías clínicas. | Enriquece fragmentos con fuente, timestamp, posición y autor. Mejora el filtrado previo a la búsqueda. |

### Slide 32 — Metadatos y guía por tipo de documento
**Metadatos esenciales — Siempre incluir:** identificador de fuente · timestamp de creación/actualización · posición del chunk dentro del documento.
**Condicional:** autor / departamento · tipo de documento y versión · jerarquía de sección, idioma, score de calidad.

**Tamaño recomendado por tipo** (la extracción rompe esta tabla en dos: las dos primeras filas quedan en tabla, «Contratos» y «Papers» quedan como bullets sueltos):

| Tipo | Estrategia | Chars |
|---|---|---|
| Blog posts | Semántico | 800-1000 |
| Docs técnicos | Estructura | 600-800 |
| Contratos | Estructura | 1000-1500 |
| Papers | Estructura | 1000-1200 |

### Slide 33 — Agenda (1 ✓, 2 ✓; el ítem 5 vuelve a la redacción corta «RAG: Evaluación y Seguridad / Riesgos y evaluacion»)

### Slide 34 — Evaluación de RAG: Métricas clave
> «Evaluar retrieval y generación por separado es fundamental. **El 70% de los fallos de RAG provienen de la recuperación**, no de la generación, por lo que dedicar esfuerzo a medir el retrieval es prioritario.»

| Context Relevance | Answer Faithfulness | Answer Relevance |
|---|---|---|
| ¿Se recuperaron los documentos correctos? Mide si el recuperador trae contexto verdaderamente útil para responder la consulta. | ¿La respuesta está fundamentada en el contexto? Evalúa si el LLM se limita a lo que hay en los documentos recuperados. | ¿La respuesta aborda la pregunta del usuario? Verifica que la respuesta generada sea pertinente y completa. |

### Slide 35 — Riesgos y desafíos de seguridad en RAG
- **Acceso no autorizado** — «Riesgo de exponer información sensible si no se controla adecuadamente la recuperación de datos. En biomedicina, esto incluye historiales clínicos y datos genómicos.»
- **Explotación de vulnerabilidades** — «Actores maliciosos pueden manipular consultas mediante prompt injection para extraer datos privados o confidenciales del sistema.»
- **Necesidad de controles** — «Políticas estrictas de acceso, auditoría continua y validación de entradas y salidas son fundamentales en cualquier despliegue productivo.»

### Slide 36 — Ejemplo real de riesgo
> «Un chatbot empresarial con RAG filtra accidentalmente datos financieros confidenciales al no validar correctamente los permisos de acceso del usuario.»

| El problema | El impacto | La lección |
|---|---|---|
| Sistema de permisos mal configurado permite el acceso a documentos marcados como restringidos durante la fase de recuperación. | Información sensible queda expuesta a usuarios no autorizados, con potenciales implicaciones legales y regulatorias. | Validar y filtrar siempre la información recuperada antes de incluirla en el contexto y antes de mostrar la respuesta final. |

### Slide 37 — Buenas prácticas para mitigar riesgos

| Control de acceso granular | Encriptación y anonimización |
|---|---|
| Implementar permisos detallados a nivel de documento y usuario en todas las bases de datos del sistema RAG. | Proteger datos sensibles mediante cifrado en reposo y en tránsito; anonimizar información personal identificable. |

| Monitoreo continuo | Validación de salidas |
|---|---|
| Auditoría en tiempo real de consultas y accesos, complementada con pruebas de penetración periódicas. | Filtrar y revisar respuestas generadas antes de entregarlas al usuario final, evitando fuga de información. |

### Slide 38 — Limitaciones actuales y retos futuros

| Escalabilidad | Integración optimizada | Sesgos y transparencia |
|---|---|---|
| Manejar eficientemente grandes volúmenes de datos y consultas concurrentes sin degradar el rendimiento ni disparar los costes operativos. | Mejorar la coordinación entre los módulos de recuperación y generación para producir resultados más coherentes y menos fragmentados. | Evitar sesgos introducidos en la recuperación y generación, garantizando la explicabilidad de las respuestas para contextos regulados. |

> «A medida que RAG evoluciona, la comunidad de investigación trabaja activamente en resolver estos desafíos para hacer la tecnología más robusta y confiable en entornos críticos.»

### Slide 39 — Resumen y conclusiones de RAG

| Superación de limitaciones | Combinación poderosa |
|---|---|
| RAG es fundamental para superar las restricciones de los LLMs tradicionales en cuanto a conocimiento estático y alucinaciones. | Integra recuperación inteligente con generación precisa y contextualizada para respuestas verificables y citables. |
| **Cuidado necesario** | **Adopción creciente** |
| Requiere atención especial en el diseño del chunking, la evaluación continua y la seguridad de los datos. | Su uso se expande en múltiples industrias: biomedicina, legal, finanzas, y cualquier dominio con información dinámica. |

> «RAG representa un avance significativo en IA generativa. Dominar búsqueda híbrida, reranking y evaluación será clave para aplicaciones de próxima generación.»

### Slide 40 — Agenda (1 ✓, 2 ✓, 5 ✓ — el ítem 4 queda sin tildar pese a haberse dictado en 31-32)

### Slide 41 — Model Context Protocol (MCP)
> «El Protocolo de Contexto del Modelo representa un avance fundamental en la integración de sistemas de IA con fuentes de datos y herramientas externas. Exploraremos los desafíos que motivaron su desarrollo, su arquitectura técnica y su impacto en el ecosistema de desarrollo de aplicaciones inteligentes.»

### Slide 42 — Necesidad: Integración de IA con sistemas externos

| Conocimiento estático | Conectores personalizados | Silos de información |
|---|---|---|
| Los LLMs operan con conocimiento almacenado durante su entrenamiento, sin capacidad de acceder a información en tiempo real o sistemas de producción. | Cada integración requería el desarrollo de conectores únicos, generando costes elevados y un mantenimiento poco escalable para equipos de ingeniería. | La falta de estandarización creaba fragmentación de datos y duplicación masiva de esfuerzos de desarrollo en toda la industria. |

### Slide 43 — Historia y necesidad del MCP
> **«Noviembre 2024 — Anthropic lanza MCP como protocolo abierto para toda la comunidad de desarrollo de IA.»**

- **Visión «USB-C para IA»** — «Lenguaje común que conecta cualquier modelo con múltiples fuentes sin necesidad de conectores propietarios.»
- **Reducción de complejidad** — «De M×N integraciones (cada modelo con cada fuente) a M+N conexiones estandarizadas y reutilizables.»
- **Aceleración del desarrollo** — «Capa de abstracción universal que facilita la construcción rápida de aplicaciones inteligentes y componibles.»

### Slide 44 — ¿Por qué no usar solo HTTP o GraphQL?

| HTTP: Generalidad sin especialización | MCP: El estándar universal para IA |
|---|---|
| Heterogeneidad de interfaces entre servicios<br>Sin negociación de capacidades entre cliente y servidor<br>Sin gestión de sesiones persistentes<br>Sin propagación de contexto semántico | MCP es un protocolo bidireccional y optimizado para la comunicación entre agentes de IA y sistemas externos. Resuelve exactamente las limitaciones de HTTP y GraphQL en contextos de IA. |

Lo que MCP agrega, según el deck:
- Negociación de capacidades en tiempo de conexión
- Sesiones persistentes con estado compartido
- Propagación nativa de contexto semántico
- Orquestación dinámica de herramientas y fuentes

**GraphQL: Consultas potentes, orquestación limitada**
- Foco en fetch de datos, no en ejecución de acciones
- Sin orquestación dinámica de múltiples fuentes
- Sin estandarización de operaciones asíncronas

### Slide 45 — Agenda (1 ✓, 2 ✓, 4 ✓, 5 ✓, 6 ✓)

### Slide 46 — Protocolo JSON-RPC: Comunicación MCP
> «MCP utiliza JSON-RPC 2.0 como capa de transporte, permitiendo mensajes ligeros y estructurados entre cliente y servidor.»

Flujo de comunicación:
- Cliente envía solicitud JSON con método y parámetros
- Servidor procesa y responde con resultado o error estructurado
- **Protocolo sin estado con soporte para batch requests**

(Ejemplo JSON completo preservado en *Raw / preserved excerpts*.)

### Slide 47 — De herramientas hardcodeadas a MCP

| Herramienta Hardcodeada | Servidor MCP (Protocolo de Contexto del Modelo) |
|---|---|
| La lógica de la herramienta reside en el código del agente. | La herramienta opera como un proceso separado en localhost. |
| El agente conoce las herramientas en tiempo de compilación. | El agente consulta `tools/list` en tiempo de ejecución para descubrir herramientas. |
| Requiere copiar y pegar código para reutilizar la herramienta. | Cualquier cliente compatible con MCP puede conectarse y usarlo. |
| Necesidad de redeploy del agente para cualquier actualización. | Solo es necesario reiniciar el servidor MCP para aplicar actualizaciones. |
| Protocolo de comunicación específico del framework. | JSON-RPC estandarizado sobre HTTP para la comunicación. |

> «MCP separa las herramientas de los agentes — un servidor MCP puede ser usado por cualquier cliente compatible: Claude, ChatGPT, Cursor o tu propio agente.»

### Slide 48 — Ciclo de vida de una herramienta MCP

| # | Etapa | Qué pasa |
|---|---|---|
| 01 | El servidor MCP arranca | Declara sus herramientas: nombre, descripción y esquema de parámetros. |
| 02 | El agente se conecta | Como cliente MCP, descubre las herramientas disponibles vía `tools/list`. |
| 03 | El usuario envía una consulta | El LLM analiza las descripciones de herramientas y decide cuál invocar. |
| 04 | El agente llama la herramienta | A través del protocolo MCP con parámetros estructurados. |
| 05 | El servidor MCP ejecuta | Procesa la solicitud y devuelve un resultado estructurado. |
| 06 | El LLM usa el resultado | Continúa el razonamiento o responde al usuario con la información obtenida. |

### Slide 49 — Principios de diseño de herramientas MCP

| Principio 1: Nombres claros y descriptivos | Principio 2: Descripciones exhaustivas |
|---|---|
| Convención: `[verbo]_[sustantivo]_[contexto]`<br>Ejemplos correctos: `get_customer_by_email`, `search_products_by_category`, `calculate_shipping_cost_for_order`<br>Evitar: `process`, `fetch`, `do_thing` | La descripción es lo más importante. Debe responder: ¿Qué hace? ¿Cuándo usarla? ¿Cuándo NO usarla? ¿Qué formato tienen entradas/salidas? |

| Principio 3: Esquemas de parámetros simples | Principio 4: Formatos de respuesta consistentes |
|---|---|
| Investigación muestra: **1-3 parámetros → 90%+ precisión \| 4-6 parámetros → 75-85% \| 7+ parámetros → 60-70%**. Preferir múltiples herramientas simples sobre una herramienta compleja. | Usar un envelope estándar: `{ success, data, error, message }`. El agente sabe qué esperar, facilita el manejo de errores y el control de éxito/fallo. |

### Slide 50 — (sin título) Cómo conectar un servidor MCP a Claude Desktop
Tres métodos. **Método 1 — Desktop Extensions (5 min)**: «Abre Claude Desktop → Configuración (⚙️) → Extensions · Busca el servidor deseado (ej. "Filesystem") · Haz clic en Instalar → Concede permisos · Inicia un nuevo chat y prueba: "Lista los archivos de mi carpeta Documentos"».
**Método 2 — Configuración manual (JSON)**: rutas `macOS: ~/Library/Application Support/Claude/claude_desktop_config.json` · `Windows: %APPDATA%\Claude\claude_desktop_config.json`.
**Método 3 — Servidor MCP local (HTTP/SSE)**: «Asegurate de que el servidor esté corriendo en `http://localhost:8002/mcp` · Edita el archivo `claude_desktop_config.json` (mismas rutas que Método 2) · Agrega la entrada con transport "http"». Cierre: «4. Reinicia Claude Desktop y verificá que aparezca el ícono 🔌 en el chat.» y «Útil para servidores propios en desarrollo o herramientas internas de la organización.»

> ⚠️ «Seguridad: Usa servidores MCP de fuentes confiables. Los servidores que acceden a contenido externo pueden exponer a ataques de prompt injection. Verifica siempre el origen antes de instalar.»

(Ambos bloques de configuración JSON preservados verbatim en *Raw / preserved excerpts*.)

### Slide 51 — Ejemplo MCP Server
Botón enlazado a `https://localhost:3000/agents/model-context-protocol#from-hardcoded-tools-to-mcp` — **enlace roto: apunta al servidor de desarrollo local del autor.**

### Slide 52 — (sin título) Precisión del agente según complejidad de parámetros
Gráfico de barras (ver *Images / diagrams*, `slide-52-1.png`): **1-3 parámetros → 90 % · 4-6 parámetros → 80 % · 7+ parámetros → 65 %** de «Precisión del Agente (%)».

> «Más parámetros = mayor carga cognitiva = más confusión. Diseña múltiples herramientas simples en lugar de una herramienta compleja.»
> «Fuente: "Tool Space Interference in the MCP Era" — Microsoft Research»

### Slide 53 — Arquitectura multi-servidor: Agente de soporte al cliente
Slide de una sola frase, sin diagrama ni listado de servidores:
> «Cada servidor corre de forma independiente, gestiona su propio dominio y puede desplegarse o escalarse por separado. El agente no sabe ni le importa dónde viven las herramientas — las descubre todas vía `tools/list`.»

### Slide 54 — MCP con Claude: Casos de uso prácticos
> «Con servidores MCP conectados, Claude deja de ser un chatbot y se convierte en un hub de trabajo que accede directamente a tus archivos, APIs, bases de datos y herramientas.»

| Caso | Prompt de ejemplo | Herramientas |
|---|---|---|
| Gestión de código y GitHub | «Implementa la funcionalidad descrita en el issue JIRA ENG-4521 y crea un PR en GitHub.» | GitHub MCP, Filesystem MCP |
| Consultas a bases de datos | «Encuentra los emails de 10 usuarios aleatorios que usaron la feature ENG-4521 en nuestra base PostgreSQL.» | PostgreSQL MCP |
| Análisis de datos y monitoreo | «Revisa Sentry y Statsig para analizar el uso de la feature ENG-4521 y detectar errores.» | Sentry MCP, Statsig MCP |

| Integración de diseño | Automatización de flujos | Reacción a eventos externos |
|---|---|---|
| Actualiza nuestra plantilla de email estándar con los nuevos diseños de Figma publicados en Slack.<br>Herramientas: Figma MCP, Slack MCP | Crea borradores en Gmail invitando a esos 10 usuarios a una sesión de feedback sobre la nueva feature.<br>Herramientas: Gmail MCP | Claude puede reaccionar a mensajes de Telegram, Discord o eventos webhook en tiempo real mientras trabajas.<br>Herramientas: Telegram MCP, Discord MCP |

### Slide 55 — Servidores MCP populares: El ecosistema
> «**Más de 890 servidores MCP disponibles.** Aquí los más utilizados por categoría.»

| Archivos y código | Bases de datos | Productividad y comunicación |
|---|---|---|
| Filesystem: lectura/escritura de archivos locales. Git: gestión de repositorios. GitHub: PRs, issues, CI/CD. | PostgreSQL: consultas SQL. SQLite: bases de datos locales. Memory: grafo de conocimiento persistente. | Slack: mensajes y canales. Gmail: borradores y envíos. Google Drive: acceso a documentos. |

| Web y búsqueda | Diseño y APIs | Razonamiento avanzado |
|---|---|---|
| Brave Search: búsqueda web. Fetch: extracción de contenido web. Playwright/Puppeteer: automatización de navegador. | Figma: diseños e interfaces. OpenAPI: conecta cualquier API con spec Swagger. Google Maps: servicios de localización. | Sequential Thinking: descomposición de tareas complejas. Context7: documentación actualizada de librerías. |

**Dónde encontrar servidores MCP** (los cuatro enlaces, tal como figuran):
- Directorio oficial: `github.com/modelcontextprotocol/servers`
- Directorio comunidad: `claudemcp.org` (25+ servidores populares)
- Directorio completo: `skillsplayground.com/guides/mcp-servers` (890+ servidores)
- **Registro oficial MCP: `mcp.so`**

### Slide 56 — Agenda (1 ✓, 2 ✓, 4 ✓, 5 ✓, 6 ✓, 7 ✓; el ítem 4 pasa a llamarse «RAG: Chunking, Metadatos y Reranking»)

### Slide 57 — (sin título) El problema de selección de herramientas
> «La precisión del agente cae drásticamente a medida que aumenta el número de herramientas disponibles. Los LLMs hacen pattern-matching sobre descripciones — los espacios de opciones grandes los abruman.»
> «**Con 20+ herramientas en lista plana, el agente selecciona la herramienta incorrecta el 42% de las veces.** El diseño de herramientas es tan importante como su implementación.»
> «Source: aitutorial.dev/agents/tool-selection-and-optimization»

Gráfico de barras horizontales (`slide-57-1.png`): **1-5 herramientas → 92 % · 6-10 → 84 % · 11-20 → 71 % · 20+ → 58 %** de precisión.

### Slide 58 — Solución 1: Routing jerárquico

| ❌ Anti-patrón: Lista plana (20 herramientas) | ✅ Solución: Herramienta de routing (1 herramienta) |
|---|---|
| The agent sees all 20 tools at once → 58% accuracy. | The agent sees 1 routing tool → 90%+ accuracy. |

> «En lugar de 20 herramientas planas, el agente recibe 1 herramienta de routing. Elige dominio + acción, y en un segundo paso se invoca la herramienta específica.»

(Ambos bloques de código preservados verbatim en *Raw / preserved excerpts*.)

### Slide 59 — Solución 2: Grupos de herramientas por contexto (fase)
> «Una conversación de soporte tiene fases distintas. Mostrar solo las herramientas relevantes a la fase actual — el agente ve 2-4 en lugar de 20.»

| 01 | 02 | 03 |
|---|---|---|
| Fase: Saludo / Autenticación | Fase: Diagnóstico | Fase: Resolución |
| Herramientas activas (1): | Herramientas activas (2): | Herramientas activas (2): |
| `authenticateCustomer` | `searchKnowledgeBase`<br>`checkSystemStatus` | `createTicket`<br>`scheduleCallback` |
| El agente no necesita ver herramientas de búsqueda ni de tickets todavía. | El agente se enfoca en encontrar la causa del problema. | El agente no necesita herramientas de búsqueda en esta fase. |

| ❌ Sin grupos de contexto | ✅ Con grupos de contexto |
|---|---|
| 20 herramientas visibles → 58% precisión | 2-3 herramientas por fase → 90%+ precisión |

> «El principio: el agente no necesita ver todas las herramientas todo el tiempo. Filtra por fase o contexto para maximizar la precisión de selección.»

### Slide 60 — Solución 3: Diferenciación clara entre herramientas similares
> «Cuando dos herramientas suenan igual, el LLM las elige al azar o llama a ambas. La solución: cada herramienta necesita un propósito distinto con guía explícita de "Usar cuando" / "NO usar cuando".»

| Herramienta | Descripción | ✅ Usar cuando | ❌ NO usar cuando | Parámetros |
|---|---|---|---|---|
| `search_products_by_text` | Búsqueda de texto completo. | el cliente describe el producto con palabras («ratón inalámbrico»). | tienes el SKU exacto. | `query: string` |
| `get_product_by_sku` | Búsqueda exacta por SKU. | el cliente proporciona un SKU («PROD-001»). | para búsquedas de texto libre. | `sku: string` |
| `filter_products_by_attributes` | Filtro estructurado por atributos. | el cliente especifica categoría, precio o marca. | para búsqueda de texto. | `category?: string`, `priceMax?: number` |

Resultado: «"ratón inalámbrico" → `search_products_by_text` ✓ · "PROD-001" → `get_product_by_sku` ✓ · "ratones por menos de $20" → `filter_products_by_attributes` ✓»

### Slide 61 — Analytics de herramientas: Optimización continua en producción
> «En producción, monitorear cada llamada a herramientas permite detectar problemas sistémicos y optimizar el rendimiento del agente.»

| Síntoma | Detectar | Acción | Ejemplo de alerta |
|---|---|---|---|
| Herramientas sin uso | herramientas que nunca se invocan. | Eliminar o consolidar. | «Eliminar herramienta sin uso: `legacy_search`» |
| Herramientas lentas | herramientas con alta latencia promedio. | Implementar caché u optimizar la API. | «`slow_api` promedia 3000ms — considerar caché» |
| Herramientas con alta tasa de error | herramientas que fallan frecuentemente. | Revisar manejo de errores o mejorar descripción. | «`flaky_tool` falla el 40% — revisar error handling» |

**Key metrics to track:** `call_count` (número de invocaciones) · `success_rate` (tasa de éxito, %) · `avg_latency_ms` (latencia promedio en ms) · `last_used` (última vez utilizada).

> «Las herramientas que el agente nunca usa o usa mal son señales de diseño deficiente — no de capacidad del modelo. Itera sobre descripciones y esquemas antes de cambiar el LLM.»

### Slides 62, 63 y 64 — Repetición literal de las slides 41, 42 y 43
El deck no cierra: termina repitiendo palabra por palabra la introducción de MCP («Model Context Protocol (MCP)»), «Necesidad: Integración de IA con sistemas externos» y «Historia y necesidad del MCP». Las imágenes de la 63 son duplicados md5 de las de la 42. No hay slide de cierre, de bibliografía ni de preguntas.

---

## Definitions and terminology

Con la redacción del deck.

- **RAG (Retrieval-Augmented Generation)** — «combina lo mejor de dos mundos: el razonamiento de los LLMs con el conocimiento actualizado de bases de datos externas» (slide 3). Tres componentes: Recuperador, LLM, Base de conocimiento.
- **Ciclo Retrieve → Augment → Generate** (slide 4) — *Retrieve*: «Encontrar documentos relevantes para la consulta del usuario dentro de la base de conocimiento del sistema». *Augment*: «Insertar los documentos recuperados en el prompt como contexto adicional que el modelo puede utilizar». *Generate*: «El LLM responde usando únicamente el contexto proporcionado, fundamentando y citando su respuesta». (El título de la slide dice «los cuatro pasos», pero solo se enumeran tres.)
- **Índice invertido** (slides 10, 12) — «un mapa invertido: cada término apunta a los documentos que lo contienen». Cuatro fases: ingesta → tokenización y normalización (lowercase, stopwords, stemming) → construcción del índice → consulta con intersección de posting lists.
- **Posting list** (slide 15) — la lista de documentos asociada a un término en el índice invertido; «Se buscan las posting lists: "pescado" → [Doc1]».
- **TF (Term Frequency)** — «¿Qué tan frecuente es este término en este documento?» · `TF(t, d) = count(t in d) / total_terms(d)` (slide 13).
- **IDF (Inverse Document Frequency)** — «¿Qué tan raro es este término en todo el corpus?» · `IDF(t) = log(N / df(t))`. «Penaliza términos que aparecen en muchos documentos (son poco informativos)» (slide 13).
- **TF-IDF** — `TF-IDF(t, d) = TF(t, d) × IDF(t)`. Limitación declarada: «TF-IDF no satura — un término que aparece 100 veces vale 100x más que uno que aparece 1 vez» (slide 13).
- **BM25** — «extiende este modelo con ponderación por frecuencia de término (TF) e infrecuencia en el corpus (IDF), mejorando el ranking de resultados» (slide 12); es lo que «resuelve» la falta de saturación de TF-IDF (slide 13). El deck nunca da la fórmula de BM25 ni sus parámetros k1/b.
- **Búsqueda léxica** (slide 22) — «BM25 / Keywords». Rápida, precisa en términos exactos, sin GPU; no reconoce sinónimos ni abstracciones.
- **Búsqueda semántica / densa** (slides 17, 22) — «Embeddings / Vectores». Sinónimos, multilenguaje, relaciones conceptuales; más lenta (100-500 ms), requiere GPU.
- **Búsqueda híbrida** (slides 10, 22) — «BM25 + Vectorial», «combina precisión léxica con comprensión semántica», «reranking para fusionar resultados», «estándar en sistemas RAG de producción».
- **Embedding** (slide 18) — «convierte texto en un punto en un espacio de N dimensiones». Se entrena de forma contrastiva con «millones de pares (pregunta, respuesta relevante)». Dimensionalidad típica: 384-3072. «El embedding captura semántica, no sintaxis.»
- **Similitud coseno** (slide 19) — `cos(θ) = (A · B) / (||A|| × ||B||)`. «cos(0°) = 1 → idénticos. cos(90°) = 0 → sin relación. cos(180°) = -1 → opuestos.» Invariante a la longitud del texto.
- **ANN (Approximate Nearest Neighbors)** (slides 19, 20) — índices que «sacrifican un poco de precisión por velocidad sub-lineal», frente al O(n) de la búsqueda exacta.
- **HNSW / IVF** (slide 20) — los dos índices ANN nombrados: «Se buscan los K vectores más cercanos en la base de datos vectorial usando índice HNSW o IVF. Sub-lineal en tiempo.» El deck no expande las siglas ni explica su funcionamiento.
- **Chunking** (slide 31) — «divide documentos extensos en fragmentos manejables». Cuatro estrategias: tamaño fijo, semántico, estructura-aware, con metadatos. Tensión declarada: «fragmentos pequeños (100-200 tokens) mejoran la precisión pero pierden contexto; fragmentos grandes (1000+) mantienen contexto pero diluyen la señal de recuperación».
- **Metadatos de chunk** (slide 32) — obligatorios: identificador de fuente, timestamp, posición del chunk. Condicionales: autor/departamento, tipo y versión de documento, jerarquía de sección, idioma, score de calidad.
- **Recuperación en dos etapas** (slides 7, 26) — Etapa 1 *recall* (red amplia, top-50); Etapa 2 *precision* (cross-encoder, top-3 a top-5).
- **Reranking** (slide 26) — «filtra el ruido y se queda solo con los documentos verdaderamente relevantes».
- **Cross-encoder** (slides 27, 28) — «recibe la query Y el documento juntos como input: `[CLS] query [SEP] documento [SEP]`», salida «score de relevancia (0 a 1)». «Analiza la interacción entre query y documento.» Limitación: «O(n) — no escala a millones de docs». Modelos citados: Cohere Rerank, BGE-Reranker, ms-marco-MiniLM.
- **Bi-encoder** (slide 28) — embeddea query y documento por separado y compara vectores; «Escalable — O(1) por doc en query time» porque los embeddings se pre-computan. «Pierde el contexto conjunto.»
- **RRF (Reciprocal Rank Fusion)** (slide 27) — `RRF(d) = Σ 1 / (k + rank_i(d))`, **con `k=60` por defecto**. «Fusiona los dos rankings en uno solo… Penaliza documentos que aparecen tarde en ambas listas.» «RRF es robusto: no requiere normalizar scores de distintas fuentes.»
- **Métricas de evaluación** (slides 7, 34) — retrieval: `Recall@k`, `NDCG`; generación: `faithfulness`. Las tres métricas nombradas en la slide 34: *Context Relevance*, *Answer Faithfulness*, *Answer Relevance*.
- **Prompt injection** (slides 35, 50) — «Actores maliciosos pueden manipular consultas mediante prompt injection para extraer datos privados o confidenciales del sistema»; en MCP, «los servidores que acceden a contenido externo pueden exponer a ataques de prompt injection».
- **MCP (Model Context Protocol)** (slides 41, 44) — «El Protocolo de Contexto del Modelo»; «un protocolo bidireccional y optimizado para la comunicación entre agentes de IA y sistemas externos». Metáfora del deck: **«USB-C para IA»**. Beneficio estructural: «De M×N integraciones (cada modelo con cada fuente) a M+N conexiones estandarizadas y reutilizables».
- **JSON-RPC 2.0** (slide 46) — «MCP utiliza JSON-RPC 2.0 como capa de transporte, permitiendo mensajes ligeros y estructurados entre cliente y servidor». Descrito como «Protocolo sin estado con soporte para batch requests».
- **`tools/list`** (slides 47, 48, 53) — el método por el que «el agente consulta en tiempo de ejecución para descubrir herramientas».
- **`tools/call`** (slide 46) — el método del ejemplo JSON-RPC.
- **Servidor MCP** (slide 47) — «La herramienta opera como un proceso separado en localhost»; «Cualquier cliente compatible con MCP puede conectarse y usarlo».
- **Tool selection** (slide 57) — el problema de que «la precisión del agente cae drásticamente a medida que aumenta el número de herramientas disponibles. Los LLMs hacen pattern-matching sobre descripciones».
- **Routing jerárquico** (slide 58) — sustituir N herramientas planas por una sola herramienta `route_to_domain` que recibe dominio + acción.
- **Grupos de herramientas por contexto / fase** (slide 59) — exponer solo las 2-4 herramientas relevantes a la fase conversacional en curso.
- **Envelope de respuesta** (slide 49, Principio 4) — `{ success, data, error, message }`.
- **Convención de nombres de herramienta** (slide 49, Principio 1) — `[verbo]_[sustantivo]_[contexto]`.

---

## Evidence and examples

Cifras, ejemplos y material reutilizable, con la slide de origen.

### Cifras cuantitativas

| Cifra | Texto del deck | Slide | Fuente citada |
|---|---|---|---|
| 70 % | «El 70% de los fallos de RAG provienen de la recuperación, no de la generación» | 34 | **ninguna** |
| 42 % | «Con 20+ herramientas en lista plana, el agente selecciona la herramienta incorrecta el 42% de las veces» | 57 | aitutorial.dev/agents/tool-selection-and-optimization |
| 92 / 84 / 71 / 58 % | Precisión del agente por cantidad de herramientas: 1-5 → 92, 6-10 → 84, 11-20 → 71, 20+ → 58 | 57 (gráfico) | ídem |
| 58 % → 90 %+ | «The agent sees all 20 tools at once → 58% accuracy» vs. «1 routing tool → 90%+ accuracy» | 58 | — |
| 58 % → 90 %+ | «20 herramientas visibles → 58% precisión» vs. «2-3 herramientas por fase → 90%+ precisión» | 59 | — |
| 90 %+ / 75-85 % / 60-70 % | «1-3 parámetros → 90%+ precisión \| 4-6 parámetros → 75-85% \| 7+ parámetros → 60-70%» | 49 | «Investigación muestra» (sin nombrar) |
| 90 / 80 / 65 % | Gráfico «Precisión del Agente (%)»: 1-3 params → 90, 4-6 → 80, 7+ → 65 | 52 (gráfico) | «Tool Space Interference in the MCP Era» — Microsoft Research |
| 890+ | «Más de 890 servidores MCP disponibles» | 55 | skillsplayground.com/guides/mcp-servers |
| 25+ | «claudemcp.org (25+ servidores populares)» | 55 | claudemcp.org |
| 85-92 % | Relevancia de la búsqueda híbrida | 22 | — |
| 100-500 ms | Latencia de la búsqueda semántica | 22 | — |
| ~$0.0001 / ~$0.001-0.01 / ~$0.002-0.015 por query | Coste de búsqueda léxica / semántica / híbrida | 22 | — |
| 100K+ → 50 → 5 | Embudo del reranking: corpus total → candidatos Stage 1 → resultado final | 26 | — |
| 20-100 / 3-5 | «mantener el pool de candidatos en 20-100 docs y el top_k final en 3-5» | 27 | — |
| k = 60 | «RRF(d) = Σ 1 / (k + rank_i(d))   [k=60 por defecto]» | 27 | — |
| 384-3072 | Rango de dimensionalidad de embeddings | 18 | — |
| 100-200 / 1000+ tokens | Tensión de tamaño de chunk | 31 | — |
| 800-1000 / 600-800 / 1000-1500 / 1000-1200 chars | Chunk recomendado para blog posts / docs técnicos / contratos / papers | 32 | — |
| 0.91 / 0.76 / 0.12 / 0.87 | Similitudes coseno de ejemplo (gato-felino, gato-perro, gato-auto, query-Doc1) | 19 | — |
| ~0.89 | «"infarto de miocardio" y "ataque al corazón" tienen similitud coseno ~0.89» | 20 | — |
| Noviembre 2024 | «Anthropic lanza MCP como protocolo abierto» | 43, 64 | — |

### El corpus de juguete (hilo conductor de las slides 12-20)

Tres documentos que reaparecen en cinco slides:
- Doc 1: «el gato come pescado fresco» (5 tokens)
- Doc 2: «el perro come carne y hueso» (6 tokens)
- Doc 3: «el gato y el perro son amigos» (7 tokens)

Se usan para mostrar, en el mismo corpus, la diferencia entre recuperación léxica (slide 15: query «pescado fresco» → solo Doc1 matchea, score 0.44) y recuperación semántica (slide 20: query «¿Qué animales comen pescado?» → Doc1 0.91, Doc3 0.43, Doc2 0.21). Es el ejemplo más reutilizable del deck para clase.

### Ejemplos de dominio biomédico
- Ontologías médicas citadas: **SNOMED, ICD-10** (slides 9, 10, 22).
- «"leucemia" aparece en 200 documentos → df("leucemia") = 200»; «si tenemos 10.000 artículos médicos, N = 10.000» (slide 13).
- «En biomedicina, esto incluye historiales clínicos y datos genómicos» (slide 35).
- «"infarto de miocardio" y "ataque al corazón"» como par semánticamente cercano (slide 20).
- Fuentes típicas: «PDFs, artículos científicos, guías clínicas, informes. La fuente más común en biomedicina» (slide 9).

### Caso de incidente (slide 36)
> «Un chatbot empresarial con RAG filtra accidentalmente datos financieros confidenciales al no validar correctamente los permisos de acceso del usuario.»

Sin empresa, fecha ni fuente — es un caso ilustrativo, no un incidente documentado.

### Herramientas, modelos y vendors nombrados
- **Bases vectoriales:** Pinecone · Weaviate · Qdrant · Chroma · pgvector (slide 10).
- **Índices invertidos:** Elasticsearch · OpenSearch · Apache Solr · Typesense (slide 10).
- **Híbridos:** Elasticsearch · Weaviate · Azure AI Search · MongoDB Atlas (slide 10).
- **Modelos de embeddings:** `text-embedding-3-small` (OpenAI) · `all-MiniLM-L6-v2` (open source) · `embed-multilingual-v3` (Cohere) (slide 18).
- **Rerankers:** Cohere Rerank · BGE-Reranker · ms-marco-MiniLM (slides 27, 28).
- **Servidores MCP:** Filesystem · Git · GitHub · PostgreSQL · SQLite · Memory · Slack · Gmail · Google Drive · Brave Search · Fetch · Playwright/Puppeteer · Figma · OpenAPI · Google Maps · Sequential Thinking · Context7 (slide 55); más Sentry, Statsig, Telegram y Discord (slide 54).
- **Frameworks/clientes:** LangChain (slides 6, 11, 16, 21) · Claude, ChatGPT, Cursor (slide 47) · Claude Desktop (slide 50).

### Enlaces que aparecen en el deck

| Destino | Dónde | Estado |
|---|---|---|
| `https://aitutorial.dev/rag/fundamentals` | botón en slides 6, 11, 16, 21 | externo, plausible |
| `https://aitutorial.dev/rag/reranking` | botón en slide 29 | externo, plausible |
| `https://aitutorial.dev/agents/tool-selection-and-optimization` | cita al pie de slide 57 | externo, plausible |
| `https://localhost:3000/agents/model-context-protocol#from-hardcoded-tools-to-mcp` | botón en slide 51 | **ROTO — dev server local del autor** |
| `https://github.com/modelcontextprotocol/servers` | slide 55 | válido |
| `https://claudemcp.org` | slide 55 | comunitario |
| `https://skillsplayground.com/guides/mcp-servers` | slide 55 | tercero |
| `https://mcp.so` | slide 55 | **etiquetado «Registro oficial MCP» — no lo es** |

Los bloques de configuración JSON y de código (slides 46, 50, 58) se preservan verbatim en *Raw / preserved excerpts*: son material de clase reutilizable.

---

## Inconsistencies / open questions

### Ya señalados en el despacho de ingesta — confirmados

1. **Slide 51 — enlace roto al dev server local del autor.** El botón «Haz clic aquí» apunta a `https://localhost:3000/agents/model-context-protocol#from-hardcoded-tools-to-mcp`. Es un enlace *visible y clickeable en el deck*: para cualquier persona que no sea el autor con su servidor corriendo, no resuelve. Además usa `https` sobre `localhost:3000`, que normalmente sirve `http` — fallaría incluso en la máquina del autor. Confirmado tanto en el Markdown como en `_manifest.json` (campo `hipervinculo` de `slide-51-1.png`). **Bloqueante si el deck se reutiliza tal cual.**
2. **Slide 55 — `mcp.so` etiquetado «Registro oficial MCP».** `mcp.so` es un marketplace/directorio comunitario, no el registro oficial del protocolo. Agravante: la misma lista ya llama «Directorio oficial» a `github.com/modelcontextprotocol/servers`, de modo que el deck aplica el adjetivo «oficial» a dos cosas distintas en cuatro líneas consecutivas, y ninguna de las dos es el *MCP Registry* propiamente dicho.
3. **Slide 34 — «el 70% de los fallos de RAG provienen de la recuperación» sin fuente.** Es la cifra más fuerte del bloque RAG (justifica todo el énfasis en retrieval y reranking) y llega sin cita, sin fecha y sin definición de qué cuenta como «fallo». No hay pie de página ni enlace en la slide.
4. **Bloque MCP (slides 41-49, y por extensión 46-55) sin la spec oficial.** El deck explica JSON-RPC 2.0, `tools/list`, `tools/call`, el ciclo de vida y los transportes sin apuntar nunca a `modelcontextprotocol.io` ni a la especificación versionada. La única URL «oficial» que ofrece es el repo de servidores de ejemplo, que no es la spec.

### Encontrados en esta ingesta

**Contradicciones internas**

5. **Slide 44 vs. slide 46 — ¿MCP tiene estado o no?** La 44 vende MCP por sus «Sesiones persistentes con estado compartido» como ventaja frente a HTTP; dos slides después, la 46 describe la capa de transporte como «Protocolo sin estado con soporte para batch requests». Las dos afirmaciones conviven sin reconciliarse (la distinción real es entre el transporte JSON-RPC y la sesión MCP, pero el deck nunca la hace).
6. **Slide 14 vs. slide 15 — el mismo IDF con dos valores.** Para el mismo corpus de 3 documentos, la slide 14 calcula `IDF("pescado") = log(3/1) = 0.48` (log base 10) y la slide 15 calcula `IDF("pescado") = log(3/1) = 1.10` (logaritmo natural). El TF-IDF resultante difiere en consecuencia: 0.10 en la 14, 0.22 en la 15. El deck nunca declara la base del logaritmo. Un alumno que rehaga las cuentas obtiene números distintos según la slide que mire.
7. **Slide 14 — error aritmético en la fila «el».** Doc1 es «el gato come pescado fresco» (5 tokens, un solo «el»), pero la tabla consigna `TF (Doc1) = 2/5 = 0.40`. Debería ser 1/5 = 0.20. El 2/5 parece arrastrado de Doc3 («el gato y el perro son amigos», que sí tiene dos «el», pero 7 tokens). El resultado final no cambia porque el IDF es 0, lo que hace el error más fácil de pasar por alto y más confuso si alguien lo audita.
8. **Slide 20 — el ejemplo se contradice con su propia moraleja.** El pie dice: «Doc1 es recuperado aunque la query no contenga exactamente "gato" ni "pescado"». La query mostrada es «¿Qué animales comen pescado?» — que sí contiene «pescado». El argumento a favor de la búsqueda densa se apoya en un ejemplo que no lo sostiene.
9. **Slide 27 — RRF Score mal calculado para Doc C.** Con `k=60`: Doc A = 1/61 + 1/63 = 0.0323 ✓ (dice 0.032); Doc B = 1/65 + 1/61 = 0.0318 ✓ (dice 0.032); **Doc C = 1/62 + 1/68 = 0.0308, pero la tabla dice 0.028**. Es la única tabla del deck donde se puede verificar la fórmula que se acaba de enseñar, y no cierra.
10. **Slide 4 — «Los cuatro pasos de RAG» enumera tres.** El título promete cuatro; la tabla da Retrieve, Augment, Generate. No hay cuarto paso en ninguna parte de la slide.
11. **Slide 46 — la respuesta JSON-RPC del ejemplo no es JSON-RPC.** El request está bien formado (`jsonrpc`, `method`, `params`, `id`), pero la respuesta se muestra como `{ "temperature": 22, "condition": "soleado" }`, sin los campos `jsonrpc`, `result` ni `id` que la especificación 2.0 exige. Material de clase que no cumple el protocolo que enseña.
12. **Slide 47 / slide 50 — el transporte stdio nunca se nombra.** La 47 afirma «JSON-RPC estandarizado sobre HTTP» y «un proceso separado en localhost»; la 50, Método 2, muestra una configuración `command` + `args` con `npx` — que es transporte **stdio**, no HTTP. El deck presenta como HTTP el modo de conexión más común de MCP local y solo nombra HTTP/SSE en el Método 3.

**Cifras sin respaldo verificable**

13. **Slide 52 — «Tool Space Interference in the MCP Era», Microsoft Research.** Es la única atribución académica del deck y no corresponde a una publicación localizable de Microsoft Research. Además, sus valores (90 / 80 / 65) son puntos únicos, mientras que la slide 49 presenta el mismo hallazgo como rangos (90 %+ / 75-85 % / 60-70 %) atribuidos a un genérico «Investigación muestra». Las dos slides están a tres de distancia y no se referencian entre sí.
14. **Slides 57-59 — el 58 % se repite como si fuera un dato medido.** Aparece tres veces (57, 58, 59) con una única fuente: `aitutorial.dev/agents/tool-selection-and-optimization`, un sitio de tutoriales, no un estudio. La cifra de 90 %+ para las soluciones propuestas (routing, grupos por fase) no tiene *ninguna* fuente: es la promesa de mejora del deck y llega sin respaldo.
15. **Slide 22 — costos, latencias y relevancia sin fuente ni fecha.** «85-92% relevancia», «100-500ms», «~$0.0001/query», «~$0.002-0.015/query». Son las cifras que un alumno usaría para justificar una decisión de arquitectura y no hay de dónde agarrarse.
16. **Slide 55 — tres directorios, tres números, ninguna fecha.** 25+ (claudemcp.org), 890+ (skillsplayground.com) y el repo oficial sin número, presentados juntos. Con «Última Modificación: Abril, 2026» en portada y el lanzamiento de MCP en noviembre de 2024, cualquier recuento del ecosistema está desactualizado por diseño: falta un «a la fecha de».

**Cobertura prometida y no entregada**

17. **La agenda anuncia cuatro temas que no existen en el deck.** Seis de las ocho renditions de la agenda (slides 8, 25, 30, 40, 45, 56) describen el ítem 5 como «Métricas clave, **LLM-as-Judge**, riesgos, **GraphRAG**, **Agentic RAG** y **RAG Multimodal**». Ninguna slide cubre LLM-as-Judge, GraphRAG, Agentic RAG ni RAG Multimodal. El bloque real (34-39) son métricas, seguridad y conclusiones.
18. **La agenda cambia de redacción a mitad de camino.** El ítem 5 alterna entre «RAG: Evaluación y Seguridad — Riesgos y evaluacion» (slides 2 y 33, con «evaluacion» sin tilde) y la versión larga con los cuatro temas fantasma. El ítem 4 pasa a llamarse «RAG: Chunking, Metadatos y Reranking» recién en la slide 56.
19. **Los ✓ de la agenda no cuadran.** El ítem 3 («RAG: Reranking y Precisión») **nunca** recibe ✓, ni siquiera en la última agenda (slide 56), pese a haberse dictado en las slides 26-29. La slide 40 marca el ítem 5 ✓ mientras deja el 4 sin marcar, aunque el 4 (chunking, slides 31-32) se dictó antes que el 5. La slide 30, ya pasado el bloque de reranking, sigue con el 3 sin marcar.
20. **Slide 53 — la arquitectura multi-servidor se anuncia y no se muestra.** Título: «Arquitectura multi-servidor: Agente de soporte al cliente». Contenido: una sola frase. No hay diagrama, no hay lista de servidores, no hay ejemplo del agente de soporte que el título nombra — pese a que las slides 59 y 60 después usan ese mismo agente de soporte como caso.
21. **Slides 62-64 — el deck no cierra: repite.** Las tres últimas slides son copia literal de las slides 41, 42 y 43 (introducción a MCP), con las mismas imágenes (duplicados md5 confirmados en el manifest). No hay slide de conclusiones de MCP, ni de bibliografía, ni de preguntas. Parece un resto de edición: alguien pegó el bloque de MCP dos veces y borró solo la primera mitad de la copia.
22. **Etiquetas de sección cruzadas.** La slide 29 («Ejemplo de Ranking», demo de reranking) está etiquetada *MCP: ARQUITECTURA Y USO*. Las slides 62-64 están etiquetadas *MCP: FUNDAMENTOS* después del bloque *MCP: DISEÑO DE HERRAMIENTAS*. Las slides 31-32 dicen «RAG: CHUNKING, METADATOS Y RERANKING» cuando el reranking real vive en 26-28 bajo otra etiqueta.
23. **BM25 se invoca doce veces y nunca se define.** Aparece en las slides 10, 12, 13, 22, 26, 27 como la línea de base léxica de todo el pipeline, y el deck solo dice que «extiende» TF-IDF con TF e IDF. No hay fórmula, no hay k1/b, no hay explicación de la saturación que supuestamente resuelve. Mismo caso, más leve, con HNSW e IVF (nombrados en la slide 20, nunca expandidos).

**Idioma y registro**

24. **Slide 58 — tabla en inglés dentro de un deck en español.** «The agent sees all 20 tools at once → 58% accuracy.» / «The agent sees 1 routing tool → 90%+ accuracy.» Los comentarios del código inmediatamente debajo dicen lo mismo en español («// El agente ve 20 herramientas → 58% precisión»). Traducción a medio hacer.
25. **Otros restos en inglés:** «Where:» en el bloque de fórmula de la slide 19 y «Key metrics to track:» en la slide 61. Los términos técnicos en inglés (recall, faithfulness, chunking, reranking, cross-encoder) son deliberados y consistentes; estos tres no.
26. **Mezcla de voseo rioplatense y tuteo peninsular.** Voseo: «¿Cuándo necesitás RAG?», «solo actualizás tu repositorio», «No podés rastrear», «Asegurate de que el servidor esté corriendo», «verificá que aparezca el ícono». Tuteo peninsular: «Abre Claude Desktop», «Busca el servidor deseado», «Haz clic en Instalar», «Edita el archivo», «Usa servidores MCP de fuentes confiables», «Verifica siempre el origen», «Diseña múltiples herramientas simples», «Itera sobre descripciones». La slide 50 concentra el choque: sus tres métodos están en tuteo y la línea de cierre en voseo. **La imagen del botón que se repite seis veces dice «Haz clic aquí»** — el elemento más visible del deck está en la variante equivocada para una cátedra argentina.
27. **Slide 50 — numeración huérfana.** Los pasos del Método 3 son bullets sin numerar, pero el último es «4. Reinicia Claude Desktop y verificá que aparezca el ícono 🔌» — un «4.» sin 1, 2 ni 3 visibles.
28. **Autoría ambigua.** La slide 1 dice «Autor: Paulo Veiga / Marcos Sanchez Sorondo» sin distinguir roles (¿coautores? ¿autor y adaptador?), y el apellido va sin tilde («Sanchez» por «Sánchez»).

**Gaps de la extracción a Markdown (no del deck original)**

29. **Dos imágenes quedaron fuera del Markdown.** `slide-26-1.png` y `slide-26-4.png` figuran en `_manifest.json` y están en disco, pero ninguna aparece referenciada en `AIG4B-Clase-5-RAG-y-MCP.md` (120 referencias contra 122 colocaciones). Ambas son duplicados md5 del mismo icono de flecha que la slide 26 ya muestra en otras cuatro posiciones, así que no se pierde contenido — pero la extracción es demostrablemente lossy y conviene no confiar en el `.md` como inventario de imágenes.
30. **Las tablas de SmartArt llegan fragmentadas y desordenadas.** El extractor aplana la geometría, de modo que en varias slides el cuerpo de un bullet precede a su título o las columnas se parten en dos tablas. Casos más visibles: slide 12 (los cuatro pasos del índice invertido salen 2-1-4-3), slide 14 (la fila «gato» se cae de la tabla y queda como bullets), slide 15 (las cuatro etapas invertidas), slide 20 (ídem), slide 27 (ídem), slide 32 (la tabla de tamaños se parte: «Contratos» y «Papers» quedan sueltos), slide 50 (los pasos del Método 2 aparecen intercalados con los del 3). El orden reconstruido en *Key claims* es mi lectura, no el orden literal del `.md`.
31. **Recuento de tablas.** El despacho anticipaba «70 bloques de tabla»; el conteo real sobre el `.md` da **42 bloques contiguos y 150 filas** (42 separadores `|---|`). La diferencia probablemente venga de contar tablas del `.pptx` antes del aplanado, o de contar cada fragmento por separado. Dejo constancia para que nadie use «70» como cifra de control.

**Nota sobre las imágenes**

32. **Casi ninguna «figura» tiene contenido.** De las 14 imágenes clasificadas `figura` en el manifest, solo tres cargan información: el logo de la Austral (slide 1) y los dos gráficos de barras (slides 52 y 57). Las once restantes son cromo decorativo de SmartArt — marcos de tarjeta vacíos, flechas grises, chevrons con iconos pero **sin una sola etiqueta de texto**, porque el texto vive en los cuadros de texto de la slide, no en la imagen. Consecuencia práctica: **los diagramas de este deck no son reutilizables como imágenes**; quien quiera reproducirlos tiene que reconstruirlos desde el texto.
33. **`slide-15-1.png` y `slide-15-2.png` son la misma flecha con dos md5.** Difieren en 99 EMU de ancho (≈ 0,0001 pulgadas) — el manifest las cuenta como dos imágenes únicas, pero visualmente son idénticas. El recuento de «64 únicas» está inflado al menos en uno.
34. **`slide-55-1.png` rasteriza casi en blanco.** 60×60 px, 540 bytes, RGBA con contenido real pero de trazo tan fino que a tamaño nativo se lee como una casilla vacía. Su SVG original (`slide-55-1.svg`, viewBox 1106×905) sí conserva el trazo. Si esa slide se re-renderiza, conviene usar el SVG.

### Preguntas abiertas para el presentador

- ¿Qué reemplaza al enlace de la slide 51? Sin él, la demo «Ejemplo MCP Server» no tiene a dónde ir.
- ¿De dónde sale el 70 % de la slide 34? Si no hay fuente, ¿se baja a «buena parte» o se cita un estudio real?
- ¿Se dictan LLM-as-Judge, GraphRAG, Agentic RAG y RAG Multimodal, o se saca la promesa de la agenda?
- ¿La base del logaritmo en TF-IDF es 10 o *e*? Hay que unificar slides 14 y 15 antes de que alguien rehaga las cuentas.
- ¿Las slides 62-64 se borran, o falta un cierre que nunca se escribió?
- ¿Se unifica el registro a voseo (incluido el botón «Haz clic aquí», que está en seis slides)?

---

## Images / diagrams

> **Los bytes se retiraron el 2026-09-03.** Ninguna de las 198 imágenes del export estaba enlazada desde un `.md`, y el deck reescrito no referencia ninguna: las figuras se rehicieron como diagramas ASCII. De las tres con contenido real, el logo institucional lo aporta `config/logo.png` del repositorio, y los dos gráficos de barras son los que esta misma revisión desacreditó por falta de fuente. Las descripciones y transcripciones de abajo se conservan intactas: son el registro de qué había. Los originales siguen en `talksmith-aig4b`.

**64 imágenes únicas en 122 colocaciones**, más **75 SVG originales**. Los bytes estaban en la carpeta compañera: `research/corpus/AIG4B-Clase-5-RAG-y-MCP.md/images/` (122 PNG + 75 SVG + copia de `_manifest.json` = 198 archivos, 1,9 MB, md5 idénticos al origen).

Sobre los SVG: 75 de los PNG proceden de un vectorial (campo `svg_original` del manifest). Los `.svg` están copiados a la carpeta compañera junto a su PNG homónimo (`slide-NN-M.svg` al lado de `slide-NN-M.png`) y son la fuente preferible para re-render. No se abrieron ni se transcribieron individualmente: son los mismos glifos que sus PNG, en vectorial.

Convención de esta sección: cada imagen se describe **una vez**, en su primera aparición; las repeticiones se listan al final en una tabla de remisión.

### Figuras con contenido real (3)

**`AIG4B-Clase-5-RAG-y-MCP.md/images/slide-01-1.png`** — 440×364 px · slide 1
- Depiction: Logo institucional de la Universidad Austral en azul marino sobre blanco: sello circular con un árbol estilizado y cuatro estrellas de cuatro puntas en la copa, rodeado por una leyenda circular en latín; debajo, el nombre de la casa en dos líneas.
- Why it matters: Marca institucional del deck. Único elemento de identidad visual; fija la procedencia académica del material.
- Transcribed text (latín + español, en el original): sello — «STVDIORVM · AVSTRALIS · VNIVERSITAS» (leyenda circular). Bajo el sello — «UNIVERSIDAD» / «**AUSTRAL**».

**`AIG4B-Clase-5-RAG-y-MCP.md/images/slide-52-1.png`** — 2398×1342 px · slide 2 del par de la slide 52
- Depiction: Gráfico de barras verticales, tres barras, fondo blanco con grilla horizontal punteada gris. Las barras van de granate oscuro (izquierda) a rojo coral (derecha), siguiendo la paleta roja del deck. Cada barra lleva su valor impreso dentro, cerca del tope. El eje Y está rotulado arriba a la derecha y su escala corre por el margen derecho, no por el izquierdo. La barra más alta no llega al tope del área de trazado: la escala se extiende más allá de 90.
- Why it matters: Es el respaldo visual del Principio 3 de diseño de herramientas MCP (slide 49) y la única visualización del deck con una atribución académica. Sostiene la recomendación operativa central del bloque MCP: preferir muchas herramientas simples antes que una compleja. Sus valores son puntos únicos, mientras que la slide 49 enuncia rangos — ver *Inconsistencies* punto 13.
- Transcribed text (**todo en español**):
  - Título del eje Y (arriba a la derecha): «Precisión del Agente (%)»
  - Marcas del eje Y (margen derecho, de arriba abajo): `80`, `60`, `40`, `20`, `0`
  - Etiquetas del eje X (izquierda a derecha): «1−3 parámetros», «4−6 parámetros», «7+ parámetros»
  - Título del eje X: «Número de Parámetros»
  - Valores dentro de las barras: `90` (1−3, granate oscuro, texto blanco), `80` (4−6, rojo medio, texto blanco), `65` (7+, rojo coral, texto negro)

**`AIG4B-Clase-5-RAG-y-MCP.md/images/slide-57-1.png`** — 2226×1248 px · slide 57
- Depiction: Gráfico de barras horizontales, cuatro barras apiladas verticalmente, fondo blanco con grilla vertical punteada gris cada 10 unidades. Degradé de granate oscuro (barra superior, la más larga) a rosa coral (barra inferior, la más corta). Cada barra lleva su valor impreso en el extremo derecho, dentro de la barra. El eje X va de 0 a 100 y el área de trazado se extiende más allá de la barra más larga.
- Why it matters: Es la evidencia visual del problema que abre el bloque «MCP: Diseño de Herramientas» — la caída monótona de precisión al crecer el catálogo de herramientas. El 42 % citado en el texto de la slide es el complemento del 58 % de la barra inferior (100 − 58), así que gráfico y texto son consistentes entre sí, aunque ambos dependan de la misma fuente única (aitutorial.dev).
- Transcribed text (**todo en español**):
  - Título del eje Y (arriba a la izquierda): «Número de Herramientas»
  - Etiquetas del eje Y (de arriba abajo): «1−5 herramientas», «6−10 herramientas», «11−20 herramientas», «20+ herramientas»
  - Marcas del eje X: `0`, `10`, `20`, `30`, `40`, `50`, `60`, `70`, `80`, `90`, `100`
  - Título del eje X: «Precisión del Agente (%)»
  - Valores en las barras: `92` (1−5, texto blanco), `84` (6−10, texto blanco), `71` (11−20, texto blanco), `58` (20+, texto negro)

### Figuras decorativas sin texto (11)

Todas se abrieron y verificaron una por una. Ninguna contiene texto transcribible: son el chasis gráfico de SmartArt, con las etiquetas viviendo en los cuadros de texto de la slide.

**`AIG4B-Clase-5-RAG-y-MCP.md/images/slide-07-1.png`** — 2378×1026 px · slide 7
- Depiction: Cuatro flechas horizontales apiladas en escalera descendente, en degradé de granate oscuro a rosa coral, cada una apuntando a la derecha y terminando un poco antes que la anterior. Sin etiquetas.
- Why it matters: Es el soporte visual del «Pipeline de RAG en producción»; las cuatro flechas corresponden a Consulta Usuario → Recuperación Rápida → Reranking Cross-Encoder → Generación LLM, pero esa correspondencia solo existe en el texto de la slide.
- Transcribed text: (ninguno)

**`AIG4B-Clase-5-RAG-y-MCP.md/images/slide-23-1.png`** — 2380×1452 px · slide 23
- Depiction: Cinco chevrons (paralelogramos escalonados en diagonal descendente) en degradé granate→coral, el último rematado en punta de flecha grande hacia la derecha. Cada chevron lleva un pictograma blanco de línea: (1) busto de persona, (2) grafo de nodos con flecha ascendente, (3) cilindro de base de datos, (4) hoja de documento con líneas de texto, (5) dos globos de diálogo.
- Why it matters: Único diagrama del deck con iconografía semántica propia — los cinco pictogramas mapean el flujo Consulta → Vectorizar → Búsqueda VDB → Recuperar doc → Generar respuesta. Sirve como referencia de estilo si hay que rehacer el flujo RAG completo.
- Transcribed text: (ninguno — las cinco etiquetas están en el texto de la slide)

**`AIG4B-Clase-5-RAG-y-MCP.md/images/slide-10-1.png`** — 1767×765 px · slide 10 (se repite en `slide-10-3.png`) · SVG: `slide-10-1.svg`
- Depiction: Marco de tarjeta vacío: rectángulo de borde gris muy claro, coronado por una barra horizontal roja gruesa con un círculo rojo relleno centrado sobre ella. Interior blanco.
- Why it matters: Contenedor de las columnas «Índice Invertido» y «Base de Datos Vectorial». Puro cromo.
- Transcribed text: (ninguno)

**`AIG4B-Clase-5-RAG-y-MCP.md/images/slide-10-5.png`** — 3567×765 px · slide 10 · SVG: `slide-10-5.svg`
- Depiction: Mismo marco de tarjeta que `slide-10-1.png` pero al doble de ancho (abarca dos columnas): borde gris claro, barra roja superior, círculo rojo centrado.
- Why it matters: Contenedor de la columna ancha «Búsqueda Híbrida».
- Transcribed text: (ninguno)

**`AIG4B-Clase-5-RAG-y-MCP.md/images/slide-15-1.png`** — 840×300 px · slide 15 (se repite en `slide-15-3.png`)
- Depiction: Flecha horizontal gruesa apuntando a la derecha, gris muy claro con borde apenas más oscuro, sobre fondo transparente. Ocupa solo el tercio superior del lienzo.
- Why it matters: Conector entre etapas del flujo TF-IDF.
- Transcribed text: (ninguno)

**`AIG4B-Clase-5-RAG-y-MCP.md/images/slide-15-2.png`** — 840×300 px · slide 15 (se repite en `slide-15-4.png`)
- Depiction: Idéntica a `slide-15-1.png`. Difiere en 99 EMU de ancho declarado en el manifest (≈ 0,0001 in) y por eso tiene md5 distinto, pero es visualmente indistinguible.
- Why it matters: Ver punto 33 de *Inconsistencies* — infla el recuento de imágenes únicas.
- Transcribed text: (ninguno)

**`AIG4B-Clase-5-RAG-y-MCP.md/images/slide-20-1.png`** — 1700×300 px · slide 20 (se repite en `slide-20-2.png`, `slide-20-3.png`, `slide-20-4.png`)
- Depiction: Misma flecha gris clara hacia la derecha, versión larga (1700 px). Cuatro colocaciones idénticas en la misma slide.
- Why it matters: Conector entre las cuatro etapas del flujo de búsqueda vectorial.
- Transcribed text: (ninguno)

**`AIG4B-Clase-5-RAG-y-MCP.md/images/slide-27-1.png`** — 1702×300 px · slide 27 (se repite en `slide-27-2.png`, `slide-27-3.png`, `slide-27-4.png`)
- Depiction: Flecha gris clara hacia la derecha, prácticamente igual a `slide-20-1.png` (2 px más ancha).
- Why it matters: Conector entre las cuatro etapas del pipeline Retrieval + RRF + Reranking.
- Transcribed text: (ninguno)

**`AIG4B-Clase-5-RAG-y-MCP.md/images/slide-35-1.png`** — 1154×673 px · slide 35 (se repite en `slide-35-2.png`, `slide-35-3.png`) · SVG: `slide-35-1.svg`
- Depiction: Tarjeta vacía con borde gris claro y una **barra roja vertical gruesa pegada al lado izquierdo**. Interior blanco.
- Why it matters: Contenedor de las tres tarjetas de riesgo de seguridad (acceso no autorizado / explotación / controles).
- Transcribed text: (ninguno)

**`AIG4B-Clase-5-RAG-y-MCP.md/images/slide-37-1.png`** — 1756×575 px · slide 37 (se repite en `slide-37-2.png`, `slide-37-3.png`, `slide-37-4.png`)
- Depiction: Tarjeta apaisada de borde gris claro con **banda superior gris cálido** ocupando el tercio de arriba, interior blanco. Variante «encabezado sombreado» del sistema de tarjetas.
- Why it matters: Contenedor de las cuatro buenas prácticas de mitigación.
- Transcribed text: (ninguno)

**`AIG4B-Clase-5-RAG-y-MCP.md/images/slide-38-1.png`** — 1154×588 px · slide 38 (se repite en `slide-38-2.png`, `slide-38-3.png`) · SVG: `slide-38-1.svg`
- Depiction: Igual a `slide-35-1.png` (barra roja vertical a la izquierda, marco gris claro), más baja.
- Why it matters: Contenedor de las tres limitaciones/retos futuros.
- Transcribed text: (ninguno)

### Iconos (50 únicos) — muestra caracterizada

Se abrieron **11** iconos para caracterizar el set. Hallazgo: son pictogramas monocromos de línea, mayoritariamente 60×60 px (algunos 138×138), en rojo Austral (`#E31E2D` aprox.) o granate oscuro, trazo uniforme, esquinas redondeadas, sin texto — salvo una excepción. Casi todos vienen de un SVG.

| Archivo (en `AIG4B-Clase-5-RAG-y-MCP.md/images/`) | Slide | Descripción |
|---|---|---|
| `slide-03-1.png` | 3 | **Lupa** de contorno rojo, círculo con mango diagonal hacia abajo a la derecha. Representa al «Recuperador». Sin texto. |
| `slide-04-4.png` | 4 | **Marcador/nota** granate oscuro: cuadrado de esquinas redondeadas con la esquina inferior derecha doblada. Es el glifo de viñeta más reutilizado del deck (6 colocaciones). Sin texto. |
| `slide-05-1.png` | 5 | **Calendario**: rectángulo redondeado con dos anillas arriba, línea divisoria bajo el encabezado y seis trazos verticales como celdas. Rojo. Ilustra «Datos actualizados». Sin texto. |
| `slide-06-1.png` | 6 | **Botón rectangular rojo relleno**, esquinas redondeadas, con texto blanco en negrita. **Única imagen del set con texto.** Transcribed text (español, variante peninsular): «**Haz clic aquí**». Enlazado a `https://aitutorial.dev/rag/fundamentals`. Se repite en 5 slides más (11, 16, 21, 29, 51) con destinos distintos. |
| `slide-13-1.png` | 13 | Mismo **marcador/nota** de esquina doblada, granate oscuro, en tamaño menor. Sin texto. |
| `slide-14-4.png` | 14 | Mismo **marcador/nota**, tono granate, otro raster. Sin texto. |
| `slide-26-1.png` | 26 | **Flecha simple hacia la derecha**, trazo rojo, punta en V abierta. Marca el paso de Etapa 1 a Etapa 2. Sin texto. **No referenciada en el `.md`** (ver *Inconsistencies* 29). |
| `slide-42-1.png` | 42 | **Candado** cerrado de contorno rojo: cuerpo rectangular redondeado, arco superior, círculo en el centro. Ilustra «Conocimiento estático» / cerrazón. Sin texto. |
| `slide-49-1.png` | 49 | **Lápiz** rojo en diagonal, punta hacia abajo a la izquierda, goma/casquillo arriba a la derecha. 138×138 px. Ilustra el Principio 1 (nombres). Sin texto. |
| `slide-55-1.png` | 55 | Icono de **trazo extremadamente fino**: a 60×60 px se lee como casilla en blanco, aunque el PNG tiene contenido RGBA real y su SVG (`slide-55-1.svg`, viewBox 1106×905) conserva el path completo. Sin texto. |
| `slide-58-1.png` | 58 | Mismo **marcador/nota** de esquina doblada, granate. Sin texto. |

Observación del set: el glifo «marcador de esquina doblada» aparece bajo **cuatro md5 distintos** (`slide-04-4`, `slide-13-1`, `slide-14-4`, `slide-58-1`) por rasterizarse a tamaños y tintes diferentes — otro motivo por el que el recuento de «64 únicas» sobreestima la variedad real.

### Iconos despachados (39 restantes)

Todos son pictogramas monocromos de línea del mismo sistema visual descrito arriba; los bytes están en la carpeta compañera y su SVG original, cuando existe, al lado.

- `slide-03-2.png` — icono de slide 3 · SVG: `slide-03-2.svg`
- `slide-03-3.png` — icono de slide 3 · SVG: `slide-03-3.svg`
- `slide-04-2.png` — icono de slide 4 · SVG: `slide-04-2.svg` (se repite en `slide-09-1.png`)
- `slide-04-3.png` — icono de slide 4 · SVG: `slide-04-3.svg`
- `slide-05-2.png` — icono de slide 5 · SVG: `slide-05-2.svg`
- `slide-05-3.png` — icono de slide 5 · SVG: `slide-05-3.svg`
- `slide-05-4.png` — icono de slide 5 · SVG: `slide-05-4.svg`
- `slide-05-5.png` — icono de slide 5 · SVG: `slide-05-5.svg`
- `slide-09-2.png` — icono de slide 9 · SVG: `slide-09-2.svg` (se repite en `slide-42-3.png`, `slide-63-3.png`)
- `slide-09-3.png` — icono de slide 9 · SVG: `slide-09-3.svg`
- `slide-09-4.png` — icono de slide 9 · SVG: `slide-09-4.svg`
- `slide-10-2.png` — icono de slide 10 · SVG: `slide-10-2.svg`
- `slide-10-4.png` — icono de slide 10 · SVG: `slide-10-4.svg`
- `slide-10-6.png` — icono de slide 10 · SVG: `slide-10-6.svg`
- `slide-12-1.png` — icono de slide 12 · SVG: `slide-12-1.svg`
- `slide-12-2.png` — icono de slide 12 · SVG: `slide-12-2.svg`
- `slide-12-3.png` — icono de slide 12 · SVG: `slide-12-3.svg`
- `slide-12-4.png` — icono de slide 12 · SVG: `slide-12-4.svg`
- `slide-14-1.png` — icono de slide 14 · SVG: `slide-14-1.svg` (se repite en `slide-14-3.png`)
- `slide-14-2.png` — icono de slide 14 · SVG: `slide-14-2.svg`
- `slide-15-5.png` — icono de slide 15 · sin SVG (se repite en `slide-27-5.png`, `slide-57-2.png`)
- `slide-18-1.png` — icono de slide 18 · SVG: `slide-18-1.svg` (se repite en `slide-18-2.png`, `slide-18-3.png`)
- `slide-18-4.png` — icono de slide 18 · sin SVG
- `slide-19-1.png` — icono de slide 19 · SVG: `slide-19-1.svg` (se repite en `slide-19-2.png`, `slide-19-3.png`)
- `slide-20-5.png` — icono de slide 20 · sin SVG (se repite en `slide-28-7.png`, `slide-50-1.png`, `slide-52-2.png`)
- `slide-24-1.png` — icono de slide 24 · SVG: `slide-24-1.svg`
- `slide-24-2.png` — icono de slide 24 · SVG: `slide-24-2.svg`
- `slide-24-3.png` — icono de slide 24 · SVG: `slide-24-3.svg`
- `slide-28-1.png` — icono de slide 28 · SVG: `slide-28-1.svg` (se repite en `slide-28-2.png` … `slide-28-6.png`)
- `slide-42-2.png` — icono de slide 42 · SVG: `slide-42-2.svg` (se repite en `slide-63-2.png`)
- `slide-49-2.png` — icono de slide 49 · SVG: `slide-49-2.svg`
- `slide-49-3.png` — icono de slide 49 · SVG: `slide-49-3.svg`
- `slide-49-4.png` — icono de slide 49 · SVG: `slide-49-4.svg`
- `slide-55-2.png` — icono de slide 55 · SVG: `slide-55-2.svg`
- `slide-55-3.png` — icono de slide 55 · SVG: `slide-55-3.svg`
- `slide-55-4.png` — icono de slide 55 · SVG: `slide-55-4.svg`
- `slide-55-5.png` — icono de slide 55 · SVG: `slide-55-5.svg`
- `slide-55-6.png` — icono de slide 55 · SVG: `slide-55-6.svg`
- `slide-59-1.png` — icono de slide 59 · sin SVG

### Tabla de remisión — colocaciones repetidas (58)

Estos archivos existen en disco y en la carpeta compañera, pero son **duplicados md5** de la imagen indicada; ya descritas arriba.

| Archivo | Slide | Es copia de |
|---|---|---|
| `slide-04-1.png` | 4 | `slide-03-1.png` |
| `slide-09-1.png` | 9 | `slide-04-2.png` |
| `slide-09-5.png` | 9 | `slide-04-4.png` |
| `slide-10-3.png` | 10 | `slide-10-1.png` |
| `slide-11-1.png` | 11 | `slide-06-1.png` |
| `slide-14-3.png` | 14 | `slide-14-1.png` |
| `slide-15-3.png` | 15 | `slide-15-1.png` |
| `slide-15-4.png` | 15 | `slide-15-2.png` |
| `slide-16-1.png` | 16 | `slide-06-1.png` |
| `slide-17-1.png` | 17 | `slide-04-4.png` |
| `slide-18-2.png`, `slide-18-3.png` | 18 | `slide-18-1.png` |
| `slide-19-2.png`, `slide-19-3.png` | 19 | `slide-19-1.png` |
| `slide-19-4.png` | 19 | `slide-13-1.png` |
| `slide-20-2.png`, `slide-20-3.png`, `slide-20-4.png` | 20 | `slide-20-1.png` |
| `slide-21-1.png` | 21 | `slide-06-1.png` |
| `slide-23-2.png` | 23 | `slide-13-1.png` |
| `slide-26-2.png` … `slide-26-6.png` | 26 | `slide-26-1.png` |
| `slide-26-7.png` | 26 | `slide-14-4.png` |
| `slide-27-2.png`, `slide-27-3.png`, `slide-27-4.png` | 27 | `slide-27-1.png` |
| `slide-27-5.png` | 27 | `slide-15-5.png` |
| `slide-28-2.png` … `slide-28-6.png` | 28 | `slide-28-1.png` |
| `slide-28-7.png` | 28 | `slide-20-5.png` |
| `slide-29-1.png` | 29 | `slide-06-1.png` |
| `slide-35-2.png`, `slide-35-3.png` | 35 | `slide-35-1.png` |
| `slide-37-2.png`, `slide-37-3.png`, `slide-37-4.png` | 37 | `slide-37-1.png` |
| `slide-38-2.png`, `slide-38-3.png` | 38 | `slide-38-1.png` |
| `slide-38-4.png` | 38 | `slide-04-4.png` |
| `slide-39-1.png` | 39 | `slide-04-4.png` |
| `slide-42-3.png` | 42 | `slide-09-2.png` |
| `slide-47-1.png` | 47 | `slide-04-4.png` |
| `slide-50-1.png` | 50 | `slide-20-5.png` |
| `slide-51-1.png` | 51 | `slide-06-1.png` — el botón «Haz clic aquí» con el **enlace roto a localhost** |
| `slide-52-2.png` | 52 | `slide-20-5.png` |
| `slide-55-7.png` | 55 | `slide-14-4.png` |
| `slide-57-2.png` | 57 | `slide-15-5.png` |
| `slide-61-1.png`, `slide-61-2.png` | 61 | `slide-14-4.png` |
| `slide-63-1.png` | 63 | `slide-42-1.png` |
| `slide-63-2.png` | 63 | `slide-42-2.png` |
| `slide-63-3.png` | 63 | `slide-09-2.png` |

---

## Raw / preserved excerpts

Material de clase reutilizable, verbatim.

### Slide 46 — Ejemplo JSON-RPC 2.0 (request + response)

Request, tal como aparece en la slide:

```json
{
  "jsonrpc": "2.0",
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "location": "Madrid"
    }
  },
  "id": 1
}
```

Response, tal como aparece en la slide (nótese que **no** lleva `jsonrpc`, `result` ni `id` — ver *Inconsistencies* punto 11):

```json
{
  "temperature": 22,
  "condition": "soleado"
}
```

Texto que la acompaña, verbatim:
> «MCP utiliza JSON-RPC 2.0 como capa de transporte, permitiendo mensajes ligeros y estructurados entre cliente y servidor.»
> Flujo de comunicación:
> - Cliente envía solicitud JSON con método y parámetros
> - Servidor procesa y responde con resultado o error estructurado
> - Protocolo sin estado con soporte para batch requests

### Slide 50 — `claude_desktop_config.json`, Método 2 (servidores por comando)

Rutas del archivo, verbatim:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/ruta/a/tu/proyecto"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "tu_token"
      }
    }
  }
}
```

### Slide 50 — `claude_desktop_config.json`, Método 3 (servidor local por HTTP)

```json
{
  "mcpServers": {
    "mi-servidor-local": {
      "type": "http",
      "url": "http://localhost:8002/mcp"
    }
  }
}
```

Pasos verbatim del Método 3:
> - Asegurate de que el servidor esté corriendo en `http://localhost:8002/mcp`
> - Edita el archivo `claude_desktop_config.json` (mismas rutas que Método 2)
> - Agrega la entrada con transport "http":
> - Útil para servidores propios en desarrollo o herramientas internas de la organización.
> - 4. Reinicia Claude Desktop y verificá que aparezca el ícono 🔌 en el chat.

Advertencia de la misma slide:
> ⚠️ «Seguridad: Usa servidores MCP de fuentes confiables. Los servidores que acceden a contenido externo pueden exponer a ataques de prompt injection. Verifica siempre el origen antes de instalar.»

### Slide 58 — Anti-patrón: lista plana de 20 herramientas

```javascript
const tools = [
  searchCustomers, searchProducts,
  searchOrders, searchTickets,
  getCustomer, getProduct,
  updateCustomer, updateProduct,
  createOrder, createTicket,
  // ... 10 más
];
// El agente ve 20 herramientas → 58% precisión
```

### Slide 58 — Solución: herramienta de routing jerárquico (MCP SDK + Zod)

```javascript
mcp.registerTool("route_to_domain", {
  description: "Enruta al dominio y acción correctos",
  inputSchema: {
    domain: z.enum([
      "customers","products",
      "orders","tickets"
    ]),
    action: z.enum([
      "search","get","update",
      "create","delete"
    ])
  }
});
// El agente ve 1 herramienta → 90%+ precisión
```

### Slide 27 — Fórmula RRF y esquema de entrada del cross-encoder

```
RRF(d) = Σ 1 / (k + rank_i(d))   [k=60 por defecto]
```

```
input:  "[CLS] query [SEP] documento [SEP]"
output: score de relevancia (0 a 1)
```

### Slide 13 — Fórmulas TF-IDF

```
TF(t, d)     = count(t in d) / total_terms(d)
IDF(t)       = log(N / df(t))
TF-IDF(t, d) = TF(t, d) × IDF(t)
```

Glosario verbatim:
> - t = un término (palabra o token) específico. Es el término cuya importancia queremos medir. Ejemplo: t = "leucemia", t = "gato", t = "el".
> - d = un documento específico del corpus. Es el documento para el cual estamos calculando el score. Ejemplo: "Doc 1: el gato come pescado fresco" → d = Doc 1.
> - N = número total de documentos en el corpus. Ejemplo: si tenemos 10.000 artículos médicos, N = 10.000.
> - df(t) = número de documentos en los que aparece el término t. Ejemplo: "leucemia" aparece en 200 documentos → df("leucemia") = 200.

### Slide 19 — Fórmula de similitud coseno (con el «Where:» en inglés del original)

```
cos(θ) = (A · B) / (||A|| × ||B||)

Where:
- A · B = producto punto (suma de productos elemento a elemento)
- ||A|| = magnitud del vector A (raíz de suma de cuadrados)
- Resultado: entre -1 (opuestos) y 1 (idénticos)
```

### Slide 18 — Vectores de ejemplo

```
"gato"   → [0.82, -0.31, 0.54, 0.12, ...]  (384 dims)
"felino" → [0.79, -0.28, 0.51, 0.15, ...]  (384 dims)
"perro"  → [0.71, -0.22, 0.48, 0.09, ...]  (384 dims)
"auto"   → [-0.12, 0.65, -0.33, 0.87, ...] (384 dims)
```

### Slide 49 — Convención de nombres y envelope de respuesta

```
Convención: [verbo]_[sustantivo]_[contexto]

Ejemplos correctos:
  get_customer_by_email
  search_products_by_category
  calculate_shipping_cost_for_order

Evitar:
  process
  fetch
  do_thing
```

```
{ success, data, error, message }
```

Principio 2, verbatim:
> «La descripción es lo más importante. Debe responder: ¿Qué hace? ¿Cuándo usarla? ¿Cuándo NO usarla? ¿Qué formato tienen entradas/salidas?»

Principio 3, verbatim:
> «Investigación muestra: 1-3 parámetros → 90%+ precisión | 4-6 parámetros → 75-85% | 7+ parámetros → 60-70%. Preferir múltiples herramientas simples sobre una herramienta compleja.»

### Slide 60 — Descriptores de herramientas diferenciadas, verbatim

```
search_products_by_text
  Descripción: Búsqueda de texto completo.
  ✅ Usar cuando: el cliente describe el producto con palabras ("ratón inalámbrico").
  ❌ NO usar cuando: tienes el SKU exacto.
  Parámetro: query: string

get_product_by_sku
  Descripción: Búsqueda exacta por SKU.
  ✅ Usar cuando: el cliente proporciona un SKU ("PROD-001").
  ❌ NO usar para búsquedas de texto libre.
  Parámetro: sku: string

filter_products_by_attributes
  Descripción: Filtro estructurado por atributos.
  ✅ Usar cuando: el cliente especifica categoría, precio o marca.
  ❌ NO usar para búsqueda de texto.
  Parámetros: category?: string, priceMax?: number
```

Resultado, verbatim:
> El agente ahora elige correctamente:
> - "ratón inalámbrico" → search_products_by_text ✓
> - "PROD-001" → get_product_by_sku ✓
> - "ratones por menos de $20" → filter_products_by_attributes ✓

### Slide 59 — Grupos de herramientas por fase, verbatim

```
Fase 01: Saludo / Autenticación
  Herramientas activas (1):
    authenticateCustomer
  El agente no necesita ver herramientas de búsqueda ni de tickets todavía.

Fase 02: Diagnóstico
  Herramientas activas (2):
    searchKnowledgeBase
    checkSystemStatus
  El agente se enfoca en encontrar la causa del problema.

Fase 03: Resolución
  Herramientas activas (2):
    createTicket
    scheduleCallback
  El agente no necesita herramientas de búsqueda en esta fase.
```

### Slide 61 — Métricas de analytics de herramientas, verbatim

```
Key metrics to track:
  call_count:      número de invocaciones
  success_rate:    tasa de éxito (%)
  avg_latency_ms:  latencia promedio en ms
  last_used:       última vez utilizada
```

Alertas de ejemplo, verbatim:
> - «Eliminar herramienta sin uso: legacy_search»
> - «slow_api promedia 3000ms — considerar caché»
> - «flaky_tool falla el 40% — revisar error handling»

### Slide 47 — Comparativa hardcoded vs. MCP, verbatim

**Herramienta Hardcodeada**
> - La lógica de la herramienta reside en el código del agente.
> - El agente conoce las herramientas en tiempo de compilación.
> - Requiere copiar y pegar código para reutilizar la herramienta.
> - Necesidad de redeploy del agente para cualquier actualización.
> - Protocolo de comunicación específico del framework.

**Servidor MCP (Protocolo de Contexto del Modelo)**
> - La herramienta opera como un proceso separado en localhost.
> - El agente consulta `tools/list` en tiempo de ejecución para descubrir herramientas.
> - Cualquier cliente compatible con MCP puede conectarse y usarlo.
> - Solo es necesario reiniciar el servidor MCP para aplicar actualizaciones.
> - JSON-RPC estandarizado sobre HTTP para la comunicación.

> «MCP separa las herramientas de los agentes — un servidor MCP puede ser usado por cualquier cliente compatible: Claude, ChatGPT, Cursor o tu propio agente.»

### Slide 44 — HTTP y GraphQL vs. MCP, verbatim

**HTTP: Generalidad sin especialización**
> - Heterogeneidad de interfaces entre servicios
> - Sin negociación de capacidades entre cliente y servidor
> - Sin gestión de sesiones persistentes
> - Sin propagación de contexto semántico

**GraphQL: Consultas potentes, orquestación limitada**
> - Foco en fetch de datos, no en ejecución de acciones
> - Sin orquestación dinámica de múltiples fuentes
> - Sin estandarización de operaciones asíncronas

**MCP: El estándar universal para IA**
> «MCP es un protocolo bidireccional y optimizado para la comunicación entre agentes de IA y sistemas externos. Resuelve exactamente las limitaciones de HTTP y GraphQL en contextos de IA:»
> - Negociación de capacidades en tiempo de conexión
> - Sesiones persistentes con estado compartido
> - Propagación nativa de contexto semántico
> - Orquestación dinámica de herramientas y fuentes

### Slide 43 / 64 — Historia de MCP, verbatim (aparece dos veces en el deck)

> **«Noviembre 2024 — Anthropic lanza MCP como protocolo abierto para toda la comunidad de desarrollo de IA.»**
>
> **Visión «USB-C para IA»** — Lenguaje común que conecta cualquier modelo con múltiples fuentes sin necesidad de conectores propietarios.
>
> **Reducción de complejidad** — De M×N integraciones (cada modelo con cada fuente) a M+N conexiones estandarizadas y reutilizables.
>
> **Aceleración del desarrollo** — Capa de abstracción universal que facilita la construcción rápida de aplicaciones inteligentes y componibles.

### Frases de cierre / «💡» del deck, verbatim

> - (s14) «El índice invertido es como el índice de un libro: vas directo al término y te dice en qué documentos aparece y con qué relevancia.»
> - (s15) «El índice TF-IDF actúa como el 'motor de búsqueda' del pipeline RAG: convierte millones de documentos en una lista ordenada de candidatos relevantes en milisegundos, antes de que el LLM genere la respuesta.»
> - (s18) «El embedding captura semántica, no sintaxis. 'No puedo iniciar sesión' y 'olvidé mi contraseña' producen vectores muy cercanos aunque no compartan ninguna palabra.»
> - (s19) «En producción, la búsqueda exacta de vecinos más cercanos es O(n) — demasiado lenta para millones de vectores. Se usan índices ANN (HNSW, IVF) que sacrifican un poco de precisión por velocidad sub-lineal.»
> - (s20) «Ventaja clave sobre TF-IDF: 'infarto de miocardio' y 'ataque al corazón' tienen similitud coseno ~0.89 → el sistema vectorial los conecta. TF-IDF los trataría como documentos completamente distintos.»
> - (s26) «¿Por qué funciona? Los retrievers rápidos son buenos encontrando candidatos pero malos rankeándolos. Los cross-encoders son excelentes rankeando pero demasiado lentos para miles de documentos. Combinados: velocidad + precisión.»
> - (s27) «Tips de producción: mantener el pool de candidatos en 20-100 docs y el top_k final en 3-5. Correr BM25 y vectorial en paralelo. Loggear latencia y costo por consulta.»
> - (s28) «La concatenación es la clave: al pasarle query y documento juntos al Transformer, el mecanismo de atención puede relacionar directamente cada palabra de la pregunta con cada palabra del documento. Eso es lo que el coseno entre vectores separados nunca puede hacer.»
> - (s09) «La calidad y cobertura de las fuentes determina directamente la calidad de las respuestas RAG. Garbage in, garbage out.»
> - (s52) «Más parámetros = mayor carga cognitiva = más confusión. Diseña múltiples herramientas simples en lugar de una herramienta compleja.»
> - (s57) «Con 20+ herramientas en lista plana, el agente selecciona la herramienta incorrecta el 42% de las veces. El diseño de herramientas es tan importante como su implementación.»
> - (s59) «El principio: el agente no necesita ver todas las herramientas todo el tiempo. Filtra por fase o contexto para maximizar la precisión de selección.»
> - (s61) «Las herramientas que el agente nunca usa o usa mal son señales de diseño deficiente — no de capacidad del modelo. Itera sobre descripciones y esquemas antes de cambiar el LLM.»
> - (s39) «RAG representa un avance significativo en IA generativa. Dominar búsqueda híbrida, reranking y evaluación será clave para aplicaciones de próxima generación.»
