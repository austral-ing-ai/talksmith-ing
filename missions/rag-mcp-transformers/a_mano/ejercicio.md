# Parte 5: un bloque de transformer a mano

Las dos frases de este ejercicio tienen la misma palabra ambigua:

- **"El banco aguanta ___"**
- **"El banco presta ___"**

"banco" puede ser un asiento o una entidad financiera. En este ejercicio tienen que pasar las dos frases por un bloque de transformer completo, con papel, lápiz y calculadora. Con los resultados van a poder observar cómo la atención le da a "banco" un significado distinto según el contexto y qué palabra predice el modelo para completar cada frase.

Antes de hacer las cuentas, miren [Attention in transformers, step-by-step](https://www.youtube.com/watch?v=eMlx5fFNoYc) (3Blue1Brown, Deep Learning Chapter 6).

## Reglas

- **Tienen que resolver todo a mano**, en papel y con letra propia. Se permite calculadora para exponenciales y raíces. Tienen que entregar el escaneo o la foto legible de las hojas, en `a_mano/` del repo.
- **Cada operación tiene que llevar su justificación**, escrita al lado del resultado: qué hace esa operación y para qué sirve en el modelo. Una operación sin justificación cuenta como no hecha, aunque el número esté bien. Frases genéricas como "se calcula la atención" no justifican nada.
- Redondeen a tres decimales. Los resultados se pueden verificar con su `atencion.py` de la parte 4, pero la hoja tiene que mostrar las cuentas.

## Los datos

Los vectores tienen dimensión d = 4. Las dimensiones de los embeddings de este ejercicio tienen un significado inventado para poder leer los resultados: 1 = objeto físico o mueble, 2 = dinero o finanzas, 3 = acción, 4 = función gramatical. En un modelo real ninguna dimensión tiene un significado tan limpio.

**Vocabulario.** El modelo conoce seis palabras: V = {El, banco, aguanta, presta, peso, dinero}. Es el mismo vocabulario para la entrada y para la salida: cualquiera de las seis puede entrar en una frase, y el modelo predice la palabra siguiente eligiendo entre las seis.

**Embeddings de palabra (E)**, una fila por palabra del vocabulario:

| palabra | d1 | d2 | d3 | d4 |
|---|---|---|---|---|
| El | 0 | 0 | 0 | 1 |
| banco | 1 | 1 | 0 | 0 |
| aguanta | 1 | 0 | 1 | 0 |
| presta | 0 | 1 | 1 | 0 |
| peso | 1 | 0 | 0 | 0 |
| dinero | 0 | 1 | 0 | 0 |

**Embeddings de posición aprendidos (P)**

| posición | d1 | d2 | d3 | d4 |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 2 | 0 | 0 | 0 | 2 |

**Pesos del bloque** (una sola cabeza)

```
Wq = identidad (4 x 4)          Wv = identidad (4 x 4)          Wo = identidad (4 x 4)

Wk =  1  0  0  0                W1 =  1 -1  0  0               W2 = identidad (4 x 4)
      0  1  0  0                     -1  1  0  0
      1  1  0  0                      0  0  0  0
      0  0  0  0                      0  0  0  0

Wout (4 x 6), una columna por palabra del vocabulario:
         El  banco  aguanta  presta  peso  dinero
          0    0      0        0      2     0
          0    0      0        0      0     2
          0    0      1        1      0     0
          0    0      0        0      0     0
```

Varias matrices son la identidad para que las cuentas sean manejables. Igual hay que escribir la operación y justificarla: en un modelo real son densas y aprendidas.

## Parte A: el bloque completo como decoder (con máscara causal)

Para cada una de las dos frases:

1. **Entrada.** X = E + P, una fila por token.
2. **Proyecciones.** Q = X Wq, K = X Wk, V = X Wv.
3. **Afinidades.** S = Q Kᵀ.
4. **Escala.** S / √d, con d = 4.
5. **Máscara causal.** Poner −∞ donde un token mira a uno posterior.
6. **Matriz de atención.** A = softmax por fila.
7. **Mezcla.** A V, y después la proyección de salida (A V) Wo.
8. **Residual.** Z = X + (A V) Wo.
9. **Layer norm.** LN(Z), fila por fila (media y varianza de cada fila; ε despreciable).
10. **Feed-forward.** FFN = ReLU(LN(Z) W1) W2.
11. **Residual.** H = Z + FFN.
12. **Layer norm final.** LN(H).
13. **Predicción.** Con la última fila de LN(H), logits = fila · Wout (un valor por palabra del vocabulario) y softmax sobre esos seis valores. ¿Qué palabra completa la frase, y con qué probabilidad?

## Parte B: la misma atención sin máscara (encoder)

Para cada frase, repitan los pasos 5 a 9 sin la máscara causal y anoten la fila de "banco" en LN(Z).

## Preguntas

Contesten en la misma hoja, en dos o tres líneas cada una:

1. Comparen la fila de "banco" en LN(Z) entre las dos frases en la parte A y en la parte B. ¿En cuál de las dos partes el vector de "banco" cambia según la frase? ¿Por qué?
2. En la parte A, ¿cómo "sabe" el modelo si tiene que predecir "peso" o "dinero", si el vector de "banco" es el mismo en las dos frases?
3. La predicción de la parte A y la que resultaría de la parte B para la última posición, ¿son iguales o distintas? Expliquen por qué con lo que hace la máscara.
4. ¿Qué modelo de la clase se parece a la parte A y cuál a la parte B? ¿Para qué se usa cada uno?
5. Si P fuera todo ceros, ¿qué cambiaría en los resultados de este ejercicio? ¿Y en una frase donde el orden de las palabras cambie el sentido?
