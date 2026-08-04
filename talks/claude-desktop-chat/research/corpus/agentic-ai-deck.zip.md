---
source_file: agentic-ai-deck.zip
source_type: chat-export
ingested_at: 2026-06-05
---

# Agentic AI at Work — Presentation Skeleton (73-slide deck outline + 2 annotated UI screenshots)

> NOTE FOR THE EDITOR — This source is a **prior, broad-scope deck** that covers Claude Code AND Cowork side by side across 7 sections / 73 slides. The new Talk `claude-cowork-funcional` is deliberately scoped to the **functional / high-level use of Claude Cowork**, de-emphasizing Claude Code and persistence/file internals. All Code-related and file-path/storage content below is preserved losslessly so it can be **selected against, contrasted, or dropped** — it is not pre-filtered. The richest Cowork-functional material is in the per-concept "what it is", "demo", and "do's/don'ts" blocks; the `where it lives` file-tree blocks are mostly Code-internals and likely de-emphasized for this Talk.

## Provenance
- Original location: `research/llm-chats/agentic-ai-deck.zip`
- Format: zip-chat (one `presentation-skeleton.md` + two annotated `.png` UI screenshots)
- Author / source: not stated inside the file. Self-described as "Agentic AI at Work — Presentation Skeleton · 7 sections · 73 slides · Claude Code & Cowork on the desktop".
- Date of original: file mtime 2026-06-02. Content references features dated through June 2026 (Opus 4.8, dynamic workflows research preview, CLI v2.1.154+).

