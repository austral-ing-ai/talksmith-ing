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

---

## L8 — Definir antes de ejemplificar, en cada card

- **Regla:** la etiqueta en negrita de una card **nombra la cosa**; la oración que sigue **la define o
  la afirma**; el ejemplo viene **después** de la definición. Nunca una card que abra con el caso
  concreto y deje la definición implícita, y nunca un término técnico (tensor, media armónica,
  normalizar, F1) usado en una card sin haberlo definido antes en el mazo. Cuando una diapositiva
  introduce un concepto, el orden es definición, a qué se aplica, efecto, recetas.
- **Por qué:** el ejemplo solo enseña si el que escucha ya sabe de qué es ejemplo. Al revés obliga a
  inferir la categoría desde un caso, que es justo el trabajo que la diapositiva tendría que
  ahorrarle. El síntoma es una diapositiva que se lee bien y no explica nada: el presentador la da
  por entendida porque él sí sabe qué es lo que está ejemplificando.
- **Dónde aplica:** todo el repositorio, cualquier card, columna o fila de tabla con etiqueta.
  Vale también para las etiquetas: dentro de una diapositiva las cards comparten forma gramatical
  (todas sintagma nominal, o todas término más definición), nunca una mezcla de pregunta,
  consecuencia y término.
- **Cómo se revisa:** leer solo las etiquetas en negrita de una diapositiva, seguidas. Si se leen
  como una lista coherente, la diapositiva está bien; si saltan de pregunta a ejemplo a término,
  hay que emparejarlas.
- **Evidencia:** recurrió 7 veces en `talks/modelado-redes-neuronales` el 2026-08-19, con las
  etiquetas `missing-definition` (4) y `definition-before-example` (3). El presentador lo marcó
  primero como "en casi todos los slides es confuso que no se define" y después lo precisó: "en los
  cards veo que se empieza definiendo ejemplo y no se define. No veo consistencia". Casos: tensor
  sin definir (1.1), Secuencia sin definición y con un solo ejemplo (2.1), normalizar que abría por
  el gradiente (2.3), las cuatro cards de errores de codificación que abrían por el caso (2.5),
  softmax que abría por el ticket (4.3), accuracy usada sin fórmula (5.1), F1 nombrado como "media
  armónica" sin decir qué es (5.3).
- **Fecha:** 2026-08-19

---

## L9 — El porqué va al pie, no arriba

- **Regla:** cuando una diapositiva tiene una afirmación y su justificación técnica, la afirmación va
  arriba y la justificación baja a **nota al pie**. La apertura es para lo que hay que retener; el
  mecanismo es para quien pregunte. Vale también para el alcance: si un tema se declara fuera de la
  clase, se lo menciona en una nota final y no se lo desarrolla en el cuerpo.
- **Por qué:** el argumento de fondo compite con la idea cuando está arriba. El que escucha se mete
  en el mecanismo antes de saber para qué sirve, y llega a las recetas sin haber entendido qué
  problema resuelven. Puesto al pie, el porqué sigue disponible sin robarle la apertura a la idea.
- **Dónde aplica:** todo el repositorio. Cualquier diapositiva que combine una definición o una
  receta con su fundamento.
- **Cómo se revisa:** leer solo la primera línea del cuerpo de la diapositiva. Si es un mecanismo
  (una derivada, una fórmula, un argumento de por qué), y no la cosa que la diapositiva enseña,
  hay que bajarlo.
- **Evidencia:** recurrió 3 veces en `talks/modelado-redes-neuronales` el 2026-08-19, con la etiqueta
  `note-demotion`. Casos: el detalle numérico de capas y ancho en la diapositiva 1.2 ("agreguemos
  esto como un ítem pero podemos poner una nota"); el argumento del gradiente en la 2.3, que abría la
  diapositiva de normalización antes de la definición ("movelo como una nota abajo"); y el caso
  multiclase en la 5.7 ("poner solo una nota al final").
- **Fecha:** 2026-08-20

---

## L10 — Acortar la afirmación, no agregar la explicación

- **Regla:** cuando una afirmación de una diapositiva resulta imprecisa y sostenerla exige traer
  material que está fuera del alcance de la clase, **lo que se recorta es la afirmación**, no lo que
  se agrega es la explicación. Si la precisión necesaria pertenece a otra clase, la afirmación no
  pertenece a esta.
- **Por qué:** la respuesta refleja a "esto no es del todo cierto" es explicar más, y esa es la
  trampa: cada explicación agregada arrastra vocabulario de otra materia y la diapositiva termina
  enseñando algo que no era el tema. El alcance de la clase es un límite, no una sugerencia, y una
  afirmación que lo cruza es la que sobra.
- **Dónde aplica:** todo el repositorio, y sobre todo en las clases introductorias, donde la
  tentación de completar el cuadro es mayor.
- **Cómo se revisa:** ante una corrección de precisión, preguntarse qué haría falta para sostener la
  afirmación tal como está. Si la respuesta nombra un tema que la clase no cubre, se reescribe la
  afirmación más chica en vez de sumar el tema.
- **Evidencia:** recurrió 4 veces sobre la misma diapositiva de `talks/modelado-redes-neuronales` el
  2026-08-19, etiquetado entre `factual-correction` y `scope`. La card decía que el canal de una
  imagen RGB "se puede reordenar sin cambiar nada". El presentador marcó primero que eso no valía
  para un DNN; la respuesta fue agregar a las notas la explicación de Conv2D, kernels y conteos de
  parámetros. El presentador entonces marcó "acá no estamos explicando redes convolucionales, hablar
  de muchas capas produce ruido". La corrección correcta era retirar la afirmación de reordenar, que
  era la que obligaba a explicar Conv2D para tener sentido. En la misma ronda apareció "el apilada no
  está bien", que era el mismo problema en otra forma: describir la imagen RGB como tres matrices
  apiladas sugería un tercer eje espacial y contradecía lo que la card enseñaba.
- **Fecha:** 2026-08-20
