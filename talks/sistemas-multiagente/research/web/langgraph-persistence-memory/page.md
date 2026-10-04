# Persistence - Docs by LangChain

_Source: <https://docs.langchain.com/oss/python/langgraph/persistence>_

> 

## Documentation Index

Fetch the complete documentation index at: [/llms.txt](/llms.txt)

Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

Interrupt is coming to NYC and London this fall. Join the builders, engineers, and teams shaping what's next for agents. [Get your tickets →](https://interrupt.langchain.com/)

![light logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-dark-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=5babf1a1962208fd7eed942fa2432ecb)![dark logo](https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-docs-light-blue.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=0bcd2a1f2599ed228bcedf0f535b45b1)[Docs by LangChain home page](/)BuildSearch...⌘KSearch...NavigationCapabilitiesPersistence[Overview](/build-overview)[Deep Agents](/oss/python/deepagents/overview)[Managed Deep Agents](/langsmith/python/managed-deep-agents-overview)[LangChain](/oss/python/langchain/overview)[LangGraph](/oss/python/langgraph/overview)[OpenWiki](/oss/openwiki/overview)[Integrations](/oss/python/integrations/providers/overview)[Learn](/oss/python/learn)[Reference](/oss/python/reference/overview)[Contribute](/oss/python/contributing/overview)[Capabilities](/oss/python/langgraph/persistence)

# Persistence

Copy pageCopy page

LangGraph’s persistence layer gives agents short-term memory through checkpointers and long-term memory through stores.

Copy pageCopy page Persistence lets LangGraph applications keep useful information beyond a single graph run. It matters when an agent needs to continue a conversation, resume after an interruption, recover from a failure, or remember information across interactions. LangGraph provides two complementary persistence systems: 

- **[Checkpointers](/oss/python/langgraph/checkpointers)** persist a thread’s graph state as checkpoints. Use them for short-term, thread-scoped memory, including conversation continuity, human-in-the-loop workflows, time travel, and fault tolerance. 
- **[Stores](/oss/python/langgraph/stores)** persist application-defined data outside the graph state. Use them for long-term, cross-thread memory, including user preferences, facts, and shared knowledge. 
Most applications can use both: a [checkpointer](/oss/python/langgraph/checkpointers) tracks the current thread, and a [store](/oss/python/langgraph/stores) tracks durable information across threads. 

## [​](#quickstart)Quickstart

Compile your graph with a checkpointer, a store, or both: 

```
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore

checkpointer = InMemorySaver()
store = InMemoryStore()

graph = builder.compile(checkpointer=checkpointer, store=store)

result = graph.invoke(
    {"messages": [{"role": "user", "content": "Hi, my name is Bob."}]},
    {"configurable": {"thread_id": "thread-1"}},
)

```

**Agent Server handles persistence automatically** When using the [Agent Server](/langsmith/agent-server), you do not need to implement or configure checkpointers or stores manually. The server handles persistence infrastructure behind the scenes. 

## [​](#checkpointer-vs-store)Checkpointer vs. store

CheckpointerStorePersistsGraph state snapshotsApplication-defined key-value dataScopeA single threadAcross threadsMemory typeShort-term, thread-scoped memoryLong-term, cross-thread memoryUse forConversation continuity, human-in-the-loop, time travel, and fault toleranceUser preferences, facts, and shared knowledgeAccess patternPass a `thread_id` in graph configRead and write items from nodes or application codeFull guide[Checkpointers](/oss/python/langgraph/checkpointers)[Stores](/oss/python/langgraph/stores) 

## [​](#troubleshooting-common-issues)Troubleshooting common issues

### [​](#postgressaver-thread_id-too-long)PostgresSaver: `thread_id` too long

When using `PostgresSaver` (or `AsyncPostgresSaver`), the `thread_id` is stored in a column with limited length. If your `thread_id` exceeds the column size, you will see a database error. **Fix:** Keep `thread_id` values under 255 characters. Use a UUID or hash if you need deterministic IDs: 

```
import uuid

config = {"configurable": {"thread_id": str(uuid.uuid4())[:255]}}

```

### [​](#memorysaver-does-not-persist-between-restarts)`MemorySaver` does not persist between restarts

`MemorySaver` and `InMemorySaver` store checkpoints in RAM. When the process restarts, all checkpoints are lost. **Fix:** Use a persistent checkpointer for production: 

- `PostgresSaver`: PostgreSQL with async support 
- `SqliteSaver`: Local file-based storage for development 

### [​](#checkpoints-growing-unboundedly)Checkpoints growing unboundedly

Over long conversations, checkpoints accumulate. This can increase latency and storage costs. **Fix:** Prune old checkpoints periodically or set a retention policy: 

```
from langgraph.checkpoint.postgres import PostgresSaver

checkpointer = PostgresSaver.from_conn_string("postgresql://...")
checkpointer.setup()  # Creates tables with indexes
# Consider adding a cron job to delete checkpoints older than N days

```

### [​](#state-access-from-parent-graph-to-subgraph)State access from parent graph to subgraph

When a subgraph updates state, the parent graph may not see the changes immediately. This is because each subgraph manages its own checkpoint namespace. **Fix:** Use [shared state via Store](/oss/python/langgraph/stores) for data that needs to cross graph boundaries, or configure your subgraph to write to the parent checkpoint. 

## [​](#next-steps)Next steps

- [Use checkpointers](/oss/python/langgraph/checkpointers) to persist and inspect thread state. 
- [Use stores](/oss/python/langgraph/stores) to persist durable data across threads. 

---

[Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/persistence.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).

Was this page helpful?

YesNo⌘I
