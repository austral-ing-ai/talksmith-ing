---
source_file: bdi-agents/
source_type: web-capture
ingested_at: 2026-10-04
---

# Belief–desire–intention software model (Wikipedia)

## Provenance
- Original location: research/web/bdi-agents/ (text from `page.md`)
- Format: html (Wikipedia article, web capture via talksmith:ingest)
- URL: https://en.wikipedia.org/wiki/Belief%E2%80%93desire%E2%80%93intention_software_model (revision oldid=1365371096)
- Fetched: 2026-10-04T19:23:02Z (HTTP 200)
- Author / source (if known): Wikipedia contributors. Key primary references: Rao & Georgeff (1991, 1995); Bratman (1987/1999); Wooldridge (2000); Georgeff et al. (1999).
- Date of original (if known): revision date not shown.

## Key claims
- BDI is "a software model developed for programming intelligent agents." Superficially about beliefs, desires and intentions, "it actually uses these concepts to solve a particular problem in agent programming": it "provides a mechanism for separating the activity of selecting a plan (from a plan library or an external planner application) from the execution of currently active plans."
- BDI agents "balance the time spent on deliberating about plans (choosing what to do) and executing those plans (doing it)." Creating plans (planning) "is not within the scope of the model, and is left to the system designer and programmer."
- Based on Michael Bratman's theory of human practical reasoning. For Bratman, desire and intention are both pro-attitudes; **commitment** distinguishes intention from desire, leading to (1) temporal persistence in plans and (2) further plans built on committed ones.
- Plans are hierarchical: "a plan consists of a number of steps, some of which may invoke other plans."
- Formal logics: Rao & Georgeff's BDICTL (multi-modal logic + temporal logic CTL*); Wooldridge's LORA (Logic Of Rational Agents) adds an action logic and, "in principle", allows reasoning about communication and interaction in a multi-agent system.
- BDI "allows agents to have private beliefs, but does not force them to be private. It also has nothing to say about agent communication."
- "The BDI software model is one example of a reasoning architecture for a single rational agent, and one concern in a broader multi-agent system."
- Limitations: no learning mechanism; debate on whether three attitudes are necessary/sufficient; underlying multi-modal logics "have little relevance in practice"; **does not explicitly describe mechanisms for interaction with other agents and integration into a multi-agent system**; most implementations lack explicit goal representation; no lookahead/forward planning by design.
- Extended with obligations → BOID architecture (obligations, norms, commitments in a social environment).

## Definitions and terminology
- **BDI agent** — "a particular type of bounded rational software agent, imbued with particular mental attitudes, viz: Beliefs, Desires and Intentions (BDI)."
- **Beliefs** — informational state of the agent about the world (including itself and other agents); may include inference rules (forward chaining). "belief" rather than "knowledge" because it may be false or change.
- **Beliefset / belief base** — storage of beliefs (implementation decision, e.g., a database).
- **Desires** — motivational state: objectives the agent *would like* to accomplish (e.g., *find the best price*, *go to the party*, *become rich*).
- **Goals** — desires adopted for active pursuit; the set of active desires must be consistent.
- **Intentions** — deliberative state: what the agent *has chosen* to do; desires to which it has committed; in implementations, the agent has begun executing a plan.
- **Plans** — sequences of actions (recipes or knowledge areas); may include other plans; partially conceived at first, details filled in as they progress.
- **Events** — triggers for reactive activity; may update beliefs, trigger plans or modify goals; external (sensors) or internal.
- **BDI interpreter** — idealized control loop at the basis of SRI's PRS lineage (preserved below).
- **BOID** — BDI + Obligations.
- **PRS** — Procedural Reasoning System (SRI).

## Evidence and examples
- "Pure" BDI implementations listed: PRS, IRMA, UM-PRS, OpenPRS, dMARS, AgentSpeak(L), AgentSpeak(RT), ARTS, JAM, JACK Intelligent Agents, JADEX, JaKtA, JASON, GORITE, SPARK, 3APL, 2APL, GOAL, CogniTAO, Living Systems Process Suite, PROFETA, Gwendolen.
- Extensions/hybrids: JACK Teams, CogniTAO, Living Systems Process Suite, Brahms, JaCaMo.
- Example plan nesting: "my plan to go for a drive may include a plan to find my car keys."
- Recent proposal (Umbrello & Yampolskiy 2021): BDI to design autonomous vehicles for human values.

