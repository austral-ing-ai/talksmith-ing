---
source_file: chain-of-thought-wei
source_type: web-capture
ingested_at: 2026-08-14
---

# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (Wei et al., 2022)

## Provenance
- Original location: `research/web/chain-of-thought-wei/`
- Format: web capture (HTML + `page.md` extraído), página de abstract de arXiv
- URL: https://arxiv.org/abs/2201.11903
- `fetched_at`: 2026-08-14T16:56:08Z
- `http_status`: 200
- Título capturado: `[2201.11903] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models`
- Autores: Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou
- Fecha del original: enviado el 28 de enero de 2022 (v1); última revisión 10 de enero de 2023 (v6, la capturada)
- arXiv ID: arXiv:2201.11903 [cs.CL] — DOI 10.48550/arXiv.2201.11903
- Materias: Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
- Venue: el abstract de arXiv no declara venue. El paper se publicó en NeurIPS 2022, pero **eso no está en la captura** — si la clase lo cita como "NeurIPS 2022", el dato viene de fuera de esta fuente.
- Licencia: CC BY 4.0

## Key claims

Desglose de las afirmaciones del abstract (texto verbatim en `Raw / preserved excerpts`):

- Generar una *chain of thought* — una serie de pasos de razonamiento intermedios — mejora significativamente la capacidad de los modelos de lenguaje grandes para hacer razonamiento complejo.
- Esas capacidades de razonamiento **emergen naturalmente en modelos suficientemente grandes**. La emergencia por escala es una afirmación central del paper, no un detalle: en modelos chicos el método no rinde.
- El método es simple: se llama *chain of thought prompting* y consiste en dar unas pocas demostraciones de cadena de pensamiento como ejemplares dentro del prompt. No hay reentrenamiento, no hay fine-tuning, no hay cambio de arquitectura — es solo el prompt.
- Experimentos sobre tres modelos de lenguaje grandes muestran mejora en tareas de razonamiento aritmético, de sentido común y simbólico.
- Las ganancias empíricas pueden ser llamativas ("striking").
- Caso concreto: un modelo de 540 mil millones de parámetros, promptado con apenas **ocho** ejemplares de chain of thought, alcanza *state of the art* en el benchmark GSM8K de problemas matemáticos verbales, superando incluso a un GPT-3 con fine-tuning y verificador.

## Definitions and terminology

- **Chain of thought (cadena de pensamiento)** — definición del propio abstract: "a series of intermediate reasoning steps". Es la salida del modelo, no la entrada: lo que el modelo genera antes de dar la respuesta final.
- **Chain-of-thought prompting** — la técnica: "a few chain of thought demonstrations are provided as exemplars in prompting". O sea, few-shot donde cada ejemplo no muestra solo pregunta→respuesta sino pregunta→razonamiento→respuesta. Es un caso particular de few-shot (ver `few-shot-learners-brown.web.md`), no una categoría aparte.
- **Exemplars (ejemplares)** — las demostraciones incluidas en el prompt. El abstract usa "eight chain of thought exemplars" como cifra concreta.
- **Emergent abilities (por escala)** — el abstract dice que las capacidades de razonamiento "emerge naturally in sufficiently large language models". El término técnico "emergent" y su umbral cuantitativo no se definen en el abstract.
- **GSM8K** — benchmark de problemas matemáticos verbales (*math word problems*) de escuela primaria. El abstract lo nombra y lo usa como métrica pero no lo describe más allá de "math word problems".

## Evidence and examples

Todo lo cuantitativo que la captura ofrece (y es poco, porque es solo el abstract):

| Resultado | Valor reportado |
|---|---|
| Modelo del resultado destacado | 540B de parámetros |
| Cantidad de ejemplares en el prompt | 8 |
| Benchmark | GSM8K (math word problems) |
| Resultado | "state of the art accuracy" — **sin número** |
| Comparación | Supera a GPT-3 con fine-tuning + verificador |
| Modelos evaluados | "three large language models" — **sin nombrar cuáles** |
| Tipos de tarea | aritmético, sentido común, simbólico |

