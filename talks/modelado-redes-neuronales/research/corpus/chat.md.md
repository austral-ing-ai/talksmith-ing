---
source_file: chat.md
source_type: chat-export
ingested_at: 2026-08-18
---

# Modelado de inputs y outputs en redes neuronales

## Provenance
- Original location: research/llm-chats/chat.md
- Format: markdown (guía de referencia estilo chat-export)
- Author / source (if known): Exportación de sesión de chat aportada por el presentador (Paulo Veiga)
- Date of original (if known): —

## Key claims

**1. Conceptos base**
- Activación = valor de salida de una neurona. Pre-activación `z = W·x + b`; activación `a = f(z)`. El término tiene tres sentidos (valor, función, tensor de la capa) que no conviene mezclar.
- La no linealidad es lo que hace útil apilar capas: sin ella, la composición de transformaciones lineales colapsa a una sola matriz.
- Funciones: ReLU (default oculto), GELU/SiLU (transformers), Sigmoide (0,1), Softmax (clasificación final), Tanh (−1,1).
- Pesos: neurona = vector `w (n,)`; capa de m neuronas = matriz `W (m,n)`; bias `b (m,)`. Params por capa = `m·n + m`.
- Convención de layout: PyTorch `(out,in)` con `x@W.T`; Keras `(in,out)` con `x@W`. Misma matemática, transpuesta distinta — fuente clásica de errores al portar.
- Batches: input `(B,n)` → salida `(B,m)`, mismos pesos para todas las filas.
- Loss (un ejemplo) vs Cost (promedio) vs Objective (cost + regularización). "Error" a secas es ambiguo (residuo `y−ŷ` / error rate).
- Se entrenan: `W`, `b`, tablas de embeddings. No: input/targets (datos), hiperparámetros. LoRA congela W,b y entrena bajo rango; linear probing solo la última capa.

**2. El input: principio general**
- El input es todo lo que sabés convertido a un vector de floats de tamaño fijo; lo que cambia entre casos es qué significa la posición.
- Pregunta que ordena todo: ¿qué transformaciones puedo aplicar al input sin cambiar la respuesta correcta? → determina la arquitectura natural (tabular→FC, señal→Conv1D/RNN/Transformer, imagen→Conv2D, texto→Transformer, conjunto→Deep Sets/attention, grafo→GNN).
- El eje de canales (RGB) no es espacial ni temporal: se comporta como tabular (variables distintas en el mismo punto), es reordenable. Un kernel 3×3 sobre RGB tiene 27 pesos (abarca todos los canales).
- Convención de orden: PyTorch channels-first `(N,C,H,W)`, TF channels-last `(N,H,W,C)`. Olvidar el permute no explota — da resultados malos, que es peor.
- Multimodal: una rama por modalidad (CNN, embeddings, tabular) → concatenar → FC.

**3. Codificación de variables**
- La pregunta que decide todo: ¿qué significa la resta entre dos valores? (cantidad interpretable → float; orden sin magnitud → ordinal; nada → one-hot/embedding).
- Todo termina en floats, no enteros (los enteros solo aparecen como índice para lookup de embeddings; el gradiente no está definido sobre enteros).
- Booleanos → 1 neurona (0/1). Un tercer estado deja de ser booleano (→ one-hot).
- Enteros con magnitud real → 1 float normalizado, con `log(1+x)` si hay cola larga (ingresos, transacciones, días desde compra).
- Enteros que son códigos → NUNCA como número: ID de barrio→one-hot, código postal/producto→embedding, DNI/CUIT→se descarta (un identificador único no tiene poder predictivo; aprenderlo = memorizar).
- Ordinales → 1 float (0,0.5,1) asume distancias iguales; one-hot pierde el orden; ambos concatenados dejan que la red decida (útil en planes comerciales Free→Enterprise).
- Nominales → one-hot si cardinalidad baja, embedding si alta.
- Cíclicas → 2 neuronas: `sin(2πt/T)`, `cos(2πt/T)`. Ambas necesarias o dos momentos colapsan (23:00 y 00:00 están a 1h pero como números planos a 23).
- Fechas → "cuándo en el ciclo" es cíclico; "hace cuánto" es continuo. Suelen necesitarse las dos.
- Texto → TF-IDF (baseline), embedding promediado, sentence transformer (default hoy), tokens→transformer si importa el orden.
- Faltantes → imputar (media/mediana) + flag binario; nunca rellenar con 0 si 0 es válido; el flag suele ser más predictivo que la variable.
- Cuándo binnear numéricas: relación no monótona (ej. riesgo crediticio que sube-baja-sube con la edad) → binning + one-hot.

**4. One-hot vs. embedding**
- One-hot: una neurona por valor, todas equidistantes (la verdad del dato). `W·x` selecciona una columna de W → cada categoría tiene pesos independientes.
- Comparación: one-hot (k neuronas, no se aprende, todas equidistantes, pocos datos, interpretable) vs embedding (d=8–64, floats densos, se aprende con la red, distancias aprendidas, muchos datos, reutilizable).
- Regla de cardinalidad: ≤15 one-hot; 15–50 cualquiera; ≥50 embedding.
- Dimensión (heurística fast.ai, no teoría): `d ≈ min(50,(k+1)/2)` o `d ≈ k^0.25·1.6`. d crece mucho más lento que k.
- El embedding es matemáticamente equivalente a one-hot seguido de una capa lineal sin bias: hace el lookup sin computar el producto con miles de ceros. Conceptualmente **es la primera capa de la red**.
- Gradiente ralo: solo se actualizan las filas de los índices presentes en el batch. Una categoría rara queda casi en su inicialización.
- Dos ventajas no obvias: comparte estadística (categorías parecidas quedan cerca) y es reutilizable (clustering, similitud, input de otro modelo).
- Puente a LLMs: un LLM empieza igual — cada token es un índice a una tabla ~50.000×4096. "Un embedding es una representación densa aprendida donde la geometría del espacio codifica el significado."
- Regla adentro/afuera: si tiene parámetros entrenables va adentro; si es transformación fija (sentence transformers, RAG) puede ir afuera.

