---
presentation: Inteligencia Artificial Generativa (AI Gen)
class: "Clase 8: El transformer por dentro"
research: research/corpus/
description: Slides are grouped into Sections. Each Section contains one or more Slides.
presenter: Paulo Veiga, Claudio Righetti, Marco Sorondo (Universidad Austral)
audience: Estudiantes de grado de Ingeniería de Software con base técnica fuerte
duration: 90 min
date: 2026-09-23
---

# Thesis

**Claim:** Un transformer es una pila de bloques idénticos, y cada bloque hace dos cosas: la atención mezcla información entre posiciones y la red feed-forward la procesa posición por posición. La matemática de un bloque son ocho multiplicaciones de matrices, un softmax, una ReLU y dos normalizaciones. Con una frase de cuatro tokens y vectores de dimensión cuatro se calcula a mano.

**Why it matters:** Los modelos que los alumnos van a usar y a evaluar en la práctica (BERT como encoder para RAG, un LLM decoder-only como agente) son este mismo bloque repetido con otros números. Quien sabe de dónde sale cada operación puede leer un paper de arquitectura nueva, razonar sobre costo por token y KV cache, y elegir un encoder con criterio.

**Presenter feedback:**

---

# Agenda

**Narrative arc:** La clase anterior terminó en la intuición de que cada token mira a todos los demás y arma su lectura de la frase. Esta clase muestra la matemática detrás de esa intuición. Primero se retoma el ciclo token a token y se fija la notación (1). Después la atención con números: tres proyecciones del mismo vector, el producto punto como medida de afinidad, la escala, el softmax y la mezcla de valores, calculado a mano sobre "the cat sat on", y la máscara causal que convierte un encoder en un generador (2). Sigue el bloque completo: varias cabezas en paralelo, la red feed-forward por posición, las conexiones residuales, la normalización y la codificación de posición, con la cuenta de parámetros por bloque (3). Con el bloque armado se ve cómo se apila: las dos columnas del paper de 2017, por qué los LLM se quedaron solo con el decoder, por qué BERT se quedó solo con el encoder, y la familia de modelos derivados que la práctica va a usar (4). Después las variantes modernas, cada una como respuesta a un cuello de botella concreto, solo a nivel de idea; la clase siguiente las desarrolla (5). El cierre es el entrenamiento a vuelo de pájaro: qué se minimiza, cómo escala la pérdida con el tamaño, y de dónde salen los cientos de miles de millones de parámetros de la tabla de la clase anterior (6).

**Sections (in delivery order):**

- 1. Dónde quedamos
- 2. La atención con números
- 3. El bloque completo
- 4. Encoder, decoder y la familia
- 5. Lo que cambió desde 2017
- 6. Entrenamiento a vuelo de pájaro
- Conclusiones

**Presenter feedback:**

---

# 1. Dónde quedamos

**Goal of this section:** Retomar en dos láminas el punto exacto donde terminó la clase anterior y fijar la notación de matrices que se usa el resto de la clase. Dos láminas.

**Presenter feedback:**

---

## 1. El ciclo de generación con el transformer abierto

### Content

**Cada token generado es una vuelta del ciclo: tokenizar, embeber, transformer, distribución sobre el vocabulario, elegir. El transformer es un bloque repetido N veces.**

```ascii
  "the cat sat on"
        |
        v
  [ TOKENIZAR ]  the | cat | sat | on          4 tokens
        |
        v
  [ EMBEDDER ]   una fila por token            X : 4 x d
        |
        v
  +---------------------------------------------+
  |  TRANSFORMER  =  bloque x N                 |   <-- hoy
  |                                             |
  |   bloque:  atencion  ->  feed-forward       |
  +---------------------------------------------+
        |
        v
  [ DISTRIBUCION ] un valor por token de V      |V| = 50.257 en GPT-2
        |
        v
  [ ELEGIR ]  "the"  -> se agrega y vuelve a empezar
```

- **Entrada y salida del bloque tienen la misma forma:** una matriz de n filas (una por token) por d columnas. Por eso se pueden apilar.
- **N bloques con la misma forma y pesos propios.** GPT-2 chico: 12 bloques. El paper de 2017: 6.
- **Cada bloque hace dos cosas.** La atención mueve información entre tokens. La feed-forward procesa cada token por separado.

### Sources

- `gpt2-radford-2019.pdf.md` (§2.3, Table 2): vocabulario de 50.257 tokens, 12 capas y d_model 768 para el modelo chico.
- `attention-is-all-you-need.html.md` (§3.1): N = 6 capas idénticas en encoder y decoder.
- `talks/palabra-al-transformer/final.md` (6.3): el ciclo de seis pasos de la clase anterior; este diagrama abre la caja del transformer.

### Speaker notes

Es la lámina 6.3 de la clase pasada con una sola diferencia: la caja "TRANSFORMER" está abierta y dice "bloque x N". Decilo así, en voz alta: lo de afuera ya lo vieron, hoy es la caja. La frase de ejemplo va a ser "the cat sat on" toda la clase, con vectores de dimensión 4, porque con eso las cuentas se hacen a mano y en la práctica van a tener que hacerlas. Tiempo objetivo: ~2 min.

**Presenter feedback:**
"La atención mueve información entre tokens, enriqueciendo sus embeddings con información del contexto"
---

## 2. La frase como matriz

### Content

**La frase "the cat sat on" es una matriz X de 4 tokens por 4 dimensiones. La atención opera sobre esa matriz.**

| | dim 1 | dim 2 | dim 3 | dim 4 |
|---|---|---|---|---|
| **the** | 1 | 0 | 1 | 0 |
| **cat** | 0 | 2 | 0 | 1 |
| **sat** | 1 | 1 | 1 | 1 |
| **on** | 0 | 1 | 1 | 2 |

- **Una fila por token, una columna por dimensión.** En un modelo real las filas son cientos o miles y d es 768 (GPT-2 chico), 512 (paper de 2017) o más. La forma es la misma.
- **Los números son de juguete.** Son enteros chicos para poder multiplicar a mano. En un modelo real son decimales aprendidos sin significado individual.
- **Convención:** n es la cantidad de tokens (acá 4) y d la dimensión del embedding (acá 4). Las matrices de pesos W son de d por d salvo indicación.

### Sources

- Ejemplo propio, calculado con NumPy (`ejemplo_atencion.py`, guardado con el material de la práctica). Los valores de X se eligieron para que ningún par de filas dé los mismos scores de atención.
- `attention-is-all-you-need.html.md` (§3.2.2): d_model = 512 en el modelo base. `gpt2-radford-2019.pdf.md` (Table 2): 768 en GPT-2 chico.

### Speaker notes

Lámina de referencia, no de explicación: se muestra, se dice que van a volver a verla, y se sigue. El único punto que vale decir es que en un modelo real un embedding es un vector de 768 decimales que nadie interpreta columna por columna; acá son cuatro enteros solo para poder multiplicar en el pizarrón. Si alguien pregunta de dónde salen estos números en un modelo real: de la tabla de embeddings, que es una matriz |V| por d aprendida, y la lámina 3.2 de la clase pasada. Tiempo objetivo: ~1 min.

**Presenter feedback:**
es confuso hacer que la dimension del embedding sea exactamente la misma que la cantidad de palabras, hagamos que sean distintos para que no piensen que la matriz es siempre cuadrada
---

# 2. La atención con números

**Goal of this section:** Calcular una capa de self-attention completa sobre la frase de juguete, operación por operación, y justificar cada una: por qué tres proyecciones, por qué producto punto, por qué la escala, por qué softmax, por qué la mezcla de valores. Cierra con la máscara causal. Seis láminas.

**Presenter feedback:**

---

## 1. Tres proyecciones del mismo vector

### Content

**Cada token se proyecta tres veces con tres matrices aprendidas. Q representa la consulta del token, K la clave con la que otros lo encuentran y V el contenido que aporta cuando lo eligen.**

```ascii
                 X (4 x d)
       fila de "cat": [0 2 0 1]
                 |
     +-----------+-----------+
     |           |           |
     v           v           v
   X Wq        X Wk        X Wv
     |           |           |
     v           v           v
     Q           K           V
  "que busco"  "que ofrezco" "que entrego"
   (4 x d)      (4 x d)      (4 x dv)
```

- **Las tres salen del mismo X.** De ahí el nombre *self*-attention: consultas, claves y valores vienen de la misma secuencia.
- **Son tres matrices porque son tres trabajos.** Buscar y ser encontrado no es simétrico: "it" busca un sustantivo y "animal" ofrece ser uno. Si consulta y clave fueran la misma proyección, un token de norma grande se parecería sobre todo a sí mismo; las tres matrices rompen esa simetría.
- **En el ejemplo:** Wq es la identidad (Q = X), Wk permuta pares de columnas y Wv suma la columna 1 con la 3 y la 2 con la 4, y baja a dimensión 2. Se eligieron para que las cuentas salgan a mano; en un modelo real las tres son aprendidas y densas.

### Sources

- `attention-is-all-you-need.html.md` (§3.2): "An attention function can be described as mapping a query and a set of key-value pairs to an output"; §3.2.3: en la self-attention del encoder "all of the keys, values and queries come from the same place".
- `illustrated-transformer-alammar.html.md` (sección "Self-Attention in Detail"): las tres matrices de pesos W^Q, W^K, W^V y la analogía de consulta, clave y valor.

