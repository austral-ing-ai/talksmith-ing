---
source_file: rope-su-2021.html
source_type: article
ingested_at: 2026-09-22
---

# RoFormer: Enhanced Transformer with Rotary Position Embedding (Su et al., 2021) — arXiv 2104.09864

## Provenance
- Original location: research/raw/rope-su-2021.html
- Format: html (ar5iv render of arXiv 2104.09864, 283 KB)
- Author / source (if known): Su, Lu, Pan, Murtadha, Wen, Liu — Zhuiyi Technology; later published in Neurocomputing (2024)
- Date of original (if known): 2021-04 (v1), revised through 2023
- Coverage in this record: complete main text (§1–5) including the derivations in §3.4, equations as LaTeX, all tables. Bibliography stripped.

## Key claims
- Goal (§3.1): find $f_q, f_k$ such that the attention inner product depends on content and on the *relative* position only: $\langle f_q(x_m,m), f_k(x_n,n)\rangle = g(x_m,x_n,m-n)$ (eq. 11).
- Solution in 2D: multiply the projected vector by $e^{im\theta}$, i.e. rotate it by angle $m\theta$ (eq. 12–13). General $d$ (even): split into $d/2$ planes, each rotated by $m\theta_i$ with $\theta_i = 10000^{-2(i-1)/d}$ (eq. 14–15). Then $q_m^\top k_n = x_m^\top W_q R_{\Theta,n-m} W_k x_n$ (eq. 16): the rotation matrices combine into one that depends only on $n-m$.
- RoPE is **multiplicative** (rotates q and k) rather than additive (summing a position vector to the embedding as in Vaswani et al. and BERT); $R_\Theta$ is orthogonal, which "ensures stability".
- Efficient realisation (§3.4.2): no matrix multiply needed; $R_{\Theta,m}x = x\otimes(\cos m\theta) + \mathrm{rotate\_half}(x)\otimes(\sin m\theta)$ element-wise (eq. 34).
- Properties: **long-term decay** — with the Vaswani base of 10000 the inner product decays as the relative distance grows (§3.4.3, Figure 2); RoPE is compatible with **linear attention** because it acts on q and k before the kernel (§3.3).
- Experiments: better BLEU on WMT14 En-De than the vanilla Transformer (27.5 vs 27.3, Table 1); faster convergence in BERT-style pre-training (Figure 3); comparable/better GLUE (Table 2); Performer + RoPE converges faster (Figure 4); Chinese long-document tasks (Table 4 / 5) where RoFormer handles 1024-token inputs with only 512 pre-training length.
- The paper's own limitations (§4.5.5): no rigorous explanation for why RoPE converges faster than baselines, and the long-term decay proof gives only intuition.

## Definitions and terminology
- **Rotary Position Embedding (RoPE)**: encode absolute position by rotating the query/key vectors, so that relative position appears in the dot product.
- **Absolute position embedding** (eq. 3–6: added to the embedding, sinusoidal or learned) vs **relative position embedding** (Shaw et al., Transformer-XL, T5, DeBERTa: extra terms inside $q^\top k$, eq. 7–10).
- **Rotary matrix** $R^d_{\Theta,m}$ (block-diagonal of 2×2 rotations), $\Theta = \{\theta_i = 10000^{-2(i-1)/d}\}$.
- **RoFormer**: a Transformer (WoBERT-style for Chinese, vanilla for WMT) using RoPE.
- **Long-term decay**: bound on $|\sum_i h_i e^{i(m-n)\theta_i}|$ that decreases with $m-n$ (Abel transformation argument).

## Evidence and examples
- Table 1: WMT14 En-De BLEU, Transformer baseline 27.3 vs RoFormer 27.5.
- Figure 3: MLM training loss of BERT vs RoFormer (faster convergence). Table 2: GLUE (RoFormer better on MRPC, STS-B, QQP; worse on SST-2, QNLI, MNLI).
- Figure 4: Performer with/without RoPE on Enwik8 (faster convergence).
- Tables 4–5: Chinese CAIL2019-SCM long-text task, RoFormer with 1024 input length 69.79 dev / 69.79 test accuracy vs WoBERT 512-limited.
- Figure 2: long-term decay curve of the relative upper bound vs relative distance.

## Inconsistencies / open questions
- RoPE base ($10000$) and its role in context extension (NTK scaling, YaRN) are not covered here; those are later works.
- The GLUE numbers are mixed (RoFormer worse on 3 of 6 tasks); the paper reports this honestly.
- Equation numbering in the ar5iv render matches the arXiv v4 PDF; older citations may refer to different numbers.

## Images / diagrams
Companion folder `rope-su-2021.html/images/` is **empty**: the source is an ar5iv render whose figures are remote assets, and the orchestrator asked for no new fetches. Each figure is listed below with its caption (captions are also inline in the excerpts) so the diagram-illustrator can redraw from the description if a slide needs it.

### Image 1
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 1: Implementation of Rotary Position Embedding(RoPE).
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 2
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 2: Long-term decay of RoPE.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 3
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 1: The proposed RoFormer gives better BLEU scores compared to its baseline alternative Vaswani et al. 2017 on the WMT 2014 English-to-German translation taskBojar et al. 2014.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 4
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 3: Evaluation of RoPE in language modeling pre-training. **Left**: training loss for BERT and RoFormer. **Right**: training loss for PerFormer with and without RoPE.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 5
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 2: Comparing RoFormer and BERT by fine tuning on downstream GLEU tasks.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 6
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 3: Cross-comparison between our RoFormer and other pre-trained models on Chinese data. ’abs’ and ’rel’ annotates absolute position embedding and relative position embedding, respectively.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 7
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 4: Pre-training strategy of RoFormer on Chinese dataset. The training procedure is divided into various consecutive stages. In each stage, we train the model with a specific combination of maximum sequence length and batch size.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 8
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 5: Experiment results on CAIL2019-SCM task. Numbers in the first column denote the maximum cut-off sequence length. The results are presented in terms of percent accuracy.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

## Raw / preserved excerpts
**Authors:** Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, Yunfeng Liu (Zhuiyi Technology)

## Abstract

Position encoding recently has shown effective in the transformer architecture. It enables valuable supervision for dependency modeling between elements at different positions of the sequence. In this paper, we first investigate various methods to integrate positional information into the learning process of transformer-based language models. Then, we propose a novel method named Rotary Position Embedding(RoPE) to effectively leverage the positional information. Specifically, the proposed RoPE encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative position dependency in self-attention formulation. Notably, RoPE enables valuable properties, including the flexibility of sequence length, decaying inter-token dependency with increasing relative distances, and the capability of equipping the linear self-attention with relative position encoding.
Finally, we evaluate the enhanced transformer with rotary position embedding, also called RoFormer, on various long text classification benchmark datasets. Our experiments show that it consistently overcomes its alternatives. Furthermore, we provide a theoretical analysis to explain some experimental results. RoFormer is already integrated into Huggingface: https://huggingface.co/docs/transformers/model_doc/roformer.

**Keywords** Pre-trained Language Models $\cdot$
Position Information Encoding $\cdot$
Pre-training $\cdot$
Natural Language Processing.

## 1 Introduction

