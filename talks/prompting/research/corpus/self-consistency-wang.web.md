---
source_file: self-consistency-wang
source_type: web-capture
ingested_at: 2026-08-14
---

# Self-Consistency Improves Chain of Thought Reasoning in Language Models (Wang et al., 2022)

## Provenance
- Original location: `research/web/self-consistency-wang/`
- Format: web capture (HTML + `page.md` extraído), página de abstract de arXiv
- URL: https://arxiv.org/abs/2203.11171
- `fetched_at`: 2026-08-14T16:56:07Z
- `http_status`: 200
- Título capturado: `[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models`
- Autores: Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou
- Fecha del original: enviado el 21 de marzo de 2022 (v1); última revisión 7 de marzo de 2023 (v4, la capturada)
- arXiv ID: arXiv:2203.11171 [cs.CL] — DOI 10.48550/arXiv.2203.11171
- Materias: Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
- **Venue declarado en la captura**: ICLR 2023. El campo `Comments` lo dice con todas las letras — a diferencia del paper de chain-of-thought, acá el venue sí está respaldado por la fuente.
- Licencia: CC BY 4.0

## Key claims

- El chain-of-thought prompting combinado con modelos de lenguaje grandes preentrenados ya venía dando resultados alentadores en tareas de razonamiento complejo. Este paper parte de ahí.
- Proponen una **nueva estrategia de decodificación**, llamada *self-consistency*, para reemplazar la decodificación *greedy* ingenua que usaba el chain-of-thought prompting. El punto es importante y suele perderse: self-consistency **no es un prompt distinto**, es una forma distinta de muestrear y agregar las salidas del mismo prompt.
- El procedimiento tiene dos pasos: (1) muestrear un conjunto diverso de caminos de razonamiento en lugar de tomar solo el greedy; (2) seleccionar la respuesta más consistente marginalizando sobre los caminos muestreados.
- La intuición que lo sostiene: un problema de razonamiento complejo típicamente admite **múltiples maneras distintas de pensarlo que llevan a su única respuesta correcta**. Si varios caminos independientes convergen a la misma respuesta, esa respuesta gana probabilidad de ser la correcta.
- La evaluación empírica extensa muestra que self-consistency mejora el rendimiento del chain-of-thought prompting "con un margen llamativo" en varios benchmarks populares de razonamiento aritmético y de sentido común.

## Definitions and terminology

- **Self-consistency (autoconsistencia)** — "a new decoding strategy... to replace the naive greedy decoding used in chain-of-thought prompting". Es una estrategia de decodificación, no una técnica de prompting. Esta distinción importa si la clase presenta CoT y self-consistency como dos ítems de la misma lista.
- **Votación por mayoría / marginalización** — el abstract **no usa la expresión "majority vote"**. Lo que dice literalmente es: "selects the most consistent answer by marginalizing out the sampled reasoning paths". La formulación del paper es probabilística (marginalizar sobre los caminos latentes de razonamiento). En la práctica esto equivale a quedarse con la respuesta final más frecuente entre las muestras, que es como se lo suele explicar y como lo llama el resto de la literatura — pero **si la clase lo llama "votación por mayoría", eso es una glosa didáctica, no el término del abstract**. Ver `aitutorial-advanced-techniques.web.md`, que sí lo presenta explícitamente como "Generate multiple responses and vote".
- **Greedy decoding (decodificación greedy)** — la línea base que self-consistency reemplaza: tomar en cada paso el token más probable, lo que produce un único camino de razonamiento. El abstract lo califica de "naive".
- **Reasoning paths (caminos de razonamiento)** — las distintas cadenas de pensamiento que el modelo genera al muestrear con temperatura. El plural es el punto: la diversidad de caminos es el insumo del método.
- **Benchmarks nombrados**: GSM8K, SVAMP, AQuA (aritméticos), StrategyQA (sentido común), ARC-challenge.

## Evidence and examples

El abstract sí da números concretos, uno por benchmark. Son ganancias **sobre chain-of-thought prompting**, no sobre prompting estándar:

| Benchmark | Tipo | Ganancia reportada |
|---|---|---|
| GSM8K | aritmético | **+17,9 %** |
| SVAMP | aritmético | **+11,0 %** |
| AQuA | aritmético | **+12,2 %** |
| StrategyQA | sentido común | **+6,4 %** |
| ARC-challenge | sentido común / ciencia | **+3,9 %** |

