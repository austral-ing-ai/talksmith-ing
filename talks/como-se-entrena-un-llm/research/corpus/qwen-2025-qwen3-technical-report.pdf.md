---
source_file: qwen-2025-qwen3-technical-report.pdf
source_type: article
ingested_at: 2026-09-26
---

# Qwen3 Technical Report

## Provenance
- Original location: articles/qwen-2025-qwen3-technical-report.pdf
- Format: pdf (35 pages; printed folio = PDF page, e.g. Table 9 on page 11)
- Author / source (if known): Qwen Team (Alibaba). Core contributors listed in §6 starting "An Yang, Anfeng Li, Baosong Yang, …". Links: https://huggingface.co/Qwen · https://modelscope.cn/organization/qwen · https://github.com/QwenLM/Qwen3
- Date of original (if known): report dated 2025-05-15; arXiv:2505.09388v1 [cs.CL], 14 May 2025.
- arXiv: 2505.09388v1 [cs.CL]
- License of the models: "all Qwen3 models are publicly accessible under Apache 2.0."
- Extraction: `pdftotext` (poppler, reading order and `-layout`); tables read from the `-layout` dump. **pdftotext drops underscores inside the monospace spans** (it prints `<|im start|>`, `/no think`, `enable thinking=False`); Table 9 and the flag names in this record were re-checked against a rendering of the page region (scratch only, not kept) and use the correct `<|im_start|>`, `/no_think`, `enable_thinking=False`, `{thinking_content}`. Figures 1–2 are vector graphics, cropped with `cropfigs.py`; Figure 2 values below were read off the crop.
- Focus note (why this source was added): the presenter's note "Effort, example on how is trained for that". The relevant material is §4 intro (two objectives: Thinking Control, Strong-to-Weak Distillation), §4.1–4.4 (four-stage pipeline), §4.3 (Thinking Mode Fusion: SFT data, chat template, `/think` & `/no_think`, thinking budget), Table 9, §4.5 (distillation of mode switching), §4.7 (thinking-budget scaling, Figure 2, Table 22), Appendix A.1.1 (budget of 8192 on long context).

