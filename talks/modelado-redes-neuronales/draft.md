---
presentation: Inteligencia Artificial Generativa (AI Gen)
class: "Diseño de redes neuronales: del dato a la predicción"
research: research/corpus/
description: Slides are grouped into Sections. Each Section contains one or more Slides.
presenter: Paulo Veiga, Claudio Riguetti, Marco Sorondo (Universidad Austral)
audience: Estudiantes de grado de Ingeniería de Software con base técnica fuerte
duration: 90 min
date: a definir
---

# Thesis

**Claim:** El diseño de una red neuronal se decide casi entero en cómo se codifica la entrada y cómo se modela la salida; el resto de la arquitectura sale del problema. Medir con la matriz de confusión y frenar el overfitting con regularización es lo que separa un modelo que entrena de uno que sirve.

**Why it matters:** Una red no ve un cliente, una imagen ni un contrato: ve un tensor de floats. Si la información que importa quedó mal codificada, ninguna cantidad de capas la recupera, y la mayoría de los errores de producción en ML nacen en la frontera entre el dato crudo y el modelo. Del otro lado, un modelo con 99% de accuracy puede ser inútil y uno que ajusta perfecto en entrenamiento puede fallar en cada caso nuevo. Diseñar bien la entrada y la salida, saber medir y saber regularizar cubre el 80% de las decisiones reales.

**Presenter feedback:**

---

# Agenda

**Narrative arc:** La clase sigue el recorrido de un dato a través de la red. Primero, qué se decide de verdad al diseñar (casi todo está en la entrada y la salida). Después el input en detalle: cómo un problema cualquiera se convierte en un vector de floats. Luego el output: cómo la tarea determina la última capa y su loss. Con la red ya armada, cómo se mide de verdad su desempeño con la matriz de confusión (accuracy sola no alcanza). Y para cerrar, el problema que arruina modelos que parecían buenos, el overfitting, y las herramientas para controlarlo, con L2 al frente.

**Sections (in delivery order):**

- 1. Qué se diseña de verdad
- 2. Modelar la entrada
- 3. Modelar la salida
- 4. La matriz de confusión
- 5. Overfitting
- 6. Regularización y L2

**Presenter feedback:**

---

# 1. Qué se diseña de verdad

**Goal of this section:** Reencuadrar el diseño de una red. La intuición del alumno suele estar en "cuántas capas, cuántas neuronas"; el mensaje es que esas decisiones importan poco y que el trabajo real está en la entrada y la salida. Sienta la base (neurona, activación) y el mapa de qué se decide y qué sale solo.

**Presenter feedback:**

---

## 1. La red no ve el problema, ve un tensor

### Content

- **Todo entra como números.** Un cliente, una máquina, una foto o un contrato llegan a la red como un vector de floats de tamaño fijo. La semántica original (que esto era una edad y aquello un barrio) desaparece en la codificación.
- **El input es una traducción.** Como toda traducción, puede perder cosas. Si la información que importa no quedó en el tensor, o quedó de una forma que borra su estructura, ninguna arquitectura la recupera después.
- **Por eso codificar mal es fatal.** La red solo ve floats y no tiene forma de detectar que una posición "era un código" y otra "era una cantidad". El error entra silencioso y se queda.

<!-- template: quote -->
<!-- generate-image: right | la traducción frágil entre un mundo complejo y un tensor de números, con información que puede perderse en el paso -->

### Sources

corpus/chat.md.md (§13 Las ideas de fondo; §2 El input: principio general)

### Speaker notes

Abrí con esto porque reordena toda la clase. La mayoría llega pensando que diseñar una red es elegir capas. Planteales la pregunta: ¿qué ve realmente la red cuando le pasás un cliente? La respuesta (un vector de números) es el hilo de las próximas dos secciones. Anclá la idea de "traducción con pérdida": es la que justifica por qué le vamos a dedicar 20 minutos a la entrada.

### Presenter feedback

---

## 2. La mitad de la arquitectura no se elige

### Content

