---
source_file: hf-trl-sft-trainer/
source_type: web-capture
ingested_at: 2026-09-26
---

# SFT Trainer — TRL documentation (Hugging Face)

## Provenance
- Original location: research/web/hf-trl-sft-trainer/ (page.md used. The first ~22 lines are the site header and version picker, and the article body starts at "# SFT Trainer".)
- Format: html (web capture via talksmith:ingest)
- URL: https://huggingface.co/docs/trl/sft_trainer
- Fetched at: 2026-09-26T22:38:23Z (HTTP 200, 324,959 bytes)
- Author / source (if known): Hugging Face, TRL library documentation. Official open-source tool documentation. The page says "This post-training method was contributed by Younes Belkada." **Tool documentation captured 2026-09-26. APIs change between releases, so re-check against the installed version.**
- Date of original (if known): not stated. Version: the rendered docs link to **TRL v1.14.0** (newest in the version picker; source links point to `blob/v1.14.0`). They also cite transformers v5.17.0, PEFT v0.21.0, and datasets v5.0.1.

## Key claims
- "TRL supports the Supervised Fine-Tuning (SFT) Trainer for training language models."
- **Minimal local SFT** (verbatim quick start): `SFTTrainer(model="Qwen/Qwen3-0.6B", train_dataset=load_dataset("trl-lib/Capybara", split="train"))` followed by `trainer.train()`.
- **Dataset formats.** "SFT supports both language modeling and prompt-completion datasets. The SFTTrainer is compatible with both standard and conversational dataset formats. When provided with a conversational dataset, the trainer will automatically apply the chat template to the dataset." There are four shapes: standard LM `{"text": …}`, conversational LM `{"messages": […]}`, standard prompt-completion `{"prompt": …, "completion": …}`, and conversational prompt-completion (prompt and completion as message lists). Pre-tokenized datasets (`input_ids`, with optional `labels`, `assistant_masks`, or `completion_mask`) are also accepted.
- **Objective.** "The goal is to minimize the negative log-likelihood (NLL) of the target sequence, conditioning on the input." The loss is "token-level cross-entropy loss", L_SFT(θ) = −Σ_{t=1..T} log p_θ(y_t | y_<t). Padding is masked with ignore index `-100`, and labels use a one-token shift.
- **Default loss is `chunked_nll`**: "same math as `nll`", but the `lm_head` skips ignored-label tokens and cross-entropy runs in chunks to cut peak memory. The alternatives are `nll` and `dft` (Dynamic Fine-Tuning, arXiv 2508.05629).
- **Completion-only loss (default for prompt-completion data).** "By default, the trainer computes the loss on the completion tokens only, ignoring the prompt tokens. If you want to train on the full sequence, set `completion_only_loss=False`." With `None`, the behaviour depends on the dataset: completion-only for prompt-completion data, full sequence for language-modeling data.
- **Assistant-only loss (opt-in).** Set `assistant_only_loss=True` with a conversational dataset. The loss is then computed "**only** on the assistant responses, ignoring user or system messages." This "requires the chat template to include `{% generation %}` and `{% endgeneration %}` keywords". For known families such as Qwen3, TRL patches the template automatically. It is compatible with completion-only loss when the dataset is conversational prompt-completion.
- **PEFT / LoRA integration.** "We support tight integration with 🤗 PEFT library, allowing any user to conveniently train adapters and share them on the Hub, rather than training the entire model." Pass `peft_config=LoraConfig()`. You can continue training an existing `PeftModel`. "When training adapters, you typically use a higher learning rate (≈1e‑4) since only new parameters are being learned."
- **QLoRA.** The `quantization_config` (BitsAndBytesConfig) parameter is "Quantization configuration used when loading the model from a model identifier. Combine with `peft_config` for QLoRA training."
- **Packing.** Set `packing=True`, which packs multiple examples into one sequence (strategies `bfd` (default), `bfd_split`, `wrapped`).
- **Instruction tuning** of a base model: pass a chat template (`chat_template_path`), for example turning `Qwen/Qwen3-0.6B-Base` into an instruct model with the SmolLM3-3B template. Align `eos_token` with the template (for example `eos_token="<|im_end|>"` for `Qwen/Qwen2.5-1.5B`).
- **Tool calling.** SFTTrainer "fully supports fine-tuning models with tool calling capabilities". Examples include `tool_calls`, `tool` role messages, and a `tools` column of JSON schemas.
- **VLMs** are supported through an `image` or `images` column. Set `max_length=None` so image tokens are not truncated.
- **Integrations.** Liger Kernel ("boosts multi-GPU throughput by 20%, cuts memory use by 60% (enabling up to 4× longer context)"). RapidFire AI (many SFT configs at once, "even on a single GPU"). Unsloth ("up to 2× faster with up to 70% less VRAM"). These are the page's own figures.
- Diffusion models such as DiffusionGemma are not natively supported, but an example extension exists.