## Key claims
- **One model, two modes (abstract)**: "A key innovation in Qwen3 is the integration of thinking mode (for complex, multi-step reasoning) and non-thinking mode (for rapid, context-driven responses) into a unified framework. This eliminates the need to switch between different models—–such as chat-optimized models (e.g., GPT-4o) and dedicated reasoning models (e.g., QwQ-32B)—–and enables dynamic mode switching based on user queries or chat templates."
- **Thinking budget (abstract)**: "Qwen3 introduces a thinking budget mechanism, allowing users to allocate computational resources adaptively during inference, thereby balancing latency and performance based on task complexity." Introduction: thinking budgets provide "users with fine-grained control over the level of reasoning effort applied by the model during task execution."
- **Two post-training objectives (§4)**: "(1) Thinking Control: This involves the integration of two distinct modes, namely the "non-thinking" and "thinking" modes, providing users with the flexibility to choose whether the model should engage in reasoning or not, and to control the depth of thinking by specifying a token budget for the thinking process. (2) Strong-to-Weak Distillation".
- **Four-stage pipeline for flagship models (Figure 1, §4)**: Base Models → Stage 1 Long-CoT Cold Start → Stage 2 Reasoning RL → Stage 3 Thinking Mode Fusion → Stage 4 General RL → Qwen3-235B-A22B, Qwen3-32B. "The first two stages focus on developing the models' "thinking" abilities. The next two stages aim to integrate strong "non-thinking" functionalities into the models." Lightweight models (Qwen3-30B-A3B, 14B/8B/4B/1.7B/0.6B) go Base → Strong-to-Weak Distillation.
- **Stage 1 — Long-CoT Cold Start (§4.1)**: problems in math, code, logic, STEM "paired with verified reference answers or code-based test cases"; queries are filtered to remove non-verifiable ones and those Qwen2.5-72B-Instruct "can answer correctly without using CoT reasoning"; N candidate responses per query from QwQ-32B, filtered on six criteria (wrong answer, repetition, guesswork, thinking/summary inconsistency, language mixing, overlap with validation). Goal: "to instill foundational reasoning patterns in the model without overly emphasizing immediate reasoning performance" — "it is preferable to minimize both the number of training samples and the training steps during this preparatory phase."
- **Stage 2 — Reasoning RL (§4.2)**: "a total of 3,995 query-verifier pairs, and employed GRPO (Shao et al., 2024)"; "large batch size and a high number of rollouts per query, along with off-policy training"; entropy controlled "to increase steadily or remain stable". "the AIME'24 score of the Qwen3-235B-A22B model increases from 70.1 to 85.1 over a total of 170 RL training steps."
- **Stage 3 — Thinking Mode Fusion (§4.3)**: "we conduct continual supervised fine-tuning (SFT) on the Reasoning RL model and design a chat template to fuse the two modes." Thinking data = "rejection sampling on Stage 1 queries using the Stage 2 model itself" (so the SFT does not degrade the Stage-2 reasoner); non-thinking data = curated coding, math, instruction following, multilingual, creative writing, QA, role-play, graded with "automatically generated checklists"; more translation for low-resource languages.
- **How the mode switch is trained (§4.3, chat template)**: `/think` and `/no_think` flags are placed "in the user query or system message"; "For non-thinking mode samples, we retain an empty thinking block in the assistant's response." Thinking is the default, so some thinking samples have no `/think` flag. For multi-turn: "we randomly insert multiple /think and /no_think flags into users' queries, with the model response adhering to the last flag encountered."
- **Hard switch without flags**: the empty think block "allows developers to prevent the model from engaging in thinking behavior by concatenating an empty think block in the chat template"; in Hugging Face's tokenizer chat template "the thinking mode can be disabled using an additional parameter enable_thinking=False" (Table 9 caption).
- **Thinking budget = truncation + injected stop sentence, and it is emergent, not trained (§4.3)**: "once the model learns to respond in both non-thinking and thinking modes, it naturally develops the ability to handle intermediate cases—generating responses based on incomplete thinking. ... when the length of the model's thinking reaches a user-defined threshold, we manually halt the thinking process and insert the stop-thinking instruction: "Considering the limited time by the user, I have to give the solution based on the thinking directly now.\n</think>.\n\n". ... It is worth noting that this ability is not explicitly trained but emerges naturally as a result of applying Thinking Mode Fusion."
- **Stage 4 — General RL (§4.4)**: reward system over "over 20 distinct tasks"; capabilities targeted include Instruction Following, **Format Following** ("it should respond appropriately to the /think and /no_think flags by switching between thinking and non-thinking modes, and consistently use designated tokens (e.g., <think> and </think>) to separate the thinking and response parts"), Preference Alignment, Agent Ability (multi-turn with "real environment execution feedback"), and specialized scenarios (e.g. RAG). Three reward types: rule-based; model-based with reference answer (Qwen2.5-72B-Instruct as judge); model-based without reference (reward model trained on human preference data).
- **Mode switching is reliably learned only after Stage 4**: ThinkFollow (in-house, multi-turn with random flags) 88.7 after Stage 3 → 98.9 after Stage 4 (Table 22). Stage 3 "has developed an initial ability to switch between modes, though it still occasionally makes errors."
- **Price of fusion + general RL**: "for challenging tasks like AIME'24 and LiveCodeBench, the performance in thinking mode actually decreases after these two training stages. We conjecture this degradation is due to the model being trained on a broader range of general tasks ... we choose to accept this performance trade-off to enhance the model's overall versatility."
- **Budget scaling (§4.7)**: "Qwen3 demonstrates scalable and smooth performance improvements correlated to the allocated thinking budget. Moreover, we observe that if we further extend the output length beyond 32K, the model's performance is expected to improve further in the future." Intro: "increasing the thinking budget for thinking tokens leads to a consistent improvement in the model's performance across various tasks."
- **Strong-to-weak distillation transfers mode switching (§4.5)**: off-policy phase combines teacher outputs "generated with both /think and /no_think modes"; on-policy phase: student samples in either mode and is "fine-tuned by aligning its logits with those of a teacher model (Qwen3-32B or Qwen3-235B-A22B) to minimize the KL divergence." Claim: "Distillation from advanced teacher models significantly outperforms reinforcement learning in performance and training efficiency" — about 1/10 of the GPU hours (Table 21) and it raises pass@64, which RL does not.
- **Thinking can hurt on retrieval-like tasks (A.1.1)**: on RULER, "In thinking mode, the model's performance slightly degrades. We hypothesize that the thinking content does not provide significant benefits for these retrieval tasks, which do not rely on reasoning and may instead interfere with the retrieval process." (Budget set to 8192 there "to mitigate overly verbose reasoning".)
- **Pre-training**: ~36 trillion tokens, 119 languages and dialects (up from 29 in Qwen2.5). Three stages: S1 General (>30T tokens, seq 4,096), S2 Reasoning (~5T higher-quality STEM/code/reasoning/synthetic tokens, faster LR decay), S3 Long Context ("hundreds of billions" of tokens at 32,768; RoPE base 10,000 → 1,000,000 via ABF; YARN + Dual Chunk Attention for 4× at inference). Extra data from Qwen2.5-VL OCR of "PDF-like documents" and synthetic data from Qwen2.5 / -Math / -Coder ("trillions of text tokens"). Instance-level data mixture optimized with a multilingual annotation system over "over 30 trillion tokens".
- **Architecture**: 6 dense (0.6B–32B) + 2 MoE (30B-A3B, 235B-A22B); GQA, SwiGLU, RoPE, RMSNorm pre-norm; QKV-bias removed, QK-Norm added; MoE with 128 experts, 8 active, no shared experts, global-batch load-balancing loss; BBPE tokenizer, vocabulary 151,669.
- **Headline**: Qwen3-235B-A22B (thinking) "achieves 85.7 on AIME'24 and 81.5 on AIME'25, 70.7 on LiveCodeBench v5, 2,056 on CodeForces, and 70.8 on BFCL v3."

## Definitions and terminology
- **Thinking mode / non-thinking mode** — the same model either emits a reasoning trace between `<think>` and `</think>` before its answer, or emits an empty `<think>\n\n</think>` block and answers directly.
- **`/think` and `/no_think` flags** — soft switches written in the user query (or system message); the latest flag in a multi-turn dialog wins. `/think` may be omitted because thinking is the default.
- **`enable_thinking=False`** — hard switch in the Hugging Face chat template that disables thinking (by inserting the empty think block).
- **Thinking Mode Fusion** — Stage 3: continual SFT on the Stage-2 (Reasoning RL) model with mixed thinking / non-thinking data in a shared chat template.
- **Thinking budget** — a user-set cap on thinking tokens; when reached, generation of the trace is halted and a fixed stop-thinking sentence plus `</think>` is inserted, after which the model answers. Described as emergent from fusion, "not explicitly trained".
- **Thinking Control** — the post-training objective covering both the mode choice and budget ("to control the depth of thinking by specifying a token budget for the thinking process").
- **Long-CoT Cold Start** — Stage 1: small SFT on verified long chain-of-thought traces to seed reasoning patterns before RL.
- **Reasoning RL** — Stage 2: GRPO on 3,995 query-verifier pairs.
- **General RL** — Stage 4: RL across >20 tasks with rule-based and model-based rewards, including format following of the mode flags.
- **Query-verifier pair** — a problem plus an automatic checker (reference answer or test cases).
- **GRPO** — Group Relative Policy Optimization (Shao et al., 2024).
- **Strong-to-Weak Distillation** — off-policy (teacher outputs in both modes) then on-policy (student samples, logits aligned to teacher by minimizing KL) distillation for the small models.
- **ThinkFollow**, **LengthCtrl**, **CounterFactQA**, **ToolUse** — in-house benchmarks (Table 22); ThinkFollow = "multi-turn dialogues with randomly inserted /think and /no_think flags to test whether the model can correctly switch thinking modes".
- **Qwen3-235B-A22B** naming — total parameters / activated parameters ("A22B" = 22B activated per token).

