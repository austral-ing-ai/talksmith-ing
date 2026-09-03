---
source_file: mcp-registro-mcp-so
source_type: web-capture
ingested_at: 2026-08-14
---

# MCP.so — MCP Marketplace (portada)

## Provenance
- Original location: `research/web/mcp-registro-mcp-so/`
- Format: html (portada de un sitio de directorio). Texto tomado de `page.md` (~16.300 caracteres, 71 encabezados). La extracción es funcional pero **ruidosa por naturaleza de la fuente**: es una home page de listados, así que `page.md` es mayormente una sucesión de tarjetas (imagen + título + descripción truncada + antigüedad + contador) con el markup colapsado. No se perdió contenido sustantivo; simplemente no hay mucho contenido sustantivo que perder fuera del FAQ.
- URL: **https://mcp.so**
- Título declarado por el sitio: **"MCP.so - MCP Marketplace"**.
- Autor / fuente: operadores de mcp.so. No se identifica ninguna persona ni organización en la portada.
- Fecha del original: sin fecha de publicación (es una home dinámica). Las antigüedades relativas de las tarjetas ("Added in 1 hour", "Added 2 days ago", "Added last month") fechan la captura, no el sitio.
- HTTP status: 200. `fetched_at`: 2026-08-14T16:57:14Z.

## ⚠️ Corrección de atribución: mcp.so NO es el registro oficial de MCP

**El deck la llama "registro oficial MCP". La página dice de sí misma otra cosa, en dos lugares distintos y de forma inequívoca:**

1. **El `<title>` de la página es `MCP.so - MCP Marketplace`.** No dice "registry", no dice "official". Dice *marketplace*.
2. **El FAQ de la propia página, pregunta 7, verbatim:**

   > **What is mcp.so?**
   > mcp.so is a **community-driven platform** that collects and organizes **third-party** MCP Servers. It serves as a central directory where users can discover, share, and learn about various MCP Servers available for AI applications.

   "Community-driven", "third-party", "directory". Ninguna palabra sugiere carácter oficial.

3. **El mecanismo de admisión confirma que es comunitario y sin curaduría formal** (FAQ 8, verbatim): *"You can submit your MCP Server by creating a new issue in our GitHub repository. Click the 'Submit' button in the navigation bar or visit our GitHub issues page directly."* — se ingresa abriendo un issue.

4. **La página vende publicidad.** La barra de navegación tiene un enlace **"Advertise"** junto a "Submit". Los listados están segmentados en "Featured" (con la etiqueta "Featured" visible sobre la primera tarjeta) frente a "Trending" y "New arrivals". Es un marketplace con inventario promocionado, no un registro neutral.

5. **Otra fuente del corpus lo distingue explícitamente del registro oficial.** `mcp-servers-skillsplayground.web.md`, en su sección "Where to Find MCP Servers", enumera por separado: *"Official MCP Registry — The canonical registry at `registry.modelcontextprotocol.io` with 5,000+ servers"*, "Smithery", y su propio directorio. **El registro oficial vive en `registry.modelcontextprotocol.io`, no en mcp.so.**

**Conclusión: la atribución del deck es incorrecta.** mcp.so es un marketplace comunitario de terceros, autodescrito como tal. Llamarlo "registro oficial" le adjudica una autoridad que la propia página no reclama y que corresponde a otro dominio. Si el deck necesita nombrar el registro oficial, el dominio es `registry.modelcontextprotocol.io` — que, además, **no está capturado en este corpus** (ver la nota sobre la spec faltante en `mcp-anuncio-anthropic-2024.web.md`).

## Key claims

- **Autodescripción**: plataforma comunitaria que colecta y organiza servidores MCP de terceros; directorio central para descubrir, compartir y aprender sobre servidores MCP.
- **Propuesta de valor de la portada (verbatim)**: *"Discover useful MCP servers — Connect AI apps to tools, data, and automated workflows."*
- **El sitio se posiciona con múltiples etiquetas simultáneas**: "MCP store", "MCP server list", "curated directory", "MCP marketplace". Del texto de posicionamiento SEO, verbatim: *"Use MCP.so as an MCP store, MCP server list, and curated directory for awesome MCP servers."*
- **El catálogo no es sólo de servidores.** La portada organiza **cinco** tipos de entidad, lo cual es un dato interesante sobre hacia dónde va el ecosistema: **servers**, **clients** (apps, IDEs y frameworks que hablan MCP), **CLI tools**, **loops** (prompts y flujos reutilizables para agentes de código) y **Agent Skills** (Claude Skills, Codex Skills y capacidades reutilizables).
- **Cinco categorías principales declaradas**: Developer Tools, AI & Agents, Cloud & Infrastructure, Memory & Knowledge, Media & Design.
- **El FAQ reproduce la definición estándar de MCP**, atribuyéndola correctamente a Anthropic: protocolo open source que permite a sistemas de IA conectarse de forma segura a distintas fuentes de datos, con arquitectura cliente-servidor.
- **Afirmación de seguridad del FAQ**, que conviene mirar con cuidado (ver `Inconsistencies`): *"Yes, security is built into the MCP protocol. Server controls its own resources, there's no need to share API keys with LLM providers, and the system maintains clear boundaries."*
- **Afirmación desactualizada del FAQ**: *"Currently, this works with local MCP servers, with enterprise remote server support coming soon."*

