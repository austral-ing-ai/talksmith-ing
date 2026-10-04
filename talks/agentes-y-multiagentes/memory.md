# memory.md — agentes-y-multiagentes

**Current step:** 8 — Learnings awaiting_presenter
**Awaiting:** 2026-10-04 17:35 — "¿Qué candidatos promovés (C1–C5)? · ¿Limpio el backlog? · ¿Promovés la clase a la biblioteca compartida?"
**Topic:** Agentes y multiagentes: definición formal de agente, tools, tipos de agentes (ReAct) y arquitecturas multiagente
**Folder:** talks/agentes-y-multiagentes/
**Started:** 2026-10-04

---

## Talk briefing

Quiero crear una nueva presentacion sobre agentes.

El scope es hablar sobre agentes y multi-agentes. Definicion formal de un agente, cubrilr https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture, no vamos a meternos en MCP sino tocar la idea que los agentes tienen tools, y los distintos tipos de https://medium.com/@datadivaai/building-a-react-langgraph-agent-the-future-of-reasoning-centric-ai-workflows-bf270cc756fa

---

## 2026-10-04 — Step 1 (Frame)
- Status: complete
- Asks log:
  - 2026-10-04 10:55 — "¿De qué trata esta clase?" → see Talk briefing (verbatim)
  - 2026-10-04 10:58 — "Una frase quedó cortada: 'y los distintos tipos de…' — ¿tipos de agentes por patrón de razonamiento / tipos de tools / ambos / otra?" → not answered (carried as open question)
  - 2026-10-04 10:58 — "Nombre de la carpeta" → agentes-y-multiagentes
- What was decided: New Talk on agents and multi-agent systems; folder `agentes-y-multiagentes`. Scope: formal definition of an agent; agents use tools (concept only, no MCP); types of agents per the ReAct/LangGraph article; multi-agent architectures per the LangChain blog post.
- Key inputs: Two seed URLs (LangChain multi-agent architectures blog; Medium ReAct LangGraph agent article). Profile defaults apply (AI Gen, Austral, español, 90 min).
- Files created/modified: talks/agentes-y-multiagentes/ tree (memory.md, research/{articles,llm-chats,web,corpus}/, images/, output/)
- Pending open questions: Truncated briefing phrase "los distintos tipos de…" — likely types of agents by reasoning pattern (ReAct, Plan-and-Execute, …); confirm with presenter.

## 2026-10-04 — Step 2 (Collect)
- Status: complete
- Asks log:
  - 2026-10-04 11:05 — "¿Agregás más fuentes, exploramos en vivo, o pasamos al corpus?" → (superseded by 11:08 ask)
  - 2026-10-04 11:08 — "¿Capturo las sugeridas / algunas / sumás las tuyas / pasamos al corpus?" → "Como corpues: Toma la URL de langchain que te pase. Busca tambien lo que seiendas que es relevante para lo que te mencione del scope. Toma ~/Download/AIG4B-Clase-6-Agent.pptx y tambien /Users/pveiga/Documents/Austral/talksmith-mim/talks/orquestacion-de-agentes contiene conceptos que quiero cubrir. No lo vamos a mostrar en el scope de Papercliping per se introduce informacion relevante."
  - 2026-10-04 11:12 — "macOS bloquea ~/Downloads y talksmith-mim — ¿podés copiarlos a research/articles/?" → "El pptx esta en agentes-y-multiagentes" (pptx copied to Talk root; moved to research/articles/ — 44 slides, Módulo 6: Agents of the biomedicina course; covers AIMA definition, ReAct, multi-agent, MCP, memory). orquestacion-de-agentes not yet copied.
  - 2026-10-04 11:21 — "¿Copiás orquestacion-de-agentes o seguimos sin ella?" → "Y copie tambien el resto de los articulos" (copied whole talk folder into research/articles/orquestacion-de-agentes/, 52 MB). Orchestrator kept final.md → research/articles/orquestacion-de-agentes-clase.md and the 3 non-Paperclip web captures (cognition-dont-build-multi-agents, koreai-orchestration-patterns, aienterprise-run-company-agents) → research/web/; set aside the 13 Paperclip-product captures, Atlas/blog/misión case files, renders and scaffolding (original remains in talksmith-mim; anthropic-multi-agent-research duplicates our own capture).
  - 2026-10-04 11:05 — "'los distintos tipos de…' — ¿patrones de razonamiento / tools / ambos?" (re-asked) → "distintos tipo de agentes (eg: ReAct)" — i.e. agent types by reasoning pattern
