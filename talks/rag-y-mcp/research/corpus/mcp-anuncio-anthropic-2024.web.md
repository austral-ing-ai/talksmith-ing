---
source_file: mcp-anuncio-anthropic-2024
source_type: web-capture
ingested_at: 2026-08-14
---

# Introducing the Model Context Protocol (Anthropic, 25 de noviembre de 2024)

## Provenance
- Original location: `research/web/mcp-anuncio-anthropic-2024/`
- Format: html (post de anuncio del sitio de Anthropic). Texto tomado de `page.md` (~6.000 caracteres, 9 encabezados). Extracción limpia; el cuerpo del anuncio está completo.
- URL: https://www.anthropic.com/news/model-context-protocol
- Autor / fuente: **Anthropic**, sección "Announcements". El post no lleva firma individual, pero acredita la creación del protocolo a **David Soria Parra** y **Justin Spahr-Summers**.
- Fecha del original: **25 de noviembre de 2024** (`Nov 25, 2024`).
- HTTP status: 200. `fetched_at`: 2026-08-14T16:57:33Z.

**Naturaleza de la fuente.** Es el **anuncio de lanzamiento** de MCP: un comunicado corporativo, no documentación técnica. Establece la fecha, la autoría y la intención del protocolo, y **no** especifica nada. Para cualquier detalle normativo (métodos, ciclo de vida, transportes, esquemas) esta fuente no sirve — ver la advertencia sobre la especificación faltante más abajo.

## ⚠️ Falta la especificación oficial de MCP en todo el corpus

**Esto afecta a todo el bloque MCP del deck (slides 41-49) y hay que decirlo antes que nada.**

- `modelcontextprotocol.io` — el sitio de la especificación oficial — **no se pudo capturar**: fallos de red repetidos.
- `github.com/modelcontextprotocol/servers` — el repositorio oficial de servidores de referencia — **devolvió HTTP 403**.

Consecuencia: **no hay ninguna fuente normativa de MCP en `research/corpus/`.** Todo lo que el deck afirma sobre el protocolo (nombres de métodos como `tools/list`, ciclo de vida de la conexión, negociación de capacidades, formato de los esquemas de herramientas, transportes soportados y su semántica) queda sin respaldo verificable en este corpus.

Lo que **sí** hay, y con qué alcance:

| Fuente disponible | Qué cubre | Qué NO cubre |
|---|---|---|
| **Este anuncio** | Fecha, autoría, motivación, arquitectura a grandísimos rasgos (clientes/servidores), lista de los primeros servidores pre-construidos, primeros adoptantes | Absolutamente ningún detalle de protocolo |
| `jsonrpc-2-spec.web.md` | **La capa de transporte de mensajes de MCP**, normativamente: request/response, notificaciones, batch, códigos de error. Es la única spec real del corpus | Todo lo específico de MCP: tools, resources, prompts, sampling, ciclo de vida, capacidades |
| `tool-space-interference-msr.web.md` | Observaciones empíricas sobre servidores MCP reales; **nombra carencias concretas de la spec** (sin namespaces formales, sin guía de tamaño de respuesta, sin recursos provistos por el cliente) | No es normativo; describe el ecosistema, no el protocolo |
| `mcp-servers-skillsplayground.web.md` | Descripción divulgativa de tools/resources/prompts y de los tres transportes (stdio, SSE, streamable-http) | No es oficial ni normativo; es una guía de terceros |
| `mcp-directorio-claudemcp.web.md`, `mcp-registro-mcp-so.web.md` | Catálogos de servidores | Nada del protocolo |

**Recomendación para el deck**: cualquier slide de 41 a 49 que enuncie una regla del protocolo debería o bien citarse contra la spec oficial (recapturándola), o bien marcarse como pendiente. En particular, la afirmación de la slide 47 de que MCP es "JSON-RPC estandarizado sobre HTTP" es **incorrecta según las fuentes que sí tenemos**: `mcp-servers-skillsplayground.web.md` documenta stdio como el transporte más común para servidores locales, y el propio ejemplo de configuración de la slide 50 (`command` + `args` con `npx`) es stdio, no HTTP.

## Key claims

