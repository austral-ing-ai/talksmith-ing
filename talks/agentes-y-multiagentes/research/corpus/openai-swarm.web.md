---
source_file: openai-swarm/
source_type: web-capture
ingested_at: 2026-10-04
---

# OpenAI Swarm (experimental, educational) — GitHub README

## Provenance
- Original location: research/web/openai-swarm/ (page.md; metadata.yaml; assets/)
- Format: html (GitHub repository page captured via talksmith:ingest; page.md used as text input — 17833 bytes, 39 headings, no fallback needed)
- URL: https://github.com/openai/swarm
- Fetched at: 2026-10-04T19:21:31Z (HTTP 200, 393613 bytes original.html)
- Page title: "GitHub - openai/swarm: Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team."
- Author / source (if known): OpenAI Solution team. Core contributors listed: Ilan Bigio, James Hills, Shyamal Anadkat, Charu Jaiswal, Colin Jarvis, Katia Gil Guzman. MIT license.
- Date of original (if known): not stated in capture. Repo stats at capture: 29 commits, 22.0k stars, 2.3k forks, 298 watching.

## Key claims
- Swarm is "experimental, educational" and "is now replaced by the OpenAI Agents SDK, which is a production-ready evolution of Swarm". OpenAI recommends migrating to the Agents SDK for all production use cases.
- Swarm makes agent **coordination** and **execution** "lightweight, highly controllable, and easily testable" through two primitive abstractions: `Agent`s and **handoffs**.
- "An `Agent` encompasses `instructions` and `tools`, and can at any point choose to hand off a conversation to another `Agent`."
- Swarm is "entirely powered by the Chat Completions API and is hence stateless between calls"; it "runs (almost) entirely on the client". Swarm Agents are unrelated to Assistants in the Assistants API.
- Approaches like Swarm are "best suited for situations dealing with a large number of independent capabilities and instructions that are difficult to encode into a single prompt."
- `client.run()` loop: (1) get a completion from the current Agent; (2) execute tool calls and append results; (3) switch Agent if necessary; (4) update context variables if necessary; (5) if no new function calls, return.
- `client.run()` returns a `Response` with `messages` (with a `sender` field per message), the last `agent`, and updated `context_variables`; passing them back continues the interaction.
- An Agent need not be personified: it can represent "a very specific workflow or step", so agents, workflows and tasks are "all represented by the same primitive".
- **Context on handoff:** "Only the `instructions` of the active `Agent` will be present at any given time (e.g. if there is an `Agent` handoff, the `system` prompt will change, but the chat history will not.)"
- A function returning an `Agent` transfers execution to that Agent (this is the handoff mechanism). Functions can also return a `Result(value, agent, context_variables)`.
- If an Agent calls multiple handoff functions, only the last handoff is used.
- Function errors are appended to the chat so the agent can recover; multiple function calls execute in order.
- Functions are auto-converted to JSON Schema for Chat Completions `tools` (docstring → description; params without defaults → required; type hints → type, default `string`).
- Streaming adds `{"delim":"start"}`/`{"delim":"end"}` events per agent message, and a final `{"response": Response}` event.
- Evaluations: developers are encouraged to bring their own eval suites; examples in `airline`, `weather_agent`, `triage_agent`.

## Definitions and terminology
- **Agent** (Swarm): `instructions` + `functions` (+ settings); can hand off execution to another Agent.
- **Handoff** (Swarm): a function returning another `Agent`.
- **`context_variables`**: dict passed into `client.run()`, available to functions and instructions; updatable via `Result`.
- **`Result`**: return object combining `value`, `agent`, `context_variables`.
- **`Response`**: `messages`, `agent`, `context_variables`.
- **`run_demo_loop`**: REPL utility in `swarm/repl/repl.py`.

`client.run()` arguments (from README table): `agent` (Agent, required), `messages` (List, required), `context_variables` (dict, `{}`), `max_turns` (int, `float("inf")`), `model_override` (str, `None`), `execute_tools` (bool, `True` — if False, interrupts and returns `tool_calls`), `stream` (bool, `False`), `debug` (bool, `False`).

`Agent` fields: `name` (`"Agent"`), `model` (`"gpt-4o"`), `instructions` (str or `func() -> str`, `"You are a helpful agent."`), `functions` (`[]`), `tool_choice` (`None`).