## Definitions and terminology
- **SFT.** "the simplest and most commonly used method to adapt a language model to a target dataset. The model is trained in a fully supervised fashion using pairs of input and output sequences."
- **Language modeling vs prompt-completion datasets.** Language-modeling data has a single `text` or `messages` field. Prompt-completion data has separate `prompt` and `completion` fields, which are "concatenated before tokenization".
- **Standard vs conversational.** Plain text versus role/content message lists.
- **Chat template.** "Defines how to structure conversations into text sequences, including role markers (user/assistant), special tokens, and turn boundaries."
- **Instruction tuning.** "teaches a base language model to follow user instructions and engage in conversations". It needs a chat template and a conversational dataset.
- **Packing.** "multiple examples are packed in the same input sequence to increase training efficiency."
- **Padding-free.** Flattens the batch into one sequence. Needs FlashAttention 2 or 3.
- **Logged metrics.** `global_step`, `epoch`, `num_tokens`, `loss`, `entropy`, `aux_loss` (MoE), `mean_token_accuracy`, `learning_rate`, `grad_norm`.

## Evidence and examples
- Preprocessing example that converts `FreedomIntelligence/medical-o1-reasoning-SFT` into conversational prompt-completion with `<think>{Complex_CoT}</think>{Response}` as the completion.
- Completion-only example with `trl-lib/kto-mix-14k` and `Qwen/Qwen2.5-0.5B-Instruct`, `SFTConfig(completion_only_loss=True)`.
- VLM example with `Qwen/Qwen2.5-VL-3B-Instruct` on `trl-lib/llava-instruct-mix`.
- **SFTConfig defaults** from the signature and notes: `per_device_train_batch_size=8`, `num_train_epochs=3.0`, `learning_rate=2e-05`, `lr_scheduler_type='linear'`, `optim='adamw_torch_fused'`, `max_length=1024`, `truncation_mode="keep_start"`, `packing=False`, `assistant_only_loss=False`, `loss_type="chunked_nll"`. They differ from TrainingArguments as follows: `logging_steps` 10 (not 500), `gradient_checkpointing` True, `bf16` True if fp16 is not set, and `learning_rate` 2e-5 (not 5e-5).
- If `dtype` is not given in `model_init_kwargs`, the model loads in `float32`.

## Inconsistencies / open questions
- [open question] This is a version-sensitive API. Parameter names and defaults (`completion_only_loss`, `assistant_only_loss`, `loss_type="chunked_nll"`, `max_length=1024`, `truncation_mode` "keep_end" deprecated for v2.0.0, `pad_token` deprecated) match TRL v1.14.0 as rendered on 2026-09-26. Older tutorials (for example the Gemma QLoRA guide in `gemma-qlora-hf-guide.web.md`) may use different names or defaults. Check against the installed `trl` version.
- [verified] The quick-start comment says `completion_only_loss=True` is "True by default for prompt-completion datasets", while the SFTConfig reference says the default is `None`, meaning dataset-dependent behaviour. Both describe the same effective behaviour for prompt-completion data. Checked the Customization section against the SFTConfig parameter docs on the same page.
- [open question] The Unsloth figures quoted here ("up to 2× faster with up to 70% less VRAM") are TRL's summary. The Unsloth guide (`unsloth-fine-tuning-guide.web.md`) may state different numbers. Treat them as vendor claims.
- [open question] AWS Bedrock fine-tuning support could not be captured (JS-rendered docs), so no claim about Bedrock is sourced in this batch.

