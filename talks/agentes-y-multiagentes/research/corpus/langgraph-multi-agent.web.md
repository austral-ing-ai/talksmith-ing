---
source_file: langgraph-multi-agent/
source_type: web-capture
ingested_at: 2026-10-04
---

# Multi-agent - Docs by LangChain

## Provenance
- Original location: research/web/langgraph-multi-agent/ (page.md; metadata.yaml; assets/)
- Format: html (Mintlify docs page captured via talksmith:ingest; page.md used as text input — 15524 bytes, 12 headings). Tables in page.md are flattened (cells concatenated); all seven tables were re-extracted from original.html and are reproduced below.
- URL: https://docs.langchain.com/oss/python/langchain/multi-agent
- Fetched at: 2026-08-14T16:57:56Z (HTTP 200, 910983 bytes original.html) — note: captured ~7 weeks before the other web captures of this Talk.
- Author / source (if known): LangChain — official "Docs by LangChain" (OSS Python, LangChain section; folder name says "langgraph" but the page lives under `/oss/python/langchain/`)
- Date of original (if known): not stated on the page. Edit link: https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/multi-agent/index.mdx

## Key claims
- "Multi-agent systems coordinate specialized components to tackle complex workflows. However, not every complex task requires this approach—a single agent with the right (sometimes dynamic) tools and prompt can often achieve similar results."
- For built-in multi-agent support LangChain points to **Deep Agents**: "a higher-level harness built on LangChain that ships with subagents, skills, planning, a virtual filesystem, and context management."
- Why multi-agent — three capabilities people actually want: **context management** ("If context were infinite and latency zero, you could dump all knowledge into a single prompt—but since it's not, you need patterns to selectively surface relevant information"), **distributed development** (teams own capabilities independently), **parallelization** (concurrent specialized workers).
- Multi-agent is valuable "when a single agent has too many tools and makes poor decisions about which to use, when tasks require specialized knowledge with extensive context (long prompts and domain-specific tools), or when you need to enforce sequential constraints that unlock capabilities only after certain conditions are met."
- "At the center of multi-agent design is **context engineering**—deciding what information each agent sees. The quality of your system depends on ensuring each agent has access to the right data for its task."
- Five patterns: Subagents, Handoffs, Skills, Router, Custom workflow (see tables).
- Patterns can be mixed (subagents invoking tools that invoke custom workflows or routers; subagents using skills).
- Performance metrics: **model calls** (latency, cost) and **tokens processed** (cost, context limits).
- One-shot ("Buy coffee"): Handoffs, Skills, Router = 3 calls; Subagents = 4, "because results flow back through the main agent—this overhead provides centralized control."
- Repeat request: "Subagents are **stateless by design**", "This provides strong context isolation but repeats the full flow" (4+4=8). Handoffs: coffee agent "still active" (3+2=5). Skills: skill context "already loaded" (3+2=5). Router: stateless, each request needs a routing call (3+3=6); "Can be optimized by wrapping as a tool in a stateful agent". "Stateful patterns (Handoffs, Skills) save 40-50% of calls on repeat requests."
- Multi-domain ("Compare Python, JavaScript, and Rust for web development", ~2000 tokens of docs per language): Subagents 5 calls ~9K tokens ("Each subagent works in isolation with only its relevant context"); Handoffs 7+ calls ~14K+ ("executes sequentially—can't research all three languages in parallel. Growing conversation history adds overhead"); Skills 3 calls ~15K ("every subsequent call processes all 6K tokens of skill documentation"); Router 5 calls ~9K ("uses an LLM for routing, then invokes agents in parallel").
- "For multi-domain tasks, patterns with parallel execution (Subagents, Router) are most efficient. Skills has fewer calls but high token usage due to context accumulation. Handoffs is inefficient here."

