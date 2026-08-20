---
presentation: Inteligencia Artificial Generativa (AI Gen)
class: "Modelado de un Multi-Layer Perceptron (MLP)"
research: research/corpus/
description: Slides are grouped into Sections. Each Section contains one or more Slides.
presenter: Paulo Veiga, Claudio Riguetti, Marco Sorondo (Universidad Austral)
audience: Estudiantes de grado de Ingeniería de Software con base técnica fuerte
duration: 90 min
date: 2026-08-19
---

# Thesis

**Claim:** El diseño de una red neuronal se decide casi entero en tres lugares: cómo se codifica la entrada, cómo se parte el dataset y cómo se modela la salida. El resto de la arquitectura sale del problema. Medir separando los tipos de error y frenar el overfitting con regularización es lo que separa un modelo que entrena de uno que sirve.

**Why it matters:** Una red no ve un cliente, una imagen ni un contrato: ve una fila de números. Si la información que importa quedó mal codificada, ninguna cantidad de capas la recupera, y la mayoría de los errores de producción en ML nacen en la frontera entre el dato crudo y el modelo. En el medio está la partición del dataset, que no cambia el modelo pero decide si la métrica dice la verdad: medir con los mismos datos con los que se entrenó es tomar examen con las respuestas a la vista. Del otro lado, un modelo con 99% de accuracy puede ser inútil y uno que ajusta perfecto en entrenamiento puede fallar en cada caso nuevo. Codificar bien, partir bien, modelar bien la salida, saber medir y saber regularizar cubre el 80% de las decisiones reales.

**Presenter feedback:**
- [closed] 2026-08-20 — "Y tal vez el titulo sea Modelado de Multi Layer Perceptron (para ser mas especifico)"
  Resolution: El campo class del frontmatter pasó de 'Diseño de redes neuronales: del dato a la predicción' a 'Modelado de un Multi-Layer Perceptron (MLP)'. Es el rótulo que el renderer pone en la portada bajo la materia.


---

# Agenda

**Narrative arc:** La clase sigue el recorrido de un dato a través de la red. Primero, qué se decide de verdad al diseñar (casi todo está en la entrada y la salida). Después el input en detalle: cómo un problema cualquiera se convierte en un vector de floats. Con el dato ya codificado, qué se hace con el dataset antes de entrenar: partirlo en tres, que es lo que vuelve honesta cualquier métrica posterior. Luego el output: cómo la tarea determina la última capa y su loss. Con la red ya armada, cómo se mide de verdad su desempeño con la matriz de confusión (accuracy sola no alcanza). Y para cerrar, el problema que arruina modelos que parecían buenos, el overfitting: cómo se diagnostica y cómo se trata, con L2 al frente del arsenal.

**Sections (in delivery order):**

- 1. Qué se diseña de verdad
- 2. Modelar la entrada
- 3. Partir el dataset
- 4. Modelar la salida
- 5. Medir un clasificador
- 6. Overfitting y regularización

**Presenter feedback:**
- [closed] 2026-08-19 — "En casi todos los slides es confusdo que no se define y en algunos caso se empieza con ejemplos." / "Lo que quise decir es que en los cards veo que se empieza definiendo ejemplo y no se define. No veo consistencia."
  Resolution: Se fijó una regla de card para todo el mazo y se barrieron las que no la cumplían. **La etiqueta en negrita nombra la cosa; la oración que sigue la define o la afirma; el ejemplo viene después de la definición, nunca antes.** Corregidas: 1.3 (la tercera card rompía el patrón término-definición de sus hermanas), 2.3 (la card de log abría con una lista de ejemplos), 2.5 (las cuatro abrían con el ejemplo y nunca definían el error), 4.3 (la de softmax abría con el ticket), 7.1 y 7.3 (etiquetas mezcladas entre pregunta, consecuencia y término; pasaron todas a sintagma nominal).

---

# 1. Qué se diseña de verdad

**Goal of this section:** Reencuadrar el diseño de una red y dar el vocabulario mínimo. La intuición del alumno suele estar en "cuántas capas, cuántas neuronas"; el mensaje es que esas decisiones importan poco y que el trabajo real está en cómo entra y cómo sale el dato. Deja cuatro cosas: que la forma del input la decide la arquitectura y que esta clase modela un MLP, cuáles son las seis decisiones que recorre la clase, qué es una neurona y su activación con las cuatro ocultas y sus formas, y de qué está hecho el vector de entrada.

**Presenter feedback:**
- [closed] 2026-08-20 — "Creo que tenemos que ser claros en el foco. La presentacion va a ser modelado MLP. Entonces, no hablamos mas de tensores por que es confuso. Es decir, los slide 2 al 5 (este nuevo es el 5) tienen que proveer este framing."
  Resolution: Se sacó el vocabulario de tensor del mazo entero: tesis, objetivo de la sección 1, título y apertura de la 1.1, título de la 2.6 y la 2.2. En su lugar, 'una fila de números'. Las diapositivas 1.2 a 1.5 quedaron como el bloque que fija el framing MLP, con la 1.5 nueva, y las activaciones ocultas pasaron a 1.6.


---

## 1. La red no ve el problema, ve una fila de números

### Content

Todo lo que entra a una red es una fila de números de largo fijo, todos del mismo tipo (float). Esa fila es el único acceso que la red tiene al problema.

- **Todo entra como números.** Un cliente, una máquina, una foto o un contrato llegan a la red como un vector de floats de tamaño fijo. La semántica original (que esto era una edad y aquello un barrio) desaparece en la codificación.
- **El input es una traducción.** Como toda traducción, puede perder cosas. Si la información que importa no quedó en esa fila, o quedó de una forma que borra su estructura, ninguna arquitectura la recupera después.
- **El error de codificación entra silencioso.** La red solo ve floats y no tiene forma de detectar que una posición "era un código" y otra "era una cantidad". Nadie recibe una excepción: el modelo entrena, converge y se equivoca.

<!-- template: quote -->
<!-- generate-image: right | la traducción frágil entre un mundo complejo y una fila de números, con información que puede perderse en el paso -->

### Sources

corpus/chat.md.md (§13 Las ideas de fondo; §2 El input: principio general)

### Speaker notes

Abrí con esto porque reordena toda la clase. La mayoría llega pensando que diseñar una red es elegir capas. Planteales la pregunta: ¿qué ve realmente la red cuando le pasás un cliente? La respuesta (un vector de números) es el hilo de las próximas dos secciones. Anclá la idea de "traducción con pérdida": es la que justifica por qué le vamos a dedicar 20 minutos a la entrada.

### Presenter feedback
- [closed] 2026-08-19 — "Ojo que no se definir tensor en ningun lado."
  Resolution: Se abrió la diapositiva con la definición de tensor (arreglo N-dimensional de floats, forma fija) y la escala escalar/vector/matriz/imagen, antes de los bullets.
- [closed] 2026-08-19 — "Codificar mal es fatal no es un buen titulo"
  Resolution: El bullet pasó de "Por eso codificar mal es fatal" a "El error de codificación entra silencioso", que describe el mecanismo en vez de calificarlo.

---

## 2. La forma del input la decide la arquitectura

### Content

La misma imagen de 28 por 28 píxeles entra a una red densa como una fila de 784 números y a una convolucional como una grilla de 28 por 28. La arquitectura decide qué forma necesita.

```ascii
            la misma imagen de 28 x 28, tres arquitecturas

  MLP (capa densa)         CNN (convolucional)      RNN / Transformer
  ----------------         -------------------      -----------------

  [ ][ ][ ] ... [ ]          +-------------+         [v1] [v2] ... [vT]
   1  2  3      784          |             |          t=1  t=2      t=T
                             |   28 x 28   |
  una fila de 784            |             |         una secuencia de
  numeros                    +-------------+         vectores, en orden

  hay que aplanarla          la grilla, intacta      el orden es el dato
```
<!-- ascii-note:
intent: mostrar que un mismo dato cambia de forma segun la arquitectura que lo recibe
emphasize: el contraste entre la fila aplanada del MLP y la grilla intacta de la CNN
labels: MLP fila de 784, CNN grilla 28 x 28, RNN/Transformer secuencia v1..vT
-->

| Arquitectura | Qué input espera | Por qué |
|---|---|---|
| MLP (densa) | Una fila de números de largo fijo | Cada neurona se conecta con todas las entradas, y la posición dentro de la fila no significa nada para ella |
| CNN | Una grilla: alto por ancho por color | La convolución necesita saber qué píxel está al lado de cuál |
| RNN / Transformer | Una secuencia de vectores | Cada paso es un vector y el orden entre pasos es parte del dato |

**Qué es un MLP.** Multi-Layer Perceptron, o perceptrón multicapa. Una capa de entrada, una o más capas ocultas donde cada neurona se conecta con todas las de la capa anterior (de ahí el nombre "densa", o *fully connected*), y una capa de salida. Es la arquitectura más simple y sigue siendo el bloque final de muchas CNN.

**El alcance de esta clase es el MLP.** Aplanar una imagen pierde qué píxel estaba al lado de cuál, y ese es el motivo por el que visión usa CNN. Acá el foco está en el MLP sobre datos tabulares, donde no hay ninguna vecindad que perder.

### Sources

corpus/chat.md.md (§2 El input: principio general — familias de estructura y su arquitectura natural)
784 = 28 × 28 — ejemplo aportado por el presentador (MNIST), no figura en el corpus

### Speaker notes

Esta diapositiva fija el alcance de la clase y conviene darla despacio, porque todo lo que sigue se apoya en ella. La pregunta que funciona antes de mostrarla: si les paso una foto de 28 por 28 en escala de grises, ¿cuántos números son? Respuesta, 784. Sirve para que dimensionen.

El punto que más rinde: la forma no es una propiedad del dato, es un requisito de la arquitectura. Una imagen es una grilla siempre; lo que cambia es si la red aprovecha esa grilla. Un MLP no tiene ningún mecanismo para saber que dos píxeles son vecinos, así que le da lo mismo el orden y por eso pide la fila aplanada.

Por si alguien pregunta si el aplanado es automático: no lo es. Una capa densa opera solo sobre el último eje (Keras: "Dense computes the dot product between the inputs and the kernel along the last axis"; PyTorch nn.Linear: "all but the last dimension are the same shape as the input"). Aplanar es una capa que uno pone, `Flatten()` en Keras o `nn.Flatten()` en PyTorch.

No te metas con cómo funciona una convolución ni con attention. Alcanza con que quede claro que existen, que esperan otra forma de input, y que de acá en adelante la clase modela un MLP sobre datos tabulares.

### Presenter feedback
- [closed] 2026-08-19 — "Borrar 'El lote es una dimensión más, siempre adelante. Un Dense(32) que recibe (B, 10) devuelve (B, 32): los mismos pesos se aplican a las B filas.'"
  Resolution: Se retiró la nota. El diagrama ya muestra la fila del lote con las cuatro formas, así que el texto la repetía; queda menos texto y el dibujo haciendo el trabajo. La indicación de mencionarlo al pasar sigue en las notas del orador, porque es la dimensión que aparece en todos los errores de shape.
- [closed] 2026-08-19 — "Confirmá esto con documentación formal sobre cómo modelar esto en un NN."
  Resolution: Verificado contra la documentación de Keras y PyTorch, y ejecutado en el venv de la misión. La nota anterior decía "se aplana" como si fuera automático y **eso estaba mal**: una capa densa opera solo sobre el último eje y no aplana sola. Keras: "If the input to the layer has a rank greater than 2, Dense computes the dot product between the inputs and the kernel along the last axis of the inputs". PyTorch nn.Linear: "Output: (*, H_out) where all but the last dimension are the same shape as the input". Aplanar es una capa explícita, Flatten() o nn.Flatten(). Medido: Dense(32) sobre (8,224,224,3) sin aplanar devuelve (8,224,224,32) con 128 parámetros, que es kernel (3,32) más bias; con Flatten() antes devuelve (8,32) con 4.816.928, que es kernel (150.528,32) más bias. El hallazgo confirma la card: el framework por defecto trata el eje de canal como el eje de variables. También valida el número del corpus, los 38,5M eran con 256 unidades.
- [closed] 2026-08-19 — "Pero si son tres números en el mismo píxel, ¿no se puede modelar la red?"
  Resolution: Sí se puede, y es exactamente la pregunta que va a hacer un alumno, así que quedó anticipada en las notas del orador. Para una red densa se aplana: los 224 por 224 por 3 se estiran en una fila de 150.528 floats y la red los trata como 150.528 variables sueltas, igual que las columnas de una tabla. Lo que se pierde al aplanar es que tres de esos números eran del mismo píxel y que dos píxeles eran vecinos: esa estructura vive en el dato, no en lo que la red usa. La respuesta refuerza la tesis de la clase, que la red ve un vector de floats, y deja claro que la forma importa para elegir arquitectura, no para poder modelar. No se agregó nada al contenido visible para no reintroducir el ruido de arquitecturas.
