---
source_file: anthropic-writing-tools-for-agents/
source_type: web-capture
ingested_at: 2026-10-04
---

# Writing effective tools for agents — with agents (Anthropic Engineering)

## Provenance
- Original location: research/web/anthropic-writing-tools-for-agents/ (text from `page.md`; 25,957 chars, 17 headings — no `original.html` fallback needed)
- Format: html (web capture via talksmith:ingest)
- URL: https://www.anthropic.com/engineering/writing-tools-for-agents
- Page title (metadata): "Writing effective tools for AI agents—using AI agents \ Anthropic"; on-page H1: "Writing effective tools for agents — with agents"
- Fetched at: 2026-10-04T14:08:30Z (HTTP 200, 195,460 bytes)
- Author / source (if known): Ken Aizawa, Anthropic, with contributions from Research (Barry Zhang, Zachary Witten, Daniel Jiang, Sami Al-Sheikh, Matt Bell, Maggie Vo), MCP (Theodora Chu, John Welsh, David Soria Parra, Adam Jones), Product Engineering (Santiago Seira), Marketing (Molly Vorwerck), Design (Drew Roper), Applied AI (Christian Ryan, Alexander Bricken)
- Date of original (if known): Published Sep 11, 2025

## Key claims
- "Agents are only as effective as the tools we give them."
- Traditional software is a contract between deterministic systems; **tools are "a new kind of software which reflects a contract between deterministic systems and non-deterministic agents."**
- Given "Should I bring an umbrella today?", an agent might call the weather tool, answer from general knowledge, or ask a clarifying question; it may also hallucinate or misuse a tool.
- Therefore tools must be designed for agents, not written the way one writes functions/APIs for other developers.
- "the tools that are most 'ergonomic' for agents also end up being surprisingly intuitive to grasp as humans."
- Process: build a prototype → run a comprehensive evaluation → collaborate with agents (e.g. Claude Code) to analyze transcripts and improve tools; repeat.
- Evaluation tasks should be realistic and may require many (even dozens of) tool calls; pair each prompt with a verifiable outcome; avoid overly strict verifiers; avoid overspecifying expected tool paths.
- Run evals with simple agentic loops: "`while`-loops wrapping alternating LLM API and tool calls".
- Asking agents to output reasoning/feedback blocks before tool calls "may increase LLMs' effective intelligence by triggering chain-of-thought (CoT) behaviors."
- "what agents omit in their feedback and responses can often be more important than what they include."
- Held-out test sets showed Claude-optimized tools beat even "expert" human-written tool implementations.
- Principles: choose the right tools (fewer, higher-impact, consolidating ones); namespace tools; return meaningful context; optimize responses for token efficiency; prompt-engineer tool descriptions.
- "More tools don't always lead to better outcomes." Wrapping every API endpoint as a tool is a common error, because agents have different "affordances" from traditional software.
- LLM agents have limited context while computer memory is cheap: a `list_contacts` tool that returns everything wastes context; prefer `search_contacts`.
- Resolving UUIDs to semantically meaningful names (or even 0-indexed IDs) "significantly improves Claude's precision in retrieval tasks by reducing hallucinations."
- Claude Code restricts tool responses to 25,000 tokens by default.
- Error responses should be prompt-engineered to give specific, actionable guidance, not opaque codes/tracebacks.
- Tool descriptions are loaded into context and "can collectively steer agents toward effective tool-calling behaviors"; describe the tool as you would to a new hire.
- "Even small refinements to tool descriptions can yield dramatic improvements." Claude Sonnet 3.5 reached state-of-the-art on SWE-bench Verified after precise refinements to tool descriptions.
- Effective tools "are intentionally and clearly defined, use agent context judiciously, can be combined together in diverse workflows, and enable agents to intuitively solve real-world tasks."

