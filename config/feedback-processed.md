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
- talk: modelado-redes-neuronales
  date: 2026-08-19
  location: Slide "2. Lo que hay que diseñar"
  feedback: "Agreguemos esto como un item pero podemos poner una nota"
  resolution: El remate al pie pasó a ser el sexto ítem de la lista ("Las capas y las neuronas. No están en la lista. Eso sí se elige, y es lo que menos importa del diseño"), y el detalle numérico (1 a 3 capas, potencias de 2, ReLU) bajó a una nota al pie de la diapositiva.
  tags: [item-promotion, note-demotion]
  promoted_to: L9
  promoted_at: 2026-08-20
- talk: modelado-redes-neuronales
  date: 2026-08-19
  location: Slide "3. Numéricas: normalizar no es opcional"
  feedback: "Movelo como una nota abajo."
  resolution: Sobre el bloque "Por qué no es opcional". El argumento del gradiente bajó de párrafo destacado, arriba de las recetas, a nota al pie de la diapositiva. La apertura queda solo con la definición.
  tags: [note-demotion, content-position]
  promoted_to: L9
  promoted_at: 2026-08-20
- talk: modelado-redes-neuronales
  date: 2026-08-19
  location: Slide "7. El umbral, una perilla de negocio"
  feedback: "Ok, enfoquemosnos solo a 2 clases. Y poner solo una nota al final."
  resolution: La sección queda binaria de punta a punta. La diapositiva pasó a llamarse "El umbral, una perilla de negocio", sin la matriz en el título, y el bloque de multiclase se redujo a una nota de dos líneas al pie: la matriz crece a una fila por clase real y una columna por clase predicha, precisión y recall se calculan por clase, y la idea no cambia. El ejemplo del clasificador de dígitos quedó en las notas del orador por si alguien pregunta. El goal de la sección dice ahora explícitamente que trabaja sobre dos clases.
  tags: [scope, note-demotion]
  promoted_to: L9
  promoted_at: 2026-08-20
- talk: modelado-redes-neuronales
  date: 2026-08-19
  location: Slide "2. Cómo se ve un tensor"
  feedback: "'El canal no es espacial: son tres variables en el mismo punto, y se puede reordenar.' ¿No es verdad si es un DNN?"
  resolution: La afirmación es cierta sobre el dato (el canal no tiene vecindad, alto y ancho sí), pero la card decía "se puede reordenar sin cambiar nada" sin decir respecto de qué, y ahí el comentario tiene razón: el contraste solo tiene consecuencias contra una Conv2D, que es la que trata alto y ancho como espacio al deslizar el mismo kernel. En un Dense sobre la imagen aplanada no hay ningún eje espacial y todas las posiciones son reordenables, las espaciales incluidas. La card pasó a decir que el canal es el único de los tres que se puede reordenar, que es lo preciso, y las notas del orador suman el matiz completo con los números del corpus: kernel 3×3 sobre RGB son 27 pesos y no 9; RGB 224×224 aplanada son 150.528 entradas y 38,5M de parámetros en la primera capa contra 896 de un Conv2d(3,32,3).
  tags: [factual-correction, precision]
  promoted_to: L10
  promoted_at: 2026-08-20
- talk: modelado-redes-neuronales
  date: 2026-08-19
  location: Slide "2. Cómo se ve un tensor"
  feedback: "Acá estamos no explicando redes convolucionales. El hablar de muchas capas produce ruido."
  resolution: Se sacó todo lo convolucional. La card de señal ya no menciona Conv 1D, la de RGB ya no habla de reordenar (era la afirmación que arrastraba la explicación de Conv2D para tener sentido) y las notas del orador perdieron el párrafo de kernels, pesos compartidos y conteos de parámetros. Queda solo la forma del tensor, más una línea que aclara que el resto de la clase va sobre el caso tabular.
  tags: [scope, factual-correction]
  promoted_to: L10
  promoted_at: 2026-08-20
- talk: modelado-redes-neuronales
  date: 2026-08-19
  location: Slide "2. Cómo se ve un tensor"
  feedback: "El apilada no está bien."
  resolution: Correcto, y era el peor error de la diapositiva. "Tres matrices apiladas" sugiere profundidad, o sea un tercer eje espacial, que es exactamente la confusión que la card quería corregir. Y el diagrama las dibujaba apiladas con desfase, reforzando el error. Ahora la card dice "la misma grilla, con tres números en cada píxel" y el diagrama muestra una sola grilla con un píxel ampliado que guarda R, G y B.
  tags: [scope, factual-correction]
  promoted_to: L10
  promoted_at: 2026-08-20
