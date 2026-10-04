---
source_file: AIG4B-Clase-6-Agent.pptx
source_type: article
ingested_at: 2026-10-04
---

# Módulo 6: Agents — Inteligencia Artificial Generativa Aplicada en Biomedicina (deck previo del presenter)

> **Librarian scope note (per Talk briefing).** This is the presenter's own earlier 44-slide deck on agents, from the biomedicine course. For the current Talk (*Agentes y multiagentes*, Inteligencia Artificial Generativa, Universidad Austral, 90 min, Spanish), the in-scope material is: the formal definition of an agent (slides 3–15), LLM-based agents / tools as a concept / ReAct (slides 17–22), and multi-agent systems (slides 28–33). **The MCP section (slides 24–26, plus MCP lines on slides 42 and 44) and the agent-memory section (slides 35–39, plus memory lines on slides 22, 42 and 44) are outside the current Talk's scope** (tools are concept-only, no MCP). They are preserved losslessly below anyway. The "Objetivos y Práctica" section (slides 41–44) is course-specific to the biomedicine run (LangChain `createAgent`, MemorySaver, MultiServerMCPClient, "Parte 3 del proyecto").

## Provenance
- Original location: `research/articles/AIG4B-Clase-6-Agent.pptx`
- Format: pptx (44 slides, 16:9; extracted with a stdlib XML parser — `python-pptx` not installed)
- Author / source (if known): Paulo Veiga / Marco Sanchez Sorondo — Universidad Austral · Facultad de Ingeniería · Departamento de Inteligencia Artificial (slide 1). Course: "Inteligencia Artificial Generativa Aplicada en Biomedicina", Módulo 6.
- Date of original (if known): "Abril, 2026" (slide 1). File metadata (`docProps/core.xml`) has empty title/creator and created/modified = 2026-10-04 (export timestamp, not authorship date).
- Speaker notes: every slide has a `notesSlide` part, but all 44 contain only the slide-number placeholder — **the deck carries no speaker notes**.
- Media: 109 files in `ppt/media/` (PNG + SVG pairs for most icons — the PNG is the rendering fallback of the SVG; plus one JPEG background and four large raster figures). All copied to `AIG4B-Clase-6-Agent.pptx/images/` with original names (`image-<slide>-<n>.<ext>`).

## Key claims

**1 · ¿Qué es un agente? (slides 3–15)**
- Definición canónica (Russell & Norvig, *AIMA*): "An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators..." (slide 4). Versión en español en slide 3: "En IA clásica, un agente es cualquier entidad que percibe su entorno mediante sensores y actúa sobre él mediante actuadores."
- "Agente" es una palabra mal utilizada: en el uso popular se llama agente a cualquier LLM o sistema basado en LLM; "Un LLM no es un agente por sí solo. Además, existen muchos tipos de agentes que no involucran en absoluto modelos de lenguaje." (slide 3)
- La definición no menciona ML, Deep Learning, LLMs, tools ni RAG ("Son implementaciones posibles, no la definición"), ni siquiera programas o software (un sistema mecánico o electrónico encaja), y contempla sistemas biológicos (células, humanos, animales, insectos). (slide 5)
- Agente racional (R&N): "A rational agent is one that does the right thing... This notion of desirability is captured by a performance measure that evaluates any given sequence of environment states." La racionalidad introduce optimización: "no basta con percibir y actuar, hay que hacerlo bien según un criterio definido." (slide 6)
- Un agente racional selecciona la acción que maximiza su medida de performance dada la evidencia de sus percepciones y su conocimiento previo; depende de cuatro factores: medida de performance, conocimiento previo, acciones disponibles, secuencia de percepciones. (slide 7)
- Tipos de ambiente (dimensiones): observable (completa vs. parcial), un agente vs. multi-agente, determinístico vs. estocástico, episódico vs. secuencial, estático vs. dinámico, discreto vs. continuo, conocido vs. desconocido. (slide 12)
- Dificultad de ambientes: crucigrama (fácil), ajedrez (medio, competitivo), taxi autónomo (difícil: parcialmente observable, estocástico, dinámico, continuo, multi-agente). (slide 13)
- Por qué formalizar: análisis riguroso, reutilización de frameworks agnósticos ("Un mismo algoritmo puede ganar en ajedrez y dirigir un robot"), decisión informada sobre cuándo usar un agente. (slide 14)
- Cuándo vale la pena usar agentes: múltiples herramientas en orden variable; interpretación dinámica de resultados; orquestación variable de sistemas; cuando una solución determinística es insuficiente ("el espacio de posibilidades es demasiado grande o dinámico para ser cubierto con reglas fijas"). (slide 15)

**2 · Agentes basados en LLMs (slides 17–22)**
- Formulación PEAS de un agente LLM: Agente = LLM con razonamiento, memoria y acceso a herramientas externas; Sensores = texto del usuario, contexto previo, resultados de herramientas; Actuadores = generar texto, razonar, ejecutar comandos, llamar APIs, producir planes; Ambiente = digital, simbólico, parcialmente observable, dinámico; Performance = calidad, relevancia y precisión; satisfacción del usuario. (slide 18)
- Valor del LLM en un agente: observar el lenguaje natural; usar herramientas con lenguaje ("medio universal para interactuar con herramientas de cualquier tipo y API"); reflexionar sobre outputs ("query con error → corrige → reintenta"); instruir sistemas complejos con lenguaje desestructurado. (slide 19)
- "ReAct es la arquitectura más simple y fundamental para agentes basados en LLMs. Combina razonamiento y acción en un ciclo iterativo hasta alcanzar una respuesta final." Ciclo Thought → Action → Observation repetido hasta tener información suficiente para una respuesta final. (slide 20)
- Tres componentes de un agente LLM: (1) Memoria y Contexto (historial, último prompt, contexto activo — la "conciencia" inmediata); (2) Tools ("descriptas en el contexto. El agente decide cuándo y cómo invocarlas"); (3) Información contextual (RAG), que "puede incrustarse en el prompt o invocarse como herramienta". (slide 22)

**3 · Desafíos de producción (slides 24–26) — OUT OF SCOPE for current Talk (MCP)**
- Brecha demo–producción: 95%+ accuracy requerida; tool selection cae de 92% (5 tools) a 58% (20+ tools); ~85% rule enforcement de reglas en prompt. "Las fallas en producción vienen de tool design inadecuado, estructuras de memoria y mecanismos de validación — no del modelo en sí." (slide 25)
- MCP como "estándar emergente de integración para agentes": estándar universal (Claude, ChatGPT, Cursor), servidores MCP, multi-servidor vía `MultiServerMCPClient`, ciclo estandarizado de descubrir/llamar/recibir resultados de herramientas. (slide 26)

**4 · Sistemas multiagente (slides 28–33)**
- Limitaciones de un solo agente: sobrecarga de tools (accuracy de selección ~92% con 5 tools → ~58% con 20+), contexto desbordado (información clínica, farmacológica, radiológica y administrativa en un solo contexto degrada el razonamiento), falta de especialización (un único system prompt no puede ser experto en todo). (slide 29)
- Ejemplo clínico (NSCLC): un agente único con 15+ tools mezcladas, prompt genérico y contexto que se llena rápido vs. agentes con 3–5 tools especializadas, instrucciones de dominio y contexto propio. "El problema no es la capacidad del LLM, sino la arquitectura. Dividir en agentes especializados es una decisión de ingeniería, no de modelo." (slide 30)
- Definición: "Un sistema multiagente consta de múltiples agentes que interactúan entre sí — de forma colaborativa, competitiva, o ambas — para resolver un problema que excede las capacidades de un agente individual." Beneficios: modularidad, especialización, control. Ejemplos ya vistos: AlphaGo (competitivo), taxi autónomo (competitivo + colaborativo); en biomedicina el patrón típico es colaborativo. (slide 31)
- Cuatro arquitecturas multiagente: **Supervisor** (agente central deriva cada consulta; "Patrón más común y predecible"); **Supervisor (tool-calling)** (los agentes especializados se exponen como tools del supervisor, invocados por function calling); **Network** (todos se comunican con todos; "Más flexible pero menos predecible"); **Hierarchical** (supervisor de supervisores). "La elección depende del nivel de control, complejidad y autonomía que necesite el sistema." (slide 32)
- Espectro workflows ↔ agentes: workflows deterministas (prompt chaining, paralelización), workflows dirigidos por LLM (routing, orchestrator-worker, evaluator-optimizer), agentes autónomos (ReAct con tool-calling). "La magia está en mezclarlos. Un sistema real puede tener routing determinista entre agentes que internamente son autónomos." (slide 33)