### Speaker notes

La pregunta que hay que contestar acá es por qué tres y no una. La respuesta corta es la asimetría: lo que un token pregunta no es lo que ofrece. Si usaran el mismo vector para buscar y para ser encontrado, el score de un token contra sí mismo sería su norma al cuadrado, y por Cauchy-Schwarz ningún otro token de norma igual o menor podría superarlo: la atención tendería a que cada token se mire a sí mismo. Ojo con afirmarlo como regla absoluta: con Q = K = X en el ejemplo, la fila de "the" da [2 0 2 1], empate entre "the" y "sat", porque "sat" tiene norma mayor. Las matrices del ejemplo son deliberadamente simples y hay que decirlo: nadie entrena una identidad. Tiempo objetivo: ~3 min.

**Presenter feedback:**
esta bien, pero creo que la intuicion para V es la siguiente: aplicar Q sobre el embedding de una palabra me da el significado contextual de la palabra codificado en un vector, aplicar K sobre todas las palabras me da el la información que aportan el resto de las palabras sobre la palabra de la query, que resulta en la matriz de atencion; y V aplica la operacion que inter-relaciona la informacion entre la palabra que se aplicó a Q contra las K utilizando la matriz de atención resultante, resultando en un nuevo embedding que codifica el significado de la palabra pero con mas enriquecimiento, mas informacion
---

## 2. Q y K en el ejemplo

### Content

**Con las matrices del ejemplo, las consultas quedan iguales a X y las claves son X con los pares de columnas intercambiados.**

| Q = X Wq | | | | |
|---|---|---|---|---|
| **the** | 1 | 0 | 1 | 0 |
| **cat** | 0 | 2 | 0 | 1 |
| **sat** | 1 | 1 | 1 | 1 |
| **on** | 0 | 1 | 1 | 2 |

| K = X Wk | | | | |
|---|---|---|---|---|
| **the** | 0 | 1 | 0 | 1 |
| **cat** | 2 | 0 | 1 | 0 |
| **sat** | 1 | 1 | 1 | 1 |
| **on** | 1 | 0 | 2 | 1 |

- **Wk intercambia la columna 1 con la 2 y la 3 con la 4.** Por eso "the", que en X es [1 0 1 0], como clave es [0 1 0 1].
- **V baja a dimensión 2** sumando la columna 1 con la 3 y la 2 con la 4: the [2 0], cat [0 3], sat [2 2], on [1 3]. La salida de la atención va a tener esa dimensión.
- **La forma importa más que los valores.** Q y K tienen que tener la misma dimensión para poder multiplicarse. V puede tener otra.

### Sources

- Ejemplo propio (`ejemplo_atencion.py`): Wq = I, Wk = permutación (1 2)(3 4), Wv = [[1,0],[0,1],[1,0],[0,1]].
- `attention-is-all-you-need.html.md` (§3.2.1): "queries and keys of dimension d_k, and values of dimension d_v".

### Speaker notes

Lámina de cálculo puro; no expliques, verificá una celda con ellos. Elegí la fila de "cat" en K: [0 2 0 1] con las columnas intercambiadas es [2 0 1 0]. Con una alcanza. El punto conceptual es la última viñeta: d_k tiene que coincidir entre Q y K porque se van a multiplicar, y d_v es libre. En el paper las tres son 64 por cabeza. Tiempo objetivo: ~2 min.

**Presenter feedback:**
falta aclarar que las matrices W que resultan en Q,K,V son parámetros entrenables del modelo
---

## 3. El producto punto mide afinidad

### Content

**Cada consulta se multiplica contra todas las claves. El resultado, Q Kᵀ, es una matriz de n por n: cuánto le importa a cada token cada otro token.**

| Q Kᵀ | the | cat | sat | on |
|---|---|---|---|---|
| **the** | 0 | 3 | 2 | 3 |
| **cat** | 3 | 0 | 3 | 1 |
| **sat** | 2 | 3 | 4 | 4 |
| **on** | 3 | 1 | 4 | 4 |

- **Una celda es un producto punto.** Fila "cat" (consulta [0 2 0 1]) contra columna "the" (clave [0 1 0 1]): 0·0 + 2·1 + 0·0 + 1·1 = 3.
- **Por qué producto punto.** Es grande cuando los dos vectores apuntan para el mismo lado y se calcula para toda la frase con una sola multiplicación de matrices, que es la operación para la que las GPU están optimizadas. El paper lo compara con la atención aditiva (una red chica por par) y la descarta por lenta.
- **Esta matriz es el costo cuadrático.** Son n² celdas: 16 con 4 tokens, 16 millones con 4.096, por cabeza y por capa.

### Sources

- `attention-is-all-you-need.html.md` (§3.2.1): dot-product vs additive attention, "dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code"; Table 1: complejidad O(n²·d) por capa.
- Ejemplo propio: la fila de "cat" en QKᵀ es [3 0 3 1].

### Speaker notes

Hacé la cuenta de una celda en el pizarrón, la de "cat" contra "the", y dejá que ellos hagan otra. La observación más importante es la de la tercera viñeta: esta matriz es la razón de casi todo lo que viene en la sección 5 (KV cache, FlashAttention, GQA, atención lineal). Cuando alguien diga "el transformer es cuadrático", es esta tabla. Una cosa que conviene señalar: la diagonal no es la más alta en todas las filas ("the" contra sí mismo da 0), y eso es efecto de que Wk no es la identidad. Con Q = K la diagonal tendería a ganar, sobre todo en los tokens de norma grande. Tiempo objetivo: ~4 min.

**Presenter feedback:**
falta aclarar que Q Kᵀ es *casi* la matriz de atención
---

## 4. Escalar y repartir: el softmax

### Content

**Los scores se dividen por √d_k y cada fila pasa por un softmax. El resultado es una distribución por token: pesos positivos que suman uno.**

| softmax(Q Kᵀ / √4) | the | cat | sat | on |
|---|---|---|---|---|
| **the** | 0,08 | 0,35 | 0,21 | 0,35 |
| **cat** | 0,39 | 0,09 | 0,39 | 0,14 |
| **sat** | 0,12 | 0,20 | 0,34 | 0,34 |
| **on** | 0,21 | 0,08 | 0,35 | 0,35 |

- **Dividir por √d_k = 2.** La fila "cat" pasa de [3 0 3 1] a [1,5 0 1,5 0,5]. Sin la escala, los productos crecen con d_k y con d_k = 64 el softmax se satura: un peso cerca de 1, el resto cerca de 0 y gradiente casi nulo.
- **Softmax por fila:** e^{x_i} / Σ e^{x_j}. Para "cat": e^{1,5} = 4,48, e^0 = 1, e^{1,5} = 4,48, e^{0,5} = 1,65; suma 11,6; pesos 0,39 · 0,09 · 0,39 · 0,14.
- **Por qué softmax.** Es derivable, así que se entrena por gradiente, y reparte: "cat" mira a "the" y a "sat" por igual y algo a "on". Quedarse con el máximo daría un peso de 1 a un solo token y no tendría gradiente.

### Sources

- `attention-is-all-you-need.html.md` (§3.2.1, eq. 1 y nota al pie): Attention(Q,K,V) = softmax(QKᵀ/√d_k)V; "for large values of d_k, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients"; con componentes de varianza 1, el producto punto tiene varianza d_k.
- Ejemplo propio: fila "cat" del softmax [0,39 0,09 0,39 0,14].

### Speaker notes

Dos justificaciones, y las dos van al ejercicio a mano de la práctica. La de la escala es estadística: si las componentes de q y k son independientes con varianza 1, la suma de d_k productos tiene varianza d_k, así que dividir por √d_k devuelve la varianza a 1 sea cual sea la dimensión. Con d = 4 el efecto es chico, pero decí que con 64 sin la escala los scores andan por ±8 y el softmax ya está saturado. La del softmax es la derivabilidad: el entrenamiento necesita que un cambio chico en los pesos mueva la salida un poco, y un máximo duro no lo hace. Verificá la fila de "cat" con ellos, con calculadora, es un minuto. Tiempo objetivo: ~4 min.

**Presenter feedback:**
falta aclarar que esto resulta en la matriz de atención
---

## 5. Mezclar los valores

### Content

**La salida de cada token es la suma de todos los V, pesada por su fila de atención. "cat" se reescribe como 0,39·the + 0,09·cat + 0,39·sat + 0,14·on.**

```ascii
  fila de atencion de "cat"     V (que entrega cada token)
     the  cat  sat  on             the [2 0]
    [0,39 0,09 0,39 0,14]    x     cat [0 3]     =   [1,69  1,46]
                                   sat [2 2]
                                   on  [1 3]
                                                  nueva "cat"
  0,39*2 + 0,09*0 + 0,39*2 + 0,14*1 = 1,69
  0,39*0 + 0,09*3 + 0,39*2 + 0,14*3 = 1,46
```

| salida A·V | dim 1 | dim 2 |
|---|---|---|
| **the** | 0,94 | 2,55 |
| **cat** | 1,69 | 1,46 |
| **sat** | 1,26 | 2,29 |
| **on** | 1,49 | 2,00 |