## Definitions and terminology
- **Subagents**: main agent coordinates subagents as tools; all routing passes through the main agent. (Supervisor / orchestrator-worker family.)
- **Handoffs**: behaviour changes dynamically based on state; tool calls update a state variable that triggers routing or configuration changes, switching agents or adjusting the current agent's tools and prompt.
- **Skills**: specialized prompts/knowledge loaded on demand; a single agent stays in control.
- **Router**: a routing step classifies input and directs it to one or more agents; results synthesized.
- **Custom workflow**: bespoke LangGraph flows mixing deterministic logic and agentic behaviour.
- **Context engineering**: deciding what information each agent sees.
- **Context isolation**: subagents start fresh each invocation, seeing only their relevant context.
- Evaluation axes: **Distributed development**, **Parallelization**, **Multi-hop** (calling multiple subagents in series), **Direct user interaction** (subagents converse directly with the user).

## Evidence and examples
All numbers below are the page's own illustrative scenario counts (not measured benchmarks).

Patterns table:

| Pattern | How it works |
|---|---|
| Subagents | A main agent coordinates subagents as tools. All routing passes through the main agent, which decides when and how to invoke each subagent. |
| Handoffs | Behavior changes dynamically based on state. Tool calls update a state variable that triggers routing or configuration changes, switching agents or adjusting the current agent's tools and prompt. |
| Skills | Specialized prompts and knowledge loaded on-demand. A single agent stays in control while loading context from skills as needed. |
| Router | A routing step classifies input and directs it to one or more specialized agents. Results are synthesized into a combined response. |
| Custom workflow | Build bespoke execution flows with LangGraph, mixing deterministic logic and agentic behavior. Embed other patterns as nodes in your workflow. |

Choosing a pattern (from original.html):

| Pattern | Distributed development | Parallelization | Multi-hop | Direct user interaction |
|---|---|---|---|---|
| Subagents | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ |
| Handoffs | - | - | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Skills | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Router | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | - | ⭐⭐⭐ |

One-shot request ("Buy coffee"):

| Pattern | Model calls | Best fit |
|---|---|---|
| Subagents | 4 | |
| Handoffs | 3 | ✅ |
| Skills | 3 | ✅ |
| Router | 3 | ✅ |

Repeat request ("Buy coffee" then "Buy coffee again"):

| Pattern | Turn 2 calls | Total (both turns) | Best fit |
|---|---|---|---|
| Subagents | 4 | 8 | |
| Handoffs | 2 | 5 | ✅ |
| Skills | 2 | 5 | ✅ |
| Router | 3 | 6 | |

Multi-domain ("Compare Python, JavaScript, and Rust for web development"):

| Pattern | Model calls | Total tokens | Best fit |
|---|---|---|---|
| Subagents | 5 | ~9K | ✅ |
| Handoffs | 7+ | ~14K+ | |
| Skills | 3 | ~15K | |
| Router | 5 | ~9K | ✅ |

Summary:

| Pattern | One-shot | Repeat request | Multi-domain |
|---|---|---|---|
| Subagents | 4 calls | 8 calls (4+4) | 5 calls, 9K tokens |
| Handoffs | 3 calls | 5 calls (3+2) | 7+ calls, 14K+ tokens |
| Skills | 3 calls | 5 calls (3+2) | 3 calls, 15K tokens |
| Router | 3 calls | 6 calls (3+3) | 5 calls, 9K tokens |

Choosing a pattern — optimize for:

| Optimize for | Subagents | Handoffs | Skills | Router |
|---|---|---|---|---|
| Single requests | | ✅ | ✅ | ✅ |
| Repeat requests | | ✅ | ✅ | |
| Parallel execution | ✅ | | | ✅ |
| Large-context domains | ✅ | | | ✅ |
| Simple, focused tasks | | | ✅ | |

