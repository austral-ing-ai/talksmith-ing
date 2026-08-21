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

**Claim:** En un MLP, casi nada de lo que decide el resultado es la arquitectura. Se decide antes, en cuatro lugares: cómo se codifica la entrada, cómo se parte el dataset, qué forma tiene la salida y qué fórmula mide el error. Backpropagation es el mecanismo que convierte ese error en pesos corregidos, y no es una decisión de diseño sino la condición para que las cuatro anteriores importen. Lo que separa un modelo que entrena de uno que sirve es lo último: medirlo sin engañarse y frenar el overfitting.

**Why it matters:** Una red no ve un cliente, una imagen ni un contrato: ve una fila de números. Si la información que importa quedó mal codificada, ninguna cantidad de capas la recupera, y la mayoría de los errores de producción en ML nacen en la frontera entre el dato crudo y el modelo. En el medio está la partición del dataset, que no cambia el modelo pero decide si la métrica dice la verdad: medir con los mismos datos con los que se entrenó es tomar examen con las respuestas a la vista. La salida y la función de pérdida vienen juntas y las determina la tarea, no el gusto de quien entrena. Abrir backpropagation importa porque es donde se entiende qué se ajusta y cuándo, y de ahí salen las perillas que uno toca cuando el entrenamiento no anda. Del otro lado, un modelo con 99% de accuracy puede ser inútil y uno que ajusta perfecto en entrenamiento puede fallar en cada caso nuevo. Codificar bien, partir bien, modelar bien la salida y su pérdida, saber medir y saber regularizar cubre el 80% de las decisiones reales.

**Presenter feedback:**
- [closed] 2026-08-21 — "Que el editor revise en forma critica el contenido de la presentacion" (revisión Composer, scope=full) — **blocker: la tesis contradecía al mazo.**
  Resolution: El `Claim` decía que el diseño "se decide casi entero en tres lugares" (entrada, dataset, salida), mientras que la diapositiva 1.4 enumera seis decisiones y el mazo tiene ocho secciones, dos de las cuales (pérdida y backpropagation) la tesis no mencionaba: 16 diapositivas, el 31% de la clase, colgando fuera de la tesis. Cuando se agregaron esas dos secciones se actualizó la agenda y no la tesis. El `Claim` pasa a cuatro lugares de decisión (entrada, dataset, salida, pérdida), declara backpropagation como mecanismo y no como decisión de diseño —que es exactamente lo que ya decían las notas del orador de la 1.4— y deja medir y regularizar como el cierre. El `Why it matters` suma la frase de que salida y pérdida vienen juntas y el porqué de abrir backpropagation.
- [closed] 2026-08-20 — "Y tal vez el titulo sea Modelado de Multi Layer Perceptron (para ser mas especifico)"
  Resolution: El campo class del frontmatter pasó de 'Diseño de redes neuronales: del dato a la predicción' a 'Modelado de un Multi-Layer Perceptron (MLP)'. Es el rótulo que el renderer pone en la portada bajo la materia.


---

# Agenda

**Narrative arc:** La clase sigue el recorrido de un dato a través de la red. Primero, qué se decide de verdad al diseñar (casi todo está en la entrada y la salida). Después el input en detalle: cómo un problema cualquiera se convierte en un vector de floats. Con el dato ya codificado, qué se hace con el dataset antes de entrenar: partirlo en tres, que es lo que vuelve honesta cualquier métrica posterior. Luego el output: cómo la tarea determina cuántas neuronas y qué activación lleva la última capa. Con la salida definida, qué fórmula convierte una predicción equivocada en un número, y cuál corresponde a cada familia de problema. Con el modelo completo, cómo se corrigen los pesos: el ciclo hacia adelante y hacia atrás, el reparto de la culpa capa por capa, y en qué momento exacto del entrenamiento se aplica el ajuste. Con la red ya entrenada, cómo se mide de verdad su desempeño con la matriz de confusión (accuracy sola no alcanza). Y para cerrar, el problema que arruina modelos que parecían buenos, el overfitting: cómo se diagnostica y cómo se trata, con L2 al frente del arsenal.

**Sections (in delivery order):**

- 1. Qué se diseña de verdad
- 2. Modelar la entrada
- 3. Partir el dataset
- 4. Modelar la salida
- 5. La función de pérdida
- 6. Backpropagation
- 7. Medir un clasificador
- 8. Capas ocultas
- 9. Overfitting

**Presenter feedback:**
- [closed] 2026-08-21 - "'Las activaciones ocultas, y como se ven' creo que deberiamos movela a un seccion que sea Hidden Layers y agregar un par de slides con recomendaciones sobre esta." El presentador eligio la opcion 1: al final, justo antes de Overfitting.
  Resolution: Seccion 8 nueva, Capas ocultas, entre 'Medir un clasificador' y 'Overfitting', que paso a ser la 9. Tres diapositivas: 'Cuantas capas y cuanto ancho' (nueva), 'Las activaciones ocultas, y como se ven' (movida desde la 1.7) y 'Como arrancan los pesos' (nueva). La seccion tapa un agujero real: 'Lo que hay que disenar' promete seis decisiones y la sexta, capas y neuronas, era la unica sin seccion propia. La costura con Overfitting es deliberada: capacidad de mas es lo que la seccion 9 diagnostica. La seccion 1 quedo en 6 diapositivas y su referencia a las activaciones apunta ahora a la seccion 8. Renumeradas las referencias cruzadas a la vieja seccion 8 (nota de la 5.2 y fila de la tabla de 6.10).
- [closed] 2026-08-19 — "En casi todos los slides es confusdo que no se define y en algunos caso se empieza con ejemplos." / "Lo que quise decir es que en los cards veo que se empieza definiendo ejemplo y no se define. No veo consistencia."
  Resolution: Se fijó una regla de card para todo el mazo y se barrieron las que no la cumplían. **La etiqueta en negrita nombra la cosa; la oración que sigue la define o la afirma; el ejemplo viene después de la definición, nunca antes.** Corregidas: 1.3 (la tercera card rompía el patrón término-definición de sus hermanas), 2.3 (la card de log abría con una lista de ejemplos), 2.5 (las cuatro abrían con el ejemplo y nunca definían el error), 4.3 (la de softmax abría con el ticket), 7.1 y 7.3 (etiquetas mezcladas entre pregunta, consecuencia y término; pasaron todas a sintagma nominal).
- [closed] 2026-08-21 — "En el corpus se discution barstante como es el algorithmo de backprograpagion. Agreguemos una seccion sobrre esto. Es importante en el plicat como se parte en training en batches, los cuales se procesan y se ajutan por neurona despues del forwatd para atras, luego de que se proceso to ese batch, se ajusta los valores. Ese batch es distitinto del epoch"
  Resolution: Sección 6 nueva, 'Cómo aprende la red: backpropagation', con siete diapositivas: el ciclo hacia adelante y hacia atrás, la función de coste como el número que hay que derivar, la regla de la cadena en tres factores, el delta, la propagación del delta hacia atrás, el paso de actualización con la tasa de aprendizaje, y batch contra época. El algoritmo salió de knowledge-library/backpropagation, curado desde la Talk intro-redes-neuronales, y se reusaron sus cinco imágenes de fórmulas sin volver a dibujarlas (la sexta, el diagrama forward/backward, tenía párrafos en inglés y se reemplazó por un ASCII propio en español). La mecánica de batches es aporte propio: el train se parte en batches de tamaño fijo, las B filas hacen el forward con los mismos pesos, se promedia su loss, y el ajuste se aplica una sola vez cuando terminó el batch entero; una época son tantos ajustes como batches tenga el train.

---

# 1. Qué se diseña de verdad

**Goal of this section:** Reencuadrar el diseño de una red y dar el vocabulario mínimo. La intuición del alumno suele estar en "cuántas capas, cuántas neuronas"; el mensaje es que esas decisiones importan poco y que el trabajo real está en cómo entra y cómo sale el dato. Deja cinco cosas: que la forma del input la decide la arquitectura, qué es exactamente un MLP y que es el alcance de la clase, cuáles son las seis decisiones que recorre la clase, qué es una neurona y su activación con las cuatro ocultas y sus formas, y de qué está hecho el vector de entrada.

**Presenter feedback:**
- [closed] 2026-08-21 — "'La forma la decide la arquitectura' creo que en vez de enfocarse todo en una imagen deberia ser datos de una tabla, imagen, señal, imagen RGB. Y dependiendo del dato es que cambia la arquitectura." / "Revisa ese slide y el ASCII para que refleje esto."
  Resolution: La diapositiva invirtió la causalidad y pasó a llamarse 'El dato decide la arquitectura'. Antes recorría **una sola** imagen de 28x28 contra tres arquitecturas; ahora recorre **cuatro tipos de dato** (tabla, señal 1D, imagen en escala de grises, imagen RGB), la forma natural de cada uno y la arquitectura que le corresponde. El ASCII se rehízo entero: cuatro paneles en dos filas, cada uno con el dato tal como es, la forma en que llega a la red y el nombre de la arquitectura. La tabla pasó de 'Arquitectura | Qué input espera | Por qué' a 'Dato | Su forma natural | Arquitectura'. Se respetaron los tres [closed] anteriores sobre esta diapositiva: no se explica cómo funciona una convolución, RGB no se describe como matrices apiladas sino como tres números en el mismo píxel, y la declaración de alcance MLP sobre datos tabulares sigue cerrando.
- [closed] 2026-08-21 — "Mover slide 7 despues del slide 5." / "Quiero decir, 'Una neurona, en una línea' quedaria mejor como bullets numerados."
  Resolution: 'Una neurona, en una línea' se movió de la posición 5 a la 4, o sea justo detrás del quote 'Qué es un MLP', y 'Lo que hay que diseñar' pasó a la 5. El orden ahora es definir el MLP, mostrar su átomo, y recién después la agenda de decisiones. Su contenido pasó de tres cards etiquetadas a **cuatro bullets numerados** que siguen el recorrido de la señal: entradas, pre-activación, activación, y la elección de `f`. El diagrama se conserva.
- [closed] 2026-08-21 — "Borrar 'One-hot contra embedding: con muchas categorías posibles, one-hot da vectores enormes y casi todos ceros, y el embedding las comprime en pocas dimensiones densas que además aprenden qué categorías se parecen. Los dos puntos son el material de la sección que sigue.'"
  Resolution: Se retiró el bullet de la diapositiva 'Una posición por variable'. El tema está desarrollado entero en la 2.4 'Categóricas: one-hot contra embedding', así que acá era un anticipo que no hacía falta. La diapositiva pasó de tres cosas que se confunden a dos, y el remate quedó apuntando solo a la escala.
- [closed] 2026-08-20 — "Creo que tenemos que ser claros en el foco. La presentacion va a ser modelado MLP. Entonces, no hablamos mas de tensores por que es confuso. Es decir, los slide 2 al 5 (este nuevo es el 5) tienen que proveer este framing."
  Resolution: Se sacó el vocabulario de tensor del mazo entero: tesis, objetivo de la sección 1, título y apertura de la 1.1, título de la 2.6 y la 2.2. En su lugar, 'una fila de números'. Las diapositivas 1.2 a 1.5 quedaron como el bloque que fija el framing MLP, con la 1.5 nueva, y las activaciones ocultas pasaron a 1.6.


---

## 1. La red ve una fila de números

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

## 2. El dato decide la arquitectura

### Content

Cada tipo de dato tiene una **forma natural**: cuántos ejes necesita para no perder información. Esa forma es la que decide qué arquitectura le corresponde, y no al revés.

```ascii
   TABLA                              SENAL 1D  (audio, ECG)

   edad  ingreso  zona                    /\      /\   /\
   ----  -------  ----                   /  \    /  \ /  \
    34    52000    12                   /    \  /    V
    41    38000    07                  /      \/

   -> [ ][ ][ ] ... [ ]                -> [x1][x2][x3] ... [xT]
      una fila de n numeros               una secuencia de T pasos
      MLP                                 CNN 1D / RNN


   IMAGEN EN GRISES                   IMAGEN RGB

   +---------------+                  +---------------+
   |               |                  |      [*]      |   cada pixel
   |    28 x 28    |                  |               |   guarda tres
   |               |                  |    28 x 28    |   numeros: R G B
   +---------------+                  +---------------+

   -> una grilla alto x ancho         -> la misma grilla,
      CNN                                3 numeros por pixel
                                         CNN
```
<!-- ascii-note:
intent: mostrar cuatro tipos de dato, la forma natural de cada uno y la arquitectura que le corresponde
emphasize: que lo que cambia entre los cuatro es la cantidad de ejes que hace falta para no perder informacion; el pixel ampliado de RGB que guarda tres numeros en el mismo punto, no tres grillas
labels: TABLA fila de n numeros MLP, SENAL 1D secuencia de T pasos CNN 1D o RNN, IMAGEN EN GRISES grilla alto por ancho CNN, IMAGEN RGB la misma grilla con 3 numeros por pixel CNN; cuatro paneles en dos filas, mismo lienzo y mismos margenes
-->

### Sources

corpus/chat.md.md (§2 El input: principio general — familias de estructura y su arquitectura natural)
784 = 28 × 28 — ejemplo aportado por el presentador (MNIST), no figura en el corpus

### Speaker notes

Esta diapositiva fija el alcance de la clase y conviene darla despacio, porque todo lo que sigue se apoya en ella. Recorré los cuatro paneles en orden y en cada uno hacé la misma pregunta: ¿cuántos ejes hacen falta para no perder nada? Uno, uno, dos, dos.

La pregunta que funciona antes de mostrarla: si les paso una foto de 28 por 28 en escala de grises, ¿cuántos números son? Respuesta, 784. Sirve para que dimensionen, y para que se vea que aplanar siempre se puede.

El punto que más rinde es el que ordena la diapositiva: la forma no es una decisión de diseño, viene con el dato. Lo que uno elige es si la arquitectura la aprovecha. Un MLP no tiene ningún mecanismo para saber que dos píxeles son vecinos, así que le da lo mismo el orden; por eso la fila aplanada le sirve y por eso la tabla es su caso natural.

Dos matices que el diagrama no dice con todas las letras y conviene decir vos: en una imagen importa qué píxel está al lado de cuál, y en una señal importa el orden de los pasos. Esa vecindad es lo que un MLP no tiene forma de aprovechar, y es la razón de que existan las otras arquitecturas.

Sobre el panel de RGB, que es el que más se malinterpreta: son tres números en el mismo punto, no tres grillas. El píxel ampliado del dibujo es para eso. De los tres ejes, el de color es el único que se podría reordenar sin cambiar el problema; alto y ancho no.

Por si alguien pregunta si el aplanado es automático: no lo es. Una capa densa opera solo sobre el último eje (Keras: "Dense computes the dot product between the inputs and the kernel along the last axis"; PyTorch nn.Linear: "all but the last dimension are the same shape as the input"). Aplanar es una capa que uno pone, `Flatten()` en Keras o `nn.Flatten()` en PyTorch.

No te metas con cómo funciona una convolución ni con attention. Alcanza con que quede claro que existen, que les corresponde otra forma de dato, y que de acá en adelante la clase modela un MLP sobre datos tabulares.

