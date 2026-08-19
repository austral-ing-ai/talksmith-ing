---
source_file: Intro-Redes-Neuronales-105min.pptx
source_type: article
ingested_at: 2026-08-19
---

# Introducción a las Redes Neuronales Artificiales (ANN)

## Provenance
- Original location: research/articles/Intro-Redes-Neuronales-105min.pptx
- Format: pptx (51 diapositivas, 12 MB, 41 imágenes únicas, ninguna tabla como objeto: las "tablas" son cuadros de texto)
- Author / source (if known): Paulo Veiga y Marcos Sanchez Sorondo
- Date of original (if known): Agosto 2026 (campo "Última Modificación" de la portada)
- **Materia de origen distinta a la de este repositorio.** La portada dice "Inteligencia Artificial Generativa Aplicada en Biomedicina"; este repositorio es de Ingeniería de Software. El mazo declara 105 minutos y el perfil del repositorio tiene 90 como default.
- Estructura: 6 capítulos numerados, cierre y anexo. Cada capítulo abre con una diapositiva separadora, y tres de ellos (4, 5 y 6) tienen además una diapositiva de tres preguntas que anticipa el contenido.

## Key claims

**Capítulo 1 — De la intuición a la red (diapositivas 4 a 6)**
- La analogía de arranque: un auto con sensores ("viene algo por la izquierda", "estoy cerca de la pared") conectados por cables a dos actuadores, acelerador y freno, con nodos en el medio que reparten la electricidad. "Eso es, literalmente, una red neuronal". Fuente citada en la propia diapositiva: Mark Riedl, *A Very Gentle Introduction to Large Language Models without the Hype*.
- Aprender es ajustar qué caminos conducen. Los parámetros arrancan azarosos y el auto choca; se prueba, se mide el error, se retocan las compuertas y se vuelve a probar. Después de muchísimas repeticiones ciertos caminos quedan reforzados. **Eso es el entrenamiento: no hay nadie programando reglas, hay un procedimiento incremental que ajusta números.**
- El punto de partida conocido es un modelo lineal: entrada (vector `x` de variables), modelo (combinación lineal con un peso por variable) y error (suma de diferencias al cuadrado entre predicción y objetivo).

**Capítulo 2 — La neurona y la capa (diapositivas 8 a 11)**
- El mundo real no es lineal: la temperatura sube y baja a lo largo del año, la distribución del ingreso cae de forma abrupta y después se aplana. Una recta aproxima el promedio y pierde la forma. "Si queremos mejores predicciones, necesitamos mejores modelos", y mejor acá significa capaz de representar curvas, saturaciones y quiebres.
- **La neurona es primero una combinación lineal:** recibe varias entradas, las multiplica por sus pesos, las suma y agrega un sesgo. `x` es el vector de entradas, `w` los pesos aprendidos y `b` el sesgo, "un desplazamiento que le permite activarse antes o después".
- **La sigmoide es la no linealidad clásica:** aplasta el resultado al intervalo (0, 1) y convierte una suma en algo legible como probabilidad o grado de activación. Cuatro propiedades que el mazo enumera: rango acotado, diferenciable ("es suave en todo punto: sin eso no habría backpropagation"), monótona creciente ("conserva el orden") y punto medio en 0 (`σ(0) = 0.5`, "un umbral natural de decisión").
- **La capa es el bloque que se repite:** combinación lineal seguida de no linealidad. "Es la unidad con la que se construye cualquier red: no hay una pieza más grande que aprender, solo esta repetida." Una capa toma un vector y devuelve otro vector; encadenarlas es pasarle a la siguiente lo que produjo la anterior.

**Capítulo 3 — Redes profundas (diapositivas 13 a 15)**
- Una red profunda mete capas intermedias entre la entrada y la salida. "Se llaman ocultas porque no las observamos directamente: no son ni el dato que entra ni la respuesta que sale."
- **Dos dimensiones describen toda arquitectura.** Ancho: la cantidad de unidades dentro de una capa, y el ancho de la red es el de su capa más grande. Profundidad: la cantidad de capas ocultas, sin contar entrada ni salida.
- **Parámetros contra hiperparámetros**, presentado como "la distinción que más confusión genera":