## Definitions and terminology

**MCP, según el FAQ del sitio (verbatim):** *"MCP is an open-source protocol developed by Anthropic that enables AI systems like Claude to securely connect with various data sources. It provides a universal standard for AI assistants to access external data, tools, and prompts through a client-server architecture."*

**MCP Server, según el FAQ (verbatim):** *"MCP Server is a system that provides context, tools, and prompts to AI clients. It can expose data sources like files, documents, databases, and API integrations, allowing AI assistants to access real-time information in a secure way."*

**Cómo funcionan, según el FAQ (verbatim):** *"MCP Server work through a simple client-server architecture. They expose data and tools through a standardized protocol, maintaining secure 1:1 connections with clients inside host applications like Claude Desktop."* — la relación **1:1 entre servidor y cliente dentro de una aplicación anfitriona** es el detalle técnico más específico de toda la página.

**Qué provee un servidor, según el FAQ**: **resources** (archivos, documentos, datos), **tools** (integraciones de API, acciones) y **prompts** (interacciones plantilladas). Es la tríada canónica de MCP, aunque acá venga de una fuente no oficial.

**Clients (en la taxonomía del sitio).** Apps, IDEs y frameworks que hablan MCP. El sitio los subclasifica con etiquetas como "Web Chat & UIs" y "Other".

**Loops.** Categoría propia del sitio: *"Reusable prompts and workflows for coding agents"*. Los ejemplos capturados tienen un patrón de nombre revelador — todos son bucles con condición de salida: `a11y-audit-until-clean`, `build-until-green`, `coverage-until-threshold`, `ci-failure-watcher`. Se etiquetan por modo de disparo: `manual` o `interval`.

**Agent Skills.** Categoría del sitio para Claude Skills, Codex Skills y capacidades reutilizables. Las cuatro capturadas pertenecen todas a la misma colección (`obra / superpowers`) y se categorizan como "Agent workflows".

## Evidence and examples

**Escala del ecosistema visible en la captura.** La portada **no publica un total de servidores**. Sólo muestra selecciones. Lo que sí da son contadores por servidor (presumiblemente estrellas o instalaciones) y antigüedades.

**Servidores destacados (Featured), con sus descripciones y contadores:**

| Servidor | Autor / org | Qué hace (según la tarjeta) | Antigüedad | Contador |
|---|---|---|---|---|
| **Subtext** | Subtext by Fullstory | "Session replay, built for agents. Subtext is agentic session review: it captures production sessions of your app and connects them to your coding agent — Claude Code, Cursor, Codex, Devin, your own harness" | 24 días | 9 |
| **Clipkit** | clipkit-video | "The video infra for AI agents: compose motion-graphics video from one JSON document (open Clipkit Protocol), validate before it costs anything, preview stills in-chat, and render deterministic MP4s on a GPU runtime." | 2 días | 11 |
| **OrangePro** | Aamir Siddiqui | "OrangePro local-first CLI + MCP server for behavior mapping, grounded test generation, and dynamic proof." | 14 días | 12 |
| **Capital.com MCP** | capital-com-sv | Descripción truncada por el disclaimer regulatorio: "CFDs are complex instruments and come with a high risk of losing money rapidly due to leverage. 81.31% of retail investor accounts lose money when trading CFDs with this provider." | 24 días | 4 |
| **Local YDB MCP** | astandrik | "Safety-first stdio MCP server with **38 tools** for operating Docker-based local-ydb environments locally or over SSH." | 13 días | 4 |
| **scvd.store** | seancrecord | "The trust layer of the x402 economy. Free conformance checking for any issuer's x402 signed offers and receipts. Settlement attestation on Base and Solana. Weekly signed, Bitcoin-anchored ecosystem corpus." | 4 días | 2 |
| **CoinLobster** | CoinLobster | "The only MCP server with live whale trades across 15 exchanges plus on-chain DEX flow. Smart Money Radar, real liquidations and outcome-scored signals. No API key required." | 1 día | 3 |
| **Asana** | Asana | "Tasks, projects, workspaces" | último mes | — |
| **Cello MCP** | Cello | "Connect Cello MCP to build and scale your referral, partner, or affiliate programs without leaving the conversation." | 10 días | — |

