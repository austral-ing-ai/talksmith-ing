---
source_file: langchain-react-agent-template/
source_type: web-capture
ingested_at: 2026-10-04
---

# LangGraph ReAct Agent Template (GitHub README, langchain-ai/react-agent)

> **Librarian scope note — why this source is in the corpus.** This README is a clean, first-party example of the **loose, modern sense of "ReAct agent"**: a chat model with a system prompt (`prompts.py`) and a set of Python-function tools (Tavily search), run in a reason → act → observe loop built as a LangGraph graph. It cites the ReAct paper (arXiv 2210.03629) as what it implements, but nothing in the README involves the paper's **strict** mechanics: a completion model, a single few-shot text prompt, and a literal `Thought i: / Action i: / Observation i:` text format cut by a stop sequence (see `react-repo-hotpotqa-prompt.md.md` and `yao-2022-react.pdf.md`). Put side by side, the two records show the label "ReAct" drifting from a specific prompting format (2022) to "any tool-calling agent loop" (2024+). See *Definitions and terminology* and *Inconsistencies / open questions*.

## Provenance
- Original location: `research/web/langchain-react-agent-template/`. Text input was `page.md` (11,578 bytes, has headings, so no fallback to `original.html`). Lines 1–27 of `page.md` are GitHub page chrome (navigation, sign-in, fork and star counts, file listing). The README runs from line 28 (`# LangGraph ReAct Agent Template`) to the Footnotes at line 142. Lines 144–190 are the repo sidebar (About, Topics, Stars, …).
- Format: html (web capture via `talksmith:ingest`)
- **Cite as (canonical URL):** https://github.com/langchain-ai/react-agent
- Fetched: 2026-10-04T21:55:00Z (HTTP 200). `metadata.yaml` was written by the orchestrator, not by `fetch.py`: the fetcher crashed (`OSError: File name too long`) while saving a shields.io/camo badge asset, after it had already written `page.md` and `original.html`. Only one asset, `badge.svg` (the CI badge), was saved.
- Author / source (if known): LangChain, Inc. (GitHub org `langchain-ai`), repo `langchain-ai/react-agent`, marked "Public template". Repo description: "LangGraph template for a simple ReAct agent". License: MIT. At capture: 852 stars, 8 watching, 698 forks, 99 commits on `main`. Topics: `langgraph`, `langgraph-python`, `langgraph-template`.
- Date of original (if known): not shown in the capture (no commit date was rendered). The README names `claude-sonnet-4-5-20250929` as the default model, so this revision is from late September 2025 or later.
- Related records in this corpus: `react-repo-hotpotqa-prompt.md.md` (the paper's actual prompt and loop, i.e. the strict sense), `yao-2022-react.pdf.md` (the paper), `react-yao-2022.web.md` (arXiv abstract page), `medium-react-langgraph-agent.web.md` (another LangGraph "ReAct" walkthrough), `langgraph-doc.web.md`.

## Key claims
- The template "showcases a [ReAct agent](https://arxiv.org/abs/2210.03629) implemented using [LangGraph](https://github.com/langchain-ai/langgraph), designed for [LangGraph Studio](https://github.com/langchain-ai/langgraph-studio)." The link on "ReAct agent" goes to the ReAct paper, arXiv **2210.03629**, which is the README's only stated source for what it implements.
- "ReAct agents are uncomplicated, prototypical agents that can be flexibly extended to many tools."
- The core logic is in `src/react_agent/graph.py` and "demonstrates a flexible ReAct agent that iteratively reasons about user queries and executes actions".
- **What "the ReAct agent" does** (verbatim, *What it does*). It has five numbered items, and steps 2–4 form the loop:
  1. Takes a user **query** as input
  2. Reasons about the query and decides on an action
  3. Executes the chosen action using available tools
  4. Observes the result of the action
  5. Repeats steps 2-4 until it can provide a final answer
- "By default, it's set up with a basic set of tools, but can be easily extended with custom tools to suit various use cases."
- **Tool:** "The primary [search tool](…/src/react_agent/tools.py) used is [Tavily](https://tavily.com/)." Tools "can be any Python functions that perform specific tasks" and are added in `tools.py`.
- **System prompt:** "We provide a default system prompt in [prompts.py](…/src/react_agent/prompts.py). You can easily update this via context in the studio." The *Development* section also says to try "updating the default system message in `src/react_agent/context.py` to take on a persona".
- **Model:** default is `model: claude-sonnet-4-5-20250929`. Anthropic and OpenAI chat models are supported; you pick another with `provider/model-name` via runtime context (example: `openai/gpt-4-turbo-preview`).
- **Extending it:** you can modify "the agent's reasoning process in graph.py" and adjust "the ReAct loop or adding additional steps to the agent's decision-making process". Development tips: "adding an interrupt before the agent calls tools", "adding additional nodes and edges".
- Studio features: edit past state and rerun from it, hot reload, follow-up requests appended to the same thread, `+` to start a new thread, LangSmith integration for tracing.

## Definitions and terminology
- **ReAct agent (as this README uses the term)** — an agent that loops reason → choose action → run tool → observe until it can answer, built on a **chat model** with a **system prompt** and a set of **tools** (Python functions). This is the loose, modern sense. The README describes no Thought/Action/Observation text format, no few-shot exemplars, and no stop-sequence parsing.
- **ReAct (strict, paper sense)** — for contrast, from `react-repo-hotpotqa-prompt.md.md`: there is no system prompt. A completion model gets one text made of an instruction, six few-shot trajectories, and the question, and it generates `Thought i:` / `Action i:` lines. A stop sequence cuts it at `\nObservation i:`, and the harness writes the real observation into the text. The README links this paper but does not use its mechanics.
- **The ReAct loop** — the README's phrase for steps 2–4 above. In LangGraph it is a graph (`graph.py`), not a prompt format.
- **LangGraph / LangGraph Studio** — LangChain's graph-based agent framework, and its visual IDE/debugger (graph view, state editing, threads).
- **Runtime context** — LangGraph mechanism used here to switch the model (`provider/model-name`) and the system prompt without changing code.
- **Tavily** — web-search API, the template's default tool. Needs a Tavily API key in `.env`.
- Footnote 1 (on "search tool"): https://python.langchain.com/docs/concepts/#tools.

## Evidence and examples
- Setup: `cp .env.example .env`, then put API keys in `.env` (`ANTHROPIC_API_KEY=…` or `OPENAI_API_KEY=…`, plus a Tavily key).
- Default model string: `claude-sonnet-4-5-20250929`. Example alternative: `openai/gpt-4-turbo-preview`.
- Repo layout (from the GitHub file listing in the chrome): `.github/`, `src/react_agent/`, `static/`, `tests/`, `.codespellignore`, `.env.example`, `.gitignore`, `LICENSE`, `Makefile`, `README.md`, `langgraph.json`, `pyproject.toml`, `uv.lock`. Files named in the README: `src/react_agent/graph.py`, `tools.py`, `prompts.py`, `context.py`.
- Figure: "Graph view in LangGraph studio UI" (`static/studio_ui.png`), see *Images / diagrams*.
- Popularity signal at capture: 852 stars, 698 forks. It is an official LangChain template, so it reflects how the framework vendor itself uses "ReAct agent".

## Inconsistencies / open questions
- [verified] The README contradicts itself on the default model. *Setup Model* says "The defaults values for `model` are shown below: `model: claude-sonnet-4-5-20250929`", while *How to customize* says "We default to Anthropic's Claude 3 Sonnet." — checked by reading both passages in `page.md` (lines 74–77 and 118). The second line is most likely left over from an older revision. If a slide quotes the default model, use the *Setup Model* value.
- [verified] The README names two places for the default system prompt: "a default system prompt in prompts.py" (*How to customize*) and "updating the default system message in `src/react_agent/context.py`" (*Development*) — checked by reading both passages in `page.md` (lines 119 and 130). The two may be compatible (context.py could load the prompts.py text as a default) but the README doesn't say. Cite `prompts.py` as where the prompt text lives.
- [open question] Does the template run its loop through **native tool calling** (`bind_tools` / `tool_calls` on chat messages) rather than a parsed Thought/Action text format? The README strongly suggests it (chat models only, tools as plain Python functions, "an interrupt before the agent calls tools", a graph rather than a prompt format) but never says so. Ingesting `src/react_agent/graph.py` and `prompts.py` would settle it, and would also give the actual system-prompt text. Until then, "loose sense = native tool calling in a loop" is an inference supported by the README, not a direct quote.
- [open question] The README attributes its design to the ReAct paper (link to arXiv 2210.03629) but describes none of the paper's specific mechanics (interleaved free-text Thought, few-shot trajectories, completion model, stop sequence). This is evidence of how the term has widened, not an error in the README. Whether to present it as "drift" or as "a legitimate generalization" is the presenter's call. Compare `react-repo-hotpotqa-prompt.md.md`.
- [open question] Revision date unknown: the capture shows no commit date. The `claude-sonnet-4-5-20250929` default dates it to late September 2025 or later. The repo commit history would settle it.
- Extraction gap (not a content defect): `fetch.py` crashed before saving the README's figure. The librarian fetched `static/studio_ui.png` separately for the companion folder (see below). The "Open in LangGraph Studio" camo/shields badge was never saved; it is site chrome.

## Images / diagrams

### `langchain-react-agent-template.web/images/studio_ui.png`
- Provenance: README figure, alt text "Graph view in LangGraph studio UI", referenced in `page.md` line 36 as `/langchain-ai/react-agent/raw/main/static/studio_ui.png`. `talksmith:ingest` did **not** save it (the fetcher crashed first). The librarian downloaded it on 2026-10-04 from https://github.com/langchain-ai/react-agent/raw/main/static/studio_ui.png (HTTP 200, PNG 3248×2112, 581,539 bytes, sha1 `c071ea38624d335ad2961261d9bc2d9a57f778c8`). Content figure, likely the template's graph (the ReAct loop as nodes/edges) in Studio.
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `langchain-react-agent-template.web/images/badge.svg`
- Provenance: `research/web/langchain-react-agent-template/assets/badge.svg`, the GitHub Actions "CI - passing" badge (`<title>CI - passing</title>`, 90×20) from the README header (`page.md` line 32). Site chrome, no content value; copied so no image is left only in the raw asset folder.
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

## Raw / preserved excerpts

README, verbatim from `page.md` lines 28–142. GitHub's heading-anchor lines (`<#…>`) were dropped. On the badge line, the very long camo URL of the "Open in LangGraph Studio" shields badge (about 2,500 hex characters) is replaced by `[camo badge URL elided — site chrome; full string in research/web/langchain-react-agent-template/page.md line 32]`. Everything else is unchanged, including the original's markdown quirks (step numbering restarting at "1.").

````markdown
# LangGraph ReAct Agent Template

![CI](https://github.com/langchain-ai/react-agent/actions/workflows/unit-tests.yml/badge.svg)<https://github.com/langchain-ai/react-agent/actions/workflows/unit-tests.yml> ![Open in - LangGraph Studio]([camo badge URL elided — site chrome; full string in research/web/langchain-react-agent-template/page.md line 32])<https://langgraph-studio.vercel.app/templates/open?githubUrl=https://github.com/langchain-ai/react-agent>

This template showcases a [ReAct agent](https://arxiv.org/abs/2210.03629) implemented using [LangGraph](https://github.com/langchain-ai/langgraph), designed for [LangGraph Studio](https://github.com/langchain-ai/langgraph-studio). ReAct agents are uncomplicated, prototypical agents that can be flexibly extended to many tools.

![Graph view in LangGraph studio UI](/langchain-ai/react-agent/raw/main/static/studio_ui.png)</langchain-ai/react-agent/blob/main/static/studio_ui.png>

The core logic, defined in `src/react_agent/graph.py`, demonstrates a flexible ReAct agent that iteratively reasons about user queries and executes actions, showcasing the power of this approach for complex problem-solving tasks.

## What it does

The ReAct agent:

1. Takes a user **query** as input 
2. Reasons about the query and decides on an action 
3. Executes the chosen action using available tools 
4. Observes the result of the action 
5. Repeats steps 2-4 until it can provide a final answer 

By default, it's set up with a basic set of tools, but can be easily extended with custom tools to suit various use cases.

## Getting Started

Assuming you have already [installed LangGraph Studio](https://github.com/langchain-ai/langgraph-studio?tab=readme-ov-file#download), to set up:

1. Create a `.env` file. 

```
cp .env.example .env
```

1. Define required API keys in your `.env` file. 

The primary [search tool](/langchain-ai/react-agent/blob/main/src/react_agent/tools.py) [1](#user-content-fn-1-6d0d082f21aabeeb05928084ca8d819d) used is [Tavily](https://tavily.com/). Create an API key [here](https://app.tavily.com/sign-in).

### Setup Model

The defaults values for `model` are shown below:

```
model: claude-sonnet-4-5-20250929
```

Follow the instructions below to get set up, or pick one of the additional options.

#### Anthropic

To use Anthropic's chat models:

1. Sign up for an [Anthropic API key](https://console.anthropic.com/) if you haven't already. 
2. Once you have your API key, add it to your `.env` file: 

```
ANTHROPIC_API_KEY=your-api-key
```

#### OpenAI

To use OpenAI's chat models:

1. Sign up for an [OpenAI API key](https://platform.openai.com/signup). 
2. Once you have your API key, add it to your `.env` file: 

```
OPENAI_API_KEY=your-api-key
```

1. Customize whatever you'd like in the code. 
2. Open the folder LangGraph Studio! 

## How to customize

1. **Add new tools**: Extend the agent's capabilities by adding new tools in [tools.py](/langchain-ai/react-agent/blob/main/src/react_agent/tools.py). These can be any Python functions that perform specific tasks. 
2. **Select a different model**: We default to Anthropic's Claude 3 Sonnet. You can select a compatible chat model using `provider/model-name` via runtime context. Example: `openai/gpt-4-turbo-preview`. 
3. **Customize the prompt**: We provide a default system prompt in [prompts.py](/langchain-ai/react-agent/blob/main/src/react_agent/prompts.py). You can easily update this via context in the studio. 

You can also quickly extend this template by:

- Modifying the agent's reasoning process in [graph.py](/langchain-ai/react-agent/blob/main/src/react_agent/graph.py). 
- Adjusting the ReAct loop or adding additional steps to the agent's decision-making process. 

## Development

While iterating on your graph, you can edit past state and rerun your app from past states to debug specific nodes. Local changes will be automatically applied via hot reload. Try adding an interrupt before the agent calls tools, updating the default system message in `src/react_agent/context.py` to take on a persona, or adding additional nodes and edges!

Follow up requests will be appended to the same thread. You can create an entirely new thread, clearing previous history, using the `+` button in the top right.

You can find the latest (under construction) docs on [LangGraph](https://github.com/langchain-ai/langgraph) here, including examples and other references. Using those guides can help you pick the right patterns to adapt here for your use case.

LangGraph Studio also integrates with [LangSmith](https://smith.langchain.com/) for more in-depth tracing and collaboration with teammates.

## Footnotes

1. [https://python.langchain.com/docs/concepts/#tools](https://python.langchain.com/docs/concepts/#tools) [↩](#user-content-fnref-1-6d0d082f21aabeeb05928084ca8d819d)
````

Repository sidebar (verbatim, `page.md` lines 144–146):

> ## About
>
> LangGraph template for a simple ReAct agent
