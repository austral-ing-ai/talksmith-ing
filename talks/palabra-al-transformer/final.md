---
presentation: Inteligencia Artificial Generativa (AI Gen)
class: "De la palabra al transformer"
research: research/corpus/
description: Slides are grouped into Sections. Each Section contains one or more Slides.
presenter: Paulo Veiga, Claudio Righetti, Marco Sorondo (Universidad Austral)
audience: Estudiantes de grado de Ingeniería de Software con base técnica fuerte
duration: 150 min (clase de 2:30 h)
date: 2026-09-23
---

# Thesis

**Claim:** Un modelo de lenguaje hace una sola cosa, predecir el token que sigue, y todo lo que la clase recorre (tokens, embeddings, capas, recurrencia y atención) existe para que esa predicción pueda usar el contexto entero en lugar de las últimas palabras.

**Why it matters:** Las decisiones que aparecen después en la materia (ventana de contexto, costo por consulta, alucinación, diseño de prompts) se explican desde ese mecanismo. Sin él, un LLM queda como una caja que a veces acierta.

---

# Agenda

**Narrative arc:**

La clase arranca por arriba, con las familias de problemas que la IA resuelve, y baja hasta la más chica de todas: predecir la palabra que sigue. Las tres primeras secciones instalan ese problema y muestran que todas las tareas de texto se pueden escribir así. La cuarta y la quinta arman las dos piezas que hacen falta para resolverlo con una red: convertir palabras en vectores y apilar perceptrones. La sexta es el nudo: procesar la frase token por token funciona y se rompe con la distancia, y la atención es lo que la desarma. La séptima cierra mostrando que un LLM de hoy es el mismo problema de la sección tres, con otro tamaño. Cómo se ajustan los pesos no se cuenta acá: lo da entero la clase de modelado de redes neuronales, y esta clase la da por vista.

**Sections (in delivery order):**

- 1. Familias de problemas
- 2. Por qué procesar texto
- 3. Modelado de lenguaje
- 4. Embeddings
- 5. De las RNN a la atención
- 6. Transformers y LLM

---

# 0. Portada

**Goal of this section:** Apertura del deck original — portada y mapa de la clase.

---

## 1. De la palabra al transformer

### Content

**Inteligencia Artificial Generativa (AI Gen) · Clase 8**

- **Cómo un modelo aprende a predecir la palabra que sigue**
- **Paulo Veiga, Claudio Righetti y Marco Sorondo (Universidad Austral)**
- **Última modificación: septiembre 2026**

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 1)

### Speaker notes

<!-- deck-omit-text: Presentate y presentá a los otros dos docentes. --> Portada. Presentate y presentá a los otros dos docentes.

---

# 1. Familias de problemas

**Goal of this section:** Ubicar el modelado de lenguaje dentro del mapa completo de problemas que resuelve la IA, y dejar clara la inversión que define a machine learning.

---

## 1. Siete familias de problemas de IA

<!-- format: editorial -->

### Content

**Cada familia se define por la forma de su entrada y de su salida, no por el dominio en el que se aplica.**

- **Predicción** Aprender una función de X a Y a partir de datos etiquetados. Incluye clasificación y regresión.
- **Percepción** Extraer estructura de señales sensoriales: imagen, audio, video.
- **Representación** Aprender embeddings y espacios latentes que capturan relaciones entre datos.
- **Decisión secuencial** Maximizar recompensa acumulada a lo largo de una serie de acciones. Se formaliza como reinforcement learning.
- **Búsqueda y planificación** Encontrar la mejor secuencia de acciones dentro de un espacio de estados.
- **Razonamiento simbólico** Manipular símbolos y reglas IF–THEN para derivar conclusiones lógicas.
- **Generación** Producir muestras nuevas y coherentes: texto, imagen, audio, código. La cantidad de salidas posibles no tiene tope.

- 💡 Un sistema real casi nunca usa una sola. Un auto autónomo combina percepción, decisión secuencial y planificación.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 3) — las siete definiciones, verbatim del deck original.

### Speaker notes

Lámina de encuadre. Lo único que hay que dejar clavado es que la última familia, generación, es la que ocupa el resto de la clase, y que las otras seis aparecen para dar contraste. Si alguien pregunta por qué representación y generación suenan parecidas, la respuesta corta es que representación aprende el espacio y generación produce puntos nuevos dentro de él; las secciones de embeddings y de transformers lo muestran en concreto. El deck original ponía ocho iconos y nombraba siete categorías: el octavo icono era la viñeta del callout, no una familia. Los ocho se retiraron.

---

## 2. El modelo aprende las reglas

### Content

**La programación clásica recibe reglas y datos, y devuelve respuestas. Machine learning recibe datos y respuestas, y devuelve las reglas.**

![La inversión entre programación clásica y machine learning: las mismas tres piezas cambian de lado](images/s1-2-1-inversion-reglas-datos.svg)
<!-- ascii-source:
                     ENTRA               PROCESO            SALE

  PROGRAMACION       reglas      ---.
  CLASICA                            +--&gt; [ programa  ] --&gt; respuestas
                     datos       ---'


  MACHINE            datos       ---.
  LEARNING                           +--&gt; [ entrenar  ] --&gt; reglas
                     respuestas  ---'


  reglas       entran arriba   ->   salen abajo
  respuestas   salen arriba    ->   entran abajo
  datos        entran en los dos

  Lo que en un paradigma se escribe a mano, en el otro se deduce.
-->
<!-- ascii-note:
intent: mostrar que los dos paradigmas usan las mismas tres piezas y que lo que cambia es cual es entrada y cual es salida; el nombre del proceso es lo de menos
emphasize: las tres lineas de abajo, que nombran la inversion pieza por pieza. En el cuerpo, la palabra "reglas" en las dos filas: entra en la de arriba y sale en la de abajo, y esa es toda la leccion
labels: "ENTRA", "PROCESO", "SALE", "PROGRAMACION CLASICA", "MACHINE LEARNING", "reglas", "datos", "respuestas", y las tres lineas de inversion
-->

- **Lo que se escribe a mano cambia de lugar.** En el paradigma clásico alguien escribe las reglas. En machine learning alguien junta ejemplos resueltos, y el algoritmo escribe las reglas.
- **La consecuencia práctica** El costo se muda de la lógica al conjunto de datos. Cuando cada tarea necesitaba su propio conjunto etiquetado a mano, ese costo se pagaba entero una vez por tarea.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 4) — la lámina original era solo el título y una figura. La figura se rehizo como diagrama propio: era un esquema plano rotulado en inglés que codificaba la inversión con el color de los círculos, y el diagrama nuevo la nombra pieza por pieza.

### Speaker notes

La figura es el argumento entero y conviene recorrerla en voz alta: fila de arriba, reglas más datos entran y salen respuestas; fila de abajo, datos más respuestas entran y salen reglas. Es la definición operativa de machine learning y la más útil para esta audiencia, porque describe qué artefacto produce el equipo. La figura está en inglés (Rules, Data, Answers, Classical Programming, Machine Learning); traducila al pasar. El título del deck original tenía un typo, "IA moAderna", corregido acá.

---

## 3. Clasificar: elegir entre categorías

### Content

**Asignar una entrada a una de varias categorías conocidas de antemano. La salida es una etiqueta de un conjunto cerrado.**

- **Clasificación** Asignar una entrada a una de varias categorías conocidas de antemano. Pregunta: ¿a qué categoría pertenece? Ejemplo: decidir si un correo es spam.

![Diagrama de clasificación de imágenes: una foto de un gato entra a una caja rotulada Modelo y sale la etiqueta CAT](images/clasificacion-de-imagenes.png)

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 5) — las dos formulaciones y sus ejemplos, verbatim.
- Diagrama propio. La lámina original ilustraba la regresión con una captura de un curso en video, en inglés y con un error tipográfico en su propio título; se rehízo como diagrama propio en español, con el mecanismo y sin nada de la fuente.

### Speaker notes

Primera de las dos formulaciones de predicción. La figura es literal y conviene usarla así: entra una foto, sale una etiqueta. Lo que define la clasificación es que el conjunto de salidas está fijado de antemano y el modelo elige uno.

---

## 4. Regresión: estimar un número

### Content

**Estimar un valor continuo a partir de las características de la entrada. La salida es un número, no una etiqueta.**

- **Regresión** Estimar un valor continuo a partir de las características de la entrada. Pregunta: ¿qué valor va a tener? Ejemplo: estimar el precio de una casa por sus metros cuadrados.

<!-- ascii-render: force -->
![Una recta de regresión devuelve un precio incluso en el tramo donde no se vendió ninguna casa](images/s1-3-1-regresion-hueco-datos.svg)
<!-- ascii-source:
   precio
      ^
      |                                           .    ,-'
      |                                       ,-'
      |                           .     ,-'        .
      |                      .      ,-'
      |               .        ,-'
      |         .        ,-'  (?)      .
      |      .      ,-'        ^
      |   ,-'   .              |
      +-------------------------------------------&gt; metros cuadrados
                               |
                    aca no se vendio ninguna casa, y la recta
                    igual devuelve un precio
   Cada punto es una casa ya vendida: sus metros y lo que pago
   alguien. La recta es el modelo, y contesta en todo el eje, asi
   que se le puede pedir el precio de un metraje que nunca aparecio
   en los datos. La salida sale de un rango continuo, y por eso los
   valores posibles no se pueden enumerar.
-->
<!-- ascii-note:
intent: mostrar que un modelo de regresion contesta tambien donde no hay datos, que es lo que separa una salida continua de una eleccion entre categorias; el ejemplo del metraje no vendido es el argumento
emphasize: el signo (?) sobre la recta en el hueco sin puntos, con su llamada al pie; es lo que el listado de la lamina no dice
labels: "precio", "metros cuadrados", "(?)", "aca no se vendio ninguna casa, y la recta igual devuelve un precio", "La salida sale de un rango continuo"
-->

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 5) — las dos formulaciones y sus ejemplos, verbatim.
- Diagrama propio. La lámina original ilustraba la regresión con una captura de un curso en video, en inglés y con un error tipográfico en su propio título; se rehízo como diagrama propio en español, con el mecanismo y sin nada de la fuente.

### Speaker notes

La clasificación queda del lado de la figura y la regresión del lado del diagrama: una salida discreta y una continua, en la misma pantalla. El ejemplo de la casa del texto y el del diagrama coinciden, así que se pueden señalar juntos. Detenete en el signo de pregunta: ahí no se vendió ninguna casa y la recta contesta igual, y ésa es la diferencia práctica con elegir entre categorías. La nube de puntos y la recta son esquemáticas, sin escala en los ejes a propósito, porque no hay ningún conjunto de datos detrás. La lámina original juntaba las cuatro formulaciones y cuatro figuras en una sola pantalla; acá van de a dos.

## 5. Agrupar y crear datos nuevos

<!-- design: split-right -->

### Content

**Las otras dos formulaciones no tienen respuesta correcta escrita de antemano: una descubre la estructura, la otra produce muestras que no estaban en los datos.**

