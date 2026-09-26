---
source_file: openai-2025-gpt-oss-model-card.pdf
source_type: article
ingested_at: 2026-09-26
---

# gpt-oss-120b & gpt-oss-20b Model Card

## Provenance
- Original location: articles/openai-2025-gpt-oss-model-card.pdf
- Format: pdf (35 pages; printed folio = PDF page − 1, e.g. Figure 3 is on PDF page 8 / printed page 7 — this record cites **PDF page numbers**)
- Author / source (if known): OpenAI (corporate author; contributor list of ~120 names "alphabetical by surname", Section 8).
- Date of original (if known): document dated "August 5, 2025"; arXiv:2508.10925v1 [cs.CL], 8 Aug 2025.
- arXiv: 2508.10925v1 [cs.CL]
- Extraction: `pdftotext` (poppler, reading order and `-layout`). Tables re-read from the `-layout` dump (column order verified). Figures 1–4 are vector plots (text layer garbled in the reading-order dump; values in this record for them were read from the vector crops). Figures 5–18 are embedded rasters with **no text layer**: their captions exist only as one-line "Figure N" labels plus a following paragraph, and the appendix examples (Figures 17–18, the harmony-format prompt with `reasoning: low`) exist only as images — their text is transcribed below in *Raw / preserved excerpts* from the extracted image so it is not lost.
- Focus note (why this source was added): the presenter's note "Effort, example on how is trained for that" — the low/medium/high reasoning-effort setting. The relevant material is §2.5 (Post-Training for Reasoning and Tool Use), §2.5.1 (Harmony Chat Format), §2.5.2 (Variable Effort Reasoning Training), §2.6.1 (Test-time scaling), Figure 3, Table 3, and Appendix 1 (Figures 17–18).

