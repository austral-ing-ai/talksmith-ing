# Belief–desire–intention software model - Wikipedia

_Source: <https://en.wikipedia.org/wiki/Belief%E2%80%93desire%E2%80%93intention_software_model>_

[Jump to content](#bodyContent) ![](/static/images/icons/enwiki-25.svg) ![Wikipedia](/static/images/mobile/copyright/wikipedia-wordmark-en-25.svg) ![The Free Encyclopedia](/static/images/mobile/copyright/wikipedia-tagline-en-25.svg) </wiki/Main_Page> [Search](/wiki/Special:Search) 

# Belief–desire–intention software model

8 languages 

- [العربية](https://ar.wikipedia.org/wiki/%D9%86%D9%85%D9%88%D8%B0%D8%AC_%D8%A8%D8%B1%D9%85%D8%AC%D9%8A_%D9%84%D9%84%D8%A7%D8%B9%D8%AA%D9%82%D8%A7%D8%AF_%D9%88%D8%A7%D9%84%D8%B1%D8%BA%D8%A8%D8%A9_%D9%88%D8%A7%D9%84%D9%82%D8%B5%D8%AF)
- [Català](https://ca.wikipedia.org/wiki/Model_de_programari_de_creen%C3%A7a-desig-intenci%C3%B3)
- [Čeština](https://cs.wikipedia.org/wiki/Softwarov%C3%BD_model_Belief-Desire-Intention)
- [Deutsch](https://de.wikipedia.org/wiki/BDI-Agent)
- [Français](https://fr.wikipedia.org/wiki/Mod%C3%A8le_logiciel_de_croyance%E2%80%93d%C3%A9sir%E2%80%93intention)
- [Italiano](https://it.wikipedia.org/wiki/Modello_BDI)
- [Русский](https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C_%D1%83%D0%B1%D0%B5%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B9,_%D0%B6%D0%B5%D0%BB%D0%B0%D0%BD%D0%B8%D0%B9_%D0%B8_%D0%BD%D0%B0%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D0%B9)
- [Українська](https://uk.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BD%D0%B0_%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C_%D0%BF%D0%B5%D1%80%D0%B5%D0%BA%D0%BE%D0%BD%D0%B0%D0%BD%D1%8C,_%D0%B1%D0%B0%D0%B6%D0%B0%D0%BD%D1%8C_%D1%82%D0%B0_%D0%BD%D0%B0%D0%BC%D1%96%D1%80%D1%96%D0%B2) 
[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q372345#sitelinks-wikipedia) From Wikipedia, the free encyclopedia Model for designing artificial intelligence 

The **belief–desire–intention software model** (**BDI**) is a [software model](https://en.wikipedia.org/wiki/Modeling_language) developed for programming [intelligent agents](https://en.wikipedia.org/wiki/Intelligent_agent). Superficially characterized by the implementation of an agent's *beliefs*, *desires* and *intentions*, it actually uses these concepts to solve a particular problem in agent programming. In essence, it provides a mechanism for separating the activity of selecting a plan (from a plan [library](https://en.wikipedia.org/wiki/Library_(computing)) or an external planner application) from the execution of currently active plans. Consequently, BDI agents are able to balance the time spent on deliberating about plans (choosing what to do) and executing those plans (doing it). A third activity, creating the plans in the first place ([planning](https://en.wikipedia.org/wiki/Automated_planning_and_scheduling)), is not within the scope of the model, and is left to the system designer and programmer.

## Overview

[[edit](/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=1)] 

In order to achieve this separation, the BDI software model implements the principal aspects of [Michael Bratman](https://en.wikipedia.org/wiki/Michael_Bratman)'s [theory of human practical reasoning](https://en.wikipedia.org/wiki/Belief-Desire-Intention_model) (also referred to as Belief-Desire-Intention, or BDI). That is to say, it implements the notions of belief, desire and (in particular) intention, in a manner inspired by Bratman. 

For Bratman, desire and intention are both pro-attitudes (mental attitudes concerned with action). He identifies commitment as the distinguishing factor between desire and intention, noting that it leads to (1) temporal persistence in plans and (2) further plans being made on the basis of those to which it is already committed. The BDI software model partially addresses these issues. Temporal persistence, in the sense of explicit reference to time, is not explored. The hierarchical nature of plans is more easily implemented: a plan consists of a number of steps, some of which may invoke other plans. The hierarchical definition of plans itself implies a kind of temporal persistence, since the overarching plan remains in effect while subsidiary plans are being executed.

An important aspect of the BDI software model (in terms of its research relevance) is the existence of logical models through which it is possible to define and reason about BDI agents. Research in this area has led, for example, to the [axiomatization](https://en.wikipedia.org/wiki/Axiomatic_system) of some BDI implementations, as well as to [formal logical](https://en.wikipedia.org/wiki/Logic) descriptions such as Anand Rao and [Michael Georgeff](https://en.wikipedia.org/wiki/Michael_Georgeff)'s BDICTL. The latter combines a [multiple-modal logic](https://en.wikipedia.org/wiki/Modal_logic) (with modalities representing beliefs, desires and intentions) with the [temporal logic](https://en.wikipedia.org/wiki/Temporal_logic) [CTL*](https://en.wikipedia.org/wiki/Computational_tree_logic). More recently, Michael Wooldridge has extended BDICTL to define LORA (the Logic Of Rational Agents), by incorporating an action logic. In principle, LORA allows reasoning not only about individual agents, but also about communication and other interaction in a [multi-agent system](https://en.wikipedia.org/wiki/Multi-agent_system).

The BDI software model is closely associated with intelligent agents, but does not, of itself, ensure all the characteristics associated with such agents. For example, it allows agents to have private beliefs, but does not force them to be private. It also has nothing to say about agent communication. Ultimately, the BDI software model is an attempt to solve a problem that has more to do with plans and planning (the choice and execution thereof) than it has to do with the programming of intelligent agents. This approach has recently been proposed by [Steven Umbrello](https://en.wikipedia.org/wiki/Steven_Umbrello?action=edit&redlink=1) and [Roman Yampolskiy](https://en.wikipedia.org/wiki/Roman_Yampolskiy) as a means of designing [autonomous vehicles](https://en.wikipedia.org/wiki/Self-driving_car) for human values.[[1]](#cite_note-1)

## BDI agents

[[edit](/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=2)] 

A BDI agent is a particular type of [bounded](https://en.wikipedia.org/wiki/Bounded_rationality) [rational software agent](https://en.wikipedia.org/wiki/Intelligent_agent), imbued with particular *mental attitudes*, viz: Beliefs, Desires and Intentions (BDI).

### Architecture

[[edit](/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=3)] 

This section defines the idealized architectural components of a BDI system.

- **Beliefs**: Beliefs represent the informational state of the agent–its beliefs about the world (including itself and other agents). Beliefs can also include [inference rules](https://en.wikipedia.org/wiki/Inference_rule), allowing [forward chaining](https://en.wikipedia.org/wiki/Forward_chaining) to lead to new beliefs. Using the term *belief* rather than *knowledge* recognizes that what an agent believes may not necessarily be true (and in fact may change in the future). 

- **Beliefset**: Beliefs are stored in [database](https://en.wikipedia.org/wiki/Database) (sometimes called a *belief base* or a *belief set*), although that is an [implementation](https://en.wikipedia.org/wiki/Implementation) decision.

- **Desires**: Desires represent the motivational state of the agent. They represent objectives or situations that the agent *would like* to accomplish or bring about. Examples of desires might be: *find the best price*, *go to the party* or *become rich*. 

- **Goals**: A goal is a desire that has been adopted for active pursuit by the agent. Usage of the term *goals* adds the further restriction that the set of active desires must be consistent. For example, one should not have concurrent goals to go to a party and to stay at home – even though they could both be desirable.

- **Intentions**: Intentions represent the deliberative state of the agent – what the agent *has chosen* to do. Intentions are desires to which the agent has to some extent committed. In implemented systems, this means the agent has begun executing a plan. 

- **Plans**: Plans are sequences of actions (recipes or knowledge areas) that an agent can perform to achieve one or more of its intentions. Plans may include other plans: my plan to go for a drive may include a plan to find my car keys. This reflects that in Bratman's model, plans are initially only partially conceived, with details being filled in as they progress.

- **Events**: These are triggers for reactive activity by the agent. An event may update beliefs, trigger plans or modify goals. Events may be generated externally and received by sensors or integrated systems. Additionally, events may be generated internally to trigger decoupled updates or plans of activity.

BDI was also extended with an obligations component, giving rise to the BOID [agent architecture](https://en.wikipedia.org/wiki/Agent_architecture)[[2]](#cite_note-2) to incorporate obligations, norms and commitments of agents that act within a [social environment](https://en.wikipedia.org/wiki/Social_environment).

### BDI interpreter

[[edit](/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=4)] 

This section defines an idealized BDI interpreter that provides the basis of SRI's [PRS](https://en.wikipedia.org/wiki/Procedural_reasoning_system) lineage of BDI systems:[[3]](#cite_note-Rao_1995-3)

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

### Limitations and criticisms

[[edit](/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=5)] 

The BDI software model is one example of a reasoning architecture for a single rational agent, and one concern in a broader [multi-agent system](https://en.wikipedia.org/wiki/Multi-agent_system). This section bounds the scope of concerns for the BDI software model, highlighting known limitations of the architecture.

- **Learning**: BDI agents lack any specific mechanisms within the architecture to learn from past behavior and adapt to new situations.[[4]](#cite_note-4)[[5]](#cite_note-5) 
- **Three attitudes**: Classical [decision theorists](https://en.wikipedia.org/wiki/Decision_theory) and planning research questions the necessity of having all three attitudes, [distributed AI](https://en.wikipedia.org/wiki/Distributed_artificial_intelligence) research questions whether the three attitudes are sufficient.[[3]](#cite_note-Rao_1995-3) 
- **Logics**: The multi-modal logics that underlie BDI (that do not have complete axiomatizations and are not efficiently computable) have little relevance in practice.[[3]](#cite_note-Rao_1995-3)[[6]](#cite_note-6) 
- **Multiple agents**: In addition to not explicitly supporting learning, the framework may not be appropriate to learning behavior. Further, the BDI model does not explicitly describe mechanisms for interaction with other agents and integration into a [multi-agent system](https://en.wikipedia.org/wiki/Multi-agent_system).[[7]](#cite_note-7) 
- **Explicit goals**: Most BDI implementations do not have an explicit representation of goals.[[8]](#cite_note-8) 
- **Lookahead**: The architecture does not have (by design) any lookahead deliberation or forward planning. This may not be desirable because adopted plans may use up limited resources, actions may not be reversible, task execution may take longer than forward planning, and actions may have undesirable side effects if unsuccessful.[[9]](#cite_note-9)

## BDI agent implementations

[[edit](/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=6)] 

### 'Pure' BDI

[[edit](/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=7)] 

- [Procedural Reasoning System](https://en.wikipedia.org/wiki/Procedural_Reasoning_System) (PRS) 
- IRMA (not implemented but can be considered as PRS with non-reconsideration) 
- UM-PRS[[10]](#cite_note-10) 
- OpenPRS[[11]](#cite_note-11) 
- [Distributed Multi-Agent Reasoning System](https://en.wikipedia.org/wiki/Distributed_Multi-Agent_Reasoning_System) (dMARS) 
- [AgentSpeak(L)](https://en.wikipedia.org/wiki/AgentSpeak) – see Jason below 
- AgentSpeak(RT)[[12]](#cite_note-12)[[13]](#cite_note-agent-lab-notts1-13) 
- Agent Real-Time System (ARTS)[[14]](#cite_note-14) (ARTS)[[15]](#cite_note-agent-lab-notts2-15) 
- JAM[[16]](#cite_note-16) 
- [JACK Intelligent Agents](https://en.wikipedia.org/wiki/JACK_Intelligent_Agents) 
- JADEX (open source project)[[17]](#cite_note-17) 
- JaKtA[[18]](#cite_note-18) 
- JASON[[19]](#cite_note-19) 
- [GORITE](https://en.wikipedia.org/wiki/GORITE) 
- SPARK[[20]](#cite_note-20) 
- [3APL](https://en.wikipedia.org/wiki/3APL) 
- [2APL](https://en.wikipedia.org/wiki/2APL)[[21]](#cite_note-21) 
- [GOAL agent programming language](https://en.wikipedia.org/wiki/GOAL_agent_programming_language) 
- CogniTAO (Think-As-One)[[22]](#cite_note-CogniTAO_Think-As-One-22)[[23]](#cite_note-icr2008.org.il-23) 
- Living Systems Process Suite[[24]](#cite_note-Living_Systems_Process_Suite-24)[[25]](#cite_note-whitestein.com-25) 
- PROFETA[[26]](#cite_note-26) 
- Gwendolen[[27]](#cite_note-27) (Part of the [Model Checking](https://en.wikipedia.org/wiki/Model_checking) Agent Programming Languages Framework[[28]](#cite_note-28)[[29]](#cite_note-29))

### Extensions and hybrid systems

[[edit](/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=8)] 

- [JACK Teams](https://en.wikipedia.org/wiki/JACK_Intelligent_Agents) 
- CogniTAO (Think-As-One)[[22]](#cite_note-CogniTAO_Think-As-One-22)[[23]](#cite_note-icr2008.org.il-23) 
- Living Systems Process Suite[[24]](#cite_note-Living_Systems_Process_Suite-24)[[25]](#cite_note-whitestein.com-25) 
- Brahms[[30]](#cite_note-30) 
- JaCaMo[[31]](#cite_note-31)

## See also

[[edit](/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=9)] 

- [Action selection](https://en.wikipedia.org/wiki/Action_selection) 
- [Artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence) 
- [Belief–desire–intention model](https://en.wikipedia.org/wiki/Belief–desire–intention_model) 
- [Belief revision](https://en.wikipedia.org/wiki/Belief_revision) 
- [GOLOG](https://en.wikipedia.org/wiki/GOLOG) 
- [Intelligent agent](https://en.wikipedia.org/wiki/Intelligent_agent) 
- [Reasoning](https://en.wikipedia.org/wiki/Reasoning) 
- [Software agent](https://en.wikipedia.org/wiki/Software_agent)

## References

[[edit](/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=10)] 

1. [↑](#cite_ref-1) Umbrello, Steven; Yampolskiy, Roman V. (2021-05-15). ["Designing AI for Explainability and Verifiability: A Value Sensitive Design Approach to Avoid Artificial Stupidity in Autonomous Vehicles"](https://doi.org/10.1007%2Fs12369-021-00790-w). *International Journal of Social Robotics*. **14** (2): 313–322. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/s12369-021-00790-w](https://doi.org/10.1007%2Fs12369-021-00790-w). [hdl](https://en.wikipedia.org/wiki/Hdl_(identifier)):[2318/1788856](https://hdl.handle.net/2318%2F1788856). [ISSN](https://en.wikipedia.org/wiki/ISSN_(identifier)) [1875-4805](https://search.worldcat.org/issn/1875-4805). 
2. [↑](#cite_ref-2)  J. Broersen, M. Dastani, J. Hulstijn, Z. Huang, L. van der Torre [The BOID architecture: conflicts between beliefs, obligations, intentions and desires](http://dl.acm.org/citation.cfm?id=375766) Proceedings of the fifth international conference on Autonomous agents, 2001, pages 9-16, ACM New York, NY, USA 
3. [1](#cite_ref-Rao_1995_3-0) [2](#cite_ref-Rao_1995_3-1) [3](#cite_ref-Rao_1995_3-2) Rao, M. P. Georgeff. (1995). ["BDI-agents: From Theory to Practice"](https://web.archive.org/web/20110604050051/https://www.aaai.org/Papers/ICMAS/1995/ICMAS95-042.pdf) (PDF). *Proceedings of the First International Conference on Multiagent Systems (ICMAS'95)*. Archived from [the original](https://www.aaai.org/Papers/ICMAS/1995/ICMAS95-042.pdf) (PDF) on 2011-06-04. Retrieved 2009-07-09. 
4. [↑](#cite_ref-4) Phung, Toan; Michael Winikoff; Lin Padgham (2005). "Learning Within the BDI Framework: An Empirical Analysis". *Knowledge-Based Intelligent Information and Engineering Systems*. Lecture Notes in Computer Science. Vol. 3683. pp. 282–288. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/11553939_41](https://doi.org/10.1007%2F11553939_41). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [978-3-540-28896-1](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-28896-1). 
5. [↑](#cite_ref-5) Guerra-Hernández, Alejandro; [Amal El Fallah Seghrouchni](https://en.wikipedia.org/wiki/Amal_El_Fallah_Seghrouchni); Henry Soldano (2004). "Learning in BDI Multi-agent Systems". *Computational Logic in Multi-Agent Systems*. Lecture Notes in Computer Science. Vol. 3259. pp. 218–233. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/978-3-540-30200-1_12](https://doi.org/10.1007%2F978-3-540-30200-1_12). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [978-3-540-24010-5](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-24010-5). 
6. [↑](#cite_ref-6) Rao, M. P. Georgeff. (1995). "Formal models and decision procedures for multi-agent systems". *Technical Note, AAII*. [CiteSeerX](https://en.wikipedia.org/wiki/CiteSeerX_(identifier)) [10.1.1.52.7924](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.52.7924). `{{[cite conference](https://en.wikipedia.org/wiki/Template:Cite_conference)}}`: Cite uses deprecated parameter `|citeseerx=` ([help](https://en.wikipedia.org/wiki/Help:CS1_errors#deprecated_params)) 
7. [↑](#cite_ref-7) Georgeff, Michael; Barney Pell; [Martha E. Pollack](https://en.wikipedia.org/wiki/Martha_E._Pollack); Milind Tambe; Michael Wooldridge (1999). "The Belief-Desire-Intention Model of Agency". *Intelligent Agents V: Agents Theories, Architectures, and Languages*. Lecture Notes in Computer Science. Vol. 1555. pp. 1–10. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/3-540-49057-4_1](https://doi.org/10.1007%2F3-540-49057-4_1). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [978-3-540-65713-2](https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-65713-2). 
8. [↑](#cite_ref-8) Pokahr, Alexander; Lars Braubach; Winfried Lamersdorf (2005). "Jadex: A BDI Reasoning Engine". *Multi-Agent Programming*. Multiagent Systems, Artificial Societies, and Simulated Organizations. Vol. 15. pp. 149–174. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/0-387-26350-0_6](https://doi.org/10.1007%2F0-387-26350-0_6). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [978-0-387-24568-3](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-24568-3). 
9. [↑](#cite_ref-9) Sardina, Sebastian; Lavindra de Silva; Lin Padgham (2006). ["Hierarchical planning in BDI agent programming languages: a formal approach"](http://portal.acm.org/citation.cfm?id=1160813). *Proceedings of the fifth international joint conference on Autonomous agents and multiagent systems*. 
10. [↑](#cite_ref-10) [UM-PRS](http://www.marcush.net/IRS/irs_downloads.html) 
11. [↑](#cite_ref-11) ["OpenPRS"](https://web.archive.org/web/20141021195123/http://homepages.laas.fr/felix/PRS). Archived from [the original](http://homepages.laas.fr/felix/PRS) on 2014-10-21. Retrieved 2014-10-23. 
12. [↑](#cite_ref-12) [AgentSpeak(RT)](http://www.iesd.dmu.ac.uk/~kvikho/publications.html) [Archived](https://web.archive.org/web/20120326071744/http://www.iesd.dmu.ac.uk/~kvikho/publications.html) 2012-03-26 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine) 
13. [↑](#cite_ref-agent-lab-notts1_13-0) Vikhorev, K., Alechina, N. and Logan, B. (2011). ["Agent programming with priorities and deadlines"](http://www.iesd.dmu.ac.uk/~kvikho/papers/Vikhorev11Agent.pdf) [Archived](https://web.archive.org/web/20120326071730/http://www.iesd.dmu.ac.uk/~kvikho/papers/Vikhorev11Agent.pdf) March 26, 2012, at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine). In Proceedings of the Tenth International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2011). Taipei, Taiwan. May 2011., pp. 397-404. 
14. [↑](#cite_ref-14) [Agent Real-Time System](http://www.cs.nott.ac.uk/~kxv/arts.html) [Archived](https://web.archive.org/web/20110927112727/http://www.cs.nott.ac.uk/~kxv/arts.html) 2011-09-27 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine) 
15. [↑](#cite_ref-agent-lab-notts2_15-0) Vikhorev, K., Alechina, N. and Logan, B. (2009). ["The ARTS Real-Time Agent Architecture"](http://www.iesd.dmu.ac.uk/~kvikho/papers/Vikhorev09ARTS.pdf) [Archived](https://web.archive.org/web/20120326071752/http://www.iesd.dmu.ac.uk/~kvikho/papers/Vikhorev09ARTS.pdf) March 26, 2012, at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine). In Proceedings of Second Workshop on Languages, Methodologies and Development Tools for Multi-agent Systems (LADS2009). Turin, Italy. September 2009. CEUR Workshop Proceedings Vol-494. 
16. [↑](#cite_ref-16) [JAM](http://www.marcush.net/IRS/irs_downloads.html) 
17. [↑](#cite_ref-17) [JADEX](http://vsis-www.informatik.uni-hamburg.de/projects/jadex/) 
18. [↑](#cite_ref-18) Baiardi, Martina; Burattini, Samuele; Ciatto, Giovanni; Pianini, Danilo (2024). **[Blending BDI Agents with Object-Oriented and Functional Programming with JaKtA](https://link.springer.com/article/10.1007/s42979-024-03244-y). *SN Computer Science*. Vol. 5, art. 1003. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/s42979-024-03244-y](https://doi.org/10.1007%2Fs42979-024-03244-y). [hdl](https://en.wikipedia.org/wiki/Hdl_(identifier)):[11585/998116](https://hdl.handle.net/11585%2F998116). 
19. [↑](#cite_ref-19) ["Jason | a Java-based interpreter for an extended version of AgentSpeak"](https://jason.sourceforge.net/wp/). 
20. [↑](#cite_ref-20) [SPARK](http://www.ai.sri.com/~spark/) 
21. [↑](#cite_ref-21) [2APL](https://apapl.sourceforge.net/) 
22. [1](#cite_ref-CogniTAO_Think-As-One_22-0) [2](#cite_ref-CogniTAO_Think-As-One_22-1) [CogniTAO (Think-As-One)](http://www.cogniteam.com/) 
23. [1](#cite_ref-icr2008.org.il_23-0) [2](#cite_ref-icr2008.org.il_23-1) TAO: A JAUS-based High-Level Control System for Single and Multiple Robots Y. Elmaliach, CogniTeam, (2008) ["Archived copy"](https://web.archive.org/web/20090107071940/http://www.icr2008.org.il/program.html). Archived from [the original](http://www.icr2008.org.il/program.html) on 2009-01-07. Retrieved 2008-11-03.`{{[cite web](https://en.wikipedia.org/wiki/Template:Cite_web)}}`: CS1 maint: archived copy as title ([link](https://en.wikipedia.org/wiki/Category:CS1_maint:_archived_copy_as_title)) 
24. [1](#cite_ref-Living_Systems_Process_Suite_24-0) [2](#cite_ref-Living_Systems_Process_Suite_24-1) [Living Systems Process Suite](http://www.whitestein.com/goal-oriented-bpm-suite) 
25. [1](#cite_ref-whitestein.com_25-0) [2](#cite_ref-whitestein.com_25-1) Rimassa, G., Greenwood, D. and Kernland, M. E., (2006). [The Living Systems Technology Suite: An Autonomous Middleware for Autonomic Computing](http://www.whitestein.com/library/WhitesteinTechnologies_Paper_ICAS2006-gri.pdf) [Archived](https://web.archive.org/web/20080516050754/http://www.whitestein.com/library/WhitesteinTechnologies_Paper_ICAS2006-gri.pdf) May 16, 2008, at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine). International Conference on Autonomic and Autonomous Systems (ICAS). 
26. [↑](#cite_ref-26) Fichera, Loris; Marletta, Daniele; Nicosia, Vincenzo; Santoro, Corrado (2011). "Flexible Robot Strategy Design Using Belief-Desire-Intention Model". In Obdržálek, David; Gottscheber, Achim (eds.). *Research and Education in Robotics - EUROBOT 2010*. Communications in Computer and Information Science. Vol. 156. Berlin, Heidelberg: Springer. pp. 57–71. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/978-3-642-27272-1_5](https://doi.org/10.1007%2F978-3-642-27272-1_5). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [978-3-642-27272-1](https://en.wikipedia.org/wiki/Special:BookSources/978-3-642-27272-1). 
27. [↑](#cite_ref-27) [Gwendolen Semantics:2017](https://intranet.csc.liv.ac.uk/research/techreports/tr2017/ulcs-17-001.pdf) 
28. [↑](#cite_ref-28) [Model Checking Agent Programming Languages](https://autonomy-and-verification.github.io/tools/mcapl) 
29. [↑](#cite_ref-29) [MCAPL (Zenodo)](https://zenodo.org/record/3235469#.X8Z55y2l0tE) 
30. [↑](#cite_ref-30) [Brahms](https://www.ejenta.com/documentation) 
31. [↑](#cite_ref-31) ["Home"](https://jacamo.sourceforge.net/). *jacamo.sourceforge.net*. 

## Further reading

[[edit](/w/index.php?title=Belief%E2%80%93desire%E2%80%93intention_software_model&action=edit&section=11)] 

- A. S. Rao and M. P. Georgeff. [Modeling Rational Agents within a BDI-Architecture](http://jmvidal.cse.sc.edu/lib/rao91a.html). In Proceedings of the 2nd International Conference on Principles of Knowledge Representation and Reasoning, pages 473–484, 1991. 
- A. S. Rao and M. P. Georgeff. [BDI-agents: From Theory to Practice](https://www.aaai.org/Papers/ICMAS/1995/ICMAS95-042.pdf) [Archived](https://web.archive.org/web/20110604050051/https://www.aaai.org/Papers/ICMAS/1995/ICMAS95-042.pdf) 2011-06-04 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine), In Proceedings of the First International Conference on Multiagent Systems (ICMAS'95), San Francisco, 1995. 
- Bratman, M. E. (1999) [1987]. **[Intention, Plans, and Practical Reason](http://csli-publications.stanford.edu/site/1575861925.shtml). [CSLI Publications](https://en.wikipedia.org/wiki/Center_for_the_Study_of_Language_and_Information). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [1-57586-192-5](https://en.wikipedia.org/wiki/Special:BookSources/1-57586-192-5). 
- Wooldridge, M. (2000). **[Reasoning About Rational Agents](https://web.archive.org/web/20100730032058/http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=3533). [The MIT Press](https://en.wikipedia.org/wiki/MIT_Press). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [0-262-23213-8](https://en.wikipedia.org/wiki/Special:BookSources/0-262-23213-8). Archived from [the original](http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=3533) on 2010-07-30. Retrieved 2006-06-15. 
- K. S. Vikhorev, N. Alechina, and B. Logan. [The ARTS Real-Time Agent Architecture](http://www.cs.nott.ac.uk/~nza/papers/Vikhorev++:09a.pdf). In Proceedings of Second Workshop on Languages, Methodologies and Development Tools for Multi-agent Systems (LADS2009). CEUR Workshop Proceedings, Vol-494, Turin, Italy, 2009.
Retrieved from "[https://en.wikipedia.org/w/index.php?title=Belief–desire–intention_software_model&oldid=1365371096](https://en.wikipedia.org/w/index.php?title=Belief–desire–intention_software_model&oldid=1365371096)" [Categories](/wiki/Help:Category): 

- [Artificial intelligence engineering](/wiki/Category:Artificial_intelligence_engineering)
- [Belief revision](/wiki/Category:Belief_revision)
- [Agent-based programming languages](/wiki/Category:Agent-based_programming_languages)
Hidden categories: 

- [Articles with short description](/wiki/Category:Articles_with_short_description)
- [Short description is different from Wikidata](/wiki/Category:Short_description_is_different_from_Wikidata)
- [CS1 errors: deprecated parameters](/wiki/Category:CS1_errors:_deprecated_parameters)
- [Webarchive template wayback links](/wiki/Category:Webarchive_template_wayback_links)
- [CS1 maint: archived copy as title](/wiki/Category:CS1_maint:_archived_copy_as_title)
Search Belief–desire–intention software model <#> <#> <#> <#> <#> <#> <#> 8 languages [Add topic](#)
