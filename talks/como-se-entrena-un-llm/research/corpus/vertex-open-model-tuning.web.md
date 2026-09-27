---
source_file: vertex-open-model-tuning/
source_type: web-capture
ingested_at: 2026-09-26
---

# Supervised and distillation fine-tuning for open models (Google Cloud — Gemini Enterprise Agent Platform / Vertex AI)

## Provenance
- Original location: research/web/vertex-open-model-tuning/ (page.md used; breadcrumb navigation stripped, body starts at the H1)
- Format: html (web capture via talksmith:ingest)
- URL: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/open-model-tuning
- Fetched at: 2026-09-26T22:38:15Z (HTTP 200, 460,564 bytes)
- Author / source (if known): Google Cloud — official vendor documentation. **Vendor documentation captured 2026-09-26; model lists change fast — re-check before quoting as current.**
- Date of original (if known): page footer "Last updated 2026-09-25 UTC."

## Key claims
- Scope: "how to perform supervised and distillation fine-tuning on open models such as Llama 3.1." "Distillation lets you tune a smaller student model using the outputs of a larger teacher model."
- **Tuning modes:**
  - Supervised fine-tuning: **Full fine-tuning** and **Low-Rank Adaptation (LoRA)** — "LoRA is a parameter-efficient tuning mode that only adjust subset of parameters. It's more cost efficient and require less training data than full fine-tuning. On the other hand, full fine-tuning has higher quality potential by adjusting all parameters." SDK values: `tuning_mode="FULL"` or `"PEFT_ADAPTER"`.
  - **Distillation fine-tuning**: "uses the GenAI SDK, where you specify a teacher model to generate responses that are then used to tune a smaller student model." (`method="DISTILLATION"`, `base_teacher_model=…`).
- **Supervised fine-tuning supported models (verbatim, with Model Garden IDs):**
  - Gemma 4 E2B IT (`google/gemma4@gemma-4-e2b-it`)
  - Gemma 4 E4B IT (`google/gemma4@gemma-4-e4b-it`)
  - Gemma 4 26B A4B IT (`google/gemma4@gemma-4-26b-a4b-it`)
  - Gemma 4 31B IT (`google/gemma4@gemma-4-31b-it`)
  - Gemma 3 1B IT (`google/gemma3@gemma-3-1b-it`)
  - Gemma 3 4B IT (`google/gemma3@gemma-3-4b-it`)
  - Gemma 3 12B IT (`google/gemma3@gemma-3-12b-it`)
  - Gemma 3 27B IT (`google/gemma3@gemma-3-27b-it`)
  - Medgemma 1.5 4B IT (`google/medgemma@medgemma-1.5-4b-it`)
  - Qwen 3.6 27B (`qwen/qwen3-6@qwen3.6-27b`)
  - Qwen 3.6 35B A3B (`qwen/qwen3-6@qwen3.6-35b-a3b`)
  - Qwen 3.5 9B (`qwen/qwen3-5@qwen3.5-9b`)
  - Qwen 3 4B (`qwen/qwen3@qwen3-4b`)
  - Qwen 3 8B (`qwen/qwen3@qwen3-8b`)
  - Qwen 3 14B (`qwen/qwen3@qwen3-14b`)
  - Qwen 3 32B (`qwen/qwen3@qwen3-32b`)
  - Llama 3.1 8B (`meta/llama3_1@llama-3.1-8b`)
  - Llama 3.1 8B Instruct (`meta/llama3_1@llama-3.1-8b-instruct`)
  - Llama 3.2 1B Instruct (`meta/llama3-2@llama-3.2-1b-instruct`)
  - Llama 3.2 3B Instruct (`meta/llama3-2@llama-3.2-3b-instruct`)
  - Llama 3.3 70B Instruct (`meta/llama3-3@llama-3.3-70b-instruct`)
  - Llama 4 Scout 17B 16E Instruct (`meta/llama4@llama-4-scout-17b-16e-instruct`)
  - GLM 4.7 Flash (`zai-org/glm-4.7-flash@glm-4.7-flash`)