The sequential order of words is of great value to natural language understanding. Recurrent neural networks (RRNs) based models encode tokens’ order by recursively computing a hidden state along the time dimension. Convolution neural networks (CNNs) based models (CNNs) Gehring et al. 2017 were typically considered position-agnostic, but recent work Islam et al. 2020 has shown that the commonly used padding operation can implicitly learn position information.
Recently, the pre-trained language models (PLMs), which were built upon the transformer Vaswani et al. 2017, have achieved the state-of-the-art performance of various natural language processing (NLP) tasks, including context representation learning Devlin et al. 2019, machine translation Vaswani et al. 2017, and language modeling Radford et al. 2019, to name a few. Unlike, RRNs and CNNs-based models, PLMs utilize the self-attention mechanism to semantically capture the contextual representation of a given corpus. As a consequence, PLMs achieve a significant improvement in terms of parallelization over RNNs and improve the modeling ability of longer intra-token relations compared to CNNs [footnote: ^1^

A stack of multiple CNN layers can also capture longer intra-token relation, here we only consider single layer setting.] .

It is noteworthy that the self-attention architecture of the current PLMs has shown to be position-agnostic Yun et al. 2020. Following this claim, various approaches have been proposed to encode the position information into the learning process. On one side, generated absolute position encoding through a pre-defined function Vaswani et al. 2017 was added to the contextual representations, while a trainable absolute position encoding Gehring et al. 2017; Devlin et al. 2019; Lan et al. 2020; Clark et al. 2020; Radford et al. 2019; Radford and Narasimhan 2018. On the other side, the previous work Parikh et al. 2016; Shaw et al. 2018; Huang et al. 2018; Dai et al. 2019; Yang et al. 2019; Raffel et al. 2020; Ke et al. 2020; He et al. 2020; Huang et al. 2020 focuses on relative position encoding, which typically encodes the relative position information into the attention mechanism. In addition to these approaches, the authors of Liu et al. 2020 have proposed to model the dependency of position encoding from the perspective of Neural ODE Chen et al. 2018a, and the authors of Wang et al. 2020 have proposed to model the position information in complex space. Despite the effectiveness of these approaches, they commonly add the position information to the context representation and thus render them unsuitable for the linear self-attention architecture.

In this paper, we introduce a novel method, namely Rotary Position Embedding(RoPE), to leverage the positional information into the learning process of PLMS. Specifically, RoPE encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative position dependency in self-attention formulation. Note that the proposed RoPE is prioritized over the existing methods through valuable properties, including the sequence length flexibility, decaying inter-token dependency with increasing relative distances, and the capability of equipping the linear self-attention with relative position encoding.
Experimental results on various long text classification benchmark datasets show that the enhanced transformer with rotary position embedding, namely RoFormer, can give better performance compared to baseline alternatives and thus demonstrates the efficacy of the proposed RoPE.

In brief, our contributions are three-folds as follows:

- We investigated the existing approaches to the relative position encoding and found that they are mostly built based on the idea of the decomposition of adding position encoding to the context representations. We introduce a novel method, namely Rotary Position Embedding(RoPE), to leverage the positional information into the learning process of PLMS. The key idea is to encode relative position by multiplying the context representations with a rotation matrix with a clear theoretical interpretation.
- We study the properties of RoPE and show that it decays with the relative distance increased, which is desired for natural language encoding. We kindly argue that previous relative position encoding-based approaches are not compatible with linear self-attention.
- We evaluate the proposed RoFormer on various long text benchmark datasets. Our experiments show that it consistently achieves better performance compared to its alternatives. Some experiments with pre-trained language models are available on GitHub: https://github.com/ZhuiyiTechnology/roformer.

The remaining of the paper is organized as follows. We establish a formal description of the position encoding problem in self-attention architecture and revisit previous works in Section 2. We then describe the rotary position encoding (RoPE) and study its properties in Section 3. We report experiments in Section 4. Finally, we conclude this paper in Section 5.

## 2 Background and Related Work

### 2.1 Preliminary

Let $\mathbb{S}_{N}=\{w_{i}\}_{i=1}^{N}$ be a sequence of $N$ input tokens with $w_{i}$ being the $i^{th}$ element. The corresponding word embedding of $\mathbb{S}_{N}$ is denoted as $\mathbb{E}_{N}=\{{\boldsymbol{x}}_{i}\}_{i=1}^{N}$, where ${\boldsymbol{x}}_{i}\in\mathbb{R}^{d}$ is the d-dimensional word embedding vector of token $w_{i}$ without position information. The self-attention first incorporates position information to the word embeddings and transforms them into queries, keys, and value representations.

$$\displaystyle{\boldsymbol{q}}_{m} \displaystyle=f_{q}({\boldsymbol{x}}_{m},m) \quad (1) \\
\displaystyle{\boldsymbol{k}}_{n} \displaystyle=f_{k}({\boldsymbol{x}}_{n},n) \\
\displaystyle{\boldsymbol{v}}_{n} \displaystyle=f_{v}({\boldsymbol{x}}_{n},n),$$

where ${\boldsymbol{q}}_{m},{\boldsymbol{k}}_{n}$ and ${\boldsymbol{v}}_{n}$ incorporate the $m^{th}$ and $n^{th}$ positions through $f_{q},f_{k}$ and $f_{v}$, respectively. The query and key values are then used to compute the attention weights, while the output is computed as the weighted sum over the value representation.

$$\displaystyle a_{m,n} \displaystyle=\frac{\exp(\frac{{\boldsymbol{q}}_{m}^{\intercal}{\boldsymbol{k}}_{n}}{\sqrt{d}})}{\sum_{j=1}^{N}\exp(\frac{{\boldsymbol{q}}_{m}^{\intercal}{\boldsymbol{k}}_{j}}{\sqrt{d}})} \quad (2) \\
\displaystyle\mathbf{o}_{m} \displaystyle=\sum_{n=1}^{N}a_{m,n}{\boldsymbol{v}}_{n}$$

The existing approaches of transformer-based position encoding mainly focus on choosing a suitable function to form Equation 1.

### 2.2 Absolute position embedding

A typical choice of Equation 1 is

$$f_{t:t\in\{q,k,v\}}({\boldsymbol{x}}_{i},i):={\boldsymbol{W}}_{t:t\in\{q,k,v\}}({\boldsymbol{x}}_{i}+{\boldsymbol{p}}_{i}), \quad (3)$$

where ${\boldsymbol{p}}_{i}\in\mathbb{R}^{d}$ is a d-dimensional vector depending of the position of token ${\boldsymbol{x}}_{i}$. Previous work Devlin et al. 2019; Lan et al. 2020; Clark et al. 2020; Radford et al. 2019; Radford and Narasimhan 2018 introduced the use of a set of trainable vectors ${\boldsymbol{p}}_{i}\in\{{\boldsymbol{p}}_{t}\}_{t=1}^{L}$, where $L$ is the maximum sequence length. The authors of Vaswani et al. 2017 have proposed to generate ${\boldsymbol{p}}_{i}$ using the sinusoidal function.

$$\begin{cases}{\boldsymbol{p}}_{i,2t}&=\sin(k/10000^{2t/d})\\ {\boldsymbol{p}}_{i,2t+1}&=\cos(k/10000^{2t/d})\end{cases} \quad (4)$$