- **MCP se anuncia como estándar abierto y open source** para conectar asistentes de IA a los sistemas donde viven los datos: repositorios de contenido, herramientas de negocio y entornos de desarrollo. Objetivo declarado: *"help frontier models produce better, more relevant responses."*
- **El diagnóstico es el aislamiento de los modelos, no su capacidad.** *"even the most sophisticated models are constrained by their isolation from data—trapped behind information silos and legacy systems."*
- **El problema concreto es el costo cuadrático de las integraciones.** *"Every new data source requires its own custom implementation, making truly connected systems difficult to scale."* MCP reemplaza integraciones fragmentadas por un solo protocolo.
- **La arquitectura, en la única formulación que da el anuncio**: *"developers can either expose their data through MCP servers or build AI applications (MCP clients) that connect to these servers."* Conexiones **bidireccionales** y seguras.
- **Tres componentes lanzados el día 1**: (1) la especificación y los SDKs, (2) soporte de servidores MCP locales en las apps de Claude Desktop, (3) un repositorio open source de servidores MCP.
- **Servidores pre-construidos para sistemas empresariales populares**: Google Drive, Slack, GitHub, Git, Postgres y Puppeteer.
- **Claude 3.5 Sonnet es bueno construyendo implementaciones de servidores MCP rápido** — argumento de adopción del propio anuncio.
- **Primeros adoptantes**: Block y Apollo integraron MCP en sus sistemas. Empresas de herramientas de desarrollo trabajando con MCP: Zed, Replit, Codeium y Sourcegraph.
- **La visión a futuro**: *"As the ecosystem matures, AI systems will maintain context as they move between different tools and datasets, replacing today's fragmented integrations with a more sustainable architecture."* — la persistencia de contexto **entre** herramientas es la promesa, y es más ambiciosa que "conectar a una base de datos".
- **Disponibilidad al momento del anuncio**: todos los planes de Claude.ai soportaban conectar servidores MCP a la app de escritorio. Los clientes de Claude for Work podían testear servidores localmente. Los toolkits para desplegar servidores remotos en producción se prometían para "pronto".

## Definitions and terminology

**Model Context Protocol (MCP).** Definición del anuncio, verbatim: *"an open standard that enables developers to build secure, two-way connections between their data sources and AI-powered tools."* Nótese: **two-way** (bidireccional) y **secure** son parte de la definición desde el día uno.

**MCP server.** El lado que **expone** datos. *"developers can either expose their data through MCP servers…"*

**MCP client.** La aplicación de IA que **se conecta** a los servidores. *"…or build AI applications (MCP clients) that connect to these servers."*

Estas dos son las únicas definiciones que el anuncio da. **No define tools, resources, prompts, transports, capabilities, ni ningún método.** Para esos conceptos, en este corpus, la única fuente es `mcp-servers-skillsplayground.web.md`, que es de terceros y no normativa.

**"Universal, open standard".** El encuadre retórico del anuncio: MCP como reemplazo de las integraciones a medida por un protocolo único. La analogía "USB-C para IA" que el deck probablemente use **no está en este anuncio** — aparece en `mcp-directorio-claudemcp.web.md` ("Think of it as USB-C for AI - a universal way to provide context"), que es un directorio de terceros.

## Evidence and examples

**Los tres componentes anunciados (verbatim):**

> - The Model Context Protocol specification and SDKs
> - Local MCP server support in the Claude Desktop apps
> - An open-source repository of MCP servers

**Servidores pre-construidos del día 1** (seis, verbatim): Google Drive, Slack, GitHub, Git, Postgres, Puppeteer.

**Adoptantes tempranos** (verbatim): Block y Apollo integraron MCP en sus sistemas. Zed, Replit, Codeium y Sourcegraph trabajando con MCP.

**Beneficio que el anuncio atribuye a los adoptantes de herramientas de desarrollo (verbatim):** *"enabling AI agents to better retrieve relevant information to further understand the context around a coding task and produce more nuanced and functional code with fewer attempts."*

**Cita de Block, verbatim (la única cita de un tercero en el anuncio):**

> "At Block, open source is more than a development model—it's the foundation of our work and a commitment to creating technology that drives meaningful change and serves as a public good for all," said Dhanji R. Prasanna, Chief Technology Officer at Block. "Open technologies like the Model Context Protocol are the bridges that connect AI to real-world applications, ensuring innovation is accessible, transparent, and rooted in collaboration. We are excited to partner on a protocol and use it to build agentic systems, which remove the burden of the mechanical so people can focus on the creative."

**Autoría (verbatim):** *"MCP was created at Anthropic by David Soria Parra and Justin Spahr-Summers."*

**Los tres pasos para empezar (verbatim):**

