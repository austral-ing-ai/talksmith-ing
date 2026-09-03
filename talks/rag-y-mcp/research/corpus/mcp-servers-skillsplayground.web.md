---
source_file: mcp-servers-skillsplayground
source_type: web-capture
ingested_at: 2026-08-14
---

# MCP Servers: The Complete Guide (skillsplayground.com)

## Provenance
- Original location: `research/web/mcp-servers-skillsplayground/`
- Format: html (guía de un sitio de terceros). Texto tomado de `page.md` (~9.500 caracteres, 25 encabezados). **Extracción muy buena**: la página es liviana (22,9 KB de HTML) y `page.md` conserva las nueve secciones íntegras, con todos los bloques de código (bash, JSON, TypeScript, Python) intactos.
- URL: **https://skillsplayground.com/guides/mcp-servers/**
- Autor / fuente: **skillsplayground.com**. No hay autor firmante. El sitio se identifica con el wordmark "⚡ skillsplayground".
- Fecha del original: **"Updated February 2026"**, declarada en la página. Tiempo de lectura estimado: 15 minutos. **Es la única de las tres capturas de directorios MCP que se fecha a sí misma** — dato que la hace notablemente más citable que `mcp-directorio-claudemcp.web.md` (sin fecha) y `mcp-registro-mcp-so.web.md` (sólo fechas relativas).
- HTTP status: 200. `fetched_at`: 2026-08-14T16:56:58Z.
- Assets: **ninguno** (`assets: []`).

**Naturaleza de la fuente.** Guía divulgativa de terceros, con un directorio comercial asociado. No es normativa. Dicho eso, **es la fuente del corpus que más se acerca a documentar el protocolo**: explica la tríada tools/resources/prompts, los tres transportes con criterio de elección, y da configuración ejecutable. Dado que la spec oficial no se pudo capturar (ver `mcp-anuncio-anthropic-2024.web.md`), es el mejor sustituto disponible — con la advertencia de que **es sustituto, no fuente normativa**.

## Key claims

- **Definición operativa de servidor MCP**: *"An MCP server is a lightweight process that exposes specific capabilities (tools, resources, or prompts) to AI clients via a standardized protocol."*
- **Analogía central**: *"Think of MCP servers as plugins for AI assistants."* En vez de que la IA intente hacer todo por sí misma, delega en servidores especializados.
- **MCP es un estándar abierto creado por Anthropic** que define cómo los asistentes de IA se comunican con herramientas y servicios externos.
- **Cuatro conceptos clave**: tools, resources, prompts, transports.
- **Tres transportes**, con recomendación explícita de cuál usar: **stdio** para herramientas locales, **streamable-http** para servidores remotos si el servidor lo soporta, **SSE** si no.
- **stdio es el más común para herramientas locales** — *"Most common for local tools. Simple, fast, no network required."*
- **Tres métodos de instalación**: CLI de Claude Code (recomendado), archivo de configuración, servidores remotos por HTTP.
- **Distinción entre Skills y servidores MCP**, con una formulación muy limpia: *"Use **skills** when you want to change *how* Claude thinks. Use **MCP servers** when you want to change *what* Claude can do."*
- **Skills y MCP se complementan**: una skill puede instruir a Claude a usar un servidor MCP determinado de cierta manera.
- **Cinco servidores de referencia** mantenidos por el equipo de MCP: Filesystem, Fetch, Git, Memory, Sequential Thinking.
- **Advertencia de seguridad explícita**: *"MCP servers can execute code, access files, and make network requests. Only install servers from trusted sources, review their permissions, and use environment variables for sensitive configuration."*
- **Consejo de higiene que conecta con el bloque de selección de herramientas**: *"Start small — Only add MCP servers you actively need. **Each server adds startup time and context.** You can always add more later."*

## Definitions and terminology

**Los cuatro conceptos clave (verbatim, la tríada canónica más el transporte):**

> - **Tools** -- Functions the AI can call, like `query_database` or `send_email`
> - **Resources** -- Data the AI can read, like file contents or API responses
> - **Prompts** -- Pre-built prompt templates the AI can use
> - **Transports** -- How the client communicates with the server (stdio, SSE, or streamable-http)

**Los tres transportes (verbatim, completos)** — es la mejor explicación de transportes de todo el corpus:

> - **stdio** -- The server runs as a local subprocess. The client launches it and communicates via stdin/stdout. Most common for local tools. Simple, fast, no network required.
> - **SSE (Server-Sent Events)** -- The server runs as an HTTP service. Client connects via HTTP and receives events over a persistent connection. Good for remote servers.
> - **Streamable HTTP** -- Modern HTTP-based transport using standard request/response with streaming. The newest and most flexible option for remote servers.

