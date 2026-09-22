---
source_file: attention-is-all-you-need.html
source_type: article
ingested_at: 2026-09-22
---

# Attention Is All You Need (Vaswani et al., 2017) — arXiv 1706.03762

## Provenance
- Original location: research/raw/attention-is-all-you-need.html
- Format: html (ar5iv render of arXiv 1706.03762, full paper, 167 KB)
- Author / source (if known): Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin — Google Brain / Google Research / University of Toronto; NeurIPS 2017
- Date of original (if known): 2017-06 (v1); ar5iv render captured 2026-09-22
- Coverage in this record: complete main text (sections 1–7), Attention Visualizations appendix (captions only), all equations as LaTeX, Tables 1–4 re-typed by hand. Bibliography and page boilerplate stripped.

## Key claims
- The Transformer is "the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention" (§7). No recurrence, no convolution.
- Scaled dot-product attention: $\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^{T}/\sqrt{d_{k}})V$ (eq. 1). The $1/\sqrt{d_k}$ scaling exists because "for large values of $d_k$, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients"; with unit-variance components the dot product has variance $d_k$ (footnote 1 in §3.2.1).
- Multi-head attention: $h=8$ heads, each projecting to $d_k=d_v=d_{\text{model}}/h=64$; heads run in parallel, are concatenated and projected by $W^O$. "Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this." Cost is similar to single-head attention at full dimensionality.
- Attention is used three ways: encoder self-attention, masked decoder self-attention (illegal connections set to $-\infty$ before the softmax to preserve auto-regression), and encoder-decoder (cross) attention where queries come from the decoder and keys/values from the encoder output.
- Position-wise FFN: $\mathrm{FFN}(x)=\max(0,xW_1+b_1)W_2+b_2$ (eq. 2), $d_{\text{model}}=512$, $d_{ff}=2048$; same parameters across positions, different across layers; "two convolutions with kernel size 1".
- Each layer: sub-layer + residual + LayerNorm, i.e. $\mathrm{LayerNorm}(x+\mathrm{Sublayer}(x))$ (post-LN). Encoder $N=6$ layers with 2 sub-layers; decoder $N=6$ layers with 3 sub-layers (adds cross-attention).
- Embeddings: input/output token embeddings and the pre-softmax linear map share one weight matrix; embedding weights are multiplied by $\sqrt{d_{\text{model}}}$.
- Positional encoding: fixed sinusoids $PE_{(pos,2i)}=\sin(pos/10000^{2i/d_{\text{model}}})$, $PE_{(pos,2i+1)}=\cos(\cdot)$, wavelengths from $2\pi$ to $10000\cdot 2\pi$; chosen so that $PE_{pos+k}$ is a linear function of $PE_{pos}$; learned embeddings gave "nearly identical results" (Table 3 row E).
- Why self-attention (§4, Table 1): per-layer complexity $O(n^2\cdot d)$ vs $O(n\cdot d^2)$ recurrent; $O(1)$ sequential operations vs $O(n)$; maximum path length $O(1)$ vs $O(n)$. Self-attention is cheaper than recurrence when $n<d$. Restricted self-attention (neighbourhood $r$) would give $O(r\cdot n\cdot d)$ with path length $O(n/r)$.
- Training (§5): WMT14 En-De 4.5M pairs, BPE shared vocab ~37k; En-Fr 36M sentences, 32k word-pieces; batches of ~25k source + 25k target tokens; 8 P100 GPUs; base 100k steps ≈ 12 h at 0.4 s/step; big 300k steps ≈ 3.5 days at 1.0 s/step; Adam $\beta_1=0.9,\beta_2=0.98,\epsilon=10^{-9}$; lr $=d_{\text{model}}^{-0.5}\cdot\min(step^{-0.5}, step\cdot warmup^{-1.5})$ with 4000 warmup steps; residual dropout 0.1; label smoothing 0.1.
- Results (§6): big model 28.4 BLEU En-De (> 2 BLEU over prior ensembles), 41.8 BLEU En-Fr at < 1/4 of the previous SOTA training cost; base model 27.3 / 38.1 at $3.3\cdot 10^{18}$ FLOPs. Ablations: single head is 0.9 BLEU worse than best; too many heads also hurts; reducing $d_k$ hurts; bigger is better; dropout matters. Constituency parsing 91.3 F1 (WSJ only) / 92.7 (semi-supervised) with a 4-layer $d_{model}=1024$ Transformer.