- **Es un promedio ponderado.** Cada token sale como una mezcla de lo que entregan todos, con más peso de los que le importan. Es la versión numérica de "it reescrito con el peso puesto sobre animal".
- **Toda la frase se procesa con cinco multiplicaciones de matrices y un softmax:** X Wq, X Wk, X Wv, Q Kᵀ, softmax por fila y A·V. No hay bucle sobre los tokens, y por eso paraleliza.

### Sources

- `attention-is-all-you-need.html.md` (§3.2): "The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key."
- `talks/palabra-al-transformer/final.md` (5.8): "it reescrito con el peso puesto sobre animal", el diagrama cualitativo que acá se vuelve numérico.
- Ejemplo propio: salida completa A·V.

### Speaker notes

Acá se cierra la atención. La cuenta del diagrama es la que hay que hacer en el pizarrón: una fila de pesos por una matriz de valores da la nueva fila del token. Insistí en la palabra "mezcla": la salida de "cat" ya no es solo "cat", es "cat" leído en su contexto, y eso es lo que la clase pasada llamaba representación contextual. La segunda viñeta es el argumento de la paralelización, ahora con las operaciones a la vista: ningún paso depende del token anterior. Tiempo objetivo: ~4 min.

**Presenter feedback:**

---

## 6. La máscara causal

### Content

**Para generar texto, un token no puede mirar a los que vienen después. Se ponen en menos infinito antes del softmax y quedan con peso cero.**

| con máscara | the | cat | sat | on |
|---|---|---|---|---|
| **the** | 1,00 | 0 | 0 | 0 |
| **cat** | 0,82 | 0,18 | 0 | 0 |
| **sat** | 0,19 | 0,31 | 0,51 | 0 |
| **on** | 0,21 | 0,08 | 0,35 | 0,35 |

- **Por qué menos infinito.** e^{-∞} = 0, así que el softmax reparte solo entre los tokens permitidos y la fila sigue sumando uno. Un score de cero le daría al token prohibido un peso e^0 = 1, que no es cero.
- **La última fila no cambia.** "on" ya veía a todos. La fila de "the" ahora solo se ve a sí misma.
- **Es la diferencia entre un encoder-only y un decoder-only.** BERT no enmascara y cada token ve la frase entera. GPT enmascara y cada token ve solo lo anterior. El resto del bloque es igual.
- **La salida cambia con la máscara:** "cat" pasa de [1,69 1,46] a [1,64 0,55], porque ya no recibe nada de "sat" ni de "on". Salida completa: the [2,00 0], cat [1,64 0,55], sat [1,39 1,94], on [1,49 2,00].

### Sources

- `attention-is-all-you-need.html.md` (§3.2.3): "We implement this inside of scaled dot-product attention by masking out (setting to −∞) all values in the input of the softmax which correspond to illegal connections", para preservar la propiedad autorregresiva.
- `bert-devlin-2018.html.md` (nota 4): "the bidirectional Transformer is often referred to as a 'Transformer encoder' while the left-context-only version is referred to as a 'Transformer decoder'".
- `gpt2-to-kimi3-waterloo-intern.md.md`: el código de GPT-2, `att.masked_fill(mask == 0, float('-inf'))` antes del softmax.
- Ejemplo propio: softmax con máscara triangular y su salida A·V.

### Speaker notes

La justificación es de entrenamiento: si "cat" pudiera ver "sat" mientras aprende a predecir "sat", la tarea sería trivial y no aprendería nada. Con la máscara, una frase de n tokens da n ejemplos de entrenamiento válidos de una vez: es la ventana deslizante de la clase pasada calculada en paralelo. La tercera viñeta organiza la sección 4: encoder y decoder difieren en esta matriz triangular y en poco más. Tiempo objetivo: ~4 min.

**Presenter feedback:**

---

# 3. El bloque completo

**Goal of this section:** Armar el bloque del transformer alrededor de la atención ya calculada: varias cabezas, la feed-forward por posición, residuales y normalización, la posición, y la cuenta de parámetros. Seis láminas.

**Presenter feedback:**

---

## 1. Varias cabezas en paralelo

### Content

**Multi-head attention corre h atenciones en paralelo, cada una con sus propias Wq, Wk, Wv y dimensión d/h, concatena las salidas y las proyecta con una matriz más.**

```ascii
                     X (n x d)
                        |
        +---------------+---------------+
        |               |               |
     cabeza 1        cabeza 2   ...   cabeza h
   Wq1 Wk1 Wv1     Wq2 Wk2 Wv2      Wqh Wkh Wvh
   (d x d/h c/u)
        |               |               |
   atencion(1)     atencion(2)      atencion(h)
   (n x d/h)       (n x d/h)        (n x d/h)
        |               |               |
        +-------- concatenar -----------+
                        |
                   (n x d)  x  Wo (d x d)
                        |
                        v
                  salida (n x d)
```

- **Por qué varias.** Una sola cabeza promedia: si "it" necesita mirar al sujeto para una cosa y al verbo para otra, con una distribución tiene que repartir. Con ocho cabezas, cada una aprende una relación distinta. El paper lo muestra: cabezas que siguen dependencias largas, otras que resuelven anáforas, otras que siguen la estructura sintáctica.
- **El costo no sube.** d_k = d/h: en el paper, 512/8 = 64 por cabeza. Las ocho cabezas juntas cuestan lo mismo que una de dimensión completa.
- **En el ejemplo de juguete,** con h = 2, habría dos cabezas de dimensión 2. La tabla de atención de la sección 2 corresponde a una sola cabeza.

### Sources

- `attention-is-all-you-need.html.md` (§3.2.2): "Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this"; h = 8, d_k = d_v = d_model/h = 64; "the total computational cost is similar to that of single-head attention with full dimensionality"; Table 3 (A): una sola cabeza es 0,9 BLEU peor que la mejor configuración, y demasiadas cabezas también empeoran. Figuras 3 a 5: cabezas que "clearly learned to perform different tasks".
- `illustrated-transformer-alammar.html.md` ("The Beast With Many Heads"): concatenación de las z_i y multiplicación por W^O.

### Speaker notes

La justificación es el "averaging inhibits this" del paper: una sola distribución de pesos no puede apuntar fuerte a dos lugares por dos motivos distintos. La segunda viñeta suele sorprender y conviene detenerse: no son ocho atenciones de 512, son ocho de 64, y la concatenación devuelve 512. Wo es la matriz que mezcla lo que dijeron las cabezas; sin ella cada cabeza escribiría en su propio rincón del vector. Tiempo objetivo: ~3 min.

**Presenter feedback:**

---

## 2. La feed-forward: la misma red para cada posición

### Content

**Después de la atención, cada token pasa solo por una red de dos capas: subir a 4d, ReLU, bajar a d. Es la misma red para todas las posiciones y concentra dos tercios de los parámetros del bloque.**

- **FFN(x) = max(0, x W1 + b1) W2 + b2.** En el paper: d = 512, d_ff = 2048. BERT usa el mismo 4d, con GELU en vez de ReLU, siguiendo al GPT original.
- **Por qué hace falta.** La atención solo mezcla: su salida es una combinación lineal de los V. La ReLU de esta red es la no linealidad que permite computar algo nuevo con lo mezclado. Sin FFN, una pila de bloques de atención seguiría siendo casi lineal.
- **Por qué por posición.** Se aplica fila por fila, con los mismos pesos, sin mirar a los vecinos. El intercambio entre tokens ya ocurrió en la atención; acá cada token procesa lo que recibió. El paper lo describe como dos convoluciones de tamaño 1.
- **Cuenta:** dos matrices de d por 4d son 8d² parámetros. La atención (Wq, Wk, Wv, Wo) son 4d². Feed-forward es el doble que la atención.

### Sources

- `attention-is-all-you-need.html.md` (§3.3, eq. 2): FFN(x) = max(0, xW1 + b1)W2 + b2, d_model = 512, d_ff = 2048, "Another way of describing this is as two convolutions with kernel size 1".
- `scaling-laws-kaplan-2020.html.md` (§2.1, Table 1): feed-forward 2·n_layer·d_model·d_ff parámetros; QKV 3·n_layer·d_model·d_attn y proyección de salida n_layer·d_attn·d_model.
- `bert-devlin-2018.html.md` (§3, nota): feed-forward de tamaño 4H, GELU.

### Speaker notes

La justificación de la FFN es la que más cuesta y la que más importa: la atención es lineal en V (pesos por valores), así que si solo hubiera atención, el modelo entero sería casi una composición de mapas lineales. La ReLU es el único lugar del bloque donde se computa algo que no es una combinación de la entrada. La cuenta de la última viñeta prepara la lámina 3.6. Tiempo objetivo: ~4 min.

**Presenter feedback:**

---

## 3. Residuales: la salida es la entrada más una corrección

### Content

**Cada subcapa suma su resultado al vector de entrada: x → x + Atención(x) → x + FFN(x). El camino directo deja pasar la entrada intacta y las capas aprenden solo la diferencia.**

