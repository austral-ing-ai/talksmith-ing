---
source_file: lambert-rlhfbook-tool-use
source_type: web-capture
ingested_at: 2026-09-25
---

# Tool Use and Function Calling (chapter of "Reinforcement Learning from Human Feedback" by Nathan Lambert)

## Provenance
- Original location: web/lambert-rlhfbook-tool-use/ (text from `page.md`; `page.md` is 26339 chars with headings, so no `original.html` fallback was needed)
- Format: html (web capture via talksmith:ingest)
- URL: https://rlhfbook.com/c/13-tools
- Captured at: 2026-09-25T22:37:34Z
- Page title: Tool Use and Function Calling | RLHF and Post-Training Book by Nathan Lambert
- Author / source (if known): Nathan Lambert — chapter of the online book *Reinforcement Learning from Human Feedback* ("A short introduction to RLHF and post-training focused on language models"), rlhfbook.com; arXiv 2504.12501 (cs.LG); Manning edition *Reinforcement Learning from Human Feedback: Alignment and post-training of LLMs* (ISBN 9781633434301). Companion video: "Lecture 11: Tool Use, Function Calling and The Road to Agents".
- Date of original (if known): Not stated on the page as a posting date. Citation blocks give 2025 (web/arXiv version) and 2026 (Manning edition); the text contains a dated note "API formatting across providers (as of May 2026)", so this capture reflects a revision from May 2026 or later.
- Chapter position: URL `c/13-tools`; previous chapter "Synthetic Data & Distillation", next "Over-Optimization".

## Key claims
- "Language models using tools is a natural way to expand their capabilities, especially for high-precision tasks where external tools contain the information or for agents that need to interact with complex web systems."
- "Tool-use is a skill that language models need to be trained to have, and RLHF and all the other methods presented in this book can refine it."
- A model without tools struggles with "Who is the president today?" "due to the knowledge cutoff of pretraining data, but this is readily accessible information with one search query."
- Some tasks (e.g., moving arXiv papers in a downloads folder) "the model weights alone cannot even attempt – the use of tools enables language models to address a far broader range of tasks."
- Distinguishes tool use, function calling (schema-constrained, usually JSON Schema), and code execution (tool = code interpreter).
- "An AI model uses any external tools by outputting special tokens to trigger a certain endpoint."
- Tools serve two roles: supplying up-to-date information "to complement the fixed nature of their weights trained on past data", and code execution "which lets language models get around their probabilistic, generative nature and return precise answers" (e.g., pi to 50 digits "without reciting it from memory and risking hallucination").
- History: the idea predates the post-ChatGPT era — Neural Programmer-Interpreters (~2015), retrieval-augmented generation, web browsing (WebGPT), program-aided LMs (PAL), tool-augmented LMs (TALM); then Toolformer ("a calculator, a Q&A system, two different search engines, a translation system, and a calendar") and Gorilla (1645 APIs; APIBench → Berkeley Function Calling Leaderboard).
- "Tool-use models are now deeply intertwined with regular language model interactions"; MCP "emerged as a common formatting"; applications include productivity copilots (Microsoft Office, Google Workspace), science, medicine, coding agents (Claude Code, Cursor), databases.
- Evaluation dimensions: exact match on tool name/arguments, schema validity, end-to-end task completion in simulated environments; reliability across trials via τ-bench's pass^k (distinct from pass@k); ToolLLM/ToolBench (16,000+ real-world APIs); BFCL.
- "Training data for function calling looks much like other post-training data, with one addition: a system prompt that instructs the model what tools it has available."
- Code execution can occur "during the thinking tokens of a reasoning model".
- "What is happening under the hood is the language model is interleaving tool inputs and outputs with standard autoregressively generated tokens."
- "Training for tool use is about getting the model to behave predictably with this different token flow—knowing when to emit a tool call, how to format arguments correctly, and how to incorporate results into its response. Open models must be trained to work with a variety of tools that users may connect off the shelf."
- "OpenAI's o3 model represented a substantial step-change in how multi-step tool-use can be integrated with language models", building on ReAct's interleaving of reasoning and actions.
- Training multi-step tool behaviors with RL "resembles classic reinforcement learning more than the per-sample RLHF loop: the agent interacts with an environment and its tools over a full trajectory before any reward is assigned."
- MCP is "an open standard for connecting language models to external data sources and information systems"; uses JSON-RPC 2.0; primitives: resources, prompts, tools; architecture of servers, clients, hosts; makes tool-use development "far more predictable".
- Tool output tokens "are masked from the model's training loss", so the model does not learn to predict the tool system's output.
- Formats differ: models "tend to select one structure" (Python vs JSON) while providers use different formats; chat templates convert structured JSON into token streams; some models use special tokens for tool calls.
- Reasoning tokens may be preserved between tool calls within a turn but "are typically erased between turns to minimize serving cost (but they aren't always – this is a design decision)."
- Constrained decoding / "strict mode" enforces valid JSON; "Some closed model providers do additional post-training specifically to make structured JSON output reliable, whereas for open models this is handled as an inference flag in systems like vLLM."
- Tool outputs can quickly consume the context window; systems must truncate, summarize, or paginate.
- Data sources: "Human-written tool traces are expensive to collect, so most modern tool-use corpora are synthetic or bootstrapped—Toolformer-style self-labeling or large-scale generation as in ToolBench."
- Objectives: SFT on tool trajectories "teaches basic formatting and tool selection" and "is often enough for establishing the foundation of the skill"; preference optimization (e.g., DPO) "can improve decisions about when to call a tool versus answer directly"; for multi-step agentic tasks "RL with environment feedback (task success, constraint satisfaction) becomes the natural objective".

