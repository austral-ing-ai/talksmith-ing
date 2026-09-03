---
source_file: AIG4B-Clase-2-LLM.md
source_type: article
ingested_at: 2026-08-14
---

# AIG4B — Clase 2: Introducción al Deep Learning y el Procesamiento del Lenguaje Natural

## Provenance
- Original location: `research/articles/AIG4B-Clase-2-LLM.md` (+ `research/articles/AIG4B-Clase-2-LLM-media/`)
- Format: Markdown — extracción lossless 1:1 de un deck PowerPoint de 32 slides (`AIG4B-Clase-2-LLM.pptx`, en la raíz del Talk). Las 30 imágenes del deck vienen en la carpeta `-media/` con nombres `slide-NN-M.<ext>` (número de slide, orden dentro de la slide) más un `_manifest.json` con slide, nombre de shape y tamaño en EMU.
- Author / source (if known): Marcos Sorondo. Material de clase del curso *Inteligencia Artificial Generativa Aplicada en Biomedicina* (AIG4B), Universidad Austral.
- Date of original (if known): "Ultima Modification: Marzo, 2026" (según la slide 1).

## Key claims

Recorrido slide por slide, en orden.

**Slide 1 — Portada.** Curso: "Inteligencia Artificial Generativa Aplicada en Biomedicina". Clase 2: "Introducción al Deep Learning y el Procesamiento del Lenguaje Natural". Autor: Marcos Sorondo. Última modificación: Marzo, 2026. Es la única slide del deck con notas del orador (ver `Raw / preserved excerpts`).

**Slide 2 — Agenda.** Objetivo declarado: "Entender cómo se puede generar texto automáticamente." El recorrido es:
- Problemas clásicos de ML
- NLP: motivación y problemas
  - Language Modelling: predecir la siguiente palabra
  - Representación de texto: tokens, vocabulario y embeddings
- Redes neuronales: del perceptrón al deep learning
- De RNNs a Transformers: el rol de attention
- Transformers: Cómo funciona un LLM

**Slide 3 — La Taxonomía de Problemas de IA.** Pregunta rectora: "¿Qué tipos de problemas resuelve la IA?" El deck define **ocho** tipos, presentados en dos tablas de tres más un bloque suelto y un callout:

| Predicción | Percepción | Representación |
|---|---|---|
| Aprender X → Y a partir de datos etiquetados. Incluye clasificación y regresión. | Extraer estructura de señales sensoriales: imagen, audio, video. | Aprender embeddings y espacios latentes que capturan relaciones entre datos. |

| Decisión Secuencial | Búsqueda / Planificación | Razonamiento Simbólico |
|---|---|---|
| Maximizar recompensa acumulada. Formalizado como Reinforcement Learning. | Encontrar la mejor secuencia de acciones en un espacio de estados. | Manipular símbolos y reglas IF–THEN para derivar conclusiones lógicas. |

- **Generación** — "Producir nuevas muestras coherentes: texto, imagen, audio, código. Infinita cantidad de outputs."
- Callout: "💡 Un auto autónomo combina percepción + decisión secuencial + planificación"

(Nota de conteo: el deck enumera siete categorías nombradas — Predicción, Percepción, Representación, Decisión Secuencial, Búsqueda/Planificación, Razonamiento Simbólico, Generación — y coloca ocho iconos. Ver `Inconsistencies / open questions`.)

**Slide 4 — "Machine Learning: Cómo funciona la IA moAderna".** Slide íntegramente visual: una sola figura (`slide-04-1.jpg`) que contrasta programación clásica (Rules + Data → Classical Programming → Answers) con machine learning (Data + Answers → Machine Learning → Rules). No hay texto propio en la slide más allá del título.

**Slide 5 — Problemas clásicos de ML.** "¿Como se formulan concretamente los problemas vistos?"
- Clasificación (Prediccion) → ¿A qué categoría pertenece? (ej: ¿este email es spam o no?)
- Regresión (Prediccion) → ¿Qué valor va a tener? (ej: ¿cuánto va a costar esta casa?)
- Clustering (Representación) → ¿Qué datos se parecen entre sí? (ej: agrupar pacientes con síntomas similares)
- Generación → ¿Puedo crear datos nuevos? (ej: generar imágenes, texto)
- Cierre: "El modelo aprende patrones de los datos, no se programa con reglas explícitas."

**Slide 6 — Problemas clásicos de ML aplicados a texto.** "Cada problema clásico de ML tiene un equivalente cuando el input es texto."

| Problema ML | ¿Qué resuelve? | Ejemplo con texto |
|---|---|---|
| Clasificación | Asignar una categoría | ¿Este review es positivo o negativo? |
| Clasif. multiclase | Elegir entre varias categorías | ¿En qué idioma está escrito? |
| Clustering | Agrupar datos similares | Agrupar noticias por tema |
| Predicción | Completar información | The ___ is on the mat → cat |
| Generación | Crear datos nuevos | The cat is on the ___ → mat |

- Ejemplos de sentimiento: "Qué bien comimos en el restaurante" → positivo; "No vuelvo nunca más a comer" → negativo.
- Cadena de procesamiento: "input (texto) → modelo → output".
- Pregunta bisagra que abre la sección NLP: "Todas requieren alguna manera de comprender el texto. ¿Cómo hacemos para que un modelo entienda texto?"

**Slide 7 — ¿Por qué procesar texto automáticamente?** "Cómo las máquinas pueden analizar grandes volúmenes de texto." Argumento: "Vivimos rodeados de texto: emails, historias clínicas, papers, redes sociales, reportes. Hay demasiado texto para que un humano lo procese manualmente." Casos de uso listados:
- Analizar opiniones de miles de pacientes sobre un tratamiento
- Clasificar papers científicos por área
- Detectar automáticamente el idioma de un documento
- Responder preguntas a partir de un texto largo
- Resumir un paper de 30 páginas en un párrafo

Cierre / definición de campo: "El campo que se ocupa de esto se llama Procesamiento del Lenguaje Natural (NLP)."

**Slide 8 — Problemas de NLP.** Matriz de 5 columnas × 5 ejemplos que aterriza cada familia de problema en NLP:

| Clasificación | Clasif. Multiclase | Clustering | Predicción | Generación |
|---|---|---|---|---|
| Detección de spam (spam / no spam) | Detección de idioma (español, inglés, francés...) | Agrupar noticias por tema | Autocompletar palabras en un buscador | Resumen automático de textos |
| Análisis de sentimiento (positivo / negativo) | Clasificación de intención del usuario (comprar, preguntar, quejarse...) | Agrupar reseñas similares de productos | Predecir la siguiente palabra en una oración | Traducción automática |
| Detección de discurso de odio (sí / no) | Etiquetado gramatical (sustantivo, verbo, adjetivo...) | Segmentar clientes por estilo de escritura | Completar huecos en texto (masked LM) | Generación de respuestas en chatbots |
| Detección de noticias falsas (real / falsa) | Clasificación de emociones (alegría, tristeza, enojo, miedo...) | Descubrir tópicos en un corpus (topic modeling) | Predecir la puntuación de una reseña | Generación de código a partir de texto |
| Detección de paráfrasis (sí / no) | Clasificación de tickets de soporte (facturación, técnico, ventas...) | Agrupar documentos legales por área del derecho | Predecir palabras faltantes en OCR dañado | Parafraseo automático de oraciones |

**Slide 9 — ¿Cómo se resolvían estos problemas? (Enfoque tradicional).** "El trabajo del data scientist consistía en:"

| 01 | 02 | 03 |
|---|---|---|
| Recolectar datos (conseguir textos relevantes) | Etiquetar datos (un humano marca: "esto es positivo", "esto es negativo") | Entrenar un modelo específico para cada tarea |

- "Un modelo para sentimiento, otro para traducción, otro para NER..."
- "Cada tarea requería su propio pipeline, sus propios datos etiquetados, su propio modelo."
- "Era costoso y lento."

**Slide 10 — Modelos de Generación de Palabras (el problema de Language Modelling).** Formulación formal. Dado:
- un vocabulario `V`
- un corpus de texto `T`
- una frase incompleta `P`

"El objetivo es predecir cuál es la siguiente palabra más probable."

Bloque **Importante**: "El modelo no devuelve directamente una palabra, sino un vector de probabilidades sobre todo el vocabulario."
- una posición por cada palabra del vocabulario
- cada valor indica la probabilidad de que esa palabra sea la siguiente
- "La longitud del vector es |V|."

**Slide 11 — Ejemplo trabajado de Language Modelling.** Corpus juguete con `V` de 14 tokens y `T` de 5 frases; `P = "the dog sat on"`; la palabra correcta es `"bed"` y el modelo le asigna 0.78. Ver el texto completo en `Raw / preserved excerpts`.

**Slide 12 — Sidetrack: Aprendizaje (Learning).** Slide de transición, una sola pregunta: "Cómo los modelos aprenden a generar texto (y cómo aprenden a resolver todas las tareas que vimos) a partir de los datos (corpus T)?"

**Slide 13 — Concepto: Entrenamiento.** "¿Cómo aprende un modelo a predecir la siguiente palabra a partir del corpus?"

- Paso 0: "El modelo por dentro tiene 'clavijas' (parámetros) internas que hay que ajustar para que predigan correctamente la siguiente palabra mas probable."

| 01 | 02 | 03 |
|---|---|---|
| Input: el modelo recibe una frase incompleta → "El gato está en la" | Predicción: genera una distribución de probabilidades | Comparación: la palabra mas probable era "alfombra". |
| 04 | 05 | 06 |
| Error (Loss): se calcula qué tan lejos estuvo de la palabra mas probable. | Ajuste: se modifican los parámetros para que el error sea menor | Repetición: se hace millones de veces con millones de frases |

- 07 — "Resultado: un modelo que sabe 'hablar'."
- "Nos quedamos con los parámetros que minimizan el error."

Conceptos clave declarados en la slide:
- **Loss (pérdida)**: número que mide qué tan equivocado estuvo el modelo
- **Optimización**: proceso de ajustar los parámetros para reducir la loss

**Slide 14 — ¿Qué le vamos a enseñar a nuestro modelo?** "En nuestro caso: a generar palabras. Pero el mismo método sirve para resolver cualquiera de los problemas ya vistos." Y el puente a representación: "El primer paso para generar palabras (o para cualquier tarea de NLP), es lograr que el modelo entienda qué significa. Para eso, necesitamos representarlas como números (vectores)."

