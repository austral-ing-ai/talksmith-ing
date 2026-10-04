# Overview & Learning Objectives - AI Tutorial

_Source: <https://aitutorial.dev/agents/overview>_

> 

## Documentation Index

Fetch the complete documentation index at: [/llms.txt](/llms.txt)

Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)![light logo](https://mintcdn.com/digibee-1a4db0d2/qVB-_urhSn1RCBv0/logo/logo-light-full.svg?fit=max&auto=format&n=qVB-_urhSn1RCBv0&q=85&s=720536383dc8eb2a95e11611fc7839b4)![dark logo](https://mintcdn.com/digibee-1a4db0d2/qVB-_urhSn1RCBv0/logo/logo-dark-full.svg?fit=max&auto=format&n=qVB-_urhSn1RCBv0&q=85&s=dde82d875ffc50b174137cb594049e8e)[AI Tutorial home page](/)Search...⌘KSearch...NavigationAI AgentsOverview & Learning ObjectivesAI Agents

# Overview & Learning Objectives

Copy pageCopy page

Overview and learning objectives for AI Agents

Copy pageCopy page

## [​](#module-overview)Module Overview

**You’ve probably noticed:** Simple LLM calls work great for one-shot tasks, but real applications need systems that can use tools, maintain context, and execute multi-step workflows reliably. **Here’s the challenge:** Building agents that work in demos is easy. Building agents that meet enterprise reliability requirements (95%+ accuracy) is hard. Most agent projects fail not because of the LLM, but because of tool design, memory architecture, and rule enforcement. **In this module:** You’ll build production-grade agent systems — from single-tool agents to multi-server MCP architectures with thread-based memory, security guardrails, and deterministic business rule validation. 

## [​](#learning-objectives)Learning Objectives

By the end of this module, you will be able to: 

- ✅ Build agents with tool calling using LangChain’s `createAgent` 
- ✅ Design and deploy MCP servers with proper tool descriptions 
- ✅ Connect agents to multiple MCP servers via `MultiServerMCPClient` 
- ✅ Implement thread-based memory with `MemorySaver` and long-term memory patterns 
- ✅ Enforce business rules deterministically with validation tools 
- ✅ Build security guardrails: PII detection, jailbreak prevention, output filtering 
- ✅ Optimize tool selection for accuracy at scale 

## [​](#why-this-matters)Why This Matters

The gap between an agent demo and a production agent is enormous: 

- **Tool accuracy:** Agent accuracy drops from 92% to 58% as you go from 5 to 20+ tools. Design matters more than model choice 
- **Business rules:** LLMs enforce prompt-based rules ~85% of the time. For financial, legal, or healthcare use cases, that’s not enough — deterministic validation is required 
- **Security:** Agents with tool access can leak PII, execute destructive actions, or be manipulated via indirect injection. Guardrails are not optional 
- **Interoperability:** MCP is the emerging standard for tool integration. Building on it now means your tools work with Claude, ChatGPT, Cursor, and any future MCP client 

## [​](#what-you’ll-build)What You’ll Build

- **Weather agent** — LangChain ReAct agent with tool calling 
- **MCP servers** — 3 domain servers (KnowledgeBase, CustomerInfo, IncidentTicket) 
- **Customer support agent** — multi-server agent with thread-based sessions and user identity via headers 
- **Memory examples** — working memory (MemorySaver) and long-term memory (cross-session persistence) 
- **Expense validator** — deterministic business rule enforcement via validation tools 
- **Security guardrails** — PII detection/redaction, jailbreak detection, output filtering pipeline 
- **Tool analytics** — usage tracking with optimization recommendations 

Was this page helpful?

YesNo⌘I
