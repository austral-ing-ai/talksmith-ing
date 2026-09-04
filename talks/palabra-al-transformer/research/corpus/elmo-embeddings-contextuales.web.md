---
source_file: research/web/elmo-embeddings-contextuales/
source_type: web-capture
ingested_at: 2026-08-14
---

# Deep contextualized word representations — ELMo (arXiv:1802.05365) — página de abstract

## Provenance
- Original location: `research/web/elmo-embeddings-contextuales/`
- Format: web-capture (`page.md` extraído de `original.html`; assets en `assets/`)
- URL: https://arxiv.org/abs/1802.05365
- Título de la captura: `[1802.05365] Deep contextualized word representations`
- HTTP status: 200 · byte_size: 41917
- fetched_at: 2026-08-14T16:38:23Z
- Author / source (if known): Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, Luke Zettlemoyer (Allen Institute for AI / Univ. of Washington — la afiliación no figura en la página de abstract)
- Date of original (if known): enviado el 15 de febrero de 2018 (v1); última revisión 22 de marzo de 2018 (v2, la versión capturada). El campo `Comments` aclara que se publicó originalmente en OpenReview el 27 de octubre de 2017.
- Identificadores: arXiv:1802.05365 [cs.CL] · DOI https://doi.org/10.48550/arXiv.1802.05365
- Materias: Computation and Language (cs.CL)
- Venue: **NAACL 2018** (declarado en el campo `Comments`; v2 es la versión *camera ready*)

## Key claims

Todo lo sustantivo de esta captura está en el abstract.

- **La propuesta**: un tipo nuevo de representación de palabras *profundamente contextualizada*. Este es el paper que la clase nombra como ELMo — el acrónimo **no aparece** en el abstract capturado, sólo la descripción.
- **Qué modela, explícitamente en dos ejes**: (1) características complejas del uso de la palabra — sintaxis y semántica; (2) **cómo ese uso varía según el contexto lingüístico**, es decir, modelar la polisemia. El propio abstract nombra la polisemia como el problema a resolver. Esto es exactamente el contraste que la clase necesita frente a Word2Vec, donde cada palabra tiene un único vector fijo.
- **De dónde salen los vectores**: son *funciones aprendidas de los estados internos* de un modelo de lenguaje bidireccional profundo (**biLM**) preentrenado sobre un corpus de texto grande. Dos ideas juntas: preentrenamiento sobre texto sin etiquetar, y uso de las representaciones internas de la red, no sólo de su salida.
- **Facilidad de adopción**: las representaciones "can be easily added to existing models" — se enchufan a arquitecturas ya existentes en lugar de exigir rediseñarlas.
- **Resultado empírico**: mejora significativa del estado del arte en **seis** problemas de NLP difíciles, entre ellos *question answering*, *textual entailment* y *sentiment analysis*.
- **El hallazgo analítico**: exponer los internos profundos de la red preentrenada es *crucial* — permite que los modelos downstream mezclen distintos tipos de señales de semi-supervisión. No alcanza con la última capa; la profundidad importa y las capas codifican cosas distintas.
- **Lo que respalda la slide 25** ("ELMo listado como variante de RNN que da embeddings contextuales"): la captura respalda de lleno la parte de *embeddings contextuales* — es literalmente el título y la tesis del paper. La parte de "variante de RNN" **no está en el abstract**: nunca se menciona RNN, LSTM ni recurrencia. El biLM de ELMo sí está construido con LSTMs bidireccionales apiladas, pero ese detalle arquitectónico vive en el cuerpo del paper, no acá. Ver `Inconsistencies / open questions`.

## Definitions and terminology

- **Deep contextualized word representation** — el término central: una representación de palabra que cambia según la oración en la que la palabra aparece, y que se construye a partir de varias capas de profundidad.
- **biLM (deep bidirectional language model)** — el único término técnico que el abstract define de hecho: el modelo de lenguaje bidireccional profundo, preentrenado sobre un corpus grande, cuyos estados internos alimentan las representaciones. El abstract explicita la sigla: "a deep bidirectional language model (biLM)".
- **Polysemy / polisemia** — nombrada explícitamente como el fenómeno que motiva el trabajo: la misma palabra con significados distintos según el contexto.
- **Internal states** — los estados de las capas intermedias del biLM; las representaciones son "learned functions" de ellos, no los estados crudos.
- **Semi-supervision signals** — señales de semi-supervisión; el abstract sostiene que exponer los internos deja que el modelo downstream mezcle varios tipos.
- **Complex characteristics of word use (syntax and semantics)** — el primero de los dos ejes que la representación modela.

**Advertencia para el uso en clase**: **ELMo** (*Embeddings from Language Models*), **LSTM**, **RNN**, *character convolutions* y la combinación ponderada de capas por tarea — vocabulario que la clase reutiliza — **no aparecen en esta captura**.

## Evidence and examples

| Dato | Valor reportado en el abstract |
|---|---|
| Tareas de NLP mejoradas | seis ("six challenging NLP problems") |
| Tareas nombradas | question answering, textual entailment, sentiment analysis |
| Magnitud de la mejora | "significantly improve the state of the art" (sin número) |
| Corpus de preentrenamiento | "a large text corpus" (sin tamaño) |

