---
source_file: anthropic-building-effective-agents/
source_type: web-capture
ingested_at: 2026-10-04
---

# Building effective agents (Anthropic Engineering)

## Provenance
- Original location: research/web/anthropic-building-effective-agents/ (text from `page.md`; `original.html` not needed — `page.md` is 21,423 chars with 21 headings)
- Format: html (web capture via talksmith:ingest)
- URL: https://www.anthropic.com/engineering/building-effective-agents
- Fetched at: 2026-10-04T14:08:28Z (HTTP 200, 173,726 bytes)
- Author / source (if known): Erik S. and Barry Zhang, Anthropic (Engineering at Anthropic blog)
- Date of original (if known): Published Dec 19, 2024. The live page carries a later editorial note ("Much of the tooling landscape described in this post has changed since December 2024…") and mentions later models (Claude Haiku 4.5, Claude Sonnet 4.5), so the captured text is a revised version of the original post.

## Key claims
- "Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks."
- Anthropic groups all variations under the umbrella term **agentic systems**, with an architectural distinction between **workflows** (predefined code paths) and **agents** (LLM dynamically directs its own process and tool usage).
- Recommendation: "finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all."
- "Agentic systems often trade latency and cost for better task performance."
- Workflows offer "predictability and consistency for well-defined tasks"; agents are better "when flexibility and model-driven decision-making are needed at scale." For many applications, "optimizing single LLM calls with retrieval and in-context examples is usually enough."
- Frameworks (Claude Agent SDK, Strands Agents SDK by AWS, Rivet, Vellum) simplify low-level tasks but add abstraction that obscures prompts/responses and makes debugging harder; start with LLM APIs directly. "Incorrect assumptions about what's under the hood are a common source of customer error."
- The foundational building block is the **augmented LLM**: an LLM enhanced with retrieval, tools, and memory; current models can generate their own search queries, select tools, and decide what to retain.
- Five workflow patterns + autonomous agents, in increasing complexity: prompt chaining, routing, parallelization (sectioning / voting), orchestrator-workers, evaluator-optimizer; then agents.
- Agents "are typically just LLMs using tools based on environmental feedback in a loop."
- Agents need "ground truth" from the environment at each step (tool call results, code execution) to assess progress; they can pause for human feedback at checkpoints; stopping conditions (e.g. max iterations) maintain control.
- Agent autonomy means "higher costs, and the potential for compounding errors"; recommend extensive testing in sandboxed environments plus guardrails.
- Three core principles for agents: (1) simplicity, (2) transparency (explicitly show planning steps), (3) carefully crafted agent-computer interface (ACI) via thorough tool documentation and testing.
- Invest as much effort in agent-computer interfaces (ACI) as in human-computer interfaces (HCI).
- On SWE-bench, Anthropic "spent more time optimizing our tools than the overall prompt."
- Agents add most value for tasks that "require both conversation and action, have clear success criteria, enable feedback loops, and integrate meaningful human oversight."

## Definitions and terminology
- **Agentic systems**: umbrella term covering both workflows and agents.
- **Workflows**: "systems where LLMs and tools are orchestrated through predefined code paths."
- **Agents**: "systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks."
- **Augmented LLM**: LLM + retrieval + tools + memory; the basic building block.
- **Prompt chaining**: task decomposed into a sequence of steps, each LLM call processes the previous output; optional programmatic "gate" checks on intermediate steps.
- **Routing**: classifies an input and directs it to a specialized follow-up task (separation of concerns).
- **Parallelization**: LLMs work simultaneously and outputs are aggregated programmatically. Two variations: **Sectioning** (independent subtasks in parallel) and **Voting** (same task multiple times for diverse outputs).
- **Orchestrator-workers**: a central LLM dynamically breaks down tasks, delegates to worker LLMs, synthesizes results. Differs from parallelization in that subtasks are not predefined but determined by the orchestrator per input.
- **Evaluator-optimizer**: one LLM call generates, another evaluates and gives feedback, in a loop.
- **Agent-computer interface (ACI)**: the tool/interface layer the agent uses; analogue of HCI.
- **Poka-yoke** (tools): change arguments so mistakes are harder to make.
- **Model Context Protocol (MCP)**: mentioned as one way to implement augmentations (out of scope for this Talk per presenter).