Buena parte de lo que parece "decisión de diseño" sale sola del problema. Lo que queda para decidir es más chico de lo que parece.

- **Lo determina la tarea (no se decide):** cantidad de neuronas de salida, activación de salida y función de loss. Predecir un precio pide una salida lineal con MSE; clasificar en N clases pide softmax con cross-entropy. No hay margen.
- **Lo determina la codificación (crítico):** cantidad de neuronas de entrada y si se normaliza. Salen de cómo se representan las variables, y es donde se gana o se pierde el modelo.
- **Lo que sí se elige (importa poco):** cantidad de capas ocultas (1 a 3 alcanza para datos tabulares), ancho de cada capa (potencias de 2, decreciente) y activación oculta (ReLU salvo motivo).

<!-- format: editorial -->

### Sources

corpus/chat.md.md (§9 Diseño de la red: qué se decide y qué no)

### Speaker notes

Este es el mapa mental que quiero que se lleven. Contrastá con la expectativa: pasan horas tuneando capas y el retorno está en la entrada. Dato honesto para dejar caer acá o al final: en datos tabulares una red muchas veces pierde contra gradient boosting (XGBoost, LightGBM); las redes brillan cuando hay estructura que explotar (imágenes, texto, señales). Sirve para bajar la sobreexpectativa.

### Presenter feedback

---

## 3. Una neurona, en una línea

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
- **ReLU por defecto** en capas ocultas (`max(0, z)`). GELU o SiLU en transformers. La activación de salida es otra historia, y la vemos en la sección 3.

### Sources

corpus/chat.md.md (§1 Conceptos base: Activación, Pesos y bias)

### Speaker notes

Refresco rápido, la audiencia tiene base técnica. El punto que no puede faltar: por qué la no linealidad. Preguntales qué pasa si sacás la ReLU de una red de 5 capas. Respuesta: te queda una regresión lineal disfrazada. Los parámetros de una capa son m·n + m; útil para la cuenta de parámetros que aparece más adelante.

### Presenter feedback

---

# 2. Modelar la entrada

**Goal of this section:** El corazón de la clase. Mostrar el método para convertir cualquier variable en floats: la pregunta de la resta, la tabla de codificaciones, one-hot vs embedding, la normalización y el artefacto de producción (μ, σ). Que salgan sabiendo decidir cuántas neuronas de entrada necesita un problema real.

**Presenter feedback:**

---

## 1. Todo termina en un vector de floats

### Content

El input es todo lo que sabés del problema, convertido a números. Vamos a concentrarnos en el primer caso, **sin estructura (tabular)**: una fila por ejemplo y una columna por variable, sin vecindad ni orden intrínseco entre las columnas. Lo que cambia entre un caso y otro es qué significa la posición dentro del vector, y eso determina la arquitectura natural.

| Estructura del dato | Ejemplo | Qué se puede cambiar sin cambiar la respuesta | Arquitectura natural |
|---|---|---|---|
| Sin estructura (tabular) | Cliente: edad, ingreso, barrio | El orden de las columnas | Fully connected |
| Grilla 1D (señal) | ECG o audio | Desplazar en el tiempo | Conv 1D, RNN, Transformer |
| Grilla 2D (imagen) | Radiografía o foto | Desplazar en el espacio | Conv 2D |
| Secuencia (texto) | Reseña o mensaje | Nada, el orden es todo | Transformer |
| Conjunto (carrito) | Productos comprados | El orden de los elementos | Deep Sets, attention |
| Grafo (red de cuentas) | Transferencias entre cuentas | Renumerar los nodos | GNN |

La pregunta que ordena todo el zoológico: **¿qué transformaciones puedo aplicarle al input sin cambiar la respuesta correcta?** Esa invariancia elige la familia de arquitectura.

### Sources

corpus/chat.md.md (§2 El input: principio general)

### Speaker notes

