---
source_file: vertex-gemini-supervised-tuning/
source_type: web-capture
ingested_at: 2026-09-26
---

# About supervised fine-tuning for Gemini models (Google Cloud — Gemini Enterprise Agent Platform, formerly Vertex AI docs path)

## Provenance
- Original location: research/web/vertex-gemini-supervised-tuning/ (page.md used; breadcrumb navigation stripped, body starts at the H1)
- Format: html (web capture via talksmith:ingest)
- URL: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning
- Fetched at: 2026-09-26T22:38:14Z (HTTP 200, 415,155 bytes)
- Author / source (if known): Google Cloud — official vendor documentation. **Vendor documentation captured 2026-09-26; model lists change fast — re-check before quoting as current.**
- Date of original (if known): page footer "Last updated 2026-09-25 UTC."
- Naming note: the page and URL use the product name **"Gemini Enterprise Agent Platform"**; code samples still use the `vertexai` SDK and `aiplatform.googleapis.com` endpoints. The capture folder is named "vertex-…" by the presenter.

## Key claims
- **Supported models (verbatim list, "The following Gemini models support supervised fine-tuning:"):**
  - Gemini 3.5 Flash
  - Gemini 3.1 Flash-Lite
  - Gemini 2.5 Pro
  - Gemini 2.5 Flash-Lite
  - Gemini 2.5 Flash
- **Modalities:** "You can tune text, image, audio, video, and document data types."
- **Mechanism:** "Supervised fine-tuning adapts model behavior with a labeled dataset. This process adjusts the model's weights to minimize the difference between its predictions and the actual labels."
- **When to use:** "a good option when you have a well-defined task with available labeled data. It's particularly effective for domain-specific applications where the language or content significantly differs from the data the large model was originally trained on."
- Task types it improves: Classification, Summarization, Extractive question answering, Chat.
- **Data format:** training data is a **JSONL** file ("Maximum training dataset file size: 1GB for JSONL"); examples are shown as **Prompt → Response** pairs (see Evidence). The page does not spell out the JSONL schema itself (it links to per-modality pages: text / image / audio / video / document, not captured).
- **Adapter-based tuning:** every model's limits table has an "Adapter size" parameter (1, 2, 4, 8, 16; Gemini 2.5 Pro only 1, 2, 4, 8) — i.e. Gemini tuning here is adapter (parameter-efficient) tuning, the user chooses adapter size, not full-weight tuning. (The page does not use the words "LoRA" or "full fine-tuning"; this is an inference from the "Adapter size" field — see Inconsistencies.)
- **SLA:** "Supervised fine-tuning is not a Covered Service and is excluded from the SLO of any Service Level Agreement."
- **Pricing:** "The number of training tokens is calculated by multiplying the number of tokens in your training dataset by the number of epochs. After tuning, inference (prediction request) costs for the tuned model still apply. Inference pricing is the same for each stable version of Gemini."
- **Quota:** concurrent tuning jobs; "Every project comes with a default quota to run at least one tuning job" (global quota "Global concurrent tuning jobs").
- **Regions (3.5 Flash / 3.1 Flash-Lite):** tuning in `us-central1` and `europe-west4`; tuned-model serving on `us` and `eu` multi-region endpoints only; CMEK not supported. "During tuning, computation could be offloaded to other `US` or `EU` regions for available accelerators."
- **Known issue:** don't use controlled generation (structured-output constraints) at inference on tuned models — "Supervised fine-tuning effectively customizes the model to generate structured output. Therefore you don't need to apply controlled generation when making inference requests on tuned models."
- **Integrated evaluation (Preview)** with the Gen AI evaluation service during tuning — supported models: `gemini-2.5-pro`, `gemini-2.5-flash`, and `gemini-2.5-flash-lite`.