- **Open model families:** Gemma (Gemma 4, Gemma 3, MedGemma), Qwen (3, 3.5, 3.6), Llama (3.1, 3.2, 3.3, 4 Scout), GLM (Z.ai, 4.7 Flash).
- **Distillation — supported teacher models (verbatim):** DeepSeek R1 0528 MaaS (`deepseek-ai/deepseek-r1-0528-maas`); DeepSeek V3.2 MaaS (`deepseek-ai/deepseek-v3.2-maas`); Qwen 3 Next 80B A3B Thinking MaaS (`qwen/qwen3-next-80b-a3b-thinking-maas`).
- **Distillation — supported student models (verbatim):** Qwen 3 4B, Qwen 3 8B, Qwen 3 14B, Qwen 3 32B, Gemma 3 1B IT, Gemma 3 4B IT, Gemma 3 12B IT, Gemma 3 27B IT.
- Distillation is recommended for "transferring complex, multi-step **reasoning** capabilities from a larger teacher to a smaller student" (math, step-by-step domain QA, tasks where a "thinking"/CoT teacher is much better); "smaller gains on tasks where the student model already performs close to the teacher, or on short-form retrieval tasks".
- **Data format:** JSONL, one example per line, uploaded to Cloud Storage. Text-only formats: **prompt-completion** (`{"prompt": …, "completion": …}`), **turn-based chat** (`messages` with `system`/`user`/`assistant` roles), and **GenerateContent** (`systemInstruction` + `contents`/`parts`). Multimodal: chat format with `image_url` parts, or GenerateContent with `file_data`. Images: JPEG, PNG, WEBP, Base64.
- **You can tune from a custom checkpoint**: "A model that has the same architecture as one of the supported base models. This could be either a custom model checkpoint from a repository such as Hugging Face or a previously tuned model…"
- **Artifacts are yours:** outputs are `.safetensors` checkpoints in your Cloud Storage bucket; "You can also export the tuned model from Cloud Storage and deploy it elsewhere." Max 10 checkpoints stored.
- **Regions:** global endpoint "strongly recommended"; region-specific: `us-central1`, `europe-west4`, `us-west1`, `us-east5`, `asia-southeast1`, `asia-southeast2`.
- **Pricing:** training tokens = dataset tokens × epochs; distillation also billed for teacher-model API calls; plus Cloud Storage and Prediction.

## Definitions and terminology
- **Full fine-tuning:** adjusts all parameters; "higher quality potential".
- **LoRA (Low-Rank Adaptation):** "a parameter-efficient tuning mode that only adjust subset of parameters" (page wording); called `PEFT_ADAPTER` in the SDK and "Parameter-efficient fine-tuning" in the Limitations table.
- **Distillation fine-tuning:** teacher model generates responses → used to tune a smaller student. For distillation, the output dir also contains `distillation_labelled_dataset.jsonl` ("The labeled dataset from teacher model's inference").
- **MaaS:** models provided as a service; teachers are MaaS endpoints using "dynamic shared quota".
- **Managed tuning:** console path "Fine tune → Managed tuning".
- **IT:** instruction-tuned variant (Gemma naming; not defined on the page).

## Evidence and examples
- **Per-model limitations (verbatim values; page.md flattened the table):**