**5. Escalas y normalización**
- `∂J/∂wⱼ = δ·xⱼ`: el gradiente es proporcional a la entrada, pero el learning rate es uno solo para toda la red → escalas dispares hacen que el gradiente apunte a la pared y zigzaguee (número de condición de la Hessiana).
- Efecto secundario: entradas grandes saturan sigmoide/tanh (derivada ≈0); Xavier/He asumen media 0, varianza ~1.
- Qué normalizar: features de entrada siempre; one-hot/booleanos no; salidas ocultas opcional (Batch/LayerNorm); target en regresión conviene y desescalar al predecir.
- Métodos: z-score (default), min-max (rango fijo), log+z-score (cola larga), robust scaling (outliers).
- "Float normalizado" = cuántos desvíos por encima/debajo del promedio; la unidad original desaparece.
- El mismo problema aparece entre capas: si cada capa multiplica la escala por c, el efecto es multiplicativo (c=1.5 → ×58 tras 10 capas) = exploding/vanishing gradients. Herramientas: Xavier/He, BatchNorm (por feature sobre el batch), LayerNorm (por ejemplo sobre features; ganó en NLP por no depender del batch), conexiones residuales.
- Un solo concepto unifica cuatro temas que se enseñan sueltos: normalización del input, inicialización, normalización interna, control de gradientes.
- Advertencias: Adam mitiga pero no resuelve; árboles/GBM son invariantes a monótonas (no normalizan); escala pareja ≠ importancia pareja (la importancia la aprenden los pesos).

**6. μ, σ y el artefacto de producción**
- μ,σ se calculan SOLO con train; usarlos de todo el dataset es data leakage (con μ,σ el efecto es chico, pero enorme con target encoding, imputación, feature selection, PCA). Regla: todo lo que se aprende de los datos se aprende solo del train, incluidas las transformaciones.
- Se guardan y se reaplican idénticos en validación, test y producción. Normalizar en prod con μ distinto = predicción incorrecta silenciosa (no hay error).
- "El modelo" en producción no es solo W,b: son los pesos + μ,σ de cada variable + diccionario categoría→índice + valores de imputación. Guardar solo los pesos lo hace inutilizable.
- Bug clásico: `scaler.fit_transform(X_test)` (mal) vs `scaler.fit(X_train); scaler.transform(X_test)` (bien).
- Dónde vive la normalización en inferencia: A manual (alto riesgo de skew), B pipeline (estándar sklearn), C en el grafo (más robusta, menos usada; ONNX/TF Serving/Keras `Normalization()`), D feature store. Regla: preprocesamiento y modelo se despliegan juntos siempre.
- Data drift: NO recalcular μ,σ en prod; detectar drift, reentrenar y desplegar paquete nuevo con sus propios μ,σ.

**7. Ejemplos completos** (con arquitecturas y conteos de parámetros)
- 12 barrios + m²: 13 neuronas (1 m² normalizado + 12 one-hot), `13→32→16→1`, MSE, 993 params. One-hot da rectas paralelas (bias por barrio); las capas ocultas construyen la interacción "en Palermo el m² vale más por metro".
- 3 numéricas PyTorch: normalizar solo continuas (el booleano queda intacto), `nn.Linear(3,16)→ReLU→Linear(16,8)→ReLU→Linear(8,1)`, 209 params.
- 500 barrios con embedding d=24: 27 neuronas vs 503 con one-hot; embedding = 75% del modelo (15.905 params). `nn.Embedding` exige enteros (torch.long). Problemas: barrios raros (agrupar en OTRO), desconocido (índice 0 = `<UNK>`), overfitting (dropout, weight decay). Artefacto incluye state_dict + barrio2idx + mu/sigma.
- Señal/imagen: aplanar una imagen en FC destruye la info espacial y explota en params (RGB 224×224 = 150.528 entradas → 38,5M en la 1ª capa). La convolución resuelve params, invarianza traslacional y pesos compartidos. Patrón general: arquitectura especializada → vector de tamaño fijo (embedding de la imagen) → caso simple.

**8. La capa de salida**
- La activación de salida se elige por la tarea (poner el número en el rango/interpretación correcta), no por aportar no linealidad: Lineal→ℝ (precio), Sigmoide→(0,1) prob, Softmax→clases excluyentes, Softplus/exp→(0,∞) conteos, Tanh→acotado.
- Catálogo completo output→(neuronas, activación, loss): real/MSE, binario/sigmoide+BCE, N clases/softmax+CE, tags/sigmoide×N+BCE, distribución μ,σ/NLL gaussiana, cuantiles/pinball, conteo/softplus+Poisson NLL, ranking/pairwise, supervivencia, secuencia/CE por paso, embedding/contrastive.
- Predecir distribución no punto: (a) μ,σ si normal; (b) cuantiles P10/P50/P90 — la más usada, no asume forma, da el intervalo del negocio (forzar que no se crucen); (c) bins+softmax para bimodales.
- Casos que sorprenden: conteos (Poisson, no MSE con salida lineal); tiempo-hasta-evento (supervivencia + datos censurados); ranking (score por ítem, loss sobre pares/listas); embeddings como salida (similares quedan cerca).
- Activación de salida y loss se eligen JUNTAS siempre; pares mal combinados convergen mal.
- Detalle de implementación: `BCEWithLogitsLoss`/`CrossEntropyLoss` incluyen la sigmoide/softmax por estabilidad numérica — no ponerla también en la capa (doble sigmoide entrena mal); en inferencia aplicarla vos (`torch.sigmoid`).
- Dos errores comunes: softmax donde va sigmoide (clases no excluyentes); predecir un punto cuando el negocio necesita un rango.

**9. Diseño de la red: qué se decide y qué no**
- La mitad de la arquitectura no se elige: neuronas de entrada (salen de la codificación), normalización (siempre), neuronas/activación de salida y loss (los determina la tarea). Sí se elige: cantidad de capas (1–3 para tabular), ancho (potencias de 2, decreciente), activación oculta (ReLU).
- Ancho: más ancho que la entrada (no crear cuello de botella), potencia de 2, decreciente. La relación que importa es params vs cantidad de datos, no params vs features.
- Procedimiento: empezar chico, mirar error de train. Alto→falta capacidad; train bien y validación mal→sobra capacidad (achicar o dropout/weight decay).
- `nn.Linear(3,16)`: in_features=3, out_features=16 → weight (16,3) + bias (16,) = 64 params. Sin ReLU en el medio, tres Linear colapsan a una transformación lineal.
- Advertencia honesta: en tabular una red frecuentemente pierde contra gradient boosting (XGBoost/LightGBM) — resultado sostenido. Las redes brillan con estructura (imágenes, texto, señales), no con 20 columnas de CSV.

