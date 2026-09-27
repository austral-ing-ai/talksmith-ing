---
source_file: anthropic-web-search-tool
source_type: web-capture
ingested_at: 2026-09-26
---

# Web search tool (Anthropic, Claude Platform Docs)

## Provenance
- Original location: web/anthropic-web-search-tool/ (text from `page.md`; `page.md` is 18022 chars with headings, so no `original.html` fallback was needed)
- Format: html (web capture via talksmith:ingest)
- URL: https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool
- Captured at: 2026-09-26T22:26:07Z (HTTP 200, 668436 bytes)
- Page title: Web search tool - Claude Platform Docs
- Author / source (if known): Anthropic. This is **vendor documentation** (Anthropic's own product docs for the Claude API, section "Agents and tools > Tool use"), not an independent or peer-reviewed source. It describes Anthropic's API as of the capture date, 2026-09-26.
- Date of original (if known): Not printed on the page. Treat as the live docs state on 2026-09-26.
- Images: none (`metadata.yaml` lists `assets: []`).
- Related record: `anthropic-tool-use-overview.web.md` (same capture batch), which gives the client-tool vs server-tool framing. Web search is a **server tool** there.

## Key claims
- "The web search tool gives Claude direct access to real-time web content, allowing it to answer questions with up-to-date information beyond its knowledge cutoff. The response includes citations for sources drawn from search results."
- **How web search works (the loop, verbatim steps):**
  1. "Claude determines when to search based on the prompt."
  2. "The API runs the searches and provides Claude with the results. This process can repeat multiple times throughout a single request."
  3. "At the end of its turn, Claude provides a final response with cited sources."
  In short: Claude decides when to search, the API (Anthropic's side) executes the searches, the search-and-read cycle can repeat several times inside one request, and the turn ends with a final answer carrying citations. The caller writes no execution code, which makes this a server tool.
- When Claude searches: "when the request depends on information that is current, changing, or outside its training data". Examples: recent events/news, current prices/rates/scores/statistics, organizations/people/products that might have changed, explicit requests to search.
- When Claude answers directly without searching: "when the request draws on stable knowledge". Examples: established facts, math, science fundamentals, coding concepts, creative writing, analysis of content already in the conversation, conversational turns.
- Triggering can be steered via the system prompt. As a hard cap, "use `max_uses` to cap the number of searches for each request."
- Three versions: `web_search_20250305` (basic), `web_search_20260209` (adds dynamic filtering), `web_search_20260318` (adds response inclusion control for agentic workflows).
- **Dynamic filtering**: "With basic web search, every search result is loaded into Claude's context window, and much of that content can be irrelevant". With `web_search_20260209`+, "Claude instead writes and runs code that filters the results first, so only relevant content reaches the context window. This reduces token use on search-heavy requests." It runs web search from inside code execution (`allowed_callers` defaults to `["code_execution_20260120"]`), and the API provisions that code execution automatically at no extra charge beyond tokens. It is available with "Claude 4.6 and later models and Claude Mythos Preview".
- `max_uses`: "Simple factual queries typically use 1–3 searches; comparative or multientity research can use 10 or more." Exceeding it yields a `max_uses_exceeded` error in the result.
- Domain filtering: `allowed_domains` or `blocked_domains`, not both (sending both returns a 400). Localization is via `user_location`.
- Citations: "Citations are always enabled for web search". The `cited_text` field holds "Up to 150 characters". The citation fields `cited_text`, `title`, `url` "do not count toward input or output token usage."
- Multi-turn: "send the assistant's content blocks back exactly as you received them, including each result's `encrypted_content`". Missing or modified content gives a 400.
- Errors return HTTP 200 with a `web_search_tool_result_error` in the body. An empty result list is not an error.
- `pause_turn`: "The API can pause a long-running search turn". To continue, send the paused message back unchanged. If web search is called in the same parallel group as a client tool, the API returns `stop_reason: "tool_use"` and runs the search only on the next request.
- Pricing: "**$10 per 1,000 searches**, plus standard token costs for search-generated content". Results count as input tokens "in search iterations executed during a single turn and in subsequent conversation turns". "Each web search counts as one use, regardless of the number of results returned. If an error occurs during web search, the web search will not be billed."

## Definitions and terminology
- **Web search tool** (`name: "web_search"`): an Anthropic server tool giving Claude real-time web content with cited sources.
- **`server_tool_use` block**: the content block recording Claude's search call (e.g. `input.query`). The id prefix is `srvtoolu_`, compared with `toolu_` for client `tool_use`.
- **`web_search_tool_result`**: the block with results (`web_search_result` items: `url`, `title`, `page_age`, `encrypted_content`) or an error object.
- **`web_search_result_location`**: citation object (`url`, `title`, `encrypted_index`, `cited_text`).
- **Dynamic filtering**: Claude writes and runs code that filters search results before they enter the context window (`web_search_20260209`+).
- **`allowed_callers`**: whether web search is called `"direct"` or from code execution (`"code_execution_20260120"`, the default on 20260209+).
- **`response_inclusion`** (`web_search_20260318`+): `"excluded"` drops nested `server_tool_use`/result pairs consumed by a completed code execution call from the response. The default is `"full"`.
- **`max_uses`**: per-request cap on number of searches.
- **`pause_turn`**: stop reason for a paused long-running server-side turn.
- **`usage.server_tool_use.web_search_requests`**: billed count of searches.

## Evidence and examples
- **Basic request (Python)**: `tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}]`, user "What's the weather in NYC?", model `claude-opus-5-5`.
- **Dynamic filtering request (Python)**: `tools=[{"type": "web_search_20260318", "name": "web_search"}]`, user "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio.", `max_tokens=4096`.
- **Tool definition JSON**: `max_uses: 5`, `allowed_domains: ["example.com", "trusteddomain.org"]`, `blocked_domains: ["untrustedsource.com"]`, `user_location` {type "approximate", city "San Francisco", region "California", country "US", timezone "America/Los_Angeles"}.
- **Example response, annotated in 4 steps**: (1) text "I'll search for when Claude Shannon was born." (2) `server_tool_use` id `srvtoolu_01WYG3ziw53XMcoyKL4XcZmE`, query "claude shannon birth date". (3) `web_search_tool_result` with a Wikipedia result (`page_age` "April 30, 2025", `encrypted_content`). (4) text "Claude Shannon was born on April 30, 1916, in Petoskey, Michigan" with a `web_search_result_location` citation whose `cited_text` begins "Claude Elwood Shannon (April 30, 1916 – February 24, 2001) was an American mathematician…". Usage: input 6039, output 931, `web_search_requests: 1`, `stop_reason: "end_turn"`. All four steps sit in **one** assistant response, with no caller round trip.
- **Error codes**: `too_many_requests`, `invalid_tool_input`, `max_uses_exceeded`, `query_too_long`, `request_too_large`, `unavailable`.
- **Streaming**: `content_block_start` for `server_tool_use`, `input_json_delta` with the query (`"latest quantum computing breakthroughs 2025"`), a pause while the search executes, then `web_search_tool_result`.
- **Usage/pricing JSON**: `input_tokens` 105, `output_tokens` 6039, cache read 7123, cache creation 7345, `web_search_requests` 1. $10 per 1,000 searches.
- **Batches**: web search is allowed in the Messages Batches API at the same price, and throttled per organization.

## Inconsistencies / open questions
- [open question] **Other vendors are out of scope for this record.** Other providers (e.g. OpenAI) have analogous hosted web-search tools that the provider executes and that return cited results. This record does not describe them, and nothing here should be read as a claim about how they work, what they cost, or whether they loop within one request. A cross-vendor slide would need those vendors' docs.
- [verified] This is vendor documentation (Anthropic about its own API). Statements such as "when Claude searches" describe intended/typical behaviour under default prompting, and the page itself says triggering "is steerable". Check: read in `page.md` "When Claude searches".
- [verified] "Server tool, no caller handling" has two stated exceptions on this page: (a) `pause_turn`, where the caller must resend the paused message to continue, and (b) a mixed parallel call with a client tool, where the API returns `stop_reason: "tool_use"` and runs the search on the next request. Check: "`pause_turn` stop reason" section of `page.md`.
- [verified] Version dates in the sample code are mixed. The intro says examples use `web_search_20250305` (basic) and `web_search_20260318` (dynamic filtering), while the overview page's minimal example uses `web_search_20260209`. All three are listed as available versions, so this is not a contradiction. Check: compared the version list with the code samples in both captures.
- [verified] Example data is illustrative, not live. The streaming example query says "2025", `page_age` "April 30, 2025", and the usage JSON's `input_tokens` 105 / `output_tokens` 6039 in the pricing section vs 6039 / 931 in the response example use swapped-looking numbers. These are sample payloads, not measurements. Check: compared the two usage blocks in `page.md`.
- [open question] "Claude Mythos Preview" (linked to anthropic.com/glasswing) is named as supporting dynamic filtering. It is not in the overview page's model token table, and its availability or status was not checked here. It is not flagged as invented, only as unverified in this record.
- [verified] Extraction artifacts: code tabs ("cURLCLIPythonTypeScriptC#GoJavaPHPRuby") survive as a text line, and only the Python sample of each tab set was captured. There is a stray double backtick in "also accept ``[response_inclusion](…)". Page chrome ("Copy page", "Was this page helpful?", "Ask Docs") is present. A lone space line precedes the pricing sentence (probably a stripped callout).

## Images / diagrams
None. The capture carried no image assets (`assets: []`).

## Raw / preserved excerpts
> "The web search tool gives Claude direct access to real-time web content, allowing it to answer questions with up-to-date information beyond its knowledge cutoff. The response includes citations for sources drawn from search results."
— Intro

> "When you add the web search tool to your API request:
> 1. Claude determines when to search based on the prompt.
> 2. The API runs the searches and provides Claude with the results. This process can repeat multiple times throughout a single request.
> 3. At the end of its turn, Claude provides a final response with cited sources."
— How web search works

> "Claude searches when the request depends on information that is current, changing, or outside its training data"
— When Claude searches

> "Claude answers directly without searching when the request draws on stable knowledge"
— When Claude searches

> "Triggering is steerable through your system prompt: you can encourage Claude to search more readily or to prefer answering directly. For a hard constraint, use `max_uses` to cap the number of searches for each request."
— When Claude searches

> "With basic web search, every search result is loaded into Claude's context window, and much of that content can be irrelevant to the request. With `web_search_20260209` or later, Claude instead writes and runs code that filters the results first, so only relevant content reaches the context window. This reduces token use on search-heavy requests."
— Dynamic filtering

> "Simple factual queries typically use 1–3 searches; comparative or multientity research can use 10 or more."
— Max uses

> "To continue a conversation that contains search results, send the assistant's content blocks back exactly as you received them, including each result's `encrypted_content`. The API decrypts that content on later turns to restore the search results in Claude's context."
— Search results

> "If Claude calls web search and one of your client tools in the same group of parallel tool calls, the API returns `stop_reason: "tool_use"` instead and does not run the search yet. To continue, return the client tool results, and the API runs the search in the next request."
— `pause_turn` stop reason

> "Web search is available on the Claude API for **$10 per 1,000 searches**, plus standard token costs for search-generated content. Web search results retrieved throughout a conversation are counted as input tokens, in search iterations executed during a single turn and in subsequent conversation turns."
— Usage and pricing

### Full extracted text (verbatim)
Complete `page.md` as captured, verbatim.

~~~~~text
# Web search tool - Claude Platform Docs

_Source: <https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool>_

[Claude Platform Docs](/docs/en/home)[API reference](/docs/en/api/overview)English[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fagents-and-tools%2Ftool-use%2Fweb-search-tool)[Messages](/docs/en/intro)Tools

# Web search tool

Copy page

Give Claude access to current web content with cited sources, optional dynamic filtering, and domain controls.

Copy page 

The web search tool gives Claude direct access to real-time web content, allowing it to answer questions with up-to-date information beyond its knowledge cutoff. The response includes citations for sources drawn from search results.

With `web_search_20260209` and later versions, Claude can write and run code that filters the search results before they reach the context window (**dynamic filtering**), keeping only relevant information. Dynamic filtering is available with Claude 4.6 and later models and [Claude Mythos Preview](https://anthropic.com/glasswing).

Three versions of the web search tool are available:

- `web_search_20250305`: basic web search 
- `web_search_20260209`: adds [dynamic filtering](#dynamic-filtering) 
- `web_search_20260318`: adds [response inclusion](#response-inclusion) control for agentic workflows 

The examples on this page use `web_search_20250305` for basic search and `web_search_20260318` for dynamic filtering.

For web search's Zero Data Retention eligibility and the related `allowed_callers` configuration, see [Server tools](/docs/en/agents-and-tools/tool-use/server-tools#zdr-and-allowed-callers).

For model support, see the [Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference).

## How web search works

When you add the web search tool to your API request:

1. Claude determines when to search based on the prompt. 
2. The API runs the searches and provides Claude with the results. This process can repeat multiple times throughout a single request. 
3. At the end of its turn, Claude provides a final response with cited sources. 

### When Claude searches

Claude searches when the request depends on information that is current, changing, or outside its training data:

- Recent events, news, or announcements 
- Current prices, rates, scores, or statistics 
- Information about specific organizations, people, or products that might have changed 
- Explicit requests to search or look something up 

Claude answers directly without searching when the request draws on stable knowledge:

- Established facts, math, science fundamentals, or coding concepts 
- Creative writing or brainstorming 
- Analysis of content already provided in the conversation 
- Conversational turns and greetings 

Triggering is steerable through your system prompt: you can encourage Claude to search more readily or to prefer answering directly. For a hard constraint, use `max_uses` to cap the number of searches for each request.

### Dynamic filtering

With basic web search, every search result is loaded into Claude's context window, and much of that content can be irrelevant to the request. With `web_search_20260209` or later, Claude instead writes and runs code that filters the results first, so only relevant content reaches the context window. This reduces token use on search-heavy requests.

Dynamic filtering runs web search from inside [code execution](/docs/en/agents-and-tools/tool-use/code-execution-tool): on `web_search_20260209` and later, the tool's `allowed_callers` field defaults to `["code_execution_20260120"]`, and when dynamic filtering runs, the API provisions the code execution it needs for the request automatically. You don't need to add the code execution tool to `tools` yourself. There are no additional charges for code execution calls made this way beyond the standard token costs.

To call web search directly, without dynamic filtering, set `allowed_callers: ["direct"]`. Models that don't support programmatic tool calling require this setting. Without it, the API returns a 400 error that tells you to set it.

The following examples use `web_search_20260318`:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio.",
        }
    ],
    tools=[{"type": "web_search_20260318", "name": "web_search"}],
)
print(response)
```

## How to use web search

These organization-level settings in the Claude Console apply to Messages API requests only. [Claude Managed Agents](/docs/en/managed-agents/overview) sessions use only the per-tool `allowed_domains` and `blocked_domains` lists on the agent toolset; see [Restrict web search and web fetch domains](/docs/en/managed-agents/tools#restrict-web-search-and-web-fetch-domains).

Provide the web search tool in your API request:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "What's the weather in NYC?"}],
    tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}],
)
print(response)
```

## Tool definition

The web search tool supports the following parameters:

JSON

```
{
  "type": "web_search_20250305",
  "name": "web_search",

  // Optional: Limit the number of searches per request
  "max_uses": 5,

  // Optional: Only include results from these domains.
  // Use allowed_domains or blocked_domains, not both.
  "allowed_domains": ["example.com", "trusteddomain.org"],

  // Optional: Never include results from these domains
  "blocked_domains": ["untrustedsource.com"],

  // Optional: Localize search results
  "user_location": {
    "type": "approximate",
    "city": "San Francisco",
    "region": "California",
    "country": "US",
    "timezone": "America/Los_Angeles"
  }
}
```

All web search tool versions accept `allowed_callers`, which controls whether Claude calls web search directly or from code execution through [dynamic filtering](#dynamic-filtering). On `web_search_20260209` and later it defaults to `["code_execution_20260120"]` instead of `["direct"]`. See [Server tools](/docs/en/agents-and-tools/tool-use/server-tools#zdr-and-allowed-callers) for how to configure it. `web_search_20260318` and later also accept ``[response_inclusion](#response-inclusion).

### Max uses

The `max_uses` parameter limits the number of searches performed. If Claude attempts more searches than allowed, the `web_search_tool_result` is an error with the `max_uses_exceeded` error code.

Simple factual queries typically use 1–3 searches; comparative or multientity research can use 10 or more. For guidance on choosing a value, see [Server tools](/docs/en/agents-and-tools/tool-use/server-tools).

### Domain filtering

Provide `allowed_domains` or `blocked_domains`, not both. If a request includes both, the API returns a 400 error. Entries are bare domains with an optional path, for example `example.com` or `example.com/blog`, without a scheme.

For the full domain filtering rules, see [Domain filtering](/docs/en/agents-and-tools/tool-use/server-tools#domain-filtering) in the Server tools guide.

On [Claude Managed Agents](/docs/en/managed-agents/overview), set these fields on the `web_search` entry of the agent toolset; see [Restrict web search and web fetch domains](/docs/en/managed-agents/tools#restrict-web-search-and-web-fetch-domains).

### Localization

The `user_location` parameter allows you to localize search results based on a user's location. Provide at least one of `city`, `region`, `country`, or `timezone`.

- `type`: The type of location (must be `approximate`) 
- `city`: The city name 
- `region`: The region or state 
- `country`: The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. The API rejects unsupported country codes with a 400 error. 
- `timezone`: The [IANA timezone ID](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). 

On Claude Managed Agents, the `web_search` entry of the agent toolset accepts a `user_location` object with the same fields. The API rejects an unsupported `country` code with a 400 error when you create or update the agent, or when you create or update a session that supplies the setting. See [Restrict web search and web fetch domains](/docs/en/managed-agents/tools#restrict-web-search-and-web-fetch-domains).

### Response inclusion

The `response_inclusion` parameter controls how search result blocks appear in the API response when the result was consumed by a completed [code execution](/docs/en/agents-and-tools/tool-use/code-execution-tool) call in the same turn. Set `"response_inclusion": "excluded"` to drop those nested `server_tool_use` and result block pairs entirely from the response, reducing output token costs for agentic workflows that don't need to echo raw search content back to the client. The default is `"full"`. Results from direct calls, or from code execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

JSON

```
{
  "tools": [
    {
      "type": "web_search_20260318",
      "name": "web_search",
      "response_inclusion": "excluded"
    }
  ]
}
```

## Response

Here's an example response structure:

Output

```
{
  "role": "assistant",
  "content": [
    // 1. Claude's decision to search
    {
      "type": "text",
      "text": "I'll search for when Claude Shannon was born."
    },
    // 2. The search query used
    {
      "type": "server_tool_use",
      "id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
      "name": "web_search",
      "input": {
        "query": "claude shannon birth date"
      }
    },
    // 3. Search results
    {
      "type": "web_search_tool_result",
      "tool_use_id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
      "content": [
        {
          "type": "web_search_result",
          "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
          "title": "Claude Shannon - Wikipedia",
          "encrypted_content": "EqgfCioIARgBIiQ3YTAwMjY1Mi1mZjM5LTQ1NGUtODgxNC1kNjNjNTk1ZWI3Y...",
          "page_age": "April 30, 2025"
        }
      ]
    },
    {
      "text": "Based on the search results, ",
      "type": "text"
    },
    // 4. Claude's response with citations
    {
      "text": "Claude Shannon was born on April 30, 1916, in Petoskey, Michigan",
      "type": "text",
      "citations": [
        {
          "type": "web_search_result_location",
          "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
          "title": "Claude Shannon - Wikipedia",
          "encrypted_index": "Eo8BCioIAhgBIiQyYjQ0OWJmZi1lNm..",
          "cited_text": "Claude Elwood Shannon (April 30, 1916 – February 24, 2001) was an American mathematician, electrical engineer, computer scientist, cryptographer and i..."
        }
      ]
    }
  ],
  "id": "msg_a930390d3a",
  "usage": {
    "input_tokens": 6039,
    "output_tokens": 931,
    "server_tool_use": {
      "web_search_requests": 1
    }
  },
  "stop_reason": "end_turn"
}
```

This example shows a direct search. When a search runs through [dynamic filtering](#dynamic-filtering), the response also contains the [code execution tool's](/docs/en/agents-and-tools/tool-use/code-execution-tool) result blocks, and each nested `server_tool_use` and `web_search_tool_result` pair carries a `caller` field identifying the code execution call that made it.

### Search results

Search results include:

- `url`: The URL of the source page 
- `title`: The title of the source page 
- `page_age`: When the site was last updated 
- `encrypted_content`: Encrypted content that you must pass back in multi-turn conversations 

To continue a conversation that contains search results, send the assistant's content blocks back exactly as you received them, including each result's `encrypted_content`. The API decrypts that content on later turns to restore the search results in Claude's context. If `encrypted_content` is missing or modified, the request fails with a 400 validation error.

### Citations

Citations are always enabled for web search, and each `web_search_result_location` includes:

- `url`: The URL of the cited source 
- `title`: The title of the cited source 
- `encrypted_index`: A reference that must be passed back for multi-turn conversations 
- `cited_text`: Up to 150 characters of the cited content 

The web search citation fields `cited_text`, `title`, and `url` do not count toward input or output token usage.

### Errors

When the web search tool encounters an error (such as hitting rate limits), the Claude API still returns a 200 (success) response. The error is represented within the response body using the following structure:

Output

```
{
  "type": "web_search_tool_result",
  "tool_use_id": "srvtoolu_a93jad",
  "content": {
    "type": "web_search_tool_result_error",
    "error_code": "max_uses_exceeded"
  }
}
```

On an error, `content` is a single error object rather than a list of result blocks. A search that succeeds but matches no results returns an empty `content` list, not an error.

These are the possible error codes:

- `too_many_requests`: Rate limit exceeded 
- `invalid_tool_input`: Invalid search query parameter 
- `max_uses_exceeded`: Maximum web search tool uses exceeded 
- `query_too_long`: Query exceeds maximum length 
- `request_too_large`: The search request is too large, typically because of a long domain filter list 
- `unavailable`: An internal error occurred 

### `pause_turn` stop reason

The API can pause a long-running search turn and return `stop_reason: "pause_turn"`. To continue, send the paused assistant message back unchanged in a new request.

If Claude calls web search and one of your client tools in the same group of parallel tool calls, the API returns `stop_reason: "tool_use"` instead and does not run the search yet. To continue, return the client tool results, and the API runs the search in the next request. See [Mixing server tools and client tools in one turn](/docs/en/agents-and-tools/tool-use/server-tools#mixing-server-tools-and-client-tools-in-one-turn).

For the server-side loop and `pause_turn` handling, see [The server-side loop and pause_turn](/docs/en/agents-and-tools/tool-use/server-tools#the-server-side-loop-and-pause-turn) in the Server tools guide.

## Prompt caching

To cache tool definitions across turns, see [Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching).

## Streaming

With streaming enabled, you'll receive search events as part of the stream. There will be a pause while the search runs:

Output

```
event: message_start
data: {"type": "message_start", "message": {"id": "msg_abc123", "type": "message"}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}

// Claude's decision to search

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "web_search"}}

// Search query streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"query\":\"latest quantum computing breakthroughs 2025\"}"}}

// Pause while search executes

// Search results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "web_search_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": [{"type": "web_search_result", "title": "Quantum Computing Breakthroughs in 2025", "url": "https://example.com"}]}}

// Claude's response with citations (omitted in this example)
```

## Batch requests

You can include the web search tool in the [Messages Batches API](/docs/en/build-with-claude/batch-processing). Web search tool calls through the Messages Batches API are priced the same as those in regular Messages API requests.

To protect shared capacity, the Batches API throttles web search requests per organization, so large batches with many searches might take longer to complete. You can see your organization's web search rate limit on the [Rate limits](/settings/limits) page in the Claude Console. To request a higher limit, contact sales from that page.

## Usage and pricing

Web search usage is charged in addition to token usage:

```
{
  "usage": {
    "input_tokens": 105,
    "output_tokens": 6039,
    "cache_read_input_tokens": 7123,
    "cache_creation_input_tokens": 7345,
    "server_tool_use": {
      "web_search_requests": 1
    }
  }
}
```

 

Web search is available on the Claude API for **$10 per 1,000 searches**, plus standard token costs for search-generated content. Web search results retrieved throughout a conversation are counted as input tokens, in search iterations executed during a single turn and in subsequent conversation turns.

Each web search counts as one use, regardless of the number of results returned. If an error occurs during web search, the web search will not be billed.

## Next steps

[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)

Fetch and read content from specific URLs to augment Claude's context with live web content.

[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)

Work with Anthropic-executed tools: server_tool_use blocks, pause_turn continuation, and domain filtering.

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)

Directory of Anthropic-provided tools and reference for optional tool definition properties.

Was this page helpful?

Ask Docs

~~~~~
