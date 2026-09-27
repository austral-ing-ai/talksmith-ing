---
source_type: presenter-notes
author: presentador (Paulo Veiga)
date: 2026-09-26
topic: Entrenamiento del reward model en un batch de pares de preferencias
note: texto pegado verbatim por el presentador en la sesión de Talksmith del 2026-09-26, pedido "Agregar en RL un slide que explique la matemática de RL. Este es un poco el code a capturar".
---

Casi: es una pregunta con dos respuestas. Lo que va en el batch son dos secuencias, cada una con la pregunta repetida:

Fila 1: [Pregunta + A]
Fila 2: [Pregunta + B]

Y el batch no tiene un solo par, sino muchos. Por ejemplo, con 64 pares:

Fila	Contenido
0	P₁ + A₁ (preferida)
1	P₁ + B₁
2	P₂ + A₂ (preferida)
3	P₂ + B₂
…	…
126	P₆₄ + A₆₄ (preferida)
127	P₆₄ + B₆₄

Son 128 secuencias en un solo forward. Después:

Se obtienen los 128 scores.
Se reagrupan por par (fila 0 con 1, 2 con 3, etc.). El orden importa: el código tiene que saber qué score va con cuál.
Loss de cada par: −log σ(r(Aᵢ) − r(Bᵢ)).
Promedio de las 64 loss → un solo backward.

Un detalle: A y B casi nunca tienen el mismo largo, así que se rellenan con padding hasta el largo máximo del batch. Por eso el score se toma del último token real de cada secuencia, no de la última posición de la fila, que podría ser padding.