## Definitions and terminology
- **Deterministic vs. non-deterministic systems**: deterministic systems produce the same output for identical inputs; non-deterministic systems "like agents" can vary.
- **Tool**: a contract between deterministic systems and non-deterministic agents.
- **Affordances**: the different ways agents perceive the potential actions they can take with tools.
- **Agentic loop** (for evals): while-loop alternating LLM API calls and tool calls.
- **Namespacing**: grouping related tools under common prefixes, by service (`asana_search`, `jira_search`) and/or resource (`asana_projects_search`, `asana_users_search`).
- **`response_format` enum**: parameter letting the agent choose `"concise"` vs `"detailed"` responses (ResponseFormat { DETAILED, CONCISE }).
- **Interleaved thinking**: Claude feature for thinking between tool calls, used to probe why agents do or don't call tools.
- **Tool annotations** (MCP): disclose which tools need open-world access or make destructive changes.
- **MCP / MCP server / DXT (Desktop extension)**: delivery mechanisms for tools — out of scope for this Talk per presenter; the conceptual tool-design content is independent of them.

## Evidence and examples
- Strong eval tasks: schedule meeting with Jane + attach notes + reserve room; Customer ID 9182 charged three times — find logs and check other customers; Sarah Chen cancellation — retention offer with reasons, offer, risk factors.
- Weak eval tasks: "Schedule a meeting with jane@acme.corp next week."; search payment logs for `purchase_complete` and `customer_id=9182`; find cancellation request by Customer ID 45892.
- Metrics to collect beyond accuracy: runtime per tool call and task, number of tool calls, token consumption, tool errors.
- Web search tool anecdote: Claude needlessly appended `2025` to the `query` parameter, biasing results; fixed by improving the tool description.
- Consolidation examples: `schedule_event` instead of `list_users` + `list_events` + `create_event`; `search_logs` instead of `read_logs`; `get_customer_context` instead of `get_customer_by_id` + `list_transactions` + `list_notes`.
- Prefix- vs suffix-based namespacing had "non-trivial effects" on evals; effects vary by LLM.
- Agent failure modes with tools: call the wrong tools, call the right tools with the wrong parameters, call too few tools, process responses incorrectly.
- Low-signal fields to avoid: `uuid`, `256px_image_url`, `mime_type`; prefer `name`, `image_url`, `file_type`.
- Detailed Slack tool response: 206 tokens; concise: 72 tokens (~1/3); concise omits `thread_ts`, `channel_id`, `user_id`.
- Response structure (XML, JSON, Markdown) affects eval performance; no one-size-fits-all.
- Parameter naming: `user_id` instead of `user`.
- Figures: held-out test set accuracy of human-written vs. Claude-optimized Slack and Asana MCP servers (numbers only in images — pending transcription).

## Inconsistencies / open questions
- [verified] "~⅓ of the tokens" for concise responses is consistent with the stated token counts — checked: 72 / 206 ≈ 0.35.
- [verified] "systems1." and the trailing "1Beyond training the underlying LLMs themselves." are a footnote marker flattened by extraction, not part of the prose — checked in `page.md`: the footnote text appears after the acknowledgements. Read as "…agentic AI systems¹" with footnote "¹ Beyond training the underlying LLMs themselves."
- [verified] "the[SWE-bench Verified]" lacks a space in `page.md` (line 210) — cosmetic extraction artifact; meaning unaffected.
- [open question] The page title in metadata ("Writing effective tools for AI agents—using AI agents") differs from the on-page H1 ("Writing effective tools for agents — with agents"). Either is citable; pick one consistently in `Sources`.
- [open question] The Slack/Asana accuracy charts carry the only quantitative results of the post; their numbers are not in the text. Phase 2 transcription is needed before the deck quotes any figure from them.
- [open question] The article is framed around MCP servers (out of scope for this Talk). The tool-design principles transfer to plain function-calling tools, but the source does not say so explicitly; the Editor should present them as general principles "según Anthropic" without introducing MCP.

## Images / diagrams

