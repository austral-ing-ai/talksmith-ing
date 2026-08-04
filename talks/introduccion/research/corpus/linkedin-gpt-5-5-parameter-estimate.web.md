---
source_file: linkedin-gpt-5-5-parameter-estimate
source_type: web-capture
ingested_at: 2026-08-04
---

# GPT-5.5 Size Estimated at 9.7 Trillion Parameters — LinkedIn post by Kirill A. B.

## Provenance

- Original location: research/web/linkedin-gpt-5-5-parameter-estimate/
- Format: captured LinkedIn HTML
- Author / source (if known): Kirill A. B.
- Date of original (if known): approximately May 2026 (shown as “3mo” at capture)

## Key claims

- The post summarizes the IKP paper and presents estimates of effective parameter capacity for closed models: GPT-5.5 ≈ 9.7T, Claude Opus 4.6 ≈ 5.3T, Claude Sonnet 4.6 ≈ 1.7T and Gemini 2.5 Pro ≈ 1.2T.
- It describes the method as a calibration from factual recall on 1,400 obscure-fact questions to parameter count across open models.
- The post itself notes uncertainty from tool use and external retrieval; visible discussion points out the estimates’ wide uncertainty interval.
- A comment by the author links the primary paper: https://arxiv.org/abs/2604.24827.

## Definitions and terminology

- IKP: Incompressible Knowledge Probes, a factual-recall benchmark used to infer an order-of-magnitude estimate of model capacity.
- Parameter estimate: an inferred lower bound / effective knowledge-capacity estimate, not an architecture disclosure by the model provider.

## Evidence and examples

- Visible discussion cites a nominal 90% prediction interval for the GPT-5.5 estimate from 3.2T to 28.7T, illustrating why the central figure must not be read as a confirmed count.
- The primary source is preserved separately as `arxiv-2604-24827-ikp.web.md`.

## Inconsistencies / open questions

- This is a secondary LinkedIn interpretation rather than the paper itself.
- The post’s headline point estimates can be over-interpreted; the visible comments raise calibration, model-release-date, refusals, retrieval and MoE-active-parameter concerns.
- The captured asset is a LinkedIn profile background, not a figure from the paper.

## Images / diagrams

- `linkedin-gpt-5-5-parameter-estimate.web/images/1780425055361.bin`
  - Provenance: LinkedIn profile background fetched with the page.
  - <!-- pending: process_images -->

## Raw / preserved excerpts

The post says that a paper on IKP estimates closed-model capacity from factual knowledge and describes a log-linear calibration trained on open models. It lists GPT-5.5 at approximately 9.7 trillion parameters and directs readers to arXiv:2604.24827 for the full paper. The captured `original.html` and `page.md` preserve the complete post and visible discussion.