## Evidence and examples
- Examples folder: `basic`, `triage_agent`, `weather_agent`, `airline` (multi-agent customer service for an airline), `support_bot` (user interface agent + help center agent), `personal_shopper` (sales and refunds).
- Usage example: Agent A with `transfer_to_agent_b`; Agent B "Only speak in Haikus."; output haiku "Hope glimmers brightly, / New paths converge gracefully, / What can I assist?"
- Sales handoff example returning `Sales Agent`; `Result` example yielding `{'department': 'sales', 'user_name': 'John'}`.

## Inconsistencies / open questions
- [verified] Swarm is deprecated in favour of the OpenAI Agents SDK — stated in the README's "Important" box in page.md. Any slide presenting Swarm should present it as historical/educational, not as a current production option.
- [verified] Context-handling contrast with the Agents SDK: in Swarm, on handoff the system prompt changes but "the chat history will not" (full history carried); the Agents SDK handoffs record also defaults to full history — checked in both captures. Consistent, not contradictory.
- [open question] Default `model` is listed as `"gpt-4o"`; whether the repo still uses that default after the capture is unknown and irrelevant for a deprecated project — re-checking the repo would settle it.
- [verified] GitHub navigation chrome (sign-in, file list, stars) is mixed into page.md — checked; ignored here except for the repo stats in Provenance.

## Images / diagrams

### openai-swarm.web/images/logo.png
- Provenance: research/web/openai-swarm/assets/logo.png ← https://github.com/openai/swarm/raw/main/assets/logo.png (alt "Swarm Logo"); 2148x544 PNG. Shown at the top of the README.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### openai-swarm.web/images/swarm_diagram.png
- Provenance: research/web/openai-swarm/assets/swarm_diagram.png ← https://github.com/openai/swarm/raw/main/assets/swarm_diagram.png (alt "Swarm Diagram"); 1938x770 PNG. Shown at the top of the "Documentation" section, before "Running Swarm".
- Depiction: Hand-drawn (Excalidraw-style) flow diagram of a single handoff. Left: user message box "What's the weather in ny"? with an arrow into an orange rounded box "Triage Assistant"; next to it a grey box with the tool call transfer_to_weather_assistant(). A downward arrow leads from Triage Assistant to a second orange box "Weather Assistant", next to which a grey box shows the tool call get_weather("New York City") and a green box with the tool result 67. An arrow goes from Weather Assistant back out to the left to the reply box "It's 67 degrees in New York." Agents are orange, tool calls grey, tool result green.
- Why it matters: The canonical picture of Swarm's two primitives (agents + handoffs): a handoff is just a tool call (transfer_to_...) that switches the active agent, and the agent that receives control is the one that answers the user directly — the triage agent never sees the final answer. Ready-made example for explaining handoff-as-tool-call vs. agents-as-tools.
- Transcribed text: "What's the weather in ny"? · Triage Assistant · transfer_to_weather_assistant() · Weather Assistant · get_weather("New York City") · 67 · It's 67 degrees in New York.

## Raw / preserved excerpts

> Swarm is now replaced by the OpenAI Agents SDK, which is a production-ready evolution of Swarm. The Agents SDK features key improvements and will be actively maintained by the OpenAI team.
>
> We recommend migrating to the Agents SDK for all production use cases.

```python
from swarm import Swarm, Agent

client = Swarm()

def transfer_to_agent_b():
    return agent_b

agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="Agent B",
    instructions="Only speak in Haikus.",
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to agent B."}],
)

print(response.messages[-1]["content"])
```

```
Hope glimmers brightly,
New paths converge gracefully,
What can I assist?
```

> # Overview
>
> Swarm focuses on making agent **coordination** and **execution** lightweight, highly controllable, and easily testable.
>
> It accomplishes this through two primitive abstractions: `Agent`s and **handoffs**. An `Agent` encompasses `instructions` and `tools`, and can at any point choose to hand off a conversation to another `Agent`.
>
> These primitives are powerful enough to express rich dynamics between tools and networks of agents, allowing you to build scalable, real-world solutions while avoiding a steep learning curve.
>
> Note
>
> Swarm Agents are not related to Assistants in the Assistants API. They are named similarly for convenience, but are otherwise completely unrelated. Swarm is entirely powered by the Chat Completions API and is hence stateless between calls.
>
> ## Why Swarm
>
> Swarm explores patterns that are lightweight, scalable, and highly customizable by design. Approaches similar to Swarm are best suited for situations dealing with a large number of independent capabilities and instructions that are difficult to encode into a single prompt.
>
> The Assistants API is a great option for developers looking for fully-hosted threads and built in memory management and retrieval. However, Swarm is an educational resource for developers curious to learn about multi-agent orchestration. Swarm runs (almost) entirely on the client and, much like the Chat Completions API, does not store state between calls.