### `anthropic-writing-tools-for-agents.web/images/876165247ba5668bd195854eef4631ad9a184001-1000x1000.svg`
- Provenance: page hero; https://www-cdn.anthropic.com/images/4zrzovbb/website/876165247ba5668bd195854eef4631ad9a184001-1000x1000.svg; alt="This is an abstract illustration for the Eng Blog article, Writing effective tools for agents -- with agents."
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-writing-tools-for-agents.web/images/image.png`
- Provenance: figure after the intro bullet list; raw asset `assets/image.bin` (PNG 1920x1080), from .../cdc027ad2730e4732168bb198fc9363678544f99-1920x1080.png. Alt: "This is an image depicting how an engineer might use Claude Code to evaluate the efficacy of agentic tools." Caption: "Building an evaluation allows you to systematically measure the performance of your tools. You can use Claude Code to automatically optimize your tools against this evaluation."
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-writing-tools-for-agents.web/images/image-2.webp`
- Provenance: figure in "Running an evaluation"; raw asset `assets/image-2.bin` (WebP), from .../6e810aee67f3f3c955832fb7bf9033ffb0102000-1920x1080.png. Alt: "This graph measures the test set accuracy of human-written vs. Claude-optimized Slack MCP servers." Caption: "Held-out test set performance of our internal Slack tools".
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-writing-tools-for-agents.web/images/image-3.webp`
- Provenance: figure in "Running the evaluation"; raw asset `assets/image-3.bin` (WebP), from .../3f1f47e80974750cd924bc51e42b6df1ad997fab-1920x1080.png. Alt: "This graph measures the test set accuracy of human-written vs. Claude-optimized Asana MCP servers." Caption: "Held-out test set performance of our internal Asana tools".
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-writing-tools-for-agents.web/images/image-4.webp`
- Provenance: figure in "Returning meaningful context from your tools"; raw asset `assets/image-4.bin` (WebP), from .../5ed0d30526bf68624f335d075b8c1541be3bb595-1920x1006.png. Alt: "This code snippet depicts an example of a detailed tool response." Preceding text: "Here's an example of a detailed tool response (206 tokens):"
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-writing-tools-for-agents.web/images/image-5.webp`
- Provenance: same section; raw asset `assets/image-5.bin` (WebP), from .../d4f649a66482efb5a80cf14ea85e84974ede1c49-1920x725.png. Alt: "This code snippet depicts a concise tool response." Preceding text: "Here's an example of a concise tool response (72 tokens):" Caption: Slack `thread_ts` explanation (verbatim in Raw excerpts).
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-writing-tools-for-agents.web/images/image-6.webp`
- Provenance: "Optimizing tool responses for token efficiency"; raw asset `assets/image-6.bin` (WebP), from .../e440d6a69d0ca80e71f3bec5c2d00906ff03ce6d-1920x1162.png. Alt: "This image depicts an example of a truncated tool response."
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-writing-tools-for-agents.web/images/image-7.webp`
- Provenance: same section; raw asset `assets/image-7.bin` (WebP), from .../2445187904704fec8c50af0b950e310ba743fac2-1920x733.png. Alt: "This image depicts an example of an unhelpful tool response." Preceding text: "Here's an example of an unhelpful error response:"
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-writing-tools-for-agents.web/images/image-8.webp`
- Provenance: same section; raw asset `assets/image-8.bin` (WebP), from .../810661bd44a35fb273806ae95160040155978c3e-1920x850.png. Alt: "This image depicts an example of a helpful error response." Caption: "Tool truncation and error responses can steer agents towards more token-efficient tool-use behaviors (using filters or pagination) or give examples of correctly formatted tool inputs."
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `anthropic-writing-tools-for-agents.web/images/43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg`
- Provenance: footer decoration ("Looking to learn more? Explore courses"); https://www-cdn.anthropic.com/images/4zrzovbb/website/43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg; alt="Interlocking puzzle piece with complex geometric shape and detailed surface texture". Site chrome; same file also appears in anthropic-multi-agent-research-system.web.
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

## Raw / preserved excerpts

> Agents are only as effective as the tools we give them. We share how to write high-quality tools and evaluations, and how you can boost performance by using Claude to optimize its tools for itself.
>
> The Model Context Protocol (MCP) can empower LLM agents with potentially hundreds of tools to solve real-world tasks. But how do we make those tools maximally effective?
>
> We begin by covering how you can:
> - Build and test prototypes of your tools
> - Create and run comprehensive evaluations of your tools with agents
> - Collaborate with agents like Claude Code to automatically increase the performance of your tools
>
> We conclude with key principles for writing high-quality tools we've identified along the way:
> - Choosing the right tools to implement (and not to implement)
> - Namespacing tools to define clear boundaries in functionality
> - Returning meaningful context from tools back to agents
> - Optimizing tool responses for token efficiency
> - Prompt-engineering tool descriptions and specs

