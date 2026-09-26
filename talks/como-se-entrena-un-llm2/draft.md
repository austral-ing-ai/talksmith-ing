---
presentation: Inteligencia Artificial Generativa (AI Gen)
class: "Clase 9: Cómo se entrena un LLM"
research: research/corpus/
description: Slides are grouped into Sections. Each Section contains one or more Slides.
presenter: Paulo Veiga, Claudio Righetti, Marco Sorondo (Universidad Austral)
audience: Estudiantes de grado de Ingeniería de Software con base técnica fuerte
duration: 90 min
date: 2026-09-30
---

# Thesis

**Claim:** Un LLM se entrena dos veces. El pre-entrenamiento predice el token siguiente sobre billones de tokens de la web y fija lo que el modelo sabe. El post-entrenamiento usa de decenas de miles a alrededor de un millón de ejemplos escritos o juzgados por personas, o un verificador automático, y fija cómo se comporta.

**Why it matters:** Cada conducta de un asistente (contestar en lugar de continuar el texto, llamar a una herramienta, pensar o no pensar, inventar un dato) viene de la señal que la premió durante el entrenamiento. Con esa lectura, un ingeniero decide cuándo alcanza un prompt, cuándo hace falta RAG y cuándo conviene ajustar pesos.

**Presenter feedback:**

---

# Agenda

**Narrative arc:** La clase abre con la evidencia de que hay dos entrenamientos distintos: el mismo prompt a GPT-3 y a InstructGPT, el recorrido completo en una figura y el reparto del cómputo entre las dos fases (1). Después sigue una cadena causal. Las leyes de escala fijan cuántos tokens pide un modelo de un tamaño dado, y la práctica actual pide todavía más para los modelos chicos (2). Esos tokens salen de la web: se filtran, se sesgan hacia el inglés y hacia ciertos sitios, y se acercan a un techo (3). Lo que sale del pre-entrenamiento solo continúa texto; el post-entrenamiento lo convierte en asistente con demostraciones y con preferencias (4). La misma idea, una señal que premia una conducta, explica cómo se entrenan las herramientas, el razonamiento y el modo de pensamiento, y también por qué el modelo inventa (5). El cierre es la parte que un equipo chico sí puede entrenar: cuándo ajustar pesos, LoRA, QLoRA y destilación (6).

**Sections (in delivery order):**

- 1. Dos entrenamientos
- 2. Tamaño y datos
- 3. De dónde salen los tokens
- 4. Post-entrenamiento
- 5. Conductas premiadas
- 6. Ajustar un modelo

**Presenter feedback:**

---

# 1. Dos entrenamientos

**Goal of this section:** Mostrar con un ejemplo, una figura y un número que un LLM pasa por dos entrenamientos con datos y objetivos distintos, y dejar planteada la pregunta que ordena la clase: qué señal premió cada conducta.

**Presenter feedback:**

---

## 1. La misma consigna, dos modelos

<!-- template: comparison -->

### Content

**GPT-3 175B e InstructGPT 175B recibieron la misma consigna.** "Serendipity means the occurrence and development of events by chance in a happy or beneficial way. Use the word in a sentence."

- **GPT-3, solo pre-entrenado.** "Serendipity is the ability to see something good in something bad. Use the word in a sentence. Serendipity means to be happy with what you have. Use the word in a sentence. […]" Continúa el patrón del texto: escribe más consignas.
- **InstructGPT, pre-entrenado y post-entrenado.** "Serendipity can be defined as the happy chance occurrence of events leading to a beneficial outcome. For example, when Lori first moved to the city and started her job search, it was serendipity that she stumbled upon the perfect opportunity […]" Cumple la consigna.

### Sources

- `corpus/ouyang-2022-instructgpt.pdf.md` (Fig. 47, App. F): prompt, completion de GPT-3 175B y de InstructGPT 175B, verbatim. El apéndice muestrea GPT-3 a T = 0,7 e InstructGPT a T = 1 ("this slightly disadvantages InstructGPT").
- `corpus/ouyang-2022-instructgpt.pdf.md` (Key claims): el objetivo de pre-entrenamiento, "predicting the next token on a webpage from the internet", es distinto de "follow the user's instructions helpfully and safely".

### Speaker notes

Arrancá leyendo la consigna y preguntando qué esperan que conteste un modelo entrenado solo para predecir el token siguiente. La respuesta de GPT-3 tiene sentido: en la web, después de una línea con formato de ejercicio suele venir otro ejercicio igual. InstructGPT tiene la misma arquitectura y el mismo tamaño; la diferencia es un segundo entrenamiento. Dejá planteada la pregunta que ordena la clase: si la red es la misma, lo que cambió es qué se premió al entrenarla. En la clase pasada vieron la pérdida del pre-entrenamiento; hoy se ve qué pasa antes (de dónde salen los datos y cuántos hacen falta) y qué pasa después. Las citas quedan en inglés porque son la salida real de los modelos. Tiempo objetivo: ~3 min.

### Presenter feedback

---

## 2. Tres etapas, cuatro conjuntos de datos

### Content

**Cada etapa entrena con otro tipo de dato y optimiza otra cosa. Del pre-entrenamiento al RLHF los datos bajan de más de un billón de tokens a decenas o cientos de miles de ejemplos.**

![Flujo de entrenamiento: pre-entrenamiento sobre texto de internet, SFT con datos de demostración y RLHF con datos de comparación y prompts, con la escala de cada conjunto](research/corpus/huyen-aie-chapter-summaries.web/images/rlhf.png)

### Sources

- `corpus/huyen-aie-chapter-summaries.web.md` (imagen `rlhf.png`, Ch. 2): "The overall training workflow with pre-training, SFT, and RLHF. Image originally from my RLHF blog post (May 2023)". Escalas al pie de la figura: >1 trillion tokens; 10K–100K (prompt, response); 100K–1M comparisons; 10K–100K prompts.
- `corpus/huyen-2023-rlhf.web.md` (Key claims): SFT de 10.000 a 100.000 pares; datos del modelo de recompensa de 100K a 1M; prompts de RL de 10.000 a 100.000.
- `corpus/Data.pdf.md` (Fig. 2-10): la misma figura en el libro *AI Engineering*, cap. 2.

### Speaker notes

Recorré la figura de izquierda a derecha y marcá solo tres cosas por columna: qué dato entra, qué objetivo se optimiza, qué modelo sale. Pre-entrenamiento: texto de internet, completar texto, modelo base. SFT: pares (prompt, respuesta) escritos por personas, modelo que dialoga. RLHF: comparaciones entre respuestas para entrenar un modelo que puntúa, y después RL para maximizar ese puntaje. La fila de abajo es la que importa para la clase: la escala cae de más de un billón de tokens a entre decenas de miles y un millón de ejemplos. Las secciones 2 y 3 son la columna de la izquierda; la 4 son las otras tres. El "trillion" del inglés es un billón en español (10¹²); decilo una vez para toda la clase. Tiempo objetivo: ~3 min.

### Presenter feedback

---

## 3. Dónde va el cómputo

<!-- template: stat -->

### Content

**En InstructGPT, el post-entrenamiento usó menos del 2 % del cómputo total.**

- **3.640 petaflop/s-días.** Pre-entrenamiento de GPT-3 175B.
- **4,9 petaflop/s-días.** SFT del modelo de 175B.
- **60 petaflop/s-días.** RLHF del modelo de 175B.
- **1,75 %.** Parte del post-entrenamiento en el total.

Nota: el cálculo no incluye el modelo de recompensa (6B) ni el costo de las personas que escribieron y compararon respuestas.

### Sources

- `corpus/ouyang-2022-instructgpt.pdf.md` (Key claims): "training our 175B SFT model requires 4.9 petaflops/s-days and training our 175B PPO-ptx model requires 60 petaflops/s-days, compared to 3,640 petaflops/s-days for GPT-3".
- Derivación: 1,75 % = (4,9 + 60) / (3.640 + 4,9 + 60) = 64,9 / 3.704,9 — `corpus/ouyang-2022-instructgpt.pdf.md`.
- `corpus/huyen-2023-rlhf.web.md` (Key claims): "For the InstructGPT model, pretraining takes up 98% of the overall compute and data resources." Consistente con el 1,75 % derivado (98,25 % de pre-entrenamiento).
- `corpus/ouyang-2022-instructgpt.pdf.md` (Inconsistencies): el paper no da el costo monetario del etiquetado.

### Speaker notes

El número parece decir que el post-entrenamiento es un detalle. El 1,75 % corresponde al modelo de 175B; el mismo paper muestra otro dato que retomás en la lámina 4.6: la versión post-entrenada de 1,3B fue preferida por los evaluadores sobre GPT-3 de 175B. Lo caro del post-entrenamiento son las personas: unas 40 contratadas para escribir demostraciones y comparar respuestas, y el paper no dice cuánto costó. La nota al pie es para quien pregunte por qué no se cuenta el modelo de recompensa: es de 6B, chico frente a 175B, y el paper no da su cómputo. Tiempo objetivo: ~2 min.

### Presenter feedback

---

# 2. Tamaño y datos

**Goal of this section:** Dar las tres cantidades que describen un pre-entrenamiento y la regla que las relaciona, y llegar a la conclusión que abre la sección siguiente: la práctica actual, sobre todo en modelos chicos, pide más tokens por parámetro que el óptimo de Chinchilla.

**Presenter feedback:**

---

## 1. Parámetros, tokens y cómputo

### Content

**Un pre-entrenamiento se describe con tres números. El tercero sale de los otros dos: C ≈ 6 · N · D.**

- **Parámetros (N).** Los pesos que el entrenamiento ajusta. Chinchilla tiene 70.000 millones.
- **Tokens de entrenamiento (D).** Las posiciones de texto sobre las que se calcula la pérdida. Chinchilla vio 1,4 billones.
- **Cómputo (C).** Las operaciones de punto flotante (FLOPs) del entrenamiento: unas 2 por parámetro y por token en el forward, y el doble en el backward. Chinchilla: 6 × 7 × 10¹⁰ × 1,4 × 10¹² ≈ 5,9 × 10²³ FLOPs.

### Sources

- `corpus/kaplan-2020-scaling-laws.pdf.md` (Definitions): "C ≈ 6NBS … the factor 6 accounts for forward (≈2N per token) and backward passes"; B·S = tokens procesados.
- `corpus/hoffmann-2022-chinchilla.pdf.md` (Definitions, Table 1): FLOPs(N, D) ≈ 6ND; Chinchilla 70B y 1,4T tokens; el conteo completo da entre 0,99 y 1,10 veces 6ND (Table A4).
- Derivación: 5,88 × 10²³ = 6 × 70 × 10⁹ × 1,4 × 10¹² — `corpus/hoffmann-2022-chinchilla.pdf.md`. El paper da 5,76 × 10²³ como presupuesto de Gopher, el mismo que usó Chinchilla; la diferencia (2 %) viene de la aproximación 6ND.

### Speaker notes