- [closed] 2026-08-19 — "Acá estamos no explicando redes convolucionales. El hablar de muchas capas produce ruido."
  Resolution: Se sacó todo lo convolucional. La card de señal ya no menciona Conv 1D, la de RGB ya no habla de reordenar (era la afirmación que arrastraba la explicación de Conv2D para tener sentido) y las notas del orador perdieron el párrafo de kernels, pesos compartidos y conteos de parámetros. Queda solo la forma del tensor, más una línea que aclara que el resto de la clase va sobre el caso tabular.
- [closed] 2026-08-19 — "El apilada no está bien."
  Resolution: Correcto, y era el peor error de la diapositiva. "Tres matrices apiladas" sugiere profundidad, o sea un tercer eje espacial, que es exactamente la confusión que la card quería corregir. Y el diagrama las dibujaba apiladas con desfase, reforzando el error. Ahora la card dice "la misma grilla, con tres números en cada píxel" y el diagrama muestra una sola grilla con un píxel ampliado que guarda R, G y B.
- [closed] 2026-08-19 — "'El canal no es espacial: son tres variables en el mismo punto, y se puede reordenar.' ¿No es verdad si es un DNN?"
  Resolution: La afirmación es cierta sobre el dato (el canal no tiene vecindad, alto y ancho sí), pero la card decía "se puede reordenar sin cambiar nada" sin decir respecto de qué, y ahí el comentario tiene razón: el contraste solo tiene consecuencias contra una Conv2D, que es la que trata alto y ancho como espacio al deslizar el mismo kernel. En un Dense sobre la imagen aplanada no hay ningún eje espacial y todas las posiciones son reordenables, las espaciales incluidas. La card pasó a decir que el canal es el único de los tres que se puede reordenar, que es lo preciso, y las notas del orador suman el matiz completo con los números del corpus: kernel 3×3 sobre RGB son 27 pesos y no 9; RGB 224×224 aplanada son 150.528 entradas y 38,5M de parámetros en la primera capa contra 896 de un Conv2d(3,32,3).
- [closed] 2026-08-19 — "Agregar después de 'La red no ve el problema, ve un tensor' cómo son estos tensores si vemos una señal 1D, imagen con un color, RGB y el input. Creo que lo mejor es que solo sea un slide con ASCII."
  Resolution: Nueva diapositiva 1.2 "Cómo se ve un tensor", con un solo diagrama que muestra los cuatro casos y su shape, de un eje a tres, más la dimensión de lote que se antepone en todos. Cuatro cards cortas, una por caso, y el canal RGB marcado como no espacial, que es el punto que menos se entiende. Las diapositivas 1.2 a 1.4 pasaron a 1.3 a 1.5.
- [closed] 2026-08-20 — "Que mencione que dependiendo de la arquitectura de la red neuronal, el tipo de dato a procesar. Que de ahora en adelante nos vamos a enfocar en MLP. Que es MLP?"
  Resolution: La 1.2 pasó de 'Cómo se ve un tensor' a 'La forma del input la decide la arquitectura'. Contrasta MLP, CNN y RNN/Transformer con la forma de input que espera cada una sobre el mismo ejemplo de 28x28, define qué es un MLP (perceptrón multicapa, capas densas, bloque final de muchas CNN) y declara el alcance de la clase. El diagrama nuevo reemplaza al de formas de tensor.


---

## 3. Lo que hay que diseñar

### Content

Diseñar un MLP son seis decisiones, y la que todos creen que es la principal, cuántas capas ponerle, es la que menos pesa. Son las seis que recorre esta clase, en este orden.

- **La entrada.** Cómo cada variable del problema se convierte en floats. Es donde se gana o se pierde el modelo, y donde más tiempo vamos a estar.
- **El dataset.** Cómo se parte antes de entrenar, en train, validación y test. Sin esto ninguna métrica posterior es honesta.
- **La salida.** Cuántas neuronas, qué activación y qué loss. No se elige: la determina la tarea. Predecir un precio pide salida lineal con MSE; clasificar en N clases, softmax con cross-entropy.
- **El error.** La distancia entre lo que el modelo predice y lo que de verdad pasó. Resumirla en un solo número es una decisión de diseño, y ningún número sirve para todos los casos.
- **# Capas & # Neuronas.** Cuántas capas ocultas y cuántas neuronas por capa. Es lo único de la lista que se elige libremente, y lo que menos impacto tiene.
- **El overfitting.** Cómo se detecta que el modelo memorizó en vez de aprender, y qué herramientas lo controlan.

**Nota:** 1 a 3 capas ocultas alcanzan para datos tabulares, ancho en potencias de 2 decreciente, ReLU salvo motivo. El retorno está en las otras cinco.

<!-- format: editorial -->

### Sources

corpus/chat.md.md (§9 Diseño de la red: qué se decide y qué no)

### Speaker notes

Este es el mapa mental que quiero que se lleven, y además es la agenda de la clase disfrazada de contenido: casi cada viñeta es una sección. Recorrelas señalando hacia adelante, sin desarrollar ninguna. El remate es la última línea: contrastá con la expectativa, pasan horas tuneando capas y el retorno está en la entrada. Dato honesto para dejar caer acá o al final: en datos tabulares una red muchas veces pierde contra gradient boosting (XGBoost, LightGBM); las redes brillan cuando hay estructura que explotar (imágenes, texto, señales). Sirve para bajar la sobreexpectativa.

### Presenter feedback
- [closed] 2026-08-19 — "Las capas y las neuronas -> # Capas & # Neuronas."
  Resolution: La card se renombró a "# Capas & # Neuronas". Al dejar de titularse como negación deja de ser el remate y pasa a ser un aspecto más de la lista, así que el cuerpo se reescribió: cuántas capas ocultas y cuántas neuronas por capa, lo único que se elige libremente y lo que menos impacto tiene.
- [closed] 2026-08-19 — "Overfitting ponelo al final."
  Resolution: La card del overfitting pasó al último lugar. La lista queda entrada, dataset, salida, error, # capas & # neuronas, overfitting. Se ajustaron el encabezado (de cinco decisiones a seis) y la nota al pie (de "las cinco de arriba" a "las otras cinco"), que con el reorden habrían quedado mintiendo.
- [closed] 2026-08-19 — "Con qué se mide que el modelo sirve. Accuracy sola engaña; la matriz separa los errores. Este texto es confuso en este contexto. Todavia no se definiuon. EXplicar que es el error."
  Resolution: La card nombraba accuracy y la matriz de confusión, que recién se definen en la sección 5, así que en la diapositiva 2 no significaban nada. Ahora define el error en sus propios términos: la distancia entre lo que el modelo predice y lo que de verdad pasó, y que resumirla en un solo número es una decisión de diseño. Es L8 aplicada a una card que reenviaba a términos todavía sin definir.
- [closed] 2026-08-19 — "Podriamos remplazar que lista algunos de los aspectos importantes. Aca estamos mencionando, input, output, error, overfitting, data set que es lo que vamos a ver en la presentacion."
  Resolution: La diapositiva pasó de "La mitad de la arquitectura no se elige" a "Lo que hay que diseñar", con los cinco aspectos que recorre la clase en orden de sección: entrada, dataset, salida, error, overfitting. El desglose en tres baldes se archivó en Cut material.
- [closed] 2026-08-19 — "Agreguemos esto como un item pero podemos poner una nota"
  Resolution: El remate al pie pasó a ser el sexto ítem de la lista ("Las capas y las neuronas. No están en la lista. Eso sí se elige, y es lo que menos importa del diseño"), y el detalle numérico (1 a 3 capas, potencias de 2, ReLU) bajó a una nota al pie de la diapositiva.

---

## 4. Una neurona, en una línea

### Content

Antes de diseñar conviene fijar el objeto mínimo. Una capa hace dos cosas: una combinación lineal y una no linealidad.

```ascii
   x1 ---w1--\
   x2 ---w2---> [ z = W·x + b ] --> [ f ] --> a
   x3 ---w3--/    (pre-activación)   (activación)
```
<!-- ascii-note:
intent: mostrar el paso de entradas a activación en una neurona
emphasize: las dos etapas z (lineal) y f (no lineal)
labels: x entradas, W·x+b pre-activación, f activación, a salida
-->

- **Pre-activación:** `z = W·x + b`. Combinación lineal de las entradas más un sesgo.
- **Activación:** `a = f(z)`. La no linealidad `f` es lo que hace que apilar capas sirva. Sin ella, la composición de capas lineales colapsa a una sola matriz.
- **Elección de `f`:** hay un puñado de candidatas y casi siempre gana ReLU. Las vemos al cierre de esta sección. La activación de salida es otra historia: la determina la tarea, y va en la sección 4.

### Sources

corpus/chat.md.md (§1 Conceptos base: Activación, Pesos y bias)

### Speaker notes

Refresco rápido, la audiencia tiene base técnica. El punto que no puede faltar: por qué la no linealidad. Preguntales qué pasa si sacás la ReLU de una red de 5 capas. Respuesta: te queda una regresión lineal disfrazada. Si preguntan cuántos parámetros tiene una capa: `m·n + m`, con n entradas y m neuronas. No lo desarrolles, no hace falta en el resto de la clase.

### Presenter feedback

---

## 5. El vector de entrada, una posición por feature

### Content

Cada posición del vector de entrada es una **feature**: una medición del problema ya convertida en número. El largo del vector es la cantidad de features, y queda fijo para toda la vida del modelo.

- **Tabular.** Una posición por columna ya codificada: edad, ingreso, antigüedad.
- **Imagen en escala de grises de 28 por 28.** 784 posiciones, una por píxel, con el valor de gris normalizado.

| Tipo de dato | Cómo se convierte en input |
|---|---|
| Numérico | Directo, normalizado a media 0 y desvío 1 |
| Categórico | One-hot hasta unas 15 categorías, embedding de 50 en adelante |
| Imagen | Píxeles normalizados, aplanados para un MLP |
| Texto | Tokenización y después embeddings |
| Audio | Espectrograma, o la forma de onda muestreada |

Tres cosas que se confunden seguido:

- **El largo no cambia.** La red espera siempre la misma cantidad de posiciones. Por eso las imágenes se redimensionan y el texto se trunca o se rellena hasta un largo fijo.
- **La escala.** Con una variable que va de 0 a 1.000.000 y otra de 0 a 1, la primera domina el entrenamiento por su magnitud y no por su importancia.
- **One-hot contra embedding.** Con muchas categorías posibles, one-hot da vectores enormes y casi todos ceros. El embedding las comprime en pocas dimensiones densas que además aprenden qué categorías se parecen.

Los dos últimos son el material de la sección que sigue.

### Sources

corpus/chat.md.md (§2 El input: principio general; §3 Codificación de variables; §4 One-hot vs. embedding — umbrales ≤15 one-hot / ≥50 embedding; §5 Escalas y normalización — z-score media 0 desvío 1)
784 = 28 × 28 — ejemplo aportado por el presentador (MNIST), no figura en el corpus

### Speaker notes

Esta diapositiva contesta la pregunta que queda colgando después de la neurona: qué es exactamente esa `x`. La respuesta corta, una feature por posición, y con eso alcanza para seguir el resto de la clase.

MNIST funciona bien acá porque es contraintuitivo de la manera correcta: 784 posiciones suena a mucho para un dígito escrito a mano, y sin embargo es un problema chico. Si preguntan cuántos parámetros tiene la primera capa con 32 unidades, son 784 × 32 + 32 = 25.120.

La tabla se recorre rápido, es un panorama. La sección que sigue desarrolla las dos primeras filas, que son las que aparecen en problemas tabulares. Texto y audio están para cerrar el mapa, no para desarrollarlos.

De los tres puntos de confusión, el del largo fijo es el que más preguntas genera. El ejemplo que lo cierra: un modelo entrenado con imágenes de 28 por 28 no acepta una de 32 por 32, hay que redimensionar antes. Con texto pasa lo mismo, y de ahí sale el padding.

### Presenter feedback
- [closed] 2026-08-20 — "Complementario a slide 4, pongamos slide 5 que cubra: el input de una red neuronal es en esencia un vector numerico; cada posicion representa una dimension (una feature); segun el tipo de dato cambia como se codifica; y los puntos que confunden: dimensionalidad fija, normalizacion/escala, y embeddings vs. one-hot."
  Resolution: Diapositiva nueva 1.5 'El vector de entrada, una posición por feature', después de 'Una neurona, en una línea'. Define feature por posición, el largo fijo del vector, MNIST 28x28 como 784 posiciones, la tabla tipo de dato a codificación (numérico, categórico, imagen, texto, audio) y los tres puntos que confunden: largo fijo, escala y one-hot contra embedding. Los dos últimos quedan apuntando a la sección 2, que es donde se desarrollan.


---

## 6. Las activaciones ocultas, y cómo se ven

### Content

Una **activación oculta** es la función no lineal `f` que se aplica después de `z = W·x + b` en las capas del medio. Su trabajo no es acotar el resultado a un rango con sentido, como en la salida, sino **romper la linealidad** para que apilar capas sirva de algo. Son cuatro candidatas y una gana casi siempre.

| Función | Fórmula | Rango | Cuándo |
|---|---|---|---|
| ReLU | `max(0, z)` | [0, ∞) | El default de las capas ocultas |
| GELU / SiLU | suavizaciones de ReLU | (−0.3, ∞) aprox. | Transformers |
| Tanh | `(eᶻ − e⁻ᶻ) / (eᶻ + e⁻ᶻ)` | (−1, 1) | Redes recurrentes, salidas centradas |
| Sigmoide | `1 / (1 + e⁻ᶻ)` | (0, 1) | Casi nunca en capas ocultas |