- talk: modelado-redes-neuronales
  date: 2026-08-19
  location: Slide "2. Cómo se ve un tensor"
  feedback: "Confirmá esto con documentación formal sobre cómo modelar esto en un NN."
  resolution: Verificado contra la documentación de Keras y PyTorch, y ejecutado en el venv de la misión. La nota anterior decía "se aplana" como si fuera automático y **eso estaba mal**: una capa densa opera solo sobre el último eje y no aplana sola. Keras: "If the input to the layer has a rank greater than 2, Dense computes the dot product between the inputs and the kernel along the last axis of the inputs". PyTorch nn.Linear: "Output: (*, H_out) where all but the last dimension are the same shape as the input". Aplanar es una capa explícita, Flatten() o nn.Flatten(). Medido: Dense(32) sobre (8,224,224,3) sin aplanar devuelve (8,224,224,32) con 128 parámetros, que es kernel (3,32) más bias; con Flatten() antes devuelve (8,32) con 4.816.928, que es kernel (150.528,32) más bias. El hallazgo confirma la card: el framework por defecto trata el eje de canal como el eje de variables. También valida el número del corpus, los 38,5M eran con 256 unidades.
  tags: [factual-correction, external-source]
  promoted_to: L10
  promoted_at: 2026-08-20
- talk: modelado-redes-neuronales
  date: 2026-08-19
  location: Slide "2. Cómo se ve un tensor"
  feedback: "Pero si son tres números en el mismo píxel, ¿no se puede modelar la red?"
  resolution: Sí se puede, y es exactamente la pregunta que va a hacer un alumno, así que quedó anticipada en las notas del orador. Para una red densa se aplana: los 224 por 224 por 3 se estiran en una fila de 150.528 floats y la red los trata como 150.528 variables sueltas, igual que las columnas de una tabla. Lo que se pierde al aplanar es que tres de esos números eran del mismo píxel y que dos píxeles eran vecinos: esa estructura vive en el dato, no en lo que la red usa. La respuesta refuerza la tesis de la clase, que la red ve un vector de floats, y deja claro que la forma importa para elegir arquitectura, no para poder modelar. No se agregó nada al contenido visible para no reintroducir el ruido de arquitecturas.
  tags: [factual-correction, external-source]
  promoted_to: L10
  promoted_at: 2026-08-20
- talk: prompting
  date: 2026-08-28
  location: Slide "5. Del prompt al entrenamiento"
  feedback: "La afirmación de que el comportamiento se movió al entrenamiento está apoyada de forma indirecta: el corpus tiene a Wei et al. para el mecanismo, y el catálogo de la API para el costo y las perillas removidas, pero no hay un registro sobre el post-entrenamiento por refuerzo de los modelos de razonamiento. ¿Ingestamos una fuente para eso, o la lámina se queda en el nivel de afirmación que la evidencia actual sostiene?"
  resolution: se ingestó DeepSeek-R1 (Nature 2025, DOI 10.1038/s41586-025-09422-z, más el arXiv 2501.12948) y se le dedicaron dos láminas nuevas, 6.3 y 6.4. La afirmación del post-entrenamiento por refuerzo queda apoyada de forma directa. Además se re-ancló la mitad de tiempo de ejecución al system prompt especializado que la API inyecta cuando el thinking está activo, documentado en la captura de Steering thinking. Se retiró la afirmación sobre temperatura y top-p deshabilitados, que ninguna de las capturas sostiene (ver Cut material).
  tags: [add-source, external-source, sources, new-slides]
  promoted_to: L11
  promoted_at: 2026-11-02
