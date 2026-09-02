# Slopsquatting - Wikipedia

_Source: <https://en.wikipedia.org/wiki/Slopsquatting>_

[Jump to content](#bodyContent) ![](/static/images/icons/enwiki-25.svg) ![Wikipedia](/static/images/mobile/copyright/wikipedia-wordmark-en-25.svg) ![The Free Encyclopedia](/static/images/mobile/copyright/wikipedia-tagline-en-25.svg) </wiki/Main_Page> [Search](/wiki/Special:Search) 

# Slopsquatting

Add languages 

[Add links](https://www.wikidata.org/wiki/Special:EntityPage/Q133898386#sitelinks-wikipedia) From Wikipedia, the free encyclopedia Type of cybersquatting ![](//upload.wikimedia.org/wikipedia/commons/thumb/8/86/Slopsquatting_flowchart.svg/250px-Slopsquatting_flowchart.svg.png?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail)<https://en.wikipedia.org/wiki/File:Slopsquatting_flowchart.svg>[Sequence diagram](https://en.wikipedia.org/wiki/Sequence_diagram) of slopsquatting 

**Slopsquatting** is a type of [cybersquatting](https://en.wikipedia.org/wiki/Cybersquatting). It is the practice of registering a non-existent software package name that a [large language model](https://en.wikipedia.org/wiki/Large_language_model) (LLM) may [hallucinate](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)) in its output, whereby someone unknowingly may copy-paste and install the software package without realizing it is fake.[[1]](#cite_note-Socket-1) Attempting to install a non-existent package should result in an error, but some have exploited this for their gain in the form of [typosquatting](https://en.wikipedia.org/wiki/Typosquatting).[[2]](#cite_note-cantstop-2)

The name is a [portmanteau](https://en.wikipedia.org/wiki/Portmanteau) of "[AI slop](https://en.wikipedia.org/wiki/AI_slop)" and "typosquatting".[[3]](#cite_note-3)

## History

[[edit](/w/index.php?title=Slopsquatting&action=edit&section=1)] 

In 2023, security researcher Bar Lanyado noted that LLMs hallucinated a package named "huggingface-cli".[[4]](#cite_note-4)[[5]](#cite_note-5)[[6]](#cite_note-LassoSecurity-6) While this name is identical to the command used for the command-line version of HuggingFace Hub, it is not the name of the package. The software is correctly installed with the code `pip install -U "huggingface_hub[cli]"`. Lanyado tested the potential for slopsquatting by uploading an empty package under this hallucinated name. In three months, it had received over 30,000 downloads.[[6]](#cite_note-LassoSecurity-6) The hallucinated packaged name was also used in the [README file](https://en.wikipedia.org/wiki/README_file) of a repo for research conducted by [Alibaba](https://en.wikipedia.org/wiki/Alibaba_Group).[[7]](#cite_note-7)

In April 2025, the term was coined by [Python Software Foundation](https://en.wikipedia.org/wiki/Python_Software_Foundation) Developer-in-Residence and security researcher Seth Larson and popularized by Andrew Nesbitt on [Mastodon](https://en.wikipedia.org/wiki/Mastodon_(social_network)).[[1]](#cite_note-Socket-1)[[8]](#cite_note-BleepingComputer-8)

In May 2025, the potential and prevalence of slopsquatting was detailed in the academic paper "We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs".[[1]](#cite_note-Socket-1)[[9]](#cite_note-9) Some of the paper's main findings are that 19.7% of the LLM recommended packages did not exist, [open-source](https://en.wikipedia.org/wiki/Open-source_software) models hallucinated far more frequently (21.7% on average, compared to [proprietary](https://en.wikipedia.org/wiki/Proprietary_software) / black-box models at 5.2%), [CodeLlama 7B](https://en.wikipedia.org/wiki/Codellama) and CodeLlama 34B hallucinated in over a third of outputs, and across all models, the researchers observed over 205,000 unique hallucinated package names.

## Prevention

[[edit](/w/index.php?title=Slopsquatting&action=edit&section=2)] 

To prevent being exploited by slopsquatting, package names should be manually verified and code that is AI-generated should never be assumed to be safe before being deployed to production environments.[[8]](#cite_note-BleepingComputer-8)[[10]](#cite_note-10) Moreover, dependency scanners, [lock files](https://en.wikipedia.org/wiki/Lock_files), and hash ID verifications to known and trusted package versions can be used.

## Impact

[[edit](/w/index.php?title=Slopsquatting&action=edit&section=3)] 

Feross Aboukhadijeh, CEO of security firm [Socket](https://en.wikipedia.org/wiki/Socket_(cybersecurity)?action=edit&redlink=1), warns that software engineers who are practicing [vibe coding](https://en.wikipedia.org/wiki/Vibe_coding) may be susceptible to slopsquatting and either using the code without reviewing it or the [AI assistant tool](https://en.wikipedia.org/wiki/AI_assistant) installing the non-existent package.[[2]](#cite_note-cantstop-2) As of July 2026, there has not yet been a reported case where slopsquatting has been used as a cyberattack.

## See also

[[edit](/w/index.php?title=Slopsquatting&action=edit&section=4)] 

- [Prompt injection](https://en.wikipedia.org/wiki/Prompt_injection) 
- [IDN homograph attack](https://en.wikipedia.org/wiki/IDN_homograph_attack)

## References

[[edit](/w/index.php?title=Slopsquatting&action=edit&section=5)] 

1. [1](#cite_ref-Socket_1-0) [2](#cite_ref-Socket_1-1) [3](#cite_ref-Socket_1-2) ["The Rise of Slopsquatting: How AI Hallucinations Are Fueling..."](https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks) *Socket*. Retrieved 2025-04-14. 
2. [1](#cite_ref-cantstop_2-0) [2](#cite_ref-cantstop_2-1) Claburn, Thomas (2025-04-12). ["LLMs can't stop making up software dependencies and sabotaging everything"](https://www.theregister.com/2025/04/12/ai_code_suggestions_sabotage_supply_chain/). *[The Register](https://en.wikipedia.org/wiki/The_Register)*. Retrieved 2025-04-14. 
3. [↑](#cite_ref-3) Cimpanu, Catalin. ["Risky Bulletin: AI slopsquatting... it's coming! - Risky Business Media"](https://www.risky.biz/risky-bulletin-ai-slopsquatting-its-coming/). *www.risky.biz*. Retrieved 2025-06-09. 
4. [↑](#cite_ref-4) Lanyado, Bar (2023-06-06). ["Can you trust ChatGPT's package recommendations?"](https://vulcan.io/blog/ai-hallucinations-package-risk). *Vulcan*. Retrieved 2025-06-10.`{{[cite web](https://en.wikipedia.org/wiki/Template:Cite_web)}}`: CS1 maint: deprecated archival service ([link](https://en.wikipedia.org/wiki/Category:CS1_maint:_deprecated_archival_service)) 
5. [↑](#cite_ref-5) Claburn, Thomas (2024-03-28). ["AI hallucinates software packages and devs download them – even if potentially poisoned with malware"](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/). *[The Register](https://en.wikipedia.org/wiki/The_Register)*. Retrieved 2025-04-14. 
6. [1](#cite_ref-LassoSecurity_6-0) [2](#cite_ref-LassoSecurity_6-1) ["Lasso Research: AI Package Hallucinations"](https://www.lasso.security/blog/ai-package-hallucinations). *Lasso Security*. Retrieved 2025-05-06. 
7. [↑](#cite_ref-7) ["Project Init · alibaba/GraphTranslator@4394d72"](https://github.com/alibaba/GraphTranslator/commit/4394d7227ae03b332c2f47a1971050b403c134e2). *GitHub*. Retrieved 2025-05-06. 
8. [1](#cite_ref-BleepingComputer_8-0) [2](#cite_ref-BleepingComputer_8-1) ["AI-hallucinated code dependencies become new supply chain risk"](https://www.bleepingcomputer.com/news/security/ai-hallucinated-code-dependencies-become-new-supply-chain-risk/). *BleepingComputer*. Retrieved 2025-06-10. 
9. [↑](#cite_ref-9) Spracklen, Joseph; Wijewickrama, Raveen; Sakib, A. H. M. Nazmus; Maiti, Anindya; Viswanath, Bimal; Jadliwala, Murtuza (2025-03-02), *We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs*, [arXiv](https://en.wikipedia.org/wiki/ArXiv_(identifier)):[2406.10279](https://arxiv.org/abs/2406.10279) 
10. [↑](#cite_ref-10) Zorz, Zeljka (2025-04-14). ["Package hallucination: LLMs may deliver malicious code to careless devs"](https://www.helpnetsecurity.com/2025/04/14/package-hallucination-slopsquatting-malicious-code/). *Help Net Security*. Retrieved 2025-06-10. 
Retrieved from "[https://en.wikipedia.org/w/index.php?title=Slopsquatting&oldid=1364039629](https://en.wikipedia.org/w/index.php?title=Slopsquatting&oldid=1364039629)" [Categories](/wiki/Help:Category): 

- [Cybercrime](/wiki/Category:Cybercrime)
- [2025 neologisms](/wiki/Category:2025_neologisms)
Hidden categories: 

- [Articles with short description](/wiki/Category:Articles_with_short_description)
- [Short description is different from Wikidata](/wiki/Category:Short_description_is_different_from_Wikidata)
- [CS1 maint: deprecated archival service](/wiki/Category:CS1_maint:_deprecated_archival_service)
Search Slopsquatting <#> <#> <#> <#> <#> <#> <#> Add languages [Add topic](#)