in which ${\boldsymbol{p}}_{i,2t}$ is the $2t^{th}$ element of the d-dimensional vector ${\boldsymbol{p}}_{i}$. In the next section, we show that our proposed RoPE is related to this intuition from the sinusoidal function perspective. However, instead of directly adding the position to the context representation, RoPE proposes to incorporate the relative position information by multiplying with the sinusoidal functions.

### 2.3 Relative position embedding

The authors of Shaw et al. 2018 applied different settings of Equation 1 as following:

$$\displaystyle f_{q}({\boldsymbol{x}}_{m}):={\boldsymbol{W}}_{q}{\boldsymbol{x}}_{m} \quad (5) \\
\displaystyle f_{k}({\boldsymbol{x}}_{n},n):={\boldsymbol{W}}_{k}({\boldsymbol{x}}_{n}+\tilde{{\boldsymbol{p}}}^{k}_{r}) \\
\displaystyle f_{v}({\boldsymbol{x}}_{n},n):={\boldsymbol{W}}_{v}({\boldsymbol{x}}_{n}+\tilde{{\boldsymbol{p}}}^{v}_{r})$$

where $\tilde{{\boldsymbol{p}}}^{k}_{r},\tilde{{\boldsymbol{p}}}^{v}_{r}\in\mathbb{R}^{d}$ are trainable relative position embeddings. Note that $r=\operatorname{clip}(m-n,r_{\text{min}},r_{\text{max}})$ represents the relative distance between position $m$ and $n$. They clipped the relative distance with the hypothesis that precise relative position information is not useful beyond a certain distance.
Keeping the form of Equation 3, the authors Dai et al. 2019 have proposed to decompose ${\boldsymbol{q}}_{m}^{\intercal}{\boldsymbol{k}}_{n}$ of Equation 2 as

$${\boldsymbol{q}}_{m}^{\intercal}{\boldsymbol{k}}_{n}={\boldsymbol{x}}_{m}^{\intercal}{\boldsymbol{W}}_{q}^{\intercal}{\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n}+{\boldsymbol{x}}_{m}^{\intercal}{\boldsymbol{W}}_{q}^{\intercal}{\boldsymbol{W}}_{k}{\boldsymbol{p}}_{n}+{\boldsymbol{p}}_{m}^{\intercal}{\boldsymbol{W}}_{q}^{\intercal}{\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n}+{\boldsymbol{p}}_{m}^{\intercal}{\boldsymbol{W}}_{q}^{\intercal}{\boldsymbol{W}}_{k}{\boldsymbol{p}}_{n}, \quad (6)$$

the key idea is to replace the absolute position embedding ${\boldsymbol{p}}_{n}$ with its sinusoid-encoded relative counterpart $\tilde{{\boldsymbol{p}}}_{m-n}$, while the absolute position ${\boldsymbol{p}}_{m}$ in the third and fourth term with two trainable vectors $\mathbf{u}$ and $\mathbf{v}$ independent of the query positions. Further, ${\boldsymbol{W}}_{k}$ is distinguished for the content-based and location-based key vectors ${\boldsymbol{x}}_{n}$ and ${\boldsymbol{p}}_{n}$, denoted as ${\boldsymbol{W}}_{k}$ and $\widetilde{{\boldsymbol{W}}}_{k}$, resulting in:

$${\boldsymbol{q}}_{m}^{\intercal}{\boldsymbol{k}}_{n}={\boldsymbol{x}}_{m}^{\intercal}{\boldsymbol{W}}_{q}^{\intercal}{\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n}+{\boldsymbol{x}}_{m}^{\intercal}{\boldsymbol{W}}_{q}^{\intercal}\widetilde{{\boldsymbol{W}}}_{k}\tilde{{\boldsymbol{p}}}_{m-n}+\mathbf{u}^{\intercal}{\boldsymbol{W}}_{q}^{\intercal}{\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n}+\mathbf{v}^{\intercal}{\boldsymbol{W}}_{q}^{\intercal}\widetilde{{\boldsymbol{W}}}_{k}\tilde{{\boldsymbol{p}}}_{m-n} \quad (7)$$

It is noteworthy that the position information in the value term is removed by setting $f_{v}({\boldsymbol{x}}_{j}):={\boldsymbol{W}}_{v}{\boldsymbol{x}}_{j}$. Later work Raffel et al. 2020; He et al. 2020; Ke et al. 2020; Huang et al. 2020 followed these settings by only encoding the relative position information into the attention weights. However, the authors of Raffel et al. 2020 reformed Equation 6 as:

$${\boldsymbol{q}}_{m}^{\intercal}{\boldsymbol{k}}_{n}={\boldsymbol{x}}_{m}^{\intercal}{\boldsymbol{W}}_{q}^{\intercal}{\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n}+b_{i,j} \quad (8)$$

where $b_{i,j}$ is a trainable bias. The authors of Ke et al. 2020 investigated the middle two terms of Equation 6 and found little correlations between absolute positions and words. The authors of Raffel et al. 2020 proposed to model a pair of words or positions using different projection matrices.

$${\boldsymbol{q}}_{m}^{\intercal}{\boldsymbol{k}}_{n}={\boldsymbol{x}}_{m}^{\intercal}{\boldsymbol{W}}_{q}^{\intercal}{\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n}+{\boldsymbol{p}}_{m}^{\intercal}\mathbf{U}_{q}^{\intercal}\mathbf{U}_{k}{\boldsymbol{p}}_{n}+b_{i,j} \quad (9)$$

The authors of He et al. 2020 argued that the relative positions of two tokens could only be fully modeled using the middle two terms of Equation 6. As a consequence, the absolute position embeddings ${\boldsymbol{p}}_{m}$ and ${\boldsymbol{p}}_{n}$ were simply replaced with the relative position embeddings $\tilde{{\boldsymbol{p}}}_{m-n}$:

$${\boldsymbol{q}}_{m}^{\intercal}{\boldsymbol{k}}_{n}={\boldsymbol{x}}_{m}^{\intercal}{\boldsymbol{W}}_{q}^{\intercal}{\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n}+{\boldsymbol{x}}_{m}^{\intercal}{\boldsymbol{W}}_{q}^{\intercal}{\boldsymbol{W}}_{k}\tilde{{\boldsymbol{p}}}_{m-n}+\tilde{{\boldsymbol{p}}}_{m-n}^{\intercal}{\boldsymbol{W}}_{q}^{\intercal}{\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n} \quad (10)$$

A comparison of the four variants of the relative position embeddings Radford and Narasimhan 2018 has shown that the variant similar to Equation 10 is the most efficient among the other three. Generally speaking, all these approaches attempt to modify Equation 6 based on the decomposition of Equation 3 under the self-attention settings in Equation 2, which was originally proposed in Vaswani et al. 2017. They commonly introduced to directly add the position information to the context representations. Unlikely, our approach aims to derive the relative position encoding from Equation 1 under some constraints. Next, we show that the derived approach is more interpretable by incorporating relative position information with the rotation of context representations.

## 3 Proposed approach

In this section, we discuss the proposed rotary position embedding (RoPE). We first formulate the relative position encoding problem in Section 3.1, we then derive the RoPE in Section 3.2 and investigate its properties in Section 3.3.