- talk: redes-generativas-antagonicas
  date: 2026-10-17
  location: Slide "2. ¿Qué es la IA Generativa de Visión?"
  feedback: "Aplicar los reemplazos ★ del editor solo con fuentes del corpus (Salimans 2016 en 1.3 y 4.8; en 4.7 solo la TC de baja dosis); corregir el crédito de Slanted Land y día→noche (Pix2Pix); deepfakes a Open questions."
  resolution: Tabla: «¿Esto es un tumor maligno o benigno?» / «Genera una imagen de un tumor maligno» → «¿Este dígito es un 7?» / «Genera un 7»; fila de ejemplo → clasificador de dígitos de MNIST y cGAN que genera el dígito pedido (cgan-mirza-osindero-2014). Texto original en Cut material.
  tags: [audience-fit, examples, generalize-examples, cut]
  promoted_to: L11
  promoted_at: 2026-11-02
- talk: redes-generativas-antagonicas
  date: 2026-10-17
  location: Slide "3. ¿Por qué importa en ingeniería?"
  feedback: "Aplicar los reemplazos ★ del editor solo con fuentes del corpus (Salimans 2016 en 1.3 y 4.8; en 4.7 solo la TC de baja dosis); corregir el crédito de Slanted Land y día→noche (Pix2Pix); deepfakes a Open questions."
  resolution: Cifra de la U-Net (Dice 0.9524 vs 0.9459, sin estudio citado) → Salimans et al. (2016), estado del arte semi-supervisado en MNIST, CIFAR-10 y SVHN; notas actualizadas. Texto original en Cut material.
  tags: [audience-fit, examples, factual-correction, external-source, speaker-notes, cut]
  promoted_to: L11
  promoted_at: 2026-11-02
- talk: redes-generativas-antagonicas
  date: 2026-10-17
  location: Slide "6. Tabla comparativa rápida"
  feedback: "Aplicar los reemplazos ★ del editor solo con fuentes del corpus (Salimans 2016 en 1.3 y 4.8; en 4.7 solo la TC de baja dosis); corregir el crédito de Slanted Land y día→noche (Pix2Pix); deepfakes a Open questions."
  resolution: Fila «Caso en biomedicina» → «Caso de uso típico»: SRGAN y Pix2Pix/CycleGAN; Stable Diffusion, DALL·E y Midjourney; SAM para segmentar cualquier objeto y asistir el etiquetado (SA-1B). Texto original en Cut material.
  tags: [audience-fit, examples, tabular, external-source, cut]
  promoted_to: L11
  promoted_at: 2026-11-02
