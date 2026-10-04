---
source_file: orquestacion-de-agentes-clase.md
source_type: article
ingested_at: 2026-10-04
---

# Orquestación de Agentes — coordinación, Tasks y gobernanza (final.md de un Talk previo del presenter)

> **Librarian scope note (presenter instruction, per briefing).** This is the `final.md` of an earlier Talksmith Talk by the same presenter, built in another subject repo (MiM, IAE Business School). It centers on **Paperclip (paperclip.ing)** as the instrument. **Paperclip itself will NOT be shown in the current Talk** (*Agentes y multiagentes*, IA Generativa, Universidad Austral, 90 min). **The concepts it introduces ARE relevant and reusable:** subagents and their own context window; what a model's context is; orchestration as a definition and as a management decision; the three levels of agent management; orchestrator-worker / supervisor pattern; adaptive agent network; the supervisor-vs-network-vs-custom decision table; when to split work (read vs. write on shared state) and the token price of parallelizing; a worked decomposition case; and the Task as the unit that carries coordination, decision record and audit trail (governance/audit). Sections 4–6 (Paperclip controls, the layer below — Skills/Plugins/MCP, sandbox, self-hosting — and the Atlas mission) are Paperclip/MiM-specific; MCP is additionally out of the current Talk's scope. Everything is preserved verbatim in *Raw / preserved excerpts*.

## Provenance
- Original location: `research/articles/orquestacion-de-agentes-clase.md`
- Format: md (Talksmith `final.md`, 2773 lines; frontmatter + Thesis + Agenda + 6 sections + Conclusions + Open questions + Cut material)
- Author / source (if known): Paulo Veiga, Marco Sorondo y Claudio Righetti (frontmatter `presenter`). Presentation: "Agentes Inteligentes — Master in Management (MiM), IAE Business School, Universidad Austral". Class: "Orquestación de Agentes — coordinación, Tasks y gobernanza".
- Date of original (if known): delivery date in frontmatter "sábado 28 de noviembre de 2026" (2026-11-28 is a Saturday — checked). Internal edit log dates run 2026-08-24 → 2026-09-01.
- Audience of the original: business professionals/students with programming fundamentals (MiM); 2 hours; 45 slides.
- Cited sources inside it (as `corpus/<name>.web.md` of the *other* repo): Anthropic, "How we built our multi-agent research system" (jun-2025); Cognition, "Don't Build Multi-Agents" (jun-2025); Kore.ai, "Choosing the right orchestration pattern for multi-agent systems" (oct-2025, upd. jul-2026); The AI Enterprise / Mark R. Hinkle, "Run a company with AI agents (Paperclip)" (abr-2026); paperclip.ing product pages (ago-2026); GitHub paperclipai/paperclip README (reconstructed, unverified). Four of these have captures in **this** Talk too: `research/web/anthropic-multi-agent-research-system/`, `research/web/cognition-dont-build-multi-agents/`, `research/web/koreai-orchestration-patterns/`, `research/web/aienterprise-run-company-agents/` (note the name difference: the old deck cites `anthropic-multi-agent-research.web.md`; here the record is `anthropic-multi-agent-research-system.web.md`). The paperclip-*, github-paperclip-repo, mision-*, atlas-*, cmo-*, blog-content-manager-* records do not exist in this Talk.

## Key claims

**Thesis of the original Talk.** "Un equipo de agentes se vuelve gobernable cuando cada unidad de trabajo es una Task con dueño, estado y rastro; esa misma Task sostiene la coordinación, la decisión y la auditoría."

**Concepts relevant to the current Talk (reusable without Paperclip)**
- **Agente** (quiz 1.3, Anthropic jun-2025): "Un modelo de lenguaje que usa herramientas en un loop: decide, ejecuta una acción, mira el resultado y vuelve a decidir." Dos fronteras: frente al chat (que responde y termina) el agente cambia algo afuera; frente al script/programa fijo, el agente elige el paso siguiente según lo que encontró en el anterior. Costo: ~4× los tokens de un chat.
- **Subagente** (quiz 1.4 y lámina 2.1): "Un agente que otro agente crea para una parte del trabajo, con su propia ventana de contexto. Crearlo es una acción del agente principal en marcha, no una pieza que alguien configuró antes." Ventana propia = ve solo lo que el que lo abrió le pasa, y "nunca ve lo que está haciendo su hermano". Devuelve "hallazgos destilados, no su historial completo". Fan-out / fan-in. Una herramienta se ejecuta y devuelve; un subagente decide.
- **Contexto de un modelo** (quiz 1.5): "Todo lo que el modelo tiene a la vista en una sola corrida: instrucciones, archivos, lo que devolvieron las herramientas y la conversación hasta ahí." Es finito, se llena, se paga por token, y no es memoria (no persiste entre corridas): lo que tiene que persistir se escribe afuera.
- **Orquestar** (1.7): "decidir quién hace qué, en qué orden, con qué información y bajo qué límite de gasto." No es prompt engineering ("Escribir mejor la instrucción mejora una tarea. Orquestar mejora un equipo"). Kore.ai: "the challenge shifts from building AI agents to coordinating them effectively"; el patrón de orquestación "defines how agents interact, share context, and collaborate to complete complex tasks". Cuatro dimensiones que mueve la elección: costo en tokens, latencia, velocidad de desarrollo vs. control, escalabilidad/mantenimiento. Tesis: orquestar es management, no arquitectura.
- **Seis decisiones para armar una compañía** (1.6): misión y objetivos; diseño organizacional; flujo de trabajo; presupuesto; quién firma; qué queda escrito. "Orquestar es sostener las seis mientras el trabajo corre."
- **Tres niveles de gestión de agentes** (1.8, The AI Enterprise abr-2026): Nivel 1 agentes de tarea única (sin memoria del negocio ni rendición de cuentas; cada sesión arranca de cero); Nivel 2 agentes especializados en paralelo (comparten jerarquía de objetivos, no colaboran, coordinación manual); Nivel 3 orquestación jerárquica (agente CEO descompone la misión, asigna por organigrama, escala bloqueos al directorio humano; cada tarea remite a la misión). La mayoría de los profesionales está en el Nivel 1.
- **Cambio de modelo mental** (1.9): "You stop thinking 'I'm prompting an AI' and start thinking 'I'm managing a team.'" (Hinkle).
- **Orchestrator-worker** (2.2, Anthropic): "un agente principal planifica y despacha subagentes especializados que trabajan en paralelo, cada uno con su propia ventana de contexto." Opus 4 lead + Sonnet 4 subagents superó a Opus 4 single-agent por 90,2% en la eval interna de Anthropic (eval sin rúbrica ni conjunto públicos). El plan se guarda en `Memory` fuera del lead porque su ventana trunca a 200.000 tokens.
- **Compartir el contexto no alcanza** (2.3, Cognition): aun dándole a cada subagente todo el contexto del lead, ninguno ve el trabajo del hermano; "Actions carry implicit decisions, and conflicting decisions carry bad results" (ejemplo Flappy Bird).
- **Cuándo repartir** (2.4): si el trabajo **lee** (investigación, búsqueda) repartir paga; si **escribe sobre algo compartido** (código, un mismo documento, una base) → un solo hilo o límites explícitos entre escritores. Anthropic: "most coding tasks involve fewer truly parallelizable tasks than research, and LLM agents are not yet great at coordinating and delegating to other agents in real time." Variante: cada subagente escribe su salida a un archivo y devuelve una referencia liviana.
- **El precio de paralelizar** (2.5, Anthropic): ~15× tokens de un chat para multi-agente, ~4× para agente único; el uso de tokens solo explica el 80% de la varianza en BrowseComp (tres factores — tokens, llamadas a herramientas, elección de modelo — explican el 95%). "multi-agent systems require tasks where the value of the task is high enough to pay for the increased performance." Subir de Sonnet 3.7 a Sonnet 4 dio más mejora que duplicar el presupuesto de tokens.
- **Patrón supervisor** (2.6, Kore.ai): un orquestador central "receives the user request, decomposes it into subtasks, delegates work to specialized agents, monitors progress, validates outputs, and synthesizes a final unified response". Capacidades del orquestador: Reasoning, Planning, Routing, Reflection; los especialistas llevan Scope & Instructions, Knowledge, Tools. Flujo de datos de mínimo privilegio.
- **Red adaptativa** (2.7, Kore.ai): sin orquestador; "Cada agente decide si ejecuta, delega o enriquece la tarea antes de pasarla." Coordinación replicada en cada par; latencia baja; nadie tiene la foto completa; "quién manda ahora" es una posición móvil (Start Agent / Current Agent). Kore.ai lo desaconseja cuando trazabilidad y debugging son prioritarios.
- **Tabla de decisión** (2.8, Kore.ai): Supervisor / Red adaptativa / Custom por estructura de control, latencia, complejidad, uso de tokens, mejor para, madurez de equipo, mantenimiento. "El patrón supervisor es el barato de construir y el caro de operar." Regla de Kore.ai: "choose the simplest pattern that effectively meets your business requirements".
- **Caso de descomposición** (2.9, Kore.ai): "Pay off my car loan using my savings account." → 4 pasos, 3 especialistas (Loan Agent, Transaction Manager, Payment Processor), dos lecturas en paralelo y la escritura (transferencia) sola y al final; cada agente ve solo su parte del dato; validación antes de ejecutar; razonamiento y transacción registrados para auditoría.
- **Task** (3.1): "unidad de trabajo con dueño único, estado, hilo de conversación y definición de terminado." **La Task hace tres trabajos a la vez** (3.8): unidad de trabajo, registro de la decisión, rastro de auditoría. "Sin esa pieza hay agentes actuando. Con ella hay una organización que se puede inspeccionar y frenar."
- **Audit trail** (3.7): registro append-only de qué leyó cada agente, qué decidió, qué ejecutó, con qué costo y cuándo. Salvedad: en self-hosted sobre Postgres la inmutabilidad es política, no propiedad criptográfica.
- **Prueba de la orquestación** (3.9): ¿cómo se bloquea una acción antes de que ocurra? ¿cómo queda registrada? ¿cómo se detiene lo que ya corre? (más una cuarta — revertir — sin respuesta seria para acciones externas).
- **Conclusiones** (C.1): orquestar es decisión de management; el paralelismo depende del dominio; el precio se paga en tokens (~15×); la Task es la pieza de gobierno; el instrumento no toma la decisión. **Árbol de decisión** (C.2): ¿la tarea vale ~15× tokens? → ¿los agentes escriben sobre estado compartido? → ¿cada acción queda en una Task con dueño y rastro?
- Cierre: "Autonomy is a privilege you grant, not a default." (paperclip.ing).

**Paperclip-specific claims (instrument — NOT to be shown in current Talk; concepts may transfer)**
- Paperclip = "control plane" sobre agentes existentes, no framework (CrewAI es framework); MIT, self-hosted; v2026.817.0. Org chart con rol, título, línea de reporte, instrucciones persistentes por puesto. Heartbeats (wakes por evento o agendados; cadencia = decisión de presupuesto). Estado persistente en la Task entre heartbeats; watchdog. Budgets mensuales con tope por agente ("Top-ups are an approval, not a config edit"). Governance: approval gates, "Deny with a note", revisión de planes versionada. Skills / Plugins / MCP; sandbox; self-hosting (los prompts igual salen al proveedor del modelo). Misión "vigía regulatorio de Atlas" (MiM-specific).

## Definitions and terminology
- **Agente**, **subagente**, **ventana de contexto**, **fan-out / fan-in**, **orquestar**, **patrón de orquestación** (Kore.ai), **orchestrator-worker**, **supervisor**, **red adaptativa**, **custom**, **token** ("la unidad en la que el proveedor del modelo mide y factura el texto"), **eval** ("la prueba con la que un equipo mide a su propio sistema"), **Task** (= `ticket` en paperclip.ing = `Issue` en el newsletter), **definition of done**, **subtask / dependencias de bloqueo**, **mission / project goal / agent goal / task**, **trabajo huérfano**, **audit trail (append-only)**, **approval gate**, **empresa virtualizada de agentes** ("un conjunto de agentes donde cada uno tiene un puesto con instrucciones permanentes, un jefe, un presupuesto y un rastro de lo que hizo"), **control plane vs. framework**, **runtime** ("el programa que de verdad ejecuta al agente"), **adapter**, **heartbeat**, **watchdog**, **sandbox**, **self-hosting**, **blast radius / radio de daño**, **PII**, **seudonimizado** (vs. token de facturación). All defined verbatim in the raw excerpt.

## Evidence and examples
- Anthropic (jun-2025): +90,2% multi-agent vs single-agent (internal eval); 4× / 15× tokens; 80% / 95% variance in BrowseComp; S&P 500 IT board-members example; Sonnet 3.7 → Sonnet 4 beats doubling token budget. **Cross-checked in this Talk's capture** (see Inconsistencies).
- Cognition (jun-2025): Flappy Bird example (background vs. bird subagents produce inconsistent styles); "Almost Surely Unreliable" / "Still Unreliable" / "Simple & Reliable" verdicts; context-compression LLM "(but hard to get right)" (in Cut material).
- Kore.ai (oct-2025): supervisor and adaptive-network figures; decision table; car-loan payoff case; "more than 200%" token-variation claim flagged as unsupported.
- The AI Enterprise (abr-2026): three levels of agent management; content-marketing org chart (CEO/CMO/CTO, runtimes `claude_local`, `process`, `openclaw_gateway`, `codex_local`, heartbeat cadences); CrewAI "1.400 millones" automations (third-hand).
- Paperclip mock-ups: PAP-1041…1044 board; overnight activity timeline (02:10–07:00) where an agent QA-approves another agent's work; Budgets table (Atlas/CodexCoder/Vera/Scribe); approval card.
- Atlas mission (MiM course instance): 4 agents + 1 human; blog pipeline with two numbered approvals and one conditional escalation.

## Inconsistencies / open questions
- [verified] Anthropic figures quoted in the deck match this Talk's capture `research/web/anthropic-multi-agent-research-system/page.md`: "outperformed single-agent Claude Opus 4 by 90.2%", "agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats", "token usage by itself explains 80% of the variance", "most coding tasks involve fewer truly parallelizable tasks than research…", "LLMs autonomously using tools in a loop" — all found verbatim (grep).
- [verified] Kore.ai quotes "the challenge shifts from building AI agents to coordinating them effectively" and "choose the simplest pattern that effectively meets your business requirements" found verbatim in `research/web/koreai-orchestration-patterns/page.md` (grep).
- [verified] Slide 1.2 "Objetivos para hoy": the Sources bullet says "Los cuatro objetivos…" and maps four, but the Content lists **seven** objectives and the notes speak of "el primero… sostiene a los otros seis" and "Los otros cinco se cumplen" — internal count mismatch (checked lines 79–118).
- [verified] Conclusions slide 1 is titled "Las cuatro ideas de la clase" but lists **five** items, and its notes say "Las cinco en orden de la clase" (checked lines 1657–1683).
- [verified] Cross-references to slide numbers are stale in several places: Open questions says the token is defined "en 2.8" but the definition lives in 2.5 "El precio de paralelizar"; Open questions says "La lámina 3.4 dibuja esas dos salidas como PARKED y CANCELLED" but the state diagram is in 3.2; it says "La lámina 6.2 dibuja la versión del sistema" for the blog pipeline, which is 6.3; "Las notas de 6.1 avisan de mostrarlos en pantalla" refers to notes that are in 6.2 (checked against section/slide headings).
- [verified] The source itself flags two incompatible Task lifecycles (paperclip.ing: in progress / blocked / in review / done; newsletter: backlog → todo → in_progress → in_review → done) and two goal chains (4 levels vs. 3 levels) — internal, documented by the source.
- [verified] All 11 image references (`images/s2-2-1-orchestrator-worker.png`, `images/s2-3-1-contexto-no-compartido.png`, `images/6925681e304d9f06a73a3f6f_supervisor-pattern.png`, `images/6925683354b56e0f11f41f38_AA-network-pattern.png`, `images/s3-2-1-ciclo-vida-task.png`, `images/s3-5-1-linaje-objetivos.png`, `images/s3-8-1-task-tres-trabajos.png`, `images/s4-2-1-org-chart-agentes.png`, `images/s4-7-1-tarjeta-aprobacion.png`, `images/s6-3-1-recorrido-pedido-blog.png`, `images/sc-2-1-arbol-decision.png`) are unresolved: no `images/` folder exists next to the source in `research/articles/`. Nine have their ASCII source inline (`<!-- ascii-source: … -->`); the two Kore.ai ones have alt text only, but their original `.webp` bytes exist in this Talk's sibling record companion `koreai-orchestration-patterns.web/images/` (checked by `ls`).
- [verified] The source's own `Sources` fields point to `corpus/*.web.md` records of the other repo; only four have equivalents in this Talk (see Provenance), and the Anthropic one has a different name here.
- [open question] Claims about Paperclip's product (states, budgets enforcement, governance scope, adapters count, "rewind", watchdog, CVE-2026-33579 for OpenClaw, "74k+" GitHub stars) were not re-checked by this librarian; they are moot for the current Talk since Paperclip is not shown, but would need re-verification before any reuse.
- [open question] "Brinsa" quotes ("Orchestration is not the magic. Orchestration is the seatbelt." / "…you don't have orchestration. You have hope.") are flagged by the source itself as having no corpus record — need a source before use.
- [open question] The Cut material preserves the Anthropic-vs-Cognition debate ("La misma figura, dos veredictos": Cognition 12 jun 2025 vs Anthropic 13 jun 2025) that was cut from the MiM deck at presenter request ("Ni lo mencionemos"); whether that cut applies to the current Talk is a presenter decision — for a multi-agent architectures class it may be relevant again.
- [open question] Model names Claude Opus 4 / Sonnet 4 / Sonnet 3.7 are historical (June 2025 article) — fine as citations of that article, but the Editor should not present them as current models without checking the `claude-api` skill.

## Images / diagrams
The source carries **no image bytes** — every reference below is unresolved (companion folder `orquestacion-de-agentes-clase.md/images/` is intentionally empty). No `pending` marker is used because there is nothing to transcribe; the ASCII sources (preserved verbatim in the raw excerpt) are the textual equivalent of nine of them.

1. `images/s2-2-1-orchestrator-worker.png` (slide 2.2) — alt: "Arquitectura orchestrator-worker: un lead agent despacha tres subagentes de busqueda en paralelo". Unresolved; ASCII source inline (Consulta → Lead agent (orchestrator) ↔ Memory (plan); 3 search subagents with self-loops; Citations subagent → Informe final). Redrawing of Anthropic fig1 (bytes likely in `anthropic-multi-agent-research-system.web/images/`).
2. `images/s2-3-1-contexto-no-compartido.png` (slide 2.3) — alt: "Cada subagente hereda el contexto del lead pero no ve el de su hermano". Unresolved; ASCII source inline ([G]/[B1]/[B2]/[P] context stacks). Redrawing of Cognition fig2 (bytes likely in `cognition-dont-build-multi-agents.web/images/`).
3. `images/6925681e304d9f06a73a3f6f_supervisor-pattern.png` (slide 2.6) — alt: "Patrón supervisor de Kore.ai: USER arriba, ORCHESTRATOR al medio con capacidades de razonamiento, planificación, ruteo y reflexión, y tres agentes especialistas abajo". Unresolved here; original bytes at `koreai-orchestration-patterns.web/images/6925681e304d9f06a73a3f6f_supervisor-pattern.webp`.
4. `images/6925683354b56e0f11f41f38_AA-network-pattern.png` (slide 2.7) — alt: "Patrón de red adaptativa de Kore.ai: seis agentes pares conectados entre sí, cada uno con su propia fila de orquestación, y una caja USER sin ningún conector". Unresolved here; original bytes at `koreai-orchestration-patterns.web/images/6925683354b56e0f11f41f38_AA-network-pattern.webp`. (The decision table of slide 2.8 is transcribed from `…_implementation-recomendation.webp`, same folder.)
5. `images/s3-2-1-ciclo-vida-task.png` (slide 3.2) — alt: "Maquina de estados de una Task: las cuatro cajas del sitio mas PARKED y CANCELLED". Unresolved; ASCII source inline.
6. `images/s3-5-1-linaje-objetivos.png` (slide 3.5) — alt: "Cadena de objetivos de cuatro niveles, de la mision a la Task". Unresolved; ASCII source inline.
7. `images/s3-8-1-task-tres-trabajos.png` (slide 3.8) — alt: "La Task sostiene tres funciones a la vez: unidad de trabajo, registro de decision y rastro de auditoria". Unresolved; ASCII source inline.
8. `images/s4-2-1-org-chart-agentes.png` (slide 4.2) — alt: "Organigrama de agentes de un equipo de marketing de contenidos". Unresolved; ASCII source inline. Paperclip-specific.
9. `images/s4-7-1-tarjeta-aprobacion.png` (slide 4.7) — alt: "Tarjeta de aprobacion: el gate de gobernanza hecho interfaz". Unresolved; ASCII source inline. Paperclip-specific.
10. `images/s6-3-1-recorrido-pedido-blog.png` (slide 6.3) — alt: "Recorrido de un pedido de blog: seis pasos, dos aprobaciones numeradas y un escalamiento excepcional". Unresolved; ASCII source inline. Atlas/MiM-specific.
11. `images/sc-2-1-arbol-decision.png` (Conclusions 2) — alt: "Arbol de decision que resume la clase en tres preguntas encadenadas". Unresolved; ASCII source inline.

Also referenced only by name in the source (no image link): `s2-7-1` (communication graph), `s2-9-1` (single thread with context overflow), Cognition `fig5-context-compression-model.png`, The AI Enterprise hero `run-company-ai-agents-paperclip.png`, `fig3-clio-usage-embedding-plot.webp` — none present.

## Raw / preserved excerpts

The complete source file follows verbatim inside a five-backtick fence (the source uses three-backtick `ascii` fences internally). **One deliberate substitution:** on source line 1824 the literal marker string `<!-- pending​: process_images -->` is written below as `<!-- pending​: process_images -->` with a zero-width space (U+200B) after `pending`, so this record is not mis-detected as an incomplete stub by the idempotency check. Everything else is byte-identical to the source.

