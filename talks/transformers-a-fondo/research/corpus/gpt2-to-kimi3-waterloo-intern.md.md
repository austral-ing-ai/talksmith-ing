---
source_file: gpt2-to-kimi3-waterloo-intern.md
source_type: article
ingested_at: 2026-09-22
---

# 22580: From GPT2 to Kimi3, Explained (ali / @waterloo_intern, X Article, 2026)

## Provenance
- Original location: research/raw/gpt2-to-kimi3-waterloo-intern.md
- Format: md (plain-text capture of an X Article via Chrome, prepared by Marco; figures and several code blocks of the published version were not captured)
- Author / source (if known): ali (@waterloo_intern); URL https://x.com/waterloo_intern/article/2081762065392541951
- Date of original (if known): 2026-07-27; captured 2026-09-22
- Coverage in this record: the file is kept **verbatim and in full** below (its own header, Marco's Spanish summary "Recorrido del articulo", and the captured text). Intended use per the file header: source for class 9 "Transformers Avanzados"; in class 8 only the stages are named.

## Key claims
- Hook: Kimi K3 (2026, 2.8T parameters) holds 22,580 GPT-2s (2019, 124M); the article asks whether the seven-year gap is "just scale".
- GPT-2 baseline as decoder-only: token + position embeddings, 12 pre-LN blocks `x = x + attn(ln1(x)); x = x + mlp(ln2(x))`, causal self-attention with a mask, tied lm_head; 50304 vocab, 12 layers, 12 heads, 768 dims, ~124M params.
- KV cache: in decode only the last position's logits are used; caching K and V of previous tokens avoids recomputation; grows O(N) and becomes a memory-bandwidth bottleneck.
- Linear attention (Katharopoulos 2020): feature map (ELU+1) on q and k separately instead of softmax after the product; lets K,V be folded into a fixed D×D state; less expressive than the softmax kernel. Three steps of any attention: non-negative scores, divide by the sum, weighted average of V.
- DeltaNet / fast weight programmers (Schlag): additive state interferes when N ≫ D; the delta rule reads what the key already holds ($v_{old}=kS$) and writes only $\beta(v-v_{old})$; chunked parallel form (Yang et al.): within-chunk masked attention, between-chunk recurrent state; C=N is full attention, C=1 is linear attention; typical C 64 or 128 for tensor cores; $S_t=S_{t-1}(I-\beta kk^T)+\beta vk^T$.
- Gated DeltaNet: adds Mamba-2's scalar decay ($\alpha S_{old}$) to the delta rule: global forgetting + targeted replacement.
- Kimi Linear / KDA: per-channel decay instead of scalar; hybrid with interleaved MLA layers; MLP replaced by MoE; claim of beating full attention with up to 6× decode throughput.
- Kimi K3: 23 macro-cycles of 4 layers (3 KDA + 1 MLA); first FFN dense, the rest latent MoE (898 experts: 2 shared + 16 of 896 per token); gated MLA; MLA query LoRA; SiTU activation (tanh bounded by $\beta\cdot$sigmoid); AttnRes every 12 layers (attention over previous layers' residual states, ~2% latency, 1.25× compute).
- Author's thesis: it is not only scale; each step changes what the model stores, how it updates that state, or how it recovers what a fixed state cannot keep. A fixed-capacity associative memory needs an eviction policy (gating, routing, decay), and attention is the most effective selective-read mechanism.

## Definitions and terminology
- **Decoder-only**, **pre-LN block**, **causal mask**, **KV cache**.
- **Linear attention**, **feature map**, **fixed-size state** $S\in\mathbb{R}^{D\times D}$.
- **Delta rule**, **fast weight programmer**, **chunked parallel form**, chunk size $C$.
- **Gated DeltaNet**, **scalar decay** (Mamba-2), **per-channel decay** (KDA), **Kimi Linear**.
- **Latent MoE**, **shared / routed experts**, **Gated MLA**, **query LoRA**, **SiTU**, **AttnRes** (attention over residual states).
- **Associative memory** with **eviction policy** (gating, routing, decay).

## Evidence and examples
- Code fragments (PyTorch-style pseudo-code) for the GPT-2 block, KV cache, linear attention, and DeltaNet chunking, as captured in the plain-text version.
- Numeric configuration of Kimi K3 (layers, experts, cycle structure) and the 22,580× ratio.
- The claim of 6× decode throughput for Kimi Linear is attributed to the Kimi Linear report, not measured by the author.

## Inconsistencies / open questions
- This is a personal worklog on X, not a peer-reviewed source; numbers about Kimi K3 should be checked against Moonshot's technical report before being put on a slide.
- Figures and some code blocks of the original were not captured (stated in the file header).
- The class-8 deck should only *name* the stages (KV cache → linear attention → DeltaNet → gated → KDA → K3); the detail belongs to class 9.
- The GPT-2 parameter count here (124M) differs from the 117M printed in the 2019 paper; the 124M figure is the corrected count widely used since 2019.

## Images / diagrams
The captured Markdown carries no images (the capture note says the figures of the published article were not captured). Companion folder `gpt2-to-kimi3-waterloo-intern.md/images/` is empty.

## Raw / preserved excerpts
*(Verbatim copy of research/raw/gpt2-to-kimi3-waterloo-intern.md, unchanged.)*

# 22580: From GPT2 to Kimi3, Explained

- Autor: ali (@waterloo_intern), X Article, 2026-07-27
- URL: https://x.com/waterloo_intern/article/2081762065392541951
- Capturado: 2026-09-22, texto plano via Chrome (las figuras y varios bloques de codigo de la version final no se capturan)
- Uso previsto: fuente para la clase 9 "Transformers Avanzados"; en la clase 8 solo se nombran las etapas.

## Recorrido del articulo (resumen propio)

1. GPT-2 como linea de base decoder-only: wte + wpe, 12 bloques pre-LN (x = x + attn(ln1(x)); x = x + mlp(ln2(x))), causal self-attention con mascara, lm_head. 50304 vocab, 12 capas, 12 cabezas, 768 dims, ~124M parametros. Kimi K3 tiene 2,8T parametros = 22.580 GPT-2.
2. KV cache: en decode solo se usan los logits de la ultima posicion; guardar K y V de los tokens previos evita recomputarlos. Crece O(N) y se vuelve cuello de botella de ancho de banda de memoria.
3. Linear attention (Katharopoulos 2020): feature map (ELU+1) sobre q y k por separado en vez de softmax despues del producto; permite reasociar y plegar K,V en un estado fijo D x D. Menos expresivo que el kernel softmax. Tres pasos de toda atencion: scores no negativos, dividir por la suma, promedio ponderado de V.
4. DeltaNet / Fast Weight Programmers (Schlag): el estado aditivo interfiere cuando N >> D; la delta rule lee lo que ya hay en la clave (v_old = k S), escribe solo la diferencia beta (v - v_old). Version paralelizable por chunks (Yang et al.): dentro del chunk atencion normal enmascarada, entre chunks estado recurrente; C=N es atencion completa, C=1 es linear attention; C tipico 64 o 128 por tensor cores. Reparametrizacion S_t = S_{t-1}(I - beta k k^T) + beta v k^T.
5. Gated DeltaNet: suma el decaimiento escalar de Mamba-2 (alpha * S_old) a la delta rule: olvido global + reemplazo puntual.
6. Kimi Linear / KDA: decaimiento por canal (alpha por dimension) en vez de escalar; hibrido con capas MLA intercaladas; MLP reemplazado por MoE. Afirmacion: supera a atencion completa con hasta 6x mas throughput de decode.
7. Kimi K3: 23 macrociclos de 4 capas (3 KDA + 1 MLA); primera capa FFN densa, el resto latent MoE (898 expertos: 2 compartidos + 16 de 896 por token); Gated MLA; MLA query LoRA; activacion SiTU (tanh acotado por beta * sigmoid); AttnRes por bloques cada 12 capas (atencion sobre los estados residuales de capas anteriores, ~2% de latencia, 1,25x de computo).
8. Tesis del autor: no es solo escala; cada paso cambia que guarda el modelo, como actualiza ese estado o como recupera lo que un estado fijo no conserva. Una memoria asociativa de capacidad fija necesita politica de desalojo (gating, routing, decay), y la atencion es el mecanismo de lectura selectiva mas efectivo.

## Texto capturado


Twenty-two thousand five hundred and eighty. That's how many GPT-2 (2019) models fit inside KimiK3 (2026). We scaled up by a factor of 22,580 in seven years. But is it just... scale?

In this worklog, I'll walk through how we got here and how much, or how little, has actually changed since then. We'll trace the major architectural developments leading to KimiK3.

### GPT-2

GPT-2 is a decoder-only architecture:

```python
tok_emb = self.transformer.wte(idx) # token embeddings of shape (b, t, n_embd)
pos_emb = self.transformer.wpe(pos) # position embeddings of shape (t, n_embd)
x = self.transformer.drop(tok_emb + pos_emb)
for block in self.transformer.h:
    x = block(x)
x = self.transformer.ln_f(x)
logits = self.lm_head(x)
return logits
```

Each transformer block, zoomed in, looks like this:

```python
class Block(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.ln_1 = LayerNorm(config.n_embd, bias=config.bias)
        self.attn = CausalSelfAttention(config)
        self.ln_2 = LayerNorm(config.n_embd, bias=config.bias)
        self.mlp = MLP(config)
    def forward(self, x):
        x = x + self.attn(self.ln_1(x))
        x = x + self.mlp(self.ln_2(x))
        return x
```

The attention process:

```python
B, T, C = x.size() # batch size, sequence length, embedding dimensionality (n_embd)
q, k, v = self.c_attn(x).split(self.n_embd, dim=2)
k = k.view(B, T, self.n_head, C // self.n_head).transpose(1, 2) # (B, nh, T, hs)
q = q.view(B, T, self.n_head, C // self.n_head).transpose(1, 2) # (B, nh, T, hs)
v = v.view(B, T, self.n_head, C // self.n_head).transpose(1, 2) # (B, nh, T, hs)
att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(k.size(-1)))
att = att.masked_fill(self.bias[:,:,:T,:T] == 0, float('-inf'))
att = F.softmax(att, dim=-1)
att = self.attn_dropout(att)
y = att @ v # (B, nh, T, T) x (B, nh, T, hs) -> (B, nh, T, hs)
y = y.transpose(1, 2).contiguous().view(B, T, C) # re-assemble all head outputs side by side
y = self.resid_dropout(self.c_proj(y))
return y
```

Once the final hidden-state matrix is produced, the language-model head maps it into vocabulary logits. During autoregressive decoding, only the logits at the final position are needed to select the next token.

This is an inefficiency of decoder-only generation: the model computes representations for every input position, but each decode step consumes only the final position's logits. Without caching, much of that work would be repeated for the next token.

The KV cache comes from a straightforward observation: after appending the generated token to the input, the model would otherwise recompute projections for all previous tokens. Storing their key and value vectors avoids that redundant work. That storage is the KV cache. It retains vectors for the previous N-1 tokens and can become large enough to create a memory-bandwidth bottleneck.

Overall, with about 50k possible tokens, 12 blocks, 12 heads, and an embedding dimension of 768, our baseline model is about 124M parameters.

```python
vocab_size: int = 50304 # GPT-2 vocab_size of 50257, padded up to nearest multiple of 64 for efficiency
n_layer: int = 12
n_head: int = 12
n_embd: int = 768
```

At 2.8 trillion parameters, one KimiK3 model contains roughly as many parameters as 22,580 GPT-2 models.

### Linear Attention

Softmax attention applies its nonlinearity after the q·k product, coupling every query to every key. Linear attention instead applies a feature map, such as ELU+1, to q and k separately. This makes the product re-associable, so the growing set of K and V vectors can be folded into a fixed D×D state.

The paper's O(N²) framing threw me off. It's not true that "the cost per time-step for transformers scales with the square of the current sequence length". That's what Flash Attention fixes... then I saw that it was released in 2020. At the time, training commonly materialized the full N×N attention matrix, FlashAttention did not exist, and reference autoregressive implementations often recomputed the token history without a KV cache.

(Codigo de atencion softmax con past_kv: en prefill q,k,v son b,h,t,d; en decode b,h,1,d; se concatena en la dimension t; mascara causal solo en prefill; past_kv=(k,v).)

Each decode step performs two ND reads and two 1D writes to HBM, while the KV cache grows linearly, in O(N), with the sequence length. Linear attention replaces that with:

```python
k=F.elu(k)+1
k=k.transpose(-1,-2)
q=F.elu(q)+1
S,z=cache if cache is not None else (0.0, 0.0)
S=S+k@v
z=z+k
o=q@S       # bhtd
denom=q@z
o_scaled=o/denom
cache=(S,z)
```

There is a trade-off. Here, we replace the exponential used by softmax with ELU+1 applied separately to q and k before they interact. Both approaches normalize the resulting scores, but the feature map used by linear attention is a less expressive approximation of the softmax kernel. That approximation can reduce fidelity, although the practical accuracy loss depends on the architecture and workload.

At a high level, attention consists of three steps: (1) make the qk scores non-negative (linear attention uses ELU+1, softmax uses exponentiation); (2) divide by the sum; (3) compute the weighted average of the values. This preserves the basic attention contract, but uses a less expressive feature map to make the QK scores non-negative.

### DeltaNet (Fast Weight Programmers)

A finite cache must overwrite or combine with information already stored. The state from token i-1 does not receive its own slot; it is added to the same D by D matrix. New queries can therefore no longer retrieve a perfectly isolated representation of each earlier token. That addition is also the source of the efficiency gain. Updating the cache additively rather than by concatenation prevents it from growing in O(N), but the same operation causes information to interfere. DeltaNet addresses this loss of recoverability.

Schlag (Fast Weight Programmers): "when the sequence length exceeds storage capacity, the model may end up in an overcapacity regime. To properly operate under such a regime, the model should learn to dynamically interact with the memory contents and selectively decide which key-value associations to keep and which ones to delete. The purely additive instruction may be inappropriate for this purpose... endlessly adding new associations to a memory of finite size inevitably will reach a limit."

```python
q = F.normalize(F.silu(q), dim=-1)
k = F.normalize(F.silu(k), dim=-1)
beta = torch.sigmoid(self.w_beta(x)).view(b, 1, t, 1)   # per-token write strength
S = cache if cache is not None else 0.0
v_old = k @ S                 # read the board at this key
u = beta * (v - v_old)        # the delta: only what's actually new
S = S + k.transpose(-1, -2) @ u
o = q @ S                     # read, no denominator
```

Take a single association written as S = k.T @ v. Read back with the same key: k @ (k.T @ v) = (k @ k.T) v = squared norm of k times v; normalize k to unit length and you get v back exactly. Q is also a learned pointer: Wq and Wk read the same residual stream, and the query for a fact points at the key direction that fact was written into. The update first asks what information the current key retrieves from the cache, subtracts that from the value to store, multiplies the key by the difference, and adds the result back. Old information is removed and new information is written in its place.

### DeltaNet (Parallelizing Linear Transformers with Delta Rule)

DeltaNet implements a first-order linear recurrence with generalized Householder transition matrices, enabling chunk-wise parallel forward passes for hardware-efficient linear-time training. It splits inputs and outputs into chunks of size C and computes each chunk's outputs from the final state of the previous chunk plus the q/k/v blocks of the current chunk.

The practical problem is prefill: a direct implementation of the delta rule over T tokens is a sequential loop (v_old = k_i @ S; u_i = b_i (v_i - v_old); S += k_i^T u_i; out_i = q_i S). Even without the delta rule, direct linear-attention prefill is sequential.

Chunked formulation:

```python
for i in range(t//C):
    q_c, k_c, v_c = chunks
    o_prev = q_c @ S                                  # everything up to this block (state first)
    attn = (q_c @ k_c.transpose(-1,-2)).tril()        # masked attention inside the chunk (score first)
    o_curr = attn @ v_c
    o = o_prev + o_curr
    S = S + k_c.transpose(-1,-2) @ v_c
```

Setting C=N recovers standard O(N^2) attention; C=1 gives regular linear attention. Intermediate values trade within-chunk work for hardware utilization; C is often 64 or 128 because tensor-core instructions operate efficiently at that granularity. Cost: fixed piece 2Ld^2 (state work, independent of C) plus growing piece 2LCd (score tiles on the diagonal); full attention is C=L, giving 2L^2 d. C=1 is cheapest in FLOPs but not in wall-clock.

For the delta rule the chunking does not apply directly, because every correction needs the state in order. The authors reparameterize:

S_t = S_{t-1}(I − β_t k_t k_tᵀ) + β_t v_t k_tᵀ ;  o_t = S_t q_t

which lets a chunk compute all C deltas at once (forward substitution for a fast inverse: T = -(K_beta K^T).tril(-1) accumulated row by row, T += I, W = T K_beta, U = T V_beta; then per chunk u_i = U[i] - w_i S; o_inter = q_i S; A_i = (q_i k_i^T).tril(); o_intra = A_i u_i; S += k_i^T u_i; O[i] = o_intra + o_inter).

### Gated Delta Net

The delta rule can forget only an association for which it has a specific replacement. It cannot efficiently clear multiple associations during a context switch or decay memory generally to free capacity. For purely additive linear attention, adding forgetting is one parameter: cache = alpha * S_old + S_new. This is the Mamba-2 contribution: decay the previous cache, then add the new one at full strength. Uniform decay does not account for the varying importance of associations; the delta rule can update one fact but cannot make the rest decay. The Gated Delta rule combines both: alpha = 1 is the pure delta rule, alpha = 0 clears memory. Same chunked reparameterization plus a data-dependent scalar in [0,1]; the γʳ/γⁱ term accounts for cumulative decay (a token written at x and read at x+t has been multiplied by α_x α_{x+1} ... α_{x+t}, the multiplicative analogue of a prefix sum).

### KDA / Kimi Linear

Hybrid models combine several forms of attention in one architecture (e.g. Gated DeltaNet with Mamba). Kimi Linear's central claim: under controlled comparisons it outperformed full attention, presented as a drop-in replacement with better quality and up to 6x higher decode throughput. It improves on Gated DeltaNet with fine-grained gating: a separate decay value per channel (alpha.reshape(nb, C, d)) instead of a single scalar. Beside the DeltaNet Transformer, Kimi Linear introduces three major changes: a hybrid that interleaves Multi-head Latent Attention (MLA) layers; MoE instead of the MLP; extra capacity in DeltaNet through the alpha projection. This is not blind scaling: the per-channel scale gives finer control over memory decay. Each architecture in this progression adds capacity to address a concrete limitation in the preceding system.

### Kimi K3

The KimiK3 backbone contains 23 four-layer macrocycles: three layers of Kimi Delta Attention and a fourth of Multi-head Latent Attention. The first layer uses a dense feed-forward network; every remaining layer uses a latent Mixture-of-Experts. Changes from Kimi Linear: a substantial increase in scale; blockwise AttnRes every 12 layers; MLA query LoRA and output gating; latent-space MoE; SiTU activations; Gated MLA. KDA supplies constant-state recurrent memory, while periodic MLA layers retain full softmax retrieval over the context.

Gated MLA determines how much of each retrieved feature passes from MLA into the residual stream, via element-wise multiplication with a gate projected from the input. MoE: 898 experts in total; two shared process every token; of the remaining 896 the router selects 16 per token. SiTU replaces SiLU-gated activation:

```python
d = x.shape[-1] // 2
gate = x[..., :d].to(torch.float32); up = x[..., d:].to(torch.float32)
situ_a = self.beta * torch.tanh(gate / self.beta) * torch.sigmoid(gate)
if self.linear_beta is not None:
    up = self.linear_beta * torch.tanh(up / self.linear_beta)
return (situ_a * up).to(x.dtype)
```

The model also down-projects inputs to the shared experts and up-projects their final sum. Without a fused kernel the new activation is almost 3x slower than the original path; offsetting that, the experts operate in a compressed latent space, which nearly halves the FLOPs.

AttnRes adds roughly 2% inference latency but provides selective retrieval of earlier representations (mitigating residual dilution and hidden-state growth) and a 1.25x compute advantage. AttnRes and MLA address the same limitation from different directions: KDA layers have constant-size state and must discard information; MLA retrieves from the token context, AttnRes from earlier depth-wise representations.

### AttnRes

Normally the input to each layer is the sum of the original embedding and every preceding layer's output, all weighted equally: h_l = h_1 + Σ_{i=1}^{l-1} f_i(h_i). The problem is the lack of selective access, and because the recurrence is purely additive, later layers must learn increasingly large outputs to influence the accumulated residual, which can destabilize training. AttnRes multiplies each term by a specialized weight: h_l = α_0 h_1 + Σ α_i f_i(h_i), each α_i computed from a query-key dot product (query learned per layer, keys and values from earlier residual-stream states, scores normalized to sum to one). Applying it at every layer would cost too much; applying it at block boundaries (every 12 decoder layers; eight AttnRes blocks across 23 macrocycles) captures most of the benefit.

```python
V = torch.stack(blocks + [partial_block])   # [N+1, B, T, D]
K = norm(V)
logits = torch.einsum('d, n b t d -> n b t', proj.weight.squeeze(), K)
h = torch.einsum('n b t, n b t d -> b t d', logits.softmax(0), V)
```

The central change is not scale alone. Each architectural step changes what the model stores, how it updates that state, or how it retrieves information that a fixed-size state cannot preserve. KimiK3 combines constant-state recurrent memory, periodic softmax retrieval, sparse expert capacity, and selective depth-wise residual access. In essence, a fixed-capacity associative memory needs an eviction policy, since a purely additive linear operation eventually adds interference once at capacity. Learned selection (gating, routing, decay) is necessary, and attention is the most effective selective-read mechanism.
