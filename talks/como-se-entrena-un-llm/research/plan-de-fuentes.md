# Plan de fuentes — como-se-entrena-un-llm

Mapa de las notas del presentador (`articles/Data.pdf`) a las fuentes. Fuente principal: **Chip Huyen, *AI Engineering: Building Applications with Foundation Models* (O'Reilly, 2025)** — cap. 2 *Understanding Foundation Models* (núcleo), cap. 7 *Finetuning* y cap. 8 *Dataset Engineering* (complementarios). Los papers son los que el libro cita, más complementos donde el libro no llega.

No está en `articles/` y lo necesita el presentador: **el texto del libro** (copia propia, caps. 2, 7 y 8).

| Bullet de las notas | Libro | Fuentes capturadas |
|---|---|---|
| Training data: Common Crawl, C4 | Cap. 2 · Training Data | `raffel-2020-t5-c4.pdf` (origen de C4), `dodge-2021-documenting-c4.pdf` (qué hay adentro de C4) |
| Languages: sub-representación, distribución por hablantes, más caro en otros idiomas | Cap. 2 · Multilingual Models | `petrov-2023-tokenizer-unfairness.pdf`, `web/jun-2023-languages-tokenized/` |
| Common Crawl: distribución por categoría/dominio | Cap. 2 · Domain-Specific Models | `dodge-2021-documenting-c4.pdf` |
| Tamaño del modelo: Chinchilla, FLOPs, 20× tokens, scaling law | Cap. 2 · Model Size / Scaling Law | `hoffmann-2022-chinchilla.pdf`, `kaplan-2020-scaling-laws.pdf` |
| Scaling bottlenecks: quedarse sin datos, datos generados por IA, acuerdos por datos | Cap. 2 · Scaling Bottlenecks (Fig. 2-9 en Data.pdf) | `villalobos-2024-run-out-of-data.pdf`, `shumailov-2023-curse-of-recursion.pdf`, `longpre-2024-consent-in-crisis.pdf` |
| Pre-trained: optimizado para autocompletar, sesgos; ejemplo auto-completion vs. conversación | Cap. 2 · Post-Training (Fig. 2-10 en Data.pdf) | `ouyang-2022-instructgpt.pdf` (ejemplos GPT-3 vs InstructGPT) |
| Post-training: SFT, preference finetuning, RLHF, ~2% del cómputo | Cap. 2 · Post-Training / SFT / Preference Finetuning | `ouyang-2022-instructgpt.pdf`, `web/huyen-2023-rlhf/`, `rafailov-2023-dpo.pdf` |
| Ejemplo de dataset SFT; demonstration data (prompt, response); costo | Cap. 2 · SFT; cap. 8 | `ouyang-2022-instructgpt.pdf`, `touvron-2023-llama2.pdf` |
| RLHF: reward model que puntúa (prompt, respuesta) | Cap. 2 · Reward Model | `web/huyen-2023-rlhf/`, `ouyang-2022-instructgpt.pdf`, `touvron-2023-llama2.pdf` |
| Entrenamiento para tools y web search — cómo se logra (varias láminas) | Cap. 6 lo trata desde el uso, no el entrenamiento | `web/lambert-rlhfbook-tool-use/` (principal: formato de datos, llamadas intercaladas, masking de la salida de la tool, multistep, MCP), `schick-2023-toolformer.pdf`, `nakano-2021-webgpt.pdf` |
| Effort: cómo se entrena el razonamiento | Posterior al libro | `deepseek-2025-r1.pdf` |
| "El modelo siempre intenta responder" — cómo se evita | Cap. 2 · Hallucination | `kalai-2025-why-lms-hallucinate.pdf` |

**Resúmenes del libro** (sustituto parcial del texto, que no está disponible): `web/huyen-aie-chapter-summaries/` (resúmenes por capítulo de la propia autora, repo aie-book), `web/tonytvo-aie-summary/`, `web/bagerbach-aie-notes/`, `web/softwarephilosopher-aie-notes/`. Ninguno cubre Chinchilla/scaling con detalle — para eso, los papers.
