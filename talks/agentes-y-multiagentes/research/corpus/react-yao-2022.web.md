---
source_file: react-yao-2022/
source_type: web-capture
ingested_at: 2026-10-04
---

# ReAct: Synergizing Reasoning and Acting in Language Models (arXiv:2210.03629)

## Provenance
- Original location: research/web/react-yao-2022/ (page.md; metadata.yaml; assets/)
- Format: html — arXiv **abstract page** only (not the full paper). page.md used as text input (7958 bytes, 15 headings).
- URL: https://arxiv.org/abs/2210.03629
- Fetched at: 2026-08-14T16:56:39Z (HTTP 200, 44231 bytes original.html)
- Author / source (if known): Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao. Subjects: cs.CL; cs.AI; cs.LG. Project site with code: https://react-lm.github.io. DOI: https://doi.org/10.48550/arXiv.2210.03629. License icon: CC BY 4.0.
- Date of original (if known): v1 submitted 6 Oct 2022 (Thu, 01:00:32 UTC, 538 KB); v2 27 Nov 2022 (538 KB); v3 10 Mar 2023 (1,256 KB) — "v3 is the ICLR camera ready version with some typos fixed."

## Key claims
- Reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) in LLMs "have primarily been studied as separate topics."
- ReAct uses LLMs "to generate both reasoning traces and task-specific actions in an interleaved manner".
- Synergy: "reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information."
- Effective over state-of-the-art baselines on diverse language and decision-making tasks, with "improved human interpretability and trustworthiness".
- On HotpotQA (question answering) and Fever (fact verification), ReAct "overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API".
- On ALFWorld and WebShop (interactive decision making), ReAct "outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples."

## Definitions and terminology
- **ReAct** (Reason + Act): prompting paradigm interleaving reasoning traces and actions.
- **Reasoning trace**: model-generated thought used to induce, track and update action plans.
- **Action**: task-specific step that interfaces with an external source (knowledge base, environment, API) and returns an observation.
- **Chain-of-thought (CoT)**: reasoning-only baseline.
- Benchmarks: **HotpotQA**, **Fever**, **ALFWorld**, **WebShop**.

## Evidence and examples
- Wikipedia API as the external source for HotpotQA/Fever.
- ALFWorld: +34 absolute success-rate points; WebShop: +10, vs imitation and RL methods, with 1–2 in-context examples.

## Inconsistencies / open questions
- [verified] Only the abstract was captured; the Thought/Action/Observation trajectory format and per-benchmark tables are not in this record — checked page.md. A slide describing the loop mechanics in detail needs the full paper.
- [verified] Folder name says 2022 (first submission, 6 Oct 2022); the camera-ready (v3) is dated 10 Mar 2023 and appeared at ICLR (year not stated on the page) — checked in submission history. Cite as Yao et al., 2022 (arXiv) / ICLR 2023 only after confirming the venue year.
- [open question] ReAct is a single-agent paradigm; its relevance to the talk is as the base agent loop that multi-agent systems compose — this is an editorial link, not a claim of the source.

## Images / diagrams
Only arXiv page chrome was captured (no paper figures).

### react-yao-2022.web/images/arxiv-logo-primary-light.svg
- Provenance: research/web/react-yao-2022/assets/arxiv-logo-primary-light.svg ← arXiv static asset (alt "archive"). Site header logo.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### react-yao-2022.web/images/by-4.0.png
- Provenance: research/web/react-yao-2022/assets/by-4.0.png ← arXiv license icon (alt "license icon"); 80x15 PNG.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### react-yao-2022.web/images/bibsonomy.png
- Provenance: research/web/react-yao-2022/assets/bibsonomy.png ← arXiv static social icon (alt "BibSonomy"); 16x16 PNG.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### react-yao-2022.web/images/reddit.png
- Provenance: research/web/react-yao-2022/assets/reddit.png ← arXiv static social icon (alt "Reddit"); 18x18 PNG.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

## Raw / preserved excerpts

> Abstract: While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples. Project site with code: https://react-lm.github.io

> Comments: v3 is the ICLR camera ready version with some typos fixed. Project site with code: https://react-lm.github.io. Subjects: Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG). Cite as: arXiv:2210.03629 [cs.CL] (or arXiv:2210.03629v3 [cs.CL] for this version) https://doi.org/10.48550/arXiv.2210.03629
