---
topic: Activaciones y capa de salida
language: Español
sources:
  - talk: modelado-redes-neuronales
    date: 2026-08-19
    contributed: Qué es una activación, las cuatro ocultas con sus formas y la saturación, y el catálogo de tarea a salida que fija neuronas, activación y loss.
last_updated: 2026-08-19
---

# Activaciones y capa de salida

## La neurona, en una línea

![Una neurona: de las entradas a la activación](images/s1-3-1-neurona.png)

Una capa hace dos cosas: una combinación lineal y una no linealidad.

- **Pre-activación:** `z = W·x + b`.
- **Activación:** `a = f(z)`. La no linealidad `f` es lo que hace que apilar capas sirva. Sin ella, la composición de capas lineales colapsa a una sola matriz, y una red de cinco capas queda siendo una regresión lineal disfrazada.

Los parámetros de una capa de m neuronas sobre n entradas son `m·n + m`.

Convenciones de layout que cambian entre frameworks y son fuente clásica de errores al portar: PyTorch usa `(out, in)` con `x @ W.T`; Keras usa `(in, out)` con `x @ W`. Misma matemática, transpuesta distinta.

## Las activaciones ocultas

Una **activación oculta** es la función no lineal que se aplica después de `z = W·x + b` en las capas del medio. Su trabajo no es acotar el resultado a un rango con sentido, como en la salida, sino romper la linealidad.

![Formas de ReLU, GELU/SiLU, tanh y sigmoide](images/s1-4-1-activaciones-ocultas.png)

| Función | Fórmula | Rango | Cuándo |
|---|---|---|---|
| ReLU | `max(0, z)` | [0, ∞) | El default de las capas ocultas |
| GELU / SiLU | suavizaciones de ReLU | (−0.3, ∞) aprox. | Transformers |
| Tanh | `(eᶻ − e⁻ᶻ) / (eᶻ + e⁻ᶻ)` | (−1, 1) | Redes recurrentes, salidas centradas |
| Sigmoide | `1 / (1 + e⁻ᶻ)` | (0, 1) | Casi nunca en capas ocultas |

**Por qué ganó ReLU: la saturación.** La sigmoide y la tanh saturan, es decir que con `z` grande su derivada es casi cero, el gradiente que llega a las capas de abajo se apaga y la red deja de aprender. ReLU no satura del lado positivo, y además es baratísima de calcular: son dos rectas pegadas.

La saturación conecta con la normalización de la entrada: una variable grande sin normalizar satura la neurona igual que un `z` grande.

## La capa de salida la determina la tarea

La activación de salida es el mismo tipo de objeto que ReLU, pero se elige con otro criterio: poner el número en el rango y la interpretación correctos. **No hay margen de decisión**, la fija la tarea.

| Qué predice | Neuronas | Activación | Loss |
|---|---|---|---|
| Un real (precio) | 1 | Lineal | MSE / MAE / Huber |
| Sí o no (churn) | 1 | Sigmoide | BCE |
| Una de N clases | N | Softmax | Cross-entropy |
| Varias de N (tags) | N | Sigmoide ×N | BCE |
| Conteo (demanda) | 1 | Softplus / exp | Poisson NLL |
| Cuantiles (P10/50/90) | k | Lineal | Pinball |
| Distribución (μ, σ) | 2 | μ lineal, σ softplus | NLL gaussiana |

"Activación lineal" es una forma elegante de decir ninguna activación. Es la única capa donde no poner activación es lo correcto.

![Formas de las cuatro activaciones de salida](images/s4-3-1-activaciones-salida.png)

La forma explica el uso:

- **Lineal.** Sin piso ni techo, y por eso sirve para un precio: cualquier real es una respuesta válida.
- **Sigmoide.** Aplasta cualquier número en (0, 1). El techo en 1 la convierte en una probabilidad.
- **Softplus.** Piso en 0 y sin techo. La forma correcta para un conteo o un desvío, que no pueden ser negativos. Salida lineal con MSE para conteos permite predicciones negativas, un error clásico.
- **Softmax.** No transforma un valor: reparte 1 entre N clases que compiten. Es la única que necesita ver todas las neuronas de salida a la vez, y si alguien la dibuja como curva, no la entendió.

## Dos errores de modelado de la salida

- **Softmax donde iba sigmoide.** Softmax fuerza a que las clases compitan y sumen 1, así que solo sirve cuando las etiquetas son excluyentes. Un ticket puede ser "urgente" y "de facturación" a la vez, y una película puede ser comedia y drama: ahí van N sigmoides independientes, una por etiqueta.
- **Predecir un punto cuando el negocio pedía un rango.** Si la decisión depende del peor escenario (cuánto stock, cuánto riesgo, cuánta capacidad), un valor puntual no alcanza. Ahí van cuantiles o una distribución. Los cuantiles suelen ser lo más rentable: no asumen forma y dan el intervalo directo.

Los dos comparten causa: la salida se eligió mirando la arquitectura en vez de la pregunta del negocio.

**Detalle de implementación:** `BCEWithLogitsLoss` y `CrossEntropyLoss` ya incluyen la sigmoide y el softmax por estabilidad numérica. Si además se pone la activación en la capa, se aplica dos veces y el modelo entrena mal. En inferencia, con logits crudos: `prob = torch.sigmoid(model(x))`. Un logit de 2.3 no es una probabilidad.

## Qué se decide y qué no

- **Lo determina la tarea, no se decide:** cantidad de neuronas de salida, activación de salida, función de loss.
- **Lo determina la codificación, y es crítico:** cantidad de neuronas de entrada y si se normaliza.
- **Lo que sí se elige, y pesa poco:** cantidad de capas ocultas (1 a 3 alcanza para datos tabulares), ancho de cada capa (potencias de 2, decreciente) y activación oculta (ReLU salvo motivo).

Dato honesto que conviene tener a mano: en datos tabulares una red muchas veces pierde contra gradient boosting (XGBoost, LightGBM). Las redes brillan cuando hay estructura que explotar: imágenes, texto, señales.

## References

- [`../../talks/modelado-redes-neuronales/research/corpus/chat.md.md`](../../talks/modelado-redes-neuronales/research/corpus/chat.md.md) — secciones 1 (conceptos base: activación, pesos y bias), 8 (la capa de salida y los dos errores más comunes) y 9 (diseño de la red: qué se decide y qué no).
- Ver [`codificacion-de-variables`](../codificacion-de-variables/index.md) para el lado de la entrada, y [`metricas-de-clasificacion`](../metricas-de-clasificacion/index.md) para cómo se evalúa la salida que produce esta capa.