| Model | Tuning modes | Max sequence length | Modalities |
|---|---|---|---|
| Gemma 4 E2B IT | Parameter-efficient fine-tuning | 8192 | Text |
| Gemma 4 E4B IT | Parameter-efficient fine-tuning | 8192 | Text |
| Gemma 4 26B A4B IT | Parameter-efficient fine-tuning | 8192 | Text |
| Gemma 4 31B IT | Parameter-efficient fine-tuning | 8192 | Text |
| Gemma 3 1B IT | Full fine-tuning | 8192 | Text |
| Gemma 3 4B IT | Full fine-tuning | 8192 | Text |
| Gemma 3 12B IT | Full fine-tuning | 8192 | Text |
| Gemma 3 27B IT | Parameter-efficient fine-tuning; Full fine-tuning | 8192 | Text |
| Medgemma 1.5 4B IT | Full fine-tuning | 8192 | Text |
| Qwen 3.6 27B | Parameter-efficient fine-tuning | 12288 | Text |
| Qwen 3.6 35B A3B | Parameter-efficient fine-tuning | 12288 | Text |
| Qwen 3.5 9B | Full fine-tuning | 8192 | Text |
| Qwen 3 4B | Full fine-tuning | 8192 | Text |
| Qwen 3 8B | Full fine-tuning | 8192 | Text |
| Qwen 3 14B | Full fine-tuning | 8192 | Text |
| Qwen 3 32B | Parameter-efficient fine-tuning; Full fine-tuning | 8192 | Text |
| Llama 3.1 8B | Parameter-efficient fine-tuning; Full fine-tuning | 8192 | Text |
| Llama 3.1 8B Instruct | Parameter-efficient fine-tuning; Full fine-tuning | 8192 | Text |
| Llama 3.2 1B Instruct | Full fine-tuning | 8192 | Text |
| Llama 3.2 3B Instruct | Full fine-tuning | 8192 | Text |
| Llama 3.3 70B Instruct | Parameter-efficient fine-tuning; Full fine-tuning | 8192 | Text |
| Llama 4 Scout 17B 16E Instruct | Parameter-efficient fine-tuning | 2048 | Text, Images* |
| GLM 4.7 Flash | Parameter-efficient fine-tuning | 8192 | Text |

  \*"Mixed datasets of both text-only and image examples are not supported. If there is at least one image example in the dataset, all text-only examples will be filtered out."
- SFT job (Agent Platform SDK): `sft.train(source_model=SourceModel(base_model="meta/llama3_1@llama-3.1-8b", custom_base_model="gs://…"), tuning_mode="FULL", epochs=3, train_dataset="gs://…", validation_dataset="gs://…", output_uri="gs://…")`.
- Distillation job (GenAI SDK): `client.tunings.tune(base_model="qwen/qwen3@qwen3-4b", …, config=types.CreateTuningJobConfig(method="DISTILLATION", base_teacher_model="qwen/qwen3-next-80b-a3b-thinking-maas", epoch_count=3, …))`.
- Deploy example: `model_garden.CustomModel(gcs_uri=…/postprocess/node-0/checkpoints/final)` → `model.deploy(machine_type="g2-standard-12", accelerator_type="NVIDIA_L4", accelerator_count=1)`.
- Quota name: `Global concurrent managed OSS model fine-tuning jobs per project`.

## Inconsistencies / open questions
- [verified] Tuning-mode availability is per model and not uniform: e.g. Gemma 4 and Qwen 3.6 are PEFT-only; Gemma 3 1B/4B/12B, Qwen 3 4B/8B/14B, Qwen 3.5 9B, Llama 3.2 1B/3B, MedGemma are full-only; Gemma 3 27B, Qwen 3 32B, Llama 3.1 8B (+Instruct), Llama 3.3 70B offer both — checked against the Limitations table. The intro's "Full fine-tuning / LoRA" is not available for every model.
- [verified] The table's multi-value cells were split across lines in page.md ("Parameter-efficient fine-tuning  \nFull fine-tuning") — reconstruction above reads these as "both modes". Checked in page.md.
- [verified] The "Before you begin" steps 1–4 are duplicated as 5–7 on the page (source-side duplication, not extraction) — seen in page.md; omitted from excerpts.
- [open question] Version-sensitive: model roster (Gemma 4, Qwen 3.6, GLM 4.7 Flash, Llama 4 Scout), sequence limits, and regions are as of "Last updated 2026-09-25 UTC".
- [open question] The page equates "LoRA" with "Parameter-efficient fine-tuning"/`PEFT_ADAPTER`; whether QLoRA or other PEFT methods are used internally is not stated.
- [open question] AWS Bedrock fine-tuning support could not be captured (JS-rendered docs), so no claim about Bedrock is sourced in this batch.