### Presenter feedback
- [closed] 2026-08-21 - Revisa el slide 4 que quedo mal. / El problema es el texto del alcance de la clase, deja solo el diagrama en el slide.
  Resolution: La diapositiva quedo con el diagrama solo. Llevaba tres bloques de cuerpo sobre el mismo contenido: el diagrama de cuatro paneles, una tabla de 3x4 que decia lo mismo, y el parrafo de alcance. Contra el presupuesto de densidad de principles.md (un callout, un table-or-diagram, un bloque de apoyo) sobraban dos, y el diagrama terminaba en una franja angosta con las etiquetas ilegibles. El presentador retiro el parrafo de alcance a mano; aca se retira la tabla y se archiva en Cut material. Queda titulo, lead y diagrama a pantalla completa, plantilla image-full. Lo que decia la tabla y no dice el dibujo (la vecindad en imagenes y el orden en senales) mas la declaracion de alcance pasaron a las notas del orador.
  Nota de proceso: este mismo fix se habia aplicado a las 15:25 y se perdio. draft.md volvio a escribirse a las 18:04 desde un buffer viejo del editor, con la tabla de nuevo y el lead sin acortar. Se verificaron las otras 53 diapositivas y ninguna mas quedo afectada.
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
- [closed] 2026-08-21 — "Move " **Qué es un MLP.** Multi-Layer Perceptron, o perceptrón multicapa. Una capa de entrada, una o más capas ocultas donde cada neurona se conecta con todas las de la capa anterior (de ahí el nombre "densa", o *fully connected*), y una capa de salida. Es la arquitectura más simple y sigue siendo el bloque final de muchas CNN." como un quote importante en un solo slide."
  Resolution: Diapositiva nueva 1.3 'Qué es un MLP', una sola frase a pantalla completa con la definición (capa de entrada, capas ocultas todas-con-todas, capa de salida) y el cierre de que sigue siendo el bloque final de muchas CNN. La definición salió del cuerpo de la 1.2, que se queda con el contraste de las tres arquitecturas y la declaración de alcance. Las diapositivas 1.3 a 1.6 pasaron a 1.4 a 1.7.


---

## 3. Qué es un MLP

### Content

> **Multi-Layer Perceptron**, o perceptrón multicapa: una capa de entrada, una o más capas ocultas donde cada neurona se conecta con todas las de la capa anterior (de ahí el nombre "densa", o *fully connected*), y una capa de salida.

<!-- template: quote -->

### Sources

corpus/chat.md.md (§1 Conceptos base: Pesos y bias; §7 Ejemplos completos — dónde se usa una capa fully connected después de un extractor)

### Speaker notes

Una sola frase en pantalla, veinte segundos. Leela y marcá con el dedo la parte que importa: cada neurona se conecta con todas las de la capa anterior. De acá en adelante, cuando la clase diga "la red", dice esto.

El nombre es histórico y viene del perceptrón de Rosenblatt; si alguien pregunta por qué se llama perceptrón habiendo capas densas de por medio, contestá eso y seguí, no abras ese frente.

Si aparece la pregunta de para qué sirve hoy un MLP con las CNN y los transformers dando vueltas, la respuesta corta es que en visión el MLP es el bloque final. La CNN convierte la imagen en un vector de features y ese vector entra a una fully connected que produce la salida. El MLP no quedó obsoleto, quedó adentro.

### Presenter feedback

- [closed] 2026-08-21 — "Remove Es la arquitectura más simple que merece el nombre de red neuronal, y sigue siendo el bloque final de muchas CNN."
  Resolution: Se eliminó esa segunda línea de la diapositiva 3. Queda solo la cita con la definición del MLP, que es lo que pide el template quote. La tercera nota del orador citaba "la segunda línea"; se reescribió para no apuntar a un texto que ya no está en pantalla, sin perder el contenido (en visión el MLP es el bloque final).

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

1. La neurona recibe las entradas `x` y calcula la **pre-activación** `z = W·x + b`: una combinación lineal de las entradas más un sesgo.
2. Ese `z` pasa por la **activación** `a = f(z)`, y `a` es lo que la neurona entrega a la capa siguiente.
3. La no linealidad de `f` es lo que hace que apilar capas sirva. Sin ella, la composición de capas lineales colapsa a una sola matriz.
4. Hay un puñado de candidatas para `f` y casi siempre gana ReLU. Las vemos en la sección 8, junto con el resto de las decisiones de las capas ocultas; la activación de salida es otra historia, la determina la tarea.

### Sources

corpus/chat.md.md (§1 Conceptos base: Activación, Pesos y bias)

### Speaker notes

Refresco rápido, la audiencia tiene base técnica. El punto que no puede faltar: por qué la no linealidad. Preguntales qué pasa si sacás la ReLU de una red de 5 capas. Respuesta: te queda una regresión lineal disfrazada. Si preguntan cuántos parámetros tiene una capa: `m·n + m`, con n entradas y m neuronas. No lo desarrolles, no hace falta en el resto de la clase.

### Presenter feedback

---

## 5. Lo que hay que diseñar

### Content

Diseñar un MLP son seis decisiones, y la que todos creen que es la principal, cuántas capas ponerle, es la que menos pesa. Son las seis que recorre esta clase, en este orden.

- **La entrada.** Cómo cada variable del problema se convierte en floats. Es donde se gana o se pierde el modelo, y donde más tiempo vamos a estar.
- **El dataset.** Cómo se parte antes de entrenar, en train, validación y test. Sin esto ninguna métrica posterior es honesta.
- **La salida.** Cuántas neuronas y qué activación lleva la última capa. No se elige: la determina la tarea. Predecir un precio pide una neurona sin activación; clasificar en N clases, N neuronas con softmax.
- **La función de pérdida.** La fórmula que convierte una predicción equivocada en un número, el único que la red intenta bajar. Viene junto con la salida: la salida lineal de un precio pide MSE, MAE o Huber; el softmax de N clases pide cross-entropy.
- **El error.** Cómo se mide que el modelo sirve, una vez entrenado. Resumir su desempeño en un solo número es una decisión de diseño, y ningún número sirve para todos los casos.
- **# Capas & # Neuronas.** Cuántas capas ocultas y cuántas neuronas por capa. Es lo único de la lista que se elige libremente, y lo que menos impacto tiene.

**Nota:** 1 a 3 capas ocultas alcanzan para datos tabulares, ancho en potencias de 2 decreciente, ReLU salvo motivo. El retorno está en las otras cinco.

<!-- format: editorial -->

### Sources

corpus/chat.md.md (§9 Diseño de la red: qué se decide y qué no)

### Speaker notes

Este es el mapa mental que quiero que se lleven, y además es la agenda de la clase disfrazada de contenido: casi cada viñeta es una sección. El overfitting salió de la lista a propósito, porque no es algo que se diseñe sino un problema que aparece y que la clase trata al final; si alguien pregunta por qué no está, esa es la respuesta. Lo mismo con backpropagation: es el algoritmo que hace funcionar todo lo demás, no una decisión de diseño. Recorrelas señalando hacia adelante, sin desarrollar ninguna. El remate es la última línea: contrastá con la expectativa, pasan horas tuneando capas y el retorno está en la entrada. Dato honesto para dejar caer acá o al final: en datos tabulares una red muchas veces pierde contra gradient boosting (XGBoost, LightGBM); las redes brillan cuando hay estructura que explotar (imágenes, texto, señales). Sirve para bajar la sobreexpectativa.

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

- [closed] 2026-08-21 — "Creo que "El overfitting" no es en realidad algo a modelar pero un problema en si. Cambiemos "El overfitting" por Loss Function y vamos a crear una nueva seccion que sea sobre esto."
  Resolution: La card 'El overfitting' salió de la lista de decisiones de diseño y en su lugar entró 'La función de pérdida', con la fórmula que convierte una predicción equivocada en un número. Para que no quedaran dos cards diciendo lo mismo, 'La salida' dejó de mencionar la loss (ahora es solo neuronas y activación) y 'El error' pasó a ser explícitamente la medición del modelo ya entrenado. El overfitting sigue teniendo su sección al final y las notas del orador explican por qué salió de la lista: es un problema que aparece, no algo que se diseñe.
---

## 6. Del dato a los nodos de entrada

### Content

```ascii
   EL DATO                              EL MODELO QUE LO TOMA
   ------------------------------------------------------------------

   TABLA   m2 + barrio (12)             1 fila se vuelve 13 nodos
   +------+-----------+                          |
   | m2   | barrio    |                          v            MLP
   | 85   | Palermo   |      ------>          (o)-\
   | 120  | Caballito |                       (o)--+--(O)--\
   +------+-----------+                       (o)--+--(O)---+--(S)
     una fila por caso                         ...-/
                                              (o)-/
                                          entrada  ocultas  salida
                                          los toma todos a la vez


   SENAL 1D  ECG, T = 300               entra el vector entero, sin aplanar

   +--+--+--+--+--+--+--+--+                 slice
   |  |  |  |  |  |  |  |  |   ------>    +======+- - -+- - -+
   +--+--+--+--+--+--+--+--+              |      |     |     |     RNN / CNN 1D
    1 x 300: una matriz de una             +======+- - -+- - -+
    sola fila, o sea un vector              ---------------->
    el orden es el dato                     toma slices de pasos
                                            consecutivos y se desliza


   IMAGEN EN GRISES  28 x 28            entra la grilla entera, sin aplanar

   +----+----+----+                          ventana
   |    |    |    |          ------>      +====+- - -+- - -+
   +----+----+----+                       |    |     |     |          CNN
   |    |    |    |                       +====+- - -+- - -+
   +----+----+----+                       | - -|     |     |
     una matriz: la vecindad                ------------->
     es el dato                             se procesa por partes: una
                                            ventana chica recorre la grilla


   IMAGEN RGB  28 x 28 x 3              entran las tres juntas, sin aplanar

    R      G      B                          R      G      B
   +---+  +---+  +---+       ------>      +=+-+  +=+-+  +=+-+
   |   |  |   |  |   |                    | | |--| | |--| | |          CNN
   +---+  +---+  +---+                    +---+  +---+  +---+
     tres matrices, una                     -------------->
     por canal                              la misma ventana toma los tres
                                            canales en el mismo punto

   ------------------------------------------------------------------
   aplanar los tres ultimos para un MLP daria 300, 784 y 2.352 entradas
   sueltas, y borra el orden y la vecindad
```
<!-- ascii-note:
intent: mostrar el traspaso del dato al modelo que lo toma, una fila por caso, y que solo el MLP procesa todas las entradas de una vez mientras los otros tres recorren la estructura por partes
emphasize: el contraste entre el MLP, que toma los 13 nodos juntos, y las tres filas siguientes, donde una ventana marcada en rojo recorre el dato; la senal dibujada como una matriz de una sola fila (un vector) y no como cajas sueltas; y las tres matrices RGB con la misma ventana en el mismo punto de los tres canales
labels: cada fila lleva el nombre del dato a la izquierda, la leyenda del traspaso sobre la flecha, y el pill de arquitectura abajo a la derecha dentro del bloque del modelo (MLP, RNN / CNN 1D, CNN, CNN); la ventana o slice va en rojo con su posicion actual en linea llena y las siguientes punteadas, mas una flecha de recorrido debajo; el pie cierra con el costo de aplanar
-->

### Sources

corpus/chat.md.md (§ Ejemplos completos: 12 barrios más m² dan 13 neuronas de entrada, 1 m² normalizado más 12 one-hot, arquitectura `13→32→16→1`; § El input: el largo del vector queda fijo, y una forma que borra la estructura no se recupera con ninguna arquitectura; § Escalas y normalización)
784 = 28 × 28 y 2.352 = 784 × 3 — ejemplo aportado por el presentador (MNIST), no figura en el corpus

### Speaker notes

Esta diapositiva es la continuación directa de la anterior, y lo que agrega es el conteo. Abrí con la corrección que trae: **aplanar no es algo que le pase al dato, es algo que pide el MLP**. Si el mismo dato va a una CNN, no se aplana nada.

Recorré los cuatro paneles con la misma pregunta: ¿qué recibe la red? Solo en el primero la respuesta es "nodos sueltos", y son trece. En los otros tres la respuesta es una secuencia, una matriz y tres matrices: la estructura sigue ahí.

El detalle del panel de la tabla: **dos variables dan trece nodos**, no dos. El one-hot del barrio ocupa doce posiciones él solo. Es la primera vez en la clase que aparece que una variable puede ocupar más de un nodo, y es lo que la sección que sigue desarrolla.

Sobre RGB, que es el que más se malinterpreta: son tres matrices, una por canal, dibujadas una al lado de la otra. No son tres imágenes apiladas ni hay un tercer eje espacial. Dicho de otro modo, cada píxel guarda tres números.

El pie es el remate y conviene leerlo entero: si igual quisieras meter los tres últimos en un MLP, se pueden aplanar, y salen 300, 784 y 2.352 entradas sueltas. Ahí es donde se borra el orden y la vecindad. La pregunta que funciona: ¿cuántas entradas tendría una foto de 224 por 224 en color? 150.528. Sirve para que se vea por qué visión no usa MLP.

Dos cosas que la diapositiva ya no dice y conviene decir vos. **El largo no cambia:** la red espera siempre la misma cantidad de entradas, y por eso las imágenes se redimensionan y el texto se trunca o se rellena hasta un largo fijo. **La escala:** con una variable que va de 0 a 1.000.000 y otra de 0 a 1, la primera domina el entrenamiento por su magnitud y no por su importancia. Esa segunda es el puente a la sección que sigue, así que dejala para el final.

Y el remate, que el pie del diagrama ya insinúa: una tabla ya viene en la forma que un MLP espera, y por eso es el caso de esta clase.

No te metas con cómo una CNN conserva la grilla. Alcanza con que quede dicho que no aplana, y seguir.

### Presenter feedback
- [closed] 2026-08-21 - Saca del slide 8 todos los textos, solo deja el SVG.
  Resolution: El cuerpo quedo con el diagrama solo, igual que la 1.2. Se retiraron el lead, los dos bullets (El largo no cambia, La escala) y el remate de que una tabla ya viene en la forma que un MLP espera. Los tres pasaron a las notas del orador y quedaron archivados en Cut material. Se conservan el pill de seccion y el titulo, que son la cabecera de la diapositiva; si el presentador los quiere fuera tambien, hay que decirlo. Plantilla de content-image a image-full, que es la que dibuja la imagen de borde a borde y no emite banda de destacados.
- [closed] 2026-08-21 - En CNN el concepto de sliding estaria bueno modelarlo. / En las matrices una caja que muestre que se procesa de partes. / Creo que en el caso de senal es realmente una matriz de una linea, un vector. / Pero cuando pasa al CNN se toma de slices.
  Resolution: Tres cambios en el diagrama. **(1) La senal paso de cajas sueltas x1 x2 x3 a una matriz de una sola fila**, dibujada como una tira con divisiones, con el rotulo 1 x 300, una matriz de una sola fila, o sea un vector. Era mas preciso y ademas empareja las cuatro filas, que ahora son todas matrices salvo la de la tabla. **(2) Se modelo el recorrido por partes en las tres filas no-MLP**: una ventana en rojo con la posicion actual en linea llena y las siguientes punteadas, mas una flecha de recorrido debajo. En la senal la ventana es un slice de pasos consecutivos; en la imagen en grises es una ventana chica sobre la grilla; en RGB es la misma ventana en el mismo punto de los tres canales, unidas por una linea punteada. **(3) El contraste quedo explicito del lado del MLP**, que ahora dice que toma todas las entradas a la vez, que es lo que lo diferencia de los otros tres. Se mantuvo el limite del [closed] previo: se muestra que la ventana recorre, no como se calcula una convolucion.
