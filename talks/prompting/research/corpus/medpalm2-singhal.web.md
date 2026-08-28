---
source_file: medpalm2-singhal
source_type: web-capture
ingested_at: 2026-08-14
---

# Towards Expert-Level Medical Question Answering with Large Language Models (Singhal et al., 2023) — Med-PaLM 2

## Provenance
- Original location: `research/web/medpalm2-singhal/`
- Format: web capture (HTML + `page.md` extraído), página de abstract de arXiv
- URL: https://arxiv.org/abs/2305.09617
- `fetched_at`: 2026-08-14T16:56:07Z
- `http_status`: 200
- Título capturado: `[2305.09617] Towards Expert-Level Medical Question Answering with Large Language Models`
- Autores (31, verbatim): Karan Singhal, Tao Tu, Juraj Gottweis, Rory Sayres, Ellery Wulczyn, Le Hou, Kevin Clark, Stephen Pfohl, Heather Cole-Lewis, Darlene Neal, Mike Schaekermann, Amy Wang, Mohamed Amin, Sami Lachgar, Philip Mansfield, Sushant Prakash, Bradley Green, Ewa Dominowska, Blaise Aguera y Arcas, Nenad Tomasev, Yun Liu, Renee Wong, Christopher Semturs, S. Sara Mahdavi, Joelle Barral, Dale Webster, Greg S. Corrado, Yossi Matias, Shekoofeh Azizi, Alan Karthikesalingam, Vivek Natarajan
- Fecha del original: enviado el 16 de mayo de 2023. **Versión única (v1)** — no hay revisiones posteriores en la captura.
- arXiv ID: arXiv:2305.09617 [cs.CL] — DOI 10.48550/arXiv.2305.09617
- Materias: Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
- Venue: **no declarado**. No hay campo `Comments` en esta ficha. (El trabajo derivó luego en una publicación en Nature Medicine, pero eso no está en la captura.)
- Licencia: CC BY 4.0

Este es el paper más directamente relevante para el cruce prompting × biomedicina de todo el corpus web: es el único donde una estrategia de prompting se evalúa sobre preguntas médicas con jueces clínicos.

## Key claims

- Los sistemas de IA recientes alcanzaron hitos en "grandes desafíos" que van desde el Go hasta el plegamiento de proteínas. La capacidad de **recuperar conocimiento médico, razonar sobre él y responder preguntas médicas de manera comparable a la de los médicos** se viene considerando desde hace mucho uno de esos grandes desafíos.
- Los LLM catalizaron un progreso significativo en question-answering médico. **Med-PaLM fue el primer modelo en superar un puntaje "de aprobación" en preguntas estilo USMLE** (examen de licencia médica de EE. UU.), con **67,2 % en el dataset MedQA**.
- Pero ese trabajo previo, y otros, sugerían un margen de mejora significativo, especialmente **cuando las respuestas de los modelos se comparaban con las de clínicos**.
- Presentan **Med-PaLM 2**, que cierra esas brechas combinando tres cosas — y la enumeración importa para una clase de prompting, porque **el prompting es uno de los tres ingredientes, no el único**:
  1. mejoras en el LLM base (PaLM 2),
  2. fine-tuning de dominio médico,
  3. **estrategias de prompting, incluyendo un enfoque novedoso de *ensemble refinement***.
- Med-PaLM 2 alcanzó **hasta 86,5 % en MedQA**, mejorando sobre Med-PaLM en más de 19 puntos y estableciendo un nuevo estado del arte.
- También observaron rendimiento que se aproxima o supera el estado del arte en MedMCQA, PubMedQA y los temas clínicos de MMLU.
- Hicieron evaluaciones humanas detalladas sobre preguntas de formato largo, a lo largo de múltiples ejes relevantes para aplicaciones clínicas.
- **Resultado más fuerte y más delicado**: en una comparación pareada por ranking de **1066 preguntas médicas de consumidores, los médicos prefirieron las respuestas de Med-PaLM 2 sobre las producidas por médicos en ocho de nueve ejes** relativos a utilidad clínica (p < 0,001).
- También observaron mejoras significativas respecto de Med-PaLM en **todos** los ejes de evaluación (p < 0,001) sobre datasets recién introducidos de **240 preguntas "adversarias" de formato largo**, diseñadas para sondear las limitaciones de los LLM.
- **Cierre cauteloso del propio abstract**: "While further studies are necessary to validate the efficacy of these models in real-world settings, these results highlight rapid progress towards physician-level performance in medical question answering". Los autores mismos acotan el alcance. Si la clase cita el 86,5 % o el "8 de 9 ejes", esta salvedad debería ir en la misma slide.