`````markdown
---
presentation: Agentes Inteligentes — Master in Management (MiM), IAE Business School, Universidad Austral
class: Orquestación de Agentes — coordinación, Tasks y gobernanza
research: research/corpus/
description: Slides are grouped into Sections. Each Section contains one or more Slides.
presenter: Paulo Veiga, Marco Sorondo y Claudio Righetti
audience: Profesionales y estudiantes de negocios con fundamentos de programación (MiM). Buscan aplicar AI a problemas de gestión y comprender cómo se construyen, revisan y gobiernan herramientas de software.
duration: 2 horas
date: sábado 28 de noviembre de 2026
---

# Thesis

**Claim:** Un equipo de agentes se vuelve gobernable cuando cada unidad de trabajo es una Task con dueño, estado y rastro; esa misma Task sostiene la coordinación, la decisión y la auditoría.

**Why it matters:** Un manager que despliega agentes hoy hereda dos preguntas que su directorio le va a hacer: cuánto costó y quién autorizó. Sin Task no hay respuesta a ninguna de las dos, y la discusión técnica sobre arquitecturas (un hilo o muchos) queda subordinada a esa decisión de gestión. La clase usa Paperclip como instrumento para ver la abstracción funcionando en un producto real, con sus mecanismos y con el alcance exacto de cada uno.

---

# Agenda

**Narrative arc:** La clase avanza en tres movimientos. El primero es abstracto y va derecho a la receta: abre nombrando la diferencia de nivel entre una herramienta y una compañía, promete lo que la clase deja, repasa el vocabulario con el que se entra, escribe qué hay que definir para armar una, arranca en el problema concreto de tener agentes capaces sin coordinación, da la forma de reparto que funciona con su límite y su precio, los patrones para coordinarla y un caso trabajado, y aterriza en la Task como forma que toman la gobernanza y la auditoría, dibujando cada pieza antes de definirla. El segundo movimiento es particular: aplica todo eso a Paperclip, primero los controles que la plataforma ofrece y después la capa que corre por debajo, con el alcance real de cada pieza. La frontera entre esos dos movimientos no es estanca: la sección 3 usa dos maquetas del producto para dibujar sus abstracciones, siempre con la atribución a la vista. El tercer movimiento es corto y concreto: la instancia que los participantes van a abrir, con sus cinco agentes, su único humano y el recorrido completo de un pedido de blog con sus aprobaciones. Ahí la clase deja de mirar el producto y pasa a mirar una empresa que ya corre, que es la antesala de la misión.

**Sections (in delivery order):**

- 1. Agentes descoordinados
- 2. Repartir el trabajo
- 3. La Task
- 4. Controles de Paperclip
- 5. La capa de abajo
- 6. La misión

---

# 1. Agentes descoordinados

**Goal of this section:** Instalar el problema que la clase resuelve, con vocabulario de management y no de ingeniería: un agente suelto funciona, diez agentes sueltos son un problema de organización. La sección abre nombrando la diferencia de nivel entre una herramienta y una compañía, enuncia enseguida los objetivos de la clase, chequea con tres preguntas qué quedó de las clases anteriores y recién entonces escribe qué hay que definir para armar esa compañía; también deja definida la orquestación antes de que aparezca en cualquier argumento posterior. La definición de agente salió del deck a pedido del presenter y se dicta de palabra al abrir.

---

## 1. CoWork y Paperclip

<!-- template: statement -->
<!-- generate-image: right | la diferencia entre una pieza suelta y una estructura que la contiene y le da lugar -->

### Content

CoWork es un empleado, Paperclip es la compañía.

### Sources

- `corpus/paperclip-home.web.md` — la forma de la analogía sale del testimonio de Resolver Vicky (@resolvervicky), verbatim: "OpenClaw is an employee, Paperclip is the company." **La lámina la adapta**: cambia OpenClaw por CoWork y la enuncia en la voz del presenter, sin atribuir. No es una cita.
- `corpus/github-paperclip-repo.web.md` — la misma frase reportada como línea central del README; el registro es una reconstrucción a mano (GitHub devolvió 403), así que la atribución al README no está verificada y no va a lámina.

### Speaker notes

Esta lámina abre la clase. Es una sola línea y conviene dejarla en pantalla mientras se habla: la sala ya usó CoWork, así que la pieza suelta la conoce, y lo que aparece hoy es el nivel de arriba. Toda la clase vive en esa diferencia de nivel, así que vale enunciarla despacio y no pasar de largo.

**La línea de la lámina es del presenter, no una cita, y conviene decirlo si alguien la busca.** La forma viene de un testimonio del sitio de Paperclip — **Original:** "OpenClaw is an employee, Paperclip is the company.", de Resolver Vicky (@resolvervicky), [muro de testimonios de paperclip.ing](https://paperclip.ing/), agosto 2026 — y la clase la reformula cambiando OpenClaw por CoWork, que es la herramienta que esta audiencia ya usó. Por eso va sin comillas y sin atribución: enunciarla como cita sería atribuirle a alguien algo que no dijo.

El problema sentido hay que instalarlo de palabra, porque el gancho que lo traía —la confesión de Mark R. Hinkle sobre su propio setup sin coordinación— se cortó a pedido del presenter. Sirve la pregunta directa a la sala: cuántos tienen hoy más de una herramienta de AI corriendo sin saber qué gasta cada una. Suele levantar bastantes manos y ancla la clase en su realidad. Si se prefiere citar, la confesión sigue disponible: «Agentes capaces. Coordinación cero. Ninguna misión compartida. Ninguna forma de ver de un vistazo qué me estaba costando cada cosa.» — [Mark R. Hinkle, The AI Enterprise, abril 2026](https://www.theaienterprise.io/p/run-company-ai-agents-paperclip); vale la salvedad de que Hinkle es publisher de un newsletter de AI, no un analista independiente, así que sirve para el problema y no para evaluar el producto.

El deck ya no trae lámina que defina agente, así que la definición va de palabra acá, que es la primera vez que la palabra aparece en la clase. Un agente es un modelo de lenguaje que usa herramientas en un loop; decide, ejecuta una acción, mira el resultado y vuelve a decidir. Hay dos fronteras que la sala necesita. Frente al chat, que responde y termina, el agente cambia algo afuera (escribe un archivo, abre un PR, manda un mail). Frente al script, que sigue un camino fijo, el agente elige el próximo paso según lo que encontró en el anterior. La definición es de [Anthropic, junio de 2025](https://www.anthropic.com/engineering/multi-agent-research-system), y el costo de esa libertad (unos 4× los tokens de un chat) se gasta en la lámina 2.5.

La analogía aguanta el cambio porque el argumento no es sobre el producto sino sobre el nivel: una herramienta que hace el trabajo es un empleado; lo que le pone jefe, presupuesto y aprobaciones es la compañía. Sirve con cualquier runtime que la sala conozca.

El muro de testimonios del que sale la formulación original no es evidencia de nada: los testimonios son autoseleccionados, sin fecha y sin link, y el marquee los repite cinco veces en el HTML. Con la línea enunciada en primera persona ese problema desaparece, porque ya no se está citando a nadie.

---

## 2. Objetivos para hoy

<!-- format: editorial -->

### Content

En Cowork la clase le delegaba trabajo a un agente. Hoy son muchos, y juntos forman una empresa.

- **Entender la empresa virtualizada** Puesto, jefe, presupuesto y rastro en cada agente.
- **Orquestar** Quién hace qué, en qué orden, con qué información y con qué tope.
- **Decidir si repartir** Cuándo conviene dividir un trabajo, y qué cuesta hacerlo.
- **Escribir una Task** La delegación de Cowork, con dueño, estado, hilo y cierre.
- **Juzgar una herramienta** Cómo se bloquea una acción, cómo se registra y cómo se detiene.
- **Ver Paperclip por dentro** Sus mecanismos, con el alcance real de cada uno.
- **Sumar un puesto** Un rol nuevo en una empresa que ya corre, sin escribir código.

### Sources

- Encuadre propio del curso, no del corpus. Los cuatro objetivos se derivan de los `Goal of this section` de este deck, uno por movimiento de la clase: el primero cubre las secciones 1 y 2, el segundo la 3, el tercero la prueba de orquestación que atraviesa 3 a 5, y el cuarto la sección 6.
- La continuidad con las clases anteriores sale de sus propias tesis, en `talks/claude-cowork` («el usuario delega resultados completos combinando sus piezas») y `talks/agent-fundamentals` («un agente sirve o no sirve según una medida de desempeño definida antes de construirlo»).

### Speaker notes

La lámina es deliberadamente corta: cuatro rótulos y una línea de cuerpo cada uno. Todo el desarrollo vive acá abajo, en estas notas, y se dicta. Si se lee la lámina en voz alta se pierde el minuto y medio que vale.

La lámina va segunda, justo después de la línea que abre la clase y justo antes del mapa de la compañía. Para cuando la sala llega acá ya sintió el problema, así que los objetivos se leen como la promesa de la clase. Lo que sigue son tres preguntas de repaso, y recién después el mapa de la compañía: primero se promete, después se chequea con qué base se arranca, y con esa base puesta el mapa se lee sin explicar nada. El gancho de apertura y la definición de agente viven ahora en las notas de la lámina que abre, así que acá no hace falta repetirlos.

El primer objetivo es el que sostiene a los otros seis, y es de comprensión y no de acción: entender qué es una **empresa virtualizada de agentes**. Los seis que siguen son cosas que el participante hace o ve; este es la pieza sin la cual los otros no se entienden, por eso va primero. El orden de los seis es el de la clase, así que la lámina funciona además como mapa: cada objetivo dice en qué parte del recorrido se paga.

Sobre el nombre: la clase lo llama **empresa virtualizada de agentes**, en singular y con esas palabras. «Organización agéntica» es la misma idea con vocabulario más técnico y conviene no alternar los dos en sala, porque suenan a dos cosas distintas. El deck lo venía construyendo sin nombrarlo: la sección 1 plantea la ausencia —agentes capaces sin nada que los organice— y la 3.8 la entrega («sin esa pieza hay agentes actuando, con ella hay una organización que se puede inspeccionar y frenar»); la sección 4 recorre sus mecanismos, que son los de cualquier organización (organigrama, presupuesto, aprobaciones, auditoría); y la sección 6 muestra una corriendo. Nombrarlo acá le da a la sala una etiqueta para todo lo que sigue.

La definición corta, para decir en sala: una empresa virtualizada de agentes es un conjunto de agentes donde cada uno tiene un puesto con instrucciones permanentes, un jefe, un presupuesto y un rastro de lo que hizo. **Lo que la vuelve una empresa y no un grupo de herramientas es que esas cuatro cosas existan, no la cantidad de agentes.** Ese es el matiz que hay que dejar clavado, porque es el error de lectura más común: la sala tiende a pensar que la diferencia es de escala y es de estructura.

La conexión con lo anterior también conviene decirla, porque es lo que vuelve al concepto una consecuencia y no una novedad: en Cowork cada uno delegaba a un agente y ya usaba subagentes, así que la pieza suelta la conocen. Lo que aparece hoy es lo que hay alrededor de esa pieza cuando son muchas.

El arco entre clases es lo que hay que decir en voz alta, porque es lo que vuelve a esta clase una continuación y no un tema nuevo. En las clases de Cowork el movimiento fue pasar de chatear a delegar: el agente baja a la computadora y se le encarga un resultado completo, con sus archivos, sus Projects, sus Skills y sus subagentes. En la clase de fundamentos el movimiento fue exigirle una medida de desempeño definida antes de construirlo, para distinguir una demo de una delegación. Esta clase agrega el problema que aparece cuando los agentes son varios a la vez, que ya no es de capacidad sino de organización.

Conviene nombrar el hilo con esas tres palabras y en ese orden: delegar, medir, gobernar. La sala reconoce las dos primeras porque las practicó. Y el sujeto cambia con la tercera: en Cowork el sujeto era un agente, acá es una organización.

El segundo objetivo es el que más agradece la conexión explícita. La Task no es un concepto nuevo que aparece en esta clase: es la misma delegación que ya hicieron en Cowork, ahora con las cuatro cosas que la vuelven auditable. Decirlo así ahorra media sección.

No leerlos uno por uno. Se muestran, se nombra el hilo con las tres palabras, y se sigue. La lámina existe para que la sala sepa dónde está parada, no para dictarla.

El segundo, orquestar, es el que le da nombre a la clase y su cuerpo es la definición de la lámina 1.7, palabra por palabra: decidir quién hace qué, en qué orden, con qué información y bajo qué límite de gasto. Vale decir que esas cuatro decisiones son de management y no de arquitectura, que es la tesis de la clase en una línea.

El sexto objetivo, ver Paperclip por dentro, tiene un matiz que conviene decir apenas se nombra el producto: Paperclip es el instrumento y no el tema. La clase lo usa para ver funcionando lo que las secciones 1 a 3 dan en abstracto, y lo lee con criterio, corrigiendo lo que el propio material del producto exagera. Las dos palabras que hacen ese trabajo en el objetivo son «alcance real»: la clase muestra cada mecanismo y también dónde termina. Si alguien pregunta si la clase enseña Paperclip, la respuesta honesta es que enseña a mirar cualquier herramienta de orquestación y usa esta como caso.

Salvedad de honestidad: el último objetivo depende de que la sección 6 se dicte de verdad. Si el tiempo aprieta y la misión queda afuera, conviene no prometerlo acá o decir que queda como trabajo posterior. Los otros cinco se cumplen aunque la clase termine en la sección 5.

---

## 3. Quiz: qué es un agente

<!-- template: quiz -->

### Content

¿Qué es un agente?

- A. Un chat al que le escribís mejores instrucciones.
- B. Un modelo de lenguaje que usa herramientas en un loop: decide, ejecuta una acción, mira el resultado y vuelve a decidir.
- C. Un programa que corre siempre los mismos pasos, en el mismo orden.
- D. Un modelo más grande y más caro que el del chat.

**Respuesta:** B. Un modelo de lenguaje que usa herramientas en un loop, y que cambia algo afuera.

Dos fronteras: frente al chat, que responde y termina, el agente escribe un archivo, abre un PR o manda un mail. Frente al programa fijo, el agente elige el paso siguiente según lo que encontró en el anterior.

`Anthropic, jun-2025`

### Sources

- `corpus/anthropic-multi-agent-research.web.md` — la definición de agente como modelo que usa herramientas en un loop; es la misma que la clase venía dictando de palabra desde que se cortó la lámina de definición.

### Speaker notes

Las tres preguntas de este bloque son un chequeo de lo que quedó de las clases anteriores, no una evaluación. Dejar votar a mano alzada antes de revelar: el valor está en que la sala se escuche a sí misma dudar, y en que el presenter sepa con qué nivel arranca. Si la mayoría acierta, el bloque se pasa en dos minutos; si no, conviene ir más despacio en la sección 2.

Esta es la pregunta que le devuelve al deck una definición que había perdido. La lámina «Qué es un agente» se cortó a pedido del presenter y la definición se venía dictando de palabra; acá vuelve a estar en pantalla, y en la forma que le sirve a esta audiencia: como algo que la sala contesta, no como algo que se le explica.

Los distractores están elegidos, no rellenados. A es la confusión más común y la que la clase anterior ya desarmó. C es la frontera contra el programa de siempre, que es la que separa a un agente de una automatización clásica. D es la creencia de que la diferencia es de tamaño de modelo y no de forma de trabajo, y es la que más conviene desarmar en voz alta si alguien la elige.

Si alguien pregunta por el costo: esa libertad de elegir el próximo paso se paga en tokens, unos 4× los de un chat, y se ve en la lámina 2.5.

---

## 4. Quiz: qué es un subagente

<!-- template: quiz -->

### Content

¿Qué es un subagente?

- A. El mismo agente corriendo otra vez, sobre la misma ventana de contexto.
- B. Un agente que otro agente crea para una parte del trabajo, con su propia ventana de contexto.
- C. Otro nombre para una herramienta del agente.
- D. Un agente que corre en otra computadora.

**Respuesta:** B. Un agente que otro agente abre para una parte del trabajo, con su propia ventana de contexto.

Ventana propia quiere decir dos cosas: ve solo lo que el que lo abrió le pasa, y **nunca ve lo que está haciendo su hermano**. Cuánto le pasa el que lo abrió es una decisión de diseño, y la sección 2 muestra que ni pasarle todo alcanza.

`Anthropic, jun-2025`

### Sources

- `corpus/anthropic-multi-agent-research.web.md` — `run_subagent` como herramienta del agente principal; ventana de contexto propia por subagente. La respuesta usa la misma formulación que la lámina 2.1, palabra por palabra, para que no queden dos versiones del término.

### Speaker notes

La sala ya usó subagentes en CoWork sin necesariamente haberlos nombrado así, y esa es la razón de la pregunta: convertir una práctica en un concepto que se puede discutir.

**La pregunta que esta lámina tiene que dejar bien contestada, porque es donde la sala se confunde: ¿comparten el contexto o no?** Hay tres cosas distintas y conviene decirlas en este orden. Uno: cada subagente tiene su PROPIA ventana de contexto, siempre; no es un pedazo de la del padre ni la misma ventana. Dos: qué le entra a esa ventana lo decide quien lo abrió, y va desde un encargo de dos líneas hasta todo lo que el padre tenía. Tres: pase lo que pase, un subagente no ve lo que está haciendo su hermano mientras trabaja. La lámina 2.3 dibuja justo el caso más generoso —al subagente se le pasa TODO el contexto del que planificó— y el veredicto de la fuente sigue siendo que no alcanza, porque el trabajo del hermano no está ahí. Esa es la idea que hay que instalar, y es la que sostiene la sección entera.

El distractor A dice «el mismo agente, la misma ventana», que es falso por los dos lados. Si alguien lo elige, la corrección es corta: es otro agente, con otra ventana, y por eso hay que decidir qué le pasás.

C confunde subagente con herramienta, y la diferencia vale decirla: una herramienta se ejecuta y devuelve, un subagente decide. D es geografía, no arquitectura, y no cambia nada de lo que la clase discute.

La respuesta se enuncia con las mismas palabras que la lámina 2.1, a propósito. Si la sala pide más, ahí está el desarrollo completo, con fan-out y fan-in, y el dato que cierra el argumento: lo que un subagente devuelve son hallazgos destilados, no su historial completo.

---

## 5. Quiz: qué es el contexto de un modelo

<!-- template: quiz -->

### Content

¿Qué es el contexto de un modelo, y qué se guarda ahí?

- A. La memoria permanente del modelo: lo que aprendió cuando lo entrenaron.
- B. Todo lo que el modelo tiene a la vista en una sola corrida: instrucciones, archivos, lo que devolvieron las herramientas y la conversación hasta ahí.
- C. Una base de datos donde el agente escribe lo que quiere recordar.
- D. El historial de la cuenta del usuario.

**Respuesta:** B. Todo lo que el modelo tiene a la vista en una sola corrida. Es finito, y se llena.

No es memoria: no sobrevive solo de una corrida a la otra. Lo que tiene que persistir se escribe afuera, y ese es el problema que la clase resuelve con la Task.

`Anthropic, jun-2025`

### Sources

- `corpus/anthropic-multi-agent-research.web.md` — la ventana de contexto como el texto que el modelo puede tener a la vista en una sola corrida, y su carácter finito. Misma formulación que la lámina 2.1.

### Speaker notes

Es la más difícil de las tres y la que más rinde, porque el error que desarma sostiene medio malentendido sobre agentes: creer que el modelo «se acuerda».

A es la confusión entre entrenamiento y contexto, y conviene nombrarla: lo que el modelo aprendió está congelado, lo que el modelo tiene a la vista cambia en cada corrida. C es tentadora porque describe algo que sí existe, pero es otra cosa: escribir afuera es exactamente lo que hay que hacer PORQUE el contexto no alcanza. D es la respuesta de producto, no de modelo.

Dos consecuencias conviene dejarlas dichas acá, porque las tres secciones siguientes se apoyan en ellas: el contexto es finito y se paga por token, así que repartir trabajo cuesta plata; y como no persiste, el estado tiene que vivir en un lugar que sí persista. La primera se cobra en 2.5, la segunda en toda la sección 3.

---

## 6. Qué hay que definir para armar una compañía

<!-- format: editorial -->

### Content

Una compañía se define antes de que alguien trabaje: seis decisiones. **Orquestar es sostener las seis mientras el trabajo corre.**

- **Misión y objetivos** Para qué existe y qué tiene que lograr.
- **Diseño organizacional** Qué roles hacen falta y quién le responde a quién.
- **El flujo de trabajo** Qué es una unidad de trabajo, quién es su dueño, cuándo cierra.
- **Presupuesto** Cuánta plata hay y quién responde por cómo se gasta.
- **Quién firma** Qué decisiones necesitan aprobación, y de quién.
- **Qué queda escrito** El rastro de lo que se hizo y por qué.

### Sources

- Encuadre propio del curso, no del corpus. Las seis decisiones se derivan de los `Goal of this section` de este deck, y cada una se paga más adelante: misión y objetivos en 3.5 y 3.6, diseño organizacional en 4.2, el flujo de trabajo en toda la sección 3, presupuesto en 4.6 y en 2.5, quién firma en 4.7, y el rastro en 3.7.

### Speaker notes

Esta lámina es el mapa de la clase disfrazado de checklist de fundación, y llega justo después del bloque de repaso, que es lo que la vuelve legible: con agente, subagente y contexto ya contestados por la sala, las seis decisiones se leen sin tener que definir nada en el camino. Conviene decir en voz alta que las seis vuelven, una por una, con el mecanismo de Paperclip que las resuelve: así la clase se lee como un solo hilo y no como seis temas sueltos.

Dónde se paga cada una, para poder señalarlo cuando llegue: misión y objetivos en 3.5 y 3.6, con el linaje que baja de la misión a la Task; diseño organizacional en el organigrama de 4.2, que es donde aparecen rol, título y línea de reporte; el flujo de trabajo en toda la sección 3, que es la Task con su dueño, su estado y su cierre; presupuesto en Budgets (4.6), y antes en 2.5, que es donde se ve lo que cuesta repartir; quién firma en Governance y aprobaciones (4.7); y el rastro en el audit trail (3.7).

**Por qué orquestar está en el encabezado y no como un séptimo ítem, que es la pregunta que la lámina invita a hacer.** Orquestar no es una cosa más que se define al fundar: es el verbo que corre sobre las seis una vez que la compañía arrancó. Y se puede mostrar, no solo afirmar: la definición que da la lámina 1.7 —decidir quién hace qué, en qué orden, con qué información y bajo qué límite de gasto— tiene sus cuatro decisiones repartidas acá adentro. Quién hace qué es el diseño organizacional; en qué orden es el flujo de trabajo; bajo qué límite de gasto es el presupuesto; y con qué información es lo que la sección 3 va a contestar con la Task. Decirlo así deja la lámina 1.7 medio dictada.

El punto que hay que dejar clavado: **ninguna de las seis es una decisión técnica.** Son las mismas que toma cualquiera que funda una empresa de personas, y ahí está la tesis de la clase en una línea: orquestar es management y no arquitectura. Si la sala se lleva una sola cosa de la apertura, que sea esta.

La conexión con lo anterior también conviene decirla. En CoWork cada uno le delegaba a un agente y ya usaba subagentes, así que el empleado lo conocen. Lo que se define acá es todo lo que va alrededor cuando son varios.

**Dos ausencias deliberadas, para que una sesión futura no las «arregle».** La primera es la comunicación entre áreas: quedó afuera porque la clase argumenta justo lo contrario, que el trabajo se pasa con Tasks con dueño y no con mensajes con onda; si alguien la nombra desde la sala, esa es la respuesta, y funciona mejor dicha que escrita. La segunda es la supervisión: el heartbeat es un mecanismo, no una decisión de fundación, y llega solo en 4.3.

**El séptimo ítem candidato, si el presenter lo quiere:** llaves y accesos, es decir a qué sistemas entra cada uno y qué puede tocar. Es legítimo y lo paga la sección 5 entera (Skills, Plugins y MCP, sandbox, self-hosting). Quedó afuera para mantener la lista en seis y porque es el único que no aterriza hasta el final; mientras no esté, la sección 5 es la única del deck sin ítem que la anticipe.

---

## 7. Qué es orquestar

### Content

Orquestar es decidir quién hace qué, en qué orden, con qué información y bajo qué límite de gasto.

- **No es prompt engineering** Escribir mejor la instrucción mejora una tarea. Orquestar mejora un equipo.
- **La decisión se mudó** Kore.ai lo formula así: el desafío pasó de construir agentes a coordinarlos.
- **Cuatro dimensiones que la elección mueve** costo en tokens, latencia, velocidad de desarrollo contra control, y escalabilidad con su mantenimiento.

`Kore.ai, oct-2025 (act. jul-2026)`

### Sources

- `corpus/koreai-orchestration-patterns.web.md` — definición de patrón de orquestación; "the challenge shifts from building AI agents to coordinating them effectively"; las cuatro dimensiones afectadas.

### Speaker notes

La definición de Kore.ai apunta al mismo lugar y conviene tenerla a mano por si alguien pide fuente: el patrón de orquestación «define cómo interactúan los agentes, cómo comparten contexto y cómo colaboran para completar tareas complejas». Estaba en el cuerpo de la lámina y bajó acá al compactarla.

**Original:** "defines how agents interact, share context, and collaborate to complete complex tasks" — [Kore.ai, oct-2025](https://www.kore.ai/blog/choosing-the-right-orchestration-pattern-for-multi-agent-systems).

[Kore.ai](https://www.kore.ai/blog/choosing-the-right-orchestration-pattern-for-multi-agent-systems) vende la plataforma que implementa los tres patrones que vamos a ver en la sección 2, así que la definición sirve y la lista de proveedores conviene tomarla como marketing.

El punto de management: las cuatro dimensiones que nombra son las cuatro variables que un manager ya sabe manejar en cualquier proceso. Costo, tiempo, control y mantenimiento. La novedad es el sustantivo al que se aplican.

---

## 8. Tres niveles de gestión de agentes

<!-- template: timeline -->

### Content

1. **Nivel 1. Agentes de tarea única.** Un agente, un trabajo. Se le pide algo, se revisa la salida y se sigue. No tiene memoria del negocio, ni conexión con los objetivos, ni rendición de cuentas. Cada sesión arranca de cero.
2. **Nivel 2. Agentes especializados en paralelo.** Varios agentes, cada uno dueño de una función, corriendo en una agenda. Comparten jerarquía de objetivos y no colaboran entre sí. La coordinación sigue siendo manual.
3. **Nivel 3. Orquestación jerárquica.** Un agente CEO interpreta la misión de la compañía, la descompone en proyectos, asigna hacia abajo por un organigrama y escala los bloqueos hacia arriba, al directorio humano. Cada tarea de cada nivel remite a la misión.

`The AI Enterprise, abr-2026`

### Sources

- `corpus/aienterprise-run-company-agents.web.md` — "The Three Levels of Agent Management", verbatim; la observación de que la mayoría de los profesionales de negocios está en el Nivel 1.

### Speaker notes

La escalera de [Hinkle](https://www.theaienterprise.io/p/run-company-ai-agents-paperclip) es el mejor recurso didáctico del corpus para esta audiencia porque está escrita en vocabulario de negocio y no de arquitectura.

Preguntar en qué nivel se ubica cada uno. La respuesta honesta de casi toda la sala es Nivel 1, y eso vuelve concreta la distancia que la clase recorre.

El Nivel 3 es el objetivo de diseño de Paperclip, y conviene decirlo recién en la sección 4. Acá alcanza con dejar la escalera parada.

---

## 9. El cambio de modelo mental

<!-- template: quote -->

### Content

> «Uno deja de pensar "le estoy dando instrucciones a una IA" y empieza a pensar "estoy dirigiendo un equipo". Ese cambio de encuadre cambia cómo se diseñan los flujos de trabajo, cómo se asignan responsabilidades y cómo se evalúa el resultado.»

`The AI Enterprise, abr-2026`

### Sources

- `corpus/aienterprise-run-company-agents.web.md` — el cambio de modelo mental, verbatim.
- `corpus/paperclip-home.web.md` — testimonio de yash (@yashns1) con la misma formulación: "The shift from 'I am prompting an AI' to 'I am managing a team'".

### Speaker notes

**Original:** "You stop thinking 'I'm prompting an AI' and start thinking 'I'm managing a team.' That reframe changes how you design workflows, assign responsibilities, and evaluate output." — [Mark R. Hinkle, The AI Enterprise, abril 2026](https://www.theaienterprise.io/p/run-company-ai-agents-paperclip).

Esta lámina es la bisagra de la primera sección y conviene darle aire. El resto de la clase se apoya en que la audiencia acepte esta reformulación: si dirigir agentes se parece a dirigir un equipo, entonces las herramientas de dirección de equipos (organigrama, presupuesto, Tasks, aprobaciones, auditoría) son el material correcto.

Dos fuentes distintas del corpus repiten la frase casi igual, una del newsletter y otra de un testimonio en el sitio de Paperclip. Se puede mencionar como señal de que la formulación circula, no como evidencia de nada.

Esta lámina cierra la sección, así que el puente hacia la siguiente se dice de palabra, sin lámina de transición: si dirigir agentes se parece a dirigir un equipo, la primera decisión de diseño es la misma que en cualquier organización, **cuánto trabajo corre en paralelo**. Avisar además que lo que viene es un desacuerdo real entre dos equipos serios (Anthropic y Cognition) y no una encuesta de opciones. La respuesta ingenua es que más agentes en paralelo van más rápido; la documentada es que depende del dominio, y las dos posiciones tienen evidencia.

---

# 2. Repartir el trabajo

**Goal of this section:** Dar la receta de reparto de trabajo entre agentes: qué forma funciona, qué límite tiene, cuándo conviene repartir, cuánto cuesta, y con qué patrón coordinarlo. Al salir de la sección la audiencia puede decidir para un caso propio si reparte, con qué patrón y qué está pagando. La receta queda repartida en las nueve láminas que la construyen y ya no tiene lámina de cierre que la junte, así que el resumen se dicta de palabra sobre el caso trabajado con el que la sección termina.

---

## 1. Qué es un subagente

### Content

Un subagente es un agente que otro agente crea para una parte del trabajo, con su propia ventana de contexto. Crearlo es una acción del agente principal en marcha, no una pieza que alguien configuró antes.

- **Ventana de contexto** El texto que el modelo puede tener a la vista en una sola corrida. Es finita, y por eso el plan se guarda afuera.
- **Fan-out / fan-in** El agente principal reparte subtareas y después junta los resultados.
- **Lo que devuelve un subagente** Hallazgos destilados, no su historial completo.
- **Por qué existe la figura** Un contexto propio por subtarea, y un solo lugar donde se juntan los resultados.

`Anthropic, jun-2025`

### Sources

- `corpus/anthropic-multi-agent-research.web.md` — `run_subagent` como herramienta del lead agent (fig1); truncado del contexto a 200.000 tokens (caption verbatim de fig2); "The essence of search is compression".

### Speaker notes

Definir esto antes del diagrama de la lámina siguiente, que lo usa entero. La lámina es una definición conceptual a propósito: los tres términos valen para cualquier sistema multi-agente, no sólo para el que la lámina siguiente dibuja.

Los números y los nombres propios quedaron acá para no atar la definición a un proveedor. En el sistema de [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system), que es de donde sale el material, crear un subagente es literalmente una llamada a herramienta del agente principal, `run_subagent`, y su ventana de contexto trunca a partir de los 200.000 tokens. Ese segundo dato es el que explica por qué en el diagrama de la lámina siguiente la caja `Memory` está afuera del agente principal: el plan se escribe ahí antes de que exista ningún subagente, porque la ventana del lead no va a sobrevivir el loop.

Si la sala pregunta si esto es propio de Anthropic, la respuesta honesta es que el mecanismo (crear un trabajador con contexto propio y pedirle un resultado destilado) es general, y que el tamaño exacto de la ventana y el nombre de la herramienta cambian con cada proveedor.

---

## 2. La forma que funciona

### Content

La arquitectura que hoy tiene la mejor medición publicada es orchestrator-worker: un agente principal planifica y despacha subagentes especializados que trabajan en paralelo, cada uno con su propia ventana de contexto.

![Arquitectura orchestrator-worker: un lead agent despacha tres subagentes de busqueda en paralelo](images/s2-2-1-orchestrator-worker.png)
<!-- ascii-source:
                        Consulta
                            |
                            v
   +------------+   +----------------------+   +----------+
   | Citations  |<--| Lead agent           |<->|  Memory  |
   | subagent   |   | (orchestrator)       |   |  (plan)  |
   +------------+   +----------------------+   +----------+
         |            ^        ^        ^
         |            |        |        |
         |            v        v        v
         |      +---------+---------+---------+
         |      | Search  | Search  | Search  |
         |      | subag.1 | subag.2 | subag.3 |
         |      +---------+---------+---------+
         |         ^  |     ^  |     ^  |
         |         +--+     +--+     +--+
         v
    Informe final
-->
<!-- ascii-note:
intent: la arquitectura orchestrator-worker que produjo la mejora medida; es la forma de referencia del resto de la seccion.
emphasize: el rombo (lead arriba, tres subagentes en paralelo abajo); los self-loops de cada subagente, que son la iteracion interna que permite devolver hallazgos destilados; Memory afuera del lead.
labels: Consulta, Lead agent (orchestrator), Memory (plan), Search subagent 1-3, Citations subagent, Informe final.
-->

### Sources

- `corpus/anthropic-multi-agent-research.web.md` — fig1 `fig1-architecture-overview.png`, transcripción completa; "a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval"; el registro marca que la eval es interna y no publica rúbrica ni conjunto de prueba.

### Speaker notes

El número que la lámina ya no muestra, por si conviene decirlo: **+90,2% sobre un agente único**, en la eval interna de Anthropic. Es prueba propia, sin rúbrica ni conjunto de prueba públicos, así que se dice como lo que es o no se dice.

Sobre "eval": es la prueba con la que un equipo mide a su propio sistema. Que sea interna significa que nadie de afuera puede repetirla, y por eso el 90,2% se cita como el número que [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system) reporta sobre sí misma. La configuración que lo produce es Opus 4 de lead con Sonnet 4 de subagentes.

El caso concreto que Anthropic da: pedir todos los miembros de directorio de las empresas de IT del S&P 500. El sistema multi-agente lo resolvió descomponiendo; el agente único no encontró la respuesta con búsquedas secuenciales lentas.

Los self-loops de cada subagente importan: cada uno itera adentro antes de devolver, y por eso devuelve un hallazgo y no su historial.

---

## 3. Compartir el contexto no alcanza

### Content

Darle a cada subagente todo el contexto del que planificó no alcanza. Cada uno sigue sin ver el trabajo del hermano, así que los dos toman decisiones que el otro no conoce y el choque aparece recién al final, cuando alguien tiene que combinar.

![Cada subagente hereda el contexto del lead pero no ve el de su hermano](images/s2-3-1-contexto-no-compartido.png)
<!-- ascii-source:
                              Task
                               |
                               v
                   +------------------------+
       [G] <-------| Agent                  |
                   | breaks down task       |
                   +------------------------+
                      |                  |
                      v                  v
   [G]         +--------------+   +--------------+         [G]
   [B1] <------|  Subagent 1  |   |  Subagent 2  |------&gt; [B2]
               +--------------+   +--------------+
                      |                  |
                      v                  v
                   +------------------------+       [G] [B1]
                   | Agent                  |-----&gt; [B2] [P]
                   | combines the results   |
                   +------------------------+
                               |
                               v
                             Result

   [G]  contexto del lead        [B1] trabajo de la subtarea 1
   [B2] trabajo de la subtarea 2 [P]  trabajo de combinacion
-->
<!-- ascii-note:
intent: mostrar que cada subagente hereda el contexto del lead pero no ve el del hermano; la pila de fichas junto a cada caja es lo que ese agente puede ver.
emphasize: que la pila de Subagent 1 tiene [G][B1] y NO [B2], y la de Subagent 2 tiene [G][B2] y NO [B1]; la pila completa de cuatro fichas recien aparece en la caja que combina.
labels: leyenda [G] [B1] [B2] [P] al pie del diagrama.
-->

`Cognition, jun-2025`

### Sources

- `corpus/cognition-dont-build-multi-agents.web.md` — fig2 `fig2-subagents-with-shared-context.png`, transcripción completa de las cuatro pilas de fichas; veredicto de esquina "Still Unreliable"; Principio 1 y Principio 2.

### Speaker notes

La regla en una línea: **toda acción lleva adentro una decisión que nadie enunció**, y dos decisiones en paralelo que se contradicen dan un resultado malo.

Leer las pilas de fichas en voz alta, que es donde está el argumento: el subagente 1 tiene el contexto del lead y su propio trabajo, y nada del hermano; el subagente 2, al revés. La pila completa aparece recién en la caja que combina, que es donde se descubre el problema.

El ejemplo del artículo, por si sirve en sala: la tarea es clonar Flappy Bird, una subtarea hace el fondo y la otra el pájaro. Con todo el contexto compartido, igual salen en estilos visuales distintos, porque ninguno de los dos vio lo que decidía el otro.

El mismo hueco se ve en el sistema de [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system): entre sus dos subagentes de búsqueda no hay ningún mensaje en todo el diagrama de proceso. Ahí no molesta, porque cada uno devuelve un hallazgo destilado y no toca nada. La lámina siguiente convierte eso en regla.

La analogía para management: dos equipos que reciben el mismo brief y no se hablan durante el trabajo. El brief compartido no evita el choque de criterios.

---

## 4. Cuándo repartir, y cuándo no

### Content

- **Si el trabajo lee** Investigación, búsqueda, lectura de fuentes. Dos subagentes que leen cosas distintas no se pisan, y devuelven un hallazgo en vez de su historial. Repartir paga.
- **Si el trabajo escribe sobre algo compartido** Código, un mismo documento, una misma base. Cada acción cambia el terreno del otro: un solo hilo, o límites explícitos entre quienes escriben.
- **La frontera, en palabras de Anthropic** *«la mayoría de las tareas de código tienen menos partes realmente paralelizables que las de investigación, y los agentes todavía no son buenos coordinando ni delegando entre ellos en tiempo real»*

`Anthropic, jun-2025`

### Sources

- `corpus/anthropic-multi-agent-research.web.md` — el límite del dominio, verbatim; criterios de encaje positivo ("valuable tasks that involve heavy parallelization, information that exceeds single context windows, and interfacing with numerous complex tools"); "The essence of search is compression"; el registro señala que en el diagrama de proceso no existe mensaje alguno entre `Subagent1` y `Subagent2`.
- `corpus/cognition-dont-build-multi-agents.web.md` — el dominio donde las acciones mutan estado compartido; "Actions carry implicit decisions, and conflicting decisions carry bad results".

### Speaker notes

**Original:** "most coding tasks involve fewer truly parallelizable tasks than research, and LLM agents are not yet great at coordinating and delegating to other agents in real time." — [Anthropic, junio 2025](https://www.anthropic.com/engineering/multi-agent-research-system).

Es la lámina que convierte la lámina anterior en criterio aplicable, y la pregunta que la audiencia se lleva para sus propios casos es de una sola línea: el trabajo que quiero repartir, ¿lee o escribe?

Leer tolera hermanos que no se hablan. Escribir sobre algo compartido, no. Y el que marca ese límite es el equipo que más ganó paralelizando, lo cual le da peso.

Si alguien pregunta por el caso intermedio (repartir escritura sobre archivos distintos), la respuesta honesta es que funciona mientras los límites estén escritos antes y nadie los cruce. El apéndice de Anthropic sugiere una variante: que cada subagente escriba su salida a un archivo y devuelva solo una referencia liviana, para no pasar todo por el coordinador.

---

## 5. El precio de paralelizar

<!-- template: stat -->

### Content

El token es la unidad en la que el proveedor del modelo mide y factura el texto, y se publica a tanto el millón: todo lo que un agente lee y escribe pasa por esa caja.

- **~15×** los tokens de un chat, para un sistema multi-agente. `Anthropic, jun-2025`
- **~4×** los tokens de un chat, para un agente único. `Anthropic, jun-2025`
- **80%** de la varianza de desempeño en BrowseComp explicada por el uso de tokens solo. `Anthropic, jun-2025`

Anthropic saca de ahí la conclusión de gestión, no de ingeniería: *«los sistemas multi-agente piden tareas cuyo valor alcance para pagar la mejora de desempeño»*

### Sources

- `corpus/anthropic-multi-agent-research.web.md` — multiplicadores 4× y 15× sobre chat; descomposición de varianza en BrowseComp (tres factores explican 95%, el uso de tokens solo explica 80%); condición de viabilidad económica, verbatim.
- `corpus/koreai-orchestration-patterns.web.md` — "Token consumption and cost efficiency" como primera de las cuatro dimensiones que mueve la elección de patrón; sostiene la línea de definición del token.

### Speaker notes

**Original:** "multi-agent systems require tasks where the value of the task is high enough to pay for the increased performance." — [Anthropic, junio 2025](https://www.anthropic.com/engineering/multi-agent-research-system).

El 15× es el número que un manager va a anotar, y esta lámina es la primera que lo gasta, así que la definición de token va acá arriba en una línea. Con el precio por millón que publica el proveedor, la cuenta se hace en pesos en el pizarrón: cuánto sale la tarea como chat, ese número por 15, y comparado contra el tope mensual de un agente.

**Traer el precio vigente al dictado.** El material capturado no incluye ninguna lista de precios, así que el precio por millón de tokens del proveedor que se vaya a mencionar hay que buscarlo el día de la clase.

El 80% viene con una lectura incómoda que conviene decir: buena parte de la mejora del multi-agente se explica porque gasta más tokens, no porque sea más inteligente. Anthropic lo dice en su propio texto ("multi-agent systems work mainly because they help spend enough tokens to solve the problem").

Los tres factores que explican el 95% son uso de tokens, cantidad de llamadas a herramientas y elección de modelo. Dato lateral útil: subir de Sonnet 3.7 a Sonnet 4 dio más mejora que duplicar el presupuesto de tokens.

---

## 6. Patrón supervisor

### Content

Un orquestador central recibe el pedido, lo descompone, delega en especialistas, monitorea, valida y sintetiza la respuesta.

![Patrón supervisor de Kore.ai: USER arriba, ORCHESTRATOR al medio con capacidades de razonamiento, planificación, ruteo y reflexión, y tres agentes especialistas abajo](images/6925681e304d9f06a73a3f6f_supervisor-pattern.png)

`Kore.ai, oct-2025 (act. jul-2026)`

### Sources

- `corpus/koreai-orchestration-patterns.web.md` — figura `supervisor-pattern.webp`, transcripción completa; el orquestador "receives the user request, decomposes it into subtasks, delegates work to specialized agents, monitors progress, validates outputs, and synthesizes a final unified response".

### Speaker notes

Las cuatro capacidades del orquestador (`Reasoning`, `Planning`, `Routing`, `Reflection`) nombran el trabajo de gestión como distinto del trabajo de ejecución. Es una descripción de puesto, y mapea directo sobre lo que hace un manager. Señalarlas en la imagen.

Los tres agentes de abajo llevan las mismas tres filas (`Scope & Instructions`, `Knowledge`, `Tools`) y ninguna fila de orquestación. Guardar ese detalle: es la única diferencia estructural con la figura siguiente.

Entre `USER` y `ORCHESTRATOR` hay dos canales dibujados por separado, `Input` bajando y `Response` subiendo. Pedido y respuesta viajan por vías distintas.

El flujo de datos de mínimo privilegio es parte del patrón según [Kore.ai](https://www.kore.ai/blog/choosing-the-right-orchestration-pattern-for-multi-agent-systems): el orquestador da a cada agente solo el dato que necesita. Esa idea vuelve en la sección 3.

Es la misma forma de la lámina 2.2, dibujada acá sin marca de producto y en vocabulario de negocio.

---

## 7. Red adaptativa de agentes

### Content

Sin orquestador. Cada agente decide si ejecuta, delega o enriquece la tarea antes de pasarla.

![Patrón de red adaptativa de Kore.ai: seis agentes pares conectados entre sí, cada uno con su propia fila de orquestación, y una caja USER sin ningún conector](images/6925683354b56e0f11f41f38_AA-network-pattern.png)

`Kore.ai, oct-2025 (act. jul-2026)`

### Sources

- `corpus/koreai-orchestration-patterns.web.md` — figura `AA-network-pattern.webp`, transcripción completa; la caja `USER` aparece sin conector alguno; los seis agentes llevan la píldora `Orchestration` que los del patrón supervisor no tienen.

### Speaker notes

La única diferencia estructural entre las dos figuras es una fila: acá cada agente lleva `Orchestration`. La coordinación se replica en cada par en vez de vivir en un nodo. Eso compra latencia baja y menos idas y vueltas, y cuesta que cada agente tenga que saber enrutar y que nadie tenga la foto completa.

Señalar la caja `USER` arriba: está dibujada sin ningún conector. La figura nunca dice cómo entra un pedido a la malla. Los rótulos `Start Agent` y `Current Agent` dicen que "quién manda ahora" es una posición móvil y no un rol, que es la objeción de gobernanza a este patrón.

El grafo es parcial: `AGENT 1` y `AGENT 3` no están unidos, y `AGENT 6` cuelga solo de `AGENT 3`. No hay hub.

[Kore.ai](https://www.kore.ai/blog/choosing-the-right-orchestration-pattern-for-multi-agent-systems) desaconseja este patrón cuando la trazabilidad y el debugging son prioritarios. Vale subrayarlo porque es exactamente lo que la sección siguiente pide.

---

## 8. La tabla de decisión

### Content

| Dimensión | Supervisor | Red adaptativa | Custom |
|---|---|---|---|
| Estructura de control | Centralizada | Descentralizada | Programable |
| Latencia | Más alta | Más baja | Variable |
| Complejidad | Baja | Media | Alta |
| Uso de tokens | Alto | Optimizado | Depende |
| Mejor para | Workflows multi-dominio | Tiempo real o conversacional | Sistemas regulados o propietarios |
| Madurez de equipo | Mínima | Intermedia | Ingeniería AI avanzada |
| Esfuerzo de mantenimiento | Bajo | Medio | Alto |

Tres filas seguidas de la columna Supervisor: **Complejidad baja**, **Uso de tokens alto**, **Latencia más alta**. El patrón supervisor es el barato de construir y el caro de operar.

`Kore.ai, oct-2025 (act. jul-2026)`

### Sources

- `corpus/koreai-orchestration-patterns.web.md` — figura `implementation-recomendation.webp`, tabla completa transcrita verbatim (traducida al español acá, con los valores intactos); filas adyacentes `Complexity: Low`, `Token usage: High` y `Latency: Higher` en la columna del patrón supervisor. El registro del Librarian marca que el intercambio nunca se enuncia en el texto del artículo.

### Speaker notes

Es el artefacto más directamente reutilizable del corpus para esta audiencia: una tabla de decisión en vocabulario de negocio que responde "cuál elijo" sin una línea de código.

Advertencia de cita: son aserciones de un proveedor sin benchmark, sin unidades y sin fuente. Se presentan como guía de [Kore.ai](https://www.kore.ai/blog/choosing-the-right-orchestration-pattern-for-multi-agent-systems), no como medición. Lo mismo vale para el "más de 200%" de variación de tokens entre patrones que el artículo menciona sin base ni contexto de medición; conviene no llevarlo a lámina.

Leer las tres celdas del intercambio en voz alta y dejar que la sala arme la frase: cada salto pasa por el hub, así que sube la latencia; el orquestador relee contexto en cada ronda, así que sube el gasto de tokens. Es el mismo intercambio que el 15× de la lámina 2.5, ahora como propiedad de un patrón concreto. Para management: el costo de construcción se ve en el proyecto, el de operación aparece después, y la arquitectura se elige mirando el primero.

La columna `Custom` introduce una tercera opción que ninguna de las dos figuras anteriores dibuja. No hay diagrama de ella en el corpus, así que no corresponde dar a entender que se mostró una tercera arquitectura.

El remate de [Kore.ai](https://www.kore.ai/blog/choosing-the-right-orchestration-pattern-for-multi-agent-systems) conviene decirlo con sus palabras, porque es la regla que ordena la tabla entera: elegir el patrón más simple que cumpla el requisito del negocio. Con la lámina de síntesis fuera del deck, esta es la frase que la sala se lleva de la sección.

---

## 9. Un caso: cómo se descompone

### Content

Pedido: *«Cancelá el crédito del auto con la plata de mi caja de ahorro.»*

1. **El orquestador descompone** cuatro pasos: cotizar el saldo, verificar fondos, ejecutar la transferencia, generar la confirmación.
2. **Asigna tres especialistas** Loan Agent cotiza saldo, interés y penalidades. Transaction Manager verifica saldo, límites diarios y umbrales de fraude. Payment Processor ejecuta la transferencia.
3. **Corre dos en paralelo** Loan Agent y Transaction Manager a la vez; el Payment Processor arranca cuando los dos volvieron.

`Kore.ai, oct-2025 (act. jul-2026)`

### Sources

- `corpus/koreai-orchestration-patterns.web.md` — ejemplo "Supervisor — loan payoff in enterprise banking", pasos 1, 2, 3 y 5 verbatim.

### Speaker notes

**Original:** "Pay off my car loan using my savings account." — [Kore.ai, oct-2025](https://www.kore.ai/blog/choosing-the-right-orchestration-pattern-for-multi-agent-systems).

El mejor ejemplo del corpus para una audiencia de negocio: usa un proceso bancario que ya conocen.

Notar que el paralelismo acá es el del patrón supervisor de la lámina 2.6, y encaja con el criterio de la sección 2: cotizar el saldo y verificar los fondos son dos lecturas independientes. Ninguna de las dos escribe. La escritura (la transferencia) queda sola y al final.

Las dos decisiones de gobierno que este caso trae ya no tienen lámina propia y se dicen acá, sobre el dibujo.

La primera es el reparto del dato. El Loan Agent ve datos de préstamo enmascarados, el Transaction Manager ve saldo y umbrales de política sin datos del préstamo, y el Payment Processor ve identificadores seudonimizados sin datos personales identificables. Cada agente recibe solo su parte, y eso acota lo que puede exponer antes de que actúe. Aclarar que el identificador seudonimizado no tiene relación con los tokens que factura el proveedor del modelo, aunque la fuente en inglés use "tokenized" para las dos cosas.

La segunda es el momento de la validación, que ocurre antes de ejecutar la transferencia: que el saldo coincida con los fondos, que cumpla política y que la cotización siga vigente. Si algo no cierra, el orquestador replanifica. Es un gate, aunque acá lo pase una máquina y no una persona.

Y la bisagra hacia la sección 3, que también salió de lámina y sigue valiendo: el rastro de razonamiento y los detalles de la transacción quedan registrados para cumplimiento y auditoría. El registro es parte del patrón, no un agregado posterior.

Sigue siendo material de proveedor: no hay implementación mostrada ni cliente citado.

---

# 3. La Task

**Goal of this section:** Instalar la tesis de la clase. La Task es a la vez unidad de trabajo, registro de decisión y rastro de auditoría, y esa triple función vuelve gobernable a un equipo de agentes. La sección recorre la anatomía de la Task en un orden fijo: primero el dibujo, después la definición de cada pieza. Así dos veces, con el ciclo de vida y sus campos, y con la cadena de objetivos y sus cuatro niveles. Las dos figuras que la sección dibuja salen de maquetas de Paperclip y llevan su atribución: acá el producto entra como ilustración de la abstracción, no como el producto que la sección 4 recorre mecanismo por mecanismo. Al cerrar, la sección da el criterio con el que se juzga cualquier herramienta de orquestación, incluida esa.

---

## 1. Qué es una Task

### Content

Una Task es una unidad de trabajo con dueño único, estado, hilo de conversación y definición de terminado.

La clase la llama **Task**. El sitio de Paperclip la llama `ticket` y el newsletter de abril la llama `Issue`. Son tres nombres para la misma pieza.

- **Dueño único** Un solo agente responsable a la vez. Paperclip lo impone para evitar trabajo duplicado.
- **Estado que significa algo** in progress, blocked, in review, done. Una Task bloqueada nombra a su dueño y la acción que la desbloquea.
- **Hilo** La conversación de la tarea, escrita para el humano que la va a leer después.
- **Definition of done** Los criterios de aceptación que el trabajo tiene que cumplir antes de cerrar.

`Paperclip, ago-2026`

### Sources

- `corpus/paperclip-tasks.web.md` — "The unit of work in Paperclip is a task an agent owns — with a status, blockers, a thread, and a definition of done"; estados; "Blocked tasks name the owner and the unblock action".
- `corpus/aienterprise-run-company-agents.web.md` — "Only one agent can own a task at a time — enforced automatically to prevent duplicate work".

### Speaker notes

Esta lámina abre la sección y hereda el trabajo de bisagra que hacía la lámina anterior, cortada a pedido del presenter. Antes de definir nada conviene decir en voz alta de dónde viene el movimiento: las tres secciones anteriores contestaron **cómo se reparte el trabajo** y ninguna contestó las dos preguntas que un directorio hace primero. Quién autorizó esto: el patrón dice quién ejecuta, no quién aprobó. Cuánto costó: el multiplicador dice cuánto gasta, no a qué se le imputa. Las dos se contestan con la misma pieza, que es la que esta lámina define, y el resto de la clase se apoya en ella.

Buena parte de la sala trabaja con Jira o Asana y la palabra les es familiar; lo que hay que hacer explícito es que acá la Task no es un artefacto de seguimiento, es la interfaz por la que se le habla a un agente.

Nota de inconsistencia del corpus que conviene tener a mano: el ciclo de vida aparece dos veces con listas distintas. [El sitio de Paperclip](https://paperclip.ing/product/tasks/) nombra in progress / blocked / in review / done; [el newsletter de abril](https://www.theaienterprise.io/p/run-company-ai-agents-paperclip) reporta backlog → todo → in_progress → in_review → done. Ninguna es autoritativa.

---

## 2. Ciclo de vida de una Task

### Content

Paperclip nombra cuatro estados. `PARKED` y `CANCELLED` son rótulos de la clase para dos salidas que el producto documenta sin decir dónde cae el trabajo.

![Maquina de estados de una Task: las cuatro cajas del sitio mas PARKED y CANCELLED](images/s3-2-1-ciclo-vida-task.png)
<!-- ascii-source:
                (creado)
                    |
                    v
           +-----------------+   se traba    +---------------+
      +---&gt;|   IN PROGRESS   |--------------&gt;|    BLOCKED    |
      |    |                 |<--------------|               |
      |    +-----------------+  se destraba  +---------------+
      |       |     |     |                  nombra dueno y
      |       |     |     |                  accion de desbloqueo
      |       |     |     |  tope de gasto
      |       |     |     +-----------------&gt;[  PARKED  ]
      |       |     |                        el trabajo queda
      |       |     |                        estacionado
      |       |     |  un humano cancela
      |       |     +-----------------------&gt;[ CANCELLED ]
      |       |                              desde cualquier estado
      |       |
      |       | el agente entrega
      |       v
      |    +-----------------+
      |    |    IN REVIEW    |
      |    +-----------------+
      |       |           |
      |       |           | approve
      |       |           v
      |       |  +-----------------+
      |       |  |      DONE       |
      |       |  +-----------------+
      |       |
      +-------+
       request changes
-->
<!-- ascii-note:
intent: la maquina de estados de una Task: las cuatro cajas que nombra el sitio de Paperclip mas dos salidas documentadas cuyo estado resultante la fuente nunca nombra. blocked es un desvio del que se vuelve.
emphasize: las cuatro cajas canonicas (IN PROGRESS, BLOCKED, IN REVIEW, DONE) dibujadas todas iguales entre si; PARKED y CANCELLED con una convencion visual claramente distinta (contorno punteado y rotulo en gris, igual que (creado)), porque son rotulos de la clase y no nombres del producto; el par de flechas de ida y vuelta entre IN PROGRESS y BLOCKED; la vuelta larga de IN REVIEW a IN PROGRESS por request changes.
labels: (creado) es el arranque implicito y la fuente no lo nombra. IN PROGRESS, BLOCKED, IN REVIEW y DONE son los cuatro estados del sitio. PARKED y CANCELLED son etiquetas de la clase, dibujarlas distintas de las cuatro cajas canonicas. La flecha a CANCELLED sale de IN PROGRESS por legibilidad y el control aplica desde cualquier estado, que es lo que dice la anotacion "desde cualquier estado". De PARKED no sale flecha de vuelta porque la fuente no documenta el retorno. Aristas: se traba, se destraba, tope de gasto, un humano cancela, el agente entrega, request changes, approve.
-->

`Paperclip, ago-2026 · PARKED y CANCELLED, rótulos de la clase`

### Sources

- `corpus/paperclip-tasks.web.md` — "Statuses that mean something: in progress, blocked, in review, done"; "Blocked tasks name the owner and the unblock action"; "Agents hand finished work to QA with acceptance criteria; QA verifies with tests, screenshots, or a repro before anything closes"; "'Done' is a verdict, not a self-report".
- `corpus/paperclip-governance.web.md` — widget "Approval request" con los controles **Approve** y **Request changes**; "Deny with a note and the agent adjusts course"; "Pause, cancel, and rewind controls at every level" y "Pause or cancel anything mid-flight". Ninguna fuente dice en qué estado queda un ticket cancelado.
- `corpus/paperclip-budgets.web.md` — "When an agent reaches its cap it stops, marks its work with a clear state, and asks for more"; "Hard stops at the cap, with graceful hand-off"; el registro glosa ese hand-off como "the state transition at the cap, so the work is parked rather than abandoned". La fuente admite que hay un estado y nunca lo nombra. "Top-ups are an approval, not a config edit".
- `corpus/aienterprise-run-company-agents.web.md` — segunda lista de estados, incompatible con la del sitio: `backlog → todo → in_progress → in_review → done`.

### Speaker notes

El estado inicial no está nombrado en ninguna fuente. El sitio empieza a contar en `in progress`, así que `(creado)` marca en el dibujo el arranque del recorrido y no un valor del campo. Decirlo así si alguien pregunta por un backlog.

Los nombres `PARKED` y `CANCELLED` son de la clase, no de Paperclip: el sitio nombra cuatro estados y solo cuatro. Las dos salidas sí están documentadas. [La página de gobernanza](https://paperclip.ing/product/governance/) promete *«pausar, cancelar y revertir en todo nivel»* y [la de presupuestos](https://paperclip.ing/product/budgets/) dice que al llegar al tope el agente para y *«marca su trabajo con un estado claro»*. Ninguna de las dos dice cuál es ese estado. Decir el nombre y decir que es nuestro, en la misma frase.

Ahí hay material de gobernanza que conviene no pasar de largo: el producto promete cortar en cualquier nivel y no documenta dónde cae el trabajo cortado. Para un manager esa es la pregunta operativa, porque de ella depende quién retoma el trabajo y con qué presupuesto.

La flecha a `CANCELLED` sale de `IN PROGRESS` para que el dibujo se lea, pero el control aplica desde cualquier estado. La anotación al lado de la caja lo dice.

De `PARKED` no sale ninguna flecha de vuelta porque la fuente no documenta el retorno. Lo que sí dice el sitio es que subir el tope es una aprobación, no una edición de configuración, así que la respuesta honesta a "¿cómo se retoma?" es que alguien aprueba más presupuesto y el corpus no describe qué pasa después.

Inconsistencia del corpus que conviene tener a mano: el sitio de Paperclip nombra in progress / blocked / in review / done, y el newsletter de abril reporta backlog → todo → in_progress → in_review → done. Las dos listas no coinciden y ninguna es autoritativa. El deck usa la del sitio por ser fuente primaria y de agosto, y la lámina 3.1 ya la fijó.

`blocked` no es una etapa del recorrido. Una Task entra y sale de ahí sin avanzar, y mientras está bloqueada nombra a su dueño y la acción que la destraba, así que ningún trabajo queda parado sin responsable.

La vuelta de in review a in progress sale de los dos controles que ofrece la tarjeta de aprobación del sitio: Approve y Request changes. Negar con una nota devuelve el trabajo con dirección. La tarjeta entera se ve en la lámina 4.7.

Antes de cerrar, alguien verifica el trabajo contra los criterios escritos; la fuente habla de evidencia adjunta. Quién verifica en la maqueta del sitio es otro agente, `Vera · QA · claude`, y ese punto se cobra en la lámina 4.4.

Pregunta útil para la sala: en su organización, ¿qué transición de este dibujo tendría que requerir una firma humana? La respuesta es una decisión de gobierno y el producto solo la ejecuta.

---

## 3. Campos principales de una Task

<!-- format: editorial -->

### Content

En el tablero, una Task se ve así: `PAP-1043 · QA pass on new routes · Blocked by 1042`. Cada campo de adentro habilita una decisión distinta.

- **Clave** El identificador con el que una aprobación, un log o una Task bloqueada nombran ese trabajo.
- **Asignado** Un agente responsable por vez. Quien quiera pausar o cancelar una corrida apunta a ese nombre.
- **Estado** Un manager recorre el trabajo por ese campo, sin abrir ninguna Task.
- **Definition of done** Se escriben antes de empezar, y los verifica alguien distinto del que trabajó.
- **Hilo** El agente escribe qué pasó, dónde está el trabajo y qué sigue. Es lo que un auditor lee después.
- **Costo** Cada corrida registra comandos, commits, comentarios y costos. Cada tarea deja su recibo.

`Paperclip, ago-2026 · mock-up`

### Sources

- `corpus/paperclip-tasks.web.md` — "Every task has one accountable agent, a live status, and a thread that doubles as the record"; tablero PAP-1041…1044 con sus tres columnas; "QA handoffs with explicit acceptance criteria" y evidencia adjunta (tests, screenshots, links); "Agents update their tickets the way you wish your teammates did: what happened, where the work is, what's next, with links"; "Threads written for the human reading them later".
- `corpus/paperclip-governance.web.md` — "Each run records what the agent read, decided, and did — commands, commits, comments, costs"; "Pause or cancel anything mid-flight".
- `corpus/paperclip-product.web.md` — widget "Issues — website team" con las columnas Key, Title y Status; solución Finance: "every agent operates under a hard budget cap, and every task carries a receipt".
- `corpus/aienterprise-run-company-agents.web.md` — inventario de campos del issue: "Each issue has a title, description, status, priority, and one assignee"; "Only one agent can own a task at a time — enforced automatically to prevent duplicate work".

### Speaker notes

Tres precisiones que salieron del cuerpo de lámina para que los seis campos entren, y que conviene decir en voz alta. El **Estado** es la tercera columna del tablero, junto a la clave y el título. En el **Hilo**, el agente deja además los links. Y sobre la **Definition of done**: sin criterios escritos, «terminado» lo declara el propio agente, que es exactamente lo que la lámina 3.8 va a llamar el problema.

La lámina 3.1 nombró los cuatro campos que un directorio mira y la 3.2 dibujó el recorrido del estado. Esta abre la Task y muestra qué se escribe adentro de cada campo y qué decisión habilita, que es el nivel al que un manager tiene que bajar antes de delegar nada.

[El newsletter de abril](https://www.theaienterprise.io/p/run-company-ai-agents-paperclip) enumera dos campos que el sitio no nombra: descripción y prioridad. La prioridad figura en la lista de campos y en ningún lado del material capturado se explica cómo la usa el agente cuando elige trabajo en un heartbeat. Decirlo como hueco si alguien pregunta.

Distinción que se presta a confusión: los seis valores active, idle, running, error, paused y terminated son el estado del **agente**. La Task tiene los cuatro que dibujó la lámina 3.2.

El presupuesto mensual de gasto también es un campo del agente. Lo que la Task lleva es el costo de sus corridas, y esa es la pieza que contesta a qué se le imputa el gasto.

El campo que más se saltea en la práctica es la definition of done. Sirve preguntar a la sala quién escribe criterios de aceptación antes de delegarle una tarea a una persona; con agentes el hueco se paga más rápido.

La fuente pide además que el trabajo terminado llegue con evidencia adjunta. Para esta clase alcanza con el punto de gestión: el que cierra no es el que hizo el trabajo. Paperclip lo dice en una línea, *«"terminado" es un veredicto, no una autodeclaración»*.

La clave `PAP-1043` sale del tablero de demostración del sitio, que es una maqueta. La forma es lo que enseña; las Tasks son ilustrativas.

---

## 4. Subtasks: el trabajo se define partiéndolo

### Content

Aprobado un plan, Paperclip lo abre en Tasks hijas con dependencias de bloqueo, y ese árbol pasa a ser la vista del proyecto.

- **Orden explícito** Las ramas independientes corren a la vez. La que depende de otra espera a que su bloqueo cierre.
- **Bloquea / bloqueado por** `PAP-1042 Build feature pages` está en curso y `PAP-1043 QA pass on new routes` figura como `Blocked by 1042`. Cualquiera que mire el tablero ve qué rama avanza y cuál espera.
- **El progreso sube por el árbol** Cada rama que cierra actualiza el avance del padre, sin que nadie consolide un reporte.
- **Cada delegación es una Task** Un agente manager toma un objetivo, lo parte y asigna cada pedazo. La entrega queda como issue enlazado y auditable.

El árbol deja escrito el reparto que la sección 2 decidió en abstracto. Repartir el trabajo y auditarlo pasan a ser la misma operación.

`Paperclip, ago-2026 · mock-up`

### Sources

- `corpus/paperclip-tasks.web.md` — "Approve a plan and it fans out into child issues with blocking dependencies — ordered where order matters, parallel where it doesn't. The tree is the project view: you can see exactly which branch is moving and which is waiting on what"; "Progress rolls up the tree automatically"; tablero con `PAP-1043 QA pass on new routes — Blocked by 1042`.
- `corpus/paperclip-org-chart.web.md` — "A manager agent takes a goal, breaks it into a tree of child issues with blocking dependencies, and assigns each piece to the teammate best suited to it. Parallel tracks run in parallel; ordered work waits on its blockers"; "Every delegation is a linked, auditable issue".
- `corpus/aienterprise-run-company-agents.web.md` — "Issues nest under parent issues, creating a traceable chain back to the company goal".

### Speaker notes

**Original:** "Approve a plan and it fans out into child issues with blocking dependencies — ordered where order matters, parallel where it doesn't." · "Every delegation is a linked, auditable issue." — paperclip.ing, agosto 2026: [Tasks](https://paperclip.ing/product/tasks/) y [Org Chart](https://paperclip.ing/product/org-chart/).

El punto de gestión que hay que hacer explícito: el árbol es el formato en el que se define el trabajo. Un plan en prosa dice qué se quiere. El árbol dice qué Tasks existen, quién tiene cada una y cuál espera a cuál.

Ahí se cierra el arco de la sección 2. Allá la pregunta era si conviene repartir y con qué forma; acá el reparto ya tomó forma de objeto con dueño y rastro, y por eso se puede auditar sin reconstruir nada.

El ejemplo PAP-1042 / PAP-1043 aparece en cuatro registros del corpus (tasks, product, org-chart y governance) siempre igual. Es la maqueta del sitio, así que enseña la forma de la relación y no un caso real.

Lo que el corpus deja sin resolver: si la delegación puede ir de costado. El newsletter reporta un árbol estricto, con cada agente reportando a exactamente un manager salvo el CEO; el sitio habla de trabajo que se enruta al especialista adecuado y de pedidos entre equipos. Vuelve en la lámina 4.3.

Si alguien pregunta qué pasa cuando el plan cambia: la aprobación se resetea y nada se vuelve a asignar hasta que hay una revisión aprobada. Ese mecanismo se ve en la lámina 4.7.

---

## 5. Missions y linaje de objetivos

### Content

El trabajo huérfano, el que no sirve a ningún objetivo, queda marcado.

![Cadena de objetivos de cuatro niveles, de la mision a la Task](images/s3-5-1-linaje-objetivos.png)
<!-- ascii-source:
   (@)  MISSION        Make $1mm ARR with the #1 AI note-taking app
         |
         v
   (O)  PROJECT GOAL   Ship collaboration features
         |
         v
   (o)  AGENT GOAL     Implement real-time sync
         |
         v
    .   TASK           Write WebSocket handler for document updates
-->
<!-- ascii-note:
intent: la cadena de objetivos de cuatro niveles; cada tarea puede rastrearse hacia arriba hasta la mision de la compania.
emphasize: la cadena vertical completa sin saltos; los cuatro rotulos de nivel (MISSION, PROJECT GOAL, AGENT GOAL, TASK) y el tamano decreciente de los marcadores.
labels: MISSION, PROJECT GOAL, AGENT GOAL, TASK.
-->

`Paperclip, ago-2026 · mock-up`

### Sources

- `corpus/paperclip-home.web.md` — cadena de objetivos de demostración verbatim, con los cuatro niveles y sus marcadores; "Every piece of work is given context that traces back to the company mission".
- `corpus/paperclip-tasks.web.md` — "Orphaned work — effort serving no goal — gets flagged"; los agentes citan el objetivo que sirve una tarea al tomarla.

### Speaker notes

Segunda vez que la sección dibuja antes de definir: la 3.2 mostró el recorrido de estados y la 3.3 abrió los campos; acá el dibujo va primero otra vez y la 3.6 nombra los cuatro niveles uno por uno. Decirlo en voz alta ayuda, porque la sala reconoce el patrón y sabe que la definición viene enseguida.

El linaje de objetivos separa el Nivel 2 del Nivel 3 de la escalera de la lámina 1.8. Sin él hay agentes especializados corriendo en paralelo; con él hay una compañía.

El detalle operativo interesante: el agente cita el objetivo que sirve la tarea cuando la toma. Eso convierte la alineación en un dato registrado y no en una intención.

"Orphaned work gets flagged" implica un detector automático cuyo mecanismo no aparece descrito en ningún lado del material capturado. Vale decirlo como lo que es, una afirmación sin mecanismo.

Los cuatro renglones del ejemplo son la maqueta [del sitio](https://paperclip.ing/).

---

## 6. Qué es una mission y qué es un goal

### Content

Cada nivel de la cadena nombra una cosa distinta, y uno solo lo escribe una persona.

- **Mission** El objetivo de la compañía. Lo escribe un humano; el agente CEO lo descompone hacia abajo. `Make $1mm ARR with the #1 AI note-taking app`
- **Project goal** El resultado en el que esa mission se descompone, y que agrupa trabajo de varios agentes. `Ship collaboration features`
- **Agent goal** La porción de ese resultado que un agente toma como suya y cita al levantar la tarea. `Implement real-time sync`
- **Task** La unidad de trabajo, con su dueño, su estado y su rastro. Es el nivel donde el trabajo se ejecuta. `Write WebSocket handler for document updates`

