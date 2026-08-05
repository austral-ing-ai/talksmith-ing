---
source_file: anthropic-docs-welcome
source_type: web-capture
ingested_at: 2026-08-05
---

# Intro to Claude — Claude Platform Docs

## Provenance
- Ubicación original: `research/web/anthropic-docs-welcome/`
- Formato: captura web (`original.html` 823.489 bytes + `page.md` 4.422 bytes)
- URL: https://platform.claude.com/docs/en/intro
- Autor / fuente: **Anthropic** (documentación oficial de producto)
- Fecha del original: no consta fecha de publicación ni de última actualización en la página
- Capturado el: 2026-08-05T12:19:56Z · HTTP 200
- `metadata.yaml` declara `assets: []`.
- **Nota de extracción:** la relación 823 KB de HTML → 4,4 KB de Markdown indica que la página es
  casi enteramente JavaScript y navegación. El `page.md` conserva el contenido sustantivo, pero
  arrastra basura de navegación al principio (una cadena de 16 repeticiones de "Loading" donde
  debería ir el índice lateral).

## Key claims

- Claude es descrito por Anthropic como *"a highly performant, trustworthy, and intelligent AI
  platform"*, que destaca en tareas de lenguaje, razonamiento, análisis y programación.
- **Generación actual de modelos Claude** según esta página:
  | Modelo | Descripción textual de la página |
  |---|---|
  | **Claude Fable 5** | "Next-generation intelligence for long-running agents." |
  | **Claude Mythos 5** | "Shares Claude Fable 5's capabilities without the safety classifiers. Available in limited release through Project Glasswing." |
  | **Claude Opus 5** | "For complex agentic coding and enterprise work." |
  | **Claude Sonnet 5** | "Frontier intelligence at scale, built for coding, agents, and enterprise workflows." |
  | **Claude Haiku 4.5** | "Fastest model with near-frontier intelligence." |
- Anthropic ofrece **dos formas de construir con Claude**, para casos de uso distintos:
  - **Messages API** — acceso directo de prompting al modelo. Mejor para *"custom agent loops and
    fine-grained control"*.
  - **Claude Managed Agents** — un harness de agente preconstruido y configurable que corre en
    infraestructura gestionada. Mejor para *"long-running tasks and asynchronous work"*.
- **Camino recomendado para desarrolladores nuevos**, en cinco pasos:
  1. Hacer la primera llamada a la API (configurar entorno, instalar un SDK, mandar el primer mensaje).
  2. **Asegurar las credenciales**: poner fecha de expiración al crear la API key; mantenerla fuera
     del control de versiones, del código de cliente y de los prompts; evaluar si la carga de trabajo
     puede usar **Workload Identity Federation** en lugar de una key estática.
  3. Entender la Messages API (estructura de request/response, conversaciones multi-turno, system
     prompts, stop reasons).
  4. Elegir el modelo adecuado comparando capacidad y costo.
  5. Explorar features y herramientas: extended thinking, búsqueda web, manejo de archivos, salidas
     estructuradas.
- **Herramientas de desarrollo**: Developer Console (con Workbench para prototipar prompts en el
  navegador), API Reference, Claude Cookbook (notebooks Jupyter interactivos sobre PDFs, embeddings).
- **Capacidades clave** que la página enumera: generación de texto y código (resumir, responder
  preguntas, extraer datos, traducir, explicar y generar código) y **visión** (procesar y analizar
  entrada visual, generar texto y código a partir de imágenes).
- Para chatear con Claude, la página deriva a claude.ai (producto de consumo, distinto de la API).

## Definitions and terminology

- **Messages API**: la interfaz de prompting directo. Unidad conceptual: el mensaje, con
  conversaciones multi-turno, system prompts y *stop reasons*.
- **Claude Managed Agents**: harness de agente gestionado por Anthropic. La distinción frente a la
  Messages API es de responsabilidad operativa: quién corre el bucle del agente.
- **Workload Identity Federation**: alternativa a la API key estática para autenticación de cargas
  de trabajo. La página la recomienda cuando es posible.
- **Extended thinking**: feature listada entre las capacidades a explorar; no definida en esta página.
- **Stop reasons**: parte del contrato de respuesta de la Messages API.
- **Workbench**: entorno del Developer Console para prototipar y probar prompts en el navegador.