**Slide 15 — Representación de palabras: Tokens.** "Los modelos trabajan con números, no con letras. El primer paso es dividir el texto en tokens — las unidades mínimas que el modelo procesa. Cada token tendrá un vector asignado que lo identifica."
- "Un token puede ser: una palabra completa, parte de una palabra, o un signo de puntuación."
- Ejemplo palabra-por-token: `"the cat sat on the mat"` → `["the", "cat", "sat", "on", "the", "mat"]` (6 tokens)
- **Palabras vs Tokens** — "Los modelos modernos usan sub-palabras (o incluso caracteres)": `"unbelievable"` → `["un", "believ", "able"]` (3 tokens)
- Ventajas de sub-palabras enumeradas: vocabularios más compactos (no necesita una entrada por cada palabra del idioma); entiende palabras nuevas descomponiéndolas en partes conocidas; funciona en múltiples idiomas.

**Slide 16 — Vocabulario y Representaciones de Texto.** "El vocabulario V es el conjunto completo de tokens que el modelo conoce. Por eso predice un vector de probabilidades de tamaño |V|. Pero el token (texto) en sí no puede ser procesado con los parámetros del modelo (números) directamente. Hay que convertir los tokens en números…"

Formas de representar texto numéricamente:

| Bag of Words / TF-IDF | Contar palabras. Ignora orden y significado. |
|---|---|
| One-Hot Encoding | Vector con un solo 1. No captura similitud ("cat" y "dog" igual de lejos que "cat" y "refrigerator"). Cada vector canónico se corresponde con un token. |
| Embeddings | Vectores donde tokens con significado similar tienen vectores similares. Es lo que usan los modelos modernos. |

**Word2Vec** (mismo slide):
- "Uno de los primeros métodos para aprender embeddings automáticamente."
- Idea: "una palabra se define por la compañía que tiene".
- Funcionamiento: "Saca promedios de los vectores de las palabras que circundan a cada una en el corpus de texto en que aparece."
- Importante: "Word2Vec no es un modelo de lenguaje (no genera palabras). Es un método para obtener embeddings con significado real de palabras en su contexto."

**Slide 17 — Embedding de Texto.** "Embedding de texto: vector que codifica el significado de una palabra."
- "Palabras relacionadas y con significados similares se encuentran 'cercanos' en el espacio."
- "También codifican relaciones entre palabras: el vector que me lleva de 'man' a 'woman' es el mismo que me lleva de 'king' a 'queen'...."

**Slide 18 — Redes Neuronales: Perceptrón.** "El bloque fundamental de las redes neuronales — la neurona artificial más simple." ¿Cómo funciona?
- Recibe varios inputs (números)
- Cada input se multiplica por un peso (importancia de ese input)
- Se suman todos los productos + un bias (valor de ajuste)
- El resultado pasa por una función de activación → output
- Fórmula tal cual aparece: `output = activación( x₁·w₁ + x₂·w₂ + x₃·w₃ + bias )`
- "Los pesos y el bias son los parámetros que el modelo aprende durante el entrenamiento."
- Analogía: "es como tomar una decisión. Tenés varios factores (inputs), cada uno te importa más o menos (pesos), y al final tomás una decisión (output). El bias es tu predisposición inicial."
- **En NLP:** "x_1,...,x_n es la representación numérica de una palabra (o de una frase). ¿Cómo sacamos el x_1,...,x_n de una frase? Word2Vec saca el promedio (obs: se pierde información del orden)."

**Slide 19 — Redes Neuronales Profundas (Deep Learning).** "¿Qué pasa si apilamos muchas capas de perceptrones? Obtenemos una red neuronal profunda — de ahí viene el nombre Deep Learning."
- "Cada capa transforma la información en una representación más abstracta":
  - Capas iniciales: detectan patrones simples (combinaciones de letras, formas básicas)
  - Capas intermedias: detectan patrones más complejos (palabras, frases, relaciones)
  - Capas finales: capturan conceptos de alto nivel (significado, intención, contexto)
- "Más capas = más parámetros = mayor capacidad de modelar relaciones complejas."
- Trade-off explícito: "Pero también = más datos necesarios para entrenar y más cómputo. Es un trade-off."
- "Los modelos de lenguaje modernos tienen miles de millones de parámetros (GPT-4, Claude, LLaMA)."

**Slide 20 — Arquitectura de Red Neuronal Profunda (Perceptrón Multicapa).** Slide íntegramente visual: solo el título y la figura `slide-20-1.jpg` (MLP completo con capas, pesos indexados y capa de salida).

**Slide 21 — Entrenamiento de Redes Neuronales: descenso de gradiente.** "¿Cómo aprenden los pesos correctos? El proceso es iterativo:"
- Se le da un ejemplo al modelo
- El modelo genera una predicción con sus pesos actuales
- Se compara la predicción con la respuesta correcta
- Se calcula la loss (qué tan lejos estuvo)
- Se ajustan los pesos un poquito en la dirección que más reduce la loss (`-∇`)
- Se repite con el siguiente ejemplo

Analogía de la montaña: "Imaginá que estás en la cima de una montaña con niebla y querés llegar al valle (mínima loss). No podés ver el camino completo, pero podés sentir la pendiente bajo tus pies. En cada paso caminás un poco hacia abajo. Eso es gradient descent."

**Learning rate**: "tamaño del paso: muy grande → te pasás, muy chico → tardás una eternidad."

**Slide 22 — Ciclo de Entrenamiento en Machine Learning.** (Slide sin título propio en la extracción; el título va como bold en el cuerpo.)

| 01 | 02 |
|---|---|
| Calcular la Loss | Determinar la Dirección |
| Pasar los pesos y el bias por el modelo con los datos del dataset para generar predicciones y luego calcular la loss. | Determinar en qué dirección mover los pesos y el bias para reducir la loss. |
| 03 | 04 |
| Actualizar los Pesos | Repetir |
| Moverse un pequeño paso en la dirección que reduce la loss. | Repetir el proceso hasta que la loss no pueda reducirse más. |

**Slide 23 — Backpropagation.** "En una red con muchas capas, ¿cómo sabemos cuánto ajustar cada peso?"
- Intuición: "en el fondo una red neuronal es una función 'diferenciable' (aproximadamente)"

| 01 | 02 |
|---|---|
| Forward pass | Cálculo de loss |
| El input viaja hacia adelante por la red hasta producir una predicción | Se mide el error entre predicción y valor real |
| 03 | 04 |
| Backward pass | Actualización |
| El error se propaga hacia atrás, calculando cuánto contribuyó cada peso | Cada peso se ajusta proporcionalmente a su contribución al error |

- "Es una forma de aplicar la regla de la cadena (sacar el gradiente de una composición de funciones), en una red neuronal."
- Analogía: "Es como rastrear un error en una cadena de producción: el producto final salió mal, entonces vamos viendo en cada paso quién tuvo más culpa y corregimos más a ese."
- "Esto es lo que permite entrenar redes con millones de parámetros."

**Slide 24 — Backpropagation: Visualización.** Slide íntegramente visual: solo el título y la figura `slide-24-1.jpg`.

**Slide 25 — Redes Recurrentes (RNNs).** "Antes de Transformers, las RNNs procesaban texto palabra por palabra, de izquierda a derecha, manteniendo un estado interno ('memoria')."
- Traza: `"El" → actualiza estado → "gato" → actualiza estado → "está" → ...`
- Variantes nombradas: **LSTM** (decide qué recordar/olvidar), **GRU** (simplificada), **ELMo** (embeddings contextuales).
- **Limitaciones**: "Procesamiento secuencial → no se puede paralelizar → lento"; "Dificultad con dependencias largas: la información se 'diluye' con la distancia".
- **El problema del contexto**: `"The animal didn't cross the street because it was too tired"` — "¿A qué se refiere 'it'? A 'animal'. Pero están lejos en la oración." / "Para cuando la RNN llega a 'it', la info sobre 'animal' se debilitó → motivó los Transformers."

**Slide 26 — Redes Recurrentes (RNNs): intuición.** "Quiero procesar: 'The cat is on the _'"
- "Red neuronal común: recibe el vector de 'The' y genera un output, luego recibe el vector de 'cat' y genera un output. Pero el output de 'cat' va a ser siempre el mismo! Porque no tiene 'memoria'."
- "RNN: para procesar el vector de 'cat', guardate el vector de 'The' y usalo para generar la salida de 'cat' (aplicar este mismo proceso para toda la frase hasta llegar a la ultima palabra)."

**Slide 27 — Transformers.** "La arquitectura que cambió todo (2017). A diferencia de las RNNs, los Transformers procesan toda la secuencia de una vez, en paralelo."
- **Intuición de la Atención**: "Cuando leemos, no prestamos la misma atención a todas las palabras": `"The animal didn't cross the street because it was too tired"` → "Para entender 'it', miramos 'animal'. Eso es atención."
- "Atención permite que cada token 'mire' a todos los demás y decida cuáles son relevantes." Captura: dependencias largas (palabras separadas que se relacionan); relaciones sintácticas (sujeto-verbo-objeto); relaciones semánticas (significado, contexto).
- **Arquitectura**: "Paper original: encoder + decoder. Pero LLMs modernos (GPT, LLaMA, Claude) usan solo decoder."

**Slide 28 — Comparación de Modelos.** Tabla comparativa Word2Vec / RNNs / Transformers con Idea principal, Novedad, Pros y Contras. Preservada verbatim en `Raw / preserved excerpts`. Cierre de la slide: "Evolución: representaciones estáticas → secuenciales → contextuales con attention."

**Slide 29 — Cómo funciona un LLM.** "Cuando le mandás un mensaje a ChatGPT/Claude, internamente pasa esto:"

| 01 | 02 |
|---|---|
| Tokenización | Embeddings |
| Tu texto se divide en tokens → "¿Cómo estás?" → ["¿","Cómo","est","ás","?"] | Cada token se convierte en un vector numérico |
| 03 | 04 |
| Transformer | Vector de probabilidades |
| Los vectores pasan por muchas capas de attention | La última capa produce un vector de tamaño \|V\| |
| 05 | 06 |
| Selección | Repetición |
| Se elige un token (con algo de aleatoriedad controlada = "temperatura") | Se agrega al texto y se repite desde el paso 1 |

- "Los modelos generan texto token por token."
- "Cada vez que ves una palabra aparecer en ChatGPT, es un ciclo completo de este proceso."

**Slide 30 — Generación de Palabras — Escala LLM.** "El mismo problema de Language Modelling, pero a una escala masiva". Tabla ejemplo-juguete vs GPT-4, preservada verbatim en `Raw / preserved excerpts`. Cierres: "El concepto es exactamente el mismo: predecir la siguiente palabra." / "Lo que cambia es la escala del vocabulario, los datos y el modelo."