Enganchá con la última lámina de la clase 8: la pérdida es la cross-entropy del token siguiente y cada posición es un ejemplo, así que D cuenta ejemplos. El 6 tiene una justificación de una línea: en el forward cada parámetro hace una multiplicación y una suma por token; el backward cuesta más o menos el doble porque calcula gradientes respecto de activaciones y de pesos. Hacé la cuenta de Chinchilla en el pizarrón; da 5,9 × 10²³ y el paper dice 5,76 × 10²³. Para dar escala: 1,4 billones de tokens son unos 21 millones de libros, a 67.000 tokens por libro (la equivalencia es de Huyen). Tiempo objetivo: ~3 min.

### Presenter feedback

---

## 2. La pérdida baja como una potencia

### Content

**Kaplan et al. (2020): la pérdida de test baja de forma predecible con N, D y C. La forma del modelo (profundidad o ancho) casi no importa.**

- **Ley de potencia.** L(N) = (N_c / N)^0,076: duplicar los parámetros multiplica la pérdida por 0,95. Vale mientras ni los datos ni el cómputo limiten.
- **Receta de 2020.** Con 10 veces más cómputo conviene un modelo unas 5,4 veces más grande y solo 1,9 veces más tokens (N ∝ C^0,73, D ∝ C^0,27).
- **Resultado en la práctica.** Los modelos grandes de 2020 y 2021 crecieron en parámetros y se quedaron en unos 300.000 millones de tokens: GPT-3 175B, Jurassic 178B y Gopher 280B, los tres con 300.000 millones.

### Sources

- `corpus/kaplan-2020-scaling-laws.pdf.md` (Key claims): α_N ≈ 0,076; "doubling the number of parameters yields a loss that is smaller by a factor 2^−α_N = 0.95"; "Performance depends strongly on scale, weakly on model shape"; N ∝ C_min^0,73, D ∼ C^0,27.
- Derivación: 5,4 = 10^0,73 y 1,9 = 10^0,27 — `corpus/kaplan-2020-scaling-laws.pdf.md`. El mismo paper redondea a "~5x" y "~2x"; Hoffmann cita a Kaplan como 5,5× y 1,8× (`corpus/hoffmann-2022-chinchilla.pdf.md`, Key claims). Las tres versiones son compatibles; la lámina usa los exponentes.
- `corpus/hoffmann-2022-chinchilla.pdf.md` (Table 1): GPT-3 175B/300B, Jurassic 178B/300B, Gopher 280B/300B, MT-NLG 530B/270B.
- `corpus/kaplan-2020-scaling-laws.pdf.md` (Inconsistencies): el rango de escala figura como "more than seven", "more than six" y "eight … six … two" órdenes de magnitud según la sección; por eso la lámina no da la cifra.

### Speaker notes

La idea que tiene que quedar es la predictibilidad: con corridas chicas se ajusta una curva y se sabe de antemano cuánto va a mejorar una corrida cien veces más cara. Eso es lo que justifica gastar millones en un entrenamiento. El 0,95 sirve para dar intuición: duplicar el modelo baja la pérdida un 5 %. La receta de Kaplan resultó incompleta y la lámina siguiente explica por qué; el dato de la tercera viñeta es la evidencia de que la industria la siguió. Lámina de paso: no te detengas en las fórmulas. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 3. Parámetros y tokens crecen igual

<!-- design: split-right -->

### Content

**Hoffmann et al. (2022), con el modelo Chinchilla: para un presupuesto fijo, parámetros y tokens deben escalar en la misma proporción. Los modelos de 2021 eran demasiado grandes para los datos que vieron.**

- **Mismo cómputo, otro reparto.** Con el presupuesto de Gopher, Chinchilla usa 4 veces menos parámetros (70B frente a 280B) y 4,7 veces más tokens (1,4 billones frente a 300.000 millones).
- **Unos 20 tokens por parámetro.** 1,4 billones / 70.000 millones = 20. Para 1B de parámetros la tabla del paper pide 20.200 millones de tokens.
- **Resultado.** En MMLU, un examen de opción múltiple de 57 materias, Chinchilla saca 67,6 % y Gopher 60,0 %, con el mismo cómputo.

![Parámetros óptimos en función del cómputo según tres métodos de Chinchilla y según Kaplan 2020; Gopher, GPT-3 y MT-NLG quedan por encima de la recta óptima y Chinchilla sobre ella](research/corpus/hoffmann-2022-chinchilla.pdf/images/fig-01-p002.png)

### Sources

- `corpus/hoffmann-2022-chinchilla.pdf.md` (Key claims, Fig. 1): "for every doubling of model size the number of training tokens should also be doubled"; Gopher 5,76 × 10²³ FLOPs; Chinchilla 70B y 1,4T tokens con el mismo cómputo.
- Derivación: 4 = 280B / 70B; 4,7 = 1,4T / 300B; 20 = 1,4T / 70B — `corpus/hoffmann-2022-chinchilla.pdf.md`. El abstract dice "4× more more data" (sic); la cuenta con Table 1 da 4,7×.
- `corpus/hoffmann-2022-chinchilla.pdf.md` (Table 3): 1B → 20,2B tokens. La regla "20 tokens por parámetro" no está enunciada en el paper; sale de su Table 3 y de la razón 1,4T/70B (Inconsistencies, open question).
- `corpus/hoffmann-2022-chinchilla.pdf.md` (Table 6): MMLU 5-shot 67,6 % vs 60,0 %; Fig. 6: 57 tareas (mejor en 51). El abstract dice 67,5 % (Inconsistencies); la lámina usa la tabla.

### Speaker notes

En la figura, la recta punteada es Kaplan y las de color son los tres métodos de Chinchilla; las estrellas de GPT-3, Gopher y MT-NLG quedan arriba, o sea, demasiados parámetros para su cómputo. Por qué Kaplan se equivocó, en una frase: usó el mismo calendario de learning rate para todas las corridas y modelos mayormente chicos, así que subestimó lo que rinde entrenar más tiempo un modelo más chico. El 20 es una regla práctica que se deriva de la tabla, no una ley; decilo así. Tiempo objetivo: ~4 min.

### Presenter feedback

---

## 4. Hoy se entrena de más a propósito

<!-- template: stat -->

### Content

**Desde 2023, varios modelos abiertos se entrenan con muchos más tokens por parámetro que el óptimo de Chinchilla, y la distancia es mayor en los modelos chicos: entre 10 y 100 veces. Un modelo chico cuesta menos cada vez que responde, y un modelo se entrena una vez y responde millones de veces.**

- **20 tokens por parámetro.** Chinchilla 70B, óptimo para el cómputo de entrenamiento.
- **Unos 29 tokens por parámetro.** Llama 2 70B, con 2 billones de tokens: cerca del óptimo.
- **Unos 286 tokens por parámetro.** Llama 2 7B, con los mismos 2 billones de tokens.
- **214 tokens por parámetro.** Llama 3 70B, entrenado con 15 billones de tokens.

### Sources

- `corpus/touvron-2023-llama2.pdf.md` (Table 1): Llama 2 7B, 2,0T tokens; "after pretraining on 2T Tokens, the models still did not show any sign of saturation".
- Derivación: 285,7 = 2,0T / 7B y 28,6 = 2,0T / 70B — `corpus/touvron-2023-llama2.pdf.md` (Table 1). Frente a Chinchilla: 285,7 / 20 ≈ 14× y 28,6 / 20 ≈ 1,4×.
- El rango "entre 10 y 100 veces" sale de Llama 3 70B (11×) y Llama 3 8B ("close to 100x") según Villalobos, y de Llama 2 7B (≈ 14×).
- `corpus/villalobos-2024-run-out-of-data.pdf.md` (Key claims): Llama 3 70B a 15T tokens = 214 tokens por parámetro, "11x more than the Chinchilla-optimal ratio"; "Llama 3 8B is overtrained by close to 100x".
- `corpus/hoffmann-2022-chinchilla.pdf.md` (Key claims): "The energy cost of a large language model is amortized through its usage for inference an[d] fine-tuning."
- `corpus/villalobos-2024-run-out-of-data.pdf.md` (Definitions, App. F): el modelo de maximización de beneficio incluye la demanda de inferencia y produce sobreentrenamiento.

### Speaker notes

Chinchilla optimiza el costo de entrenar. Una empresa que sirve el modelo a millones de usuarios optimiza entrenar más servir, y un modelo más chico es más barato en cada consulta. Por eso se entrena de más un modelo chico. La segunda fila sirve de contraste: el Llama 2 grande vio los mismos 2 billones de tokens que el chico y quedó cerca de Chinchilla; el sobreentrenamiento fuerte está en los modelos chicos. El costo: la demanda de tokens crece más rápido que con la regla de Chinchilla. Llama 3 8B está sobreentrenado cerca de 100 veces según Villalobos, por si alguien pregunta por un caso extremo. De acá sale la pregunta de la sección siguiente: de dónde salen 15 billones de tokens. Tiempo objetivo: ~2 min.

### Presenter feedback

---

# 3. De dónde salen los tokens

**Goal of this section:** Seguir el camino de la web al corpus de entrenamiento con un caso documentado (C4), mostrar qué se pierde y qué se sesga en ese camino (dialectos, idiomas, costo por token) y cerrar con el techo: el texto humano público se agota.

**Presenter feedback:**

---

## 1. De Common Crawl a C4

### Content

**Common Crawl archiva la web todos los meses. C4 tomó el crawl de abril de 2019, lo filtró con reglas simples y conservó el 11 % de los tokens en inglés.**

```ascii
+-------------------------------------------------+
| Common Crawl, abril 2019, páginas en inglés     |
| 1.100 M documentos   |   1,4 billones de tokens |
+-------------------------------------------------+
                        |
                        v
+-------------------------------------------------+
| Reglas de limpieza                              |
|  - líneas que terminan en . ! ? o comillas      |
|  - líneas de 5 palabras o más                   |
|  - páginas de 3 oraciones o más                 |
|  - sin "lorem ipsum", sin "{", sin la blocklist |
|  - un solo ejemplar de cada tramo repetido      |
+-------------------------------------------------+
                        |
                        v
+-------------------------------------------------+
| C4.EN                                           |
| 365 M documentos   |   156.000 M de tokens      |
|                (11 % de los tokens)             |
+-------------------------------------------------+
```
<!-- ascii-note:
intent: embudo de limpieza; el volumen cae de 1,4 billones a 156.000 millones de tokens
emphasize: el "11 %" en la caja de salida es el único elemento en acento
labels: documentos (M = millones), tokens
-->

- **Sin los filtros el modelo rinde peor.** En GLUE, un conjunto de tareas de comprensión de texto, T5 pre-entrenado con C4 sin filtrar obtiene 81,46; con C4, 83,28.

### Sources

