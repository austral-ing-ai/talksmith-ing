---
source_file: mcp-intro/
source_type: web-capture
ingested_at: 2026-09-26
---

# What is the Model Context Protocol (MCP)? (docs, version 2026-07-28)

## Provenance
- Original location: web/mcp-intro/ (`page.md` used as text input; 4,053 chars, 15 headings — above the 400-char threshold, so no fallback to `original.html`; checked `original.html` for missed images: only the logos and `mcp-simple-diagram.png`)
- Format: html (web capture via talksmith:ingest; Mintlify docs site)
- URL: https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
- Fetched at: 2026-09-26T22:35:54Z (HTTP 200, 315,079 bytes). Captured 2026-09-26; the protocol/spec version in the URL and on the page is **2026-07-28** ("Version 2026-07-28 (latest)").
- Author / source (if known): Model Context Protocol project, official documentation ("Get started").
- Date of original (if known): not stated on the page.
- Companion architecture page: `mcp-architecture.web.md` (host / client / server, JSON-RPC, primitives, `tools/list` / `tools/call`, transports).

## Key claims
- Definition: "MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems."
- What it connects: "Using MCP, AI applications like Claude or ChatGPT can connect to data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks." (Calculators named explicitly as an example tool.)
- Analogy: "Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems."
- What MCP can enable (verbatim list): "Agents can access your Google Calendar and Notion, acting as a more personalized AI assistant." / "Claude Code can generate an entire web app using a Figma design." / "Enterprise chatbots can connect to multiple databases across an organization, empowering users to analyze data using chat." / "AI models can create 3D designs on Blender and print them out using a 3D printer."
- Why it matters: Developers — "reduces development time and complexity"; AI applications or agents — "access to an ecosystem of data sources, tools and apps"; End-users — "more capable AI applications or agents that can access user data and take actions on the user’s behalf when necessary."
- Ecosystem: "MCP is an open protocol supported across a wide range of clients and servers." Named supporters: Claude, ChatGPT, Visual Studio Code, Cursor, MCPJam — "making it easy to build once and integrate everywhere."

## Definitions and terminology
- **MCP** — "an open-source standard for connecting AI applications to external systems"; also "an open protocol".
- Three kinds of external systems: **data sources**, **tools**, **workflows** (which map onto the architecture page's resources, tools, prompts primitives — mapping is the librarian's reading, not stated on this page).
- "Build servers" = "expose your data and tools"; "Build clients" = "applications that connect to MCP servers"; "Build MCP Apps" = "interactive apps that run inside AI clients".

## Evidence and examples
- Diagram `mcp-simple-diagram.png` (see Images): AI applications on the left (Chat interface: Claude Desktop, LibreChat; IDEs and code editors: Claude Code, Goose; Other AI applications: 5ire, Superinterface) ↔ "MCP / Standardized protocol" ↔ data sources and tools on the right (Data and file systems: PostgreSQL, SQLite, GDrive; Development tools: Git, Sentry, etc.; Productivity tools: Slack, Google Maps, etc.), with "Bidirectional data flow" arrows on both sides. (Read by viewing the image during Phase 1 to verify it is content, not chrome; formal transcription is Phase 2.)

## Inconsistencies / open questions
- [open question] The page is marketing-level: no protocol details (roles, JSON-RPC, transports) — those live in `mcp-architecture.web.md`. Nothing to reconcile, but do not cite this page for mechanism claims.
- [open question] The "USB-C port" analogy is the project's own framing; whether it holds (MCP standardizes discovery/calls but the model still decides what to call) is an interpretive point for the presenter, not a factual defect.

## Images / diagrams
### `mcp-intro.web/images/mcp-simple-diagram.png`
- Provenance: copied from `web/mcp-intro/assets/mcp-simple-diagram.png` (source URL https://mintcdn.com/mcp/bEUxYpZqie0DsluH/images/mcp-simple-diagram.png), 3840x1500 px, the page's only content image (placed right after the USB-C analogy paragraph; empty alt text).
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

Discarded: `light.svg`, `dark.svg` — MCP wordmark logo (1338x195 viewBox), site chrome; dropped under the corpus rule for logos/icons.

## Raw / preserved excerpts

### What is the Model Context Protocol (MCP)? (full article body)
> MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems. Using MCP, AI applications like Claude or ChatGPT can connect to data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.
>
> [image: mcp-simple-diagram.png]
>
> **What can MCP enable?**
> - Agents can access your Google Calendar and Notion, acting as a more personalized AI assistant.
> - Claude Code can generate an entire web app using a Figma design.
> - Enterprise chatbots can connect to multiple databases across an organization, empowering users to analyze data using chat.
> - AI models can create 3D designs on Blender and print them out using a 3D printer.
>
> **Why does MCP matter?**
> Depending on where you sit in the ecosystem, MCP can have a range of benefits.
> - **Developers**: MCP reduces development time and complexity when building, or integrating with, an AI application or agent.
> - **AI applications or agents**: MCP gives them access to an ecosystem of data sources, tools and apps, which enhances their capabilities and improves the end-user experience.
> - **End-users**: MCP results in more capable AI applications or agents that can access user data and take actions on the user’s behalf when necessary.
>
> **Broad ecosystem support**
> MCP is an open protocol supported across a wide range of clients and servers. AI assistants like Claude (https://claude.com/docs/connectors/building) and ChatGPT (https://developers.openai.com/api/docs/mcp/), development tools like Visual Studio Code (https://code.visualstudio.com/docs/copilot/chat/mcp-servers), Cursor (https://cursor.com/docs/context/mcp), MCPJam (https://docs.mcpjam.com/getting-started), and many others all support MCP — making it easy to build once and integrate everywhere.
>
> **Start Building** — Build servers: "Create MCP servers to expose your data and tools" · Build clients: "Develop applications that connect to MCP servers" · Build MCP Apps: "Build interactive apps that run inside AI clients"
>
> **Learn more** — Architecture: "Learn the core concepts and architecture of MCP" · Security: "Understand the security considerations and best practices for MCP"
>
> **Community** — Contributing: "Learn how to get involved and contribute to MCP"