## Evidence and examples
- Prompt chaining examples: marketing copy then translation; outline → check criteria → write document.
- Routing examples: customer-service query types (general, refund, technical support) → different processes/prompts/tools; easy questions → smaller models (Claude Haiku 4.5), hard ones → more capable models (Claude Sonnet 4.5).
- Parallelization / sectioning: guardrails in one instance while another answers (performs better than one call doing both); automated evals where each call evaluates a different aspect.
- Parallelization / voting: multiple prompts reviewing code for vulnerabilities; multiple prompts judging inappropriate content with different vote thresholds.
- Orchestrator-workers examples: coding products changing multiple files; search tasks gathering from multiple sources.
- Evaluator-optimizer examples: literary translation with critic LLM; complex search with evaluator deciding whether to search more. Two signs of fit: LLM responses improve when a human articulates feedback, and the LLM can provide such feedback.
- Agent examples (Anthropic's own): coding agent resolving SWE-bench tasks; "computer use" reference implementation.
- Appendix 1 — Customer support: conversation flow + external info/actions; tools pull customer data, order history, KB; actions like refunds; success measurable; some companies charge only for successful resolutions.
- Appendix 1 — Coding agents: verifiable via automated tests; iterate using test results; well-defined problem space; objective quality. Agents solve real GitHub issues in SWE-bench Verified from PR description alone; human review still crucial.
- Appendix 2 — Tool format: diffs require knowing changed line count in the chunk header before writing; code inside JSON needs extra escaping vs. markdown.
- Appendix 2 — SWE-bench anecdote: model made mistakes with relative filepaths after moving out of root; tool changed to require absolute filepaths, "the model used this method flawlessly."

## Inconsistencies / open questions
- [verified] The page is a revised version of the Dec 19, 2024 post, not the original text — checked: `page.md` line 13 carries an editorial note ("Much of the tooling landscape described in this post has changed since December 2024…") pointing to Claude Managed Agents, and the routing example names Claude Haiku 4.5 / Claude Sonnet 4.5. Cite as "Anthropic (2024, rev.)" if dating matters.
- [open question] The framework list (Claude Agent SDK, Strands, Rivet, Vellum) may differ from the original Dec 2024 list (which a citation might quote) — would be settled by comparing against an archived Dec 2024 snapshot.
- [verified] "Whereas it's topographically similar" (orchestrator-workers vs. parallelization) is the source's own wording, not an extraction error — checked: the same string appears in `original.html`. The intended sense is almost certainly "topologically" (same graph shape); if quoted in Spanish, translate the meaning ("con la misma forma/topología").
- [open question] The post does not name reasoning-pattern families (ReAct, Reflexion, Plan-and-Execute); its taxonomy is by control flow (workflow vs. agent). Evaluator-optimizer is the closest analogue to Reflexion-style loops, but that mapping is the reader's, not the source's.

## Images / diagrams

### `anthropic-building-effective-agents.web/images/039b6648c28eb33070a63a58d49013600b229238-2554x2554.svg`
- Provenance: page hero illustration; https://www-cdn.anthropic.com/images/4zrzovbb/website/039b6648c28eb33070a63a58d49013600b229238-2554x2554.svg; saved as-is (SVG); alt="" (no caption).
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-building-effective-agents.web/images/image.png`
- Provenance: figure under "Building block: The augmented LLM"; caption in source: "The augmented LLM". Raw asset `assets/image.bin` (PNG 2401x1000), from https://www-cdn.anthropic.com/images/4zrzovbb/website/d3083d3f40bb2b6f477901cc9a240738d3dd1371-2401x1000.png.
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-building-effective-agents.web/images/image-2.webp`
- Provenance: figure under "Workflow: Prompt chaining"; caption in source: "The prompt chaining workflow". Raw asset `assets/image-2.bin` (WebP), from .../7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.png.
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-building-effective-agents.web/images/image-3.png`
- Provenance: figure under "Workflow: Routing"; caption in source: "The routing workflow". Raw asset `assets/image-3.bin` (PNG 2401x1000), from .../5c0c0e9fe4def0b584c04d37849941da55e5e71c-2401x1000.png.
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-building-effective-agents.web/images/image-4.webp`
- Provenance: figure under "Workflow: Parallelization"; caption in source: "The parallelization workflow". Raw asset `assets/image-4.bin` (WebP), from .../406bb032ca007fd1624f261af717d70e6ca86286-2401x1000.png.
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-building-effective-agents.web/images/image-5.webp`
- Provenance: figure under "Workflow: Orchestrator-workers"; caption in source: "The orchestrator-workers workflow". Raw asset `assets/image-5.bin` (WebP), from .../8985fc683fae4780fb34eab1365ab78c7e51bc8e-2401x1000.png.
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-building-effective-agents.web/images/image-6.webp`
- Provenance: figure under "Workflow: Evaluator-optimizer"; caption in source: "The evaluator-optimizer workflow". Raw asset `assets/image-6.bin` (WebP), from .../14f51e6406ccb29e695da48b17017e899a6119c7-2401x1000.png.
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-building-effective-agents.web/images/image-7.webp`
- Provenance: figure under "Agents"; caption in source: "Autonomous agent". Raw asset `assets/image-7.bin` (WebP), from .../58d9f10c985c4eb5d53798dea315f7bb5ab6249e-2401x1000.png.
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-building-effective-agents.web/images/image-8.webp`
- Provenance: figure after the agent examples; caption in source: "High-level flow of a coding agent". Raw asset `assets/image-8.bin` (WebP), from .../4b9a1f4eb63d5962a6e1746ac26bbc857cf3474f-2400x1666.png.
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

## Raw / preserved excerpts

> We've worked with dozens of teams building LLM agents across industries. Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks.

> *Note: Much of the tooling landscape described in this post has changed since December 2024. For our current approach, see how we built Claude Managed Agents and the Managed Agents documentation.*

**What are agents?**

> "Agent" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as **agentic systems**, but draw an important architectural distinction between **workflows** and **agents**:
>
> - **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
> - **Agents**, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

**When (and when not) to use agents**

> When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense.
>
> When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough.

**When and how to use frameworks**

> These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice.
>
> We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error.

**Building block: The augmented LLM**

> The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain.
>
> We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol, which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation.

**Workflow: Prompt chaining**

> Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see "gate" in the diagram below) on any intermediate steps to ensure that the process is still on track.
>
> **When to use this workflow:** This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task.