- `corpus/raffel-2020-t5-c4.pdf.md` (Key claims, §2.2): Common Crawl "produces around 20TB of scraped text data each month"; "the majority of the resulting text is not natural language"; reglas de filtrado (puntuación terminal, ≥ 3 oraciones por página, ≥ 5 palabras por línea, blocklist, "Javascript", "lorem ipsum", "{", deduplicación de tramos de tres oraciones, langdetect ≥ 0,99); crawl de abril de 2019.
- `corpus/dodge-2021-documenting-c4.pdf.md` (Table 1): C4.EN.NOCLEAN 1.100 M documentos, 1,4 billones de tokens; C4.EN 365 M documentos, 156.000 M de tokens.
- Derivación: 11 % = 156.000 M / 1,4 billones = 0,111 — `corpus/dodge-2021-documenting-c4.pdf.md`.
- `corpus/raffel-2020-t5-c4.pdf.md` (Table 8): GLUE 83,28 (C4) vs 81,46 (C4 sin filtrar).
- Conflicto en el corpus: Dodge describe los umbrales invertidos ("fewer than three words", "less than five sentences"); Raffel dice ≥ 5 palabras por línea y ≥ 3 oraciones por página (`corpus/dodge-2021-documenting-c4.pdf.md`, Inconsistencies). La lámina sigue a Raffel, que construyó C4.
- Conflicto en el corpus: la introducción de Dodge dice "365 million domains"; su Table 1 da 365 M documentos. La lámina usa la tabla.

### Speaker notes

Common Crawl es una organización sin fines de lucro que archiva la web; casi todos los corpus abiertos (C4, RefinedWeb, RedPajama) salen de ahí. C4 es el caso que conviene mostrar porque está documentado: Raffel publicó las reglas y Dodge midió el resultado. Las reglas son heurísticas de ingeniero: si la línea no termina en punto, probablemente es un menú; si hay una llave, probablemente es código. Pedí que piensen qué se pierde con "sin {" (todo el código) antes de pasar a la lámina siguiente. El número a retener es el 11 %: de cada nueve tokens en inglés quedó uno. Tiempo objetivo: ~3 min.

### Presenter feedback

---

## 2. Lo que el filtro se lleva y lo que deja

<!-- format: grid -->

### Content

**Las reglas de C4 parecen neutrales. Medidas documento por documento, sacan más de unos grupos que de otros y dejan adentro cosas que nadie buscó.**

- **Dialectos minoritarios.** La blocklist elimina el 42 % de los documentos en inglés afroamericano y el 32 % de los de inglés hispano, frente al 6,2 % del inglés mayoritario.
- **Temas que no son ofensivos.** De los documentos que la blocklist excluye, el 31 % es contenido sexual; el resto incluye ciencia, medicina, salud y textos legales.
- **Sitios sobrerrepresentados.** El sitio con más texto en C4 es patents.google.com, y el 51,3 % de las páginas está alojado en Estados Unidos.
- **Benchmarks filtrados al corpus.** Entre el 1,87 % y el 24,88 % de los textos de referencia de benchmarks de generación aparecen literales en C4.

### Sources

- `corpus/dodge-2021-documenting-c4.pdf.md` (Key claims): remoción por blocklist AAE 42 %, Hispanic-aligned 32 %, WAE 6,2 %, otros 7,2 %; 100.000 documentos excluidos en 50 clusters, 16 de contenido sexual (31 %), el resto ciencia, medicina, salud, legal y política; patents.google.com como sitio más representado; 51,3 % de 175.000 URLs en EE. UU.; contaminación exacta 1,87 %–24,88 % en tests de generación.
- `corpus/dodge-2021-documenting-c4.pdf.md` (Key claims): "We recommend against using blockilst [sic] filtering when constructing datasets from web-crawled data."
- `corpus/dodge-2021-documenting-c4.pdf.md` (Inconsistencies): la geolocalización por IP se confunde con centros de datos y CDN; la lámina da el 51,3 % como "alojado", no como "escrito".

### Speaker notes

La blocklist venía de una lista de palabras pensada para que un buscador no autocompletara groserías. Aplicada a documentos enteros, una sola palabra de la lista saca la página completa, y eso pega más en textos de minorías y en textos sobre orientación sexual escritos con las palabras que usa esa comunidad. Consecuencia para el modelo: rinde peor con textos de y sobre esos grupos. La cuarta tarjeta anticipa la clase de evaluación: si el test está en el corpus, el benchmark mide memoria. Tiempo objetivo: ~3 min.

### Presenter feedback

---

## 3. Casi todo en inglés

<!-- template: stat -->

### Content

**Common Crawl ya está cargado hacia el inglés, y los corpus armados con él lo están todavía más.**

- **Entre 45 % y 46 %.** Páginas de Common Crawl en inglés.
- **89,70 %.** Pre-entrenamiento de Llama 2 en inglés.
- **0,13 %.** Pre-entrenamiento de Llama 2 en español.

### Sources

- `corpus/jun-2023-languages-tokenized.web.md` (Key claims): "English makes up over 46% of the Common Crawl corpus".
- `corpus/villalobos-2024-run-out-of-data.pdf.md` (Key claims): "In Common Crawl, around 45% of webpages is in English"; otras estimaciones del mismo paper dan 58,8 % y "around 20%" para la web en general.
- `corpus/bagerbach-aie-notes.web.md` (Key claims): según estas notas, el libro *AI Engineering* dice "nearly 46%".
- Conflicto en el corpus: 45 % (Villalobos) frente a más de 46 % (Jun); la lámina da el rango. Ninguna fuente fecha el snapshot.
- `corpus/touvron-2023-llama2.pdf.md` (Table 10): en 89,70 %, unknown 8,38 % (en parte código), de 0,17 %, fr 0,16 %, es 0,13 %; "the model may not be suitable for use in other languages".

### Speaker notes

Dos números para mirar juntos: cerca de la mitad de Common Crawl es inglés, pero en Llama 2 el inglés es casi el 90 % y el español una parte en mil. Llama 2 no publica su mezcla de fuentes, así que la lámina no puede decir en qué paso se perdió el resto. Las notas de *AI Engineering* agregan un dato cualitativo: los idiomas con peor MMLU (telugu, marathi, panyabí) están entre los menos representados en Common Crawl. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 4. El español paga más tokens

### Content

**El mismo texto traducido ocupa más tokens fuera del inglés. Con el tokenizer de GPT-4, una frase en español usa 1,55 veces los tokens de su versión en inglés.**

| Idioma | Tokens por cada token en inglés (cl100k_base) |
|---|---|
| Inglés | 1,00 |
| Portugués | 1,48 |
| Español | 1,55 |
| Francés | 1,60 |
| Chino simplificado | 1,91 |
| Árabe estándar | 3,04 |
| Birmano | 11,70 |
| Shan | 15,05 |

- **Tres consecuencias.** Más costo con precios por token, más latencia y menos texto útil en la misma ventana de contexto.
- **Tres orígenes.** Una buena parte viene del corpus del tokenizer, dominado por el inglés: sus unidades más frecuentes son fragmentos del inglés. Petrov señala además la escritura (cuántos bytes ocupa cada carácter) y la familia del idioma.

### Sources

- `corpus/petrov-2023-tokenizer-unfairness.pdf.md` (Table 1, columna ChatGPT/GPT-4 = cl100k_base): Portugués 1,48; Español 1,55; Francés 1,60; Chino simplificado 1,91; Árabe estándar 3,04; Birmano 11,70; Shan 15,05. La tabla fue reconstruida de una extracción aplanada y cotejada con la prosa (Inconsistencies).
- `corpus/petrov-2023-tokenizer-unfairness.pdf.md` (Key claims): costo, latencia y contexto como las tres consecuencias; los vocabularios reflejan "the biases of the corpus source"; dos fuentes de disparidad a nivel de bytes y caracteres ("natural differences in number of characters per content, and UTF-8 using 1–3+ bytes depending on script"); idiomas de familias grandes comparten tokens (ejemplo "hotel"). El paper no ordena las causas por peso; como remedio pide un corpus paralelo balanceado y un método de construcción del vocabulario, no solo balancear los datos.
- `corpus/jun-2023-languages-tokenized.web.md` (Key claims): con cl100k_base, mediana de 7 tokens en inglés y 72 en birmano sobre el dataset MASSIVE; "Romance languages such as Spanish, French, and Portuguese tended to result in a similar number of tokens as English". Mide mensajes cortos de asistente de voz, no texto largo.

### Speaker notes

La pregunta que conviene hacerle a la clase: ¿el español cuesta más por el idioma o por los datos? En buena parte por los datos con que se entrenó el tokenizer, aunque Petrov no dice qué proporción explica cada causa. BPE arma el vocabulario con los fragmentos más frecuentes del corpus con que se entrena el tokenizer; si el corpus es casi todo inglés, "the" es un token y muchas palabras del español se parten en dos o tres. Petrov lo muestra con tokenizers entrenados para el alemán o el francés: también favorecen al inglés, porque hay mucho inglés mezclado en la web de esos idiomas. El 1,55 es sobre FLORES-200, frases de Wikipedia traducidas. Jun, con mensajes cortos de asistente, ve el español casi igual al inglés; la diferencia depende del tipo de texto. Si alguien pregunta por tokenizers más nuevos, el corpus no tiene mediciones posteriores a 2023; no afirmes que la brecha se cerró. Tiempo objetivo: ~3 min.

### Presenter feedback

---

## 5. El texto humano público tiene un techo

<!-- design: split-right -->

### Content

**Los datasets de entrenamiento crecen unas 2,4 veces por año. El texto humano público disponible no crece a ese ritmo, y las dos curvas se cruzan hacia 2028.**

- **Stock efectivo.** Unos 4 × 10¹⁴ tokens de texto público indexado, ya descontada la calidad y contando hasta 5 pasadas por el mismo texto.
- **Fecha de cruce.** Mediana en 2028, con un rango de 2026 a 2032. Un año antes si los modelos se sobreentrenan 5 veces.

![Proyección del tamaño de los datasets de entrenamiento frente al stock de texto humano público, 2020-2034, con GPT-3, FLAN, PaLM, Falcon-180B, DBRX y Llama 3 marcados](research/corpus/Data.pdf/images/p002-fig-2-9-data-stock-projection.png)

### Sources

- `corpus/villalobos-2024-run-out-of-data.pdf.md` (Key claims): crecimiento de 0,38 órdenes de magnitud por año ("~2.4x per year"); mediana 2028, rango 2026–2032; stock "around 4e14 tokens"; 5× de sobreentrenamiento adelanta el cruce "one year earlier".
- Derivación: 2,4 = 10^0,38 — `corpus/villalobos-2024-run-out-of-data.pdf.md`.
- `corpus/villalobos-2024-run-out-of-data.pdf.md` (Key claims, Fig. 3): stock deduplicado 510T → ajustado por calidad 100T → ajustado por repetición (tope de 5 épocas) 320T.
- Conflicto en el corpus: el stock al momento del cruce figura como ~4e14 (Figs. 1 y 5) y como 320T (Fig. 3); la diferencia puede ser el crecimiento del stock hasta 2028, que el paper no explica (Inconsistencies). La lámina usa el valor de la figura mostrada.
- `corpus/Data.pdf.md` (imagen p002): foto de la Fig. 2-9 de *AI Engineering*, que reproduce la Fig. 1 de Villalobos et al. 2024.
- Notas: `corpus/longpre-2024-consent-in-crisis.pdf.md` (Key claims: "~5%+ of all tokens in C4 … fully restricted"); `corpus/shumailov-2023-curse-of-recursion.pdf.md` (Key claims: "tails of the original content distribution disappear"); `corpus/villalobos-2024-run-out-of-data.pdf.md` (datos sintéticos "in domains where model outputs are relatively easy to verify").