## Images / diagrams
- None retained. Dropped per instruction (both dimensions < 300 px): `lockup_full_color.svg` (224×36 viewBox) and `192px.svg` (192×192) — site/product logos. Companion folder `vertex-open-model-tuning.web/images/` exists and is empty.

## Raw / preserved excerpts

> # Supervised and distillation fine-tuning for open models
>
> This page describes how to perform supervised and distillation fine-tuning on open models such as Llama 3.1. Unless stated otherwise, the instructions on this page apply to both supervised fine-tuning and distillation fine-tuning. Distillation lets you tune a smaller student model using the outputs of a larger teacher model.
>
> ## Supported tuning modes
>
> - **Supervised fine-tuning:**
>   - Full fine-tuning
>   - Low-Rank Adaptation (LoRA): LoRA is a parameter-efficient tuning mode that only adjust subset of parameters. It's more cost efficient and require less training data than full fine-tuning. On the other hand, full fine-tuning has higher quality potential by adjusting all parameters.
> - **Distillation fine-tuning:** Distillation fine-tuning uses the GenAI SDK, where you specify a teacher model to generate responses that are then used to tune a smaller student model.
>
> ### Recommended use cases for distillation fine-tuning
>
> Distillation fine-tuning is most effective when the teacher model is substantially more capable than the student on the target task. It is recommended for transferring complex, multi-step **reasoning** capabilities from a larger teacher to a smaller student, including:
>
> - Math and quantitative reasoning
> - Scientific, medical, and other domain-specific question answering that requires step-by-step reasoning
> - Other tasks where a strong teacher model with "thinking" or chain-of-thought behavior consistently produces higher-quality responses than the student.
>
> Distillation provides smaller gains on tasks where the student model already performs close to the teacher, or on short-form retrieval tasks where the teacher's reasoning trace does not add value.

> ## Supported regions
>
> Global endpoint (`global`) is **strongly recommended** for launching tuning jobs; it will select a supported region with available capacity and launch a tuning job. Note the following considerations when launching a job from the global endpoint:
>
> - When you create a global tuning job, a corresponding regional tuning job (in the selected region) will be created. **You will only be charged quota and billed against a single tuning job.**
> - Sub-resources (like tensorboard experiments or models) will be created in the target region that was selected. The location can be be extracted from the full resource name and queried using the Vertex AI SDK.
>
> Region-specific tuning jobs are still available for users with more advanced needs (such as all resources scoped to a single region): Iowa (`us-central1`), Netherlands (`europe-west4`), Oregon (`us-west1`), Columbus (`us-east5`), Singapore (`asia-southeast1`), Jakarta (`asia-southeast2`).