## Evidence and examples
- **Table 9 — SFT data examples for thinking and non-thinking modes** (verbatim in *Raw / preserved excerpts*).
- **Figure 2 — Qwen3-235B-A22B pass@1 vs thinking budget (1K–32K tokens, log x-axis; values read off the crop, approximate)**:

  | Budget (K tokens) | 1 | 2 | 4 | 8 | 16 | 32 | Non-thinking (dashed line) |
  |---|---|---|---|---|---|---|---|
  | AIME'24 | ≈42 | ≈42.7 | ≈56 | ≈72.5 | ≈84 | ≈86.7 | ≈40 |
  | AIME'25 | ≈30.6 | ≈35.6 | ≈42.7 | ≈59.6 | ≈76.7 | ≈81.7 | ≈24.7 |
  | LiveCodeBench (v5) | ≈45 | ≈48 | ≈52 | ≈59 | ≈65.5 | ≈67.7 | ≈35.3 |
  | GPQA Diamond | ≈64.2 | ≈64.3 | ≈68.1 | ≈70.3 | ≈70.6 | ≈72 | ≈62.9 |

  The non-thinking lines match Table 12's non-thinking scores (AIME'24 40.1, AIME'25 24.7, LiveCodeBench 35.3, GPQA 62.9). Even a 1K budget beats non-thinking on all four; gains are steepest between 2K and 16K on math.
- **Same model, thinking vs non-thinking (Qwen3-235B-A22B; Table 11 vs Table 12)**: AIME'24 85.7 vs 40.1; AIME'25 81.5 vs 24.7; LiveCodeBench v5 70.7 vs 35.3; CodeForces 2056 (98.2%) vs 1387 (75.7%); GPQA-Diamond 71.1 vs 62.9; MATH-500 98.0 vs 91.2; BFCL v3 70.8 vs 68.0; MMLU-Redux 92.7 vs 89.2; but Arena-Hard 95.6 vs 96.1 and IFEval 83.4 vs 83.2 — thinking buys a lot on math/code, almost nothing on alignment/chat.
- **Same for Qwen3-32B (Table 13 vs 14)**: AIME'24 81.4 vs 31.0; AIME'25 72.9 vs 20.2; LiveCodeBench 65.7 vs 31.3; GPQA 68.4 vs 54.6; Arena-Hard 93.8 vs 92.8.
- **Table 22 — Qwen3-32B across Stages 2, 3, 4** (Thinking / Non-thinking; deltas vs previous stage as printed):

  | Benchmark | S2 Thinking | S3 Thinking | S3 Non-thinking | S4 Thinking | S4 Non-thinking |
  |---|---|---|---|---|---|
  | LiveBench 2024-11-25 | 68.6 | 70.9 (+2.3) | 57.1 | 74.9 (+4.0) | 59.8 (+2.8) |
  | Arena-Hard | 86.8 | 89.4 (+2.6) | 88.5 | 93.8 (+4.4) | 92.8 (+4.3) |
  | CounterFactQA* | 50.4 | 61.3 (+10.9) | 64.3 | 68.1 (+6.8) | 66.4 (+2.1) |
  | IFEval strict prompt | 73.0 | 78.4 (+5.4) | 78.4 | 85.0 (+6.6) | 83.2 (+4.8) |
  | Multi-IF | 61.4 | 64.6 (+3.2) | 65.2 | 73.0 (+8.4) | 70.7 (+5.5) |
  | LengthCtrl* | 62.6 | 70.6 (+8.0) | 84.9 | 73.5 (+2.9) | 87.3 (+2.4) |
  | ThinkFollow* | – | 88.7 (single score for both modes) | | 98.9 (+10.2) | |
  | BFCL v3 | 69.0 | 68.4 (−0.6) | 61.5 | 70.3 (+1.9) | 63.0 (+1.5) |
  | ToolUse* | 63.3 | 70.4 (+7.1) | 73.2 | 85.5 (+15.1) | 86.5 (+13.3) |
  | MMLU-Redux | 91.4 | 91.0 (−0.4) | 86.7 | 90.9 (−0.1) | 85.7 (−1.0) |
  | GPQA-Diamond | 68.8 | 69.0 (+0.2) | 50.4 | 68.4 (−0.6) | 54.6 (+4.3) |
  | AIME'24 | 83.8 | 81.9 (−1.9) | 28.5 | 81.4 (−0.5) | 31.0 (+2.5) |
  | LiveCodeBench v5 | 68.4 | 67.2 (−1.2) | 31.1 | 65.7 (−1.5) | 31.3 (+0.2) |

  (* = in-house datasets.)
