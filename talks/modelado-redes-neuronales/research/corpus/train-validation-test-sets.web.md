---
source_file: train-validation-test-sets
source_type: web-capture
ingested_at: 2026-08-19
---

# About Train, Validation and Test Sets in Machine Learning

## Provenance
- Original location: research/web/train-validation-test-sets/
- Format: html (captura web de Medium; texto extraído en page.md, HTML crudo en original.html)
- Author / source (if known): Tarang Shah, publicado en TDS Archive (ex Towards Data Science), Medium. Original del autor en http://tarangshah.com/blog/2017-12-03/train-validation-and-test-sets/
- Date of original (if known): 2017-12-06 (lectura de 4 minutos)
- URL: https://medium.com/data-science/train-validation-and-test-sets-72cb40cba9e7
- Fuente citada por el propio artículo: Jason Brownlee, "What is the Difference Between Test and Validation Datasets?" (machinelearningmastery.com/difference-test-validation-datasets/). Las definiciones formales de los tres conjuntos son cita textual de ese artículo.

## Key claims

**1. Los tres conjuntos, definidos**
- **Training set**: la muestra de datos que se usa para ajustar el modelo. Es el dataset con el que se entrenan los pesos y bias en el caso de una red neuronal. El modelo *ve* y *aprende* de estos datos.
- **Validation set**: la muestra que se usa para dar una evaluación no sesgada de un modelo ajustado sobre el training set, mientras se tunean los hiperparámetros. La evaluación se vuelve **más sesgada** a medida que la habilidad medida sobre validación se incorpora a la configuración del modelo.
- **Test set**: la muestra que se usa para dar una evaluación no sesgada del modelo **final** ajustado sobre el training set.

**2. Qué distingue a validación de test (el punto central del artículo)**
- Validación se usa para evaluación **frecuente**: el ingeniero la mira una y otra vez para afinar hiperparámetros. El modelo "ve" ocasionalmente estos datos, pero nunca *aprende* de ellos: los pesos no se actualizan con validación.
- Validación afecta al modelo, pero **solo de forma indirecta**, a través de las decisiones de hiperparámetros que toma la persona.
- Al validation set también se lo llama **dev set** o **development set**, nombre que tiene sentido porque es el conjunto que acompaña la etapa de desarrollo del modelo.
- El test set es el **gold standard**. Se usa **una sola vez**, cuando el modelo ya está completamente entrenado (con train y validación).
- El test set es lo que se usa para comparar modelos en competencia. Ejemplo del artículo: en muchas competencias de Kaggle el validation set se libera al principio junto con el training set, y el test set recién se libera cuando la competencia está por cerrar; el resultado sobre el test set decide el ganador.
- **Muchas veces se usa el validation set como test set, y es mala práctica.**
- Un buen test set está bien curado: contiene datos muestreados con cuidado que cubren las distintas clases que el modelo va a enfrentar en el mundo real.

**3. El ratio de partición**
- No hay un número único. Depende de dos cosas: (a) la cantidad total de muestras disponibles, y (b) el modelo concreto que se está entrenando.
- Modelos que necesitan mucho dato para entrenar: optimizar por un training set más grande.
- Modelos con **pocos hiperparámetros**: fáciles de validar y tunear, así que se puede achicar el validation set.
- Modelos con **muchos hiperparámetros**: conviene un validation set grande (y considerar cross-validation).
- Modelos **sin hiperparámetros** o con hiperparámetros que no se pueden tunear fácil: probablemente no haga falta validation set.
- Conclusión del autor: el ratio es específico del caso de uso, y la intuición para elegirlo se gana entrenando y construyendo más modelos.

**4. Cross-validation**
- Patrón habitual: primero partir en 2 (train y test), guardar el test aparte, y después tomar al azar un X% del train como training real y el (100-X)% restante como validación, con X fijo (por ejemplo 80%).
- El modelo se entrena y valida iterativamente sobre esas particiones distintas.
- Se usa el training set para generar múltiples particiones train/validación.
- Cross-validation **evita el overfitting** y es cada vez más popular. **K-fold cross validation** es el método más usado.

