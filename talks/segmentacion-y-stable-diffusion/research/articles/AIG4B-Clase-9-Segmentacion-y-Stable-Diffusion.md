## Slide 1 — Inteligencia Artificial Generativa Aplicada en Biomedicina

**Clase 9: Segmentación y Stable Diffusion**

- **Autor: Marco Sanchez Sorondo**
- **Última modificación: Abril 2026**

---

## Slide 2 — Tabla de contenidos

| 01 | 02 | 03 |
|---|---|---|
| Segmentación: qué es y dónde aparece | Un modelo básico → UNET | Generación condicionada por texto |

| 04 | 05 |
|---|---|
| Stable Diffusion | TilTedTinder v2, Notebook y Cierre |

---

## Slide 3 — Segmentación: qué es y dónde aparece

*Sección: SECCIÓN 1*

---

## Slide 4 — ¿Qué es segmentar?

- En visión por computadora, hay tres preguntas distintas que podemos hacerle a una imagen — y segmentar es la más fina de todas.

| Tarea | Pregunta | Salida |
|---|---|---|
| Clasificación | ¿Qué hay en esta imagen? | Una etiqueta (ej: "perro") |
| Detección | ¿Dónde está y qué es? | Cajas con etiquetas |
| Segmentación | ¿Qué representa cada píxel? | Una etiqueta por píxel — una "máscara" |

- Frase clave: segmentar es darle un significado pixel por pixel a la imagen.

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-04-1.jpg)

---

## Slide 5 — Tipos de segmentación

- Tres niveles de granularidad, según qué tan finamente queramos diferenciar lo que vemos:

- Semántica: etiqueta cada píxel con su clase, sin distinguir individuos. Todos los píxeles de "auto" reciben la misma etiqueta, aunque haya cinco autos.
- De instancias: distingue cada objeto individual. "Auto 1", "auto 2", "auto 3"... aunque sean de la misma clase.
- Panóptica: combina ambas — clasifica cada píxel y distingue instancias. Es la versión más completa.

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-05-1.jpg)

---

## Slide 6 — Aplicaciones genéricas

- **La segmentación es uno de los pilares de la visión moderna. Algunos casos donde ya está corriendo en producción:**

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-06-1.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-06-1.svg -->

**Autos autónomos**

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-06-2.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-06-2.svg -->

**Imagen satelital**

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-06-3.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-06-3.svg -->

**Videoconferencia (Zoom, Meet)**

- **Separar carretera, peatones, semáforos, otros vehículos.**

- **Medir cobertura forestal, urbanización, cuerpos de agua.**

- **Separar persona del fondo en tiempo real.**

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-06-4.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-06-4.svg -->

**Agricultura de precisión**

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-06-5.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-06-5.svg -->

**Edición de fotos**

- **"Seleccionar sujeto" automático en Photoshop.**

- **Detectar zonas con plagas o estrés hídrico.**

---

## Slide 7 — Aplicaciones en medicina

- En biomedicina, segmentar suele ser el paso clínico, no un paso intermedio. La máscara final es la respuesta:

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-07-2.jpg)

- Neuroimagen (MRI cerebro y en general): delinear tumores, lesiones de esclerosis múltiple, hipocampo.
- Oncología (CT/PET): medir volumen tumoral para planificar radioterapia.
- Cardiología: delimitar ventrículos para calcular fracción de eyección.
- Patología digital: contar y delimitar células, núcleos, mitosis.
- Oftalmología: segmentar vasos retinianos (diabetes, hipertensión).
- Dermatología: delimitar lesiones para seguimiento y biopsia guiada.

- Punto importante: la máscara es lo que se mide, se documenta y se compara entre estudios.

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-07-1.png)

---

## Slide 8 — Aplicaciones en medicina

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-08-1.jpg)

---

## Slide 9 — Cómo se ve una salida