## Definitions and terminology
- **Attention function**: mapping a query and a set of key-value pairs to an output (all vectors); output is a weighted sum of values, weights from a compatibility function of query and key.
- **Scaled Dot-Product Attention**: dot-product attention divided by $\sqrt{d_k}$ before the softmax. Contrast: additive attention (single-hidden-layer FFN as compatibility function).
- **Multi-Head Attention**: $h$ learned linear projections of Q, K, V to $d_k, d_k, d_v$, attention in parallel, concat, output projection $W^O\in\mathbb{R}^{hd_v\times d_{\text{model}}}$.
- **Self-attention / intra-attention**: all of Q, K, V come from the same sequence (output of the previous layer).
- **Encoder-decoder attention**: queries from the decoder, keys/values from the encoder output.
- **Position-wise feed-forward network**: two linear maps with ReLU, applied identically at each position.
- **Positional encoding**: fixed sinusoidal vectors of dimension $d_{\text{model}}$ added to the embeddings at the bottom of both stacks.
- Notation: $N$ layers, $d_{\text{model}}$, $d_{ff}$, $h$ heads, $d_k$, $d_v$, $P_{drop}$, $\epsilon_{ls}$.

## Evidence and examples
- Table 1 (complexity per layer type), Table 2 (BLEU and FLOPs vs ByteNet, GNMT, ConvS2S, MoE and ensembles), Table 3 (21 architectural variations on newstest2013), Table 4 (WSJ parsing F1) — all preserved in full below.
- Hardware assumptions for FLOP estimates: 2.8, 3.7, 6.0 and 9.5 TFLOPS for K80, K40, M40 and P100.
- Inference: beam size 4, length penalty $\alpha=0.6$, max output length = input + 50; checkpoint averaging (last 5 for base, last 20 for big).
- Figures 3–5 (appendix): attention heads in layer 5 of 6 following long-distance dependencies ("making … more difficult"), anaphora resolution ("its"), and sentence-structure-like patterns; different heads "clearly learned to perform different tasks".

## Inconsistencies / open questions
- The En-Fr big-model BLEU is quoted as 41.8 in Table 2 / abstract but as 41.0 in the §6.1 prose ("our big model achieves a BLEU score of 41.0"): a known inconsistency of the paper itself.
- The paper does not state the parameter count of the base model outside Table 3 (65M) nor break it down by component; the class will need its own per-block count (see scaling-laws record, Table 1, for the formula).
- Post-LN is what the paper describes; pre-LN (as in GPT-2 and ViT) is not discussed here.
- ar5iv's Table 3 uses rowspans that the automatic converter misaligned; the version below was re-typed by hand from the rendered values and checked against the printed paper.

## Images / diagrams
Companion folder `attention-is-all-you-need.html/images/` is **empty**: the source is an ar5iv render whose figures are remote assets, and the orchestrator asked for no new fetches. Each figure is listed below with its caption (captions are also inline in the excerpts) so the diagram-illustrator can redraw from the description if a slide needs it.

### Image 1
- Filename: *(not on disk)*
- Provenance: https://ar5iv.labs.arxiv.org/html/1706.03762/assets/Figures/ModalNet-21.png
- Caption (verbatim): Figure 1: The Transformer - model architecture.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 2
- Filename: *(not on disk)*
- Provenance: https://ar5iv.labs.arxiv.org/html/1706.03762/assets/Figures/ModalNet-19.png, https://ar5iv.labs.arxiv.org/html/1706.03762/assets/Figures/ModalNet-20.png
- Caption (verbatim): Figure 2: (left) Scaled Dot-Product Attention. (right) Multi-Head Attention consists of several attention layers running in parallel.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 3
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 1: Maximum path lengths, per-layer complexity and minimum number of sequential operations for different layer types. $n$ is the sequence length, $d$ is the representation dimension, $k$ is the kernel size of convolutions and $r$ the size of the neighborhood in restricted self-attention.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 4
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 2: The Transformer achieves better BLEU scores than previous state-of-the-art models on the English-to-German and English-to-French newstest2014 tests at a fraction of the training cost.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 5
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 3: Variations on the Transformer architecture. Unlisted values are identical to those of the base model. All metrics are on the English-to-German translation development set, newstest2013. Listed perplexities are per-wordpiece, according to our byte-pair encoding, and should not be compared to per-word perplexities.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 6
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 4: The Transformer generalizes well to English constituency parsing (Results are on Section 23 of WSJ)
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 7
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 3: An example of the attention mechanism following long-distance dependencies in the encoder self-attention in layer 5 of 6. Many of the attention heads attend to a distant dependency of the verb ‘making’, completing the phrase ‘making…more difficult’. Attentions here shown only for the word ‘making’. Different colors represent different heads. Best viewed in color.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 8
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 4: Two attention heads, also in layer 5 of 6, apparently involved in anaphora resolution. Top: Full attentions for head 5. Bottom: Isolated attentions from just the word ‘its’ for attention heads 5 and 6. Note that the attentions are very sharp for this word.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 9
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 5: Many of the attention heads exhibit behaviour that seems related to the structure of the sentence. We give two such examples above, from two different heads from the encoder self-attention at layer 5 of 6. The heads clearly learned to perform different tasks.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

