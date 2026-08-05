---
source_file: moonshot-ai
source_type: web-capture
ingested_at: 2026-08-05
---

# Moonshot AI — página institucional (home)

## Provenance
- Ubicación original: `research/web/moonshot-ai/`
- Formato: captura web (`original.html` 91.761 bytes + `page.md` 13.167 bytes + `assets/`)
- URL: https://www.moonshot.ai/
- Autor / fuente: **Moonshot AI** (laboratorio chino, creador de **Kimi**)
- Fecha del original: la home no declara fecha; las entradas de blog listadas van del **2026-04-20**
  al **2026-07-16**
- Capturado el: 2026-08-05T12:19:52Z · HTTP 200
- Extracción pobre. El `page.md` de 13 KB está dominado por SVGs inline en `data:` URI (flechas,
  íconos de descarga). El contenido textual real ocupa menos de 2 KB. `metadata.yaml` (23,5 KB) está
  igualmente inflado por los mismos data-URIs, marcados `skipped: "non-http"`.

## Key claims

Es una **landing page corporativa**, no un documento. Lo que afirma:

- Lema de la compañía: *"Seeking the optimal conversion from energy to intelligence"* (buscar la
  conversión óptima de energía en inteligencia).
- Posicionamiento del equipo de investigación: *"Our research team works toward AGI while sharing
  the latest research with the global open-source community."*
- **Kimi K3** es el modelo insignia, presentado como *"The new frontier of intelligence"*, con estas
  especificaciones:
  - **2,8 billones de parámetros** (2.8T)
  - **nativamente multimodal**
  - **contexto de 1 millón de tokens**
  - construido para *"long-horizon coding, knowledge work, and deep reasoning"*
- Propuesta de producto: *"AI Models is capability. Code, analyze, sheets and slides — simplify
  complex work with the latest flagship model."* (frase con error gramatical en el original)
- **Últimas publicaciones de investigación** listadas en la home:
  | Fecha | Título | URL |
  |---|---|---|
  | 2026-07-16 | **Kimi K3** | https://www.kimi.com/blog/kimi-k3 |
  | 2026-07-16 | **PerceptionBench** | https://www.kimi.com/blog/perception-bench |
  | 2026-04-20 | **Kimi K2.6** | https://www.kimi.com/blog/kimi-k2-6 |
- Superficies de producto disponibles: web (kimi.com), API (platform.kimi.ai), **app móvil** (con
  código QR para descarga), **extensión de Chrome**, **escritorio en macOS y Windows**.
- Sección "Kimi doodles": doodles temáticos mensuales por feriados, eventos y tendencias. Los tres
  visibles:
  - **Junio · Cumpleaños de Turing** — *"A tape defined computation. One question inspired AI. Chat
    with Kimi continues Turing's legacy."*
  - **Mayo · Cumpleaños de Bob Dylan** — *"Sunglasses, guitar, harmonica. For the old rock Nobel who
    couldn't be bothered. The question is the answer."*
  - **Abril · Día de la Tierra** — *"A Fauvist forest honoring Matisse's cut-outs. Let this Doodle
    remind you: log off and step into spring."*

## Definitions and terminology

- **Kimi**: la marca de producto de Moonshot AI (asistente conversacional). La compañía es Moonshot;
  el producto es Kimi.
- **Kimi K3 / K2.6**: nomenclatura de versiones de modelo.
- **PerceptionBench**: benchmark publicado por Moonshot el mismo día que K3. La home solo enlaza al
  post; **no dice qué mide**.
- **Long-horizon coding**: término que la home usa sin definir, para tareas de programación de
  horizonte largo.
- *"Energy to intelligence"*: el encuadre conceptual de la compañía — la inteligencia como producto
  de una conversión de energía. Es la afirmación más citable de la página.

## Evidence and examples

**Prácticamente ninguna.** Tres cifras en total, todas sobre Kimi K3 y todas auto-declaradas sin
respaldo: 2,8T de parámetros, multimodalidad nativa, 1M de tokens de contexto.

No hay benchmarks, ni comparaciones, ni precios, ni resultados. La home enlaza a los posts de blog
donde presumiblemente están, y **esos posts no fueron capturados**.

## Inconsistencies / open questions

- **Fuente de valor muy bajo para contenido.** Es una landing de marketing. Fuera de las tres cifras
  de K3 y el lema de la compañía, no hay nada citable. Si la presentación necesita datos sobre Kimi
  K3, hay que capturar `https://www.kimi.com/blog/kimi-k3` — **esta captura no sirve para eso**.
- **Las tres cifras de K3 no tienen respaldo acá.** "2.8T parameters" es una afirmación grande sin
  aclarar si son totales o activos (importa mucho si el modelo es MoE, como lo son casi todos a esa
  escala). La página no lo dice.
- **PerceptionBench queda sin explicar.** Un laboratorio publicando su propio benchmark el mismo día
  que su modelo insignia es un dato interesante en sí mismo — pero la home no dice qué mide, y sin el
  post no se puede evaluar si es una medida independiente o construida a medida.
- **Extracción degradada.** Los SVGs inline en `data:` URI hacen el `page.md` casi ilegible: el
  contenido útil está intercalado entre bloques de miles de caracteres de path SVG. Se preservó tal
  cual, pero cualquier lectura automática de este archivo va a tener problemas.
- **Descarga incompleta de assets.** Tres imágenes se guardaron con extensión `.bin` porque el CDN de
  Moonshot (`kimi-file.moonshot.cn`) sirve sin extensión y con parámetros de transformación en la
  query. Se corrigieron las extensiones al copiarlas al corpus (ver más abajo). Los data-URI de
  íconos se marcaron `skipped: "non-http"` y no se descargaron — no importa, son flechas decorativas.
