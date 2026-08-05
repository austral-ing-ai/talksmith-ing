---
source_file: alibaba-qwen-doc
source_type: web-capture
ingested_at: 2026-08-05
---

# Alibaba Unveils New AI Chip, Flagship Model, and Rebuilt Cloud Stack AI for Agentic Era

## Provenance
- Ubicación original: `research/web/alibaba-qwen-doc/`
- Formato: captura web (`original.html` 79.155 bytes + `page.md` 50.344 bytes + `metadata.yaml` 84.052 bytes)
- URL: https://www.alibabagroup.com/en-US/document-1994119844504535040
- Autor / fuente: **Alibaba Group** (comunicado corporativo oficial)
- Fecha del original: **20 de mayo de 2026**
- Capturado el: 2026-08-05T12:19:54Z · HTTP 200
- Contexto del anuncio: **Alibaba Cloud Summit**, Hangzhou
- `metadata.yaml` declara `assets` con una sola entrada, un logo embebido como data-URI base64
  (no descargable como archivo). No hay carpeta `assets/`.
- **Nota de extracción:** el `page.md` pesa 50 KB pero contiene solo **26 líneas no vacías**. El
  grueso del archivo es un único logo PNG embebido como base64 al final. El texto del comunicado está
  completo y limpio.

## Key claims

Alibaba anuncia simultáneamente en **tres capas del stack** — silicio, modelo y nube — presentándolo
como "su empuje de IA más agresivo hasta ahora".

### 1. Modelo: Qwen 3.7-Max

- **Qwen3.7-Max** es el nuevo modelo de lenguaje insignia, *"built for agentic workloads"*, diseñado
  para operaciones sostenidas y multi-paso en lugar de respuestas de un solo turno.
- **La capacidad definitoria que Alibaba reivindica es la resistencia (endurance).** El benchmark
  interno presentado en la cumbre:
  - Se le dio un *brief* de tarea y se lo puso sobre un chip **Zhenwu M890 que nunca había visto
    durante el entrenamiento**.
  - Trabajó **sin intervención humana durante 35 horas consecutivas**.
  - Ejecutó **más de 1.000 llamadas a herramientas**.
  - Entregó un **kernel de cómputo de IA de grado producción** que **superó por diez veces (tenfold)
    la versión oficial del fabricante del chip**.
- Alibaba lee ese resultado como la definición de la era agéntica: *"a model that completes complex
  engineering tasks on its own"*.
- Otras capacidades declaradas: proyectos de software multi-archivo, orquestación de flujos de
  trabajo de oficina multi-agente.
- **Optimizado para harnesses de agente de terceros**: OpenClaw, Hermes Agent, **Claude Code**,
  Qwen Paw y Qoder.

### 2. Nube: reconstruida para agentes

- **Panjiu AL128 Supernode Server**: sistema a escala de rack con **128 aceleradores de IA en una sola
  unidad** y **ancho de banda interno de petabyte por segundo (PB/s)**.
- Diseñado específicamente para los patrones de concurrencia que generan los agentes: *"unpredictable,
  high-frequency bursts of inference requests that overwhelm conventional compute clusters"*.
- Disponible a través de **Bailian** (llamada **Model Studio** fuera de China), la plataforma de
  servicio de modelos de Alibaba.
- La plataforma introduce **Agentic RL**: mecanismo de aprendizaje por refuerzo que refina los
  modelos de forma continua **según los resultados reales de las tareas de los agentes**.
- Incluye **guardrails de gobernanza de seguridad** integrados para mantener a los agentes autónomos
  dentro de límites definidos.

### 3. Silicio: T-Head

- **T-Head**, la subsidiaria de diseño de chips de Alibaba, debutó formalmente el **Zhenwu M890**, su
  procesador de IA más potente hasta la fecha:
  - **3× el rendimiento** de su predecesor, el **Zhenwu 810E**
  - **144 GB de memoria en chip**
  - **800 GB/s de ancho de banda entre chips**
  - **soporte nativo de formatos de precisión de FP32 hasta FP4**, lo que permite que un mismo
    dispositivo maneje entrenamiento de alta exactitud e inferencia rápida y barata
- **ICN Switch 1.0**, chip de red: hasta **25,6 Tbps de ancho de banda agregado**, comunicación sin
  congestión en clusters de **64 aceleradores**.
- **T-Head SAIL™**: stack de software para extraer el máximo rendimiento del hardware propietario.
- **Escala de despliegue declarada: más de 560.000 chips Zhenwu enviados a la fecha**, con más de
  **400 clientes externos en 20 industrias**, incluidas automotrices y servicios financieros líderes.

### 4. Reposicionamiento estratégico y cifras financieras

- El CEO **Eddie Wu** declaró en el último anuncio de resultados que Alibaba espera que el ARR de su
  plataforma de servicios de modelos y aplicaciones **supere los RMB 10.000 millones (≈US$1.400
  millones) en el trimestre de junio**, y proyectó **RMB 30.000 millones (US$4.100 millones) para fin
  de año**.