**Workflow: Routing**

> Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.
>
> **When to use this workflow:** Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm.

**Workflow: Parallelization**

> LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations:
>
> - **Sectioning**: Breaking a task into independent subtasks run in parallel.
> - **Voting:** Running the same task multiple times to get diverse outputs.
>
> **When to use this workflow:** Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect.

**Workflow: Orchestrator-workers**

> In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.
>
> **When to use this workflow:** This workflow is well-suited for complex tasks where you can't predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it's topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

**Workflow: Evaluator-optimizer**

> In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.
>
> **When to use this workflow:** This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document.

**Agents**

> Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain "ground truth" from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it's also common to include stopping conditions (such as a maximum number of iterations) to maintain control.
>
> Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 ("Prompt Engineering your Tools").
>
> **When to use agents:** Agents can be used for open-ended problems where it's difficult or impossible to predict the required number of steps, and where you can't hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments.
>
> The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails.

**Combining and customizing these patterns / Summary**

> These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases. The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity *only* when it demonstrably improves outcomes.
>
> Success in the LLM space isn't about building the most sophisticated system. It's about building the *right* system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short.
>
> When implementing agents, we try to follow three core principles:
>
> 1. Maintain **simplicity** in your agent's design.
> 2. Prioritize **transparency** by explicitly showing the agent's planning steps.
> 3. Carefully craft your agent-computer interface (ACI) through thorough tool **documentation and testing**.
>
> Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users.

**Appendix 1: Agents in practice (intro)**

> Our work with customers has revealed two particularly promising applications for AI agents that demonstrate the practical value of the patterns discussed above. Both applications illustrate how agents add the most value for tasks that require both conversation and action, have clear success criteria, enable feedback loops, and integrate meaningful human oversight.

**Appendix 2: Prompt engineering your tools**

> No matter which agentic system you're building, tools will likely be an important part of your agent. Tools enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a tool use block in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts.
>
> There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes.
>
> Our suggestions for deciding on tool formats are the following:
>
> - Give the model enough tokens to "think" before it writes itself into a corner.
> - Keep the format close to what the model has seen naturally occurring in text on the internet.
> - Make sure there's no formatting "overhead" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes.
>
> One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good *agent*-computer interfaces (ACI). Here are some thoughts on how to do so:
>
> - Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it's probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools.
> - How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools.
> - Test how the model uses your tools: Run many example inputs in our workbench to see what mistakes the model makes, and iterate.
> - Poka-yoke your tools. Change the arguments so that it is harder to make mistakes.
>
> While building our agent for SWE-bench, we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly.