## Images / diagrams
- `hf-trl-sft-trainer.web/images/sft_figure.png` (2256×1153)
  - Provenance: figure under "Computing the loss", alt "sft_figure". Saved from https://huggingface.co/datasets/trl-lib/documentation-images/resolve/main/sft_figure.png
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `hf-trl-sft-trainer.web/images/train_on_assistant.png` (1988×462)
  - Provenance: figure under "Train on assistant messages only", alt "train_on_assistant". Saved from https://huggingface.co/datasets/trl-lib/documentation-images/resolve/main/train_on_assistant.png
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `hf-trl-sft-trainer.web/images/train_on_completion.png` (1988×462)
  - Provenance: figure under "Train on completion only", alt "train_on_completion". Saved from https://huggingface.co/datasets/trl-lib/documentation-images/resolve/main/train_on_completion.png
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- Dropped per instruction (both dimensions < 300 px): `huggingface_logo-noborder.svg` (95×88), and the shields.io badges `All_models-SFT-blue` (98×20) and `smol_course-Chapter_1-yellow` (142×20).

## Raw / preserved excerpts

> ## Quick start
>
> This example demonstrates how to train a language model using the SFTTrainer from TRL. We train a Qwen 3 0.6B model on the Capybara dataset, a compact, diverse multi-turn dataset to benchmark reasoning and generalization.
>
> ```
> from trl import SFTTrainer
> from datasets import load_dataset
>
> trainer = SFTTrainer(
>     model="Qwen/Qwen3-0.6B",
>     train_dataset=load_dataset("trl-lib/Capybara", split="train"),
> )
> trainer.train()
> ```

> ## Expected dataset type and format
>
> SFT supports both language modeling and prompt-completion datasets. The SFTTrainer is compatible with both standard and conversational dataset formats. When provided with a conversational dataset, the trainer will automatically apply the chat template to the dataset.
>
> ```
> # Standard language modeling
> {"text": "The sky is blue."}
>
> # Conversational language modeling
> {"messages": [{"role": "user", "content": "What color is the sky?"},
>               {"role": "assistant", "content": "It is blue."}]}
>
> # Standard prompt-completion
> {"prompt": "The sky is",
>  "completion": " blue."}
>
> # Conversational prompt-completion
> {"prompt": [{"role": "user", "content": "What color is the sky?"}],
>  "completion": [{"role": "assistant", "content": "It is blue."}]}
> ```
>
> If your dataset is not in one of these formats, you can preprocess it to convert it into the expected format. Here is an example with the FreedomIntelligence/medical-o1-reasoning-SFT dataset:
>
> ```
> from datasets import load_dataset
>
> dataset = load_dataset("FreedomIntelligence/medical-o1-reasoning-SFT", "en")
>
> def preprocess_function(example):
>     return {
>         "prompt": [{"role": "user", "content": example["Question"]}],
>         "completion": [
>             {"role": "assistant", "content": f"<think>{example['Complex_CoT']}</think>{example['Response']}"}
>         ],
>     }
>
> dataset = dataset.map(preprocess_function, remove_columns=["Question", "Response", "Complex_CoT"])
> ```

> ## Looking deeper into the SFT method
>
> Supervised Fine-Tuning (SFT) is the simplest and most commonly used method to adapt a language model to a target dataset. The model is trained in a fully supervised fashion using pairs of input and output sequences. The goal is to minimize the negative log-likelihood (NLL) of the target sequence, conditioning on the input.
>
> ### Preprocessing and tokenization
>
> During training, each example is expected to contain a **text field** or a **(prompt, completion)** pair, depending on the dataset format. … The SFTTrainer tokenizes each input using the model's tokenizer. If both prompt and completion are provided separately, they are concatenated before tokenization.
>
> ### Computing the loss
>
> The loss used in SFT is the **token-level cross-entropy loss**, defined as: 𝓛_SFT(θ) = − Σ_{t=1}^{T} log p_θ(y_t ∣ y_{<t}), where y_t is the target token at timestep t, and the model is trained to predict the next token given the previous ones. In practice, padding tokens are masked out during loss computation.
>
> The paper On the Generalization of SFT: A Reinforcement Learning Perspective with Reward Rectification proposes an alternative loss function, called **Dynamic Fine-Tuning (DFT)**, which aims to improve generalization by rectifying the reward signal. This method can be enabled by setting `loss_type="dft"` in the SFTConfig.
>
> By default, SFTTrainer uses `loss_type="chunked_nll"`: same math as `"nll"`, but the `lm_head` projection skips ignored-label tokens and the cross-entropy is processed in chunks, so peak activation memory does not scale with the full vocab × seq_len logits tensor. To fall back to the standard path, set `loss_type="nll"`. When `use_liger_kernel=True`, the default automatically resolves to `"nll"` (the two paths are not compatible).
>
> ### Label shifting and masking
>
> During training, the loss is computed using a **one-token shift**: the model is trained to predict each token in the sequence based on all previous tokens. Specifically, the input sequence is shifted right by one position to form the target labels. Padding tokens (if present) are ignored in the loss computation by applying an ignore index (default: `-100`) to the corresponding positions. This ensures that the loss focuses only on meaningful, non-padding tokens.