- [closed] 2026-08-21 - Deberia verse como la matriz y como pasa al modelo que toma el input. / El del MLP quedo bien, el resto no. / Seria importante marcar tambien que tipo de arquitectura es cada una para evitar confusiones.
  Resolution: El diagrama paso de cuatro paneles en dos filas a **cuatro filas de traspaso**, con dos columnas rotuladas: EL DATO y EL MODELO QUE LO TOMA. Cada fila cruza la flecha con la leyenda de que pasa en ese cruce, y del lado derecho se dibuja **el modelo con la forma de su entrada**: el MLP con sus tres capas y los rotulos entrada, ocultas y salida; la RNN con tres pasos encadenados; la CNN con la grilla entera; y la CNN de RGB con las tres matrices juntas. Cada bloque lleva su pill de arquitectura adentro, y el del MLP es el unico acentuado. Antes solo la fila de la tabla mostraba el traspaso y las otras tres se quedaban en el dato, que es lo que el presentador marco.
- [closed] 2026-08-21 - Creo que imagen RGB no esta bien porque cada uno se mapea a una arquitectura distinta, y asi en un caso en realidad se preserva y no se aplana. / eg: en caso de imagen RGB se mapean dejando las matrices, y de ahi que MLP no sirve.
  Resolution: Correcto, y era un error de fondo, no de la RGB sola. El diagrama aplanaba los cuatro casos por igual, cuando **aplanar es un requisito del MLP y no del dato**: la diapositiva anterior dice que cada dato tiene su arquitectura natural y esta la contradecia. Se rehizo el diagrama con el eje correcto, que es que recibe la red: la tabla llega como 13 nodos sueltos y el MLP los toma tal cual; la senal llega como una secuencia de 300 pasos en orden; la imagen en grises como una matriz intacta; y la RGB como tres matrices de 28x28, una por canal, dibujadas una al lado de la otra. El conteo de nodos que el presentador habia pedido no se perdio: bajo al pie, como el precio de aplanar los tres ultimos para meterlos en un MLP (300, 784 y 2.352 entradas sueltas) y lo que eso borra. Se respetaron los dos [closed] previos sobre RGB: nada de matrices apiladas ni de tercer eje espacial, y no se explica como funciona una convolucion.
- [closed] 2026-08-20 — "Complementario a slide 4, pongamos slide 5 que cubra: el input de una red neuronal es en esencia un vector numerico; cada posicion representa una dimension (una feature); segun el tipo de dato cambia como se codifica; y los puntos que confunden: dimensionalidad fija, normalizacion/escala, y embeddings vs. one-hot."
  Resolution: Diapositiva nueva 1.5 'El vector de entrada, una posición por feature', después de 'Una neurona, en una línea'. Define feature por posición, el largo fijo del vector, MNIST 28x28 como 784 posiciones, la tabla tipo de dato a codificación (numérico, categórico, imagen, texto, audio) y los tres puntos que confunden: largo fijo, escala y one-hot contra embedding. Los dos últimos quedan apuntando a la sección 2, que es donde se desarrollan.


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

```ascii
   una fila por casa, una columna por variable

   +--------+----------+------+---------+
   |  m2    | barrio   | amb  | precio  |
   +--------+----------+------+---------+
   |  85    | Palermo  |  3   | 210.000 |
   |  120   | Caballito|  4   | 185.000 |
   |  62    | Almagro  |  2   | 121.000 |
   +--------+----------+------+---------+

              intercambio dos columnas
                       |
                       v

   +----------+--------+------+---------+
   | barrio   |  m2    | amb  | precio  |
   +----------+--------+------+---------+
   | Palermo  |  85    |  3   | 210.000 |
   | Caballito|  120   |  4   | 185.000 |
   | Almagro  |  62    |  2   | 121.000 |
   +----------+--------+------+---------+

              es EL MISMO dato

   la posicion de la columna no significa nada,
   mientras cada una conserve su nombre

   en una imagen, en cambio, mover un pixel
   si cambia el dato
```
<!-- ascii-note:
intent: mostrar con el caso de house pricing que en datos tabulares el orden de las columnas no lleva informacion
emphasize: las dos columnas que se intercambian entre la primera tabla y la segunda, y que las dos tablas dicen exactamente lo mismo; el contraste final con la imagen va en tono secundario
labels: la tabla de casas con m2, barrio, ambientes y precio; la leyenda de intercambio entre las dos tablas; el remate de que es el mismo dato; formato vertical, pensado para ir en una columna al costado de la diapositiva
-->

### Sources

corpus/chat.md.md (§2 El input: principio general — el caso sin estructura y su invariancia al orden de columnas)

### Speaker notes

Definí "tabular" por contraste con una imagen, que es el ejemplo que todos tienen a mano: en una tabla no hay píxeles vecinos ni orden temporal que explotar, y el modelo puede recibir las columnas en cualquier orden mientras sepa cuál es cuál. Ese es el punto que conecta con la diapositiva de arquitecturas de la sección anterior: el MLP no usa la posición, y en tabular no hay posición que usar, así que la arquitectura y el dato se corresponden.

El resto de la sección es método, y conviene anunciarlo así: cada columna del dataset se convierte en una o más posiciones del vector, y lo que decide en cuántas y con qué valores es el tipo de variable.

Si alguien pregunta por imágenes, texto o series temporales, la respuesta corta es que cada familia tiene su arquitectura y que las vimos al pasar en la sección 1. No abras ese frente acá.
### Presenter feedback
- [closed] 2026-08-21 - Creo que la frase sobre el paso de la columna al numero se puede borrar, ya se explico antes. / Poner una imagen al costado del slide 10 que muestre la representacion visual con el caso que seguimos de house pricing.
  Resolution: Se retiro el parrafo de cierre (archivado en Cut material): el paso de columna a posiciones del vector ya lo dice la diapositiva anterior, que lo cuenta con numeros, y la seccion entera es ese desarrollo. En su lugar la diapositiva lleva ahora un diagrama al costado con el caso de house pricing: la misma tabla de casas dos veces, con dos columnas intercambiadas, y el remate de que es el mismo dato. Es la ilustracion directa de lo que la diapositiva afirma, que el orden de las columnas no lleva informacion, y cierra con el contraste de que en una imagen mover un pixel si cambia el dato.
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

## 6. La tabla de decisiones

### Content

La sección entera cabe en una tabla. Cada fila es un tipo de variable que te vas a encontrar, y la columna del medio es la única decisión que hay que tomar. En la última columna, **`k` es la cantidad de valores distintos** que toma la variable y **`d` es la dimensión del embedding**, que se elige.

La última columna cuenta **floats, no neuronas**. La capa de entrada no es una capa: no tiene pesos ni calcula nada, es el vector en sí. Una neurona hace `z = W·x + b` y después una activación, y la primera que hace eso es la primera capa oculta. Lo que la tabla cuenta son posiciones del vector de entrada.

| Variable | Ejemplo | Codificación | # de inputs (floats) |
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

<!-- format: editorial -->

### Sources

corpus/chat.md.md (§3 Codificación de variables; §4 One-hot vs. embedding)

### Speaker notes

Es la diapositiva de referencia de la sección, la que van a fotografiar. No la leas fila por fila: pediles que elijan tres variables de un dataset que conozcan y las ubiquen. Las filas que más discusión generan son las tres del medio (ordinal, código con forma de número, identificador único) y son justamente las tres que más aparecen mal resueltas en los trabajos. Dos aclaraciones para tener a mano: la fila de fecha dice "2 por ciclo" porque una fecha suele tener más de uno, el mes del año y el día de la semana, y ahí son 2 + 2 + 1; y si alguien pregunta por qué faltantes no está en la tabla, la respuesta es que faltar no es un tipo de variable sino algo que le puede pasar a cualquiera. Se imputa (media o mediana en las numéricas, categoría propia en las categóricas) y se suma un float más, el flag binario que dice si el dato estaba. Ese flag muchas veces predice más que la variable misma. El cierre importa: el largo del vector de entrada es una consecuencia de la tabla, no una decisión de arquitectura. Si alguien pregunta por qué la columna dice floats y no neuronas, la respuesta corta es que la entrada no calcula nada: una neurona hace `z = W·x + b` más activación, y la primera que hace eso es la primera capa oculta. Es una imprecisión frecuente en los libros y vale la pena marcarla, porque es la misma idea con la que abre la clase: la red ve un vector de floats.

### Presenter feedback
- [closed] 2026-08-19 — "Borrar 'Sumar la última columna, más un flag por cada variable que pueda faltar, da el largo del vector de entrada. Esa cuenta no se elige: sale de la tabla.'"
  Resolution: Se retiró el cierre. La tabla y el párrafo de faltantes se sostienen solos.
- [closed] 2026-08-19 — "Leí que el input realmente no son neuronas"
  Resolution: Correcto, y la tabla decía "Neuronas". La capa de entrada no tiene pesos ni calcula nada: es el vector en sí, y la primera que hace `z = W·x + b` más activación es la primera capa oculta. La columna pasó a llamarse "Floats", que además es el término con el que abre la sección ("Todo termina en un vector de floats"), y se agregó un párrafo que explica la distinción. También se corrigieron el goal de la sección y el cierre de la diapositiva, que decían "cantidad de neuronas de entrada", y las notas del orador para responder si alguien pregunta. El encabezado "Neuronas" del catálogo de salida no se tocó: ahí sí son neuronas de verdad.
- [closed] 2026-08-19 — "En la tabla de neuronas para el input hay una tabla. ¿Es eso correcto?"
  Resolution: Los números estaban bien, pero la tabla tenía tres problemas. (1) `k` y `d` aparecían en cinco filas sin definirse; ahora se definen en la bajada, antes de la tabla. (2) "Con faltantes" no era un tipo de variable sino un modificador que se cruza con todas las filas, y su "1 + 1" solo valía si la variable de abajo era numérica: con un barrio en one-hot son k + 1. Salió de la tabla y pasó a un párrafo que dice que faltar le pasa a cualquiera y suma una neurona de flag. (3) "Fecha 2 + 1" asumía un solo ciclo; pasó a "2 por ciclo + 1", porque una fecha suele tener mes del año y día de la semana. El cierre ahora suma también los flags.
- [closed] 2026-08-21 — "Cambia en la columa Floats por # de inputs (floats)"
  Resolution: El encabezado de la última columna quedó '# de inputs (floats)'. La bajada decía 'La columna dice floats, no neuronas' y con el nombre nuevo habría quedado mintiendo: pasó a 'La última columna cuenta floats, no neuronas'. El párrafo de faltantes que borraste en el borrador quedó archivado en Cut material y su contenido (imputar y sumar un flag binario) se conservó en las notas del orador, que ya respondían esa pregunta.
---

# 3. Partir el dataset

**Goal of this section:** Qué se hace con el dataset antes de entrenar. Los tres conjuntos, para qué sirve cada uno, en qué proporción, y qué errores de partición arruinan la medición sin lanzar ningún error. Es la sección que hace honesta cualquier métrica de las secciones 5 y 6.

**Presenter feedback:**
- [closed] 2026-08-21 - "Mover 'La diferencia sutil esta entre validacion y test...' y 'Augmentation solo en train...' a un slide Does and don'ts y expandir con tips claves."
  Resolution: Diapositiva nueva 3.5 'Que hacer y que no', cierre de la seccion, en dos columnas enfrentadas. Los dos puntos citados se movieron ahi: la diferencia validacion/test paso a la columna de que no hacer, como no tunear contra el test, y augmentation quedo en la de que hacer. Se expandio con cinco tips que no estaban en ninguna otra diapositiva: partir antes de explorar, partir por grupo y no por fila, fijar la semilla y guardar el split, no volver a partir cuando el numero no cierra, y no confiar en el corte por defecto de train_test_split. Se cuido no repetir la 3.3 (todo se aprende del train) ni la 3.4 (los errores que arruinan la medicion): esa explica los modos de falla, esta da las reglas operativas. La 3.2 quedo con la tabla mas un solo remate.

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

- **Por eso no alcanza con partir en dos.** Sin validación terminás tuneando contra el test, y cuando desplegás sus métricas ya no son insesgadas. El split de dos vías sirve solo si no tomás ninguna decisión iterativa, que no describe a ningún proyecto real.

### Sources

corpus/train-test-split-roboflow.web.md (§6 La distinción sutil; §7 Preprocesamiento contra augmentation; §11 Por qué no alcanza con train y test; tabla comparativa); corpus/train-validation-test-sets.web.md (§2 Qué distingue a validación de test)

### Speaker notes

Esta tabla es el resumen que se llevan de la sección. La fila que cuesta es "actualiza los pesos": muchos creen que el modelo aprende algo de validación porque la métrica aparece en pantalla cada epoch. No aprende nada; el que aprende sos vos, y por eso hace falta el test. La analogía que funciona: validación son los simulacros que hacés para estudiar, test es el examen final; si te dan el examen final de simulacro, deja de medir. Menciona que en Kaggle el test set se libera recién al cierre de la competencia, exactamente por esto.


### Presenter feedback
---

## 3. Todo se aprende solo del train

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

## 4. Los errores que arruinan la medición

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

## 5. Qué hacer y qué no

### Content

La sección en reglas operativas. A la izquierda lo que hay que hacer siempre; a la derecha lo que más se ve mal resuelto.

**Qué hacer**

- Partir antes de explorar
- Partir por grupo, no por fila
- Fijar la semilla y guardar el split
- Augmentation solo en train

**Qué no hacer**

- Tunear contra el test
- Volver a partir porque el número no cerró
- Confiar en el corte por defecto

### Sources

corpus/train-test-split-roboflow.web.md (§6 La distinción sutil; §7 Preprocesamiento contra augmentation); corpus/train-validation-test-sets.web.md (§2 Qué distingue a validación de test)
Partir antes de explorar, partir por grupo, fijar la semilla y no volver a partir son aporte propio para la clase; no figuran en el corpus

### Speaker notes

Esta es la diapositiva que se fotografía y la que cierra la sección. Las dos columnas se leen enfrentadas, no en orden, y cada línea se desarrolla en voz alta: la diapositiva es el índice, vos sos el contenido.

**Partir antes de explorar.** Es la que más se resiste, y la objeción típica es "pero si todavía no entrené nada". La respuesta: las decisiones que tomás mirando los datos, qué variables sacar, cómo tratar los outliers, qué imputar, también son aprendizaje. Si las tomaste mirando todo, el test ya no está limpio.

**Partir por grupo.** Es la que más aparece en los trabajos que entregan. El caso que lo hace evidente: diez radiografías del mismo paciente repartidas entre train y test. El modelo no generaliza a pacientes nuevos, reconoce a ese paciente. Vale igual para varias filas del mismo cliente o de la misma sesión.

**Fijar la semilla y guardar el split.** Un experimento que no se puede repetir no se puede comparar con el siguiente. Guardar los índices, no solo la semilla.

**Augmentation solo en train.** Validación y test se quedan con los datos originales, porque su trabajo es representar lo que viene en producción. El preprocesamiento, en cambio, se aplica a los tres: esa es la distinción que se confunde.