## Inconsistencies / open questions
- [verified] The article is internally explicit that BDI is a **single-agent** reasoning architecture that "does not explicitly describe mechanisms for interaction with other agents" — checked in both "Overview" and "Limitations and criticisms". If the deck presents BDI as a multi-agent architecture, it should be framed as the per-agent internal architecture inside a MAS (communication comes from elsewhere, e.g., FIPA-ACL / contract net), per this source.
- [open question] "Most BDI implementations do not have an explicit representation of goals" is cited to a 2005 Jadex paper; may be outdated for current implementations — not checked.
- [verified] Minor internal tension: the "Goals" bullet says goals are desires adopted for pursuit (so goals exist conceptually), while Limitations says most implementations lack explicit goals — not a contradiction (concept vs. implementation), checked by reading both passages.

## Images / diagrams

### bdi-agents.web/images/enwiki-25.svg
- Provenance: `research/web/bdi-agents/assets/enwiki-25.svg`. Wikipedia globe icon, site chrome. (The article has no content figures.)
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### bdi-agents.web/images/wikipedia-wordmark-en-25.svg
- Provenance: `research/web/bdi-agents/assets/wikipedia-wordmark-en-25.svg` (alt "Wikipedia"). Site chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### bdi-agents.web/images/wikipedia-tagline-en-25.svg
- Provenance: `research/web/bdi-agents/assets/wikipedia-tagline-en-25.svg` (alt "The Free Encyclopedia"). Site chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

## Raw / preserved excerpts

**Lead**

> The **belief–desire–intention software model** (**BDI**) is a software model developed for programming intelligent agents. Superficially characterized by the implementation of an agent's *beliefs*, *desires* and *intentions*, it actually uses these concepts to solve a particular problem in agent programming. In essence, it provides a mechanism for separating the activity of selecting a plan (from a plan library or an external planner application) from the execution of currently active plans. Consequently, BDI agents are able to balance the time spent on deliberating about plans (choosing what to do) and executing those plans (doing it). A third activity, creating the plans in the first place (planning), is not within the scope of the model, and is left to the system designer and programmer.

**Overview**

> In order to achieve this separation, the BDI software model implements the principal aspects of Michael Bratman's theory of human practical reasoning (also referred to as Belief-Desire-Intention, or BDI). That is to say, it implements the notions of belief, desire and (in particular) intention, in a manner inspired by Bratman.
>
> For Bratman, desire and intention are both pro-attitudes (mental attitudes concerned with action). He identifies commitment as the distinguishing factor between desire and intention, noting that it leads to (1) temporal persistence in plans and (2) further plans being made on the basis of those to which it is already committed. The BDI software model partially addresses these issues. Temporal persistence, in the sense of explicit reference to time, is not explored. The hierarchical nature of plans is more easily implemented: a plan consists of a number of steps, some of which may invoke other plans. The hierarchical definition of plans itself implies a kind of temporal persistence, since the overarching plan remains in effect while subsidiary plans are being executed.
>
> An important aspect of the BDI software model (in terms of its research relevance) is the existence of logical models through which it is possible to define and reason about BDI agents. Research in this area has led, for example, to the axiomatization of some BDI implementations, as well as to formal logical descriptions such as Anand Rao and Michael Georgeff's BDICTL. The latter combines a multiple-modal logic (with modalities representing beliefs, desires and intentions) with the temporal logic CTL*. More recently, Michael Wooldridge has extended BDICTL to define LORA (the Logic Of Rational Agents), by incorporating an action logic. In principle, LORA allows reasoning not only about individual agents, but also about communication and other interaction in a multi-agent system.
>
> The BDI software model is closely associated with intelligent agents, but does not, of itself, ensure all the characteristics associated with such agents. For example, it allows agents to have private beliefs, but does not force them to be private. It also has nothing to say about agent communication. Ultimately, the BDI software model is an attempt to solve a problem that has more to do with plans and planning (the choice and execution thereof) than it has to do with the programming of intelligent agents. This approach has recently been proposed by Steven Umbrello and Roman Yampolskiy as a means of designing autonomous vehicles for human values.

**BDI agents — Architecture**

