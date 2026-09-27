---
source_file: unsloth-fine-tuning-guide/
source_type: web-capture
ingested_at: 2026-09-26
---

# Fine-tuning LLMs Guide — Unsloth Documentation

## Provenance
- Original location: research/web/unsloth-fine-tuning-guide/ (page.md used and is complete. I cross-checked original.html for VRAM/GGUF/Ollama text: no body content beyond page.md, only sidebar navigation.)
- Format: html (GitBook site; web capture via talksmith:ingest)
- URL: https://unsloth.ai/docs/get-started/fine-tuning-llms-guide
- Fetched at: 2026-09-26T22:38:30Z (HTTP 200, 1,038,156 bytes)
- Author / source (if known): Unsloth (unslothai). This is vendor/tool documentation for an open-source fine-tuning framework, and it is promotional in places. **Tool documentation captured 2026-09-26. It changes fast, so re-check before quoting as current.**
- Date of original (if known): the page says "Last updated 6 months ago" (relative to capture, so roughly March 2026; no absolute date is given).
- Sidebar context (navigation only, not body): it lists model pages such as "Qwen3.8-27B", "Qwen3.6", "Kimi K3", "Qwen3.5", plus "Dynamic 3.0 GGUFs", "Unsloth Studio" and "Tutorial: Finetune Llama-3 and Use In Ollama".

## Key claims
- **Hardware / VRAM:** "With Unsloth, you can fine-tune or do RL for free on Colab, Kaggle, or locally with just 3GB VRAM by using our notebooks." Local install needs "a Windows or Linux device" (`pip install unsloth` on Linux, WSL or Windows, or Docker). "depending on the model you're using, you'll need enough VRAM and resources." A detailed VRAM table lives on the linked "Unsloth Requirements" page, which was **not captured**.
- **LoRA vs QLoRA:** "LoRA is when the original model is 16-bit unquantized while QLoRA quantizes to 4-bit to save 75% memory." LoRA "typically keeps the base model's weights frozen and trains a small set of added low-rank adapter weights (in 16-bit precision)". QLoRA "combines LoRA with 4-bit precision to handle very large models with minimal resources." LoRA trains thin matrices A and B: "we only optimize 1% of weights."
- **Recommendation:** "We recommend starting with QLoRA, as it is one of the most accessible and effective methods for training models. Our dynamic 4-bit quants, the accuracy loss for QLoRA compared to LoRA is now largely recovered."
- **Full fine-tuning (FFT)** is supported (`full_finetuning = True`), as are 8-bit (`load_in_8bit = True`) and 16-bit LoRA (`load_in_16bit = True`). But "FFT is usually unnecessary. When done correctly, LoRA can match FFT." Also: "Start by testing with LoRA or QLoRA first, if it won't work there, it almost certainly won't work with FFT."
- **Precision:** "Research shows that **training and serving in the same precision** helps preserve accuracy. This means if you want to serve in 4-bit, train in 4-bit and vice versa."
- **Beginner model:** "start with a small instruct model like Llama 3.1 (8B)". Start from **Instruct** models rather than Base models, because they use chat templates (ChatML, ShareGPT) and need less data.
- **Methods:** SFT is "the standard method of post training". The others are DPO, ORPO, distillation, and RL (GRPO, GSPO). The page also covers TTS, embedding, vision, multimodal, and continued pretraining. "for most use-cases, standard SFT is sufficient."
- **Dataset:** "usually with 2 columns - question and answer". You can generate data synthetically with ChatGPT or local LLMs. For code, "just dumping all your code data" can work. Most notebooks use the Alpaca dataset.
- **Default hyperparameters shown:** `max_seq_length = 2048`, `load_in_4bit = True`, `per_device_train_batch_size = 2`, `gradient_accumulation_steps = 4`, `max_steps = 60` (or `num_train_epochs = 1`; "1–3 epochs recommended"), `learning_rate = 2e-4`.
- **Loss guidance:** "a loss around 0.5 to 1.0 is a good sign… If the loss goes to 0, that could mean overfitting."
- **Export / local deployment:** "If you're running inference on a single device (like a laptop or Mac), use llama.cpp to convert to GGUF format to use in Ollama, llama.cpp, LM Studio etc." For enterprise or multi-user serving (FP8, AWQ), use vLLM. The LoRA adapter saves as "a small 100MB file", or you can push it to the Hugging Face Hub. The page says "2x faster inference natively" via `FastLanguageModel.for_inference(model)`.
- **Vendor opinion (strong claims):** "**Fine-tuning can replicate all of RAG's capabilities**, but not vice versa." The page also calls it "**false**" that fine-tuning can't add new knowledge.
- **Unsloth Studio:** "Our new open-source web UI for training and running models… fine-tune models with no-code".

