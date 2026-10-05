---
source_file: openai-agents-sdk-handoffs/
source_type: web-capture
ingested_at: 2026-10-04
---

# Handoffs - OpenAI Agents SDK

## Provenance
- Original location: research/web/openai-agents-sdk-handoffs/ (page.md; metadata.yaml)
- Format: html (captured via talksmith:ingest; page.md used as text input — 15355 bytes, 9 headings, no fallback needed)
- URL: https://openai.github.io/openai-agents-python/handoffs/
- Fetched at: 2026-10-04T19:21:26Z (HTTP 200, 100166 bytes original.html)
- Author / source (if known): OpenAI — official documentation of the OpenAI Agents SDK (Python)
- Date of original (if known): not stated on the page

## Key claims
- "Handoffs allow an agent to delegate tasks to another agent." Useful when agents specialize in distinct areas (customer support: order status, refunds, FAQs).
- "Handoffs are represented as tools to the LLM." A handoff to `Refund Agent` becomes a tool named `transfer_to_refund_agent`.
- Every agent has a `handoffs` param taking an `Agent` directly or a `Handoff` object built with `handoff()`. A plain Agent's `handoff_description` is appended to the default tool description.
- `handoff()` customization fields: `agent`, `tool_name_override` (default `transfer_to_<agent_name>`), `tool_description_override`, `on_handoff` (callback run when the handoff is invoked; receives agent context and optionally LLM-generated input), `input_type` (schema of handoff tool-call arguments), `input_filter` (filters the input the next agent receives), `is_enabled` (bool or function, dynamic enable/disable), `nest_handoff_history` (per-handoff override of RunConfig setting).
- `handoff()` always transfers to the specific agent passed in; for multiple destinations, register one handoff per destination and let the model choose. A custom `Handoff` only when your code must decide the destination at invocation time.
- `input_type` is for small model-decided metadata at handoff time (`reason`, `language`, `priority`, `summary`); it does not replace the next agent's main input nor choose the destination. Distinct from `RunContextWrapper.context` (application state/dependencies).
- Security/authorization: `is_enabled` is evaluated before the model returns handoff arguments, so it cannot authorize argument values; do authorization at the start of `on_handoff` and raise on failure, because "the SDK continues the transfer after `on_handoff` returns successfully". "Tool input guardrails apply to function tools, not handoffs."
- **Context on handoff:** "When a handoff occurs, it's as though the new agent takes over the conversation, and gets to see the entire previous conversation history." To change this, use an `input_filter` (receives and returns `HandoffInputData`).
- `HandoffInputData` fields: `input_history`, `pre_handoff_items`, `new_items`, `input_items`, `run_context`.
- Nested handoff history is opt-in beta, disabled by default: the runner compacts summarizable history into assistant summary segments wrapped in `<CONVERSATION HISTORY>`. Custom mapping via `RunConfig.handoff_history_mapper`.
- "Nested handoff history changes how the transcript is represented; it does not redact sensitive data." Tool arguments/outputs may remain in summaries; "Treat the receiving agent and its model provider as recipients of the forwarded history."
- Server-managed conversations (`conversation_id`, `previous_response_id`, `auto_previous_response_id`) do not support handoff input filters.
- Per-handoff `input_filter` takes precedence over `RunConfig.handoff_input_filter`.
- "Handoffs stay within a single run. Input guardrails still apply only to the first agent in the chain, and output guardrails only to the agent that produces the final output."
- `handoff_filters.remove_all_tools` removes structured tool items but "does not redact tool arguments or results already copied into ordinary messages or nested-history summaries".
- Recommended: include handoff information in agent prompts via `RECOMMENDED_PROMPT_PREFIX` or `prompt_with_handoff_instructions`.

