---
source_file: alphafold-db
source_type: web-capture
ingested_at: 2026-08-14
---

# AlphaFold Protein Structure Database — captura vacía (SPA Angular)

> **⚠️ CAPTURA SIN CONTENIDO.** `page.md` tiene **83 caracteres** y son solo el título y la URL. Esta captura **no sirve como fuente**. Ver `Inconsistencies / open questions`.

## Provenance
- Original location: `research/web/alphafold-db/`
- Format: web capture (HTML + `page.md` extraído) — **SPA Angular que renderiza por JavaScript**
- URL: https://alphafold.ebi.ac.uk/
- `fetched_at`: 2026-08-14T16:56:16Z
- `http_status`: **200** — la petición fue exitosa. El problema no es de red.
- `byte_size`: 8360
- Título capturado: `AlphaFold Protein Structure Database`
- Autor / fuente: **EMBL-EBI** (European Bioinformatics Institute) en colaboración con **Google DeepMind**. El HTML lo confirma indirectamente: `<meta name="author" content="AlphaFold Protein Structure Database">`, `<meta name="keywords" content="AlphaFold, PDBe">`, hojas de estilo y fuentes servidas desde `ebi.emblstatic.net` y `assets.emblstatic.net` (framework web institucional del EBI, v1.4), y color de marca `#193F90`.
- Fecha del original: **sin fecha**. Ni de publicación ni de última actualización. Tampoco versión de la base de datos.
- Assets: **ninguno** (`assets: []`). Carpeta compañera vacía — válido.

## Key claims

La página **no afirma nada** en la captura. El único texto descriptivo del HTML es tautológico: `<meta name="description" content="AlphaFold Protein Structure Database">` — la descripción repite el título y no aporta información.

Lo único que se puede inferir del HTML, y son detalles técnicos, no contenido:

- El sitio es de **EMBL-EBI** y está emparentado con **PDBe** (Protein Data Bank in Europe) — la keyword `PDBe` lo dice.
- Carga **PDBe-Mol\*** (`pdbe-molstar@3.11.0` desde jsDelivr), el visor 3D de estructuras moleculares. Confirma que el sitio muestra estructuras proteicas interactivas, pero no muestra ninguna en la captura.
- Tiene un widget de búsqueda generativa (`gen-search-widget`, con estilos inyectados en su shadow DOM).

**Ninguna de las cifras que la clase necesita — cuántas estructuras contiene la base, qué versión, qué cobertura de proteomas — aparece en la captura.**

## Definitions and terminology

**Ninguna.** La captura no define nada. Ni "AlphaFold", ni "predicción de estructura de proteínas", ni "pLDDT" (la métrica de confianza que la base usa y que sería lo relevante para hablar de fiabilidad en clase). Nada.

## Evidence and examples

**Ninguno.** Cero cifras, cero ejemplos, cero figuras. En particular, **no está el número de estructuras de la base**, que es el único dato que el deck le pide a esta fuente.

## Inconsistencies / open questions

1. **La captura está vacía de contenido y no puede usarse como fuente.** `page.md` son 83 caracteres: el encabezado `# AlphaFold Protein Structure Database` y la línea `_Source: <https://alphafold.ebi.ac.uk/>_`. Nada más.

2. **La causa es arquitectónica, no un fallo de la captura.** El HTTP fue **200** y llegaron 8.360 bytes de HTML — pero son puro `<head>`: metas, preconnects, precargas de fuentes, favicons, y los scripts de analítica (Microsoft Clarity, Hotjar, Google Analytics). El `<body>` útil se reduce a:

   ```html
   <div id="content">
     <app-root></app-root>
   </div>
   ```

   `<app-root>` es el punto de montaje de una aplicación **Angular** (`polyfills-JUTM3XWE.js`, `main-RMCDQW2G.js`, varios `chunk-*.js` con `modulepreload`). Todo el contenido se construye en el cliente. El fallback a `original.html` **no ayuda**: no hay contenido que rescatar. Recapturar con el mismo método daría idéntico resultado; haría falta un navegador headless que ejecute JS.