> ### Train on assistant messages only
>
> To train on assistant messages only, use a conversational dataset and set `assistant_only_loss=True` in the SFTConfig. This setting ensures that loss is computed **only** on the assistant responses, ignoring user or system messages.
>
> ```
> training_args = SFTConfig(assistant_only_loss=True)
> ```
>
> This functionality requires the chat template to include `{% generation %}` and `{% endgeneration %}` keywords. For known model families (e.g. Qwen3), TRL automatically patches the template when `assistant_only_loss=True`. See Chat Templates for the full list of bundled training templates. For other models, check that your chat template includes these keywords.
>
> ### Train on completion only
>
> To train on completion only, use a prompt-completion dataset. By default, the trainer computes the loss on the completion tokens only, ignoring the prompt tokens. If you want to train on the full sequence, set `completion_only_loss=False` in the SFTConfig.
>
> ```
> from trl import SFTConfig, SFTTrainer
> from datasets import load_dataset
>
> # Load a prompt-completion dataset; loss is computed on the completion only by default
> dataset = load_dataset("trl-lib/kto-mix-14k", split="train")
>
> trainer = SFTTrainer(
>     model="Qwen/Qwen2.5-0.5B-Instruct",
>     args=SFTConfig(completion_only_loss=True),  # True by default for prompt-completion datasets
>     train_dataset=dataset,
> )
> trainer.train()
> ```
>
> Training on completion only is compatible with training on assistant messages only. In this case, use a conversational prompt-completion dataset and set `assistant_only_loss=True` in the SFTConfig.

> ### Train adapters with PEFT
>
> We support tight integration with 🤗 PEFT library, allowing any user to conveniently train adapters and share them on the Hub, rather than training the entire model.
>
> ```
> from datasets import load_dataset
> from trl import SFTTrainer
> from peft import LoraConfig
>
> dataset = load_dataset("trl-lib/Capybara", split="train")
>
> trainer = SFTTrainer(
>     "Qwen/Qwen3-0.6B",
>     train_dataset=dataset,
>     peft_config=LoraConfig(),
> )
>
> trainer.train()
> ```
>
> You can also continue training your PeftModel. For that, first load a `PeftModel` outside SFTTrainer and pass it directly to the trainer without the `peft_config` argument being passed.
>
> ```
> model = AutoPeftModelForCausalLM.from_pretrained("trl-lib/Qwen3-4B-LoRA", is_trainable=True)
> ```
>
> When training adapters, you typically use a higher learning rate (≈1e‑4) since only new parameters are being learned.

> ### Train with Liger Kernel
>
> Liger Kernel is a collection of Triton kernels for LLM training that boosts multi-GPU throughput by 20%, cuts memory use by 60% (enabling up to 4× longer context), and works seamlessly with tools like FlashAttention, PyTorch FSDP, and DeepSpeed.
>
> ### Rapid Experimentation for SFT
>
> RapidFire AI is an open-source experimentation engine that sits on top of TRL and lets you launch multiple SFT configurations at once, even on a single GPU. …
>
> ### Train with Unsloth
>
> Unsloth is an open‑source framework for fine‑tuning and reinforcement learning that trains LLMs (like Llama, Mistral, Gemma, DeepSeek, and more) up to 2× faster with up to 70% less VRAM, while providing a streamlined, Hugging Face–compatible workflow for training, evaluation, and deployment.