### 3.1 Formulation

Transformer-based language modeling usually leverages the position information of individual tokens through a self-attention mechanism. As can be observed in Equation 2, ${\boldsymbol{q}}_{m}^{\intercal}{\boldsymbol{k}}_{n}$ typically enables knowledge conveyance between tokens at different positions. In order to incorporate relative position information, we require the inner product of query ${\boldsymbol{q}}_{m}$ and key ${\boldsymbol{k}}_{n}$ to be formulated by a function $g$, which takes only the word embeddings ${\boldsymbol{x}}_{m}$, ${\boldsymbol{x}}_{n}$, and their relative position $m-n$ as input variables. In other words, we hope that the inner product encodes position information only in the relative form:

$$\langle f_{q}({\boldsymbol{x}}_{m},m),f_{k}({\boldsymbol{x}}_{n},n)\rangle=g({\boldsymbol{x}}_{m},{\boldsymbol{x}}_{n},m-n). \quad (11)$$

The ultimate goal is to find an equivalent encoding mechanism to solve the functions $f_{q}({\boldsymbol{x}}_{m},m)$ and $f_{k}({\boldsymbol{x}}_{n},n)$ to conform the aforementioned relation.

### 3.2 Rotary position embedding

#### 3.2.1 A 2D case

We begin with a simple case with a dimension $d=2$. Under these settings, we make use of the geometric property of vectors on a 2D plane and its complex form to prove (refer Section 3.4.1 for more details) that a solution to our formulation Equation 11 is:

$$\displaystyle f_{q}({\boldsymbol{x}}_{m},m) \displaystyle=({\boldsymbol{W}}_{q}{\boldsymbol{x}}_{m})e^{im\theta} \quad (12) \\
\displaystyle f_{k}({\boldsymbol{x}}_{n},n) \displaystyle=({\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n})e^{in\theta} \\
\displaystyle g({\boldsymbol{x}}_{m},{\boldsymbol{x}}_{n},m-n) \displaystyle=\operatorname{Re}[({\boldsymbol{W}}_{q}{\boldsymbol{x}}_{m})({\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n})^{*}e^{i(m-n)\theta}]$$

where $\operatorname{Re}[\cdot]$ is the real part of a complex number and $({\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n})^{*}$ represents the conjugate complex number of $({\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n})$. $\theta\in\mathbb{R}$ is a preset non-zero constant. We can further write $f_{\{q,k\}}$ in a multiplication matrix:

$$f_{\{q,k\}}({\boldsymbol{x}}_{m},m)=\left(\begin{array}[]{cc}\cos{m\theta}&-\sin{m\theta}\\ \sin{m\theta}&\cos{m\theta}\end{array}\right)\left(\begin{array}[]{cc}W^{(11)}_{\{q,k\}}&W^{(12)}_{\{q,k\}}\\ W^{(21)}_{\{q,k\}}&W^{(22)}_{\{q,k\}}\end{array}\right)\left(\begin{array}[]{cc}x^{(1)}_{m}\\ x^{(2)}_{m}\end{array}\right) \quad (13)$$

where $(x^{(1)}_{m},x^{(2)}_{m})$ is ${\boldsymbol{x}}_{m}$ expressed in the 2D coordinates. Similarly, $g$ can be viewed as a matrix and thus enables the solution of formulation in Section 3.1 under the 2D case. Specifically, incorporating the relative position embedding is straightforward: simply rotate the affine-transformed word embedding vector by amount of angle multiples of its position index and thus interprets the intuition behind *Rotary Position Embedding*.

#### 3.2.2 General form

In order to generalize our results in 2D to any ${\boldsymbol{x}}_{i}\in\mathbb{R}^{d}$ where $d$ is even, we divide the d-dimension space into $d/2$ sub-spaces and combine them in the merit of the linearity of the inner product, turning $f_{\{q,k\}}$ into:

$$f_{\{q,k\}}({\boldsymbol{x}}_{m},m)={\boldsymbol{R}}^{d}_{\Theta,m}{\boldsymbol{W}}_{\{q,k\}}{\boldsymbol{x}}_{m} \quad (14)$$

where

$${\boldsymbol{R}}^{d}_{\Theta,m}=\begin{pmatrix}\cos{m\theta_{1}}&-\sin{m\theta_{1}}&0&0&\cdots&0&0\\ \sin{m\theta_{1}}&\cos{m\theta_{1}}&0&0&\cdots&0&0\\ 0&0&\cos{m\theta_{2}}&-\sin{m\theta_{2}}&\cdots&0&0\\ 0&0&\sin{m\theta_{2}}&\cos{m\theta_{2}}&\cdots&0&0\\ \vdots&\vdots&\vdots&\vdots&\ddots&\vdots&\vdots\\ 0&0&0&0&\cdots&\cos{m\theta_{d/2}}&-\sin{m\theta_{d/2}}\\ 0&0&0&0&\cdots&\sin{m\theta_{d/2}}&\cos{m\theta_{d/2}}\end{pmatrix} \quad (15)$$

is the rotary matrix with pre-defined parameters $\Theta=\{\theta_{i}=10000^{-2(i-1)/d},i\in[1,2,...,d/2]\}$. A graphic illustration of RoPE is shown in Figure 1. Applying our RoPE to self-attention in Equation 2, we obtain:

$${\boldsymbol{q}}_{m}^{\intercal}{\boldsymbol{k}}_{n}=({\boldsymbol{R}}^{d}_{\Theta,m}{\boldsymbol{W}}_{q}{\boldsymbol{x}}_{m})^{\intercal}({\boldsymbol{R}}^{d}_{\Theta,n}{\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n})={\boldsymbol{x}}^{\intercal}{\boldsymbol{W}}_{q}R^{d}_{\Theta,n-m}{\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n} \quad (16)$$

where ${\boldsymbol{R}}^{d}_{\Theta,n-m}=({\boldsymbol{R}}^{d}_{\Theta,m})^{\intercal}{\boldsymbol{R}}^{d}_{\Theta,n}$. Note that ${\boldsymbol{R}}^{d}_{\Theta}$ is an orthogonal matrix, which ensures stability during the process of encoding position information. In addition, due to the sparsity of $R^{d}_{\Theta}$, applying matrix multiplication directly as in Equation 16 is not computationally efficient; we provide another realization in theoretical explanation.

In contrast to the additive nature of position embedding method adopted in the previous works, i.e., Equations 3, 4, 5, 6, 7, 8, 9 and 10, our approach is multiplicative. Moreover, RoPE naturally incorporates relative position information through rotation matrix product instead of altering terms in the expanded formulation of additive position encoding when applied with self-attention.

> **Figure 1: Implementation of Rotary Position Embedding(RoPE).**

### 3.3 Properties of RoPE

##### Long-term decay:

Following Vaswani et al. 2017, we set $\theta_{i}=10000^{-2i/d}$. One can prove that this setting provides a long-term decay property (refer to Section 3.4.3 for more details), which means the inner-product will decay when the relative position increase. This property coincides with the intuition that a pair of tokens with a long relative distance should have less connection.

##### RoPE with linear attention:

The self-attention can be rewritten in a more general form.