- **Table 21 — RL vs on-policy distillation on Qwen3-8B (from the same off-policy-distilled checkpoint; pass@64 in parentheses)**: Off-policy distillation AIME'24 55.0 (90.0), AIME'25 42.8 (83.3), MATH500 92.4, LiveCodeBench v5 42.0, MMLU-Redux 86.4, GPQA-Diamond 55.6; + RL 67.6 (90.0), 55.5 (83.3), 94.8, 52.9, 86.9, 61.3 — 17,920 GPU hours; + On-policy distillation 74.4 (93.3), 65.5 (86.7), 97.0, 60.3, 88.3, 63.3 — 1,800 GPU hours.
- **Evaluation settings (§4.6)**: thinking mode sampled at temperature 0.6, top-p 0.95, top-k 20; non-thinking temperature 0.7, top-p 0.8, top-k 20, presence penalty 1.5; max output 32,768 tokens, extended to 38,912 for AIME'24/'25 "to provide sufficient thinking space"; AIME = 30 questions, 64 samples each, averaged.
- **Table 23 (RULER, long context)**: Qwen3-235B-A22B avg 95.0 non-thinking vs 92.2 thinking; Qwen3-32B 93.7 vs 91.0; Qwen3-4B 85.2 vs 83.5 — thinking slightly worse for retrieval.
- **Base model comparisons (Tables 3–8)**: Qwen3-235B-A22B-Base beats DeepSeek-V3-Base "on 14 out of 15 evaluation benchmarks with only about 1/3 the total number of parameters and 2/3 activated parameters"; Qwen3 MoE bases match dense bases "with only 1/5 activated parameters"; Qwen3-1.7B/4B/8B/14B/32B-Base ≈ Qwen2.5-3B/7B/14B/32B/72B-Base.
- **Architecture tables**: dense — 0.6B (28 layers, 16/8 heads, 32K), 1.7B (28, 16/8, 32K), 4B (36, 32/8, 128K), 8B (36, 32/8, 128K), 14B (40, 40/8, 128K), 32B (64, 64/8, 128K); MoE — 30B-A3B (48 layers, 32/4 heads, 128/8 experts, 128K), 235B-A22B (94, 64/4, 128/8, 128K).
- **Cross-corpus note**: the gpt-oss model card (`openai-2025-gpt-oss-model-card.pdf.md`) lists "Qwen 3 Thinking" among the open models it compared against for biosecurity capability.

## Inconsistencies / open questions
- [verified] **"respectively" in the chat-template sentence does not match Table 9**: §4.3 says "we introduce /think and /no_think flags in the user query or system message, respectively", which reads as `/think` → user query and `/no_think` → system message; Table 9 shows both flags appended to the user query (`{query} /think`, `{query} /no_think`) — checked against the rendered Table 9. Most likely meaning: either flag can go in the user query or the system message. A slide should follow Table 9.
- [verified] **The thinking budget is not a trained skill, per the source**: §4.3 says budget handling "is not explicitly trained but emerges naturally as a result of applying Thinking Mode Fusion"; the mechanism is an inference-time cut ("we manually halt the thinking process and insert the stop-thinking instruction"). A slide saying "Qwen3 is trained to respect a budget" contradicts the text — checked in §4.3. What *is* trained: the on/off switch (SFT in Stage 3, format-following reward in Stage 4).
- [verified] **Fusion + General RL lowers thinking-mode scores on hard reasoning**: Table 22 thinking AIME'24 83.8 → 81.9 → 81.4 and LiveCodeBench 68.4 → 67.2 → 65.7; the authors state they "accept this performance trade-off" — checked in Table 22 and the (3) conclusion.
- [verified] **pdftotext mangles the flag names** (`/no think`, `<|im start|>`, `enable thinking=False`); the correct forms have underscores — checked against a rendering of the Table 9 region. Any text copied from a raw dump must be corrected.
- [open question] **Footnote 1 (chat template link) is not present in the text layer**: the Table 9 caption cites "the chat template¹", but page 11's extracted text ends without a footnote and the page has no link annotations. Would be settled by looking at the printed page bottom or the Qwen3 model card on Hugging Face.
- [open question] **No per-level effort (low/medium/high) exists in Qwen3** — control is binary mode + continuous token budget. Comparisons with gpt-oss's three levels (`openai-2025-gpt-oss-model-card.pdf.md`) are an analogy the deck would be drawing, not something either source states.
- [open question] Stage 1 cold-start size is not given ("a carefully selected subset", "minimize both the number of training samples and the training steps") — no count, unlike Stage 2's 3,995 pairs.
- [open question] How the budget threshold is exposed to users (API parameter name, default) is not described in the report; only the internal mechanism is.
- [open question] Figure 2 "if we further extend the output length beyond 32K, the model's performance is expected to improve further" is a projection, not a measurement.
- [open question] Table 22's 88.7 → 98.9 ThinkFollow is on an in-house, unreleased benchmark; not externally verifiable.
- [verified] Minor typos in the source: Table 6 caption says "Qwen8B-Base" (for Qwen3-8B-Base) and the row label "IINCLUDE"; the abstract uses "—–" dashes — checked in the `-layout` dump.

## Images / diagrams
Raster extraction (`pdfimages -png`) found 4 objects, all on page 1: two logos and their two `smask` alpha channels. Both logos are ≥ 300 px in at least one dimension, so under the presenter's rule (delete only when width **and** height < 300) they are kept; they were saved with the alpha mask applied (PyMuPDF) because without it the backgrounds render black. The smask files themselves are alpha channels, not images, and were not kept. Figures 1–2 are vector figures cropped with `cropfigs.py` (pages 9 and 20; both crops checked visually and correct). No other page has a "Figure N" caption; all remaining exhibits are text tables (captured in this record's text).

