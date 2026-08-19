---
topic: Partición del dataset: train, validación y test
language: Español
sources:
  - talk: modelado-redes-neuronales
    date: 2026-08-19
    contributed: Los tres conjuntos con sus proporciones, la distinción sutil entre validación y test, el data leakage de preprocesamiento y los errores de partición que inflan la métrica.
last_updated: 2026-08-19
---

# Partición del dataset: train, validación y test

**Partir el dataset** es reservar de antemano tres porciones separadas, cada una con un trabajo distinto. Existe por una sola razón: si se mide el modelo con los mismos datos con los que se lo entrenó, la métrica miente.

![Las tres porciones del dataset](images/s3-1-1-particion-dataset.png)

## Los tres conjuntos

| | Train | Validación | Test |
|---|---|---|---|
| Para qué sirve | El modelo aprende de él | Tuning, early stopping, elegir modelo | Evaluación final sin sesgo |
| Cuándo lo ve el modelo | Cada epoch | Se evalúa cada epoch, nunca entrena con él | Una vez, al final |
| Actualiza los pesos | Sí | No | No |
| Augmentation | Sí | No | No |
| Proporción típica | 70% | 20% | 10% |

Al conjunto de validación también se lo llama **dev set** o **development set**, porque acompaña la etapa de desarrollo del modelo.

## La distinción sutil entre validación y test

El modelo no entrena con ninguno de los dos. La diferencia está en quien toma decisiones: el ingeniero mira las métricas de validación para elegir hiperparámetros, y **a lo largo de muchos experimentos va sobreajustando sus elecciones a ese conjunto**. Cuanto más se usa validación para decidir configuración, más sesgada queda esa métrica.

El test existe para atrapar eso. Como nada del modelo se eligió mirándolo, sus números son lo más parecido al desempeño en producción que se puede ver antes de desplegar. Reusar el validation set como test es mala práctica documentada.

Corolario: **el split de dos vías no alcanza.** Sin validación se termina tuneando contra el test, y para cuando se despliega sus métricas ya no son insesgadas. Solo sirve cuando no se toma ninguna decisión iterativa, que no describe a ningún proyecto real.

## Proporciones

- **70 / 20 / 10** es el default práctico de la industria.
- Con datasets muy grandes, de decenas de miles de ejemplos, **80 / 10 / 10** también funciona, porque ese 10% sigue siendo mucha muestra.
- **Piso absoluto:** no bajar validación ni test de unos pocos cientos de ejemplos. Por debajo de eso la métrica es ruido.

Advertencia de procedencia: estos números son recomendación de la casa de Roboflow, contenido de marketing de producto, no el resultado de un estudio. Sirven como criterio práctico, no como evidencia.

Modelos con pocos hiperparámetros son fáciles de validar y toleran un conjunto de validación más chico; con muchos hiperparámetros conviene uno grande, o cross-validation. Un modelo sin hiperparámetros tuneables casi no necesita validación.

## Todo lo que se aprende sale solo del train

La partición no alcanza si el preprocesamiento se calcula mal.

```python
# MAL: μ y σ contaminados con el test (data leakage)
scaler.fit_transform(X_test)

# BIEN: μ y σ aprendidos solo del train
scaler.fit(X_train)
scaler.transform(X_test)
```

- **Calcular las estadísticas sobre todo el dataset es data leakage.** Información del test se filtra al entrenamiento y la métrica sale optimista.
- **La transformación se aplica a los tres, sus parámetros salen de uno.** Normalizar, imputar y mapear categorías corre sobre train, validación y test por igual. Pero μ, σ, la mediana de imputación y el diccionario categoría a índice se calculan únicamente sobre train. Es un matiz que las fuentes de visión no cubren: dicen que el preprocesamiento se aplica a los tres splits, sin advertir de dónde salen sus parámetros.
- **Un modelo desplegado no son solo `W` y `b`.** Son los pesos más los μ y σ de cada variable, más el diccionario de categorías, más los valores de imputación. Si se guardan solo los pesos, el modelo queda inservible.
- **El bug es silencioso.** Normalizar en producción con μ=120 en vez de 95 no lanza ninguna excepción. Solo devuelve predicciones incorrectas.

## Errores de partición que inflan la métrica

Ninguno lanza una excepción. Todos devuelven un número mejor que el real.

- **Duplicados repartidos entre conjuntos (train/test bleed).** El mismo caso, o uno casi idéntico, cae en train y en test. El test deja de medir generalización y mide memoria. Aparece en cualquier dataset armado juntando fuentes. Se deduplica antes de partir.
- **No estratificar con clases desbalanceadas.** El azar reparte sin mirar la clase. Con 2% de positivos, el test puede quedar con tres casos, y un recall calculado sobre tres casos no es una métrica. Se estratifica por la clase.
- **Partir al azar una serie de tiempo.** El azar pone futuro en train y pasado en test: el modelo predice usando información que en producción no va a tener. Se corta por fecha.
- **Achicar validación y test.** Con conjuntos chicos la métrica tiene tanto ruido que dos modelos distintos parecen iguales, o el peor parece mejor.
- **Augmentation fuera de train.** Las variantes generadas sirven para aprender; validación y test tienen que quedarse con los datos originales, porque su trabajo es representar lo que viene en producción.

Nota de alcance: la estratificación y la partición temporal **no** están cubiertas por ninguna de las dos fuentes web de este tema. Son aporte del docente y conviene anclarlas a una fuente propia si se van a enseñar como tales.

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

## Cross-validation, y cuándo paga

K-fold divide el train en k porciones iguales, entrena k veces reservando una distinta cada vez y promedia las métricas. Cada ejemplo se usa para entrenar y para validar, lo que da una estimación más confiable con datasets chicos.

El costo es cómputo: k folds significa entrenar k veces. Para ML clásico es barato; para modelos profundos, donde una corrida cuesta tiempo y plata real, rara vez paga. Las dos fuentes de este tema difieren en el énfasis (Shah la presenta como cada vez más popular, Roboflow argumenta que en visión profunda no conviene) y no se contradicen en el fondo: depende del costo de entrenar y del tamaño del dataset.

## References

- [`../../talks/modelado-redes-neuronales/research/corpus/train-validation-test-sets.web.md`](../../talks/modelado-redes-neuronales/research/corpus/train-validation-test-sets.web.md) — Tarang Shah, *About Train, Validation and Test Sets in Machine Learning* (TDS Archive, 2017). Las definiciones formales de los tres conjuntos y la distinción validación/test. No da ratios a propósito.
- [`../../talks/modelado-redes-neuronales/research/corpus/train-test-split-roboflow.web.md`](../../talks/modelado-redes-neuronales/research/corpus/train-test-split-roboflow.web.md) — Jacob Solawetz, *Train, Validation, Test Split for Machine Learning* (Roboflow, 2026). Ratios concretos, tabla comparativa, errores típicos, código y el intercambio de cross-validation. Escrito para visión por computadora y con sesgo de producto.
- [`../../talks/modelado-redes-neuronales/research/corpus/chat.md.md`](../../talks/modelado-redes-neuronales/research/corpus/chat.md.md) — sección 6, μ, σ y el artefacto de producción.
- Jason Brownlee, *What is the Difference Between Test and Validation Datasets?* — machinelearningmastery.com/difference-test-validation-datasets/. Fuente de las definiciones que cita Shah.