## Definitions and terminology
- **Handoff**: delegation of the conversation to another agent; exposed to the LLM as a tool `transfer_to_<agent_name>`.
- **`Handoff` object / `handoff()` helper**: customizable handoff wrapper.
- **`on_handoff`**: callback executed when the handoff is invoked.
- **`input_type`**: Pydantic schema for handoff tool-call arguments (model-generated metadata).
- **`input_filter`**: function `HandoffInputData -> HandoffInputData` controlling what history the receiving agent sees.
- **`HandoffInputData`**: `input_history`, `pre_handoff_items`, `new_items`, `input_items`, `run_context`.
- **Nested handoff history**: beta feature compacting prior history into `<CONVERSATION HISTORY>` summary segments.
- **`RunContextWrapper.context`**: local application state and dependencies (not seen by the model as handoff input).
- **Guardrails** (input / output / tool): checks scoped respectively to first agent, final-output agent, and each function-tool call.

## Evidence and examples
- Basic usage: `triage_agent = Agent(name="Triage agent", handoffs=[billing_agent, handoff(refund_agent)])`.
- Escalation agent with `EscalationData(reason: str)` as `input_type`, logged in `on_handoff`.
- Example metadata: `{ "reason": "duplicate_charge", "priority": "high" }` from triage to refund agent.
- `FAQ agent` handoff with `input_filter=handoff_filters.remove_all_tools`.
- `Billing agent` instructions prefixed with `RECOMMENDED_PROMPT_PREFIX`.

## Inconsistencies / open questions
- [verified] Default context behaviour is full-history inheritance ("gets to see the entire previous conversation history"); context isolation must be opted into via `input_filter` / nested history — checked in the "Input filters" section of page.md. Relevant to the talk's context-isolation theme: handoffs in this SDK do NOT isolate context by default.
- [open question] Nested handoff history is labelled "opt-in beta" — its stability/default may have changed after the capture date (2026-10-04); re-checking the live docs would settle it.
- [verified] Code blocks in page.md carry `<#__codelineno-N-M>` line-anchor artifacts from the HTML renderer — checked in page.md; excerpts below strip those anchors without changing code.

## Images / diagrams
No images captured (metadata.yaml lists `assets: []`). Companion folder `openai-agents-sdk-handoffs.web/images/` exists and is empty.

## Raw / preserved excerpts

> Handoffs allow an agent to delegate tasks to another agent. This is particularly useful in scenarios where different agents specialize in distinct areas. For example, a customer support app might have agents that each specifically handle tasks like order status, refunds, FAQs, etc.
>
> Handoffs are represented as tools to the LLM. So if there's a handoff to an agent named `Refund Agent`, the tool would be named `transfer_to_refund_agent`.

```python
from agents import Agent, handoff

billing_agent = Agent(name="Billing agent")
refund_agent = Agent(name="Refund agent")

# (1)!
triage_agent = Agent(name="Triage agent", handoffs=[billing_agent, handoff(refund_agent)])
```

> 1. You can use the agent directly (as in `billing_agent`), or you can use the `handoff()` function.

> - `agent`: This is the agent to which things will be handed off.
> - `tool_name_override`: By default, the `Handoff.default_tool_name()` function is used, which resolves to `transfer_to_<agent_name>`. You can override this.
> - `tool_description_override`: Override the default tool description from `Handoff.default_tool_description()`
> - `on_handoff`: A callback function executed when the handoff is invoked. This is useful for things like kicking off some data fetching as soon as you know a handoff is being invoked. This function receives the agent context, and can optionally also receive LLM generated input. The input data is controlled by the `input_type` param.
> - `input_type`: The schema for the handoff tool-call arguments. When set, the parsed payload is passed to `on_handoff`.
> - `input_filter`: This lets you filter the input received by the next agent. See below for more.
> - `is_enabled`: Whether the handoff is enabled. This can be a boolean or a function that returns a boolean, allowing you to dynamically enable or disable the handoff at runtime.
> - `nest_handoff_history`: Optional per-handoff override for the RunConfig-level `nest_handoff_history` setting. If `None`, the value defined in the active run configuration is used instead.
>
> The `handoff()` helper always transfers control to the specific `agent` you passed in. If you have multiple possible destinations, register one handoff per destination and let the model choose among them. Use a custom `Handoff` only when your own handoff code must decide which agent to return at invocation time.

