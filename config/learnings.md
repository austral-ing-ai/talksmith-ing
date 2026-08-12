# Learnings

Reglas editoriales promovidas desde el feedback recurrente. Se cargan al inicio de cada Talk de
este repositorio y aplican sin volver a pedirlas.

---

## L1 — Cada familia de problemas se presenta en dos diapositivas: definición con diagrama, después ejemplos

- **Regla:** cuando una sección introduce un tipo de problema que la IA resuelve, la familia se
  presenta primero en una diapositiva propia que la **define en una línea** y lleva un **diagrama
  ASCII** del concepto, y recién después viene la diapositiva de **ejemplos, herramientas e hito**.
  Nunca una sola diapositiva que mezcle definición y ejemplos, y nunca una definición sin diagrama
  mientras sus hermanas lo tengan.
- **Por qué:** el par separa dos trabajos distintos. La primera responde "qué es y qué forma tiene";
  la segunda, "dónde aparece y con qué se hace". Mezclarlas produce diapositivas densas que no
  terminan de explicar ninguna de las dos cosas. El diagrama en la de definición es lo que hace que
  la forma del problema se entienda antes de ver los casos.
- **Dónde aplica:** cualquier sección taxonómica. En `talks/introduccion` son las siete familias de
  `# 5. Taxinomia de Problemas` y la apertura de `# 6. Modelos Fundacionales`.
- **Consistencia visual del conjunto:** los diagramas de una misma sección comparten lienzo,
  márgenes, tipografía, tratamiento de cajas y un solo elemento con el acento rojo. **La forma sí
  puede cambiar** cuando el concepto lo pide: una tubería de tres columnas para lo que transforma
  una entrada en una salida, un lazo cerrado para lo que interactúa con un entorno, un árbol para lo
  que explora estados, una cadena para lo que encadena reglas, cajas anidadas para lo que contiene.
  Dibujar un lazo como tubería enseñaría algo falso.
- **Evidencia:** propuesto por el presentador el 2026-08-05 después de ver el par
  definición + diagrama en Percepción y Representación. La sección venía de una reconstrucción donde
  seis de siete familias estaban comprimidas en una sola diapositiva; la inconsistencia de que solo
  Predicción tuviera separadora fue el primer síntoma que él marcó.
- **Fecha:** 2026-08-05

---

## L2 — El diagrama va en la diapositiva que introduce el tema, no en una nueva

- **Regla:** cuando un tema ya tiene una diapositiva que lo introduce, el diagrama se agrega **ahí**.
  Solo se crea una diapositiva nueva cuando la sección no tiene apertura, y en ese caso la nueva es
  la de definición del par de L1.
- **Por qué:** una diapositiva de diagrama suelta rompe el ritmo y obliga a repetir el encuadre.
  Puesto en la que ya define el tema, el diagrama es la explicación de la definición que está
  justo arriba.
- **Dónde aplica:** todo el repositorio.
- **Evidencia:** indicación explícita del presentador el 2026-08-05, sobre la diapositiva 30
  (Predicción).
- **Fecha:** 2026-08-05

---

## L3 — Listas con ordinales usan la plantilla de lista numerada

- **Regla:** cuando una lista lleva el número dentro del texto, o son tarjetas con un ordinal en la
  etiqueta (el caso señalado: cards que arrancan con "46."), la diapositiva usa la plantilla de
  **lista / secuencia numerada**: el ordinal lo dibuja el estilo, nunca el contenido. Al convertir,
  se retiran los ordinales de las etiquetas y las tarjetas se abren en líneas planas sin perder
  ninguna.
- **Por qué:** un número escrito dentro de la tarjeta compite con el que dibuja el estilo y se lee
  como dato, no como orden. La plantilla numerada da el conteo que vuelve una lista en un conjunto
  que el presentador puede señalar, y deja el texto limpio.
- **Dónde aplica:** todo el repositorio, cualquier lista de pasos, entregables, conclusiones o
  contenidos.
- **Evidencia:** recurrió ~10 veces en `talks/introduccion` (diapositivas 1, 13, 14, 15, 16,
  Conclusiones) entre el 2026-08-04 y el 2026-08-05; el presentador lo pidió repetidamente como
  "el estilo que numera".
- **Fecha:** 2026-08-12

---

## L4 — Fidelidad a la fuente al adaptar desde un PPTX de referencia

- **Regla:** al adaptar contenido desde un PPTX de referencia, se preservan **cifras, datos, fechas
  y enlaces verbatim**. Antes de reescribir una diapositiva se verifica contra el original; los
  hipervínculos perdidos en la adaptación se reponen desde los del PPTX. Los ejemplos se pueden
  trasladar de dominio; los hechos históricos y las fuentes quedan intactos.
- **Por qué:** la adaptación cambia el mundo del ejemplo, no la verdad de los datos. Una cifra
  cambiada o un link perdido rompe la credibilidad de la clase y es difícil de detectar después.
- **Dónde aplica:** toda Talk que se arme adaptando material de origen.
- **Evidencia:** recurrió ~5 veces en `talks/introduccion` (cuello blanco 70→75%, Deep Blue,
  taxonomía de problemas, links de McKinsey y Citrini repuestos, AlexNet) el 2026-08-05.
- **Fecha:** 2026-08-12

---

## L5 — Sin subtítulo que duplique el título

- **Regla:** una diapositiva no lleva un subtítulo que repita lo que ya dice el título. Cuando el
  feedback renombra la diapositiva, se retira el subtítulo que quedó redundante.
- **Por qué:** el subtítulo repetido gasta la línea más visible de la diapositiva sin agregar
  información; el espacio es para lo que el título no dice.
- **Dónde aplica:** todo el repositorio.
- **Evidencia:** recurrió ~5 veces en `talks/introduccion` (LLMs/Foundation Models, IA Tradicional
  vs. Foundation Models, Limitaciones, Modelos de propósito general, ¿Por qué relevantes?) entre el
  2026-08-04 y el 2026-08-05.
- **Fecha:** 2026-08-12

---

## L6 — No repetir líneas entre diapositivas

- **Regla:** una línea que ya cubre otra diapositiva no se duplica: se retira de la diapositiva
  secundaria y se archiva en `Cut material`, nunca se borra en silencio.
- **Por qué:** el contenido repetido diluye ambas diapositivas y deja al presentador diciendo dos
  veces lo mismo; el desglose vive en un solo lugar (ej. la ponderación de la nota vive en
  Evaluación, no en Cómo vamos a trabajar).
- **Dónde aplica:** todo el repositorio.
- **Evidencia:** recurrió 4 veces en `talks/introduccion` (diapositivas 13 y 15) el 2026-08-05.
- **Fecha:** 2026-08-12

---

## L7 — Referencias editoriales fuera del contenido visible

- **Regla:** las menciones al material de origen o a decisiones de adaptación ("el PPTX original
  presenta…", "esta versión traslada…") no van en el contenido visible de la diapositiva. Se
  eliminan, o si aportan contexto para presentar, pasan a las notas del orador.
- **Por qué:** la audiencia no ve el material de origen; una referencia editorial en la diapositiva
  expone el andamiaje de producción en lugar del contenido.
- **Dónde aplica:** todo el repositorio.
- **Evidencia:** recurrió 3 veces en `talks/introduccion` (diapositivas 8, 9, 10) entre el
  2026-08-03 y el 2026-08-04.
- **Fecha:** 2026-08-12
