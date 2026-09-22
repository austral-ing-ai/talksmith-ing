---
source_file: vit-dosovitskiy-2020.html
source_type: article
ingested_at: 2026-09-22
---

# An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (Dosovitskiy et al., 2020) — arXiv 2010.11929

## Provenance
- Original location: research/raw/vit-dosovitskiy-2020.html
- Format: html (ar5iv render of arXiv 2010.11929, 274 KB)
- Author / source (if known): Dosovitskiy et al. — Google Research, Brain Team; ICLR 2021
- Date of original (if known): 2020-10 (v1), 2021-06 (v2)
- Coverage in this record: complete main text (§1–5), Appendix A (multihead self-attention equations) and Appendix D (additional analyses) verbatim; Appendices B and C (hyper-parameter and result tables) omitted.

## Key claims
- "A pure transformer applied directly to sequences of image patches can perform very well on image classification tasks" — no convolutions, "the standard Transformer receives as input a 1D sequence of token embeddings".
- Method (§3.1): reshape image $x\in\mathbb{R}^{H\times W\times C}$ into $N=HW/P^2$ flattened patches of size $P^2\cdot C$ (e.g. 16×16), map them with a trainable linear projection $E$ to $D$ dims ("patch embeddings"), prepend a learnable `[class]` token (as in BERT), add **learnable 1D position embeddings**, then a standard Transformer **encoder**: $z'_\ell=\mathrm{MSA}(\mathrm{LN}(z_{\ell-1}))+z_{\ell-1}$, $z_\ell=\mathrm{MLP}(\mathrm{LN}(z'_\ell))+z'_\ell$ (eq. 1–4). **Pre-LN** ("Layernorm is applied before every block, and residual connections after every block"); MLP with GELU.
- Appendix A restates attention: $[q,k,v]=zU_{qkv}$, $A=\mathrm{softmax}(qk^\top/\sqrt{D_h})$, $\mathrm{SA}(z)=Av$; MSA = $k$ heads concatenated and projected by $U_{msa}$; $D_h=D/k$ to keep compute constant.
- Inductive bias: ViT has much less image-specific inductive bias than CNNs (only the MLP is local and translation-equivariant; patch cutting and fine-tuning resolution adjustment are the only 2D hints). So it needs more data: worse than ResNets on ImageNet alone, better when pre-trained on ImageNet-21k (14M) or JFT-300M (§4.3).
- Results (§4.2, Table 2): ViT-H/14 pre-trained on JFT-300M reaches 88.55% ImageNet, 90.72% ImageNet-ReaL, 94.55% CIFAR-100, 77.63% VTAB (19 tasks), while taking substantially fewer TPUv3-core-days to pre-train (2.5k vs 9.9k for BiT-L, 12.3k for Noisy Student).
- Model sizes (Table 1): ViT-Base L=12, D=768, MLP 3072, 12 heads, 86M; ViT-Large L=24, D=1024, MLP 4096, 16 heads, 307M; ViT-Huge L=32, D=1280, MLP 5120, 16 heads, 632M. Naming ViT-L/16 = Large with 16×16 patches; smaller patch = longer sequence = more compute.
- Inspection (§4.5): learned filters of $E$ resemble basis functions; position embeddings learn 2D image topology (similar rows/columns); some heads attend globally already in the lowest layers ("attention distance" analogous to receptive field); self-supervised masked-patch prediction works but lags supervised pre-training by 4% (§4.6).

## Definitions and terminology
- **Patch** $(P,P)$, **patch embedding** (linear projection $E\in\mathbb{R}^{(P^2\cdot C)\times D}$), **`[class]` token** $x_{\text{class}}$, **position embedding** $E_{pos}\in\mathbb{R}^{(N+1)\times D}$.
- **MSA**: multiheaded self-attention; **SA**: single-head qkv self-attention; $D_h$ head dim, $k$ heads.
- **Inductive bias** (locality, 2D neighbourhood structure, translation equivariance) — present in CNNs, mostly absent in ViT.
- **Hybrid architecture**: patch embedding applied to CNN feature maps instead of raw pixels.
- **Attention distance**: average distance in image space spanned by attention weights, per head and layer.

## Evidence and examples
- Table 1: ViT variants B/L/H with layers, hidden size, MLP size, heads and params.
- Table 2: comparison with BiT-L (ResNet152x4) and Noisy Student on ImageNet, ReaL, CIFAR-10/100, Pets, Flowers, VTAB, with TPUv3-core-days.
- Figure 3 / 4: transfer accuracy vs pre-training dataset size (ImageNet, ImageNet-21k, JFT) and vs number of samples — ViT overtakes ResNets only with enough data.
- Figure 5: performance vs pre-training compute for ViT, ResNets and hybrids (ViT uses 2–4× less compute for the same performance).
- Figure 7: RGB embedding filters, position-embedding similarity, attention distance per layer; Figure 6: attention maps from the output token to the input.
- Appendix D.4: 1D vs 2D vs relative positional embeddings make little difference (Table 8).

## Inconsistencies / open questions
- ViT's best results depend on the private JFT-300M dataset; ImageNet-21k results are the public reference.
- The paper uses learnable 1D positions and pre-LN, both differing from the 2017 paper (sinusoidal, post-LN) — worth pointing out in class when comparing block layouts.
- Appendix B/C tables omitted here; batch sizes, learning rates and per-dataset results live there.

## Images / diagrams
Companion folder `vit-dosovitskiy-2020.html/images/` is **empty**: the source is an ar5iv render whose figures are remote assets, and the orchestrator asked for no new fetches. Each figure is listed below with its caption (captions are also inline in the excerpts) so the diagram-illustrator can redraw from the description if a slide needs it.

