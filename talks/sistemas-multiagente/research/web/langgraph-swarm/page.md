# GitHub - langchain-ai/langgraph-swarm-py: For your multi-agent needs · GitHub

_Source: <https://github.com/langchain-ai/langgraph-swarm-py>_

[Skip to content](#start-of-content) 

## Navigation Menu

</>[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Flangchain-ai%2Flanggraph-swarm-py)Appearance settingsSearch/[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Flangchain-ai%2Flanggraph-swarm-py)[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=langchain-ai%2Flanggraph-swarm-py)Appearance settings You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert {{ message }} [langchain-ai](/langchain-ai) / ** [langgraph-swarm-py](/langchain-ai/langgraph-swarm-py) ** Public 

- [Notifications](/login?return_to=%2Flangchain-ai%2Flanggraph-swarm-py) You must be signed in to change notification settings 
- [Fork 225](/login?return_to=%2Flangchain-ai%2Flanggraph-swarm-py) 
- [Star 1.6k](/login?return_to=%2Flangchain-ai%2Flanggraph-swarm-py) 
</langchain-ai/langgraph-swarm-py> main[Branches](/langchain-ai/langgraph-swarm-py/branches)[Tags](/langchain-ai/langgraph-swarm-py/tags)</langchain-ai/langgraph-swarm-py/branches></langchain-ai/langgraph-swarm-py/tags>Go to fileCodeOpen more actions menu

## Latest commit

## History

[57 Commits](/langchain-ai/langgraph-swarm-py/commits/main/)</langchain-ai/langgraph-swarm-py/commits/main/>57 Commits

## Folders and files

NameNameLast commit messageLast commit date[.github](/langchain-ai/langgraph-swarm-py/tree/main/.github)[.github](/langchain-ai/langgraph-swarm-py/tree/main/.github) [examples](/langchain-ai/langgraph-swarm-py/tree/main/examples)[examples](/langchain-ai/langgraph-swarm-py/tree/main/examples) [langgraph_swarm](/langchain-ai/langgraph-swarm-py/tree/main/langgraph_swarm)[langgraph_swarm](/langchain-ai/langgraph-swarm-py/tree/main/langgraph_swarm) [static/img](/langchain-ai/langgraph-swarm-py/tree/main/static/img)[static/img](/langchain-ai/langgraph-swarm-py/tree/main/static/img) [tests](/langchain-ai/langgraph-swarm-py/tree/main/tests)[tests](/langchain-ai/langgraph-swarm-py/tree/main/tests) [.gitignore](/langchain-ai/langgraph-swarm-py/blob/main/.gitignore)[.gitignore](/langchain-ai/langgraph-swarm-py/blob/main/.gitignore) [LICENSE](/langchain-ai/langgraph-swarm-py/blob/main/LICENSE)[LICENSE](/langchain-ai/langgraph-swarm-py/blob/main/LICENSE) [Makefile](/langchain-ai/langgraph-swarm-py/blob/main/Makefile)[Makefile](/langchain-ai/langgraph-swarm-py/blob/main/Makefile) [README.md](/langchain-ai/langgraph-swarm-py/blob/main/README.md)[README.md](/langchain-ai/langgraph-swarm-py/blob/main/README.md) [pyproject.toml](/langchain-ai/langgraph-swarm-py/blob/main/pyproject.toml)[pyproject.toml](/langchain-ai/langgraph-swarm-py/blob/main/pyproject.toml) [uv.lock](/langchain-ai/langgraph-swarm-py/blob/main/uv.lock)[uv.lock](/langchain-ai/langgraph-swarm-py/blob/main/uv.lock) View all files

## Repository files navigation

# 🤖 LangGraph Multi-Agent Swarm

<#-langgraph-multi-agent-swarm> 

A Python library for creating swarm-style multi-agent systems using [LangGraph](https://github.com/langchain-ai/langgraph). A swarm is a type of [multi-agent](https://langchain-ai.github.io/langgraph/concepts/multi_agent) architecture where agents dynamically hand off control to one another based on their specializations. The system remembers which agent was last active, ensuring that on subsequent interactions, the conversation resumes with that agent.

![Swarm](/langchain-ai/langgraph-swarm-py/raw/main/static/img/swarm.png)</langchain-ai/langgraph-swarm-py/blob/main/static/img/swarm.png>

## Features

<#features> 

- 🤖 **Multi-agent collaboration** - Enable specialized agents to work together and hand off context to each other 
- 🛠️ **Customizable handoff tools** - Built-in tools for communication between agents 

This library is built on top of [LangGraph](https://github.com/langchain-ai/langgraph), a powerful framework for building agent applications, and comes with out-of-box support for [streaming](https://langchain-ai.github.io/langgraph/how-tos/#streaming), [short-term and long-term memory](https://langchain-ai.github.io/langgraph/concepts/memory/) and [human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)

## Installation

<#installation> 

```
pip install langgraph-swarm
```

## Quickstart

<#quickstart> 

```
pip install langgraph-swarm langchain-openai

export OPENAI_API_KEY=<your_api_key>
```

```
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

Tip

For developing, debugging, and deploying AI agents and LLM applications, see [LangSmith](https://docs.langchain.com/langsmith/home).

## Memory

<#memory> 

You can add [short-term](https://langchain-ai.github.io/langgraph/how-tos/persistence/) and [long-term](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence/) [memory](https://langchain-ai.github.io/langgraph/concepts/memory/) to your swarm multi-agent system. Since `create_swarm()` returns an instance of `StateGraph` that needs to be compiled before use, you can directly pass a [checkpointer](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver) or a [store](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) instance to the `.compile()` method:

```
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

Important

Adding [short-term memory](https://langchain-ai.github.io/langgraph/concepts/persistence/) is crucial for maintaining conversation state across multiple interactions. Without it, the swarm would "forget" which agent was last active and lose the conversation history. Make sure to always compile the swarm with a checkpointer if you plan to use it in multi-turn conversations; e.g., `workflow.compile(checkpointer=checkpointer)`.

## How to customize

<#how-to-customize> 

You can customize multi-agent swarm by changing either the [handoff tools](#customizing-handoff-tools) implementation or the [agent implementation](#customizing-agent-implementation).

### Customizing handoff tools

<#customizing-handoff-tools> 

By default, the agents in the swarm are assumed to use handoff tools created with the prebuilt `create_handoff_tool`. You can also create your own, custom handoff tools. Here are some ideas on how you can modify the default implementation:

- change tool name and/or description 
- add tool call arguments for the LLM to populate, for example a task description for the next agent 
- change what data is passed to the next agent as part of the handoff: by default `create_handoff_tool` passes **full** message history (all of the messages generated in the swarm up to this point), as well as a tool message indicating successful handoff. 

Here is an example of what a custom handoff tool might look like:

```
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

Important

If you are implementing custom handoff tools that return `Command`, you need to ensure that:  
 (1) your agent has a tool-calling node that can handle tools returning `Command` (like LangGraph's prebuilt ``[ToolNode](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.ToolNode))  
 (2) both the swarm graph and the next agent graph have the [state schema](https://langchain-ai.github.io/langgraph/concepts/low_level#schema) containing the keys you want to update in `Command.update`

### Customizing agent implementation

<#customizing-agent-implementation> 

By default, individual agents are expected to communicate over a single `messages` key that is shared by all agents and the overall multi-agent swarm graph. This means that messages from **all** of the agents will be combined into a single, shared list of messages. This might not be desirable if you don't want to expose an agent's internal history of messages. To change this, you can customize the agent by taking the following steps:

1. use custom [state schema](https://langchain-ai.github.io/langgraph/concepts/low_level#schema) with a different key for messages, for example `alice_messages` 
2. write a wrapper that converts the parent graph state to the child agent state and back (see this [how-to](https://langchain-ai.github.io/langgraph/how-tos/subgraph-transform-state/) guide) 

```
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

Then, you can create the swarm manually in the following way:

```
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

## About

For your multi-agent needs

[langchain-ai.github.io/langgraph/concepts/multi_agent/](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)

### Topics

[agents](/topics/agents)[langgraph](/topics/langgraph)[llms](/topics/llms)[multiagent](/topics/multiagent)[multiagent-systems](/topics/multiagent-systems)[python](/topics/python)

### Resources

[Readme](#readme-ov-file)[MIT license](#MIT-1-ov-file)

### Code of conduct

[Code of conduct](/langchain-ai/langgraph-swarm-py#coc-ov-file)

### Contributing

[Contributing](#contributing-ov-file)

### Security policy

[Security policy](#security-ov-file)[Activity](/langchain-ai/langgraph-swarm-py/activity)[Custom properties](/langchain-ai/langgraph-swarm-py/custom-properties)

### Stars

**1.6k** stars

### Watchers

**14** watching

### Forks

****[225 forks](/langchain-ai/langgraph-swarm-py/forks)[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Flangchain-ai%2Flanggraph-swarm-py&report=langchain-ai+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

 You can’t perform that action at this time.
