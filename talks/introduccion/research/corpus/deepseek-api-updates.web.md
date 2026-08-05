---
source_file: deepseek-api-updates
source_type: web-capture
ingested_at: 2026-08-05
---

# Change Log — DeepSeek API Docs

## Provenance
- Ubicación original: `research/web/deepseek-api-updates/`
- Formato: captura web (`original.html` 42.756 bytes + `page.md` 13.954 bytes)
- URL: https://api-docs.deepseek.com/updates/
- Autor / fuente: **DeepSeek** (documentación oficial de la API)
- Fecha del original: página viva; la entrada más reciente es del **31 de julio de 2026** y la más
  antigua del **17 de mayo de 2024**
- Capturado el: 2026-08-05T12:19:57Z · HTTP 200
- `metadata.yaml` declara `assets: []`.
- Extracción limpia: el changelog completo (17 entradas) está en `page.md`. Al final se duplica el
  índice de la página como lista de anclas; es ruido de extracción.

## Key claims

Es un **changelog**: una secuencia fechada de anuncios de versiones de modelo y features de API. El
valor de la fuente no es argumentativo sino cronológico — permite fechar con precisión la cadencia de
lanzamientos de un laboratorio.

**Cronología completa, de más reciente a más antigua:**

| Fecha | Anuncio |
|---|---|
| 2026-07-31 | **DeepSeek-V4-Flash** oficial en beta pública. Misma arquitectura y tamaño que V4-Flash-Preview, solo re-post-entrenado. Soporte nativo del formato Responses API, adaptado a Codex. |
| 2026-04-24 | **DeepSeek-V4**: la API soporta V4-Pro y V4-Flash, vía interfaz OpenAI ChatCompletions *y* vía interfaz Anthropic. Se anuncia la discontinuación de `deepseek-chat` y `deepseek-reasoner` en tres meses (2026-07-24). |
| 2025-12-01 | **DeepSeek-V3.2**. Además, **V3.2-Speciale** en endpoint temporal con fecha de expiración explícita en la URL. |
| 2025-09-29 | **DeepSeek-V3.2-Exp**. |
| 2025-09-22 | **DeepSeek-V3.1-Terminus**: mantiene capacidades y corrige problemas reportados por usuarios. |
| 2025-08-21 | **DeepSeek-V3.1**: arquitectura de razonamiento híbrida (un solo modelo con modo pensante y no pensante). |
| 2025-05-28 | **DeepSeek-R1-0528** en `deepseek-reasoner`. |
| 2025-03-24 | **DeepSeek-V3-0324** en `deepseek-chat`. |
| 2025-01-20 | **DeepSeek-R1** disponible como `deepseek-reasoner`. |
| 2024-12-26 | **DeepSeek-V3** en `deepseek-chat`. |
| 2024-12-10 | **DeepSeek-V2.5-1210**. |
| 2024-09-05 | Fusión: **DeepSeek V2 Chat + DeepSeek Coder V2 → DeepSeek V2.5**. |
| 2024-08-02 | **Context Caching on Disk**: caché en disco duro, "reduciendo precios en otro orden de magnitud". |
| 2024-07-25 | Nuevas features de API: JSON Mode, Function Calling, Chat Prefix Completion (beta), 8K `max_tokens` (beta), FIM Completion (beta). |
| 2024-07-24 | **DeepSeek-Coder-V2-0724**. |
| 2024-06-28 | **DeepSeek-V2-0628**. |
| 2024-06-14 | **DeepSeek-Coder-V2-0614**: "ha alcanzado el nivel de GPT-4-Turbo-0409" en generación, comprensión, depuración y completado de código. |
| 2024-05-17 | **DeepSeek-V2-0517**. |

**Patrones estructurales que la fuente hace visibles:**
- **Estabilidad del contrato de API.** Casi todas las entradas repiten la misma fórmula: *"The API
  calling method remains unchanged"* / *"the base_url remains unchanged"*. Los modelos cambian debajo
  de nombres de endpoint estables.
