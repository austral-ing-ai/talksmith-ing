---
source_file: medium-react-langgraph-agent/
source_type: web-capture
ingested_at: 2026-10-04
---

# Building a ReAct LangGraph Agent: The Future of Reasoning-Centric AI Workflows (Medium, Datadivaai)

## Provenance
- Original location: `research/web/medium-react-langgraph-agent/` (`page.md` used as text input; no fallback needed)
- Format: html (web capture via `talksmith:ingest`)
- **Cite as (canonical URL):** https://medium.com/@datadivaai/building-a-react-langgraph-agent-the-future-of-reasoning-centric-ai-workflows-bf270cc756fa
- Captured via mirror: medium.com returned HTTP 403, so the page was fetched from the Freedium mirror at https://freedium-mirror.cfd/https://medium.com/@datadivaai/building-a-react-langgraph-agent-the-future-of-reasoning-centric-ai-workflows-bf270cc756fa (HTTP 200, 142,405 bytes). The "- Freedium" suffix in the captured title is the mirror's, not the author's.
- Fetched: 2026-10-04T14:02:29Z
- Author / source (if known): "Datadivaai" (Medium handle @datadivaai); companion code at https://github.com/datadivaai/GenAI/tree/main/ReActAgentFolder
- Date of original (if known): July 31, 2025 (as shown in the mirror's header; "2 min read")
- Presenter-provided.

## Key claims
- AI agents are moving beyond static prompt→response toward **reasoning, planning, and action** stitched together in structured workflows; ReAct + LangGraph is presented as the way to get there.
- **ReAct** (Reasoning and Acting) is "a prompting technique introduced by researchers at Google" that lets agents:
  - interleave **thoughts (reasoning)** and **actions**;
  - use tools (search, calculators, databases) mid-conversation;
  - keep a traceable "chain of thought" for transparency and error recovery.
- **LangGraph** is a LangChain library for "stateful, event-driven agents" using graph-based computation: a directed graph of nodes where each node can reason, call tools, or decide; loops and branching are native; state is tracked across the session.
- ReAct + LangGraph gives: structured reasoning (think, plan, revise), tool use, looping/branches (retry, multi-hop), memory/state, debuggability (trace the graph and every decision).
- The walkthrough builds an agent that: (1) receives a question, (2) thinks about needed tools, (3) calls tools (Wikipedia search, math), (4) loops until it has the final answer, (5) exits.
- The core ReAct loop in LangGraph = an `agent` node (LLM with tools bound) + a `tools` node (`ToolNode`) + a conditional edge: if the last message has no `tool_calls` → END, otherwise → tools → back to agent.
- Future extensions named: long-term memory, enterprise tools (SQL, APIs, private docs), multi-agent graphs ("e.g., Planner-Agent-Worker pattern").

## Definitions and terminology
- **ReAct** — Reasoning + Acting; Thought / Action / Observation trace, ending in a Final Answer.
- **LangGraph** — graph-based, stateful agent library from LangChain; `StateGraph`, nodes, edges, conditional edges, `END`, entry point.
- **Tool** — a Python function decorated with `@tool`; its docstring serves as the description given to the model.
- **`bind_tools`** — attaches tool schemas to a chat model so it can emit tool calls.
- **`AgentState`** — typed dict carrying the message list, merged with the `add_messages` reducer.
- **`ToolNode`** — prebuilt LangGraph node that executes the tool calls in the last message.

## Evidence and examples
- ReAct trace example (verbatim):
  ```
  Question: What is the population of France plus Germany?
  Thought: I need to look up the population of each country first.
  Action: Lookup("Population of France")
  Observation: France has 67 million people.
  Thought: Now I need the population of Germany.
  Action: Lookup("Population of Germany")
  ...
  Final Answer: 150 million
  ```
- "Why combine" table (reconstructed from the flattened `page.md` row):

  | Capability | Description |
  |---|---|
  | Structured reasoning | Agents can think, plan, and revise |
  | Tool use | Integrated tools like calculators, APIs |
  | Looping/branches | Retry logic, multi-hop questions |
  | Memory/state | Context persists across steps |
  | Debuggability | You can trace the graph and every decision |

- Full code walkthrough is preserved verbatim under Raw / preserved excerpts (six steps: install, tools, model, nodes, graph with loop, run). Model used: `ChatOpenAI(model="gpt-4o-mini")`.
- Teaching note (not a claim of the source): the `calculator` tool runs Python `eval()` on a model-generated string, which executes arbitrary code — fine for a demo, unsafe in production.

## Inconsistencies / open questions
- [verified] Every code block appears twice in a row in `page.md` (mirror rendering artifact, likely a copy-button duplicate); excerpts below keep one copy of each — checked by comparing consecutive fenced blocks, which are byte-identical.
- [verified] `is_done` is annotated `-> bool` but returns the strings `"end"` / `"continue"` — checked in the Step 5 snippet. (Its docstring also calls it a "node" though it is used as a routing function for a conditional edge.)
- [verified] The snippets are not runnable as shown: `TypedDict`, `Annotated`, `Sequence`, `BaseMessage`, `add_messages`, `SystemMessage`, `ToolNode` and `print_stream` are used but never imported/defined — checked against the import lines in Steps 2–5. The full code is said to be in the linked GitHub folder (not checked).
- [verified] "Features Recap" says "Powered by LangChain + OpenAI GPT-4", but the code uses `gpt-4o-mini` — checked against Step 3.
- [verified] The `search_wikipedia` docstring says "Simulates a Wikipedia lookup" but the body calls the real `wikipedia` library — checked in Step 2.
- [open question] "ReAct … introduced by researchers at Google" — the ReAct paper (arXiv 2210.03629, linked in the References) may list co-authors from other institutions too; settle by checking the paper's author affiliations before repeating the attribution on a slide.
- [open question] Publication date July 31, 2025 comes from the Freedium mirror header, not from medium.com directly — settle by opening the canonical Medium URL in a logged-in browser.
- [open question] The article is light on depth ("2 min read" per header) and is a tutorial/blog post, not a primary source — use for code illustration, cite the ReAct paper for the concept.

## Images / diagrams

### `medium-react-langgraph-agent.web/images/1-dmbNkD5D-u45r44go_cf0g.png`
- Provenance: rendered as a 48x48 rounded avatar next to "By Datadivaai" in the mirror's article header (HTML class `w-12 h-12 rounded-full`) — almost certainly the author's profile image, not an article figure. Mirror URL https://freedium-mirror.cfd/img/medium/700/1*dmbNkD5D-u45r44go_cf0g.png; original filename `1*dmbNkD5D-u45r44go_cf0g.png` (asterisk replaced with `-`).
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

## Raw / preserved excerpts

**Introduction**
> AI agents are evolving beyond simple prompts and static responses. Today's applications demand **reasoning**, **planning**, and **action** — all stitched together in real-time across structured workflows. This is where the **ReAct pattern** and **LangGraph** converge to deliver next-gen agentic behavior.
>
> In this post, I'll walk you through:
> - What ReAct and LangGraph are
> - Why their combination is powerful
> - How to implement a **ReAct LangGraph agent** in Python
> - Key features and use cases

**What is ReAct?**
> **ReAct** (Reasoning and Acting) is a prompting technique introduced by researchers at Google to enable agents to:
> - Interleave **thoughts (reasoning)** and **actions**
> - Use tools like search, calculators, or databases mid-conversation
> - Maintain a traceable "chain of thought" for transparency and error recovery

**What is LangGraph?**
> **LangGraph** is a library from **LangChain** that lets you build **stateful, event-driven agents** using graph-based computation.
>
> Instead of a linear chain of prompts → tools → outputs, LangGraph uses a **directed graph of nodes** where:
> - Each node can do reasoning, call tools, or make decisions
> - Loops and branching logic are native (ideal for multi-hop reasoning)
> - State is tracked across the session

**Code Walkthrough** (one copy of each duplicated block)

Step 1: Install LangGraph
```
pip install langchain langgraph openai
```

Step 2: Define Tools
```
from langchain.tools import tool
@tool
def calculator(expression: str) -> str:
    """Evaluates a math expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"
@tool
def search_wikipedia(query: str) -> str:
    """Simulates a Wikipedia lookup."""
    import wikipedia
    return wikipedia.summary(query, sentences=2)
```

Step 3: Define the ReAct Agent Node
```
from langchain_openai import ChatOpenAI
tools = [calculator, search_wikipedia]

model = ChatOpenAI(model="gpt-4o-mini").bind_tools(tools)
```

Step 4: Define LangGraph Nodes
```
from langgraph.graph import StateGraph, END
# This state will carry our conversation context
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
def agent_node(state: AgentState) -> AgentState:
    """
    This node will call the model and return the response.
    """
    system_prompt = SystemMessage(content="""
    You are a helpful assistant with various tools at your disposal. Please use the tools to answer my questions to the best of your ability.
    """)
    response = model.invoke([system_prompt] + state['messages'])

    return {"messages": [response]}
```

Step 5: Graph with Loops — "We'll build a graph that loops back to the agent until it signals it's done."
```
def is_done(state: AgentState) -> bool:
    """
    This node will determine if the agent should continue.
    """
    messages = state['messages']
    last_message = messages[-1]

    if not last_message.tool_calls:
        return "end"

    return "continue"
builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)

tool_node = ToolNode(tools=tools)
builder.add_node("tools", tool_node)

builder.set_entry_point("agent")
builder.add_conditional_edges(
    "agent",
    is_done,
    {
        "end": END,
        "continue": "tools"
    }
)
builder.add_edge("tools", "agent")
agent = builder.compile()
```

Step 6: Run the Agent
```
inputs = {"messages": [("user", "What is the population of France plus Germany?")]}
print_stream(agent.stream(inputs, stream_mode="values"))
```

**Features Recap**
> - Supports **multi-hop reasoning**
> - Integrates **tool use** like calculators, APIs, or web search
> - Built-in **control flow**: loops, conditionals, exit
> - Easy to **trace and debug**
> - Powered by **LangChain + OpenAI GPT-4**

**Future Possibilities**
> With ReAct + LangGraph, you can go further:
> - Add **long-term memory** (LangChain Memory)
> - Plug into **enterprise tools** (SQL, APIs, private docs)
> - Extend with **multi-agent graphs** (e.g., Planner-Agent-Worker pattern)

**References** (as listed): LangGraph Docs https://python.langchain.com/docs/langgraph · ReAct Paper https://arxiv.org/abs/2210.03629 · LangChain Agents https://python.langchain.com/docs/modules/agents/

**Closing Thoughts**
> This ReAct LangGraph agent is a blueprint for building intelligent, context-aware agents. Whether you're creating customer support bots, research assistants, or data copilots, this approach can dramatically improve how your systems reason and act.