Y el criterio de elección, verbatim: *"**Which transport should you use?** For local tools, use `stdio` -- it's the simplest and most reliable. For remote/shared servers, use `streamable-http` if the server supports it, otherwise `sse`."*

**Este pasaje contradice directamente la slide 47 del deck**, que afirma que MCP es "JSON-RPC estandarizado sobre HTTP". Ver `Inconsistencies`.

**MCP server (definición operativa):** *"a lightweight process that exposes specific capabilities (tools, resources, or prompts) to AI clients via a standardized protocol."* El énfasis en **proceso** es coherente con stdio como transporte por defecto.

**Skills vs. MCP servers (verbatim, la distinción más nítida del corpus):**

> - **Skills** are prompt-based instructions that guide how Claude approaches a task. They're text files (`SKILL.md`) loaded into context. Great for encoding workflows, standards, and domain expertise.
> - **MCP servers** are executable tools that give Claude new capabilities it doesn't have by default. They run as separate processes and handle specific actions like database queries or API calls.
>
> Use **skills** when you want to change *how* Claude thinks. Use **MCP servers** when you want to change *what* Claude can do.

## Evidence and examples

**Cifras del ecosistema declaradas (todas con la fecha "Updated February 2026" como referencia):**

| Fuente de servidores | Cantidad declarada | Cómo la describe la página |
|---|---|---|
| **Registro oficial de MCP** | **5.000+** | *"The canonical registry at `registry.modelcontextprotocol.io`"* |
| **Smithery** | **3.600+** | *"A popular directory and hosting platform"* |
| **Skills Playground (propio)** | **890+** | *"Our curated directory, organized by category"*, y en la intro: *"sourced from the official MCP registry"* |
| GitHub | sin número | *"Search for `mcp-server` repos; many are open source"* |

**Este es el dato más importante de la página para corregir el deck**: identifica el **registro oficial** como `registry.modelcontextprotocol.io`, distinto de mcp.so y de claudemcp.org. Confirma la corrección de atribución documentada en `mcp-registro-mcp-so.web.md`.

**El 890+ es la cifra que el deck cita en la slide 55**, atribuida correctamente a skillsplayground.com. Con esta captura se puede además fechar: **febrero de 2026**.

**Método 1 — CLI de Claude Code (verbatim, recomendado por la página):**

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

**Método 2 — archivo de configuración (verbatim).** `.mcp.json` para Claude Code, `claude_desktop_config.json` para Claude Desktop:

```json
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

**Nótese que esta configuración es stdio**: usa `command` + `args`, es decir, el cliente lanza un subproceso. Es exactamente la forma que el deck muestra en la slide 50 (Método 2) mientras describe MCP como HTTP.

**Método 3 — servidores remotos (verbatim):**

```json
{
  "mcpServers": {
    "remote-service": {
      "url": "https://mcp.example.com/sse",
      "transport": "sse"
    }
  }
}
```

**Los cinco servidores de referencia (verbatim):**

> - **Filesystem** -- Secure file operations with configurable allowed directories
> - **Fetch** -- Web content fetching with HTML-to-markdown conversion
> - **Git** -- Repository operations (status, diff, log, commit)
> - **Memory** -- Persistent knowledge graph for storing facts across sessions
> - **Sequential Thinking** -- Structured problem-solving through thought sequences

**Las ocho categorías del directorio propio (verbatim):** Database (PostgreSQL, MySQL, SQLite, Redis) · Developer Tools (Git, GitHub, CI/CD, testing) · Search & Scraping (Brave, Google, web scraping) · AI & ML (OpenAI, embeddings, vectors) · Cloud & Infra (AWS, Docker, Kubernetes) · Communication (Slack, Discord, email) · Productivity (Notion, Jira, Linear) · Data & Analytics (CSV, JSON, BigQuery).

**Construir un servidor propio — TypeScript (verbatim):**

```typescript
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

**Construir un servidor propio — Python (verbatim):**