Este marco es elegante y vale la pena bajarlo despacio. Definí "sin estructura" en contraste con una imagen: en una tabla, intercambiar dos columnas no cambia el significado si el modelo conserva sus nombres; no hay píxeles vecinos ni orden temporal que explotar. Para el resto de la clase nos quedamos en el caso tabular, el más común en problemas de negocio y donde las decisiones de codificación se ven más claras. Usá los ejemplos de la tabla para que cada familia tenga una imagen mental. Mencioná que texto e imágenes terminan también en un vector de tamaño fijo (un embedding) y de ahí vuelven al caso simple.

### Presenter feedback
- [closed] 2026-08-18 — "Marcar aca que lo que vamos a enforcanos en el caso 1 Sin estructura (tabular) |"
  Resolution: Se marcó el foco de la clase en el caso tabular.
- [closed] 2026-08-18 — "Que significa Sin estructura (tabular)"
  Resolution: Se definió explícitamente el caso tabular como filas y columnas sin vecindad ni orden intrínseco.
- [closed] 2026-08-18 — "?. Poner ejemplos en la tabla de que es cada caso."
  Resolution: Se añadieron ejemplos concretos para cada familia de estructura.

---

## 2. La pregunta que decide la codificación

### Content

Frente a cualquier variable, una sola pregunta ordena la decisión: **¿qué significa la resta entre dos valores?**

- **Da una cantidad interpretable** (85 m² menos 60 m² son 25 m² reales): 1 float normalizado, una neurona.
- **Da un orden pero no una magnitud confiable** (satisfacción 4 menos 2): ordinal, evaluar también one-hot.
- **No significa nada** (barrio 14 menos barrio 7): one-hot o embedding según cuántos valores distintos haya.
- **No se puede ni plantear:** probablemente no sea una feature útil.

Todo termina en floats, nunca en enteros. Los enteros aparecen en un solo lugar: como índice para buscar una fila en una tabla de embeddings. El entero no entra a la red, entra al lookup.

### Sources

corpus/chat.md.md (§3 Codificación de variables: la pregunta que decide todo; §3 Todo termina en floats)

### Speaker notes

Esta pregunta es la herramienta más transferible de la clase. Si se llevan una sola cosa de la sección, que sea esta. Ejemplo en vivo: tirales tres variables de un dataset que conozcan (edad, código postal, nivel educativo) y que apliquen la pregunta en voz alta. El código postal es la trampa clásica: parece número, la resta no significa nada.

### Presenter feedback

---

## 3. Numéricas: normalizar no es opcional

### Content

El gradiente respecto a un peso es proporcional al valor de la entrada (`∂J/∂wⱼ = δ · xⱼ`), pero el learning rate es uno solo para toda la red. Si una variable vale ~200 (m²) y otra vale 0 o 1 (cochera), sus gradientes están a escala 200 a 1 y el entrenamiento zigzaguea.

- **z-score por defecto:** `(x − μ) / σ`. El valor pasa a leerse como "cuántos desvíos por encima o por debajo del promedio". La unidad original desaparece.
- **log antes del z-score con colas largas:** ingresos, cantidad de transacciones, días desde la última compra. La diferencia entre 1 y 10 transacciones importa más que entre 4000 y 4010.
- **Los booleanos y one-hot no se tocan:** ya están en 0 y 1.
- **Escala pareja no es importancia pareja.** Normalizar no le quita peso a una variable; la importancia la aprenden los pesos. Solo la pone en condiciones de ser evaluada.

### Sources

corpus/chat.md.md (§5 Escalas y normalización)

### Speaker notes

El "por qué" formal es el número de condición de la Hessiana, pero para la clase alcanza con la imagen de las curvas de nivel: escalas parejas dan círculos y el gradiente apunta al mínimo; escalas dispares dan elipses alargadas y el gradiente apunta a la pared. Efecto secundario importante: con sigmoide o tanh una entrada grande satura la neurona (derivada casi cero) y deja de aprender. Aclará que árboles y gradient boosting no necesitan normalización; es una particularidad de los métodos basados en gradiente.

### Presenter feedback

---

