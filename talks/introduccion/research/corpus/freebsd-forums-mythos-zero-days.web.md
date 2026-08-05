---
source_file: freebsd-forums-mythos-zero-days
source_type: web-capture
ingested_at: 2026-08-05
---

# AI finds thousands of zero-day exploits... including in FreeBSD. (hilo de The FreeBSD Forums)

## Provenance
- Ubicación original: `research/web/freebsd-forums-mythos-zero-days/`
- Formato: captura web (`original.html` 213.007 bytes + `page.md` 28.957 bytes + 22 assets)
- URL: https://forums.freebsd.org/threads/ai-finds-thousands-of-zero-day-exploits-including-in-freebsd.102288/
- Autor / fuente: hilo de foro. Iniciado por **blackbird9** el **8 de abril de 2026**, en las
  secciones *Base System → General*. 25 posts, del 8 al 9 de abril de 2026.
- Participantes (por orden de aparición): blackbird9 (OP), atax1a, cracauer@ (marcado
  **Developer**), rbranco, MG, OpenFreeNet, AlfredoLlaquet, bakul, LibreQuest, T-Aoki, msplsh
  (marcado **Developer** en el hilo mediante etiqueta de rol), loveydovey, mer.
- Capturado el: 2026-08-05T15:48:19Z · HTTP 200
- Fuente **terciaria**: es un foro donde usuarios comentan y citan artículos de prensa
  (The Hacker News, Tom's Hardware, ai.rs, dev.to) que a su vez citan a Anthropic.

### Nota sobre el estado de la captura (corrige el encuadre recibido)

El encargo de ingesta indicaba que `page.md` era "casi todo cromo de navegación" y que el contenido
sustantivo de los posts **no** había quedado en la captura estática, de modo que la afirmación
técnica clave solo existiría vía WebFetch. **Verificado contra el archivo: no es así.** El `page.md`
sí trae los 25 posts completos, incluida la afirmación sobre FreeBSD/NFS, que aparece verbatim en el
**post #20** de blackbird9 (9 de abril de 2026). Es cierto que el archivo arranca con ~80 líneas de
menú del sitio FreeBSD antes del primer post, y que el marcado del foro (avatares, permalinks,
"Click to expand...") ensucia la lectura, pero el cuerpo de los mensajes está entero.

Lo que **sí** es cierto y sostiene la advertencia original: la afirmación **no es del foro**. Está
citada dentro de un post que copia un artículo de dev.to, que a su vez enlaza a una publicación de
Anthropic. La cadena de procedencia se detalla abajo.

## Key claims

### La afirmación técnica sobre FreeBSD (la que importa para la clase)

Texto **verbatim**, tal como aparece en el post #20:

> On FreeBSD, Mythos [autonomously identified and exploited] a 17-year-old remote code execution
> vulnerability in the NFS service. Unauthenticated root access. Fully autonomous. No human
> steering.

**Cadena de procedencia de esa frase (tres saltos):**

1. La escribe **Valentin Monteiro** en dev.to, artículo *"Claude Mythos Finds Bugs Like a Senior Dev
   Finds Excuses to Skip Standup"*.
2. **blackbird9** la copia y pega en el post #20 del hilo de FreeBSD, el 9 de abril de 2026, bajo el
   comentario *"Another couple of articles with a bit more info"*.
3. El enlace de "autonomously identified and exploited" apunta a
   `https://red.anthropic.com/2026/mythos-preview/`, es decir, **a la propia publicación de
   Anthropic**. Ese documento **no fue capturado** y no está en el corpus.

**Estatus: afirmación reportada, no verificada.** Ni el foro ni la captura contienen número de CVE,
aviso del equipo de seguridad de FreeBSD (`security-advisories`), commit, parche ni reporte de bug.
El propio hilo discute la afirmación con escepticismo abierto (ver más abajo).

### Otras afirmaciones técnicas reportadas en el hilo (mismo estatus: reportadas, no verificadas)

Todas provienen de artículos citados por los participantes, no de los participantes:

- **OpenBSD**: fallo de **27 años** en la implementación de **TCP SACK**, con origen en **1999**;
  desbordamiento de entero con signo que permite denegación de servicio remota. Ya parcheado
  ("now-patched") según Tom's Hardware. (citado en posts #1 y #20)
- **FFmpeg**: defecto de **16 años** en el decodificador **H.264**; colisión de centinela que causa
  una escritura fuera de límites. Según la cita, las herramientas automáticas nunca lo detectaron:
  **5 millones de tests de fuzzing, cero resultados**; Mythos lo encontró analizando el código
  directamente. (post #20)
- **Kernel de Linux**: el modelo **encadenó múltiples vulnerabilidades** para construir una ruta
  completa de escalada de privilegios, derrotando protecciones endurecidas: **stack canaries,
  KASLR, W^X**. Descrito como cadena de ataque funcional, no como fallo aislado. (post #20)
- **Firefox 147**: el modelo desarrolló exploits de shell en JavaScript con éxito **181 veces**;
  **Claude Opus 4.6**, el mejor modelo anterior, **2 veces**. (post #20)
- **Vulnerabilidad de corrupción de memoria en un monitor de máquina virtual "memory-safe"**.
  (citado de Tom's Hardware, post #1)
- **CyberGym**: Mythos Preview supera a Opus 4.6 **83 % contra 67 %** (dato del resumen del artículo
  de ai.rs enlazado en el post #20; no desarrollado en el hilo).
- **Titular de Tom's Hardware**: "miles de vulnerabilidades zero-day" en "todo sistema operativo
  importante y todo navegador web importante", algunas sin parchear durante décadas.
- **Nicholas Carlini / Claude Code y FreeBSD**: en un hilo hermano del mismo foro
  (*"Claude Code cracks FreeBSD within four hours"*, enlazado en el post #6), se reporta que Carlini
  trabajó ~4 horas sobre FreeBSD asistido por Claude y que el modelo hizo gran parte del trabajo de
  forma autónoma, desde identificar la vulnerabilidad hasta el exploit terminado. **Ese hilo no está
  capturado**; acá solo consta el enlace y su resumen.

### Afirmaciones sobre el programa (Project Glasswing)

- Cita textual del sitio de Anthropic, reproducida por **OpenFreeNet** en el post #12:
  *"The model will be used by a small set of organizations, including Amazon Web Services, Apple,
  Broadcom, Cisco, CrowdStrike, Google, JPMorgan Chase, the Linux Foundation, Microsoft, NVIDIA, and
  Palo Alto Networks, along with Anthropic, to secure critical software."*
- Interpretación del mismo participante: antes de liberar el modelo, parchearán infraestructura de
  software importante.
- **blackbird9** (#13) reporta, desde un noticiero, que *"no está seguro de que piensen liberarlo
  nunca"*: lo venderían a empresas socias para identificar y arreglar exploits, sin liberación
  general, por considerarlo demasiado peligroso.
- El tema llegó al **noticiero vespertino de la BBC**, cosa que el OP marca como inusual (#6).

## Definitions and terminology

- **Zero-day / día cero**: vulnerabilidad aún sin parche público. El hilo la usa en su sentido
  habitual; nadie la define.
- **NFS (Network File System)**: el servicio de FreeBSD donde se ubica la RCE de 17 años reportada.
- **RCE (remote code execution)** + **unauthenticated root access**: ejecución remota de código sin
  credenciales previas y con privilegios de root. Es la combinación de máxima severidad; por eso la
  afirmación es fuerte y por eso su falta de respaldo publicado importa.
- **"Fully autonomous. No human steering."**: la parte de la afirmación que carga el peso retórico —
  no es "una persona usando la herramienta", es el modelo actuando solo. Es exactamente el punto que
  el hilo pone en duda por no poder inspeccionarse.
- **TCP SACK (Selective Acknowledgment)**: extensión de TCP donde se ubica el fallo de OpenBSD.
- **Stack canaries / KASLR / W^X**: mitigaciones del kernel de Linux que, según la cita, la cadena
  de exploits derrotó.
- **Fuzzing**: prueba automática por entradas aleatorias/mutadas. La cifra de "5 millones de tests"
  de FFmpeg es el contraste que se usa para argumentar que el modelo hace algo distinto (análisis
  directo del código) y no "más de lo mismo".
- **CyberGym**: benchmark de capacidades de ciberseguridad; solo aparece nombrado.
- **"protection racket"** (atax1a, #2; retomado por blackbird9, #21): el término que el hilo usa
  para el modelo de negocio — encontrar los agujeros y cobrar por decir dónde están.

## Evidence and examples

**Dentro del hilo no hay evidencia primaria de ningún tipo.** Lo que hay es:

- Cuatro enlaces a artículos de prensa/blogs (The Hacker News, Tom's Hardware, ai.rs, dev.to) con
  sus tarjetas de vista previa.
- Un enlace a un post de Mastodon (Jenniferplusplus en hachyderm.io) que argumenta lo contrario.
- Un enlace a un hilo hermano del mismo foro sobre Carlini y Claude Code.
- Dos enlaces a Anthropic (`anthropic.com/glasswing` y `red.anthropic.com/2026/mythos-preview/`),
  **ninguno de los dos capturado**.
- **Un único testimonio de primera mano**, de un desarrollador de FreeBSD:

  > cracauer@ (#3): "I had Claude Code find real bugs including trickier ones."
  >
  > cracauer@ (#7): "I'm talking about running CC on my own code by myself. There was less than 50%
  > BS in there so far. I have no experience being the target of third parties doing it on my code."

  Es la única observación empírica directa del hilo, y es modesta: bugs reales en su propio código,
  con una tasa de falsos positivos que él estima **por debajo del 50 %**. No se refiere a Mythos
  (que es inaccesible) sino a **Claude Code**, un producto distinto y público.

## Inconsistencies / open questions

Esta sección es la que un docente necesita leer antes de proyectar cualquier cifra de este hilo.

### Qué está verificado

- **Que el hilo existe y dice lo que dice.** La captura es fiel: HTTP 200, HTML completo, 25 posts.
  Es citable como *documento de recepción*: cómo reaccionó una comunidad técnica veterana ante el
  anuncio, en caliente, el 8 y 9 de abril de 2026.
- **Que la comunidad de FreeBSD discutió el tema con escepticismo mayoritario.** Eso es observable
  directamente en la fuente y no depende de terceros.
- **Nada más.** Ninguna afirmación técnica está verificada dentro de esta fuente.

### Qué es afirmación de una sola fuente (y de qué fuente)

- La RCE de **17 años en NFS de FreeBSD** es, en última instancia, **afirmación de Anthropic sobre
  sí misma** (`red.anthropic.com/2026/mythos-preview/`), reproducida por un blog (dev.to) y pegada
  en un foro. **Tres saltos de distancia respecto del dato original, y cero confirmación
  independiente.** No es "lo dice el foro de FreeBSD": es "un usuario del foro cita a un blog que
  cita a Anthropic".
- Lo mismo vale para OpenBSD/27 años, FFmpeg/16 años, la cadena del kernel de Linux, los 181
  exploits de Firefox 147 y el 83 % vs 67 % de CyberGym: **todos remiten a la misma publicación de
  Anthropic**, no a hallazgos independientes. No son cinco fuentes: es una fuente citada cinco
  veces.

### Qué no tiene respaldo técnico publicado

- **No hay número de CVE** para el fallo de NFS. Ni en el hilo, ni en la captura.
- **No hay aviso del equipo de seguridad de FreeBSD.** Ningún participante enlaza un
  `FreeBSD-SA-…`, un commit, un parche ni un reporte en Bugzilla. En un hilo del foro oficial de
  FreeBSD, con al menos un desarrollador del proyecto participando, **nadie lo aporta** — dato
  significativo por sí mismo.
- **El modelo no es inspeccionable.** cracauer@ (#9) lo plantea en una sola línea y msplsh (#18) se
  lo confirma: *"Correct me if I'm wrong, but Anthropic doesn't publish the holes right now, and the
  reports are from a LLM not even accessible by the public yet?"* → *"That's correct."* La
  afirmación central es, por diseño, **no reproducible por terceros**.
- **`red.anthropic.com/2026/mythos-preview/` no está en el corpus.** Si la clase va a citar la cifra
  de FreeBSD, la fuente honesta a capturar es esa, no este hilo.

### Contradicciones y tensiones internas del hilo (preservar, no promediar)

- **Escepticismo frontal vs. experiencia directa.** atax1a (#2) llama al anuncio *"marketing
  bullshit by a company that lies to prop up its value, and acts like a protection racket"*.
  cracauer@ (#3), desarrollador de FreeBSD, responde con un contraejemplo empírico: encontró bugs
  reales con Claude Code. atax1a (#4) no lo concede: *"sift through enough of the sewage, you'll
  find one or two pieces of corn"*. **El hilo no resuelve esta tensión.**
- **"No es impresionante" vs. "es inevitable".** MG (#8) sostiene que la explotación de software
  requiere razonamiento humano por naturaleza y que cualquier agujero hallable solo con software no
  puede impresionar. AlfredoLlaquet (#14) dice que encontrar bugs es tarea sencilla para un
  reconocedor de patrones. En la vereda opuesta, msplsh (#18) plantea que la discusión sobre si vale
  la pena es irrelevante: *"FreeBSD doesn't get to decide if it is 'worthwhile participating'. The
  choice is participate now, or let somebody else use the tool on FreeBSD later and 'participate' by
  having zero-days drop like rain."*
- **Autocorrección del OP.** blackbird9 (#6) reconoce haber duplicado un hilo previo:
  *"Yes I just realised I may have been guilty of re-posting the same thing... although that was
  specifically about freebsd."*
- **Hilo abandonado.** MG (#8) pregunta si existe algún gráfico estadístico sobre el aumento de
  sistemas comprometidos a raíz de esto. **Nadie responde.** Es la pregunta empírica más directa del
  hilo y queda sin contestar.
- **Deriva off-topic.** Los posts #14–#16 se van a chistes (qué nombre viene después de "Mythos" —
  "Pathos", "Deity"; el mejor zero-day es la contraseña en un post-it). AlfredoLlaquet (#14) se
  declara *"anti-talking-about-AI now"* y a la vez sigue participando, contradicción que él mismo
  señala: *"(Yes, yes, yes, I'm being contradictory, but how do you protest protests?)"*.
- **Especulación sin base.** blackbird9 (#24) sugiere que la NSA y sus equivalentes extranjeros
  podrían tener esta capacidad desde hace tiempo; loveydovey (#25) asiente. **Es especulación
  explícita**, sin ninguna evidencia, y no debe citarse como dato.
- **Una advertencia técnica que sí conviene rescatar.** T-Aoki (#17): la atención a los
  **falsos positivos** es obligatoria, y hay código peligroso cerca del hardware que es inevitable
  para que ciertos dispositivos funcionen. Es el matiz de ingeniería que el resto del hilo no
  desarrolla, y cuadra con el <50 % de ruido que reporta cracauer@.

### Riesgo concreto para quien cite esta fuente en clase

Proyectar "en FreeBSD, una IA explotó sola una RCE de 17 años en NFS" **con este hilo como fuente al
pie es una atribución incorrecta**: sugiere que lo dice la comunidad de FreeBSD, cuando lo dice
Anthropic y el foro lo está poniendo en duda. Si la afirmación entra en la charla, tiene que entrar
etiquetada como *afirmación de Anthropic, reportada por prensa, sin CVE ni aviso de seguridad
publicado, discutida con escepticismo en el foro oficial de FreeBSD*. Con ese encuadre, la fuente es
excelente — porque el escepticismo **es** el contenido.

## Images / diagrams

22 imágenes copiadas a la carpeta companion desde
`research/web/freebsd-forums-mythos-zero-days/assets/`. Dos assets de dev.to estaban guardados con
el nombre de su URL percent-encoded completa; se copiaron con el nombre final del archivo
(`zhbx130qs0xzb28lvac9.png`, `8j7kvp660rqzt99zui8e.png`), rastreable vía `metadata.yaml`.

Ninguna imagen del hilo es una figura técnica: no hay diagramas, gráficos ni capturas de código.
Son tarjetas de vista previa de enlaces (arte editorial de los artículos citados), avatares de
usuarios, logos y favicons.

**Tarjetas de vista previa de artículos enlazados (4) — pendientes de transcripción.** Suelen llevar
titular incrustado en la imagen; hasta transcribirlas no se sabe qué texto contienen.

- `freebsd-forums-mythos-zero-days.web/images/claude-mythos.png`
  - Provenance: post #1 de blackbird9; tarjeta del artículo de The Hacker News
    *"Anthropic's Claude Mythos Finds Thousands of Zero-Day Flaws Across Major Systems"*.
    Alt = "thehackernews.com". Origen: blogger.googleusercontent.com. 276.609 bytes.
  - <!-- pending: process_images -->
- `freebsd-forums-mythos-zero-days.web/images/iAtJT6Ab8gPu3iDZq9bCnL-1920-80.jpg`
  - Provenance: post #1 de blackbird9; tarjeta del artículo de Tom's Hardware sobre las "miles de
    vulnerabilidades zero-day". Alt = "www.tomshardware.com". Origen: cdn.mos.cms.futurecdn.net.
    225.218 bytes.
  - <!-- pending: process_images -->
- `freebsd-forums-mythos-zero-days.web/images/claude-mythos-glasswing-why-gated.png`
  - Provenance: post #20 de blackbird9; tarjeta del artículo de ai.rs *"Claude Mythos Preview: Why
    Anthropic Locked Its Best Security Model Behind a Wall"*. Alt = "ai.rs". 89.727 bytes.
  - <!-- pending: process_images -->
- `freebsd-forums-mythos-zero-days.web/images/zhbx130qs0xzb28lvac9.png`
  - Provenance: post #20 de blackbird9; tarjeta del artículo de dev.to de Valentin Monteiro
    *"Claude Mythos Finds Bugs Like a Senior Dev Finds Excuses to Skip Standup"* — **el artículo del
    que sale la cita textual sobre FreeBSD/NFS**. Alt = "dev.to". 187.124 bytes.
  - <!-- pending: process_images -->

**Cromo del sitio, avatares y favicons (18) — sin valor expositivo, no requieren transcripción.**

- `freebsd-forums-mythos-zero-days.web/images/freebsd_logo.png`
  - Provenance: cabecera del sitio; alt = "FreeBSD".
  - Depiction: logotipo del proyecto FreeBSD. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/logo.og.png`
  - Provenance: tarjeta de vista previa del hilo hermano en el propio foro (post #6);
    alt = "forums.freebsd.org".
  - Depiction: logotipo Open Graph de forums.freebsd.org. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/58187.jpg`
  - Provenance: avatar de **blackbird9** (OP), repetido en posts #1, #6, #13, #20, #21, #23, #24.
  - Depiction: avatar de usuario. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/81721.jpg`
  - Provenance: avatar de **atax1a**, posts #2, #4, #11.
  - Depiction: avatar de usuario. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/74.jpg`
  - Provenance: avatar de **cracauer@** (Developer), posts #3, #7, #9.
  - Depiction: avatar de usuario. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/77978.jpg`
  - Provenance: avatar de **rbranco**, post #5.
  - Depiction: avatar de usuario. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/1018.jpg`
  - Provenance: avatar de **MG**, posts #8, #10.
  - Depiction: avatar de usuario. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/84001.jpg`
  - Provenance: avatar de **OpenFreeNet**, post #12.
  - Depiction: avatar de usuario. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/74462.jpg`
  - Provenance: avatar de **LibreQuest**, post #16.
  - Depiction: avatar de usuario. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/52451.jpg`
  - Provenance: avatar de **msplsh**, post #18.
  - Depiction: avatar de usuario. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/84248.jpg`
  - Provenance: avatar de **loveydovey**, posts #19, #25.
  - Depiction: avatar de usuario. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/thn.jpg`
  - Provenance: favicon de thehackernews.com en la tarjeta del post #1 (32 px).
  - Depiction: icono de sitio. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/favicon.ico`
  - Provenance: favicon de tomshardware.com en la tarjeta del post #1.
  - Depiction: icono de sitio. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/favicon-2.ico`
  - Provenance: favicon de forums.freebsd.org en la tarjeta del post #6.
  - Depiction: icono de sitio. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/favicon-32x32.png`
  - Provenance: favicon de ai.rs en la tarjeta del post #20.
  - Depiction: icono de sitio. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/7b1cc534bd3a902c.png`
  - Provenance: icono de hachyderm.io en la tarjeta del post de Mastodon citado por atax1a (#2).
  - Depiction: icono de instancia de Mastodon. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/8j7kvp660rqzt99zui8e.png`
  - Provenance: favicon de dev.to (32 px) en la tarjeta del post #20. Nombre original en `assets/`:
    URL percent-encoded completa.
  - Depiction: icono de sitio. · Why it matters: no aplica.
- `freebsd-forums-mythos-zero-days.web/images/1f600.png`
  - Provenance: emoji JoyPixels `:D` usado por LibreQuest en el post #16.
  - Depiction: emoji de cara sonriente. · Why it matters: no aplica.

## Raw / preserved excerpts

Transcripción completa de los 25 posts del hilo, en orden, con el marcado de foro (menús, avatares,
permalinks, "Click to expand...") retirado. Texto de los mensajes **verbatim**.

> **Hilo:** AI finds thousands of zero-day exploits... including in FreeBSD.
> **Foro:** Base System → General · **Iniciado por:** blackbird9 · **Fecha de inicio:** Apr 8, 2026

> **#1 — blackbird9 (OP) · Apr 8, 2026**
>
> Anthropic Claude Mythos...
>
> [enlace] *Anthropic's Claude Mythos Finds Thousands of Zero-Day Flaws Across Major Systems* —
> thehackernews.com
> <https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html>
> "Claude Mythos finds thousands of zero-days as Anthropic launches Project Glasswing, enhancing
> defenses but exposing AI security risks."
>
> [enlace] *Anthropic's latest AI model identifies 'thousands of zero-day vulnerabilities' in 'every
> major operating system and every major web browser' — Claude Mythos Preview sparks race to fix
> critical bugs, some unpatched for decades* — www.tomshardware.com
> "Anthropic holds back its most advanced model yet to allow companies and institutions to prepare."
>
> Quote: "Mythos Preview, Anthropic claimed, has already discovered [red.anthropic.com/2026/mythos-preview/]
> thousands of high-severity zero-day vulnerabilities in every major operating system and web
> browser. Some of these include a now-patched 27-year-old bug in OpenBSD, a 16-year-old flaw in
> FFmpeg, and a memory-corrupting vulnerability in a memory-safe virtual machine monitor."

> **#2 — atax1a · Apr 8, 2026**
>
> counterpoint: this is marketing bullshit by a company that lies to prop up its value, and acts
> like a protection racket
>
> [enlace] *Jenniferplusplus (@jenniferplusplus@hachyderm.io)* —
> <https://hachyderm.io/@jenniferplusplus/116370960046107139>
> "There's one very important thing I would like everyone to try to remember this week, and it is
> that AI companies are full of shit Only rarely do their claims actually bear scrutiny, and those
> are only the mildest of claims they make. So, anthropic is claiming that their new, secret,
> unreleased..."
>
> they are drowning us in slop reports, and then trying to sell us slop-based solutions to manage
> all of it. shit behavior from garbage capitalists.

> **#3 — cracauer@ (Developer) · Apr 8, 2026**
>
> I had Claude Code find real bugs including trickier ones.

> **#4 — atax1a · Apr 8, 2026**
>
> yes, i'm sure if you sift through enough of the sewage, you'll find one or two pieces of corn.
> nothing about this is healthy or sustainable or worthwhile.

> **#5 — rbranco · Apr 8, 2026**
>
> Also OpenBSD. But I think there was another thread where we were discussing this.

> **#6 — blackbird9 (Thread Starter) · Apr 8, 2026**
>
> Yes I just realised I may have been guilty of re-posting the same thing... although that was
> specifically about freebsd.
>
> [enlace] *Claude Code cracks FreeBSD within four hours* — forums.freebsd.org
> <https://forums.freebsd.org/threads/claude-code-cracks-freebsd-within-four-hours.102251/unread>
> "For about four hours, Nicholas Carlini worked on FreeBSD supported by Anthropic's Claude. Carlini
> states that Claude performed a large part of the work autonomously, from identifying the
> vulnerability to the finished exploit. ☄️..."
>
> I thought the articles about mythos were interesting anyway. It even made the BBC evening news
> here, which is pretty unusual...

> **#7 — cracauer@ (Developer) · Apr 8, 2026**
>
> > atax1a said: yes, i'm sure if you sift through enough of the sewage, you'll find one or two
> > pieces of corn. nothing about this is healthy or sustainable or worthwhile.
>
> I'm talking about running CC on my own code by myself. There was less than 50% BS in there so far.
>
> I have no experience being the target of third parties doing it on my code.

> **#8 — MG · Apr 8, 2026**
>
> There should be a notable increase in compromised systems worldwide due to Claude hacking
> business. Is there any statisctical graph about it?
>
> I don't think it works like this. Software exploitation is a method that requires human reasoning
> naturally. Any hole that can be found with software only can't be impressive. The knowledge to
> find it already existed and can be found with logic.

> **#9 — cracauer@ (Developer) · Apr 8, 2026**
>
> Correct me if I'm wrong, but Anthropic doesn't publish the holes right now, and the reports are
> from a LLM not even accessible by the public yet?

> **#10 — MG · Apr 8, 2026**
>
> > cracauer@ said: Correct me if I'm wrong, but Anthropic doesn't publish the holes right now, and
> > the reports are from a LLM not even accessible by the public yet?
>
> They are just bug-hunting for p&r? It wouldn't surprise me. Find public software and run
> professional security audits

> **#11 — atax1a · Apr 8, 2026**
>
> "i have a scary bogeyman of an AI that will end computer security!!" okay, can we see it? "no".
>
> again, this is just corporate asswipes trying to force their way in to make you pay attention to
> their slop. it's a show of force by technocratic fascists.

> **#12 — OpenFreeNet · Apr 8, 2026**
>
> > cracauer@ said: Correct me if I'm wrong, but Anthropic doesn't publish the holes right now, and
> > the reports are from a LLM not even accessible by the public yet?
>
> yes, but "The model will be used [anthropic.com/glasswing] by a small set of organizations,
> including Amazon Web Services, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorgan Chase, the
> Linux Foundation, Microsoft, NVIDIA, and Palo Alto Networks, along with Anthropic, to secure
> critical software."
>
> So before release it, they will patch important software infrastructure.

> **#13 — blackbird9 (Thread Starter) · Apr 8, 2026**
>
> From what I heard I'm not sure they intend ever to release it. Instead they will sell it to
> industry partner companies to identify and fix exploits, but will not release it for general use.
> That was the gist of the news report I heard earlier. They consider it too dangerous to put it out
> on general release.
>
> I'm sure the opposition is working on the same kind of thing...

> **#14 — AlfredoLlaquet · Apr 9, 2026**
>
> Finding bugs or exploits in software seems an extremely simple task for a very sophisticated
> contrivance whose specialty is recognizing patterns. I'm not impressed at all. They are just
> feeding their little machine the baby food it knows how to chew well, so it can shine. Oh, look
> how well our little machine chews its baby food! It's just more Anthropic being good at niche
> marketing. Nothing new.
>
> Also, I wonder where the escalation in naming will lead. What comes after "Mythos"? "Deity,"
> perhaps?
>
> I'm anti-talking-about-AI now. I'm very fed up with the thing. There are other things happening in
> the world. (Yes, yes, yes, I'm being contradictory, but how do you protest protests?).
>
> And now, sports.

> **#15 — bakul · Apr 9, 2026**
>
> > AlfredoLlaquet said: What comes after "Mythos"?
>
> Pathos.

> **#16 — LibreQuest · Apr 9, 2026**
>
> The best zero day exploit is written on a sticky note under the keyboard in the form of username
> and password. :D Did AI check there?

> **#17 — T-Aoki · Apr 9, 2026**
>
> This would be relatively "safe" use-case of AI / LLM, compared with using codes generated by
> AI / LLM that has possible fatal copyright issues in the future.
>
> But special attentions is mandatory for false-positives.
> There should be warned dangerous codes near the hardware level that should be unavoidable to make
> some devices to just work.

> **#18 — msplsh · Apr 9, 2026**
>
> > cracauer@ said: Correct me if I'm wrong, but Anthropic doesn't publish the holes right now, and
> > the reports are from a LLM not even accessible by the public yet?
>
> That's correct.
>
> > atax1a said: worthwhile
>
> Slight problem, FreeBSD doesn't get to decide if it is "worthwhile participating." The choice is
> participate now, or let somebody else use the tool on FreeBSD later and "participate" by having
> zero-days drop like rain.

> **#19 — loveydovey · Apr 9, 2026**
>
> It's obvious you don't trust your security to anyone else who has no stake in your security. Which
> is why the only true way to not have exploits is to write your own OS. Which is a formidable task.

> **#20 — blackbird9 (Thread Starter) · Apr 9, 2026**
>
> Another couple of articles with a bit more info
>
> [enlace] *Claude Mythos Preview: Why Anthropic Locked Its Best Security Model Behind a Wall* —
> ai.rs · <https://ai.rs/ai-for-business/claude-mythos-glasswing-why-gated>
> "Claude Mythos Preview found a 27-year-old OpenBSD vulnerability and beats Opus 4.6 on CyberGym
> 83% to 67%. We break down Project Glasswing access, the 12 founding partners, the pricing, and why
> Anthropic isn't selling it to you."
>
> [enlace] *Claude Mythos Finds Bugs Like a Senior Dev Finds Excuses to Skip Standup* — dev.to
> <https://dev.to/valentin_monteiro/claude-mythos-finds-bugs-like-a-senior-dev-finds-excuses-to-skip-standup-2h07>
> "A bug in OpenBSD. It had been there for 27 years. 27 years of code reviews, security audits,
> version..."
>
> "A flaw in OpenBSD's TCP SACK implementation dating back to 1999. A signed integer overflow
> allowing remote denial-of-service. The kind of bug that survived hundreds of reviews, dozens of
> major releases, thousands of pairs of eyes. Still there.
>
> A defect in FFmpeg's H.264 decoder, 16 years old. A sentinel collision causing an out-of-bounds
> write. Automated tools never caught it. Not for lack of trying: 5 million fuzz tests
> [red.anthropic.com/2026/mythos-preview/]. Zero results. Mythos found it by analyzing the code
> directly."
>
> Although it doesn't say so, what would have impressed me would be if it only found ONE bug in
> openbsd... we don't know the full number, of course.
>
> "The model chained multiple Linux kernel vulnerabilities to build a full privilege escalation
> path, defeating hardened protections: stack canaries, KASLR, W^X. Not an isolated flaw. A working
> attack chain.
>
> On FreeBSD, Mythos autonomously identified and exploited
> [red.anthropic.com/2026/mythos-preview/] a 17-year-old remote code execution vulnerability in the
> NFS service. Unauthenticated root access. Fully autonomous. No human steering.
>
> And then there's this: against Firefox 147, the model successfully developed JavaScript shell
> exploits 181 times [red.anthropic.com/2026/mythos-preview/]. Claude Opus 4.6, the previous best
> model? Twice."
>
> Browsers look to be much more exploitable than operating systems, as expected.

> **#21 — blackbird9 (Thread Starter) · Apr 9, 2026**
>
> > msplsh said: Slight problem, FreeBSD doesn't get to decide if it is "worthwhile participating."
> > The choice is participate now, or let somebody else use the tool on FreeBSD later and
> > "participate" by having zero-days drop like rain.
>
> Or... someone else, somewhere else, develops a similar AI with similar capabilities, which you
> have no option of participating in, and that is going to be used against you. If anthropic can do
> this... others can, or will soon have that capability. "What one fool can do, another can".
>
> What would be somewhat annoying is if they want money to tell you where the bugs are... given that
> they were handed the code that they analysed for free in the first place. Although I suppose there
> is a certain cost to building and running the model, however, if they are skimming a big margin
> from it, that doesn't sound very attractive to me, more like a protection racket, as ataxia said.

> **#22 — mer · Apr 9, 2026**
>
> > blackbird9 said: Browsers look to be much more exploitable than operating systems, as expected.
>
> I would say "applications". The problem is "what happens after the exploit"

> **#23 — blackbird9 (Thread Starter) · Apr 9, 2026**
>
> Perhaps, although the majority of apps don't contain a language interpreter. Javascript was the
> primary tool exploited, according to that article. I bet there are similar problems with things
> like pdfs and spreadsheets.

> **#24 — blackbird9 (Thread Starter) · Apr 9, 2026**
>
> Well... let's see if MS submits the windows source code for the AI's evaluation. Although if they
> do, it's going to be NDA'd to high heaven, so we will probably never know.
>
> And for all we know, outfits like the NSA, and their foreign equivalents, may have already had
> this kind of capability for some time, and kept quiet about it. Usually when something makes it
> out into civvie street, it's already been used for some time by the security services.

> **#25 — loveydovey · Apr 9, 2026**
>
> > blackbird9 said: Usually when something makes it out into civvie street, it's already been used
> > for some time by the security services.
>
> Haha, you bet. Public domain lags by decades.

*(Cierre del hilo en la captura: "You must log in or register to reply here.")*

`metadata.yaml` — encabezado (la lista completa de 34 entradas de `assets`, con duplicados marcados
`deduped: True`, queda en el archivo original):

> ```yaml
> url: "https://forums.freebsd.org/threads/ai-finds-thousands-of-zero-day-exploits-including-in-freebsd.102288/"
> fetched_at: "2026-08-05T15:48:19Z"
> title: "AI finds thousands of zero-day exploits... including in FreeBSD. | The FreeBSD ForumsThread starterStart date"
> http_status: 200
> byte_size: 213007
> ```