- **Nombres de modelo como punteros, no como versiones.** `deepseek-chat` y `deepseek-reasoner` fueron
  actualizados repetidamente a modelos distintos (V2-0517 → V2-0628 → V2.5 → V3 → V3-0324 → V3.1 →
  V3.1-Terminus → V3.2-Exp → V3.2 → V4-Flash). El mismo nombre apuntó a al menos nueve modelos.
- **Convergencia de razonamiento.** El par `deepseek-chat` / `deepseek-reasoner` empezó como dos
  modelos y a partir de V3.1 pasó a ser **modo no-pensante / modo pensante del mismo modelo**.
- **Interoperabilidad deliberada.** V4 se expone simultáneamente por la interfaz de OpenAI y la de
  Anthropic; V4-Flash soporta nativamente el formato Responses API y está adaptado a Codex.
- **Aceleración de cadencia.** De ~5 lanzamientos anuales en 2024 a saltos de versión mayor (V3 → V4)
  en meses.

## Definitions and terminology

- **`deepseek-chat` / `deepseek-reasoner`**: nombres de modelo *legacy*. Desde V3.1 apuntan
  respectivamente al modo **non-thinking** y **thinking** del mismo modelo. Se discontinúan el
  2026-07-24.
- **Hybrid reasoning architecture**: "un solo modelo soporta modo pensante y no pensante".
  Introducida en V3.1.
- **Thinking mode / non-thinking mode**: los dos modos de operación del modelo híbrido.
- **Context Caching on Disk**: caché en disco duro para contexto repetido; DeepSeek la presenta como
  reducción de precio de un orden de magnitud.
- **FIM Completion** (Fill In the Middle): completado de código en el medio de un archivo, en
  endpoint `/completions`.
- **Chat Prefix Completion**: continuación desde un prefijo dado de la respuesta del asistente.
- **DeepSeek Harness minimal mode**: framework de evaluación propio usado para los benchmarks de
  agente de V4-Flash. "A publicarse pronto" al momento de la captura.
- **DSBench-FullStack / DSBench-Hard**: conjuntos de prueba **internos** de DeepSeek (desarrollo
  full-stack y problemas difíciles de coding agent).

## Evidence and examples

**Benchmarks de DeepSeek-V4-Flash (2026-07-31)**, presentados como "muy por encima de V4-Pro-Preview":

| Benchmark | Resultado |
|---|---|
| Terminal Bench 2.1 | 82,7 |
| NL2Repo | 54,2 |
| Cybergym | 76,7 |
| DeepSWE | 54,4 |
| Toolathlon verified | 70,3 |
| Agent Last Exam | 25,2 |
| Automation Bench (Public) | 25,1 |
| DSBench-FullStack (interno) | 68,7 |
| DSBench-Hard (interno) | 59,6 |

Condiciones declaradas: DeepSeek Harness minimal mode, max effort level, topp=0,95, temperature=1,0.

**DeepSeek-R1-0528 (2025-05-28)** — mejoras Pass@1 declaradas:
| Benchmark | Antes → Después |
|---|---|
| AIME 2025 | 70,0 → 87,5 (+17,5) |
| GPQA | 71,5 → 81,0 (+9,5) |
| LCB_v6 | 63,5 → 73,3 (+9,8) |
| Aider | 57,0 → 71,6 (+14,6) |
| Tau-bench (function calling) | 53,5 (Airline) / 63,9 (Retail) |

Además: mejor desarrollo front-end, y *"Significantly suppressed hallucination issues present in
legacy R1 version"*. Advertencia declarada: las tareas de razonamiento complejo **pueden consumir más
tokens** que la versión anterior.

**DeepSeek-V3.1 (2025-08-21)**: SWE-bench Verified 66,0 · SWE-bench Multilingual 54,5 ·
Terminal-bench 31,3. Eficiencia: V3.1-Think responde en *"significantly less time"* que R1-0528.

**DeepSeek-V3-0324 (2025-03-24)**: MMLU-Pro 75,9 → 81,2 (+5,3) · GPQA 59,1 → 68,4 (+9,3) ·
AIME 39,6 → 59,4 (+19,8) · LiveCodeBench 39,2 → 49,2 (+10,0).

