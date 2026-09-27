---
source_file: notas-presentador-reward-model-batch.md
source_type: other
ingested_at: 2026-09-26
---

# Notas del presentador — Entrenamiento del reward model en un batch de pares de preferencias

## Provenance
- Original location: articles/notas-presentador-reward-model-batch.md
- Format: md (Markdown with YAML frontmatter; the source's own frontmatter declares `source_type: presenter-notes`, which is not in the corpus-record enum, so this record uses `other`)
- Author / source (if known): presentador (Paulo Veiga) — presenter-authored note, not a published source
- Date of original (if known): 2026-09-26
- Source frontmatter `topic`: "Entrenamiento del reward model en un batch de pares de preferencias"
- Source frontmatter `note`: "texto pegado verbatim por el presentador en la sesión de Talksmith del 2026-09-26, pedido \"Agregar en RL un slide que explique la matemática de RL. Este es un poco el code a capturar\"."
- Purpose stated by the presenter: material for a slide in the RL section explaining the math of reward-model training ("el code a capturar").

## Key claims
- A training example for the reward model is one question (prompt) with two answers, fed as **two sequences, each with the question repeated**: "Fila 1: [Pregunta + A]" / "Fila 2: [Pregunta + B]".
- A batch holds many pairs, not one. Worked example: **64 pairs → 128 rows** (rows 0–127), laid out as interleaved pairs: row 2(i−1) = Pᵢ + Aᵢ (preferred), row 2i−1 = Pᵢ + Bᵢ.
- "Son 128 secuencias en un solo forward." — all 128 sequences go through the model in **one forward pass**.
- The forward pass yields **128 scores** (one scalar per sequence).
- Scores are **regrouped by pair** (row 0 with 1, 2 with 3, etc.). "El orden importa: el código tiene que saber qué score va con cuál."
- **Per-pair loss:** −log σ(r(Aᵢ) − r(Bᵢ)).
- **Mean of the 64 losses → a single backward pass.**
- **Padding detail:** A and B almost never have the same length, so sequences are padded to the batch's max length. "Por eso el score se toma del último token real de cada secuencia, no de la última posición de la fila, que podría ser padding." (Presenter-sourced; see Inconsistencies.)

## Definitions and terminology
- **Par / pair** — one prompt Pᵢ with two responses, Aᵢ (preferida) and Bᵢ (the other).
- **Fila / row** — one sequence in the batch tensor: prompt + one response concatenated.
- **Score / r(·)** — the reward model's scalar output for a (prompt + response) sequence; written r(Aᵢ), r(Bᵢ) with the prompt implicit.
- **σ** — the sigmoid (logistic) function (not defined in the note; standard reading, and matches InstructGPT Eq. 1).
- **Padding** — filler tokens appended so all rows in the batch share the max length.
- **Último token real** — the last non-padding token of a sequence; the position from which the score is read.
- **Forward / backward** — one forward pass over the batch; one backward (gradient) pass on the averaged loss.

## Evidence and examples
- Worked example of the batch layout (row table, verbatim in *Raw / preserved excerpts*): 64 pairs, 128 rows, rows 0–3 and 126–127 shown explicitly, middle elided with "…".
- Arithmetic check: 64 pairs × 2 = 128 sequences; last pair P₆₄ occupies rows 126 and 127 — consistent with 0-indexed interleaving (pair i at rows 2i−2, 2i−1). Internally consistent.
- No external citation, dataset, or code is given; the note is the presenter's own explanation.

## Inconsistencies / open questions
- [verified] Same loss as InstructGPT, different batching granularity — checked against `ouyang-2022-instructgpt.pdf.md` (Section 3.5, Eq. 1, and App. C.2). InstructGPT's RM loss is loss(θ) = −1/(K choose 2) · E[(x,y_w,y_l)∼D] [log(σ(r_θ(x,y_w) − r_θ(x,y_l)))]; the note's per-pair −log σ(r(Aᵢ) − r(Bᵢ)) is the same term with A = y_w, B = y_l. InstructGPT, however, has labelers rank K = 4 to 9 responses and "we train on all (K choose 2) comparisons from each prompt as a single batch element", because "comparisons are very correlated within each labeling task" and shuffling them into one dataset made "a single pass over the dataset caus[e] the reward model to overfit"; grouping also needs "only ... a single forward pass of the RM for each completion (rather than (K choose 2) forward passes for K completions)". The note's example uses **one pair per prompt** (K = 2, where (K choose 2) = 1 and Eq. 1 reduces exactly to the note's loss). Both are consistent with the same loss; the note is the simple K = 2 case, OpenAI's grouping is the K > 2 generalization motivated by overfitting and compute. Not a contradiction — a framing difference the Editor may want to mention.
- [verified] "Batch of 64" means different things — checked against `ouyang-2022-instructgpt.pdf.md` App. C.2: InstructGPT's RM batch size of 64 "represents the distinct number of prompts per batch", so "a single batch could contain up to 64 × (K choose 2) ≤ 2,304 comparisons". The note's 64 is **64 pairs** (= 64 prompts only because it uses one pair per prompt). The coincidence of the number is harmless for the note's K = 2 example but should not be presented as "InstructGPT used 64 pairs".
- [verified] Prompt repetition vs. score reuse — checked against the same InstructGPT passage. In the note each row repeats the prompt and each response is scored once per pair it appears in (here, once). With K > 2 grouped per prompt, InstructGPT scores each completion once and reuses that score across its K − 1 comparisons; the note's scheme, if naively extended to K > 2 by listing every pair as two rows, would re-encode the same completion K − 1 times. Relevant only if the slide generalizes beyond one pair per prompt.
- [open question] Padding / last-real-token claim is **presenter-sourced** — searched every record in `research/corpus/` for padding, last/final token, EOS and pad-token handling in reward-model scoring; none states it. Adjacent but not equivalent: `cobbe-2021-gsm8k-verifiers.pdf.md` contrasts a token-level verifier with one that predicts "only after the final token"; `hf-trl-sft-trainer.web.md` says padding tokens are masked out of the **SFT** loss. InstructGPT only says r_θ(x, y) is "the scalar output of the reward model". The claim is standard practice in common RM implementations but is not corroborated by any corpus source — settle by adding a source (e.g., a reward-model trainer's docs or code) or keep it attributed to the presenter.
- [open question] The note opens with "Casi:" — it answers a prior question/statement that is not captured in the source, so the misconception being corrected is unknown — settle by asking the presenter what "casi" responds to, if the slide should address it.
- [open question] Loss sign/reduction convention: the note says "Promedio de las 64 loss" (mean); InstructGPT writes an expectation scaled by 1/(K choose 2). For K = 2 these coincide (mean over pairs); no conflict, noted only so the slide's formula and its prose use the same reduction.

## Images / diagrams
None. The source is plain text; its row table is a Markdown/tab-separated text table, preserved verbatim below. No companion folder created.

## Raw / preserved excerpts

Source frontmatter (verbatim):

```yaml
source_type: presenter-notes
author: presentador (Paulo Veiga)
date: 2026-09-26
topic: Entrenamiento del reward model en un batch de pares de preferencias
note: texto pegado verbatim por el presentador en la sesión de Talksmith del 2026-09-26, pedido "Agregar en RL un slide que explique la matemática de RL. Este es un poco el code a capturar".
```

Full body (verbatim, tabs in the row table preserved):

```text
Casi: es una pregunta con dos respuestas. Lo que va en el batch son dos secuencias, cada una con la pregunta repetida:

Fila 1: [Pregunta + A]
Fila 2: [Pregunta + B]

Y el batch no tiene un solo par, sino muchos. Por ejemplo, con 64 pares:

Fila	Contenido
0	P₁ + A₁ (preferida)
1	P₁ + B₁
2	P₂ + A₂ (preferida)
3	P₂ + B₂
…	…
126	P₆₄ + A₆₄ (preferida)
127	P₆₄ + B₆₄

Son 128 secuencias en un solo forward. Después:

Se obtienen los 128 scores.
Se reagrupan por par (fila 0 con 1, 2 con 3, etc.). El orden importa: el código tiene que saber qué score va con cuál.
Loss de cada par: −log σ(r(Aᵢ) − r(Bᵢ)).
Promedio de las 64 loss → un solo backward.

Un detalle: A y B casi nunca tienen el mismo largo, así que se rellenan con padding hasta el largo máximo del batch. Por eso el score se toma del último token real de cada secuencia, no de la última posición de la fila, que podría ser padding.
```

Row table rendered as a Markdown table (same content, for reuse in slides):

| Fila | Contenido |
|---|---|
| 0 | P₁ + A₁ (preferida) |
| 1 | P₁ + B₁ |
| 2 | P₂ + A₂ (preferida) |
| 3 | P₂ + B₂ |
| … | … |
| 126 | P₆₄ + A₆₄ (preferida) |
| 127 | P₆₄ + B₆₄ |

InstructGPT cross-reference excerpts (from `ouyang-2022-instructgpt.pdf.md`, quoted for the comparison above):

> "Since comparisons are very correlated within each labeling task, we found that if we simply shuffle the comparisons into one dataset, a single pass over the dataset caused the reward model to overfit. Instead, we train on all (K choose 2) comparisons from each prompt as a single batch element. This is much more computationally efficient because it only requires a single forward pass of the RM for each completion (rather than (K choose 2) forward passes for K completions) and, because it no longer overfits, it achieves much improved validation accuracy and log loss."

> loss(θ) = −1/(K choose 2) · E(x,y_w,y_l)∼D [log(σ(r_θ(x, y_w) − r_θ(x, y_l)))]   (1)

> "The batch size here represents the distinct number of prompts per batch. Each prompt had between K = 4 and K = 9 labeled completions, from which there were up to (K choose 2) possible comparisons. Ties were dropped. Therefore, a single batch could contain up to 64 × (K choose 2) ≤ 2,304 comparisons."