```ascii
     ReLU  max(0,z)          GELU / SiLU            Tanh  (-1,1)         Sigmoide  (0,1)
        |        /              |        /             |    _______         |    _______
        |       /               |       /            1 |   /              1 |   /
    ----+------/----        ----+---.--/----       ----+--/-------      ----+--/-------
        |     /                 |  \_/               0 | /              0.5 | /
        |____/                  |__/                -1 |/                 0 |/

    plana y despues        igual pero suave       acotada y            acotada, nunca
    recta. barata          en el cero             centrada en 0        negativa
```
<!-- ascii-note:
intent: mostrar la forma de las cuatro activaciones ocultas una al lado de la otra, para compararlas de un vistazo
emphasize: el codo de ReLU en el cero, que es lo que la distingue; la saturación de tanh y sigmoide en los extremos
labels: ReLU, GELU/SiLU, Tanh, Sigmoide; eje horizontal z, eje vertical f(z)
-->

**Nota:** la sigmoide y la tanh saturan. Con `z` grande su derivada es casi cero, el gradiente que llega a las capas de abajo se apaga y la red deja de aprender. ReLU no satura del lado positivo, y esa es la razón por la que ganó.

### Sources

corpus/chat.md.md (§1 Conceptos base: Activación)

### Speaker notes

Esta es la diapositiva que faltaba: hasta acá la activación era un nombre, ahora tiene forma. Recorré el diagrama de izquierda a derecha y detenete en el codo de ReLU: es literalmente dos rectas pegadas, y con eso alcanza. La pregunta que funciona: ¿por qué una función tan tonta le gana a las suaves? Respuesta corta, no satura y es baratísima de calcular. La saturación es el concepto que se llevan, y vuelve en la sección 2 con la normalización: una entrada grande sin normalizar satura la neurona igual que un `z` grande.

### Presenter feedback

---

# 2. Modelar la entrada

**Goal of this section:** El corazón de la clase. Mostrar el método para convertir cualquier variable en floats: la pregunta de la resta, one-hot contra embedding, la normalización y la tabla de decisiones que cierra la sección. Que salgan sabiendo decidir de qué largo es el vector de entrada de un problema real.

**Presenter feedback:**
- [closed] 2026-08-19 — "Borremos esta seccion"
  Resolution: Se retiró la diapositiva 2.6 (μ y σ). Su contenido de data leakage y artefacto de producción no se descartó: pasó a la diapositiva 3.3 de la sección nueva, que es donde el tema se entiende mejor. Registrado en Cut material.
- [closed] 2026-08-19 — "Y agreghemos una new seccion sobre como partir el data set entre test, training (...). La idea es cubir que es lo que se hace con el data set."
  Resolution: Se creó la sección 3 "Partir el dataset" con cuatro diapositivas, entre "Modelar la entrada" y "Modelar la salida". Las secciones 3 a 6 se renumeraron a 4 a 7.
- [closed] 2026-08-19 — "En est seccion falta alguna tabla que tome ejemplos de entradas y a que se deberia mapear o previa tarformacion. Eso estaba en el corpus, eso es un nuevo slide."
  Resolution: Nueva diapositiva 2.6 "De la variable al tensor: la tabla de decisiones", con doce filas de variable → ejemplo → codificación → neuronas, armada desde corpus/chat.md.md §3 y §4.
- [closed] 2026-08-19 — "La tabla Test Set vs. Training Set vs. Validation Set deberia estar"
  Resolution: Es la diapositiva 3.2, con las cinco filas de la fuente (propósito, cuándo lo ve el modelo, actualiza pesos, augmentation, proporción).

---

## 1. Qué significa que el dato sea tabular

### Content

Esta clase modela datos **tabulares**: una fila por ejemplo y una columna por variable, sin vecindad ni orden intrínseco entre las columnas. Intercambiar la columna de edad con la de ingreso no cambia el significado del dato mientras cada una conserve su nombre.

Esa propiedad es la que hace que un MLP encaje. Una capa densa conecta cada neurona con todas las entradas y no usa la posición para nada, así que recibir las columnas en otro orden no le quita información. En una imagen sí se la quitaría, porque ahí la posición del píxel es parte del dato.

Falta el paso de la columna al número. Cada columna se convierte en una o más posiciones del vector, y de qué depende esa conversión es el resto de esta sección.

### Sources

corpus/chat.md.md (§2 El input: principio general — el caso sin estructura y su invariancia al orden de columnas)

### Speaker notes

Definí "tabular" por contraste con una imagen, que es el ejemplo que todos tienen a mano: en una tabla no hay píxeles vecinos ni orden temporal que explotar, y el modelo puede recibir las columnas en cualquier orden mientras sepa cuál es cuál. Ese es el punto que conecta con la diapositiva de arquitecturas de la sección anterior: el MLP no usa la posición, y en tabular no hay posición que usar, así que la arquitectura y el dato se corresponden.

El resto de la sección es método, y conviene anunciarlo así: cada columna del dataset se convierte en una o más posiciones del vector, y lo que decide en cuántas y con qué valores es el tipo de variable.

Si alguien pregunta por imágenes, texto o series temporales, la respuesta corta es que cada familia tiene su arquitectura y que las vimos al pasar en la sección 1. No abras ese frente acá.
### Presenter feedback
- [closed] 2026-08-18 — "Marcar aca que lo que vamos a enforcanos en el caso 1 Sin estructura (tabular) |"
  Resolution: Se marcó el foco de la clase en el caso tabular.
- [closed] 2026-08-18 — "Que significa Sin estructura (tabular)"
  Resolution: Se definió explícitamente el caso tabular como filas y columnas sin vecindad ni orden intrínseco.
- [closed] 2026-08-18 — "?. Poner ejemplos en la tabla de que es cada caso."
  Resolution: Se añadieron ejemplos concretos para cada familia de estructura.
- [closed] 2026-08-19 — "Secuencia no se si es la definicion correcta. Seria bueno que introducca de definicion del tipo y luego ejemplos. Los ejemplos son procos."
  Resolution: La tabla pasó a cinco columnas con una de definición propia ("Qué es") antes de los ejemplos, y cada fila subió a tres ejemplos. Se corrigió Secuencia (elementos discretos de un vocabulario, orden, largo variable) y se agregó un párrafo que la separa de Señal. Las notas del orador recogen la distinción.
- [closed] 2026-08-20 — "Si, vamos con eso (recortar la 2.1 al caso tabular; el zoologico de seis familias queda solapado con el framing nuevo de la seccion 1)."
  Resolution: Se recortó la 2.1 al caso tabular. Salió la tabla de seis familias de estructura (archivada en Cut material) y la diapositiva pasa a definir qué significa tabular y por qué esa propiedad es la que hace encajar un MLP: la capa densa no usa la posición y en tabular no hay posición que usar. El resto de la sección queda anunciado como el método de columna a número.

---

## 2. La pregunta que decide la codificación

### Content

Frente a cualquier variable, una sola pregunta ordena la decisión: **¿qué significa la resta entre dos valores?**

- **Da una cantidad interpretable** (85 m² menos 60 m² son 25 m² reales): 1 float normalizado, una posición del vector.
- **Da un orden pero no una magnitud confiable** (satisfacción 4 menos 2): ordinal, evaluar también one-hot.
- **No significa nada** (barrio 14 menos barrio 7): one-hot o embedding según cuántos valores distintos haya.
- **No se puede ni plantear:** probablemente no sea una feature útil.

**Poner un número real en el vector es afirmar algo.** Cada float le promete a la red dos cosas sobre esa posición: que las diferencias son comparables (14 está más lejos de 7 que de 13) y que la magnitud escala el efecto, porque el aporte a `z = W·x + b` es el peso por el valor. Con 85 m² y 60 m² la promesa se cumple. Con barrio 14 y barrio 7 es falsa, y ahí es donde hay que cambiar de codificación.

Todo termina en floats, nunca en enteros. Los enteros aparecen en un solo lugar: como índice para buscar una fila en una tabla de embeddings. El entero no entra a la red, entra al lookup.

### Sources

corpus/chat.md.md (§3 Codificación de variables: la pregunta que decide todo; §3 Todo termina en floats)

### Speaker notes

Esta pregunta es la herramienta más transferible de la clase. Si se llevan una sola cosa de la sección, que sea esta. Ejemplo en vivo: tirales tres variables de un dataset que conozcan (edad, código postal, nivel educativo) y que apliquen la pregunta en voz alta. El código postal es la trampa clásica: parece número, la resta no significa nada.

### Presenter feedback
- [closed] 2026-08-19 — "Seria bueno aca agregar una nota que los valores al sear reales hay cierta expectativa que las deferencias y magntides modelan algo. g: Barrio 14-7 no dice nada de ahi que hay que modelarlo distinto"
  Resolution: Se agregó el párrafo "Poner un número real en el tensor es afirmar algo", con las dos promesas que hace un float (diferencias comparables y magnitud que escala el efecto vía W·x) y el contraste 85 m² contra barrio 14.

---

## 3. Numéricas: normalizar no es opcional

### Content

**Normalizar** es reexpresar una variable en una escala comparable con las demás antes de que entre a la red. Cambia la unidad en la que se lee el número, no la información que trae. Aplica a las numéricas con magnitud real: superficie, ingreso, edad, cantidad de transacciones.

- **z-score por defecto:** `(x − μ) / σ`. El valor pasa a leerse como "cuántos desvíos por encima o por debajo del promedio". La unidad original desaparece.
- **log antes del z-score:** con colas largas, `log(1+x)` comprime los valores altos antes de estandarizar. La diferencia entre 1 y 10 transacciones importa más que entre 4000 y 4010. Casos típicos: ingresos, cantidad de transacciones, días desde la última compra.
- **Los booleanos y one-hot no se tocan:** ya están en 0 y 1.
- **Escala pareja no es importancia pareja.** Normalizar no le quita peso a una variable; la importancia la aprenden los pesos. Solo la pone en condiciones de ser evaluada.

**Nota:** por qué no es opcional. El gradiente respecto a un peso es proporcional al valor de la entrada (`∂J/∂wⱼ = δ · xⱼ`), pero el learning rate es uno solo para toda la red. Si una variable vale ~200 (m²) y otra vale 0 o 1 (cochera), sus gradientes están a escala 200 a 1 y el entrenamiento zigzaguea.

### Sources

corpus/chat.md.md (§5 Escalas y normalización)

### Speaker notes

El "por qué" formal es el número de condición de la Hessiana, pero para la clase alcanza con la imagen de las curvas de nivel: escalas parejas dan círculos y el gradiente apunta al mínimo; escalas dispares dan elipses alargadas y el gradiente apunta a la pared. Efecto secundario importante: con sigmoide o tanh una entrada grande satura la neurona (derivada casi cero) y deja de aprender. Aclará que árboles y gradient boosting no necesitan normalización; es una particularidad de los métodos basados en gradiente.

### Presenter feedback
- [closed] 2026-08-19 — "Movelo como una nota abajo."
  Resolution: Sobre el bloque "Por qué no es opcional". El argumento del gradiente bajó de párrafo destacado, arriba de las recetas, a nota al pie de la diapositiva. La apertura queda solo con la definición.
- [closed] 2026-08-19 — "En casi todos los slides es confusdo que no se define y en algunos caso se empieza con ejemplos. En este caso, fata la defincion, luego se peude mencionar datos tipo y el effecto de."
  Resolution: La diapositiva pasa a orden definición → a qué datos aplica → recetas, con el efecto al pie. Se abre definiendo qué es normalizar y sobre qué variables aplica; el argumento del gradiente quedó después, bajo "Por qué no es opcional". La parte general del comentario (que casi todas las diapositivas arrancan por el ejemplo) queda pendiente de decisión del presentador como barrido definición-primero de todo el mazo.

---

## 4. Categóricas: one-hot contra embedding

### Content

Una categoría sin orden se codifica de dos formas, y la cardinalidad decide cuál.

```ascii
one-hot "Depto":  [0, 1, 0, 0]   un float por valor, todas equidistantes
                      |
        W · x  selecciona la columna de W  -->  cada categoría, sus propios pesos
```
<!-- ascii-note:
intent: mostrar que one-hot con W selecciona una columna de pesos
emphasize: el 1 activa una sola columna de W
labels: one-hot vector, W matriz de pesos
-->

- **One-hot** (cardinalidad baja): un float por valor, todas en 0 salvo una en 1. Todas las categorías quedan a la misma distancia, que es la verdad del dato. No se aprende, es interpretable, necesita pocos datos.
- **Embedding** (cardinalidad alta): una tabla de `k × d` floats entrenable. La red aprende la distancia entre categorías desde los datos. Con 500 barrios, un embedding de dimensión 24 usa 24 floats donde one-hot usaría 500.
- **La regla de la cardinalidad:** hasta 15 valores, one-hot; de 15 a 50, cualquiera; 50 o más, embedding.