### Image 1
- Filename: *(not on disk)*
- Provenance: https://ar5iv.labs.arxiv.org/html/2010.11929/assets/model_scheme.png
- Caption (verbatim): Figure 1: Model overview. We split an image into fixed-size patches, linearly embed each of them, add position embeddings, and feed the resulting sequence of vectors to a standard Transformer encoder. In order to perform classification, we use the standard approach of adding an extra learnable “classification token” to the sequence. The illustration of the Transformer encoder was inspired by Vaswani et al. 2017.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 2
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 1: Details of Vision Transformer model variants.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 3
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 2: Comparison with state of the art on popular image classification benchmarks. We report mean and standard deviation of the accuracies, averaged over three fine-tuning runs. Vision Transformer models pre-trained on the JFT-300M dataset outperform ResNet-based baselines on all datasets, while taking substantially less computational resources to pre-train. ViT pre-trained on the smaller public ImageNet-21k dataset performs well too. ^∗^Slightly improved $88.5\%$ result reported in Touvron et al. 2020.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 4
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 2: Breakdown of VTAB performance in *Natural*, *Specialized*, and *Structured* task groups.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 5
- Filename: *(not on disk)*
- Provenance: https://ar5iv.labs.arxiv.org/html/2010.11929/assets/images/dataset_analysis/imagenet_5shot.png
- Caption (verbatim): Figure 3: Transfer to ImageNet. While large ViT models perform worse than BiT ResNets (shaded area) when pre-trained on small datasets, they shine when pre-trained on larger datasets. Similarly, larger ViT variants overtake smaller ones as the dataset grows.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 6
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 5: Performance versus pre-training compute for different architectures: Vision Transformers, ResNets, and hybrids. Vision Transformers generally outperform ResNets with the same computational budget. Hybrids improve upon pure Transformers for smaller model sizes, but the gap vanishes for larger models.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 7
- Filename: *(not on disk)*
- Provenance: https://ar5iv.labs.arxiv.org/html/2010.11929/assets/20201002_selected_attention_examples.png
- Caption (verbatim): Figure 6: Representative examples of attention from the output token to the input space. See Appendix D.7 for details.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 8
- Filename: *(not on disk)*
- Provenance: https://ar5iv.labs.arxiv.org/html/2010.11929/assets/20201002_rgb_filter_pca.png, https://ar5iv.labs.arxiv.org/html/2010.11929/assets/20201002_position_embeddings_17085772_1.png
- Caption (verbatim): Figure 7: **Left:** Filters of the initial linear embedding of RGB values of ViT-L/32. **Center:** Similarity of position embeddings of ViT-L/32. Tiles show the cosine similarity between the position embedding of the patch with the indicated row and column and the position embeddings of all other patches. **Right:** Size of attended area by head and network depth. Each dot shows the mean attention distance across images for one of 16 heads at one layer. See Appendix D.7 for details.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 9
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 3: Hyperparameters for training. All models are trained with a batch size of 4096 and learning rate warmup of 10k steps. For ImageNet we found it beneficial to additionally apply gradient clipping at global norm 1. Training resolution is 224.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 10
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 4: Hyperparameters for fine-tuning. All models are fine-tuned with cosine learning rate decay, a batch size of 512, no weight decay, and grad clipping at global norm 1. If not mentioned otherwise, fine-tuning resolution is 384.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 11
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 5: Top1 accuracy (in %) of Vision Transformer on various datasets when pre-trained on ImageNet, ImageNet-21k or JFT300M. These values correspond to Figure 4 in the main text. Models are fine-tuned at 384 resolution. Note that the ImageNet results are computed without additional techniques (Polyak averaging and 512 resolution images) used to achieve results in Table 2.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 12
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 6: Detailed results of model scaling experiments. These correspond to Figure 5 in the main paper. We show transfer accuracy on several datasets, as well as the pre-training compute (in exaFLOPs).
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 13
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 7: Fine-tuning ResNet models pre-trained with Adam and SGD.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 14
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 8: Scaling different model dimensions of the Vision Transformer.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 15
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 9: Comparison of class-token and global average pooling classifiers. Both work similarly well, but require different learning-rates.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 16
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 8: Results of the ablation study on positional embeddings with ViT-B/16 model evaluated on ImageNet 5-shot linear.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 17
- Filename: *(not on disk)*
- Provenance: https://ar5iv.labs.arxiv.org/html/2010.11929/assets/20200930_position_embeddings_16490619_1.png, https://ar5iv.labs.arxiv.org/html/2010.11929/assets/20200930_position_embeddings_17192124_1.png, https://ar5iv.labs.arxiv.org/html/2010.11929/assets/20200930_position_embeddings_17192217_1.png
- Caption (verbatim): Figure 10: Position embeddings of models trained with different hyperparameters.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 18
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 11: Size of attended area by head and network depth. Attention distance was computed for 128 example images by averaging the distance between the query pixel and all other pixels, weighted by the attention weight. Each dot shows the mean attention distance across images for one of 16 heads at one layer. Image width is 224 pixels.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 19
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 12: **Left:** Real wall-clock timings of various architectures across input sizes. ViT models have speed comparable to similar ResNets. **Right**: Largest per-core batch-size fitting on device with various architectures across input sizes. ViT models are clearly more memory-efficient.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 20
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Figure 13: Performance of Axial-Attention based models, in terms of top-1 accuracy on ImageNet 5-shot linear, versus their speed in terms of number of FLOPs (**left**) and inference time (**left**).
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 21
- Filename: *(not on disk)*
- Provenance: https://ar5iv.labs.arxiv.org/html/2010.11929/assets/20201002_batch_attention_examples_compressed.png
- Caption (verbatim): Figure 14: Further example attention maps as in Figure 6 (random selection).
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

### Image 22
- Filename: *(not on disk)*
- Provenance: table/algorithm rendered inline (no bitmap)
- Caption (verbatim): Table 9: Breakdown of VTAB-1k performance across tasks.
- Depiction / Why it matters / Transcribed text: not transcribed (process_images: no; bytes not fetched)

## Raw / preserved excerpts
**Authors:** Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby (Google Research, Brain Team)

## Abstract


