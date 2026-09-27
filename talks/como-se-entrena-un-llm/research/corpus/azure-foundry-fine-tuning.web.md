---
source_file: azure-foundry-fine-tuning/
source_type: web-capture
ingested_at: 2026-09-26
---

# Customize a model with fine-tuning — Microsoft Foundry (Microsoft Learn)

## Provenance
- Original location: research/web/azure-foundry-fine-tuning/ (page.md used. It is 2,496 lines because the capture holds all four tab pivots of the article in sequence: **Foundry portal** (lines ~25–345), **OpenAI Python SDK** (~347–835), **Foundry SDK** (two language variants, ~836–2023), and **REST API** (~2024–2467). The "Supported models" table is identical across all four; checked by hashing the four table blocks.)
- Format: html (web capture via talksmith:ingest)
- URL: https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/fine-tuning
- Fetched at: 2026-09-26T22:38:18Z (HTTP 200, 242,015 bytes)
- Author / source (if known): Microsoft — official vendor documentation (Microsoft Learn; meta author `ssalgadodev` / `ssalgado`). **Vendor documentation captured 2026-09-26; model lists and regions change fast, so re-check before quoting as current.**
- Date of original (if known): `ms.date` 2026-07-30; `updated_at` 2026-09-01 (from original.html meta tags).

## Key claims
- **Supported models (verbatim table, "The following models are supported for fine-tuning:"):**

| Model ID | Standard regions | Data Zone | Global | Developer | Methods | Status | Modality |
|---|---|---|---|---|---|---|---|
| `gpt-4o-mini` (2024-07-18) | North Central US, Sweden Central | US | ✅ | ✅ | SFT | GA | Text to text |
| `gpt-4o` (2024-08-06) | East US2, North Central US, Sweden Central | US | ✅ | ✅ | SFT, DPO | GA | Text and vision to text |
| `gpt-4.1` (2025-04-14) | North Central US, Sweden Central | US | ✅ | ✅ | SFT, DPO | GA | Text and vision to text |
| `gpt-4.1-mini` (2025-04-14) | North Central US, Sweden Central | US | ✅ | ✅ | SFT, DPO | GA | Text to text |
| `gpt-4.1-nano` (2025-04-14) | North Central US, Sweden Central | US | ✅ | ✅ | SFT, DPO | GA | Text to text |
| `o4-mini` (2025-04-16) | East US2, Sweden Central | US | ✅ | ✅ | RFT | GA | Text to text |
| `gpt-5` (2025-08-07) | North Central US, Sweden Central | US | ✅ | ❌ | RFT | GA* | Text to text |
| `Ministral-3B` (2411) | Not supported | US | ✅ | ❌ | SFT | GA | Text to text |
| `Qwen-32B` | Not supported | US | ✅ | ❌ | SFT | GA | Text to text |
| `Llama-3.3-70B-Instruct` | Not supported | US | ✅ | ❌ | SFT | GA | Text to text |
| `gpt-oss-20b` | Not supported | US | ✅ | ❌ | SFT | GA | Text to text |

  (Reconstructed from the flattened page.md row text; cell values verbatim. See Inconsistencies for the column reading.)
  - "\* GPT-5 support for reinforcement fine-tuning is generally available, but access is gated and available by invitation only. Contact your Microsoft account team if you're interested in enrollment."
  - "Open-source models (Ministral-3B, Qwen-32B, Llama-3.3-70B-Instruct, gpt-oss-20b) are only supported on Foundry resources and in the new Foundry UI."
  - "For Azure OpenAI models, you can also fine-tune a previously fine-tuned model, formatted as `base-model.ft-{jobid}`."
- **Methods (customization method depends on the model):**
  - **SFT**: "Trains the model on labeled input/output pairs. Best for most scenarios, including task specialization."
  - **DPO**: "Aligns the model with human-preferred responses. Ideal for improving response quality."
  - **RFT**: "Uses reward signals from model graders to optimize complex behaviors."
  - The article covers SFT; DPO and RFT have separate guides (not captured).
