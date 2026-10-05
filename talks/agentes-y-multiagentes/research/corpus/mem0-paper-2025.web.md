---
source_file: mem0-paper-2025/
source_type: web-capture
ingested_at: 2026-10-04
---

# Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory (arXiv:2504.19413)

## Provenance
- Original location: research/web/mem0-paper-2025/ (page.md; metadata.yaml; assets/)
- Format: html — arXiv **abstract page** only (not the full paper). page.md used as text input (7608 bytes, 14 headings).
- URL: https://arxiv.org/abs/2504.19413
- Fetched at: 2026-08-14T16:57:06Z (HTTP 200, 43569 bytes original.html)
- Author / source (if known): Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, Deshraj Yadav. Subjects: cs.CL; cs.AI. DOI: https://doi.org/10.48550/arXiv.2504.19413. License: arXiv non-exclusive distribution 1.0.
- Date of original (if known): submitted 28 Apr 2025 (v1, Mon, 28 Apr 2025 01:46:35 UTC, 946 KB). Only v1 listed at capture.

## Key claims
- Problem: LLMs' "fixed context windows pose fundamental challenges for maintaining consistency over prolonged multi-session dialogues."
- Mem0 is "a scalable memory-centric architecture" that dynamically **extracts, consolidates, and retrieves** salient information from ongoing conversations.
- An enhanced variant uses **graph-based memory representations** to capture relational structure among conversational elements (Mem0 with graph memory; often written Mem0^g in the paper — not on this page).
- Evaluated on the **LOCOMO** benchmark against six baseline categories: (i) established memory-augmented systems, (ii) RAG with varying chunk sizes and k-values, (iii) full-context (entire conversation history), (iv) an open-source memory solution, (v) a proprietary model system, (vi) a dedicated memory management platform.
- "our methods consistently outperform all existing memory systems across four question categories: single-hop, temporal, multi-hop, and open-domain."
- "Mem0 achieves 26% relative improvements in the LLM-as-a-Judge metric over OpenAI"; graph variant "around 2% higher overall score than the base configuration".
- Versus full-context: "91% lower p95 latency" and "saves more than 90% token cost".
- Conclusion: structured, persistent memory is critical for long-term conversational coherence.

## Definitions and terminology
- **Long-term memory** (for agents): persistent store of salient facts extracted from conversations across sessions.
- **Extract / consolidate / retrieve**: Mem0's three memory operations as named in the abstract.
- **Graph memory**: graph-based representation of conversational elements and their relations.
- **Full-context approach**: baseline feeding the entire conversation history to the model.
- **LOCOMO**: benchmark of long multi-session conversations used for evaluation.
- **LLM-as-a-Judge**: evaluation metric using an LLM to grade answers.
- **p95 latency**: 95th-percentile latency.

## Evidence and examples
- Headline numbers (abstract only): +26% relative LLM-as-a-Judge vs "OpenAI"; graph variant ~+2% overall over base; −91% p95 latency and >90% token-cost savings vs full-context.

## Inconsistencies / open questions
- [verified] Only the abstract was captured; tables, the exact baselines, absolute scores, and model versions are not in this record — checked page.md (no full-text content). Claims beyond the abstract need the PDF/HTML version.
- [open question] "26% relative improvements ... over OpenAI" does not say which OpenAI system (the abstract's baseline category "(v) a proprietary model system" suggests ChatGPT's memory feature, but this capture does not confirm it) — the paper's results table would settle it.
- [open question] Results are reported by the Mem0 authors (who build the product); independent replication is not established by this source. The Zep paper record (`zep-paper-2025.web.md`) is a competing vendor's evaluation on related benchmarks.
- [open question] "consistently outperform all existing memory systems" is a strong claim scoped to LOCOMO and the chosen baselines — the full paper would show per-category margins.

## Images / diagrams
Only arXiv page chrome was captured (no paper figures).

### mem0-paper-2025.web/images/arxiv-logo-primary-light.svg
- Provenance: research/web/mem0-paper-2025/assets/arxiv-logo-primary-light.svg ← arXiv static asset (alt "archive"). Site header logo.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### mem0-paper-2025.web/images/bibsonomy.png
- Provenance: research/web/mem0-paper-2025/assets/bibsonomy.png ← arXiv static social icon (alt "BibSonomy"); 16x16 PNG. Bookmark button.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### mem0-paper-2025.web/images/reddit.png
- Provenance: research/web/mem0-paper-2025/assets/reddit.png ← arXiv static social icon (alt "Reddit"); 18x18 PNG. Bookmark button.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

## Raw / preserved excerpts

> Abstract: Large Language Models (LLMs) have demonstrated remarkable prowess in generating contextually coherent responses, yet their fixed context windows pose fundamental challenges for maintaining consistency over prolonged multi-session dialogues. We introduce Mem0, a scalable memory-centric architecture that addresses this issue by dynamically extracting, consolidating, and retrieving salient information from ongoing conversations. Building on this foundation, we further propose an enhanced variant that leverages graph-based memory representations to capture complex relational structures among conversational elements. Through comprehensive evaluations on LOCOMO benchmark, we systematically compare our approaches against six baseline categories: (i) established memory-augmented systems, (ii) retrieval-augmented generation (RAG) with varying chunk sizes and k-values, (iii) a full-context approach that processes the entire conversation history, (iv) an open-source memory solution, (v) a proprietary model system, and (vi) a dedicated memory management platform. Empirical results show that our methods consistently outperform all existing memory systems across four question categories: single-hop, temporal, multi-hop, and open-domain. Notably, Mem0 achieves 26% relative improvements in the LLM-as-a-Judge metric over OpenAI, while Mem0 with graph memory achieves around 2% higher overall score than the base configuration. Beyond accuracy gains, we also markedly reduce computational overhead compared to full-context method. In particular, Mem0 attains a 91% lower p95 latency and saves more than 90% token cost, offering a compelling balance between advanced reasoning capabilities and practical deployment constraints. Our findings highlight critical role of structured, persistent memory mechanisms for long-term conversational coherence, paving the way for more reliable and efficient LLM-driven AI agents.

> Cite as: arXiv:2504.19413 [cs.CL] (or arXiv:2504.19413v1 [cs.CL] for this version) https://doi.org/10.48550/arXiv.2504.19413