## Raw / preserved excerpts
Provided proper attribution is provided, Google hereby grants permission to reproduce the tables and figures in this paper solely for use in journalistic or scholarly works.

**Authors:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin (Google Brain / Google Research / U. Toronto). Author note: "Equal contribution. Listing order is random. Jakob proposed replacing RNNs with self-attention... Noam proposed scaled dot-product attention, multi-head attention and the parameter-free position representation."
Ashish, with Illia, designed and implemented the first Transformer models and has been crucially involved in every aspect of this work. Noam proposed scaled dot-product attention, multi-head attention and the parameter-free position representation and became the other person involved in nearly every detail. Niki designed, implemented, tuned and evaluated countless model variants in our original codebase and tensor2tensor. Llion also experimented with novel model variants, was responsible for our initial codebase, and efficient inference and visualizations. Lukasz and Aidan spent countless long days designing various parts of and implementing tensor2tensor, replacing our earlier codebase, greatly improving results and massively accelerating our research. Affiliation: Google Brain Email: avaswani@google.com Noam Shazeer 1 1 footnotemark: 1 Affiliation: Google Brain Email: noam@google.com Niki Parmar 1 1 footnotemark: 1 Affiliation: Google Research Email: nikip@google.com Jakob Uszkoreit 1 1 footnotemark: 1 Affiliation: Google Research Email: usz@google.com Llion Jones 1 1 footnotemark: 1 Affiliation: Google Research Email: llion@google.com Aidan N. Gomez 1 1 footnotemark: 1 Thanks: Work performed while at Google Brain. Affiliation: University of Toronto Email: aidan@cs.toronto.edu Łukasz Kaiser 1 1 footnotemark: 1 Affiliation: Google Brain Email: lukaszkaiser@google.com Illia Polosukhin 1 1 footnotemark: 1 Thanks: Work performed while at Google Research. Email: illia.polosukhin@gmail.com

## Abstract

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

## 1 Introduction

Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation [35, 2, 5]. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures [38, 24, 15].

Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states $h_{t}$, as a function of the previous hidden state $h_{t-1}$ and the input for position $t$. This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples.
Recent work has achieved significant improvements in computational efficiency through factorization tricks [21] and conditional computation [32], while also improving model performance in case of the latter. The fundamental constraint of sequential computation, however, remains.

Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences [2, 19]. In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network.

In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs.

## 2 Background

The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU [16], ByteNet [18] and ConvS2S [9], all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions [12]. In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention as described in section 3.2.

Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations [4, 27, 28, 22].

End-to-end memory networks are based on a recurrent attention mechanism instead of sequence-aligned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks [34].

To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequence-aligned RNNs or convolution.
In the following sections, we will describe the Transformer, motivate self-attention and discuss its advantages over models such as [17, 18] and [9].

## 3 Model Architecture

> **Figure 1: The Transformer - model architecture.**
> (image not fetched: /html/1706.03762/assets/Figures/ModalNet-21.png)

Most competitive neural sequence transduction models have an encoder-decoder structure [5, 2, 35]. Here, the encoder maps an input sequence of symbol representations $(x_{1},...,x_{n})$ to a sequence of continuous representations $\mathbf{z}=(z_{1},...,z_{n})$. Given $\mathbf{z}$, the decoder then generates an output sequence $(y_{1},...,y_{m})$ of symbols one element at a time. At each step the model is auto-regressive [10], consuming the previously generated symbols as additional input when generating the next.

The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively.

### 3.1 Encoder and Decoder Stacks

##### Encoder:

The encoder is composed of a stack of $N=6$ identical layers. Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, position-wise fully connected feed-forward network. We employ a residual connection [11] around each of the two sub-layers, followed by layer normalization [1]. That is, the output of each sub-layer is $\mathrm{LayerNorm}(x+\mathrm{Sublayer}(x))$, where $\mathrm{Sublayer}(x)$ is the function implemented by the sub-layer itself. To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension $d_{\text{model}}=512$.

