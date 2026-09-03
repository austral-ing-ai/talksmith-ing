---
source_file: mcp-directorio-claudemcp
source_type: web-capture
ingested_at: 2026-08-14
---

# Claude MCP Servers Directory (claudemcp.org)

## Provenance
- Original location: `research/web/mcp-directorio-claudemcp/`
- Format: html (portada de un directorio). Texto tomado de `page.md` (~6.800 caracteres, 55 encabezados). La extracción es completa: la página es liviana (17,7 KB de HTML) y `page.md` conserva las tres secciones (qué es MCP, los dos listados de servidores, y el FAQ). Los 55 encabezados son las tarjetas de servidor, casi todas con el `<h3>` vacío y el texto dentro del enlace.
- URL: **https://www.claudemcp.org/**
- Título declarado: **"Claude MCP Servers Directory - Model Context Protocol"**.
- Autor / fuente: operadores de claudemcp.org. **No se identifica ninguna persona ni organización** en la página. El dominio no pertenece a Anthropic.
- Fecha del original: sin fecha de publicación ni de última actualización en ninguna parte de la página.
- HTTP status: 200. `fetched_at`: 2026-08-14T16:56:59Z.
- Assets: **ninguno** (`assets: []`).

**Naturaleza de la fuente.** Directorio de terceros. **No es oficial**, pese a que el dominio contiene "claude" y a que la página etiqueta parte de su catálogo como "Official" — esa etiqueta califica a los *servidores* listados, no al directorio. Es el más chico y más ordenado de los tres directorios del corpus.

## Key claims

- **Propósito declarado**: *"Discover and integrate Claude MCP servers for Claude and other AI assistants."* Nótese "and other AI assistants": el directorio no se presenta como exclusivo de Claude.
- **La analogía USB-C.** Es la fuente de esta metáfora en el corpus, verbatim: *"The Model Context Protocol (MCP) is an open standard that enables AI assistants to securely connect with external data sources and tools. **Think of it as USB-C for AI - a universal way to provide context.**"* Si el deck usa la analogía USB-C, **viene de acá o de un lugar equivalente, no del anuncio de Anthropic**, que nunca la emplea (ver `mcp-anuncio-anthropic-2024.web.md`).
- **El catálogo se divide en dos clases con criterio explícito**: **Reference Servers (Official)** y **Popular Community Servers (30+)**.
- **Criterio de la distinción, verbatim del FAQ**: *"Official servers are maintained by Anthropic and the MCP core team, ensuring high quality and regular updates. Community servers are created and maintained by third-party developers and offer additional integrations and features beyond the official servers."*
- **Siete servidores de referencia oficiales**: Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, Time.
- **Treinta y cuatro servidores comunitarios** listados (la sección se titula "30+").
- **Modelo de seguridad que propone**: *"MCP servers run locally on your machine and you control what data they can access. Official servers are thoroughly vetted by Anthropic. For community servers, review the source code and permissions before installation."*
- **Instalación**: agregar la configuración del servidor al archivo de configuración de Claude Desktop. Cada página de servidor provee los paquetes npm necesarios y la configuración lista para copiar y pegar.
- **Se pueden usar varios servidores a la vez**: *"You can install and use multiple MCP servers simultaneously."*
- **Barrera de entrada**: familiaridad básica con archivos de configuración y línea de comandos; para la mayoría de los servidores hace falta instalar Node.js y editar un JSON.
- **Recomendación de por dónde empezar**: Filesystem (acceso a archivos locales), Fetch (contenido web) y GitHub (si trabajás con repositorios).

## Definitions and terminology

**MCP, según este directorio (verbatim):** *"The Model Context Protocol (MCP) is an open standard that enables AI assistants to securely connect with external data sources and tools. Think of it as USB-C for AI - a universal way to provide context."*

**Claude MCP, según el FAQ (verbatim):** *"Claude MCP (Model Context Protocol) is an open standard that enables AI assistants like Claude to securely connect with external data sources and tools. It provides a universal way for AI assistants to access context from various services and applications."*