- **Technique:** "We use low-rank adaptation (LoRA) to fine-tune models in a way that reduces their complexity without significantly affecting their performance. This method works by approximating the original high-rank matrix with a lower-rank one."
- **Training tiers ("Training type"), the compute-location distinction the page actually makes:**
  - **Standard**: training in the resource's region; "provides guarantees for data residency".
  - **Global**: "more affordable pricing compared to Standard by using capacity beyond your current region. Data and weights are copied to the region where training occurs."
  - **Developer**: "significant cost savings by using idle capacity for training. There are no latency or SLA guarantees, so jobs in this tier might be automatically preempted and resumed later. There are no guarantees for data residency either."
  - API values: `"trainingType": "Standard" | "GlobalStandard" | "developerTier"` (samples use `GlobalStandard`; the comments list "Standard" and "Developer" as the other options).
- **Serverless vs managed compute:** the page does **not** use the terms "serverless" or "managed compute" (grep over page.md found no match). The only compute distinctions it states are the three training tiers above and the note that open-source models are "only supported on Foundry resources and in the new Foundry UI".
- **Data format:** JSONL "in the conversational format that the Chat Completions API uses" (`messages` with system/user/assistant); UTF-8 **with a BOM**; each file < 512 MB. Multi-turn is supported; the optional per-assistant-message `"weight": 0|1` skips training on specific turns. Vision examples use `image_url` content parts.
- **Dataset size:** jobs need at least 10 examples; "best practice… hundreds, if not thousands"; "We recommend that you start with 50 well-crafted examples." "doubling the dataset size can lead to a linear increase in model quality."
- **OpenAI-only features:** automatic deployment, pause, and continuous fine-tuning are "supported only for OpenAI models".
- **Deployment cost:** "each customized (fine-tuned) model that's deployed incurs an hourly hosting cost regardless of whether chat completions or response API calls are made"; inactive deployments (no calls for 15 continuous days) are auto-deleted, while the model itself remains.
- **Roles:** Foundry Owner needed to deploy; "Foundry Users may train (fine-tune) models, only AI Owners may deploy them". The RBAC roles were renamed from "Azure AI User/Owner/…" to "Foundry User/Owner/…".

## Definitions and terminology
- **LoRA**: approximating "the original high-rank matrix with a lower-rank one"; fine-tunes "a smaller subset of important parameters during the supervised training phase".
- **Continuous fine-tuning**: "the iterative process of selecting an already fine-tuned model as a base model and fine-tuning it further on new sets of training examples." Model ID shape: `gpt-4.1-2025-04-14.ft-5fd1918ee65d4cd38a5dcf6835066ed7`.
- **Checkpoint**: generated at the end of each epoch; "a fully functional version of a model that can be both deployed and used as the target model for subsequent fine-tuning jobs"; the 3 most recent are deployable. ID format `ftchkpt-…`.
- **Hyperparameters**: `batch_size` (−1 = 0.2% of examples, max 256), `learning_rate_multiplier` (recommended 0.02–0.2), `n_epochs` (−1 = dynamic). The REST sample also shows `prompt_loss_weight`.
- **Metrics**: `train_loss`, `full_valid_loss`, `train_mean_token_accuracy`, `full_valid_mean_token_accuracy`.
- **Suffix**: up to 18 characters, used in the fine-tuned model name. **Seed**: controls reproducibility.
- **Copy a model (preview)**: copy a fine-tuned checkpoint across regions and subscriptions within the same tenant (API only).

## Evidence and examples
- Example SFT line (verbatim): `{"messages": [{"role": "system", "content": "Clippy is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "Who discovered Antarctica?"}, {"role": "assistant", "content": "Some chaps named Fabian Gottlieb von Bellingshausen and Mikhail Lazarev, as if they don't teach that in every school!"}]}` (10 such lines in the page).
- Multi-turn with weights (verbatim): `{"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What's the biggest city in France?"}, {"role": "assistant", "content": "Paris", "weight": 0}, {"role": "user", "content": "Can you be more sarcastic?"}, {"role": "assistant", "content": "Paris, as if everyone doesn't know that already.", "weight": 1}]}`
- Token-accuracy worked example: batch size 3, completions `[[1, 2], [0, 5], [4, 2]]`, prediction `[[1, 1], [0, 5], [4, 2]]` gives `0.83` (5 of 6).
- Python SDK workflow: prepare data, select base model, upload, train, check status, deploy, use, analyze.
- Developer-tier job (verbatim): `client.fine_tuning.jobs.create(model="gpt-4.1-mini", training_file="<FILE-ID>", extra_body={"trainingType": "developerTier"})`.
- Deployment uses the control-plane API (`management.azure.com …/deployments/…`, api-version 2024-10-01 / 2024-10-21) with `"sku": {"name": "standard", "capacity": 1}`; the Foundry SDK sample uses `sku: { name: "GlobalStandard", capacity: 1 }`.
- Pause/resume REST endpoints: `/openai/v1/fine_tuning/jobs/{id}/pause` and `/resume`.

