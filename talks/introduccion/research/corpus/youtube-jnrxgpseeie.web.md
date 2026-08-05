---
source_file: youtube-jnrxgpseeie
source_type: web-capture
ingested_at: 2026-08-05
---

# Move 37!! Lee Sedol vs AlphaGo Match 2 (video de YouTube)

## Provenance
- Ubicación original: `research/web/youtube-jnrxgpseeie/`
- Formato: captura web (`original.html` 1.134.502 bytes + `page.md` reescrito a mano)
- URL: https://www.youtube.com/watch?v=JNrXgpSEEIE
- Autor / fuente: canal **Daniel Estrada** (https://www.youtube.com/@DanielEstrada)
- Fecha del original: no consta en la captura (el partido registrado es de marzo de 2016)
- Capturado el: 2026-08-05T12:18:44Z · HTTP 200
- **Extracción manual.** YouTube renderiza su contenido con JavaScript, así que `original.html`
  no contiene ni el título ni la descripción del video. `page.md` fue reescrito a mano a partir
  del endpoint oEmbed público de YouTube
  (`https://www.youtube.com/oembed?url=...&format=json`), consultado el 2026-08-05.
  El `metadata.yaml` lo declara explícitamente en el campo `extraction`.

## Key claims

Esta fuente **no argumenta nada**: es un puntero a un artefacto audiovisual. Lo que la captura
establece con certeza es:

- Existe un video público titulado *"Move 37!! Lee Sedol vs AlphaGo Match 2"*, publicado por el
  canal Daniel Estrada.
- El video registra el momento de la **jugada 37 de la segunda partida** del match entre AlphaGo
  (DeepMind) y Lee Sedol, jugado en Seúl en **marzo de 2016**.
- Miniatura disponible en `https://i.ytimg.com/vi/JNrXgpSEEIE/hqdefault.jpg` (no descargada).

## Definitions and terminology

- **Move 37 / jugada 37**: la jugada de AlphaGo en la partida 2 del match contra Lee Sedol que los
  comentaristas describieron como no-humana. El término circula como abreviatura de "momento en que
  una máquina produce una jugada que ningún jugador humano habría elegido y que sin embargo resulta
  buena". *La captura nombra el evento pero no lo define ni lo explica.*
- **Lee Sedol**: jugador profesional de Go, rival humano del match.
- **AlphaGo**: sistema de DeepMind, rival de máquina del match.

## Evidence and examples

Ninguna dentro de la captura. El contenido probatorio (el video en sí, los comentarios, la
reacción de los comentaristas) **no fue capturado**. La captura documenta la existencia y la
ubicación de la fuente, no su contenido.

## Inconsistencies / open questions

- **No hay transcripción.** La captura no alcanzó ni la transcripción ni la descripción del video.
  Cualquier cita textual de lo que se dice en el video tendría que obtenerse de otra manera.
- **No hay fecha de publicación** del video ni conteo de vistas: el HTML JS-renderizado no los trae.
- **No se descargó la miniatura.** La URL queda registrada arriba por si se la quiere usar en una
  diapositiva; habría que traerla aparte.
- El propio `page.md` deja constancia de que *"el contenido narrativo sobre la jugada 37 vive en las
  notas del orador de la diapositiva correspondiente, no acá. Este registro documenta la fuente, no
  la interpreta."* Esa separación se respeta en este registro.
- **Riesgo para quien cite esta fuente:** sirve como referencia audiovisual para proyectar o enlazar,
  no como respaldo de afirmaciones textuales. Una diapositiva que afirme algo *sobre* la jugada 37
  necesita otra fuente además de esta.

## Images / diagrams

Ninguna. `metadata.yaml` declara `assets: []` y no se descargó la miniatura. La carpeta companion
`youtube-jnrxgpseeie.web/images/` existe y está vacía.

## Raw / preserved excerpts

Contenido completo de `page.md` (extracción manual), preservado verbatim:

> # Move 37!! Lee Sedol vs AlphaGo Match 2
>
> _Source: <https://www.youtube.com/watch?v=JNrXgpSEEIE>_
>
> > Extracción manual. La página de YouTube renderiza su contenido con JavaScript, así que
> > `original.html` (preservado verbatim, 1,1 MB) no trae ni el título ni la descripción del video.
> > Los datos de abajo salen del endpoint oEmbed público de YouTube
> > (`https://www.youtube.com/oembed?url=...&format=json`), consultado el 2026-08-05.
>
> ## Metadatos del video
>
> - **Título:** Move 37!! Lee Sedol vs AlphaGo Match 2
> - **Canal:** Daniel Estrada (<https://www.youtube.com/@DanielEstrada>)
> - **URL:** <https://www.youtube.com/watch?v=JNrXgpSEEIE>
> - **Miniatura:** <https://i.ytimg.com/vi/JNrXgpSEEIE/hqdefault.jpg>
> - **Tipo:** video
>
> ## Qué registra
>
> El momento de la jugada 37 en la segunda partida del match entre AlphaGo (DeepMind) y
> Lee Sedol, jugado en Seúl en marzo de 2016.
>
> ## Limitaciones de esta captura
>
> - No hay transcripción ni descripción del video: la captura no las alcanzó.
> - No se descargó la miniatura. La URL queda registrada arriba por si se la quiere usar en una diapositiva.
> - El contenido narrativo sobre la jugada 37 vive en las notas del orador de la diapositiva
>   correspondiente, no acá. Este registro documenta la fuente, no la interpreta.

`metadata.yaml` completo:

> ```yaml
> url: "https://www.youtube.com/watch?v=JNrXgpSEEIE"
> fetched_at: "2026-08-05T12:18:44Z"
> title: "Move 37!! Lee Sedol vs AlphaGo Match 2"
> http_status: 200
> byte_size: 1134502
> assets:
>   []
> extraction: "manual — page.md reescrito a mano; original.html es JS-rendered y no trae metadatos"
> channel: "Daniel Estrada"
> thumbnail: "https://i.ytimg.com/vi/JNrXgpSEEIE/hqdefault.jpg"
> ```