**Dato aprovechable para el bloque de selección de herramientas**: **Local YDB MCP declara 38 herramientas en un solo servidor.** Contrastar con la mediana de 4 y la recomendación de OpenAI de menos de 20 documentadas en `tool-space-interference-msr.web.md`. Es un ejemplo concreto y fechado de un servidor que excede la recomendación, encontrado al azar en la portada de un directorio.

**Tendencias de la semana (Trending this week — "What the community is installing"):**

| Servidor | Contador | Nota |
|---|---|---|
| **Medplum** | 2.5K | "Medplum is a healthcare platform that helps you quickly develop high-quality compliant applications." **El único de temática biomédica en toda la portada** — relevante para el curso. |
| **PLUR** | 226 | "AI agents start every session with amnesia — you re-explain the project, repeat your preferences, and correct the same mistakes over and over. PLUR gives them a memory that persists." |
| **Termany** | 174 | "Agent-Native Terminal" |
| **LocalCan** | 82 | "Gives AI agents public URLs (tunnels) for localhost, live HTTP traffic inspection, snapshot publishing, and access control." |
| OrangePro | 12 | (también en Featured) |
| Clipkit | 11 | (también en Featured) |
| Subtext | 9 | (también en Featured) |
| Local YDB MCP | 4 | (también en Featured) |

**Novedades (New arrivals):** Snipara ("MCP connector for Snipara, the Project Brain for AI coding agents", 7 horas), **BlazingCDN** (1 hora), **easydocforms** (13 horas — "MCP server for healthcare intake forms — import a blank PDF, hand the patient a hosted fill link, retrieve the completed PDF. **PHI never enters agent context.**"), FARPY (24 horas), CoinLobster, Clipkit, directree, NERAI Risk Intelligence.

**`easydocforms` merece atención especial para este curso**: es un caso de MCP en salud con una decisión de diseño de privacidad explícita — "PHI never enters agent context". Es el ejemplo más directamente aplicable a biomedicina de toda la portada.

**Clientes destacados**: FormLM, Banks to AI (upx.com — "secure, read-only access to real bank data — 12,000+ financial institutions"), APIMart (apimart.ai), PoYo.ai ("one API key for 500+ AI models").

**Herramientas CLI destacadas** (todas etiquetadas "Official"): **Bun** (`$ bun`), **Cloudflare Wrangler** (`$ wrangler`), **DuckDB CLI** (`$ duckdb`), **FFmpeg** (`$ ffmpeg`).

**Loops destacados**: `a11y-audit-until-clean` (Quality, manual), `build-until-green` (Testing, manual), `coverage-until-threshold` (Testing, manual — "Add focused tests until coverage meets your threshold (e.g. 80%)"), `ci-failure-watcher` (CI, interval).

**Agent Skills destacadas** (las cuatro de `obra / superpowers`): `brainstorming`, `systematic-debugging`, `writing-plans`, `using-superpowers`.

## Inconsistencies / open questions

