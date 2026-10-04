---
source_file: mcp-spec/
source_type: web-capture
ingested_at: 2026-10-04
---

# What is the Model Context Protocol (MCP)? - Model Context Protocol

## Provenance
- Original location: research/web/mcp-spec/ (page.md; metadata.yaml; assets/)
- Format: html (Mintlify docs page captured via talksmith:ingest; page.md used as text input — 3869 bytes, 12 headings; short but structured, and original.html holds the same intro page, so no fallback was needed)
- URL: https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro
- Fetched at: 2026-08-14T16:56:51Z (HTTP 200, 274725 bytes original.html)
- Author / source (if known): Model Context Protocol project — official documentation site (modelcontextprotocol.io). Site nav lists: Documentation, Specification (`/specification/2026-07-28`), Extensions, Registry, SEPs, Community.
- Date of original (if known): documentation version selector shows "Version 2026-07-28 (latest)" at capture time.
- Note: despite the folder name `mcp-spec`, the capture is the **"Get started → intro"** documentation page, not the protocol specification text.

## Key claims
- "MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems."
- AI applications "like Claude or ChatGPT" can connect via MCP to data sources (local files, databases), tools (search engines, calculators) and workflows (specialized prompts).
- Analogy: "Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems."
- What MCP enables (examples): agents accessing Google Calendar and Notion; Claude Code generating a web app from a Figma design; enterprise chatbots connecting to multiple databases; AI models creating 3D designs in Blender and printing them.
- Benefits by role: developers (less development time and complexity), AI applications/agents (access to an ecosystem of data sources, tools, apps), end-users (more capable AI acting on their behalf).
- "MCP is an open protocol supported across a wide range of clients and servers" — Claude, ChatGPT, Visual Studio Code, Cursor, MCPJam — "making it easy to build once and integrate everywhere".
- Build paths: servers (expose data and tools), clients (connect to servers), MCP Apps (interactive apps that run inside AI clients).

## Definitions and terminology
- **MCP (Model Context Protocol)**: open-source standard for connecting AI applications to external systems.
- **MCP server**: exposes data and tools.
- **MCP client**: application that connects to MCP servers.
- **MCP Apps**: interactive apps that run inside AI clients.
- **SEPs**: listed in site navigation (not defined on this page).

## Evidence and examples
- Four illustrative use cases (Calendar/Notion, Figma → web app with Claude Code, enterprise multi-DB chatbots, Blender + 3D printer). No quantitative evidence on this page.

## Inconsistencies / open questions
- [verified] The capture does not contain the MCP specification itself (no message types, transports, primitives such as tools/resources/prompts, or lifecycle) — checked page.md and its headings. Slides needing protocol mechanics need another source (e.g. the `/specification/2026-07-28` page).
- [open question] The "Version 2026-07-28 (latest)" label reflects the site at capture time (2026-08-14); whether a newer version exists by the talk date is unchecked — the site's version selector would settle it.
- [open question] The ecosystem-support list is self-reported by the MCP project; each client's support level was not verified.

## Images / diagrams

### mcp-spec.web/images/mcp-simple-diagram.png
- Provenance: research/web/mcp-spec/assets/mcp-simple-diagram.png ← https://mintcdn.com/mcp/bEUxYpZqie0DsluH/images/mcp-simple-diagram.png (no alt); 3840x1500 PNG. Placed right after the USB-C analogy paragraph — the page's only content diagram.
- Depiction: Clean three-column architecture diagram. Centre: a light-blue box "MCP — Standardized protocol". Left column, captioned "AI applications": three boxes — "Chat interface: Claude Desktop, LibreChat", "IDEs and code editors: Claude Code, Goose", "Other AI applications: 5ire, Superinterface". Right column, captioned "Data sources and tools": "Data and file systems: PostgreSQL, SQLite, GDrive", "Development tools: Git, Sentry, etc.", "Productivity tools: Slack, Google Maps, etc.". Each box is joined to the central MCP box by a grey double-headed arrow; both sides carry the label "Bidirectional data flow".
- Why it matters: The hub-and-spoke picture behind the USB-C analogy: MCP turns an M×N integration problem (every AI app × every tool) into M+N, because each side only implements the protocol once. Useful for the slide that places MCP as the standard tool/context layer that agents (and multi-agent systems) plug into.
- Transcribed text: AI applications: Chat interface — Claude Desktop, LibreChat · IDEs and code editors — Claude Code, Goose · Other AI applications — 5ire, Superinterface | MCP — Standardized protocol | Data sources and tools: Data and file systems — PostgreSQL, SQLite, GDrive · Development tools — Git, Sentry, etc. · Productivity tools — Slack, Google Maps, etc. | Bidirectional data flow (x2)

### mcp-spec.web/images/light.svg
- Provenance: research/web/mcp-spec/assets/light.svg ← https://mintcdn.com/mcp/2BMHnlNW5OqOohXZ/logo/light.svg (alt "light logo"). Site header logo.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

### mcp-spec.web/images/dark.svg
- Provenance: research/web/mcp-spec/assets/dark.svg ← https://mintcdn.com/mcp/2BMHnlNW5OqOohXZ/logo/dark.svg (alt "dark logo"). Site header logo (dark theme).
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)

## Raw / preserved excerpts

> MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems. Using MCP, AI applications like Claude or ChatGPT can connect to data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.

> ## What can MCP enable?
> - Agents can access your Google Calendar and Notion, acting as a more personalized AI assistant.
> - Claude Code can generate an entire web app using a Figma design.
> - Enterprise chatbots can connect to multiple databases across an organization, empowering users to analyze data using chat.
> - AI models can create 3D designs on Blender and print them out using a 3D printer.
>
> ## Why does MCP matter?
> Depending on where you sit in the ecosystem, MCP can have a range of benefits.
> - **Developers**: MCP reduces development time and complexity when building, or integrating with, an AI application or agent.
> - **AI applications or agents**: MCP provides access to an ecosystem of data sources, tools and apps which will enhance capabilities and improve the end-user experience.
> - **End-users**: MCP results in more capable AI applications or agents which can access your data and take actions on your behalf when necessary.
>
> ## Broad ecosystem support
> MCP is an open protocol supported across a wide range of clients and servers. AI assistants like Claude and ChatGPT, development tools like Visual Studio Code, Cursor, MCPJam, and many others all support MCP — making it easy to build once and integrate everywhere.

> ## Build servers
> Create MCP servers to expose your data and tools
> ## Build clients
> Develop applications that connect to MCP servers
> ## Build MCP Apps
> Build interactive apps that run inside AI clients