## Inconsistencies / open questions
- [verified] "Subagents processes 67% fewer tokens overall due to context isolation" does not match the page's own numbers: Subagents ~9K vs Skills ~15K tokens is (15−9)/15 = 40% fewer; 67% is how many MORE tokens Skills uses than Subagents (15/9 − 1 ≈ 0.67) — arithmetic checked against the multi-domain table. A slide should say "Skills uses ~67% more tokens" or "Subagents uses ~40% fewer".
- [open question] "Stateful patterns (Handoffs, Skills) save 40-50% of calls on repeat requests" — on the page's numbers, turn-2 calls are 2 vs Subagents' 4 (50%) and vs Router's 3 (33%); totals 5 vs 8 (37.5%). The 40-50% range only partly fits; the page does not state the baseline. Asking which comparison is intended would settle it.
- [verified] All counts are illustrative scenarios drawn in diagrams, not measured benchmarks — the page presents them as worked examples with no experimental setup.
- [open question] The page is vendor documentation promoting Deep Agents and LangSmith; its framing ("not every complex task requires this approach") is a design opinion, not evidence.
- [verified] The capture date (2026-08-14) differs from the other captures of this Talk (2026-10-04) — checked in metadata.yaml; page content may have changed since.
- [verified] Several `.png` assets are actually JPEG data (pattern-*.png and multidomain-*.png) — checked with `file`; bytes copied unchanged, extension kept as captured.

## Images / diagrams

Logos (page chrome):

### langgraph-multi-agent.web/images/langchain-docs-dark-blue.png
- Provenance: research/web/langgraph-multi-agent/assets/langchain-docs-dark-blue.png ← mintcdn LangChain brand asset (alt "light logo"); 3889x507 PNG. Site header logo.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### langgraph-multi-agent.web/images/langchain-docs-light-blue.png
- Provenance: research/web/langgraph-multi-agent/assets/langchain-docs-light-blue.png ← mintcdn LangChain brand asset (alt "dark logo"); 3889x507 PNG. Site header logo (dark theme).
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

Pattern diagrams ("Visual overview" section):

### langgraph-multi-agent.web/images/pattern-subagents.png
- Provenance: research/web/langgraph-multi-agent/assets/pattern-subagents.png (JPEG data, 1020x734) — alt "Subagents pattern: main agent coordinates subagents as tools"; caption "A main agent coordinates subagents as tools. All routing passes through the main agent."
- Depiction: Mermaid flowchart (JPEG data despite .png name). A rounded "User request" node points to a "Main Agent" box. Main Agent has outgoing arrows to three boxes stacked on the right — Subagent A, Subagent B, Subagent C — and each subagent has a return arrow back into Main Agent. A final arrow from Main Agent goes to a rounded "Response" node.
- Why it matters: Subagents (supervisor / agents-as-tools) pattern: every hop goes out from and returns to the main agent, so the main agent keeps control and is the only one that answers the user. Contrasts with handoffs, where control does not come back.
- Transcribed text: User request · Main Agent · Subagent A · Subagent B · Subagent C · Response

### langgraph-multi-agent.web/images/pattern-handoffs.png
- Provenance: research/web/langgraph-multi-agent/assets/pattern-handoffs.png (JPEG data, 1568x464) — alt "Handoffs pattern: agents transfer control via tool calls"; caption "Agents transfer control to each other via tool calls. Each agent can hand off to others or respond directly to the user."
- Depiction: Mermaid flowchart (JPEG data). "User request" points into a yellow container labelled "Agents" holding Agent A, Agent B and Agent C, connected pairwise by bidirectional arrows (A↔B, B↔C, A↔C). Each of the three agents has its own arrow out of the container to a single rounded "Response" node.
- Why it matters: Handoffs pattern: peer agents pass control among themselves and any of them may answer the user directly; there is no central coordinator. This is the decentralized counterpart of the subagents picture.
- Transcribed text: Agents · User request · Agent A · Agent B · Agent C · Response

### langgraph-multi-agent.web/images/pattern-skills.png
- Provenance: research/web/langgraph-multi-agent/assets/pattern-skills.png (JPEG data, 874x734) — alt "Skills pattern: single agent loads specialized context on-demand"; caption "A single agent loads specialized prompts and knowledge on-demand while staying in control."
- Depiction: Mermaid flowchart (JPEG data). "User request" → "Agent"; from Agent, one-way arrows go to Skill A, Skill B and Skill C (no return arrows drawn), and a fourth arrow goes to "Response".
- Why it matters: Skills pattern: a single agent stays in control and loads specialized prompts/knowledge on demand instead of delegating to other agents. Visually close to subagents, but the boxes are context, not agents — useful to show that not every specialization requires a second agent.
- Transcribed text: User request · Agent · Skill A · Skill B · Skill C · Response