## Inconsistencies / open questions
- [verified] Azure still offers fine-tuning of OpenAI models (gpt-4o-mini, gpt-4o, gpt-4.1 / -mini / -nano, o4-mini, gpt-5 RFT) while OpenAI's own platform is "winding down" fine-tuning and closed to new users (`openai-model-optimization.web.md`). Checked both captures. For the talk, this is the cloud route that still sells OpenAI fine-tuning as of 2026-09-26.
- [verified] Azure lists `gpt-5` (2025-08-07) for RFT (GA, invitation-only) and `gpt-4o-mini` for SFT. Neither appears in OpenAI's own methods table, which lists only gpt-4.1 family, gpt-4o-2024-08-06 (vision) and o4-mini-2025-04-16. Cross-checked the two records.
- [verified] The supported-models table is identical in all four pivots (portal / OpenAI SDK / Foundry SDK / REST). Checked by md5 over the four table blocks.
- [open question] Column reading of the flattened table: page.md gives each row as "<regions> US ✅ ✅/❌ <methods> …", which maps to Standard regions / Data Zone = "US" / Global / Developer by header order. The mapping is inferred from header order. Rendering the live page would settle it.
- [open question] The presenter asked about a serverless vs managed compute distinction. This page does not make one. Microsoft's separate "serverless API fine-tuning" / "managed compute" pages for non-OpenAI models were not captured, so no claim about that distinction is sourced.
- [open question] `Qwen-32B` is listed with no version or date, unlike every other row. Which Qwen release it is cannot be determined from this page.
- [open question] Version-sensitive: model roster, regions, GA status, and the gpt-5 RFT gating are as of `updated_at` 2026-09-01 and the 2026-09-26 capture.
- [open question] Inconsistent role wording: "only AI Owners may deploy them" versus the renamed "Foundry Owner". Stale wording from the in-progress RBAC rename the page itself mentions.
- [open question] AWS Bedrock fine-tuning support could not be captured (JS-rendered docs), so no claim about Bedrock is sourced in this batch.

## Images / diagrams
- None. The capture carried no image assets (metadata `assets: []`). Companion folder `azure-foundry-fine-tuning.web/images/` exists and is empty.

## Raw / preserved excerpts

> # Customize a model with fine-tuning
>
> Learn how to fine-tune models in Microsoft Foundry for your datasets and use cases. Fine-tuning enables:
>
> - Higher-quality results than what you can get just from prompt engineering.
> - The ability to train on more examples than what can fit into a model's request context limit.
> - Token savings due to shorter prompts.
> - Lower-latency requests, particularly when you're using smaller models.
>
> In contrast to few-shot learning, fine-tuning improves the model by training on more examples than what fits in a prompt. Because weights adapt to your task, you include fewer examples or instructions. Including less reduces tokens per call and potentially lowers cost and latency.
>
> We use low-rank adaptation (LoRA) to fine-tune models in a way that reduces their complexity without significantly affecting their performance. This method works by approximating the original high-rank matrix with a lower-rank one. Fine-tuning a smaller subset of important parameters during the supervised training phase makes the model more manageable and efficient. For users, it also makes training faster and more affordable than other techniques.