## Definitions and terminology
- **Fine-tuning / post-training:** "customizes its behavior, enhances + injects knowledge, and optimizes performance for domains and specific tasks."
- **LoRA / QLoRA:** see Key claims. "Llama 70B has 70 billion numbers. Instead of changing all 70B numbers, we instead add thin matrices A and B to each weight, and optimize those."
- **FFT:** full fine-tuning.
- **Model-name suffixes:** `unsloth-bnb-4bit` means Unsloth dynamic 4-bit quants ("slightly more VRAM than standard BitsAndBytes 4-bit models but offer significantly higher accuracy"). `bnb-4bit` means standard BitsAndBytes 4-bit. No suffix means the original 16-bit or 8-bit weights, sometimes with chat-template or tokenizer fixes.
- **RL:** an "agent" learns "by interacting with an environment and receiving feedback in the form of rewards or penalties". It is used "when you need a model to excel at a specific behavior (e.g., tool-calling) using an environment and reward function rather than labeled data."
- **GGUF:** the format produced by llama.cpp for Ollama, llama.cpp and LM Studio.
- **gradient_accumulation_steps:** "Simulates a larger batch size without increasing memory usage."

## Evidence and examples
- Use cases: headline sentiment effect on a company, customer-interaction data, legal texts (contract analysis, case law, compliance).
- "OpenAI's **GPT-5** was post-trained to improve instruction following and helpful chat behavior." (given as an example; not sourced)
- Example model id: `unsloth/llama-3.1-8b-unsloth-bnb-4bit`.
- Evaluation: chat manually, set `evaluation_steps = 100`, or hold out 20% of the data.

## Inconsistencies / open questions
- [open question] "just 3GB VRAM" is a best case for small models and is not tied to a model size on this page. The per-model VRAM table is on the uncaptured "Unsloth Requirements" page. Capturing it would settle concrete hardware guidance.
- [verified] There is a tension inside the page: "Llama-3 supports 8192, we recommend 2048 for testing" while also claiming "Unsloth enables 4× longer context fine-tuning". These are not contradictory, but the 4× claim has no baseline stated. Checked in section 2.
- [open question] "QLoRA quantizes to 4-bit to save 75% memory" and "load_in_4bit… reducing memory use 4×" are the vendor's arithmetic on weight storage. Total training memory savings are smaller. The QLoRA paper (`dettmers-2023-qlora.pdf.md`) would settle this.
- [open question] "Fine-tuning can replicate all of RAG's capabilities" and "When done correctly, LoRA can match FFT" are vendor claims with no citation on this page. Treat them as opinion.
- [open question] TRL's docs summarize Unsloth as "up to 2× faster with up to 70% less VRAM" (`hf-trl-sft-trainer.web.md`). This page states "2x faster inference" but gives no training-speed figure. The figures are not directly comparable.
- [open question] Version-sensitive: model names in the sidebar (Qwen3.8-27B, Kimi K3), "Unsloth Studio", and "Dynamic 3.0 GGUFs" reflect the site as of capture. The body is "Last updated 6 months ago".
- [verified] Typo in the source: "For inidivudal tutorials on models" appears as written. Also "Unsloth **all types models**" is missing a verb. Both are left verbatim.
- [open question] AWS Bedrock fine-tuning support could not be captured (JS-rendered docs), so no claim about Bedrock is sourced in this batch.

