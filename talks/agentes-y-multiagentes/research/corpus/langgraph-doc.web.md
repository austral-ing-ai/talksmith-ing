---
source_file: langgraph-doc/
source_type: web-capture
ingested_at: 2026-10-04
---

# LangGraph overview - Docs by LangChain

## Provenance
- Original location: research/web/langgraph-doc/ (page.md; metadata.yaml; assets/)
- Format: html (Mintlify docs page captured via talksmith:ingest; page.md used as text input — 8891 bytes, 10 headings, no fallback needed)
- URL: https://docs.langchain.com/oss/python/langgraph/overview
- Fetched at: 2026-08-14T16:57:52Z (HTTP 200, 814168 bytes original.html)
- Author / source (if known): LangChain Inc — official "Docs by LangChain". Edit link: https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/overview.mdx
- Date of original (if known): not stated

## Key claims
- Tagline: "Gain control with LangGraph to design agents that reliably handle complex tasks".
- "LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents." Claimed users: Klarna, Uber, J.P. Morgan, "and more".
- LangGraph gives "fine-grained control to mix deterministic, hand-coded steps with LLM-driven agentic steps in the same graph".
- "LangGraph is very low-level, and focused entirely on agent **orchestration**." It "does not abstract prompts or architecture".
- LangChain components are used throughout the docs, "but you don't need to use LangChain to use LangGraph". Beginners are pointed to LangChain's prebuilt agents.
- Underlying capabilities: durable execution, streaming, human-in-the-loop, persistence.
- Product map: **Deep Agents** = agent harness (planning, subagents, filesystem tools, context management on top of LangGraph); **LangChain** = agent framework; **LangGraph** = orchestration runtime; **LangSmith** = tracing/evaluation/prompts/deployment platform; **LangSmith Engine** = detects issues in traces and proposes fixes; **LangSmith Fleet** = no-code agent builder.
- Core benefits: mix deterministic and agentic steps; persistence (resume from where they left off after failures); human-in-the-loop (inspect/modify state at any point); comprehensive memory (short-term working memory + long-term memory across sessions); debugging with LangSmith; production-ready deployment.
- "LangGraph is inspired by Pregel and Apache Beam. The public interface draws inspiration from NetworkX."

## Definitions and terminology
- **Orchestration framework / runtime**: LangGraph's self-description.
- **Agent harness**: higher-level layer (Deep Agents) providing planning, subagents, filesystem tools, context management.
- **`StateGraph`**, **`MessagesState`**, **`START`**, **`END`**, `add_node`, `add_edge`, `compile`, `invoke`: graph-construction primitives shown in hello world.
- **Durable execution**, **human-in-the-loop**, **persistence**, **short-term working memory**, **long-term memory**.

## Evidence and examples
- Install: `pip install -U langgraph` / `uv add langgraph`.
- Hello world with a `mock_llm` node returning "hello world" (see excerpt).
- LangSmith tracing via `LANGSMITH_TRACING=true`.

## Inconsistencies / open questions
- [open question] "Trusted by companies ... Klarna, Uber, J.P. Morgan" is a vendor marketing claim with no detail on what those companies run — a case study would settle it; do not present as evidence of adoption scale.
- [verified] The page is marketing-heavy (LangSmith products appear in several sections); the technical content is limited to the hello world and the benefits list — checked against page.md.
- [verified] Captured 2026-08-14, earlier than the 2026-10-04 captures — checked in metadata.yaml.

## Images / diagrams
All five images are site chrome / product icons, not content diagrams.