**Slide 31 — ¿Qué cambió?** "Muchas tareas se resuelven ahora con una sola técnica: generación de texto con modelos fundacionales (modelos grandes pre-entrenados)."
- "Si un modelo puede comprender texto y generar palabras, podemos reformular casi cualquier tarea como generación:"
  - Sentimiento: "¿Este review es positivo o negativo?" → modelo genera "positivo"
  - Traducción: "Traducí: the cat is on the mat" → modelo genera "el gato está sobre la alfombra"
  - Resumen: "Resumí este texto: [texto largo]" → modelo genera el resumen
- Cadena: "problema → prompt (instrucción en texto) → modelo genera la solución"
- "Esto es lo que hacemos cuando usamos ChatGPT, Claude, etc."

**Slide 32 — Entrenamiento vs Inferencia.** Tabla de seis filas comparando ambas fases, preservada verbatim en `Raw / preserved excerpts`. Claims de cierre:
- "Cuando usás ChatGPT, el modelo no está aprendiendo de tu conversación. Los parámetros ya están fijos. Solo está haciendo inference."
- "Entrenar un modelo grande requiere billones de palabras y miles de GPUs durante semanas. Por eso muy pocas empresas lo hacen."

## Definitions and terminology

Todas las definiciones en la formulación propia del deck.

- **Agente racional (definición de IA)** — de las notas de la slide 1: "como proponen Russell y Norvig, la IA es el diseño de agentes racionales: sistemas que perciben su entorno y toman acciones para maximizar sus posibilidades de éxito en un objetivo dado". Y en el contexto técnico: "La definición de agente racional evita el debate filosófico sobre la 'conciencia' y se centra en la función matemática que mapea secuencias de percepciones a acciones (arquitectura de agentes)." Contrapuesto a la definición intuitiva: "máquinas haciendo cosas que requerirían inteligencia si las hiciera un humano".
- **Los tipos de problema de IA (slide 3)** — 
  - *Predicción*: "Aprender X → Y a partir de datos etiquetados. Incluye clasificación y regresión."
  - *Percepción*: "Extraer estructura de señales sensoriales: imagen, audio, video."
  - *Representación*: "Aprender embeddings y espacios latentes que capturan relaciones entre datos."
  - *Decisión Secuencial*: "Maximizar recompensa acumulada. Formalizado como Reinforcement Learning."
  - *Búsqueda / Planificación*: "Encontrar la mejor secuencia de acciones en un espacio de estados."
  - *Razonamiento Simbólico*: "Manipular símbolos y reglas IF–THEN para derivar conclusiones lógicas."
  - *Generación*: "Producir nuevas muestras coherentes: texto, imagen, audio, código. Infinita cantidad de outputs."
- **Problemas clásicos de ML (slide 5)** — *Clasificación (Prediccion)*: "¿A qué categoría pertenece?"; *Regresión (Prediccion)*: "¿Qué valor va a tener?"; *Clustering (Representación)*: "¿Qué datos se parecen entre sí?"; *Generación*: "¿Puedo crear datos nuevos?".
- **Machine Learning (contraste con programación clásica)** — "El modelo aprende patrones de los datos, no se programa con reglas explícitas." La figura de la slide 4 lo formaliza: programación clásica toma Rules + Data y produce Answers; ML toma Data + Answers y produce Rules.
- **NLP (Procesamiento del Lenguaje Natural)** — "El campo que se ocupa de esto [procesar texto automáticamente] se llama Procesamiento del Lenguaje Natural (NLP)."
- **Language Modelling** — "Dado: un vocabulario V, un corpus de texto T, una frase incompleta P. El objetivo es predecir cuál es la siguiente palabra más probable." El output no es una palabra sino "un vector de probabilidades sobre todo el vocabulario", de longitud `|V|`, con "una posición por cada palabra del vocabulario" y donde "cada valor indica la probabilidad de que esa palabra sea la siguiente".
- **Parámetros ("clavijas")** — "El modelo por dentro tiene 'clavijas' (parámetros) internas que hay que ajustar para que predigan correctamente la siguiente palabra mas probable."
- **Loss (pérdida)** — "número que mide qué tan equivocado estuvo el modelo".
- **Optimización** — "proceso de ajustar los parámetros para reducir la loss". Regla de selección: "Nos quedamos con los parámetros que minimizan el error."
- **Token** — "las unidades mínimas que el modelo procesa. Cada token tendrá un vector asignado que lo identifica." "Un token puede ser: una palabra completa, parte de una palabra, o un signo de puntuación."
- **Vocabulario V** — "el conjunto completo de tokens que el modelo conoce. Por eso predice un vector de probabilidades de tamaño |V|."
- **Bag of Words / TF-IDF** — "Contar palabras. Ignora orden y significado."
- **One-Hot Encoding** — "Vector con un solo 1. No captura similitud ('cat' y 'dog' igual de lejos que 'cat' y 'refrigerator'). Cada vector canónico se corresponde con un token."
- **Embeddings** — "Vectores donde tokens con significado similar tienen vectores similares. Es lo que usan los modelos modernos." Y en la slide 17: "Embedding de texto: vector que codifica el significado de una palabra." Propiedades: cercanía semántica en el espacio, y codificación de relaciones ("el vector que me lleva de 'man' a 'woman' es el mismo que me lleva de 'king' a 'queen'").
- **Word2Vec** — "Uno de los primeros métodos para aprender embeddings automáticamente." Idea: "una palabra se define por la compañía que tiene". Funcionamiento: "Saca promedios de los vectores de las palabras que circundan a cada una en el corpus de texto en que aparece." Advertencia explícita: "Word2Vec no es un modelo de lenguaje (no genera palabras). Es un método para obtener embeddings con significado real de palabras en su contexto." Limitación al usarlo para frases: "Word2Vec saca el promedio (obs: se pierde información del orden)."
- **Perceptrón** — "El bloque fundamental de las redes neuronales — la neurona artificial más simple." Mecánica: recibe inputs numéricos, multiplica cada uno por un peso, suma los productos más un bias, y pasa el resultado por una función de activación. `output = activación( x₁·w₁ + x₂·w₂ + x₃·w₃ + bias )`. "Los pesos y el bias son los parámetros que el modelo aprende durante el entrenamiento."
- **Bias** — "valor de ajuste"; en la analogía de decisión, "tu predisposición inicial".
- **Deep Learning / red neuronal profunda** — resultado de "apilar muchas capas de perceptrones": "Obtenemos una red neuronal profunda — de ahí viene el nombre Deep Learning." Jerarquía de abstracción por capas (iniciales → simples; intermedias → complejas; finales → conceptos de alto nivel).
- **Gradient descent (descenso de gradiente)** — proceso iterativo de ejemplo → predicción → comparación → loss → ajuste "un poquito en la dirección que más reduce la loss (-∇)" → repetición. Analogía de la montaña con niebla, bajando hacia el valle.
- **Learning rate** — "tamaño del paso: muy grande → te pasás, muy chico → tardás una eternidad."
- **Backpropagation** — "El error se propaga hacia atrás, calculando cuánto contribuyó cada peso" y "cada peso se ajusta proporcionalmente a su contribución al error". Formalmente: "una forma de aplicar la regla de la cadena (sacar el gradiente de una composición de funciones), en una red neuronal." Prerrequisito: "en el fondo una red neuronal es una función 'diferenciable' (aproximadamente)".
- **Forward pass** — "El input viaja hacia adelante por la red hasta producir una predicción."
- **Backward pass** — "El error se propaga hacia atrás, calculando cuánto contribuyó cada peso."
- **RNN (Red Recurrente)** — procesa "texto palabra por palabra, de izquierda a derecha, manteniendo un estado interno ('memoria')". Contraste con red común: "el output de 'cat' va a ser siempre el mismo! Porque no tiene 'memoria'."
- **LSTM** — "decide qué recordar/olvidar".
- **GRU** — "simplificada".
- **ELMo** — "embeddings contextuales"; en la tabla de la slide 28 aparece como construido sobre RNNs ("Base de modelos como ELMo").
- **Attention (atención)** — "Atención permite que cada token 'mire' a todos los demás y decida cuáles son relevantes." Intuición: "Cuando leemos, no prestamos la misma atención a todas las palabras."
- **Transformer** — "La arquitectura que cambió todo (2017). A diferencia de las RNNs, los Transformers procesan toda la secuencia de una vez, en paralelo." Arquitectura: "Paper original: encoder + decoder. Pero LLMs modernos (GPT, LLaMA, Claude) usan solo decoder."
- **Temperatura** — definida de pasada en la slide 29 dentro del paso "Selección": "Se elige un token (con algo de aleatoriedad controlada = 'temperatura')."
- **Modelos fundacionales** — "modelos grandes pre-entrenados" (slide 31).
- **Prompt** — "instrucción en texto"; la cadena completa es "problema → prompt (instrucción en texto) → modelo genera la solución".
- **Entrenamiento** — "Aprende ajustando parámetros"; ocurre "antes de estar disponible"; los parámetros "se modifican constantemente".
- **Inferencia** — "Usa parámetros ya aprendidos"; ocurre "cada vez que un usuario pregunta"; los parámetros "están congelados (no cambian)".

## Evidence and examples