## Key claims
- **The deck's organizing thesis:** Claude Code (terminal / Code tab) and Cowork (GUI / Cowork tab) are **the same agent engine on different surfaces** — "Same engine. Different surface." Same files, same skills, same MCP, same plan→approve→redirect loop.
- The capabilities are grouped in **four tiers**: **Foundation** (persistent instructions · auto memory · working directory · agentic loop · Cowork approval), **Agent capabilities** (skills · subagents), **Integration & output** (connectors · plugins · artifacts), **Automation** (scheduled tasks · dynamic workflows).
- Every concept is taught in the same fixed order: `what it is` → `demo` → (`extras`) → `where it lives` → `do's, don'ts & commands`.
- **The reframe (the deck's central pitch):** *"Stop prompting. Start delegating."* — you stop typing one message at a time and hand over an outcome; the agent plans it, works on your real files, and you steer.
- **Markdown is the lingua franca:** almost everything you configure (CLAUDE.md, SKILL.md, agent files, plugin docs, outputs) is a plain-text `.md` file.
- **Slash commands are a Claude Code thing.** The deck's `Env` column distinguishes **Code** (Code tab only) from **Code · Cowork** (Code command with a Cowork GUI equivalent). Cowork is GUI-only, no slash commands — control is the mode dropdown, per-action approve/redirect prompts, and the folder picker.
- **Cowork-specific functional claims (most relevant to this Talk):**
  - Cowork runs the same agentic loop as Code but with **no Plan mode and no terminal** — control is a single two-way switch: **"Ask before acting"** (default; pauses before each action) vs **"Act without asking"** (runs straight through).
  - **Two things are always true in either Cowork mode:** Claude always asks before permanently **deleting** a file, and always asks before using a **new app** on your computer (some apps — trading, crypto — blocked by default).
  - Cowork **does NOT load project-directory skills** (`<project-root>/.claude/skills/`) — that's a Code mechanism. To use a skill in Cowork, install it as a **user-level** skill (Customize → Skills) or **ship it inside a plugin**. Plugin-provided skills work in both Chat and Cowork.
  - Cowork **subagents** are coordinated "under the hood" — no manual `/agents` config exposed in the GUI.
  - **Scheduled tasks** are a Cowork feature (Scheduled tab / `/schedule`): describe a job once, pick a cadence (hourly/daily/weekly/weekdays/on-demand), each run spins up its own fresh Cowork session.
  - **Live Artifacts** (Cowork, April 2026, paid): persistent dashboards that refresh with current data on open; saved in the Cowork "Live artifacts" tab; connect to MCP data sources.
  - **Cowork has no audit trail** — "Not suitable for regulated or sensitive data." Every output is a draft.
  - **Dynamic workflows are Code-only** — NOT supported in Cowork.
- **Governance non-negotiables:** no PII/confidential/regulated/NDA data into the wrong surface; every output is a draft (verify figures, quotes, claims); keep prompt+inputs+outputs together for auditability; layer guardrails (folder permissions → CLAUDE.md → vetted plugins → human review).
- **The one habit (closing line):** *"Anything you explain to Claude twice is a skill you should write once."*

## Definitions and terminology
- **Section vs Slide:** a Section is a collection of slides on one topic; a Slide is one screen, one idea, numbered `section.slide` (e.g. 3.4 = Section 3, slide 4).
- **Agentic loop:** "Gather context → act → check → repeat." The engine that makes Claude an agent rather than a chatbot; runs on both Code and Cowork in every mode. What you control is not *whether* there's a loop but *how much it pauses to check with you* (the permission mode).
- **Permission / checkpoint modes:** Per-action approval (Ask / Ask before acting — both, default) · Up-front plan (Plan mode — Code only) · No checkpoint (Auto / Act without asking — both).
- **Project (Chat/Cowork):** a self-contained workspace with its own chat history and knowledge base; three persistent layers (Instructions, Knowledge base, Chats). Chats within a project do NOT share context with each other — only the knowledge base is shared.
- **CLAUDE.md:** the behavioral contract — plain markdown read at session start; user-level `~/.claude/CLAUDE.md` (all projects) + project-level `./CLAUDE.md`. Keep under ~200 lines. **Cowork equivalent: the project context panel (GUI) — same concept, no editable .md file.**
- **Auto memory:** notes Claude writes for itself from corrections and preferences; editable markdown; complements CLAUDE.md. Cowork has full auto memory per project, viewable with `/memory`.
- **Working directory + permissions:** operates inside a sandboxed local VM; accesses only folders you explicitly grant. **In Cowork the OS folder picker — not a config file — controls which folders are granted; there is no `settings.json` to edit in Cowork.**
- **Skill:** a folder + `SKILL.md` with YAML frontmatter (name + description). Description drives triggering (semantic, not keyword). One job per skill. "If you write 'and also', split it."
- **Subagent:** an isolated assistant with its own context, instructions, tool access; returns one summary. Built on top of the agentic loop, not a replacement. Auto-delegation is unreliable — explicit invocation by name is dependable.
- **Skill vs Subagent (the one-line rule):** "Small, and should stay in front of you → Skill. Big or noisy, and should run in a side process → Subagent." A skill runs *inside* your conversation; a subagent runs *beside* it.
- **Connector (MCP):** Model Context Protocol — standardized connection to external systems (Drive, Gmail, Slack, DBs, APIs). "The hands — what the agent can touch that it otherwise cannot."
- **Plugin:** distribution unit for a full workflow — bundles skills + agents + hooks + MCP in one install. "Ship the whole thing." (Also: *the* way to get a skill into Cowork.)
- **Artifact:** live, runnable output rendered in a side panel. Two tiers in 2026: Standard (all plans) and Advanced (paid — persistent storage via `window.storage`, AI-powered, MCP connections, Live Artifacts in Cowork).
- **Scheduled task:** Cowork's proactive mode — describe a job once, pick a cadence, each run is its own fresh Cowork session.
- **Dynamic workflow:** Claude writes a JavaScript orchestration script on the fly, runs it in the background, fans work across tens–hundreds of parallel subagents (up to 1,000/run, 16 concurrent) with built-in adversarial verification. Code-only, research preview (May/June 2026), needs Claude Code v2.1.154+.

## Evidence and examples
Concrete demos and example artifacts the deck scripts (Cowork-relevant ones flagged):
- **Opening demo (the hook, slide 2.3):** "Organise this folder of 8 PDFs by topic and give me a one-paragraph summary of each." Run live; let them watch Claude plan, touch files, deliver.
- **CLAUDE.md demo (3.2):** an Acme Co marketing CLAUDE.md (plain-English, lead-with-recommendation, "customers" not "users", flag <80% certainty with `[uncertain]`, never include PII) → a blank prompt about Q3 churn → output obeys all unstated rules.
- **Cowork approval demo (3.19, Cowork-specific):** messy ~10-file folder, default "Ask before acting" mode → "Rename every file to `YYYY-MM-DD_description`, sort into subfolders by type, write an index" → Claude proposes first change and pauses; you approve or redirect "copy, don't move the originals."
- **Skills demo (4.2):** a `doc-summary` skill (Purpose / Key points / Decisions / Risks / Next steps). And a parameterized `digest` skill (4.3) with `--since` / `--format` args and a bundled `scripts/recent.py`.
- **Subagents demo (4.8):** 8 vendor proposals reviewed three ways in parallel (terms-extractor, risk-screener, scorer) → combined table. Includes a full `risk-screener.md` agent file with read-only tools, parameter contract in the body, table-only output.
- **Connectors demo (5.2):** Google Drive MCP — search a "Q3 Planning" folder, refuse the "HR/Compensation" folder (permission boundary). MCP range examples (5.4): Figma, Vercel, Cal.com, Home Assistant, Roblox Studio.
- **Artifacts demo (5.14):** build an interactive experiment tracker (React), add rows live, chart updates, Publish → shareable link; persistent storage via `window.storage`; **Live Artifact in Cowork** — "Build a live dashboard showing our open deals and last 5 closed-won accounts," reopen next day → data fresh.
- **Scheduled tasks demo (6.2, Cowork-specific):** a daily 8am briefing — "Summarise everything that needs my attention from the last 24 hours… group by urgency, under 200 words." Set via `/schedule` or Scheduled tab → New.
- **Dynamic workflows demo (6.7, Code-only):** screen 200 résumés against 3 criteria, two independent reviewers each, flag disagreements, return CSV.
- **Two hands-on missions embedded in the deck:**
  - **Section 3 mission (3.20, Claude Code):** "Build your Claude Code workspace" — `/init` + edit CLAUDE.md, verify the permission boundary, Plan mode reorg, cross-session memory.
  - **Section 4 mission (4.12, Claude Code):** "Build two specialists" — one `meeting-notes` skill + one `action-screener` subagent, both invoked explicitly.
- **Availability matrices** appear for every concept (Web/Chat · Code · Cowork · Studio with ✓ / ⚠️ / ✗ / ▣ markers) — useful raw data for any "where does this work" slide. Preserved in full in the excerpts below for the Cowork-relevant ones.
- **Plugin marketplaces (5.10):** `anthropics/claude-plugins-official` (55+ plugins), `anthropics/knowledge-work-plugins` (11 production plugins), plus community: `wshobson/agents`, `jeremylongshore/...` (425 plugins / 2,810 skills), `hyperskill/...`, `claudemarketplaces.com`.

## Inconsistencies / open questions
- **Scope mismatch with this Talk (the big one):** This deck is ~50% Claude Code content (Plan mode, slash commands, project-directory skills, subagents config, dynamic workflows, the two hands-on missions are both Code-based). The new Talk de-emphasizes Code. The Editor will need to **select Cowork-facing slides and translate or drop the Code-only ones.** Everything is preserved here so that selection is the Editor's call, not pre-made.
- **Formatting glitch in source (slide 7.5):** the `/fast` command row is malformed in the original — renders as `| `/fast [on\| Code |off]` | Toggle fast mode...` (the Env/cell boundaries are scrambled). Intended meaning: `/fast [on|off]` · Code · "Toggle fast mode for quicker responses." Preserved verbatim in excerpts.
- The deck references two annotated screenshots by filename but the **annotations themselves are not transcribed in the markdown** — they live only in the image bytes (see Images / diagrams, pending Phase 2). The markdown only lists *how many* labelled elements each has (Chat tab: 12; Cowork tab: 14).
- Feature dates/version numbers are fast-moving (the deck itself flags "Anthropic ships updates frequently" and "re-verify before presenting"). Treat specific version gates (Opus 4.8, v2.1.154+, April 2026 Live Artifacts) as point-in-time.

## Images / diagrams

### `agentic-ai-deck.zip/images/screenshot-chat-tab.png`
- Provenance: bundled in the deck ZIP as `screenshot-chat-tab.png`; referenced by slide 1.2 ("Chat tab anatomy — annotated diagram with 12 labelled elements: tabs, + New chat, Projects, Artifacts, account/plan, attachment, model + effort, voice, connector chips, Dispatch"). JPEG, 2184×1456.
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

### `agentic-ai-deck.zip/images/screenshot-cowork-tab.png`
- Provenance: bundled in the deck ZIP as `screenshot-cowork-tab.png`; referenced by slides 1.2 and 7.1 ("Cowork tab anatomy — annotated diagram with 14 labelled elements; adds Scheduled routines, Live artifacts, Dispatch Beta, Work-in-a-project, Ask permission mode"). This is the **most Cowork-functional asset in the source** — the annotated Cowork interface. JPEG, 2198×1452.
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

## Raw / preserved excerpts

### Deck header + organization (slides 0–"How this deck is organised")
> # Agentic AI at Work — Presentation Skeleton
> *7 sections · 73 slides · Claude Code & Cowork on the desktop*
> *Note: slash commands are Claude Code (terminal / Code tab). The **Env** column in command tables shows where each works: **Code** = Code tab only; **Code · Cowork** = the command is Code, and Cowork has a GUI equivalent (button/menu) for the same action.*
>
> **Sections** are collections of slides on one topic. **Slides** are one screen, one idea — numbered `section.slide`.
>
> | Section | Topic | Slides |
> |---|---|---|
> | **1 — Orientation** | Title, interface anatomy, projects | 1.1–1.5 |
> | **2 — Framing** | Concept map, Markdown primer, the reframe | 2.1–2.3 |
> | **3 — Foundation** | Persistent instructions · Auto memory · Working directory · Agentic loop · Cowork approval · **capstone mission** | 3.x |
> | **4 — Agent capabilities** | Skills · Subagents | 4.x |
> | **5 — Integration & output** | Connectors · Plugins · Artifacts | 5.x |
> | **6 — Automation** | Scheduled tasks · Dynamic workflows | 6.x |
> | **7 — Synthesis & close** | Code vs Cowork, governance, one habit, utilities | 7.x |
>
> **Each concept is a mini-section of slides, all in the same order:** `what it is` → `demo` → (`extras`, if any) → `where it lives` → `do's, don'ts & commands`.

### The concept map (slide 2.1)
> | Tier | What it means | Capabilities |
> |---|---|---|
> | **Foundation** | What you set up first — how the agent behaves and what it can touch | Persistent instructions · Auto memory · Working directory · Agentic loop · Cowork approval |
> | **Agent capabilities** | How the agent thinks and delegates | Skills · Subagents |
> | **Integration & output** | How it reaches outside itself and produces things | Connectors · Plugins · Artifacts |
> | **Automation** | Work that runs without you — on a schedule, or fanned across many agents | Scheduled tasks · Dynamic workflows |
>
> *Same engine, different surface: Code tab = terminal, Cowork tab = GUI.*

### The reframe (slide 2.3)
> **Headline:** Stop prompting. Start delegating.
> The shift this whole session is about: you stop typing one message at a time and start handing over an *outcome*. The agent plans it, works on your real files, and you steer — instead of you doing every step yourself.
> > **Opening demo:** "Organise this folder of 8 PDFs by topic and give me a one-paragraph summary of each." Run it live. Don't explain the mechanics — just let them watch Claude plan, touch files, and deliver. That single demo is the hook for everything that follows.

### Chatting vs Delegating (slide 3.16)
> | | Chatting | Delegating to an agent |
> |---|---|---|
> | **How you work** | One message at a time | Describe an outcome |
> | **Steps** | You do each one | It plans and executes them |
> | **Output** | Text in the window | Files on your disk |
> | **Your role** | Type the next prompt | Read the plan, steer mid-task |
>
> *Note: "chatting" and "delegating" are two ways of working — not two products. You can chat in the Cowork tab and delegate from the Chat tab. The difference is the mode, not the surface.*

### Cowork: how approval works (slide 3.19) — VERBATIM, most relevant slide to this Talk
> **Headline:** Cowork — the same loop, a simpler approval model
> Cowork runs the same agentic engine as Claude Code, but with **no Plan mode and no terminal**. Instead of one consolidated up-front plan, you control it with a single two-way switch.
>
> ### The mode selector — two options (the "Ask ∨" dropdown)
> | Mode | What Claude does | Use it when |
> |---|---|---|
> | **Ask before acting** *(default)* | Pauses and asks before **each action** it takes on your behalf — editing a file, running a command, using a connector, opening an app | New tools, unfamiliar files, anything you want to watch closely |
> | **Act without asking** | Works straight through without pausing — faster, riskier | Well-defined tasks you trust, while you're actively supervising |
>
> > **Two things are always true, in either mode:**
> > - Claude **always asks before permanently deleting** a file.
> > - Claude **always asks before using a new app** on your computer (computer use is prompted per-app; some apps — trading, crypto — are blocked by default).
>
> ### What "each action" means
> The pause is for things Claude *does*, not things it reads. Reading files in a folder you already granted just proceeds. The approval prompt appears when it's about to **change something or reach outside** — write, move, run, connect, click.
>
> ### Do and Don'ts
> | ✅ Do | ❌ Don't |
> |---|---|
> | Start in **Ask before acting** until you trust a workflow | Switch to "Act without asking" on unfamiliar files or untrusted sites |
> | Watch the per-action prompts — they're your steering points | Click approve reflexively; read what each step will change |
> | Keep a dedicated working folder so you know what's in scope | Grant a folder with confidential data or credentials |
> | Use "Act without asking" only while actively supervising a trusted, well-defined task | Walk away with "Act without asking" on |
>
> *Cowork is GUI-only — no slash commands. Control is the mode dropdown, the per-action approve/redirect prompts, and the folder picker. For a hard, un-talk-around-able block (e.g. /confidential/), you'd need Claude Code's configuration-level enforcement — Cowork can only ask, not hard-block.*

### Skills vs Subagents (slides 4.9, the comparison table)
> | | **Skill** | **Subagent** |
> |---|---|---|
> | **What it is** | Reusable instructions (+ optional scripts) the main agent loads | A separate agent the main one delegates a job to |
> | **Where it runs** | *Inside* your current thread — in front of you | *Beside* it — its own context window, own tools |
> | **Effect** | Changes **how the main agent behaves** for this task | Offloads a whole sub-task and **returns a summary** |
> | **Context** | Shares your context — you see every step | Isolated — you get the result, not the transcript |
> | **Parallel?** | No — one inline task at a time | Yes — several can run at once |
> | **Triggering** | Auto-loaded when your request matches its description | Reliable only when you name it explicitly |
> | **Lives in** | `.claude/skills/<name>/SKILL.md` | `.claude/agents/<name>.md` |
>
> > **Small, and should stay in front of you → Skill.** **Big or noisy, and should run in a side process → Subagent.**

### Skills in Cowork — the project-skills caveat (slide 4.5, the Cowork note verbatim)
> **Important for Cowork:** project-directory skills (`<project-root>/.claude/skills/`) are a **Claude Code** mechanism — Code scans the working directory + parents up to the repo root at session start. **Cowork does not load project-directory skills.** To use a skill in Cowork, install it as a user-level skill (Customize → Skills / the directory) or ship it inside a plugin. Plugin-provided skills work in both Chat and Cowork.

### Connectors — the range (slide 5.4 intro)
> **Headline:** Any app that exposes an MCP server becomes something you can talk to
> MCP isn't only for productivity tools… A few cases that show the range: Figma · Vercel · Cal.com · Home Assistant (86+ tools over a WebSocket) · Roblox Studio (96+ tools).
> > **The pattern in all five:** the platform opened its own internals as MCP tools. Claude didn't get a new capability — the *platform* became conversational. Any system with an API can do the same thing.

### Artifacts — the two tiers (slide 5.13)
> **Standard Artifacts (all plans):** React components · HTML pages · SVG graphics · Mermaid diagrams · Code snippets · Markdown · Downloadable `.docx`/`.pptx`/`.xlsx`/`.pdf`; single-file outputs only.
> **Advanced Artifacts (paid plans):** Persistent storage (up to 20 MB, survives via `window.storage`) · AI-powered (artifact calls Claude's own API) · MCP connections · **Live Artifacts (Cowork)** — persistent dashboards that refresh with current data on open; saved in the Cowork "Live artifacts" tab.

### Scheduled tasks (slide 6.1) — Cowork-specific
> Everything so far has been *reactive* — you ask, Claude does. Scheduled tasks make Cowork **proactive**: you describe a job once, pick a cadence, and Claude runs it automatically.
> - You describe the task once; Claude saves the prompt as the task's instructions
> - Pick a cadence: hourly · daily · weekly · weekdays · or **on demand** ("Run now")
> - Each run spins up its **own fresh Cowork session** and posts a notification when done
> - Has the **same powers as a normal Cowork task** — connectors, skills, installed plugins
> - Lives in the **Scheduled** tab in the Cowork sidebar
> - All paid plans; Cowork on Claude Desktop

### Scheduled tasks — THE caveat (slide 6.3) — repeated across both ZIPs
> **Scheduled tasks only run while your computer is awake and Claude Desktop is open.** If the machine is asleep or the app is closed at the scheduled time, the run is **skipped** — then runs automatically once you wake the machine or reopen the app (with a "this was skipped" notification). For runs that must fire even when your computer is off, you need a **cloud routine**, not a local scheduled task.

### Claude Code vs Cowork — the close (slide 7.1)
> **Same engine. Different surface.**
> | | Web / Chat | Claude Code | Cowork |
> |---|---|---|---|
> | **Access** | Browser or app, no install | Desktop app — Code tab + terminal | Desktop app — Cowork tab |
> | **Audience** | Everyone | Developers / technical | Knowledge workers, no terminal |
> | **Surface** | claude.ai · mobile app | Terminal / CLI + Code tab | Cowork tab — GUI, no terminal |
> | **Core job** | Chat, Q&A, one-off tasks | Write, edit, ship code | Multi-step knowledge work on files |
> | **Persistent context** | Project instructions + memory | `CLAUDE.md` files | Project context + auto memory |
> | **Skills** | User-level via Settings | User + project `.claude/skills/` + Vercel CLI | User-level via Settings + plugins (no project skills) |
> | **Subagents** | ✗ | Configured via `/agents` | Under the hood |
> | **Plugins** | Skills only via Settings | `/plugin install` + CLI | GUI marketplace |
> | **Dynamic workflows** | ✗ | Yes (Max/Team/Ent) | ✗ |
> | **Slash commands** | ✗ | Full set | GUI equivalents |
> **Shared:** same agent engine · same files · same skills · same MCP · same plan → approve → redirect loop.

### Governance & verification (slide 7.2) — verbatim
> - **No PII or confidential data where it shouldn't go.** Nothing regulated, nothing under NDA, into the wrong surface.
> - **No audit trail in Cowork.** Not suitable for regulated or sensitive data.
> - **Every output is a draft.** Verify figures, quotes, and factual claims against the source.
> - **Reproducibility.** Keep prompt + inputs + outputs together — the work must be auditable.
> - **Layer your guardrails:** Folder permissions → CLAUDE.md rules → Vetted plugins only → human review.

### One habit (slide 7.3)
> *"Anything you explain to Claude twice is a skill you should write once."*

### Availability matrices for Cowork-relevant concepts (verbatim, Cowork column noted)
> - **Persistent instructions (3.3):** Web ✗ · Code ✓ · Cowork ⚠️ · Studio ✗ — "Cowork: project context panel — same concept, different mechanism, no editable .md file."
> - **Auto memory (3.7):** Web ⚠️ · Code ✓ · Cowork ✓ · Studio ✗ — "Code & Cowork: full auto memory per project, viewable with `/memory`."
> - **Working directory (3.12):** Web ✗ · Code ✓ · Cowork ✓ · Studio ✗ — "In Cowork, the OS folder picker — not a config file — controls which folders are granted. There is no `settings.json` to edit in Cowork."
> - **Agentic loop (3.17):** Web ✗ · Code ✓ · Cowork ✓ — "Code adds Plan mode; Cowork uses per-action approval."
> - **Skills (4.5):** Web ⚠️ · Code ✓ · Cowork ✓ — "Cowork: user-level skills only (Customize → Skills) + plugin-provided skills — **not** project-directory skills."
> - **Subagents (4.10):** Web ✗ · Code ✓ · Cowork ⚠️ · Studio ✗ — "Cowork: subagents coordinated under the hood — no manual `/agents` config exposed in the GUI."
> - **Connectors (5.6):** Web ✓ · Code ✓ · Cowork ✓ — "full MCP connector support." "Web and Cowork connectors are configured via the Settings UI — no local file to edit."
> - **Plugins (5.11):** Web ⚠️ · Code ✓ · Cowork ✓ — "Cowork: GUI plugin marketplace." "(This is *the* way to get a skill into Cowork — bundle it in a plugin.)"
> - **Artifacts (5.16):** Web ✓ · Code ⚠️ · Cowork ✓ · Studio ⚠️ — "Cowork: full Artifacts + Live Artifacts (paid, April 2026) in the Cowork sidebar."
> - **Scheduled tasks (6.3):** Web ✗ · Code ▣ · Cowork ✓ — "Cowork: full scheduled tasks via the Scheduled tab / `/schedule`. Code: same Desktop engine surfaces as **Routines**. ▣ = different name, same underlying scheduler."
> - **Dynamic workflows (6.10):** Web ✗ · Code ✓ · Cowork ✗ — "Code only… Cowork, Web/Chat, Studio: not supported."

### Source formatting glitch (slide 7.5, preserved verbatim)
> `| `/fast [on\| Code |off]` | Toggle fast mode for quicker responses. |`
> *(Intended: `/fast [on|off]` · Env: Code · "Toggle fast mode for quicker responses." — the cell boundaries are scrambled in the original markdown.)*

### Note on omitted Code-internals
The deck's `where it lives` file-tree blocks for CLAUDE.md (3.3), auto memory (3.7), working dir (3.12), the agentic loop (3.17), skills (4.5), subagents (4.10), connectors (5.6), plugins (5.11), and dynamic workflows (6.10) are detailed `~/.claude/...` and `<project-root>/.claude/...` directory trees — Claude Code internals, largely out of scope for a functional Cowork Talk. They are NOT reproduced verbatim here to keep the record focused; the Cowork-relevant caveats from each (folder picker, no settings.json, plugin-as-skill-delivery, etc.) are captured above. If the Editor needs an exact file tree, the original is `research/llm-chats/agentic-ai-deck.zip → presentation-skeleton.md`.
