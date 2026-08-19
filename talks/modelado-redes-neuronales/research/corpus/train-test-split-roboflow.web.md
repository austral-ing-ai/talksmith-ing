---
source_file: train-test-split-roboflow
source_type: web-capture
ingested_at: 2026-08-19
---

# Train, Validation, Test Split for Machine Learning (Roboflow)

## Provenance
- Original location: research/web/train-test-split-roboflow/
- Format: html (captura web de blog.roboflow.com; page.md salió limpio y completo)
- Author / source (if known): Jacob Solawetz, Founding Engineer @ Roboflow
- Date of original (if known): 2026-04-07 (lectura de 8 minutos)
- URL: https://blog.roboflow.com/train-test-split/
- Relación con el otro registro: complementa a train-validation-test-sets.web.md (Tarang Shah, 2017). Aquel define los tres conjuntos y se niega a dar un ratio; este da ratios concretos, tabla comparativa, errores típicos y código.

## Key claims

**1. El resumen del propio artículo (verbatim del bloque SUMMARY)**
- Partir el dataset en tres para prevenir overfitting: **train 70%** (el modelo aprende), **validation 20%** (tuning y early stopping durante el entrenamiento), **test 10%** (se toca una sola vez al final, lectura no sesgada del desempeño en producción).
- Las **augmentations van solo en el training set**.
- Cuidado con el **train/test bleed**: imágenes duplicadas que caen en splits distintos e inflan las métricas.

**2. Por qué existe el split: overfitting**
- Durante el entrenamiento el modelo puede sobreajustar al training set, aprendiendo una función demasiado específica que anda bien en los datos de entrenamiento y no generaliza a datos nuevos.
- El síntoma medible: la loss de entrenamiento sigue bajando mientras la loss del validation set en algún momento **empieza a subir**. El artículo lo grafica con las dos curvas.
- Cuando eso pasa, el modelo no está aprendiendo, está memorizando el training set.
- "The train, validation, and testing splits are built to combat overfitting."

**3. Training set (70%)**
- El corpus más grande, reservado para entrenar. Inferir sobre estas imágenes no dice nada útil: el modelo ya tuvo oportunidad de mirarlas y memorizar la salida correcta.
- Recomendación explícita: **70% del dataset** como default.

**4. Validation set (20%)**
- Sección separada que se usa **durante** el entrenamiento para saber cómo le va al modelo con datos que no está usando para entrenar.
- Es habitual reportar métricas de validación **después de cada epoch** (validation mAP, validation loss). Con esas métricas se detecta cuándo el modelo llegó a su mejor desempeño posible y se puede cortar ahí: eso es **early stopping**.
- Sobre el validation set se itera dataset, augmentations y diseño del modelo.
- Recomendación: **20%**.

**5. Test set (10%)**
- Las métricas de validación **te influyeron a vos** durante la creación del modelo, así que como diseñador podés terminar sobreajustando el modelo al validation set.
- Por eso hace falta un conjunto completamente separado y guardado ("a completely separate stronghold of data"), que se evalúa **al final del proyecto**.
- Recomendación: **10%**.

**6. La distinción sutil validación contra test (el punto que el artículo remarca al cierre)**
- El modelo no entrena con ninguno de los dos. La diferencia es que **vos tomás decisiones mirando validación**, así que a lo largo de muchos experimentos vas sobreajustando tus elecciones a ese conjunto.
- El test set existe para atrapar eso: como **nada del modelo se eligió usándolo**, sus métricas son la mejor aproximación al desempeño en producción antes de desplegar.

**7. Preprocesamiento contra augmentation (regla operativa)**
- **Preprocesamiento** (crop estático, escala de grises, resize, auto-orient): estandariza el dataset y **se aplica a los tres splits**.
- **Augmentation** (alteraciones leves para agrandar el training set): **solo al training set**. Validación y test tienen que quedarse con las imágenes ground truth sin modificar, porque su trabajo es representar lo que el modelo va a ver en producción.

**8. Errores típicos (los tres que lista)**
- **Train/test bleed**: imágenes de test demasiado parecidas a las de train. El caso claro son los duplicados que caen en splits distintos; sesgan las métricas de evaluación.
- **Sobrepeso al training set**: la tentación de "más datos, mejor modelo" lleva a dejar apenas 10% para validación y test juntos. Con muestras chicas las métricas quedan turbias y te pueden hacer elegir un modelo subóptimo.
- **Sobrepeso a las métricas de validación y test**: valen lo que valen los datos que las respaldan y pueden no representar bien producción. Sirven de guía, no de verdad.