1. **La atribución del deck es incorrecta: no es el registro oficial.** Ver el bloque de advertencia arriba. Es marketplace comunitario de terceros, autodescrito así en su propio FAQ, y el registro oficial está en otro dominio (`registry.modelcontextprotocol.io`).
2. **La portada no publica ningún total.** No hay un "N servidores" en ninguna parte de la página. Si el deck cita un número de servidores atribuido a mcp.so, ese número **no está en esta captura**. Los únicos totales del corpus son los de `mcp-servers-skillsplayground.web.md`: 890+ (su propio directorio), 5.000+ (registro oficial), 3.600+ (Smithery) — y ese sitio se fecha a sí mismo en febrero de 2026.
3. **Conflicto de interés estructural.** El sitio vende publicidad ("Advertise" en la barra de navegación) y destaca inventario ("Featured", "Hand-picked, production-ready"). Un directorio con posiciones pagas no es una fuente neutral sobre qué servidores son importantes. Cualquier ranking tomado de acá debe presentarse con esa salvedad.
4. **La afirmación de seguridad del FAQ es demasiado fuerte.** *"Yes, security is built into the MCP protocol"* choca de frente con lo que documenta `tool-space-interference-msr.web.md`, que registra ausencia de namespaces formales (imposibilidad de desambiguar herramientas homónimas de servidores distintos), errores señalizados como éxitos, y ausencia de convenciones para compartir recursos. Y choca con `langchain-rag-tutorial.web.md`, que advierte que **ningún prompt ni delimitador previene de forma confiable la inyección indirecta de prompts**. La afirmación del FAQ es marketing, no análisis de seguridad, y no debería citarse en una slide sobre seguridad de MCP.
5. **El FAQ está desactualizado.** *"Currently, this works with local MCP servers, with enterprise remote server support coming soon"* describe el estado de noviembre de 2024 (es casi literalmente lo que decía el anuncio original de Anthropic). En la captura de agosto de 2026 la propia portada lista clientes y servidores remotos. **El FAQ no se actualizó; los listados sí.** Es un indicador de la calidad de mantenimiento del sitio.
6. **Ninguna entrada tiene fecha absoluta.** Todo es relativo ("Added 2 days ago", "Added last month"), lo que hace que la página no sea citable sin adjuntar la fecha de captura (2026-08-14). Cualquier slide que muestre este contenido tiene que llevar el "a la fecha de".
7. **Los contadores no están etiquetados.** Cada tarjeta muestra un número (9, 11, 12, 2.5K…) sin decir de qué. Podrían ser estrellas de GitHub, instalaciones, o visitas. No se puede citar como métrica de adopción sin saber qué mide.
8. **La calidad del catálogo es visiblemente heterogénea.** Conviven Asana y Medplum con servidores de dos días y contador 2. Hay una densidad notable de cripto y finanzas especulativas (CoinLobster, scvd.store/x402, Capital.com con su disclaimer de que el 81,31 % de las cuentas minoristas pierden dinero). Es un dato honesto sobre el estado del ecosistema, y una razón más para no presentar el sitio como autoridad.
9. **Cuatro imágenes no se pudieron descargar.** `metadata.yaml` registra cuatro assets con `skipped: "fetch-failed: HTTPError"`, todos avatares de organización de GitHub (`github.com/oven-sh.png`, `cloudflare.png`, `duckdb.png`, `FFmpeg.png`) correspondientes a las cuatro CLI tools destacadas. Son logos decorativos; no se perdió contenido.
10. **Ocho imágenes se descargaron sin extensión.** Los avatares de GitHub (`avatars.githubusercontent.com/u/...?v=4`) se guardaron como `.bin`. Se copiaron a la carpeta compañera con la extensión real detectada por contenido (PNG o JPEG).
11. **`metadata.yaml` lista assets duplicados.** Varias entradas llevan `deduped: True` porque la misma imagen aparece dos veces en la página (una vez en "Featured servers" y otra en "Trending this week"). La carpeta compañera tiene una sola copia de cada una: 24 archivos únicos.

## Images / diagrams

24 archivos únicos. **Ninguno tiene contenido técnico**: son todos logotipos de producto y avatares de organización de las tarjetas del directorio, más el logo del sitio. No hay diagramas, gráficos ni capturas de pantalla. La utilidad para el deck es nula salvo como collage ilustrativo de "el ecosistema es grande y heterogéneo".

Se identifica cada archivo con el servidor/cliente al que corresponde según su posición en `page.md`.

### `mcp-registro-mcp-so.web/images/logo.png`
- **Provenance**: `https://mcp.so/logo.png`, `alt="MCP.so"`. Logo del sitio, barra de navegación. 28.800 bytes.
- **Depiction**: sobre fondo blanco azulado muy claro, una **letra "M" mayúscula azul marino de trazo grueso, encerrada en un marco cuadrado de esquinas redondeadas** del mismo color. El marco está interrumpido: le faltan segmentos en la esquina superior derecha y en la inferior izquierda, con dos trazos diagonales cortos que sugieren un corte.
- **Why it matters**: identifica la fuente. Útil sólo si una slide muestra el logo del directorio.
- **Transcribed text**: `M`.

### `mcp-registro-mcp-so.web/images/c186c0c154579cd73196bf7a5063b45a.png`
- **Provenance**: `https://cdn.mcp.so/uploads/…`, `alt=""`. Logo de **Subtext (by Fullstory)**, primer servidor destacado. 9.646 bytes.
- **Depiction**: sobre fondo blanco, una **"S" estilizada compuesta por tres bandas paralelas en diagonal**, las dos superiores en negro y la inferior en rosa fucsia.
- **Why it matters**: ninguna.
- **Transcribed text**: ninguno.

