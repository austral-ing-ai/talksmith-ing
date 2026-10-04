# Hands-On Exercise - AI Tutorial

_Source: <https://aitutorial.dev/agents/hands-on-exercise>_

> 

## Documentation Index

Fetch the complete documentation index at: [/llms.txt](/llms.txt)

Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)![light logo](https://mintcdn.com/digibee-1a4db0d2/qVB-_urhSn1RCBv0/logo/logo-light-full.svg?fit=max&auto=format&n=qVB-_urhSn1RCBv0&q=85&s=720536383dc8eb2a95e11611fc7839b4)![dark logo](https://mintcdn.com/digibee-1a4db0d2/qVB-_urhSn1RCBv0/logo/logo-dark-full.svg?fit=max&auto=format&n=qVB-_urhSn1RCBv0&q=85&s=dde82d875ffc50b174137cb594049e8e)[AI Tutorial home page](/)Search...⌘KSearch...NavigationAI AgentsHands-On ExerciseAI Agents

# Hands-On Exercise

Copy pageCopy page

Build an intelligent customer support agent

Copy pageCopy page

## [​](#reference-examples)Reference Examples

Before building your own agent, review the examples from earlier in this module: 

- [Weather Agent (LLM + Tool)](/agents/intro#your-first-agent-simple-tool-use) — basic agent with tool calling 
- [Weather MCP Server](/agents/model-context-protocol#from-hardcoded-tools-to-mcp) — same tool exposed via MCP 
- [Customer Support MCP Server](/agents/model-context-protocol#complete-example-customer-support-mcp-server) — production-style multi-tool server 

---

## [​](#project-goal)Project Goal

Build a customer support agent that demonstrates the three core concepts from this module: 

- ✅ **Agent basics** - Tool use with proper agent loop 
- ✅ **Well-designed tools** - Following MCP best practices 
- ✅ **Memory management** - Working memory for conversation + long-term for preferences 

## [​](#architecture)Architecture

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

## [​](#project-requirements)Project Requirements

**1. Agent Foundation** Must implement: 

- Basic agent loop with tool use 
- At least 3 tools from customer support domain 
- Proper error handling for tool failures 
- Graceful responses when no tool is needed 
**2. Tool Design (MCP Best Practices)** Each tool must have: 

- Clear, descriptive name (verb_noun_context format) 
- Comprehensive description (what, when to use, when NOT to use) 
- Simple parameter schema (3 or fewer parameters preferred) 
- Consistent response format (success/error envelope) 
- Graceful error handling with actionable messages 
Recommended tools: 

- `search_knowledge_base(query, category)` - Find help articles 
- `get_customer_info(email)` - Look up customer account 
- `check_order_status(order_id)` - Track order/delivery 
- `create_support_ticket(email, subject, description)` - Escalate to human 
**3. Memory Implementation** Must implement: 

- Working memory for conversation continuity 
- Tool result caching (avoid redundant calls within session) 
- Long-term memory for user preferences 
- Choose one integration pattern (code-driven or background extraction) 
Example preferences to track: 

- Communication style (formal/casual) 
- Preferred contact method (email/phone) 
- Product interests 
- Past issues and resolutions 
**4. Testing Requirements** Must demonstrate: 

- Multi-turn conversation with context retention 
- Tool selection accuracy (right tool for each query) 
- Memory retrieval (reference previous conversation) 
- Error handling (tool failure gracefully handled) 
- Preference learning and application 
Test scenarios: 

1. **Order tracking:** “I ordered a laptop last week” → “When will it arrive?” (should remember order) 
2. **Knowledge base:** “How do I reset my password?” (search articles) 
3. **Escalation:** “This doesn’t work, I need help” (create ticket) 
4. **Preference:** “I prefer email communication” → later: “Contact me about this” (should use email) 

## [​](#bonus-challenges)Bonus Challenges

Choose one or more: 

- **Tool consolidation:** Combine related data fetches into single efficient tool 
- **Semantic enrichment:** Add contextual insights to tool responses 
- **Custom memory strategy:** Implement domain-specific extraction 
- **Multiple patterns:** Use both code-driven and LLM-driven memory 
- **Advanced caching:** Implement intelligent cache invalidation 

### [​](#resources)Resources

- [MCP Specification](https://modelcontextprotocol.io/) 
- [Anthropic Tool Use Guide](https://docs.anthropic.com/claude/docs/tool-use) 
- [Redis Agent Memory Server](https://redis.github.io/agent-memory-server/) 

---

Was this page helpful?

YesNo⌘I