```ascii
        x  ---------------------------+
        |                             |
        v                             |
   [ atencion ]                       |  camino residual
        |                             |
        v                             v
       (+) <--------------------------+
        |
   x' = x + atencion(x)
        |  -----------------------------+
        v                               |
   [ feed-forward ]                     |
        |                               v
       (+) <----------------------------+
        |
   x'' = x' + FFN(x')
```

- **El vector de cada token atraviesa toda la pila** y cada bloque le agrega algo. Se lo llama *residual stream*. Una cabeza puede escribir en él en la capa 3 y otra leerlo en la capa 10.
- **Por qué está.** Con 12, 48 o 96 bloques apilados, el gradiente tiene que llegar desde la salida hasta el embedding. El camino residual es una identidad, así que la señal de error pasa sin atenuarse por más capas que haya.
- **Por qué d se conserva** en toda la pila: para que la suma sea posible.

### Sources

- `attention-is-all-you-need.html.md` (§3.1): "We employ a residual connection around each of the two sub-layers, followed by layer normalization. That is, the output of each sub-layer is LayerNorm(x + Sublayer(x))"; todas las subcapas y los embeddings producen salidas de dimensión d_model = 512 "to facilitate these residual connections".
- `gpt2-to-kimi3-waterloo-intern.md.md` (código de GPT-2): `x = x + self.attn(self.ln_1(x)); x = x + self.mlp(self.ln_2(x))`.
- `gpt2-radford-2019.pdf.md` (§2.3): los pesos de las capas residuales se escalan al inicializar por 1/√N, con N la cantidad de capas residuales.

### Speaker notes

La justificación es de optimización y les va a sonar de la clase de backpropagation: sin el atajo, el gradiente en la capa 1 es el producto de 48 jacobianos y se desvanece o explota. Con el atajo, hay un término que es la identidad. La consecuencia de la segunda viñeta es la más útil para leer papers modernos: la imagen del residual stream como una cinta que atraviesa el modelo y a la que las capas leen y escriben. AttnRes de Kimi K3, que van a ver en la clase que viene, es una atención sobre esa cinta. Tiempo objetivo: ~3 min.

**Presenter feedback:**
falta explicar la razón matemática y la intuición de por la que se hace todo esto, quizás una diapositiva previa explicando el problema primero y luego la solución que se muestra en esta diapositiva
---

## 4. Layer norm: mantener los números en rango

### Content

**Antes de cada subcapa, cada vector se normaliza por separado: se le resta su media y se lo divide por su desvío. Dos parámetros aprendidos por dimensión lo reescalan.**

- **La cuenta, para un vector [2 0 1 1]:** media 1, varianza 0,5, desvío 0,71. Normalizado: [1,41 -1,41 0 0]. Después se multiplica por γ y se suma β, aprendidos.
- **Por qué.** Cada bloque suma algo al residual stream, así que sin normalizar la escala del vector crece capa a capa y el softmax de la atención y la ReLU dejan de trabajar en su rango. La normalización pone cada token en escala conocida antes de entrar a una subcapa.
- **Por qué por vector.** Normalizar sobre las d dimensiones de un token no depende de qué otras frases hay en el batch ni de la longitud de la secuencia. Batch norm depende de las dos cosas, y por eso no se usa en transformers.
- **Pre-LN y post-LN.** El paper de 2017 normaliza después de sumar: LN(x + Sub(x)). GPT-2 lo movió antes: x + Sub(LN(x)). Con pre-LN el camino residual queda limpio y el entrenamiento es más estable. GPT-2, ViT y casi todo lo posterior usan pre-LN.

### Sources

- `attention-is-all-you-need.html.md` (§3.1): LayerNorm(x + Sublayer(x)), post-LN.
- `gpt2-radford-2019.pdf.md` (§2.3): "Layer normalization was moved to the input of each sub-block, similar to a pre-activation residual network and an additional layer normalization was added after the final self-attention block".
- `vit-dosovitskiy-2020.html.md` (§3.1, eq. 2-3): "Layernorm (LN) is applied before every block, and residual connections after every block".
- Ejemplo propio: LN([2 0 1 1]) = [1,41 -1,41 0 0] con ε = 10⁻⁵.

### Speaker notes

Hacé la cuenta de la primera viñeta, es de treinta segundos y es exactamente lo que van a tener que justificar en el ejercicio a mano: qué hace y por qué. La justificación de "por vector" es la que distingue layer norm de batch norm, que vieron en redes: acá cada token se normaliza solo, y por eso funciona con secuencias de distinto largo y con batch de tamaño uno en inferencia. Lo de pre-LN contra post-LN es una viñeta y sigue; lo que importa es que el diagrama de la lámina anterior, con la suma limpia, es pre-LN. Tiempo objetivo: ~3 min.

**Presenter feedback:**

---

## 5. La posición: la atención no sabe el orden

### Content

**Nada en Q Kᵀ depende de dónde está cada token: si se permutan las filas de X, se permuta la salida y nada más. La posición hay que agregarla a la entrada.**

| pos | dim 1 (sen) | dim 2 (cos) | dim 3 (sen) | dim 4 (cos) |
|---|---|---|---|---|
| 0 | 0 | 1 | 0 | 1 |
| 1 | 0,84 | 0,54 | 0,01 | 1,00 |
| 2 | 0,91 | -0,42 | 0,02 | 1,00 |
| 3 | 0,14 | -0,99 | 0,03 | 1,00 |

- **El paper suma un vector fijo de senos y cosenos:** PE(pos, 2i) = sen(pos / 10000^{2i/d}), PE(pos, 2i+1) = cos(·). Cada par de dimensiones es una sinusoide de distinta frecuencia; las de la izquierda cambian rápido, las de la derecha casi no cambian (con d = 4, la tercera y cuarta columna apenas se mueven).
- **Por qué sinusoides.** Para cualquier desplazamiento k, PE(pos + k) es una función lineal de PE(pos), así que el modelo puede aprender a atender por posición relativa. El paper conjetura que extrapolan a secuencias más largas que las del entrenamiento; en la práctica lo hacen mal, y eso motiva RoPE (sección 5).
- **Alternativas:** embeddings de posición aprendidos (BERT, GPT-2: una tabla de 512 o 1024 filas, iguales en calidad según el paper) y RoPE, que rota Q y K en vez de sumar un vector; la usan los LLM actuales (sección 5).

### Sources

- `attention-is-all-you-need.html.md` (§3.5, eq. de PE): "Since our model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position"; longitudes de onda de 2π a 10000·2π; "for any fixed offset k, PE_{pos+k} can be represented as a linear function of PE_{pos}"; Table 3 (E): embeddings aprendidos dan "nearly identical results".
- `bert-devlin-2018.html.md` (§3): position embeddings aprendidos, máximo 512. `gpt2-radford-2019.pdf.md`: contexto de 1024 tokens (`wpe` en el código).
- Ejemplo propio: PE con d = 4 para posiciones 0 a 3.

### Speaker notes

La justificación se demuestra, no se afirma: pedí que imaginen X con las filas de "cat" y "sat" intercambiadas y sigan la cuenta de la sección 2. Q Kᵀ queda con filas y columnas intercambiadas, el softmax por fila da lo mismo permutado, y A·V devuelve las mismas filas en otro orden. El modelo no puede distinguir "the cat sat on" de "on sat cat the". La tabla muestra el truco del paper con d = 4, que es demasiado chico para verlo bien (las dos columnas de la derecha casi no se mueven); con d = 512 hay 256 frecuencias entre las dos. No entres en RoPE acá. Tiempo objetivo: ~4 min.

**Presenter feedback:**
los embeddings posicionales se tienen que explicar tambien desde el principio, antes de empezar a hablar sobre cómo se obtiene la matriz de atención 
---

## 6. Cuenta de parámetros de un bloque

### Content

**Un bloque tiene unos 12 d² parámetros: 4 d² en la atención y 8 d² en la feed-forward. Con eso se reconstruyen los tamaños de los modelos conocidos.**

| | Fórmula | Paper 2017 (d = 512, N = 6) | GPT-2 chico (d = 768, N = 12) |
|---|---|---|---|
| **Atención por bloque** | 4 d² (Wq, Wk, Wv, Wo) | 1,05 M | 2,36 M |
| **Feed-forward por bloque** | 8 d² (d × 4d, 4d × d) | 2,10 M | 4,72 M |
| **N bloques de encoder** | 12 N d² | 18,9 M | 84,9 M (decoder-only) |
| **N bloques de decoder** | 16 N d² (suma la cross-attention) | 25,2 M | no tiene |
| **Embeddings** | \|V\| · d (+ posiciones) | 37k · 512 = 19 M | 50.257 · 768 = 38,6 M |
| **Total aprox.** | | ~63 M (paper: 65 M) | ~124 M |

- **Los bloques suman 12 N d².** Es la fórmula de Kaplan y otros para los parámetros sin contar embeddings; con ella se estima cualquier modelo del que se conozcan d y N.
- **La tabla de embeddings es grande en modelos chicos y despreciable en los grandes.** En GPT-2 chico es un tercio del total; en un modelo con d = 12.288 y 96 bloques, los bloques son 174.000 M y los embeddings 600 M.
- **Los cientos de miles de millones de parámetros de un LLM** son 12 N d² con d y N grandes.

### Sources