##### Decoder:

The decoder is also composed of a stack of $N=6$ identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization. We also modify the self-attention sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position $i$ can depend only on the known outputs at positions less than $i$.

### 3.2 Attention

An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.

#### 3.2.1 Scaled Dot-Product Attention

We call our particular attention "Scaled Dot-Product Attention" (Figure 2). The input consists of queries and keys of dimension $d_{k}$, and values of dimension $d_{v}$. We compute the dot products of the query with all keys, divide each by $\sqrt{d_{k}}$, and apply a softmax function to obtain the weights on the values.

In practice, we compute the attention function on a set of queries simultaneously, packed together into a matrix $Q$. The keys and values are also packed together into matrices $K$ and $V$. We compute the matrix of outputs as:

$$\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(\frac{QK^{T}}{\sqrt{d_{k}}})V \quad (1)$$

The two most commonly used attention functions are additive attention [2], and dot-product (multiplicative) attention. Dot-product attention is identical to our algorithm, except for the scaling factor of $\frac{1}{\sqrt{d_{k}}}$. Additive attention computes the compatibility function using a feed-forward network with a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code.

While for small values of $d_{k}$ the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of $d_{k}$ [3]. We suspect that for large values of $d_{k}$, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients [footnote: ^1^

To illustrate why the dot products get large, assume that the components of $q$ and $k$ are independent random variables with mean $0$ and variance $1$. Then their dot product, $q\cdot k=\sum_{i=1}^{d_{k}}q_{i}k_{i}$, has mean $0$ and variance $d_{k}$.] . To counteract this effect, we scale the dot products by $\frac{1}{\sqrt{d_{k}}}$.

#### 3.2.2 Multi-Head Attention

> **Figure 2: (left) Scaled Dot-Product Attention. (right) Multi-Head Attention consists of several attention layers running in parallel.**
> (image not fetched: /html/1706.03762/assets/Figures/ModalNet-19.png, /html/1706.03762/assets/Figures/ModalNet-20.png)

Instead of performing a single attention function with $d_{\text{model}}$-dimensional keys, values and queries, we found it beneficial to linearly project the queries, keys and values $h$ times with different, learned linear projections to $d_{k}$, $d_{k}$ and $d_{v}$ dimensions, respectively.
On each of these projected versions of queries, keys and values we then perform the attention function in parallel, yielding $d_{v}$-dimensional output values. These are concatenated and once again projected, resulting in the final values, as depicted in Figure 2.

Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this.

$$\displaystyle\mathrm{MultiHead}(Q,K,V) \displaystyle=\mathrm{Concat}(\mathrm{head_{1}},...,\mathrm{head_{h}})W^{O} \\
\displaystyle\text{where}~\mathrm{head_{i}} \displaystyle=\mathrm{Attention}(QW^{Q}_{i},KW^{K}_{i},VW^{V}_{i})$$

Where the projections are parameter matrices $W^{Q}_{i}\in\mathbb{R}^{d_{\text{model}}\times d_{k}}$, $W^{K}_{i}\in\mathbb{R}^{d_{\text{model}}\times d_{k}}$, $W^{V}_{i}\in\mathbb{R}^{d_{\text{model}}\times d_{v}}$ and $W^{O}\in\mathbb{R}^{hd_{v}\times d_{\text{model}}}$.

In this work we employ $h=8$ parallel attention layers, or heads. For each of these we use $d_{k}=d_{v}=d_{\text{model}}/h=64$.
Due to the reduced dimension of each head, the total computational cost is similar to that of single-head attention with full dimensionality.

#### 3.2.3 Applications of Attention in our Model

The Transformer uses multi-head attention in three different ways:

- In "encoder-decoder attention" layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence. This mimics the typical encoder-decoder attention mechanisms in sequence-to-sequence models such as [38, 2, 9].
- The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder.
- Similarly, self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position. We need to prevent leftward information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking out (setting to $-\infty$) all values in the input of the softmax which correspond to illegal connections. See Figure 2.

### 3.3 Position-wise Feed-Forward Networks

In addition to attention sub-layers, each of the layers in our encoder and decoder contains a fully connected feed-forward network, which is applied to each position separately and identically. This consists of two linear transformations with a ReLU activation in between.

$$\mathrm{FFN}(x)=\max(0,xW_{1}+b_{1})W_{2}+b_{2} \quad (2)$$

While the linear transformations are the same across different positions, they use different parameters from layer to layer. Another way of describing this is as two convolutions with kernel size 1. The dimensionality of input and output is $d_{\text{model}}=512$, and the inner-layer has dimensionality $d_{ff}=2048$.

