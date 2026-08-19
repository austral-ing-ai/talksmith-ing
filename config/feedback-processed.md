# Feedback — processed

> Format spec and audit-trail invariant live in [`${CLAUDE_PLUGIN_ROOT}/schemas/feedback-processed.md`](${CLAUDE_PLUGIN_ROOT}/schemas/feedback-processed.md).

## Entries

<!-- Editor role appends entries below this line during the Step 8 Move pass. -->
- talk: modelado-redes-neuronales
  date: 2026-08-19
  location: Agenda
  feedback: "En casi todos los slides es confusdo que no se define y en algunos caso se empieza con ejemplos." / "Lo que quise decir es que en los cards veo que se empieza definiendo ejemplo y no se define. No veo consistencia."
  resolution: Se fijó una regla de card para todo el mazo y se barrieron las que no la cumplían. **La etiqueta en negrita nombra la cosa; la oración que sigue la define o la afirma; el ejemplo viene después de la definición, nunca antes.** Corregidas: 1.3 (la tercera card rompía el patrón término-definición de sus hermanas), 2.3 (la card de log abría con una lista de ejemplos), 2.5 (las cuatro abrían con el ejemplo y nunca definían el error), 4.3 (la de softmax abría con el ticket), 7.1 y 7.3 (etiquetas mezcladas entre pregunta, consecuencia y término; pasaron todas a sintagma nominal).
  tags: [definition-before-example, card-consistency]
  promoted_to: L8
  promoted_at: 2026-08-19
- talk: modelado-redes-neuronales
  date: 2026-08-19
  location: Slide "1. La red no ve el problema, ve un tensor"
  feedback: "Ojo que no se definir tensor en ningun lado."
  resolution: Se abrió la diapositiva con la definición de tensor (arreglo N-dimensional de floats, forma fija) y la escala escalar/vector/matriz/imagen, antes de los bullets.
  tags: [missing-definition]
  promoted_to: L8
  promoted_at: 2026-08-19
- talk: modelado-redes-neuronales
  date: 2026-08-19
  location: Slide "1. Todo termina en un vector de floats"
  feedback: "Secuencia no se si es la definicion correcta. Seria bueno que introducca de definicion del tipo y luego ejemplos. Los ejemplos son procos."
  resolution: La tabla pasó a cinco columnas con una de definición propia ("Qué es") antes de los ejemplos, y cada fila subió a tres ejemplos. Se corrigió Secuencia (elementos discretos de un vocabulario, orden, largo variable) y se agregó un párrafo que la separa de Señal. Las notas del orador recogen la distinción.
  tags: [missing-definition, definition-before-example]
  promoted_to: L8
  promoted_at: 2026-08-19
- talk: modelado-redes-neuronales
  date: 2026-08-19
  location: Slide "2. La pregunta que decide la codificación"
  feedback: "Seria bueno aca agregar una nota que los valores al sear reales hay cierta expectativa que las deferencias y magntides modelan algo. g: Barrio 14-7 no dice nada de ahi que hay que modelarlo distinto"
  resolution: Se agregó el párrafo "Poner un número real en el tensor es afirmar algo", con las dos promesas que hace un float (diferencias comparables y magnitud que escala el efecto vía W·x) y el contraste 85 m² contra barrio 14.
  tags: [missing-definition]
  promoted_to: L8
  promoted_at: 2026-08-19
- talk: modelado-redes-neuronales
  date: 2026-08-19
  location: Slide "3. Numéricas: normalizar no es opcional"
  feedback: "En casi todos los slides es confusdo que no se define y en algunos caso se empieza con ejemplos. En este caso, fata la defincion, luego se peude mencionar datos tipo y el effecto de."
  resolution: La diapositiva pasa a orden definición → a qué datos aplica → efecto → recetas. Se abre definiendo qué es normalizar y sobre qué variables aplica; el argumento del gradiente quedó después, bajo "Por qué no es opcional". La parte general del comentario (que casi todas las diapositivas arrancan por el ejemplo) queda pendiente de decisión del presentador como barrido definición-primero de todo el mazo.
  tags: [definition-before-example]
  promoted_to: L8
  promoted_at: 2026-08-19
- talk: modelado-redes-neuronales
  date: 2026-08-19
  location: Slide "3. Precision, recall y F1"
  feedback: "No se definio 'F1, media armónica'"
  resolution: La card ahora abre con la fórmula `2 · (P · R) / (P + R)` y define la media armónica por contraste con el promedio común, con dos números concretos (0.9 y 0.5 dan 0.70 de promedio y 0.64 de F1). Las notas del orador suman el porqué de la armónica y el caso del clasificador que marca todo.
  tags: [missing-definition, missing-formula]
  promoted_to: L8
  promoted_at: 2026-08-19