## Definitions and terminology

| Término | Definición del artículo |
|---|---|
| Training set | Muestra usada para ajustar el modelo. El modelo ve y aprende de ella. |
| Validation set | Muestra usada para evaluación no sesgada del ajuste sobre train **mientras se tunean hiperparámetros**. Evaluación frecuente. |
| Dev set / Development set | Sinónimos de validation set. |
| Test set | Muestra usada para evaluación no sesgada del modelo **final**. Uso único. Gold standard. |
| Cross-validation | Generar múltiples particiones train/validación a partir del training set, entrenando y validando de forma iterativa. |
| K-fold cross validation | El método de cross-validation más popular. |

Distinción operativa que el artículo repite: el modelo **aprende** del train, **ve ocasionalmente** el de validación (sin aprender), y **no toca** el de test hasta el final.

## Evidence and examples

- **Kaggle como caso concreto**: el validation set se publica al inicio junto con el training set; el test set real se publica recién cuando la competencia está por cerrar, y el resultado sobre él decide el ganador. Sirve para explicar por qué el test set se reserva.
- **Sesgo creciente de validación**: el artículo advierte que cuanto más se usa validación para decidir configuración, más sesgada queda esa métrica. Es el argumento de por qué hace falta un tercer conjunto.
- No hay tablas de ratios ni números concretos de split en el artículo: el autor evita dar un porcentaje recomendado a propósito y lo deja como decisión dependiente del caso. El único número que aparece es "X = 80%" como ejemplo ilustrativo de cross-validation.

## Inconsistencies / open questions

- **El artículo no da un ratio recomendado.** Para la clase, si se quiere un número concreto (70/15/15, 80/10/10), hay que traerlo de otra fuente o presentarlo como criterio propio del docente. El artículo solo justifica de qué depende.
- **No cubre partición temporal ni estratificada.** Nada sobre series de tiempo (donde el split aleatorio filtra futuro al pasado) ni sobre estratificar por clase cuando hay desbalance. Ambos son relevantes para esta Talk (la sección 4 trabaja con desbalance de clases) y quedarían como aporte del docente.
- **No conecta explícitamente el split con data leakage de preprocesamiento** (calcular μ y σ sobre todo el dataset). El artículo trata el leakage solo por el lado de reusar el test como validación. La conexión con el escalador la aporta el corpus de chat.md.md (§6).
- **Extracción**: page.md salió completo para el cuerpo del artículo, pero arrastra chrome de Medium (barras de navegación, pies, links de signin) arriba y abajo del texto. El cuerpo útil está entre "This is aimed to be a short primer" y "Originally found at". original.html está preservado verbatim.
- **Antigüedad**: 2017. Las definiciones siguen vigentes; el ecosistema de herramientas que menciona (Kaggle) cambió poco en lo relevante.

## Images / diagrams

- `train-validation-test-sets.web/images/splits-visualization-1Nv2NNAL.png` (776x185 px)
  - Provenance: figura del cuerpo del artículo, con epígrafe "A visualization of the splits". Recuperada a mano desde el `srcset` de original.html - el fetcher no la había bajado porque Medium la sirve con lazy-loading.
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->

- `train-validation-test-sets.web/images/hero-1ymAm5YO.jpeg` (1400x933 px)
  - Provenance: imagen de portada del artículo. Recuperada a mano desde el `srcset` de original.html.
  - Depiction: <!-- pending: process_images -->
  - Why it matters: <!-- pending: process_images -->
  - Transcribed text: <!-- pending: process_images -->

