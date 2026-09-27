---
source_file: gemma-qlora-hf-guide/
source_type: web-capture
ingested_at: 2026-09-26
---

# Fine-Tune Gemma using Hugging Face Transformers and QLoRA (Google AI for Developers)

## Provenance
- Original location: research/web/gemma-qlora-hf-guide/ (page.md was used; I removed the site navigation, and the body starts at the H1 on line 40)
- Format: html (web capture via talksmith:ingest). The page is a rendered Jupyter notebook from the `google-gemma/cookbook` repo (`docs/core/huggingface_text_finetune_qlora.ipynb`), with Colab, Kaggle and Vertex AI launch buttons.
- URL: https://ai.google.dev/gemma/docs/core/huggingface_text_finetune_qlora
- Fetched at: 2026-09-26T22:38:33Z (HTTP 200, 210,493 bytes)
- Author / source (if known): Google (Gemma team), official vendor tutorial on ai.google.dev. **This is vendor/tool documentation captured 2026-09-26. Library versions and model IDs change fast, so re-check them before you quote this as current.**
- Date of original (if known): the footer says "Last updated 2026-06-19 UTC."

## Key claims
- **What QLoRA is (verbatim):** "In QloRA, the pretrained model is quantized to 4-bit and the weights are frozen. Then trainable adapter layers (LoRA) are attached and only the adapter layers are trained. Afterwards, the adapter weights can be merged with the base model or kept as a separate adapter." The page cites arXiv 2305.14314.
- **Task:** fine-tune Gemma as a natural-language→SQL translator, using `philschmid/gretel-synthetic-text-to-sql`. Stack: Hugging Face Transformers + TRL `SFTTrainer` + PEFT + bitsandbytes.
- **Concrete steps, in order:**
  1. **Install:** `torch tensorboard`, `torchao`, `"transformers>=5.10.1"`, `datasets accelerate evaluate bitsandbytes trl "peft>=0.19.0" protobuf sentencepiece`. `flash-attn` is optional, "if you are running on a GPU that supports BF16 data type and flash attn, such as NVIDIA L4 or NVIDIA A100".
  2. **Log in to the Hugging Face Hub** with a token that has write access, because the model is pushed during training.
  3. **Prepare the dataset** in conversational "OAI messages" format (`{"messages": [system, user, assistant]}`). The user prompt wraps `<SCHEMA>` and `<USER_QUERY>`, and the assistant turn is the SQL. The code selects 1,250 samples and splits them 80/20 train/test.
  4. **Load Gemma 4 in 4-bit:** `model_id = "google/gemma-4-E2B"`, with a picker listing `google/gemma-4-E2B`, `google/gemma-4-E4B`, `google/gemma-4-12B`, `google/gemma-4-31B`, `google/gemma-4-26B-A4B`. `BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_use_double_quant=True, bnb_4bit_quant_type='nf4', …)`. The model is loaded with `AutoModelForMultimodalLM`, and the processor with `AutoProcessor.from_pretrained("google/gemma-4-E2B-it")` ("Load the Instruction Processor to use the official Gemma template"). `prepare_model_for_kbit_training()` runs only if the GPU has more than 16 GB ("On T4, we are skipping this step purely due to VRAM limitation").
  5. **LoRA config:** `LoraConfig(lora_alpha=16, lora_dropout=0.05, r=16, bias="none", task_type="CAUSAL_LM", modules_to_save=["lm_head", "embed_tokens"], ensure_weight_tying=True)`. There are no `target_modules`; the comment says "PEFT's Gemma 4 defaults scope to the LM layers".
  6. **SFTConfig:** `max_length=512`, `num_train_epochs=3`, `per_device_train_batch_size=1`, `optim="adamw_torch_fused"`, `learning_rate=2e-4`, `lr_scheduler_type="constant"`, fp16/bf16 by GPU support, `push_to_hub=True`, `report_to="tensorboard"`, `dataset_kwargs={"skip_prepare_dataset": True}`, `remove_unused_columns=False`.
  7. **Custom data collator:** applies the chat template, then **masks every token up to and including the model-turn header `<|turn>model\n` with `-100`**, so the loss is computed only on the assistant (SQL) answer. It also masks padding.
  8. **Train:** `SFTTrainer(model, args, train_dataset, eval_dataset, peft_config, processing_class=processor, data_collator=collate_fn)`, then `trainer.train()` and `trainer.save_model()`.
  9. **Merge:** "When using QLoRA, you only train adapters and not the full model." To serve with vLLM or TGI, merge with `PeftModel.from_pretrained(...).merge_and_unload()` and `save_pretrained("merged_model", safe_serialization=True, max_shard_size="2GB")`.
  10. **Test inference:** `pipeline("text-generation")` on a test sample, with `eos_token_id = <turn|>` and `max_new_tokens = 256`.