### `qwen-2025-qwen3-technical-report.pdf/images/fig-01-p009.png`
- Provenance: Figure 1 ("Post-training pipeline of the Qwen3 series models.") of `articles/qwen-2025-qwen3-technical-report.pdf`, page 9, vector figure; cropped with `cropfigs.py` (figure + labels + caption), 1035 × 473 px. **Key figure for the four-stage pipeline.**
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `qwen-2025-qwen3-technical-report.pdf/images/fig-02-p020.png`
- Provenance: Figure 2 ("Performance of Qwen3-235B-A22B with respect to the thinking budget."), page 20, vector figure (four panels: AIME'24, AIME'25, LiveCodeBench (v5), GPQA Diamond); cropped with `cropfigs.py`, 1035 × 724 px. **Key figure for the thinking-budget / effort topic.**
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `qwen-2025-qwen3-technical-report.pdf/images/logo-01-p001.png`
- Provenance: page 1 title block, embedded raster (JPEG object 31 + smask), 550 × 346 px, extracted with PyMuPDF with its alpha mask applied (a pixel-style icon).
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `qwen-2025-qwen3-technical-report.pdf/images/logo-02-p001.png`
- Provenance: page 1 title block, embedded raster (object 23 + smask), 2000 × 1027 px, extracted with PyMuPDF with its alpha mask applied (Qwen logo with wordmark).
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

## Raw / preserved excerpts

### Abstract (complete)
> In this work, we present Qwen3, the latest version of the Qwen model family. Qwen3 comprises a series of large language models (LLMs) designed to advance performance, efficiency, and multilingual capabilities. The Qwen3 series includes models of both dense and Mixture-of-Expert (MoE) architectures, with parameter scales ranging from 0.6 to 235 billion. A key innovation in Qwen3 is the integration of thinking mode (for complex, multi-step reasoning) and non-thinking mode (for rapid, context-driven responses) into a unified framework. This eliminates the need to switch between different models—–such as chat-optimized models (e.g., GPT-4o) and dedicated reasoning models (e.g., QwQ-32B)—–and enables dynamic mode switching based on user queries or chat templates. Meanwhile, Qwen3 introduces a thinking budget mechanism, allowing users to allocate computational resources adaptively during inference, thereby balancing latency and performance based on task complexity. Moreover, by leveraging the knowledge from the flagship models, we significantly reduce the computational resources required to build smaller-scale models, while ensuring their highly competitive performance. Empirical evaluations demonstrate that Qwen3 achieves state-of-the-art results across diverse benchmarks, including tasks in code generation, mathematical reasoning, agent tasks, etc., competitive against larger MoE models and proprietary models. Compared to its predecessor Qwen2.5, Qwen3 expands multilingual support from 29 to 119 languages and dialects, enhancing global accessibility through improved cross-lingual understanding and generation capabilities. To facilitate reproducibility and community-driven research and development, all Qwen3 models are publicly accessible under Apache 2.0.

### §1 Introduction — modes, budgets, and post-training overview
> Qwen3 introduces several key advancements to enhance its functionality and usability. First, it integrates two distinct operating modes, thinking mode and non-thinking mode, into a single model. This allows users to switch between these modes without alternating between different models, e.g., switching from Qwen2.5 to QwQ (Qwen Team, 2024). This flexibility ensures that developers and users can adapt the model's behavior to suit specific tasks efficiently. Additionally, Qwen3 incorporates thinking budgets, providing users with fine-grained control over the level of reasoning effort applied by the model during task execution. This capability is crucial to the optimization of computational resources and performance, tailoring the model's thinking behavior to meet varying complexity in real-world applications. Furthermore, Qwen3 has been pre-trained on 36 trillion tokens covering up to 119 languages and dialects, effectively enhancing its multilingual capabilities.

> To better align foundation models with human preferences and downstream applications, we employ a multi-stage post-training approach that empowers both thinking (reasoning) and non-thinking modes. In the first two stages, we focus on developing strong reasoning abilities through long chain-of-thought (CoT) cold-start finetuning and reinforcement learning focusing on mathematics and coding tasks. In the final two stages, we combine data with and without reasoning paths into a unified dataset for further fine-tuning, enabling the model to handle both types of input effectively, and we then apply general-domain reinforcement learning to improve performance across a wide range of downstream tasks. For smaller models, we use strong-to-weak distillation, leveraging both off-policy and on-policy knowledge transfer from larger models to enhance their capabilities. Distillation from advanced teacher models significantly outperforms reinforcement learning in performance and training efficiency.

> ... Furthermore, we observe that increasing the thinking budget for thinking tokens leads to a consistent improvement in the model's performance across various tasks.

### §3.2 Pre-training Stage (complete list)
> (1) General Stage (S1): At the first pre-training stage, all Qwen3 models are trained on over 30 trillion tokens using a sequence length of 4,096 tokens. At this stage, the models have been fully pre-trained on language proficiency and general world knowledge, with training data covering 119 languages and dialects.
> (2) Reasoning Stage (S2): To further improve the reasoning ability, we optimize the pre-training corpus of this stage by increasing the proportion of STEM, coding, reasoning, and synthetic data. The models are further pre-trained with about 5T higher-quality tokens at a sequence length of 4,096 tokens. We also accelerate the learning rate decay during this stage.
> (3) Long Context Stage: In the final pre-training stage, we collect high-quality long context corpora to extend the context length of Qwen3 models. All models are pre-trained on hundreds of billions of tokens with a sequence length of 32,768 tokens. The long context corpus includes 75% of text between 16,384 to 32,768 tokens in length, and 25% of text between 4,096 to 16,384 in length. Following Qwen2.5 (Yang et al., 2024b), we increase the base frequency of RoPE from 10,000 to 1,000,000 using the ABF technique (Xiong et al., 2023). Meanwhile, we introduce YARN (Peng et al., 2023) and Dual Chunk Attention (DCA, An et al., 2024) to achieve a four-fold increase in sequence length capacity during inference.