- **Clustering** Agrupar elementos parecidos sin categorías definidas de antemano. Pregunta: ¿qué datos se parecen entre sí? Ejemplo: agrupar los tickets de soporte que describen la misma falla, sin haber decidido antes cuáles son las fallas.
- **Generación** Producir datos nuevos que se parezcan a los de entrenamiento sin copiarlos. Pregunta: ¿puedo crear datos que no estaban? Ejemplo: escribir texto o completar código.

![El agrupamiento forma los grupos de tickets; los nombres los pone una persona después](images/s1-4-1-agrupar-tickets.svg)
<!-- ascii-source:
  ANTES                            DESPUES DE AGRUPAR

  una pila de tickets,             tres grupos, y recien ahora
  sin categoria ninguna            se les puede poner nombre

   t1  "no carga el login"          +----------------+
   t2  "el pago tira 500"           | t1   t3   t7   |  <- una persona
   t3  "no puedo entrar"            +----------------+     los lee y
   t4  "la factura sale mal"                               les pone
   t5  "timeout al pagar"           +----------------+     nombre
   t6  "no llega el recibo"         | t2   t5        |     recien
   t7  "usuario bloqueado"          +----------------+     aca
   t8  "el importe no cierra"
                                    +----------------+
                                    | t4   t6   t8   |
                                    +----------------+

  El algoritmo forma los grupos midiendo parecido entre los textos.
  No sabe que el primero es "acceso" ni el tercero "facturacion":
  los nombres los pone alguien despues, mirando el resultado.
-->
<!-- ascii-note:
intent: mostrar que el agrupamiento produce los grupos y no los nombres; el algoritmo mide parecido y las etiquetas las pone una persona despues, que es lo que distingue agrupar de clasificar
emphasize: las tres cajas de la derecha con sus tickets adentro, y la llamada que dice que el nombre llega despues y lo pone una persona
labels: "ANTES", "DESPUES DE AGRUPAR", "una pila de tickets, sin categoria ninguna", "tres grupos, y recien ahora se les puede poner nombre", "una persona los lee y les pone nombre recien aca", "El algoritmo forma los grupos midiendo parecido entre los textos"
-->

- 💡 El modelo aprende patrones de los datos. Nadie le escribe las reglas.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 5) — las dos formulaciones y el cierre sobre patrones.
- Diagrama propio. La lámina original ilustraba el agrupamiento con una figura de un tercero, en inglés y con su logo proyectado; se rehízo como diagrama propio en español, con el mecanismo y sin nada de la marca.

### Speaker notes

El clustering es el que más cuesta, porque la pregunta "¿qué datos se parecen?" suena vacía hasta que se ve un caso. El de tickets de soporte funciona bien con esta audiencia: nadie sabe de antemano cuántas fallas distintas hay en la cola, y agrupar es justamente cómo se descubren. Leé dos o tres tickets de la columna izquierda y preguntá cómo los agruparían; van a dar los tres grupos del diagrama sin esfuerzo, y ése es el momento de decir que el algoritmo llega hasta ahí y no más. Los nombres —acceso, pagos, facturación— los pone una persona mirando el resultado, y eso es lo que separa agrupar de clasificar.

---

# 2. Por qué procesar texto

**Goal of this section:** Mostrar que toda tarea de texto cae en las mismas familias ya vistas, y qué costaba resolverlas antes de que un solo modelo sirviera para todas.

---

## 1. Los mismos problemas, con texto

### Content

**Cada formulación clásica tiene su equivalente cuando la entrada es texto. Cambia el tipo de dato, no la forma del problema.**

| Formulación | Qué resuelve | Ejemplo con texto |
|---|---|---|
| Clasificación | Asignar una categoría | ¿Este comentario es positivo o negativo? |
| Clasificación multiclase | Elegir entre varias categorías | ¿En qué idioma está escrito? |
| Clustering | Agrupar datos similares | Agrupar incidentes por causa raíz |
| Predicción | Completar información faltante | `The ___ is on the mat` → `cat` |
| Generación | Crear datos nuevos | `The cat is on the ___` → `mat` |

- **Predicción y generación son la misma operación en distinta posición.** Las dos completan un hueco con el token más probable; la única diferencia es dónde está el hueco.
- **Todas necesitan lo mismo primero:** alguna forma de convertir texto en algo que un modelo pueda operar. Eso es tokenizar y embeber, y es la sección *Tokens y embeddings*.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 6) — la tabla completa y la pregunta bisagra que cierra la lámina.

### Speaker notes

Lámina bisagra entre el mapa general y el resto de la clase. El punto que conviene subrayar es el primero de los dos de abajo, porque anticipa el modelado de lenguaje: predicción y generación son la misma cuenta, y por eso un modelo que sabe completar huecos sabe escribir. Las dos últimas filas de la tabla lo muestran con la misma frase. El ejemplo de sentimiento del deck original ("qué bien comimos en el restaurante") se retiró: la columna de la derecha ya trae uno.

---

## 2. Hay más texto del que se puede leer

### Content

**Procesamiento del lenguaje natural (NLP) es el campo que se ocupa de resolver estas tareas de forma automática, sobre volúmenes de texto que nadie va a leer entero.**

- **De dónde sale el texto** Tickets de soporte, mensajes de commit, logs de aplicación, documentación técnica, hilos de incidentes, correos, foros y reseñas de usuarios.
- **Qué se le pide** Analizar miles de reportes de usuarios sobre una misma versión; clasificar tickets por área; detectar el idioma de un documento; responder preguntas sobre un texto largo; resumir un informe de treinta páginas en un párrafo.

- 💡 El volumen es lo que convierte estas tareas en un problema de ingeniería. Cualquiera de ellas la resuelve una persona sobre diez documentos; ninguna se resuelve así sobre diez mil.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 7) — la definición del campo, el argumento de volumen y la lista de casos de uso.

### Speaker notes

Lámina corta y de motivación. Lo que la sostiene es el callout del final: la escala es lo que separa una tarea de NLP de un rato de lectura. Si querés un caso propio, la cola de tickets de cualquier equipo grande sirve, porque nadie la lee entera y todos necesitan saber qué hay adentro. El deck original listaba historias clínicas y opiniones de pacientes sobre un tratamiento, heredados de la materia anterior; están convertidos.

---

## 3. Veinticinco tareas de NLP

### Content

**Las cinco familias, aterrizadas. Cada columna es una formulación de la lámina anterior y cada celda una tarea que alguien resuelve hoy en producción.**

| Clasificación | Clasificación multiclase | Clustering | Predicción | Generación |
|---|---|---|---|---|
| Detección de spam (spam / no spam) | Detección de idioma (español, inglés, francés…) | Agrupar noticias por tema | Autocompletar en un buscador | Resumen automático de textos |
| Análisis de sentimiento (positivo / negativo) | Clasificación de intención (comprar, preguntar, quejarse…) | Agrupar reseñas similares de productos | Predecir la siguiente palabra de una oración | Traducción automática |
| Detección de discurso de odio (sí / no) | Etiquetado gramatical (sustantivo, verbo, adjetivo…) | Segmentar usuarios por estilo de escritura | Completar huecos en el texto (masked LM) | Generación de respuestas en chatbots |
| Detección de noticias falsas (real / falsa) | Clasificación de emociones (alegría, tristeza, enojo, miedo…) | Descubrir tópicos en un corpus | Predecir la puntuación de una reseña | Generación de código a partir de texto |
| Detección de paráfrasis (sí / no) | Clasificación de tickets de soporte (facturación, técnico, ventas…) | Agrupar documentos legales por área | Predecir palabras faltantes en un OCR dañado | Parafraseo automático de oraciones |

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 8) — la matriz completa, verbatim.

### Speaker notes

Lámina de referencia, no de lectura. Señalá una celda por columna y seguí; la matriz está para que quede como material de consulta. La celda que conviene marcar es "predecir la siguiente palabra de una oración", en la columna de predicción, porque es la que abre la sección siguiente y la que termina absorbiendo a casi todas las demás cuando aparecen los modelos fundacionales.

---

## 4. Un modelo por tarea

### Content

**Antes de los modelos fundacionales, cada tarea de la matriz anterior necesitaba su propio conjunto de datos etiquetado y su propio modelo entrenado desde cero.**

![Tres tareas, tres columnas aisladas, y el etiquetado humano como tramo caro del medio](images/s2-4-1-un-modelo-por-tarea.svg)
<!-- ascii-source:
  TAREA 1  sentimiento     TAREA 2  traduccion     TAREA 3  entidades
  +------------------+   +------------------+   +------------------+
  | textos crudos    |   | textos crudos    |   | textos crudos    |
  +------------------+   +------------------+   +------------------+
           |                      |                      |
           v  etiqueta            v  etiqueta            v  etiqueta
           |  una persona         |  una persona         |  una persona
  +------------------+   +------------------+   +------------------+
  | pos / neg        |   | pares es <-> en  |   | PER / ORG / LOC  |
  +------------------+   +------------------+   +------------------+
           |                      |                      |
           v                      v                      v
  +------------------+   +------------------+   +------------------+
  | modelo propio    |   | modelo propio    |   | modelo propio    |
  +------------------+   +------------------+   +------------------+

  Nada cruza de una columna a la otra. Sumar una tarea cuesta una
  columna entera, y el tramo caro es el del medio: lo escribe una
  persona, una fila por vez.
-->
<!-- ascii-note:
intent: mostrar que el costo del enfoque tradicional no está en el modelo sino en la etiqueta, y que las columnas son independientes: nada de lo hecho para una tarea sirve para la siguiente
emphasize: la fila del medio, el etiquetado humano, que es donde está el costo real; el aislamiento de las tres columnas, que nunca se tocan
labels: "TAREA 1 sentimiento", "TAREA 2 traduccion", "TAREA 3 entidades", "textos crudos", "etiqueta una persona", "pos / neg", "pares es <-> en", "PER / ORG / LOC", "modelo propio", "Nada cruza de una columna a la otra"
-->

- **Recolectar, etiquetar, entrenar** eran los tres trabajos, y el segundo no se automatizaba: alguien tenía que marcar a mano qué era positivo y qué negativo.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 9) — los tres pasos del enfoque tradicional y el cierre: "cada tarea requería su propio pipeline, sus propios datos etiquetados, su propio modelo. Era costoso y lento."

### Speaker notes

El diagrama dice algo que la lista del deck original no decía: el costo no está en entrenar sino en etiquetar, y no se amortiza entre tareas. Recorré las tres columnas señalando que ninguna flecha cruza de una a otra. Esta lámina es la que le da peso al cierre de la clase: cuando se muestre que las tres tareas se resuelven con el mismo modelo y tres prompts distintos, el contraste es contra esta imagen. La viñeta decorativa del deck original en esta lámina se retiró.

---

# 3. Modelado de lenguaje