### langgraph-doc.web/images/langchain-docs-dark-blue.png
- Provenance: research/web/langgraph-doc/assets/langchain-docs-dark-blue.png ← mintcdn LangChain brand asset (alt "light logo"); 3889x507 PNG. Site header logo.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### langgraph-doc.web/images/langchain-docs-light-blue.png
- Provenance: research/web/langgraph-doc/assets/langchain-docs-light-blue.png ← mintcdn LangChain brand asset (alt "dark logo"); 3889x507 PNG. Site header logo (dark theme).
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### langgraph-doc.web/images/observability-icon-dark.png
- Provenance: research/web/langgraph-doc/assets/observability-icon-dark.png ← mintcdn brand asset (no alt); 200x200 PNG. Icon on the "LangSmith Observability" card in "LangGraph ecosystem".
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### langgraph-doc.web/images/deployment-icon-dark.png
- Provenance: research/web/langgraph-doc/assets/deployment-icon-dark.png ← mintcdn brand asset (no alt); 200x200 PNG. Icon on the "LangSmith Deployment" card.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### langgraph-doc.web/images/langchain-icon.png
- Provenance: research/web/langgraph-doc/assets/langchain-icon.png ← mintcdn brand asset (no alt); 195x195 PNG. Icon on the "LangChain" card.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

## Raw / preserved excerpts

> Trusted by companies shaping the future of agents—including Klarna, Uber, J.P. Morgan, and more—LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents. LangGraph gives you fine-grained control to mix deterministic, hand-coded steps with LLM-driven agentic steps in the same graph, so you can build bespoke agents that behave exactly the way your application requires. LangGraph is very low-level, and focused entirely on agent **orchestration**. Before using LangGraph, we recommend you familiarize yourself with some of the components used to build agents, starting with models and tools. We will commonly use LangChain components throughout the documentation to integrate models and tools, but you don't need to use LangChain to use LangGraph. If you are just getting started with agents or want a higher-level abstraction, we recommend you use LangChain's agents that provide prebuilt architectures for common LLM and tool-calling loops. LangGraph is focused on the underlying capabilities important for agent orchestration: durable execution, streaming, human-in-the-loop, and more. One of LangGraph's core strengths is the ability to mix deterministic steps with LLM-driven agentic steps in a single graph. This lets you build bespoke workflows where parts of the logic are fully predictable and auditable while other parts are flexible and model-driven, giving you fine-grained control over exactly where and how AI is applied.

> - Deep Agents is an agent harness: planning, subagents, filesystem tools, and context management on top of LangGraph.
> - LangChain is the agent framework: abstractions and integrations for models, tools, and agent loops.
> - LangGraph is the orchestration runtime: durable execution, streaming, human-in-the-loop, and persistence.
> - LangSmith is the platform for tracing, evaluation, prompts, and deployment across frameworks.
> - LangSmith Engine detects issues in your LangGraph agent traces and proposes fixes. You can open a pull request with the proposed fix directly from the Engine tab.
> - LangSmith Fleet is the no-code agent builder for templates, integrations, and routine automation.

```python
from langgraph.graph import StateGraph, MessagesState, START, END

def mock_llm(state: MessagesState):
    return {"messages": [{"role": "ai", "content": "hello world"}]}

graph = StateGraph(MessagesState)
graph.add_node(mock_llm)
graph.add_edge(START, "mock_llm")
graph.add_edge("mock_llm", END)
graph = graph.compile()

graph.invoke({"messages": [{"role": "user", "content": "hi!"}]})
```

> ## Core benefits
>
> LangGraph provides low-level supporting infrastructure for *any* long-running, stateful workflow or agent. LangGraph does not abstract prompts or architecture, and provides the following central benefits:
>
> - **Mix deterministic and agentic steps**: Combine hand-coded, deterministic logic with LLM-driven decision-making in a single graph. Use deterministic steps where you need reliability and predictability, and agentic steps where you need flexibility—giving you precise control over every part of your agent's behavior.
> - Persistence: Build agents that persist through failures and can run for extended periods, resuming from where they left off.
> - Human-in-the-loop: Incorporate human oversight by inspecting and modifying agent state at any point.
> - Comprehensive memory: Create stateful agents with both short-term working memory for ongoing reasoning and long-term memory across sessions.
> - Debugging with LangSmith: Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics.
> - Production-ready deployment: Deploy sophisticated agent systems confidently with scalable infrastructure designed to handle the unique challenges of stateful, long-running workflows.

> ## Acknowledgements
>
> LangGraph is inspired by Pregel and Apache Beam. The public interface draws inspiration from NetworkX. LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.