**10. Regularización**
- Overfitting = brecha entre error de train y de validación. Diagnóstico: train alto+val alto=underfitting (más capacidad); train bajo+val alto=overfitting (regularizar); ambos bajos=bien.
- La regularización empeora el ajuste en train a propósito a cambio de mejor generalización: intercambio explícito de sesgo por varianza.
- **L2 (weight decay):** `J = cost + λ·Σw²`. El gradiente empuja cada peso hacia cero en cada paso (de ahí "decay"). Por qué funciona: un peso grande hace la salida muy sensible a esa entrada; pesos chicos → función más suave → menos capaz de pasar por cada punto de train (que es lo que hace el overfitting). λ típico 1e-5 a 1e-2; `Adam(params, weight_decay=1e-4)`; NO se aplica al bias (no controla sensibilidad); en inferencia no hace nada (ya está en los pesos).
- **L1:** `J = cost + λ·Σ|w|`. Lleva pesos chicos exactamente a 0 (solución rala, selecciona features) vs L2 que los reduce sin anular. Poco común en redes (más en Lasso lineal); Elastic net combina ambos.
- **Dropout:** apaga aleatoriamente una fracción de neuronas por forward pass (p 0.2–0.5). En inferencia se DESACTIVA (todas activas). Por qué funciona: la red no puede depender de ninguna neurona → distribuye la representación (ensemble implícito de subredes). Bug que muerde: olvidar `model.eval()` → predicciones distintas cada llamada (afecta también BatchNorm).
- Resto del arsenal: early stopping (gratis, el que más rinde y menos se menciona), data augmentation (visión), más datos (ataca la causa), reducir capacidad, batch norm (regularizador secundario), label smoothing, ensembling.
- Cuál usar: tabular chica→L2+early stopping; profunda→dropout+L2; visión→augmentation+dropout; transformers→dropout 0.1+weight decay; embeddings→weight decay+agrupar raras.
- Tres matices: regularizar sin overfitting empeora ambas métricas (diagnosticar primero); dropout y batch norm se llevan mal (dropout cambia la varianza que BN normalizó); weight decay sobre embeddings penaliza filas que no aparecieron en el batch (variantes sparse).

**11. Los errores que más cuestan** (tabla): código como número, ID único como feature, ordinal como one-hot sin necesidad, no normalizar, μ/σ del dataset completo, fuga temporal, rellenar faltantes con 0, softmax donde va sigmoide, doble sigmoide, olvidar `model.eval()`, regularizar sin overfitting, predecir un punto.

**12. Checklist operativo** — por variable: ¿número/categoría/ciclo/fecha/texto? ¿qué significa la resta? ¿tiene orden real y cuántos valores? ¿puede faltar y significa algo? ¿la tendré al momento de predecir? Para la salida: ¿qué pregunta responde? ¿valor o rango? ¿clases excluyentes? ¿debe ser positivo?

**13. Ideas de fondo** — el input es una traducción que puede perder cosas; el trabajo de diseño está casi entero en el input; la red solo ve floats (la semántica del tipo se perdió en la codificación); el aprendizaje funciona por comparación relativa entre cosas en la misma escala; la mayoría de los errores de producción están en la frontera dato crudo↔modelo, no en el modelo.

## Definitions and terminology
- **Activación** — valor emitido por una neurona (`a = f(z)`); también la función `f` o el tensor de salida de una capa.
- **Loss / Cost / Objective** — error de un ejemplo / promedio sobre el dataset / lo que se optimiza (cost + regularización).
- **One-hot** — vector con un 1 y el resto 0, una posición por categoría; categorías equidistantes.
- **Embedding** — tabla `k×d` de floats entrenable; representación densa aprendida donde la geometría codifica el significado; equivalente a one-hot × capa lineal sin bias.
- **Normalización / z-score** — `(x−μ)/σ`; expresa el valor en desvíos respecto al promedio.
- **Data leakage** — información del test/futuro que se filtra al entrenamiento (ej. μ,σ calculados sobre todo el dataset).
- **Weight decay (L2)** — penalización `λ·Σw²` en el objetivo que empuja los pesos hacia cero.
- **Dropout** — apagar neuronas al azar en entrenamiento; desactivado en inferencia.
- **Overfitting / underfitting** — brecha train-validación alta / error de train alto.
- **Exploding/vanishing gradients** — crecimiento/decaimiento multiplicativo de escala entre capas.

## Evidence and examples
- Código PyTorch: normalización selectiva de columnas continuas; `PrecioNet` con `nn.Embedding(500,24)`; artefacto `torch.save` con state_dict + barrio2idx + mu/sigma/y_mu/y_sigma; `BCEWithLogitsLoss` con logits crudos.
- Conteos de parámetros como ejemplos concretos: 12 barrios `13→32→16→1` = 993 params; 3 numéricas = 209 params; 500 barrios embedding = 15.905 params (embedding = 75%); FC sobre RGB 224×224 = 38,5M solo en la 1ª capa vs `nn.Conv2d(3,32,3)` = 896 params.
- Tablas de codificación por tipo de variable, catálogo de outputs (qué predice → neuronas/activación/loss), tabla de errores costosos, opciones de dónde vive la normalización (A/B/C/D).
- Heurísticas de dimensión de embedding (fast.ai): k=50→d=12, k=10.000→d=48, k=1M→d=64–128.

## Inconsistencies / open questions
- **La fuente NO cubre la matriz de confusión** ("red de confusión" en el briefing) — no hay sección sobre matriz de confusión, precision/recall, verdaderos/falsos positivos ni métricas de clasificación derivadas. La guía toca clasificación (softmax, cross-entropy, "error rate") pero no la evaluación con matriz de confusión. **Gap a llenar** (conocimiento del agente o fuente adicional) si esa sección va en la charla.
- La guía es notablemente honesta sobre límites: reconoce que en tabular las redes suelen perder contra gradient boosting — útil como contrapunto pero puede chocar con una charla centrada en redes; decidir cómo enmarcarlo para estudiantes de ingeniería.
- Cobertura muy amplia (13 secciones): excede el alcance del briefing (diseño, input/output, matriz de confusión, overfitting, L2). Habrá que recortar fuerte — el input/codificación ocupa la mayor parte de la fuente, pero el briefing pesa más hacia salida + evaluación + regularización.

## Images / diagrams
Ninguna imagen embebida. Los diagramas del original son ASCII/tablas markdown, preservados textualmente en *Raw / preserved excerpts* (ej. el diagrama multimodal §2, el pipeline `imagen → CNN → vector → FC` §7). Companion folder vacío (válido).

## Raw / preserved excerpts

Guía completa preservada verbatim (13 secciones, ~1070 líneas). Fuente canónica para citar en slides.

### 1. Conceptos base

**Activación** — El valor de salida de una neurona. Pre-activación `z = W·x + b`; activación `a = f(z)`. Tres sentidos: activación (valor = el número que emite la neurona), función de activación (la transformación no lineal `f`), activaciones plural (tensor de salidas de una capa para un batch). Por qué existe la no linealidad: sin ella, apilar capas no sirve; la composición de transformaciones lineales sigue siendo lineal y la red colapsa a una sola matriz. Funciones: ReLU `max(0,z)` (capas ocultas, default); GELU/SiLU (suavizado de ReLU, transformers); Sigmoide (0,1) (salida binaria, gates LSTM); Softmax (distribución que suma 1, capa final de clasificación); Tanh (−1,1) (RNN clásicas).