Un embedding es matemáticamente equivalente a un one-hot seguido de una capa lineal sin sesgo. Conceptualmente, la tabla de embeddings es la primera capa de la red.

### Sources

corpus/chat.md.md (§4 One-hot vs. embedding; §7 Con 500 barrios)

### Speaker notes

El puente conceptual que engancha: así arranca un LLM. Cada token es un índice que busca su fila en una tabla de unas 50.000 por 4096. El embedding de categorías tabulares y el embedding de palabras son la misma idea, una representación densa aprendida donde la geometría del espacio codifica el significado. Las dos ventajas no obvias del embedding: comparte estadística entre categorías parecidas (una categoría rara hereda de sus vecinas) y es reutilizable para clustering o búsqueda por similitud.

### Presenter feedback

---

## 5. Errores de codificación caros

### Content

Casi todos entran silenciosos: el modelo entrena sin dar error y falla en producción.

- **Código como número.** Un identificador de categoría cargado como entero. La red lee orden y magnitud donde no hay ninguno: con barrio 7 y barrio 14, asume que 14 es "el doble" de 7. Van como one-hot o embedding.
- **Identificador único como feature.** Una columna cuyo valor no se repite entre ejemplos, como DNI, CUIT o número de póliza. No tiene poder predictivo porque no hay nada que generalizar; si el modelo "aprende" de ella, está memorizando. Se descarta.
- **Variable cíclica aplastada.** Una magnitud que vuelve a empezar (hora, día de la semana, mes) codificada como número plano. Los extremos del ciclo quedan lejísimos: las 23:00 y las 00:00 están a una hora y como números planos están a 23. Se codifica con dos floats, `sin(2πt/T)` y `cos(2πt/T)`.
- **Faltante rellenado con 0.** Un hueco tapado con un valor que la red no distingue de un dato real. Cuando 0 es válido, confunde ausencia con valor. La receta es imputar (media o mediana) más un flag binario, que muchas veces predice más que la variable misma.

### Sources

corpus/chat.md.md (§3 Codificación de variables: enteros que son códigos, cíclicas, faltantes; §11 Los errores que más cuestan)

### Speaker notes

Sección de "no lo hagas". Estos cuatro son los que más veces vas a ver en trabajos de alumnos y en producción. El de los códigos y el de los IDs únicos son los favoritos. Contá el caso del ID: el modelo memoriza el dataset de train, da accuracy perfecto y se derrumba con datos nuevos. Es un puente natural hacia overfitting, que vemos en la sección 6.

### Presenter feedback

---

## 6. De la variable al vector: la tabla de decisiones

### Content

La sección entera cabe en una tabla. Cada fila es un tipo de variable que te vas a encontrar, y la columna del medio es la única decisión que hay que tomar. En la última columna, **`k` es la cantidad de valores distintos** que toma la variable y **`d` es la dimensión del embedding**, que se elige.

La columna dice **floats, no neuronas**. La capa de entrada no es una capa: no tiene pesos ni calcula nada, es el vector en sí. Una neurona hace `z = W·x + b` y después una activación, y la primera que hace eso es la primera capa oculta. Lo que la tabla cuenta son posiciones del vector de entrada.

| Variable | Ejemplo | Codificación | Floats |
|---|---|---|---|
| Booleana | Tiene cochera | 0 o 1, tal cual | 1 |
| Numérica con magnitud | Superficie 85 m² | z-score `(x − μ) / σ` | 1 |
| Numérica con cola larga | Ingreso mensual | `log(1+x)` y después z-score | 1 |
| Ordinal | Plan Free → Enterprise | Float 0, 0.5, 1 más one-hot, concatenados | 1 + k |
| Nominal, cardinalidad baja | Tipo de vivienda (4 valores) | One-hot | k |
| Nominal, cardinalidad alta | Barrio (500 valores) | Embedding de dimensión d | d |
| Código con forma de número | Código postal, código de producto | Embedding. Nunca como número | d |
| Identificador único | DNI, CUIT, número de póliza | Se descarta | 0 |
| Cíclica | Hora del día, mes de venta | `sin(2πt/T)` y `cos(2πt/T)` | 2 |
| Fecha | Fecha de alta del cliente | "Cuándo en el ciclo" (cíclica) más "hace cuánto" (continua) | 2 por ciclo + 1 |
| Texto libre | Reseña, descripción | Sentence transformer (TF-IDF como baseline) | d |

**Faltar no es un tipo, le pasa a cualquiera.** Puede faltar un booleano, un barrio o una fecha, así que no es una fila más: es un modificador que se aplica sobre la fila que corresponda. Se imputa (media o mediana en las numéricas, categoría propia en las categóricas) y **se suma un float**, el flag binario que dice si el dato estaba. Ese flag muchas veces predice más que la variable misma.

<!-- format: editorial -->

### Sources

corpus/chat.md.md (§3 Codificación de variables; §4 One-hot vs. embedding)

### Speaker notes

Es la diapositiva de referencia de la sección, la que van a fotografiar. No la leas fila por fila: pediles que elijan tres variables de un dataset que conozcan y las ubiquen. Las filas que más discusión generan son las tres del medio (ordinal, código con forma de número, identificador único) y son justamente las tres que más aparecen mal resueltas en los trabajos. Dos aclaraciones para tener a mano: la fila de fecha dice "2 por ciclo" porque una fecha suele tener más de uno, el mes del año y el día de la semana, y ahí son 2 + 2 + 1; y si alguien pregunta por qué faltantes no está en la tabla, la respuesta es que faltar no es un tipo de variable sino algo que le puede pasar a cualquiera. El cierre importa: el largo del vector de entrada es una consecuencia de la tabla, no una decisión de arquitectura. Si alguien pregunta por qué la columna dice floats y no neuronas, la respuesta corta es que la entrada no calcula nada: una neurona hace `z = W·x + b` más activación, y la primera que hace eso es la primera capa oculta. Es una imprecisión frecuente en los libros y vale la pena marcarla, porque es la misma idea con la que abre la clase: la red ve un vector de floats.

### Presenter feedback
- [closed] 2026-08-19 — "Borrar 'Sumar la última columna, más un flag por cada variable que pueda faltar, da el largo del vector de entrada. Esa cuenta no se elige: sale de la tabla.'"
  Resolution: Se retiró el cierre. La tabla y el párrafo de faltantes se sostienen solos.
- [closed] 2026-08-19 — "Leí que el input realmente no son neuronas"
  Resolution: Correcto, y la tabla decía "Neuronas". La capa de entrada no tiene pesos ni calcula nada: es el vector en sí, y la primera que hace `z = W·x + b` más activación es la primera capa oculta. La columna pasó a llamarse "Floats", que además es el término con el que abre la sección ("Todo termina en un vector de floats"), y se agregó un párrafo que explica la distinción. También se corrigieron el goal de la sección y el cierre de la diapositiva, que decían "cantidad de neuronas de entrada", y las notas del orador para responder si alguien pregunta. El encabezado "Neuronas" del catálogo de salida no se tocó: ahí sí son neuronas de verdad.
- [closed] 2026-08-19 — "En la tabla de neuronas para el input hay una tabla. ¿Es eso correcto?"
  Resolution: Los números estaban bien, pero la tabla tenía tres problemas. (1) `k` y `d` aparecían en cinco filas sin definirse; ahora se definen en la bajada, antes de la tabla. (2) "Con faltantes" no era un tipo de variable sino un modificador que se cruza con todas las filas, y su "1 + 1" solo valía si la variable de abajo era numérica: con un barrio en one-hot son k + 1. Salió de la tabla y pasó a un párrafo que dice que faltar le pasa a cualquiera y suma una neurona de flag. (3) "Fecha 2 + 1" asumía un solo ciclo; pasó a "2 por ciclo + 1", porque una fecha suele tener mes del año y día de la semana. El cierre ahora suma también los flags.

---

# 3. Partir el dataset

**Goal of this section:** Qué se hace con el dataset antes de entrenar. Los tres conjuntos, para qué sirve cada uno, en qué proporción, y qué errores de partición arruinan la medición sin lanzar ningún error. Es la sección que hace honesta cualquier métrica de las secciones 5 y 6.

**Presenter feedback:**

---

## 1. Un dataset, tres trabajos distintos

### Content

**Partir el dataset** es reservar de antemano tres porciones separadas, cada una con un trabajo distinto. Existe por una sola razón: si medís el modelo con los mismos datos con los que lo entrenaste, la métrica miente.

```ascii
  dataset completo
  +-----------------------------+----------+---------+
  |          train  70%         | val  20% | test 10%|
  +-----------------------------+----------+---------+
     aprende de el                se mira    se abre
     actualiza W y b              cada epoch una vez
```
<!-- ascii-note:
intent: mostrar las tres porciones del dataset y qué hace el modelo con cada una
emphasize: los tres bloques y la asimetría de tamaño; que solo train actualiza pesos
labels: train 70%, val 20%, test 10%
-->

- **Train.** La muestra con la que se ajusta el modelo. Es la única que actualiza `W` y `b`. El modelo la ve y aprende de ella.
- **Validación.** Evaluación frecuente durante el entrenamiento, para tunear hiperparámetros y decidir cuándo cortar (early stopping). El modelo la ve después de cada epoch y nunca entrena con ella. También se la llama dev set.
- **Test.** Se abre una sola vez, con el modelo ya terminado. Es la lectura más cercana al desempeño en producción que se puede conseguir antes de desplegar.

### Sources

corpus/train-test-split-roboflow.web.md (§1 Resumen; §3 Training set; §4 Validation set; §5 Test set; §10 Ratios); corpus/train-validation-test-sets.web.md (§1 Los tres conjuntos, definidos)

### Speaker notes

Arranca por el porqué, no por los porcentajes: medir con los datos de entrenamiento es como tomar examen con las respuestas a la vista. Los números 70/20/10 están en el diagrama y son criterio práctico de la industria (Roboflow los recomienda como default), no un resultado empírico; decilo así si alguien pregunta de dónde salen. Con datasets muy grandes, de decenas de miles de ejemplos, 80/10/10 también funciona, porque ese 10% sigue siendo mucha muestra. El punto que más se olvida es el piso absoluto: con 200 ejemplos totales, un 10% de test son 20 casos y cualquier métrica sobre 20 casos es ruido. Ahí conviene cross-validation, que aparece en la 3.4.


### Presenter feedback
- [closed] 2026-08-19 — "Borrar Proporciones 70 / 20 / 10 de arranque. Con datasets muy grandes, 80 / 10 / 10. No bajar validación ni test de unos pocos cientos de ejemplos, ya esta en el assci."
  Resolution: Se retiró la card. Los 70/20/10 ya los dibuja el diagrama, así que la card los repetía. Lo que la card decía y el diagrama no dice pasó a las notas del orador: el 80/10/10 para datasets grandes, y el piso de unos pocos cientos de ejemplos por debajo del cual la métrica es ruido.
---

## 2. Los tres, lado a lado

### Content

| | Train | Validación | Test |
|---|---|---|---|
| Para qué sirve | El modelo aprende de él | Tuning, early stopping, elegir modelo | Evaluación final sin sesgo |
| Cuándo lo ve el modelo | Cada epoch | Se evalúa cada epoch, nunca entrena con él | Una vez, al final |
| Actualiza los pesos | Sí | No | No |
| Augmentation | Sí | No | No |
| Proporción típica | 70% | 20% | 10% |

- **La diferencia sutil está entre validación y test.** El modelo no entrena con ninguno de los dos. La diferencia sos vos: tomás decisiones mirando validación, y a lo largo de muchos experimentos vas sobreajustando tus elecciones a ese conjunto. El test atrapa eso, porque nada del modelo se eligió mirándolo.
- **Por eso no alcanza con partir en dos.** Sin validación terminás tuneando contra el test, y cuando desplegás sus métricas ya no son insesgadas. El split de dos vías sirve solo si no tomás ninguna decisión iterativa, que no describe a ningún proyecto real.
- **Augmentation solo en train.** Agrandar el training set con variaciones sirve para aprender. Validación y test tienen que quedarse con los datos originales, porque su trabajo es representar lo que viene en producción. El preprocesamiento, en cambio, se aplica a los tres.

### Sources

corpus/train-test-split-roboflow.web.md (§6 La distinción sutil; §7 Preprocesamiento contra augmentation; §11 Por qué no alcanza con train y test; tabla comparativa); corpus/train-validation-test-sets.web.md (§2 Qué distingue a validación de test)

### Speaker notes

Esta tabla es el resumen que se llevan de la sección. La fila que cuesta es "actualiza los pesos": muchos creen que el modelo aprende algo de validación porque la métrica aparece en pantalla cada epoch. No aprende nada; el que aprende sos vos, y por eso hace falta el test. La analogía que funciona: validación son los simulacros que hacés para estudiar, test es el examen final; si te dan el examen final de simulacro, deja de medir. Menciona que en Kaggle el test set se libera recién al cierre de la competencia, exactamente por esto.


### Presenter feedback
---

## 3. Todo lo que se aprende sale solo del train

### Content

La partición no alcanza si el preprocesamiento se calcula mal. Las estadísticas de normalización se calculan **solo** con el conjunto de entrenamiento, y se guardan para reaplicarlas idénticas en validación, test y producción.