**Tunear contra el test.** Dala despacio porque es contraintuitiva. El modelo no entrena con validación ni con test; la diferencia sos vos, que elegís mirando validación y a lo largo de muchos experimentos vas sobreajustando tus decisiones a ese conjunto. El test atrapa eso solo si nada se eligió mirándolo, y por eso existe el tercer conjunto.

**Volver a partir porque el número no cerró.** Repartir hasta que el resultado guste es elegir la partición más favorable. Es sobreajustar al test sin darse cuenta y sin que nada falle.

**Confiar en el corte por defecto.** La más práctica: mostrá la firma de `train_test_split` y señalá que `stratify` es opcional y viene en `None`, que no hay parámetro de grupo, y que no mira el tiempo. La mayoría de los splits rotos que van a ver son exactamente ese default.

### Presenter feedback

---

# 4. Modelar la salida

**Goal of this section:** Mostrar que la última capa no se elige, la determina la tarea, y que activación de salida y loss van siempre juntas. La loss aparece acá nombrada en el catálogo y se desarrolla en la sección 5. Que salgan sabiendo mapear "qué predice el modelo" a "cuántas neuronas, qué activación, qué loss", y sabiendo por qué la forma de cada activación de salida corresponde a lo que se predice.

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

- [closed] 2026-08-21 — "Dado que creamos un seccion sobre lost functions, tomemos cada una de las descriptas aca. Empecemos con un slide que sea lost function, cuando se utilizar, Por qué esa arquitectura (eg: 1 neurona sin activación (lineal) porque el valor puede ser cualquier número. MSE penaliza fuerte los errores grandes, MAE es más robusto a outliers, Huber es un punto medio (cuadrático cerca de cero, lineal lejos).). Y luego un slide por cada una que cubra la formula y consideraciones. Si podemos poder un ARCII chart que modele el comportamiento, agreguemosla por casa una."
  Resolution: Sección 5 nueva, 'La función de pérdida', entre Modelar la salida y Medir un clasificador, con seis diapositivas por familia como acordamos: la cita de apertura, qué es una loss (loss contra cost contra objective, y por qué tiene que ser diferenciable), regresión con MSE, MAE y Huber en una sola con el ASCII comparando las tres penalizaciones, BCE con el ASCII de -log(y), cross-entropy con el reparto de softmax, y las especializadas (Poisson, pinball, NLL gaussiana) en tabla. Las tres de regresión van juntas porque el punto es el contraste entre ellas y se ve en un solo dibujo. Cada una lleva fórmula, cuándo se usa y la consideración de implementación (doble sigmoide, softmax donde va sigmoide). El bloque archivado sobre los pares que no se rompen volvió al mazo repartido entre la 5.4 y la 5.5.

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

# 5. La función de pérdida

**Goal of this section:** Dar el segundo componente del par que la tarea determina. La sección anterior dejó cuántas neuronas y qué activación; esta deja qué número minimiza la red y por qué ese y no otro. Que salgan sabiendo elegir la loss para las tres familias que van a usar (regresión, binaria, multiclase), sabiendo leer su fórmula y la consecuencia de la forma de cada una, y con las especializadas ubicadas como referencia.

**Presenter feedback:**
- [closed] 2026-08-21 — "Pone este quote como primer slide de la seccion de lost functions "La IA es el diseño de agentes racionales: sistemas que perciben su entorno y toman acciones para maximizar sus posibilidades de éxito en un objetivo dado. Resolver problemas complejos con matemáticas a gran escala, en lugar de crear humanos sintéticos.""
  Resolution: La cita quedó como diapositiva 5.1, a pantalla completa y sin nada más. El puente a la sección lo hace la propia cita: 'maximizar sus posibilidades de éxito en un objetivo dado' es literalmente lo que la función de pérdida escribe en una fórmula, y las notas del orador lo marcan. Queda sin atribución en la diapositiva; el texto es una paráfrasis cercana a la definición de agentes racionales de Russell y Norvig, y quedó anotado en Open questions para que decidas si va citada.

---

## 1. Qué es, en el fondo, la IA

### Content

> La IA es el diseño de agentes racionales: sistemas que perciben su entorno y toman acciones para maximizar sus posibilidades de éxito en un objetivo dado. Resolver problemas complejos con matemáticas a gran escala, en lugar de crear humanos sintéticos.

<!-- template: quote -->

### Sources

Cita aportada por el presentador. Sin fuente atribuida todavía (ver Open questions)

### Speaker notes

Abrí la sección con esta diapositiva y dejala en pantalla mientras la leés entera. Es una definición de la materia, no de la clase, así que vale bajar un cambio de ritmo acá.

El puente a la sección es la última parte de la primera oración: **un objetivo dado**. Todo lo que sigue es la respuesta a la pregunta de dónde sale ese objetivo y cómo se escribe en una fórmula. La función de pérdida es, literalmente, el objetivo dado.

La segunda oración sirve para bajar la mística: nada de lo que van a ver en esta clase se parece a construir una mente. Es una fórmula, una derivada y un paso de actualización, repetidos muchas veces.

### Presenter feedback

---

## 2. Qué es una función de pérdida

### Content

Una **función de pérdida** es la fórmula que convierte una predicción equivocada en un número. Es el único número que la red intenta bajar, y de él sale el gradiente que corrige cada peso.

- **Loss.** El error de un solo ejemplo. Es lo que mide la fórmula que elegimos acá.
- **Cost.** El promedio del loss sobre un batch o sobre el dataset. Es el número que el entrenamiento reporta.
- **Objective.** El cost más los términos de regularización. Es lo que el optimizador minimiza de verdad, y aparece en la sección 9.

La loss no se elige libre: viene con la salida. Para predecir un precio la tarea pide una neurona sin activación, porque el valor puede ser cualquier número real, y sobre esa salida van MSE, MAE o Huber. Cambiar la activación de salida obliga a cambiar la loss, y al revés.

**Diferenciable o no sirve.** El gradiente se calcula derivando la loss, así que la fórmula tiene que tener derivada en todo su dominio. Accuracy no la tiene: es un conteo, salta de a escalones. Por eso accuracy se reporta y nunca se optimiza, y las métricas de clasificación tienen su propia sección.

**Notación de acá en adelante:** `y` es lo que la red predijo y `t` el valor verdadero que viene con el dato.

### Sources

corpus/chat.md.md (§1 Conceptos base: Loss, cost, error, objective; §8 La capa de salida — activación de salida y loss se eligen juntas siempre)
El ejemplo de la salida lineal para un precio lo aportó el presentador; la fila correspondiente del catálogo (1 neurona / lineal / MSE-MAE-Huber) sí está en el corpus (§8)

### Speaker notes

Es la diapositiva de vocabulario de la sección y conviene darla despacio, porque los tres términos se usan como sinónimos en todos lados y después no se entiende de qué se habla. La distinción viene de los cursos de Andrew Ng; Bishop y Goodfellow usan "error function" y "cost function" indistintamente, y en papers modernos se dice "loss" para todo. Si alguien te corrige, esa es la respuesta honesta: la distinción es útil para enseñar, no es un estándar.

Cuidado con la palabra "error" a secas, que es la que más confusión genera: en estadística es el residuo `y − t`, y "error rate" es la proporción de clasificaciones incorrectas. Ninguna de las dos es la loss.

El punto de la diferenciabilidad es el que ordena la clase entera y vale la pena insistir: la razón por la que no entrenamos directamente sobre accuracy, que es lo que en el fondo nos importa, es que accuracy no tiene derivada. Se entrena sobre un sustituto derivable y se mide con lo que importa. Esa brecha entre lo que se optimiza y lo que se reporta reaparece en la sección 7.

### Presenter feedback

---

## 3. Regresión: MSE, MAE y Huber

### Content

Salida de una neurona con activación lineal. Las tres losses miden lo mismo, la distancia entre `y` y `t`, y se diferencian en cuánto castigan un error grande.

```ascii
      cuanto castiga cada loss un error de tamano  e = y - t

     MSE   e^2               MAE   |e|             Huber  (d = 1)
       |\           /          |\          /          |\          /
       | \         /           | \        /           | \        /
       |  \       /            |  \      /            |  \      /
       |   \     /             |   \    /             |   \    /
       |    \   /              |    \  /              |    \__/
   ----+-----\_/-----      ----+-----\/-----      ----+------+-----
       0      e                0      e                0     e

   parabola: el error      una V: cada unidad     parabola cerca del
   grande manda            de error pesa igual    cero, rectas lejos
```
<!-- ascii-note:
intent: contrastar la forma de las tres curvas de penalizacion sobre el mismo eje de error
emphasize: que MSE es una parabola que acelera, MAE una V de pendiente constante, y Huber una parabola cerca del cero cuyas colas se vuelven rectas
labels: eje horizontal e = y - t, eje vertical penalizacion; MSE e^2, MAE |e|, Huber con d = 1
-->

- **MSE (error cuadrático medio).** `L = (y − t)²`. Castiga el error al cuadrado, así que un ejemplo muy lejos aporta más gradiente que cien ejemplos cerca. Es el default de regresión y la opción correcta cuando los valores raros son datos legítimos que el modelo tiene que aprender.
- **MAE (error absoluto medio).** `L = |y − t|`. Castiga proporcional al error, así que un outlier pesa como un ejemplo más. Es la opción cuando los valores raros son ruido o errores de carga.
- **Huber.** Cuadrática mientras `|y − t| ≤ d` y lineal a partir de ahí. Se queda con el gradiente suave de MSE cerca del cero y con la resistencia de MAE lejos. `d` es un hiperparámetro y marca dónde está la frontera.

### Sources

corpus/chat.md.md (§8 Catálogo completo de outputs — real (precio): 1 neurona / lineal / MSE-MAE-Huber)
El contraste entre las tres (MSE castiga fuerte los errores grandes, MAE resiste outliers, Huber es el punto medio) lo aportó el presentador; las fórmulas son estándar y no figuran en el corpus

### Speaker notes

El número que cierra la discusión, y conviene escribirlo en el pizarrón: con un error de 1, 2 y 10, MSE castiga 1, 4 y 100; MAE castiga 1, 2 y 10; Huber con `d = 1` castiga 0,5, 1,5 y 9,5. Ese salto de 100 contra 10 es exactamente por qué una propiedad mal cargada arrastra el entrenamiento entero con MSE.

Huber con `d = 1` vale `½e²` mientras `|e| ≤ 1` y `|e| − ½` después. Si alguien pregunta por el medio que aparece en la parte cuadrática y no en MSE, la respuesta es que está para que las dos ramas peguen sin salto en `|e| = d`, y vuelve en la sección que sigue con otro motivo.

La pregunta que funciona para elegir: ¿esa propiedad de 20 millones es un dato real o alguien puso un cero de más? Si es real, MSE. Si es carga sucia, MAE o Huber. La elección de loss es una afirmación sobre los datos, no una preferencia.

Aviso práctico para el trabajo: si el target no está normalizado, MSE sobre precios en pesos da números gigantes y el entrenamiento arranca inestable. Normalizar el target y desescalar al predecir es la costumbre.

### Presenter feedback

---

## 4. Clasificación binaria: BCE

### Content

Salida de una neurona con sigmoide, o sea una probabilidad entre 0 y 1. La **binary cross-entropy** castiga según cuánta probabilidad le dio la red a la respuesta correcta.

`L = −[ t · log(y) + (1 − t) · log(1 − y) ]`

Con `t = 1` sobrevive el primer término y la penalización es `−log(y)`; con `t = 0` sobrevive el segundo y es `−log(1 − y)`. Siempre queda un solo término vivo.

```ascii
        penalizacion  -log(y)   cuando la etiqueta verdadera es  t = 1

    L  |
       |\
       | \
       |  \
       |   \____
       |        \________
   ----+------------------+----  y  (probabilidad que dio la red)
       0                  1

   y cerca de 1   ->  penalizacion cerca de 0    acertar seguro no cuesta
   y cerca de 0   ->  penalizacion al infinito   errar seguro cuesta todo
```
<!-- ascii-note:
intent: mostrar que la penalizacion de BCE explota cuando la red le da poca probabilidad a la clase correcta
emphasize: la asintota vertical en y = 0 y que la curva toca cero en y = 1
labels: eje horizontal y de 0 a 1 (probabilidad predicha), eje vertical penalizacion -log(y)
-->

- **La confianza equivocada es lo caro.** Decir 0,5 y errar cuesta poco; decir 0,01 y errar cuesta muchísimo. Es lo que empuja a la red a calibrar y no solo a acertar el lado.
- **La sigmoide ya viene adentro.** `BCEWithLogitsLoss` en PyTorch aplica la sigmoide internamente por estabilidad numérica. Poner además la activación en la última capa la aplica dos veces y el modelo entrena mal.
- **Con logits crudos hay que convertir al predecir.** `prob = torch.sigmoid(model(x))`. Un logit de 2,3 no es una probabilidad.

### Sources

corpus/chat.md.md (§8 La capa de salida — sí o no (churn): 1 neurona / sigmoide / BCE; el detalle de implementación de BCEWithLogitsLoss y el error de la doble sigmoide)
La fórmula de BCE es estándar y no figura en el corpus

### Speaker notes

Recuperá acá el bloque que quedó archivado sobre los pares que no se rompen: es el mismo contenido y este es su lugar natural ahora que la loss tiene sección propia.

La forma de leer la fórmula sin que asuste: son dos casos disfrazados de uno. `t` vale 0 o 1, así que uno de los dos términos se multiplica por cero y desaparece. Mostralo con los dos casos en el pizarrón antes de mostrar la fórmula completa y deja de dar miedo.

El error de la doble sigmoide es de los que más aparecen en los trabajos y es difícil de diagnosticar, porque el modelo entrena, no tira excepción, simplemente aprende mal. La señal: probabilidades apelotonadas cerca de 0,5 que nunca se despegan.

Si preguntan por qué logaritmo, la respuesta corta es que convierte productos de probabilidades en sumas (la verosimilitud de todo el dataset es un producto) y que su derivada da la forma limpia `y − t` cuando se combina con la sigmoide. Esa cancelación es la que hace que el par sigmoide más BCE entrene bien y que otros pares no.

### Presenter feedback

---

## 5. Clasificación multiclase: cross-entropy

### Content

Salida de N neuronas con softmax, o sea un vector de probabilidades que suma 1. La **cross-entropy** mira una sola casilla de ese vector, la de la clase verdadera, y castiga `−log` de esa probabilidad.

`L = −log(y_c)`, donde `c` es la clase correcta.

```ascii
    3 clases, la verdadera es  gato

    la red predice                    cross-entropy mira una sola casilla

    gato   [########  ]  0.80   <---  L = -log(0.80) = 0.22
    perro  [##        ]  0.15
    zorro  [#         ]  0.05
                         ----
                         1.00

    si a gato le hubiera dado 0.05:   L = -log(0.05) = 3.00
```
<!-- ascii-note:
intent: mostrar que cross-entropy ignora las clases equivocadas y solo mira la probabilidad de la correcta
emphasize: la flecha a la casilla de gato y el contraste entre 0.22 y 3.00
labels: tres clases gato/perro/zorro con sus probabilidades, la suma 1.00, y las dos penalizaciones
-->

- **Las clases compiten.** Softmax reparte una única unidad de probabilidad, así que subir una clase baja las otras. Es correcto cuando las etiquetas son excluyentes.
- **El softmax ya viene adentro.** `CrossEntropyLoss` en PyTorch espera logits crudos y aplica el softmax internamente, igual que su hermana binaria.
- **Etiquetas no excluyentes rompen el modelado.** Un ticket puede ser urgente y de facturación al mismo tiempo. Ahí van N sigmoides con BCE, no un softmax, porque forzar competencia entre etiquetas compatibles está mal desde el diseño.