$$\operatorname{Attention}(\mathbf{Q},\mathbf{K},\mathbf{V})_{m}=\frac{\sum_{n=1}^{N}\operatorname{sim}({\boldsymbol{q}}_{m},{\boldsymbol{k}}_{n}){\boldsymbol{v}}_{n}}{\sum_{n=1}^{N}\operatorname{sim}({\boldsymbol{q}}_{m},{\boldsymbol{k}}_{n})}. \quad (17)$$

The original self-attention chooses $\operatorname{sim}({\boldsymbol{q}}_{m},{\boldsymbol{k}}_{n})=\exp({\boldsymbol{q}}_{m}^{\intercal}{\boldsymbol{k}}_{n}/\sqrt{d})$. Note that the original self-attention should compute the inner product of query and key for every pair of tokens, which has a quadratic complexity $\mathbb{O}(N^{2})$. Follow Katharopoulos et al. 2020, the linear attentions reformulate Equation 17 as

$$\operatorname{Attention}({\boldsymbol{Q}},{\boldsymbol{K}},{\boldsymbol{V}})_{m}=\frac{\sum_{n=1}^{N}\phi({\boldsymbol{q}}_{m})^{\intercal}\varphi({\boldsymbol{k}}_{n}){\boldsymbol{v}}_{n}}{\sum_{n=1}^{N}\phi({\boldsymbol{q}}_{m})^{\intercal}\varphi({\boldsymbol{k}}_{n})}, \quad (18)$$

where $\phi(\cdot),\varphi(\cdot)$ are usually non-negative functions. The authors of Katharopoulos et al. 2020 have proposed $\phi(x)=\varphi(x)=\operatorname{elu}(x)+1$ and first computed the multiplication between keys and values using the associative property of matrix multiplication. A softmax function is used in Shen et al. 2021 to normalize queries and keys separately before the inner product, which is equivalent to $\phi({\boldsymbol{q}}_{i})=\operatorname{softmax}({\boldsymbol{q}}_{i})$ and $\phi({\boldsymbol{k}}_{j})=\exp({\boldsymbol{k}}_{j})$. For more details about linear attention, we encourage readers to refer to original papers. In this section, we focus on discussing incorporating RoPE with Equation 18. Since RoPE injects position information by rotation, which keeps the norm of hidden representations unchanged, we can combine RoPE with linear attention by multiplying the rotation matrix with the outputs of the non-negative functions.

$$\operatorname{Attention}(\mathbf{Q},\mathbf{K},\mathbf{V})_{m}=\frac{\sum_{n=1}^{N}\big({\boldsymbol{R}}^{d}_{\Theta,m}\phi({\boldsymbol{q}}_{m})\big)^{\intercal}\big({\boldsymbol{R}}^{d}_{\Theta,n}\varphi({\boldsymbol{k}}_{n})\big){\boldsymbol{v}}_{n}}{\sum_{n=1}^{N}\phi({\boldsymbol{q}}_{m})^{\intercal}\varphi({\boldsymbol{k}}_{n})}. \quad (19)$$

It is noteworthy that we keep the denominator unchanged to avoid the risk of dividing zero, and the summation in the numerator could contain negative terms. Although the weights for each value ${\boldsymbol{v}}_{i}$ in Equation 19 are not strictly probabilistic normalized, we kindly argue that the computation can still model the importance of values.

### 3.4 Theoretical Explanation

#### 3.4.1 Derivation of RoPE under 2D

Under the case of $d=2$, we consider two-word embedding vectors ${\boldsymbol{x}}_{q}$, ${\boldsymbol{x}}_{k}$ corresponds to query and key and their position $m$ and $n$, respectively. According to eq. 1, their position-encoded counterparts are:

$$\displaystyle{\boldsymbol{q}}_{m} \displaystyle=f_{q}({\boldsymbol{x}}_{q},m), \quad (20) \\
\displaystyle{\boldsymbol{k}}_{n} \displaystyle=f_{k}({\boldsymbol{x}}_{k},n),$$

where the subscripts of ${\boldsymbol{q}}_{m}$ and ${\boldsymbol{k}}_{n}$ indicate the encoded positions information. Assume that there exists a function $g$ that defines the inner product between vectors produced by $f_{\{q,k\}}$:

$${\boldsymbol{q}}^{\intercal}_{m}{\boldsymbol{k}}_{n}=\langle f_{q}({\boldsymbol{x}}_{m},m),f_{k}({\boldsymbol{x}}_{n},n)\rangle=g({\boldsymbol{x}}_{m},{\boldsymbol{x}}_{n},n-m), \quad (21)$$

we further require below initial condition to be satisfied:

$$\displaystyle{\boldsymbol{q}} \displaystyle=f_{q}({\boldsymbol{x}}_{q},0), \quad (22) \\
\displaystyle{\boldsymbol{k}} \displaystyle=f_{k}({\boldsymbol{x}}_{k},0),$$

which can be read as the vectors with empty position information encoded. Given these settings, we attempt to find a solution of $f_{q}$, $f_{k}$. First, we take advantage of the geometric meaning of vector in 2D and its complex counter part, decompose functions in Equations 20 and 21 into:

$$\displaystyle f_{q}({\boldsymbol{x}}_{q},m) \displaystyle=R_{q}({\boldsymbol{x}}_{q},m)e^{i\Theta_{q}({\boldsymbol{x}}_{q},m)}, \quad (23) \\
\displaystyle f_{k}({\boldsymbol{x}}_{k},n) \displaystyle=R_{k}({\boldsymbol{x}}_{k},n)e^{i\Theta_{k}({\boldsymbol{x}}_{k},n)}, \\
\displaystyle g({\boldsymbol{x}}_{q},{\boldsymbol{x}}_{k},n-m) \displaystyle=R_{g}({\boldsymbol{x}}_{q},{\boldsymbol{x}}_{k},n-m)e^{i\Theta_{g}({\boldsymbol{x}}_{q},{\boldsymbol{x}}_{k},n-m)},$$

where $R_{f}$, $R_{g}$ and $\Theta_{f}$, $\Theta_{g}$ are the radical and angular components for $f_{\{q,k\}}$ and $g$, respectively. Plug them into Equation 21, we get the relation:

$$\displaystyle R_{q}({\boldsymbol{x}}_{q},m)R_{k}({\boldsymbol{x}}_{k},n) \displaystyle=R_{g}({\boldsymbol{x}}_{q},{\boldsymbol{x}}_{k},n-m), \quad (24) \\
\displaystyle\Theta_{k}({\boldsymbol{x}}_{k},n)-\Theta_{q}({\boldsymbol{x}}_{q},m) \displaystyle=\Theta_{g}({\boldsymbol{x}}_{q},{\boldsymbol{x}}_{k},n-m),$$

with the corresponding initial condition as:

$$\displaystyle{\boldsymbol{q}} \displaystyle=\|{\boldsymbol{q}}\|e^{i\theta_{q}}=R_{q}({\boldsymbol{x}}_{q},0)e^{i\Theta_{q}({\boldsymbol{x}}_{q},0)}, \quad (25) \\
\displaystyle{\boldsymbol{k}} \displaystyle=\|{\boldsymbol{k}}\|e^{i\theta_{k}}=R_{k}({\boldsymbol{x}}_{k},0)e^{i\Theta_{k}({\boldsymbol{x}}_{k},0)},$$

