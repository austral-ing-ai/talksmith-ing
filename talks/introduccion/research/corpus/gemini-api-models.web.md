---
source_file: gemini-api-models
source_type: web-capture
ingested_at: 2026-08-05
---

# Models — Gemini API (Google AI for Developers)

## Provenance
- Ubicación original: `research/web/gemini-api-models/`
- Formato: captura web (`original.html` 142.957 bytes + `page.md` 15.897 bytes + `assets/`)
- URL: https://ai.google.dev/gemini-api/docs/models
- Autor / fuente: **Google** (documentación oficial de la Gemini API)
- Fecha del original: la página declara **"Last updated 2026-08-04 UTC"** (un día antes de la captura)
- Capturado el: 2026-08-05T12:19:57Z · HTTP 200
- Licencia declarada: contenido bajo Creative Commons Attribution 4.0; ejemplos de código bajo
  Apache 2.0
- Extracción buena: el catálogo completo de modelos está presente. Arrastra el selector de idioma
  (22 idiomas) y el bloque de feedback al pie como ruido.

## Key claims

Es un **catálogo de modelos**, no un texto argumentativo. Su valor es doble: (a) inventario fechado
de la oferta de Google al 2026-08-04, y (b) el esquema de versionado, que es material conceptual
reutilizable.

**Aviso destacado en la página:** *"The Interactions API is now generally available. We recommend
using this API for access to all the latest features and models."*

### Familia Gemini 3

**Estables:**
| Modelo | Endpoint | Descripción de la página |
|---|---|---|
| Gemini 3.6 Flash | `gemini-3.6-flash` | "Our latest model that balances speed with intelligence to deliver strong performance in agentic and multimodal tasks." |
| Gemini 3.5 Flash | `gemini-3.5-flash` | "Most intelligent model for sustained frontier performance on agentic and coding tasks." |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | "Our fastest, most cost-effective 3.5 model for high-throughput execution." |
| Gemini 3.1 Flash-Lite | `gemini-3.1-flash-lite` | "Frontier-class performance rivaling larger models at a fraction of the cost." |
| Nano Banana 2 | `gemini-3.1-flash-image` | Generación y edición de imágenes de alta eficiencia, optimizada para velocidad y alto volumen. |
| Nano Banana 2 Lite | `gemini-3.1-flash-lite-image` | Latencia ultra baja y bajo costo para uso interactivo de alto volumen. |
| Nano Banana Pro | `gemini-3-pro-image` | "A professional design engine with a reasoning core for studio-quality 4K visuals, complex layouts, and precise text rendering." |

**En preview:**
| Modelo | Endpoint | Descripción |
|---|---|---|
| Gemini 3.1 Pro | `gemini-3.1-pro-preview` | "Advanced intelligence, complex problem-solving skills, and powerful agentic and vibe coding capabilities." |
| Gemini 3 Flash | `gemini-3-flash-preview` | Rendimiento frontier a fracción del costo. |
| Gemini 3.5 Live Translate | `gemini-3.5-live-translate-preview` | Traducción voz a voz en tiempo real, baja latencia, **70+ idiomas**. |
| Gemini 3.1 Flash Live | `gemini-3.1-flash-live-preview` | Audio-a-audio (A2A) para diálogo en tiempo real. |
| Gemini 3.1 Flash TTS | `gemini-3.1-flash-tts-preview` | Generación de voz de baja latencia, con "expressive audio tags". |
| Gemini Omni Flash | `gemini-omni-flash` | Generación y edición de video conversacional. |

### Familias anteriores vigentes
- **Gemini 2.5 Flash** (`gemini-2.5-flash`), **Nano Banana** (`gemini-2.5-flash-image`),
  **Gemini 2.5 Flash Live** (`gemini-2.5-flash-native-audio-preview-12-2025`),
  **Gemini 2.5 Flash TTS** (`gemini-2.5-flash-preview-tts`).
- **Gemini 2.5 Flash-Lite** (`gemini-2.5-flash-lite`): "el más rápido y económico multimodal de la
  familia 2.5".
- **Gemini 2.5 Pro** (`gemini-2.5-pro`) y **Gemini 2.5 Pro TTS** (`gemini-2.5-pro-preview-tts`).

### Modelos de medios generativos
Veo 3.1 (`veo-3.1-generate-preview`, video cinematográfico con audio sincronizado nativo),
Veo 3.1 Lite (`veo-3.1-lite-generate-preview`), Imagen 4 (`imagen-4.0-generate`, **deprecado**).
Música: **Lyria 3 Pro** (canciones completas), **Lyria 3 Clip** (clips de hasta 30 segundos),
**Lyria RealTime** (streaming en tiempo real).

