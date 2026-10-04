---
source_file: zep-paper-2025/
source_type: web-capture
ingested_at: 2026-10-04
---

# Zep: A Temporal Knowledge Graph Architecture for Agent Memory (arXiv:2501.13956)

## Provenance
- Original location: research/web/zep-paper-2025/ (page.md; metadata.yaml; assets/)
- Format: html — arXiv **abstract page** only (not the full paper). page.md used as text input (7405 bytes, 14 headings).
- URL: https://arxiv.org/abs/2501.13956
- Fetched at: 2026-08-14T16:57:06Z (HTTP 200, 43012 bytes original.html)
- Author / source (if known): Preston Rasmussen, Pavlo Paliychuk, Travis Beauvais, Jack Ryan, Daniel Chalef. Subjects: cs.CL; cs.AI; cs.IR. Comments: "12 pages, 3 tables". DOI: https://doi.org/10.48550/arXiv.2501.13956. License icon: CC BY-NC-SA 4.0.
- Date of original (if known): submitted 20 Jan 2025 (v1, Mon, 20 Jan 2025 16:52:48 UTC, 22 KB). Only v1 listed at capture.

## Key claims
- Zep is "a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark."
- Existing RAG frameworks for LLM agents "are limited to static document retrieval", whereas "enterprise applications demand dynamic knowledge integration from diverse sources including ongoing conversations and business data."
- Core component **Graphiti**: "a temporally-aware knowledge graph engine that dynamically synthesizes both unstructured conversational data and structured business data while maintaining historical relationships."
- DMR (established by the MemGPT team as their primary metric): Zep 94.8% vs 93.4%.
- LongMemEval ("more challenging", complex temporal reasoning): "accuracy improvements of up to 18.5% while simultaneously reducing response latency by 90% compared to baseline implementations."
- Gains "particularly pronounced in enterprise-critical tasks such as cross-session information synthesis and long-term context maintenance."

## Definitions and terminology
- **Memory layer service**: Zep's self-description — a service providing memory to AI agents.
- **Graphiti**: Zep's temporally-aware knowledge graph engine.
- **Temporal knowledge graph**: knowledge graph that keeps historical relationships (time-aware facts).
- **DMR (Deep Memory Retrieval)**: benchmark established by the MemGPT team.
- **LongMemEval**: benchmark with complex temporal reasoning tasks.
- **MemGPT**: the prior state-of-the-art system Zep compares against.

## Evidence and examples
- DMR: 94.8% (Zep) vs 93.4% (MemGPT).
- LongMemEval: up to +18.5% accuracy, −90% response latency vs "baseline implementations".

## Inconsistencies / open questions
- [verified] Only the abstract was captured; per-task tables, baselines definitions and models are not in this record — checked page.md.
- [open question] "up to 18.5%" is a maximum over tasks/configurations and "baseline implementations" are unspecified in the abstract — the paper's tables would settle what the typical gain is and against what.
- [open question] DMR margin is 1.4 points (94.8 vs 93.4); the abstract does not report variance or significance — the full paper would settle whether the difference is meaningful.
- [open question] Results are reported by Zep's own team (vendor evaluation); Mem0's paper (`mem0-paper-2025.web.md`) is a competing vendor evaluation on LOCOMO. Neither capture establishes independent replication.

## Images / diagrams
Only arXiv page chrome was captured (no paper figures).

### zep-paper-2025.web/images/arxiv-logo-primary-light.svg
- Provenance: research/web/zep-paper-2025/assets/arxiv-logo-primary-light.svg ← arXiv static asset (alt "archive"). Site header logo.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### zep-paper-2025.web/images/by-nc-sa-4.0.png
- Provenance: research/web/zep-paper-2025/assets/by-nc-sa-4.0.png ← arXiv license icon (alt "license icon"); 80x15 PNG.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### zep-paper-2025.web/images/bibsonomy.png
- Provenance: research/web/zep-paper-2025/assets/bibsonomy.png ← arXiv static social icon (alt "BibSonomy"); 16x16 PNG.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### zep-paper-2025.web/images/reddit.png
- Provenance: research/web/zep-paper-2025/assets/reddit.png ← arXiv static social icon (alt "Reddit"); 18x18 PNG.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

## Raw / preserved excerpts

> Abstract: We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases. While existing retrieval-augmented generation (RAG) frameworks for large language model (LLM)-based agents are limited to static document retrieval, enterprise applications demand dynamic knowledge integration from diverse sources including ongoing conversations and business data. Zep addresses this fundamental limitation through its core component Graphiti -- a temporally-aware knowledge graph engine that dynamically synthesizes both unstructured conversational data and structured business data while maintaining historical relationships. In the DMR benchmark, which the MemGPT team established as their primary evaluation metric, Zep demonstrates superior performance (94.8% vs 93.4%). Beyond DMR, Zep's capabilities are further validated through the more challenging LongMemEval benchmark, which better reflects enterprise use cases through complex temporal reasoning tasks. In this evaluation, Zep achieves substantial results with accuracy improvements of up to 18.5% while simultaneously reducing response latency by 90% compared to baseline implementations. These results are particularly pronounced in enterprise-critical tasks such as cross-session information synthesis and long-term context maintenance, demonstrating Zep's effectiveness for deployment in real-world applications.

> Comments: 12 pages, 3 tables. Subjects: Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Information Retrieval (cs.IR). Cite as: arXiv:2501.13956 [cs.CL] (or arXiv:2501.13956v1 [cs.CL] for this version) https://doi.org/10.48550/arXiv.2501.13956