- **Corpus juguete de Language Modelling (slides 10–11)** — `V` de 14 tokens: `{ "a", "to", "on", "the", "sat", "cat", "dog", "bed", "ran", "mat", " ", "<fin>", ".", "," }`. `T` de 5 frases: "the cat sat on mat", "a dog ran to bed", "the dog sat on bed", "a cat ran to mat", "the cat ran to dog". `P = "the dog sat on"`. La palabra correcta corresponde a `T[2] = "bed"`; el vector objetivo es one-hot en la posición de "bed". Salida del modelo: `bed: 0.78` como valor dominante, con `the: 0.04` y `mat: 0.04` segundos, y `<fin>`, `"."`, `","` en 0.00. (Vector completo en `Raw / preserved excerpts`.)
- **Ejemplos de análisis de sentimiento (slide 6)** — "Qué bien comimos en el restaurante" → positivo; "No vuelvo nunca más a comer" → negativo.
- **Predicción vs generación con la misma frase (slide 6)** — Predicción: `The ___ is on the mat` → `cat`. Generación: `The cat is on the ___` → `mat`.
- **Ambigüedad de "it" (slides 25 y 27)** — `"The animal didn't cross the street because it was too tired"`. En la slide 25 es la evidencia de la limitación de las RNNs: "¿A qué se refiere 'it'? A 'animal'. Pero están lejos en la oración. Para cuando la RNN llega a 'it', la info sobre 'animal' se debilitó → motivó los Transformers." En la slide 27 es el mismo ejemplo reutilizado como intuición positiva de attention: "Para entender 'it', miramos 'animal'. Eso es atención." El deck usa deliberadamente el mismo ejemplo dos veces, como problema y como solución.
- **Tokenización palabra vs sub-palabra (slide 15)** — `"the cat sat on the mat"` → `["the", "cat", "sat", "on", "the", "mat"]` (6 tokens); `"unbelievable"` → `["un", "believ", "able"]` (3 tokens).
- **Tokenización en español con puntuación (slide 29)** — `"¿Cómo estás?"` → `["¿","Cómo","est","ás","?"]` (5 tokens; nótese que "estás" se parte en dos sub-palabras y los signos de interrogación son tokens propios).
- **Analogía vectorial man→woman :: king→queen (slide 17)** — "el vector que me lleva de 'man' a 'woman' es el mismo que me lleva de 'king' a 'queen'". Restatement aritmético en la slide 28: "(rey - hombre + mujer ≈ reina)". Las figuras `slide-17-1.jpg` y `slide-17-2.jpg` lo muestran gráficamente, y `slide-17-1.jpg` agrega dos analogías más: tiempo verbal (walking→walked, swimming→swam) y país-capital (Italy→Rome, Spain→Madrid, Canada→Ottawa, Turkey→Ankara, Russia→Moscow, Germany→Berlin, Japan→Tokyo, China→Beijing, Vietnam→Hanoi).
- **Traza de una RNN (slide 25)** — `"El" → actualiza estado → "gato" → actualiza estado → "está" → ...`
- **Frase de trabajo de la slide 26** — `"The cat is on the _"`.
- **Ejemplo de entrenamiento en español (slide 13)** — Input: "El gato está en la"; la palabra más probable era "alfombra".
- **Tabla de escala: ejemplo juguete vs GPT-4 (slide 30)** — Vocabulario: 14 palabras vs ~100.000 tokens. Corpus: 5 frases vs "billones de palabras (internet, libros, código, papers...)". Parámetros: "pocos" vs "cientos de miles de millones". Entrenamiento: segundos vs "meses en miles de GPUs". Frase P: "the dog sat on" vs "cualquier texto, de cualquier largo".
- **Costo de entrenamiento vs inferencia (slide 32)** — Entrenamiento: "Millones de dólares, semanas". Inferencia: "Fracción de segundo por respuesta".
- **Ejemplos de reformulación como generación (slide 31)** — Sentimiento, traducción ("Traducí: the cat is on the mat" → "el gato está sobre la alfombra") y resumen, todos como prompts.
- **Caso combinado de la slide 3** — "Un auto autónomo combina percepción + decisión secuencial + planificación."
- **Modelos nombrados a lo largo del deck** — GPT-4, Claude, LLaMA (slides 19, 27, 29, 30, 32); ChatGPT (slides 29, 30, 31, 32); OpenAI, Anthropic, Meta como entrenadores (slide 32).

## Inconsistencies / open questions

- **31 de 32 slides tienen las notas del orador vacías.** Solo la slide 1 trae notas (y son extensas: discurso sugerido + contexto técnico + enlace recomendado). El resto del deck no tiene guión hablado, así que toda la narración de las clases 2 a 32 hay que reconstruirla desde el contenido visible.
- **Typo en el título de la slide 4**: "Machine Learning: Cómo funciona la IA moAderna" (una "A" espuria dentro de "moderna").
- **El "paper original" del Transformer se referencia sin citación** (slide 27: "Paper original: encoder + decoder"). No se nombra *Attention Is All You Need* ni a Vaswani et al., ni se da año de publicación en esa línea — el "(2017)" aparece solo en el encabezado de la slide. La figura `slide-27-1.jpg` es la figura 1 de ese paper, reproducida sin atribución en la slide.
- **LSTM, GRU y ELMo se nombran sin papers ni referencias** (slide 25 y slide 28). Tampoco se explica en qué consiste la "simplificación" del GRU, ni qué hace a ELMo "contextual" frente a Word2Vec.
- **Word2Vec tampoco lleva citación** (Mikolov et al. no aparece), pese a ser el método sobre el que se apoya toda la sección de embeddings.
- **Conteo de tipos de problema en la slide 3.** El brief describe "los 8 tipos de problema de IA", pero la slide nombra siete categorías (Predicción, Percepción, Representación, Decisión Secuencial, Búsqueda/Planificación, Razonamiento Simbólico, Generación) e incluye ocho imágenes — la octava (`slide-03-8.png`) es un icono de callout decorativo, no una categoría. Conviene resolver si la intención era 7 u 8 antes de reutilizar el material.
- **La slide 22 no tiene título propio**; el encabezado "Ciclo de Entrenamiento en Machine Learning" vive en el cuerpo como texto en negrita.
- **Discrepancia entre "palabra" y "token".** El deck usa las dos casi intercambiablemente ("predecir la siguiente palabra", "vector de probabilidades sobre el vocabulario", "|V|"), pese a haber establecido en las slides 15–16 que la unidad real es el token sub-palabra. En la tabla de la slide 30 la fila "Vocabulario V" mezcla las dos: "14 palabras" en una columna y "~100.000 tokens" en la otra.
- **"Billones" es ambiguo** (slides 30 y 32: "billones de palabras"). En español rioplatense un billón es 10¹²; el original probablemente traduce "billions" (10⁹) del inglés. Vale aclararlo si el número se usa en clase.
- **Errores de acentuación / ortografía menores en el original**: "Prediccion" sin tilde (slide 5, dos veces), "Ultima Modification" (slide 1, mezcla de español e inglés), "mas" sin tilde (slides 13, 26), "Como" sin tilde (slide 5).
- **La afirmación "Word2Vec saca el promedio" para representar una frase** (slide 18) es una simplificación fuerte: Word2Vec produce embeddings por palabra, y el promedio es una técnica de agregación aplicada encima, no parte del método. El deck lo nota al pasar ("obs: se pierde información del orden") pero no lo separa conceptualmente.
- **Slide 13, paso 03**: "Comparación: la palabra mas probable era 'alfombra'." La redacción confunde la palabra *correcta* del corpus con la *más probable* según el modelo — que es justamente lo que se está comparando. Los pasos 03 y 04 arrastran la misma ambigüedad.
- **Slides sin contenido textual propio** (4, 20, 24): dependen enteramente de su figura. Si la figura no se reproduce, la slide se pierde. La slide 27 depende parcialmente de lo mismo.
- **Cobertura de la agenda**: la agenda (slide 2) anuncia "Transformers: Cómo funciona un LLM" como bloque final, pero el deck cierra en entrenamiento vs inferencia sin abordar fine-tuning, RLHF, alucinaciones ni ninguna aplicación biomédica concreta — pese a que el curso es "Aplicada en Biomedicina". El único gancho biomédico del deck son dos ejemplos sueltos (agrupar pacientes con síntomas similares, slide 5; analizar opiniones de pacientes sobre un tratamiento y las historias clínicas, slide 7).
- **`_manifest.json` no trae alt text.** Los campos por imagen son `slide`, `file`, `shape` (nombre genérico tipo "Image 0"), `w_emu` y `h_emu`. No hay texto alternativo original que preservar, así que toda la descripción de imágenes de este registro es transcripción de Fase 2, no metadata heredada.

## Images / diagrams

> **Nueve figuras se retiraron del disco el 2026-09-03** — `slide-18-1.jpg` (perceptrón), `slide-22-1.jpg` (ciclo de entrenamiento) y `slide-24-1.jpg` (retropropagación); y `slide-26-1.jpg` (red recurrente contra red directa); `slide-04-1.jpg`, `slide-05-2.jpg`, `slide-05-3.png`, `slide-05-4.jpg` y `slide-17-2.jpg`, esquemas planos rotulados en inglés, dos de ellos con marca de un tercero y uno que era una miniatura de video. Se rehicieron reproduciendo el mecanismo y nunca la marca. Eran diagramas planos y simples, rotulados en inglés, y una traía marca gráfica de un tercero. Se rehicieron como diagramas ASCII propios del deck, en español y con la paleta de la materia; la del perceptrón además incorpora el sesgo, que la figura original omitía. Las descripciones y transcripciones de abajo se conservan como registro de qué mostraban. Los originales siguen en `talksmith-aig4b`.


30 imágenes, todas copiadas byte a byte desde `research/articles/AIG4B-Clase-2-LLM-media/`. Los tamaños en pantalla citados vienen de `_manifest.json` (EMU; 914400 EMU = 1 pulgada).

---

### `AIG4B-Clase-2-LLM.md/images/slide-01-1.png`
- **Provenance**: Slide 1 (portada), shape "Image 0", 1198235 × 990302 EMU (~1,31 × 1,08 in).
- **Depiction**: Logotipo institucional de la Universidad Austral en azul marino sobre fondo blanco. Un sello ovalado con la leyenda circular y, dentro, un árbol estilizado con cuatro estrellas sobre el follaje; debajo del sello, el nombre de la universidad en dos líneas.
- **Why it matters**: Marca institucional de la portada. Sin contenido conceptual; identifica al emisor del material.
- **Transcribed text**: (en latín, en el sello) "STVDIORVM · AVSTRALIS · VNIVERSITAS ·" — (debajo) "UNIVERSIDAD" / "AUSTRAL".

### `AIG4B-Clase-2-LLM.md/images/slide-03-1.png`
- **Provenance**: Slide 3 (taxonomía de problemas de IA), shape "Image 0", 302411 × 302419 EMU (~0,33 in cuadrado).
- **Depiction**: Icono decorativo de sección, línea roja sobre transparente: una bola de cristal sobre su base. Acompaña a la categoría **Predicción**. No se describe en más detalle.
- **Why it matters**: Marcador visual de categoría; sin contenido propio.
- **Transcribed text**: (ninguno).

### `AIG4B-Clase-2-LLM.md/images/slide-03-2.png`
- **Provenance**: Slide 3, shape "Image 1", 302411 × 302419 EMU.
- **Depiction**: Icono decorativo de sección, línea roja: dos ojos vistos de frente. Acompaña a la categoría **Percepción**.
- **Why it matters**: Marcador visual de categoría; sin contenido propio.
- **Transcribed text**: (ninguno).

### `AIG4B-Clase-2-LLM.md/images/slide-03-3.png`
- **Provenance**: Slide 3, shape "Image 2", 302411 × 302419 EMU.
- **Depiction**: Icono decorativo de sección, línea roja: una pieza de rompecabezas cuadrada. Acompaña a la categoría **Representación**.
- **Why it matters**: Marcador visual de categoría; sin contenido propio.
- **Transcribed text**: (ninguno).

### `AIG4B-Clase-2-LLM.md/images/slide-03-4.png`
- **Provenance**: Slide 3, shape "Image 3", 302411 × 302419 EMU.
- **Depiction**: Icono decorativo de sección, línea roja: un joystick / control de videojuego con cruceta y cuatro botones. Acompaña a la categoría **Decisión Secuencial** (reinforcement learning).
- **Why it matters**: Marcador visual de categoría; sin contenido propio.
- **Transcribed text**: (ninguno).

### `AIG4B-Clase-2-LLM.md/images/slide-03-5.png`
- **Provenance**: Slide 3, shape "Image 4", 302411 × 302419 EMU.
- **Depiction**: Icono decorativo de sección, línea roja: un organigrama / árbol de tres nodos hijos colgando de un nodo raíz. Acompaña a la categoría **Búsqueda / Planificación** (espacio de estados).
- **Why it matters**: Marcador visual de categoría; sin contenido propio.
- **Transcribed text**: (ninguno).

### `AIG4B-Clase-2-LLM.md/images/slide-03-6.png`
- **Provenance**: Slide 3, shape "Image 5", 302411 × 302419 EMU.
- **Depiction**: Icono decorativo de sección, línea roja: un cerebro visto de frente, con los dos hemisferios. Acompaña a la categoría **Razonamiento Simbólico**.
- **Why it matters**: Marcador visual de categoría; sin contenido propio.
- **Transcribed text**: (ninguno).

### `AIG4B-Clase-2-LLM.md/images/slide-03-7.png`
- **Provenance**: Slide 3, shape "Image 6", 302411 × 302419 EMU.
- **Depiction**: Icono decorativo de sección, línea roja: tres destellos / sparkles (uno grande y dos chicos). Acompaña a la categoría **Generación** — es el icono convencional de IA generativa.
- **Why it matters**: Marcador visual de categoría; sin contenido propio.
- **Transcribed text**: (ninguno).

### `AIG4B-Clase-2-LLM.md/images/slide-03-8.png`
- **Provenance**: Slide 3, shape "Image 7", 189007 × 151209 EMU (~0,21 × 0,17 in) — el más chico del deck (463 bytes).
- **Depiction**: Icono decorativo diminuto: un rectángulo redondeado en rojo oscuro con la esquina inferior derecha doblada, tipo marcador de nota. Acompaña al callout "💡 Un auto autónomo combina percepción + decisión secuencial + planificación".
- **Why it matters**: Viñeta de callout. Sin contenido propio. Es el mismo glifo que reaparece en las slides 7, 9, 10, 18, 19 y 21.
- **Transcribed text**: (ninguno).

### `AIG4B-Clase-2-LLM.md/images/slide-04-1.jpg`
- **Provenance**: Slide 4 ("Machine Learning: Cómo funciona la IA moAderna"), shape "Image 0", 7077394 × 4260652 EMU (~7,74 × 4,66 in) — figura a pantalla completa; es el único contenido de la slide.
- **Depiction**: **Figura en inglés.** Diagrama de dos filas que contrasta el paradigma clásico con el de machine learning. Fila superior: dos círculos de entrada — "Rules" (naranja) y "Data" (celeste) — con flechas grises hacia una caja gris rotulada "Classical Programming" (icono de monitor con `</>`), y desde ahí una flecha hacia un círculo azul oscuro "Answers". Fila inferior: los círculos de entrada son "Data" (celeste) y "Answers" (azul oscuro), apuntan a una caja gris "Machine Learning" (icono de cerebro dentro de un engranaje), y la salida es un círculo naranja "Rules". La inversión de qué es entrada y qué es salida es todo el argumento.
- **Why it matters**: Es la formalización visual de la claim central de la sección: "El modelo aprende patrones de los datos, no se programa con reglas explícitas" (slide 5). Como la slide 4 no tiene texto propio, esta figura *es* la slide.
- **Transcribed text**: "Rules" · "Data" · "Classical Programming" · "Answers" · "Data" · "Answers" · "Machine Learning" · "Rules".

### `AIG4B-Clase-2-LLM.md/images/slide-05-1.png`
- **Provenance**: Slide 5 (problemas clásicos de ML), shape "Image 0", 3440126 × 1184176 EMU (~3,76 × 1,29 in).
- **Depiction**: **Figura en español.** Diagrama de clasificación de imágenes bajo el título "Clasificación de Imágenes": una foto de un gato naranja sobre pasto, una flecha azul, una caja negra rotulada "Modelo", otra flecha azul, y la etiqueta de salida "CAT". Todo dentro de un marco rectangular de borde fino.
- **Why it matters**: Ilustra el bullet "Clasificación (Prediccion) → ¿A qué categoría pertenece?". Nótese que la etiqueta de salida está en inglés ("CAT") mientras el título está en español.
- **Transcribed text**: "Clasificación de Imágenes" · "Modelo" · "CAT".

### `AIG4B-Clase-2-LLM.md/images/slide-05-2.jpg`
- **Provenance**: Slide 5, shape "Image 1", 1968153 × 1463080 EMU (~2,15 × 1,60 in).
- **Depiction**: **Figura en inglés.** Scatter plot de regresión lineal, capturado de un video o curso. Título "Use a **linear** regression model" (con "linear" en negrita). Ejes magenta: vertical rotulado "y" con la leyenda "price ($)"; horizontal rotulado "x" con la leyenda "square feet (sq.ft.)". Unos quince puntos celestes dispersos y una recta verde ajustada que los atraviesa con pendiente positiva. Anotación arriba: "Fit a line through the data". Un clipart de casa verde se superpone al final del eje x.
- **Why it matters**: Ilustra el bullet "Regresión (Prediccion) → ¿Qué valor va a tener? (ej: ¿cuánto va a costar esta casa?)" — el ejemplo de la casa del deck y el de la figura coinciden.
- **Transcribed text**: "Use a **linear** regression model" · "Fit a line through the data" · "y" · "price ($)" · "x" · "square feet (sq.ft.)".

### `AIG4B-Clase-2-LLM.md/images/slide-05-3.png`
- **Provenance**: Slide 5, shape "Image 2", 3034926 × 1426369 EMU (~3,32 × 1,56 in).
- **Depiction**: **Figura en inglés.** Diagrama sobre fondo crema titulado "Topic Modeling working", con el logo de GeeksforGeeks arriba a la derecha. De izquierda a derecha: una pila de tres cuadrados rosados rotulada "Collection of Text Documents", una flecha hacia una caja de borde oscuro "Topic Modelling", y desde ahí dos flechas de salida. La de arriba lleva a tres elipses solapadas (verde oliva, turquesa, rosa) llenas de puntos, rotuladas "Cluster of Word by Topic". La de abajo lleva a un cuadro con puntos de colores agrupados por zona más una leyenda de cuatro barras de color, rotulado "Cluster of Document by Topic".
- **Why it matters**: Ilustra el bullet "Clustering (Representación) → ¿Qué datos se parecen entre sí?" y conecta con el ejemplo "Descubrir tópicos en un corpus (topic modeling)" de la tabla de la slide 8.
- **Transcribed text**: "Topic Modeling working" · "Collection of Text Documents" · "Topic Modelling" · "Cluster of Word by Topic" · "Cluster of Document by Topic".

### `AIG4B-Clase-2-LLM.md/images/slide-05-4.jpg`
- **Provenance**: Slide 5, shape "Image 3", 2728943 × 1535509 EMU (~2,98 × 1,68 in).
- **Depiction**: **Figura en inglés.** Miniatura de video sobre fondo negro con el título "Text Generation" en serif blanca. Abajo a la izquierda, la frase incompleta troceada en tokens con recuadros grises y letras naranjas: "It" "rains" "a" "lot" "in" "the". Una flecha naranja curva apunta hacia la silueta de una cabeza humana verde menta con engranajes dentro, rotulada "AI". Otra flecha naranja sale hacia la derecha, hacia un gráfico de barras horizontales de candidatos con sus etiquetas: "UK", "winter", "summer", "Pacific", "mountain" — las barras (degradé celeste-turquesa) tienen longitudes distintas, siendo "winter" la más larga y "mountain" la más corta.
- **Why it matters**: Es la ilustración más literal del problema de Language Modelling de toda la clase — frase incompleta + modelo + distribución de probabilidad sobre candidatos — y aparece ya en la slide 5, antes de que el concepto se formalice en las slides 10–11. Ilustra el bullet "Generación → ¿Puedo crear datos nuevos?".
- **Transcribed text**: "Text Generation" · "It" "rains" "a" "lot" "in" "the" · "AI" · "UK" · "winter" · "summer" · "Pacific" · "mountain".

### `AIG4B-Clase-2-LLM.md/images/slide-07-1.png`
- **Provenance**: Slide 7 (¿Por qué procesar texto automáticamente?), shape "Image 0", 224427 × 179487 EMU (~0,25 × 0,20 in), 546 bytes.
- **Depiction**: Icono decorativo diminuto: rectángulo redondeado rojo oscuro con la esquina inferior derecha doblada (viñeta de callout). Mismo glifo que `slide-03-8.png`.
- **Why it matters**: Viñeta que marca el cierre "El campo que se ocupa de esto se llama Procesamiento del Lenguaje Natural (NLP)". Sin contenido propio.
- **Transcribed text**: (ninguno).

### `AIG4B-Clase-2-LLM.md/images/slide-09-1.png`
- **Provenance**: Slide 9 (¿Cómo se resolvían estos problemas?), shape "Image 0", 236234 × 189012 EMU (~0,26 × 0,21 in), 594 bytes.
- **Depiction**: Icono decorativo diminuto: el mismo rectángulo redondeado rojo oscuro con esquina doblada. **No** es un diagrama de pipeline — pese al tamaño en pantalla podría esperarse una figura, pero el archivo es la viñeta de callout.
- **Why it matters**: Viñeta que marca el bloque "Un modelo para sentimiento, otro para traducción, otro para NER... / Era costoso y lento." Sin contenido propio.
- **Transcribed text**: (ninguno).

### `AIG4B-Clase-2-LLM.md/images/slide-10-1.png`
- **Provenance**: Slide 10 (Modelos de Generación de Palabras), shape "Image 0", 200814 × 160635 EMU (~0,22 × 0,18 in), 530 bytes.
- **Depiction**: Icono decorativo diminuto: mismo rectángulo redondeado rojo oscuro con esquina doblada. No contiene el diagrama del vector de probabilidades.
- **Why it matters**: Viñeta que marca el bloque "Importante" sobre el vector de probabilidades de tamaño |V|. Sin contenido propio.
- **Transcribed text**: (ninguno).

### `AIG4B-Clase-2-LLM.md/images/slide-17-1.jpg`
- **Provenance**: Slide 17 (Embedding de Texto), shape "Image 0", 4452628 × 1697534 EMU (~4,87 × 1,86 in) — la figura principal de la slide.
- **Depiction**: **Figura en inglés.** Tres paneles de ejes 3D (fondo blanco, ejes negros en perspectiva) que muestran analogías vectoriales, cada uno con su rótulo debajo.
  - Panel izquierdo, "Male-Female": cuatro puntos con flechas punteadas paralelas — "man" (azul) → "woman" (violeta) arriba, y "king" (azul) → "queen" (violeta) abajo. Las dos flechas tienen la misma dirección y longitud, que es exactamente la claim de la slide.
  - Panel central, "Verb Tense": "walking" (amarillo) → "walked" (rojo) y "swimming" (amarillo) → "swam" (rojo), con flechas punteadas naranjas paralelas.
  - Panel derecho, "Country-Capital": nueve pares país (marrón) → capital (verde), con flechas punteadas grises todas paralelas — Italy→Rome, Spain→Madrid, Canada→Ottawa, Turkey→Ankara, Russia→Moscow, Germany→Berlin, Japan→Tokyo, China→Beijing, Vietnam→Hanoi.
- **Why it matters**: Sostiene visualmente la claim más fuerte de la sección de embeddings — "el vector que me lleva de 'man' a 'woman' es el mismo que me lleva de 'king' a 'queen'" — y la generaliza a dos relaciones más (morfológica y factual), mostrando que la regularidad no es un accidente del ejemplo de género.
- **Transcribed text**: "man" · "woman" · "king" · "queen" · "Male-Female" · "walking" · "walked" · "swimming" · "swam" · "Verb Tense" · "Italy" · "Rome" · "Spain" · "Madrid" · "Canada" · "Ottawa" · "Turkey" · "Ankara" · "Russia" · "Moscow" · "Germany" · "Berlin" · "Japan" · "Tokyo" · "China" · "Beijing" · "Vietnam" · "Hanoi" · "Country-Capital".

### `AIG4B-Clase-2-LLM.md/images/slide-17-2.jpg`
- **Provenance**: Slide 17, shape "Image 1", 4452628 × 1488480 EMU (~4,87 × 1,63 in).
- **Depiction**: **Figura en inglés.** Diagrama de tres bloques unidos por flechas huecas. Bloque 1, rotulado "Words": una caja con cuatro palabras entrecomilladas, cada una en su color — "queen" (rojo), "king" (azul), "man" (verde), "woman" (naranja). Bloque 2, titulado "Word Embeddings" en azul negrita: una matriz de 4 filas × 6 columnas entre corchetes, cada fila del color de su palabra —
  - `[0.1  0.2  0.7  0.3  0.2  0.8]` (queen, rojo)
  - `[0.8  0.5  0.1  0.9  0.7  0.2]` (king, azul)
  - `[0.5  0.6  0.3  0.2  0.4  0.1]` (man, verde)
  - `[0.9  0.8  0.4  0.1  0.1  0.2]` (woman, naranja)
  
  Bloque 3: ejes 3D con cuatro puntos rotulados — "king" (azul) y "man" (verde) a la izquierda/arriba, "queen" (rojo) y "woman" (naranja) a la derecha/abajo, con dos flechas celestes gruesas y paralelas king→queen y man→woman.
- **Why it matters**: Cierra el circuito palabra → vector numérico → posición en el espacio, que es justo el paso que la slide 16 plantea como necesario ("Hay que convertir los tokens en números…"). Los valores numéricos son ilustrativos, no reales.
- **Transcribed text**: "Words" · "queen" · "king" · "man" · "woman" · "Word Embeddings" · "[0.1 0.2 0.7 0.3 0.2 0.8]" · "[0.8 0.5 0.1 0.9 0.7 0.2]" · "[0.5 0.6 0.3 0.2 0.4 0.1]" · "[0.9 0.8 0.4 0.1 0.1 0.2]" · "king" · "man" · "queen" · "woman".

### `AIG4B-Clase-2-LLM.md/images/slide-17-3.png`
- **Provenance**: Slide 17, shape "Image 2", 3273542 × 3328988 EMU (~3,58 × 3,64 in) — la más grande de la slide y casi cuadrada.
- **Depiction**: **Figura sin texto léxico** (solo números en los ejes). Plano cartesiano 2D con ejes azules, marcados 0, 0.5 y 1 en ambos ejes. Cuatro vectores azules parten del origen y terminan en emojis en vez de puntos: un rey coronado (~0.35, 0.62) y una reina coronada (~0.52, 0.68) arriba, y una manzana (~0.20, 0.22) y una banana (~0.37, 0.20) abajo. Los dos pares quedan agrupados por región del plano.
- **Why it matters**: Ilustra la primera propiedad de los embeddings de la slide 17 — "Palabras relacionadas y con significados similares se encuentran 'cercanos' en el espacio" — con dos clusters semánticos evidentes (realeza vs frutas). Al usar emojis en lugar de etiquetas, funciona en cualquier idioma.
- **Transcribed text**: "0" · "0.5" · "1" (en ambos ejes). Sin otro texto.

### `AIG4B-Clase-2-LLM.md/images/slide-18-1.jpg`
- **Provenance**: Slide 18 (Redes Neuronales: Perceptrón), shape "Image 0", 3251615 × 1625798 EMU (~3,56 × 1,78 in).
- **Depiction**: **Figura en inglés.** Diagrama canónico del perceptrón sobre fondo gris muy claro. A la izquierda, tres círculos blancos de entrada apilados — "X₁", "X₂" y (tras una línea punteada vertical que indica omisión) "Xₙ" — bajo el rótulo "Inputs". De cada uno sale una flecha negra rotulada con su peso: "w₁", "w₂", "wₙ", bajo el rótulo "Weights". Las tres flechas convergen en un círculo verde claro con el símbolo de sumatoria "Σ", titulado "Weighted Sum". De ahí una flecha va a un segundo círculo verde claro con una curva sigmoide, titulado "Activation Function". La flecha final sale hacia "ŷ", bajo el rótulo "Output".
- **Why it matters**: Es el diagrama exacto de la fórmula que la slide escribe en texto — `output = activación( x₁·w₁ + x₂·w₂ + x₃·w₃ + bias )` — con una diferencia notable: **la figura no muestra el bias**, que el texto sí menciona como parámetro aprendido. Vale señalarlo al explicar.
- **Transcribed text**: "X₁" · "X₂" · "Xₙ" · "Inputs" · "w₁" · "w₂" · "wₙ" · "Weights" · "Weighted Sum" · "Σ" · "Activation Function" · "Output" · "ŷ".

### `AIG4B-Clase-2-LLM.md/images/slide-18-2.png`
- **Provenance**: Slide 18, shape "Image 1", 354401 × 283468 EMU (~0,39 × 0,31 in), 928 bytes.
- **Depiction**: Icono decorativo: rectángulo redondeado rojo oscuro con esquina inferior derecha doblada. Mismo glifo de callout que en las slides 3, 7, 9, 10, 19 y 21, apenas más grande.
- **Why it matters**: Viñeta que marca el bloque "En NLP:" sobre cómo obtener x₁,…,xₙ de una frase. Sin contenido propio.
- **Transcribed text**: (ninguno).

### `AIG4B-Clase-2-LLM.md/images/slide-19-1.png`
- **Provenance**: Slide 19 (Redes Neuronales Profundas), shape "Image 0", 212620 × 170061 EMU (~0,23 × 0,19 in), 527 bytes.
- **Depiction**: Icono decorativo diminuto: el mismo rectángulo redondeado rojo oscuro con esquina doblada. **No** es un diagrama de MLP — la slide 19 no tiene figura sustantiva; el MLP aparece recién en la slide 20.
- **Why it matters**: Viñeta que marca el cierre "Los modelos de lenguaje modernos tienen miles de millones de parámetros (GPT-4, Claude, LLaMA)". Sin contenido propio.
- **Transcribed text**: (ninguno).

### `AIG4B-Clase-2-LLM.md/images/slide-20-1.jpg`
- **Provenance**: Slide 20 (Arquitectura de Red Neuronal Profunda), shape "Image 0", 8694917 × 4347567 EMU (~9,51 × 4,75 in) — la figura más grande del deck; es el único contenido de la slide.
- **Depiction**: **Figura en inglés.** Diagrama completo de un perceptrón multicapa, titulado "Deep Neural Network Architecture (Multi-Layer Perceptron)". De izquierda a derecha:
  - "Input Layer": cinco círculos blancos — x₁, x₂, x₃, ⋮, x_m — bajo el rótulo "Inputs".
  - Las conexiones hacia la primera capa oculta están rotuladas con pesos superindicados por capa: w⁽¹⁾₁,₁ · w⁽¹⁾₁,₂ · w⁽¹⁾₁,₃ · w⁽¹⁾₃,₄ · w⁽¹⁾ₙ,₁ · w⁽¹⁾ₘ,₂ · w⁽¹⁾ₘ,₁ · w⁽¹⁾ₘ,ₙ, bajo el rótulo "Weights".
  - Primera capa oculta: cinco círculos verdes con "Σ∫" (sumatoria + activación), titulada "Weighted Sum & Activation (Layer 1)".
  - Segunda capa oculta: cuatro círculos verdes "Σ∫" con puntos suspensivos, titulada "Weighted Sum & Activation (Layer 2)"; pesos rotulados w⁽²⁾₁,₁ · w⁽²⁾₁,₂ · w⁽²⁾₂,₄ · w⁽²⁾ₙ,₁ · w⁽²⁾ₙ,₃ · w⁽²⁾ₙ,ₚ.
  - Elipsis horizontales ("· · ·") indicando capas omitidas, luego "Hidden Layer k" con cuatro nodos "Σ∫".
  - "Output Layer": un único nodo verde "Σ∫" que emite una flecha a "ŷ", bajo "Output", con la aclaración "(e.g., probability of class A)".
  - Arriba a la derecha, un esquema compacto de cajas encadenadas: "Input → Layer 1 → Layer 2 → · · · → Layer k → Output", rotulado "Deep Neural Network".