### §4 Post-training (opening, complete)
> The post-training pipeline of Qwen3 is strategically designed with two core objectives:
> (1) Thinking Control: This involves the integration of two distinct modes, namely the "non-thinking" and "thinking" modes, providing users with the flexibility to choose whether the model should engage in reasoning or not, and to control the depth of thinking by specifying a token budget for the thinking process.
> (2) Strong-to-Weak Distillation: This aims to streamline and optimize the post-training process for lightweight models. By leveraging the knowledge from large-scale models, we substantially reduce both the computational costs and the development efforts required for building smaller-scale models.
>
> As illustrated in Figure 1, the flagship models in the Qwen3 series follow a sophisticated four-stage training process. The first two stages focus on developing the models' "thinking" abilities. The next two stages aim to integrate strong "non-thinking" functionalities into the models.
>
> Preliminary experiments suggest that directly distilling the output logits from teacher models into lightweight student models can effectively enhance their performance while maintaining fine-grained control over their reasoning processes. This approach eliminates the necessity of performing an exhaustive four-stage training process individually for every small-scale model. It leads to better immediate performance, as indicated by higher Pass@1 scores, and also improves the model's ability of exploration, as reflected in improved Pass@64 results. In addition, it achieves these gains with much greater training efficiency, requiring only 1/10 of the GPU hours compared to the four-stage training method.

### Figure 1 (text of the vector diagram, from the text layer)
> Flagship Models: Base Models → Stage 1 Long-CoT Cold Start → Stage 2 Reasoning RL → Stage 3 Thinking Mode Fusion → Stage 4 General RL → Qwen3-235B-A22B, Qwen3-32B
> Lightweight Models: Base Models → Strong-to-Weak Distillation → Qwen3-30B-A3B, 14B/8B/4B/1.7B/0.6B
> Figure 1: Post-training pipeline of the Qwen3 series models.

### §4.1 Long-CoT Cold Start (complete)
> We begin by curating a comprehensive dataset that spans a wide range of categories, including math, code, logical reasoning, and general STEM problems. Each problem in the dataset is paired with verified reference answers or code-based test cases. This dataset serves as the foundation for the "cold start" phase of long Chain-of-Thought (long-CoT) training.
>
> The dataset construction involves a rigorous two-phase filtering process: query filtering and response filtering. In the query filtering phase, we use Qwen2.5-72B-Instruct to identify and remove queries that are not easily verifiable. This includes queries containing multiple sub-questions or those asking for general text generation. Furthermore, we exclude queries that Qwen2.5-72B-Instruct can answer correctly without using CoT reasoning. This helps prevent the model from relying on superficial guessing and ensures that only complex problems requiring deeper reasoning are included. Additionally, we annotate each query's domain using Qwen2.5-72B-Instruct to maintain balanced domain representation across the dataset.
>
> After reserving a validation query set, we generate N candidate responses for each remaining query using QwQ-32B (Qwen Team, 2025). When QwQ-32B consistently fails to generate correct solutions, human annotators manually assess the accuracy of the responses. For queries with positive Pass@N, further stringent filtering criteria are applied to remove responses that (1) yield incorrect final answers, (2) contain substantial repetition, (3) clearly indicate guesswork without adequate reasoning, (4) exhibit inconsistencies between the thinking and summary contents, (5) involve inappropriate language mixing or stylistic shifts, or (6) are suspected of being overly similar to potential validation set items. Subsequently, a carefully selected subset of the refined dataset is used for the initial cold-start training of the reasoning patterns. The objective at this stage is to instill foundational reasoning patterns in the model without overly emphasizing immediate reasoning performance. This approach ensures that the model's potential is not limited, allowing for greater flexibility and improvement during the subsequent reinforcement learning (RL) phase. To achieve this objective effectively, it is preferable to minimize both the number of training samples and the training steps during this preparatory phase.

### §4.2 Reasoning RL (complete)
> The query-verifier pairs used in the Reasoning RL stage must satisfy the following four criteria: (1) They were not used during the cold-start phase. (2) They are learnable for the cold-start model. (3) They are as challenging as possible. (4) They cover a broad range of sub-domains. We ultimately collect a total of 3,995 query-verifier pairs, and employed GRPO (Shao et al., 2024) to update the model parameters. We observe that using a large batch size and a high number of rollouts per query, along with off-policy training to improve sample efficiency, is beneficial to the training process. We have also addressed how to balance exploration and exploitation by controlling the model's entropy to increase steadily or remain stable, which is crucial for maintaining stable training. As a result, we achieve consistent improvements in both training reward and validation performance over the course of a single RL run, without any manual intervention on hyperparameters. For instance, the AIME'24 score of the Qwen3-235B-A22B model increases from 70.1 to 85.1 over a total of 170 RL training steps.

### Table 9 (verbatim; underscores restored from the rendered page — see Provenance)
> Table 9: **Examples of SFT data for thinking and non-thinking modes during the thinking mode fusion stage.** For the thinking mode, the /think flag can be omitted since it represents the default behavior. This feature has been implemented in the chat template¹ supported by the Hugging Face's tokenizer, where the thinking mode can be disabled using an additional parameter enable_thinking=False.

Thinking Mode:
```
<|im_start|>user
{query} /think<|im_end|>
<|im_start|>assistant
<think>
{thinking_content}
</think>

{response}<|im_end|>
```

Non-Thinking Mode:
```
<|im_start|>user
{query} /no_think<|im_end|>
<|im_start|>assistant
<think>

</think>

{response}<|im_end|>
```
(In the source the two columns sit side by side; `{query}` and `{response}` are printed in blue, `/think`, `/no_think` and `{thinking_content}` in red. The empty line inside the non-thinking `<think>` block is how the table aligns the two columns: the non-thinking block is empty.)