- **Visualización típica: Imagen original (MRI) → Máscara binaria del tumor (blanco = tumor, negro = no tumor) → Overlay (máscara coloreada superpuesta sobre la imagen).**
- **Punto técnico: internamente, la máscara es una matriz del mismo tamaño que la imagen, donde cada celda dice a qué clase pertenece ese píxel. Para 2 clases es 0/1; para N clases es 0..N-1.**

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-09-1.jpg)

---

## Slide 10 — Un modelo básico → UNET

*Sección: SECCIÓN 2*

---

## Slide 11 — La intuición: clasificar cada píxel

- **Si segmentar es asignar una etiqueta a cada píxel, la idea más directa es: tratá cada píxel como un mini-problema de clasificación.**
- **Recordemos: ya sabemos clasificar imágenes. Una CNN clásica recibe una imagen y devuelve una etiqueta. Para llegar a esa única etiqueta, va comprimiendo la imagen con convoluciones + pooling, hasta que al final una capa densa entrega la clase.**
- **Idea de FCN (Fully Convolutional Network — Long et al., 2015): sacar la capa densa final y reemplazarla por más capas convolucionales que produzcan una salida espacial del mismo tamaño que la entrada — un mapa donde cada celda es la clase de ese píxel.**

- **Una sola frase: "convertí un clasificador de imágenes en un clasificador de píxeles".**

---

## Slide 12 — FCN: cómo se ve por dentro

- Tres pasos conceptuales:

**1**

- Encoder convolucional

**2**

- Reemplazo de la capa densa por convoluciones 1×1

**3**

- Upsampling

- La imagen entra y se va comprimiendo capa a capa — cada capa "ve" patrones más abstractos (bordes → texturas → estructuras → objetos).

- Ese mapa pequeño se "estira" hasta el tamaño original con convoluciones traspuestas (la operación inversa al pooling).

- En lugar de aplastar todo a un vector, se mantienen las dimensiones espaciales. La salida es un mapa de baja resolución con probabilidades por clase.

- Resultado: una máscara con una etiqueta por píxel. Funciona — y fue el primer modelo de segmentación end-to-end con deep learning.

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-12-1.jpg)

---

## Slide 13 — El problema de FCN

- **FCN funciona, pero tiene una limitación seria que se ve en las máscaras que produce:**

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-13-1.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-13-1.svg -->

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-13-2.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-13-2.svg -->

| El problema | Síntoma visual |
|---|---|
| Durante el encoder, la red comprime mucho — una imagen de 512×512 puede terminar como un mapa de 16×16. Cuando hacemos upsampling para volver al tamaño original, la información espacial fina ya se perdió. | Los contornos quedan borrosos o redondeados. Detalles finos — el borde exacto de un tumor, el contorno de un núcleo celular — desaparecen. |

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-13-3.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-13-3.svg -->

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-13-4.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-13-4.svg -->

| Por qué importa en medicina | La pregunta |
|---|---|
| Si estás midiendo el volumen de un tumor para decidir radioterapia, un borde 2 píxeles más adentro o más afuera cambia el cálculo y puede cambiar la decisión clínica. | ¿Cómo recuperamos los detalles finos que el encoder se llevó? |

---

## Slide 14 — UNET: nacida en biomedicina

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-14-1.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-14-1.svg -->

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-14-2.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-14-2.svg -->

| Origen | Contexto |
|---|---|
| Olaf Ronneberger, Philipp Fischer, Thomas Brox — Universidad de Friburgo, 2015. Paper original: "U-Net: Convolutional Networks for Biomedical Image Segmentation". | La primera versión se diseñó específicamente para segmentar células en microscopía electrónica, en un challenge donde había muy pocas imágenes etiquetadas — el clásico problema biomédico. |

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-14-3.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-14-3.svg -->

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-14-4.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-14-4.svg -->

| El truco | Dato |
|---|---|
| Una arquitectura simétrica — un encoder que comprime + un decoder que reconstruye — conectados por atajos que evitan la pérdida de detalle. | Es uno de los papers más citados de la última década en visión por computadora. Diez años después sigue siendo la base por defecto para segmentación médica. |

---

## Slide 15