- talk: redes-generativas-antagonicas
  date: 2026-10-17
  location: Slide "1. El Problema: ¡Bienvenidos a Slanted Land! 🌀"
  feedback: "Aplicar los reemplazos ★ del editor solo con fuentes del corpus (Salimans 2016 en 1.3 y 4.8; en 4.7 solo la TC de baja dosis); corregir el crédito de Slanted Land y día→noche (Pix2Pix); deepfakes a Open questions."
  resolution: Crédito corregido: el tutorial y el video son de Luis Serrano («A Friendly Introduction to Generative Adversarial Networks»), no de Rowel Atienza (inconsistencia #1). Fuente serrano-gans-lab agregada.
  tags: [factual-correction, source-link, sources]
  promoted_to: L11
  promoted_at: 2026-11-02
- talk: redes-generativas-antagonicas
  date: 2026-10-17
  location: Slide "1. Tipos de GANs: el punto de partida"
  feedback: "Aplicar los reemplazos ★ del editor solo con fuentes del corpus (Salimans 2016 en 1.3 y 4.8; en 4.7 solo la TC de baja dosis); corregir el crédito de Slanted Land y día→noche (Pix2Pix); deepfakes a Open questions."
  resolution: cGAN: «Genera una imagen histológica de carcinoma ductal» → «Genera un 7» (MNIST, Mirza & Osindero, 2014). Texto original en Cut material.
  tags: [audience-fit, examples, external-source, cut]
  promoted_to: L11
  promoted_at: 2026-11-02
- talk: redes-generativas-antagonicas
  date: 2026-10-17
  location: Slide "5. Fortaleza 1: Generación de imágenes realistas"
  feedback: "Aplicar los reemplazos ★ del editor solo con fuentes del corpus (Salimans 2016 en 1.3 y 4.8; en 4.7 solo la TC de baja dosis); corregir el crédito de Slanted Land y día→noche (Pix2Pix); deepfakes a Open questions."
  resolution: Tarjeta «Imágenes médicas sintéticas» (neurorradiólogos, sin fuente) → «Test de Turing visual (Salimans et al., 2016)»: MNIST indistinguible, 21,3 % de error humano en CIFAR-10. Notas sobre cómo leer la tasa de error. Texto original en Cut material.
  tags: [audience-fit, examples, factual-correction, external-source, speaker-notes, cut]
  promoted_to: L11
  promoted_at: 2026-11-02
- talk: redes-generativas-antagonicas
  date: 2026-10-17
  location: Slide "6. Fortaleza 2: Transformación de imágenes (Image Translation)"
  feedback: "Aplicar los reemplazos ★ del editor solo con fuentes del corpus (Salimans 2016 en 1.3 y 4.8; en 4.7 solo la TC de baja dosis); corregir el crédito de Slanted Land y día→noche (Pix2Pix); deepfakes a Open questions."
  resolution: Fila «Foto de día → noche»: el modelo pasa de CycleGAN a Pix2Pix.
  tags: [factual-correction]
  promoted_to: L11
  promoted_at: 2026-11-02
- talk: redes-generativas-antagonicas
  date: 2026-10-17
  location: Slide "7. Fortaleza 3: Completado de imágenes (Image Inpainting)"
  feedback: "Aplicar los reemplazos ★ del editor solo con fuentes del corpus (Salimans 2016 en 1.3 y 4.8; en 4.7 solo la TC de baja dosis); corregir el crédito de Slanted Land y día→noche (Pix2Pix); deepfakes a Open questions."
  resolution: Quitada la tabla de artefactos de MRI y biopsias; queda solo el caso de tomografías con dosis reducida. Texto original en Cut material.
  tags: [audience-fit, examples, cut]
  promoted_to: L11
  promoted_at: 2026-11-02
- talk: redes-generativas-antagonicas
  date: 2026-10-17
  location: Slide "8. Fortaleza 4: Generación de datos sintéticos para entrenamiento"
  feedback: "Aplicar los reemplazos ★ del editor solo con fuentes del corpus (Salimans 2016 en 1.3 y 4.8; en 4.7 solo la TC de baja dosis); corregir el crédito de Slanted Land y día→noche (Pix2Pix); deepfakes a Open questions."
  resolution: El caso de biopsias (+30 %, sin fuente) pasa a Salimans et al. (2016): GAN y clasificador con pocas etiquetas, estado del arte semi-supervisado en MNIST, CIFAR-10 y SVHN. Bonus de privacidad quitado (sin fuente, y una GAN puede memorizar el entrenamiento). Notas nuevas con el mecanismo. Texto original en Cut material.
  tags: [audience-fit, examples, factual-correction, external-source, speaker-notes, cut]
  promoted_to: L11
  promoted_at: 2026-11-02
- talk: redes-generativas-antagonicas
  date: 2026-10-17
  location: Slide "1. Limitaciones (1 de 2): los problemas de entrenamiento"
  feedback: "Aplicar los reemplazos ★ del editor solo con fuentes del corpus (Salimans 2016 en 1.3 y 4.8; en 4.7 solo la TC de baja dosis); corregir el crédito de Slanted Land y día→noche (Pix2Pix); deepfakes a Open questions."
  resolution: Mode collapse: el ejemplo de tumores pasa a una GAN de MNIST que genera siempre el mismo dígito y no sirve como dataset para un clasificador de diez clases (conocimiento general). Texto original en Cut material.
  tags: [audience-fit, examples, cut]
  promoted_to: L11
  promoted_at: 2026-11-02
- talk: cierre-magnifica-humanitas
  date: 2026-11-02
  location: Agenda
  feedback: "Aplicar las correcciones del fact-check de cifras y fuentes (siete en slides y las menores de fuentes y notas)."
  resolution: Corregidas 7 afirmaciones en slides (1.5, 2.3, 2.18, 3.3, 4.3, 4.4, 4.6), 4 menores en slides (2.4, 3.10 y fuentes de 2.1 y 4.1) y 3 en notas (2.3, 2.10, 3.9), contra las fuentes primarias; texto reemplazado en Cut material, fuentes en el corpus §Fact-check y 3 puntos abiertos (link de Gandalf, artículo de Ford, cifra de citas).
  tags: [fact-check, numeric-fidelity, external-source]
  promoted_to: L11
  promoted_at: 2026-11-02