> ## Prepare dataset for tuning
>
> A training dataset is required for tuning. You are recommended to prepare an optional validation dataset if you'd like to evaluate your tuned model's performance.
>
> Your dataset must be in one of the following supported JSON Lines (JSONL) formats, where each line contains a single tuning example.
>
> Upload your JSONL files to Cloud Storage.
>
> ### Text-only datasets
>
> ### Prompt completion
>
> ```
> {"prompt": "<prompt text>", "completion": "<ideal generated text>"}
> ```
>
> ### Turn based chat format
>
> ```
> {"messages": [
>   {"content": "You are a chatbot that helps with scientific literature and generates state-of-the-art abstracts from articles.",
>     "role": "system"},
>   {"content": "Summarize the paper in one paragraph.",
>     "role": "user"},
>   {"content": " Here is a one paragraph summary of the paper:\n\nThe paper describes PaLM, ...",
>     "role": "assistant"}
> ]}
> ```
>
> ### GenerateContent
>
> ```
> {
> "systemInstruction": {
>   "parts": [{ "text": "You are a chatbot that helps with scientific literature and generates state-of-the-art abstracts from articles." }]},
> "contents": [
>   {"role": "user",
>     "parts": [{ "text": "Summarize the paper in one paragraph." }]},
>   {"role": "assistant",
>     "parts": [{ "text": "Here is a one paragraph summary of the paper:\n\nThe paper describes PaLM, ..." }]}
> ]}
> ```
>
> ### Multimodal datasets
>
> ### Turn based chat format
>
> ```
> {"messages": [
>   {"role": "user", "content": [
>     {"type": "text", "text": "You are a chatbot that helps with scientific literature and generates state-of-the-art abstracts from articles."},
>     {"type": "image_url", "image_url": {
>       "url": "gs://your-gcs-bucket/your-image.jpeg",
>       "detail": "low"}}]
>   },
>   {"role": "assistant", "content": [
>     {"type": "text", "text": "Here is a one paragraph summary of the paper:\n\nThe paper describes PaLM, ..."}]
>   },
>   {"role": "user", "content": [
>     {"type": "text", "text": "You are a chatbot that helps with scientific literature and generates state-of-the-art abstracts from articles."},
>     {"type": "image_url", "image_url": {
>       "url": "data:image/jpeg;base64,<base64 image>",
>       "detail": "low"}}]
>   },
>   {"role": "assistant", "content": [
>     {"type": "text", "text": "Here is a one paragraph summary of the paper:\n\nThe paper describes PaLM, ..."}]
>   },
> ]}
> ```
>
> ### GenerateContent
>
> ```
> {
> "systemInstruction": {
>   "parts": [{ "text": "You are a chatbot that helps with scientific literature and generates state-of-the-art abstracts from articles." }]},
> "contents": [
>   {"role": "user",
>     "parts": [
>       {"text": "You are a chatbot that helps with scientific literature and generates state-of-the-art abstracts from articles." },
>       {"file_data": {
>         "mime_type": "image/jpeg", "file_uri": "gs://your-gcs-bucket/your-image.jpeg"}}]
>   },
>   {"role": "assistant",
>     "parts": [{ "text": "Here is a one paragraph summary of the paper:\n\nThe paper describes PaLM, ..." }]}
> ]}
> ```
>
> Supported formats include JPEG, PNG, WEBP, and Base64-encoded images.
>
> Note that if your images are stored under a different Cloud Storage bucket from your JSONL files, make sure that you have granted the Storage Object User (`roles/storage.objectUser`) IAM role on both buckets for these two service accounts: `service-PROJECT_NUMBER@gcp-sa-vertex-moss-ft.iam.gserviceaccount.com`, `service-PROJECT_NUMBER@gcp-sa-aiplatform.iam.gserviceaccount.com`