**La arquitectura en U**

- La forma en U no es decoración — describe literalmente cómo fluyen los datos:

- Rama izquierda — Encoder (camino contractivo)

- Punto inferior — Bottleneck

- Rama derecha — Decoder (camino expansivo)

- La representación más comprimida y abstracta. Acá vive la información semántica de alto nivel.

- La imagen baja por convoluciones + max pooling.
- En cada nivel, las dimensiones espaciales se reducen a la mitad y los canales se duplican.
- "Qué hay" se entiende cada vez mejor; "dónde está" se pierde.

- La representación sube por convoluciones traspuestas (upsampling aprendido).
- En cada nivel, las dimensiones espaciales se duplican y los canales se reducen a la mitad.
- "Dónde" se reconstruye progresivamente.

- Salida: una máscara del mismo tamaño que la entrada, con una clase por píxel.

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-15-1.jpg)

---

## Slide 16 — La clave: skip connections

- Sin esto, UNET sería un FCN más elegante. Las skip connections son la innovación que cambia todo.
- Qué hacen: cada nivel del encoder tiene una conexión directa horizontal al nivel correspondiente del decoder. La salida del encoder en ese nivel se concatena con la entrada del decoder en el mismo nivel.
- Por qué resuelve el problema de FCN:

- El decoder recibe dos fuentes de información en cada nivel: la representación abstracta que sube desde el bottleneck (qué es) + la representación detallada del encoder al mismo nivel (dónde está, exactamente).
- Los detalles finos que el encoder vio antes de comprimir no se pierden — viajan por el atajo y se recuperan en el decoder.

- Resultado: contornos precisos, no borrosos. Esto es lo que hace que UNET sirva para uso clínico real.

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-16-1.jpg)

---

## Slide 17 — Por qué funciona tan bien en medicina

- **UNET se volvió el estándar de facto en imagen médica por tres razones que se alinean con las restricciones de la disciplina:**

**Funciona con pocos datos**

**Contornos precisos**

**Es modular y adaptable**

- **Los detalles finos sobreviven el viaje por la U. En medicina, el borde es el dato.**

- **Las skip connections actúan como un regularizador estructural. UNET puede entrenarse con cientos de imágenes — no miles — y aún así generalizar bien. Crítico cuando etiquetar requiere un radiólogo.**

- **La misma arquitectura funciona para MRI cerebro, células de patología, retina, ecografía cardíaca... cambia el dataset, no la red.**

---

## Slide 18 — SAM: ¿qué hace y por qué fue revolucionario?

- Si UNET es el modelo artesanal — chico, especializado, entrenado para una tarea concreta — SAM (Segment Anything Model, Meta, 2023) es el opuesto: un foundation model masivo que segmenta cualquier cosa en cualquier imagen, sin reentrenamiento.
- Lo que hace: recibe una imagen + una pista (un click, una caja, una máscara aproximada o, desde SAM 3, texto) y devuelve la máscara del objeto que querés. Cero entrenamiento previo sobre tu dominio.
- La idea nueva: segmentación promptable. SAM trajo al mundo de la segmentación el paradigma "foundation model + prompt en inferencia" que ya había explotado en NLP con los LLMs.
- Una frase para llevarse: SAM no aprende una tarea — aprende qué es un objeto, y deja que vos le digas cuál querés.

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-18-1.jpg)

---

## Slide 19

**SAM: ¿qué hace y por qué fue revolucionario?**

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-19-1.jpg)

---

## Slide 20 — SAM: mejoras conceptuales internas

- La arquitectura de SAM tiene dos ideas elegantes que explican su impacto:

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-20-1.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-20-1.svg -->

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-20-2.png)
<!-- original vectorial: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-20-2.svg -->

| Idea 1 — Separar lo caro de lo barato. | Idea 2 — El dataset SA-1B. |
|---|---|
| SAM divide el problema en tres componentes con costos muy distintos: | Meta construyó el dataset más grande de la historia de la segmentación: 1.000 millones de máscaras sobre 11 millones de imágenes. Lo armaron con un data engine iterativo donde el propio SAM ayudaba a anotar más datos, mejorando ronda tras ronda. Sin SA-1B, SAM no funcionaría — el secreto está tanto en el modelo como en los datos. |