```python
# MAL: μ y σ contaminados con el test (data leakage)
scaler.fit_transform(X_test)

# BIEN: μ y σ aprendidos solo del train
scaler.fit(X_train)
scaler.transform(X_test)
```

- **Calcularlos sobre todo el dataset es data leakage.** Información del test se filtra al entrenamiento y la métrica sale optimista. La regla general: todo lo que se aprende de los datos se aprende solo del train, transformaciones incluidas.
- **La transformación se aplica a los tres, sus parámetros salen de uno.** Normalizar, imputar y mapear categorías corre sobre train, validación y test por igual. Pero μ, σ, la mediana de imputación y el diccionario categoría a índice se calculan únicamente sobre train.
- **Un modelo desplegado no son solo `W` y `b`.** Son los pesos más los μ y σ de cada variable, más el diccionario categoría a índice, más los valores de imputación. Si se guardan solo los pesos, el modelo queda inservible.
- **El bug es silencioso.** Normalizar en producción con μ=120 en vez de 95 no lanza ninguna excepción. Solo devuelve predicciones incorrectas.

### Sources

corpus/chat.md.md (§6 μ, σ y el artefacto de producción); corpus/train-test-split-roboflow.web.md (§7 Preprocesamiento contra augmentation)

### Speaker notes

Esta diapositiva venía de la sección de input y encaja mejor acá, con la partición ya explicada. Es el error número uno de producción en ML según la fuente: que la normalización o el diccionario de categorías queden fuera del artefacto. La regla para llevarse: el preprocesamiento y el modelo se despliegan juntos; quien consume el modelo no debería tener que saber que la normalización existe. Ojo con un matiz que la fuente de Roboflow no cubre: ellos dicen "el preprocesamiento se aplica a los tres splits" y es cierto, pero no advierten que los parámetros salen solo de train. Si hay tiempo, mencioná data drift: la solución no es recalcular μ y σ en producción, es detectar el drift y reentrenar.


### Presenter feedback
---

## 4. Partir mal: los errores que arruinan la medición

### Content

Ninguno de estos lanza una excepción. Todos devuelven una métrica mejor que la real.

- **Duplicados repartidos entre conjuntos.** El mismo caso, o uno casi idéntico, cae en train y también en test. El test deja de medir generalización y mide memoria: el modelo ya vio la respuesta. Aparece en cualquier dataset armado juntando fuentes. Se deduplica antes de partir, nunca después.
- **No estratificar con clases desbalanceadas.** El split aleatorio reparte sin mirar la clase. Con 2% de fraude, el test puede quedar con tres casos positivos, y un recall calculado sobre tres casos no es una métrica, es una anécdota. Se estratifica por la clase, así las tres porciones conservan la proporción original.
- **Partir al azar una serie de tiempo.** Si el dato tiene orden temporal, el azar pone futuro en train y pasado en test. El modelo predice enero mirando marzo, información que en producción nunca va a tener. El número se ve espectacular y no se sostiene. Se corta por fecha: lo anterior a un día entrena, lo posterior evalúa.
- **Achicar validación y test.** "Más datos, mejor modelo" tienta a dejar 90% en train. Con validación y test chicos la métrica tiene tanto ruido que dos modelos distintos parecen iguales, o el peor parece mejor. El piso práctico son unos pocos cientos de ejemplos en cada uno.
- **Cross-validation, y cuándo paga.** K-fold parte el train en k porciones y entrena k veces, reservando una distinta cada vez y promediando los resultados. Da una estimación mucho más confiable cuando hay pocos datos, y cuesta k entrenamientos. Con modelos profundos rara vez conviene; con datasets chicos o modelos baratos, sí.

```python
from sklearn.model_selection import train_test_split

# 70 / 20 / 10 en dos pasos, con la clase estratificada
train_X, hold_X, train_y, hold_y = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)
val_X, test_X, val_y, test_y = train_test_split(
    hold_X, hold_y, test_size=1/3, random_state=42, stratify=hold_y
)
```

`random_state` fijo hace la partición reproducible, que es lo que permite comparar dos modelos sobre exactamente los mismos datos.

### Sources

corpus/train-test-split-roboflow.web.md (§8 Errores típicos; §9 Cómo se hace en Python; §12 Cross-validation); corpus/train-validation-test-sets.web.md (§4 Cross-validation); conocimiento del área (estratificación y partición temporal, no cubiertas por las fuentes)

### Speaker notes

Los dos del medio son aporte propio: ninguna de las dos fuentes cubre estratificación ni series de tiempo, y las dos importan para los trabajos que entregan. El de series de tiempo es el que más veces vas a ver mal resuelto, y el síntoma es un modelo que en el papel anda espectacular. Conectá con la sección 2: el identificador único es la versión extrema de este problema, memorizar en vez de aprender. Y dejá el puente abierto hacia overfitting: la brecha entre train y validación, que es el diagnóstico de la sección 6, solo se puede mirar si esta partición está bien hecha.


### Presenter feedback
- [closed] 2026-08-19 — "Partir mal: los errores que arruinan la medición -> exploicar un pcoo cada boxed."
  Resolution: Las cinco cards pasaron de una línea a tres, con el mismo patrón cada una: qué es el error, por qué infla la métrica y qué se hace en su lugar. Se agregaron el "se deduplica antes de partir", el ejemplo del recall sobre tres casos, el de predecir enero mirando marzo, el efecto concreto del ruido (dos modelos que parecen iguales) y cómo funciona k-fold. La diapositiva pasa de grilla editorial a lista, que es lo que tolera cuerpos largos sin encogerse.
---

# 4. Modelar la salida

**Goal of this section:** Mostrar que la última capa no se elige, la determina la tarea, y que activación de salida y loss van siempre juntas. Que salgan sabiendo mapear "qué predice el modelo" a "cuántas neuronas, qué activación, qué loss", y sabiendo por qué la forma de cada activación de salida corresponde a lo que se predice.

**Presenter feedback:**

---

## 1. Un catálogo para elegir sin dudar

### Content

Casi cualquier tarea entra en esta tabla. Elegida la fila, la salida queda determinada.

| Qué predice | Neuronas | Activación | Loss |
|---|---|---|---|
| Un real (precio) | 1 | Lineal | MSE / MAE / Huber |
| Sí o no (churn) | 1 | Sigmoide | BCE |
| Una de N clases | N | Softmax | Cross-entropy |
| Varias de N (tags) | N | Sigmoide ×N | BCE |
| Conteo (demanda) | 1 | Softplus / exp | Poisson NLL |
| Cuantiles (P10, P50, P90) | k | Lineal | Pinball |
| Distribución (μ, σ) | 2 | μ lineal, σ softplus | NLL gaussiana |

Un caso que conviene remarcar: cuando el negocio necesita un rango y no un punto, los cuantiles (P10, P50, P90) son la opción más rentable. No asumen forma de la distribución y dan directamente el intervalo que el negocio quiere.

### Sources

corpus/chat.md.md (§8 Catálogo completo de outputs; predecir una distribución, no un punto)

### Speaker notes

No leas toda la tabla; usala como referencia y detenete en dos o tres filas. La de cuantiles suele ser nueva para los alumnos y es muy útil en la práctica (stock, riesgo, capacidad, donde importa el peor escenario). La media es la respuesta correcta a una pregunta que muchas veces nadie hizo. La distribución con μ y σ conecta con estadística que ya vieron.

### Presenter feedback
- [closed] 2026-08-19 — "Dos formas de modelar mal la salida, borra este slide"
  Resolution: Se retiró la última diapositiva de la sección; el contenido completo, incluidas las notas del orador que se pierden, quedó archivado en Cut material. La sección queda con tres diapositivas: catálogo, capa de salida, cómo se ven las cuatro.
- [closed] 2026-08-19 — "Mover Un catálogo para elegir sin dudar antes de Cómo se ven las cuatro y La capa de salida la determina la tarea."
  Resolution: El catálogo pasó a abrir la sección. El orden queda catálogo, capa de salida, cómo se ven las cuatro, dos formas de modelar mal: primero el mapa completo de tarea a salida, después el detalle de la activación y recién ahí su forma. El diagrama de las formas se renombró de s4-2-1 a s4-3-1 para seguir a su diapositiva.

---

## 2. La capa de salida la determina la tarea

### Content

La activación de salida es el mismo tipo de objeto que ReLU, pero se elige con otro criterio: poner el número en el rango y la interpretación correctos. Son cuatro, y cada una corresponde a un tipo de respuesta.

| Activación | Representación | Rango | Ejemplo |
|---|---|---|---|
| Lineal (ninguna) | `y = z` | todo ℝ | precio |
| Sigmoide | `σ(z) = 1 / (1 + e⁻ᶻ)` | (0, 1) | probabilidad de churn |
| Softmax | `eᶻⁱ / Σⱼeᶻʲ` | vector que suma 1 | clase de una imagen |
| Softplus | `log(1 + eᶻ)` | (0, ∞) | demanda o desvío |

"Activación lineal" es una forma elegante de decir ninguna activación. Es la única capa donde no poner activación es lo correcto.

<!-- template: concept-breakdown -->

### Sources

corpus/chat.md.md (§8 La capa de salida)

### Speaker notes

Contrastá con las capas ocultas: ahí la activación casi no importa (ReLU y listo). En la salida, cada opción corresponde a un rango y a una interpretación. Quedate en la fórmula y el rango; las formas las dibuja la diapositiva que sigue, no las adelantes. Preguntá por casos: ¿qué activación para predecir la cantidad de unidades vendidas? Softplus o exp, porque un conteo no puede ser negativo. La salida lineal con MSE para conteos permite predicciones negativas, un error clásico.

### Presenter feedback
- [closed] 2026-08-18 — "Seria bueno si podemos meter todas en en un slide como es la representacion de cada una de estas funciones."
  Resolution: Se reorganizó la diapositiva como una tabla comparativa de las cuatro funciones, con fórmula, rango y ejemplo.
- [closed] 2026-08-19 — "Agregar otro slide que sea para cada una de las funciones la representacion. Tal vez solo un ASCCI con tido."
  Resolution: Nueva diapositiva 4.2 "Cómo se ven las cuatro", con un solo diagrama que pone lineal, sigmoide y softplus como curvas y softmax como reparto entre clases, que es lo que realmente es. La tabla de fórmulas y rangos queda en la 4.1 y el dibujo en la 4.2.
- [closed] 2026-08-19 — "Tambien faltaria en el input las funciones de activation como relu, etc. Seguiria el mismo patron de defincion y luego la visualizacion de como se ven las funciones."
  Resolution: Nueva diapositiva 1.4 "Las activaciones ocultas, y cómo se ven", con el mismo patrón: definición de qué es una activación oculta, tabla de las cuatro candidatas con fórmula, rango y cuándo, y un diagrama con las cuatro formas. Cierra con la saturación, que es la razón por la que ganó ReLU. La card de la 1.3 dejó de adelantar la respuesta y ahora apunta a esta diapositiva.


---

## 3. Cómo se ven las cuatro

### Content

La tabla de la diapositiva anterior dice el rango; el dibujo dice la forma. Es lo que hace evidente por qué cada una sirve para lo que sirve.

```ascii
     Lineal  y = z          Sigmoide  1/(1+e^-z)     Softplus  log(1+e^z)     Softmax  reparte 1
        |       /              |     _______            |         /
        |      /             1 |    /                   |        /            gato  [######   ]
    ----+-----/----        ----+---/-------         ----+------/------        perro [##       ]
        |    /               0 |__/                   0 |____/                zorro [#        ]
        |   /                  |                        |                          suma = 1

    sin piso ni techo      tiene techo en 1       tiene piso en 0        no es una curva
    un precio              una probabilidad       un conteo              una clase entre N
```
<!-- ascii-note:
intent: mostrar la forma de las cuatro activaciones de salida en cuatro paneles iguales, con el mismo layout que el diagrama de las activaciones ocultas
emphasize: el techo de la sigmoide en 1 y el piso de softplus en 0; que softmax no es una curva sino un reparto que suma 1
labels: Lineal, Sigmoide, Softplus, Softmax; sin piso ni techo, techo en 1, piso en 0, reparto entre clases
-->

- **Lineal.** La recta `y = z`. No tiene piso ni techo, y por eso sirve para un precio: cualquier valor real es una respuesta válida.
- **Sigmoide.** Aplasta cualquier número en (0, 1). El techo en 1 es lo que la convierte en una probabilidad.
- **Softplus.** Piso en 0 y sin techo. Es la forma correcta para un conteo o un desvío, que no pueden ser negativos.
- **Softmax.** No transforma un valor, reparte 1 entre N clases que compiten. Es la única que necesita ver todas las neuronas de salida a la vez.

### Sources

corpus/chat.md.md (§8 La capa de salida)

### Speaker notes

Es el complemento visual de la diapositiva anterior y se da rápido, dos minutos. El punto que justifica la diapositiva: la forma explica el uso. La sigmoide tiene techo en 1, por eso es una probabilidad. Softplus tiene piso en 0 y no tiene techo, por eso sirve para conteos. La lineal no tiene ni piso ni techo, por eso sirve para un precio. Y softmax no es una curva: si alguien la dibuja como curva, no la entendió. Cerrá con la pregunta de la diapositiva anterior si no la hiciste: ¿cuál para unidades vendidas?