```python
from agents import Agent, handoff, RunContextWrapper


def on_handoff(ctx: RunContextWrapper[None]):
    print("Handoff called")


agent = Agent(name="My agent")

handoff_obj = handoff(
    agent=agent,
    on_handoff=on_handoff,
    tool_name_override="custom_handoff_tool",
    tool_description_override="Custom description",
)
```

> ## Handoff inputs
>
> In certain situations, you want the LLM to provide some data when it calls a handoff. For example, imagine a handoff to an "Escalation agent". You might want the model to provide a reason so you can log it.

```python
from pydantic import BaseModel

from agents import Agent, handoff, RunContextWrapper


class EscalationData(BaseModel):
    reason: str


async def on_handoff(ctx: RunContextWrapper[None], input_data: EscalationData):
    print(f"Escalation agent called with reason: {input_data.reason}")


agent = Agent(name="Escalation agent")

handoff_obj = handoff(
    agent=agent,
    on_handoff=on_handoff,
    input_type=EscalationData,
)
```

> `input_type` describes the arguments for the handoff tool call itself. The SDK exposes that schema to the model as the handoff tool's `parameters`, validates the returned JSON locally, and passes the parsed value to `on_handoff`.
>
> `is_enabled` is evaluated while the SDK prepares the available handoffs, before the model returns handoff arguments, so it cannot authorize values inside an argument-bearing handoff. When authorization depends on the parsed fields, perform the check at the start of `on_handoff`, before any application side effects. If authorization fails, raise instead of returning; the SDK continues the transfer after `on_handoff` returns successfully. Tool input guardrails apply to function tools, not handoffs.
>
> It does not replace the next agent's main input, and it does not choose a different destination. The `handoff()` helper still transfers to the specific agent you wrapped, and the receiving agent still sees the conversation history unless you change it with an `input_filter` or nested handoff history settings.
>
> `input_type` is also separate from `RunContextWrapper.context`. Use `input_type` for metadata the model decides at handoff time, not for application state or dependencies you already have locally.

> ### When to use `input_type`
>
> Use `input_type` when the handoff needs a small piece of model-generated metadata such as `reason`, `language`, `priority`, or `summary`. For example, a triage agent can hand off to a refund agent with `{ "reason": "duplicate_charge", "priority": "high" }`, and `on_handoff` can log or persist that metadata before the refund agent takes over.
>
> Choose a different mechanism when the goal is different:
>
> - Put existing application state and dependencies in `RunContextWrapper.context`. See the context guide.
> - Use `input_filter`, `RunConfig.nest_handoff_history`, or `RunConfig.handoff_history_mapper` if you want to change what history the receiving agent sees.
> - Register one handoff per destination if there are multiple possible specialists. `input_type` can add metadata to the chosen handoff, but it does not dispatch between destinations.
> - If you want structured input for a nested specialist without transferring the conversation, prefer `Agent.as_tool(parameters=...)`. See tools.