### `mcp-registro-mcp-so.web/images/a87f3fcd83addd468e032cc8d5b6003e.svg`
- **Provenance**: `https://cdn.mcp.so/uploads/…`, `alt=""`. Logo de **OrangePro**. 286 bytes — el asset más liviano de la captura.
- **Depiction**: SVG de 200×200 con tres elementos, legibles directamente en el código fuente: un **cuadrado de fondo negro** (`#050505`) que ocupa todo el lienzo, una **circunferencia blanca de trazo grueso** (radio 70, sin relleno, `stroke-width` 8) centrada, y en el centro un **círculo pequeño relleno naranja intenso** (`#FF4500`, radio 14). Visualmente: una diana o un ojo.
- **Why it matters**: ninguna.
- **Transcribed text**: ninguno (el SVG no contiene elementos de texto).

### `mcp-registro-mcp-so.web/images/6753a6798ace8ce5babe213dc8519a75.png`
- **Provenance**: `https://cdn.mcp.so/uploads/…`, `alt=""`. Logo de **Local YDB MCP**. 12.211 bytes.
- **Depiction**: cuadrado negro de esquinas muy redondeadas con una **"Y" mayúscula azul brillante** de trazo grueso, centrada.
- **Why it matters**: ninguna, salvo que identifica el servidor de 38 herramientas citado arriba.
- **Transcribed text**: `Y`.

### `mcp-registro-mcp-so.web/images/73e9663f1831a9db00cc41d2d3e39886.png`
- **Provenance**: `https://cdn.mcp.so/uploads/…`, `alt=""`. Logo de **scvd.store**. 577.267 bytes — el segundo asset más pesado.
- **Depiction**: sobre fondo blanco, la **silueta de un dinosaurio tipo tiranosaurio en marrón oscuro**, mirando a la izquierda, con las fauces abiertas y dientes visibles. Debajo, el texto **"scvd.store"** en tipografía serif marrón.
- **Why it matters**: ninguna.
- **Transcribed text**: `scvd.store`.

### `mcp-registro-mcp-so.web/images/asana-logo.svg`
- **Provenance**: `https://svgl.app/library/asana-logo.svg`, `alt=""`. Logo de **Asana**. 614 bytes.
- **Depiction**: SVG con un único trazado en color coral (`#F06A6A`): **tres círculos dispuestos en triángulo** — uno arriba al centro y dos abajo, a izquierda y derecha. Es el logotipo corporativo de Asana.
- **Why it matters**: ninguna. Es el único servidor de una marca empresarial ampliamente conocida entre los destacados.
- **Transcribed text**: ninguno.

### `mcp-registro-mcp-so.web/images/9e9b1c9484d705fb14961cc0e1498596.png`
- **Provenance**: `https://cdn.mcp.so/uploads/…`, `alt=""`. Logo de **Cello MCP**. 16.827 bytes.
- **Depiction**: sobre fondo blanco, una **forma de "C" o de dos anillos entrelazados en violeta azulado**, de trazo muy grueso, con la abertura hacia la derecha.
- **Why it matters**: ninguna.
- **Transcribed text**: ninguno.

### `mcp-registro-mcp-so.web/images/296988713.png`
- **Provenance**: `https://avatars.githubusercontent.com/u/296988713?v=4`, `alt=""`. Avatar de GitHub de **clipkit-video (Clipkit)**. Descargado como `.bin`; es PNG. 4.623 bytes.
- **Depiction**: cuadrado de fondo negro con **tres rectángulos redondeados apilados en escalera**, desplazados horizontalmente: el superior blanco, el del medio amarillo/ámbar, el inferior rojo. Evoca pistas de una línea de tiempo de edición de video.
- **Why it matters**: ninguna.
- **Transcribed text**: ninguno.

### `mcp-registro-mcp-so.web/images/101812180.png`
- **Provenance**: `https://avatars.githubusercontent.com/u/101812180?v=4`, `alt=""`. Avatar de **capital-com-sv (Capital.com MCP)**. Descargado como `.bin`; es PNG. 5.947 bytes.
- **Depiction**: sobre fondo blanco, el wordmark **"capital·com"** en tipografía sans-serif negra de peso alto, con un punto medio separando las dos palabras.
- **Why it matters**: ninguna.
- **Transcribed text**: `capital.com`.