`Paperclip, ago-2026 · mock-up`

### Sources

- `corpus/paperclip-home.web.md` — cadena de objetivos de cuatro niveles con sus marcadores, `Mission (◎) → Project Goal (◉) → Agent Goal (○) → Task (•)`, y el ejemplo de la maqueta verbatim; "Every piece of work is given context that traces back to the company mission. Your agents will know *what* to do and *why*"; "Projects are groups of work".
- `corpus/aienterprise-run-company-agents.web.md` — Company como unidad de más arriba, que contiene la mission: "You define a mission, set a monthly budget, and build an org below it"; "A CEO agent interprets a company mission, decomposes it into projects, assigns work down an org chart, and escalates blockers up to you — the human board. Every task at every level traces back to the mission"; "Issues nest under parent issues, creating a traceable chain back to the company goal".
- `corpus/paperclip-tasks.web.md` — la misma escalera contada en tres niveles: "Set a company goal — grow installs, cut the support backlog, ship the migration — and managers decompose it into sub-goals for their teams"; "Each agent sees its slice and cites the goal a task serves when it takes it, so effort stays pointed at an outcome instead of drifting into busywork"; widget "Goals — Q3" con `Company goal | Grow weekly active installs 20% | 64%`.
- `corpus/github-paperclip-repo.web.md` — "Every task traces back to the company mission. Agents know what to do and why", reportada desde el README; el registro la marca como copy de producto genuino porque la misma frase es el texto de la feature Goal Alignment en el sitio.