**What is a tool?**

> In computing, deterministic systems produce the same output every time given identical inputs, while *non-deterministic* systems—like agents—can generate varied responses even with the same starting conditions.
>
> When we traditionally write software, we're establishing a contract between deterministic systems. For instance, a function call like `getWeather("NYC")` will always fetch the weather in New York City in the exact same manner every time it is called.
>
> Tools are a new kind of software which reflects a contract between deterministic systems and non-deterministic agents. When a user asks "Should I bring an umbrella today?," an agent might call the weather tool, answer from general knowledge, or even ask a clarifying question about location first. Occasionally, an agent might hallucinate or even fail to grasp how to use a tool.
>
> This means fundamentally rethinking our approach when writing software for agents: instead of writing tools and MCP servers the way we'd write functions and APIs for other developers or systems, we need to design them for agents.
>
> Our goal is to increase the surface area over which agents can be effective in solving a wide range of tasks by using tools to pursue a variety of successful strategies. Fortunately, in our experience, the tools that are most "ergonomic" for agents also end up being surprisingly intuitive to grasp as humans.

**How to write tools (intro)**

> In this section, we describe how you can collaborate with agents both to write and to improve the tools you give them. Start by standing up a quick prototype of your tools and testing them locally. Next, run a comprehensive evaluation to measure subsequent changes. Working alongside agents, you can repeat the process of evaluating and improving your tools until your agents achieve strong performance on real-world tasks.

**Generating evaluation tasks**

> With your early prototype, Claude Code can quickly explore your tools and create dozens of prompt and response pairs. Prompts should be inspired by real-world uses and be based on realistic data sources and services (for example, internal knowledge bases and microservices). We recommend you avoid overly simplistic or superficial "sandbox" environments that don't stress-test your tools with sufficient complexity. Strong evaluation tasks might require multiple tool calls—potentially dozens.
>
> Each evaluation prompt should be paired with a verifiable response or outcome. Your verifier can be as simple as an exact string comparison between ground truth and sampled responses, or as advanced as enlisting Claude to judge the response. Avoid overly strict verifiers that reject correct responses due to spurious differences like formatting, punctuation, or valid alternative phrasings.
>
> For each prompt-response pair, you can optionally also specify the tools you expect an agent to call in solving the task, to measure whether or not agents are successful in grasping each tool's purpose during evaluation. However, because there might be multiple valid paths to solving tasks correctly, try to avoid overspecifying or overfitting to strategies.

**Running the evaluation**

> We recommend running your evaluation programmatically with direct LLM API calls. Use simple agentic loops (`while`-loops wrapping alternating LLM API and tool calls): one loop for each evaluation task. Each evaluation agent should be given a single task prompt and your tools.
>
> In your evaluation agents' system prompts, we recommend instructing agents to output not just structured response blocks (for verification), but also reasoning and feedback blocks. Instructing agents to output these *before* tool call and response blocks may increase LLMs' effective intelligence by triggering chain-of-thought (CoT) behaviors.
>
> If you're running your evaluation with Claude, you can turn on interleaved thinking for similar functionality "off-the-shelf". This will help you probe why agents do or don't call certain tools and highlight specific areas of improvement in tool descriptions and specs.
>
> As well as top-level accuracy, we recommend collecting other metrics like the total runtime of individual tool calls and tasks, the total number of tool calls, the total token consumption, and tool errors. Tracking tool calls can help reveal common workflows that agents pursue and offer some opportunities for tools to consolidate.

**Analyzing results**

> Agents are your helpful partners in spotting issues and providing feedback on everything from contradictory tool descriptions to inefficient tool implementations and confusing tool schemas. However, keep in mind that what agents omit in their feedback and responses can often be more important than what they include. LLMs don't always say what they mean.
>
> Observe where your agents get stumped or confused. Read through your evaluation agents' reasoning and feedback (or CoT) to identify rough edges. Review the raw transcripts (including tool calls and tool responses) to catch any behavior not explicitly described in the agent's CoT. Read between the lines; remember that your evaluation agents don't necessarily know the correct answers and strategies.
>
> Analyze your tool calling metrics. Lots of redundant tool calls might suggest some rightsizing of pagination or token limit parameters is warranted; lots of tool errors for invalid parameters might suggest tools could use clearer descriptions or better examples. When we launched Claude's web search tool, we identified that Claude was needlessly appending `2025` to the tool's `query` parameter, biasing search results and degrading performance (we steered Claude in the right direction by improving the tool description).

