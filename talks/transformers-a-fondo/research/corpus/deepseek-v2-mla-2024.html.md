---
source_file: deepseek-v2-mla-2024.html
source_type: article
ingested_at: 2026-09-22
---

# DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model (DeepSeek-AI, 2024) — arXiv 2405.04434

## Provenance
- Original location: research/raw/deepseek-v2-mla-2024.html
- Format: html (ar5iv render of arXiv 2405.04434, 695 KB)
- Author / source (if known): DeepSeek-AI (technical report)
- Date of original (if known): 2024-05 (v1), 2024-06 (v5)
- Coverage in this record: Abstract; **§2 Architecture in full** (2.1 Multi-Head Latent Attention with all equations 1–19 and Table 1; 2.2 DeepSeekMoE with eq. 20–29: basic architecture, device-limited routing, the three balance losses, token dropping); **Appendix C** (full MLA formulas) and **Appendix D** (ablations MHA/GQA/MQA and MLA vs MHA) verbatim. §1, §3 (pre-training), §4 (alignment), §5, Appendices A, B, E, F, G are summarized in one paragraph below, per orchestrator instruction.

## Key claims
- Model: 236B total parameters, 21B activated per token, 128K context; vs DeepSeek 67B it "saves 42.5% of training costs, reduces the KV cache by 93.3%, and boosts the maximum generation throughput to 5.76 times". Pre-trained on 8.1T tokens, then SFT and RL (GRPO).
- **MLA idea (§2.1.2)**: instead of caching $k_t, v_t$ per head, cache a single low-rank latent $c_t^{KV}=W^{DKV}h_t\in\mathbb{R}^{d_c}$ per token; keys and values are up-projected ($k^C_t=W^{UK}c^{KV}_t$, $v^C_t=W^{UV}c^{KV}_t$). At inference $W^{UK}$ is absorbed into $W^Q$ and $W^{UV}$ into $W^O$, so K and V never need to be materialised. Queries are also low-rank compressed ($d'_c$) to cut activation memory during training.
- **Decoupled RoPE (§2.1.3)**: RoPE is a position-dependent matrix between $W^Q$ and $W^{UK}$, so it blocks the absorption trick ("matrix multiplication does not obey a commutative law"). Fix: carry position in extra small query heads $q^R_{t,i}$ and one **shared** key $k^R_t$ of dimension $d^R_h$, concatenated to the compressed parts; softmax scale becomes $\sqrt{d_h+d^R_h}$ (eq. 14–19).
- **KV cache per token (Table 1)**: MHA $2n_hd_hl$; GQA $2n_gd_hl$; MQA $2d_hl$; MLA $(d_c+d^R_h)l \approx \tfrac{9}{2}d_hl$ with $d_c=4d_h$, $d^R_h=d_h/2$ — "equal to GQA with only 2.25 groups, but its performance is stronger than MHA" (Appendix D.2: MLA beats MHA on the 7B and 16B ablations).
- **DeepSeekMoE (§2.2)**: FFN output $h'_t = u_t + \sum_{i=1}^{N_s}\mathrm{FFN}^{(s)}_i(u_t) + \sum_{i=1}^{N_r} g_{i,t}\mathrm{FFN}^{(r)}_i(u_t)$ with **shared experts** always on and **fine-grained routed experts** gated by top-$K_r$ softmax affinities $s_{i,t}=\mathrm{Softmax}_i(u_t^\top e_i)$ (eq. 20–22). Device-limited routing (at most $M=3$ devices per token), three auxiliary balance losses (expert-level $\alpha_1=0.003$, device-level $\alpha_2=0.05$, communication $\alpha_3=0.02$), and a device-level token-dropping strategy at training time.
- Hyper-parameters (§3.1.2, summarized): 60 layers, hidden 5120, $n_h=128$, $d_h=128$, $d_c=512$, $d'_c=1536$, $d^R_h=64$; all FFNs except the first layer are MoE with 2 shared + 160 routed experts (intermediate 1536), 6 routed experts activated per token; extra RMSNorm after the latent vectors. Ablation (Appendix D.1, 7B dense): MHA > GQA > MQA on benchmarks when heads are made comparable in parameters.
- Summary of omitted sections: §1 motivates economical MoE + efficient inference; §3 describes the 8.1T-token corpus (more Chinese, 12% more than DeepSeek 67B's), training with AdamW, warmup-and-step-decay LR, YaRN for 128K context (needle-in-a-haystack shown), the HAI-LLM framework (16-way pipeline, 8-way expert parallel, ZeRO-1), and benchmark results (MMLU 78.5 base, top open-source at 21B activated); training cost 172.8K GPU hours per trillion tokens on H800; inference throughput > 50K tokens/s with KV cache quantised to 6 bits. §4 covers SFT (1.5M instances) and GRPO reinforcement learning in two stages (reasoning, then human preference), with discussion of the alignment tax. Appendix B presents DeepSeek-V2-Lite (15.7B total, 2.4B activated, 27 layers, 16 heads, $d_c=512$, 2 shared + 64 routed experts, 6 active). Appendices E–G cover data debiasing, extra math/code evals and evaluation formats.

## Definitions and terminology
- **Multi-head Latent Attention (MLA)**: attention with low-rank joint compression of keys and values into a latent vector $c^{KV}_t$ that is the only thing cached.
- **Compressed latent vector**, **down-projection** $W^{DKV}$, **up-projections** $W^{UK}, W^{UV}$, **KV compression dimension** $d_c$, **query compression dimension** $d'_c$.
- **Decoupled RoPE**: separate small rotary query heads $q^R$ and a shared rotary key $k^R$ of per-head dimension $d^R_h$.
- **DeepSeekMoE**: MoE with fine-grained expert segmentation and isolated shared experts; **routed** vs **shared** experts; **token-to-expert affinity** $s_{i,t}$; **centroid** $e_i$; **device-limited routing**; **expert-/device-/communication-level balance losses**; **token-dropping strategy**.
- Notation: $d$ embedding dim, $n_h$ heads, $d_h$ per-head dim, $l$ layers, $n_g$ GQA groups, $N_s$ / $N_r$ shared / routed experts, $K_r$ activated routed experts.

## Evidence and examples
- Table 1 (§2.1.4): KV cache per token by attention mechanism, with capability ratings (MHA strong, GQA moderate, MQA weak, MLA stronger).
- Figure 2: architecture diagram (MLA + DeepSeekMoE); Figure 3: MHA vs GQA vs MQA vs MLA side by side.
- Appendix D, Table 8: MHA/GQA/MQA ablation at 7B; Table 9: MLA vs MHA at 7B and 16B (MLA better on most benchmarks).
- Appendix C: the complete MLA computation (eq. 37–47 in the original), including the RMSNorm on latents.
- Figure 1: MMLU vs activated parameters and the 42.5% / 93.3% / 5.76× savings chart.

## Inconsistencies / open questions
- The ablations compare mechanisms at matched parameter counts by adjusting head counts; the "stronger than MHA" claim is on that footing, not at matched KV-cache size.
- The record deliberately omits the training/alignment chapters; if the deck wants the 128K-context or throughput details, re-run with `force: true` and a wider keep-list.
- MLA's weight absorption is only stated, not derived, in §2.1.2; Appendix C makes it explicit.

## Images / diagrams
Companion folder `deepseek-v2-mla-2024.html/images/` is **empty**: the source is an ar5iv render whose figures are remote assets, and the orchestrator asked for no new fetches. Each figure is listed below with its caption (captions are also inline in the excerpts) so the diagram-illustrator can redraw from the description if a slide needs it.

### Image 1
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 1: (a) MMLU accuracy vs. activated parameters, among different open-source models. (b) Training costs and inference efficiency of DeepSeek 67B (Dense) and DeepSeek-V2.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 2
- Filename: *(not on disk)*
- Provenance: https://ar5iv.labs.arxiv.org/html/2405.04434/assets/deepseekv2.png
- Caption (verbatim): Figure 2: Illustration of the architecture of DeepSeek-V2. MLA ensures efficient inference by significantly reducing the KV cache for generation, and DeepSeekMoE enables training strong models at an economical cost through the sparse architecture.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 3
- Filename: *(not on disk)*
- Provenance: https://ar5iv.labs.arxiv.org/html/2405.04434/assets/dsattn.png
- Caption (verbatim): Figure 3: Simplified illustration of Multi-Head Attention (MHA), Grouped-Query Attention (GQA), Multi-Query Attention (MQA), and Multi-head Latent Attention (MLA). Through jointly compressing the keys and values into a latent vector, MLA significantly reduces the KV cache during inference.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 4
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 1: Comparison of the KV cache per token among different attention mechanisms. $n_{h}$ denotes the number of attention heads, $d_{h}$ denotes the dimension per attention head, $l$ denotes the number of layers, $n_{g}$ denotes the number of groups in GQA, and $d_{c}$ and $d_{h}^{R}$ denote the KV compression dimension and the per-head dimension of the decoupled queries and key in MLA, respectively. The amount of KV cache is measured by the number of elements, regardless of the storage precision. For DeepSeek-V2, $d_{c}$ is set to $4d_{h}$ and $d_{h}^{R}$ is set to $\frac{d_{h}}{2}$. So, its KV cache is equal to GQA with only 2.25 groups, but its performance is stronger than MHA.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 5
- Filename: *(not on disk)*
- Provenance: https://ar5iv.labs.arxiv.org/html/2405.04434/assets/needle_in_a_haystack.png
- Caption (verbatim): Figure 4: Evaluation results on the “Needle In A Haystack” (NIAH) tests. DeepSeek-V2 performs well across all context window lengths up to 128K.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 6
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 2: Comparison among DeepSeek-V2 and other representative open-source models. All models are evaluated in our internal framework and share the same evaluation setting. **Bold** denotes the best and underline denotes the second-best. Scores with a gap smaller than 0.3 are regarded as at the same level. With only 21B activated parameters, DeepSeek-V2 achieves top-tier performance among open-source models.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 7
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 3: Comparison among DeepSeek-V2 Chat (SFT), DeepSeek-V2 Chat (RL), and other representative open-source chat models. Regarding TriviaQA and NaturalQuestions, it is worth noting that chat models, such as LLaMA3 70B Instruct, might not strictly adhere to the format constraints typically specified in the few-shot setting. Consequently, this can lead to underestimation of certain models in our evaluation framework.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 8
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 4: English open-ended conversation evaluations. For AlpacaEval 2.0, we use the length-controlled win rate as the metric.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 9
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 5: AlignBench leaderboard rated by GPT-4-0613. Models are ranked in descending order based on the overall score. Models marked with * represent that we evaluate them through their API service or open-weighted model, instead of referring to the results reported in their original papers. Suffixes of Erniebot-4.0 and Moonshot denote the timestamps when we called their API.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 10
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 6: Performance of DeepSeek-V2-Lite, DeepSeekMoE 16B, and DeepSeek 7B.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 11
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 7: Performance of DeepSeek-V2-Lite Chat, DeepSeekMoE 16B Chat, and DeepSeek 7B Chat.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 12
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 8: Comparison among 7B dense models with MHA, GQA, and MQA, respectively. MHA demonstrates significant advantages over GQA and MQA on hard benchmarks.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 13
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 9: Comparison between MLA and MHA on hard benchmarks. DeepSeek-V2 shows better performance than MHA, but requires a significantly smaller amount of KV cache.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 14
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 10: Three well-educated human annotators conduct independent annotations on 420 moral scenarios from the MMLU Humanity-Moral subset, on which DeepSeek-V2 and its competitive models demonstrate performance inconsistency. Three annotators and the ground-truth label exhibit a low agreement with each other. This indicates that the answers to the Humanity-Moral subset can be contentious according to specific regional cultures.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 15
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 11: SC-Math6 Model Reasoning Level. “R Level” stands for Reasoning Level, “Comp. Score” stands for Comprehensive Score, “Reas. Steps Score” stands for Reasoning Steps Score, and “OvrAcc Score” stands for Overall Accuracy Score.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 16
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 5: Evaluation results on HumanEval and LiveCodeBench. The questions of LiveCodeBench are selected from the period between September 1st, 2023 and April 1st, 2024.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 17
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 12: An example of AGIEval.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 18
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 13: An example of ARC.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 19
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 14: An example of BBH.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 20
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 15: An example of C-Eval.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 21
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 16: An example of C3.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 22
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 17: An example of CCPM.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 23
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 18: An example of CMATH.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 24
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 19: An example of CMMLU.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 25
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 20: An example of CMRC2018.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 26
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 21: An example of DROP.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 27
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 22: An example of CHID.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 28
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 23: An example of CLUEWSC.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 29
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 24: An example of GSM8K.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 30
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 25: An example of HellaSwag.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 31
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 26: An example of HumanEval.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 32
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 27: An example of MATH.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 33
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 28: An example of MBPP.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 34
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 29: An example of MMLU.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 35
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 30: An example of NaturalQuestions.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 36
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 31: An example of OpenBookQA.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 37
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 32: An example of PIQA.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 38
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 33: An example of RACE.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 39
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 34: An example of TriviaQA.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 40
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 35: An example of WinoGrande. Note that there are multiple prefixes and only one completion for WinoGrande, and we choose the predicted prefix with the lowest perplexity of the completion.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 41
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 36: An example of CRUXEval-I.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 42
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 37: An example of CRUXEval-O.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

## Raw / preserved excerpts
\reportnumber

001

**Authors:** DeepSeek-AI (full contributor list in Appendix A of the original, omitted here)

## Abstract


We present DeepSeek-V2, a strong Mixture-of-Experts (MoE) language model characterized by economical training and efficient inference.
It comprises 236B total parameters, of which 21B are activated for each token, and supports a context length of 128K tokens.
DeepSeek-V2 adopts innovative architectures including Multi-head Latent Attention (MLA) and DeepSeekMoE.
MLA guarantees efficient inference through significantly compressing the Key-Value (KV) cache into a latent vector, while DeepSeekMoE enables training strong models at an economical cost through sparse computation.
Compared with DeepSeek 67B, DeepSeek-V2 achieves significantly stronger performance, and meanwhile saves 42.5% of training costs, reduces the KV cache by 93.3%, and boosts the maximum generation throughput to 5.76 times.
We pretrain DeepSeek-V2 on a high-quality and multi-source corpus consisting of 8.1T tokens, and further perform Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) to fully unlock its potential.
Evaluation results show that, even with only 21B activated parameters, DeepSeek-V2 and its chat versions still achieve top-tier performance among open-source models.
The model checkpoints are available at https://github.com/deepseek-ai/DeepSeek-V2.

> **Figure 1: (a) MMLU accuracy vs. activated parameters, among different open-source models. (b) Training costs and inference efficiency of DeepSeek 67B (Dense) and DeepSeek-V2.**



> *[Sections omitted from this record: 1 Introduction. Only the architecture chapter (MLA and DeepSeekMoE) and the two attention appendices are kept in full per orchestrator instruction; the rest is summarized in Key claims]*

## 2 Architecture


By and large, DeepSeek-V2 is still in the Transformer architecture (Vaswani et al. 2017), where each Transformer block consists of an attention module and a Feed-Forward Network (FFN).
However, for both the attention module and the FFN, we design and employ innovative architectures.
For attention, we design MLA, which utilizes low-rank key-value joint compression to eliminate the bottleneck of inference-time key-value cache, thus supporting efficient inference.
For FFNs, we adopt the DeepSeekMoE architecture (Dai et al. 2024), a high-performance MoE architecture that enables training strong models at an economical cost.
An illustration of the architecture of DeepSeek-V2 is presented in Figure 2, and we will introduce the details of MLA and DeepSeekMoE in this section.
For other tiny details (e.g., layer normalization and the activation function in FFNs), unless specifically stated, DeepSeek-V2 follows the settings of DeepSeek 67B (DeepSeek-AI 2024).

### 2.1 Multi-Head Latent Attention: Boosting Inference Efficiency

Conventional Transformer models usually adopts Multi-Head Attention (MHA) (Vaswani et al. 2017), but during generation, its heavy Key-Value (KV) cache will become the bottleneck that limit the inference efficiency.
In order to reduce the KV cache, Multi-Query Attention (MQA) (Shazeer 2019) and Grouped-Query Attention (GQA) (Ainslie et al. 2023) are proposed.
They require a smaller magnitude of KV cache, but their performance does not match MHA (we provide the ablation of MHA, GQA and MQA in Appendix D.1).

For DeepSeek-V2, we design an innovative attention mechanism called Multi-head Latent Attention (MLA).
Equipped with low-rank key-value joint compression, MLA achieves better performance than MHA, but requires a significantly smaller amount of KV cache.
We introduce its architecture in the following, and also provide a comparison between MLA and MHA in Appendix D.2.

#### 2.1.1 Preliminaries: Standard Multi-Head Attention

We first introduce the standard MHA mechanism as background.
Let $d$ be the embedding dimension, $n_{h}$ be the number of attention heads, $d_{h}$ be the dimension per head, and $\mathbf{h}_{t}\in\mathbb{R}^{d}$ be the attention input of the $t$-th token at an attention layer.
Standard MHA first produces $\mathbf{q}_{t},\mathbf{k}_{t},\mathbf{v}_{t}\in\mathbb{R}^{d_{h}n_{h}}$ through three matrices $W^{Q},W^{K},W^{V}\in\mathbb{R}^{d_{h}n_{h}\times d}$, respectively:

$$\displaystyle\mathbf{q}_{t} \displaystyle=W^{Q}\mathbf{h}_{t}, \quad (1) \\
\displaystyle\mathbf{k}_{t} \displaystyle=W^{K}\mathbf{h}_{t}, \quad (2) \\
\displaystyle\mathbf{v}_{t} \displaystyle=W^{V}\mathbf{h}_{t}, \quad (3)$$

Then, $\mathbf{q}_{t},\mathbf{k}_{t},\mathbf{v}_{t}$ will be sliced into $n_{h}$ heads for the multi-head attention computation:

$$\displaystyle[\mathbf{q}_{t,1}; \displaystyle\mathbf{q}_{t,2};...;\mathbf{q}_{t,n_{h}}]=\mathbf{q}_{t}, \quad (4) \\
\displaystyle[\mathbf{k}_{t,1}; \displaystyle\mathbf{k}_{t,2};...;\mathbf{k}_{t,n_{h}}]=\mathbf{k}_{t}, \quad (5) \\
\displaystyle[\mathbf{v}_{t,1}; \displaystyle\mathbf{v}_{t,2};...;\mathbf{v}_{t,n_{h}}]=\mathbf{v}_{t}, \quad (6) \\
\displaystyle\mathbf{o}_{t,i} \displaystyle=\sum_{j=1}^{t}\operatorname{Softmax}_{j}(\frac{\mathbf{q}_{t,i}^{T}\mathbf{k}_{j,i}}{\sqrt{d_{h}}})\mathbf{v}_{j,i}, \quad (7) \\
\displaystyle\mathbf{u}_{t} \displaystyle=W^{O}[\mathbf{o}_{t,1};\mathbf{o}_{t,2};...;\mathbf{o}_{t,n_{h}}], \quad (8)$$

where $\mathbf{q}_{t,i},\mathbf{k}_{t,i},\mathbf{v}_{t,i}\in\mathbb{R}^{d_{h}}$ denote the query, key, and value of the $i$-th attention head, respectively;
$W^{O}\in\mathbb{R}^{d\times d_{h}n_{h}}$ denotes the output projection matrix.
During inference, all keys and values need to be cached to accelerate inference, so MHA needs to cache $2n_{h}d_{h}l$ elements for each token.
In model deployment, this heavy KV cache is a large bottleneck that limits the maximum batch size and sequence length.

> **Figure 3: Simplified illustration of Multi-Head Attention (MHA), Grouped-Query Attention (GQA), Multi-Query Attention (MQA), and Multi-head Latent Attention (MLA). Through jointly compressing the keys and values into a latent vector, MLA significantly reduces the KV cache during inference.**
> (image not fetched: /html/2405.04434/assets/dsattn.png)

#### 2.1.2 Low-Rank Key-Value Joint Compression

The core of MLA is the low-rank joint compression for keys and values to reduce KV cache:

$$\displaystyle\mathbf{c}_{t}^{KV} \displaystyle=W^{DKV}\mathbf{h}_{t}, \quad (9) \\
\displaystyle\mathbf{k}_{t}^{C} \displaystyle=W^{UK}\mathbf{c}_{t}^{KV}, \quad (10) \\
\displaystyle\mathbf{v}_{t}^{C} \displaystyle=W^{UV}\mathbf{c}_{t}^{KV}, \quad (11)$$

where $\mathbf{c}_{t}^{KV}\in\mathbb{R}^{d_{c}}$ is the compressed latent vector for keys and values;
$d_{c}(\ll d_{h}n_{h})$ denotes the KV compression dimension;
$W^{DKV}\in\mathbb{R}^{d_{c}\times d}$ is the down-projection matrix;
and $W^{UK},W^{UV}\in\mathbb{R}^{d_{h}n_{h}\times d_{c}}$ are the up-projection matrices for keys and values, respectively.
During inference, MLA only needs to cache $\mathbf{c}_{t}^{KV}$, so its KV cache has only $d_{c}l$ elements, where $l$ denotes the number of layers.
In addition, during inference, since $W^{UK}$ can be absorbed into $W^{Q}$, and $W^{UV}$ can be absorbed into $W^{O}$, we even do not need to compute keys and values out for attention.
Figure 3 intuitively illustrates how the KV joint compression in MLA reduces the KV cache.

Moreover, in order to reduce the activation memory during training, we also perform low-rank compression for the queries, even if it cannot reduce the KV cache:

$$\displaystyle\mathbf{c}_{t}^{Q} \displaystyle=W^{DQ}\mathbf{h}_{t}, \quad (12) \\
\displaystyle\mathbf{q}_{t}^{C} \displaystyle=W^{UQ}\mathbf{c}_{t}^{Q}, \quad (13)$$

where $\mathbf{c}_{t}^{Q}\in\mathbb{R}^{d_{c}^{\prime}}$ is the compressed latent vector for queries;
$d_{c}^{\prime}(\ll d_{h}n_{h})$ denotes the query compression dimension;
and $W^{DQ}\in\mathbb{R}^{d_{c}^{\prime}\times d},W^{UQ}\in\mathbb{R}^{d_{h}n_{h}\times d_{c}^{\prime}}$ are the down-projection and up-projection matrices for queries, respectively.

#### 2.1.3 Decoupled Rotary Position Embedding

Following DeepSeek 67B (DeepSeek-AI 2024), we intend to use the Rotary Position Embedding (RoPE) (Su et al. 2024) for DeepSeek-V2.
However, RoPE is incompatible with low-rank KV compression.
To be specific, RoPE is position-sensitive for both keys and queries.
If we apply RoPE for the keys $\mathbf{k}_{t}^{C}$, $W^{UK}$ in Equation 10 will be coupled with a position-sensitive RoPE matrix.
In this way, $W^{UK}$ cannot be absorbed into $W^{Q}$ any more during inference, since a RoPE matrix related to the currently generating token will lie between $W^{Q}$ and $W^{UK}$ and matrix multiplication does not obey a commutative law.
As a result, we must recompute the keys for all the prefix tokens during inference, which will significantly hinder the inference efficiency.

As a solution, we propose the decoupled RoPE strategy that uses additional multi-head queries $\mathbf{q}_{t,i}^{R}\in\mathbb{R}^{d_{h}^{R}}$ and a shared key $\mathbf{k}_{t}^{R}\in\mathbb{R}^{d_{h}^{R}}$ to carry RoPE, where $d_{h}^{R}$ denotes the per-head dimension of the decoupled queries and key.
Equipped with the decoupled RoPE strategy, MLA performs the following computation:

$$\displaystyle[\mathbf{q}_{t,1}^{R};\mathbf{q}_{t,2}^{R};...;\mathbf{q}_{t,n_{h}}^{R}]=\mathbf{q}_{t}^{R} \displaystyle=\operatorname{RoPE}({W^{QR}}\mathbf{c}_{t}^{Q}), \quad (14) \\
\displaystyle\mathbf{k}_{t}^{R} \displaystyle=\operatorname{RoPE}({W^{KR}}\mathbf{h}_{t}), \quad (15) \\
\displaystyle\mathbf{q}_{t,i} \displaystyle=[\mathbf{q}_{t,i}^{C};\mathbf{q}_{t,i}^{R}], \quad (16) \\
\displaystyle\mathbf{k}_{t,i} \displaystyle=[\mathbf{k}_{t,i}^{C};\mathbf{k}_{t}^{R}], \quad (17) \\
\displaystyle\mathbf{o}_{t,i} \displaystyle=\sum_{j=1}^{t}\operatorname{Softmax}_{j}(\frac{\mathbf{q}_{t,i}^{T}\mathbf{k}_{j,i}}{\sqrt{d_{h}+d_{h}^{R}}})\mathbf{v}_{j,i}^{C}, \quad (18) \\
\displaystyle\mathbf{u}_{t} \displaystyle=W^{O}[\mathbf{o}_{t,1};\mathbf{o}_{t,2};...;\mathbf{o}_{t,n_{h}}], \quad (19)$$

where $W^{QR}\in\mathbb{R}^{d_{h}^{R}n_{h}\times d_{c}^{\prime}}$ and $W^{KR}\in\mathbb{R}^{d_{h}^{R}\times d}$ are matrices to produce the decouples queries and key, respectively;
$\operatorname{RoPE}(\cdot)$ denotes the operation that applies RoPE matrices;
and $[\cdot;\cdot]$ denotes the concatenation operation.
During inference, the decoupled key should also be cached.
Therefore, DeepSeek-V2 requires a total KV cache containing $(d_{c}+d_{h}^{R})l$ elements.

In order to demonstrate the complete computation process of MLA, we also organize and provide its full formulas in Appendix C.

> **Table 1: Comparison of the KV cache per token among different attention mechanisms. $n_{h}$ denotes the number of attention heads, $d_{h}$ denotes the dimension per attention head, $l$ denotes the number of layers, $n_{g}$ denotes the number of groups in GQA, and $d_{c}$ and $d_{h}^{R}$ denote the KV compression dimension and the per-head dimension of the decoupled queries and key in MLA, respectively. The amount of KV cache is measured by the number of elements, regardless of the storage precision. For DeepSeek-V2, $d_{c}$ is set to $4d_{h}$ and $d_{h}^{R}$ is set to $\frac{d_{h}}{2}$. So, its KV cache is equal to GQA with only 2.25 groups, but its performance is stronger than MHA.**

| **Attention Mechanism** | **KV Cache per Token (# Element)** | **Capability** |
|---|---|---|
| Multi-Head Attention (MHA) | $2n_{h}d_{h}l$ | Strong |
| Grouped-Query Attention (GQA) | $2n_{g}d_{h}l$ | Moderate |
| Multi-Query Attention (MQA) | $2d_{h}l$ | Weak |
| MLA (Ours) | $\penalty\ \penalty\ \penalty\ \penalty\ \penalty\ \penalty\ \penalty\ \penalty\ (d_{c}+d_{h}^{R})l\approx\frac{9}{2}d_{h}l$ | Stronger |

#### 2.1.4 Comparison of Key-Value Cache

We demonstrate a comparison of the KV cache per token among different attention mechanisms in Table 1.
MLA requires only a small amount of KV cache, equal to GQA with only 2.25 groups, but can achieve stronger performance than MHA.

### 2.2 DeepSeekMoE: Training Strong Models at Economical Costs

#### 2.2.1 Basic Architecture

For FFNs, we employ the DeepSeekMoE architecture (Dai et al. 2024).
DeepSeekMoE has two key ideas: segmenting experts into finer granularity for higher expert specialization and more accurate knowledge acquisition, and isolating some shared experts for mitigating knowledge redundancy among routed experts.
With the same number of activated and total expert parameters, DeepSeekMoE can outperform conventional MoE architectures like GShard (Lepikhin et al. 2021) by a large margin.

Let $\mathbf{u}_{t}$ be the FFN input of the $t$-th token, we compute the FFN output $\mathbf{h}_{t}^{\prime}$ as follows:

$$\displaystyle\mathbf{h}_{t}^{\prime} \displaystyle=\mathbf{u}_{t}+\sum_{i=1}^{N_{s}}{\operatorname{FFN}^{(s)}_{i}\left(\mathbf{u}_{t}\right)}+\sum_{i=1}^{N_{r}}{g_{i,t}\operatorname{FFN}^{(r)}_{i}\left(\mathbf{u}_{t}\right)}, \quad (20) \\
\displaystyle g_{i,t} \displaystyle=\begin{cases}s_{i,t},&s_{i,t}\in\operatorname{Topk}(\{s_{j,t}|1\leqslant j\leqslant N_{r}\},K_{r}),\\ 0,&\text{otherwise},\end{cases} \quad (21) \\
\displaystyle s_{i,t} \displaystyle=\operatorname{Softmax}_{i}\left({\mathbf{u}_{t}}^{T}\mathbf{e}_{i}\right), \quad (22)$$

where $N_{s}$ and $N_{r}$ denote the numbers of shared experts and routed experts, respectively;
$\operatorname{FFN}^{(s)}_{i}(\cdot)$ and $\operatorname{FFN}^{(r)}_{i}(\cdot)$ denote the $i$-th shared expert and the $i$-th routed expert, respectively;
$K_{r}$ denotes the number of activated routed experts;
$g_{i,t}$ is the gate value for the $i$-th expert;
$s_{i,t}$ is the token-to-expert affinity;
$\mathbf{e}_{i}$ is the centroid of the $i$-th routed expert in this layer;
and $\operatorname{Topk}(\cdot,K)$ denotes the set comprising $K$ highest scores among the affinity scores calculated for the $t$-th token and all routed experts.

#### 2.2.2 Device-Limited Routing

We design a device-limited routing mechanism to bound MoE-related communication costs.
When expert parallelism is employed, the routed experts will be distributed across multiple devices.
For each token, its MoE-related communication frequency is proportional to the number of devices covered by its target experts.
Due to the fine-grained expert segmentation in DeepSeekMoE, the number of activated experts can be large, so the MoE-related communication will be more costly if we apply expert parallelism.

For DeepSeek-V2, beyond the naive top-K selection of routed experts, we additionally ensure that the target experts of each token will be distributed on at most $M$ devices.
To be specific, for each token, we first select $M$ devices that have experts with the highest affinity scores in them.
Then, we perform top-K selection among experts on these $M$ devices.
In practice, we find that when $M\geqslant 3$, the device-limited routing can achieve a good performance roughly aligned with the unrestricted top-K routing.

#### 2.2.3 Auxiliary Loss for Load Balance

We take the load balance into consideration for automatically learned routing strategies.
Firstly, unbalanced load will raise the risk of routing collapse (Shazeer et al. 2017), preventing some experts being fully trained and utilized.
Secondly, when expert parallelism is employed, unbalanced load will diminish computation efficiency.
During the training of DeepSeek-V2, we design three kinds of auxiliary losses, for controlling expert-level load balance ($\mathcal{L}_{\mathrm{ExpBal}}$), device-level load balance ($\mathcal{L}_{\mathrm{DevBal}}$), and communication balance ($\mathcal{L}_{\mathrm{CommBal}}$), respectively.

##### Expert-Level Balance Loss.

We use an expert-level balance loss (Fedus et al. 2021; Lepikhin et al. 2021) to mitigate the risk of routing collapse:

$$\displaystyle\mathcal{L}_{\mathrm{ExpBal}} \displaystyle=\alpha_{1}\sum_{i=1}^{N_{r}}{f_{i}P_{i}}, \quad (23) \\
\displaystyle f_{i} \displaystyle=\frac{N_{r}}{K_{r}T}\sum_{t=1}^{T}{\mathds{1}(\text{Token $t$ selects Expert $i$})}, \quad (24) \\
\displaystyle P_{i} \displaystyle=\frac{1}{T}\sum_{t=1}^{T}{s_{i,t}}, \quad (25)$$

where $\alpha_{1}$ is a hyper-parameter called expert-level balance factor;
$\mathds{1}(\cdot)$ denotes the indicator function;
and $T$ denotes the number of tokens in a sequence.

##### Device-Level Balance Loss.

In addition to the expert-level balance loss, we additionally design a device-level balance loss to ensure balanced computation across different devices.
In the training process of DeepSeek-V2, we partition all routed experts into $D$ groups $\{\mathcal{E}_{1},\mathcal{E}_{2},...,\mathcal{E}_{D}\}$, and deploy each group on a single device.
The device-level balance loss is computed as follows:

$$\displaystyle\mathcal{L}_{\mathrm{DevBal}} \displaystyle=\alpha_{2}\sum_{i=1}^{D}{f_{i}^{\prime}P_{i}^{\prime}}, \quad (26) \\
\displaystyle f_{i}^{\prime} \displaystyle=\frac{1}{|\mathcal{E}_{i}|}\sum_{j\in\mathcal{E}_{i}}{f_{j}}, \quad (27) \\
\displaystyle P_{i}^{\prime} \displaystyle=\sum_{j\in\mathcal{E}_{i}}{P_{j}}, \quad (28)$$

where $\alpha_{2}$ is a hyper-parameter called device-level balance factor.

##### Communication Balance Loss.

Finally, we introduce a communication balance loss to ensure that the communication of each device is balanced.
Although the device-limited routing mechanism guarantees that the sending communication of each device is bounded, if a certain device receives more tokens than other devices, the practical communication efficiency will also be affected.
In order to mitigate this issue, we design a communication balance loss as follows:

$$\displaystyle\mathcal{L}_{\mathrm{CommBal}} \displaystyle=\alpha_{3}\sum_{i=1}^{D}{f_{i}^{\prime\prime}P_{i}^{\prime\prime}}, \quad (29) \\
\displaystyle f_{i}^{\prime\prime} \displaystyle=\frac{D}{MT}\sum_{t=1}^{T}{\mathds{1}(\text{Token $t$ is sent to Device $i$})}, \quad (30) \\
\displaystyle P_{i}^{\prime\prime} \displaystyle=\sum_{j\in\mathcal{E}_{i}}{P_{j}}, \quad (31)$$

where $\alpha_{3}$ is a hyper-parameter called communication balance factor.
The device-limited routing mechanism operates on the principle of ensuring that each device transmits at most $MT$ hidden states to other devices.
Simultaneously, the communication balance loss is employed to encourage each device to receive around $MT$ hidden states from other devices.
The communication balance loss guarantees a balanced exchange of information among devices, promoting efficient communications.

#### 2.2.4 Token-Dropping Strategy

While balance losses aim to encourage a balanced load, it is important to acknowledge that they cannot guarantee a strict load balance.
In order to further mitigate the computation wastage caused by unbalanced load, we introduce a device-level token-dropping strategy during training.
This approach first computes the average computational budget for each device, which means that the capacity factor for each device is equivalent to 1.0.
Then, inspired by Riquelme et al. 2021, we drop tokens with the lowest affinity scores on each device until reaching the computational budget.
In addition, we ensure that the tokens belonging to approximately 10% of the training sequences will never be dropped.
In this way, we can flexibly decide whether to drop tokens during inference according to the efficiency requirements, and always ensure consistency between training and inference.



> *[Sections omitted from this record: 3 Pre-Training; 4 Alignment; 5 Conclusion, Limitation, and Future Work; Appendix; Appendix A Contributions and Acknowledgments; Appendix B DeepSeek-V2-Lite: A 16B Model Equipped with MLA and DeepSeekMoE. Only the architecture chapter (MLA and DeepSeekMoE) and the two attention appendices are kept in full per orchestrator instruction; the rest is summarized in Key claims]*

## Appendix C Full Formulas of MLA


In order to demonstrate the complete computation process of MLA, we provide its full formulas in the following:

$$\displaystyle\mathbf{c}_{t}^{Q} \displaystyle=W^{DQ}\mathbf{h}_{t}, \quad (37) \\
\displaystyle[\mathbf{q}_{t,1}^{C};\mathbf{q}_{t,2}^{C};...;\mathbf{q}_{t,n_{h}}^{C}]=\mathbf{q}_{t}^{C} \displaystyle=W^{UQ}\mathbf{c}_{t}^{Q}, \quad (38) \\
\displaystyle[\mathbf{q}_{t,1}^{R};\mathbf{q}_{t,2}^{R};...;\mathbf{q}_{t,n_{h}}^{R}]=\mathbf{q}_{t}^{R} \displaystyle=\operatorname{RoPE}({W^{QR}}\mathbf{c}_{t}^{Q}), \quad (39) \\
\displaystyle\mathbf{q}_{t,i} \displaystyle=[\mathbf{q}_{t,i}^{C};\mathbf{q}_{t,i}^{R}], \quad (40) \\
\displaystyle\boxed{\color[rgb]{0,0,1}\mathbf{c}_{t}^{KV}} \displaystyle=W^{DKV}\mathbf{h}_{t}, \quad (41) \\
\displaystyle[\mathbf{k}_{t,1}^{C};\mathbf{k}_{t,2}^{C};...;\mathbf{k}_{t,n_{h}}^{C}]=\mathbf{k}_{t}^{C} \displaystyle=W^{UK}\mathbf{c}_{t}^{KV}, \quad (42) \\
\displaystyle\boxed{\color[rgb]{0,0,1}\mathbf{k}_{t}^{R}} \displaystyle=\operatorname{RoPE}({W^{KR}}\mathbf{h}_{t}), \quad (43) \\
\displaystyle\mathbf{k}_{t,i} \displaystyle=[\mathbf{k}_{t,i}^{C};\mathbf{k}_{t}^{R}], \quad (44) \\
\displaystyle[\mathbf{v}_{t,1}^{C};\mathbf{v}_{t,2}^{C};...;\mathbf{v}_{t,n_{h}}^{C}]=\mathbf{v}_{t}^{C} \displaystyle=W^{UV}\mathbf{c}_{t}^{KV}, \quad (45) \\
\displaystyle\mathbf{o}_{t,i} \displaystyle=\sum_{j=1}^{t}\operatorname{Softmax}_{j}(\frac{\mathbf{q}_{t,i}^{T}\mathbf{k}_{j,i}}{\sqrt{d_{h}+d_{h}^{R}}})\mathbf{v}_{j,i}^{C}, \quad (46) \\
\displaystyle\mathbf{u}_{t} \displaystyle=W^{O}[\mathbf{o}_{t,1};\mathbf{o}_{t,2};...;\mathbf{o}_{t,n_{h}}], \quad (47)$$

where the boxed vectors in blue need to be cached for generation.
During inference, the naive formula needs to recover $\mathbf{k}_{t}^{C}$ and $\mathbf{v}_{t}^{C}$ from $\mathbf{c}_{t}^{KV}$ for attention.
Fortunately, due to the associative law of matrix multiplication, we can absorb $W^{UK}$ into $W^{UQ}$, and $W^{UV}$ into $W^{O}$.
Therefore, we do not need to compute keys and values out for each query.
Through this optimization, we avoid the computational overhead for recomputing $\mathbf{k}_{t}^{C}$ and $\mathbf{v}_{t}^{C}$ during inference.

## Appendix D Ablation of Attention Mechanisms


### D.1 Ablation of MHA, GQA, and MQA

We show the evaluation results for 7B dense models with MHA, GQA, and MQA on four hard benchmarks in Table 8.
All of these three models are trained on 1.33T tokens, and share the same architecture except for the attention mechanisms.
In addition, for a fair comparison, we align the number of parameters of them to around 7B by adjusting the number of layers.
From the table, we can find that MHA demonstrates significant advantages over GQA and MQA on these benchmarks.

> **Table 8: Comparison among 7B dense models with MHA, GQA, and MQA, respectively. MHA demonstrates significant advantages over GQA and MQA on hard benchmarks.**

| **Benchmark (Metric)** | **# Shots** | **Dense 7B** | **Dense 7B** | **Dense 7B** |
|---|---|---|---|---|
| **w/ MQA** | **w/ GQA (8 Groups)** | **w/ MHA** |  |  |
| # Params | - | 7.1B | 6.9B | 6.9B |
| BBH (EM) | 3-shot | 33.2 | 35.6 | **37.0** |
| MMLU (Acc.) | 5-shot | 37.9 | 41.2 | **45.2** |
| C-Eval (Acc.) | 5-shot | 30.0 | 37.7 | **42.9** |
| CMMLU (Acc.) | 5-shot | 34.6 | 38.4 | **43.5** |

### D.2 Comparison Between MLA and MHA

In Table 9, we show the evaluation results for MoE models equipped with MLA and MHA, respectively, on four hard benchmarks.
For a solid conclusion, we train and evaluate models across two scales.
Two small MoE models comprise about 16B total parameters, and we train them on 1.33T tokens.
Two large MoE models comprise about 250B total parameters, and we train them on 420B tokens.
Also, two small MoE models and two large MoE models respectively share the same architecture except for the attention mechanisms.
From the table, we can observe that MLA shows better performance than MHA.
More importantly, MLA requires a significantly smaller amount of KV cache (14% for small MoE models and 4% for large MoE models) than MHA.

> **Table 9: Comparison between MLA and MHA on hard benchmarks. DeepSeek-V2 shows better performance than MHA, but requires a significantly smaller amount of KV cache.**

| **Benchmark (Metric)** | **# Shots** | **Small MoE** | **Small MoE** | **Large MoE** | **Large MoE** |
|---|---|---|---|---|---|
| **w/ MHA** | **w/ MLA** | **w/ MHA** | **w/ MLA** |  |  |
| # Activated Params | - | 2.5B | 2.4B | 25.0B | 21.5B |
| # Total Params | - | 15.8B | 15.7B | 250.8B | 247.4B |
| KV Cache per Token (# Element) | - | 110.6K | 15.6K | 860.2K | 34.6K |
| BBH (EM) | 3-shot | 37.9 | **39.0** | 46.6 | **50.7** |
| MMLU (Acc.) | 5-shot | 48.7 | **50.0** | 57.5 | **59.0** |
| C-Eval (Acc.) | 5-shot | **51.6** | 50.9 | 57.9 | **59.2** |
| CMMLU (Acc.) | 5-shot | 52.3 | **53.4** | 60.7 | **62.5** |



> *[Sections omitted from this record: Appendix E Discussion About Pre-Training Data Debiasing; Appendix F Additional Evaluations on Math and Code; Appendix G Evaluation Formats. Only the architecture chapter (MLA and DeepSeekMoE) and the two attention appendices are kept in full per orchestrator instruction; the rest is summarized in Key claims]*