### Speaker notes

Promesa del producto que la lámina ya no muestra en cuerpo, cortada a pedido del presenter, y que conviene tener a mano si la sala pregunta qué se gana con escribir la cadena entera: "Every piece of work is given context that traces back to the company mission. Your agents will know *what* to do and *why*." — [paperclip.ing, agosto 2026](https://paperclip.ing/).

Company y mission no son lo mismo, y conviene decirlo apenas se nombran. La Company es la entidad de más arriba, con su presupuesto mensual y su organigrama colgando; la mission es el enunciado que esa Company se fija. Un mismo deployment puede correr varias companies con datos aislados entre sí.

Conflicto de fuentes que la clase resuelve por decisión propia: el sitio cuenta cuatro niveles (Mission / Project Goal / Agent Goal / Task) y la página de tasks cuenta tres (company goal, sub-goals por equipo, y el goal que el agente cita al tomar la tarea). No son la misma lista. El deck usa la de cuatro porque es la que el sitio dibuja y la que la lámina anterior acaba de mostrar. Mismo criterio que con las dos listas de estados de la lámina 3.2.

Los goals llevan porcentaje de avance: el widget de la página de tasks muestra un company goal al 64%. Ese widget pertenece a la lista de tres niveles, así que no conviene pegarle ese número a un project goal en lámina.

La frase citada aparece idéntica en el sitio y en la reconstrucción del [README del repositorio](https://github.com/paperclipai/paperclip). Son dos capturas separadas, así que el Librarian la marcó como copy de producto genuino; la reconstrucción del README es de segunda mano y no está verificada byte a byte, y eso conviene decirlo si alguien pregunta de dónde sale.

La decisión de gestión que deja esta lámina: el único nivel que escribe una persona es la mission. Todo lo de abajo lo derivan agentes, así que una mission mal escrita produce una cadena entera de objetivos mal escritos, y el error recién se ve en las tareas.

La cadena ya se vio entera en la 3.5, con el diagrama de la maqueta y el trabajo huérfano. Esta lámina no la vuelve a contar: nombra cada nivel y dice quién lo escribe. Si el tiempo aprieta, la 3.5 se muestra y esta se recorre leyendo solo los cuatro rótulos en negrita.

---

## 7. Qué es un audit trail

### Content

Un audit trail es el registro append-only de lo que pasó: qué leyó cada agente, qué decidió, qué ejecutó, con qué costo y en qué momento.

- **Append-only** Se agrega, no se edita ni se borra.
- **Por corrida** Comandos, commits, comentarios y costos de cada ejecución.
- **Para qué sirve** Responder "quién autorizó esto" con un link y no con una excavación.

`Paperclip, ago-2026`

### Sources

- `corpus/paperclip-home.web.md` — "Immutable audit log. Append-only history. No edits, no deletions. Full accountability."
- `corpus/paperclip-governance.web.md` — "Each run records what the agent read, decided, and did — commands, commits, comments, costs"; "the answer is a link, not an archaeology project".

### Speaker notes

Advertencia técnica que vale decir en clase, porque es exactamente el tipo de matiz que un MiM tiene que aprender a detectar: en un deployment self-hosted sobre Postgres, la inmutabilidad es una política, no una propiedad criptográfica. Nada en el material capturado describe evidencia de manipulación. "Append-only" describe cómo se usa la tabla, no una garantía sobre quién puede tocarla.

Para el negocio: un audit trail sirve si alguien lo lee. La pregunta útil es quién en la organización lo revisa y cada cuánto.

---

## 8. La Task hace tres trabajos a la vez

### Content

![La Task sostiene tres funciones a la vez: unidad de trabajo, registro de decision y rastro de auditoria](images/s3-8-1-task-tres-trabajos.png)
<!-- ascii-source:
                     +--------------------------------+
                     |              TASK              |
                     +--------------------------------+
                     |  dueno unico                   |
                     |  estado                        |
                     |  hilo de conversacion          |
                     |  definition of done            |
                     +--------------------------------+
                        |            |            |
                        v            v            v
          +----------------+ +--------------+ +------------------+
          | UNIDAD DE      | | REGISTRO DE  | | RASTRO DE        |
          | TRABAJO        | | LA DECISION  | | AUDITORIA        |
          |                | |              | |                  |
          | quien hace que | | que se pidio | | que leyo, decidio|
          | y que esta     | | y quien lo   | | y ejecuto, con   |
          | bloqueado      | | aprobo       | | costo y hora     |
          +----------------+ +--------------+ +------------------+
-->
<!-- ascii-note:
intent: una sola pieza (la Task) sostiene tres funciones distintas de la organizacion; es la tesis de la charla dibujada.
emphasize: que las tres cajas de abajo cuelgan del MISMO objeto de arriba; los cuatro campos de la Task como origen de las tres funciones.
labels: TASK, UNIDAD DE TRABAJO, REGISTRO DE LA DECISION, RASTRO DE AUDITORIA.
-->

Sin esa pieza hay agentes actuando. Con ella hay una organización que se puede inspeccionar y frenar.

### Sources

- `corpus/paperclip-tasks.web.md` — el ticket como unidad de trabajo con dueño, estado, hilo y definition of done; "a thread that doubles as the record".
- `corpus/paperclip-home.web.md` — el ticket como canal de comunicación y a la vez registro: "Every instruction, every response, every tool call and decision is recorded with full tracing".
- `corpus/paperclip-heartbeats.web.md` — "Task threads double as the audit log".
- `corpus/koreai-orchestration-patterns.web.md` — "The reasoning trace and transaction details are logged for compliance and audit purposes" como propiedad del patrón, no como agregado.

### Speaker notes

Es la lámina central de la clase. Dedicarle tiempo.

El argumento: en una organización humana estas tres funciones viven en artefactos distintos. El trabajo está en el tablero, la decisión en un mail o una reunión, la auditoría en un sistema aparte que alguien completa después. Con agentes las tres colapsan en el mismo objeto, porque el agente escribe su propio hilo mientras trabaja.

La consecuencia práctica para un manager: la calidad del gobierno depende de la calidad de la Task. Una Task sin dueño no tiene a quién frenar; sin estado no se sabe qué está pasando; sin hilo no hay qué auditar.

Cuatro registros del corpus dicen la misma cosa con palabras distintas, y uno de ellos es de un proveedor que no vende Paperclip ([Kore.ai](https://www.kore.ai/blog/choosing-the-right-orchestration-pattern-for-multi-agent-systems)). Esa coincidencia entre fuentes que compiten es lo más cerca que llega el corpus a una validación.

---

## 9. La prueba de la orquestación

### Content

Un sistema de agentes se puede llamar gobernado si tiene respuesta para las tres preguntas:

1. **¿Cómo se bloquea una acción antes de que ocurra?** Approval gates sobre las acciones que la organización designe.
2. **¿Cómo queda registrada?** Rastro por corrida, con costo y con la persona que aprobó.
3. **¿Cómo se detiene lo que ya está corriendo?** Pausa y cancelación en cualquier nivel.

`Paperclip, ago-2026`

### Sources

- `corpus/paperclip-governance.web.md` — approval gates; per-run logs con comandos, commits, comentarios y costos; "Pause, cancel, and rewind controls at every level"; el registro del Librarian marca que *rewind* aparece una sola vez, nunca se define y ningún otro registro lo menciona.

### Speaker notes

Es el criterio con el que la audiencia puede juzgar cualquier producto de orquestación, incluido el que viene en la sección siguiente. Las tres preguntas se aplican en sala a la herramienta que alguien esté evaluando.

Corrección deliberada al material fuente que la lámina ya no lleva en cuerpo y que conviene decir de palabra: hay una cuarta pregunta —cómo se revierte lo ya ejecutado— que no tiene respuesta seria para acciones externas, porque un post publicado o un mail enviado no se deshacen. [La página de gobernanza de Paperclip](https://paperclip.ing/product/governance/) lista "Pause, cancel, and rewind controls at every level". La palabra *rewind* aparece una sola vez en todo el corpus, no se define en ningún lado, e implica deshacer efectos ya ejecutados afuera, que para una publicación o un mail no es creíble. Marcarlo acá enseña el hábito que la clase quiere dejar: leer el material de un producto contra sí mismo, y desconfiar de la palabra que aparece una sola vez y nunca se define.

Si alguien pregunta por qué importa la distinción entre bloquear y detener: bloquear ocurre antes de la acción y es barato; detener ocurre durante y deja trabajo a medias que alguien tiene que limpiar.

---

# 4. Controles de Paperclip

**Goal of this section:** Recorrer los mecanismos con los que Paperclip gobierna un equipo de agentes (organigrama, heartbeats, presupuestos, aprobaciones), cada uno amarrado al problema abstracto que responde. Los objetivos y la Task ya quedaron instalados en la sección 3, así que acá se dan por sabidos. La plataforma que corre por debajo queda para la sección 5.

---

## 1. Qué es Paperclip

### Content

Paperclip es una capa de gestión sobre agentes que ya existen. No provee el modelo ni el runtime: administra los que se traigan.

- **Control plane** Administra agentes sin importar cómo fueron construidos.
- **Framework** Define cómo se construyen los agentes, qué roles toman y cómo se pasan el trabajo. CrewAI es un framework; Paperclip no.
- **Cómo llega** MIT, self-hosted, `npx paperclipai onboard --yes`. Versión capturada: v2026.817.0, 17 de agosto de 2026.

`The AI Enterprise, abr-2026` · `Paperclip, ago-2026`

### Sources

- `corpus/aienterprise-run-company-agents.web.md` — distinción control plane / framework, verbatim; CrewAI como framework complementario vía adapter HTTP.
- `corpus/paperclip-bring-your-own-agent.web.md` — "Paperclip is a workforce layer, not a model".
- `corpus/paperclip-home.web.md` — comando de instalación; release v2026.817.0.

### Speaker notes

La distinción control plane contra framework es la más limpia del corpus y vale que la audiencia se la lleve, porque ordena todo el mercado de herramientas de agentes en dos categorías.

Analogía de management: el framework decide cómo se contrata y se entrena a la gente; el control plane es el organigrama, el presupuesto y el sistema de aprobaciones que existe por encima, con independencia de dónde vino cada persona.

Las dos palabras que quedan sin desplegar acá son runtime y self-hosted. `self-hosted` se define en la sección 5. `runtime` **ya no tiene lámina propia**: se sacó por decisión del presenter, así que hay que definirlo hablando, acá, la primera vez que aparece. La frase que funciona: el runtime es el programa que de verdad ejecuta al agente, el que habla con el modelo y corre las herramientas; Paperclip reparte el trabajo, mide el gasto y guarda el rastro, pero no ejecuta nada.

[El newsletter de abril](https://www.theaienterprise.io/p/run-company-ai-agents-paperclip) reporta que CrewAI mueve 1.400 millones de automatizaciones agénticas en organizaciones como PwC, IBM, Capgemini y NVIDIA, atribuido a Insight Partners a través del newsletter. Es una cifra de tercera mano; si se usa, decir la cadena.

---

## 2. Org Chart

### Content

Los agentes tienen rol, título, línea de reporte y descripción de puesto. Las instrucciones del rol persisten en cada tarea que el agente toma.

![Organigrama de agentes de un equipo de marketing de contenidos](images/s4-2-1-org-chart-agentes.png)
<!-- ascii-source:
  CEO  (claude_local)
  Mision: Grow newsletter to 50K subscribers
   |
   +-- CMO  (claude_local)      Strategy and campaign planning
   |    |
   |    +-- Content Writer  (claude_local)   heartbeat cada 4h
   |    +-- SEO Analyst     (claude_local)   heartbeat cada 8h
   |    +-- Social Manager  (process)        heartbeat cada 12h
   |
   +-- CTO  (openclaw_gateway) Site performance and tooling
        |
        +-- Dev Agent  (codex_local)         Bug fixes and feature work
-->
<!-- ascii-note:
intent: organigrama de agentes de un caso real de marketing de contenidos; cada agente conoce su rol, su manager y la mision de la compania.
emphasize: la mision escrita arriba de todo, de la que cuelga el arbol entero; el runtime entre parentesis en cada caja, distinto por agente; las cadencias de heartbeat en las hojas.
labels: CEO, CMO, CTO, Content Writer, SEO Analyst, Social Manager, Dev Agent; runtimes claude_local, process, openclaw_gateway, codex_local.
-->

`The AI Enterprise, abr-2026`

### Sources

- `corpus/aienterprise-run-company-agents.web.md` — organigrama de marketing de contenidos, verbatim, con misión, runtimes y cadencias de heartbeat.
- `corpus/paperclip-org-chart.web.md` — "An org chart, not a chat window"; el rol carga instrucciones permanentes: "you brief a position once instead of re-prompting a chatbot forever"; roles y modelos desacoplados.

### Speaker notes

La idea de management que hay que hacer explícita: se instruye un puesto una vez, en vez de reinstruir un chatbot cada sesión. Es la diferencia entre una descripción de puesto y una conversación.

Los runtimes entre paréntesis son distintos por agente en el mismo árbol, y es el primer uso concreto del término en un ejemplo. Como `runtime` ya no tiene lámina de definición, conviene repetir la frase corta: es el programa que ejecuta al agente. El Social Manager corre con el adapter `process`, que ejecuta comandos de shell, así que ni siquiera es un LLM. `adapter` tampoco tiene ya lámina de definición y pide la misma frase corta: es el puente entre Paperclip y el programa que corre al agente; sin adapter, un agente del organigrama es apenas un registro en una base de datos. El organigrama admite trabajo automatizado clásico como empleado.

Los roles y los modelos están desacoplados: se cambia el modelo detrás de un rol sin reescribir el puesto. Para un manager eso es una perilla de costo, y vuelve en la lámina de Budgets.

Punto que el corpus deja sin resolver: [el newsletter](https://www.theaienterprise.io/p/run-company-ai-agents-paperclip) reporta un árbol estricto, con cada agente reportando a exactamente un manager salvo el CEO. La página del sitio habla de trabajo que "se enruta al especialista adecuado" y de pedidos entre equipos, que sugiere ruteo cruzando el árbol. Si delegar puede ir de costado, no está establecido.

---

## 3. Qué es un heartbeat

### Content

Un heartbeat es la señal que despierta a un agente. Los agentes no corren de forma continua: despiertan, revisan su trabajo, actúan y vuelven a dormir.

- **Wakes por evento** tarea asignada, comentario nuevo, bloqueo liberado, revisión pedida.
- **Wakes agendados** un tick de reloj para rutinas y trabajos permanentes.
- **El payload trae el delta** el cambio que disparó el wake llega con la señal, así el agente no relee la historia.
- **La misma perilla mueve dos cosas** Más heartbeats es más progreso sin nadie mirando, y también más gasto. La cadencia es la decisión, y ninguna página del producto la presenta como tal. `Paperclip, ago-2026` · `The AI Enterprise, abr-2026`

`Paperclip, ago-2026`

### Sources

- `corpus/paperclip-heartbeats.web.md` — tipos de wake; "Wake payloads carry the delta, so no time is lost re-reading history"; la página vende el heartbeat como progreso 24/7 y nunca menciona costo.
- `corpus/aienterprise-run-company-agents.web.md` — "This is what keeps costs predictable and prevents runaway loops": el heartbeat descrito como mecanismo de control de costos.
- `corpus/paperclip-home.web.md` — "If it can receive a heartbeat, it's hired", enunciado dos veces.

### Speaker notes

Término técnico que la audiencia necesita antes de la lámina siguiente. La analogía útil: es el turno de trabajo, no el contrato.

El cuarto punto es el que hay que decir en voz alta y no dejar picando. Dos fuentes describen el heartbeat de maneras distintas: [la página](https://paperclip.ing/product/heartbeats/) lo vende como característica de productividad (progreso 24/7) y el newsletter como el mecanismo que mantiene el costo predecible. Las dos lecturas son compatibles, y la conclusión es que subir la cadencia compra progreso y cuesta plata. Ninguna página del producto lo dice.

Para el manager: la cadencia de heartbeat es una decisión de presupuesto disfrazada de configuración técnica.

Detalle menor y honesto: "agents don't poll and they don't idle" convive con "scheduled heartbeats… or simply because time passed". Un tick agendado sin nada que hacer es un poll. La distinción real es sobre el payload, no sobre el agendamiento.

---

## 4. Una noche sin nadie mirando

<!-- template: timeline -->

### Content

1. **02:10** `issue_assigned` · un agente toma la Task PAP-1041
2. **02:14** resuelve la Task
3. **02:19** lo entrega a revisión
4. **02:31** otro agente lo aprueba con la evidencia adjunta
5. **07:00** heartbeat agendado · redacta el brief diario

`Paperclip, ago-2026 · mock-up`

### Sources

- `corpus/paperclip-heartbeats.web.md` — widget "Activity — overnight", cinco eventos verbatim con sus horarios: `02:10 issue_assigned · picked up PAP-1041`, `02:14 implemented fix, tests passing`, `02:19 opened PR #212, handed to QA`, `02:31 QA verified · screenshots attached`, `07:00 heartbeat · daily brief drafted`. El registro anota además que "the overnight-activity widget shows an agent QA-ing another agent's work". El registro rotula los visuales de la página como "Re-tabulated UI mock-ups".
- `corpus/paperclip-tasks.web.md` — el organigrama de demostración muestra `Vera · QA · claude`, es decir un agente en el rol de QA.

### Speaker notes

Acá se cobra la promesa que la sección 3 dejó planteada — «terminado» es un veredicto, no algo que el agente se autoproclama — y conviene decir el remate con todas las letras: entre las 02:10 y las 02:31 no hubo una sola persona despierta. Un agente hizo el trabajo y otro agente lo aprobó.

Quién aprueba a las 02:31 tiene nombre en [la maqueta del propio sitio](https://paperclip.ing/product/heartbeats/): `Vera · QA · claude`, es decir un agente corriendo sobre claude. Aprobado por un agente no es aprobado por un humano, y el material de producto no distingue las dos cosas en ningún lado. Es la grieta del "Done is a verdict, not a self-report".

La evidencia que la Task lleva adjunta son capturas de pantalla, según el mismo widget. El detalle no va a lámina porque el punto de la clase no es qué tipo de evidencia se adjunta, sino quién la mira.

Es un mock-up de la página de producto, no la captura de un deployment real. Decirlo.

Si la sala pregunta cómo se arregla: el gate humano de la lámina 4.7 es la respuesta, y hay que configurarlo a propósito.

---

## 5. Estado persistente entre heartbeats

### Content

La Task sostiene el trabajo cuando el agente se apaga.

- **Cada wake termina en progreso durable** un commit, un comentario, un documento, o un bloqueo marcado con dueño.
- **El hilo de la Task es el estado** Al abrir el tablero a la mañana se lee lo que pasó, sin reconstruirlo.
- **Los planes se vuelven árboles** Un plan aprobado se abre en tareas hijas con dependencias explícitas; el progreso sube por el árbol solo.
- **Watchdog** Si una corrida se cuelga, entra en loop o muere callada, diagnostica el punto de parada y reinicia o escala.

`Paperclip, ago-2026`

### Sources

- `corpus/paperclip-heartbeats.web.md` — progreso durable como resultado obligado de cada wake ("a commit, a comment, a document, or a clearly-marked blocker with an owner"); "you read what happened — you don't reconstruct it"; "Task threads double as the audit log"; watchdogs con detección de stalls y loops; "Escalations name the exact stop point, not just 'it failed'".
- `corpus/paperclip-tasks.web.md` — planes que se abren en árboles de tareas hijas con dependencias de bloqueo; el progreso sube por el árbol.

### Speaker notes

Acá se cierra el arco que arrancó en la sección 2 con el límite de la ventana de contexto. La salida habitual es comprimir el historial con un modelo dedicado, que es difícil de calibrar. Paperclip lo resuelve por otro lado: el estado no vive en la ventana de contexto del agente, vive en la Task, y el agente lo vuelve a levantar en el próximo wake.

Es la respuesta más elegante del corpus a la regla de la lámina 2.3, y también una respuesta parcial. Dos agentes despertados sobre el mismo árbol siguen sin poder ver el razonamiento en vuelo del otro. El hilo de la Task comparte lo que ya se escribió, no lo que se está pensando.

Existe una formulación más fuerte de esto, "agents resume the same task context across heartbeats instead of restarting from scratch", que viene de la reconstrucción a mano del [README](https://github.com/paperclipai/paperclip) (GitHub devolvió 403) y no está verificada. La lámina usa en su lugar la formulación capturada de la página de heartbeats. Si se dice la del README, decirla como reportada.

El watchdog es la afirmación técnicamente más interesante y la menos especificada: cómo se distingue un loop de trabajo legítimo lento no se describe en ningún lado.

---

## 6. Budgets

### Content

Cada agente tiene un presupuesto mensual con tope. Cada tarea queda medida.

| Agente | Función | Usado / Tope | Utilización |
|---|---|---|---|
| Atlas | CTO | $186 / $300 | 62% |
| CodexCoder | Eng | $184 / $250 | 74% |
| Vera | QA | $57 / $150 | 38% |
| Scribe | Content | $91 / $100 | **91%** |

Subir un tope es una aprobación, no un cambio de configuración.

`Paperclip, ago-2026 · mock-up`

### Sources

- `corpus/paperclip-budgets.web.md` — widget "Budgets — July", cuatro filas verbatim con usado y tope; el registro rotula los visuales de la página como "Re-tabulated UI mock-ups" y aclara que las cifras en dólares son ilustrativas; "Top-ups are an approval, not a config edit"; "AI spend should look like payroll, not like a surprise".
- `corpus/paperclip-home.web.md` — aviso suave al 80% de utilización y auto-pausa al 100%.
- Derivación de la columna Utilización (no está en la fuente): 186/300 = 62%; 184/250 = 73,6% ≈ 74%; 57/150 = 38%; 91/100 = 91%.

### Speaker notes

Decir que son cifras de maqueta antes de que alguien las anote como referencia de mercado. Lo que enseña la tabla es la forma (tope por agente, medición por tarea), no los montos.

La columna de utilización está calculada acá, no viene en el mock-up del sitio. Los cuatro valores usado/tope sí son verbatim.

Scribe está en 91%, por encima del umbral de aviso suave del 80% que documenta la página principal. Sirve para mostrar en la misma tabla cómo se ve un agente cerca del tope.

La frase que vale para management: el gasto de AI tendría que parecerse a la nómina y no a una sorpresa. Es la traducción exacta del problema que abrió la clase.

"Top-ups are an approval, not a config edit" es la propiedad de gobernanza más interesante de esta página: aumentar el presupuesto es a su vez una decisión gobernada. Aparece solo acá en todo el corpus.

Sobre si el tope realmente frena, la formulación honesta: frena en el borde de la tarea, no adentro de una llamada en curso. [El FAQ del propio sitio](https://paperclip.ing/) dice que al 100% el agente se auto-pausa y se bloquean las tareas nuevas, y un tercero fechado en abril de 2026 reporta que la aplicación es mensual y que adentro de un mismo heartbeat un agente todavía puede hacer llamadas caras. El titular de la página de Budgets ("overruns are impossible") es más fuerte que las dos cosas.

---

## 7. Governance y aprobaciones

### Content

![Tarjeta de aprobacion: el gate de gobernanza hecho interfaz](images/s4-7-1-tarjeta-aprobacion.png)
<!-- ascii-source:
   +---------------------------------------------+
   |  Awaiting your approval                     |
   +---------------------------------------------+
   |  Publish "Comparing agent runtimes"         |
   |  to the blog                                |
   |                                             |
   |  Requested by : Scribe (Content)            |
   |  Attached     : final render                |
   |  Goal served  : Organic growth              |
   +---------------------------------------------+
   |    [ Approve ]        [ Request changes ]   |
   +---------------------------------------------+
-->
<!-- ascii-note:
intent: la tarjeta de aprobacion es el gate de gobernanza hecho interfaz; muestra los cuatro datos que un humano necesita para decidir sin reconstruir contexto.
emphasize: los tres campos de atribucion (Requested by, Attached, Goal served) alineados; los dos botones de accion al pie.
labels: Awaiting your approval, Requested by, Attached, Goal served, Approve, Request changes.
-->

Negar con una nota devuelve el trabajo con dirección. Todo lo aprobado, negado o ejecutado cae además en un feed de actividad de toda la compañía.

`Paperclip, ago-2026 · mock-up`

### Sources

- `corpus/paperclip-governance.web.md` — widget "Approval request", campos verbatim; categorías de gate (external posts, spend, deploys, "anything you define"); "Deny with a note and the agent adjusts course"; revisión de planes con aprobaciones ligadas a una revisión; feed de actividad de toda la compañía.

### Speaker notes

Mirar la forma de la tarjeta, que es lo que un manager puede copiar aunque no use este producto: el pedido trae qué, quién, el artefacto y el objetivo al que sirve. Cuatro campos, suficientes para decidir sin reconstruir el contexto.

"Deny with a note" convierte el rechazo en instrucción. Es la diferencia entre un semáforo y un revisor.

La revisión de planes es el mecanismo más interesante de la página: los planes son documentos versionados, la aprobación se liga a una revisión concreta, y cambiar el plan resetea la aprobación. Es la defensa contra el corrimiento de alcance silencioso, y no aparece en ninguna otra fuente del corpus.

El feed por compañía es la vista agregada de lo que la lámina 3.8 dibujó como tercera cara de la Task: cada gate y cada corrida quedan en un mismo stream.

El alcance real es más angosto que el titular. [La página](https://paperclip.ing/product/governance/) promete que "toda acción sensible puede parar en un gate humano"; [el FAQ del mismo sitio](https://paperclip.ing/) lo acota a lo que los agentes pueden hacerle a Paperclip. La lectura correcta, y la que hay que decir: Paperclip frena las acciones que pasan por Paperclip. Lo que un agente hace adentro de su propio runtime, no. Es la salvedad más cara del deck y descansa en un término que ya no tiene lámina: si la sala no lo tiene claro a esta altura, definir `runtime` en el momento antes de decir la salvedad.

---

# 5. La capa de abajo

**Goal of this section:** Dar el glosario de la capa que hace funcionar todo lo anterior (MCP, Skills, sandbox, self-hosting), con el alcance real de cada pieza. Adapter y runtime salieron del deck a pedido del presenter y se dictan de palabra donde aparecen. Cada pieza se presenta con el límite que el propio sitio le pone, para que la audiencia sepa qué cubre y qué no.

---

## 1. Skills, Plugins y MCP

### Content

Paperclip apila tres capas encima del runtime.

- **Skills** El procedimiento de la casa, escrito una vez y versionado como código. Cómo se prepara un PR, cómo se corre un release, cómo se escribe un mail a un cliente. Los agentes citan la skill que siguieron en el log de la corrida.
- **Plugins** Capacidades nuevas para la plataforma: integraciones, workflows, paneles de interfaz.
- **MCP** (Model Context Protocol) El estándar por el que un agente descubre y usa herramientas externas: una base de datos, un CRM, un stack de observabilidad. Los permisos son por agente.

*«Las integraciones heredan Governance: los gates también aplican a las herramientas.»*

`Paperclip, ago-2026`

### Sources

- `corpus/paperclip-extensions.web.md` — las tres capas; definición de skill ("a procedure an agent can be trusted with"); "Skills version like code and ship like packages"; "Agents cite the skill they followed in the run log"; "Integrations inherit governance: gates apply to tools too".

### Speaker notes

**Original:** "Integrations inherit governance: gates apply to tools too." — [paperclip.ing, agosto 2026](https://paperclip.ing/product/extensions/).

Antes de entrar: el adapter, que abría esta sección hasta que el presenter lo sacó del deck, es el puente entre Paperclip y el programa que corre al agente. Las claves del proveedor y su factura quedan del lado del usuario, y nada pasa por un medidor de Paperclip. El adapter HTTP es la salida universal, así que cualquier cosa que reciba un request HTTP puede ser empleado del organigrama. Si la sala pregunta cuántos adapters vienen, no dar un número: el corpus trae tres listas distintas y ninguna reconcilia.

Desplegar la sigla completa: Model Context Protocol. La analogía útil es el enchufe estándar: antes cada herramienta necesitaba su propio cable a medida; con MCP el agente descubre lo que hay enchufado y lo usa. En la maqueta del sitio, `crm-tools` figura como MCP en estado `Connected`.

El modelo de permisos no está descrito en ningún lado del corpus más allá de "per agent, with permissions", y no se ve cómo se relaciona con el modelo de roles y grants de la página de seguridad. Decirlo como hueco.

La idea de management que vale la pena: la Skill es conocimiento institucional sacado de la cabeza de una persona y puesto en un archivo versionado que todos los agentes siguen. Es el mismo movimiento que un manual de procedimientos, con la diferencia de que acá el que lo ejecuta no se olvida.

"Agents cite the skill they followed in the run log" es la afirmación más útil del corpus para una charla de gobernanza, porque hace auditable el cumplimiento del procedimiento en vez de darlo por supuesto. Está afirmada una vez y sin mecanismo. Si esa cita es forzada por el sistema o autorreportada por el agente es exactamente la distinción que importa, y la página no lo dice.

"Gates apply to tools too" es una afirmación de gobernanza fuerte (que una llamada a herramienta MCP pueda frenarse en un gate humano) y la página de gobernanza nunca la menciona; ahí solo lista posts externos, gasto, deploys y "lo que definas". Si las llamadas a herramientas son individualmente gateables queda sin resolver.

El vocabulario del propio sitio no es consistente: en la página principal `SKILL.md` se describe como el archivo con el que los agentes descubren el contexto que necesitan, que es un tercer sentido de la palabra skill.

---

## 2. Qué es un sandbox

### Content

Un sandbox es un entorno de ejecución aislado: la corrida pasa ahí adentro, con permisos y salida a la red acotados, y al terminar el entorno se destruye.

- **Workspace por corrida** aislado, con lease que el proveedor rastrea y limpieza al liberarse.
- **Secretos con alcance** ligados a agente, proyecto, rutina o entorno; el servidor los resuelve en el momento del despacho.
- **El límite del producto** El aislamiento y los privilegios dependen del proveedor y de la imagen que se configure. Paperclip da la superficie para expresar el límite.

`Paperclip, ago-2026`

### Sources

- `corpus/paperclip-security.web.md` — workspaces de ejecución con leases; referencias a secretos resueltas en runtime y valores user-scoped nunca mostrados; los descargos "depends on the provider and image you configure" y "on providers that support network policy".

### Speaker notes

Es el mecanismo detrás de la idea de radio de daño acotado, que ya no tiene lámina propia en el deck: el conjunto de cosas que un agente puede dañar si se equivoca o si alguien lo manipula, acotado antes de actuar y no corregido después. La analogía que funciona es la puerta cortafuego: no evita el incendio, limita hasta dónde llega.

En la maqueta de política de red del sitio, la corrida de una Task sale a tres destinos y nada más — `api.github.com`, `api.anthropic.com` y `registry.npmjs.org` — con todo lo demás denegado por defecto. Escribirlos en el pizarrón si la sala quiere verlos; es una maqueta, así que la forma es la enseñanza y los destinos son ilustrativos.

El hallazgo del Librarian sobre esta página vale como enseñanza de método: es la única [del sitio](https://paperclip.ing/product/security/) que se cubre con salvedades a cada paso, y eso se lee como escrita por ingeniería y no por marketing. Cuando una página de producto se pone precisa, conviene creerle más y no menos.

La lectura exacta la da el tercer punto. Una lámina que dijera "Paperclip aísla a los agentes" estaría exagerando.

---

## 3. Qué protege el self-hosting

### Content

Self-hosting es correr el software en infraestructura propia, con claves propias, sin cuenta en el proveedor del producto.

- **Tres modos de despliegue** solo localhost, privado por Tailscale o VPN, o servicio público autenticado.
- **De qué protege** Las tareas, los hilos y los secretos no pasan por Paperclip.
- **De qué no protege** Los prompts y el código siguen saliendo hacia el proveedor del modelo. La propia lista de destinos permitidos del sitio muestra `api.anthropic.com` en `allow`. `Paperclip, ago-2026`

`Paperclip, ago-2026`

### Sources

- `corpus/paperclip-security.web.md` — "Paperclip is self-hosted software: you run the instance, on your own machines or cloud, with your own model-provider keys"; tres modos de despliegue; allow-list del sandbox con `api.anthropic.com · model provider · allow`.
- `corpus/paperclip-open-source.web.md` — MIT, self-hosted, "no Paperclip account required"; "The trust model is: you don't have to trust us."

### Speaker notes

Definir el término acá, aunque haya aparecido antes en la lámina 4.1, porque es el que más se malinterpreta en una audiencia de cumplimiento.

La frase del sitio que vale citar: ["the trust model is: you don't have to trust us"](https://paperclip.ing/product/security/). Es un argumento honesto y bien construido, y tiene un límite exacto que el propio sitio dibuja: en la maqueta de política de red de su propia página de seguridad, `api.anthropic.com` aparece permitido. La afirmación precisa es que Paperclip no recibe los datos; el proveedor del modelo sí. Para un sector regulado la pregunta correcta no es dónde corre el software, es a qué proveedor de modelo salen los prompts y bajo qué contrato.

Riesgo de composición que ninguna página aborda: traer tu propio agente es heredar la postura de seguridad de ese agente. El único CVE del corpus es de OpenClaw, no de Paperclip: CVE-2026-33579, escalada de privilegios por el mecanismo de pairing, parcheado, reportado en abril de 2026. Y OpenClaw es precisamente uno de los runtimes que el producto invita a contratar.

Para un sector regulado la pregunta correcta no es dónde corre el software, es a qué proveedor de modelo salen los prompts y bajo qué contrato.

---

# 6. La misión

**Goal of this section:** Entregar la misión y aterrizarla en la instancia de Paperclip que los participantes van a tener abierta. La primera lámina presenta el encargo: la empresa automatizada que igual se comió un cambio regulatorio, y el agente que van a sumar en tres pasos sin escribir código. Las dos siguientes son el Paso 0, mirar lo que ya corre antes de tocar nada: quiénes son los agentes de Atlas y de qué se hace cargo cada uno, y cómo un pedido de blog atraviesa la empresa hasta publicarse, con cada aprobación y su dueño. La cuarta abre el tramo práctico con los tres pasos en tres tarjetas; el desarrollo lo dicta el presenter sobre la instancia proyectada. Todo lo que la sección afirma sale de la instancia viva y de las instrucciones que los agentes corren, no de la documentación del producto.

---

## 1. La misión: el vigía regulatorio de Atlas

### Content

Sos el CEO de Atlas y ya automatizaste una parte de la empresa: un equipo de agentes que publica tu contenido técnico. Funcionó, hasta que un cambio regulatorio se te coló por el costado y te costó dos veces. Quedaste afuera de una preselección de un cliente grande. Y el blog que pediste para reaccionar salió sin revisión legal, sonó a denuncia política y lo tuviste que bajar.

Dos golpes, una sola causa: nadie vigila el horizonte.

Vas a sumar el agente que lo haga. Primero mirás la empresa que ya corre, y después tres pasos. Sin escribir código.

`Misión del curso, ago-2026`

### Sources

- `corpus/mision-vigia-regulatorio.md.md` — el encuadre completo: la situación de Atlas y el golpe doble (la preselección perdida por la reforma de integridad ligada a la Ley 27.401, y el blog que salió sin revisión legal); el hueco («nadie, ni humano ni agente, vigila el horizonte regulatorio»); el Paso 0 de reconocimiento y los tres pasos; y las tres piezas que conectan la historia (escalera de goals, el proyecto como casa, la task como costura).
- `corpus/atlas-instancia-viva.md.md` — el goal «Anticipación regulatoria» colgando del goal de compañía, activo en la instancia desde el 2026-08-26.

### Speaker notes

Esta lámina abre el tramo práctico de la clase. Hasta acá la sala vio la teoría y los controles del producto; de acá en adelante mira una empresa que ya corre y le suma una pieza. Conviene decirlo con esas palabras, porque cambia el modo de escuchar.

El encuadre importa más que el detalle del caso. El punto de partida es una empresa que **ya está automatizada y aun así falla**, y falla por una razón de diseño organizacional, no de tecnología: la automatización sólo escribe lo que se le pide. Cada pedido es una Task que marketing lleva por un pipeline con el visto bueno humano al final. Nadie vigila el horizonte. Ese es el hueco, y es un hueco de organigrama.

Los dos golpes conviene contarlos separados, porque enseñan cosas distintas. El primero es de información: un cliente ligado a YPF avisó que sólo iba a contratar proveedores que certifiquen su programa de integridad, en línea con la Ley 27.401, y venía en una reforma que se discutía hacía semanas. Atlas se enteró tarde y quedó afuera. El segundo es de gobierno: cuando el CEO pidió un blog para reaccionar, el encuadre de un tema sensible quedó improvisado por Marketing, que no tiene la expertise regulatoria ni la conciencia del riesgo reputacional. El blog hubo que bajarlo. La lámina siguiente muestra el CLO en el organigrama, y la 6.3 muestra la aprobación legal que hoy impide que eso se repita.

La respuesta que la misión propone es de management y vale enunciarla así: en vez de sumar personas, se suma un rol. El participante no escribe código en ningún momento, conecta piezas de Paperclip. Si alguien de la sala pregunta qué habilidad técnica hace falta, la respuesta honesta es ninguna, y esa es parte de la tesis del curso.

Las tres piezas que atan la historia, por si conviene anticiparlas: el goal nuevo del vigía cuelga del goal de compañía, porque el riesgo regulatorio es materia prima del contenido de marca; el goal vive en un proyecto propio, que es donde corre el heartbeat y quedan las notas de riesgo; y la task de blog asignada al CMO es el único punto donde el dominio regulatorio y el de marketing se tocan. Sin la escalera de goals el agente nuevo sería un agente suelto, que es el error más común al armar un organigrama de agentes.

El tema legislativo del ejemplo es un proyecto de reforma de integridad y transparencia en la cadena de suministro de hidrocarburos: exigiría declarar beneficiarios finales, adoptar programas de integridad y certificar cumplimiento para poder facturar en Vaca Muerta. Es sensible porque toca corrupción, y es material para Atlas porque su compliance se vuelve una ventaja de acceso. La misión ofrece alternativas si el presenter prefiere un tema menos cargado: un cambio al RIGI, regulación de metano y venteo, o certificación técnica obligatoria.

Aviso de estado, importante antes de dictar: la instancia que se va a proyectar **ya tiene al vigía creado**. El guion pide que el participante registre que el rol no existe, y en la máquina existe desde el 26 de agosto. Hay que decidir antes de la clase si se resetea la instancia o si se dicta sobre la empresa ya resuelta y la misión se corre sobre una copia. Está anotado en Open questions.

---

## 2. Quién es quién en Atlas

<!-- format: editorial -->

### Content

Atlas vende insumos de perforación para Vaca Muerta y opera en español. La empresa que van a abrir tiene cuatro agentes y un humano, todos en el mismo organigrama. El CEO arriba; CMO y CLO cuelgan de él, y el Blog Content Manager cuelga del CMO. Nadie vigila el horizonte regulatorio: ese es el puesto que falta.

- **CEO** Fija dirección y abre los roles que faltan. El único puesto sin instrucciones escritas.
- **CMO** Marketing punta a punta. No escribe una línea de contenido: delega la producción.
- **Blog Content Manager** El único que reporta al CMO. Escribe el brief y el contenido final, y publica.
- **CLO** Riesgo legal, contratos, cumplimiento regulatorio y gobierno corporativo.
- **Austral Admin** *(humano, owner)* El único humano: crea agentes, goals y proyectos, y aprueba cada blog.

`Instancia del curso, ago-2026`

### Sources

- `corpus/atlas-instancia-viva.md.md` — captura directa de las tablas `companies`, `agents` y `goals` de la instancia el 2026-08-27: las siete filas de agentes con `role`, `reports_to`, estado y `adapter_type`; el `capabilities` verbatim de cada uno; la escalera de goals; y las dos cuentas humanas con su rol.
- `corpus/atlas-org-setup.md.md` — qué es Atlas (insumos de perforación, español, Vaca Muerta, prefijo ACMA, board-governed); funciones por agente; los dos humanos y su reparto.

### Speaker notes

Cuatro precisiones que salieron del cuerpo para que las cinco fichas entren. El CMO abarca audiencia, posicionamiento, línea editorial, canales y análisis competitivo. El CLO cubre además la revisión de contratos del negocio de insumos. La aprobación del owner sobre el contenido final es la misma que autoriza publicar, como muestra la lámina siguiente. Y el CEO es el único puesto del organigrama sin `capabilities` escritas.

Esta lámina abre el Paso 0 de la misión, y el Paso 0 tiene una consigna precisa: mirar lo que ya existe antes de crear nada. La [misión](missions/Paperclip/mission.md) lo dice así: la mejor forma de aprender a crear un agente es leer dos que ya funcionan.

Lo que la sala tiene que llevarse de acá es de qué está hecho un agente, más que qué dice cada uno. Un agente no es un prompt suelto: es un rol con jefe (`reportsTo`), un para qué (goal), un dónde (proyecto), un comportamiento escrito (`capabilities`) y un presupuesto. Cuando en la misión creen al Director van a llenar esas mismas casillas, una por una. Conviene abrir la ficha del CMO en pantalla mientras se dicta esto.

El campo `capabilities` es la pieza que más cuesta entender de entrada. Es texto plano y es la descripción de puesto: persiste en cada corrida, no se reescribe por tarea. Ahí está la diferencia con un chatbot, y vale decirla con esas palabras: al puesto se lo instruye una vez.

El humano está en el organigrama, no mirando de afuera, y es uno solo: la misma cuenta arma la estructura y aprueba el trabajo del día a día. Vale decirlo porque desarma una expectativa: la gobernanza de la lámina siguiente no depende de repartir permisos entre varias personas, sino de que el sistema pare y espere a un humano en los momentos definidos. Con una sola persona, las dos aprobaciones del pipeline son de ella.

La lámina muestra cuatro agentes a propósito: es la empresa **antes** de la misión. El puesto de vigilancia regulatoria es el que la sala va a crear en el Paso 2, así que nombrarlo acá le sacaría el sentido al Paso 0. Si aparece proyectado en la instancia, decir que ya está creado de una corrida anterior y que la misión se hace igual.

Detalle que no está en lámina y sirve si alguien pregunta: en la base hay siete filas de agentes. Además del vigía ya creado, dos están `terminated` y son versiones anteriores de ese mismo rol de relaciones institucionales. El rol se rehízo dos veces. Terminar un agente no lo borra, lo saca de circulación y la fila queda, que es exactamente lo que uno querría de un registro de personal.

Los agentes de la instancia corren todos sobre el mismo adapter, `codex_local`, con DeepSeek detrás. El organigrama de la lámina 4.2 mezclaba runtimes distintos por agente; esta instancia no lo hace, y conviene aclararlo para que nadie crea que la mezcla es obligatoria.

La escalera de goals se ve mejor acá que en cualquier lámina teórica: Atlas tiene un goal de compañía (posicionamiento orgánico vía contenido técnico) y sub-goals colgando de él, uno por frente de trabajo. Ese es el enganche hacia la misión, y conviene dejarlo picando sin resolverlo: el puesto nuevo también va a necesitar su goal colgado del de compañía, porque si no queda como un agente suelto. Es el argumento de gestión que el Paso 2 hace probar con las manos.

Salvedad para no afirmar de más: la ficha de un agente incluye presupuesto y heartbeat, pero la captura leyó `companies`, `agents` y `goals`, no los budgets ni las cadencias configuradas. Si alguien pregunta números de presupuesto, mostrarlos en pantalla en vez de decirlos.

Hay una inconsistencia en la base que conviene conocer por si aparece proyectada: el `capabilities` del Blog Content Manager quedó guardado con una sintaxis de link rota que arrastra una versión anterior del texto adentro. La versión vigente dice que sólo publica drafts aprobados y que no es dueño de la estrategia ni del calendario editorial, pero el procedimiento que el agente efectivamente corre le hace escribir el brief y el draft completos. La descripción de puesto quedó atrás del trabajo real. Como enseñanza sirve: las descripciones de puesto envejecen igual que en una empresa de personas.

---

## 3. Cómo se publica un blog en Atlas

### Content

![Recorrido de un pedido de blog: seis pasos, dos aprobaciones numeradas y un escalamiento excepcional](images/s6-3-1-recorrido-pedido-blog.png)
<!-- ascii-source:
              CMO                                BLOG CONTENT MANAGER
      =================                   ==============================

   PEDIDO DE BLOG
          |
          v
  +-------------------+
  | 1. entiende y     |
  |    propone 3      |
  |    angulos        |
  +-------------------+
          |
          v
    << APROBACION 1 >>
       el board elige 1 de 3
          |
          v
  +-------------------+
  | 2. pide revision  |
  |    legal al CLO   |
  +-------------------+
          |
          v
  +-------------------+
  | 3. el CLO         |
  |    dictamina      |
  |  GO / CONDICIONES |
  |     / NO-GO       |
  +-------------------+
          |
          |  solo si el riesgo es alto
          + - - - - - ->  [[ ESCALAMIENTO ]]
          |                  el board decide
          |  camino normal    seguir o descartar
          v
  +-------------------+                    +--------------------------+
  | 4. delega UNA     |                    | 5. escribe el brief y    |
  |    subtask        |                    |    el contenido final    |
  +-------------------+                    +--------------------------+
          |                                             |
          +========= handoff =========>                 v
                                              << APROBACION 2 >>
                                                    el board
                                              ( aprobar = publicar )
                                                          |
                                                          v
                                            +--------------------------+
                                            | 6. corre                 |
                                            |    /blog-publisher       |
                                            +--------------------------+
                                                          |
                                                          v
                                                  BLOG PUBLICADO
                                                    ticket done

  En la APROBACION 2 el humano puede pedir cambios: el agente reescribe el mismo
  documento y vuelve a pedir la misma aprobacion. Nunca se abre un ticket nuevo.
-->

<!-- ascii-note:
intent: el recorrido completo de un pedido de blog dentro de la empresa de agentes de Atlas, dibujado como una escalera donde se alternan PASOS DE TRABAJO (los hace un agente) y APROBACIONES (las decide un humano). La lamina existe para que la audiencia vea de un vistazo cuando tiene que decidir un humano antes de que un texto escrito por IA salga publicado: dos veces, al principio y al final, mas una tercera excepcional. Todo ocurre sobre un unico ticket que cambia de dueno una sola vez.

que muestra, en orden: un pedido de blog entra y lo toma el CMO. (1) El CMO entiende el pedido y propone tres angulos distintos. APROBACION 1: el board elige uno de los tres. (2) El CMO le pide revision legal al CLO, en comentarios sobre el mismo ticket. (3) El CLO dictamina GO, GO CON CONDICIONES o NO-GO. Si el riesgo es alto, y SOLO en ese caso, se abre el ESCALAMIENTO: el board decide si sigue o se descarta; el camino normal lo saltea. (4) El CMO delega UNA sola subtask al Blog Content Manager: ese es el handoff, el unico cruce entre los dos carriles. (5) El Blog Content Manager escribe el brief y el contenido final, los dos como documentos sobre el ticket, sin pedir aprobacion en el medio. APROBACION 2: el board otra vez, y esta aprobacion ademas autoriza publicar. (6) Corre /blog-publisher y el blog queda publicado, con el ticket cerrado.

layout: dos carriles verticales lado a lado. Carril izquierdo rotulado CMO, con los pasos 1 a 4, la APROBACION 1 y la rama del ESCALAMIENTO. Carril derecho rotulado BLOG CONTENT MANAGER, con los pasos 5 y 6 y la APROBACION 2. El flujo baja por el carril izquierdo, cruza una sola vez al derecho por el handoff del paso 4 al paso 5, y sigue bajando. El carril derecho es mas corto que el izquierdo: no rellenar el hueco con adornos, el desbalance es informacion (el trabajo de gobierno esta arriba, la produccion abajo). Formato de lamina apaisado: preferir dos columnas anchas y equilibradas antes que una sola columna alta y flaca. Los rotulos de carril arriba de cada columna, como encabezados.

emphasize: LA DISTINCION VISUAL ENTRE PASO Y APROBACION ES LO MAS IMPORTANTE DEL DIBUJO. Un paso de trabajo y una aprobacion humana tienen que verse como dos especies distintas a tres metros de distancia: distinta forma, distinto peso, distinto color. Los pasos son cajas rectangulares sobrias y numeradas del 1 al 6. Las aprobaciones son la parada del camino y tienen que resaltar: forma propia (rombo, pastilla o hexagono, lo que la gramatica del deck permita), color de acento, y el nombre de quien decide escrito junto a cada una, legible, no en letra chica.

emphasize (segundo nivel): SON DOS APROBACIONES NUMERADAS Y UNA EXCEPCION SIN NUMERAR. El ESCALAMIENTO no lleva numero a proposito: si se numera, el dibujo vuelve a decir que hay tres aprobaciones y se pierde el argumento de la lamina. Dibujarlo como rama lateral, con su condicion "solo si el riesgo es alto" visible, con el rotulo "camino normal" sobre la flecha que lo saltea, y en una variante visual mas tenue que las dos aprobaciones numeradas (por ejemplo contorno punteado) para que se lea como excepcion y no como paso. Las tres paradas las decide el mismo humano, el board: Atlas tiene un unico usuario humano. No inventar un segundo decisor ni repartir los rotulos entre nombres distintos; el rotulo del board se repite en la APROBACION 1, el ESCALAMIENTO y la APROBACION 2, y esa repeticion es informacion. La APROBACION 2 lleva la glosa "aprobar = publicar" porque hace dos cosas a la vez.

emphasize (tercer nivel): el handoff del paso 4 al paso 5 es el unico cruce entre carriles y merece ser la flecha mas visible del dibujo, rotulada. Es donde el trabajo cambia de dueno.

labels: PEDIDO DE BLOG (entrada), CMO y BLOG CONTENT MANAGER (rotulos de carril), CLO y board (quienes deciden), APROBACION 1, ESCALAMIENTO y APROBACION 2, los seis pasos numerados con su texto, "solo si el riesgo es alto" (condicion de la rama), "camino normal" (la flecha que la saltea), "handoff" (el cruce), "aprobar = publicar" (glosa de la aprobacion 2), /blog-publisher, BLOG PUBLICADO y "ticket done" (salida). Al pie, la nota del bucle de revision: en la aprobacion 2 el humano puede pedir cambios, el agente reescribe el mismo documento y vuelve a pedir la misma aprobacion, sin abrir un ticket nuevo. Esa nota va como pie discreto, no como caja del flujo.

avoid: no encerrar varios pasos dentro de una misma caja grande: cada paso y cada aprobacion es su propio nodo. No usar el mismo color para pasos y aprobaciones. No numerar el ESCALAMIENTO ni dibujarlo en la linea principal como si fuera obligatorio. No agregar aprobaciones intermedias para el brief ni para el draft: no existen, y una version anterior de este dibujo las tenia. No agregar iconos de personas ni de robots. No traducir ningun rotulo al ingles.

text: los rotulos van en español. El texto de las cajas puede acortarse para que entre, pero los rotulos APROBACION 1, ESCALAMIENTO y APROBACION 2 y los nombres de quien decide se conservan completos.
-->

### Sources

- `corpus/cmo-blog-request-procedure.md.md` — el procedimiento del CMO: las tres etapas más el escalamiento 2b; los dueños de cada aprobación (board para el ángulo y para el escalamiento, CLO para la revisión legal, content-reviewer para el contenido producido); el chequeo legal en el hilo y bloqueante; la sección `LEGAL - MUST HONOR` obligatoria; y que delegar no es completar.
- `corpus/blog-content-manager-procedure.md.md` — el procedimiento del Blog Content Manager. ⚠️ El registro documenta el modelo viejo, de tres aprobaciones de contenido (brief, draft, final). **El procedimiento se cambió el 2026-08-27 a una sola aprobación**: brief y contenido final se escriben seguidos, los dos como documentos sobre el ticket (`concept-brief`, `full-draft`), sin tarjeta en el medio, y la única tarjeta que se abre es la del contenido final, que además autoriza publicar. El bucle de revisiones no cambió: mismo documento, misma clave, aprobación reabierta con versión bumpeada.
- `corpus/atlas-org-setup.md.md` — la descripción del pipeline desde el setup de la company y el ticket que queda asignado al Blog Content Manager todo el camino. ⚠️ Igual que el registro anterior, describe el pipeline previo al cambio del 2026-08-27.

### Speaker notes

Esta es la lámina donde la clase ve la Task de la sección 3 haciendo su trabajo en un sistema que corre. Vale nombrarlo: cada aprobación del dibujo es una tarjeta sobre el mismo ticket, y el ticket es el que sostiene el rastro de quién aprobó qué.

El argumento de la lámina, en una línea, por si se dicta apurado: el humano aprueba **la dirección** al principio y **el resultado** al final, y en el medio no aprueba nada. Ese reparto es la decisión de gobierno, y es replicable fuera de Paperclip.

Los dos dueños son el CMO y el Blog Content Manager, y el trabajo cambia de manos una sola vez, en el handoff del paso 4 al 5. El CLO participa sin ser dueño: opina sobre el mismo ticket, en comentarios, y no abre un ticket legal aparte. Ese detalle vale más de lo que parece, porque es lo que hace que la revisión legal quede en el mismo rastro que el resto de la decisión.

El CMO nunca escribe contenido. Su salida es dirección: entendimiento del pedido y tres ángulos genuinamente distintos, con título tentativo, punto de vista, audiencia y por qué ahora. Si la sala pregunta por qué tres y no uno, la respuesta del procedimiento es que el board elija, no que el agente decida solo.

El escalamiento es el que más discusión da y conviene dictarlo con precisión. La revisión del CLO es advisory pero bloqueante: bloquea al CMO, no al board. Con veredicto GO, o con condiciones satisfacibles dentro del contenido y riesgo bajo o medio, el CMO sigue solo y el escalamiento nunca se abre. Con NO-GO, riesgo alto, o condiciones que no puede cumplir, no delega y escala al board. La regla escrita en sus instrucciones es que nunca puede pasar por encima de un veredicto legal: un veredicto duro es decisión del board. Por eso en el dibujo no lleva número: no es la tercera aprobación del camino, es la que aparece cuando el camino se sale de lo normal.

La sección `LEGAL - MUST HONOR` de la delegación es el mecanismo que hace que la revisión legal sobreviva al handoff. El CMO transcribe cada condición del veredicto reescrita como regla concreta de producción, del tipo «no nombrar competidores» o «toda afirmación fáctica tiene que ser verificable y citada». Con un GO limpio escribe «Legal: GO, sin condiciones». Tiene prohibido delegar sin esa sección. Es la respuesta concreta a la pregunta de cómo se transporta una decisión de gobierno de un agente a otro.

Un punto de gestión que la sala del MiM agradece: delegar no es completar. El CMO no marca su pedido como hecho cuando lo entrega; lo deja abierto y lo cierra recién cuando el hijo termina. Un manager que da por cerrado lo que delegó pierde el hilo del resultado.

Del lado del Blog Content Manager, tres reglas que explican la forma del dibujo. Todo pasa en un solo ticket, sin sub-tickets ni cadenas de dependencias. Escribe el brief y el contenido final de corrido, sin pedir permiso en el medio, y abre una sola tarjeta al final. Y el brief y el contenido son documentos sobre el ticket, con revisiones, no adjuntos: se ven en el panel Documents y guardan su historia. El brief sigue existiendo aunque ya no se apruebe: es donde queda escrito el porqué del post, y el que aprueba lo tiene al lado cuando lee el contenido.

La aprobación 2 es la que hay que remarcar. Aprobar el contenido final y autorizar la publicación son el mismo acto, no hay una aprobación de publicar aparte. Recién con esa aceptación el agente corre `/blog-publisher` y marca el ticket done.

El bucle de revisiones, que en el dibujo es la línea de abajo, funciona así: el humano pide cambios, el agente reescribe el mismo documento como nueva revisión, comenta qué cambió y reabre la misma aprobación con la versión siguiente. Nunca abre un ticket nuevo. El ticket queda asignado al mismo agente de punta a punta.

Acá está el precio del diseño y conviene decirlo, porque es la pregunta que va a hacer alguien de la sala: con una sola aprobación al final, un rechazo es caro. Antes un post mal encarado moría en el brief; ahora muere escrito entero. La respuesta es que la dirección ya se aprobó arriba, en la aprobación 1, que es la salida barata de verdad; lo que el reviewer juzga al final es ejecución, no rumbo. Es la misma decisión que toma un director que aprueba el enfoque de un informe y después el informe, y no cada capítulo.

Salvedad de método, por si alguien contrasta con la documentación: el documento de setup de Atlas describe un pipeline de tres aprobaciones de contenido y se saltea las dos del CMO, la elección de ángulo y el chequeo legal. Está doblemente desactualizado, porque el procedimiento del Blog Content Manager se cambió el 2026-08-27 y hoy tiene una sola. Lo que el dibujo muestra sale de las instrucciones que los agentes efectivamente corren. Cuando la documentación y el sistema no coinciden, en esta clase le creemos al sistema, y esta lámina es el ejemplo.

---

## 4. Los tres pasos

### Content

- **1 · A mano** Le pedís el blog al CMO vos mismo.
- **2 · El vigía** Un goal, un proyecto, y un agente con heartbeat semanal.
- **3 · Una corrida** Lo disparás una vez y seguís la cadena.

`Misión del curso, ago-2026`

### Sources

- `corpus/mision-vigia-regulatorio.md.md` — los tres pasos de la misión: la línea de base reactiva (Paso 1), la creación del vigía con su goal ladderado, su proyecto y sus `capabilities` (Paso 2), y la corrida única del heartbeat seguida en Activity y en el timeline (Paso 3).

### Speaker notes

Lámina de arranque del tramo práctico. El presenter dicta; el cuerpo es sólo el andamio para que la sala sepa dónde está parada.

Apuntes por si hacen falta, uno por paso.

**Paso 1, a mano.** Con la cuenta admin, que es la única, se crea la task de blog en el proyecto de marca y se le asigna al CMO. Fluye por el pipeline de la lámina anterior hasta publicarse. Lo que hay que hacer notar es que funciona y aun así no sirve: pasó sólo porque alguien lo detectó y lo pidió. Es, palabra por palabra, cómo nació el blog que hubo que bajar.

**Paso 2, el vigía.** Se sigue con la misma cuenta: contratar agentes es facultad del board, y es la que tiene. Tres cosas en orden: el goal «Anticipación regulatoria» colgado del goal de compañía, el proyecto «Radar Regulatorio» como casa del agente, y el agente con sus `capabilities` escritas. Es contratación directa del board, sin approval. La rutina que se le escribe tiene cuatro movimientos: investigar la normativa argentina del sector, medir materialidad con nivel bajo, medio o alto, abrir una nota de riesgo y delegarle el blog al CMO cuando hay algo material, y dejar una task visible de «sin acción» cuando no lo hay. Esa última vale la pena remarcarla: el caso negativo también deja rastro.

**Paso 3, una corrida.** Se dispara el heartbeat a mano y se sigue la cadena en Activity: investiga, encuentra el riesgo, crea la nota de riesgo, crea la task de blog asignada al CMO. Después se aprueban las compuertas desde esa misma cuenta. El resultado que cierra la clase es que un solo heartbeat produjo dos tasks y metió un blog en el pipeline sin que nadie lo pidiera.

Si la sala pregunta por las barreras del vigía: contenido técnico y factual, nunca militancia partidaria, y no acusa a personas ni empresas puntuales. El humano sigue siendo la aprobación final, y el vigía propone y arma el brief pero no escribe ni publica.

---

# Conclusions

## 1. Las cuatro ideas de la clase

<!-- format: editorial -->

### Content

- **Orquestar es una decisión de management** Cuánto paralelizar, con qué presupuesto y bajo qué aprobación. La arquitectura viene después.
- **El paralelismo depende del dominio** Leer tolera hermanos que no se hablan. Escribir sobre estado compartido, no.
- **El precio se paga en tokens** Un multi-agente consume unos 15× lo de un chat. La tarea tiene que valer eso.
- **La Task es la pieza de gobierno** Unidad de trabajo, registro de decisión y rastro de auditoría en el mismo objeto.
- **El instrumento no toma la decisión** Paperclip pone los mecanismos. Qué se aprueba y qué se gasta los define un manager.

### Sources

- `corpus/anthropic-multi-agent-research.web.md`
- `corpus/cognition-dont-build-multi-agents.web.md`
- `corpus/koreai-orchestration-patterns.web.md`
- `corpus/paperclip-tasks.web.md`
- `corpus/paperclip-governance.web.md` · `corpus/paperclip-home.web.md` — organigrama, tickets, heartbeats, budgets y gates como mecanismos; el humano define qué se aprueba y qué se gasta.

### Speaker notes

Las cinco en orden de la clase. Si el tiempo se acortó, esta es la lámina que no se saltea.

Dos precisiones que salieron del cuerpo para que las cinco fichas entren. El 15× es de [Anthropic, junio de 2025](https://www.anthropic.com/engineering/multi-agent-research-system). Y los mecanismos que Paperclip pone son, con nombre: el organigrama, las Tasks, los heartbeats, los budgets y los gates; lo que sigue siendo decisión humana es qué acciones se aprueban, qué presupuesto se asigna y quién lee el rastro.

La quinta cierra la mitad de Paperclip y evita que la clase termine sonando a demostración de producto: las herramientas cambian, las cuatro decisiones de management no.

---

## 2. El árbol de decisión

### Content

![Arbol de decision que resume la clase en tres preguntas encadenadas](images/sc-2-1-arbol-decision.png)
<!-- ascii-source:
        La tarea vale ~15x los tokens de un chat?
                        |
              no -------+------- si
              |                    |
              v                    v
        un solo hilo      Los agentes escriben sobre
                          estado compartido?
                                   |
                          si ------+------ no
                          |                 |
                          v                 v
                   un solo hilo, o     supervisor con
                   limites explicitos  fan-out
                   entre escritores          |
                                             v
                                   Cada accion queda en una
                                   Task con dueno y rastro?
                                             |
                                    no ------+------ si
                                    |                 |
                                    v                 v
                             agentes actuando   organizacion
                             sin gobierno       gobernable
-->
<!-- ascii-note:
intent: arbol de decision que resume la clase entera en tres preguntas encadenadas; es la herramienta que la audiencia se lleva.
emphasize: las tres preguntas como nodos de decision; las dos hojas finales opuestas (agentes actuando sin gobierno / organizacion gobernable).
labels: las tres preguntas, las ramas si/no, y las cuatro hojas terminales.
-->

### Sources

- `corpus/anthropic-multi-agent-research.web.md` — condición de viabilidad económica y multiplicador de tokens.
- `corpus/cognition-dont-build-multi-agents.web.md` — la objeción sobre estado compartido.
- `corpus/koreai-orchestration-patterns.web.md` — el patrón supervisor como opción con fan-out.
- `corpus/paperclip-tasks.web.md` — el ticket con dueño y rastro.

### Speaker notes

Recorrer el árbol con un caso que proponga la sala. Funciona bien pedir un proceso concreto de la empresa de alguien y bajarlo por las tres preguntas en vivo.

La primera pregunta se contesta con el precio por millón de tokens del proveedor, el mismo que se usó en la lámina 2.5. Sin ese número la raíz del árbol queda abstracta.

Las tres preguntas están ordenadas de más barata a más cara de responder: la económica primero, porque descarta la mayoría de los casos sin discutir arquitectura.

---

## 3. Qué hacer el lunes

### Content

1. **Elegir un proceso** repetitivo, con criterio de terminado claro y sin efectos externos irreversibles.
2. **Escribirla como Task** dueño, estado, hilo y definition of done, antes de tocar ninguna herramienta.
3. **Definir el radio de daño** el conjunto de cosas que el agente puede dañar si se equivoca: qué puede leer, a dónde puede salir, con qué credencial.
4. **Poner un tope de gasto** y decidir quién aprueba subirlo.
5. **Nombrar a quien lee el rastro** y con qué frecuencia. Un audit trail que nadie abre no gobierna nada.

### Sources

- `corpus/paperclip-tasks.web.md` — los campos del ticket.
- `corpus/paperclip-security.web.md` — radio de daño y mínimo privilegio.
- `corpus/paperclip-budgets.web.md` — topes y aprobación de aumentos.
- `corpus/paperclip-governance.web.md` — rastro por corrida.

### Speaker notes

Los cinco pasos son de gestión y ninguno requiere instalar nada. Se pueden hacer en una hoja antes de evaluar herramienta alguna, y ese es el punto.

El paso 1 tiene una restricción deliberada: sin efectos externos irreversibles. El primer proceso que se delega a agentes no debería ser uno donde el "rewind" haga falta.

El paso 5 es el que más se saltea en la práctica.

---

## 4. Fuentes y preguntas

<!-- template: quote -->
<!-- generate-image: right | estructura y limite: la calma de un sistema que se puede inspeccionar entero -->

### Content

> «La autonomía es un privilegio que se otorga, no un valor por defecto.»

`Paperclip, ago-2026`

Las cuatro fuentes que sostienen la clase: [Anthropic, *How we built our multi-agent research system*](https://www.anthropic.com/engineering/multi-agent-research-system) · [Cognition, *Don't Build Multi-Agents*](https://cognition.com/blog/dont-build-multi-agents) · [Kore.ai, *Choosing the right orchestration pattern*](https://www.kore.ai/blog/choosing-the-right-orchestration-pattern-for-multi-agent-systems) · [paperclip.ing](https://paperclip.ing)

### Sources

- `corpus/paperclip-home.web.md` — "Autonomy is a privilege you grant, not a default", verbatim.
- `corpus/anthropic-multi-agent-research.web.md` · `corpus/cognition-dont-build-multi-agents.web.md` · `corpus/koreai-orchestration-patterns.web.md` · `corpus/paperclip-open-source.web.md` — URLs de origen.

### Speaker notes

**Original:** "Autonomy is a privilege you grant, not a default." — [paperclip.ing, agosto 2026](https://paperclip.ing/).

La frase de cierre es de Paperclip y resume la clase mejor que cualquier resumen propio: la autonomía es un privilegio que alguien otorga.

Dejar la lámina proyectada durante las preguntas.

---

# Open questions

- **El pipeline de blog se rediseñó el 2026-08-27, y la lámina 6.3 documenta el diseño nuevo.** El Blog Content Manager pasó de tres aprobaciones de contenido (brief, draft, final) a **una sola**: escribe el brief y el contenido final de corrido, los dos como documentos sobre el ticket, y abre una única tarjeta al final que además autoriza publicar. El pipeline completo queda en dos aprobaciones humanas —el ángulo, arriba, en el CMO; el contenido final, abajo— más el escalamiento legal, que sigue siendo condicional y sin numerar. El cambio se aplicó a las instrucciones vivas del agente (`BLOG_CREATION_WORKFLOW.md`, `AGENTS.md`, `HEARTBEAT.md`, `TOOLS.md`), con backups `*.bak.20260827-*-onegate`. **Tres cosas quedan pendientes antes de dictar:** (a) `missions/Paperclip/atlas-org-setup.md` todavía describe el pipeline viejo y hay que actualizarlo; (b) los cuatro registros de corpus de esta sección no están en disco, así que las Sources de 6.1 a 6.3 apuntan a archivos que no existen —lo verificado salió de leer las instrucciones vivas de los agentes, que es mejor fuente pero no es la que el deck cita—; (c) el ticket `ACMA-167` quedó con una tarjeta del modelo viejo pendiente y hay que migrarlo antes de proyectar la instancia. **Y una advertencia para el ensayo:** el diseño nuevo todavía no se vio correr punta a punta. Si se dicta antes de probarlo, decir eso en sala en vez de mostrarlo como hecho consumado.

- **Atlas pasó a tener un solo usuario humano, y el corpus todavía dice dos.** Por decisión del presenter (2026-08-31) la instancia queda con una única cuenta, `austral-admin@example.com`, que hace lo estructural y además aprueba cada compuerta; `content-reviewer@example.com` desaparece. Las láminas 6.2, 6.3 y 6.4 ya están alineadas, y los tres archivos de la misión también (`mission.md`, `mission-res.md`, `atlas-org-setup.md`). **Lo que no se tocó son las Sources**, a propósito: `corpus/atlas-instancia-viva.md.md` dice «las dos cuentas humanas con su rol» y `corpus/cmo-blog-request-procedure.md.md` nombra a «content-reviewer para el contenido producido», porque eso es lo que esos registros efectivamente capturaron el 2026-08-27. Son atribución de procedencia, no contenido de lámina, y reescribirlas sería inventar una fuente. Antes de dictar hay que decidir: re-capturar la instancia para que el corpus refleje la cuenta única, o dejar la discrepancia anotada y avisarla si alguien contrasta. **Y hay que confirmar en la instancia que la segunda cuenta esté efectivamente dada de baja**, porque la lámina ya afirma que hay un solo humano.

- **La instancia está en estado post-misión, y la misión asume el estado inicial.** El guion del Paso 0 pide que el participante registre que **no existe** ningún Director de Relaciones Institucionales, porque ese es el hueco que va a llenar. En la instancia al 2026-08-27 el **DRI existe**, está `idle`, y su goal «Anticipación regulatoria» está activo desde el 2026-08-26. Además hay dos agentes `terminated` que son iteraciones previas del mismo rol. Antes de dictar hay que decidir: resetear la instancia al estado inicial, o dictar la sección 6 sobre la empresa ya resuelta y correr la misión sobre una copia. La lámina 6.1 hoy muestra los cinco activos, DRI incluido, así que si se resetea hay que sacarlo de la lámina.
- **Cuándo interviene Legales: la misión y el sistema no coinciden.** El guion de la misión dice que la revisión del CLO es obligatoria sólo en temas de alta sensibilidad (corrupción, transparencia) y opcional en baja o media. El procedimiento que el CMO efectivamente corre la hace **bloqueante para todo blog**, sin excepción por sensibilidad. La lámina 6.2 dibuja la versión del sistema y lo dice en notas. Si el presenter prefiere dictar la versión de la misión, hay que cambiar el diagrama y avisar que el sistema real es más estricto.
- **Presupuestos y cadencias de heartbeat de los agentes de Atlas, sin verificar.** La captura del 2026-08-27 leyó `companies`, `agents` y `goals`. No leyó budgets ni las cadencias configuradas, así que ninguna de las dos cosas puede afirmarse en lámina. El `capabilities` del DRI declara un heartbeat semanal, pero eso es lo que dice su descripción de puesto, no lo que está configurado. Las notas de 6.1 avisan de mostrarlos en pantalla en vez de decirlos. Si se quieren números en lámina, hay que leer esas columnas.
- **La descripción de puesto del Blog Content Manager contradice lo que el agente hace.** Su `capabilities` en la base dice que sólo publica drafts aprobados y que no es dueño de la estrategia ni del calendario editorial; el procedimiento que corre le hace escribir el brief y el draft completos. El campo además quedó guardado con una sintaxis de link rota que arrastra adentro una versión anterior del texto. Hoy vive en notas de 6.1 como enseñanza sobre descripciones de puesto que envejecen. Decidir si se muestra proyectado o se arregla en la instancia antes de la clase.
- **Los tres pasos se dictan de palabra.** La 6.4 los enuncia en tres tarjetas a pedido del presenter, que dicta el desarrollo sobre la instancia proyectada; el detalle de cada paso vive en sus notas. Quedan sin usar dos figuras del corpus que servirían si alguno pidiera lámina propia: el diagrama de conexión goal/proyecto/task para el Paso 2, y el de reactivo contra proactivo, que es el que mejor explica por qué el Paso 2 existe. Están en `corpus/mision-vigia-regulatorio.md/images/`.
- **Precio por millón de tokens, para la lámina 2.5.** El material capturado no incluye ninguna lista de precios de ningún proveedor. Tras el pedido del presenter de borrar la lámina de definición, el token se define en una línea en 2.8, la primera lámina que gasta el número; el precio vigente hay que traerlo el día del dictado para que los multiplicadores 4× y 15× se conviertan en pesos. Decidir qué proveedor se toma como referencia.
- **El deck ya no dice nada sobre la madurez del proyecto.** Con la sección de auditoría cortada salieron también las señales contradictorias (entidad comercial, conteos de estrellas de GitHub, issues abiertos contra contribuidores), todas archivadas en Cut material. Ninguna afirmación reputacional queda en lámina, así que ya no hay nada que re-verificar antes de dictar; a cambio, la clase presenta Paperclip sin decir cuán nuevo ni cuán respaldado está. Si el presenter quiere una línea sobre eso, el material está archivado y la cifra de estrellas a usar sería "74k+" (paperclip.ing, agosto 2026).
- **Cita atribuida a "Brinsa" sin registro en el corpus.** El encuadre pedido para la sección 3 incluía dos frases atribuidas a Brinsa: *"Orchestration is not the magic. Orchestration is the seatbelt."* y *"If you can't explain how an agent's action gets blocked, logged, and reversed, you don't have orchestration. You have hope."* Ninguna aparece en `research/corpus/` ni en `research/web/`, y tampoco el nombre. Las dos láminas que desarrollaban esas ideas con material sí capturado ("Qué es blast radius" y "Los tres requisitos") salieron del deck el 2026-08-26, así que hoy la sección 3 no las sostiene desde ninguna lámina. Si el presenter quiere las citas textuales, hace falta ingestar la fuente con `/talksmith:ingest` antes de que vayan a lámina.
- **Anécdota del fondo de cobertura con 20+ pestañas de Claude Code sin registro en el corpus.** La confesión equivalente y capturada de Mark R. Hinkle, que el deck usaba en su lugar, se cortó con la lámina de apertura el 2026-08-28 y hoy sobrevive solo como cita dictable en las notas de la lámina que abre la sección 1. Si el presenter prefiere la anécdota del fondo, hace falta la fuente.
- **Duración contra cantidad de láminas.** 45 láminas más Thesis y Agenda para 2 horas dan unos 2,5 minutos por lámina (eran 39 y 3,1 antes de la sección 6). Entre la fusión de las secciones 2 y 3 y el corte de la sección de auditoría, el deck perdió 16 láminas respecto del draft revisado por el Composer y ahora sobra tiempo. Las cuatro láminas nuevas de la sección 3 (3.2, 3.3, 3.4 y 3.5) consumen parte de ese margen. Conviene decidir en el ensayo dónde se usa el resto: el caso trabajado (2.9 y 2.10), la discusión sobre gates en 4.10 y las preguntas son los candidatos naturales.
- **Las salvedades sobre Paperclip viven ahora solo en las notas del orador.** Con la sección de auditoría cortada, las cuatro correcciones que la clase hacía en lámina (el borde en que actúa el tope de gasto, el alcance real de Governance, el límite del self-hosting y la palabra `rewind`) quedaron repartidas entre el cuerpo de 4.1, 5.2 y 5.3 y las notas de 3.9, 4.6 y 4.7. El corte del 2026-08-26 se llevó dos de sus soportes: la salvedad de que la política de red solo aplica en proveedores de sandbox que la soporten (vivía en "Qué es blast radius") y el criterio de los tres requisitos con el que la clase juzgaba el radio de daño; la primera bajó a las notas de 5.2. Si el presenter dicta sin leer las notas, la sala escucha las promesas del sitio sin la letra chica. Decidir si alguna de esas líneas tiene que subir al cuerpo de su lámina.
- **Tres figuras renderizadas quedaron sin lámina.** La fusión de las secciones 2 y 3 cortó las láminas que usaban `s2-2-1` (fan-out de Cognition), `s2-7-1` (grafo de comunicación) y `s2-9-1` (hilo único con desborde de contexto). Los SVG y sus PNG siguen en `images/` y se pueden recuperar si alguna vuelve. Los `slide_id` se re-derivan de la posición, así que cada reordenamiento los mueve. Estado al 2026-08-26: el corte de siete láminas no movió ninguno de los ocho bloques, porque las cortadas no llevaban diagrama y todas caían después del último bloque de su sección (verificado bloque por bloque). Siguen pendientes de re-render tres de los ocho, por la unificación en `Task` del 2026-08-25 (`s3-3-1` la máquina de estados, `s3-9-1` las tres funciones y `sc-2-1` el árbol de decisión); los otros cinco conservan su sello.
- **`runtime` quedó usado sin definir, y es a propósito.** La lámina "Qué es un runtime", que era la 4.2 antes del corte, se borró a pedido del presenter (2026-08-25) y él eligió, consultado, dictar la definición de palabra en vez de mover la definición a otra lámina. El término sigue vivo en el cuerpo de 4.1 ("no provee el modelo ni el runtime"), en los rótulos del ASCII del organigrama de 4.2 (`claude_local`, `process`, `openclaw_gateway`, `codex_local`) y en las notas de 4.2, 5.1 y 5.2. El corte del 2026-08-26 se llevó dos de sus usos anteriores, la lámina del adapter y las Sources de "Los tres requisitos". **La más cara es la salvedad de gobierno de 4.7**: "Paperclip frena las acciones que pasan por Paperclip; lo que un agente hace adentro de su propio runtime, no". Sin el término definido, esa frase no se entiende, y es la corrección más importante que la clase le hace al material del producto. Las notas de 4.1 (primer uso), 4.2 y 4.7 llevan la frase corta para decir en sala. **Que una sesión futura no lo "arregle" creyendo que es un descuido**: el deck solo no se sostiene ahí y el presenter lo sabe.
- **`agente` volvió a estar definido en lámina, ahora como pregunta (2026-09-01).** El quiz de la lámina 1.3 pone la definición en pantalla como respuesta de la sala, así que lo que sigue describe el estado anterior y se conserva por el historial y por las dos fronteras, que siguen viviendo solo en notas. **`agente` quedó usado sin definir, y era a propósito.** La lámina "Qué es un agente", que era la 1.2 antes del corte, se borró a pedido del presenter (2026-08-26); esos números ya los ocupan otras láminas, así que buscarla por título en Cut material. Es la palabra que da nombre a la clase y aparece en la tesis, en las cinco secciones y en las cuatro de Conclusions. Las notas de la lámina que abre la sección 1 llevan la definición en una línea para decir en sala (estaban en «Diez agentes, ninguna organización» hasta que esa lámina se cortó el 2026-08-28, y bajaron con ella), con las dos fronteras que la audiencia del MiM necesita (frente al chat y frente al script) y el puntero al 4× de tokens, que se gasta en 2.5. **Que una sesión futura no lo "arregle" creyendo que es un descuido.**
- **`blast radius` / radio de daño quedó usado sin definir.** La lámina "Qué es blast radius", que era la 3.11 antes del corte, se borró a pedido del presenter (2026-08-26). El término sigue vivo en el paso 3 de Conclusions 3, que ahora trae su propia glosa en el cuerpo, y en las notas de 5.2 ("Qué es un sandbox"), donde bajaron la definición corta, la analogía de la puerta cortafuego y los tres destinos permitidos de la maqueta de red. Lo que se perdió sin reemplazo en lámina: la advertencia de que `api.anthropic.com` figura entre los destinos permitidos, que es la corrección que la clase le hace a la promesa de "100% of your data stays on your infra". Sobrevive en las notas de 5.3.
- **`adapter` quedó usado sin definir.** La lámina "Qué es un adapter", que era la 5.1 antes del corte, se borró a pedido del presenter (2026-08-26), en el mismo pedido que sacó `agente` y `blast radius`. Hoy la 5.1 es "Skills, Plugins y MCP". El término sigue vivo en las notas de 4.2 y en el cuerpo de 5.1 ("Skills, Plugins y MCP"); las dos llevan ahora la frase corta. Es la tercera pieza del glosario de la sección 5 que sale del deck después de `runtime` y `MCP`, así que esa sección quedó en tres láminas y su Goal ya no promete definir ni adapter ni runtime.
- **Cadena de objetivos: tres niveles contra cuatro.** El sitio dibuja cuatro (`Mission → Project Goal → Agent Goal → Task`) y su propia página de tasks cuenta tres (company goal, sub-goals por equipo, y el goal que el agente cita al tomar la tarea). No son la misma lista y ninguna fuente reconcilia las dos. Las láminas 3.5 y 3.6 usan la de cuatro, que es la que el sitio dibuja y la que el diagrama de 3.5 fija; la de tres queda en notas del orador. El porcentaje de avance (un company goal al 64%) sale del widget de la lista de tres, así que no se le pegó a ningún nivel de la de cuatro. Si el presenter quiere hablar de sub-goals por equipo, hay que decidir cuál de las dos listas se adopta en lámina.
- **El producto promete cortar en cualquier nivel y no dice dónde cae el trabajo cortado.** La página de gobernanza ofrece "Pause, cancel, and rewind controls at every level" y la de presupuestos un hard stop que "marks its work with a clear state"; ninguna de las dos nombra el estado resultante, y `cancelled` no aparece en ninguna fuente del corpus. La lámina 3.4 dibuja esas dos salidas como `PARKED` y `CANCELLED`, con una convención visual distinta de las cuatro cajas del sitio y con la aclaración en el cuerpo, en la atribución visible y en notas de que los dos nombres son de la clase. Tampoco está documentado el retorno desde el tope de gasto: el sitio dice que subir el tope es una aprobación y ahí se corta el rastro, así que el diagrama no dibuja la flecha de vuelta. Es letra chica de la promesa de controles de corte en todo nivel y da buena discusión de gobernanza. Si aparece documentación de Paperclip que nombre esos estados, hay que reemplazar los rótulos y sacar la salvedad.
- **Ciclo de vida de las Tasks: dos listas incompatibles en el corpus.** El sitio nombra `in progress / blocked / in review / done`; el newsletter de abril reporta `backlog → todo → in_progress → in_review → done`. Las láminas 3.1 y 3.2 usan la del sitio por ser la fuente primaria y más reciente, y el diagrama de 3.4 no dibuja ningún estado de la otra lista. El estado inicial del que arranca ese diagrama (`(creado)`) no está nombrado en ninguna fuente y va rotulado como arranque, no como valor del campo. Si el presenter quiere hablar de un backlog en lámina, hace falta decidir cuál de las dos listas se adopta.
- **Cantidad de adapters: tres listas distintas.** El sitio dice 7 y nombra cuatro; el newsletter enumera otros siete; la tira de logos da ocho nombres. La lámina que citaba dos fuentes con su fecha sin enumerar una lista única ("Qué es un adapter") salió del deck el 2026-08-26. Hoy ninguna lámina nombra adapters; las notas de 5.1 avisan de no dar un número si la sala pregunta. Definir si el presenter quiere fijar una lista.
- **Redibujo ASCII contra imagen del corpus.** Las figuras de Kore.ai (láminas 2.6 y 2.7) usan las imágenes originales del corpus. Las dos que quedan redibujadas como ASCII son la arquitectura de Anthropic (2.2) y las pilas de contexto (2.3), en ambos casos para tenerlas en la gramática visual del deck y no en la del autor original. Las imágenes originales están en disco si el presenter prefiere usarlas.
- **Las dos imágenes de Kore.ai son `.webp`.** Step 6 (b) las rasteriza a PNG antes del render, porque Keynote no embebe WebP. Sin acción del presenter.
- **Líneas de reporte del organigrama de demostración del sitio.** El widget de paperclip.ing lista cinco miembros sin decir quién reporta a quién. La lámina 4.2 usa en su lugar el árbol explícito del newsletter, que sí está dibujado en la fuente.
- **Imágenes pendientes de fase 2 del Librarian.** De las 66 imágenes del corpus, las 12 que importan están transcriptas. Las restantes conservan marcadores `<!-- pending​: process_images -->` y son chrome de sitio, avatares y logos, sin uso previsto en lámina.
- **Fase 2 corrida sobre `fig3-clio-usage-embedding-plot.webp`, sin uso en lámina.** El registro advierte que no tiene ejes, leyenda ni conteos. Sus porcentajes de uso (10% software, 8% contenido técnico, 8% estrategias de crecimiento, 7% investigación académica, 5% verificación de información) salen de la prosa del artículo. Queda disponible si el presenter quiere una lámina sobre quién usa research multi-agente.

# Cut material

- **Lámina "1.1 Diez agentes, ninguna organización" (cortada a pedido del presenter, 2026-08-28).** Era la lámina de apertura de la clase: la confesión de Mark R. Hinkle sobre su propio setup sin coordinación, usada como gancho del problema sentido antes de cualquier definición. La sección 1 pasa a abrir en "Objetivos" y baja de 5 a 4 láminas. Bajaron a las notas de esa nueva apertura, porque son carga de la clase y no de la lámina: la definición de agente con sus dos fronteras y el puntero al 4× de tokens (que ya venía acá desde el corte de "Qué es un agente" el 2026-08-26, y que una entrada de Open questions pide expresamente no perder), la pregunta de apertura a la sala sobre herramientas de AI corriendo sin saber qué gastan, la cita de Hinkle como línea dictable con su atribución, y la salvedad de que Hinkle es publisher de un newsletter y sirve para el problema y no para evaluar el producto. Se pierde la directiva `generate-image` de esta lámina, que nunca se había cumplido: quedan dos en el deck. Archivo verbatim:

  ## 1. Diez agentes, ninguna organización

  <!-- template: quote -->
  <!-- generate-image: right | dispersión sin centro: piezas capaces que trabajan cada una por su lado, sin nada que las una -->

  ### Content

  > «Agentes capaces. Coordinación cero. Ninguna misión compartida. Ninguna forma de ver de un vistazo qué me estaba costando cada cosa.»

  Mark R. Hinkle describe su propio setup antes de buscar una capa de gestión: una instancia de OpenClaw por acá, una sesión de Claude Code por allá, un par de scripts en cron a medio olvidar.

  `The AI Enterprise, abr-2026`

  ### Sources

  - `corpus/aienterprise-run-company-agents.web.md` — confesión de apertura del autor, verbatim; inventario del setup previo (OpenClaw, Claude Code, scripts en cron).

  ### Speaker notes

  **Original:** "Capable agents. Zero coordination. No shared mission. No way to see what anything was costing me at a glance." — [Mark R. Hinkle, The AI Enterprise, abril 2026](https://www.theaienterprise.io/p/run-company-ai-agents-paperclip).

  Abrir la clase acá, no con una definición. Es la lámina del problema sentido y funciona como gancho.

  El deck ya no trae lámina que defina agente, así que la definición va de palabra en algún momento de esta lámina o de la siguiente. Un agente es un modelo de lenguaje que usa herramientas en un loop; decide, ejecuta una acción, mira el resultado y vuelve a decidir. Hay dos fronteras que la sala necesita. Frente al chat, que responde y termina, el agente cambia algo afuera (escribe un archivo, abre un PR, manda un mail). Frente al script, que sigue un camino fijo, el agente elige el próximo paso según lo que encontró en el anterior. La definición es de [Anthropic, junio de 2025](https://www.anthropic.com/engineering/multi-agent-research-system), y el costo de esa libertad (unos 4× los tokens de un chat) se gasta en la lámina 2.5.

  Leer la cita despacio y dejar que caiga la última frase, que es la que duele: ninguna forma de ver de un vistazo qué estaba costando cada cosa.

  Preguntar a la sala cuántos tienen hoy más de una herramienta de AI corriendo sin saber qué gasta cada una. Suele levantar bastantes manos y ancla la clase en su realidad.

  Hinkle es publisher de un newsletter de AI, no un analista independiente, y está a mitad de camino de armar el setup que describe. Como fuente sirve para el problema, no para la evaluación del producto.

  ---

- **Lámina "3.1 De elegir patrón a rendir cuentas" (cortada a pedido del presenter, 2026-08-28).** Era la bisagra que cerraba el movimiento de arquitectura y abría el de gobierno: nombraba las dos preguntas del directorio —quién autorizó, cuánto costó— que la sección 3 contesta con la Task. Su par simétrico de la sección 1, "La pregunta que sigue", ya se había cortado el 2026-08-27, así que la sección 3 pasa a abrir directamente en "Qué es una Task" y baja de 10 a 9 láminas. El planteo de las dos preguntas no se pierde: bajó a las notas de esa lámina, que ahora abre la sección. Queda sin lámina propia la observación de que los tres patrones de coordinación tratan la trazabilidad como propiedad deseable sin darle mecanismo. Archivo verbatim:

  ## 1. De elegir patrón a rendir cuentas

  ### Content

  Las tres secciones anteriores contestaron **cómo se reparte el trabajo**. Ninguna contestó las dos preguntas que un directorio hace primero:

  - **¿Quién autorizó esto?** El patrón dice quién ejecuta. No dice quién aprobó.
  - **¿Cuánto costó?** El multiplicador dice cuánto gasta. No dice a qué se le imputa.

  Las dos se contestan con la misma pieza, y el resto de la clase se apoya en ella.

  ### Sources

  - `corpus/koreai-orchestration-patterns.web.md` — los tres patrones resuelven coordinación; la trazabilidad aparece como propiedad deseable, sin mecanismo propio.
  - `corpus/paperclip-tasks.web.md` — el ticket como unidad con dueño, estado, hilo y definition of done.

  ### Speaker notes

  Lámina bisagra. Sin ella la sala llega a la Task a mitad de la clase sin ver por qué el argumento se mueve de arquitectura a gobierno. Su par en la sección 1 se cortó, así que esta quedó sola haciendo ese trabajo: darle aire.

  Decirlo con esas palabras: hasta acá elegimos una forma de repartir trabajo. Lo que sigue es cómo se rinde cuenta de ese trabajo.

  La respuesta es una sola pieza y conviene no adelantarla; la lámina 3.9 la muestra entera.

  ---

- **Lámina "1.5 La pregunta que sigue" (cortada a pedido del presenter, 2026-08-27).** Era la transición que cerraba la sección 1 y abría el desacuerdo entre Anthropic y Cognition que la sección 2 desarrolla. La sección baja a 4 láminas y cierra en "El cambio de modelo mental". El puente no se pierde: bajó verbatim a las notas de esa lámina, con la pregunta del paralelismo y las dos respuestas. Su par simétrico, la 3.1, queda sola haciendo ese trabajo de bisagra, y su nota lo dice. Archivo verbatim:

  ## 5. La pregunta que sigue

  ### Content

  Si dirigir agentes se parece a dirigir un equipo, la primera decisión de diseño es la misma que en cualquier organización: **cuánto trabajo corre en paralelo**.

  - **La respuesta ingenua** Más agentes en paralelo, más rápido.
  - **La respuesta documentada** Depende del dominio, y las dos posiciones tienen evidencia.

  ### Sources

  - `corpus/cognition-dont-build-multi-agents.web.md`
  - `corpus/anthropic-multi-agent-research.web.md`

  ### Speaker notes

  Lámina de transición corta. Sirve para avisar que lo que viene es un desacuerdo real entre dos equipos serios y no una encuesta de opciones.

  Tiene su lámina simétrica en la apertura de la sección 3, que hace el mismo trabajo de bisagra hacia la tesis de la Task.

  ---

- **Lámina "1.2 Qué es un agente" (cortada a pedido del presenter, 2026-08-26, en el mismo pedido que movió siete láminas al Cut material).** El deck ya no define **agente**. El Goal de la sección 1 prometía dejarlo definido antes de cualquier argumento posterior y se reescribió; el multiplicador de 4× tokens sobrevive en 2.5, que es donde se gasta. La frase corta para decir en sala está en las notas de 1.1. Archivo verbatim:

  ## 2. Qué es un agente

  ### Content

  Un agente es un modelo de lenguaje que usa herramientas en un loop: decide, ejecuta una acción, mira el resultado y vuelve a decidir. Anthropic define así a un agente: *«modelos de lenguaje que usan herramientas de forma autónoma, en loop»*.

  - **Lo que lo separa de un chat** El chat responde y termina. El agente ejecuta acciones que cambian algo afuera: escribe un archivo, abre un PR, manda un mail.
  - **Lo que lo separa de un script** El script sigue un camino fijo. El agente elige el próximo paso según lo que encontró en el anterior.
  - **El costo de esa libertad** Un agente consume alrededor de 4× los tokens de una interacción de chat. `Anthropic, jun-2025`

  ### Sources

  - `corpus/anthropic-multi-agent-research.web.md` — definición "multiple agents (LLMs autonomously using tools in a loop) working together"; multiplicador de tokens 4× agente vs. chat.

  ### Speaker notes

  **Original:** "LLMs autonomously using tools in a loop" — [Anthropic, junio 2025](https://www.anthropic.com/engineering/multi-agent-research-system).

  La audiencia del MiM llega con la idea de "IA = chat", y todo el resto de la clase depende de que quede clara la diferencia entre responder y actuar.

  La frase citada define agentes en general dentro del artículo de Anthropic, no el sistema de Research en particular. Usarla con ese alcance.

  Si alguien pregunta por qué "autonomously": porque nadie aprueba cada paso intermedio. Ese hueco es el que la sección 3 llena con gates.

  El 4× lleva directo a la lámina siguiente, que define la unidad en la que se paga.

  ---

- **Lámina "2.10 Qué ve cada agente, y qué se valida" (cortada a pedido del presenter, 2026-08-26, en el mismo pedido que movió siete láminas al Cut material).** Deja a 2.9 ("Un caso: cómo se descompone") como un caso planteado y sin resolver: 2.9 descompone el pago del préstamo y esta lámina era la que mostraba qué ve cada agente y qué se valida antes de ejecutar. También era la bisagra explícita hacia la sección 3 (el registro como parte del patrón). Las notas de 2.9 recogen las dos ideas en una línea cada una. Archivo verbatim:

  ## 10. Qué ve cada agente, y qué se valida

  ### Content

  - **Cada agente recibe solo su parte del dato** Loan Agent ve datos de préstamo enmascarados. Transaction Manager ve saldo y umbrales de política, sin datos del préstamo. Payment Processor ve identificadores seudonimizados, sin PII (datos personales identificables).
  - **La validación ocurre antes de ejecutar** Que el saldo coincida con los fondos, que cumpla política y que la cotización siga vigente. Si algo no cierra, el orquestador replanifica.
  - **Todo queda registrado** El rastro de razonamiento y los detalles de la transacción quedan para cumplimiento y auditoría.

  `Kore.ai, oct-2025 (act. jul-2026)`

  ### Sources

  - `corpus/koreai-orchestration-patterns.web.md` — ejemplo "Supervisor — loan payoff", pasos 4, 6, 7 y 8 verbatim; "This ensures minimal data exposure while maintaining continuity"; "The reasoning trace and transaction details are logged for compliance and audit purposes".

  ### Speaker notes

  Punto uno: que cada agente vea solo su parte del dato es una decisión de diseño de seguridad, y es lo que la sección 3 llama radio de daño acotado. Es también la respuesta práctica a "¿y si un agente se comporta mal?": limitar lo que puede ver antes de que actúe.

  Sobre PII: son los datos con los que se puede identificar a una persona concreta (nombre, documento, número de cuenta). El caso los reemplaza por identificadores seudonimizados, que no valen nada fuera del sistema que los emitió. Aclarar que esto no tiene relación con los tokens que factura el proveedor del modelo, aunque la fuente en inglés use la palabra "tokenized" para las dos cosas. Son dos sentidos distintos: el token de facturación es un fragmento de texto que se cobra; el identificador seudonimizado es un reemplazo de un dato sensible. En el deck el segundo aparece siempre como "seudonimizado".

  Punto dos: la validación ocurre antes de ejecutar la transferencia, no después. Es un gate, aunque acá lo pase una máquina y no una persona.

  Punto tres es la bisagra hacia la sección 3: el registro no es un agregado, es parte del patrón.

  ---

- **Lámina "2.11 La receta, en cinco líneas" (cortada a pedido del presenter, 2026-08-26, en el mismo pedido que movió siete láminas al Cut material).** Era el cierre sintético de la sección 2 y la lámina que la sala fotografía; nació del pedido de la ronda 4 de "dar la receta de lo que sirve". Sin ella la sección 2 termina en el caso trabajado y la receta queda repartida en las nueve láminas que la construyen, sin lámina que la junte. Se pierde sin reemplazo el remate de Kore.ai ("elegir el patrón más simple que cumpla el requisito del negocio"), que bajó a las notas de 2.8. Archivo verbatim:

  ## 11. La receta, en cinco líneas

  <!-- format: editorial -->

  ### Content

  - **Repartir solo lo que lee** Lo que escribe sobre estado compartido va en un solo hilo, o con límites escritos antes.
  - **Pagar el reparto solo donde vale** Un sistema multi-agente consume alrededor de 15× lo que consume un chat. `Anthropic, jun-2025`
  - **Supervisor cuando importa la trazabilidad** Barato de construir, caro de operar. `Kore.ai, oct-2025`
  - **Red adaptativa cuando importa la latencia** Y nadie tiene la foto completa. `Kore.ai, oct-2025`
  - **A cada agente, solo su parte del dato** Y validar antes de ejecutar, no después. `Kore.ai, oct-2025`

  ### Sources

  - `corpus/anthropic-multi-agent-research.web.md` — multiplicador de 15× sobre chat; condición de viabilidad económica; el límite del dominio.
  - `corpus/koreai-orchestration-patterns.web.md` — tabla de selección de patrón; mínimo privilegio y validación previa en el ejemplo del pago del préstamo; "choose the simplest pattern that effectively meets your business requirements".
  - `corpus/cognition-dont-build-multi-agents.web.md` — el costo de repartir trabajo que muta estado compartido.

  ### Speaker notes

  Es la lámina que la sala fotografía. Las cinco líneas son la sección entera y ninguna necesita saber cómo funciona un modelo por dentro.

  El orden no es casual: las dos primeras deciden si se reparte, las dos del medio deciden la forma, y la última es la que se olvida y la que más cuesta cuando falla.

  La quinta línea es también la bisagra hacia la sección siguiente. Dar a cada agente solo su parte del dato y validar antes de ejecutar son decisiones que hay que poder mostrar después, y eso pide un lugar donde queden escritas.

  [Kore.ai](https://www.kore.ai/blog/choosing-the-right-orchestration-pattern-for-multi-agent-systems) lo resume en una regla que conviene decir: elegir el patrón más simple que cumpla el requisito del negocio.

  ---

- **Lámina "3.10 Tasks con dueño, no mensajes con onda" (cortada a pedido del presenter, 2026-08-26, en el mismo pedido que movió siete láminas al Cut material).** Cita de la página de producto. Era la promesa que 4.5 ("Una noche sin nadie mirando") se cobraba, y ese puntero se reescribió para valerse solo. El original en inglés, con su atribución, queda archivado acá. Archivo verbatim:

  ## 10. Tasks con dueño, no mensajes con onda

  <!-- template: quote -->

  ### Content

  > «Tasks con dueño, no mensajes con onda.»

  > «"Terminado" es un veredicto, no algo que el agente se autoproclama. Cada tarea tiene un solo dueño, un estado que significa algo, y un hilo que se lee como el registro que es.»

  `Paperclip, ago-2026`

  ### Sources

  - `corpus/paperclip-tasks.web.md` — los dos títulos de sección, verbatim.

  ### Speaker notes

  **Original:** "Tickets with owners, not messages with vibes." · "'Done' is a verdict, not a self-report. Every task has one owner, a status that means something, and a thread that reads like the record it is." — [paperclip.ing, agosto 2026](https://paperclip.ing/product/tasks/).

  **La cita está adaptada y hay que decirlo si alguien la busca.** El sitio escribe "Tickets with owners, not messages with vibes"; la lámina pone `Tasks` porque el deck unificó el término. La frase en inglés de arriba es la original, sin tocar.

  Las dos frases son de la página de producto de Paperclip y sirven como formulación breve de la tesis. Presentarlas como lo que son: copy de marketing bien escrito que da en el clavo conceptual.

  "Done is a verdict, not a self-report" tiene un paréntesis crítico que se cobra en la lámina 4.5: en la maqueta del propio sitio, quien verifica el trabajo de un agente a las 02:31 es otro agente (`Vera · QA · claude`). Avisar acá que ese punto vuelve, y dejarlo para allá.

  ---

- **Lámina "3.11 Qué es blast radius" (cortada a pedido del presenter, 2026-08-26, en el mismo pedido que movió siete láminas al Cut material).** El deck ya no define **blast radius / radio de daño**, y el término sigue vivo en el paso 3 de Conclusions 3 ("Definir el radio de daño"), en las notas de 5.2 ("Qué es un sandbox") y en el Goal de la sección 4. Con esta lámina se van también los tres destinos permitidos de la maqueta de red y la salvedad de que la política sólo aplica en proveedores de sandbox que la soporten. Archivo verbatim:

  ## 11. Qué es blast radius

  ### Content

  El blast radius es el conjunto de cosas que un agente puede dañar si se equivoca o si alguien lo manipula.

  - **Se acota antes de actuar** No se corrige después.
  - **Tres perillas** qué puede leer, a dónde puede salir a la red, con qué credenciales.
  - **Cómo se ve en concreto** La corrida de una Task sale a tres destinos y nada más: el repositorio, el proveedor del modelo y el registro de paquetes. Todo lo demás, denegado por defecto.

  `Paperclip, ago-2026 · mock-up`

  ### Sources

  - `corpus/paperclip-security.web.md` — "Autonomy with a blast radius you set"; "Agents move fast; the damage they can do stays bounded"; mock-up "Sandbox — network policy" con `Deny by default` y los tres destinos permitidos para la corrida `PAP-1042`. El registro rotula los visuales de la página como "Re-tabulated UI mock-ups".
  - `corpus/koreai-orchestration-patterns.web.md` — mínimo privilegio como parte del patrón supervisor: "The orchestrator provides each agent with only the data necessary to complete its task securely".

  ### Speaker notes

  El término viene de seguridad y la audiencia del MiM probablemente no lo tenga. Explicarlo con la analogía de la puerta cortafuego: no evita el incendio, limita hasta dónde llega.

  La formulación de Paperclip es buena y la clase se la puede quedar: la autonomía viene con un radio de daño que alguien define. Quien define ese radio es el manager, y es una decisión que hoy nadie está tomando de forma explícita en la mayoría de las organizaciones.

  Los tres destinos salen de [la política de red que el sitio muestra](https://paperclip.ing/product/security/) para la corrida de la Task `PAP-1042`: `api.github.com`, `api.anthropic.com` y `registry.npmjs.org`, con `* everything else` en `deny`. Es una maqueta, así que la forma es la enseñanza y los destinos son ilustrativos. Escribirlos en el pizarrón si la sala quiere verlos.

  Decir en voz alta la fila del proveedor del modelo, porque es la que corrige sola una promesa del propio sitio: la misma política que acota el radio de daño deja pasar `api.anthropic.com`. El sitio afirma en otra página que "100% of your data stays on your infra", y no es literal: Paperclip no recibe los datos, el proveedor del modelo sí. La lámina 5.4 lo dice de frente.

  Advertencia de la propia página: la política de red aplica solo en proveedores de sandbox que la soporten, y el aislamiento depende del proveedor y de la imagen que se configure. Paperclip provee la superficie para expresar el límite, no el aislamiento.

  Conecta directo con el punto 1 de la lámina 2.10: el reparto de datos del caso del préstamo es esta misma idea aplicada antes de que el agente actúe.

  ---

- **Lámina "3.12 Los tres requisitos" (cortada a pedido del presenter, 2026-08-26, en el mismo pedido que movió siete láminas al Cut material).** Era el criterio de cierre de la sección 3 — instrumentación, radio de daño acotado, mínimo privilegio — armado con tres registros del corpus que llegan al mismo lugar desde intereses distintos, y con él se va el método de triangulación que el Goal de la sección anuncia. La sección cierra ahora en "La prueba de la orquestación" (3.10). Archivo verbatim:

  ## 12. Los tres requisitos

  ### Content

  - **Instrumentación** Trazado de producción de las decisiones y las interacciones, más checkpoints para retomar desde donde falló. Anthropic lo describe como el sustrato con el que depura su propio sistema. `Anthropic, jun-2025`
  - **Radio de daño acotado** Workspace aislado por corrida, egress restringido a los destinos que la tarea necesita, entorno destruido al liberarse. `Paperclip, ago-2026`
  - **Acceso a herramientas con mínimo privilegio** Cada agente recibe solo el dato y la credencial que su tarea requiere; los secretos se resuelven en tiempo de despacho. `Kore.ai, oct-2025` · `Paperclip, ago-2026`

  ### Sources

  - `corpus/anthropic-multi-agent-research.web.md` — trazado completo de producción de patrones de decisión e interacción; retomar desde el punto de falla en vez de reiniciar; checkpoints y lógica de reintento.
  - `corpus/paperclip-security.web.md` — workspaces de ejecución aislados, leases, egress restringido, referencias a secretos resueltas en runtime, valores user-scoped nunca mostrados.
  - `corpus/koreai-orchestration-patterns.web.md` — mínimo privilegio en el patrón supervisor; sandbox gestionado con cifrado, RBAC y mínimo privilegio en el patrón custom.

  ### Speaker notes

  Los tres requisitos no salen de una sola fuente: se arman con tres registros del corpus que llegan al mismo lugar desde intereses distintos. Vale decirlo, porque el método importa tanto como la lista.

  Orden de aplicación en la práctica: primero mínimo privilegio (limita lo que se puede hacer), después radio de daño (limita hasta dónde llega lo que igual pasó), y la instrumentación al final porque solo sirve si las dos anteriores dejaron algo que registrar.

  [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system) agrega un matiz que vale mencionar: monitorean patrones de decisión y estructuras de interacción sin mirar el contenido de las conversaciones individuales, por privacidad. Es una decisión de diseño de auditoría que un manager puede copiar.

  ---

- **Lámina "5.1 Qué es un adapter" (cortada a pedido del presenter, 2026-08-26, en el mismo pedido que movió siete láminas al Cut material).** El deck ya no define **adapter**, que es la primera pieza que el Goal de la sección 5 nombra en su glosario. El término sigue vivo en las notas de 4.3 (el adapter `process` que ejecuta comandos de shell) y en 5.1 ("Skills, Plugins y MCP"). Se va también la inconsistencia de las tres listas de adapters, que queda sólo en Open questions. Archivo verbatim:

  ## 1. Qué es un adapter

  ### Content

  Un adapter es el puente entre Paperclip y el runtime que corre el agente. La definición del sitio es la más nítida: *«Sin un adapter, un agente es apenas un registro en una base de datos; con uno, es un miembro que trabaja en el equipo.»*

  - **Las claves son propias** `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, como variables de entorno bajo control del usuario.
  - **La factura del proveedor es propia** Nada pasa por un medidor de Paperclip.
  - **El adapter HTTP es la salida universal** Cualquier cosa que reciba un request HTTP puede ser empleado.

  `Paperclip, ago-2026` · `The AI Enterprise, abr-2026`

  ### Sources

  - `corpus/paperclip-bring-your-own-agent.web.md` — definición de adapter verbatim; variables de entorno nombradas; "Nothing routes through a Paperclip meter".
  - `corpus/aienterprise-run-company-agents.web.md` — "Anything that can receive an HTTP request can become an employee in your Paperclip org"; enumera siete adapters: claude_local, codex_local, gemini_local, cursor, process, http, openclaw_gateway.

  ### Speaker notes

  **Original:** "Without one an agent is just a record in a database; with one it is a working member of your team." — [paperclip.ing, agosto 2026](https://paperclip.ing/product/bring-your-own-agent/).

  El adapter vuelve real la promesa de bring your own agent, y es también donde el corpus deja una inconsistencia que conviene no repetir en lámina.

  [El sitio](https://paperclip.ing/product/bring-your-own-agent/) dice que vienen 7 adapters en la caja y nombra cuatro (claude_local, codex_local, gemini_local, hermes_local) "y más". El newsletter de abril enumera exactamente siete pero otros siete: claude_local, codex_local, gemini_local, cursor, process, http, openclaw_gateway. Sin Hermes y con dos adapters que no son LLM. La tira de logos da una tercera lista de ocho. Ninguna lámina debería enumerar adapters sin elegir una fuente con su fecha y decirlo.

  El adapter `process` merece un comentario: ejecuta comandos de shell arbitrarios, así que un script de siempre puede ser empleado del organigrama. Para management es el puente entre la automatización que ya existe en la empresa y esta capa nueva.

  ---
- **Lámina "4.2 Qué es un runtime" (borrada a pedido del presenter, 2026-08-25: "«Qué es un runtime» borrarlo, no es para esta audiencia").** Consultado sobre la consecuencia, el presenter eligió borrar solo la lámina y dictar la definición de palabra. El término `runtime` queda usado sin definir en el resto del deck (la salvedad de gobierno de 4.9, los rótulos del ASCII del organigrama, y las láminas de la sección 5); el hueco está registrado en Open questions y anotado en las notas de 4.3, que es la primera lámina que lo usa. Archivo verbatim:

  ## 2. Qué es un runtime

  ### Content

  El runtime es el programa que de verdad ejecuta al agente: el que habla con el modelo, corre las herramientas y produce el trabajo.

  - **Paperclip no es un runtime** Reparte tareas, mide gasto y guarda el rastro. El trabajo lo hace otro programa.
  - **Runtimes nombrados como soportados** Claude, Codex, Gemini, Cursor, Hermes, OpenClaw, Pi, OpenCode. También scripts de Python, comandos de shell y webhooks HTTP.
  - **Por qué importa para gobierno** Lo que un agente hace adentro de su propio runtime queda fuera del alcance de Paperclip: la plataforma gobierna lo que pasa por la plataforma. `Paperclip, ago-2026`

  `Paperclip, ago-2026`

  ### Sources

  - `corpus/paperclip-bring-your-own-agent.web.md` — "An adapter is the bridge between Paperclip and the AI system that actually runs an agent"; "Paperclip is a workforce layer, not a model"; strip de ocho runtimes.
  - `corpus/paperclip-home.web.md` — runtimes soportados; "anything that can receive a heartbeat signal".
  - `corpus/aienterprise-run-company-agents.web.md` — "What an individual agent does during a heartbeat is determined by its own system prompt and adapter runtime".

  ### Speaker notes

  Término sin el cual el tercer punto de esta lámina no aterriza. Definirlo acá, temprano, y volver a nombrarlo en cada lámina de la sección.

  El tercer punto es el límite más importante de todo el material de Paperclip y conviene decirlo con las palabras del propio FAQ del sitio: "Paperclip has governance and control modules for what your agents can do to modify Paperclip… However, your agents are your own and you secure them however you want to." Un tercero lo resume más corto: governance controla contrataciones, no conducta. El gate protege el organigrama; lo que el agente hace adentro de su runtime durante un heartbeat queda registrado, no frenado.

  La imagen que funciona: el runtime es el empleado que hace la tarea; Paperclip es la oficina donde ese empleado tiene escritorio, jefe y presupuesto. La oficina ve entrar y salir a la persona, y no ve lo que piensa mientras trabaja.

  El tercer punto es el que hay que dejar sembrado. Anunciarlo sin desarrollarlo; se cobra en 7.4.

- **Sección entera "6. Promesa y evidencia", 9 láminas (cortada a pedido del presenter, 2026-08-24: "Borrar la seccion 7").** Era la auditoría crítica del producto: las cuatro brechas documentadas entre lo que Paperclip promete y lo que su propia evidencia sostiene, más la lámina de método "Cómo leer una página de producto" y el cierre "Qué queda en pie". Al cortarla, las salvedades que vivían en ella y que siguen siendo ciertas se conservaron en las notas del orador de las láminas que hacen la afirmación (3.6 sobre el destino del proveedor del modelo, 4.2 sobre el alcance de Governance, 4.9 sobre el borde en que actúa el tope, 4.10 sobre el FAQ que acota el titular, 5.4 sobre el límite del self-hosting). Lo que no tiene dónde sobrevivir y se pierde con la sección: el método de lectura crítica de una página de producto, y todo el material de madurez del proyecto (entidad comercial, conteos de estrellas de GitHub, issues abiertos). Archivo verbatim de la sección completa, con su Goal:

  # 6. Promesa y evidencia

  **Goal of this section:** Aplicar a Paperclip el criterio que la sección 3 construyó, con cuatro brechas documentadas entre lo que el producto promete y lo que su propia evidencia sostiene. La sección enseña un método de lectura que sirve para cualquier producto, y cierra mostrando qué queda en pie.

  ---

  ## 1. Por qué auditar el instrumento

  ### Content

  La lección abstracta de la primera mitad se valida cuando se aplica al producto que la encarna.

  - **Todo lo que sigue viene del propio material del proveedor** o de una fuente que se puede fechar y nombrar.
  - **Ninguna de las cuatro brechas descalifica al producto** Marcan la distancia entre el titular y la letra chica.
  - **La habilidad que se lleva la clase** no es una opinión sobre Paperclip, es cómo leer la página de producto de cualquier herramienta de agentes.

  ### Sources

  - `corpus/paperclip-home.web.md`
  - `corpus/paperclip-budgets.web.md`
  - `corpus/paperclip-governance.web.md`
  - `corpus/paperclip-open-source.web.md`
  - `corpus/aienterprise-run-company-agents.web.md`

  ### Speaker notes

  Encuadrar la sección antes de entrar. Es una clase de management, no una demo de producto, y la diferencia se juega acá.

  Avisar que las cuatro brechas se encontraron leyendo el sitio contra sí mismo y contra un tercero fechado. Ninguna requiere acceso privilegiado ni conocimiento técnico profundo.

  ---

  ## 2. Brecha 1: el tope que no frena

  ### Content

  **La promesa:** *«pasarse del presupuesto es imposible, no apenas improbable.»*

  **La letra chica del propio FAQ:** al 100% de utilización el agente se auto-pausa y **se bloquean las tareas nuevas**. Aviso suave al 80%.

  **Un tercero fechado:** la aplicación del tope es mensual, no en tiempo real; adentro de un mismo heartbeat un agente todavía puede hacer llamadas caras. `The AI Enterprise, abr-2026`

  La formulación honesta: el tope frena en el borde de la tarea, no adentro de una llamada en curso.

  `Paperclip, ago-2026`

  ### Sources

  - `corpus/paperclip-budgets.web.md` — "overruns are impossible, not just unlikely", verbatim.
  - `corpus/paperclip-home.web.md` — FAQ: auto-pausa al 100% y bloqueo de tareas nuevas, aviso al 80%.
  - `corpus/aienterprise-run-company-agents.web.md` — "Budget enforcement is monthly, not real-time… within a single heartbeat, an agent can still make expensive calls before the cap applies" (abril 2026).

  ### Speaker notes

  **Original:** "overruns are impossible, not just unlikely." — paperclip.ing, página de Budgets, agosto 2026.

  Las tres evidencias son independientes entre sí y llegan al mismo lugar. La primera es el titular de marketing, la segunda es el FAQ del mismo sitio (pausar y bloquear tareas nuevas es una acción en el límite entre unidades de trabajo), la tercera es un tercero de abril de 2026.

  Separan cuatro meses el reporte de abril y la página de agosto, así que la brecha pudo haberse cerrado. Nada en el material lo verifica en ningún sentido.

  Conectar con la lámina 4.6: si el tope actúa entre tareas y la cadencia de heartbeat decide cuántas tareas hay por noche, las dos perillas se multiplican.

  ---

  ## 3. La señal en el código comentado

  ### Content

  El HTML del propio sitio trae una grilla de extensiones **comentada**, con la nota del desarrollador *«comentado hasta que tengamos extensiones de verdad»*.

  Una de las seis extensiones planeadas: **Cost Guardrails — auto-pause agents exceeding budget**.

  La página de Budgets vende esa misma auto-pausa como garantía central ya funcionando.

  `Paperclip, ago-2026`

  ### Sources

  - `corpus/paperclip-home.web.md` — grilla de extensiones comentada, recuperada por pasada a mano sobre `original.html`, con la nota del desarrollador y las seis extensiones planeadas (Slack Alerts, Cost Guardrails, GitHub Sync, Custom Heartbeats, Webhook Bridge, Build Your Own). El registro advierte que un bloque deshabilitado no es una promesa pública y no debe citarse como tal.
  - `corpus/paperclip-budgets.web.md` — la auto-pausa al tope vendida como propiedad central.

  ### Speaker notes

  **Original:** "commented out until we have real extensions" — comentario en el HTML de paperclip.ing, agosto 2026.

  Es la lección de método más fina de la sección y por eso tiene lámina propia.

  Decir con precisión qué es y qué no es: un bloque comentado en el HTML no es una promesa pública, y no corresponde citarlo como si el producto hubiera prometido algo. Sirve como tercer indicio, independiente de los dos anteriores, de que la aplicación de costos está menos completa que el titular.

  Es también la explicación de por qué la sección "Extensible, adaptable, open source" de la página en vivo no muestra ninguna extensión.

  Si alguien pregunta cómo se encuentra algo así: mirando el código fuente de la página, que en un sitio de marketing es público y suele estar menos cuidado que el texto.

  ---

  ## 4. Brecha 2: el alcance de Governance

  ### Content

  **El FAQ del propio sitio:** *«Paperclip tiene módulos de Governance y control para lo que tus agentes pueden hacerle a Paperclip; por ejemplo, contratar agentes nuevos pasa por aprobación del directorio por defecto. Pero tus agentes son tuyos y los asegurás como quieras.»*

  La lectura correcta: Paperclip puede frenar las acciones que pasan por Paperclip. Lo que un agente hace adentro de su propio runtime durante un heartbeat, no.

  `Paperclip, ago-2026`

  ### Sources

  - `corpus/paperclip-home.web.md` — FAQ, respuesta a "How do I keep agents from doing things I don't want?", verbatim.
  - `corpus/paperclip-governance.web.md` — pull-quote "Every sensitive action can stop at a human gate", verbatim: el titular que el FAQ acota.
  - `corpus/aienterprise-run-company-agents.web.md` — "Governance controls hiring, not behavior. Board approval is required to add agents to the org chart. What an individual agent does during a heartbeat is determined by its own system prompt and adapter runtime".

  ### Speaker notes

  **Original:** "Paperclip has governance and control modules for what your agents can do to modify Paperclip — for example, hiring new agents is gated by Board approval by default. However, your agents are your own and you secure them however you want to." — FAQ de paperclip.ing, agosto 2026.

  Es la brecha más importante de todo el material de Paperclip, y la que más consecuencias tiene para un manager que esté evaluando la herramienta.

  El titular que el FAQ acota está en la página de Governance: "Every sensitive action can stop at a human gate". Decirlo de memoria para montar el contraste, sin ponerlo en lámina.

  Un tercero lo dice más corto y sirve de remate: governance controla contrataciones, no conducta.

  La consecuencia práctica se apoya en el término definido en la lámina 4.2: el gate protege el organigrama, no la conducta. Si un agente contratado hace algo indebido adentro de su propio runtime, Paperclip lo registra pero no lo frenó. Diseñar las instrucciones responsables de cada agente sigue siendo trabajo aparte.

  Notar que el FAQ es la fuente más precisa del sitio y la que menos se ve: está al pie de la home, no en la página de Governance. Enseñar a buscar ahí.

  Conectar con la prueba de la lámina 3.8. De las tres preguntas, Paperclip responde bien la de registrar y la de detener. La de bloquear la responde con un alcance más angosto que el que anuncia.

  ---

  ## 5. Brecha 3: "100% de tus datos"

  ### Content

  **La promesa:** *«el 100% de tus datos se queda en tu infraestructura.»*

  **La tabla de la propia página de seguridad:**

  | Regla | Destino | Propósito | Veredicto |
  |---|---|---|---|
  | egress | api.anthropic.com | model provider | **allow** |

  El self-hosting protege de Paperclip. No protege del proveedor del modelo, que sigue recibiendo prompts, código y contenido de las tareas.

  `Paperclip, ago-2026`

  ### Sources

  - `corpus/paperclip-open-source.web.md` — stat strip "100% of your data stays on your infra"; el registro del Librarian marca que la afirmación no es literalmente cierta y que el sitio lo sabe.
  - `corpus/paperclip-security.web.md` — allow-list del sandbox con `egress · api.anthropic.com · model provider · allow`; "you run the instance… with your own model-provider keys".

  ### Speaker notes

  **Original:** "100% of your data stays on your infra." — paperclip.ing, página de Open Source, agosto 2026.

  Es la brecha que conviene subrayar con una audiencia sensible a cumplimiento, y la única de las cuatro que se resuelve leyendo dos páginas del mismo sitio una al lado de la otra.

  La afirmación precisa: Paperclip no recibe los datos. El proveedor del modelo sí. Y la propia página de seguridad lo dibuja en su lista de destinos permitidos, la misma política de red que nombra la lámina 3.6.

  La frase que el sitio usa hace un trabajo cuidadoso y vale leerla despacio: "the honest answer to 'where does our data go' is: nowhere it wasn't already". Es cierta si los datos ya iban a Anthropic antes. Es una respuesta sobre el cambio, no sobre el estado.

  ---

  ## 6. Brecha 4: la entidad comercial

  ### Content

  | Señal | Fuente | Fecha | Estado |
  |---|---|---|---|
  | Liderazgo seudónimo, sin financiamiento, sin entidad comercial que dé soporte | analista independiente | ~jun 2026 | **reportado, no verificable**: la captura falló |
  | "© 2026 Paperclip Labs, Inc." en el pie del sitio, más páginas de Careers y Newsroom | sitio de Paperclip | ago 2026 | evidencia primaria |

  ### Sources

  - `corpus/rywalker-paperclip-research.web.md` — debilidades reportadas: liderazgo seudónimo, sin financiamiento, sin entidad comercial. **Reconstrucción a mano: el fetcher recibió connection reset y no existe `original.html`. La propia fuente pide re-verificar toda cifra.**
  - `corpus/paperclip-home.web.md` — pie de página "© 2026 Paperclip Labs, Inc." recuperado a mano del `original.html`, con links a Careers y Newsroom. El registro advierte: "Neither claim should go on a slide without a check of the live site".

  ### Speaker notes

  **Re-verificar antes de dictar.** Es la afirmación reputacional más filosa del deck y viene de la única captura que falló. Entrar a rywalker.com/research/paperclip y al pie de paperclip.ing el día de la clase. Si no se puede, la celda ya está redactada en forma condicional y hay que leerla así en voz alta: reportado, no verificable.

  El pie de página con la razón social es evidencia primaria y contradice la forma más fuerte de la crítica. El analista pudo haber escrito antes de la constitución de la sociedad.

  Dato que conviene dejar en notas y no en lámina, por su estado: la misma reconstrucción reporta 4.953 issues abiertos contra 105 contribuidores históricos, una relación de unos 47 a 1. Sería la cifra más filosa del caso negativo y es la que más falta hace verificar.

  La enseñanza es de método: una debilidad atribuida a un tercero que resulta falsa es peor que ninguna debilidad.

  ---

  ## 7. Brecha 4: las estrellas de GitHub

  ### Content

  | Cifra | Fuente | Fecha | Estado |
  |---|---|---|---|
  | 44.000 | newsletter de terceros | abr 2026 | fechada, de tercero |
  | 53.487 | analista independiente | abr 2026 | reconstrucción a mano, sin verificar |
  | 69.955 | analista independiente | jun 2026 | reconstrucción a mano, sin verificar |
  | 74k+ | sitio de Paperclip | ago 2026 | primaria, la más reciente |

  Ninguna cifra viaja sin su fecha y su fuente.

  ### Sources

  - `corpus/aienterprise-run-company-agents.web.md` — 44.000 estrellas en menos de tres semanas, abril 2026.
  - `corpus/rywalker-paperclip-research.web.md` — 53.487 → 69.955 entre abril y junio de 2026; reconstrucción a mano, sin verificar.
  - `corpus/paperclip-open-source.web.md` — "74k+" estrellas, agosto 2026; el registro reúne las cuatro cifras con sus fechas y recomienda usar la del proveedor o ninguna.

  ### Speaker notes

  La lámina no está para decidir si Paperclip creció. Está para mostrar que cuatro cifras del mismo indicador se contradicen y que dos de ellas no son verificables.

  Las dos de abril son las que peor cierran: 44.000 y 53.487 con nueve mil de diferencia en el mismo mes. Una curva de crecimiento monótona las reconcilia solo si están separadas por varias semanas.

  Si hay que usar una sola, usar 74k+ de paperclip.ing en agosto de 2026 y decir de dónde salió.

  El punto que importa para management: las estrellas de GitHub miden atención, no adopción ni uso en producción. Una audiencia de negocio las escucha como adopción y no lo son.

  ---

  ## 8. Cómo leer una página de producto

  ### Content

  - **Leer el sitio contra sí mismo** El FAQ suele ser más preciso que el titular, y está más abajo.
  - **Buscar la página que se cubre con salvedades** Cuando una sección se pone cuidadosa, la escribió quien construyó la cosa.
  - **Preguntar dónde aplica el límite** En el borde de la tarea, adentro de la llamada, al cierre del mes. Cambia todo.
  - **Fechar cada cifra y nombrar cada fuente** Y separar lo capturado verbatim de lo reconstruido.
  - **Distinguir capacidad de estado** "100% de las acciones externas *pueden* requerir firma" significa que se pueden configurar, no que estén configuradas.

  ### Sources

  - `corpus/paperclip-home.web.md` — el FAQ como fuente más precisa que el titular.
  - `corpus/paperclip-security.web.md` — la página más hedgeada del sitio.
  - `corpus/paperclip-governance.web.md` — "100% of external actions can require sign-off" como afirmación de capacidad presentada con forma de estadística.
  - `corpus/paperclip-open-source.web.md` — tabla de cifras de estrellas con fecha y procedencia.

  ### Speaker notes

  Es la lámina que justifica la sección entera y probablemente la que más valor tenga a largo plazo para esta audiencia. Los cinco criterios se aplican a cualquier herramienta, no a esta.

  El quinto merece énfasis. "100% of external actions can require sign-off" está escrito con forma de estadística y es una afirmación de capacidad. Ese truco aparece en casi todo sitio de software empresarial.

  Ejercicio posible si sobra tiempo: darle a la sala otra página de producto de agentes y pedir que encuentren la brecha en cinco minutos.

  ---

  ## 9. Qué queda en pie

  ### Content

  - **La abstracción es correcta y es portable** El ticket con dueño, estado y rastro gobierna un equipo de agentes, use el producto que use.
  - **El instrumento hace bien tres cosas** registrar por corrida, frenar en cualquier nivel, y atribuir cada acción a un objetivo.
  - **Los límites reales son dos** el gate cubre lo que pasa por la plataforma, y el tope de gasto actúa entre tareas.
  - **La decisión de un manager no cambia** definir qué acciones se aprueban, qué presupuesto se asigna y quién lee el rastro.

  ### Sources

  - `corpus/paperclip-tasks.web.md`
  - `corpus/paperclip-governance.web.md`
  - `corpus/paperclip-home.web.md`
  - `corpus/aienterprise-run-company-agents.web.md`

  ### Speaker notes

  Cerrar la sección sin dejarla en tono de demolición. Las cuatro brechas hacen más útil al producto para quien lo evalúa, porque le dicen dónde poner su propio control.

  El punto que sostiene la tesis de la clase: la abstracción sobrevive a la auditoría del producto. El ticket sigue siendo la pieza correcta aunque este producto en particular la implemente con límites.

- **Lámina "2.2 Cognition: «Almost Surely Unreliable»" (cortada a pedido del presenter, 2026-08-24: "dejar solo «Anthropic: +90,2% con la misma forma» y no Cognition. Ni lo mencionemos").** Existía para montar el desacuerdo con Anthropic, que la sección ya no plantea. Su figura (`s2-2-1`) queda sin uso. Archivo verbatim:

  ## 2. Cognition: "Almost Surely Unreliable"

  ### Content

  Walden Yan, de Cognition (los que hacen Devin), descarta esta arquitectura por principio y le pone ese veredicto en el margen del diagrama.

  ```ascii
                          Task
                           |
                           v
               +--------------------------+
               | Agent                    |
               | breaks down task         |
               +--------------------------+
                  |                    |
            Subtask 1              Subtask 2
                  v                    v
          +--------------+      +--------------+
          |  Subagent 1  |      |  Subagent 2  |
          +--------------+      +--------------+
                  |                    |
            Result 1               Result 2
                  v                    v
               +--------------------------+
               | Agent                    |
               | combines the results     |
               +--------------------------+
                           |
                           v
                         Result
  ```
  <!-- ascii-note:
  intent: la arquitectura fan-out / fan-in que Cognition rechaza; se compara lamina a lamina con la de Anthropic, asi que las dos deben compartir gramatica visual.
  emphasize: el rombo completo (una caja arriba, dos en paralelo al medio, una que combina abajo); la ausencia total de conexion horizontal entre Subagent 1 y Subagent 2.
  labels: Task, Subtask 1, Subtask 2, Result 1, Result 2, Result.
  -->

  `Cognition, jun-2025`

  ### Sources

  - `corpus/cognition-dont-build-multi-agents.web.md` — fig1 `fig1-parallel-subagents.png`, transcripción completa; veredicto de esquina "Almost Surely Unreliable"; nombra `swarm` (OpenAI) y `autogen` (Microsoft) como librerías que empujan el enfoque equivocado.

  ### Speaker notes

  El diagrama original es de Excalidraw, dibujado a mano, con el veredicto escrito en la esquina superior izquierda. Acá se redibuja en la misma gramática que el de Anthropic para que la sala vea que son la misma forma.

  El ejemplo con el que Cognition lo explica es Flappy Bird: subtarea 1 construye un fondo con caños verdes, subtarea 2 construye un pájaro. El subagente 1 entiende mal y hace un fondo tipo Super Mario Bros; el subagente 2 hace un pájaro que ni parece ni se mueve como el de Flappy Bird. El agente final queda con la tarea de combinar dos malentendidos.

  Cognition no publica ningún número. El argumento es de principio y de ejemplo, y conviene decirlo antes de mostrar el 90,2% de Anthropic.

- **Lámina "2.4 La misma figura, dos veredictos" (cortada en la misma ronda).** Era el dispositivo del par enfrentado: sin los dos veredictos no tiene objeto. Archivo verbatim:

  ## 4. La misma figura, dos veredictos

  ### Content

  Dos equipos serios dibujaron el mismo diagrama en el mismo mes y le pusieron etiquetas opuestas.

  | | Cognition | Anthropic |
  |---|---|---|
  | Fecha | 12 jun 2025 | 13 jun 2025 |
  | Veredicto | "Almost Surely Unreliable" (casi con certeza, poco confiable) | +90,2% sobre agente único |
  | Tipo de evidencia | principio y ejemplo, sin números | eval propia, sin rúbrica publicada |
  | Producto que venden | Devin (agente de código) | Claude Research |

  `Cognition, jun-2025` · `Anthropic, jun-2025`

  ### Sources

  - `corpus/cognition-dont-build-multi-agents.web.md` — fecha 06.12.25; ausencia de evidencia cuantitativa; el post cierra con pitch de producto y búsqueda de talento.
  - `corpus/anthropic-multi-agent-research.web.md` — fecha 13 jun 2025; el post describe un producto que Anthropic vende.

  ### Speaker notes

  El punto de método para la audiencia: los dos son vendedores describiendo la arquitectura que les conviene, y aun así el desacuerdo es real y se resuelve con una variable identificable. La lámina 2.6 la nombra.

  Un día de diferencia entre las publicaciones. No hay respuesta de uno al otro; llegaron a conclusiones opuestas en paralelo.

- **Lámina "2.6 La variable que reconcilia: el dominio" (reemplazada en la misma ronda).** La regla del dominio sobrevive entera en la lámina 2.4 "Cuándo repartir, y cuándo no", ahora enunciada como receta y no como reconciliación de un desacuerdo. Archivo verbatim:

  ## 6. La variable que reconcilia: el dominio

  ### Content

  - **Investigación de solo lectura** El subagente lee, destila y devuelve un hallazgo. Dos subagentes que leen fuentes distintas no se pisan.
  - **Código que muta estado compartido** Cada acción cambia el terreno del otro. Dos subagentes que editan el mismo repositorio sí se pisan.

  Anthropic marca el límite con sus propias palabras: *«la mayoría de las tareas de código tienen menos partes realmente paralelizables que las de investigación, y los agentes todavía no son buenos coordinando ni delegando entre ellos en tiempo real»*

  `Anthropic, jun-2025`

  ### Sources

  - `corpus/anthropic-multi-agent-research.web.md` — el límite del dominio, verbatim; criterios de encaje positivo ("valuable tasks that involve heavy parallelization, information that exceeds single context windows, and interfacing with numerous complex tools").
  - `corpus/cognition-dont-build-multi-agents.web.md` — el dominio de Cognition es código, donde las acciones mutan estado compartido.

  ### Speaker notes

  **Original:** "most coding tasks involve fewer truly parallelizable tasks than research, and LLM agents are not yet great at coordinating and delegating to other agents in real time." — Anthropic, junio 2025.

  Es la lámina que convierte una pelea de opiniones en un criterio aplicable. Anthropic concede el punto estructural con nombre y apellido: en código hay menos tareas realmente paralelizables que en research.

  La pregunta que la audiencia se lleva para sus propios casos: ¿el trabajo que quiero repartir lee o escribe? Leer tolera paralelismo. Escribir sobre algo compartido, no.

  El apéndice de Anthropic agrega una tercera vía que se puede mencionar si hay tiempo: hacer que los subagentes escriban su salida a un sistema de archivos y devuelvan solo una referencia liviana, para evitar el teléfono descompuesto.

- **Lámina "2.7 La concesión de Anthropic" (cortada en la misma ronda).** Sin el desacuerdo, su único mensaje restante (los dos subagentes no se mandan mensajes) duplica la lámina 2.3, que muestra la misma regla con más información: qué ve y qué no ve cada hermano. El grafo de comunicación (`s2-7-1`) está renderizado y en disco por si el presenter quiere una segunda vista. Archivo verbatim:

  ## 7. La concesión de Anthropic

  ### Content

  Anthropic concede el punto estructural de Cognition: en su propio sistema, los hermanos no se ven. Su respuesta es que en búsqueda de solo lectura no hace falta que se vean.

  ```ascii
        +--------------------------+                  +--------------------+
        |  Lead agent              |    pide las      |  Subagente         |
        |  (orquestador)           |--------------->  |  de citas          |
        +--------------------------+      citas       +--------------------+
               ^                ^
    asigna y   |                |   asigna y
    recibe     |                |   recibe
               v                v
     +-----------------------+       +-----------------------+
     |      Subagente 1      |       |      Subagente 2      |
     +-----------------------+       +-----------------------+

         Subagente 1 y Subagente 2 solo se tocan a traves del Lead agent
  ```
  <!-- ascii-note:
  intent: grafo de comunicacion entre los cuatro agentes del sistema de Research; el hallazgo es la ARISTA QUE NO EXISTE entre Subagente 1 y Subagente 2. NO dibujar esto como diagrama de secuencia: tres rondas de critica ciega mostraron que la forma de secuencia contradice su propio epigrafe, porque cada mensaje cruza el corredor que el epigrafe declara vacio.
  emphasize: el hueco entre Subagente 1 y Subagente 2, que debe ser la region vacia mas grande del cuadro; los dos subagentes acentuados en rojo para que el ojo caiga ahi; las tres aristas que si existen, todas pasando por el Lead agent.
  labels: Lead agent (orquestador), Subagente de citas, Subagente 1, Subagente 2; aristas "asigna y recibe" x2 (bidireccionales) y "pide las citas" (una sola direccion); epigrafe al pie.
  -->

  `Anthropic, jun-2025`

  ### Sources

  - `corpus/anthropic-multi-agent-research.web.md` — fig2 `fig2-process-diagram-full-workflow.png`, transcripción completa de los mensajes en orden; el registro señala que no existe mensaje alguno entre `Subagent1` y `Subagent2`. El deck redibuja esa relación como grafo de comunicación en vez de como diagrama de secuencia: el hecho citado es el mismo, la forma de mostrarlo cambia.

  ### Speaker notes

  Este es el hallazgo más preciso de la investigación y conviene decirlo con esas palabras: el desacuerdo entre Cognition y Anthropic no está en la forma de la arquitectura, está en si los hermanos necesitan verse. Anthropic dice que en búsqueda de solo lectura no hace falta, y su propio sistema está armado así.

  El dibujo muestra quién le habla a quién y nada más. Todo lo que sigue es lo que describe el paper y no está en la imagen, así que va hablado:

  El orden de los mensajes. El agente principal piensa el plan, lo guarda en `Memory` y recién después crea los subagentes. Esa escritura del plan ocurre antes de que exista ningún subagente, así que el estado del plan se externaliza a propósito: la ventana de contexto del lead no sobrevive el loop.

  La repetición. Toda la fase de subagentes está adentro de un loop con condición de reentrada ("¿hace falta más investigación?"), así que el fan-out del dibujo se repite en rondas en vez de dispararse una sola vez.

  El cierre. La inserción de citas es una pasada terminal, después de que la investigación terminó, y no algo que hagan los subagentes de búsqueda mientras trabajan. En el grafo eso se ve como una arista que sale del Lead agent, sin orden.

  Las tres cosas viven en el diagrama de secuencia original de Anthropic (`fig2` del registro). Si alguien las pide, la referencia está en Sources.

- **Lámina "2.9 Un solo hilo, y su techo" (cortada en la misma ronda).** Existía para motivar la alternativa de un solo hilo que el desacuerdo hacía necesaria. La regla sobrevive como línea en 2.4 y como hoja del árbol de decisión de Conclusions 2; el desborde de contexto queda en las notas de 4.8. Su figura (`s2-9-1`) queda sin uso. Archivo verbatim:

  ## 9. Un solo hilo, y su techo

  ### Content

  El default de Cognition es un solo hilo con contexto continuo. La figura que lo dibuja termina en `Result`; la que muestra su límite, no.

  ```ascii
       Task
        |
        v
    +--------------------------+     [G]
    | Agent breaks down task   |
    +--------------------------+
    | Agent does subtask 1     |     [G][B1]
    +--------------------------+
    | Agent does subtask 2     |     [G][B1][B2]
    +--------------------------+
    | Agent does subtask 3     |    ,--[G][B1][B2][P]--,
    +--------------------------+    |  context overflow |
        :                           `-------------------'
        :
        :
        :
  ```
  <!-- ascii-note:
  intent: el agente lineal de hilo unico, extendido hasta que la pila de contexto desborda; la figura original NO llega a una caja Result, y esa falta de cierre es deliberada.
  emphasize: la pila de fichas que crece de a una por caja y nunca pierde ninguna; el recuadro punteado de context overflow; los cuatro puntos verticales del final, que reemplazan al Result de las figuras anteriores.
  labels: leyenda [G] [B1] [B2] [P] como en la lamina 2.5; context overflow.
  -->

  `Cognition, jun-2025`

  ### Sources

  - `corpus/cognition-dont-build-multi-agents.web.md` — fig3 `fig3-single-threaded-linear-agent.png` (veredicto "Simple & Reliable"); fig4 `fig4-context-window-overflow.png` (caption de esquina "but struggles with longer tasks…", recuadro rojo de context overflow, elipsis vertical de cuatro puntos sin `Result`).

  ### Speaker notes

  La honestidad de la figura importa y conviene no limpiarla: figs 4 y 5 de Cognition terminan en una elipsis vertical y ninguna llega a una caja `Result`. El diagrama falla en terminar a propósito. Aplanarlo en un flujo prolijo exageraría la posición de Cognition.

  Lo que fig3 muestra: el mismo trabajo que fig1, en los mismos cuatro pasos, con la única diferencia de que nada corre en paralelo. El precio de la confiabilidad se paga en tiempo de reloj.

  Lo que fig4 muestra: la pila de contexto que hacía confiable a fig3 es exactamente lo que la rompe a escala. La restricción es la ventana de contexto y no el organigrama.

  La propuesta de Cognition para eso (fig5) es un modelo dedicado a comprimir la historia, con la salvedad textual "(but hard to get right)". En esa figura la caja `Context Compression LLM` está dibujada sin conectarse a nada, así que el diagrama nunca dice qué dispara la compresión. Si se muestra fig5 en clase, decir esa limitación en voz alta.

- **Lámina "2.10 Lo que la sección deja decidido" (reemplazada en la misma ronda).** Cerraba la sección vieja; la reemplaza "2.11 La receta, en cinco líneas", que cierra la sección fusionada con las cinco decisiones en vez de con las tres conclusiones del desacuerdo. Archivo verbatim:

  ## 10. Lo que la sección deja decidido

  ### Content

  - **Si el trabajo lee** El paralelismo paga, y hay una medición que lo respalda.
  - **Si el trabajo escribe sobre estado compartido** Un solo hilo, o límites explícitos entre quienes escriben.
  - **En los dos casos** La decisión de cuánto paralelizar es económica antes que técnica: depende de si la tarea vale ~15× los tokens de un chat.

  `Anthropic, jun-2025` · `Cognition, jun-2025`

  ### Sources

  - `corpus/anthropic-multi-agent-research.web.md`
  - `corpus/cognition-dont-build-multi-agents.web.md`

  ### Speaker notes

  Cierre de sección. Recoger las tres líneas y avisar que la sección siguiente muestra las formas concretas que toma esa decisión cuando hay que implementarla.

  Primera candidata de recorte si el ensayo se pasa de tiempo: los tres puntos vuelven casi textuales en la lámina 1 de Conclusions.

- **Lámina "3.4 Lo que la tabla no dice en palabras" (fusionada en la misma ronda).** El intercambio que la tabla esconde (Complejidad baja contra Uso de tokens alto y Latencia más alta) pasó a ser el remate en negrita de la lámina 2.8, debajo de la tabla que lo evidencia. Archivo verbatim:

  ## 4. Lo que la tabla no dice en palabras

  ### Content

  Tres filas consecutivas de la columna Supervisor: **Complejidad baja**, **Uso de tokens alto**, **Latencia más alta**.

  El patrón supervisor es el barato de construir y el caro de operar.

  `Kore.ai, oct-2025 (act. jul-2026)`

  ### Sources

  - `corpus/koreai-orchestration-patterns.web.md` — filas adyacentes `Complexity: Low`, `Token usage: High`, `Latency: Higher` en la columna del patrón supervisor; el registro del Librarian marca que el intercambio nunca se enuncia en el texto del artículo.

  ### Speaker notes

  Vale leer las tres celdas en voz alta y dejar que la sala arme la frase. Cada salto pasa por el hub, así que sube la latencia; el orquestador relee contexto en cada ronda, así que sube el gasto de tokens.

  Es el mismo intercambio que la sección 2 dejó planteado con el 15×, ahora expresado como propiedad de un patrón concreto. Barato de construir, caro de correr, y la factura llega mensual.

  Para management: el costo de construcción es visible en el proyecto, el costo de operación aparece después, y las decisiones de arquitectura se toman con el primero a la vista.

- **Lámina "3.7 Radio de daño, en concreto" (cortada a pedido del presenter, 2026-08-24: "Borrar el slide «Radio de daño, en concreto»").** Los tres destinos permitidos y el `deny by default` pasaron al tercer bullet de la lámina 3.6 "Qué es blast radius", con la etiqueta `· mock-up`; la advertencia sobre proveedores de sandbox y el gancho hacia la Brecha 3 bajaron a las notas de esa misma lámina. Archivo verbatim:

  ## 7. Radio de daño, en concreto

  ### Content

  Política de red para la corrida de un solo ticket, `PAP-1042`, en workspace aislado. Encabezado: **Deny by default**.

  | Regla | Destino | Propósito | Veredicto |
  |---|---|---|---|
  | egress | api.github.com | source + PRs | allow |
  | egress | api.anthropic.com | model provider | allow |
  | egress | registry.npmjs.org | package install | allow |
  | egress | * everything else | no egress | **deny** |

  `Paperclip, ago-2026 · mock-up`

  ### Sources

  - `corpus/paperclip-security.web.md` — mock-up "Sandbox — network policy", tabla completa verbatim; contexto "run PAP-1042 · isolated workspace". El registro rotula los visuales de la página como "Re-tabulated UI mock-ups".

  ### Speaker notes

  Es el artefacto de seguridad más concreto del corpus y funciona muy bien con audiencia no técnica: el agente que trabaja en el ticket PAP-1042 puede alcanzar exactamente tres lugares de internet.

  Decir que es una maqueta del sitio y no la captura de un deployment real. La forma es la enseñanza; los destinos son ilustrativos.

  Guardar la fila de `api.anthropic.com` para la sección 7. La misma tabla que demuestra el radio de daño acotado es la que contradice el "100% of your data stays on your infra" que el sitio afirma en otra página.

  Advertencia de la propia página: la política de red aplica solo en proveedores de sandbox que la soporten, y el aislamiento depende del proveedor y de la imagen que se configure. Paperclip provee la superficie para expresar el límite, no el aislamiento.

- **Lámina "5.2 Qué es MCP" (cortada a pedido del presenter, 2026-08-24: "Borrar «Qué es MCP», ya lo explicamos").** Antes de cortarla se verificó que "Skills, Plugins y MCP" no llevaba la definición: el bullet de MCP se amplió ahí para desplegar la sigla (Model Context Protocol), definir el estándar y nombrar los permisos por agente. La analogía del enchufe y el hueco del modelo de permisos bajaron a las notas de esa lámina. Archivo verbatim:

  ## 2. Qué es MCP

  ### Content

  MCP (Model Context Protocol) es el estándar por el que un agente descubre y usa herramientas externas: una base de datos, un CRM, un stack de observabilidad.

  - **El agente las usa como cualquier otra herramienta** No hay integración a medida por cada sistema.
  - **Los permisos son por agente** Cada agente ve el conjunto de herramientas que se le concedió.
  - **En la maqueta del sitio** `crm-tools` figura como MCP, en estado `Connected`.

  `Paperclip, ago-2026`

  ### Sources

  - `corpus/paperclip-extensions.web.md` — definición de servidor MCP ("your database, your CRM, your observability stack. Agents discover and use them like any other tool"); descubrimiento de herramientas MCP por agente, con permisos; widget "Extensions" con `crm-tools` (MCP, Connected).

  ### Speaker notes

  Sigla que esta audiencia probablemente haya oído sin que nadie se la desplegara. Desplegarla completa: Model Context Protocol.

  La analogía útil: MCP es el enchufe estándar. Antes cada herramienta necesitaba su propio cable a medida; con MCP el agente descubre lo que hay enchufado y lo usa.

  El modelo de permisos no está descrito en ningún lado del corpus más allá de "per agent, with permissions", y no se ve cómo se relaciona con el modelo de roles y grants de la página de seguridad. Decirlo como hueco.

- **Lámina "1.3 Qué es un token" (eliminada a pedido del presenter, 2026-08-24: "Borrar slide 5").** La definición del token bajó a una línea de lámina en 2.8, la primera que gasta el número, y la nota de 3.6 que desambiguaba los dos sentidos de "token" se reescribió para valerse sola. Archivo verbatim de la lámina:

  ## 3. Qué es un token

  ### Content

  El token es la unidad en la que los proveedores de modelos miden y facturan el texto: un fragmento de palabra. Todo lo que un agente lee y escribe se cobra en tokens, de entrada y de salida.

  - **Es la unidad de la factura** El proveedor publica un precio por millón de tokens, y ese precio cambia según el modelo.
  - **Un agente no gasta como un chat** ~4× un chat. Un sistema multi-agente, ~15×. `Anthropic, jun-2025`
  - **Por eso el presupuesto se pone por agente** En la maqueta del sitio de Paperclip, los topes mensuales van de $100 a $300 por agente. `Paperclip, ago-2026 · mock-up`

  ### Sources

  - `corpus/anthropic-multi-agent-research.web.md` — multiplicadores 4× (agente) y 15× (multi-agente) sobre chat; el uso de tokens explica 80% de la varianza de desempeño en BrowseComp.
  - `corpus/paperclip-budgets.web.md` — widget "Budgets — July": topes por agente de $100 (Scribe), $150 (Vera), $250 (CodexCoder) y $300 (Atlas). Rango $100–$300 leído de esas cuatro filas.
  - `corpus/koreai-orchestration-patterns.web.md` — "Token consumption and cost efficiency" como primera de las cuatro dimensiones que mueve la elección de patrón.

  ### Speaker notes

  Lámina obligatoria: sin ella la sala asiente al 15× sin poder convertirlo en plata, y el 15× es el número que sostiene toda la decisión económica de la clase.

  **Traer el precio vigente al dictado.** El material capturado no incluye ninguna lista de precios, así que el precio por millón de tokens del proveedor que se vaya a mencionar hay que buscarlo el día de la clase y decirlo en voz alta acá. Con ese número, los multiplicadores se vuelven pesos.

  La cuenta que conviene hacer en el pizarrón con el precio del día: cuánto sale una tarea como chat, ese número por 15, y comparado contra el tope mensual de un agente.

  Advertencia de vocabulario que se cobra en la sección 3: "tokenizar" en seguridad de datos significa reemplazar un dato sensible por un identificador sin valor, y no tiene nada que ver con los tokens de facturación. En esta clase ese segundo sentido aparece como "seudonimizados" para no cruzar los dos significados.

- **Lámina "Audit trail" (era 5.10 del draft anterior).** Eliminada por redundancia: tres de sus cuatro bullets repetían casi palabra por palabra la lámina 3.3 (registro por corrida con comandos, commits, comentarios y costos; "la respuesta es un link") y el punto 3 de la lámina 3.8 (controles en vuelo). El único contenido nuevo, el feed de actividad de toda la compañía, se fusionó en la lámina 4.10 (Governance y aprobaciones). La cita "Agents cite the skill they followed in the run log" se conservó en la lámina 5.2.
- **Cifra de variación de tokens entre patrones de Kore.ai ("sometimes by more than 200%").** Fuera de lámina: el registro del corpus marca que no tiene fuente, ni línea base, ni contexto de medición. Queda en las notas del orador de la lámina 2.8.
- **Ratio de issues abiertos sobre contribuidores (4.953 / 105 ≈ 47:1).** Fuera de lámina: viene de la reconstrucción a mano de la página del analista, que el fetcher no pudo capturar y que pide re-verificar toda cifra. Queda en las notas del orador de la lámina 6.6.
- **Comparación con CrewAI (1.400 millones de automatizaciones agénticas en PwC, IBM, Capgemini, NVIDIA).** Fuera de lámina por ser cifra de tercera mano y por abrir un tema de mercado que la clase no necesita. Queda en las notas del orador de la lámina 4.1.
- **Imagen hero de The AI Enterprise (`run-company-ai-agents-paperclip.png`).** Fuera del deck: es un render de marketing 3-D, casi con seguridad generado por AI, y el registro del corpus advierte que no es una figura publicada por Paperclip ni una afirmación sobre cómo funciona. Sirve como opción atmosférica si el presenter la quiere, con la advertencia dicha.
- **Figura 5 de Cognition (`fig5-context-compression-model.png`, compresión de contexto).** Fuera del deck: dependía de la lámina "Un solo hilo, y su techo", cortada en la misma ronda. La compresión de contexto sobrevive como una línea en las notas de la lámina 4.8. Advertencia si vuelve: en esa figura la caja `Context Compression LLM` está dibujada sin conectarse a nada, así que el original nunca dice qué dispara la compresión.
- **Los ocho principios de prompting de Anthropic.** Fuera del deck: son material de ingeniería y la clase es de management. Dos de ellos sobreviven adentro de otras láminas (escalar el esfuerzo a la complejidad, y delegar con objetivo, formato de salida y límites de tarea explícitos).
- **Patrón custom de Kore.ai con su ejemplo de revisión regulatoria de riesgo.** Fuera de lámina propia: aparece como columna en la tabla de decisión de la lámina 2.8. El ejemplo trabajado queda disponible si el presenter quiere una lámina extra sobre sectores regulados.
- **Rainbow deployments y evaluación de agentes (LLM-as-judge, evals de muestra chica, evaluación de estado final).** Fuera del deck por alcance. Es el material con el que se cubriría el área "Agent Employee Training" de Paperclip, que no tiene página capturada en el corpus.
`````