### `mcp-registro-mcp-so.web/images/310856622.png`
- **Provenance**: `https://avatars.githubusercontent.com/u/310856622?v=4`, `alt=""`. Avatar de **CoinLobster**. Descargado como `.bin`; es PNG. 131.902 bytes.
- **Depiction**: ilustración de caricatura sobre círculo celeste: una **langosta naranja antropomórfica**, sonriente, con ojos grandes y pinzas levantadas, tocada con una **galera negra** en cuyo frente hay una **moneda dorada con el símbolo de Bitcoin (₿)**.
- **Why it matters**: ninguna para el contenido. Sirve, si acaso, como ilustración del tono del ecosistema de servidores cripto en el directorio.
- **Transcribed text**: `₿` (símbolo de Bitcoin en la galera).

### `mcp-registro-mcp-so.web/images/d1341762da73dfa75d09dca3c073ac88.png`
- **Provenance**: `https://cdn.mcp.so/uploads/…`, `alt=""`. Logo de **FormLM**, primer cliente destacado. 1.807 bytes.
- **Depiction**: cuadrado naranja intenso con esquinas ligeramente redondeadas, y en el centro una **forma blanca de cuadrilátero irregular** que sugiere una hoja de papel en perspectiva o una puerta abierta.
- **Why it matters**: ninguna.
- **Transcribed text**: ninguno.

### `mcp-registro-mcp-so.web/images/8cdb222cfc33889eeb289c05bf7d8a10.jpg`
- **Provenance**: `https://cdn.mcp.so/uploads/…`, `alt=""`. Logo de **Banks to AI (upx.com)**, cliente destacado. 24.210 bytes.
- **Depiction**: sobre fondo blanco, el wordmark **"UPX"** en mayúsculas de trazo grueso; "UP" en azul marino y la "X" en degradado de verde azulado a verde, formada por dos trazos que se cruzan.
- **Why it matters**: ninguna.
- **Transcribed text**: `UPX`.

### `mcp-registro-mcp-so.web/images/82ea0d0f20e13c828479a07cc5ea6716.jpg`
- **Provenance**: `https://cdn.mcp.so/uploads/…`, `alt=""`. Logo de **APIMart (apimart.ai)**, cliente destacado. 49.165 bytes.
- **Depiction**: sobre fondo blanco casi puro, una **"M" mayúscula grande en negro**, de estilo geométrico, construida con líneas paralelas dobles que dejan ver el fondo entre ellas.
- **Why it matters**: ninguna.
- **Transcribed text**: `M`.

### `mcp-registro-mcp-so.web/images/732581d3c1b54526ef807d71e79d47e1.webp`
- **Provenance**: `https://cdn.mcp.so/uploads/…`, `alt=""`. Logo de **PoYo.ai**, cliente destacado. 47.780 bytes.
- **Depiction**: cuadrado de fondo negro con las letras **"PY"** en blanco, de gran tamaño y tipografía geométrica condensada, ocupando casi todo el lienzo.
- **Why it matters**: ninguna.
- **Transcribed text**: `PY`.

### `mcp-registro-mcp-so.web/images/75462971.png`
- **Provenance**: `https://avatars.githubusercontent.com/u/75462971?v=4`, `alt=""`. Avatar de **Medplum**, el servidor más popular de "Trending" (2.5K). Descargado como `.bin`; es PNG. 8.873 bytes.
- **Depiction**: cuadrado de fondo violeta intenso con un ícono blanco centrado: una **manzana estilizada con una hoja**, y dentro de ella una **cruz médica**.
- **Why it matters**: es el único servidor de temática **biomédica** entre los destacados y tendencias, y por lejos el más popular de la portada (2.5K). Si el deck quiere un ejemplo de MCP aplicado a salud, Medplum es el candidato que este directorio ofrece.
- **Transcribed text**: ninguno.

### `mcp-registro-mcp-so.web/images/9e58505c6cb490cc371926850626936c.png`
- **Provenance**: `https://cdn.mcp.so/uploads/…`, `alt=""`. Logo de **PLUR**. 81.375 bytes.
- **Depiction**: cuatro **círculos de colores etiquetados con las letras P, L, U y R**, unidos por segmentos cortos formando una cadena en zigzag, al estilo de un diagrama de estructura molecular. La "P" es celeste, la "L" naranja, la "U" violeta y la "R" verde.
- **Why it matters**: ninguna, salvo que ilustra un servidor de memoria persistente, tema adyacente a RAG.
- **Transcribed text**: `P` · `L` · `U` · `R`.