## Key claims
- **What the models are**: "two open-weight reasoning models available under the Apache 2.0 license and our gpt-oss usage policy ... designed to be used within agentic workflows with strong instruction following, tool use like web search and Python code execution, and reasoning capabilities—including the ability to adjust the reasoning effort for tasks that don't require complex reasoning. The models are customizable, provide full chain-of-thought (CoT), and support Structured Outputs."
- **Reasoning effort — the whole of what the card says about training it (§2.5.2, verbatim)**: "We train the models to support three reasoning levels: low, medium, and high. These levels are configured in the system prompt by inserting keywords such as "Reasoning: low". Increasing the reasoning level will cause the model's average CoT length to increase."
- **How post-training is done (§2.5)**: "After pre-training, we post-train the models using similar CoT RL techniques as OpenAI o3. This procedure teaches the models how to reason and solve problems using CoT and teaches the model how to use tools. Because of the similar RL techniques, these models have a personality similar to models served in our first-party products like ChatGPT. Our training dataset consists of a wide range of problems from coding, math, science, and more."
- **Effort is a system-prompt control, not a separate model**: the same weights serve low/medium/high; the level is a keyword in the system message of the harmony format (Figure 17 shows `reasoning: low` inside the `system` message, together with "Knowledge cutoff", "Current date" and the list of valid channels).
- **Test-time scaling (§2.6.1, verbatim)**: "Our models demonstrate smooth test-time scaling. In Figure 3, we sweep over the different reasoning modes of the model (low, medium, high) and plot accuracy versus average CoT+Answer length. We generally see log-linear returns on most tasks, where longer CoTs provide higher accuracy at a relatively large increase in final response latency and cost. We recommend that users pick a model size and corresponding reasoning level that balances these tradeoffs for their use case."
- **Figure 3 caption (verbatim)**: "We evaluate AIME and GPQA using the three different reasoning modes (low, medium, high) and plot accuracy against the average CoT + Answer length. We find that there is smooth test-time scaling of accuracy when increasing the reasoning level."
- **Long CoTs explain math strength**: "The gpt-oss models are strong at math in particular, which we believe is because they can use very long CoTs effectively, e.g., our gpt-oss-20b use over 20k CoT tokens per problem on average for AIME. On more knowledge-related tasks such as GPQA, the gpt-oss-20b model lags behind due to its smaller size."
- **Headline evals are reported at "high"**: "For all datasets, we report basic pass@1 results for high reasoning mode using the model's default system prompt." Figures 1, 2, 4 all compare "the gpt-oss models at reasoning level high".
- **Harmony chat format — channels separate CoT from answer (§2.5.1)**: channels "indicate the intended visibility of each message, e.g., analysis for CoT tokens, commentary for function tool calling and final for answers shown to users." It enables "interleaving tool calls within the CoT or providing preambles that outline longer action plans to the user." Deployment note: "in multi-turn conversations the reasoning traces from past assistant turns should be removed."
- **Role hierarchy**: "the models follow a role-based information hierarchy to resolve instruction conflicts: System > Developer > User > Assistant > Tool."
- **Tools are also a system-prompt switch**: "The models have been trained to support running with and without these tools by specifying so in the system prompt." Tools: a browsing tool (`search`, `open`), a python tool ("stateful Jupyter notebook environment"), and "Arbitrary developer functions" defined in a Developer message.
- **No optimization pressure on the CoT (§4.4)**: "we decided not to put any direct optimization pressure on the CoT for either of our two open-weight models. We hope that this gives developers the opportunity to implement CoT monitoring systems in their projects and enables the research community to further study CoT monitorability." Consequence: CoTs "can contain hallucinated content, including language that does not reflect OpenAI's standard safety policies. Developers should not directly show chains of thought to users of their applications, without further filtering, moderation, or summarization".
- **Architecture**: autoregressive MoE transformers building on GPT-2/GPT-3; 120b = 36 layers, 116.8B total / 5.1B active per token; 20b = 24 layers, 20.9B total / 3.6B active. Top-4 experts per token (128 experts in 120b, 32 in 20b); residual dimension 2880; alternating banded-window (128 tokens) and dense attention; GQA with 8 KV heads; RoPE, context extended to 131,072 tokens with YaRN; learned attention-sink bias.
- **Quantization**: MoE weights post-trained in MXFP4 ("4.25 bits per parameter"); MoE weights are "90+% of the total parameter count"; lets 120b "fit on a single 80GB GPU" and 20b "run on systems with as little as 16GB memory".
- **Pretraining**: "a text-only dataset with trillions of tokens, with a focus on STEM, coding, and general knowledge"; harmful-content filtering reused "the CBRN pre-training filters from GPT-4o"; knowledge cutoff June 2024. "The training run for gpt-oss-120b required 2.1 million H100-hours to complete, with gpt-oss-20b needing almost 10x fewer."
- **Tokenizer**: `o200k_harmony`, a BPE extending o200k (GPT-4o, o4-mini) with harmony-format tokens; 201,088 tokens total.
- **Safety training**: "During post-training, we use deliberative alignment[29] to teach the models to refuse on a wide range of content (e.g., illicit advice), be robust to jailbreaks, and adhere to the instruction hierarchy[30]." Instruction hierarchy was taught by collecting conflicting-role examples and supervising the model "to follow the instructions in the system message over developer messages, and instructions in developer messages over user messages."
- **Worst-case (adversarial) fine-tuning**: OpenAI trained internal "helpful-only" and domain-maximized (bio, cyber) versions of gpt-oss-120b with "incremental reinforcement learning" on its o-series RL stack, "During training and evaluation time, we use the highest reasoning setting on gpt-oss." SAG concluded that even so "gpt-oss-120b did not reach High capability in Biological and Chemical Risk or Cyber risk."
- **Relative position**: "gpt-oss-120b surpasses OpenAI o3-mini and approaches OpenAI o4-mini accuracy. The smaller gpt-oss-20b model is also surprisingly competitive, despite being 6 times smaller than gpt-oss-120b."
- **Hallucination**: both underperform o4-mini on SimpleQA/PersonQA — "expected, as smaller models have less world knowledge than larger frontier models and tend to hallucinate more."

## Definitions and terminology
- **Reasoning level / reasoning effort / reasoning mode** — one of `low`, `medium`, `high`; set by a keyword in the system prompt ("Reasoning: low" in §2.5.2; rendered `reasoning: low` in Figure 17). Higher level → longer average CoT. The card uses "reasoning level", "reasoning mode" and "reasoning effort" interchangeably.
- **Variable Effort Reasoning Training** — the §2.5.2 heading for training the model to honor the three levels. No further mechanism (data, reward, length targets) is described.
- **CoT RL** — reinforcement learning on chain-of-thought, "similar ... as OpenAI o3".
- **Test-time scaling** — accuracy rising with the amount of inference compute (CoT + answer tokens); here "log-linear returns".
- **Harmony chat format** — OpenAI's custom chat format with special tokens (`<|start|>`, `<|message|>`, `<|channel|>`, `<|constrain|>`, `<|end|>`, `<|call|>`), roles (system, developer, user, assistant, tool) and channels.
- **Channels** — `analysis` (CoT), `commentary` (function tool calls, preambles), `final` (answer shown to user).
- **Instruction hierarchy** — System > Developer > User > Assistant > Tool.
- **Deliberative alignment** — OpenAI technique (ref. [29], Guan et al. 2024) used to teach refusals.
- **Active parameters** — parameters used per token per forward pass in the MoE ("Unembedding parameters are counted towards active, but not embeddings").
- **MXFP4** — OCP Microscaling 4-bit format; 4.25 bits per parameter.
- **Helpful-only training** — "an additional stage of reinforcement learning to reward answers that comply with unsafe prompts" (used to simulate a malicious fine-tuner).
- **Model card vs system card** — "We're terming this document a model card, rather than a system card, because the gpt-oss models will be used as part of a wide range of systems, created and maintained by a wide range of stakeholders."