- What was decided: Collection closed with 14 sources (4 articles + 10 web captures). Paperclip product material excluded from the corpus; its concepts arrive via the prior talk's final.md. MCP and agent memory (present in the pptx) are out of scope per briefing.
- Key inputs: Presenter: LangChain URL, Medium URL, AIG4B-Clase-6-Agent.pptx (Módulo 6: Agents, biomedicina course), orquestacion-de-agentes talk (talksmith-mim). Agent-sourced per "busca lo relevante": Anthropic ×3, LangChain planning agents, Lilian Weng, ReAct + Reflexion papers.
- Files created/modified: research/articles/orquestacion-de-agentes-clase.md; research/web/{cognition-dont-build-multi-agents, koreai-orchestration-patterns, aienterprise-run-company-agents}/ (copied from orquestacion-de-agentes); research/web/{anthropic-building-effective-agents, anthropic-multi-agent-research-system, anthropic-writing-tools-for-agents, langchain-planning-agents, lilianweng-llm-powered-agents}/ (agent-sourced per presenter's "busca lo relevante"); research/articles/{yao-2022-react.pdf, shinn-2023-reflexion.pdf} (arXiv); research/articles/AIG4B-Clase-6-Agent.pptx (presenter); research/web/langchain-multi-agent-architectures/ (ingest, 16 images); research/web/medium-react-langgraph-agent/ (ingest via freedium-mirror.cfd after medium.com 403; canonical_url appended to metadata.yaml)
- Pending open questions: none. Note for drafting: orquestacion-de-agentes covers Paperclip — Paperclip itself is OUT of scope for slides, but the concepts it introduces are in scope.

## 2026-10-04 — Step 3 (Corpus)
- Status: complete
- Asks log:
  - 2026-10-04 11:45 — "¿Transcribo las imágenes? Solo figuras con contenido (~70) / todas (~185) / solo texto / más adelante" → "No las descrivamos, esrta bien." (text only; Phase 2 skipped — 185 stubs stay pending)
- What was decided: Phase 1 complete — 14/14 records, 0 unparseable, 0 skipped (4 parallel librarian batches).
- Files created/modified: research/corpus/{AIG4B-Clase-6-Agent.pptx, orquestacion-de-agentes-clase.md, yao-2022-react.pdf, shinn-2023-reflexion.pdf}.md; research/corpus/{anthropic-building-effective-agents, anthropic-multi-agent-research-system, anthropic-writing-tools-for-agents, lilianweng-llm-powered-agents, langchain-multi-agent-architectures, langchain-planning-agents, medium-react-langgraph-agent, cognition-dont-build-multi-agents, koreai-orchestration-patterns, aienterprise-run-company-agents}.web.md; companion images/ folders (234 image files, 185 pending stubs).
- Key inputs: Presenter declined image transcription (text-only corpus).
- Pending open questions: 185 image stubs remain `<!-- pending: process_images -->` by presenter choice; Phase 2 can be run later on request.
- Librarian notables (for drafting): pptx has no speaker notes; pptx slide 25 production stats unsourced [open]; pptx slides 32/33 likely derive from Anthropic/LangGraph uncredited [open]; LangChain multi-agent article's "40-50% calls saved" and "67% fewer tokens" don't match its own tables [verified]; Cognition (Jun 2025, single-thread) vs Anthropic/LangChain (multi-agent +90.2%) — candidate debate slide (the prior talk cut it; presenter's call); "90.2%" ambiguous relative vs pp [open]; building-effective-agents capture is a revised version (cite "2024, revisado"); ReAct formal definition (o_t, a_t, π(a_t|c_t), Â = A ∪ L) preserved; ReAct never says "tool" (presenter framing); Reflexion Actor=ReAct, three LLM roles bridge to multi-agent; Plan-and-Execute only from langchain-planning-agents; writing-tools post MCP-framed but principles general; Medium code has defects [verified]; date 2022–23 SOTA claims on slides.

## 2026-10-04 — Step 4 (Draft)
- Status: complete
- Mode: B — Agent Draft
- Asks log:
  - 2026-10-04 11:50 — "Nombre de la clase (class)" → presenter said "Movamos a creacion de la presentacion." without picking — orchestrator took recommended default: "Agentes y sistemas multiagente" (editable in Step 5)
  - 2026-10-04 11:50 — "Fecha (date)" → default taken: 2026-10-07 (next Wednesday, matching the course's Wednesday cadence)
  - 2026-10-04 11:50 — "Modo: A Entrevista / B Borrador del agente / C Tu esquema" → default taken: B (recommended)
  - 2026-10-04 12:00 — (unprompted) Presenter: "Tama que tenemos 2 h de clase." → per-Talk duration override: 120 minutos (profile default 90 untouched); relayed to the in-flight Editor draft
  - 2026-10-04 12:40 — "Draft ready — read draft.md, leave feedback bullets or reply in chat; signal ready to move to Review" → "Listo, pasalo a polish" (no feedback bullets in draft.md)
- What was decided: Mode B draft written (52 slides) → Composer scope=full (0 blockers, 10 majors, 8 minors) → all 10 majors applied by Editor (sections split: 1 Qué es un agente 10 · 2 Tools 6 · 3 ReAct 5 · 4 Otros cuatro tipos 11 · break · 5 Patrones multiagente 11 · 6 Cuándo repartir 6 · Conclusions 3; 52 slides, 14 ASCII, 4 corpus images; ~113 min + buffer). 8 minors deferred to Step 5 under draft.md # Open questions. Step 5.5 live view rendered (background): output/html/index.html, 59 slides (51 content), fresh vs draft.md; 51 classifier critics → 47 confirmed, 4 image-full stand-ins (3.2, 6.1, 6.6, C.2) pending Polish SVGs; advisory: 5.6–5.9 four consecutive content+cards+image (intended). Defects logged: BUG-20261004-02/03/04.
- Key inputs:
  - 2026-10-04 11:55 — Presenter scope note (verbatim): "Agrega como nota que vamos a cubir [tabla] en la presentacion. Uno a la vez." Tabla pegada:
    > Los principales, para comparar:
    >
    > | Tipo | Cómo funciona | Cuándo conviene |
    > |---|---|---|
    > | ReAct | Loop pensar → actuar → observar, un paso a la vez | Tareas exploratorias, donde el siguiente paso depende del resultado anterior |
    > | Plan-and-Execute | Planifica todo al inicio, luego ejecuta los pasos | Tareas largas y predecibles; menos llamadas al LLM |
    > | Reflexion | Ejecuta, se autoevalúa y reintenta con esa crítica como memoria | Cuando hay un criterio claro de éxito (tests, validaciones) |
    > | ReWOO | Planifica con variables y ejecuta las tools sin volver a razonar entre medio | Optimizar costo/latencia |
    > | Multi-agente (orquestador + workers) | | |
    Interpretation for drafting: the deck MUST cover these five agent types, one at a time (one slide/block per type, in this order), plus a comparison. Multi-agente row arrived without description — it is the bridge into the multi-agent section. Sources: ReAct → yao-2022-react.pdf.md + medium-react-langgraph-agent; Plan-and-Execute + ReWOO → langchain-planning-agents; Reflexion → shinn-2023-reflexion.pdf.md; orquestador + workers → anthropic-building-effective-agents + anthropic-multi-agent-research-system + langchain-multi-agent-architectures.
- Files created/modified:
  - talks/agentes-y-multiagentes/draft.md (created, Mode B end-to-end draft: Thesis, Agenda, 4 sections + Conclusions = 52 slides, 13 ASCII diagrams, 4 corpus images; duration 120 min per presenter override; numeric correction applied on 4.11 — LangChain prose "40-50%" / "67% fewer tokens" replaced by its own table values 37,5% (8→5) and 40% (1 − 9K/15K))
  - talks/agentes-y-multiagentes/draft.md (modified, Composer scope=full majors applied — 10/10; 0 blockers): 6 sections + Conclusions = 52 slides (10/6/5/11/11/6 + 3), 14 ASCII, 4 corpus images. Old S3 split into "3. ReAct" + "4. Otros cuatro tipos de agente"; old S4 split into "5. Patrones multiagente" + "6. Cuándo repartir"; old 1.6 "Tipos de ambiente" cut (multi-agent dimension → 1.5 notes); memory bullet/title removed from 1.9; new 4.2 Plan-and-Execute example (editor-built on the 3.3 HotpotQA question, marked as such); 4.9 workflow-vs-multiagent line + notes re-attributed to pptx slide 33; fan-out/Claude Research duplicates removed (5.3, 5.6, 6.3); 6.1 Kore.ai table → notes; 2.5 principle-first cards; benchmark descriptors (HotpotQA 3.3, ALFWorld 3.5, HumanEval/pass@1 4.6, BrowseComp 6.2); 6.6 ASCII flow (steps → notes); running times + 10-min break after 4.11 (min 65–75) + ~7-min buffer. No figures changed. 8 Composer [minor] items deferred to Step 5, listed under `# Open questions`; moved/cut text logged under `# Cut material`.
- Pending open questions: draft.md # Open questions (editor-logged items + 8 deferred Composer minors) — presenter moved on without resolving; Step 6 rescue-open handles any [open] feedback (none).

## 2026-10-04 — Step 5 (Review)
- Status: complete
- Asks log:
  - 2026-10-04 12:55 — (folded into Step 4 handoff) → "Listo, pasalo a polish"
- What was decided: Zero feedback rounds — presenter approved the draft as-is after viewing the live HTML view. draft.md frozen.
- Key inputs: Live view (output/html/index.html) fresh vs draft.md at approval (model_freshness rendered → exit 0).
- Files created/modified: none
- Pending open questions: none new

## 2026-10-04 — Step 6 (Polish)
- Status: complete
- Asks log:
- What was decided: final.md produced from draft.md (verbatim copy, draft.md untouched). 14/14 ASCII diagrams rendered to SVG + PNG by the Diagram-Illustrator — 10 clean on first pass, 3 after one revision, 1 critic-unresolved (s4-1-1 "tools") accepted because "tools" is the deck's term of art. Orchestrator hand-edited the s1-6-1 SVG text "lazo sigue" → "loop sigue" to match the slide prose/ASCII and re-rasterized the PNG (1002px). polish-ascii cleanup rewrote all 14 fences to image refs (+ ascii-source echoes). No generate-image directives (polish-images skipped). Image consolidation: the 4 LangChain corpus images on 5.6–5.9 copied into images/ and refs rewritten; the 14 diagram refs rewritten .svg → .png (Keynote-safe; SVGs kept on disk as source). All 18 image refs resolve to images/*.png, no forbidden extensions, no remote refs. rescue-open: 0 [open] bullets. strip_feedback removed 60 Presenter-feedback blocks (52 H3 + 8 paragraph). No anti-slop pass (by contract).
- Key inputs: plan.annotated.json from the Diagram-Illustrator (14 blocks, line numbers matching final.md); research/corpus/langchain-multi-agent-architectures.web/images/ (4 PNGs).
- Files created/modified: final.md (cp draft.md, then fences → image refs, image refs consolidated, Presenter feedback stripped); images/{s1-2-1-lazo-agente-ambiente, s1-6-1-lazo-formalizado, s1-7-1-bifurcacion-pensar-actuar, s2-1-1-llm-pide-programa-ejecuta, s3-2-1-lazo-react, s4-1-1-plan-and-execute, s4-4-1-lazo-reflexion, s4-7-1-tuberia-rewoo, s4-9-1-orquestador-workers, s5-3-1-subagentes-ventana-propia, s6-1-1-supervisor-vs-red, s6-4-1-contexto-no-compartido, s6-6-1-caso-descomposicion, sc-2-1-arbol-decision}.{ascii,svg,png}; images/{69cbaa03649e3ebd9d135314_image--9--1, 69cbaa0feea3104c341d0d4f_image--10, 69cbaa10eea3104c341d0d5e_image--11, 69cbaa10eea3104c341d0d5b_image--12}.png (copied from corpus).
- Pending open questions: final.md # Open questions carries 22 items inherited from draft.md (editor-logged items + 8 deferred Composer minors), none added in Polish; s4-1-1 diagram has one critic note left unresolved ("tools" wording), accepted.

## 2026-10-04 — Step 7 (Render)
- Status: complete
- Asks log:
  - 2026-10-04 13:20 — "¿Qué produzco? HTML / HTML+PDF / HTML+PowerPoint / los tres · ¿Qué estilo?" → "default" (style default; formats not named → default HTML only)
- What was decided: HTML deck rendered from final.md, style default, no exports. 59 slides (51 content + 6 section openers + divider + closing) + cover; 51 classifier critics → 50 confirmed, 1 weak trace fixed; 3.2/6.1/6.6/C.2 now image-full; all coverage audits clean; advisory 5.6–5.9 run of content+cards+image kept (deliberate series).
- Key inputs: Presenter: "default".
- Files created/modified: output/slide-model.json, output/html/index.html, repo-root index.html (landing). Also (presenter request, outside workflow): samples/react-langgraph/{react_agent.py, README.md, requirements.txt}.
- Pending open questions: for presenter review — deck slides 50 (6.1) and 55 (6.6): Kore.ai citation sits in the line under the title (image-full has no source slot, BUG-20261004-08); slide 32 (4.7 ReWOO) lead ~137 chars keeps it text+image (trim <120 → image-full); slide 39 (5.2 quiz) title == question text. Defects logged: BUG-20261004-08/09.

## 2026-10-04 — Step 8 (Learnings)
- Status: awaiting_presenter
- Asks log:
  - 2026-10-04 17:35 — "Candidatos ≥3×: C1 barrido terminológico (7) · C2 dibujar lo que tiene forma (9) · C3 una lámina una idea (6) · C4 fuente con link (3) · C5 diagrama no se repite en texto (3) — Promover / Saltear / Promover con cambios" → pending
  - 2026-10-04 17:35 — "¿Limpio el backlog (mover filas ya promovidas de L1–L10 a processed)?" → pending
  - 2026-10-04 17:35 — "¿Promover esta clase a la biblioteca compartida?" → pending
- What was decided:
- Key inputs: This Talk produced 0 presenter-feedback bullets (approved draft as-is) — no new backlog rows.
- Files created/modified:
- Pending open questions:
