# Modelado de inputs y outputs en redes neuronales

Guía de referencia. Cubre desde conceptos base hasta codificación de variables, escalas, y diseño de la capa de salida.

---

## 1. Conceptos base

### Activación

El valor de salida de una neurona.

| Paso | Fórmula |
|---|---|
| Pre-activación | `z = W·x + b` |
| Activación | `a = f(z)` |

El término se usa en tres sentidos que conviene no mezclar:

| Término | Qué es |
|---|---|
| Activación (valor) | El número que emite la neurona |
| Función de activación | La transformación no lineal `f` |
| Activaciones (plural) | El tensor de salidas de una capa para un batch |

**Por qué existe la no linealidad:** sin ella, apilar capas no sirve. La composición de transformaciones lineales sigue siendo lineal y toda la red colapsaría a una sola matriz.

| Función | Salida | Uso típico |
|---|---|---|
| ReLU | `max(0, z)` | Capas ocultas, default |
| GELU / SiLU | Suavizado de ReLU | Transformers |
| Sigmoide | (0, 1) | Salida binaria, gates en LSTM |
| Softmax | Distribución que suma 1 | Capa final de clasificación |
| Tanh | (−1, 1) | Redes recurrentes clásicas |

### Pesos y bias

| Nivel | Objeto | Shape |
|---|---|---|
| Una neurona | vector `w` | `(n,)` |
| Capa de m neuronas | matriz `W` | `(m, n)` |
| Bias | vector `b` | `(m,)` |

Parámetros de una capa: `m·n + m`.

**Convención de layout:** PyTorch guarda `weight` como `(out, in)` y hace `x @ W.T`. Keras usa `(in, out)` y hace `x @ W`. Misma matemática, transpuesta distinta — fuente clásica de errores al portar código.

**Batches:** con batch de tamaño B, el input es `(B, n)` y la salida `(B, m)`. Los pesos son los mismos para todas las filas.

### Loss, cost, error, objective

| Término | Alcance |
|---|---|
| **Loss** | Error de un solo ejemplo |
| **Cost** | Promedio del loss sobre el dataset o batch |
| **Error function** | Término genérico, ambiguo |
| **Objective** | Lo que se optimiza: cost + regularización |

La distinción loss/cost viene de los cursos de Andrew Ng. Bishop y Goodfellow usan "error function" y "cost function" indistintamente. En papers modernos se dice "loss" para todo.

Cuidado con "error" a secas: en estadística suele referirse al residuo `y − ŷ`, y "error rate" es la proporción de clasificaciones incorrectas — una métrica, no algo diferenciable.

### Qué cambia durante el entrenamiento

| Objeto | ¿Se entrena? |
|---|---|
| `W`, `b` | **Sí** — son los parámetros |
| Tabla de embeddings | **Sí** |
| Input `x`, targets `y` | No, son datos |
| Activaciones | Cambian como consecuencia del forward |
| Learning rate, capas, batch size | No — hiperparámetros |
| Estado del optimizador (momentos de Adam) | Se guarda, pero no es parte del modelo |

En fine-tuning moderno esto se relaja: LoRA congela `W` y `b` y entrena una matriz de bajo rango aparte; linear probing entrena solo la última capa.

---

## 2. El input: principio general

**El input es todo lo que sabés, convertido a números.** Todo termina en un vector de floats de tamaño fijo.

Lo que diferencia los casos es qué significa la posición dentro de ese vector.

| Familia | Qué es cada componente | Estructura entre componentes |
|---|---|---|
| Features tabulares | Una variable distinta | Ninguna — el orden es arbitrario |
| Píxeles | Intensidad en una posición | Vecindad 2D |
| Señal | Amplitud en un instante | Vecindad 1D temporal |

La pregunta que ordena el zoológico completo: **¿qué transformaciones puedo aplicarle al input sin cambiar la respuesta correcta?**

| Estructura | Qué podés cambiar | Arquitectura natural |
|---|---|---|
| Sin estructura (tabular) | El orden de las columnas | Fully connected |
| Grilla 1D (señal) | Desplazar en el tiempo | Conv 1D, RNN, Transformer |
| Grilla 2D (imagen) | Desplazar en el espacio | Conv 2D |
| Grilla 3D (video, tomografía) | Desplazar en espacio y tiempo | Conv 3D |
| Secuencia discreta (texto) | Nada — el orden es todo | Transformer |
| Conjunto | El orden de los elementos | Deep Sets, attention |
| Grafo | Renumerar los nodos | GNN |

### Familias completas

| Familia | Ejemplo de negocio | Cómo entra |
|---|---|---|
| Tabular | Scoring crediticio | Vector de features normalizadas |
| Imagen | Control de calidad visual | Tensor `(C,H,W)` |
| Señal 1D | Vibración de una máquina | Vector de muestras, o espectrograma |
| Texto | Clasificar reclamos | Secuencia de tokens → embeddings |
| Serie temporal multivariada | Demanda por SKU | Matriz `(tiempo, variables)` |
| Video | Análisis de góndola | Tensor `(T,C,H,W)` |
| Grafo | Fraude en red de cuentas | Nodos + lista de aristas |
| Conjunto | Carrito de compras | Colección sin orden + agregación |
| Nube de puntos 3D | LiDAR | `(N, 3)` — es un conjunto |
| Eventos / logs | Journey del cliente | Secuencia de (evento, timestamp) |
| Multimodal | Tasación con fotos + texto + datos | Rama por modalidad → concatenar |

### El eje de canales

RGB introduce un eje que no es ni espacial ni temporal.

| Eje | Relación entre posiciones vecinas | ¿Reordenable? |
|---|---|---|
| Espacial (H, W) | Vecindad | No |
| Temporal (T) | Vecindad | No |
| **Canal (C)** | **Ninguna** — R no está "cerca" de G | Sí |

El eje de canales se comporta como el caso tabular: variables distintas medidas en el mismo punto.

Un filtro convolucional **se desliza** sobre H y W, pero **abarca todos los canales de una vez**. Un kernel 3×3 sobre RGB tiene 3×3×3 = 27 pesos, no 9.

| Caso | Ejes con vecindad | Canales |
|---|---|---|
| Foto RGB | H, W | 3 |
| Satelital multiespectral | H, W | 13 bandas |
| Resonancia magnética | H, W, D | 1 o varias secuencias |
| Video | T, H, W | 3 |
| Audio estéreo | T | 2 |
| ECG 12 derivaciones | T | 12 |
| Serie temporal multivariada | T | Una por variable |

Una serie de ventas de 40 SKUs es matemáticamente lo mismo que una imagen de 1 píxel de alto con 40 canales. Por eso las conv 1D funcionan en forecasting.

**Convención de orden:** PyTorch usa channels-first `(N,C,H,W)`, TensorFlow channels-last `(N,H,W,C)`. Olvidarse del `permute` no explota — entrena y da resultados malos, que es peor.

### Multimodal

```
fotos    → CNN        → (128,)  ┐
texto    → embeddings → (768,)  ├→ concat (912,) → FC → precio
tabular  → (16,)               ┘
```

---

## 3. Codificación de variables

### La pregunta que decide todo

Frente a un número: **¿qué significa la resta entre dos valores?**

| Si la resta... | Entonces |
|---|---|
| Da una cantidad interpretable | Float normalizado, 1 neurona |
| Da un orden pero no una magnitud confiable | Ordinal — evaluar one-hot también |
| No significa nada | One-hot o embedding según cardinalidad |
| No se puede ni plantear | Probablemente no sea una feature |

### Tabla base

| Tipo de variable | Neuronas | Qué va en cada una |
|---|---|---|
| Numérica continua | 1 | Valor normalizado |
| Binaria | 1 | 0.0 o 1.0 |
| Categórica con k valores | k | One-hot |
| Categórica (dummy) | k−1 | La base es "todo 0" |
| Ordinal | 1 | 0, 0.5, 1 |
| Categórica alta cardinalidad | d (8–64) | Embedding aprendido |
| Cíclica | 2 | sin y cos |
| Faltante | +1 | Flag binario |

### Todo termina en floats, no enteros

| | Entero | Float |
|---|---|---|
| Valores posibles | Discretos | Continuos |
| `(x−μ)/σ` representable | No | Sí |
| Gradiente definido | No | Sí |

Los enteros aparecen en un solo lugar: como **índice** para buscar en una tabla de embeddings. El entero no entra a la red, entra al lookup.

### Booleanos

| Variable | Codificación | Neuronas |
|---|---|---|
| Tiene cochera | 0 / 1 | 1 |
| Cliente activo | 0 / 1 | 1 |
| Es feriado | 0 / 1 | 1 |
| Fumador (sí/no/no declara) | One-hot | **3** |

Un booleano con un tercer estado deja de ser booleano.

### Enteros con magnitud real → 1 float normalizado

| Variable | Transformación previa |
|---|---|
| Ambientes, antigüedad, hijos | Ninguna |
| Días desde última compra | `log(1+x)` |
| Cantidad de transacciones | `log(1+x)` |
| Ingreso mensual | `log(1+x)` |
| Cantidad de reclamos | `log(1+x)` + flag "es cero" |
| Empleados de la empresa | `log(1+x)` |

El log aparece con colas largas: la diferencia entre 1 y 10 transacciones importa más que entre 4000 y 4010.

### Enteros que son códigos → NUNCA como número

| Variable | Codificación | Neuronas |
|---|---|---|
| ID de barrio (1–48) | One-hot | 48 |
| Código postal | Embedding, o jerárquico por prefijo | 32, o 3–5 |
| ID de producto (2M) | Embedding | 64 |
| Código de rubro CIIU | Una feature por nivel | 4 one-hots |
| DNI / CUIT / nº de póliza | **Se descarta** | 0 |

Un identificador único no tiene poder predictivo. Si el modelo "aprende" de él, está memorizando ejemplos individuales.

### Ordinales

| Variable | Opción | Neuronas |
|---|---|---|
| Nivel educativo | 1 float, o one-hot | 1 o 5 |
| Plan (Free/Basic/Pro/Enterprise) | Ambos concatenados | 1 + 4 |
| Satisfacción 1–5 | 1 float | 1 |
| Severidad (leve/moderado/grave) | 1 float | 1 |
| Rating crediticio (AAA→D) | 1 float | 1 |

| Opción | Asume |
|---|---|
| Un float: 0, 0.5, 1 | Que las distancias son iguales |
| One-hot | Nada sobre distancias, pero pierde el orden |
| Ambos concatenados | Le deja a la red decidir |

Los planes comerciales son el caso donde conviene poner ambos: el salto Pro→Enterprise suele ser mayor que Free→Basic.

### Nominales

| Variable | Cardinalidad | Codificación | Neuronas |
|---|---|---|---|
| Tipo de propiedad | 5 | One-hot | 5 |
| Canal de adquisición | 8 | One-hot | 8 |
| Provincia | 24 | One-hot | 24 |
| Marca de auto | 60 | Embedding | 16 |
| Rubro comercial | 400 | Embedding | 32 |
| Ciudad | 3000 | Embedding | 48 |
| Modelo de celular | 20.000 | Embedding + hashing | 64 |

### Cíclicas

| Variable | Período | Neuronas |
|---|---|---|
| Hora del día | 24 | 2 |
| Día de la semana | 7 | 2 |
| Mes | 12 | 2 |
| Día del año | 365 | 2 |
| Dirección de viento | 360° | 2 |

`sin(2πt/T)` y `cos(2πt/T)`. Ambas son necesarias: con una sola, dos momentos distintos del ciclo colapsan al mismo valor. Las 23:00 y las 00:00 están a 1 hora, pero como números planos están a 23.

### Fechas

| Feature derivada | Neuronas | Qué captura |
|---|---|---|
| Hora (cíclica) | 2 | Patrón diario |
| Día de semana (cíclica) | 2 | Patrón semanal |
| Mes (cíclico) | 2 | Estacionalidad |
| Feriado / fin de semana | 1–2 | Anomalías de calendario |
| Días desde el evento | 1 | Recencia |
| Tiempo absoluto | 1 | Tendencia de largo plazo |

