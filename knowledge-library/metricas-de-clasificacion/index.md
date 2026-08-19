---
topic: Métricas de clasificación: accuracy, matriz de confusión, precisión y recall
language: Español
sources:
  - talk: modelado-redes-neuronales
    date: 2026-08-19
    contributed: Por qué accuracy engaña con clases desbalanceadas, la matriz de confusión como foto completa, precisión, recall y F1 con sus casos de uso, y el umbral como decisión de negocio.
last_updated: 2026-08-19
---

# Métricas de clasificación

Todo este tema trabaja sobre **dos clases**. Con más de dos la idea no cambia: la matriz crece a una fila por clase real y una columna por clase predicha, y precisión y recall se calculan por clase y se promedian.

## Accuracy engaña

**Accuracy** es la fracción de predicciones correctas sobre el total.

![99% de accuracy sobre clases desbalanceadas](images/s5-1-2-desbalance-accuracy.png)

Un detector de fraude sobre 10.000 transacciones, de las que 100 son fraude. La regla más tonta posible, decir siempre "no es fraude", da 9.900 aciertos sobre 10.000: **accuracy 99%** y **cero fraudes detectados**.

- Con clases desbalanceadas el número lo pone la clase mayoritaria, y el error que importa queda escondido adentro.
- Accuracy suma errores de costo muy distinto como si fueran iguales. Dejar pasar un fraude y molestar a un cliente legítimo no son lo mismo.

De ahí la necesidad de separar los tipos de error en vez de resumirlos en un número.

## La matriz de confusión

![La matriz de confusión 2×2](images/s5-2-1-matriz-confusion.png)

Cruza lo que el modelo predijo con lo que era verdad:

- **TP** (verdadero positivo): era positivo y el modelo lo marcó.
- **FP** (falso positivo): era negativo y el modelo lo marcó. Falsa alarma.
- **FN** (falso negativo): era positivo y el modelo lo dejó pasar.
- **TN** (verdadero negativo): era negativo y el modelo lo dejó pasar.

Las dos celdas de error, FP y FN, son las que tienen costos distintos y las que ninguna métrica agregada distingue por sí sola.

## Precisión, recall y F1

**Precisión.** De todo lo que el modelo marcó, ¿cuánto era de verdad? `TP / (TP + FP)`. Sube cuando el modelo molesta poco con falsas alarmas. Importa cuando el falso positivo es caro.

**Recall.** De todo lo que había, ¿cuánto encontró? `TP / (TP + FN)`. Sube cuando se escapan pocos. Importa cuando el falso negativo es caro.

**F1.** ¿Y si las dos importan parecido? `2 · (P · R) / (P + R)`, la media armónica. A diferencia del promedio común, la manda el número más chico: con precisión 0.9 y recall 0.5 el promedio da 0.70 y F1 da 0.64; con recall 0, el promedio da 0.45 y F1 da 0. Esa es la propiedad que la hace útil, porque impide que un 1.0 tape un 0.0: un clasificador que marca todo tiene recall 1.0 con precisión pésima.

Truco mnemotécnico: precisión mira la columna de predichos positivos, recall mira la fila de reales positivos.

**Precisión y recall están en tensión.** Subir una suele bajar la otra. Qué priorizar lo decide el costo del error, no la matemática.

### Tres casos que fijan el criterio

| Caso | Error caro | Métrica |
|---|---|---|
| Filtro de spam: bloquear un mail legítimo es peor que dejar pasar uno dudoso | Falso positivo | Precisión |
| Test de una enfermedad grave y tratable: dejar ir a una persona enferma es lo grave | Falso negativo | Recall |
| Modelo de churn: el descuento regalado y el cliente perdido cuestan parecido | Los dos igual | F1 |

Los dos primeros son espejo: mismo modelo, misma matemática, decisión opuesta. Lo único que cambia es cuánto cuesta cada error, y eso lo define el negocio.

Un cuarto caso que **no** tiene respuesta única y funciona mejor como discusión abierta: una alerta de fraude donde el equipo puede revisar pocas alertas pero cada fraude no detectado cuesta caro. Depende de la capacidad de revisión y del costo del fraude.

## El umbral

![El umbral sobre el eje de probabilidad](images/s5-7-1-umbral.png)

Un clasificador binario no devuelve "sí" o "no", devuelve una probabilidad. El **umbral** es el número que la convierte en decisión, y moverlo reacomoda toda la matriz.

- Bajarlo sube el recall y baja la precisión: el modelo marca más, agarra más verdaderos y también más falsas alarmas.
- Subirlo hace lo contrario.
- **Dejarlo en 0.5 también es una decisión**, no un default neutro.
- La **curva precisión-recall** muestra ese intercambio para todos los umbrales de una vez, y sirve para comparar dos modelos sin fijar ninguno.

Ejemplo operativo: un modelo de fraude con recall bajo en 0.5 pasa a recall alto bajando el umbral a 0.2, a costa de más falsas alarmas que el equipo antifraude tendrá que revisar. Es una perilla de negocio, no de modelado.

## References

- [`../../talks/modelado-redes-neuronales/research/corpus/chat.md.md`](../../talks/modelado-redes-neuronales/research/corpus/chat.md.md) — cubre la capa de salida y el modelado de clasificación, no las métricas.
- **Advertencia de procedencia:** este tema **no** está cubierto por el corpus del Talk de origen. El contenido viene del conocimiento del área y los números del ejemplo de fraude (10.000 transacciones, 100 fraudes) son ilustrativos, no un dato medido. Si se va a enseñar apoyado en una fuente, hace falta sumarla.