### langgraph-multi-agent.web/images/pattern-router.png
- Provenance: research/web/langgraph-multi-agent/assets/pattern-router.png (JPEG data, 1560x556) — alt "Router pattern: routing step classifies input to specialized agents"; caption "A routing step classifies input and directs it to specialized agents. Results are synthesized."
- Depiction: Mermaid flowchart (JPEG data), left to right: "User request" → "Router", which fans out to Agent A, Agent B and Agent C; all three converge into a "Synthesize" box, which leads to "Response".
- Why it matters: Router pattern: a classification step dispatches the input to specialized agents (possibly several in parallel) and a synthesis step merges the results. A fixed fan-out/fan-in workflow rather than agents deciding control flow.
- Transcribed text: User request · Router · Agent A · Agent B · Agent C · Synthesize · Response

One-shot request diagrams ("Buy coffee"):

### langgraph-multi-agent.web/images/oneshot-subagents.png
- Provenance: research/web/langgraph-multi-agent/assets/oneshot-subagents.png (PNG 1568x1124) — alt "Subagents one-shot: 4 model calls for buy coffee request"; label "4 model calls".
- Depiction: Mermaid sequence diagram with four lifelines: User, Main Agent, Coffee Subagent, buy_coffee tool. User → Main Agent: "Buy coffee"; note Call 1 on Main Agent. Main Agent → Coffee Subagent: coffee_subagent(); note Call 2. Coffee Subagent → buy_coffee tool: buy_coffee(); tool returns Done (dashed); note Call 3 on Coffee Subagent. Coffee Subagent → Main Agent: "Bought coffee" (dashed); note Call 4 on Main Agent. Main Agent → User: "I bought coffee for you" (dashed).
- Why it matters: Cost accounting for a one-shot request: subagents needs 4 model calls because the result must travel back through the main agent, one more than handoffs/skills/router (3). Concrete numbers for the latency/cost trade-off of the supervisor pattern.
- Transcribed text: User · Main Agent · Coffee Subagent · buy_coffee tool · "Buy coffee" · Call 1 · coffee_subagent() · Call 2 · buy_coffee() · Done · Call 3 · "Bought coffee" · Call 4 · "I bought coffee for you"

### langgraph-multi-agent.web/images/oneshot-handoffs.png
- Provenance: research/web/langgraph-multi-agent/assets/oneshot-handoffs.png (PNG 1568x948) — alt "Handoffs one-shot: 3 model calls for buy coffee request"; label "3 model calls".
- Depiction: Mermaid sequence diagram, lifelines User, Main Agent, Coffee Agent, buy_coffee tool. User → Main Agent: "Buy coffee"; Call 1. Main Agent → Coffee Agent: transfer_to_coffee_agent(); Call 2 on Coffee Agent. Coffee Agent → buy_coffee tool: buy_coffee(); Done returned; Call 3. Coffee Agent → User directly: "I bought coffee for you" (dashed arrow skips Main Agent).
- Why it matters: Handoffs saves one call versus subagents (3 vs 4) because the agent that receives control answers the user itself — the answer does not return through the main agent.
- Transcribed text: User · Main Agent · Coffee Agent · buy_coffee tool · "Buy coffee" · Call 1 · transfer_to_coffee_agent() · Call 2 · buy_coffee() · Done · Call 3 · "I bought coffee for you"

### langgraph-multi-agent.web/images/oneshot-skills.png
- Provenance: research/web/langgraph-multi-agent/assets/oneshot-skills.png (PNG 1568x1036) — alt "Skills one-shot: 3 model calls for buy coffee request"; label "3 model calls".
- Depiction: Mermaid sequence diagram, lifelines User, Agent, load_skill tool, buy_coffee tool. User → Agent: "Buy coffee"; Call 1. Agent → load_skill tool: load_skill("coffee"); returns "Coffee skill context"; Call 2. Agent → buy_coffee tool: buy_coffee(); returns Done; Call 3. Agent → User: "I bought coffee for you".
- Why it matters: Skills also costs 3 calls for a one-shot request, all made by the same single agent; the extra step is loading context, not delegating.
- Transcribed text: User · Agent · load_skill tool · buy_coffee tool · "Buy coffee" · Call 1 · load_skill("coffee") · Coffee skill context · Call 2 · buy_coffee() · Done · Call 3 · "I bought coffee for you"