### Speaker notes

La figura se lee así: la franja verde es el stock de texto, con su incertidumbre; la curva azul es el tamaño de los datasets de los modelos notables, proyectada. Las verticales marcan el cruce. Aclará que es una proyección publicada en 2024: el paper dice que el paradigma de texto humano público no llega a la próxima década y también que lo más probable es que se encuentre la forma de seguir. Pagar personas para escribir no alcanza: 10 millones de personas escribiendo 8 horas por día producirían unos 70 billones de palabras por año, el mismo orden que Common Crawl, por cientos de miles de millones de dólares. Si hay tiempo, dos presiones más cerca del techo (el detalle está en Cut material): entre 2023 y 2024 robots.txt pasó a bloquear más del 5 % de los tokens de C4 (Longpre et al. 2024), y el texto generado por modelos, reciclado generación tras generación, borra las colas de la distribución (Shumailov et al.). Los datos sintéticos rinden donde la salida se puede verificar, como matemática y código; ese es el puente a la lámina 5.3. Tiempo objetivo: ~3 min.

### Presenter feedback

---

# 4. Post-entrenamiento

**Goal of this section:** Explicar las dos formas de post-entrenamiento con sus datos y sus pérdidas: imitar demostraciones (SFT) y aprender de comparaciones (RLHF y DPO). Cerrar con lo que ese entrenamiento cambia en el modelo y lo que deja igual.

**Presenter feedback:**

---

## 1. SFT: imitar una demostración

### Content

**El SFT sigue entrenando el modelo base con la misma pérdida del pre-entrenamiento, sobre pares (prompt, respuesta) escritos por personas. La pérdida se cuenta solo en los tokens de la respuesta.**

```text
prompt     Write a poem to help me remember the first 10 elements on the
           periodic table, giving each element its own line.

respuesta  Hydrogen comes first as element number one.
           Helium is second for balloons to have fun!
           In third place is Lithium to hold battery charge,
           [...]
```

- **Una fila del dataset de SFT de Llama 2.** La escribió un anotador contratado; el modelo aprende a producir respuestas con esa forma para prompts con esta forma.
- **Clonar una conducta.** OpenAI llama a este paso *behavior cloning*: la persona muestra cómo responder y el modelo copia ese comportamiento.

### Sources

- `corpus/touvron-2023-llama2.pdf.md` (Table 5): ejemplo de anotación de SFT (helpfulness), verbatim, recortado a las tres primeras líneas de la respuesta.
- `corpus/touvron-2023-llama2.pdf.md` (Definitions): prompt y respuesta concatenados, token especial separador, "zero-out the loss on tokens from the user prompt"; 2 épocas.
- `corpus/huyen-2023-rlhf.web.md` (Key claims, Definitions): SFT = *behavior cloning*; "only the tokens in the response are counted towards the loss".

### Speaker notes

Lo importante es que no hay algoritmo nuevo: es el mismo entrenamiento de la clase 8 con otros datos. El cambio que conviene subrayar es poner la pérdida en cero sobre el prompt: el modelo no aprende a escribir preguntas de usuario, solo respuestas. Volvé al ejemplo de la apertura: GPT-3 escribía más consignas porque nunca había visto el par consigna-respuesta como tal. Tiempo objetivo: ~3 min.

### Presenter feedback

---

## 2. Pocos ejemplos, bien escritos

<!-- template: stat -->

### Content

**Las demostraciones se cuentan en decenas de miles, y la calidad pesa más que la cantidad.**

- **Unos 13.000 prompts.** SFT de InstructGPT, con respuestas de unos 40 anotadores seleccionados por examen.
- **27.540 anotaciones.** SFT de Llama 2. Meta dejó de lado millones de ejemplos de datasets de terceros porque rendían peor.
- **9.209 ejemplos.** OASST1 superó a un subconjunto de 450.000 ejemplos de FLAN v2 como dato de fine-tuning para chat.

### Sources

- `corpus/ouyang-2022-instructgpt.pdf.md` (Key claims, §3.2): "The SFT dataset contains about 13k training prompts"; Table 6: 11.295 de anotadores + 1.430 de clientes = 12.725; ~40 contratistas con examen de selección.
- `corpus/touvron-2023-llama2.pdf.md` (Key claims): "By setting aside millions of examples from third-party datasets and using fewer but higher-quality examples from our own vendor-based annotation efforts, our results notably improved"; "We stopped annotating SFT after collecting a total of 27,540 annotations."
- `corpus/dettmers-2023-qlora.pdf.md` (Key claims, App. B.1): "a 9k sample dataset (OASST1) outperformed a 450k sample dataset (FLAN v2, subsampled) on chatbot performance"; OASST1 filtrado a 9.209 ejemplos.
- `corpus/huyen-2023-rlhf.web.md` (Key claims): unos 90 % de los anotadores de InstructGPT con título universitario y más de un tercio con maestría.

### Speaker notes

Con 13.000 ejemplos se cambia la conducta de un modelo que vio 300.000 millones de tokens; eso refuerza la lectura de la lámina 1.3: el post-entrenamiento desbloquea algo que el modelo base ya sabía. Llama 2 agrega un dato de proceso: las muestras que generaba su propio modelo SFT competían con las escritas por anotadores, y por eso movieron el esfuerzo de anotación hacia comparaciones. Es el paso a la lámina siguiente. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 3. Comparar es más fácil que escribir

<!-- format: row -->

### Content

**Una demostración muestra una respuesta buena y nada más. Una comparación entre dos respuestas dice cuál es mejor, cuesta menos y no depende de que el anotador sepa escribir la mejor respuesta.**

- **Techo del anotador.** Con SFT, el modelo queda limitado por lo que escriben los mejores anotadores. Juzgar una respuesta ajena no tiene ese techo.
- **Juicio relativo.** Puntuar una respuesta en abstracto da notas inconsistentes entre personas. Elegir la mejor de dos es más estable y más rápido.
- **Acuerdo parcial.** En InstructGPT, dos anotadores coinciden en el 72,6 % de las comparaciones.

### Sources

- `corpus/touvron-2023-llama2.pdf.md` (Key claims, "Beyond Human Supervision"): "the model's performance is capped by the writing abilities of the most skilled annotators"; "while we may not all be accomplished artists, our ability to appreciate and critique art remains intact".
- `corpus/rafailov-2023-dpo.pdf.md` (Key claims): relative judgments "are often easier to collect than expert demonstrations".
- `corpus/huyen-2023-rlhf.web.md` (Key claims): el puntaje absoluto es inconsistente entre anotadores; "It's a lot easier to ask labelers to compare two responses".
- `corpus/ouyang-2022-instructgpt.pdf.md` (Key claims): acuerdo entre anotadores 72,6 ± 1,5 %.

### Speaker notes

La analogía de Llama 2 funciona bien en voz alta: no hace falta ser pintor para decir cuál de dos cuadros es mejor. El 72,6 % es un recordatorio de que la señal es ruidosa: en más de una comparación de cada cuatro, otra persona habría elegido la otra respuesta. Huyen trae un ejemplo del dataset público de Anthropic donde ella prefiere la respuesta marcada como perdedora; sirve si hay tiempo. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 4. RLHF: puntuar y maximizar el puntaje

<!-- design: banded -->

### Content

**Las comparaciones entrenan un modelo de recompensa. Después, el modelo de lenguaje genera respuestas, el de recompensa las puntúa y el aprendizaje por refuerzo sube la probabilidad de las mejor puntuadas.**

![Los tres pasos de InstructGPT: SFT con demostraciones, modelo de recompensa entrenado con rankings de respuestas, y optimización de la política con PPO contra ese modelo](research/corpus/ouyang-2022-instructgpt.pdf/images/fig-02-p003.png)

- **Modelo de recompensa.** Es el modelo SFT con una salida escalar en lugar del vocabulario. Se entrena para que la respuesta preferida puntúe más: pérdida −log σ(r_ganadora − r_perdedora).
- **Penalización por alejarse.** PPO (Proximal Policy Optimization), un algoritmo de aprendizaje por refuerzo, maximiza el puntaje menos una penalización que crece cuanto más se aleja el modelo del SFT (la divergencia KL entre sus distribuciones). Sin ese término, el modelo encuentra respuestas que engañan al modelo de recompensa.

### Sources

- `corpus/ouyang-2022-instructgpt.pdf.md` (Fig. 2, Definitions): los tres pasos; RM = modelo SFT "with the final unembedding layer removed", pérdida −E[log σ(r(x, y_w) − r(x, y_l))]; PPO con "a per-token KL penalty from the SFT model … to mitigate over-optimization of the reward model"; β = 0,02.
- `corpus/huyen-2023-rlhf.web.md` (Definitions): RM y objetivo RLHF; el término KL evita que el modelo se aleje del SFT porque el RM puede dar puntajes erróneos a pares nunca vistos.
- `corpus/touvron-2023-llama2.pdf.md` (Definitions): *reward hacking*, "taking advantage of some weaknesses of our reward, and so artificially inflating the score"; 1.418.091 comparaciones propias de Meta.

### Speaker notes

Recorré la figura en tres columnas. En el paso 2 marcá que los anotadores ordenan de 4 a 9 respuestas, y cada orden produce todas las comparaciones de a pares. La fórmula de la pérdida es la sigmoide de la diferencia de puntajes: si la ganadora puntúa mucho más, la pérdida es casi cero. En el paso 3, el aprendizaje por refuerzo aparece porque el puntaje llega al final de la respuesta completa y no es derivable respecto de los tokens elegidos. La penalización por alejarse se entiende con reward hacking: el modelo de recompensa es otra red con errores, y si se lo maximiza sin freno el modelo encuentra esos errores. Escala de referencia: Meta juntó 1,4 millones de comparaciones propias para Llama 2. Tiempo objetivo: ~4 min.

### Presenter feedback

---

## 5. DPO: la misma meta sin refuerzo

<!-- design: banded -->

### Content

**DPO optimiza el mismo objetivo que RLHF directamente sobre los pares de preferencia, con una pérdida de clasificación. No entrena un modelo de recompensa aparte ni genera respuestas durante el entrenamiento.**

![Comparación de RLHF, con modelo de recompensa y ciclo de muestreo con RL, y DPO, que pasa de los datos de preferencia al modelo final por máxima verosimilitud](research/corpus/rafailov-2023-dpo.pdf/images/fig-01-p002.png)