## Definitions and terminology
- **Supervised fine-tuning (SFT):** "adapts model behavior with a labeled dataset… adjusts the model's weights to minimize the difference between its predictions and the actual labels."
- **Adapter size:** a tuning hyperparameter with values 1/2/4/8/16 (not further defined on this page).
- **Controlled generation:** Google's term for constraining output format at inference time (linked, not defined here).
- **Tuning job region:** where "user data, such as the transformed dataset and the tuned model, is stored".
- **Covered Service:** SLA term; SFT is excluded.

## Evidence and examples
- Limits per model (verbatim values):

| Spec | Gemini 3.5 Flash | Gemini 3.1 Flash-Lite | Gemini 2.5 Flash / 2.5 Flash-Lite | Gemini 2.5 Pro |
|---|---|---|---|---|
| Max input+output tokens per training example | 131,072 | 131,072 | 131,072 | 131,072 ("training tokens") |
| Max serving tokens | Same as base Gemini model | same | same | same |
| Max validation examples | 5000 examples or 30% of the number of training examples if there are more than 1000 validation examples | same | same | same |
| Max training file size | 1GB for JSONL | same | same | same |
| Max training dataset size | 10M text-only examples or 300K multimodal examples | same | same | same |
| Adapter size | 1, 2, 4, 8, and 16 | 1, 2, 4, 8, and 16 | 1, 2, 4, 8, and 16 | 1, 2, 4, and 8 |
| Tuning endpoint | `us-central1`, `europe-west4` | `us-central1`, `europe-west4` | (not stated) | (not stated) |
| Tuned-model serving | `us` and `eu` multi-region only | same | (not stated) | (not stated) |
| CMEK | Not supported | Not supported | (not stated) | (not stated) |

- Worked Prompt/Response examples (verbatim): Classification ("Classify the following text into one of the following classes: [business, entertainment]. Text: Diversify your investment portfolio" → "business"); Summarization with PII replaced (`#Person1`, `#Person2`); Extractive QA ("What does LGM stand for?" → "Last Glacial Maximum"); Chat persona ("As the virtual shopkeeper of Example Organization, I can only help you with the purchases and shipping.").
- Region selection code: `vertexai.init(project='myproject', location='us-central1')`; REST: `https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs` (method `tuningJobs.create`).
- Blog links cited (not captured): "Hundreds of organizations are fine-tuning Gemini models. Here's their favorite use cases"; "When to use supervised fine-tuning for Gemini".

## Inconsistencies / open questions
- [verified] The supported-models list includes **Gemini 2.5 Flash-Lite** but the Limitations section has no separate table header for it: page.md renders "### Gemini 2.5 Flash" followed by a bare line "Gemini 2.5 Flash-Lite" and a single table — a tab widget flattened by extraction; the two share one table. Checked in page.md lines 72–75.
- [verified] The integrated-evaluation feature lists only Gemini 2.5 models (`gemini-2.5-pro`, `gemini-2.5-flash`, `gemini-2.5-flash-lite`), not 3.5 Flash / 3.1 Flash-Lite, while SFT itself supports all five — checked both lists on the same page.
- [open question] Version-sensitive: the model list (Gemini 3.5 Flash, 3.1 Flash-Lite, 2.5 family), token limits, and regions are as of "Last updated 2026-09-25 UTC". Re-check before the talk.
- [open question] "Adapter size" implies adapter/LoRA-style tuning, but the page never names LoRA nor says full fine-tuning is unavailable for Gemini. Settle via Google's "tuning approaches" page (not captured).
- [open question] The exact JSONL schema for Gemini SFT (e.g. `contents` / `role` / `parts`) is on the linked per-modality pages, not this one. The sibling open-model page (`vertex-open-model-tuning.web.md`) shows JSONL formats for open models; do not assume they are identical for Gemini.
- [open question] The product is named "Gemini Enterprise Agent Platform" in this capture; whether "Vertex AI" is still the marketed name is not settled by this page (SDK still `vertexai`).
- [open question] AWS Bedrock fine-tuning support could not be captured (JS-rendered docs), so no claim about Bedrock is sourced in this batch.