> - Install pre-built MCP servers through the Claude Desktop app
> - Follow our quickstart guide to build your first MCP server
> - Contribute to our open-source repositories of connectors and implementations

**Enlaces salientes del anuncio** (útiles como pista de dónde vive la documentación real):
- `https://modelcontextprotocol.io` — sitio del protocolo. **No capturado (fallos de red).**
- `https://github.com/modelcontextprotocol` — organización de GitHub con spec y SDKs.
- `https://github.com/modelcontextprotocol/servers` — repositorio de servidores. **No capturado (HTTP 403).**
- `https://modelcontextprotocol.io/quickstart` — guía de inicio rápido. No capturada.

## Inconsistencies / open questions

1. **La spec oficial no está en el corpus.** Ver el bloque de advertencia arriba. Es la carencia más importante de todo el material de la clase y afecta a nueve slides.
2. **El anuncio no contiene un solo detalle técnico.** No hay ni un ejemplo de mensaje, ni un nombre de método, ni un esquema, ni una mención del transporte. Es correcto para un anuncio, pero significa que **citar este post como fuente de cualquier afirmación técnica sobre MCP es un error**. Sirve para "qué es y cuándo salió", nada más.
3. **"Two-way connections" nunca se explica.** Es un término del anuncio y no está desarrollado. Sin la spec no se puede sostener qué significa exactamente (¿sampling? ¿notificaciones del servidor al cliente? ¿ambas?).
4. **El anuncio no menciona la palabra "tool" ni una sola vez.** Habla de "data sources", "content repositories", "business tools" y "development environments". La centralidad de las *herramientas* en MCP —que es como el deck y todo el ecosistema lo entienden hoy— es posterior al lanzamiento. Dato interesante para una slide sobre la evolución del protocolo, y advertencia contra proyectar el MCP de 2026 sobre el texto de 2024.
5. **Desfase temporal de casi 18 meses.** El anuncio es de noviembre de 2024; el deck es de abril de 2026. Todo lo que el anuncio describe como estado presente ("Claude for Work customers can begin testing MCP servers locally", "We'll soon provide developer toolkits for deploying remote production MCP servers") está desactualizado. En particular, los servidores remotos, que acá son una promesa futura, ya son realidad corriente en el ecosistema que describen `mcp-registro-mcp-so.web.md` y `tool-space-interference-msr.web.md`.
6. **La afirmación de escalabilidad no está cuantificada.** "Making truly connected systems difficult to scale" es el diagnóstico, pero el anuncio nunca enuncia el argumento N×M (N clientes × M fuentes de datos requieren N×M integraciones; con un protocolo, N+M). Si el deck usa ese argumento —que es el argumento correcto— **no lo saca de acá**: lo está agregando por su cuenta y debería presentarlo como razonamiento propio, no como cita de Anthropic.
7. **La sección "Related content" trajo ruido.** La extracción incluyó tres posts no relacionados del sidebar ("Improving Fable 5's biology safeguards", "Mariano-Florentino (Tino) Cuéllar to join Anthropic…", "Investigating three real-world incidents in our cybersecurity evaluations"). No son parte del anuncio. Se ignoran.
8. **El asset se guardó sin extensión.** La captura bajó la imagen de cabecera como `image.bin` porque la URL de Next.js (`/_next/image?url=…&w=3840&q=75`) no expone extensión. El archivo es en realidad **WebP** y se copió a la carpeta compañera con la extensión corregida (`image.webp`).

## Images / diagrams

Un solo asset: la imagen de cabecera del anuncio. **No hay ningún diagrama de arquitectura** — el anuncio describe la arquitectura cliente/servidor en una sola oración de prosa y nunca la dibuja. Si el deck muestra un diagrama de arquitectura MCP, no viene de esta fuente.