- **La pérdida.** Sube la probabilidad relativa de la respuesta preferida frente a la rechazada, medida contra el modelo de referencia (el SFT). Son tres líneas de PyTorch.
- **Evidencia y alcance.** En resúmenes de Reddit, 61 % de victorias contra las referencias humanas frente a 57 % de PPO. Los experimentos llegan a 6B de parámetros.

### Sources

- `corpus/rafailov-2023-dpo.pdf.md` (Key claims, Fig. 1): "solve the standard RLHF problem with only a simple classification loss"; "eliminating the need for sampling from the LM during fine-tuning"; DPO optimiza el mismo objetivo con restricción de KL.
- `corpus/rafailov-2023-dpo.pdf.md` (Definitions): L_DPO = −E log σ(β log(πθ(y_w|x)/π_ref(y_w|x)) − β log(πθ(y_l|x)/π_ref(y_l|x))).
- `corpus/rafailov-2023-dpo.pdf.md` (Evidence, App. B): código `pi_logratios = pi_yw_logps - pi_yl_logps`; `ref_logratios = ref_yw_logps - ref_yl_logps`; `losses = -F.logsigmoid(beta * (pi_logratios - ref_logratios))`.
- `corpus/rafailov-2023-dpo.pdf.md` (Key claims): TL;DR, DPO ≈ 61 % a temperatura 0 frente a PPO 57 %, juzgado por GPT-4; modelos "up to 6B parameters".

### Speaker notes

Si el grupo viene fuerte en matemática, la idea en una frase: la política óptima de RLHF tiene forma cerrada en función de la recompensa, así que se puede despejar la recompensa en función de la política y entrenar la política directo con la pérdida del modelo de recompensa. Mostrá las tres líneas de código (están en Sources): la diferencia de log-probabilidades entre preferida y rechazada, menos la misma diferencia en el modelo de referencia, dentro de una log-sigmoide. Aclará el límite: el paper prueba hasta 6B y usa a GPT-4 como juez; no dice qué usan hoy los laboratorios grandes. Llama 2 usó PPO y rejection sampling; DeepSeek-R1 y Qwen3 usan GRPO, que aparece en la sección 5. Tiempo objetivo: ~3 min.

### Presenter feedback

---

## 6. Qué cambia y qué no

<!-- template: comparison -->

### Content

**El post-entrenamiento cambia cómo responde el modelo. Lo que el modelo sabe y lo que aprendió del corpus quedan casi iguales.**

- **Lo que mejora.** Los evaluadores prefieren InstructGPT de 1,3B a GPT-3 de 175B. En tareas donde la respuesta tiene que salir del texto dado, InstructGPT inventa información en el 21 % de los casos y GPT-3 en el 41 %.
- **Lo que no se mueve o empeora.** Los sesgos medidos en Winogender y CrowS-Pairs no mejoran. Si se le pide un texto tóxico, produce uno más tóxico que el de GPT-3. Pierde rendimiento en SQuAD, DROP, HellaSwag y traducción.

### Sources

- `corpus/ouyang-2022-instructgpt.pdf.md` (Key claims): "outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3"; "a 21% vs. 41% hallucination rate" en tareas de dominio cerrado; sin mejora significativa en Winogender y CrowS-Pairs; "when explicitly prompted to produce a toxic output, InstructGPT outputs are much more toxic than those from GPT-3"; *alignment tax* en SQuAD, DROP, HellaSwag y WMT 2015 Fr→En.
- `corpus/ouyang-2022-instructgpt.pdf.md` (Key claims): el procedimiento alinea el modelo "to the stated preferences of a specific group of people (mostly our labelers and researchers), rather than any broader notion of 'human values'".
- `corpus/huyen-2023-rlhf.web.md` (Key claims): SFT y RLHF desbloquean "the capabilities that the pretrained model already has but are hard for users to access via prompting alone".
- `corpus/huyen-2023-rlhf.web.md` (Key claims): "the InstructGPT paper shows that RLHF actually made hallucination worse" (frente al modelo solo con SFT). Compatible con el 21 % vs 41 %, que compara contra GPT-3.

### Speaker notes

Lectura para la clase: el post-entrenamiento es barato y cambia mucho la conducta, pero no borra lo que vino del corpus de la sección 3. Los sesgos siguen; el modelo sigue sabiendo escribir texto tóxico y lo hace mejor cuando se lo piden, porque aprendió a seguir instrucciones. La pregunta de Huyen sirve para abrir la sección siguiente. Hay tres modelos en juego: GPT-3 (solo pre-entrenado), el modelo SFT y InstructGPT (SFT más RLHF con PPO). InstructGPT inventa la mitad que GPT-3, pero inventa más que el modelo SFT. Ninguna de las dos etapas premió decir "no sé". El paper también lo dice: el modelo se alinea con las preferencias de unas 40 personas y de los autores, no con valores humanos en general. Tiempo objetivo: ~3 min.

### Presenter feedback

---

# 5. Conductas premiadas

**Goal of this section:** Aplicar la misma lectura (qué dato y qué señal premió la conducta) a cuatro conductas que los alumnos ven en un asistente: usar herramientas, razonar, pensar o no pensar según el pedido, e inventar datos, con la corrección que se propone para lo último.

**Presenter feedback:**

---

## 1. Una herramienta es texto con formato

<!-- design: banded -->

### Content

**El modelo llama a una herramienta generando tokens con un formato acordado. Un programa externo ejecuta la llamada, pega el resultado en la secuencia y el modelo sigue generando.**

![Generación intercalada: el modelo escribe tokens, emite una llamada a código, un ejecutor externo inserta la salida y el modelo continúa con la respuesta](research/corpus/lambert-rlhfbook-tool-use.web/images/tool_use_generation.png)

- **Los datos de entrenamiento.** Son datos de post-entrenamiento comunes con un agregado: un system prompt que lista las herramientas disponibles y sus esquemas.
- **La pérdida.** Los tokens de salida de la herramienta se enmascaran. El modelo aprende cuándo llamar y con qué argumentos, no a adivinar el resultado.

### Sources

- `corpus/lambert-rlhfbook-tool-use.web.md` (Fig. 1, Key claims): "the language model is interleaving tool inputs and outputs with standard autoregressively generated tokens"; "Training data for function calling looks much like other post-training data, with one addition: a system prompt that instructs the model what tools it has available"; salidas de herramienta "masked from the model's training loss".
- `corpus/lambert-rlhfbook-tool-use.web.md` (Key claims): entrenar tool use es lograr que el modelo sepa "when to emit a tool call, how to format arguments correctly, and how to incorporate results into its response".
- `corpus/openai-2025-gpt-oss-model-card.pdf.md` (Key claims): las herramientas de gpt-oss también se activan desde el system prompt ("trained to support running with and without these tools").

### Speaker notes

Enganchá con la clase de RAG y MCP: allá vieron el lado del orquestador (el loop que recibe la llamada, ejecuta y devuelve). Acá está el lado del modelo: un modelo base no conoce el formato de llamada de cada proveedor, y los modelos abiertos se entrenan para trabajar con herramientas variadas. Un modelo de chat puede usar una herramienta simple sin entrenamiento específico (Llama 2-Chat con una calculadora, en las notas de la lámina siguiente), pero el formato y la decisión de cuándo llamar se aprenden en el post-entrenamiento. MCP estandarizó cómo se describen las herramientas; el modelo igual tiene que haber visto ejemplos de llamadas en su post-entrenamiento para usarlas bien. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 2. Tres señales para herramientas

<!-- format: list -->

### Content

**Las tres formas usan señales distintas: la pérdida del propio modelo, el juicio de personas y el éxito de la tarea.**

- **Autoetiquetado.** El modelo inserta llamadas candidatas en texto común y se conservan solo las que bajan la pérdida de los tokens que siguen. Con ese método, Toolformer (GPT-J de 6,7B) saca 40,4 en ASDiv usando una calculadora; GPT-3 de 175B saca 14,0.
- **Demostraciones y selección por recompensa.** Personas resuelven la tarea con comandos de texto (Search, Click, Quote) y el modelo las imita con SFT; con sus comparaciones se entrena un modelo de recompensa que, al responder, elige la mejor de 64 respuestas. WebGPT usó 6.209 demostraciones y 21.548 comparaciones; esa versión fue preferida el 56 % de las veces sobre los propios demostradores.
- **Refuerzo sobre la trayectoria completa.** En tareas de varios pasos, el agente llama herramientas a lo largo de toda la trayectoria y recibe una sola recompensa al final, según si completó la tarea.

### Sources

- `corpus/schick-2023-toolformer.pdf.md` (Key claims, Definitions): filtro L_i− − L_i+ ≥ τ_f (se conserva la llamada si baja la pérdida de los tokens siguientes); GPT-J 6,7B; Table 4: ASDiv Toolformer 40,4, GPT-3 (175B) 14,0; la capacidad aparece recién cerca de 775M parámetros.
- `corpus/nakano-2021-webgpt.pdf.md` (Table 1, Table 4, Key claims): comandos Search, Clicked on link, Quote, etc.; 6.209 demostraciones y 21.548 comparaciones; mejor modelo = behavior cloning + rejection sampling (best-of-n) contra el modelo de recompensa, "preferred by humans 56% of the time to those of our human demonstrators"; 175B best-of-64 preferido 68 % sobre BC y 175B RL 58 % sobre BC; rejection sampling "requires no additional training, but instead uses more inference-time compute". La sección 3.1 del paper redondea a "around 6,000" (Inconsistencies); la lámina usa la tabla.
- `corpus/touvron-2023-llama2.pdf.md` (Key claims, Table 15): "tool usage can spontaneously emerge from alignment in a zero-shot manner"; con calculadora, Llama 2-Chat ASDiv 67,1 frente a Toolformer 40,4, sin entrenamiento explícito de herramientas.
- `corpus/lambert-rlhfbook-tool-use.web.md` (Fig. 2, Key claims): RL multi-paso con recompensa terminal r_T "after a multi-step rollout – closer to classic RL"; SFT para formato, DPO para decidir cuándo llamar, RL con feedback del entorno para tareas agénticas.

### Speaker notes

Las tres tarjetas son tres respuestas a la pregunta de quién decide que una llamada fue buena. En Toolformer lo decide el propio modelo: una llamada sirve si hace más fácil predecir el texto que sigue. Es barato y no necesita anotadores, pero es ineficiente (un millón de documentos dan unos pocos miles de llamadas útiles a la calculadora). En WebGPT deciden personas, en dos momentos: sus demostraciones entrenan al modelo con SFT, y sus comparaciones entrenan un modelo de recompensa que se usa al responder, para elegir la mejor de 64 salidas. Ese paso no entrena más al modelo. WebGPT también probó RL con PPO y rindió menos: preferido 58 % sobre el modelo SFT, contra 68 % de la selección entre 64. La tercera es lo que se usa para agentes de varios pasos, y se parece más al RL clásico de juegos porque la recompensa llega al final. Dato para quien pregunte: Llama 2-Chat usó una calculadora sin haber sido entrenado explícitamente para eso y superó a Toolformer (67,1 frente a 40,4 en ASDiv). Tiempo objetivo: ~3 min.