## 4. Categóricas: one-hot contra embedding

### Content

Una categoría sin orden se codifica de dos formas, y la cardinalidad decide cuál.

```ascii
one-hot "Depto":  [0, 1, 0, 0]   una neurona por valor, todas equidistantes
                      |
        W · x  selecciona la columna de W  -->  cada categoría, sus propios pesos
```
<!-- ascii-note:
intent: mostrar que one-hot con W selecciona una columna de pesos
emphasize: el 1 activa una sola columna de W
labels: one-hot vector, W matriz de pesos
-->

- **One-hot** (cardinalidad baja): una neurona por valor, todas en 0 salvo una en 1. Todas las categorías quedan a la misma distancia, que es la verdad del dato. No se aprende, es interpretable, necesita pocos datos.
- **Embedding** (cardinalidad alta): una tabla de `k × d` floats entrenable. La red aprende la distancia entre categorías desde los datos. Con 500 barrios, un embedding de dimensión 24 usa 24 neuronas donde one-hot usaría 500.
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

- **Código como número.** Barrio 7 y barrio 14 cargados como 7 y 14. La red asume que 14 es "el doble" de 7. Van como one-hot o embedding.
- **ID único como feature.** DNI, número de póliza, CUIT. No tienen poder predictivo; si el modelo "aprende" de ellos, está memorizando ejemplos. Se descartan.
- **Variables cíclicas aplastadas.** Las 23:00 y las 00:00 están a una hora, pero como números planos están a 23. Se codifican con dos neuronas, `sin(2πt/T)` y `cos(2πt/T)`.
- **Faltantes rellenados con 0.** Cuando 0 es un valor válido, confunde ausencia con valor. La receta es imputar (media o mediana) más un flag binario, que muchas veces predice más que la variable misma.

### Sources

corpus/chat.md.md (§3 Codificación de variables: enteros que son códigos, cíclicas, faltantes; §11 Los errores que más cuestan)

### Speaker notes

Sección de "no lo hagas". Estos cuatro son los que más veces vas a ver en trabajos de alumnos y en producción. El de los códigos y el de los IDs únicos son los favoritos. Contá el caso del ID: el modelo memoriza el dataset de train, da accuracy perfecto y se derrumba con datos nuevos. Es un puente natural hacia overfitting, que vemos en la sección 5.

### Presenter feedback

---

## 6. μ y σ: el modelo no son solo los pesos

### Content

Las estadísticas de normalización se calculan solo con el conjunto de entrenamiento, y se guardan para reaplicarlas idénticas en validación, test y producción.

```python
# MAL: μ y σ contaminados con el test (data leakage)
scaler.fit_transform(X_test)

# BIEN: μ y σ aprendidos solo del train
scaler.fit(X_train)
scaler.transform(X_test)
```

- **Calcularlos sobre todo el dataset es data leakage.** Información del test se filtra al entrenamiento y la métrica sale optimista. La regla general: todo lo que se aprende de los datos se aprende solo del train, transformaciones incluidas.
- **Un modelo desplegado no son solo `W` y `b`.** Son los pesos más los μ y σ de cada variable, más el diccionario categoría a índice, más los valores de imputación. Si se guardan solo los pesos, el modelo queda inservible.
- **El bug es silencioso.** Normalizar en producción con μ=120 en vez de 95 no lanza ninguna excepción. Solo devuelve predicciones incorrectas.

### Sources

corpus/chat.md.md (§6 μ, σ y el artefacto de producción)

### Speaker notes

Cierre práctico de la sección de input y el puente al mundo real. Este es el error número uno de producción en ML según la fuente: que la normalización o el diccionario de categorías queden fuera del artefacto. La regla para llevarse: el preprocesamiento y el modelo se despliegan juntos, siempre; quien consume el modelo no debería tener que saber que la normalización existe. Si hay tiempo, mencioná data drift: la solución no es recalcular μ y σ en producción, es detectar el drift y reentrenar.

### Presenter feedback

---

# 3. Modelar la salida