- **Why it matters**: Materializa la claim de la slide 19 ("¿Qué pasa si apilamos muchas capas de perceptrones?"): cada nodo verde es el perceptrón de la slide 18 repetido, y el esquema compacto de arriba a la derecha da la lectura de alto nivel. Los subíndices de los pesos muestran por qué el conteo de parámetros explota con la profundidad.
- **Transcribed text**: "Deep Neural Network Architecture (Multi-Layer Perceptron)" · "Input Layer" · "Inputs" · "Weights" · "x₁" "x₂" "x₃" "x_m" · "Weighted Sum & Activation (Layer 1)" · "Weighted Sum & Activation (Layer 2)" · "Hidden Layer k" · "Output Layer" · "Output" · "ŷ" · "(e.g., probability of class A)" · "Input" "Layer 1" "Layer 2" "Layer k" "Output" · "Deep Neural Network" · pesos: "w⁽¹⁾₁,₁" "w⁽¹⁾₁,₂" "w⁽¹⁾₁,₃" "w⁽¹⁾₃,₄" "w⁽¹⁾ₙ,₁" "w⁽¹⁾ₘ,₂" "w⁽¹⁾ₘ,₁" "w⁽¹⁾ₘ,ₙ" "w⁽²⁾₁,₁" "w⁽²⁾₁,₂" "w⁽²⁾₂,₄" "w⁽²⁾ₙ,₁" "w⁽²⁾ₙ,₃" "w⁽²⁾ₙ,ₚ" · "Σ∫" (en cada nodo oculto y de salida).

### `AIG4B-Clase-2-LLM.md/images/slide-21-1.jpg`
- **Provenance**: Slide 21 (descenso de gradiente), shape "Image 0", 3003574 × 2434332 EMU (~3,28 × 2,66 in).
- **Depiction**: **Figura casi sin texto** (solo un número). Superficie 3D de pérdida (loss landscape) renderizada como malla de alambre con degradé de color por altura: rojo en los picos, pasando por naranja, amarillo y verde, hasta azul en los valles. Debajo, proyectado sobre un plano horizontal, el mapa de curvas de nivel correspondiente. Una trayectoria negra continua arranca en un punto marcado cerca de la cima roja y desciende serpenteando por la ladera hasta terminar con una punta de flecha en el fondo azul de un valle. Un círculo blanco sobre la trayectoria lleva el número "04".
- **Why it matters**: Es la contraparte visual literal de la analogía de la slide 21 — "estás en la cima de una montaña con niebla y querés llegar al valle (mínima loss)". La superficie con varios valles azules deja ver, sin decirlo, que hay mínimos locales; el deck no menciona ese punto.
- **Transcribed text**: "04". Sin otro texto.

### `AIG4B-Clase-2-LLM.md/images/slide-21-2.png`
- **Provenance**: Slide 21, shape "Image 1", 221451 × 177205 EMU (~0,24 × 0,19 in), 528 bytes.
- **Depiction**: Icono decorativo diminuto: mismo rectángulo redondeado rojo oscuro con esquina doblada.
- **Why it matters**: Viñeta que marca el bloque "Analogía". Sin contenido propio.
- **Transcribed text**: (ninguno).

### `AIG4B-Clase-2-LLM.md/images/slide-22-1.jpg`
- **Provenance**: Slide 22 (Ciclo de Entrenamiento en Machine Learning), shape "Image 0", 5017267 × 3770015 EMU (~5,49 × 4,12 in).
- **Depiction**: **Figura en inglés.** Infografía sobre fondo verde intenso, con tarjetas verde muy claro, que traza el bucle de entrenamiento en cuatro pasos numerados en círculos blancos.
  - **1 "Calculate loss"** — tarjeta grande superior, leída de izquierda a derecha: "Weight and Bias" (dos círculos punteados con flecha de rotación) → flecha → "Model" (icono de chip) → flecha → "Predictions" (tres círculos de color: amarillo, turquesa, magenta) → flecha → "Determine Loss" (icono de gráfico con recta amarilla ajustada a puntos y un segmento rosa de residuo) → flecha hacia abajo → "Loss" (icono de termómetro con el bulbo rosa). Desde abajo, un bloque "Dataset" (grilla de círculos) alimenta al modelo por la flecha rotulada "Features", y una columna de círculos azules rotulada "Label" se conecta con la etapa de determinar la loss.
  - **2 "Determine the direction to move the weights and bias"** — tarjeta inferior derecha con dos círculos punteados con signo "?" adentro y flechas de rotación.
  - **3 "Move a small amount in the direction that reduces loss"** — tarjeta inferior central con los mismos dos círculos, ahora con las flechas de rotación resueltas.
  - **4 "Repeat the process until loss can't be reduced"** — texto abajo a la izquierda, con una flecha larga que vuelve a "Weight and Bias" y cierra el bucle.
- **Why it matters**: Es el diagrama 1:1 de la tabla de cuatro pasos de la slide 22 (Calcular la Loss / Determinar la Dirección / Actualizar los Pesos / Repetir) — la tabla es la traducción al español de estos mismos cuatro rótulos. También hace visible el rol del dataset (features + label) que la tabla textual solo menciona de pasada.
- **Transcribed text**: "1" "Calculate loss" · "Weight and Bias" · "Model" · "Predictions" · "Determine Loss" · "Features" · "Dataset" · "Label" · "Loss" · "2" "Determine the direction to move the weights and bias" · "3" "Move a small amount in the direction that reduces loss" · "4" "Repeat the process until loss can't be reduced".

### `AIG4B-Clase-2-LLM.md/images/slide-24-1.jpg`
- **Provenance**: Slide 24 (Backpropagation: Visualización), shape "Image 0", 7608102 × 4707533 EMU (~8,32 × 5,15 in) — único contenido de la slide.
- **Depiction**: **Figura en inglés**, estilo dibujo a mano (tipografía manuscrita, nodos con relleno de rayado diagonal rosa). Red feed-forward de cuatro capas dibujada de izquierda a derecha:
  - Cuatro nodos de entrada rotulados "a", "b", "c", "d", cada uno con una flecha negra entrante desde la izquierda bajo el rótulo "Inputs".
  - Primera capa oculta: tres nodos "h₍₁,₁₎", "h₍₁,₂₎", "h₍₁,₃₎", totalmente conectados desde la entrada.
  - Segunda capa oculta: tres nodos "h₍₂,₁₎", "h₍₂,₂₎", "h₍₂,₃₎", totalmente conectados desde la primera. El rótulo "Hidden layers" va centrado abajo.
  - Un nodo de salida verde rotulado "o", con flecha hacia la derecha bajo el rótulo "Output".
  - Superpuesto y en azul: tres flechas curvas punteadas que van de derecha a izquierda — de la salida hacia la segunda capa oculta, de ahí hacia la primera, y de ahí hacia el nodo de entrada "a" — rotuladas en conjunto "Backpropagation" (manuscrita, arriba a la derecha).
- **Why it matters**: Separa visualmente los dos sentidos de circulación que la slide 23 describe en texto: las flechas negras sólidas son el forward pass, las azules punteadas el backward pass. Es la única figura del deck que muestra el error viajando hacia atrás.
- **Transcribed text**: "Inputs" · "a" · "b" · "c" · "d" · "h(1,1)" · "h(1,2)" · "h(1,3)" · "h(2,1)" · "h(2,2)" · "h(2,3)" · "Hidden layers" · "o" · "Output" · "Backpropagation".

### `AIG4B-Clase-2-LLM.md/images/slide-26-1.jpg`
- **Provenance**: Slide 26 (Redes Recurrentes: intuición), shape "Image 0", 5085727 × 3263007 EMU (~5,56 × 3,57 in).
- **Depiction**: **Figura en inglés.** Dos diagramas de red lado a lado sobre fondo blanco, con el logo "SCALER Topics" al pie.
  - Panel (a) "Recurrent Neural Network": cuatro nodos de entrada negros a la izquierda, totalmente conectados por flechas a tres nodos beige a la derecha; cada nodo beige tiene además una **flecha curva que sale y vuelve sobre sí mismo** (el bucle recurrente) y una flecha de salida hacia la derecha.
  - Panel (b) "Feed-Forward Neural Network": exactamente la misma topología — cuatro nodos negros, tres beige, mismas conexiones y salidas — pero **sin los bucles**.
  - La única diferencia entre los dos paneles son los self-loops.
- **Why it matters**: Aísla el mecanismo que la slide 26 explica en palabras — "para procesar el vector de 'cat', guardate el vector de 'The' y usalo para generar la salida de 'cat'". Al mantener idénticos los dos paneles salvo el bucle, muestra que la recurrencia es *lo único* que agrega memoria. Advertencia: la figura **no** es una RNN desenrollada en el tiempo ni muestra la frase "The cat is on the _" de la slide; el paso temporal está implícito en el self-loop.
- **Transcribed text**: "(a) Recurrent Neural Network" · "(b) Feed-Forward Neural Network" · "SCALER Topics".

### `AIG4B-Clase-2-LLM.md/images/slide-27-1.jpg`
- **Provenance**: Slide 27 (Transformers), shape "Image 0", 4571886 × 6858000 EMU (~5,00 × 7,50 in) — la figura más alta del deck, en formato vertical.
- **Depiction**: **Figura en inglés.** La figura de arquitectura canónica del Transformer (la Figura 1 del paper original de 2017, reproducida sin atribución en la slide). Dos columnas dentro de cajas grises redondeadas, cada una marcada "N×" al costado:
  - **Columna izquierda (encoder)**, de abajo hacia arriba: "Inputs" → caja rosa "Input Embedding" → un símbolo ⊕ que suma la "Positional Encoding" (representada por un icono circular de onda sinusoidal) → caja naranja "Multi-Head Attention" (con tres flechas de entrada que se bifurcan del mismo tensor: query, key, value) → caja amarilla "Add & Norm" con conexión residual → caja celeste "Feed Forward" → otra "Add & Norm" con residual.
  - **Columna derecha (decoder)**, de abajo hacia arriba: "Outputs (shifted right)" → caja rosa "Output Embedding" → ⊕ con "Positional Encoding" → caja naranja "Masked Multi-Head Attention" → "Add & Norm" → caja naranja "Multi-Head Attention" que recibe además, por una flecha larga desde el tope del encoder, las salidas del encoder (cross-attention) → "Add & Norm" → caja celeste "Feed Forward" → "Add & Norm".
  - Encima del decoder: caja violeta "Linear" → caja verde "Softmax" → flecha a "Output Probabilities".
