---
source_file: txgnn-nature-medicine
source_type: web-capture
ingested_at: 2026-08-14
---

# TxGNN (Nature Medicine) — captura bloqueada por muro anti-bot

> **⚠️ CAPTURA SIN CONTENIDO.** No se capturó el artículo: se capturó un **muro anti-bot de Cloudflare**. `page.md` tiene **296 caracteres** y son un mensaje de error. Esta captura **no sirve como fuente**. Ver `Inconsistencies / open questions`.

## Provenance
- Original location: `research/web/txgnn-nature-medicine/`
- Format: web capture (HTML + `page.md` extraído) — **página de desafío anti-bot, no el artículo**
- URL solicitada: https://www.nature.com/articles/s41591-023-02351-8
- `fetched_at`: 2026-08-14T16:56:07Z
- `http_status`: **200** — y este 200 es engañoso. Ver punto 2 de `Inconsistencies`.
- `byte_size`: 3038
- Título capturado: **`Client Challenge`** — no es el título del artículo. Es el título de la página de verificación de Cloudflare. Que el `title` del `metadata.yaml` sea "Client Challenge" es en sí mismo el diagnóstico.
- Autor / fuente del artículo pretendido: **TxGNN, Harvard**, publicado en **Nature Medicine** (Springer Nature). El DOI del identificador — `s41591-023-02351-8` — corresponde a la revista `s41591` (*Nature Medicine*) y al año de registro **2023**.
- Fecha del original: **no verificable desde la captura**. Ver punto 5 de `Inconsistencies`.
- Assets: **ninguno** (`assets: []`). Carpeta compañera vacía — válido.

## Key claims

**Ninguna.** No hay artículo capturado. Ni título real, ni autores, ni abstract, ni resultados, ni figuras.

Lo único que dice la captura es que el contenido no se pudo cargar:

> "A required part of this site couldn't load. This may be due to a browser extension, network issues, or browser settings. Please check your connection, disable any ad blockers, or try using a different browser."

Ese mensaje **no viene del artículo ni de Nature**: es el texto de fallback de un desafío de cliente.

## Definitions and terminology

**Ninguna.** La captura no contiene una sola palabra sobre TxGNN, redes neuronales de grafos, reposicionamiento de fármacos ni predicción de indicaciones terapéuticas.

## Evidence and examples

**Ninguno.** Cero cifras, cero resultados, cero figuras.

## Inconsistencies / open questions

1. **La captura está vacía de contenido y no puede usarse como fuente.** `page.md` son 296 caracteres, de los cuales el contenido es un mensaje de error genérico de navegador. Es la única de las catorce capturas que falló por **bloqueo deliberado del servidor**, no por arquitectura de la página.

2. **El `http_status: 200` es engañoso y hay que leerlo con cuidado.** No significa que la captura haya salido bien. Significa que **el muro anti-bot respondió correctamente con su propia página**. La evidencia está en el HTML:
   - El `<title>` es `Client Challenge`, no el título del artículo.
   - Todos los recursos cuelgan de una ruta ofuscada con hash de sesión: `/_fs-ch-1T1wmsGaOgGaSxcX/assets/styles.css`, `/_fs-ch-1T1wmsGaOgGaSxcX/errors.js`, `/_fs-ch-1T1wmsGaOgGaSxcX/script.js?reload=true`. El prefijo `_fs-ch-` es la firma del desafío de cliente.
   - Hay una `Content-Security-Policy` restrictiva con hashes `sha256` fijos para el único script y el único estilo permitidos — típico de una página de verificación aislada.
   - El `<noscript>` dice `"JavaScript is disabled in your browser. Please enable JavaScript to proceed."` — o sea: **el servidor exige ejecutar JS para probar que sos un navegador real antes de servir el artículo.**

   Un lector automático nunca pasa ese desafío. **Recapturar con el mismo método dará siempre el mismo resultado.**

3. **Qué afirmación del deck queda sin respaldo.** El deck usa TxGNN en la **slide 52** (pipeline de descubrimiento de fármacos), en la etapa "Preclínica y Validación", con esta afirmación destacada en negrita:

   > **"TxGNN (Harvard) predice indicaciones para 17.000 enfermedades"**

   La cifra también está tabulada en el índice de números del deck: *"**17.000 enfermedades** | Indicaciones predichas por TxGNN (Harvard) | slide 52 | TxGNN, Harvard (Nature Medicine, 2024)"*.

   **Esa cifra no está respaldada por nada en el corpus.** La única fuente que se intentó capturar para sostenerla es esta, y no trajo ni una letra del artículo. La afirmación de la slide 52 sobre TxGNN queda, hoy, **sin respaldo documental**.

   Para sostenerla en clase haría falta: la cifra exacta de enfermedades y qué significa (¿enfermedades cubiertas por el modelo?, ¿indicaciones predichas?, ¿enfermedades con pocos o ningún tratamiento?, que es lo que suele destacarse de este trabajo), más los autores y la fecha. Nada de eso está.

