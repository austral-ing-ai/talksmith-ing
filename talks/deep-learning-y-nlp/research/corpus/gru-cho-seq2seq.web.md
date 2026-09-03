---
source_file: research/web/gru-cho-seq2seq/
source_type: web-capture
ingested_at: 2026-08-14
---

# Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation — GRU (arXiv:1406.1078) — página de abstract

## Provenance
- Original location: `research/web/gru-cho-seq2seq/`
- Format: web-capture (`page.md` extraído de `original.html`; assets en `assets/`)
- URL: https://arxiv.org/abs/1406.1078
- Título de la captura: `[1406.1078] Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation`
- HTTP status: 200 · byte_size: 43144
- fetched_at: 2026-08-14T16:38:23Z
- Author / source (if known): Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio (Université de Montréal / Université du Maine — las afiliaciones no figuran en la página de abstract)
- Date of original (if known): enviado el 3 de junio de 2014 (v1); última revisión 3 de septiembre de 2014 (v3, la versión capturada)
- Identificadores: arXiv:1406.1078 [cs.CL] · DOI https://doi.org/10.48550/arXiv.1406.1078
- Materias: Computation and Language (cs.CL); Machine Learning (cs.LG); Neural and Evolutionary Computing (cs.NE); Machine Learning (stat.ML)
- Venue: **EMNLP 2014** (declarado en el campo `Comments`)

## Key claims

Todo lo sustantivo de esta captura está en el abstract.

- **La propuesta**: un modelo de red neuronal nuevo llamado **RNN Encoder-Decoder**, compuesto por dos redes neuronales recurrentes.
- **La mecánica, en una frase**: una RNN codifica una secuencia de símbolos en una representación vectorial de **longitud fija**; la otra decodifica esa representación en otra secuencia de símbolos. El cuello de botella de longitud fija es explícito en el abstract — y es justamente la limitación que después motivaría la atención.
- **Cómo se entrena**: encoder y decoder se entrenan *conjuntamente* para maximizar la probabilidad condicional de la secuencia objetivo dada la secuencia fuente.
- **Resultado empírico**: el rendimiento de un sistema de traducción automática estadística mejora empíricamente al usar las probabilidades condicionales de pares de frases computadas por el RNN Encoder-Decoder como *feature adicional* en el modelo log-lineal existente. Es decir: en 2014 el modelo neuronal todavía no reemplaza al sistema estadístico, lo asiste.
- **Resultado cualitativo**: el modelo aprende una representación de frases lingüísticas semántica y sintácticamente significativa.
- **Lo que respalda la slide 25** ("GRU listado como la variante 'simplificada' de RNN"): este es el paper donde se introduce la unidad recurrente con compuertas que luego se conoce como **GRU**. Pero **la captura no lo dice**: el abstract no menciona la unidad, ni la sigla GRU, ni la palabra *gated*, ni ninguna comparación con LSTM. El abstract habla del modelo encoder-decoder, no de la celda. La atribución de la GRU a este paper es correcta y estándar, pero **no es citable contra este corpus**. Ver `Inconsistencies / open questions`.

## Definitions and terminology

- **RNN Encoder-Decoder** — el modelo propuesto: dos RNN, una que codifica y otra que decodifica, entrenadas juntas.
- **Recurrent neural network (RNN)** — nombrada y usada, no definida.
- **Fixed-length vector representation** — el vector de tamaño fijo en el que el encoder comprime toda la secuencia de entrada. Término clave: es el cuello de botella que la clase suele usar para explicar por qué después hizo falta la atención.
- **Conditional probability of a target sequence given a source sequence** — el objetivo de entrenamiento.
- **Statistical machine translation (SMT)** — el sistema anfitrión al que el modelo neuronal se agrega como feature.
- **Log-linear model** — el modelo de combinación de features del sistema SMT clásico, al que se le suma la nueva señal.
- **Phrase pairs** — los pares de frases fuente/objetivo cuyas probabilidades condicionales aporta el modelo.
- **Phrase representations** — las representaciones de frases aprendidas, descritas como semántica y sintácticamente significativas.

**Advertencia para el uso en clase**: **GRU** (*gated recurrent unit*), *update gate*, *reset gate*, *vanishing gradient*, la comparación con **LSTM** y el término *seq2seq* — todo el vocabulario que la slide 25 reutiliza — **no aparece en esta captura**. La celda con compuertas se define en el cuerpo del paper (sección de la arquitectura propuesta), no en el abstract.

## Evidence and examples

| Dato | Valor reportado en el abstract |
|---|---|
| Mejora en traducción automática | "empirically found to improve" (sin número, sin BLEU) |
| Calidad de las representaciones | "semantically and syntactically meaningful" (cualitativo) |
| Tarea | traducción automática estadística, con el modelo neuronal como feature adicional |

