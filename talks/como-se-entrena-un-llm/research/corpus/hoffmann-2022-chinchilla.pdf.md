---
source_file: hoffmann-2022-chinchilla.pdf
source_type: article
ingested_at: 2026-09-25
---

# Training Compute-Optimal Large Language Models

## Provenance
- Original location: articles/hoffmann-2022-chinchilla.pdf
- Format: pdf (36 pages)
- Author / source (if known): Jordan Hoffmann★, Sebastian Borgeaud★, Arthur Mensch★, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals and Laurent Sifre★ (★ equal contributions). DeepMind (corresponding authors: {jordanhoffmann|sborgeaud|amensch|sifre}@deepmind.com). arXiv preprint, cs.CL. Commonly known as the "Chinchilla" paper.
- Date of original (if known): 29 Mar 2022 (arXiv:2203.15556v1, as printed; model card gives "Model Date: March 2022"). The page footer reads "© 2023 DeepMind. All rights reserved".
- arXiv: 2203.15556v1 [cs.CL]
- Extraction: `pdftotext` (poppler, UTF-8, reading order). Math, tables and multi-column layout are flattened; equations and table cells may be garbled in the verbatim text below — consult the page renders in the companion folder for exact figures/tables.

## Key claims
- Headline (abstract): "current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant."
- Core rule: "for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled."
- Evidence base: "over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens."
- Disagreement with Kaplan et al. (2020): Kaplan suggests that for a 10× compute increase "the size of the model should increase 5.5× while the number of training tokens should only increase 1.8×"; Hoffmann et al. find "model size and the number of training tokens should be scaled in equal proportions." Both agree large models "should not be trained to their lowest possible loss to be compute optimal."
- Why Kaplan differed: Kaplan used "a fixed number of training tokens and learning rate schedule for all models," so intermediate losses overestimate the loss of properly scheduled shorter runs, "underestimating the effectiveness of training models on less data than 130B tokens"; and Kaplan's runs were mostly small ("many being less than 100M parameters"), whereas most of Hoffmann's runs exceed 500M and there is "slight curvature in the FLOP-loss frontier."
- Three independent approaches agree (Table 2): Approach 1 (minimum over training curves) a = 0.50, b = 0.50; Approach 2 (IsoFLOP profiles) a = 0.49, b = 0.51; Approach 3 (parametric loss fit) a = 0.46, b = 0.54 — vs. Kaplan a = 0.73, b = 0.27 (N_opt ∝ C^a, D_opt ∝ C^b).
- Results replicate on C4 (a = 0.50, b = 0.50) and GitHub code (a = 0.53, b = 0.47): "our results are independent of the dataset as long as one does not train for more than one epoch."
- The learning-rate cosine cycle should match the number of training tokens; overshooting by more than 25% "leads to clear drops in performance."
- Most large models were trained on ~300B tokens (Table 1: GPT-3 175B/300B, Jurassic 178B/300B, Gopher 280B/300B, MT-NLG 530B/270B, LaMDA 137B/168B), "in line with the approach of predominantly increasing model size when increasing compute."
- For Gopher's budget (5.76 × 10^23 FLOPs) the optimal model should be "4 times smaller, while being training on 4 times more tokens" — optimal size "somewhere between 40 and 70 billion parameters."
- Chinchilla: 70B parameters, 1.4 trillion tokens, same compute as Gopher; "uniformly and significantly outperforms Gopher (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks."
- Smaller model → cheaper fine-tuning and inference: "The energy cost of a large language model is amortized through its usage for inference an[d] fine-tuning."
- Projections (Table 3, Approach 1): 1B params → 20.2B tokens; 10B → 205.1B; 67B → 1.5T; 175B → 3.7T; 280B → 5.9T; 520B → 11.0T; 1T → 21.2T; 10T → 216.2T tokens. Text: a 175B model "should be trained with a compute budget of 4.41 × 10^24 FLOPs and on over 4.2 trillion tokens"; a 280B model optimal at ~10^25 FLOPs with 6.8T tokens; a 1T-parameter model is unlikely optimal unless compute is ~10^26 FLOPs ("over 250× the compute used to train Gopher").
- Data becomes the bottleneck: "the amount of training data that is projected to be needed is far beyond what is currently used to train large models, and underscores the importance of dataset collection"; "larger, high quality datasets will play a key role in any further scaling of language models."
- "Speculatively, we expect that scaling to larger and larger datasets is only beneficial when the data is high-quality. This calls for responsibly collecting larger datasets with a high focus on dataset quality."
- Ethical/privacy: "training for trillions of tokens introduces many ethical and privacy concerns. Large datasets scraped from the web will contain toxic language, biases, and private information."
- Retrieval (RETRO) "effectively increases the number of data tokens seen during training (by a factor of ∼ 10 ...)" — "performance of language models may be more dependant on the size of the training data than previously thought."
- MMLU: Chinchilla 67.6% average 5-shot (Gopher 60.0%, GPT-3 43.9%), exceeding the June 2023 expert forecast of 63.4%; >90% on 4 individual tasks.
- TruthfulQA: 43.6% 0-shot vs Gopher 29.5% — "better modelling of the pre-training data alone can lead to substantial improvements on this benchmark."
- Toxicity is "largely independent of the model quality (measured in language modelling loss)"; "better models of the training dataset are not necessarily more toxic."
- Expected generality: "we expect that there is a similar trade-off between model size and the amount of data in other modalities."
- Chinchilla model card: trained on English data; not released publicly ("We will not make this model available publicly").

## Definitions and terminology
- **Compute-optimal allocation** — N_opt(C), D_opt(C) = argmin over N, D with FLOPs(N, D) = C of L(N, D) (Eq. 1).
- **FLOPs(N, D) ≈ 6ND** — the Kaplan approximation used for the efficient frontier; Appendix F counts all FLOPs including embeddings and finds the ratio of their count to 6ND between 0.99 and 1.10 (Table A4).
- **Final pre-training loss L(N, D)** — analyzed on smoothed training loss, "an unbiased estimate of the test loss, as we are in the infinite data regime (the number of training tokens is less than the number of tokens in the entire corpus)."
- **Approach 1 (training curve envelope)** — fixed model sizes (70M to >10B), 4 cosine cycle lengths each (horizon range 16×); take minimal loss per FLOP at 1500 log-spaced FLOP values; fit N_opt ∝ C^a, D_opt ∝ C^b.
- **Approach 2 (IsoFLOP profiles)** — vary model size for 9 fixed FLOP budgets (6 × 10^18 to 3 × 10^21), fit a parabola to each loss valley.
- **Approach 3 (parametric loss)** — L̂(N, D) = E + A/N^α + B/D^β, fitted with Huber loss (δ = 10^−3) on log loss via L-BFGS; fit: E = 1.69, A = 406.4, B = 410.7, α = 0.34, β = 0.28. Efficient frontier N_opt = G(C/6)^a, D_opt = G^−1(C/6)^b, G = (αA/βB)^(1/(α+β)), a = β/(α+β), b = α/(α+β).
- **Loss decomposition** — L(N, D) = L(f*) + [L(f_N) − L(f*)] + [L(f̄_N,D) − L(f_N)]: the Bayes risk ("entropy of natural text"), a functional approximation term (depends on N), and a stochastic approximation term (single-epoch optimization on D tokens).
- **Bayes classifier f*** — minimizer of expected cross-entropy over all predictors; **f_N** — best transformer of size N; **f̄_N,D** — "single-epoch empirical-risk minimizer."
- **Efficient frontier** — the curve through each iso-loss contour at the point with fewest FLOPs (a line in log-log space).
- **Chinchilla** — 70B-parameter compute-optimal model: 80 layers, 64 heads, key/value size 128, d_model 8,192, max LR 1 × 10^−4, batch 1.5M → 3M tokens (Gopher 280B: 80 layers, 128 heads, d_model 16,384, max LR 4 × 10^−5, batch 3M → 6M). Feed-forward size 4 × d_model.
- **MassiveText** — Gopher/Chinchilla training dataset: MassiveWeb, Books, C4, News, GitHub, Wikipedia.
- **Undertrained / over-sized** — models trained on fewer tokens than compute-optimal for their size.
- **Cosine cycle length** — learning-rate schedule horizon; optimal when matched to training steps, decaying 10×.
- **Bits-per-byte (bpb)** — language-modelling metric on The Pile.
- **Gotcha examples (Winogender)** — cases where the correct pronoun resolution contradicts gender stereotypes.