where $\|{\boldsymbol{q}}\|$, $\|{\boldsymbol{k}}\|$ and $\theta_{q}$, $\theta_{k}$ are the radial and angular part of ${\boldsymbol{q}}$ and ${\boldsymbol{k}}$ on the 2D plane.

Next, we set $m=n$ in Equation 24 and take into account initial conditions in Equation 25:

$$\displaystyle R_{q}({\boldsymbol{x}}_{q},m)R_{k}({\boldsymbol{x}}_{k},m) \displaystyle=R_{g}({\boldsymbol{x}}_{q},{\boldsymbol{x}}_{k},0)=R_{q}({\boldsymbol{x}}_{q},0)R_{k}({\boldsymbol{x}}_{k},0)=\|{\boldsymbol{q}}\|\|{\boldsymbol{k}}\|, \quad (26a) \\
\displaystyle\Theta_{k}({\boldsymbol{x}}_{k},m)-\Theta_{q}({\boldsymbol{x}}_{q},m) \displaystyle=\Theta_{g}({\boldsymbol{x}}_{q},{\boldsymbol{x}}_{k},0)=\Theta_{k}({\boldsymbol{x}}_{k},0)-\Theta_{q}({\boldsymbol{x}}_{q},0)=\theta_{k}-\theta_{q}. \quad (26b)$$

On one hand, from, a straightforward solution of $R_{f}$ could be formed from Equation 26a :

$$\displaystyle R_{q}({\boldsymbol{x}}_{q},m) \displaystyle=R_{q}({\boldsymbol{x}}_{q},0)=\|{\boldsymbol{q}}\| \quad (27) \\
\displaystyle R_{k}({\boldsymbol{x}}_{k},n) \displaystyle=R_{k}({\boldsymbol{x}}_{k},0)=\|{\boldsymbol{k}}\| \\
\displaystyle R_{g}({\boldsymbol{x}}_{q},{\boldsymbol{x}}_{k},n-m) \displaystyle=R_{g}({\boldsymbol{x}}_{q},{\boldsymbol{x}}_{k},0)=\|{\boldsymbol{q}}\|\|{\boldsymbol{k}}\|$$

which interprets the radial functions $R_{q}$, $R_{k}$ and $R_{g}$ are independent from the position information. On the other hand, as can be noticed in Equation 26b, $\Theta_{q}({\boldsymbol{x}}_{q},m)-\theta_{q}=\Theta_{k}({\boldsymbol{x}}_{k},m)-\theta_{k}$ indicates that the angular functions does not dependent on query and key, we set them to $\Theta_{f}:=\Theta_{q}=\Theta_{k}$ and term $\Theta_{f}({\boldsymbol{x}}_{\{q,k\}},m)-\theta_{\{q,k\}}$ is a function of position $m$ and is independent of word embedding ${\boldsymbol{x}}_{\{q,k\}}$, we denote it as $\phi(m)$, yielding:

$$\Theta_{f}({\boldsymbol{x}}_{\{q,k\}},m)=\phi(m)+\theta_{\{q,k\}}, \quad (28)$$

Further, by plugging $n=m+1$ to Equation 24 and consider the above equation, we can get:

$$\phi(m+1)-\phi(m)=\Theta_{g}({\boldsymbol{x}}_{q},{\boldsymbol{x}}_{k},1)+\theta_{q}-\theta_{k}, \quad (29)$$

Since RHS is a constant irrelevant to $m$, $\phi(m)$ with continuous integer inputs produce an arithmetic progression:

$$\phi(m)=m\theta+\gamma, \quad (30)$$

where $\theta,\gamma\in\mathbb{R}$ are constants and $\theta$ is non-zero. To summarize our solutions from Equations 27, 28, 29 and 30:

$$\displaystyle f_{q}({\boldsymbol{x}}_{q},m) \displaystyle=\|{\boldsymbol{q}}\|e^{i\theta_{q}+m\theta+\gamma}={\boldsymbol{q}}e^{i(m\theta+\gamma)}, \quad (31) \\
\displaystyle f_{k}({\boldsymbol{x}}_{k},n) \displaystyle=\|{\boldsymbol{k}}\|e^{i\theta_{k}+n\theta+\gamma}={\boldsymbol{k}}e^{i(n\theta+\gamma)}.$$

Note that we do not apply any constrains to $f_{q}$ and $f_{k}$ of Equation 22, thus $f_{q}({\boldsymbol{x}}_{m},0)$ and $f_{k}({\boldsymbol{x}}_{n},0)$ are left to choose freely. To make our results comparable to Equation 3, we define:

$$\displaystyle{\boldsymbol{q}}=f_{q}({\boldsymbol{x}}_{m},0) \displaystyle={\boldsymbol{W}}_{q}{\boldsymbol{x}}_{n}, \quad (32) \\
\displaystyle{\boldsymbol{k}}=f_{k}({\boldsymbol{x}}_{n},0) \displaystyle={\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n}.$$

Then, we simply set $\gamma=0$ in Equation 31 of the final solution:

$$\displaystyle f_{q}({\boldsymbol{x}}_{m},m) \displaystyle=({\boldsymbol{W}}_{q}{\boldsymbol{x}}_{m})e^{im\theta}, \quad (33) \\
\displaystyle f_{k}({\boldsymbol{x}}_{n},n) \displaystyle=({\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n})e^{in\theta}.$$

#### 3.4.2 Computational efficient realization of rotary matrix multiplication

Taking the advantage of the sparsity of ${\boldsymbol{R}}^{d}_{\Theta,m}$ in Equation 15, a more computational efficient realization of a multiplication of $R^{d}_{\Theta}$ and ${\boldsymbol{x}}\in\mathbb{R}^{d}$ is:

$${\boldsymbol{R}}^{d}_{\Theta,m}{\boldsymbol{x}}=\begin{pmatrix}x_{1}\\ x_{2}\\ x_{3}\\ x_{4}\\ \vdots\\ x_{d-1}\\ x_{d}\end{pmatrix}\otimes\begin{pmatrix}\cos{m\theta_{1}}\\ \cos{m\theta_{1}}\\ \cos{m\theta_{2}}\\ \cos{m\theta_{2}}\\ \vdots\\ \cos{m\theta_{d/2}}\\ \cos{m\theta_{d/2}}\end{pmatrix}+\begin{pmatrix}-x_{2}\\ x_{1}\\ -x_{4}\\ x_{3}\\ \vdots\\ -x_{d}\\ x_{d-1}\end{pmatrix}\otimes\begin{pmatrix}\sin{m\theta_{1}}\\ \sin{m\theta_{1}}\\ \sin{m\theta_{2}}\\ \sin{m\theta_{2}}\\ \vdots\\ \sin{m\theta_{d/2}}\\ \sin{m\theta_{d/2}}\end{pmatrix} \quad (34)$$

#### 3.4.3 Long-term decay of RoPE

We can group entries of vectors ${\boldsymbol{q}}={\boldsymbol{W}}_{q}{\boldsymbol{x}}_{m}$ and ${\boldsymbol{k}}={\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n}$ in pairs, and the inner product of RoPE in Equation 16 can be written as a complex number multiplication.