## Definitions and terminology
- **Tool use** — "the model emits a structured request (tool name and arguments); an orchestrator executes the tool; results are appended to the context; the model continues generating."
- **Function calling** — "tool use where the arguments must conform to a declared schema for a set of functions (usually JSON Schema), enabling reliable parsing and validation."
- **Code execution** — "a special case of tool use where the "tool" is a code interpreter (e.g., Python); results are returned as tool output."
- **Neural Programmer-Interpreters (NPI)** — "a recurrent and compositional neural network that learns to represent and execute programs" (circa 2015).
- **pass^k** — τ-bench metric "(distinct from pass@k) to measure whether an agent succeeds consistently rather than occasionally."
- **BFCL (Berkeley Function Calling Leaderboard)** — popular benchmark for function-calling accuracy, founded on Gorilla's APIBench.
- **ReAct** — using LLMs "to generate both reasoning traces and task-specific actions in an interleaved manner".
- **Trajectory / terminal reward r_T** — in multi-step tool RL, the policy π_θ alternates actions a_t with observations o_t; the completed trajectory is graded or verified to produce a single reward r_T at the end.
- **Model Context Protocol (MCP)** — "an open standard for connecting language models to external data sources and information systems"; data layer uses JSON-RPC 2.0 with discovery and execution methods.
- **MCP primitives** — resources ("read-only data blobs"), prompts ("templated messages/workflows"), tools ("functions the model can call").
- **MCP server / client / host** — servers "wrap a specific data source or capability"; clients (e.g., Claude Desktop, IDE plug-ins) "aggregate one or more servers"; hosts (e.g., Claude or ChatGPT applications) "provide the user/LLM interface".
- **Masking tool outputs** — excluding tool-output tokens from the training loss.
- **Chat template** — "the code for controlling the format of messages sent to the model", converting structured messages into raw token streams.
- **Reasoning token continuity** — whether reasoning tokens persist across tool-calling steps/turns.
- **Constrained decoding / strict mode** — enforcing valid JSON and argument types at generation time.
- **Provider API formats (as of May 2026)** — OpenAI Chat Completions: `tool_calls` arrays with unique IDs; OpenAI Responses API: `function_call` items and `function_call_output` items keyed by `call_id`; Anthropic: tools defined with `input_schema`, calls/results as `tool_use` and `tool_result` content blocks; Gemini: function-calling modes `AUTO`, `ANY`, `NONE`, and (in supported Gemini/Vertex AI configurations) `VALIDATED`.

## Evidence and examples
- **User examples** — "Who is the president today?"; "Move all the arXiv papers in my downloads folder to my ~/research/ directory with names indicating the date of the paper."
- **Pi via code execution** — `<code>` block computing pi with the Chudnovsky algorithm (`getcontext().prec = 60`, `C = 426880 * Decimal(10005).sqrt()`, loop `for i in range(1, 100)`, `print(str(compute_pi())[:52])`) and `<output>` `3.14159265358979323846264338327950288419716939937510`.
- **Function-calling system prompt (verbatim)** — "You are a function-calling AI model. You are provided with function signatures within <functions></functions> XML tags. You may call one or more functions to assist with the user query. Don't make assumptions about what values to plug into functions." Followed by a `<functions>` JSON list: `search_movies` (param `query`, required), `get_movie_details` (param `movie_id`, required), `get_showtimes` (params `movie_id`, `zip_code`, `date` "in YYYY-MM-DD format"; required `movie_id`, `zip_code`), then `<user>...</user>`. The model "would generate the tokens `search_movies("Star Wars")`".
- **Code execution inside thinking (verbatim)** — `<|user|>` "What is the 50th Fibonacci number? (Use the standard F_0=0, F_1=1 indexing.)" → `<think>` "Okay, I will compute the 50th Fibonacci number with a simple loop, then return the result." `<code>` def fib(n) loop … `fib(50)` `</code>` `<output>` 12586269025 `</output>` `</think>` `<answer>` "The 50th Fibonacci number is 12 586 269 025." `</answer>`.
- **Orchestration loop** — `messages = [...]`; `while True: response = model(messages, tools=tools)`; if no `response.tool_calls` return `response.text`; else for each call `result = execute_tool(call.name, call.args)` and append `{"role": "tool", "tool_call_id": call.id, "content": result}`.
- **Figure 1 (tool_use_generation.png)** — "Tool use interleaves model generation with external execution: the model generates tokens until it emits a tool call (orange), an external system executes the tool and injects the output (purple) into the sequence, then the model continues generating. Models can emit multiple tool calls in a single generation. During training, tool call and output tokens are typically masked from the loss."
- **ReAct quote** — reasoning traces "help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments."
- **Figure 2 (tool_use_rl_loop.png)** — "Reinforcement learning for multi-step tool use. A prompt is sampled from the training data and the agent (policy π_θ) interacts with the environment and its tools over a trajectory, alternating actions a_t with observations o_t. The completed trajectory is graded or verified to produce a single reward r_T at the end, which drives the policy update. Unlike the per-sample RLHF loop, the reward arrives only after a multi-step rollout – closer to classic RL."
- **MCP tool schema** — `get_weather` with `description` "Get current weather for a location" and `inputSchema` requiring `location` ("City name or coordinates").
- **Minimal Python MCP server** — `from mcp.server import Server`; `server = Server("weather-server")`; `@server.list_tools()` returns a `Tool(name="get_weather", …)`; `@server.call_tool()` dispatches to `fetch_weather(arguments["location"])` and returns `[TextContent(type="text", text=weather)]`.
- **Multi-turn tool dataset format** — messages list with a system message (same function-calling prompt; `functions` = `live_giveaways_by_type` from the GamerPower API, param `type` e.g. game, loot, beta, default "game"), user "Where can I find live giveaways for beta access and games?", and assistant with `content: null` and `function_calls: "live_giveaways_by_type(type='beta')\nlive_giveaways_by_type(type='game')"` (two parallel calls).
- **Scale numbers** — Gorilla trained on 1645 APIs (PyTorch Hub, TensorFlow Hub v2, Hugging Face); ToolLLM/ToolBench 16,000+ real-world APIs.
- **Chat template playground** — Hugging Face space linked (example model Qwen/Qwen3-8B) to explore how models convert message formats to token streams.
- **Bibliography** — 15 references incl. Reed & De Freitas (NPI, ICLR 2016), Lewis et al. (RAG, 2020), Nakano et al. (WebGPT, 2021), Gao et al. (PAL, 2023), Parisi et al. (TALM, 2022), Schick et al. (Toolformer, 2023), Patil et al. (Gorilla, 2024), Anthropic (MCP, 2024), Yao et al. (τ-bench, June 2024), Qin et al. (ToolLLM, 2024), Yao et al. (ReAct, 2023), Wang et al. (RAGEN, 2025).