## Evidence and examples
- **Table 3 — evaluations across reasoning levels (verbatim values, from `-layout` dump)**:

  | Benchmark (Accuracy %) | 120b low | 120b medium | 120b high | 20b low | 20b medium | 20b high |
  |---|---|---|---|---|---|---|
  | AIME 2024 (no tools) | 56.3 | 80.4 | 95.8 | 42.1 | 80.0 | 92.1 |
  | AIME 2024 (with tools) | 75.4 | 87.9 | 96.6 | 61.2 | 86.0 | 96.0 |
  | AIME 2025 (no tools) | 50.4 | 80.0 | 92.5 | 37.1 | 72.1 | 91.7 |
  | AIME 2025 (with tools) | 72.9 | 91.6 | 97.9 | 57.5 | 90.4 | 98.7 |
  | GPQA Diamond (no tools) | 67.1 | 73.1 | 80.1 | 56.8 | 66.0 | 71.5 |
  | GPQA Diamond (with tools) | 68.1 | 73.5 | 80.9 | 58.0 | 67.1 | 74.2 |
  | HLE (no tools) | 5.2 | 8.6 | 14.9 | 4.2 | 7.0 | 10.9 |
  | HLE (with tools) | 9.1 | 11.3 | 19.0 | 6.3 | 8.8 | 17.3 |
  | MMLU | 85.9 | 88.0 | 90.0 | 80.4 | 84.0 | 85.3 |
  | SWE-Bench Verified | 47.9 | 52.6 | 62.4 | 37.4 | 53.2 | 60.7 |
  | Tau-Bench Retail | 49.4 | 62.0 | 67.8 | 35.0 | 47.3 | 54.8 |
  | Tau-Bench Airline | 42.6 | 48.6 | 49.2 | 32.0 | 42.6 | 38.0 |
  | Aider Polyglot | 24.0 | 34.2 | 44.4 | 16.6 | 26.6 | 34.2 |
  | MMMLU (Average) | 74.1 | 79.3 | 81.3 | 67.0 | 73.5 | 75.7 |
  | HealthBench (score %) | 53.0 | 55.9 | 57.6 | 40.4 | 41.8 | 42.5 |
  | HealthBench Hard | 22.8 | 26.9 | 30.0 | 9.0 | 12.9 | 10.8 |
  | HealthBench Consensus | 90.6 | 90.8 | 89.9 | 84.9 | 83.0 | 82.6 |
  | Codeforces Elo (no tools) | 1595 | 2205 | 2463 | 1366 | 1998 | 2230 |
  | Codeforces Elo (with tools) | 1653 | 2365 | 2622 | 1251 | 2064 | 2516 |

  Effort effect is largest on math/code: e.g. AIME 2025 no-tools 120b 50.4 → 80.0 → 92.5; Codeforces no-tools 120b 1595 → 2205 → 2463 Elo. Small on knowledge: MMLU 120b 85.9 → 88.0 → 90.0. Not always monotonic (see *Inconsistencies*).
- **Figure 3 — accuracy vs. average CoT + Answer length (values read from the vector plot; x-axis log-scale, approximate)**:
  - AIME 2025, gpt-oss-120b: low ≈ 73% at ≈1.2k tokens; medium ≈ 91.5% at ≈4.3k; high ≈ 98% at ≈13k.
  - AIME 2025, gpt-oss-20b: low ≈ 57.5% at ≈1.1k; medium ≈ 90.4% at ≈6k; high ≈ 98.7% at ≈20k.
  - GPQA Diamond, gpt-oss-120b: low ≈ 68% at ≈1.3k; medium ≈ 73.5% at ≈3.8k; high ≈ 81% at ≈17k.
  - GPQA Diamond, gpt-oss-20b: low ≈ 58% at ≈0.9k; medium ≈ 67% at ≈7k; high ≈ 74% at ≈30k.
  - Reading: each step up in level multiplies CoT length by roughly 3–5×; the smaller model spends more tokens at the same level (20b "high" ≈ 20k on AIME, matching the §2.6.1 "over 20k CoT tokens per problem" statement).