> ### Supported models (raw page.md rendering, preserved as captured)
>
> Model ID Standard regions Data Zone Global Developer Methods Status Modality `gpt-4o-mini` (2024-07-18) North Central US Sweden Central US ✅ ✅ SFT GA Text to text `gpt-4o` (2024-08-06) East US2 North Central US Sweden Central US ✅ ✅ SFT, DPO GA Text and vision to text `gpt-4.1` (2025-04-14) North Central US Sweden Central US ✅ ✅ SFT, DPO GA Text and vision to text `gpt-4.1-mini` (2025-04-14) North Central US Sweden Central US ✅ ✅ SFT, DPO GA Text to text `gpt-4.1-nano` (2025-04-14) North Central US Sweden Central US ✅ ✅ SFT, DPO GA Text to text `o4-mini` (2025-04-16) East US2 Sweden Central US ✅ ✅ RFT GA Text to text `gpt-5` (2025-08-07) North Central US Sweden Central US ✅ ❌ RFT GA* Text to text `Ministral-3B` (2411) Not supported US ✅ ❌ SFT GA Text to text `Qwen-32B` Not supported US ✅ ❌ SFT GA Text to text `Llama-3.3-70B-Instruct` Not supported US ✅ ❌ SFT GA Text to text `gpt-oss-20b` Not supported US ✅ ❌ SFT GA Text to text
>
> \* GPT-5 support for reinforcement fine-tuning is generally available, but access is gated and available by invitation only. Contact your Microsoft account team if you're interested in enrollment.
>
> For Azure OpenAI models, you can also fine-tune a previously fine-tuned model, formatted as `base-model.ft-{jobid}`.
>
> Note: Open-source models (Ministral-3B, Qwen-32B, Llama-3.3-70B-Instruct, gpt-oss-20b) are only supported on Foundry resources and in the new Foundry UI.

> ## Prepare your data
>
> Your training and validation datasets consist of input and output examples for how you want the model to perform.
>
> The training and validation data that you use *must* be formatted as a JSON Lines (JSONL) document. It must also be formatted in the conversational format that the Chat Completions API uses.
>
> In addition to the JSONL format, training and validation data files must be encoded in UTF-8 and include a byte-order mark (BOM). Each file must be less than 512 MB in size.
>
> We recommend that you use the instructions and prompts that you found worked best in every training example. This approach helps you get the best results, especially if you have fewer than a hundred examples.
>
> If you don't have an existing dataset prepared, you can use the data generation capabilities to create a new one.
>
> ### Multiple-turn chat file format
>
> Multiple turns of a conversation in a single line of your JSONL training file are also supported. To skip fine-tuning on specific assistant messages, add the optional `weight` key/value pair. Currently, `weight` can be set to `0` or `1`.
>
> ### Chat completions with vision
>
> `{"messages": [{"role": "user", "content": [{"type": "text", "text": "What's in this image?"}, {"type": "image_url", "image_url": {"url": "https://raw.githubusercontent.com/MicrosoftDocs/azure-ai-docs/main/articles/ai-services/openai/media/how-to/generated-seattle.png"}}]}, {"role": "assistant", "content": "The image appears to be a watercolor painting of a city skyline, featuring tall buildings and a recognizable structure often associated with Seattle, like the Space Needle. The artwork uses soft colors and brushstrokes to create a somewhat abstract and artistic representation of the cityscape."}]}`
>
> ### Dataset size considerations
>
> The more training examples you have, the better. Fine-tuning jobs won't proceed without at least 10 training examples, but such a small number isn't enough to noticeably influence model responses. A best practice for successful fine-tuning is to provide hundreds, if not thousands, of training examples. We recommend that you start with 50 well-crafted examples.
>
> In general, doubling the dataset size can lead to a linear increase in model quality. But keep in mind that low-quality examples can negatively affect performance. If you train the model on a large amount of internal data without first pruning the dataset for only the highest-quality examples, your model might perform worse than expected.

> ### Customization method
>
> The supported customization methods depend on the selected model:
>
> - **Supervised fine-tuning (SFT)**: Trains the model on labeled input/output pairs. Best for most scenarios, including task specialization.
> - **Direct preference optimization (DPO)**: Aligns the model with human-preferred responses. Ideal for improving response quality.
> - **Reinforcement fine-tuning (RFT)**: Uses reward signals from model graders to optimize complex behaviors.
>
> Note: The rest of this article covers steps for the SFT method. For instructions specific to other customization methods, see the guide for DPO and the guide for RFT.
>
> ### Training type
>
> Select the training tier based on your use case and budget:
>
> - **Standard**: Training occurs in the current Foundry resource's region and provides guarantees for data residency. Ideal for workloads where data must remain in a specific region.
> - **Global**: Provides more affordable pricing compared to Standard by using capacity beyond your current region. Data and weights are copied to the region where training occurs. Ideal if data residency is not a restriction and you want faster queue times.
> - **Developer**: Provides significant cost savings by using idle capacity for training. There are no latency or SLA guarantees, so jobs in this tier might be automatically preempted and resumed later. There are no guarantees for data residency either. Ideal for experimentation and price-sensitive workloads.