**Reference Servers / Official.** Servidores mantenidos por Anthropic y el equipo central de MCP. Sirven como implementaciones de referencia del protocolo. Son siete.

**Community Servers.** Creados y mantenidos por desarrolladores externos. Ofrecen integraciones más allá de las oficiales. La página no describe ningún proceso de revisión propio para admitirlos; delega la responsabilidad en el usuario ("review the source code and permissions before installation").

**Filtro de la interfaz.** La página expone un control con tres opciones: `All` · `Official` · `Community`.

## Evidence and examples

**Los siete servidores de referencia oficiales, con su descripción verbatim:**

| Servidor | Descripción |
|---|---|
| **Everything** | "Reference/test server with prompts, resources, and tools" |
| **Fetch** | "Web content fetching and conversion for efficient LLM usage" |
| **Filesystem** | "Secure file operations with configurable access controls" |
| **Git** | "Tools to read, search, and manipulate Git repositories" |
| **Memory** | "Knowledge graph-based persistent memory system" |
| **Sequential Thinking** | "Dynamic and reflective problem-solving through thought sequences" |
| **Time** | "Time and timezone conversion capabilities" |

Este listado es **cotejable** con el del anuncio de Anthropic y con el de skillsplayground — ver `Inconsistencies`.

**Los 34 servidores comunitarios listados, con su descripción verbatim:**

| Servidor | Descripción |
|---|---|
| **GitHub** | "Interact with GitHub repositories, issues, and pull requests" |
| **Slack** | "Read and send messages, manage channels in Slack workspaces" |
| **PostgreSQL** | "Query and manage PostgreSQL databases" |
| **Puppeteer** | "Browser automation for web scraping and testing" |
| **Brave Search** | "Web search capabilities using Brave Search API" |
| **Google Drive** | "Access and manage files in Google Drive" |
| **Google Maps** | "Location services and mapping capabilities" |
| **AWS** | "Integration with Amazon Web Services" |
| **Azure** | "Microsoft Azure cloud services integration" |
| **SQLite** | "Query and manage SQLite databases" |
| **Sentry** | "Error tracking and monitoring integration" |
| **GitLab** | "Interact with GitLab repositories and CI/CD" |
| **Redis** | "In-memory data structure store operations" |
| **EverArt** | "AI image generation capabilities" |
| **Atlassian** | "Interact with Jira and Confluence" |
| **Notion** | "Manage Notion pages and databases" |
| **Discord** | "Interact with Discord servers and channels" |
| **Docker** | "Manage Docker containers and images" |
| **Apollo** | "Connect GraphQL APIs to AI agents" |
| **Auth0** | "Identity and access management integration" |
| **Playwright** | "Browser automation using accessibility tree (Microsoft)" |
| **Context7** | "Up-to-date code documentation for LLMs" |
| **Supabase** | "Connect to Supabase projects and manage databases" |
| **Figma** | "Generate code from Figma designs and components" |
| **Serena** | "Coding agent toolkit with semantic code analysis" |
| **Blender** | "AI-assisted 3D modeling, scene creation, and rendering in Blender" |
| **Microsoft 365** | "Outlook, Teams, OneDrive, SharePoint, Excel via Microsoft Graph" |
| **Godot** | "Drive the Godot game engine — scenes, scripts, and play mode" |
| **Perplexity** | "Live web search and cited answers via the Sonar API" |
| **Firecrawl** | "Advanced web scraping, crawling, and structured extraction" |
| **Unity** | "Drive the Unity editor — GameObjects, scenes, and play mode" |
| **LinkedIn** | "Search profiles, jobs, and companies for research and outreach" |
| **Monarch Money** | "Personal finance — accounts, transactions, budgets, net worth" |
| **Google Ads** | "Query campaigns, run GAQL reports, optimize ad performance" |