- Pronóstico: **los ingresos por productos relacionados con IA superarán a las ventas de cómputo en
  nube convencional** como la mayor línea de ingresos de Cloud Intelligence Group **en
  aproximadamente un año**.

## Definitions and terminology

- **Agentic workload**: carga de trabajo en la que el modelo opera de forma sostenida y multi-paso,
  no en turnos de pregunta-respuesta. Es el eje conceptual de todo el anuncio.
- **Endurance / resistencia**: la métrica que Alibaba propone como definitoria — cuánto tiempo puede
  operar un modelo sin intervención humana. 35 horas y 1.000+ llamadas a herramientas es la cifra que
  ofrece.
- **Agentic RL**: aprendizaje por refuerzo cuya señal son los **resultados reales de tareas de
  agentes en producción**, no un dataset fijo.
- **Supernode**: sistema a escala de rack tratado como una unidad de cómputo única (128 aceleradores).
- **Harness de agente**: el armazón de software que corre el bucle del agente. Alibaba nombra cinco y
  declara compatibilidad, incluida la de un competidor directo (Claude Code).
- **FP32 → FP4**: rango de formatos de precisión de punto flotante. FP4 (4 bits) es para inferencia
  barata; FP32 para entrenamiento de alta exactitud. Que un solo chip soporte ambos nativamente es lo
  que Alibaba destaca.
- **Bailian / Model Studio**: la misma plataforma con dos nombres, dentro y fuera de China.

## Evidence and examples

Toda la evidencia es **auto-reportada por Alibaba** y proviene de un comunicado corporativo.

| Afirmación | Cifra | Naturaleza |
|---|---|---|
| Operación autónoma de Qwen 3.7-Max | 35 horas consecutivas, >1.000 tool calls | benchmark **interno** |
| Kernel producido vs. versión oficial del fabricante | 10× mejor | benchmark **interno** |
| Panjiu AL128 | 128 aceleradores/rack, PB/s interno | especificación de producto |
| Zhenwu M890 vs. Zhenwu 810E | 3× rendimiento | comparación **contra su propio predecesor** |
| Zhenwu M890 | 144 GB on-chip, 800 GB/s inter-chip, FP32–FP4 | especificación |
| ICN Switch 1.0 | 25,6 Tbps agregados, clusters de 64 | especificación |
| Chips Zhenwu enviados | >560.000 | dato de despliegue |
| Clientes externos | >400, en 20 industrias | dato de despliegue |
| ARR plataforma de modelos (trim. junio) | >RMB 10.000M (≈US$1.400M) | guidance del CEO |
| ARR proyectado a fin de año | RMB 30.000M (US$4.100M) | proyección |

## Inconsistencies / open questions

- **El benchmark estrella no es verificable y está construido en casa.** Las 35 horas, las 1.000+
  llamadas y el "10× mejor que la versión oficial del fabricante" salen de una prueba **interna**
  presentada en la propia cumbre de Alibaba. No hay metodología publicada, ni línea base descrita, ni
  verificación de terceros. Es la afirmación más impactante del comunicado y la menos sostenida.
- **Hay circularidad en el benchmark.** El modelo de Alibaba escribió un kernel para el chip de
  Alibaba y superó "por diez veces" al kernel oficial del fabricante — que **también es Alibaba**
  (T-Head es su subsidiaria). Que el modelo supere al kernel de referencia de la casa dice tanto sobre
  la calidad del kernel de referencia como sobre la capacidad del modelo. El comunicado no lo comenta.
- **"3× el rendimiento" es contra su propio predecesor**, no contra la competencia. No hay ninguna
  comparación con GPUs de otros fabricantes en toda la página. Para un chip cuyo argumento comercial
  es la soberanía tecnológica, esa ausencia es notable.
- **"Rendimiento" sin unidad.** Ni el 3× ni el 10× declaran qué se mide (FLOPS, throughput, latencia,
  perf/watt).
- **Nada sobre Qwen 3.7-Max como modelo.** No hay parámetros, ventana de contexto, arquitectura,
  precio ni benchmarks estándar. Es un anuncio de capacidad agéntica sin ficha técnica. El enlace
  `https://qwen.ai/blog?id=qwen3.7` **no fue capturado**.
- **Ausencia total de contrapunto.** Comunicado corporativo puro: sin limitaciones, sin casos de
  fracaso, sin voces externas, sin análisis de competencia.
- **Los "guardrails de gobernanza de seguridad" se mencionan y no se describen.** En un anuncio cuyo
  eje es la autonomía de 35 horas sin supervisión humana, es la omisión más relevante.
- **Compatibilidad con Claude Code declarada unilateralmente.** El comunicado lista harnesses de
  terceros —incluido el de un competidor directo— como plataformas para las que el modelo está
  optimizado. No hay confirmación de la otra parte en esta fuente.