- Image Encoder (ViT, masivo): procesa la imagen una vez y produce un embedding rico. Es el ~95% del cómputo.
- Prompt Encoder (liviano): convierte el prompt (punto, caja, texto) en un embedding compatible.
- Mask Decoder (liviano): combina los dos embeddings y produce la máscara.

- El truco: la imagen se codifica una sola vez. Después podés probar decenas de prompts distintos sobre esa misma imagen casi gratis — solo se reejecuta el decoder. Esto es lo que hace que SAM se sienta interactivo.

---

## Slide 21

*Sección: SAM 3.1*

**SAM: evolución de capacidades (2023 → 2026)**

- Tres años, cuatro versiones — cada una agregó una capacidad nueva sin romper la anterior:

| Versión | Lanzamiento | Capacidad nueva |
|---|---|---|
| SAM 1 | Abril 2023 | Foundation model para imágenes. Prompts visuales: puntos, cajas, máscaras. |
| SAM 2 | Julio 2024 | Extiende SAM al video — módulo de memoria que mantiene la segmentación coherente entre frames. |
| SAM 3 | Noviembre 2025 | Suma prompts de texto y vocabulario abierto. Permite pedir "todos los hepatocitos" en lenguaje natural. |
| SAM 3.1 | Marzo 2026 | Object Multiplex: tracking conjunto multi-objeto con memoria compartida, sin sacrificar precisión. |

- Patrón a observar: cada versión generaliza más — de imagen a video, de prompts visuales a texto, de un objeto a muchos. Es la misma trayectoria que vivieron los LLMs.
- En la práctica clínica: UNET y SAM conviven. UNET se usa cuando la salida tiene que ser clínicamente medible y reproducible (datos específicos, contornos bajo el píxel). SAM brilla en anotación asistida — un radiólogo clickea, SAM propone la máscara — acelerando 10× o más la creación de datasets médicos.

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-21-1.jpg)

---

## Slide 22 — UNET es modular: adelanto

- **Antes de cerrar la sección, una observación que vamos a retomar muy pronto:**
- **UNET no es solo para segmentación. Su arquitectura — encoder que comprime + decoder que reconstruye + skip connections — sirve para cualquier tarea donde la entrada y la salida sean del mismo tamaño espacial, y donde necesitemos preservar detalles finos.**
- **Ejemplos donde reaparece:**

- **Restauración de imágenes (denoising, deblurring, super-resolución).**
- **Image-to-image translation (MRI → CT, día → noche).**
- **El corazón de Stable Diffusion ← acá la vamos a ver de nuevo.**

- **Spoiler: dentro de un par de slides, vamos a usar una UNET para quitar ruido paso a paso de una imagen — y eso va a ser la pieza central de la generación por difusión.**

---

## Slide 23 — Generación condicionada por texto

*Sección: SECCIÓN 3*

---

## Slide 24 — Recordando Slanted Land

- **Antes de meternos en text-to-image, volvamos al universo que armamos en la clase pasada:**

- **Slanted Land: un mundo donde todo está inclinado. Sus habitantes solo conocen rostros con cierta inclinación — un rostro recto les resultaría incomprensible.**
- **TilTedTinder: la app de citas del lugar. Tenía un problema serio: solo 4 fotos reales en su base de datos. Sin perfiles, no había matches.**
- **La solución de la clase 8: entrenamos una Vanilla GAN que aprendió a generar rostros inclinados a partir de ruido aleatorio. La GAN internalizó el patrón diagonal característico y empezó a producir caras nuevas, plausibles, todas inclinadas.**

- **Resultado: TilTedTinder llenó su base de datos. Los matches florecieron. Slanted Land prosperó.**
- **Pero ahora — un año después — el equipo se topó con un problema nuevo.**

