---
source_file: esm-atlas
source_type: web-capture
ingested_at: 2026-08-14
---

# ESM Metagenomic Atlas (Meta AI) — captura vacía (SPA React)

> **⚠️ CAPTURA SIN CONTENIDO.** `page.md` tiene **72 caracteres** y son solo el título y la URL. Esta captura **no sirve como fuente**. Ver `Inconsistencies / open questions`.

## Provenance
- Original location: `research/web/esm-atlas/`
- Format: web capture (HTML + `page.md` extraído) — **SPA React que renderiza por JavaScript**
- URL: https://esmatlas.com/
- `fetched_at`: 2026-08-14T16:56:16Z
- `http_status`: **200** — la petición fue exitosa. El problema no es de red.
- `byte_size`: **1637** — la captura más pequeña de las catorce. El HTML entero es una sola línea minificada.
- Título capturado: `ESM Metagenomic Atlas by Meta AI`
- Autor / fuente: **Meta AI** (FAIR). Las metas Open Graph lo declaran: `og:title` = `"ESM Metagenomic Atlas | Meta AI"`.
- Fecha del original: **sin fecha**. Ni de publicación ni de actualización ni versión del atlas.
- Assets: **ninguno** (`assets: []`). Carpeta compañera vacía — válido.

## Key claims

La página **no afirma nada en su cuerpo**, porque no hay cuerpo capturado. A diferencia de `alphafold-db` y `gpt-tokenizer`, acá las metas **sí traen un dato sustantivo**, repetido cuatro veces en el `<head>`:

- El atlas contiene **617 millones de estructuras proteicas metagenómicas predichas**.
- Es **abierto** (`"An open atlas of..."`).
- Es de **Meta AI**.

Ese número — **617M** — es lo único de valor que sobrevivió a la captura, y sobrevivió por accidente: está en las metas de previsualización social, no en el contenido. Es un dato sin contexto: no dice de qué versión del atlas es, ni de cuándo, ni con qué modelo se generó (ESMFold, presumiblemente, pero **la captura nunca nombra ESMFold**).

## Definitions and terminology

**Ninguna definida.** La captura no explica nada. Aparecen nombrados, sin definir:

- **Metagenómico** — en `"predicted metagenomic protein structures"`. Es el término clave que distingue este recurso de AlphaFold DB: son proteínas provenientes de secuenciación metagenómica (muestras ambientales, microorganismos no cultivados), no de organismos con genoma de referencia. **La captura no explica esa distinción**, que es precisamente lo que justificaría mencionar ESM Atlas *además* de AlphaFold en una clase.
- **Atlas** — usado como nombre propio del recurso.
- **ESMFold** — **no aparece en la captura**. Ni una vez. Aunque es el modelo que produjo el atlas y es lo que el deck cita.

## Evidence and examples

Un solo dato, y de segunda mano (viene de una meta, no del contenido):

| Dato | Valor | De dónde sale |
|---|---|---|
| Estructuras proteicas metagenómicas predichas | **617.000.000** | `<meta name="description">`, `og:description`, `twitter:description` — las tres coinciden |

Nada más. Sin fecha, sin versión, sin metodología, sin métricas de confianza, sin ejemplos.

## Inconsistencies / open questions

1. **La captura está vacía de contenido y no puede usarse como fuente.** `page.md` son 72 caracteres: el encabezado `# ESM Metagenomic Atlas by Meta AI` y la línea `_Source: <https://esmatlas.com/>_`. Nada más.

2. **La causa es arquitectónica, no un fallo de la captura.** El HTTP fue **200**, pero el HTML son 1.637 bytes que terminan así:

   ```html
   <body>
     <noscript>You need to enable JavaScript to run this app.</noscript>
     <div id="root"></div>
   </body>
   ```

   El propio sitio lo dice en el `<noscript>`: **hay que habilitar JavaScript para que la aplicación funcione**. Es una SPA React (bundle `main.b2c22278.js`) que construye todo en el cliente. El fallback a `original.html` **no ayuda**: no hay contenido que rescatar. Recapturar con el mismo método daría idéntico resultado; haría falta un navegador headless.