- **Cifras financieras en dos monedas con conversión implícita.** RMB 10.000M ≈ US$1.400M y RMB
  30.000M ≈ US$4.100M implican tipos de cambio ligeramente distintos (~7,14 vs. ~7,32). Diferencia
  menor, pero conviene citar la cifra en RMB si la precisión importa.
- **Guidance, no resultados.** Las cifras de ARR son proyecciones del CEO, no ingresos reportados.
- **Título ambiguo.** El `<title>` de la página es *"...Rebuilt Cloud Stack AI for Agentic Era"*, con
  un "AI" que parece un error de edición. Se preserva tal cual.

## Images / diagrams

Ninguna imagen descargable. `metadata.yaml` registra un único asset: el logo de Alibaba embebido en
el HTML como **data-URI base64** (`data:image/png;base64,iVBORw0KGgo...`, alt = "logo"), que por eso
no existe como archivo en `assets/`. Es cromo del sitio y no tiene valor expositivo.

La carpeta companion `alibaba-qwen-doc.web/images/` existe y está vacía.

## Raw / preserved excerpts

Bajada del comunicado, verbatim:

> Alibaba launched its most aggressive AI push yet, unveiling a new flagship large language model, a homegrown AI chip that triples the performance of its predecessor, and a rebuilt cloud platform designed from the ground up for autonomous AI agents. The announcements came at the Alibaba Cloud Summit in Hangzhou and span every layer of the company's technology stack, from silicon to software.

Sección "Qwen 3.7-Max: A Model That Works, Not Just Answers", verbatim:

> [Qwen3.7-Max](https://qwen.ai/blog?id=qwen3.7), Alibaba's latest large language model, is built for agentic workloads. The model is engineered for sustained, multi-step operations rather than single-turn responses.
>
> The model's defining capability is endurance. In an internal benchmark shared at the summit, **Qwen 3.7-Max was given a task brief and placed on a Zhenwu M890 chip it had never encountered in training. Working without human intervention, the model ran for 35 consecutive hours, executed more than 1,000 tool calls, and delivered a production-grade AI computing kernel that outperformed the chip manufacturer's official version by tenfold.**
>
> The result illustrates a shift that Alibaba believes defines the agentic era: a model that completes complex engineering tasks on its own. Qwen3.7-Max also handles multi-file software projects, orchestrates multi-agent office workflows, and is optimized for agent harnesses including OpenClaw, Hermes Agent, Claude Code, Qwen Paw and Qoder.

Sección "A Cloud Rebuilt for Agents", verbatim:

> Alibaba Cloud also launched the **Panjiu AL128 Supernode Server**, a rack-scale system that packs 128 AI accelerators into a single unit and delivers petabyte-per second (PB/s) internal bandwidth. The configuration is designed specifically for the concurrency patterns that agents generate: unpredictable, high-frequency bursts of inference requests that overwhelm conventional compute clusters.
>
> The server is now available through Alibaba's model service platform, Bailian (also known as Model Studio outside China). The platform has introduced Agentic RL, a reinforcement learning mechanism that refines models continuously based on actual agent task outcomes. It also features built-in safety governance guardrails that keep autonomous agents operating within defined boundaries.

Sección "Homegrown Silicon: T-Head Steps Up", verbatim:

> T-Head, Alibaba's chip design subsidiary, formally debuted the **Zhenwu M890**, its most powerful AI processor to date. The chip delivers three times the performance of its predecessor, Zhenwu 810E, and carries **144 gigabytes (GB) of on-chip memory alongside 800 GB per second of inter-chip bandwidth.** It **natively supports precision formats from FP32 (32-bit floating-point) down to FP4 (4-bit floating-point),** allowing a single device to handle both high-accuracy model training and the rapid, low-cost inference that agent workloads demand.
>
> T-Head paired the Zhenwu M890 with a new networking chip, **ICN Switch 1.0**, which delivers up to **25.6 terabits per second (Tbps) of aggregate bandwidth** and enables congestion-free communication across clusters of 64 accelerators. The company also launched **T-Head SAIL™,** a software stack designed to extract maximum performance from its proprietary hardware. Together, the chips underpin the Panjiu AL128 server.
>
> T-Head has shipped more than **560,000 Zhenwu chips to date**. More than 400 external customers across 20 industries have deployed them, including leading automakers and financial services companies.

Cierre financiero, verbatim:

> The announcements signal a strategic repositioning. During its latest earnings announcement, Alibaba CEO Eddie Wu shared that the company expects its model and application services platform annual recurring revenue (ARR) to surpass RMB 10 billion (approximately US$1.4 billion) in the June quarter and projected that figure to reach RMB 30 billion (US$4.1 billion) by year-end. He forecasted that AI-related product revenue will surpass conventional cloud compute sales as Cloud Intelligence Group's largest revenue line in approximately one year.
