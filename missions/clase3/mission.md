# Misión: ¿cuánto vale esta casa?

## Qué se entrega

**Un único notebook Jupyter (`.ipynb`).** No un repo, no un `.py`, no un informe aparte: todo — código, gráficos, tabla de decisiones y respuestas escritas — vive adentro del notebook.

Tiene que **correr de arriba a abajo con "Restart & Run All"** en una máquina que solo tenga el `.csv` al lado, y **entregarse con las salidas ya ejecutadas a la vista** (gráficos y métricas visibles sin volver a correrlo).

Las explicaciones van en **celdas de markdown**, no en comentarios de código. Un notebook que es solo celdas de código no está entregado.

## Descarga

**[`house-prices-extended.csv`](https://austral-ing-ai.github.io/talksmith-ing/missions/clase3/house-prices-extended.csv)** — 1460 casas, 19 columnas de entrada y el precio.

Es el dataset de la clase ampliado: las 10 columnas numéricas que ya usamos, más columnas nuevas que **no** son enteros. La columna `AboveMedianPrice` ya no está.

## El cambio

En clase el modelo respondía *¿está por encima de la mediana?* — una sigmoide, un sí o un no. Ahora la pregunta es otra:

> **¿Cuánto sale esta casa, en dólares?**

Cambia la última capa, cambia la loss, cambian las métricas. Y cambia la entrada: hay estado, distrito, estilo de casa, mes de venta. Nada de eso entra en un `Dense` tal como viene.

## Milestones

### 1. La tabla de decisiones

Antes de escribir una línea de red, pasen **cada columna** por el checklist de la clase: qué es, qué significa la resta entre dos valores, cuántos valores distintos tiene, puede faltar, la voy a tener al momento de predecir.

**En el notebook:** una celda de markdown con una tabla, una fila por columna, la codificación elegida y el motivo en una línea.

> El dataset tiene **al menos tres trampas** de codificación de las que vimos en clase. Si su tabla las pasa por alto, el modelo va a entrenar igual — y ahí está el problema. Encontrarlas es parte del trabajo.

### 2. Baseline numérico

Entrenen una red usando **solo** las columnas numéricas, con salida de regresión. Es el piso contra el que se mide todo lo demás.

**Criterio de éxito:** el par activación-loss de la última capa es el correcto para predecir un real, y saben decir por qué la `accuracy` acá no significa nada. Reporten sobre el conjunto de prueba las tres métricas de regresión:

- **MAE** — *Mean Absolute Error*, error absoluto medio. El promedio de `|real - predicho|`. Sale en dólares.
- **RMSE** — *Root Mean Squared Error*, raíz del error cuadrático medio. También en dólares, pero el cuadrado castiga los errores grandes de forma desproporcionada.
- **MAPE** — *Mean Absolute Percentage Error*, error porcentual absoluto medio. El error relativo al precio de cada casa, en porcentaje.

### 3. Que entren las categóricas

Sumen las columnas no numéricas al modelo. `State` y `District` no tienen la misma cardinalidad: **una pide one-hot y la otra pide embedding**, y la decisión tienen que poder defenderla.

**Criterio de éxito:** el MAE baja de forma clara respecto del baseline, y pueden mostrar cuánto aportó cada bloque de columnas.

### 4. Que no memorice

Hagan overfitear al modelo a propósito y después arréglenlo: L2, dropout, early stopping — lo que decidan.

**Criterio de éxito:** el gráfico de pérdida de entrenamiento contra validación muestra el problema, y el gráfico del modelo corregido muestra la diferencia.

### 5. Tasar una casa

Predigan el precio de una casa que inventen ustedes, escrita como la escribiría una persona (`OverallQual=7`, `State='CA'`, `District='Greenfield'`, …), no como un vector escalado a mano.

**Criterio de éxito:** el preprocesamiento es parte del modelo, no un paso suelto del notebook. Cambiar solo el estado y volver a predecir mueve el precio en la dirección esperada.

## Extra: el rango, no el punto

Una tasación de "esta casa vale 240.000" es menos útil que "entre 205.000 y 290.000". Cambien la salida para que devuelva **P10, P50 y P90** con pinball loss.

**Criterio de éxito:** aproximadamente el 80% de las casas de prueba caen entre P10 y P90.

## Las cinco preguntas

Estas van respondidas **en el notebook**, en texto, con el número o el gráfico que las respalda. Son la parte que se corrige.

1. **Tres métricas, tres números.** MAE, RMSE y MAPE evalúan el mismo modelo y no coinciden. ¿Cuál le reportan a una inmobiliaria y por qué? Señalen la casa concreta del conjunto de prueba que más separa el MAE del RMSE, y expliquen qué tiene de particular.

2. **12 valores contra 72.** Justifiquen la codificación que eligieron para `State` y para `District`. Después háganlo mal a propósito: metan `District` como un entero de 0 a 71 y muestren qué le pasa al error. ¿Qué está asumiendo la red cuando lo lee así?

3. **La columna que no debería estar.** ¿Qué hicieron con `ListingId`? Entrenen una vez dejándola adentro y muestren las curvas de entrenamiento y validación. ¿Qué está "aprendiendo" el modelo, y por qué eso no es aprender?

4. **Lo que falta.** `LotFrontage` no está en ~7% de las filas. ¿Con qué la completaron? Comparen contra rellenar con 0 y digan qué significa ese 0 para la red. Y una más difícil: **¿el hecho de que falte dice algo por sí solo?** Pruébenlo.

5. **De dónde salió el escalador.** ¿Sobre qué datos calcularon la media y el desvío con los que normalizaron? Si los calculan sobre el dataset completo, el modelo entrena igual y sin dar ningún error — pero un número del reporte queda mentido. ¿Cuál, y por qué?

## Aprendizajes

Al cerrar la misión tienen que poder defender estas cinco:

- **La red no ve casas, ve un tensor de floats.** Todo el trabajo real está en cómo se arma ese tensor; ninguna capa extra recupera información que se perdió en la codificación.
- **La última capa la decide el problema, no el gusto.** Predecir un real, una probabilidad o una clase son tres salidas distintas, y la activación y la loss se eligen juntas.
- **Un error de codificación no da error.** Entrena, converge, muestra métricas lindas y falla en producción. Por eso el checklist va antes que la red, no después.
- **Medir es elegir qué error duele.** En clasificación era precision contra recall; en regresión es MAE contra RMSE. La elección la hace el negocio.
- **El modelo no son solo los pesos.** El escalador, el imputador y el mapa de categorías viajan con él. Si quedan sueltos en celdas del notebook en vez de viajar con el modelo, el modelo no se puede usar en ningún lado.

## La entrega

**Un archivo: `apellido1-apellido2-...ipynb`.** Adentro, en este orden:

1. Una celda de markdown inicial con los **nombres del grupo**.
2. La **tabla de decisiones** del Milestone 1 (markdown).
3. Los **cinco milestones** en secciones marcadas con títulos markdown (`## Milestone 2 — Baseline numérico`, etc.), cada uno con su código, sus gráficos y sus métricas ejecutados.
4. Las **cinco preguntas** respondidas en celdas de markdown, cada una pegada al código o al gráfico que la respalda.
5. El **extra**, si lo hicieron, al final y marcado como tal.

Recordatorio: se entrega **ejecutado** (con las salidas guardadas) y tiene que **volver a correr entero** sin intervención manual.

---

*Nota sobre el dataset: las columnas numéricas son las de la clase; las columnas nuevas y el precio son generados. Sirven para practicar codificación y regresión, no para sacar conclusiones sobre el mercado inmobiliario real.*
