# Run a Company of AI Agents with Paperclipcaret-right

_Source: <https://www.theaienterprise.io/p/run-company-ai-agents-paperclip>_

This website uses cookies

Read our [Privacy policy](https://www.beehiiv.com/privacy) and [Terms of use](https://www.beehiiv.com/tou) for more information.

AcceptCustomizeDeclineYour browser does not support the audio element.

# Run a Company of AI Agents

*Paperclip gives you the org chart, budget controls, and governance to manage a workforce of AI agents — the way a CEO manages a team*

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/a50cd392-2c52-4626-bc91-87bc2d0ca129/run-company-ai-agents-paperclip.png?t=1775575049)

There's an old saying about the cobbler whose children have no shoes. I'm that cobbler.

I publish a newsletter about AI tools. I write tutorials on agent automation. And until recently, I was managing my own AI agents the way most people manage their inbox — reactively, inconsistently, and with no real system behind it. I had an OpenClaw instance running here, a Claude Code session open there, a couple of scripts firing on cron jobs I'd half-forgotten about. Capable agents. Zero coordination. No shared mission. No way to see what anything was costing me at a glance.

The irony wasn't lost on me.

What I needed wasn't better agents. I already had those. What I needed was a management layer — something that gave my agents an org chart, a shared goal, a budget, and a reporting structure. Something that let me go from managing agents willy-nilly to actually running them like a company.

That's exactly what [Paperclip](https://paperclip.ing/) does. It launched in March 2026 and crossed 44,000 GitHub stars in under three weeks — one of the fastest-rising open-source AI repositories of the year — because it solved a problem many people had but couldn't name. It's an open source orchestration platform that sits above your existing agents — OpenClaw, Claude Code, Codex, Gemini, Cursor, whatever you're already running — and turns them into an organized workforce. My current project: get my OpenClaw instance properly integrated as the foundation, then scale out through a single dashboard. This lesson covers what I've learned while building that setup and how you can do the same.

###### **LISTEN TO THE AI ENTERPRISE ON THE ROGUE AGENTS PODCAST**

This is my latest project, while we do have audio summaries for each newsletter. They are not ideal for listening; they are simple text-to-speech. We created a way to provide a weekly summary of the newsletters in this podcast. And actually, it’s a work in progress. Right now, you get a pretty good podcast recap of the previous week’s newsletters. But over time, they will be better. That’s the plan. 

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/48f7143a-67de-4c35-a273-fcb037593ad6/rogue_agents_podcast.webp?t=1774799337)<https://rogueagents.io>

What happens when two AI agents break down the week's biggest AI news? You get Rogue Agents. Vera and Neuro deliver the stories that matter in enterprise AI — the deals, the tools, the breakthroughs, and the stuff everyone's getting wrong — in 15-20 minutes every week.

