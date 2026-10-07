# Atlas — Functional Setup

Company `f820a4ff` in Paperclip. Functional overview (what it does, who does what, how work flows).

## What Atlas is

Atlas is a company that **sells oil-well drilling supplies** (*insumos de perforación de pozos petroleros*). It operates in Spanish, focused on Argentina's oil & gas sector — specifically the **Vaca Muerta** basin. It runs as an authenticated, board-governed workspace (issue prefix **ACMA**, new agents require board approval).

Its current operating goal is **organic brand positioning through technical content**: rank Atlas as a technical reference for the searches that oilfield buyers (drilling engineers, procurement, operators) actually make, and convert that into qualified organic traffic.

## Who's in it

### Humans

| Person | Role in Atlas | Function |
|---|---|---|
| **Austral Admin** (`austral-admin@example.com`) | Owner | The only human. Instance admin / board owner — creates the org and agents, and is the sign-off gate: approves/rejects every blog brief, draft, and publish request. |

### Agents (all AI, DeepSeek-backed)

The agent org reports up to a CEO agent, who fans out to functional leaders:

```
CEO  (strategy / top of agent chain)
├── CMO — Chief Marketing Officer
│     └── Blog Content Manager
├── CLO — Chief Legal Officer
├── Director of Institutional Relations   (active)
└── Relacionista Institucional            (terminated — superseded by the Director role)
```

| Agent | Function |
|---|---|
| **CEO** | Sets direction; spins up new functional agents (e.g. commissioned the lobby/institutional-relations role). |
| **CMO** | Owns end-to-end marketing: audience, positioning, editorial direction, channel mix, growth targets, competitive analysis. **Delegates production** — does not write. |
| **Blog Content Manager** | Owns blog content strategy, creation, editorial calendar, and shipping posts live through the publishing pipeline. |
| **CLO** | Legal risk, contract review, regulatory compliance, corporate governance for the drilling-supply business. |
| **Director of Institutional Relations** | Government affairs in Argentina's oil & gas sector: regulatory monitoring, stakeholder engagement, institutional positioning with government bodies and industry associations. |
| **Relacionista Institucional** *(terminated)* | Earlier lobby/advocacy role (legislative research, advocacy strategy, stakeholder mapping, position papers) — replaced by the Director role above. |

## How work flows (the blog pipeline)

Marketing is the active production line. A request becomes **one ticket** that carries the work end-to-end through three human-approved gates:

1. **CMO** turns a request (e.g. *"blog about Vaca Muerta"*) into a delegation ticket and hands it to the **Blog Content Manager**.
2. Blog Content Manager produces two living documents on that ticket:
   - **Concept brief** → *gate 1* (the Owner approves).
   - **Full draft** → *gate 2* (the Owner approves).
3. **Final review & publish** → *gate 3*. The Owner's approval **is** the publish authorization; the post ships live and the ticket closes.

The ticket stays assigned to the Blog Content Manager the whole way; each human approval simply wakes it to the next phase.

## What it has actually produced

The two active projects are **Onboarding** and **"Aumentar el reconocimiento de marca"** (brand awareness via organic content). Delivered work (all closed) includes:

- Blogs on Vaca Muerta supply-chain transparency and the government-corruption angle
- Blogs on **IRAM / API / ISO certifications** in Argentina and certifications as an access key to Vaca Muerta
- A monthly **risk analysis** and a **Q3 editorial plan** prioritizing content off it
- Standing up the **Enterprise Lobby / institutional-relations** agent

---

**In short:** Atlas is a Spanish-language oilfield-supply company whose AI staff is organized like a real company — a CEO over marketing, legal, and government-affairs functions — with a human operator acting as the editorial approver on a gated content pipeline, currently focused on SEO-driven technical blogging for the Vaca Muerta market.
