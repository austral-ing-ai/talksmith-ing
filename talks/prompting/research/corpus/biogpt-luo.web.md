---
source_file: biogpt-luo
source_type: web-capture
ingested_at: 2026-08-14
---

# BioGPT: Generative Pre-trained Transformer for Biomedical Text Generation and Mining (Luo et al., 2022)

## Provenance
- Original location: `research/web/biogpt-luo/`
- Format: web capture (HTML + `page.md` extraído), página de abstract de arXiv
- URL: https://arxiv.org/abs/2210.10341
- `fetched_at`: 2026-08-14T16:56:07Z
- `http_status`: 200
- Título capturado: `[2210.10341] BioGPT: Generative Pre-trained Transformer for Biomedical Text Generation and Mining`
- Autores: Renqian Luo, Liai Sun, Yingce Xia, Tao Qin, Sheng Zhang, Hoifung Poon, Tie-Yan Liu (Microsoft Research)
- Fecha del original: enviado el 19 de octubre de 2022 (v1); última revisión 3 de abril de 2023 (v3, la capturada)
- arXiv ID: arXiv:2210.10341 [cs.CL] — DOI 10.48550/arXiv.2210.10341
- Materias: Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
- **Venue declarado en la captura, con referencia de journal completa**: *Briefings in Bioinformatics*, 2022, bbac409. DOI relacionado: https://doi.org/10.1093/bib/bbac409. Es la única fuente del corpus web con `Journal reference` explícita — o sea, la cita bibliográfica formal está totalmente respaldada.
- Código: https://github.com/microsoft/BioGPT
- Licencia: **no declarada** en la captura (no hay badge de Creative Commons en esta ficha).

## Key claims

- Los modelos de lenguaje preentrenados vienen atrayendo atención creciente en el dominio biomédico, inspirados por su gran éxito en el dominio de lenguaje natural general.
- De las dos ramas principales de modelos preentrenados en el dominio general — **BERT (y variantes) y GPT (y variantes)** — la primera fue estudiada extensamente en biomedicina, con casos como **BioBERT y PubMedBERT**.
- Esos modelos tipo BERT lograron gran éxito en tareas biomédicas **discriminativas** de downstream, pero **la falta de capacidad generativa restringe su alcance de aplicación**. Este es el vacío que el paper identifica y ataca.
- Proponen **BioGPT, un modelo de lenguaje Transformer generativo específico de dominio, preentrenado sobre literatura biomédica a gran escala**.
- Evalúan BioGPT en **seis tareas de NLP biomédico** y demuestran que supera a modelos previos en la mayoría de ellas.
- Un estudio de caso sobre generación de texto demuestra además la ventaja de BioGPT para **generar descripciones fluidas de términos biomédicos** a partir de literatura biomédica.

## Definitions and terminology

- **Modelos discriminativos vs. generativos** — la distinción vertebra el paper. BERT y variantes son discriminativos (clasifican, etiquetan, extraen); GPT y variantes generan texto. El abstract dice literalmente que a los primeros "the lack of generation ability constrains their application scope". Es una definición útil y limpia para una clase que necesita explicar por qué los modelos generativos abrieron un espacio nuevo.
- **Domain-specific pre-training (preentrenamiento específico de dominio)** — BioGPT se preentrena "on large scale biomedical literature". Es la alternativa al prompting: en vez de guiar un modelo general con el prompt, se entrena uno sobre el dominio. **Contraste útil para la clase de prompting**: BioGPT representa el camino del entrenamiento; Med-PaLM 2 (`medpalm2-singhal.web.md`) combina ambos.
- **BioBERT / PubMedBERT** — modelos biomédicos previos de la rama BERT, nombrados en el abstract como el estado del arte discriminativo.
- **Relation extraction end-to-end (extracción de relaciones extremo a extremo)** — el tipo de tarea de tres de los benchmarks (BC5CDR, KD-DTI, DDI).
- **F1 score** — la métrica de las tareas de extracción de relaciones.
- **Benchmarks nombrados**: BC5CDR, KD-DTI, DDI (extracción de relaciones), PubMedQA (question answering).

## Evidence and examples

| Tarea | Tipo | Métrica | Valor |
|---|---|---|---|
| BC5CDR | extracción de relaciones end-to-end | F1 | **44,98 %** |
| KD-DTI | extracción de relaciones end-to-end | F1 | **38,42 %** |
| DDI | extracción de relaciones end-to-end | F1 | **40,76 %** |
| PubMedQA | question answering | accuracy | **78,2 %** — "creating a new record" |
| Total de tareas evaluadas | seis tareas de NLP biomédico | — | supera a modelos previos "en la mayoría" |

