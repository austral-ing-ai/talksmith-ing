---
source_file: react-yao
source_type: web-capture
ingested_at: 2026-08-14
---

# ReAct: Synergizing Reasoning and Acting in Language Models (Yao et al., 2022)

## Provenance
- Original location: `research/web/react-yao/`
- Format: web capture (HTML + `page.md` extraído), página de abstract de arXiv
- URL: https://arxiv.org/abs/2210.03629
- `fetched_at`: 2026-08-14T16:56:07Z
- `http_status`: 200
- Título capturado: `[2210.03629] ReAct: Synergizing Reasoning and Acting in Language Models`
- Autores: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- Fecha del original: enviado el 6 de octubre de 2022 (v1); última revisión 10 de marzo de 2023 (v3, la capturada)
- arXiv ID: arXiv:2210.03629 [cs.CL] — DOI 10.48550/arXiv.2210.03629
- Materias: Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
- **Venue declarado en la captura**: ICLR (campo `Comments`: "v3 is the ICLR camera ready version"). El año no se declara explícitamente; corresponde a ICLR 2023.
- Sitio del proyecto con código: https://react-lm.github.io
- Licencia: CC BY 4.0

Nota de autoría: mismo primer autor que Tree of Thoughts (`tree-of-thoughts-yao.web.md`). "Yao et al. 2022" = ReAct; "Yao et al. 2023" = ToT.

## Key claims

- Los LLM ya mostraban capacidades impresionantes tanto en comprensión de lenguaje como en toma de decisiones interactiva, pero **el razonamiento (p. ej. chain-of-thought prompting) y la acción (p. ej. generación de planes de acción) se venían estudiando como temas separados**. El aporte del paper es unirlos.
- Proponen usar el LLM para generar **trazas de razonamiento y acciones específicas de la tarea de manera intercalada**. El entrelazado es el mecanismo: no razonar primero y actuar después, sino alternar.
- La sinergia va en las dos direcciones, y el abstract la explicita:
  - Las **trazas de razonamiento ayudan al modelo a inducir, seguir y actualizar planes de acción, y a manejar excepciones**.
  - Las **acciones le permiten interactuar con fuentes externas** — bases de conocimiento o entornos — para reunir información adicional.
- El método, llamado ReAct, se aplica a un conjunto diverso de tareas de lenguaje y de toma de decisiones, y demuestra efectividad sobre baselines estado del arte.
- Además del rendimiento, ReAct mejora **la interpretabilidad y la confiabilidad para humanos** frente a métodos sin componente de razonamiento o sin componente de acción. Este punto es relevante para una audiencia biomédica: la traza es auditable.
- Afirmación fuerte y directamente citable en una clase de prompting médico: en question-answering (HotpotQA) y verificación de hechos (Fever), **ReAct supera los problemas de alucinación y propagación de errores prevalentes en el razonamiento chain-of-thought** interactuando con una API simple de Wikipedia.
- ReAct genera trayectorias de resolución de tareas **similares a las humanas, más interpretables** que baselines sin trazas de razonamiento.
- En dos benchmarks de toma de decisiones interactiva (ALFWorld y WebShop), ReAct supera a métodos de imitación y de aprendizaje por refuerzo, **estando promptado con solo uno o dos ejemplos in-context**. El contraste es el argumento: uno o dos ejemplos en el prompt contra métodos que requieren entrenamiento.

## Definitions and terminology

- **ReAct** — el acrónimo condensa Reasoning + Acting. Definición operativa del abstract: generar "both reasoning traces and task-specific actions in an interleaved manner".
- **Reasoning trace (traza de razonamiento)** — lo que el modelo genera para pensar. Funciones que le atribuye el abstract: inducir, seguir y actualizar planes de acción, y manejar excepciones.
- **Action (acción)** — la interfaz con el afuera: "actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information". Acá aparece la idea que la clase probablemente quiera destacar: el modelo deja de depender solo de su memoria paramétrica.
- **Interleaved (intercalado)** — la palabra clave del método. Razonamiento y acción se alternan en la misma secuencia generada.
- **Hallucination y error propagation** — el abstract nombra ambos como problemas "prevalent in chain-of-thought reasoning". Es una crítica explícita a CoT desde dentro de la literatura: útil para la clase, porque evita presentar CoT como solución universal.
- **In-context examples** — ReAct usa "only one or two in-context examples". Conecta directamente con el vocabulario de `few-shot-learners-brown.web.md`.
- **Benchmarks nombrados**: HotpotQA (QA multi-salto), Fever (verificación de hechos), ALFWorld y WebShop (toma de decisiones interactiva).