### §4.3 Thinking Mode Fusion (complete)
> The goal of the Thinking Mode Fusion stage is to integrate the "non-thinking" capabilities into the previously developed "thinking" model. This approach allows developers to manage and control reasoning behaviors, while also reducing the cost and complexity of deploying separate models for thinking and non-thinking tasks. To achieve this, we conduct continual supervised fine-tuning (SFT) on the Reasoning RL model and design a chat template to fuse the two modes. Moreover, we find that models capable of handling both modes proficiently perform consistently well under different thinking budgets.
>
> **Construction of SFT data.** The SFT dataset combines both the "thinking" and "non-thinking" data. To ensure that the performance of the Stage 2 model is not compromised by the additional SFT, the "thinking" data is generated via rejection sampling on Stage 1 queries using the Stage 2 model itself. The "non-thinking" data, on the other hand, is carefully curated to cover a diverse range of tasks, including coding, mathematics, instruction-following, multilingual tasks, creative writing, question answering, and role-playing. Additionally, we employ automatically generated checklists for assessing the response quality of "non-thinking" data. To enhance the performance on tasks with low-resource languages, we particularly increase the proportion of translation tasks.
>
> **Chat Template Design.** To better integrate the two modes and enable users to dynamically switch the model's thinking process, we design chat templates for Qwen3, as shown in Table 9. Specifically, for samples in thinking mode and non-thinking mode, we introduce /think and /no_think flags in the user query or system message, respectively. This allows the model to follow the user's input and select the appropriate thinking mode accordingly. For non-thinking mode samples, we retain an empty thinking block in the assistant's response. This design ensures internal format consistency within the model and allows developers to prevent the model from engaging in thinking behavior by concatenating an empty think block in the chat template. By default, the model operates in thinking mode; therefore, we add some thinking mode training samples where the user queries do not include /think flags. For more complex multi-turn dialogs, we randomly insert multiple /think and /no_think flags into users' queries, with the model response adhering to the last flag encountered.
>
> **Thinking Budget.** An additional advantage of Thinking Mode Fusion is that, once the model learns to respond in both non-thinking and thinking modes, it naturally develops the ability to handle intermediate cases—generating responses based on incomplete thinking. This capability lays the foundation for implementing budget control over the model's thinking process. Specifically, when the length of the model's thinking reaches a user-defined threshold, we manually halt the thinking process and insert the stop-thinking instruction: "Considering the limited time by the user, I have to give the solution based on the thinking directly now.\n</think>.\n\n". After this instruction is inserted, the model proceeds to generate a final response based on its accumulated reasoning up to that point. It is worth noting that this ability is not explicitly trained but emerges naturally as a result of applying Thinking Mode Fusion.

### §4.4 General RL (complete)
> The General RL stage aims to broadly enhance the models' capabilities and stability across diverse scenarios. To facilitate this, we have established a sophisticated reward system covering over 20 distinct tasks, each with customized scoring criteria. These tasks specifically target enhancements in the following core capabilities:
> • Instruction Following: This capability ensures that models accurately interpret and follow user instructions, including requirements related to content, format, length, and the use of structured output, delivering responses that align with user expectations.
> • Format Following: In addition to explicit instructions, we expect the model to adhere to specific formatting conventions. For instance, it should respond appropriately to the /think and /no_think flags by switching between thinking and non-thinking modes, and consistently use designated tokens (e.g., <think> and </think>) to separate the thinking and response parts in the final output.
> • Preference Alignment: For open-ended queries, preference alignment focuses on improving the model's helpfulness, engagement, and style, ultimately delivering a more natural and satisfying user experience.
> • Agent Ability: This involves training the model to correctly invoke tools via designated interfaces. During the RL rollout, the model is allowed to perform complete multi-turn interaction cycles with real environment execution feedback, thereby improving its performance and stability in long-horizon decision-making tasks.
> • Abilities for Specialized Scenarios: In more specialized scenarios, we design tasks tailored to the specific context. For example, in Retrieval-Augmented Generation (RAG) tasks, we incorporate reward signals to guide the model toward generating accurate and contextually appropriate responses, thereby minimizing the risk of hallucination.
>
> To provide feedback for the aforementioned tasks, we utilized three distinct types of rewards:
> (1) Rule-based Reward: The rule-based reward has been widely used in the reasoning RL stage, and is also useful for general tasks such as instruction following (Lambert et al., 2024) and format adherence. Well-designed rule-based rewards can assess the correctness of model outputs with high precision, preventing issues like reward hacking.
> (2) Model-based Reward with Reference Answer: In this approach, we provide a reference answer for each query and prompt Qwen2.5-72B-Instruct to score the model's response based on this reference. This method allows for more flexible handling of diverse tasks without requiring strict formatting, avoiding false negatives that can occur with purely rule-based rewards.
> (3) Model-based Reward without Reference Answer: Leveraging human preference data, we train a reward model to assign scalar scores to model responses. This approach, which does not depend on a reference answer, can handle a broader range of queries while effectively enhancing the model's engagement and helpfulness.

### §4.5 Strong-to-Weak Distillation (complete)
> The Strong-to-Weak Distillation pipeline is specifically designed to optimize lightweight models, encompassing 5 dense models (Qwen3-0.6B, 1.7B, 4B, 8B, and 14B) and one MoE model (Qwen3-30B-A3B). This approach enhances model performance while effectively imparting robust mode-switching capabilities. The distillation process is divided into two primary phases:
> (1) Off-policy Distillation: At this initial phase, we combine the outputs of teacher models generated with both /think and /no_think modes for response distillation. This helps lightweight student models develop basic reasoning skills and the ability to switch between different modes of thinking, laying a solid foundation for the next on-policy training phase.
> (2) On-policy Distillation: In this phase, the student model generates on-policy sequences for fine-tuning. Specifically, prompts are sampled, and the student model produces responses in either /think or /no_think mode. The student model is then fine-tuned by aligning its logits with those of a teacher model (Qwen3-32B or Qwen3-235B-A22B) to minimize the KL divergence.