### Sources

corpus/chat.md.md (§8 La capa de salida — una de N clases: N neuronas / softmax / cross-entropy; varias de N (tags): sigmoide ×N + BCE; el error de usar softmax donde va sigmoide)
La fórmula es estándar y no figura en el corpus. Los dos valores del diagrama son derivados: −log(0,80) = 0,22 y −log(0,05) = 3,00 (logaritmo natural); las tres probabilidades suman 1,00

### Speaker notes

La idea que se llevan: cross-entropy no mira el vector entero, mira una casilla. Todo el trabajo de repartir lo hizo el softmax antes.

El contraste de 0,22 contra 3,00 es el que conviene dejar escrito. Con 0,80 de probabilidad a la clase correcta la penalización es casi nada; con 0,05 se multiplica por más de trece. Y la red no necesita acertar la clase para mejorar: le alcanza con subir la probabilidad de la correcta, aunque siga sin ser la más alta. Eso responde la pregunta de por qué el entrenamiento avanza aunque accuracy no se mueva durante varias épocas.

El caso del ticket es el mejor ejemplo del error de modelado y conviene preguntarlo antes de responderlo: si un ticket puede ser urgente y de facturación, ¿sirve softmax? No, porque las obliga a competir por la misma unidad de probabilidad. Van N sigmoides independientes con BCE, una por etiqueta.

### Presenter feedback

---

## 6. Las especializadas, para tener ubicadas

### Content

Tres casos donde la loss de siempre da resultados malos de una forma que no se nota. No hace falta memorizarlas, alcanza con reconocer cuándo buscarlas.

| Qué predice | Salida | Loss | Por qué la de siempre falla |
|---|---|---|---|
| Un conteo (demanda, visitas) | 1 neurona, softplus o exp | Poisson NLL | Lineal con MSE predice conteos negativos y asume varianza constante, cuando en un conteo a mayor media hay mayor varianza |
| Un rango (P10, P50, P90) | k neuronas lineales | Pinball | Un valor puntual no responde la pregunta cuando la decisión depende del peor escenario |
| Una distribución (μ, σ) | 2 neuronas, μ lineal y σ softplus | NLL gaussiana | Predecir la media sola tira a la basura cuánta incertidumbre hay |

**Los cuantiles son los más rentables de los tres.** No asumen forma de la distribución, dan directamente el intervalo que el negocio pide y se implementan en pocas líneas con pinball loss. El detalle que muerde: hay que forzar que los cuantiles no se crucen.

<!-- format: editorial -->

### Sources

corpus/chat.md.md (§8 Catálogo completo de outputs y "Predecir una distribución, no un punto"; "Casos que sorprenden" — conteos, ranking, supervivencia)

### Speaker notes

Es una diapositiva de referencia y se pasa rápido, dos minutos. El objetivo no es que las aprendan sino que las reconozcan cuando el problema no entra en las tres familias anteriores.

La fila de conteos es la que más rinde porque el error es invisible: el modelo entrena, converge, y predice menos tres unidades de demanda. Nadie mira las predicciones negativas hasta que alguien las mira.

La de cuantiles es la que más van a usar en la práctica, sobre todo en stock, riesgo y capacidad. La frase que la vende: la media es la respuesta correcta a una pregunta que muchas veces nadie hizo.

Si alguien pregunta por ranking, supervivencia o embeddings, la respuesta corta es que existen, que siguen la misma lógica de que la tarea determina el par salida-loss, y que quedan fuera del alcance de esta clase.

### Presenter feedback

---

# 6. Backpropagation

**Goal of this section:** Abrir la caja del entrenamiento. Hasta acá el modelo estaba diseñado y la loss elegida, pero nadie dijo cómo se corrigen los pesos. La sección abre con la idea que ordena todo, entrenar es buscar el mínimo de una función, recorre el algoritmo (ciclo hacia adelante y hacia atrás, regla de la cadena, delta, propagación y paso de actualización) y cierra con la mecánica que más se confunde en la práctica: el forward va fila por fila, el backward solo acumula valores intermedios, y `W` y `b` se tocan una única vez, al cerrar el batch. **Regla editorial de la sección:** ninguna diapositiva puede dar a entender que el backward corrige pesos; lo que el backward produce son valores intermedios que se acumulan.

**Presenter feedback:**
- [closed] 2026-08-21 — "Agreguemos en back progagation un grafico (un slide con todo el life-cycle) en un slide. Que sea claro que en cada ejecucion se ajunta parametros intermedios que luego cuando termuna el batch se aplica y se mueve el nuevo batch." / "Creo que lo correcto es mostrar que hay batches, y el forard es un individual. se propaga el error ajutando valores intermedios (valores), luego al terminar el batch se ajustan los valores W,B. Y ahi nos movemso al nuevo batch."
  Resolution: Diapositiva nueva 6.9 'El ciclo completo, batch a batch', un solo diagrama con el ciclo de vida entero. Dos bloques y una flecha de retorno: arriba, las B filas del batch haciendo cada una su forward y su backward y sumando su gradiente a un acumulador, con la leyenda de que W y b no se tocan; abajo, el cierre del batch en tres pasos (promediar, aplicar, vaciar) marcado como el único momento en que la red cambia; y la flecha que vuelve al batch k+1 con los pesos nuevos. Al pie, que agotar los batches es una época.
- [closed] 2026-08-21 — "Eg 'Hacia adelante la red calcula su predicción. Hacia atrás propaga el error y ajusta cada peso según cuánto contribuyó a equivocarse. El entrenamiento repite ese ciclo miles de veces.' Aca esta bueno ser claro que se corrige valores intermedios hasta que se termina el batch. Buscar en la documentacion y links que respanden todo este contendino." / "Revisar todos los slides the backpropagation con respecto a este feeback."
  Resolution: La frase citada **estaba mal** y era el peor error de la sección: decía que el backward ajusta los pesos, y no los ajusta. Se barrió la sección entera contra la regla "el backward produce valores intermedios que se acumulan; W y b cambian una sola vez, al cerrar el batch", que quedó anotada en el Goal de la sección. Corregidas: 6.2 (frase de apertura, bullets y diagrama ASCII, que ahora dice explícitamente que W y b quedan quietos), 6.3 (se aclara que la fórmula es la loss de una fila y que lo que se deriva es el promedio del batch), 6.4 (los tres factores de la cadena nombrados como valores intermedios), 6.5 (δ definido como valor intermedio que no sobrevive al batch), 6.6 (lo que viaja hacia atrás son deltas, no pesos corregidos), 6.7 (el paso pasa a estar explícitamente condicionado al cierre del batch, más un bullet nuevo "una vez por batch, no una vez por fila") y 6.8 (el bullet del ajuste ahora nombra el acumulador y el vaciado). Respaldo documental agregado a las fuentes de 6.8, 6.9 y 6.10: el bucle canónico de PyTorch ("Gradients by default add up; to prevent double-counting, we explicitly zero them at each iteration"), `batch_size` de Keras ("Number of samples per gradient update") y CS231n sobre el gradiente del minibatch como aproximación del gradiente completo.
- [closed] 2026-08-21 — "Tambien agregar un slide de entrada donde muetre la idea visual que lo que nos vamos moviendo es buscando el minimo de una function. Hay ya un par de chats en la presentacion de introducion que podemos usar."
  Resolution: Diapositiva nueva 6.1 'Entrenar es buscar el mínimo de una función', de apertura de la sección: la superficie de error en ASCII con el punto de arranque al azar, cuatro pasos que se acortan cerca del fondo y el mínimo marcado, más los cuatro bullets que fijan la idea (la loss depende solo de los pesos, no hay fórmula que salte al mínimo, el gradiente es la brújula y apunta al revés, y backpropagation es cómo se calcula esa brújula). **Nota sobre las fuentes:** se revisó la presentación de introducción y no tiene ese gráfico. Sus imágenes de este tema son fórmulas (coste L2, regla de la cadena, delta, paso de actualización) y están en inglés; la idea del valle aparece solo en prosa, como la analogía de la pelota. El diagrama es propio, y las citas se tomaron del Machine Learning Crash Course de Google y de CS231n.
- [closed] 2026-08-21 — "Que el editor revise en forma critica el contenido de la presentacion" (revisión Composer, scope=full)
  Resolution: Cuatro correcciones en la sección. **(1) L6, la misma frase cuatro veces.** El barrido de la ronda anterior dejó "se acumula durante el batch y se aplica al cerrarlo" como contenido visible en 6.2, 6.7, 6.8 y 6.9. Se repartió por dueño: 6.2 lo enuncia, 6.7 se queda solo con la aritmética del paso y cedió tanto "el único momento en que W y b cambian" (ahora exclusivo de 6.9) como el bullet "una vez por batch, no una vez por fila" (que era el trabajo de 6.8), 6.8 se queda con el conteo, 6.9 con el ensamblado. **(2) L6 en 6.10.** Dos de las cinco filas de la tabla repetían material de otras secciones: el diagnóstico de overfitting que es el cuerpo entero de 8.1, y el argumento de normalización que ya está en la nota de 2.3 y en las notas de 6.7. Las dos pasaron a puntero seco. **(3) Precisión matemática contra API.** El diagrama de 6.9 muestra `g += grad` fila por fila, que es la descomposición matemática correcta pero no lo que se escribe en código: `loss.backward()` se llama una vez por batch y la suma sobre las filas es vectorizada. Con esta audiencia alguien lo iba a marcar, así que quedó en las notas del orador para decirlo primero. **(4) Título de sección.** `Cómo aprende la red: backpropagation` tenía 36 caracteres contra un presupuesto de 25; colapsó a la cláusula derecha, `Backpropagation`.
  **Override registrado — largo de la sección.** La sección quedó en 10 diapositivas contra el ~8 que sugiere `principles.md`. Los dos remedios cuestan más que el defecto: fusionar 6.4 con 6.5 produce una diapositiva con dos imágenes de fórmula y seis bullets, que rompe el presupuesto de densidad; y partir la sección en dos agrega una diapositiva divisoria a un mazo que ya está largo, o sea empeora el problema real. Se deja en 10 a propósito.
- [closed] 2026-08-21 — "Agregar un slide en backprogration al final ambien cosas practicas a tener en cuenta durante el entrenamiento. Gradient lost, parametros a tocar."
  Resolution: Diapositiva nueva 6.10 'Qué mirar cuando esto se entrena', de cierre de la sección. Tabla de síntoma, causa y qué tocar con cinco filas (loss estancada, loss que oscila o va a NaN, loss ruidosa, validación que sube, una variable que domina), más cuatro bullets: gradiente que se desvanece, gradiente que explota, las perillas ordenadas por impacto (η, batch size, activación e inicialización, y último capas y neuronas) y la regla de mover una sola por vez. Las dos últimas filas de la tabla apuntan a las secciones 8 y 2 a propósito, para que no se confundan con problemas de gradiente. Fuentes: Pascanu, Mikolov y Bengio 2013 para desvanecimiento y explosión más el recorte de norma, y los argumentos `clipnorm` y `global_clipnorm` de Keras verbatim.

---

## 1. Buscar el mínimo de una función

### Content

Antes del algoritmo, la idea que lo ordena todo. Fijado el dataset, la loss depende **solo de los pesos**: cambiar un peso cambia el error. Eso dibuja una superficie, y entrenar es caminar por ella hacia abajo.

```ascii
      L(W)   el error, como funcion de los pesos
       ^
       |  o (1)                                             /
       |   \    pesos al azar: el error arranca alto       /
       |    \                                             /
       |     o (2)                                       /
       |      \                                         /
       |       o (3)                                   /
       |        \      cada paso:  W <- W - n * grad  /
       |         o (4)                               /
       |          \__                            __/
       |             o__ o__ o__ o__ o__ o__ ___/
       |                          ^
       |                       el minimo: el error mas bajo alcanzable
       +----------------------------------------------------------> W

   un eje por cada peso de la red: el dibujo muestra uno,
   un MLP real tiene millones
```
<!-- ascii-note:
intent: instalar la imagen mental del descenso por una superficie de error antes de entrar en las formulas
emphasize: el punto de arranque alto y al azar, los pasos cada vez mas cortos cerca del fondo, y el minimo marcado
labels: L(W) el error en el eje vertical, W los pesos en el horizontal, (1) a (4) los pasos sucesivos, n es la tasa de aprendizaje; la nota al pie aclara que el dibujo es de un solo peso
-->

- **La loss es una función de los pesos.** El dataset está fijo, así que lo único que puede cambiar el error es `W` y `b`. La superficie del dibujo es esa dependencia.
- **No hay fórmula que salte al mínimo.** Se arranca en un punto al azar y se llega caminando, paso a paso. Por eso entrenar lleva tiempo.
- **El gradiente es la brújula.** Indica hacia dónde el error *sube* más rápido. El paso va justo en la dirección contraria, y de ahí sale el signo menos que aparece en todas las fórmulas que siguen.
- **Backpropagation es cómo se calcula esa brújula.** No cambia la idea: es el procedimiento que consigue el gradiente de millones de pesos sin rehacer la cuenta para cada uno.

**Todo lo que viene son los detalles de este dibujo.** Qué función se deriva, cómo se calcula la dirección, y en qué momento exacto se da el paso.

### Sources

Google, *Machine Learning Crash Course* — "Gradient descent is a mathematical technique that iteratively finds the weights and bias that produce the model with the lowest loss" <https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent>
Stanford CS231n, *Optimization* — "we are making an update in the negative direction of the gradient df since we wish our loss function to decrease, not increase" <https://cs231n.github.io/optimization-1/>
knowledge-library/backpropagation/index.md (aportado por la Talk intro-redes-neuronales) — el paso de actualización, el rol de η y el signo menos
El diagrama es propio: la presentación de introducción no tiene un gráfico de la superficie de error, solo la analogía de la pelota en el valle en prosa

### Speaker notes

Esta diapositiva es la que hay que dar bien para que las cinco siguientes no sean cinco fórmulas sueltas. Todo el resto de la sección son detalles de este dibujo, y conviene decirlo así al abrir y al cerrar.

La pregunta de apertura que funciona: si les doy la red y el dataset, ¿de qué depende el error? De los pesos, y de nada más. Ese es el salto conceptual, porque hasta acá venían pensando la loss como función de la predicción.

Dos honestidades, dichas al pasar y sin desarrollarlas: el dibujo tiene un eje y la red tiene millones, y la superficie real no es un valle limpio sino algo con mesetas y mínimos locales, así que el algoritmo llega a uno bueno, no al mejor. Si preguntan si entonces importa dónde se arranca: sí, y por eso la inicialización es una decisión.

No gastes acá la analogía de la pelota bajando por el valle: es de la diapositiva del paso de actualización, donde η le da sentido al largo del paso.

### Presenter feedback

---

## 2. Entrenar es un ciclo de dos movimientos

### Content

**Hacia adelante** la red calcula su predicción, una fila por vez. **Hacia atrás** reparte el error y deja anotado, en **valores intermedios**, cuánto contribuyó cada peso a equivocarse. Los pesos no se mueven todavía: se corrigen recién cuando terminó el batch entero, y ahí se pasa al batch siguiente.