**Pesos y bias** — Una neurona: vector `w (n,)`; capa de m neuronas: matriz `W (m,n)`; bias `b (m,)`. Params por capa = `m·n + m`. Layout: PyTorch guarda `weight` como `(out,in)` y hace `x@W.T`; Keras usa `(in,out)` y hace `x@W` — misma matemática, transpuesta distinta, fuente clásica de errores al portar código. Batches: input `(B,n)`, salida `(B,m)`, los pesos son los mismos para todas las filas.

**Loss, cost, error, objective** — Loss: error de un solo ejemplo. Cost: promedio del loss sobre el dataset o batch. Error function: término genérico ambiguo. Objective: lo que se optimiza = cost + regularización. La distinción loss/cost viene de los cursos de Andrew Ng; Bishop y Goodfellow usan "error function"/"cost function" indistintamente; en papers modernos se dice "loss" para todo. Cuidado con "error" a secas: en estadística es el residuo `y−ŷ`, y "error rate" es la proporción de clasificaciones incorrectas — una métrica, no algo diferenciable.

**Qué cambia durante el entrenamiento** — Se entrena: `W`,`b` (parámetros), tabla de embeddings. No: input `x`/targets `y` (datos), learning rate/capas/batch size (hiperparámetros). Activaciones cambian como consecuencia del forward. Estado del optimizador (momentos de Adam) se guarda pero no es parte del modelo. En fine-tuning moderno se relaja: LoRA congela `W`,`b` y entrena una matriz de bajo rango aparte; linear probing entrena solo la última capa.

### 2. El input: principio general

El input es todo lo que sabés, convertido a números; todo termina en un vector de floats de tamaño fijo. Lo que diferencia los casos es qué significa la posición dentro de ese vector. Familias: features tabulares (una variable distinta, orden arbitrario), píxeles (intensidad en una posición, vecindad 2D), señal (amplitud en un instante, vecindad 1D). Pregunta que ordena el zoológico: ¿qué transformaciones puedo aplicarle al input sin cambiar la respuesta correcta? → sin estructura/tabular (cambiar orden de columnas)→FC; grilla 1D/señal→Conv1D/RNN/Transformer; grilla 2D/imagen→Conv2D; grilla 3D→Conv3D; secuencia discreta/texto (el orden es todo)→Transformer; conjunto→Deep Sets/attention; grafo→GNN.

Familias completas (ejemplo de negocio → cómo entra): Tabular/scoring crediticio/vector normalizado; Imagen/QA visual/tensor (C,H,W); Señal 1D/vibración/vector o espectrograma; Texto/reclamos/tokens→embeddings; Serie temporal multivariada/demanda por SKU/matriz (tiempo,variables); Video/góndola/(T,C,H,W); Grafo/fraude/nodos+aristas; Conjunto/carrito/colección sin orden+agregación; Nube de puntos/LiDAR/(N,3); Eventos-logs/journey/secuencia (evento,timestamp); Multimodal/tasación con fotos+texto+datos/rama por modalidad→concatenar.

El eje de canales: RGB introduce un eje que no es espacial ni temporal. Espacial(H,W) y temporal(T) tienen vecindad y no son reordenables; el canal(C) no tiene relación entre posiciones (R no está "cerca" de G) y SÍ es reordenable — se comporta como el caso tabular. Un filtro convolucional se desliza sobre H y W pero abarca todos los canales de una vez: kernel 3×3 sobre RGB = 3×3×3 = 27 pesos, no 9. Casos (ejes con vecindad / canales): foto RGB (H,W / 3), satelital multiespectral (H,W / 13 bandas), resonancia (H,W,D / 1+), video (T,H,W / 3), audio estéreo (T / 2), ECG 12 derivaciones (T / 12). Una serie de ventas de 40 SKUs es matemáticamente lo mismo que una imagen de 1 píxel de alto con 40 canales — por eso las conv 1D funcionan en forecasting. Convención de orden: PyTorch channels-first `(N,C,H,W)`, TensorFlow channels-last `(N,H,W,C)`; olvidarse del `permute` no explota, entrena y da resultados malos (peor).

Multimodal:
```
fotos    → CNN        → (128,)  ┐
texto    → embeddings → (768,)  ├→ concat (912,) → FC → precio
tabular  → (16,)               ┘
```

### 3. Codificación de variables

La pregunta que decide todo: frente a un número, ¿qué significa la resta entre dos valores? Da cantidad interpretable→float normalizado 1 neurona; da orden pero no magnitud confiable→ordinal (evaluar one-hot también); no significa nada→one-hot o embedding según cardinalidad; no se puede ni plantear→probablemente no sea feature.

Tabla base (tipo → neuronas → qué va): numérica continua/1/valor normalizado; binaria/1/0.0 o 1.0; categórica k valores/k/one-hot; categórica dummy/k−1/base "todo 0"; ordinal/1/0,0.5,1; categórica alta cardinalidad/d(8–64)/embedding aprendido; cíclica/2/sin y cos; faltante/+1/flag binario.

Todo termina en floats, no enteros: `(x−μ)/σ` no es representable ni tiene gradiente sobre enteros. Los enteros aparecen en un solo lugar: como índice para buscar en una tabla de embeddings — el entero no entra a la red, entra al lookup.

Booleanos → 1 neurona (tiene cochera, cliente activo, es feriado). Fumador sí/no/no-declara → one-hot 3 neuronas: un booleano con tercer estado deja de ser booleano.

Enteros con magnitud real → 1 float normalizado: ambientes/antigüedad/hijos (sin transformación); días desde última compra, transacciones, ingreso mensual, empleados → `log(1+x)`; cantidad de reclamos → `log(1+x)`+flag "es cero". El log aparece con colas largas: la diferencia entre 1 y 10 transacciones importa más que entre 4000 y 4010.

Enteros que son códigos → NUNCA como número: ID de barrio (1–48)→one-hot 48; código postal→embedding 32 o jerárquico por prefijo 3–5; ID de producto (2M)→embedding 64; código CIIU→una feature por nivel (4 one-hots); DNI/CUIT/nº póliza→se descarta (0). Un identificador único no tiene poder predictivo; si el modelo "aprende" de él está memorizando ejemplos individuales.