- `scaling-laws-kaplan-2020.html.md` (§2.1, Table 1): N ≈ 2·d_model·n_layer·(2·d_attn + d_ff) = 12·n_layer·d_model² para d_attn = d_ff/4 = d_model; embeddings (n_vocab + n_ctx)·d_model.
- `attention-is-all-you-need.html.md` (Table 3): modelo base 65 M parámetros; vocabulario BPE compartido de ~37.000 tokens (§5.1).
- `gpt2-radford-2019.pdf.md` (Table 2): 117 M declarados para el modelo chico; `gpt2-to-kimi3-waterloo-intern.md.md`: "about 124M parameters" con 12 bloques, 12 cabezas y 768 dimensiones (la cifra corregida, ver Inconsistencies del corpus).
- Cálculo propio: 12·12·768² = 84,9 M; 50.257·768 = 38,6 M; 1024·768 = 0,8 M.

### Speaker notes

La lámina cierra la sección con una cuenta que cualquiera puede repetir y que resuelve una pregunta que quedó abierta la clase pasada ("del orden de cientos de miles de millones", sin fuente). El ejemplo de d = 12.288 y 96 capas es la configuración publicada de GPT-3 175B; da 174 mil millones con la fórmula, y el resto son embeddings. Los 63 M contra los 65 M del paper: la diferencia son sesgos, layer norms y el redondeo del vocabulario; el decoder suma 4 d² más por bloque por la cross-attention, y por eso su fila es 16 N d². Alcanza con que el orden dé. Tiempo objetivo: ~3 min.

**Presenter feedback:**

---

# 4. Encoder, decoder y la familia

**Goal of this section:** Mostrar cómo se apilan los bloques en las dos columnas del paper, por qué los LLM se quedaron con el decoder y BERT con el encoder, y el mapa de arquitecturas y modelos derivados que la práctica va a usar. Seis láminas.

**Presenter feedback:**

---

## 1. Las dos columnas de 2017

### Content

<!-- design: split-left -->

![Figura 1 del paper de Vaswani y otros, la misma que se proyectó la clase pasada](images/arquitectura-transformer.jpg)

**El paper apila 6 bloques de encoder y 6 de decoder. El decoder tiene una tercera subcapa, la cross-attention, donde las consultas vienen del decoder y las claves y valores del encoder.**

```ascii
     ENCODER (x6)                    DECODER (x6)
  +-------------------+          +-----------------------+
  |  self-attention   |          |  self-attention       |
  |  (sin mascara)    |          |  CON mascara causal   |
  |        +          |          |          +            |
  |  feed-forward     |   K,V    |  cross-attention      |
  |                   | -------> |  Q del decoder,       |
  +-------------------+          |  K y V del encoder    |
          ^                      |          +            |
          |                      |  feed-forward         |
   frase de entrada              +-----------------------+
   "the cat sat on"                        ^      |
                                           |      v
                                 salida generada hasta ahora   -> softmax |V|
```

- **Encoder:** lee la frase de entrada completa, cada token ve a todos. Produce una representación contextual por token.
- **Decoder:** genera la salida token a token con máscara causal, y en cada paso consulta al encoder con la cross-attention: la misma cuenta de la sección 2, con Q de un lado y K, V del otro.
- **Fue diseñado para traducir.** Entrada en un idioma, salida en otro; por eso dos columnas. Casi ningún modelo actual usa las dos.

### Sources

- `attention-is-all-you-need.html.md` (§3.1, §3.2.3): encoder de N = 6 capas con dos subcapas, decoder de N = 6 con tres; "In 'encoder-decoder attention' layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder".
- `talks/palabra-al-transformer/final.md` (6.1): la figura 1 del paper que ya vieron; este diagrama es su versión en cajas con las tres subcapas nombradas.

### Speaker notes

Es la figura que vieron la clase pasada, ahora con nombres en cada caja porque ya saben qué hay adentro. Lo nuevo es la cross-attention, y la justificación es simple: es la misma fórmula con Q de una secuencia y K, V de otra; es el mecanismo por el que el decoder "lee" la frase de origen. La tercera viñeta prepara las dos láminas siguientes. Tiempo objetivo: ~3 min.

**Presenter feedback:**

---

## 2. Solo el decoder: GPT

### Content

**GPT-2 es la columna derecha sola, sin cross-attention: bloques de self-attention con máscara causal más feed-forward, y un softmax sobre el vocabulario arriba. Es la arquitectura de casi todos los LLM actuales.**

- **Por qué alcanza con el decoder.** Si la tarea es "predecir el token siguiente", entrada y salida son la misma secuencia: no hay una frase de origen aparte que codificar. El prompt y la respuesta van en el mismo flujo, y la máscara causal garantiza que cada token solo vea lo anterior.
- **Cuatro tamaños en 2019:** 117 M (12 capas, d = 768), 345 M (24, 1024), 762 M (36, 1280), 1.542 M (48, 1600). El más chico tiene el tamaño del GPT original; el segundo, el de BERT-large. Todos con contexto de 1024 tokens.
- **La tesis del paper:** entrenado solo con next-token sobre 40 GB de texto de la web, el modelo hace tareas para las que nadie lo entrenó (traducción, resumen, preguntas) si se le describe la tarea en el prompt. Es el origen del prompting (clase 5).

### Sources

- `gpt2-radford-2019.pdf.md` (§2.3, Table 2): arquitectura "largely follows the details of the OpenAI GPT model" (decoder-only), pre-LN, vocabulario 50.257, contexto 1024; los cuatro tamaños; "language models begin to learn these tasks without any explicit supervision"; WebText 40 GB.
- `gpt2-to-kimi3-waterloo-intern.md.md`: "GPT-2 is a decoder-only architecture", código de `forward` con `wte`, `wpe`, `h` (bloques) y `lm_head`.
- `talks/palabra-al-transformer/final.md` (6.1, notas): la afirmación "los LLM modernos usan solo decoder" quedó allí como aporte propio sin fuente; acá tiene fuente (GPT-2 y el artículo de Kimi K3).

### Speaker notes

La justificación de "solo decoder" es la primera viñeta y es conceptual, no de ingeniería: cuando entrada y salida son la misma cadena de texto, el encoder no tiene qué codificar. La tabla de tamaños sirve para que vean que 1,5 mil millones era "enorme" en 2019 y hoy es un modelo de celular. La tercera viñeta cierra el círculo con la clase de prompting. Tiempo objetivo: ~3 min.

**Presenter feedback:**

---

## 3. Solo el encoder: BERT

### Content

**BERT es la columna izquierda sola: bloques sin máscara, cada token ve la frase entera. No genera texto; produce una representación contextual por token, y la práctica usa esa representación para RAG.**

- **Sin máscara, el next-token no sirve** (cada token vería la respuesta). BERT se entrena tapando el 15 % de los tokens y prediciéndolos desde ambos lados (*masked language model*), con una tarea auxiliar: decidir si una frase sigue a otra.
- **Dos tamaños:** BERT-base, 12 capas, d = 768, 12 cabezas, 110 M (elegido para igualar al GPT original); BERT-large, 24 capas, d = 1024, 16 cabezas, 340 M. Entrada: tokens WordPiece (30k) + embedding de segmento + embedding de posición aprendido, máximo 512.
- **Cómo se usa:** se agrega una capa de salida y se ajusta entero para la tarea (clasificación, respuesta a preguntas), o se toman las representaciones de las últimas capas como vectores fijos. Con solo la última opción, BERT pierde apenas 0,3 F1 en reconocimiento de entidades contra ajustarlo entero.

### Sources

- `bert-devlin-2018.html.md` (§3, §3.1, §5.3): "a multi-layer bidirectional Transformer encoder"; MLM con 15 % de tokens (80 % [MASK], 10 % aleatorio, 10 % sin cambio) y NSP; tamaños BASE y LARGE; entrada = token + segmento + posición; feature-based 96,1 F1 en CoNLL-NER, "only 0.3 F1 behind fine-tuning the entire model".

### Speaker notes

La justificación de la máscara al revés: si nadie enmascara la atención, hay que enmascarar la entrada, porque de lo contrario predecir el token siguiente es copiarlo. Eso es el MLM. Para la práctica lo que importa es la tercera viñeta: BERT como fábrica de vectores contextuales. Pero ojo con la lámina que sigue: los vectores crudos de BERT son malos embeddings de oración, y hay que decirlo antes de que alguien los use así. Tiempo objetivo: ~3 min.

**Presenter feedback:**

---

## 4. Del encoder al embedding de oración

### Content

**Para RAG hace falta un vector por fragmento, comparable por coseno. BERT crudo no lo da: promediar sus tokens es peor que promediar GloVe. Sentence-BERT lo arregla con pooling y un ajuste siamés.**

```ascii
   fragmento A  ->  [ BERT ]  -> tokens (n x d) -> POOLING (media) -> u (d)
                                                                       \
                                                                        coseno(u, v)
                                                                       /
   fragmento B  ->  [ BERT ]  -> tokens (n x d) -> POOLING (media) -> v (d)
                    (mismos pesos)
   entrenamiento: pares de frases etiquetadas (NLI, STS) para que
   coseno alto = significado parecido
```