## Images / diagrams
- `unsloth-fine-tuning-guide.web/images/image.png` (780×224)
  - Provenance: site logo "unsloth final space black.png", alt "Logo" (header). Kept because width is 300 px or more.
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `unsloth-fine-tuning-guide.web/images/image-2.png` (780×224)
  - Provenance: site logo "unsloth final space white.png", alt "Logo" (header, dark-theme variant).
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `unsloth-fine-tuning-guide.web/images/image-3.png` (1147×505)
  - Provenance: figure under "What is LoRA/QLoRA?". Caption: "Instead of optimizing Model Weights (yellow), we optimize 2 thin matrices A and B." (gitbook blob 715b6260)
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `unsloth-fine-tuning-guide.web/images/image-4.jpg` (2304×1264)
  - Provenance: screenshot after the "Introducing Unsloth Studio" callout ("more cropped ui for homepage.png").
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `unsloth-fine-tuning-guide.web/images/image-5.png` (1452×718)
  - Provenance: figure in section 2 before "You can change the model name…" ("model name change.png"). Likely a notebook code cell.
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `unsloth-fine-tuning-guide.web/images/image-6.png` (1382×968)
  - Provenance: figure in section 6. Caption: "The training loss will appear as numbers" (blob feb9b0f5).
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `unsloth-fine-tuning-guide.web/images/image-7.jpg` (2304×660)
  - Provenance: first of two figures in section 7 "Running + Deploying the model" (blob f2d5f23f), showing running the trained model.
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `unsloth-fine-tuning-guide.web/images/image-8.png` (2304×776)
  - Provenance: second figure in section 7 (blob cdf5d779, "image (47).png"), a multi-turn call example.
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `unsloth-fine-tuning-guide.web/images/image-9.png` (2155×685)
  - Provenance: first of two figures under "Saving + Deployment" (blob 8c577103). Likely the code that saves the LoRA adapter.
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `unsloth-fine-tuning-guide.web/images/image-10.png` (2300×1054)
  - Provenance: second figure under "Saving + Deployment" (blob 1a1be852). Likely loading or pushing to the Hub.
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `unsloth-fine-tuning-guide.web/images/image-11.png` (2304×2304)
  - Provenance: decorative mascot "sloth sparkling square.png" at the end of section 8.
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->

## Raw / preserved excerpts

> # 🧬Fine-tuning LLMs Guide
>
> Learn all the basics and best practices of fine-tuning. Beginner-friendly.
>
> ## 1. What Is Fine-tuning?
>
> Fine-tuning / training / post-training models customizes its behavior, enhances + injects knowledge, and optimizes performance for domains and specific tasks. For example:
>
> - OpenAI's **GPT-5** was post-trained to improve instruction following and helpful chat behavior.
> - The standard method of post training is called Supervised Fine-Tuning (SFT). Other methods include preference optimization (DPO, ORPO), distillation and Reinforcement Learning (RL) (GRPO, GSPO), where an "agent" learns to make decisions by interacting with an environment and receiving **feedback** in the form of **rewards** or **penalties**.
>
> With Unsloth, you can fine-tune or do RL for free on Colab, Kaggle, or locally with just 3GB VRAM by using our notebooks. By fine-tuning a pre-trained model on a dataset, you can:
>
> - **Update + Learn New Knowledge**: Inject and learn new domain-specific information.
> - **Customize Behavior**: Adjust the model's tone, personality, or response style.
> - **Optimize for Tasks**: Improve accuracy and relevance for specific use cases.
>
> **Example fine-tuning or RL use-cases**:
>
> - Enables LLMs to predict if a headline impacts a company positively or negatively.
> - Can use historical customer interactions for more accurate and custom responses.
> - Fine-tune LLM on legal texts for contract analysis, case law research, and compliance.
>
> You can think of a fine-tuned model as a specialized agent designed to do specific tasks more effectively and efficiently. **Fine-tuning can replicate all of RAG's capabilities**, but not vice versa.