Ordinales: nivel educativo (1 float o one-hot); plan Free/Basic/Pro/Enterprise (ambos concatenados 1+4); satisfacción 1–5 (1 float); severidad (1 float); rating crediticio (1 float). Un float 0,0.5,1 asume distancias iguales; one-hot no asume distancias pero pierde el orden; ambos concatenados le dejan a la red decidir. Los planes comerciales son el caso donde conviene ambos: Pro→Enterprise suele ser mayor salto que Free→Basic.

Nominales (cardinalidad → codificación): tipo propiedad 5/one-hot; canal 8/one-hot; provincia 24/one-hot; marca auto 60/embedding 16; rubro 400/embedding 32; ciudad 3000/embedding 48; modelo celular 20.000/embedding+hashing 64.

Cíclicas → 2 neuronas `sin(2πt/T)`, `cos(2πt/T)`: hora del día (24), día semana (7), mes (12), día del año (365), dirección viento (360°). Ambas necesarias: con una sola, dos momentos distintos colapsan al mismo valor. Las 23:00 y 00:00 están a 1 hora pero como números planos a 23.

Fechas (feature derivada / qué captura): hora cíclica/patrón diario; día de semana cíclica/patrón semanal; mes cíclico/estacionalidad; feriado-finde/anomalías calendario; días desde el evento/recencia; tiempo absoluto/tendencia largo plazo. "Cuándo en el ciclo" es cíclico; "hace cuánto" es continuo — dos preguntas distintas, suelen necesitarse las dos.

Texto: bag of words (legacy, muy ralo), TF-IDF (baseline decente), embedding promediado 100–300 (simple y sólido), sentence transformer 384–1536 (default hoy), tokens→transformer (cuando el orden importa).

Faltantes: falta al azar→imputar media/mediana + flag binario; falta por motivo→categoría propia "NO_INFORMADO"; falta mucho (>50%)→considerar descartar; numérica que puede ser 0→nunca rellenar con 0. El flag cuesta una neurona y muchas veces es más predictivo que la variable misma.

Casos que no encajan limpio: monto en varias monedas→convertir+log+z-score; porcentaje 0–100→÷100; rango declarado→dos floats min/max; lista de tags→multi-hot; coordenadas lat/lon→proyección 3D o distancia a puntos clave; versión software→un float por componente; temperatura °C→min-max con rango conocido.

Otros métodos categóricas: target encoding (1, alta fuga sin CV interna), hashing (d fijo, colisiones), frecuencia (1, pierde identidad). Numéricas cuándo binnear: estandarización (default), min-max (rango conocido), log+estandarización (cola larga), quantile (outliers), binning+one-hot k (relación NO monótona), binning+valor 2. Si el riesgo crediticio sube con la edad hasta 30, baja hasta 55 y vuelve a subir, un solo número obliga a la red a aprender esa curva; los bins se la dan servida.

### 4. One-hot vs. embedding

One-hot: una neurona por valor posible, todas en 0 salvo una en 1 (Casa/Depto/PH/Local). Todas las categorías equidistantes = exactamente la verdad del dato; codificar Casa=1,Depto=2,PH=3 impondría orden y distancias inventadas. Como solo una posición vale 1, `W·x` selecciona una columna de W: cada categoría tiene su propio conjunto de pesos independiente. Dummy encoding (k−1, importa en lineales, irrelevante en redes); categoría desconocida (todo 0 o columna "OTRO"); no hace falta normalizar; multi-hot (varios 1 si admite varios valores).

Comparación (one-hot / embedding): neuronas k / d(8–64); contenido ceros+un 1 / floats densos; ¿se aprende? no / sí con la red; distancia entre categorías todas iguales / la aprende de los datos; datos necesarios pocos / muchos; interpretabilidad alta / baja; reutilizable no / sí.

Cuándo cada uno (cardinalidad): ≤15 one-hot; 15–50 cualquiera (one-hot si pocos datos); ≥50 embedding. Otros criterios: pocos datos→one-hot; interpretar coeficientes→one-hot; reusar representación→embedding; categorías nuevas seguido→embedding+hashing.

Dimensión del embedding (heurísticas fast.ai, no teoría): `d ≈ min(50,(k+1)/2)`, `d ≈ k^0.25·1.6`. k=50→d=12; k=500→d=24; k=10.000→d=48; k=1M→d=64–128. d crece mucho más lento que k.

Cómo funciona: tabla de `k×d` floats, entrenable como cualquier peso. Categoría→índice entero (afuera, preprocesamiento); índice→vector de d floats (adentro, primera capa); vector→capas ocultas→salida. Es matemáticamente equivalente a one-hot seguido de una capa lineal sin bias: multiplicar un one-hot por una matriz `(d,k)` selecciona una columna; el embedding hace ese lookup sin computar el producto con miles de ceros. Conceptualmente la tabla de embeddings ES la primera capa de la red, aplicada a un one-hot implícito; se piensa como "codificación del input" por costumbre, pero está del lado del modelo.

Gradiente ralo: linear actualiza todas las filas por batch (gradiente denso); embedding solo las de los índices presentes (ralo). Un batch de 32 propiedades toca como mucho 32 filas; un barrio que aparece 3 veces recibe 3 actualizaciones y queda casi en su inicialización. Dos ventajas no obvias: comparte estadística (con one-hot cada categoría aprende aislada, un producto con 3 ventas no aprende nada; con embedding queda cerca de productos parecidos y hereda parte de lo aprendido); es reutilizable (clustering, similitud, input de otro modelo).

Puente a LLMs (qué se embebe): tabular/categorías, NLP/palabras-tokens, recomendación/usuarios-productos, grafos/nodos, RAG/documentos. Un LLM empieza así: cada token es un índice que busca su fila en una tabla de ~50.000×4096. "Un embedding es una representación densa aprendida donde la geometría del espacio codifica el significado." Cuándo el embedding va afuera: categoría en tabular (adentro, desde cero); Word2Vec/GloVe (adentro, cargado, a veces congelado); sentence transformers (afuera, es otro modelo); RAG/búsqueda semántica (afuera, vector DB). Regla: si tiene parámetros que querés entrenar va adentro; si es transformación fija puede ir afuera.

### 5. Escalas y normalización

Por qué importa: `∂J/∂wⱼ = δ·xⱼ` — el gradiente respecto a un peso es proporcional al valor de la entrada. Si `x₁`=m²≈200 y `x₂`=cochera∈{0,1}, el gradiente de `w₁` es ~200× mayor, pero el learning rate es uno solo para toda la red. Escalas parejas: curvas de nivel circulares, el gradiente apunta al mínimo, converge en pocos pasos. Escalas dispares: elipses alargadas, el gradiente apunta a la pared, zigzaguea. Formalmente: el número de condición de la Hessiana; normalizar lo baja y la velocidad de convergencia depende directamente de él. Efecto secundario: con sigmoide/tanh una entrada grande empuja `z` a la zona plana (derivada ≈0), la neurona se satura y deja de aprender; además Xavier y He asumen entradas con media 0 y varianza ~1.