---

## Slide 25 — El nuevo desafío de TilTedTinder

- **La app creció. Ahora tienen miles de usuarios y un dataset valiosísimo: qué tipo de perfiles le gusta a cada uno.**
- **El equipo de producto descubre un patrón: los usuarios no quieren simplemente "más caras inclinadas al azar". Cada usuario tiene preferencias específicas:**

- **"Me atraen las personas inclinadas, altas, con anteojos y pelo rizado."**
- **"Prefiero caras inclinadas, jóvenes, con sonrisa y barba corta."**
- **"Me gustan las inclinadas, mayores, con expresión seria y rasgos angulosos."**

- **La nueva idea de negocio: en lugar de generar perfiles al azar, generar perfiles que coincidan con la descripción de lo que cada usuario busca. Que el usuario pueda escribir lo que le atrae — en lenguaje natural — y la app le muestre candidatos generados a medida.**

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-25-1.png)

- **Pasamos de: "generá una persona inclinada cualquiera"**
- **A: "generá una persona inclinada con estos atributos descritos en texto libre"**

---

## Slide 26 — ¿Por qué la GAN del año pasado no alcanza?

- **El equipo intenta resolverlo con la Vanilla GAN que ya tiene. Falla rápido. Y entender por qué falla es entender qué necesitamos hoy:**

- **La Vanilla GAN aprende una única cosa: "producir algo que parezca un rostro inclinado". No tiene ningún canal para recibir descripciones.**
- **Una Conditional GAN ayudaría parcialmente: podría condicionar por etiquetas predefinidas ("alto", "con anteojos", "rubio"). Pero las preferencias reales son descripciones libres — frases con matices que no encajan en categorías cerradas.**
- **StyleGAN da control de estilo, pero no semántico. No podés decirle "expresión melancólica al atardecer" en texto.**

- **Lo que necesitan: una arquitectura donde la entrada sea texto libre y la salida sea una imagen que coincida con esa descripción. Generación condicionada por texto natural.**
- **Esa arquitectura existe — y se llama Stable Diffusion. El resto de esta clase es entender cómo funciona, para que el equipo de TilTedTinder pueda construir su nuevo sistema.**

---

## Slide 27 — Una nueva tarea: del ruido a las palabras

- Hasta ahora vimos generación de imágenes con GANs — y el control que ofrecían era limitado:

- Vanilla GAN: generabas a partir de ruido aleatorio. Salía algo plausible, pero no podías pedir qué.
- Conditional GAN: podías condicionar por etiqueta de clase ("genera un dígito 7"). Útil, pero pobre — solo manejás categorías predefinidas.
- StyleGAN: te daba control de estilo y atributos, pero no semántico. No podías decir "una mujer joven con anteojos en una cafetería al atardecer".

- La nueva tarea — text-to-image: escribís una descripción en lenguaje natural — un prompt — y el modelo genera una imagen que coincide con esa descripción.

**Por qué es un salto cualitativo:**

- Control expresivo: lenguaje natural cubre infinitamente más matices que una etiqueta.
- Accesibilidad: cualquier persona puede usarlo — no hace falta saber programar.
- Composición libre: podés combinar conceptos que el modelo nunca vio juntos ("un astronauta montando un caballo").

- Esto cierra el paradigma puramente visual y abre el matrimonio entre lenguaje y visión.

---

## Slide 28 — Línea de tiempo: text-to-image en cinco años

- El campo pasó de "no existe" a "uso masivo en producción" en un período muy corto. Cada hito agregó algo:

- 2021 · DALL·E 1 (OpenAI): primera demo viral. Calidad limitada, pero la idea funciona.
- 2022 · DALL·E 2, Imagen (Google), Midjourney v1: salto enorme en realismo. La era del "wow, esto es real".
- Agosto 2022 · Stable Diffusion 1.4: primer modelo open source serio de la era. Pesos publicados, todo el mundo puede ejecutarlo en una GPU de consumo. Cambia el panorama por completo.
- 2023 · DALL·E 3, Stable Diffusion XL, Midjourney v5/v6: mejora drástica en seguir prompts complejos y coherencia.
- 2024 · FLUX, Stable Diffusion 3, Sora (video): texto a imagen se vuelve commodity; texto a video empieza a funcionar.
- 2025-2026: modelos cada vez más grandes, mejor edición controlada, integración con segmentación (SAM) y 3D (SAM 3D).

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-28-1.png)