> #### Hyperparameters
>
> `batch_size` Integer: The batch size to use for training. The batch size is the number of training examples used to train a single forward and backward pass. In general, we find that larger batch sizes tend to work better for larger datasets. The default value and the maximum value for this property are specific to a base model. A larger batch size means that model parameters are updated less frequently, but with lower variance. When the value is set to `-1`, the batch size is calculated as 0.2% of examples in the training set. The maximum is `256`.
>
> `learning_rate_multiplier` Number: The learning rate multiplier to use for training. The fine-tuning learning rate is the original learning rate used for pre-training, multiplied by this value. Larger learning rates tend to perform better with larger batch sizes. We recommend experimenting with values in the range of `0.02` to `0.2` to see what produces the best results. A smaller learning rate can be useful to avoid overfitting.
>
> `n_epochs` Integer: The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset. If the value is set to `-1`, the number of epochs is determined dynamically based on the input data.
>
> #### Automatic deployment
>
> … Automatic deployment is supported only for OpenAI models.

> ### Metrics
>
> - `train_loss`: The loss for the training batch. Each training step on the x-axis represents a single pass, forward and backward, on a batch of training data.
> - `full_valid_loss`: The validation loss calculated at the end of each epoch. When training goes well, loss should decrease.
> - `train_mean_token_accuracy`: The percentage of tokens in the training batch that the model correctly predicted. For example, if the batch size is set to `3` and your data contains completions `[[1, 2], [0, 5], [4, 2]]`, this value is set to `0.83` (5 of 6) if the model predicted `[[1, 1], [0, 5], [4, 2]]`.
> - `full_valid_mean_token_accuracy`: The valid mean token accuracy calculated at the end of each epoch. When training is going well, token accuracy should increase.
>
> Look for your loss to decrease over time, and your accuracy to increase. If your training and validation data diverge, you might be overfitting. Try training with fewer epochs or a smaller learning-rate multiplier.
>
> ### Checkpoints
>
> When each training epoch finishes, a checkpoint is generated. … A checkpoint is a fully functional version of a model that can be both deployed and used as the target model for subsequent fine-tuning jobs. Checkpoints can be particularly useful, because they might provide snapshots prior to overfitting. When a fine-tuning job finishes, you have the three most recent versions of the model available to deploy. You can copy checkpoints between resources and subscriptions through the REST API.
>
> … The pause operation is applicable only for jobs that are trained for at least one step and are in a **Running** state. Pausing is supported only for OpenAI models.

> ## Use a deployed fine-tuned model
>
> … For chat models, the system message that you use to guide your fine-tuned model (whether it's deployed or available for testing in the playground) must be the same as the system message that you used for training. If you use a different system message, the model might not perform as expected.
>
> ## Perform continuous fine-tuning
>
> … Continuous fine-tuning is the iterative process of selecting an already fine-tuned model as a base model and fine-tuning it further on new sets of training examples. … A custom fine-tuned model looks like `gpt-4o-2024-08-06.ft-d93dda6110004b4da3472d96f4dd4777-ft`. Continuous fine-tuning is supported only for OpenAI models.

> ### Delete your fine-tuned model deployment
>
> After you deploy a customized model, if at any time the deployment remains inactive for more than 15 days, the deployment is deleted. The deployment of a customized model is *inactive* if the model was deployed more than 15 days ago and no chat completions or response API calls were made to it during a continuous 15-day period.
>
> The deletion of an inactive deployment doesn't delete or affect the underlying customized model. The customized model can be redeployed at any time.
>
> … each customized (fine-tuned) model that's deployed incurs an hourly hosting cost regardless of whether chat completions or response API calls are made to the model.

> ## Copy a model (preview)
>
> You can now copy a fine-tuned checkpointed model from one region to another, across different subscriptions but within the same tenant. The process uses dedicated APIs to help ensure efficient and secure transfers. This feature is currently available only with the API and not through the Foundry portal.
