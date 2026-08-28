---
source_file: gpt-tokenizer
source_type: web-capture
ingested_at: 2026-08-14
---

# GPT Tokenizer Playground — captura vacía (SPA)

> **⚠️ CAPTURA SIN CONTENIDO.** `page.md` tiene **107 caracteres** y son solo el título y la URL. Esta captura **no sirve como fuente**. Ver `Inconsistencies / open questions`.

## Provenance
- Original location: `research/web/gpt-tokenizer/`
- Format: web capture (HTML + `page.md` extraído) — **SPA que renderiza por JavaScript**
- URL: https://gpt-tokenizer.dev
- `fetched_at`: 2026-08-14T16:56:16Z
- `http_status`: **200** — la petición fue exitosa. El problema no es de red.
- `byte_size`: 2984
- Título capturado: `GPT Tokenizer Playground – Visualize Tokens for OpenAI Models`
- Autor / fuente: proyecto `gpt-tokenizer`. El HTML declara `"publisher": {"@type": "Organization", "name": "gpt-tokenizer"}` y `twitter:creator` **`@niieani`** (Bazyli Brzóska, autor de la librería `gpt-tokenizer` en npm/GitHub).
- Fecha del original: **sin fecha**. No hay fecha de publicación ni de actualización en ninguna parte del HTML.
- Assets: **ninguno** (`assets: []`). Carpeta compañera vacía — válido.

## Key claims

La página **no afirma nada** en la captura, porque no hay página capturada. Lo único recuperable son las etiquetas `<meta>` y el bloque JSON-LD del `<head>`, que describen la herramienta pero no son contenido:

- Es un **playground interactivo de tokenización** para modelos de OpenAI.
- Sus tres funciones declaradas: **visualizar tokens**, **estimar el costo de un prompt** y **entender los límites de la ventana de contexto**.
- Permite **comparar modelos** entre sí (`"compare models, and stay within context limits"`).
- Es **gratuita**: el JSON-LD declara `"offers": {"price": "0", "priceCurrency": "USD"}`.
- Está clasificada como `SoftwareApplication` / `DeveloperApplication`, `operatingSystem: Web`.

Eso es todo. No hay explicación de qué es un token, ni ejemplos, ni la tabla de equivalencias que uno esperaría de una página así.

## Definitions and terminology

**Ninguna.** La captura no define nada. Los términos aparecen solo nombrados en las metas: *tokens*, *prompt costs*, *context limits*, *tokenization*.

La única formulación con algo de sustancia conceptual está en la meta `twitter:description`, y es una frase suelta: *"see how prompts become tokens"* — la idea de que el prompt no es texto para el modelo sino una secuencia de tokens. Es exactamente lo que la clase quiere transmitir en la slide 9, pero la captura no lo desarrolla ni un renglón más.

## Evidence and examples

**Ninguno.** Cero ejemplos, cero cifras, cero capturas de pantalla. El valor entero de esta herramienta es interactivo — pegar texto y ver los tokens coloreados — y eso, por definición, no sobrevive a una captura estática.

## Inconsistencies / open questions

1. **La captura está vacía de contenido y no puede usarse como fuente.** `page.md` son 107 caracteres: el encabezado `# GPT Tokenizer Playground – Visualize Tokens for OpenAI Models` y la línea `_Source: <https://gpt-tokenizer.dev>_`. Nada más.

2. **La causa es arquitectónica, no un fallo de la captura.** El HTTP fue **200** y el HTML llegó entero. Pero el `<body>` completo es:

   ```html
   <body class="bg-slate-950 text-slate-50">
     <div id="root"></div>
   </body>
   ```

   Un `<div id="root">` vacío y un `<script type="module" src="/assets/index-OsEgNqlO.js">`. Es una SPA (build de Vite, por el hash del bundle) que construye toda la interfaz en el cliente. El fallback a `original.html` **no ayuda**: no hay contenido que rescatar, porque nunca se envió del servidor. Recapturarla con el mismo método daría idéntico resultado; haría falta un navegador headless que ejecute JS.