4. **Discrepancia de año entre el deck y el DOI.** El deck cita **"TxGNN, Harvard (Nature Medicine, 2024)"**. El DOI de la URL que se intentó capturar es `s41591-023-02351-8`, cuyo segmento `023` indica registro en **2023**. Es una discrepancia real, aunque tiene explicación posible y benigna: en Nature es habitual que un artículo se registre y se publique online en un año y aparezca en un número impreso del siguiente. **Pero la captura no permite resolverlo**, porque no trae ni fecha de recepción, ni de aceptación, ni de publicación. Queda como pregunta abierta: si el deck cita el año en pantalla, conviene verificar cuál corresponde.

5. **Segunda cita a Nature Medicine 2024 en el mismo deck, sin URL propia.** La slide 52 cita *"Nature Medicine, 2024"* **otra vez**, en la etapa "Ensayos Clínicos", para una afirmación distinta: *"GPT-4 mejora el reclutamiento simplificando criterios de elegibilidad"*. No hay carpeta de captura para esa segunda referencia — **solo se intentó la de TxGNN**. Así que la slide 52 apoya dos afirmaciones diferentes en la misma revista y el mismo año, y el corpus no tiene contenido para ninguna de las dos. Vale registrarlo para que no se confundan entre sí al momento de citar.

6. **Qué necesitaría la clase y no está.** Todo: título real, autores, afiliación, abstract, la definición de qué hace TxGNN (predicción sobre grafo de conocimiento para indicaciones y contraindicaciones), las métricas reportadas, el alcance real de las "17.000 enfermedades", y cualquier figura del pipeline. La captura no aporta nada de esto.

7. **Vía alternativa, no intentada.** Los artículos de Nature suelen tener versión indexada en PubMed/PMC, y muchos grupos depositan preprint. Si la clase necesita sostener la cifra, esas rutas no están bloqueadas por el mismo muro. **No se intentaron en esta pasada** y no corresponde inventarlas acá; queda anotado como acción para el orquestador.

## Images / diagrams

Ninguna. `metadata.yaml` declara `assets: []` y la carpeta compañera `txgnn-nature-medicine.web/images/` está vacía — válido según el esquema.

La única imagen referenciada en el HTML es `/_fs-ch-1T1wmsGaOgGaSxcX/assets/errorIcon.svg`, el icono de error del muro anti-bot, marcado en el propio HTML como `role="presentation"` con `alt=""` — decorativo por declaración explícita del sitio. No se descargó y no tiene ningún valor. **Las figuras del artículo — que serían lo más útil de esta fuente para una slide sobre el pipeline de descubrimiento de fármacos — nunca llegaron.**

## Raw / preserved excerpts

**`page.md` íntegro** (los 296 caracteres, esto es literalmente todo lo que se extrajo):

```markdown
# Client Challenge

_Source: <https://www.nature.com/articles/s41591-023-02351-8>_

A required part of this site couldn't load. This may be due to a browser extension, network issues, or browser settings. Please check your connection, disable any ad blockers, or try using a different browser.
```

**El `<title>` de la página capturada** — el diagnóstico en una línea:

```html
<title>Client Challenge</title>
```

**Aviso de `<noscript>`, verbatim** — el servidor exige ejecución de JS para dejar pasar:

```html
<noscript>
  <div class="noscript-container">
    <div class="noscript-content">
      <img src="/_fs-ch-1T1wmsGaOgGaSxcX/assets/errorIcon.svg" alt="" role="presentation" class="error-icon" />
      <span class="noscript-span">JavaScript is disabled in your browser.</span>
      <p>Please enable JavaScript to proceed.</p>
    </div>
  </div>
</noscript>
```

**Content-Security-Policy del desafío** — hashes fijos, un solo script y un solo estilo permitidos:

```html
<meta
  http-equiv="Content-Security-Policy"
  content="default-src 'self'; img-src 'self' data:; media-src 'self' data:; object-src 'none'; style-src 'self' 'sha256-o4vzfmmUENEg4chMjjRP9EuW9ucGnGIGVdbl8d0SHQQ='; script-src 'self' 'sha256-a9bHdQGvRzDwDVzx8m+Rzw+0FHZad8L0zjtBwkxOIz4=';"
/>
```

**Cargador del desafío** — las rutas con hash de sesión `_fs-ch-`:

```javascript
loadScript('/_fs-ch-1T1wmsGaOgGaSxcX/errors.js')
  .then(() => {
    const script = document.createElement('script');
    script.src = '/_fs-ch-1T1wmsGaOgGaSxcX/script.js?reload=true';
    ...
  })
```