- **El problema medido:** en STS, promediar los tokens de BERT da 54,8 y usar el vector [CLS] da 29,2; promediar GloVe da 61,3. BERT sin ajustar no sabe que dos frases se parecen.
- **La alternativa lenta:** meter las dos frases juntas en BERT (*cross-encoder*) funciona, pero comparar 10.000 frases entre sí son 50 millones de pasadas, unas 65 horas. Con embeddings, 5 segundos.
- **La solución:** una capa de pooling (la media de los tokens funciona mejor que [CLS] o el máximo) y ajuste con pares de frases para que el coseno refleje similitud. STS sube a 74,9 (base) y 76,6 (large). Es la idea de base de los modelos de embeddings actuales, que le suman objetivos contrastivos y más datos.

### Sources

- `sentence-bert-reimers-2019.html.md` (§1, §3, Table 1, Table 7, §7): "finding the most similar pair in a collection of 10,000 sentences requires about 50 million inference computations (~65 hours)"; media de tokens 54,81, CLS 29,19, GloVe 61,32; SBERT-NLI-base 74,89 y large 76,55; MEAN pooling mejor en la ablación; búsqueda "from 65 hours ... to about 5 seconds".

### Speaker notes

Esta lámina conecta la clase con la práctica de RAG y es la que justifica que "elegir el encoder" sea un hiperparámetro. La justificación del pooling: el encoder produce n vectores y la búsqueda necesita uno, así que hay que colapsar la secuencia, y la media resultó mejor que el token especial. La del ajuste siamés: el coseno solo sirve como similitud si el modelo fue entrenado para que lo sea; BERT fue entrenado para tapar palabras, no para eso. Los modelos de embeddings actuales (los que van a probar) son esta misma idea con más datos y objetivos contrastivos. Tiempo objetivo: ~3 min.

**Presenter feedback:**

---

## 5. Fuera del texto: ViT

### Content

**El bloque no sabe que procesa texto. Si una imagen se corta en parches y cada parche se proyecta a un vector, el mismo encoder clasifica imágenes: Vision Transformer.**

- **Cómo:** una imagen de 224 × 224 se corta en parches de 16 × 16 (196 parches), cada uno se aplana (16·16·3 = 768 valores) y se proyecta linealmente a d. Se agrega un token [class] al frente, como el [CLS] de BERT, y embeddings de posición aprendidos. Después, un encoder estándar con pre-LN.
- **Menos sesgo inductivo.** Sin convoluciones no hay sesgo de localidad ni de traslación. Con pocos datos rinde peor que una ResNet; con 14 M o 300 M de imágenes de preentrenamiento la supera (88,55 % en ImageNet) con menos cómputo.
- **Tamaños calcados de BERT:** ViT-Base 12 capas, d = 768, 86 M; ViT-Large 24, 1024, 307 M; ViT-Huge 32, 1280, 632 M. "ViT-L/16" quiere decir Large con parches de 16.

### Sources

- `vit-dosovitskiy-2020.html.md` (§3.1, §4.2, §4.3, Table 1-2): "the standard Transformer receives as input a 1D sequence of token embeddings"; parches de P² · C, proyección E, token [class], position embeddings 1D aprendidos; pre-LN (eq. 1-4); menos sesgo inductivo, peor con ImageNet solo, mejor con ImageNet-21k y JFT-300M; ViT-H/14 88,55 % ImageNet con 2,5k TPUv3-core-days contra 9,9k de BiT-L.

### Speaker notes

Lámina de una idea: el transformer es agnóstico a la modalidad porque lo único que ve son filas de una matriz. La justificación de por qué necesita más datos es la que vale: las CNN traen de fábrica que los píxeles vecinos se relacionan y que un gato a la izquierda es el mismo gato que a la derecha; el transformer tiene que aprender eso de los datos. Es una lámina de contexto; no se profundiza. Tiempo objetivo: ~2 min.

**Presenter feedback:**

---

## 6. El mapa de la familia

### Content

**Tres formas de apilar el mismo bloque, y qué modelo va con cada tarea.**

| | Encoder-only | Decoder-only | Encoder-decoder |
|---|---|---|---|
| **Máscara** | ninguna: cada token ve todo | causal: solo lo anterior | encoder sin máscara, decoder con máscara y cross-attention |
| **Objetivo de entrenamiento** | tapar tokens y predecirlos (MLM) | predecir el token siguiente | secuencia de entrada a secuencia de salida |
| **Produce** | una representación por token | texto, token a token | texto, condicionado a una entrada aparte |
| **Modelos** | BERT, RoBERTa, Sentence-BERT, los modelos de embeddings, ViT | GPT-2 y sucesores, Llama, DeepSeek, Kimi | el transformer de 2017, T5, BART, Whisper |
| **En la práctica** | el encoder del RAG vectorial | el agente que responde y llama herramientas | no se usa |

- **La regla práctica:** cuando la salida es un vector se usa un encoder; cuando es texto, un decoder. Encoder-decoder sobrevive en traducción, resumen y audio, donde la entrada es de otra naturaleza que la salida.
- **Todos comparten el bloque de la sección 3.** Cambian la máscara, el objetivo de entrenamiento y la salida que se lee.

### Sources

- `bert-devlin-2018.html.md` (nota 4): encoder vs decoder según el contexto que se permite ver.
- `gpt2-radford-2019.pdf.md`, `sentence-bert-reimers-2019.html.md`, `vit-dosovitskiy-2020.html.md`, `deepseek-v2-mla-2024.html.md`, `gpt2-to-kimi3-waterloo-intern.md.md`: cada fila de modelos según su propio paper. T5, BART, Whisper, RoBERTa y Llama se nombran como conocimiento general del área, no están en el corpus (ver Open questions).

### Speaker notes

Lámina de repaso de la sección, y la que hay que dejar en pantalla mientras se presenta la práctica: el encoder del ejercicio 1 está en la primera columna y el agente del ejercicio 2 en la segunda. La regla práctica de la primera viñeta es la que importa. Si alguien pregunta por qué no usar un LLM decoder-only como encoder de embeddings: se puede, y hay modelos de embeddings hechos así, pero un token de decoder solo vio lo anterior, así que hay que tomar el último o ajustar el modelo para que mire todo. Tiempo objetivo: ~3 min.

**Presenter feedback:**

---

# 5. Lo que cambió desde 2017

**Goal of this section:** Presentar las variantes modernas del bloque como respuestas a cuellos de botella concretos, solo a nivel de idea: qué problema atacan y qué cambian. Cada una se abre en la clase siguiente. Cinco láminas.

**Presenter feedback:**

---

## 1. El cuello de botella es la matriz n por n

### Content

**Casi todo lo que cambió desde 2017 ataca el mismo lugar: la tabla de atención de n por n de la sección 2 y la memoria para guardar K y V durante la generación.**

| Cuello de botella | Dónde aparece | Respuesta | Clase |
|---|---|---|---|
| Recomputar K y V de todos los tokens anteriores en cada paso de generación | inferencia | KV cache | hoy |
| El KV cache ocupa más memoria que los pesos con contextos largos | inferencia | MQA, GQA, MLA | hoy |
| Leer y escribir la matriz n × n en memoria lenta | entrenamiento e inferencia | FlashAttention | hoy |
| La posición sumada no generaliza a contextos más largos | ambas | RoPE | hoy |
| La feed-forward es la mayoría de los parámetros y no todo token la necesita entera | ambas | Mixture of Experts | hoy |
| La atención sigue siendo O(n²) por más rápida que sea | ambas | atención lineal, DeltaNet, híbridos | clase 9 |

- **Ninguna cambia la matemática de la sección 2.** KV cache, GQA, FlashAttention y MLA calculan la misma atención con menos memoria o menos tráfico; RoPE cambia cómo entra la posición y MoE cambia la feed-forward. La atención lineal sí cambia la fórmula (clase 9).

### Sources

- `attention-is-all-you-need.html.md` (Table 1): complejidad por capa O(n²·d).
- `gpt2-to-kimi3-waterloo-intern.md.md`: el recorrido de GPT-2 a Kimi K3, del que esta tabla toma el orden de los problemas.
- Los papers de cada fila están citados en las láminas siguientes.

### Speaker notes

Lámina índice de la sección. Lo único que hay que decir es la viñeta: cuatro de las cinco variantes de hoy no tocan la fórmula, solo la implementan mejor, y por eso se pueden contar en una lámina cada una. Anticipá que la clase que viene arranca en la última fila, con el artículo de GPT-2 a Kimi K3 como guía. Tiempo objetivo: ~2 min.

**Presenter feedback:**

---

## 2. KV cache y GQA: guardar claves y valores, y compartirlos

### Content

**Al generar, cada token nuevo solo necesita su propia consulta contra las claves y valores de todos los anteriores, que no cambian. Se guardan (KV cache) y el costo baja de recomputar todo a una fila por paso. El precio es memoria, y GQA la reduce compartiendo K y V entre cabezas.**

```ascii
  paso t:  tokens 1..t-1 ya tienen K y V guardados
                                 K cache (t-1 x d)   V cache (t-1 x d)
   token t -> q_t (1 x d) ---->  q_t K^T  -> softmax -> . V  -> salida_t
                                   |
                                   +--> k_t, v_t se agregan al cache
  sin cache: recalcular Q, K, V de los t tokens en cada paso  (t x d)
  con cache: una fila nueva por paso                        (1 x d)
  memoria del cache: 2 x capas x cabezas x d_cabeza x t
```