### 3.4 Embeddings and Softmax

Similarly to other sequence transduction models, we use learned embeddings to convert the input tokens and output tokens to vectors of dimension $d_{\text{model}}$. We also use the usual learned linear transformation and softmax function to convert the decoder output to predicted next-token probabilities. In our model, we share the same weight matrix between the two embedding layers and the pre-softmax linear transformation, similar to [30]. In the embedding layers, we multiply those weights by $\sqrt{d_{\text{model}}}$.

### 3.5 Positional Encoding

Since our model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position of the tokens in the sequence. To this end, we add "positional encodings" to the input embeddings at the bottoms of the encoder and decoder stacks. The positional encodings have the same dimension $d_{\text{model}}$ as the embeddings, so that the two can be summed. There are many choices of positional encodings, learned and fixed [9].

In this work, we use sine and cosine functions of different frequencies:

$$\displaystyle PE_{(pos,2i)}=sin(pos/10000^{2i/d_{\text{model}}}) \\
\displaystyle PE_{(pos,2i+1)}=cos(pos/10000^{2i/d_{\text{model}}})$$

where $pos$ is the position and $i$ is the dimension. That is, each dimension of the positional encoding corresponds to a sinusoid. The wavelengths form a geometric progression from $2\pi$ to $10000\cdot 2\pi$. We chose this function because we hypothesized it would allow the model to easily learn to attend by relative positions, since for any fixed offset $k$, $PE_{pos+k}$ can be represented as a linear function of $PE_{pos}$.

We also experimented with using learned positional embeddings [9] instead, and found that the two versions produced nearly identical results (see Table 3 row (E)). We chose the sinusoidal version because it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training.

## 4 Why Self-Attention

In this section we compare various aspects of self-attention layers to the recurrent and convolutional layers commonly used for mapping one variable-length sequence of symbol representations $(x_{1},...,x_{n})$ to another sequence of equal length $(z_{1},...,z_{n})$, with $x_{i},z_{i}\in\mathbb{R}^{d}$, such as a hidden layer in a typical sequence transduction encoder or decoder. Motivating our use of self-attention we consider three desiderata.

One is the total computational complexity per layer.
Another is the amount of computation that can be parallelized, as measured by the minimum number of sequential operations required.

The third is the path length between long-range dependencies in the network. Learning long-range dependencies is a key challenge in many sequence transduction tasks. One key factor affecting the ability to learn such dependencies is the length of the paths forward and backward signals have to traverse in the network. The shorter these paths between any combination of positions in the input and output sequences, the easier it is to learn long-range dependencies [12]. Hence we also compare the maximum path length between any two input and output positions in networks composed of the different layer types.

> **Table 1: Maximum path lengths, per-layer complexity and minimum number of sequential operations for different layer types. $n$ is the sequence length, $d$ is the representation dimension, $k$ is the kernel size of convolutions and $r$ the size of the neighborhood in restricted self-attention.**

| Layer Type | Complexity per Layer | Sequential Operations | Maximum Path Length |
|---|---|---|---|
| Self-Attention | $O(n^{2}\cdot d)$ | $O(1)$ | $O(1)$ |
| Recurrent | $O(n\cdot d^{2})$ | $O(n)$ | $O(n)$ |
| Convolutional | $O(k\cdot n\cdot d^{2})$ | $O(1)$ | $O(\log_{k}(n))$ |
| Self-Attention (restricted) | $O(r\cdot n\cdot d)$ | $O(1)$ | $O(n/r)$ |

As noted in Table 1, a self-attention layer connects all positions with a constant number of sequentially executed operations, whereas a recurrent layer requires $O(n)$ sequential operations.
In terms of computational complexity, self-attention layers are faster than recurrent layers when the sequence length $n$ is smaller than the representation dimensionality $d$, which is most often the case with sentence representations used by state-of-the-art models in machine translations, such as word-piece [38] and byte-pair [31] representations.
To improve computational performance for tasks involving very long sequences, self-attention could be restricted to considering only a neighborhood of size $r$ in the input sequence centered around the respective output position. This would increase the maximum path length to $O(n/r)$. We plan to investigate this approach further in future work.