### `mcp-registro-mcp-so.web/images/c9c490b994c82c8c4fe1b1e3efc24dd0.png`
- **Provenance**: `https://cdn.mcp.so/uploads/…`, `alt=""`. Logo de **Termany**. 22.643 bytes.
- **Depiction**: cuadrado de esquinas redondeadas con **degradado de celeste a verde agua**, y en el centro el ícono de una **ventana de terminal** en trazo negro: un rectángulo con barra de título, dentro del cual se ven un símbolo de prompt (`>_`) y una línea horizontal verde.
- **Why it matters**: ninguna.
- **Transcribed text**: `>_` (símbolo de prompt dentro del ícono).

### `mcp-registro-mcp-so.web/images/159428968.png`
- **Provenance**: `https://avatars.githubusercontent.com/u/159428968?v=4`, `alt=""`. Avatar de **LocalCan**. Descargado como `.bin`; es PNG. 39.861 bytes.
- **Depiction**: sobre fondo negro con un resplandor cálido difuso en la base, un **cilindro en perspectiva dibujado con trazo fino en degradado violeta-rosa-naranja**, con la elipse superior visible. Es el ícono convencional de base de datos, renderizado con estética neón.
- **Why it matters**: ninguna.
- **Transcribed text**: ninguno.

### `mcp-registro-mcp-so.web/images/e45fc107af19de98735b6d9566855195.png`
- **Provenance**: `https://cdn.mcp.so/uploads/…`, `alt=""`. Logo de **Snipara**, la novedad más reciente ("Added in 7 hours"). 24.692 bytes.
- **Depiction**: sobre fondo blanco, una **"S" formada por dos trazos curvos gruesos en dos tonos de azul**, uno más oscuro arriba y otro más claro abajo, con las puntas redondeadas y separadas.
- **Why it matters**: ninguna.
- **Transcribed text**: ninguno.

### `mcp-registro-mcp-so.web/images/314216781.jpg`
- **Provenance**: `https://avatars.githubusercontent.com/u/314216781?v=4`, `alt=""`. Avatar de **BlazingCDN**. Descargado como `.bin`; es JPEG. 10.192 bytes.
- **Depiction**: rectángulo de fondo azul marino muy oscuro con el wordmark **"blazing"** en minúsculas blancas de tipografía redondeada. A la izquierda de la palabra, un pequeño **ícono naranja con líneas de velocidad** horizontales, sugiriendo movimiento rápido.
- **Why it matters**: ninguna.
- **Transcribed text**: `blazing`.

### `mcp-registro-mcp-so.web/images/316378971.png`
- **Provenance**: `https://avatars.githubusercontent.com/u/316378971?v=4`, `alt=""`. Avatar de **easydocforms**. Descargado como `.bin`; es PNG. 1.560 bytes.
- **Depiction**: sobre fondo blanco, una **forma pixelada verde claro** compuesta por bloques cuadrados, que sugiere una letra estilizada o un glifo tipo QR de baja resolución.
- **Why it matters**: identifica el servidor de formularios de admisión clínica con la política "PHI never enters agent context", que es el ejemplo biomédico más pertinente de la portada.
- **Transcribed text**: ninguno.

### `mcp-registro-mcp-so.web/images/49634116.png`
- **Provenance**: `https://avatars.githubusercontent.com/u/49634116?v=4`, `alt=""`. Avatar de **serkvay13 (NERAI Risk Intelligence)**. Descargado como `.bin`; es PNG. 1.557 bytes.
- **Depiction**: sobre fondo blanco, una **forma pixelada violeta** de bloques cuadrados, de estructura similar a la anterior pero distinto patrón. Tiene el aspecto de un avatar generado proceduralmente (tipo identicon).
- **Why it matters**: ninguna.
- **Transcribed text**: ninguno.

### `mcp-registro-mcp-so.web/images/6cf12be2b766c0a6d89c0dc9bd7f6da7.png`
- **Provenance**: `https://cdn.mcp.so/uploads/…`, `alt=""`. Logo de **FARPY (Mangomunchr)**. **911.591 bytes — el asset más pesado de toda la captura**, para un logo de tarjeta.
- **Depiction**: sobre fondo blanco, la fotografía recortada de un **hámster dorado** asomando por detrás del wordmark **"Farpy"**, escrito en tipografía sans-serif negra de peso muy alto con un pequeño "™". Debajo, en letras espaciadas más pequeñas, el eslogan **"TINY TAPS. BIG COMPUTE."**
- **Why it matters**: ninguna para el contenido. Es, eso sí, otro ejemplo del descuido de ingeniería que señala `tool-space-interference-msr.web.md`: casi un megabyte para una miniatura de directorio.
- **Transcribed text**: `Farpy` · `™` · `TINY TAPS. BIG COMPUTE.`