**5 · Memoria de agentes (slides 35–39) — OUT OF SCOPE for current Talk**
- Arquitectura de dos niveles: working memory (sesión; MemorySaver + thread_id; "Caché L1") y long-term memory (persistente; vector DB o servicio gestionado). (slide 36)
- Tres patrones de integración: code-driven (recomendado como punto de partida), LLM-driven (tool-based), background extraction. (slide 37)
- Soluciones: Redis Agent Memory Server, Mem0, Zep, LangChain Memory. "Patrón universal: store → search → inject en prompt o tool results." (slide 39)

**6 · Objetivos y práctica (slides 41–44)** — course-specific; see raw excerpts.

## Definitions and terminology
- **Agente** (R&N): entidad que percibe su entorno mediante sensores y actúa sobre él mediante actuadores. Formulado en el deck como tabla PEAS-like: Agente / Sensores / Actuadores / Ambiente / Acciones / Performance (slides 8–10, 18).
- **Agente racional**: selecciona la acción que maximiza su medida de performance, dada la evidencia de sus percepciones y su conocimiento previo.
- **Medida de performance**: "El criterio que define el éxito del agente. Sin esta medida, no hay racionalidad posible."
- **Secuencia de percepciones**: "El historial de todo lo que el agente ha observado del ambiente hasta el momento."
- **Ambiente episódico vs. secuencial**: acciones independientes vs. acciones con consecuencias a largo plazo. **Estático vs. dinámico**: el ambiente cambia o no mientras el agente delibera. **Conocido vs. desconocido**: el agente conoce o no las reglas del ambiente.
- **ReAct (Reason + Act)**: ciclo Thought → Action → Observation hasta respuesta final.
- **Tools**: herramientas descriptas en el contexto; el agente decide cuándo y cómo invocarlas.
- **Sistema multiagente**: múltiples agentes que interactúan (colaborativa, competitiva o ambas) para resolver un problema que excede a un agente individual.
- **Supervisor / Supervisor (tool-calling) / Network / Hierarchical**: ver Key claims §4.
- **Workflows deterministas / dirigidos por LLM / agentes autónomos**: espectro de slide 33.
- **Working memory / Long-term memory**; **code-driven / LLM-driven / background extraction** (out of scope).
- **MCP (Model Context Protocol)** (out of scope).

## Evidence and examples
- **Vacuum Cleaner** (slide 8): grilla n×m, parcialmente observable, determinístico; acciones Aspirar, MoverIzquierda, MoverDerecha, Esperar; performance +10 limpiar celda sucia · −1 moverse · −5 aspirar celda limpia · −10 chocar.
- **Robot móvil** (slide 9): cámara, LiDAR, GPS, giroscopio; entorno continuo, parcialmente observable, dinámico; performance = llegar rápido, sin colisiones, con mínimo consumo.
- **DeepMind AlphaGo** (slide 10): red neuronal profunda + MCTS; tablero 19×19, determinístico, completamente observable, competitivo; performance = probabilidad de victoria.
- **AlphaGo → AlphaGo Zero → AlphaZero** (slide 11): de datos humanos, a autojuego sin datos humanos (red unificada política-valor + MCTS), a generalización a ajedrez/shogi/go con el mismo algoritmo. Métrica universal: tasa de victorias.
- **Crucigrama / Ajedrez / Taxi autónomo** como escala de dificultad de ambientes (slide 13).
- **Soporte a decisiones clínicas, cáncer de pulmón (NSCLC)** (slide 30): comparación agente único vs. multiagente (tools, system prompt, contexto, precisión).
- **Ejemplos biomédicos de arquitecturas** (slide 32): coordinador que deriva al agente clínico o farmacológico (supervisor); agente clínico y farmacológico que dialogan para resolver una interacción (network); hospital con departamentos y coordinadores internos (hierarchical).
- **Ejemplos del espectro** (slide 33): pipeline fijo análisis clínico → verificación farmacológica → informe (workflow determinista); router clínico/farmacológico (workflow dirigido por LLM); agente que decide tools, orden y cuándo responder (agente autónomo).
- **Cifras de producción** (slide 25, repetidas en 29): 95%+ accuracy requerida; 92% → 58% tool selection (5 → 20+ tools); ~85% rule enforcement. No source cited on the slide.
- **Ejercicio práctico** (slide 43): elegir un problema real, modelarlo con agente/sensores/actuadores/ambiente/performance, implementarlo sobre la notebook de la práctica; guía: https://aitutorial.dev/agents/hands-on-exercise
- **Bibliografía** (slide 44): Russell & Norvig (2020), *AIMA* 4th ed., Pearson; LangGraph Docs (langchain-ai.github.io/langgraph); AI Tutorial – Agents Module (aitutorial.dev/agents/overvie[w]); LangChain Memory (python.langchain.com/docs/modules/memory).