### langgraph-multi-agent.web/images/oneshot-router.png
- Provenance: research/web/langgraph-multi-agent/assets/oneshot-router.png (PNG 1568x994) — alt "Router one-shot: 3 model calls for buy coffee request"; label "3 model calls".
- Depiction: Mermaid sequence diagram, lifelines User, Router LLM, Coffee Agent, buy_coffee tool. User → Router LLM: "Buy coffee"; note "Call 1: Route to coffee agent". Router LLM → Coffee Agent: Invoke with query; Call 2. Coffee Agent → buy_coffee tool: buy_coffee(); Done; Call 3. Coffee Agent → User: "I bought coffee for you".
- Why it matters: Router: 3 calls for a one-shot request (routing call + two calls of the specialist), with the specialist answering the user directly in this single-domain case.
- Transcribed text: User · Router LLM · Coffee Agent · buy_coffee tool · "Buy coffee" · Call 1: Route to coffee agent · Invoke with query · Call 2 · buy_coffee() · Done · Call 3 · "I bought coffee for you"

Multi-domain diagrams ("Compare Python, JavaScript, and Rust"):

### langgraph-multi-agent.web/images/multidomain-subagents.png
- Provenance: research/web/langgraph-multi-agent/assets/multidomain-subagents.png (JPEG data, 1568x1232) — alt "Subagents multi-domain: 5 calls with parallel execution"; caption "Each subagent works in isolation with only its relevant context. Total: 9K tokens."
- Depiction: Mermaid sequence diagram (JPEG data), lifelines User, Main Agent, Python Subagent, JS Subagent, Rust Subagent. User → Main Agent: "Compare Python, JS, Rust"; Call 1 (1K). A "par [Parallel execution]" block contains three lanes: python_subagent() → Call 2 (2K) → "Python analysis" back to Main Agent; js_subagent() → Call 3 (2K) → "JS analysis"; rust_subagent() → Call 4 (2K) → "Rust analysis". After the block, Call 5 (2K) on Main Agent, then "Synthesized comparison" to User.
- Why it matters: Multi-domain cost for subagents: 5 calls, the three specialists run in parallel and each sees only its own context (~9K tokens total per the caption). Shows the main advantage of the supervisor pattern: context isolation plus parallelism.
- Transcribed text: User · Main Agent · Python Subagent · JS Subagent · Rust Subagent · "Compare Python, JS, Rust" · Call 1 (1K) · par [Parallel execution] · python_subagent() · Call 2 (2K) · Python analysis · js_subagent() · Call 3 (2K) · JS analysis · rust_subagent() · Call 4 (2K) · Rust analysis · Call 5 (2K) · Synthesized comparison

### langgraph-multi-agent.web/images/multidomain-handoffs.png
- Provenance: research/web/langgraph-multi-agent/assets/multidomain-handoffs.png (JPEG data, 1568x834) — alt "Handoffs multi-domain: 7+ sequential calls"; caption "Handoffs executes sequentially—can't research all three languages in parallel. Growing conversation history adds overhead. Total: ~14K+ tokens."
- Depiction: Mermaid sequence diagram (JPEG data), lifelines User, Main Agent, Python Agent, JS Agent, Rust Agent. User → Main Agent: "Compare Python, JS, Rust"; Call 1 (1K). Main Agent → Python Agent: transfer_to_python(); Calls 2-3 (2K each). Python Agent → JS Agent: transfer_to_js(); Calls 4-5 (2K each). JS Agent → Rust Agent: transfer_to_rust(); Calls 6-7 (2K each). Rust Agent → User: "Combined comparison". Strictly sequential; no parallel block.
- Why it matters: Handoffs' weakness on multi-domain work: 7+ sequential calls, no parallelism, and the conversation context grows as it passes along the chain. The counterweight to its one-shot advantage.
- Transcribed text: User · Main Agent · Python Agent · JS Agent · Rust Agent · "Compare Python, JS, Rust" · Call 1 (1K) · transfer_to_python() · Calls 2-3 (2K each) · transfer_to_js() · Calls 4-5 (2K each) · transfer_to_rust() · Calls 6-7 (2K each) · Combined comparison

