---
source_file: AIG4B-Clase-8-GANs.md
source_type: article
ingested_at: 2026-08-14
---

# AIG4B — Clase 8: Visión Generativa / Generative Adversarial Networks (GANs)

## Provenance

- Original location: `research/articles/AIG4B-Clase-8-GANs.md` (+ carpeta de medios `research/articles/AIG4B-Clase-8-GANs-media/`)
- Format: markdown — extracción 1:1 de un deck PowerPoint de 51 slides (`AIG4B-Clase-8-GANs.pptx`, en la raíz del Talk)
- Author / source (if known): la slide 1 dice literalmente **«Autor: Paulo Veiga/Marcos Sanchez Sorondo»**. No hay más atribución de autoría en ninguna otra slide. La única marca institucional del deck es el **logo de la Universidad Austral** (imagen `slide-01-1.png`); el texto del deck nunca nombra a la universidad.
- Date of original (if known): la slide 1 dice **«Última Modificación: Abril, 2026»**. No hay fecha de creación.
- Curso: *Inteligencia Artificial Generativa Aplicada en Biomedicina* (título de la slide 1). Clase 8 de la serie.
- **Notas del orador: cero.** Verificado abriendo el `.pptx`: existen 51 partes `ppt/notesSlides/notesSlideN.xml`, una por slide, pero el placeholder `type="body"` de cada una está vacío — el único texto que contienen es el número de slide (placeholder automático). **0 de 51 slides tienen notas del orador reales.**
- Estructura: 5 secciones — *Panorama de la IA Generativa de Visión* (2–8), *Introducción a las GANs* (9–16), *El Ejemplo de Slanted Land* (17–37), *Tipos de GANs y Aplicaciones en Biomedicina* (38–47), *Limitaciones y Cierre* (48–51).
- Medios: 72 colocaciones de imagen sobre 64 archivos únicos (por md5), más 29 SVG originales detrás de los PNG vectorizados. Todos los bytes copiados a la carpeta compañera, incluido el `_manifest.json` original.

## Key claims

Las 51 slides en orden. Se preservan las tablas como tablas Markdown.

### Sección 1 — Panorama de la IA Generativa de Visión (slides 2–8)

**Slide 1 — portada.** «Inteligencia Artificial Generativa Aplicada en Biomedicina / Clase 8: Vision Generativa / Generative Adversarial Networks (GANs)». Autor: Paulo Veiga/Marcos Sanchez Sorondo. Última modificación: Abril, 2026.

**Slide 2 — agenda de 5 bloques** (se repite verbatim en las slides 9, 17, 38 y 48):

1. **Panorama de la IA Generativa de Visión** — IA discriminativa vs. generativa, línea de tiempo histórica y modelos del curso
2. **Introducción a las GANs** — Origen (Goodfellow 2014), intuición del falsificador y el detective, arquitectura básica
3. **El Ejemplo de Slanted Land** — De la intuición a los números: Discriminador, Generador y sus pesos
4. **Tipos de GANs y Aplicaciones en Biomedicina** — Vanilla GAN, StyleGAN, fortalezas clínicas y generación de datos sintéticos
5. **Limitaciones y Cierre** — Problemas de entrenamiento, evaluación, sesgo y próximos pasos

**Slide 3 — tres preguntas guía:**

| 01 | 02 | 03 |
|---|---|---|
| ¿Qué hace diferente a la IA generativa? | ¿Por qué importa en Biomedicina? | ¿Qué modelos existen? |
| En qué se distingue conceptualmente de otros tipos de IA visual. | Qué problemas reales resuelve en el contexto clínico e investigador. | Un mapa de GANs, Diffusion Networks y SAM — y cuándo usar cada uno. |

**Slide 4 — la distinción fundamental discriminativo/generativo.** «Históricamente, la IA visual se diseñó para analizar lo que ya existe — clasificar radiografías, detectar tumores, medir estructuras. Eso es la IA discriminativa: aprende a distinguir entre categorías. La IA generativa hace algo cualitativamente distinto: aprende a crear contenido visual nuevo que no existía antes.»

| Aspecto | IA Discriminativa | IA Generativa |
|---|---|---|
| ¿Qué hace? | Analiza y clasifica lo que ya existe | Crea contenido nuevo que no existía |
| Pregunta típica | "¿Esto es un tumor maligno o benigno?" | "Genera una imagen de un tumor maligno" |
| Lo que aprende | A distinguir entre categorías | La estructura interna de los datos |
| Salida | Una etiqueta o un número | Una imagen, un sonido, un texto |
| Ejemplo en medicina | Clasificador de histología | Generador de imágenes histológicas sintéticas |

**Slide 5 — por qué importa en Biomedicina: tres barreras.** «Entrenar un buen modelo de diagnóstico por imágenes requiere miles — a veces decenas de miles — de imágenes etiquetadas por expertos.»

| Escasez | Privacidad | Coste |
|---|---|---|
| Ciertas patologías son tan raras que simplemente no existen suficientes casos documentados para entrenar modelos robustos. | Los datos de pacientes están protegidos por regulaciones estrictas: HIPAA, GDPR y legislaciones locales limitan el acceso y la distribución. | Etiquetar imágenes médicas requiere tiempo de especialistas altamente cualificados — un recurso escaso y caro. |

Lo que la IA Generativa habilita: aumentación de datos sintéticos, síntesis de casos raros, traducción entre modalidades (MRI→CT), anonimización con realismo clínico, restauración de imágenes con artefactos. **Cifra:** «Una U-Net entrenada combinando imágenes reales y sintéticas de MRI logró un Dice score de 0.9524 frente a 0.9459 entrenando solo con datos reales.»

**Slide 6 — línea de tiempo.** Encabezado: «Tres eras, un campo en aceleración constante.» Pero enumera **cuatro** bloques:

1. **Era Estadística · 1950s–2000s** — redes neuronales, backpropagation. Prometedor en teoría, muy limitado visualmente en la práctica.
2. **Era de las GANs · 2014–2020** — Ian Goodfellow publica la GAN original. Primera generación fotorrealista. El campo explota en variantes.
3. **Era de la Difusión · 2020–hoy** — DALL·E, Stable Diffusion, Midjourney. Control por texto, generación de vídeo, modelos de base masivos.
4. **SAM & Modelos de Segmentación · 2023–hoy** — Meta lanza Segment Anything Model. Segmentación interactiva prompteable con puntos, cajas o máscaras, sin reentrenamiento.

Cierre: «Este curso empieza con el hito más influyente de la segunda era: las Generative Adversarial Networks.»

**Slide 7 — los tres modelos del curso.**

- **GANs — Generative Adversarial Networks.** «Dos redes que compiten: una genera, la otra evalúa. Motor de los deepfakes, StyleGAN y la síntesis de imágenes médicas.» Pregunta: *¿Cómo generar imágenes realistas que "engañen" a un evaluador?*
- **Diffusion Networks.** «Aprenden a reconstruir una imagen desde el ruido, paso a paso. Motor de Stable Diffusion, DALL·E y Midjourney.» Pregunta: *¿Cómo generar imágenes diversas y controlables a partir de una descripción?*
- **SAM — Segment Anything Model (Meta, 2023).** «No genera imágenes — las entiende. Puede segmentar cualquier objeto en cualquier imagen con precisión quirúrgica. Es prompteable: se guía con puntos, cajas o máscaras.» Pregunta: *¿Cómo identificar y aislar estructuras en imágenes médicas de forma automatizada e interactiva?*

**Slide 8 — tabla comparativa.** «Esta tabla no es para memorizar — es para consultar cuando tengas un problema real y necesites decidir qué herramienta usar.»

| Criterio | GANs | Diffusion Networks | SAM |
|---|---|---|---|
| ¿Para qué sirve? | Generar imágenes realistas, transformar modalidades, aumentar datos | Generar imágenes desde texto o guías visuales con alta diversidad | Segmentar y aislar estructuras en imágenes existentes |
| Velocidad | Muy rápida (una pasada) | Lenta (muchos pasos iterativos) | Muy rápida |
| Control | Moderado | Alto (guiado por texto) | Alto (guiado por puntos o cajas) |
| Fortaleza | Velocidad + realismo | Diversidad + controlabilidad | Precisión de segmentación |
| Limitación | Inestabilidad, mode collapse | Lento, costoso computacionalmente | No genera contenido nuevo |
| Caso en biomedicina | Síntesis histológica, MRI→CT | Generación desde descripciones clínicas | Segmentación de tumores, órganos, células |

### Sección 2 — Introducción a las GANs (slides 9–16)

**Slide 9 —** repetición de la agenda de 5 bloques.

**Slide 10 —** separador de sección titulado «Generative Adversarial Networks (GANs)». **Sin cuerpo: la slide no tiene contenido alguno más allá del título.**

**Slide 11 — punto de partida.** «"¿Cómo enseñarle a una máquina a crear algo que nunca ha visto?" Esta es la pregunta que Ian Goodfellow se hizo en 2014. La respuesta que encontró cambió el campo de la inteligencia artificial para siempre y puso en marcha una de las líneas de investigación más prolíficas de la historia de la IA.»

| La idea central | El recorrido de este capítulo |
|---|---|
| En lugar de enseñarle a una red a crear directamente, haz que compita contra otra red que aprende a detectar sus errores. La presión de la competencia hace que ambas mejoren continuamente. | De dónde vienen las GANs y cómo evolucionaron<br>Cómo funcionan por dentro — sin fórmulas, con intuición<br>Para qué sirven y dónde tienen límites<br>Cómo se aplican concretamente en Biomedicina |

**Slide 12 — el origen: una noche en un bar (2014).** «Montreal, junio de 2014. Ian Goodfellow, 27 años, propone en una conversación de bar una idea aparentemente simple: ¿y si en lugar de una sola red, usamos dos? Una que genera, otra que evalúa. Que compitan. Sus colegas son escépticos. Esa misma noche implementa el prototipo. Funciona en el primer intento.» Cifra destacada: **«70K+ Citas del paper original»**. Cita: **«La idea más interesante en machine learning en los últimos 20 años.» — Yann LeCun**.

**Slide 13 — modelo mental: el falsificador y el detective.** «Un experimento mental: el mundo de los rostros. Imaginad una sociedad donde existen miles de rostros reales con características reconocibles. En esa sociedad aparecen dos personajes con objetivos opuestos:»

| El Falsificador | El Detective |
|---|---|
| Objetivo: crear rostros que parezcan pertenecer a ese mundo.<br>Método: prueba y error. Genera un rostro, recibe feedback, ajusta, repite. Puede estudiar todos los rostros reales que quiera, pero no sabe cómo se fabrican. | Objetivo: distinguir los rostros reales de los falsos.<br>Ventaja: ve ambos tipos — los reales del dataset y los que produce el falsificador. Como el falsificador mejora constantemente, él también tiene que mejorar. |

«¿Qué pasa cuando estos dos compiten durante miles — o millones — de rondas? Los dos se vuelven extraordinariamente buenos en lo suyo.»

**Slide 14 — arquitectura de una GAN: el mapeo analogía → componente.**

| Analogía | Componente técnico | Función |
|---|---|---|
| El Falsificador | Generador (G) | Transforma ruido aleatorio en imágenes sintéticas |
| Los rostros falsos | Imágenes generadas | Output del Generador — al principio, puro ruido visual |
| El Detective | Discriminador (D) | Clasifica cada imagen como "real" o "falsa" con un score entre 0 y 1 |
| El veredicto | Señal de pérdida (loss) | Número que mide el error de cada red y guía su aprendizaje |
| Las rondas de competencia | Épocas de entrenamiento | Ciclos en los que ambas redes actualizan sus parámetros internos |

Etiquetas sueltas del diagrama: «Clasificación / Salida: real o falso», «Generador / Recibe ruido aleatorio», «Arquitectura GAN», «Discriminador», «Salida sintética», «Recibe reales y generadas», «Imágenes generadas».