| Aspecto | Hiperparámetros | Parámetros |
|---|---|---|
| ¿Quién los fija? | Los definimos nosotros, a mano, antes de entrenar | Los aprende la red durante el entrenamiento |
| Ejemplos | Ancho, profundidad, tasa de aprendizaje η, tamaño de lote | Pesos `w` de cada conexión y sesgos `b` de cada unidad |
| ¿Cuándo cambian? | Solo si volvemos a lanzar el entrenamiento | En cada iteración, con cada lote de datos |
| ¿Cuántos hay? | Unos pocos: decenas como mucho | Millones, o miles de millones en modelos grandes |
| ¿Cómo se eligen? | Búsqueda, experiencia previa y validación | Descenso por gradiente sobre el error |

- Remate del capítulo: "Ajustar hiperparámetros es un ciclo externo; entrenar es el ciclo interno que corre dentro de cada configuración."

**Capítulo 4 — El recorrido completo (diapositivas 18 a 22)**
- Se recorre punta a punta con **un caso concreto: predecir el clima**. Ocho variables de entrada (temperatura media, máxima, mínima, humedad, precipitación, presión, nubosidad y visibilidad) y una primera capa oculta de nueve unidades.
- **Los números del ejemplo, que se usan en todo el capítulo:** 8 entradas × 9 unidades ocultas = **72 conexiones**; más un sesgo por unidad oculta = **81 parámetros solo en la primera capa**.
- Los 72 pesos se ordenan en una **matriz de 8 filas por 9 columnas**: cada fila una variable de entrada, cada columna una unidad oculta, y cada celda el peso de esa conexión concreta.
- "Pensar en matrices no es un capricho de notación. Es lo que permite calcular la capa entera con una sola operación y aprovechar la GPU."
- **El cálculo de la capa es un producto matricial:** vector fila de 8 × matriz 8×9 = vector de 9, que es la capa oculta antes de la activación. "Las dimensiones encajan de una única manera posible."
- Tabla de dimensiones del ejemplo: entrada `x` 1×8; pesos `W⁽¹⁾` 8×9; capa oculta `h⁽¹⁾` 1×9; pesos `W⁽ⁿ⁾` 100×4; salida `y` 1×4.
- Regla práctica que cierra el capítulo: "el número de columnas de la izquierda tiene que coincidir con el de filas de la derecha. Si no coincide, la arquitectura está mal planteada."

**Capítulo 5 — Funciones de activación (diapositivas 25 a 28)**
- La pregunta que sostiene el capítulo, citada textual en la diapositiva: "Necesitamos las no linealidades para poder romper la linealidad y representar relaciones más complicadas."
- **Sin no linealidad la red colapsa.** Dos transformaciones lineales encadenadas equivalen a una sola: multiplicar por `W₁` y después por `W₂` es lo mismo que multiplicar por una única `W*`. "Diez capas lineales tienen exactamente el mismo poder expresivo que una." Con no linealidad, "cada capa dobla el espacio a su manera" y encadenarlas permite aproximar prácticamente cualquier función continua: **teorema de aproximación universal**.
- Remate: "La no linealidad no es un detalle de implementación. Es lo único que justifica apilar capas."
- **Las cuatro activaciones comunes**, que comparten tres propiedades que el entrenamiento necesita (monótonas, continuas y diferenciables) y se diferencian en el rango de salida y en el comportamiento de sus derivadas:

| Función | Definición | Rango | Cuándo usarla |
|---|---|---|---|
| Sigmoide | `σ(a) = 1 / (1 + e⁻ᵃ)` | (0, 1) | Salida binaria; interpretable como probabilidad |
| Tanh | `(eᵃ − e⁻ᵃ) / (eᵃ + e⁻ᵃ)` | (−1, 1) | Capas ocultas; centrada en 0, converge más rápido que la sigmoide |
| ReLU | `max(0, a)` | [0, ∞) | El estándar en capas ocultas: barata y evita el gradiente que se desvanece |
| Softmax | `eᵃⁱ / Σⱼ eᵃʲ` | (0, 1) | Capa de salida en clasificación multiclase; las salidas suman 1 |