> ## Input filters
>
> When a handoff occurs, it's as though the new agent takes over the conversation, and gets to see the entire previous conversation history. If you want to change this, you can set an `input_filter`. An input filter is a function that receives the existing input via a `HandoffInputData`, and must return a new `HandoffInputData`.
>
> `HandoffInputData` includes:
>
> - `input_history`: the input history before `Runner.run(...)` started.
> - `pre_handoff_items`: items generated before the agent turn where the handoff was invoked.
> - `new_items`: items generated during the current turn, including the handoff call and handoff output items.
> - `input_items`: optional items to forward to the next agent instead of `new_items`, allowing you to filter model input while keeping `new_items` intact for session history.
> - `run_context`: the active `RunContextWrapper` at the time the handoff was invoked.
>
> Nested handoff history is available as an opt-in beta and is disabled by default while we stabilize it. When you enable `RunConfig.nest_handoff_history`, the runner compacts summarizable history into ordered assistant summary segments while preserving lossless message items in their original positions. Each generated summary segment uses the `<CONVERSATION HISTORY>` wrapper, and later handoffs flatten earlier generated segments before rebuilding the ordered transcript. Sessions, `RunState`, and `RunResult.to_input_list()` track exact message occurrences moved into this SDK-default history so those occurrences are not appended twice; separate identical messages are still preserved. You can provide your own mapping function via `RunConfig.handoff_history_mapper` to return the exact list of input items for the next agent instead of using the built-in segmentation. The opt-in applies only when neither the handoff's `input_filter` nor the active run's `RunConfig.handoff_input_filter` is set, so existing code that already customizes the payload (including the examples in this repository) keeps its current behavior without changes. You can override the nesting behaviour for a single handoff by passing `nest_handoff_history=True` or `False` to `handoff(...)`, which sets `Handoff.nest_handoff_history`. If you just need to change the wrapper text for generated summary segments, call `set_conversation_history_wrappers` before running your agents. Call `reset_conversation_history_wrappers` before a later run when you need to restore the default wrappers.
>
> Nested handoff history changes how the transcript is represented; it does not redact sensitive data. Tool-call arguments and tool outputs can remain in the generated assistant summary even when the corresponding structured tool items are no longer forwarded separately. Treat the receiving agent and its model provider as recipients of the forwarded history.
>
> For client-managed history, use an explicit `input_filter` or `RunConfig.handoff_input_filter` to select or redact the content that the receiving agent may see. If a custom filter also calls `nest_handoff_history`, sanitize `input_history`, `pre_handoff_items`, and `new_items` before that call. The helper builds nested history from those three fields and ignores any existing `input_items` override. Filtering only `input_items` can therefore leave excluded tool content in the generated summary.
>
> If the filter must preserve the original `new_items` for session history, the filter can instead call `nest_handoff_history` and sanitize the returned `input_history` before returning the nested result. Clearing or replacing only `input_items` after nesting does not remove content already included in `input_history`.
>
> Server-managed conversations (`conversation_id`, `previous_response_id`, or `auto_previous_response_id`) do not support handoff input filters; use a separate run with explicitly selected input when the receiving agent must not inherit that server-managed history. Do not reuse the original `conversation_id` or `previous_response_id` in that separate run.
>
> If both the handoff and the active `RunConfig.handoff_input_filter` define a filter, the per-handoff `input_filter` takes precedence for that specific handoff.
>
> Note
>
> Handoffs stay within a single run. Input guardrails still apply only to the first agent in the chain, and output guardrails only to the agent that produces the final output. Use tool guardrails when you need checks around each custom function-tool call inside the workflow.
>
> There are some common patterns (for example removing all tool calls from the history), which are implemented for you in `agents.extensions.handoff_filters`

```python
from agents import Agent, handoff
from agents.extensions import handoff_filters

agent = Agent(name="FAQ agent")

handoff_obj = handoff(
    agent=agent,
    input_filter=handoff_filters.remove_all_tools,  # (1)!
)
```

> 1. This will automatically remove all tool-related items from the history when `FAQ agent` is called.
>
> `remove_all_tools` removes structured tool items. It does not redact tool arguments or results already copied into ordinary messages or nested-history summaries. Use a custom input filter to remove or redact those message contents when needed.

> ## Recommended prompts
>
> To make sure that LLMs understand handoffs properly, we recommend including information about handoffs in your agents. We have a suggested prefix in `agents.extensions.handoff_prompt.RECOMMENDED_PROMPT_PREFIX`, or you can call `agents.extensions.handoff_prompt.prompt_with_handoff_instructions` to automatically add recommended data to your prompts.

```python
from agents import Agent
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

billing_agent = Agent(
    name="Billing agent",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
    <Fill in the rest of your prompt here>.""",
)
```
