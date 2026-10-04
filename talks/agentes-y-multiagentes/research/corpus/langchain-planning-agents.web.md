---
source_file: langchain-planning-agents/
source_type: web-capture
ingested_at: 2026-10-04
---

# Plan-and-Execute Agents (LangChain blog)

## Provenance
- Original location: `research/web/langchain-planning-agents/` (`page.md` used as text input; no fallback needed)
- Format: html (web capture via `talksmith:ingest`)
- URL: https://www.langchain.com/blog/planning-agents
- Fetched: 2026-10-04T14:08:33Z (HTTP 200, 165,093 bytes)
- Author / source (if known): The LangChain Team, LangChain blog (categories "LangGraph", "Agent Architecture"; 5 min read)
- Date of original (if known): February 13, 2024 (byline on page)
- Companion code: LangGraph notebooks — Plan-and-execute (Python + JS), LLMCompiler (Python), ReWOO (Python); YouTube walkthrough https://youtu.be/uRya4zRrRx4

## Key claims
- LangChain releases three LangGraph agent architectures in the **"plan-and-execute"** style, claimed to improve on ReAct-style agents in three ways:
  1. **Faster** — the larger agent need not be consulted after each action; sub-tasks can run without an extra LLM call (or with a lighter LLM).
  2. **Cheaper** — sub-task LLM calls can go to smaller, domain-specific models; the large model is only called for (re-)planning and the final response.
  3. **Better** (task completion rate and quality) — forcing the planner to "think through" all steps; subdividing permits more focused execution.
