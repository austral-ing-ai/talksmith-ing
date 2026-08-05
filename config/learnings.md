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