Qué normalizar: features de entrada siempre; one-hot y booleanos no (ya en 0/1); salidas de capas ocultas opcional (BatchNorm/LayerNorm); target en regresión conviene y desescalar al predecir. Métodos: z-score `(x−μ)/σ` (default); min-max `(x−min)/(max−min)` (rango fijo); log+estandarización (cola larga); robust scaling mediana e IQR (outliers). "Float normalizado" con m² media 95 desvío 40: 85→−0.25, 95→0.00, 175→+2.00. La unidad desaparece; la escala pasa a ser "cuántos desvíos por encima/debajo del promedio".

El mismo problema entre capas (qué viaja / cómo se controla): datos→capa1 features x (normalización del input); capa1→capa2 activaciones a₁ (inicialización + Batch/LayerNorm); última capa→loss predicción ŷ (escala del target). Si cada capa multiplica la escala por c, el efecto es multiplicativo: c=1.2→×6, c=1.5→×58, c=0.8→×0.1, c=0.5→×0.001 tras 10 capas = exploding/vanishing gradients (mismo fenómeno en forward y backward). Herramientas: Xavier/He (elige Var(W) para c≈1 al inicio), BatchNorm (renormaliza sobre el batch por feature), LayerNorm (sobre las features por ejemplo, ganó en NLP por no depender del batch), conexiones residuales (camino directo al gradiente). Un solo concepto unifica cuatro temas que se enseñan sueltos: normalización del input, inicialización de pesos, normalización interna y control de gradientes.

Dos advertencias: Adam mitiga pero no resuelve (escala el paso por parámetro, absorbe parte; a veces un modelo sin normalizar "funciona igual", pero la saturación y la inicialización rota no se arreglan con el optimizador). No aplica a todo: árboles y gradient boosting son invariantes a transformaciones monótonas, no necesitan normalización — es particularidad de métodos basados en gradiente. Escala pareja ≠ importancia pareja: normalizar no le quita importancia a una variable (la importancia la aprende la red vía los pesos), solo la pone en condiciones de ser evaluada.

### 6. μ, σ y el artefacto de producción

Solo con train: μ,σ solo de train → el test es realmente desconocido, métrica confiable; μ,σ de todo el dataset → información del test se filtró, métrica optimista = data leakage (con μ,σ el efecto es chico, pero enorme en target encoding, imputación, feature selection, PCA). Regla: todo lo que se "aprende" de los datos se aprende solo del train, incluidas las transformaciones. Se guardan y reaplican: entrenamiento (calculados de train), validación/test/producción (los de train). Si en producción normalizás con μ=120 en vez de 95, una propiedad de 175 m² entra como +1.375 en vez de +2.00; el modelo la lee más chica — no hay error, no hay excepción, predicción incorrecta silenciosa.

Qué es "el modelo" en producción: no es solo W y b, son los pesos + μ,σ de cada variable + diccionario categoría→índice (u orden de columnas del one-hot) + valores de imputación de faltantes. Si guardás solo los pesos, el modelo es inutilizable. Bug clásico:
```python
# MAL — μ y σ del test
scaler.fit_transform(X_test)
# BIEN — μ y σ de train
scaler.fit(X_train)
scaler.transform(X_test)
```
Un `fit` de más y el modelo se degrada sin dar ningún error.

Dónde vive la normalización en inferencia (opción / dónde vive / qué recibe el modelo / riesgo de skew): A Manual (código que llama / vector ya normalizado / alto); B Pipeline (objeto serializado / valores crudos / bajo); C En el grafo (capa de la red / valores crudos / muy bajo); D Feature store (servicio centralizado / features transformadas / muy bajo, costoso). Frecuencia real: tabular sklearn→B (estándar de facto); DL imágenes→A (torchvision.transforms fuera del modelo); ONNX/TF Serving/edge→C (artefacto autocontenido); Keras moderno→C (`layers.Normalization()` con `adapt()`); producción industrial madura→D. La C es la más robusta y la menos usada; en visión domina A por razones históricas (el preprocesamiento corre en CPU mientras la GPU entrena, y ahí está la augmentación que no debe correr en inferencia). Regla: el preprocesamiento y el modelo se despliegan juntos siempre; el que consume el modelo no debería tener que saber que la normalización existe.

Data drift: con el tiempo la distribución real cambia; la solución NO es recalcular μ,σ en producción sino detectar el drift, reentrenar con datos nuevos y desplegar un paquete nuevo con sus propios μ,σ — se actualizan junto con los pesos, nunca por separado.

### 7. Ejemplos completos

Barrios + m² (12 barrios): posición 1 = m² normalizado (85 m² Palermo → −0.25); posiciones 2–13 = barrio one-hot. 13 neuronas. Como el one-hot activa una sola posición, cada barrio tiene su propio bias efectivo (`precio ≈ w_m2·m²_norm + w_palermo`), rectas paralelas una por barrio — pero eso es lo que haría un modelo lineal; una red con capas ocultas puede aprender que en Palermo el m² vale más por metro (interacción que construye sola). Arquitectura `13→32→16→1`, salida lineal, MSE, 993 parámetros.