**Collaborating with agents**

> You can even let agents analyze your results and improve your tools for you. Simply concatenate the transcripts from your evaluation agents and paste them into Claude Code. Claude is an expert at analyzing transcripts and refactoring lots of tools all at once—for example, to ensure tool implementations and descriptions remain self-consistent when new changes are made.
>
> In fact, most of the advice in this post came from repeatedly optimizing our internal tool implementations with Claude Code. Our evaluations were created on top of our internal workspace, mirroring the complexity of our internal workflows, including real projects, documents, and messages.
>
> We relied on held-out test sets to ensure we did not overfit to our "training" evaluations. These test sets revealed that we could extract additional performance improvements even beyond what we achieved with "expert" tool implementations—whether those tools were manually written by our researchers or generated by Claude itself.

**Choosing the right tools for agents**

> More tools don't always lead to better outcomes. A common error we've observed is tools that merely wrap existing software functionality or API endpoints—whether or not the tools are appropriate for agents. This is because agents have distinct "affordances" to traditional software—that is, they have different ways of perceiving the potential actions they can take with those tools
>
> LLM agents have limited "context" (that is, there are limits to how much information they can process at once), whereas computer memory is cheap and abundant. Consider the task of searching for a contact in an address book. Traditional software programs can efficiently store and process a list of contacts one at a time, checking each one before moving on.
>
> However, if an LLM agent uses a tool that returns ALL contacts and then has to read through each one token-by-token, it's wasting its limited context space on irrelevant information (imagine searching for a contact in your address book by reading each page from top-to-bottom—that is, via brute-force search). The better and more natural approach (for agents and humans alike) is to skip to the relevant page first (perhaps finding it alphabetically).
>
> We recommend building a few thoughtful tools targeting specific high-impact workflows, which match your evaluation tasks and scaling up from there. In the address book case, you might choose to implement a `search_contacts` or `message_contact` tool instead of a `list_contacts` tool.
>
> Tools can consolidate functionality, handling potentially *multiple* discrete operations (or API calls) under the hood. For example, tools can enrich tool responses with related metadata or handle frequently chained, multi-step tasks in a single tool call.
>
> Make sure each tool you build has a clear, distinct purpose. Tools should enable agents to subdivide and solve tasks in much the same way that a human would, given access to the same underlying resources, and simultaneously reduce the context that would have otherwise been consumed by intermediate outputs.
>
> Too many tools or overlapping tools can also distract agents from pursuing efficient strategies. Careful, selective planning of the tools you build (or don't build) can really pay off.

**Namespacing your tools**

> Your AI agents will potentially gain access to dozens of MCP servers and hundreds of different tools–including those by other developers. When tools overlap in function or have a vague purpose, agents can get confused about which ones to use.
>
> Namespacing (grouping related tools under common prefixes) can help delineate boundaries between lots of tools; MCP clients sometimes do this by default. For example, namespacing tools by service (e.g., `asana_search`, `jira_search`) and by resource (e.g., `asana_projects_search`, `asana_users_search`), can help agents select the right tools at the right time.
>
> We have found selecting between prefix- and suffix-based namespacing to have non-trivial effects on our tool-use evaluations. Effects vary by LLM and we encourage you to choose a naming scheme according to your own evaluations.
>
> Agents might call the wrong tools, call the right tools with the wrong parameters, call too few tools, or process tool responses incorrectly. By selectively implementing tools whose names reflect natural subdivisions of tasks, you simultaneously reduce the number of tools and tool descriptions loaded into the agent's context and offload agentic computation from the agent's context back into the tool calls themselves. This reduces an agent's overall risk of making mistakes.

**Returning meaningful context from your tools**

> In the same vein, tool implementations should take care to return only high signal information back to agents. They should prioritize contextual relevance over flexibility, and eschew low-level technical identifiers (for example: `uuid`, `256px_image_url`, `mime_type`). Fields like `name`, `image_url`, and `file_type` are much more likely to directly inform agents' downstream actions and responses.
>
> Agents also tend to grapple with natural language names, terms, or identifiers significantly more successfully than they do with cryptic identifiers. We've found that merely resolving arbitrary alphanumeric UUIDs to more semantically meaningful and interpretable language (or even a 0-indexed ID scheme) significantly improves Claude's precision in retrieval tasks by reducing hallucinations.
>
> In some instances, agents may require the flexibility to interact with both natural language and technical identifiers outputs, if only to trigger downstream tool calls (for example, `search_user(name='jane')` → `send_message(id=12345)`). You can enable both by exposing a simple `response_format` enum parameter in your tool, allowing your agent to control whether tools return `"concise"` or `"detailed"` responses.

```
enum ResponseFormat {
   DETAILED = "detailed",
   CONCISE = "concise"
}
```

> Slack threads and thread replies are identified by unique `thread_ts` which are required to fetch thread replies. `thread_ts` and other IDs (`channel_id`, `user_id`) can be retrieved from a `"detailed"` tool response to enable further tool calls that require these. `"concise"` tool responses return only thread content and exclude IDs. In this example, we use ~⅓ of the tokens with `"concise"` tool responses.
>
> Even your tool response structure—for example XML, JSON, or Markdown—can have an impact on evaluation performance: there is no one-size-fits-all solution. This is because LLMs are trained on next-token prediction and tend to perform better with formats that match their training data. The optimal response structure will vary widely by task and agent. We encourage you to select the best response structure based on your own evaluation.

**Optimizing tool responses for token efficiency**

> Optimizing the quality of context is important. But so is optimizing the *quantity* of context returned back to agents in tool responses.
>
> We suggest implementing some combination of pagination, range selection, filtering, and/or truncation with sensible default parameter values for any tool responses that could use up lots of context. For Claude Code, we restrict tool responses to 25,000 tokens by default. We expect the effective context length of agents to grow over time, but the need for context-efficient tools to remain.
>
> If you choose to truncate responses, be sure to steer agents with helpful instructions. You can directly encourage agents to pursue more token-efficient strategies, like making many small and targeted searches instead of a single, broad search for a knowledge retrieval task. Similarly, if a tool call raises an error (for example, during input validation), you can prompt-engineer your error responses to clearly communicate specific and actionable improvements, rather than opaque error codes or tracebacks.

**Prompt-engineering your tool descriptions**

> We now come to one of the most effective methods for improving tools: prompt-engineering your tool descriptions and specs. Because these are loaded into your agents' context, they can collectively steer agents toward effective tool-calling behaviors.
>
> When writing tool descriptions and specs, think of how you would describe your tool to a new hire on your team. Consider the context that you might implicitly bring—specialized query formats, definitions of niche terminology, relationships between underlying resources—and make it explicit. Avoid ambiguity by clearly describing (and enforcing with strict data models) expected inputs and outputs. In particular, input parameters should be unambiguously named: instead of a parameter named `user`, try a parameter named `user_id`.
>
> With your evaluation you can measure the impact of your prompt engineering with greater confidence. Even small refinements to tool descriptions can yield dramatic improvements. Claude Sonnet 3.5 achieved state-of-the-art performance on the SWE-bench Verified evaluation after we made precise refinements to tool descriptions, dramatically reducing error rates and improving task completion.

**Looking ahead**

> To build effective tools for agents, we need to re-orient our software development practices from predictable, deterministic patterns to non-deterministic ones.
>
> Through the iterative, evaluation-driven process we've described in this post, we've identified consistent patterns in what makes tools successful: Effective tools are intentionally and clearly defined, use agent context judiciously, can be combined together in diverse workflows, and enable agents to intuitively solve real-world tasks.
>
> In the future, we expect the specific mechanisms through which agents interact with the world to evolve—from updates to the MCP protocol to upgrades to the underlying LLMs themselves. With a systematic, evaluation-driven approach to improving tools for agents, we can ensure that as agents become more capable, the tools they use will evolve alongside them.