**Total en la portada: 7 oficiales + 34 comunitarios = 41 servidores.**

**Composición del catálogo, para leerlo con criterio**: el listado comunitario está dominado por **infraestructura de desarrollo** (GitHub, GitLab, Docker, Sentry, Auth0, Supabase), **bases de datos** (PostgreSQL, SQLite, Redis), **nubes** (AWS, Azure), **automatización de navegador** (Puppeteer, Playwright, Firecrawl), **productividad** (Slack, Notion, Atlassian, Microsoft 365, Discord) y **motores de juego / creación** (Blender, Godot, Unity, Figma). **No hay ningún servidor de temática biomédica, científica ni clínica en toda la página** — dato relevante para un curso de IA generativa aplicada a biomedicina. El único servidor de salud que aparece en cualquier directorio de este corpus es Medplum, en `mcp-registro-mcp-so.web.md`.

**Respuestas del FAQ sobre operación práctica (verbatim, resumidas):**

- **Instalación**: agregar la configuración al archivo de config de Claude Desktop; cada página de servidor trae instrucciones detalladas con los paquetes npm requeridos y los ajustes de configuración.
- **Varios servidores a la vez**: sí, agregando la configuración de cada uno.
- **Conocimiento requerido**: familiaridad básica con archivos de configuración y línea de comandos, "helpful, but not strictly required"; para la mayoría hace falta Node.js y editar un JSON.
- **Por dónde empezar**: Filesystem, Fetch, GitHub.
- **Crear un servidor propio**: sí, MCP es un estándar abierto; remite a "the official MCP documentation and server examples on GitHub".

## Inconsistencies / open questions

1. **El listado "oficial" no coincide con el del anuncio de Anthropic.** El anuncio de noviembre de 2024 (`mcp-anuncio-anthropic-2024.web.md`) nombra como servidores pre-construidos a **Google Drive, Slack, GitHub, Git, Postgres y Puppeteer**. Este directorio pone **sólo Git** en la columna oficial, y manda **Google Drive, Slack, GitHub, PostgreSQL y Puppeteer a la columna comunitaria**. Alguno de los dos está desactualizado, o el conjunto de servidores de referencia cambió entre 2024 y 2026. **La discrepancia no se puede resolver con este corpus**, porque el repositorio oficial (`github.com/modelcontextprotocol/servers`) devolvió HTTP 403 y no se capturó. Si el deck presenta una lista de "servidores oficiales", esta es una fuente insegura.
2. **La lista de referencia tampoco coincide con la de skillsplayground.** `mcp-servers-skillsplayground.web.md` enumera cinco servidores de referencia (Filesystem, Fetch, Git, Memory, Sequential Thinking); este directorio enumera siete (agrega **Everything** y **Time**). Dos directorios, dos listas distintas de lo que es "oficial".
3. **La página no tiene ninguna fecha.** Ni de publicación, ni de última actualización, ni por servidor. Es el problema más grave de citabilidad: un directorio sin fecha en un ecosistema que cambia cada semana no se puede citar sin adjuntar la fecha de captura (2026-08-14).
4. **El rótulo "30+" no cuadra con el contenido.** La sección se titula "Popular Community Servers (30+)" y lista 34. No es un error, pero sugiere que el título es estático y el listado creció por debajo — otra señal de mantenimiento manual.
5. **"Official servers are thoroughly vetted by Anthropic" es una afirmación fuerte y no verificable acá.** El directorio no aporta ninguna evidencia de ese proceso de auditoría, y no es Anthropic quien lo afirma sino un tercero. Cuidado si el deck lo repite en una slide de seguridad.
6. **"MCP servers run locally on your machine" ya no es cierto en general.** El FAQ presenta la ejecución local como propiedad del modelo de seguridad de MCP. Pero `mcp-servers-skillsplayground.web.md` documenta transportes remotos (SSE y streamable HTTP) y `mcp-registro-mcp-so.web.md` lista servidores remotos con OAuth. La afirmación describe el MCP de 2024, no el de 2026, y **si se cita como garantía de seguridad es engañosa**.
7. **No dice de dónde saca su catálogo.** A diferencia de skillsplayground, que declara que sus 890+ servidores vienen "sourced from the official MCP registry", este directorio no explica su procedencia ni su criterio de inclusión.
8. **Dominio potencialmente confuso.** `claudemcp.org` contiene la marca "Claude" y usa "Claude MCP" como si fuera el nombre del protocolo ("Claude MCP (Model Context Protocol) is an open standard…"), cuando el protocolo se llama simplemente Model Context Protocol y no es específico de Claude. La página misma se contradice al decir "for Claude and other AI assistants". **No es un sitio de Anthropic.**
9. **Los encabezados de las tarjetas están vacíos en el HTML.** `page.md` muestra 55 encabezados `###` seguidos de una línea en blanco y luego el enlace con todo el texto pegado (`[EverythingReference/test server with prompts, resources, and toolsOfficial](mcp/everything.html)`). Es un artefacto del marcado del sitio, no de la extracción; los nombres y descripciones se recuperaron correctamente separándolos del texto del enlace.