**9. Cómo se hace en Python**
- La herramienta estándar es `train_test_split` de scikit-learn, **llamada dos veces** para producir tres conjuntos.
- `random_state` fijo hace el split reproducible, lo que importa para comparar modelos entrenados sobre datos idénticos.
- Para detección de objetos: se parten pares imagen-anotación, y **cada clase tiene que aparecer en los tres conjuntos**.

**10. Ratios según tamaño del dataset (de la sección de preguntas)**
- **70/20/10** es un default sólido para datasets de visión.
- Con datasets muy grandes (decenas de miles de imágenes), **80/10/10** funciona porque 10% sigue siendo mucha imagen para evaluar confiable.
- **No achicar validación ni test por debajo de unos pocos cientos de ejemplos cada uno**: las métricas calculadas sobre una muestra chica son ruidosas.

**11. Por qué no alcanza con train y test**
- Sin validation set terminás tuneando contra el test, y para cuando desplegás sus métricas ya no son insesgadas porque tus decisiones se sobreajustaron a él.
- El split de dos vías sirve solo cuando no tomás ninguna decisión iterativa, que casi nunca describe un proyecto real.

**12. Cross-validation y su costo**
- K-fold es la principal alternativa al split fijo: se divide en k folds iguales, se entrena k veces reservando un fold distinto para validación cada vez, y se promedian las métricas. Cada ejemplo se usa para entrenar y para validar, lo que da una estimación más confiable con datasets chicos.
- **El costo es cómputo**: k folds significa entrenar k veces. Para ML clásico es barato; para modelos de visión profundos, donde una corrida cuesta tiempo y plata real, rara vez conviene.
- En la práctica los equipos de visión usan split fijo y gastan el cómputo ahorrado en más datos, y reservan cross-validation para datasets muy chicos donde un 20% de validación son muy pocos ejemplos.

## Definitions and terminology

| Término | Definición del artículo |
|---|---|
| Train, validation, test split | Dividir el dataset en tres: uno del que el modelo aprende, uno para tunear y monitorear durante el entrenamiento, y uno guardado hasta el final para medir sin sesgo el desempeño en producción. |
| Overfitting | El modelo aprende una función demasiado específica que anda bien en train y no generaliza a datos nunca vistos. Memorizar en vez de aprender. |
| Loss function | Forma de describir la "maldad" de un modelo. Cuanto más chico el valor, mejor el modelo. |
| Early stopping | Cortar el entrenamiento en el punto donde las métricas de validación indican que el modelo llegó a su mejor desempeño. |
| Preprocesamiento | Transformaciones que estandarizan el dataset. Se aplican a los tres splits. |
| Augmentation | Alteraciones leves que agrandan el training set. Solo al training set. |
| Train/test bleed | Ejemplos de test demasiado parecidos (o duplicados) de los de train, repartidos en splits distintos; inflan las métricas. |
| K-fold cross validation | k folds, k entrenamientos reservando un fold distinto por vez, métricas promediadas. |

**Tabla comparativa del artículo** (venía como tabla HTML y el extractor la aplanó; reconstruida):

| | Training set | Validation set | Test set |
|---|---|---|---|
| Propósito | El modelo aprende de él | Tuning, early stopping, selección de modelo | Evaluación final, no sesgada |
| Cuándo lo ve el modelo | Cada epoch | Se evalúa cada epoch, nunca se entrena con él | Una vez, al final |
| Augmentations | Sí | No | No |
| Proporción típica | 70% | 20% | 10% |

## Evidence and examples

- **Código de referencia (verbatim)**, split 70/20/10 con dos llamadas a scikit-learn:

```python
from sklearn.model_selection import train_test_split

# First split: 70% train, 30% held out
train_files, holdout_files = train_test_split(
    image_files, test_size=0.30, random_state=42
)

# Second split: divide the holdout into validation (20%) and test (10%)
val_files, test_files = train_test_split(
    holdout_files, test_size=1/3, random_state=42
)
```

