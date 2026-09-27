---
source_file: openai-model-optimization/
source_type: web-capture
ingested_at: 2026-09-26
---

# Model optimization | OpenAI API

## Provenance
- Original location: research/web/openai-model-optimization/ (page.md used as text input; the first ~830 lines of page.md are site navigation, the article body starts at the `# Model optimization` heading and was extracted from there)
- Format: html (web capture via talksmith:ingest; page.md + original.html + metadata.yaml)
- URL: https://developers.openai.com/api/docs/guides/model-optimization
- Fetched at: 2026-09-26T22:38:09Z (HTTP 200, 374,692 bytes)
- Author / source (if known): OpenAI — official vendor documentation (OpenAI API docs, developers.openai.com). **Vendor documentation captured 2026-09-26; this surface changes fast — re-check before quoting as current.**
- Date of original (if known): not stated on the page. State as of capture 2026-09-26.
- Status of the page itself: the page says it "covers evals and fine-tuning workflows that are being moved into legacy documentation"; in the site navigation, the "Fine-tuning" group (Optimization cycle, Supervised fine-tuning, Vision fine-tuning, Direct preference optimization, Reinforcement fine-tuning, RFT use cases, Best practices) sits under the **"Legacy APIs"** section.

## Key claims
- **Official winding-down statement (verbatim, under "## Fine-tune a model"):** "OpenAI is winding down the fine-tuning platform. The platform is no longer accessible to new users, but existing users of the fine-tuning platform will be able to create training jobs for the coming months."
- **Inference of existing fine-tunes (verbatim):** "All fine-tuned models will remain available for inference until their base models are [deprecated](/api/docs/deprecations). The full timeline is [here](/api/docs/deprecations)."
- **Legacy status (verbatim):** "This guide covers evals and fine-tuning workflows that are being moved into legacy documentation. See the [deprecations page](/api/docs/deprecations) for the current timelines for the affected platform surfaces."
- The page lists four "fine-tuning methods supported in the OpenAI platform today", each with the exact model snapshots it can be used with ("Use with" column):
  - **Supervised fine-tuning (SFT):** `gpt-4.1-2025-04-14` `gpt-4.1-mini-2025-04-14` `gpt-4.1-nano-2025-04-14`
  - **Vision fine-tuning** (image inputs for SFT): `gpt-4o-2024-08-06`
  - **Direct preference optimization (DPO):** `gpt-4.1-2025-04-14` `gpt-4.1-mini-2025-04-14` `gpt-4.1-nano-2025-04-14`
  - **Reinforcement fine-tuning (RFT):** "**Reasoning models only**." — `o4-mini-2025-04-16`
- Fine-tuning process on the platform: dataset → upload "formatted in JSONL" → create a fine-tuning job with one of the methods → for RFT "define a grader to score the model's behavior" → evaluate. Jobs can be created in the dashboard (platform.openai.com/finetune) or via the API.
- Model optimization is framed as a flywheel of **evals + prompt engineering + fine-tuning** (six-step loop, see excerpts).
- Stated benefits of fine-tuning over prompting alone: more examples than fit in a context window; shorter prompts (lower token cost / latency); training on proprietary data without sending it every request; making "a smaller, cheaper, faster model" excel at a task.
- Prompting guidance on the same page recommends starting "with `gpt-6-astra` for new work" (the site nav also has "Using GPT-6"). Note the contrast: the current recommended model is not among the fine-tunable snapshots listed.

## Definitions and terminology
- **Supervised fine-tuning (SFT):** "Provide examples of correct responses to prompts to guide the model's behavior. Often uses human-generated 'ground truth' responses to show the model how it should respond."
- **Vision fine-tuning:** "Provide image inputs for supervised fine-tuning to improve the model's understanding of image inputs."
- **Direct preference optimization (DPO):** "Provide both a correct and incorrect example response for a prompt. Indicate the correct response to help the model perform better."
- **Reinforcement fine-tuning (RFT):** "Generate a response for a prompt, provide an expert grade for the result, and reinforce the model's chain-of-thought for higher-scored responses. Requires expert graders to agree on the ideal output from the model. Reasoning models only."
- **Few-shot learning:** giving "a few examples of correct output for a given prompt".
- **Graders:** the eval mechanism used to "measure the results of a prompt against your test data set" (also used by RFT).