## Inconsistencies / open questions
- [verified] Slide 30's comparison table is broken in the file: the `a:tbl` graphic frame has a single empty cell, and the table's content was flattened into one paragraph of the body text box ("Tools 15+ tools mezcladas de todos los dominios 3–5 tools por agente, especializadas System prompt Genérico, …"). No column headers exist anywhere on the slide — checked `ppt/slides/slide30.xml`. The reconstruction in Raw excerpts (two columns, presumably "Un solo agente" vs. "Multiagente") is the librarian's reading of the row order, not source text.
- [verified] Slide 44's URL is cut off in the source: "aitutorial.dev/agents/overvie" (missing final "w") — checked the raw string in `ppt/slides/slide44.xml`.
- [verified] Formulation tables are not uniform: slides 8 and 9 include an "Acciones" row; slides 10 (AlphaGo) and 18 (LLM agent) omit it — checked against the extracted tables.
- [verified] Slide 11's title "De AlphaGo Zero a AlphaZero" covers three stages, starting with plain AlphaGo — internal title/content mismatch.
- [verified] Slide 20 mixes languages in the ReAct diagram labels ("Respuesta", "Razonar" in Spanish; "Thought", "Action", "Observation" in English).
- [verified] Slides 2, 16, 23, 27, 34 and 40 are the same six-item agenda (section dividers); the source does not visibly highlight the current section in text (any highlight would be styling only).
- [open question] The production figures on slide 25 (95%+ required accuracy; tool-selection accuracy 92% with 5 tools → 58% with 20+; ~85% prompt-rule enforcement) carry no citation in the deck — the original source would need to be found before reusing them (also reused on slide 29).
- [open question] Slide 33's workflow taxonomy (prompt chaining, parallelization, routing, orchestrator-worker, evaluator-optimizer vs. autonomous agents) matches the vocabulary of Anthropic's "Building effective agents" (captured in this Talk's `research/web/anthropic-building-effective-agents/`), but the slide gives no attribution — cross-check against that record before citing.
- [open question] Slide 32's four architectures (Supervisor, Supervisor tool-calling, Network, Hierarchical) mirror LangGraph's multi-agent architectures naming; no attribution on the slide — cross-check against `research/web/langchain-multi-agent-architectures/`.
- [open question] Slide 3 attributes the Spanish definition to "Russell & Norvig" — it is a paraphrase/translation of the English quote on slide 4, not a published Spanish edition quote.
- [open question] Slides 21 and 38 are image-only (wide 3424×526 rasters) with no text; their content (probably a diagram / screenshot) is unknown until Phase 2 transcription.
- [open question] Scope: slides 24–26 (MCP) and 35–39 (memory), plus MCP/memory lines on 22, 42, 44, are outside the current Talk's scope per briefing — the Editor should not draw from them unless the presenter re-scopes.

## Images / diagrams

All bytes extracted to `AIG4B-Clase-6-Agent.pptx/images/` (109 files). In this deck most icons are stored twice: a `.svg` and its `.png` raster fallback; each pair is one stub below (both files listed). Large figures: `image-20-1.png` (2984×1120, ReAct cycle, slide 20), `image-21-1.png` and `image-38-1.png` (3424×526, image-only slides 21 and 38), `image-32-1.jpeg` (1440×2160, background of slide 32), `image-1-1.png` (432×358, cover). The `.svg`/`.png` media whose ids are skipped in the numbering (e.g. `image-32-6/7`) do not exist in the package — numbering gaps are in the source.

### Image 1 — image-1-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-1-1.png`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 1 (Módulo 6: Agents).
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 2 — image-3-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-3-1.png`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 3 (¿Qué es un Agente?) — next to «En IA clásica, un agente es cualquier entidad que percibe su entorno mediante sensores y actúa sobre él mediante actuadores. — Russell & Norvig».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 3 — image-3-2.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-3-2.png` + `AIG4B-Clase-6-Agent.pptx/images/image-3-3.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 3 (¿Qué es un Agente?) — next to «¿Qué se suele llamar agente?».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 4 — image-3-4.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-3-4.png` + `AIG4B-Clase-6-Agent.pptx/images/image-3-5.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 3 (¿Qué es un Agente?) — next to «¿Por qué esto es incorrecto?».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 5 — image-3-6.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-3-6.png` + `AIG4B-Clase-6-Agent.pptx/images/image-3-7.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 3 (¿Qué es un Agente?) — next to «¿Cuál es el camino correcto?».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 6 — image-5-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-5-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-5-2.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 5 (Comentarios sobre la definición) — next to «Sin ML ni LLMs».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 7 — image-5-3.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-5-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-5-4.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 5 (Comentarios sobre la definición) — next to «Sin programas».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 8 — image-5-5.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-5-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-5-6.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 5 (Comentarios sobre la definición) — next to «Sistemas biológicos».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 9 — image-7-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-7-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-7-2.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 7 (Racionalidad) — next to «Medida de performance».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 10 — image-7-3.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-7-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-7-4.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 7 (Racionalidad) — next to «Conocimiento previo».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 11 — image-7-5.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-7-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-7-6.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 7 (Racionalidad) — next to «Acciones disponibles».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 12 — image-7-7.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-7-7.png` + `AIG4B-Clase-6-Agent.pptx/images/image-7-8.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 7 (Racionalidad) — next to «Secuencia de percepciones».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 13 — image-11-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-11-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-11-2.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 11 (De AlphaGo Zero a AlphaZero) — next to «AlphaGo».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 14 — image-11-3.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-11-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-11-4.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 11 (De AlphaGo Zero a AlphaZero) — next to «AlphaGo Zero».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 15 — image-11-5.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-11-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-11-6.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 11 (De AlphaGo Zero a AlphaZero) — next to «AlphaZero».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 16 — image-11-7.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-11-7.png`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 11 (De AlphaGo Zero a AlphaZero) — next to «La métrica de performance es universal: tasa de victorias (ganar > empatar > perder).»; slide 25 (¿Por qué importa en producción?) — next to «Las fallas en producción vienen de tool design inadecuado, estructuras de memoria y mecanismos de validación — no del modelo en sí.»; slide 37 (Patrones de Integración de Memoria) — next to «Recomendación: Empezar con code-driven, agregar background extraction para enriquecimiento, y usar LLM-driven cuando la autonomía sea un requisito funcional.».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 17 — image-12-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-12-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-12-2.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 12 (Tipos de Ambientes) — next to «Observable».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 18 — image-12-3.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-12-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-12-4.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 12 (Tipos de Ambientes) — next to «Agentes».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 19 — image-12-5.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-12-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-12-6.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 12 (Tipos de Ambientes) — next to «Determinismo».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 20 — image-12-7.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-12-7.png` + `AIG4B-Clase-6-Agent.pptx/images/image-12-8.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 12 (Tipos de Ambientes) — next to «Episódico vs. Secuencial».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 21 — image-12-9.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-12-9.png` + `AIG4B-Clase-6-Agent.pptx/images/image-12-10.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 12 (Tipos de Ambientes) — next to «Estático vs. Dinámico».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 22 — image-12-11.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-12-11.png` + `AIG4B-Clase-6-Agent.pptx/images/image-12-12.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 12 (Tipos de Ambientes) — next to «Discreto vs. Continuo».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 23 — image-12-13.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-12-13.png` + `AIG4B-Clase-6-Agent.pptx/images/image-12-14.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 12 (Tipos de Ambientes) — next to «Conocido vs. Desconocido».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 24 — image-14-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-14-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-14-2.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 14 (¿Por qué todas estas definiciones?) — next to «Análisis riguroso».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 25 — image-14-3.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-14-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-14-4.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 14 (¿Por qué todas estas definiciones?) — next to «Reutilización de frameworks».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 26 — image-14-5.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-14-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-14-6.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 14 (¿Por qué todas estas definiciones?) — next to «Decisión informada».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 27 — image-15-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-15-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-15-2.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 15 (¿Cuándo vale la pena usar agentes?) — next to «Múltiples herramientas en orden variable»; slide 15 (¿Cuándo vale la pena usar agentes?) — next to «Interpretación dinámica de resultados»; slide 15 (¿Cuándo vale la pena usar agentes?) — next to «Orquestación variable de sistemas»; slide 15 (¿Cuándo vale la pena usar agentes?) — next to «Solución determinística insuficiente».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 28 — image-19-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-19-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-19-2.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 19 (¿Cuál es el valor de un LLM en un agente?) — next to «Observar el lenguaje natural».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 29 — image-19-3.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-19-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-19-4.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 19 (¿Cuál es el valor de un LLM en un agente?) — next to «Usar herramientas con lenguaje».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 30 — image-19-5.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-19-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-19-6.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 19 (¿Cuál es el valor de un LLM en un agente?) — next to «Reflexionar sobre outputs».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 31 — image-19-7.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-19-7.png` + `AIG4B-Clase-6-Agent.pptx/images/image-19-8.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 19 (¿Cuál es el valor de un LLM en un agente?) — next to «Instruir sistemas complejos».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 32 — image-20-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-20-1.png`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 20 (Arquitectura ReAct (Reason + Act)) — next to «Respuesta».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 33 — image-21-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-21-1.png`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 21 ((sin texto)).
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 34 — image-22-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-22-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-22-2.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 22 (Componentes de un Agente basado en LLM) — next to «1. Memoria y Contexto».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 35 — image-22-3.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-22-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-22-4.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 22 (Componentes de un Agente basado en LLM) — next to «2. Tools (Herramientas)».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 36 — image-22-5.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-22-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-22-6.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 22 (Componentes de un Agente basado en LLM) — next to «3. Información Contextual (RAG)».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 37 — image-26-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-26-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-26-2.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 26 (MCP: Model Context Protocol) — next to «Estándar universal»; slide 26 (MCP: Model Context Protocol) — next to «Servidores MCP»; slide 44 (Bibliografía y Recursos) — next to «Russell & Norvig (2020)»; slide 44 (Bibliografía y Recursos) — next to «LangGraph Docs»; slide 44 (Bibliografía y Recursos) — next to «AI Tutorial – Agents Module»; slide 44 (Bibliografía y Recursos) — next to «LangChain Memory».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 38 — image-26-5.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-26-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-26-6.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 26 (MCP: Model Context Protocol) — next to «Multi-servidor»; slide 26 (MCP: Model Context Protocol) — next to «Ciclo estandarizado».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 39 — image-29-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-29-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-29-2.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 29 (Limitaciones de un solo agente) — next to «Sobrecarga de tools».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 40 — image-29-3.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-29-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-29-4.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 29 (Limitaciones de un solo agente) — next to «Contexto desbordado».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 41 — image-29-5.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-29-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-29-6.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 29 (Limitaciones de un solo agente) — next to «Falta de especialización».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 42 — image-31-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-31-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-31-2.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 31 (¿Qué es un Sistema Multiagente?) — next to «Modularidad».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 43 — image-31-3.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-31-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-31-4.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 31 (¿Qué es un Sistema Multiagente?) — next to «Especialización».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 44 — image-31-5.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-31-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-31-6.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 31 (¿Qué es un Sistema Multiagente?) — next to «Control».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 45 — image-32-1.jpeg

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-32-1.jpeg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 32 (Arquitecturas Multiagente) — next to «SISTEMAS MULTIAGENTE».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 46 — image-32-2.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-32-2.png` + `AIG4B-Clase-6-Agent.pptx/images/image-32-3.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 32 (Arquitecturas Multiagente) — next to «Supervisor»; slide 32 (Arquitecturas Multiagente) — next to «Supervisor (tool-calling)».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 47 — image-32-4.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-32-4.png` + `AIG4B-Clase-6-Agent.pptx/images/image-32-5.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 32 (Arquitecturas Multiagente) — next to «Supervisor».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 48 — image-32-8.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-32-8.png` + `AIG4B-Clase-6-Agent.pptx/images/image-32-9.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 32 (Arquitecturas Multiagente) — next to «Supervisor (tool-calling)».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 49 — image-32-10.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-32-10.png` + `AIG4B-Clase-6-Agent.pptx/images/image-32-11.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 32 (Arquitecturas Multiagente) — next to «Network»; slide 32 (Arquitecturas Multiagente) — next to «Hierarchical».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 50 — image-32-12.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-32-12.png` + `AIG4B-Clase-6-Agent.pptx/images/image-32-13.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 32 (Arquitecturas Multiagente) — next to «Network».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 51 — image-32-16.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-32-16.png` + `AIG4B-Clase-6-Agent.pptx/images/image-32-17.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 32 (Arquitecturas Multiagente) — next to «Hierarchical».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 52 — image-38-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-38-1.png`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 38 ((sin texto)).
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 53 — image-39-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-39-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-39-2.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 39 (Soluciones de Memoria en Producción) — next to «Redis Agent Memory Server»; slide 39 (Soluciones de Memoria en Producción) — next to «Mem0»; slide 39 (Soluciones de Memoria en Producción) — next to «Zep»; slide 39 (Soluciones de Memoria en Producción) — next to «LangChain Memory».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 54 — image-39-9.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-39-9.png`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 39 (Soluciones de Memoria en Producción) — next to «Patrón universal: store → search → inject en prompt o tool results. Independientemente de la solución elegida, este flujo es constante.».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 55 — image-42-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-42-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-42-2.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 42 (Objetivos de Aprendizaje) — next to «Construir agentes con tool capabilities».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 56 — image-42-3.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-42-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-42-4.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 42 (Objetivos de Aprendizaje) — next to «Diseñar y operar servidores MCP».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 57 — image-42-5.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-42-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-42-6.svg`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 42 (Objetivos de Aprendizaje) — next to «Implementar memoria y seguridad».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 58 — image-43-1.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-43-1.png`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 43 (Ejercicio Práctico) — next to «Paso 1: Elegir un problema».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 59 — image-43-2.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-43-2.png`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 43 (Ejercicio Práctico) — next to «Paso 2: Modelar como agente».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### Image 60 — image-43-3.png

- File(s): `AIG4B-Clase-6-Agent.pptx/images/image-43-3.png`
- Provenance: `ppt/media/` of `research/articles/AIG4B-Clase-6-Agent.pptx`; used on slide 43 (Ejercicio Práctico) — next to «Paso 3: Implementar».
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

## Raw / preserved excerpts

Slide-by-slide, lossless text of all 44 slides in reading (z-)order as stored in the XML. First line of each slide is the small section label (eyebrow) when present. `[imagen: …]` marks where an image sits. **Speaker notes: none on any slide** (each notesSlide contains only the slide number). Tables are rendered as Markdown tables with the first column as row label (the source tables have no header row).

### Slide 1 — Módulo 6: Agents

Inteligencia Artificial Generativa Aplicada en Biomedicina

Módulo 6: Agents

Profesores: Paulo Veiga / Marco Sanchez Sorondo
Universidad Austral · Facultad de Ingeniería · Departamento de Inteligencia Artificial
Abril, 2026

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-1-1.png`]