Advertencia para la clase: el abstract **no da el porcentaje de accuracy en GSM8K**. Dice "state of the art" y nada más. Si la slide quiere un número (el valor que circula en la literatura es ~57 % con PaLM 540B), ese número **no sale de esta captura**.

## Inconsistencies / open questions

- **La captura trae solo el abstract, no el cuerpo del paper.** Es una página `arxiv.org/abs/`, que es la ficha bibliográfica. Lo que la clase necesitaría y no está acá:
  - La **Figura 1**, que es la imagen canónica del paper (prompt estándar vs. prompt con cadena de pensamiento, lado a lado, con el ejemplo de las pelotas de tenis). Si el deck reproduce ese esquema, la imagen hay que sacarla del PDF, no de esta captura.
  - Los **números concretos por benchmark y por modelo** (las tablas de resultados). El abstract solo dice "state of the art" sin cifra.
  - La identidad de los tres modelos evaluados (el abstract no los nombra).
  - La **curva de escala** que sustenta la afirmación de emergencia — el hallazgo de que por debajo de cierto tamaño el chain-of-thought no ayuda o incluso perjudica.
  - Los prompts exactos de los ocho ejemplares.
- El abstract dice "sufficiently large" sin fijar un umbral. Si la clase afirma "a partir de X parámetros", esa precisión no tiene respaldo acá.
- Ningún venue declarado en la ficha de arXiv. Atribuir "NeurIPS 2022" excede lo que la captura sostiene.

## Images / diagrams

La captura no trae ninguna figura del paper. Todo lo que hay es cromo del sitio arXiv — logo e iconos de compartir. No hay contenido científico en ninguna imagen de esta carpeta.



## Raw / preserved excerpts

**Abstract completo, verbatim (inglés, tal como aparece en la captura):**

> Abstract:We explore how generating a chain of thought -- a series of intermediate reasoning steps -- significantly improves the ability of large language models to perform complex reasoning. In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain of thought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting. Experiments on three large language models show that chain of thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks. The empirical gains can be striking. For instance, prompting a 540B-parameter language model with just eight chain of thought exemplars achieves state of the art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier.

**Ficha bibliográfica, verbatim:**

> **arXiv:2201.11903** (cs)  [Submitted on 28 Jan 2022 ([v1](https://arxiv.org/abs/2201.11903v1)), last revised 10 Jan 2023 (this version, v6)]

> Authors: Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou

> Subjects: Computation and Language (cs.CL); Artificial Intelligence (cs.AI) Cite as: arXiv:2201.11903 [cs.CL] (or arXiv:2201.11903v6 [cs.CL] for this version) https://doi.org/10.48550/arXiv.2201.11903

**Historial de versiones, verbatim** (útil para fechar la cita: la v1 es de enero de 2022, la que la clase probablemente cita como "Wei et al., 2022"):

> **[v1]** Fri, 28 Jan 2022 02:33:07 UTC (944 KB)
> **[v2]** Wed, 6 Apr 2022 03:51:50 UTC (933 KB)
> **[v3]** Wed, 1 Jun 2022 00:10:30 UTC (303 KB)
> **[v4]** Mon, 13 Jun 2022 21:44:34 UTC (283 KB)
> **[v5]** Mon, 10 Oct 2022 20:21:17 UTC (285 KB)
> **[v6]** Tue, 10 Jan 2023 23:07:57 UTC (306 KB)

**Enlaces al texto completo que la captura ofrece** (por si hace falta ir al cuerpo del paper):

> - View PDF: https://arxiv.org/pdf/2201.11903
> - HTML (experimental): https://arxiv.org/html/2201.11903v6
> - TeX Source: https://arxiv.org/src/2201.11903
