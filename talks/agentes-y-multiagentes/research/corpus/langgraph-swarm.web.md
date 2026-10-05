---
source_file: langgraph-swarm/
source_type: web-capture
ingested_at: 2026-10-04
---

# LangGraph Multi-Agent Swarm (langgraph-swarm-py) — GitHub README

## Provenance
- Original location: research/web/langgraph-swarm/ (page.md; metadata.yaml; assets/)
- Format: html (GitHub repository page captured via talksmith:ingest; page.md used as text input — 14608 bytes, 36 headings, no fallback needed)
- URL: https://github.com/langchain-ai/langgraph-swarm-py
- Fetched at: 2026-10-04T19:21:35Z (HTTP 200, 356280 bytes original.html)
- Page title: "GitHub - langchain-ai/langgraph-swarm-py: For your multi-agent needs"
- Author / source (if known): LangChain (langchain-ai organization). MIT license.
- Date of original (if known): not stated. Repo stats at capture: 57 commits, 1.6k stars, 225 forks, 14 watching. Topics: agents, langgraph, llms, multiagent, multiagent-systems, python.

## Key claims
- "A Python library for creating swarm-style multi-agent systems using LangGraph."
- Definition: "A swarm is a type of multi-agent architecture where agents dynamically hand off control to one another based on their specializations. The system remembers which agent was last active, ensuring that on subsequent interactions, the conversation resumes with that agent."
- Features: multi-agent collaboration (agents "hand off context to each other"); customizable handoff tools.
- Built on LangGraph with out-of-box support for streaming, short-term and long-term memory, and human-in-the-loop.
- `create_swarm()` returns a `StateGraph` that must be compiled; a checkpointer (short-term memory) and a store (long-term memory) are passed to `.compile()`.
- "Adding short-term memory is crucial for maintaining conversation state across multiple interactions. Without it, the swarm would 'forget' which agent was last active and lose the conversation history."
- **Default context passing:** "by default `create_handoff_tool` passes **full** message history (all of the messages generated in the swarm up to this point), as well as a tool message indicating successful handoff."
- **Shared message list by default:** "individual agents are expected to communicate over a single `messages` key that is shared by all agents and the overall multi-agent swarm graph. This means that messages from **all** of the agents will be combined into a single, shared list of messages. This might not be desirable if you don't want to expose an agent's internal history of messages."
- To isolate an agent's history: use a custom state schema with a separate key (e.g. `alice_messages`) and a wrapper converting parent state ↔ child state.
- Custom handoff tools can add LLM-populated arguments (e.g. a `task_description` for the next agent) and return `Command(goto=agent_name, graph=Command.PARENT, update={...})`.
- Custom `Command`-returning handoff tools require (1) a tool-calling node that handles `Command` (e.g. prebuilt `ToolNode`) and (2) the target keys in both the swarm graph and the next agent's state schema.
- `add_active_agent_router` is "the router that enables us to keep track of the last active agent".

## Definitions and terminology
- **Swarm** (LangGraph sense): multi-agent architecture with dynamic peer-to-peer handoffs by specialization, remembering the last active agent.
- **`create_handoff_tool(agent_name, description)`**: prebuilt tool that transfers control to another agent.
- **`create_swarm(agents, default_active_agent)`**: builds the swarm `StateGraph`.
- **`active_agent`**: state key tracking the currently active agent.
- **`SwarmState`**: the swarm graph's state schema.
- **`add_active_agent_router`**: router that resumes at the last active agent.
- **Checkpointer** (`InMemorySaver`): short-term memory (conversation state per `thread_id`).
- **Store** (`InMemoryStore`): long-term memory.
- **`Command`**: LangGraph primitive combining a state update and a `goto` routing decision; `graph=Command.PARENT` applies it to the parent graph.
- **`InjectedState` / `InjectedToolCallId`**: annotations injecting graph state / tool call id into a tool without the LLM populating them.

## Evidence and examples
- Quickstart: Alice ("an addition expert", with an `add` tool and handoff to Bob) and Bob ("you speak like a pirate", handoff to Alice); `create_swarm([alice, bob], default_active_agent="Alice")`; two turns on `thread_id "1"`: "i'd like to speak to Bob" then "what's 5 + 7?". Model in example: `ChatOpenAI(model="gpt-4o")`; agents created with `langchain.agents.create_agent`.
- Manual swarm construction with `StateGraph(SwarmState)`, nodes `Alice`/`Bob` with `destinations`, and `add_active_agent_router`.