*Speaker notes:* (none)

### Slide 2 — 1

Agenda

1

¿Qué es un Agente?

Definición formal, racionalidad, ejemplos y tipos de ambientes

2

Agentes basados en LLMs

Formulación, valor del LLM, arquitectura ReAct y componentes

3

Desafíos de Producción

Brecha prototipo-producción y Model Context Protocol

4

Sistemas Multiagente

Limitaciones de un agente, arquitecturas multiagente y el espectro workflows-agentes

5

Memoria de Agentes

Arquitectura de dos niveles, patrones de integración y soluciones

6

Objetivos y Práctica

Objetivos de aprendizaje, proyectos prácticos y ejercicio final

*Speaker notes:* (none)

### Slide 3 — ¿Qué es un Agente?

¿QUÉ ES UN AGENTE?

¿Qué es un Agente?

Antes de hablar de agentes basados en LLMs, necesitamos entender la definición formal y rigurosa del concepto.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-3-1.png`]

En IA clásica, un agente es cualquier entidad que percibe su entorno mediante sensores y actúa sobre él mediante actuadores. — Russell & Norvig

Agentes – Una palabra mal utilizada

En el uso cotidiano, la palabra "agente" se aplica con demasiada frecuencia a sistemas basados en LLMs, pero esa simplificación suele ocultar distinciones importantes.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-3-2.png` + `AIG4B-Clase-6-Agent.pptx/images/image-3-3.svg`]

¿Qué se suele llamar agente?

En el uso popular, se denomina "agente" simplemente a un LLM o a cualquier sistema basado en LLM, sin más distinción.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-3-4.png` + `AIG4B-Clase-6-Agent.pptx/images/image-3-5.svg`]

¿Por qué esto es incorrecto?

Un LLM no es un agente por sí solo. Además, existen muchos tipos de agentes que no involucran en absoluto modelos de lenguaje.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-3-6.png` + `AIG4B-Clase-6-Agent.pptx/images/image-3-7.svg`]

¿Cuál es el camino correcto?

Entender la definición formal de agente antes de hablar de agentes basados en LLMs es indispensable para razonar con rigor.

*Speaker notes:* (none)

### Slide 4 — "An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators..."

¿QUÉ ES UN AGENTE?

"An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators..."

— Russell & Norvig, Artificial Intelligence: A Modern Approach

Esta es la definición canónica y punto de partida de toda la teoría de agentes inteligentes en IA clásica.

*Speaker notes:* (none)

### Slide 5 — Comentarios sobre la definición

¿QUÉ ES UN AGENTE?

Comentarios sobre la definición

La elegancia de esta definición radica en su amplitud y generalidad. Veamos lo que no menciona:

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-5-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-5-2.svg`]

Sin ML ni LLMs

No se mencionan Machine Learning, Deep Learning, LLMs, tools ni RAG. Son implementaciones posibles, no la definición.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-5-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-5-4.svg`]

Sin programas