### Modelos de herramientas y agentes
- **Computer Use** (`gemini-2.5-computer-use-preview-10-2025`): modelo que puede "ver" una pantalla
  digital y ejecutar acciones de UI (clic, escritura, navegación) para automatizar tareas de navegador.
- **Gemini Deep Research** (`deep-research-preview-04-2026`): modelo agéntico que planifica y ejecuta
  investigación multi-paso a través de cientos de fuentes, produciendo informes citados e interactivos.
- **Gemini Deep Research Max** (`deep-research-max-preview-04-2026`).
- **Antigravity Agent** (`antigravity-preview-05-2026`): "A general-purpose managed agent that
  autonomously plans, reasons, runs code, manages files, and browses the web inside a secure,
  isolated Linux sandbox."

### Modelos especializados
- **Gemini Embedding 2** (`gemini-embedding-2-preview`): primer modelo de embedding **multimodal** de
  Google — mapea texto, imágenes, video, audio y PDFs a un espacio de embedding unificado.
- **Gemini Embedding** (`gemini-embedding-001`).
- **Gemini Robotics ER 2** (`gemini-robotics-er-2-preview`) y **ER 1.6**
  (`gemini-robotics-er-1.6-preview`): razonamiento encarnado, comprensión de video, razonamiento
  espacial, orquestación de herramientas multi-paso y colaboración multi-robot.

### Modelos dados de baja (Shut down)
Gemini 2.0 Flash, Gemini 2.0 Flash-Lite, Gemini 3.1 Flash-Lite Preview, Gemini 3 Pro Preview.

## Definitions and terminology

**El esquema de versionado de Google, con sus cuatro categorías** (esto es lo más reutilizable de la
página, porque es una taxonomía y no un dato perecedero):

- **Stable**: apunta a un modelo estable específico. *"Stable models usually don't change. Most
  production apps should use a specific stable model."* Ejemplo: `gemini-3.6-flash`.
- **Preview**: modelo en preview que **puede usarse en producción**. Típicamente con facturación
  habilitada, límites de tasa más restrictivos, y **deprecación con al menos 2 semanas de aviso**.
  Ejemplo: `gemini-2.5-flash-preview-09-2025`.
- **Latest**: alias que apunta al último release de una variante. Puede ser estable, preview o
  experimental. **Se intercambia en caliente** con cada nuevo release. Para cambios que rompen, hay
  aviso por email con **2 semanas** de anticipación. Ejemplo: `gemini-flash-latest`.
- **Experimental**: no apto para producción, límites de tasa más restrictivos. *"We release
  experimental models to gather feedback and get our latest updates into the hands of developers
  quickly."* No son estables y su disponibilidad puede cambiar.

Otros términos:
- **Interactions API**: la API que Google recomienda ahora para acceder a todas las features y
  modelos más recientes.
- **Embodied reasoning** (razonamiento encarnado): el marco de los modelos Robotics ER — entender
  espacios físicos y planificar tareas multi-paso para agentes robóticos.
- **Vibe coding**: aparece literalmente en la descripción de Gemini 3.1 Pro, sin definición.
- **A2A (audio-to-audio)**: modalidad de los modelos Live.

## Evidence and examples

**La página no contiene ni un solo benchmark, precio, tamaño de contexto o cifra de rendimiento.**
Salvo tres números: "70+ idiomas" (Live Translate), "4K" (Nano Banana Pro), "hasta 30 segundos"
(Lyria 3 Clip) y la ventana de 1M de tokens mencionada al pasar para Gemini 2.0 Flash (modelo dado de
baja). La evidencia es puramente el **inventario** y su fecha.

Recuento al 2026-08-04: **7 modelos Gemini 3 estables**, 6 en preview, 4 dados de baja, 3 modelos de
música, 4 de agentes/herramientas, 4 especializados.

## Inconsistencies / open questions

- **Fuente perecedera.** Es un catálogo vivo de un proveedor. La página misma se actualizó el
  2026-08-04 y la captura es del 2026-08-05: **la ventana de validez es de horas o días**. Toda
  diapositiva que use este inventario tiene que fecharlo explícitamente. Lo que no caduca es el
  esquema de versionado.
