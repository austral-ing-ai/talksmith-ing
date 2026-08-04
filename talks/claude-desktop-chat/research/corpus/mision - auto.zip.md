---
source_file: mision - auto.zip
source_type: chat-export
ingested_at: 2026-06-05
---

# Misión "Atlas, el analista de mercado de tu equipo" — capstone Cowork workshop (brief + Cowork solution + Codex-equivalent solution + Cowork-vs-Codex comparisons + sample data)

> NOTE FOR THE EDITOR — This ZIP is the **single most on-target source for the new Talk** `claude-cowork-funcional`. It is a complete, hands-on, **non-technical, Spanish-language** workshop that drives a non-programmer through the six core Cowork pieces (Projects · Instructions · Skills · Connectors · Schedule · Artifacts) by building "Atlas", a virtual market analyst, in **four milestones**. It deliberately uses ZERO code and is framed entirely around a real office task. The ZIP also carries two **Codex-comparison** documents (one full Codex re-solution, one concept-by-concept table) that map every Cowork piece to OpenAI Codex — useful if the Talk wants a "vs. the alternative" angle, but secondary. Two PDFs in the ZIP (`mission.pdf`, `mission-claud-res.pdf`) are 1:1 renders of the corresponding `.md` files (no unique content, not transcribed). Sample market-report data lives under `reportes/`.

## Provenance
- Original location: `research/llm-chats/mision - auto.zip`
- Format: zip-chat — a project folder containing: `mission.md` (the brief), `mission-claud- res.md` (the Cowork step-by-step solution), `mission-codex-res.md` (the Codex-equivalent solution), `cowork-vs-codex.md` (mission-mapped comparison), `cowork-vs-codex-comparacion.md` (deck-concept comparison), `mockup-tablero.html` + `mockup-tablero.png` (the dashboard wireframe), `mission.pdf` + `mission-claud-res.pdf` (PDF renders of the .md files), and `reportes/` (3 weeks of sample input `fuentes/` + output reports).
- Author / source: not stated. Internal Talksmith workshop material. Language: Spanish (Río de la Plata / "vos" voseo).
- Date of original: file mtimes through 2026-06-05. Sample data dated weeks of 2026-05-18, 05-25, 06-01. Codex facts "verified against official OpenAI docs, June 2026."
- Note: filename has a literal space ("mision - auto.zip") and the inner folder is "mision - auto/". One inner file has an irregular name with a space before the extension dash: `mission-claud- res.md`.

## Key claims

### The mission framing (from `mission.md`)
- **The premise:** every Monday 8:55am your boss needs a clear weekly report on three companies the team watches — **Apple (AAPL), Microsoft (MSFT), Nvidia (NVDA)**. He wants it **two ways**: a **weekly email in his inbox** AND an **always-updated web page (dashboard)** he can open anytime. He sketches the dashboard on a napkin (= `mockup-tablero.png`).
- Until now an **intern** did this manually: each week he visited many portals (Yahoo Finance, Bloomberg, CNBC…) and pasted what he found into **one file per source** — raw, messy notes left behind in `reportes/` (one subfolder per week, with a `fuentes/` folder inside). That pile is your starting point.
- **The pitch:** instead of doing it by hand forever, you **delegate** — you "hire" Atlas, a virtual analyst that researches the companies, writes the report while you sleep, drops it in the team's mail, and publishes it to a dashboard the boss can open. **Train it once; it works alone after that.**
- **The real prize is not Atlas — it's you, mastering Claude Cowork.** The office task is the excuse to touch every Cowork piece, one by one, in the right order. "When you finish, you won't have 'read about' Cowork. You'll have solved a real work problem with it."
- **Audience:** anyone who has to deliver recurring work, even if they've never programmed. "No coding here: you guide Claude with prompting techniques and combine Cowork's pieces. If you can send an email and move a folder, you have everything you need. The entry barrier is zero. The ceiling is sky-high."

### The four milestones (the spine of the workshop)
| Milestone | What Atlas achieves | Cowork superpower unlocked |
|---|---|---|
| **1 · 🥚 Atlas nace** | **Report on demand:** turns the intern's loose notes into a tidy weekly pulse with a fixed format | **Projects** + **Instructions** + **Skills** |
| **2 · 🔎 Atlas aprende a investigar** | **Autonomous report:** gets news and prices on its own — no more manual copy-paste | **Tools** (web search) + **Connectors** (stock data) |
| **3 · 🐣 Atlas trabaja solo** | **Report ready to send:** every Monday leaves the report as a Gmail draft, ready to review and send | **Connectors** (Gmail) + **Schedule** |
| **4 · 📣 Atlas llega al equipo** | **Public page:** the `pulso-semanal` dashboard publishes to a team-accessible URL and refreshes itself weekly | **Artifacts** (Live Artifacts) · **Connectors** (ShareDuo) · **Skills** |