- **Curvas de overfitting**: el artículo grafica loss de train bajando contra loss de validación subiendo (imagen `image-14.png`).
- **Ajuste excesivo en 2D**: figura de una función que pasa exactamente por los puntos de entrenamiento (imagen `image-12.png`).
- **Roboflow como producto**: el split se asigna en la carga, los duplicados se eliminan automáticamente, los ratios se ajustan por proyecto y el split queda congelado en la versión del dataset para que toda corrida y comparación use la misma partición.

## Inconsistencies / open questions

- **El artículo está escrito para visión por computadora**, no para datos tabulares. Habla de imágenes, mAP, augmentations de imagen y pares imagen-anotación. Los ratios, la lógica de los tres conjuntos, el train/test bleed y el argumento de validación contra test se trasladan sin problema a tabular; los ejemplos hay que traducirlos.
- **Es contenido de marketing de producto.** Varias secciones empujan a Roboflow ("Roboflow automatically removes duplicates"). Los números (70/20/10, 80/10/10) se presentan como recomendación de la casa, no como resultado de un estudio. Citar como criterio práctico de la industria, no como evidencia empírica.
- **No cubre partición temporal ni estratificada.** Igual que el registro de Medium, no dice nada de series de tiempo (donde el split aleatorio filtra futuro al pasado) ni de estratificar por clase con datos desbalanceados. Para esta Talk la estratificación importa: la sección 4 trabaja sobre desbalance de clases. Ese aporte lo tiene que poner el docente.
- **No conecta el split con el leakage de preprocesamiento numérico.** Dice que el preprocesamiento se aplica a los tres splits, pero no advierte que los **parámetros** de ese preprocesamiento (μ, σ, valores de imputación, diccionario de categorías) tienen que calcularse solo sobre train. Es una omisión relevante y es justo lo que cubre chat.md.md (§6).
- **Contradicción aparente entre las dos fuentes sobre cross-validation.** Tarang Shah la presenta como cada vez más popular y recomendable; Roboflow argumenta que en visión profunda rara vez paga el cómputo. No se contradicen en el fondo (dependen del costo de entrenar y del tamaño del dataset), y el contraste sirve para la clase.
- El título extraído arrastra "SearchSearch" del chrome del blog. El cuerpo salió limpio.

## Images / diagrams

- `train-test-split-roboflow.web/images/image-14.png`
  - Provenance: cuerpo del artículo, epígrafe "An example of overfitting during training". Curvas de loss de entrenamiento contra validación.
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->

- `train-test-split-roboflow.web/images/image-12.png`
  - Provenance: cuerpo del artículo, epígrafe "An example of a model tightly fitting a function based on training data". Ejemplo 2D de ajuste excesivo.
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->

- `train-test-split-roboflow.web/images/Screenshot-2026-04-01-at-2.44.41---PM.png`
  - Provenance: cuerpo del artículo, sin epígrafe, ubicada justo después de la pregunta "What is the train, validation, test split and why do I need it?".
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->

- `train-test-split-roboflow.web/images/Screenshot-2026-07-15-at-12.09.27---PM.png`
  - Provenance: cuerpo del artículo, en la sección del training set, junto a la mención de ajustar los defaults en Roboflow. Probablemente captura de la interfaz del producto.
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->

- `train-test-split-roboflow.web/images/img-blog-train-validation-and-test-split.png`
  - Provenance: imagen de portada del post.
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->

- `train-test-split-roboflow.web/images/logo-roboflow-purple.svg`
  - Provenance: logo de la marca, chrome del sitio.
  - Depiction: logotipo de Roboflow. Sin contenido editorial, no usar en diapositivas.
  - Why it matters: ninguno.
  - Transcribed text: "Roboflow".

## Raw / preserved excerpts

### Resumen del artículo (bloque SUMMARY, verbatim)

> Split your dataset three ways to prevent overfitting: a training set the model learns from (70%), a validation set for tuning and early stopping during training (20%), and a test set you touch once at the end for an unbiased read on production performance (10%). Augmentations go in the training set only, and watch for train/test bleed, where duplicate images land in different splits and inflate your metrics.

### Definición de arranque

> A train, validation, test split divides your dataset into three parts: a training set the model learns from, a validation set for tuning and monitoring during training, and a test set held back until the end for an unbiased measure of how the model will perform in production. The split exists to prevent overfitting and to keep your evaluation honest.

### Overfitting

