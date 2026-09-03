# Análisis del Talk — Trabajar con LLMs: prompts, costos y producción

Estado al 2026-09-02. Cubre la estructura del deck, lo que cambió en la última ronda de
edición, qué está verificado contra fuente y qué queda abierto.

---

## 1. Estado

| | |
|---|---|
| Láminas | 71 |
| Secciones | 8 de contenido, más la portada |
| Duración objetivo | 150 min (clase de 2:30 h) |
| Diagramas renderizados | 15 SVG derivados de arte ASCII |
| Láminas con panel de código | 15 |
| Capturas web en el corpus | 32 |
| Notas del orador | ~60.700 caracteres |
| Preguntas abiertas | 15 |

Las cinco auditorías del renderizador pasan. El modelo del deck está sincronizado con
`final.md`. El árbol de trabajo está limpio: todo lo de esta ronda quedó commiteado.

La única marca que devuelve `text_coverage` es un falso positivo conocido, sobre la URL
larga de CanLII en la lámina de casos de alucinación. La auditoría parte el texto por
espacios y no reconoce el enlace como una unidad; el enlace es idéntico byte a byte en la
fuente y en el modelo.

---

## 2. Estructura

| # | Sección | Láminas |
|---|---|---|
| 0 | Portada | 1 |
| 1 | Fundamentos | 18 |
| 2 | Modelos y costos | 5 |
| 3 | Prompts estructurados | 4 |
| 4 | In-context learning | 3 |
| 5 | Prompting avanzado | 12 |
| 6 | Effort y thinking | 11 |
| 7 | LLMs en ingeniería | 8 |
| 8 | Resumen y práctica | 2 |

**Fundamentos concentra el 25% del deck.** Es la sección más larga por bastante y es la
que un recorte de tiempo debería mirar primero. Contiene tres bloques que podrían vivir
separados: qué entra en el prompt (láminas 1 a 5), el costo de los tokens (6 a 12) y las
alucinaciones (13 a 18).

**Prompting avanzado y Effort y thinking suman 23 láminas**, casi un tercio del deck. Es
donde vive la tesis de la clase, y las dos secciones cuentan la misma idea desde dos
lados: primero el usuario le pide al modelo que escriba pasos intermedios, después el
modelo lo hace solo porque se lo enseñaron.

---

## 3. Qué cambió en esta ronda

### La sección de effort y thinking se rehizo casi entera

Quedó en once láminas y cambió de eje. Antes explicaba parámetros; ahora explica un
mecanismo y después cómo se configura.

Se agregaron cuatro láminas: cómo queda el razonamiento en código, la traza de tokens con
y sin bloque separado, la tabla de qué cambia el bloque, y la mecánica interna del
parámetro de esfuerzo.

Se borraron seis: la desambiguación de las cuatro acepciones de *thinking*, el presupuesto
fijo, el prompting con un modelo que razona, el costo del razonamiento, qué se factura, y
las perillas de sampling. Dos más se fusionaron en una sola sobre el origen del
comportamiento.

**Consecuencia que conviene tener presente:** con esas bajas, el deck ya no explica en
pantalla cómo se factura el razonamiento. La única mención que queda es una línea en
*¿CoT todavía sirve?* diciendo que los tokens de pensamiento se cobran como salida. El
detalle completo vive en las notas del orador.

### Los diagramas se rehicieron con criterio

Seis de los quince se volvieron a dibujar. El del ciclo de vida pasó a mostrar la tarea
concreta del modelo en cada uno de los seis estadios, que era lo que la lámina afirmaba y
la imagen no mostraba. El de los regímenes de aprendizaje dejó de fingir un gráfico
cuantitativo y pasó a filas de progresión discreta. El de self-consistency invirtió el
color, que antes destacaba el voto perdedor. El de cascading corrigió la asimetría de las
ramas. El del mecanismo de razonamiento equilibró las dos ramas. El de cadena de
pensamiento pasó de horizontal a vertical.

Se estableció una regla de color que ahora se cumple en los quince: **el acento marca lo
que hay que mirar, nunca el caso perdido.**

### Los ejemplos pasaron a código real

Zero-shot contra few-shot dejó de ser una tabla con saltos de línea forzados y pasó a dos
paneles de código Python independientes, uno por régimen. Many-shot pasó de un transcript
a código que arma el prompt en un bucle. Se agregaron dos láminas de código nuevas: el
gate de confianza del cascading y la configuración del razonamiento.

**Límite del renderizador que conviene conocer:** admite un panel de código propio de la
plantilla más otro en el lado de medios. Dos paneles reales son posibles; tres no. Y el
tamaño de la tipografía está topeado por la hoja de estilos, sin forma soportada de
subirlo. Está registrado como BUG-20260902-01.

---

## 4. Verificación

Todo lo que el deck afirma sobre la interfaz de programación se verificó contra
documentación, no contra memoria. Lo confirmado en esta ronda:

- Las salidas estructuradas son de disponibilidad general en toda la generación actual,
  hasta el modelo más chico. Por eso se retiró la pregunta del formato del árbol de
  elección de modelo: ya no descarta a nadie.
- La descripción de un campo viaja en el esquema y el modelo la lee. Las restricciones
  numéricas no son soportadas, pero el kit de desarrollo las traslada al texto de la
  descripción y valida la respuesta contra el esquema original.