- "La derivada importa tanto como la función: es la que viaja hacia atrás durante el entrenamiento. Una derivada que se aplana frena el aprendizaje."
- **Softmax convierte puntajes en probabilidades.** Advertencia explícita del mazo: "Ojo con dónde se aplica. Softmax se usa en la activación de la capa final. Si se la aplica en una capa oculta, se pierde información sobre la magnitud de los valores y solo sobrevive su proporción."

**Capítulo 6 — Backpropagation (diapositivas 31 a 36)**
- El entrenamiento es un ciclo de dos movimientos. **Forward:** empujar la entrada a través de la red; al final de cada época se comparan las salidas con los objetivos y se forma el error. **Backward:** propagar ese error hacia atrás y actualizar pesos y sesgos.
- **La función de coste** es la pérdida L2, suma de diferencias al cuadrado entre predicción y objetivo, con tres justificaciones que el mazo desglosa: *al cuadrado* (los errores por exceso y por defecto no se cancelan, y los grandes pesan más), *el medio* (el factor ½ no mueve el mínimo, está para que la derivada quede limpia) y *diferenciable* (es lo que permite calcular el gradiente). `y` es lo que la red predijo y `t` el objetivo; la suma recorre todas las unidades de salida.
- **La regla de la cadena** responde "¿cuánto cambia el error si movemos un peso en particular?". El peso no toca el error directamente: lo hace a través de la suma ponderada, y esta a través de la activación. Tres factores encadenados: cuánto cambia el error si cambia la salida (sale directo de la función de coste, la diferencia entre predicción y objetivo); cuánto cambia la salida si cambia la suma (la derivada de la activación evaluada en ese punto); cuánto cambia la suma si cambia el peso ("es simplemente la entrada que multiplicaba a ese peso").
- **El delta.** Se agrupan los dos primeros factores en un solo término `δ`, "la sensibilidad del error respecto de la suma ponderada de esa unidad". Con δ calculado, el gradiente de cualquier peso que llega a la unidad es una multiplicación.
- **Capa oculta: propagar el delta hacia atrás.** "Una unidad oculta no tiene un objetivo con el cual compararse: nadie le dice cuál era su valor correcto. Su culpa se calcula sumando los deltas de todas las unidades de la capa siguiente a las que alimenta, ponderados por los pesos que las conectan." En la capa de salida δ se calcula directo; en las ocultas se hereda de la capa siguiente; y el mismo cálculo se repite hacia atrás por recursión hasta la primera capa. El mazo lo marca como "el corazón del algoritmo" y de ahí el nombre propagación hacia atrás.
- **El paso de actualización.** Corregir el peso es restarle una fracción del gradiente. La tasa de aprendizaje η controla el tamaño del paso y "es uno de los hiperparámetros más sensibles del entrenamiento". Tres notas: η muy chico (el entrenamiento avanza tan despacio que puede volverse impracticable), η muy grande (los pasos se pasan del mínimo y el error oscila o diverge) y el signo menos (el gradiente apunta hacia donde el error crece, y nos movemos en la dirección opuesta).

**Cierre (diapositivas 37 y 38)**
- Seis ideas que el mazo declara como lo que hay que llevarse: (1) una red es un circuito, sensores, compuertas y actuadores, y aprender es ajustar cuánta señal deja pasar cada compuerta; (2) la capa es el bloque, combinación lineal más no linealidad repetido, "no hay una pieza más grande que entender"; (3) la no linealidad es obligatoria; (4) los pesos viven en matrices, las dimensiones se deducen de la arquitectura; (5) el error se propaga hacia atrás, la regla de la cadena reparte la culpa capa por capa; (6) el aprendizaje es incremental, "adivinar, medir, corregir un poco, repetir. Millones de veces".
- **Próximos pasos declarados:** redes convolucionales ("el mismo esqueleto, adaptado a imágenes: pesos compartidos y detección de patrones locales"), redes generativas (GANs y modelos de difusión) y aplicaciones en biomedicina (datos sintéticos, traducción entre modalidades, segmentación de estructuras clínicas). El mazo dice explícitamente: "La clase 8 retoma exactamente desde acá: las GANs son dos de estas redes compitiendo entre sí, entrenadas con el mismo mecanismo de backpropagation que acabamos de ver."