> ## Create tuning job
>
> You can tune from:
>
> - A supported base model, such as Llama 3.1
> - A model that has the same architecture as one of the supported base models. This could be either a custom model checkpoint from a repository such as Hugging Face or a previously tuned model from a Gemini Enterprise Agent Platform tuning job. This lets you continue tuning a model that has already been tuned.
>
> ### Cloud Console (Supervised)
>
> 1. You can initiate fine tuning in the following ways: Go the model card and click **Fine tune** and choose **Managed tuning**. or Go to the **Tuning** page and click **Create tuned model**.
> 2. Fill out the parameters and click **Start tuning**.
>
> This starts a tuning job, which you can see in the Tuning page under the **Managed tuning** tab. Once the tuning job has finished, you can view the information about the tuned model in the **Details** tab.
>
> ### Agent Platform SDK (Supervised)
>
> ```
> sft_tuning_job = sft.train(
>     source_model=SourceModel(
>       base_model="meta/llama3_1@llama-3.1-8b",
>       # Optional, folder that is either a custom model checkpoint or previously tuned model
>       custom_base_model="gs://{STORAGE-URI}",
>     ),
>     tuning_mode="FULL", # FULL or PEFT_ADAPTER
>     epochs=3,
>     train_dataset="gs://{STORAGE-URI}", # JSONL file
>     validation_dataset="gs://{STORAGE-URI}", # JSONL file
>     output_uri="gs://{STORAGE-URI}",
> )
> ```
>
> ### GenAI SDK (Distillation)
>
> ```
> tuning_job = client.tunings.tune(
>     base_model="qwen/qwen3@qwen3-4b",
>     training_dataset=types.TuningDataset(
>         gcs_uri="gs://{STORAGE-URI}"
>     ),
>     config=types.CreateTuningJobConfig(
>         method="DISTILLATION",
>         base_teacher_model="qwen/qwen3-next-80b-a3b-thinking-maas",
>         epoch_count=3,
>         validation_dataset=types.TuningValidationDataset(
>             gcs_uri="gs://{STORAGE-URI}"
>         ),
>         output_uri="gs://{STORAGE-URI}",
>     ),
> )
> ```

> ## Tuned model artifacts
>
> When the tuning job finishes, the model artifacts for the tuned model are stored in your Cloud Storage output directory.
>
> ```
> gs://<output_dir>/
>     # (Distillation tuning only) The labeled dataset from teacher model's inference
>     -> distillation_labelled_dataset.jsonl
>
> gs://<output_dir>/postprocess/node-0/checkpoints/
>     # Final checkpoint
>     -> final/
>         -> model-00001-of-000xx.safetensors
>         -> model-000yy-of-000xx.safetensors
>     # Intermediate checkpoints
>     -> checkpoint-M/ … -> checkpoint-N/
> ```
>
> - A maximum of 10 checkpoints are stored.
> - If the number of epochs (E) is less than 10, then exactly E checkpoints are stored (one for each epoch).
> - Intermediate checkpoints from range M to N are ordered. Note that intermediate checkpoints are not always consecutively numbered. For example, checkpoints might be numbered 1, 3, 5, 10 rather than 1, 2, 3, 4.

> ## Deploy tuned model
>
> You can deploy the tuned model to a Gemini Enterprise Agent Platform endpoint. You can also export the tuned model from Cloud Storage and deploy it elsewhere.
>
> ```
> from vertexai.preview import model_garden
> MODEL_ARTIFACTS_STORAGE_URI = "gs://{STORAGE-URI}/postprocess/node-0/checkpoints/final"
> model = model_garden.CustomModel(gcs_uri=MODEL_ARTIFACTS_STORAGE_URI)
> # deploy the model to an endpoint using GPUs. Cost will incur for the deployment
> endpoint = model.deploy(machine_type="g2-standard-12", accelerator_type="NVIDIA_L4", accelerator_count=1)
> ```
>
> Notice that managed open models use the `chat.completions` method instead of the `predict` method used by deployed models.

> ## Limits and quotas
>
> Quota is enforced on the number of concurrent tuning jobs. Every project comes with a default quota to run at least one tuning job. This is a global quota, shared across all available regions and supported models. If you want to run more jobs concurrently, you need to request additional quota for `Global concurrent managed OSS model fine-tuning jobs per project`.
>
> In addition to the tuning job quota, distillation fine-tuning uses the teacher model, and your project must have sufficient quota for the specified teacher model. Open models provided as a service (MaaS) use dynamic shared quota. When a tuning job calls a teacher model, it consumes from the project's shared quota for that model.

> ## Pricing
>
> You are billed for tuning based on pricing for Model tuning. The number of training tokens is calculated by multiplying the number of tokens in your training dataset by the number of epochs. For distillation tuning, you are also billed for the API calls made to the teacher model to generate responses, based on pricing for managed models.
>
> You are also billed for related services, such as Cloud Storage and Gemini Enterprise Agent Platform Prediction.
