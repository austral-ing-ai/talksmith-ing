---
source_file: aienterprise-run-company-agents/
source_type: web-capture
ingested_at: 2026-10-04
---

# Run a Company of AI Agents (with Paperclip) — The Artificially Intelligent Enterprise newsletter

## Provenance
- Original location: `research/web/aienterprise-run-company-agents/` (`page.md` used as text input; no fallback needed. `original.html` consulted only for the publication date in its JSON-LD.)
- Format: html (web capture via `talksmith:ingest`; beehiiv newsletter page)
- URL: https://www.theaienterprise.io/p/run-company-ai-agents-paperclip
- Fetched: 2026-08-24T15:57:12Z (HTTP 200, 918,251 bytes). Captured for a prior talk and copied into this Talk.
- Author / source (if known): Mark R. Hinkle, publisher, The AIE Network / "The Artificially Intelligent Enterprise" newsletter ("AI LESSON" section)
- Date of original (if known): 2026-04-07 (`datePublished` in the page's JSON-LD; article itself says "Verified: April 2026")
- Captured title "Run a Company of AI Agents with Paperclipcaret-right" includes a stray icon label ("caret-right") from the page markup.
- Nature: newsletter tutorial / product walkthrough of the open-source tool Paperclip; partly promotional (podcast and event plugs).

## Key claims
- Managing many agents ad hoc ("an OpenClaw instance running here, a Claude Code session open there, a couple of scripts firing on cron jobs") gives "Capable agents. Zero coordination." What's missing is a **management layer**: org chart, shared goal, budget, reporting structure.
- **Paperclip** is presented as that layer: "an open source orchestration platform that sits above your existing agents — OpenClaw, Claude Code, Codex, Gemini, Cursor, whatever you're already running — and turns them into an organized workforce." Described as a **control plane**: open source (MIT), self-hosted, "built around the mental model of a company rather than a pile of scripts."
- Claimed adoption: launched March 2026; "crossed 44,000 GitHub stars in under three weeks".
- **Three levels of agent management**:
  1. **Single-task agents** (where most people are) — one agent, one job; no business memory, no goal connection, no accountability; every session starts from zero.
  2. **Parallel specialized agents** — several agents each owning a function on a schedule (Content Writer every 4h, SEO Analyst every 8h, Social Manager every 12h); share a goal hierarchy but don't directly collaborate; coordination still mostly manual.
  3. **Hierarchical orchestration (full company model)** — a CEO agent interprets a mission ("Build the #1 AI note-taking app to $1M MRR"), decomposes into projects, assigns work down an org chart, escalates blockers to the human "board"; every task traces back to the mission.
- Mental-model shift: from "I'm prompting an AI" to "I'm managing a team."
- **Five building blocks**: Company (mission, monthly budget, data isolation between companies); Agents/Employees (title, reporting line, capabilities, monthly budget, status; strict tree — each agent reports to exactly one manager except the CEO); Issues/Tasks (single assignee; nest under parent issues; lifecycle backlog → todo → in_progress → in_review → done; one owner at a time enforced); Heartbeats (agents wake on timer, assignment, @-mention or manual invoke — keeps cost predictable, prevents runaway loops); Governance (human board approves hires, CEO's initial strategy, major overrides; pause/resume/reassign/terminate; immutable audit trail).
- **Adapters** connect runtimes: `claude_local` (Claude Code), `codex_local` (OpenAI Codex CLI), `gemini_local` (Gemini CLI), `cursor`, `process` (shell commands, no LLM), `http` (webhooks to any service/custom agent), `openclaw_gateway`.
- **CrewAI** contrasted as a **framework** (defines how agents are built, roles, handoffs) vs. Paperclip as a **control plane** (manages agents however built); complementary via the HTTP adapter.
- Limitations stated by the author: brand new; Cliphub marketplace not live; self-hosted only; budget enforcement monthly not real-time (auto-pause at 100%, warning at 80%, but a single heartbeat can still overspend); "Governance controls hiring, not behavior."

## Definitions and terminology
- **Control plane** — management layer above agents (org chart, budgets, governance), independent of how agents are built.
- **Framework** (vs. control plane) — library that defines agent construction, roles and handoffs (e.g., CrewAI).
- **Heartbeat** — a trigger-driven wake cycle in which an agent checks assignments, executes, updates status.
- **Adapter** — plug-in connector between Paperclip and an agent runtime.
- **Board** — the human(s) holding approval authority over the agent company.
- **Hierarchical orchestration** — Level 3: CEO agent decomposes mission and delegates down a strict reporting tree.

## Evidence and examples
- Example org chart (verbatim structure from the source):
  ```
  CEO (claude_local) — Mission: Grow newsletter to 50K subscribers
  ├── CMO (claude_local) — Strategy and campaign planning
  │   ├── Content Writer (claude_local) — Drafts articles, heartbeat every 4h
  │   ├── SEO Analyst (claude_local) — Keyword research, heartbeat every 8h
  │   └── Social Manager (process) — Schedules posts via script, heartbeat every 12h
  └── CTO (openclaw_gateway) — Site performance and tooling
      └── Dev Agent (codex_local) — Bug fixes and feature work
  ```
  ("Each agent knows its role, its manager, and the company mission it's working toward.")
- Requirements: Node.js ≥ 20, pnpm ≥ 9.15; quickstart "under fifteen minutes": https://docs.paperclip.ing/start/quickstart
- Security note: OpenClaw high-severity vulnerability CVE-2026-33579 (privilege escalation via pairing), per an Ars Technica article (April 2026); patches released.
- CrewAI: Agent Management Platform with open-source framework, AMP Cloud (SaaS), AMP Factory (self-hosted on AWS/Azure/GCP); Studio drag-and-drop; integrations Gmail, Teams, Notion, HubSpot, Salesforce, Slack, Zendesk. Per Insight Partners, "1.4 billion agentic automations" at PwC, IBM, Capgemini, NVIDIA.
- Getting-started sequence: run quickstart → connect first agent (OpenClaw via `openclaw_gateway`, or a `claude_local` agent on a heartbeat) → watch a task flow end-to-end → add a second agent in another function.

## Inconsistencies / open questions
- [open question] "Launched in March 2026 and crossed 44,000 GitHub stars in under three weeks" — not checked; settle against the Paperclip GitHub repository history.
- [open question] CVE-2026-33579 in OpenClaw and its description — not checked; settle against the NVD entry / linked Ars Technica article.
- [open question] "CrewAI currently powers 1.4 billion agentic automations" — second-hand via Insight Partners, not checked; settle against the linked Insight Partners page.
- [open question] Paperclip's adapter list, task lifecycle and budget behaviour reflect the product "as of April 2026" (the author warns details "may evolve quickly"); the Talk is October 2026 — settle against current docs at https://docs.paperclip.ing before presenting specifics.
- [verified] Mild internal tension: "Skill level: No coding required" sits next to self-hosted setup requiring Node.js 20+, pnpm 9.15+ and database configuration ("If you're comfortable opening a terminal, you can follow this") — checked in the "How to Access Paperclip" section.
- Note: the "company" / org-chart framing is a metaphor for hierarchical (supervisor-of-supervisors) orchestration — relevant to the Talk as a vivid example of the hierarchical multi-agent pattern, not as an academic definition.

## Images / diagrams

### `aienterprise-run-company-agents.web/images/run-company-ai-agents-paperclip.png`
- Provenance: article hero image directly under the subtitle (3.2 MB PNG; no alt). Original via beehiiv CDN (`…/run-company-ai-agents-paperclip.png`).
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `aienterprise-run-company-agents.web/images/rogue_agents_podcast.png`
- Provenance: promo image for the "Rogue Agents" podcast (newsletter plug, not lesson content). Served as `rogue_agents_podcast.webp` but the bytes are PNG — saved with `.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `aienterprise-run-company-agents.web/images/red_network_headshot_200x200.png`
- Provenance: author headshot in the sign-off ("Your AI Sherpa, Mark R. Hinkle").
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

### `aienterprise-run-company-agents.web/images/the_aie_network_nl_ww.png`
- Provenance: footer logo, alt "The AIE NEtwork".
- Depiction: <!-- pending: process_images -->
- Why it matters:
- Transcribed text:

## Raw / preserved excerpts

**Opening (author's framing)**
> There's an old saying about the cobbler whose children have no shoes. I'm that cobbler.
>
> I publish a newsletter about AI tools. I write tutorials on agent automation. And until recently, I was managing my own AI agents the way most people manage their inbox — reactively, inconsistently, and with no real system behind it. I had an OpenClaw instance running here, a Claude Code session open there, a couple of scripts firing on cron jobs I'd half-forgotten about. Capable agents. Zero coordination. No shared mission. No way to see what anything was costing me at a glance.
>
> The irony wasn't lost on me.
>
> What I needed wasn't better agents. I already had those. What I needed was a management layer — something that gave my agents an org chart, a shared goal, a budget, and a reporting structure. Something that let me go from managing agents willy-nilly to actually running them like a company.
>
> That's exactly what Paperclip does. It launched in March 2026 and crossed 44,000 GitHub stars in under three weeks — one of the fastest-rising open-source AI repositories of the year — because it solved a problem many people had but couldn't name. It's an open source orchestration platform that sits above your existing agents — OpenClaw, Claude Code, Codex, Gemini, Cursor, whatever you're already running — and turns them into an organized workforce.

**AI Lesson intro**
> Running one AI agent is easy. Running ten is chaos — unless you have a control plane. Paperclip is that control plane: open source, self-hosted, and built around the mental model of a company rather than a pile of scripts. This lesson walks through the design patterns for scaling from a single agent to a fully orchestrated AI workforce, introduces Paperclip's core mechanics, and shows you exactly which agents you can plug in and how.

**The Three Levels of Agent Management**
> Before touching Paperclip, it helps to understand where you are and where you're going. Agent management follows a natural progression — and most business professionals are stuck at Level 1.
>
> **Level 1 — Single-task agents (where most people are now)**
> One agent. One job. You prompt it, review the output, and move on. This works fine for isolated tasks: summarizing a report, drafting an email, generating code. The problem is that the agent has no memory of your business, no connection to your goals, and no accountability. Every session starts from zero.
>
> **Level 2 — Parallel specialized agents**
> Multiple agents, each owning a discrete function, running on a schedule. A Content Writer fires every four hours. An SEO Analyst runs every eight. A Social Manager every twelve. They don't directly collaborate, but they share a common goal hierarchy. This is where the value of specialization shows up — but coordination is still mostly manual without the right infrastructure.
>
> **Level 3 — Hierarchical orchestration (the full company model)**
> This is Paperclip's design target. A CEO agent interprets a company mission ("Build the #1 AI note-taking app to $1M MRR"), decomposes it into projects, assigns work down an org chart, and escalates blockers up to you — the human board. Every task at every level traces back to the mission. Agents know not just *what* to do, but *why* they're doing it.
>
> The mental model shift here is significant. You stop thinking "I'm prompting an AI" and start thinking "I'm managing a team." That reframe changes how you design workflows, assign responsibilities, and evaluate output.

**How to Access Paperclip**
> **Cost:** Free. MIT-licensed. Open source. You pay only for the AI provider tokens your agents consume.
> **Requirements:** Node.js 20 or higher and pnpm 9.15 or higher. Paperclip is self-hosted — no Paperclip account required.
> **Setup:** The official Paperclip quickstart walks you through installation, database configuration, and your first company in under fifteen minutes. Once running, the dashboard is your board of directors view — org chart, task board, agent status, budget tracker, and audit log in one place.
> **Skill level:** No coding required. If you're comfortable opening a terminal, you can follow this.
> **Note:** Paperclip launched in March 2026 and is under active development. Configuration details may evolve quickly — always verify steps against the official docs before following any third-party guide, including this one. *(Verified: April 2026)*

**The Core Design: How Paperclip Structures a Company**
> Every Paperclip deployment organizes around five building blocks:
>
> **Company** — The top-level unit. You define a mission, set a monthly budget, and build an org below it. One Paperclip instance can run multiple companies with complete data isolation between them.
>
> **Agents (Employees)** — Every employee is an AI agent with a title, a reporting line, a description of its capabilities, a monthly spend budget, and a status (active, idle, running, error, paused, or terminated). Agents sit in a strict tree hierarchy — every agent reports to exactly one manager, except the CEO.
>
> **Issues (Tasks)** — The unit of work. Each issue has a title, description, status, priority, and one assignee. Issues nest under parent issues, creating a traceable chain back to the company goal. The status lifecycle runs: backlog → todo → in_progress → in_review → done. Only one agent can own a task at a time — enforced automatically to prevent duplicate work.
>
> **Heartbeats** — Agents don't run continuously. They wake on a trigger: a scheduled timer, a new task assignment, an @-mention in a ticket, or a manual invoke from the dashboard UI. Each heartbeat, the agent checks its assignments, picks up work, executes, and updates status. This is what keeps costs predictable and prevents runaway loops.
>
> **Governance** — You're the board. Certain actions require your approval before they execute: hiring new agents, the CEO's initial strategic plan, and major overrides. You can pause, resume, reassign, or terminate any agent at any time. Every action is logged in an immutable audit trail.

**The Agents You Can Manage**
> Paperclip connects to agent runtimes through adapters — plug-in connectors that bridge the orchestration layer to the actual AI doing the work. Here's what ships out of the box, with guidance on when to use each:
>
> *For coding and technical tasks:*
> **Claude Local** (claude_local) — Runs Claude Code locally. Best for agents handling writing, research, code generation, or multi-step reasoning. A natural starting point if you're already in the Anthropic ecosystem.
> **Codex Local** (codex_local) — Runs OpenAI Codex CLI locally. The parallel option for engineering agents on OpenAI models.
> **Gemini Local** (gemini_local) — Runs Gemini CLI locally. Relevant for teams embedded in the Google Workspace ecosystem.
> **Cursor** (cursor) — Connects the Cursor IDE as an agent runtime. Good for development agents that need active file access during execution.
>
> *For operations and automation:*
> **Process Adapter** (process) — Executes arbitrary shell commands. Use this for scripts, scheduled jobs, data pipelines, or any automation that doesn't require an LLM. This is your bridge from AI agents to traditional workflow tools.
> **HTTP Adapter** (http) — Sends webhook payloads to any external service or custom agent. Anything that can receive an HTTP request can become an employee in your Paperclip org. If you've built your own agent or need to connect a third-party service, this is your bridge.
> **OpenClaw Gateway** (openclaw_gateway) — Sends wake payloads to an OpenClaw instance via its gateway URL (the public or local address where your OpenClaw instance accepts incoming requests). This is the adapter I'm using as my foundation. If you're already running OpenClaw, Paperclip doesn't replace it — it wraps it in governance, giving your existing agent a boss, a budget, and a place in an org chart.
>
> **Security note:** As of April 2026, security researchers have disclosed a high-severity vulnerability in OpenClaw (CVE-2026-33579) that allowed privilege escalation via the pairing mechanism. Patches have been released. Before connecting any OpenClaw instance to Paperclip, ensure you are running the latest patched version and that authentication is properly configured.

**CrewAI: The Enterprise Framework Option**
> If your team has Python developers and needs a code-first multi-agent system — with enterprise compliance, custom tool integrations, and production-grade monitoring — CrewAI is the reference framework worth evaluating alongside Paperclip.
>
> Where Paperclip is a **control plane** (it manages agents regardless of how they were built), CrewAI is a **framework** (it defines how agents are constructed, what roles they play, and how they hand off work). The two are complementary: a CrewAI-built agent can connect into Paperclip via the HTTP adapter.
>
> CrewAI's Agent Management Platform offers three deployment paths: an open source framework for developers, AMP Cloud (managed SaaS), and AMP Factory (self-hosted on AWS, Azure, or GCP). The Studio interface provides drag-and-drop workflow building with no coding required. Native integrations include Gmail, Microsoft Teams, Notion, HubSpot, Salesforce, Slack, and Zendesk.
>
> According to Insight Partners, CrewAI currently powers 1.4 billion agentic automations at organizations including PwC, IBM, Capgemini, and NVIDIA. It's best suited for teams that need defined role delegation at scale, have Python-comfortable developers, or require enterprise compliance certifications like SOC 2.
>
> **The practical comparison:** Paperclip gets you running in under fifteen minutes with no coding. CrewAI offers deeper programmatic control and a mature enterprise track record. Start with Paperclip if you're a solo operator or small team. Evaluate CrewAI AMP if your IT or engineering team is building production multi-agent systems with compliance requirements.

**What Paperclip Can't Do (Yet)**
> **It's brand new.** Paperclip launched in March 2026. That means limited independent validation, an evolving feature set, and documentation that's still catching up to the code. It's worth running in a test environment before connecting it to production agents.
>
> **The Cliphub marketplace isn't live.** The feature that lets you import a pre-built org — a full "Content Marketing Agency" with agents, goals, and skills — in seconds is listed as coming soon. For now, you build company structures manually.
>
> **It's self-hosted only.** There's no managed cloud option. You own the infrastructure. The embedded database works well locally; scaling to dozens of agents across multiple companies may require more infrastructure planning.
>
> **Budget enforcement is monthly, not real-time.** Paperclip auto-pauses agents at 100% of their monthly spend cap, with a soft warning at 80%. But within a single heartbeat, an agent can still make expensive calls before the cap applies. Set conservative budgets while you're learning your agents' token patterns.
>
> **Governance controls hiring, not behavior.** Board approval is required to add agents to the org chart. What an individual agent does during a heartbeat is determined by its own system prompt and adapter runtime — you still need to design responsible agent instructions separately.

**Closing**
> I'm building this same setup myself, moving from a collection of disconnected agents to a single coordinated dashboard. The infrastructure is free. The agents are ones you're probably already running. The missing piece — until now — was the management layer.

**Non-lesson content (newsletter promotion, kept for completeness)**
> LISTEN TO THE AI ENTERPRISE ON THE ROGUE AGENTS PODCAST — This is my latest project, while we do have audio summaries for each newsletter. They are not ideal for listening; they are simple text-to-speech. We created a way to provide a weekly summary of the newsletters in this podcast. And actually, it's a work in progress. Right now, you get a pretty good podcast recap of the previous week's newsletters. But over time, they will be better. That's the plan.
>
> What happens when two AI agents break down the week's biggest AI news? You get Rogue Agents. Vera and Neuro deliver the stories that matter in enterprise AI — the deals, the tools, the breakthroughs, and the stuff everyone's getting wrong — in 15-20 minutes every week. (https://theaie.net/podcasts/rogue-agents)

> AI EXTRA CREDIT — upcoming free virtual events from the All Things AI community: **April 22nd** | Live at The American Underground | "Building Your Startup in the Age of AI" (Mark Hinkle, Raleigh Durham Startup Week). **May 6th** | LinkedIn Live | "Why Jensen Huang's Betting on Confidential Computing in the AI Factory" (Mark Hinkle with Aaron Fulkerson, CEO of Opaque Systems).

(Cookie banner and footer social links omitted.)