**"Cuándo en el ciclo" es cíclico; "hace cuánto" es continuo.** Dos preguntas distintas, suelen necesitarse las dos.

### Texto

| Método | Neuronas | Cuándo |
|---|---|---|
| Bag of words | tamaño vocab | Legacy, muy ralo |
| TF-IDF | tamaño vocab | Baseline decente |
| Embedding promediado | 100–300 | Simple y sólido |
| Sentence transformer | 384–1536 | Default hoy |
| Tokens → transformer | Secuencia | Cuando el orden importa |

### Faltantes

| Situación | Estrategia |
|---|---|
| Falta al azar | Imputar (media/mediana) + **flag binario** |
| Falta por un motivo | Categoría propia: "NO_INFORMADO" |
| Falta mucho (>50%) | Considerar descartar la variable |
| Numérica que puede ser 0 | **Nunca** rellenar con 0 |

El flag cuesta una neurona y muchas veces es más predictivo que la variable misma.

### Casos que no encajan limpio

| Variable | Codificación | Neuronas |
|---|---|---|
| Monto en varias monedas | Convertir a una unidad, después log + z-score | 1 |
| Porcentaje (0–100) | Dividir por 100 | 1 |
| Rango declarado ("$1000–2000") | Dos floats: min y max | 2 |
| Lista de tags | Multi-hot | k |
| Coordenadas lat/lon | Proyección 3D, o distancia a puntos clave | 3, o k |
| Versión de software ("3.4.1") | Un float por componente | 3 |
| Temperatura en °C | Min-max con rango conocido | 1 |

### Otros métodos para categóricas

| Método | Neuronas | Riesgo |
|---|---|---|
| Target encoding | 1 | **Alta fuga** si no se hace con CV interna |
| Hashing | d fijo | Colisiones |
| Frecuencia | 1 | Pierde identidad |

### Numéricas: cuándo binnear

| Método | Neuronas | Cuándo |
|---|---|---|
| Estandarización | 1 | Default |
| Min-max | 1 | Rango conocido y acotado |
| Log + estandarización | 1 | Cola larga |
| Quantile / rango-inverso | 1 | Outliers fuertes |
| **Binning + one-hot** | **k** | **Relación no monótona** |
| Binning + valor | 2 | Bin one-hot + valor dentro del bin |

Si el riesgo crediticio sube con la edad hasta 30, baja hasta 55 y vuelve a subir, un solo número obliga a la red a aprender esa curva. Los bins se la dan servida.

---

## 4. One-hot vs. embedding

### One-hot

Una neurona por valor posible, todas en 0 salvo una en 1.

| Valor | Casa | Depto | PH | Local |
|---|---|---|---|---|
| Casa | **1** | 0 | 0 | 0 |
| Departamento | 0 | **1** | 0 | 0 |
| PH | 0 | 0 | **1** | 0 |
| Local | 0 | 0 | 0 | **1** |

Todas las categorías quedan equidistantes, que es exactamente la verdad del dato. Codificar Casa=1, Depto=2, PH=3 le impondría al modelo un orden y unas distancias inventadas.

Como solo una posición vale 1, el producto `W·x` **selecciona una columna de W**: cada categoría tiene su propio conjunto de pesos independiente.

| Aspecto | Detalle |
|---|---|
| Dummy encoding | k−1 columnas; importa en modelos lineales, irrelevante en redes |
| Categoría desconocida | Todo 0, o columna extra "OTRO" |
| Normalización | No hace falta, ya está en 0/1 |
| Multi-hot | Varios 1 si la variable admite varios valores |

### Comparación

| | One-hot | Embedding |
|---|---|---|
| Neuronas | k | d (8–64) |
| Contenido | Ceros y un 1 | Floats densos |
| ¿Se aprende? | No | **Sí, con la red** |
| Distancia entre categorías | Todas iguales | La aprende de los datos |
| Datos necesarios | Pocos | Muchos |
| Interpretabilidad | Alta | Baja |
| Reutilizable | No | Sí |

### Cuándo cada uno

| Cardinalidad | Elegí |
|---|---|
| ≤ 15 | One-hot |
| 15–50 | Cualquiera; one-hot si hay pocos datos |
| ≥ 50 | Embedding |

Otros criterios: pocos datos totales → one-hot. Necesitás interpretar coeficientes → one-hot. Querés reusar la representación → embedding. Aparecen categorías nuevas seguido → embedding + hashing.

### Dimensión del embedding

Heurísticas de industria (fast.ai), no teoría:

```
d ≈ min(50, (k+1)/2)
d ≈ k^0.25 · 1.6
```

| k | d razonable |
|---|---|
| 50 | 12 |
| 500 | 24 |
| 10.000 | 48 |
| 1.000.000 | 64–128 |

d crece mucho más lento que k.

### Cómo funciona el embedding

Una tabla de `k × d` floats, entrenable como cualquier peso.

| Paso | Qué pasa | Dónde |
|---|---|---|
| 1 | Categoría → índice entero (Toyota → 3) | **Afuera**, preprocesamiento |
| 2 | Índice → vector de d floats | **Adentro**, primera capa |
| 3 | Vector → capas ocultas → salida | Adentro |

**Es matemáticamente equivalente a one-hot seguido de una capa lineal sin bias.** Multiplicar un one-hot por una matriz `(d,k)` selecciona una columna. El embedding hace ese lookup sin computar el producto con miles de ceros.

Conceptualmente: la tabla de embeddings **es la primera capa de la red**, aplicada a un one-hot implícito. Se piensa como "codificación del input" por costumbre, pero está del lado del modelo.

### Gradiente ralo

| | Linear | Embedding |
|---|---|---|
| Filas actualizadas por batch | Todas | Solo las de los índices presentes |
| Gradiente | Denso | **Ralo** |

Un batch de 32 propiedades toca como mucho 32 filas. Un barrio que aparece 3 veces en todo el dataset recibe 3 actualizaciones y queda casi en su valor de inicialización.

### Las dos ventajas no obvias

**Comparte estadística.** Con one-hot cada categoría aprende aislada: un producto con 3 ventas no aprende nada. Con embedding queda cerca de productos parecidos y hereda parte de lo aprendido por ellos.

**Es reutilizable.** El embedding entrenado sirve para clustering, búsqueda por similitud, o como input de otro modelo.

### El puente a los LLMs

| Aplicación | Qué se embebe |
|---|---|
| Tabular | Categorías |
| NLP | Palabras / tokens |
| Recomendación | Usuarios y productos |
| Grafos | Nodos |
| RAG | Documentos completos |

Un LLM empieza exactamente así: cada token es un índice que busca su fila en una tabla de ~50.000 × 4096.

**Un embedding es una representación densa aprendida donde la geometría del espacio codifica el significado.**

### Cuándo el embedding sí va afuera

| Caso | Dónde |
|---|---|
| Categoría en tabular | Adentro, entrenado desde cero |
| Word2Vec / GloVe | Adentro, cargado, a veces congelado |
| Sentence transformers | **Afuera** — es otro modelo |
| RAG / búsqueda semántica | **Afuera** — se guardan en vector DB |

Regla: **si tiene parámetros que querés entrenar, va adentro. Si es una transformación fija, puede ir afuera.**

---

## 5. Escalas y normalización

### Por qué importa

El gradiente respecto a un peso es proporcional al valor de la entrada:

```
∂J/∂wⱼ = δ · xⱼ
```

Si `x₁` = m² ≈ 200 y `x₂` = cochera ∈ {0,1}, el gradiente de `w₁` es ~200 veces mayor. Pero el learning rate es **uno solo para toda la red**.

| Escalas parejas | Escalas dispares |
|---|---|
| Curvas de nivel circulares | Elipses muy alargadas |
| El gradiente apunta al mínimo | El gradiente apunta a la pared |
| Converge en pocos pasos | Zigzaguea |

Formalmente: el **número de condición** de la Hessiana. Normalizar lo baja, y la velocidad de convergencia depende directamente de él.

**Efecto secundario:** con sigmoide o tanh, una entrada grande empuja `z` a la zona plana donde la derivada es casi cero. La neurona se **satura** y deja de aprender. Además, Xavier y He asumen entradas con media 0 y varianza ~1: sin normalizar, la inicialización deja de tener sentido.

### Qué normalizar

| Qué | ¿Se normaliza? |
|---|---|
| Features de entrada | **Siempre** |
| One-hot y booleanos | No — ya están en 0/1 |
| Salidas de capas ocultas | Opcional, con BatchNorm/LayerNorm |
| Target en regresión | Conviene, y desescalar al predecir |

| Método | Fórmula | Cuándo |
|---|---|---|
| Estandarización (z-score) | `(x−μ)/σ` | Default |
| Min-max | `(x−min)/(max−min)` | Rango conocido y fijo |
| Log + estandarización | `log(1+x)` primero | Cola larga |
| Robust scaling | Mediana e IQR | Outliers fuertes |

### Qué significa "float normalizado"

Con m² de media 95 y desvío 40:

| Valor original | Cuenta | Normalizado |
|---|---|---|
| 85 m² | (85−95)/40 | −0.25 |
| 95 m² | (95−95)/40 | 0.00 |
| 175 m² | (175−95)/40 | +2.00 |

La unidad "metros cuadrados" desaparece. La escala pasa a ser **"cuántos desvíos por encima o por debajo del promedio"**.

### El mismo problema entre capas

| Etapa | Qué viaja | Cómo se controla |
|---|---|---|
| Datos → capa 1 | Features `x` | Normalización del input |
| Capa 1 → capa 2 | Activaciones `a₁` | Inicialización + BatchNorm/LayerNorm |
| Última capa → loss | Predicción `ŷ` | Escala del target |

Si cada capa multiplica la escala por un factor `c`, el efecto es multiplicativo:

| c | Después de 10 capas |
|---|---|
| 1.2 | ×6 |
| 1.5 | ×58 |
| 0.8 | ×0.1 |
| 0.5 | ×0.001 |

Son los **exploding / vanishing gradients**. El mismo fenómeno aparece en el forward (activaciones) y en el backward (gradientes).

| Herramienta | Qué hace |
|---|---|
| Xavier / He | Elige `Var(W)` para que `c ≈ 1` al inicio |
| BatchNorm | Renormaliza sobre el batch, por feature |
| LayerNorm | Renormaliza sobre las features, por ejemplo |
| Conexiones residuales | Dan un camino directo al gradiente |

LayerNorm ganó en NLP porque no depende del tamaño del batch.

**El principio que unifica:** un solo concepto cubre cuatro temas que suelen enseñarse sueltos — normalización del input, inicialización de pesos, normalización interna y control de gradientes.

### Las dos advertencias

**Adam mitiga pero no resuelve.** Escala el paso por parámetro, así que absorbe parte del problema. Por eso a veces un modelo sin normalizar "funciona igual". Sigue haciendo falta: la saturación y la inicialización rota no se arreglan con el optimizador.

**No aplica a todo.** Los árboles y gradient boosting son invariantes a transformaciones monótonas: no necesitan normalización. Es una particularidad de los métodos basados en gradiente, no una ley general del ML.

**Escala pareja ≠ importancia pareja.** Normalizar no le quita importancia a una variable. La importancia la aprende la red vía los pesos. Normalizar solo la pone en condiciones de ser evaluada.

---

## 6. μ, σ y el artefacto de producción

### Solo con train

| Cómo lo hacés | Qué pasa |
|---|---|
| μ, σ solo de train | El test es realmente desconocido → métrica confiable |
| μ, σ de todo el dataset | Información del test se filtró → métrica optimista |

Se llama **data leakage**. Con μ y σ el efecto es chico, pero el mismo principio aplica a target encoding, imputación, selección de features y PCA — donde el efecto es enorme.

