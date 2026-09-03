# MCP Servers Guide: How to Find, Install, and Use Model Context Protocol Servers

_Source: <https://skillsplayground.com/guides/mcp-servers/>_

[⚡ skillsplayground](/) 

# MCP Servers: The Complete Guide

Updated February 2026 · 15 min read 

**MCP (Model Context Protocol) servers** extend AI assistants like Claude Code, Cursor, and Windsurf with external capabilities -- connecting them to databases, APIs, cloud services, and thousands of other tools. This guide covers everything you need to know about finding, installing, configuring, and building MCP servers.

Browse our [MCP Server Directory](/mcps/) with 890+ servers sourced from the official MCP registry, organized by category with install commands.

## 1. What Are MCP Servers?

The **Model Context Protocol (MCP)** is an open standard created by Anthropic that defines how AI assistants communicate with external tools and services. An MCP server is a lightweight process that exposes specific capabilities (tools, resources, or prompts) to AI clients via a standardized protocol.

Think of MCP servers as plugins for AI assistants. Instead of the AI trying to do everything itself, it can delegate to specialized MCP servers that handle specific tasks -- querying a database, searching the web, managing files, interacting with APIs, and more.

### Key concepts

- **Tools** -- Functions the AI can call, like `query_database` or `send_email` 
- **Resources** -- Data the AI can read, like file contents or API responses 
- **Prompts** -- Pre-built prompt templates the AI can use 
- **Transports** -- How the client communicates with the server (stdio, SSE, or streamable-http) 

## 2. How to Install MCP Servers

There are three main ways to add MCP servers to your AI assistant setup:

### Method 1: Claude Code CLI (recommended)

Claude Code has built-in MCP server management. Add a server directly from the command line:

```
# Add an npm-based MCP server
claude mcp add my-server -- npx -y @modelcontextprotocol/server-filesystem /path/to/allowed

# Add a Python-based MCP server
claude mcp add my-db-server -- uvx mcp-server-sqlite --db-path ./my.db

# List installed MCP servers
claude mcp list

# Remove a server
claude mcp remove my-server
```

### Method 2: Configuration file

Add servers to your `.mcp.json` file (for Claude Code) or `claude_desktop_config.json` (for Claude Desktop):

```
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me/projects"]
    },
    "postgres": {
      "command": "uvx",
      "args": ["mcp-server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### Method 3: Remote MCP servers

Some MCP servers run remotely and connect via HTTP. These don't require local installation:

```
{
  "mcpServers": {
    "remote-service": {
      "url": "https://mcp.example.com/sse",
      "transport": "sse"
    }
  }
}
```

## 3. Best MCP Servers by Category

Here are the most popular and useful MCP servers organized by what they do. Browse our full [MCP Server Directory](/mcps/) for the complete list.

[Database PostgreSQL, MySQL, SQLite, Redis](/mcps/categories/database/) [Developer Tools Git, GitHub, CI/CD, testing](/mcps/categories/developer-tools/) [Search & Scraping Brave, Google, web scraping](/mcps/categories/search/) [AI & ML OpenAI, embeddings, vectors](/mcps/categories/ai-ml/) [Cloud & Infra AWS, Docker, Kubernetes](/mcps/categories/cloud/) [Communication Slack, Discord, email](/mcps/categories/communication/) [Productivity Notion, Jira, Linear](/mcps/categories/productivity/) [Data & Analytics CSV, JSON, BigQuery](/mcps/categories/data/) 

### The official reference servers

These are maintained by the MCP team and serve as reference implementations:

- **Filesystem** -- Secure file operations with configurable allowed directories 
- **Fetch** -- Web content fetching with HTML-to-markdown conversion 
- **Git** -- Repository operations (status, diff, log, commit) 
- **Memory** -- Persistent knowledge graph for storing facts across sessions 
- **Sequential Thinking** -- Structured problem-solving through thought sequences 

## 4. Transport Types Explained

MCP servers communicate with clients using one of three transport protocols:

- **stdio** -- The server runs as a local subprocess. The client launches it and communicates via stdin/stdout. Most common for local tools. Simple, fast, no network required. 
- **SSE (Server-Sent Events)** -- The server runs as an HTTP service. Client connects via HTTP and receives events over a persistent connection. Good for remote servers. 
- **Streamable HTTP** -- Modern HTTP-based transport using standard request/response with streaming. The newest and most flexible option for remote servers. 

**Which transport should you use?** For local tools, use `stdio` -- it's the simplest and most reliable. For remote/shared servers, use `streamable-http` if the server supports it, otherwise `sse`.

## 5. MCP Servers vs Claude Code Skills

Both MCP servers and [Claude Code skills](/guides/claude-code-skills-vs-mcp/) extend AI capabilities, but they work differently:

- **Skills** are prompt-based instructions that guide how Claude approaches a task. They're text files (`SKILL.md`) loaded into context. Great for encoding workflows, standards, and domain expertise. 
- **MCP servers** are executable tools that give Claude new capabilities it doesn't have by default. They run as separate processes and handle specific actions like database queries or API calls. 

Use **skills** when you want to change *how* Claude thinks. Use **MCP servers** when you want to change *what* Claude can do.

They work great together: a skill might instruct Claude to use a specific MCP server in a certain way. For example, a "database migration" skill could guide Claude through a migration workflow while using a PostgreSQL MCP server to inspect the current schema.

## 6. Building Your Own MCP Server

Creating an MCP server is straightforward with the official SDKs:

### TypeScript (Node.js)

```
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new McpServer({
  name: "my-server",
  version: "1.0.0",
});

