# New tools for building agents | OpenAI

_Source: <https://openai.com/index/new-tools-for-building-agents/>_

[Skip to main content](#main)</>Log in[Try ChatGPT(opens in a new window)](https://chatgpt.com/)

- Research
- Products
- Business
- Developers
- Company
- [Foundation(opens in a new window)](https://openaifoundation.org)
[Try ChatGPT(opens in a new window)](https://chatgpt.com/)LoginOpenAI

March 11, 2025

[Product](/news/product-releases/)

# New tools for building agents

[Try in Playground(opens in a new window)](https://platform.openai.com/playground/chat?preset=ks7kayjX55ehTBR9oyUviuJe)![A sleek, minimal interface displaying a task list for an AI agent, including ‘triage_agent,’ ‘guardrail,’ and ‘update_salesforce_record,’ over a fluid blue abstract background.](https://images.ctfassets.net/kftzwdyauwt9/4QaBJvGYlSBY9iYMhWBN6I/c97e4a784aef38012d91e9a9cf2010c7/API_Agents_Hero_16.9.png?w=3840&q=90&fm=webp)

Today, we’re releasing the first set of building blocks that will help developers and enterprises build useful and reliable agents. We view agents as systems that independently accomplish tasks on behalf of users. Over the past year, we’ve introduced new model capabilities—such as advanced reasoning, multimodal interactions, and new safety techniques—that have laid the foundation for our models to handle the complex, multi-step tasks required to build agents. However, customers have shared that turning these capabilities into production-ready agents can be challenging, often requiring extensive prompt iteration and custom orchestration logic without sufficient visibility or built-in support.

To address these challenges, we’re launching a new set of APIs and tools specifically designed to simplify the development of agentic applications:

- 

The new [Responses API⁠(opens in a new window)](https://platform.openai.com/docs/quickstart?api-mode=responses), combining the simplicity of the Chat Completions API with the tool use capabilities of the Assistants API for building agents

- 

Built-in tools including [web search⁠(opens in a new window)](https://platform.openai.com/docs/guides/tools-web-search), [file search⁠(opens in a new window)](https://platform.openai.com/docs/guides/tools-file-search), and [computer use⁠(opens in a new window)](https://platform.openai.com/docs/guides/tools-computer-use)

- 

The new [Agents SDK⁠(opens in a new window)](https://platform.openai.com/docs/guides/agents) to orchestrate single-agent and multi-agent workflows

- 

Integrated [observability tools⁠(opens in a new window)](https://platform.openai.com/docs/guides/agents#orchestration) to trace and inspect agent workflow execution

These new tools streamline core agent logic, orchestration, and interactions, making it significantly easier for developers to get started with building agents. Over the coming weeks and months, we plan to release additional tools and capabilities to further simplify and accelerate building agentic applications on our platform.

## Introducing the Responses API

The Responses API is our new API primitive for leveraging OpenAI’s built-in tools to build agents. It combines the simplicity of Chat Completions with the tool-use capabilities of the Assistants API. As model capabilities continue to evolve, we believe the Responses API will provide a more flexible foundation for developers building agentic applications. With a single Responses API call, developers will be able to solve increasingly complex tasks using multiple tools and model turns.

To start, the Responses API will support new built-in tools like web search, file search, and computer use. These tools are designed to work together to connect models to the real world, making them more useful in completing tasks. It also brings with it several usability improvements including a unified item-based design, simpler polymorphism, intuitive streaming events, and SDK helpers like `response.output_text` to easily access the model’s text output.

The Responses API is designed for developers who want to easily combine OpenAI models and built-in tools into their apps, without the complexity of integrating multiple APIs or external vendors. The API also makes it easier to store data on OpenAI so developers can evaluate agent performance using features such as tracing and evaluations. As a reminder, we [do not train](/enterprise-privacy/) our models on business data by default, even when the data is stored on OpenAI. The API is available to all developers starting today and is not charged separately—tokens and tools are billed at standard rates specified on our [pricing page⁠(opens in a new window)](https://platform.openai.com/docs/pricing). Check out the Responses API [quickstart guide⁠(opens in a new window)](https://platform.openai.com/docs/quickstart?api-mode=responses) to learn more.

## What this means for existing APIs

- 

[Chat Completions API⁠(opens in a new window)](https://platform.openai.com/docs/guides/text-generation): Chat Completions remains our most widely adopted API, and we’re fully committed to supporting it with new models and capabilities. Developers who don’t require built-in tools can confidently continue using Chat Completions. We’ll keep releasing new models to Chat Completions whenever their capabilities don’t depend on built-in tools or multiple model calls. However, the Responses API is a [superset⁠(opens in a new window)](https://platform.openai.com/docs/guides/responses-vs-chat-completions) of Chat Completions with the same great performance, so for new integrations, we recommend starting with the Responses API.

- 

[Assistants API⁠(opens in a new window)](https://platform.openai.com/docs/assistants/overview): Based on developer feedback from the Assistants API beta, we’ve incorporated key improvements into the Responses API, making it more flexible, faster, and easier to use. We’re working to achieve full feature parity between the Assistants and the Responses API, including support for Assistant-like and Thread-like objects, and the Code Interpreter tool. Once this is complete, we plan to formally announce the deprecation of the Assistants API with a target sunset date in mid-2026. Upon deprecation, we will provide a clear migration guide from the Assistants API to the Responses API that allows developers to preserve all their data and migrate their applications. Until we formally announce the deprecation, we will continue delivering new models to the Assistants API. The Responses API represents the future direction for building agents on OpenAI.

## Introducing built-in tools in the Responses API

## Web search

Developers can now get fast, up-to-date answers with clear and relevant citations from the web. In the Responses API, web search is available as a tool when using gpt-4o and gpt-4o-mini, and can be paired with other tools or function calls.

#### JavaScript

`

```
1const response = await openai.responses.create({2    model: "gpt-4o",3    tools: [ { type: "web_search_preview" } ],4    input: "What was a positive news story that happened today?",5});6  
7console.log(response.output_text);
```

`

During early testing, we’ve seen developers build with web search for a variety of use cases including shopping assistants, research agents, and travel booking agents—any application that requires timely information from the web.

For example, [Hebbia⁠(opens in a new window)](https://www.hebbia.com/) leverages the web search tool to help asset managers, private equity and credit firms, and law practices quickly extract actionable insights from extensive public and private datasets. By integrating real-time search capabilities into their research workflows, Hebbia delivers richer, context-specific market intelligence and continuously improves the precision and relevance of their analyses, outperforming current benchmarks.

Web search in the API is powered by the same model used for ChatGPT search. On SimpleQA, a benchmark that evaluates the accuracy of LLMs in answering short, factual questions, GPT‑4o search preview and GPT‑4o mini search preview score 90% and 88% respectively.

##### SimpleQA Accuracy (higher is better)

63%38%47%15%90%88%Accuracy

Responses generated with web search in the API include links to sources, such as news articles and blog posts, giving users a way to learn more. With these clear, inline citations, users can engage with information in a new way, while content owners gain new opportunities to reach a broader audience.

Any website or publisher can [choose to appear⁠(opens in a new window)](https://platform.openai.com/docs/bots) in web search in the API.

The web search tool is available to all developers in preview in the Responses API. We are also giving developers direct access to our fine-tuned search models in the Chat Completions API via `gpt-4o-search-preview` and `gpt-4o-mini-search-preview`. [Pricing⁠(opens in a new window)](https://platform.openai.com/docs/pricing) starts respectively at $30 and $25 per thousand queries for GPT‑4o search and 4o-mini search respectively. Check out web search in the [Playground⁠(opens in a new window)](https://platform.openai.com/playground/chat?preset=17UUXulQ970dEE3jgRfyzSFQ) and learn more in our [docs⁠(opens in a new window)](https://platform.openai.com/docs/guides/tools-web-search).

## File search

Developers can now easily retrieve relevant information from large volumes of documents using the improved file search tool. With support for multiple file types, query optimization, metadata filtering, and custom reranking, it can deliver fast, accurate search results. And again, with the Responses API, it takes only a few lines of code to integrate.

#### JavaScript

`

```
1const productDocs = await openai.vectorStores.create({2    name: "Product Documentation",3    file_ids: [file1.id, file2.id, file3.id],4});5  
6const response = await openai.responses.create({7    model: "gpt-4o-mini",8    tools: [{9        type: "file_search",10        vector_store_ids: [productDocs.id],11    }],12    input: "What is deep research by OpenAI?",13});14  
15console.log(response.output_text);
```

`

The file search tool can be used for a variety of real-world use cases, including enabling a customer support agent to easily access FAQs, helping a legal assistant to quickly reference past cases for a qualified professional, and assisting a coding agent to query technical documentation. For example, [Navan⁠(opens in a new window)](https://navan.com/) uses file search in its AI-powered travel agent to quickly provide their users with precise answers from knowledge-base articles (like their company’s travel policy). With built-in query optimization and reranking, they are able to set up a powerful RAG (retrieval-augmented generation) pipeline without extra tuning or configuration. With dedicated vector stores for each user group, Navan is able to tailor answers to individual account settings and user roles, saving time for customers and their staff while helping provide accurate, personalized support.

This tool is available in the Responses API to all developers. Usage is [priced⁠(opens in a new window)](https://platform.openai.com/docs/pricing) at $2.50 per thousand queries and file storage at $0.10/GB/day, with the first GB free. The tool continues to be available in the Assistants API. Finally, we’ve also added a new search endpoint to Vector Store API objects to directly query your data for use in other applications and APIs. Learn more in our [docs⁠(opens in a new window)](https://platform.openai.com/docs/guides/tools-file-search) and start testing in the [Playground⁠(opens in a new window)](https://platform.openai.com/playground/chat).

## Computer use

To build agents capable of completing tasks on a computer, developers can now use the computer use tool in the Responses API, powered by the same [Computer-Using Agent (CUA) model](/index/computer-using-agent/) that enables [Operator](/index/introducing-operator/). This research preview model set a new state-of-the-art record, achieving 38.1% success on [OSWorld⁠(opens in a new window)](https://os-world.github.io/) for full computer use tasks, 58.1% on [WebArena⁠(opens in a new window)](https://webarena.dev/), and 87% on [WebVoyager⁠(opens in a new window)](https://arxiv.org/abs/2401.13919) for web-based interactions.

The built-in computer use tool captures mouse and keyboard actions generated by the model, making it possible for developers to automate computer use tasks by directly translating these actions into executable commands within their environments.

#### JavaScript

`

```
1const response = await openai.responses.create({2    model: "computer-use-preview",3    tools: [{4        type: "computer_use_preview",5        display_width: 1024,6        display_height: 768,7        environment: "browser",8    }],9    truncation: "auto",10    input: "I'm looking for a new camera. Help me find the best one.",11});12  
13console.log(response.output);
```

`

Developers can use the computer use tool to automate browser-based workflows like performing quality assurance on web apps or executing data-entry tasks across legacy systems. For example, [Unify⁠(opens in a new window)](https://www.unifygtm.com/) is a system of action for growing revenue that uses agents to identify intent, research accounts, and engage with buyers. Using OpenAI’s computer use tool, Unify’s agents can access information that was previously unreachable via APIs—such as enabling a property management company to verify through online maps if a business has expanded its real estate footprint. This research acts as a custom signal to trigger personalized outreach—empowering go-to-market teams to engage buyers with precision and scale.

As another example, [Luminai⁠(opens in a new window)](https://www.luminai.com/) integrated the computer use tool to automate complex operational workflows for large enterprises with legacy systems that lack API availability and standardized data. In a recent pilot with a major community service organization, Luminai automated the application processing and user enrollment process in just days—something traditional robotic process automation (RPA) struggled to achieve after months of effort.

Before launching CUA in Operator last year, we conducted extensive safety testing and red teaming, addressing three key areas of risk: misuse, model errors, and frontier risks. To address risks associated with expanding Operator’s capabilities to local operating systems through CUA in the API, we performed additional safety evaluations and red teaming. We also added mitigations for developers, including safety checks to guard against prompt injections, confirmation prompts for sensitive tasks, tools to help developers isolate their environments, and enhanced detection of potential policy violations. While these mitigations help reduce risk, the model is still susceptible to inadvertent mistakes, especially in non-browser environments. For example, CUA’s performance on OSWorld, a benchmark designed to measure the performance of AI agents on real-world tasks, is currently at 38.1%, indicating that the model is not yet highly reliable for automating tasks on operating systems. Human oversight is recommended in these scenarios. More details about our API-specific safety work can be found in our updated [system card](/index/operator-system-card/).

Benchmark typeBenchmarkComputer use (universal interface)Web browsing agentsHumanOpenAI CUAPrevious SOTAPrevious SOTAComputer useOSWorld38.1%[22.0%](https://www.anthropic.com/news/3-5-models-and-computer-use)-[72.4%](https://arxiv.org/abs/2404.07972)Browser useWebArena58.1%[36.2%](https://huggingface.co/spaces/ServiceNow/browsergym-leaderboard)[57.1%](https://docs.google.com/spreadsheets/d/1M801lEpBbKSNwP-vDBkC_pF7LdyGU1f_ufZb_NWNBZQ)[78.2%](https://arxiv.org/abs/2307.13854)WebVoyager87.0%[56.0%](https://www.trykura.com/benchmarks)[87.0%](https://www.trykura.com/benchmarks)-Evaluation details are described [here](https://cdn.openai.com/cua/CUA_eval_extra_information.pdf)

Starting today, the computer use tool is available as a research preview in the Responses API for select developers in [usage tiers 3-5⁠(opens in a new window)](https://platform.openai.com/docs/guides/rate-limits#usage-tiers). Usage is [priced⁠(opens in a new window)](https://platform.openai.com/docs/pricing) at $3/1M input tokens and $12/1M output tokens. Learn more in our [docs⁠(opens in a new window)](https://platform.openai.com/docs/guides/tools-computer-use) and check out the [sample application⁠(opens in a new window)](https://github.com/openai/openai-cua-quickstart) illustrating how to build with this tool.

## Agents SDK

In addition to building the core logic of agents and giving them access to tools so they are useful, developers also need to orchestrate agentic workflows. Our new open-source Agents SDK simplifies orchestrating multi-agent workflows and offers significant improvements over [Swarm⁠(opens in a new window)](https://github.com/openai/swarm), an experimental SDK we released last year that was widely adopted by the developer community and successfully deployed by multiple customers.

Improvements include:

- 

**Agents**: Easily configurable LLMs with clear instructions and built-in tools.

- 

**Handoffs**: Intelligently transfer control between agents.

- 

**Guardrails**: Configurable safety checks for input and output validation.

- 

**Tracing & Observability**: Visualize agent execution traces to debug and optimize performance.

#### Python

`

```
1from agents import Agent, Runner, WebSearchTool, function_tool, guardrail2  
3@function_tool4def submit_refund_request(item_id: str, reason: str):5    # Your refund logic goes here6    return "success"7  
8support_agent = Agent(9    name="Support & Returns",10    instructions="You are a support agent who can submit refunds [...]",11    tools=[submit_refund_request],12)13  
14shopping_agent = Agent(15    name="Shopping Assistant",16    instructions="You are a shopping assistant who can search the web [...]",17    tools=[WebSearchTool()],18)19  
20triage_agent = Agent(21    name="Triage Agent",22    instructions="Route the user to the correct agent.",23    handoffs=[shopping_agent, support_agent],24)25  
26output = Runner.run_sync(27    starting_agent=triage_agent,28    input="What shoes might work best with my outfit so far?",29)
```

`

The Agents SDK is suitable for various real-world applications, including customer support automation, multi-step research, content generation, code review, and sales prospecting. For instance, [Coinbase⁠(opens in a new window)](https://www.coinbase.com/) used the Agents SDK to quickly prototype and deploy AgentKit, a toolkit enabling AI agents to interact seamlessly with crypto wallets and various on-chain activities. In just a few hours, Coinbase integrated custom actions from their Developer Platform SDK into a fully functional agent. AgentKit’s streamlined architecture simplified the process of adding new agent actions, letting developers focus more on meaningful integrations and less on navigating complex agent setups. 

In a couple of days, [Box⁠(opens in a new window)](http://box.com) was able to quickly create agents that leverage web search and the Agents SDK to enable enterprises to search, query, and extract insights from unstructured data stored within Box and public internet sources. This approach allows customers to not only access the latest information, but also search their internal, proprietary data in a safe and secure way that obeys their internal permissions and security policies. For example, a financial services firm can build a custom agent that calls on the Box AI agent to integrate their internal market analysis stored in Box with real-time news and economic data from the web, providing their analysts with a comprehensive view for investment decisions.

The Agents SDK works with the Responses API and Chat Completions API. The SDK will also work with models from other providers, as long as they provide a Chat Completions style API endpoint. Developers can immediately integrate it into their Python codebases, with Node.js support coming soon. Learn more in our [docs⁠(opens in a new window)](https://platform.openai.com/docs/guides/agents).

In designing the Agents SDK, our team was inspired by the excellent work of others in the community including [Pydantic⁠(opens in a new window)](https://pydantic.dev/), [Griffe⁠(opens in a new window)](https://mkdocstrings.github.io/griffe/) and [MkDocs⁠(opens in a new window)](https://www.mkdocs.org/). We’re committed to continuing to build the Agents SDK as an open source framework so others in the community can expand on our approach.

## What’s next: building the platform for agents

We believe agents will soon become integral to the workforce, significantly enhancing productivity across industries. As companies increasingly seek to leverage AI for complex tasks, we’re committed to providing the building blocks that enable developers and enterprises to effectively create autonomous systems that deliver real-world impact.

With today’s releases, we’re introducing the first building blocks to empower developers and enterprises to more easily build, deploy, and scale reliable, high-performing AI agents. As model capabilities become more and more agentic, we’ll continue investing in deeper integrations across our APIs and new tools to help deploy, evaluate, and optimize agents in production. Our goal is to give developers a seamless platform experience for building agents that can help with a variety of tasks across any industry. We’re excited to see what developers build next. To get started, explore our [docs⁠(opens in a new window)](https://platform.openai.com/docs/overview) and stay tuned for more updates soon.

- [API Platform](/news/?tags=api-platform)
- [2025](/news/?tags=2025)

## Authors

OpenAI