- **Why it matters**: Es la referencia visual de la única afirmación arquitectónica de la slide 27 — "Paper original: encoder + decoder. Pero LLMs modernos (GPT, LLaMA, Claude) usan solo decoder" — y permite señalar exactamente cuál mitad se descarta en un modelo decoder-only. También aterriza el "vector de probabilidades" de las slides 10 y 29: es literalmente el "Output Probabilities" del tope de la figura, después del Softmax.
- **Transcribed text**: "Output Probabilities" · "Softmax" · "Linear" · "Add & Norm" (×5) · "Feed Forward" (×2) · "Multi-Head Attention" (×2) · "Masked Multi-Head Attention" · "N×" (×2) · "Positional Encoding" (×2) · "Input Embedding" · "Output Embedding" · "Inputs" · "Outputs (shifted right)".

## Raw / preserved excerpts

### Slide 1 — notas del orador (únicas del deck, verbatim)

> Discurso Sugerido: "Bienvenidos. Hoy vamos a desmitificar la Inteligencia Artificial. Intuitivamente, solemos pensar en la IA como 'máquinas haciendo cosas que requerirían inteligencia si las hiciera un humano'. Pero si queremos ser rigurosos, como proponen Russell y Norvig, la IA es el diseño de agentes racionales: sistemas que perciben su entorno y toman acciones para maximizar sus posibilidades de éxito en un objetivo dado. No se trata de crear humanos sintéticos, sino de resolver problemas complejos con matemáticas a gran escala."
>
> Contexto Técnico Profundo: La definición de agente racional evita el debate filosófico sobre la "conciencia" y se centra en la función matemática que mapea secuencias de percepciones a acciones (arquitectura de agentes).
>
> Enlace Recomendado: Sitio oficial del libro "Artificial Intelligence: A Modern Approach" (Russell & Norvig)

### Slide 11 — Modelos de Generación de Palabras — Ejemplo (verbatim)

```
V = { "a", "to", "on", "the", "sat", "cat", "dog", "bed", "ran", "mat", " ", "<fin>", ".", "," }

T = {
"the cat sat on mat"
"a dog ran to bed"
"the dog sat on bed"
"a cat ran to mat"
"the cat ran to dog"
}

P =

the dog sat on

En el corpus, la palabra correcta corresponde a T[2] = "bed".
El vector objetivo tendrá un 1 en la posición correspondiente a "bed" y 0 en el resto.
Salida del modelo (vector de probabilidades sobre el vocabulario):

[a: 0.01, to: 0.02, on: 0.03, the: 0.04, sat: 0.01, cat: 0.01, dog: 0.02,
bed: 0.78, ran: 0.03, mat: 0.04, " ": 0.01, <fin>: 0.00, ".": 0.00, ",": 0.00]
```

### Slide 28 — Comparación de Modelos (verbatim)

**Sección: TRANSFORMERS: CÓMO FUNCIONA UN LLM**

| Modelo | Idea principal | Novedad | Pros | Contras |
|---|---|---|---|---|
| Word2Vec | Aprende embeddings a partir del contexto en que aparecen las palabras | Demostró que se pueden aprender representaciones semánticas de forma no supervisada. Palabras similares quedan cerca en el espacio vectorial. | Simple, rápido de entrenar. Captura analogías semánticas (rey - hombre + mujer ≈ reina). | Cada palabra tiene un solo vector sin importar el contexto. No modela el orden de las palabras ni secuencias. |
| RNNs (LSTM, GRU) | Procesan texto secuencialmente manteniendo un estado interno que actúa como memoria | Introdujeron la capacidad de modelar secuencias y dependencias temporales en texto. Permitieron tareas como traducción y generación. | Capturan el orden de las palabras. LSTM/GRU mejoran la memoria a mediano plazo. Base de modelos como ELMo. | Procesamiento secuencial (no paralelizable, lento). Pierden información en secuencias largas. Difícil capturar contexto distante. |
| Transformers | Usan attention para que cada token mire a todos los demás tokens en paralelo | Eliminaron la necesidad de procesar secuencialmente. Capturan dependencias largas sin degradación. Base de todos los LLMs modernos. | Altamente paralelizables (entrenan rápido en GPUs). Capturan contexto largo. Escalan muy bien con más datos y parámetros. | Requieren enormes cantidades de datos y cómputo. Alto costo de entrenamiento. El mecanismo de attention crece cuadráticamente con la longitud. |

- Evolución: representaciones estáticas → secuenciales → contextuales con attention.

### Slide 30 — Generación de Palabras — Escala LLM (verbatim)

**Sección: TRANSFORMERS: CÓMO FUNCIONA UN LLM**

**El mismo problema de Language Modelling, pero a una escala masiva:**

|  | Ejemplo anterior | ChatGPT (GPT-4) |
|---|---|---|
| Vocabulario V | 14 palabras ("a", "to", "cat", ...) | ~100.000 tokens (sub-palabras en múltiples idiomas) |
| Corpus T | 5 frases | Billones de palabras (internet, libros, código, papers...) |
| Parámetros | Pocos | Cientos de miles de millones |
| Entrenamiento | Segundos | Meses en miles de GPUs |
| Frase P | "the dog sat on" | Cualquier texto, de cualquier largo |

- El concepto es exactamente el mismo: predecir la siguiente palabra.
- Lo que cambia es la escala del vocabulario, los datos y el modelo.

### Slide 32 — Entrenamiento vs Inferencia (verbatim)

**Sección: TRANSFORMERS: CÓMO FUNCIONA UN LLM**

|  | Entrenamiento | Inferencia |
|---|---|---|
| ¿Qué pasa? | Aprende ajustando parámetros | Usa parámetros ya aprendidos |
| ¿Cuándo? | Antes de estar disponible | Cada vez que un usuario pregunta |
| ¿Quién? | OpenAI, Anthropic, Meta... | Vos, al usar ChatGPT o Claude |
| Ejemplo | Entrenar GPT-4 | Preguntarle "¿qué es NLP?" |
| Costo | Millones de dólares, semanas | Fracción de segundo por respuesta |
| Parámetros | Se modifican constantemente | Están congelados (no cambian) |

- **Cuando usás ChatGPT, el modelo no está aprendiendo de tu conversación. Los parámetros ya están fijos. Solo está haciendo inference.**
- **Entrenar un modelo grande requiere billones de palabras y miles de GPUs durante semanas. Por eso muy pocas empresas lo hacen.**

### Slide 2 — Agenda (verbatim, estructura de la clase)

**Objetivo: Entender cómo se puede generar texto automáticamente.**

- **Problemas clásicos de ML**
- **NLP: motivación y problemas**
  - **Language Modelling: predecir la siguiente palabra**
  - **Representación de texto: tokens, vocabulario y embeddings**
- **Redes neuronales: del perceptrón al deep learning**
- **De RNNs a Transformers: el rol de attention**
- **Transformers: Cómo funciona un LLM**

### Slide 15 — Palabras vs Tokens (verbatim, bloque completo)

> **Los modelos trabajan con números, no con letras. El primer paso es dividir el texto en tokens — las unidades mínimas que el modelo procesa. Cada token tendrá un vector asignado que lo identifica.**
>
> - Un token puede ser: una palabra completa, parte de una palabra, o un signo de puntuación.
>
> - "the cat sat on the mat"
> - → ["the", "cat", "sat", "on", "the", "mat"]    (6 tokens)
>
> **Palabras vs Tokens**
>
> - Los modelos modernos usan sub-palabras (o incluso caracteres):
>
> - "unbelievable"
> - → ["un", "believ", "able"]    (3 tokens)
>
> - Vocabularios más compactos (no necesita una entrada por cada palabra del idioma)
> - Entiende palabras nuevas descomponiéndolas en partes conocidas
> - Funciona en múltiples idiomas

### Slide 16 — Word2Vec (verbatim, bloque completo)

> **Word2Vec**
>
> - Uno de los primeros métodos para aprender embeddings automáticamente.
> - Idea: "una palabra se define por la compañía que tiene".
> - Funcionamiento: Saca promedios de los vectores de las palabras que circundan a cada una en el corpus de texto en que aparece.
> - Importante: Word2Vec no es un modelo de lenguaje (no genera palabras). Es un método para obtener embeddings con significado real de palabras en su contexto.

### Slide 25 — El problema del contexto (verbatim, bloque completo)

> **El problema del contexto**
>
> - "The animal didn't cross the street because it was too tired"
>
> - ¿A qué se refiere "it"? A "animal". Pero están lejos en la oración.
> - Para cuando la RNN llega a "it", la info sobre "animal" se debilitó → motivó los Transformers.

### Slide 27 — Intuición de la Atención y Arquitectura (verbatim, bloques completos)

> **La arquitectura que cambió todo (2017). A diferencia de las RNNs, los Transformers procesan toda la secuencia de una vez, en paralelo.**
>
> **Intuición de la Atención**
>
> - Cuando leemos, no prestamos la misma atención a todas las palabras:
>
> - "The animal didn't cross the street because it was too tired"
> - → Para entender "it", miramos "animal". Eso es atención.
>
> - Atención permite que cada token "mire" a todos los demás y decida cuáles son relevantes.
>
> - Captura dependencias largas (palabras separadas que se relacionan)
> - Relaciones sintácticas (sujeto-verbo-objeto)
> - Relaciones semánticas (significado, contexto)
>
> **Arquitectura**
>
> - Paper original: encoder + decoder. Pero LLMs modernos (GPT, LLaMA, Claude) usan solo decoder.

### Slide 31 — ¿Qué cambió? (verbatim, bloque completo)

> **Muchas tareas se resuelven ahora con una sola técnica: generación de texto con modelos fundacionales (modelos grandes pre-entrenados).**
>
> - **Si un modelo puede comprender texto y generar palabras, podemos reformular casi cualquier tarea como generación:**
>
> - **Sentimiento: "¿Este review es positivo o negativo?" → modelo genera "positivo"**
> - **Traducción: "Traducí: the cat is on the mat" → modelo genera "el gato está sobre la alfombra"**
> - **Resumen: "Resumí este texto: [texto largo]" → modelo genera el resumen**
>
> - **problema  →  prompt (instrucción en texto)  →  modelo genera la solución**
>
> - **Esto es lo que hacemos cuando usamos ChatGPT, Claude, etc.**