## Inconsistencies / open questions
- [verified] Context isolation is NOT the default: the README states both the full-history handoff default and the single shared `messages` key — checked in "Customizing handoff tools" and "Customizing agent implementation" sections. Isolation requires custom state schemas.
- [verified] The "Features" bullet says agents "hand off context to each other", consistent with the full-history default — checked within page.md, no contradiction.
- [open question] Several links point to `langchain-ai.github.io/langgraph/...` concept pages; the LangGraph docs have since moved to docs.langchain.com (see langgraph-doc / langgraph-multi-agent captures) — whether those old links still resolve is unchecked.
- [verified] GitHub chrome and emoji headers are present in page.md — ignored except for repo stats.

## Images / diagrams

### langgraph-swarm.web/images/swarm.png
- Provenance: research/web/langgraph-swarm/assets/swarm.png ← https://github.com/langchain-ai/langgraph-swarm-py/raw/main/static/img/swarm.png (alt "Swarm"); 1708x1024 PNG. Shown directly after the swarm definition at the top of the README.
- Depiction: Hand-drawn diagram titled "Multi-Agent Swarm". Left column: a human emoji at a laptop labelled "Human", with a vertical "Time" arrow pointing down, and a stack of 8 message boxes alternating user (white) and agent replies (pink for flight agent, blue for hotel agent): Book me a flight → Here is a flight (pink) → Ok, let's book it! → It's booked (pink) → Book me a hotel → Here is a hotel (blue) → Ok, let's book it! → It's booked (blue). Arrows point right for user turns and left for agent replies. Right: a large rounded frame split by a dashed vertical line into two lanes, "Flight agent" (pink circle) and "Hotel agent" (blue circle). In the flight lane, the red label "Flight Agent Active" sits above the pink boxes Here is a flight, It's booked, and Handoff tool; an arrow from "Handoff tool" crosses the dashed line to the blue label "Hotel Agent Active", under which are the blue boxes Here is a hotel and It's booked. At the top of the hotel lane, greyed-out ghost boxes (Book me a flight, Here is a flight, Book me a hotel, It's booked) indicate the earlier conversation history visible to the hotel agent but not produced by it.
- Why it matters: Shows the defining property of the swarm architecture: one agent is "active" at a time, control passes via a handoff tool, and the system remembers which agent was last active so the next user turn goes straight to it (no supervisor in the loop). The greyed boxes illustrate shared message history across the handoff. Good contrast slide against the supervisor/subagents pattern.
- Transcribed text: Multi-Agent Swarm · Human · Time · Flight agent · Hotel agent · Book me a flight · Here is a flight · Ok, let's book it! · It's booked · Book me a hotel · Here is a hotel · Ok, let's book it! · It's booked · Flight Agent Active · Handoff tool · Hotel Agent Active · (ghost, greyed) Book me a flight · Here is a flight · Book me a hotel · It's booked

## Raw / preserved excerpts

> A Python library for creating swarm-style multi-agent systems using LangGraph. A swarm is a type of multi-agent architecture where agents dynamically hand off control to one another based on their specializations. The system remembers which agent was last active, ensuring that on subsequent interactions, the conversation resumes with that agent.

> - **Multi-agent collaboration** - Enable specialized agents to work together and hand off context to each other
> - **Customizable handoff tools** - Built-in tools for communication between agents
>
> This library is built on top of LangGraph, a powerful framework for building agent applications, and comes with out-of-box support for streaming, short-term and long-term memory and human-in-the-loop

```python
from langchain_openai import ChatOpenAI

from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from langgraph_swarm import create_handoff_tool, create_swarm

model = ChatOpenAI(model="gpt-4o")

def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

alice = create_agent(
    model,
    tools=[
        add,
        create_handoff_tool(
            agent_name="Bob",
            description="Transfer to Bob",
        ),
    ],
    system_prompt="You are Alice, an addition expert.",
    name="Alice",
)

bob = create_agent(
    model,
    tools=[
        create_handoff_tool(
            agent_name="Alice",
            description="Transfer to Alice, she can help with math",
        ),
    ],
    system_prompt="You are Bob, you speak like a pirate.",
    name="Bob",
)

checkpointer = InMemorySaver()
workflow = create_swarm(
    [alice, bob],
    default_active_agent="Alice"
)
app = workflow.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "1"}}
turn_1 = app.invoke(
    {"messages": [{"role": "user", "content": "i'd like to speak to Bob"}]},
    config,
)
print(turn_1)
turn_2 = app.invoke(
    {"messages": [{"role": "user", "content": "what's 5 + 7?"}]},
    config,
)
print(turn_2)
```

> ## Memory
>
> You can add short-term and long-term memory to your swarm multi-agent system. Since `create_swarm()` returns an instance of `StateGraph` that needs to be compiled before use, you can directly pass a checkpointer or a store instance to the `.compile()` method:

```python
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore

# short-term memory
checkpointer = InMemorySaver()
# long-term memory
store = InMemoryStore()

model = ...
alice = ...
bob = ...

workflow = create_swarm(
    [alice, bob],
    default_active_agent="Alice"
)

# Compile with checkpointer/store
app = workflow.compile(
    checkpointer=checkpointer,
    store=store
)
```

> Important
>
> Adding short-term memory is crucial for maintaining conversation state across multiple interactions. Without it, the swarm would "forget" which agent was last active and lose the conversation history. Make sure to always compile the swarm with a checkpointer if you plan to use it in multi-turn conversations; e.g., `workflow.compile(checkpointer=checkpointer)`.

> ### Customizing handoff tools
>
> By default, the agents in the swarm are assumed to use handoff tools created with the prebuilt `create_handoff_tool`. You can also create your own, custom handoff tools. Here are some ideas on how you can modify the default implementation:
>
> - change tool name and/or description
> - add tool call arguments for the LLM to populate, for example a task description for the next agent
> - change what data is passed to the next agent as part of the handoff: by default `create_handoff_tool` passes **full** message history (all of the messages generated in the swarm up to this point), as well as a tool message indicating successful handoff.

```python
from typing import Annotated

from langchain.tools import tool, BaseTool, InjectedToolCallId
from langchain.messages import ToolMessage
from langgraph.types import Command
from langgraph.prebuilt import InjectedState

def create_custom_handoff_tool(*, agent_name: str, name: str | None, description: str | None) -> BaseTool:

    @tool(name, description=description)
    def handoff_to_agent(
        # you can add additional tool call arguments for the LLM to populate
        # for example, you can ask the LLM to populate a task description for the next agent
        task_description: Annotated[str, "Detailed description of what the next agent should do, including all of the relevant context."],
        # you can inject the state of the agent that is calling the tool
        state: Annotated[dict, InjectedState],
        tool_call_id: Annotated[str, InjectedToolCallId],
    ):
        tool_message = ToolMessage(
            content=f"Successfully transferred to {agent_name}",
            name=name,
            tool_call_id=tool_call_id,
        )
        # you can use a different messages state key here, if your agent uses a different schema
        # e.g., "alice_messages" instead of "messages"
        messages = state["messages"]
        return Command(
            goto=agent_name,
            graph=Command.PARENT,
            # NOTE: this is a state update that will be applied to the swarm multi-agent graph (i.e., the PARENT graph)
            update={
                "messages": messages + [tool_message],
                "active_agent": agent_name,
                # optionally pass the task description to the next agent
                "task_description": task_description,
            },
        )

    return handoff_to_agent
```

> Important
>
> If you are implementing custom handoff tools that return `Command`, you need to ensure that:
> (1) your agent has a tool-calling node that can handle tools returning `Command` (like LangGraph's prebuilt `ToolNode`)
> (2) both the swarm graph and the next agent graph have the state schema containing the keys you want to update in `Command.update`

> ### Customizing agent implementation
>
> By default, individual agents are expected to communicate over a single `messages` key that is shared by all agents and the overall multi-agent swarm graph. This means that messages from **all** of the agents will be combined into a single, shared list of messages. This might not be desirable if you don't want to expose an agent's internal history of messages. To change this, you can customize the agent by taking the following steps:
>
> 1. use custom state schema with a different key for messages, for example `alice_messages`
> 2. write a wrapper that converts the parent graph state to the child agent state and back (see this how-to guide)

```python
from typing_extensions import TypedDict, Annotated

from langchain.messages import AnyMessage
from langgraph.graph import StateGraph, add_messages
from langgraph_swarm import SwarmState

class AliceState(TypedDict):
    alice_messages: Annotated[list[AnyMessage], add_messages]

# see this guide to learn how you can implement a custom tool-calling agent
# https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/
alice = (
    StateGraph(AliceState)
    .add_node("model", ...)
    .add_node("tools", ...)
    .add_edge(...)
    ...
    .compile()
)

# wrapper calling the agent
def call_alice(state: SwarmState):
    # you can put any input transformation from parent state -> agent state
    # for example, you can invoke "alice" with "task_description" populated by the LLM
    response = alice.invoke({"alice_messages": state["messages"]})
    # you can put any output transformation from agent state -> parent state
    return {"messages": response["alice_messages"]}

def call_bob(state: SwarmState):
    ...
```

```python
from langgraph_swarm import add_active_agent_router

workflow = (
    StateGraph(SwarmState)
    .add_node("Alice", call_alice, destinations=("Bob",))
    .add_node("Bob", call_bob, destinations=("Alice",))
)
# this is the router that enables us to keep track of the last active agent
workflow = add_active_agent_router(
    builder=workflow,
    route_to=["Alice", "Bob"],
    default_active_agent="Alice",
)

# compile the workflow
app = workflow.compile()
```
