# RAG Fundamentals - AI Tutorial

_Source: <https://aitutorial.dev/rag/fundamentals>_

> 

## Documentation Index

Fetch the complete documentation index at: [/llms.txt](/llms.txt)

Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)![light logo](https://mintcdn.com/digibee-1a4db0d2/qVB-_urhSn1RCBv0/logo/logo-light-full.svg?fit=max&auto=format&n=qVB-_urhSn1RCBv0&q=85&s=720536383dc8eb2a95e11611fc7839b4)![dark logo](https://mintcdn.com/digibee-1a4db0d2/qVB-_urhSn1RCBv0/logo/logo-dark-full.svg?fit=max&auto=format&n=qVB-_urhSn1RCBv0&q=85&s=dde82d875ffc50b174137cb594049e8e)[AI Tutorial home page](/)Search...⌘KSearch...NavigationRetrieval Augmented Generation (RAG)RAG FundamentalsRetrieval Augmented Generation (RAG)

# RAG Fundamentals

Copy pageCopy page

The core RAG pattern and how it works

Copy pageCopy pageLLMs only know what they were trained on. RAG bridges this gap by retrieving relevant data and injecting it into the prompt. This page covers the core pattern and a production pipeline. 

## [​](#why-rag)Why RAG?

LLMs are powerful — but they have a fundamental limitation: **they only know what they were trained on.** Ask an LLM about your company’s Q4 revenue, yesterday’s incident report, or a document you uploaded last week, and it will either hallucinate an answer or admit it doesn’t know. This is the **knowledge boundary problem**, and RAG is how production systems solve it. 

### [​](#the-problem-rag-solves)The Problem RAG Solves

Try asking the model about private company data — it simply doesn’t have it: If you try this same question in ChatGPT, you might get a real answer — but that’s because ChatGPT is not a pure LLM. It has built-in tools (web browsing, code interpreter, etc.) that fetch live data behind the scenes. Under the hood, it’s doing exactly what we’re about to build: retrieving external data and injecting it into the prompt. The difference is that you don’t control the retrieval pipeline — ChatGPT decides what to search, which sources to trust, and what context to use. Building your own RAG gives you full control over these decisions. 

### [​](#when-you-need-rag)When You Need RAG

ScenarioWhy the LLM alone failsWhat RAG adds**Data freshness**Training data has a cutoff date — the model doesn’t know about anything afterRetrieves current data from live sources**Proprietary data**Your internal docs, databases, and APIs were never in the training setConnects the LLM to your private knowledge base**Accuracy & citations**The model can hallucinate plausible-sounding but wrong answersConstrains generation to retrieved facts with source citations**Cost**Fine-tuning a model on new data is expensive and slow to updateJust update your document store — no retraining needed**Auditability**You can’t trace why the model said somethingEvery answer links back to specific source documents 

### [​](#the-simplest-rag-three-lines-of-logic)The Simplest RAG: Three Lines of Logic

At its core, RAG is just three steps: 

```
1. RETRIEVE  →  Find relevant documents for the user's question
2. AUGMENT   →  Insert those documents into the prompt as context
3. GENERATE  →  Have the LLM answer using only the provided context

```

That’s it. Everything else — chunking, embeddings, reranking, hybrid search — is about making each step better. Let’s start with the simplest working version. 

## [​](#basic-rag-implementation)Basic RAG Implementation

The company documents live in a JSON file (`assets/company_docs.json`), but they could come from anywhere — a database, an API, a CMS, a web scraper. The RAG pattern is the same regardless of the data source. This prototype works but has clear limitations: 

- No error handling 
- No caching (repeated queries waste money) 
- No retrieval quality measurement 
- Single-stage retrieval (accuracy suffers) 
- No lexical/vector hybrid search 
- No metadata or filtering 
We’ll fix these throughout the module. 

## [​](#the-real-life-rag-pipeline)The Real-Life RAG Pipeline

Production RAG systems go beyond “search + LLM.” They use a carefully designed multi-stage pipeline where each stage solves a distinct problem. 

```
+------------------+
│    User Query    │
+------------------+
        |
        v
+------------------+
│  Stage 1:        │
│  Fast Retrieval  │  ← Get 10-50 candidates per method
│  (Lexical/Vector)│     (prioritize recall over precision)
+------------------+
        |
        v
+------------------+
│  Stage 2:        │
│  Rank Fusion     │  ← Merge results from multiple retrievers
│  (RRF)           │     into a single ranked list
+------------------+
        |
        v
+------------------+
│  Stage 3:        │
│  Reranking       │  ← Narrow to top 3-5 precisely
│  (Cross-Encoder) │     (prioritize precision over speed)
+------------------+
        |
        v
+------------------+
│  Stage 4:        │
│  LLM Generation  │  ← Use retrieved context to generate
│  (GPT-4/Claude)  │     grounded response
+------------------+
        |
        v
+------------------+
│    Response      │
+------------------+

```

### [​](#why-multi-stage-retrieval)Why Multi-Stage Retrieval?

**The Fundamental Trade-off:** 

- Fast retrieval methods (lexical, vector) can process 100K+ documents in milliseconds 
- Accurate ranking methods (cross-encoders) can only handle ~100 documents in reasonable time 
- Solution: Use fast methods to filter, fuse their results, then use an accurate method to rank 
**Why Rank Fusion (RRF)?** 

- Different retrieval methods have different strengths — lexical search excels at exact keyword matches, while vector search captures semantic similarity 
- Running both in parallel and then merging the results with **Reciprocal Rank Fusion (RRF)** gives you the best of both worlds 
- RRF combines ranked lists by assigning each document a score based on its rank position across all retrievers: `score = Σ 1/(k + rank)` — documents that appear high in multiple lists bubble to the top 
- This fused list is then passed to the cross-encoder reranker for precise scoring 
**Latency in practice (varies by system):** 

- First-pass retrieval returns a small candidate set quickly (implementation-, scale-, and hardware-dependent). 
- RRF merging is near-instant — it’s just arithmetic over rank positions. 
- Cross-encoder reranking narrows to top results but adds additional latency. 
- Production systems typically target interactive end-to-end latency budgets on available hardware. 

## [​](#production-rag-key-components)Production RAG: Key Components

A production RAG system needs: 

1. **Document Processing Pipeline** 

- Chunking strategy (size, overlap) 
- Metadata extraction (title, date, source) 
- Quality filtering 

2. **Multi-Stage Retrieval** 

- First-pass: Fast, broad recall (lexical and vector in parallel) 
- Rank fusion: Merge results from multiple retrievers via RRF 
- Reranking: Slow, precise scoring with cross-encoders 

3. **Context Engineering** 

- Prompt design for grounding 
- Citation formatting 
- Handling insufficient context 

4. **Evaluation Framework** 

- Retrieval metrics (Recall@k, NDCG) 
- Generation metrics (faithfulness, relevance) 
- Component-level debugging 

5. **Observability** 

- Retrieval quality monitoring 
- Latency tracking 
- Cost per query 

We’ll build each component step by step. 

Was this page helpful?

YesNo⌘I