Ni siquiera se mencionan programas o software. Un sistema mecánico o electrónico también encaja perfectamente.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-5-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-5-6.svg`]

Sistemas biológicos

La definición contempla sistemas biológicos: células, humanos, animales e insectos son todos agentes válidos bajo esta definición.

*Speaker notes:* (none)

### Slide 6 — "A rational agent is one that does the right thing... This notion of desirability is captured by a performance measure that evaluates any given sequence of environment states."

¿QUÉ ES UN AGENTE?

"A rational agent is one that does the right thing... This notion of desirability is captured by a performance measure that evaluates any given sequence of environment states."

— Russell & Norvig, Artificial Intelligence: A Modern Approach

La racionalidad introduce el concepto de optimización: no basta con percibir y actuar, hay que hacerlo bien según un criterio definido.

*Speaker notes:* (none)

### Slide 7 — Racionalidad

¿QUÉ ES UN AGENTE?

Racionalidad

Un agente racional selecciona la acción que maximiza su medida de performance, dada la evidencia de sus percepciones y su conocimiento previo. La racionalidad depende de cuatro factores clave:

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-7-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-7-2.svg`]

Medida de performance

El criterio que define el éxito del agente. Sin esta medida, no hay racionalidad posible.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-7-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-7-4.svg`]

Conocimiento previo

Lo que el agente ya sabe sobre el ambiente antes de comenzar a actuar.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-7-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-7-6.svg`]

Acciones disponibles

El conjunto de acciones que el agente puede ejecutar en su entorno.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-7-7.png` + `AIG4B-Clase-6-Agent.pptx/images/image-7-8.svg`]

Secuencia de percepciones

El historial de todo lo que el agente ha observado del ambiente hasta el momento.

*Speaker notes:* (none)

### Slide 8 — Ejemplo: Vacuum Cleaner

¿QUÉ ES UN AGENTE?

Ejemplo: Vacuum Cleaner

Formulación como agente inteligente — Mantener limpio un entorno (grilla n×m) eliminando la suciedad con el mínimo de acciones posibles.

| Campo | Valor |
|---|---|
| Agente | Aspiradora autónoma (robot o modelo abstracto) |
| Sensores | Detector de suciedad, posición actual en la grilla |
| Actuadores | Motor de movimiento (izq/der/adelante/atrás), motor de succión |
| Ambiente | Grilla n×m, parcialmente observable, determinístico |
| Acciones | Aspirar, MoverIzquierda, MoverDerecha, Esperar |
| Performance | +10 limpiar celda sucia · −1 moverse · −5 aspirar celda limpia · −10 chocar |

*Speaker notes:* (none)

### Slide 9 — Ejemplo: Robot Móvil

¿QUÉ ES UN AGENTE?

Ejemplo: Robot Móvil

Formulación como agente inteligente — Desplazarse desde un punto inicial hasta un destino evitando obstáculos en entornos complejos.

| Campo | Valor |
|---|---|
| Agente | Robot móvil autónomo con sistema de control y planificación |
| Sensores | Cámara, LiDAR, GPS, giroscopio, sensores de proximidad |
| Actuadores | Motores de tracción, dirección, frenos, brazo robótico |
| Ambiente | Entorno físico (indoor/outdoor), continuo, parcialmente observable, dinámico |
| Acciones | Avanzar, girar, frenar, recalcular ruta |
| Performance | Llegar al destino rápido, sin colisiones y con mínimo consumo de energía |

*Speaker notes:* (none)

### Slide 10 — Ejemplo: DeepMind AlphaGo

¿QUÉ ES UN AGENTE?

Ejemplo: DeepMind AlphaGo

Formulación como agente inteligente — Jugar al Go a nivel superhumano mediante redes neuronales profundas y búsqueda Monte Carlo.

| Campo | Valor |
|---|---|
| Agente | Red neuronal profunda + búsqueda Monte Carlo (MCTS) |
| Sensores | Estado actual del tablero (disposición de fichas blancas y negras) |
| Actuadores | Colocar una piedra en una intersección válida o pasar turno |
| Ambiente | Tablero de Go 19×19, determinístico, completamente observable, competitivo |
| Performance | Probabilidad de victoria en la partida |

*Speaker notes:* (none)

### Slide 11 — De AlphaGo Zero a AlphaZero

¿QUÉ ES UN AGENTE?

De AlphaGo Zero a AlphaZero

La evolución de AlphaGo ilustra uno de los saltos más significativos en la historia de los agentes inteligentes: pasar del aprendizaje con datos humanos a la generalización pura.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-11-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-11-2.svg`]

AlphaGo

Aprende de partidas humanas. Requiere datos de expertos como punto de partida.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-11-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-11-4.svg`]

AlphaGo Zero

Aprende desde cero sin datos humanos, solo autojuego y retroalimentación. Red neuronal unificada política-valor + MCTS.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-11-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-11-6.svg`]

AlphaZero

Generaliza a múltiples juegos (ajedrez, shogi, go) sin conocimiento previo. Mismo algoritmo, distintos juegos.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-11-7.png`]

La métrica de performance es universal: tasa de victorias (ganar > empatar > perder).

*Speaker notes:* (none)

### Slide 12 — Tipos de Ambientes

¿QUÉ ES UN AGENTE?

Tipos de Ambientes

La naturaleza del ambiente determina en gran medida la complejidad del agente necesario para operar en él. Estas son las dimensiones fundamentales de clasificación:

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-12-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-12-2.svg`]

Observable

Completamente observable vs. Parcialmente observable

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-12-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-12-4.svg`]

Agentes

Un agente vs. Multi-agente

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-12-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-12-6.svg`]

Determinismo

Determinístico vs. Estocástico

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-12-7.png` + `AIG4B-Clase-6-Agent.pptx/images/image-12-8.svg`]

Episódico vs. Secuencial

Acciones independientes vs. acciones con consecuencias a largo plazo

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-12-9.png` + `AIG4B-Clase-6-Agent.pptx/images/image-12-10.svg`]

Estático vs. Dinámico

El ambiente cambia o no mientras el agente delibera

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-12-11.png` + `AIG4B-Clase-6-Agent.pptx/images/image-12-12.svg`]

Discreto vs. Continuo

Estados y acciones finitos vs. infinitos

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-12-13.png` + `AIG4B-Clase-6-Agent.pptx/images/image-12-14.svg`]

Conocido vs. Desconocido

El agente conoce o no las reglas del ambiente

*Speaker notes:* (none)

### Slide 13 — Dificultad de Ambientes

¿QUÉ ES UN AGENTE?

Dificultad de Ambientes

Las dimensiones del ambiente se combinan para determinar cuán desafiante resulta operar en él. El espectro va de problemas triviales a extraordinariamente complejos.

1

Crucigrama

Fácil: observable, determinístico, estático. Un solo agente.

2

Ajedrez

Medio: observable y determinístico, pero competitivo. Requiere anticipar al oponente.

3

Taxi Autónomo

Difícil: parcialmente observable, estocástico, dinámico, continuo, multi-agente.

*Speaker notes:* (none)

### Slide 14 — ¿Por qué todas estas definiciones?

¿QUÉ ES UN AGENTE?

¿Por qué todas estas definiciones?

La formalización agentica no es un ejercicio académico vacío. Tiene tres utilidades prácticas concretas y poderosas:

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-14-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-14-2.svg`]

Análisis riguroso

Nos obliga a pensar bien en el problema a resolver y analizar todos sus aspectos antes de implementar.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-14-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-14-4.svg`]

Reutilización de frameworks

Permite usar frameworks agnósticos que resuelven la formulación agentica. Un mismo algoritmo puede ganar en ajedrez y dirigir un robot.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-14-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-14-6.svg`]

Decisión informada

Es fundamental saber cuándo vale la pena usar un agente y cuándo una solución más simple es suficiente.

*Speaker notes:* (none)

### Slide 15 — ¿Cuándo vale la pena usar agentes?

¿QUÉ ES UN AGENTE?

¿Cuándo vale la pena usar agentes?

Los agentes no son la solución a todo. Estas son las condiciones que justifican su uso frente a soluciones determinísticas más simples:

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-15-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-15-2.svg`]