**Regla:** todo lo que se "aprende" de los datos se aprende solo del train. Incluidas las transformaciones.

### Se guardan y se reaplican

| Momento | μ, σ que se usan |
|---|---|
| Entrenamiento | Calculados de train |
| Validación | Los de train |
| Test | Los de train |
| Producción | Los de train |

Si en producción normalizás con μ=120 en vez de 95, una propiedad de 175 m² entra como +1.375 en vez de +2.00. El modelo la lee como más chica de lo que es. **No hay error, no hay excepción — predicción incorrecta silenciosa.**

### Qué es "el modelo" en producción

Un modelo desplegado no es solo `W` y `b`:

- Los pesos
- Los μ y σ de cada variable
- El diccionario categoría → índice (o el orden de columnas del one-hot)
- Los valores de imputación de faltantes

Si guardás solo los pesos, el modelo es inutilizable.

### El bug clásico

```python
# MAL — μ y σ del test
scaler.fit_transform(X_test)

# BIEN — μ y σ de train
scaler.fit(X_train)
scaler.transform(X_test)
```

Un `fit` de más y el modelo se degrada sin dar ningún error.

### Dónde vive la normalización en inferencia

| Opción | Dónde vive | Qué recibe el modelo | Riesgo de skew |
|---|---|---|---|
| **A** — Manual | En el código que llama | Vector ya normalizado | **Alto** |
| **B** — Pipeline | Adentro del objeto serializado | Valores crudos | Bajo |
| **C** — En el grafo | Como capa de la red | Valores crudos | **Muy bajo** |
| **D** — Feature store | Servicio centralizado | Features ya transformadas | Muy bajo, costoso |

Frecuencia real:

| Contexto | Lo habitual |
|---|---|
| Tabular, scikit-learn | **B** — Pipeline, estándar de facto |
| Deep learning, imágenes | **A** — `torchvision.transforms` fuera del modelo |
| ONNX / TF Serving / edge | **C** — el artefacto tiene que ser autocontenido |
| Keras moderno | **C** — `layers.Normalization()` con `adapt()` |
| Producción industrial madura | **D** |

La C es la más robusta y la menos usada. En visión domina la A por razones históricas: el preprocesamiento corre en CPU mientras la GPU entrena, y ahí mismo está la augmentación que no debe correr en inferencia.

**Regla:** el preprocesamiento y el modelo se despliegan juntos, siempre. **El que consume el modelo no debería tener que saber que la normalización existe.**

### Data drift

Con el tiempo la distribución real cambia. La solución **no** es recalcular μ y σ en producción: es detectar el drift, reentrenar con datos nuevos y desplegar un paquete nuevo con sus propios μ, σ. Se actualizan junto con los pesos, nunca por separado.

---

## 7. Ejemplos completos

### Barrios + metros cuadrados (12 barrios)

| Posición | Contenido | Ejemplo: 85 m² en Palermo |
|---|---|---|
| 1 | m² normalizado | −0.25 |
| 2–13 | Barrio one-hot | 0,0,1,0,0,0,0,0,0,0,0,0 |

**13 neuronas.**

Como el one-hot activa una sola posición, cada barrio tiene su propio bias efectivo:

```
precio ≈ w_m2 · m²_norm + w_palermo
precio ≈ w_m2 · m²_norm + w_liniers
```

Rectas paralelas, una por barrio. **Pero eso es lo que haría un modelo lineal.** Una red con capas ocultas puede aprender que en Palermo el m² vale más *por metro* — esa interacción la construye sola.

Arquitectura: `13 → 32 → 16 → 1`, salida lineal, MSE. **993 parámetros.**

### Tres numéricas (PyTorch)

Agua de pozo (booleano), m² cubiertos, superficie del terreno.

```python
X_raw = torch.tensor([
    [1.0,  85.0,  300.0],
    [0.0, 120.0,  400.0],
    [1.0,  60.0,  250.0],
    [0.0, 200.0, 1000.0],
], dtype=torch.float32)

# Normalizar SOLO las columnas continuas
mu    = X_raw[:, 1:].mean(dim=0)
sigma = X_raw[:, 1:].std(dim=0)

def preprocess(x):
    out = x.clone()
    out[:, 1:] = (x[:, 1:] - mu) / sigma   # el booleano queda intacto
    return out

model = nn.Sequential(
    nn.Linear(3, 16), nn.ReLU(),
    nn.Linear(16, 8), nn.ReLU(),
    nn.Linear(8, 1),
)
```

**3 neuronas de entrada, 209 parámetros.** El booleano no se normaliza: ya está en {0,1}.

Feature derivada útil: el ratio cubierto/terreno, que dice si el lote está aprovechado.

Inferencia:

```python
with torch.no_grad():
    pred = model(preprocess(nueva)) * y_sigma + y_mu   # desescalar
```

### Con 500 barrios (embedding)

| Variable | Codificación | Neuronas |
|---|---|---|
| Agua de pozo | 0/1 | 1 |
| m² cubiertos | z-score | 1 |
| Superficie terreno | z-score | 1 |
| **Barrio (500)** | **Embedding d=24** | **24** |

**27 neuronas.** Con one-hot serían 503.

```python
class PrecioNet(nn.Module):
    def __init__(self, n_barrios=500, d_emb=24, n_num=3):
        super().__init__()
        self.emb = nn.Embedding(n_barrios, d_emb)
        self.net = nn.Sequential(
            nn.Linear(d_emb + n_num, 64), nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, 32), nn.ReLU(),
            nn.Linear(32, 1),
        )

    def forward(self, barrio_idx, x_num):
        e = self.emb(barrio_idx)              # (B,) long → (B, 24)
        return self.net(torch.cat([e, x_num], dim=1))
```

Dos entradas separadas: índices como `torch.long`, numéricas como `float32`. `nn.Embedding` **exige** enteros — es lo único que hace explícita la distinción categórica/numérica en el código.

| Componente | Shape | Params |
|---|---|---|
| Embedding | (500, 24) | **12.000** |
| Linear 27→64 | | 1.792 |
| Linear 64→32 | | 2.080 |
| Linear 32→1 | | 33 |
| | | **15.905** |

El embedding es el 75% del modelo.

**Los tres problemas con 500 categorías:**

| Problema | Mitigación |
|---|---|
| Barrios con pocos ejemplos | Agrupar los raros en "OTRO", subir weight decay |
| Barrio desconocido en producción | Reservar índice 0 para `<UNK>` |
| Overfitting (12k params solo ahí) | Dropout, weight decay |

Artefacto completo:

```python
torch.save({
    "state_dict": model.state_dict(),
    "barrio2idx": barrio2idx,
    "mu": mu, "sigma": sigma,
    "y_mu": y_mu, "y_sigma": y_sigma,
}, "modelo.pt")
```

### Señal, imagen gris, imagen RGB

| Caso | Shape crudo | Neuronas | Params 1ª capa (a 256) |
|---|---|---|---|
| Señal 1000 muestras | (1000,) | 1.000 | 256 mil |
| Gris 64×64 | (1,64,64) | 4.096 | 1 millón |
| RGB 64×64 | (3,64,64) | 12.288 | 3,1 millones |
| RGB 224×224 | (3,224,224) | 150.528 | **38,5 millones** |

Para meter una imagen en una fully connected hay que **aplanarla**, y ahí se destruye la información espacial: el píxel (10,10) y el (11,10) eran vecinos verticales, pero aplanados quedan en las posiciones 650 y 714 — indistinguibles de cualquier otro par.

Normalización: señal con z-score (global o por-señal según si importa la amplitud absoluta); imágenes por canal, con los `mean=[0.485,0.456,0.406]` de ImageNet como caso típico.

**Por qué no se hace así:**

| Problema | Detalle |
|---|---|
| Params | Crece con la resolución, insostenible |
| Sin invarianza traslacional | Un gato arriba a la izquierda y abajo a la derecha son inputs distintos |
| Sin pesos compartidos | Un detector de bordes se aprende de nuevo en cada posición |

La convolución resuelve los tres: `nn.Conv2d(3, 32, kernel_size=3)` son 896 parámetros contra 3 millones, y funciona mejor.

**Dónde sí se usa fully connected:** después de un extractor.

```
imagen → CNN → vector de 512 features → fully connected → salida
```

Ese vector es funcionalmente un **embedding de la imagen** — la misma idea que el embedding de barrios. El patrón general: una arquitectura especializada convierte el dato estructurado en un vector de tamaño fijo, y a partir de ahí todo vuelve al caso simple.

---

## 8. La capa de salida

La activación de salida es la misma clase de objeto que ReLU, pero se elige con un criterio distinto:

| Capa | Para qué está | Cómo se elige |
|---|---|---|
| Ocultas | Aportar no linealidad | ReLU por defecto; casi no importa |
| **Salida** | **Poner el número en el rango y la interpretación correctos** | **Lo determina la tarea** |

| Activación | Salida cae en | Por qué |
|---|---|---|
| Lineal (ninguna) | ℝ | Un precio puede ser cualquier número |
| Sigmoide | (0, 1) | Una probabilidad |
| Softmax | (0,1), suman 1 | Probabilidades sobre clases excluyentes |
| Softplus / exp | (0, ∞) | Un conteo o un desvío no puede ser negativo |
| Tanh | (−1, 1) | Target acotado y centrado |

"Activación lineal" es una forma elegante de decir **ninguna**. Es la única capa donde no poner activación es correcto.

### Catálogo completo de outputs

| Qué predice | Neuronas | Activación | Loss |
|---|---|---|---|
| Un real (precio) | 1 | Lineal | MSE / MAE / Huber |
| Varios reales (bounding box) | k | Lineal | MSE |
| Sí/no (churn) | 1 | Sigmoide | BCE |
| Una de N clases | N | Softmax | Cross-entropy |
| Varias de N (tags) | N | Sigmoide ×N | BCE |
| Distribución (μ, σ) | 2 | μ lineal, σ softplus | NLL gaussiana |
| Cuantiles (P10, P50, P90) | k | Lineal | Pinball |
| Distribución discretizada | k bins | Softmax | Cross-entropy |
| Conteo (demanda) | 1 | Softplus / exp | Poisson NLL |
| Ranking | 1 por ítem | Lineal | Pairwise / listwise |
| Tiempo hasta evento | 1–2 | Positiva | Survival loss |
| Secuencia (traducción) | vocab × pasos | Softmax por paso | Cross-entropy |
| Imagen (segmentación) | H×W×C | Depende | Por píxel |
| Vector denso (embedding) | d | Lineal | Contrastive / triplet |
| Serie temporal futura | h pasos | Lineal | MSE por paso |

### Predecir una distribución, no un punto

Tres formas distintas:

| Método | Neuronas | Salida | Cuándo |
|---|---|---|---|
| **(a) μ y σ** | 2 | "USD 180.000 ± 25.000" | Si la distribución es aproximadamente normal |
| **(b) Cuantiles** | 3 (P10, P50, P90) | "Entre 150k y 220k, mediana 180k" | **La más usada**; no asume forma |
| **(c) Bins + softmax** | k | Un histograma de precios probables | Distribuciones bimodales o asimétricas |

Los cuantiles son los más rentables en la práctica: no asumen normalidad, dan directamente el intervalo que el negocio quiere, y se implementan en pocas líneas con pinball loss. Detalle: hay que forzar que los cuantiles no se crucen.

### Casos que sorprenden

**Conteos.** Predecir unidades vendidas con MSE y salida lineal permite predicciones negativas y asume varianza constante — en conteos, a mayor media, mayor varianza. Poisson o Negative Binomial con salida positiva es lo correcto.

**Tiempo hasta el evento.** "¿Se va a ir?" es clasificación. "¿Cuándo?" es análisis de supervivencia, con la complicación de los datos **censurados**: los clientes que todavía no se fueron duraron al menos X, pero no sabés cuánto van a durar.