**DeepSeek V2.5 (2024-09-05)**: ArenaHard win rate 68,3% → 76,3% · AlpacaEval 2.0 LC 46,61% →
50,52% · MT-Bench 8,84 → 9,02 · AlignBench 7,88 → 8,04 · HumanEval 89% · LiveCodeBench (ene-sep) 41%.

**DeepSeek-V2.5-1210 (2024-12-10)**: MATH-500 74,8% → 82,8% · LiveCodebench (01/08–01/12) 29,2% → 34,38%.

**DeepSeek-V2-0628**: HumanEval Pass@1 79,88% → 84,76% · MATH ACC@1 55,02% → 71,02% · BBH 78,56% →
83,40% · Arena-Hard win rate contra GPT-4-0314 41,6% → 68,3%.

**DeepSeek-V2-0517**: IFEval Prompt-Level 63,9% → 77,6% · tasa de parseo JSON 78% → 85%, y hasta 97%
"introduciendo expresiones regulares apropiadas".

**V3.1-Terminus (2025-09-22)** — problemas corregidos, declarados por el propio proveedor:
- *Language consistency*: menos mezcla chino-inglés y menos caracteres anómalos ocasionales.
- *Agent capabilities*: optimización del Code Agent y del Search Agent.

## Inconsistencies / open questions

- **Todos los benchmarks son auto-reportados por el proveedor**, sin verificación independiente ni
  intervalos de confianza. Varios se corren sobre conjuntos **internos** (DSBench-FullStack,
  DSBench-Hard) que no son auditables. Citarlos requiere decir de dónde salen.
- **La comparación de V4-Flash es contra V4-Pro-Preview, no contra competidores.** "Far exceeding
  V4-Pro-Preview" es una afirmación relativa a la propia línea de producto. No dice nada sobre
  posición competitiva.
- **El framework de evaluación no estaba publicado al momento de la captura**: "DeepSeek Harness
  minimal mode (to be released soon)". Los resultados de agente no son reproducibles con lo publicado.
- **Los deltas "antes → después" no siempre declaran la línea base.** En V3-0324 y V2-0628 se
  entiende que es la versión previa del mismo endpoint, pero no está dicho explícitamente.
- **Rareza en la nomenclatura V4:** la entrada de 2026-04-24 anuncia V4-Pro y V4-Flash, y la de
  2026-07-31 dice que el lanzamiento oficial de **V4-Pro "seguirá pronto"** — tres meses después de
  haber anunciado que la API ya lo soportaba. La distinción entre "soportado en API" y "lanzamiento
  oficial" no está definida en ninguna parte de la página.
- **Discontinuación con plazo corto:** tres meses de aviso para retirar `deepseek-chat` y
  `deepseek-reasoner` (2026-04-24 → 2026-07-24). Es un dato relevante si la presentación habla de
  estabilidad de APIs de proveedores.
- **Endpoint con fecha de expiración en la URL:** `https://api.deepseek.com/v3.2_speciale_expires_on_20251215`.
  Curiosidad de diseño de API que puede servir como ejemplo, pero está sin explicar.
- **La página no dice qué es V3.2-Speciale** más allá de su pricing (igual que V3.2), su falta de
  tool calls y su fecha de expiración. Modelo anunciado y retirado sin descripción.
