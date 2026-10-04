---
source_file: wikipedia-intelligent-agent/
source_type: web-capture
ingested_at: 2026-10-04
---

# Intelligent agent (Wikipedia, English)

## Provenance
- Original location: research/web/wikipedia-intelligent-agent/ (`page.md` used as text input; 79 KB, many headings, no fallback to `original.html` needed; `original.html` consulted only to check the last-edited date and to grep for PEAS)
- Format: html (web capture via `talksmith:ingest`)
- URL: https://en.wikipedia.org/wiki/Intelligent_agent
- Fetched at: 2026-10-04T21:07:47Z (HTTP 200, 362,473 bytes)
- Author / source (if known): Wikipedia contributors (English Wikipedia). The taxonomy section rests on Russell & Norvig, *Artificial Intelligence: A Modern Approach*, 2nd ed. (2003), ch. 2, pp. 46–54; the agent / rational-agent definitions cite the 4th ed. (2021), chapter "Intelligent Agents".
- Date of original (if known): page footer says "This page was last edited on 4 October 2026, at 05:07".
- Hatnotes on the page: "Software agent which acts autonomously"; "Not to be confused with AI agent"; "Not to be confused with Embodied agent".

## Key claims

### General definition
- "An **intelligent agent** is an entity that perceives its environment, takes actions autonomously to achieve goals, and may improve its performance through by acquiring knowledge." (sic, see Inconsistencies.)
- Range: from a basic thermostat or control system to a human being, or "any other system that meets the same criteria—such as a firm, a state, or a biome" (cites Russell & Norvig 2003, ch. 2).
- AI agents ("also known as agentic AI") are "a specialized subset of intelligent agents" that "expand this concept by proactively pursuing goals, making decisions, and taking actions over extended periods."
- Intelligent agents operate on an objective function that encapsulates their goals, and are designed to create and execute plans that maximize the expected value of that function. Examples: RL agent → reward function; evolutionary algorithm → fitness function.
- Also referred to with a term borrowed from economics: "rational agent". Closely related to software agents (autonomous programs that act on behalf of users).

### Agent-based definition of AI (Russell & Norvig, 2021)
- AI = "the study of agents that receive percepts from an environment and perform actions."
- "An **agent** is anything that perceives its environment through sensors and acts upon that environment through actuators."
- "A **rational agent** selects the action expected to maximize its performance measure, given its percept sequence, prior knowledge, and available actions."
- Rationality "does not require an agent to be omniscient or always successful; it concerns the expected outcome of an action on the basis of the information available to the agent."
- Agent-oriented computing characterizes agents by autonomy, responsiveness to environmental change, and goal-directed / proactive behavior (Padgham & Winikoff 2004). BDI architecture models an agent by its information about the world (beliefs), objectives (desires), and committed courses of action (intentions) (Rao & Georgeff 1995).

### Classic taxonomy — Russell & Norvig (2003), five classes
The page states: "Russell & Norvig (2003) group agents into five classes based on their degree of perceived intelligence and capability" (cites pp. 46–54). Each class, as defined on the page:

1. **Simple reflex agents** — "act only on the basis of the current percept, ignoring the rest of the percept history. The agent function is based on the *condition-action rule*: 'if condition, then action'." It "only succeeds when the environment is fully observable." In partially observable environments "infinite loops are often unavoidable"; randomizing actions may allow escape. Example: a home thermostat that turns on or off when the temperature drops below a certain point.
2. **Model-based reflex agents** — "can handle partially observable environments. Its current state is stored inside the agent, maintaining a structure that describes the part of the world which cannot be seen." This knowledge about "how the world works" is "a model of the world, hence the name 'model-based agent'." It maintains an internal model "that depends on the percept history and thereby reflects at least some of the unobserved aspects of the current state", then "chooses an action in the same way as reflex agent." An agent may also use models to describe and predict the behavior of other agents (Albrecht & Stone 2018).
3. **Goal-based agents** — "further expand on the capabilities of the model-based agents, by using 'goal' information. Goal information describes situations that are desirable. This provides the agent a way to choose among multiple possibilities, selecting the one which reaches a goal state." Search and planning are the AI subfields devoted to finding action sequences that achieve goals. Examples given: ChatGPT and the Roomba vacuum (cited to a popular-press article, see Inconsistencies).
4. **Utility-based agents** — goal-based agents "only distinguish between goal states and non-goal states"; a utility function "maps a state to a measure of the utility of the state", allowing comparison of world states by how well they satisfy the agent's goals ("how 'happy' the agent is"). "A rational utility-based agent chooses the action that maximizes the expected utility of the action outcomes" — what it expects to derive on average given probabilities and utilities of each outcome. It "has to model and keep track of its environment".
5. **Learning agents** — learning "lets agents begin in unknown environments and gradually surpass the bounds of their initial knowledge." Four components: the **learning element** (improves performance), the **performance element** / "actor" (chooses external actions; "once considered the entire agent"), the **critic** (gives feedback to the learning element on how the agent is doing), and the **problem generator** (suggests "new and informative experiences that encourage exploration").

Note on the build-up: the page describes each class as extending the previous one (model-based adds internal state; goal-based "further expand[s]" model-based; utility-based refines goals into a graded measure). The diagrams for goal-based and utility-based are explicitly labelled "Model-based, goal-based agent" and "Model-based, utility-based agent". Learning agents are presented as a general architecture, not as a further rung.

### PEAS
- **The page does not mention PEAS** (Performance measure, Environment, Actuators, Sensors). It does contain three of the four ingredients separately: *performance measure* (in the rational-agent definition), *sensors* and *actuators* (in the agent definition), and *environment*. See Inconsistencies.

### Other taxonomies and characterizations
- **Weiss (2013)**, four classes: logic-based agents (decisions by logical deduction); reactive agents (direct mapping situation → action); belief–desire–intention agents (manipulate data structures for beliefs, desires, intentions); layered architectures (decision-making across multiple software layers, each reasoning at a different abstraction level).
- **Kasabov (1998)**, characteristics intelligent agent systems should exhibit: accommodate new problem-solving rules incrementally; adapt online and in real time; analyze themselves in terms of behavior, error and success; learn and improve through interaction with the environment (embodiment); learn quickly from large amounts of data; memory-based exemplar storage and retrieval; parameters for short- and long-term memory, age, forgetting, etc.
- Wissner-Gross (2013): theory relating freedom and intelligence in agents ("Causal Entropic Forces").

### Hierarchies of agents (links to Multi-agent system as main article)
- "Intelligent agents can be organized hierarchically into multiple 'sub-agents.' These sub-agents handle lower-level functions, and together with the main agent, they form a complete system capable of executing complex tasks and achieving challenging goals."
- An agent is structured into sensors and actuators; perception feeds a central controller that commands the actuators; "often, a multilayered hierarchy of controllers is necessary to balance the rapid responses required for low-level tasks with the more deliberative reasoning needed for high-level objectives" (Poole & Mackworth).

### Agentic AI
- In generative AI, AI agents ("also called compound AI systems") operate autonomously in complex environments; "prioritize decision-making over content creation and do not require human prompts or continuous oversight." Attributes: complex goal structures, natural-language interfaces, acting independently of user supervision, integration of software tools or planning systems; control flow frequently driven by LLMs; memory systems and orchestration software.
- "Researchers and commentators have noted that AI agents do not have a standard definition" (Kapoor et al. 2024 "AI Agents That Matter"; TechCrunch; Business Insider).
- Examples listed: Devin AI, AutoGPT, SIMA; since 2025: OpenAI Operator, ChatGPT Deep Research, Manus, Accio Work (Alibaba), Quark (Qwen), AutoGLM Rumination, Coze (ByteDance), nexos.ai, OpenClaw. Frameworks: LangChain, CAMEL, Microsoft AutoGen, OpenAI Swarm.