Múltiples herramientas en orden variable

Cuando la solución requiere usar varias herramientas, en múltiples órdenes y de distintas maneras según el contexto.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-15-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-15-2.svg`]

Interpretación dinámica de resultados

Cuando hay que interpretar y relacionar apropiadamente resultados en tiempo de ejecución, adaptando el comportamiento.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-15-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-15-2.svg`]

Orquestación variable de sistemas

Cuando hay que sincronizar y/u orquestar distintos sistemas de manera variable según las circunstancias.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-15-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-15-2.svg`]

Solución determinística insuficiente

Cuando el espacio de posibilidades es demasiado grande o dinámico para ser cubierto con reglas fijas.

*Speaker notes:* (none)

### Slide 16 — Agenda

AGENDA

Agenda

1

¿Qué es un Agente?

Definición formal, racionalidad, ejemplos y tipos de ambientes

2

Agentes basados en LLMs

Formulación, valor del LLM, arquitectura ReAct y componentes

3

Desafíos de Producción

Brecha prototipo-producción y Model Context Protocol

4

Sistemas Multiagente

Limitaciones de un agente, arquitecturas multiagente y el espectro workflows-agentes

5

Memoria de Agentes

Arquitectura de dos niveles, patrones de integración y soluciones

6

Objetivos y Práctica

Objetivos de aprendizaje, proyectos prácticos y ejercicio final

*Speaker notes:* (none)

### Slide 17 — Agentes basados en LLMs

AGENTES BASADOS EN LLMS

Agentes basados en LLMs

Con la base teórica asentada, exploramos cómo los modelos de lenguaje encajan en el marco formal de agentes inteligentes.

*Speaker notes:* (none)

### Slide 18 — Agentes basados en LLMs

AGENTES BASADOS EN LLMS

Agentes basados en LLMs

Formulación como agente inteligente — Resolver tareas lingüísticas o de razonamiento a partir de instrucciones en lenguaje natural.

| Campo | Valor |
|---|---|
| Agente | Modelo de lenguaje grande (LLM) con razonamiento, memoria y acceso a herramientas externas |
| Sensores | Texto de entrada del usuario, contexto previo, resultados de herramientas |
| Actuadores | Generar texto, razonar, ejecutar comandos, llamar APIs, producir planes |
| Ambiente | Entorno digital, simbólico, parcialmente observable, dinámico |
| Performance | Calidad, relevancia y precisión de respuestas; satisfacción del usuario |

*Speaker notes:* (none)

### Slide 19 — ¿Cuál es el valor de un LLM en un agente?

AGENTES BASADOS EN LLMS

¿Cuál es el valor de un LLM en un agente?

El LLM no es simplemente un chatbot dentro de un agente. Su valor radica en capacidades genuinamente novedosas que ningún sistema anterior podía ofrecer:

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-19-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-19-2.svg`]

Observar el lenguaje natural

Abre las puertas a un agente genérico para "percibir" el ambiente del lenguaje natural y actuar en él de forma fluida.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-19-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-19-4.svg`]

Usar herramientas con lenguaje

Emplea el lenguaje natural como medio universal para interactuar con herramientas de cualquier tipo y API.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-19-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-19-6.svg`]

Reflexionar sobre outputs

Puede analizar el resultado de una herramienta (ej: query con error → corrige → reintenta) en un ciclo reflexivo.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-19-7.png` + `AIG4B-Clase-6-Agent.pptx/images/image-19-8.svg`]

Instruir sistemas complejos

Permite comunicarse con sistemas informáticos complejos usando lenguaje desestructurado y natural.

*Speaker notes:* (none)

### Slide 20 — Arquitectura ReAct (Reason + Act)

AGENTES BASADOS EN LLMS

Arquitectura ReAct (Reason + Act)

ReAct es la arquitectura más simple y fundamental para agentes basados en LLMs. Combina razonamiento y acción en un ciclo iterativo hasta alcanzar una respuesta final.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-20-1.png`]

Respuesta

Razonar

Observation

Action

Thought

El ciclo Thought → Action → Observation se repite hasta que el agente determina que tiene suficiente información para producir una respuesta final de calidad.

*Speaker notes:* (none)

### Slide 21 — (sin texto)

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-21-1.png`]

*Speaker notes:* (none)

### Slide 22 — Componentes de un Agente basado en LLM

AGENTES BASADOS EN LLMS

Componentes de un Agente basado en LLM

Todo agente basado en LLM se construye sobre tres componentes esenciales que definen qué sabe, qué puede hacer y de qué contexto dispone:

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-22-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-22-2.svg`]

1. Memoria y Contexto

Historial de conversación, último prompt y contexto activo. Es la "conciencia" inmediata del agente sobre la situación actual.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-22-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-22-4.svg`]

2. Tools (Herramientas)

Conjunto de herramientas a las que puede llamar, descriptas en el contexto. El agente decide cuándo y cómo invocarlas.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-22-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-22-6.svg`]

3. Información Contextual (RAG)

Información asociada al historial mediante recuperación semántica. Puede incrustarse en el prompt o invocarse como herramienta.

*Speaker notes:* (none)

### Slide 23 — Agenda

AGENDA

Agenda

1

¿Qué es un Agente?

Definición formal, racionalidad, ejemplos y tipos de ambientes

2

Agentes basados en LLMs

Formulación, valor del LLM, arquitectura ReAct y componentes

3

Desafíos de Producción

Brecha prototipo-producción y Model Context Protocol

4

Sistemas Multiagente

Limitaciones de un agente, arquitecturas multiagente y el espectro workflows-agentes

5

Memoria de Agentes

Arquitectura de dos niveles, patrones de integración y soluciones

6

Objetivos y Práctica

Objetivos de aprendizaje, proyectos prácticos y ejercicio final

*Speaker notes:* (none)

### Slide 24 — Desafíos de Producción · OUT OF SCOPE (MCP / producción)

DESAFÍOS DE PRODUCCIÓN

Desafíos de Producción

Llevar agentes del prototipo funcional a un sistema de producción confiable es uno de los mayores retos de la ingeniería de IA actual.

*Speaker notes:* (none)

### Slide 25 — ¿Por qué importa en producción? · OUT OF SCOPE (MCP / producción)

DESAFÍOS DE PRODUCCIÓN

¿Por qué importa en producción?

Existe una brecha significativa entre un demo que funciona y un sistema de producción confiable. Los datos son reveladores:

95%+

Accuracy requerida

El umbral mínimo para sistemas de producción confiables. Los demos funcionales no llegan a este nivel.

58%

Tool selection con 20+ tools

La accuracy de selección de herramientas cae de 92% (5 tools) a solo 58% con más de 20 herramientas disponibles.

~85%

Rule enforcement

Los LLMs cumplen reglas basadas en prompt el 85% del tiempo. Insuficiente para sectores regulados.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-11-7.png`]

Las fallas en producción vienen de tool design inadecuado, estructuras de memoria y mecanismos de validación — no del modelo en sí.

*Speaker notes:* (none)

### Slide 26 — MCP: Model Context Protocol · OUT OF SCOPE (MCP / producción)

DESAFÍOS DE PRODUCCIÓN

MCP: Model Context Protocol

El Model Context Protocol es el estándar emergente de integración para agentes, diseñado para resolver la fragmentación del ecosistema y garantizar interoperabilidad a largo plazo.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-26-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-26-2.svg`]

Estándar universal

Asegura compatibilidad entre Claude, ChatGPT, Cursor y futuras plataformas. Diseña una vez, integra en todas partes.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-26-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-26-2.svg`]

Servidores MCP

Permite diseñar y operar servidores MCP con especificaciones completas de herramientas, recursos y capacidades.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-26-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-26-6.svg`]