- El razonamiento tiene tres valores de tipo y dos de visualización. El nivel de esfuerzo
  vive fuera de ese objeto.
- En los modelos más nuevos el razonamiento ya viene activo y oculto por defecto.
- El valor resuelto del esfuerzo se renderiza dentro del prompt, y el modelo fue entrenado
  en el post-entrenamiento para comportarse distinto en cada nivel. Ese comportamiento está
  grabado en los pesos congelados, no implementado en el servidor.

**Dos afirmaciones se dejaron deliberadamente fuera** por falta de fuente:

1. Que el entrenamiento por refuerzo use ejemplos etiquetados con niveles de esfuerzo
   objetivo. Es coherente con todo lo demás, pero no aparece en ninguna documentación
   pública. Está en las notas como hipótesis, no en pantalla como dato.
2. La cantidad de tokens del system prompt que la plataforma inyecta cuando el
   razonamiento está activo. La documentación confirma que ese prompt existe; no da cifra.

---

## 5. Inconsistencias encontradas y resueltas

La revisión completa encontró nueve, todas corregidas.

- **Dos referencias a láminas borradas seguían visibles.** El resumen de cierre listaba
  cinco técnicas incluyendo ReAct, cuya lámina ya no existía, y las notas de encadenamiento
  remitían a ella con un "que acaban de ver".
- **Dos objetivos de sección prometían lo que la sección ya no hacía.** El de apertura
  contaba siete secciones y hay ocho. El de effort y thinking prometía separar cuatro
  acepciones y cerrar con el costo en latencia; las dos cosas se habían eliminado.
- **Ocho preguntas abiertas apuntaban a cosas inexistentes**: la lámina de ReAct, un bloque
  duplicado, una cifra retirada, el vocabulario de las aplicaciones de chat, una tabla de
  precios de otros proveedores y dos pares de gráficos que no se usan en ninguna lámina.
- **Cinco entradas citaban láminas por un número que ya apuntaba a otra cosa.** Se
  reescribieron por nombre, que no se rompe cuando algo se mueve.
- **Una nota del orador seguía recomendando bajar la temperatura**, después de que se
  eliminaran las láminas que explican que esas perillas ya no existen.

**Causa raíz de la mitad de estos casos:** borrar una lámina no borra lo que otras láminas
dicen sobre ella. Conviene, después de cada baja, buscar el título eliminado en los dos
archivos fuente y en el modelo.

**Un error de método que apareció y se corrigió:** los scripts de renumeración leían los
comentarios dentro de los bloques de código como encabezados de sección, porque empiezan
con almohadilla. Eso cortaba el recorrido antes de tiempo y dejó dos láminas mal numeradas.
Toda la lógica de recorrido ahora ignora lo que está dentro de bloques cercados.

---

## 6. Riesgos y decisiones pendientes

### Para decidir antes de dar la clase

**El tiempo.** No hay medición. Setenta y una láminas en 150 minutos son poco más de dos
minutos por lámina, sin contar preguntas ni la práctica. Fundamentos, con dieciocho, es la
candidata natural a recorte.

**Dos afirmaciones sin fuente propia** que están en pantalla y conviene confirmar antes de
decirlas desde el escenario: las ventanas de contexto de proveedores que no son Anthropic,
heredadas del deck original, y que *Thinking* y *Deep Thinking* sean exactamente los
rótulos de las aplicaciones de chat.

**El registro del corpus.** Cinco capturas sobre razonamiento y esfuerzo se citan desde las
láminas pero no tienen registro propio en la carpeta de corpus. Funcionan como fuente para
quien lea el repositorio, no para quien recorra el corpus curado.

### Deuda menor

**Monotonía visual.** Hay dos tramos de cuatro láminas seguidas con la misma plantilla, en
el bloque 15 a 18 y en el 66 a 71. No es un error, es repetición que el aula percibe.

**Registro de las notas.** La sección de effort y thinking quedó en tuteo neutro por pedido
explícito; las otras siete usan voseo. Falta decidir si se normaliza.

**Nombre de la sección 6.** Se sigue llamando *Effort y thinking*, que nombra dos
parámetros cuando la sección ahora explica un mecanismo.

**El backlog cruzado.** Sesenta y dos entradas cerradas de este Talk nunca se espejaron al
backlog compartido de la materia.

---

## 7. Lo que sostiene el deck

Tres cosas que conviene no perder en futuras ediciones.

**La tesis se dice tres veces y se demuestra una.** Que el modelo completa en vez de
razonar, y que los pasos escritos son el cómputo, aparece en Fundamentos como modelo
mental, en Prompting avanzado como mecanismo compartido de las cuatro técnicas, y en Effort
y thinking como resultado experimental de otra gente. La curva del entrenamiento por
refuerzo es la única evidencia externa de la clase y por eso vale su lámina.

**Cada cifra tiene derivación.** Los precios, el punto de equilibrio del cascading, el
ahorro del caché y los números del entrenamiento están calculados a la vista en las fuentes
de cada lámina, no citados de memoria.

**Los diagramas cargan argumento, no decoran.** Ninguno de los quince repite lo que dice el
texto al lado. Ese es el criterio que hizo falta aplicar cuando el del ciclo de vida
dibujaba un ciclo genérico mientras la lámina hablaba de otra cosa.