****[Listen to the Rogue Agents →](https://theaie.net/podcasts/rogue-agents)

###### AI LESSON

## Run a Company of AI Agents

*Paperclip gives you the org chart, budget controls, and governance to manage a workforce of AI agents — the way a CEO manages a team*

Running one AI agent is easy. Running ten is chaos — unless you have a control plane. Paperclip is that control plane: open source, self-hosted, and built around the mental model of a company rather than a pile of scripts. This lesson walks through the design patterns for scaling from a single agent to a fully orchestrated AI workforce, introduces Paperclip's core mechanics, and shows you exactly which agents you can plug in and how.

### The Three Levels of Agent Management

Before touching Paperclip, it helps to understand where you are and where you're going. Agent management follows a natural progression — and most business professionals are stuck at Level 1.

**Level 1 — Single-task agents (where most people are now)**

One agent. One job. You prompt it, review the output, and move on. This works fine for isolated tasks: summarizing a report, drafting an email, generating code. The problem is that the agent has no memory of your business, no connection to your goals, and no accountability. Every session starts from zero.

**Level 2 — Parallel specialized agents**

Multiple agents, each owning a discrete function, running on a schedule. A Content Writer fires every four hours. An SEO Analyst runs every eight. A Social Manager every twelve. They don't directly collaborate, but they share a common goal hierarchy. This is where the value of specialization shows up — but coordination is still mostly manual without the right infrastructure.

**Level 3 — Hierarchical orchestration (the full company model)**

This is Paperclip's design target. A CEO agent interprets a company mission ("Build the #1 AI note-taking app to $1M MRR"), decomposes it into projects, assigns work down an org chart, and escalates blockers up to you — the human board. Every task at every level traces back to the mission. Agents know not just *what* to do, but *why* they're doing it.

The mental model shift here is significant. You stop thinking "I'm prompting an AI" and start thinking "I'm managing a team." That reframe changes how you design workflows, assign responsibilities, and evaluate output.

### How to Access Paperclip

**Cost:** Free. MIT-licensed. Open source. You pay only for the AI provider tokens your agents consume.

**Requirements:** Node.js 20 or higher and pnpm 9.15 or higher. Paperclip is self-hosted — no Paperclip account required.

**Setup:** The [official Paperclip quickstart](https://docs.paperclip.ing/start/quickstart) walks you through installation, database configuration, and your first company in under fifteen minutes. Once running, the dashboard is your board of directors view — org chart, task board, agent status, budget tracker, and audit log in one place.

**Skill level:** No coding required. If you're comfortable opening a terminal, you can follow this.

**Note:** Paperclip launched in March 2026 and is under active development. Configuration details may evolve quickly — always verify steps against the [official docs](https://docs.paperclip.ing) before following any third-party guide, including this one. *(Verified: April 2026)*

### The Core Design: How Paperclip Structures a Company

Every Paperclip deployment organizes around five building blocks:

**Company** — The top-level unit. You define a mission, set a monthly budget, and build an org below it. One Paperclip instance can run multiple companies with complete data isolation between them.

**Agents (Employees)** — Every employee is an AI agent with a title, a reporting line, a description of its capabilities, a monthly spend budget, and a status (active, idle, running, error, paused, or terminated). Agents sit in a strict tree hierarchy — every agent reports to exactly one manager, except the CEO.

**Issues (Tasks)** — The unit of work. Each issue has a title, description, status, priority, and one assignee. Issues nest under parent issues, creating a traceable chain back to the company goal. The status lifecycle runs: backlog → todo → in_progress → in_review → done. Only one agent can own a task at a time — enforced automatically to prevent duplicate work.

**Heartbeats** — Agents don't run continuously. They wake on a trigger: a scheduled timer, a new task assignment, an @-mention in a ticket, or a manual invoke from the dashboard UI. Each heartbeat, the agent checks its assignments, picks up work, executes, and updates status. This is what keeps costs predictable and prevents runaway loops.

**Governance** — You're the board. Certain actions require your approval before they execute: hiring new agents, the CEO's initial strategic plan, and major overrides. You can pause, resume, reassign, or terminate any agent at any time. Every action is logged in an immutable audit trail.

### The Agents You Can Manage

Paperclip connects to agent runtimes through adapters — plug-in connectors that bridge the orchestration layer to the actual AI doing the work. Here's what ships out of the box, with guidance on when to use each:

**For coding and technical tasks:**

**Claude Local** (claude_local) — Runs [Claude Code](https://docs.anthropic.com/en/docs/claude-code) locally. Best for agents handling writing, research, code generation, or multi-step reasoning. A natural starting point if you're already in the Anthropic ecosystem.

**Codex Local** (codex_local) — Runs OpenAI Codex CLI locally. The parallel option for engineering agents on OpenAI models.

**Gemini Local** (gemini_local) — Runs Gemini CLI locally. Relevant for teams embedded in the Google Workspace ecosystem.

**Cursor** (cursor) — Connects the Cursor IDE as an agent runtime. Good for development agents that need active file access during execution.

**For operations and automation:**

**Process Adapter** (process) — Executes arbitrary shell commands. Use this for scripts, scheduled jobs, data pipelines, or any automation that doesn't require an LLM. This is your bridge from AI agents to traditional workflow tools.

**HTTP Adapter** (http) — Sends webhook payloads to any external service or custom agent. Anything that can receive an HTTP request can become an employee in your Paperclip org. If you've built your own agent or need to connect a third-party service, this is your bridge.

**OpenClaw Gateway** (openclaw_gateway) — Sends wake payloads to an OpenClaw instance via its gateway URL (the public or local address where your OpenClaw instance accepts incoming requests). This is the adapter I'm using as my foundation. If you're already running OpenClaw, Paperclip doesn't replace it — it wraps it in governance, giving your existing agent a boss, a budget, and a place in an org chart. See the [OpenClaw documentation](https://github.com/openclawai/openclaw) for how to expose your instance as a reachable endpoint before connecting it here.

❝

**Security note:** As of April 2026, security researchers have [disclosed a high-severity vulnerability in OpenClaw](https://arstechnica.com/security/2026/04/heres-why-its-prudent-for-openclaw-users-to-assume-compromise/) (CVE-2026-33579) that allowed privilege escalation via the pairing mechanism. Patches have been released. Before connecting any OpenClaw instance to Paperclip, ensure you are running the latest patched version and that authentication is properly configured.

**A practical content marketing org in Paperclip:**

CEO (claude_local) — Mission: Grow newsletter to 50K subscribers

├── CMO (claude_local) — Strategy and campaign planning

│ ├── Content Writer (claude_local) — Drafts articles, heartbeat every 4h

│ ├── SEO Analyst (claude_local) — Keyword research, heartbeat every 8h

│ └── Social Manager (process) — Schedules posts via script, heartbeat every 12h

└── CTO (openclaw_gateway) — Site performance and tooling

└── Dev Agent (codex_local) — Bug fixes and feature work

Each agent knows its role, its manager, and the company mission it's working toward.

### CrewAI: The Enterprise Framework Option

If your team has Python developers and needs a code-first multi-agent system — with enterprise compliance, custom tool integrations, and production-grade monitoring — [CrewAI](https://crewai.com/) is the reference framework worth evaluating alongside Paperclip.

Where Paperclip is a **control plane** (it manages agents regardless of how they were built), CrewAI is a **framework** (it defines how agents are constructed, what roles they play, and how they hand off work). The two are complementary: a CrewAI-built agent can connect into Paperclip via the HTTP adapter.

CrewAI's [Agent Management Platform](https://crewai.com/amp) offers three deployment paths: an open source framework for developers, AMP Cloud (managed SaaS), and AMP Factory (self-hosted on AWS, Azure, or GCP). The Studio interface provides drag-and-drop workflow building with no coding required. Native integrations include Gmail, Microsoft Teams, Notion, HubSpot, Salesforce, Slack, and Zendesk.

According to [Insight Partners](https://www.insightpartners.com/ideas/crewai-scaleup-ai-story/), CrewAI currently powers 1.4 billion agentic automations at organizations including PwC, IBM, Capgemini, and NVIDIA. It's best suited for teams that need defined role delegation at scale, have Python-comfortable developers, or require enterprise compliance certifications like SOC 2.

**The practical comparison:** Paperclip gets you running in under fifteen minutes with no coding. CrewAI offers deeper programmatic control and a mature enterprise track record. Start with Paperclip if you're a solo operator or small team. Evaluate CrewAI AMP if your IT or engineering team is building production multi-agent systems with compliance requirements.

### What Paperclip Can't Do (Yet)

**It's brand new.** Paperclip launched in March 2026. That means limited independent validation, an evolving feature set, and documentation that's still catching up to the code. It's worth running in a test environment before connecting it to production agents.

**The Cliphub marketplace isn't live.** The feature that lets you import a pre-built org — a full "Content Marketing Agency" with agents, goals, and skills — in seconds is listed as coming soon. For now, you build company structures manually.

**It's self-hosted only.** There's no managed cloud option. You own the infrastructure. The embedded database works well locally; scaling to dozens of agents across multiple companies may require more infrastructure planning.

**Budget enforcement is monthly, not real-time.** Paperclip auto-pauses agents at 100% of their monthly spend cap, with a soft warning at 80%. But within a single heartbeat, an agent can still make expensive calls before the cap applies. Set conservative budgets while you're learning your agents' token patterns.

**Governance controls hiring, not behavior.** Board approval is required to add agents to the org chart. What an individual agent does during a heartbeat is determined by its own system prompt and adapter runtime — you still need to design responsible agent instructions separately.

### Getting Started Today

1. 

**Right now:** Follow the [official Paperclip quickstart](https://docs.paperclip.ing/start/quickstart) and get a company running locally. Under fifteen minutes.

2. 

**Today:** Connect your first agent. If you're running OpenClaw, ensure you're on the latest patched version first, then use the openclaw_gateway adapter and give it a role in the org. If not, spin up a claude_local agent for a task you repeat every day and set it on a heartbeat schedule.

3. 

**This week:** Watch your first task flow from creation to completion.

4. 

**Next week:** Add a second agent in a different function — research, content, or operations — and see how goal alignment flows from the company mission down through the task hierarchy.

I'm building this same setup myself, moving from a collection of disconnected agents to a single coordinated dashboard. The infrastructure is free. The agents are ones you're probably already running. The missing piece — until now — was the management layer.

###### AI EXTRA CREDIT

Keep learning with these upcoming free virtual events from the ****[All Things AI](https://allthingsai.org/) <https://allthingsai.org/>community.

**April 22nd | ****[Live at The American Underground](https://americanunderground.com/)**** | ****[Building Your Startup in the Age of AI](https://www.meetup.com/all-things-ai-live/events/314147027/?eventOrigin=group_events_list)** <https://www.meetup.com/all-things-ai-live/events/314147027/?eventOrigin=group_events_list>— In this session, ****[Mark Hinkle](https://www.linkedin.com/in/markrhinkle) is joining forces with ****[The American Underground](https://americanunderground.com/) as part of ****[Raleigh Durham Startup Week](https://www.raleighdurhamstartupweek.com/) to share what he's learned the hard way about where AI actually delivers for early-stage companies. From capital strategy to agent-powered execution, this session is for founders who want to move faster and build smarter.

**May 6th | ****[Linkedin Live | Why Jensen Huang's Betting on Confidential Computing in the AI Factory](https://www.linkedin.com/events/7443033524330369025/)** — In this session, ****[Mark Hinkle](https://www.linkedin.com/in/markrhinkle) <https://www.linkedin.com/in/markrhinkle>sits down with ****[Aaron Fulkerson](https://www.linkedin.com/in/aaronfulkerson), CEO of Opaque Systems — the leading Confidential AI platform born from UC Berkeley's RISELab and backed by Intel, Accenture, and many others — for a conversation that will fundamentally change how you think about enterprise AI.

I appreciate your support.

![](https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,quality=80,format=auto,onerror=redirect/uploads/asset/file/967c2726-795d-41b5-a43b-6c358ec4065c/red_network_headshot_200x200.png?t=1714221032)

Your AI Sherpa, 

**Mark R. Hinkle**  
Publisher, The [AIE Network](https://theaie.net)  
Connect with me on [LinkedIn](https://www.linkedin.com/in/markrhinkle/)  
Follow Me on [Twitter](https://twitter.com/mrhinkle)

### Keep Reading

[View more](https://www.theaienterprise.io:3002/archive)![The AIE NEtwork](https://media.beehiiv.com/cdn-cgi/image/format=auto,fit=scale-down,onerror=redirect/uploads/asset/file/4661e3ec-112c-4747-a866-1f8e2d5d5e39/the_aie_network_nl_ww.png?t=1778523198)<https://theaie.net><https://twitter.com/theaienterprise><https://www.linkedin.com/company/the-artificially-intelligent-enterprise/><https://www.facebook.com/the.artificially.intelligent.enterprise>