- **Por qué funciona.** Con máscara causal, las filas de K y V de los tokens anteriores no dependen del token nuevo: son las mismas en el paso t y en el t+1. Lo único nuevo es la consulta del último token.
- **Por qué tarda el primer token.** El *prefill* procesa el prompt entero de una vez (n × n); los tokens siguientes son una fila cada uno. El tiempo hasta el primer token crece con el prompt; el resto no.
- **GQA:** en lugar de una K y una V por cabeza, varias cabezas de consulta comparten una misma K y V. Con 8 grupos, T5-XXL genera en 0,28 s por muestra contra 1,51 s con todas las cabezas, con la misma calidad. Llama y casi todos los modelos abiertos usan GQA. MLA (DeepSeek) va más lejos: guarda un vector comprimido por token y reconstruye K y V; su cache equivale al de GQA con 2,25 grupos y rinde mejor que MHA.

### Sources

- `gpt2-to-kimi3-waterloo-intern.md.md`: "The KV cache comes from a straightforward observation: after appending the generated token to the input, the model would otherwise recompute projections for all previous tokens. Storing their key and value vectors avoids that redundant work"; "can become large enough to create a memory-bandwidth bottleneck"; código con `past_kv` y prefill vs decode.
- `gqa-ainslie-2023.html.md` (§1, §2.2, Table 1): "memory bandwidth overhead from loading keys and values"; grupos de cabezas de consulta que comparten una cabeza de K y V; MHA-XXL 1,51 s y 47,2 de promedio, GQA-8-XXL 0,28 s y 47,1; KV cache H/G veces menor.
- `deepseek-v2-mla-2024.html.md` (§2.1.2, Table 1): latente comprimido c_t^{KV} por token, "reduces the KV cache by 93.3%", equivalente a GQA con 2,25 grupos pero mejor que MHA.

### Speaker notes

La justificación de la KV cache sale directo de la máscara causal de la lámina 2.6: si la fila de "cat" no puede ver a "sat", entonces la K y la V de "cat" no cambian cuando aparece "sat", y no tiene sentido recalcularlas. La segunda viñeta explica una experiencia que todos tuvieron con un chat: la pausa antes de la primera palabra y la velocidad después. La fórmula de memoria del diagrama es la que hay que hacer una vez con números: Llama-2 70B, 80 capas, 8 grupos KV de 128, 16 bits, son 2·80·8·128·2 bytes = 320 KB por token; 100k tokens de contexto son 32 GB solo de cache. GQA se cuenta como "compartir", MLA como "comprimir", y ahí se termina. Tiempo objetivo: ~4 min.

**Presenter feedback:**

---

## 3. FlashAttention: la misma atención por bloques

### Content

**La atención estándar escribe la matriz n × n en la memoria principal de la GPU y la vuelve a leer para el softmax y para multiplicar por V. FlashAttention calcula por bloques que caben en la memoria rápida del chip y nunca materializa la matriz. El resultado es exacto y hasta 3 veces más rápido según hardware y forma.**

- **El diagnóstico:** en una A100, la memoria principal (HBM) mueve 1,5 a 2 TB/s; la memoria del chip (SRAM), 19 TB/s pero solo 192 KB por multiprocesador. El tráfico de memoria limita a la atención antes que la cantidad de operaciones.
- **El método:** partir Q, K y V en bloques, calcular la atención bloque por bloque en SRAM, y combinar los softmax parciales de forma exacta llevando un máximo y una suma corrientes (*online softmax*). Para el gradiente, recalcular los bloques en vez de guardarlos.
- **Resultados:** hasta 3× sobre la implementación de GPT-2 de HuggingFace y 1,7 a 1,8× sobre Megatron-LM, memoria lineal en n en vez de cuadrática, y contextos de 16k tokens con la versión exacta (64k con una variante por bloques dispersos, que ya no es exacta).

### Sources

- `flashattention-dao-2022.html.md` (§1, §2.1, §3.1, §4): "a missing principle is making attention algorithms IO-aware"; A100 con 40-80 GB de HBM a 1,5-2,0 TB/s y 192 KB de SRAM por cada uno de 108 SMs a ≈ 19 TB/s; tiling con online softmax (running max m y running sum ℓ) y recomputación en backward; Theorem 1: resultado exacto con O(N) memoria extra; hasta 3× sobre HuggingFace en GPT-2, Path-X (16K) y Path-256 (64K) resueltos por primera vez.

### Speaker notes

La justificación es de arquitectura de computadoras, y a ingenieros de software les va a gustar: el problema no era cuántas multiplicaciones, era cuántas veces se lee y escribe la RAM de la GPU. El softmax por bloques es la parte no obvia: parece que necesitás la fila entera para normalizar, pero podés llevar el máximo y la suma parciales y corregir al final; es un truco de dos líneas que vale la pena mostrar en la clase que viene. Lo que hay que dejar claro hoy es que el resultado es idéntico y no una aproximación, y que el 2 a 4× que se cita a veces es la variante dispersa contra FlashAttention, no FlashAttention contra el estándar. Tiempo objetivo: ~3 min.

**Presenter feedback:**

---

## 4. RoPE: la posición como rotación

### Content

**En vez de sumar un vector de posición al embedding, RoPE rota Q y K un ángulo proporcional a la posición. El producto punto entre una consulta en la posición m y una clave en la n depende entonces solo de la distancia m − n.**

- **La idea en dos dimensiones:** el vector (x, y) de la posición m se rota un ángulo m·θ. Rotar q en m·θ y k en n·θ y hacer el producto punto equivale a rotar uno de ellos (m − n)·θ. Solo queda la posición relativa.
- **En d dimensiones:** el vector se parte en d/2 planos, cada uno con su frecuencia θ_i = 10000^{-2i/d} para i = 0 … d/2 − 1, las mismas frecuencias de la lámina 3.5 pero multiplicando en vez de sumando. Se implementa sin matrices, con senos y cosenos elemento a elemento.
- **Por qué se impuso.** Es relativa por construcción, no agrega parámetros, decae con la distancia y se puede estirar a contextos más largos que los del entrenamiento. Llama, DeepSeek, Kimi y casi todos los LLM actuales la usan.

### Sources

- `rope-su-2021.html.md` (§3.1-3.4): objetivo ⟨f_q(x_m, m), f_k(x_n, n)⟩ = g(x_m, x_n, m − n) (eq. 11); rotación por e^{imθ} en 2D (eq. 12-13); d/2 planos con θ_i = 10000^{-2(i-1)/d} (eq. 14-15); q_mᵀ k_n = x_mᵀ W_q R_{Θ,n−m} W_k x_n (eq. 16); realización elemento a elemento (eq. 34); decaimiento con la distancia (§3.4.3); WMT14 27,5 vs 27,3 BLEU (Table 1).
- `deepseek-v2-mla-2024.html.md` (§2.1.3): RoPE como matriz dependiente de la posición entre W^Q y W^{UK}, y el "decoupled RoPE" que MLA necesita para poder comprimir.

### Speaker notes

La justificación es la de la lámina 3.5 llevada un paso más lejos: sumar posición absoluta obliga al modelo a aprender solo la relativa; rotar se la da gratis. El argumento de la rotación en 2D se puede hacer en el pizarrón en un minuto con un ángulo: dos vectores rotados el mismo ángulo mantienen su producto punto, así que rotarlos ángulos distintos deja solo la diferencia. Es la única lámina de la sección con una fórmula, y va porque la práctica de la clase siguiente la implementa. Tiempo objetivo: ~3 min.

**Presenter feedback:**

---

## 5. Mixture of Experts: varias feed-forward y un router

### Content

**La feed-forward es dos tercios de los parámetros y todo token la atraviesa entera. MoE reemplaza esa red por varias (expertos) y un router que elige unas pocas por token. El modelo tiene muchos más parámetros de los que usa en cada paso.**

```ascii
                token h_t
                    |
             [ router: softmax(h_t . e_i) ]  -> elige top-K expertos
                    |
     +--------------+--------------+----------------+
     |              |              |                |
  experto 3     experto 17      ... (K elegidos)   expertos compartidos
  FFN_3(h_t)    FFN_17(h_t)                        (siempre activos)
     |              |                               |
     +------ suma pesada por la afinidad -----------+
                    |
                 salida
```

- **Los números de DeepSeek-V2:** 236 mil millones de parámetros totales, 21 mil millones activos por token; 2 expertos compartidos y 160 ruteados, de los que cada token usa 6.
- **Por qué.** El costo por token depende de los parámetros activos y la capacidad de los totales. Un MoE de DeepSeek-V2 cuesta como un modelo de 21 B y rinde como uno mucho más grande. El precio es memoria, porque todos los expertos tienen que estar cargados, y balance, porque el router tiende a mandar todo a los mismos expertos y hay que corregirlo con pérdidas auxiliares.
- **Los expertos compartidos** procesan todos los tokens y aprenden lo común. Los ruteados se especializan.

### Sources