> A BDI agent is a particular type of bounded rational software agent, imbued with particular *mental attitudes*, viz: Beliefs, Desires and Intentions (BDI).
>
> This section defines the idealized architectural components of a BDI system.
>
> - **Beliefs**: Beliefs represent the informational state of the agent–its beliefs about the world (including itself and other agents). Beliefs can also include inference rules, allowing forward chaining to lead to new beliefs. Using the term *belief* rather than *knowledge* recognizes that what an agent believes may not necessarily be true (and in fact may change in the future).
> - **Beliefset**: Beliefs are stored in database (sometimes called a *belief base* or a *belief set*), although that is an implementation decision.
> - **Desires**: Desires represent the motivational state of the agent. They represent objectives or situations that the agent *would like* to accomplish or bring about. Examples of desires might be: *find the best price*, *go to the party* or *become rich*.
> - **Goals**: A goal is a desire that has been adopted for active pursuit by the agent. Usage of the term *goals* adds the further restriction that the set of active desires must be consistent. For example, one should not have concurrent goals to go to a party and to stay at home – even though they could both be desirable.
> - **Intentions**: Intentions represent the deliberative state of the agent – what the agent *has chosen* to do. Intentions are desires to which the agent has to some extent committed. In implemented systems, this means the agent has begun executing a plan.
> - **Plans**: Plans are sequences of actions (recipes or knowledge areas) that an agent can perform to achieve one or more of its intentions. Plans may include other plans: my plan to go for a drive may include a plan to find my car keys. This reflects that in Bratman's model, plans are initially only partially conceived, with details being filled in as they progress.
> - **Events**: These are triggers for reactive activity by the agent. An event may update beliefs, trigger plans or modify goals. Events may be generated externally and received by sensors or integrated systems. Additionally, events may be generated internally to trigger decoupled updates or plans of activity.
>
> BDI was also extended with an obligations component, giving rise to the BOID agent architecture to incorporate obligations, norms and commitments of agents that act within a social environment.

**BDI interpreter** — "an idealized BDI interpreter that provides the basis of SRI's PRS lineage of BDI systems" (nesting restored from the original list structure):

```
1. initialize-state
2. repeat
   1. options: option-generator (event-queue)
   2. selected-options: deliberate(options)
   3. update-intentions(selected-options)
   4. execute()
   5. get-new-external-events()
   6. drop-unsuccessful-attitudes()
   7. drop-impossible-attitudes()
3. end repeat
```

**Limitations and criticisms**

> The BDI software model is one example of a reasoning architecture for a single rational agent, and one concern in a broader multi-agent system. This section bounds the scope of concerns for the BDI software model, highlighting known limitations of the architecture.
>
> - **Learning**: BDI agents lack any specific mechanisms within the architecture to learn from past behavior and adapt to new situations.
> - **Three attitudes**: Classical decision theorists and planning research questions the necessity of having all three attitudes, distributed AI research questions whether the three attitudes are sufficient.
> - **Logics**: The multi-modal logics that underlie BDI (that do not have complete axiomatizations and are not efficiently computable) have little relevance in practice.
> - **Multiple agents**: In addition to not explicitly supporting learning, the framework may not be appropriate to learning behavior. Further, the BDI model does not explicitly describe mechanisms for interaction with other agents and integration into a multi-agent system.
> - **Explicit goals**: Most BDI implementations do not have an explicit representation of goals.
> - **Lookahead**: The architecture does not have (by design) any lookahead deliberation or forward planning. This may not be desirable because adopted plans may use up limited resources, actions may not be reversible, task execution may take longer than forward planning, and actions may have undesirable side effects if unsuccessful.

**Selected references** (from the article)

- Rao, A. S. & Georgeff, M. P. (1995). "BDI-agents: From Theory to Practice". Proceedings of the First International Conference on Multiagent Systems (ICMAS'95), San Francisco.
- Rao, A. S. & Georgeff, M. P. (1991). "Modeling Rational Agents within a BDI-Architecture". Proc. 2nd Int. Conf. on Principles of Knowledge Representation and Reasoning, pp. 473–484.
- Bratman, M. E. (1999) [1987]. *Intention, Plans, and Practical Reason*. CSLI Publications. ISBN 1-57586-192-5.
- Wooldridge, M. (2000). *Reasoning About Rational Agents*. MIT Press. ISBN 0-262-23213-8.
- Georgeff, M.; Pell, B.; Pollack, M. E.; Tambe, M.; Wooldridge, M. (1999). "The Belief-Desire-Intention Model of Agency". *Intelligent Agents V*, LNCS 1555, pp. 1–10. doi:10.1007/3-540-49057-4_1.
- Broersen, J.; Dastani, M.; Hulstijn, J.; Huang, Z.; van der Torre, L. (2001). "The BOID architecture: conflicts between beliefs, obligations, intentions and desires". Proc. 5th Int. Conf. on Autonomous Agents, pp. 9–16.
- Pokahr, A.; Braubach, L.; Lamersdorf, W. (2005). "Jadex: A BDI Reasoning Engine". *Multi-Agent Programming*, pp. 149–174.
- Sardina, S.; de Silva, L.; Padgham, L. (2006). "Hierarchical planning in BDI agent programming languages: a formal approach". AAMAS 2006.
- Umbrello, S.; Yampolskiy, R. V. (2021). "Designing AI for Explainability and Verifiability: A Value Sensitive Design Approach to Avoid Artificial Stupidity in Autonomous Vehicles". *International Journal of Social Robotics* 14(2): 313–322.