```ascii
   hacia adelante: la red predice UNA fila del batch

   x --> [ capa 1 ] --> [ capa 2 ] --> [ salida ] --> y
                                                      |
                                                      |  L(y, t)
                                                      v
       [ capa 1 ] <-- [ capa 2 ] <-- [ salida ] <-----+

   hacia atras: cada peso recibe su parte de la culpa,
                y esa culpa se ACUMULA como valor intermedio

   W y b quedan quietos: se corrigen al cerrar el batch
```
<!-- ascii-note:
intent: mostrar el ciclo cerrado forward-backward de UNA fila, y que su resultado se acumula en vez de aplicarse
emphasize: que el error nace en la comparacion de y con t, viaja hacia atras por las mismas conexiones, y que W y b quedan intactos hasta el cierre del batch
labels: x entrada, y prediccion, t objetivo, L la loss; flechas hacia la derecha en el forward y hacia la izquierda en el backward; la linea final sobre W y b en tono de advertencia
-->

- **Propagación hacia adelante.** Empujar una fila a través de la red hasta obtener `y`. Es la misma cuenta que hace el modelo ya entrenado cuando predice.
- **Propagación hacia atrás.** Recorrer la red al revés calculando valores intermedios: cuánta culpa le toca a cada unidad (`δ`) y, a partir de eso, el gradiente de cada peso. Esos gradientes se **suman a un acumulador**; no se aplican.
- **La corrección, al cerrar el batch.** Cuando todas las filas del batch pasaron, se promedia el acumulador y ahí sí se corrigen `W` y `b`, una sola vez. Después arranca el batch siguiente con la red ya ajustada.
- **Lo que cambia y lo que no.** Cambian los pesos `W`, los sesgos `b` y las tablas de embedding. Los datos, la cantidad de capas y el learning rate quedan fijos: son hiperparámetros que elige quien entrena.

### Sources

knowledge-library/backpropagation/index.md (aportado por la Talk intro-redes-neuronales, capítulo 6 de su mazo)
corpus/chat.md.md (§1 Conceptos base: Qué cambia durante el entrenamiento)

### Speaker notes

Esta sección repite material que ya vieron en la clase de introducción, así que el tono es de repaso rápido, no de primera exposición. Preguntá al abrir quién se acuerda de qué hace el backward; según la respuesta, acelerá o frená.

El punto que ordena todo lo que sigue: la red no tiene ninguna forma de saber cuál era el valor correcto de un peso. Lo único que tiene es un número final que le dice cuánto se equivocó, y el algoritmo entero existe para repartir ese número hacia atrás.

Si alguien pregunta por qué el forward y el backward usan las mismas conexiones, la respuesta corta es que el backward recorre la misma cadena de operaciones al revés, aplicando derivadas en lugar de multiplicaciones.

### Presenter feedback

---

## 3. El número que hay que derivar

### Content

La sección anterior eligió la loss. Para derivarla, la deducción clásica usa la versión de mínimos cuadrados sobre las neuronas de salida.

![La función de coste L2](images/bp-funcion-de-coste.png)

- **Al cuadrado.** Los errores por exceso y por defecto dejan de cancelarse, y los grandes pesan más que los chicos. Es la misma propiedad que separaba MSE de MAE en la sección anterior.
- **El factor ½.** No mueve el mínimo. Está para que la derivada quede limpia: el 2 del exponente baja al derivar y se cancela contra él.
- **Diferenciable.** Es lo que permite calcular el gradiente y saber en qué dirección mover cada peso. Sin esta propiedad no hay algoritmo.

`y` es lo que la red predijo y `t` el objetivo. La suma recorre todas las unidades de salida.

**Ojo con la escala.** Esta fórmula es la loss de **una** fila. Lo que el entrenamiento deriva es el promedio de las `B` filas del batch, y ese promedio es el que produce el único ajuste del batch.

### Sources

knowledge-library/backpropagation/index.md (aportado por la Talk intro-redes-neuronales) — imagen `s32`, la función de coste L2 y sus tres decisiones de diseño

### Speaker notes

Aclará el ½ apenas aparece, porque en la sección anterior MSE se escribió sin él y alguien lo va a notar. La respuesta: multiplicar la loss por una constante positiva no cambia dónde está el mínimo, solo escala el gradiente, y el ½ se elige para que la derivada quede sin coeficientes. En la práctica los frameworks promedian sobre el batch y el ½ no aparece.

Esta es la única diapositiva de la sección donde conviene detenerse en la fórmula misma. Las que siguen son derivaciones de esta.

Si preguntan por qué se deriva sobre L2 si después van a usar cross-entropy, la respuesta es que el algoritmo no cambia: lo único que cambia es el primer factor de la cadena. La estructura del backward es la misma para cualquier loss diferenciable.

### Presenter feedback

---

## 4. La regla de la cadena

### Content

La pregunta que hay que responder es concreta: **¿cuánto cambia el error si movemos un peso en particular?** El peso no toca el error directo. Lo hace a través de la suma ponderada, y esta a través de la activación.

![La regla de la cadena en tres factores](images/bp-regla-de-la-cadena.png)

- **Cuánto cambia el error si cambia la salida.** Sale directo de la loss: la diferencia entre predicción y objetivo.
- **Cuánto cambia la salida si cambia la suma.** Es la derivada de la activación evaluada en ese punto.
- **Cuánto cambia la suma si cambia el peso.** Es la entrada que multiplicaba a ese peso, nada más.

El tercer factor sorprende por lo simple. Derivar `a = Σ xᵢwᵢ + b` respecto de uno de sus pesos deja la entrada que lo acompañaba.

Los tres factores son **valores intermedios**: se calculan, se multiplican y se acumulan. Ningún peso se movió todavía.

### Sources

knowledge-library/backpropagation/index.md (aportado por la Talk intro-redes-neuronales) — imagen `s33`, la regla de la cadena descompuesta en tres factores

### Speaker notes

La metáfora que funciona: el peso influye en el error a través de una cadena de tres eslabones, y la regla de la cadena dice que el efecto total es el producto de los tres efectos parciales.

Recorré los tres factores de derecha a izquierda en la fórmula, que es el orden en el que se calculan. El tercero es el más fácil y conviene mostrarlo primero para bajar la ansiedad: es literalmente la entrada.

El segundo factor es el que importa para la sección 1 de esta clase: es la derivada de la activación. Si esa derivada se aplana, el producto entero se va a cero y el peso deja de aprender. Es la razón por la que ReLU le ganó a la sigmoide en capas ocultas, y ya lo vieron en la diapositiva de las activaciones ocultas.

### Presenter feedback

---

## 5. El delta

### Content

Los dos primeros factores de la cadena se agrupan en un solo término, **`δ`**, la sensibilidad del error respecto de la suma ponderada de esa unidad. `δ` es el valor intermedio por excelencia del backward: se calcula, se usa para armar gradientes y se descarta. No es un parámetro de la red y no sobrevive al batch.

![La definición de delta en la capa de salida](images/bp-delta-salida.png)

- **Es una abreviatura, no un concepto nuevo.** Agrupa lo que ya estaba en la cadena.
- **La ganancia es concreta.** Con `δ` calculado, el gradiente de cualquier peso que llega a esa unidad es una multiplicación por su entrada. No hay que rehacer la cadena para cada peso.
- **Esa economía es lo que hace viable el algoritmo.** Sin ella, entrenar millones de parámetros sería impracticable.

El factor `y(1 − y)` de la fórmula es la derivada de la sigmoide. Con otra activación cambia ese factor y nada más.

### Sources

knowledge-library/backpropagation/index.md (aportado por la Talk intro-redes-neuronales) — imagen `s34`, la definición de delta en la capa de salida

### Speaker notes

Insistí en que delta no agrega nada nuevo, porque el símbolo asusta más de lo que debería. Es un nombre para dos factores que ya vieron juntos.

La fórmula de la imagen está escrita con sigmoide en la salida, y ese `y(1 − y)` es su derivada. Decilo explícito, porque si no queda como si fuera parte de la definición de delta. Con salida lineal el factor es 1; con softmax más cross-entropy la combinación se simplifica y delta queda directamente `y − t`, que es el resultado más lindo del tema y vale la pena mencionarlo.

Si preguntan por qué se molesta uno en definir delta, la respuesta práctica: una capa con 512 entradas y 256 neuronas tiene 131.072 pesos. Con delta se calculan 256 números y después cada gradiente es una multiplicación.

### Presenter feedback

---

## 6. Propagar el delta hacia atrás

### Content

Acá está el corazón del algoritmo, y arranca con una pregunta incómoda: **¿contra qué se compara una unidad oculta?** Contra nada. No tiene un objetivo propio, nadie le dice cuál era su valor correcto.

![Delta heredado de la capa siguiente](images/bp-delta-oculta.png)

Su culpa se calcula **sumando los deltas de todas las unidades de la capa siguiente a las que alimenta, ponderados por los pesos que las conectan**.

- **Capa de salida.** `δ` se calcula directo: hay un objetivo contra el cual comparar.
- **Capas ocultas.** `δ` se hereda de la capa siguiente, ponderado por los pesos de conexión.
- **Recursión.** El mismo cálculo se repite hacia atrás, capa por capa, hasta la primera.

De ahí el nombre: el error se propaga hacia atrás, y cada unidad recibe la parte de culpa que le corresponde según cuánto influyó en las que venían después.

Lo que viaja hacia atrás son **deltas, no pesos corregidos**. `W` y `b` siguen intactos durante todo el recorrido.

### Sources

knowledge-library/backpropagation/index.md (aportado por la Talk intro-redes-neuronales) — imagen `s35`, delta de una unidad oculta heredado de la capa siguiente

### Speaker notes

Esta es la diapositiva que justifica el nombre del algoritmo y la que más cuesta. Dale aire.

La pregunta de apertura conviene hacerla de verdad y esperar: ¿contra qué se compara una neurona del medio? El silencio es útil, porque la respuesta correcta es que no se compara contra nada, y esa es exactamente la dificultad que el algoritmo resuelve.

La imagen que funciona es la del jefe repartiendo culpa: la unidad oculta no sabe qué tenía que hacer, pero las tres unidades que alimenta sí saben cuánto se equivocaron, y le pasan su parte en proporción a cuánto la escucharon (los pesos de conexión).

Si alguien pregunta por qué se suma sobre la capa siguiente, la respuesta es que una unidad oculta influye en todas las de la capa siguiente a la vez, así que su culpa total es la suma de todas esas influencias.

### Presenter feedback

---

## 7. El paso de actualización

### Content

Cerrado el batch y promediados los gradientes acumulados, corregir un peso es restarle una fracción de su gradiente. Cuánta es esa fracción lo fija la **tasa de aprendizaje `η`**, y es uno de los hiperparámetros más sensibles del entrenamiento.

![El paso de actualización](images/bp-paso-de-actualizacion.png)

- **El signo menos.** El gradiente apunta hacia donde el error crece, así que el paso va en la dirección opuesta.
- **`η` muy chico.** El entrenamiento avanza, pero tan despacio que puede volverse impracticable.
- **`η` muy grande.** Los pasos se pasan del mínimo y el error oscila o diverge.

### Sources

knowledge-library/backpropagation/index.md (aportado por la Talk intro-redes-neuronales) — imagen `s36`, el paso de actualización y el rol de la tasa de aprendizaje

### Speaker notes

La imagen que funciona en clase es la pelota bajando por un valle, con `η` como el tamaño del paso: pasos chicos tardan una eternidad, pasos grandes saltan de una ladera a la otra sin bajar nunca.

Conectá con la sección 2 de esta clase: el gradiente respecto de un peso es proporcional al valor de la entrada, y el learning rate es uno solo para toda la red. Si una variable va de 0 a 1.000.000 y otra de 0 a 1, sus gradientes viven en escalas distintas y un solo `η` no le sirve a las dos. Ese es el argumento formal de por qué se normaliza el input, y ahora tienen la fórmula delante.

Si preguntan por Adam, la respuesta corta: escala el paso por parámetro y absorbe parte del problema, pero no arregla la saturación ni una inicialización rota.

### Presenter feedback

---

## 8. Batch y época no son lo mismo

### Content

Los pesos no se ajustan ejemplo por ejemplo ni una sola vez por dataset. El train se parte en **batches** de tamaño fijo, y cada batch produce **un** ajuste.

```ascii
   train: 10.000 filas,  batch = 100  ->  100 batches

   +---------+  +---------+  +---------+           +---------+
   | batch 1 |  | batch 2 |  | batch 3 |    ...    |batch 100|
   +---------+  +---------+  +---------+           +---------+
        |            |            |                     |
     forward      forward      forward               forward
     backward     backward     backward              backward
     1 ajuste     1 ajuste     1 ajuste              1 ajuste

   |<------------------------ 1 epoca ------------------------>|
                     100 ajustes de los pesos
```
<!-- ascii-note:
intent: separar visualmente el batch (una unidad de ajuste) de la epoca (una pasada completa por el train)
emphasize: que cada batch produce exactamente un ajuste y que la epoca es la suma de todos los batches
labels: 10.000 filas de train, batch de 100, 100 batches, 1 epoca, 1 ajuste por batch
-->

- **Batch.** Un subconjunto de filas del train que entra junto. Las `B` filas hacen el forward a la vez con los mismos pesos, se promedia su loss, y ese promedio es lo que se deriva.
- **Un ajuste por batch.** No uno por fila ni uno por dataset: exactamente uno cada vez que se cierra un batch. Con 10.000 filas y batch de 100 son 100 ajustes por vuelta.
- **Época.** Una pasada completa por todo el train, o sea por todos sus batches. Con 10.000 filas y batch de 100, una época son 100 ajustes de los pesos.

**El tamaño del batch es un hiperparámetro.** No se aprende: lo elige quien entrena, y cambia cuántos ajustes entran en cada época.

### Sources

corpus/chat.md.md (§1 Conceptos base: Pesos y bias — batches, input `(B,n)` a salida `(B,m)` con los mismos pesos para todas las filas; Qué cambia durante el entrenamiento — el batch size es hiperparámetro); §4 One-hot vs. embedding (gradiente ralo: solo se actualizan las filas presentes en el batch)
Keras, `Model.fit` — `batch_size`: "Number of samples per gradient update"; `epochs`: "An epoch is an iteration over the entire `x` and `y` data provided" <https://keras.io/api/models/model_training_apis/>
PyTorch, *Optimizing Model Parameters* — "Gradients by default add up; to prevent double-counting, we explicitly zero them at each iteration" <https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html>
El ejemplo aritmético (10.000 filas / batch 100 = 100 batches por época) es construido para la clase y no figura en el corpus

### Speaker notes

Esta diapositiva es el pedido explícito de la clase y la confusión más frecuente del tema, así que no la apures. La pregunta de apertura que la ordena: si el dataset tiene 10.000 filas y entrenamos 10 épocas, ¿cuántas veces se tocaron los pesos? Casi siempre contestan 10, o 10.000. Con batch de 100 son 1.000.

Los tres números que conviene dejar en el pizarrón: filas del train, tamaño del batch, ajustes por época. El tercero sale de dividir los dos primeros.

Si preguntan por qué no ajustar fila por fila, la respuesta tiene dos mitades: el gradiente de una sola fila es ruidoso y el promedio del batch lo estabiliza, y procesar 100 filas a la vez aprovecha la GPU mucho mejor que 100 pasadas sueltas.