**Goal of this section:** Mostrar que la última capa no se elige, la determina la tarea, y que activación de salida y loss van siempre juntas. Que salgan sabiendo mapear "qué predice el modelo" a "cuántas neuronas, qué activación, qué loss", y evitar los dos errores de modelado de salida más comunes.

**Presenter feedback:**

---

## 1. La capa de salida la determina la tarea

### Content

La activación de salida es el mismo tipo de objeto que ReLU, pero se elige con otro criterio: poner el número en el rango y la interpretación correctos. Las cuatro representaciones viven en una misma slide para comparar su forma y su rango.

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

Contrastá con las capas ocultas: ahí la activación casi no importa (ReLU y listo). En la salida, cada opción corresponde a una forma y un rango. Recorré las cuatro filas como representaciones: recta para lineal, curva acotada para sigmoide, competencia entre clases para softmax y curva positiva para softplus. Preguntá por casos: ¿qué activación para predecir la cantidad de unidades vendidas? Softplus o exp, porque un conteo no puede ser negativo. La salida lineal con MSE para conteos permite predicciones negativas, un error clásico.

### Presenter feedback
- [closed] 2026-08-18 — "Seria bueno si podemos meter todas en en un slide como es la representacion de cada una de estas funciones."
  Resolution: Se reorganizó la diapositiva como una tabla comparativa de las cuatro funciones, con fórmula, rango y ejemplo.

---

## 2. Un catálogo para elegir sin dudar

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

---

## 3. Dos formas de modelar mal la salida

### Content

- **Softmax donde iba sigmoide.** Un ticket puede ser "urgente" y "de facturación" a la vez. Softmax fuerza a que las clases compitan y sumen 1. Si las etiquetas no son excluyentes, la salida está mal modelada de raíz: van N sigmoides independientes.
- **Predecir un punto cuando el negocio pedía un rango.** Si la decisión depende del peor escenario (cuánto stock, cuánto riesgo, cuánta capacidad), un valor puntual no alcanza. Ahí van cuantiles o una distribución.

Los dos errores comparten causa: la salida se eligió mirando la arquitectura en vez de la pregunta del negocio.

### Sources

corpus/chat.md.md (§8 Los dos errores más comunes)

### Speaker notes

Cierre de sección. El de softmax vs sigmoide es conceptual y se entiende con el ejemplo del ticket multi-etiqueta. Preguntá: ¿clasificar géneros de una película es softmax o sigmoide? Sigmoide, porque una película puede ser comedia y drama. Buen momento para reforzar que el modelado de la salida es una decisión de producto, no solo técnica.

### Presenter feedback

- [closed] 2026-08-18 — "Borrar este slide."
  Resolution: Se retiró la diapositiva; su detalle de implementación quedó preservado en Cut material.

---

# 4. La matriz de confusión

**Goal of this section:** El modelo ya está diseñado y entrenado; ahora, ¿anda? Mostrar por qué accuracy engaña, presentar la matriz de confusión como la foto completa de los aciertos y errores, derivar precision, recall y F1, y explicar por qué el umbral cambia todo. Nota: este tema no está en el corpus; el contenido viene del conocimiento del área (ver Open questions).

**Presenter feedback:**

---

## 1. El 99% de accuracy que no sirve

### Content

Un detector de fraude sobre transacciones donde 99 de cada 100 son legítimas alcanza 99% de accuracy con una sola regla: decir siempre "no es fraude". Nunca detecta un fraude y su métrica se ve excelente.

- **Accuracy es la fracción de aciertos sobre el total.** Con clases desbalanceadas, la mide la clase mayoritaria y esconde el error que importa.
- **No todos los errores cuestan lo mismo.** Marcar como sana a una transacción fraudulenta y molestar a un cliente legítimo con una alerta son errores distintos, con costos distintos.
- **Hace falta separar los tipos de error,** no un solo número. Ahí entra la matriz de confusión.

<!-- template: stat -->

### Sources

