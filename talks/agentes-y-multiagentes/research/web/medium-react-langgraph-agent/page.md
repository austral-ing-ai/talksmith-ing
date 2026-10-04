# Building a ReAct LangGraph Agent: The Future of Reasoning-Centric AI Workflows - Freedium

_Source: <https://freedium-mirror.cfd/https://medium.com/@datadivaai/building-a-react-langgraph-agent-the-future-of-reasoning-centric-ai-workflows-bf270cc756fa>_

July 31, 2025

# Building a ReAct LangGraph Agent: The Future of Reasoning-Centric AI Workflows

Introduction

![](/img/medium/700/1*dmbNkD5D-u45r44go_cf0g.png) 

By Datadivaai

2 min read

Download article 

## Contents

15 

- [1Introduction](#introduction)
- [2What is ReAct?](#what-is-react)
- [3What is LangGraph?](#what-is-langgraph)
- [4Why Combine ReAct and LangGraph?](#why-combine-react-and-langgraph)
- [5Code Walkthrough: ReAct Agent with LangGraph](#code-walkthrough-react-agent-with-langgraph)
Show all 15 sections 

### Introduction

AI agents are evolving beyond simple prompts and static responses. Today's applications demand **reasoning**, **planning**, and **action** — all stitched together in real-time across structured workflows. This is where the **ReAct pattern** and **LangGraph** converge to deliver next-gen agentic behavior.

In this post, I'll walk you through:

- What ReAct and LangGraph are 
- Why their combination is powerful 
- How to implement a **ReAct LangGraph agent** in Python 
- Key features and use cases 

### What is ReAct?

**ReAct** (Reasoning and Acting) is a prompting technique introduced by researchers at Google to enable agents to:

- Interleave **thoughts (reasoning)** and **actions** 
- Use tools like search, calculators, or databases mid-conversation 
- Maintain a traceable "chain of thought" for transparency and error recovery 

It looks like this:

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

### What is LangGraph?

**LangGraph** is a library from **LangChain** that lets you build **stateful, event-driven agents** using graph-based computation.

Instead of a linear chain of prompts → tools → outputs, LangGraph uses a **directed graph of nodes** where:

- Each node can do reasoning, call tools, or make decisions 
- Loops and branching logic are native (ideal for multi-hop reasoning) 
- State is tracked across the session 

### Why Combine ReAct and LangGraph?

Together, **ReAct + LangGraph** gives you:

Capability Description Structured reasoning Agents can think, plan, and revise Tool use Integrated tools like calculators, APIs Looping/branches Retry logic, multi-hop questions Memory/state Context persists across steps Debuggability You can trace the graph and every decision

### Code Walkthrough: ReAct Agent with LangGraph

We'll build a ReAct LangGraph agent that can (you can download code from [https://github.com/datadivaai/GenAI/tree/main/ReActAgentFolder](https://github.com/datadivaai/GenAI/tree/main/ReActAgentFolder)):

1. Receive a user question 
2. Think about what tools it needs 
3. Call tools (like Wikipedia search, math functions) 
4. Loop until it has the final answer 
5. Exit 

### Step 1: Install LangGraph

```
pip install langchain langgraph openai
```

```
pip install langchain langgraph openai
```

### Step 2: Define Tools

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

### Step 3: Define the ReAct Agent Node

```
from langchain_openai import ChatOpenAI
tools = [calculator, search_wikipedia]

model = ChatOpenAI(model="gpt-4o-mini").bind_tools(tools)
```

```
from langchain_openai import ChatOpenAI
tools = [calculator, search_wikipedia]

model = ChatOpenAI(model="gpt-4o-mini").bind_tools(tools)
```

### Step 4: Define LangGraph Nodes

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

### Step 5: Graph with Loops

We'll build a graph that loops back to the agent until it signals it's done.

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

### Step 6: Run the Agent

```
inputs = {"messages": [("user", "What is the population of France plus Germany?")]}
print_stream(agent.stream(inputs, stream_mode="values"))
```

```
inputs = {"messages": [("user", "What is the population of France plus Germany?")]}
print_stream(agent.stream(inputs, stream_mode="values"))
```

### ✨ Features Recap

- Supports **multi-hop reasoning** 
- Integrates **tool use** like calculators, APIs, or web search 
- Built-in **control flow**: loops, conditionals, exit 
- Easy to **trace and debug** 
- Powered by **LangChain + OpenAI GPT-4** 

### Future Possibilities

With ReAct + LangGraph, you can go further:

- Add **long-term memory** (LangChain Memory) 
- Plug into **enterprise tools** (SQL, APIs, private docs) 
- Extend with **multi-agent graphs** (e.g., Planner-Agent-Worker pattern) 

### References

- [LangGraph Docs](https://python.langchain.com/docs/langgraph) 
- [ReAct Paper](https://arxiv.org/abs/2210.03629) 
- [LangChain Agents](https://python.langchain.com/docs/modules/agents/) 

### Closing Thoughts

This ReAct LangGraph agent is a blueprint for building intelligent, context-aware agents. Whether you're creating customer support bots, research assistants, or data copilots, this approach can dramatically improve how your systems reason and act.