## Evidence and examples

| Benchmark | Tipo | Resultado reportado |
|---|---|---|
| HotpotQA | question answering | Supera alucinación y propagación de errores de CoT usando una API simple de Wikipedia — **sin cifra** |
| Fever | verificación de hechos | Ídem — **sin cifra** |
| ALFWorld | decisión interactiva | **+34 %** de tasa de éxito absoluta sobre imitación / RL |
| WebShop | decisión interactiva | **+10 %** de tasa de éxito absoluta sobre imitación / RL |

Dato de eficiencia citable: esos +34 % y +10 % se obtienen "while being prompted with only one or two in-context examples", contra métodos de imitación y refuerzo que requieren entrenamiento con datos. Es el argumento de costo-beneficio más fuerte del abstract.

La herramienta externa usada en HotpotQA y Fever es **"a simple Wikipedia API"** — vale la precisión: no es un sistema de recuperación elaborado, es una API simple. Refuerza que la ganancia viene del patrón, no de la infraestructura.

## Inconsistencies / open questions

- **La captura trae solo el abstract, no el cuerpo del paper.** Lo que la clase necesitaría y no está acá:
  - La **Figura 1**, que muestra el ciclo Thought → Action → Observation lado a lado contra CoT y contra act-only. Es el diagrama que hace entender ReAct de un vistazo y **no está en la captura**.
  - Un **ejemplo de traza ReAct completa** (Thought 1 / Act 1 / Obs 1 / Thought 2 / ...). Para una clase de prompting esto es el material más valioso del paper y hay que sacarlo del PDF o del sitio del proyecto.
  - Los **números absolutos** en HotpotQA y Fever. El abstract afirma cualitativamente que supera la alucinación pero **no da accuracy**. Si la slide dice "ReAct reduce alucinaciones en X %", ese número no existe en esta fuente.
  - El formato exacto del prompt y de los verbos de acción (`search[]`, `lookup[]`, `finish[]`).
  - Los baselines contra los que se compara en cada caso.
  - La combinación ReAct + CoT-SC que el paper explora.
- El abstract dice "improved human interpretability and trustworthiness" sin describir cómo se midió. Si la clase presenta la interpretabilidad como resultado medido, esa metodología no está en la captura.
- Ningún experimento biomédico. Si el deck sitúa ReAct en un flujo clínico (por ejemplo, un agente que consulta PubMed), el ejemplo es una extrapolación propia. La extrapolación es razonable — la API de Wikipedia es intercambiable por cualquier fuente — pero es una extrapolación, no un hallazgo del paper.

## Images / diagrams

La captura no trae ninguna figura del paper — en particular, no trae el diagrama del ciclo Thought/Action/Observation. Solo cromo del sitio arXiv.



## Raw / preserved excerpts

**Abstract completo, verbatim (inglés):**

> Abstract:While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples. Project site with code: https://react-lm.github.io

**Comments, verbatim:**

> Comments: v3 is the ICLR camera ready version with some typos fixed. Project site with code: https://react-lm.github.io

**Ficha bibliográfica, verbatim:**

> **arXiv:2210.03629** (cs)  [Submitted on 6 Oct 2022 ([v1](https://arxiv.org/abs/2210.03629v1)), last revised 10 Mar 2023 (this version, v3)]

> Authors: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao

> Subjects: Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG) Cite as: arXiv:2210.03629 [cs.CL] (or arXiv:2210.03629v3 [cs.CL] for this version) https://doi.org/10.48550/arXiv.2210.03629

**Enlaces al texto completo:**

> - View PDF: https://arxiv.org/pdf/2210.03629
> - HTML (experimental): https://arxiv.org/html/2210.03629v3
> - TeX Source: https://arxiv.org/src/2210.03629