## Evidence and examples

Ninguna. **La página no contiene benchmarks, cifras de rendimiento, precios ni comparaciones
cuantitativas.** Es una página de bienvenida de documentación: describe la oferta y enruta a otras
páginas. Todos los datos duros están detrás de los enlaces que no fueron capturados
(`/docs/en/about-claude/models/overview`, el anuncio de cada modelo, etc.).

## Inconsistencies / open questions

- **Sin fecha.** La página no declara fecha de publicación ni de última actualización. Como es
  documentación de producto viva, su contenido cambia sin aviso: la única fecha confiable es la de
  captura (**2026-08-05**). Cualquier diapositiva que use esta lista de modelos debe fecharla.
- **La nomenclatura de modelos de esta captura es inusual.** "Claude Fable 5" y "Claude Mythos 5" no
  siguen el esquema Opus/Sonnet/Haiku del resto de la familia, y "Mythos 5" se describe como
  compartiendo capacidades con Fable 5 *"without the safety classifiers"*, en release limitada a
  través de algo llamado "Project Glasswing". **Se registra tal cual está en la fuente.** Antes de
  llevar esto a una diapositiva conviene verificarlo contra otra fuente: es el tipo de afirmación que,
  si está mal, se nota.
- **La lista de modelos convive mal consigo misma.** Se anuncia como "la última generación" pero
  incluye Haiku 4.5, de la generación anterior. La página no explica el criterio.
- **Contenido de una sola cara.** Es material de marketing técnico del proveedor. No hay
  comparaciones con competidores, ni limitaciones, ni casos en los que Claude no sea la opción
  adecuada. Sirve para describir la oferta de Anthropic; no sirve como evidencia de rendimiento
  relativo.
- **Enlaces no capturados.** Todo el detalle (overview de modelos, guía de autenticación, guía de
  Messages API, features) queda fuera. Esta captura es un índice, no el contenido.
- Ruido de extracción: la cadena "MessagesIntro to ClaudeLoadingLoading…" al inicio del `page.md` es
  el índice lateral sin renderizar.

## Images / diagrams

Ninguna. `metadata.yaml` declara `assets: []`. La carpeta companion
`anthropic-docs-welcome.web/images/` existe y está vacía.

## Raw / preserved excerpts

Bloque de modelos, verbatim:

> The latest generation of Claude models:
>
> **Claude Fable 5** - Next-generation intelligence for long-running agents. Read the [Claude Fable 5 and Claude Mythos 5 announcement](https://www.anthropic.com/news/claude-fable-5-mythos-5).
>
> **Claude Mythos 5** - Shares Claude Fable 5's capabilities without the safety classifiers. Available in limited release through [Project Glasswing](https://anthropic.com/glasswing).
>
> **Claude Opus 5** - For complex agentic coding and enterprise work. Read the [Claude Opus 5 announcement](https://www.anthropic.com/news/claude-opus-5).
>
> **Claude Sonnet 5** - Frontier intelligence at scale, built for coding, agents, and enterprise workflows. Read the [Claude Sonnet 5 announcement](https://www.anthropic.com/news/claude-sonnet-5).
>
> **Claude Haiku 4.5** - Fastest model with near-frontier intelligence. Read the [Claude Haiku 4.5 announcement](https://www.anthropic.com/news/claude-haiku-4-5).

Descripción de producto, verbatim:

> Claude is a highly performant, trustworthy, and intelligent AI platform built by Anthropic. Claude excels at tasks involving language, reasoning, analysis, coding, and more.

Comparación Messages API vs. Managed Agents, verbatim (la tabla llega aplanada desde el HTML):

> Messages APIClaude Managed Agents**What it is**Direct model prompting accessPre-built, configurable agent harness that runs in managed infrastructure**Best for**Custom agent loops and fine-grained controlLong-running tasks and asynchronous work

Paso 2 del camino recomendado, verbatim:

> Secure your credentials
>
> Set an expiration when you create your API key. Keep the key out of source control, client-side code, and prompts. Check whether your workload can use Workload Identity Federation instead of a static key.

Capacidades clave, verbatim:

> Claude can assist with many tasks that involve text, code, and images.
>
> [Text and code generation] Summarize text, answer questions, extract data, translate text, and explain and generate code.
>
> [Vision] Process and analyze visual input and generate text and code from images.