**Anexo (diapositivas 39 a 51)**
- El propio mazo lo define: "Slides que quedaron fuera del recorrido de 105 minutos. Sirven para responder preguntas en vivo o como material de lectura posterior." Son 13 diapositivas que extienden los mismos seis capítulos:
- *Cada nodo decide cuánta energía deja pasar* (40): sensor, compuerta y actuador como los tres roles del circuito.
- *Deep Learning: el mismo truco, más piezas* (41): "«Deep» no se refiere a la profundidad conceptual, sino a la cantidad de capas apiladas."
- *Del ejemplo mínimo a la red neuronal* (42): una red sin capas ocultas es una combinación lineal, "nada que una regresión no pudiera hacer".
- *¿Qué pasa dentro de las capas ocultas?* (43): "la pregunta incómoda". Las capas ocultas construyen representaciones intermedias; en visión las primeras detectan bordes, las siguientes texturas, las últimas objetos, y nadie se lo indicó.
- *Cómo leer un diagrama de red* (44): círculos son unidades, flechas son transformaciones con pesos, cada columna es una capa.
- *El ciclo de ajuste* (45): elegir configuración, entrenar y medir, volver a probar hasta que el error deja de mejorar.
- *Notación: quién se conecta con quién* (46): "El subíndice no es decorativo. El primer número identifica la unidad de entrada; el segundo, la unidad oculta a la que llega. Así, `w₃₆` es el peso que va de la tercera entrada a la sexta unidad oculta."
- *La capa oculta, completa* (47): las nueve unidades se calculan en paralelo con una única multiplicación de matrices; todas ven las mismas ocho variables y lo que las diferencia es su columna de pesos.
- *Hacia la capa de salida* (48): si la última capa oculta tiene 100 unidades y se quieren 4 salidas, la matriz es 100×4, "cuatrocientos pesos más".
- *La función de activación* (49): la analogía del termostato, la temperatura baja de forma continua pero la decisión de ponerse el abrigo es binaria.
- *La sigmoide y su derivada* (50): la derivada se escribe en términos de la propia sigmoide, "así que no hay que recalcular nada". "Por eso la sigmoide fue la activación por defecto durante años: su derivada sale casi gratis. Su problema aparece en los extremos, donde se aplana y el gradiente se desvanece."
- *Glosario de símbolos* (51): tabla completa de notación, reproducida más abajo.

## Definitions and terminology

| Término | Definición del mazo |
|---|---|
| Red neuronal (intuitiva) | Un circuito de sensores conectados a actuadores, con nodos en el medio que deciden cuánta señal dejan pasar |
| Entrenamiento | Procedimiento incremental que ajusta números hasta que el comportamiento del circuito se parece al que queríamos. No hay reglas programadas |
| Neurona | Recibe entradas, las multiplica por sus pesos, las suma y agrega un sesgo. Ese único número es todo lo que produce la parte lineal |
| Sesgo `b` | Un desplazamiento que le permite a la neurona activarse antes o después |
| Capa | Combinación lineal seguida de una no linealidad. Toma un vector y devuelve otro vector |
| Capa oculta | Capa intermedia. Se llama oculta porque no se observa directamente: no es ni el dato que entra ni la respuesta que sale |
| Ancho | Cantidad de unidades dentro de una capa. El ancho de la red es el de su capa más grande |
| Profundidad | Cantidad de capas ocultas. No cuentan ni la entrada ni la salida |
| Parámetros | Pesos y sesgos. Los aprende la red durante el entrenamiento |
| Hiperparámetros | Ancho, profundidad, tasa de aprendizaje, tamaño de lote. Los fija quien diseña, antes de entrenar |
| Teorema de aproximación universal | Encadenando capas con no linealidad se puede aproximar prácticamente cualquier función continua |
| Forward | Empujar la entrada a través de la red y formar el error contra los objetivos |
| Backward | Propagar ese error hacia atrás y actualizar pesos y sesgos |
| Delta `δ` | La sensibilidad del error respecto de la suma ponderada de esa unidad |
| Tasa de aprendizaje `η` | El tamaño del paso con el que se corrige cada peso |

**Glosario de símbolos, verbatim de la diapositiva 51:**