// Define a tool
server.tool("greet", { name: "string" }, async ({ name }) => ({
  content: [{ type: "text", text: `Hello, ${name}!` }],
}));

// Start the server
const transport = new StdioServerTransport();
await server.connect(transport);
```

### Python

```
from mcp.server import Server
from mcp.server.stdio import stdio_server

server = Server("my-server")

@server.tool()
async def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

async def main():
    async with stdio_server() as (read, write):
        await server.run(read, write)
```

For a detailed guide on building MCP servers, check out the [MCP Builder skill](/skills/anthropics-skills-mcp-builder/) from Anthropic's official skills collection.

## 7. Where to Find MCP Servers

The MCP ecosystem is growing rapidly. Here are the best places to discover servers:

- **[Skills Playground MCP Directory](/mcps/)** -- Our curated directory with 890+ servers, organized by category 
- **Official MCP Registry** -- The canonical registry at `registry.modelcontextprotocol.io` with 5,000+ servers 
- **Smithery** -- A popular directory and hosting platform with 3,600+ servers 
- **GitHub** -- Search for `mcp-server` repos; many are open source 

## 8. Configuration Best Practices

- **Use environment variables for secrets** -- Never hardcode API keys in `.mcp.json`. Use the `env` field to reference environment variables. 
- **Limit file system access** -- When using the filesystem MCP server, restrict access to specific directories rather than giving access to your entire system. 
- **Version pin packages** -- Use specific versions in your install commands (`npx -y @package/name@1.2.3`) to avoid breaking changes. 
- **Start small** -- Only add MCP servers you actively need. Each server adds startup time and context. You can always add more later. 
- **Test locally first** -- Before adding a server to your config, test it manually to make sure it works and provides the tools you expect. 

**Security note:** MCP servers can execute code, access files, and make network requests. Only install servers from trusted sources, review their permissions, and use environment variables for sensitive configuration.

## 9. Troubleshooting Common Issues

### Server not connecting

- Check that the package is installed: `npx -y @package/name --version` 
- Verify the command and args in your config match what the server expects 
- Check for required environment variables in the server's documentation 

### Tools not appearing

- Restart Claude Code after adding or modifying `.mcp.json` 
- Run `claude mcp list` to verify the server is registered 
- Some servers require authentication before tools become available 

### Slow startup

- Use `npx -y` (the `-y` flag skips the install prompt) for faster npm-based servers 
- Consider using `bunx` instead of `npx` for faster package resolution 
- Reduce the number of active MCP servers to only what you need