- `deepseek-v2-mla-2024.html.md` (§1, §2.2, §3.1.2, eq. 20-22): 236 B totales, 21 B activados; h'_t = u_t + Σ FFN_shared + Σ g_{i,t} FFN_routed con afinidades softmax(u_tᵀ e_i) y top-K_r; 2 compartidos + 160 ruteados, 6 activos por token; pérdidas de balance por experto, por dispositivo y de comunicación.
- `gpt2-to-kimi3-waterloo-intern.md.md`: Kimi K3 con 898 expertos, 2 compartidos, 16 de 896 elegidos por token; la primera capa densa y el resto latent MoE.

### Speaker notes

La justificación se apoya en la cuenta de la lámina 3.6: si la FFN es 8d² de los 12d² del bloque, ahí es donde conviene poner capacidad sin pagarla en cada token. El router es un softmax sobre productos punto, o sea, otra atención: el token consulta a los expertos. Según el artículo de Kimi K3 (sin verificar contra el reporte técnico), ese modelo tiene 898 expertos, 2 compartidos y 16 de 896 por token. Con eso alcanza; cómo se balancea y cómo se distribuye en máquinas es de la clase que viene. Tiempo objetivo: ~3 min.

**Presenter feedback:**

---

# 6. Entrenamiento a vuelo de pájaro

**Goal of this section:** Cerrar con qué se minimiza al entrenar, cómo escala la pérdida con tamaño, datos y cómputo, y qué sale de ahí. Dos láminas.

**Presenter feedback:**

---

## 1. Qué se minimiza

### Content

**La pérdida es la cross-entropy entre la distribución que el modelo produce sobre el vocabulario y el token que seguía en el texto. Con la máscara causal, cada posición de cada frase es un ejemplo.**

- **Para una posición:** el modelo da p(token) para los |V| tokens; la pérdida es −log p(token correcto). Si le dio 0,5 al correcto, 0,69; si le dio 0,01, 4,6. Se promedia sobre todas las posiciones del batch.
- **Por qué cross-entropy.** Es derivable respecto de los logits y castiga más cuanto menos probabilidad le dio al token correcto. Su mínimo es la entropía del texto, que es mayor que cero porque después de una frase hay varios tokens posibles.
- **Escala de los entrenamientos:** el modelo base de 2017, 100k pasos y 12 horas en 8 GPU P100; el grande, 300k pasos y 3,5 días. GPT-2: 40 GB de texto. BERT: 3.300 millones de palabras, 4 días en 4 Cloud TPU (16 chips).

### Sources

- `attention-is-all-you-need.html.md` (§5.3, §5.4, §6.1): Adam con β1 = 0,9, β2 = 0,98, ε = 10⁻⁹; lr = d_model^{-0,5} · min(step^{-0,5}, step · warmup^{-1,5}) con 4.000 pasos de warmup; dropout 0,1; label smoothing 0,1; base 100k pasos ≈ 12 h, big 300k ≈ 3,5 días en 8 P100.
- `gpt2-radford-2019.pdf.md` (§2.1): WebText, 40 GB. `bert-devlin-2018.html.md` (§3.1, A.2): BooksCorpus + Wikipedia, 3.300 M de palabras, 1 M pasos, 4 días en 4 Cloud TPU (BASE).
- `scaling-laws-kaplan-2020.html.md` (§1): pérdida en nats por token.

### Speaker notes

Retoma "aprender es ajustar parámetros" de la clase pasada con la función concreta. La justificación de la cross-entropy: es la que vieron para clasificación en la clase de redes, con |V| clases. El punto de la segunda viñeta merece la frase: el mínimo no es cero porque después de "the cat sat on the" hay varios tokens razonables, y ningún modelo puede saber cuál iba. Los números de la tercera viñeta son para dar escala. Tiempo objetivo: ~2 min.

**Presenter feedback:**

---

## 2. Las leyes de escala

### Content

**Con la misma arquitectura, la pérdida baja como una ley de potencia con los parámetros, los datos y el cómputo, a lo largo de siete órdenes de magnitud. La forma del modelo (profundo o ancho) casi no importa comparada con el tamaño.**

- **Las tres leyes de Kaplan (2020):** L(N) ∝ N^{-0,076} con N los parámetros sin embeddings; L(D) ∝ D^{-0,095} con D los tokens; L(C) ∝ C^{-0,050} con C el cómputo. Rectas en escala log-log.
- **Qué implica.** Se puede predecir la pérdida de un modelo grande entrenando chicos. Con presupuesto fijo, conviene un modelo grande entrenado poco antes que uno chico entrenado hasta converger. Chinchilla (2022) corrigió la receta hacia más datos por parámetro, pero la forma de ley de potencia quedó.
- **Los cientos de miles de millones de parámetros y los meses sobre miles de GPU** son el punto de la curva al que cada laboratorio decidió llegar.

### Sources

- `scaling-laws-kaplan-2020.html.md` (§1.2, eq. 1.1-1.3, §1.1, Appendix C): α_N ≈ 0,076, α_D ≈ 0,095, α_C^{min} ≈ 0,050; "some trends spanning more than seven orders of magnitude"; forma del modelo con efecto mínimo; con cómputo fijo, "train very large models and stop well short of convergence"; nota del corpus: Chinchilla (2022) revisó la asignación óptima hacia más datos.

### Speaker notes

Última lámina de contenido y la que explica la economía del campo en una curva. La justificación de "por qué escalar" no es filosófica: la pérdida baja de forma predecible, así que gastar más da un modelo mejor con una certeza que casi ninguna otra inversión de ingeniería tiene. Mencioná Chinchilla en una frase (más tokens por parámetro que lo que Kaplan decía) y no entres. Cerrá volviendo a la fórmula 12Nd² de la lámina 3.6: escalar es elegir N y d más grandes en esa fórmula. Tiempo objetivo: ~3 min.

**Presenter feedback:**

---

# Conclusiones

**Goal of this section:** Una lámina de resumen con el enganche con la práctica y con la clase siguiente.

**Presenter feedback:**

---

## 1. Un bloque repetido

### Content

**Un transformer es un bloque repetido. En el bloque, la atención mezcla entre tokens y la feed-forward procesa cada token. Con eso se lee cualquier modelo actual.**

- **La atención, en una línea:** softmax(Q Kᵀ / √d_k) V. Tres proyecciones, una afinidad, una escala, una distribución y una mezcla. Con máscara causal genera texto; sin máscara produce representaciones.
- **El bloque:** varias cabezas, feed-forward de 4d con la única no linealidad por posición, residuales para que el gradiente llegue a las primeras capas, layer norm para mantener la escala, posición porque la atención no sabe el orden. Unos 12 d² parámetros por bloque.
- **La familia:** encoder para vectores (BERT, el encoder de la práctica), decoder para texto (GPT y casi todos los LLM), las dos columnas para traducción, resumen y audio. ViT es el mismo encoder con parches.
- **Lo que cambió desde 2017** ataca la matriz n × n y el KV cache sin tocar la fórmula. La atención lineal y sus derivados hasta Kimi K3 sí la cambian, y son el tema de la clase 9.
- **La práctica:** un RAG con encoder elegido y evaluado, un agente con ese RAG y tool-use, las herramientas como servidor MCP, una capa de atención en NumPy, y una hoja con las cuentas de la atención y del bloque hechas a mano, con la justificación de cada operación.

### Sources

- Síntesis de la charla; sin fuentes nuevas.

### Speaker notes

Lámina de cierre; se lee de arriba abajo en dos minutos y se pasa a presentar la práctica. La última viñeta es la consigna: el ejercicio a mano es la sección 2 y las láminas 3.3 y 3.4, con la frase de juguete u otra, y en cada paso una línea que diga para qué sirve esa operación. Tiempo objetivo: ~2 min.

**Presenter feedback:**

---

# Open questions

- T5, BART, Whisper, RoBERTa y Llama aparecen en el mapa de la familia (4.6) y GPT-3 175B en las notas de 3.6 como conocimiento general, sin registro en el corpus. Si se quiere fuente, capturar sus papers.
- La cuenta de memoria de KV cache para Llama-2 70B en las notas de 5.2 (80 capas, 8 grupos, d_cabeza 128) usa la configuración publicada por Meta; no está en el corpus.
- "Casi todos los LLM actuales usan RoPE y GQA" (5.2, 5.4) se afirma por conocimiento del área; el corpus solo lo documenta para DeepSeek-V2 y Kimi.
- El ejemplo de juguete usa Wq = identidad; conviene decidir si el ejercicio a mano de la práctica usa estas mismas matrices o pide a cada grupo elegir las suyas con la restricción de enteros chicos.
- Chinchilla (Hoffmann 2022) se menciona en 6.2 como corrección de Kaplan; no está en el corpus.
- GPT-2 con d_ff = 4d: el paper no lo declara; la lámina 3.2 lo sostiene solo para BERT. Verificar en el código de referencia si se quiere afirmar para GPT-2.
- Las cifras de expertos de Kimi K3 (898, 2 compartidos, 16 de 896) vienen del artículo de X y quedaron en notas de 5.5 hasta verificarlas contra el reporte técnico de Moonshot.
- "En la práctica extrapolan mal" sobre las sinusoides (3.5) es conocimiento del área; el paper de 2017 solo conjetura la extrapolación.