### `mcp-registro-mcp-so.web/images/b2b170f09d1630fa4063b777228d1d1b.png`
- **Provenance**: `https://cdn.mcp.so/uploads/…`, `alt=""`. Logo de **directree (coburn2716)**. 49.406 bytes.
- **Depiction**: cuadrado de fondo azul muy oscuro, casi negro, con un ícono centrado que sugiere un **árbol estilizado**: tres trazos anchos y curvos que ascienden y se abren en abanico, en tonos que van del dorado al rosa pálido de izquierda a derecha.
- **Why it matters**: ninguna.
- **Transcribed text**: ninguno.

## Raw / preserved excerpts

**Cabecera de la portada (verbatim):**

> # Discover useful MCP servers
>
> Connect AI apps to tools, data, and automated workflows.

**Barra de navegación (verbatim):**

> [MCP.so](/) Search MCP servers, tools, integrations…⌘K [Advertise](/advertise) [Submit](/submit) Switch language Toggle theme [Sign In](/sign-in)

**Categorías principales (verbatim):**

> ## Top categories
> Developer Tools · AI & Agents · Cloud & Infrastructure · Memory & Knowledge · Media & Design

**Rótulos de sección (verbatim):**

> Featured servers — Hand-picked, production-ready
> Featured clients — Apps, IDEs, and frameworks that speak MCP
> Featured CLI tools — Official and agent-ready command-line tools for everyday workflows
> Featured loops — Reusable prompts and workflows for coding agents
> Featured Agent Skills — Popular Claude Skills, Codex Skills, and reusable capabilities for AI agents
> Trending this week — What the community is installing
> New arrivals — Recently published servers

**Bloque de posicionamiento SEO al pie (verbatim, completo):**

> ## Find MCP servers, clients, and integrations in one MCP marketplace
>
> Use MCP.so as an MCP store, MCP server list, and curated directory for awesome MCP servers. Browse servers for Claude, IDEs, automation, databases, search, files, and developer tools.
>
> **Search MCP servers** — Discover MCP servers by name, category, tag, runtime, or integration so you can connect AI apps to the tools and data you already use.
> **MCP server list** — Scan a practical MCP server list with popular, featured, and newly published projects from the community.
> **MCP store and tags** — Use tags to explore the MCP store by use case: search, databases, GitHub, browser automation, memory, cloud services, and more.
> **Awesome MCP servers and clients** — Compare awesome MCP servers with compatible MCP clients, IDEs, desktop apps, and agent tools that support the protocol.

**FAQ completo (verbatim) — es el único contenido expositivo de la página:**

> **1. What is MCP (Model Context Protocol)?**
> MCP is an open-source protocol developed by Anthropic that enables AI systems like Claude to securely connect with various data sources. It provides a universal standard for AI assistants to access external data, tools, and prompts through a client-server architecture.
>
> **2. What is MCP Server?**
> MCP Server is a system that provides context, tools, and prompts to AI clients. It can expose data sources like files, documents, databases, and API integrations, allowing AI assistants to access real-time information in a secure way.
>
> **3. How do MCP Server work?**
> MCP Server work through a simple client-server architecture. They expose data and tools through a standardized protocol, maintaining secure 1:1 connections with clients inside host applications like Claude Desktop.
>
> **4. What can MCP Server provide?**
> MCP Server can share resources (files, docs, data), expose tools (API integrations, actions), and provide prompts (templated interactions). They control their own resources and maintain clear system boundaries for security.
>
> **5. How does Claude use MCP?**
> Claude can connect to MCP server to access external data sources and tools, enhancing its capabilities with real-time information. Currently, this works with local MCP servers, with enterprise remote server support coming soon.
>
> **6. Is MCP Server secure?**
> Yes, security is built into the MCP protocol. Server controls its own resources, there's no need to share API keys with LLM providers, and the system maintains clear boundaries. Each server manages its own authentication and access control.
>
> **7. What is mcp.so?**
> mcp.so is a community-driven platform that collects and organizes third-party MCP Servers. It serves as a central directory where users can discover, share, and learn about various MCP Servers available for AI applications.
>
> **8. How can I submit my MCP Server to mcp.so?**
> You can submit your MCP Server by creating a new issue in our GitHub repository. Click the 'Submit' button in the navigation bar or visit our GitHub issues page directly. Please provide details about your server including its name, description, features, and connection information.

**Cierre de la página (verbatim):**

> ## Explore MCP Servers
> Start here to discover awesome MCP servers.
> [Submit Server](/submit) [View MCP Servers](/servers)