A single convolutional layer with kernel width $k<n$ does not connect all pairs of input and output positions. Doing so requires a stack of $O(n/k)$ convolutional layers in the case of contiguous kernels, or $O(log_{k}(n))$ in the case of dilated convolutions [18], increasing the length of the longest paths between any two positions in the network.
Convolutional layers are generally more expensive than recurrent layers, by a factor of $k$. Separable convolutions [6], however, decrease the complexity considerably, to $O(k\cdot n\cdot d+n\cdot d^{2})$. Even with $k=n$, however, the complexity of a separable convolution is equal to the combination of a self-attention layer and a point-wise feed-forward layer, the approach we take in our model.

As side benefit, self-attention could yield more interpretable models. We inspect attention distributions from our models and present and discuss examples in the appendix. Not only do individual attention heads clearly learn to perform different tasks, many appear to exhibit behavior related to the syntactic and semantic structure of the sentences.

## 5 Training

This section describes the training regime for our models.

### 5.1 Training Data and Batching

We trained on the standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs. Sentences were encoded using byte-pair encoding [3], which has a shared source-target vocabulary of about 37000 tokens. For English-French, we used the significantly larger WMT 2014 English-French dataset consisting of 36M sentences and split tokens into a 32000 word-piece vocabulary [38]. Sentence pairs were batched together by approximate sequence length. Each training batch contained a set of sentence pairs containing approximately 25000 source tokens and 25000 target tokens.

### 5.2 Hardware and Schedule

We trained our models on one machine with 8 NVIDIA P100 GPUs. For our base models using the hyperparameters described throughout the paper, each training step took about 0.4 seconds. We trained the base models for a total of 100,000 steps or 12 hours. For our big models,(described on the bottom line of table 3), step time was 1.0 seconds. The big models were trained for 300,000 steps (3.5 days).

### 5.3 Optimizer

We used the Adam optimizer [20] with $\beta_{1}=0.9$, $\beta_{2}=0.98$ and $\epsilon=10^{-9}$. We varied the learning rate over the course of training, according to the formula:

$$lrate=d_{\text{model}}^{-0.5}\cdot\min({step\_num}^{-0.5},{step\_num}\cdot{warmup\_steps}^{-1.5}) \quad (3)$$

This corresponds to increasing the learning rate linearly for the first $warmup\_steps$ training steps, and decreasing it thereafter proportionally to the inverse square root of the step number. We used $warmup\_steps=4000$.

### 5.4 Regularization

We employ three types of regularization during training:

##### Residual Dropout

We apply dropout [33] to the output of each sub-layer, before it is added to the sub-layer input and normalized. In addition, we apply dropout to the sums of the embeddings and the positional encodings in both the encoder and decoder stacks. For the base model, we use a rate of $P_{drop}=0.1$.

##### Label Smoothing

During training, we employed label smoothing of value $\epsilon_{ls}=0.1$ [36]. This hurts perplexity, as the model learns to be more unsure, but improves accuracy and BLEU score.

## 6 Results

### 6.1 Machine Translation

> **Table 2: The Transformer achieves better BLEU scores than previous state-of-the-art models on the English-to-German and English-to-French newstest2014 tests at a fraction of the training cost.**

| Model | BLEU EN-DE | BLEU EN-FR | Training Cost (FLOPs) EN-DE | Training Cost (FLOPs) EN-FR |
|---|---|---|---|---|
| ByteNet [18] | 23.75 | | | |
| Deep-Att + PosUnk [39] | | 39.2 | | $1.0\cdot 10^{20}$ |
| GNMT + RL [38] | 24.6 | 39.92 | $2.3\cdot 10^{19}$ | $1.4\cdot 10^{20}$ |
| ConvS2S [9] | 25.16 | 40.46 | $9.6\cdot 10^{18}$ | $1.5\cdot 10^{20}$ |
| MoE [32] | 26.03 | 40.56 | $2.0\cdot 10^{19}$ | $1.2\cdot 10^{20}$ |
| Deep-Att + PosUnk Ensemble [39] | | 40.4 | | $8.0\cdot 10^{20}$ |
| GNMT + RL Ensemble [38] | 26.30 | 41.16 | $1.8\cdot 10^{20}$ | $1.1\cdot 10^{21}$ |
| ConvS2S Ensemble [9] | 26.36 | **41.29** | $7.7\cdot 10^{19}$ | $1.2\cdot 10^{21}$ |
| Transformer (base model) | 27.3 | 38.1 | $3.3\cdot 10^{18}$ | $3.3\cdot 10^{18}$ |
| Transformer (big) | **28.4** | **41.8** | $2.3\cdot 10^{19}$ | $2.3\cdot 10^{19}$ |

*(Note: in the paper the two Transformer training-cost cells span both language pairs: $3.3\cdot 10^{18}$ for base and $2.3\cdot 10^{19}$ for big.)*