## Images / diagrams
- None retained. Dropped per instruction (both dimensions < 300 px): `lockup_full_color.svg` (Google Cloud Documentation logo, 224×36 viewBox) and `192px.svg` (Gemini product logo, 192×192). Companion folder `vertex-gemini-supervised-tuning.web/images/` exists and is empty.

## Raw / preserved excerpts

> # About supervised fine-tuning for Gemini models
>
> Supervised fine-tuning is a good option when you have a well-defined task with available labeled data. It's particularly effective for domain-specific applications where the language or content significantly differs from the data the large model was originally trained on. You can tune text, image, audio, video, and document data types. You can also create Gemini-based applications and agents that can interact with real-time information and services like databases, customer relationship management systems, and document repositories.
>
> Supervised fine-tuning adapts model behavior with a labeled dataset. This process adjusts the model's weights to minimize the difference between its predictions and the actual labels. For example, it can improve model performance for the following types of tasks:
>
> - Classification
> - Summarization
> - Extractive question answering
> - Chat

> ## Supported models
>
> The following Gemini models support supervised fine-tuning:
>
> - Gemini 3.5 Flash
> - Gemini 3.1 Flash-Lite
> - Gemini 2.5 Pro
> - Gemini 2.5 Flash-Lite
> - Gemini 2.5 Flash

> ## Limitations
>
> Supervised fine-tuning is not a Covered Service and is excluded from the SLO of any Service Level Agreement.
>
> ### Gemini 3.5 Flash
>
> Specification Value Maximum input and output tokens per training example 131,072 Maximum input and output serving tokens Same as base Gemini model Maximum number of examples in a validation dataset 5000 examples or 30% of the number of training examples if there are more than 1000 validation examples Maximum training dataset file size 1GB for JSONL Maximum training dataset size 10M text-only examples or 300K multimodal examples Adapter size Supported values are 1, 2, 4, 8, and 16 Supported endpoint for model tuning `us-central1`, and `europe-west4` Supported endpoint for tuned model serving `us` and `eu` multi-region endpoints only CMEK support Not supported
>
> ### Gemini 3.1 Flash-Lite
>
> (identical values to Gemini 3.5 Flash)
>
> ### Gemini 2.5 Flash / Gemini 2.5 Flash-Lite
>
> Specification Value Maximum input and output tokens per training example 131,072 Maximum input and output serving tokens Same as base Gemini model Maximum number of examples in a validation dataset 5000 examples or 30% of the number of training examples if there are more than 1000 validation examples Maximum training dataset file size 1GB for JSONL Maximum training dataset size 10M text-only examples or 300K multimodal examples Adapter size Supported values are 1, 2, 4, 8, and 16
>
> ### Gemini 2.5 Pro
>
> Specification Value Maximum input and output training tokens 131,072 Maximum input and output serving tokens Same as base Gemini model Maximum validation dataset size 5000 examples or 30% of the number of training examples if there are more than 1000 validation examples Maximum training dataset file size 1GB for JSONL Maximum training dataset size 10M text-only examples or 300K multimodal examples Adapter size Supported values are 1, 2, 4, and 8

> ## Known issues
>
> Applying controlled generation when submitting inference requests to tuned Gemini models can result in decreased model quality due to data misalignment during tuning and inference time. During tuning, controlled generation isn't applied, so the tuned model isn't able to handle controlled generation well at inference time. Supervised fine-tuning effectively customizes the model to generate structured output. Therefore you don't need to apply controlled generation when making inference requests on tuned models.