Advertencia de lectura para la clase: los F1 de 38–45 % en extracción de relaciones **parecen bajos vistos en aislamiento**. Son el estado del arte para esas tareas en 2022, no una nota de examen. Si la slide muestra estos números junto al 86,5 % de Med-PaLM 2 sin explicar que son tareas y métricas distintas, la comparación es engañosa.

El 78,2 % en PubMedQA es el número que el abstract destaca como récord ("creating a new record").

Ejemplo cualitativo citable: el "case study on text generation" muestra que BioGPT genera "fluent descriptions for biomedical terms" — es decir, dado un término biomédico, produce una descripción coherente. El abstract no muestra ningún ejemplo concreto de esa generación.

## Inconsistencies / open questions

- **La captura trae solo el abstract, no el cuerpo del paper.** Lo que la clase necesitaría y no está acá:
  - **Cuáles son las seis tareas**. El abstract nombra cuatro benchmarks (BC5CDR, KD-DTI, DDI, PubMedQA) pero dice "six biomedical NLP tasks". Faltan dos, sin identificar.
  - **En cuáles NO supera a los modelos previos.** El abstract dice "outperforms previous models on most tasks" — "most", no "all". Cuáles son las excepciones no está.
  - Los **ejemplos concretos de generación** del case study. Es el material más ilustrativo para una clase y no está en la captura.
  - El **tamaño del modelo** (parámetros) y la composición del corpus de preentrenamiento (el abstract dice "large scale biomedical literature" sin cuantificar).
  - Los **baselines** contra los que se compara cada número.
  - Si hubo **prompting** o solo fine-tuning por tarea. Esto importa mucho para el encuadre de la clase: el abstract no aclara el régimen de evaluación, así que **usar BioGPT como ejemplo de prompting no está sostenido por esta fuente**.
- Relevancia para una clase de *prompting*: BioGPT es sobre todo un paper de preentrenamiento de dominio, no de prompting. Encaja en el deck como contexto ("existen modelos biomédicos dedicados") más que como técnica. Conviene ser explícito sobre ese rol para no dar la impresión de que ilustra una técnica de prompting.
- Fecha: octubre 2022 (journal 2022). Anterior a la ola de modelos actuales; sus números ya no son estado del arte.
- Sin badge de licencia en la captura: reproducir figuras del PDF no está cubierto por una licencia abierta explícita según esta fuente.

## Images / diagrams

La captura no trae ninguna figura del paper. Solo cromo del sitio arXiv — y en este caso sin badge de licencia, así que son tres imágenes.



## Raw / preserved excerpts

**Abstract completo, verbatim (inglés):**

> Abstract:Pre-trained language models have attracted increasing attention in the biomedical domain, inspired by their great success in the general natural language domain. Among the two main branches of pre-trained language models in the general language domain, i.e., BERT (and its variants) and GPT (and its variants), the first one has been extensively studied in the biomedical domain, such as BioBERT and PubMedBERT. While they have achieved great success on a variety of discriminative downstream biomedical tasks, the lack of generation ability constrains their application scope. In this paper, we propose BioGPT, a domain-specific generative Transformer language model pre-trained on large scale biomedical literature. We evaluate BioGPT on six biomedical NLP tasks and demonstrate that our model outperforms previous models on most tasks. Especially, we get 44.98%, 38.42% and 40.76% F1 score on BC5CDR, KD-DTI and DDI end-to-end relation extraction tasks respectively, and 78.2% accuracy on PubMedQA, creating a new record. Our case study on text generation further demonstrates the advantage of BioGPT on biomedical literature to generate fluent descriptions for biomedical terms. Code is available at https://github.com/microsoft/BioGPT.

**Comments y referencia de journal, verbatim** (la cita bibliográfica formal más completa del corpus web):

> Comments: Published at Briefings in Bioinformatics. Code is available at https://github.com/microsoft/BioGPT

> Journal reference: Briefings in Bioinformatics, 2022;, bbac409 Related DOI: https://doi.org/10.1093/bib/bbac409

**Ficha bibliográfica, verbatim:**

> **arXiv:2210.10341** (cs)  [Submitted on 19 Oct 2022 ([v1](https://arxiv.org/abs/2210.10341v1)), last revised 3 Apr 2023 (this version, v3)]

> Authors: Renqian Luo, Liai Sun, Yingce Xia, Tao Qin, Sheng Zhang, Hoifung Poon, Tie-Yan Liu

> Subjects: Computation and Language (cs.CL); Artificial Intelligence (cs.AI) Cite as: arXiv:2210.10341 [cs.CL] (or arXiv:2210.10341v3 [cs.CL] for this version) https://doi.org/10.48550/arXiv.2210.10341

**Enlaces al texto completo:**

> - View PDF: https://arxiv.org/pdf/2210.10341
> - HTML (experimental): https://arxiv.org/html/2210.10341v3
> - TeX Source: https://arxiv.org/src/2210.10341
