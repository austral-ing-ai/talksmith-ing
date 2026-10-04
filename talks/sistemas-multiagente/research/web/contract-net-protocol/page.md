# Contract Net Protocol - Wikipedia

_Source: <https://en.wikipedia.org/wiki/Contract_Net_Protocol>_

[Jump to content](#bodyContent) ![](/static/images/icons/enwiki-25.svg) ![Wikipedia](/static/images/mobile/copyright/wikipedia-wordmark-en-25.svg) ![The Free Encyclopedia](/static/images/mobile/copyright/wikipedia-tagline-en-25.svg) </wiki/Main_Page> [Search](/wiki/Special:Search) 

# Contract Net Protocol

3 languages 

- [Čeština](https://cs.wikipedia.org/wiki/Kontrakta%C4%8Dn%C3%AD_s%C3%AD%C5%A5)
- [Deutsch](https://de.wikipedia.org/wiki/Contract_Net)
- [Français](https://fr.wikipedia.org/wiki/Contract_Net_Protocol) 
[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q1129064#sitelinks-wikipedia) From Wikipedia, the free encyclopedia Computer task-sharing protocol 

The **Contract Net Protocol** (CNP) is a task-sharing protocol in [multi-agent systems](https://en.wikipedia.org/wiki/Multi-agent_systems), introduced in 1980 by Reid G. Smith.[[1]](#cite_note-1) It is used to allocate tasks among autonomous agents. It is close to [sealed auctions protocols](https://en.wikipedia.org/wiki/Auction#Primary). It mainly relies on the [Subcontractor](https://en.wikipedia.org/wiki/Subcontracting): a manager proposes a task to several agents. The latter make a proposal among which the manager chooses to allocate the task. This task can then be divided and subcontracted.

## Formal description

[[edit](/w/index.php?title=Contract_Net_Protocol&action=edit&section=1)] 

The formalization of the protocol can be performed through the [speech act](https://en.wikipedia.org/wiki/Speech_act) theory. In this protocol, each agent can be either *manager* or *contractor*

1. The protocol is initialized by the manager, who sends a *call-for-proposals* to the contractors 
2. The contractors can send either a *proposal* if they are interested or a *reject* if they are not. This proposal is provided with all the elements required by the manager to make its choice. 
3. The manager chooses among the proposals the one that suits it best and sends to the corresponding contractor an *accept*. It sends a *reject* to the other contractors to inform them of its decision. 
4. Once the contract has been accomplished, the contractor informs the manager using an *inform* message. If there is a result to communicate, it is also communicated through the *inform* message. If the contractor cannot fulfill its engagement, it informs the manager through a *cancel* message.

The Contract Net Protocol can be represented using the [AUML](https://en.wikipedia.org/wiki/AUML?action=edit&redlink=1) formalism:

![Contract Net Protocol AUML Diagram](//thumb.wikimedia.org/wikipedia/commons/thumb/f/f8/CNP.svg/500px-CNP.svg.png?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail)<https://en.wikipedia.org/wiki/File:CNP.svg>Contract Net Protocol AUML Diagram 

This protocol can be used to implement hierarchical organizations, where a manager assigns tasks to contractors, who in turn decompose into lower-level task and assign them to the lower level. This kind of organization can be used when agents are cooperative, *i.e.* when their objectives are identical. In this situation, it is possible to make sure that the contractors do not lie to the manager when they make their proposal. When the agents are competitive, the protocol ends up in a marketplace organization, very similar to auctions.[[2]](#cite_note-2)

## Implementation

[[edit](/w/index.php?title=Contract_Net_Protocol&action=edit&section=2)] 

The protocol has been implemented by the [FIPA](https://en.wikipedia.org/wiki/Foundation_for_Intelligent_Physical_Agents) in the [ACL](https://en.wikipedia.org/wiki/FIPA-ACL) (Agent Communication Language).[[3]](#cite_note-3)

The Contract Net Protocol has been implemented for various problems and contexts. The original article describes a sensor network use case. Subsequent work showed its utility in this context.[[4]](#cite_note-4) It has also been used for Multi-Robot Task Allocation.[[5]](#cite_note-5) It has also been used as a negotiation protocol both for e commerce marketplaces [[6]](#cite_note-6) and for supply chains.[[7]](#cite_note-7)

## Issues and extensions

[[edit](/w/index.php?title=Contract_Net_Protocol&action=edit&section=3)] 

Reid G Smith identified several issues related to its protocol. In particular, he proposes to create only short messages, and to interact only with agents that could be relevant to the proposed task in order to avoid overloading the network communication in terms of exchanged messages. In order to limit the number of interactions, in the case where a manager knows with which contractor it would like to contract, it can contact it directly to make an offer, that the contractor can accept or not.

A second issue is related to the occupation rate of the contractor when there are many tasks. Indeed, in this case, it may be complicated for the manager to find available contractors. In order to solve this problem, the contractor can answer a call for proposals even if they are already working for another contract. This trick can be used to prevent a situation where the manager makes call for proposals without getting any answer because the contractors are all busy. In this case, the contractors add to their proposal the moment when they'll be ready to seal with the proposal from the manager. Similarly in this situation, it is possible to keep a list of all available contractors so that the manager can contact them first. This trick makes it possible to avoid a network overload due to the managers sending their call for proposals to all the agents over and over again while ensuring that they will eventually find a contractor to contract on the proposed task. This information is directly sent to the managers by the contractors.

Beyond extensions proposed by the author, several works have extended the Contract Net Protocol. One of the issues raised by it is the fact that the manager cannot precise what it values most. It must choose among the proposals it receives from the contractors. In the case where each contractor can make a range of proposals, this can lead to suboptimal solutions. To address this issue, the FIPA also proposes an iterated version of the protocol in which the manager can make a new call for proposal some of the contractors that answered it, and refuse others, eventually accepting one of them. The resulting protocol can be compared with the iterated auction protocols. As the CNP, this protocol can be represented as an [AUML](https://en.wikipedia.org/wiki/AUML?action=edit&redlink=1) diagram [[8]](#cite_note-8)

![Iterated Contract Net Protocol AUML diagram](//thumb.wikimedia.org/wikipedia/commons/thumb/8/89/Icnp.svg/500px-Icnp.svg.png?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail)<https://en.wikipedia.org/wiki/File:Icnp.svg> 

Another issue of the protocol is actually dealing with the task. In the original protocol, a contractor that makes a proposal commits to accomplish the task it has made a proposal on, whatever it takes. The failure of the task is only taken in consideration through the *cancel* message informing the manager that the task won't be addressed, without any sanction for the contractor. In the case where the agent is selfish, they therefore may have an incentive to make as many proposals as they can, and only fulfill the most profitable ones. In a collaborative context, the agent has no way to know if opting out from a task in order to commit to another one is good for the overall system. An extension of the protocol has been released in 1995 by Tuomas Sandholm and [Victor Lesser](https://en.wikipedia.org/wiki/Victor_R._Lesser) in order to take these elements into account and define beforehand a commitment cost for the contractor to pay if they cannot accomplish the task.[[9]](#cite_note-9)

## References

[[edit](/w/index.php?title=Contract_Net_Protocol&action=edit&section=4)] 

1. [↑](#cite_ref-1) Smith (December 1980). "The Contract Net Protocol: High-Level Communication and Control in a Distributed Problem Solver". *IEEE Transactions on Computers*. **C-29** (12): 1104–1113. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1109/TC.1980.1675516](https://doi.org/10.1109%2FTC.1980.1675516). [ISSN](https://en.wikipedia.org/wiki/ISSN_(identifier)) [0018-9340](https://search.worldcat.org/issn/0018-9340). [S2CID](https://en.wikipedia.org/wiki/S2CID_(identifier)) [15267324](https://api.semanticscholar.org/CorpusID:15267324). 
2. [↑](#cite_ref-2) Horling, Bryan; Lesser, Victor (2005-11-11). "A survey of multi-agent organizational paradigms". *The Knowledge Engineering Review*. **19** (4): 281. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1017/S0269888905000317](https://doi.org/10.1017%2FS0269888905000317). [ISSN](https://en.wikipedia.org/wiki/ISSN_(identifier)) [0269-8889](https://search.worldcat.org/issn/0269-8889). [S2CID](https://en.wikipedia.org/wiki/S2CID_(identifier)) [562855](https://api.semanticscholar.org/CorpusID:562855). 
3. [↑](#cite_ref-3) ["FIPA Contract Net Interaction Protocol Specification"](http://www.fipa.org/specs/fipa00029/SC00029H.html). *fipa.org*. Retrieved 2019-04-09. 
4. [↑](#cite_ref-4) Chen, L.; Xue-song, Q.; Yang, Y.; Gao, Z.; Qu, Z. (July 2012). "The contract net based task allocation algorithm for wireless sensor network". *2012 IEEE Symposium on Computers and Communications (ISCC)*. pp. 000600–000604. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1109/ISCC.2012.6249362](https://doi.org/10.1109%2FISCC.2012.6249362). [ISBN](https://en.wikipedia.org/wiki/ISBN_(identifier)) [978-1-4673-2713-8](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4673-2713-8). [S2CID](https://en.wikipedia.org/wiki/S2CID_(identifier)) [11799626](https://api.semanticscholar.org/CorpusID:11799626). 
5. [↑](#cite_ref-5) Grabovskis, Arvids; Lavendelis, Egons; Liekna, Aleksis (2012-11-08). ["Experimental analysis of contract net protocol in multi-robot task allocation"](https://doi.org/10.2478%2Fv10312-012-0001-7). *Applied Computer Systems*. **13** (1): 6–14. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.2478/v10312-012-0001-7](https://doi.org/10.2478%2Fv10312-012-0001-7). 
6. [↑](#cite_ref-6) Sandholm, Tuomas (1993). ["An implementation of the contract net protocol based on marginal cost calculations"](https://www.aaai.org/Papers/AAAI/1993/AAAI93-039.pdf) (PDF). *AAAI-93 Proceedings*. pp. 256–262. 
7. [↑](#cite_ref-7) (Roger) Jiao, Jianxin; You, Xiao; Kumar, Arun (July 2006). "An agent-based framework for collaborative negotiation in the global manufacturing supply chain network". *Robotics and Computer-Integrated Manufacturing*. **22** (3): 239–255. [doi](https://en.wikipedia.org/wiki/Doi_(identifier)):[10.1016/j.rcim.2005.04.003](https://doi.org/10.1016%2Fj.rcim.2005.04.003). 
8. [↑](#cite_ref-8) ["FIPA Iterated Contract Net Interaction Protocol Specification"](http://www.fipa.org/specs/fipa00030/SC00030H.html). *fipa.org*. Retrieved 2019-04-09. 
9. [↑](#cite_ref-9) Sandholm, Tuomas; Lesser, Victor (1995). ["Issues in automated negotiation and electronic commerce: Extending the contract net framework"](https://www.aaai.org/Papers/ICMAS/1995/ICMAS95-044.pdf) (PDF). *Proceedings of the First International Conference on Multiagent Systems*. pp. 328–335. 

## See also

[[edit](/w/index.php?title=Contract_Net_Protocol&action=edit&section=5)] 

- [Multi-agent system](https://en.wikipedia.org/wiki/Multi-agent_system) 
- [Intelligent agent](https://en.wikipedia.org/wiki/Intelligent_agent) 
- [Agent-based model](https://en.wikipedia.org/wiki/Agent-based_model)
Retrieved from "[https://en.wikipedia.org/w/index.php?title=Contract_Net_Protocol&oldid=1342154242](https://en.wikipedia.org/w/index.php?title=Contract_Net_Protocol&oldid=1342154242)" [Categories](/wiki/Help:Category): 

- [Agent communications languages](/wiki/Category:Agent_communications_languages)
- [Multi-robot systems](/wiki/Category:Multi-robot_systems)
Hidden categories: 

- [Articles with short description](/wiki/Category:Articles_with_short_description)
- [Short description matches Wikidata](/wiki/Category:Short_description_matches_Wikidata)
Search Contract Net Protocol <#> <#> <#> <#> <#> <#> <#> 3 languages [Add topic](#)