- **Numeración incoherente entre familias.** Conviven Gemini 3.6, 3.5, 3.1 y 3 dentro de "Gemini 3",
  con el 3.6 Flash marcado como "our latest" y el 3.5 Flash como "most intelligent" — es decir, **el
  más nuevo no es el más inteligente**, y la página no explica el criterio. Además, Gemini 3.1 Pro
  está en preview mientras que Gemini 3.5 y 3.6 Flash ya son estables: el orden de versión no predice
  el orden de madurez.
- **`gemini-3.1-flash-image` se llama "Nano Banana 2"** y `gemini-3-pro-image` se llama "Nano Banana
  Pro". Los nombres comerciales y los endpoints usan numeraciones distintas y cruzadas. Para citar un
  modelo conviene usar el endpoint, no el nombre.
- **"Gemini 3.1 Flash-Lite Preview" figura como dado de baja** mientras "Gemini 3.1 Flash-Lite"
  (estable) sigue vigente. Es correcto pero confuso de leer.
- **Sin datos comparativos.** No hay nada acá para comparar Gemini con otros proveedores, ni siquiera
  entre modelos de la propia familia más allá de adjetivos ("most intelligent", "fastest").
- **Secciones duplicadas por diseño.** La página advierte: *"This section contains all audio models,
  including ones that may already be listed in other sections"*. Varios modelos aparecen dos o tres
  veces. Contar filas sobreestima el catálogo.
- **Enlaces no capturados.** La página de deprecaciones (`/gemini-api/docs/deprecations`) y cada
  ficha individual de modelo quedan fuera. Los datos técnicos reales (contexto, precio, límites) están
  ahí, no acá.
- Ruido de extracción: el selector de 22 idiomas al inicio y el widget de feedback en JSON crudo al
  final del `page.md`.

## Images / diagrams

Una sola imagen, y es cromo del sitio.

- `gemini-api-models.web/images/gemini-api-logo.svg`
  - Provenance: `research/web/gemini-api-models/assets/`; origen
    `https://ai.google.dev/_static/googledevai/images/gemini-api-logo.svg`; alt = "Gemini API"
  - Depiction: logotipo de la Gemini API, elemento de cabecera del sitio.
  - Why it matters: no aplica. Cromo del sitio. Podría servir como marca en una diapositiva
    comparativa de proveedores, sujeto a los términos de marca de Google.

## Raw / preserved excerpts

Aviso de cabecera, verbatim:

> The [Interactions API](/gemini-api/docs/interactions-overview) is now generally available. We recommend using this API for access to all the latest features and models.

Sección completa "Model version name patterns", verbatim:

> Gemini models are available in either *stable*, *preview*, *latest*, or *experimental* versions.
>
> ### Stable
>
> Points to a specific stable model. Stable models usually don't change. Most production apps should use a specific stable model.
>
> For example: `gemini-3.6-flash`.
>
> ### Preview
>
> Points to a preview model which may be used for production. Preview models will typically have billing enabled, might come with more restrictive rate limits and will be deprecated with at least 2 weeks notice.
>
> For example: `gemini-2.5-flash-preview-09-2025`.
>
> ### Latest
>
> Points to the latest release for a specific model variation. This can be a stable, preview or experimental release. This alias will get hot-swapped with every new release of a specific model variation. For breaking changes, a **2-week notice** will be provided through email before the version behind latest is changed.
>
> For example: `gemini-flash-latest`.
>
> ### Experimental
>
> Points to an experimental model which will typically be not be suitable for production use and come with more restrictive rate limits. We release experimental models to gather feedback and get our latest updates into the hands of developers quickly.
>
> Experimental models are not stable and availability of model endpoints is subject to change.

Descripciones de los modelos de agente, verbatim:

> [Computer Use] A specialized model that can "see" a digital screen and perform UI actions like clicking, typing, and navigating to automate complex browser tasks.
>
> [Gemini Deep Research] An agentic model that autonomously plans and executes multi-step research across hundreds of sources to produce cited, interactive reports.
>
> [Gemini Deep Research Max] Maximum comprehensiveness for automated context gathering and synthesis across hundreds of sources.
>
> [Antigravity Agent] A general-purpose managed agent that autonomously plans, reasons, runs code, manages files, and browses the web inside a secure, isolated Linux sandbox.

Descripción de Gemini Embedding 2, verbatim:

> Our first multimodal embedding model, mapping text, images, video, audio, and PDFs into a unified embedding space for advanced semantic search and RAG systems.

Descripción de Gemini Robotics ER 2, verbatim:

> Embodied reasoning model delivering advanced video understanding, spatial reasoning, multi-step tool orchestration, and multi-robot collaboration for robotics tasks.

Pie de página, verbatim:

> Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License.
>
> Last updated 2026-08-04 UTC.
