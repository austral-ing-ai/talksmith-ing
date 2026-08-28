---
source_file: few-shot-learners-brown
source_type: web-capture
ingested_at: 2026-08-14
---

# Language Models are Few-Shot Learners (Brown et al., 2020) — el paper de GPT-3

## Provenance
- Original location: `research/web/few-shot-learners-brown/`
- Format: web capture (HTML + `page.md` extraído), página de abstract de arXiv
- URL: https://arxiv.org/abs/2005.14165
- `fetched_at`: 2026-08-14T16:56:07Z
- `http_status`: 200
- Título capturado: `[2005.14165] Language Models are Few-Shot Learners`
- Autores (31, verbatim en el orden de la captura): Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei
- Fecha del original: enviado el 28 de mayo de 2020 (v1); última revisión 22 de julio de 2020 (v4, la capturada)
- arXiv ID: arXiv:2005.14165 [cs.CL] — DOI 10.48550/arXiv.2005.14165
- Materias: Computation and Language (cs.CL)
- Extensión declarada en `Comments`: "40+32 pages"
- Venue: **no declarado en la captura**. (El paper se presentó en NeurIPS 2020, pero ese dato no está en esta fuente.)
- Licencia: **no declarada** en la captura — esta ficha no trae badge de Creative Commons, a diferencia de los papers de CoT, self-consistency, ToT y ReAct. Reproducir figuras del PDF de GPT-3 no está cubierto por una licencia abierta explícita según lo que muestra la captura.

## Key claims

- El trabajo previo había mostrado ganancias sustanciales en muchas tareas de NLP mediante preentrenamiento sobre un corpus grande seguido de fine-tuning sobre una tarea específica.
- Ese método, aunque de arquitectura agnóstica a la tarea, **sigue requiriendo datasets de fine-tuning específicos de miles o decenas de miles de ejemplos**. Este es el problema que el paper ataca.
- Por contraste, **los humanos generalmente pueden hacer una tarea lingüística nueva a partir de solo unos pocos ejemplos o de instrucciones simples** — algo que los sistemas de NLP de entonces todavía no lograban. Esta frase del abstract es la justificación conceptual del few-shot y sirve como puente didáctico natural en la clase.
- Escalar los modelos de lenguaje mejora enormemente el rendimiento *few-shot* agnóstico a la tarea, a veces incluso alcanzando competitividad con enfoques de fine-tuning que eran estado del arte.
- Entrenan **GPT-3, un modelo de lenguaje autoregresivo de 175 mil millones de parámetros, 10× más grande que cualquier modelo de lenguaje no disperso previo**, y prueban su rendimiento en el escenario few-shot.
- Punto operativo central: **en todas las tareas, GPT-3 se aplica sin ninguna actualización de gradiente ni fine-tuning**. Las tareas y las demostraciones few-shot se especifican **puramente por interacción de texto con el modelo**. Esta frase es la definición práctica de in-context learning y probablemente la cita más útil de todo el registro para una clase de prompting.
- GPT-3 rinde fuerte en muchos datasets de NLP: traducción, question-answering, tareas cloze, además de tareas que requieren razonamiento sobre la marcha o adaptación de dominio — desordenar palabras, usar una palabra nueva en una oración, o hacer aritmética de 3 dígitos.
- Los autores **también identifican límites**: datasets donde el aprendizaje few-shot de GPT-3 todavía tiene dificultades, y datasets donde GPT-3 enfrenta problemas metodológicos relacionados con haber sido entrenado sobre corpus web grandes (es decir, contaminación de datos).
- GPT-3 puede generar muestras de artículos de noticias que a evaluadores humanos les cuesta distinguir de artículos escritos por humanos. Los autores discuten los impactos sociales más amplios de ese hallazgo y de GPT-3 en general.

## Definitions and terminology

Esta es la fuente primaria de la clase para el vocabulario de zero/one/few-shot. Ojo con un matiz importante:

- **Few-shot learning** — en el uso de este paper: dar al modelo unas pocas demostraciones de la tarea **dentro del prompt**, sin actualizar pesos. El abstract lo caracteriza así: "with tasks and few-shot demonstrations specified purely via text interaction with the model".
- **In-context learning** — **atención: el abstract no usa la expresión "in-context learning"**. El término aparece en el cuerpo del paper y se volvió estándar después. Lo que el abstract describe es exactamente ese fenómeno ("without any gradient updates or fine-tuning... purely via text interaction"), pero si la clase atribuye el término al abstract, la atribución es imprecisa. Vale citarlo como "lo que después se llamó in-context learning".
- **Zero-shot / one-shot** — **el abstract tampoco los menciona**. La taxonomía zero-shot / one-shot / few-shot es del cuerpo del paper (donde se define y se compara sistemáticamente), no de la ficha capturada. Si la slide presenta los tres términos como "de Brown et al. 2020", es correcto respecto del paper pero **no está respaldado por esta captura**.
- **Task-agnostic (agnóstico a la tarea)** — el modelo no se modifica por tarea. El abstract contrasta "task-agnostic in architecture" (lo que ya lograba el paradigma previo) con "task-agnostic, few-shot performance" (lo que aporta GPT-3).
- **Gradient updates / fine-tuning** — lo que GPT-3 explícitamente **no** hace en estos experimentos. Es la línea divisoria entre prompting y entrenamiento.
- **Autoregressive language model** — la caracterización de GPT-3 en el abstract.
- **Non-sparse model (modelo no disperso)** — la calificación exacta del récord de tamaño: "10x more than any previous non-sparse language model". La precisión importa: había modelos dispersos (mixture-of-experts) más grandes en conteo de parámetros.
- **Cloze tasks** — tareas de completar huecos; el abstract las nombra sin definirlas.