- **What SFTTrainer adds on top of `Trainer`** (per the page): dataset formatting, training on completions only, packing, PEFT support including QLoRA, and preparing the model and tokenizer for conversational fine-tuning.
- **FlashAttention note:** "reduces memory usage from quadratic to linear in sequence length, leading to acelerating training up to 3x". It works on Ampere (L4) or newer.

## Definitions and terminology
- **QLoRA:** see Key claims. "a popular method to efficiently fine-tune LLMs as it reduces computational resource requirements while maintaining high performance."
- **NF4 / double quantization:** used through `bnb_4bit_quant_type='nf4'` and `bnb_4bit_use_double_quant=True` (not defined on the page).
- **Merge (`merge_and_unload`):** folds the adapter weights into the base weights so you can save "a default model".
- **Gemma 4 chat-template tokens** (from the output): `<bos><|turn>system … <turn|>`, `<|turn>user … <turn|>`, `<|turn>model`.
- **Ways to build a dataset:** existing open-source data (Spider), synthetic data from LLMs (Alpaca), human-written data (Dolly), or a mix of these (Orca).

## Evidence and examples
- Training sample (verbatim assistant target): `SELECT salesperson_id, name, SUM(volume) as total_volume FROM timber_sales JOIN salesperson ON timber_sales.salesperson_id = salesperson.salesperson_id GROUP BY salesperson_id, name ORDER BY total_volume DESC;`
- Test result (verbatim):
  - Query: "How many auto shows were held in the United States in the year 2019?"
  - Original: `SELECT COUNT(*) FROM Auto_Shows WHERE show_year = 2019 AND location = 'United States';`
  - Generated: `SELECT COUNT(*) FROM Auto_Shows WHERE location = 'United States' AND show_year = 2019;`, which is semantically equivalent with the conditions reordered.
- Upload log shows `adapter_model.safetensors … / 1.62GB`. The adapter is large because `modules_to_save` includes `lm_head` and `embed_tokens`.
- A TRL warning in the output reads: "The default `loss_type` will change from `'nll'` to `'chunked_nll'` in TRL 1.7."

## Inconsistencies / open questions
- [verified] The prose and the code disagree on dataset size. The prose says the 100k+ dataset "is downsampled to only use 10,000 samples", but the code runs `dataset.select(range(1250))`, which is 1,250 samples, split into 1,000 train and 250 test. I checked both passages in the same capture.
- [verified] Comments in the collator are copy-paste leftovers from another notebook: "Tokenize the texts and process the audios", "we mask the padding tokens and audio tokens", and "Mask everything from index 0 up to the start of the actual Japanese text response". This task is English→SQL text only. I checked them in the code block.
- [verified] The page's claim that SFTTrainer offers "Training on completions only" is consistent with TRL's docs. However, this tutorial does **not** use TRL's `assistant_only_loss`/`completion_only_loss`. It sets `skip_prepare_dataset=True` and masks by hand in a custom collator. I cross-checked this against `hf-trl-sft-trainer.web.md`.
- [open question] The model picker lists `google/gemma-4-12B`, but Vertex's open-model tuning list (`vertex-open-model-tuning.web.md`) has Gemma 4 E2B IT, E4B IT, 26B A4B IT and 31B IT, with no 12B. Either the checkpoint exists on Hugging Face and Vertex simply doesn't offer it, or the picker has a stale entry. Checking the Hugging Face model hub would settle it.
- [open question] The tutorial loads the **base** `google/gemma-4-E2B` weights with the **instruction-tuned** processor/template (`gemma-4-E2B-it`). The page presents this as intentional ("to use the official Gemma template"). It matters if the presenter wants to explain base vs instruct.
- [open question] This content is version-sensitive: `transformers>=5.10.1`, `peft>=0.19.0`, `AutoModelForMultimodalLM`, Gemma 4 model IDs, and the TRL loss-type change at 1.7. It reflects "Last updated 2026-06-19".
- [open question] No explicit VRAM figure is given beyond the T4/16 GB branch and the L4/A100 mention. Minimum hardware for each Gemma 4 size is not stated.
- [open question] AWS Bedrock fine-tuning support could not be captured (JS-rendered docs), so nothing in this batch sources a claim about Bedrock.