## Evidence and examples
- "Best for" per method (from the methods table):
  - SFT: Classification; Nuanced translation; Generating content in a specific format; Correcting instruction-following failures.
  - Vision: Image classification; Correcting failures in instruction following for complex prompts.
  - DPO: Summarizing text, focusing on the right things; Generating chat messages with the right tone and style.
  - RFT: Complex domain-specific tasks that require advanced reasoning; Medical diagnoses based on history and diagnostic guidelines; Determining relevant passages from legal case law.
- "Learn from experts" section references videos titled "Cost/accuracy/latency", "Distillation", "Optimizing LLM Performance" (video content not captured).

## Inconsistencies / open questions
- [verified] The page is internally in transition: it still presents a table of "fine-tuning methods supported in the OpenAI platform today" while stating the platform is being wound down and closed to new users — checked both passages in page.md lines ~840–940 of the same capture. For the talk: the model list applies only to *existing* fine-tuning users as of 2026-09-26.
- [verified] The recommended model for new work on this same page (`gpt-6-astra`) is not in any fine-tunable list; the newest fine-tunable snapshots are `gpt-4.1-*-2025-04-14` and `o4-mini-2025-04-16` — checked against the methods table in the same capture.
- [open question] Version-sensitive: exact snapshot names, the "coming months" window for existing users, and deprecation dates. The page defers timelines to /api/docs/deprecations, which was **not** captured — capturing that page would settle when training jobs and inference of fine-tunes stop.
- [open question] The community thread (see `openai-finetuning-winding-down.web.md`) claims "o4-mini already has a shutoff date later in 2026"; this official page does not state it. Settle via the deprecations page.
- [open question] AWS Bedrock fine-tuning support could not be captured (JS-rendered docs), so no claim about Bedrock is sourced anywhere in this corpus batch.

## Images / diagrams
- `openai-model-optimization.web/images/blue_card.png` (512×512)
  - Provenance: card image on the page, alt "Evals", links to /api/docs/guides/evals; saved from https://cdn.openai.com/API/docs/images/blue_card.png
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `openai-model-optimization.web/images/orange_card.png` (512×512)
  - Provenance: card image, alt "Prompt engineering", links to the prompt-engineering guide; saved from https://cdn.openai.com/API/docs/images/orange_card.png
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- `openai-model-optimization.web/images/purple_card.png` (512×512)
  - Provenance: card image, alt "Fine-tuning", links to /api/docs/guides/supervised-fine-tuning; saved from https://cdn.openai.com/API/docs/images/purple_card.png
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->
- (Dropped per instruction, both dimensions < 300 px: `OpenAI_Developers.svg` site logo, 211×22.)

## Raw / preserved excerpts

> # Model optimization
>
> Ensure quality model outputs with evals and fine-tuning in the OpenAI platform.
>
> LLM output is non-deterministic, and model behavior changes between model snapshots and families. Developers must constantly measure and tune the performance of LLM applications to ensure they're getting the best results. In this guide, we explore the techniques and OpenAI platform tools you can use to ensure high quality outputs from the model.
>
> This guide covers evals and fine-tuning workflows that are being moved into legacy documentation. See the [deprecations page](/api/docs/deprecations) for the current timelines for the affected platform surfaces.

> ## Model optimization workflow
>
> Optimizing model output requires a combination of **evals**, **prompt engineering**, and **fine-tuning**, creating a flywheel of feedback that leads to better prompts and better training data for fine-tuning. The optimization process usually goes something like this.
>
> 1. Write evals that measure model output, establishing a baseline for performance and accuracy.
> 2. Prompt the model for output, providing relevant context data and instructions.
> 3. For some use cases, it may be desirable to fine-tune a model for a specific task.
> 4. Run evals using test data that is representative of real world inputs. Measure the performance of your prompt and fine-tuned model.
> 5. Tweak your prompt or fine-tuning dataset based on eval feedback.
> 6. Repeat the loop continuously to improve your model results.

> ## Build evals
>
> In the OpenAI platform, you can build and run evals either via API or in the dashboard. You might even consider writing evals *before* you start writing prompts, taking an approach akin to behavior-driven development (BDD).
>
> Run your evals against test inputs like you expect to see in production. Using one of several available graders, measure the results of a prompt against your test data set.

> ## Write effective prompts
>
> With evals in place, you can effectively iterate on prompts. The prompt engineering process may be all you need in order to get great results for your use case. Different models may require different prompting techniques, but there are several best practices you can apply across the board to get better results.
>
> - **Include relevant context** - in your instructions, include text or image content that the model will need to generate a response from outside its training data. This could include data from private databases or current, up-to-the-minute information.
> - **Provide clear instructions** - your prompt should contain clear goals about what kind of output you want. Start with [gpt-6-astra](/api/docs/models/gpt-6-astra) for new work, and use reasoning model guidance to tune outcome-level instructions, reasoning effort, and verbosity.
> - **Provide example outputs** - give the model a few examples of correct output for a given prompt (a process called few-shot learning). The model can extrapolate from these examples how it should respond for other prompts.