- **Each milestone is an incremental, independently-useful win** ("like a video game") that adds a new Cowork superpower on top of the previous one. From milestone 1 you already have something useful; at the end the boss receives the email AND opens the web — the two things he asked for — without you touching anything.

### Setup / prerequisites (from `mission.md` + `mission-claud- res.md`)
- **Claude desktop app** (macOS/Windows), latest version. **Cowork does NOT run on web or mobile to CREATE things** — but once built, you can trigger it from your phone.
- **Paid Claude plan** (Pro, Max, Team, or Enterprise). The free plan does not include Cowork.
- The **"Cowork" tab** must be visible (next to "Chat" and "Code"). Not visible → update the app.
- **Web search** must be active: Settings → Capabilities.
- Per-milestone needs are reminded just-in-time, not front-loaded.

### The Cowork solution, milestone by milestone (from `mission-claud- res.md`)
- **M1 — Atlas nace (Projects · Instructions · Skills):**
  - Create a Project "Inteligencia de Mercado Semanal" pointed at your folder (`Documentos/Atlas-Mercado`). The Project gives Atlas its own folder, project memory, and a fixed place for its tasks.
  - Write the **project Instructions** (Atlas's "work contract"): who Atlas is, which companies, audience (your team), tone (Spanish, clear, no jargon), format, and the **golden rule — NEVER gives investment advice / not financial advice** (this disclaimer is pinned here in M1).
  - Build a **Skill `reporte-semanal`** via `/skill-creator`: input = a week's `fuentes/` folder (several raw files, one per portal); reads them ALL, consolidates by company, outputs a fixed-template report (title, executive summary, one section per company with price/move/2-3 news/mood/"what to watch", summary table, sources, legal disclaimer). The most relevant company goes first (marked ⭐). Saves with a `-new` suffix so it never overwrites the example report.
  - Success: the Skill turns several messy files into a report matching the example for that week.
- **M2 — Atlas investiga (Tools · Connectors):** "the hardest jump."
  - **Connect to MT Newswires** (the market-news provider the team subscribes to) — "the best part: **MT Newswires already has a ready connector in Cowork** in the Connectors directory. Nothing to create or configure — just find it and click Connect, like any other app." This is the teaching beat: "you're not programming or creating anything; you connect to a service that already exists, like connecting Gmail."
  - Build a second Skill **`buscar-accion`**: given a ticker + week, fetches price/variation from **Yahoo Finance** via **direct `web_fetch`** to `finance.yahoo.com/quote/<TICKER>/` (not general web search — gives cleaner, more predictable results) and news from **MT Newswires** via the connector. Saves to disk in `fuentes/` as **two cumulative `.txt` files** (`yahoo-finance.txt`, `mt-newswires.txt`), appending a block per ticker without overwriting.
  - **Claude in Chrome:** some pages (Yahoo Finance) render with JavaScript and aren't accessible by web search alone — for those, Cowork can use **Claude in Chrome** as a real browser (needs Chrome installed + the Claude in Chrome extension).
  - Success: Atlas fills `fuentes/` from scratch with data it found itself. "Atlas stopped being an assistant that copies: now it investigates alone."
- **M3 — Atlas trabaja solo (Connectors: Gmail · Schedule):**
  - Connect the **Gmail connector** (one-click in the directory).
  - Ask Atlas to **leave the report as a Gmail DRAFT** addressed to `superboss@gmail.com` (in the live solution the prompt uses `pveiga@gmail.com` in the Codex version) — draft, not direct send, for review control.
  - Schedule with `/schedule` a task **every Monday 8:00** that runs `buscar-accion` → `reporte-semanal` → leaves the Gmail draft, ready before the 9:00 meeting.
  - **THE caveat (repeated everywhere):** scheduled tasks only run with the **computer awake and the Claude app open**; if it was off, Cowork runs the task as soon as you turn it on.
  - Success: draft appears in Gmail AND the recurring task appears in the "Scheduled" tab. Demo tip: don't wait for Monday — use "Run on demand."
- **M4 — Atlas llega al equipo (Artifacts · ShareDuo · Skills):**
  - **ShareDuo is NOT an external MCP connector** — it's Cowork's **built-in sharing**, activated by a call to `update_artifact_settings(share="duo")`. "Nothing to install or register." (The brief `mission.md` framed ShareDuo as something to register as an MCP connector — see Inconsistencies; the actual solution corrects this.)
  - Build a Skill **`publicar-tablero`**: reads the latest `reporte-semana-*.md`, generates the dashboard HTML, creates a **new Live Artifact per week** with ID `pulso-semanal-FECHA` (e.g. `pulso-semanal-2026-06-01`) — so a **history of weekly dashboards** accumulates in Cowork — then activates ShareDuo and returns the public URL.
  - Hook it onto the Monday scheduled task so the dashboard refreshes itself.
  - Success: the team has a **public URL** with the dashboard (no Cowork needed to view), the artifact appears in the Cowork sidebar, and the scheduled task regenerates it every Monday.

### The complete loop (Cowork version)
> `Monday 8:00` → **Schedule** fires → Skill **`buscar-accion`** `web_fetch`s Yahoo Finance + queries MT Newswires via connector, saving `yahoo-finance.txt` + `mt-newswires.txt` in `fuentes/` → Skill **`reporte-semanal`** consolidates into the `.md` report in the **Project** → **Gmail** leaves it as a **draft** for the team → Skill **`publicar-tablero`** generates HTML, creates the **Live Artifact** `pulso-semanal-FECHA` and activates **ShareDuo**, publishing the dashboard to a public URL.

### Cowork vs Codex (from the two comparison files — secondary, for a "vs alternative" angle)
- **Architecture difference:** Cowork runs **only local**, GUI, no terminal, on the real files of a folder you granted. Codex is **hybrid** (local CLI/IDE/desktop-app sandbox OR cloud containers), unified by your ChatGPT account; born a dev tool, pivoting toward knowledge workers (≈5M weekly users, ~20% non-devs).
- **The mapping is ~10/13 concepts direct or close.** Codex can solve the same mission end to end (same `Automation → buscar-accion → reporte-semanal → Gmail → dashboard` circuit) but with more per-file/terminal setup.
- **Cleanest mapping — Skills:** Codex adopted the **same `SKILL.md` standard** and has its own `$skill-creator`. The three skills are written almost identically.
- **Instructions → `AGENTS.md`:** Cowork's GUI Instructions panel becomes a committable text file `AGENTS.md` in Codex.
- **Connectors → MCP:** same concept, different plumbing. Cowork has a one-click directory ("Connect"); Codex uses MCP servers in `config.toml` / `codex mcp`. Affects MT Newswires and Gmail (more setup in Codex).
- **Schedule → Automations:** strong equivalent. Codex adds custom cron, local-vs-worktree mode, and the "Triage" inbox. Same caveat: local-scope tasks need the app open and folder on disk.
- **THE biggest gap — Live Artifacts → (no direct equivalent):** Cowork has a managed, live object refreshed in its panel and published with ShareDuo, zero install. Codex has **no direct equivalent**: it generates real HTML on disk, previewed in its in-app browser and published separately via **Codex Sites** / static hosting; "the life" comes from the Skill regenerating the file, not a managed object. (Codex Artifact Viewer, since Apr 2026, is a preview of generated files — not live interactive web apps.)
- **Audience/surface:** Cowork = non-technical, all buttons/prompts; Codex = a programming agent (app/IDE/CLI) with files (`AGENTS.md`, `config.toml`) in the loop.
- **Governance:** Cowork has no audit trail, all local, every output a draft. Codex has a review queue/Triage, sandbox + permission profiles, but cloud runs mean code/data can upload to OpenAI infrastructure (a concern for sensitive/regulated material).
- **Codex caveat:** features move fast — desktop app macOS (Feb 2026) / Windows (Mar 2026), Artifact Viewer + task sidebar (Apr 2026), CLI v0.136.0 (Jun 2026). Re-verify before presenting.
- Note: `cowork-vs-codex-comparacion.md` explicitly excludes Claude Code from its comparison "even though it appears in the material" — aligning with this Talk's de-emphasis of Code.

## Definitions and terminology
- **Atlas:** the named persona of the virtual analyst the workshop builds. An *educational* exercise; its reports are NOT investment recommendations.
- **Pulso semanal de mercado:** "weekly market pulse" — the recurring deliverable (a 2-minute read before the Monday meeting).
- **`fuentes/`:** the per-week input folder of raw notes, one `.txt` file per portal (the intern's leftovers / the entrada). Output is the `reporte-semana-*.md` sitting beside it (the salida).
- **`reporte-semanal`:** Skill #1 — consolidates `fuentes/*` into the formatted report.
- **`buscar-accion`:** Skill #2 — given ticker + week, researches and writes the `fuentes/` files itself.
- **`publicar-tablero`:** Skill #3 — generates the dashboard HTML, creates/updates the Live Artifact, activates ShareDuo.
- **MT Newswires:** the market-news data provider; in Cowork it's a ready-made one-click connector (https://www.mtnewswires.com).
- **ShareDuo:** Cowork's **built-in** sharing mechanism — `update_artifact_settings(share="duo")` — that gives an artifact a public URL. NOT an external service to install. (The brief mislabels it as an MCP connector to register — corrected in the solution.)
- **Live Artifact `pulso-semanal-FECHA`:** the auto-updating dashboard, one new artifact per week, building a history in the Cowork sidebar.
- **The golden rule / legal disclaimer:** "Reporte interno e informativo; no constituye asesoramiento financiero" — pinned in the project Instructions in M1 and in every report footer.

## Evidence and examples
- **Three weeks of sample data under `reportes/`** — each a `fuentes/` input folder + a finished `reporte-semana-*.md` output, used as both raw material and "correct answer." News and links are REAL (May/June 2026); prices and percentages are APPROXIMATE / illustrative.
  - `semana-2026-05-18/`: fuentes = yahoo-finance.txt, bloomberg.txt (Nvidia), the-next-platform.txt (Microsoft), coincentral.txt (Apple), cnbc.txt, heygotrade.txt. Report: pre-conference week; AAPL +1,5%, MSFT +1,8%, NVDA −2,5% (profit-taking before earnings).
  - `semana-2026-05-25/`: fuentes = yahoo-finance.txt, sec-gov.txt, bloomberg.txt, macdailynews.txt, capital-com.txt, techtimes.txt, blog-google.txt. Report: NVDA the star ⭐ +13% on record earnings (US$81.6B revenue, +85% YoY; US$80B buyback). AAPL +2,7%, MSFT +1,1%. (Teaching point: Nvidia data is split across sec-gov.txt + bloomberg.txt + yahoo-finance.txt — shows why the Skill must read ALL files.)
  - `semana-2026-06-01/`: fuentes = yahoo-finance.txt, coincentral.txt, motley-fool.txt, fx-leaders.txt, cnbc.txt. Report: AAPL the star ⭐ +5,0% (WWDC run-up). MSFT +0,4% (AI "run rate" ~US$37B/yr, Azure +31%). NVDA −7,8% (healthy correction after the record).
- **Exact copy-paste prompts** are provided for every step (project Instructions text, three `/skill-creator` descriptions, the M1.3 generation prompt, the M3 Gmail-draft prompt, the `/schedule` prompt, the M4 publish prompt). These are reusable verbatim — see excerpts.
- **The dashboard wireframe** (`mockup-tablero.html` / `.png`): a deliberately hand-drawn/Comic-Sans "napkin sketch" (the boss's sketch) of the dashboard — title + date + "LIVE" chip, executive-summary box, one card per company (ticker, price, ▲/▼ %, mood, 2 news links, "what to watch"), and a summary table. Green = up, red = down. "Same design every week, only the data changes."
- **Facilitator guide** (in both solution files): a "what to show live / concept that lands" table per milestone, common errors to anticipate, suggested timing (~130 min: Setup 10' · M1 25' · M2 35' · M3 20' · M4 30' · Close 10'), and a closing hook: *"You just automated a report that was going to eat your Monday mornings. What other recurring task could you delegate to your own Atlas?"*

## Inconsistencies / open questions
- **ShareDuo — the brief contradicts the solution.** `mission.md` (M4 setup) says to **register ShareDuo as an MCP connector** (Settings → Connectors → Add MCP) — "the service that gives the dashboard a public URL." But `mission-claud- res.md` (Step 4.1) explicitly **corrects this**: "Good news: nothing to install or register. ShareDuo is NOT an external MCP connector — it's Cowork's built-in sharing via `update_artifact_settings(share='duo')`." → The **solution is authoritative**; the brief's framing is the earlier/looser version. The Editor should use the built-in-sharing framing and can surface the discrepancy as a "common confusion" beat.
- **Email recipient differs across files.** Cowork solution uses `superboss@gmail.com` (a stand-in); Codex solution uses `pveiga@gmail.com` (the real user). The brief says the email is sent to yourself "as if you were the team recipient." Minor — pick one consistently in the Talk.
- **`-new` suffix only in the Cowork solution.** The Cowork `reporte-semanal` saves with a `-new` suffix to avoid overwriting the example; the brief and Codex versions describe saving as `reporte-semana-AAAA-MM-DD.md` directly. Workshop-logistics detail, not a conceptual conflict.
- **Skills "ya armadas" / pre-built skills folder.** The Cowork solution mentions the mission "includes three pre-built skills in a `skills/` folder (`reporte-semanal/`, `buscar-accion/`, `publicar-tablero/`) as reference / 'correct answer.'" **That `skills/` folder is NOT present in this ZIP** — only the `reportes/` sample data and the docs are here. If the workshop relies on shipping those skills, they're missing from this export. (Flag for the presenter.)
- **Cowork-vs-Codex files are point-in-time** and self-flag rapid feature churn — re-verify Codex specifics before presenting.
- **Scope note:** the comparison file `cowork-vs-codex-comparacion.md` references a `final.md` deck whose concepts it compares — that deck is the `agentic-ai-deck.zip` source (the 73-slide skeleton), not included in this ZIP.

## Images / diagrams

### `mision - auto.zip/images/mockup-tablero.png`
- Provenance: bundled in the ZIP as `mockup-tablero.png` (rendered from the sibling `mockup-tablero.html`). Referenced in `mission.md` as the boss's napkin sketch of the dashboard and in both solution files (M4) as the design spec the `publicar-tablero` Skill must reproduce. PNG, 1565×1016. This is THE dashboard design reference and the visual hook of the whole mission. (The HTML source of this wireframe is transcribed verbatim in the excerpts below — so its structure is captured even before Phase 2.)
- Depiction:
- Why it matters:
- Transcribed text:
<!-- pending: process_images -->

## Raw / preserved excerpts

### The situation / the napkin (mission.md, opening)
> Lunes, 8:55 de la mañana. Reunión de equipo a las 9:00.
> Tu jefe te mira y dice: *"Necesito que sigas estas tres empresas: **Apple, Microsoft y Nvidia**. Un pulso semanal — qué se movió, qué noticias salieron, qué hay que vigilar. Y lo quiero **de dos formas**: un **email en mi inbox, una vez por semana**, y una **página web siempre actualizada** con un resumen, que yo pueda abrir cuando quiera. Algo así…"*
> …
> A menos que delegues. En esta misión vas a **contratar a Atlas**: un analista virtual que investiga las empresas del equipo, arma el reporte mientras vos dormís, lo deja en el correo del equipo y lo publica en un tablero que tu jefe puede abrir cuando quiera. Lo entrenás una vez. A partir de ahí, trabaja solo.
> Pero el verdadero premio no es Atlas: **sos vos, dominando Claude Cowork.**

### For whom / zero barrier (mission.md)
> Para cualquiera que tenga que **entregar trabajo recurrente**, aunque jamás haya programado nada. Acá no se programa: se **guía a Claude con técnicas de prompting** y se **combinan las piezas de Cowork** (Projects, Skills, Connectors, Schedule, Artifacts). Si sabés mandar un email y mover una carpeta, ya tenés todo lo que hace falta. La barrera de entrada es cero. El techo es altísimo.

### The rules of the game (mission.md)
> - **Conversá, no programes.** Todo se consigue describiéndole a Claude lo que querés. ¿No salió? Reformulá y volvé a tirar.
> - **Respetá el orden.** Cada milestone se para sobre el anterior. Saltearte uno es construir un piso sin cimientos.
> - **Verificá antes de avanzar.** Tocá el criterio de éxito con la mano antes de pasar de milestone.
> - **Cuando te trabes, preguntale a Atlas.** Cowork también sabe explicarse a sí mismo — usalo como copiloto.
> - **Tomá nota mientras avanzás.**

### Project Instructions — the exact text to paste (mission-claud- res.md, Step 1.1)
> *"Sos **Atlas**, el analista de mercado de un equipo de trabajo. Preparás un pulso semanal para colegas no técnicos (incluido el jefe del área), que se lee en 2 minutos antes de la reunión de los lunes.*
> *Seguís estas empresas que el equipo vigila: `[EMPRESAS]`.*
> *Escribís en español, claro y breve, sin jerga financiera complicada. Si usás un término técnico, lo explicás en una línea.*
> *Tus reportes son informativos y para uso interno: NO son recomendaciones de inversión ni asesoramiento financiero. Siempre incluís esa aclaración al final.*
> *Para armar cada reporte partís de las notas en crudo de la carpeta `fuentes/` de la semana (y, más adelante, de lo que vos mismo busques). Si un dato no está, lo decís en lugar de inventarlo.*
> *Guardás cada reporte como Markdown con el nombre `reporte-semana-AAAA-MM-DD.md`, junto a la carpeta `fuentes/` de esa semana."*

### Why a Project matters (mission-claud- res.md, Step 1.1)
> el Proyecto le da a Atlas una **carpeta propia**, **memoria** dentro del proyecto y un **lugar fijo** para sus tareas. Las **Instrucciones** son su "contrato de trabajo": valen para todo lo que hagas dentro del proyecto, sin repetirlas una y otra vez.

### Skill `reporte-semanal` — the exact /skill-creator prompt (mission-claud- res.md, Step 1.2)
> *"Quiero crear una Skill llamada `reporte-semanal`. Su entrada es la carpeta `fuentes/` de una semana, que tiene **varios archivos en crudo, uno por portal** (la info de una misma empresa puede estar repartida entre varios). Debe leerlos TODOS, consolidar por empresa y generar un archivo Markdown con esta estructura exacta:*
> *1. **Título:** «Pulso semanal de mercado — [fecha]».*
> *2. **Resumen ejecutivo:** 3 a 4 líneas en lenguaje simple sobre la semana.*
> *3. **Una sección por empresa**: nombre y ticker; precio aprox. de cierre y variación de la semana; 2-3 noticias con una línea de contexto; «Ánimo» (Positivo/Neutral/Negativo) con media línea; «A vigilar» (1 cosa).*
> *4. **Tabla resumen:** una fila por empresa con ticker, variación % y ánimo.*
> *5. **Fuentes principales:** 3-4 de los links que venían en los archivos de `fuentes/`.*
> *6. **Aclaración legal:** «Reporte interno e informativo; no constituye asesoramiento financiero».*
> *La empresa más relevante de la semana va primera (marcada con ⭐). No inventes datos: si falta algo, decílo. Precios = aproximados; conservá los links reales. **Guardá el resultado con el sufijo `-new`** … (ej. `reporte-semana-2026-05-25-new.md`)."*

### Connecting MT Newswires — the teaching beat (mission-claud- res.md, Step 2.1)
> ⭐ **Lo mejor:** **MT Newswires ya tiene un connector listo en Cowork** — aparece en el directorio de Connectors. No hay que crear ni configurar nada raro: lo buscás y lo conectás, como cualquier otra app.
> …
> **no estás programando ni creando nada.** Te **conectás** a un servicio que ya existe —como cuando conectás Gmail— y Atlas pasa a usar sus datos.

### Skill `buscar-accion` — the exact /skill-creator prompt (mission-claud- res.md, Step 2.2)
> *"Quiero crear una Skill llamada `buscar-accion`. Recibe un **ticker** (ej. AAPL) y una **semana** (fecha del lunes, ej. 2026-06-01). Busca info en DOS fuentes: (1) **Yahoo Finance** —precio de cierre aprox. del viernes y variación semanal— accediendo directamente con `web_fetch` a `https://finance.yahoo.com/quote/<TICKER>/`; y (2) **MT Newswires** para noticias, vía el connector conectado. Guarda en disco, dentro de `reportes/semana-AAAA-MM-DD/fuentes/`, **dos archivos acumulativos** (uno por fuente): `yahoo-finance.txt` con un bloque `-- TICKER --` por empresa, y `mt-newswires.txt` con una sección `=== TICKER ===` por empresa. Si el archivo ya existe (tiene datos de otro ticker), agrega el bloque al final sin pisar lo anterior. De MT Newswires solo guarda artículos donde el ticker es el foco principal. No inventa datos: si algo no está disponible, escribe 'n/d'. Conserva los links reales y marca los precios como aproximados."*

### Gmail draft prompt (mission-claud- res.md, Step 3.2)
> *"Atlas, tomá el último reporte semanal de la carpeta y dejalo como **borrador en Gmail** dirigido a `superboss@gmail.com`, con el asunto «Pulso semanal de mercado — [fecha]». Poné el resumen ejecutivo y la tabla en el cuerpo del correo, en un formato prolijo, listo para que el equipo lo lea con un clic."*

### Why draft, not direct send (mission-claud- res.md, Step 3.2)
> guardar como borrador (en lugar de enviar de una) te da control de revisión. Antes de que el correo llegue a tu jefe, pasás un ojo rápido. En producción podés cambiar esto y pedir que lo envíe directamente — pero el borrador es la práctica más segura para empezar.

### Schedule prompt + the caveat (mission-claud- res.md, Step 3.3)
> *"Cada lunes a las 8:00: con la Skill `buscar-accion` buscá la info de la semana de `[EMPRESAS]` y guardá las fuentes; después con la Skill `reporte-semanal` armá el reporte, guardalo en la carpeta del proyecto; y por último dejá el reporte como **borrador en Gmail** dirigido a `superboss@gmail.com` con el asunto «Pulso semanal de mercado — [fecha]»."*
> ⚠️ **Recordá:** las tareas programadas solo corren **con la computadora encendida y la app de Claude abierta**. Si estaba apagada, Cowork corre la tarea apenas la encendés y te avisa.

### ShareDuo correction (mission-claud- res.md, Step 4.1)
> 💡 **Buena noticia: no hay nada que instalar ni registrar.** ShareDuo **no es un conector MCP externo**: es el sistema de sharing **integrado en Cowork** que se activa con una llamada a `update_artifact_settings` con `share="duo"`. La Skill lo hace sola. Vos no tocás nada de Settings para esto.

### Skill `publicar-tablero` — what it does, 4 steps (mission-claud- res.md, Step 4.2)
> | Paso | Qué hace | Herramienta |
> | 1 | Lee el último `reporte-semana-*.md` y determina la `FECHA` de la semana | Carpeta del proyecto |
> | 2 | Genera el HTML del tablero (tarjetas + tabla + resumen) y lo guarda como `tablero-FECHA.html` | Archivo local en outputs |
> | 3 | Crea el Live Artifact `pulso-semanal-FECHA` en Cowork (o lo actualiza si ya existe) | `mcp__cowork__create_artifact` / `update_artifact` |
> | 4 | Activa el ShareDuo y confirma el link público | `mcp__cowork__update_artifact_settings` con `share="duo"` |
>
> 📌 **Un artifact por semana:** … la Skill crea un **artifact nuevo por semana** (ej. `pulso-semanal-2026-06-01`, `pulso-semanal-2026-06-08`), no actualiza siempre el mismo. Así queda un **historial de tableros** accesible en Cowork.

### The closing hook (mission-claud- res.md, facilitator guide)
> **Gancho de cierre:** *"Acaban de automatizar un reporte que les iba a comer la mañana de cada lunes. ¿Qué otra tarea recurrente de su trabajo podrían delegarle a su propio Atlas?"*

### Common errors to anticipate (mission-claud- res.md, facilitator guide) — verbatim
> - Olvidarse de habilitar la **búsqueda web** → Atlas no puede complementar con Yahoo Finance en el Milestone 2.
> - **MT Newswires** sin conectar → `buscar-accion` no tiene noticias; avisará pero seguirá solo con Yahoo.
> - Confundir los archivos de fuentes: `buscar-accion` genera **`.txt`**, no `.md`.
> - Olvidar el **sufijo `-new`** del reporte: `reporte-semanal` nunca pisa el original.
> - Cerrar la app y esperar que la tarea programada corra igual → no corre; necesita la app abierta.
> - Esperar que el tablero se refresque solo leyendo el disco → no puede; lo actualiza la Skill `publicar-tablero` (idealmente desde el schedule).
> - **Buscar "ShareDuo" en Connectors** para registrarlo → no hace falta; el sharing ya está integrado en Cowork vía `update_artifact_settings`.

### Official Cowork docs cited (mission-claud- res.md)
> - Get started with Claude Cowork — https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
> - Organize your tasks with projects in Cowork — https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-cowork
> - Schedule recurring tasks in Claude Cowork — https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork
> - How to create custom skills — https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
> - Use connectors to extend Claude's capabilities — https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
> - Browse skills, connectors, and plugins in one directory — https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory
> - Use live artifacts in Claude Cowork — https://support.claude.com/en/articles/14729249-use-live-artifacts-in-claude-cowork

### Cowork vs Codex — the verdict (cowork-vs-codex.md)
> el mapeo es ~10/13 conceptos directos o cercanos. Codex puede resolver la misma misión de punta a punta … pero pide más setup por archivo/terminal y pierde la magia del tablero vivo de un clic. Para un perfil no técnico, Cowork es más liso; para quien quiere un artefacto desplegable y control por archivos, Codex es más potente.

### Cowork vs Codex — the four differences to name (cowork-vs-codex.md)
> 1. **Público y superficie.** Cowork es una app para no-técnicos (todo botones y prompts). Codex es un agente de **programación** que vive en app/IDE/CLI…
> 2. **Skills:** el mapeo más limpio — mismo estándar `SKILL.md`, mismo creador asistido.
> 3. **Connectors → MCP:** mismo concepto, distinta plomería.
> 4. **Live Artifacts → (sin equivalente directo):** la brecha grande.

### Cowork vs Codex — architecture framing (cowork-vs-codex-comparacion.md)
> - **Claude Cowork:** corre **solo local**, sobre los archivos reales de la carpeta que le concediste en tu computadora. GUI, sin terminal.
> - **OpenAI Codex:** es **híbrido**, unificado por tu cuenta de ChatGPT — corre **local** … **o en la nube** … Nació como herramienta de devs y está pivoteando hacia knowledge workers (≈5M usuarios semanales; ~20% no-devs).
> - "Artifacts" significa cosas distintas en cada producto: en Claude son apps web vivas e interactivas; en Codex es un visor de previsualización de archivos generados.

### Sample report — week 2026-06-01 (full, representative output)
> # 📊 Pulso semanal de mercado — 1 de junio de 2026
> ## Resumen ejecutivo
> Cierre de mayo con rotación. **Apple** fue la estrella: a días del WWDC, la acción siguió subiendo… **Nvidia** corrigió tras el salto por sus resultados récord… **Microsoft** sumó un dato que gustó: su IA ya factura a un ritmo de US$ 37.000 millones al año.
> ## 🍎 Apple — AAPL · Cierre aprox. US$ 315 · Semana +5,0% 🟢 ⭐ · Ánimo Positivo · A vigilar: que el WWDC esté a la altura.
> ## 🪟 Microsoft — MSFT · US$ 452 · +0,4% 🟢 · IA ~US$ 37.000 M/año; Azure +31% · Ánimo Positivo.
> ## 🎮 Nvidia — NVDA · US$ 214 · −7,8% 🔴 · Toma de ganancias tras tocar ~US$ 236 · Ánimo Neutral (corrección sana).
> | Apple | AAPL | +5,0% | Positivo | · | Microsoft | MSFT | +0,4% | Positivo | · | Nvidia | NVDA | −7,8% | Neutral |
> Fuentes: CoinCentral · Motley Fool · FX Leaders. *Reporte interno e informativo; no constituye asesoramiento financiero.*

### Sample raw `fuentes/` note — intern's style (reportes/semana-2026-06-01/fuentes/yahoo-finance.txt)
> FUENTE: Yahoo Finance  |  SEMANA DEL 25 AL 29 DE MAYO 2026
> (cotizaciones copiadas de finance.yahoo.com) *** precios aprox, confirmar ***
> -- Cotizaciones al viernes (cierre aprox) --  cierre de mayo
> AAPL  ~ 315   (+5,0% en la semana)   https://finance.yahoo.com/quote/AAPL/
> MSFT  ~ 452   (+0,4%)                https://finance.yahoo.com/quote/MSFT/
> NVDA  ~ 214   (-7,8%)                https://finance.yahoo.com/quote/NVDA/
> -- Nota / Apple (AAPL) --  *** la mejor de la semana ***
> "Apple's WWDC 2026 'Key Catalyst' for AAPL stock" (Morgan Stanley)
> => a pocos dias del WWDC (8 de junio) no para de subir. cerca de records.

### The dashboard wireframe — structure (mockup-tablero.html, verbatim header + layout)
> <!-- MOCKUP (BOCETO A MANO / WIREFRAME) — Tablero "Pulso semanal de mercado". Idea de diseño para la Skill publicar-tablero. NO es el producto final: es un sketch para mostrar QUÉ queremos. Simplificado a 3 empresas (AAPL, MSFT, NVDA). -->
> Layout (top to bottom): hand-drawn header "📊 Pulso semanal de mercado" + "◍ LIVE" pill + "BOCETO" stamp; sub-note "título + fecha ('actualizado: lun 1 jun') · chip 'LIVE'"; a boxed **Resumen ejecutivo** (2–3 lines, simple language); a row label "una TARJETA por empresa (solo 3) — ticker, precio, ▲/▼ %, ánimo y 2 noticias"; a 3-column **grid of cards** (AAPL US$315 +5,0% ▲ Positivo; MSFT US$452 +0,4% ▲ Positivo; NVDA US$214 −7,8% ▼ Neutral), each card with ticker badge, name, price, % change (green up / red down), mood pill, 2 news bullets with [link], and "⌖ a vigilar"; a margin note "verde = subió · rojo = bajó · mismo diseño todas las semanas, solo cambian los datos"; a **tabla resumen** (Ticker · Empresa · Precio · Semana · Ánimo); footer "Reporte interno e informativo; no es asesoramiento financiero · fuentes: Yahoo Finance + MT Newswires". Hand-drawn aesthetic: Comic Sans / cursive font, dashed borders, slight rotations, grid-paper background.

### Codex equivalence master table (mission-codex-res.md) — for the "vs alternative" angle
> | Cowork (Claude) | Codex (OpenAI) |
> | Project | Project in the Codex app (+ folder/repo on disk) |
> | Instructions | `AGENTS.md` |
> | Skills (`SKILL.md`) | Skills (`SKILL.md`, same standard) |
> | `/skill-creator` | `$skill-creator` |
> | Connectors (MT Newswires, Gmail) | MCP servers (`config.toml` / `codex mcp`) |
> | Web search | Web search tool (`web_search = "live"` / `--search`) |
> | Claude in Chrome | In-app browser / Chrome extension / Computer Use |
> | Schedule | Automations (cron, Triage inbox) |
> | Live Artifacts | **No direct equivalent** → regenerated HTML + in-app browser (+ Codex Sites) |
> | Project memory | Memories + AGENTS.md |