- **La captura no trae ni un solo número de benchmark.** El paper reporta deltas concretos por tarea (SQuAD, SNLI, SST-5, coreferencia, NER, SRL), pero el abstract se queda en "significantly". Si el deck quiere una cifra, **no está en este corpus**.
- **De las seis tareas, sólo tres se nombran.** Las otras tres no figuran en la captura.
- **Peso del envío**: v1 135 KB, v2 140 KB — consistente con un paper de conferencia con figuras y tablas.
- **Huella del paper**: 22 *blog links* (trackbacks) registrados por arXiv; dos versiones (febrero y marzo de 2018).
- **Trazabilidad de la publicación**: el campo `Comments` documenta el recorrido completo — OpenReview el 27 de octubre de 2017, arXiv en febrero de 2018, camera ready de NAACL 2018 en marzo. Un dato menor, pero es el único de las cuatro capturas de arXiv que muestra el ciclo entero.

## Inconsistencies / open questions

- **La captura es la página de abstract, no el paper.** Todo lo que la clase quiera decir sobre *cómo* está construido ELMo — LSTMs bidireccionales apiladas, convoluciones a nivel de carácter, la combinación ponderada de capas aprendida por tarea, el ejemplo canónico de una palabra polisémica con dos vectores distintos — **no está en este corpus**.
- **"Variante de RNN" (slide 25) no tiene respaldo en esta captura.** El abstract no menciona recurrencia en ninguna forma. La afirmación es correcta respecto del paper completo (el biLM son LSTMs), pero hay que citarla contra otra fuente si la slide la sostiene.
- **El acrónimo ELMo no aparece.** Quien busque "ELMo" en `page.md` no lo encuentra. La conexión entre el nombre que usa la clase y este paper hay que hacerla explícita.
- **La comparación con Word2Vec/GloVe no está en el abstract.** El contraste "vector fijo vs. vector contextual" — que es todo el punto pedagógico de la slide — está implícito en "how these uses vary across linguistic contexts", pero el abstract nunca nombra los métodos previos. Es una inferencia del docente, razonable pero no citable literalmente.
- **Sin números, la afirmación de mejora es difícil de calibrar.** "Significantly improve the state of the art across six challenging NLP problems" es lo máximo que sostiene el corpus.
- La captura no dice nada sobre el costo de preentrenamiento del biLM, ni sobre las limitaciones de ELMo que motivaron el salto a BERT y a los Transformers.

## Images / diagrams

La página no trae ninguna figura del paper. Los tres archivos capturados son cromo de interfaz de arXiv — idénticos byte a byte a los de las otras tres capturas de arXiv de este corpus. Se conservan por completitud; **ninguno tiene valor didáctico**.



## Raw / preserved excerpts

**Abstract, verbatim (inglés, tal como aparece en la captura):**

> Abstract:We introduce a new type of deep contextualized word representation that models both (1) complex characteristics of word use (e.g., syntax and semantics), and (2) how these uses vary across linguistic contexts (i.e., to model polysemy). Our word vectors are learned functions of the internal states of a deep bidirectional language model (biLM), which is pre-trained on a large text corpus. We show that these representations can be easily added to existing models and significantly improve the state of the art across six challenging NLP problems, including question answering, textual entailment and sentiment analysis. We also present an analysis showing that exposing the deep internals of the pre-trained network is crucial, allowing downstream models to mix different types of semi-supervision signals.

**Encabezado bibliográfico, verbatim:**

> # Computer Science > Computation and Language
>
> **arXiv:1802.05365** (cs)  [Submitted on 15 Feb 2018 ([v1](https://arxiv.org/abs/1802.05365v1)), last revised 22 Mar 2018 (this version, v2)]
>
> # Title:Deep contextualized word representations
>
> Authors:Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, Luke Zettlemoyer

**Bloque de metadatos, verbatim:**

> Comments: NAACL 2018. Originally posted to openreview 27 Oct 2017. v2 updated for NAACL camera ready Subjects: Computation and Language (cs.CL) Cite as: [arXiv:1802.05365](https://arxiv.org/abs/1802.05365) [cs.CL] (or [arXiv:1802.05365v2](https://arxiv.org/abs/1802.05365v2) [cs.CL] for this version) [https://doi.org/10.48550/arXiv.1802.05365](https://doi.org/10.48550/arXiv.1802.05365) Focus to learn more  arXiv-issued DOI via DataCite

**Historial de versiones, verbatim:**

> From: Matthew Peters
> **[v1]** Thu, 15 Feb 2018 00:05:11 UTC (135 KB)
> **[v2]** Thu, 22 Mar 2018 21:59:40 UTC (140 KB)

**Enlaces de acceso al texto completo (lo que la captura *no* bajó):**

> - [View PDF](/pdf/1802.05365)
> - [HTML (experimental)](https://arxiv.org/html/1802.05365v2)

**Señal de impacto, verbatim:**

> ### [22 blog links](/tb/1802.05365)