3. **Qué afirmación del deck queda sin respaldo.** El deck cita **ESMFold, Meta AI (2022)** en la línea de fuentes de la **slide 52** (pipeline de descubrimiento de fármacos), como respaldo de la etapa "Target y Diseño Molecular" — la que afirma que *"Los LLMs predicen estructuras proteicas y optimizan candidatos a fármacos"*.

   Dos problemas encadenados:
   - **La captura no menciona ESMFold en ningún lado.** El deck cita un modelo; la captura es del atlas de datos que ese modelo produjo, y ni siquiera lo nombra. Son cosas distintas y el corpus no puede tender el puente.
   - **El deck no cita la cifra de 617M.** Curiosamente, el único dato que la captura sí conserva no aparece en el deck: la slide 52 destaca los "200M+" de AlphaFold pero no dice nada del volumen de ESM Atlas. Así que la captura tiene un dato que el deck no usa, y el deck cita un modelo del que la captura no habla. **No se cruzan en ningún punto.**

   Resultado: **la mención a ESMFold en la slide 52 queda sin respaldo documental en el corpus.** Es una cita por nombre, sin URL en el deck y sin contenido en la captura.

4. **Qué necesitaría la clase y no está.** La distinción conceptual entre AlphaFold DB y ESM Atlas — por qué existen los dos, qué aporta el metagenómico — que es lo único que justifica nombrar ambos en la misma slide. También: fecha y versión del atlas, la relación explícita atlas ↔ ESMFold, métricas de confianza de las predicciones, y el paper de referencia (Lin et al., *Science*, 2023, para ESMFold) que sería la fuente citable de verdad.

5. **Riesgo de recurso discontinuado, no verificable desde la captura.** El atlas es un proyecto de investigación de Meta AI de 2022-2023, y el equipo ESM se escindió después de Meta. La captura no tiene fecha ni aviso de estado, así que **el corpus no puede decir si el recurso sigue mantenido**. Si el deck enlaza a `esmatlas.com` en vivo, conviene verificarlo antes de la clase.

6. **El dato de 617M no está fechado ni versionado.** Viene de una meta de previsualización social, que es de lo último que se actualiza en un sitio. Tomarlo como cifra vigente es un acto de fe.

## Images / diagrams

Ninguna. `metadata.yaml` declara `assets: []` y la carpeta compañera `esm-atlas.web/images/` está vacía — válido según el esquema.

Nota: el HTML **sí referencia** dos imágenes que **no se descargaron** (no figuran en `assets`, el ingestor no las persiguió):

- `https://esmatlas.com/bg_share.png` — declarada en `og:image` y `twitter:image`. Es la imagen de previsualización social del atlas; por el nombre (`bg_` = background) es plausible que sea el fondo visual del sitio, probablemente una representación de estructuras proteicas. **Sería la única imagen de contenido que esta fuente podría aportar**, y no está en el corpus.
- Favicons de Meta (`M_Favicon.ico`, `M_Favicon_16x16.png`, `M_Favicon_32x32.png`, `M_Favicon_192x192.png`) — cromo puro, sin valor.

Nótese también que `twitter:card` está declarado como `summary` (tarjeta chica) mientras `og:image` apunta a una imagen — inconsistencia menor del sitio, sin consecuencias para la clase.

## Raw / preserved excerpts

**`page.md` íntegro** (los 72 caracteres, esto es literalmente todo lo que se extrajo):

```markdown
# ESM Metagenomic Atlas by Meta AI

_Source: <https://esmatlas.com/>_
```

**Metadatos del `<head>`, verbatim** — acá está el único dato sustantivo de toda la captura, repetido tres veces:

> `<meta name="description" content="ESM Metagenomic Atlas. An open atlas of 617 million predicted metagenomic protein structures"/>`
>
> `<meta property="og:title" content="ESM Metagenomic Atlas | Meta AI"/>`
> `<meta property="og:description" content="An open atlas of 617 million predicted metagenomic protein structures"/>`
> `<meta property="og:url" content="https://esmatlas.com"/>`
> `<meta property="og:image" content="/bg_share.png"/>`
>
> `<meta name="twitter:title" content="ESM Metagenomic Atlas | Meta AI"/>`
> `<meta name="twitter:description" content="An open atlas of 617 million predicted metagenomic protein structures"/>`
> `<meta name="twitter:image" content="https://esmatlas.com/bg_share.png"/>`
> `<meta name="twitter:card" content="summary"/>`

**El `<body>` completo del HTML capturado** — la prueba de que no hay contenido, con el aviso explícito del propio sitio:

```html
<body>
  <noscript>You need to enable JavaScript to run this app.</noscript>
  <div id="root"></div>
</body>
```

**Bundle React que construye la página en el cliente:**

```html
<script defer="defer" src="/static/js/main.b2c22278.js"></script>
<link href="/static/css/main.f4da62f1.css" rel="stylesheet"/>
```
