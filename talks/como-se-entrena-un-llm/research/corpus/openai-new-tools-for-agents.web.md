---
source_file: openai-new-tools-for-agents
source_type: web-capture
ingested_at: 2026-09-27
---

# New tools for building agents (OpenAI blog, March 11, 2025)

## Provenance
- Original location: web/openai-new-tools-for-agents/ (text from `page.md`; `page.md` is 22153 chars with 16 heading lines, so no `original.html` fallback was needed. `original.html` was cross-checked by keyword for the SimpleQA chart, whose bar labels are missing from `page.md`; see Inconsistencies.)
- Format: html (web capture via talksmith:ingest of an openai.com blog post)
- URL: https://openai.com/index/new-tools-for-building-agents/
- Captured at: 2026-09-27T18:17:20Z (HTTP 200, 516982 bytes)
- Page title: New tools for building agents | OpenAI
- Author / source (if known): OpenAI (byline "Authors: OpenAI"; category "Product"; tags "API Platform", "2025"). This is a **vendor product announcement**: OpenAI describing its own API launch. Benchmark numbers are OpenAI's own. Not an independent source.
- Date of original (if known): **March 11, 2025** (printed at the top of the post). Blog captured 2026-09-27. Everything the post says about availability, pricing, "preview" status and the Assistants API sunset is as of March 2025, not as of the capture date.
- Images: the capture carried 1 image, the post's hero (`API_Agents_Hero_16.9.png`, 3840 x 2160 px). It is above the 300 px threshold and was copied to the companion folder as `openai-new-tools-for-agents.web/images/API_Agents_Hero_16.9.webp`. It was renamed from `.png` to `.webp` because the bytes are WebP (`file`: "RIFF ... Web/P image, VP8 encoding, 3840x2160"; the source URL requested `fm=webp`). Bytes are identical to the raw asset (`cmp`).

## Key claims
Relevance for the Talk: this post is the **hosted-platform** counterpoint to self-served tool calling (vLLM, Ollama). Here the platform provides the tools itself ("built-in tools") on top of the model API.

- **Date and scope:** posted March 11, 2025. "Today, we’re releasing the first set of building blocks that will help developers and enterprises build useful and reliable agents."
- **Definition of agent:** "We view agents as systems that independently accomplish tasks on behalf of users."
- **What launched (verbatim list):**
  - "The new Responses API, combining the simplicity of the Chat Completions API with the tool use capabilities of the Assistants API for building agents"
  - "Built-in tools including web search, file search, and computer use"
  - "The new Agents SDK to orchestrate single-agent and multi-agent workflows"
  - "Integrated observability tools to trace and inspect agent workflow execution"