**Ranking.** El output es un orden, no un valor absoluto. Cada ítem recibe un score, pero el loss compara pares o listas enteras.

**Embeddings como salida.** El modelo predice un vector entrenado para que ejemplos similares queden cerca. Base de búsqueda por similitud, reconocimiento facial y recomendación.

### Los pares que no se rompen

Activación de salida y loss se eligen **juntas, siempre**. Softmax con MSE, o sigmoide con cross-entropy categórica, entrenan igual pero convergen mal.

### El detalle de implementación

```python
nn.Linear(32, 1)                # sin sigmoide
loss = nn.BCEWithLogitsLoss()   # ← la sigmoide está acá adentro
```

`BCEWithLogitsLoss` y `CrossEntropyLoss` incluyen la sigmoide/softmax por estabilidad numérica. Si la ponés también en la capa, se aplica dos veces.

Consecuencia: en inferencia tenés que aplicarla vos.

```python
prob = torch.sigmoid(model(x))
```

Error frecuente: el modelo entrena bien y después alguien interpreta un logit de 2.3 como si fuera una probabilidad.

### Los dos errores más comunes

**Softmax cuando debería ser sigmoide.** Un ticket puede ser "urgente" **y** "de facturación". Softmax fuerza que las clases compitan. Si las etiquetas no son excluyentes, la salida está mal modelada de raíz.

**Predecir un punto cuando el negocio necesita un rango.** Si la decisión depende del peor escenario — stock, riesgo, capacidad — un valor puntual no alcanza. La media es la respuesta correcta a una pregunta que nadie hizo.

---

## 9. Diseño de la red: qué se decide y qué no

| Decisión | Cómo se define | Cuánto importa |
|---|---|---|
| Neuronas de entrada | Sale de la codificación de features | **Crítico** |
| Normalización del input | Siempre | **Crítico** |
| Neuronas de salida | Lo determina la tarea | No es decisión |
| Activación de salida | Lo determina la tarea | No es decisión |
| Loss | Acompaña a la activación de salida | No es decisión |
| Cantidad de capas ocultas | 1–3 alcanza para tabular | Medio |
| Neuronas por capa oculta | Potencias de 2, decreciente | **Bajo** |
| Activación oculta | ReLU salvo motivo | Bajo |

**La mitad de la arquitectura no se elige** — sale sola del problema.

### Ancho de las capas ocultas

Criterios, en orden de peso: más ancho que la entrada (para no crear un cuello de botella), potencia de 2 (convención por alineación de memoria), decreciente hacia la salida.

| Datos disponibles | Punto de partida |
|---|---|
| Cientos de filas | 1 capa de 8–16 |
| Miles | 1–2 capas de 32–64 |
| Decenas de miles | 2–3 capas de 64–128 |

La relación que importa es **parámetros vs. cantidad de datos**, no parámetros vs. features.

Procedimiento: empezar chico y mirar el error de train. Alto → falta capacidad, agrandar. Train bien y validación mal → sobra capacidad, achicar o agregar dropout/weight decay.

### `nn.Linear(3, 16)`

| Argumento | Qué es |
|---|---|
| `in_features` = 3 | Tamaño del vector que entra |
| `out_features` = 16 | Cantidad de neuronas de la capa |

Crea `weight` de shape `(16,3)` y `bias` de `(16,)` → 64 parámetros. El `out_features` de una capa tiene que ser el `in_features` de la siguiente.

No incluye activación: la no linealidad va aparte. Sin ReLU en el medio, tres `Linear` seguidos colapsan a una sola transformación lineal.

### Defaults razonables para tabular

- **Normalizar siempre** — sin esto nada más importa
- **Empezar chico** — 32–64 neuronas en una capa oculta es un baseline decente
- **ReLU** por defecto
- **Adam con lr 1e-3**
- **Dropout o weight decay** si se abre el gap train/validation

**Advertencia honesta:** para datos tabulares una red frecuentemente pierde contra gradient boosting (XGBoost, LightGBM). Es un resultado sostenido en la literatura. Las redes brillan cuando hay estructura que explotar — imágenes, texto, señales — no con 20 columnas de un CSV.

---

## 10. Regularización

### Qué problema resuelve

El overfitting es la brecha entre el error de entrenamiento y el de validación.

| Síntoma | Diagnóstico | Qué hacer |
|---|---|---|
| Train alto, validación alto | Underfitting | Más capacidad |
| Train bajo, validación alto | **Overfitting** | Regularizar |
| Train bajo, validación bajo | Bien | Nada |

La regularización no mejora el ajuste — lo **empeora a propósito** en train, a cambio de que generalice mejor. Es un intercambio explícito de sesgo por varianza.

### L2 (weight decay)

Agrega un término al objetivo que penaliza pesos grandes:

```
J = cost + λ · Σ w²
```

El gradiente resultante empuja cada peso hacia cero en cada paso — de ahí el nombre *decay*.

**Por qué funciona:** un peso grande hace que la salida sea muy sensible a esa entrada. Con pesos chicos la función aprendida es más suave, y una función suave es menos capaz de pasar exactamente por cada punto de entrenamiento — que es justamente lo que hace el overfitting.

| Aspecto | Detalle |
|---|---|
| Hiperparámetro | λ, típico 1e-5 a 1e-2 |
| En PyTorch | `Adam(params, weight_decay=1e-4)` |
| Al bias | **No se aplica** — el bias no controla sensibilidad |
| En inferencia | No hace nada, ya está incorporado en los pesos |

### L1

Misma idea con valor absoluto en vez de cuadrado:

```
J = cost + λ · Σ |w|
```

| | L1 | L2 |
|---|---|---|
| Penaliza | `\|w\|` | `w²` |
| Efecto en pesos chicos | Los lleva **exactamente a 0** | Los reduce sin anularlos |
| Resultado | Solución rala, selecciona features | Pesos parejos y chicos |
| Uso en redes | Poco común | **El estándar** |

L1 se usa más en modelos lineales (Lasso) que en redes. **Elastic net** combina ambos.

### Dropout