- Idea para llevarse: Stable Diffusion es el modelo del que vamos a ver las tripas hoy — porque es el que abrió el ecosistema y porque tiene una arquitectura que ya conocemos en parte.

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-28-2.jpg)

---

## Slide 29 — ¿Cómo "entiende" texto una red neuronal?

- Una red neuronal no procesa palabras — procesa números. Para usar texto como entrada, hay que traducirlo primero.

| 01 | 02 | 03 |
|---|---|---|
| Tokenización | Embeddings de palabras | Encoder contextual |
| La oración se parte en piezas pequeñas llamadas tokens (palabras o subpalabras). "Astronauta" puede ser un token; "fotorrealista" puede partirse en "foto" + "realista". | Cada token se reemplaza por un vector de cientos de dimensiones — un punto en un espacio donde palabras de significado parecido están cerca. ("perro" y "gato" cerca; "perro" y "lavarropas" lejos.) | Los vectores sueltos no entienden la oración como un todo — "banco" en "banco de plaza" vs. "banco financiero" significa cosas distintas. Un encoder basado en Transformer procesa toda la secuencia y produce un embedding contextual de la oración completa. |

- Frase clave: un text encoder convierte una oración humana en un vector que captura su significado — y ese vector es lo que vamos a usar para guiar la generación de imágenes.

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-29-1.png)

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-29-2.jpg)

---

## Slide 30

**CLIP: el puente texto ↔ imagen**

- CLIP (Contrastive Language–Image Pre-training, OpenAI, 2021). Es el text encoder que usa Stable Diffusion — y entender por qué está ahí es entender cómo se conectan los dos mundos.
- La idea genial: entrenar dos encoders en paralelo — uno para imagen, uno para texto — de modo que sus salidas vivan en el mismo espacio vectorial.
- Cómo se entrena (intuitivamente):

- Tomá 400 millones de pares (imagen, descripción) de internet.
- Para cada par real, los embeddings de imagen y texto deben quedar cerca.
- Para pares mal apareados, deben quedar lejos.
- Entrenamiento contrastivo a gran escala.

- Resultado: un espacio compartido donde la frase "una foto de un perro corriendo en la playa" aterriza en el mismo vecindario que una imagen real de un perro corriendo en la playa.
- Por qué esto importa para Stable Diffusion: ese embedding de texto que sale de CLIP es el lenguaje común que el resto del modelo (la UNET) entiende. CLIP traduce de "humano" a "espacio que la red puede usar".

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-30-1.jpg)

---

## Slide 31 — La idea de condición: guiar el proceso con el prompt

- Estamos llegando al corazón de Stable Diffusion. Antes de entrar, fijemos una idea clave:

| Generación incondicional | Generación condicionada |
|---|---|
| ruido aleatorio → red → imagen. La red genera lo que aprendió, sin guía. | ruido aleatorio + condición → red → imagen que respeta la condición. |

- La condición puede ser muchas cosas:

- Una etiqueta de clase (cGAN — clase 8).
- Una imagen de referencia (Pix2Pix, image-to-image).
- Un embedding de texto (Stable Diffusion ← acá vamos).

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-31-1.png)

- Punto crucial: la condición no es un input opcional al costado. Es lo que dirige cada paso del proceso de generación. Si la condición dice "perro en la playa", la red empuja el ruido en cada iteración hacia algo que se parezca a eso.

- Adelanto: en Stable Diffusion, el embedding de CLIP se inyecta en cada capa de la UNET mediante un mecanismo llamado cross-attention. Esto es lo que vamos a desarmar en la próxima sección.

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-31-2.png)