### Presenter feedback

---

## 3. Razonar se premia con un verificador

<!-- design: banded -->

### Content

**DeepSeek-R1-Zero se entrenó con RL desde el modelo base, sin ejemplos de razonamiento escritos por personas. La recompensa solo revisaba si la respuesta final era correcta y si el razonamiento estaba entre etiquetas `<think>`.**

![DeepSeek-R1-Zero durante el RL: la precisión en AIME sube por encima del promedio humano y la longitud promedio de las respuestas crece de unos cientos a más de 10.000 tokens](research/corpus/deepseek-2025-r1.pdf/images/fig-01-p004.png)

- **Resultado.** En AIME 2024, una competencia de matemática con respuesta numérica, el acierto en el primer intento (pass@1) pasó de 15,6 % a 77,9 %, y las respuestas se alargaron solas: el modelo aprendió a verificar y a revisar pasos.
- **GRPO.** Para cada problema se generan 16 respuestas; cada una se premia según cuánto supera el promedio de su grupo. No hace falta un modelo de valor aparte.

### Sources

- `corpus/deepseek-2025-r1.pdf.md` (Key claims, Fig. 1): R1-Zero desde DeepSeek-V3-Base con GRPO, "without imposing constraints on the reasoning process itself"; recompensa = exactitud + formato (`<think>…</think>`); AIME 2024 pass@1 "from an initial 15.6% to 77.9%"; respuestas cada vez más largas con verificación y reflexión.
- `corpus/deepseek-2025-r1.pdf.md` (Definitions, Evidence): ventaja A_i = (r_i − media) / desvío del grupo; 16 salidas por pregunta; GRPO "foregoes the value model".
- `corpus/deepseek-2025-r1.pdf.md` (Key claims): no usan modelos de recompensa neuronales para razonamiento porque "are susceptible to reward hacking"; R1 final agrega SFT de arranque, ~800.000 ejemplos de SFT y una etapa de preferencias.
- `corpus/deepseek-2025-r1.pdf.md` (Inconsistencies): los autores advierten que los patrones "en primera persona" reflejan heurísticas de DeepSeek y no inteligencia humana; el "pure RL" vale solo para R1-Zero.

### Speaker notes

Esta lámina conecta con las notas de la 3.5: donde la salida se puede verificar, un programa reemplaza al anotador. Para matemática alcanza comparar el número final; para código, correr los tests. La curva de la derecha es la que conviene señalar: nadie le pidió al modelo que pensara más, y la longitud creció porque pensar más daba más recompensa. Hay un límite que decir en voz alta: el método necesita un verificador confiable, y fuera de matemática y código no lo hay. Por eso R1 final vuelve a usar SFT y preferencias. Costo del post-entrenamiento de R1, para escala: 147.000 horas de GPU H800, unos 294.000 dólares, sin contar el pre-entrenamiento del modelo base. Tiempo objetivo: ~3 min.

### Presenter feedback

---

## 4. Pensar o no pensar es un modo entrenado

<!-- design: split-right -->

### Content

**Qwen3 entrena un solo modelo para responder pensando o sin pensar, según una marca en el prompt. El tope de tokens de pensamiento se aplica al generar: el sistema corta el razonamiento al llegar al límite.**

- **Interruptor entrenado.** El SFT mezcla ejemplos con `/think`, que traen el razonamiento, y con `/no_think`, que traen un bloque `<think></think>` vacío. Después, el RL premia respetar la marca.
- **Tope al generar.** Al llegar al límite se inserta una frase de cierre y `</think>`, y el modelo responde con lo que pensó hasta ahí. Según el paper, esa capacidad aparece sin entrenarla.

![Qwen3-235B-A22B: acierto en AIME'24, AIME'25, LiveCodeBench y GPQA según el tope de tokens de pensamiento, de 1K a 32K, frente al modo sin pensamiento](research/corpus/qwen-2025-qwen3-technical-report.pdf/images/fig-02-p020.png)

### Sources

- `corpus/qwen-2025-qwen3-technical-report.pdf.md` (§4.3, Key claims, Definitions): flags `/think` y `/no_think` en el prompt; "For non-thinking mode samples, we retain an empty thinking block"; RL de Stage 4 con recompensa de *format following* sobre las flags; el tope se aplica cortando e insertando "Considering the limited time by the user, I have to give the solution based on the thinking directly now.\n</think>"; "this ability is not explicitly trained but emerges naturally".
- `corpus/qwen-2025-qwen3-technical-report.pdf.md` (Inconsistencies): el texto dice "in the user query or system message, respectively", pero la Table 9 muestra las dos flags en la consulta del usuario; la lámina sigue a la tabla.
- `corpus/qwen-2025-qwen3-technical-report.pdf.md` (Fig. 2): pass@1 de Qwen3-235B-A22B entre 1K y 32K tokens de pensamiento.
- Notas: `corpus/openai-2025-gpt-oss-model-card.pdf.md` (§2.5.2, Table 3): "We train the models to support three reasoning levels: low, medium, and high … configured in the system prompt"; sin descripción del mecanismo (Inconsistencies, open question); AIME 2025 sin herramientas, 120b: 50,4 / 80,0 / 92,5; 20b Tau-Bench Airline 42,6 (medium) → 38,0 (high).

### Speaker notes

Lo que Qwen3 entrena es el interruptor: ejemplos de SFT de los dos modos y una recompensa por respetar la marca. El tope intermedio es un corte al generar, que el paper describe como no entrenado; funciona porque el modelo ya sabe responder con y sin razonamiento. En la figura, la línea roja es el modo sin pensamiento y la azul crece con el tope; en matemática la subida fuerte está entre 2K y 16K tokens. Si preguntan por los niveles low, medium y high de otros modelos: gpt-oss los configura en el system prompt, pero OpenAI no publicó cómo los entrena; lo único medido es el efecto (en AIME 2025 sin herramientas, gpt-oss-120b pasa de 50,4 % a 80,0 % y a 92,5 %). Más esfuerzo no mejora todo: en gpt-oss-20b, Tau-Bench Airline baja de 42,6 en medium a 38,0 en high. Tiempo objetivo: ~3 min.

### Presenter feedback

---

## 5. Inventar suma puntos en un examen

<!-- format: row -->

### Content

**Con corrección binaria, una respuesta cualquiera tiene más valor esperado que decir "no sé". El pre-entrenamiento produce errores sobre datos raros, y la evaluación premia adivinar en lugar de abstenerse.**

- **Síntoma.** Consultado tres veces por el cumpleaños de uno de los autores del paper, DeepSeek-V3 dio tres fechas distintas, todas falsas, aunque la consigna pedía responder solo si lo sabía.
- **Origen en el pre-entrenamiento.** Un dato que aparece una sola vez en el corpus no tiene patrón del que aprender. La tasa de alucinación del modelo base es como mínimo la fracción de datos que aparecen una sola vez.
- **Refuerzo en la evaluación.** Nueve de diez benchmarks influyentes califican 1 o 0 y no dan crédito por "no sé". Un modelo que adivina supera en esas tablas a uno que admite dudas.

### Sources

- `corpus/kalai-2025-why-lms-hallucinate.pdf.md` (Key claims, Evidence): "language models hallucinate because the training and evaluation procedures reward guessing over acknowledging uncertainty"; DeepSeek-V3 respondió "03-07", "15-06" y "01-01" a "What is Adam Tauman Kalai's birthday? If you know, just respond with DD-MM."
- `corpus/kalai-2025-why-lms-hallucinate.pdf.md` (Key claims, Definitions): cota por *singleton rate*: "if 20% of birthday facts appear exactly once in the pretraining data, then one expects base models to hallucinate on at least 20% of birthday facts".
- `corpus/kalai-2025-why-lms-hallucinate.pdf.md` (Table 2): de 10 benchmarks (GPQA, MMLU-Pro, IFEval, Omni-MATH, WildBench, BBH, MATH L5, MuSR, SWE-bench, HLE), 9 binarios sin crédito por IDK; WildBench da crédito parcial.
- `corpus/kalai-2025-why-lms-hallucinate.pdf.md` (Key claims): "Under binary grading, abstaining is strictly sub-optimal"; comparación Modelo A (señala dudas) vs Modelo B (siempre adivina).
- Notas: `corpus/kalai-2025-why-lms-hallucinate.pdf.md` (Key claims, Evidence): consigna verbatim "Answer only if you are > t confident, since mistakes are penalized t/(1 − t) points, while correct answers receive 1 point, and an answer of 'I don't know' receives 0 points"; responder supera a IDK "iff its confidence … is > t"; precedentes JEE, NEET, GATE, AMC; modificar "the scoring of existing benchmarks that are misaligned but dominate leaderboards, rather than introducing additional hallucination evaluations".
- Derivación (notas): penalización 1 = 0,5 / 0,5 y 9 = 0,9 / 0,1; valor esperado −0,4 = 0,3 × 1 − 0,7 × 1 — `corpus/kalai-2025-why-lms-hallucinate.pdf.md`. El paper da "t = 0.75 (penalty 2)", pero su fórmula da 3; las notas omiten ese caso (ver Open questions).
- Notas: `corpus/huyen-2023-rlhf.web.md` (Key claims): mitigación a nivel de prompt, "if you're unsure of the answer, say 'Sorry, I don't know'".

### Speaker notes

La analogía del paper es el examen de opción múltiple sin penalización: si no sabés, marcás cualquiera, porque en blanco es cero seguro. La segunda tarjeta explica por qué el modelo base se equivoca justo en datos raros: el cumpleaños de Einstein aparece miles de veces y el de un investigador aparece una vez o ninguna, y no hay regla general de la que deducirlo. La tercera explica por qué el post-entrenamiento no lo arregla: los laboratorios optimizan para las tablas de benchmarks, y esas tablas premian adivinar. Volvé a la lámina 4.6: ninguna etapa premió decir "no sé". Un número de contexto si hace falta: en SimpleQA, gpt-oss-120b acierta el 16,8 % de las preguntas y su tasa de alucinación es 78,2 % (Table 9 del model card, `corpus/openai-2025-gpt-oss-model-card.pdf.md`).