Conocimiento del área (no cubierto por el corpus). Ejemplo del detector de fraude, ilustrativo.

### Speaker notes

Arranque con gancho concreto: el clasificador que dice siempre "no". Es la mejor forma de que se les caiga la ficha de que accuracy sola no alcanza. El 99% es un ejemplo ilustrativo, no un dato de una fuente; dejalo claro si alguien pregunta. Este es el puente desde la salida (sección 3, clasificación con sigmoide) hacia cómo se evalúa esa clasificación.

### Presenter feedback

---

## 2. Quiz: ¿precisión o recall?

### Content

En cada caso, elegí qué error es menos tolerable. La métrica que priorizás cae sola.

1. **Filtro de spam:** bloquear un mail legítimo es peor que dejar pasar uno dudoso. ¿Priorizás precisión o recall?
2. **Test de una enfermedad grave:** dejar ir a una persona enferma es peor que pedir estudios extra. ¿Priorizás precisión o recall?
3. **Alerta de fraude:** el equipo puede revisar pocas alertas, pero cada fraude no detectado cuesta caro. ¿Qué priorizás y qué costo aceptás?

**Respuesta:** precisión cuando una alerta falsa es cara; recall cuando dejar pasar un positivo es más grave. En fraude no hay respuesta universal: depende de la capacidad de revisión y del costo del fraude.

<!-- template: quiz -->

### Sources

Conocimiento del área (no cubierto por el corpus). Casos ilustrativos.

### Speaker notes

Hacé las tres preguntas antes de mostrar la respuesta. En spam, la respuesta esperada es precisión; en diagnóstico, recall. En fraude, no cierres con una métrica automática: pediles que expliciten el costo de una revisión y el costo de no detectar. Usá esta slide como puente: precision y recall no son trofeos técnicos, son decisiones de operación.

### Presenter feedback

- [closed] 2026-08-18 — "Hagamos un quiz de 3 pregutas donde mostremos la decision en cuanto queres que elegir precision sobre recall."
  Resolution: Se agregó un quiz de tres casos para decidir entre precisión y recall, con una respuesta que explicita los costos.

---

## 3. La matriz de confusión

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

El centro de la sección. Dibujá la matriz en el pizarrón mientras aparece en la slide y pedí que ubiquen el ejemplo del fraude en cada celda. La confusión típica del alumno es FP vs FN; anclalo con el costo: en un test médico, un FN (mandar a casa a alguien enfermo) suele ser mucho peor que un FP (un estudio de más). Que se lleven que la matriz es la foto completa y accuracy es solo la diagonal sobre el total.

### Presenter feedback

---

## 4. Precision, recall y F1

### Content

De las cuatro celdas salen las métricas que de verdad describen a un clasificador.

- **Precision = TP / (TP + FP).** De todo lo que el modelo marcó como positivo, cuánto lo era. Sube cuando molesta poco con falsas alarmas. Importa cuando el costo del FP es alto (marcar spam un mail importante).
- **Recall = TP / (TP + FN).** De todo lo que era positivo, cuánto agarró. Sube cuando se escapan pocos. Importa cuando el costo del FN es alto (no detectar una enfermedad o un fraude).
- **F1 = media armónica de precision y recall.** Un solo número cuando ambas importan. La media armónica castiga los desbalances: si una es 1.0 y la otra 0.0, F1 es 0, no 0.5.
- **Precision y recall están en tensión.** Subir una suele bajar la otra. Qué priorizar lo decide el costo del error, no la matemática.

### Sources

Conocimiento del área (no cubierto por el corpus).

### Speaker notes

Insistí en la intuición antes que en la fórmula. Precision responde "cuando dice que sí, ¿le creo?"; recall responde "de todos los que eran, ¿cuántos encontró?". El truco mnemotécnico: precisión mira la columna de predichos positivos, recall mira la fila de reales positivos. F1 es útil pero peligroso si se reporta solo; siempre conviene mirar las dos. Si dan tiempo, mencioná accuracy = (TP+TN)/total para cerrar el círculo con la slide anterior.