- Generic LLM-agent loop: (1) **Propose action** (LLM generates text for the user or for a function), (2) **Execute action** (your code invokes software — DB query, API call), (3) **Observe** (react to the tool result: call another function or respond to the user).
- **ReAct** is "a great prototypical design", prompting a repeated thought → act → observation loop; it builds on chain-of-thought to choose one action per step.
- Two downsides of ReAct: (1) one LLM call per tool invocation; (2) the LLM plans only one sub-problem at a time → possibly sub-optimal trajectories, "since it isn't forced to 'reason' about the whole task."
- Fix: an explicit **planning step**.
- **Plan-and-Execute** (loosely based on Wang et al., *Plan-and-Solve Prompting*, and Yohei Nakajima's BabyAGI): a **planner** LLM writes a multi-step plan; **executor(s)** take the query + one step and call 1+ tools; then a **re-planning** prompt decides to finish or produce a follow-up plan. Limitation: still serial tool calling, and an LLM per task (no variable assignment).
- **ReWOO** (Reasoning WithOut Observations; Xu et al.): planner output interleaves "Plan" reasoning lines with "E#" evidence lines that can reference earlier results (`#E2`), so the task list executes without re-planning; a **worker** fills variables; a **solver** integrates outputs. Each task gets only the context it needs. Limitation: still sequential execution.
- **LLMCompiler** (Kim et al.): the **planner** streams a DAG of tasks (tool, arguments, dependencies); a **Task Fetching Unit** schedules each task as soon as its dependencies are met; a **Joiner** decides to answer or hand back to the re-planner. Claimed speedup "3.6x" (per the paper). Tasks can take outputs of earlier tasks as variables (`search("${1}")`), going beyond OpenAI's "embarrassingly parallel" tool calling.
- Conclusion: the plan-and-execute pattern "separates an LLM-powered 'planner' from the tool execution runtime", reducing latency and cost when many tool/API calls are needed.

## Definitions and terminology
- **Plan-and-execute agent** — design that separates an LLM planner from tool execution.
- **Planner / Executor / Re-planner** — components of the basic Plan-and-Execute architecture.
- **ReAct** — Reasoning and Action; repeated Thought / Act / Observation loop (paper: https://arxiv.org/abs/2210.03629).
- **Chain-of-thought** — prompting technique generating intermediate reasoning (https://arxiv.org/abs/2201.11903).
- **ReWOO** — Reasoning WithOut Observations (https://arxiv.org/abs/2305.18323); components Planner, Worker, Solver; variable references `#E1`, `#E2`…
- **LLMCompiler** — https://arxiv.org/abs/2312.04511; components Planner (streams DAG), Task Fetching Unit, Joiner.
- **Plan-and-Solve Prompting** — Wang et al., https://arxiv.org/abs/2305.04091.
- **BabyAGI** — Yohei Nakajima's project, https://github.com/yoheinakajima/babyagi.
- **DAG** — directed acyclic graph of tasks with dependencies.

## Evidence and examples
- ReAct trajectory (verbatim, from source):
  ```
  Thought: I should call Search() to see the current score of the game.
  Act: Search("What is the current score of game X?")
  Observation: The current score is 24-21
  ... (repeat N times)
  ```
- ReWOO plan for "What are the stats for the quarterbacks of the super bowl contenders this year" (verbatim):
  ```
  Plan: I need to know the teams playing in the superbowl this year
  E1: Search[Who is competing in the superbowl?]
  Plan: I need to know the quarterbacks for each team
  E2: LLM[Quarterback for the first team of #E1]
  Plan: I need to know the quarterbacks for each team
  E3: LLM[Quarter back for the second team of #E1]
  Plan: I need to look up stats for the first quarterback
  E4: Search[Stats for #E2]
  Plan: I need to look up stats for the second quarterback
  E5: Search[Stats for #E3]
  ```
- LLMCompiler variable example: `search("${1}")` — search for queries generated by task 1's output.
- LLMCompiler speedup claim: "the paper claims 3.6x".

## Inconsistencies / open questions
- [verified] The post announces "three agent architectures" and later presents three (Plan-and-Execute, ReWOO, LLMCompiler), but the Background section says "Below are two such designs we have implemented in LangGraph" — checked against the section headings that follow.
- [verified] Typos present in the source text: "While this can be effect for simple tasks" (= effective); "Quarter back" in E3 — preserved verbatim in excerpts.
- [open question] The "3.6x" speedup is attributed to the LLMCompiler paper (Kim et al., arXiv 2312.04511) but not checked — settle by reading the paper's results.
- [open question] The "faster / cheaper / better" claims over ReAct are asserted, not benchmarked in this post — settle against the ReWOO / LLMCompiler papers if the Talk needs numbers.
- [open question] Dated framing: written February 2024 ("Over the past year…"; compares against "OpenAI's parallel tool calling"). Whether these LangGraph example notebook links still resolve in 2026 was not checked.

## Images / diagrams

Content figures (in article body, no alt text; captions from adjacent text):

### `langchain-planning-agents.web/images/69cbb030c588d5fac7b85a9b_plan-and-execute.png`
- Provenance: inline under "Plan-And-Execute", caption "Plan-and-execute Agent" (2000x1337). Original: https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbb030c588d5fac7b85a9b_plan-and-execute.png
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-planning-agents.web/images/69cbb030c588d5fac7b85aaa_rewoo.png`
- Provenance: inline under "Reasoning WithOut Observations", caption "ReWOO Agent" (2000x1323).
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-planning-agents.web/images/69cbb030c588d5fac7b85a9e_llm-compiler-1.png`
- Provenance: inline under "LLMCompiler", caption "LLMCompiler Agent" (2000x1415).
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

Site chrome (avatars, icons, related-post thumbnails — not article content):

### `langchain-planning-agents.web/images/69d50051c5c24f19b81fd73a_Group-2147239256-2.svg`
- Provenance: byline avatar for "The LangChain Team". Original filename `…_Group%202147239256-2.svg`.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-planning-agents.web/images/69ce2c533137196179bae949_Icon-7.svg`
- Provenance: reading-time icon next to the byline.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-planning-agents.web/images/69cd1fd0002272ce39bf1241_Icon-6.svg`
- Provenance: reading-time icon on related-content cards.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-planning-agents.web/images/69ce01ea562f8cc223cabf25_Frame-2147254328.svg`
- Provenance: newsletter form decoration at page bottom.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-planning-agents.web/images/69dcee60745f0e15b18ad4d5_sydney-runkle.png`
- Provenance: author avatar on related-content cards.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-planning-agents.web/images/69dd146b49c3ff6f8c05da14_Eugene-Yurtsev-1.png`
- Provenance: author avatar on related-content card.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-planning-agents.web/images/69e12735c02bb07c894a067a_hunter-lovell.png`
- Provenance: author avatar on related-content cards.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-planning-agents.web/images/6abdc9fb7390b9da2726672e_model-router-webflow-dark-1200x675.png`
- Provenance: related-content thumbnail, alt "How to Build a Model Router in the Harness".
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-planning-agents.web/images/6ab6ba616821ea2bd3edd56a_webflow-cover-light-building-prod-jev-langgraph-1600x900.png`
- Provenance: related-content thumbnail "Building Prod with Jev and LangGraph".
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `langchain-planning-agents.web/images/6aac8ce2e3f50ce7069ae68f_jev-harness-a-title-hero-1600x900.png`
- Provenance: related-content thumbnail "Building a Harness with Jev".
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

## Raw / preserved excerpts

> We're releasing three agent architectures in LangGraph showcasing the "plan-and-execute" style agent design. These agents promise a number of improvements over traditional Reasoning and Action (ReAct)-style agents.
>
> ⏰ First of all, they can execute multi-step workflow ***faster***, since the larger agent doesn't need to be consulted after each action. Each sub-task can be performed without an additional LLM call (or with a call to a lighter-weight LLM).
>
> 💸 Second, they offer **cost savings** over ReAct agents. If LLM calls are used for sub-tasks, they typically can be made to smaller, domain-specific models. The larger model then is only called for (re-)planning steps and to generate the final response.
>
> 🏆 Third, they can **perform better** overall (in terms of task completions rate and quality) by forcing the planner to explicitly "think through" all the steps required to accomplish the entire task. Generating the full reasoning steps is a tried-and-true prompting technique to improve outcomes. Subdividing the problem also permits more focused task execution.

**Background**
> Over the past year, language model-powered agents and state machines have emerged as a promising design pattern for creating flexible and effective ai-powered products.
>
> At their core, agents use LLMs as general-purpose problem-solvers, connecting them with external resources to answer questions or accomplish tasks.
>
> LLM agents typically have the following main steps:
>
> 1. Propose action: the LLM generates text to respond directly to a user or to pass to a function.
> 2. Execute action: your code invokes other software to do things like query a database or call an API.
> 3. Observe: react to the response of the tool call by either calling another function or responding to the user.
>
> The ReAct agent is a great prototypical design for this, as it prompts the language model using a repeated thought, act, observation loop: [trajectory in Evidence above] — A typical ReAct-style agent trajectory.
>
> This takes advantage of Chain-of-thought prompting to make a single action choice per step. While this can be effect for simple tasks, it has a couple main downsides:
>
> 1. It requires an LLM call for each tool invocation.
> 2. The LLM only plans for 1 sub-problem at a time. This may lead to sub-optimal trajectories, since it isn't forced to "reason" about the whole task.
>
> One way to overcome these two shortcomings is through an explicit planning step. Below are two such designs we have implemented in LangGraph.

**Plan-And-Execute**
> Based loosely on Wang, et. al.'s paper on Plan-and-Solve Prompting, and Yohei Nakajima's BabyAGI project, this simple architecture is emblematic of the planning agent architecture. It consists of two basic components:
>
> 1. A **planner**, which prompts an LLM to generate a multi-step plan to complete a large task.
> 2. **Executor**(s), which accept the user query and a step in the plan and invoke 1 or more tools to complete that task.
>
> Once execution is completed, the agent is called again with a re-planning prompt, letting it decide whether to finish with a response or whether to generate a follow-up plan (if the first plan didn't have the desired effect).
>
> This agent design lets us avoid having to call the large planner LLM for each tool invocation. It still is restricted by serial tool calling and uses an LLM for each task since it doesn't support variable assignment.

**Reasoning WithOut Observations**
> In ReWOO, Xu, et. al, propose an agent that removes the need to always use an LLM for each task while still allowing tasks to depend on previous task results. They do so by permitting variable assignment in the planner's output.
>
> Its **planner** generates a plan list consisting of interleaving "Plan" (reasoning) and "E#" lines. [plan in Evidence above]
>
> Notice how the planner can reference previous outputs using syntax like `#E2`. This means it can execute a task list without having to re-plan every time.
>
> The **worker** node loops through each task and assigns the task output to the corresponding variable. It also replaces variables with their results when calling subsequent calls.
>
> Finally, the **Solver** integrates all these outputs into a final answer.
>
> This agent design can be more effective than a naive plan-and-execute agent since each task can have only the required context (its input and variable values).
>
> It still relies on sequential task execution, however, which can create a longer runtime.

**LLMCompiler**
> The **LLMCompiler**, by Kim, et. al., is an agent architecture designed to further increase the **speed** of task execution beyond the plan-and-execute and ReWOO agents described above, and even beyond OpenAI's parallel tool calling.
>
> The LLMCompiler has the following main components:
>
> 1. **Planner**: streams a DAG of tasks. Each task contains a tool, arguments, and list of dependencies.
> 2. **Task Fetching Unit** schedules and executes the tasks. This accepts a stream of tasks. This unit schedules tasks once their dependencies are met. Since many tools involve other calls to search engines or LLMs, the extra parallelism can grant a significant speed boost (the paper claims 3.6x).
> 3. **Joiner**: dynamically replan or finish based on the entire graph history (including task execution results) is an LLM step that decides whether to respond with the final answer or whether to pass the progress back to the (re-)planning agent to continue work.
>
> The key runtime-boosting ideas here are:
>
> - **Planner** outputs are ***streamed;*** the output parser eagerly yields task parameters and their dependencies.
> - The **task fetching unit** receives the parsed task stream and schedules tasks once all their dependencies are satisfied.
> - Task arguments can be *variables,* which are the outputs of previous tasks in the DAG. For instance, the model can call `search("${1}")` to search for queries generated by the output of task 1. This lets the agent work even faster than the "embarrassingly parallel" tool calling in OpenAI.
>
> By formatting tasks as a DAG, the agent can save precious time while invoking tools, leading to an overall better user experience.

**Conclusion**
> These three agent architectures are prototypical of the "plan-and-execute" design pattern, which separates an LLM-powered "planner" from the tool execution runtime. If your application requires multiple tool invocations or API calls, these types of approaches can reduce the time it takes to return a final result and help you save costs by reducing the frequency of calls to more powerful LLMs.