> ## Instruction tuning example
>
> **Instruction tuning** teaches a base language model to follow user instructions and engage in conversations. This requires:
>
> 1. **Chat template**: Defines how to structure conversations into text sequences, including role markers (user/assistant), special tokens, and turn boundaries.
> 2. **Conversational dataset**: Contains instruction-response pairs
>
> This example shows how to transform the Qwen 3 0.6B Base model into an instruction-following model using the Capybara dataset and a chat template from HuggingFaceTB/SmolLM3-3B. The SFT Trainer automatically handles tokenizer updates and special token configuration.
>
> ```
> trainer = SFTTrainer(
>     model="Qwen/Qwen3-0.6B-Base",
>     args=SFTConfig(
>         output_dir="Qwen3-0.6B-Instruct",
>         chat_template_path="HuggingFaceTB/SmolLM3-3B",
>     ),
>     train_dataset=load_dataset("trl-lib/Capybara", split="train"),
> )
> trainer.train()
> ```
>
> Some base models, like those from Qwen, have a predefined chat template in the model's tokenizer. In these cases, it is not necessary to apply `clone_chat_template()`, as the tokenizer already handles the formatting. However, it is necessary to align the EOS token with the chat template to ensure the model's responses terminate correctly. In these cases, specify `eos_token` in SFTConfig; for example, for `Qwen/Qwen2.5-1.5B`, one should set `eos_token="<|im_end|>"`.
>
> ```
> >>> prompt = [{"role": "user", "content": "What is the capital of France? Answer in one word."}]
> >>> response = pipe(prompt)
> >>> response[0]["generated_text"]
> [{'role': 'user', 'content': 'What is the capital of France? Answer in one word.'}, {'role': 'assistant', 'content': 'The capital of France is Paris.'}]
> ```

> ## Tool Calling with SFT
>
> The SFTTrainer fully supports fine-tuning models with *tool calling* capabilities. In this case, each dataset example should include:
>
> - The conversation messages, including any tool calls (`tool_calls`) and tool responses (`tool` role messages)
> - The list of available tools in the `tools` column, typically provided as JSON schemas

> ## Training Vision Language Models
>
> SFTTrainer fully supports training Vision-Language Models (VLMs). To train a VLM, provide a dataset with either an `image` column (single image per sample) or an `images` column (list of images per sample). … For VLMs, truncating may remove image tokens, leading to errors during training. To avoid this, set `max_length=None` in the SFTConfig.

> ### SFTTrainer parameters (selected, verbatim)
>
> - **quantization_config** (BitsAndBytesConfig, optional) — Quantization configuration used when loading the model from a model identifier. Combine with `peft_config` for QLoRA training. Ignored if the model is already instantiated.
> - **peft_config** (PeftConfig, optional) — PEFT configuration used to wrap the model. If `None`, the model is not wrapped.
> - **model** … A PreTrainedModel object. Only causal language models are supported. … If `dtype` is not specified in `args.model_init_kwargs`, it defaults to `float32`.
>
> ### SFTConfig parameters (selected, verbatim)
>
> - **max_length** (`int` or `None`, optional, defaults to `1024`) — Maximum length of the tokenized sequence. Sequences longer than `max_length` are truncated from the left or right depending on `truncation_mode`. If `None`, no truncation is applied. When packing is enabled, this value sets the sequence length.
> - **completion_only_loss** (`bool`, optional) — Whether to compute loss only on the completion part of the sequence. If set to `True`, loss is computed only on the completion, which is supported only for prompt-completion datasets. If `False`, loss is computed on the entire sequence. If `None` (default), the behavior depends on the dataset: loss is computed on the completion for prompt-completion datasets, and on the full sequence for language modeling datasets.
> - **assistant_only_loss** (`bool`, optional, defaults to `False`) — Whether to compute loss only on the assistant part of the sequence. If set to `True`, loss is computed only on the assistant responses, which is supported only for conversational datasets. If `False`, loss is computed on the entire sequence.
> - **packing** (`bool`, optional, defaults to `False`) — Whether to group multiple sequences into fixed-length blocks to improve computational efficiency and reduce padding. Uses `max_length` to define sequence length.
>
> These parameters have default values different from TrainingArguments: `logging_steps`: Defaults to `10` instead of `500`. `gradient_checkpointing`: Defaults to `True` instead of `False`. `bf16`: Defaults to `True` if `fp16` is not set, instead of `False`. `learning_rate`: Defaults to `2e-5` instead of `5e-5`.