### Presenter feedback

---

# 5. Medir un clasificador

**Goal of this section:** El modelo ya está diseñado y entrenado; ahora, ¿anda? La sección va en cadena y trabaja sobre dos clases de punta a punta: accuracy engaña, la matriz de confusión separa los cuatro tipos de resultado, de ahí salen precisión, recall y F1, con eso ya definido tres quiz obligan a elegir cuál duele en tres casos reales, y el umbral cierra mostrando que la elección es una perilla y no un destino. El caso multiclase queda como una nota al final. Nota: este tema no está en el corpus; el contenido viene del conocimiento del área (ver Open questions).

**Presenter feedback:**

---

## 1. El 99% de accuracy que no sirve

### Content

**Accuracy** es la fracción de predicciones correctas sobre el total.

```
              predicciones correctas
Accuracy  =  ------------------------
                total de casos
```

Un detector de fraude sobre 10.000 transacciones, donde 100 son fraude y 9.900 legítimas. La regla más tonta posible: decir siempre "no es fraude".

```ascii
  10.000 transacciones
  +-------------------------------------------------+---+
  |             9.900 legitimas                     |100|
  +-------------------------------------------------+---+
                                                      ^
                            el modelo dice "no es fraude" a todo

    aciertos           9.900 / 10.000  =  accuracy 99%
    fraudes detectados     0 / 100     =  se escapa el 100% de lo que importa
```
<!-- ascii-note:
intent: mostrar que el 99% de accuracy sale de la clase mayoritaria y que la clase que importa se pierde entera
emphasize: el contraste entre la barra enorme de legitimas y el bloque chico de fraudes; los dos numeros de abajo
labels: 9.900 legitimas, 100 fraudes, accuracy 99%, fraudes detectados 0
-->

- **Accuracy la escribe la clase mayoritaria.** Con clases desbalanceadas el número lo pone la clase grande, y el error que importa queda escondido adentro.
- **No todos los errores cuestan lo mismo.** Dejar pasar un fraude y molestar a un cliente legítimo con una alerta son errores distintos, con costos distintos. Accuracy los suma como si fueran iguales.
- **Hace falta separar los tipos de error,** no un solo número. Ahí entra la matriz de confusión.

### Sources

Conocimiento del área (no cubierto por el corpus). Ejemplo del detector de fraude, ilustrativo.

### Speaker notes

Arranque con gancho concreto: el clasificador que dice siempre "no". Es la mejor forma de que se les caiga la ficha de que accuracy sola no alcanza. Escribí la fórmula en el pizarrón antes de mostrar el diagrama y hacé la cuenta con ellos: 9.900 sobre 10.000. El golpe llega cuando pasás al segundo número, 0 sobre 100. Los números son ilustrativos, no un dato de una fuente; dejalo claro si alguien pregunta. Este es el puente desde la salida (sección 4, clasificación con sigmoide) hacia cómo se evalúa esa clasificación.

### Presenter feedback
- [closed] 2026-08-19 — "Falta agregar la formula de accuracy, es como que se habla pero no se explica"
  Resolution: La diapositiva abre con la definición y la fórmula en bloque propio (predicciones correctas sobre total de casos). La versión con TP y TN queda para la 5.3, donde esos términos ya están definidos.
- [closed] 2026-08-19 — "Creo que este slide pude tener un mejor exploy y diagrama que valas al punto"
  Resolution: El ejemplo pasó de "99 de cada 100" a 10.000 transacciones con 100 fraudes, que permite hacer la cuenta en voz alta. Se agregó un diagrama ASCII con la barra desbalanceada y los dos números enfrentados: accuracy 99% contra 0 de 100 fraudes detectados. Se retiró la plantilla `stat`, que ya no corresponde con un diagrama en la diapositiva.. 
---

## 2. La matriz de confusión

### Content

Para clasificación binaria, todos los resultados caen en una tabla de 2×2 que cruza lo que el modelo predijo con lo que era verdad.

```ascii
                        REALIDAD
                  Positivo      Negativo
              +-------------+-------------+
   PREDICHO   |     TP      |     FP      |   Positivo
              | (acierto)   | (falsa      |
              |             |  alarma)    |
              +-------------+-------------+
              |     FN      |     TN      |   Negativo
              | (se escapó) |  (acierto)  |
              +-------------+-------------+
```
<!-- ascii-note:
intent: la matriz de confusión 2x2 cruzando predicción y realidad
emphasize: las dos celdas de error FP y FN
labels: TP verdadero positivo, FP falso positivo, FN falso negativo, TN verdadero negativo
-->

- **TP (verdadero positivo):** era positivo y el modelo lo marcó. Acierto.
- **FP (falso positivo):** era negativo y el modelo lo marcó. Falsa alarma.
- **FN (falso negativo):** era positivo y el modelo lo dejó pasar. Lo más caro en fraude o diagnóstico médico.
- **TN (verdadero negativo):** era negativo y el modelo lo dejó pasar. Acierto.

### Sources

Conocimiento del área (no cubierto por el corpus).

### Speaker notes

El centro de la sección. Dibujá la matriz en el pizarrón mientras aparece en la diapositiva y pedí que ubiquen el ejemplo del fraude en cada celda. La confusión típica del alumno es FP vs FN; anclalo con el costo: en un test médico, un FN (mandar a casa a alguien enfermo) suele ser mucho peor que un FP (un estudio de más). Que se lleven que la matriz es la foto completa y accuracy es solo la diagonal sobre el total.

### Presenter feedback

---

## 3. Precision, recall y F1

### Content

De las cuatro celdas salen las métricas que de verdad describen a un clasificador.

**Precisión.** De todo lo que el modelo marcó, ¿cuánto era de verdad?

- Fórmula: `TP / (TP + FP)`. Sube cuando el modelo molesta poco con falsas alarmas.
- **Importa cuando** el falso positivo es caro: mandar a spam un mail importante.

**Recall.** De todo lo que había, ¿cuánto encontró?

- Fórmula: `TP / (TP + FN)`. Sube cuando se escapan pocos.
- **Importa cuando** el falso negativo es caro: no detectar una enfermedad o un fraude.

**F1.** ¿Y si las dos importan parecido?

- Fórmula: `2 · (P · R) / (P + R)`, la media armónica. La manda el número más chico: con precisión 0.9 y recall 0.5 el promedio da 0.70 y F1 da 0.64; con recall 0, F1 da 0.
- **Importa cuando** ninguna de las dos alcanza sola, como el caso de churn del quiz.

**Nota:** precisión y recall están en tensión. Subir una suele bajar la otra, y qué priorizar lo decide el costo del error, no la matemática.

### Sources

Conocimiento del área (no cubierto por el corpus).

### Speaker notes

Insistí en la intuición antes que en la fórmula. Precision responde "cuando dice que sí, ¿le creo?"; recall responde "de todos los que eran, ¿cuántos encontró?". El truco mnemotécnico: precisión mira la columna de predichos positivos, recall mira la fila de reales positivos. Si preguntan por qué media armónica y no promedio: el promedio deja que un 1.0 tape un 0.0, y un clasificador que marca todo tiene recall 1.0 con precision pésima. La armónica no lo permite, porque tiende al más chico de los dos. Hacé la cuenta de 0.9 y 0.5 en el pizarrón, son diez segundos y se entiende de una. F1 es útil pero peligroso si se reporta solo; siempre conviene mirar las dos. Si dan tiempo, escribí accuracy = (TP+TN)/total: es la misma fórmula de la 5.1, ahora con los cuatro términos ya definidos, y cierra el círculo de la sección.

### Presenter feedback
- [closed] 2026-08-19 — "Agregar en Precision, recall y F1 en cada box una descripcion de lo que es. Eg: Precicion es: Cuantos detected correctamente ?" / "'Importa...' que esta ahi deberia tener un especio de la descripcion que esta."
  Resolution: Cada métrica pasó a tres zonas separadas en vez de un párrafo corrido. Arriba el nombre y la pregunta en castellano que responde (precisión: de todo lo que marcó, ¿cuánto era de verdad?; recall: de todo lo que había, ¿cuánto encontró?; F1: ¿y si las dos importan parecido?). Debajo la fórmula y el comportamiento. Y aparte, con su propio espacio, el "Importa cuando". La diapositiva pasó de lista de cards a plantilla de columnas, que es la que da esas tres zonas. La tensión entre precisión y recall bajó a nota al pie.
- [closed] 2026-08-19 — "No se definio 'F1, media armónica'"
  Resolution: La card ahora abre con la fórmula `2 · (P · R) / (P + R)` y define la media armónica por contraste con el promedio común, con dos números concretos (0.9 y 0.5 dan 0.70 de promedio y 0.64 de F1). Las notas del orador suman el porqué de la armónica y el caso del clasificador que marca todo.

---

## 4. Quiz 1: el filtro de spam

### Content

Un filtro de spam. Bloquear un mail legítimo es peor que dejar pasar uno dudoso: el usuario perdona ver basura en la bandeja, no perdona perder una factura.

**¿Qué métrica priorizás?**

1. Precisión
2. Recall

**Respuesta: precisión.** El error caro es el falso positivo, marcar como spam algo que no lo era. Priorizar precisión significa que el filtro solo bloquea cuando está seguro, a costa de dejar pasar algo de spam.

<!-- template: quiz -->

### Sources

Conocimiento del área (no cubierto por el corpus). Caso ilustrativo.

### Speaker notes

El primero de los tres, y el más fácil. Pedí voto a mano alzada antes de revelar. Si alguien contesta recall, la pregunta que lo desarma: ¿qué preferís, ver tres spams por día o perder un mail de tu jefe?

### Presenter feedback
- [closed] 2026-08-19 — "El problema del quiz es que deberia ser 3 quiz la verdad donde esta la pregunta y luego seleciona precicion o recall"
  Resolution: El quiz único se partió en tres, uno por caso, cada uno con su pregunta y opciones reales para elegir: spam (precisión), enfermedad grave (recall) y churn (F1, con tres opciones). Así la mecánica de la plantilla funciona: hay una sola respuesta correcta por diapositiva y el renderer la resalta al avanzar. El caso de fraude no quedó como quiz porque no tiene respuesta única; pasó a las notas del orador de la tercera, como discusión abierta si sobra tiempo. Las diapositivas 4.1 a 4.3 anteriores del quiz único quedaron reemplazadas, y el umbral pasó de 5.5 a 5.7.

---

## 5. Quiz 2: el test de una enfermedad grave

### Content

Un test para detectar una enfermedad grave y tratable. Dejar ir a una persona enferma es peor que pedirle estudios extra a una sana.

**¿Qué métrica priorizás?**

1. Precisión
2. Recall

**Respuesta: recall.** El error caro es el falso negativo, no detectar a quien sí estaba enfermo. Priorizar recall significa que el test marca ante la duda, a costa de mandar a estudios a gente sana.

<!-- template: quiz -->

### Sources

Conocimiento del área (no cubierto por el corpus). Caso ilustrativo.

### Speaker notes

El espejo del anterior, y el contraste es el punto: mismo modelo, misma matemática, decisión opuesta. Lo que cambió no es técnico, es cuánto cuesta cada error. Acá es donde conviene decir en voz alta que la métrica la elige el negocio, no el modelo.

### Presenter feedback

---

## 6. Quiz 3: el modelo de churn

### Content

Un modelo que marca quién se va a dar de baja, y a cada marcado se le ofrece un descuento. Un descuento regalado a alguien que no se iba cuesta plata; un cliente que se va sin oferta también.

**¿Qué métrica priorizás?**

1. Precisión
2. Recall
3. F1

**Respuesta: F1.** Los dos errores cuestan parecido, así que optimizar una sola métrica deja la otra libre. F1 es el número que las mantiene atadas, y por eso es el caso donde sirve como número único.

<!-- template: quiz -->

### Sources

Conocimiento del área (no cubierto por el corpus). Caso ilustrativo.

### Speaker notes

El que cierra la secuencia y el que justifica F1. Los dos anteriores tenían un error claramente más caro; este no, y ahí es donde una sola métrica deja de alcanzar. Un cuarto caso para tirar en voz alta si sobra tiempo, sin diapositiva: una alerta de fraude donde el equipo puede revisar pocas alertas pero cada fraude no detectado cuesta caro. No tiene respuesta única, depende de la capacidad de revisión y del costo del fraude, y por eso funciona mejor como discusión abierta que como quiz.

### Presenter feedback

---

## 7. El umbral, una perilla de negocio

### Content

Un clasificador binario no devuelve "sí" o "no", devuelve una probabilidad. El **umbral** es el número que la convierte en decisión.

```ascii
        probabilidad que devuelve el modelo
   0.0 ----------------------------------------------- 1.0
              |                  |                |
           umbral 0.2        umbral 0.5       umbral 0.8

           marca mucho        el default       marca poco
           recall  alto                        recall  bajo
           precision baja                      precision alta
```
<!-- ascii-note:
intent: mostrar que mover el umbral sobre el eje de probabilidad intercambia recall por precision
emphasize: el eje 0.0 a 1.0 y las tres posiciones del umbral; el cruce de recall y precision entre los extremos
labels: probabilidad 0.0 a 1.0, umbral 0.2 / 0.5 / 0.8, recall, precision
-->

