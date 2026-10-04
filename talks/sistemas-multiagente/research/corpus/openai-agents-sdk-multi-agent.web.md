---
source_file: openai-agents-sdk-multi-agent/
source_type: web-capture
ingested_at: 2026-10-04
---

# Agent orchestration - OpenAI Agents SDK

## Provenance
- Original location: research/web/openai-agents-sdk-multi-agent/ (page.md; metadata.yaml)
- Format: html (captured via talksmith:ingest; page.md used as text input — 5119 bytes, 6 headings, no fallback needed)
- URL: https://openai.github.io/openai-agents-python/multi_agent/
- Fetched at: 2026-10-04T19:21:26Z (HTTP 200, 72955 bytes original.html)
- Author / source (if known): OpenAI — official documentation of the OpenAI Agents SDK (Python)
- Date of original (if known): not stated on the page

## Key claims
- "Orchestration refers to the flow of agents in your app. Which agents run, in what order, and how is the next step decided?"
- There are two main ways to orchestrate agents: (1) letting the LLM make decisions (plan, reason, decide steps), and (2) orchestrating via code (flow of agents determined by your code). They can be mixed; each has tradeoffs.
- Definition used by the SDK: "An agent is an LLM equipped with instructions, tools and handoffs."
- Given an open-ended task, the LLM can autonomously plan, use tools to act and acquire data, and use handoffs to delegate to sub-agents.
- Two core SDK patterns in Python:
  - **Agents as tools** — a manager agent keeps control of the conversation and calls specialists via `Agent.as_tool()`. Best when one agent should own the final answer, combine outputs from several specialists, or enforce shared guardrails in one place.
  - **Handoffs** — a triage agent routes the conversation to a specialist, which "becomes the active agent for the rest of the turn". Best when the specialist should respond directly, prompts should stay focused, or the handoff should switch active instructions without the manager narrating the result.
- Use agents-as-tools when a specialist should help with a bounded subtask "but should not take over the user-facing conversation"; use handoffs "when routing itself is part of the workflow".
- The two can be combined: a triage agent hands off to a specialist, which in turn calls other agents as tools.
- Tactics for LLM orchestration: invest in good prompts; monitor and iterate; let the agent introspect and improve (loop + self-critique, feed error messages); prefer specialized agents that excel at one task over a general-purpose agent; invest in evals.
- Code orchestration "makes tasks more deterministic and predictable, in terms of speed, cost and performance". Common code patterns: structured outputs to classify and route; chaining agents (output of one is input of the next, e.g. research → outline → write → critique → improve); evaluator loop (`while` loop with task agent + evaluator agent until pass); running agents in parallel (e.g. `asyncio.gather`).

## Definitions and terminology
- **Orchestration**: the flow of agents in the app — which run, in what order, how the next step is decided.
- **Agent** (SDK sense): an LLM equipped with instructions, tools and handoffs.
- **Agents as tools / `Agent.as_tool()`**: manager-style orchestration; the manager keeps the conversation and calls specialists as tools.
- **Handoff**: delegation in which the specialist becomes the active agent for the rest of the turn.
- **Triage agent**: the routing agent that decides which specialist receives the conversation.
- **Evaluator agent**: agent that assesses another agent's output in a loop until criteria are met.

## Evidence and examples
- Research-agent example capability set: web search, file search and retrieval over proprietary data, computer use, code execution, handoffs to specialized agents (planning, report writing).
- Blog-post pipeline example: research → outline → write → critique → improve.
- Examples repository referenced: https://github.com/openai/openai-agents-python/tree/main/examples/agent_patterns
- Related guides linked: Agents, Tools (agents-as-tools), Handoffs, Running agents, Quickstart.

## Inconsistencies / open questions
- [open question] The page offers no quantitative evidence for the claim that code orchestration is more predictable "in terms of speed, cost and performance" — it is a design guideline, not a measured result; a benchmark or case study would settle it.
- [verified] The patterns comparison table is flattened into running text in page.md (cells concatenated on one line) — checked against the page.md capture; the table is reconstructed below from that line without altering wording.

## Images / diagrams
No images captured (metadata.yaml lists `assets: []`). Companion folder `openai-agents-sdk-multi-agent.web/images/` exists and is empty.

## Raw / preserved excerpts

> Orchestration refers to the flow of agents in your app. Which agents run, in what order, and how is the next step decided? There are two main ways to orchestrate agents:
>
> 1. Allowing the LLM to make decisions: this uses the intelligence of an LLM to plan, reason, and decide on what steps to take based on that.
> 2. Orchestrating via code: determining the flow of agents via your code.
>
> You can mix and match these patterns. Each has their own tradeoffs, described below.

> An agent is an LLM equipped with instructions, tools and handoffs. This means that given an open-ended task, the LLM can autonomously plan how it will tackle the task, using tools to take actions and acquire data, and using handoffs to delegate tasks to sub-agents. For example, a research agent could be equipped with capabilities like:
> - Web search to find information online
> - File search and retrieval to search through proprietary data and connected data sources
> - Computer use to take actions on a computer
> - Code execution to do data analysis
> - Handoffs to specialized agents that are great at planning, report writing and more.

Core SDK patterns (table reconstructed from the flattened capture):

| Pattern | How it works | Best when |
|---|---|---|
| Agents as tools | A manager agent keeps control of the conversation and calls specialist agents through `Agent.as_tool()`. | You want one agent to own the final answer, combine outputs from multiple specialists, or enforce shared SDK guardrails in one place. |
| Handoffs | A triage agent routes the conversation to a specialist, and that specialist becomes the active agent for the rest of the turn. | You want the specialist to respond directly, keep prompts focused, or have the handoff switch the active instructions without requiring the manager to narrate the result. |

> Use **agents as tools** when a specialist should help with a bounded subtask but should not take over the user-facing conversation. Use **handoffs** when routing itself is part of the workflow and you want the chosen specialist to own the remainder of the current turn.
>
> You can also combine the two. A triage agent might hand off to a specialist, and that specialist can still call other agents as tools for narrow subtasks.
>
> This pattern is great when the task is open-ended and you want to rely on the intelligence of an LLM. The most important tactics here are:
>
> 1. Invest in good prompts. Make it clear what tools are available, how to use them, and what constraints the agent must follow.
> 2. Monitor your app and iterate on it. See where things go wrong, and iterate on your prompts.
> 3. Allow the agent to introspect and improve. For example, run it in a loop, and let it critique itself; or, provide error messages and let it improve.
> 4. Have specialized agents that excel in one task, rather than having a general purpose agent that is expected to be good at anything.
> 5. Invest in evals. This lets you train your agents to improve and get better at tasks.

> ## Orchestrating via code
>
> While orchestrating via LLM is powerful, orchestrating via code makes tasks more deterministic and predictable, in terms of speed, cost and performance. Common patterns here are:
>
> - Using structured outputs to generate well formed data that you can inspect with your code. For example, you might ask an agent to classify the task into a few categories, and then pick the next agent based on the category.
> - Chaining multiple agents by transforming the output of one into the input of the next. You can decompose a task like writing a blog post into a series of steps - do research, write an outline, write the blog post, critique it, and then improve it.
> - In each iteration of a `while` loop, run the task agent to produce an output, then run an evaluator agent to assess that output and provide feedback; stop when the evaluator says the output passes the required criteria.
> - Running multiple agents in parallel, e.g. via Python primitives like `asyncio.gather`. This is useful for speed when you have multiple tasks that don't depend on each other.