La corrección que propone el paper, para cerrar: declarar en la consigna un umbral de confianza t. Un acierto vale 1, "no sé" vale 0 y un error resta t / (1 − t); con t = 0,5 el error resta 1, con t = 0,9 resta 9, y t = 0 es la corrección binaria de hoy. Responder conviene solo si la confianza supera t. Hacé la cuenta con un caso: umbral 0,5 y un modelo con 30 % de confianza. Si responde, el valor esperado es 0,3 × 1 − 0,7 × 1 = −0,4; si dice "no sé", 0. Con corrección binaria el mismo modelo gana 0,3 respondiendo, así que responde. Los autores piden aplicarlo a los benchmarks que ya dominan las tablas, y citan exámenes de ingreso que ya penalizan el error (JEE en India, AMC en Estados Unidos). Es una propuesta de 2025 sin prueba empírica en el paper. Enganche con la clase de prompting: pedir en el system prompt que diga "no sé" si no está seguro es la versión de usuario de la misma idea; ayuda, pero no cambia lo que el entrenamiento premió. Tiempo objetivo: ~4 min.

### Presenter feedback

---

# 6. Ajustar un modelo

**Goal of this section:** Bajar la clase a lo que un equipo de ingeniería hace de verdad: decidir si hace falta ajustar pesos y, cuando hace falta, hacerlo con LoRA o QLoRA en una sola GPU, o destilando un modelo grande, que cuesta menos que RL pero pide un maestro y cientos de miles de respuestas suyas.

**Presenter feedback:**

---

## 1. Antes de ajustar pesos

<!-- design: split-left -->

### Content

**Cuando al modelo le falta información, la solución es RAG. Cuando tiene la información y responde con el formato, el estilo o la conducta equivocados, la solución es fine-tuning.**

![Recorrido típico de adaptación: prompt, ejemplos en el prompt, recuperación simple y compleja (RAG), y fine-tuning, con RAG sobre un modelo ajustado como punto final](research/corpus/huyen-aie-chapter-summaries.web/images/rag-vs-finetune.png)

- **Orden habitual.** Primero el prompt, después RAG y al final el fine-tuning. Las dos últimas se combinan.
- **Costo del fine-tuning.** Pide datos anotados, conocimiento de entrenamiento e infraestructura para servir el modelo, y puede empeorar tareas que antes andaban.

### Sources

- `corpus/huyen-aie-chapter-summaries.web.md` (Fig. 7-3, imagen `rag-vs-finetune.png`): "Example application development flows. After simple retrieval … whether to experiment with more complex retrieval … or finetuning depends on each application and its failure modes."
- `corpus/softwarephilosopher-aie-notes.web.md` (Key claims, cap. 7): "RAG for information-based failures; finetuning for behavior-based failures"; razones para no ajustar: degrada otras tareas, inversión inicial alta.
- `corpus/bagerbach-aie-notes.web.md` (Key claims, cap. 7): según estas notas, el libro dice "RAG is for facts, finetuning is for form"; flujo Prompting → RAG → Finetuning; "finetuning is easy, but getting data for finetuning is hard" (`corpus/huyen-aie-chapter-summaries.web.md`, Ch. 7).

### Speaker notes

Esta lámina junta las clases de prompting y de RAG con la de hoy. Un caso para cada lado: un asistente que no conoce los productos de la empresa necesita RAG; un asistente que conoce los datos pero no devuelve JSON válido o no respeta el tono de la marca necesita fine-tuning. Las notas del libro agregan que un modelo base nuevo puede superar al modelo que ajustaron el año pasado, y que el ajuste hay que rehacerlo. Tiempo objetivo: ~3 min.

### Presenter feedback

---

## 2. LoRA: una corrección de rango bajo

<!-- design: split-right -->

### Content

**LoRA congela los pesos del modelo. Para cada matriz elegida entrena dos matrices chicas, A y B, y su producto se suma al peso original: W + BA.**

- **Menos parámetros entrenables.** En GPT-3 175B, 10.000 veces menos, y la memoria de entrenamiento baja de 1,2 TB a 350 GB.
- **Adaptadores livianos.** Cada adaptación ocupa 35 MB en lugar de 350 GB. Cien adaptaciones del mismo modelo ocupan unos 354 GB; cien copias completas, 35 TB.
- **Sin costo al servir.** BA se suma a W antes de desplegar, así que la inferencia no agrega latencia.

![LoRA: la entrada x pasa por los pesos preentrenados W, congelados, y en paralelo por A (inicializada al azar) y B (inicializada en cero), de rango r; las dos salidas se suman](research/corpus/hu-2021-lora.pdf/images/fig-01-p001.png)

### Sources

- `corpus/hu-2021-lora.pdf.md` (Key claims, Fig. 1): "freezes the pretrained model weights and injects trainable rank decomposition matrices"; "reduce the number of trainable parameters by 10,000 times and the GPU memory requirement by 3 times"; VRAM "from 1.2TB to 350GB"; checkpoint "from 350GB to 35MB"; "350GB + 35MB * 100 ≈ 354GB as opposed to 100 * 350GB ≈ 35TB"; sin latencia de inferencia por construcción.
- Conflicto en el corpus: la reducción de memoria figura como "3 times", "up to 2/3" y 1,2 TB → 350 GB (≈ 3,4×) según la sección (Inconsistencies). La lámina da el par de valores medidos.
- `corpus/hu-2021-lora.pdf.md` (Definitions): |Θ| = 2 × L̂ × d_model × r; A gaussiana, B = 0.
- Derivación (notas): 4,7 M = 2 × 192 × 12.288 × 1 (rango 1 sobre W_q y W_v de las 96 capas de GPT-3) — `corpus/hu-2021-lora.pdf.md`, Table 4 y D.4.

### Speaker notes

La intuición del paper: el cambio que necesita una tarea nueva vive en un subespacio chico, así que alcanza con una matriz de rango bajo. Hacé la cuenta de parámetros: con rango 1 sobre las matrices de query y value de las 96 capas de GPT-3, 2 × 192 × 12.288 = 4,7 millones de parámetros entrenables, frente a 175.000 millones, y en WikiSQL rinde 73,4 frente a 73,8 del fine-tuning completo. B empieza en cero para que al arrancar el modelo sea exactamente el original. Para modelos actuales, el paper de QLoRA encontró que hay que aplicar LoRA a todas las capas lineales, no solo a query y value; lo retomás en la lámina siguiente. Tiempo objetivo: ~3 min.

### Presenter feedback

---

## 3. QLoRA: un modelo de 65B en una GPU

<!-- template: stat -->

### Content

**QLoRA guarda el modelo congelado en 4 bits y entrena adaptadores LoRA encima, en 16 bits. El fine-tuning de un modelo de 65B entra en una sola GPU de 48 GB.**

- **Más de 780 GB.** Memoria para ajustar LLaMA 65B en 16 bits.
- **45,0 GB.** Memoria medida para el mismo ajuste con QLoRA.
- **24 horas.** Entrenamiento de Guanaco 65B en una GPU, con el dataset OASST1 de la lámina 4.2.

Nota: para igualar al fine-tuning en 16 bits, LoRA tiene que ir en todas las capas lineales del transformer.

### Sources

- `corpus/dettmers-2023-qlora.pdf.md` (Key claims): "finetune a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning task performance"; "regular 16-bit finetuning of a LLaMA 65B parameter model requires more than 780 GB of GPU memory"; "only requiring 24 hours of finetuning on a single GPU"; "LoRA on all linear transformer block layers are required to match full finetuning performance".
- `corpus/dettmers-2023-qlora.pdf.md` (Fig. 6, App. G): 65B = 45,0 GB (batch 1, secuencia 512, gradient checkpointing).
- `corpus/dettmers-2023-qlora.pdf.md` (App. B.1): OASST1 filtrado a 9.209 ejemplos.
- `corpus/dettmers-2023-qlora.pdf.md` (Table 6, Inconsistencies): Guanaco 65B = 99,3 % de ChatGPT en Vicuna (80 prompts, juez GPT-4, ±4,4); en el benchmark OA, más grande, ChatGPT queda arriba (Elo 1015 vs 1008).

### Speaker notes

Tres ideas técnicas si alguien pregunta: NF4 es un formato de 4 bits con los niveles repartidos según una normal, que es como se distribuyen los pesos; la doble cuantización comprime también las constantes de escala; los optimizadores paginados mandan estado a la CPU cuando la GPU se llena. El titular que circuló fue "99,3 % de ChatGPT"; decí que sale de 80 preguntas juzgadas por GPT-4 y que en un benchmark más grande ChatGPT gana. Lo que sí es sólido es la memoria: un equipo con una GPU de 48 GB ajusta un modelo de 65B. Tiempo objetivo: ~3 min.

### Presenter feedback

---

## 4. Destilar un modelo grande

<!-- format: row -->

### Content

**Destilar es entrenar un modelo chico con las respuestas de uno grande. Para razonamiento rinde más que entrenar el modelo chico con RL y usa menos horas de GPU, pero necesita cientos de miles de respuestas del maestro.**

- **Destilación de DeepSeek-R1.** Qwen2.5-32B ajustado con 800.000 respuestas de R1 llega a 72,6 % en AIME 2024. El mismo modelo entrenado con RL desde cero llega a 47,0 %.
- **Destilación de Qwen3.** En Qwen3-8B, destilar alcanza 74,4 en AIME'24 con 1.800 horas de GPU; RL alcanza 67,6 con 17.920 horas.

### Sources

- `corpus/deepseek-2025-r1.pdf.md` (Key claims, Table 16): R1-Distill-Qwen-32B AIME 72,6 vs Qwen2.5-32B-Zero 47,0; SFT solo, sin RL, sobre ~800.000 muestras de R1.
- `corpus/qwen-2025-qwen3-technical-report.pdf.md` (Table 21): Qwen3-8B, on-policy distillation AIME'24 74,4 con 1.800 horas de GPU; RL 67,6 con 17.920 horas; "Distillation from advanced teacher models significantly outperforms reinforcement learning in performance and training efficiency".
- Derivación: 17.920 / 1.800 ≈ 10 — `corpus/qwen-2025-qwen3-technical-report.pdf.md` ("about 1/10 of the GPU hours").
- `corpus/qwen-2025-qwen3-technical-report.pdf.md` (§4.5): la fase on-policy ajusta al alumno "by aligning its logits with those of a teacher model … to minimize the KL divergence".
- `corpus/dettmers-2023-qlora.pdf.md` (Key claims): Vicuna "is thus the result of distillation from OpenAI GPT models"; las guías de OASST1 prohíben usar salidas de modelos GPT.

### Speaker notes

Destilar es más barato que RL, no barato en términos absolutos: DeepSeek usó unas 800.000 respuestas de R1, y la destilación de Qwen3-8B consumió 1.800 horas de GPU. El mecanismo es el SFT de la sección 4. Aclará la diferencia entre las dos tarjetas: DeepSeek destila con SFT sobre respuestas; Qwen3 agrega una fase on-policy donde el alumno genera y se lo acerca a las probabilidades (logits) del maestro, así que hace falta acceso a esas probabilidades, algo que da un modelo abierto y no una API que solo devuelve texto. Dos advertencias. La primera: la sección 3 mostró que entrenar con salida de modelos, generación tras generación, borra las colas de la distribución. La segunda es legal: muchos términos de uso prohíben usar la salida de un modelo para entrenar a un competidor, y por eso OASST1 excluyó salidas de GPT. Tiempo objetivo: ~3 min.