While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited.
In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure in place.
We show that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks.
When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision Transformer (ViT) attains excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train. [footnote: ^1^

Fine-tuning code and pre-trained models are available at https://github.com/google-research/vision_transformer]

## 1 Introduction


Self-attention-based architectures, in particular Transformers (Vaswani et al. 2017), have become the model of choice in natural language processing (NLP).
The dominant approach is to pre-train on a large text corpus and then fine-tune on a smaller task-specific dataset (Devlin et al. 2019).
Thanks to Transformers’ computational efficiency and scalability, it has become possible to train models of unprecedented size, with over 100B parameters (Brown et al. 2020; Lepikhin et al. 2020).
With the models and datasets growing, there is still no sign of saturating performance.

In computer vision, however, convolutional architectures remain dominant (LeCun et al. 1989; Krizhevsky et al. 2012; He et al. 2016).
Inspired by NLP successes, multiple works try combining CNN-like architectures with self-attention (Wang et al. 2018; Carion et al. 2020), some replacing the convolutions entirely (Ramachandran et al. 2019; Wang et al. 2020a).
The latter models, while theoretically efficient, have not yet been scaled effectively on modern hardware accelerators due to the use of specialized attention patterns.
Therefore, in large-scale image recognition, classic ResNet-like architectures are still state of the art (Mahajan et al. 2018; Xie et al. 2020; Kolesnikov et al. 2020).

Inspired by the Transformer scaling successes in NLP, we experiment with applying a standard Transformer directly to images, with the fewest possible modifications.
To do so, we split an image into patches and provide the sequence of linear embeddings of these patches as an input to a Transformer.
Image patches are treated the same way as tokens (words) in an NLP application.
We train the model on image classification in supervised fashion.

When trained on mid-sized datasets such as ImageNet without strong regularization, these models yield modest accuracies of a few percentage points below ResNets of comparable size.
This seemingly discouraging outcome may be expected: Transformers lack some of the inductive biases inherent to CNNs, such as translation equivariance and locality, and therefore do not generalize well when trained on insufficient amounts of data.

However, the picture changes if the models are trained on larger datasets (14M-300M images).
We find that large scale training trumps inductive bias.
Our Vision Transformer (ViT) attains excellent results when pre-trained at sufficient scale and transferred to tasks with fewer datapoints.
When pre-trained on the public ImageNet-21k dataset or the in-house JFT-300M dataset, ViT approaches or beats state of the art on multiple image recognition benchmarks.
In particular, the best model reaches the accuracy of $88.55\%$ on ImageNet, $90.72\%$ on ImageNet-ReaL, $94.55\%$ on CIFAR-100, and $77.63\%$ on the VTAB suite of 19 tasks.

## 2 Related Work


Transformers were proposed by Vaswani et al. 2017 for machine translation, and have since become the state of the art method in many NLP tasks. Large Transformer-based models are often pre-trained on large corpora and then fine-tuned for the task at hand: BERT (Devlin et al. 2019) uses a denoising self-supervised pre-training task, while the GPT line of work uses language modeling as its pre-training task (Radford et al. 2018; Radford et al. 2019; Brown et al. 2020).

Naive application of self-attention to images would require that each pixel attends to every other pixel. With quadratic cost in the number of pixels, this does not scale to realistic input sizes.
Thus, to apply Transformers in the context of image processing, several approximations have been tried in the past.
Parmar et al. 2018 applied the self-attention only in local neighborhoods for each query pixel instead of globally.
Such local multi-head dot-product self attention blocks can completely replace convolutions (Hu et al. 2019; Ramachandran et al. 2019; Zhao et al. 2020).
In a different line of work, Sparse Transformers (Child et al. 2019) employ scalable approximations to global self-attention in order to be applicable to images.
An alternative way to scale attention is to apply it in blocks of varying sizes (Weissenborn et al. 2019), in the extreme case only along individual axes (Ho et al. 2019; Wang et al. 2020a).
Many of these specialized attention architectures demonstrate promising results on computer vision tasks, but require complex engineering to be implemented efficiently on hardware accelerators.

Most related to ours is the model of Cordonnier et al. 2020, which extracts patches of size $2\times 2$ from the input image and applies full self-attention on top. This model is very similar to ViT, but our work goes further to demonstrate that large scale pre-training makes vanilla transformers competitive with (or even better than) state-of-the-art CNNs. Moreover, Cordonnier et al. 2020 use a small patch size of $2\times 2$ pixels, which makes the model applicable only to small-resolution images, while we handle medium-resolution images as well.

There has also been a lot of interest in combining convolutional neural networks (CNNs) with forms of self-attention, e.g. by augmenting feature maps for image classification (Bello et al. 2019) or by further processing the output of a CNN using self-attention, e.g. for object detection (Hu et al. 2018; Carion et al. 2020), video processing (Wang et al. 2018; Sun et al. 2019), image classification (Wu et al. 2020), unsupervised object discovery (Locatello et al. 2020), or unified text-vision tasks (Chen et al. 2020c; Lu et al. 2019; Li et al. 2019).

Another recent related model is image GPT (iGPT) (Chen et al. 2020a), which applies Transformers to image pixels after reducing image resolution and color space. The model is trained in an unsupervised fashion as a generative model, and the resulting representation can then be fine-tuned or probed linearly for classification performance, achieving a maximal accuracy of 72% on ImageNet.

Our work adds to the increasing collection of papers that explore image recognition at larger scales than the standard ImageNet dataset.
The use of additional data sources allows to achieve state-of-the-art results on standard benchmarks (Mahajan et al. 2018; Touvron et al. 2019; Xie et al. 2020).
Moreover, Sun et al. 2017 study how CNN performance scales with dataset size, and Kolesnikov et al. 2020; Djolonga et al. 2020 perform an empirical exploration of CNN transfer learning from large scale datasets such as ImageNet-21k and JFT-300M.
We focus on these two latter datasets as well, but train Transformers instead of ResNet-based models used in prior works.

## 3 Method


> **Figure 1: Model overview. We split an image into fixed-size patches, linearly embed each of them, add position embeddings, and feed the resulting sequence of vectors to a standard Transformer encoder. In order to perform classification, we use the standard approach of adding an extra learnable “classification token” to the sequence. The illustration of the Transformer encoder was inspired by Vaswani et al. 2017.**
> (image not fetched: /html/2010.11929/assets/model_scheme.png)

| [image: /html/2010.11929/assets/model_scheme.png] |
|---|

In model design we follow the original Transformer (Vaswani et al. 2017) as closely as possible.
An advantage of this intentionally simple setup is that scalable NLP Transformer architectures – and their efficient implementations – can be used almost out of the box.

### 3.1 Vision Transformer (ViT)

An overview of the model is depicted in Figure 1.
The standard Transformer receives as input a 1D sequence of token embeddings.
To handle 2D images, we reshape the image $\mathbf{x}\in\mathbb{R}^{H\times W\times C}$ into a sequence of flattened 2D patches $\mathbf{x}_{p}\in\mathbb{R}^{N\times(P^{2}\cdot C)}$, where $(H,W)$ is the resolution of the original image, $C$ is the number of channels, $(P,P)$ is the resolution of each image patch, and $N=HW/P^{2}$ is the resulting number of patches, which also serves as the effective input sequence length for the Transformer.
The Transformer uses constant latent vector size $D$ through all of its layers, so we flatten the patches and map to $D$ dimensions with a trainable linear projection (Eq. 1).
We refer to the output of this projection as the patch embeddings.

Similar to BERT’s `[class]` token, we prepend a learnable embedding to the sequence of embedded patches ($\mathbf{z}_{0}^{0}=\mathbf{x}_{\text{class}}$), whose state at the output of the Transformer encoder ($\mathbf{z}^{0}_{L}$) serves as the image representation $\mathbf{y}$ (Eq. 4).
Both during pre-training and fine-tuning, a classification head is attached to $\mathbf{z}^{0}_{L}$.
The classification head is implemented by a MLP with one hidden layer at pre-training time and by a single linear layer at fine-tuning time.

Position embeddings are added to the patch embeddings to retain positional information.
We use standard learnable 1D position embeddings, since we have not observed significant performance gains from using more advanced 2D-aware position embeddings (Appendix D.4).
The resulting sequence of embedding vectors serves as input to the encoder.

The Transformer encoder (Vaswani et al. 2017) consists of alternating layers of multiheaded self-attention (MSA, see Appendix A) and MLP blocks (Eq. 2, 3).
Layernorm (LN) is applied before every block, and residual connections after every block (Wang et al. 2019; Baevski & Auli 2019).
The MLP contains two layers with a GELU non-linearity.

$$\displaystyle\mathbf{z}_{0} \displaystyle=[\mathbf{x}_{\text{class}};\,\mathbf{x}^{1}_{p}\mathbf{E};\,\mathbf{x}^{2}_{p}\mathbf{E};\cdots;\,\mathbf{x}^{N}_{p}\mathbf{E}]+\mathbf{E}_{pos}, \displaystyle\mathbf{E}\in\mathbb{R}^{(P^{2}\cdot C)\times D},\,\mathbf{E}_{pos}\in\mathbb{R}^{(N+1)\times D} \quad (1) \\
\displaystyle\mathbf{z^{\prime}}_{\ell} \displaystyle=\operatorname{MSA}(\operatorname{LN}(\mathbf{z}_{\ell-1}))+\mathbf{z}_{\ell-1}, \displaystyle\ell=1\ldots L \quad (2) \\
\displaystyle\mathbf{z}_{\ell} \displaystyle=\operatorname{MLP}(\operatorname{LN}(\mathbf{z^{\prime}}_{\ell}))+\mathbf{z^{\prime}}_{\ell}, \displaystyle\ell=1\ldots L \quad (3) \\
\displaystyle\mathbf{y} \displaystyle=\operatorname{LN}(\mathbf{z}_{L}^{0}) \quad (4)$$

##### Inductive bias.

We note that Vision Transformer has much less image-specific inductive bias than CNNs.
In CNNs, locality, two-dimensional neighborhood structure, and translation equivariance are baked into each layer throughout the whole model.
In ViT, only MLP layers are local and translationally equivariant, while the self-attention layers are global.
The two-dimensional neighborhood structure is used very sparingly: in the beginning of the model by cutting the image into patches and at fine-tuning time for adjusting the position embeddings for images of different resolution (as described below).
Other than that, the position embeddings at initialization time carry no information about the 2D positions of the patches and all spatial relations between the patches have to be learned from scratch.

##### Hybrid Architecture.

As an alternative to raw image patches, the input sequence can be formed from feature maps of a CNN (LeCun et al. 1989).
In this hybrid model, the patch embedding projection $\mathbf{E}$ (Eq. 1) is applied to patches extracted from a CNN feature map.
As a special case, the patches can have spatial size 1x1, which means that the input sequence is obtained by simply flattening the spatial dimensions of the feature map and projecting to the Transformer dimension.
The classification input embedding and position embeddings are added as described above.

### 3.2 Fine-tuning and Higher Resolution

Typically, we pre-train ViT on large datasets, and fine-tune to (smaller) downstream tasks.
For this, we remove the pre-trained prediction head and attach a zero-initialized $D\times K$ feedforward layer, where $K$ is the number of downstream classes.
It is often beneficial to fine-tune at higher resolution than pre-training (Touvron et al. 2019; Kolesnikov et al. 2020).
When feeding images of higher resolution, we keep the patch size the same, which results in a larger effective sequence length.
The Vision Transformer can handle arbitrary sequence lengths (up to memory constraints), however, the pre-trained position embeddings may no longer be meaningful.
We therefore perform 2D interpolation of the pre-trained position embeddings, according to their location in the original image.
Note that this resolution adjustment and patch extraction are the only points at which an inductive bias about the 2D structure of the images is manually injected into the Vision Transformer.

## 4 Experiments


We evaluate the representation learning capabilities of ResNet, Vision Transformer (ViT), and the hybrid.
To understand the data requirements of each model, we pre-train on datasets of varying size and evaluate many benchmark tasks.
When considering the computational cost of pre-training the model, ViT performs very favourably, attaining state of the art on most recognition benchmarks at a lower pre-training cost.
Lastly, we perform a small experiment using self-supervision, and show that self-supervised ViT holds promise for the future.

### 4.1 Setup

**Datasets.**
To explore model scalability, we use the ILSVRC-2012 ImageNet dataset with 1k classes and 1.3M images (we refer to it as ImageNet in what follows),
its superset ImageNet-21k with 21k classes and 14M images (Deng et al. 2009),
and JFT (Sun et al. 2017) with 18k classes and 303M high-resolution images.
We de-duplicate the pre-training datasets w.r.t. the test sets of the downstream tasks following Kolesnikov et al. 2020.
We transfer the models trained on these dataset to several benchmark tasks:
ImageNet on the original validation labels and the cleaned-up ReaL labels (Beyer et al. 2020),
CIFAR-10/100 (Krizhevsky 2009),
Oxford-IIIT Pets (Parkhi et al. 2012),
and Oxford Flowers-102 (Nilsback & Zisserman 2008).
For these datasets, pre-processing follows Kolesnikov et al. 2020.

We also evaluate on the 19-task VTAB classification suite (Zhai et al. 2019b).
VTAB evaluates low-data transfer to diverse tasks, using 1 000 training examples per task.
The tasks are divided into three groups:
*Natural* – tasks like the above, Pets, CIFAR, etc.
*Specialized* – medical and satellite imagery, and
*Structured* – tasks that require geometric understanding like localization.

**Model Variants.**
We base ViT configurations on those used for BERT (Devlin et al. 2019), as summarized in Table 1.
The “Base” and “Large” models are directly adopted from BERT and we add the larger “Huge” model.
In what follows we use brief notation to indicate the model size and the input patch size: for instance, ViT-L/16 means the “Large” variant with $16\times 16$ input patch size.
Note that the Transformer’s sequence length is inversely proportional to the square of the patch size, thus models with smaller patch size are computationally more expensive.

For the baseline CNNs, we use ResNet (He et al. 2016), but replace the Batch Normalization layers (Ioffe & Szegedy 2015) with Group Normalization (Wu & He 2018), and used standardized convolutions (Qiao et al. 2019).
These modifications improve transfer (Kolesnikov et al. 2020), and we denote the modified model “ResNet (BiT)”.
For the hybrids, we feed the intermediate feature maps into ViT with patch size of one “pixel”.
To experiment with different sequence lengths, we either
(i) take the output of stage 4 of a regular ResNet50 or
(ii) remove stage 4, place the same number of layers in stage 3 (keeping the total number of layers), and take the output of this extended stage 3.
Option (ii) results in a 4x longer sequence length, and a more expensive ViT model.

> **Table 1: Details of Vision Transformer model variants.**

| Model | Layers | Hidden size $D$ | MLP size | Heads | Params |
|---|---|---|---|---|---|
| ViT-Base | 12 | 768 | 3072 | 12 | 86M |
| ViT-Large | 24 | 1024 | 4096 | 16 | 307M |
| ViT-Huge | 32 | 1280 | 5120 | 16 | 632M |

**Training & Fine-tuning.**
We train all models, including ResNets, using Adam (Kingma & Ba 2015) with $\beta_{1}=0.9$, $\beta_{2}=0.999$, a batch size of 4096 and apply a high weight decay of $0.1$, which we found to be useful for transfer of all models (Appendix D.1 shows that, in contrast to common practices, Adam works slightly better than SGD for ResNets in our setting).
We use a linear learning rate warmup and decay, see Appendix B.1 for details.
For fine-tuning we use SGD with momentum, batch size 512, for all models, see Appendix B.1.1.
For ImageNet results in Table 2, we fine-tuned at higher resolution: $512$ for ViT-L/16 and $518$ for ViT-H/14, and also used Polyak & Juditsky 1992 averaging with a factor of $0.9999$ (Ramachandran et al. 2019; Wang et al. 2020b).

**Metrics.**
We report results on downstream datasets either through few-shot or fine-tuning accuracy.
Fine-tuning accuracies capture the performance of each model after fine-tuning it on the respective dataset.
Few-shot accuracies are obtained by solving a regularized least-squares regression problem that maps the (frozen) representation of a subset of training images to $\{-1,1\}^{K}$ target vectors.
This formulation allows us to recover the exact solution in closed form.
Though we mainly focus on fine-tuning performance, we sometimes use linear few-shot accuracies for fast on-the-fly evaluation where fine-tuning would be too costly.

### 4.2 Comparison to State of the Art

We first compare our largest models – ViT-H/14 and ViT-L/16  – to state-of-the-art CNNs from the literature.
The first comparison point is Big Transfer (BiT) (Kolesnikov et al. 2020), which performs supervised transfer learning with large ResNets.
The second is Noisy Student (Xie et al. 2020),
which is a large EfficientNet trained using semi-supervised learning on ImageNet and JFT-300M with the labels removed.
Currently, Noisy Student is the state of the art on ImageNet and BiT-L on the other datasets reported here.
All models were trained on TPUv3 hardware, and we report the number of TPUv3-core-days taken to pre-train each of them, that is, the number of TPU v3 cores (2 per chip) used for training multiplied by the training time in days.

> **Table 2: Comparison with state of the art on popular image classification benchmarks. We report mean and standard deviation of the accuracies, averaged over three fine-tuning runs. Vision Transformer models pre-trained on the JFT-300M dataset outperform ResNet-based baselines on all datasets, while taking substantially less computational resources to pre-train. ViT pre-trained on the smaller public ImageNet-21k dataset performs well too. ^∗^Slightly improved $88.5\%$ result reported in Touvron et al. 2020.**

|  | Ours-JFT | Ours-JFT | Ours-I21k | BiT-L | Noisy Student |
|---|---|---|---|---|---|
|  | (ViT-H/14) | (ViT-L/16) | (ViT-L/16) | (ResNet152x4) | (EfficientNet-L2) |
| ImageNet | $\mathbf{88.55}{\scriptstyle\,\pm\,0.04}$ | $87.76{\scriptstyle\,\pm\,0.03}$ | $85.30{\scriptstyle\,\pm\,0.02}$ | $87.54{\scriptstyle\,\pm\,0.02}$ | $88.4/88.5^{*}$ |
| ImageNet ReaL | $\mathbf{90.72}{\scriptstyle\,\pm\,0.05}$ | $90.54{\scriptstyle\,\pm\,0.03}$ | $88.62{\scriptstyle\,\pm\,0.05}$ | $90.54$ | $90.55$ |
| CIFAR-10 | $\mathbf{99.50}{\scriptstyle\,\pm\,0.06}$ | $99.42{\scriptstyle\,\pm\,0.03}$ | $99.15{\scriptstyle\,\pm\,0.03}$ | $99.37{\scriptstyle\,\pm\,0.06}$ | $-$ |
| CIFAR-100 | $\mathbf{94.55}{\scriptstyle\,\pm\,0.04}$ | $93.90{\scriptstyle\,\pm\,0.05}$ | $93.25{\scriptstyle\,\pm\,0.05}$ | $93.51{\scriptstyle\,\pm\,0.08}$ | $-$ |
| Oxford-IIIT Pets | $\mathbf{97.56}{\scriptstyle\,\pm\,0.03}$ | $97.32{\scriptstyle\,\pm\,0.11}$ | $94.67{\scriptstyle\,\pm\,0.15}$ | $96.62{\scriptstyle\,\pm\,0.23}$ | $-$ |
| Oxford Flowers-102 | $99.68{\scriptstyle\,\pm\,0.02}$ | $\mathbf{99.74}{\scriptstyle\,\pm\,0.00}$ | $99.61{\scriptstyle\,\pm\,0.02}$ | $99.63{\scriptstyle\,\pm\,0.03}$ | $-$ |
| VTAB (19 tasks) | $\mathbf{77.63}{\scriptstyle\,\pm\,0.23}$ | $76.28{\scriptstyle\,\pm\,0.46}$ | $72.72{\scriptstyle\,\pm\,0.21}$ | $76.29{\scriptstyle\,\pm\,1.70}$ | $-$ |
| TPUv3-core-days | $2.5$k | $0.68$k | $0.23$k | $9.9$k | $12.3$k |

> **Figure 2: Breakdown of VTAB performance in *Natural*, *Specialized*, and *Structured* task groups.**

Table 2 shows the results.
The smaller ViT-L/16 model pre-trained on JFT-300M outperforms BiT-L (which is pre-trained on the same dataset) on all tasks, while requiring substantially less computational resources to train.
The larger model, ViT-H/14, further improves the performance, especially on the more challenging datasets – ImageNet, CIFAR-100, and the VTAB suite.
Interestingly, this model still took substantially less compute to pre-train than prior state of the art. However, we note that pre-training efficiency may be affected not only by the architecture choice, but also other parameters, such as training schedule, optimizer, weight decay, etc.
We provide a controlled study of performance vs. compute for different architectures in Section 4.4.
Finally, the ViT-L/16 model pre-trained on the public ImageNet-21k dataset performs well on most datasets too, while taking fewer resources to pre-train: it could be trained using a standard cloud TPUv3 with 8 cores in approximately 30 days.

Figure 2 decomposes the VTAB tasks into their respective groups, and compares to previous SOTA methods on this benchmark:
BiT,
VIVI – a ResNet co-trained on ImageNet and Youtube (Tschannen et al. 2020),
and S4L – supervised plus semi-supervised learning on ImageNet (Zhai et al. 2019a).
ViT-H/14 outperforms BiT-R152x4, and other methods, on the *Natural* and *Structured* tasks.
On the *Specialized* the performance of the top two models is similar.

### 4.3 Pre-training Data Requirements

> **Figure 3: Transfer to ImageNet. While large ViT models perform worse than BiT ResNets (shaded area) when pre-trained on small datasets, they shine when pre-trained on larger datasets. Similarly, larger ViT variants overtake smaller ones as the dataset grows.**
> (image not fetched: /html/2010.11929/assets/images/dataset_analysis/imagenet_5shot.png)

The Vision Transformer performs well when pre-trained on a large JFT-300M dataset.
With fewer inductive biases for vision than ResNets, how crucial is the dataset size?
We perform two series of experiments.

First, we pre-train ViT models on datasets of increasing size: ImageNet, ImageNet-21k, and JFT-300M.
To boost the performance on the smaller datasets, we optimize three basic regularization parameters – weight decay, dropout, and label smoothing.
Figure 4 shows the results after fine-tuning to ImageNet (results on other datasets are shown in Table 5) [footnote: ^2^

Note that the ImageNet pre-trained models are also fine-tuned, but again on ImageNet. This is because the resolution increase during fine-tuning improves the performance.] .
When pre-trained on the smallest dataset, ImageNet, ViT-Large models underperform compared to ViT-Base models, despite (moderate) regularization.
With ImageNet-21k pre-training, their performances are similar.
Only with JFT-300M, do we see the full benefit of larger models.
Figure 4 also shows the performance region spanned by BiT models of different sizes.
The BiT CNNs outperform ViT on ImageNet, but with the larger datasets, ViT overtakes.

Second, we train our models on random subsets of 9M, 30M, and 90M as well as the full JFT-300M dataset.
We do not perform additional regularization on the smaller subsets and use the same hyper-parameters for all settings.
This way, we assess the intrinsic model properties, and not the effect of regularization.
We do, however, use early-stopping, and report the best validation accuracy achieved during training.
To save compute, we report few-shot linear accuracy instead of full fine-tuning accuracy.
Figure 4 contains the results.
Vision Transformers overfit more than ResNets with comparable computational cost on smaller datasets.
For example, ViT-B/32 is slightly faster than ResNet50; it performs much worse on the 9M subset, but better on 90M+ subsets.
The same is true for ResNet152x2 and ViT-L/16.
This result reinforces the intuition that the convolutional inductive bias is useful for smaller datasets, but for larger ones, learning the relevant patterns directly from data is sufficient, even beneficial.

Overall, the few-shot results on ImageNet (Figure 4), as well as the low-data results on VTAB (Table 2) seem promising for very low-data transfer. Further analysis of few-shot properties of ViT is an exciting direction of future work.

> **Figure 5: Performance versus pre-training compute for different architectures: Vision Transformers, ResNets, and hybrids. Vision Transformers generally outperform ResNets with the same computational budget. Hybrids improve upon pure Transformers for smaller model sizes, but the gap vanishes for larger models.**

### 4.4 Scaling Study

We perform a controlled scaling study of different models by evaluating transfer performance from JFT-300M.
In this setting data size does not bottleneck the models’ performances, and we assess performance versus pre-training cost of each model.
The model set includes:
7 ResNets, R50x1, R50x2 R101x1, R152x1, R152x2, pre-trained for 7 epochs, plus R152x2 and R200x3 pre-trained for 14 epochs;
6 Vision Transformers, ViT-B/32, B/16, L/32, L/16, pre-trained for 7 epochs, plus L/16 and H/14 pre-trained for 14 epochs;
and 5 hybrids, R50+ViT-B/32, B/16, L/32, L/16 pre-trained for 7 epochs, plus R50+ViT-L/16 pre-trained for 14 epochs (for hybrids, the number at the end of the model name stands not for the patch size, but for the total dowsampling ratio in the ResNet backbone).

Figure 5 contains the transfer performance versus total pre-training compute (see Appendix D.5 for details on computational costs).
Detailed results per model are provided in Table 6 in the Appendix.
A few patterns can be observed.
First, Vision Transformers dominate ResNets on the performance/compute trade-off.
ViT uses approximately $2-4\times$ less compute to attain the same performance (average over 5 datasets).
Second, hybrids slightly outperform ViT at small computational budgets, but the difference vanishes for larger models.
This result is somewhat surprising, since one might expect convolutional local feature processing to assist ViT at any size.
Third, Vision Transformers appear not to saturate within the range tried, motivating future scaling efforts.

### 4.5 Inspecting Vision Transformer

> **Figure 6: Representative examples of attention from the output token to the input space. See Appendix D.7 for details.**
> (image not fetched: /html/2010.11929/assets/20201002_selected_attention_examples.png)

To begin to understand how the Vision Transformer processes image data, we analyze its internal representations.
The first layer of the Vision Transformer linearly projects the flattened patches into a lower-dimensional space (Eq. 1).
Figure 7 (left) shows the top principal components of the the learned embedding filters.
The components resemble plausible basis functions for a low-dimensional representation of the fine structure within each patch.

After the projection, a learned position embedding is added to the patch representations.
Figure 7 (center) shows that the model learns to encode distance within the image in the similarity of position embeddings, i.e. closer patches tend to have more similar position embeddings.
Further, the row-column structure appears; patches in the same row/column have similar embeddings.
Finally, a sinusoidal structure is sometimes apparent for larger grids (Appendix D).
That the position embeddings learn to represent 2D image topology explains why hand-crafted 2D-aware embedding variants do not yield improvements (Appendix D.4).

> **Figure 7: **Left:** Filters of the initial linear embedding of RGB values of ViT-L/32. **Center:** Similarity of position embeddings of ViT-L/32. Tiles show the cosine similarity between the position embedding of the patch with the indicated row and column and the position embeddings of all other patches. **Right:** Size of attended area by head and network depth. Each dot shows the mean attention distance across images for one of 16 heads at one layer. See Appendix D.7 for details.**
> (image not fetched: /html/2010.11929/assets/20201002_rgb_filter_pca.png, /html/2010.11929/assets/20201002_position_embeddings_17085772_1.png)

Self-attention allows ViT to integrate information across the entire image even in the lowest layers. We investigate to what degree the network makes use of this capability. Specifically, we compute the average distance in image space across which information is integrated, based on the attention weights (Figure 7, right). This “attention distance” is analogous to receptive field size in CNNs. We find that some heads attend to most of the image already in the lowest layers, showing that the ability to integrate information globally is indeed used by the model. Other attention heads have consistently small attention distances in the low layers. This highly localized attention is less pronounced in hybrid models that apply a ResNet before the Transformer (Figure 7, right), suggesting that it may serve a similar function as early convolutional layers in CNNs.
Further, the attention distance increases with network depth.
Globally, we find that the model attends to image regions that are semantically relevant for classification (Figure 6).

### 4.6 Self-supervision

Transformers show impressive performance on NLP tasks. However, much of their success stems not only from their excellent scalability but also from large scale self-supervised pre-training (Devlin et al. 2019; Radford et al. 2018). We also perform a preliminary exploration on *masked patch prediction* for self-supervision, mimicking the masked language modeling task used in BERT. With self-supervised pre-training, our smaller ViT-B/16 model achieves 79.9% accuracy on ImageNet, a significant improvement of 2% to training from scratch, but still 4% behind supervised pre-training. Appendix B.1.2 contains further details.
We leave exploration of contrastive pre-training (Chen et al. 2020b; He et al. 2020; Bachman et al. 2019; Hénaff et al. 2020) to future work.

## 5 Conclusion


We have explored the direct application of Transformers to image recognition.
Unlike prior works using self-attention in computer vision, we do not introduce image-specific inductive biases into the architecture apart from the initial patch extraction step.
Instead, we interpret an image as a sequence of patches and process it by a standard Transformer encoder as used in NLP.
This simple, yet scalable, strategy works surprisingly well when coupled with pre-training on large datasets.
Thus, Vision Transformer matches or exceeds the state of the art on many image classification datasets, whilst being relatively cheap to pre-train.

While these initial results are encouraging, many challenges remain.
One is to apply ViT to other computer vision tasks, such as detection and segmentation.
Our results, coupled with those in Carion et al. 2020, indicate the promise of this approach.
Another challenge is to continue exploring self-supervised pre-training methods.
Our initial experiments show improvement from self-supervised pre-training, but there is still large gap between self-supervised and large-scale supervised pre-training.
Finally, further scaling of ViT would likely lead to improved performance.

## Acknowledgements


The work was performed in Berlin, Zürich, and Amsterdam. We thank many colleagues at Google for their help, in particular Andreas Steiner for crucial help with the infrastructure and the open-source release of the code; Joan Puigcerver and Maxim Neumann for help with the large-scale training infrastructure; Dmitry Lepikhin, Aravindh Mahendran, Daniel Keysers, Mario Lučić, Noam Shazeer, Ashish Vaswani, and Colin Raffel for useful discussions.

## Appendix


## Appendix A Multihead Self-attention


Standard $\mathbf{qkv}$ self-attention (SA, Vaswani et al. 2017) is a popular building block for neural architectures. For each element in an input sequence $\mathbf{z}\in\mathbb{R}^{N\times D}$, we compute a weighted sum over all values $\mathbf{v}$ in the sequence. The attention weights $A_{ij}$ are based on the pairwise similarity between two elements of the sequence and their respective query $\mathbf{q}^{i}$ and key $\mathbf{k}^{j}$ representations.

$$\displaystyle[\mathbf{q},\mathbf{k},\mathbf{v}] \displaystyle=\mathbf{z}\mathbf{U}_{qkv} \displaystyle\mathbf{U}_{qkv} \displaystyle\in\mathbb{R}^{D\times 3D_{h}}, \quad (5) \\
\displaystyle A \displaystyle=\operatorname{softmax}\left(\mathbf{q}\mathbf{k}^{\top}/\sqrt{D_{h}}\right) \displaystyle A \displaystyle\in\mathbb{R}^{N\times N}, \quad (6) \\
\displaystyle\operatorname{SA}(\mathbf{z}) \displaystyle=A\mathbf{v}\,. \quad (7)$$

Multihead self-attention (MSA) is an extension of SA in which we run $k$ self-attention operations, called “heads”, in parallel, and project their concatenated outputs. To keep compute and number of parameters constant when changing $k$, $D_{h}$ (Eq. 5) is typically set to $D/k$.

$$\displaystyle\operatorname{MSA}(\mathbf{z}) \displaystyle=[\operatorname{SA}_{1}(z);\operatorname{SA}_{2}(z);\cdots;\operatorname{SA}_{k}(z)]\,\mathbf{U}_{msa} \displaystyle\mathbf{U}_{msa}\in\mathbb{R}^{k\cdot D_{h}\times D} \quad (8)$$



> *[Sections omitted from this record: Appendix B Experiment details; Appendix C Additional Results. Appendix B (training/fine-tuning hyper-parameter tables, self-supervision details) and C (additional result tables) omitted; Appendix A (multihead self-attention) and D (analyses: SGD vs Adam, shape, head type, positional embedding, compute, axial attention, attention distance/maps, ObjectNet, VTAB) kept]*

## Appendix D Additional Analyses


### D.1 SGD vs. Adam for ResNets

ResNets are typically trained with SGD and our use of Adam as optimizer is quite unconventional.
Here we show the experiments that motivated this choice.
Namely, we compare the fine-tuning performance of two ResNets – 50x1 and 152x2 – pre-trained on JFT with SGD and Adam.
For SGD, we use the hyperparameters recommended by Kolesnikov et al. 2020.
Results are presented in Table 7.
Adam pre-training outperforms SGD pre-training on most datasets and on average.
This justifies the choice of Adam as the optimizer used to pre-train ResNets on JFT.
Note that the absolute numbers are lower than those reported by Kolesnikov et al. 2020, since we pre-train only for $7$ epochs, not $30$.

> **Table 7: Fine-tuning ResNet models pre-trained with Adam and SGD.**

|  | ResNet50 |  | ResNet152x2 |  |
|---|---|---|---|---|
| Dataset | Adam | SGD | Adam | SGD |
| ImageNet | $77.54$ | $78.24$ | $84.97$ | $84.37$ |
| CIFAR10 | $97.67$ | $97.46$ | $99.06$ | $99.07$ |
| CIFAR100 | $86.07$ | $85.17$ | $92.05$ | $91.06$ |
| Oxford-IIIT Pets | $91.11$ | $91.00$ | $95.37$ | $94.79$ |
| Oxford Flowers-102 | $94.26$ | $92.06$ | $98.62$ | $99.32$ |
| Average | $89.33$ | $88.79$ | $94.01$ | $93.72$ |

### D.2 Transformer shape

> **Figure 8: Scaling different model dimensions of the Vision Transformer.**

We ran ablations on scaling different dimensions of the Transformer architecture to find out which are best suited for scaling to very large models. Figure 8 shows 5-shot performance on ImageNet for different configurations. All configurations are based on a ViT model with $8$ layers, $D=1024$, $D_{MLP}=2048$ and a patch size of $32$, the intersection of all lines. We can see that scaling the depth results in the biggest improvements which are clearly visible up until 64 layers. However, diminishing returns are already visible after 16 layers. Interestingly, scaling the width of the network seems to result in the smallest changes. Decreasing the patch size and thus increasing the effective sequence length shows surprisingly robust improvements without introducing parameters. These findings suggest that compute might be a better predictor of performance than the number of parameters, and that scaling should emphasize depth over width if any. Overall, we find that scaling all dimensions proportionally results in robust improvements.

> **Figure 9: Comparison of class-token and global average pooling classifiers. Both work similarly well, but require different learning-rates.**

### D.3 Head Type and `class` token

In order to stay as close as possible to the original Transformer model, we made use of an additional `[class]` token, which is taken as image representation. The output of this token is then transformed into a class prediction via a small multi-layer perceptron (MLP) with $\tanh$ as non-linearity in the single hidden layer.

This design is inherited from the Transformer model for text, and we use it throughout the main paper.
An initial attempt at using only image-patch embeddings, globally average-pooling (GAP) them, followed by a linear classifier—just like ResNet’s final feature map—performed very poorly.
However, we found that this is neither due to the extra token, nor to the GAP operation. Instead, the difference in performance is fully explained by the requirement for a different learning-rate, see Figure 9.

### D.4 Positional Embedding

We ran ablations on different ways of encoding spatial information using positional embedding. We tried the following cases:

- Providing no positional information: Considering the inputs as a *bag of patches*.
- 1-dimensional positional embedding: Considering the inputs as a sequence of patches in the raster order (default across all other experiments in this paper).
- 2-dimensional positional embedding: Considering the inputs as a grid of patches in two dimensions. In this case, two sets of embeddings are learned, each for one of the axes, $X$-embedding, and $Y$-embedding, each with size $D/2$. Then, based on the coordinate on the path in the input, we concatenate the $X$ and $Y$ embedding to get the final positional embedding for that patch.
- Relative positional embeddings: Considering the relative distance between patches to encode the spatial information as instead of their absolute position. To do so, we use 1-dimensional Relative Attention, in which we define the relative distance all possible pairs of patches. Thus, for every given pair (one as query, and the other as key/value in the attention mechanism), we have an offset $p_{q}-p_{k}$, where each offset is associated with an embedding. Then, we simply run extra attention, where we use the original query (the content of query), but use relative positional embeddings as keys. We then use the logits from the relative attention as a bias term and add it to the logits of the main attention (content-based attention) before applying the softmax.

> **Table 8: Results of the ablation study on positional embeddings with ViT-B/16 model evaluated on ImageNet 5-shot linear.**

| Pos. Emb. | Default/Stem | Every Layer | Every Layer-Shared |
|---|---|---|---|
| No Pos. Emb. | 0.61382 | N/A | N/A |
| 1-D Pos. Emb. | 0.64206 | 0.63964 | 0.64292 |
| 2-D Pos. Emb. | 0.64001 | 0.64046 | 0.64022 |
| Rel. Pos. Emb. | 0.64032 | N/A | N/A |

> **Figure 10: Position embeddings of models trained with different hyperparameters.**
> (image not fetched: /html/2010.11929/assets/20200930_position_embeddings_16490619_1.png, /html/2010.11929/assets/20200930_position_embeddings_17192124_1.png, /html/2010.11929/assets/20200930_position_embeddings_17192217_1.png)

In addition to different ways of encoding spatial information, we also tried different ways of incorporating this information in our model. For the 1-dimensional and 2-dimensional positional embeddings, we tried three different cases: (1) add positional embeddings to the inputs right after the stem of them model and before feeding the inputs to the Transformer encoder (default across all other experiments in this paper); (2) learn and add positional embeddings to the inputs at the beginning of each layer; (3) add a learned positional embeddings to the inputs at the beginning of each layer (shared between layers).

Table 8 summarizes the results from this ablation study on a ViT-B/16 model. As we can see, while there is a large gap between the performances of the model with no positional embedding and models with positional embedding, there is little to no difference between different ways of encoding positional information. We speculate that since our Transformer encoder operates on patch-level inputs, as opposed to pixel-level, the differences in how to encode spatial information is less important. More precisely, in patch-level inputs, the spatial dimensions are much smaller than the original pixel-level inputs, e.g., $14\times 14$ as opposed to $224\times 224$, and learning to represent the spatial relations in this resolution is equally easy for these different positional encoding strategies.
Even so, the specific pattern of position embedding similarity learned by the network depends on the training hyperparameters (Figure 10).

> **Figure 11: Size of attended area by head and network depth. Attention distance was computed for 128 example images by averaging the distance between the query pixel and all other pixels, weighted by the attention weight. Each dot shows the mean attention distance across images for one of 16 heads at one layer. Image width is 224 pixels.**

### D.5 Empirical Computational Costs

We are also interested in real-world speed of the architectures on our hardware, which is not always well predicted by theoretical FLOPs due to details like lane widths and cache sizes.
For this purpose, we perform timing of inference speed for the main models of interest, on a TPUv3 accelerator; the difference between inference and backprop speed is a constant model-independent factor.

Figure 12 (left) shows how many images one core can handle per second, across various input sizes.
Every single point refers to the peak performance measured across a wide range of batch-sizes.
As can be seen, the theoretical bi-quadratic scaling of ViT with image size only barely starts happening for the largest models at the largest resolutions.

Another quantity of interest is the largest batch-size each model can fit onto a core, larger being better for scaling to large datasets.
Figure 12 (right) shows this quantity for the same set of models.
This shows that large ViT models have a clear advantage in terms of memory-efficiency over ResNet models.

> **Figure 12: **Left:** Real wall-clock timings of various architectures across input sizes. ViT models have speed comparable to similar ResNets. **Right**: Largest per-core batch-size fitting on device with various architectures across input sizes. ViT models are clearly more memory-efficient.**

### D.6 Axial Attention

Axial Attention (Huang et al. 2020; Ho et al. 2019) is a simple, yet effective technique to run self-attention on large inputs that are organized as multidimensional tensors. The general idea of axial attention is to perform multiple attention operations, each along a single axis of the input tensor, instead of applying 1-dimensional attention to the flattened version of the input. In axial attention, each attention mixes information along a particular axis, while keeping information along the other axes independent.
Along this line, Wang et al. 2020b proposed the AxialResNet model in which all the convolutions with kernel size $3\times 3$ in a ResNet50 are replaced by axial self-attention, i.e. a row and column attention, augmented by relative positional encoding.
We have implemented AxialResNet as a baseline model. [footnote: ^3^

Our implementation is based on the open-sourced PyTorch implementation in https://github.com/csrhddlam/axial-deeplab. In our experiments, we reproduced the scores reported in (Wang et al. 2020b) in terms of accuracy, however, our implementation, similar to the open-source implementation, is very slow on TPUs.
Therefore, we were not able to use it for extensive large-scale experiments.
These may be unlocked by a carefully optimized implementation.] .

Moreover, we have modified ViT to process inputs in the 2-dimensional shape, instead of a 1-dimensional sequence of patches, and incorporate Axial Transformer blocks, in which instead of a self-attention followed by an MLP, we have a a row-self-attention plus an MLP followed by a column-self-attention plus an MLP.

> **Figure 13: Performance of Axial-Attention based models, in terms of top-1 accuracy on ImageNet 5-shot linear, versus their speed in terms of number of FLOPs (**left**) and inference time (**left**).**

Figure 13, present the performance of Axial ResNet, Axial-ViT-B/32 and Axial-ViT-B/16 on ImageNet 5shot linear, when pretrained on JFT dataset, verses the pretraining compute, both in terms of number of FLOPs and inference time (example per seconds). As we can see, both
Axial-ViT-B/32 and Axial-ViT-B/16 do better than their ViT-B counterpart in terms of performance, but it comes at the cost of more compute. This is because in Axial-ViT models, each Transformer block with global self-attention is replaced by two Axial Transformer blocks, one with row and one with column self-attention and although the sequence length that self-attention operates on is smaller in axial case, there is a extra MLP per Axial-ViT block.
For the AxialResNet, although it looks reasonable in terms of accuracy/compute trade-off (Figure 13, left), the naive implementation is extremely slow on TPUs (Figure 13, right).

### D.7 Attention Distance

To understand how ViT uses self-attention to integrate information across the image, we analyzed the average distance spanned by attention weights at different layers (Figure 11). This “attention distance” is analogous to receptive field size in CNNs. Average attention distance is highly variable across heads in lower layers, with some heads attending to much of the image, while others attend to small regions at or near the query location. As depth increases, attention distance increases for all heads. In the second half of the network, most heads attend widely across tokens.

### D.8 Attention Maps

To compute maps of the attention from the output token to the input space (Figures 6 and 14), we used Attention Rollout (Abnar & Zuidema 2020). Briefly, we averaged attention weights of ViT-L/16 across all heads and then recursively multiplied the weight matrices of all layers. This accounts for the mixing of attention across tokens through all layers.

> **Figure 14: Further example attention maps as in Figure 6 (random selection).**
> (image not fetched: /html/2010.11929/assets/20201002_batch_attention_examples_compressed.png)

### D.9 ObjectNet Results

We also evaluate our flagship ViT-H/14 model on the ObjectNet benchmark following the evaluation setup in Kolesnikov et al. 2020, resulting in 82.1% top-5 accuracy and 61.7% top-1 accuracy.

### D.10 VTAB Breakdown

Table 9 shows the scores attained on each of the VTAB-1k tasks.

> **Table 9: Breakdown of VTAB-1k performance across tasks.**

|  | Caltech101 | CIFAR-100 | DTD | Flowers102 | Pets | Sun397 | SVHN | Camelyon | EuroSAT | Resisc45 | Retinopathy | Clevr-Count | Clevr-Dist | DMLab | dSpr-Loc | dSpr-Ori | KITTI-Dist | sNORB-Azim | sNORB-Elev | Mean |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ViT-H/14 (JFT) | 95.3 | 85.5 | 75.2 | 99.7 | 97.2 | 65.0 | 88.9 | 83.3 | 96.7 | 91.4 | 76.6 | 91.7 | 63.8 | 53.1 | 79.4 | 63.3 | 84.5 | 33.2 | 51.2 | 77.6 |
| ViT-L/16 (JFT) | 95.4 | 81.9 | 74.3 | 99.7 | 96.7 | 63.5 | 87.4 | 83.6 | 96.5 | 89.7 | 77.1 | 86.4 | 63.1 | 49.7 | 74.5 | 60.5 | 82.2 | 36.2 | 51.1 | 76.3 |
| ViT-L/16 (I21k) | 90.8 | 84.1 | 74.1 | 99.3 | 92.7 | 61.0 | 80.9 | 82.5 | 95.6 | 85.2 | 75.3 | 70.3 | 56.1 | 41.9 | 74.7 | 64.9 | 79.9 | 30.5 | 41.7 | 72.7 |