## Images / diagrams
- `gemma-qlora-hf-guide.web/images/kaggle-logo-transparent-300.png` (1056×480)
  - Provenance: the "Run in Kaggle" button logo in the notebook launch bar. I kept it because it is 300 px or more on both sides, but it is decorative.
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `gemma-qlora-hf-guide.web/images/lockup-new.svg` (viewBox 461.7×64)
  - Provenance: the "Google AI for Developers" site logo in the header. I kept it because it is 300 px or more wide, but it is decorative.
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- Dropped per instruction (both dimensions under 300 px): `notebook-site-button.png` (32×32), `colab_logo_32px.png` (32×32), `cloud-icon.svg` (32×32), `GitHub-Mark-32px.png` (32×32).

## Raw / preserved excerpts

> This guide walks you through how to fine-tune Gemma on a custom text-to-sql dataset using Hugging Face Transformers and TRL. You will learn:
>
> - What is Quantized Low-Rank Adaptation (QLoRA)
> - Setup development environment
> - Create and prepare the fine-tuning dataset
> - Fine-tune Gemma using TRL and the SFTTrainer
> - Test Model Inference and generate SQL queries
>
> ## What is Quantized Low-Rank Adaptation (QLoRA)
>
> This guide demonstrates the use of Quantized Low-Rank Adaptation (QLoRA), which emerged as a popular method to efficiently fine-tune LLMs as it reduces computational resource requirements while maintaining high performance. In QloRA, the pretrained model is quantized to 4-bit and the weights are frozen. Then trainable adapter layers (LoRA) are attached and only the adapter layers are trained. Afterwards, the adapter weights can be merged with the base model or kept as a separate adapter.

> ## Setup development environment
>
> The first step is to install Hugging Face Libraries, including TRL, and datasets to fine-tune open model, including different RLHF and alignment techniques.
>
> ```
> # Install Pytorch & other libraries
> %pip install torch tensorboard
> %pip install -U torchao
>
> # Install Transformers
> %pip install "transformers>=5.10.1"
>
> # Install Hugging Face libraries
> %pip install datasets accelerate evaluate bitsandbytes trl "peft>=0.19.0" protobuf sentencepiece
>
> # COMMENT IN: if you are running on a GPU that supports BF16 data type and flash attn, such as NVIDIA L4 or NVIDIA A100
> #%pip install flash-attn
> ```
>
> *Note: If you are using a GPU with Ampere architecture (such as NVIDIA L4) or newer, you can use Flash attention. Flash Attention is a method that significantly speeds computations up and reduces memory usage from quadratic to linear in sequence length, leading to acelerating training up to 3x.*
>
> You need a valid Hugging Face Token to publish your model. … Make sure your token has write access too, as you push your model to the Hub during training.