**Goal of this section:** Formular el problema que resuelve un LLM —predecir el token siguiente— y dejar claro que su salida es una distribución sobre el vocabulario entero, no una palabra.

---

## 1. Predecir la palabra que sigue

### Content

**El problema tiene tres entradas: un vocabulario V, un corpus de texto T y una frase incompleta P. La salida es el token más probable a continuación de P.**

![La ventana deslizante convierte una frase cruda en cinco pares de entrada y respuesta](images/s3-1-1-ventana-deslizante.svg)
<!-- ascii-source:
  Una frase del corpus, sin una sola etiqueta escrita a mano:

      the   cat   sat   on   the   mat

  La ventana avanza un token por vez. Lo que quedo a la izquierda
  es la entrada; el token siguiente es la respuesta correcta.

      [ the ]                       ->  cat
      [ the cat ]                   ->  sat
      [ the cat sat ]               ->  on
      [ the cat sat on ]            ->  the
      [ the cat sat on the ]        ->  mat

  Una frase de 6 tokens dio 5 ejemplos de entrenamiento, y la
  respuesta correcta de cada uno ya estaba escrita en el texto.
  Ahi esta la diferencia con la lamina anterior: nadie etiqueto.
-->
<!-- ascii-note:
intent: mostrar que la supervisión del modelado de lenguaje sale del propio texto: la ventana que se corre convierte una frase cruda en varios pares entrada-respuesta sin intervención humana
emphasize: la columna de respuestas correctas a la derecha de las flechas, que es lo que en la lámina anterior escribía una persona; el pie que cierra el contraste
labels: "the cat sat on the mat", "La ventana avanza un token por vez", "entrada", "respuesta correcta", "6 tokens dio 5 ejemplos", "nadie etiqueto"
-->

- **Por qué esto escala y lo anterior no.** El texto crudo trae la respuesta adentro. Todo lo escrito en internet es un conjunto de entrenamiento ya etiquetado para esta tarea.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 10) — la formulación con V, T y P, y el objetivo "predecir cuál es la siguiente palabra más probable".

### Speaker notes

Ésta es la lámina que hay que dejar clavada de la sección. El diagrama contesta la pregunta que queda flotando desde el enfoque tradicional: si etiquetar es lo caro, cómo se entrenaron los modelos grandes. La respuesta es que para esta tarea la etiqueta ya está escrita, y por eso el conjunto de entrenamiento es todo el texto disponible. Contá los ejemplos en voz alta: seis tokens, cinco pares. Si alguien pregunta por qué son cinco y no seis, es porque el último token no tiene siguiente. La viñeta decorativa del deck original en esta lámina se retiró.

---

## 2. La salida es un vector, no una palabra

### Content

**El modelo devuelve un número por cada token del vocabulario: la probabilidad de que ese token sea el siguiente. El vector tiene longitud |V|.**

![La salida del modelo es un valor por cada token del vocabulario, no una palabra](images/s3-2-1-distribucion-vocabulario.svg)
<!-- ascii-source:
  ENTRADA   "the cat is on the"
                     |
                     v
                [ MODELO ]
                     |
                     v
  SALIDA    un valor por cada token del vocabulario

     mat    #################################
     bed    ############
     floor  #####
     dog    ##
     the    #
     roof   .
     ...    y asi hasta completar los |V| tokens
            -----------------------------------------------
            los |V| valores suman 1

  La lista entera es la salida del modelo. Quedarse con la barra
  mas larga es un paso aparte, y no es el unico: muestrear entre
  las primeras es lo que hace que el mismo texto de entrada no
  devuelva siempre la misma continuacion.
-->
<!-- ascii-note:
intent: mostrar que la salida es una lista completa sobre el vocabulario y no una palabra, y separar dos cosas que se confunden: producir la distribucion, que hace el modelo, y elegir un token, que es un paso posterior
emphasize: la columna de barras entera, sobre todo las filas de abajo que casi no se ven y la linea de que los |V| valores suman 1; la barra mas larga es solo una fila de esa lista
labels: "ENTRADA", "MODELO", "SALIDA", "un valor por cada token del vocabulario", "los |V| valores suman 1", "La lista entera es la salida del modelo", "Quedarse con la barra mas larga es un paso aparte"
-->

- **Una posición por token del vocabulario.** El valor de cada posición es la probabilidad de ese token, y las |V| posiciones suman uno.
- **Elegir viene después.** Quedarse con el máximo es una decisión aparte, y no es la única. Muestrear con algo de aleatoriedad es la otra, y es lo que controla la temperatura.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 10) — el bloque "Importante": el modelo devuelve un vector de probabilidades sobre todo el vocabulario, de longitud |V|.
- Diagrama propio. La lámina original ilustraba esto con una miniatura de video del deck, en inglés y con estética de portada; se rehízo como diagrama propio en español, con el mecanismo y sin nada de la fuente.

### Speaker notes

El diagrama es el argumento entero: una frase incompleta entra, y lo que sale es la columna completa de barras. Recorré las filas de arriba abajo hasta las que casi no se ven, y decí que la lista sigue hasta completar el vocabulario. El punto que conviene decir en voz alta es el segundo de los de apoyo: el modelo produce la distribución, y elegir un token es una decisión de quien lo usa. Las barras son esquemáticas y no llevan números a propósito, porque no salen de ninguna corrida; lo único que se afirma es la estructura, que hay un valor por token y que suman uno.

---

## 3. Los modelos no leen letras

### Content

**Un token es la unidad mínima que el modelo procesa: una palabra entera, un pedazo de palabra o un signo de puntuación. Tokenizar es el primer paso de cualquier tarea de NLP.**

![Tokenización por palabra frente a sub-palabra ante una palabra nunca vista](images/s3-3-1-tokenizacion-subpalabra.svg)
<!-- ascii-source:
  POR PALABRA                          POR SUB-PALABRA

  "the cat sat on the mat"             "unbelievable"
             |                                |
             v                                v
  [the][cat][sat][on][the][mat]        [un][believ][able]
           6 tokens                          3 tokens


  UNA PALABRA QUE EL MODELO NUNCA VIO:  "descontracturante"

    por palabra      ->  [ <desconocido> ]
                         el contenido se pierde entero

    por sub-palabra  ->  [des][contract][urante]
                         se arma con piezas ya conocidas

  El vocabulario deja de tener que contener el idioma entero, y el
  mismo vocabulario sirve para varios idiomas a la vez.
-->
<!-- ascii-note:
intent: mostrar que la elección de unidad no es cosmética: con palabras enteras una palabra desconocida se pierde, con sub-palabras se reconstruye desde piezas que el modelo ya tiene
emphasize: el bloque de abajo, la palabra nunca vista, y en particular la línea de sub-palabra que la descompone en tres piezas conocidas; ése es el argumento que la parte de arriba no da
labels: "POR PALABRA", "POR SUB-PALABRA", "6 tokens", "3 tokens", "UNA PALABRA QUE EL MODELO NUNCA VIO", "<desconocido>", "des / contract / urante", "se arma con piezas ya conocidas"
-->

- **Vocabularios más chicos** No hace falta una entrada por cada palabra del idioma, y las palabras nuevas se arman con piezas.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 15) — la definición de token, los dos ejemplos de tokenización (6 y 3 tokens) y las tres ventajas de las sub-palabras.
- `AIG4B-Clase-2-LLM.md.md` (slide 14) — "el primer paso es lograr que el modelo entienda qué significan las palabras; para eso hay que representarlas como números".

### Speaker notes

Los dos conteos del diagrama están verificados contra el deck: "the cat sat on the mat" da seis tokens y "unbelievable" da tres. El ejemplo de la palabra desconocida es agregado y no está en el deck original: sirve porque es el único momento en que se ve para qué sirve la descomposición, y "descontracturante" funciona con esta audiencia porque nadie duda de que ningún vocabulario la va a tener. Si preguntan cómo se decide el vocabulario de sub-palabras, la respuesta corta es que se aprende del corpus por frecuencia, y que el algoritmo concreto (BPE y parientes) queda fuera de esta clase.

---

## 4. Catorce tokens y cinco frases

### Content

**El mismo problema, con números chicos: un vocabulario de 14 tokens, un corpus de 5 frases y una frase incompleta.**

- **V** `{ "a", "to", "on", "the", "sat", "cat", "dog", "bed", "ran", "mat", " ", "<fin>", ".", "," }` — 14 tokens.
- **T** `"the cat sat on mat"` · `"a dog ran to bed"` · `"the dog sat on bed"` · `"a cat ran to mat"` · `"the cat ran to dog"` — 5 frases.
- **P** `"the dog sat on"`. La única frase del corpus que empieza así continúa con `"bed"`, así que ésa es la respuesta correcta.

**Salida del modelo, un valor por token de V:**

`a: 0,01` · `to: 0,02` · `on: 0,03` · `the: 0,04` · `sat: 0,01` · `cat: 0,01` · `dog: 0,02` · **`bed: 0,78`** · `ran: 0,03` · `mat: 0,04` · `" ": 0,01` · `<fin>: 0,00` · `".": 0,00` · `",": 0,00`

- **El vector objetivo es todo ceros y un uno** en la posición de `bed`. Entrenar es acercar la salida del modelo a ese vector.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 11) — vocabulario, corpus, frase incompleta y vector de salida, verbatim.
- Verificación aritmética: los 14 valores del vector suman exactamente 1,00 (0,01 + 0,02 + 0,03 + 0,04 + 0,01 + 0,01 + 0,02 + 0,78 + 0,03 + 0,04 + 0,01 + 0,00 + 0,00 + 0,00), y el vocabulario listado tiene 14 entradas.

### Speaker notes

Los números cierran: el vector suma uno exacto y el vocabulario tiene los catorce tokens que declara. Si alguien los suma en el momento, van a dar. La frase incompleta se resuelve por la tercera del corpus, "the dog sat on bed". El deck original la identificaba como `T[2]` sin declarar si indexaba desde cero o desde uno; acá se dice cuál es la frase en vez de su índice, porque las dos lecturas dan "bed" y la ambigüedad no aporta nada. Notá también que la primera frase del corpus dice "the cat sat on mat" y no "the cat sat on the mat": es un corpus de juguete y está bien, pero si alguien lo marca, es eso.

---

## 5. Aprender es ajustar parámetros

### Content

**Un modelo por dentro es un conjunto de números ajustables. Entrenar es buscar los valores que hacen que la salida se parezca al vector objetivo.**

- **Parámetros** Los números internos del modelo, los que el deck llama "clavijas". Empiezan en valores arbitrarios y son lo único que el entrenamiento modifica.
- **Loss (pérdida)** Un número que mide qué tan lejos quedó la salida del modelo del vector objetivo. Cuanto más chico, mejor predijo.
- **Optimización** El procedimiento que ajusta los parámetros para que la loss baje. Termina quedándose con los valores que dan la loss más chica.