Dato que conecta con la sección 2, por si hay tiempo: en una tabla de embeddings el gradiente es ralo, solo se actualizan las filas de las categorías que aparecieron en el batch. Un barrio que aparece tres veces en todo el train recibe tres actualizaciones y queda casi como se inicializó.

### Presenter feedback

---


## 9. El ciclo completo, batch a batch

### Content

Todo junto, y con el reloj a la vista: **dentro del batch se acumula, al cerrar el batch se aplica.**

```ascii
    .------------------------------------------------------------------.
                                                                      |
    v                                                                 |
    +--------------------------------------------------------------+  |
    |                                                              |  |
    |  BATCH k        B filas, todas con los MISMOS W y b          |  |
    |                                                              |  |
    |   fila 1  -> forward -> L -> backward --.                    |  |
    |   fila 2  -> forward -> L -> backward --+--> g += grad       |  |
    |    ...                                  |                    |  |
    |   fila B  -> forward -> L -> backward --'    ACUMULADOR      |  |
    |                                              (valores        |  |
    |                                               intermedios)   |  |
    |  W y b NO se tocan en ningun punto de este bloque            |  |
    |                                                              |  |
    +--------------------------------------------------------------+  |
                              |                                       |
                      termino el batch                                |
                              |                                       |
                              v                                       |
    +--------------------------------------------------------------+  |
    |                                                              |  |
    |  1. promediar    g <- g / B                                  |  |
    |  2. APLICAR      W <- W - n*g       b <- b - n*g             |  |
    |  3. vaciar       g <- 0                                      |  |
    |                                                              |  |
    |  unico momento del entrenamiento en que la red cambia        |  |
    |                                                              |  |
    +--------------------------------------------------------------+  |
                              |                                       |
                              '--- batch k+1, con W y b nuevos -------'

    agotados todos los batches = 1 epoca -> se baraja y vuelve a empezar
```
<!-- ascii-note:
intent: mostrar el ciclo de vida completo de un batch, con el limite exacto entre acumular y aplicar
emphasize: el bloque de arriba (donde W y b quedan intactos) contra el bloque de abajo (el unico donde cambian), y la flecha de retorno que cierra el ciclo hacia el batch siguiente
labels: BATCH k, filas 1 a B, forward, L la loss, backward, g el acumulador de gradientes, n es la tasa de aprendizaje, 1 epoca cuando se agotan los batches; el bloque de arriba en tono neutro y el de abajo destacado
-->

- **El forward es individual.** Cada fila del batch atraviesa la red por su cuenta y produce su propia predicción y su propia loss. Las `B` filas ven exactamente los mismos `W` y `b`.
- **El backward acumula, no aplica.** Calcula valores intermedios (`δ` por unidad, gradiente por peso) y los **suma** a un acumulador. La red no cambió.
- **Al cerrar el batch, el ajuste.** Se promedia el acumulador, se restan `η · g` de `W` y de `b`, y se vacía el acumulador. Un batch, un ajuste.
- **Y se pasa al siguiente.** El batch `k+1` arranca con la red ya corregida. Cuando se agotan los batches terminó una época, se baraja el train y vuelve a empezar.

**Por qué importa.** Porque explica algo que no se deduce de las fórmulas: el batch size no cambia solo la velocidad, cambia el resultado. Mueve cuántos ajustes entran en cada vuelta y cuánto ruido arrastra cada uno.

### Sources

PyTorch, *Optimizing Model Parameters* — el bucle canónico de tres pasos: "Gradients by default add up; to prevent double-counting, we explicitly zero them at each iteration"; "PyTorch deposits the gradients of the loss w.r.t. each parameter"; "Once we have our gradients, we call `optimizer.step()` to adjust the parameters by the gradients collected in the backward pass" <https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html>
Keras, `Model.fit` — `batch_size`: "Number of samples per gradient update" <https://keras.io/api/models/model_training_apis/>
Stanford CS231n, *Optimization* — "the gradient from a mini-batch is a good approximation of the gradient of the full objective" <https://cs231n.github.io/optimization-1/>
corpus/chat.md.md (§1 Conceptos base: Pesos y bias — las B filas pasan con los mismos pesos)

### Speaker notes

Es la diapositiva de síntesis de la sección: si el tiempo aprieta, esta se da igual y se recortan las fórmulas del medio. Dala señalando con la mano el límite entre los dos bloques: arriba no pasa nada en la red, abajo pasa todo. "Acumular arriba, aplicar abajo", repetido hasta que sea aburrido.

Las tres líneas del bloque de abajo son literalmente el bucle de PyTorch: `optimizer.zero_grad()` es vaciar, `loss.backward()` es acumular, `optimizer.step()` es aplicar. La documentación dice con todas las letras que los gradientes se suman por defecto y que hay que vaciarlos a mano para no contarlos dos veces. Si alguien ya programó, ahí es donde la diapositiva hace clic. Y si se olvidan de vaciar, el gradiente del batch anterior se suma al de este: el paso sale mal escalado y el entrenamiento se degrada sin tirar ningún error.

Una precisión que un alumno que programó va a marcar, y conviene decirla vos primero: el desglose fila por fila del dibujo es la descomposición matemática, no el código. `loss.backward()` se llama **una vez por batch** y la suma sobre las `B` filas ocurre vectorizada adentro. El resultado es idéntico, porque el gradiente del batch es el promedio de los gradientes por fila; el dibujo abre esa cuenta para que se vea de dónde sale.

Sobre barajar entre épocas: se hace para que los batches no sean siempre los mismos grupos de filas.

### Presenter feedback

---

## 10. Qué mirar cuando esto se entrena

### Content

En la práctica nadie mira las fórmulas: se mira la curva de loss y se toca alguna perilla. Este es el mapa de síntoma, causa y qué tocar.

| Lo que ves | Qué suele ser | Qué tocar |
|---|---|---|
| La loss no baja desde el arranque | `η` demasiado chico, o el gradiente se desvanece antes de llegar a las primeras capas | Subir `η` ×10; ReLU en las ocultas en vez de sigmoide; revisar la inicialización |
| La loss oscila fuerte, o se va a `NaN` | `η` demasiado grande, o el gradiente explota | Bajar `η` ÷10; recortar el gradiente con `clipnorm` o `global_clipnorm` |
| La loss baja pero con mucho ruido | Batch chico: el promedio sale de pocas filas y el gradiente es ruidoso | Subir el batch size |
| Train baja y validación sube | Overfitting, no un problema de gradiente | Sección 9 |
| Una variable domina el ajuste | Codificación de la entrada, no el gradiente | Sección 2 |

- **El gradiente que se desvanece.** Cada capa hacia atrás multiplica por la derivada de su activación. Si esa derivada es chica, el producto se achica capa tras capa y las primeras dejan de recibir señal. Es el argumento formal de por qué ReLU desplazó a la sigmoide en capas ocultas.
- **El gradiente que explota.** El problema simétrico: el producto crece y el paso se dispara. Se ataca recortando la norma del gradiente antes de aplicarlo.
- **Las perillas, en orden de impacto.** `η` primero y por lejos. Después el batch size. Después activación e inicialización. Último, cuántas capas y cuántas neuronas, que es lo que todos tocan primero.
- **Una perilla por vez.** Si se mueven dos y el resultado mejora, no se sabe cuál fue.

### Sources

Pascanu, Mikolov & Bengio (2013), *On the difficulty of training Recurrent Neural Networks* — "There are two widely known issues with properly training Recurrent Neural Networks, the vanishing and the exploding gradient problems"; proponen "a gradient norm clipping strategy to deal with exploding gradients and a soft constraint for the vanishing gradients problem" <https://arxiv.org/abs/1211.5063>
Keras, `Adam` y argumentos base del optimizador — `learning_rate` "Defaults to `0.001`"; `clipnorm`: "If set, the gradient of each weight is individually clipped so that its norm is no higher than this value"; `global_clipnorm`: "If set, the gradient of all weights is clipped so that their global norm is no higher than this value" <https://keras.io/api/optimizers/adam/>
Stanford CS231n, *Backpropagation* — el backward "starts at the end and recursively applies the chain rule to compute the gradients all the way to the inputs of the circuit" <https://cs231n.github.io/optimization-2/>
knowledge-library/backpropagation/index.md (aportado por la Talk intro-redes-neuronales) — η muy chico y η muy grande; la derivada de la sigmoide que se aplana en los extremos
La tabla de síntoma, causa y perilla es construida para la clase; no figura en el corpus

### Speaker notes

Esta es la diapositiva que los alumnos van a fotografiar, y la que más rinde en la práctica de laboratorio. Dala como checklist, no como teoría.

El orden de las perillas es el mensaje principal y es contraintuitivo: el reflejo de todo el mundo es agregar capas, y es lo último de la lista. `η` es la primera y la que más mueve la aguja. Conectá con la diapositiva 5 de la sección 1, donde ya dijimos que la cantidad de capas es lo que menos pesa; esta lo confirma desde el otro lado.

Las dos filas de `NaN` y de loss estancada son las que van a ver de verdad en la práctica. Si tenés tiempo, provocá una en vivo subiendo `η` a 10 y mostrá el `NaN`.

El gradiente que se desvanece ya apareció dos veces en la clase, en las activaciones ocultas y en el segundo factor de la regla de la cadena. Acá se cierra el círculo: aquel factor chiquito, multiplicado capa tras capa, es esto. Decilo explícito, porque es la conexión que hace que el tema deje de ser una anécdota sobre la sigmoide.

### Presenter feedback


# 7. Medir un clasificador

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

# 8. Capas ocultas

**Goal of this section:** La única parte de la arquitectura que se elige libremente, y la que menos pesa de las seis decisiones. Cuántas capas, cuánto ancho, qué activación y cómo arrancan los pesos. La sección da recetas de punto de partida y, sobre todo, el procedimiento para corregirlas mirando el error, en vez de adivinar. Cierra el recorrido de diseño justo antes de que el overfitting muestre qué pasa cuando sobra capacidad.

**Presenter feedback:**

---

## 1. Cuántas capas y cuánto ancho

### Content

Es la única decisión de la lista que se elige libremente, y la que menos impacto tiene. Conviene resolverla rápido con un punto de partida y corregir después mirando el error.

| Cuántos datos tenés | Punto de partida |
|---|---|
| Cientos de filas | 1 capa de 8 a 16 neuronas |
| Miles | 1 o 2 capas de 32 a 64 |
| Decenas de miles | 2 o 3 capas de 64 a 128 |

- **Más ancho que la entrada.** La primera capa oculta no debería ser más angosta que el vector de entrada, para no crear un cuello de botella que tire información antes de empezar.
- **Potencia de 2 y decreciente.** 128, 64, 32 hacia la salida. La potencia de 2 es alineación de memoria; lo decreciente es que la red va comprimiendo hacia la respuesta.
- **Lo que manda es la cantidad de datos.** La relación que importa es parámetros contra filas de entrenamiento, no parámetros contra features.
- **El procedimiento, no la fórmula.** Empezar chico y mirar el error de **train**: si es alto, falta capacidad y hay que agrandar; si el train está bien y la validación mal, sobra capacidad y hay que achicar o regularizar.

**1 a 3 capas ocultas alcanzan para datos tabulares.** Si necesitás más profundidad que eso en una tabla, el problema casi nunca es la arquitectura.

### Sources

corpus/chat.md.md (§ Arquitectura: cantidad de capas 1–3 para tabular, ancho en potencias de 2 decreciente; ancho de las capas ocultas — más ancho que la entrada, alineación de memoria, decreciente; datos y punto de partida — cientos / miles / decenas de miles; el procedimiento de empezar chico y mirar el error de train; la relación parámetros contra cantidad de datos)

### Speaker notes

Esta es la diapositiva que la clase espera desde el principio y la que hay que desinflar. Recordales la primera diapositiva de la sección 1: de las seis decisiones, esta es la última en impacto, y llegaron hasta acá sin haberla necesitado.

Lo que se llevan no es la tabla, es el procedimiento de las dos últimas líneas. La tabla es un punto de partida para no quedarse trabado; el error de train dice si hay que agrandar y la brecha con validación dice si hay que achicar. Es un lazo, no una fórmula cerrada.

Si preguntan por qué potencias de 2, la respuesta honesta es alineación de memoria en la GPU, y que la diferencia entre 60 y 64 neuronas no se va a notar en un dataset tabular. No lo vendas como si fuera profundo.

El cuello de botella es el error que más van a cometer: poner una primera capa de 8 neuronas después de un one-hot de 40 posiciones. La información se pierde ahí y ninguna capa posterior la recupera.

Y si alguien pregunta por el teorema de aproximación universal para justificar una sola capa muy ancha: es cierto y es inútil en la práctica, porque el teorema no dice cuántas neuronas hacen falta ni que el entrenamiento las vaya a encontrar.

### Presenter feedback

---

## 2. Las activaciones ocultas, y cómo se ven

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

**Nota:** la sigmoide y la tanh saturan. El **gradiente** es la derivada del error respecto de un peso: dice cuánto cambia el error si movés ese peso, y es lo único que el entrenamiento tiene para corregirlo (sección 6). Con `z` grande la derivada de estas dos es casi cero, el gradiente que llega a las capas de abajo se apaga y la red deja de aprender. ReLU no satura del lado positivo, y esa es la razón por la que ganó.

### Sources

corpus/chat.md.md (§1 Conceptos base: Activación)

### Speaker notes

Esta es la diapositiva que faltaba: hasta acá la activación era un nombre, ahora tiene forma. Recorré el diagrama de izquierda a derecha y detenete en el codo de ReLU: es literalmente dos rectas pegadas, y con eso alcanza. La pregunta que funciona: ¿por qué una función tan tonta le gana a las suaves? Respuesta corta, no satura y es baratísima de calcular. La saturación es el concepto que se llevan, y vuelve en la sección 2 con la normalización: una entrada grande sin normalizar satura la neurona igual que un `z` grande.

### Presenter feedback

---

## 3. Cómo arrancan los pesos

### Content

Los pesos empiezan en valores al azar, pero **no en cualquier azar**. La escala de esa inicialización decide si la señal sobrevive al atravesar las capas o se apaga en el camino.

- **Por qué no todos en cero.** Si todas las neuronas de una capa arrancan iguales, calculan lo mismo y reciben el mismo gradiente: quedan idénticas para siempre. El azar es lo que las hace distintas.
- **El efecto es multiplicativo.** Si cada capa multiplica la escala de las activaciones por un factor `c`, después de 10 capas el efecto es `c¹⁰`. Con `c = 1.5` la señal se multiplica por 58; con `c = 0.5` se divide por 1.000. Eso es exactamente el gradiente que explota y el que se desvanece de la sección 6.
- **He para ReLU, Glorot para el resto.** Las dos eligen la varianza de `W` para que `c` quede cerca de 1 al arrancar. He (o Kaiming) está pensada para ReLU; Glorot (o Xavier) para activaciones simétricas como tanh. Son el default de los frameworks, así que casi nunca hay que tocarlas.
- **Un solo problema, cuatro herramientas.** Normalizar la entrada, inicializar bien, normalizar entre capas (BatchNorm, LayerNorm) y recortar el gradiente atacan todos la misma cosa: que la escala no se descontrole al atravesar la red.

