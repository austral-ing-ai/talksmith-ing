---
source_file: aitutorial-hands-on-exercise/
source_type: web-capture
ingested_at: 2026-10-04
---

# Hands-On Exercise — AI Tutorial (AI Agents module): build a customer support agent

## Provenance
- Original location: research/web/aitutorial-hands-on-exercise/ (text from `page.md`; visible text of `original.html` checked, same content)
- Format: html (Mintlify docs site, web capture via talksmith:ingest)
- URL: https://aitutorial.dev/agents/hands-on-exercise
- Fetched: 2026-08-14T16:56:38Z (HTTP 200)
- Author / source (if known): aitutorial.dev ("AI Tutorial")
- Date of original (if known): not stated

## Key claims
- The exercise asks for a **single** customer support agent demonstrating three concepts: "Agent basics — Tool use with proper agent loop", "Well-designed tools — Following MCP best practices", "Memory management — Working memory for conversation + long-term for preferences".
- Tool design rules (MCP best practices): verb_noun_context naming; description covering "what, when to use, when NOT to use"; 3 or fewer parameters preferred; consistent success/error envelope; actionable error messages.
- Memory requirements: working memory, tool-result caching within a session, long-term memory for user preferences, and one integration pattern ("code-driven or background extraction").

## Definitions and terminology
- **Agent loop** — the basic loop of an agent that decides on and calls tools until it can answer.
- **Working memory (session)** vs **Long-Term Memory (preferences)** — as drawn in the architecture diagram.
- **Code-driven vs background extraction / LLM-driven memory** — two integration patterns for long-term memory (the page names them but does not define them).
- **Escalate to human** — `create_support_ticket` tool as escalation path.

## Evidence and examples
- Recommended tools: `search_knowledge_base(query, category)`, `get_customer_info(email)`, `check_order_status(order_id)`, `create_support_ticket(email, subject, description)`.
- Test scenarios: order tracking with follow-up ("I ordered a laptop last week" → "When will it arrive?"); knowledge base ("How do I reset my password?"); escalation ("This doesn't work, I need help"); preference ("I prefer email communication" → later "Contact me about this").
- Bonus challenges: tool consolidation, semantic enrichment, custom memory strategy, multiple memory patterns, advanced cache invalidation.
- Resources linked: MCP spec, Anthropic tool use guide (docs.anthropic.com/claude/docs/tool-use), Redis Agent Memory Server.

## Inconsistencies / open questions
- Note: this is a single-agent exercise (one agent + 4 tools), not a multi-agent design. Useful to the talk as the "single agent with tools" baseline before splitting into agents.
- [open question] The linked "Anthropic Tool Use Guide" URL (`docs.anthropic.com/claude/docs/tool-use`) is an old docs path; whether it still resolves was not checked.

## Images / diagrams

The page's architecture diagram is ASCII text, preserved verbatim under Raw excerpts (not an image).

### aitutorial-hands-on-exercise.web/images/logo-light-full.svg
- Provenance: `research/web/aitutorial-hands-on-exercise/assets/logo-light-full.svg` (alt "light logo"). Site logo, navigation chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### aitutorial-hands-on-exercise.web/images/logo-dark-full.svg
- Provenance: `research/web/aitutorial-hands-on-exercise/assets/logo-dark-full.svg` (alt "dark logo"). Site logo, navigation chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

## Raw / preserved excerpts

**Project Goal** — Build a customer support agent that demonstrates the three core concepts from this module:

> - **Agent basics** - Tool use with proper agent loop
> - **Well-designed tools** - Following MCP best practices
> - **Memory management** - Working memory for conversation + long-term for preferences

**Architecture** (verbatim ASCII from the page):

```
User Query
    |
    V
+-------------------------------------+
│ Customer Support Agent              │
│ - Maintains conversation context    │
│ - Remembers user preferences        │
│ - Uses tools intelligently          │
+-------------------------------------+
          |
          |--> [search_knowledge_base]
          |--> [get_customer_info]
          |--> [check_order_status]
          |--> [create_support_ticket]
          |
          V
    Working Memory (session)
          +
  Long-Term Memory (preferences)
```

**Project Requirements** (verbatim):

> **1. Agent Foundation** Must implement:
> - Basic agent loop with tool use
> - At least 3 tools from customer support domain
> - Proper error handling for tool failures
> - Graceful responses when no tool is needed
>
> **2. Tool Design (MCP Best Practices)** Each tool must have:
> - Clear, descriptive name (verb_noun_context format)
> - Comprehensive description (what, when to use, when NOT to use)
> - Simple parameter schema (3 or fewer parameters preferred)
> - Consistent response format (success/error envelope)
> - Graceful error handling with actionable messages
>
> Recommended tools:
> - `search_knowledge_base(query, category)` - Find help articles
> - `get_customer_info(email)` - Look up customer account
> - `check_order_status(order_id)` - Track order/delivery
> - `create_support_ticket(email, subject, description)` - Escalate to human
>
> **3. Memory Implementation** Must implement:
> - Working memory for conversation continuity
> - Tool result caching (avoid redundant calls within session)
> - Long-term memory for user preferences
> - Choose one integration pattern (code-driven or background extraction)
>
> Example preferences to track:
> - Communication style (formal/casual)
> - Preferred contact method (email/phone)
> - Product interests
> - Past issues and resolutions
>
> **4. Testing Requirements** Must demonstrate:
> - Multi-turn conversation with context retention
> - Tool selection accuracy (right tool for each query)
> - Memory retrieval (reference previous conversation)
> - Error handling (tool failure gracefully handled)
> - Preference learning and application
>
> Test scenarios:
> 1. **Order tracking:** "I ordered a laptop last week" → "When will it arrive?" (should remember order)
> 2. **Knowledge base:** "How do I reset my password?" (search articles)
> 3. **Escalation:** "This doesn't work, I need help" (create ticket)
> 4. **Preference:** "I prefer email communication" → later: "Contact me about this" (should use email)

**Bonus Challenges** — Choose one or more:

> - **Tool consolidation:** Combine related data fetches into single efficient tool
> - **Semantic enrichment:** Add contextual insights to tool responses
> - **Custom memory strategy:** Implement domain-specific extraction
> - **Multiple patterns:** Use both code-driven and LLM-driven memory
> - **Advanced caching:** Implement intelligent cache invalidation

Reference examples linked: Weather Agent (LLM + Tool) `/agents/intro#your-first-agent-simple-tool-use`; Weather MCP Server `/agents/model-context-protocol#from-hardcoded-tools-to-mcp`; Customer Support MCP Server `/agents/model-context-protocol#complete-example-customer-support-mcp-server`.