- 💡 El método no depende de la tarea. Cambia qué es la respuesta correcta (el token siguiente, la categoría, el número) y el resto del procedimiento es el mismo para cualquiera de las tareas de NLP ya vistas.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 13) — la metáfora de las clavijas y las definiciones de loss y optimización, verbatim.
- `AIG4B-Clase-2-LLM.md.md` (slide 14) — "el mismo método sirve para resolver cualquiera de los problemas ya vistos".

### Speaker notes

Lámina de vocabulario, corta a propósito. Las tres definiciones se usan sin parar en las dos secciones de redes neuronales, así que conviene decirlas despacio y no volver sobre ellas. El ciclo concreto (cómo se calcula la loss, en qué dirección se mueven los parámetros) es la sección *Cómo aprende una red* entera y acá no se adelanta. Si alguien pregunta cuántos parámetros, la respuesta llega al hablar de profundidad. Una advertencia sobre el deck original: sus pasos 03 y 04 decían "la palabra más probable era alfombra", confundiendo la palabra correcta del corpus con la más probable según el modelo, que es justamente lo que se está comparando; acá esa redacción no se usa.

---

# 4. Embeddings

**Goal of this section:** Cerrar el camino de texto a números: cómo se parte una frase en unidades y cómo se le da a cada unidad un vector cuya distancia significa algo.

---

## 1. Tres formas de volver texto en números

### Content

**El vocabulario V es el conjunto de tokens que el modelo conoce, y por eso predice un vector de tamaño |V|. Pero un token es texto, y los parámetros son números: hace falta una representación numérica.**

- **Bag of words / TF-IDF** Contar apariciones de cada palabra. Ignora el orden y el significado.
- **One-hot encoding** Un vector de largo |V| con un solo uno, en la posición del token. Distingue tokens, pero todos quedan a la misma distancia entre sí.
- **Embeddings** Vectores densos de unos cientos de dimensiones, donde los tokens de significado parecido caen cerca. Es lo que usan los modelos modernos.

![En one-hot todas las distancias son iguales; en embeddings la distancia es la información](images/s4-1-1-one-hot-vs-embedding.svg)
<!-- ascii-source:
  ONE-HOT                             EMBEDDING

  cat      [0 1 0 0 0 0 0 ... 0]      cat      [ 0.82 -0.31  0.54 ...]
  dog      [0 0 1 0 0 0 0 ... 0]      dog      [ 0.79 -0.28  0.51 ...]
  heladera [0 0 0 0 0 1 0 ... 0]      heladera [-0.12  0.65 -0.33 ...]

  cat - dog       ->  distancia d     cat - dog       ->  cerca
  cat - heladera  ->  distancia d     cat - heladera  ->  lejos

  Todos los pares estan a la misma    La distancia dice algo, y
  distancia. El espacio no guarda     es lo unico que hay que
  nada sobre el significado.          medir para comparar.

  |V| dimensiones, una por token      unos cientos de dimensiones
-->
<!-- ascii-note:
intent: mostrar por qué one-hot no alcanza y embeddings sí, comparando la misma terna de palabras en los dos espacios: en uno todas las distancias son iguales, en el otro la distancia es la información
emphasize: las dos líneas de distancia de la columna derecha, cerca y lejos, frente a la d repetida de la izquierda; ése es todo el argumento
labels: "ONE-HOT", "EMBEDDING", "cat", "dog", "heladera", "distancia d", "cerca", "lejos", "|V| dimensiones, una por token", "unos cientos de dimensiones"
-->

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 16) — las tres formas de representación y la observación de que en one-hot "cat" y "dog" quedan igual de lejos que "cat" y "refrigerator".

### Speaker notes

El diagrama es la definición de one-hot y su límite en la misma imagen. La terna cat / dog / heladera viene del deck original, que usaba "refrigerator"; se tradujo la tercera para que el contraste se lea sin pasar por el inglés. Lo que hay que dejar dicho es la última línea: one-hot necesita tantas dimensiones como tokens tenga el vocabulario, o sea decenas de miles, y no usa ninguna de ellas para decir algo sobre significado. Los valores de embedding son ilustrativos.

---

## 2. De token a vector

### Content

**Un embedding de texto es un vector que codifica el significado de un token. Cada token del vocabulario tiene el suyo, y ese vector es lo que entra al modelo.**

![De la palabra a su fila de números y de ahí a su punto en el espacio](images/s4-2-1-palabra-fila-punto.svg)
<!-- ascii-source:
   LA PALABRA        SU FILA DE NUMEROS       SU LUGAR EN EL ESPACIO

                                                ^ dim 2
    "hombre"  ---&gt;   [ . . . . . . ]  ---&gt;      |     o--------&gt;o
                                                |   hombre    mujer
    "mujer"   ---&gt;   [ . . . . . . ]  ---&gt;      |
                                                |  o--------&gt;o
    "rey"     ---&gt;   [ . . . . . . ]  ---&gt;      | rey       reina
                                                |
    "reina"   ---&gt;   [ . . . . . . ]  ---&gt;      +---------------&gt; dim 1

   Cada fila tiene tantos numeros como dimensiones tiene el espacio,
   y esos numeros son las coordenadas del punto. La fila y el punto
   son la misma cosa escrita de dos maneras.

   De ahi que una relacion se pueda medir como un trecho: el que va
   de hombre a mujer y el que va de rey a reina tienen el mismo
   largo y la misma direccion.
-->
<!-- ascii-note:
intent: cerrar el circuito palabra -> fila de numeros -> punto, y sobre todo que la fila y el punto son lo mismo: los numeros son las coordenadas; de ahi sale que una relacion se pueda medir como un desplazamiento
emphasize: las dos flechas del panel derecho, paralelas y del mismo largo, que muestran que la misma relacion es el mismo desplazamiento; los puntos de la fila de numeros van deliberadamente sin valores
labels: "LA PALABRA", "SU FILA DE NUMEROS", "SU LUGAR EN EL ESPACIO", "hombre", "mujer", "rey", "reina", "dim 1", "dim 2", "esos numeros son las coordenadas del punto", "el mismo largo y la misma direccion"
-->

- **El circuito completo** Palabra, fila de números, punto en el espacio. Las tres cosas son la misma, escritas de tres maneras.
- **La dimensión no es interpretable de a una.** Ningún eje del espacio significa algo por separado; lo único que se lee es la posición relativa entre puntos.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 16) — "hay que convertir los tokens en números"; el diagrama cierra ese paso.
- `AIG4B-Clase-2-LLM.md.md` (slide 17) — "embedding de texto: vector que codifica el significado de una palabra".
- Diagrama propio. La lámina original traía una figura del deck con los tres bloques encadenados, en inglés y con una matriz de valores ilustrativos; se rehízo como diagrama propio en español, sin los valores, que eran decorado.

### Speaker notes

Recorré el diagrama de izquierda a derecha una vez y volvé al medio: lo que hay que dejar dicho es que la fila de números y el punto son la misma cosa, porque los números *son* las coordenadas. Ése es el paso que cierra la sección y el que más cuesta. Las filas van con puntos suspensivos y sin valores a propósito: la figura del deck original traía una matriz con dos decimales que parecía medida y no salía de ningún modelo. El segundo punto de apoyo evita el malentendido más común de la sección: nadie va a poder decir qué mide la dimensión 3. Las dos flechas del panel derecho anticipan la lámina siguiente, así que señalalas y no las desarrolles acá.

---

## 3. El espacio de embeddings

<!-- design: split-right -->

### Content

**Los tokens de significado parecido caen cerca. Esa cercanía es lo único que el espacio codifica, y es lo que permite comparar dos textos sin compararlos palabra por palabra.**

![Plano cartesiano con cuatro vectores que salen del origen y terminan en emojis: un rey y una reina agrupados arriba, una manzana y una banana agrupadas abajo](images/plano-de-embeddings.png)

- **Los vecindarios son campos de significado.** Realeza en una zona, frutas en otra, sin que nadie haya escrito esas categorías: salen de con qué palabras aparece cada una en el corpus.
- **La cercanía se mide, no se lee.** En dos dimensiones se ve; en las varias centenas reales del espacio, se calcula.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 17) — "palabras relacionadas y con significados similares se encuentran cercanos en el espacio".

### Speaker notes

La figura no tiene una sola palabra escrita: usa emojis en vez de etiquetas, así que se entiende en cualquier idioma y sirve para señalar los dos grupos sin leer nada. Es la más directa de las tres de embeddings. Lo que conviene aclarar es que la proyección a dos ejes es una simplificación útil: el espacio real tiene varias centenas de dimensiones y no se puede dibujar. Si alguien pregunta cuántas, la respuesta honesta es que depende del modelo y que esta clase no fija un número.

---

## 4. Las relaciones también son vectores

<!-- design: split-left -->

### Content

**El espacio no sólo agrupa: también guarda relaciones. El desplazamiento que lleva de "man" a "woman" es el mismo que lleva de "king" a "queen".**

![Tres paneles de ejes tridimensionales con flechas punteadas paralelas: pares de género, pares de tiempo verbal y pares de país y capital](images/analogias-vectoriales.jpg)

- **La regularidad no es un accidente del ejemplo de género.** Se repite con tiempo verbal (walking → walked, swimming → swam) y con país y capital (Italy → Rome, Japan → Tokyo).
- **De ahí sale la aritmética de analogías** que se cita seguido como `rey − hombre + mujer ≈ reina`.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 17) — "el vector que me lleva de man a woman es el mismo que me lleva de king a queen".
- `AIG4B-Clase-2-LLM.md.md` (slide 28) — la formulación aritmética `rey − hombre + mujer ≈ reina`.
- `word2vec-mikolov.web.md` — el abstract reporta rendimiento estado del arte en similitudes sintácticas *y* semánticas; la distinción es de los autores y es la que sostiene los dos tipos de analogía de la figura.

### Speaker notes

Los tres paneles muestran tres relaciones distintas con flechas paralelas, y el argumento es la paralelidad, no los puntos. El panel del medio, tiempo verbal, es la relación sintáctica; los otros dos son semánticos, y esa división es justamente la que el paper de Mikolov usa para evaluar. Advertencia sobre lo que no se puede citar contra el corpus: la aritmética de vectores `rey − hombre + mujer ≈ reina` está en el cuerpo del paper, no en el abstract que tenemos capturado, así que en la lámina aparece como formulación del propio deck. La figura está en inglés.

---

## 5. Word2Vec aprende de la compañía

### Content

**Word2Vec es un método para aprender los vectores de embedding a partir de un corpus, sin que nadie los diseñe a mano. Parte de que una palabra queda definida por las palabras que la rodean.**

- **Qué produce** Un vector por palabra del vocabulario, aprendido de las coocurrencias del corpus. Vectores, no texto.
- **Qué no es** Un modelo de lenguaje. Word2Vec no genera palabras; produce las representaciones que después usa un modelo que sí genera.
- **Qué cuesta** Menos de un día para aprender vectores de calidad sobre un corpus de 1.600 millones de palabras, según el paper original. Esa es la mitad interesante del resultado: gana precisión y baja el costo a la vez.