3. **Qué afirmación del deck queda sin respaldo.** El deck usa AlphaFold en la **slide 52** (pipeline de descubrimiento de fármacos), en la etapa "Target y Diseño Molecular", con esta afirmación destacada en negrita:

   > **"AlphaFold predijo estructuras de 200M+ proteínas"**

   La cifra también está tabulada en el índice de números del deck: *"**200M+ proteínas** | Estructuras predichas por AlphaFold | slide 52 | AlphaFold 2/3, DeepMind (2022/2024)"*.

   **Esa cifra no está en la captura.** El corpus no contiene ninguna fuente que la respalde. La cifra de "200 millones y pico" es ampliamente citada y corresponde al orden de magnitud que la base anunció en su expansión de julio de 2022, pero **eso es conocimiento externo, no algo que este corpus documente**. Si el presentador quiere sostener el número en clase, necesita:
   - la cifra exacta y su fecha desde la propia base (la portada la muestra, pero solo con JS), o
   - el paper de AlphaFold DB (Varadi et al., *Nucleic Acids Research*) que sí es un documento estático citable.

   Además, la atribución del deck — "AlphaFold 2/3, DeepMind (2022/2024)" — **mezcla el modelo con la base de datos**. Los 200M+ son de la *base* (EMBL-EBI + DeepMind), no una salida directa de AlphaFold 3. La captura no permite deshacer esa ambigüedad porque no dice nada.

4. **Qué necesitaría la clase y no está.** El conteo actual de estructuras con su fecha; la cobertura por organismo; la explicación de pLDDT y de las bandas de confianza (crítico si en clase se va a hablar de cuánto confiar en una predicción); las condiciones de licencia y reutilización (CC-BY 4.0) por si el deck reproduce una imagen de estructura.

5. **Riesgo de cifra desactualizada, no verificable.** La base creció por saltos y no tiene fecha visible en la captura. Un número citado sin fecha ("200M+") puede quedar corto o largo según el momento. Como la captura no trae fecha ni versión, **el corpus no puede fechar el dato de ninguna manera**.

## Images / diagrams

Ninguna. `metadata.yaml` declara `assets: []` y la carpeta compañera `alphafold-db.web/images/` está vacía — válido según el esquema.

Nota: el HTML solo referencia favicons e iconos de aplicación (`favicon.ico`, `favicon-32x32.png`, `android-chrome-192x192.png`, los `apple-icon-*` del EMBL-EBI y un `safari-pinned-tab.svg`), todos cromo de navegador sin valor de contenido, y ninguno fue descargado. **No hay ninguna imagen de estructura proteica en la captura** — que es justamente lo que uno querría de este sitio para una slide. Las estructuras las dibuja el visor PDBe-Mol\* en tiempo de ejecución, en un canvas, a partir de datos que se piden por red.

## Raw / preserved excerpts

**`page.md` íntegro** (los 83 caracteres, esto es literalmente todo lo que se extrajo):

```markdown
# AlphaFold Protein Structure Database

_Source: <https://alphafold.ebi.ac.uk/>_
```

**Metadatos del `<head>`, verbatim** — nótese que la descripción no describe nada:

> `<meta name="description" content="AlphaFold Protein Structure Database">`
> `<meta name="keywords" content="AlphaFold, PDBe">`
> `<meta name="author" content="AlphaFold Protein Structure Database">`
> `<meta name="theme-color" content="#193F90">`

**El `<body>` útil del HTML capturado** — la prueba de que no hay contenido:

```html
<body class="level2 no-global-search" ngcm="">
  <div id="content">
    <app-root></app-root>
  </div>
</body>
```

**Evidencia de que el sitio monta un visor molecular** (relevante solo para entender qué se perdió):

> `<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/pdbe-molstar@3.11.0/build/pdbe-molstar-light.css">`

**Scripts de la aplicación Angular que construyen la página en el cliente:**

```html
<script src="polyfills-JUTM3XWE.js" type="module"></script>
<script src="main-RMCDQW2G.js" type="module"></script>
```