$$({\boldsymbol{R}}^{d}_{\Theta,m}{\boldsymbol{W}}_{q}{\boldsymbol{x}}_{m})^{\intercal}({\boldsymbol{R}}^{d}_{\Theta,n}{\boldsymbol{W}}_{k}{\boldsymbol{x}}_{n})=\operatorname{Re}\bigg[\sum_{i=0}^{d/2-1}{\boldsymbol{q}}_{[2i:2i+1]}{\boldsymbol{k}}_{[2i:2i+1]}^{*}e^{i(m-n)\theta_{i}}\bigg] \quad (35)$$

where ${\boldsymbol{q}}_{[2i:2i+1]}$ represents the $2i^{th}$ to $(2i+1)^{th}$ entries of ${\boldsymbol{q}}$. Denote $h_{i}={\boldsymbol{q}}_{[2i:2i+1]}{\boldsymbol{k}}_{[2i:2i+1]}^{*}$ and $S_{j}=\sum_{i=0}^{j-1}e^{i(m-n)\theta_{i}}$, and let $h_{d/2}=0$ and $S_{0}=0$, we can rewrite the summation using Abel transformation

$$\sum_{i=0}^{d/2-1}{\boldsymbol{q}}_{[2i:2i+1]}{\boldsymbol{k}}_{[2i:2i+1]}^{*}e^{i(m-n)\theta_{i}}=\sum_{i=0}^{d/2-1}h_{i}(S_{i+1}-S_{i})=-\sum_{i=0}^{d/2-1}S_{i+1}(h_{i+1}-h_{i}). \quad (36)$$

Thus,

$$\displaystyle\bigg|\sum_{i=0}^{d/2-1}{\boldsymbol{q}}_{[2i:2i+1]}{\boldsymbol{k}}_{[2i:2i+1]}^{*}e^{i(m-n)\theta_{i}}\bigg| \displaystyle=\bigg|\sum_{i=0}^{d/2-1}S_{i+1}(h_{i+1}-h_{i})\bigg| \quad (37) \\
\displaystyle\leq\sum_{i=0}^{d/2-1}|S_{i+1}||(h_{i+1}-{h_{i}})| \\
\displaystyle\leq\big(\max_{i}|h_{i+1}-h_{i}|\big)\sum_{i=0}^{d/2-1}|S_{i+1}|$$

Note that the value of $\frac{1}{d/2}\sum_{i=1}^{d/2}|S_{i}|$ decay with the relative distance $m-n$ increases by setting $\theta_{i}=10000^{-2i/d}$, as shown in Figure 2.

> **Figure 2: Long-term decay of RoPE.**

## 4 Experiments and Evaluation

We evaluate the proposed RoFormer on various NLP tasks as follows. We validate the performance of the proposed solution on machine translation task Section 4.1. Then, we compare our RoPE implementation with BERTDevlin et al. 2019 during the pre-training stage in Section 4.2. Based on the pre-trained model, in Section 4.3, we further carry out evaluations across different downstream tasks from GLUE benchmarksSingh et al. 2018. In Addition, we conduct experiments using the proposed RoPE with the linear attention of PerFormer Choromanski et al. 2020 in Section 4.4. By the end, additional tests on Chinese data are included in Section 4.5. All the experiments were run on two cloud severs with 4 x V100 GPUs.

### 4.1 Machine Translation

We first demonstrate the performance of RoFormer on sequence-to-sequence language translation tasks.

#### 4.1.1 Experimental Settings

We choose the standard WMT 2014 English-German datasetBojar et al. 2014, which consists of approximately 4.5 million sentence pairs. We compare to the transformer-based baseline alternative Vaswani et al. 2017.

#### 4.1.2 Implementation details

We carry out some modifications on self-attention layer of the baseline model Vaswani et al. 2017 to enable RoPE to its learning process. We replicate the setup for English-to-German translation with a vocabulary of 37k based on a joint source and target byte pair encoding(BPE)Sennrich et al. 2015. During the evaluation, a single model is obtained by averaging the last 5 checkpoints. The result uses beam search with a beam size of 4 and length penalty 0.6. We implement the experiment in PyTorch in the fairseq toolkit (MIT License)Ott et al. 2019. Our model is optimized with the Adam optimizer using $\beta_{1}=0.9$, $\beta_{2}=0.98$, learning rate is increased linearly from $1e-7$ to $5e-4$ and then decayed proportionally to the inverse square root of the step number. Label smoothing with 0.1 is also adopted. We report the BLEUPapineni et al. 2002 score on the test set as the final metric.

#### 4.1.3 Results

We train the baseline model and our RoFormer under the same settings and report the results in Table 1. As can be seen, our model gives better BLEU scores compared to the baseline Transformer.

> **Table 1: The proposed RoFormer gives better BLEU scores compared to its baseline alternative Vaswani et al. 2017 on the WMT 2014 English-to-German translation taskBojar et al. 2014.**

| Model | BLEU |
|---|---|
| Transformer-baseVaswani et al. 2017 | 27.3 |
| RoFormer | **27.5** |

### 4.2 Pre-training Language Modeling

The second experiment is to validate the performance of our proposal in terms of learning contextual representations. To achieve this, we replace the original sinusoidal position encoding of BERT with our RoPE during the pre-training step.

#### 4.2.1 Experimental Settings

We use the BookCorpus Zhu et al. 2015 and the Wikipedia Corpus Foundation 2021 from Huggingface Datasets library (Apache License 2.0) for pre-training. The corpus is further split into train and validation sets at 8:2 ratio. We use the masked language-modeling (MLM) loss values of the training process as an evaluation metric.
The well-known BERT Devlin et al. 2019 is adopted as our baseline model. Note that we use bert-base-uncased in our experiments.

#### 4.2.2 Implementation details

For RoFormer, we replace the sinusoidal position encoding in the self-attention block of the baseline model with our proposed RoPE and realizes self-attention according to Equation 16. We train both BERT and RoFormer with batch size 64 and maximum sequence length of 512 for 100k steps. AdamW Loshchilov and Hutter 2017 is used as the optimizer with learning rate 1e-5.

#### 4.2.3 Results

The MLM loss during pre-training is shown on the left plot of Figure 3. Compare to the vanilla BERT, RoFormer experiences faster convergence.

> **Figure 3: Evaluation of RoPE in language modeling pre-training. **Left**: training loss for BERT and RoFormer. **Right**: training loss for PerFormer with and without RoPE.**

### 4.3 Fine-tuning on GLUE tasks

Consistent with the previous experiments, we fine-tune the weights of our pre-trained RoFormer across various GLUE tasks in order to evaluate its generalization ability on the downstream NLP tasks.

#### 4.3.1 Experimental Settings

We look at several datasets from GLUE, i.e. MRPC Dolan and Brockett 2005, SST-2 Socher et al. 2013, QNLI Rajpurkar et al. 2016, STS-B Al-Natsheh 2017, QQP Chen et al. 2018b and MNLI Williams et al. 2018. We use F1-score for MRPC and QQP dataset, spearman correlation for STS-B, and accuracy for the remaining as the evaluation metrics.

#### 4.3.2 Implementation details

