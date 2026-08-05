---
source_file: engadget-mythos-glasswing-10000
source_type: web-capture
ingested_at: 2026-08-05
---

# Anthropic says Mythos has already found more than 10,000 vulnerabilities (Engadget)

## Provenance
- Ubicación original: `research/web/engadget-mythos-glasswing-10000/`
- Formato: captura web (`original.html` 59.163 bytes + `page.md` + 3 assets)
- URL: https://www.engadget.com/2180028/anthropic-claude-mythos-preview-project-glasswing-update/
- Autor / fuente: **Mariella Moon**, para **Engadget** (Static Media). Secciones: News, AI.
- Fecha del original: **23 de mayo de 2026, 8:48 am EST**
- Capturado el: 2026-08-05T15:48:21Z · HTTP 200
- Crédito de la foto: Michael M. Santiago / Getty Images
- **La captura sí trae el cuerpo del artículo completo.** No hubo que recurrir a extracción manual
  ni a `original.html`: `page.md` contiene el texto entero, con un poco de cromo del sitio al
  principio (aviso de copyright, logos, migas de categoría) y el corte final en la sección
  "Recommended".
- Fuente **secundaria**: periodismo tecnológico que informa sobre un reporte de Anthropic. Todas las
  cifras del artículo son atribuidas explícitamente a Anthropic o a los propios socios.

## Key claims

Subtítulo del artículo: *"The company has published an update about Project Glasswing, a month after
its launch."*

- Anthropic publicó un **informe inicial de Project Glasswing**, la iniciativa de ciberseguridad
  lanzada en **abril de 2026** que busca prevenir ciberataques de IA con IA. Enlace del artículo al
  informe: `https://www.anthropic.com/research/glasswing-initial-update`.
- La iniciativa está impulsada por **Claude Mythos Preview**, el modelo **no liberado** de la
  empresa.
- **Más de 10.000 vulnerabilidades** encontradas por los socios en total, **apenas un mes después**
  del lanzamiento de Glasswing.
- La mayoría de los socios *"each found hundreds of critical- or high-severity vulnerabilities in
  their software"* usando el modelo.
- La **tasa de detección de bugs de los socios aumentó más de diez veces** (factor >10).
- **Cloudflare: 2.000 bugs**, de los cuales **400 son de severidad alta o crítica**.
- **Mozilla: 271 vulnerabilidades de Firefox** encontradas y corregidas — **10 veces más** de lo que
  había encontrado en una versión anterior del navegador usando otro modelo de Claude. (Engadget
  aclara que Mozilla ya lo había reportado antes, con enlace a su propia nota previa.)
- **Microsoft**: su anuncio de que los paquetes de parches *"continue trending larger for some
  time"* se debe, aparentemente, a los bugs encontrados vía Mythos Preview. Enlace al blog del MSRC
  (`microsoft.com/en-us/msrc/blog/2026/05/a-note-on-patch-tuesday`).
- **Barrido de open source**: Anthropic usó Mythos Preview para escanear **1.000 proyectos de código
  abierto** en los últimos meses y encontró **6.202 vulnerabilidades de severidad alta y crítica
  sobre 23.019** (total de vulnerabilidades halladas).
- **macOS**: una firma de investigación en seguridad afirmó recientemente haber encontrado una forma
  de vulnerar macOS con ayuda de las capacidades de Mythos. **Engadget marca explícitamente que
  Anthropic no incluyó esto en su informe.**
- **Motivo de la no liberación**: Anthropic explica en el informe que **ninguna empresa (incluida
  ella misma) ha desarrollado salvaguardas lo bastante fuertes** para impedir el uso indebido de
  modelos como este. Pretende liberar *"Mythos-class models"* en el futuro, cuando esas salvaguardas
  existan.
- **Expansión**: planea trabajar con socios como el gobierno de EE. UU. y otros gobiernos para
  ampliar la disponibilidad de Glasswing. Engadget lee esto como señal de que la empresa podría
  estar reparando su relación con el gobierno de EE. UU. (al que demandó por una designación de
  riesgo en la cadena de suministro).
- **Socios nombrados en esta nota** (además de Cloudflare, Mozilla y Microsoft ya mencionados):
  **Amazon Web Services, Apple, CrowdStrike, Google, JPMorganChase, NVIDIA y Palo Alto Networks**.
- **Contexto financiero** (no es sobre seguridad, pero está en el artículo): según el *Wall Street
  Journal*, Anthropic estaría por ser rentable por primera vez desde su fundación en 2021, con
  ingresos proyectados de **10.900 millones de dólares** y una **ganancia operativa de 559 millones**
  para el trimestre que cierra en junio. La empresa **no espera seguir siendo rentable** en los
  trimestres siguientes, porque planea invertir más en cómputo y otros gastos.