- **Sin fecha en la página.** La home no se fecha a sí misma. La única referencia temporal son las
  entradas de blog (la más reciente, 2026-07-16). Contenido perecedero.
- Errata en el original: *"AI Models is capability"* — la fuente tiene ese error de concordancia. Se
  preserva verbatim.

## Images / diagrams

6 imágenes copiadas desde `research/web/moonshot-ai/assets/`. **Tres se guardaron con extensión
`.bin`** porque el CDN las sirve sin extensión; se identificó el formato real y se corrigió al copiar.

**Imágenes de contenido (3) — pendientes de transcripción.** Son las miniaturas de las tres entradas
de investigación destacadas.

- `moonshot-ai.web/images/1d9ct7h6dcmosb3roh1n0.webp` (originalmente `1d9ct7h6dcmosb3roh1n0.bin`; WebP VP8, 1104×621, 23.628 bytes)
  - Provenance: miniatura de la entrada **"Kimi K3"** (2026-07-16); alt = "Kimi K3"; origen
    `https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/2/2026-07-17/1d9ct7h6dcmosb3roh1n0`
  - <!-- pending: process_images -->
- `moonshot-ai.web/images/d9cg3vmdcmosb3rni9i0.png` (originalmente `d9cg3vmdcmosb3rni9i0.bin`; PNG 2912×1632, 4.600.403 bytes)
  - Provenance: miniatura de la entrada **"PerceptionBench"** (2026-07-16); alt = "PerceptionBench";
    origen `https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/2/2026-07-16/d9cg3vmdcmosb3rni9i0`.
    Por resolución y tamaño es probable que contenga una tabla o gráfico de resultados — vale la pena
    transcribirla.
  - <!-- pending: process_images -->
- `moonshot-ai.web/images/1d7kuvrpl51jas5fhet20.webp` (originalmente `1d7kuvrpl51jas5fhet20.bin`; WebP, 21.394 bytes)
  - Provenance: miniatura de la entrada **"Kimi K2.6"** (2026-04-20); alt = "Kimi K2.6"; origen
    `https://kimi-file.moonshot.cn/prod-chat-kimi/kfs/4/2/2026-04-23/1d7kuvrpl51jas5fhet20`
  - <!-- pending: process_images -->

**Cromo del sitio (3) — sin valor expositivo.**

- `moonshot-ai.web/images/kimi-icon.ByIGCGon.webp`
  - Provenance: sección "Discover Kimi doodles"; alt = "Kimi"; origen `//statics.moonshot.cn/moonshot-ai/assets/static/kimi-icon.ByIGCGon.webp`
  - Depiction: ícono de marca de Kimi. · Why it matters: no aplica.
- `moonshot-ai.web/images/qr-code.CEtPtLiM.webp`
  - Provenance: sección "Built for the future. Available today."; leyenda "Scan to download Kimi App"
  - Depiction: código QR de descarga de la app móvil de Kimi. · Why it matters: no aplica.
- `moonshot-ai.web/images/wireframe-bg.BAsHc09q.svg`
  - Provenance: fondo decorativo de la sección de doodles; sin alt
  - Depiction: fondo de wireframe, elemento gráfico decorativo. · Why it matters: no aplica.

## Raw / preserved excerpts

Todo el contenido textual sustantivo de la página, verbatim (despojado de los data-URI de los íconos):

> # Moonshot AI
>
> Seeking the optimal conversion from energy to intelligence
>
> [Try Kimi](https://www.kimi.com) [Try API](https://platform.kimi.ai)
>
> ## Latest Research
>
> Our research team works toward AGI while sharing the latest research with the global open-source community.
>
> [Get More](https://www.kimi.com/blog/)
>
> [2026-07-16 Kimi K3](https://www.kimi.com/blog/kimi-k3)
> [2026-07-16 PerceptionBench](https://www.kimi.com/blog/perception-bench)
> [2026-04-20 Kimi K2.6](https://www.kimi.com/blog/kimi-k2-6)
>
> ## Complex problems, solved with ease
>
> AI Models is capability. Code, analyze, sheets and slides — simplify complex work with the latest flagship model.
>
> ### Kimi K3
>
> The new frontier of intelligence. 2.8T parameters, natively multimodal, 1M-token context — built for long-horizon coding, knowledge work, and deep reasoning.
>
> [Explore Features](https://www.kimi.com/)
>
> ## Discover Kimi doodles
>
> Explore doodles for holidays, events, and trends — each one a small surprise.
>
> ### June · Turing's Birthday
>
> A tape defined computation. One question inspired AI. Chat with Kimi continues Turing's legacy.
>
> ### May · Bob Dylan 's Birthday
>
> Sunglasses, guitar, harmonica. For the old rock Nobel who couldn't be bothered. The question is the answer.
>
> ### April · Earth Day
>
> A Fauvist forest honoring Matisse's cut-outs. Let this Doodle remind you: log off and step into spring.
>
> ## Built for the future. Available today.
>
> App — Scan to download Kimi App
> [Chrome Extension](https://chromewebstore.google.com/detail/kimi-浏览器助手/caejcfciegnnnepdhaopdogngbmojodl)
> Desktop — [macOS](https://appsupport.moonshot.cn/api/app/pkg/latest/macos/download) · [Windows](https://appsupport.moonshot.cn/api/app/pkg/latest/windows/download)
> [Try Kimi right now](https://www.kimi.com)