Estas cinco cifras son el material citable más sólido de la captura. Advertencia de lectura: son **mejoras relativas al baseline de CoT**, no accuracy absoluta. Si una slide dice "self-consistency alcanza 17,9 % en GSM8K" está leyendo mal el abstract.

El campo `Comments` documenta además la evolución experimental del paper: "V2: added PaLM results; V3: added UL2 results". Es decir, los resultados con PaLM y con UL2 se agregaron después de la v1.

## Inconsistencies / open questions

- **La captura trae solo el abstract, no el cuerpo del paper.** Lo que la clase necesitaría y no está acá:
  - **Cuántas muestras hacen falta** (el valor de *k*, la cantidad de caminos muestreados). Es la pregunta operativa obvia y el abstract no la responde. En el paper el barrido va hasta 40 muestras, pero eso no está en la captura.
  - La **curva de rendimiento vs. cantidad de muestras** — dónde saturan las ganancias, que es lo que determina si el método vale la pena en costo.
  - Los **parámetros de muestreo** (temperatura, top-k / top-p) que producen la diversidad requerida.
  - El **accuracy absoluto** en cada benchmark, y con qué modelo. Las cifras del abstract son deltas sin línea base.
  - Qué modelos se usaron para cada número (el abstract menciona en `Comments` que hay resultados con PaLM y UL2, pero no dice qué benchmark corresponde a qué modelo).
  - El **costo**: self-consistency multiplica el número de llamadas al modelo por *k*. Ese trade-off no aparece en el abstract. La fuente que sí lo dice explícitamente es `aitutorial-advanced-techniques.web.md` ("5x Agent tasks = 5x cost").
- Tensión terminológica a resolver antes de la clase: el abstract habla de **marginalizar**, la divulgación habla de **votar por mayoría**. Son compatibles pero no idénticos. Conviene decidir cuál se usa en la slide y ser consistente.

## Images / diagrams

La captura no trae ninguna figura del paper — ni el diagrama de los tres caminos convergiendo, que es la figura canónica de este trabajo. Solo cromo del sitio arXiv.



## Raw / preserved excerpts

**Abstract completo, verbatim (inglés):**

> Abstract:Chain-of-thought prompting combined with pre-trained large language models has achieved encouraging results on complex reasoning tasks. In this paper, we propose a new decoding strategy, self-consistency, to replace the naive greedy decoding used in chain-of-thought prompting. It first samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths. Self-consistency leverages the intuition that a complex reasoning problem typically admits multiple different ways of thinking leading to its unique correct answer. Our extensive empirical evaluation shows that self-consistency boosts the performance of chain-of-thought prompting with a striking margin on a range of popular arithmetic and commonsense reasoning benchmarks, including GSM8K (+17.9%), SVAMP (+11.0%), AQuA (+12.2%), StrategyQA (+6.4%) and ARC-challenge (+3.9%).

**Comments, verbatim** (acá está el venue y la historia de los experimentos):

> Comments: Published at ICLR 2023. V2: added PaLM results; V3: added UL2 results; V4: camera ready version at ICLR 2023

**Ficha bibliográfica, verbatim:**

> **arXiv:2203.11171** (cs)  [Submitted on 21 Mar 2022 ([v1](https://arxiv.org/abs/2203.11171v1)), last revised 7 Mar 2023 (this version, v4)]

> Authors: Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou

> Subjects: Computation and Language (cs.CL); Artificial Intelligence (cs.AI) Cite as: arXiv:2203.11171 [cs.CL] (or arXiv:2203.11171v4 [cs.CL] for this version) https://doi.org/10.48550/arXiv.2203.11171

**Historial de versiones, verbatim:**

> **[v1]** Mon, 21 Mar 2022 17:48:52 UTC (7,808 KB)
> **[v2]** Wed, 6 Apr 2022 04:40:11 UTC (12,644 KB)
> **[v3]** Tue, 4 Oct 2022 16:46:29 UTC (12,968 KB)
> **[v4]** Tue, 7 Mar 2023 17:57:37 UTC (12,751 KB)

**Enlaces al texto completo:**

> - View PDF: https://arxiv.org/pdf/2203.11171
> - HTML (experimental): https://arxiv.org/html/2203.11171v4
> - TeX Source: https://arxiv.org/src/2203.11171