> #### ❓What is LoRA/QLoRA?
>
> In LLMs, we have model weights. Llama 70B has 70 billion numbers. Instead of changing all 70B numbers, we instead add thin matrices A and B to each weight, and optimize those. This means we only optimize 1% of weights. LoRA is when the original model is 16-bit unquantized while QLoRA quantizes to 4-bit to save 75% memory.
>
> Instead of optimizing Model Weights (yellow), we optimize 2 thin matrices A and B.
>
> #### Fine-tuning misconceptions:
>
> You may have heard that fine-tuning does not make a model learn new knowledge or RAG performs better than fine-tuning. That is **false**. You can train a specialized coding model with fine-tuning and RL while RAG can't change the model's weights and only augments what the model sees at inference time.
>
> Introducing Unsloth Studio: Our new open-source web UI for training and running models. This means you can now fine-tune models with no-code and have observability and automatic dataset creation features.

> ## 2. Choose the Right Model + Method
>
> If you're a beginner, it is best to start with a small instruct model like Llama 3.1 (8B) and experiment from there. You'll also need to decide between normal fine-tuning, RL, QLoRA or LoRA training:
>
> - **Reinforcement Learning (RL)** is used when you need a model to excel at a specific behavior (e.g., tool-calling) using an environment and reward function rather than labeled data. We have several notebook examples, but for most use-cases, standard SFT is sufficient.
> - **LoRA** is a parameter efficient training method that typically keeps the base model's weights frozen and trains a small set of added low-rank adapter weights (in 16-bit precision).
> - **QLoRA** combines LoRA with 4-bit precision to handle very large models with minimal resources.
> - Unsloth also supports full fine-tuning (FFT) and pretraining, which require significantly more resources, but FFT is usually unnecessary. When done correctly, LoRA can match FFT.
> - Unsloth **all types models**: text-to-speech, embedding, GRPO, RL, vision, multimodal and more.
>
> Research shows that **training and serving in the same precision** helps preserve accuracy. This means if you want to serve in 4-bit, train in 4-bit and vice versa.
>
> We recommend starting with QLoRA, as it is one of the most accessible and effective methods for training models. Our dynamic 4-bit quants, the accuracy loss for QLoRA compared to LoRA is now largely recovered.
>
> You can change the model name to whichever model you like by matching it with model's name on Hugging Face e.g. '`unsloth/llama-3.1-8b-unsloth-bnb-4bit`'.
>
> We recommend starting with **Instruct models**, as they allow direct fine-tuning using conversational chat templates (ChatML, ShareGPT etc.) and require less data compared to **Base models** (which uses Alpaca, Vicuna etc).
>
> - Model names ending in `unsloth-bnb-4bit` indicate they are Unsloth dynamic 4-bit quants. These models consume slightly more VRAM than standard BitsAndBytes 4-bit models but offer significantly higher accuracy.
> - If a model name ends with just `bnb-4bit`, without "unsloth", it refers to a standard BitsAndBytes 4-bit quantization.
> - Models with **no suffix** are in their original **16-bit or 8-bit formats**. While they are the original models from the official model creators, we sometimes include important fixes - such as chat template or tokenizer fixes. So it's recommended to use our versions when available.
>
> There are other settings which you can toggle:
>
> - `max_seq_length = 2048` – Controls context length. While Llama-3 supports 8192, we recommend 2048 for testing. Unsloth enables 4× longer context fine-tuning.
> - `dtype = None` – Defaults to None; use `torch.float16` or `torch.bfloat16` for newer GPUs.
> - `load_in_4bit = True` – Enables 4-bit quantization, reducing memory use 4× for fine-tuning. Disabling it enables LoRA 16-bit fine-tuning. You can also enable 16-bit LoRA with `load_in_16bit = True`
> - To enable full fine-tuning (FFT), set `full_finetuning = True`. For 8-bit fine-tuning, set `load_in_8bit = True`.
> - **Note:** Only one training method can be set to `True` at a time.
>
> A common mistake is jumping straight into full fine-tuning (FFT), which is compute-heavy. Start by testing with LoRA or QLoRA first, if it won't work there, it almost certainly won't work with FFT. And if LoRA fails, don't assume FFT will magically fix it.