> ## Create and prepare the fine-tuning dataset
>
> When fine-tuning LLMs, it is important to know your use case and the task you want to solve. This helps you create a dataset to fine-tune your model. If you haven't defined your use case yet, you might want to go back to the drawing board.
>
> As an example, this guide focuses on the following use case:
>
> - Fine-tune a natural language to SQL model for seamless integration into a data analysis tool. The objective is to significantly reduce the time and expertise required for SQL query generation, enabling even non-technical users to extract meaningful insights from data.
>
> Text-to-SQL can be a good use case for fine-tuning LLMs, as it is a complex task that requires a lot of (internal) knowledge about the data and the SQL language.
>
> Once you have determined that fine-tuning is the right solution, you need a dataset to fine-tune. The dataset should be a diverse set of demonstrations of the task(s) you want to solve. There are several ways to create such a dataset, including:
>
> - Using existing open-source datasets, such as Spider
> - Using synthetic datasets created by LLMs, such as Alpaca
> - Using datasets created by humans, such as Dolly.
> - Using a combination of the methods, such as Orca
>
> Each of the methods has its own advantages and disadvantages and depends on the budget, time, and quality requirements. For example, using an existing dataset is the easiest but might not be tailored to your specific use case, while using domain experts might be the most accurate but can be time-consuming and expensive.
>
> This guide uses an already existing dataset (philschmid/gretel-synthetic-text-to-sql), a high quality synthetic Text-to-SQL dataset including natural language instructions, schema definitions, reasoning and the corresponding SQL query.
>
> Hugging Face TRL supports automatic templating of conversation dataset formats. This means you only need to convert your dataset into the right json objects, and `trl` takes care of templating and putting it into the right format.
>
> ```
> {"messages": [{"role": "system", "content": "You are..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
> ```
>
> The philschmid/gretel-synthetic-text-to-sql contains over 100k samples. To keep the guide small, it is downsampled to only use 10,000 samples.
>
> ```
> system_message = """You are a text to SQL query translator. Users will ask you questions in English and you will generate a SQL query based on the provided SCHEMA."""
>
> user_prompt = """Given the <USER_QUERY> and the <SCHEMA>, generate the corresponding SQL command to retrieve the desired data, considering the query's syntax, semantics, and schema constraints.
>
> <SCHEMA>
> {context}
> </SCHEMA>
>
> <USER_QUERY>
> {question}
> </USER_QUERY>
> """
> def create_conversation(sample, idx):
>   return {
>     "messages": [
>       {"role": "system", "content": system_message},
>       {"role": "user", "content": user_prompt.format(question=sample["sql_prompt"], context=sample["sql_context"])},
>       {"role": "assistant", "content": sample["sql"]}
>     ]
>   }
>
> dataset = load_dataset("philschmid/gretel-synthetic-text-to-sql", split="train")
> dataset = dataset.select(range(1250))
> dataset = dataset.map(create_conversation, with_indices=True, remove_columns=dataset.features)
> # split dataset into 80% training samples and 20% test samples
> dataset = dataset.train_test_split(test_size=0.2, shuffle=False)
> ```

> ## Fine-tune Gemma using TRL and the SFTTrainer
>
> You are now ready to fine-tune your model. Hugging Face TRL SFTTrainer makes it straightforward to supervise fine-tune open LLMs. The `SFTTrainer` is a subclass of the `Trainer` from the `transformers` library and supports all the same features, including logging, evaluation, and checkpointing, but adds additional quality of life features, including:
>
> - Dataset formatting, including conversational and instruction formats
> - Training on completions only, ignoring prompts
> - Packing datasets for more efficient training
> - Parameter-efficient fine-tuning (PEFT) support including QloRA
> - Preparing the model and tokenizer for conversational fine-tuning (such as adding special tokens)
>
> ```
> model_id = "google/gemma-4-E2B" # @param ["google/gemma-4-E2B","google/gemma-4-E4B","google/gemma-4-12B","google/gemma-4-31B","google/gemma-4-26B-A4B"] {"allow-input":true}
>
> if torch.cuda.is_bf16_supported():
>     torch_dtype = torch.bfloat16
> else:
>     torch_dtype = torch.float16
>
> model_kwargs = dict(
>     dtype=torch_dtype, # What torch dtype to use
>     device_map="auto", # Let torch decide how to load the model
> )
>
> # BitsAndBytesConfig: Enables 4-bit quantization to reduce model size/memory usage
> model_kwargs["quantization_config"] = BitsAndBytesConfig(
>     load_in_4bit=True,
>     bnb_4bit_use_double_quant=True,
>     bnb_4bit_quant_type='nf4',
>     bnb_4bit_compute_dtype=torch_dtype,
>     bnb_4bit_quant_storage=torch_dtype,
> )
>
> model = AutoModelForMultimodalLM.from_pretrained(model_id, **model_kwargs)
> processor = AutoProcessor.from_pretrained("google/gemma-4-E2B-it") # Load the Instruction Processor to use the official Gemma template
>
> # NOTE: You should call the prepare_model_for_kbit_training() function to preprocess the quantized model for training.
> # On T4, we are skipping this step purely due to VRAM limitation and for a quick demonstration.
> if (torch.cuda.get_device_properties(0).total_memory/1024**3) > 16:
>     model = prepare_model_for_kbit_training(model)
> ```
>
> The `SFTTrainer` supports a built-in integration with `peft`, which makes it straightforward to efficiently tune LLMs using QLoRA. You only need to create a `LoraConfig` and provide it to the trainer.
>
> ```
> peft_config = LoraConfig(
>     lora_alpha=16,
>     lora_dropout=0.05,
>     r=16,
>     bias="none",
>     # no target_modules — PEFT's Gemma 4 defaults scope to the LM layers
>     task_type="CAUSAL_LM",
>     modules_to_save=["lm_head", "embed_tokens"], # make sure to save the lm_head and embed_tokens as you train the special tokens
>     ensure_weight_tying=True,
> )
> ```
>
> ```
> args = SFTConfig(
>     output_dir="gemma-text-to-sql",         # directory to save and repository id
>     max_length=512,                         # max length for model and packing of the dataset
>     num_train_epochs=3,                     # number of training epochs
>     per_device_train_batch_size=1,          # batch size per device during training
>     per_device_eval_batch_size=1,           # batch size per device during evaluation
>     optim="adamw_torch_fused",              # use fused adamw optimizer
>     logging_steps=10,                       # log every 10 steps
>     save_strategy="epoch",                  # save checkpoint every epoch
>     eval_strategy="epoch",                  # evaluate checkpoint every epoch
>     learning_rate=2e-4,                     # learning rate
>     fp16=True if torch_dtype == torch.float16 else False,  # use float16 precision
>     bf16=True if torch_dtype == torch.bfloat16 else False, # use bfloat16 precision
>     lr_scheduler_type="constant",           # use constant learning rate scheduler
>     push_to_hub=True,                       # push model to hub
>     report_to="tensorboard",                # report metrics to tensorboard
>     dataset_kwargs={"skip_prepare_dataset": True}, # important for collator
>     remove_unused_columns = False,                 # important for collator
> )
> ```
>
> Data collator (key lines):
>
> ```
>     target_tokens = [
>         processor.tokenizer.convert_tokens_to_ids("<|turn>"),
>         processor.tokenizer.convert_tokens_to_ids("model"),
>         processor.tokenizer.convert_tokens_to_ids("\n")
>     ]
>     ...
>                 # We want to keep loss calculation on the assistant transcription tokens,
>                 # so we move the index right past the assistant header ('<|turn>\nmodel\n')
>                 assistant_start_idx = idx + target_len
>     ...
>         if assistant_start_idx is not None:
>             # Mask everything from index 0 up to the start of the actual Japanese text response
>             labels[i, :assistant_start_idx] = -100
>     ...
>     # Mask tokens for not being used in the loss computation
>     labels[labels == processor.tokenizer.pad_token_id] = -100
> ```
>
> ```
> trainer = SFTTrainer(
>     model=model,
>     args=args,
>     train_dataset=dataset["train"],
>     eval_dataset=dataset["test"],
>     peft_config=peft_config,
>     processing_class=processor,
>     data_collator=collate_fn,
> )
> # Start training, the model will be automatically saved to the Hub and the output directory
> trainer.train()
> # Save the final model again to the Hugging Face Hub
> trainer.save_model()
> ```