## Definitions and terminology

- **Ensemble refinement (refinamiento por ensamble)** — nombrado en el abstract como "a novel ensemble refinement approach", parte de las "prompting strategies" del modelo. **El abstract no lo define**: no dice cómo funciona. Es un vacío importante para una clase de prompting, porque es precisamente la contribución de prompting del paper. Conceptualmente emparenta con self-consistency (`self-consistency-wang.web.md`) — generar múltiples salidas y agregarlas — pero **esa conexión es inferencia, no está en la captura**.
- **Prompting strategies** — el abstract las lista como uno de los tres componentes de la mejora, junto con el modelo base y el fine-tuning. Vale para la clase: el prompting aporta, pero acá no aporta solo.
- **MedQA** — dataset de preguntas estilo USMLE. Es la métrica principal citada.
- **USMLE** — United States Medical Licensing Examination. El abstract habla de "USMLE style questions", no del examen real.
- **Passing score (puntaje de aprobación)** — el abstract lo pone entre comillas ("passing"), señalando que es una analogía y no una acreditación formal.
- **Long-form questions (preguntas de formato largo)** — preguntas que se responden en prosa, no de opción múltiple. Es donde se hizo la evaluación humana.
- **Adversarial questions (preguntas adversarias)** — 240 preguntas diseñadas específicamente para "probe LLM limitations".
- **Pairwise comparative ranking** — la metodología de la evaluación humana: se comparan de a pares respuestas del modelo y de médicos.
- Otros datasets nombrados: **MedMCQA**, **PubMedQA**, **MMLU clinical topics**.

## Evidence and examples

Este abstract es, por lejos, el más rico en números del corpus web. Todo esto es citable:

| Dato | Valor |
|---|---|
| Med-PaLM (v1) en MedQA | **67,2 %** — primer modelo en superar el umbral de "aprobación" |
| Med-PaLM 2 en MedQA | **hasta 86,5 %** — nuevo estado del arte |
| Mejora de Med-PaLM 2 sobre Med-PaLM | **más de 19 puntos** |
| Preguntas médicas de consumidores en el ranking pareado | **1066** |
| Ejes de utilidad clínica donde los médicos prefirieron a Med-PaLM 2 | **8 de 9** (p < 0,001) |
| Preguntas adversarias de formato largo | **240** |
| Mejora sobre Med-PaLM en los ejes adversarios | significativa en **todos** los ejes (p < 0,001) |
| Otros datasets con rendimiento cercano o superior al SOTA | MedMCQA, PubMedQA, MMLU clinical topics |

Advertencia de lectura sobre el 86,5 %: el abstract dice **"scored up to 86.5%"**. El "up to" no es decorativo — sugiere que es el mejor resultado entre configuraciones, no un número único. Citarlo como "Med-PaLM 2 obtiene 86,5 % en MedQA" a secas pierde ese matiz.

Advertencia de lectura sobre el "8 de 9 ejes": las 1066 preguntas son **de consumidores** ("consumer medical questions"), no preguntas clínicas entre profesionales. Y la comparación es contra respuestas escritas por médicos **en ese formato**. Es un resultado real y notable, pero no dice "el modelo es mejor médico que un médico".

## Inconsistencies / open questions

- **La captura trae solo el abstract, no el cuerpo del paper.** Lo que la clase necesitaría y no está acá:
  - **Cómo funciona el ensemble refinement.** Es el aporte de prompting del paper y el abstract solo lo nombra. Para una clase de prompting, esta es la ausencia más costosa de todo el corpus: si una slide quiere explicar la técnica, el material no está en la captura y hay que ir al PDF.
  - **Cuáles son los nueve ejes** de utilidad clínica. El abstract dice "eight of nine axes" sin enumerarlos. Sin saber cuáles son, el "8 de 9" es difícil de interpretar honestamente.
  - **Cuál es el eje donde los médicos NO prefirieron a Med-PaLM 2.** El abstract lo omite, y es justamente el dato más interesante para una discusión crítica en el aula.
  - Las **configuraciones detrás del "up to 86.5%"** — cuántas muestras, qué prompting, qué variante del modelo.
  - Los números de MedMCQA, PubMedQA y MMLU (el abstract dice "approaching or exceeding" sin cifras).
  - La descomposición del aporte de cada uno de los tres ingredientes (modelo base / fine-tuning / prompting). **Sin esa ablación no se puede afirmar cuánto del salto se debe al prompting.** Si el deck usa Med-PaLM 2 como evidencia de que "el prompting mejora el desempeño clínico", esa atribución no está sostenida por el abstract.
  - Detalles de las 240 preguntas adversarias y de la metodología de evaluación humana (quiénes eran los médicos, cómo se controló el sesgo).