Multi-servidor

Los agentes pueden integrarse con múltiples servidores MCP simultáneamente via MultiServerMCPClient.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-26-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-26-6.svg`]

Ciclo estandarizado

Define cómo los agentes descubren, llaman y reciben resultados de herramientas de manera consistente.

*Speaker notes:* (none)

### Slide 27 — Agenda

AGENDA

Agenda

1

¿Qué es un Agente?

Definición formal, racionalidad, ejemplos y tipos de ambientes

2

Agentes basados en LLMs

Formulación, valor del LLM, arquitectura ReAct y componentes

3

Desafíos de Producción

Brecha prototipo-producción y Model Context Protocol

4

Sistemas Multiagente

Limitaciones de un agente, arquitecturas multiagente y el espectro workflows-agentes

5

Memoria de Agentes

Arquitectura de dos niveles, patrones de integración y soluciones

6

Objetivos y Práctica

Objetivos de aprendizaje, proyectos prácticos y ejercicio final

*Speaker notes:* (none)

### Slide 28 — Sistemas Multiagente

SISTEMAS MULTIAGENTE

Sistemas Multiagente

Cuando un solo agente no alcanza: motivación, arquitecturas y aplicación en biomedicina.

*Speaker notes:* (none)

### Slide 29 — Limitaciones de un solo agente

SISTEMAS MULTIAGENTE

Limitaciones de un solo agente

Ya vimos que un agente con tools puede resolver problemas complejos. Pero a medida que crece el número de herramientas y dominios, aparecen problemas concretos:

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-29-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-29-2.svg`]

Sobrecarga de tools

La accuracy de selección de herramientas cae drásticamente cuando el agente tiene demasiadas opciones (de ~92% con 5 tools a ~58% con 20+). Un agente generalista pierde precisión.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-29-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-29-4.svg`]

Contexto desbordado

Si el agente debe manejar información clínica, farmacológica, radiológica y administrativa en un solo contexto, la calidad de razonamiento se degrada.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-29-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-29-6.svg`]

Falta de especialización

Un único system prompt no puede ser simultáneamente experto en interacciones farmacológicas Y en interpretación de ensayos clínicos Y en análisis de imágenes.

*Speaker notes:* (none)

### Slide 30 — Ejemplo: Soporte a Decisiones Clínicas

SISTEMAS MULTIAGENTE

Ejemplo: Soporte a Decisiones Clínicas

Queremos asistir a un equipo médico en la toma de decisiones para un paciente con cáncer de pulmón (NSCLC), integrando datos clínicos, farmacológicos y de evidencia.
Tools 15+ tools mezcladas de todos los dominios 3–5 tools por agente, especializadas System prompt Genérico, intenta cubrir todo Cada agente tiene instrucciones de su dominio Contexto Se llena rápidamente con info de todos los dominios Cada agente mantiene solo su contexto relevante Precisión Se degrada con la complejidad Cada agente es experto en lo suyo

*(Source table frame is a single empty cell — see Inconsistencies. Librarian reconstruction of the flattened paragraph above; column headers are NOT in the source:)*

| | Un solo agente *(header inferred)* | Multiagente *(header inferred)* |
|---|---|---|
| Tools | 15+ tools mezcladas de todos los dominios | 3–5 tools por agente, especializadas |
| System prompt | Genérico, intenta cubrir todo | Cada agente tiene instrucciones de su dominio |
| Contexto | Se llena rápidamente con info de todos los dominios | Cada agente mantiene solo su contexto relevante |
| Precisión | Se degrada con la complejidad | Cada agente es experto en lo suyo |

El problema no es la capacidad del LLM, sino la arquitectura. Dividir en agentes especializados es una decisión de ingeniería, no de modelo.

*Speaker notes:* (none)

### Slide 31 — ¿Qué es un Sistema Multiagente?

SISTEMAS MULTIAGENTE

¿Qué es un Sistema Multiagente?

Un sistema multiagente consta de múltiples agentes que interactúan entre sí — de forma colaborativa, competitiva, o ambas — para resolver un problema que excede las capacidades de un agente individual.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-31-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-31-2.svg`]

Modularidad

Agentes independientes facilitan el desarrollo, testing y mantenimiento. Se puede mejorar un agente sin tocar los demás.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-31-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-31-4.svg`]

Especialización

Cada agente tiene su propio dominio de expertise, sus tools y su system prompt optimizado para una tarea concreta.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-31-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-31-6.svg`]

Control

Se define explícitamente cómo se comunican los agentes y quién decide el flujo, en vez de depender de un único LLM para todo.

Ya vimos ejemplos multiagente: AlphaGo (competitivo), Taxi Autónomo (competitivo + colaborativo). En biomedicina, el patrón típico es colaborativo.

*Speaker notes:* (none)

### Slide 32 — Arquitecturas Multiagente

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-32-1.jpeg`]

SISTEMAS MULTIAGENTE

Arquitecturas Multiagente

Hay varias formas de conectar agentes. La elección depende del nivel de control, complejidad y autonomía que necesite el sistema.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-32-2.png` + `AIG4B-Clase-6-Agent.pptx/images/image-32-3.svg`]

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-32-4.png` + `AIG4B-Clase-6-Agent.pptx/images/image-32-5.svg`]

Supervisor

Un agente central decide a qué agente especializado derivar cada consulta. Patrón más común y predecible. Ejemplo: un agente coordinador recibe la pregunta del médico y la deriva al agente clínico o al farmacológico según corresponda.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-32-2.png` + `AIG4B-Clase-6-Agent.pptx/images/image-32-3.svg`]

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-32-8.png` + `AIG4B-Clase-6-Agent.pptx/images/image-32-9.svg`]

Supervisor (tool-calling)

Los agentes especializados se exponen como tools del supervisor. El LLM supervisor usa function calling para invocarlos. Ejemplo: es lo que los alumnos van a implementar en la Parte 3 del proyecto.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-32-10.png` + `AIG4B-Clase-6-Agent.pptx/images/image-32-11.svg`]

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-32-12.png` + `AIG4B-Clase-6-Agent.pptx/images/image-32-13.svg`]

Network

Todos los agentes se comunican entre sí. Más flexible pero menos predecible. Ejemplo: agente clínico y farmacológico dialogan directamente para resolver una interacción.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-32-10.png` + `AIG4B-Clase-6-Agent.pptx/images/image-32-11.svg`]

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-32-16.png` + `AIG4B-Clase-6-Agent.pptx/images/image-32-17.svg`]

Hierarchical

Supervisor de supervisores. Para sistemas muy complejos. Ejemplo: hospital con departamentos, cada uno con su coordinador interno.

*Speaker notes:* (none)

### Slide 33 — Workflows vs Agentes — El espectro

SISTEMAS MULTIAGENTE

Workflows vs Agentes — El espectro

No todo sistema con múltiples LLMs es un 'agente'. Existe un espectro entre flujos deterministas y agentes autónomos.

Workflows (deterministas)

Rutas de código predefinidas. El LLM se embebe en pasos fijos.
Patrones: prompt chaining, paralelización.
Ejemplo: Pipeline que siempre ejecuta análisis clínico → verificación farmacológica → informe.

Workflows (dirigidos por LLM)

El LLM dirige el flujo entre rutas predefinidas.
Patrones: routing, orchestrator-worker, evaluator-optimizer.
Ejemplo: Un router decide si la pregunta va al agente clínico o al farmacológico.

Agentes (autónomos)

El LLM decide sus propias acciones basado en feedback del ambiente.
Patrón: ReAct con tool-calling.
Ejemplo: El agente decide qué tools usar, en qué orden, y cuándo tiene suficiente información para responder.

La magia está en mezclarlos. Un sistema real puede tener routing determinista entre agentes que internamente son autónomos.

*Speaker notes:* (none)

### Slide 34 — Agenda