### langgraph-multi-agent.web/images/multidomain-skills.png
- Provenance: research/web/langgraph-multi-agent/assets/multidomain-skills.png (JPEG data, 1560x988) — alt "Skills multi-domain: 3 calls with accumulated context"; caption "After loading, every subsequent call processes all 6K tokens of skill documentation. [...] Total: 15K tokens."
- Depiction: Mermaid sequence diagram (JPEG data), lifelines User, Agent, load_skill tool. User → Agent: "Compare Python, JS, Rust"; Call 1 (1K). Agent → load_skill tool: load_skill("python", "js", "rust"); returns "+6K context (2K each)". Then Call 2 (7K: 1K base + 6K skills) and Call 3 (7K: 1K base + 6K skills). Agent → User: "Synthesized comparison".
- Why it matters: Skills uses few calls (3) but every call after loading carries all 6K tokens of skill text — the token bill grows with accumulated context (~15K per the caption). Illustrates the context-bloat cost of keeping everything in one agent.
- Transcribed text: User · Agent · load_skill tool · "Compare Python, JS, Rust" · Call 1 (1K) · load_skill("python", "js", "rust") · +6K context (2K each) · Call 2 (7K: 1K base + 6K skills) · Call 3 (7K: 1K base + 6K skills) · Synthesized comparison

### langgraph-multi-agent.web/images/multidomain-router.png
- Provenance: research/web/langgraph-multi-agent/assets/multidomain-router.png (JPEG data, 1568x1052) — alt "Router multi-domain: 5 calls with parallel execution"; caption "Router uses an LLM for routing, then invokes agents in parallel. Similar to Subagents but with explicit routing step. Total: 9K tokens."
- Depiction: Mermaid sequence diagram (JPEG data), lifelines User, Router LLM, Python Agent, JS Agent, Rust Agent, Synthesis LLM. User → Router LLM: "Compare Python, JS, Rust"; Call 1 (1K). "par [Parallel execution]" block: Route to Python → Call 2 (2K) → "Python analysis" sent to Synthesis LLM; Route to JS → Call 3 (2K) → "JS analysis" to Synthesis LLM; Route to Rust → Call 4 (2K) → "Rust analysis" to Synthesis LLM. Then Call 5 (2K) on Synthesis LLM, which sends "Combined comparison" to User.
- Why it matters: Router on multi-domain work: 5 calls with parallel specialists, similar to subagents, but results go to a separate synthesis step rather than back to a coordinating agent. Completes the 4-pattern cost comparison.
- Transcribed text: User · Router LLM · Python Agent · JS Agent · Rust Agent · Synthesis LLM · "Compare Python, JS, Rust" · Call 1 (1K) · par [Parallel execution] · Route to Python · Call 2 (2K) · Python analysis · Route to JS · Call 3 (2K) · JS analysis · Route to Rust · Call 4 (2K) · Rust analysis · Call 5 (2K) · Combined comparison

Note: the Repeat-request section has no diagrams in the capture (text only).

## Raw / preserved excerpts

> Multi-agent systems coordinate specialized components to tackle complex workflows. However, not every complex task requires this approach—a single agent with the right (sometimes dynamic) tools and prompt can often achieve similar results. For built-in multi-agent support, use Deep Agents: a higher-level harness built on LangChain that ships with subagents, skills, planning, a virtual filesystem, and context management.