Durante el entrenamiento, apaga aleatoriamente una fracción de las neuronas en cada forward pass.

| | |
|---|---|
| p típico | 0.2–0.5 en capas ocultas |
| En entrenamiento | Cada neurona se apaga con probabilidad p |
| **En inferencia** | **Se desactiva** — todas las neuronas activas |
| En PyTorch | `nn.Dropout(0.2)` |

**Por qué funciona:** la red no puede depender de ninguna neurona en particular, porque en cualquier paso puede desaparecer. Eso la obliga a distribuir la representación en vez de crear detectores frágiles y coadaptados. Lectura alternativa: es un ensemble implícito de muchas subredes que comparten pesos.

**El detalle que muerde:** `model.train()` y `model.eval()` cambian su comportamiento. Olvidarse de `model.eval()` en inferencia hace que el modelo apague neuronas al azar y devuelva predicciones distintas en cada llamada. Es de los bugs más frecuentes en PyTorch, y afecta también a BatchNorm.

### El resto del arsenal

| Técnica | Cómo actúa | Costo |
|---|---|---|
| **Early stopping** | Corta cuando validación deja de mejorar | Gratis, casi siempre conviene |
| **Data augmentation** | Genera variantes del dato (crops, flips, ruido) | Muy efectivo en visión |
| **Más datos** | Ataca la causa, no el síntoma | Caro, pero es el mejor |
| **Reducir capacidad** | Menos capas o neuronas | Simple y directo |
| **Batch norm** | Efecto regularizador secundario | Ya suele estar |
| **Label smoothing** | Targets 0.9/0.1 en vez de 1/0 | Clasificación |
| **Ensembling** | Promediar varios modelos | Caro en inferencia |

Early stopping es el que menos se menciona y el que más rinde: no tiene hiperparámetro que calibrar y funciona con cualquier arquitectura.

### Cuál usar

| Situación | Elegí |
|---|---|
| Tabular, red chica | L2 + early stopping |
| Red profunda | Dropout + L2 |
| Visión | Data augmentation primero, después dropout |
| Transformers | Dropout bajo (0.1) + weight decay |
| Pocos datos por categoría (embeddings) | Weight decay, agrupar categorías raras |

### Tres matices para no aplicarlo mal

**Regularizar sin overfitting es contraproducente.** Si el error de train ya es alto, agregar dropout empeora las dos métricas. Primero se diagnostica, después se trata.

**Dropout y batch norm se llevan mal.** Combinados en la misma capa pueden degradar el resultado, porque dropout cambia la varianza de las activaciones que batch norm acaba de normalizar. En arquitecturas modernas de visión se usa batch norm y poco o nada de dropout.

**Weight decay sobre embeddings tiene un efecto raro:** empuja a cero también las filas de categorías que no aparecieron en el batch, penalizando justamente a las que ya estaban poco entrenadas. Hay optimizadores con variantes *sparse* para eso.

---

## 11. Los errores que más cuestan

| Error | Ejemplo | Consecuencia |
|---|---|---|
| **Código como número** | Barrio 7 vs. barrio 14 | La red asume que 14 es "el doble" de 7 |
| **ID único como feature** | DNI, número de póliza | Overfitting; train perfecto, test malo |
| **Ordinal como one-hot sin necesidad** | Satisfacción 1–5 en 5 neuronas | Pierde el orden, necesita más datos |
| **No normalizar** | m² y booleanos crudos | Converge lentísimo o no converge |
| **μ, σ del dataset completo** | `fit_transform(X_test)` | Métricas infladas, degradación silenciosa |
| **Fuga temporal** | "Reclamos del cliente" para predecir churn | Métricas excelentes, inservible en producción |
| **Rellenar faltantes con 0** | Cuando 0 es un valor válido | Confunde ausencia con valor |
| **Softmax donde va sigmoide** | Tags no excluyentes | Fuerza competencia entre clases |
| **Doble sigmoide** | Activación en la capa + en el loss | Entrena mal |
| **Olvidar `model.eval()`** | Dropout y BatchNorm activos en inferencia | Predicciones distintas en cada llamada |
| **Regularizar sin overfitting** | Dropout con train error alto | Empeora train y validación |
| **Predecir un punto** | Cuando el negocio necesita un rango | Respuesta a una pregunta que nadie hizo |

---

## 12. Checklist operativo

Para cada variable:

1. ¿Es número, categoría, ciclo, fecha o texto?
2. ¿Qué significa la resta entre dos valores?
3. Si es categoría: ¿tiene orden real? ¿cuántos valores distintos?
4. ¿Puede faltar? ¿faltar significa algo?
5. ¿La voy a tener disponible en el momento de predecir?

Con eso resuelto, la cantidad de neuronas sale sola.

Para la salida:

1. ¿Qué pregunta responde el modelo?
2. ¿El negocio necesita un valor o un rango?
3. ¿Las clases son excluyentes?
4. ¿El valor tiene que ser positivo?

---

## 13. Las ideas de fondo

**El input es una traducción, y como toda traducción puede perder cosas.** La red no ve un cliente, una máquina ni un contrato — ve un tensor. Si la información que importa no está codificada ahí, o está codificada de una forma que borra su estructura, ninguna arquitectura la va a recuperar.

**El trabajo de diseño está casi entero en el input.** La arquitectura de las capas ocultas importa bastante menos que decidir qué variables incluir y cómo codificarlas.

**La red no sabe qué tipo de dato tenía cada posición.** Solo ve floats. Toda la semántica del tipo de variable se perdió en la codificación — por eso codificar mal es fatal: no hay forma de que el modelo lo detecte y lo corrija.

**El aprendizaje funciona por comparación relativa,** y comparar solo tiene sentido entre cosas medidas en la misma escala. Si una variable grita y otra susurra, el modelo escucha la que grita — no porque importe más, sino porque es más ruidosa.

**La mayoría de los errores de producción en ML no están en el modelo, están en la frontera entre el dato crudo y el modelo.** Que la normalización o el diccionario de categorías queden fuera del artefacto es la causa individual más común.