AGENDA

Agenda

1

¿Qué es un Agente?

Definición formal, racionalidad, ejemplos y tipos de ambientes

2

Agentes basados en LLMs

Formulación, valor del LLM, arquitectura ReAct y componentes

3

Desafíos de Producción

Brecha prototipo-producción y Model Context Protocol

4

Sistemas Multiagente

Limitaciones de un agente, arquitecturas multiagente y el espectro workflows-agentes

5

Memoria de Agentes

Arquitectura de dos niveles, patrones de integración y soluciones

6

Objetivos y Práctica

Objetivos de aprendizaje, proyectos prácticos y ejercicio final

*Speaker notes:* (none)

### Slide 35 — Memoria de Agentes · OUT OF SCOPE (memoria)

MEMORIA DE AGENTES

Memoria de Agentes

La memoria es uno de los componentes más críticos y menos intuitivos de los agentes en producción. Sin una estrategia adecuada, los agentes son caros, incoherentes y frustrantes.

*Speaker notes:* (none)

### Slide 36 — Arquitectura de Memoria: Dos Niveles · OUT OF SCOPE (memoria)

MEMORIA DE AGENTES

Arquitectura de Memoria: Dos Niveles

La solución al problema de memoria es una arquitectura que combina velocidad con persistencia, inspirada en los sistemas de caché de hardware:

Working Memory (Sesión)

Duración: Una sola sesión activa
Propósito: Estado activo de conversación
Ejemplo: Detalles del pedido en el chat actual
Implementación: MemorySaver + thread_id
Analogía: Caché L1 — rápida y temporal

Long-Term Memory (Persistente)

Duración: Entre sesiones, indefinidamente
Propósito: Conocimiento persistente del usuario
Ejemplo: Preferencias de usuario a lo largo de meses
Implementación: Vector DB o servicio gestionado
Analogía: Base de datos — persistente y buscable

*Speaker notes:* (none)

### Slide 37 — Patrones de Integración de Memoria · OUT OF SCOPE (memoria)

MEMORIA DE AGENTES

Patrones de Integración de Memoria

Existen tres patrones principales para integrar la memoria en un agente, con distintos niveles de control y autonomía:

01

Code-Driven (Programático)

Tu código decide explícitamente cuándo guardar y recuperar. Comportamiento predecible y eficiente. Punto de partida recomendado.

02

LLM-Driven (Tool-Based)

El agente recibe tools de memoria y decide autónomamente qué recordar. Más natural y flexible, pero menos predecible.

03

Background Extraction (Automático)

Almacena toda la conversación; procesos en segundo plano extraen hechos importantes de forma asíncrona.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-11-7.png`]

Recomendación: Empezar con code-driven, agregar background extraction para enriquecimiento, y usar LLM-driven cuando la autonomía sea un requisito funcional.

*Speaker notes:* (none)

### Slide 38 — (sin texto) · OUT OF SCOPE (memoria)

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-38-1.png`]

*Speaker notes:* (none)

### Slide 39 — Soluciones de Memoria en Producción · OUT OF SCOPE (memoria)

MEMORIA DE AGENTES

Soluciones de Memoria en Producción

El ecosistema de memoria para agentes ha madurado rápidamente. Estas son las soluciones más relevantes y el patrón universal que todas implementan:

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-39-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-39-2.svg`]

Redis Agent Memory Server

Working + long-term con búsqueda semántica integrada. Alta performance para producción.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-39-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-39-2.svg`]

Mem0

Capa de memoria gestionada para agentes. API simple, ideal para integración rápida.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-39-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-39-2.svg`]

Zep

Long-term memory con extracción automática de hechos desde conversaciones.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-39-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-39-2.svg`]

LangChain Memory

Integración nativa con LangChain/LangSmith. La opción más directa si ya usás el stack de LangChain.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-39-9.png`]

Patrón universal: store → search → inject en prompt o tool results. Independientemente de la solución elegida, este flujo es constante.

*Speaker notes:* (none)

### Slide 40 — Agenda

AGENDA

Agenda

1

¿Qué es un Agente?

Definición formal, racionalidad, ejemplos y tipos de ambientes

2

Agentes basados en LLMs

Formulación, valor del LLM, arquitectura ReAct y componentes

3

Desafíos de Producción

Brecha prototipo-producción y Model Context Protocol

4

Sistemas Multiagente

Limitaciones de un agente, arquitecturas multiagente y el espectro workflows-agentes

5

Memoria de Agentes

Arquitectura de dos niveles, patrones de integración y soluciones

6

Objetivos y Práctica

Objetivos de aprendizaje, proyectos prácticos y ejercicio final

*Speaker notes:* (none)

### Slide 41 — Objetivos y Práctica · course-specific (práctica biomedicina)

OBJETIVOS Y PRÁCTICA

Objetivos y Práctica

Esta parte del módulo traduce toda la teoría en competencias concretas y proyectos prácticos implementables.

*Speaker notes:* (none)

### Slide 42 — Objetivos de Aprendizaje · course-specific (práctica biomedicina)

OBJETIVOS Y PRÁCTICA

Objetivos de Aprendizaje

Al finalizar este módulo, el estudiante será capaz de diseñar, implementar y operar agentes basados en LLMs en entornos de producción:

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-42-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-42-2.svg`]

Construir agentes con tool capabilities

Usando createAgent de LangChain con patrones ReAct completos.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-42-3.png` + `AIG4B-Clase-6-Agent.pptx/images/image-42-4.svg`]

Diseñar y operar servidores MCP

Con especificaciones completas e integración multi-servidor via MultiServerMCPClient.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-42-5.png` + `AIG4B-Clase-6-Agent.pptx/images/image-42-6.svg`]

Implementar memoria y seguridad

Memoria con MemorySaver, reglas de negocio determinísticas, detección de PII y mitigación de jailbreak.

*Speaker notes:* (none)

### Slide 43 — Ejercicio Práctico · course-specific (práctica biomedicina)

OBJETIVOS Y PRÁCTICA

Ejercicio Práctico

El siguiente ejercicio busca integrar todos los conceptos del módulo en un problema original elegido por cada estudiante:

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-43-1.png`]

Paso 1: Elegir un problema

Pensar en un problema real a ser resuelto por un agente basado en LLMs. Cuanto más cercano a la realidad, mejor.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-43-2.png`]

Paso 2: Modelar como agente

Formularlo con las definiciones formales: agente, sensores, actuadores, ambiente y medida de performance.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-43-3.png`]

Paso 3: Implementar

Resolverlo usando como base la notebook de la práctica. Se puede usar información hardcodeada (JSONs, CSVs, .txt, etc.).

Guia de ejercicios: https://aitutorial.dev/agents/hands-on-exercise

*Speaker notes:* (none)

### Slide 44 — Bibliografía y Recursos · course-specific (práctica biomedicina)

OBJETIVOS Y PRÁCTICA

Bibliografía y Recursos

Recursos fundamentales para profundizar en los conceptos de este módulo:

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-26-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-26-2.svg`]

Russell & Norvig (2020)

Artificial Intelligence: A Modern Approach, 4th ed. Pearson. La referencia canónica para la teoría formal de agentes inteligentes.

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-26-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-26-2.svg`]

LangGraph Docs

Documentación oficial del framework para construcción de agentes stateful con grafos. langchain-ai.github.io/langgraph

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-26-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-26-2.svg`]

AI Tutorial – Agents Module

Guía práctica sobre el módulo de agentes con ejemplos de código. aitutorial.dev/agents/overvie
<!-- truncated-in-source: no complete version available -->

[imagen: `AIG4B-Clase-6-Agent.pptx/images/image-26-1.png` + `AIG4B-Clase-6-Agent.pptx/images/image-26-2.svg`]

LangChain Memory

Documentación de los módulos de memoria de LangChain para agentes. python.langchain.com/docs/modules/memory

*Speaker notes:* (none)