### Presenter feedback

---

## 5. El umbral y la matriz N×N

### Content

Un clasificador binario no devuelve "sí" o "no", devuelve una probabilidad. El umbral (por defecto 0.5) es el que la convierte en decisión, y moverlo reacomoda toda la matriz.

- **Bajar el umbral sube el recall y baja la precision:** el modelo marca más positivos, agarra más verdaderos pero también más falsas alarmas.
- **Subir el umbral hace lo contrario.** El umbral se elige según el costo del error, no se deja en 0.5 por inercia.
- **La curva precision-recall resume ese trade-off** para todos los umbrales de una vez, y sirve para comparar modelos sin fijar uno.
- **En multiclase la matriz crece a N×N.** La diagonal son los aciertos; cada celda fuera de la diagonal dice con qué otra clase se confunde cada una. Precision y recall se calculan por clase y se promedian.

### Sources

Conocimiento del área (no cubierto por el corpus).

### Speaker notes

El umbral es lo que más cuesta que entiendan y lo más útil en la práctica. Ejemplo: un modelo de fraude con recall bajo en 0.5 puede pasar a recall alto bajando el umbral a 0.2, a costa de más falsas alarmas que el equipo antifraude tendrá que revisar. Es una perilla de negocio. La matriz N×N cierra la sección y conecta con el softmax de la sección 3. Si el tiempo aprieta, esta slide se puede recortar a los dos primeros bullets.

### Presenter feedback

---

# 5. Overfitting

**Goal of this section:** Definir overfitting como la brecha train-validación, dar el diagnóstico de tres casos y explicar el intercambio sesgo-varianza que justifica por qué regularizar empeora el entrenamiento a propósito. Prepara la sección 6.

**Presenter feedback:**

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

Este es el mapa de decisión que ordena la sección 6. Insistí en el orden: primero se diagnostica, después se trata. Regularizar un modelo que hace underfitting (train alto) empeora las dos métricas. Conectá con el ID único de la sección 2: memorizar el DNI es overfitting en estado puro, train perfecto y validación mala.

### Presenter feedback

---

## 2. Sesgo contra varianza

### Content

La regularización no mejora el ajuste. Lo empeora a propósito en entrenamiento, a cambio de que el modelo generalice mejor a datos nuevos. La brecha de la slide anterior se ve así a lo largo del entrenamiento:

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

El intercambio sesgo-varianza es el fundamento teórico de todo lo que viene. La metáfora que funciona: estudiar para un examen memorizando las respuestas de los ejercicios viejos (varianza alta, te va mal con ejercicios nuevos) contra entender el método (algo de sesgo, generaliza). Preparen el terreno: todas las técnicas de la sección 6 son formas distintas de bajar varianza.

### Presenter feedback

---

# 6. Regularización y L2

**Goal of this section:** El cierre técnico. L2 (weight decay) en detalle porque es el estándar y está en el título de la clase, después L1 por contraste, dropout, y el resto del arsenal con la guía de cuál usar y los errores de aplicación.

**Presenter feedback:**

---

## 1. L2: penalizar los pesos grandes

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

- **Por qué funciona.** Un peso grande hace que la salida sea muy sensible a esa entrada. Con pesos chicos la función aprendida es más suave, y una función suave es menos capaz de pasar exactamente por cada punto de entrenamiento, que es justo lo que hace el overfitting.
- **De ahí el nombre "decay".** El gradiente del término λΣw² empuja cada peso un poco hacia cero en cada paso.
- **λ es el hiperparámetro,** típicamente entre 1e-5 y 1e-2. En PyTorch: `Adam(params, weight_decay=1e-4)`.
- **Al sesgo (bias) no se le aplica:** el bias no controla la sensibilidad a la entrada. En inferencia L2 no hace nada, ya quedó incorporado en los pesos.

### Sources

corpus/chat.md.md (§10 Regularización: L2 weight decay)

### Speaker notes

