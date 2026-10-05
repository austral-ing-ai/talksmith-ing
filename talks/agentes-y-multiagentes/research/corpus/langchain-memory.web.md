---
source_file: langchain-memory/
source_type: web-capture
ingested_at: 2026-10-04
---

# LangChain overview - Docs by LangChain

## Provenance
- Original location: research/web/langchain-memory/ (page.md; metadata.yaml; assets/)
- Format: html (Mintlify docs page captured via talksmith:ingest; page.md used as text input — 10632 bytes, 20 headings, no fallback needed)
- URL: https://docs.langchain.com/oss/python/langchain/overview
- Fetched at: 2026-08-14T16:56:40Z (HTTP 200, 973772 bytes original.html)
- Author / source (if known): LangChain Inc — official "Docs by LangChain". Edit link: https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/overview.mdx
- Date of original (if known): not stated
- Note: the capture folder is named `langchain-memory`, but the captured URL is the LangChain **overview** page, not a memory page (see Inconsistencies).

## Key claims
- "LangChain provides create_agent: a minimal, highly configurable agent harness. Compose exactly the agent your use case needs from model, tools, prompt, and middleware."
- "**Agent = Model + Harness.**" "The harness is everything around the model loop: the prompt, the tools, and any middleware that shapes behavior."
- Supports OpenAI, Anthropic, Google and more providers.
- Positioning: start with **Deep Agents** for a "batteries-included" agent ("automatic context compression, a virtual filesystem, and subagent-spawning"); use **LangChain** (`create_agent`) for a highly customizable harness; use **LangGraph** ("our low-level orchestration framework") for "advanced needs combining deterministic and agentic workflows"; use **LangSmith** to trace, debug and evaluate.
- Deep Agents are built on LangChain agents.
- Core benefits: standard model interface across providers; highly configurable harness via middleware ("from guardrails and retries to routing and custom tool policies"); "LangChain's agents are built on top of LangGraph" (durable execution, human-in-the-loop, persistence); debug with LangSmith ("Find failure modes, evaluate quality").

## Definitions and terminology
- **Agent = Model + Harness**: LangChain's working definition of an agent.
- **Harness**: everything around the model loop — prompt, tools, middleware.
- **`create_agent`**: LangChain's minimal agent harness constructor (`model`, `tools`, `system_prompt`).
- **Middleware**: composable add-ons shaping agent behaviour (guardrails, retries, routing, tool policies).
- **Deep Agents**: batteries-included harness with context compression, virtual filesystem and subagent spawning.

## Evidence and examples
- Same `get_weather` example ("It's always sunny in {city}!") repeated across provider tabs; model strings shown verbatim in the capture: `openai:gpt-5.5`; `google_genai:gemini-2.5-flash-lite`; `claude-sonnet-4-6`; `openrouter:anthropic/claude-sonnet-4-6`; `fireworks:accounts/fireworks/models/qwen3p5-397b-a17b`; `baseten:zai-org/GLM-5.2`; `ollama:devstral-2`; `azure_openai:gpt-5.5` (via `init_chat_model`); `bedrock_converse:us.anthropic.claude-sonnet-4-6` (comment: use `global.anthropic.claude-sonnet-4-6` for worldwide routing); `huggingface:microsoft/Phi-3-mini-4k-instruct`.

## Inconsistencies / open questions
- [verified] Folder name / content mismatch: `langchain-memory` contains the LangChain overview page, which has no section on memory (only a passing mention of "persistence" under "Built on top of LangGraph") — checked against metadata.yaml URL and page.md headings. For memory content use `langgraph-persistence-memory.web.md`.
- [open question] Model identifiers in the code tabs are reproduced verbatim from the vendor page as of 2026-08-14; their current availability was not checked, and nothing here asserts any of them is wrong — the provider catalogs (and the `claude-api` skill for the Anthropic ones) would settle it if a slide uses them.
- [verified] Captured 2026-08-14 — checked in metadata.yaml.

## Images / diagrams
All four images are site chrome / product icons.

### langchain-memory.web/images/langchain-docs-dark-blue.png
- Provenance: research/web/langchain-memory/assets/langchain-docs-dark-blue.png ← mintcdn LangChain brand asset (alt "light logo"); 3889x507 PNG. Site header logo.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### langchain-memory.web/images/langchain-docs-light-blue.png
- Provenance: research/web/langchain-memory/assets/langchain-docs-light-blue.png ← mintcdn LangChain brand asset (alt "dark logo"); 3889x507 PNG. Site header logo (dark theme).
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### langchain-memory.web/images/langgraph-icon.png
- Provenance: research/web/langchain-memory/assets/langgraph-icon.png ← mintcdn brand asset (no alt); 195x195 PNG. Icon on the "Built on top of LangGraph" card.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### langchain-memory.web/images/observability-icon-dark.png
- Provenance: research/web/langchain-memory/assets/observability-icon-dark.png ← mintcdn brand asset (no alt); 200x200 PNG. Icon on the "Debug with LangSmith" card.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

## Raw / preserved excerpts

> LangChain provides create_agent: a minimal, highly configurable agent harness. Compose exactly the agent your use case needs from model, tools, prompt, and middleware.

> **Agent = Model + Harness.** LangChain provides `create_agent`: a minimal, highly configurable harness. The harness is everything around the model loop: the prompt, the tools, and any middleware that shapes behavior. Start with the primitives and compose exactly what your use case needs. Supports OpenAI, Anthropic, Google, and more. **LangChain vs. LangGraph vs. Deep Agents** Start with Deep Agents for a "batteries-included" agent with features like automatic context compression, a virtual filesystem, and subagent-spawning. Deep Agents are built on LangChain agents which you can also use directly. Use LangChain (`create_agent`) for a highly customizable harness, easily tailored to your use case and data. Use LangGraph, our low-level orchestration framework, for advanced needs combining deterministic and agentic workflows. Use LangSmith to trace, debug, and evaluate agents built with any of these frameworks.

```python
# pip install -qU langchain "langchain[openai]"
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
```

(The other nine provider tabs repeat this code verbatim, changing only the `pip install` comment and the `model=` string listed under Evidence; the Azure tab builds the model with `init_chat_model("azure_openai:gpt-5.5", azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"])`.)

> ## Standard model interface
> Use one interface for chat models, embeddings, and more across providers. Switch models with minimal code changes and keep your application portable as requirements evolve.
>
> ## Highly configurable harness
> Start with `create_agent` as a minimal harness and add capabilities incrementally through middleware. Compose only what your use case needs, from guardrails and retries to routing and custom tool policies.
>
> ## Built on top of LangGraph
> LangChain's agents are built on top of LangGraph. This allows us to take advantage of LangGraph's durable execution, human-in-the-loop support, persistence, and more.
>
> ## Debug with LangSmith
> Inspect traces, tool calls, state transitions, and latency in one place. Find failure modes, evaluate quality, and improve agent behavior with execution data.