- **Salvedad de los propios autores**, que conviene no perder: "further studies are necessary to validate the efficacy of these models in real-world settings". El paper mide question-answering, no atención clínica.
- Med-PaLM 2 es un modelo **cerrado, de Google**, no accesible para los alumnos. Si la clase lo presenta junto a herramientas que se pueden usar en el práctico, vale marcar la diferencia.
- Fecha: mayo de 2023. En el escenario actual de modelos, estos números están desactualizados como estado del arte, aunque el diseño experimental sigue siendo válido como referencia metodológica.
- Nota de coherencia con el deck: la guía de la OMS sobre grandes modelos multimodales (`iris.who.int/handle/10665/375579`) sería el contrapeso ético natural de esta slide, pero **no se pudo capturar** (HTTP 403). Ver el reporte del librarian.

## Images / diagrams

La captura no trae ninguna figura del paper. Solo cromo del sitio arXiv.



## Raw / preserved excerpts

**Abstract completo, verbatim (inglés), con los saltos de párrafo tal como aparecen en la captura:**

> Abstract:Recent artificial intelligence (AI) systems have reached milestones in "grand challenges" ranging from Go to protein-folding. The capability to retrieve medical knowledge, reason over it, and answer medical questions comparably to physicians has long been viewed as one such grand challenge.
>
> Large language models (LLMs) have catalyzed significant progress in medical question answering; Med-PaLM was the first model to exceed a "passing" score in US Medical Licensing Examination (USMLE) style questions with a score of 67.2% on the MedQA dataset. However, this and other prior work suggested significant room for improvement, especially when models' answers were compared to clinicians' answers. Here we present Med-PaLM 2, which bridges these gaps by leveraging a combination of base LLM improvements (PaLM 2), medical domain finetuning, and prompting strategies including a novel ensemble refinement approach.
>
> Med-PaLM 2 scored up to 86.5% on the MedQA dataset, improving upon Med-PaLM by over 19% and setting a new state-of-the-art. We also observed performance approaching or exceeding state-of-the-art across MedMCQA, PubMedQA, and MMLU clinical topics datasets.
>
> We performed detailed human evaluations on long-form questions along multiple axes relevant to clinical applications. In pairwise comparative ranking of 1066 consumer medical questions, physicians preferred Med-PaLM 2 answers to those produced by physicians on eight of nine axes pertaining to clinical utility (p < 0.001). We also observed significant improvements compared to Med-PaLM on every evaluation axis (p < 0.001) on newly introduced datasets of 240 long-form "adversarial" questions to probe LLM limitations.
>
> While further studies are necessary to validate the efficacy of these models in real-world settings, these results highlight rapid progress towards physician-level performance in medical question answering.

**Ficha bibliográfica, verbatim:**

> **arXiv:2305.09617** (cs)  [Submitted on 16 May 2023]

> Subjects: Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Machine Learning (cs.LG) Cite as: arXiv:2305.09617 [cs.CL] (or arXiv:2305.09617v1 [cs.CL] for this version) https://doi.org/10.48550/arXiv.2305.09617

**Lista de autores, verbatim y completa** (31 autores; el deck probablemente cita "Singhal et al."):

> Authors: Karan Singhal, Tao Tu, Juraj Gottweis, Rory Sayres, Ellery Wulczyn, Le Hou, Kevin Clark, Stephen Pfohl, Heather Cole-Lewis, Darlene Neal, Mike Schaekermann, Amy Wang, Mohamed Amin, Sami Lachgar, Philip Mansfield, Sushant Prakash, Bradley Green, Ewa Dominowska, Blaise Aguera y Arcas, Nenad Tomasev, Yun Liu, Renee Wong, Christopher Semturs, S. Sara Mahdavi, Joelle Barral, Dale Webster, Greg S. Corrado, Yossi Matias, Shekoofeh Azizi, Alan Karthikesalingam, Vivek Natarajan

**Enlaces al texto completo:**

> - View PDF: https://arxiv.org/pdf/2305.09617
> - HTML (experimental): https://arxiv.org/html/2305.09617v1
> - TeX Source: https://arxiv.org/src/2305.09617