## Evidence and examples

Lo cuantitativo que da el abstract:

| Dato | Valor |
|---|---|
| Parámetros de GPT-3 | **175 mil millones (175B)** |
| Factor respecto del mayor modelo no disperso previo | **10×** |
| Actualizaciones de gradiente en la evaluación | **cero** |
| Extensión del paper (`Comments`) | 40 + 32 páginas |

Tipos de tarea que el abstract nombra como éxitos:
- traducción
- question-answering
- tareas cloze
- razonamiento sobre la marcha / adaptación de dominio: desordenar palabras (*unscrambling words*), usar una palabra nueva en una oración, aritmética de 3 dígitos
- generación de artículos de noticias indistinguibles de los humanos para evaluadores

Ejemplos citables para la clase: "usar una palabra nueva en una oración" y "aritmética de 3 dígitos" son demostraciones concretas y memorables de que el modelo aprende la tarea desde el prompt.

**El abstract no da un solo porcentaje.** Ni un número de accuracy, ni un benchmark con cifra. Toda afirmación numérica sobre rendimiento de GPT-3 que la clase quiera hacer tiene que venir de otro lado.

## Inconsistencies / open questions

- **La captura trae solo el abstract, no el cuerpo del paper.** Lo que la clase necesitaría y no está acá:
  - **La taxonomía formal zero-shot / one-shot / few-shot** con su figura comparativa (la Figura 2.1 del paper). Es justamente el material que una clase de prompting querría proyectar, y no está en la captura.
  - El **término "in-context learning"** y su definición.
  - **Todos los números de rendimiento** por benchmark y por tamaño de modelo.
  - Las **curvas de escala** (rendimiento vs. parámetros vs. cantidad de shots), que son el argumento visual del paper.
  - La **composición del corpus de entrenamiento** y el análisis de contaminación que el abstract insinúa ("methodological issues related to training on large web corpora").
  - **Cuáles** son los datasets donde el few-shot de GPT-3 falla. El abstract admite que existen pero no los nombra. Si la clase quiere ser honesta sobre los límites, ese detalle no está acá.
  - La sección de impactos sociales (sesgo, desinformación, uso indebido) que el abstract anuncia.
- Riesgo de anacronismo: GPT-3 es de 2020 y el escenario de prompting cambió mucho. Las afirmaciones del abstract sobre "estado del arte" describen 2020, no el presente. Si la clase presenta el paper como fundacional (que lo es), conviene marcar la fecha.
- La ausencia de badge de licencia CC en la captura es una diferencia real con los otros papers de arXiv del corpus. Vale tenerlo en cuenta si se piensa reproducir figuras.

## Images / diagrams

La captura no trae ninguna figura del paper. Solo cromo del sitio arXiv. Notar que esta ficha, a diferencia de las de CoT/self-consistency/ToT/ReAct, **no incluye badge de licencia** — son tres imágenes, no cuatro.



## Raw / preserved excerpts

**Abstract completo, verbatim (inglés):**

> Abstract:Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches. Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model. GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic. At the same time, we also identify some datasets where GPT-3's few-shot learning still struggles, as well as some datasets where GPT-3 faces methodological issues related to training on large web corpora. Finally, we find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans. We discuss broader societal impacts of this finding and of GPT-3 in general.

**Ficha bibliográfica, verbatim:**

> **arXiv:2005.14165** (cs)  [Submitted on 28 May 2020 ([v1](https://arxiv.org/abs/2005.14165v1)), last revised 22 Jul 2020 (this version, v4)]

> Comments: 40+32 pages Subjects: Computation and Language (cs.CL) Cite as: arXiv:2005.14165 [cs.CL] (or arXiv:2005.14165v4 [cs.CL] for this version) https://doi.org/10.48550/arXiv.2005.14165

**Lista de autores, verbatim y completa** (31 autores — relevante porque el deck probablemente cita "Brown et al."):

> Authors: Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei

**Enlaces al texto completo:**

> - View PDF: https://arxiv.org/pdf/2005.14165
> - HTML (experimental): https://arxiv.org/html/2005.14165v4
> - TeX Source: https://arxiv.org/src/2005.14165