We use Huggingface Transformers library (Apache License 2.0)Wolf et al. 2020 to fine-tune each of the aforementioned downstream tasks for 3 epochs, with a maximum sequence length of 512, batch size of 32 and learning rates 2,3,4,5e-5. Following Devlin et al. 2019, we report the best-averaged results on the validation set.

> **Table 2: Comparing RoFormer and BERT by fine tuning on downstream GLEU tasks.**

| Model | MRPC | SST-2 | QNLI | STS-B | QQP | MNLI(m/mm) |
|---|---|---|---|---|---|---|
| BERTDevlin et al. 2019 | 88.9 | 93.5 | 90.5 | 85.8 | 71.2 | 84.6/83.4 |
| RoFormer | **89.5** | 90.7 | 88.0 | **87.0** | **86.4** | 80.2/79.8 |

#### 4.3.3 Results

The evaluation results of the fine-tuning tasks are reported in Table 2. As can be seen, RoFormer can significantly outperform BERT in three out of six datasets, and the improvements are considerable.

### 4.4 Performer with RoPE

Performer Choromanski et al. 2020 introduces an alternative attention mechanism, linear attention, which is designed to avoid quadratic computation cost that scales with input sequence length. As discussed in Section 3.3, the proposed RoPE can be easily implemented in the PerFormer model to realize the relative position encoding while keeping its linearly scaled complexity in self-attention. We demonstrate its performance with the pre-training task of language modeling.

#### 4.4.1 Implementation details

We carry out tests on the Enwik8 dataset Mahoney 2006, which is from English Wikipedia that includes markup, special characters and text in other languages in addition to English text. We incorporate RoPE into the 12 layer char-based PerFormer with 768 dimensions and 12 heads [footnote: ^2^

For this experiment, we adopt code (MIT License) from https://github.com/lucidrains/performer-pytorch] .
To better illustrate the efficacy of RoPE, we report the loss curves of the pre-training process with and without RoPE under the same settings, i.e., learning rate 1e-4, batch size 128 and a fixed maximum sequence length of 1024, etc.

#### 4.4.2 Results

As shown on the right plot of Figure 3, substituting RoPE into Performer leads to rapid convergence and lower loss under the same amount of training steps. These improvements, in addition to the linear complexity, make Performer more attractive.

### 4.5 Evaluation on Chinese Data

In addition to experiments on English data, we show additional results on Chinese data. To validate the performance of RoFormer on long texts, we conduct experiments on long documents whose length exceeds 512 characters.

#### 4.5.1 Implementation

In these experiments, we carried out some modifications on WoBERT Su 2020 by replacing the absolute position embedding with our proposed RoPE. As a cross-comparison with other pre-trained Transformer-based models in Chinese, i.e. BERT Devlin et al. 2019, WoBERT Su 2020, and NEZHA Wei et al. 2019, we tabulate their tokenization level and position embedding information in Table 3.

> **Table 3: Cross-comparison between our RoFormer and other pre-trained models on Chinese data. ’abs’ and ’rel’ annotates absolute position embedding and relative position embedding, respectively.**

| Model | BERTDevlin et al. 2019 | WoBERTSu 2020 | NEZHAWei et al. 2019 | RoFormer |
|---|---|---|---|---|
| Tokenization level | char | word | char | word |
| Position embedding | abs. | abs. | rel. | RoPE |

#### 4.5.2 Pre-training

We pre-train RoFormer on approximately 34GB of data collected from Chinese Wikipedia, news and forums. The pre-training is carried out in multiple stages with changing batch size and maximum input sequence length in order to adapt the model to various scenarios. As shown in Table 4, the accuracy of RoFormer elevates with an increasing upper bound of sequence length, which demonstrates the ability of RoFormer in dealing with long texts. We claim that this is the attribute to the excellent generalizability of the proposed RoPE.

> **Table 4: Pre-training strategy of RoFormer on Chinese dataset. The training procedure is divided into various consecutive stages. In each stage, we train the model with a specific combination of maximum sequence length and batch size.**

| Stage | Max seq length | Batch size | Training steps | Loss | Accuracy |
|---|---|---|---|---|---|
| 1 | 512 | 256 | 200k | 1.73 | 65.0% |
| 2 | 1536 | 256 | 12.5k | 1.61 | 66.8% |
| 3 | 256 | 256 | 120k | 1.75 | 64.6% |
| 4 | 128 | 512 | 80k | 1.83 | 63.4% |
| 5 | 1536 | 256 | 10k | 1.58 | 67.4% |
| 6 | 512 | 512 | 30k | 1.66 | 66.2% |

#### 4.5.3 Downstream Tasks & Dataset

We choose Chinese AI and Law 2019 Similar Case Matching (CAIL2019-SCM)Xiao et al. 2019 dataset to illustrate the ability of RoFormer in dealing with long texts, i.e., semantic text matching. CAIL2019-SCM contains 8964 triplets of cases published by the Supreme People’s Court of China. The input triplet, denoted as (A, B and C), are fact descriptions of three cases. The task is to predict whether the pair (A, B) is closer than (A, C) under a predefined similarity measure. Note that existing methods mostly cannot perform significantly on CAIL2019-SCM dataset due to the length of documents (i.e., mostly more than 512 characters). We split train, validation and test sets based on the well-known ratio 6:2:2.

#### 4.5.4 Results

We apply the pre-trained RoFormer model to CAIL2019-SCM with different input lengths. The model is compared with the pre-trained BERT and WoBERT model on the same pre-training data, as shown in Table 5. With short text cut-offs, i.e., 512, the result from RoFormer is comparable to WoBERT and is slightly better than the BERT implementation. However, when increasing the maximum input text length to 1024, RoFormer outperforms WoBERT by an absolute improvement of 1.5%.

> **Table 5: Experiment results on CAIL2019-SCM task. Numbers in the first column denote the maximum cut-off sequence length. The results are presented in terms of percent accuracy.**

| Model | Validation | Test |
|---|---|---|
| BERT-512 | 64.13% | 67.77% |
| WoBERT-512 | 64.07% | 68.10% |
| **RoFormer-512** | 64.13% | 68.29% |
| **RoFormer-1024** | **66.07**% | **69.79**% |

#### 4.5.5 Limitations of the work

Although we provide theoretical groundings as well as promising experimental justifications, our method is limited by following facts:

- Despite the fact that we mathematically format the relative position relations as rotations under 2D sub-spaces, there lacks of thorough explanations on why it converges faster than baseline models that incorporates other position encoding strategies.
- Although we have proved that our model has favourable property of long-term decay for intern-token products, Section 3.3, which is similar to the existing position encoding mechanisms, our model shows superior performance on long texts than peer models, we have not come up with a faithful explanation.

Our proposed RoFormer is built upon the Transformer-based infrastructure, which requires hardware resources for pre-training purpose.

## 5 Conclusions

In this work, we proposed a new position embedding method that incorporates explicit relative position dependency in self-attention to enhance the performance of transformer architectures. Our theoretical analysis indicates that relative position can be naturally formulated using vector production in self-attention, with absolution position information being encoded through a rotation matrix. In addition, we mathematically illustrated the advantageous properties of the proposed method when applied to the Transformer. Finally, experiments on both English and Chinese benchmark datasets demonstrate that our method encourages faster convergence in pre-training. The experimental results also show that our proposed RoFormer can achieve better performance on long texts task.