### `mcp-anuncio-anthropic-2024.web/images/image.webp`
- **Provenance**: `https://www.anthropic.com/_next/image?url=…3aabd8804251c0364cbde9d2e4be6dc8e8c2faec-2880x1620.png&w=3840&q=75`, con `alt="An abstract illustration of critical context connecting to a central hub"`. Imagen de cabecera del post, 2880×1620. Descargada como `image.bin` (sin extensión, por la URL del optimizador de imágenes de Next.js); es WebP y se guardó con la extensión corregida. 121.942 bytes.
- **Depiction**: ilustración abstracta apaisada sobre fondo naranja terracota con textura granulada. A la izquierda, una cuadrícula irregular de **nueve formas geométricas blancas** de bordes recortados a mano —un rombo, un cuadrado, triángulos apuntando en distintas direcciones, una forma lobulada, un óvalo, un reloj de arena— dispuestas en tres filas de tres, como piezas heterogéneas de un mosaico. A la derecha, separado por un espacio vacío, un **polígono blanco aislado** (casi circular, de muchos lados). Los dos grupos están unidos por una **gruesa barra negra horizontal terminada en dos círculos negros**, como una mancuerna o un conector físico: un extremo apoya sobre el bloque de formas heterogéneas y el otro sobre la forma aislada.
- **Why it matters**: es la metáfora visual del anuncio y es literalmente el argumento de MCP en una imagen — muchas fuentes de datos distintas y disímiles a un lado, un modelo al otro, **un único conector** entre ambos. Sirve como imagen de portada del bloque MCP del deck. El `alt` oficial de Anthropic ("An abstract illustration of critical context connecting to a central hub") confirma la lectura. Ojo con una sutileza: la imagen sugiere **un** conector, no un protocolo con N implementaciones, así que no ilustra el argumento N+M por sí sola.
- **Transcribed text**: ninguno. La ilustración es puramente gráfica, sin tipografía.

## Raw / preserved excerpts

**Apertura del anuncio (verbatim):**

> Today, we're open-sourcing the Model Context Protocol (MCP), a new standard for connecting AI assistants to the systems where data lives, including content repositories, business tools, and development environments. Its aim is to help frontier models produce better, more relevant responses.

**El diagnóstico (verbatim):**

> As AI assistants gain mainstream adoption, the industry has invested heavily in model capabilities, achieving rapid advances in reasoning and quality. Yet even the most sophisticated models are constrained by their isolation from data—trapped behind information silos and legacy systems. Every new data source requires its own custom implementation, making truly connected systems difficult to scale.
>
> MCP addresses this challenge. It provides a universal, open standard for connecting AI systems with data sources, replacing fragmented integrations with a single protocol. The result is a simpler, more reliable way to give AI systems access to the data they need.

**Sección "Model Context Protocol" (verbatim, completa — es toda la descripción técnica que da el anuncio):**

> The Model Context Protocol is an open standard that enables developers to build secure, two-way connections between their data sources and AI-powered tools. The architecture is straightforward: developers can either expose their data through MCP servers or build AI applications (MCP clients) that connect to these servers.
>
> Today, we're introducing three major components of the Model Context Protocol for developers:
>
> - The Model Context Protocol specification and SDKs
> - Local MCP server support in the Claude Desktop apps
> - An open-source repository of MCP servers
>
> Claude 3.5 Sonnet is adept at quickly building MCP server implementations, making it easy for organizations and individuals to rapidly connect their most important datasets with a range of AI-powered tools. To help developers start exploring, we're sharing pre-built MCP servers for popular enterprise systems like Google Drive, Slack, GitHub, Git, Postgres, and Puppeteer.

**Adoptantes tempranos (verbatim):**

> Early adopters like Block and Apollo have integrated MCP into their systems, while development tools companies including Zed, Replit, Codeium, and Sourcegraph are working with MCP to enhance their platforms—enabling AI agents to better retrieve relevant information to further understand the context around a coding task and produce more nuanced and functional code with fewer attempts.

**La visión de futuro (verbatim):**

> Instead of maintaining separate connectors for each data source, developers can now build against a standard protocol. As the ecosystem matures, AI systems will maintain context as they move between different tools and datasets, replacing today's fragmented integrations with a more sustainable architecture.

**Sección "Getting started" (verbatim, completa):**

> Developers can start building and testing MCP connectors today. All Claude.ai plans support connecting MCP servers to the Claude Desktop app.
>
> Claude for Work customers can begin testing MCP servers locally, connecting Claude to internal systems and datasets. We'll soon provide developer toolkits for deploying remote production MCP servers that can serve your entire Claude for Work organization.
>
> To start building:
>
> - Install pre-built MCP servers through the Claude Desktop app
> - Follow our quickstart guide to build your first MCP server
> - Contribute to our open-source repositories of connectors and implementations

**Sección "An open community" (verbatim, completa):**

> MCP was created at Anthropic by David Soria Parra and Justin Spahr-Summers. We're committed to building MCP as a collaborative, open-source project and ecosystem, and we're eager to hear your feedback. Whether you're an AI tool developer, an enterprise looking to leverage existing data, or an early adopter exploring the frontier, we invite you to build the future of context-aware AI together.
