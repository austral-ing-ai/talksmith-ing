# [2604.24827] Incompressible Knowledge Probes: Estimating Black-Box LLM Parameter Counts via Factual Capacity

_Source: <https://arxiv.org/abs/2604.24827>_

[Skip to main content](#content) <https://arxiv.org/IgnoreMe> ![archive](/static/base/1.0.1/images/arxiv-logo-primary-light.svg) <https://arxiv.org/>  Press Enter to search · [Advanced search](https://arxiv.org/search/advanced) 

# Computer Science > Machine Learning

**arXiv:2604.24827** (cs)  [Submitted on 27 Apr 2026 ([v1](https://arxiv.org/abs/2604.24827v1)), last revised 5 Jul 2026 (this version, v2)] 

# Title:Incompressible Knowledge Probes: Estimating Black-Box LLM Parameter Counts via Factual Capacity

Authors:[Bojie Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+B) View a PDF of the paper titled Incompressible Knowledge Probes: Estimating Black-Box LLM Parameter Counts via Factual Capacity, by Bojie Li [View PDF](/pdf/2604.24827) [HTML (experimental)](https://arxiv.org/html/2604.24827v2) 

> Abstract:Closed-source frontier labs do not disclose parameter counts. Storing F facts requires at least F/(bits per parameter) weights, so factual recall lower-bounds parameter count--an intrinsic, serving-independent signal, though (as we show) a coarse one. We introduce Incompressible Knowledge Probes (IKPs), a benchmark of 1,400 factual questions spanning 7 tiers of obscurity, designed to isolate knowledge that cannot be derived by reasoning or compressed by architectural improvements.   
We score with no hallucination penalty (lambda = 0: IKP accuracy is simply the fraction of probed facts answered correctly), which removes both the penalty hyperparameter and the per-tier flooring choice; a full lambda x flooring ablation shows the calibration is robust across scoring choices while individual estimates are not, motivating the no-penalty default. We calibrate a log-linear mapping from IKP accuracy to parameter count on 93 open-weight models (135M-1,600B) spanning 19 vendors, achieving R^2 = 0.910; leave-one-out cross-validation confirms generalization (median fold error 1.48x, 72% within 2x, 86% within 3x). The instrument is deliberately coarse--its 90% prediction interval spans ~3x in either direction, wider than inference economics--so IKP recovers order-of-magnitude effective capacity and relative rankings, not precise parameter counts. For Mixture-of-Experts models, total parameters predict knowledge (R^2 = 0.67) better than active parameters (R^2 = 0.41). We evaluate 201 models from 27 vendors on a curated probe set (1,311 of 1,400 probes surviving name-collision and label-ambiguity filters) and report effective knowledge capacity for all major proprietary frontier models as prediction bands rather than point estimates; for heavily safety-tuned models these are lower bounds, since refusal policy can suppress tens of percentage points of otherwise-answerable capacity. 

Subjects: Machine Learning (cs.LG); Artificial Intelligence (cs.AI) Cite as: [arXiv:2604.24827](https://arxiv.org/abs/2604.24827) [cs.LG] (or [arXiv:2604.24827v2](https://arxiv.org/abs/2604.24827v2) [cs.LG] for this version) [https://doi.org/10.48550/arXiv.2604.24827](https://doi.org/10.48550/arXiv.2604.24827) Focus to learn more  arXiv-issued DOI via DataCite 

## Submission history

 From: Bojie Li [[view email](/show-email/df368cd9/2604.24827)]   
**[[v1]](/abs/2604.24827v1)** Mon, 27 Apr 2026 15:46:23 UTC (2,479 KB)  
**[v2]** Sun, 5 Jul 2026 14:51:01 UTC (2,531 KB)  
Full-text links: 

## Access Paper:

 View a PDF of the paper titled Incompressible Knowledge Probes: Estimating Black-Box LLM Parameter Counts via Factual Capacity, by Bojie Li
- [View PDF](/pdf/2604.24827)
- [HTML (experimental)](https://arxiv.org/html/2604.24827v2)
- [TeX Source](/src/2604.24827)
![license icon](https://arxiv.org/icons/licenses/by-4.0.png) [view license](http://creativecommons.org/licenses/by/4.0/) 

### Current browse context:

cs.LG [< prev](/prevnext?id=2604.24827&function=prev&context=cs.LG)  | [next >](/prevnext?id=2604.24827&function=next&context=cs.LG)   
[new](/list/cs.LG/new)  | [recent](/list/cs.LG/recent)  | [2026-04](/list/cs.LG/2026-04)  Change to browse by: [cs](/abs/2604.24827?context=cs)  
[cs.AI](/abs/2604.24827?context=cs.AI)  

### References & Citations

- [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2604.24827)
- [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2604.24827) 
- [Semantic Scholar](https://api.semanticscholar.org/arXiv:2604.24827) 
export BibTeX citation Loading... 

## BibTeX formatted citation

× loading... Data provided by: 

### Bookmark

![BibSonomy](/static/browse/0.3.4/images/icons/social/bibsonomy.png) <http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2604.24827&description=Incompressible Knowledge Probes: Estimating Black-Box LLM Parameter Counts via Factual Capacity> ![Reddit](/static/browse/0.3.4/images/icons/social/reddit.png) <https://reddit.com/submit?url=https://arxiv.org/abs/2604.24827&title=Incompressible Knowledge Probes: Estimating Black-Box LLM Parameter Counts via Factual Capacity> Bibliographic Tools 

# Bibliographic and Citation Tools

Bibliographic Explorer Toggle Bibliographic Explorer *([What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))* Connected Papers Toggle Connected Papers *([What is Connected Papers?](https://www.connectedpapers.com/about))* Litmaps Toggle Litmaps *([What is Litmaps?](https://www.litmaps.co/))* scite.ai Toggle scite Smart Citations *([What are Smart Citations?](https://www.scite.ai/))* Code, Data, Media 

# Code, Data and Media Associated with this Article

alphaXiv Toggle alphaXiv *([What is alphaXiv?](https://alphaxiv.org/))* Links to Code Toggle CatalyzeX Code Finder for Papers *([What is CatalyzeX?](https://www.catalyzex.com))* DagsHub Toggle DagsHub *([What is DagsHub?](https://dagshub.com/))* GotitPub Toggle Gotit.pub *([What is GotitPub?](http://gotit.pub/faq))* Huggingface Toggle Hugging Face *([What is Huggingface?](https://huggingface.co/huggingface))* ScienceCast Toggle ScienceCast *([What is ScienceCast?](https://sciencecast.org/welcome))* Demos 

# Demos

Replicate Toggle Replicate *([What is Replicate?](https://replicate.com/docs/arxiv/about))* Spaces Toggle Hugging Face Spaces *([What is Spaces?](https://huggingface.co/docs/hub/spaces))* Spaces Toggle TXYZ.AI *([What is TXYZ.AI?](https://txyz.ai))* Related Papers 

# Recommenders and Search Tools

Link to Influence Flower Influence Flower *([What are Influence Flowers?](https://influencemap.cmlab.dev/))* Core recommender toggle CORE Recommender *([What is CORE?](https://core.ac.uk/services/recommender))* IArxiv recommender toggle IArxiv Recommender *([What is IArxiv?](https://iarxiv.org/about))* 

- Author 
- Venue 
- Institution 
- Topic 
 About arXivLabs 

# arXivLabs: experimental projects with community collaborators

arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

Have an idea for a project that will add value for arXiv's community? ****[Learn more about arXivLabs](https://info.arxiv.org/labs/index.html).

[Which authors of this paper are endorsers?](/auth/show-endorsers/2604.24827) | [Disable MathJax](javascript:setMathjaxCookie()) ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