- **Table 1 — parameter counts**: MLP 114.71B / 19.12B; Attention 0.96B / 0.64B; Embed+Unembed 1.16B / 1.16B; Active 5.13B / 3.61B; Total 116.83B / 20.91B; Checkpoint 60.8 GiB / 12.8 GiB (120b / 20b).
- **Figure 1 (at high)**: AIME 2024 with tools — o3 95.2, o3-mini* 87.3, o4-mini 98.7, gpt-oss-120b 96.6, gpt-oss-20b 96.0; AIME 2025 with tools — 98.4, 86.5*, 99.5, 97.9, 98.7; GPQA Diamond no tools — 83.3, 77.0, 81.4, 80.1, 71.5; HLE — o3 (tool) 24.9, o3-mini (no tool) 13.4, o4-mini (tool) 17.7, 120b tool 19.0 / no tool 14.9, 20b tool 17.3 / no tool 10.9; MMLU — 93.4, 87.0, 93.0, 90.0, 85.3. (*o3-mini evaluated on AIME without tools.)
- **Figure 2 (at high)**: Codeforces Elo — o3 (tool) 2706, o3-mini (no tool) 2073, o4-mini (tool) 2719, 120b tool 2622 / no tool 2463, 20b tool 2516 / no tool 2230; SWE-Bench Verified — 69.1, 49.3, 68.1, 62.4, 60.7; Tau-Bench Retail — 70.4, 57.6, 65.6, 67.8, 54.8.
- **Figure 4 (at high)**: HealthBench — gpt-4o 32.0, o1 41.8, o3 59.8, o3-mini 37.8, o4-mini 50.1, 120b 57.6, 20b 42.5; HealthBench Hard — 0.0, 7.9, 31.6, 4.0, 17.5, 30.0, 10.8; HealthBench Consensus — 88.7, 91.5, 92.8, 91.1, 91.8, 90.0, 82.6.
- **Table 2 — MMMLU averages**: 120b low/medium/high 74.1 / 79.3 / 81.3; 20b 67.0 / 73.5 / 75.7; o3-mini 80.7, o4-mini 85.2, o3 88.8 (all high). Lowest languages: Yoruba (120b high 62.4) and Swahili (72.3).
- **Hallucination (Table 9)**: SimpleQA accuracy / hallucination rate — 120b 0.168 / 0.782; 20b 0.067 / 0.914; o4-mini 0.234 / 0.750. PersonQA — 120b 0.298 / 0.491; 20b 0.155 / 0.532; o4-mini 0.356 / 0.361.
- **Instruction hierarchy (Tables 7–8)**: system-prompt extraction 0.832 / 0.881 / 0.993 (120b / 20b / o4-mini); prompt-injection hijacking 0.780 / 0.639 / 0.917; gpt-oss "generally underperform OpenAI o4-mini" here.
- **Disallowed content (Tables 4–5)**, **jailbreaks (Table 6, StrongReject)**, **BBQ (Table 10: ambiguous 0.87 / 0.79 / 0.82; disambiguated 0.90 / 0.89 / 0.95)** — roughly on par with o4-mini.
- **Preparedness (§5)**: bio evals vs. DeepSeek R1-0528, Qwen 3 Thinking and Kimi K2 ("no single open model consistently outperforms the others in this domain"); cyber range: "No model is able to solve any scenario unaided or with hints"; 22 external recommendations, 11 acted on "including 9 of 12 items that reviewers labeled as high urgency".
- **Harmony example (Figures 17–18)**: a system message with `reasoning: low`, a developer message defining a `get_current_weather` function, a user asking "What is the weather like in SF?", and a response whose `analysis` channel says "Need to use function get_weather." followed by a `commentary` call `to=functions.get_weather` with `{"location":"San_Francisco"}`. Full transcription in *Raw / preserved excerpts*.