> ### `client.run()`
>
> Swarm's `run()` function is analogous to the `chat.completions.create()` function in the Chat Completions API – it takes `messages` and returns `messages` and saves no state between calls. Importantly, however, it also handles Agent function execution, hand-offs, context variable references, and can take multiple turns before returning to the user.
>
> At its core, Swarm's `client.run()` implements the following loop:
>
> 1. Get a completion from the current Agent
> 2. Execute tool calls and append results
> 3. Switch Agent if necessary
> 4. Update context variables, if necessary
> 5. If no new function calls, return

> Once `client.run()` is finished (after potentially multiple calls to agents and tools) it will return a `Response` containing all the relevant updated state. Specifically, the new `messages`, the last `Agent` to be called, and the most up-to-date `context_variables`. You can pass these values (plus new user messages) in to your next execution of `client.run()` to continue the interaction where it left off – much like `chat.completions.create()`. (The `run_demo_loop` function implements an example of a full execution loop in `/swarm/repl/repl.py`.)

> ## Agents
>
> An `Agent` simply encapsulates a set of `instructions` with a set of `functions` (plus some additional settings below), and has the capability to hand off execution to another `Agent`.
>
> While it's tempting to personify an `Agent` as "someone who does X", it can also be used to represent a very specific workflow or step defined by a set of `instructions` and `functions` (e.g. a set of steps, a complex retrieval, single step of data transformation, etc). This allows `Agent`s to be composed into a network of "agents", "workflows", and "tasks", all represented by the same primitive.

> ### Instructions
>
> `Agent` `instructions` are directly converted into the `system` prompt of a conversation (as the first message). Only the `instructions` of the active `Agent` will be present at any given time (e.g. if there is an `Agent` handoff, the `system` prompt will change, but the chat history will not.)

> ## Functions
>
> - Swarm `Agent`s can call python functions directly.
> - Function should usually return a `str` (values will be attempted to be cast as a `str`).
> - If a function returns an `Agent`, execution will be transferred to that `Agent`.
> - If a function defines a `context_variables` parameter, it will be populated by the `context_variables` passed into `client.run()`.
>
> - If an `Agent` function call has an error (missing function, wrong argument, error) an error response will be appended to the chat so the `Agent` can recover gracefully.
> - If multiple functions are called by the `Agent`, they will be executed in that order.

```python
sales_agent = Agent(name="Sales Agent")

def transfer_to_sales():
   return sales_agent

agent = Agent(functions=[transfer_to_sales])

response = client.run(agent, [{"role":"user", "content":"Transfer me to sales."}])
print(response.agent.name)
```

```python
sales_agent = Agent(name="Sales Agent")

def talk_to_sales():
   print("Hello, World!")
   return Result(
       value="Done",
       agent=sales_agent,
       context_variables={"department": "sales"}
   )

agent = Agent(functions=[talk_to_sales])

response = client.run(
   agent=agent,
   messages=[{"role": "user", "content": "Transfer me to sales"}],
   context_variables={"user_name": "John"}
)
print(response.agent.name)
print(response.context_variables)
```

```
Sales Agent
{'department': 'sales', 'user_name': 'John'}
```

> Note
>
> If an `Agent` calls multiple functions to hand-off to an `Agent`, only the last handoff function will be used.

> Swarm automatically converts functions into a JSON Schema that is passed into Chat Completions `tools`.
>
> - Docstrings are turned into the function `description`.
> - Parameters without default values are set to `required`.
> - Type hints are mapped to the parameter's `type` (and default to `string`).
> - Per-parameter descriptions are not explicitly supported, but should work similarly if just added in the docstring. (In the future docstring argument parsing may be added.)

> ## Streaming
> Uses the same events as Chat Completions API streaming. [...] Two new event types have been added:
>
> - `{"delim":"start"}` and `{"delim":"end"}`, to signal each time an `Agent` handles a single message (response or function call). This helps identify switches between `Agent`s.
> - `{"response": Response}` will return a `Response` object at the end of a stream with the aggregated (complete) response, for convenience.

> # Evaluations
>
> Evaluations are crucial to any project, and we encourage developers to bring their own eval suites to test the performance of their swarms. For reference, we have some examples for how to eval swarm in the `airline`, `weather_agent` and `triage_agent` quickstart examples. See the READMEs for more details.