## Inconsistencies / open questions
- [verified] The chapter says "Human-written tool traces are expensive to collect", so most corpora are "synthetic or bootstrapped" — an author-stated limitation on data provenance for tool-use training.
- [verified] The chapter admits uncertainty on history: "The exact origin of the term "tool use" is not clear".
- [verified] Reasoning-token handling is explicitly described as unsettled: tokens "are typically erased between turns … (but they aren't always – this is a design decision)."
- [verified] The MCP architecture bullet says hosts "provide the user/LLM interface; switching model vendors or back-end tools only means swapping the client in the middle" — slightly confusing given clients were just defined as aggregators of servers (e.g., Claude Desktop); wording is as in source.
- [verified] Terminology: "pass^k (distinct from pass@k)" is introduced without defining either metric in this chapter.
- [open question] Provider API details are explicitly dated "(as of May 2026)" (OpenAI Chat Completions vs Responses API, Anthropic `tool_use`/`tool_result`, Gemini `VALIDATED` mode) — would need current provider docs to confirm they still hold.
- [open question] "OpenAI's o3 model represented a substantial step-change in how multi-step tool-use can be integrated" — an evaluative claim without evidence in the chapter; settle via o3 system card / independent evals.
- [open question] Date of the chapter text is not printed; citation years (2025 web/arXiv, 2026 Manning) and the May 2026 note suggest a living document — check the book's changelog for revision date.
- [verified] Extraction artifacts: code blocks carry line-anchor prefixes like `<#cb2-1>`, `<#cb4-1>`, `<#cb7-1>` (from the site's code-line links), which are not part of the actual code/data; the bibliography is flattened into one paragraph; the two figures are image-only (their captions survive as alt text). The "Chapter Contents" block captured only a lecture link, not a section TOC.

## Images / diagrams
### `lambert-rlhfbook-tool-use.web/images/tool_use_generation.png`
- Provenance: web asset `web/lambert-rlhfbook-tool-use/assets/tool_use_generation.png` (PNG image data, 2023 x 686), captured from https://rlhfbook.com/c/13-tools. Alt text: "Figure 1: Tool use interleaves model generation with external execution: the model generates tokens until it emits a tool call (orange), an external system executes the tool and injects the output (purple) into the sequence, then the model continues generating. Models can emit multiple tool calls in a single generation. During training, tool call and output tokens are typically masked from the loss.".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `lambert-rlhfbook-tool-use.web/images/tool_use_rl_loop.png`
- Provenance: web asset `web/lambert-rlhfbook-tool-use/assets/tool_use_rl_loop.png` (PNG image data, 4899 x 1909), captured from https://rlhfbook.com/c/13-tools. Alt text: "Figure 2: Reinforcement learning for multi-step tool use. A prompt is sampled from the training data and the agent (policy \\pi_\\theta) interacts with the environment and its tools over a trajectory, alternating actions a_t with observations o_t. The completed trajectory is graded or verified to produce a single reward r_T at the end, which drives the policy update. Unlike the per-sample RLHF loop, the reward arrives only after a multi-step rollout – closer to classic RL.".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->


## Raw / preserved excerpts
> "Language models using tools is a natural way to expand their capabilities, especially for high-precision tasks where external tools contain the information or for agents that need to interact with complex web systems. Tool-use is a skill that language models need to be trained to have, and RLHF and all the other methods presented in this book can refine it."
— Chapter opening

> "A language model without tools will have a hard time answering this question due to the knowledge cutoff of pretraining data, but this is readily accessible information with one search query."
— Chapter opening ("Who is the president today?")

> "This is a task that the model weights alone cannot even attempt – the use of tools enables language models to address a far broader range of tasks."
— Chapter opening

> "Tool use: the model emits a structured request (tool name and arguments); an orchestrator executes the tool; results are appended to the context; the model continues generating. Function calling: tool use where the arguments must conform to a declared schema for a set of functions (usually JSON Schema), enabling reliable parsing and validation. Code execution: a special case of tool use where the "tool" is a code interpreter (e.g., Python); results are returned as tool output."
— Terminology

> "An AI model uses any external tools by outputting special tokens to trigger a certain endpoint. These can be anything from highly specific tools, such as functions that return the weather at a specific place, to code interpreters or search engines that act as fundamental building blocks of complex behaviors. Our first example showcased where language models need more up-to-date information to complement the fixed nature of their weights trained on past data, but there are also tools such as code execution, which lets language models get around their probabilistic, generative nature and return precise answers."
— Tool-Use Overview

> "The exact origin of the term "tool use" is not clear, but the origins of the idea far predate the post-ChatGPT world where RLHF proliferated."
— Tool-Use Overview

> "Tool-use models are now deeply intertwined with regular language model interactions. Model Context Protocol (MCP) emerged as a common formatting used to connect language models to external data sources (or tools)."
— Tool-Use Overview

> "Evaluating tool-use models involves multiple dimensions: exact-match metrics for tool name and argument correctness, schema validity, and end-to-end task completion in simulated environments. Reliability across trials also matters – τ-bench introduced the pass^k metric (distinct from pass@k) to measure whether an agent succeeds consistently rather than occasionally."
— Tool-Use Overview

> "Training data for function calling looks much like other post-training data, with one addition: a system prompt that instructs the model what tools it has available."
— Interweaving Tool Calls in Generation

> "Although the language model is generating a completion, if it is following this example, it would generate the tokens `search_movies("Star Wars")` to search for Star Wars. This is often encoded inside special formatting tokens, and then the next tokens inserted into the sequence will contain the tool outputs."
— Interweaving Tool Calls in Generation

> "A popular form of tool use is code-execution, allowing the model to get precise answers to complex logic or mathematics problems. For example, code-execution within a language model execution can occur during the thinking tokens of a reasoning model."
— Interweaving Tool Calls in Generation

> "What is happening under the hood is the language model is interleaving tool inputs and outputs with standard autoregressively generated tokens."
— Interweaving Tool Calls in Generation

> "Training for tool use is about getting the model to behave predictably with this different token flow—knowing when to emit a tool call, how to format arguments correctly, and how to incorporate results into its response. Open models must be trained to work with a variety of tools that users may connect off the shelf."
— Interweaving Tool Calls in Generation

> "OpenAI's o3 model represented a substantial step-change in how multi-step tool-use can be integrated with language models."
— Multistep Tool Reasoning

> "With the solidification of tool-use capabilities and the take-off of reasoning models, multi-turn tool-use has grown into an exciting area of research. Training these multi-step behaviors with RL resembles classic reinforcement learning more than the per-sample RLHF loop: the agent interacts with an environment and its tools over a full trajectory before any reward is assigned"
— Multistep Tool Reasoning

> "MCP is a simple addition on top of the tool-use content in this chapter – it is how applications pass context (data + actions) to language models in a predictable JSON schema. MCP servers that the models interact with have core primitives: resources (read-only data blobs), prompts (templated messages/workflows), and tools (functions the model can call)."
— Model Context Protocol

> "Masking tool outputs: An important detail when training tool-use models is that the tokens in the tool output are masked from the model's training loss. This ensures the model is not learning to predict the output of the system that processes the tool call (as the results are not tokens generated by the model)."
— Implementation Details

> "Reasoning token continuity: As reasoning models have emerged, with their separate token stream of "reasoning" before an answer, different implementations exist for how they're handled with tool-use in the loop. Some models preserve reasoning tokens between tool-calling steps within a single turn, maintaining context across multiple tool invocations. However, these tokens are typically erased between turns to minimize serving cost (but they aren't always – this is a design decision)."
— Implementation Details

> "Schema conformance and constrained decoding: Production systems often enforce valid JSON and correct argument types using constrained decoding or "strict mode" options, reducing retries from malformed outputs. Some closed model providers do additional post-training specifically to make structured JSON output reliable, whereas for open models this is handled as an inference flag in systems like vLLM."
— Implementation Details

> "Tying this back to post-training: where does tool-use training data come from, and what objectives are used? Human-written tool traces are expensive to collect, so most modern tool-use corpora are synthetic or bootstrapped—Toolformer-style self-labeling or large-scale generation as in ToolBench. For training objectives, supervised fine-tuning (SFT) on tool trajectories teaches basic formatting and tool selection. This bootstraps the behavior and is often enough for establishing the foundation of the skill. Preference optimization (e.g., DPO) over trajectories can improve decisions about when to call a tool versus answer directly. For agentic tasks with multi-step tool use, RL with environment feedback (task success, constraint satisfaction) becomes the natural objective – the model learns from whether its tool-augmented actions actually solved the problem."
— Implementation Details (closing paragraph)

### Full extracted text (verbatim)
Complete `page.md` as captured, verbatim (image links inside point to the raw `assets/` names; see *Images / diagrams* above for the companion-folder paths).

~~~~~text
# Tool Use and Function Calling | RLHF and Post-Training Book by Nathan Lambert

_Source: <https://rlhfbook.com/c/13-tools>_

[Reinforcement Learning from Human Feedback](https://rlhfbook.com/) 

A short introduction to RLHF and post-training focused on language models.

Nathan Lambert

###  Chapter Contents 

- [Lecture 11: Tool Use, Function Calling and The Road to Agents](https://www.youtube.com/watch?v=GMry2DzC304&list=PLL1tdVxB1CpVpEtMHxwuR4uI4Lxjw00_y&index=17) 

# Tool Use and Function Calling

Language models using tools is a natural way to expand their capabilities, especially for high-precision tasks where external tools contain the information or for agents that need to interact with complex web systems. Tool-use is a skill that language models need to be trained to have, and RLHF and all the other methods presented in this book can refine it. Consider a question from a user such as:

> 

**User**: Who is the president today?

A language model without tools will have a hard time answering this question due to the knowledge cutoff of pretraining data, but this is readily accessible information with one search query. Consider another example:

> 

**User**: Move all the arXiv papers in my downloads folder to my ~/research/ directory with names indicating the date of the paper.

This is a task that the model weights alone cannot even attempt – the use of tools enables language models to address a far broader range of tasks.

Before diving deeper, it is useful to distinguish related terms that are often used interchangeably:

- **Tool use**: the model emits a structured request (tool name and arguments); an orchestrator executes the tool; results are appended to the context; the model continues generating. 
- **Function calling**: tool use where the arguments must conform to a declared schema for a set of functions (usually JSON Schema), enabling reliable parsing and validation. 
- **Code execution**: a special case of tool use where the “tool” is a code interpreter (e.g., Python); results are returned as tool output. 

## Tool-Use Overview

An AI model uses any external tools by outputting special tokens to trigger a certain endpoint. These can be anything from highly specific tools, such as functions that return the weather at a specific place, to code interpreters or search engines that act as fundamental building blocks of complex behaviors. Our first example showcased where language models need more up-to-date information to complement the fixed nature of their weights trained on past data, but there are also tools such as code execution, which lets language models get around their probabilistic, generative nature and return precise answers. Consider the task of printing an approximation of pi to 50 digits (without reciting it from memory and risking hallucination). A language model with tools can do the following:

```
<code>
from decimal import Decimal, getcontext
getcontext().prec = 60

def compute_pi():
    # Chudnovsky algorithm for computing pi
    C = 426880 * Decimal(10005).sqrt()
    K, M, X, L, S = 0, 1, 1, 13591409, Decimal(13591409)
    for i in range(1, 100):
        M = M * (K**3 - 16*K) // ((i)**3)
        K += 12
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
    return C / S

print(str(compute_pi())[:52])
</code>

<output>
3.14159265358979323846264338327950288419716939937510
</output>
```

This chapter provides an overview of the origins of tool-use in modern language models, its fundamentals and formatting, and current trade-offs in utilizing tools well in leading models.

The exact origin of the term “tool use” is not clear, but the origins of the idea far predate the post-ChatGPT world where RLHF proliferated. Early examples circa 2015 attempted to build systems predating modern language models, such as Neural Programmer-Interpreters (NPI) [[1]](#ref-reed2015neural), “a recurrent and compositional neural network that learns to represent and execute programs.” As language models became more popular, many subfields were using integrations with external capabilities to boost performance. To obtain information outside of just the weights many used retrieval augmented generation [[2]](#ref-lewis2020retrieval) or web browsing [[3]](#ref-nakano2021webgpt). Soon after, others were exploring language models integrated with programs [[4]](#ref-gao2023pal) or tools [[5]](#ref-parisi2022talm).

As the field matured, these models gained more complex abilities in addition to the vast improvements to the underlying language modeling. For example, Toolformer could use “a calculator, a Q&A system, two different search engines, a translation system, and a calendar” [[6]](#ref-schick2023toolformerlanguagemodelsteach). Soon after, Gorilla was trained to use 1645 APIs (from PyTorch Hub, TensorFlow Hub v2, and Hugging Face) and its evaluation APIBench became a foundation of the popular Berkeley Function Calling Leaderboard [[7]](#ref-patil2023gorilla). Since these early models, the diversity of actions called has grown substantially.

Tool-use models are now deeply intertwined with regular language model interactions. Model Context Protocol (MCP) emerged as a common formatting used to connect language models to external data sources (or tools) [[8]](#ref-anthropic_mcp_2024). With stronger models and better formats, tool-use language models are used in many situations, including productivity copilots within popular applications such as Microsoft Office or Google Workspace, scientific domains [[9]](#ref-bran2023chemcrow), medical domains [[10]](#ref-li2024mmedagent), coding agents [[11]](#ref-zhang2024codeagent) such as Claude Code or Cursor, integrations with databases, and many other autonomous workflows.

Evaluating tool-use models involves multiple dimensions: exact-match metrics for tool name and argument correctness, schema validity, and end-to-end task completion in simulated environments. Reliability across trials also matters – \(\tau\)-bench introduced the pass^k metric (distinct from pass@k) to measure whether an agent succeeds consistently rather than occasionally [[12]](#ref-yao2024taubench). ToolLLM and its ToolBench dataset provide a large-scale framework for training and evaluating tool use across 16,000+ real-world APIs [[13]](#ref-qin2023toollm), while the Berkeley Function Calling Leaderboard (BFCL) remains a popular benchmark for comparing models on function calling accuracy [[7]](#ref-patil2023gorilla).

## Interweaving Tool Calls in Generation

Training data for function calling looks much like other post-training data, with one addition: a system prompt that instructs the model what tools it has available. An example formatted data point with the system prompt and tools available in JSON format is shown below:

```
<#cb2-1><system>
<#cb2-2>You are a function-calling AI model. You are provided with function signatures within <functions></functions> XML tags. You may call one or more functions to assist with the user query. Don't make assumptions about what values to plug into functions.
<#cb2-3></system>
<#cb2-4>
<#cb2-5><functions>
<#cb2-6>[
<#cb2-7>  {
<#cb2-8>    "name": "search_movies",
<#cb2-9>    "description": "Search for movies by title and return matching results with IDs.",
<#cb2-10>    "parameters": {
<#cb2-11>      "type": "object",
<#cb2-12>      "properties": {
<#cb2-13>        "query": {
<#cb2-14>          "type": "string",
<#cb2-15>          "description": "The search string for the movie title."
<#cb2-16>        }
<#cb2-17>      },
<#cb2-18>      "required": ["query"]
<#cb2-19>    }
<#cb2-20>  },
<#cb2-21>  {
<#cb2-22>    "name": "get_movie_details",
<#cb2-23>    "description": "Fetch detailed information about a movie including cast, runtime, and synopsis.",
<#cb2-24>    "parameters": {
<#cb2-25>      "type": "object",
<#cb2-26>      "properties": {
<#cb2-27>        "movie_id": {
<#cb2-28>          "type": "string",
<#cb2-29>          "description": "The unique identifier for the movie."
<#cb2-30>        }
<#cb2-31>      },
<#cb2-32>      "required": ["movie_id"]
<#cb2-33>    }
<#cb2-34>  },
<#cb2-35>  {
<#cb2-36>    "name": "get_showtimes",
<#cb2-37>    "description": "Get movie showtimes for a given location and date.",
<#cb2-38>    "parameters": {
<#cb2-39>      "type": "object",
<#cb2-40>      "properties": {
<#cb2-41>        "movie_id": {
<#cb2-42>          "type": "string",
<#cb2-43>          "description": "The unique identifier for the movie."
<#cb2-44>        },
<#cb2-45>        "zip_code": {
<#cb2-46>          "type": "string",
<#cb2-47>          "description": "ZIP code for theater location."
<#cb2-48>        },
<#cb2-49>        "date": {
<#cb2-50>          "type": "string",
<#cb2-51>          "description": "Date for showtimes in YYYY-MM-DD format."
<#cb2-52>        }
<#cb2-53>      },
<#cb2-54>      "required": ["movie_id", "zip_code"]
<#cb2-55>    }
<#cb2-56>  }
<#cb2-57>]
<#cb2-58></functions>
<#cb2-59>
<#cb2-60><user>
<#cb2-61>...
<#cb2-62></user>
```

Although the language model is generating a completion, if it is following this example, it would generate the tokens `search_movies("Star Wars")` to search for Star Wars. This is often encoded inside special formatting tokens, and then the next tokens inserted into the sequence will contain the tool outputs. With this, models can learn to accomplish more challenging tasks than many simple standalone models.

A popular form of tool use is code-execution, allowing the model to get precise answers to complex logic or mathematics problems. For example, code-execution within a language model execution can occur during the thinking tokens of a reasoning model. As with function calling, there are tags first for the code to execute (generated by the model) and then a separate tag for output.

```
<|user|>
What is the 50th Fibonacci number? (Use the standard F_0=0, F_1=1 indexing.)</s>
<|assistant|>
<think>
Okay, I will compute the 50th Fibonacci number with a simple loop, then return the result.

<code>
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

fib(50)
</code>

<output>
12586269025
</output>
</think>
<answer>
The 50th Fibonacci number is 12 586 269 025.
</answer>
```

What is happening under the hood is the language model is interleaving tool inputs and outputs with standard autoregressively generated tokens. The orchestration loop that makes this possible looks something like:

```
<#cb4-1>messages = [...]
<#cb4-2>while True:
<#cb4-3>    response = model(messages, tools=tools)
<#cb4-4>    if not response.tool_calls:
<#cb4-5>        return response.text
<#cb4-6>
<#cb4-7>    for call in response.tool_calls:
<#cb4-8>        result = execute_tool(call.name, call.args)
<#cb4-9>        messages.append({"role": "tool", "tool_call_id": call.id, "content": result})
```

![Figure 1: Tool use interleaves model generation with external execution: the model generates tokens until it emits a tool call (orange), an external system executes the tool and injects the output (purple) into the sequence, then the model continues generating. Models can emit multiple tool calls in a single generation. During training, tool call and output tokens are typically masked from the loss.](images/tool_use_generation.png) Figure 1: Tool use interleaves model generation with external execution: the model generates tokens until it emits a tool call (orange), an external system executes the tool and injects the output (purple) into the sequence, then the model continues generating. Models can emit multiple tool calls in a single generation. During training, tool call and output tokens are typically masked from the loss. 

Training for tool use is about getting the model to behave predictably with this different token flow—knowing when to emit a tool call, how to format arguments correctly, and how to incorporate results into its response. Open models must be trained to work with a variety of tools that users may connect off the shelf.

## Multistep Tool Reasoning

OpenAI’s o3 model represented a substantial step-change in how multi-step tool-use can be integrated with language models. This behavior is related to much earlier research trends in the community. For example, ReAct [[14]](#ref-yao2023react) showcased how actions and reasoning can be interleaved into one model generation:

> 

In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments.

With the solidification of tool-use capabilities and the take-off of reasoning models, multi-turn tool-use has grown into an exciting area of research [[15]](#ref-wang2025ragenunderstandingselfevolutionllm). Training these multi-step behaviors with RL resembles classic reinforcement learning more than the per-sample RLHF loop: the agent interacts with an environment and its tools over a full trajectory before any reward is assigned, as shown in fig. [2](#fig:tool-use-rl).

![Figure 2: Reinforcement learning for multi-step tool use. A prompt is sampled from the training data and the agent (policy \pi_\theta) interacts with the environment and its tools over a trajectory, alternating actions a_t with observations o_t. The completed trajectory is graded or verified to produce a single reward r_T at the end, which drives the policy update. Unlike the per-sample RLHF loop, the reward arrives only after a multi-step rollout – closer to classic RL.](images/tool_use_rl_loop.png) Figure 2: Reinforcement learning for multi-step tool use. A prompt is sampled from the training data and the agent (policy \(\pi_\theta\)) interacts with the environment and its tools over a trajectory, alternating actions \(a_t\) with observations \(o_t\). The completed trajectory is graded or verified to produce a single reward \(r_T\) at the end, which drives the policy update. Unlike the per-sample RLHF loop, the reward arrives only after a multi-step rollout – closer to classic RL. 

## Model Context Protocol

Model Context Protocol (MCP) is an open standard for connecting language models to external data sources and information systems [[8]](#ref-anthropic_mcp_2024). At the data layer, MCP uses JSON-RPC 2.0 with discovery and execution methods for its primitives. Rather than requiring specific tool call formatting per external system, MCP enables models to access rich contextual information through a standardized protocol.

MCP is a simple addition on top of the tool-use content in this chapter – it is how applications pass context (data + actions) to language models in a predictable JSON schema. MCP servers that the models interact with have core primitives: resources (read-only data blobs), prompts (templated messages/workflows), and tools (functions the model can call). With this, the MCP architecture can be summarized as:

- MCP servers wrap a specific data source or capability. 
- MCP clients (e.g., Claude Desktop, IDE plug-ins) aggregate one or more servers. 
- Hosts, e.g. Claude or ChatGPT applications, provide the user/LLM interface; switching model vendors or back-end tools only means swapping the client in the middle. 

MCP enables developers of tool-use models to use the same infrastructure to attach their servers or clients to different models, and at the same time models have a predictable format they can use to integrate external components. These together make for a far more predictable development environment for tool-use models in real-world domains.

An MCP server exposes tools to clients through a standardized JSON schema:

```
<#cb5-1>{
<#cb5-2>  "name": "get_weather",
<#cb5-3>  "description": "Get current weather for a location",
<#cb5-4>  "inputSchema": {
<#cb5-5>    "type": "object",
<#cb5-6>    "properties": {
<#cb5-7>      "location": {
<#cb5-8>        "type": "string",
<#cb5-9>        "description": "City name or coordinates"
<#cb5-10>      }
<#cb5-11>    },
<#cb5-12>    "required": ["location"]
<#cb5-13>  }
<#cb5-14>}
```

A minimal Python MCP server implementing this tool:

```
<#cb6-1>from mcp.server import Server
<#cb6-2>from mcp.types import Tool, TextContent
<#cb6-3>
<#cb6-4>server = Server("weather-server")
<#cb6-5>
<#cb6-6>@server.list_tools()
<#cb6-7>async def list_tools():
<#cb6-8>    return [Tool(
<#cb6-9>        name="get_weather",
<#cb6-10>        description="Get current weather",
<#cb6-11>        inputSchema={
<#cb6-12>            "type": "object",
<#cb6-13>            "properties": {"location": {"type": "string"}},
<#cb6-14>            "required": ["location"]
<#cb6-15>        }
<#cb6-16>    )]
<#cb6-17>
<#cb6-18>@server.call_tool()
<#cb6-19>async def call_tool(name: str, arguments: dict):
<#cb6-20>    if name == "get_weather":
<#cb6-21>        weather = fetch_weather(arguments["location"])
<#cb6-22>        return [TextContent(type="text", text=weather)]
```

## Implementation Details

There are multiple formatting and masking decisions when implementing a tool-use model:

- **Python vs. JSON formatting**: In this chapter, we include examples that format tool use as both JSON data structures and Python code. Models tend to select one structure, whereas different providers across the industry use different formats. 
- **Masking tool outputs**: An important detail when training tool-use models is that the tokens in the tool output are masked from the model’s training loss. This ensures the model is not learning to predict the output of the system that processes the tool call (as the results are not tokens generated by the model). 
- **Multi-turn formatting for tool invocations**: It is common practice when implementing tool-calling models to add more structure to the data-loading format. Standard practice for post-training datasets is a list of messages alternating between user and assistant (and often a system message). The overall structure is the same for tool-use, but the turns of the model are split into subsections of content delimited by each tool call. An example is below. 

```
<#cb7-1>messages = [
<#cb7-2>{
<#cb7-3>"content": "You are a function calling AI model. You are provided with function signatures within <functions></functions> XML tags. You may call one or more functions to assist with the user query. Don't make assumptions about what values to plug into functions.",
<#cb7-4>"function_calls": null,
<#cb7-5>"functions": "[{\"name\": \"live_giveaways_by_type\", \"description\": \"Retrieve live giveaways from the GamerPower API based on the specified type.\", \"parameters\": {\"type\": {\"description\": \"The type of giveaways to retrieve (e.g., game, loot, beta).\", \"type\": \"str\", \"default\": \"game\"}}}]",
<#cb7-6>"role": "system"
<#cb7-7>},
<#cb7-8>{
<#cb7-9>"content": "Where can I find live giveaways for beta access and games?",
<#cb7-10>"function_calls": null,
<#cb7-11>"functions": null,
<#cb7-12>"role": "user"
<#cb7-13>},
<#cb7-14>{
<#cb7-15>"content": null,
<#cb7-16>"function_calls": "live_giveaways_by_type(type='beta')\nlive_giveaways_by_type(type='game')",
<#cb7-17>"functions": null,
<#cb7-18>"role": "assistant"
<#cb7-19>}
<#cb7-20>]
```

- **Tokenization and message format details**: Tool calls in OpenAI messages format often undergo tokenization through chat templates (the code for controlling the format of messages sent to the model), converting structured JSON representations into raw token streams. This process varies across model architectures—some use special tokens to demarcate tool calls, while others maintain structured formatting within the token stream itself. [Chat template playgrounds](https://huggingface.co/spaces/huggingfacejs/chat-template-playground?modelId=Qwen/Qwen3-8B) provide an interactive environment to explore how different models convert message formats to token streams. 
- **Reasoning token continuity**: As reasoning models have emerged, with their separate token stream of “reasoning” before an answer, different implementations exist for how they’re handled with tool-use in the loop. Some models preserve reasoning tokens between tool-calling steps within a single turn, maintaining context across multiple tool invocations. However, these tokens are typically erased between turns to minimize serving cost (but they aren’t always – this is a design decision). 
- **API formatting across providers** (as of May 2026): Different providers use conceptually similar but technically distinct formats. OpenAI’s Chat Completions API uses `tool_calls` arrays with unique IDs, while the newer Responses API represents calls as `function_call` items and returns results as `function_call_output` items keyed by `call_id`. Anthropic defines tools with `input_schema` and represents calls and results as `tool_use` and `tool_result` content blocks. Gemini exposes function-calling modes such as `AUTO`, `ANY`, `NONE`, and, in supported Gemini and Vertex AI configurations, `VALIDATED`. 
- **Schema conformance and constrained decoding**: Production systems often enforce valid JSON and correct argument types using constrained decoding or “strict mode” options, reducing retries from malformed outputs. Some closed model providers do additional post-training specifically to make structured JSON output reliable, whereas for open models this is handled as an inference flag in systems like vLLM. 
- **Tool output context consumption**: Tool outputs can quickly consume the model’s context window, especially with search or retrieval tools that return many results. Systems must decide how to truncate, summarize, or paginate tool outputs to keep context manageable while preserving the information the model needs to continue. 

Tying this back to post-training: where does tool-use training data come from, and what objectives are used? Human-written tool traces are expensive to collect, so most modern tool-use corpora are synthetic or bootstrapped—Toolformer-style self-labeling [[6]](#ref-schick2023toolformerlanguagemodelsteach) or large-scale generation as in ToolBench [[13]](#ref-qin2023toollm). For training objectives, supervised fine-tuning (SFT) on tool trajectories teaches basic formatting and tool selection. This bootstraps the behavior and is often enough for establishing the foundation of the skill. Preference optimization (e.g., DPO) over trajectories can improve decisions about when to call a tool versus answer directly. For agentic tasks with multi-step tool use, RL with environment feedback (task success, constraint satisfaction) becomes the natural objective – the model learns from whether its tool-augmented actions actually solved the problem.

# Bibliography

[1] S. Reed and N. De Freitas, “Neural programmer-interpreters,” in *International conference on learning representations (ICLR)*, 2016. [2] P. Lewis *et al.*, “Retrieval-augmented generation for knowledge-intensive nlp tasks,” *Advances in neural information processing systems*, vol. 33, pp. 9459–9474, 2020. [3] R. Nakano *et al.*, “Webgpt: Browser-assisted question-answering with human feedback,” *arXiv preprint arXiv:2112.09332*, 2021. [4] L. Gao *et al.*, “Pal: Program-aided language models,” in *International conference on machine learning*, PMLR, 2023, pp. 10764–10799. [5] A. Parisi, Y. Zhao, and N. Fiedel, “Talm: Tool augmented language models,” *arXiv preprint arXiv:2205.12255*, 2022. [6] T. Schick *et al.*, “Toolformer: Language models can teach themselves to use tools,” in *Advances in neural information processing systems (NeurIPS)*, 2023. [7] S. G. Patil, T. Zhang, X. Wang, and J. E. Gonzalez, “Gorilla: Large language model connected with massive APIs,” in *Advances in neural information processing systems (NeurIPS)*, 2024. [8] Anthropic, “Model context protocol (MCP).” [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/), 2024. [9] A. M. Bran, S. Cox, O. Schilter, C. Baldassari, A. D. White, and P. Schwaller, “Chemcrow: Augmenting large-language models with chemistry tools,” *arXiv preprint arXiv:2304.05376*, 2023. [10] B. Li *et al.*, “Mmedagent: Learning to use medical tools with multi-modal agent,” in *Conference on empirical methods in natural language processing (EMNLP)*, 2024. [11] K. Zhang, J. Li, G. Li, X. Shi, and Z. Jin, “Codeagent: Enhancing code generation with tool-integrated agent systems for real-world repo-level coding challenges,” *arXiv preprint arXiv:2401.07339*, 2024. [12] S. Yao, N. Shinn, P. Razavi, and K. Narasimhan, “\(\tau\)-bench: A benchmark for tool-agent-user interaction in real-world domains.” June 2024. doi: [10.48550/arXiv.2406.12045](https://doi.org/10.48550/arXiv.2406.12045). [13] Y. Qin *et al.*, “ToolLLM: Facilitating large language models to master 16000+ real-world APIs,” in *International conference on learning representations (ICLR)*, July 2024. doi: [10.48550/arXiv.2307.16789](https://doi.org/10.48550/arXiv.2307.16789). [14] S. Yao *et al.*, “React: Synergizing reasoning and acting in language models,” in *International conference on learning representations (ICLR)*, 2023. [15] Z. Wang *et al.*, “RAGEN: Understanding self-evolution in LLM agents via multi-turn reinforcement learning.” 2025. Available: [https://arxiv.org/abs/2504.20073](https://arxiv.org/abs/2504.20073) [← Previous: Synthetic Data & Distillation](12-synthetic-data) [Next: Over-Optimization →](14-over-optimization) 

#### Citation

If you found this useful for your research, please cite it!

For the web and arXiv version:

```
@misc{lambert2025reinforcementlearninghumanfeedback,
  title = {Reinforcement Learning from Human Feedback},
  author = {Nathan Lambert},
  year = {2025},
  eprint = {2504.12501},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  url = {https://arxiv.org/abs/2504.12501}
}
```

For the Manning edition:

```
@book{lambert2026reinforcement,
  author = {Nathan Lambert},
  title = {Reinforcement Learning from Human Feedback: Alignment and post-training of {LLMs}},
  year = {2026},
  publisher = {Manning Publications},
  isbn = {9781633434301},
  url = {https://www.manning.com/books/reinforcement-learning-from-human-feedback}
}
```
~~~~~