- 💡 Cada palabra recibe un vector y sólo uno, sin importar la frase en la que aparezca. "Banco" tiene el mismo vector en un río que en una plaza. Resolver eso es lo que motiva las representaciones contextuales y, después, la atención.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 16) — la idea distribucional, la advertencia de que no es un modelo de lenguaje y el mecanismo de promediar los vectores del entorno.
- `word2vec-mikolov.web.md` — Mikolov, Chen, Corrado y Dean, *Efficient Estimation of Word Representations in Vector Space* (arXiv:1301.3781, enero de 2013). Del abstract: dos arquitecturas nuevas, "large improvements in accuracy at much lower computational cost", y menos de un día sobre 1.600 millones de palabras.

### Speaker notes

Tres advertencias sobre el respaldo, todas del registro del corpus, y ninguna va en la lámina. Primera: el deck original decía que Word2Vec fue el primer método que aprende embeddings, y el abstract del paper se compara explícitamente con técnicas neuronales anteriores, así que no reclama ser el primero; acá la lámina dice "un método", no "el primero". Segunda: la frase "una palabra se define por la compañía que tiene" es la hipótesis distribucional de Firth, de 1957, y no aparece en el paper; está parafraseada en el encabezado sin atribuírsela a Mikolov. Tercera: que Word2Vec promedia los vectores de contexto es la mecánica de la arquitectura CBOW, que vive en el cuerpo del paper y no en el abstract capturado, así que no la presentes como algo que el paper afirma en la parte que tenemos. El único número de la lámina, 1.600 millones de palabras en menos de un día, sí está en el abstract y se puede citar de frente.

---

# 5. De las RNN a la atención

**Goal of this section:** Mostrar por qué procesar una frase token por token resuelve el orden y se rompe con la distancia, y qué hace la atención distinto.

---

## 1. Lo que ya vieron sobre redes

### Content

**Todo esto se dio en las clases 3 y 4. Va como repaso de una lámina, porque el resto de la clase se apoya en ello.**

- **La neurona** Una combinación lineal de las entradas más un sesgo, seguida de una no linealidad. Clase 3.
- **La profundidad** Apilar capas es lo que permite representar funciones que una sola capa no puede. Clase 3.
- **El entrenamiento** Calcular el error, ver en qué dirección baja, mover los pesos un paso, repetir. El tamaño del paso es el learning rate. Clases 3 y 4.
- **La retropropagación** El error vuelve por cada conexión, con la regla de la cadena, y a cada peso le toca su parte. Clase 3.

- 💡 Lo único que cambia con texto es qué se le da de comer a esa red, y es el problema del resto de la clase.

### Sources

- `talks/intro-redes-neuronales/final.md` — la neurona, la profundidad, la función de coste y la retropropagación se dictaron en la clase 3.
- `talks/modelado-redes-neuronales/final.md` — el learning rate y la loss se dictaron en la clase 4.

### Speaker notes

Lámina de repaso, no de enseñanza. Recorrela en dos minutos y no te detengas: el grupo ya vio las cuatro cosas con detalle. Sirve para dos cosas. Una, reactivar el vocabulario que el resto de la clase va a usar sin volver a explicarlo. Dos, dejar dicho explícitamente que el aparato de redes no cambia cuando el dato es texto: lo que cambia es la representación de la entrada, y a eso se dedica la clase. Si alguien no cursó las clases 3 y 4, mandalo a esos dos decks, que están enlazados en el README.

### Presenter feedback

- [closed] 2026-09-04 — "Seis láminas de esta sección repetían contenido ya dictado en las clases 3 y 4: el perceptrón, apilar capas, el descenso por gradiente, el learning rate, los cuatro pasos del entrenamiento y la retropropagación."
  Resolution: las seis pasaron a `Cut material` y quedaron reemplazadas por esta lámina de repaso. La única de la sección que era propia de esta clase, sobre la pérdida de orden al promediar, se conservó.

---

## 2. Promediar una frase pierde el orden

### Content

**Un perceptrón necesita un vector de tamaño fijo, y una frase son varios vectores. La forma directa de resolverlo es promediarlos, y esa forma tiene un costo.**

![Dos frases opuestas con las mismas palabras colapsan en el mismo vector al promediar](images/s5-3-1-promedio-pierde-orden.svg)
<!-- ascii-source:
  "el cliente cancelo el pedido"    "el pedido cancelo al cliente"
      |     |       |     |             |     |       |     |
      v     v       v     v             v     v       v     v
    [..]  [..]    [..]  [..]          [..]  [..]    [..]  [..]
       \    |      |    /                \    |      |    /
        \   |      |   /                  \   |      |   /
         +--+------+--+                    +--+------+--+
              |                                  |
              v  PROMEDIO                        v  PROMEDIO
              |                                  |
              v                                  v
     [ 0.41 -0.08  0.22 ...]           [ 0.41 -0.08  0.22 ...]

                     EL MISMO VECTOR

  Las dos frases tienen las mismas palabras y dicen cosas opuestas.
  El promedio no las distingue, porque sumar no depende del orden.
  Para que el orden importe hace falta procesar la frase token por
  token, y ese es el tema de la seccion que sigue.
-->
<!-- ascii-note:
intent: mostrar que promediar es una operación conmutativa y por lo tanto ciega al orden, usando dos frases con las mismas palabras y sentido opuesto que colapsan en el mismo punto
emphasize: la línea "EL MISMO VECTOR" entre las dos salidas idénticas, que es donde se ve el problema; las dos frases de arriba, que son la evidencia
labels: "el cliente cancelo el pedido", "el pedido cancelo al cliente", "PROMEDIO", "EL MISMO VECTOR", "sumar no depende del orden"
-->

- **Ésta es la limitación que arrastra Word2Vec al pasar de palabra a frase.** El método da un vector por palabra; el promedio es una agregación que se aplica encima, no parte del método.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 18) — el bloque "En NLP": cómo se obtiene x₁,…,xₙ de una frase, con la observación de que promediando se pierde la información del orden.

### Speaker notes

Lámina bisagra: cierra las redes neuronales y plantea el problema que resuelve la atención. El ejemplo de las dos frases con las mismas palabras y sentido opuesto es agregado; el deck original decía "se pierde información del orden" y no lo mostraba. Con esta audiencia funciona directo, porque conmutatividad es una propiedad que ya conocen y acá tiene consecuencia semántica. Si alguien pregunta si no alcanza con ponderar el promedio, la respuesta corta es que ninguna ponderación fija arregla el orden: hace falta que el cálculo dependa de la posición, y eso es lo que hacen las redes recurrentes primero y la atención después.

---

## 3. Una red sin memoria

### Content

**Una red común procesa cada entrada de forma independiente: dado el mismo vector, produce siempre la misma salida. Una red recurrente recibe además el estado que dejó el paso anterior, y con eso arrastra lo que ya procesó.**

![La red recurrente recibe en el paso 2 la palabra y el estado h1; la directa solo la palabra](images/s6-1-1-directa-vs-recurrente.svg)
<!-- ascii-source:
  RED DIRECTA                          RED RECURRENTE

  paso 1  "The"                        paso 1  "The"
            |                                    |
            v                                    v
        +-------+                            +-------+
        |  red  |                            |  red  |---.
        +-------+                            +-------+   | h1
            |                                    |       |
            v                                    v       |
        salida A                             salida A    |
                                                         |
  paso 2  "cat"                        paso 2  "cat"     |
            |                                    |   .---'
            |                                    |   |
            v                                    v   v
        +-------+                            +-----------+
        |  red  |                            |    red    |
        +-------+                            +-----------+
            |                                      |
            v                                      v
        salida B                               salida C

  En cada paso entra solo la          En el paso 2 entran dos cosas:
  palabra. La salida de "cat"         la palabra Y el estado h1. La
  es la misma aparezca donde          salida de "cat" cambia segun
  aparezca en la frase.               que palabra vino antes.
-->
<!-- ascii-note:
intent: mostrar la diferencia entre las dos arquitecturas por lo que entra en cada paso, no por la forma del dibujo: a la derecha el paso 2 recibe dos entradas y a la izquierda una sola, y de ahi sale que una tenga memoria y la otra no
emphasize: la conexion que baja desde la salida del paso 1 hasta la entrada del paso 2 en la columna derecha, rotulada h1, y la caja mas ancha del paso 2 que la recibe; es la unica diferencia entre las dos columnas
labels: "RED DIRECTA", "RED RECURRENTE", "paso 1", "paso 2", "The", "cat", "red", "h1", "salida A", "salida B", "salida C", "En cada paso entra solo la palabra", "En el paso 2 entran dos cosas: la palabra Y el estado h1"
-->

- **El caso concreto** Al procesar `"The cat is on the _"`, una red común da siempre la misma salida para `"cat"`, venga de donde venga. Una recurrente guarda lo que produjo con `"The"` y lo usa para procesar `"cat"`.
- **Lo único que cambia es una conexión.** Las dos columnas tienen los mismos pasos, la misma red y las mismas palabras. La diferencia está en que a la derecha el paso 2 recibe también el estado del paso 1, y eso alcanza para que haya memoria.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 26) — el contraste entre red común y RNN sobre la frase "The cat is on the _", verbatim.
- `AIG4B-Clase-2-LLM.md.md` (slide 25) — "las RNN procesan texto palabra por palabra, de izquierda a derecha, manteniendo un estado interno".
- Diagrama propio. La lámina original traía una figura del deck con dos paneles idénticos salvo los bucles, en inglés y con marca de agua de un tercero; se rehízo como diagrama propio para mostrar qué entra en cada paso, que es lo que la figura no dejaba ver.

### Speaker notes

Recorré las dos columnas en paralelo, paso por paso, y detenete en el paso 2: a la izquierda entra una flecha, a la derecha entran dos. Ésa es la definición operativa de la recurrencia y es todo lo que hay que retener de la lámina. El detalle que vale señalar es que el paso 1 da la misma salida en las dos columnas, porque todavía no hay estado anterior que traer; la diferencia aparece recién en el segundo. La figura del deck original mostraba los bucles pero no lo que entra en cada paso, así que el argumento quedaba en el dibujo y no en la mecánica. Anunciá la lámina siguiente: acá se ve un paso; ahora vamos a ver la frase entera.

---

## 4. La red desenrollada en el tiempo

### Content

**Desenrollar la red es dibujar una copia por cada token de la frase. Las copias comparten los mismos pesos, y lo único que viaja de una a la otra es el estado.**

