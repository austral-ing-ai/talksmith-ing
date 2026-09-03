# Reranking & Precision Optimization - AI Tutorial

_Source: <https://aitutorial.dev/rag/reranking>_

> 

## Documentation Index

Fetch the complete documentation index at: [/llms.txt](/llms.txt)

Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)![light logo](https://mintcdn.com/digibee-1a4db0d2/qVB-_urhSn1RCBv0/logo/logo-light-full.svg?fit=max&auto=format&n=qVB-_urhSn1RCBv0&q=85&s=720536383dc8eb2a95e11611fc7839b4)![dark logo](https://mintcdn.com/digibee-1a4db0d2/qVB-_urhSn1RCBv0/logo/logo-dark-full.svg?fit=max&auto=format&n=qVB-_urhSn1RCBv0&q=85&s=dde82d875ffc50b174137cb594049e8e)[AI Tutorial home page](/)Search...⌘KSearch...NavigationRetrieval Augmented Generation (RAG)Reranking & Precision OptimizationRetrieval Augmented Generation (RAG)

# Reranking & Precision Optimization

Copy pageCopy page

Multi-stage retrieval with RRF fusion and cross-encoder reranking for precision optimization

Copy pageCopy pageFast retrieval finds candidates but ranks them poorly. This page covers multi-stage retrieval — hybrid search, RRF fusion, and cross-encoder reranking — for precision optimization. 

## [​](#why-multi-stage-retrieval)Why Multi-Stage Retrieval?

A single retrieval pass — whether lexical or semantic — returns noisy results. Relevant documents get buried, irrelevant ones slip through, and the LLM generates worse answers as a result. Multi-stage retrieval fixes this by progressively filtering and re-scoring candidates before they reach the LLM. **When you need it:** 

- Your RAG answers are inconsistent — sometimes great, sometimes wrong 
- Relevant documents exist but don’t appear in top results 
- You’re using both keyword and semantic search and want the best of both 
**How it works — each stage solves a different problem:** 

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

1. **Stage 1 (Fast Retrieval) - Maximize Recall:** 

- **Goal:** Don’t miss relevant documents — cast a wide net 
- **Method:** Retrieve many candidates (e.g., top-50) using fast methods like lexical and vector search in parallel 
- **Trade-off:** Fast but includes some noise/irrelevant results 

2. **Stage 2 (Rank Fusion) - Merge Results:** 

- **Goal:** Combine rankings from multiple retrievers into a single list 
- **Method:** Reciprocal Rank Fusion (RRF) scores each document by its rank across retrievers: `score = Σ 1/(k + rank)` 
- **Trade-off:** Near-instant, captures strengths of both lexical and semantic search 

3. **Stage 3 (Reranking) - Maximize Precision:** 

- **Goal:** Keep only the truly relevant documents — filter out the noise 
- **Method:** Use a more accurate cross-encoder model to deeply analyze each candidate and rerank them 
- **Trade-off:** Slower but much more accurate at identifying relevance 

4. **Stage 4 (LLM Generation) - Generate Answer:** 

- **Goal:** Produce a grounded response using the top-ranked context 
- **Method:** Feed the reranked documents into the LLM prompt 
- **Trade-off:** Quality depends on all previous stages 

**Why it works:** 

- Fast retrievers are good at finding candidates but not great at ranking them 
- Cross-encoders are excellent at ranking but too slow to run on thousands of documents 
- Combining both gives you speed + accuracy 
**Result:** Better quality documents sent to your LLM → better answers 

## [​](#the-4-stage-pipeline-in-practice)The 4-Stage Pipeline In Practice

The complete pipeline shows: 

1. **First-pass retrieval** (lexical + semantic in parallel) — Cast a wide net (top-50) 
2. **Reciprocal Rank Fusion (RRF)** — Merge results into a single ranked list 
3. **Cross-encoder reranking** — Keep only the best (top-5) 
4. **LLM generation** — Generate a grounded answer from the top results 
**Latency/cost tips:** 

- Keep candidate pool small (e.g., 20-100) and final top_k small (3-5). 
- Run first-pass lexical + semantic in parallel; batch rerank scoring for throughput. 
- Log latency and token/call costs during the lab. 

Was this page helpful?

YesNo⌘I