> ## 3. Your Dataset
>
> For LLMs, datasets are collections of data that can be used to train our models. In order to be useful for training, text data needs to be in a format that can be tokenized.
>
> - You will need to create a dataset usually with 2 columns - question and answer. The quality and amount will largely reflect the end result of your fine-tune so it's imperative to get this part right.
> - You can synthetically generate data and structure your dataset (into QA pairs) using ChatGPT or local LLMs.
> - You can also use our new Synthetic Dataset notebook which automatically parses documents (PDFs, videos etc.), generates QA pairs and auto cleans data using local models like Llama 3.2.
> - Fine-tuning can learn from an existing repository of documents and continuously expand its knowledge base, but just dumping data alone won't work as well. For optimal results, curate a well-structured dataset, ideally as question-answer pairs. This enhances learning, understanding, and response accuracy.
> - But, that's not always the case, e.g. if you are fine-tuning a LLM for code, just dumping all your code data can actually enable your model to yield significant performance improvements, even without structured formatting. So it really depends on your use case.
>
> For most of our notebook examples, we utilize the Alpaca dataset however other notebooks like Vision will use different datasets which may need images in the answer ouput as well.

> ## 5. Install + Requirements
>
> You can use Unsloth via two main ways, our free notebooks or locally.
>
> ### Unsloth Notebooks
>
> We would recommend beginners to utilise our pre-made notebooks first as it's the easiest way to get started with guided steps. You can later export the notebooks to use locally.
>
> ### Local Installation
>
> You can also install Unsloth locally via Docker or `pip install unsloth` (with Linux, WSL or Windows). Also depending on the model you're using, you'll need enough VRAM and resources.
>
> Installing Unsloth will require a Windows or Linux device. Once you install Unsloth, you can copy and paste our notebooks and use them in your own local environment.

> ## 6. Training + Evaluation
>
> Once you have everything set, it's time to train! If something's not working, remember you can always change hyperparameters, your dataset etc.
>
> You'll see a log of numbers during training. This is the training loss, which shows how well the model is learning from your dataset. For many cases, a loss around 0.5 to 1.0 is a good sign, but it depends on your dataset and task. If the loss is not going down, you might need to adjust your settings. If the loss goes to 0, that could mean overfitting, so it's important to check validation too.
>
> We generally recommend keeping the default settings unless you need longer training or larger batch sizes.
>
> - `per_device_train_batch_size = 2` – Increase for better GPU utilization but beware of slower training due to padding. Instead, increase `gradient_accumulation_steps` for smoother training.
> - `gradient_accumulation_steps = 4` – Simulates a larger batch size without increasing memory usage.
> - `max_steps = 60` – Speeds up training. For full runs, replace with `num_train_epochs = 1` (1–3 epochs recommended to avoid overfitting).
> - `learning_rate = 2e-4` – Lower for slower but more precise fine-tuning. Try values like `1e-4`, `5e-5`, or `2e-5`.
>
> #### Evaluation
>
> In order to evaluate, you could do manually evaluation by just chatting with the model and see if it's to your liking. You can also enable evaluation for Unsloth, but keep in mind it can be time-consuming depending on the dataset size. To speed up evaluation you can: reduce the evaluation dataset size or set `evaluation_steps = 100`.
>
> For testing, you can also take 20% of your training data and use that for testing. If you already used all of the training data, then you have to manually evaluate it. You can also use automatic eval tools but keep in mind that automated tools may not perfectly align with your evaluation criteria.

> ## 7. Running + Deploying the model
>
> … Reminder Unsloth itself provides **2x faster inference** natively as well, so always do not forget to call `FastLanguageModel.for_inference(model)`. If you want the model to output longer responses, set `max_new_tokens = 128` to some larger number like 256 or 1024.
>
> ### Saving + Deployment
>
> For saving and deploying your model in desired inference engines like Ollama, vLLM, Open WebUI, you will need to use the LoRA adapter on top of the base model. We have designated guides for each framework.
>
> If you're running inference on a single device (like a laptop or Mac), use llama.cpp to convert to GGUF format to use in Ollama, llama.cpp, LM Studio etc.
>
> If you're deploying an LLM for enterprise or multi-user inference for FP8, AWQ, use vLLM.
>
> We can now save the fine-tuned model as a small 100MB file called a LoRA adapter like below. You can instead push to the Hugging Face hub as well if you want to upload your model! Remember to get a Hugging Face token and add your token!
>
> After saving the model, we can again use Unsloth to run the model itself! Use `FastLanguageModel` again to call it for inference!