- **El umbral es una perilla de negocio.** Se mueve según cuál de los dos errores duele más. Dejarlo en 0.5 también es una decisión, no un default neutro.
- **La curva precision-recall** muestra ese intercambio para todos los umbrales de una vez, y sirve para comparar dos modelos sin fijar ninguno.

**Nota:** toda esta sección trabaja sobre dos clases. Con más de dos, la matriz crece a una fila por clase real y una columna por clase predicha, y precisión y recall se calculan por clase y se promedian. La idea es la misma.

### Sources

Conocimiento del área (no cubierto por el corpus).

### Speaker notes

El umbral es lo que más cuesta que entiendan y lo más útil en la práctica. Recorré el diagrama con el dedo, de izquierda a derecha, y que ellos digan qué pasa con cada métrica antes de que lo leas. Ejemplo para anclar: un modelo de fraude con recall bajo en 0.5 pasa a recall alto bajando el umbral a 0.2, a costa de más falsas alarmas que el equipo antifraude tendrá que revisar. Ahí se ve que es una decisión de operación y no de modelado. La nota del final va al pasar, en diez segundos: toda la sección es binaria a propósito, y con más clases la idea no cambia. Si alguien pregunta, el ejemplo concreto es un clasificador de diez dígitos que confunde el 4 con el 9 y nunca el 4 con el 0; eso se ve en la celda de la matriz y jamás en la accuracy. No lo desarrolles salvo que lo pidan. Si el tiempo aprieta, esta diapositiva se puede dar solo con el diagrama.

### Presenter feedback
- [closed] 2026-08-19 — "Ok, enfoquemosnos solo a 2 clases. Y poner solo una nota al final."
  Resolution: La sección queda binaria de punta a punta. La diapositiva pasó a llamarse "El umbral, una perilla de negocio", sin la matriz en el título, y el bloque de multiclase se redujo a una nota de dos líneas al pie: la matriz crece a una fila por clase real y una columna por clase predicha, precisión y recall se calculan por clase, y la idea no cambia. El ejemplo del clasificador de dígitos quedó en las notas del orador por si alguien pregunta. El goal de la sección dice ahora explícitamente que trabaja sobre dos clases.
- [closed] 2026-08-19 — "Que es 'la matriz N×N'?"
  Resolution: El término estaba en el título de la diapositiva y recién se explicaba en una línea al pie, o sea L8 al revés. La diapositiva pasó a llamarse "El umbral, y qué pasa con más de dos clases", sin jerga sin definir, y la línea de cierre pasó a definirla de verdad: una fila por clase real, una columna por clase predicha, la diagonal como aciertos y cada celda fuera de la diagonal diciendo con qué clase concreta se confundió cada una. Las notas suman el ejemplo del clasificador de dígitos que confunde el 4 con el 9.
- [closed] 2026-08-19 — "El slide deberi explicar un pocmo las de lo que se esta hablando. Es confuzo. Creo que se puede mostrar esto con un diagrama y menos texto."
  Resolution: La confusión venía de que la diapositiva hacía dos cosas a la vez. Ahora el umbral es el centro y se explica con un diagrama del eje de probabilidad con tres posiciones, que reemplaza los dos primeros bullets. Quedan dos cards en vez de cuatro, y la matriz N×N baja a una línea de cierre al pie. El texto se redujo a poco menos de la mitad.
- [closed] 2026-08-19 — "Mostrar 'la matriz N×N'. Tal vez el slide hay que partirlo en dos. Son dos conceptos distintos."
  Resolution: Este comentario quedó sin procesar porque estaba escrito sin espacio después del guion y el barrido no lo detectó. Pedía lo contrario de la instrucción posterior ("enfoquémonos solo a 2 clases, poner solo una nota al final"), que es la que vale por ser más reciente. La diapositiva no se parte: la matriz con más de dos clases queda como nota al pie y el ejemplo del clasificador de dígitos en las notas del orador. Si más adelante se quiere una diapositiva propia de multiclase, el material está en las notas.

---

# 6. Overfitting y regularización

**Goal of this section:** Diagnosticar y tratar, en ese orden. Primero definir overfitting como la brecha train-validación, dar el diagnóstico de tres casos y explicar el intercambio sesgo-varianza que justifica por qué regularizar empeora el entrenamiento a propósito. Después el tratamiento: L2 (weight decay) en detalle porque es el estándar y está en el título de la clase, L1 por contraste, dropout, y el resto del arsenal con la guía de cuál usar y los errores de aplicación.

**Presenter feedback:**
- [closed] 2026-08-19 — "Regularización y L2 no es parte de formas de solucional Overfeeting. No deberia estar en la misma seccion. ?"
  Resolution: Se fusionaron las secciones 6 y 7 en una sola, "Overfitting y regularización", con seis diapositivas: dos de diagnóstico y cuatro de tratamiento. La regularización es el tratamiento canónico del overfitting y las notas de la 6.1 ya la trataban como continuación, así que la división por secciones contradecía el arco. El mazo pasa de siete secciones a seis.

---

## 1. El diagnóstico en dos números

### Content

Overfitting es la brecha entre el error de entrenamiento y el de validación. El diagnóstico sale de mirar los dos juntos.

| Error de train | Error de validación | Diagnóstico | Qué hacer |
|---|---|---|---|
| Alto | Alto | Underfitting | Más capacidad |
| Bajo | Alto | **Overfitting** | Regularizar |
| Bajo | Bajo | Bien | Nada |

El síntoma es la separación: el error de train baja sin parar y el de validación deja de bajar y empieza a subir. La red dejó de aprender el patrón y empezó a memorizar los ejemplos.

<!-- generate-image: left | una brecha que se abre entre aprendizaje aparente y desempeño real, tensión entre memorizar y generalizar -->

### Sources

corpus/chat.md.md (§10 Regularización: qué problema resuelve)

### Speaker notes

Este es el mapa de decisión que ordena la segunda mitad de la sección. Insistí en el orden: primero se diagnostica, después se trata. Regularizar un modelo que hace underfitting (train alto) empeora las dos métricas. Conectá con el ID único de la sección 2: memorizar el DNI es overfitting en estado puro, train perfecto y validación mala.

### Presenter feedback

---

## 2. Sesgo contra varianza

### Content

La regularización no mejora el ajuste. Lo empeora a propósito en entrenamiento, a cambio de que el modelo generalice mejor a datos nuevos. La brecha de la diapositiva anterior se ve así a lo largo del entrenamiento:

```ascii
error
  |\                         curva de validación
  | \                    __/  (vuelve a subir)
  |  \___             __/
  |      \______   __/   <-- acá empieza a sobreajustar
  |             \_/______  curva de entrenamiento (sigue bajando)
  +------------------------------> épocas
```
<!-- ascii-note:
intent: curvas de train y validación que se separan (overfitting = alta varianza)
emphasize: el punto donde validación deja de bajar y empieza a subir
labels: eje x épocas, eje y error, dos curvas train y validación
-->

- **Mucha capacidad da alta varianza:** el modelo pasa exactamente por cada punto de train, incluido el ruido, y cambia mucho con datos nuevos. Es la curva de validación que sube.
- **Poca capacidad da alto sesgo:** no captura el patrón ni en train.
- **Regularizar es un intercambio explícito:** se acepta un poco más de sesgo (peor ajuste en train) para bajar la varianza (mejor desempeño fuera de train).
- **El objetivo nunca fue el error de train.** Un modelo que ajusta perfecto lo que ya vio y falla en lo nuevo no sirve para nada.

### Sources

corpus/chat.md.md (§10 Regularización: qué problema resuelve)

### Speaker notes

El intercambio sesgo-varianza es el fundamento teórico de todo lo que viene. La metáfora que funciona: estudiar para un examen memorizando las respuestas de los ejercicios viejos (varianza alta, te va mal con ejercicios nuevos) contra entender el método (algo de sesgo, generaliza). Preparen el terreno: todas las técnicas que vienen a continuación son formas distintas de bajar varianza.

### Presenter feedback

---

## 3. L2: penalizar los pesos grandes

### Content

L2 agrega un término al objetivo que penaliza los pesos grandes:

```ascii
   J  =  cost  +  λ · Σ w²
         \___/     \______/
         ajuste    penalización
                   (empuja cada w hacia 0)
```
<!-- ascii-note:
intent: descomponer el objetivo con el término de regularización L2
emphasize: el término lambda por suma de w al cuadrado
labels: J objetivo, cost ajuste, término L2
-->

- **Pesos chicos, función suave.** Un peso grande hace que la salida sea muy sensible a esa entrada. Con pesos chicos la función aprendida es más suave, y una función suave no puede pasar exactamente por cada punto de entrenamiento, que es justo lo que hace el overfitting.
- **Weight decay, el otro nombre.** El gradiente del término λΣw² empuja cada peso un poco hacia cero en cada paso.
- **λ, el hiperparámetro.** Típicamente entre 1e-5 y 1e-2. En PyTorch: `Adam(params, weight_decay=1e-4)`.
- **El sesgo queda afuera.** El bias no controla la sensibilidad a la entrada, así que no se penaliza. En inferencia L2 no hace nada, ya quedó incorporado en los pesos.

### Sources

corpus/chat.md.md (§10 Regularización: L2 weight decay)

### Speaker notes

El tema del título, dedicale tiempo. El "por qué funciona" es lo importante: pesos grandes, función que oscila para tocar cada punto; pesos chicos, función suave que generaliza. Dibujá dos ajustes sobre los mismos puntos, uno que serpentea y uno suave. Aclará el detalle del bias, que a casi nadie le queda claro: penalizás pesos, no sesgos, porque el bias solo desplaza, no amplifica la entrada.

### Presenter feedback

---

## 4. L1 contra L2

### Content

Misma idea, otra norma: L1 penaliza con el valor absoluto en lugar del cuadrado.

- **L2 penaliza `w²`:** reduce todos los pesos sin llevarlos a cero. Resultado, pesos parejos y chicos. Es el estándar en redes.
- **L1 penaliza `|w|`:** lleva los pesos chicos exactamente a cero. Resultado, una solución rala que selecciona features. Se usa más en modelos lineales (Lasso) que en redes.
- **Elastic net combina las dos.** Rara vez hace falta en una red.

La diferencia práctica: si querés que el modelo descarte features solo, L1. Si querés que ningún peso domine, L2.

### Sources

corpus/chat.md.md (§10 Regularización: L1)

### Speaker notes

Comparación corta, no te extiendas. El punto geométrico, si quieren profundizar: la bola L1 tiene puntas sobre los ejes, y ahí es donde el óptimo tiende a caer con alguna coordenada en cero (rala). La bola L2 es redonda, empuja parejo. Para la clase alcanza con "L1 selecciona, L2 empareja".

### Presenter feedback

---

## 5. Dropout: no depender de ninguna neurona

### Content

Durante el entrenamiento, dropout apaga al azar una fracción de las neuronas en cada paso hacia adelante.

- **Apagado al azar.** Cada neurona se apaga con probabilidad p, típico 0.2 a 0.5 en capas ocultas. La red no puede depender de ninguna neurona en particular, así que reparte la representación en vez de armar detectores frágiles.
- **Un ensamble implícito.** Muchas subredes que comparten pesos, entrenadas en simultáneo.
- **En inferencia se desactiva.** Todas las neuronas quedan activas. En PyTorch, `nn.Dropout(0.2)`.
- **El bug clásico.** Olvidar `model.eval()` deja dropout activo en inferencia, y el modelo devuelve predicciones distintas en cada llamada. Le pasa también a BatchNorm.

### Sources

corpus/chat.md.md (§10 Regularización: Dropout)

### Speaker notes

El `model.eval()` es el bug de PyTorch que van a cometer sí o sí en la práctica; que suene fuerte ahora para que lo recuerden después. La lectura de ensamble es elegante: en cada paso entrenás una subred distinta, y en inferencia usás el promedio. Dato para el que pregunte por qué en visión moderna casi no se usa dropout: se lleva mal con BatchNorm (lo vemos en la próxima slide).

### Presenter feedback

---

## 6. El resto del arsenal y cuál usar

### Content

Hay más de una herramienta, y la mejor a veces no es la más sofisticada.

- **Early stopping:** cortar el entrenamiento cuando la validación deja de mejorar. Gratis, sin hiperparámetro que calibrar, funciona con cualquier arquitectura. Es el que más rinde y el que menos se menciona.
- **Más datos:** ataca la causa, no el síntoma. Caro, pero es el mejor remedio.
- **Data augmentation:** generar variantes del dato (recortes, giros, ruido). Muy efectivo en visión.
- **Reducir capacidad:** menos capas o neuronas. Simple y directo.

Guía rápida por caso:

| Situación | Elegir |
|---|---|
| Tabular, red chica | L2 + early stopping |
| Red profunda | Dropout + L2 |
| Visión | Data augmentation, después dropout |
| Transformers | Dropout bajo (0.1) + weight decay |

### Sources

corpus/chat.md.md (§10 Regularización: el resto del arsenal; cuál usar)