## Evidence and examples
- **Figure 1** — overlaid predictions of the three approaches plus Kaplan projections: "current large models should be substantially smaller and therefore trained much longer than is currently done."
- **Table 1** — current LLMs and training tokens: LaMDA 137B/168B; GPT-3 175B/300B; Jurassic 178B/300B; Gopher 280B/300B; MT-NLG 530B/270B; Chinchilla 70B/1.4T.
- **Figure 2** — training curve envelope for models 70M–10B, four cosine cycles each; green projections for Gopher FLOPs (5.76 × 10^23): ~67B parameters, ~1.5T tokens.
- **Figure 3** — IsoFLOP curves show "a clear valley in loss"; projections ~63B parameters, 1.4T tokens for Gopher's budget.
- **Figure 4** — parametric fit contours; efficient frontier projects 40B parameters for Gopher's budget.
- **Table 2** — exponents with bootstrap 10th/90th percentiles: 0.50 (0.488, 0.502) / 0.50 (0.501, 0.512); 0.49 (0.462, 0.534) / 0.51 (0.483, 0.529); 0.46 (0.454, 0.455) / 0.54 (0.542, 0.543); Kaplan 0.73 / 0.27.
- **Table 3** — FLOPs and tokens for compute-optimal models (Approach 1), e.g., 400M: 1.92e19 FLOPs, 8.0B tokens; 67B: 5.76e23 (1 Gopher unit), 1.5T; 175B: 3.85e24, 3.7T; 280B: 9.90e24, 5.9T; 520B: 3.43e25, 11.0T; 1T: 1.27e26 (221.3 Gopher units), 21.2T; 10T: 1.30e28, 216.2T.
- **Table A3** — Approach 2 and 3 projections; Approach 3 gives much larger token counts (e.g., 175B → 12.0T tokens; 1T → 94.1T; 10T → 1425.5T).
- **Table A1 (MassiveText makeup)** — MassiveWeb 1.9 TB, 604M docs, 45% sampling (Gopher 48%), 1.24 epochs in 1.4T tokens; Books 2.1 TB, 4M docs, 30% (27%), 0.75 epochs; C4 0.75 TB, 361M docs, 10%, 0.77; News 2.7 TB, 1.1B docs, 10%, 0.21; GitHub 3.1 TB, 142M docs, 4% (3%), 0.13; Wikipedia 0.001 TB, 6M docs, 1% (2%), 3.40 epochs.
- **Training changes vs. Gopher** — AdamW instead of Adam; SentencePiece tokenizer without NFKC normalisation (94.15% of tokens shared with Gopher's; vocab 32,000), helping "with the representation of mathematics and chemistry"; bfloat16 forward/backward with a float32 copy of weights in the optimiser state; TPUv3/TPUv4, JAX, Haiku. AdamW "only passes the training performance of a model trained with Adam around 80% of the way through the cosine cycle."
- **Figure 5 / Table A5 (The Pile)** — Chinchilla beats Gopher on all subsets in bits-per-byte (e.g., pile_cc 0.667 vs 0.691; github 0.337 vs 0.377); Jurassic-1 beats Chinchilla only on dm_mathematics and ubuntu_irc.
- **Wikitext103** — perplexity 7.16 (Chinchilla) vs 7.75 (Gopher), with a caveat about train/test leakage.
- **Table 6 (MMLU 5-shot)** — Random 25.0%; average human rater 34.5%; GPT-3 43.9%; Gopher 60.0%; Chinchilla 67.6%; average human expert 89.8%; forecasts June 2022 57.1%, June 2023 63.4%. Figure 6: better on 51/57 tasks, same on 2, worse on 4 (college_mathematics, econometrics, moral_scenarios, formal_logic).
- **Table 7 (reading comprehension)** — LAMBADA zero-shot 77.4 (Gopher 74.5, GPT-3 76.2, MT-NLG 76.6); RACE-m 86.8 (75.1); RACE-h 82.3 (71.6).
- **BIG-bench (Figure 7, Table A7)** — 65.1% vs 54.4% average (+10.7%); worse on only 4 of 62 tasks (crash_blossom, dark_humor_detection, mathematical_induction, logical_args).
- **Table 8 (common sense, zero-shot)** — HellaSwag 80.8%, PIQA 81.8%, Winogrande 74.9%, SIQA 51.3%, BoolQ 83.7%; beats Gopher and GPT-3 on all, MT-NLG on all but one.
- **TruthfulQA** — 43.6% / 58.5% / 66.7% (0/5/10-shot) vs Gopher 29.5% 0-shot and 43.7% 10-shot.
- **Table 9 (closed-book QA)** — Natural Questions 16.6% / 31.5% / 35.5% (0/5/64-shot) vs Gopher 10.1% / 24.5% / 28.2%; TriviaQA unfiltered 67.0% / 73.2% / 72.3%; filtered 55.4% / 64.1% / 64.6%, "lags behind the open book SOTA ... by only 7.9%."
- **Table 10 (Winogender)** — All 78.3% vs 71.4%; male 71.2 vs 68.0; female 79.6 vs 71.3; neutral 84.2 vs 75.0; female gotcha 76.7 vs 66.7 (+10%). Example prompt: "The librarian helped the child pick out a book because {pronoun} liked to encourage reading." completed as "'{Pronoun}' refers to the" [librarian/child].
- **Toxicity** — 25,000 unprompted samples, PerspectiveAPI: mean (median) 0.081 (0.064) Gopher vs 0.087 (0.066) Chinchilla; 95th percentile 0.230 vs 0.238.
- **Figure A1** — cosine cycle 1×, 1.1×, 1.25×, 1.5×, 2×, 5× the target steps; too-long cycles impair performance.
- **Figure A4 (head-to-head at 10^21 FLOPs)** — Kaplan predicts 4.68B optimal, Approach 1 predicts 2.86B; trained 4.74B vs 2.80B with same depth-to-width ratio; the smaller (Approach 1) model wins.
- **Figure A5 / Appendix E** — curvature in the FLOP-loss frontier: fits on the first, middle and last third of points differ; "even smaller models may be optimal for large FLOP budgets."
- **Figures A6–A7** — AdamW and a high-precision weight copy outperform Adam (680M, 417M and 1.4B models).
- **Table A9** — list of all trained models from 44M to 16,183M parameters.
- **Model card (Table A8)** — trained on English data; unequal performance on some dialects (e.g., African American English, per Rae et al.); associates "dietician" and "receptionist" with women and "carpenter" and "sheriff" with men; authors chose not to filter toxic content because filtering "can introduce new biases"; "it is likely that personal information is also in the dataset."

## Inconsistencies / open questions
- [verified] MMLU numbers differ between abstract and body: abstract "67.5% on the MMLU benchmark, greater than a 7% improvement over Gopher"; Section 4.2.2 and Table 6 "67.6% (improving upon Gopher by 7.6%)" — checked abstract vs. Table 6.
- [verified] Token range differs: abstract "5 to 500 billion tokens"; Section 1 "trained on 5B to over 400B tokens"; model range "70 million" (abstract) vs "under 70M" (Section 1).
- [verified] Text vs. Table 3 disagree for a 175B model: text says "4.41 × 10^24 FLOPs and on over 4.2 trillion tokens", Table 3 (Approach 1) gives 3.85e24 FLOPs and 3.7T tokens, Table A3 (Approach 2) 4.54e24 and 4.3T. For 280B, text says ~10^25 FLOPs and 6.8T tokens vs Table 3's 9.90e24 and 5.9T and Table A3's 1.18e25 and 7.1T.
- [verified] Table A3 (Approach 3) lists 175B at 1.26e+24 FLOPs, smaller than the 67B entry (1.71e+24) — non-monotonic, likely a typo (e.g., for 1.26e+25).
- [verified] Table 2 Approach 3 intervals do not contain the point estimate: "0.46 (0.454, 0.455)" and "0.54 (0.542, 0.543)".
- [verified] GPT-3 is described as having "170 billion parameters" in Section 5, but 175B elsewhere; Jurassic-1 is "(170B)" in Table A5 but 178B elsewhere.
- [verified] Gopher's training compute is 5.76 × 10^23 in the main text but "6.3 × 10^23" under the paper's more accurate FLOP count (Appendix F) — acknowledged by authors.
- [verified] Epoch statements are in tension: footnote 2 says "we are in the infinite data regime (the number of training tokens is less than the number of tokens in the entire corpus)" and Section 5 says runs were "trained on less than an epoch of data," yet Table A1 says "both the MassiveWeb and Wikipedia subsets are both used for more than one epoch" (1.24 and 3.40 epochs in 1.4T tokens).
- [verified] Toxicity: Section 5 says Chinchilla "seems less affected than Gopher," but Section 4.2.7 reports slightly higher toxicity scores for Chinchilla (mean 0.087 vs 0.081; 95th percentile 0.238 vs 0.230) and calls the difference "negligible."
- [verified] Parametric fit text says "we assume that the second term only depends on D", but the D-dependent term is the third term — typo in Appendix D.2.
- [verified] Author-stated limitations: "we only have two comparable training runs at large scale (Chinchilla and Gopher), and we do not have additional tests at intermediate scales"; assumes a power-law frontier while observing "some concavity in log N_opt at high compute budgets ... we may still be overestimating the optimal size of large models"; multi-epoch regime not studied; Chinchilla trained only once ("we did not train Chinchilla multiple times"); train/test leakage may inflate language-modelling results since Chinchilla saw 4× more data; bias/toxicity evaluations "are not comprehensive"; no intersectional bias analysis.
- [verified] Chinchilla is 70B and 1.4T tokens vs Gopher 280B and 300B tokens — described as "4× more more data" (abstract, typo) though 1.4T/300B ≈ 4.7×.
- [verified] The page footer reads "© 2023 DeepMind" on an arXiv v1 dated 29 Mar 2022.
- [verified] Extraction problems: equations (1)–(11) are garbled (e.g., "𝑁 11/2" in D.2 for an N^−1/2 rate); Figure 2/3/A2 axis labels jumbled; Table A5 Jurassic-1 column has fewer values (16) than rows (19), so values cannot be aligned to subsets reliably; Table A6/A7 two-column layouts flattened.
- [open question] The Chinchilla ratio (~20 tokens per parameter, 70B/1.4T) is widely used as a rule of thumb, but the paper only states equal scaling and gives Table 3; whether later models follow it (vs. "overtraining" for inference cost) would be settled by later training reports (the Villalobos record in this corpus discusses Llama 3 at ~214 tokens/parameter).
- [open question] Whether the recommended data volumes (e.g., 21.2T tokens for a 1T model, 216.2T for 10T) are available at the required quality — the paper flags dataset collection as critical but does not estimate the stock; cross-check with the Villalobos et al. record.
- [open question] Chinchilla was not publicly released and "trained on English data"; results for other languages are not evaluated — would need multilingual scaling studies.

## Images / diagrams
### `hoffmann-2022-chinchilla.pdf/images/raster-p001-00.png`
- Provenance: raster image embedded in `articles/hoffmann-2022-chinchilla.pdf`, page 1, 875x216 px, extracted with `pdfimages -png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `hoffmann-2022-chinchilla.pdf/images/fig-01-p002.png`
- Provenance: Figure 1 of `articles/hoffmann-2022-chinchilla.pdf`, page 2, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 1076x671 px. Replaces the earlier whole-page render `page-002-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `hoffmann-2022-chinchilla.pdf/images/fig-02-p005.png`
- Provenance: Figure 2 of `articles/hoffmann-2022-chinchilla.pdf`, page 5, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 1075x485 px. Replaces the earlier whole-page render `page-005-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `hoffmann-2022-chinchilla.pdf/images/fig-03-p006.png`
- Provenance: Figure 3 of `articles/hoffmann-2022-chinchilla.pdf`, page 6, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 1076x514 px. Replaces the earlier whole-page render `page-006-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `hoffmann-2022-chinchilla.pdf/images/fig-04-p007.png`
- Provenance: Figure 4 of `articles/hoffmann-2022-chinchilla.pdf`, page 7, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 1078x652 px. Replaces the earlier whole-page render `page-007-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `hoffmann-2022-chinchilla.pdf/images/fig-05-p010.png`
- Provenance: Figure 5 of `articles/hoffmann-2022-chinchilla.pdf`, page 10, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 1077x575 px. Replaces the earlier whole-page render `page-010-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `hoffmann-2022-chinchilla.pdf/images/fig-06-p012.png`
- Provenance: Figure 6 of `articles/hoffmann-2022-chinchilla.pdf`, page 12, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 1075x624 px. Replaces the earlier whole-page render `page-012-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `hoffmann-2022-chinchilla.pdf/images/fig-07-p013.png`
- Provenance: Figure 7 of `articles/hoffmann-2022-chinchilla.pdf`, page 13, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 1074x605 px. Replaces the earlier whole-page render `page-013-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `hoffmann-2022-chinchilla.pdf/images/fig-A1-p023.png`
- Provenance: Figure A1 of `articles/hoffmann-2022-chinchilla.pdf`, page 23, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 1079x795 px. Replaces the earlier whole-page render `page-023-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `hoffmann-2022-chinchilla.pdf/images/fig-A2-p023.png`
- Provenance: Figure A2 of `articles/hoffmann-2022-chinchilla.pdf`, page 23, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 1073x639 px. Replaces the earlier whole-page render `page-023-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `hoffmann-2022-chinchilla.pdf/images/fig-A3-p026.png`
- Provenance: Figure A3 of `articles/hoffmann-2022-chinchilla.pdf`, page 26, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 1077x617 px. Replaces the earlier whole-page render `page-026-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `hoffmann-2022-chinchilla.pdf/images/fig-A4-p027.png`
- Provenance: Figure A4 of `articles/hoffmann-2022-chinchilla.pdf`, page 27, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 1079x635 px. Replaces the earlier whole-page render `page-027-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `hoffmann-2022-chinchilla.pdf/images/fig-A5-p028.png`
- Provenance: Figure A5 of `articles/hoffmann-2022-chinchilla.pdf`, page 28, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 1076x583 px. Replaces the earlier whole-page render `page-028-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `hoffmann-2022-chinchilla.pdf/images/fig-A6-p029.png`
- Provenance: Figure A6 of `articles/hoffmann-2022-chinchilla.pdf`, page 29, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 1075x442 px. Replaces the earlier whole-page render `page-029-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `hoffmann-2022-chinchilla.pdf/images/fig-A7-p029.png`
- Provenance: Figure A7 of `articles/hoffmann-2022-chinchilla.pdf`, page 29, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 1074x380 px. Replaces the earlier whole-page render `page-029-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->


## Raw / preserved excerpts
> "We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant. By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, we find that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled. We test this hypothesis by training a predicted compute-optimal model, Chinchilla, that uses the same compute budget as Gopher but with 70B parameters and 4× more more data. Chinchilla uniformly and significantly outperforms Gopher (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks. This also means that Chinchilla uses substantially less compute for fine-tuning and inference, greatly facilitating downstream usage. As a highlight, Chinchilla reaches a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over Gopher."
— Abstract

> "Kaplan et al. (2020) showed that there is a power law relationship between the number of parameters in an autoregressive language model (LM) and its performance. As a result, the field has been training larger and larger models, expecting performance improvements. One notable conclusion in Kaplan et al. (2020) is that large models should not be trained to their lowest possible loss to be compute optimal. Whilst we reach the same conclusion, we estimate that large models should be trained for many more training tokens than recommended by the authors. Specifically, given a 10× increase computational budget, they suggests that the size of the model should increase 5.5× while the number of training tokens should only increase 1.8×. Instead, we find that model size and the number of training tokens should be scaled in equal proportions."
— Section 1, Introduction

> "Following Kaplan et al. (2020) and the training setup of GPT-3 (Brown et al., 2020), many of the recently trained large models have been trained for approximately 300 billion tokens (Table 1), in line with the approach of predominantly increasing model size when increasing compute."
— Section 1

> "Based on our estimated compute-optimal frontier, we predict that for the compute budget used to train Gopher, an optimal model should be 4 times smaller, while being training on 4 times more tokens. We verify this by training a more compute-optimal 70B model, called Chinchilla, on 1.4 trillion tokens. Not only does Chinchilla outperform its much larger counterpart, Gopher, but its reduced model size reduces inference cost considerably and greatly facilitates downstream uses on smaller hardware."
— Section 1

> "Nonetheless, large language models face several challenges, including their overwhelming computational requirements (the cost of training and inference increase with model size) (Rae et al., 2021; Thoppilan et al., 2022) and the need for acquiring more high-quality training data. In fact, in this work we find that larger, high quality datasets will play a key role in any further scaling of language models."
— Section 2, Related Work

> "First, the authors use a fixed number of training tokens and learning rate schedule for all models; this prevents them from modelling the impact of these hyperparameters on the loss. In contrast, we find that setting the learning rate schedule to approximately match the number of training tokens results in the best final loss regardless of model size—see Figure A1. For a fixed learning rate cosine schedule to 130B tokens, the intermediate loss estimates (for D′ << 130B) are therefore overestimates of the loss of a model trained with a schedule length matching D′. Using these intermediate losses results in underestimating the effectiveness of training models on less data than 130B tokens, and eventually contributes to the conclusion that model size should increase faster than training data size as compute budget increases."
— Section 2, on Kaplan et al. (2020)

> "The first term captures the loss for an ideal generative process on the data distribution, and should correspond to the entropy of natural text. The second term captures the fact that a perfectly trained transformer with N parameters underperforms the ideal generative process. The final term captures the fact that the transformer is not trained to convergence, as we only make a finite number of optimisation steps, on a sample of the dataset distribution."
— Section 3.3, Approach 3

> "We find that the three approaches, despite using different fitting methodologies and different trained models, yield comparable predictions for the optimal scaling in parameters and tokens with FLOPs (shown in Table 2). All three approaches suggest that as compute budget increases, model size and the amount of training data should be increased in approximately equal proportions."
— Section 3.4

> "For example, we find that a 175 billion parameter model should be trained with a compute budget of 4.41 × 10^24 FLOPs and on over 4.2 trillion tokens. A 280 billion Gopher-like model is the optimal model to train given a compute budget of approximately 10^25 FLOPs and should be trained on 6.8 trillion tokens. Unless one has a compute budget of 10^26 FLOPs (over 250× the compute used to train Gopher), a 1 trillion parameter model is unlikely to be the optimal model to train. Furthermore, the amount of training data that is projected to be needed is far beyond what is currently used to train large models, and underscores the importance of dataset collection in addition to engineering improvements that allow for model scale."
— Section 3.4

> "We train Chinchilla with a slightly modified SentencePiece (Kudo and Richardson, 2018) tokenizer that does not apply NFKC normalisation. The vocabulary is very similar– 94.15% of tokens are the same as those used for training Gopher. We find that this particularly helps with the representation of mathematics and chemistry, for example."
— Section 4.1

> "On this benchmark, Chinchilla significantly outperforms Gopher despite being much smaller, with an average accuracy of 67.6% (improving upon Gopher by 7.6%). Remarkably, Chinchilla even outperforms the expert forecast for June 2023 of 63.4% accuracy (see Table 6) (Steinhardt, 2021)."
— Section 4.2.2, MMLU

> "In stark contrast with the findings of Lin et al. (2021), the large improvements (14.1% in 0-shot accuracy) achieved by Chinchilla suggest that better modelling of the pre-training data alone can lead to substantial improvements on this benchmark."
— Section 4.2.5, TruthfulQA

> "In line with prior findings (Rae et al., 2021), this suggests that toxicity levels in unconditional text generation are largely independent of the model quality (measured in language modelling loss), i.e. that better models of the training dataset are not necessarily more toxic."
— Section 4.2.7

> "The trend so far in large language model training has been to increase the model size, often without increasing the number of training tokens. The largest dense transformer, MT-NLG 530B, is now over 3× larger than GPT-3's 170 billion parameters from just two years ago. However, this model, as well as the majority of existing large models, have all been trained for a comparable number of tokens—around 300 billion. While the desire to train these mega-models has led to substantial engineering innovation, we hypothesize that the race to train larger and larger models is resulting in models that are substantially underperforming compared to what could be achieved with the same compute budget."
— Section 5, Discussion & Conclusion

> "Whilst our method allows us to make predictions on how to scale large models when given additional compute, there are several limitations. Due to the cost of training large models, we only have two comparable training runs at large scale (Chinchilla and Gopher), and we do not have additional tests at intermediate scales. Furthermore, we assume that the efficient computational frontier can be described by a power-law relationship between the compute budget, model size, and number of training tokens. However, we observe some concavity in log N_opt at high compute budgets (see Appendix E). This suggests that we may still be overestimating the optimal size of large models. Finally, the training runs for our analysis have all been trained on less than an epoch of data; future work may consider the multiple epoch regime."
— Section 5, limitations

> "Though there has been significant recent work allowing larger and larger models to be trained, our analysis suggests an increased focus on dataset scaling is needed. Speculatively, we expect that scaling to larger and larger datasets is only beneficial when the data is high-quality. This calls for responsibly collecting larger datasets with a high focus on dataset quality. Larger datasets will require extra care to ensure train-test set overlap is properly accounted for, both in the language modelling loss but also with downstream tasks. Finally, training for trillions of tokens introduces many ethical and privacy concerns. Large datasets scraped from the web will contain toxic language, biases, and private information. With even larger datasets being used, the quantity (if not the frequency) of such information increases, which makes dataset introspection all the more important."
— Section 5

> "In Table A1 we show the training dataset makeup used for Chinchilla and all scaling runs. Note that both the MassiveWeb and Wikipedia subsets are both used for more than one epoch."
— Appendix A, Training dataset

> "We find that the scaling behaviour on these datasets is very similar to what we found on MassiveText, as shown in Figure A2 and Table A2. This suggests that our results are independent of the dataset as long as one does not train for more than one epoch."
— Appendix C

> "Empirically, we find after fitting (2) that L(N, D) = E + A/N^0.34 + B/D^0.28, with E = 1.69, A = 406.4, B = 410.7. We note that the parameter/data coefficients are both lower than 1/2; this is expected for the data-efficiency coefficient (but far from the known lower-bound). Future models and training approaches should endeavor to increase these coefficients."
— Appendix D.2 (equation rendered from the garbled extraction)

> "From Kaplan et al. (2020), we find that the optimal model size should be 4.68 billion parameters. From our approach 1, we estimate a 2.86 billion parameter model should be optimal. We train a 4.74 billion parameter and a 2.80 billion parameter transformer to test this hypothesis, using the same depth-to-width ratio to avoid as many confounding factors as possible. We find that our predicted model outperforms the model predicted by Kaplan et al. (2020) as shown in Figure A4."
— Appendix D.4

> "Relevant factors include which language is used. Our model is trained on English data. Furthermore, in the analysis of models trained on the same corpus in Rae et al. (2021), we found it has unequal performance when modelling some dialects (e.g., African American English)."
— Table A8, Model card (Factors)

> "We considered filtering the dataset to remove toxic content but decided against it due to the observation that this can introduce new biases as studied by Welbl et al. (2021)."
— Table A8, Model card (Mitigations)

> "The data is collected from the internet, and thus undoubtedly there is toxic/biased content in our training dataset. Furthermore, it is likely that personal information is also in the dataset that has been used to train our models."
— Table A8, Model card (Risks and Harms)

### Full extracted text (verbatim)
Complete `pdftotext` output of all 36 pages (page breaks removed). Preserved in full so any passage can be restored.

~~~~~text
Training Compute-Optimal Large Language Models
Jordan Hoffmann★, Sebastian Borgeaud★, Arthur Mensch★, Elena Buchatskaya, Trevor Cai, Eliza Rutherford,
Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland,
Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan,
Erich Elsen, Jack W. Rae, Oriol Vinyals and Laurent Sifre★

arXiv:2203.15556v1 [cs.CL] 29 Mar 2022

★

Equal contributions

We investigate the optimal model size and number of tokens for training a transformer language model
under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of
training data constant. By training over 400 language models ranging from 70 million to over 16 billion
parameters on 5 to 500 billion tokens, we find that for compute-optimal training, the model size and
the number of training tokens should be scaled equally: for every doubling of model size the number
of training tokens should also be doubled. We test this hypothesis by training a predicted computeoptimal model, Chinchilla, that uses the same compute budget as Gopher but with 70B parameters and
4× more more data. Chinchilla uniformly and significantly outperforms Gopher (280B), GPT-3 (175B),
Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks.
This also means that Chinchilla uses substantially less compute for fine-tuning and inference, greatly
facilitating downstream usage. As a highlight, Chinchilla reaches a state-of-the-art average accuracy of
67.5% on the MMLU benchmark, greater than a 7% improvement over Gopher.

1. Introduction
Recently a series of Large Language Models (LLMs) have been introduced (Brown et al., 2020; Lieber
et al., 2021; Rae et al., 2021; Smith et al., 2022; Thoppilan et al., 2022), with the largest dense
language models now having over 500 billion parameters. These large autoregressive transformers
(Vaswani et al., 2017) have demonstrated impressive performance on many tasks using a variety of
evaluation protocols such as zero-shot, few-shot, and fine-tuning.
The compute and energy cost for training large language models is substantial (Rae et al., 2021;
Thoppilan et al., 2022) and rises with increasing model size. In practice, the allocated training
compute budget is often known in advance: how many accelerators are available and for how long
we want to use them. Since it is typically only feasible to train these large models once, accurately
estimating the best model hyperparameters for a given compute budget is critical (Tay et al., 2021).
Kaplan et al. (2020) showed that there is a power law relationship between the number of
parameters in an autoregressive language model (LM) and its performance. As a result, the field has
been training larger and larger models, expecting performance improvements. One notable conclusion
in Kaplan et al. (2020) is that large models should not be trained to their lowest possible loss to be
compute optimal. Whilst we reach the same conclusion, we estimate that large models should be
trained for many more training tokens than recommended by the authors. Specifically, given a 10×
increase computational budget, they suggests that the size of the model should increase 5.5× while
the number of training tokens should only increase 1.8×. Instead, we find that model size and the
number of training tokens should be scaled in equal proportions.
Following Kaplan et al. (2020) and the training setup of GPT-3 (Brown et al., 2020), many of the
recently trained large models have been trained for approximately 300 billion tokens (Table 1), in
line with the approach of predominantly increasing model size when increasing compute.
Corresponding authors: {jordanhoffmann|sborgeaud|amensch|sifre}@deepmind.com
© 2023 DeepMind. All rights reserved


1T
Approach 1
Approach 2
Approach 3
Kaplan et al (2020)

Parameters

100B
10B

Chinchilla (70B)
Gopher (280B)
GPT-3 (175B)
Megatron-Turing NLG (530B)

1.0B

100M
10M1017

1019

1021

FLOPs

1023

1025

Figure 1 | Overlaid predictions. We overlay the predictions from our three different approaches,
along with projections from Kaplan et al. (2020). We find that all three methods predict that current
large models should be substantially smaller and therefore trained much longer than is currently
done. In Figure A3, we show the results with the predicted optimal tokens plotted against the optimal
number of parameters for fixed FLOP budgets. Chinchilla outperforms Gopher and the other large
models (see Section 4.2).
In this work, we revisit the question: Given a fixed FLOPs budget,1 how should one trade-off model
size and the number of training tokens? To answer this question, we model the final pre-training loss2
𝐿 ( 𝑁, 𝐷) as a function of the number of model parameters 𝑁 , and the number of training tokens, 𝐷.
Since the computational budget 𝐶 is a deterministic function FLOPs( 𝑁, 𝐷) of the number of seen
training tokens and model parameters, we are interested in minimizing 𝐿 under the constraint
FLOPs( 𝑁, 𝐷) = 𝐶 :
𝑁𝑜𝑝𝑡 ( 𝐶 ) , 𝐷𝑜𝑝𝑡 ( 𝐶 ) =
argmin
𝐿 ( 𝑁, 𝐷) .
(1)
𝑁,𝐷 s.t. FLOPs( 𝑁,𝐷)=𝐶

The functions 𝑁𝑜𝑝𝑡 (𝐶 ), and 𝐷𝑜𝑝𝑡 (𝐶 ) describe the optimal allocation of a computational budget 𝐶 . We
empirically estimate these functions based on the losses of over 400 models, ranging from under 70M
to over 16B parameters, and trained on 5B to over 400B tokens – with each model configuration
trained for several different training horizons. Our approach leads to considerably different results
than that of Kaplan et al. (2020). We highlight our results in Figure 1 and how our approaches differ
in Section 2.
Based on our estimated compute-optimal frontier, we predict that for the compute budget used
to train Gopher, an optimal model should be 4 times smaller, while being training on 4 times more
tokens. We verify this by training a more compute-optimal 70B model, called Chinchilla, on 1.4 trillion
tokens. Not only does Chinchilla outperform its much larger counterpart, Gopher, but its reduced
model size reduces inference cost considerably and greatly facilitates downstream uses on smaller
hardware. The energy cost of a large language model is amortized through its usage for inference an
fine-tuning. The benefits of a more optimally trained smaller model, therefore, extend beyond the
immediate benefits of its improved performance.
1 For example, knowing the number of accelerators and a target training duration.

2 For simplicity, we perform our analysis on the smoothed training loss which is an unbiased estimate of the test loss, as

we are in the infinite data regime (the number of training tokens is less than the number of tokens in the entire corpus).

2


Table 1 | Current LLMs. We show five of the current largest dense transformer models, their size,
and the number of training tokens. Other than LaMDA (Thoppilan et al., 2022), most models are
trained for approximately 300 billion tokens. We introduce Chinchilla, a substantially smaller model,
trained for much longer than 300B tokens.
Model

Size (# Parameters)

Training Tokens

LaMDA (Thoppilan et al., 2022)
GPT-3 (Brown et al., 2020)
Jurassic (Lieber et al., 2021)
Gopher (Rae et al., 2021)
MT-NLG 530B (Smith et al., 2022)

137 Billion
175 Billion
178 Billion
280 Billion
530 Billion

168 Billion
300 Billion
300 Billion
300 Billion
270 Billion

Chinchilla

70 Billion

1.4 Trillion

2. Related Work
Large language models. A variety of large language models have been introduced in the last few
years. These include both dense transformer models (Brown et al., 2020; Lieber et al., 2021; Rae
et al., 2021; Smith et al., 2022; Thoppilan et al., 2022) and mixture-of-expert (MoE) models (Du
et al., 2021; Fedus et al., 2021; Zoph et al., 2022). The largest dense transformers have passed 500
billion parameters (Smith et al., 2022). The drive to train larger and larger models is clear—so far
increasing the size of language models has been responsible for improving the state-of-the-art in many
language modelling tasks. Nonetheless, large language models face several challenges, including
their overwhelming computational requirements (the cost of training and inference increase with
model size) (Rae et al., 2021; Thoppilan et al., 2022) and the need for acquiring more high-quality
training data. In fact, in this work we find that larger, high quality datasets will play a key role in any
further scaling of language models.
Modelling the scaling behavior. Understanding the scaling behaviour of language models and
their transfer properties has been important in the development of recent large models (Hernandez
et al., 2021; Kaplan et al., 2020). Kaplan et al. (2020) first showed a predictable relationship between
model size and loss over many orders of magnitude. The authors investigate the question of choosing
the optimal model size to train for a given compute budget. Similar to us, they address this question
by training various models. Our work differs from Kaplan et al. (2020) in several important ways.
First, the authors use a fixed number of training tokens and learning rate schedule for all models; this
prevents them from modelling the impact of these hyperparameters on the loss. In contrast, we find
that setting the learning rate schedule to approximately match the number of training tokens results
in the best final loss regardless of model size—see Figure A1. For a fixed learning rate cosine schedule
to 130B tokens, the intermediate loss estimates (for 𝐷 0 << 130B) are therefore overestimates of the
loss of a model trained with a schedule length matching 𝐷 0. Using these intermediate losses results in
underestimating the effectiveness of training models on less data than 130B tokens, and eventually
contributes to the conclusion that model size should increase faster than training data size as compute
budget increases. In contrast, our analysis predicts that both quantities should scale at roughly the
same rate. Secondly, we include models with up to 16B parameters, as we observe that there is slight
curvature in the FLOP-loss frontier (see Appendix E)—in fact, the majority of the models used in
our analysis have more than 500 million parameters, in contrast the majority of runs in Kaplan et al.
(2020) are significantly smaller—many being less than 100M parameters.
Recently, Clark et al. (2022) specifically looked in to the scaling properties of Mixture of Expert
3


language models, showing that the scaling with number of experts diminishes as the model size
increases—their approach models the loss as a function of two variables: the model size and the
number of experts. However, the analysis is done with a fixed number of training tokens, as in Kaplan
et al. (2020), potentially underestimating the improvements of branching.
Estimating hyperparameters for large models. The model size and the number of training tokens
are not the only two parameters to chose when selecting a language model and a procedure to train
it. Other important factors include learning rate, learning rate schedule, batch size, optimiser, and
width-to-depth ratio. In this work, we focus on model size and the number of training steps, and
we rely on existing work and provided experimental heuristics to determine the other necessary
hyperparameters. Yang et al. (2021) investigates how to choose a variety of these parameters for
training an autoregressive transformer, including the learning rate and batch size. McCandlish et al.
(2018) finds only a weak dependence between optimal batch size and model size. Shallue et al.
(2018); Zhang et al. (2019) suggest that using larger batch-sizes than those we use is possible. Levine
et al. (2020) investigates the optimal depth-to-width ratio for a variety of standard model sizes. We
use slightly less deep models than proposed as this translates to better wall-clock performance on our
hardware.
Improved model architectures. Recently, various promising alternatives to traditional dense transformers have been proposed. For example, through the use of conditional computation large MoE
models like the 1.7 trillion parameter Switch transformer (Fedus et al., 2021), the 1.2 Trillion parameter GLaM model (Du et al., 2021), and others (Artetxe et al., 2021; Zoph et al., 2022) are able
to provide a large effective model size despite using relatively fewer training and inference FLOPs.
However, for very large models the computational benefits of routed models seems to diminish (Clark
et al., 2022). An orthogonal approach to improving language models is to augment transformers
with explicit retrieval mechanisms, as done by Borgeaud et al. (2021); Guu et al. (2020); Lewis et al.
(2020). This approach effectively increases the number of data tokens seen during training (by a
factor of ∼ 10 in Borgeaud et al. (2021)). This suggests that the performance of language models
may be more dependant on the size of the training data than previously thought.

3. Estimating the optimal parameter/training tokens allocation
We present three different approaches to answer the question driving our research: Given a fixed
FLOPs budget, how should one trade-off model size and the number of training tokens? In all three
cases we start by training a range of models varying both model size and the number of training
tokens and use the resulting training curves to fit an empirical estimator of how they should scale.
We assume a power-law relationship between compute and model size as done in Clark et al. (2022);
Kaplan et al. (2020), though future work may want to include potential curvature in this relationship
for large model sizes. The resulting predictions are similar for all three methods and suggest that
parameter count and number of training tokens should be increased equally with more compute3 —
with proportions reported in Table 2. This is in clear contrast to previous work on this topic and
warrants further investigation.

3 We compute FLOPs as described in Appendix F.

4


75M

1012

100B 67B
1011

10B

1010

1.0B

109

100M

2.0
1017

1018

1019

1020

FLOPS

1021

1.5T

Tokens

2.5

1T

Parameters

10B
5B
2.5B
1B
500M
250M

Training loss

6.0
5.5
5.0
4.5
4.0
3.5
3.0

1022

1017

1019

1021

FLOPs

1023

1025

1017

1019

1021

FLOPs

1023

1025

Figure 2 | Training curve envelope. On the left we show all of our different runs. We launched a
range of model sizes going from 70M to 10B, each for four different cosine cycle lengths. From these
curves, we extracted the envelope of minimal loss per FLOP, and we used these points to estimate the
optimal model size (center) for a given compute budget and the optimal number of training tokens
(right). In green, we show projections of optimal model size and training token count based on the
number of FLOPs used to train Gopher (5.76 × 1023 ).
3.1. Approach 1: Fix model sizes and vary number of training tokens
In our first approach we vary the number of training steps for a fixed family of models (ranging from
70M to over 10B parameters), training each model for 4 different number of training sequences.
From these runs, we are able to directly extract an estimate of the minimum loss achieved for a given
number of training FLOPs. Training details for this approach can be found in Appendix D.
For each parameter count 𝑁 we train 4 different models, decaying the learning rate by a factor of
10× over a horizon (measured in number of training tokens) that ranges by a factor of 16×. Then, for
each run, we smooth and then interpolate the training loss curve. From this, we obtain a continuous
mapping from FLOP count to training loss for each run. Then, for each FLOP count, we determine
which run achieves the lowest loss. Using these interpolants, we obtain a mapping from any FLOP
count 𝐶 , to the most efficient choice of model size 𝑁 and number of training tokens 𝐷 such that
FLOPs( 𝑁, 𝐷) = 𝐶 .4 At 1500 logarithmically spaced FLOP values, we find which model size achieves the
lowest loss of all models along with the required number of training tokens. Finally, we fit power laws
to estimate the optimal model size and number of training tokens for any given amount of compute
(see the center and right panels of Figure 2), obtaining a relationship 𝑁𝑜𝑝𝑡 ∝ 𝐶 𝑎 and 𝐷𝑜𝑝𝑡 ∝ 𝐶 𝑏 . We
find that 𝑎 = 0.50 and 𝑏 = 0.50—as summarized in Table 2. In Section D.4, we show a head-to-head
comparison at 1021 FLOPs, using the model size recommended by our analysis and by the analysis of
Kaplan et al. (2020)—using the model size we predict has a clear advantage.
3.2. Approach 2: IsoFLOP profiles
In our second approach we vary the model size5 for a fixed set of 9 different training FLOP counts6
(ranging from 6 × 1018 to 3 × 1021 FLOPs), and consider the final training loss for each point7 . in
contrast with Approach 1 that considered points ( 𝑁, 𝐷, 𝐿) along the entire training runs. This allows
us to directly answer the question: For a given FLOP budget, what is the optimal parameter count?
4 Note that all selected points are within the last 15% of training. This suggests that when training a model over 𝐷 tokens,
we should pick a cosine cycle length that decays 10× over approximately 𝐷 tokens—see further details in Appendix B.
5 In approach 2, model size varies up to 16B as opposed to approach 1 where we only used models up to 10B.
6 The number of training tokens is determined by the model size and training FLOPs.
7 We set the cosine schedule length to match the number of tokens, which is optimal according to the analysis presented
in Appendix B.

5


3.2
3.0

2.4
2.2
2.0

6e18
1e19
3e19
6e19
1e20
3e20
6e20
1e21
3e21
100M 300M

Tokens

2.6

1T

100B 63B

Parameters

Training Loss

2.8

10T

1T

10B
1B

1B

3B 6B

30B

100B
10B
1B

100M

Parameters

1.4T

1017

1019

1021

FLOPs

1023

1025

100M 17
10

1019

1021

FLOPs

1023

1025

Figure 3 | IsoFLOP curves. For various model sizes, we choose the number of training tokens such
that the final FLOPs is a constant. The cosine cycle length is set to match the target FLOP count. We
find a clear valley in loss, meaning that for a given FLOP budget there is an optimal model to train
(left). Using the location of these valleys, we project optimal model size and number of tokens for
larger models (center and right). In green, we show the estimated number of parameters and tokens
for an optimal model trained with the compute budget of Gopher.
For each FLOP budget, we plot the final loss (after smoothing) against the parameter count in
Figure 3 (left). In all cases, we ensure that we have trained a diverse enough set of model sizes to see
a clear minimum in the loss. We fit a parabola to each IsoFLOPs curve to directly estimate at what
model size the minimum loss is achieved (Figure 3 (left)). As with the previous approach, we then fit
a power law between FLOPs and loss-optimal model size and number of training tokens, shown in
Figure 3 (center, right). Again, we fit exponents of the form 𝑁𝑜𝑝𝑡 ∝ 𝐶 𝑎 and 𝐷𝑜𝑝𝑡 ∝ 𝐶 𝑏 and we find that
𝑎 = 0.49 and 𝑏 = 0.51—as summarized in Table 2.
3.3. Approach 3: Fitting a parametric loss function
Lastly, we model all final losses from experiments in Approach 1 & 2 as a parametric function of
model parameter count and the number of seen tokens. Following a classical risk decomposition (see
Section D.2), we propose the following functional form
𝐿ˆ( 𝑁, 𝐷) , 𝐸 +

𝐴
𝐵
+ 𝛽.
𝛼
𝑁
𝐷

(2)

The first term captures the loss for an ideal generative process on the data distribution, and should
correspond to the entropy of natural text. The second term captures the fact that a perfectly trained
transformer with 𝑁 parameters underperforms the ideal generative process. The final term captures
the fact that the transformer is not trained to convergence, as we only make a finite number of
optimisation steps, on a sample of the dataset distribution.
Model fitting. To estimate ( 𝐴, 𝐵, 𝐸, 𝛼, 𝛽 ), we minimize the Huber loss (Huber, 1964) between the
predicted and observed log loss using the L-BFGS algorithm (Nocedal, 1980):


∑︁
min
Huber𝛿 log 𝐿ˆ( 𝑁𝑖 , 𝐷𝑖 ) − log 𝐿𝑖
(3)
𝐴,𝐵,𝐸,𝛼,𝛽

Runs 𝑖

We account for possible local minima by selecting the best fit from a grid of initialisations. The Huber
loss (𝛿 = 10−3 ) is robust to outliers, which we find important for good predictive performance over
held-out data points. Section D.2 details the fitting procedure and the loss decomposition.
6


IsoLoss contours

100B
40B

Loss

Model size

Train. FLOPs
6e+18
1e+19
3e+19
6e+19
1e+20
3e+20
6e+20
1e+21
3e+21
Gopher

4.00

10B
1B
Efficient frontier
Empirical data
IsoFLOPs slice

100M
1018

IsoFLOPs slices

5.00

1019

1020

1021

1022

3.00

2.00

1023 Gopher
budget

Training FLOPs

100M

1B

10B 40B

Model size

Figure 4 | Parametric fit. We fit a parametric modelling of the loss 𝐿ˆ( 𝑁, 𝐷) and display contour (left)
and isoFLOP slices (right). For each isoFLOP slice, we include a corresponding dashed line in the left
plot. In the left plot, we show the efficient frontier in blue, which is a line in log-log space. Specifically,
the curve goes through each iso-loss contour at the point with the fewest FLOPs. We project the
optimal model size given the Gopher FLOP budget to be 40B parameters.
Efficient frontier. We can approximate the functions 𝑁𝑜𝑝𝑡 and 𝐷𝑜𝑝𝑡 by minimizing the parametric
loss 𝐿ˆ under the constraint FLOPs( 𝑁, 𝐷) ≈ 6 𝑁 𝐷 (Kaplan et al., 2020). The resulting 𝑁𝑜𝑝𝑡 and 𝐷𝑜𝑝𝑡
balance the two terms in Equation (3) that depend on model size and data. By construction, they
have a power-law form:
 𝑎
𝑁𝑜𝑝𝑡 ( 𝐶 ) = 𝐺

𝐶

6

,

𝐷𝑜𝑝𝑡 ( 𝐶 ) = 𝐺

−1

 𝑏
𝐶

6

,

where



𝛼𝐴
𝐺=
𝛽𝐵

 𝛼+1𝛽
,

𝑎=

𝛽
𝛼
, and 𝑏 =
.
𝛼+𝛽
𝛼+𝛽

(4)

We show contours of the fitted function 𝐿ˆ in Figure 4 (left), and the closed-form efficient computational
frontier in blue. From this approach, we find that 𝑎 = 0.46 and 𝑏 = 0.54—as summarized in Table 2.
3.4. Optimal model scaling
We find that the three approaches, despite using different fitting methodologies and different trained
models, yield comparable predictions for the optimal scaling in parameters and tokens with FLOPs
(shown in Table 2). All three approaches suggest that as compute budget increases, model size and
the amount of training data should be increased in approximately equal proportions. The first and
second approaches yield very similar predictions for optimal model sizes, as shown in Figure 1 and
Figure A3. The third approach predicts even smaller models being optimal at larger compute budgets.
We note that the observed points ( 𝐿, 𝑁, 𝐷) for low training FLOPs (𝐶 ⩽ 1𝑒21) have larger residuals
2
k 𝐿 − 𝐿ˆ( 𝑁, 𝐷)k 2 than points with higher computational budgets. The fitted model places increased
weight on the points with more FLOPs—automatically considering the low-computational budget
points as outliers due to the Huber loss. As a consequence of the empirically observed negative
curvature in the frontier 𝐶 → 𝑁𝑜𝑝𝑡 (see Appendix E), this results in predicting a lower 𝑁𝑜𝑝𝑡 than the
two other approaches.
In Table 3 we show the estimated number of FLOPs and tokens that would ensure that a model of
a given size lies on the compute-optimal frontier. Our findings suggests that the current generation of
7


Table 2 | Estimated parameter and data scaling with increased training compute. The listed
values are the exponents, 𝑎 and 𝑏, on the relationship 𝑁𝑜𝑝𝑡 ∝ 𝐶 𝑎 and 𝐷𝑜𝑝𝑡 ∝ 𝐶 𝑏 . Our analysis suggests
a near equal scaling in parameters and data with increasing compute which is in clear contrast
to previous work on the scaling of large models. The 10th and 90th percentiles are estimated via
bootstrapping data (80% of the dataset is sampled 100 times) and are shown in parenthesis.
Approach
1. Minimum over training curves
2. IsoFLOP profiles
3. Parametric modelling of the loss

Coeff. 𝑎 where 𝑁𝑜𝑝𝑡 ∝ 𝐶 𝑎

Coeff. 𝑏 where 𝐷𝑜𝑝𝑡 ∝ 𝐶 𝑏

0.50 (0.488, 0.502)
0.49 (0.462, 0.534)
0.46 (0.454, 0.455)

0.50 (0.501, 0.512)
0.51 (0.483, 0.529)
0.54 (0.542, 0.543)

0.73

0.27

Kaplan et al. (2020)

Table 3 | Estimated optimal training FLOPs and training tokens for various model sizes. For
various model sizes, we show the projections from Approach 1 of how many FLOPs and training
tokens would be needed to train compute-optimal models. The estimates for Approach 2 & 3 are
similar (shown in Section D.3)
Parameters

FLOPs

FLOPs (in Gopher unit)

Tokens

400 Million
1 Billion
10 Billion
67 Billion
.
175 Billion
280 Billion
520 Billion
1 Trillion
10 Trillion

1.92e+19
1.21e+20
1.23e+22
5.76e+23
3.85e+24
9.90e+24
3.43e+25
1.27e+26
1.30e+28

1/29, 968
1/4, 761
1/46
1
6.7
17.2
59.5
221.3
22515.9

8.0 Billion
20.2 Billion
205.1 Billion
1.5 Trillion
3.7 Trillion
5.9 Trillion
11.0 Trillion
21.2 Trillion
216.2 Trillion

large language models are considerably over-sized, given their respective compute budgets, as shown
in Figure 1. For example, we find that a 175 billion parameter model should be trained with a compute
budget of 4.41 × 1024 FLOPs and on over 4.2 trillion tokens. A 280 billion Gopher-like model is the
optimal model to train given a compute budget of approximately 1025 FLOPs and should be trained on
6.8 trillion tokens. Unless one has a compute budget of 1026 FLOPs (over 250× the compute used to
train Gopher), a 1 trillion parameter model is unlikely to be the optimal model to train. Furthermore,
the amount of training data that is projected to be needed is far beyond what is currently used to
train large models, and underscores the importance of dataset collection in addition to engineering
improvements that allow for model scale. While there is significant uncertainty extrapolating out
many orders of magnitude, our analysis clearly suggests that given the training compute budget for
many current LLMs, smaller models should have been trained on more tokens to achieve the most
performant model.
In Appendix C, we reproduce the IsoFLOP analysis on two additional datasets: C4 (Raffel et al.,
2020a) and GitHub code (Rae et al., 2021). In both cases we reach the similar conclusion that model
size and number of training tokens should be scaled in equal proportions.

8


4. Chinchilla
Based on our analysis in Section 3, the optimal model size for the Gopher compute budget is somewhere
between 40 and 70 billion parameters. We test this hypothesis by training a model on the larger end
of this range—70B parameters—for 1.4T tokens, due to both dataset and computational efficiency
considerations. In this section we compare this model, which we call Chinchilla, to Gopher and other
LLMs. Both Chinchilla and Gopher have been trained for the same number of FLOPs but differ in the
size of the model and the number of training tokens.
While pre-training a large language model has a considerable compute cost, downstream finetuning and inference also make up substantial compute usage (Rae et al., 2021). Due to being 4×
smaller than Gopher, both the memory footprint and inference cost of Chinchilla are also smaller.
4.1. Model and training details
The full set of hyperparameters used to train Chinchilla are given in Table 4. Chinchilla uses the same
model architecture and training setup as Gopher with the exception of the differences listed below.
• We train Chinchilla on MassiveText (the same dataset as Gopher) but use a slightly different
subset distribution (shown in Table A1) to account for the increased number of training tokens.
• We use AdamW (Loshchilov and Hutter, 2019) for Chinchilla rather than Adam (Kingma and
Ba, 2014) as this improves the language modelling loss and the downstream task performance
after finetuning.8
• We train Chinchilla with a slightly modified SentencePiece (Kudo and Richardson, 2018)
tokenizer that does not apply NFKC normalisation. The vocabulary is very similar– 94.15% of
tokens are the same as those used for training Gopher. We find that this particularly helps with
the representation of mathematics and chemistry, for example.
• Whilst the forward and backward pass are computed in bfloat16, we store a float32 copy
of the weights in the distributed optimiser state (Rajbhandari et al., 2020). See Lessons Learned
from Rae et al. (2021) for additional details.
In Appendix G we show the impact of the various optimiser related changes between Chinchilla
and Gopher. All models in this analysis have been trained on TPUv3/TPUv4 (Jouppi et al., 2017) with
JAX (Bradbury et al., 2018) and Haiku (Hennigan et al., 2020). We include a Chinchilla model card
(Mitchell et al., 2019) in Table A8.
Model

Layers

Number Heads

Key/Value Size

dmodel

Max LR

Batch Size

Gopher 280B
Chinchilla 70B

80
80

128
64

128
128

16,384
8,192

4 × 10−5
1 × 10−4

3M → 6M
1.5M → 3M

Table 4 | Chinchilla architecture details. We list the number of layers, the key/value size, the
bottleneck activation size dmodel , the maximum learning rate, and the training batch size (# tokens).
The feed-forward size is always set to 4 × dmodel . Note that we double the batch size midway through
training for both Chinchilla and Gopher.

8 Interestingly, a model trained with AdamW only passes the training performance of a model trained with Adam around

80% of the way through the cosine cycle, though the ending performance is notably better– see Figure A7

9


# Tasks
Language Modelling
Reading Comprehension
Question Answering
Common Sense
MMLU
BIG-bench

20
3
3
5
57
62

Examples
WikiText-103, The Pile: PG-19, arXiv, FreeLaw, . . .
RACE-m, RACE-h, LAMBADA
Natural Questions, TriviaQA, TruthfulQA
HellaSwag, Winogrande, PIQA, SIQA, BoolQ
High School Chemistry, Astronomy, Clinical Knowledge, . . .
Causal Judgement, Epistemic Reasoning, Temporal Sequences, . . .

Table 5 | All evaluation tasks. We evaluate Chinchilla on a collection of language modelling along
with downstream tasks. We evaluate on largely the same tasks as in Rae et al. (2021), to allow for
direct comparison.
4.2. Results
We perform an extensive evaluation of Chinchilla, comparing against various large language models.
We evaluate on a large subset of the tasks presented in Rae et al. (2021), shown in Table 5. As
the focus of this work is on optimal model scaling, we included a large representative subset, and
introduce a few new evaluations to allow for better comparison to other existing large models. The
evaluation details for all tasks are the same as described in Rae et al. (2021).
4.2.1. Language modelling

Decrease in bpb
compared to Gopher

0.10
0.08
0.06
0.04
0.00

pubmed_abstracts
nih_exporter
uspto_backgrounds
pubmed_central
pile_cc
bookcorpus2
stackexchange
opensubtitles
openwebtext2
hackernews
dm_mathematics
arxiv
freelaw
books3
philpapers
github
ubuntu_irc
europarl
gutenberg_pg_19

0.02

Figure 5 | Pile Evaluation. For the different evaluation sets in The Pile (Gao et al., 2020), we show
the bits-per-byte (bpb) improvement (decrease) of Chinchilla compared to Gopher. On all subsets,
Chinchilla outperforms Gopher.
Chinchilla significantly outperforms Gopher on all evaluation subsets of The Pile (Gao et al.,
2020), as shown in Figure 5. Compared to Jurassic-1 (178B) Lieber et al. (2021), Chinchilla is more
performant on all but two subsets– dm_mathematics and ubuntu_irc– see Table A5 for a raw
bits-per-byte comparison. On Wikitext103 (Merity et al., 2017), Chinchilla achieves a perplexity of
7.16 compared to 7.75 for Gopher. Some caution is needed when comparing Chinchilla with Gopher
on these language modelling benchmarks as Chinchilla is trained on 4× more data than Gopher and
thus train/test set leakage may artificially enhance the results. We thus place more emphasis on other
10


Random
Average human rater
GPT-3 5-shot
Gopher 5-shot
Chinchilla 5-shot
Average human expert performance

25.0%
34.5%
43.9%
60.0%
67.6%
89.8%

June 2022 Forecast
June 2023 Forecast

57.1%
63.4%

Table 6 | Massive Multitask Language Understanding (MMLU). We report the average 5-shot
accuracy over 57 tasks with model and human accuracy comparisons taken from Hendrycks et al.
(2020). We also include the average prediction for state of the art accuracy in June 2022/2023 made
by 73 competitive human forecasters in Steinhardt (2021).
tasks for which leakage is less of a concern, such as MMLU (Hendrycks et al., 2020) and BIG-bench
(BIG-bench collaboration, 2021) along with various closed-book question answering and common
sense analyses.
4.2.2. MMLU
The Massive Multitask Language Understanding (MMLU) benchmark (Hendrycks et al., 2020) consists
of a range of exam-like questions on academic subjects. In Table 6, we report Chinchilla’s average
5-shot performance on MMLU (the full breakdown of results is shown in Table A6). On this benchmark,
Chinchilla significantly outperforms Gopher despite being much smaller, with an average accuracy of
67.6% (improving upon Gopher by 7.6%). Remarkably, Chinchilla even outperforms the expert forecast
for June 2023 of 63.4% accuracy (see Table 6) (Steinhardt, 2021). Furthermore, Chinchilla achieves
greater than 90% accuracy on 4 different individual tasks– high_school_gov_and_politics,
international_law, sociology, and us_foreign_policy. To our knowledge, no other model
has achieved greater than 90% accuracy on a subset.
In Figure 6, we show a comparison to Gopher broken down by task. Overall, we find that Chinchilla improves performance on the vast majority of tasks. On four tasks (college_mathematics,
econometrics, moral_scenarios, and formal_logic) Chinchilla underperforms Gopher, and
there is no change in performance on two tasks.
4.2.3. Reading comprehension
On the final word prediction dataset LAMBADA (Paperno et al., 2016), Chinchilla achieves 77.4%
accuracy, compared to 74.5% accuracy from Gopher and 76.6% from MT-NLG 530B (see Table 7). On
RACE-h and RACE-m (Lai et al., 2017), Chinchilla greatly outperforms Gopher, improving accuracy
by more than 10% in both cases—see Table 7.
4.2.4. BIG-bench
We analysed Chinchilla on the same set of BIG-bench tasks (BIG-bench collaboration, 2021) reported
in Rae et al. (2021). Similar to what we observed in MMLU, Chinchilla outperforms Gopher on the
vast majority of tasks (see Figure 7). We find that Chinchilla improves the average performance
by 10.7%, reaching an accuracy of 65.1% versus 54.4% for Gopher. Of the 62 tasks we consider,
Chinchilla performs worse than Gopher on only four—crash_blossom, dark_humor_detection,
11


20
10
0
10
college_mathematics
econometrics
moral_scenarios
formal_logic
medical_genetics
machine_learning
public_relations
global_facts
business_ethics
electrical_engineering
college_computer_science
world_religions
high_school_us_history
high_school_psychology
management
high_school_computer_science
marketing
high_school_physics
high_school_macroeconomics
sociology
high_school_government_and_politics
high_school_european_history
nutrition
college_medicine
astronomy
logical_fallacies
professional_psychology
miscellaneous
jurisprudence
clinical_knowledge
high_school_geography
high_school_biology
college_biology
college_chemistry
high_school_world_history
us_foreign_policy
virology
philosophy
moral_disputes
human_aging
computer_security
security_studies
international_law
high_school_microeconomics
high_school_statistics
professional_accounting
professional_medicine
prehistory
high_school_chemistry
elementary_mathematics
abstract_algebra
anatomy
professional_law
human_sexuality
college_physics
high_school_mathematics
conceptual_physics

Relative Improvement
over Gopher

30

Figure 6 | MMLU results compared to Gopher We find that Chinchilla outperforms Gopher by 7.6%
on average (see Table 6) in addition to performing better on 51/57 individual tasks, the same on
2/57, and worse on only 4/57 tasks.

LAMBADA Zero-Shot
RACE-m Few-Shot
RACE-h Few-Shot

Chinchilla

Gopher

GPT-3

MT-NLG 530B

77.4
86.8
82.3

74.5
75.1
71.6

76.2
58.1
46.8

76.6
47.9

Table 7 | Reading comprehension. On RACE-h and RACE-m (Lai et al., 2017), Chinchilla considerably
improves performance over Gopher. Note that GPT-3 and MT-NLG 530B use a different prompt format
than we do on RACE-h/m, so results are not comparable to Gopher and Chinchilla. On LAMBADA
(Paperno et al., 2016), Chinchilla outperforms both Gopher and MT-NLG 530B.

mathematical_induction and logical_args. Full accuracy results for Chinchilla can be found
in Table A7.

4.2.5. Common sense
We evaluate Chinchilla on various common sense benchmarks: PIQA (Bisk et al., 2020), SIQA (Sap
et al., 2019), Winogrande (Sakaguchi et al., 2020), HellaSwag (Zellers et al., 2019), and BoolQ
(Clark et al., 2019). We find that Chinchilla outperforms both Gopher and GPT-3 on all tasks and
outperforms MT-NLG 530B on all but one task—see Table 8.
On TruthfulQA (Lin et al., 2021), Chinchilla reaches 43.6%, 58.5%, and 66.7% accuracy with
0-shot, 5-shot, and 10-shot respectively. In comparison, Gopher achieved only 29.5% 0-shot and 43.7%
10-shot accuracy. In stark contrast with the findings of Lin et al. (2021), the large improvements
(14.1% in 0-shot accuracy) achieved by Chinchilla suggest that better modelling of the pre-training
data alone can lead to substantial improvements on this benchmark.

12


Relative Improvement
over Gopher

120
100
80
60
40
20
0
crash_blossom
dark_humor_detection
mathematical_induction
logical_args
general_knowledge_json
Human_organs_senses_multiple_choice
formal_fallacies_syllogisms_negation
known_unknowns
navigate
sentence_ambiguity
moral_permissibility
intent_recognition
irony_identification
entailed_polarity
hyperbaton
misconceptions
evaluating_information_essentiality
similarities_abstraction
epistemic_reasoning
fantasy_reasoning
movie_dialog_same_or_different
winowhy
novel_concepts
discourse_marker_prediction
strategyqa
causal_judgment
hindu_knowledge
phrase_relatedness
alignment_questionnaire
reasoning_about_colored_objects
date_understanding
penguins_in_a_table
figure_of_speech_detection
disambiguation_q
implicatures
SNARKS
ruin_names
logical_fallacy_detection
anachronisms
logic_grid_puzzle
riddle_sense
analytic_entailment
question_selection
nonsense_words_grammar
physics_mc
empirical_judgments
sports_understanding
crass_ai
physical_intuition
timedial
implicit_relations
english_proverbs
presuppositions_as_nli
movie_recommendation
understanding_fables
metaphor_boolean
temporal_sequences
logical_sequence
identify_odd_metaphor
gre_reading_comprehension
odd_one_out
analogical_similarity

20

Figure 7 | BIG-bench results compared to Gopher Chinchilla out performs Gopher on all but four
BIG-bench tasks considered. Full results are in Table A7.
4.2.6. Closed-book question answering
Results on closed-book question answering benchmarks are reported in Table 9. On the Natural
Questions dataset (Kwiatkowski et al., 2019), Chinchilla achieves new closed-book SOTA accuracies:
31.5% 5-shot and 35.5% 64-shot, compared to 21% and 28% respectively, for Gopher. On TriviaQA
(Joshi et al., 2017) we show results for both the filtered (previously used in retrieval and open-book
work) and unfiltered set (previously used in large language model evaluations). In both cases,
Chinchilla substantially out performs Gopher. On the filtered version, Chinchilla lags behind the open
book SOTA (Izacard and Grave, 2020) by only 7.9%. On the unfiltered set, Chinchilla outperforms
GPT-3—see Table 9.
4.2.7. Gender bias and toxicity
Large Language Models carry potential risks such as outputting offensive language, propagating
social biases, and leaking private information (Bender et al., 2021; Weidinger et al., 2021). We
expect Chinchilla to carry risks similar to Gopher because Chinchilla is trained on the same data,

HellaSWAG
PIQA
Winogrande
SIQA
BoolQ

Chinchilla

Gopher

GPT-3

MT-NLG 530B

Supervised SOTA

80.8%
81.8%
74.9%
51.3%
83.7%

79.2%
81.8%
70.1%
50.6%
79.3%

78.9%
81.0%
70.2%
60.5%

80.2%
82.0%
73.0%
78.2%

93.9%
90.1%
91.3%
83.2%
91.4%

Table 8 | Zero-shot comparison on Common Sense benchmarks. We show a comparison between
Chinchilla, Gopher, and MT-NLG 530B on various Common Sense benchmarks. We see that Chinchilla
matches or outperforms Gopher and GPT-3 on all tasks. On all but one Chinchilla outperforms the
much larger MT-NLG 530B model.
13


Method

Chinchilla

Gopher

GPT-3

SOTA (open book)

Natural Questions (dev)

0-shot
5-shot
64-shot

16.6%
31.5%
35.5%

10.1%
24.5%
28.2%

14.6%
29.9%

54.4%

TriviaQA (unfiltered, test)

0-shot
5-shot
64-shot

67.0%
73.2%
72.3%

52.8%
63.6%
61.3%

64.3 %
71.2%

-

TriviaQA (filtered, dev)

0-shot
5-shot
64-shot

55.4%
64.1%
64.6%

43.5%
57.0%
57.2%

-

72.5%

Table 9 | Closed-book question answering. For Natural Questions (Kwiatkowski et al., 2019) and
TriviaQA (Joshi et al., 2017), Chinchilla outperforms Gopher in all cases. On Natural Questions,
Chinchilla outperforms GPT-3. On TriviaQA we show results on two different evaluation sets to allow
for comparison to GPT-3 and to open book SOTA (FiD + Distillation (Izacard and Grave, 2020)).
albeit with slightly different relative weights, and because it has a similar architecture. Here, we
examine gender bias (particularly gender and occupation bias) and generation of toxic language. We
select a few common evaluations to highlight potential issues, but stress that our evaluations are not
comprehensive and much work remains to understand, evaluate, and mitigate risks in LLMs.
Gender bias. As discussed in Rae et al. (2021), large language models reflect contemporary and
historical discourse about different groups (such as gender groups) from their training dataset, and
we expect the same to be true for Chinchilla. Here, we test if potential gender and occupation biases
manifest in unfair outcomes on coreference resolutions, using the Winogender dataset (Rudinger
et al., 2018) in a zero-shot setting. Winogender tests whether a model can correctly determine if
a pronoun refers to different occupation words. An unbiased model would correctly predict which
word the pronoun refers to regardless of pronoun gender. We follow the same setup as in Rae et al.
(2021) (described further in Section H.3).
As shown in Table 10, Chinchilla correctly resolves pronouns more frequently than Gopher across
all groups. Interestingly, the performance increase is considerably smaller for male pronouns (increase
of 3.2%) than for female or neutral pronouns (increases of 8.3% and 9.2% respectively). We also
consider gotcha examples, in which the correct pronoun resolution contradicts gender stereotypes
(determined by labor statistics). Again, we see that Chinchilla resolves pronouns more accurately
than Gopher. When breaking up examples by male/female gender and gotcha/not gotcha, the largest
improvement is on female gotcha examples (improvement of 10%). Thus, though Chinchilla uniformly
overcomes gender stereotypes for more coreference examples than Gopher, the rate of improvement
is higher for some pronouns than others, suggesting that the improvements conferred by using a more
compute-optimal model can be uneven.
Sample toxicity. Language models are capable of generating toxic language—including insults,
hate speech, profanities and threats (Gehman et al., 2020; Rae et al., 2021). While toxicity is an
umbrella term, and its evaluation in LMs comes with challenges (Welbl et al., 2021; Xu et al., 2021),
automatic classifier scores can provide an indication for the levels of harmful text that a LM generates.
Rae et al. (2021) found that improving language modelling loss by increasing the number of model
parameters has only a negligible effect on toxic text generation (unprompted); here we analyze
14


All
Male
Female
Neutral

Chinchilla

Gopher

78.3%
71.2%
79.6%
84.2%

71.4%
68.0%
71.3%
75.0%

Male gotcha
Male not gotcha
Female gotcha
Female not gotcha

Chinchilla

Gopher

62.5%
80.0%
76.7%
82.5%

59.2%
76.7%
66.7%
75.8%

Table 10 | Winogender results. Left: Chinchilla consistently resolves pronouns better than Gopher.
Right: Chinchilla performs better on examples which contradict gender stereotypes (gotcha examples).
However, difference in performance across groups suggests Chinchilla exhibits bias.
whether the same holds true for a lower LM loss achieved via more compute-optimal training. Similar
to the protocol of Rae et al. (2021), we generate 25,000 unprompted samples from Chinchilla, and
compare their PerspectiveAPI toxicity score distribution to that of Gopher-generated samples. Several
summary statistics indicate an absence of major differences: the mean (median) toxicity score for
Gopher is 0.081 (0.064), compared to 0.087 (0.066) for Chinchilla, and the 95th percentile scores
are 0.230 for Gopher, compared to 0.238 for Chinchilla. That is, the large majority of generated
samples are classified as non-toxic, and the difference between the models is negligible. In line with
prior findings (Rae et al., 2021), this suggests that toxicity levels in unconditional text generation
are largely independent of the model quality (measured in language modelling loss), i.e. that better
models of the training dataset are not necessarily more toxic.

5. Discussion & Conclusion
The trend so far in large language model training has been to increase the model size, often without
increasing the number of training tokens. The largest dense transformer, MT-NLG 530B, is now
over 3× larger than GPT-3’s 170 billion parameters from just two years ago. However, this model,
as well as the majority of existing large models, have all been trained for a comparable number
of tokens—around 300 billion. While the desire to train these mega-models has led to substantial
engineering innovation, we hypothesize that the race to train larger and larger models is resulting in
models that are substantially underperforming compared to what could be achieved with the same
compute budget.
We propose three predictive approaches towards optimally setting model size and training duration, based on the outcome of over 400 training runs. All three approaches predict that Gopher is
substantially over-sized and estimate that for the same compute budget a smaller model trained on
more data will perform better. We directly test this hypothesis by training Chinchilla, a 70B parameter
model, and show that it outperforms Gopher and even larger models on nearly every measured
evaluation task.
Whilst our method allows us to make predictions on how to scale large models when given
additional compute, there are several limitations. Due to the cost of training large models, we only
have two comparable training runs at large scale (Chinchilla and Gopher), and we do not have
additional tests at intermediate scales. Furthermore, we assume that the efficient computational
frontier can be described by a power-law relationship between the compute budget, model size, and
number of training tokens. However, we observe some concavity in log 𝑁𝑜𝑝𝑡 at high compute budgets
(see Appendix E). This suggests that we may still be overestimating the optimal size of large models.
Finally, the training runs for our analysis have all been trained on less than an epoch of data; future
work may consider the multiple epoch regime. Despite these limitations, the comparison of Chinchilla
to Gopher validates our performance predictions, that have thus enabled training a better (and more
15


lightweight) model at the same compute budget.
Though there has been significant recent work allowing larger and larger models to be trained,
our analysis suggests an increased focus on dataset scaling is needed. Speculatively, we expect that
scaling to larger and larger datasets is only beneficial when the data is high-quality. This calls for
responsibly collecting larger datasets with a high focus on dataset quality. Larger datasets will require
extra care to ensure train-test set overlap is properly accounted for, both in the language modelling
loss but also with downstream tasks. Finally, training for trillions of tokens introduces many ethical
and privacy concerns. Large datasets scraped from the web will contain toxic language, biases, and
private information. With even larger datasets being used, the quantity (if not the frequency) of such
information increases, which makes dataset introspection all the more important. Chinchilla does
suffer from bias and toxicity but interestingly it seems less affected than Gopher. Better understanding
how performance of large language models and toxicity interact is an important future research
question.
While we have applied our methodology towards the training of auto-regressive language models,
we expect that there is a similar trade-off between model size and the amount of data in other
modalities. As training large models is very expensive, choosing the optimal model size and training
steps beforehand is essential. The methods we propose are easy to reproduce in new settings.

6. Acknowledgements
We’d like to thank Jean-baptiste Alayrac, Kareem Ayoub, Chris Dyer, Nando de Freitas, Demis Hassabis,
Geoffrey Irving, Koray Kavukcuoglu, Nate Kushman and Angeliki Lazaridou for useful comments on
the manuscript. We’d like to thank Andy Brock, Irina Higgins, Michela Paganini, Francis Song, and
other colleagues at DeepMind for helpful discussions. We are also very grateful to the JAX and XLA
team for their support and assistance.

References
M. Artetxe, S. Bhosale, N. Goyal, T. Mihaylov, M. Ott, S. Shleifer, X. V. Lin, J. Du, S. Iyer, R. Pasunuru,
G. Anantharaman, X. Li, S. Chen, H. Akin, M. Baines, L. Martin, X. Zhou, P. S. Koura, B. O’Horo,
J. Wang, L. Zettlemoyer, M. Diab, Z. Kozareva, and V. Stoyanov. Efficient Large Scale Language
Modeling with Mixtures of Experts. arXiv:2112.10684, 2021.
E. M. Bender, T. Gebru, A. McMillan-Major, and S. Shmitchell. On the dangers of stochastic parrots:
Can language models be too big? In Proceedings of the 2021 ACM Conference on Fairness,
Accountability, and Transparency, pages 610–623, 2021.
BIG-bench collaboration. Beyond the imitation game: Measuring and extrapolating the capabilities of
language models. In preparation, 2021. URL https://github.com/google/BIG-bench/.
Y. Bisk, R. Zellers, J. Gao, Y. Choi, et al. PIQA: Reasoning about physical commonsense in natural
language. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 34, pages
7432–7439, 2020.
S. Borgeaud, A. Mensch, J. Hoffmann, T. Cai, E. Rutherford, K. Millican, G. van den Driessche, J.-B.
Lespiau, B. Damoc, A. Clark, D. de Las Casas, A. Guy, J. Menick, R. Ring, T. Hennigan, S. Huang,
L. Maggiore, C. Jones, A. Cassirer, A. Brock, M. Paganini, G. Irving, O. Vinyals, S. Osindero,
K. Simonyan, J. W. Rae, E. Elsen, and L. Sifre. Improving language models by retrieving from
trillions of tokens. arXiv 2112.04426, 2021.
16


J. Bradbury, R. Frostig, P. Hawkins, M. J. Johnson, C. Leary, D. Maclaurin, G. Necula, A. Paszke, J. VanderPlas, S. Wanderman-Milne, and Q. Zhang. JAX: composable transformations of Python+NumPy
programs. 2018. URL http://github.com/google/jax.
T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam,
G. Sastry, A. Askell, S. Agarwal, A. Herbert-Voss, G. Krueger, T. Henighan, R. Child, A. Ramesh,
D. Ziegler, J. Wu, C. Winter, C. Hesse, M. Chen, E. Sigler, M. Litwin, S. Gray, B. Chess, J. Clark,
C. Berner, S. McCandlish, A. Radford, I. Sutskever, and D. Amodei. Language models are few-shot
learners. In H. Larochelle, M. Ranzato, R. Hadsell, M. F. Balcan, and H. Lin, editors, Advances
in Neural Information Processing Systems, volume 33, pages 1877–1901. Curran Associates, Inc.,
2020. URL https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb49674
18bfb8ac142f64a-Paper.pdf.
S. Bubeck. Convex Optimization: Algorithms and Complexity. Foundations and Trends in Machine
Learning, 8(3-4):231–357, 2015. URL http://www.nowpublishers.com/article/Detail
s/MAL-050.
A. Clark, D. d. l. Casas, A. Guy, A. Mensch, M. Paganini, J. Hoffmann, B. Damoc, B. Hechtman,
T. Cai, S. Borgeaud, G. v. d. Driessche, E. Rutherford, T. Hennigan, M. Johnson, K. Millican,
A. Cassirer, C. Jones, E. Buchatskaya, D. Budden, L. Sifre, S. Osindero, O. Vinyals, J. Rae, E. Elsen,
K. Kavukcuoglu, and K. Simonyan. Unified scaling laws for routed language models, 2022. URL
https://arxiv.org/abs/2202.01169.
C. Clark, K. Lee, M.-W. Chang, T. Kwiatkowski, M. Collins, and K. Toutanova. Boolq: Exploring
the surprising difficulty of natural yes/no questions. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers), pages 2924–2936, 2019.
N. Du, Y. Huang, A. M. Dai, S. Tong, D. Lepikhin, Y. Xu, M. Krikun, Y. Zhou, A. W. Yu, O. Firat, B. Zoph,
L. Fedus, M. Bosma, Z. Zhou, T. Wang, Y. E. Wang, K. Webster, M. Pellat, K. Robinson, K. MeierHellstern, T. Duke, L. Dixon, K. Zhang, Q. V. Le, Y. Wu, Z. Chen, and C. Cui. Glam: Efficient scaling of
language models with mixture-of-experts, 2021. URL https://arxiv.org/abs/2112.06905.
W. Fedus, B. Zoph, and N. Shazeer. Switch transformers: Scaling to trillion parameter models with
simple and efficient sparsity. arXiv preprint arXiv:2101.03961, 2021.
L. Gao, S. Biderman, S. Black, L. Golding, T. Hoppe, C. Foster, J. Phang, H. He, A. Thite, N. Nabeshima,
S. Presser, and C. Leahy. The Pile: An 800GB dataset of diverse text for language modeling. arXiv
preprint arXiv:2101.00027, 2020.
S. Gehman, S. Gururangan, M. Sap, Y. Choi, and N. A. Smith. RealToxicityPrompts: Evaluating
neural toxic degeneration in language models. In Findings of the Association for Computational
Linguistics: EMNLP 2020, pages 3356–3369, Online, Nov. 2020. Association for Computational
Linguistics. doi: 10.18653/v1/2020.findings-emnlp.301. URL https://aclanthology.org/2
020.findings-emnlp.301.
K. Guu, K. Lee, Z. Tung, P. Pasupat, and M.-W. Chang. REALM: Retrieval-augmented language model
pre-training, 2020.
D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt. Measuring massive
multitask language understanding. arXiv preprint arXiv:2009.03300, 2020.
T. Hennigan, T. Cai, T. Norman, and I. Babuschkin. Haiku: Sonnet for JAX. 2020. URL http:
//github.com/deepmind/dm-haiku.
17


D. Hernandez, J. Kaplan, T. Henighan, and S. McCandlish. Scaling laws for transfer, 2021.
P. J. Huber. Robust Estimation of a Location Parameter. The Annals of Mathematical Statistics, 35
(1):73–101, Mar. 1964. ISSN 0003-4851, 2168-8990. doi: 10.1214/aoms/1177703732. URL

https://projecteuclid.org/journals/annals-of-mathematical-statistics/vol
ume-35/issue-1/Robust-Estimation-of-a-Location-Parameter/10.1214/aoms/11
77703732.full.
G. Izacard and E. Grave. Distilling knowledge from reader to retriever for question answering, 2020.
M. Joshi, E. Choi, D. Weld, and L. Zettlemoyer. TriviaQA: A Large Scale Distantly Supervised Challenge
Dataset for Reading Comprehension. arXiv e-prints, art. arXiv:1705.03551, 2017.
N. P. Jouppi, C. Young, N. Patil, D. Patterson, G. Agrawal, R. Bajwa, S. Bates, S. Bhatia, N. Boden,
A. Borchers, R. Boyle, P.-l. Cantin, C. Chao, C. Clark, J. Coriell, M. Daley, M. Dau, J. Dean, B. Gelb,
T. V. Ghaemmaghami, R. Gottipati, W. Gulland, R. Hagmann, C. R. Ho, D. Hogberg, J. Hu, R. Hundt,
D. Hurt, J. Ibarz, A. Jaffey, A. Jaworski, A. Kaplan, H. Khaitan, D. Killebrew, A. Koch, N. Kumar, S. Lacy,
J. Laudon, J. Law, D. Le, C. Leary, Z. Liu, K. Lucke, A. Lundin, G. MacKean, A. Maggiore, M. Mahony,
K. Miller, R. Nagarajan, R. Narayanaswami, R. Ni, K. Nix, T. Norrie, M. Omernick, N. Penukonda,
A. Phelps, J. Ross, M. Ross, A. Salek, E. Samadiani, C. Severn, G. Sizikov, M. Snelham, J. Souter,
D. Steinberg, A. Swing, M. Tan, G. Thorson, B. Tian, H. Toma, E. Tuttle, V. Vasudevan, R. Walter,
W. Wang, E. Wilcox, and D. H. Yoon. In-datacenter performance analysis of a tensor processing unit.
In Proceedings of the 44th Annual International Symposium on Computer Architecture, ISCA ’17,
page 1–12, New York, NY, USA, 2017. Association for Computing Machinery. ISBN 9781450348928.
doi: 10.1145/3079856.3080246. URL https://doi.org/10.1145/3079856.3080246.
J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu,
and D. Amodei. Scaling laws for neural language models. arXiv preprint arXiv:2001.08361, 2020.
D. P. Kingma and J. Ba. Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980,
2014.
T. Kudo and J. Richardson. SentencePiece: A simple and language independent subword tokenizer
and detokenizer for neural text processing. arXiv preprint arXiv:1808.06226, 2018.
T. Kwiatkowski, J. Palomaki, O. Redfield, M. Collins, A. Parikh, C. Alberti, D. Epstein, I. Polosukhin,
M. Kelcey, J. Devlin, K. Lee, K. N. Toutanova, L. Jones, M.-W. Chang, A. Dai, J. Uszkoreit, Q. Le, and
S. Petrov. Natural questions: a benchmark for question answering research. Transactions of the
Association of Computational Linguistics, 2019.
G. Lai, Q. Xie, H. Liu, Y. Yang, and E. Hovy. RACE: Large-scale ReAding comprehension dataset from
examinations. In Proceedings of the 2017 Conference on Empirical Methods in Natural Language
Processing, pages 785–794, Copenhagen, Denmark, Sept. 2017. Association for Computational
Linguistics. doi: 10.18653/v1/D17-1082. URL https://aclanthology.org/D17-1082.
Y. Levine, N. Wies, O. Sharir, H. Bata, and A. Shashua. The depth-to-width interplay in self-attention.
arXiv preprint arXiv:2006.12467, 2020.
P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W.-t. Yih,
T. Rocktäschel, S. Riedel, and D. Kiela. Retrieval-augmented generation for knowledge-intensive
nlp tasks. In Advances in Neural Information Processing Systems, volume 33, pages 9459–9474,
2020.

18


O. Lieber, O. Sharir, B. Lenz, and Y. Shoham. Jurassic-1: Technical details and evaluation. White
Paper. AI21 Labs, 2021.
S. Lin, J. Hilton, and O. Evans. TruthfulQA: Measuring how models mimic human falsehoods. arXiv
preprint arXiv:2109.07958, 2021.
I. Loshchilov and F. Hutter. Decoupled weight decay regularization. In International Conference on
Learning Representations, 2019. URL https://openreview.net/forum?id=Bkg6RiCqY7.
S. McCandlish, J. Kaplan, D. Amodei, and O. D. Team. An empirical model of large-batch training,
2018.
S. Merity, C. Xiong, J. Bradbury, and R. Socher. Pointer sentinel mixture models. International
Conference on Learning Representations, 2017.
M. Mitchell, S. Wu, A. Zaldivar, P. Barnes, L. Vasserman, B. Hutchinson, E. Spitzer, I. D. Raji, and T. Gebru. Model cards for model reporting. In Proceedings of the conference on fairness, accountability,
and transparency, pages 220–229, 2019.
J. Nocedal. Updating Quasi-Newton Matrices with Limited Storage. Mathematics of Computation,
35(151):773–782, 1980. ISSN 0025-5718. doi: 10.2307/2006193. URL https://www.jstor.
org/stable/2006193.
D. Paperno, G. Kruszewski, A. Lazaridou, Q. N. Pham, R. Bernardi, S. Pezzelle, M. Baroni, G. Boleda,
and R. Fernández. The LAMBADA dataset: Word prediction requiring a broad discourse context,
2016.
J. Rae, S. Borgeaud, T. Cai, K. Millican, J. Hoffmann, F. Song, J. Aslanides, S. Henderson, R. Ring,
S. Young, E. Rutherford, T. Hennigan, J. Menick, A. Cassirer, R. Powell, G. van den Driessche, L. A.
Hendricks, M. Rauh, P.-S. Huang, A. Glaese, J. Welbl, S. Dathathri, S. Huang, J. Uesato, J. Mellor,
I. Higgins, A. Creswell, N. McAleese, A. Wu, E. Elsen, S. Jayakumar, E. Buchatskaya, D. Budden,
E. Sutherland, K. Simonyan, M. Paganini, L. Sifre, L. Martens, X. L. Li, A. Kuncoro, A. Nematzadeh,
E. Gribovskaya, D. Donato, A. Lazaridou, A. Mensch, J.-B. Lespiau, M. Tsimpoukelli, N. Grigorev,
D. Fritz, T. Sottiaux, M. Pajarskas, T. Pohlen, Z. Gong, D. Toyama, C. de Masson d’Autume, Y. Li,
T. Terzi, I. Babuschkin, A. Clark, D. de Las Casas, A. Guy, J. Bradbury, M. Johnson, L. Weidinger,
I. Gabriel, W. Isaac, E. Lockhart, S. Osindero, L. Rimell, C. Dyer, O. Vinyals, K. Ayoub, J. Stanway,
L. Bennett, D. Hassabis, K. Kavukcuoglu, and G. Irving. Scaling language models: Methods, analysis
& insights from training Gopher. arXiv 2112.11446, 2021.
J. W. Rae, A. Potapenko, S. M. Jayakumar, T. P. Lillicrap, K. Choromanski, V. Likhosherstov, D. Dohan,
X. Song, A. Gane, T. Sarlos, et al. Compressive transformers for long-range sequence modelling.
Advances in Neural Information Processing Systems, 33:6154–6158, 2020.
C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y. Zhou, W. Li, and P. J. Liu. Exploring
the limits of transfer learning with a unified text-to-text transformer. Journal of Machine Learning
Research, 21(140):1–67, 2020a. URL http://jmlr.org/papers/v21/20-074.html.
C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y. Zhou, W. Li, and P. J. Liu. Exploring
the limits of transfer learning with a unified text-to-text transformer. Journal of Machine Learning
Research, 21(140):1–67, 2020b.
S. Rajbhandari, J. Rasley, O. Ruwase, and Y. He. Zero: Memory optimizations toward training
trillion parameter models. In SC20: International Conference for High Performance Computing,
Networking, Storage and Analysis, pages 1–16. IEEE, 2020.
19


H. Robbins and S. Monro. A Stochastic Approximation Method. The Annals of Mathematical Statistics,
22(3):400–407, Sept. 1951.
R. Rudinger, J. Naradowsky, B. Leonard, and B. Van Durme. Gender bias in coreference resolution. In Proceedings of the 2018 Conference of the North American Chapter of the Association for
Computational Linguistics: Human Language Technologies, New Orleans, Louisiana, June 2018.
Association for Computational Linguistics.
K. Sakaguchi, R. Le Bras, C. Bhagavatula, and Y. Choi. Winogrande: An adversarial winograd schema
challenge at scale. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 34,
pages 8732–8740, 2020.
M. Sap, H. Rashkin, D. Chen, R. LeBras, and Y. Choi. SocialIQA: Commonsense reasoning about
social interactions. Proceedings of the 2019 Conference on Empirical Methods in Natural Language
Processing, 2019.
C. J. Shallue, J. Lee, J. Antognini, J. Sohl-Dickstein, R. Frostig, and G. E. Dahl. Measuring the effects
of data parallelism on neural network training. arXiv preprint arXiv:1811.03600, 2018.
J. W. Siegel and J. Xu. Approximation rates for neural networks with general activation functions.
Neural Networks, 128:313–321, Aug. 2020. URL https://www.sciencedirect.com/scienc
e/article/pii/S0893608020301891.
S. Smith, M. Patwary, B. Norick, P. LeGresley, S. Rajbhandari, J. Casper, Z. Liu, S. Prabhumoye,
G. Zerveas, V. Korthikanti, E. Zhang, R. Child, R. Y. Aminabadi, J. Bernauer, X. Song, M. Shoeybi,
Y. He, M. Houston, S. Tiwary, and B. Catanzaro. Using Deepspeed and Megatron to Train Megatronturing NLG 530b, A Large-Scale Generative Language Model. arXiv preprint arXiv:2201.11990,
2022.
J. Steinhardt. Updates and lessons from AI forecasting, 2021. URL https://bounded-regret.g
host.io/ai-forecasting/.
Y. Tay, M. Dehghani, J. Rao, W. Fedus, S. Abnar, H. W. Chung, S. Narang, D. Yogatama, A. Vaswani,
and D. Metzler. Scale efficiently: Insights from pre-training and fine-tuning transformers, 2021.
R. Thoppilan, D. D. Freitas, J. Hall, N. Shazeer, A. Kulshreshtha, H.-T. Cheng, A. Jin, T. Bos, L. Baker,
Y. Du, Y. Li, H. Lee, H. S. Zheng, A. Ghafouri, M. Menegali, Y. Huang, M. Krikun, D. Lepikhin,
J. Qin, D. Chen, Y. Xu, Z. Chen, A. Roberts, M. Bosma, Y. Zhou, C.-C. Chang, I. Krivokon, W. Rusch,
M. Pickett, K. Meier-Hellstern, M. R. Morris, T. Doshi, R. D. Santos, T. Duke, J. Soraker, B. Zevenbergen, V. Prabhakaran, M. Diaz, B. Hutchinson, K. Olson, A. Molina, E. Hoffman-John, J. Lee,
L. Aroyo, R. Rajakumar, A. Butryna, M. Lamm, V. Kuzmina, J. Fenton, A. Cohen, R. Bernstein,
R. Kurzweil, B. Aguera-Arcas, C. Cui, M. Croak, E. Chi, and Q. Le. LaMDA: Language models for
dialog applications, 2022.
A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin.
Attention is all you need. In Advances in neural information processing systems, pages 5998–6008,
2017.
L. Weidinger, J. Mellor, M. Rauh, C. Griffin, J. Uesato, P.-S. Huang, M. Cheng, M. Glaese, B. Balle,
A. Kasirzadeh, Z. Kenton, S. Brown, W. Hawkins, T. Stepleton, C. Biles, A. Birhane, J. Haas, L. Rimell,
L. A. Hendricks, W. Isaac, S. Legassick, G. Irving, and I. Gabriel. Ethical and social risks of harm
from language models. arXiv submission, 2021.

20


J. Welbl, A. Glaese, J. Uesato, S. Dathathri, J. Mellor, L. A. Hendricks, K. Anderson, P. Kohli, B. Coppin,
and P.-S. Huang. Challenges in detoxifying language models. In Findings of the Association for
Computational Linguistics: EMNLP 2021, pages 2447–2469, Punta Cana, Dominican Republic,
Nov. 2021. Association for Computational Linguistics. URL https://aclanthology.org/2021.
findings-emnlp.210.
A. Xu, E. Pathak, E. Wallace, S. Gururangan, M. Sap, and D. Klein. Detoxifying language models
risks marginalizing minority voices. In Proceedings of the 2021 Conference of the North American
Chapter of the Association for Computational Linguistics: Human Language Technologies, pages
2390–2397, Online, June 2021. Association for Computational Linguistics. doi: 10.18653/v1/2021
.naacl-main.190. URL https://aclanthology.org/2021.naacl-main.190.
G. Yang, E. J. Hu, I. Babuschkin, S. Sidor, X. Liu, D. Farhi, N. Ryder, J. Pachocki, W. Chen, and J. Gao.
Tuning large neural networks via zero-shot hyperparameter transfer. In A. Beygelzimer, Y. Dauphin,
P. Liang, and J. W. Vaughan, editors, Advances in Neural Information Processing Systems, 2021.
URL https://openreview.net/forum?id=Bx6qKuBM2AD.
R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi. HellaSwag: Can a machine really finish
your sentence? In Proceedings of the 57th Annual Meeting of the Association for Computational
Linguistics, 2019.
G. Zhang, L. Li, Z. Nado, J. Martens, S. Sachdeva, G. Dahl, C. Shallue, and R. B. Grosse. Which
algorithmic choices matter at which batch sizes? insights from a noisy quadratic model. In
H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alché-Buc, E. Fox, and R. Garnett, editors, Advances
in Neural Information Processing Systems, volume 32. Curran Associates, Inc., 2019. URL https:

//proceedings.neurips.cc/paper/2019/file/e0eacd983971634327ae1819ea8b621
4-Paper.pdf.
B. Zoph, I. Bello, S. Kumar, N. Du, Y. Huang, J. Dean, N. Shazeer, and W. Fedus. Designing effective
sparse expert models, 2022.

21


Appendix
A. Training dataset
In Table A1 we show the training dataset makeup used for Chinchilla and all scaling runs. Note that
both the MassiveWeb and Wikipedia subsets are both used for more than one epoch.

MassiveWeb
Books
C4
News
GitHub
Wikipedia

Disk Size

Documents

1.9 TB
2.1 TB
0.75 TB
2.7 TB
3.1 TB
0.001 TB

604M
4M
361M
1.1B
142M
6M

Sampling proportion

Epochs in 1.4T tokens

45% (48%)
30% (27%)
10% (10%)
10% (10%)
4% (3%)
1% (2%)

1.24
0.75
0.77
0.21
0.13
3.40

Table A1 | MassiveText data makeup. For each subset of MassiveText, we list its total disk size, the
number of documents and the sampling proportion used during training—we use a slightly different
distribution than in Rae et al. (2021) (shown in parenthesis). In the rightmost column show the
number of epochs that are used in 1.4 trillion tokens.

B. Optimal cosine cycle length
One key assumption is made on the cosine cycle length and the corresponding learning rate drop
(we use a 10× learning rate decay in line with Rae et al. (2021)).9 We find that setting the cosine
cycle length too much longer than the target number of training steps results in sub-optimally trained
models, as shown in Figure A1. As a result, we assume that an optimally trained model will have the
cosine cycle length correctly calibrated to the maximum number of steps, given the FLOP budget; we
follow this rule in our main analysis.

C. Consistency of scaling results across datasets
We show scaling results from an IsoFLOP (Approach 2) analysis after training on two different datasets:
C4 (Raffel et al., 2020b) and GitHub code (we show results with data from Rae et al. (2021)), results
are shown in Table A2. For both set of experiments using subsets of MassiveText, we use the same
tokenizer as the MassiveText experiments.
We find that the scaling behaviour on these datasets is very similar to what we found on MassiveText,
as shown in Figure A2 and Table A2. This suggests that our results are independent of the dataset as
long as one does not train for more than one epoch.

9 We find the difference between decaying by 10× and decaying to 0.0 (over the same number of steps) to be small,

though decaying by a factor of 10× to be slightly more performant. Decaying by less (5×) is clearly worse.

22


3.00

1.0

Learning Rate/Max LR

Training Loss

C4 Loss

3.00
2.95

2.80

0.2

2.90

2.75
0

2

4

Million Sequences

6

2.85

2.70

8

0

2

4

Million Sequences

6

2.80

8

3.00

1.0

Learning Rate/Max LR

Training Loss
0.0

2.5

5.0

7.5

10.0

Million Sequences

12.5

7.5

10.0

C4 Loss

3.00
2.95
2.90

2.75
2.70

6

3.05

2.80

0.2

4

Million Sequences

3.10

2.85

0.4

2

3.15

2.90

0.6

0

3.20

2.95

0.8

0.0

3.05

2.85

0.4

1.0× num. steps
1.1× num. steps
1.25× num. steps
1.5× num. steps
2.0× num. steps
5.0× num. steps

3.10

2.90

0.6

Cosine Cycle Length

3.15

2.95

0.8

0.0

3.20

2.85
0.0

2.5

5.0

7.5

10.0

Million Sequences

2.80

12.5

0.0

2.5

5.0

Million Sequences

12.5

Figure A1 | Grid over cosine cycle length. We show 6 curves with the cosine cycle length set to 1,
1.1, 1.25, 1.5, 2, and 5× longer than the target number of training steps. When the cosine cycle length
is too long, and the learning rate does not drop appropriately, then performance is impaired. We find
that overestimating the number of training steps beyond 25% leads to clear drops in performance.
We show results where we have set the number of training steps to two different values (top and
bottom).
3.2
3.0

1T

Parameters

2.6
2.4

10B
1B

3B 6B

1e19
1e20
6e20
1e21

GitHub Training Loss

1017

30B

1019

1021

FLOPs

1023

1025

1B

3B 6B

Parameters

1T

100B 59B

30B

10B
1B

1017

10B

1019

10T

1T

1021

1023

1025

1021

1023

1025

FLOPs

1.6T

100B
10B
1B

100M
100M 300M

100B

100M 17
10

Tokens

1B

Parameters

1.3T

1B

100M

Parameters

1e19
1e20
2.2
6e20
1e21
2.0
100M 300M

Tokens

C4 Training Loss

100B 73B

2.8

1.0
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2

10T

1T

1019

1021

FLOPs

1023

1025

100M 17
10

1019

FLOPs

Figure A2 | C4 and GitHub IsoFLOP curves. Using the C4 dataset (Raffel et al., 2020b) and a GitHub
dataset (Rae et al., 2021), we generate 4 IsoFLOP profiles and show the parameter and token count
scaling, as in Figure 3. Scaling coefficients are shown in Table A2.

23


Approach

Coef. 𝑎 where 𝑁𝑜𝑝𝑡 ∝ 𝐶 𝑎

Coef. 𝑏 where 𝐷𝑜𝑝𝑡 ∝ 𝐶 𝑏

C4
GitHub

0.50
0.53

0.50
0.47

Kaplan et al. (2020)

0.73

0.27

Table A2 | Estimated parameter and data scaling with increased training compute on two alternate datasets. The listed values are the exponents, 𝑎 and 𝑏, on the relationship 𝑁𝑜𝑝𝑡 ∝ 𝐶 𝑎 and
𝐷𝑜𝑝𝑡 ∝ 𝐶 𝑏 . Using IsoFLOP profiles, we estimate the scaling on two different datasets.

D. Details on the scaling analyses
D.1. Approach 1: Fixing model sizes and varying training sequences
We use a maximum learning rate of 2 × 10−4 for the smallest models and 1.25 × 10−4 for the largest
models. In all cases, the learning rate drops by a factor of 10× during training, using a cosine schedule.
We make the assumption that the cosine cycle length should be approximately matched to the number
of training steps. We find that when the cosine cycle overshoots the number of training steps by more
than 25%, performance is noticeably degraded—see Figure A1.10 We use Gaussian smoothing with a
window length of 10 steps to smooth the training curve.
D.2. Approach 3: Parametric fitting of the loss
In this section, we first show how Equation (2) can be derived. We repeat the equation below for
clarity,
𝐵
𝐴
+
𝐿ˆ( 𝑁, 𝐷) , 𝐸 +
,
(5)
𝑁𝛼

𝐷𝛽

based on a decomposition of the expected risk between a function approximation term and an
optimisation suboptimality term. We then give details on the optimisation procedure for fitting the
parameters.
Loss decomposition. Formally, we consider the task of predicting the next token 𝑦 ∈ Y based on
the previous tokens in a sequence 𝑥 ∈ Y 𝑠 , with 𝑠 varying from 0 to 𝑠max —the maximum sequence
length. We consider a distribution 𝑃 ∈ D (X × Y) of tokens in Y and their past in X. A predictor
𝑓 : X → D (Y) computes the probability of each token given the past sequence. The Bayes classifier,
𝑓 ★, minimizes the cross-entropy of 𝑓 ( 𝑥 ) with the observed tokens 𝑦 , with expectation taken on the
whole data distribution. We let 𝐿 be the expected risk
𝐿 ( 𝑓 ) , 𝔼[log 𝑓 ( 𝑥 ) 𝑦 ] ,

and set

𝑓★ ,

argmin

𝐿( 𝑓 ) .

(6)

𝑓 ∈ F ( X , D ( Y))

The set of all transformers of size 𝑁 , that we denote H𝑁 , forms a subset of all functions that map
sequences to distributions of tokens X → D (Y). Fitting a transformer of size 𝑁 on the expected risk
𝐿 ( 𝑓 ) amounts to minimizing such risk on a restricted functional space
𝑓 𝑁 , argmin 𝐿 ( 𝑓 ) .

(7)

𝑓 ∈H𝑁

When we observe a dataset ( 𝑥 𝑖 , 𝑦𝑖 ) 𝑖 𝑖 ∈ [1,𝐷 ] of size 𝐷, we do not have access to 𝔼𝑃 , but instead to the
ˆ 𝐷 over the empirical distribution 𝑃ˆ𝐷 . What happens when we are given 𝐷
empirical expectation 𝔼
10 This further emphasises the point of not only determining model size, but also training length before training begins.

24


datapoints that we can only see once, and when we constrain the size of the hypothesis space to be
𝑁 -dimensional ? We are making steps toward minimizing the empirical risk within a finite-dimensional
functional space H𝑁 :
ˆ 𝐷 [log 𝑓 ( 𝑥 ) 𝑦 ] ,
𝐿ˆ𝐷 ( 𝑓 ) , 𝔼

𝑓ˆ𝑁,𝐷 , argmin 𝐿ˆ𝐷 ( 𝑓 ) .

setting

(8)

𝑓 ∈H𝑁

We are never able to obtain 𝑓ˆ𝑁,𝐷 as we typically perform a single epoch over the dataset of size 𝐷.
Instead, be obtain 𝑓¯𝑁,𝐷 , which is the result of applying a certain number of gradient steps based on
the 𝐷 datapoints—the number of steps to perform depends on the gradient batch size, for which we
use well-tested heuristics.
Using the Bayes-classifier 𝑓 ★, the expected-risk minimizer 𝑓𝑁 and the “single-epoch empirical-risk
minimizer” 𝑓¯𝑁,𝐷 , we can finally decompose the loss 𝐿 ( 𝑁, 𝐷) into


𝐿 ( 𝑁, 𝐷) , 𝐿 ( 𝑓¯𝑁,𝐷 ) = 𝐿 ( 𝑓 ★) + 𝐿 ( 𝑓 𝑁 ) − 𝐿 ( 𝑓 ★) + 𝐿 ( 𝑓¯𝑁,𝐷 ) − 𝐿 ( 𝑓 𝑁 ) .
(9)
The loss comprises three terms: the Bayes risk, i.e. the minimal loss achievable for next-token
prediction on the full distribution 𝑃 , a.k.a the “entropy of natural text.”; a functional approximation
term that depends on the size of the hypothesis space; finally, a stochastic approximation term that
captures the suboptimality of minimizing 𝐿ˆ𝐷 instead of 𝐿, and of making a single epoch on the provided
dataset.
Expected forms of the loss terms. In the decomposition (9), the second term depends entirely on
the number of parameters 𝑁 that defines the size of the functional approximation space. On the set
of two-layer neural networks, it is expected to be proportional to 𝑁 11/2 (Siegel and Xu, 2020). Finally,
given that it corresponds to early stopping in stochastic first order methods, the third term should
1
scale as the convergence rate of these methods, which is lower-bounded by 𝐷1/2
(Robbins and Monro,
1951) (and may attain the bound). This convergence rate is expected to be dimension free (see e.g.
Bubeck, 2015, for a review) and depends only on the loss smoothness; hence we assume that the
second term only depends on 𝐷 in (2). Empirically, we find after fitting (2) that
𝐿 ( 𝑁, 𝐷) = 𝐸 +

𝐴
𝑁 0.34

+

𝐵
𝐷0.28

,

(10)

with 𝐸 = 1.69, 𝐴 = 406.4, 𝐵 = 410.7. We note that the parameter/data coefficients are both lower
than 12 ; this is expected for the data-efficiency coefficient (but far from the known lower-bound).
Future models and training approaches should endeavor to increase these coefficients.
Fitting the decomposition to data. We effectively minimize the following problem


∑︁

min
Huber𝛿 LSE 𝑎 − 𝛼 log 𝑁𝑖 , 𝑏 − 𝛽 log 𝐷𝑖 , 𝑒 − log 𝐿𝑖 ,
𝑎,𝑏,𝑒,𝛼,𝛽

(11)

Run 𝑖

where 𝐿𝑆𝐸 is the log-sum-exp operator. We then set 𝐴, 𝐵, 𝐸 = exp( 𝑎) , exp( 𝑏) , exp( 𝑒).
We use the LBFGS algorithm to find local minima of the objective above, started on a grid
of initialisation given by: 𝛼 ∈ {0., 0.5, . . . , 2. }, 𝛽 ∈ {0., 0.5, . . . , 2. }, 𝑒 ∈ {−1., −.5, . . . , 1. }, 𝑎 ∈
{0, 5, . . . , 25}, and 𝑏 ∈ {0, 5, . . . , 25}. We find that the optimal initialisation is not on the boundary of
our initialisation sweep.
We use 𝛿 = 10−3 for the Huber loss. We find that using larger values of 𝛿 pushes the model to
overfit the small compute regime and poorly predict held-out data from larger runs. We find that
using a 𝛿 smaller than 10−3 does not impact the resulting predictions.
25


D.3. Predicted compute optimal frontier for all three methods
For Approaches 2 and 3, we show the estimated model size and number of training tokens for a
variety of compute budgets in Table A3. We plot the predicted number of tokens and parameters for a
variety of FLOP budgets for the three methods in Figure A3.
Approach 2

Approach 3

Parameters

FLOPs

Tokens

FLOPs

Tokens

400 Million
1 Billion
10 Billion
67 Billion
175 Billion
280 Billion
520 Billion
1 Trillion
10 Trillion

1.84e+19
1.20e+20
1.32e+22
6.88e+23
4.54e+24
1.18e+25
4.19e+25
1.59e+26
1.75e+28

7.7 Billion
20.0 Billion
219.5 Billion
1.7 Trillion
4.3 Trillion
7.1 Trillion
13.4 Trillion
26.5 Trillion
292.0 Trillion

2.21e+19
1.62e+20
2.46e+22
1.71e+24
1.26e+24
3.52e+25
1.36e+26
5.65e+26
8.55e+28

9.2 Billion
27.1 Billion
410.1 Billion
4.1 Trillion
12.0 Trillion
20.1 Trillion
43.5 Trillion
94.1 Trillion
1425.5 Trillion

Table A3 | Estimated optimal training FLOPs and training tokens for various model sizes. Analogous to Table 3, we show the model size/token count projections from Approaches 2 and 3 for various
compute budgets.
.
1012

Parameters

1011

Approach 1
Approach 2
Approach 3
Chinchilla
Gopher
GPT-3
Megatron-Turing NLG

1e+26
1e+25
1e+24
1e+23

1010

1e+22
1e+21

109

1e+20
1e+19

108

1e+18
1010

1011

Tokens

1012

1013

Figure A3 | Optimal number of tokens and parameters for a training FLOP budget. For a fixed
FLOP budget, we show the optimal number of tokens and parameters as predicted by Approaches 1,
2, and 3. For an alternate representation, see Figure 1.

D.4. Small-scale comparison to Kaplan et al. (2020)
For 1021 FLOPs, we perform a head-to-head comparison of a model predicted by Approach 1 and
that predicted by Kaplan et al. (2020). For both models, we use a batch size of 0.5M tokens and a
26


maximum learning rate of 1.5 × 10−4 that decays by 10×. From Kaplan et al. (2020), we find that
the optimal model size should be 4.68 billion parameters. From our approach 1, we estimate a 2.86
billion parameter model should be optimal. We train a 4.74 billion parameter and a 2.80 billion
parameter transformer to test this hypothesis, using the same depth-to-width ratio to avoid as many
confounding factors as possible. We find that our predicted model outperforms the model predicted
by Kaplan et al. (2020) as shown in Figure A4.

2.7

2.7

2.6

2.6

2.5

2.5

2.4

2.4

2.3
2.2

Kaplan et al (2020)
Approach 1

Training Loss

2.8

Training Loss

2.8

2.3
0

1

Sequences

2

2.2
1e7

0.0

0.2

0.4

0.6

FLOPs ×1021

0.8

1.0

Figure A4 | Comparison to Kaplan et al. (2020) at 1021 FLOPs. We train 2.80 and 4.74 billion
parameter transformers predicted as optimal for 1021 FLOPs by Approach 1 and by Kaplan et al.
(2020). We find that our prediction results in a more performant model at the end of training.

E. Curvature of the FLOP-loss frontier
We observe that as models increase there is a curvature in the FLOP-minimal loss frontier. This means
that projections from very small models lead to different predictions than those from larger models.
In Figure A5 we show linear fits using the first, middle, and final third of frontier-points. In this work,
we do not take this in to account and we leave this as interesting future work as it suggests that even
smaller models may be optimal for large FLOP budgets.

F. FLOPs computation
We include all training FLOPs, including those contributed to by the embedding matrices, in our
analysis. Note that we also count embeddings matrices in the total parameter count. For large models
the FLOP and parameter contribution of embedding matrices is small. We use a factor of 2 to describe
the multiply accumulate cost. For the forward pass, we consider contributions from:
• Embeddings
– 2 × seq_len × vocab_size × d_model
• Attention (Single Layer)
– Key, query and value projections: 2 × 3 × seq_len × d_model × (key_size × num_heads)
27


10000
5000
2500

4.0
1000

3.5
3.0

500

2.5

250

2.0
1017

1018

1019

1020

FLOPS

1021

Million Parameters

Training loss

6.0
5.5
5.0
4.5

75

1022

Figure A5 | Training curve envelopes. We fit to the first third (orange), the middle third (green),
and the last third (blue) of all points along the loss frontier. We plot only a subset of the points.
– Key @ Query logits: 2 × seq_len × seq_len × (key_size × num_heads)
– Softmax: 3 × num_heads × seq_len × seq_len
– Softmax @ query reductions: 2 × seq_len × seq_len × (key_size × num_heads)
– Final Linear: 2 × seq_len × (key_size × num_heads) × d_model
• Dense Block (Single Layer)
– 2 × seq_len × (d_model × ffw_size + d_model × ffw_size)
• Final Logits
– 2 × seq_len × d_model × vocab_size
• Total forward pass FLOPs: embeddings+num_layers× (total_attention+dense_block) + logits
As in Kaplan et al. (2020) we assume that the backward pass has twice the FLOPs of the forward pass.
We show a comparison between our calculation and that using the common approximation 𝐶 = 6 𝐷𝑁
(Kaplan et al., 2020) where 𝐶 is FLOPs, 𝐷 is the number of training tokens, and 𝑁 is the number of
parameters in Table A4. We find the differences in FLOP calculation to be very small and they do not
impact our analysis. Compared to the results presented in Rae et al. (2021), we use a slightly more
Parameters

num_layers

d_model

ffw_size

num_heads

k/q size

FLOP Ratio (Ours/6 𝑁 𝐷)

73M
305M
552M
1.1B
1.6B
6.8B

10
20
24
26
28
40

640
1024
1280
1792
2048
3584

2560
4096
5120
7168
8192
14336

10
16
10
14
16
28

64
64
128
128
128
128

1.03
1.10
1.08
1.04
1.03
0.99

Table A4 | FLOP comparison. For a variety of different model sizes, we show the ratio of the FLOPs
that we compute per sequence to that using the 6 𝑁 𝐷 approximation.
accurate calculation giving a slightly different value (6.3 × 1023 compared to 5.76 × 1023 ).
28


G. Other differences between Chinchilla and Gopher
Beyond differences in model size and number of training tokens, there are some additional minor
differences between Chinchilla and Gopher. Specifically, Gopher was trained with Adam (Kingma and
Ba, 2014) whereas Chinchilla was trained with AdamW (Loshchilov and Hutter, 2019). Furthermore,
as discussed in Lessons Learned in Rae et al. (2021), Chinchilla stored a higher-precision copy of the
weights in the sharded optimiser state.
We show comparisons of models trained with Adam and AdamW in Figure A6 and Figure A7.
We find that, independent of the learning rate schedule, AdamW trained models outperform models
trained with Adam. In Figure A6 we show a comparison of an 680 million parameter model trained
2.70

2.55
2.50
0

5

10

15

20

Million Sequences

25

30

Training Setup

2.95

Adam w/ High Precision
AdamW w/ High Precision
Adam No High Precision
AdamW No High Precision

2.90
2.85

C4 Loss

Training Loss

2.60

2.45

3.00

Wikitext103 Perplexity

2.65

26
25
24
23
22
21
20
19
18
17

2.80
2.75
2.70
2.65

0

5

10

15

20

Million Sequences

25

2.60

30

0

5

10

15

20

Million Sequences

25

30

Figure A6 | Comparison of other differences. Using an 680 million parameter model, we show a
comparison between the setup used to train Gopher and Chinchilla— the change in optimiser and
using a higher precision copy of the weights in the optimiser state. The setup used for Chinchilla
(orange) clearly outperforms the setup used to train Gopher (green).
2.8

30.0

Wikitext103 Perplexity

0.5

LAMBADA Accuracy

25.0
22.5

C4 Loss

2.6

0.4

20.0

2.5

0.3

17.5

0.2

15.0

2.4
2.3

0.6

27.5

2.7

0.1

12.5
0

25

50

75

100

Million Sequences

125

150

10.0

0

25

50

75

100

Million Sequences

125

150

0.0

0

417M, Adam
417M, AdamW
1.4B, Adam
1.4B, AdamW
25
50
75

100

Million Sequences

125

150

Figure A7 | Adam vs AdamW. For a 417M (blue) and 1.4B model (green), we find that training with
AdamW improves performance over training with Adam.
with and without the higher precision copy of the weights and with Adam/AdamW for comparison.

H. Results
H.1. The Pile
In Table A5 we show the bits-per-byte (bpb) on The Pile (Gao et al., 2020) of Chinchilla, Gopher,
and Jurassic-1. Chinchilla outperforms Gopher on all subsets. Jurassic-1 outperforms Chinchilla on 2
subsets— dm_mathematics and ubuntu_irc.

29


Subset
pile_cc
pubmed_abstracts
stackexchange
github
openwebtext2
arxiv
uspto_backgrounds
freelaw
pubmed_central
dm_mathematics
hackernews
nih_exporter
opensubtitles
europarl
books3
philpapers
gutenberg_pg_19
bookcorpus2
ubuntu_irc

Chinchilla (70B)

Gopher (280B)

Jurassic-1 (170B)

0.667
0.559
0.614
0.337
0.647
0.627
0.526
0.476
0.504
1.111
0.859
0.572
0.871
0.833
0.675
0.656
0.548
0.714
1.026

0.691
0.578
0.641
0.377
0.677
0.662
0.546
0.513
0.525
1.142
0.890
0.590
0.900
0.938
0.712
0.695
0.656
0.741
1.090

0.669
0.587
0.655
0.358
0.680
0.537
0.514
0.579
1.037
0.869
0.590
0.879
0.835
0.742
0.890
0.857

Table A5 | Bits-per-Byte on The Pile. We show the bpb on The Pile for Chinchilla compared to Gopher
and Jurassic-1.
H.2. MMLU
In Table A6 we show the performance of Chinchilla and Gopher on each subset of MMLU.
H.3. Winogender Setup
We follow the same setup as in Rae et al. (2021). To test coreference resolution in Chinchilla, we
input a sentence which includes a pronoun reference (e.g., “The librarian helped the child pick out a
book because {pronoun} liked to encourage reading.”), then measure the probability of the model
completing the sentence “‘{Pronoun}’ refers to the” with different sentence roles (“librarian” and
“child” in this example). Each example is annotated with the correct pronoun resolution (the pronoun
corresponds to the librarian in this example). Each sentence is tested with a female, male, and
gender-neutral pronoun. An unbiased model would correctly predict which word the pronoun refers
to regardless of pronoun gender.
H.4. BIG-bench
In Table A7 we show Chinchilla and Gopher performance on each subset of BIG-bench that we consider.

I. Model Card
We present the Chinchilla model card in Table A8, following the framework presented by Mitchell
et al. (2019).

30


Task

Chinchilla

Gopher

Task

Chinchilla

Gopher

abstract_algebra
astronomy
clinical_knowledge
college_chemistry
college_mathematics
college_physics
conceptual_physics
electrical_engineering
formal_logic
high_school_biology
high_school_computer_science
high_school_geography
high_school_macroeconomics
high_school_microeconomics
high_school_psychology
high_school_us_history
human_aging
international_law
logical_fallacies
management
medical_genetics
moral_disputes
nutrition
prehistory
professional_law
professional_psychology
security_studies
us_foreign_policy
world_religions

31.0
73.0
75.1
51.0
32.0
46.1
67.2
62.1
33.3
80.3
58.0
86.4
70.5
77.7
86.6
83.3
77.6
90.9
80.4
82.5
69.0
77.5
77.1
81.2
56.5
75.7
75.9
92.0
87.7

25.0
65.8
67.2
45.0
37.0
34.3
49.4
60.0
35.7
71.3
54.0
76.8
65.1
66.4
81.8
78.9
66.4
77.7
72.4
77.7
69.0
66.8
69.9
67.6
44.5
68.1
64.9
81.0
84.2

anatomy
business_ethics
college_biology
college_computer_science
college_medicine
computer_security
econometrics
elementary_mathematics
global_facts
high_school_chemistry
high_school_european_history
high_school_gov_and_politics
high_school_mathematics
high_school_physics
high_school_statistics
high_school_world_history
human_sexuality
jurisprudence
machine_learning
marketing
miscellaneous
moral_scenarios
philosophy
professional_accounting
professional_medicine
public_relations
sociology
virology

70.4
72.0
79.9
51.0
66.5
76.0
38.6
41.5
39.0
58.1
78.8
91.2
31.9
36.4
58.8
85.2
86.3
79.6
41.1
89.7
84.5
36.5
79.4
52.1
75.4
73.6
91.0
53.6

56.3
70.0
70.8
49.0
60.1
65.0
43.0
33.6
38.0
47.8
72.1
83.9
23.7
33.8
50.0
75.1
67.2
71.3
41.1
83.3
75.7
40.2
68.8
44.3
64.0
71.8
84.1
47.0

Table A6 | Chinchilla MMLU results. For each subset of MMLU (Hendrycks et al., 2020), we show
Chinchilla’s accuracy compared to Gopher.

Model Details
Organization Developing the Model

DeepMind

Model Date

March 2022

Model Type

Autoregressive Transformer Language Model (Section 4.1 for
details)

Feedback on the Model

{jordanhoffmann, sborgeaud,
amensch,sifre}@deepmind.com
Intended Uses

Primary Intended Uses

The primary use is research on language models, including:
research on the scaling behaviour of language models along
with those listed in Rae et al. (2021).

31


Primary Intended Users

DeepMind researchers. We will not make this model available
publicly.

Out-of-Scope Uses

Uses of the language model for language generation in harmful or deceitful settings. More generally, the model should not
be used for downstream applications without further safety
and fairness mitigations.
Factors

Card Prompts – Relevant Factor

Relevant factors include which language is used. Our model is
trained on English data. Furthermore, in the analysis of models trained on the same corpus in Rae et al. (2021), we found
it has unequal performance when modelling some dialects
(e.g., African American English). Our model is designed for
research. The model should not be used for downstream applications without further analysis on factors in the proposed
downstream application.

Card Prompts – Evaluation Factors

See the results in Rae et al. (2021) which analyzes models
trained on the same text corpus.
Metrics

Model Performance Measures

• Perplexity and bits per byte on language modelling
datasets
• Accuracy on completion tasks, reading comprehension,
MMLU, BIG-bench and fact checking.
• Exact match accuracy for question answering.
• Generation toxicity from Real Toxicity Prompts (RTP)
alongside toxicity classification accuracy.
• Gender and occupation bias. Test include comparing
the probability of generating different gender terms
and the Winogender coreference resolution task.
We principally focus on Chinchilla’s performance compared
to Gopher on text likelihood prediction.

Decision thresholds

N/A

Approaches to Uncertainty and Vari- Due to the costs of training large language models, we did
ability
not train Chinchilla multiple times. However, the breadth
of our evaluation on a range of different task types gives a
reasonable estimate of the overall performance of the model.
Furthermore, the existence of another large model trained
on the same dataset (Gopher) provides a clear point of comparison.
Evaluation Data

32


Datasets
• Language modelling on LAMBADA, Wikitext103 (Merity et al., 2017), C4 (Raffel et al., 2020a), PG-19 (Rae
et al., 2020) and the Pile (Gao et al., 2020).
• Language understanding, real world knowledge,
mathematical and logical reasoning on the Massive
Multitask Language Understanding (MMLU) benchmark (Hendrycks et al., 2020) and on the “Beyond the
Imitation Game Benchmark” (BIG-bench) (BIG-bench
collaboration, 2021).
• Question answering (closed book) on Natural Questions (Kwiatkowski et al., 2019) and TriviaQA (Joshi
et al., 2017).
• Reading comprehension on RACE (Lai et al., 2017)
• Common sense understanding on HellaSwag (Zellers
et al., 2019), PIQA (Bisk et al., 2020), Winogrande (Sakaguchi et al., 2020), SIQA (Sap et al., 2019),
BoolQ (Clark et al., 2019), and TruthfulQA (Lin et al.,
2021).
Motivation

We chose evaluations from Rae et al. (2021) to allow us to
most directly compare to Gopher.

Preprocessing

Input text is tokenized using a SentencePiece tokenizer with
a vocabulary of size 32,000. Unlike the tokenizer used for
Gopher, the tokenizer used for Chinchilla does not perform
NFKC normalization.
Training Data

The same dataset is used as in Rae et al. (2021). Differences in sampling are shown in Table A1.
Quantitative Analyses
Unitary Results

Section 4.2 gives a detailed description of our analysis. Main
take-aways include:
• Our model is capable of outputting toxic language as
measured by the PerspectiveAPI. This is particularly
true when the model is prompted with toxic prompts.
• Gender: Our model emulates stereotypes found in our
dataset, with occupations such as “dietician” and “receptionist” being more associated with women and “carpenter” and “sheriff ” being more associated with men.
• Race/religion/country sentiment: Prompting our
model to discuss some groups leads to sentences with
lower or higher sentiment, likely reflecting text in our
dataset.

33


Intersectional Results

We did not investigate intersectional biases.
Ethical Considerations

Data

The data is the same as described in Rae et al. (2021).

Human Life

The model is not intended to inform decisions about matters
central to human life or flourishing.

Mitigations

We considered filtering the dataset to remove toxic content
but decided against it due to the observation that this can
introduce new biases as studied by Welbl et al. (2021). More
work is needed on mitigation approaches to toxic content and
other types of risks associated with language models, such
as those discussed in Weidinger et al. (2021).

Risks and Harms

The data is collected from the internet, and thus undoubtedly
there is toxic/biased content in our training dataset. Furthermore, it is likely that personal information is also in the
dataset that has been used to train our models. We defer to
the more detailed discussion in Weidinger et al. (2021).

Use Cases

Especially fraught use cases include the generation of factually incorrect information with the intent of distributing
it or using the model to generate racist, sexist or otherwise
toxic text with harmful intent. Many more use cases that
could cause harm exist. Such applications to malicious use
are discussed in detail in Weidinger et al. (2021).

Table A8 | Chinchilla model card. We follow the framework presented in Mitchell et al. (2019).

J. List of trained models
In Table A9 we list the model size and configuration of all models used in this study. Many models
have been trained multiple times, for a different number of training steps.

34


Task

Chinchilla

Gopher

Task

Chinchilla

Gopher

hyperbaton
causal_judgment
formal_fallacies_syllogisms_neg
crash_blossom
discourse_marker_prediction
general_knowledge_json
sports_understanding
implicit_relations
penguins_in_a_table
intent_recognition
reasoning_about_colored_objects
logic_grid_puzzle
timedial
epistemic_reasoning
ruin_names
hindu_knowledge
misconceptions
implicatures
disambiguation_q
known_unknowns
dark_humor_detection
analogical_similarity
sentence_ambiguity
riddle_sense
date_understanding
analytic_entailment
odd_one_out
logical_args
alignment_questionnaire
similarities_abstraction
anachronisms

54.2
57.4
52.1
47.6
13.1
94.3
71.0
49.4
48.7
92.8
59.7
44.0
68.8
60.6
47.1
91.4
65.3
75.0
54.7
65.2
66.2
38.1
71.7
85.7
52.3
67.1
70.9
56.2
91.3
87.0
69.1

51.7
50.8
50.7
63.6
11.7
93.9
54.9
36.4
40.6
88.7
49.2
35.1
50.9
56.4
38.6
80.0
61.7
62.0
45.5
63.6
83.1
17.2
69.1
68.2
44.1
53.0
32.5
59.1
79.2
81.8
56.4

movie_dialog_same_or_diff
winowhy
movie_recommendation
moral_permissibility
strategyqa
nonsense_words_grammar
metaphor_boolean
navigate
presuppositions_as_nli
temporal_sequences
question_selection
logical_fallacy_detection
physical_intuition
physics_mc
identify_odd_metaphor
understanding_fables
logical_sequence
mathematical_induction
fantasy_reasoning
SNARKS
crass_ai
entailed_polarity
irony_identification
evaluating_info_essentiality
phrase_relatedness
novel_concepts
empirical_judgments
figure_of_speech_detection
english_proverbs
Human_organs_senses_mcc
gre_reading_comprehension

54.5
62.5
75.6
57.3
68.3
78.0
93.1
52.6
49.9
32.0
52.6
72.1
79.0
65.5
68.8
60.3
64.1
47.3
69.0
58.6
75.0
94.0
73.0
17.6
94.0
65.6
67.7
63.3
82.4
85.7
53.1

50.7
56.7
50.5
55.1
61.0
61.4
59.3
51.1
34.0
19.0
41.4
58.9
59.7
50.9
38.6
39.6
36.4
57.6
64.1
48.3
56.8
89.5
69.7
16.7
81.8
59.1
52.5
52.7
57.6
84.8
27.3

Table A7 | Chinchilla BIG-bench results. For each subset of BIG-bench (BIG-bench collaboration,
2021), we show Chinchilla and Gopher’s accuracy.

35


Parameters (million)

d_model

ffw_size

kv_size

n_heads

n_layers

44
57
74
90
106
117
140
163
175
196
217
251
278
306
425
489
509
552
587
632
664
724
816
893
1,018
1,143
1,266
1,424
1,429
1,593
1,609
1,731
1,794
2,007
2,283
2,298
2,639
2,980
3,530
3,802
4,084
4,516
6,796
9,293
11,452
12,295
12,569
13,735
14,940
16,183

512
576
640
640
640
768
768
768
896
896
896
1024
1024
1024
1280
1280
1408
1280
1408
1536
1408
1536
1536
1792
1792
1792
2048
2176
2048
2048
2176
2304
2176
2304
2304
2560
2560
2560
2688
2816
2944
3072
3584
4096
4352
4608
4608
4864
4992
5120

2048
2304
2560
2560
2560
3072
3072
3072
3584
3584
3584
4096
4096
4096
5120
5120
5632
5120
5632
6144
5632
6144
6144
7168
7168
7168
8192
8704
8192
8192
8704
9216
8704
9216
9216
10240
10240
10240
10752
11264
11776
12288
14336
16384
17408
18432
18432
19456
19968
20480

64
64
64
64
64
64
64
64
64
64
64
64
64
64
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128
128

8
9
10
10
10
12
12
12
14
14
14
16
16
16
10
10
11
10
11
12
11
12
12
14
14
14
16
17
16
16
17
18
17
18
18
20
20
20
22
22
22
24
28
32
32
36
32
32
32
40

8
9
10
13
16
12
15
18
14
16
18
16
18
20
18
21
18
24
21
19
24
22
25
20
23
26
22
22
25
28
25
24
28
28
32
26
30
34
36
36
36
36
40
42
47
44
47
47
49
47

Table A9 | All models. We list the hyperparameters and size of all models trained as part of this work.
Many shown models have been trained with multiple learning rate schedules/number of training
tokens.

36
~~~~~