### §4.6 Sampling settings
> For all Qwen3 models in the thinking mode, we utilize a sampling temperature of 0.6, a top-p value of 0.95, and a top-k value of 20. Additionally, for Creative Writing v3 and WritingBench, we apply a presence penalty of 1.5 to encourage the generation of more diverse content. For Qwen3 models in the non-thinking mode, we configure the sampling hyperparameters with temperature = 0.7, top-p = 0.8, top-k = 20, and presence penalty = 1.5. For both the thinking and non-thinking modes, we set the max output length to 32,768 tokens, except AIME'24 and AIME'25 where we extend this length to 38,912 tokens to provide sufficient thinking space.

### §4.7 Discussion — thinking budget, on-policy distillation, fusion + general RL
> **The Effectiveness of Thinking Budget** To verify that Qwen3 can enhance its intelligence level by leveraging an increased thinking budget, we adjust the allocated thinking budget on four benchmarks across Mathematics, Coding, and STEM domains. The resulting scaling curves are presented in Figure 2, Qwen3 demonstrates scalable and smooth performance improvements correlated to the allocated thinking budget. Moreover, we observe that if we further extend the output length beyond 32K, the model's performance is expected to improve further in the future. We leave this exploration as future work.
>
> Figure 2: Performance of Qwen3-235B-A22B with respect to the thinking budget.
>
> **The Effectiveness and Efficiency of On-Policy Distillation** We evaluate the effectiveness and efficiency of on-policy distillation by comparing the performance and computational cost—measured in GPU hours—after undergoing distillation versus direct reinforcement learning, both starting from the same off-policy distilled 8B checkpoint. For simplicity, we focus solely on math and code-related queries in this comparison. The results, summarized in Table 21, show that distillation achieves significantly better performance than reinforcement learning while requiring approximately only 1/10 of the GPU hours. Furthermore, distillation from teacher logits enables the student model to expand its exploration space and enhance its reasoning potential, as evidenced by the improved pass@64 scores on the AIME'24 and AIME'25 benchmarks after distillation, compared to the initial checkpoint. In contrast, reinforcement learning does not lead to any improvement in pass@64 scores. These observations highlight the advantages of leveraging a stronger teacher model in guiding student model learning.
>
> **The Effects of Thinking Mode Fusion and General RL** To evaluate the effectiveness of Thinking Mode Fusion and General Reinforcement Learning (RL) during the post-training, we conduct evaluations on various stages of the Qwen-32B model. In addition to the datasets mentioned earlier, we introduce several in-house benchmarks to monitor other capabilities. These benchmarks include:
> • CounterFactQA: Contains counterfactual questions where the model needs to identify that the questions are not factual and avoid generating hallucinatory answers.
> • LengthCtrl: Includes creative writing tasks with length requirements; the final score is based on the difference between the generated content length and the target length.
> • ThinkFollow: Involves multi-turn dialogues with randomly inserted /think and /no_think flags to test whether the model can correctly switch thinking modes based on user queries.
> • ToolUse: Evaluates the stability of the model in single-turn, multi-turn, and multi-step tool calling processes. The score includes accuracy in intent recognition, format accuracy, and parameter accuracy during the tool calling process.
>
> The results are shown in Table 22, where we can draw the following conclusions:
> (1) Stage 3 integrates the non-thinking mode into the model, which already possesses thinking capabilities after the first two stages of training. The ThinkFollow benchmark score of 88.7 indicates that the model has developed an initial ability to switch between modes, though it still occasionally makes errors. Stage 3 also enhances the model's general and instruction-following capabilities in thinking mode, with CounterFactQA improving by 10.9 points and LengthCtrl by 8.0 points.
> (2) Stage 4 further strengthens the model's general, instruction-following, and agent capabilities in both thinking and non-thinking modes. Notably, the ThinkFollow score improves to 98.9, ensuring accurate mode switching.
> (3) For Knowledge, STEM, Math, and Coding tasks, Thinking Mode Fusion and General RL do not bring significant improvements. In contrast, for challenging tasks like AIME'24 and LiveCodeBench, the performance in thinking mode actually decreases after these two training stages. We conjecture this degradation is due to the model being trained on a broader range of general tasks, which may compromise its specialized capabilities in handling complex problems. During the development of Qwen3, we choose to accept this performance trade-off to enhance the model's overall versatility.

### A.1.1 Long-Context Ability (commentary)
> For evaluating long-context processing capabilities, we report the results on the RULER benchmark (Hsieh et al., 2024) in Table 23. To enable length extrapolation, we utilize YARN (Peng et al., 2023) with a scaling factor=4. In thinking mode, we set the thinking budget to 8192 tokens to mitigate overly verbose reasoning on the extremely long inputs.
> The results show that:
> 1. In non-thinking mode, Qwen3 outperforms Qwen2.5 models of a similar size in long-context processing tasks.
> 2. In thinking mode, the model's performance slightly degrades. We hypothesize that the thinking content does not provide significant benefits for these retrieval tasks, which do not rely on reasoning and may instead interfere with the retrieval process. We are committed to enhancing the long-context capability in the thinking mode in future versions.

### §5 Conclusion (complete)
> In this technical report, we introduce Qwen3, the latest version of the Qwen series. Qwen3 features both thinking mode and non-thinking mode, allowing users to dynamically manage the number of tokens used for complex thinking tasks. The model was pre-trained on an extensive dataset containing 36 trillion tokens, enabling it to understand and generate text in 119 languages and dialects. Through a series of comprehensive evaluations, Qwen3 has shown strong performance across a range of standard benchmarks for both pre-trained and post-trained models, including tasks related to code generation, mathematics, reasoning, and agents.
>
> In the near future, our research will focus on several key areas. We will continue to scale up pretraining by using data that is both higher in quality and more diverse in content. At the same time, we will work on improving model architecture and training methods for the purposes of effective compression, scaling to extremely long contexts, etc. In addition, we plan to increase computational resources for reinforcement learning, with a particular emphasis on agent-based RL systems that learn from environmental feedback. This will allow us to build agents capable of tackling complex tasks that require inference time scaling.
