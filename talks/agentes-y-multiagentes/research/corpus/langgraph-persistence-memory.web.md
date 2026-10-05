---
source_file: langgraph-persistence-memory/
source_type: web-capture
ingested_at: 2026-10-04
---

# Persistence - Docs by LangChain (LangGraph)

## Provenance
- Original location: research/web/langgraph-persistence-memory/ (page.md; metadata.yaml; assets/)
- Format: html (Mintlify docs page captured via talksmith:ingest; page.md used as text input — 6289 bytes, 12 headings). The checkpointer-vs-store table is flattened in page.md and was reconstructed from that line.
- URL: https://docs.langchain.com/oss/python/langgraph/persistence
- Fetched at: 2026-08-14T16:57:50Z (HTTP 200, 810527 bytes original.html)
- Author / source (if known): LangChain Inc — official "Docs by LangChain" (LangGraph → Capabilities → Persistence). Edit link: https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/persistence.mdx
- Date of original (if known): not stated

## Key claims
- "LangGraph's persistence layer gives agents short-term memory through checkpointers and long-term memory through stores."
- Persistence matters "when an agent needs to continue a conversation, resume after an interruption, recover from a failure, or remember information across interactions."
- **Checkpointers** persist a thread's graph state as checkpoints → short-term, thread-scoped memory (conversation continuity, human-in-the-loop, time travel, fault tolerance).
- **Stores** persist application-defined data outside the graph state → long-term, cross-thread memory (user preferences, facts, shared knowledge).
- "Most applications can use both: a checkpointer tracks the current thread, and a store tracks durable information across threads."
- With the Agent Server, persistence is handled automatically.
- Troubleshooting: `PostgresSaver` `thread_id` must be < 255 chars; `MemorySaver`/`InMemorySaver` lose everything on restart (use `PostgresSaver` or `SqliteSaver`); checkpoints grow unboundedly in long conversations (prune / retention policy); **subgraph state isolation**: "When a subgraph updates state, the parent graph may not see the changes immediately. This is because each subgraph manages its own checkpoint namespace." Fix: shared state via Store, or configure the subgraph to write to the parent checkpoint.

## Definitions and terminology
- **Checkpointer**: persists graph state snapshots per thread (`thread_id`).
- **Checkpoint**: a snapshot of a thread's graph state.
- **Store**: application-defined key-value data across threads.
- **Thread** / **`thread_id`**: the scope of short-term memory (passed in `{"configurable": {"thread_id": ...}}`).
- **Checkpoint namespace**: per-subgraph namespace for checkpoints.
- **Time travel**: replay/inspect earlier checkpoints (listed as a checkpointer use).

## Evidence and examples

Checkpointer vs. store (reconstructed from the flattened table):

| | Checkpointer | Store |
|---|---|---|
| Persists | Graph state snapshots | Application-defined key-value data |
| Scope | A single thread | Across threads |
| Memory type | Short-term, thread-scoped memory | Long-term, cross-thread memory |
| Use for | Conversation continuity, human-in-the-loop, time travel, and fault tolerance | User preferences, facts, and shared knowledge |
| Access pattern | Pass a `thread_id` in graph config | Read and write items from nodes or application code |
| Full guide | Checkpointers | Stores |

## Inconsistencies / open questions
- [verified] Relevance for the talk: subgraphs (the LangGraph building block for nested agents) have their own checkpoint namespace, so parent/child state is not automatically shared — a framework-level form of context/state isolation; checked in the "State access from parent graph to subgraph" troubleshooting entry.
- [open question] "the parent graph may not see the changes immediately" is vague about when/whether it eventually sees them; the subgraphs guide (not captured) would settle it.
- [verified] Captured 2026-08-14 — checked in metadata.yaml.

## Images / diagrams
Only site-chrome logos were captured.

### langgraph-persistence-memory.web/images/langchain-docs-dark-blue.png
- Provenance: research/web/langgraph-persistence-memory/assets/langchain-docs-dark-blue.png ← mintcdn LangChain brand asset (alt "light logo"); 3889x507 PNG. Site header logo.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### langgraph-persistence-memory.web/images/langchain-docs-light-blue.png
- Provenance: research/web/langgraph-persistence-memory/assets/langchain-docs-light-blue.png ← mintcdn LangChain brand asset (alt "dark logo"); 3889x507 PNG. Site header logo (dark theme).
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

## Raw / preserved excerpts

> LangGraph's persistence layer gives agents short-term memory through checkpointers and long-term memory through stores.
>
> Persistence lets LangGraph applications keep useful information beyond a single graph run. It matters when an agent needs to continue a conversation, resume after an interruption, recover from a failure, or remember information across interactions. LangGraph provides two complementary persistence systems:
>
> - **Checkpointers** persist a thread's graph state as checkpoints. Use them for short-term, thread-scoped memory, including conversation continuity, human-in-the-loop workflows, time travel, and fault tolerance.
> - **Stores** persist application-defined data outside the graph state. Use them for long-term, cross-thread memory, including user preferences, facts, and shared knowledge.
>
> Most applications can use both: a checkpointer tracks the current thread, and a store tracks durable information across threads.

```python
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

> **Agent Server handles persistence automatically** When using the Agent Server, you do not need to implement or configure checkpointers or stores manually. The server handles persistence infrastructure behind the scenes.

> ### PostgresSaver: `thread_id` too long
> When using `PostgresSaver` (or `AsyncPostgresSaver`), the `thread_id` is stored in a column with limited length. If your `thread_id` exceeds the column size, you will see a database error. **Fix:** Keep `thread_id` values under 255 characters. Use a UUID or hash if you need deterministic IDs:

```python
import uuid

config = {"configurable": {"thread_id": str(uuid.uuid4())[:255]}}
```

> ### `MemorySaver` does not persist between restarts
> `MemorySaver` and `InMemorySaver` store checkpoints in RAM. When the process restarts, all checkpoints are lost. **Fix:** Use a persistent checkpointer for production:
> - `PostgresSaver`: PostgreSQL with async support
> - `SqliteSaver`: Local file-based storage for development
>
> ### Checkpoints growing unboundedly
> Over long conversations, checkpoints accumulate. This can increase latency and storage costs. **Fix:** Prune old checkpoints periodically or set a retention policy:

```python
from langgraph.checkpoint.postgres import PostgresSaver

checkpointer = PostgresSaver.from_conn_string("postgresql://...")
checkpointer.setup()  # Creates tables with indexes
# Consider adding a cron job to delete checkpoints older than N days
```

> ### State access from parent graph to subgraph
> When a subgraph updates state, the parent graph may not see the changes immediately. This is because each subgraph manages its own checkpoint namespace. **Fix:** Use shared state via Store for data that needs to cross graph boundaries, or configure your subgraph to write to the parent checkpoint.
