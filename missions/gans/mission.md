# Misión: la fábrica de datos

## Qué se entrega

**Un único notebook Jupyter (`.ipynb`).** Todo adentro: código, gráficos, imágenes generadas, la curva comparativa y las respuestas escritas.

Tiene que **correr de arriba a abajo con "Restart & Run All"** en una máquina que solo tenga el dataset al lado, y **entregarse con las salidas ya ejecutadas a la vista** — los gráficos y las métricas visibles sin volver a correrlo. Una corrida completa tarda cerca de una hora; eso es esperado y no es excusa para entregar un notebook sin salidas.

Las explicaciones van en **celdas de markdown**, no en comentarios de código. Un notebook que es solo celdas de código no está entregado.

Si guardan pesos entrenados o lotes de imágenes generadas, van en un zip aparte. El notebook tiene que correr sin ellos.

Grupos de 3. Dos semanas.

## Descarga

**[`fabrica-de-datos.npz`](https://austral-ing-ai.github.io/talksmith-ing/missions/gans/fabrica-de-datos.npz)** — 15.250 imágenes de 28×28 en escala de grises, cuatro arreglos:

```python
import numpy as np

URL = "https://austral-ing-ai.github.io/talksmith-ing/missions/gans/fabrica-de-datos.npz"
d = np.load(URL)   # si falla, descarguen el archivo y abran la ruta local

X_train, y_train = d["X_train"], d["y_train"]   # (12250, 28, 28) uint8, (12250,) uint8
X_test,  y_test  = d["X_test"],  d["y_test"]     # (3000, 28, 28),      (3000,)
```

Las clases son `0 = sandalia`, `1 = zapatilla`, `2 = bota`. El reparto del set de entrenamiento:

| Clase | En entrenamiento | En prueba |
|---|---|---|
| sandalia | **250** | 1.000 |
| zapatilla | 6.000 | 1.000 |
| bota | 6.000 | 1.000 |

Desbalance de 1 a 24. Las tres clases son calzado y se confunden entre sí: la difícil no es difícil solo por ser escasa.

El dataset es un recorte de Fashion-MNIST. **El set de prueba es real, está balanceado y no se toca** — ni para entrenar, ni para elegir hiperparámetros, ni para decidir en qué época cortar.

## La historia

Un centro de distribución de indumentaria clasifica calzado por foto a medida que pasa por una cinta, y lo rutea según la categoría. Zapatillas y botas llegan todo el año: hay miles de fotos de cada una. De sandalias hay 250, porque son de temporada y la cinta las vio tres semanas en todo el año. La categoría escasa es también la que más se confunde con las otras dos, así que el clasificador se equivoca justo donde el error cuesta.

Sumar fotos reales no es opción: habría que esperar al verano que viene.

La pregunta de la misión es la que haría el jefe de planta:

> **¿Sirve fabricar los datos que faltan con una GAN, y cuánto?**

La respuesta por defecto es "no". Hay que ganársela con un número.

## Milestones

### 1. El piso honesto

Entrenen un clasificador de tres clases sobre el set desbalanceado, tal como viene. Reporten sobre el set de prueba: **recall por clase**, **macro-F1**, la **matriz de confusión** y el **PR-AUC de la clase escasa**.

Después midan los tres arreglos que **no** son generativos, cada uno por separado: **pesos de clase**, **oversampling** de la clase escasa y **aumentación clásica** (lo que decidan — volteos, recortes, pequeñas rotaciones).

**Criterio de éxito:** tienen cinco números en una tabla y saben decir por qué la `accuracy` acá miente. Esos cinco números son la vara: todo lo generativo que venga después se mide contra ellos, no contra el baseline pelado.

> El set de validación lo tienen que sacar del set de entrenamiento, y de 250 sandalias salen pocas. Cómo lo resuelven — estratificar, validación cruzada, cuántas reservan — es parte del trabajo y va justificado.

### 2. La GAN que memoriza

Entrenen una **DCGAN desde cero** usando solo las 250 sandalias. Es el camino que la intuición indica y el que no funciona; el entregable de este milestone es la evidencia de por qué.

Muestren tres cosas:

- Las **curvas de pérdida** del discriminador y del generador, con el momento donde el entrenamiento se desarma señalado y explicado.
- Una grilla de muestras generadas a lo largo del entrenamiento, donde se vea el **mode collapse** si aparece.
- El **chequeo de vecino más cercano**: para cada imagen generada, la imagen de entrenamiento más parecida por distancia L2, mostradas lado a lado. Más el histograma de esas distancias comparado contra el histograma de distancias entre imágenes reales distintas.

**Criterio de éxito:** pueden afirmar, con el histograma como respaldo, si el generador está inventando o copiando. Un generador que copia no fabrica datos nuevos — fabrica oversampling caro.

### 3. La GAN que sí funciona

Hay 12.000 fotos de calzado que la GAN de arriba ignoró. Elijan uno de los dos caminos y defiéndanlo:

- **Transferencia** — preentrenar la GAN con zapatillas y botas, después hacer fine-tuning sobre las 250 sandalias.
- **Condicionamiento** — una **cGAN** entrenada sobre las tres clases, que recibe la etiqueta como entrada y genera la clase que se le pida.

**Criterio de éxito:** el histograma de vecino más cercano del milestone 2 se corrió, y pueden mostrar en qué dirección. Medir diversidad, no "se ven lindas": cuántas imágenes de entrenamiento distintas aparecen como vecino más cercano de alguna muestra generada, y cuántas no aparecen nunca.

### 4. La fábrica

Ahora sí, fabriquen. Para varios tamaños de lote sintético — 250, 500, 1.000, 2.000, 4.000 sandalias generadas — agreguen las muestras al set de entrenamiento, reentrenen el clasificador y midan sobre el set de prueba real.

**El entregable es un gráfico:** macro-F1 (y el recall de sandalia) contra la cantidad de muestras sintéticas agregadas, con una línea por condición — baseline, oversampling, aumentación clásica, GAN del milestone 2, GAN del milestone 3.

**Criterio de éxito:** el gráfico tiene un punto donde la curva se da vuelta, o pueden mostrar que no se da vuelta en el rango probado. Si ninguna línea generativa le gana a las dos baratas, eso es un resultado válido y se reporta como tal — pero tienen que poder explicar por qué.

### 5. El filtro del discriminador

No todas las muestras generadas sirven. El discriminador que entrenaron ya es un juez entrenado: úsenlo. Puntúen las muestras generadas, quédense con el mejor percentil — elijan el corte y justifíquenlo — y reentrenen el clasificador con ese lote filtrado.

**Criterio de éxito:** la decisión escrita, con el número que la respalda: **esta fábrica va a producción o no va**. Y una advertencia que tienen que verificar en sus propios datos: el discriminador premia lo que *a él* le parece real, y lo que más le parece real suele ser lo más cercano a las imágenes que memorizó. Muestren si filtrar les subió la métrica a costa de bajar la diversidad.

## Extra: la loss que no se desarma

Reemplacen la pérdida original por **WGAN-GP** y entrenen con el mismo presupuesto de tiempo que usaron en el milestone 3 — el mismo reloj, no las mismas épocas.

**Criterio de éxito:** las dos curvas de entrenamiento una al lado de la otra, y la diferencia en estabilidad señalada sobre el gráfico. Si la métrica del clasificador no cambia, dígalo.

## Las cinco preguntas

Van respondidas **en el notebook**, en texto, con el número o el gráfico que las respalda. Son la parte que se corrige.

1. **Un número para el jefe de planta.** `accuracy` y macro-F1 evalúan el mismo clasificador y no coinciden. ¿Cuál reportan y por qué? Señalen la celda concreta de la matriz de confusión que más separa a los dos números, y digan qué le pasa a la planta cuando esa celda se equivoca.

2. **¿Inventó o copió?** Con el histograma del milestone 2, decidan si su GAN desde cero generó imágenes nuevas. Si copió: ¿qué aportó entonces agregar esas muestras, por encima de repetir las 250 originales? Compárenlo contra la línea de oversampling del milestone 4 — si las dos curvas son la misma, eso es la respuesta.

3. **El discriminador como control de calidad.** El score del discriminador, ¿correlaciona con que la muestra le sirva al clasificador, o solo con que se parezca a lo que ya vio? Muéstrenlo: grafiquen el score contra la mejora de métrica por lote filtrado, o muestren que no hay relación.

4. **Dos métricas que no se hablan.** Calculen una distancia tipo FID entre sandalias reales y generadas, usando como extractor de features su propio clasificador — no InceptionV3, y por lo tanto el número **no** es comparable con ningún FID publicado; digan por qué. Después encuentren el caso donde esa distancia mejora y la métrica del clasificador no se mueve, o al revés. ¿Cuál de las dos mide lo que la planta necesita?

5. **El número mentido.** ¿Sobre qué datos calcularon la normalización de las imágenes, y con qué conjunto eligieron la época en la que cortaron cada entrenamiento? Si la respuesta a cualquiera de las dos es "el set de prueba", el modelo entrena igual y sin dar ningún error, pero hay un número del informe que quedó mentido. ¿Cuál, y cuánto se infla?

## Reglas

- **El set de prueba es real e intacto.** Ni una imagen generada entra ahí, y no se usa para elegir nada. Un notebook donde el set de prueba tocó una decisión de entrenamiento no se corrige.
- **Sin la curva del milestone 4 no hay misión.** Es el entregable central; el resto la sostiene.
- **No se puntúa que las imágenes generadas se vean lindas.** Una grilla de sandalias convincentes que no mueve la métrica del clasificador vale cero. Lo que se mide es si el dato fabricado sirve.
- Todo en **Python**, con el stack de la materia (TensorFlow/Keras, numpy, scikit-learn, matplotlib).

## Cómo correrlo y cuánto tarda

Corre entero en una notebook común, sin GPU y sin gastar un peso en APIs. Estimaciones de reloj para una corrida completa:

| Pieza | CPU | GPU (Colab T4) |
|---|---|---|
| Clasificador baseline y los tres arreglos baratos | 5–10 min | ~1 min |
| DCGAN desde cero (M2) | 10–25 min | 2–4 min |
| Preentrenamiento + fine-tuning, o cGAN (M3) | 15–30 min | 3–5 min |
| Reentrenamientos del clasificador (M4 y M5) | 20–45 min | 4–6 min |
| **Total** | **45 min – 1,5 h** | **10–15 min** |

Menos de 2 GB de RAM. Las imágenes generadas se guardan como `uint8` en un `.npy`: 2.000 muestras pesan 1,6 MB, así que no hay motivo para guardar PNGs sueltos.

En Google Colab no hay que instalar nada y el dataset se lee desde la URL de arriba, igual que en la máquina de ustedes. Si lo corren local, sirve el mismo entorno de la misión de redes neuronales (`missions/mlp/setup.sh`).