> The danger in the training process is that your model may overfit to the training set. That is, the model might learn an overly specific function that performs well on your training data, but does not generalize to images it has never seen.

> If your model hyper-specifies to the training set, your loss function on the training data will continue to show lower and lower values, but your loss function on the held-out validation set will eventually increase.

> This means that your model isn't learning well, but is basically memorizing the training set.

### Training set

> The difference between the training set and the validation set is the training set is the largest corpus of your dataset that you reserve for training your model. After training, inference on these images will be taken with a grain of salt, since the model has already had a chance to look at and memorize the correct output.

> For a default, **we recommend allocating 70% of your dataset to the training set**.

### Validation set

> The validation set is a separate section of your dataset that you will use during training to get a sense of how well your model is doing on images that are not being used in training.

> During training, it is common to report validation metrics continually after each training epoch such as validation mAP or validation loss. You use these metrics to get a sense of when your model has hit the best performance it can reach on your validation set. You may choose to cease training at this point, a process called "early stopping."

> We recommend holding out 20% of your dataset for the validation set.

### Test set

> After all of the training experiments have concluded, you probably have gotten a sense on how your model might do on the validation set. But it is important to remember that the validation set metrics may have influenced you during the creation of the model, and in this sense you might, as a designer, overfit the new model to the validation set.

> Because the validation set is heavily used in model creation, it is important to hold back a completely separate stronghold of data - the test set. You can run evaluation metrics on the test set at the very end of your project, to get a sense of how well your model will do in production.

> **We recommend allocating 10% of your dataset to the test set**.

### Preprocesamiento y augmentation

> Preprocessing steps are image transformations that are used to standardize your dataset across all three splits. Examples include static cropping your images, or gray scaling them. **All preprocessing steps are applied to train, validation, and test.**

> Image augmentations are used to increase the size of your training set by making slight alterations to your training images. These occur only to the training set and should not be used during evaluation procedures. For evaluation, you want to use the ground truth images, residing in the validation and test sets.

### Errores típicos

> Train Test bleed is when some of your testing images are overly similar to your training images. For example, if you have duplicate images in your dataset, you want to make sure that these do not enter different train, validation, test splits, since their presence will bias your evaluation metrics.

> The more data, the better the model. This mantra might tempt you to use most of your dataset for the training set and only to hold out 10% or so for validation and test. Skimping on your validation and test sets, however, could cloud your evaluation metrics with a limited subsample, and lead you to choose a suboptimal model.

> At the end of the day, the validation and test set metrics are only as good as the data underlying them, and may not be fully representative of how well you model will perform in production. That said, you should use them as a guide post, pushing your models performance and robustness ever higher.

### La distinción validación contra test (cierre)

> The subtle one is validation versus test. The model never trains on either, but you make decisions based on validation metrics, so over many experiments you gradually overfit your choices to the validation set. The test set exists to catch that: because nothing about the model was chosen using it, its metrics are the closest preview of production performance you can get before deploying.

### Tamaño de los conjuntos

> A 70/20/10 split is a solid default for computer vision datasets. With very large datasets (tens of thousands of images), 80/10/10 works because 10% is still plenty of images for reliable evaluation. Avoid shrinking validation and test below a few hundred images each; metrics computed on a tiny sample are noisy.

### Por qué no alcanza train y test

> Without a validation set, you end up tuning against the test set, and by the time you deploy, its metrics are no longer unbiased since your decisions overfit to it. The two-way split works only when you make no iterative decisions, which almost never describes a real project.

### Cross-validation

> K-fold cross-validation is the main alternative to a fixed split. Instead of one validation set, the data is divided into k equal folds; the model trains k times, each time holding out a different fold for validation, and the metrics are averaged. Every image gets used for both training and validation, which produces a more reliable performance estimate from a small dataset.

> The cost is compute: k folds means training the model k times. For classical machine learning that is cheap; for deep learning vision models, where a single training run takes real time and money, it rarely pays. In practice, computer vision teams use a fixed train, validation, test split and spend the saved compute on more training data, and reserve cross-validation for very small datasets where a single 20% validation slice is too few images to trust.

### Cita sugerida por el propio artículo

> Jacob Solawetz. (Apr 7, 2026). Train, Validation, Test Split for Machine Learning. Roboflow Blog: https://blog.roboflow.com/train-test-split/