| Símbolo | Nombre | Qué representa |
|---|---|---|
| `x` | Entrada | El valor que llega a la unidad desde la capa anterior |
| `w` | Peso | El número que se aprende, asociado a cada conexión |
| `a` | Suma ponderada | La combinación lineal `xw + b`, antes de la activación |
| `y` | Salida | El resultado de aplicar la activación a la suma ponderada |
| `t` | Objetivo | El valor verdadero que viene con el dato de entrenamiento |
| `L` | Pérdida | El número único que mide cuánto se equivocó la red |
| `δ` | Delta | La sensibilidad del error respecto de la suma ponderada de esa unidad |
| `η` | Tasa de aprendizaje | El tamaño del paso con el que se corrige cada peso |

## Evidence and examples

- **El auto con sensores** (capítulo 1), atribuido a Mark Riedl. Es la metáfora que sostiene todo el primer capítulo y reaparece en el cierre como idea 1.
- **El ejemplo del clima** (capítulo 4), que es el hilo conductor con números concretos: 8 variables meteorológicas nombradas una por una, 9 unidades ocultas, 72 conexiones, 81 parámetros en la primera capa, matriz 8×9, y una capa final de 100×4.
- **La temperatura a lo largo del año y la distribución del ingreso** (diapositiva 8) como ejemplos de por qué una recta no alcanza.
- **El termostato** (diapositiva 49, anexo) como analogía de la activación: magnitud continua, decisión binaria.
- **Detección de bordes, texturas y objetos en visión** (diapositiva 43, anexo) como ejemplo de representaciones intermedias que la red descubre sola.
- El mazo **no trae ningún dataset, código ni resultado experimental**. Todos los números son de arquitectura (conteos de pesos y dimensiones), no medidos.

## Inconsistencies / open questions

- **Salto sin explicar en la tabla de dimensiones (diapositiva 22).** El ejemplo se construye con 8 entradas y 9 unidades ocultas, y la tabla pasa de golpe a `W⁽ⁿ⁾` de 100×4 y salida 1×4, sin decir de dónde salen las 100 unidades ni las 4 salidas. La diapositiva 48 del anexo lo aclara ("si la última capa oculta tiene 100 unidades y queremos 4 salidas"), pero esa diapositiva está fuera del recorrido de 105 minutos. Quien vea solo el mazo principal se queda sin la conexión.
- **La sigmoide se presenta como la no linealidad por defecto en el capítulo 2 y recién en el 5 se dice que el estándar en capas ocultas es ReLU.** No es un error, es el orden histórico, pero deja tres capítulos donde el alumno puede quedarse con que la sigmoide es la elección normal. La diapositiva 50 del anexo explica el porqué histórico y el problema del gradiente que se desvanece, pero también está fuera del recorrido.
- **Materia de origen distinta.** El mazo es de "Inteligencia Artificial Generativa Aplicada en Biomedicina" y este repositorio es de Ingeniería de Software. Los ejemplos (clima, ingreso, temperatura) son neutrales y se trasladan sin problema, pero la portada, el cierre ("aplicaciones en biomedicina") y la referencia a "la clase 8" son específicos de la otra materia y hay que decidir qué se hace con ellos.
- **Duración.** El archivo declara 105 minutos y el perfil del repositorio tiene 90 como default.
- **Solapamiento con `talks/modelado-redes-neuronales`.** Neurona y capa, funciones de activación con la misma tabla de cuatro funciones, y el catálogo de salida están cubiertos en las dos clases. Hay que decidir el orden entre ambas y qué se recorta para no repetir.
- **No hay notas del orador en ninguna diapositiva.** El mazo es solo contenido visible; todo el guion de cómo darlo hay que reconstruirlo.
- **Los conteos de parámetros del capítulo 4 conviene verificarlos** antes de reusarlos: 8×9=72 y 72+9=81 son correctos, y 100×4=400 también, pero el mazo no dice cuántos parámetros tiene la red completa ni cuántas capas ocultas hay entre la primera y la última.

## Images / diagrams

Las 41 imágenes únicas del mazo, extraídas a la carpeta compañera. El mazo tenía repeticiones (la misma imagen en varias diapositivas); se deduplicó por hash y se conservó la primera aparición. El nombre codifica la diapositiva de origen y el hash: `s<NN>-<hash>.<ext>`.