> ## Use cases for using supervised fine-tuning
>
> Foundation models work well when the expected output or task can be clearly and concisely defined in a prompt and the prompt consistently produces the expected output. If you want a model to learn something niche or specific that deviates from general patterns, then you might want to consider tuning that model. For example, you can use model tuning to teach the model the following:
>
> - Specific structures or formats for generating output.
> - Specific behaviors such as when to provide a terse or verbose output.
> - Specific customized outputs for specific types of inputs.
>
> The following examples are use cases that are difficult to capture with only prompt instructions:
>
> - **Classification**: The expected response is a specific word or phrase.
>   **Prompt:** Classify the following text into one of the following classes: [business, entertainment]. Text: Diversify your investment portfolio
>   **Response:** business
>   Tuning the model can help prevent the model from generating verbose responses.
> - **Summarization**: The summary follows a specific format. For example, you might need to remove personally identifiable information (PII) in a chat summary.
>   **Prompt:** Summarize: Jessica: That sounds great! See you in Times Square! Alexander: See you at 10!
>   **Response:** #Person1 and #Person2 agree to meet at Times Square at 10:00 AM.
>   This formatting of replacing the names of the speakers with `#Person1` and `#Person2` is difficult to describe and the foundation model might not naturally produce such a response.
> - **Extractive question answering**: The question is about a context and the answer is a substring of the context.
>   **Prompt:** Context: There is evidence that there have been significant changes in Amazon rainforest vegetation over the last 21,000 years through the Last Glacial Maximum (LGM) and subsequent deglaciation. Question: What does LGM stand for?
>   **Response:** Last Glacial Maximum
>   The response "Last Glacial Maximum" is a specific phrase from the context.
> - **Chat**: You need to customize model response to follow a persona, role, or character.
>   **Prompt:** User: What's the weather like today?
>   **Response:** Assistant: As the virtual shopkeeper of Example Organization, I can only help you with the purchases and shipping.
>
> You can also tune a model in the following situations:
>
> - Prompts are not producing the expected results consistently enough.
> - The task is too complicated to define in a prompt. For example, you want the model to do behavior cloning for a behavior that's hard to articulate in a prompt.
> - You have complex intuitions about a task that are difficult to formalize in a prompt.
> - You want to reduce the context length by removing the few-shot examples.

> ## Configure a tuning job region
>
> User data, such as the transformed dataset and the tuned model, is stored in the tuning job region. During tuning, computation could be offloaded to other `US` or `EU` regions for available accelerators. The offloading is transparent to users.
>
> - If you use the Vertex AI SDK, you can specify the region at initialization. For example: `vertexai.init(project='myproject', location='us-central1')`
> - If you create a supervised fine-tuning job by sending a POST request using the `tuningJobs.create` method, then you use the URL to specify the region where the tuning job runs… `https://TUNING_JOB_REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/TUNING_JOB_REGION/tuningJobs`
> - If you use the Google Cloud console, you can select the region name in the **Region** drop-down field on the **Model details** page. This is the same page where you select the base model and a tuned model name.

> ## Evaluating tuned models
>
> - **Tuning and validation metrics**: Evaluate the tuned model using tuning and validation metrics after the tuning job completes.
> - **Integrated evaluation with Gen AI evaluation service** (Preview): Configure tuning jobs to automatically run evaluations using the Gen AI evaluation service during tuning. … **Supported interfaces**: Google Gen AI SDK and REST API. **Supported models**: `gemini-2.5-pro`, `gemini-2.5-flash`, and `gemini-2.5-flash-lite`.

> ## Quota
>
> Quota is enforced on the number of concurrent tuning jobs. Every project comes with a default quota to run at least one tuning job. This is a global quota, shared across all available regions and supported models. If you want to run more jobs concurrently, you need to request additional quota for `Global concurrent tuning jobs`.

> ## Pricing
>
> Pricing for Gemini supervised fine-tuning can be found here: Gemini Enterprise Agent Platform pricing.
>
> The number of training tokens is calculated by multiplying the number of tokens in your training dataset by the number of epochs. After tuning, inference (prediction request) costs for the tuned model still apply. Inference pricing is the same for each stable version of Gemini.
>
> If you configure the Gen AI evaluation service to run automatically during tuning, evaluations are charged as batch prediction jobs.