3. **Qué afirmación del deck queda sin respaldo.** El deck nombra esta herramienta en la **slide 9**, con la invitación *"Pruébalo en tiempo real"* (registrada en el índice de herramientas del deck como: *"**Tokenizador:** `gpt-tokenizer.dev` ('Pruébalo en tiempo real') — slide 9"*). Es decir: **la slide 9 le pide a la audiencia que use esta herramienta en vivo, y el corpus no tiene ni una línea de lo que la herramienta muestra.**

   Consecuencias prácticas para la clase:
   - Si el presentador hace la demo en vivo, la captura es irrelevante y no hay problema — pero **conviene que verifique el sitio antes de la clase**, porque el corpus no puede confirmar que siga funcionando ni cómo se ve.
   - Si el deck muestra una captura de pantalla de la herramienta, **esa imagen no vino de acá** y su procedencia queda sin documentar.
   - Cualquier cifra concreta sobre tokenización que el deck atribuya a esta fuente (cuántos tokens tiene una palabra, cómo se parte una palabra en español, el costo de un prompt de ejemplo) **no está respaldada por esta captura**.

4. **Qué necesitaría la clase y no está.** Lo obvio: un ejemplo concreto de texto tokenizado — idealmente en español, porque la clase es en español y la tokenización de OpenAI es notoriamente menos eficiente fuera del inglés, que es justo el punto pedagógico interesante. También la regla práctica de conversión (tokens ≈ palabras × factor) y la tabla de límites de contexto por modelo. Nada de eso está.

5. **Riesgo de obsolescencia no verificable.** La página no tiene fecha. No se puede saber qué modelos de OpenAI cubre el playground ni si la lista está actualizada. El deck usa esta herramienta junto a una tabla de ventanas de contexto (slide 45 y alrededores); si esos números salieron de acá, no hay forma de fecharlos.

## Images / diagrams

Ninguna. `metadata.yaml` declara `assets: []` y la carpeta compañera `gpt-tokenizer.web/images/` está vacía — válido según el esquema.

Vale registrar que el HTML **sí referencia** una imagen social que **no se descargó** (no figura en `assets`, por lo que el ingestor no la persiguió): `https://raw.githubusercontent.com/niieani/gpt-tokenizer/main/docs/gpt-tokenizer.png`, declarada tanto en `og:image` como en `twitter:image` con `twitter:card: summary_large_image`. Es la imagen de previsualización del repositorio y, siendo la captura de pantalla promocional del proyecto, es plausible que muestre la interfaz del tokenizador en acción — lo único parecido a contenido visual que esta fuente podría aportar. **No está en el corpus.** Si la clase necesita una imagen de la herramienta, ese es el candidato a buscar.

## Raw / preserved excerpts

**`page.md` íntegro** (los 107 caracteres, esto es literalmente todo lo que se extrajo):

```markdown
# GPT Tokenizer Playground – Visualize Tokens for OpenAI Models

_Source: <https://gpt-tokenizer.dev>_
```

**Metadatos del `<head>`, verbatim** — la única prosa descriptiva que existe en la captura:

> `<meta name="description" content="Experiment with the gpt-tokenizer playground to visualize tokens, measure prompt costs, and understand context limits across OpenAI models." />`
>
> `<meta property="og:description" content="Interactive tokenizer playground for OpenAI models. Count tokens, estimate pricing, and learn how tokenization shapes prompts." />`
>
> `<meta name="twitter:description" content="Use the gpt-tokenizer playground to see how prompts become tokens, compare models, and stay within context limits." />`
>
> `<meta name="twitter:creator" content="@niieani" />`

**Bloque JSON-LD, verbatim:**

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "GPT Tokenizer Playground",
  "description": "Interactive tokenizer playground for OpenAI models. Visualize tokens, estimate prompt costs, and understand context limits.",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Web",
  "url": "https://gpt-tokenizer.dev/",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  },
  "publisher": {
    "@type": "Organization",
    "name": "gpt-tokenizer"
  }
}
```

**El `<body>` completo del HTML capturado** — la prueba de que no hay contenido:

```html
<body class="bg-slate-950 text-slate-50">
  <div id="root"></div>
</body>
```