## Inconsistencies / open questions
- [open question] **How the effort levels are actually trained is not disclosed.** §2.5.2 is three sentences: levels exist, they are set in the system prompt, higher → longer average CoT. No data recipe, no length reward/penalty, no per-level target budget, no statement on whether levels were trained jointly in RL or via SFT. Any slide that says *how* OpenAI trains effort goes beyond this source — would be settled only by another source (e.g. OpenAI's harmony/open-source guide or a later paper); compare the explicit mechanism in `qwen-2025-qwen3-technical-report.pdf.md` (thinking-mode fusion + thinking budget).
- [verified] **Keyword casing differs between text and example**: §2.5.2 says keywords "such as "Reasoning: low"", while the Figure 17 example system message shows `reasoning: low` (lowercase) — checked by viewing the extracted image `fig-17-p030.png`. Whether the model is case-sensitive is not stated.
- [verified] **Figures 17–18 are cited as "Table 17 and 18"**: §2.5.1 says "Table 17 and 18 in the Appendix show an example model input and output", §2.3 says "harmony chat format described in Table 18", §2.5.3 says "An example can be found in Table 18"; the appendix labels them "Figure 17" and "Figure 18" — checked against the page-30/31 captions.
- [verified] **Figure 3 plots the "with tools" numbers without saying so**: its AIME 2025 points (120b ≈ 73 / 91.5 / 98; 20b ≈ 57.5 / 90.4 / 98.7) and GPQA points (120b ≈ 68 / 73.5 / 81; 20b ≈ 58 / 67 / 74) match Table 3's "(with tools)" rows (72.9 / 91.6 / 97.9; 57.5 / 90.4 / 98.7; 68.1 / 73.5 / 80.9; 58.0 / 67.1 / 74.2), not the "(no tools)" rows — checked by comparing the crop to the table.
- [verified] **Effort is not monotonically better everywhere** (Table 3): gpt-oss-20b Tau-Bench Airline high 38.0 < medium 42.6; 20b HealthBench Hard high 10.8 < medium 12.9; HealthBench Consensus falls with effort for both sizes (120b 90.8 → 89.9; 20b 84.9 → 83.0 → 82.6); 20b Codeforces with tools at low (1251) is below no tools at low (1366). The text's "smooth test-time scaling" is shown only for AIME and GPQA.
- [verified] **Function name mismatch in the appendix example**: Figure 17 declares `get_current_weather`, but the Figure 18 response calls `functions.get_weather` — checked by viewing both extracted images. Do not reuse the pair as a correct tool-call example without fixing the name.
- [open question] "log-linear returns on most tasks" — only two tasks are plotted (Figure 3); the claim for "most tasks" is not backed by a plot in the card. Table 3 has only three points per task, not token lengths.
- [open question] Figure 3 x-axis is "average CoT + Answer length", not a user-set budget: the level controls length only on average; the card gives no distribution or cap per level.
- [open question] Reasoning traces "from past assistant turns should be removed" in multi-turn use — the card asserts it but doesn't say why (training distribution presumably); settled by the harmony guide.
- [open question] Personality claim "similar to models served in our first-party products like ChatGPT" because of "similar RL techniques" — asserted, no evidence.

## Images / diagrams
Raster extraction (`pdfimages -png`) yielded 26 files on PDF pages 20–31: 14 RGB figures plus 12 `smask` alpha channels (soft masks belonging to 12 of those figures, not separate images). The alpha masks were discarded; the RGB bytes render correctly on white. No raster was below the 300 × 300 px deletion threshold in both dimensions (Figure 18 is 1070 × 144 — wide, kept). Figures 1–4 are vector plots and were cropped with `cropfigs.py` (PDF pages 6, 7, 8, 10). Files are named `fig-NN-pPPP.png` where NN is the paper's figure number and PPP the PDF page.

### `openai-2025-gpt-oss-model-card.pdf/images/fig-01-p006.png`
- Provenance: Figure 1 ("Main capabilities evaluations") of `articles/openai-2025-gpt-oss-model-card.pdf`, PDF page 6, vector figure; cropped with `cropfigs.py` (figure + labels + caption), 1039 × 773 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-02-p007.png`
- Provenance: Figure 2 ("Coding and tool use results"), PDF page 7, vector figure; cropped with `cropfigs.py`, 1036 × 521 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-03-p008.png`
- Provenance: Figure 3 (accuracy vs. CoT + Answer length across low/medium/high reasoning, AIME 2025 and GPQA Diamond), PDF page 8, vector figure; cropped with `cropfigs.py`, 1039 × 563 px. **Key figure for the reasoning-effort topic.**
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-04-p010.png`
- Provenance: Figure 4 ("Health performance"), PDF page 10, vector figure; cropped with `cropfigs.py`, 1038 × 488 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-05-p020.png`
- Provenance: Figure 5 (long-form biorisk, "Autograded Gryphon Free Response" by biothreat stage), PDF page 20, embedded raster (`pdfimages -png`, object 520), 7197 × 1519 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-06-p021.png`
- Provenance: Figure 6 (Multimodal Troubleshooting Virology), PDF page 21, embedded raster (object 521), 5946 × 1898 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-07-p021.png`
- Provenance: Figure 7 (ProtocolQA Open-Ended), PDF page 21, embedded raster (object 522), 5947 × 1898 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-08-p022.png`
- Provenance: Figure 8 (Tacit Knowledge and Troubleshooting), PDF page 22, embedded raster (object 523), 5946 × 1898 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-09-p023.png`
- Provenance: Figure 9 (TroubleshootingBench), PDF page 23, embedded raster (object 524), 5947 × 1898 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-10-p025.png`
- Provenance: Figure 10 (Collegiate CTF challenges), PDF page 25, embedded raster (object 525), 5147 × 1898 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-11-p025.png`
- Provenance: Figure 11 (Professional CTF challenges, incl. cybermax model), PDF page 25, embedded raster (object 526), 5147 × 1898 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-12-p027.png`
- Provenance: Figure 12 (Cyber range scenarios), PDF page 27, embedded raster (object 527), 5108 × 1821 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-13-p028.png`
- Provenance: Figure 13 (SWE-bench Verified example task flow), PDF page 28, embedded raster (object 528), 3404 × 800 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-14-p028.png`
- Provenance: Figure 14 (SWE-bench Verified results), PDF page 28, embedded raster (object 529), 5947 × 1977 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-15-p029.png`
- Provenance: Figure 15 (OpenAI PRs), PDF page 29, embedded raster (object 530), 3947 × 1977 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-16-p030.png`
- Provenance: Figure 16 (PaperBench), PDF page 30, embedded raster (object 531), 3947 × 1977 px.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-17-p030.png`
- Provenance: Figure 17 (Appendix 1: "Model input in the harmony format specifying a system message with reasoning set to low, a developer message specifying one available function tool for the model, and a user message asking for the weather in SF."), PDF page 30, embedded raster (object 532, no alpha mask), 1078 × 656 px. **Key figure for the reasoning-effort topic** — the only place the card shows where the effort keyword sits. Its text is transcribed in *Raw / preserved excerpts* (Phase 1, so the prompt text is not lost); the prose fields below remain for Phase 2.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `openai-2025-gpt-oss-model-card.pdf/images/fig-18-p031.png`
- Provenance: Figure 18 (Appendix 1: "Example model response in the harmony format with the CoT and the model making a tool call."), PDF page 31, embedded raster (object 533, no alpha mask), 1070 × 144 px (kept: width ≥ 300). Text transcribed in *Raw / preserved excerpts*.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

## Raw / preserved excerpts

### §1 Introduction (opening)
> We introduce gpt-oss-120b and gpt-oss-20b, two open-weight reasoning models available under the Apache 2.0 license and our gpt-oss usage policy. Developed with feedback from the open-source community, these text-only models are compatible with our Responses API and are designed to be used within agentic workflows with strong instruction following, tool use like web search and Python code execution, and reasoning capabilities—including the ability to adjust the reasoning effort for tasks that don't require complex reasoning. The models are customizable, provide full chain-of-thought (CoT), and support Structured Outputs.
>
> Safety is foundational to our approach to open models. They present a different risk profile than proprietary models: Once they are released, determined attackers could fine-tune them to bypass safety refusals or directly optimize for harm without the possibility for OpenAI to implement additional mitigations or to revoke access.

### §2.4 Pretraining
> Data: We train the models on a text-only dataset with trillions of tokens, with a focus on STEM, coding, and general knowledge. To improve the safety of the model, we filtered the data for harmful content in pre-training, especially around hazardous biosecurity knowledge, by reusing the CBRN pre-training filters from GPT-4o [18]. Our model has a knowledge cutoff of June 2024.
>
> Training: The gpt-oss models trained on NVIDIA H100 GPUs using the PyTorch framework [19] with expert-optimized Triton [20] kernels. The training run for gpt-oss-120b required 2.1 million H100-hours to complete, with gpt-oss-20b needing almost 10x fewer. Both models leverage the Flash Attention [21] algorithms to reduce the memory requirements and accelerate training.

### §2.5 Post-Training for Reasoning and Tool Use
> After pre-training, we post-train the models using similar CoT RL techniques as OpenAI o3. This procedure teaches the models how to reason and solve problems using CoT and teaches the model how to use tools. Because of the similar RL techniques, these models have a personality similar to models served in our first-party products like ChatGPT. Our training dataset consists of a wide range of problems from coding, math, science, and more.

### §2.5.1 Harmony Chat Format
> For the models' training, we use a custom chat format known as the harmony chat format. This format provides special tokens to delineate message boundaries and uses keyword arguments (e.g., User and Assistant) to indicate message authors and recipients. We use the same System and Developer message roles that are present in the OpenAI API models. Using these roles, the models follow a role-based information hierarchy to resolve instruction conflicts: System > Developer > User > Assistant > Tool.
>
> The format also introduces "channels" to indicate the intended visibility of each message, e.g., analysis for CoT tokens, commentary for function tool calling and final for answers shown to users. This format enables gpt-oss to provide advanced agentic features including interleaving tool calls within the CoT or providing preambles that outline longer action plans to the user. Our accompanying open-source implementation and guide provides full details on the proper usage of this format–it is critical to deploy our gpt-oss models properly to achieve their best capabilities. For example, in multi-turn conversations the reasoning traces from past assistant turns should be removed. Table 17 and 18 in the Appendix show an example model input and output in the harmony chat format.

### §2.5.2 Variable Effort Reasoning Training (complete section)
> We train the models to support three reasoning levels: low, medium, and high. These levels are configured in the system prompt by inserting keywords such as "Reasoning: low". Increasing the reasoning level will cause the model's average CoT length to increase.

### §2.5.3 Agentic Tool Use (complete section)
> During post-training, we also teach the models to use different agentic tools:
> • A browsing tool, that allows the model to call search and open functions to interact with the web. This aids factuality and allows the models to fetch info beyond their knowledge cutoff.
> • A python tool, which allows the model to run code in a stateful Jupyter notebook environment.
> • Arbitrary developer functions, where one can specify function schemas in a Developer message similar to the OpenAI API. The definition of function is done within our harmony format. An example can be found in Table 18. The model can interleave CoT, function calls, function responses, intermediate messages that are shown to users, and final answers.
>
> The models have been trained to support running with and without these tools by specifying so in the system prompt. For each tool, we have provided basic reference harnesses that support the general core functionality. Our open-source implementation provides further details.

### §2.6 Evaluation (opening)
> We evaluate gpt-oss on canonical reasoning, coding, and tool use benchmarks. For all datasets, we report basic pass@1 results for high reasoning mode using the model's default system prompt. We compare to OpenAI o3, o3-mini, and o4-mini.

### §2.6.1 Reasoning, Factuality and Tool Use (complete section)
> Main Capabilities: Figure 1 shows our main results on four canonical knowledge and reasoning tasks: AIME, GPQA, HLE, and MMLU. The gpt-oss models are strong at math in particular, which we believe is because they can use very long CoTs effectively, e.g., our gpt-oss-20b use over 20k CoT tokens per problem on average for AIME. On more knowledge-related tasks such as GPQA, the gpt-oss-20b model lags behind due to its smaller size.
>
> Agentic Tasks: The gpt-oss models have particularly strong performance on coding and tool-use tasks. Figure 2 shows our performance on Codeforces, Swe-Bench and τ-bench retail. Similarly to the main capabilities evals, we find gpt-oss-120b comes close to OpenAI's o4-mini in performance.
>
> Test-time scaling: Our models demonstrate smooth test-time scaling. In Figure 3, we sweep over the different reasoning modes of the model (low, medium, high) and plot accuracy versus average CoT+Answer length. We generally see log-linear returns on most tasks, where longer CoTs provide higher accuracy at a relatively large increase in final response latency and cost. We recommend that users pick a model size and corresponding reasoning level that balances these tradeoffs for their use case.

### Figure 3 caption
> Figure 3: We evaluate AIME and GPQA using the three different reasoning modes (low, medium, high) and plot accuracy against the average CoT + Answer length. We find that there is smooth test-time scaling of accuracy when increasing the reasoning level.

### Figure 1 caption
> Figure 1: Main capabilities evaluations. We compare the gpt-oss models at reasoning level high to OpenAI's o3, o3-mini, and o4-mini on canonical benchmarks. gpt-oss-120b surpasses OpenAI o3-mini and approaches OpenAI o4-mini accuracy. The smaller gpt-oss-20b model is also surprisingly competitive, despite being 6 times smaller than gpt-oss-120b.
> *Note: o3-mini was evaluated on AIME without tools, see Table 3 for the gpt-oss models on AIME without tools

### Figure 17 — harmony-format model input (transcribed from the extracted image `fig-17-p030.png`; in the PDF this text exists only as an image; red special tokens rendered here as plain text)
```
<|start|>system<|message|>You are ChatGPT, a large language model trained by OpenAI.
Knowledge cutoff: 2024-06
Current date: 2025-06-28

reasoning: low

# Valid channels: analysis, commentary, final. Channel must be included for every
    message.
Calls to these tools must go to the commentary channel: 'functions'.<|end|>
<|start|>developer<|message|># Instructions

Use a friendly tone.

# Tools

## functions

namespace functions {

// Gets the current weather in the provided location.
type get_current_weather = (_: {
// The city and state, e.g. San Francisco, CA
location: string,
format?: "celsius" | "fahrenheit", // default: celsius
}) => any;

} // namespace functions<|end|>
<|start|>user<|message|>What is the weather like in SF?<|end|>
<|start|>assistant
```
Caption: "Figure 17: Model input in the harmony format specifying a system message with reasoning set to low, a developer message specifying one available function tool for the model, and a user message asking for the weather in SF."

### Figure 18 — harmony-format model response (transcribed from `fig-18-p031.png`)
```
<|channel|>analysis<|message|>Need to use function get_weather.<|end|>
<|start|>assistant<|channel|>commentary to=functions.get_weather <|constrain|>json<|
    message|>{"location":"San_Francisco"}<|call|>
```
Caption: "Figure 18: Example model response in the harmony format with the CoT and the model making a tool call."
(Note: the function is declared as `get_current_weather` in Figure 17 but called as `functions.get_weather` in Figure 18 — as printed in the source.)

### §3 Safety testing and mitigation approach (opening)
> During post-training, we use deliberative alignment[29] to teach the models to refuse on a wide range of content (e.g., illicit advice), be robust to jailbreaks, and adhere to the instruction hierarchy[30].
>
> In line with our longstanding views on open model weights, we believe that testing conditions for open weight models "would ideally reflect the range of ways that downstream actors can modify the model. One of the most useful properties of open models is that downstream actors can modify the models to expand their initial capabilities and tailor them to the developer's specific applications. However, this also means that malicious parties could potentially enhance the model's harmful capabilities. Rigorously assessing an open-weights release's risks should thus include testing for a reasonable range of ways a malicious party could feasibly modify the model, including by fine-tuning."

### §4.3 Instruction Hierarchy (training description)
> To mitigate this issue, we taught the model to adhere to an Instruction Hierarchy. At a high level, we post-trained the model with our harmony prompt format that uses several roles including: system messages, developer messages, and user messages. We collected examples of these different roles of messages conflicting with each other, and supervised gpt-oss to follow the instructions in the system message over developer messages, and instructions in developer messages over user messages. This provides both model inference providers, and developers using the model to control guardrails at their respective levels.

### §4.4 Hallucinated chains of thought (complete section)
> In our recent research, we found that monitoring a reasoning model's chain of thought can be helpful for detecting misbehavior. We further found that models could learn to hide their thinking while still misbehaving if their CoTs were directly pressured against having "bad thoughts." More recently, we joined a position paper with a number of other labs arguing that frontier developers should "consider the impact of development decisions on CoT monitorability."
>
> In accord with these concerns, we decided not to put any direct optimization pressure on the CoT for either of our two open-weight models. We hope that this gives developers the opportunity to implement CoT monitoring systems in their projects and enables the research community to further study CoT monitorability.
>
> Because these chains of thought are not restricted, they can contain hallucinated content, including language that does not reflect OpenAI's standard safety policies. Developers should not directly show chains of thought to users of their applications, without further filtering, moderation, or summarization of this type of content.

### §4.5 Hallucinations (conclusion)
> gpt-oss-120b and gpt-oss-20b underperform OpenAI o4-mini on both our SimpleQA and PersonQA evaluations. This is expected, as smaller models have less world knowledge than larger frontier models and tend to hallucinate more. Additionally, browsing or gathering external information tends to reduce instances of hallucination as models are able to look up information they do not have internal knowledge of.

### §5.1 Adversarial Training (method)
> In our adversarial training, we simulate an adversary who is technical, has access to strong post-training infrastructure and ML knowledge, can collect in-domain data for harmful capabilities, and has a large budget of compute. There is a large design space of technical approaches this adversary could try. We focus on incremental reinforcement learning, which we believe is the most apt technical approach. We use our internal OpenAI o-series RL training stack, which adds new capabilities while preserving the model's reasoning behavior. During training and evaluation time, we use the highest reasoning setting on gpt-oss.
>
> Our approach, which is further detailed in a research paper, combined two elements:
> • Helpful-only training: We performed an additional stage of reinforcement learning to reward answers that comply with unsafe prompts. We have found this approach can be highly effective. This process has also been used to create helpful-only versions of other recent models, most recently ChatGPT agent.
> • Maximizing capabilities relevant to Preparedness benchmarks in the biological and cyber domains: For our adversarially trained biological model, we incrementally trained gpt-oss-120b end-to-end for web browsing, and trained it incrementally with in-domain human expert data relevant to biorisk (for which previous OpenAI models have been the most capable). In the case of our cyber model, the domain-specific data consisted of cybersecurity capture the flag challenge environments.

### §5.2.1 comparison with other open models
> To investigate this question, we compared gpt-oss-120b to other released open source models. At first, we primarily considered DeepSeek R1-0528. Partway through our process, the Qwen 3 Thinking and Kimi K2 models were released, and we added these to our comparison set. These evaluations confirmed that Qwen 3 Thinking and Kimi K2 have advanced to a level such that gpt-oss-120b does not significantly advance the state of the art on biosecurity-relevant evaluations. While gpt-oss-120b achieves the highest performance on select biosecurity evaluations, no single open model consistently outperforms the others in this domain.