## Definitions and terminology

- **Project Glasswing**: la iniciativa de ciberseguridad de Anthropic lanzada en abril de 2026,
  descrita como un esfuerzo para *"prevent AI cyberattacks with, well, AI"*.
- **Claude Mythos Preview**: el modelo no liberado que impulsa la iniciativa.
- **"Mythos-class models"**: la categoría de modelos que Anthropic dice que liberará en el futuro,
  cuando existan salvaguardas suficientes. Término de la empresa, sin definición técnica.
- **Severidad alta / crítica**: la nota usa la escala de severidad estándar de la industria sin
  definirla ni indicar qué sistema de puntaje (CVSS u otro) se aplicó a los conteos.

## Evidence and examples

Las cifras concretas del artículo, tal como aparecen, con su atribución:

| Dato | Cifra | Atribuido a |
|---|---|---|
| Vulnerabilidades halladas por los socios, primer mes | **más de 10.000** | Anthropic (informe Glasswing) |
| Aumento de la tasa de detección de los socios | **más de 10×** | Anthropic |
| Cloudflare — bugs totales | **2.000** | Anthropic / Cloudflare |
| Cloudflare — altos o críticos | **400** | Anthropic / Cloudflare |
| Mozilla — vulnerabilidades de Firefox corregidas | **271** | Mozilla (reporte previo) |
| Mozilla — multiplicador vs. modelo Claude anterior | **10×** | Mozilla |
| Barrido open source — proyectos escaneados | **1.000** | Anthropic |
| Barrido open source — altas y críticas | **6.202** | Anthropic |
| Barrido open source — total de vulnerabilidades | **23.019** | Anthropic |
| Anthropic — ingresos proyectados del trimestre a junio | **US$ 10.900 M** | Wall Street Journal |
| Anthropic — ganancia operativa del trimestre | **US$ 559 M** | Wall Street Journal |

Ejemplos cualitativos citados: el crecimiento del tamaño de los Patch Tuesday de Microsoft y el
exploit de macOS reportado por una firma de investigación externa (esta última, fuera del informe de
Anthropic).

## Inconsistencies / open questions

Para un docente que va a citar estas cifras en clase:

### Qué está verificado

- **Que Engadget publicó estas cifras el 23 de mayo de 2026, con esta atribución.** Eso es
  verificable directamente contra la captura (HTTP 200, cuerpo completo).
- **Que Anthropic publicó un informe inicial de Glasswing** con esas cifras: el artículo enlaza el
  documento (`anthropic.com/research/glasswing-initial-update`). El informe **no está capturado en
  este corpus**; solo consta el enlace.

### Qué es afirmación de una sola fuente

- **Casi todo.** Los 10.000+, el factor 10×, los 2.000 de Cloudflare, el barrido de 1.000 proyectos
  y los 6.202/23.019 son **cifras autoinformadas por Anthropic** sobre su propio producto,
  reproducidas por un medio. Engadget informa; no audita. *"Anthropic says"* está en el propio
  titular, y conviene conservar esa forma al citar.
- **Excepción parcial: los 271 de Mozilla.** Es la única cifra que **un tercero reportó por su
  cuenta** (Mozilla, antes de este artículo, con nota previa de Engadget enlazada). Es la más sólida
  del conjunto — y aun así viene de la organización que se beneficia de mostrar que corrigió mucho.
- **Microsoft es inferencia, no confirmación.** El artículo dice que el crecimiento de los parches
  se debe *"apparently"* a Mythos. Microsoft, en el blog citado, no lo afirma en esos términos según
  lo que reproduce Engadget. **Citar "Microsoft confirmó que sus parches crecen por Mythos" sería
  incorrecto.**
- **macOS es doblemente débil.** Es una firma de investigación no nombrada, y Engadget aclara que
  **Anthropic no lo incluyó en el informe**. No debería aparecer en una diapositiva como hecho.

### Qué no tiene respaldo técnico publicado

- **Ningún CVE, ningún identificador, ninguna metodología.** No se explica cómo se contaron las
  vulnerabilidades, con qué escala se clasificó "alta o crítica", cuántas fueron confirmadas por los
  mantenedores, ni cuántas resultaron **falsos positivos**. Un conteo de "vulnerabilidades
  encontradas" sin tasa de confirmación no es comparable con un conteo de CVE publicados.