El tema del título, dedicale tiempo. El "por qué funciona" es lo importante: pesos grandes, función que oscila para tocar cada punto; pesos chicos, función suave que generaliza. Dibujá dos ajustes sobre los mismos puntos, uno que serpentea y uno suave. Aclará el detalle del bias, que a casi nadie le queda claro: penalizás pesos, no sesgos, porque el bias solo desplaza, no amplifica la entrada.

### Presenter feedback

---

## 2. L1 contra L2

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

## 3. Dropout: no depender de ninguna neurona

### Content

Durante el entrenamiento, dropout apaga al azar una fracción de las neuronas en cada paso hacia adelante.

- **Cómo actúa.** Cada neurona se apaga con probabilidad p (típico 0.2 a 0.5 en capas ocultas). La red no puede depender de ninguna neurona en particular, así que reparte la representación en vez de armar detectores frágiles.
- **Es un ensamble implícito** de muchas subredes que comparten pesos.
- **En inferencia se desactiva:** todas las neuronas quedan activas. En PyTorch, `nn.Dropout(0.2)`.
- **El bug que muerde:** olvidar `model.eval()` deja dropout activo en inferencia, y el modelo devuelve predicciones distintas en cada llamada. Le pasa también a BatchNorm.

### Sources

corpus/chat.md.md (§10 Regularización: Dropout)

### Speaker notes

El `model.eval()` es el bug de PyTorch que van a cometer sí o sí en la práctica; que suene fuerte ahora para que lo recuerden después. La lectura de ensamble es elegante: en cada paso entrenás una subred distinta, y en inferencia usás el promedio. Dato para el que pregunte por qué en visión moderna casi no se usa dropout: se lleva mal con BatchNorm (lo vemos en la próxima slide).

### Presenter feedback

---

## 4. El resto del arsenal y cuál usar

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
- **Accuracy sola engaña.** La matriz de confusión separa los tipos de error; precision, recall y F1 describen lo que accuracy esconde, y el umbral es una perilla de negocio.
- **Regularizar es bajar varianza a propósito.** Primero se diagnostica el overfitting (brecha train-validación), después se trata: L2 de base, dropout en redes profundas, early stopping casi siempre.

### Sources

corpus/chat.md.md (§9, §10, §13); conocimiento del área (sección 4)

### Speaker notes

Recapitulá siguiendo el recorrido del dato: entró (input), salió (output), lo medimos (matriz de confusión), lo cuidamos (regularización). Cuatro ideas, una por sección troncal. Dejá espacio para preguntas antes del checklist.

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

- Sección 4 (Matriz de confusión) no está cubierta por el corpus (`chat.md.md`). El contenido viene del conocimiento del área. Si el presentador quiere anclarlo a una fuente propia (apunte, capítulo, ejemplo con números reales de un dataset del curso), conviene sumarla en la Colecta y re-verificar los números. El ejemplo del "99% de accuracy" y los costos FP/FN son ilustrativos, no datos de una fuente.
- La fuente advierte que en datos tabulares una red suele perder contra gradient boosting (XGBoost, LightGBM). Está en las notas del orador (slide 1.2) como contrapunto honesto. Decidir si darle más aire en clase o dejarlo como comentario al pasar.
- Duración: el borrador tiene ~25 slides para 90 min. La sección 2 (input) es la más cargada. Si en el ensayo queda largo, candidatas a recortar: slide 4.4 (umbral + multiclase, a dos bullets) y slide 6.2 (L1 vs L2).

# Cut material

## Activación y loss se eligen juntas (retirada por feedback)

- `BCEWithLogitsLoss` y `CrossEntropyLoss` ya incluyen la sigmoide y el softmax por estabilidad numérica. Si además se pone la activación en la capa, se aplica dos veces y el modelo entrena mal.
- En inferencia, con logits crudos: `prob = torch.sigmoid(model(x))`. Un logit de 2.3 no es una probabilidad.
- Fuente: corpus/chat.md.md (§8 El detalle de implementación; los pares que no se rompen).