- **Responses API as the vehicle for OpenAI's own tools:** "The Responses API is our new API primitive for leveraging OpenAI’s built-in tools to build agents. It combines the simplicity of Chat Completions with the tool-use capabilities of the Assistants API." "With a single Responses API call, developers will be able to solve increasingly complex tasks using multiple tools and model turns."
- **Built-in tools, and no third-party integration needed:** "To start, the Responses API will support new built-in tools like web search, file search, and computer use. These tools are designed to work together to connect models to the real world". "The Responses API is designed for developers who want to easily combine OpenAI models and built-in tools into their apps, without the complexity of integrating multiple APIs or external vendors."
- **Data can live on OpenAI:** "The API also makes it easier to store data on OpenAI so developers can evaluate agent performance using features such as tracing and evaluations." "we do not train our models on business data by default, even when the data is stored on OpenAI."
- **Billing:** "The API is available to all developers starting today and is not charged separately—tokens and tools are billed at standard rates".
- **Web search, run on OpenAI's side:** "In the Responses API, web search is available as a tool when using gpt-4o and gpt-4o-mini, and can be paired with other tools or function calls." "Web search in the API is powered by the same model used for ChatGPT search." Tool type in code: `{ type: "web_search_preview" }`. Available "to all developers in preview in the Responses API". Pricing "starts respectively at $30 and $25 per thousand queries for GPT‑4o search and 4o-mini search".
- **File search, over vector stores hosted by OpenAI:** "retrieve relevant information from large volumes of documents using the improved file search tool. With support for multiple file types, query optimization, metadata filtering, and custom reranking". Code creates `openai.vectorStores.create({...file_ids...})` and passes `{type: "file_search", vector_store_ids: [...]}`. "$2.50 per thousand queries and file storage at $0.10/GB/day, with the first GB free."
- **Computer use: the model proposes actions, and the developer's environment runs them:** "The built-in computer use tool captures mouse and keyboard actions generated by the model, making it possible for developers to automate computer use tasks by directly translating these actions into executable commands within their environments." Powered by the "Computer-Using Agent (CUA) model that enables Operator". Tool type `computer_use_preview`, model `computer-use-preview`. "research preview in the Responses API for select developers in usage tiers 3-5"; "$3/1M input tokens and $12/1M output tokens".
- **Function calls still coexist:** web search "can be paired with other tools or function calls"; the Agents SDK example uses `@function_tool` for the developer's own `submit_refund_request` ("# Your refund logic goes here") next to the built-in `WebSearchTool()`.
- **Existing APIs:** Chat Completions "remains our most widely adopted API"; "the Responses API is a superset of Chat Completions [...] so for new integrations, we recommend starting with the Responses API." Assistants API: "we plan to formally announce the deprecation of the Assistants API with a target sunset date in mid-2026."
- **Agents SDK:** "open-source", improves over Swarm; primitives "Agents", "Handoffs", "Guardrails", "Tracing & Observability". "The SDK will also work with models from other providers, as long as they provide a Chat Completions style API endpoint."
- **Safety caveat for computer use:** "the model is still susceptible to inadvertent mistakes, especially in non-browser environments. [...] CUA’s performance on OSWorld [...] is currently at 38.1%, indicating that the model is not yet highly reliable for automating tasks on operating systems. Human oversight is recommended in these scenarios."

## Definitions and terminology
- **Agent**: "systems that independently accomplish tasks on behalf of users."
- **Responses API**: OpenAI's API primitive (launched March 11, 2025) for model calls with built-in tools and multiple model turns; "a superset of Chat Completions". SDK helper `response.output_text`; "unified item-based design, simpler polymorphism, intuitive streaming events".
- **Built-in tools**: tools that OpenAI provides inside the Responses API (web search, file search, computer use). The developer declares them by `type` (`web_search_preview`, `file_search`, `computer_use_preview`); they are not functions the developer writes.
- **Function calls / function tools**: the developer's own functions (`@function_tool` in the Agents SDK), as opposed to built-in tools.
- **Vector store**: OpenAI-hosted index of uploaded files used by file search (`openai.vectorStores.create`); also has "a new search endpoint to Vector Store API objects".
- **CUA (Computer-Using Agent)**: the model behind Operator and the computer use tool.
- **Agents SDK**: open-source orchestration library (successor to Swarm) with Agents, Handoffs, Guardrails, Tracing.
- **Handoffs**: "Intelligently transfer control between agents."
- **Guardrails**: "Configurable safety checks for input and output validation."

## Evidence and examples
- **Web search call (verbatim):**
  ```
  const response = await openai.responses.create({
      model: "gpt-4o",
      tools: [ { type: "web_search_preview" } ],
      input: "What was a positive news story that happened today?",
  });

  console.log(response.output_text);
  ```
- **File search call (verbatim):**
  ```
  const productDocs = await openai.vectorStores.create({
      name: "Product Documentation",
      file_ids: [file1.id, file2.id, file3.id],
  });

  const response = await openai.responses.create({
      model: "gpt-4o-mini",
      tools: [{
          type: "file_search",
          vector_store_ids: [productDocs.id],
      }],
      input: "What is deep research by OpenAI?",
  });

  console.log(response.output_text);
  ```