- **"Más de 10.000" no es un número, es un piso.** Y los 6.202 sobre 23.019 del barrido open source
  no aclaran si esas 23.019 están **incluidas** en las 10.000+ de los socios o si son un conjunto
  aparte — de hecho la aritmética sugiere que son conjuntos distintos (los socios son empresas; el
  barrido es de Anthropic sobre proyectos abiertos), pero **el artículo no lo dice**. No sumar las
  cifras entre sí.
- **Ventana temporal inconsistente.** Las 10.000+ corresponden a "un mes" desde el lanzamiento; el
  barrido open source es "over the past few months". No son la misma ventana y no deben presentarse
  como parte del mismo conteo.
- **Sin denominador.** No se dice sobre cuánta base de código, cuántas horas de cómputo ni cuántos
  intentos. Sin eso, el "factor 10×" no es evaluable.

### Coherencia con las otras dos fuentes del corpus

- La fecha de lanzamiento de Glasswing (**abril de 2026**) coincide con
  `medium-mythos-bugs-seguridad.web.md` (7 de abril) y con el hilo de
  `freebsd-forums-mythos-zero-days.web.md` (abierto el 8 de abril). **Ese punto sí tiene respaldo
  cruzado.**
- El argumento de la no liberación es **consistente pero no idéntico** entre fuentes: Medium lo cita
  como *"the model is too capable to release safely"*; Engadget lo formula como que ninguna empresa
  tiene aún salvaguardas suficientes. Es el mismo razonamiento con distinto énfasis (capacidad del
  modelo vs. estado de las defensas de la industria).
- **Los recuentos de socios no cierran entre sí.** Medium dice 12 empresas socias + 40
  organizaciones de infraestructura crítica; el hilo de FreeBSD cita a Anthropic con 11
  organizaciones nombradas + Anthropic; Engadget nombra 7 "además de los ya mencionados" (AWS,
  Apple, CrowdStrike, Google, JPMorganChase, NVIDIA, Palo Alto Networks) y suma Cloudflare, Mozilla
  y Microsoft en el cuerpo. Las listas se solapan pero **no son la misma lista** — Broadcom, Cisco y
  la Linux Foundation aparecen en la cita de Anthropic y no en Engadget; Cloudflare y Mozilla
  aparecen en Engadget y no en la cita de Anthropic. Si la clase muestra "los socios", conviene
  mostrar una lista con su fuente al pie, no un número redondo.
- **Esta fuente no menciona FreeBSD, NFS ni OpenBSD.** El caso técnico de los BSD no sale de acá.

### Otras notas

- El párrafo financiero (rentabilidad, WSJ) es un aparte editorial sin relación con las cifras de
  seguridad. Si se cita, hay que citarlo como reporte del WSJ, no de Anthropic ni de Engadget.
- La nota tiene **seis enlaces internos a otras notas de Engadget**, lo que indica una cobertura
  sostenida del tema; ninguna de esas notas está capturada en el corpus.

## Images / diagrams

3 imágenes copiadas a la carpeta companion desde
`research/web/engadget-mythos-glasswing-10000/assets/`.

**Imagen de contenido (1) — pendiente de transcripción.**

- `engadget-mythos-glasswing-10000.web/images/intro-1779540303.jpg`
  - Provenance: foto de cabecera del artículo, ubicada inmediatamente después de la línea de firma
    ("By Mariella Moon, May 23, 2026 8:48 am EST") y antes del primer párrafo. Texto alt = "A man
    speaking." Crédito: Michael M. Santiago / Getty Images. Origen:
    `https://www.engadget.com/img/gallery/anthropic-says-mythos-has-already-found-more-than-10000-vulnerabilities/intro-1779540303.jpg`.
    72.780 bytes. Es una foto de prensa, no una figura de datos: no contiene cifras del artículo.
  - <!-- pending: process_images -->

**Cromo del sitio (2) — sin valor expositivo, no requieren transcripción.**

- `engadget-mythos-glasswing-10000.web/images/engadget-logo-RGB-default.svg`
  - Provenance: cabecera del sitio; alt = "Engadget". 1.758 bytes.
  - Depiction: logotipo de Engadget. · Why it matters: no aplica.
- `engadget-mythos-glasswing-10000.web/images/engadget-icon-RGB-default.svg`
  - Provenance: cabecera del sitio; alt = "Engadget". 408 bytes.
  - Depiction: isotipo de Engadget. · Why it matters: no aplica.

## Raw / preserved excerpts

Cuerpo completo del artículo, preservado verbatim desde `page.md` (retirado el cromo de navegación
del encabezado y el corte "Recommended" del final; los enlaces del original se conservan entre
corchetes):