### Speaker notes

Early stopping es el que quiero que se lleven como primer reflejo: cero costo, siempre conviene. La tabla es de referencia, no la leas entera. Tres matices para no aplicar mal, si hay tiempo: regularizar sin overfitting empeora las dos métricas; dropout y BatchNorm se llevan mal (dropout cambia la varianza que BatchNorm acaba de normalizar); y weight decay sobre embeddings castiga a las categorías raras que no aparecieron en el batch, justo las que menos entrenadas están.

### Presenter feedback

---

# Conclusions

## 1. Lo que hay que llevarse

### Content

- **El diseño está en la entrada y la salida.** La cantidad de capas importa poco; cómo se codifica cada variable y cómo se modela la respuesta es donde se gana o se pierde el modelo.
- **La red solo ve floats.** Codificar mal es fatal porque el error entra silencioso y ninguna arquitectura lo corrige. La pregunta de la resta ordena casi toda la decisión de codificación.
- **La partición decide si la métrica dice la verdad.** Train para aprender, validación para decidir, test una sola vez al final. Y todo lo que se aprende de los datos, μ y σ incluidos, se aprende solo del train.
- **Accuracy sola engaña.** La matriz de confusión separa los tipos de error; precision, recall y F1 describen lo que accuracy esconde, y el umbral es una perilla de negocio.
- **Regularizar es bajar varianza a propósito.** Primero se diagnostica el overfitting (brecha train-validación), después se trata: L2 de base, dropout en redes profundas, early stopping casi siempre.

### Sources

corpus/chat.md.md (§9, §10, §13); conocimiento del área (sección 5)

### Speaker notes

Recapitulá siguiendo el recorrido del dato: se codificó (entrada), se partió (dataset), salió (salida), lo medimos (clasificador) y lo cuidamos (regularización). Cinco ideas, una por sección troncal. Dejá espacio para preguntas antes del checklist.

### Presenter feedback

---

## 2. Checklist operativo para la práctica

### Content

Para cada variable de un problema real, antes de tocar la red:

- **¿Es número, categoría, ciclo, fecha o texto?** Define la familia de codificación.
- **¿Qué significa la resta entre dos valores?** Decide float, ordinal, one-hot o embedding.
- **¿Cuántos valores distintos tiene?** One-hot o embedding según la cardinalidad.
- **¿Puede faltar, y faltar significa algo?** Imputación más flag, o categoría propia.
- **¿La voy a tener disponible al momento de predecir?** Si no, no es una feature.

Para la salida: ¿qué pregunta responde el modelo, necesita un valor o un rango, las clases son excluyentes, el valor tiene que ser positivo? Con eso resuelto, la cantidad de neuronas sale sola.

### Sources

corpus/chat.md.md (§12 Checklist operativo)

### Speaker notes

Cierre accionable. Este checklist es directamente aplicable al TP o al dataset con el que trabajen. Sugiero dejarlo como material de la clase. Si hay práctica a continuación, este es el puente: que apliquen el checklist a un dataset real antes de escribir una sola línea de la red.

### Presenter feedback

---

# Open questions

- Sección 5 (Medir un clasificador) no está cubierta por el corpus (`chat.md.md`). El contenido viene del conocimiento del área. Si el presentador quiere anclarlo a una fuente propia (apunte, capítulo, ejemplo con números reales de un dataset del curso), conviene sumarla en la Colecta y re-verificar los números. El ejemplo del "99% de accuracy" y los costos FP/FN son ilustrativos, no datos de una fuente.
- La fuente advierte que en datos tabulares una red suele perder contra gradient boosting (XGBoost, LightGBM). Está en las notas del orador (slide 1.3) como contrapunto honesto. Decidir si darle más aire en clase o dejarlo como comentario al pasar.
- Duración: 34 diapositivas de contenido, con el mismo presupuesto de 90 minutos. La ronda del enfoque MLP sumó una diapositiva (la 1.5) y aligeró la 2.1, así que el balance queda parejo. Sigue siendo el punto que más conviene mirar, y conviene cronometrar un pase completo antes de la clase. Candidatas a recortar, en este orden: slide 6.4 (L1 contra L2), slide 3.4 (errores de partición, dejando los dos primeros bullets más el código) y slide 5.7 (el umbral), que ya quedó aligerada y se puede dar solo con el diagrama.
- Diagramas: 10 (formas de input por arquitectura, neurona, activaciones ocultas, one-hot, partición, activaciones de salida, desbalance de accuracy, matriz de confusión, umbral, curvas de overfitting, objetivo L2). El de formas de input reemplaza al de formas de tensor, retirado con el vocabulario de tensor.
- Las dos directivas `generate-image` (slides 1.1 y 6.1) siguen sin cumplir: ninguna sesión tuvo capacidad de generación de imágenes. Las diapositivas conservan su texto y no dependen de ellas.
- Ninguna de las dos fuentes nuevas cubre partición estratificada ni partición temporal, y las dos importan para los trabajos que entregan los alumnos. En la diapositiva 3.4 están como aporte del docente, sin fuente detrás. Si se quiere anclar, hace falta sumar una tercera fuente en la Colecta.
- Los ratios 70/20/10 y 80/10/10 son recomendación de la casa de Roboflow (contenido de marketing de producto), no resultado de un estudio. Están citados como criterio práctico de la industria; si alguien en clase pregunta de dónde salen, esa es la respuesta honesta.
- El artículo de Roboflow está escrito para visión por computadora y esta clase es tabular. Los ejemplos se trasladaron (imágenes a filas), la lógica no cambió. Revisar en el ensayo que no quede ningún resto de vocabulario de visión.
- El framing MLP de la sección 1 (diapositivas 1.2 y 1.5) viene de una exploración del presentador en un chat, no del corpus. El corpus respalda las familias de estructura y su arquitectura natural (§2), los umbrales de one-hot contra embedding (§4) y la normalización z-score (§5), pero no el ejemplo de MNIST 28x28 con 784 posiciones ni el contraste de tres arquitecturas tal como quedó armado. Si se quiere anclar, la exploración se puede sumar en la Colecta como fuente propia.
- Las citas de Keras y PyTorch sobre el aplanado (notas del orador de la 1.2) están verificadas contra la documentación oficial pero no viven en el corpus. Ingerir las dos páginas si se las quiere como fuente formal de la Talk.

# Cut material

## Diapositiva 2.1 "Todo termina en un vector de floats" — tabla de seis familias de estructura (recortada por feedback, 2026-08-20)

Se retiró al declararse el alcance MLP en la sección 1. La tabla listaba seis familias (sin estructura, grilla 1D, grilla 2D, secuencia, conjunto, grafo) con su arquitectura natural, y quedaba solapada con la tabla de tres arquitecturas de la diapositiva 1.2 y con la tabla de tipos de dato de la 1.5. La 2.1 pasó a definir solo el caso tabular.

## 1. Todo termina en un vector de floats

### Content

El input es todo lo que sabés del problema, convertido a números. Vamos a concentrarnos en el primer caso, **sin estructura (tabular)**: una fila por ejemplo y una columna por variable, sin vecindad ni orden intrínseco entre las columnas. Lo que cambia entre un caso y otro es qué significa la posición dentro del vector, y eso determina la arquitectura natural.

| Estructura | Qué es | Ejemplos | Invariancia | Arquitectura |
|---|---|---|---|---|
| Sin estructura (tabular) | Filas y columnas, sin vecindad ni orden intrínseco entre columnas | Cliente (edad, ingreso, barrio), solicitud de préstamo, ficha clínica | El orden de las columnas | Fully connected |
| Grilla 1D (señal) | Muestras tomadas a intervalos regulares sobre un eje continuo | ECG, audio, vibración de una máquina, temperatura horaria | Desplazar en el tiempo | Conv 1D, RNN, Transformer |
| Grilla 2D (imagen) | Píxeles con vecindad en dos ejes | Radiografía, foto satelital, captura de pantalla | Desplazar en el espacio | Conv 2D |
| Secuencia | Elementos discretos de un vocabulario, en orden y de largo variable | Reseña, log de eventos, código fuente, cadena de ADN | Nada, el orden es todo | Transformer |
| Conjunto | Elementos sin orden y en cantidad variable | Carrito de compras, síntomas de un paciente, hashtags de un post | El orden de los elementos | Deep Sets, attention |
| Grafo | Nodos y aristas, sin numeración canónica | Transferencias entre cuentas, red social, molécula | Renumerar los nodos | GNN |

Señal y secuencia se confunden seguido y son distintas. La señal está muestreada a intervalos regulares y una ventana de 50 muestras significa lo mismo al principio o al final; la secuencia es una lista de símbolos de un vocabulario, sin intervalo temporal fijo y sin invariancia por desplazamiento.

La pregunta que ordena todo el zoológico: **¿qué transformaciones puedo aplicarle al input sin cambiar la respuesta correcta?** Esa invariancia elige la familia de arquitectura.

### Sources

corpus/chat.md.md (§2 El input: principio general)

### Speaker notes

Este marco es elegante y vale la pena bajarlo despacio. Definí "sin estructura" en contraste con una imagen: en una tabla, intercambiar dos columnas no cambia el significado si el modelo conserva sus nombres; no hay píxeles vecinos ni orden temporal que explotar. La confusión que más aparece es señal contra secuencia: el audio es señal (muestreo regular, invariante al desplazamiento), el texto es secuencia (símbolos discretos, largo variable, sin invariancia). El ADN sirve de ejemplo tramposo porque parece señal y es secuencia. Para el resto de la clase nos quedamos en el caso tabular, el más común en problemas de negocio y donde las decisiones de codificación se ven más claras. Usá los ejemplos de la tabla para que cada familia tenga una imagen mental. Mencioná que texto e imágenes terminan también en un vector de tamaño fijo (un embedding) y de ahí vuelven al caso simple.


## Diapositiva 4.4 "Dos formas de modelar mal la salida" (retirada por feedback, 2026-08-19)

Se retiró por pedido del presentador. El contenido queda archivado acá:

- **Softmax donde iba sigmoide.** Softmax fuerza a que las clases compitan y sumen 1, así que solo sirve cuando las etiquetas son excluyentes. Un ticket puede ser "urgente" y "de facturación" a la vez: ahí la salida está mal modelada de raíz y van N sigmoides independientes, una por etiqueta.
- **Predecir un punto cuando el negocio pedía un rango.** Si la decisión depende del peor escenario (cuánto stock, cuánto riesgo, cuánta capacidad), un valor puntual no alcanza. Ahí van cuantiles o una distribución.

Los dos errores comparten causa: la salida se eligió mirando la arquitectura en vez de la pregunta del negocio.

Notas del orador que se pierden con ella: el ejemplo del ticket multi-etiqueta, la pregunta de control (¿clasificar géneros de una película es softmax o sigmoide? sigmoide, porque puede ser comedia y drama) y el remate de que modelar la salida es una decisión de producto, no solo técnica.

Fuente: corpus/chat.md.md (§8 Los dos errores más comunes).

## Desglose en tres baldes de la diapositiva 1.2 (reemplazado por feedback, 2026-08-19)

La versión anterior de la diapositiva 1.2 organizaba el diseño en tres baldes en vez de listar los aspectos de la clase. Se reemplazó por pedido del presentador; el contraste final sobrevive como remate de la diapositiva nueva, y este es el detalle que se retiró:

- **Lo determina la tarea (no se decide):** cantidad de neuronas de salida, activación de salida y función de loss. Predecir un precio pide una salida lineal con MSE; clasificar en N clases pide softmax con cross-entropy. No hay margen.
- **Lo determina la codificación (crítico):** cantidad de neuronas de entrada y si se normaliza. Salen de cómo se representan las variables, y es donde se gana o se pierde el modelo.
- **Lo que sí se elige (importa poco):** cantidad de capas ocultas (1 a 3 alcanza para datos tabulares), ancho de cada capa (potencias de 2, decreciente) y activación oculta (ReLU salvo motivo).

Fuente: corpus/chat.md.md (§9 Diseño de la red: qué se decide y qué no).

## Diapositiva 2.6 "μ y σ: el modelo no son solo los pesos" (retirada por feedback, 2026-08-19)

La diapositiva se retiró de la sección 2 por pedido del presentador. **El contenido no se descartó:** el bloque de código MAL/BIEN, los tres bullets (data leakage, el artefacto de producción completo, el bug silencioso) y las notas del orador pasaron a la diapositiva 3.3 "Todo lo que se aprende sale solo del train", donde el tema queda mejor apoyado porque la partición ya está explicada. Se le sumó ahí un bullet nuevo sobre la diferencia entre aplicar la transformación (a los tres conjuntos) y calcular sus parámetros (solo sobre train).

## Activación y loss se eligen juntas (retirada por feedback)

- `BCEWithLogitsLoss` y `CrossEntropyLoss` ya incluyen la sigmoide y el softmax por estabilidad numérica. Si además se pone la activación en la capa, se aplica dos veces y el modelo entrena mal.
- En inferencia, con logits crudos: `prob = torch.sigmoid(model(x))`. Un logit de 2.3 no es una probabilidad.
- Fuente: corpus/chat.md.md (§8 El detalle de implementación; los pares que no se rompen).