> ## Fine-tune a model
>
> OpenAI is winding down the fine-tuning platform. The platform is no longer accessible to new users, but existing users of the fine-tuning platform will be able to create training jobs for the coming months.
>
> All fine-tuned models will remain available for inference until their base models are [deprecated](/api/docs/deprecations). The full timeline is [here](/api/docs/deprecations).
>
> OpenAI models are already pre-trained to perform across a broad range of subjects and tasks. Fine-tuning lets you take an OpenAI base model, provide the kinds of inputs and outputs you expect in your application, and get a model that excels in the tasks you'll use it for.
>
> Fine-tuning can be a time-consuming process, but it can also enable a model to consistently format responses in a certain way or handle novel inputs. You can use fine-tuning with prompt engineering to realize a few more benefits over prompting alone:
>
> - You can provide more example inputs and outputs than could fit within the context window of a single request, enabling the model handle a wider variety of prompts.
> - You can use shorter prompts with fewer examples and context data, which saves on token costs at scale and can be lower latency.
> - You can train on proprietary or sensitive data without having to include it via examples in every request.
> - You can train a smaller, cheaper, faster model to excel at a particular task where a larger model is not cost-effective.
>
> Visit our pricing page to learn more about how fine-tuned model training and usage are billed.

> ### Fine-tuning methods
>
> These are the fine-tuning methods supported in the OpenAI platform today.
>
> | Method | How it works | Best for | Use with |
> |---|---|---|---|
> | Supervised fine-tuning (SFT) | Provide examples of correct responses to prompts to guide the model's behavior. Often uses human-generated "ground truth" responses to show the model how it should respond. | Classification; Nuanced translation; Generating content in a specific format; Correcting instruction-following failures | `gpt-4.1-2025-04-14` `gpt-4.1-mini-2025-04-14` `gpt-4.1-nano-2025-04-14` |
> | Vision fine-tuning | Provide image inputs for supervised fine-tuning to improve the model's understanding of image inputs. | Image classification; Correcting failures in instruction following for complex prompts | `gpt-4o-2024-08-06` |
> | Direct preference optimization (DPO) | Provide both a correct and incorrect example response for a prompt. Indicate the correct response to help the model perform better. | Summarizing text, focusing on the right things; Generating chat messages with the right tone and style | `gpt-4.1-2025-04-14` `gpt-4.1-mini-2025-04-14` `gpt-4.1-nano-2025-04-14` |
> | Reinforcement fine-tuning (RFT) | Generate a response for a prompt, provide an expert grade for the result, and reinforce the model's chain-of-thought for higher-scored responses. Requires expert graders to agree on the ideal output from the model. **Reasoning models only**. | Complex domain-specific tasks that require advanced reasoning; Medical diagnoses based on history and diagnostic guidelines; Determining relevant passages from legal case law | `o4-mini-2025-04-16` |

(Table re-assembled from the flattened page.md rendering; cell text is verbatim.)

> ### How fine-tuning works
>
> In the OpenAI platform, you can create fine-tuned models either in the dashboard or with the API. This is the general shape of the fine-tuning process:
>
> 1. Collect a dataset of examples to use as training data
> 2. Upload that dataset to OpenAI, formatted in JSONL
> 3. Create a fine-tuning job using one of the methods above, depending on your goals—this begins the fine-tuning training process
> 4. In the case of RFT, you'll also define a grader to score the model's behavior
> 5. Evaluate the results
>
> Get started with supervised fine-tuning, vision fine-tuning, direct preference optimization, or reinforcement fine-tuning.

> ## Learn from experts
>
> Model optimization is a complex topic, and sometimes more art than science. Check out the videos below from members of the OpenAI team on model optimization techniques.
>
> Cost/accuracy/latency · Distillation · Optimizing LLM Performance

Site navigation excerpt (shows where fine-tuning now lives):

> ### Legacy APIs
> - Agent Builder … - Evals (Getting started, Working with evals, Prompt optimizer, External models, Best practices, Graders)
> - Fine-tuning
>   - Optimization cycle · Supervised fine-tuning · Vision fine-tuning · Direct preference optimization · Reinforcement fine-tuning · RFT use cases · Best practices
> - Assistants API (Migration guide)