```python
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

**Los dos ejemplos mínimos usan stdio.** Es el "hola mundo" de MCP y confirma cuál es el transporte por defecto en la práctica. Buen material para una slide de demo en vivo: son ~10 líneas en cualquiera de los dos lenguajes.

**Las cinco buenas prácticas de configuración (verbatim):**

> - **Use environment variables for secrets** -- Never hardcode API keys in `.mcp.json`. Use the `env` field to reference environment variables.
> - **Limit file system access** -- When using the filesystem MCP server, restrict access to specific directories rather than giving access to your entire system.
> - **Version pin packages** -- Use specific versions in your install commands (`npx -y @package/name@1.2.3`) to avoid breaking changes.
> - **Start small** -- Only add MCP servers you actively need. Each server adds startup time and context. You can always add more later.
> - **Test locally first** -- Before adding a server to your config, test it manually to make sure it works and provides the tools you expect.

**Resolución de problemas (verbatim, resumida)** — es la sección más práctica y no tiene equivalente en las otras fuentes:

- *Servidor que no conecta*: verificar que el paquete esté instalado (`npx -y @package/name --version`), que comando y argumentos coincidan con lo que el servidor espera, y que estén las variables de entorno requeridas.
- *Herramientas que no aparecen*: reiniciar Claude Code tras modificar `.mcp.json`; correr `claude mcp list` para verificar el registro; algunos servidores requieren autenticación antes de exponer sus herramientas.
- *Arranque lento*: usar `npx -y` (el flag `-y` saltea el prompt de instalación); considerar `bunx` en vez de `npx` para resolución de paquetes más rápida; **reducir la cantidad de servidores activos a los necesarios**.

## Inconsistencies / open questions

1. **Contradice la slide 47 del deck sobre el transporte, y esta fuente tiene razón.** El deck afirma que MCP es "JSON-RPC estandarizado sobre HTTP" y que el servidor es "un proceso separado en localhost". Esta página documenta que **stdio es el transporte más común para herramientas locales** ("The server runs as a local subprocess. The client launches it and communicates via stdin/stdout… no network required"), y que HTTP/SSE es para servidores remotos. Los dos ejemplos de código mínimo de la página usan stdio, y la configuración del Método 2 —idéntica en forma a la que el deck muestra en la slide 50— **es stdio, no HTTP**. La descripción del deck es incorrecta y esta captura lo demuestra. (Advertencia: esta fuente no es normativa; la confirmación definitiva requiere la spec oficial, que no se pudo capturar.)
2. **Tres cifras de ecosistema irreconciliables entre sí.** 5.000+ (registro oficial), 3.600+ (Smithery) y 890+ (directorio propio) — y el propio sitio afirma que sus 890+ están "sourced from the official MCP registry", que tiene 5.000+. O el sub-conjunto está curado con criterio (probable, dice "curated") o las cifras son de momentos distintos. La página no lo aclara. **Si el deck cita el 890+, debería aclarar que es un directorio curado, no el total del ecosistema.**
3. **Y el artículo de MSR da un cuarto número.** `tool-space-interference-msr.web.md` (septiembre de 2025) dice que Smithery tiene "over 7,000" servidores; esta página (febrero de 2026) le atribuye 3.600+. **Smithery habría perdido la mitad de su catálogo en cinco meses**, lo cual es poco plausible: más probable es que uno de los dos cuente algo distinto (servidores registrados vs. servidores que arrancan, por ejemplo — MSR documenta que de su muestra hubo que excluir los vacíos y los que no arrancaban). **Ninguna cifra de tamaño del ecosistema en este corpus es confiable.** Si el deck da un número, que sea con fuente y fecha explícitas, y preferentemente con la salvedad de que los recuentos no son comparables entre sí.
4. **La lista de servidores de referencia no coincide con la de claudemcp.org.** Acá son **cinco** (Filesystem, Fetch, Git, Memory, Sequential Thinking); `mcp-directorio-claudemcp.web.md` lista **siete** (agrega Everything y Time). Ni una ni otra es autoridad. La lista canónica está en `github.com/modelcontextprotocol/servers`, que devolvió HTTP 403 y no se capturó.
5. **Un paquete del ejemplo parece tener el scope equivocado.** El bloque de configuración usa `@anthropic/mcp-server-brave-search`, mientras que los otros dos usan `@modelcontextprotocol/…`. Los servidores de referencia se publican bajo el scope `@modelcontextprotocol`, no `@anthropic`. Es muy probablemente un error de la guía. **No copiar ese bloque a una slide sin verificar el nombre del paquete.**
6. **No hay ninguna mención a los límites del protocolo.** La guía no dice nada sobre namespaces, colisiones de nombres, tamaño de respuestas ni gestión de contexto — todas carencias que `tool-space-interference-msr.web.md` documenta con evidencia. Es una guía de "cómo empezar", no de "qué sale mal". Complementarias, no intercambiables.
7. **Punto de contacto interesante con el bloque de selección de herramientas.** El consejo "Start small — each server adds startup time and context" y el consejo de troubleshooting "reduce the number of active MCP servers to only what you need" son, en lenguaje práctico, exactamente el hallazgo de MSR sobre interferencia de espacio de herramientas. **Sirve para cerrar el círculo en una slide**: la recomendación operativa que circula en las guías coincide con lo que la investigación mide.
8. **El sitio tiene interés comercial en su propio directorio.** Enlaza tres veces a `/mcps/`. No invalida el contenido técnico, que es sólido y verificable, pero conviene tenerlo presente al citar sus cifras.
9. **La fecha es una fortaleza y una advertencia a la vez.** "Updated February 2026" la hace la más citable de los tres directorios. Pero también significa que, a la fecha de la clase, los recuentos tienen medio año.

## Images / diagrams

Ninguna. `metadata.yaml` registra `assets: []`. La página no contiene imágenes, diagramas ni capturas — es texto y bloques de código. La carpeta compañera `research/corpus/mcp-servers-skillsplayground.web/images/` existe y está vacía, lo cual es válido.

## Raw / preserved excerpts

**Cabecera (verbatim):**

> # MCP Servers: The Complete Guide
>
> Updated February 2026 · 15 min read
>
> **MCP (Model Context Protocol) servers** extend AI assistants like Claude Code, Cursor, and Windsurf with external capabilities -- connecting them to databases, APIs, cloud services, and thousands of other tools. This guide covers everything you need to know about finding, installing, configuring, and building MCP servers.
>
> Browse our [MCP Server Directory](/mcps/) with 890+ servers sourced from the official MCP registry, organized by category with install commands.

**Sección 1, "What Are MCP Servers?" (verbatim, completa):**

> The **Model Context Protocol (MCP)** is an open standard created by Anthropic that defines how AI assistants communicate with external tools and services. An MCP server is a lightweight process that exposes specific capabilities (tools, resources, or prompts) to AI clients via a standardized protocol.
>
> Think of MCP servers as plugins for AI assistants. Instead of the AI trying to do everything itself, it can delegate to specialized MCP servers that handle specific tasks -- querying a database, searching the web, managing files, interacting with APIs, and more.
>
> ### Key concepts
>
> - **Tools** -- Functions the AI can call, like `query_database` or `send_email`
> - **Resources** -- Data the AI can read, like file contents or API responses
> - **Prompts** -- Pre-built prompt templates the AI can use
> - **Transports** -- How the client communicates with the server (stdio, SSE, or streamable-http)

**Sección 4, "Transport Types Explained" (verbatim, completa):**

> MCP servers communicate with clients using one of three transport protocols:
>
> - **stdio** -- The server runs as a local subprocess. The client launches it and communicates via stdin/stdout. Most common for local tools. Simple, fast, no network required.
> - **SSE (Server-Sent Events)** -- The server runs as an HTTP service. Client connects via HTTP and receives events over a persistent connection. Good for remote servers.
> - **Streamable HTTP** -- Modern HTTP-based transport using standard request/response with streaming. The newest and most flexible option for remote servers.
>
> **Which transport should you use?** For local tools, use `stdio` -- it's the simplest and most reliable. For remote/shared servers, use `streamable-http` if the server supports it, otherwise `sse`.

**Sección 5, "MCP Servers vs Claude Code Skills" (verbatim, completa):**

> Both MCP servers and Claude Code skills extend AI capabilities, but they work differently:
>
> - **Skills** are prompt-based instructions that guide how Claude approaches a task. They're text files (`SKILL.md`) loaded into context. Great for encoding workflows, standards, and domain expertise.
> - **MCP servers** are executable tools that give Claude new capabilities it doesn't have by default. They run as separate processes and handle specific actions like database queries or API calls.
>
> Use **skills** when you want to change *how* Claude thinks. Use **MCP servers** when you want to change *what* Claude can do.
>
> They work great together: a skill might instruct Claude to use a specific MCP server in a certain way. For example, a "database migration" skill could guide Claude through a migration workflow while using a PostgreSQL MCP server to inspect the current schema.

**Sección 7, "Where to Find MCP Servers" (verbatim, completa — la fuente de la corrección sobre el registro oficial):**

> The MCP ecosystem is growing rapidly. Here are the best places to discover servers:
>
> - **[Skills Playground MCP Directory](/mcps/)** -- Our curated directory with 890+ servers, organized by category
> - **Official MCP Registry** -- The canonical registry at `registry.modelcontextprotocol.io` with 5,000+ servers
> - **Smithery** -- A popular directory and hosting platform with 3,600+ servers
> - **GitHub** -- Search for `mcp-server` repos; many are open source

**Sección 8, nota de seguridad (verbatim):**

> **Security note:** MCP servers can execute code, access files, and make network requests. Only install servers from trusted sources, review their permissions, and use environment variables for sensitive configuration.

**Sección 9, "Troubleshooting Common Issues" (verbatim, completa):**

> ### Server not connecting
>
> - Check that the package is installed: `npx -y @package/name --version`
> - Verify the command and args in your config match what the server expects
> - Check for required environment variables in the server's documentation
>
> ### Tools not appearing
>
> - Restart Claude Code after adding or modifying `.mcp.json`
> - Run `claude mcp list` to verify the server is registered
> - Some servers require authentication before tools become available
>
> ### Slow startup
>
> - Use `npx -y` (the `-y` flag skips the install prompt) for faster npm-based servers
> - Consider using `bunx` instead of `npx` for faster package resolution
> - Reduce the number of active MCP servers to only what you need