- `train-validation-test-sets.web/images/0*zndPPKgmW_e7SWzR.jpeg`, `...-2.jpeg`, `...-3.jpeg` (tres tamaños del mismo archivo), `1*JEuS4KBdakUcjg9sC7Wo4A.png`, `...-2.png`, `...-3.png` (tres tamaños), `1*dmbNkD5D-u45r44go_cf0g.png`
  - Provenance: avatares de autor y publicación, más el placeholder de usuario anónimo, bajados por el fetcher desde el chrome de Medium.
  - Depiction: chrome de la plataforma, sin contenido editorial. No usar en diapositivas.
  - Why it matters: ninguno.
  - Transcribed text: ninguno.

## Raw / preserved excerpts

> This is aimed to be a short primer for anyone who needs to know the difference between the various dataset splits while training Machine Learning models.

> For this article, I would quote the base definitions from Jason Brownlee's excellent article on the same topic, it is quite comprehensive, do check it out for more details.

### Training Dataset

> **Training Dataset**: The sample of data used to fit the model.

> The actual dataset that we use to train the model (weights and biases in the case of a Neural Network). The model *sees* and *learns* from this data.

### Validation Dataset

> **Validation Dataset**: The sample of data used to provide an unbiased evaluation of a model fit on the training dataset while tuning model hyperparameters. The evaluation becomes more biased as skill on the validation dataset is incorporated into the model configuration.

> The validation set is used to evaluate a given model, but this is for frequent evaluation. We, as machine learning engineers, use this data to fine-tune the model hyperparameters. Hence the model occasionally *sees* this data, but never does it "*Learn*" from this. We use the validation set results, and update higher level hyperparameters. So the validation set affects a model, but only indirectly. The validation set is also known as the Dev set or the Development set. This makes sense since this dataset helps during the "development" stage of the model.

### Test Dataset

> **Test Dataset**: The sample of data used to provide an unbiased evaluation of a final model fit on the training dataset.

> The Test dataset provides the gold standard used to evaluate the model. It is only used once a model is completely trained (using the train and validation sets). The test set is generally what is used to evaluate competing models (For example on many Kaggle competitions, the validation set is released initially along with the training set and the actual test set is only released when the competition is about to close, and it is the result of the the model on the Test set that decides the winner). Many a times the validation set is used as the test set, but it is not good practice. The test set is generally well curated. It contains carefully sampled data that spans the various classes that the model would face, when used in the real world.

### About the dataset split ratio

> Now that you know what these datasets do, you might be looking for recommendations on how to split your dataset into Train, Validation and Test sets.

> This mainly depends on 2 things. First, the total number of samples in your data and second, on the actual model you are training.

> Some models need substantial data to train upon, so in this case you would optimize for the larger training sets. Models with very few hyperparameters will be easy to validate and tune, so you can probably reduce the size of your validation set, but if your model has many hyperparameters, you would want to have a large validation set as well (although you should also consider cross validation). Also, if you happen to have a model with no hyperparameters or ones that cannot be easily tuned, you probably don't need a validation set too!

> All in all, like many other things in machine learning, the train-test-validation split ratio is also quite specific to your use case and it gets easier to make judgement as you train and build more and more models.

### Nota sobre cross-validation (verbatim)

> *Note on Cross Validation: Many a times, people first split their dataset into 2 - Train and Test. After this, they keep aside the Test set, and randomly choose X% of their Train dataset to be the actual **Train** set and the remaining (100-X)% to be the **Validation** set, where X is a fixed number (say 80%), the model is then iteratively trained and validated on these different sets. There are multiple ways to do this, and is commonly known as Cross Validation. Basically you use your training set to generate multiple splits of the Train and Validation sets. Cross validation avoids over fitting and is getting more and more popular, with K-fold Cross Validation being the most popular method of cross validation.*

### Cierre

> Originally found at http://tarangshah.com/blog/2017-12-03/train-validation-and-test-sets/

Tags de la publicación: Machine Learning, Data Science, Deep Learning, Statistics, Data.