On the WMT 2014 English-to-German translation task, the big transformer model (Transformer (big) in Table 2) outperforms the best previously reported models (including ensembles) by more than $2.0$ BLEU, establishing a new state-of-the-art BLEU score of $28.4$. The configuration of this model is listed in the bottom line of Table 3. Training took $3.5$ days on $8$ P100 GPUs. Even our base model surpasses all previously published models and ensembles, at a fraction of the training cost of any of the competitive models.

On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of $41.0$, outperforming all of the previously published single models, at less than $1/4$ the training cost of the previous state-of-the-art model. The Transformer (big) model trained for English-to-French used dropout rate $P_{drop}=0.1$, instead of $0.3$.

For the base models, we used a single model obtained by averaging the last 5 checkpoints, which were written at 10-minute intervals. For the big models, we averaged the last 20 checkpoints. We used beam search with a beam size of $4$ and length penalty $\alpha=0.6$ [38]. These hyperparameters were chosen after experimentation on the development set. We set the maximum output length during inference to input length + $50$, but terminate early when possible [38].

Table 2 summarizes our results and compares our translation quality and training costs to other model architectures from the literature. We estimate the number of floating point operations used to train a model by multiplying the training time, the number of GPUs used, and an estimate of the sustained single-precision floating-point capacity of each GPU [footnote: ^2^

We used values of 2.8, 3.7, 6.0 and 9.5 TFLOPS for K80, K40, M40 and P100, respectively.] .

### 6.2 Model Variations

> **Table 3: Variations on the Transformer architecture. Unlisted values are identical to those of the base model. All metrics are on the English-to-German translation development set, newstest2013. Listed perplexities are per-wordpiece, according to our byte-pair encoding, and should not be compared to per-word perplexities.**

| | $N$ | $d_{\text{model}}$ | $d_{\text{ff}}$ | $h$ | $d_{k}$ | $d_{v}$ | $P_{drop}$ | $\epsilon_{ls}$ | train steps | PPL (dev) | BLEU (dev) | params $\times 10^{6}$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| base | 6 | 512 | 2048 | 8 | 64 | 64 | 0.1 | 0.1 | 100K | 4.92 | 25.8 | 65 |
| (A) | | | | 1 | 512 | 512 | | | | 5.29 | 24.9 | |
| (A) | | | | 4 | 128 | 128 | | | | 5.00 | 25.5 | |
| (A) | | | | 16 | 32 | 32 | | | | 4.91 | 25.8 | |
| (A) | | | | 32 | 16 | 16 | | | | 5.01 | 25.4 | |
| (B) | | | | | 16 | | | | | 5.16 | 25.1 | 58 |
| (B) | | | | | 32 | | | | | 5.01 | 25.4 | 60 |
| (C) | 2 | | | | | | | | | 6.11 | 23.7 | 36 |
| (C) | 4 | | | | | | | | | 5.19 | 25.3 | 50 |
| (C) | 8 | | | | | | | | | 4.88 | 25.5 | 80 |
| (C) | | 256 | | | 32 | 32 | | | | 5.75 | 24.5 | 28 |
| (C) | | 1024 | | | 128 | 128 | | | | 4.66 | 26.0 | 168 |
| (C) | | | 1024 | | | | | | | 5.12 | 25.4 | 53 |
| (C) | | | 4096 | | | | | | | 4.75 | 26.2 | 90 |
| (D) | | | | | | | 0.0 | | | 5.77 | 24.6 | |
| (D) | | | | | | | 0.2 | | | 4.95 | 25.5 | |
| (D) | | | | | | | | 0.0 | | 4.67 | 25.3 | |
| (D) | | | | | | | | 0.2 | | 5.47 | 25.7 | |
| (E) | positional embedding instead of sinusoids | | | | | | | | | 4.92 | 25.7 | |
| big | 6 | 1024 | 4096 | 16 | | | 0.3 | | 300K | **4.33** | **26.4** | 213 |

*(Unlisted values are identical to the base model; the table was re-typed by hand from the ar5iv render because rowspans misalign the automatic conversion. Rows (A) keep computation constant: $d_k = d_v = d_{\text{model}}/h$.)*

To evaluate the importance of different components of the Transformer, we varied our base model in different ways, measuring the change in performance on English-to-German translation on the development set, newstest2013. We used beam search as described in the previous section, but no checkpoint averaging. We present these results in Table 3.

In Table 3 rows (A), we vary the number of attention heads and the attention key and value dimensions, keeping the amount of computation constant, as described in Section 3.2.2. While single-head attention is 0.9 BLEU worse than the best setting, quality also drops off with too many heads.