**Lo accionable es corto.** Dejá el default del framework, normalizá la entrada, y si el entrenamiento no arranca, revisá la inicialización antes de agregar capas.

### Sources

corpus/chat.md.md (§ Normalización y escala: el problema entre capas — qué viaja y cómo se controla; el efecto multiplicativo c=1.2→×6, c=1.5→×58, c=0.8→×0.1, c=0.5→×0.001 tras 10 capas; Xavier/He eligen Var(W) para c≈1 al inicio; BatchNorm, LayerNorm y conexiones residuales; el concepto único que unifica normalización del input, inicialización, normalización interna y control de gradientes)
Keras, inicializadores `HeNormal` y `GlorotUniform` — `GlorotUniform` es el default de `Dense` <https://keras.io/api/layers/initializers/>

### Speaker notes

Esta diapositiva es corta a propósito y cierra la sección. El mensaje operativo es el remate: no toques el default, normalizá la entrada. Todo lo demás es para que entiendan por qué el default es el que es.

El punto que más rinde es el multiplicativo, y conviene hacerlo con números en voz alta: 1.5 elevado a 10 da 58, 0.5 elevado a 10 da un milésimo. Ahí se ve que no hace falta ningún fenómeno raro para que el gradiente explote o se apague, alcanza con que cada capa desajuste un poco la escala.

Conectá con la sección 6: el gradiente que se desvanece y el que explota que aparecieron en la diapositiva de qué mirar durante el entrenamiento son este mismo fenómeno visto desde el backward.

Lo de arrancar todos en cero es la pregunta que siempre aparece, y la respuesta de la simetría es corta y satisfactoria: si arrancan iguales, se quedan iguales.

No abras BatchNorm ni LayerNorm más allá de nombrarlas. Están en la card para que sepan que existen y que atacan lo mismo, no para explicarlas.

### Presenter feedback

---

# 9. Overfitting

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
- **La loss viene con la salida.** Elegida la tarea quedan determinadas las neuronas, la activación y la fórmula que mide el error. Esa fórmula tiene que ser diferenciable, y esa es la razón por la que nadie entrena directamente sobre accuracy.
- **El ajuste ocurre una vez por batch.** El forward predice, el backward reparte la culpa capa por capa, y los pesos se corrigen recién cuando el batch entero terminó de procesarse. Una época son tantos ajustes como batches tenga el train.
- **Accuracy sola engaña.** La matriz de confusión separa los tipos de error; precision, recall y F1 describen lo que accuracy esconde, y el umbral es una perilla de negocio.
- **Regularizar es bajar varianza a propósito.** Primero se diagnostica el overfitting (brecha train-validación), después se trata: L2 de base, dropout en redes profundas, early stopping casi siempre.

### Sources

corpus/chat.md.md (§1, §8, §9, §10, §13); knowledge-library/backpropagation/index.md; conocimiento del área (sección 7)

### Speaker notes

Recapitulá siguiendo el recorrido del dato: se codificó (entrada), se partió (dataset), salió (salida), se le puso número al error (pérdida), se corrigieron los pesos (backpropagation), lo medimos (clasificador) y lo cuidamos (regularización). Siete ideas, una por sección troncal. Dejá espacio para preguntas antes del checklist.

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

- Sección 7 (Medir un clasificador) no está cubierta por el corpus (`chat.md.md`). El contenido viene del conocimiento del área. Si el presentador quiere anclarlo a una fuente propia (apunte, capítulo, ejemplo con números reales de un dataset del curso), conviene sumarla en la Colecta y re-verificar los números. El ejemplo del "99% de accuracy" y los costos FP/FN son ilustrativos, no datos de una fuente.
- La fuente advierte que en datos tabulares una red suele perder contra gradient boosting (XGBoost, LightGBM). Está en las notas del orador (slide 1.5) como contrapunto honesto. Decidir si darle más aire en clase o dejarlo como comentario al pasar.
- **Duración: es el problema más serio del mazo y empeoró en esta ronda.** 51 diapositivas de contenido para 90 minutos, contra 48 antes de esta ronda y 34 antes de la anterior. La sección 6 pasó de 7 a 10 diapositivas. A dos minutos por diapositiva la clase da 102 minutos sin una sola pregunta del público, y esta clase es presencial. Hay que recortar o partir la clase en dos, y es una decisión del presentador. Candidatas a recortar, en este orden: slide 8.4 (L1 contra L2), slide 3.4 (errores de partición, dejando los dos primeros bullets más el código), slide 7.7 (el umbral, que se puede dar solo con el diagrama), slide 5.6 (las especializadas), y dentro de la sección 6, fusionar 6.5 (el delta) con 6.4 (la regla de la cadena), que es la fusión más natural del mazo. **Lo que no conviene recortar de la sección 6** son 6.1, 6.9 y 6.10: son las tres pedidas explícitamente y las que más rinden por minuto.
- Diagramas: 15. Los 10 anteriores (formas de input por arquitectura, neurona, activaciones ocultas, one-hot, partición, activaciones de salida, desbalance de accuracy, matriz de confusión, umbral, curvas de overfitting, objetivo L2) más 5 nuevos de esta ronda: penalización de MSE/MAE/Huber, penalización de BCE, reparto de cross-entropy, ciclo forward-backward y batches contra época. Además hay 5 imágenes reusadas de la biblioteca de conocimiento, que no se renderizan.
- Las dos directivas `generate-image` (slides 1.1 y 8.1) siguen sin cumplir: ninguna sesión tuvo capacidad de generación de imágenes. Las diapositivas conservan su texto y no dependen de ellas.
- Ninguna de las dos fuentes nuevas cubre partición estratificada ni partición temporal, y las dos importan para los trabajos que entregan los alumnos. En la diapositiva 3.4 están como aporte del docente, sin fuente detrás. Si se quiere anclar, hace falta sumar una tercera fuente en la Colecta.
- Los ratios 70/20/10 y 80/10/10 son recomendación de la casa de Roboflow (contenido de marketing de producto), no resultado de un estudio. Están citados como criterio práctico de la industria; si alguien en clase pregunta de dónde salen, esa es la respuesta honesta.
- El artículo de Roboflow está escrito para visión por computadora y esta clase es tabular. Los ejemplos se trasladaron (imágenes a filas), la lógica no cambió. Revisar en el ensayo que no quede ningún resto de vocabulario de visión.
- El framing MLP de la sección 1 (diapositivas 1.2, 1.3 y 1.6) viene de una exploración del presentador en un chat, no del corpus. El corpus respalda las familias de estructura y su arquitectura natural (§2), los umbrales de one-hot contra embedding (§4) y la normalización z-score (§5), pero no el ejemplo de MNIST 28x28 con 784 posiciones ni el contraste de tres arquitecturas tal como quedó armado. Si se quiere anclar, la exploración se puede sumar en la Colecta como fuente propia.
- **Notación `y` / `t`.** Las secciones 5 y 6 usan `y` para la predicción y `t` para el objetivo, que es la notación de las cinco imágenes reusadas de la biblioteca de conocimiento y la que los alumnos ya vieron en `intro-redes-neuronales`. El corpus (§1) usa `y − ŷ`, o sea `y` para el valor real. Las dos convenciones son estándar y no se pueden mezclar. Si el presentador prefiere `ŷ`, hay que reescribir las fórmulas de la sección 5 y volver a dibujar las cinco imágenes.
- **Notas del orador por encima del presupuesto — 22 de 51 diapositivas superan las ~120 palabras** que `principles.md` fija para una diapositiva de 1 a 2 minutos. Se recortaron las cuatro de la sección 6 escritas el 2026-08-21 (6.1, 6.8, 6.9, 6.10); la 6.9 queda deliberadamente en ~235 porque es la de síntesis y carga el anclaje al bucle de PyTorch más la precisión de matemática contra API. Las peores pendientes son **2.6 (266 palabras)**, **1.2 (216)**, **5.3 (201)** y **5.2 (189)**, todas anteriores a esta ronda. Según la regla, una nota así larga significa que la diapositiva son dos: el remedio choca de frente con el problema de duración, así que la decisión va junto con esa.
- **La sección 6 no sale del corpus de esta Talk.** El algoritmo de backpropagation viene de `knowledge-library/backpropagation/index.md`, curado desde la Talk `intro-redes-neuronales`, cuya advertencia de procedencia dice que el material es de un mazo de clase y no de un paper. Las fórmulas son estándar y verificables en cualquier texto de deep learning. La mecánica de batches contra época (slide 6.7) es aporte propio apoyado en el corpus solo para el manejo de batches `(B,n)` y para que el batch size sea hiperparámetro.
- **La cita de apertura de la sección 5 (slide 5.1) no tiene fuente atribuida.** El texto es una paráfrasis cercana a la definición de IA como diseño de agentes racionales de Russell y Norvig (*Artificial Intelligence: A Modern Approach*). Confirmar con el presentador si va con atribución y, si es así, con qué edición, o si queda como cita sin atribuir.
- **Las fórmulas de las losses no están en el corpus.** El corpus nombra MSE, MAE, Huber, BCE, cross-entropy, Poisson NLL, pinball y NLL gaussiana en el catálogo de outputs (§8), pero no escribe ninguna fórmula ni el contraste entre las tres de regresión. Las fórmulas de las slides 5.3, 5.4 y 5.5 son estándar y están marcadas así en sus campos Sources.
- **La 1.3 y la 5.1 son diapositivas de una sola frase.** Las dos rinden en vivo y cuestan poco tiempo, pero dos citas a pantalla completa en un mazo de 48 diapositivas es un patrón nuevo. Vale mirarlas juntas en el ensayo.
- Las citas de Keras y PyTorch sobre el aplanado (notas del orador de la 1.2) están verificadas contra la documentación oficial pero no viven en el corpus. Ingerir las dos páginas si se las quiere como fuente formal de la Talk.

# Cut material

## Diapositiva 2.1 Que significa que el dato sea tabular - parrafo de cierre (retirado, 2026-08-21)

"Falta el paso de la columna al numero. Cada columna se convierte en una o mas posiciones del vector, y de que depende esa conversion es el resto de esta seccion." Retirado por pedido del presentador: la diapositiva 1.6 ya muestra ese paso con numeros (13 nodos desde dos variables) y la seccion 2 entera es ese desarrollo, asi que el parrafo anunciaba algo ya dicho.


## Diapositiva 1.6 Del dato a los nodos de entrada - todo el texto del cuerpo (retirado, 2026-08-21)

Por pedido del presentador la diapositiva quedo con el diagrama solo. El contenido sigue disponible en las notas del orador. Texto retirado:

Lead: "Que recibe el modelo en cada caso. Solo el MLP toma una fila de nodos sueltos y los procesa todos a la vez; los otros tres reciben la estructura entera y la recorren por partes."

- El largo no cambia. La red espera siempre la misma cantidad de entradas. Por eso las imagenes se redimensionan y el texto se trunca o se rellena hasta un largo fijo.
- La escala. Con una variable que va de 0 a 1.000.000 y otra de 0 a 1, la primera domina el entrenamiento por su magnitud y no por su importancia. Es el material de la seccion que sigue.

Remate: "Una tabla ya viene en la forma que un MLP espera. Por eso es el caso de esta clase."


## Diapositiva 1.6 Una posicion por variable - tabla Tipo de dato / Como se convierte en input (recortada, 2026-08-21)

Reemplazada por el diagrama de mapeo a nodos de entrada. La tabla era ademas un anticipo mas pobre de la 2.6 La tabla de decisiones, que recorre el mismo eje con diez filas y ademas dice cuantos floats ocupa cada codificacion. Texto retirado:

| Tipo de dato | Como se convierte en input |
|---|---|
| Numerico | Directo, normalizado a media 0 y desvio 1 |
| Categorico | One-hot hasta unas 15 categorias, embedding de 50 en adelante |
| Imagen | Pixeles normalizados, aplanados para un MLP |
| Texto | Tokenizacion y despues embeddings |
| Audio | Espectrograma, o la forma de onda muestreada |

Tambien se retiraron los dos bullets de apertura, que el diagrama ahora muestra con numeros: "Tabular. Una posicion por columna ya codificada: edad, ingreso, antiguedad." y "Imagen en escala de grises de 28 por 28. 784 posiciones, una por pixel, con el valor de gris normalizado."


## Diapositiva 1.2 El dato decide la arquitectura - tabla Dato / Forma / Arquitectura (recortada por densidad, 2026-08-21)

La diapositiva llevaba el diagrama de cuatro paneles y esta tabla a la vez, y las dos decian lo mismo: el diagrama ya muestra, para cada caso, el dato tal como es, la forma en que llega a la red y el nombre de la arquitectura. Con las dos juntas la diapositiva pasaba el presupuesto de densidad y el diagrama quedaba ilegible. Texto retirado:

| Dato | Su forma natural | Arquitectura |
|---|---|---|
| **Tabla** | Una fila de `n` numeros, una posicion por columna | MLP |
| **Senal** | Una secuencia de `T` pasos, donde el orden es parte del dato | CNN 1D / RNN |
| **Imagen en escala de grises** | Una grilla de alto por ancho, donde importa que pixel esta al lado de cual | CNN |
| **Imagen RGB** | La misma grilla, con tres numeros en cada pixel | CNN |

## Diapositiva 1.2 El dato decide la arquitectura - parrafo de alcance (retirado por el presentador, 2026-08-21)

El parrafo decia que el alcance de esta clase es el MLP sobre datos tabulares, que una tabla ya viene en la forma que un MLP espera, y que los otros tres se pueden aplanar en una fila pero al aplanar se pierde la vecindad. La declaracion de alcance sobrevive en las notas del orador y en el pill de MLP acentuado del diagrama.


## Diapositiva 6.7 "El paso de actualización" — bullet "Una vez por batch, no una vez por fila" (recortado por revisión Composer, 2026-08-21)

Duplicaba el bullet "Un ajuste por batch" de la 6.8, que es la diapositiva dueña del conteo. Texto retirado: "**Una vez por batch, no una vez por fila.** El paso se da con el gradiente promediado de las `B` filas que acaban de pasar, y después el acumulador se vacía." La 6.7 se queda con la aritmética del paso y con `η`.

## Diapositiva 6.8 "Batch y época no son lo mismo" — párrafo de notas sobre pesos quietos (recortado por revisión Composer, 2026-08-21)

Lo enuncia la 6.2 y lo dibuja la 6.9, así que en las notas de la 6.8 era la tercera vez. Texto retirado: "El punto que más se resiste es que los pesos quedan quietos durante el batch. La forma de decirlo: las 100 filas se evalúan todas con la misma red, la de antes del ajuste. Si los pesos cambiaran en el medio, las primeras filas y las últimas estarían evaluando modelos distintos."

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


## Párrafo de faltantes de la diapositiva 2.6 (borrado por el presentador en el borrador, 2026-08-21)

El presentador lo sacó de la diapositiva junto con el renombre de la columna. La sustancia (imputar y sumar un flag binario) quedó en las notas del orador, que ya respondían la pregunta de por qué faltantes no es una fila de la tabla. Texto retirado:

> **Faltar no es un tipo, le pasa a cualquiera.** Puede faltar un booleano, un barrio o una fecha, así que no es una fila más: es un modificador que se aplica sobre la fila que corresponda. Se imputa (media o mediana en las numéricas, categoría propia en las categóricas) y **se suma un float**, el flag binario que dice si el dato estaba. Ese flag muchas veces predice más que la variable misma.

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