- **La captura no trae ni un solo número.** Ni BLEU, ni tamaño de corpus, ni tiempo de entrenamiento, ni número de parámetros. El abstract es enteramente cualitativo. Si el deck quiere una cifra de este paper, **no está en este corpus**.
- **Peso del envío**: v1 875 KB, v2 460 KB, v3 551 KB — el envío más pesado de las cuatro capturas de arXiv, coherente con un paper con figuras de visualización de representaciones de frases.
- **Amplitud de clasificación**: cuatro categorías arXiv (cs.CL, cs.LG, cs.NE, stat.ML), más que cualquiera de las otras tres capturas — señal de que el trabajo se leyó como aporte tanto lingüístico como de arquitectura de redes.
- **Huella del paper**: 20 *blog links* (trackbacks); tres versiones entre junio y septiembre de 2014.

## Inconsistencies / open questions

- **La captura es la página de abstract, no el paper.** Todo lo que la clase quiera decir sobre la GRU — las compuertas de actualización y reinicio, por qué "simplifica" a la LSTM, cuántos parámetros ahorra, cómo mitiga el gradiente que se desvanece — **no está en este corpus**. Hay que traerlo del PDF (`/pdf/1406.1078`) o de otra fuente.
- **Esta es la brecha más grande de las cinco capturas.** El deck cita este paper *por* la GRU, y la GRU es precisamente lo único que el abstract no menciona. Es la desalineación más fuerte entre lo que la slide necesita y lo que el corpus contiene; conviene resolverla antes de que la slide 25 se apoye en esta cita.
- **"Simplificada" es una caracterización comparativa que el abstract no hace.** Que la GRU sea una simplificación de la LSTM es consenso posterior; el paper no se presenta así, y la LSTM ni siquiera se nombra en la captura.
- **El paper no es "seq2seq" en el sentido moderno.** El nombre de la carpeta (`gru-cho-seq2seq`) sugiere la línea seq2seq, pero el abstract deja claro que el modelo se usa como *feature adicional* dentro de un sistema de traducción estadística preexistente, no como sistema de traducción end-to-end. El seq2seq puro es de Sutskever et al. (2014), un paper distinto. Vale la pena no colapsar los dos.
- **El cuello de botella de longitud fija está nombrado pero no problematizado.** El abstract lo describe como propiedad del diseño, no como limitación. La crítica llegó después — con el paper de atención de Bahdanau (uno de los coautores acá), que tampoco está en este corpus.

## Images / diagrams

La página no trae ninguna figura del paper. Los tres archivos capturados son cromo de interfaz de arXiv — idénticos byte a byte a los de las otras tres capturas de arXiv de este corpus. Se conservan por completitud; **ninguno tiene valor didáctico**.



## Raw / preserved excerpts

**Abstract, verbatim (inglés, tal como aparece en la captura):**

> Abstract:In this paper, we propose a novel neural network model called RNN Encoder-Decoder that consists of two recurrent neural networks (RNN). One RNN encodes a sequence of symbols into a fixed-length vector representation, and the other decodes the representation into another sequence of symbols. The encoder and decoder of the proposed model are jointly trained to maximize the conditional probability of a target sequence given a source sequence. The performance of a statistical machine translation system is empirically found to improve by using the conditional probabilities of phrase pairs computed by the RNN Encoder-Decoder as an additional feature in the existing log-linear model. Qualitatively, we show that the proposed model learns a semantically and syntactically meaningful representation of linguistic phrases.

**Encabezado bibliográfico, verbatim:**

> # Computer Science > Computation and Language
>
> **arXiv:1406.1078** (cs)  [Submitted on 3 Jun 2014 ([v1](https://arxiv.org/abs/1406.1078v1)), last revised 3 Sep 2014 (this version, v3)]
>
> # Title:Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation
>
> Authors:Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio

**Bloque de metadatos, verbatim:**

> Comments: EMNLP 2014 Subjects: Computation and Language (cs.CL); Machine Learning (cs.LG); Neural and Evolutionary Computing (cs.NE); Machine Learning (stat.ML) Cite as: [arXiv:1406.1078](https://arxiv.org/abs/1406.1078) [cs.CL] (or [arXiv:1406.1078v3](https://arxiv.org/abs/1406.1078v3) [cs.CL] for this version) [https://doi.org/10.48550/arXiv.1406.1078](https://doi.org/10.48550/arXiv.1406.1078) Focus to learn more  arXiv-issued DOI via DataCite

**Historial de versiones, verbatim:**

> From: KyungHyun Cho
> **[v1]** Tue, 3 Jun 2014 17:47:08 UTC (875 KB)
> **[v2]** Thu, 24 Jul 2014 20:07:13 UTC (460 KB)
> **[v3]** Wed, 3 Sep 2014 00:25:02 UTC (551 KB)

**Enlaces de acceso al texto completo (lo que la captura *no* bajó):**

> - [View PDF](/pdf/1406.1078)
> - [HTML (experimental)](https://arxiv.org/html/1406.1078v3)

**Señal de impacto, verbatim:**

> ### [20 blog links](/tb/1406.1078)