- **No hay precios** en esta página, salvo menciones cualitativas ("reduciendo precios en otro orden
  de magnitud"). Todos los enlaces `/news/...` que darían detalle **no fueron capturados**.
- Ruido de extracción: el índice de la página se repite completo al final del `page.md` como lista de
  anclas, y una de las entradas quedó con backticks corruptos (```` ````[deepseek-coder & deepseek-chat ... ````).

## Images / diagrams

Ninguna. `metadata.yaml` declara `assets: []`. La carpeta companion
`deepseek-api-updates.web/images/` existe y está vacía.

## Raw / preserved excerpts

Entrada más reciente (2026-07-31), verbatim:

> ### DeepSeek-V4-Flash Update
>
> The official release of the DeepSeek-V4-Flash API is now in public beta. The API calling method remains unchanged — simply set the model name to `deepseek-v4-flash` to use the latest version.
>
> **Significantly enhanced agent capabilities, with benchmark results far exceeding V4-Pro-Preview:**
>
> - Terminal Bench 2.1: 82.7
> - NL2Repo: 54.2
> - Cybergym: 76.7
> - DeepSWE: 54.4
> - Toolathlon verified: 70.3
> - Agent Last Exam: 25.2
> - Automation Bench (Public): 25.1
> - DSBench-FullStack: 68.7
> - DSBench-Hard: 59.6
>
> Note 1: For the Code Agent tasks in the public benchmark sets, the official DeepSeek-V4-Flash was tested using the DeepSeek Harness minimal mode (to be released soon) as the framework, with the max effort level, topp=0.95, and temperature=1.0
> Note 2: DSBench-FullStack is an internal full-stack development test set, and DSBench-Hard is an internal Coding Agent hard-problem test set
>
> **The official V4-Flash natively supports the Responses API format and is specifically adapted for Codex.**
>
> **DeepSeek-V4-Flash-0731 keeps the same model architecture and size as DeepSeek-V4-Flash-Preview, and was only re-post-trained.**
>
> **Note: This update only upgrades the DeepSeek-V4-Flash API. The DeepSeek-V4-Pro API and the APP/WEB models are unchanged.**
> **The official release of DeepSeek-V4-Pro will follow soon.**

Entrada de V4 (2026-04-24), verbatim:

> The DeepSeek API now supports V4-Pro and V4-Flash, available via both the OpenAI ChatCompletions interface and the Anthropic interface. To access the new models, the base_url remains unchanged, and the model parameter should be set to `deepseek-v4-pro` or `deepseek-v4-flash`.
>
> The two legacy API model names, `deepseek-chat` and `deepseek-reasoner`, will be discontinued in three months (2026-07-24). During the current period, these two model names point to the non-thinking mode and thinking mode of `deepseek-v4-flash`, respectively.

Entrada de V3.1 (2025-08-21), verbatim:

> **Both `deepseek-chat` and `deepseek-reasoner` have been upgraded to DeepSeek-V3.1.** `deepseek-chat` corresponds to DeepSeek-V3.1's **non-thinking mode**, while `deepseek-reasoner` corresponds to its **thinking mode**.
>
> - Key updates in DeepSeek-V3.1:
> - **Hybrid reasoning architecture**: A single model supports both thinking mode and non-thinking mode
> - **Improved reasoning efficiency**: Compared to DeepSeek-R1-0528, DeepSeek-V3.1-Think provides answers in significantly less time
> - **Enhanced agent capabilities**: With post-training optimization, the new model achieves major improvements in tool usage and intelligent agent tasks
> - SWE-bench Verified: 66.0
> - SWE-bench Multilingual: 54.5
> - Terminal-bench: 31.3

Entrada de V3.2-Speciale (2025-12-01), verbatim:

> DeepSeek-V3.2-Speciale is served via a temporary endpoint: base_url="https://api.deepseek.com/v3.2_speciale_expires_on_20251215". Same pricing as V3.2, no tool calls, available until Dec 15th, 2025, 15:59 (UTC Time).

Entrada de V3.1-Terminus (2025-09-22), verbatim:

> This update maintains the model's original capabilities while addressing issues reported by users, including:
>
> - Language consistency: Reduced occurrences of Chinese-English mixing and occasional abnormal characters;
> - Agent capabilities: Further optimized the performance of the Code Agent and Search Agent.

Entrada de context caching (2024-08-02), verbatim:

> ### API Launches Context Caching on Disk Technology
>
> The DeepSeek API has innovatively adopted hard disk caching, reducing prices by another order of magnitude.

Entrada de Coder-V2-0614 (2024-06-14), verbatim:

> The `deepseek-coder` model has been upgraded to DeepSeek-Coder-V2-0614, significantly enhancing its coding capabilities. It has reached the level of GPT-4-Turbo-0409 in code generation, code understanding, code debugging, and code completion. Additionally, it possesses excellent mathematical and reasoning abilities, and its general capabilities are on par with DeepSeek-V2-0517.
