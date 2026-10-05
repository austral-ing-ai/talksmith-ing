---
source_file: contract-net-protocol/
source_type: web-capture
ingested_at: 2026-10-04
---

# Contract Net Protocol (Wikipedia)

## Provenance
- Original location: research/web/contract-net-protocol/ (text from `page.md`)
- Format: html (Wikipedia article, web capture via talksmith:ingest)
- URL: https://en.wikipedia.org/wiki/Contract_Net_Protocol (revision oldid=1342154242)
- Fetched: 2026-10-04T19:23:00Z (HTTP 200)
- Author / source (if known): Wikipedia contributors. Primary reference: Reid G. Smith, "The Contract Net Protocol: High-Level Communication and Control in a Distributed Problem Solver", *IEEE Transactions on Computers* C-29(12):1104–1113, December 1980.
- Date of original (if known): protocol introduced 1980; article revision date not shown.

## Key claims
- CNP is "a task-sharing protocol in multi-agent systems, introduced in 1980 by Reid G. Smith. It is used to allocate tasks among autonomous agents."
- "It is close to sealed auctions protocols."
- "a manager proposes a task to several agents. The latter make a proposal among which the manager chooses to allocate the task. This task can then be divided and subcontracted."
- Can implement **hierarchical organizations**: "a manager assigns tasks to contractors, who in turn decompose into lower-level task and assign them to the lower level."
- With **cooperative** agents (identical objectives) one can ensure contractors do not lie; with **competitive** agents "the protocol ends up in a marketplace organization, very similar to auctions."
- Implemented by FIPA in the ACL (Agent Communication Language).
- Used for sensor networks (original article's use case), multi-robot task allocation, e-commerce negotiation and supply chains.
- Issues identified by Smith: message overload → short messages, contact only relevant agents, direct offers when the manager already knows the contractor; busy contractors → may bid while working, stating when they will be ready; maintain a list of available contractors.
- Extension: FIPA **Iterated** Contract Net (manager can re-issue calls for proposals to a subset, like iterated auctions).
- Extension: Sandholm & Lesser (1995) add a **commitment cost** (penalty for decommitting), because in the original a contractor can `cancel` without sanction — selfish agents may over-bid and fulfil only the profitable tasks.

## Definitions and terminology
- **Manager** — agent that initiates the protocol and allocates the task.
- **Contractor** — agent that bids on and executes the task.
- Message types (speech acts): **call-for-proposals**, **proposal**, **reject**, **accept**, **inform**, **cancel**.
- **Speech act theory** — formal basis for the protocol's messages.
- **AUML** — Agent UML, notation used for the protocol diagrams.
- **FIPA / FIPA-ACL** — Foundation for Intelligent Physical Agents; its Agent Communication Language.

## Evidence and examples
- Four-step formal description (preserved verbatim below).
- References: Smith 1980; Horling & Lesser 2005 (survey of MAS organizational paradigms); FIPA CNP spec SC00029H; FIPA Iterated CNP spec SC00030H; Chen et al. 2012 (WSN); Grabovskis et al. 2012 (multi-robot); Sandholm 1993 (marginal cost, AAAI-93); Jiao et al. 2006 (supply chain); Sandholm & Lesser 1995 (ICMAS-95).

## Inconsistencies / open questions
- [open question] "introduced in 1980 by Reid G. Smith" — Wikipedia cites the 1980 IEEE TC paper; Smith's earlier 1977–1978 work on contract nets is sometimes cited as the origin. Not checked; settle against Smith 1980's own references if the deck states a precise year of origin.
- Note for the talk: CNP is a classic, pre-LLM ancestor of the orchestrator-worker / manager-subcontractor pattern (call-for-proposals ≈ the orchestrator asking workers; recursion = hierarchical). That mapping is an interpretation, not a claim of the source, except for the "hierarchical organizations" sentence, which is in the source.

## Images / diagrams

### contract-net-protocol.web/images/500px-CNP.svg.png
- Provenance: `research/web/contract-net-protocol/assets/500px-CNP.svg.png` (Wikimedia Commons File:CNP.svg, 500px PNG thumbnail). Alt/caption: "Contract Net Protocol AUML Diagram". Placed in "Formal description".
- Depiction: AUML sequence diagram with two lifelines, 'manager' (left) and 'contractor' (right). Manager sends 'callforproposal'. A decision diamond on the contractor side branches to either 'reject' or 'propose' back to the manager. After evaluating, a manager-side diamond sends either 'reject' or 'accept' to the contractor. After an accepted task, a contractor-side diamond sends either 'inform' or 'cancel' to the manager. Activation bars on both lifelines.
- Why it matters: The canonical one-round Contract Net message flow (announce -> bid/decline -> award/reject -> result) — the reference diagram for task allocation by negotiation in a MAS.
- Transcribed text: manager; contractor; callforproposal; reject; propose; reject; accept; inform; cancel.

### contract-net-protocol.web/images/500px-Icnp.svg.png
- Provenance: `research/web/contract-net-protocol/assets/500px-Icnp.svg.png` (Wikimedia Commons File:Icnp.svg, 500px PNG thumbnail). Alt: "Iterated Contract Net Protocol AUML diagram". Placed in "Issues and extensions".
- Depiction: Same AUML layout as the basic Contract Net diagram, but the manager-side decision diamond after receiving proposals has an extra branch: a new 'callforproposal' that loops back up to the contractor's lifeline (iteration), alongside 'reject' and 'accept'. Then 'inform' or 'cancel' from the contractor as before.
- Why it matters: Shows the Iterated Contract Net: the manager can re-issue a revised call for proposals instead of accepting, enabling multi-round negotiation.
- Transcribed text: manager; contractor; callforproposal; reject; propose; reject; callforproposal; accept; inform; cancel.

### contract-net-protocol.web/images/enwiki-25.svg
- Provenance: `research/web/contract-net-protocol/assets/enwiki-25.svg`. Wikipedia globe icon, site chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### contract-net-protocol.web/images/wikipedia-wordmark-en-25.svg
- Provenance: `research/web/contract-net-protocol/assets/wikipedia-wordmark-en-25.svg` (alt "Wikipedia"). Site chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### contract-net-protocol.web/images/wikipedia-tagline-en-25.svg
- Provenance: `research/web/contract-net-protocol/assets/wikipedia-tagline-en-25.svg` (alt "The Free Encyclopedia"). Site chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

## Raw / preserved excerpts

> The **Contract Net Protocol** (CNP) is a task-sharing protocol in multi-agent systems, introduced in 1980 by Reid G. Smith. It is used to allocate tasks among autonomous agents. It is close to sealed auctions protocols. It mainly relies on the Subcontractor: a manager proposes a task to several agents. The latter make a proposal among which the manager chooses to allocate the task. This task can then be divided and subcontracted.

**Formal description**

> The formalization of the protocol can be performed through the speech act theory. In this protocol, each agent can be either *manager* or *contractor*
>
> 1. The protocol is initialized by the manager, who sends a *call-for-proposals* to the contractors
> 2. The contractors can send either a *proposal* if they are interested or a *reject* if they are not. This proposal is provided with all the elements required by the manager to make its choice.
> 3. The manager chooses among the proposals the one that suits it best and sends to the corresponding contractor an *accept*. It sends a *reject* to the other contractors to inform them of its decision.
> 4. Once the contract has been accomplished, the contractor informs the manager using an *inform* message. If there is a result to communicate, it is also communicated through the *inform* message. If the contractor cannot fulfill its engagement, it informs the manager through a *cancel* message.
>
> The Contract Net Protocol can be represented using the AUML formalism.
>
> This protocol can be used to implement hierarchical organizations, where a manager assigns tasks to contractors, who in turn decompose into lower-level task and assign them to the lower level. This kind of organization can be used when agents are cooperative, *i.e.* when their objectives are identical. In this situation, it is possible to make sure that the contractors do not lie to the manager when they make their proposal. When the agents are competitive, the protocol ends up in a marketplace organization, very similar to auctions.

**Implementation**

> The protocol has been implemented by the FIPA in the ACL (Agent Communication Language).
>
> The Contract Net Protocol has been implemented for various problems and contexts. The original article describes a sensor network use case. Subsequent work showed its utility in this context. It has also been used for Multi-Robot Task Allocation. It has also been used as a negotiation protocol both for e commerce marketplaces and for supply chains.

**Issues and extensions**

> Reid G Smith identified several issues related to its protocol. In particular, he proposes to create only short messages, and to interact only with agents that could be relevant to the proposed task in order to avoid overloading the network communication in terms of exchanged messages. In order to limit the number of interactions, in the case where a manager knows with which contractor it would like to contract, it can contact it directly to make an offer, that the contractor can accept or not.
>
> A second issue is related to the occupation rate of the contractor when there are many tasks. Indeed, in this case, it may be complicated for the manager to find available contractors. In order to solve this problem, the contractor can answer a call for proposals even if they are already working for another contract. This trick can be used to prevent a situation where the manager makes call for proposals without getting any answer because the contractors are all busy. In this case, the contractors add to their proposal the moment when they'll be ready to seal with the proposal from the manager. Similarly in this situation, it is possible to keep a list of all available contractors so that the manager can contact them first. This trick makes it possible to avoid a network overload due to the managers sending their call for proposals to all the agents over and over again while ensuring that they will eventually find a contractor to contract on the proposed task. This information is directly sent to the managers by the contractors.
>
> Beyond extensions proposed by the author, several works have extended the Contract Net Protocol. One of the issues raised by it is the fact that the manager cannot precise what it values most. It must choose among the proposals it receives from the contractors. In the case where each contractor can make a range of proposals, this can lead to suboptimal solutions. To address this issue, the FIPA also proposes an iterated version of the protocol in which the manager can make a new call for proposal some of the contractors that answered it, and refuse others, eventually accepting one of them. The resulting protocol can be compared with the iterated auction protocols. As the CNP, this protocol can be represented as an AUML diagram
>
> Another issue of the protocol is actually dealing with the task. In the original protocol, a contractor that makes a proposal commits to accomplish the task it has made a proposal on, whatever it takes. The failure of the task is only taken in consideration through the *cancel* message informing the manager that the task won't be addressed, without any sanction for the contractor. In the case where the agent is selfish, they therefore may have an incentive to make as many proposals as they can, and only fulfill the most profitable ones. In a collaborative context, the agent has no way to know if opting out from a task in order to commit to another one is good for the overall system. An extension of the protocol has been released in 1995 by Tuomas Sandholm and Victor Lesser in order to take these elements into account and define beforehand a commitment cost for the contractor to pay if they cannot accomplish the task.

**References** (verbatim list)

1. Smith (December 1980). "The Contract Net Protocol: High-Level Communication and Control in a Distributed Problem Solver". *IEEE Transactions on Computers*. C-29 (12): 1104–1113. doi:10.1109/TC.1980.1675516.
2. Horling, Bryan; Lesser, Victor (2005-11-11). "A survey of multi-agent organizational paradigms". *The Knowledge Engineering Review*. 19 (4): 281. doi:10.1017/S0269888905000317.
3. "FIPA Contract Net Interaction Protocol Specification". fipa.org (http://www.fipa.org/specs/fipa00029/SC00029H.html). Retrieved 2019-04-09.
4. Chen, L.; Xue-song, Q.; Yang, Y.; Gao, Z.; Qu, Z. (July 2012). "The contract net based task allocation algorithm for wireless sensor network". 2012 IEEE ISCC. pp. 000600–000604. doi:10.1109/ISCC.2012.6249362.
5. Grabovskis, Arvids; Lavendelis, Egons; Liekna, Aleksis (2012-11-08). "Experimental analysis of contract net protocol in multi-robot task allocation". *Applied Computer Systems*. 13 (1): 6–14. doi:10.2478/v10312-012-0001-7.
6. Sandholm, Tuomas (1993). "An implementation of the contract net protocol based on marginal cost calculations". AAAI-93 Proceedings. pp. 256–262.
7. (Roger) Jiao, Jianxin; You, Xiao; Kumar, Arun (July 2006). "An agent-based framework for collaborative negotiation in the global manufacturing supply chain network". *Robotics and Computer-Integrated Manufacturing*. 22 (3): 239–255. doi:10.1016/j.rcim.2005.04.003.
8. "FIPA Iterated Contract Net Interaction Protocol Specification". fipa.org (http://www.fipa.org/specs/fipa00030/SC00030H.html). Retrieved 2019-04-09.
9. Sandholm, Tuomas; Lesser, Victor (1995). "Issues in automated negotiation and electronic commerce: Extending the contract net framework". Proceedings of the First International Conference on Multiagent Systems. pp. 328–335.