![La misma caja de pesos W reusada cinco veces, con el estado h como único canal entre pasos](images/s6-2-1-red-desenrollada.svg)
<!-- ascii-source:
  La misma red, aplicada una vez por token. Los pesos W no cambian
  entre pasos. Lo unico que viaja hacia adelante es el estado h.

      "The"        "cat"        "is"         "on"        "the"
        |            |            |            |            |
        v            v            v            v            v
     +-----+  h1  +-----+  h2  +-----+  h3  +-----+  h4  +-----+
  h0-|  W  |-----&gt;|  W  |-----&gt;|  W  |-----&gt;|  W  |-----&gt;|  W  |--&gt; h5
     +-----+      +-----+      +-----+      +-----+      +-----+
        |            |            |            |            |
        v            v            v            v            v
      salida       salida       salida       salida     prediccion
                                                         de "_"

  Los pesos son los mismos cinco veces: entrenar una RNN es
  entrenar una sola caja W que se reusa en cada posicion. Por eso
  la frase puede tener cualquier largo sin cambiar el modelo.
-->
<!-- ascii-note:
intent: mostrar que la recurrencia es una sola red reusada, no una red por posición: los pesos W se repiten idénticos y el estado h es el único canal entre pasos; de ahí sale que la frase pueda tener cualquier largo
emphasize: la cadena horizontal de estados h0 a h5, que es lo único que se mueve entre cajas; la repetición de la etiqueta W idéntica en las cinco cajas
labels: "The / cat / is / on / the", "W", "h0", "h1", "h2", "h3", "h4", "h5", "prediccion de _", "Los pesos son los mismos cinco veces"
-->

- **Un solo juego de pesos, cualquier largo de frase.** Es lo que permite entrenar con frases de cinco palabras y aplicar el modelo a una de cincuenta.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 25) — la traza "El → actualiza estado → gato → actualiza estado → está → …".
- `AIG4B-Clase-2-LLM.md.md` (slide 26) — la frase de trabajo `"The cat is on the _"` y el procedimiento de guardar el vector anterior para generar la salida siguiente.

### Speaker notes

Lámina nueva, y de las que más falta hacían: el deck original describía la recurrencia en palabras y nunca la desenrollaba. Lo que hay que señalar es que las cinco cajas dicen la misma W, o sea que es una sola red aplicada cinco veces, y que la flecha horizontal es lo único que las conecta. De ahí salen dos cosas que la sección necesita: que el modelo no depende del largo de la frase, y que todo lo que el paso 5 sabe del paso 1 tiene que haber sobrevivido cuatro reescrituras del estado. Esa segunda idea es la lámina siguiente.

---

## 5. Todo el pasado en un vector

### Content

**El estado tiene un tamaño fijo y no crece con la frase. Cuanto más larga la entrada, más comprimido queda cada token, y el primero que entró es el primero que se diluye.**

![El mismo vector de tamaño fijo tiene que contener tres palabras o diez](images/s6-3-1-cuello-botella-estado.svg)
<!-- ascii-source:
  UNA FRASE CORTA                   UNA FRASE LARGA

  el pago fallo                     el pago de marzo fallo por un
                                    timeout del banco

      |    |    |                    |  |  |  |  |  |  |  |  |  |
      v    v    v                    v  v  v  v  v  v  v  v  v  v
  +-----------------+               +-----------------+
  |  h  tamano fijo |               |  h  tamano fijo |
  +-----------------+               +-----------------+

  Tres palabras, un vector.         Diez palabras, un vector del
                                    mismo tamano exacto.

  El estado no crece con la frase. Lo que el modelo sabe del token
  1 cuando llega al token 10 tuvo que sobrevivir nueve reescrituras
  del mismo vector. Esa compresion es el cuello de botella, y es
  independiente de que la red este bien o mal entrenada.
-->
<!-- ascii-note:
intent: mostrar que el cuello de botella no es un defecto de entrenamiento sino una propiedad de la arquitectura: el mismo recipiente de tamaño fijo tiene que contener tres palabras o diez, y la compresión crece con el largo
emphasize: las dos cajas de estado, idénticas en tamaño bajo entradas de largo muy distinto; el pie que explica que la compresión es estructural
labels: "UNA FRASE CORTA", "UNA FRASE LARGA", "h tamano fijo", "Tres palabras, un vector", "Diez palabras, un vector del mismo tamano exacto", "Esa compresion es el cuello de botella"
-->

- **El cuello de botella está en la arquitectura, no en el entrenamiento.** El modelo encoder-decoder de Cho y otros (2014) lo describe de frente: una RNN codifica la secuencia entera en una representación vectorial de longitud fija, y la otra la decodifica.

### Sources

- `gru-cho-seq2seq.web.md` — Cho, van Merriënboer, Gulcehre, Bahdanau, Bougares, Schwenk y Bengio, *Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation* (arXiv:1406.1078, junio de 2014; EMNLP 2014). El abstract describe la representación de longitud fija como propiedad del diseño.
- `AIG4B-Clase-2-LLM.md.md` (slide 25) — "dificultad con dependencias largas: la información se diluye con la distancia".

### Speaker notes

Lámina nueva. El dato que le da peso es que el vector de longitud fija está declarado en el abstract del paper de Cho, no es una crítica posterior: el paper lo presenta como propiedad de diseño y la crítica llegó después, con el trabajo de atención de Bahdanau, que es coautor de este mismo paper y no está en nuestro corpus. Si alguien pregunta de qué tamaño es el estado, decí que es una decisión de diseño del modelo y no fijes un número, porque no lo tenemos sostenido en ninguna fuente. El diagrama no lo fija a propósito.

---

## 6. LSTM, GRU y ELMo

### Content

**Tres trabajos que empujaron la línea recurrente antes de que la atención la reemplazara.**

- **LSTM** Una celda recurrente con compuertas que deciden qué guardar y qué descartar del estado en cada paso. Ataca la dilución que muestra la lámina anterior.
- **GRU** La celda con compuertas que introduce el trabajo de Cho y otros (2014), dentro del modelo encoder-decoder. Se usa como alternativa más chica a la LSTM.
- **ELMo** Representaciones de palabra profundamente contextualizadas: el vector de una palabra cambia según la oración en la que aparece. Sale de las capas internas de un modelo de lenguaje bidireccional preentrenado, y su paper nombra la polisemia como el problema que viene a resolver.

- 💡 ELMo es lo que arregla el límite de Word2Vec: ahí "banco" tiene un solo vector; con representaciones contextuales tiene uno por contexto.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 25) — las tres variantes tal como el deck las nombra.
- `gru-cho-seq2seq.web.md` — Cho y otros, arXiv:1406.1078, EMNLP 2014: RNN Encoder-Decoder, dos redes recurrentes entrenadas en conjunto.
- `elmo-embeddings-contextuales.web.md` — Peters, Neumann, Iyyer, Gardner, Clark, Lee y Zettlemoyer, *Deep contextualized word representations* (arXiv:1802.05365, febrero de 2018; NAACL 2018). Del abstract: las representaciones modelan el uso de la palabra y cómo ese uso varía con el contexto lingüístico, salen de los estados internos de un biLM preentrenado, y mejoran el estado del arte en seis problemas de NLP.

### Speaker notes

Tres advertencias del registro del corpus, y ninguna cambia lo que dice la lámina, pero conviene tenerlas si preguntan. Primera: LSTM no tiene captura en nuestro corpus, así que la descripción de las compuertas es del deck original y de conocimiento general, no de una fuente que podamos mostrar. Segunda: el abstract del paper de Cho no menciona la sigla GRU, ni la palabra "gated", ni compara con LSTM; la atribución es correcta y estándar, pero la celda se define en el cuerpo del paper, así que la lámina dice "que introduce el trabajo" y no "que el paper llama GRU". El deck original la calificaba de "simplificada", que es consenso posterior y no una afirmación del paper; se retiró. Tercera: el abstract de ELMo no menciona RNN ni LSTM en ninguna forma, así que la lámina no lo presenta como variante de RNN, aunque su modelo bidireccional efectivamente esté construido con LSTM. De las seis tareas que ELMo mejora, el abstract sólo nombra tres: question answering, textual entailment y análisis de sentimiento. Ninguna de las tres capturas trae un número de benchmark.

---

## 7. Cuando "it" queda lejos

### Content

**En `"The animal didn't cross the street because it was too tired"`, resolver a qué se refiere `it` obliga a llegar hasta `animal`. Con recurrencia esa información recorre seis estados intermedios; con atención, uno solo.**

![Seis estados intermedios con recurrencia frente a un solo salto con atención](images/s6-5-1-atencion-un-salto.svg)
<!-- ascii-source:
  "The animal didn't cross the street because it was too tired"
   Para resolver "it" hay que llegar hasta "animal".

        CON RECURRENCIA                    CON ATENCION

           animal                            animal
             |                                 |
             v                                 |
           didn't                              |
             |                                 |
             v                                 |
           cross                               |
             |                                 |
             v                                 |    un solo
            the                                |    salto
             |                                 |
             v                                 |
          street                               |
             |                                 |
             v                                 |
          because                              |
             |                                 |
             v                                 v
             it                                it

  Seis estados intermedios y una             "it" consulta a
  reescritura del vector en cada             "animal" directo,
  paso. Lo de "animal" que llega             sin importar cuantas
  a "it" es lo que sobrevivio.               palabras hay en medio.
-->
<!-- ascii-note:
intent: comparar los dos recorridos posibles entre las mismas dos palabras de la misma frase, alineados en altura para que la diferencia se lea como distancia recorrida
emphasize: la columna derecha, la línea única y continua de "animal" a "it" con la etiqueta "un solo salto"; ése es el mecanismo que la sección viene a presentar
labels: "The animal didn't cross the street because it was too tired", "CON RECURRENCIA", "CON ATENCION", "animal", "it", "un solo salto", "Seis estados intermedios", "sin importar cuantas palabras hay en medio"
-->

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 25) — la frase, la pregunta sobre a qué se refiere "it" y "para cuando la RNN llega a it, la info sobre animal se debilitó".
- `AIG4B-Clase-2-LLM.md.md` (slide 27) — la misma frase reutilizada como intuición positiva de la atención.

### Speaker notes

El deck original usa esta frase dos veces, primero como problema de las RNN y después como intuición de la atención. Acá está una sola vez, con los dos recorridos al lado, que es lo que hace que se entienda de una. Contá los pasos en voz alta: seis estados de "animal" a "it", con una reescritura del vector en cada uno. El conteo sale de la frase: animal, didn't, cross, the, street, because, it. Lo que hay que señalar es la columna de la derecha, no la de la izquierda: el argumento de la lámina es el salto único, y la cadena está para dar la medida de lo que se ahorra.

---

## 8. Cada token mira a todos

### Content

**La atención le da a cada token un peso contra todos los demás tokens de la secuencia, y con esos pesos arma su propia lectura de la frase.**

![El token it consulta a toda la frase y reescribe su representación con el peso sobre animal](images/s6-6-1-cada-token-mira-todos.svg)
<!-- ascii-source:
  "it" le pregunta a cada token de la frase cuanto le importa, y
  arma su nueva representacion con las respuestas.

     The     animal    didn't   cross    the    street   because
      |         |        |        |       |        |        |
      v         v        v        v       v        v        v
    bajo       ALTO     bajo     bajo    bajo    medio     bajo
      \         |        |        |       |        |        /
       \        |        |        |       |        |       /
        +-------+--------+--------+-------+--------+------+
                              |
                              v
                  "it" reescrito con el peso
                  puesto sobre "animal"

  Los pesos son una distribucion: suman uno y salen de comparar el
  vector de "it" contra el de cada token. Esa fila se calcula para
  cada token de la frase, y todas juntas, en una multiplicacion de
  matrices. Ahi esta la paralelizacion: no hay orden que respetar.