- `Intro-Redes-Neuronales-105min.pptx/images/s01-4077a450392b.png`
  - Provenance: diapositiva 1 del mazo — Inteligencia Artificial / Generativa Aplicada en
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s04-5f38a6a6454d.png`
  - Provenance: diapositiva 4 del mazo — DE LA INTUICIÓN A LA RED / Una red de sensores y actuadores
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s05-7d4e5ffebc44.png`
  - Provenance: diapositiva 5 del mazo — DE LA INTUICIÓN A LA RED / Aprender es ajustar qué caminos conducen
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s06-8bfdede90321.png`
  - Provenance: diapositiva 6 del mazo — DE LA INTUICIÓN A LA RED / El modelo más simple que ya conocemos
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s08-40ba91b6a999.png`
  - Provenance: diapositiva 8 del mazo — LA NEURONA Y LA CAPA / El mundo real no es lineal
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s09-4d516fc1e6a4.png`
  - Provenance: diapositiva 9 del mazo — LA NEURONA Y LA CAPA / La neurona: primero, una combinación
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s09-d050a6977b8b.png`
  - Provenance: diapositiva 9 del mazo — LA NEURONA Y LA CAPA / La neurona: primero, una combinación
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s10-3c2d24dbb626.png`
  - Provenance: diapositiva 10 del mazo — LA NEURONA Y LA CAPA / La sigmoide: la no linealidad clásica
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s11-54a05bc4894e.png`
  - Provenance: diapositiva 11 del mazo — LA NEURONA Y LA CAPA / La capa: el bloque que se repite
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s13-6be945f50483.png`
  - Provenance: diapositiva 13 del mazo — REDES PROFUNDAS / Apilar capas: qué es una red profunda
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s14-1d954f83773d.png`
  - Provenance: diapositiva 14 del mazo — REDES PROFUNDAS / Las dos dimensiones: ancho y profundidad
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s18-f1889f090f73.png`
  - Provenance: diapositiva 18 del mazo — EL RECORRIDO COMPLETO / Un caso concreto: predecir el clima
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s19-4331b60351e7.png`
  - Provenance: diapositiva 19 del mazo — EL RECORRIDO COMPLETO / Cada conexión es un peso
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s20-21f2fd47d0a3.png`
  - Provenance: diapositiva 20 del mazo — EL RECORRIDO COMPLETO / Todos los pesos, en una matriz
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s21-51491d0e73ef.png`
  - Provenance: diapositiva 21 del mazo — EL RECORRIDO COMPLETO / El cálculo de la capa es un producto
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s21-cf87887ddd74.png`
  - Provenance: diapositiva 21 del mazo — EL RECORRIDO COMPLETO / El cálculo de la capa es un producto
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s26-6bddaf9b74ea.png`
  - Provenance: diapositiva 26 del mazo — FUNCIONES DE ACTIVACIÓN / Sin activación, la red colapsa
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s28-6322673fdf1b.png`
  - Provenance: diapositiva 28 del mazo — FUNCIONES DE ACTIVACIÓN / Softmax: de puntajes a probabilidades
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s28-c9cadec7c247.png`
  - Provenance: diapositiva 28 del mazo — FUNCIONES DE ACTIVACIÓN / Softmax: de puntajes a probabilidades
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s31-222a372707cc.png`
  - Provenance: diapositiva 31 del mazo — BACKPROPAGATION / Ida y vuelta: forward y backward
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s32-d1a3c2fb290d.png`
  - Provenance: diapositiva 32 del mazo — BACKPROPAGATION / El error: la función de coste
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s33-1ccbc75a127c.png`
  - Provenance: diapositiva 33 del mazo — BACKPROPAGATION / La regla de la cadena
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s34-453542b3b9d8.png`
  - Provenance: diapositiva 34 del mazo — BACKPROPAGATION / Capa de salida: el delta
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s34-4c04b498f28d.png`
  - Provenance: diapositiva 34 del mazo — BACKPROPAGATION / Capa de salida: el delta
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s34-7e1441f8b259.png`
  - Provenance: diapositiva 34 del mazo — BACKPROPAGATION / Capa de salida: el delta
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s35-747d5b5238c4.png`
  - Provenance: diapositiva 35 del mazo — BACKPROPAGATION / Capa oculta: propagar el delta hacia
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s36-f3642b53d48c.png`
  - Provenance: diapositiva 36 del mazo — BACKPROPAGATION / El paso de actualización
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s40-8cc2e024855d.png`
  - Provenance: diapositiva 40 del mazo — DE LA INTUICIÓN A LA RED / Cada nodo decide cuánta energía deja
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s42-ea23758b1e80.png`
  - Provenance: diapositiva 42 del mazo — LA NEURONA Y LA CAPA / Del ejemplo mínimo a la red neuronal
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s43-b0e0fdd242eb.png`
  - Provenance: diapositiva 43 del mazo — REDES PROFUNDAS / ¿Qué pasa dentro de las capas ocultas?
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s44-eda1f816d334.png`
  - Provenance: diapositiva 44 del mazo — REDES PROFUNDAS / Cómo leer un diagrama de red
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s45-f160ea1eefb4.png`
  - Provenance: diapositiva 45 del mazo — REDES PROFUNDAS / El ciclo de ajuste
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s46-42838f7f1626.png`
  - Provenance: diapositiva 46 del mazo — EL RECORRIDO COMPLETO / Notación: quién se conecta con quién
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s46-bc3931b1a4a0.png`
  - Provenance: diapositiva 46 del mazo — EL RECORRIDO COMPLETO / Notación: quién se conecta con quién
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s47-842a83c0c695.png`
  - Provenance: diapositiva 47 del mazo — EL RECORRIDO COMPLETO / La capa oculta, completa
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s48-0711e53ea0d0.png`
  - Provenance: diapositiva 48 del mazo — EL RECORRIDO COMPLETO / Hacia la capa de salida
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s48-080d39f77284.png`
  - Provenance: diapositiva 48 del mazo — EL RECORRIDO COMPLETO / Hacia la capa de salida
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s49-0c5c7d04e27c.png`
  - Provenance: diapositiva 49 del mazo — FUNCIONES DE ACTIVACIÓN / La función de activación
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s49-1361be4b725f.png`
  - Provenance: diapositiva 49 del mazo — FUNCIONES DE ACTIVACIÓN / La función de activación
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s50-3f7e68cecb38.png`
  - Provenance: diapositiva 50 del mazo — BACKPROPAGATION / La sigmoide y su derivada
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->
- `Intro-Redes-Neuronales-105min.pptx/images/s50-fd950a8d8f36.png`
  - Provenance: diapositiva 50 del mazo — BACKPROPAGATION / La sigmoide y su derivada
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->

## Raw / preserved excerpts

### Agenda de la clase, verbatim (diapositiva 2)

> 1 · **De la intuición a la red** — Un circuito de sensores y actuadores, y por qué eso ya es una red neuronal
> 2 · **La neurona y la capa** — Combinación lineal, no linealidad y el bloque que se repite
> 3 · **Redes profundas** — Apilar capas: ancho, profundidad, parámetros e hiperparámetros
> 4 · **El recorrido completo** — Del input a la salida con un caso real: pesos, matrices y notación
> 5 · **Funciones de activación** — Por qué sin no linealidad la red colapsa, y cuál conviene elegir
> 6 · **Backpropagation** — Cómo la red mide su error y ajusta cada uno de sus pesos

### La metáfora de apertura (diapositiva 4)

> Imaginemos un auto con sensores — «viene algo por la izquierda», «estoy cerca de la pared» — conectados por cables a dos actuadores: el acelerador y el freno. Entre medio hay nodos que reparten la electricidad. Eso es, literalmente, una red neuronal.
>
> Fuente: Mark Riedl, «A Very Gentle Introduction to Large Language Models without the Hype».

### Qué es entrenar (diapositiva 5)

> Al principio los parámetros son azarosos y el auto choca. Probamos, medimos el error, retocamos apenas las compuertas y volvemos a probar. Después de muchísimas repeticiones, ciertos caminos quedan reforzados: son los que llevan del sensor correcto al actuador correcto.
>
> Esto es el entrenamiento. No hay nadie programando reglas: hay un procedimiento incremental que ajusta números hasta que el comportamiento del circuito se parece al que queríamos.

### Por qué no alcanza una recta (diapositiva 8)

> La temperatura a lo largo del año sube y baja; la distribución del ingreso cae de forma abrupta y después se aplana. Una recta puede aproximar el promedio, pero pierde justamente la forma que nos importa.
>
> Si queremos mejores predicciones, necesitamos mejores modelos. Y «mejor» acá significa: capaz de representar curvas, saturaciones y quiebres.

### La capa como bloque (diapositiva 11)

> Combinación lineal seguida de una no linealidad. Ese par es una capa, y es la unidad con la que se construye cualquier red: no hay una pieza más grande que aprender, solo esta repetida.
>
> Una capa toma un vector y devuelve otro vector. Encadenarlas es simplemente pasarle a la siguiente lo que produjo la anterior.

### El colapso sin no linealidad (diapositivas 25 y 26)

> «Necesitamos las no linealidades para poder romper la linealidad y representar relaciones más complicadas.»
>
> **Sin no linealidad:** La red puede ser tan profunda como queramos: sigue siendo equivalente a una única transformación lineal. Diez capas y una capa tienen el mismo poder expresivo.
>
> **Con no linealidad:** Cada capa dobla el espacio a su manera. Al encadenarlas podemos aproximar prácticamente cualquier función continua — es el teorema de aproximación universal.
>
> La no linealidad no es un detalle de implementación. Es lo único que justifica apilar capas.

> Dos transformaciones lineales encadenadas equivalen a una sola. Multiplicar por W₁ y después por W₂ es lo mismo que multiplicar por una única matriz W* — la profundidad desaparece.

### La advertencia sobre softmax (diapositiva 28)

> Ojo con dónde se aplica. Softmax se usa en la activación de la capa final. Si se la aplica en una capa oculta, se pierde información sobre la magnitud de los valores y solo sobrevive su proporción.

### El corazón de backpropagation (diapositiva 35)

> Una unidad oculta no tiene un objetivo con el cual compararse: nadie le dice cuál era su valor correcto. Su culpa se calcula sumando los deltas de todas las unidades de la capa siguiente a las que alimenta, ponderados por los pesos que las conectan.
>
> Acá está el corazón del algoritmo. El error se reparte hacia atrás capa por capa: cada unidad recibe la parte de culpa que le corresponde según cuánto influyó en las que venían después. De ahí el nombre «propagación hacia atrás».

### Las tres notas sobre η (diapositiva 36)

> **η muy chico:** El entrenamiento avanza, pero tan despacio que puede volverse impracticable.
> **η muy grande:** Los pasos se pasan del mínimo y el error oscila o directamente diverge.
> **El signo menos:** El gradiente apunta hacia donde el error crece; nos movemos justo en la dirección opuesta.

### El cierre, verbatim (diapositiva 37)

> Seis ideas que sostienen todo lo que viene después. Si estas quedan firmes, cualquier arquitectura moderna es una variación sobre el mismo tema.
>
> 01 · **Una red es un circuito** — Sensores, compuertas y actuadores. Aprender es ajustar cuánta señal deja pasar cada compuerta.
> 02 · **La capa es el bloque** — Combinación lineal más no linealidad, repetido. No hay una pieza más grande que entender.
> 03 · **La no linealidad es obligatoria** — Sin ella, apilar capas no agrega nada: la red colapsa en una sola transformación lineal.
> 04 · **Los pesos viven en matrices** — Las dimensiones se deducen de la arquitectura, y el cálculo de una capa es un producto matricial.
> 05 · **El error se propaga hacia atrás** — La regla de la cadena reparte la culpa entre todos los pesos, capa por capa.
> 06 · **El aprendizaje es incremental** — Adivinar, medir, corregir un poco, repetir. Millones de veces.

### Los próximos pasos declarados (diapositiva 38)

> La clase 8 retoma exactamente desde acá: las GANs son dos de estas redes compitiendo entre sí, entrenadas con el mismo mecanismo de backpropagation que acabamos de ver.

### Qué es el anexo, verbatim (diapositiva 39)

> Slides que quedaron fuera del recorrido de 105 minutos. Sirven para responder preguntas en vivo o como material de lectura posterior.

### Dos definiciones del anexo que vale la pena conservar

> **Deep Learning (diapositiva 41):** «Deep» no se refiere a la profundidad conceptual, sino a la cantidad de capas apiladas.
>
> **Notación (diapositiva 46):** El subíndice no es decorativo. El primer número identifica la unidad de entrada; el segundo, la unidad oculta a la que llega. Así, w₃₆ es el peso que va de la tercera entrada a la sexta unidad oculta.