**Slide 15 — arquitectura de una "Vanilla" GAN.** Única fuente citada: **[¿Qué es una GAN? — Explicación sobre las redes generativas antagónicas — AWS](https://aws.amazon.com/es/what-is/gan/)**. El diagrama es la pieza visual central de la sección (ver *Images / diagrams*, `slide-15-1.jpg`).

**Slide 16 — entrenamiento paso a paso.** Encabezado: «**Cuatro pasos** que se repiten miles de veces — así es como una GAN aprende a engañar.» El cuerpo enumera **cinco**:

- **Paso 1 — El Generador produce su primer intento.** «Recibe como entrada un vector de ruido aleatorio — números al azar que representan un punto en un espacio de posibilidades. Con ese ruido como semilla, produce una imagen. Al principio del entrenamiento, esa imagen es literalmente ruido visual — manchas sin forma ni sentido. Analogía: el falsificador en su primer día. No sabe nada de los rostros reales — produce garabatos.»
- **Paso 2 — El Discriminador evalúa.** «Recibe dos tipos de inputs en cada ronda: imágenes reales del dataset de entrenamiento e imágenes falsas producidas por el Generador en el Paso 1. Su tarea: asignar a cada imagen una probabilidad de ser real (entre 0 y 1). Al principio tiene la tarea fácil — las imágenes del Generador son obviamente falsas.»
- **Paso 3 — El Discriminador emite su veredicto.** «Produce un número entre 0 y 1: cerca de 1 → "Esto es real"; cerca de 0 → "Esto es claramente falso"; cerca de 0.5 → "No tengo idea". Cuando el Generador logra que el Discriminador dé 0.5 de forma consistente, es el éxito.»
- **Paso 4 — Ambos aprenden del resultado.** «El veredicto se convierte en señal de aprendizaje: el Generador ajusta sus parámetros para engañar mejor la próxima vez; el Discriminador ajusta los suyos para detectar mejor. Ambos actualizan simultáneamente — cada uno aprende del error del otro.»
- **Paso 5 — El ciclo se repite miles de veces.** «Generar → evaluar → aprender. Este loop puede repetirse cientos de miles de veces. Con cada iteración, el Generador produce imágenes más convincentes y el Discriminador se vuelve más exigente. Al final, el ojo humano no puede distinguir lo real de lo generado.»

### Sección 3 — El Ejemplo de Slanted Land (slides 17–37)

Construcción pedagógica larga: **21 slides** que van de la fábula al cálculo de la derivada. No comprimir.

**Slide 17 —** repetición de la agenda.

**Slide 18 — el problema: ¡Bienvenidos a Slanted Land! 🌀** «Imagina un mundo peculiar llamado Slanted Land, donde absolutamente todo se inclina: los árboles, las casas, las personas e incluso la pizza que comen los gatos. En este universo, la norma es la inclinación. Los habitantes de Slanted Land solo conocen rostros con una ligera inclinación. Para ellos, un rostro completamente recto sería una anomalía, algo totalmente extraño e incomprensible.»

«El problema urgente: la app de citas de Slanted Land, **TiltedTinder**, necesita generar fotos de perfil para sus usuarios. Pero solo tienen **4 fotos reales** en toda su base de datos. Con tan pocos datos, nadie encuentra pareja. ¡La supervivencia romántica de toda una civilización inclinada depende de nuestra GAN! 💘»

| Universo Inclinado | Rostros "Normales" |
|---|---|
| Todo, desde la gravedad hasta las cejas de sus habitantes, está en un ángulo distintivo. | Solo existen los rostros inclinados; un rostro recto les resulta completamente alienígena. |

Atribución al pie: «[Basado en el tutorial de **Rowel Atienza** — ver video:](https://www.youtube.com/watch?v=8L11aMN5KY8&t=16s)» — **atribución errónea, ver `Inconsistencies / open questions` #1.**

**Slide 19 — el mundo de Slanted Land.**

| Imágenes 2×2 píxeles | Dataset real | Red de una sola capa |
|---|---|---|
| Cada imagen se representa como una pantalla con 4 celdas — cada celda tiene un valor entre 0 (blanco) y 1 (negro). | Son imágenes de personas inclinadas. El Generador va a aprender a producir imágenes que se parezcan a esas personas. | La arquitectura más simple posible — ideal para entender los fundamentos sin complejidad adicional. |

**Slide 20 — los datos reales: caras con patrón.** «Las "caras" de Slanted Land, codificadas como píxeles, tienen un patrón consistente:»

- Esquinas oscuras en la diagonal principal (arriba-izquierda y abajo-derecha): **valor alto**
- Esquinas claras en la diagonal secundaria (arriba-derecha y abajo-izquierda): **valor bajo**

«Ese patrón diagonal es la "firma" de una cara real. El Discriminador tiene que aprenderlo para poder distinguirla del ruido.»

**Slide 21 — caras vs. ruido.**

| Caras (imágenes reales) | Ruido (imágenes falsas) |
|---|---|
| Valores altos en la diagonal principal, bajos en la secundaria. Patrón estructurado y reconocible. | Valores sin patrón, distribuidos aleatoriamente. Sin estructura diagonal. El Discriminador debe aprender a distinguirlos a partir de esos valores numéricos. |

**Slide 22 — construyendo el Discriminador: ¿qué píxeles importan?** «El Discriminador aprende que en las caras de Slanted Land:»

- Los píxeles de la **diagonal principal** son grandes → reciben **peso positivo (+1)**
- Los píxeles de la **diagonal secundaria** son pequeños → reciben **peso negativo (−1)**

«Asigna estos pesos a cada posición: +1 para las que caracterizan una cara, −1 para las que no la caracterizan.»

**Slide 23 — cálculo del score.** «El score de una imagen = suma ponderada de sus valores de píxel × pesos aprendidos:»

| Cara prototipo | Imagen de ruido |
|---|---|
| 1×(+1) + 0×(−1) + 0×(−1) + 1×(+1) = **2** | 0.25×(+1) + 1×(−1) + 0.5×(−1) + 0.75×(+1) = **−0.5** |
| Score > 1 → Real ✓ | Score < 1 → Falsa ✓Score > 1 → Real ✓ *(celda con el texto duplicado en el original)* |

**Slide 24 — el Discriminador como red neuronal.** «Para la cara prototipo: σ(1×(+1) + 0×(−1) + 0×(−1) + 1×(+1) − 1) = σ(1)»

| Entradas (z) | Pesos (w) | Bias |
|---|---|---|
| z₁=1, z₂=0, z₃=0, z₄=1 | w₁=+1, w₂=−1, w₃=−1, w₄=+1 | valor fijo = 1, peso = −1 |

| Suma ponderada | Sigmoid |
|---|---|
| 1(+1)+0(−1)+0(−1)+1(+1)+1(−1) = 1 | σ(1) ≈ 0.73 → imagen real |

**Slide 25 — función sigmoid.** «La función sigmoid convierte cualquier número real en una probabilidad entre 0 y 1. Es la función de activación que usa el Discriminador para emitir su veredicto.» Fórmula (en imagen): **σ(x) = 1 / (1 + e⁻ˣ)**.

| Rango acotado | Diferenciable | Monótona creciente | Punto medio en 0 |
|---|---|---|---|
| Devuelve valores entre 0 y 1; se lee como probabilidad. | Es suave en todo punto; permite backpropagation. | Si sube la entrada, sube la salida; conserva el orden. | σ(0) = 0.5; umbral natural de decisión. |

**Slide 26 — todo junto: el Discriminador completo.**

- «Cuando la cara prototipo pasa por la red completa: **σ(1) = 0.73** → "Estoy un 73% seguro de que esto es real". Como 0.73 > 0.5, clasifica correctamente la imagen como real ✓»
- «Cuando la imagen de ruido pasa por la misma red: **σ(−0.5) = 0.37** → "Estoy solo un 37% seguro de que esto sea real". Como 0.37 < 0.5, clasifica correctamente la imagen como falsa ✓»

**Slide 27 — construyendo el Generador: el objetivo opuesto.** «El Generador recibe un número aleatorio z (entre 0 y 1 — el "ruido latente") y tiene que producir una imagen de 2×2 píxeles. Su objetivo: producir imágenes que el Discriminador clasifique como reales (output cercano a 1). La estructura es la inversa del Discriminador: de 1 número → 4 píxeles. En redes reales, esto se implementa con capas de upsampling y convoluciones transpuestas.»

**Slide 28 — el Generador en acción: z = 0.7 → imagen.** «Con z = 0.7 como entrada y los pesos aprendidos, el Generador produce una imagen que reproduce el patrón diagonal de las caras reales. El Generador aprendió a engañar al Discriminador. El resultado muestra el patrón diagonal característico de las caras de Slanted Land: valores altos en la diagonal principal, bajos en la secundaria. El Generador internalizó la estructura del dataset real.» *(la imagen da los números concretos: σ(1.7)=0.85 y σ(−1.7)=0.15 → matriz [[0.85, 0.15],[0.15, 0.85]])*

**Slide 29 — proceso de entrenamiento: la función de error.** «En los slides anteriores definimos los pesos del Discriminador y el Generador a mano (+1, −1, Bias). En la práctica, la red debe aprender esos pesos sola. Para eso necesitamos una forma de medir cuánto se equivocó — esa es la función de error. La función que hace eso en las GANs se llama **log-loss (binary cross-entropy)**:»

| Cuando queremos que la predicción sea 1 | Cuando queremos que la predicción sea 0 |
|---|---|
| Error = −ln(predicción)<br>Se usa cuando la imagen es real y el Discriminador debe acercarse a 1. | Error = −ln(1 − predicción)<br>Se usa cuando la imagen es falsa y el Discriminador debe acercarse a 0. |

«La propiedad clave: el error es grande cuando la predicción está lejos del objetivo, y pequeño cuando está cerca. Esto guía el aprendizaje en la dirección correcta.»

**Slide 30 — log-loss: los dos casos.**

| Label = 1 — Imagen Real | Label = 0 — Imagen Falsa |
|---|---|
| 🔍 Discriminador entrenando con imagen real. Debe acercarse a 1.<br>✅ Predicción = 0.9 → −ln(0.9) ≈ 0.1 → Error pequeño<br>❌ Predicción = 0.1 → −ln(0.1) ≈ 2.3 → Error enorme | 🎨 Generador entrenando: el Discriminador debe acercarse a 0 (detectar la imagen como falsa).<br>✅ Predicción = 0.1 → −ln(0.9) ≈ 0.1 → Error pequeño<br>❌ Predicción = 0.9 → −ln(0.1) ≈ 2.3 → Error enorme |

Fórmulas en imagen: **Error_D = −ln(predicción)** y **Error_G = −ln(1 − predicción)**.

**Slide 31 — loss function visualmente.** Dos gráficas:

- 🔍 **Discriminador — imagen real:** «Predicción = 1 (imagen real). Error = −ln(predicción). Predicción baja → alto error. Predicción alta → bajo error. El Discriminador quiere acercarse a 1 cuando ve imágenes reales.»
- 🎨 **Generador — imagen falsa:** «Predicción = 0 (imagen falsa). Error = −ln(1−predicción). Predicción alta → alto error. El Generador quiere que el Discriminador le asigne score alto (cercano a 1) — lo opuesto al objetivo del Discriminador.»

**Slide 32 — backpropagation: del error al ajuste de pesos.** «Una vez calculado el error, la red lo "propaga hacia atrás" para ajustar cada peso:»

- Pesos con **alta** contribución al error → se ajustan **más**
- Pesos con **baja** contribución al error → se ajustan **poco**
- La dirección del ajuste apunta siempre a reducir el error

«Este proceso ocurre simultáneamente en el Generador y el Discriminador en cada iteración.»

**Slide 33 — backpropagation: el procedimiento paso a paso.**

| 01 | 02 | 03 |
|---|---|---|
| Calcular el error | Derivar la sensibilidad de cada peso | Actualizar en la dirección opuesta al gradiente |

- 01: «La función log-loss da un número que mide qué tan lejos estuvo la red de la respuesta correcta.»
- 02: «Con la regla de la cadena se calcula ∂E/∂w para cada peso: si subo este peso un poco, ¿el error sube o baja?»
- 03: «**w_nuevo = w_actual − α · (∂E/∂w)** — α (learning rate) controla el tamaño del paso.»
- 04 — **Repetir para todos los pesos, en ambas redes:** «El cálculo se ejecuta para cada peso del Discriminador y del Generador de forma simultánea.»

**Slide 34 — backpropagation: ejemplo con Slanted Land.** «Con el error del Discriminador = 1.14 y output D(G(z)) = 0.68, calculamos el ajuste concreto usando la derivada **∂E/∂wᵢ = −[1 − D(x)] · xᵢ**:»

| Píxel | Valor xᵢ | ∂E/∂w | α = 0.1 | w_nuevo |
|---|---|---|---|---|
| Arriba-izq (diagonal) | 0.25 | −0.32 × 0.25 = −0.08 | −0.1 × (−0.08) | 1 + 0.008 = 1.008 ↑ |
| Arriba-der | 1.00 | −0.32 × 1.00 = −0.32 | −0.1 × (−0.32) | −1 + 0.032 = −0.968 ↑ |

«Los pesos se mueven en la dirección que hace al Discriminador más exigente: en la próxima iteración dará un score más bajo a imágenes similares.»

**Slide 35 — el ciclo completo: Generador y Discriminador juntos.** «Con z = 0.7, el Generador produce una imagen → el Discriminador la evalúa → output: **0.68**. Este único número conecta los dos errores:»

| Error del Discriminador | Error del Generador |
|---|---|
| Recibió 0.68 cuando quería dar 0 → se equivocó. Debe ajustar sus pesos para detectar mejor. | Recibió 0.68 cuando quería que diera 1 → casi lo engañó, pero no del todo. Debe ajustar para engañar más. |

**Slide 36 — el error del Discriminador.** «El Discriminador recibió una imagen falsa pero le asignó un score de 0.68 (quería dar 0):» Fórmula en imagen: **Error_D = −ln(1 − 0.68) = −ln(0.32) ≈ 1.14**. «Un error considerable. El Discriminador va a ajustar sus pesos para clasificar mejor estas imágenes en la próxima iteración — volviéndose más exigente y difícil de engañar.»

**Slide 37 — para los curiosos: la derivada del error.** «La derivada del error del Discriminador respecto a sus pesos permite calcular exactamente cuánto ajustar cada uno:» Fórmula en imagen: **∂E/∂wᵢ = −[1 − D(x)] xᵢ**. «Este cálculo es lo que backpropagation ejecuta automáticamente en cada iteración, para todas las capas y todos los pesos de la red. La regla de la cadena lo hace computacionalmente eficiente incluso con millones de parámetros. Slide opcional — para quien quiera profundizar en la matemática. **Fuente: A Friendly Introduction to Generative Adversarial Networks — Luis Serrano Academy.**» La figura completa (`slide-37-3.jpg`) trae la derivación entera — ver *Raw / preserved excerpts*.

### Sección 4 — Tipos de GANs y Aplicaciones en Biomedicina (slides 38–47)

**Slide 38 —** repetición de la agenda.

**Slide 39 — tipos de GANs: el punto de partida.** «Todo lo que describimos corresponde a la Vanilla GAN — el modelo original de Goodfellow (2014). Pero ese modelo base tiene limitaciones importantes, y surgieron variantes especializadas que resuelven problemas concretos.»

- **Vanilla GAN · Goodfellow et al. 2014** — «Generador produce imágenes desde ruido aleatorio. Sin control sobre el resultado. Inestable y de baja calidad visual. Uso: punto de partida teórico.»
- **Conditional GAN (cGAN) · Mirza & Osindero, 2014** — «Generador y Discriminador reciben etiquetas de clase como condición. "Genera una imagen histológica de carcinoma ductal." Uso: síntesis por patología, aumentación controlada.»

| DCGAN · Radford et al., 2015 | SRGAN · Ledig et al., 2017 |
|---|---|
| Reemplaza capas densas con redes convolucionales. Entrenamiento estable, imágenes nítidas. Uso: base estándar para generación de imágenes de calidad. | Especializado en ampliar imágenes de baja a alta resolución. Infiere detalles finos que no estaban en la imagen original. Uso: mejora de imágenes médicas de menor calidad. |

**Slide 40 — el salto que lo cambió todo: StyleGAN (2018).** «El problema que nadie había resuelto en cuatro años: las GANs generaban imágenes, pero no podías pedirle "genera una cara joven, con pelo castaño y expresión neutral". El Generador mezclaba todos los atributos juntos sin control. ¿Qué cambió exactamente en StyleGAN? En una GAN clásica, el ruido entra directamente y todo (forma, color, textura) sale del mismo vector mezclado. StyleGAN lo separa en capas independientes:»

| Componente | Qué hace | Qué controla |
|---|---|---|
| Red de mapeo (mapping network) | Transforma el ruido en un vector de estilo (w) | Define las características globales de la imagen |
| Síntesis por capas (AdaIN) | Inyecta el estilo en distintas capas de la red | Cada capa controla una escala diferente de detalle |
| Ruido estocástico por capa | Añade variación aleatoria capa a capa | Controla variaciones finas: poros, pelo suelto, arrugas |

«**Style mixing:** StyleGAN permite tomar la estructura de una cara (pose, forma) y el estilo de otra (color de pelo, edad) para generar una cara completamente nueva con coherencia total. Esto no era posible en ninguna GAN anterior.»

**Slide 41 — StyleGAN: arquitectura. Dos redes en lugar de una.** Caption presente en la slide: «Caras fotorrealistas generadas por StyleGAN (**NVIDIA, 2019**)» — *pero la slide no muestra ninguna cara; ver inconsistencia #3.*

- 🔀 **Mapping Network:** transforma el ruido z en un vector de estilo w (**512 dimensiones**)
- 🎨 **Synthesis Network:** genera la imagen progresivamente, inyectando el estilo w en cada capa

«Esto permite controlar atributos separados en cada nivel de resolución: pose y forma en capas bajas, textura y color en capas altas. La clave: el estilo se inyecta en cada capa mediante **AdaIN (Adaptive Instance Normalization)**, no solo al inicio. Esto da control granular sobre cada aspecto visual.»

**Slide 42 — StyleGAN: innovaciones clave.** «StyleGAN (NVIDIA) redefine la generación de imágenes al modificar **únicamente el Generador**, manteniendo el Discriminador estándar. Sus tres innovaciones arquitectónicas permiten control fino sobre el estilo y alta calidad visual.»

| Progressive Growing | Bi-linear Sampling | Mapping Network + AdaIN |
|---|---|---|
| Entrena comenzando con imágenes de **4×4** píxeles y agrega capas progresivamente hasta **1024×1024**. Mejora la estabilidad del entrenamiento y la calidad final. | Reemplaza el muestreo nearest-neighbor por bi-linear sampling en up/downsampling, reduciendo artefactos y logrando transiciones más suaves. | Una **red de 8 capas** transforma el vector latente z en un vector intermedio w, que modula las características vía AdaIN. Permite controlar textura, iluminación y estilo de forma independiente por nivel. |

«**Fuente: GeeksforGeeks — StyleGAN: Style Generative Adversarial Networks**»

**Slide 43 — Fortaleza 1: generación de imágenes realistas.** «El resultado más sorprendente de las GANs: imágenes que el ojo humano no puede distinguir de las reales. Después de millones de rondas de entrenamiento, el Generador aprendió la estructura profunda de cómo lucen esas imágenes — proporciones, distribución de luz, imperfecciones que hacen que algo parezca real.»

- **ThisPersonDoesNotExist.com** — «Cada recarga genera un rostro humano completamente inventado con StyleGAN. Ninguno existe en el mundo real.»
- **Imágenes médicas sintéticas** — «GANs entrenadas con resonancias magnéticas generan imágenes de cerebro que **neurorradiólogos no pueden distinguir de las reales en estudios ciegos**.»
- **Videojuegos y entretenimiento** — «Las GANs generan texturas, escenarios y personajes con un nivel de detalle que antes requería artistas trabajando manualmente durante días.»

**Slide 44 — Fortaleza 2: transformación de imágenes (image translation).** «Las GANs pueden transformar una imagen en otra preservando la estructura subyacente. Aplicación clínica clave: MRI → CT sin necesitar al mismo paciente escaneado dos veces — reduce costes, tiempo y exposición a radiación.»

| Input | Output | Modelo |
|---|---|---|
| Boceto de un edificio | Foto del edificio terminado | Pix2Pix |
| Foto de día | La misma foto de noche | CycleGAN |
| Imagen de un caballo | La misma imagen con una cebra | CycleGAN |
| Imagen de baja resolución | Alta resolución (super-resolución) | SRGAN |
| Imagen en blanco y negro | La misma imagen en color | DeOldify / CycleGAN |
| MRI de cerebro | Imagen equivalente de CT | CycleGAN médico |

**Slide 45 — Fortaleza 3: completado de imágenes (image inpainting).** «Las GANs pueden reconstruir regiones faltantes de forma coherente con el contexto. La red recibe una imagen con una región enmascarada e infiere el contenido más probable basándose en colores, texturas y estructuras adyacentes. **No copia píxeles cercanos — entiende el contenido semántico de la escena completa.**»

| Artefactos de movimiento en MRI | Biopsias con burbujas o pliegues |
|---|---|
| Reconstruye la imagen original estimada eliminando las distorsiones causadas por el movimiento del paciente durante la adquisición. | Completa el tejido faltante en preparaciones histológicas con defectos de proceso o manipulación. |

**Tomografías con dosis reducida** — «Recupera la información sacrificada en protocolos de baja radiación, protegiendo al paciente sin perder calidad diagnóstica.»

**Slide 46 — Fortaleza 4: generación de datos sintéticos para entrenamiento.**

- **El cuello de botella en IA médica:** «Enfermedades raras → pocos casos documentados. Datos de pacientes → protegidos por regulaciones estrictas. Etiquetado → requiere especialistas, es caro y lento.»
- **La solución con GANs:** «Entrenar con las pocas imágenes reales disponibles y generar miles de imágenes sintéticas adicionales para ampliar el dataset.»
- **Cifra:** «Una GAN entrenada con biopsias histológicas de tumores de mama generó imágenes indistinguibles de las reales para patólogos. Combinando datos reales y sintéticos, **la precisión del clasificador mejoró un 30%**.»
- **Bonus:** «los datos sintéticos no corresponden a ningún paciente real → no están sujetos a restricciones de privacidad (HIPAA, GDPR).»

**Slide 47 — el dataset importa: lo que le das es lo que obtenés.** «Una GAN solo puede generar lo que aprendió. Si el dataset mezcla clases sin etiquetas, el Generador produce híbridos incoherentes — inútiles para entrenar clasificadores. En Biomedicina, el dataset debe ser homogéneo dentro de cada clase — o usar una Conditional GAN.»

| Tipo de dataset | Lo que genera la GAN |
|---|---|
| Solo imágenes de gatos | Gatos variados y realistas ✓ |
| Solo imágenes de perros | Perros variados y realistas ✓ |
| Gatos + perros sin etiqueta | Híbridos incoherentes ✗ |
| Gatos + perros con etiqueta (cGAN) | Puede generar cada clase por separado ✓ |

«En aplicaciones médicas reales, asegurate de que el dataset de entrenamiento esté limpio, bien etiquetado y sea homogéneo dentro de cada clase patológica antes de empezar a entrenar.»

### Sección 5 — Limitaciones y Cierre (slides 48–51)

**Slide 48 —** repetición de la agenda.

**Slide 49 — limitaciones (1 de 2): los problemas de entrenamiento.**

| Mode Collapse — el más común y frustrante | Inestabilidad en el entrenamiento |
|---|---|
| El Generador descubre un "truco": produce siempre el mismo tipo de imagen que engaña al Discriminador, en lugar de aprender toda la variedad posible.<br>Analogía: el falsificador que solo falsifica un tipo de billete. En medicina: una GAN para síntesis de tumores que solo genera un tipo de morfología produce datos sintéticos inútiles. | El balance entre Generador y Discriminador es frágil. Si el Discriminador es demasiado bueno, el Generador no recibe señal útil y el gradiente "desaparece". Si el Discriminador es demasiado malo, el Generador aprende trucos baratos en lugar de aprender la distribución real. |

**Slide 50 — limitaciones (2 de 2): evaluación, coste y sesgo.**

| Dificultad para evaluar la calidad | Alta demanda computacional | Sesgo heredado del dataset |
|---|---|---|
| No existe una métrica universal. Las más usadas — **FID** e **Inception Score (IS)** — son aproximaciones imperfectas que no reemplazan la evaluación humana experta. | Entrenar una GAN de calidad requiere GPUs potentes, datasets grandes y horas o días de entrenamiento. Una barrera real para equipos con recursos limitados. | Si los datos tienen sesgos — subrepresentación de grupos demográficos o patologías concretas — las imágenes generadas van a heredar y amplificar esos sesgos. |

**Slide 51 — cierre: lo que aprendimos y lo que sigue.** «En este capítulo construimos la comprensión de las GANs desde cero, siguiendo una narrativa completa:»

| 01 — La intuición | 02 — La arquitectura | 03 — El entrenamiento |
|---|---|---|
| El falsificador y el detective, compitiendo para mejorar mutuamente. | Generador y Discriminador como implementación técnica de esa intuición. | El ciclo de cinco pasos que hace converger al sistema, con el ejemplo de Slanted Land. |

| 04 — La lógica matemática | 05 — Fortalezas y limitaciones |
|---|---|
| El juego minimax como marco conceptual, log-loss y backpropagation. | Cuatro capacidades concretas en Biomedicina y los problemas reales antes de usar GANs en producción. |

## Definitions and terminology

- **IA discriminativa** (slide 4) — «Analiza y clasifica lo que ya existe»; aprende a distinguir entre categorías; salida = una etiqueta o un número.
- **IA generativa de visión** (slide 4) — «Crea contenido nuevo que no existía»; aprende la estructura interna de los datos; salida = una imagen, un sonido, un texto.
- **Generador (G)** (slide 14) — «Transforma ruido aleatorio en imágenes sintéticas». En Slanted Land (slide 27): «recibe un número aleatorio z (entre 0 y 1 — el "ruido latente") y tiene que producir una imagen de 2×2 píxeles… La estructura es la inversa del Discriminador: de 1 número → 4 píxeles. En redes reales, esto se implementa con capas de upsampling y convoluciones transpuestas.»
- **Discriminador (D)** (slide 14) — «Clasifica cada imagen como "real" o "falsa" con un score entre 0 y 1».
- **Entrenamiento adversarial** (slides 13, 16) — dos redes con objetivos opuestos que se actualizan simultáneamente; «cada uno aprende del error del otro». Criterio de éxito (slide 16): «Cuando el Generador logra que el Discriminador dé 0.5 de forma consistente, es el éxito.»
- **Espacio latente / ruido latente (z)** (slides 16, 27, 41) — «un vector de ruido aleatorio — números al azar que representan un punto en un espacio de posibilidades». En Slanted Land z es un escalar en [0,1]; en StyleGAN, el vector w derivado tiene 512 dimensiones.
- **Señal de pérdida (loss)** (slide 14) — «Número que mide el error de cada red y guía su aprendizaje».
- **Época de entrenamiento** (slide 14) — «Ciclos en los que ambas redes actualizan sus parámetros internos».
- **Sigmoid (σ)** (slide 25) — σ(x) = 1/(1+e⁻ˣ). Rango acotado (0,1), diferenciable, monótona creciente, σ(0)=0.5.
- **Score / suma ponderada** (slides 22–24) — Σ xᵢwᵢ + b; con pesos +1 en la diagonal principal y −1 en la secundaria, y bias = −1.
- **Log-loss / binary cross-entropy** (slide 29) — Error = −ln(predicción) cuando el objetivo es 1; Error = −ln(1 − predicción) cuando el objetivo es 0.
- **Backpropagation** (slides 32–34) — propagación del error hacia atrás; regla de la cadena; regla de actualización **w_nuevo = w_actual − α · (∂E/∂w)**; α = learning rate.
- **Mode collapse** (slide 49) — «El Generador descubre un "truco": produce siempre el mismo tipo de imagen que engaña al Discriminador, en lugar de aprender toda la variedad posible.» Analogía: «el falsificador que solo falsifica un tipo de billete.»
- **Inestabilidad / gradiente que desaparece** (slide 49) — «Si el Discriminador es demasiado bueno, el Generador no recibe señal útil y el gradiente "desaparece".»
- **Vanilla GAN** (slide 39) — Goodfellow et al. 2014. Ruido → imagen, sin control. Inestable, baja calidad. «Punto de partida teórico.»
- **Conditional GAN (cGAN)** (slide 39) — Mirza & Osindero, 2014. «Generador y Discriminador reciben etiquetas de clase como condición.»
- **DCGAN** (slide 39) — Radford et al., 2015. «Reemplaza capas densas con redes convolucionales.»
- **SRGAN** (slide 39) — Ledig et al., 2017. Super-resolución; «infiere detalles finos que no estaban en la imagen original».
- **StyleGAN** (slides 40–42) — NVIDIA. Modifica únicamente el Generador. Tres innovaciones: progressive growing, bi-linear sampling, mapping network + AdaIN.
- **Mapping network** (slides 40–42) — red de 8 capas que transforma el vector latente z en un vector de estilo intermedio w (512 dimensiones).
- **AdaIN — Adaptive Instance Normalization** (slides 40–42) — inyección del estilo w en cada capa de la red de síntesis, no solo al inicio; «da control granular sobre cada aspecto visual».
- **Progressive growing** (slide 42) — «Entrena comenzando con imágenes de 4×4 píxeles y agrega capas progresivamente hasta 1024×1024.»
- **Bi-linear sampling** (slide 42) — reemplaza nearest-neighbor en up/downsampling; reduce artefactos.
- **Ruido estocástico por capa** (slide 40) — «Controla variaciones finas: poros, pelo suelto, arrugas».
- **Style mixing** (slide 40) — «tomar la estructura de una cara (pose, forma) y el estilo de otra (color de pelo, edad) para generar una cara completamente nueva con coherencia total».
- **Image-to-image / image translation** (slide 44) — **Pix2Pix** (pares alineados: boceto→foto), **CycleGAN** (día→noche, caballo→cebra, MRI→CT), **DeOldify** (B/N→color).
- **Image inpainting** (slide 45) — completado de regiones enmascaradas por comprensión semántica de la escena, no por copia de píxeles vecinos.
- **FID e Inception Score (IS)** (slide 50) — las métricas más usadas para evaluar GANs; «aproximaciones imperfectas que no reemplazan la evaluación humana experta». *El deck no expande las siglas ni da fórmulas.*
- **SAM — Segment Anything Model** (slides 6, 7, 8) — Meta, 2023. No genera: segmenta. Prompteable con puntos, cajas o máscaras, sin reentrenamiento.
- **Slanted Land** (slide 18) — mundo ficticio donde todo se inclina; el dataset real tiene solo 4 caras; la app de citas se llama **TiltedTinder**.

## Evidence and examples

Cifras y ejemplos concretos, cada uno con su slide de origen:

| Dato | Slide | Texto literal |
|---|---|---|
| **Dice 0.9524 vs 0.9459** | 5 | «Una U-Net entrenada combinando imágenes reales y sintéticas de MRI logró un Dice score de 0.9524 frente a 0.9459 entrenando solo con datos reales.» |
| **70K+ citas** | 12 | «70K+ / Citas del paper original» |
| **Cita de Yann LeCun** | 12 | «La idea más interesante en machine learning en los últimos 20 años.» — Yann LeCun |
| **Goodfellow, 27 años, Montreal, junio 2014** | 12 | «Ian Goodfellow, 27 años, propone en una conversación de bar… Esa misma noche implementa el prototipo. Funciona en el primer intento.» |
| **4 fotos reales** | 18 | El dataset entero de TiltedTinder en Slanted Land. |
| **Score cara prototipo = 2; ruido = −0.5** | 23 | 1(+1)+0(−1)+0(−1)+1(+1)=2 · 0.25(+1)+1(−1)+0.5(−1)+0.75(+1)=−0.5 |
| **σ(1) ≈ 0.73** | 24, 26 | «Estoy un 73% seguro de que esto es real» |
| **σ(−0.5) = 0.37** | 26 | «Estoy solo un 37% seguro de que esto sea real» |
| **z = 0.7 → [[0.85, 0.15],[0.15, 0.85]]** | 28 | σ(1.7)=0.85, σ(−1.7)=0.15 *(los números están solo en la imagen `slide-28-1.jpg`, no en el texto de la slide)* |
| **D(G(z)) = 0.68** | 34, 35, 36 | El número que conecta ambos errores. |
| **Error_D = −ln(0.32) ≈ 1.14** | 34, 36 | Fórmula en la imagen `slide-36-1.png`. |
| **∂E/∂w para dos píxeles, α = 0.1** | 34 | 1 → 1.008 ↑ y −1 → −0.968 ↑ |
| **−ln(0.9) ≈ 0.1 · −ln(0.1) ≈ 2.3** | 30 | Los dos extremos del log-loss. |
| **w de 512 dimensiones** | 41 | «Mapping Network: transforma el ruido z en un vector de estilo w (512 dimensiones)» |
| **4×4 → 1024×1024, red de 8 capas** | 42 | Progressive growing + mapping network. |
| **+30% de precisión del clasificador** | 46 | «Una GAN entrenada con biopsias histológicas de tumores de mama generó imágenes indistinguibles de las reales para patólogos. Combinando datos reales y sintéticos, la precisión del clasificador mejoró un 30%.» |
| **Neurorradiólogos en estudios ciegos** | 43 | «GANs entrenadas con resonancias magnéticas generan imágenes de cerebro que neurorradiólogos no pueden distinguir de las reales en estudios ciegos.» |

**Ejemplos y casos nombrados:** ThisPersonDoesNotExist.com (43); MRI→CT como caso clínico estrella (5, 8, 44); síntesis histológica (4, 8, 46); artefactos de movimiento en MRI, biopsias con burbujas/pliegues, TC de dosis reducida (45); gatos vs. perros como ilustración del dataset homogéneo (47); DALL·E, Stable Diffusion, Midjourney como motores de difusión (6, 7); deepfakes (7).

**Las tres únicas fuentes citadas en todo el deck:**

1. Slide 15 — AWS, *¿Qué es una GAN?* → `https://aws.amazon.com/es/what-is/gan/`
2. Slide 18 — «Basado en el tutorial de Rowel Atienza» → `https://www.youtube.com/watch?v=8L11aMN5KY8&t=16s` **(atribución errónea, ver #1)**
3. Slide 37 — «A Friendly Introduction to Generative Adversarial Networks — Luis Serrano Academy»
4. Slide 42 — «GeeksforGeeks — StyleGAN: Style Generative Adversarial Networks»

## Inconsistencies / open questions

1. **Error de atribución confirmado — el video de Slanted Land.** La slide 18 dice «Basado en el tutorial de **Rowel Atienza**» y enlaza `https://www.youtube.com/watch?v=8L11aMN5KY8&t=16s`. Ese video es **A Friendly Introduction to Generative Adversarial Networks (GANs)** de **Luis Serrano**. La propia slide 37 acredita correctamente a Serrano («Fuente: A Friendly Introduction to Generative Adversarial Networks — Luis Serrano Academy») por el mismo material. Rowel Atienza es autor de *Advanced Deep Learning with Keras/TensorFlow 2*, un libro distinto y no relacionado con este tutorial. **El deck se contradice a sí mismo: dos atribuciones distintas para la misma fuente, a 19 slides de distancia.** El alcance del error es grande: **todas** las figuras de las slides 19–37 (`slide-19-1`, `20-1`, `21-1`, `22-1`, `23-1`, `24-1`, `25-2`, `26-1`, `26-2`, `27-1`, `28-1`, `31-1`, `31-2`, `32-4`, `35-1`, `36-2`, `37-3`) son capturas de pantalla del video de Serrano — 17 figuras cubiertas por una atribución errónea y una correcta.
2. **Contradicción de fecha en StyleGAN.** Slide 40 titula «El salto que lo cambió todo: **StyleGAN (2018)**»; slide 41 pone al pie «StyleGAN (**NVIDIA, 2019**)»; slide 42 dice «StyleGAN (NVIDIA)» sin fecha. El deck nunca resuelve cuál es. (StyleGAN se publicó en arXiv en diciembre de 2018 y se presentó en CVPR 2019 — ambas fechas son defendibles, pero el deck no lo explica.)
3. **Caption sin figura: la slide 41 promete caras y no muestra ninguna.** El texto de la slide 41 dice «Caras fotorrealistas generadas por StyleGAN (NVIDIA, 2019)», pero la única figura de la slide (`slide-41-2.jpg`) es el **diagrama de arquitectura de StyleGAN** en verde (mapping network de 8 FC, synthesis network con AdaIN, ProGan Discriminator, 1024×1024) — no hay caras. Lo mismo en la slide 43, «Fortaleza 1: Generación de imágenes realistas», cuyo argumento entero es «imágenes que el ojo humano no puede distinguir de las reales»: su única figura grande (`slide-43-1.png`) es una **ilustración decorativa de línea** de una cara estilizada. **El deck argumenta sobre fotorrealismo sin mostrar jamás una sola imagen fotorrealista generada.**
4. **Figura equivocada en la slide del Generador.** La slide 27 se titula «Construyendo el Generador — El objetivo opuesto» y su figura (`slide-27-1.png`) es la del **Discriminador**: el diagrama «Faces / Noise» con las etiquetas Big / small / any, visualmente idéntico al de la slide 22 (`slide-22-1.png`, md5 distinto pero mismo contenido). La slide que introduce el Generador no tiene ninguna figura del Generador.
5. **Cifras sin estudio detrás.** Cuatro afirmaciones cuantitativas o de peso clínico se presentan sin nombrar autor, publicación, año ni cohorte:
   - Dice **0.9524 vs 0.9459** (slide 5) — cuatro decimales, precisión que sugiere una tabla concreta de un paper concreto, nunca nombrado.
   - **«+30%»** de precisión del clasificador y «patólogos» que no distinguen biopsias sintéticas (slide 46).
   - **«neurorradiólogos no pueden distinguir… en estudios ciegos»** (slide 43).
   - **«70K+ citas del paper original»** (slide 12) — sin fecha de corte ni base bibliométrica.
6. **La cita de Yann LeCun va sin fuente** (slide 12): «La idea más interesante en machine learning en los últimos 20 años.» No hay referencia a dónde, cuándo ni en qué medio lo dijo.
7. **El deck no nombra ni un solo dataset.** Ni CelebA, ni FFHQ, ni ImageNet, ni MNIST, ni ningún dataset biomédico (BraTS, CAMELYON, TCGA…). Y sin embargo argumenta sobre datasets en **cuatro slides**: la 5 (escasez / privacidad / coste), la 46 (generar miles de imágenes sintéticas para ampliar el dataset), la 47 (entera dedicada a «el dataset importa», con la tabla gatos/perros), y la 50 (sesgo heredado del dataset). El consejo operativo de la slide 47 — «asegurate de que el dataset de entrenamiento esté limpio, bien etiquetado y sea homogéneo» — no viene acompañado de un solo ejemplo de dataset real.
8. **La slide 10 es un separador sin cuerpo.** Titulada «Generative Adversarial Networks (GANs)», dentro de la sección «INTRODUCCIÓN A LAS GANS», no tiene ningún contenido.
9. **Error_D / Error_G: el mismo símbolo para dos cosas distintas.** La imagen `slide-30-2.png` rotula **Error_G = −ln(1 − predicción)**. Nueve slides después, `slide-36-1.png` rotula exactamente la misma fórmula como **Error_D = −ln(1 − 0.68) = −ln(0.32) ≈ 1.14**, y el título de la slide 36 es «El error del **Discriminador**». Un alumno que compare ambas slides no puede saber de quién es ese error.
10. **Desajuste matemático en la slide 34.** La slide parte de «el error del Discriminador = 1.14», que proviene de E = −ln(1 − D(x)) (caso *queremos 0*), pero aplica la derivada **∂E/∂wᵢ = −[1 − D(x)] · xᵢ**, que la figura `slide-37-3.jpg` deriva explícitamente de **E = −ln(D(x))** (caso *queremos 1*). Las dos no se corresponden: la derivada mostrada no es la derivada del error que se acaba de calcular. Es el punto matemáticamente más frágil del bloque de Slanted Land.
11. **La slide 16 anuncia cuatro pasos y enumera cinco.** «Cuatro pasos que se repiten miles de veces» encabeza una lista de Paso 1 a Paso 5. La slide 51 refuerza el número correcto al hablar de «el ciclo de **cinco** pasos».
12. **La slide 6 anuncia tres eras y enumera cuatro.** «Tres eras, un campo en aceleración constante» encabeza cuatro bloques numerados (Estadística, GANs, Difusión, SAM).
13. **La slide 51 acredita un contenido que el deck nunca dio.** El resumen de cierre dice que aprendimos «**El juego minimax** como marco conceptual, log-loss y backpropagation». El juego minimax no aparece en ninguna de las 50 slides anteriores: ni el término, ni la fórmula min_G max_D, ni el concepto de equilibrio. Log-loss y backpropagation sí están cubiertos.
14. **Celda de tabla corrupta en la slide 23.** La segunda fila de la columna «Imagen de ruido» dice literalmente «Score < 1 → Falsa ✓Score > 1 → Real ✓» — dos veredictos colapsados en una sola celda.
15. **Prosa y figuras desalineadas en la slide 31.** Los dos bullets de encabezado van en el orden «🔍 Discriminador — imagen real» / «🎨 Generador — imagen falsa», y las imágenes siguen ese orden (`slide-31-1.png` = y = −ln(x); `slide-31-2.png` = y = −ln(1−x)), pero los dos párrafos explicativos aparecen **invertidos** respecto a ambos. Las figuras son correctas; el texto que las acompaña está cruzado.
16. **La slide 42 dice que StyleGAN mantiene «el Discriminador estándar»**, pero el diagrama de la slide 41 (`slide-41-2.jpg`) rotula ese componente como **«ProGan Discriminator»** — el discriminador de Progressive GAN, que no es exactamente «estándar». El deck no reconcilia ambas descripciones.
17. **Erratas dentro del diagrama de StyleGAN** (`slide-41-2.jpg`, figura de terceros): los bloques convolucionales dicen «**Conv (383)**» donde debería leerse *Conv 3×3*, y el segundo bloque de síntesis repite «Const (4X4X512)» donde correspondería la salida de la capa anterior. Son errores de la figura fuente, no del deck, pero se proyectan tal cual.
18. **La agenda de 5 bloques se repite verbatim cinco veces** (slides 2, 9, 17, 38, 48): 5 de 51 slides, casi el 10% del deck, son la misma diapositiva.
19. **Títulos ausentes en siete slides.** Las slides 14, 20, 22, 27, 31, 35 y 37 no tienen título en el placeholder correspondiente; su título real («Arquitectura de una GAN», «Los datos reales: caras con patrón», «Construyendo el Discriminador», «Construyendo el Generador», «Loss Function Visualmente», «El ciclo completo…», «Para los curiosos: la derivada del error») está dentro del cuerpo, en negrita.
20. **Las capturas del video llevan un artefacto de navegador.** En `slide-24-1.png`, `slide-26-1.jpg`, `slide-28-1.jpg`, `slide-36-2.jpg` y `slide-37-3.jpg` se ve, abajo al centro, el **icono de la extensión Google Translate** del navegador. Confirma que las figuras son capturas de pantalla del video hechas en un browser, no material licenciado ni exportado. En `slide-20-1.png` y `slide-21-1.jpg` además la última cuadrícula 2×2 aparece truncada / con artefactos de renderizado del propio frame capturado.
21. **Diez de las 72 colocaciones de imagen son marcos de tarjeta vacíos de plantilla** (ver *Images / diagrams*): el manifiesto los clasifica como `figura` por su tamaño, pero no contienen nada. Slides afectadas: 7, 14, 39 y 49.
22. **Cinco imágenes clasificadas como `icono` por el manifiesto son en realidad fórmulas** — el contenido matemático más importante del deck. Ver la nota de reclasificación en *Images / diagrams*.
23. **Mezcla de idiomas sin criterio.** La prosa es española; los diagramas de las slides 15, 19–37 y 41 están íntegramente en inglés (Generator, Discriminator, Fake Sample, Real Data, Faces, Noise, High error, Low error, Error plot, Prediction, Bias), y solo las fórmulas de las slides 25, 30, 36 y 37 fueron rehechas en español («Error_D = −ln(predicción)»). El deck no traduce ni glosa los términos de las figuras.
24. **La cifra de la slide 5 mezcla dos cosas.** El Dice score es una métrica de segmentación y la U-Net es una red de segmentación; la slide la presenta como evidencia del valor de la *generación* con GANs. El razonamiento es válido (aumentación sintética mejora un segmentador aguas abajo), pero la slide no lo explicita y salta de «lo que la IA Generativa hace posible» a una métrica de segmentación sin puente.
25. **Ningún paper se cita con referencia completa.** Las slides 39 y 42 nombran autores y años (Goodfellow et al. 2014, Mirza & Osindero 2014, Radford et al. 2015, Ledig et al. 2017), pero sin título, venue ni DOI. Las únicas URLs del deck son la de AWS (15) y la del video de YouTube (18).

## Images / diagrams

**Inventario:** 72 colocaciones · **64 imágenes únicas** por md5 · 29 SVG originales detrás de PNG vectorizados. Todos los bytes están en `AIG4B-Clase-8-GANs.md/images/`, incluido el `_manifest.json` original. Cada imagen se describe **una sola vez, en su `primera_aparicion`**; las repeticiones se anotan al final.

**Reclasificación respecto del manifiesto.** El `_manifest.json` clasifica por tamaño en EMU y **falla en las dos direcciones**. De las 30 `figura` únicas:

- **19 tienen contenido informativo real** — `slide-15-1`, `19-1`, `20-1`, `21-1`, `22-1`, `23-1`, `24-1`, `25-2`, `26-1`, `26-2`, `27-1`, `28-1`, `31-1`, `31-2`, `32-4`, `35-1`, `36-2`, `37-3`, `41-2`.
- **6 son ilustración decorativa sin texto** — `slide-01-1` (logo), `12-1`, `18-1`, `43-1`, `45-1`, `49-1`.
- **5 son marcos de tarjeta vacíos de la plantilla** — `slide-07-1`, `14-1`, `39-1`, `39-3`, `49-2` (10 colocaciones contando repeticiones).

Y en la dirección contraria, **5 imágenes marcadas como `icono` son fórmulas matemáticas** — tiras horizontales muy anchas y bajas (hasta 1141×31 px), que el criterio de tamaño confundió con separadores: `slide-25-1`, `30-1`, `30-2`, `36-1`, `37-1`. Llevan el contenido matemático que el markdown no transcribe.

---

### Fórmulas (clasificadas `icono` por el manifiesto — contenido crítico)

**`AIG4B-Clase-8-GANs.md/images/slide-25-1.png`**
Depiction: tira horizontal con la fórmula de la sigmoid en tipografía matemática gris.
Why it matters: es la definición formal de la función de activación del Discriminador; el texto de la slide 25 la describe en prosa pero nunca la escribe.
Transcribed text: `σ(x) = 1 / (1 + e⁻ˣ)`

**`AIG4B-Clase-8-GANs.md/images/slide-30-1.png`**
Depiction: tira horizontal, fórmula centrada.
Why it matters: define el caso «queremos que la predicción sea 1» del log-loss. El subíndice *D* es la fuente de la inconsistencia #9.
Transcribed text: `Error_D = −ln(predicción)`

**`AIG4B-Clase-8-GANs.md/images/slide-30-2.png`**
Depiction: tira horizontal, fórmula centrada.
Why it matters: define el caso «queremos que la predicción sea 0». Rotulada aquí como error del **Generador**, y como error del **Discriminador** nueve slides más tarde (`slide-36-1.png`).
Transcribed text: `Error_G = −ln(1 − predicción)`

**`AIG4B-Clase-8-GANs.md/images/slide-36-1.png`**
Depiction: tira horizontal con la evaluación numérica del log-loss.
Why it matters: es el número (1.14) del que parte el cálculo de backpropagation de la slide 34. Aparece solo en la imagen.
Transcribed text: `Error_D = −ln(1 − 0.68) = −ln(0.32) ≈ 1.14`

**`AIG4B-Clase-8-GANs.md/images/slide-37-1.png`**
Depiction: tira horizontal con la derivada del error respecto de un peso.
Why it matters: es la fórmula operativa que la tabla de la slide 34 aplica píxel por píxel. Núcleo del bloque «Para los curiosos».
Transcribed text: `∂E/∂wᵢ = −[1 − D(x)] xᵢ`

---

### Figuras con contenido real

**`AIG4B-Clase-8-GANs.md/images/slide-15-1.jpg`** (slide 15)
Depiction: diagrama de flujo de una Vanilla GAN sobre papel cuadriculado, estilo draw.io. A la izquierda un triángulo violeta rotulado «Random Z» alimenta una caja 3D amarilla «Generator»; de ella sale un documento «Fake Sample» hacia una caja 3D azul «Discriminator». Abajo, un cilindro verde «Real Data» envía un documento «Real Sample» al mismo Discriminator. La salida del Discriminator entra en un rombo «Real or Fake», del que salen dos flechas hacia dos documentos: «Generator Loss» (arriba) y «Discriminator Loss» (abajo). Dos flechas grises gruesas devuelven cada loss a su red respectiva.
Why it matters: es **el** diagrama de arquitectura del deck — la única representación completa del bucle adversarial, con las dos pérdidas separadas y sus caminos de retropropagación explícitos. Todo el bloque de Slanted Land es su instanciación numérica.
Transcribed text: `Random Z` · `Generator` · `Fake Sample` · `Real Data` · `Real Sample` · `Discriminator` · `Real or Fake` · `Generator Loss` · `Discriminator Loss`

**`AIG4B-Clase-8-GANs.md/images/slide-19-1.jpg`** (slide 19)
Depiction: tres paneles sobre fondo casi blanco. Izquierda: dos monigotes dibujados a mano, inclinados hacia adelante. Centro: un monitor de escritorio cuya pantalla está dividida en una cuadrícula de 2×2 celdas vacías. Derecha: un grafo de red neuronal — tres nodos oscuros a la izquierda, flechas convergiendo a un único nodo a la derecha.
Why it matters: establece de un golpe las tres simplificaciones del ejemplo — sujeto (personas inclinadas), representación (imagen de 4 píxeles) y modelo (red de una capa). Primer frame del video de Serrano usado en el deck.
Transcribed text: `Slanted people` · `2x2 screens` · `1-layer Neural network`

**`AIG4B-Clase-8-GANs.md/images/slide-20-1.png`** (slide 20)
Depiction: dos filas. Arriba, cuatro caras dibujadas a mano alzada, todas alargadas e inclinadas en distintos ángulos. Abajo, las cuatro cuadrículas 2×2 correspondientes en escala de grises: en cada una, las celdas superior-izquierda e inferior-derecha son oscuras y las otras dos claras. La cuarta cuadrícula aparece truncada por un artefacto de captura.
Why it matters: es el puente visual entre «cara inclinada» y «patrón diagonal en 4 números» — el momento en que la fábula se convierte en datos.
Transcribed text: sin texto.

**`AIG4B-Clase-8-GANs.md/images/slide-21-1.jpg`** (slide 21)
Depiction: arriba, una barra de gradiente de blanco a negro rotulada `0` y `1`. Debajo, dos filas de cuatro cuadrículas 2×2 con el valor numérico impreso en cada celda. Fila **Faces**: (0.75, 0 / 0, 0.75), (1, 0.25 / 0.25, 0.75), (1, 0 / 0, 1), (0.75, 0 / 0.25, 0.75). Fila **Noise**: (0.25, 0 / 1, 0.75), (0.25, 1 / 0.5, 0.75), (0.75, 0.5 / 0.75, 0), (1, 1 / 0, 0.75 — con artefacto de captura).
Why it matters: es el dataset completo del ejemplo, con los ocho ejemplares numéricos. La imagen de ruido (0.25, 1 / 0.5, 0.75) que aparece aquí es la que se usa en todos los cálculos posteriores (slides 23, 26, 34, 35, 36).
Transcribed text: `0` · `1` · `Faces` · `Noise` · `0.75` `0` `0.25` `0.5` `1`

**`AIG4B-Clase-8-GANs.md/images/slide-22-1.png`** (slide 22)
Depiction: dos cuadrículas 2×2 lado a lado. Izquierda, rotulada **Faces**, con valores (1, 0 / 0, 1); cuatro cajitas de colores apuntan a sus celdas con flechas curvas — rojas «Big» a la diagonal principal, azules «small» a la secundaria. Derecha, rotulada **Noise**, con valores (0.25, 1 / 0.5, 0.75) y cuatro cajitas verdes «any».
Why it matters: articula la intuición del Discriminador antes de cualquier número — «en las caras la diagonal principal es grande y la secundaria pequeña; en el ruido todo puede ser cualquier cosa».
Transcribed text: `Big` · `small` · `Faces` · `any` · `Noise` · `1` `0` `0.25` `0.5` `0.75`

**`AIG4B-Clase-8-GANs.md/images/slide-23-1.png`** (slide 23)
Depiction: la misma composición que `slide-22-1.png` pero con las cajitas reducidas a signos: rojas con `+` en la diagonal principal, azules con `−` en la secundaria, en **ambas** cuadrículas (Faces y Noise).
Why it matters: el paso de la intuición cualitativa (Big/small) al peso numérico (+1/−1). Muestra que los mismos pesos se aplican a cualquier imagen, sea cara o ruido — que es exactamente lo que permite comparar los dos scores.
Transcribed text: `+` · `−` · `Faces` · `Noise` · `1` `0` `0.25` `0.5` `0.75`

**`AIG4B-Clase-8-GANs.md/images/slide-24-1.png`** (slide 24)
Depiction: el Discriminador como grafo. A la izquierda la cuadrícula de la cara prototipo (1, 0 / 0, 1) en blanco y negro; cuatro flechas negras curvas llevan cada celda a uno de cuatro nodos grises apilados. De cada nodo sale una arista rotulada hacia un nodo de salida: rojas gruesas `+1` (primera y cuarta), azules finas `−1` (segunda y tercera). Abajo, un nodo `1` rotulado «Bias» conecta con una arista verde `−1`. Al pie, el icono de la extensión Google Translate.
Why it matters: primera representación del Discriminador como red neuronal con bias explícito. Es la figura de referencia para el cálculo σ(1) = 0.73.
Transcribed text: `1` `0` `0` `1` · `+1` `−1` `−1` `+1` · `Bias` `1` · `−1`

**`AIG4B-Clase-8-GANs.md/images/slide-25-2.jpg`** (slide 25)
Depiction: gráfica de la sigmoid — curva en S negra sobre ejes finos, con la fórmula a la izquierda y dos puntos azules marcados: uno en el eje x en `1`, otro en el eje y en `0.73`, unidos por líneas punteadas azules.
Why it matters: enlaza la definición de la función con el número concreto del ejemplo (σ(1)=0.73), que es el resultado que la slide 26 usa para el veredicto «73% seguro de que es real».
Transcribed text: `σ(x) = 1 / (1 + e⁻ˣ)` · `0.73` · `1`

**`AIG4B-Clase-8-GANs.md/images/slide-26-1.jpg`** (slide 26)
Depiction: la misma red del Discriminador que `slide-24-1.png` (entrada 1,0/0,1; pesos +1,−1,−1,+1; bias 1 con peso −1), ahora **con el resultado**: a la derecha del nodo de salida, en grande, `σ(1) = 0.73`. Arriba a la derecha, en miniatura, la gráfica de la sigmoid con los puntos 0.73 y 1 marcados.
Why it matters: es la figura del veredicto correcto sobre una imagen **real** — el «✓ clasifica correctamente como real» de la slide 26.
Transcribed text: `1` `0` `0` `1` · `+1` `−1` `−1` `+1` · `Bias` `1` `−1` · `σ(1) = 0.73` · `σ(x) = 1/(1+e⁻ˣ)` · `0.73` · `1`

**`AIG4B-Clase-8-GANs.md/images/slide-26-2.jpg`** (slide 26)
Depiction: la misma red, ahora con la cuadrícula de **ruido** (0.25, 1 / 0.5, 0.75) como entrada y los mismos pesos. A la derecha: `σ(-0.5) = 0.37`.
Why it matters: el par simétrico de la anterior — el veredicto correcto sobre una imagen **falsa**. Juntas cierran la demostración de que el Discriminador a mano funciona.
Transcribed text: `0.25` `1` `0.5` `0.75` · `+1` `−1` `−1` `+1` · `Bias` `1` `−1` · `σ(-0.5) = 0.37`

**`AIG4B-Clase-8-GANs.md/images/slide-27-1.png`** (slide 27)
Depiction: **la misma composición Faces/Noise con cajitas Big/small/any que `slide-22-1.png`** (md5 distinto, recorte y resolución distintos, contenido equivalente).
Why it matters: **figura fuera de lugar** — la slide se titula «Construyendo el Generador» y la figura es del Discriminador. Ver inconsistencia #4.
Transcribed text: `Big` · `small` · `Faces` · `any` · `Noise` · `1` `0` `0.25` `0.5` `0.75`

**`AIG4B-Clase-8-GANs.md/images/slide-28-1.jpg`** (slide 28)
Depiction: el Generador como grafo, rotulado «Generator» arriba a la izquierda. A la izquierda, una recta numérica de 0 a 1 con un punto verde en `0.7`, etiquetada `z`. De un nodo `z` y un nodo `1` («Bias») salen ocho aristas — rojas `+1` y azules `−1` — hacia cuatro nodos de salida, cada uno con su resultado: `σ(1.7) = 0.85`, `σ(-1.7) = 0.15`, `σ(-1.7) = 0.15`, `σ(1.7) = 0.85`. Cuatro flechas negras llevan esos valores a una cuadrícula 2×2 a la derecha: (0.85, 0.15 / 0.15, 0.85). Al pie, el icono de Google Translate.
Why it matters: es el momento de pago del ejemplo — un solo número z=0.7 produce una imagen con el patrón diagonal correcto. Los valores 0.85/0.15 y σ(±1.7) **solo existen en esta imagen**, no en el texto de la slide.
Transcribed text: `Generator` · `0.7` · `0` `1` · `z` · `+1` `−1` · `Bias` `1` · `σ(1.7) = 0.85` · `σ(-1.7) = 0.15` · `0.85` `0.15` `0.15` `0.85`

**`AIG4B-Clase-8-GANs.md/images/slide-31-1.png`** (slide 31)
Depiction: gráfica recortada en vertical de `y = −ln(x)` sobre el intervalo (0, 1]. Ejes rotulados de −1 a 1 en x y de 0 a 3 en y. Dos segmentos verticales marcan puntos sobre la curva: uno rojo cerca de x pequeño (altura ≈ 1.4) con la etiqueta «High error», uno verde cerca de x = 0.8 (altura baja) con la etiqueta «Low error».
Why it matters: hace visible por qué el log-loss castiga fuerte al Discriminador cuando le da score bajo a una imagen real — la curva se dispara al acercarse a 0.
Transcribed text: `y = −ln(x)` · `y` · `-1` `0` `1` · `1` `2` `3` · `High error` · `Low error`

**`AIG4B-Clase-8-GANs.md/images/slide-31-2.png`** (slide 31)
Depiction: gráfica recortada en vertical de `y = −ln(1 − x)`, espejo de la anterior: crece hacia la derecha. Segmento verde «Low error» a la izquierda (x pequeño), segmento rojo «High error» a la derecha (x cercano a 1).
Why it matters: el par simétrico — por qué el error se dispara cuando el Discriminador da score alto a una imagen falsa. Juntas explican la tensión adversarial en una sola imagen.
Transcribed text: `y = −ln(1 − x)` · `y` · `0` `1` · `1` `2` `3` · `Low error` · `High error`

**`AIG4B-Clase-8-GANs.md/images/slide-32-4.jpg`** (slide 32)
Depiction: red neuronal densa de tres capas con nodos azules; sobre cada arista hay una flecha roja gruesa apuntando hacia arriba o hacia abajo. A la derecha, arriba, una pequeña curva en U rotulada «Error plot»; debajo, en grande, la palabra «Prediction», y bajo ella «Error».
Why it matters: la representación de backpropagation como «cada peso sube o baja» — la traducción visual de ∂E/∂w para toda la red a la vez, sin fórmulas.
Transcribed text: `Error plot` · `Prediction` · `Error`

**`AIG4B-Clase-8-GANs.md/images/slide-35-1.jpg`** (slide 35)
Depiction: las dos redes juntas por primera vez. Izquierda: «Generator» en rojo — recta numérica con punto verde `z`, nodos `z` y `1` (Bias), aristas rojas hacia cuatro nodos `σ`. Centro: la cuadrícula generada (0.25, 1 / 0.5, 0.75). Derecha: «Discriminator» en azul — cuatro flechas negras llevan las celdas a cuatro nodos, más un nodo `1` (Bias), aristas azules convergiendo a un nodo `σ` cuya salida es `0.68`.
Why it matters: **la figura que cierra todo el bloque de Slanted Land** — el pipeline completo G → imagen → D → score en una sola vista, y el origen del número 0.68 del que dependen las slides 34, 35, 36 y 37.
Transcribed text: `Generator` · `z` · `0` `1` · `Bias` `1` · `σ` · `0.25` `1` `0.5` `0.75` · `Discriminator` · `0.68`

**`AIG4B-Clase-8-GANs.md/images/slide-36-2.jpg`** (slide 36)
Depiction: la misma composición que `slide-35-1.jpg`, con una anotación añadida en azul junto al nodo de salida: «Want 0 / Error = -ln(1-0.68)». Al pie, el icono de Google Translate.
Why it matters: superpone el objetivo (queremos 0) al resultado obtenido (0.68) sobre el mismo diagrama — la definición operativa del error del Discriminador en contexto.
Transcribed text: `Generator` · `Discriminator` · `z` · `Bias` `1` · `0.25` `1` `0.5` `0.75` · `0.68` · `Want 0` · `Error = -ln(1-0.68)`

**`AIG4B-Clase-8-GANs.md/images/slide-37-3.jpg`** (slide 37)
Depiction: la figura matemáticamente más densa del deck. Izquierda: el Discriminador como grafo, rotulado «Discriminator», con la cuadrícula (1, 0 / 0, 1), entradas `x₁`…`x₄` sobre flechas curvas negras, pesos `w₁`…`w₄` sobre aristas rojas, un nodo `σ` de salida y un nodo `1` («Bias») con arista azul rotulada `b`. Derecha: tres bloques de fórmulas bajo los encabezados «Prediction», «Loss function (error) from images» y «Derivatives», con la derivación completa por regla de la cadena en cuatro pasos, más la derivada respecto del bias al final. Al pie, el icono de Google Translate.
Why it matters: es la única derivación matemática completa del deck y la justificación de la fórmula que la slide 34 aplica. La slide la marca como opcional («para los curiosos»), pero es donde el resultado `∂E/∂wᵢ = −[1 − D(x)]xᵢ` deja de ser un dato y pasa a ser una consecuencia.
Transcribed text:
`Discriminator` · `x₁` `x₂` `x₃` `x₄` · `w₁` `w₂` `w₃` `w₄` · `b` · `Bias` `1` · `1` `0` `0` `1`
`Prediction` — `D(x) = σ(x₁w₁ + x₂w₂ + x₃w₃ + x₄w₄ + b)`
`Loss function (error) from images` — `E = −ln(D(x))`
`Derivatives` —
`∂E/∂wᵢ = ∂E/∂D · ∂D/∂wᵢ`
`= (−1/D(x)) · σ(Σⱼ₌₁⁴ xⱼwⱼ + b)[1 − σ(Σⱼ₌₁⁴ xⱼwⱼ + b)]xᵢ`
`= (−1/D(x)) · D(x)[1 − D(x)]xᵢ`
`= −[1 − D(x)]xᵢ`
`∂E/∂b = ∂E/∂D · ∂D/∂b = −[1 − D(x)]`

**`AIG4B-Clase-8-GANs.md/images/slide-41-2.jpg`** (slide 41)
Depiction: diagrama de arquitectura de StyleGAN en tonos verdes. Arriba, «Random Vector (Latent Code) {512 X 1}» entra en un bloque «Normalise» y de ahí a la **Mapping Network X**: una columna de ocho cajas «FC» apiladas que termina en `w ∈ W`. De `w` salen cuatro conectores rotulados `A` hacia la **Synthesis Network 'y'**: pila de bloques `Const (4X4X512)` → `Ada IN` → `Conv (383)` → `Ada IN` → `Upsample` → `Const (4X4X512)` → `Ada IN` → `Conv (383)` → `Ada IN` → `....` → `1024 X 1024`. Por la derecha entra «Noise» a través de cuatro conectores `B` que suman en los puntos ⊕. A la derecha, el «ProGan Discriminator» — una pila de barras rotulada `{1024 X 1024}` — recibe la salida por «Downscaling», y un bloque «Loss» cierra el lazo con una flecha punteada «Training». Todo el conjunto izquierdo está encuadrado y rotulado «Generator» en vertical.
Why it matters: es la única figura del deck que muestra dónde entra el estilo (A/AdaIN) y dónde el ruido (B) capa por capa — la sustancia de las tres innovaciones que las slides 40 y 42 enumeran en prosa. Estilo y paleta corresponden a la figura de GeeksforGeeks que la slide 42 cita. **Contradice el caption de su propia slide, que promete caras fotorrealistas.** Contiene además las erratas `Conv (383)` (por *Conv 3×3*) y el `Const (4X4X512)` repetido.
Transcribed text: `Random Vector (Latent Code) {512 X 1}` · `Normalise` · `Mapping Network X` · `FC` ×8 · `w ∈ W` · `Generator` · `Synthesis Network 'y'` · `Const (4X4X512)` · `Ada IN` · `Conv (383)` · `Upsample` · `A` · `B` · `Noise` · `....` · `1024 X 1024` · `ProGan Discriminator` · `{1024 X 1024}` · `Downscaling` · `Loss` · `Training`

---

### Ilustración decorativa (figuras sin contenido informativo)

**`AIG4B-Clase-8-GANs.md/images/slide-01-1.png`** (slide 1) — Logo institucional de la **Universidad Austral**: árbol estilizado con estrellas dentro de un óvalo con la leyenda latina, sobre el nombre en dos líneas. Es la única marca institucional del deck; el texto nunca nombra la universidad.
Transcribed text: `STVDIORVM · AVSTRALIS · VNIVERSITAS` · `UNIVERSIDAD AUSTRAL`

**`AIG4B-Clase-8-GANs.md/images/slide-12-1.png`** (slide 12) — Ilustración de línea roja sobre transparente: dos personas sentadas a una mesa con copas, y detrás un panel de presentación con una bombilla y una flecha ascendente. Ilustra la anécdota del bar de Montreal. Sin texto.

**`AIG4B-Clase-8-GANs.md/images/slide-18-1.png`** (slide 18) — Ilustración de línea roja: una colina curva con tres casas inclinadas arriba, cuatro monigotes inclinados en la ladera, dos nubes, un sol y dos árboles. Es la representación visual de Slanted Land. Sin texto.

**`AIG4B-Clase-8-GANs.md/images/slide-43-1.png`** (slide 43) — Retrato femenino de trazo continuo único en rojo terracota, estilo *one-line art*. Decorativo: ocupa el lugar donde la slide argumenta sobre caras fotorrealistas generadas. Sin texto.

**`AIG4B-Clase-8-GANs.md/images/slide-45-1.png`** (slide 45) — Ilustración de línea: cuadrado de esquinas redondeadas con una cruz médica dentro y una cruz fina superpuesta. Alude al inpainting médico. Sin texto.

**`AIG4B-Clase-8-GANs.md/images/slide-49-1.png`** (slide 49) — Dos curvas de trazo continuo, una granate y una salmón, con picos irregulares, sobre la palabra `INSTABILITY` en mayúsculas grises. Es la única figura del deck cuyo texto está en inglés dentro de una slide sobre limitaciones en español.
Transcribed text: `INSTABILITY`

---

### Marcos de tarjeta vacíos (clasificados `figura`, sin contenido)

Cinco imágenes únicas / **diez colocaciones**. Son elementos de la plantilla de diapositivas, no ilustraciones. Nada que transcribir.

| Archivo | Slide | Descripción | Colocaciones |
|---|---|---|---|
| `slide-07-1.png` | 7 | Marco rectangular blanco con borde gris fino y barra vertical roja a la izquierda. | 3 (`07-1`, `07-2`, `07-3`) |
| `slide-14-1.png` | 14 | Cuatro rectángulos rosa claro con esquina de bocadillo, dispuestos en cruz alrededor de un círculo rojo central. Diagrama de plantilla sin ninguna etiqueta. | 1 |
| `slide-39-1.png` | 39 | Marco de tarjeta horizontal: banda superior beige, cuerpo blanco, borde gris. | 2 (`39-1`, `39-2`) |
| `slide-39-3.png` | 39 | Igual que el anterior, proporción ligeramente distinta. | 2 (`39-3`, `39-4`) |
| `slide-49-2.png` | 49 | Marco cuadrado blanco con barra vertical roja a la izquierda. | 2 (`49-2`, `49-3`) |

---

### Iconos

29 iconos únicos genuinos (34 clasificados `icono` menos las 5 fórmulas reclasificadas arriba). Sin texto ninguno de ellos. Todos son pictogramas de línea de la biblioteca de la plantilla; 23 tienen SVG original en la carpeta compañera.

| Archivo | Slide | Icono |
|---|---|---|
| `slide-05-1.png` | 5 | Triángulo de advertencia con signo de exclamación (rojo) — *Escasez* |
| `slide-05-2.png` | 5 | Escudo con candado (rojo) — *Privacidad* |
| `slide-05-3.png` | 5 | Pila de monedas con símbolo `$` (rojo) — *Coste* |
| `slide-05-4.png` | 5 | Círculo azul con «i» de información |
| `slide-06-1.png` | 6 | Esquina de tarjeta / marcador granate |
| `slide-12-2.png` | 12 | Círculo verde con tilde de verificación |
| `slide-13-1.png` | 13 | Esquina de tarjeta / marcador granate |
| `slide-16-1.png` | 16 | Destellos / chispas — *Paso 1, el Generador produce* |
| `slide-16-2.png` | 16 | Ojo — *Paso 2, el Discriminador evalúa* |
| `slide-16-3.png` | 16 | Mazo de juez — *Paso 3, el veredicto* |
| `slide-16-4.png` | 16 | Cerebro — *Paso 4, ambos aprenden* |
| `slide-16-5.png` | 16 | Flecha en bucle / repetición — *Paso 5, el ciclo se repite* |
| `slide-18-2.png` | 18 | Esquina de tarjeta / marcador granate |
| `slide-29-1.png` | 29 | Círculo azul con «i» *(reutilizado en la slide 41)* |
| `slide-30-3.png` | 30 | Círculo azul con «i» |
| `slide-32-1.png` | 32 | Flecha recta roja hacia la derecha *(3 colocaciones en la slide 32)* |
| `slide-37-2.png` | 37 | Esquina de tarjeta granate, muy pequeña (13×10 px) |
| `slide-40-1.png` | 40 | Círculo azul con «i» |
| `slide-42-1.png` | 42 | Capas apiladas — *Progressive Growing* |
| `slide-42-2.png` | 42 | Marco de imagen con montaña y sol — *Bi-linear Sampling* |
| `slide-42-3.png` | 42 | Deslizadores / controles — *Mapping Network + AdaIN* |
| `slide-43-2.png` | 43 | Cara sonriente enmarcada — *ThisPersonDoesNotExist* |
| `slide-43-3.png` | 43 | Cerebro — *imágenes médicas sintéticas* |
| `slide-43-4.png` | 43 | Cámara de vídeo — *videojuegos y entretenimiento* |
| `slide-46-1.png` | 46 | Círculo verde con tilde |
| `slide-47-1.png` | 47 | Triángulo de advertencia amarillo |
| `slide-50-1.png` | 50 | Regla graduada — *dificultad para evaluar la calidad* |
| `slide-50-2.png` | 50 | Servidor / rack — *alta demanda computacional* |
| `slide-50-3.png` | 50 | Persona junto a una balanza — *sesgo heredado del dataset* |

---

### Repeticiones (8 colocaciones de imágenes ya descritas)

| Colocación | Slide | Primera aparición |
|---|---|---|
| `slide-07-2.png`, `slide-07-3.png` | 7 | `slide-07-1.png` |
| `slide-32-2.png`, `slide-32-3.png` | 32 | `slide-32-1.png` |
| `slide-39-2.png` | 39 | `slide-39-1.png` |
| `slide-39-4.png` | 39 | `slide-39-3.png` |
| `slide-41-1.png` | 41 | `slide-29-1.png` *(el círculo azul «i» de la slide 29, reutilizado 12 slides después)* |
| `slide-49-3.png` | 49 | `slide-49-2.png` |

### Créditos y URLs embebidos dentro de figuras

**Ninguno.** Se revisaron las 19 figuras con contenido real, incluyendo recortes ampliados de las zonas de marca de agua (bordes y pie de imagen). No hay una sola firma, watermark, URL ni línea de crédito dentro de ninguna imagen del deck.

La única marca recurrente encontrada al pie de `slide-24-1.png`, `slide-26-1.jpg`, `slide-28-1.jpg`, `slide-36-2.jpg` y `slide-37-3.jpg` es el **icono de la extensión Google Translate del navegador** — un artefacto de captura de pantalla, no un crédito.

Esto es relevante para el problema de atribución: **las 17 figuras tomadas del video de Luis Serrano no llevan ninguna marca que identifique su origen**. La atribución existe solo en el texto de dos slides, y esas dos slides se contradicen (18 = Rowel Atienza, 37 = Luis Serrano). Nada dentro de las imágenes permite resolver la discrepancia — y presumiblemente por eso pasó inadvertida.

## Raw / preserved excerpts

### El desarrollo completo de Slanted Land (slides 17–37), verbatim

> **Slide 18 — El Problema: ¡Bienvenidos a Slanted Land! 🌀**
>
> Imagina un mundo peculiar llamado Slanted Land, donde absolutamente todo se inclina: los árboles, las casas, las personas e incluso la pizza que comen los gatos. En este universo, la norma es la inclinación.
>
> Los habitantes de Slanted Land solo conocen rostros con una ligera inclinación. Para ellos, un rostro completamente recto sería una anomalía, algo totalmente extraño e incomprensible.
>
> El problema urgente: la app de citas de Slanted Land, TiltedTinder, necesita generar fotos de perfil para sus usuarios. Pero solo tienen 4 fotos reales en toda su base de datos. Con tan pocos datos, nadie encuentra pareja. ¡La supervivencia romántica de toda una civilización inclinada depende de nuestra GAN! 💘
>
> | Universo Inclinado | Rostros "Normales" |
> |---|---|
> | Todo, desde la gravedad hasta las cejas de sus habitantes, está en un ángulo distintivo. | Solo existen los rostros inclinados; un rostro recto les resulta completamente alienígena. |
>
> [Basado en el tutorial de Rowel Atienza — ver video:](https://www.youtube.com/watch?v=8L11aMN5KY8&t=16s)

> **Slide 19 — El mundo de Slanted Land**
>
> | Imágenes 2×2 píxeles | Dataset real | Red de una sola capa |
> |---|---|---|
> | Cada imagen se representa como una pantalla con 4 celdas — cada celda tiene un valor entre 0 (blanco) y 1 (negro). | Son imágenes de personas inclinadas. El Generador va a aprender a producir imágenes que se parezcan a esas personas. | La arquitectura más simple posible — ideal para entender los fundamentos sin complejidad adicional. |

> **Slide 20 — Los datos reales: caras con patrón**
>
> Las "caras" de Slanted Land, codificadas como píxeles, tienen un patrón consistente:
>
> - Esquinas oscuras en la diagonal principal (arriba-izquierda y abajo-derecha): valor alto
> - Esquinas claras en la diagonal secundaria (arriba-derecha y abajo-izquierda): valor bajo
>
> Ese patrón diagonal es la "firma" de una cara real. El Discriminador tiene que aprenderlo para poder distinguirla del ruido.

> **Slide 21 — Caras vs. ruido: los dos tipos de imágenes**
>
> | Caras (imágenes reales) | Ruido (imágenes falsas) |
> |---|---|
> | Valores altos en la diagonal principal, bajos en la secundaria. Patrón estructurado y reconocible. | Valores sin patrón, distribuidos aleatoriamente. Sin estructura diagonal. El Discriminador debe aprender a distinguirlos a partir de esos valores numéricos. |

> **Slide 22 — Construyendo el Discriminador / ¿qué píxeles importan?**
>
> El Discriminador aprende que en las caras de Slanted Land:
>
> - Los píxeles de la diagonal principal son grandes → reciben peso positivo (+1)
> - Los píxeles de la diagonal secundaria son pequeños → reciben peso negativo (−1)
>
> Asigna estos pesos a cada posición: +1 para las que caracterizan una cara, −1 para las que no la caracterizan.

> **Slide 23 — Construyendo el Discriminador / Calculo del Score**
>
> El score de una imagen = suma ponderada de sus valores de píxel × pesos aprendidos:
>
> | Cara prototipo | Imagen de ruido |
> |---|---|
> | 1×(+1) + 0×(−1) + 0×(−1) + 1×(+1) = 2 | 0.25×(+1) + 1×(−1) + 0.5×(−1) + 0.75×(+1) = −0.5 |
> | Score > 1 → Real ✓ | Score < 1 → Falsa ✓Score > 1 → Real ✓ |

> **Slide 24 — Discriminador Como red neuronal**
>
> Para la cara prototipo: σ(1×(+1) + 0×(−1) + 0×(−1) + 1×(+1) − 1) = σ(1)
>
> | Entradas (z) | Pesos (w) | Bias |
> |---|---|---|
> | z₁=1, z₂=0, z₃=0, z₄=1 | w₁=+1, w₂=−1, w₃=−1, w₄=+1 | valor fijo = 1, peso = −1 |
>
> | Suma ponderada | Sigmoid |
> |---|---|
> | 1(+1)+0(−1)+0(−1)+1(+1)+1(−1) = 1 | σ(1) ≈ 0.73 → imagen real |

> **Slide 25 — Función Sigmoid: la activación del Discriminador**
>
> La función sigmoid convierte cualquier número real en una probabilidad entre 0 y 1. Es la función de activación que usa el Discriminador para emitir su veredicto.
>
> [imagen: σ(x) = 1 / (1 + e⁻ˣ)]
>
> | Rango acotado | Diferenciable | Monótona creciente | Punto medio en 0 |
> |---|---|---|---|
> | Devuelve valores entre 0 y 1; se lee como probabilidad. | Es suave en todo punto; permite backpropagation. | Si sube la entrada, sube la salida; conserva el orden. | σ(0) = 0.5; umbral natural de decisión. |

> **Slide 26 — Pongamos todo junto del Discriminador**
>
> Cuando la cara prototipo pasa por la red completa:
> σ(1) = 0.73 → "Estoy un 73% seguro de que esto es real"
> Como 0.73 > 0.5, clasifica correctamente la imagen como real ✓
>
> Cuando la imagen de ruido pasa por la misma red:
> σ(-0.5) = 0.37 → "Estoy solo un 37% seguro de que esto sea real"
> Como 0.37 < 0.5, clasifica correctamente la imagen como falsa ✓

> **Slide 27 — Construyendo el Generador / El objetivo opuesto**
>
> El Generador recibe un número aleatorio z (entre 0 y 1 — el "ruido latente") y tiene que producir una imagen de 2×2 píxeles. Su objetivo: producir imágenes que el Discriminador clasifique como reales (output cercano a 1).
>
> La estructura es la inversa del Discriminador: de 1 número → 4 píxeles. En redes reales, esto se implementa con capas de upsampling y convoluciones transpuestas.

> **Slide 28 — Construyendo el Generador / El Generador en acción: z = 0.7 → imagen**
>
> Con z = 0.7 como entrada y los pesos aprendidos, el Generador produce una imagen que reproduce el patrón diagonal de las caras reales. El Generador aprendió a engañar al Discriminador.
>
> El resultado muestra el patrón diagonal característico de las caras de Slanted Land: valores altos en la diagonal principal, bajos en la secundaria. El Generador internalizó la estructura del dataset real.
>
> [imagen `slide-28-1.jpg`: σ(1.7) = 0.85 · σ(-1.7) = 0.15 · σ(-1.7) = 0.15 · σ(1.7) = 0.85 → cuadrícula (0.85, 0.15 / 0.15, 0.85)]

> **Slide 29 — Proceso de Entrenamiento**
>
> En los slides anteriores definimos los pesos del Discriminador y el Generador a mano (+1, −1, Bias). En la práctica, la red debe aprender esos pesos sola. Para eso necesitamos una forma de medir cuánto se equivocó — esa es la función de error.
>
> Para que ambas redes aprendan, necesitamos medir exactamente cuánto se equivocaron. La función que hace eso en las GANs se llama log-loss (binary cross-entropy):
>
> | Cuando queremos que la predicción sea 1 | Cuando queremos que la predicción sea 0 |
> |---|---|
> | Error = −ln(predicción)<br>Se usa cuando la imagen es real y el Discriminador debe acercarse a 1. | Error = −ln(1 − predicción)<br>Se usa cuando la imagen es falsa y el Discriminador debe acercarse a 0. |
>
> La propiedad clave: el error es grande cuando la predicción está lejos del objetivo, y pequeño cuando está cerca. Esto guía el aprendizaje en la dirección correcta.

> **Slide 30 — Log-loss: los dos casos**
>
> [imagen `slide-30-1.png`: Error_D = −ln(predicción)]
> [imagen `slide-30-2.png`: Error_G = −ln(1 − predicción)]
>
> | Label = 1 — Imagen Real | Label = 0 — Imagen Falsa |
> |---|---|
> | 🔍 Discriminador entrenando con imagen real. Debe acercarse a 1.<br>✅ Predicción = 0.9 → −ln(0.9) ≈ 0.1 → Error pequeño<br>❌ Predicción = 0.1 → −ln(0.1) ≈ 2.3 → Error enorme | 🎨 Generador entrenando: el Discriminador debe acercarse a 0 (detectar la imagen como falsa).<br>✅ Predicción = 0.1 → −ln(0.9) ≈ 0.1 → Error pequeño<br>❌ Predicción = 0.9 → −ln(0.1) ≈ 2.3 → Error enorme |
>
> La propiedad clave: el error es grande cuando la predicción está lejos del objetivo, y pequeño cuando está cerca. Esto guía el aprendizaje en la dirección correcta.

> **Slide 31 — Loss Function Visualmente**
>
> 🔍 Discriminador — imagen real
> 🎨 Generador — imagen falsa
>
> [imagen `slide-31-1.png`: y = −ln(x), High error / Low error]
> [imagen `slide-31-2.png`: y = −ln(1 − x), Low error / High error]
>
> Predicción = 0 (imagen falsa). Error = −ln(1−predicción). Predicción alta → alto error. El Generador quiere que el Discriminador le asigne score alto (cercano a 1) — lo opuesto al objetivo del Discriminador.
>
> Predicción = 1 (imagen real). Error = −ln(predicción). Predicción baja → alto error. Predicción alta → bajo error. El Discriminador quiere acercarse a 1 cuando ve imágenes reales.

> **Slide 32 — Backpropagation: del error al ajuste de pesos**
>
> Una vez calculado el error, la red lo "propaga hacia atrás" para ajustar cada peso:
>
> - Pesos con alta contribución al error → se ajustan más
> - Pesos con baja contribución al error → se ajustan poco
> - La dirección del ajuste apunta siempre a reducir el error
>
> Este proceso ocurre simultáneamente en el Generador y el Discriminador en cada iteración.

> **Slide 33 — Backpropagation: el procedimiento paso a paso**
>
> | 01 | 02 | 03 |
> |---|---|---|
> | Calcular el error | Derivar la sensibilidad de cada peso | Actualizar en la dirección opuesta al gradiente |
>
> La función log-loss da un número que mide qué tan lejos estuvo la red de la respuesta correcta.
>
> Con la regla de la cadena se calcula ∂E/∂w para cada peso: si subo este peso un poco, ¿el error sube o baja?
>
> w_nuevo = w_actual − α · (∂E/∂w) — α (learning rate) controla el tamaño del paso.
>
> 04 — Repetir para todos los pesos, en ambas redes
>
> El cálculo se ejecuta para cada peso del Discriminador y del Generador de forma simultánea.

> **Slide 34 — Backpropagation: ejemplo con Slanted Land**
>
> Con el error del Discriminador = 1.14 y output D(G(z)) = 0.68, calculamos el ajuste concreto usando la derivada ∂E/∂wᵢ = −[1 − D(x)] · xᵢ:
>
> | Píxel | Valor xᵢ | ∂E/∂w | α = 0.1 | w_nuevo |
> |---|---|---|---|---|
> | Arriba-izq (diagonal) | 0.25 | −0.32 × 0.25 = −0.08 | −0.1 × (−0.08) | 1 + 0.008 = 1.008 ↑ |
> | Arriba-der | 1.00 | −0.32 × 1.00 = −0.32 | −0.1 × (−0.32) | −1 + 0.032 = −0.968 ↑ |
>
> Los pesos se mueven en la dirección que hace al Discriminador más exigente: en la próxima iteración dará un score más bajo a imágenes similares.

> **Slide 35 — El ciclo completo: Generador y Discriminador juntos**
>
> Con z = 0.7, el Generador produce una imagen → el Discriminador la evalúa → output: 0.68. Este único número conecta los dos errores:
>
> | Error del Discriminador | Error del Generador |
> |---|---|
> | Recibió 0.68 cuando quería dar 0 → se equivocó. Debe ajustar sus pesos para detectar mejor. | Recibió 0.68 cuando quería que diera 1 → casi lo engañó, pero no del todo. Debe ajustar para engañar más. |

> **Slide 36 — El error del Discriminador**
>
> El Discriminador recibió una imagen falsa pero le asignó un score de 0.68 (quería dar 0):
>
> [imagen `slide-36-1.png`: Error_D = −ln(1 − 0.68) = −ln(0.32) ≈ 1.14]
>
> Un error considerable. El Discriminador va a ajustar sus pesos para clasificar mejor estas imágenes en la próxima iteración — volviéndose más exigente y difícil de engañar.

> **Slide 37 — Para los curiosos: la derivada del error**
>
> La derivada del error del Discriminador respecto a sus pesos permite calcular exactamente cuánto ajustar cada uno:
>
> [imagen `slide-37-1.png`: ∂E/∂wᵢ = −[1 − D(x)] xᵢ]
>
> Este cálculo es lo que backpropagation ejecuta automáticamente en cada iteración, para todas las capas y todos los pesos de la red. La regla de la cadena lo hace computacionalmente eficiente incluso con millones de parámetros.
>
> Slide opcional — para quien quiera profundizar en la matemática. Fuente: A Friendly Introduction to Generative Adversarial Networks — Luis Serrano Academy.

### Las fórmulas de la slide 37, verbatim desde las imágenes

De `slide-37-1.png` (la fórmula que la slide muestra en el cuerpo):

```
∂E/∂wᵢ = −[1 − D(x)] xᵢ
```

De `slide-37-3.jpg` (la derivación completa, en la figura grande — **este texto no existe en el markdown del deck**):

```
Discriminator

Prediction
    D(x) = σ(x₁w₁ + x₂w₂ + x₃w₃ + x₄w₄ + b)

Loss function (error) from images
    E = − ln(D(x))

Derivatives

    ∂E        ∂E     ∂D
    ───  =   ───  ·  ───
    ∂wᵢ       ∂D     ∂wᵢ

           −1          4                   4
       = ─────  ·  σ(  Σ  xⱼwⱼ + b )[1 − σ( Σ  xⱼwⱼ + b )] xᵢ
          D(x)        j=1                 j=1

           −1
       = ─────  ·  D(x)[1 − D(x)] xᵢ
          D(x)

       = − [1 − D(x)] xᵢ


    ∂E       ∂E     ∂D
    ──   =  ───  ·  ──   =  − [1 − D(x)]
    ∂b       ∂D     ∂b
```

Entradas y pesos rotulados en el grafo de esa misma figura: `x₁`, `x₂`, `x₃`, `x₄` sobre las flechas de entrada; `w₁`, `w₂`, `w₃`, `w₄` sobre las aristas rojas; `b` sobre la arista azul del nodo `Bias` con valor `1`; cuadrícula de entrada `(1, 0 / 0, 1)`; nodo de salida `σ`.

### Otras fórmulas del deck, verbatim desde las imágenes

```
slide-25-1.png    σ(x) = 1 / (1 + e⁻ˣ)
slide-30-1.png    Error_D = − ln(predicción)
slide-30-2.png    Error_G = − ln(1 − predicción)
slide-36-1.png    Error_D = − ln(1 − 0.68) = − ln(0.32) ≈ 1.14
```

### Las cuatro atribuciones del deck, verbatim

```
Slide 15   <!-- enlace de la forma: https://aws.amazon.com/es/what-is/gan/ -->
           **[¿Qué es una GAN? - Explicación sobre las redes generativas antagónicas - AWS](https://aws.amazon.com/es/what-is/gan/)**

Slide 18   <!-- enlace de la forma: https://www.youtube.com/watch?v=8L11aMN5KY8&t=16s -->
           - [Basado en el tutorial de Rowel Atienza — ver video:](https://www.youtube.com/watch?v=8L11aMN5KY8&t=16s)

Slide 37   - Slide opcional — para quien quiera profundizar en la matemática.
             Fuente: A Friendly Introduction to Generative Adversarial Networks — Luis Serrano Academy.

Slide 42   - Fuente: GeeksforGeeks — StyleGAN: Style Generative Adversarial Networks
```