Tres numéricas (PyTorch): agua de pozo (booleano), m² cubiertos, superficie terreno.
```python
X_raw = torch.tensor([
    [1.0,  85.0,  300.0],
    [0.0, 120.0,  400.0],
    [1.0,  60.0,  250.0],
    [0.0, 200.0, 1000.0],
], dtype=torch.float32)
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
3 neuronas de entrada, 209 parámetros. El booleano no se normaliza. Feature derivada útil: ratio cubierto/terreno. Inferencia: `pred = model(preprocess(nueva)) * y_sigma + y_mu` (desescalar).

Con 500 barrios (embedding): agua de pozo 0/1 (1), m² z-score (1), terreno z-score (1), barrio 500 embedding d=24 (24) → 27 neuronas (vs 503 con one-hot).
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
Dos entradas separadas: índices `torch.long`, numéricas `float32`. `nn.Embedding` exige enteros. Params: embedding (500,24)=12.000; Linear 27→64=1.792; 64→32=2.080; 32→1=33; total 15.905. El embedding es el 75%. Tres problemas con 500 categorías: barrios con pocos ejemplos (agrupar raros en "OTRO", subir weight decay); barrio desconocido en producción (reservar índice 0 para `<UNK>`); overfitting 12k params (dropout, weight decay). Artefacto:
```python
torch.save({
    "state_dict": model.state_dict(),
    "barrio2idx": barrio2idx,
    "mu": mu, "sigma": sigma,
    "y_mu": y_mu, "y_sigma": y_sigma,
}, "modelo.pt")
```

Señal, imagen gris, RGB (shape crudo / neuronas / params 1ª capa a 256): señal 1000 (1.000 / 256 mil); gris 64×64 (4.096 / 1M); RGB 64×64 (12.288 / 3,1M); RGB 224×224 (150.528 / 38,5M). Aplanar una imagen en FC destruye la info espacial: el píxel (10,10) y (11,10) eran vecinos verticales pero aplanados quedan en 650 y 714, indistinguibles. Por qué no se hace: params crece con la resolución (insostenible); sin invarianza traslacional (un gato arriba-izq y abajo-der son inputs distintos); sin pesos compartidos (un detector de bordes se aprende de nuevo en cada posición). La convolución resuelve los tres: `nn.Conv2d(3,32,kernel_size=3)` = 896 params contra 3M, y funciona mejor. Dónde sí se usa FC: después de un extractor — `imagen → CNN → vector de 512 features → fully connected → salida`. Ese vector es funcionalmente un embedding de la imagen; el patrón general: una arquitectura especializada convierte el dato estructurado en un vector de tamaño fijo, y a partir de ahí todo vuelve al caso simple.

### 8. La capa de salida

La activación de salida es la misma clase de objeto que ReLU pero se elige con criterio distinto: ocultas (aportar no linealidad, ReLU por defecto, casi no importa); salida (poner el número en el rango y la interpretación correctos, lo determina la tarea). Activación / salida cae en / por qué: Lineal ninguna/ℝ (un precio puede ser cualquier número); Sigmoide (0,1) (una probabilidad); Softmax (0,1 suman 1) (clases excluyentes); Softplus/exp (0,∞) (conteo o desvío no negativo); Tanh (−1,1) (target acotado y centrado). "Activación lineal" = ninguna, la única capa donde no poner activación es correcto.

Catálogo completo de outputs (qué predice / neuronas / activación / loss): real (precio) 1/lineal/MSE-MAE-Huber; varios reales (bbox) k/lineal/MSE; sí-no (churn) 1/sigmoide/BCE; una de N clases N/softmax/cross-entropy; varias de N (tags) N/sigmoide×N/BCE; distribución μ,σ 2/(μ lineal,σ softplus)/NLL gaussiana; cuantiles P10,P50,P90 k/lineal/pinball; distribución discretizada k bins/softmax/CE; conteo (demanda) 1/softplus-exp/Poisson NLL; ranking 1 por ítem/lineal/pairwise-listwise; tiempo hasta evento 1–2/positiva/survival; secuencia (traducción) vocab×pasos/softmax por paso/CE; imagen (segmentación) H×W×C/depende/por píxel; vector denso (embedding) d/lineal/contrastive-triplet; serie temporal futura h pasos/lineal/MSE por paso.

Predecir una distribución, no un punto: (a) μ y σ 2 neuronas ("USD 180.000 ± 25.000", si aprox normal); (b) cuantiles P10/P50/P90 3 neuronas ("entre 150k y 220k, mediana 180k", la más usada, no asume forma); (c) bins+softmax k (histograma, distribuciones bimodales/asimétricas). Los cuantiles son los más rentables: no asumen normalidad, dan el intervalo que el negocio quiere, pocas líneas con pinball loss; hay que forzar que no se crucen.

Casos que sorprenden: conteos (MSE+lineal permite negativos y asume varianza constante; en conteos a mayor media mayor varianza → Poisson/Negative Binomial con salida positiva); tiempo hasta evento ("¿se va a ir?" es clasificación, "¿cuándo?" es supervivencia con datos censurados); ranking (output es un orden, score por ítem, loss sobre pares/listas); embeddings como salida (vector entrenado para que similares queden cerca; base de similitud, reconocimiento facial, recomendación). Los pares que no se rompen: activación de salida y loss se eligen juntas siempre (softmax con MSE, o sigmoide con CE categórica, entrenan igual pero convergen mal).

Detalle de implementación:
```python
nn.Linear(32, 1)                # sin sigmoide
loss = nn.BCEWithLogitsLoss()   # ← la sigmoide está acá adentro
```
`BCEWithLogitsLoss` y `CrossEntropyLoss` incluyen la sigmoide/softmax por estabilidad numérica; si la ponés también en la capa se aplica dos veces. En inferencia la aplicás vos: `prob = torch.sigmoid(model(x))`. Error frecuente: interpretar un logit de 2.3 como si fuera una probabilidad. Dos errores más comunes: softmax cuando debería ser sigmoide (un ticket puede ser "urgente" Y "de facturación"; softmax fuerza que las clases compitan; si las etiquetas no son excluyentes la salida está mal modelada de raíz); predecir un punto cuando el negocio necesita un rango (si la decisión depende del peor escenario — stock, riesgo, capacidad — un valor puntual no alcanza; la media es la respuesta correcta a una pregunta que nadie hizo).

### 9. Diseño de la red: qué se decide y qué no

Decisión / cómo se define / cuánto importa: neuronas de entrada (sale de la codificación / crítico); normalización del input (siempre / crítico); neuronas de salida (la tarea / no es decisión); activación de salida (la tarea / no es decisión); loss (acompaña la activación de salida / no es decisión); cantidad de capas ocultas (1–3 para tabular / medio); neuronas por capa (potencias de 2, decreciente / bajo); activación oculta (ReLU salvo motivo / bajo). La mitad de la arquitectura no se elige — sale sola del problema.

Ancho de las capas ocultas (criterios en orden de peso): más ancho que la entrada (no crear cuello de botella); potencia de 2 (alineación de memoria); decreciente hacia la salida. Datos / punto de partida: cientos de filas (1 capa de 8–16); miles (1–2 de 32–64); decenas de miles (2–3 de 64–128). La relación que importa es parámetros vs cantidad de datos, no vs features. Procedimiento: empezar chico y mirar el error de train; alto→falta capacidad (agrandar); train bien y validación mal→sobra capacidad (achicar o dropout/weight decay).

`nn.Linear(3, 16)`: in_features=3 (tamaño del vector que entra), out_features=16 (cantidad de neuronas). Crea `weight (16,3)` y `bias (16,)` → 64 params. El out_features de una capa tiene que ser el in_features de la siguiente. No incluye activación: sin ReLU en el medio, tres Linear seguidos colapsan a una sola transformación lineal. Defaults para tabular: normalizar siempre (sin esto nada más importa); empezar chico (32–64 en una capa oculta es baseline decente); ReLU por defecto; Adam con lr 1e-3; dropout o weight decay si se abre el gap train/validation. Advertencia honesta: para datos tabulares una red frecuentemente pierde contra gradient boosting (XGBoost, LightGBM) — resultado sostenido en la literatura; las redes brillan cuando hay estructura que explotar (imágenes, texto, señales), no con 20 columnas de un CSV.

### 10. Regularización

Qué problema resuelve: el overfitting es la brecha entre el error de entrenamiento y el de validación. Síntoma / diagnóstico / qué hacer: train alto+val alto (underfitting / más capacidad); train bajo+val alto (overfitting / regularizar); train bajo+val bajo (bien / nada). La regularización no mejora el ajuste — lo empeora a propósito en train, a cambio de que generalice mejor; es un intercambio explícito de sesgo por varianza.

L2 (weight decay): agrega un término al objetivo que penaliza pesos grandes: `J = cost + λ · Σ w²`. El gradiente resultante empuja cada peso hacia cero en cada paso (de ahí el nombre *decay*). Por qué funciona: un peso grande hace que la salida sea muy sensible a esa entrada; con pesos chicos la función aprendida es más suave, y una función suave es menos capaz de pasar exactamente por cada punto de entrenamiento — que es justamente lo que hace el overfitting. Aspecto / detalle: hiperparámetro λ (típico 1e-5 a 1e-2); en PyTorch `Adam(params, weight_decay=1e-4)`; al bias no se aplica (el bias no controla sensibilidad); en inferencia no hace nada (ya está incorporado en los pesos).

L1: misma idea con valor absoluto en vez de cuadrado: `J = cost + λ · Σ |w|`. L1/L2: penaliza |w| / w²; efecto en pesos chicos: los lleva exactamente a 0 / los reduce sin anularlos; resultado: solución rala, selecciona features / pesos parejos y chicos; uso en redes: poco común / el estándar. L1 se usa más en modelos lineales (Lasso). Elastic net combina ambos.

Dropout: durante el entrenamiento apaga aleatoriamente una fracción de las neuronas en cada forward pass. p típico 0.2–0.5 en capas ocultas; en entrenamiento cada neurona se apaga con probabilidad p; en inferencia se desactiva (todas activas); en PyTorch `nn.Dropout(0.2)`. Por qué funciona: la red no puede depender de ninguna neurona en particular porque en cualquier paso puede desaparecer, lo que la obliga a distribuir la representación en vez de crear detectores frágiles y coadaptados (lectura alternativa: ensemble implícito de muchas subredes que comparten pesos). El detalle que muerde: `model.train()` y `model.eval()` cambian su comportamiento; olvidarse de `model.eval()` en inferencia hace que el modelo apague neuronas al azar y devuelva predicciones distintas en cada llamada — de los bugs más frecuentes en PyTorch, afecta también a BatchNorm.

El resto del arsenal (técnica / cómo actúa / costo): early stopping (corta cuando validación deja de mejorar / gratis, casi siempre conviene); data augmentation (variantes del dato: crops, flips, ruido / muy efectivo en visión); más datos (ataca la causa / caro pero el mejor); reducir capacidad (menos capas o neuronas / simple); batch norm (efecto regularizador secundario / ya suele estar); label smoothing (targets 0.9/0.1 / clasificación); ensembling (promediar varios / caro en inferencia). Early stopping es el que menos se menciona y el que más rinde: no tiene hiperparámetro que calibrar y funciona con cualquier arquitectura.

Cuál usar: tabular red chica (L2 + early stopping); red profunda (dropout + L2); visión (data augmentation primero, después dropout); transformers (dropout bajo 0.1 + weight decay); pocos datos por categoría/embeddings (weight decay, agrupar categorías raras). Tres matices: regularizar sin overfitting es contraproducente (si el error de train ya es alto, agregar dropout empeora las dos métricas; primero se diagnostica, después se trata); dropout y batch norm se llevan mal (dropout cambia la varianza de las activaciones que batch norm acaba de normalizar; en visión moderna se usa batch norm y poco o nada de dropout); weight decay sobre embeddings tiene efecto raro (empuja a cero también las filas de categorías que no aparecieron en el batch, penalizando a las que ya estaban poco entrenadas; hay optimizadores con variantes sparse).

### 11. Los errores que más cuestan
Código como número (barrio 7 vs 14 → la red asume que 14 es "el doble"); ID único como feature (DNI, póliza → overfitting, train perfecto test malo); ordinal como one-hot sin necesidad (satisfacción 1–5 en 5 neuronas → pierde el orden); no normalizar (m² y booleanos crudos → converge lentísimo o no); μ,σ del dataset completo (`fit_transform(X_test)` → métricas infladas, degradación silenciosa); fuga temporal ("reclamos del cliente" para predecir churn → excelente pero inservible en prod); rellenar faltantes con 0 (cuando 0 es válido → confunde ausencia con valor); softmax donde va sigmoide (tags no excluyentes → fuerza competencia); doble sigmoide (activación en capa + en loss → entrena mal); olvidar `model.eval()` (dropout/BN activos en inferencia → predicciones distintas cada llamada); regularizar sin overfitting (dropout con train error alto → empeora ambas); predecir un punto (cuando el negocio necesita un rango).

### 12. Checklist operativo
Para cada variable: 1) ¿es número, categoría, ciclo, fecha o texto? 2) ¿qué significa la resta entre dos valores? 3) si es categoría: ¿tiene orden real? ¿cuántos valores distintos? 4) ¿puede faltar? ¿faltar significa algo? 5) ¿la voy a tener disponible al momento de predecir? Con eso resuelto, la cantidad de neuronas sale sola. Para la salida: 1) ¿qué pregunta responde el modelo? 2) ¿el negocio necesita un valor o un rango? 3) ¿las clases son excluyentes? 4) ¿el valor tiene que ser positivo?

### 13. Las ideas de fondo
El input es una traducción, y como toda traducción puede perder cosas: la red no ve un cliente, una máquina ni un contrato — ve un tensor; si la información que importa no está codificada ahí, o está codificada de una forma que borra su estructura, ninguna arquitectura la va a recuperar. El trabajo de diseño está casi entero en el input: la arquitectura de las capas ocultas importa bastante menos que decidir qué variables incluir y cómo codificarlas. La red no sabe qué tipo de dato tenía cada posición — solo ve floats; toda la semántica del tipo de variable se perdió en la codificación, por eso codificar mal es fatal. El aprendizaje funciona por comparación relativa, y comparar solo tiene sentido entre cosas medidas en la misma escala: si una variable grita y otra susurra, el modelo escucha la que grita (no porque importe más, sino porque es más ruidosa). La mayoría de los errores de producción en ML no están en el modelo, están en la frontera entre el dato crudo y el modelo: que la normalización o el diccionario de categorías queden fuera del artefacto es la causa individual más común.