## Images / diagrams

Ninguna. `metadata.yaml` registra `assets: []`. La página no contiene imágenes, logos de servidor, diagramas ni capturas — las tarjetas de servidor tienen un espacio para ícono que quedó vacío en el HTML capturado. La carpeta compañera `research/corpus/mcp-directorio-claudemcp.web/images/` existe y está vacía, lo cual es válido.

## Raw / preserved excerpts

**Cabecera (verbatim):**

> # Claude MCP Servers Directory
>
> Discover and integrate Claude MCP servers for Claude and other AI assistants

**"What is MCP?" (verbatim, completo — es la fuente de la analogía USB-C):**

> The Model Context Protocol (MCP) is an open standard that enables AI assistants to securely connect with external data sources and tools. Think of it as USB-C for AI - a universal way to provide context.

**Filtro de la interfaz (verbatim):**

> All Official Community

**FAQ completo (verbatim):**

> **What is Claude MCP?**
> Claude MCP (Model Context Protocol) is an open standard that enables AI assistants like Claude to securely connect with external data sources and tools. It provides a universal way for AI assistants to access context from various services and applications.
>
> **How do I install an MCP server?**
> To install an MCP server, you'll need to add its configuration to your Claude Desktop config file. Each server page provides detailed installation instructions including the required npm packages and configuration settings. Simply copy the provided configuration into your Claude Desktop settings.
>
> **What's the difference between Official and Community servers?**
> Official servers are maintained by Anthropic and the MCP core team, ensuring high quality and regular updates. Community servers are created and maintained by third-party developers and offer additional integrations and features beyond the official servers.
>
> **Are MCP servers secure?**
> MCP servers run locally on your machine and you control what data they can access. Official servers are thoroughly vetted by Anthropic. For community servers, review the source code and permissions before installation. Always use API keys and credentials securely.
>
> **Can I use multiple MCP servers at the same time?**
> Yes! You can install and use multiple MCP servers simultaneously. Simply add each server's configuration to your Claude Desktop config file, and Claude will have access to all of them during your conversations.
>
> **Do I need coding knowledge to use MCP servers?**
> Basic familiarity with configuration files and command-line operations is helpful, but not strictly required. Each server page provides copy-paste configurations and step-by-step instructions. For most servers, you'll need to install Node.js and edit a JSON configuration file.
>
> **Which MCP servers should I start with?**
> Popular starting points include the Filesystem server for local file access, the Fetch server for web content, and the GitHub server if you work with code repositories. Choose servers based on your specific workflow and needs.
>
> **Can I create my own MCP server?**
> Yes! MCP is an open standard and you can create custom servers to integrate any data source or tool. Check the official MCP documentation and server examples on GitHub to get started with building your own server.
