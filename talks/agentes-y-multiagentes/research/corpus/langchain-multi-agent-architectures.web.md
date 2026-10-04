---
source_file: langchain-multi-agent-architectures/
source_type: web-capture
ingested_at: 2026-10-04
---

# Choosing the Right Multi-Agent Architecture (LangChain blog)

## Provenance
- Original location: `research/web/langchain-multi-agent-architectures/` (`page.md` used as text input; `original.html` consulted to recover the six tables, which `page.md` flattened into unreadable runs of text and stars)
- Format: html (web capture via `talksmith:ingest`)
- URL: https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture
- Fetched: 2026-10-04T14:02:05Z (HTTP 200, 170,404 bytes)
- Author / source (if known): Sydney Runkle, LangChain blog (category "Agent Architecture"; 7 min read)
- Date of original (if known): January 14, 2026 (byline on page)
- Presenter-provided; a core source for the Talk.

## Key claims
- **Start single-agent.** "Many agentic tasks are best handled by a single agent with well-designed tools. You should start here—single agents are simpler to build, reason about, and debug." Closing advice: "Start with a single agent and good prompt engineering. Add tools before adding agents. Graduate to multi-agent patterns only when you hit clear limits."
- Two constraints push teams toward multi-agent as capabilities grow:
  - **Context management** — specialized knowledge for every capability does not fit in one prompt; you need to surface information selectively.
  - **Distributed development** — different teams own different capabilities; one monolithic prompt is hard to manage across team boundaries.
