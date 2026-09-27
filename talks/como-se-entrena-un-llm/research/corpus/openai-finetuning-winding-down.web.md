---
source_file: openai-finetuning-winding-down/
source_type: web-capture
ingested_at: 2026-09-26
---

# OpenAI is winding down the fine-tuning API and platform — Discussion Thread (OpenAI Developer Community)

## Provenance
- Original location: research/web/openai-finetuning-winding-down/ (page.md used; cross-checked against the JSON-LD in original.html)
- Format: html (web capture via talksmith:ingest)
- URL: https://community.openai.com/t/openai-is-winding-down-the-fine-tuning-api-and-platform-discussion-thread/1380522
- Fetched at: 2026-09-26T22:38:11Z (HTTP 200)
- Author / source (if known): **Community forum thread — user posts, NOT official OpenAI documentation.** Posters: `itsarnavsalkade` (thread opener), `_j`, `aprendendo.next`. Category: API › Deprecations. Hosted on community.openai.com (Discourse). Treat as **secondary** evidence; the official statement lives in `openai-model-optimization.web.md`. Captured 2026-09-26 as part of a vendor/tool documentation sweep; this topic changes fast.
- Date of original (if known): thread opened **May 8, 2026, 5:10pm** (JSON-LD `datePublished` 2026-05-08T17:10:37Z); replies at 5:29pm and 6:53pm the same day.
- Capture scope: only the 3 posts rendered for no-JS crawlers were captured (JSON-LD `answerCount: 2`); any later replies are not in this record.

## Key claims
(All are user statements, not OpenAI statements.)
- Opener (`itsarnavsalkade`): "For SFT only gpt4.1 variants are available and for RL only o4-mini is available so if im not wrong the degree of freedom to test and fine tune is anyway limited." — consistent with the official methods table.
- Opener asks whether fine-tuned models on gpt-4.1-mini become unusable for inference once the base model is deprecated.
- `_j`: "o4-mini already has a shutoff date later in 2026. That was the first sign that fine-tuning was doomed."
- `_j`: "gpt-4.1 series has not appeared in the deprecation list with a shutoff date. I anticipate you will have six months of deprecation notice before shutoff, and like the notice says, model shutoff is fine-tuning model shutoff when based on that model."
- `_j`: "OpenAI pricing has not become cheaper for API developers with new release models in 2026, instead, huge hikes." (opinion)
- `aprendendo.next`: "It seems they have given up on ft for now, at least until we get some Stargates up and running with some gpu power to spare…" (opinion; attaches a screenshot).

## Definitions and terminology
- "ft" = fine-tuning. "SFT" = supervised fine-tuning; "RL" here = reinforcement fine-tuning (RFT).
- Fine-tuned model naming: "you specify the job-generated name with your prefix after it is created" (`_j`).

## Evidence and examples
- Related topics listed on the page (titles + last activity), which show the timeline of community concern:
  - "With gpt-4o being deprecated - what does that mean for gpt-4o fine tunes?" — February 16, 2026
  - "Deprecation of fine tuned models, but still can't access newer ones?" — April 22, 2026
  - "What will happen to the fine tuned projects on Open AI portal" — May 9, 2026
  - "OpenAI's self-serve fine-tuning availability" — May 8, 2026
  - "GPT3 Model deprecation question" — July 31, 2023

## Inconsistencies / open questions
- [verified] This is user-generated content, not an official source — checked: posts are by forum users, category Deprecations, no OpenAI staff post in the capture. Cite only as "community reaction", never as the source of the winding-down fact; use `openai-model-optimization.web.md` for the verbatim official statement.
- [verified] The opener's model constraint ("SFT only gpt4.1 variants", "RL only o4-mini") matches the official methods table in `openai-model-optimization.web.md` (SFT/DPO: gpt-4.1 / -mini / -nano 2025-04-14; RFT: o4-mini-2025-04-16) — cross-checked the two records.
- [open question] "o4-mini already has a shutoff date later in 2026" and the "six months of deprecation notice" expectation are unverified user claims; the official deprecations page (not captured) would settle them. Version-sensitive.
- [open question] The thread title says "winding down the fine-tuning API and platform" (dated May 8, 2026), implying the official announcement was around that date; the official page captured 2026-09-26 carries no date. Settle via OpenAI's changelog / deprecations page.
- [open question] The attached screenshot (`240c8016….png`) may reproduce the official notice; not transcribed in Phase 1.
- [open question] AWS Bedrock fine-tuning support could not be captured (JS-rendered docs), so no claim about Bedrock is sourced in this batch.

## Images / diagrams
- `openai-finetuning-winding-down.web/images/240c8016d7f41d5b36f0f6be0cef71c26ee0cdad.png` (893×370, 25.7 KB)
  - Provenance: image attached to post #3 by `aprendendo.next` (May 8, 2026, 6:53pm), alt "image"; saved from https://us1.discourse-cdn.com/openai1/original/4X/2/4/0/240c8016d7f41d5b36f0f6be0cef71c26ee0cdad.png
  - Depiction:
  - Why it matters:
  - Transcribed text:
  <!-- pending: process_images -->

## Raw / preserved excerpts

> **itsarnavsalkade** — May 8, 2026, 5:10pm (#1)
>
> So if i have fine tuned models on gpt4.1 mini and openai deprecates it does this mean my model will never be used for inference? So i would have wasted money and compute on it? For SFT only gpt4.1 variants are available and for RL only o4-mini is available so if im not wrong the degree of freedom to test and fine tune is anyway limited.
>
> Also if GPT5.5 onwards models will be good at instruction following what would developers do with the money they have on the API Platform? As inference costs get cheaper and cheaper due to data center expansions and demands continue to increase will all inference be done using the same models released by OpenAI?

> **_j** — May 8, 2026, 5:29pm (#2)
>
> o4-mini already has a shutoff date later in 2026. That was the first sign that fine-tuning was doomed.
>
> gpt-4.1 series has not appeared in the deprecation list with a shutoff date. I anticipate you will have six months of deprecation notice before shutoff, and like the notice says, model shutoff is fine-tuning model shutoff when based on that model.
>
> You choose which model you use on the API. You run a particular model name you have trained by API specification. To use a fine tuning trained model for inference generation, you specify the job-generated name with your prefix after it is created. Until it is turned off by OpenAI or you delete it.
>
> OpenAI pricing has not become cheaper for API developers with new release models in 2026, instead, huge hikes. For now, there is a wide variety of models to run an API call against, as long as you accept that there is no aspect of machine learning experimentation and nothing emergent, novel, inspirational, educational to come out of these boring consumer products again.

> **aprendendo.next** — May 8, 2026, 6:53pm (#3)
>
> It seems they have given up on ft for now, at least until we get some Stargates up and running with some gpu power to spare…
>
> [image 893×370 25.7 KB]