---

## Slide 32 — Stable Diffusion

*Sección: SECCIÓN 4*

---

## Slide 33 — La idea de difusión: agregar y quitar ruido

- La inspiración viene de la física: difusión es el proceso por el cual partículas se dispersan hasta el desorden total — pensá una gota de tinta cayendo en un vaso de agua hasta volverse uniforme.
- Aplicado a imágenes — el proceso tiene dos direcciones:

- Forward process (entrenamiento): tomamos una imagen real y le vamos agregando un poquito de ruido gaussiano en cada paso, durante miles de pasos. Al final, la imagen se vuelve ruido puro — indistinguible de un patrón aleatorio.
- Reverse process (inferencia): la red aprende a hacer el camino inverso. Empezamos con ruido puro y, paso a paso, quitamos ruido hasta que emerja una imagen.

- La red aprende una sola cosa: dado un latente ruidoso y un timestep, predecir qué ruido fue agregado. Si sabe predecir el ruido, puede restarlo.
- Diferencia clave con GANs: acá no hay competencia entre dos redes. Hay una sola red aprendiendo a desruidizar — más estable de entrenar, sin mode collapse, con mucha más diversidad en las salidas.
- Una frase: Stable Diffusion no construye la imagen, la talla — empezando por un bloque de ruido y removiendo lo que sobra hasta dejar la figura.

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-33-1.jpg)

---

## Slide 34 — La idea de difusión: agregar y quitar ruido

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-34-1.jpg)

---

## Slide 35

**La idea de difusión: agregar y quitar ruido**

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-35-1.jpg)

---

## Slide 36 — Por qué la difusión "pura" es lenta y costosa

- La idea anterior funciona — DALL·E 2 e Imagen operan así, directamente sobre píxeles. Pero tiene un problema serio.

| Las cuentas | Por qué importa |
|---|---|
| Una imagen de 512×512 RGB = 786.432 valores que la red tiene que procesar.<br>Cada paso de denoising procesa esa imagen completa.<br>Se necesitan típicamente 50 a 1000 pasos para generar una imagen de calidad.<br>Resultado: muchísima memoria (GPUs de 40GB+) y mucho cómputo — minutos por imagen. | Inviable en GPUs de consumo.<br>Inviable para deployment masivo.<br>Inviable para que un equipo chico itere rápido. |

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-36-1.png)

- La pregunta inteligente que se hizo el equipo de CompVis (2021): ¿es realmente necesario operar en píxeles? ¿Y si trabajamos en una versión comprimida de la imagen?

---

## Slide 37 — Latent Diffusion: la idea genial

- Stable Diffusion se llama así por una razón — y la idea fundamental viene del paper de Rombach et al., 2021, "High-Resolution Image Synthesis with Latent Diffusion Models".

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-37-1.png)

- La idea: en lugar de difundir en el espacio de píxeles, difundir en un espacio latente comprimido.

- Las cuentas con compresión:

- Una imagen de 512×512×3 (= 786.432 valores) se comprime a un latente de 64×64×4 (= 16.384 valores).
- Eso es 48× menos información para procesar en cada paso.
- Toda la difusión ocurre en este espacio chico; al final descomprimimos a píxeles.

- Por qué funciona: las imágenes naturales tienen mucha redundancia espacial — píxeles vecinos son muy similares. Una compresión 8× preserva la información estructural y descarta ruido perceptual irrelevante.

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-37-2.png)

- Resultado práctico: Stable Diffusion corre en una GPU de consumo (GTX/RTX con 8-16GB) en pocos segundos. Es lo que democratizó la generación por difusión.

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-37-3.png)

---

## Slide 38

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-38-1.jpg)

---

## Slide 39

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-39-1.jpg)

---

## Slide 40 — Componente 1: el VAE

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-40-1.jpg)

---

## Slide 41

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-41-1.jpg)

---

## Slide 42 — Componente 3: el CLIP Text Encoder

