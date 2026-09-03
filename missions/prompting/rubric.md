# Rúbrica — Misión: el prompt mínimo

Instrumento de corrección derivado de `mission.md`. Cada criterio se evalúa contra
**evidencia observable en el repositorio entregado**, no contra la descripción que el grupo
hace de su trabajo.

Total: 100 puntos.

---

## Regla de admisibilidad

La misión lo dice literalmente: *"una corrida sin log no se puede auditar y no cuenta"*.

**Sin los logs `.md` con su usage, el ejercicio 2 y el ejercicio 3 valen cero**, aunque el
script funcione y el informe esté escrito. No es una penalización de estilo: sin log no hay
forma de verificar cuántos prompts hubo, y ese es el objeto de la misión.

---

## Ejercicio 1 — Interfaz de chat, cuatro modelos (30 pts)

| # | Criterio | Pts | Evidencia que lo confirma |
|---|---|---|---|
| 1.1 | Sirve los cuatro modelos, uno por proveedor | 6 | Los cuatro ids en el código; un log por modelo |
| 1.2 | Muestra el usage después de cada respuesta | 6 | Entrada, salida, razonamiento, cacheados y costo, los cinco |
| 1.3 | Permite cambiar de modelo, y el cambio inicia conversación nueva | 4 | Código del selector; el log no mezcla modelos |
| 1.4 | Guarda un log `.md` por conversación con rol, mensaje y usage | 6 | Archivos en el repo, no capturas de pantalla |
| 1.5 | Slot 1: se ve el efecto de cambiar el nivel de esfuerzo | 4 | Dos corridas del mismo prompt con niveles distintos y sus tokens de razonamiento |
| 1.6 | Slot 2: se ve un cache hit | 4 | `cached_tokens` mayor que cero en la segunda pasada del mismo contexto |

**Descuentos.** Si sustituyeron algún modelo del catálogo sin anotarlo en el informe,
menos 2. Si el usage se muestra parcial (faltan tokens de razonamiento o cacheados),
1.2 va a la mitad.

**No se puntúa.** Que la interfaz sea linda. La misión lo dice explícitamente.

---

## Ejercicio 2 — El target en 1 prompt (40 pts)

| # | Criterio | Pts | Evidencia que lo confirma |
|---|---|---|---|
| 2.1 | Los 9 tests pasan con el script tal cual salió del chat | 12 | Correr `test_vida.py` contra el `vida.py` entregado |
| 2.2 | La conversación ganadora tiene 1 o 2 prompts en total | 12 | Contar turnos de usuario en el log ganador |
| 2.3 | Los intentos quemados están entregados, no escondidos | 6 | Un log por intento; el informe los cuenta todos |
| 2.4 | Caching en el diseño del prompt: `cached_tokens` > 0 del segundo intento en adelante | 6 | Usage de cada intento en su log |
| 2.5 | El prompt es una especificación, no un pedido | 4 | Rol, contexto, instrucciones, restricciones, ejemplos e input identificables |

**La regla dura.** Si el `vida.py` entregado **no coincide** con el que aparece en el log
ganador, 2.1 y 2.2 valen cero. Parchear a mano está prohibido por la consigna y es
verificable comparando los dos textos.

**Cómo se cuenta un prompt.** Turnos de rol `user` en la conversación ganadora. Un
mensaje que solo dice "corré los tests" cuenta igual que cualquier otro.

**Gradiente en 2.2.** Un prompt: 12. Dos prompts: 9. Tres o más sin abrir conversación
nueva: 0, porque la corrida estaba quemada y siguieron igual.

**Escala en 2.1.** Los nueve tests: 12. Siete u ocho: 6. Menos: 0. No hay crédito parcial
por "casi anda": el criterio de la misión es binario por test.

---

## Ejercicio 3 — La cuenta final (20 pts)

| # | Criterio | Pts | Evidencia que lo confirma |
|---|---|---|---|
| 3.1 | Tokens de entrada y salida por intento, y totales | 4 | Tabla en el informe, reconciliable contra los logs |
| 3.2 | Tokens de pensamiento y qué se facturó por ellos | 4 | Si el modelo no los devuelve, documentado como hallazgo |
| 3.3 | Tokens cacheados y ahorro calculado | 4 | El ahorro derivado, no solo el conteo |
| 3.4 | Gasto total en USD contrastado contra el dashboard | 4 | La comparación explícita, y la diferencia explicada si la hay |
| 3.5 | Conclusión de tres líneas con una decisión concreta | 4 | Nombra modelo, parámetro o cambio de prompt. "Mejorar el prompt" no puntúa |

**Verificación cruzada.** Los números del informe tienen que cerrar contra los logs. Una
discrepancia sin explicar cuesta la mitad del criterio afectado. Si el informe reporta
menos intentos de los que hay en los logs, 2.3 también cae.

---

## Forma de trabajo del repositorio (10 pts)

| # | Criterio | Pts | Evidencia que lo confirma |
|---|---|---|---|
| 4.1 | `CLAUDE.md` con instrucciones reales del proyecto | 3 | Que dirija el trabajo, no un archivo de relleno |
| 4.2 | `SPEC.md` que describe lo que se construyó | 3 | Coherente con el código entregado |
| 4.3 | Historia de commits limpia | 4 | Mensajes que explican el cambio; no un único commit "todo" |

---

## Trabajo previo obligatorio

La misión pide, **antes de escribir código**, tres respuestas: qué hace un router de
modelos, el mapa de los siete proveedores con precio, ventana y posición en benchmarks, y
la comparación de parámetros soportados entre fichas.

**No suma puntos por separado.** Se evalúa como parte del informe: si está ausente, el
ejercicio 3 no puede superar los 15 puntos, porque las decisiones de modelo quedan sin
fundamento.

---

## Señales de alarma

Cosas que conviene mirar de cerca antes de poner la nota.

- **El log ganador no tiene marcas de tiempo o las tiene fuera de orden.** Sugiere edición
  posterior.
- **El primer intento ya muestra `cached_tokens` mayor que cero.** Imposible con prefijo
  nuevo; sugiere que hubo corridas previas no entregadas.
- **El costo del informe es más bajo que la suma de los logs.** Suelen faltar intentos.
- **El `vida.py` tiene un estilo distinto al del código del log**, o comentarios que el
  modelo no escribió.
- **Todos los grupos entregan el mismo prompt.** No está prohibido colaborar, pero cambia
  qué se está midiendo y conviene saberlo antes de comparar.

---

## Planilla de salida

Por grupo, una fila:

| Grupo | Repo | E1 /30 | E2 /40 | E3 /20 | Repo /10 | Total | Prompts del ganador | Tests en verde | Gasto USD |
|---|---|---|---|---|---|---|---|---|---|