> # Anthropic says Mythos has already found more than 10,000 vulnerabilities
>
> The company has published an update about Project Glasswing, a month after its launch.
>
> By Mariella Moon · May 23, 2026 8:48 am EST
> *[foto] "A man speaking." — Michael M. Santiago/Getty Images*
>
> Anthropic has published [anthropic.com/research/glasswing-initial-update] an initial report for
> Project Glasswing [engadget.com/ai/anthropic-launches-project-glasswing-an-effort-to-prevent-ai-cyberattacks-with-ai-214939773.html],
> the cybersecurity initiative it launched in April that aims to prevent AI cyberattacks with, well,
> AI. The initiative is powered by Claude Mythos Preview, the company's unreleased model, which
> Anthropic says has already helped its partners find more than ten thousand vulnerabilities overall
> just a month after Glasswing's launch. In addition, it says most of its partners have "each found
> hundreds of critical- or high-severity vulnerabilities in their software" using the model.
>
> The company said that its partners' rate of bug-finding has increased by more than a factor of
> ten. Cloudflare found 2,000 bugs, 400 of which are high or critical in severity. Mozilla
> [engadget.com/ai/mozilla-says-it-patched-271-firefox-vulnerabilities-thanks-to-anthropics-claude-mythos-224330023.html]
> previously reported that it found and fixed 271 vulnerabilities in Firefox, 10 times more what it
> found in an older version of the browser using another Claude model.
>
> Microsoft's recent announcement [microsoft.com/en-us/msrc/blog/2026/05/a-note-on-patch-tuesday]
> that its patch releases will "continue trending larger for some time" is apparently because of the
> bugs it found through Mythos Preview. Anthropic also used Mythos Preview to scan 1,000 open-source
> projects over the past few months and found 6,202 high- and critical-severity vulnerabilities out
> of 23,019. While the company didn't include it in the report, a security research firm recently
> claimed that it found a way to breach macOS
> [engadget.com/2173543/security-researchers-anthropic-mythos-macos-exploit/], an operating system
> known for having tight security, with help from Mythos' bug-finding capabilities.
>
> The company explained in its report that it hasn't released Mythos Preview to the public yet,
> because no company (including itself) has developed safeguards strong enough to prevent models
> like it from being misused. It intends to release "Mythos-class models" in the future, though,
> when those safeguards become available. For now, it's planning to work with partners like the US
> and other governments to expand the availability of Project Glasswing. That indicates that the
> company may be on its way to repairing its relationship with the US government
> [engadget.com/ai/anthropic-sues-us-government-over-supply-chain-risk-designation-152838128.html].
> The company is already working with several partners at the moment, including Amazon Web Services,
> Apple, CrowdStrike, Google, JPMorganChase, NVIDIA and Palo Alto Networks, in addition to the
> others we've already mentioned.
>
> Anthropic is reportedly about to be profitable for the first time since it was founded in 2021.
> According to a recent report [engadget.com/2178340/anthropic-first-profitable-quarter/] by the
> *The Wall Street Journal*, it's on track to post a revenue of $10.9 billion with an operating
> profit of $559 million for the quarter ending in June. The company doesn't expect to remain
> profitable in the quarters that will follow, however, as it intends to invest more money into
> computing resources and other expenses.

`metadata.yaml` completo:

> ```yaml
> url: "https://www.engadget.com/2180028/anthropic-claude-mythos-preview-project-glasswing-update/"
> fetched_at: "2026-08-05T15:48:21Z"
> title: "Anthropic Says Mythos Has Already Found More Than 10,000 Vulnerabilities"
> http_status: 200
> byte_size: 59163
> assets:
>   - { src: "https://www.engadget.com/img/engadget-logo-RGB-default.svg", absolute: "https://www.engadget.com/img/engadget-logo-RGB-default.svg", saved_as: "engadget-logo-RGB-default.svg", alt: "Engadget" }
>   - { src: "https://www.engadget.com/img/engadget-icon-RGB-default.svg", absolute: "https://www.engadget.com/img/engadget-icon-RGB-default.svg", saved_as: "engadget-icon-RGB-default.svg", alt: "Engadget" }
>   - { src: "https://www.engadget.com/img/gallery/anthropic-says-mythos-has-already-found-more-than-10000-vulnerabilities/intro-1779540303.jpg", absolute: "https://www.engadget.com/img/gallery/anthropic-says-mythos-has-already-found-more-than-10000-vulnerabilities/intro-1779540303.jpg", saved_as: "intro-1779540303.jpg", alt: "A man speaking." }
> ```