-->
<!-- ascii-note:
intent: mostrar la atención como una distribución de pesos que un token calcula contra la frase entera, y de ahí derivar la paralelización: si no hay dependencia secuencial, todas las filas se calculan a la vez
emphasize: la etiqueta ALTO sobre "animal", que es el peso que resuelve el pronombre y lo que hay que mirar; la convergencia de las siete ramas en la nueva representación
labels: "The / animal / didn't / cross / the / street / because", "bajo", "ALTO", "medio", "it reescrito con el peso puesto sobre animal", "Los pesos son una distribucion: suman uno", "no hay orden que respetar"
-->

- **Qué captura** Dependencias largas entre palabras separadas, relaciones sintácticas de sujeto, verbo y objeto, y relaciones semánticas de contexto.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 27) — "atención permite que cada token mire a todos los demás y decida cuáles son relevantes", la intuición de la lectura selectiva y las tres cosas que captura.

### Speaker notes

Ésta es la lámina más importante de la clase y el deck original la resolvía con tres viñetas dentro de una lámina que ya tenía otras cuatro cosas. Los pesos del diagrama son cualitativos a propósito: bajo, medio y alto, sin números, porque cualquier número que pusiéramos sería inventado y se leería como medido. Lo que hay que decir es que la fila suma uno, que es lo que la vuelve una distribución, y que la misma fila se calcula para cada token. De ahí sale la paralelización, que es la propiedad que hizo posible entrenar modelos grandes, y es el tema de la lámina siguiente.

---

## 9. Qué se gana al soltar la recurrencia

### Content

**El Transformer prescinde por completo de recurrencia y de convoluciones, y se apoya sólo en mecanismos de atención. El resultado del paper original es doble: mejor calidad y menos tiempo de entrenamiento a la vez.**

- **Paralelización** Sin dependencia secuencial, la secuencia entera se procesa de una. Es la consecuencia directa de sacar la recurrencia, y lo que permite aprovechar una GPU de punta a punta.
- **Calidad medida** 28,4 BLEU en la tarea de traducción inglés a alemán de WMT 2014, más de 2 puntos BLEU por encima de los mejores resultados previos, incluidos los ensambles. Y 41,8 BLEU en inglés a francés, estado del arte para modelo único.
- **Costo medido** Ese resultado de inglés a francés salió de 3,5 días de entrenamiento sobre ocho GPU, que los autores describen como una fracción pequeña del costo de los mejores modelos de la literatura.

- 💡 La arquitectura no quedó atada a la traducción: el mismo paper la aplica a análisis sintáctico de constituyentes en inglés, con datos abundantes y con datos limitados.

### Sources

- `attention-is-all-you-need.web.md` — Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser y Polosukhin, *Attention Is All You Need* (arXiv:1706.03762, enviado el 12 de junio de 2017). Del abstract: "based solely on attention mechanisms, dispensing with recurrence and convolutions entirely"; 28.4 BLEU en WMT 2014 EN→DE, mejorando los mejores resultados existentes, incluidos ensembles, por más de 2 BLEU; 41.8 BLEU en WMT 2014 EN→FR, nuevo estado del arte para modelo único, tras 3,5 días sobre ocho GPU; generalización a English constituency parsing.

### Speaker notes

Lámina nueva, y la única de la clase con números medidos de una fuente primaria. Dos cuidados al decirlos. Primero: la mejora es de más de 2 **puntos** BLEU, no de un 2 %; BLEU es una escala de 0 a 100 y confundir puntos con porcentaje es el error clásico. Segundo: el abstract no dice qué GPU eran ni cuánto costaron en dinero, así que "3,5 días sobre ocho GPU" es todo lo que se puede afirmar. Lo que no está en nuestro corpus, porque la captura es la página de abstract y no el paper: self-attention, multi-head attention, positional encoding, scaled dot-product y layer normalization. Si alguien pregunta por el detalle interno, la respuesta es que está en el paper y que esta clase se queda en el mecanismo de la lámina anterior.

---

# 6. Transformers y LLM

**Goal of this section:** Cerrar el recorrido mostrando la arquitectura completa y el ciclo que corre cada vez que un modelo escribe una palabra, y que ese ciclo es el problema del modelado de lenguaje a otra escala.

---

## 1. La arquitectura de 2017

<!-- design: split-left -->

### Content

**El Transformer es la arquitectura que reemplazó a las RNN en 2017. Procesa la secuencia entera de una vez, en paralelo, apilando bloques de atención.**

![Diagrama de arquitectura en dos columnas: la izquierda con embedding de entrada, codificación posicional, atención multi-cabeza y feed forward; la derecha con atención enmascarada y atención cruzada, terminando en una capa lineal y un softmax hacia probabilidades de salida](images/arquitectura-transformer.jpg)

- **Dos columnas, dos trabajos.** La izquierda codifica la entrada; la derecha genera la salida token a token y consulta a la izquierda por el camino.
- **El softmax de arriba es la distribución sobre el vocabulario.** El "Output Probabilities" del tope de la figura es literalmente ese vector de tamaño |V| con el que se formuló el modelado de lenguaje.

- Figura 1 de Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser y Polosukhin, *Attention Is All You Need*, arXiv:1706.03762 (2017).

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 27) — "la arquitectura que cambió todo (2017); a diferencia de las RNN, los Transformers procesan toda la secuencia de una vez, en paralelo" y la afirmación sobre encoder más decoder.
- `attention-is-all-you-need.web.md` — el abstract enmarca el Transformer dentro del paradigma encoder-decoder para transducción de secuencias. La figura reproducida en la lámina es la figura 1 del paper, y la atribución va al pie del contenido visible.

### Speaker notes

La figura es la figura 1 del paper de Vaswani y otros, y el deck original la reproducía sin atribución; acá el crédito está al pie de la lámina, a la vista, además de en las fuentes. Es la figura más reconocible del campo y proyectarla sin crédito es evitable. Está en inglés y es densa: no la recorras entera. Señalá tres cosas y seguí: las dos columnas, la caja de atención multi-cabeza que se repite, y el softmax de arriba, que es donde el recorrido se cierra sobre el modelado de lenguaje. El deck original agregaba que los LLM modernos usan solo decoder, o sea sólo la columna derecha. Es cierto y es consenso, pero no sale del paper de 2017 ni de ninguna fuente de nuestro corpus, así que decilo de palabra y como afirmación propia, no como algo que el paper diga. Está anotado en las preguntas abiertas.

---

## 2. Tres generaciones de representación

### Content

**El recorrido de la clase, en una tabla: representaciones estáticas, después secuenciales, después contextuales con atención.**

| | Idea principal | Lo que aportó | Lo que no resuelve |
|---|---|---|---|
| **Word2Vec** | Aprende embeddings del contexto en el que aparecen las palabras | Representaciones semánticas aprendidas sin supervisión; las palabras parecidas quedan cerca | Un solo vector por palabra, sin importar el contexto. No modela el orden ni las secuencias |
| **RNN (LSTM, GRU)** | Procesan el texto secuencialmente con un estado interno que hace de memoria | Modelan secuencias y dependencias temporales; habilitaron traducción y generación | Procesamiento secuencial, no paralelizable. Pierden información en secuencias largas |
| **Transformers** | Atención para que cada token mire a todos los demás, en paralelo | Dependencias largas sin degradación y entrenamiento paralelo. Base de todos los LLM actuales | Enormes cantidades de datos y cómputo. La atención crece cuadráticamente con la longitud |

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 28) — la tabla comparativa completa y el cierre "evolución: representaciones estáticas → secuenciales → contextuales con attention".

### Speaker notes

Lámina de repaso, y la única que conviene leer entera, porque cada fila es una sección de la clase. La lectura útil es en columna: la columna de la derecha es la cadena de motivaciones, porque cada limitación es lo que el renglón siguiente vino a arreglar. La tabla del deck original tenía cinco columnas, con "Novedad" y "Pros" diciendo casi lo mismo; quedaron fusionadas en una. Si preguntan por lo cuadrático de la última fila, es que cada token calcula un peso contra cada otro token, o sea n² pares.

---

## 3. El ciclo de un LLM, token a token

### Content

**Cada palabra que aparece en pantalla es una vuelta entera de este ciclo. El modelo escribe un token, se vuelve a leer completo y escribe el siguiente.**

![El ciclo de generación de un LLM, que se realimenta con su propio token de salida](images/s7-3-1-ciclo-llm-token.svg)
<!-- ascii-source:
  texto de entrada:  "¿Como estas?"
        |
        v
   [ TOKENIZAR ]    ["¿"]["Como"]["est"]["as"]["?"]
        |
        v
   [ EMBEDDER ]     un vector por token
        |
        v
   [ TRANSFORMER ]  capas de atencion sobre la secuencia entera
        |
        v
   [ DISTRIBUCION ] un valor por cada token del vocabulario, |V|
        |
        v
   [ ELEGIR ]       se toma uno; la temperatura decide cuanto se
        |           aparta del mas probable
        v
     "Bien"  ---&gt; se agrega al final del texto y vuelve a empezar
        |                                                       |
        +-------------------------------------------------------+

  El modelo no escribe una respuesta de una: escribe un token, se
  relee entero con ese token adentro, y vuelve a decidir. Lo que
  se ve como una frase que aparece de a poco son N vueltas.
-->
<!-- ascii-note:
intent: mostrar que la generación es un bucle que se realimenta con su propia salida, y que el costo de una respuesta es lineal en la cantidad de tokens que produce
emphasize: la flecha de retorno desde el token producido hasta el comienzo del ciclo, que es lo que convierte cinco cajas en un bucle; el paso de la distribución sobre el vocabulario
labels: "texto de entrada", "TOKENIZAR", "EMBEDDER", "TRANSFORMER", "DISTRIBUCION", "ELEGIR", "temperatura", "se agrega al final del texto y vuelve a empezar", "N vueltas"
-->

- **Temperatura** El parámetro que decide cuánta aleatoriedad hay en el paso de elegir. Con temperatura cero, siempre el token más probable.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 29) — los seis pasos del ciclo, el ejemplo de tokenización `"¿Cómo estás?"` → `["¿","Cómo","est","ás","?"]`, la definición de temperatura y "los modelos generan texto token por token".

### Speaker notes

El diagrama convierte una tabla de seis celdas en un bucle, que es lo que la tabla del deck original no dejaba ver. Lo que hay que señalar es la flecha de retorno: es la que explica por qué una respuesta larga tarda más que una corta de forma proporcional, y por qué el costo se cobra por token. El ejemplo de tokenización en español es bueno y vale detenerse: "estás" se parte en dos sub-palabras y los dos signos de interrogación son tokens propios, o sea que una frase de dos palabras da cinco tokens. Eso conecta directo con la tokenización por sub-palabras.

