---
source_file: slido-preguntas-en-vivo
source_type: web-capture
ingested_at: 2026-08-05
---

# Slido — evento de preguntas en vivo (Clase 1)

## Provenance
- Ubicación original: `research/web/slido-preguntas-en-vivo/`
- Formato: captura web (`original.html` 73.879 bytes + `page.md` reescrito a mano)
- URL: https://app.sli.do/event/s7Ccr6C4awbUzRW1RpH19c
- Autor / fuente: evento creado por la cátedra en Slido
- Capturado el: 2026-08-05T15:26:17Z · HTTP 200
- Título que devolvió la página: *"Join Slido: Enter #code to vote and ask questions"*
- **Extracción manual.** Slido es una aplicación de una sola página: `original.html` trae el shell
  de la app y la pantalla de ingreso, no el contenido del evento. `page.md` fue reescrito a mano
  para documentar qué es la fuente y qué no contiene. El `metadata.yaml` lo declara en el campo
  `extraction`.

## Key claims

Esta fuente **no argumenta nada**: es un puntero a una herramienta de participación en vivo. Lo que
la captura establece con certeza:

- Existe un evento público de Slido en `https://app.sli.do/event/s7Ccr6C4awbUzRW1RpH19c`.
- La página de ingreso responde 200 y ofrece entrar por URL o por código de evento, para votar y
  dejar preguntas.
- El evento se corre en clase; la captura es previa a cualquier respuesta.

## Definitions and terminology

- **Slido**: plataforma de participación en vivo. El presentador crea un evento con preguntas
  (encuestas, nube de palabras, Q&A abierto) y la audiencia responde desde el celular. Los
  resultados se proyectan desde el panel del presentador.
- **Código de evento**: alternativa a la URL para que la audiencia entre.

## Evidence and examples

Ninguna dentro de la captura.

## Inconsistencies / open questions

- **Las preguntas configuradas no están en la captura.** Viven detrás de la cuenta del presentador.
  Las cuatro preguntas que figuran en la diapositiva "Ahora cuéntennos ustedes" son **propuesta
  editorial** y tienen que confirmarse contra lo que esté efectivamente cargado en el evento. Si no
  coinciden, la diapositiva proyecta preguntas que la audiencia no va a encontrar al entrar.
- **Sin respuestas ni resultados**: el evento no se había corrido al momento de la captura.
- **Sin fecha de expiración conocida.** Los eventos de Slido pueden archivarse o vencer según el
  plan de la cuenta. Conviene verificar que el enlace siga vivo antes de la clase.
- **Riesgo para quien cite esta fuente:** sirve como enlace operativo para proyectar, no como
  respaldo de ninguna afirmación de contenido.

## Images / diagrams

Ninguna. `metadata.yaml` declara `assets: []`. La carpeta companion
`slido-preguntas-en-vivo.web/images/` existe y está vacía.

## Raw / preserved excerpts

Contenido completo de `page.md` (extracción manual), preservado verbatim:

> # Slido — evento de preguntas en vivo (Clase 1)
>
> _Source: <https://app.sli.do/event/s7Ccr6C4awbUzRW1RpH19c>_
>
> > Extracción manual. Slido es una aplicación de una sola página: `original.html` (preservado
> > verbatim, 74 KB) trae el shell de la app y la pantalla de ingreso, no el contenido del evento.
> > Las preguntas configuradas viven detrás de la cuenta del presentador y no se pueden capturar
> > desde acá.
>
> ## Qué es
>
> Evento de Slido que el presentador abre durante la Clase 1 para recoger respuestas del curso en
> vivo. La audiencia entra por la URL o por el código del evento, vota y deja preguntas.
>
> ## Metadatos
>
> - **URL del evento:** <https://app.sli.do/event/s7Ccr6C4awbUzRW1RpH19c>
> - **Título de la página de ingreso:** "Join Slido: Enter #code to vote and ask questions"
> - **Estado HTTP:** 200
> - **Capturado:** 2026-08-05
>
> ## Limitaciones de esta captura
>
> - Las preguntas configuradas en el evento no están en la captura. Las que figuran en la diapositiva
>   del deck son una propuesta editorial y tienen que coincidir con lo que el presentador cargó en
>   Slido.
> - Sin respuestas ni resultados: el evento se corre en clase.

`metadata.yaml` completo:

> ```yaml
> url: "https://app.sli.do/event/s7Ccr6C4awbUzRW1RpH19c"
> fetched_at: "2026-08-05T15:26:17Z"
> title: "Slido — evento de preguntas en vivo (Clase 1)"
> http_status: 200
> byte_size: 73879
> assets:
>   []
> extraction: "manual — page.md reescrito a mano; original.html es el shell JS de la app"
> ```