- **Computer use call (verbatim):** `model: "computer-use-preview"`, `tools: [{ type: "computer_use_preview", display_width: 1024, display_height: 768, environment: "browser" }]`, `truncation: "auto"`; it prints `response.output`, not `output_text` (full block in excerpts).
- **Benchmarks (OpenAI's numbers):** SimpleQA: "GPT‑4o search preview and GPT‑4o mini search preview score 90% and 88% respectively." CUA: OSWorld 38.1% (previous SOTA 22.0%, human 72.4%); WebArena 58.1% (previous SOTA 36.2% computer use / 57.1% web-browsing agents; human 78.2%); WebVoyager 87.0% (previous SOTA 56.0% / 87.0%).
- **Customer examples:** Hebbia (web search), Navan (file search, "dedicated vector stores for each user group"), Unify and Luminai (computer use), Coinbase AgentKit and Box (Agents SDK).

## Inconsistencies / open questions
- [verified] The post does not state in one sentence that built-in tools *execute on OpenAI's servers*. What it says: they are "OpenAI’s built-in tools", usable "without the complexity of integrating multiple APIs or external vendors"; web search is "powered by the same model used for ChatGPT search"; file search runs over vector stores created through OpenAI's API. Check: searched `page.md` for "server", "hosted", "execute" (no hits) and read each tool section. For web search and file search, "run by OpenAI" is a fair reading of those sentences.
- [verified] **Computer use is the exception: the post says the developer executes the actions.** "captures mouse and keyboard actions generated by the model, making it possible for developers to automate computer use tasks by directly translating these actions into executable commands within their environments." Check: `page.md`, Computer use section. A slide that says "all three built-in tools are run by OpenAI" would overstate this source.
- [verified] The SimpleQA bar chart has six values (63%, 38%, 47%, 15%, 90%, 88%) but only the last two are identified in the text (GPT‑4o search preview 90%, GPT‑4o mini search preview 88%). Check: `original.html` chart markup contains only the `<tspan>` value labels and the axis label "Accuracy"; no bar names. The four other bars cannot be attributed from this capture.
- [verified] The benchmark table was flattened by the capture into one line. Check: `page.md`. Re-laid out in the excerpt by column order of the header row. One judgement call: the header lists "Computer use (universal interface)" and "Web browsing agents" as groups over "OpenAI CUA / Previous SOTA / Previous SOTA", and the librarian assigned the first "Previous SOTA" to computer use and the second to web browsing agents. The OSWorld row has "-" in the web-browsing column, which fits that reading.
- [open question] Status as of the capture date (2026-09-27) is not settled by this March 2025 post: whether the Assistants API was sunset ("target sunset date in mid-2026"), whether tool type names are still `web_search_preview` / `computer_use_preview`, whether computer use is still a research preview limited to tiers 3-5, and whether the quoted prices still hold. Settled by current OpenAI API docs, pricing page and deprecations page.
- [open question] "Node.js support coming soon" for the Agents SDK is dated March 2025; current status unchecked. Settled by the Agents SDK docs.

## Images / diagrams

### openai-new-tools-for-agents.web/images/API_Agents_Hero_16.9.webp
- Provenance: hero image of the post, captured by `talksmith:ingest` from `https://images.ctfassets.net/kftzwdyauwt9/4QaBJvGYlSBY9iYMhWBN6I/c97e4a784aef38012d91e9a9cf2010c7/API_Agents_Hero_16.9.png?w=3840&q=90&fm=webp` as `web/openai-new-tools-for-agents/assets/API_Agents_Hero_16.9.png`. WebP bytes, 3840 x 2160 px. Page alt text (from the source, not a transcription): "A sleek, minimal interface displaying a task list for an AI agent, including ‘triage_agent,’ ‘guardrail,’ and ‘update_salesforce_record,’ over a fluid blue abstract background."
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

## Raw / preserved excerpts
The complete post body as captured in `page.md` (from the H1 "New tools for building agents" to the end of "What’s next"), with the site navigation, "(opens in a new window)" link suffixes and the trailing tag links removed. Headings are demoted by two levels (capped at level 6). The hero image line is replaced by a pointer to `Images / diagrams`. The four code blocks were captured with their line numbers fused into the code (e.g. `});6  `); the librarian restored them to clean code with the same content, cross-checked line by line against the numbered capture. The SimpleQA chart values and the benchmark table were flattened by the capture and are re-laid out as noted inline.

Date line from the capture: "March 11, 2025 · Product". Byline at the end: "Authors: OpenAI". Tags: "API Platform", "2025".

### New tools for building agents

[Try in Playground](https://platform.openai.com/playground/chat?preset=ks7kayjX55ehTBR9oyUviuJe)

[Hero image, alt text: "A sleek, minimal interface displaying a task list for an AI agent, including ‘triage_agent,’ ‘guardrail,’ and ‘update_salesforce_record,’ over a fluid blue abstract background." See Images / diagrams: openai-new-tools-for-agents.web/images/API_Agents_Hero_16.9.webp]

Today, we’re releasing the first set of building blocks that will help developers and enterprises build useful and reliable agents. We view agents as systems that independently accomplish tasks on behalf of users. Over the past year, we’ve introduced new model capabilities—such as advanced reasoning, multimodal interactions, and new safety techniques—that have laid the foundation for our models to handle the complex, multi-step tasks required to build agents. However, customers have shared that turning these capabilities into production-ready agents can be challenging, often requiring extensive prompt iteration and custom orchestration logic without sufficient visibility or built-in support.

To address these challenges, we’re launching a new set of APIs and tools specifically designed to simplify the development of agentic applications:

- The new [Responses API](https://platform.openai.com/docs/quickstart?api-mode=responses), combining the simplicity of the Chat Completions API with the tool use capabilities of the Assistants API for building agents

- Built-in tools including [web search](https://platform.openai.com/docs/guides/tools-web-search), [file search](https://platform.openai.com/docs/guides/tools-file-search), and [computer use](https://platform.openai.com/docs/guides/tools-computer-use)

- The new [Agents SDK](https://platform.openai.com/docs/guides/agents) to orchestrate single-agent and multi-agent workflows

- Integrated [observability tools](https://platform.openai.com/docs/guides/agents#orchestration) to trace and inspect agent workflow execution

These new tools streamline core agent logic, orchestration, and interactions, making it significantly easier for developers to get started with building agents. Over the coming weeks and months, we plan to release additional tools and capabilities to further simplify and accelerate building agentic applications on our platform.

#### Introducing the Responses API

The Responses API is our new API primitive for leveraging OpenAI’s built-in tools to build agents. It combines the simplicity of Chat Completions with the tool-use capabilities of the Assistants API. As model capabilities continue to evolve, we believe the Responses API will provide a more flexible foundation for developers building agentic applications. With a single Responses API call, developers will be able to solve increasingly complex tasks using multiple tools and model turns.

To start, the Responses API will support new built-in tools like web search, file search, and computer use. These tools are designed to work together to connect models to the real world, making them more useful in completing tasks. It also brings with it several usability improvements including a unified item-based design, simpler polymorphism, intuitive streaming events, and SDK helpers like `response.output_text` to easily access the model’s text output.

The Responses API is designed for developers who want to easily combine OpenAI models and built-in tools into their apps, without the complexity of integrating multiple APIs or external vendors. The API also makes it easier to store data on OpenAI so developers can evaluate agent performance using features such as tracing and evaluations. As a reminder, we [do not train](/enterprise-privacy/) our models on business data by default, even when the data is stored on OpenAI. The API is available to all developers starting today and is not charged separately—tokens and tools are billed at standard rates specified on our [pricing page](https://platform.openai.com/docs/pricing). Check out the Responses API [quickstart guide](https://platform.openai.com/docs/quickstart?api-mode=responses) to learn more.

#### What this means for existing APIs

- [Chat Completions API](https://platform.openai.com/docs/guides/text-generation): Chat Completions remains our most widely adopted API, and we’re fully committed to supporting it with new models and capabilities. Developers who don’t require built-in tools can confidently continue using Chat Completions. We’ll keep releasing new models to Chat Completions whenever their capabilities don’t depend on built-in tools or multiple model calls. However, the Responses API is a [superset](https://platform.openai.com/docs/guides/responses-vs-chat-completions) of Chat Completions with the same great performance, so for new integrations, we recommend starting with the Responses API.

- [Assistants API](https://platform.openai.com/docs/assistants/overview): Based on developer feedback from the Assistants API beta, we’ve incorporated key improvements into the Responses API, making it more flexible, faster, and easier to use. We’re working to achieve full feature parity between the Assistants and the Responses API, including support for Assistant-like and Thread-like objects, and the Code Interpreter tool. Once this is complete, we plan to formally announce the deprecation of the Assistants API with a target sunset date in mid-2026. Upon deprecation, we will provide a clear migration guide from the Assistants API to the Responses API that allows developers to preserve all their data and migrate their applications. Until we formally announce the deprecation, we will continue delivering new models to the Assistants API. The Responses API represents the future direction for building agents on OpenAI.

#### Introducing built-in tools in the Responses API

#### Web search

Developers can now get fast, up-to-date answers with clear and relevant citations from the web. In the Responses API, web search is available as a tool when using gpt-4o and gpt-4o-mini, and can be paired with other tools or function calls.

###### JavaScript

```
const response = await openai.responses.create({
    model: "gpt-4o",
    tools: [ { type: "web_search_preview" } ],
    input: "What was a positive news story that happened today?",
});

console.log(response.output_text);
```

During early testing, we’ve seen developers build with web search for a variety of use cases including shopping assistants, research agents, and travel booking agents—any application that requires timely information from the web.

For example, [Hebbia](https://www.hebbia.com/) leverages the web search tool to help asset managers, private equity and credit firms, and law practices quickly extract actionable insights from extensive public and private datasets. By integrating real-time search capabilities into their research workflows, Hebbia delivers richer, context-specific market intelligence and continuously improves the precision and relevance of their analyses, outperforming current benchmarks.

Web search in the API is powered by the same model used for ChatGPT search. On SimpleQA, a benchmark that evaluates the accuracy of LLMs in answering short, factual questions, GPT‑4o search preview and GPT‑4o mini search preview score 90% and 88% respectively.

###### SimpleQA Accuracy (higher is better)

[Bar chart; captured values only, bar labels not in capture: 63% · 38% · 47% · 15% · 90% · 88% · axis "Accuracy"]

Responses generated with web search in the API include links to sources, such as news articles and blog posts, giving users a way to learn more. With these clear, inline citations, users can engage with information in a new way, while content owners gain new opportunities to reach a broader audience.

Any website or publisher can [choose to appear](https://platform.openai.com/docs/bots) in web search in the API.

The web search tool is available to all developers in preview in the Responses API. We are also giving developers direct access to our fine-tuned search models in the Chat Completions API via `gpt-4o-search-preview` and `gpt-4o-mini-search-preview`. [Pricing](https://platform.openai.com/docs/pricing) starts respectively at $30 and $25 per thousand queries for GPT‑4o search and 4o-mini search respectively. Check out web search in the [Playground](https://platform.openai.com/playground/chat?preset=17UUXulQ970dEE3jgRfyzSFQ) and learn more in our [docs](https://platform.openai.com/docs/guides/tools-web-search).

#### File search

Developers can now easily retrieve relevant information from large volumes of documents using the improved file search tool. With support for multiple file types, query optimization, metadata filtering, and custom reranking, it can deliver fast, accurate search results. And again, with the Responses API, it takes only a few lines of code to integrate.

###### JavaScript

```
const productDocs = await openai.vectorStores.create({
    name: "Product Documentation",
    file_ids: [file1.id, file2.id, file3.id],
});

const response = await openai.responses.create({
    model: "gpt-4o-mini",
    tools: [{
        type: "file_search",
        vector_store_ids: [productDocs.id],
    }],
    input: "What is deep research by OpenAI?",
});

console.log(response.output_text);
```

The file search tool can be used for a variety of real-world use cases, including enabling a customer support agent to easily access FAQs, helping a legal assistant to quickly reference past cases for a qualified professional, and assisting a coding agent to query technical documentation. For example, [Navan](https://navan.com/) uses file search in its AI-powered travel agent to quickly provide their users with precise answers from knowledge-base articles (like their company’s travel policy). With built-in query optimization and reranking, they are able to set up a powerful RAG (retrieval-augmented generation) pipeline without extra tuning or configuration. With dedicated vector stores for each user group, Navan is able to tailor answers to individual account settings and user roles, saving time for customers and their staff while helping provide accurate, personalized support.

This tool is available in the Responses API to all developers. Usage is [priced](https://platform.openai.com/docs/pricing) at $2.50 per thousand queries and file storage at $0.10/GB/day, with the first GB free. The tool continues to be available in the Assistants API. Finally, we’ve also added a new search endpoint to Vector Store API objects to directly query your data for use in other applications and APIs. Learn more in our [docs](https://platform.openai.com/docs/guides/tools-file-search) and start testing in the [Playground](https://platform.openai.com/playground/chat).

#### Computer use

To build agents capable of completing tasks on a computer, developers can now use the computer use tool in the Responses API, powered by the same [Computer-Using Agent (CUA) model](/index/computer-using-agent/) that enables [Operator](/index/introducing-operator/). This research preview model set a new state-of-the-art record, achieving 38.1% success on [OSWorld](https://os-world.github.io/) for full computer use tasks, 58.1% on [WebArena](https://webarena.dev/), and 87% on [WebVoyager](https://arxiv.org/abs/2401.13919) for web-based interactions.

The built-in computer use tool captures mouse and keyboard actions generated by the model, making it possible for developers to automate computer use tasks by directly translating these actions into executable commands within their environments.

###### JavaScript

```
const response = await openai.responses.create({
    model: "computer-use-preview",
    tools: [{
        type: "computer_use_preview",
        display_width: 1024,
        display_height: 768,
        environment: "browser",
    }],
    truncation: "auto",
    input: "I'm looking for a new camera. Help me find the best one.",
});

console.log(response.output);
```

Developers can use the computer use tool to automate browser-based workflows like performing quality assurance on web apps or executing data-entry tasks across legacy systems. For example, [Unify](https://www.unifygtm.com/) is a system of action for growing revenue that uses agents to identify intent, research accounts, and engage with buyers. Using OpenAI’s computer use tool, Unify’s agents can access information that was previously unreachable via APIs—such as enabling a property management company to verify through online maps if a business has expanded its real estate footprint. This research acts as a custom signal to trigger personalized outreach—empowering go-to-market teams to engage buyers with precision and scale.

As another example, [Luminai](https://www.luminai.com/) integrated the computer use tool to automate complex operational workflows for large enterprises with legacy systems that lack API availability and standardized data. In a recent pilot with a major community service organization, Luminai automated the application processing and user enrollment process in just days—something traditional robotic process automation (RPA) struggled to achieve after months of effort.

Before launching CUA in Operator last year, we conducted extensive safety testing and red teaming, addressing three key areas of risk: misuse, model errors, and frontier risks. To address risks associated with expanding Operator’s capabilities to local operating systems through CUA in the API, we performed additional safety evaluations and red teaming. We also added mitigations for developers, including safety checks to guard against prompt injections, confirmation prompts for sensitive tasks, tools to help developers isolate their environments, and enhanced detection of potential policy violations. While these mitigations help reduce risk, the model is still susceptible to inadvertent mistakes, especially in non-browser environments. For example, CUA’s performance on OSWorld, a benchmark designed to measure the performance of AI agents on real-world tasks, is currently at 38.1%, indicating that the model is not yet highly reliable for automating tasks on operating systems. Human oversight is recommended in these scenarios. More details about our API-specific safety work can be found in our updated [system card](/index/operator-system-card/).

Table as flattened in the capture, re-laid out by the librarian (column order per the header row: Benchmark type · Benchmark · OpenAI CUA · Previous SOTA (computer use) · Previous SOTA (web browsing agents) · Human; cell values unchanged):

| Benchmark type | Benchmark | Computer use (universal interface): OpenAI CUA | Computer use: Previous SOTA | Web browsing agents: Previous SOTA | Human |
|---|---|---|---|---|---|
| Computer use | OSWorld | 38.1% | [22.0%](https://www.anthropic.com/news/3-5-models-and-computer-use) | - | [72.4%](https://arxiv.org/abs/2404.07972) |
| Browser use | WebArena | 58.1% | [36.2%](https://huggingface.co/spaces/ServiceNow/browsergym-leaderboard) | [57.1%](https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ) | [78.2%](https://arxiv.org/abs/2307.13854) |
| Browser use | WebVoyager | 87.0% | [56.0%](https://www.trykura.com/benchmarks) | [87.0%](https://www.trykura.com/benchmarks) | - |

Evaluation details are described [here](https://cdn.openai.com/cua/CUA_eval_extra_information.pdf)

Starting today, the computer use tool is available as a research preview in the Responses API for select developers in [usage tiers 3-5](https://platform.openai.com/docs/guides/rate-limits#usage-tiers). Usage is [priced](https://platform.openai.com/docs/pricing) at $3/1M input tokens and $12/1M output tokens. Learn more in our [docs](https://platform.openai.com/docs/guides/tools-computer-use) and check out the [sample application](https://github.com/openai/openai-cua-quickstart) illustrating how to build with this tool.

#### Agents SDK

In addition to building the core logic of agents and giving them access to tools so they are useful, developers also need to orchestrate agentic workflows. Our new open-source Agents SDK simplifies orchestrating multi-agent workflows and offers significant improvements over [Swarm](https://github.com/openai/swarm), an experimental SDK we released last year that was widely adopted by the developer community and successfully deployed by multiple customers.

Improvements include:

- **Agents**: Easily configurable LLMs with clear instructions and built-in tools.

- **Handoffs**: Intelligently transfer control between agents.

- **Guardrails**: Configurable safety checks for input and output validation.

- **Tracing & Observability**: Visualize agent execution traces to debug and optimize performance.

###### Python

```
from agents import Agent, Runner, WebSearchTool, function_tool, guardrail

@function_tool
def submit_refund_request(item_id: str, reason: str):
    # Your refund logic goes here
    return "success"

support_agent = Agent(
    name="Support & Returns",
    instructions="You are a support agent who can submit refunds [...]",
    tools=[submit_refund_request],
)

shopping_agent = Agent(
    name="Shopping Assistant",
    instructions="You are a shopping assistant who can search the web [...]",
    tools=[WebSearchTool()],
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="Route the user to the correct agent.",
    handoffs=[shopping_agent, support_agent],
)

output = Runner.run_sync(
    starting_agent=triage_agent,
    input="What shoes might work best with my outfit so far?",
)
```

The Agents SDK is suitable for various real-world applications, including customer support automation, multi-step research, content generation, code review, and sales prospecting. For instance, [Coinbase](https://www.coinbase.com/) used the Agents SDK to quickly prototype and deploy AgentKit, a toolkit enabling AI agents to interact seamlessly with crypto wallets and various on-chain activities. In just a few hours, Coinbase integrated custom actions from their Developer Platform SDK into a fully functional agent. AgentKit’s streamlined architecture simplified the process of adding new agent actions, letting developers focus more on meaningful integrations and less on navigating complex agent setups. 

In a couple of days, [Box](http://box.com) was able to quickly create agents that leverage web search and the Agents SDK to enable enterprises to search, query, and extract insights from unstructured data stored within Box and public internet sources. This approach allows customers to not only access the latest information, but also search their internal, proprietary data in a safe and secure way that obeys their internal permissions and security policies. For example, a financial services firm can build a custom agent that calls on the Box AI agent to integrate their internal market analysis stored in Box with real-time news and economic data from the web, providing their analysts with a comprehensive view for investment decisions.

The Agents SDK works with the Responses API and Chat Completions API. The SDK will also work with models from other providers, as long as they provide a Chat Completions style API endpoint. Developers can immediately integrate it into their Python codebases, with Node.js support coming soon. Learn more in our [docs](https://platform.openai.com/docs/guides/agents).

In designing the Agents SDK, our team was inspired by the excellent work of others in the community including [Pydantic](https://pydantic.dev/), [Griffe](https://mkdocstrings.github.io/griffe/) and [MkDocs](https://www.mkdocs.org/). We’re committed to continuing to build the Agents SDK as an open source framework so others in the community can expand on our approach.

#### What’s next: building the platform for agents

We believe agents will soon become integral to the workforce, significantly enhancing productivity across industries. As companies increasingly seek to leverage AI for complex tasks, we’re committed to providing the building blocks that enable developers and enterprises to effectively create autonomous systems that deliver real-world impact.

With today’s releases, we’re introducing the first building blocks to empower developers and enterprises to more easily build, deploy, and scale reliable, high-performing AI agents. As model capabilities become more and more agentic, we’ll continue investing in deeper integrations across our APIs and new tools to help deploy, evaluate, and optimize agents in production. Our goal is to give developers a seamless platform experience for building agents that can help with a variety of tasks across any industry. We’re excited to see what developers build next. To get started, explore our [docs](https://platform.openai.com/docs/overview) and stay tuned for more updates soon.