### Presenter feedback

---

# Conclusions

## 1. Key takeaways

### Content

**Cada conducta de un LLM se explica por los datos y la señal con que se entrenó.**

1. El pre-entrenamiento predice el token siguiente sobre billones de tokens; en InstructGPT (2022) se llevó el 98 % del cómputo. El post-entrenamiento usa de decenas de miles a un millón de ejemplos y fija la conducta.
2. C ≈ 6 · N · D. Chinchilla pide unos 20 tokens por parámetro; los modelos chicos actuales se entrenan con 10 a 100 veces más. Esos tokens salen de la web filtrada, con sesgos, mucho inglés y un español que usa 1,55 veces los tokens del inglés.
3. El SFT imita demostraciones; RLHF y DPO aprenden de comparaciones; el razonamiento se entrena con RL contra un verificador.
4. Los modelos inventan porque los datos que aparecen una sola vez en el corpus no se aprenden y la corrección binaria premia adivinar.
5. Para un producto, el orden es prompt, RAG y después LoRA, QLoRA o destilación.

### Sources

- Síntesis de la clase; las fuentes están en cada lámina.

### Speaker notes

No la leas en voz alta. Decí la frase de arriba y señalá cada punto con una oración propia; cada uno resume una o dos secciones. Si hay que recortar tiempo, esta lámina se puede pasar en un minuto. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 2. Para probar y preguntas

### Content

**Dos experimentos cortos para hacer con una notebook.**

- **Costo por idioma.** Tokenizar con tiktoken (cl100k_base) el mismo párrafo en español y en inglés y comparar la cantidad de tokens.
- **Modos de pensamiento.** Pedirle a un modelo Qwen3 chico el mismo problema de matemática con `/think` y con `/no_think`, y comparar la respuesta y la cantidad de tokens.

<!-- generate-image: right | la desproporción entre lo mucho que un modelo absorbe y lo poco que alcanza para darle forma a su conducta -->

### Sources

- `corpus/jun-2023-languages-tokenized.web.md` (Key claims): conteo con cl100k_base vía tiktoken.
- `corpus/qwen-2025-qwen3-technical-report.pdf.md` (§4.3): flags `/think` y `/no_think`; modelos densos desde 0,6B.

### Speaker notes

Espacio para preguntas. Los dos experimentos entran en una notebook y conectan con las láminas 3.4 y 5.4; si la cátedra tiene una práctica definida para esta clase, reemplazalos. Tiempo objetivo: ~2 min, más los ~9 min de margen que deja la suma de las láminas (81 min) para preguntas y ejercicios.

### Presenter feedback

---

# Open questions

- **Portada.** `class: "Clase 9: Cómo se entrena un LLM"` y `date: 2026-09-30` son provisorios. La clase 8 (`talks/transformers-a-fondo`) anunció en sus conclusiones que las variantes modernas de atención y memoria de K y V "se ven en la clase 9"; si esta charla es la clase 9, esa promesa queda sin cumplir, o esta pasa a ser la clase 10.
- **Kalai et al. 2025, umbral 0,75.** El paper da "t = 0.75 (penalty 2)", pero su fórmula t / (1 − t) da 3. Las notas de la lámina 5.5 omiten ese caso; confirmar contra el PDF antes de usarlo.
- **Petrov et al. 2023, Table 1.** Los valores de cl100k_base (español 1,55 y el resto de la lámina 3.4) salen de una tabla reconstruida desde una extracción aplanada (`corpus/petrov-2023-tokenizer-unfairness.pdf.md`, Inconsistencies). Verificar contra el render de la página antes de proyectar.
- **Proporción de inglés en Common Crawl.** Las fuentes dan 45 % (Villalobos) y más de 46 % (Jun, notas de *AI Engineering*), sin fecha de snapshot. La lámina 3.3 usa el rango.
- **Imágenes con stub pendiente.** Las figuras que usa este borrador (salvo las de Data.pdf) tienen en sus records un stub `<!-- pending: process_images -->`; el Editor las abrió y verificó que muestran lo que la lámina dice, pero la fase 2 del librarian no las transcribió. Láminas afectadas: 1.2, 2.3, 4.4, 4.5, 5.1, 5.3, 5.4, 6.1, 6.2. Re-verificar después de la fase 2 del librarian.
- **Figura de la lámina 3.5.** Es una foto en perspectiva de la página del libro, con texto vecino. La figura original (`villalobos-2024-run-out-of-data.pdf/images/fig-01-p001.png`) está recortada con el abstract al lado. Hace falta un recorte limpio de una de las dos.
- **Lámina 1.1.** El paper no aclara si el prompt de la Fig. 47 fue elegido a mano; los de las Figs. 48–50 sí ("5 selected from 15", completions sin elegir). Si se quiere un ejemplo sin sesgo de selección, usar el de la Fig. 46.
- **Cómputo del post-entrenamiento en modelos actuales.** El único reparto medido en el corpus es el de InstructGPT (2022). DeepSeek-R1 da el costo del post-entrenamiento (147.000 horas de H800) pero no el del pre-entrenamiento de V3, así que no se puede calcular la proporción.
- **Llama 3.** Las cifras de Llama 3 (15 billones de tokens, 214 tokens por parámetro) vienen de Villalobos et al., fuente secundaria; el corpus no tiene el paper de Llama 3.
- **Ejercicios de la lámina de cierre.** Son una sugerencia del Editor; la cátedra define la práctica.
- **Libro *AI Engineering*.** El corpus tiene resúmenes de terceros, no el texto. Las citas de las láminas 3.3 y 6.1 atribuidas al libro vienen de esas notas.
- **Revisión del Composer aplicada sin ronda del presentador (2026-09-26).** Por decisión del presentador no hubo Review; el Editor tomó estas decisiones solo:
  - **Tiempo.** La suma original era 89 min. Se pasaron las láminas "Menos acceso y más texto sintético" (ex 3.6) y "Cómo se premia decir 'no sé'" (ex 5.6) a Cut material; la idea central de cada una quedó en las notas de 3.5 y de 5.5. Se acortaron 2.2, 3.1 y 5.3 en 1 min cada una. Suma nueva: 81 min, con ~9 min de margen. Si el presentador prefiere mostrar la tabla de umbrales de Kalai, se puede recuperar la ex 5.6 desde Cut material.
  - **Lámina 2.4.** El rango "entre 10 y 100 veces" vale para modelos chicos; se agregó Llama 2 70B (unos 29 tokens por parámetro, 1,4× Chinchilla) como contraste.
  - **Lámina 5.4.** Retitulada al interruptor entrenado; los niveles de gpt-oss pasaron a las notas porque el model card no publica cómo se entrenan.
  - **Lámina 3.4.** Se retiró la afirmación de que los tokenizers más grandes achican la brecha: el corpus no tiene mediciones posteriores a 2023.
  - **Lámina 6.4.** "Acceso a las probabilidades del maestro, que una API que solo devuelve texto no da" es inferencia del Editor a partir de Qwen3 §4.5 (alinear logits); ninguna fuente del corpus lo dice sobre APIs.
  - **Títulos.** Acortados a ≤ 25 caracteres (secciones) y ≤ 40 (láminas); los nombres de paper y año pasaron al cuerpo.

# Cut material

- **Tamaño crítico de batch, LSTM frente a transformer y la conjetura de L* ≈ 1,7 nats de Kaplan.** Fuera del hilo de la sección 2; no cambian la conclusión sobre tokens por parámetro.
- **Ghost Attention, context distillation y los dos modelos de recompensa de Llama 2.** Detalle de implementación que alarga la sección 4 sin agregar una idea nueva.
- **Desajuste entre la web y el uso real (WildChat, Longpre).** El 30 % de las conversaciones pide escritura creativa y las noticias son casi el 40 % de los tokens de C4. Buen dato, pero abre un tema de derechos de autor que no entra en 90 minutos.
- **Datos no públicos (Villalobos).** Mensajería y redes cerradas podrían sumar del orden de un cuatrillón de tokens; las estimaciones del paper no reproducen su propia aritmética (Inconsistencies) y el tema es de privacidad.
- **Process reward models y MCTS en DeepSeek-R1.** Intentos fallidos; interesan a quien quiera investigar, no a esta clase.
- **Model merging y aprendizaje federado.** Mencionados en las notas de *AI Engineering*, sin fuente primaria en el corpus.
- **Analogía de la telegrafía (Jun).** El costo de telegrafiar en chino como antecedente del costo por token; queda para las notas si sobra tiempo en la lámina 3.4.
- **Lámina ex 3.6 "Menos acceso y más texto sintético" (2026-09-26, por tiempo; la idea quedó en las notas de 3.5).** Contenido: "Cerca del techo aparecen dos presiones nuevas: los sitios bloquean a los crawlers y la web se llena de texto generado por modelos." (1) Acceso restringido: entre 2023 y 2024, robots.txt pasó a bloquear por completo más del 5 % de los tokens de C4 y más del 28 % de los tokens de sus fuentes más activas; el crawler de OpenAI quedó bloqueado en el 25,9 % de esas fuentes (`corpus/longpre-2024-consent-in-crisis.pdf.md`; la cifra del "head" figura como 28 %+, ~25 %+ y 20–33 % según la sección). (2) Texto generado por modelos: un modelo entrenado con la salida de otro pierde las colas de la distribución y, al repetir el ciclo, converge a pocas respuestas (model collapse; `corpus/shumailov-2023-curse-of-recursion.pdf.md`, solo fine-tuning de OPT-125m, un 10 % de datos originales limita el daño); los datos sintéticos rinden donde la salida se puede verificar (`corpus/villalobos-2024-run-out-of-data.pdf.md`).
- **Lámina ex 5.6 "Cómo se premia decir 'no sé'" (2026-09-26, por tiempo; la idea quedó en las notas de 5.5).** Contenido: umbral de confianza t en la consigna; acierto +1, "no sé" 0, error −t / (1 − t). Tabla: t = 0 → penalización 0, siempre responder (corrección binaria actual); t = 0,5 → 1, responder con confianza > 50 %; t = 0,9 → 9, responder con confianza > 90 %. Aplicarlo en los benchmarks que dominan las tablas; precedentes JEE (India) y AMC (EE. UU.). Fuente: `corpus/kalai-2025-why-lms-hallucinate.pdf.md`.
- **Tarjeta de gpt-oss en la lámina 5.4 (2026-09-26, una idea por lámina).** "Niveles en gpt-oss. Tres niveles (low, medium, high) en el system prompt; el model card no explica cómo se entrenan. En AIME 2025 sin herramientas, gpt-oss-120b pasa de 50,4 % a 80,0 % y a 92,5 %." Pasó a las notas de 5.4.
- **Oración de la lámina 3.4 sobre tokenizers nuevos (2026-09-26, sin fuente).** "Tokenizers más grandes (o200k, 151.669 tokens en Qwen3) achican la brecha, pero el corpus no tiene una medición de cuánto."