- In those cases multi-agent architectures "*can* become the right choice" (emphasis in source).
- Cites Anthropic's multi-agent research system: a lead Claude Opus 4 agent with Claude Sonnet 4 subagents "outperformed single-agent Claude Opus 4 by 90.2% on internal research evaluations"; attributed to separate context windows enabling parallel reasoning.
- **Four foundational patterns**: subagents, skills, handoffs, routers. They differ on task coordination, state management, and "sequential unlocking".
  - **Subagents (centralized orchestration)** — a supervisor calls specialized subagents *as tools*; main agent keeps conversation context, subagents are stateless → strong context isolation; can invoke several in parallel. Tradeoff: one extra model call per interaction (results flow back through the main agent) → latency and tokens.
  - **Skills (progressive disclosure)** — one agent loads specialized prompts/knowledge on demand; "perhaps controversially, we consider skills to be a quasi-multi-agent architecture." Skills are directories of instructions, scripts and resources; at startup only names + descriptions are known; full content loads when relevant; extra files are a third level of detail. Tradeoff: context accumulates in history → token bloat.
  - **Handoffs (state-driven transitions)** — the active agent changes based on conversation state; agents transfer control via a handoff tool call that updates state (switch agent, or change the current agent's system prompt and tools). State survives across turns. Tradeoff: more stateful, needs careful state management.
  - **Router (parallel dispatch and synthesis)** — a routing step classifies/decomposes input, invokes zero or more specialized agents in parallel, synthesizes results. Typically stateless. Tradeoff: repeated routing overhead if history matters; mitigate by wrapping the router as a tool inside a stateful conversational agent.
- Architecture choice "directly impacts latency, cost, and user experience"; three scenarios quantify it (see Evidence).
- Deep Agents (LangChain) is offered as an out-of-the-box implementation combining subagents and skills.

## Definitions and terminology
- **Subagents pattern** — supervisor agent coordinates stateless specialized subagents by calling them as tools; all routing passes through the main agent.
- **Skills pattern / progressive disclosure** — single agent that loads specialized prompt-packages on demand; three levels of detail (name+description → full skill → additional files).
- **Handoffs pattern** — agents transfer control to one another through tool calls that update persistent state.
- **Router pattern** — stateless classification + parallel dispatch + synthesis.
- **Context isolation** — subagents see only the context relevant to their subtask.
- **Multi-hop** — "Does the pattern support calling multiple subagents in series?"
- **Direct user interaction** — "Can subagents converse directly with the user?"
- **Distributed development** — "Can different teams maintain components independently?"
- **Parallelization** — "Can multiple agents execute concurrently?"

## Evidence and examples
- Example uses per pattern: Subagents → personal assistant coordinating calendar, email, CRM; research systems delegating to domain experts. Skills → coding agents, creative assistants. Handoffs → customer-support flows that collect information in stages. Router → enterprise knowledge bases, multi-vertical support assistants.

**Table 1 — Matching requirements to patterns** (recovered from `original.html`)

| Your requirements | Pattern |
|---|---|
| Multiple distinct domains (calendar, email, CRM), need parallel execution | Subagents |
| Single agent with many possible specializations, lightweight composition | Skills |
| Sequential workflow with state transitions, agent converses with user throughout | Handoffs |
| Distinct verticals, query multiple sources in parallel and synthesize results | Router |

**Table 2 — How each pattern supports common requirements** (recovered from `original.html`; `page.md` collapsed the stars)

| Pattern | Distributed development | Parallelization | Multi-hop | Direct user interaction |
|---|---|---|---|---|
| Subagents | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ |
| Skills | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Handoffs | — | — | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Router | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | — | ⭐⭐⭐ |

**Table 3 — Scenario 1: one-shot request ("buy coffee", agent calls a `buy_coffee` tool)**

| Pattern | Model calls | Notes |
|---|---|---|
| Subagents | 4 | Results flow back through main agent |
| Skills | 3 | Direct execution |
| Handoffs | 3 | Direct execution |
| Router | 3 | Direct execution |

**Table 4 — Scenario 2: repeat request (Turn 1 "buy coffee", Turn 2 "buy coffee again")**

| Pattern | Turn 2 calls | Total calls | Efficiency gain |
|---|---|---|---|
| Subagents | 4 | 8 | — |
| Skills | 2 | 5 | 40% |
| Handoffs | 2 | 5 | 40% |
| Router | 3 | 6 | 25% |

**Table 5 — Scenario 3: multi-domain query ("Compare Python, JavaScript, and Rust for web development"; ~2000 tokens of docs per language agent; all patterns can make parallel tool calls)**

| Pattern | Model calls | Total tokens | Notes |
|---|---|---|---|
| Subagents | 5 | ~9K | Each subagent works in isolation |
| Skills | 3 | ~15K | Context accumulation |
| Handoffs | 7+ | ~14K+ | Sequential execution required |
| Router | 5 | ~9K | Parallel execution |

**Table 6 — Performance summary**

| Pattern | Single requests | Repeat requests | Parallel execution | Large-context domains |
|---|---|---|---|---|
| Subagents | — | — | ✅ | ✅ |
| Skills | ✅ | ✅ | — | — |
| Handoffs | ✅ | ✅ | — | — |
| Router | ✅ | — | ✅ | ✅ |

- Full performance breakdown (with mermaid diagrams per architecture) is said to live in LangChain's multi-agent docs: https://docs.langchain.com/oss/python/langchain/multi-agent#performance-comparison
- Docs/tutorial links per pattern: subagents (personal assistant tutorial), skills (SQL assistant tutorial), handoffs (customer-support tutorial), router (multi-source knowledge base tutorial) — all under `docs.langchain.com/oss/python/langchain/multi-agent/…`.

## Inconsistencies / open questions
- [verified] Scenario 2 text says "Stateful patterns (Handoffs, Skills) save 40-50% of calls on repeat requests", but the source's own table shows 40% for both and nothing reaching 50% — checked against Table 4 (8 → 5 total calls, which is 37.5%, rounded to 40% in the table).
- [verified] Scenario 3 text says "Subagents processes 67% fewer tokens overall compared to Skills", but the table gives ~9K vs ~15K: that is 40% fewer for Subagents (9/15 = 0.6), or equivalently Skills uses ~67% *more* (15/9 ≈ 1.67) — checked by arithmetic on Table 5. The "67% fewer" wording is wrong; the direction of the claim (Subagents cheaper) holds.
- [open question] The 90.2% figure for Anthropic's multi-agent research system is quoted second-hand — settle by checking the linked Anthropic engineering post (https://www.anthropic.com/engineering/multi-agent-research-system).
- [open question] Model counts in Tables 3–5 are LangChain's own illustrative analysis of "representative scenarios", not measured benchmarks; methodology is only in the linked docs page — settle by reading the performance-comparison docs.
- [verified] `page.md` flattened all six HTML tables into run-on strings (e.g. "PatternDistributed developmentParallelization…⭐⭐⭐…") — checked against `original.html`; tables above are reconstructed from the HTML `<table>` cells.
- Note (not a defect): the source itself labels the classification of Skills as multi-agent "perhaps controversially" — worth flagging if the Talk adopts this taxonomy.

## Images / diagrams

Content figures (in article body, no alt text):

### `langchain-multi-agent-architectures.web/images/69cbaa03649e3ebd9d135314_image--9--1.png`
- Provenance: inline after the "Subagents: Centralized orchestration" section (1500x963). Original: https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbaa03649e3ebd9d135314_image--9--1.png
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-multi-agent-architectures.web/images/69cbaa0feea3104c341d0d4f_image--10.png`
- Provenance: inline after the "Skills: Progressive disclosure" section (1552x926). Original filename `69cbaa0feea3104c341d0d4f_image--10-.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-multi-agent-architectures.web/images/69cbaa10eea3104c341d0d5e_image--11.png`
- Provenance: inline after the "Handoffs: State-driven transitions" section (1610x844). Original filename `…_image--11-.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-multi-agent-architectures.web/images/69cbaa10eea3104c341d0d5b_image--12.png`
- Provenance: inline after the "Router: Parallel dispatch and synthesis" section (2590x627). Original filename `…_image--12-.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-multi-agent-architectures.web/images/69cbaa10eea3104c341d0d78_image--13.png`
- Provenance: inline after "Scenario 1: One-shot request" key insight (2322x1844). Original filename `…_image--13-.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-multi-agent-architectures.web/images/69cbaa10eea3104c341d0d62_image--14.png`
- Provenance: inline after "Scenario 2: Repeat request" key insight (1714x1846). Original filename `…_image--14-.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-multi-agent-architectures.web/images/69cbaa10eea3104c341d0d75_image--15.png`
- Provenance: inline after "Scenario 3: Multi-domain query" (2000x1295). Original filename `…_image--15-.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

Site chrome (author avatars, icons, related-post thumbnails — not article content):

### `langchain-multi-agent-architectures.web/images/69dcee60745f0e15b18ad4d5_sydney-runkle.png`
- Provenance: author avatar (byline and related-content cards).
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-multi-agent-architectures.web/images/69dd146b49c3ff6f8c05da14_Eugene-Yurtsev-1.png`
- Provenance: author avatar on related-content card "How to Build a Model Router in the Harness". Original filename `…_Eugene-Yurtsev%201.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-multi-agent-architectures.web/images/69e12735c02bb07c894a067a_hunter-lovell.png`
- Provenance: author avatar on related-content cards.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-multi-agent-architectures.web/images/6abdc9fb7390b9da2726672e_model-router-webflow-dark-1200x675.png`
- Provenance: related-content thumbnail, alt "How to Build a Model Router in the Harness".
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-multi-agent-architectures.web/images/6ab6ba616821ea2bd3edd56a_webflow-cover-light-building-prod-jev-langgraph-1600x900.png`
- Provenance: related-content thumbnail "Building Prod with Jev and LangGraph".
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-multi-agent-architectures.web/images/6aac8ce2e3f50ce7069ae68f_jev-harness-a-title-hero-1600x900.png`
- Provenance: related-content thumbnail "Building a Harness with Jev".
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-multi-agent-architectures.web/images/69ce2c533137196179bae949_Icon-7.svg`
- Provenance: reading-time icon next to the byline.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-multi-agent-architectures.web/images/69cd1fd0002272ce39bf1241_Icon-6.svg`
- Provenance: reading-time icon on related-content cards.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-multi-agent-architectures.web/images/69ce01ea562f8cc223cabf25_Frame-2147254328.svg`
- Provenance: newsletter form decoration at page bottom. Original filename `…_Frame%202147254328.svg`.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

## Raw / preserved excerpts

> Many agentic tasks are best handled by a single agent with well-designed tools. You should start here—single agents are simpler to build, reason about, and debug. But as applications scale, teams face a common challenge wherein they have sprawling agent capabilities they want to combine into a single coherent interface. As the features they want to combine grow in number, two main constraints emerge:
>
> **Context management**: Specialized knowledge for each capability doesn't fit comfortably in a single prompt. If context windows were infinite and latency was zero, you could include all relevant information upfront. In practice, you need strategies to selectively surface information as agents work.
>
> **Distributed development**: Different teams develop and maintain each capability independently, with clear boundaries and ownership. A single monolithic agent prompt becomes difficult to manage across team boundaries.
>
> These constraints become critical when you're managing extensive domain knowledge, coordinating across teams, or tackling genuinely complex tasks. In these cases, multi-agent architectures *can* become the right choice.

> Recent research demonstrates how multi-agent systems perform better in these situations. In Anthropic's multi-agent research system, a multi-agent architecture with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on internal research evaluations. The architecture's ability to distribute work across agents with separate context windows enabled parallel reasoning that a single agent couldn't achieve.

> Four architectural patterns form the foundation of most multi-agent applications: subagents, skills, handoffs, and routers. Each takes a different approach to task coordination, state management, and sequential unlocking.

**Subagents: Centralized orchestration**
> In the subagents pattern, a supervisor agent coordinates specialized subagents by calling them as tools. The main agent maintains conversation context while subagents remain stateless, providing strong context isolation.
>
> **How it works**: The main agent decides which subagents to invoke, what input to provide, and how to combine results. Subagents don't remember past interactions. This architecture provides centralized control where all routing passes through the main agent, which can invoke multiple subagents in parallel.
>
> **Best for**: Applications with multiple distinct domains where you need centralized workflow control and subagents don't need to converse directly with users. Examples include personal assistants that coordinate calendar, email, and CRM operations, or research systems that delegate to specialized domain experts.
>
> **Key tradeoff**: Adds one extra model call per interaction because results must flow back through the main agent. This overhead provides centralized control and context isolation, but costs latency and tokens.

**Skills: Progressive disclosure**
> In the skills pattern, an agent loads specialized prompts and knowledge on-demand. Think of it as progressive disclosure for agent capabilities.
>
> While the skills architecture technically uses a single agent, it shares characteristics with multi-agent systems by enabling that agent to dynamically adopt specialized personas. This approach provides similar benefits to multi-agent patterns—like distributed development and fine-grained context control—but through a lighter-weight, prompt-driven method rather than managing multiple agent instances. So, perhaps controversially, we consider skills to be a quasi-multi-agent architecture.
>
> **How it works**: Skills are primarily prompt-driven specializations packaged as directories containing instructions, scripts, and resources. At startup, the agent knows only skill names and descriptions. When a skill becomes relevant, the agent loads its full context. Additional files within skills provide a third level of detail that the agent discovers only as needed.
>
> **Best for**: Single agents with many possible specializations, situations where you don't need to enforce constraints between capabilities, or team distribution where different teams maintain different skills. Common examples include coding agents or creative assistants.
>
> **Key tradeoff**: Context accumulates in conversation history as skills are loaded, which can lead to token bloat on subsequent calls. However, the pattern provides simplicity and direct user interaction throughout.

**Handoffs: State-driven transitions**
> In the handoffs pattern, the active agent changes dynamically based on conversation context. Each agent has the ability to transfer to others via tool calling.
>
> **How it works**: When an agent calls a handoff tool, it updates state that determines the next agent to activate. This can mean switching to a different agent or changing the current agent's system prompt and available tools. The state survives across conversation turns, enabling sequential workflows.
>
> **Best for**: Customer support flows that collect information in stages, multi-stage conversational experiences, or any scenario requiring sequential constraints where capabilities unlock only after preconditions are met.
>
> **Key tradeoff**: More stateful than other patterns, requiring careful state management. However, this enables fluid multi-turn conversations where context carries forward naturally between stages.

**Router: Parallel dispatch and synthesis**
> In the router pattern, a routing step classifies input and directs it to specialized agents, executing queries in parallel and synthesizing results.
>
> **How it works**: The router decomposes the query, invokes zero or more specialized agents in parallel, and synthesizes results into a coherent response. Routers are typically stateless, handling each request independently.
>
> **Best for**: Applications with distinct verticals (separate knowledge domains), scenarios requiring queries across multiple sources in parallel, or situations where you need to synthesize results from multiple agents. Examples include enterprise knowledge bases and multi-vertical customer support assistants.
>
> **Key tradeoff**: Stateless design means consistent performance per request, but repeated routing overhead if you need conversation history. Can be mitigated by wrapping the router as a tool within a stateful conversational agent.

**Key insights from the performance scenarios (verbatim)**
> **Key insight:** Handoffs, Skills, and Router are most efficient for single tasks (3 calls each). Subagents adds one extra call because results flow back through the main agent. This overhead provides centralized control, as seen below.

> **Key insight**: Stateful patterns (Handoffs, Skills) save 40-50% of calls on repeat requests by maintaining context. Subagents maintain consistent cost per request through stateless design, providing strong context isolation at the cost of repeated model calls.

> **Key insight**: For multi-domain tasks, patterns with parallel execution (Subagents, Router) are most efficient. Skills has fewer calls but high token usage due to context accumulation. Handoffs must execute sequentially and can't leverage parallel tool calling for consulting multiple domains simultaneously.
>
> In this scenario, Subagents processes 67% fewer tokens overall compared to Skills due to context isolation. Each subagent works only with relevant context, avoiding the token bloat that accumulates when loading multiple skills into a single conversation.

**Getting Started**
> Multi-agent systems coordinate specialized components to tackle complex workflows. When you do need multi-agent capabilities, match your requirements to the decision framework above. For teams wanting to start quickly, Deep Agents offers an out-of-the-box implementation combining subagents and skills for complex task planning.
>
> In many cases though, simpler architectures often suffice. Start with a single agent and good prompt engineering. Add tools before adding agents. Graduate to multi-agent patterns only when you hit clear limits.