> When using QLoRA, you only train adapters and not the full model. This means when saving the model during training you only save the adapter weights and not the full model. If you want to save the full model, which makes it easier to use with serving stacks like vLLM or TGI, you can merge the adapter weights into the model weights using the `merge_and_unload` method and then save the model with the `save_pretrained` method. This saves a default model, which can be used for inference.
>
> ```
> model = AutoModelForMultimodalLM.from_pretrained(model_id, low_cpu_mem_usage=True)
> peft_model = PeftModel.from_pretrained(model, args.output_dir)
> merged_model = peft_model.merge_and_unload()
> merged_model.save_pretrained("merged_model", safe_serialization=True, max_shard_size="2GB")
> processor = AutoProcessor.from_pretrained("google/gemma-4-E2B-it")
> processor.save_pretrained("merged_model")
> ```

> ## Test Model Inference and generate SQL queries — sample output
>
> ```
> <bos><|turn>system
> You are a text to SQL query translator. Users will ask you questions in English and you will generate a SQL query based on the provided SCHEMA.<turn|>
> <|turn>user
> Given the <USER_QUERY> and the <SCHEMA>, … 
> <USER_QUERY>
> How many auto shows were held in the United States in the year 2019?
> </USER_QUERY><turn|>
> <|turn>model
>
> Original Answer:
> SELECT COUNT(*) FROM Auto_Shows WHERE show_year = 2019 AND location = 'United States';
> Generated Answer:
> SELECT COUNT(*) FROM Auto_Shows WHERE location = 'United States' AND show_year = 2019;
> ```

> ## Summary and next steps
>
> This tutorial covered how to fine-tune a Gemma model using TRL and QLoRA. Check out the following docs next: generate text with a Gemma model; fine-tune Gemma for vision tasks using Hugging Face Transformers; distributed fine-tuning and inference on a Gemma model; use Gemma open models with Vertex AI; fine-tune Gemma using KerasNLP and deploy to Vertex AI.
