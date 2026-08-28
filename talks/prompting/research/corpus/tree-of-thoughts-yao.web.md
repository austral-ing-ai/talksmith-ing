---
source_file: tree-of-thoughts-yao
source_type: web-capture
ingested_at: 2026-08-14
---

# Tree of Thoughts: Deliberate Problem Solving with Large Language Models (Yao et al., 2023)

## Provenance
- Original location: `research/web/tree-of-thoughts-yao/`
- Format: web capture (HTML + `page.md` extraído), página de abstract de arXiv
- URL: https://arxiv.org/abs/2305.10601
- `fetched_at`: 2026-08-14T16:56:08Z
- `http_status`: 200
- Título capturado: `[2305.10601] Tree of Thoughts: Deliberate Problem Solving with Large Language Models`
- Autores: Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan
- Fecha del original: enviado el 17 de mayo de 2023 (v1); última revisión 3 de diciembre de 2023 (v2, la capturada)
- arXiv ID: arXiv:2305.10601 [cs.CL] — DOI 10.48550/arXiv.2305.10601
- Materias: Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
- **Venue declarado en la captura**: NeurIPS 2023 (campo `Comments`: "NeurIPS 2023 camera ready version").
- Código: https://github.com/princeton-nlp/tree-of-thought-llm — "Code repo with all prompts", declarado tanto en el abstract como en `Comments`.
- Licencia: CC BY 4.0

Nota de autoría: Shunyu Yao es también primer autor de ReAct (`react-yao.web.md`). Son dos papers distintos del mismo autor — si el deck cita "Yao et al." a secas, hay ambigüedad y conviene desambiguar por año (ReAct 2022, ToT 2023).

## Key claims

- Los modelos de lenguaje se despliegan cada vez más para resolución general de problemas, pero siguen confinados a procesos de decisión **a nivel de token y de izquierda a derecha** durante la inferencia. Este es el diagnóstico del que parte el paper.
- Esa limitación los hace fallar en tareas que requieren **exploración, lookahead estratégico, o donde las decisiones iniciales son determinantes**. Si el primer paso fue malo, la generación autoregresiva no tiene mecanismo para volver atrás.
- Proponen Tree of Thoughts (ToT), un marco de inferencia que **generaliza el enfoque popular de Chain of Thought**. La relación es explícita: ToT no compite con CoT, lo contiene como caso particular (CoT es un ToT con un solo camino y sin ramificación).
- ToT habilita exploración sobre **unidades coherentes de texto ("thoughts")** que funcionan como pasos intermedios hacia la solución. La unidad de decisión deja de ser el token y pasa a ser el pensamiento.
- ToT permite al modelo tomar decisiones deliberadas: considerar múltiples caminos de razonamiento, **autoevaluar** las opciones para decidir el próximo curso de acción, y **mirar hacia adelante o retroceder (backtracking)** cuando hace falta, para tomar decisiones globales.
- Los experimentos muestran que ToT mejora significativamente la capacidad de resolución de problemas en tres tareas nuevas que requieren planificación o búsqueda no trivial: **Game of 24, Creative Writing y Mini Crosswords**.

## Definitions and terminology

- **Tree of Thoughts (ToT)** — "a new framework for language model inference... which generalizes over the popular Chain of Thought approach to prompting language models, and enables exploration over coherent units of text (thoughts) that serve as intermediate steps toward problem solving".
- **Thought (pensamiento)** — la unidad de la que está hecho el árbol: "coherent units of text". Explícitamente no es un token: es un fragmento de texto coherente que constituye un paso intermedio. Esta es la diferencia conceptual clave con la decodificación token a token.
- **Deliberate decision making (decisión deliberada)** — el contraste con la generación autoregresiva. El modelo considera alternativas antes de comprometerse, en lugar de emitir el token más probable y seguir.
- **Self-evaluating choices (autoevaluación)** — el modelo evalúa sus propios pensamientos candidatos para decidir cuál expandir. Es el mecanismo que reemplaza a la heurística externa de una búsqueda clásica.
- **Lookahead y backtracking** — mirar hacia adelante y retroceder. Vocabulario de búsqueda en árbol traído al prompting; es lo que la generación izquierda-a-derecha no puede hacer.
- **Token-level, left-to-right decision-making** — la limitación diagnosticada. Buen término para la clase: nombra por qué CoT solo no alcanza en tareas de planificación.
- **Game of 24** — tarea de prueba: combinar cuatro números con operaciones aritméticas para obtener 24. El abstract la nombra pero no la explica.

## Evidence and examples

El abstract da **un solo par de números**, pero es contundente y es el más citable de la fuente:

| Tarea | Método | Resultado |
|---|---|---|
| Game of 24 | GPT-4 con chain-of-thought prompting | **4 %** de tareas resueltas |
| Game of 24 | ToT (este paper) | **74 %** de tasa de éxito |

Es un salto de 4 % a 74 % en la misma tarea con el mismo modelo base, cambiando solo la estrategia de inferencia. Para la clase es el ejemplo más nítido de que "el andamiaje alrededor del prompt importa tanto como el prompt".

Las otras dos tareas (Creative Writing, Mini Crosswords) se nombran pero **sin ninguna cifra** en el abstract.

## Inconsistencies / open questions

- **La captura trae solo el abstract, no el cuerpo del paper.** Lo que la clase necesitaría y no está acá:
  - La **Figura 1**, el esquema que compara IO prompting / CoT / Self-Consistency-CoT / ToT como cuatro topologías de nodos. Es la imagen que hace entender el concepto de un vistazo y **no está en la captura** — hay que sacarla del PDF.
  - Los **resultados de Creative Writing y Mini Crosswords** (el abstract los menciona sin números).
  - El **algoritmo de búsqueda** concreto: el paper implementa BFS y DFS sobre el árbol, con parámetros de amplitud y profundidad. Nada de eso está en el abstract.
  - Cómo se implementa la **autoevaluación** (los prompts de "value" / "vote" que puntúan cada pensamiento).
  - El **costo en llamadas al modelo**. ToT es sustancialmente más caro que CoT — muchas generaciones por nodo, muchos nodos — y el abstract no lo menciona. Si la slide presenta ToT como mejora sin más, omite el trade-off central.
  - La comparación contra self-consistency (`self-consistency-wang.web.md`), que es el competidor natural.
- El abstract dice "three novel tasks". Son tareas construidas por los autores para exhibir el método. Es honesto pero conviene notarlo: **no son benchmarks estándar preexistentes** como GSM8K. La generalización a tareas del mundo real no está establecida por esta evidencia.
- Ninguna evidencia biomédica en esta fuente. Si el deck usa ToT en un ejemplo clínico, el ejemplo es propio, no del paper.

## Images / diagrams

La captura no trae ninguna figura del paper — en particular, no trae el diagrama de las cuatro topologías. Solo cromo del sitio arXiv.



## Raw / preserved excerpts

**Abstract completo, verbatim (inglés):**

> Abstract:Language models are increasingly being deployed for general problem solving across a wide range of tasks, but are still confined to token-level, left-to-right decision-making processes during inference. This means they can fall short in tasks that require exploration, strategic lookahead, or where initial decisions play a pivotal role. To surmount these challenges, we introduce a new framework for language model inference, Tree of Thoughts (ToT), which generalizes over the popular Chain of Thought approach to prompting language models, and enables exploration over coherent units of text (thoughts) that serve as intermediate steps toward problem solving. ToT allows LMs to perform deliberate decision making by considering multiple different reasoning paths and self-evaluating choices to decide the next course of action, as well as looking ahead or backtracking when necessary to make global choices. Our experiments show that ToT significantly enhances language models' problem-solving abilities on three novel tasks requiring non-trivial planning or search: Game of 24, Creative Writing, and Mini Crosswords. For instance, in Game of 24, while GPT-4 with chain-of-thought prompting only solved 4% of tasks, our method achieved a success rate of 74%. Code repo with all prompts: https://github.com/princeton-nlp/tree-of-thought-llm

**Comments, verbatim:**

> Comments: NeurIPS 2023 camera ready version. Code repo with all prompts: https://github.com/princeton-nlp/tree-of-thought-llm

**Ficha bibliográfica, verbatim:**

> **arXiv:2305.10601** (cs)  [Submitted on 17 May 2023 ([v1](https://arxiv.org/abs/2305.10601v1)), last revised 3 Dec 2023 (this version, v2)]

> Authors: Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan

> Subjects: Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG) Cite as: arXiv:2305.10601 [cs.CL] (or arXiv:2305.10601v2 [cs.CL] for this version) https://doi.org/10.48550/arXiv.2305.10601

**Historial de versiones, verbatim:**

> **[v1]** Wed, 17 May 2023 23:16:17 UTC (609 KB)
> **[v2]** Sun, 3 Dec 2023 22:50:35 UTC (623 KB)

**Enlaces al texto completo:**

> - View PDF: https://arxiv.org/pdf/2305.10601
> - HTML (experimental): https://arxiv.org/html/2305.10601v2
> - TeX Source: https://arxiv.org/src/2305.10601