---

## 4. El mismo problema, a otra escala

### Content

**Es la misma formulación de modelado de lenguaje, con los mismos tres ingredientes y otro orden de magnitud.**

| | El ejemplo de juguete | Un LLM de hoy |
|---|---|---|
| **Vocabulario V** | 14 tokens | del orden de 100.000 tokens, sub-palabras de varios idiomas |
| **Corpus T** | 5 frases | texto de internet, libros, código y papers |
| **Parámetros** | pocos | del orden de cientos de miles de millones |
| **Entrenamiento** | segundos | meses sobre miles de GPU |
| **Frase P** | `"the dog sat on"` | cualquier texto, de cualquier largo |

- **El concepto no cambia:** predecir el token siguiente. Lo que cambia es el tamaño del vocabulario, la cantidad de datos y la del modelo.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 30) — la tabla comparativa completa y los dos cierres.
- Verificación: el vocabulario de 14 tokens y las 5 frases coinciden con el ejemplo trabajado de la sección *Modelado de lenguaje*, donde están enumerados uno por uno.

### Speaker notes

Tres cuidados con los números de la columna derecha, y los tres importan porque son las cifras que un alumno se lleva anotadas. El primero: el deck original decía "billones de palabras" para el corpus, que en español rioplatense son 10¹² y en el original en inglés casi con seguridad eran 10⁹; como no hay forma de saber cuál era la intención, la cifra se retiró y quedó la descripción cualitativa. El segundo: los cientos de miles de millones de parámetros y los ~100.000 tokens de vocabulario salen del deck original y no de una fuente pública, porque ni OpenAI ni Anthropic publican esos números para sus modelos actuales; están con "del orden de" y anotados en las preguntas abiertas. El tercero: la fila de vocabulario del deck original mezclaba unidades, "14 palabras" contra "100.000 tokens"; acá las dos dicen tokens, que es la unidad que la clase estableció al tokenizar.

---

## 5. Casi cualquier tarea es generación

### Content

**Un modelo que comprende texto y genera palabras permite reescribir casi cualquier tarea de NLP como una instrucción en texto.**

- **Sentimiento** `"¿Este comentario es positivo o negativo?"` → el modelo genera `"positivo"`.
- **Traducción** `"Traducí: the cat is on the mat"` → el modelo genera `"el gato está sobre la alfombra"`.
- **Resumen** `"Resumí este texto: […]"` → el modelo genera el resumen.

- **La cadena completa:** problema → prompt (instrucción en texto) → el modelo genera la solución.

- 💡 Con el enfoque tradicional, esas tres tareas necesitaban tres conjuntos etiquetados y tres modelos entrenados por separado. Acá son tres frases contra el mismo modelo.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 31) — los tres ejemplos de reformulación, la cadena problema → prompt → solución y "muchas tareas se resuelven ahora con una sola técnica: generación de texto con modelos fundacionales".

### Speaker notes

Ésta es la lámina donde la clase se cierra sobre sí misma, y el callout final es el remate: volvé a la 2.4, la de las tres columnas independientes, y contrastá. Ahí estaba el costo de etiquetar tres veces; acá son tres frases. Si alguien pregunta si entonces el entrenamiento etiquetado desapareció, la respuesta corta es que no, que se mudó al ajuste de instrucciones y a la alineación, y que eso es materia de otra clase. Esta lámina también es la que engancha con la clase de prompting.

---

## 6. Entrenamiento e inferencia

### Content

**Dos fases distintas, con costos, responsables y momentos distintos. Confundirlas es el malentendido más común sobre estos modelos.**

| | Entrenamiento | Inferencia |
|---|---|---|
| **Qué pasa** | Aprende ajustando parámetros | Usa parámetros ya aprendidos |
| **Cuándo** | Antes de que el modelo esté disponible | Cada vez que alguien pregunta |
| **Quién** | OpenAI, Anthropic, Meta y unos pocos más | Cualquiera que use el modelo |
| **Costo** | Millones de dólares, semanas | Fracción de segundo por respuesta |
| **Parámetros** | Se modifican constantemente | Están congelados |

- **Una conversación no entrena al modelo.** Los parámetros ya están fijos; lo que ocurre en el chat es inferencia.
- **Por eso son pocas las organizaciones que entrenan.** Entrenar un modelo grande pide un corpus de escala web y miles de GPU durante semanas.

### Sources

- `AIG4B-Clase-2-LLM.md.md` (slide 32) — la tabla completa y los dos cierres, verbatim.

### Speaker notes

Última lámina de contenido y la más aplicable de la sección. El primer punto de abajo es el que hay que decir despacio, porque es el malentendido más frecuente que va a aparecer fuera de la clase: la conversación no entrena nada. El deck original decía "billones de palabras" también acá; se retiró por la misma ambigüedad de la tabla de escala y quedó "escala web". La fila de "Ejemplo" del deck original (entrenar GPT-4 contra preguntarle qué es NLP) se retiró porque repetía lo que ya dicen las filas de qué pasa y cuándo.

---

# Conclusions

## 7. Lo que queda de la clase

### Content

- **Un modelo de lenguaje hace una sola cosa.** Predice el token siguiente y devuelve una distribución sobre el vocabulario entero. Todo lo demás de la clase, tokens, embeddings, capas y atención, existe para que esa predicción use el contexto.
- **La etiqueta gratis es lo que cambió la escala.** Mientras cada tarea necesitaba su propio conjunto etiquetado a mano, el costo crecía tarea por tarea. El texto crudo trae la respuesta correcta adentro, y eso convirtió a internet en conjunto de entrenamiento.
- **El cuello de botella de las RNN era estructural.** Comprimir la frase entera en un vector de tamaño fijo diluye lo primero que entró, y ningún entrenamiento arregla eso. La atención lo elimina dejando que cada token consulte a todos los demás en un solo paso.
- **Un LLM de hoy es el ejemplo de catorce tokens con otro tamaño.** Cambian el vocabulario, los datos y la cantidad de parámetros. La cuenta es la misma.
- **Verificá las cifras antes de repetirlas.** Este mismo deck citaba tres papers sin nombrarlos y usaba "billones" en un sentido ambiguo entre 10⁹ y 10¹². Pasa en el material de todos, incluido el nuestro.

### Sources

- `AIG4B-Clase-2-LLM.md.md` — el deck original no tiene lámina de cierre.
- `attention-is-all-you-need.web.md`, `word2vec-mikolov.web.md`, `gru-cho-seq2seq.web.md`, `elmo-embeddings-contextuales.web.md` — las cuatro fuentes primarias que respaldan el recorrido.

### Speaker notes

Cinco frases y ninguna es un resumen de la agenda. La primera es la tesis desplegada. La segunda es la que más se recuerda, porque explica el salto de escala con un argumento económico y no con uno técnico. La tercera es el nudo de la clase y conviene decirla mirando el diagrama del cuello de botella. La quinta es la que menos se espera de una clase: contá que al revisar este mismo material encontramos tres papers citados sin nombre y una unidad ambigua, y que se corrigieron. Si te queda tiempo, cerrá con la pregunta que abre la clase siguiente: si el modelo sólo predice el token siguiente, de dónde sale que parezca que razona.

---

# Open questions

**Cifras que quedaron sin respaldo verificable**

- **El vocabulario de ~100.000 tokens y los cientos de miles de millones de parámetros (sección 7, escala del vocabulario)** — Vienen del deck original. Ni OpenAI ni Anthropic publican esos números para sus modelos actuales, así que no se pueden verificar contra ninguna fuente. Quedaron en la lámina con "del orden de". Falta decidir si se citan contra un modelo abierto con números publicados o si se retiran.
- **"Billones de palabras" (8.4 y 8.6)** — En español rioplatense un billón es 10¹²; el original casi con seguridad traduce "billions" (10⁹) del inglés. Retirado de las dos láminas y reemplazado por descripción cualitativa. Falta decidir si se pone una cifra con fuente.
- **Los valores de embedding de las láminas 4.2 y 4.3** — Ilustrativos, no salidas de ningún modelo. Los de la figura 17-2 vienen así del deck original. Están declarados como ilustrativos en las notas del orador.
- **Los pesos de atención de la lámina 7.6** — Deliberadamente cualitativos (bajo, medio, alto), sin números, porque cualquier valor concreto sería inventado y se leería como medido.

**Afirmaciones que el corpus no sostiene**

- **"Los LLM modernos usan solo decoder" (sección 7, la arquitectura de 2017)** — El registro de `attention-is-all-you-need.web.md` es explícito: el paper es de 2017 y GPT, LLaMA y Claude son posteriores, así que la afirmación no sale de ahí. Es correcta y es consenso, pero quedó en notas del orador como afirmación propia. Falta capturar una fuente que la sostenga.
- **LSTM sin captura en el corpus (sección 6, LSTM/GRU/ELMo)** — Es la única de las tres variantes sin fuente propia. La descripción de las compuertas sale del deck original. Convendría capturar Hochreiter y Schmidhuber (1997) antes de la próxima edición.
- **La mecánica de Word2Vec (sección 4, Word2Vec)** — Que promedia los vectores del contexto es la arquitectura CBOW, que vive en el cuerpo del paper y no en el abstract capturado. Lo mismo con la aritmética `rey − hombre + mujer ≈ reina` y con los nombres CBOW y skip-gram. Convendría capturar el PDF.
- **La atribución de la GRU a Cho y otros (sección 6, LSTM/GRU/ELMo)** — Correcta y estándar, pero el abstract capturado no menciona la sigla, ni la palabra "gated", ni compara con LSTM. La lámina está redactada para no exceder lo que la captura sostiene.
- **Las cinco capturas de arXiv son páginas de abstract, no papers** — Nada del mecanismo interno de ninguno de los cuatro trabajos está en el corpus: ni self-attention, ni multi-head, ni positional encoding, ni las compuertas de la GRU, ni las capas del biLM de ELMo.

**Decisiones de alcance**

- **Largo de la clase** — La revisión del 2026-09-03 llevó el deck de 32 a 40 láminas, con 20 diagramas ASCII y 6 figuras del deck original conservadas. Para 150 minutos son unos 3,5 minutos por lámina. Falta decidir si alcanza o si hay que recortar la última sección.
- **Cuatro de las seis figuras conservadas están en inglés** — Las excepciones son la de clasificación de imágenes (título en español) y la del plano de embeddings (sin texto, usa emojis). Las cuatro restantes se conservan porque aportan algo que el arte de texto no reproduce: la superficie de pérdida en 3D, la geometría vectorial con valores en los ejes, la densidad de la red multicapa y la figura canónica del Transformer. Se traducen de palabra al presentarlas.
- Ver `research/corpus/AIG4B-Clase-2-LLM.md.md` → *Inconsistencies / open questions* para el resto de los problemas detectados en el material original.