## Definitions and terminology
- **Agent** (R&N 2021): anything that perceives its environment through sensors and acts upon it through actuators.
- **Rational agent** (R&N 2021): selects the action expected to maximize its performance measure, given its percept sequence, prior knowledge, and available actions. Not omniscient; judged on expected outcome given available information.
- **Percept**: "the agent's sensory inputs at a single point in time" (e.g., a self-driving car's camera images, lidar, GPS, speed at an instant).
- **Percept sequence / history**: the agent's entire perceptual history; P* = set of all possible percept sequences ("zero or more percepts").
- **Agent function**: f : P* → A — "maps the agent's entire history of percepts to an action" (cites R&N 2003 p. 33). Abstract mathematical description.
- **Agent program**: "the actual code that runs on the agent"; "takes the *current* percept as input and produces an action as output." Distinct from the agent function.
- **Condition-action rule**: "if condition, then action" — basis of the simple reflex agent.
- **Model of the world**: internal knowledge about "how the world works", stored state describing unobserved parts of the world.
- **Goal information**: describes desirable situations; goal states vs non-goal states.
- **Utility function**: maps a state to a measure of its utility (desirability); enables graded comparison of states.
- **Learning element / performance element ("actor") / critic / problem generator**: the four components of a learning agent (see Key claims).
- **Objective function (goal function)**: specifies the agent's goals and the trade-offs among conflicting goals; synonyms by field — utility function (economics, decision theory), objective function (optimization), loss function (ML, minimized), reward function (RL), fitness function (evolutionary systems). Goals can be explicitly defined or induced (learned/evolved).
- **Abstract intelligent agent**: abstract (theoretical) description of an agent, as opposed to a real implementation.
- **AIXI**: proposed maximally intelligent agent formalism; uncomputable.
- **Reward shaping**: giving rewards for incremental progress instead of setting reward equal to the benchmark evaluation function (Ng, Harada & Russell 1999).

## Evidence and examples
- Thermostat as minimal intelligent agent and as the example of a simple reflex agent (refs 22–23: unstop.com blog, IBM "Types of AI Agents").
- Go objective: 1 for a win, 0 for a loss. AlphaZero chess: +1 per win, −1 per loss. Self-driving car objective balances safety, speed, passenger comfort.
- Yann LeCun (2018): "Most of the learning algorithms that people have come up with essentially consist of minimizing some objective function."
- GANs framed as agents: generator maximizes how well it fools the discriminator.
- Nearest-neighbor systems reason by analogy rather than explicit goals, but can be benchmarked as if their goal were the classification task.
- Applications: agent-based modeling for self-driving (2003); Hallerbach et al. digital twin + microscopic traffic simulation; Waymo's Carcraft multi-agent simulator; Salesforce Agentforce; TSA biometric/incident-response agentic AI; AWS Amazon Connect Health (March 2026), first HIPAA-eligible AI agent platform.

## Inconsistencies / open questions
- [verified] PEAS is not in this source — grepped `page.md` and `original.html` for "PEAS" (case-insensitive) and for "performance measure, environment": zero matches. A slide citing this record for the PEAS acronym would overreach; the PEAS definition must come from another record (a grep of the corpus shows `russell-norvig-aima.web.md` and `aig4b-clase-6-agentes-biomedica.pdf.md` mention PEAS — not verified here, not touched).
- [verified] Grammatical slip in the lead: "may improve its performance through by acquiring knowledge" — read verbatim in `page.md` line 51. Quote with "(sic)" or paraphrase.
- [verified] Edition mismatch within the page: the agent / rational-agent definitions cite R&N 4th ed. (2021), while the five-class taxonomy and the agent function cite the 2nd ed. (2003) — checked in references 1, 6, 19, 21 and the Sources list. Cite the edition matching the claim used.
- [verified] The learning-agent diagram labels differ from the prose: it says "Effectors" (prose and other diagrams say "Actuators") and misspells "Perfomance Standard" — checked visually on `500px-IntelligentAgent-Learning.svg.png`. The prose never mentions the "performance standard" input to the critic.
- [verified] Two different simple-reflex diagrams on the page with different wording ("What is the world like now" / "Action to be done" / "Condition-action (if-then) rules" in the lead image vs "What the world is like now" / "What action I should do now" / "Condition-action rules" in the section image) — compared both images.
- [open question] "ChatGPT and the Roomba vacuum are examples of goal-based agents" rests on a popular-press source (Inverse, 2024, ref. 25), not on R&N; whether a chat model fits the goal-based class is debatable — settle against R&N or a technical source before using it on a slide.
- [open question] The thermostat example for simple reflex agents is cited to a blog (unstop.com) and IBM marketing (refs 22–23), not to R&N directly — R&N's own canonical example (the vacuum world) would settle it; consult `russell-norvig-aima.web.md`.
- [open question] The page says R&N "group agents into five classes"; some editions of AIMA present four basic agent programs plus learning agents as a general method of improving any of them — check AIMA ch. 2 if the slide states "five types" as R&N's exact claim.
- [open question] Reference 5 (Mishra 2025, Amazon KDP, "p. XX") is a placeholder citation in the article — low reliability for the "abstract functional systems" sentence it supports.
- [open question] Recent examples (Accio Work 2026, OpenClaw, Amazon Connect Health March 2026) come from a page edited the same day as capture; not checked against primary sources.

## Images / diagrams

### wikipedia-intelligent-agent.web/images/IntelligentAgent-SimpleReflex.png
- Provenance: lead image of the page ("Simple reflex agent diagram"), from upload.wikimedia.org File:IntelligentAgent-SimpleReflex.png; 480×354 PNG.
- Depiction: Box diagram with two large rounded containers, AGENT (left) and ENVIRONMENT (right). An arrow labelled "percepts" goes from the environment into "Sensors" at the top of the agent; Sensors → box "What is the world like now" → box "Action to be done", which also receives an arrow from a rounded box "Condition-action (if-then) rules"; "Action to be done" → "Actuators" → arrow labelled "actions" back into the environment.
- Why it matters: canonical simple-reflex loop: current percept + if-then rules → action, with no internal state. Direct visual for the first rung of the taxonomy.
- Transcribed text: AGENT; ENVIRONMENT; percepts; Sensors; What is the world like now; Condition-action (if-then) rules; Action to be done; Actuators; actions.

### wikipedia-intelligent-agent.web/images/500px-Simple_reflex_agent.png
- Provenance: section "Simple reflex agents", File:Simple_reflex_agent.png (500px thumb); 500×220 grayscale PNG.
- Depiction: Same structure as the lead diagram, redrawn in the series style shared by the next three diagrams: Agent container (left), vertical Environment container (right, label rotated). Precepts arrow (sic) → Sensors → "What the world is like now" → "What action I should do now" (also fed by "Condition-action rules") → Actuators → Actions arrow to Environment.
- Why it matters: first of a four-diagram series that adds one block at a time (state/model → prediction → goals → utility); good for a "build-up" slide.
- Transcribed text: Agent; Environment; Sensors; Precepts [sic, "Percepts"]; What the world is like now; Condition-action rules; What action I should do now; Actuators; Actions.

### wikipedia-intelligent-agent.web/images/500px-Model_based_reflex_agent.png
- Provenance: section "Model-based reflex agents", File:Model_based_reflex_agent.png; 500×220 grayscale PNG.
- Depiction: Simple-reflex diagram plus three internal inputs feeding "What the world is like now": "State" (with a dashed feedback line from the top of the agent's processing back into State), "How the world evolves", and "What my actions do". Then "Condition-action rules" → "What action I should do now" → Actuators → Actions.
- Why it matters: shows exactly what "model-based" adds — internal state plus a model of world dynamics and of the effects of the agent's own actions, so the agent can act under partial observability.
- Transcribed text: State; How the world evolves; What my actions do; Sensors; Precepts [sic]; What the world is like now; Condition-action rules; What action I should do now; Actuators; Actions; Environment; Agent.

### wikipedia-intelligent-agent.web/images/500px-Model_based_goal_based_agent.png
- Provenance: section "Goal-based agents", caption "Model-based, goal-based agent", File:Model_based_goal_based_agent.png; 500×290 grayscale PNG.
- Depiction: Model-based diagram with a new prediction step: "What the world is like now" → "What it will be like if I do action A" (also fed by "How the world evolves" and "What my actions do") → "What action I should do now", which is also fed by a "Goals" box. Condition-action rules are gone. Then Actuators → Actions.
- Why it matters: shows the jump from reacting to deliberating: the agent simulates the consequence of an action and checks it against goals (search/planning).
- Transcribed text: State; How the world evolves; What my actions do; Sensors; Precepts [sic]; What the world is like now; What it will be like if I do action A; Goals; What action I should do now; Actuators; Actions; Environment; Agent.

### wikipedia-intelligent-agent.web/images/500px-Model_based_utility_based.png
- Provenance: section "Utility-based agents", caption "Model-based, utility-based agent", File:Model_based_utility_based.png; 500×379 grayscale PNG.
- Depiction: Goal-based diagram with "Goals" replaced by "Utility", which feeds a new box "How happy I will be in such a state" placed between "What it will be like if I do action A" and "What action I should do now". Then Actuators → Actions.
- Why it matters: shows that utility turns the binary goal test into a graded score over predicted states, which is what lets the agent trade off and pick the best of several goal-reaching actions.
- Transcribed text: State; How the world evolves; What my actions do; Sensors; Precepts [sic]; What the world is like now; What it will be like if I do action A; Utility; How happy I will be in such a state; What action I should do now; Actuators; Actions; Environment; Agent.

### wikipedia-intelligent-agent.web/images/500px-IntelligentAgent-Learning.svg.png
- Provenance: section "Learning agents", caption "A general learning agent", File:IntelligentAgent-Learning.svg (500px PNG thumb); 500×306 PNG.
- Depiction: Agent container (left) and ENVIRONMENT (right). "percepts" → Sensors, which feed both "Critic" and "Performance element". "Perfomance Standard" [sic] → Critic. Critic → "feedback" → "Learning element". Learning element → "changes" → Performance element; Performance element → "knowledge" → Learning element. Learning element → "learning goals" → "Problem Generator" → "experiments" → Performance element. Performance element → "Effectors" → "actions" → Environment.
- Why it matters: the four-component learning architecture (critic, learning element, performance element, problem generator) in one picture; the performance element alone is the whole agent of the earlier diagrams.
- Transcribed text: Agent; Perfomance Standard [sic]; Critic; Sensors; percepts; feedback; Learning element; changes; knowledge; Performance element; learning goals; Problem Generator; experiments; Effectors; actions; ENVIRONMENT.

### wikipedia-intelligent-agent.web/images/5e46430775928ac0bb01bcc51d8b725266e37aa9.svg
- Provenance: section "Agent function", MathJax SVG render from wikimedia.org math API (saved in the capture as `.bin`, renamed `.svg`; content is SVG).
- Depiction: Rendered formula of the agent function.
- Why it matters: the formal definition of an agent as a mapping from percept histories to actions.
- Transcribed text: `f : P* → A,` (LaTeX: `f\colon P^{*}\rightarrow A,`)

### wikipedia-intelligent-agent.web/images/19037f76d8eedef2ccc15a9cd3c61cb6a48bc542.svg
- Provenance: section "Agent function", MathJax SVG (renamed from `.bin`).
- Depiction: Bold symbol P*.
- Why it matters: set of all possible percept sequences (inline symbol in the definition list).
- Transcribed text: `P*` (LaTeX: `{\boldsymbol {P^{*}}}`)

### wikipedia-intelligent-agent.web/images/5a8b5a6d1dbadead8b1dc48719c888e6cac5f861.svg
- Provenance: section "Agent function", MathJax SVG (renamed from `.bin`).
- Depiction: Bold symbol A.
- Why it matters: set of all possible actions.
- Transcribed text: `A` (LaTeX: `{\boldsymbol {A}}`)

### wikipedia-intelligent-agent.web/images/9637dfaeb3214b577efe019ad53b8269f042e306.svg
- Provenance: section "Agent function", MathJax SVG (renamed from `.bin`).
- Depiction: Bold symbol f.
- Why it matters: the agent function itself.
- Transcribed text: `f` (LaTeX: `{\boldsymbol {f}}`)

### wikipedia-intelligent-agent.web/images/enwiki-25.svg
- Provenance: page header, Wikipedia globe icon.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### wikipedia-intelligent-agent.web/images/wikipedia-wordmark-en-25.svg
- Provenance: page header, "Wikipedia" wordmark.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### wikipedia-intelligent-agent.web/images/wikipedia-tagline-en-25.svg
- Provenance: page header, "The Free Encyclopedia" tagline.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### wikipedia-intelligent-agent.web/images/20px-Symbol_category_class.svg.png
- Provenance: AI navbox at the foot of the page, category icon (20×21).
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### wikipedia-intelligent-agent.web/images/20px-OOjs_UI_icon_edit-ltr-progressive.svg.png
- Provenance: navbox "Edit this at Wikidata" pencil icon (20×20).
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

## Raw / preserved excerpts

> An **intelligent agent** is an entity that perceives its environment, takes actions autonomously to achieve goals, and may improve its performance through by acquiring knowledge. Intelligent agents can range from simple to highly complex. A basic thermostat or control system is considered an intelligent agent, as is a human being, or any other system that meets the same criteria—such as a firm, a state, or a biome.

> In artificial intelligence, a specialized subset of intelligent agents, AI agents (also known as agentic AI) expand this concept by proactively pursuing goals, making decisions, and taking actions over extended periods.

> Intelligent agents operate based on an objective function, which encapsulates their goals. They are designed to create and execute plans that maximize the expected value of this function upon completion. For example, a reinforcement learning agent has a reward function, which allows programmers to shape its desired behavior. Similarly, an evolutionary algorithm's behavior is guided by a fitness function.

> Intelligent agents are often described schematically as abstract functional systems similar to computer programs. To distinguish theoretical models from real-world implementations, abstract descriptions of intelligent agents are called abstract intelligent agents. Intelligent agents are also closely related to software agents—autonomous computer programs that carry out tasks on behalf of users. They are also referred to using a term borrowed from economics: a "rational agent".

**Agent-based definition of artificial intelligence**

> Russell and Norvig describe artificial intelligence as the study of agents that receive percepts from an environment and perform actions. In this framework, an **agent** is anything that perceives its environment through sensors and acts upon that environment through actuators. A **rational agent** selects the action expected to maximize its performance measure, given its percept sequence, prior knowledge, and available actions. Rationality in this sense does not require an agent to be omniscient or always successful; it concerns the expected outcome of an action on the basis of the information available to the agent.

> In agent-oriented computing, agents are also commonly characterized by properties such as autonomy, responsiveness to changes in their environment, and goal-directed or proactive behavior. One approach to modeling practical reasoning is the belief–desire–intention (BDI) architecture, which represents an agent in terms of its information about the world, its objectives, and the courses of action to which it has committed.

**Objective function**

> An objective function (or goal function) specifies the goals of an intelligent agent. An agent is deemed more intelligent if it consistently selects actions that yield outcomes better aligned with its objective function. In effect, the objective function serves as a measure of success.
>
> The objective function encapsulates *all* of the goals the agent is designed to achieve. For rational agents, it also incorporates the trade-offs between potentially conflicting goals. For instance, a self-driving car's objective function might balance factors such as safety, speed, and passenger comfort.

> The mathematical formalism of AIXI was proposed as a maximally intelligent agent in this paradigm. However, AIXI is uncomputable. In the real world, an intelligent agent is constrained by finite time and hardware resources, and scientists compete to produce algorithms that achieve progressively higher scores on benchmark tests with existing hardware.

**Agent function**

> An intelligent agent's behavior can be described mathematically by an agent function. This function determines what the agent *does* based on what it has *seen*.
>
> A percept refers to the agent's sensory inputs at a single point in time. For example, a self-driving car's percepts might include camera images, lidar data, GPS coordinates, and speed readings at a specific instant. The agent uses these percepts, and potentially its history of percepts, to decide on its next action (e.g., accelerate, brake, turn).
>
> The agent function, often denoted as *f*, maps the agent's entire history of percepts to an *action*.
>
> Mathematically, this can be represented as f : P* → A, where: P* represents the set of all possible *percept sequences* (the agent's entire perceptual history). The asterisk (*) indicates a sequence of zero or more percepts. A represents the set of all possible *actions* the agent can take. f is the agent function that maps a percept sequence to an action.
>
> It is crucial to distinguish between the *agent function* (an abstract mathematical concept) and the *agent program* (the concrete implementation of that function).
> - The agent function is a theoretical description.
> - The agent program is the actual code that runs on the agent. The agent program takes the *current* percept as input and produces an action as output.
>
> The agent function can incorporate a wide range of decision-making approaches, including: Calculating the utility (desirability) of different actions. Using logical rules and deduction. Employing fuzzy logic. Other methods.

**Classes of intelligent agents — Russell and Norvig's classification (full text)**

> Russell & Norvig (2003) group agents into five classes based on their degree of perceived intelligence and capability:

> **Simple reflex agents**
> Simple reflex agents act only on the basis of the current percept, ignoring the rest of the percept history. The agent function is based on the *condition-action rule*: "if condition, then action".
>
> This agent function only succeeds when the environment is fully observable. Some reflex agents can also contain information on their current state which allows them to disregard conditions whose actuators are already triggered.
>
> Infinite loops are often unavoidable for simple reflex agents operating in partially observable environments. If the agent can randomize its actions, it may be possible to escape from infinite loops.
>
> A home thermostat, which turns on or off when the temperature drops below a certain point, is an example of a simple reflex agent.

> **Model-based reflex agents**
> A model-based agent can handle partially observable environments. Its current state is stored inside the agent, maintaining a structure that describes the part of the world which cannot be seen. This knowledge about "how the world works" is referred to as a model of the world, hence the name "model-based agent".
>
> A model-based reflex agent should maintain some sort of internal model that depends on the percept history and thereby reflects at least some of the unobserved aspects of the current state. Percept history and impact of action on the environment can be determined by using the internal model. It then chooses an action in the same way as reflex agent.
>
> An agent may also use models to describe and predict the behaviors of other agents in the environment.

> **Goal-based agents**
> Goal-based agents further expand on the capabilities of the model-based agents, by using "goal" information. Goal information describes situations that are desirable. This provides the agent a way to choose among multiple possibilities, selecting the one which reaches a goal state. Search and planning are the subfields of artificial intelligence devoted to finding action sequences that achieve the agent's goals.
>
> ChatGPT and the Roomba vacuum are examples of goal-based agents.

> **Utility-based agents**
> Goal-based agents only distinguish between goal states and non-goal states. It is also possible to define a measure of how desirable a particular state is. This measure can be obtained through the use of a *utility function* which maps a state to a measure of the utility of the state. A more general performance measure should allow a comparison of different world states according to how well they satisfied the agent's goals. The term utility can be used to describe how "happy" the agent is.
>
> A rational utility-based agent chooses the action that maximizes the expected utility of the action outcomes - that is, what the agent expects to derive, on average, given the probabilities and utilities of each outcome. A utility-based agent has to model and keep track of its environment, tasks that have involved a great deal of research on perception, representation, reasoning, and learning.

> **Learning agents**
> Learning lets agents begin in unknown environments and gradually surpass the bounds of their initial knowledge. A key distinction in such agents is the separation between a "learning element," responsible for improving performance, and a "performance element," responsible for choosing external actions.
>
> The learning element gathers feedback from a "critic" to assess the agent's performance and decides how the performance element—also called the "actor"—can be adjusted to yield better outcomes. The performance element, once considered the entire agent, interprets percepts and takes actions.
>
> The final component, the "problem generator," suggests new and informative experiences that encourage exploration and further improvement.

**Weiss's classification**

> According to Weiss (2013), agents can be categorized into four classes:
> - Logic-based agents, where decisions about actions are derived through logical deduction.
> - Reactive agents, where decisions occur through a direct mapping from situation to action.
> - Belief–desire–intention agents, where decisions depend on manipulating data structures that represent the agent's beliefs, desires, and intentions.
> - Layered architectures, where decision-making takes place across multiple software layers, each of which reasons about the environment at a different level of abstraction.

**Hierarchies of agents**

> Intelligent agents can be organized hierarchically into multiple "sub-agents." These sub-agents handle lower-level functions, and together with the main agent, they form a complete system capable of executing complex tasks and achieving challenging goals.
>
> Typically, an agent is structured by dividing it into sensors and actuators. The perception system gathers input from the environment via the sensors and feeds this information to a central controller, which then issues commands to the actuators. Often, a multilayered hierarchy of controllers is necessary to balance the rapid responses required for low-level tasks with the more deliberative reasoning needed for high-level objectives.

**Agentic AI**

> In the context of generative AI, AI agents (also called compound AI systems) are a class of intelligent agents distinguished by their ability to operate autonomously in complex environments. Agentic AI tools prioritize decision-making over content creation and do not require human prompts or continuous oversight. They possess several key attributes, including complex goal structures, natural language interfaces, the capacity to act independently of user supervision, and the integration of software tools or planning systems. Their control flow is frequently driven by large language models (LLMs). Agents also include memory systems for remembering previous user-agent interactions and orchestration software for organizing agent components.
>
> Researchers and commentators have noted that AI agents do not have a standard definition. The concept of agentic AI has been compared to the fictional character J.A.R.V.I.S.

**Key references (as listed on the page)**
- Russell, Stuart J.; Norvig, Peter (2003). *Artificial Intelligence: A Modern Approach* (2nd ed.). Prentice Hall. Chapter 2. ISBN 0-13-790395-2. (Taxonomy: pp. 46–54; agent function: p. 33.)
- Russell, Stuart J.; Norvig, Peter (2021). "Intelligent Agents". *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. ISBN 978-0-13-461099-3.
- Weiss, G. (2013). *Multiagent systems* (2nd ed.). MIT Press. ISBN 978-0-262-01889-0.
- Kasabov, N. (1998). "Introduction: Hybrid intelligent adaptive systems". *International Journal of Intelligent Systems* 13(6): 453–454.
- Rao, A. S.; Georgeff, M. P. (1995). "BDI Agents: From Theory to Practice". ICMAS-95, pp. 312–319.
- Padgham, L.; Winikoff, M. (2004). *Developing Intelligent Agent Systems: A Practical Guide*. Wiley.
- Albrecht, S.; Stone, P. (2018). "Autonomous Agents Modelling Other Agents: A Comprehensive Survey and Open Problems". *Artificial Intelligence* 258: 66–95.
- Poole, D.; Mackworth, A. *Artificial Intelligence: Foundations of Computational Agents*, 2nd ed., ch. 2 "Agent Architectures and Hierarchical Control".
- Kapoor, S. et al. (2024). "AI Agents That Matter". arXiv:2407.01502.
- Wissner-Gross, A. D.; Freer, C. E. (2013). "Causal Entropic Forces". *Physical Review Letters* 110(16) 168702.
- Domingos, P. (2015). *The Master Algorithm*. Basic Books.