- **Ya lo conocimos en Sección 3 — acá solo cerramos el rol específico que cumple en Stable Diffusion.**
- **Modelo concreto que usa SD 1.x: CLIP ViT-L/14 de OpenAI (123M parámetros). Congelado durante el entrenamiento de Stable Diffusion — el equipo no lo reentrena, lo usa tal cual.**
- **Lo que entra y lo que sale:**

- **Entrada: el prompt de texto (ej: "un astronauta montando un caballo").**
- **Tokenización: 77 tokens (con padding si la frase es corta, truncado si es muy larga).**
- **Salida: una matriz de embeddings de 77 × 768 dimensiones.**

- **Esa matriz se enchufa al UNET en cada bloque de cross-attention, como vimos en el slide anterior. Es el "lenguaje común" entre el prompt humano y la red que talla la imagen.**
- **Decisión de diseño interesante: Stable Diffusion no entrena el text encoder. Lo toma prestado de OpenAI ya entrenado. Esto ahorra cómputo y aprovecha que CLIP ya entendía la relación texto-imagen — no había razón de reinventar esa rueda.**

---

## Slide 43

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-43-1.jpg)

---

## Slide 44 — Los hiperparámetros que importan

- **Cuando ejecutemos la notebook van a aparecer cuatro perillas. Vale entenderlas antes:**

- **num_inference_steps — cuántos pasos de denoising. Más pasos = mejor calidad, pero más lento. Default: 50. Por debajo de 20 la calidad se degrada notoriamente; por encima de 100 las mejoras son marginales.**
- **guidance_scale (classifier-free guidance) — qué tan estrictamente seguir el prompt. Default: 7.5.**
  - **Bajo (1-3): más diverso y creativo, pero menos fiel al prompt.**
  - **Medio (7-9): el sweet spot.**
  - **Alto (15+): muy fiel pero saturado, menos natural.**
- **seed — controla el ruido inicial. Misma seed + mismo prompt = misma imagen (reproducibilidad total). Útil para iterar sin perder el control.**
- **height y width — tamaño de salida. Múltiplos de 8 (porque el VAE comprime 8×). Default: 512×512.**

- **Tip práctico: el ciclo de iteración natural es fijar la seed, fijar el guidance, y mover el prompt — así aislás el efecto de cada cambio textual.**

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-44-1.png)

---

## Slide 45 — Limitaciones de Stable Diffusion

- **No todo es magia. Antes de pasar al notebook, vale tener calibradas las expectativas:**

- **Manos y dedos: notoriamente difíciles. Cantidad de dedos errática, dedos fundidos, anatomía rara. Es el "tell" más conocido de las imágenes generadas.**
- **Anatomía compleja en general: ojos asimétricos, orejas extrañas, articulaciones en lugares improbables.**
- **Texto dentro de la imagen: carteles, letreros, etiquetas → suelen salir como caracteres pseudo-aleatorios. Mejoró mucho en SD 3 / FLUX, pero sigue siendo limitado.**
- **Conteo preciso: "tres manzanas" puede salir con dos, cuatro o cinco. La red no "cuenta", aproxima.**
- **Composición con múltiples sujetos: "un perro a la izquierda y un gato a la derecha" — la separación espacial es frágil.**
- **Sesgos heredados del dataset: lo entrenado con LAION-5B refleja sesgos demográficos, culturales y estéticos de internet. Importante en aplicaciones médicas y sociales.**
- **Costo de inferencia: sigue siendo costoso para deployment masivo en tiempo real.**

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-45-1.png)

- **Idea para cerrar la sección: Stable Diffusion es una herramienta muy poderosa pero falible. Saber dónde falla es tan importante como saber qué puede hacer.**

---

## Slide 46 — TilTedTinder v2, Notebook y Cierre

*Sección: SECCIÓN 5*

---

## Slide 47

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-47-1.jpg)

---

## Slide 48

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-48-1.jpg)

---

## Slide 49

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-49-1.jpg)

---

## Slide 50

![](AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/slide-50-1.jpg)

---