In Table 3 rows (B), we observe that reducing the attention key size $d_{k}$ hurts model quality. This suggests that determining compatibility is not easy and that a more sophisticated compatibility function than dot product may be beneficial. We further observe in rows (C) and (D) that, as expected, bigger models are better, and dropout is very helpful in avoiding over-fitting. In row (E) we replace our sinusoidal positional encoding with learned positional embeddings [9], and observe nearly identical results to the base model.

### 6.3 English Constituency Parsing

> **Table 4: The Transformer generalizes well to English constituency parsing (Results are on Section 23 of WSJ)**

| **Parser** | **Training** | **WSJ 23 F1** |
|---|---|---|
| Vinyals & Kaiser el al. (2014) [37] | WSJ only, discriminative | 88.3 |
| Petrov et al. (2006) [29] | WSJ only, discriminative | 90.4 |
| Zhu et al. (2013) [40] | WSJ only, discriminative | 90.4 |
| Dyer et al. (2016) [8] | WSJ only, discriminative | 91.7 |
| Transformer (4 layers) | WSJ only, discriminative | 91.3 |
| Zhu et al. (2013) [40] | semi-supervised | 91.3 |
| Huang & Harper (2009) [14] | semi-supervised | 91.3 |
| McClosky et al. (2006) [26] | semi-supervised | 92.1 |
| Vinyals & Kaiser el al. (2014) [37] | semi-supervised | 92.1 |
| Transformer (4 layers) | semi-supervised | 92.7 |
| Luong et al. (2015) [23] | multi-task | 93.0 |
| Dyer et al. (2016) [8] | generative | 93.3 |

To evaluate if the Transformer can generalize to other tasks we performed experiments on English constituency parsing. This task presents specific challenges: the output is subject to strong structural constraints and is significantly longer than the input.
Furthermore, RNN sequence-to-sequence models have not been able to attain state-of-the-art results in small-data regimes [37].

We trained a 4-layer transformer with $d_{model}=1024$ on the Wall Street Journal (WSJ) portion of the Penn Treebank [25], about 40K training sentences. We also trained it in a semi-supervised setting, using the larger high-confidence and BerkleyParser corpora from with approximately 17M sentences [37]. We used a vocabulary of 16K tokens for the WSJ only setting and a vocabulary of 32K tokens for the semi-supervised setting.

We performed only a small number of experiments to select the dropout, both attention and residual (section 5.4), learning rates and beam size on the Section 22 development set, all other parameters remained unchanged from the English-to-German base translation model. During inference, we increased the maximum output length to input length + $300$. We used a beam size of $21$ and $\alpha=0.3$ for both WSJ only and the semi-supervised setting.

Our results in Table 4 show that despite the lack of task-specific tuning our model performs surprisingly well, yielding better results than all previously reported models with the exception of the Recurrent Neural Network Grammar [8].

In contrast to RNN sequence-to-sequence models [37], the Transformer outperforms the BerkeleyParser [29] even when training only on the WSJ training set of 40K sentences.

## 7 Conclusion

In this work, we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention.

For translation tasks, the Transformer can be trained significantly faster than architectures based on recurrent or convolutional layers. On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, we achieve a new state of the art. In the former task our best model outperforms even all previously reported ensembles.

We are excited about the future of attention-based models and plan to apply them to other tasks. We plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video.
Making generation less sequential is another research goals of ours.

The code we used to train and evaluate our models is available at https://github.com/tensorflow/tensor2tensor.

##### Acknowledgements

We are grateful to Nal Kalchbrenner and Stephan Gouws for
their fruitful comments, corrections and inspiration.

## Attention Visualizations

> **Figure 3: An example of the attention mechanism following long-distance dependencies in the encoder self-attention in layer 5 of 6. Many of the attention heads attend to a distant dependency of the verb ‘making’, completing the phrase ‘making…more difficult’. Attentions here shown only for the word ‘making’. Different colors represent different heads. Best viewed in color.**

> **Figure 4: Two attention heads, also in layer 5 of 6, apparently involved in anaphora resolution. Top: Full attentions for head 5. Bottom: Isolated attentions from just the word ‘its’ for attention heads 5 and 6. Note that the attentions are very sharp for this word.**

> **Figure 5: Many of the attention heads exhibit behaviour that seems related to the structure of the sentence. We give two such examples above, from two different heads from the encoder self-attention at layer 5 of 6. The heads clearly learned to perform different tasks.**
