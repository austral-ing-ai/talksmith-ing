# Tool Selection & Optimization - AI Tutorial

_Source: <https://aitutorial.dev/agents/tool-selection-and-optimization>_

> 

## Documentation Index

Fetch the complete documentation index at: [/llms.txt](/llms.txt)

Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)![light logo](https://mintcdn.com/digibee-1a4db0d2/qVB-_urhSn1RCBv0/logo/logo-light-full.svg?fit=max&auto=format&n=qVB-_urhSn1RCBv0&q=85&s=720536383dc8eb2a95e11611fc7839b4)![dark logo](https://mintcdn.com/digibee-1a4db0d2/qVB-_urhSn1RCBv0/logo/logo-dark-full.svg?fit=max&auto=format&n=qVB-_urhSn1RCBv0&q=85&s=dde82d875ffc50b174137cb594049e8e)[AI Tutorial home page](/)Search...⌘KSearch...NavigationAI AgentsTool Selection & OptimizationAI Agents

# Tool Selection & Optimization

Copy pageCopy page

Hierarchical routing, context-based filtering, and analytics to improve tool selection accuracy

Copy pageCopy pageAgent accuracy drops from 92% to 58% as tool count grows from 5 to 20+. This page covers hierarchical routing, context-based filtering, and tool analytics. 

## [​](#the-tool-selection-problem)The Tool Selection Problem

**Scenario:** You give your agent 20 tools. The agent uses wrong ones constantly. **Research shows:** Agent accuracy decreases with tool count: 

- 1-5 tools: 92% correct selection 
- 6-10 tools: 84% correct selection 
- 11-20 tools: 71% correct selection 
- 20+ tools: 58% correct selection 
**Why:** LLMs pattern-match descriptions. Large option spaces overwhelm them. 

## [​](#challenge-1-too-many-tools)Challenge 1: Too Many Tools

Your customer support agent handles customers, products, orders, and tickets. The naive approach: register all 20 CRUD tools in a flat list. The LLM sees all 20 at once and picks the wrong one 42% of the time. **Anti-pattern:** All 20 tools in a flat list. Pseudocode

```
// Agent sees all 20 tools at once → 58% accuracy
const tools = [
    searchCustomers, searchProducts, searchOrders, searchTickets,
    getCustomer, getProduct, getOrder, getTicket,
    updateCustomer, updateProduct, updateOrder, updateTicket,
    createCustomer, createProduct, createOrder, createTicket,
    deleteCustomer, deleteProduct, deleteOrder, deleteTicket,
];

```

### [​](#solution-1-hierarchical-routing)Solution 1: Hierarchical Routing

Instead of 20 flat tools, give the agent 1 routing tool. It picks the domain + action, then a second step calls the specific tool. Pseudocode

```
// Agent sees 1 tool instead of 20 → 90%+ accuracy
const routeTool = tool(async ({ domain, action }) => {
    const mapping = {
        "customers,search": searchCustomers,
        "customers,get": getCustomer,
        "orders,search": searchOrders,
        // ... 20 mappings
    };
    return mapping[`${domain},${action}`];
}, {
    name: "route_to_domain",
    schema: z.object({
        domain: z.enum(["customers", "products", "orders", "tickets"]),
        action: z.enum(["search", "get", "update", "create", "delete"]),
    })
});

```

### [​](#solution-2-context-based-tool-groups)Solution 2: Context-Based Tool Groups

A support conversation has phases: greeting (authentication), diagnosis (searching), resolution (ticketing). During diagnosis, the agent doesn’t need ticket creation tools. During resolution, it doesn’t need search. Show only the tools relevant to the current phase — the agent sees 2-4 instead of 20. Pseudocode

```
function getToolsForPhase(phase: string) {
    const groups = {
        greeting:  [authenticateCustomer],
        diagnosis: [searchKnowledgeBase, checkSystemStatus],
        resolution: [createTicket, scheduleCallback],
    };
    return groups[phase];  // Agent sees 2-3 tools, not 20
}

```

## [​](#challenge-2-overlapping-functionality)Challenge 2: Overlapping Functionality

Your e-commerce agent has three product tools: `search_products`, `find_products`, and `product_lookup`. They all sound the same — the LLM picks randomly or calls all three. Even with just 3 tools, overlapping descriptions destroy accuracy. 

### [​](#solution-clear-differentiation)Solution: Clear Differentiation

Each tool has a distinct purpose with “Use when” / “Do NOT use” guidance: Pseudocode

```
// Instead of 3 overlapping tools, 3 distinct tools:

tool("search_products_by_text", {
    description: `Full-text search.
    Use when: customer describes product ("wireless mouse").
    Do NOT use when: you have exact SKU.`,
    schema: { query: z.string() }
});

tool("get_product_by_sku", {
    description: `Exact SKU lookup.
    Use when: customer provides SKU ("PROD-001").
    Do NOT use for search.`,
    schema: { sku: z.string() }
});

tool("filter_products_by_attributes", {
    description: `Structured filter.
    Use when: customer specifies category, price, brand.
    Do NOT use for text search.`,
    schema: { category: z.string().optional(), priceMax: z.number().optional() }
});

```

The agent picks the right tool for each query: 

- “wireless mouse” → `search_products_by_text` 
- “PROD-001” → `get_product_by_sku` 
- “mice under $20” → `filter_products_by_attributes` 

## [​](#advanced-tool-usage-analytics)Advanced: Tool Usage Analytics

Track every tool call to find unused tools, high-failure tools, and latency bottlenecks: Run this in production to get recommendations like: 

- “Remove unused tool: `legacy_search`” 
- “`flaky_tool` fails 40% — review error handling” 
- “`slow_api` averages 3000ms — consider caching” 

Was this page helpful?

YesNo⌘I