> ## Why multi-agent?
>
> When developers say they need "multi-agent," they're usually looking for one or more of these capabilities:
>
> - **Context management**: Provide specialized knowledge without overwhelming the model's context window. If context were infinite and latency zero, you could dump all knowledge into a single prompt—but since it's not, you need patterns to selectively surface relevant information.
> - **Distributed development**: Allow different teams to develop and maintain capabilities independently, composing them into a larger system with clear boundaries.
> - **Parallelization**: Spawn specialized workers for subtasks and execute them concurrently for faster results.
>
> Multi-agent patterns are particularly valuable when a single agent has too many tools and makes poor decisions about which to use, when tasks require specialized knowledge with extensive context (long prompts and domain-specific tools), or when you need to enforce sequential constraints that unlock capabilities only after certain conditions are met. At the center of multi-agent design is **context engineering**—deciding what information each agent sees. The quality of your system depends on ensuring each agent has access to the right data for its task.

> - **Distributed development**: Can different teams maintain components independently?
> - **Parallelization**: Can multiple agents execute concurrently?
> - **Multi-hop**: Does the pattern support calling multiple subagents in series?
> - **Direct user interaction**: Can subagents converse directly with the user?
>
> You can mix patterns! For example, a **subagents** architecture can invoke tools that invoke custom workflows or router agents. Subagents can even use the **skills** pattern to load context on-demand. The possibilities are endless!

> Different patterns have different performance characteristics. Understanding these tradeoffs helps you choose the right pattern for your latency and cost requirements. **Key metrics:**
>
> - **Model calls**: Number of LLM invocations. More calls = higher latency (especially if sequential) and higher per-request API costs.
> - **Tokens processed**: Total context window usage across all calls. More tokens = higher processing costs and potential context limits.

> **Key insight:** Handoffs, Skills, and Router are most efficient for single tasks (3 calls each). Subagents adds one extra call because results flow back through the main agent—this overhead provides centralized control.

> **4 calls again → 8 total**
> - Subagents are **stateless by design**—each invocation follows the same flow
> - The main agent maintains conversation context, but subagents start fresh each time
> - This provides strong context isolation but repeats the full flow
>
> **2 calls → 5 total**
> - The coffee agent is **still active** from turn 1 (state persists)
> - No handoff needed—agent directly calls `buy_coffee` tool (call 1)
> - Agent responds to user (call 2)
> - **Saves 1 call by skipping the handoff**
>
> **2 calls → 5 total**
> - The skill context is **already loaded** in conversation history
> - No need to reload—agent directly calls `buy_coffee` tool (call 1)
> - Agent responds to user (call 2)
> - **Saves 1 call by reusing loaded skill**
>
> **3 calls again → 6 total**
> - Routers are **stateless**—each request requires an LLM routing call
> - Turn 2: Router LLM call (1) → Milk agent calls buy_coffee (2) → Milk agent responds (3)
> - Can be optimized by wrapping as a tool in a stateful agent
>
> **Key insight:** Stateful patterns (Handoffs, Skills) save 40-50% of calls on repeat requests. Subagents maintain consistent cost per request—this stateless design provides strong context isolation but at the cost of repeated model calls.

> Each language agent/skill contains ~2000 tokens of documentation. All patterns can make parallel tool calls.
>
> **5 calls, ~9K tokens** — Each subagent works in **isolation** with only its relevant context. Total: **9K tokens**.
> **7+ calls, ~14K+ tokens** — Handoffs executes **sequentially**—can't research all three languages in parallel. Growing conversation history adds overhead. Total: **~14K+ tokens**.
> **3 calls, ~15K tokens** — After loading, **every subsequent call processes all 6K tokens of skill documentation**. Subagents processes 67% fewer tokens overall due to context isolation. Total: **15K tokens**.
> **5 calls, ~9K tokens** — Router uses an **LLM for routing**, then invokes agents in parallel. Similar to Subagents but with explicit routing step. Total: **9K tokens**.
>
> **Key insight:** For multi-domain tasks, patterns with parallel execution (Subagents, Router) are most efficient. Skills has fewer calls but high token usage due to context accumulation. Handoffs is inefficient here—it must execute sequentially and can't leverage parallel tool calling for consulting multiple domains simultaneously.

(Note: the Router repeat-request bullet names a "Milk agent" while the scenario is about coffee — preserved verbatim as in source.)
