---
source_file: AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion.md
source_type: article
ingested_at: 2026-08-14
---

# AIG4B — Clase 9: Segmentación y Stable Diffusion

## Provenance
- Original location: `research/articles/AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion.md` (+ `research/articles/AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion-media/`)
- Format: Markdown — extracción 1:1 del deck `AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion.pptx` (50 slides), que vive en la raíz del Talk
- Author / source (if known): la slide 1 dice textualmente **"Autor: Marco Sanchez Sorondo"**. El deck se titula *Inteligencia Artificial Generativa Aplicada en Biomedicina — Clase 9: Segmentación y Stable Diffusion*. **La slide 1 no menciona a la Universidad Austral ni a ninguna institución**; la atribución institucional del curso no está en el archivo y no se registra acá como hecho.
- Date of original (if known): la slide 1 dice **"Última modificación: Abril 2026"**. No hay fecha de creación.
- Notas del orador: **cero**. Verificado abriendo el `.pptx`: existen las 50 partes `ppt/notesSlides/notesSlideN.xml`, pero ninguna contiene texto real — solo el placeholder del número de slide. **0 de 50 slides tienen notas del orador.**
- Imágenes: 53 colocaciones en el deck, **46 imágenes únicas por md5** (31 marcadas `figura`, 15 `icono` en su primera aparición), materializadas en 68 archivos en disco (26 `.jpg`, 27 `.png`, 15 `.svg` originales vectoriales detrás de PNGs). Los 68 archivos + `_manifest.json` están copiados en la carpeta compañera.

## Key claims

Las 50 slides en orden, tal como aparecen en la extracción. Las slides que en el markdown son solo una imagen están marcadas **[SLIDE-IMAGEN]** y su contenido está reconstruido desde la transcripción de la figura (ver `## Images / diagrams`).

**Slide 1 — Inteligencia Artificial Generativa Aplicada en Biomedicina**
- Clase 9: Segmentación y Stable Diffusion.
- Autor: Marco Sanchez Sorondo.
- Última modificación: Abril 2026.

**Slide 2 — Tabla de contenidos**

| 01 | 02 | 03 |
|---|---|---|
| Segmentación: qué es y dónde aparece | Un modelo básico → UNET | Generación condicionada por texto |

| 04 | 05 |
|---|---|
| Stable Diffusion | TilTedTinder v2, Notebook y Cierre |

**Slide 3 — Segmentación: qué es y dónde aparece** (*Sección: SECCIÓN 1*)

**Slide 4 — ¿Qué es segmentar?**
- En visión por computadora, hay tres preguntas distintas que podemos hacerle a una imagen — y segmentar es la más fina de todas.

| Tarea | Pregunta | Salida |
|---|---|---|
| Clasificación | ¿Qué hay en esta imagen? | Una etiqueta (ej: "perro") |
| Detección | ¿Dónde está y qué es? | Cajas con etiquetas |
| Segmentación | ¿Qué representa cada píxel? | Una etiqueta por píxel — una "máscara" |

- Frase clave: segmentar es darle un significado pixel por pixel a la imagen.

**Slide 5 — Tipos de segmentación**
- Tres niveles de granularidad, según qué tan finamente queramos diferenciar lo que vemos:
- **Semántica**: etiqueta cada píxel con su clase, sin distinguir individuos. Todos los píxeles de "auto" reciben la misma etiqueta, aunque haya cinco autos.
- **De instancias**: distingue cada objeto individual. "Auto 1", "auto 2", "auto 3"... aunque sean de la misma clase.
- **Panóptica**: combina ambas — clasifica cada píxel y distingue instancias. Es la versión más completa.

**Slide 6 — Aplicaciones genéricas**
- La segmentación es uno de los pilares de la visión moderna. Algunos casos donde ya está corriendo en producción:
- **Autos autónomos** — Separar carretera, peatones, semáforos, otros vehículos.
- **Imagen satelital** — Medir cobertura forestal, urbanización, cuerpos de agua.
- **Videoconferencia (Zoom, Meet)** — Separar persona del fondo en tiempo real.
- **Agricultura de precisión** — Detectar zonas con plagas o estrés hídrico.
- **Edición de fotos** — "Seleccionar sujeto" automático en Photoshop.

**Slide 7 — Aplicaciones en medicina**
- En biomedicina, segmentar suele ser el paso clínico, no un paso intermedio. La máscara final es la respuesta:
- Neuroimagen (MRI cerebro y en general): delinear tumores, lesiones de esclerosis múltiple, hipocampo.
- Oncología (CT/PET): medir volumen tumoral para planificar radioterapia.
- Cardiología: delimitar ventrículos para calcular fracción de eyección.
- Patología digital: contar y delimitar células, núcleos, mitosis.
- Oftalmología: segmentar vasos retinianos (diabetes, hipertensión).
- Dermatología: delimitar lesiones para seguimiento y biopsia guiada.
- Punto importante: la máscara es lo que se mide, se documenta y se compara entre estudios.

**Slide 8 — Aplicaciones en medicina** **[SLIDE-IMAGEN]** — sin texto alguno en el markdown.
- Contenido rescatado de la figura: comparación cualitativa de segmentación cardíaca en dos modalidades de MRI. Filas: **LGE** y **SSFP**. Columnas: **Input**, **Single image type UNet**, **MI-UNet**. Tres estructuras segmentadas por color: azul/violeta (cavidad del ventrículo izquierdo), verde (miocardio), rojo (ventrículo derecho). El punto visual es que MI-UNet produce contornos más limpios que la UNet de tipo de imagen único, sobre todo en el ventrículo derecho (rojo).

**Slide 9 — Cómo se ve una salida**
- Visualización típica: Imagen original (MRI) → Máscara binaria del tumor (blanco = tumor, negro = no tumor) → Overlay (máscara coloreada superpuesta sobre la imagen).
- Punto técnico: internamente, la máscara es una matriz del mismo tamaño que la imagen, donde cada celda dice a qué clase pertenece ese píxel. Para 2 clases es 0/1; para N clases es 0..N-1.

**Slide 10 — Un modelo básico → UNET** (*Sección: SECCIÓN 2*)

**Slide 11 — La intuición: clasificar cada píxel**
- Si segmentar es asignar una etiqueta a cada píxel, la idea más directa es: tratá cada píxel como un mini-problema de clasificación.
- Recordemos: ya sabemos clasificar imágenes. Una CNN clásica recibe una imagen y devuelve una etiqueta. Para llegar a esa única etiqueta, va comprimiendo la imagen con convoluciones + pooling, hasta que al final una capa densa entrega la clase.
- Idea de FCN (Fully Convolutional Network — Long et al., 2015): sacar la capa densa final y reemplazarla por más capas convolucionales que produzcan una salida espacial del mismo tamaño que la entrada — un mapa donde cada celda es la clase de ese píxel.
- Una sola frase: "convertí un clasificador de imágenes en un clasificador de píxeles".

**Slide 12 — FCN: cómo se ve por dentro**
- Tres pasos conceptuales:
- **1 — Encoder convolucional**: la imagen entra y se va comprimiendo capa a capa — cada capa "ve" patrones más abstractos (bordes → texturas → estructuras → objetos).
- **2 — Reemplazo de la capa densa por convoluciones 1×1**: en lugar de aplastar todo a un vector, se mantienen las dimensiones espaciales. La salida es un mapa de baja resolución con probabilidades por clase.
- **3 — Upsampling**: ese mapa pequeño se "estira" hasta el tamaño original con convoluciones traspuestas (la operación inversa al pooling).
- Resultado: una máscara con una etiqueta por píxel. Funciona — y fue el primer modelo de segmentación end-to-end con deep learning.

**Slide 13 — El problema de FCN**
- FCN funciona, pero tiene una limitación seria que se ve en las máscaras que produce:

| El problema | Síntoma visual |
|---|---|
| Durante el encoder, la red comprime mucho — una imagen de 512×512 puede terminar como un mapa de 16×16. Cuando hacemos upsampling para volver al tamaño original, la información espacial fina ya se perdió. | Los contornos quedan borrosos o redondeados. Detalles finos — el borde exacto de un tumor, el contorno de un núcleo celular — desaparecen. |

| Por qué importa en medicina | La pregunta |
|---|---|
| Si estás midiendo el volumen de un tumor para decidir radioterapia, un borde 2 píxeles más adentro o más afuera cambia el cálculo y puede cambiar la decisión clínica. | ¿Cómo recuperamos los detalles finos que el encoder se llevó? |

**Slide 14 — UNET: nacida en biomedicina**

| Origen | Contexto |
|---|---|
| Olaf Ronneberger, Philipp Fischer, Thomas Brox — Universidad de Friburgo, 2015. Paper original: "U-Net: Convolutional Networks for Biomedical Image Segmentation". | La primera versión se diseñó específicamente para segmentar células en microscopía electrónica, en un challenge donde había muy pocas imágenes etiquetadas — el clásico problema biomédico. |

| El truco | Dato |
|---|---|
| Una arquitectura simétrica — un encoder que comprime + un decoder que reconstruye — conectados por atajos que evitan la pérdida de detalle. | Es uno de los papers más citados de la última década en visión por computadora. Diez años después sigue siendo la base por defecto para segmentación médica. |

**Slide 15 — La arquitectura en U**
- La forma en U no es decoración — describe literalmente cómo fluyen los datos:
- **Rama izquierda — Encoder (camino contractivo)**: la imagen baja por convoluciones + max pooling. En cada nivel, las dimensiones espaciales se reducen a la mitad y los canales se duplican. "Qué hay" se entiende cada vez mejor; "dónde está" se pierde.
- **Punto inferior — Bottleneck**: la representación más comprimida y abstracta. Acá vive la información semántica de alto nivel.
- **Rama derecha — Decoder (camino expansivo)**: la representación sube por convoluciones traspuestas (upsampling aprendido). En cada nivel, las dimensiones espaciales se duplican y los canales se reducen a la mitad. "Dónde" se reconstruye progresivamente.
- Salida: una máscara del mismo tamaño que la entrada, con una clase por píxel.

**Slide 16 — La clave: skip connections**
- Sin esto, UNET sería un FCN más elegante. Las skip connections son la innovación que cambia todo.
- Qué hacen: cada nivel del encoder tiene una conexión directa horizontal al nivel correspondiente del decoder. La salida del encoder en ese nivel se concatena con la entrada del decoder en el mismo nivel.
- Por qué resuelve el problema de FCN: el decoder recibe dos fuentes de información en cada nivel — la representación abstracta que sube desde el bottleneck (qué es) + la representación detallada del encoder al mismo nivel (dónde está, exactamente).
- Los detalles finos que el encoder vio antes de comprimir no se pierden — viajan por el atajo y se recuperan en el decoder.
- Resultado: contornos precisos, no borrosos. Esto es lo que hace que UNET sirva para uso clínico real.

**Slide 17 — Por qué funciona tan bien en medicina**
- UNET se volvió el estándar de facto en imagen médica por tres razones que se alinean con las restricciones de la disciplina:
- **Funciona con pocos datos**: las skip connections actúan como un regularizador estructural. UNET puede entrenarse con cientos de imágenes — no miles — y aún así generalizar bien. Crítico cuando etiquetar requiere un radiólogo.
- **Contornos precisos**: los detalles finos sobreviven el viaje por la U. En medicina, el borde es el dato.
- **Es modular y adaptable**: la misma arquitectura funciona para MRI cerebro, células de patología, retina, ecografía cardíaca... cambia el dataset, no la red.

**Slide 18 — SAM: ¿qué hace y por qué fue revolucionario?**
- Si UNET es el modelo artesanal — chico, especializado, entrenado para una tarea concreta — SAM (Segment Anything Model, Meta, 2023) es el opuesto: un foundation model masivo que segmenta cualquier cosa en cualquier imagen, sin reentrenamiento.
- Lo que hace: recibe una imagen + una pista (un click, una caja, una máscara aproximada o, desde SAM 3, texto) y devuelve la máscara del objeto que querés. Cero entrenamiento previo sobre tu dominio.
- La idea nueva: **segmentación promptable**. SAM trajo al mundo de la segmentación el paradigma "foundation model + prompt en inferencia" que ya había explotado en NLP con los LLMs.
- Una frase para llevarse: SAM no aprende una tarea — aprende qué es un objeto, y deja que vos le digas cuál querés.

**Slide 19 — SAM: ¿qué hace y por qué fue revolucionario?** **[SLIDE-IMAGEN]** — solo título en negrita, cero cuerpo.
- Contenido rescatado de la figura: diagrama de la **tarea de segmentación promptable**. Abajo a la derecha, `image` (foto de dos gatos junto a una maceta). Abajo a la izquierda, cuatro cajas agrupadas bajo la llave `segmentation prompt`: (1) puntos — un punto rojo (negativo) y dos verdes (positivos); (2) una caja vacía (bounding box); (3) una mancha azul difusa (máscara aproximada); (4) texto libre — `cat with black ears`. Ambas ramas suben a una caja amarilla ancha rotulada `model`, de la que sale una flecha hacia arriba a `valid mask` — la misma foto con el gato de la derecha pintado en azul.

**Slide 20 — SAM: mejoras conceptuales internas**
- La arquitectura de SAM tiene dos ideas elegantes que explican su impacto:

| Idea 1 — Separar lo caro de lo barato. | Idea 2 — El dataset SA-1B. |
|---|---|
| SAM divide el problema en tres componentes con costos muy distintos. | Meta construyó el dataset más grande de la historia de la segmentación: 1.000 millones de máscaras sobre 11 millones de imágenes. Lo armaron con un data engine iterativo donde el propio SAM ayudaba a anotar más datos, mejorando ronda tras ronda. Sin SA-1B, SAM no funcionaría — el secreto está tanto en el modelo como en los datos. |

- **Image Encoder** (ViT, masivo): procesa la imagen una vez y produce un embedding rico. Es el ~95% del cómputo.
- **Prompt Encoder** (liviano): convierte el prompt (punto, caja, texto) en un embedding compatible.
- **Mask Decoder** (liviano): combina los dos embeddings y produce la máscara.
- El truco: la imagen se codifica una sola vez. Después podés probar decenas de prompts distintos sobre esa misma imagen casi gratis — solo se reejecuta el decoder. Esto es lo que hace que SAM se sienta interactivo.

**Slide 21 — SAM: evolución de capacidades (2023 → 2026)** (*Sección: SAM 3.1*)
- Tres años, cuatro versiones — cada una agregó una capacidad nueva sin romper la anterior:

| Versión | Lanzamiento | Capacidad nueva |
|---|---|---|
| SAM 1 | Abril 2023 | Foundation model para imágenes. Prompts visuales: puntos, cajas, máscaras. |
| SAM 2 | Julio 2024 | Extiende SAM al video — módulo de memoria que mantiene la segmentación coherente entre frames. |
| SAM 3 | Noviembre 2025 | Suma prompts de texto y vocabulario abierto. Permite pedir "todos los hepatocitos" en lenguaje natural. |
| SAM 3.1 | Marzo 2026 | Object Multiplex: tracking conjunto multi-objeto con memoria compartida, sin sacrificar precisión. |

- Patrón a observar: cada versión generaliza más — de imagen a video, de prompts visuales a texto, de un objeto a muchos. Es la misma trayectoria que vivieron los LLMs.
- En la práctica clínica: UNET y SAM conviven. UNET se usa cuando la salida tiene que ser clínicamente medible y reproducible (datos específicos, contornos bajo el píxel). SAM brilla en anotación asistida — un radiólogo clickea, SAM propone la máscara — acelerando 10× o más la creación de datasets médicos.

**Slide 22 — UNET es modular: adelanto**
- Antes de cerrar la sección, una observación que vamos a retomar muy pronto:
- UNET no es solo para segmentación. Su arquitectura — encoder que comprime + decoder que reconstruye + skip connections — sirve para cualquier tarea donde la entrada y la salida sean del mismo tamaño espacial, y donde necesitemos preservar detalles finos.
- Ejemplos donde reaparece: restauración de imágenes (denoising, deblurring, super-resolución); image-to-image translation (MRI → CT, día → noche); **el corazón de Stable Diffusion**.
- Spoiler: dentro de un par de slides, vamos a usar una UNET para quitar ruido paso a paso de una imagen — y eso va a ser la pieza central de la generación por difusión.

**Slide 23 — Generación condicionada por texto** (*Sección: SECCIÓN 3*)

**Slide 24 — Recordando Slanted Land**
- Antes de meternos en text-to-image, volvamos al universo que armamos en la clase pasada:
- **Slanted Land**: un mundo donde todo está inclinado. Sus habitantes solo conocen rostros con cierta inclinación — un rostro recto les resultaría incomprensible.
- **TilTedTinder**: la app de citas del lugar. Tenía un problema serio: solo 4 fotos reales en su base de datos. Sin perfiles, no había matches.
- La solución de la clase 8: entrenamos una Vanilla GAN que aprendió a generar rostros inclinados a partir de ruido aleatorio. La GAN internalizó el patrón diagonal característico y empezó a producir caras nuevas, plausibles, todas inclinadas.
- Resultado: TilTedTinder llenó su base de datos. Los matches florecieron. Slanted Land prosperó.
- Pero ahora — un año después — el equipo se topó con un problema nuevo.

**Slide 25 — El nuevo desafío de TilTedTinder**
- La app creció. Ahora tienen miles de usuarios y un dataset valiosísimo: qué tipo de perfiles le gusta a cada uno.
- El equipo de producto descubre un patrón: los usuarios no quieren simplemente "más caras inclinadas al azar". Cada usuario tiene preferencias específicas:
  - "Me atraen las personas inclinadas, altas, con anteojos y pelo rizado."
  - "Prefiero caras inclinadas, jóvenes, con sonrisa y barba corta."
  - "Me gustan las inclinadas, mayores, con expresión seria y rasgos angulosos."
- La nueva idea de negocio: en lugar de generar perfiles al azar, generar perfiles que coincidan con la descripción de lo que cada usuario busca. Que el usuario pueda escribir lo que le atrae — en lenguaje natural — y la app le muestre candidatos generados a medida.
- Pasamos de: "generá una persona inclinada cualquiera" → A: "generá una persona inclinada con estos atributos descritos en texto libre".

**Slide 26 — ¿Por qué la GAN del año pasado no alcanza?**
- El equipo intenta resolverlo con la Vanilla GAN que ya tiene. Falla rápido. Y entender por qué falla es entender qué necesitamos hoy:
- La Vanilla GAN aprende una única cosa: "producir algo que parezca un rostro inclinado". No tiene ningún canal para recibir descripciones.
- Una Conditional GAN ayudaría parcialmente: podría condicionar por etiquetas predefinidas ("alto", "con anteojos", "rubio"). Pero las preferencias reales son descripciones libres — frases con matices que no encajan en categorías cerradas.
- StyleGAN da control de estilo, pero no semántico. No podés decirle "expresión melancólica al atardecer" en texto.
- Lo que necesitan: una arquitectura donde la entrada sea texto libre y la salida sea una imagen que coincida con esa descripción. Generación condicionada por texto natural.
- Esa arquitectura existe — y se llama Stable Diffusion. El resto de esta clase es entender cómo funciona, para que el equipo de TilTedTinder pueda construir su nuevo sistema.

**Slide 27 — Una nueva tarea: del ruido a las palabras**
- Hasta ahora vimos generación de imágenes con GANs — y el control que ofrecían era limitado:
- Vanilla GAN: generabas a partir de ruido aleatorio. Salía algo plausible, pero no podías pedir qué.
- Conditional GAN: podías condicionar por etiqueta de clase ("genera un dígito 7"). Útil, pero pobre — solo manejás categorías predefinidas.
- StyleGAN: te daba control de estilo y atributos, pero no semántico. No podías decir "una mujer joven con anteojos en una cafetería al atardecer".
- La nueva tarea — **text-to-image**: escribís una descripción en lenguaje natural — un prompt — y el modelo genera una imagen que coincide con esa descripción.
- Por qué es un salto cualitativo:
  - Control expresivo: lenguaje natural cubre infinitamente más matices que una etiqueta.
  - Accesibilidad: cualquier persona puede usarlo — no hace falta saber programar.
  - Composición libre: podés combinar conceptos que el modelo nunca vio juntos ("un astronauta montando un caballo").
- Esto cierra el paradigma puramente visual y abre el matrimonio entre lenguaje y visión.

**Slide 28 — Línea de tiempo: text-to-image en cinco años**
- El campo pasó de "no existe" a "uso masivo en producción" en un período muy corto. Cada hito agregó algo:
- 2021 · DALL·E 1 (OpenAI): primera demo viral. Calidad limitada, pero la idea funciona.
- 2022 · DALL·E 2, Imagen (Google), Midjourney v1: salto enorme en realismo. La era del "wow, esto es real".
- Agosto 2022 · Stable Diffusion 1.4: primer modelo open source serio de la era. Pesos publicados, todo el mundo puede ejecutarlo en una GPU de consumo. Cambia el panorama por completo.
- 2023 · DALL·E 3, Stable Diffusion XL, Midjourney v5/v6: mejora drástica en seguir prompts complejos y coherencia.
- 2024 · FLUX, Stable Diffusion 3, Sora (video): texto a imagen se vuelve commodity; texto a video empieza a funcionar.
- 2025-2026: modelos cada vez más grandes, mejor edición controlada, integración con segmentación (SAM) y 3D (SAM 3D).
- Idea para llevarse: Stable Diffusion es el modelo del que vamos a ver las tripas hoy — porque es el que abrió el ecosistema y porque tiene una arquitectura que ya conocemos en parte.

**Slide 29 — ¿Cómo "entiende" texto una red neuronal?**
- Una red neuronal no procesa palabras — procesa números. Para usar texto como entrada, hay que traducirlo primero.

| 01 | 02 | 03 |
|---|---|---|
| Tokenización | Embeddings de palabras | Encoder contextual |
| La oración se parte en piezas pequeñas llamadas tokens (palabras o subpalabras). "Astronauta" puede ser un token; "fotorrealista" puede partirse en "foto" + "realista". | Cada token se reemplaza por un vector de cientos de dimensiones — un punto en un espacio donde palabras de significado parecido están cerca. ("perro" y "gato" cerca; "perro" y "lavarropas" lejos.) | Los vectores sueltos no entienden la oración como un todo — "banco" en "banco de plaza" vs. "banco financiero" significa cosas distintas. Un encoder basado en Transformer procesa toda la secuencia y produce un embedding contextual de la oración completa. |

- Frase clave: un text encoder convierte una oración humana en un vector que captura su significado — y ese vector es lo que vamos a usar para guiar la generación de imágenes.

**Slide 30 — CLIP: el puente texto ↔ imagen**
- CLIP (Contrastive Language–Image Pre-training, OpenAI, 2021). Es el text encoder que usa Stable Diffusion — y entender por qué está ahí es entender cómo se conectan los dos mundos.
- La idea genial: entrenar dos encoders en paralelo — uno para imagen, uno para texto — de modo que sus salidas vivan en el mismo espacio vectorial.
- Cómo se entrena (intuitivamente):
  - Tomá 400 millones de pares (imagen, descripción) de internet.
  - Para cada par real, los embeddings de imagen y texto deben quedar cerca.
  - Para pares mal apareados, deben quedar lejos.
  - Entrenamiento contrastivo a gran escala.
- Resultado: un espacio compartido donde la frase "una foto de un perro corriendo en la playa" aterriza en el mismo vecindario que una imagen real de un perro corriendo en la playa.
- Por qué esto importa para Stable Diffusion: ese embedding de texto que sale de CLIP es el lenguaje común que el resto del modelo (la UNET) entiende. CLIP traduce de "humano" a "espacio que la red puede usar".

**Slide 31 — La idea de condición: guiar el proceso con el prompt**
- Estamos llegando al corazón de Stable Diffusion. Antes de entrar, fijemos una idea clave:

| Generación incondicional | Generación condicionada |
|---|---|
| ruido aleatorio → red → imagen. La red genera lo que aprendió, sin guía. | ruido aleatorio + condición → red → imagen que respeta la condición. |

- La condición puede ser muchas cosas: una etiqueta de clase (cGAN — clase 8); una imagen de referencia (Pix2Pix, image-to-image); un embedding de texto (Stable Diffusion ← acá vamos).
- Punto crucial: la condición no es un input opcional al costado. Es lo que dirige cada paso del proceso de generación. Si la condición dice "perro en la playa", la red empuja el ruido en cada iteración hacia algo que se parezca a eso.
- Adelanto: en Stable Diffusion, el embedding de CLIP se inyecta en cada capa de la UNET mediante un mecanismo llamado **cross-attention**. Esto es lo que vamos a desarmar en la próxima sección.

**Slide 32 — Stable Diffusion** (*Sección: SECCIÓN 4*)

**Slide 33 — La idea de difusión: agregar y quitar ruido**
- La inspiración viene de la física: difusión es el proceso por el cual partículas se dispersan hasta el desorden total — pensá una gota de tinta cayendo en un vaso de agua hasta volverse uniforme.
- Aplicado a imágenes — el proceso tiene dos direcciones:
  - **Forward process (entrenamiento)**: tomamos una imagen real y le vamos agregando un poquito de ruido gaussiano en cada paso, durante miles de pasos. Al final, la imagen se vuelve ruido puro — indistinguible de un patrón aleatorio.
  - **Reverse process (inferencia)**: la red aprende a hacer el camino inverso. Empezamos con ruido puro y, paso a paso, quitamos ruido hasta que emerja una imagen.
- La red aprende una sola cosa: dado un latente ruidoso y un timestep, predecir qué ruido fue agregado. Si sabe predecir el ruido, puede restarlo.
- Diferencia clave con GANs: acá no hay competencia entre dos redes. Hay una sola red aprendiendo a desruidizar — más estable de entrenar, sin mode collapse, con mucha más diversidad en las salidas.
- Una frase: Stable Diffusion no construye la imagen, la talla — empezando por un bloque de ruido y removiendo lo que sobra hasta dejar la figura.

**Slide 34 — La idea de difusión: agregar y quitar ruido** **[SLIDE-IMAGEN]** — sin texto alguno en el markdown.
- Contenido rescatado de la figura: diagrama titulado **"Reverse / Denoising process"** con el subtítulo `Sample noise p_T(x_T) → turn into data`. Una flecha roja de izquierda a derecha atraviesa ocho miniaturas de un golden retriever que pasan de ruido de color puro a la foto nítida. Extremo izquierdo: `p_T(x_T) ~ N(0, I)` y la etiqueta *Pure noise*; extremo derecho: `p_0(x_0)` y la etiqueta *Clean sample*. Bajo las miniaturas: `X_T`, `X_{T-1}`, ..., `X_1`, `X_0`.
- **Crédito embebido**: la figura lleva el logo y la palabra **"Calibraint"** arriba a la izquierda. El deck no cita esa fuente en ninguna parte del texto.

**Slide 35 — La idea de difusión: agregar y quitar ruido** **[SLIDE-IMAGEN]** — solo título en negrita, cero cuerpo.
- Contenido rescatado de la figura: figura de paper de cuatro paneles (a–e) sobre difusión aplicada a imagen médica (cortes axiales de CT/MRI de pelvis).
  - **a) Diffusion process**: fila de imágenes `X_0, X_1, X_2, ..., X_{T-2}, X_{T-1}, X_T`, con una flecha verde **Forward diffusion** hacia la derecha y una flecha amarilla **Reverse diffusion** hacia la izquierda.
  - **b) Network architecture**: `X_t` entra a una U de bloques etiquetados con anchos de canal `64, 128, 128, 128, 256, 512, 512, 512, 512, 512, 512, 512, 256, 256, 128, 128`; salen dos cabezas, `Noise ε_θ` y `Variance coeff v_t`, que producen `X_{t-1}`. Una barra amarilla `Timestep t` alimenta todos los bloques. Leyenda: verde/naranja = *Up/down-sample Convolutional layer*; azul/crema/rosa = *Up/down/no-sample Swin-transformer layer*; amarillo = *Linear layer*; violeta = *Swin layer*; teal = *Up/down 3x3x3 Convolutional layer*; gris = *3x3 Convolutional layer*; línea de guiones = *Shortcut connection*; línea punto-raya = *Residual connection*; ⊕ = *Addition*.
  - **c) Swin-transformer layer** y **d) Convolutional layer**: detalle interno de cada bloque, ambos con una caja `Time embedding` inyectada.
  - **e) Image generation**: `New X_T` → `Fine-trained MDT` → `New X_{T-1}` → `Fine-trained MDT` → `New X_{T-2}` → ... → `New X_0`.

**Slide 36 — Por qué la difusión "pura" es lenta y costosa**
- La idea anterior funciona — DALL·E 2 e Imagen operan así, directamente sobre píxeles. Pero tiene un problema serio.

| Las cuentas | Por qué importa |
|---|---|
| Una imagen de 512×512 RGB = 786.432 valores que la red tiene que procesar.<br>Cada paso de denoising procesa esa imagen completa.<br>Se necesitan típicamente 50 a 1000 pasos para generar una imagen de calidad.<br>Resultado: muchísima memoria (GPUs de 40GB+) y mucho cómputo — minutos por imagen. | Inviable en GPUs de consumo.<br>Inviable para deployment masivo.<br>Inviable para que un equipo chico itere rápido. |

- La pregunta inteligente que se hizo el equipo de CompVis (2021): ¿es realmente necesario operar en píxeles? ¿Y si trabajamos en una versión comprimida de la imagen?

**Slide 37 — Latent Diffusion: la idea genial**
- Stable Diffusion se llama así por una razón — y la idea fundamental viene del paper de Rombach et al., 2021, "High-Resolution Image Synthesis with Latent Diffusion Models".
- La idea: en lugar de difundir en el espacio de píxeles, difundir en un espacio latente comprimido.
- Las cuentas con compresión:
  - Una imagen de 512×512×3 (= 786.432 valores) se comprime a un latente de 64×64×4 (= 16.384 valores).
  - Eso es **48× menos información** para procesar en cada paso.
  - Toda la difusión ocurre en este espacio chico; al final descomprimimos a píxeles.
- Por qué funciona: las imágenes naturales tienen mucha redundancia espacial — píxeles vecinos son muy similares. Una compresión 8× preserva la información estructural y descarta ruido perceptual irrelevante.
- Resultado práctico: Stable Diffusion corre en una GPU de consumo (GTX/RTX con 8-16GB) en pocos segundos. Es lo que democratizó la generación por difusión.

**Slide 38 — Las tres piezas de Stable Diffusion** **[SLIDE-IMAGEN]** — sin texto alguno en el markdown.
- Contenido rescatado de la figura: *"Antes de meternos en cada componente, fijemos el mapa completo. Stable Diffusion tiene **tres redes** que trabajan juntas:"*

| Componente | Qué hace | Tamaño aprox. |
|---|---|---|
| VAE (Variational Autoencoder) | Comprime imagen ↔ latente | ~80M params |
| UNET | Denoiser condicional en espacio latente | ~860M params |
| CLIP Text Encoder | Prompt de texto → embedding | ~123M params |

- **Cómo se conectan**: el prompt entra al CLIP, que produce un embedding. El UNET usa ese embedding para guiar el denoising en el espacio latente. Cuando termina, el VAE Decoder transforma el latente final en una imagen visible.
- **Punto importante para llevarse**: dos de estas piezas — UNET y CLIP — ya las vimos. UNET la vimos en segmentación (Sección 2), CLIP en text-to-image (Sección 3). Solo nos queda entender el VAE y cómo se orquestan.
- La slide incluye además un diagrama de pipeline embebido (ver `## Images / diagrams`, slide-38-1).

**Slide 39 — Componente 1: el VAE** **[SLIDE-IMAGEN]** — sin texto alguno en el markdown.
- Contenido rescatado de la figura: *"**VAE — Variational Autoencoder.** Es la pieza que se encarga de la compresión-descompresión entre píxeles y espacio latente."*
- **Dos mitades:**
  - **Encoder**: toma la imagen 512×512×3 y la mapea a un latente 64×64×4. Compresión ~48×.
  - **Decoder**: toma un latente 64×64×4 y reconstruye una imagen 512×512×3.
- **Cuándo se usa cada parte:**
  - **Durante entrenamiento de SD**: se usa el encoder — para llevar las imágenes reales del dataset al espacio latente, donde la UNET aprende a desruidizar.
  - **Durante inferencia (lo que nos interesa hoy): solo se usa el decoder** — para tomar el latente final ya desruidizado y reconstruir la imagen visible.
- **Cómo se entrena**: el VAE se entrena **antes y por separado** de la UNET. Su objetivo es simple: que `decoder(encoder(imagen)) ≈ imagen`. Una vez entrenado, sus pesos quedan congelados.
- **Frase corta**: el VAE es un compresor inteligente — convierte el problema de "generar 800K píxeles" en el problema de "generar 16K números latentes".

**Slide 40 — Componente 1: el VAE** — título presente, **cuerpo vacío**; todo el contenido es la figura.
- Contenido rescatado de la figura: diagrama esquemático de autoencoder. De izquierda a derecha: caja blanca `x` bajo la llave **Input** → flecha → bloque verde alto → `...` → bloque verde más chico, todo bajo la llave **Encoder** → flecha → bloque rojo con una curva gaussiana dibujada dentro, bajo la llave **Latent Space** → flecha → bloque azul chico → `...` → bloque azul alto, bajo la llave **Decoder** → flecha → caja blanca `x'` bajo la llave **Output**. El estrechamiento progresivo de los bloques representa la reducción de dimensionalidad; la campana gaussiana marca que el latente es una distribución, no un punto (lo "variacional" del VAE).

**Slide 41 — Componente 2: la UNET (¡acá vuelve!)** **[SLIDE-IMAGEN]** — sin texto alguno en el markdown.
- Contenido rescatado de la figura:
- *"**Esta es la pieza central de Stable Diffusion** — y es **la misma estructura** que vimos en Sección 2 para segmentación."*
- **Arquitectura**: encoder + decoder con forma en U + skip connections. Idéntica a UNET de segmentación.
- **Pero la tarea es distinta:**
  - **UNET de segmentación**: entrada = imagen, salida = máscara.
  - **UNET de Stable Diffusion**: entrada = (latente ruidoso, timestep, embedding de texto), salida = **predicción del ruido presente en el latente**.
- **Cómo se inyecta la condición de texto — cross-attention**: en cada nivel de la U (tanto bajando como subiendo), hay un bloque de cross-attention que "consulta" al embedding de CLIP. El modelo se pregunta en cada capa: *"dado lo que sé hasta acá, ¿qué partes del prompt son relevantes para guiar este nivel?"*
- **El ciclo de denoising en cada paso:**
  1. La UNET recibe el latente ruidoso actual + el timestep + el embedding del prompt.
  2. Predice el ruido que cree que está presente.
  3. El scheduler resta ese ruido del latente → latente un poco menos ruidoso.
  4. Se repite ~50 veces.
- **La conexión que cierra el círculo**: la misma arquitectura que en 2015 servía para segmentar células al microscopio, hoy es el corazón de la generación de imágenes más usada del mundo. UNET no es solo una red — es **un patrón arquitectónico** poderosamente reutilizable.

**Slide 42 — Componente 3: el CLIP Text Encoder**
- Ya lo conocimos en Sección 3 — acá solo cerramos el rol específico que cumple en Stable Diffusion.
- Modelo concreto que usa SD 1.x: **CLIP ViT-L/14 de OpenAI (123M parámetros)**. Congelado durante el entrenamiento de Stable Diffusion — el equipo no lo reentrena, lo usa tal cual.
- Lo que entra y lo que sale:
  - Entrada: el prompt de texto (ej: "un astronauta montando un caballo").
  - Tokenización: **77 tokens** (con padding si la frase es corta, truncado si es muy larga).
  - Salida: una matriz de embeddings de **77 × 768** dimensiones.
- Esa matriz se enchufa al UNET en cada bloque de cross-attention, como vimos en el slide anterior. Es el "lenguaje común" entre el prompt humano y la red que talla la imagen.
- Decisión de diseño interesante: Stable Diffusion no entrena el text encoder. Lo toma prestado de OpenAI ya entrenado. Esto ahorra cómputo y aprovecha que CLIP ya entendía la relación texto-imagen — no había razón de reinventar esa rueda.

**Slide 43 — Pipeline completo de inferencia** **[SLIDE-IMAGEN]** — sin texto alguno en el markdown.
- Contenido rescatado de la figura: *"Juntamos todo. Esto es lo que ocurre, paso por paso, cuando alguien escribe un prompt y Stable Diffusion produce una imagen."*
- **Paso 1 — Procesar el prompt:** Prompt → tokenizer → CLIP Text Encoder → embedding de texto (77 × 768).
- **Paso 2 — Inicializar el latente con ruido:** Generar un tensor aleatorio de 64×64×4 desde una distribución normal (controlado por la *seed*). Este es el "bloque de mármol" del que vamos a tallar.
- **Paso 3 — Bucle de denoising (~50 pasos):** Para cada timestep t (de máximo a mínimo):
  - UNET recibe (latente actual, timestep t, embedding del prompt).
  - UNET predice el ruido presente.
  - El scheduler resta ese ruido → latente un poco menos ruidoso.
- **Paso 4 — Decodificar a píxeles:** Latente final 64×64×4 → VAE Decoder → imagen 512×512×3.
- **Paso 5 — Devolver al usuario.** La imagen final.
- **Frase para cerrar**: todo lo que vimos en las secciones anteriores — UNET, embeddings de texto, condición — confluye en este pipeline. No es un modelo monolítico mágico; **son tres piezas modulares orquestadas por un loop iterativo**.

**Slide 44 — Los hiperparámetros que importan**
- Cuando ejecutemos la notebook van a aparecer cuatro perillas. Vale entenderlas antes:
- **`num_inference_steps`** — cuántos pasos de denoising. Más pasos = mejor calidad, pero más lento. Default: 50. Por debajo de 20 la calidad se degrada notoriamente; por encima de 100 las mejoras son marginales.
- **`guidance_scale`** (classifier-free guidance) — qué tan estrictamente seguir el prompt. Default: 7.5.
  - Bajo (1-3): más diverso y creativo, pero menos fiel al prompt.
  - Medio (7-9): el sweet spot.
  - Alto (15+): muy fiel pero saturado, menos natural.
- **`seed`** — controla el ruido inicial. Misma seed + mismo prompt = misma imagen (reproducibilidad total). Útil para iterar sin perder el control.
- **`height` y `width`** — tamaño de salida. Múltiplos de 8 (porque el VAE comprime 8×). Default: 512×512.
- Tip práctico: el ciclo de iteración natural es fijar la seed, fijar el guidance, y mover el prompt — así aislás el efecto de cada cambio textual.

**Slide 45 — Limitaciones de Stable Diffusion**
- No todo es magia. Antes de pasar al notebook, vale tener calibradas las expectativas:
- **Manos y dedos**: notoriamente difíciles. Cantidad de dedos errática, dedos fundidos, anatomía rara. Es el "tell" más conocido de las imágenes generadas.
- **Anatomía compleja en general**: ojos asimétricos, orejas extrañas, articulaciones en lugares improbables.
- **Texto dentro de la imagen**: carteles, letreros, etiquetas → suelen salir como caracteres pseudo-aleatorios. Mejoró mucho en SD 3 / FLUX, pero sigue siendo limitado.
- **Conteo preciso**: "tres manzanas" puede salir con dos, cuatro o cinco. La red no "cuenta", aproxima.
- **Composición con múltiples sujetos**: "un perro a la izquierda y un gato a la derecha" — la separación espacial es frágil.
- **Sesgos heredados del dataset**: lo entrenado con **LAION-5B** refleja sesgos demográficos, culturales y estéticos de internet. Importante en aplicaciones médicas y sociales.
- **Costo de inferencia**: sigue siendo costoso para deployment masivo en tiempo real.
- Idea para cerrar la sección: Stable Diffusion es una herramienta muy poderosa pero falible. Saber dónde falla es tan importante como saber qué puede hacer.

**Slide 46 — TilTedTinder v2, Notebook y Cierre** (*Sección: SECCIÓN 5*)

**Slide 47 — Recap: el desafío que dejamos pendiente** **[SLIDE-IMAGEN]** — sin texto alguno en el markdown.
- Contenido rescatado de la figura: *"Volvamos al problema con el que arrancamos la Sección 3, ahora con todas las piezas en la mano:"*
- **El equipo de TilTedTinder quería pasar de:** *"Generá una persona inclinada cualquiera"* (lo que resolvía la GAN de la clase pasada).
- **A:** *"Generá una persona inclinada que coincida con esta descripción en texto libre"* (lo que ninguna GAN podía hacer).
- **Lo que ahora sabemos:**
  - Existe la **generación condicionada por texto** como tarea (Sección 3).
  - **Stable Diffusion** es la herramienta que la implementa, combinando **VAE + UNET + CLIP** (Sección 4).
  - El usuario escribe un prompt, CLIP lo entiende, la UNET talla la imagen denoising paso a paso, el VAE la decodifica.
- **El próximo paso**: traducir las preferencias reales de los usuarios a prompts concretos que el modelo pueda procesar.

**Slide 48 — De preferencias a prompts: ejemplos concretos** **[SLIDE-IMAGEN]** — sin texto alguno en el markdown.
- Contenido rescatado de la figura: *"El equipo de producto toma las preferencias documentadas y las convierte en prompts. Estos son los tres ejemplos del slide del nuevo desafío, ahora como prompts ejecutables:"*
- **Usuario A** — *"Me atraen las personas inclinadas, altas, con anteojos y pelo rizado."*
  ```
  prompt = "a tilted portrait of a tall person with round glasses and curly hair,
            soft natural lighting, photorealistic, 4k"
  ```
- **Usuario B** — *"Prefiero caras inclinadas, jóvenes, con sonrisa y barba corta."*
  ```
  prompt = "a tilted portrait of a young person with a warm smile and short beard,
            soft daylight, candid photo, shallow depth of field"
  ```
- **Usuario C** — *"Inclinadas, mayores, expresión seria, rasgos angulosos."*
  ```
  prompt = "a tilted portrait of an older person with a serious expression and angular features,
            dramatic shadows, black and white photography"
  ```
- **Patrón a observar**: un buen prompt para SD combina **sujeto + atributos + estilo + condiciones de luz**. La imagen final depende de esa estructura tanto como del modelo en sí. Aprender a escribir prompts es una habilidad propia — *prompt engineering*.
- **Y la pieza que falta**: usar el `seed` para fijar el perfil generado. Si el usuario "matchea" con un perfil, queremos poder reproducirlo idénticamente cuando vuelva a abrir la app. Mismo prompt + misma seed = mismo perfil estable.

**Slide 49 — Lo que el equipo va a encontrar al ejecutar esto** **[SLIDE-IMAGEN]** — sin texto alguno en el markdown.
- Contenido rescatado de la figura: *"Las limitaciones generales del slide anterior se vuelven concretas en este caso:"*
- **Stable Diffusion no conoce Slanted Land.** El dataset de entrenamiento (LAION-5B) no contiene fotos del universo inclinado. Las primeras generaciones probablemente saldrán como caras **rectas**, no inclinadas. Solución profesional: **fine-tuning** con las 4 fotos reales que tienen — técnicas como **DreamBooth** o **LoRA** permiten enseñarle a SD un concepto nuevo con muy pocas imágenes.
- **Sesgo demográfico heredado.** SD refleja sesgos del dataset: ciertos grupos demográficos están sobrerrepresentados, otros casi ausentes. El equipo va a tener que **auditar** las generaciones para no excluir poblaciones.
- **Control limitado a nivel de detalle.** No podés pedir *"exactamente esa nariz"*. Cada generación tiene variaciones inevitables. Para detalles finos hay que iterar — o usar herramientas más avanzadas (**ControlNet**, **Inpainting**).
- **Costo computacional.** Generar 50 perfiles personalizados por usuario, en tiempo real, es caro. El equipo va a tener que pensar en **caché de perfiles**, generación batched offline, o modelos más rápidos (**SDXL Turbo**, **FLUX Schnell**).
- **Consideración ética.** Generar personas que **no existen** para una app de citas plantea preguntas serias: ¿se le avisa al usuario que el perfil es sintético? ¿Hay riesgo de manipulación emocional? Decisiones de producto, no técnicas — pero hay que tomarlas.
- **Idea para llevarse**: Stable Diffusion les resuelve **el motor**. El producto final requiere muchas decisiones más — sobre datos, ética, cómputo y UX.

**Slide 50 — Pasamos al notebook** **[SLIDE-IMAGEN]** — sin texto alguno en el markdown.
- Contenido rescatado de la figura: *"Ahora pasamos a la práctica. Vamos a ejecutar Stable Diffusion en Google Colab."*
- **Stack:**
  - **Plataforma**: Google Colab con GPU (Tesla T4, 16GB).
  - **Librería**: 🤗 Hugging Face Diffusers.
  - **Modelo**: Stable Diffusion v1.4 (CompVis), en precisión `float16` para que entre en la GPU gratuita.
- **Lo que vamos a hacer:**
  1. **Pipeline alto nivel** — `StableDiffusionPipeline.from_pretrained(...)` y generar imágenes en pocas líneas.
  2. **Jugar con hiperparámetros** — `num_inference_steps`, `guidance_scale`, `seed` — y ver qué cambia en la imagen.
  3. **Generar grids** — múltiples imágenes de un mismo prompt para apreciar la variabilidad.
  4. **Cambiar dimensiones** — generar imágenes rectangulares (512×768).
  5. **Pipeline manual** — desarmar el pipeline en sus tres componentes (VAE + UNET + CLIP) y reconstruirlo a mano. Esto cierra el círculo conceptual de la clase: cada bloque que vimos en teoría aparece como código.
- **Punto importante**: el último ejercicio (pipeline manual) es donde **toda la Sección 4 se vuelve tangible**. Vas a ver el bucle de denoising, las cross-attention con el embedding de CLIP, y el VAE decodificando al final.

## Definitions and terminology

**Segmentación y sus variantes**
- **Segmentación** (slide 4): asignar una etiqueta a cada píxel de la imagen. La salida es una "máscara". Se contrasta con clasificación (una etiqueta por imagen) y detección (cajas con etiquetas). Frase del deck: "segmentar es darle un significado pixel por pixel a la imagen".
- **Máscara** (slide 9): internamente, una matriz del mismo tamaño que la imagen donde cada celda dice a qué clase pertenece ese píxel. Para 2 clases es 0/1; para N clases es 0..N-1.
- **Segmentación semántica** (slide 5): etiqueta cada píxel con su clase, sin distinguir individuos. Cinco autos comparten la misma etiqueta.
- **Segmentación de instancias** (slide 5): distingue cada objeto individual — "auto 1", "auto 2" — aunque sean de la misma clase.
- **Segmentación panóptica** (slide 5): combina ambas — clasifica cada píxel y distingue instancias. "La versión más completa".

**Arquitecturas de segmentación**
- **FCN — Fully Convolutional Network** (slides 11–12, Long et al. 2015): un clasificador de imágenes al que se le saca la capa densa final y se la reemplaza por convoluciones 1×1 + upsampling, para producir una salida espacial del mismo tamaño que la entrada. "Convertí un clasificador de imágenes en un clasificador de píxeles". Primer modelo de segmentación end-to-end con deep learning.
- **Convolución traspuesta** (slides 12, 15): la operación de upsampling aprendido, presentada como "la operación inversa al pooling".
- **U-Net / UNET** (slides 14–17, Ronneberger, Fischer y Brox — Universidad de Friburgo, 2015; paper *"U-Net: Convolutional Networks for Biomedical Image Segmentation"*): arquitectura simétrica encoder-decoder en forma de U.
  - **Encoder (camino contractivo)**: convoluciones + max pooling; en cada nivel las dimensiones espaciales se reducen a la mitad y los canales se duplican. "Qué hay" mejora, "dónde está" se pierde.
  - **Bottleneck**: la representación más comprimida y abstracta; donde vive la información semántica de alto nivel.
  - **Decoder (camino expansivo)**: convoluciones traspuestas; en cada nivel las dimensiones espaciales se duplican y los canales se reducen a la mitad.
  - **Skip connections**: conexión directa horizontal de cada nivel del encoder al nivel correspondiente del decoder; la salida del encoder se **concatena** con la entrada del decoder. Es la innovación que resuelve el borroneo de FCN, y el deck la llama además "un regularizador estructural" que permite entrenar con cientos y no miles de imágenes.
- **UNET como patrón arquitectónico** (slides 22, 41): sirve para cualquier tarea donde entrada y salida tengan el mismo tamaño espacial y haya que preservar detalle fino — restauración (denoising, deblurring, super-resolución), image-to-image translation (MRI → CT), y el denoiser de Stable Diffusion.

**SAM**
- **SAM — Segment Anything Model** (Meta, 2023; slides 18–21): foundation model masivo que segmenta cualquier cosa en cualquier imagen sin reentrenamiento. "SAM no aprende una tarea — aprende qué es un objeto, y deja que vos le digas cuál querés."
- **Segmentación promptable** (slide 18): el paradigma "foundation model + prompt en inferencia" traído desde NLP a la segmentación. El prompt puede ser un click, una caja, una máscara aproximada o (desde SAM 3) texto.
- **Image Encoder** (slide 20): ViT masivo; procesa la imagen una vez y produce un embedding rico. El deck lo cifra en "~95% del cómputo".
- **Prompt Encoder** (slide 20): liviano; convierte el prompt (punto, caja, texto) en un embedding compatible.
- **Mask Decoder** (slide 20): liviano; combina los dos embeddings y produce la máscara. El truco de diseño: codificar la imagen una sola vez y reejecutar solo el decoder para cada prompt nuevo — de ahí la sensación interactiva.
- **SA-1B** (slide 20): el dataset de Meta — 1.000 millones de máscaras sobre 11 millones de imágenes — construido con un *data engine* iterativo donde el propio SAM ayudaba a anotar, mejorando ronda tras ronda.
- **Timeline SAM** (slide 21): SAM 1 (Abril 2023, imágenes, prompts visuales) → SAM 2 (Julio 2024, video, módulo de memoria entre frames) → SAM 3 (Noviembre 2025, prompts de texto y vocabulario abierto) → SAM 3.1 (Marzo 2026, *Object Multiplex*: tracking conjunto multi-objeto con memoria compartida).

**Texto, embeddings y condición**
- **Tokenización** (slide 29): partir la oración en tokens (palabras o subpalabras). "Fotorrealista" puede partirse en "foto" + "realista".
- **Embedding de palabra** (slide 29): vector de cientos de dimensiones donde palabras de significado parecido quedan cerca.
- **Encoder contextual** (slide 29): un Transformer que procesa toda la secuencia y produce un embedding contextual de la oración completa, resolviendo ambigüedades tipo "banco de plaza" vs. "banco financiero".
- **CLIP — Contrastive Language–Image Pre-training** (OpenAI, 2021; slides 30, 42): dos encoders entrenados en paralelo — uno de imagen, uno de texto — de modo que sus salidas vivan en el mismo espacio vectorial. Entrenamiento contrastivo: pares reales cerca, pares mal apareados lejos. En SD 1.x el modelo concreto es **CLIP ViT-L/14 de OpenAI**, congelado, con salida de **77 × 768**.
- **Generación condicionada** (slide 31): `ruido aleatorio + condición → red → imagen que respeta la condición`, contra la incondicional `ruido aleatorio → red → imagen`. La condición puede ser etiqueta de clase (cGAN), imagen de referencia (Pix2Pix) o embedding de texto (Stable Diffusion). "La condición no es un input opcional al costado. Es lo que dirige cada paso."
- **Cross-attention** (slides 31, 41, 42): el mecanismo que inyecta el embedding de CLIP en cada nivel de la U (bajando y subiendo). En cada capa el modelo se pregunta *"dado lo que sé hasta acá, ¿qué partes del prompt son relevantes para guiar este nivel?"*.

**Difusión y Stable Diffusion**
- **Difusión** (slide 33): metáfora física — partículas que se dispersan hasta el desorden total, como una gota de tinta en agua.
- **Forward process** (entrenamiento, slide 33): agregar un poco de ruido gaussiano a una imagen real en cada paso, durante miles de pasos, hasta llegar a ruido puro.
- **Reverse process** (inferencia, slide 33): partir de ruido puro y quitar ruido paso a paso hasta que emerja una imagen.
- **Lo que la red aprende** (slide 33): dado un latente ruidoso y un timestep, predecir qué ruido fue agregado. Si sabe predecir el ruido, puede restarlo.
- **Diferencia con GANs** (slide 33): no hay competencia entre dos redes; una sola red aprende a desruidizar. Más estable de entrenar, sin mode collapse, más diversidad.
- **Difusión latente / Latent Diffusion** (slide 37, Rombach et al. 2021, *"High-Resolution Image Synthesis with Latent Diffusion Models"*, equipo CompVis): difundir en un espacio latente comprimido en lugar del espacio de píxeles.
- **VAE — Variational Autoencoder** (slides 38–40): la pieza de compresión-descompresión. Encoder: 512×512×3 → 64×64×4. Decoder: 64×64×4 → 512×512×3. Se entrena antes y por separado de la UNET, con el objetivo `decoder(encoder(imagen)) ≈ imagen`, y después queda congelado. En **inferencia solo se usa el decoder**. "Convierte el problema de generar 800K píxeles en el de generar 16K números latentes."
- **UNET de Stable Diffusion** (slide 41): misma estructura que la UNET de segmentación, distinta tarea. Entrada = (latente ruidoso, timestep, embedding de texto); salida = predicción del ruido presente en el latente.
- **Scheduler** (slides 41, 43): el componente que resta el ruido predicho del latente para producir un latente un poco menos ruidoso en cada iteración.
- **Classifier-free guidance / `guidance_scale`** (slide 44): qué tan estrictamente seguir el prompt. Default 7.5; bajo (1-3) diverso, medio (7-9) sweet spot, alto (15+) saturado.
- **`seed`** (slides 44, 48): controla el ruido inicial. Misma seed + mismo prompt = misma imagen.
- **LAION-5B** (slides 45, 49): el dataset de entrenamiento de Stable Diffusion, del que hereda sesgos demográficos, culturales y estéticos.
- **Fine-tuning de conceptos nuevos** (slide 49): **DreamBooth** y **LoRA** como técnicas para enseñarle a SD un concepto nuevo con muy pocas imágenes.
- **Herramientas de control fino** (slide 49): **ControlNet**, **Inpainting**.
- **Modelos rápidos** (slide 49): **SDXL Turbo**, **FLUX Schnell**.

## Evidence and examples

**Cifras y datos, con su slide de origen**
- **SA-1B: 1.000 millones de máscaras sobre 11 millones de imágenes** — slide 20 (texto) — el dataset con el que Meta entrenó SAM, construido con un data engine iterativo.
- **Image Encoder de SAM = ~95% del cómputo** — slide 20 (texto). Presentado como hecho, sin fuente.
- **CLIP: 400 millones de pares (imagen, descripción) de internet** — slide 30 (texto).
- **CLIP ViT-L/14, 123M parámetros** — slide 42 (texto) y slide 38 (tabla en imagen: "~123M params").
- **Tokenización de CLIP: 77 tokens; salida 77 × 768** — slide 42 (texto) y slide 43 (imagen, Paso 1).
- **Latente 64×64×4 = 16.384 valores** — slide 37 (texto), slide 39 (imagen), slide 43 (imagen, Pasos 2 y 4).
- **Imagen 512×512×3 = 786.432 valores** — slides 36 y 37 (texto).
- **"48× menos información"** — slide 37 (texto); repetido como "Compresión ~48×" en la imagen de la slide 39. La compresión espacial es 8× por lado (slide 37: "una compresión 8× preserva la información estructural"; slide 44: "múltiplos de 8 porque el VAE comprime 8×").
- **"generar 800K píxeles" → "generar 16K números latentes"** — slide 39 (imagen).
- **Tamaños de las tres redes de SD: VAE ~80M params · UNET ~860M params · CLIP Text Encoder ~123M params** — slide 38 (tabla dentro de la imagen). **Este es el único lugar del deck donde aparecen los tamaños del VAE y de la UNET**, y vive únicamente en una imagen.
- **Difusión en píxeles: 50 a 1000 pasos, GPUs de 40GB+, minutos por imagen** — slide 36 (texto). Presentado como hecho, sin fuente.
- **SD en GPU de consumo: GTX/RTX de 8-16GB, pocos segundos** — slide 37 (texto).
- **Defaults de generación: 50 pasos, guidance 7.5, 512×512** — slide 44 (texto). Complementos: por debajo de 20 pasos la calidad se degrada notoriamente; por encima de 100 las mejoras son marginales; height/width múltiplos de 8.
- **Bucle de denoising ~50 veces** — slide 41 (imagen, paso 4 del ciclo) y slide 43 (imagen, Paso 3).
- **Stack de la notebook: Google Colab, Tesla T4 16GB, Hugging Face Diffusers, Stable Diffusion v1.4 (CompVis), `float16`, grids, 512×768** — slide 50 (imagen).
- **"acelerando 10× o más la creación de datasets médicos"** — slide 21 (texto). Presentado como hecho, sin fuente.
- **"uno de los papers más citados de la última década en visión por computadora"** (U-Net) — slide 14 (texto). Sin cifra ni fuente.
- **TilTedTinder tenía solo 4 fotos reales** — slides 24 y 49 (imagen).

**Ejemplos y casos**
- **Aplicaciones genéricas** (slide 6): autos autónomos (separar carretera, peatones, semáforos, otros vehículos); imagen satelital (cobertura forestal, urbanización, cuerpos de agua); videoconferencia Zoom/Meet (separar persona del fondo en tiempo real); agricultura de precisión (zonas con plagas o estrés hídrico); edición de fotos ("Seleccionar sujeto" automático en Photoshop).
- **Aplicaciones médicas** (slide 7): neuroimagen MRI (tumores, lesiones de esclerosis múltiple, hipocampo); oncología CT/PET (volumen tumoral para planificar radioterapia); cardiología (ventrículos para calcular fracción de eyección); patología digital (células, núcleos, mitosis); oftalmología (vasos retinianos en diabetes e hipertensión); dermatología (lesiones para seguimiento y biopsia guiada).
- **El argumento clínico del borde** (slide 13): "un borde 2 píxeles más adentro o más afuera cambia el cálculo y puede cambiar la decisión clínica".
- **U-Net nació en un challenge de microscopía electrónica** con muy pocas imágenes etiquetadas (slide 14).
- **Ejemplos visuales de segmentación médica**: comparación LGE/SSFP con Single-image-type UNet vs. MI-UNet (slide 8, imagen); MRI cerebral con tumores marcados y sus áreas numéricas — `tumor,area:9392,size:163`, `tumor,area:23350,size:284`, `tumor,area:7190,size:138` (slide 9, imagen); grilla de infarto de miocardio con columnas *MI Image / Ground Truth Mask / Predicted Mask Overlay (Green) / Probability Heatmap* (slide 7, imagen).
- **Prompt de ejemplo recurrente**: "un astronauta montando un caballo" (slides 27, 42) — y en la figura de la slide 38 el diagrama embebido usa el mismo *User Prompt*: "an astronaut riding a horse".
- **Los tres prompts ejecutables de TilTedTinder v2** (slide 48, imagen) — ver `## Raw / preserved excerpts`.
- **Analogías del deck**: la tinta en el vaso de agua (difusión, slide 33); "Stable Diffusion no construye la imagen, la talla" y el "bloque de mármol" (slides 33 y 43); "el borde es el dato" (slide 17).

## Inconsistencies / open questions

**1. Hueco pedagógico mayor: 22 slides de segmentación sin una sola métrica de evaluación.**
La Sección 1 y la Sección 2 (slides 3 a 22, más las slides 4–9 de introducción) enseñan qué es segmentar, cómo se ve una máscara, FCN, U-Net, skip connections y SAM — pero **el deck nunca define cómo se mide la calidad de una segmentación**. Verificado por búsqueda sobre el texto completo: cero apariciones de *IoU*, *Jaccard*, *Hausdorff*, *métrica*, *accuracy*, *F1*, *precision*, *recall*. Las **dos únicas apariciones de la cadena "dice"** son el verbo español, no el coeficiente de Dice:
- Slide 9: "cada celda **dice** a qué clase pertenece ese píxel".
- Slide 31: "Si la condición **dice** 'perro en la playa'".

El hueco es más agudo porque el deck sí construye el argumento clínico que exigiría la métrica: la slide 13 afirma que "un borde 2 píxeles más adentro o más afuera cambia el cálculo y puede cambiar la decisión clínica", y la slide 21 distingue a UNET por producir salidas "clínicamente medibles y reproducibles" — pero nunca dice **con qué se mide**. La figura de la slide 8 compara dos modelos (Single-image-type UNet vs. MI-UNet) de manera puramente cualitativa, sin ningún número.

**2. Cifras presentadas como hechos, sin fuente.**
- *"Es el ~95% del cómputo"* (image encoder de SAM, slide 20). El reparto de cómputo entre image encoder y mask decoder no está publicado con esa cifra en el paper de SAM. El orden de magnitud es plausible — el encoder es un ViT masivo y el decoder es deliberadamente liviano — pero el número puntual es del deck, no de la literatura.
- *"acelerando 10× o más la creación de datasets médicos"* (slide 21). Sin estudio, dominio ni condición de medición.
- *"uno de los papers más citados de la última década en visión por computadora"* (U-Net, slide 14). Sin cifra de citas ni ranking de referencia.
- *"Se necesitan típicamente 50 a 1000 pasos"*, *"GPUs de 40GB+"*, *"minutos por imagen"* (slide 36). Presentado como las "cuentas" de la difusión en píxeles, pero sin fuente y sin decir a qué modelo/resolución corresponde.

**3. Riesgo de imprecisión: "CLIP ViT-L/14 de OpenAI (123M parámetros)" (slide 42, repetido en la tabla de la slide 38).**
123M es el conteo del **text encoder** de CLIP ViT-L/14, no del modelo CLIP completo (~428M parámetros contando también el image encoder ViT-L/14). En el contexto de Stable Diffusion la cifra es la correcta *en la práctica* — SD solo embarca el text encoder — pero la slide 42 la presenta atada al nombre del modelo completo ("CLIP ViT-L/14 de OpenAI (123M parámetros)"), lo que induce a leer 123M como el tamaño de CLIP. La tabla de la slide 38 está mejor formulada ("CLIP Text Encoder ~123M params"). Vale desambiguar en clase.

**4. La figura de la slide 18 no ilustra el modelo que la slide describe.**
El texto de la slide 18 presenta **SAM 1** (Meta, 2023) y su tríada image encoder / prompt encoder / mask decoder. La figura que acompaña es la arquitectura de **SAM 2**: incluye `Memory Attention`, `Memory Encoder` y `Memory Bank`, que son exactamente el módulo de memoria para video que la slide 21 recién introduce como la novedad de SAM 2 (Julio 2024). Además la figura tiene un emoji de corona 👑 dibujado sobre el bloque `Memory Attention` — un resalte del autor original de la figura, no de este deck. Un alumno que lea la figura junto al texto se lleva una arquitectura de SAM 1 con memoria de video, que no existe.

**5. La figura de la slide 21 contradice la tabla de la slide 21.**
La tabla del deck lista cuatro versiones, hasta **SAM 3.1 (Marzo 2026)** con *Object Multiplex*. La figura de la misma slide es una captura del sitio de Meta ("Evolution of SAM", con botón *Download the model*) que muestra **solo SAM 1, SAM 2 y SAM 3** — no hay SAM 3.1. La captura es evidentemente anterior a la fila que el deck agrega. Es la fila más nueva y la menos verificable del deck, y su propia ilustración no la respalda.

**6. La figura de la slide 28 contradice el texto de la slide 28 en fechas.**
El texto dice *"2021 · DALL·E 1 (OpenAI)"* y *"2022 · … Midjourney v1"*. La figura ("AI Image Model Timeline (2022-2026)") dice **"DALL-E — April 2022"** y **"Midjourney — July 2023 (v5)"**. Solo coinciden en *Stable Diffusion — August 2022*. La figura además agrega un hito que el texto no menciona: **"Nano Banana 2 — February 2026 — Upcoming Release"**. Texto e imagen cuentan dos cronologías distintas en la misma slide.

**7. La figura de la slide 9 no muestra lo que la slide 9 describe.**
El texto anuncia la progresión "Imagen original (MRI) → Máscara binaria del tumor (blanco = tumor, negro = no tumor) → Overlay". La figura muestra tres cortes axiales de MRI cerebral distintos, cada uno con una **caja de detección roja** y una etiqueta tipo `tumor,area:9392,size:163` — es decir, salidas de detección con overlay, no la secuencia original → máscara binaria → overlay. Justo en la slide donde el deck contrapone detección y segmentación, la ilustración usa cajas de detección.

**8. Sospecha de atribución: diagramas de terceros sin cita.**
Contra la sospecha planteada en el encargo, revisé cada figura buscando créditos o URLs embebidos. Resultado:
- **Crédito embebido, no citado en el deck**: la figura de la slide 34 lleva el logo y el nombre **"Calibraint"** (empresa de servicios de IA) impresos arriba a la izquierda. Es el único crédito visible en todo el set de imágenes.
- **Sin crédito visible pero de origen reconocible**:
  - Slide 38, diagrama embebido — es el diagrama de pipeline de Stable Diffusion que circula con el material de **Hugging Face / "The Illustrated Stable Diffusion"**: cajas `Latent Seed (Gaussian noise ~ N(0,1))`, `User Prompt "an astronaut riding a horse"`, `Frozen CLIP Text Encoder`, `Text conditioned latent UNet`, `Scheduler algorithm "reconstruct"`, `Variational Autoencoder Decoder`, `512×512 output image`, con el loop `repeat N scheduler steps`. Sin atribución.
  - Slide 19 — la figura de la tarea promptable ("cat with black ears") corresponde a la Figura 1 del paper **Segment Anything (Kirillov et al., 2023)**. Sin atribución.
  - Slide 18 — diagrama de arquitectura de **SAM 2**, con la corona sobrepuesta de la fuente original. Sin atribución.
  - Slide 12 — la figura de FCN es la del paper **Long, Shelhamer & Darrell (2015)**, con las etiquetas `forward/inference`, `backward/learning`, `pixelwise prediction`, `segmentation g.t.` y los anchos `96, 256, 384, 384, 256, 4096, 4096, 21`. Sin atribución (aunque el paper sí se cita en el texto de la slide 11).
  - Slide 35 — figura de paper de imagen médica con arquitectura Swin-transformer + "Fine-trained MDT". Sin atribución ni identificación del paper.
  - Slide 21 — captura del sitio web de Meta. Sin atribución.
  - Slide 30 — reproducción del diagrama de *Contrastive Pre-Training* de CLIP, con el ejemplo canónico `pepper the aussie pup` del paper de Radford et al. Sin atribución.
  - Slide 29 — la figura de aritmética de embeddings (Male-Female / Verb Tense / Country-Capital) es la figura clásica de **word2vec (Mikolov et al.)**. Sin atribución.
  - Slide 5 — figura de segmentación urbana (a) image / (b) semantic / (c) instance / (d) panoptic, del paper de **Panoptic Segmentation (Kirillov et al., 2019)** o derivada. Sin atribución.
- **Sí atribuido en el texto**: el paper de Rombach et al. 2021 (slide 37), el de Ronneberger et al. 2015 (slide 14), el de Long et al. 2015 (slide 11), CLIP de OpenAI 2021 (slide 30).
- **Conclusión**: el deck cita **papers** con razonable disciplina en el cuerpo del texto, pero **no atribuye ninguna figura**. Es un riesgo real para material de curso universitario que se distribuye.

**9. El manifiesto clasifica por tamaño y sobreestima el conteo de figuras.**
De las **31 imágenes marcadas `figura`** en su primera aparición, **26 tienen contenido real**. Las otras **5 son marcos de tarjeta vacíos** — rectángulo blanco con una barra roja de acento a la izquierda, sin texto ni gráfico: `slide-13-1.png`, `slide-13-3.png`, `slide-14-1.png`, `slide-14-3.png`, `slide-20-1.png`. Cada una tiene un gemelo con md5 distinto pero apariencia idéntica (`slide-13-2`, `slide-13-4`, `slide-14-2`, `slide-14-4`, `slide-20-2`), lo que da los 10 marcos que el deck usa como fondo de las tablas de dos columnas en las slides 13, 14 y 20. El conteo real de figuras con contenido es **26**, no 31.

**10. Desalineación entre la numeración conceptual de componentes y la numeración de slides.**
La slide 39 (solo imagen) es "Componente 1: el VAE" completo. La slide 40 lleva el mismo título "Componente 1: el VAE" en el markdown pero su cuerpo está vacío: es solo la figura de apoyo del autoencoder. La slide 41 (solo imagen) es "Componente 2: la UNET". La slide 42 es "Componente 3: el CLIP Text Encoder" — la única de las tres que tiene texto real en el markdown. Es decir: **de los tres componentes de Stable Diffusion, dos viven exclusivamente dentro de imágenes**. El título faltante de la slide 41 ("Componente 2: la UNET (¡acá vuelve!)") solo se recupera transcribiendo la figura.

**11. Otras observaciones menores.**
- La slide 21 tiene una etiqueta de sección anómala: `Sección: SAM 3.1`, en medio de la Sección 1. Las demás secciones son "SECCIÓN 1" a "SECCIÓN 5". Parece un residuo de edición.
- Las slides 8 y 19 repiten el título de la slide anterior (7 y 18 respectivamente) sin marcar que son continuación.
- La slide 15 no tiene título en la estructura del deck; el título "La arquitectura en U" aparece como primer párrafo en negrita del cuerpo. Lo mismo en las slides 19, 21, 30 y 35.
- La slide 37 fecha el paper de Rombach et al. en 2021 (el preprint de arXiv es de diciembre de 2021; la publicación en CVPR es de 2022). No es un error, pero conviene saberlo si alguien lo busca por la cita de CVPR.
- El deck se apoya en las clases previas sin recapitular: "Slanted Land", "TilTedTinder", la Vanilla GAN, la cGAN y StyleGAN se dan por vistas en la clase 8.
- **Pregunta abierta**: no hay ninguna slide sobre cómo se **evalúa** una imagen generada (FID, CLIP score) — el mismo hueco de métricas que en segmentación se repite en generación. La slide 45 lista limitaciones cualitativas, pero nada cuantitativo.

## Images / diagrams

46 imágenes únicas por md5. Cada una descrita **una sola vez, en su `primera_aparicion`**; las reapariciones se anotan en la entrada correspondiente. Los 68 archivos en disco (26 `.jpg`, 27 `.png`, 15 `.svg`) más `_manifest.json` están copiados en la carpeta compañera.

**Nota sobre los `.svg`**: 15 archivos `.svg` son los originales vectoriales detrás de PNGs rasterizados (slides 6, 13, 14, 20). Están copiados a la carpeta compañera pero, por instrucción del encargo, no se abrieron. Su contenido es el mismo que el del PNG hermano.

### Figuras con contenido real (26)

**`AIG4B-Clase-9-Segmentacion-y-Stable-Diffusion.md/images/slide-04-1.jpg`** — slide 4 · `figura` · 659×312 px
- **Depiction**: cuadrícula 2×2 sobre la misma foto de un perro pastor y tres ovejas en un campo. Arriba izq. **Image Recognition**: recuadro con probabilidades `P 0.6 sheep / P 0.3 dog / P 0.1 cat / P 0.0 horse`. Arriba der. **Semantic Segmentation**: el perro en rojo sólido, las tres ovejas todas en el mismo azul. Abajo izq. **Object Detection**: cajas de color — roja sobre el perro, azul/celeste/verde-agua sobre cada oveja. Abajo der. **Instance Segmentation**: perro en rojo, y cada oveja en un color distinto (azul, celeste, verde-agua).
- **Why it matters**: es la figura que sostiene toda la tabla clasificación/detección/segmentación de la slide 4, y de paso adelanta la distinción semántica vs. instancias de la slide 5.
- **Transcribed text**: `P 0.6 sheep` · `P 0.3 dog` · `P 0.1 cat` · `P 0.0 horse` · `Image Recognition` · `Semantic Segmentation` · `Object Detection` · `Instance Segmentation`

**`.../slide-05-1.jpg`** — slide 5 · `figura` · 742×405 px
- **Depiction**: cuadrícula 2×2 sobre una escena urbana (cruce con taxis, peatones, semáforos, edificios). (a) la foto original; (b) máscara semántica de colores planos — calle violeta, edificios gris, vegetación verde, autos azul, personas rojo; (c) máscara de instancias sobre fondo negro, cada vehículo y cada persona en un color propio, con cajas finas; (d) máscara panóptica que combina el fondo semántico con las instancias coloreadas individualmente.
- **Why it matters**: es la ilustración canónica de los tres niveles de granularidad de la slide 5, incluida la panóptica que el texto define pero no ejemplifica.
- **Transcribed text**: `(a) image` · `(b) semantic segmentation` · `(c) instance segmentation` · `(d) panoptic segmentation`

**`.../slide-07-2.jpg`** — slide 7 · `figura` · 467×467 px
- **Depiction**: grilla de 4 filas × 4 columnas de resultados de segmentación cardíaca. Cada fila es un caso distinto. Columnas: MRI en escala de grises (corte de eje corto del ventrículo izquierdo); máscara binaria blanca en forma de media luna sobre fondo negro; la MRI con la predicción superpuesta en verde; y un mapa de calor azul-a-rojo de la probabilidad por píxel.
- **Why it matters**: materializa las tres representaciones que la slide 9 describirá (original, máscara binaria, overlay) y agrega una cuarta — el heatmap de probabilidad — que el deck nunca menciona en texto. Es también el mejor ejemplo visual de "la máscara es lo que se mide".
- **Transcribed text**: `MI Image` · `Ground Truth Mask` · `Predicted Mask Overlay (Green)` · `Probability Heatmap` (repetidos en las 4 filas)

**`.../slide-08-1.jpg`** — slide 8 · `figura` · 801×532 px · **slide íntegramente imagen**
- **Depiction**: grilla 2 filas × 3 columnas. Filas rotuladas a la izquierda **LGE** y **SSFP** (dos secuencias de MRI cardíaca). Columnas: **Input** (MRI cruda, corte de eje corto), **Single image type UNet** y **MI-UNet** (ambas con la segmentación superpuesta). Tres estructuras por color: azul/violeta = cavidad del ventrículo izquierdo, verde = miocardio (anillo), rojo = ventrículo derecho. En la columna del medio el rojo se desborda hacia arriba de forma difusa; en MI-UNet queda más contenido y con borde limpio.
- **Why it matters**: **es todo el contenido de la slide 8** — el markdown no tiene una sola línea de texto. Es también la única comparación cabeza a cabeza entre dos arquitecturas de segmentación en todo el deck, y es puramente cualitativa: no hay ninguna métrica que respalde que MI-UNet es mejor (ver `Inconsistencies`, punto 1).
- **Transcribed text**: `Input` · `Single image type UNet` · `MI-UNet` · `LGE` · `SSFP`

**`.../slide-09-1.jpg`** — slide 9 · `figura` · 927×334 px
- **Depiction**: tres cortes axiales de MRI cerebral, lado a lado, cada uno de un paciente distinto. En cada uno, una región tumoral sombreada en rojo translúcido, encerrada en una caja de detección roja con una etiqueta roja de texto arriba.
- **Why it matters**: es la ilustración de "cómo se ve una salida", pero muestra detección con overlay en lugar de la progresión original → máscara binaria → overlay que el texto describe (ver `Inconsistencies`, punto 7). Los números de área son el ejemplo más concreto del deck de "la máscara es lo que se mide".
- **Transcribed text**: `tumor,area:9392,size:163` · `tumor,area:23350,size:284` · `tumor,area:7190,size:138`

**`.../slide-12-1.jpg`** — slide 12 · `figura` · 695×318 px
- **Depiction**: diagrama isométrico clásico de FCN. A la izquierda una foto de dos gatos sobre un sofá. A la derecha una serie de prismas rectangulares que se estrechan, rotulados por debajo con los anchos de canal. Al final, dos planos: la predicción y el ground truth (gatos en violeta y marrón sobre fondo verde). Dos flechas horizontales arriba marcan los sentidos de propagación.
- **Why it matters**: es la figura original del paper de Long et al. (2015) que la slide 11 sí cita en el texto, aunque la figura no lleva atribución. Sostiene los tres pasos conceptuales de la slide 12: encoder, conv 1×1, upsampling.
- **Transcribed text**: `forward/inference` · `backward/learning` · `pixelwise prediction` · `segmentation g.t.` · anchos de canal: `96` · `256` · `384` · `384` · `256` · `4096` · `4096` · `21` · `21`

**`.../slide-15-1.jpg`** — slide 15 · `figura` · 603×325 px
- **Depiction**: la arquitectura U-Net dibujada literalmente en forma de U con bloques azules apilados de a pares. Rama izquierda descendente con flechas azul oscuro `Maxpooling2D`; punto inferior; rama derecha ascendente con flechas verdes `Conv. Transpose`. Cuatro flechas horizontales azul claro rotuladas `Concatenate` cruzan de un lado al otro, más una quinta en el bottleneck. Entrada a la izquierda: micrografía en escala de grises con grietas/bordes; salida a la derecha: máscara binaria blanco-sobre-negro de esa misma red de grietas. Llaves inferiores marcan `Encoder` y `Decoder`.
- **Why it matters**: es el diagrama que sostiene toda la slide 15 y buena parte de la 16, e incluye los anchos de filtro por nivel que el texto nunca da (64 → 128 → 256 → 512 → 1024 y de vuelta).
- **Transcribed text**: `Input` · `Prediction` · `3x3 Convolutionx2 64 filters` · `3x3 Convolutionx2 128 Filters` · `3x3 Convolutionx2 256 Filters` · `3x3 Convolutionx2 512 Filters` · `3x3 Convolutionx2 1024 Filters` · `3x3 Convolutionx2 512 Filters` · `3x3 Convolutionx2 256 Filters` · `3x3 Convolutionx2 128 Filters` · `3x3 Convolutionx2 64 Filters` · `Maxpooling2D` (×4) · `Conv. Transpose` (×4) · `Concatenate` (×5) · `Encoder` · `Decoder`

**`.../slide-16-1.jpg`** — slide 16 · `figura` · 706×276 px
- **Depiction**: otra vista de la U, esta vez con los bloques dibujados como láminas verticales apiladas y con las **resoluciones espaciales** rotuladas en lugar de los filtros. Entrada a la izquierda: foto de una calle; salida a la derecha: máscara semántica de colores planos. Cuatro conexiones de salto dibujadas como líneas grises que suben, cruzan horizontalmente y bajan con una punta de flecha sobre los bloques verdes del decoder. Leyenda de tres colores abajo.
- **Why it matters**: es la figura que hace visible el argumento central de la slide 16 — las skip connections como puentes horizontales — y da la escala numérica de la compresión que el texto describe en prosa (224×224 → 14×14 → 224×224).
- **Transcribed text**: `224×224` · `112×112` · `56×56` · `28×28` · `14×14` · `14×14` · `28×28` · `56×56` · `112×112` · `224×224` · `Convolution Layer` · `Max Pooling Layer` · `Concatenate Layer`

**`.../slide-18-1.jpg`** — slide 18 · `figura` · 754×301 px
- **Depiction**: diagrama de bloques de flujo izquierda-a-derecha. Un stack de frames de video (una jirafa en la sabana) entra a un trapecio azul `Image Encoder`; sigue una caja amarilla redondeada `Memory Attention` con un **emoji de corona dorada 👑** superpuesto arriba; luego una caja verde `Mask Decoder`, alimentada desde abajo por un trapecio naranja `Prompt Encoder` con tres cuadros de ejemplo (`clicks` con un punto rojo y dos verdes, `box` con un rectángulo, `masks` con una mancha azul). La salida son frames con la jirafa segmentada en blanco sobre negro, que entran a un trapecio azul `Memory Encoder` → cubos apilados `Memory` → un cilindro amarillo `Memory Bank`, que cierra el loop con una flecha azul gruesa de vuelta hacia `Memory Attention`.
- **Why it matters**: **es la arquitectura de SAM 2, no la de SAM 1 que describe la slide** (ver `Inconsistencies`, punto 4). Como material técnico es valiosa — es el mejor diagrama del deck sobre cómo funciona la memoria entre frames — pero está colocada dos slides antes de que el deck introduzca SAM 2.
- **Transcribed text**: `Image Encoder` · `Memory Attention` · `Mask Decoder` · `Prompt Encoder` · `clicks` · `box` · `masks` · `Memory Encoder` · `Memory` · `Memory Bank`

**`.../slide-19-1.jpg`** — slide 19 · `figura` · 706×526 px · **slide íntegramente imagen** (solo título)
- **Depiction**: diagrama de la tarea de segmentación promptable, de abajo hacia arriba. En la base, a la izquierda, cuatro recuadros agrupados bajo una llave rotulada `segmentation prompt`: (1) un punto rojo y dos verdes sobre fondo blanco; (2) un rectángulo vacío (bounding box); (3) una mancha azul difusa (máscara aproximada); (4) el texto `cat with black ears`. A la derecha, un recuadro rotulado `image` con la foto de dos gatos blancos junto a una maceta gris. Ambas ramas suben con flechas a una caja amarilla ancha rotulada `model`, de la que sale una flecha hacia `valid mask`: la misma foto con el gato de la derecha pintado en azul sólido.
- **Why it matters**: **es todo el contenido de la slide 19** más allá del título repetido. Es la mejor ilustración del deck de la idea central de SAM — cuatro tipos de prompt intercambiables, un solo modelo, una máscara válida — incluyendo el prompt de texto que el deck atribuye a SAM 3. Corresponde a la Figura 1 del paper *Segment Anything* (Kirillov et al., 2023), sin atribución.
- **Transcribed text**: `valid mask` · `model` · `segmentation prompt` · `cat with black ears` · `image`

**`.../slide-21-1.jpg`** — slide 21 · `figura` · 478×347 px
- **Depiction**: captura de pantalla de una página web de Meta. Encabezado: un eyebrow azul `ENHANCED CAPABILITIES` sobre el título `Evolution of SAM`, con un párrafo descriptivo a la derecha. Debajo, tres tarjetas con video (pingüinos caminando en una playa, con distintos individuos resaltados en magenta, naranja y cian, cada tarjeta con un botón de pausa). Tarjeta 1 (resaltada en celeste): **SAM 3**, con un campo de búsqueda superpuesto sobre el video que dice `Penguin`. Tarjeta 2: **SAM 2**. Tarjeta 3: **SAM 1**. Cada tarjeta lista sus capacidades con checks verdes. La tarjeta de SAM 3 termina en un botón azul `Download the model`.
- **Why it matters**: **la captura solo llega hasta SAM 3 — no muestra SAM 3.1**, la fila que la tabla de la misma slide presenta como la novedad de Marzo 2026 (ver `Inconsistencies`, punto 5). Además es la única fuente del deck sobre qué capacidades exactas suma cada versión, en las palabras de Meta.
- **Transcribed text**: `ENHANCED CAPABILITIES` · `Evolution of SAM` · `The Segment Anything models build on each other, offering increasingly advanced capabilities for developers and researchers to create, experiment and uplevel media workflows.` · `Penguin` · `SAM 3` — `Detect, segment and track every example of any object category in an image or video, using text or examples` — `Segment an object from a click` / `Track segmented objects in videos` / `Refine prediction with follow up clicks` / `Detect and segment matching instances from text` / `Refine detection with visual examples` · `Download the model` · `SAM 2` — `Segment and track any object in any image or video using click, box or mask prompts` — `Segment an object from a click` / `Track segmented objects in videos` / `Refine prediction with follow up clicks` · `SAM 1` — `Segment any object in any image with as little as a single click` — `Segment an object from a click` / `Refine prediction with follow up clicks`

**`.../slide-28-2.jpg`** — slide 28 · `figura` · 612×341 px
- **Depiction**: infografía de línea de tiempo horizontal sobre fondo crema, titulada `AI Image Model Timeline (2022-2026)`. Un eje azul con marcas de año de 2022 a 2026. Cuatro tarjetas blancas redondeadas con icono a la izquierda: **DALL-E · April 2022** (icono de grafo/pincel), **Stable Diffusion · August 2022** (icono de nube con flecha, colgando por debajo del eje), **Midjourney · July 2023 (v5)** (icono de velero), y **Nano Banana 2 · February 2026** (icono de molinete, tarjeta resaltada con glow azul y una etiqueta `Upcoming Release`).
- **Why it matters**: contradice el texto de su propia slide en las fechas de DALL·E y Midjourney, y agrega un hito (Nano Banana 2) que el texto no menciona (ver `Inconsistencies`, punto 6).
- **Transcribed text**: `AI Image Model Timeline (2022-2026)` · `DALL-E` `April 2022` · `Stable Diffusion` `August 2022` · `Midjourney` `July 2023 (v5)` · `Nano Banana 2` `February 2026` `Upcoming Release` · `2022` `2023` `2024` `2025` `2026`

**`.../slide-29-2.jpg`** — slide 29 · `figura` · 659×254 px
- **Depiction**: tres diagramas de ejes 3D lado a lado, con puntos de colores y flechas punteadas que conectan pares. Panel 1 **Male-Female**: `man → woman`, `king → queen`, ambas flechas paralelas. Panel 2 **Verb Tense**: `walking → walked`, `swimming → swam`, paralelas. Panel 3 **Country-Capital**: nueve pares país→capital (`Turkey → Ankara`, `Canada → Ottawa`, `Spain → Madrid`, `Italy → Rome`, `Germany → Berlin`, `Russia → Moscow`, `Japan → Tokyo`, `Vietnam → Hanoi`, `China → Beijing`), todas las flechas apuntando en la misma dirección.
- **Why it matters**: es la ilustración del punto 02 de la slide 29 ("palabras de significado parecido están cerca"), y va más allá del texto: muestra que las *relaciones* son direcciones consistentes en el espacio, no solo que las palabras similares se agrupan. Es la figura clásica de word2vec (Mikolov et al.), sin atribución.
- **Transcribed text**: `man` `woman` `king` `queen` `Male-Female` · `walking` `walked` `swimming` `swam` `Verb Tense` · `Turkey` `Ankara` `Canada` `Ottawa` `Spain` `Madrid` `Italy` `Rome` `Germany` `Berlin` `Russia` `Moscow` `Japan` `Tokyo` `Vietnam` `Hanoi` `China` `Beijing` `Country-Capital`

**`.../slide-30-1.jpg`** — slide 30 · `figura` · 545×367 px
- **Depiction**: diagrama sobre fondo verde menta titulado `Contrastive Pre-Training`. Arriba a la izquierda, un stack de tarjetas violetas con el texto `pepper the aussie pup` entra a un trapecio naranja `Text Encoder`, cuya salida se despliega en una fila de cajas naranjas `T₁ T₂ T₃ ... T_N`. Abajo a la izquierda, un stack de fotos de un labrador negro entra a un trapecio verde `Image Encoder`, cuya salida es una columna de cajas verdes `I₁ I₂ I₃ ⋮ I_N`. El cruce forma una matriz de similitudes `Iᵢ·Tⱼ` donde **la diagonal está resaltada en azul** (`I₁·T₁`, `I₂·T₂`, `I₃·T₃`, `I_N·T_N`) y el resto queda en crema.
- **Why it matters**: es la figura que hace concreto el entrenamiento contrastivo de la slide 30 — la diagonal azul *es* "los pares reales deben quedar cerca" y las celdas crema *son* "los pares mal apareados deben quedar lejos". Reproduce el diagrama del paper de CLIP (Radford et al., 2021), incluido el ejemplo `pepper the aussie pup`, sin atribución.
- **Transcribed text**: `Contrastive Pre-Training` · `pepper the aussie pup` · `Text Encoder` · `Image Encoder` · `T₁ T₂ T₃ ... T_N` · `I₁ I₂ I₃ ⋮ I_N` · celdas `I₁·T₁` `I₁·T₂` `I₁·T₃` ... `I_N·T_N`

**`.../slide-33-1.jpg`** — slide 33 · `figura` · 706×239 px
- **Depiction**: diagrama de dos bandas horizontales. Banda gris superior, **Forward Diffusion Process**, con la fórmula `q(x_t | x_{t-1})` y una caja amarilla `Noise Schedule`; flechas hacia la derecha entre círculos azules `x₀ → ... → x_{t-1} → ... → x_t → ... → x_T`; en el extremo derecho, `x_T ~ N(0, I)`. Banda verde inferior, **Reverse Denoising Diffusion Process**, con la fórmula `p_θ(x_{t-1} | x_t, c)` y una caja amarilla `Conditional Noise Predictor`; flechas hacia la izquierda entre los mismos círculos. Desde abajo, una flecha rotulada `condition : c` entra al predictor y se ramifica hacia ambos extremos del proceso inverso.
- **Why it matters**: es la única formalización matemática de la difusión en todo el deck — `q(x_t|x_{t-1})`, `p_θ(x_{t-1}|x_t, c)`, `x_T ~ N(0,I)` — y además ya introduce la **condición `c`** que el deck recién desarrolla en la slide 41. Conecta la slide 31 (condición) con la 33 (difusión) visualmente.
- **Transcribed text**: `Forward Diffusion Process` · `q(x_t|x_{t-1})` · `Noise Schedule` · `x_T ~ N(0, I)` · `x₀` `x_{t-1}` `x_t` `x_T` · `Reverse Denoising Diffusion Process` · `p_θ(x_{t-1}|x_t, c)` · `Conditional Noise Predictor` · `condition : c`

**`.../slide-34-1.jpg`** — slide 34 · `figura` · 942×357 px · **slide íntegramente imagen**
- **Depiction**: lámina sobre fondo rosa pálido titulada **Reverse / Denoising process**. Subtítulo gris: `Sample noise p_T(x_T) → turn into data`. Una flecha roja gruesa apunta a la derecha sobre una tira de ocho miniaturas cuadradas de un golden retriever, que van de ruido de color puro (izquierda) a la foto perfectamente nítida del perro (derecha). A la izquierda, la fórmula `p_T(x_T) ~ N(0, I)` y la etiqueta en negrita cursiva *Pure noise*; a la derecha, `p_0(x_0)` y *Clean sample*. Bajo la tira: `X_T`, `X_{T-1}`, ..., `X_1`, `X_0`.
- **Why it matters**: **es todo el contenido de la slide 34** — el markdown no tiene texto. Es la ilustración más directa del "reverse process" de la slide 33 y la que hace visible que la imagen *emerge* gradualmente del ruido. **Lleva un crédito embebido — el logo y el nombre `Calibraint` arriba a la izquierda — que el deck no cita en ninguna parte** (ver `Inconsistencies`, punto 8).
- **Transcribed text**: `Calibraint` · `Reverse / Denoising process` · `Sample noise p_T(x_T) → turn into data` · `p_T(x_T) ~ N(0, I)` · `Pure noise` · `X_T` · `X_{T-1}` · `X_1` · `X_0` · `p_0(x_0)` · `Clean sample`

**`.../slide-35-1.jpg`** — slide 35 · `figura` · 706×530 px · **slide íntegramente imagen** (solo título)
- **Depiction**: figura de paper de cinco paneles separados por líneas de guiones, sobre cortes axiales de CT/MRI de pelvis.
  - **a) Diffusion process**: fila de imágenes médicas de `X₀` (nítida) a `X_T` (ruido puro), con una flecha verde gruesa **Forward diffusion** hacia la derecha arriba y una flecha amarilla gruesa **Reverse diffusion** hacia la izquierda abajo.
  - **b) Network architecture**: `X_t` entra a una hilera de bloques de colores dentro de un panel celeste, con anchos de canal rotulados arriba: `64, 128, 128, 128, 256, 512, 512, 512, 512, 512, 512, 512, 256, 256, 128, 128`. Salen dos cabezas en cajas blancas — `Noise ε_θ` y `Variance coeff v_t` — que convergen en `X_{t-1}`. Una barra amarilla horizontal rotulada `Timestep t` alimenta todos los bloques desde abajo.
  - **c) Swin-transformer layer** (panel verde) y **d) Convolutional layer** (panel amarillo): detalle interno, ambos con una caja `Time embedding` arriba y una cadena de bloques con nodos ⊕.
  - **e) Image generation**: flecha naranja gruesa `Image generation`; secuencia `New X_T` → `Fine-trained MDT` → `New X_{T-1}` → `Fine-trained MDT` → `New X_{T-2}` → `......` → `New X₀`, con las miniaturas pasando de ruido gris a un corte anatómico limpio.
- **Why it matters**: **es todo el contenido de la slide 35**. Es la única figura del deck que muestra difusión aplicada específicamente a **imagen médica**, y la única que expone el interior de un denoiser con sus dos cabezas de salida (ruido + coeficiente de varianza) y la inyección del timestep. Sin atribución ni identificación del paper de origen.
- **Transcribed text**: `a) Diffusion process` · `Forward diffusion` · `Reverse diffusion` · `X₀ X₁ X₂ ... X_{T-2} X_{T-1} X_T` · `b) Network architecture` · `X_t` · `X_{t-1}` · `Noise ε_θ` · `Variance coeff v_t` · `Timestep t` · anchos `64 128 128 128 256 512 512 512 512 512 512 512 256 256 128 128` · `c) Swin-transformer layer` · `d) Convolutional layer` · `Time embedding` · `e) Image generation` · `Image generation` · `New X_T` · `Fine-trained MDT` · `New X_{T-1}` · `New X_{T-2}` · `New X₀` · leyenda: `: Up/down-sample Convolutional layer` · `: Up/down/no-sample Swin-transformer layer` · `: Linear layer` · `: Swin layer` · `: Up/down 3x3x3 Convolutional layer` · `: 3x3 Convolutional layer` · `---→ : Shortcut connection` · `-·-→ : Residual connection` · `⊕ : Addition`

**`.../slide-38-1.jpg`** — slide 38 · `figura` · 864×486 px · **slide íntegramente imagen**
- **Depiction**: captura de una slide completa titulada **"Las tres piezas de Stable Diffusion"**, con texto corrido, una tabla de tres columnas y, abajo al centro, un diagrama de pipeline embebido en un recuadro gris. El diagrama, de arriba hacia abajo: `Latent Seed / Gaussian noise ~ N(0,1)` → cuadro amarillo `64×64 latents`; en paralelo a la derecha, `User Prompt / "an astronaut riding a horse"` → caja violeta `Frozen CLIP Text Encoder` → cuadro celeste `77×768 text embeddings`. Ambos convergen en una caja amarilla grande `Text conditioned latent UNet`; su salida baja a `64×64 conditioned latents`; una caja rosa a la izquierda, `Scheduler algorithm "reconstruct"`, cierra un loop de vuelta hacia arriba rotulado `repeat N scheduler steps`. Del latente condicionado se baja a un pentágono verde `Variational Autoencoder Decoder` y de ahí al `512×512 output image` — la miniatura del astronauta a caballo.
- **Why it matters**: **es todo el contenido de la slide 38, y es la pieza más importante del deck que vive solo en una imagen.** La tabla de tres columnas es **el único lugar donde aparecen los tamaños del VAE (~80M) y de la UNET (~860M)**; sin transcribirla, esas cifras se pierden por completo. El diagrama embebido es además el mapa de conexiones que la slide 43 después narra en prosa. El diagrama corresponde al material de Hugging Face / "The Illustrated Stable Diffusion", sin atribución.
- **Transcribed text**: `Las tres piezas de Stable Diffusion` · `Antes de meternos en cada componente, fijemos el mapa completo. Stable Diffusion tiene tres redes que trabajan juntas:` · tabla `Componente | Qué hace | Tamaño aprox.` → `VAE (Variational Autoencoder) | Comprime imagen ↔ latente | ~80M params`; `UNET | Denoiser condicional en espacio latente | ~860M params`; `CLIP Text Encoder | Prompt de texto → embedding | ~123M params` · `Cómo se conectan: el prompt entra al CLIP, que produce un embedding. El UNET usa ese embedding para guiar el denoising en el espacio latente. Cuando termina, el VAE Decoder transforma el latente final en una imagen visible.` · `Punto importante para llevarse: dos de estas piezas — UNET y CLIP — ya las vimos. UNET la vimos en segmentación (Sección 2), CLIP en text-to-image (Sección 3). Solo nos queda entender el VAE y cómo se orquestan.` · diagrama: `Latent Seed` `Gaussian noise ~ N(0,1)` · `User Prompt` `"an astronaut riding a horse"` · `64×64 latents` · `Frozen CLIP Text Encoder` · `77×768 text embeddings` · `Text conditioned latent UNet` · `Scheduler algorithm "reconstruct"` · `repeat N scheduler steps` · `64×64 conditioned latents` · `Variational Autoencoder Decoder` · `512×512 output image`

**`.../slide-39-1.jpg`** — slide 39 · `figura` · 864×486 px · **slide íntegramente imagen**
- **Depiction**: captura de una slide completa titulada **"Componente 1: el VAE"**, con texto corrido y viñetas, y abajo un diagrama esquemático: un cuadrado negro con un `2` manuscrito blanco rotulado `Original input` → flecha → caja blanca `Encoder` → flecha → una tira vertical de celdas blancas y negras rotulada `Compressed representation` → flecha → caja blanca `Decoder` → flecha → un cuadrado negro con un `2` borroso rotulado `Reconstructed input`.
- **Why it matters**: **es todo el contenido de la slide 39.** Contiene la definición operativa completa del VAE — las dos mitades con sus dimensiones exactas, la asimetría entrenamiento/inferencia (encoder solo en entrenamiento, **decoder solo en inferencia**), el objetivo `decoder(encoder(imagen)) ≈ imagen` y el congelamiento de pesos. Nada de esto está en ninguna otra parte del deck.
- **Transcribed text**: `Componente 1: el VAE` · `VAE — Variational Autoencoder. Es la pieza que se encarga de la compresión-descompresión entre píxeles y espacio latente.` · `Dos mitades:` · `Encoder: toma la imagen 512×512×3 y la mapea a un latente 64×64×4. Compresión ~48×.` · `Decoder: toma un latente 64×64×4 y reconstruye una imagen 512×512×3.` · `Cuándo se usa cada parte:` · `Durante entrenamiento de SD: se usa el encoder — para llevar las imágenes reales del dataset al espacio latente, donde la UNET aprende a desruidizar.` · `Durante inferencia (lo que nos interesa hoy): solo se usa el decoder — para tomar el latente final ya desruidizado y reconstruir la imagen visible.` · `Cómo se entrena: el VAE se entrena antes y por separado de la UNET. Su objetivo es simple: que decoder(encoder(imagen)) ≈ imagen. Una vez entrenado, sus pesos quedan congelados.` · `Frase corta: el VAE es un compresor inteligente — convierte el problema de "generar 800K píxeles" en el problema de "generar 16K números latentes".` · diagrama: `Original input` · `Encoder` · `Compressed representation` · `Decoder` · `Reconstructed input`

**`.../slide-40-1.jpg`** — slide 40 · `figura` · 942×407 px · **slide con título pero cuerpo vacío**
- **Depiction**: diagrama esquemático de autoencoder variacional, horizontal. De izquierda a derecha: un rectángulo blanco alto de borde negro con una `x` en negrita, bajo la llave **Input**; flecha; un rectángulo verde alto, `...`, un rectángulo verde más bajo, bajo la llave **Encoder**; flecha; un rectángulo rojo con una **curva de campana gaussiana** dibujada dentro, bajo la llave **Latent Space**; flecha; un rectángulo azul bajo, `...`, un rectángulo azul alto, bajo la llave **Decoder**; flecha; un rectángulo blanco alto con `x'`, bajo la llave **Output**.
- **Why it matters**: es la única figura del deck que representa explícitamente lo *variacional* del VAE — la campana gaussiana en el espacio latente indica que el latente es una distribución, no un punto fijo. El texto del deck nunca menciona ese detalle: la slide 39 solo habla de compresión. El estrechamiento y ensanchamiento progresivo de los bloques es la representación visual del cuello de botella.
- **Transcribed text**: `x` · `x'` · `Input` · `Encoder` · `Latent Space` · `Decoder` · `Output`

**`.../slide-41-1.jpg`** — slide 41 · `figura` · 864×486 px · **slide íntegramente imagen**
- **Depiction**: captura de una slide completa de texto, titulada **"Componente 2: la UNET (¡acá vuelve!)"**, con secciones en negrita, dos viñetas de contraste y una lista numerada de cuatro pasos. Sin gráficos.
- **Why it matters**: **es todo el contenido de la slide 41 — incluido su título, que el markdown perdió por completo.** Es la slide más importante de la Sección 4: define la diferencia de tarea entre la UNET de segmentación y la de SD, explica el mecanismo de cross-attention con la pregunta literal que se hace el modelo en cada capa, y da el ciclo de denoising en cuatro pasos. Es también donde el deck cierra su arco narrativo (2015 microscopía → hoy generación).
- **Transcribed text**: `Componente 2: la UNET (¡acá vuelve!)` · `Esta es la pieza central de Stable Diffusion — y es la misma estructura que vimos en Sección 2 para segmentación.` · `Arquitectura: encoder + decoder con forma en U + skip connections. Idéntica a UNET de segmentación.` · `Pero la tarea es distinta:` · `UNET de segmentación: entrada = imagen, salida = máscara.` · `UNET de Stable Diffusion: entrada = (latente ruidoso, timestep, embedding de texto), salida = predicción del ruido presente en el latente.` · `Cómo se inyecta la condición de texto — cross-attention: en cada nivel de la U (tanto bajando como subiendo), hay un bloque de cross-attention que "consulta" al embedding de CLIP. El modelo se pregunta en cada capa: "dado lo que sé hasta acá, ¿qué partes del prompt son relevantes para guiar este nivel?"` · `El ciclo de denoising en cada paso:` · `1. La UNET recibe el latente ruidoso actual + el timestep + el embedding del prompt.` · `2. Predice el ruido que cree que está presente.` · `3. El scheduler resta ese ruido del latente → latente un poco menos ruidoso.` · `4. Se repite ~50 veces.` · `La conexión que cierra el círculo: la misma arquitectura que en 2015 servía para segmentar células al microscopio, hoy es el corazón de la generación de imágenes más usada del mundo. UNET no es solo una red — es un patrón arquitectónico poderosamente reutilizable.`

**`.../slide-43-1.jpg`** — slide 43 · `figura` · 864×486 px · **slide íntegramente imagen**
- **Depiction**: captura de una slide completa de texto, titulada **"Pipeline completo de inferencia"**, estructurada en cinco pasos numerados con encabezados en negrita, más un bloque de tres viñetas dentro del Paso 3 y una frase de cierre. Sin gráficos.
- **Why it matters**: **es todo el contenido de la slide 43, y es el cierre técnico de toda la Sección 4** — la única narración paso a paso, de punta a punta, de qué ocurre cuando alguien escribe un prompt. Contiene las dimensiones exactas de cada etapa (77×768, 64×64×4, 512×512×3) y la frase que resume la tesis del deck: "son tres piezas modulares orquestadas por un loop iterativo".
- **Transcribed text**: `Pipeline completo de inferencia` · `Juntamos todo. Esto es lo que ocurre, paso por paso, cuando alguien escribe un prompt y Stable Diffusion produce una imagen.` · `Paso 1 — Procesar el prompt: Prompt → tokenizer → CLIP Text Encoder → embedding de texto (77 × 768).` · `Paso 2 — Inicializar el latente con ruido: Generar un tensor aleatorio de 64×64×4 desde una distribución normal (controlado por la seed). Este es el "bloque de mármol" del que vamos a tallar.` · `Paso 3 — Bucle de denoising (~50 pasos): Para cada timestep t (de máximo a mínimo):` · `UNET recibe (latente actual, timestep t, embedding del prompt).` · `UNET predice el ruido presente.` · `El scheduler resta ese ruido → latente un poco menos ruidoso.` · `Paso 4 — Decodificar a píxeles: Latente final 64×64×4 → VAE Decoder → imagen 512×512×3.` · `Paso 5 — Devolver al usuario. La imagen final.` · `Frase para cerrar: todo lo que vimos en las secciones anteriores — UNET, embeddings de texto, condición — confluye en este pipeline. No es un modelo monolítico mágico; son tres piezas modulares orquestadas por un loop iterativo.`

**`.../slide-47-1.jpg`** — slide 47 · `figura` · 864×486 px · **slide íntegramente imagen**
- **Depiction**: captura de una slide completa de texto, titulada **"Recap: el desafío que dejamos pendiente"**, con dos bloques de cita en cursiva (el "de" y el "a") y una lista de tres viñetas ("Lo que ahora sabemos"). Sin gráficos. La mitad inferior de la slide está vacía.
- **Why it matters**: **es todo el contenido de la slide 47.** Es la slide bisagra de la Sección 5: reconecta el caso de negocio de TilTedTinder con las tres secciones técnicas y resume la tesis completa del deck en una línea ("El usuario escribe un prompt, CLIP lo entiende, la UNET talla la imagen denoising paso a paso, el VAE la decodifica").
- **Transcribed text**: `Recap: el desafío que dejamos pendiente` · `Volvamos al problema con el que arrancamos la Sección 3, ahora con todas las piezas en la mano:` · `El equipo de TilTedTinder quería pasar de:` · `"Generá una persona inclinada cualquiera" (lo que resolvía la GAN de la clase pasada).` · `A:` · `"Generá una persona inclinada que coincida con esta descripción en texto libre" (lo que ninguna GAN podía hacer).` · `Lo que ahora sabemos:` · `Existe la generación condicionada por texto como tarea (Sección 3).` · `Stable Diffusion es la herramienta que la implementa, combinando VAE + UNET + CLIP (Sección 4).` · `El usuario escribe un prompt, CLIP lo entiende, la UNET talla la imagen denoising paso a paso, el VAE la decodifica.` · `El próximo paso: traducir las preferencias reales de los usuarios a prompts concretos que el modelo pueda procesar.`

**`.../slide-48-1.jpg`** — slide 48 · `figura` · 864×486 px · **slide íntegramente imagen**
- **Depiction**: captura de una slide completa titulada **"De preferencias a prompts: ejemplos concretos"**. Tres bloques, uno por usuario: cada uno con la preferencia en cursiva y, debajo, un bloque de código en fondo gris con fuente monoespaciada conteniendo la variable `prompt`. Cierra con dos párrafos en negrita.
- **Why it matters**: **es todo el contenido de la slide 48.** Es el único lugar del deck donde aparecen prompts completos y ejecutables, y donde se enuncia la fórmula de prompting (**sujeto + atributos + estilo + condiciones de luz**). También es donde el uso de `seed` pasa de ser un hiperparámetro a ser un requisito de producto ("mismo prompt + misma seed = mismo perfil estable").
- **Transcribed text**: `De preferencias a prompts: ejemplos concretos` · `El equipo de producto toma las preferencias documentadas y las convierte en prompts. Estos son los tres ejemplos del slide del nuevo desafío, ahora como prompts ejecutables:` · `Usuario A — "Me atraen las personas inclinadas, altas, con anteojos y pelo rizado."` · `prompt = "a tilted portrait of a tall person with round glasses and curly hair, soft natural lighting, photorealistic, 4k"` · `Usuario B — "Prefiero caras inclinadas, jóvenes, con sonrisa y barba corta."` · `prompt = "a tilted portrait of a young person with a warm smile and short beard, soft daylight, candid photo, shallow depth of field"` · `Usuario C — "Inclinadas, mayores, expresión seria, rasgos angulosos."` · `prompt = "a tilted portrait of an older person with a serious expression and angular features, dramatic shadows, black and white photography"` · `Patrón a observar: un buen prompt para SD combina sujeto + atributos + estilo + condiciones de luz. La imagen final depende de esa estructura tanto como del modelo en sí. Aprender a escribir prompts es una habilidad propia — prompt engineering.` · `Y la pieza que falta: usar el seed para fijar el perfil generado. Si el usuario "matchea" con un perfil, queremos poder reproducirlo idénticamente cuando vuelva a abrir la app. Mismo prompt + misma seed = mismo perfil estable.`

**`.../slide-49-1.jpg`** — slide 49 · `figura` · 864×486 px · **slide íntegramente imagen**
- **Depiction**: captura de una slide completa titulada **"Lo que el equipo va a encontrar al ejecutar esto"**, con cinco viñetas de encabezado en negrita y un párrafo de cierre separado por un espacio grande. Sin gráficos.
- **Why it matters**: **es todo el contenido de la slide 49.** Es la única slide del deck que aterriza las limitaciones genéricas de la slide 45 en un caso concreto, y **la única que introduce fine-tuning (DreamBooth, LoRA), ControlNet, Inpainting, SDXL Turbo y FLUX Schnell** — cinco herramientas que no aparecen en ninguna otra parte. También es donde aparece la consideración ética, ausente del resto del deck.
- **Transcribed text**: `Lo que el equipo va a encontrar al ejecutar esto` · `Las limitaciones generales del slide anterior se vuelven concretas en este caso:` · `Stable Diffusion no conoce Slanted Land. El dataset de entrenamiento (LAION-5B) no contiene fotos del universo inclinado. Las primeras generaciones probablemente saldrán como caras rectas, no inclinadas. Solución profesional: fine-tuning con las 4 fotos reales que tienen — técnicas como DreamBooth o LoRA permiten enseñarle a SD un concepto nuevo con muy pocas imágenes.` · `Sesgo demográfico heredado. SD refleja sesgos del dataset: ciertos grupos demográficos están sobrerrepresentados, otros casi ausentes. El equipo va a tener que auditar las generaciones para no excluir poblaciones.` · `Control limitado a nivel de detalle. No podés pedir "exactamente esa nariz". Cada generación tiene variaciones inevitables. Para detalles finos hay que iterar — o usar herramientas más avanzadas (ControlNet, Inpainting).` · `Costo computacional. Generar 50 perfiles personalizados por usuario, en tiempo real, es caro. El equipo va a tener que pensar en caché de perfiles, generación batched offline, o modelos más rápidos (SDXL Turbo, FLUX Schnell).` · `Consideración ética. Generar personas que no existen para una app de citas plantea preguntas serias: ¿se le avisa al usuario que el perfil es sintético? ¿Hay riesgo de manipulación emocional? Decisiones de producto, no técnicas — pero hay que tomarlas.` · `Idea para llevarse: Stable Diffusion les resuelve el motor. El producto final requiere muchas decisiones más — sobre datos, ética, cómputo y UX.`

**`.../slide-50-1.jpg`** — slide 50 · `figura` · 864×486 px · **slide íntegramente imagen**
- **Depiction**: captura de la slide de cierre, titulada **"Pasamos al notebook"**, con un bloque "Stack:" de tres viñetas (una lleva el emoji 🤗 de Hugging Face) y un bloque "Lo que vamos a hacer:" con cinco puntos numerados, más un párrafo final en negrita. Los identificadores de código van en fuente monoespaciada.
- **Why it matters**: **es todo el contenido de la slide 50 y de todo el cierre de la clase.** Es la única slide con el stack concreto de la práctica (Colab, Tesla T4 16GB, Diffusers, SD v1.4 de CompVis, `float16`) y el plan de cinco ejercicios — incluido el "pipeline manual" que desarma SD en VAE + UNET + CLIP y que el deck señala como el momento en que "toda la Sección 4 se vuelve tangible". Sin transcribirla se pierde el puente entre la teoría y el notebook.
- **Transcribed text**: `Pasamos al notebook` · `Ahora pasamos a la práctica. Vamos a ejecutar Stable Diffusion en Google Colab.` · `Stack:` · `Plataforma: Google Colab con GPU (Tesla T4, 16GB).` · `Librería: 🤗 Hugging Face Diffusers.` · `Modelo: Stable Diffusion v1.4 (CompVis), en precisión float16 para que entre en la GPU gratuita.` · `Lo que vamos a hacer:` · `1. Pipeline alto nivel — StableDiffusionPipeline.from_pretrained(...) y generar imágenes en pocas líneas.` · `2. Jugar con hiperparámetros — num_inference_steps, guidance_scale, seed — y ver qué cambia en la imagen.` · `3. Generar grids — múltiples imágenes de un mismo prompt para apreciar la variabilidad.` · `4. Cambiar dimensiones — generar imágenes rectangulares (512×768).` · `5. Pipeline manual — desarmar el pipeline en sus tres componentes (VAE + UNET + CLIP) y reconstruirlo a mano. Esto cierra el círculo conceptual de la clase: cada bloque que vimos en teoría aparece como código.` · `Punto importante: el último ejercicio (pipeline manual) es donde toda la Sección 4 se vuelve tangible. Vas a ver el bucle de denoising, las cross-attention con el embedding de CLIP, y el VAE decodificando al final.`

### Marcos de tarjeta vacíos, mal clasificados como `figura` (5 únicos, 10 colocaciones)

Estos cinco archivos están marcados `figura` en `_manifest.json` por su tamaño en EMU, pero **no tienen contenido**: son el fondo decorativo de las tablas de dos columnas de las slides 13, 14 y 20. Cada uno es un rectángulo blanco con borde gris claro y una **barra vertical roja carmesí** en el borde izquierdo. Cada uno tiene un gemelo visualmente idéntico (md5 distinto) que ocupa la segunda columna.

- **`.../slide-13-1.png`** (+ `slide-13-1.svg`) — slide 13, 560×210 px. Marco de la celda izquierda de la primera tabla ("El problema"). Gemelo: `slide-13-2.png` / `.svg` (celda "Síntoma visual"). Sin texto.
- **`.../slide-13-3.png`** (+ `slide-13-3.svg`) — slide 13, 560×179 px. Marco de la celda izquierda de la segunda tabla ("Por qué importa en medicina"). Gemelo: `slide-13-4.png` / `.svg` (celda "La pregunta"). Sin texto.
- **`.../slide-14-1.png`** (+ `slide-14-1.svg`) — slide 14, 560×214 px. Marco de la celda "Origen". Gemelo: `slide-14-2.png` / `.svg` (celda "Contexto"). Sin texto.
- **`.../slide-14-3.png`** (+ `slide-14-3.svg`) — slide 14, 560×183 px. Marco de la celda "El truco". Gemelo: `slide-14-4.png` / `.svg` (celda "Dato"). Sin texto.
- **`.../slide-20-1.png`** (+ `slide-20-1.svg`) — slide 20, 562×433 px. Marco de la celda "Idea 1 — Separar lo caro de lo barato". Gemelo: `slide-20-2.png` / `.svg` (celda "Idea 2 — El dataset SA-1B"). Sin texto.

### Iconos (15 únicos)

Iconos de línea, monocromos. Diez fueron abiertos y descritos; cinco se despacharon sin abrir por ser decorativos y de tamaño mínimo (16–21 px).

**Descritos (10):**
- **`.../slide-06-1.png`** (+ `.svg`) — slide 6, 49×49 px. Auto visto de frente/perfil en trazo rojo carmesí, con dos ruedas circulares. Acompaña **"Autos autónomos"**.
- **`.../slide-06-2.png`** (+ `.svg`) — slide 6, 49×49 px. Satélite en trazo rojo: cuerpo central circular con dos paneles solares en diagonal y una antena parabólica. Acompaña **"Imagen satelital"**.
- **`.../slide-06-3.png`** (+ `.svg`) — slide 6, 49×49 px. Videocámara en trazo rojo: rectángulo redondeado con el triángulo del lente a la derecha. Acompaña **"Videoconferencia (Zoom, Meet)"**.
- **`.../slide-06-4.png`** (+ `.svg`) — slide 6, 49×49 px. Hoja vegetal en trazo rojo con nervadura central y venas laterales. Acompaña **"Agricultura de precisión"**.
- **`.../slide-06-5.png`** (+ `.svg`) — slide 6, 49×49 px. Documento con líneas de texto y un lápiz superpuesto en diagonal, en trazo rojo. Acompaña **"Edición de fotos"**.
- **`.../slide-07-1.png`** — slide 7, 21×16 px. Cuadrado rojo oscuro de esquinas redondeadas con la esquina inferior derecha doblada — marca de nota/callout. **Reaparece en `slide-37-1.png`** (slide 37).
- **`.../slide-25-1.png`** — slide 25, 23×18 px. Círculo azul sólido con una "i" blanca — icono de información. Marca el bloque "Pasamos de… A:".
- **`.../slide-31-1.png`** — slide 31, 19×15 px. Triángulo de advertencia amarillo/mostaza con signo de exclamación. Marca el "Punto crucial" sobre la condición.
- **`.../slide-36-1.png`** — slide 36, 22×17 px. Círculo gris con signo de interrogación — icono de pregunta. Marca "La pregunta inteligente que se hizo el equipo de CompVis".
- **`.../slide-44-1.png`** — slide 44, 23×18 px. Cuadrado rojo oscuro de esquinas redondeadas con la esquina inferior derecha doblada, variante del de la slide 7. Marca el "Tip práctico". **Reaparece en `slide-45-1.png`** (slide 45).

**Despachados sin abrir (5)** — decorativos, 12–21 px, sin texto:
- **`.../slide-28-1.png`** — slide 28, 16×12 px. Marcador de viñeta de la línea de tiempo.
- **`.../slide-29-1.png`** — slide 29, 17×13 px. Marcador de la "Frase clave".
- **`.../slide-31-2.png`** — slide 31, 19×15 px. Segundo marcador de la slide 31 (bloque "Adelanto").
- **`.../slide-37-2.png`** — slide 37, 21×16 px. Marcador del bloque "Por qué funciona".
- **`.../slide-37-3.png`** — slide 37, 21×16 px. Marcador del bloque "Resultado práctico".

### Reapariciones (7 colocaciones que no generan entrada propia)

`slide-13-2.png` (= gemelo de 13-1) · `slide-13-4.png` (= gemelo de 13-3) · `slide-14-2.png` (= gemelo de 14-1) · `slide-14-4.png` (= gemelo de 14-3) · `slide-20-2.png` (= gemelo de 20-1) · `slide-37-1.png` (= `slide-07-1.png`, md5 `afaf76a5bf61`) · `slide-45-1.png` (= `slide-44-1.png`, md5 idéntico). Los archivos están todos en la carpeta compañera; sus `.svg` hermanos también.

## Raw / preserved excerpts

### La timeline de SAM (slide 21, tabla completa verbatim)

> Tres años, cuatro versiones — cada una agregó una capacidad nueva sin romper la anterior:

| Versión | Lanzamiento | Capacidad nueva |
|---|---|---|
| SAM 1 | Abril 2023 | Foundation model para imágenes. Prompts visuales: puntos, cajas, máscaras. |
| SAM 2 | Julio 2024 | Extiende SAM al video — módulo de memoria que mantiene la segmentación coherente entre frames. |
| SAM 3 | Noviembre 2025 | Suma prompts de texto y vocabulario abierto. Permite pedir "todos los hepatocitos" en lenguaje natural. |
| SAM 3.1 | Marzo 2026 | Object Multiplex: tracking conjunto multi-objeto con memoria compartida, sin sacrificar precisión. |

> Patrón a observar: cada versión generaliza más — de imagen a video, de prompts visuales a texto, de un objeto a muchos. Es la misma trayectoria que vivieron los LLMs.
>
> En la práctica clínica: UNET y SAM conviven. UNET se usa cuando la salida tiene que ser clínicamente medible y reproducible (datos específicos, contornos bajo el píxel). SAM brilla en anotación asistida — un radiólogo clickea, SAM propone la máscara — acelerando 10× o más la creación de datasets médicos.

**Contrapunto de la figura de la misma slide** (captura del sitio de Meta, `slide-21-1.jpg`), que solo documenta tres versiones:

| Versión (según Meta) | Descripción | Capacidades listadas |
|---|---|---|
| SAM 1 | Segment any object in any image with as little as a single click | Segment an object from a click · Refine prediction with follow up clicks |
| SAM 2 | Segment and track any object in any image or video using click, box or mask prompts | Segment an object from a click · Track segmented objects in videos · Refine prediction with follow up clicks |
| SAM 3 | Detect, segment and track every example of any object category in an image or video, using text or examples | Segment an object from a click · Track segmented objects in videos · Refine prediction with follow up clicks · **Detect and segment matching instances from text** · **Refine detection with visual examples** |

### La tabla de parámetros de generación (slide 44, verbatim)

> Cuando ejecutemos la notebook van a aparecer cuatro perillas. Vale entenderlas antes:
>
> - **num_inference_steps** — cuántos pasos de denoising. Más pasos = mejor calidad, pero más lento. Default: 50. Por debajo de 20 la calidad se degrada notoriamente; por encima de 100 las mejoras son marginales.
> - **guidance_scale (classifier-free guidance)** — qué tan estrictamente seguir el prompt. Default: 7.5.
>   - Bajo (1-3): más diverso y creativo, pero menos fiel al prompt.
>   - Medio (7-9): el sweet spot.
>   - Alto (15+): muy fiel pero saturado, menos natural.
> - **seed** — controla el ruido inicial. Misma seed + mismo prompt = misma imagen (reproducibilidad total). Útil para iterar sin perder el control.
> - **height y width** — tamaño de salida. Múltiplos de 8 (porque el VAE comprime 8×). Default: 512×512.
>
> Tip práctico: el ciclo de iteración natural es fijar la seed, fijar el guidance, y mover el prompt — así aislás el efecto de cada cambio textual.

Consolidado en tabla:

| Hiperparámetro | Qué controla | Default | Rango / notas |
|---|---|---|---|
| `num_inference_steps` | Cantidad de pasos de denoising | 50 | <20 degrada notoriamente; >100 mejoras marginales |
| `guidance_scale` | Adherencia al prompt (classifier-free guidance) | 7.5 | 1-3 diverso/creativo · 7-9 sweet spot · 15+ saturado, poco natural |
| `seed` | Ruido inicial | — | Misma seed + mismo prompt = misma imagen |
| `height` / `width` | Tamaño de salida | 512×512 | Múltiplos de 8 (el VAE comprime 8×). La notebook también usa 512×768 |

### La anatomía de Stable Diffusion, reconstruida desde las imágenes

Las cuatro slides que definen la arquitectura (38, 39, 41, 43) no tienen una sola línea de texto en la extracción — todo lo siguiente proviene de transcribir sus figuras.

**A. Las tres piezas y sus tamaños** (slide 38, `slide-38-1.jpg`)

> Antes de meternos en cada componente, fijemos el mapa completo. Stable Diffusion tiene **tres redes** que trabajan juntas:

| Componente | Qué hace | Tamaño aprox. |
|---|---|---|
| VAE (Variational Autoencoder) | Comprime imagen ↔ latente | ~80M params |
| UNET | Denoiser condicional en espacio latente | ~860M params |
| CLIP Text Encoder | Prompt de texto → embedding | ~123M params |

> **Cómo se conectan:** el prompt entra al **CLIP**, que produce un embedding. El **UNET** usa ese embedding para guiar el denoising en el **espacio latente**. Cuando termina, el **VAE Decoder** transforma el latente final en una imagen visible.
>
> **Punto importante para llevarse:** dos de estas piezas — **UNET y CLIP** — ya las vimos. UNET la vimos en segmentación (Sección 2), CLIP en text-to-image (Sección 3). Solo nos queda entender el VAE y cómo se orquestan.

**B. El diagrama de pipeline embebido en la slide 38**, reconstruido como flujo:

```
Latent Seed                              User Prompt
Gaussian noise ~ N(0,1)                  "an astronaut riding a horse"
     |                                        |
     v                                        v
[64×64 latents] <----+                 [Frozen CLIP Text Encoder]
     |               |                        |
     |               |                        v
     |               |                 [77×768 text embeddings]
     v               |                        |
[Text conditioned latent UNet] <--------------+
     |               |
     v               |
[64×64 conditioned latents]
     |               |
     |        [Scheduler algorithm "reconstruct"]
     |               ^
     +---------------+   (repeat N scheduler steps)
     |
     v
[Variational Autoencoder Decoder]
     |
     v
[512×512 output image]
```

**C. Componente 1 — el VAE** (slide 39, `slide-39-1.jpg`, verbatim)

> **VAE — Variational Autoencoder.** Es la pieza que se encarga de la compresión-descompresión entre píxeles y espacio latente.
>
> **Dos mitades:**
> - **Encoder:** toma la imagen 512×512×3 y la mapea a un latente 64×64×4. Compresión ~48×.
> - **Decoder:** toma un latente 64×64×4 y reconstruye una imagen 512×512×3.
>
> **Cuándo se usa cada parte:**
> - **Durante entrenamiento de SD:** se usa el **encoder** — para llevar las imágenes reales del dataset al espacio latente, donde la UNET aprende a desruidizar.
> - **Durante inferencia (lo que nos interesa hoy): solo se usa el decoder** — para tomar el latente final ya desruidizado y reconstruir la imagen visible.
>
> **Cómo se entrena:** el VAE se entrena **antes y por separado** de la UNET. Su objetivo es simple: que `decoder(encoder(imagen)) ≈ imagen`. Una vez entrenado, sus pesos quedan congelados.
>
> **Frase corta:** el VAE es un compresor inteligente — convierte el problema de "generar 800K píxeles" en el problema de "generar 16K números latentes".

**D. Componente 2 — la UNET** (slide 41, `slide-41-1.jpg`, verbatim)

> **Componente 2: la UNET (¡acá vuelve!)**
>
> **Esta es la pieza central de Stable Diffusion** — y es **la misma estructura** que vimos en Sección 2 para segmentación.
>
> **Arquitectura:** encoder + decoder con forma en U + skip connections. Idéntica a UNET de segmentación.
>
> **Pero la tarea es distinta:**
> - **UNET de segmentación:** entrada = imagen, salida = máscara.
> - **UNET de Stable Diffusion:** entrada = (latente ruidoso, timestep, embedding de texto), salida = **predicción del ruido presente en el latente**.
>
> **Cómo se inyecta la condición de texto — cross-attention:** en cada nivel de la U (tanto bajando como subiendo), hay un bloque de **cross-attention** que "consulta" al embedding de CLIP. El modelo se pregunta en cada capa: *"dado lo que sé hasta acá, ¿qué partes del prompt son relevantes para guiar este nivel?"*
>
> **El ciclo de denoising en cada paso:**
> 1. La UNET recibe el latente ruidoso actual + el timestep + el embedding del prompt.
> 2. Predice el ruido que cree que está presente.
> 3. El scheduler resta ese ruido del latente → latente un poco menos ruidoso.
> 4. Se repite ~50 veces.
>
> **La conexión que cierra el círculo:** la misma arquitectura que en 2015 servía para segmentar células al microscopio, hoy es el corazón de la generación de imágenes más usada del mundo. UNET no es solo una red — es **un patrón arquitectónico** poderosamente reutilizable.

**E. Componente 3 — el CLIP Text Encoder** (slide 42 — la única de las tres que sí tiene texto en el markdown, verbatim)

> Ya lo conocimos en Sección 3 — acá solo cerramos el rol específico que cumple en Stable Diffusion.
>
> Modelo concreto que usa SD 1.x: CLIP ViT-L/14 de OpenAI (123M parámetros). Congelado durante el entrenamiento de Stable Diffusion — el equipo no lo reentrena, lo usa tal cual.
>
> Lo que entra y lo que sale:
> - Entrada: el prompt de texto (ej: "un astronauta montando un caballo").
> - Tokenización: 77 tokens (con padding si la frase es corta, truncado si es muy larga).
> - Salida: una matriz de embeddings de 77 × 768 dimensiones.
>
> Esa matriz se enchufa al UNET en cada bloque de cross-attention, como vimos en el slide anterior. Es el "lenguaje común" entre el prompt humano y la red que talla la imagen.
>
> Decisión de diseño interesante: Stable Diffusion no entrena el text encoder. Lo toma prestado de OpenAI ya entrenado. Esto ahorra cómputo y aprovecha que CLIP ya entendía la relación texto-imagen — no había razón de reinventar esa rueda.

**F. Pipeline completo de inferencia** (slide 43, `slide-43-1.jpg`, verbatim)

> Juntamos todo. Esto es lo que ocurre, paso por paso, cuando alguien escribe un prompt y Stable Diffusion produce una imagen.
>
> **Paso 1 — Procesar el prompt:**
> Prompt → tokenizer → CLIP Text Encoder → embedding de texto (77 × 768).
>
> **Paso 2 — Inicializar el latente con ruido:**
> Generar un tensor aleatorio de 64×64×4 desde una distribución normal (controlado por la *seed*). Este es el "bloque de mármol" del que vamos a tallar.
>
> **Paso 3 — Bucle de denoising (~50 pasos):**
> Para cada timestep t (de máximo a mínimo):
> - UNET recibe (latente actual, timestep t, embedding del prompt).
> - UNET predice el ruido presente.
> - El scheduler resta ese ruido → latente un poco menos ruidoso.
>
> **Paso 4 — Decodificar a píxeles:**
> Latente final 64×64×4 → VAE Decoder → imagen 512×512×3.
>
> **Paso 5 — Devolver al usuario.**
> La imagen final.
>
> **Frase para cerrar:** todo lo que vimos en las secciones anteriores — UNET, embeddings de texto, condición — confluye en este pipeline. No es un modelo monolítico mágico; **son tres piezas modulares orquestadas por un loop iterativo**.

**G. Tabla consolidada de dimensiones a lo largo del pipeline** (derivada de las slides 37, 38, 39, 42, 43)

| Etapa | Representación | Dimensión | Cantidad de valores |
|---|---|---|---|
| Prompt tokenizado | tokens CLIP | 77 tokens | 77 |
| Embedding de texto | salida CLIP ViT-L/14 | 77 × 768 | 59.136 |
| Latente inicial (semilla de ruido) | tensor gaussiano | 64 × 64 × 4 | 16.384 |
| Latente durante el bucle | tensor condicionado | 64 × 64 × 4 | 16.384 |
| Imagen de salida | RGB | 512 × 512 × 3 | 786.432 |

Relación de compresión declarada por el deck: **786.432 / 16.384 = 48×** (compresión espacial 8× por lado).

### Los tres prompts ejecutables de TilTedTinder v2 (slide 48, verbatim de la imagen)

> **Usuario A** — *"Me atraen las personas inclinadas, altas, con anteojos y pelo rizado."*
> ```
> prompt = "a tilted portrait of a tall person with round glasses and curly hair,
>           soft natural lighting, photorealistic, 4k"
> ```
> **Usuario B** — *"Prefiero caras inclinadas, jóvenes, con sonrisa y barba corta."*
> ```
> prompt = "a tilted portrait of a young person with a warm smile and short beard,
>           soft daylight, candid photo, shallow depth of field"
> ```
> **Usuario C** — *"Inclinadas, mayores, expresión seria, rasgos angulosos."*
> ```
> prompt = "a tilted portrait of an older person with a serious expression and angular features,
>           dramatic shadows, black and white photography"
> ```
> **Patrón a observar:** un buen prompt para SD combina **sujeto + atributos + estilo + condiciones de luz**. La imagen final depende de esa estructura tanto como del modelo en sí. Aprender a escribir prompts es una habilidad propia — *prompt engineering*.
>
> **Y la pieza que falta:** usar el `seed` para fijar el perfil generado. Si el usuario "matchea" con un perfil, queremos poder reproducirlo idénticamente cuando vuelva a abrir la app. Mismo prompt + misma seed = mismo perfil estable.

### El argumento clínico del borde (slides 13 y 17, verbatim)

> **Slide 13** — Si estás midiendo el volumen de un tumor para decidir radioterapia, un borde 2 píxeles más adentro o más afuera cambia el cálculo y puede cambiar la decisión clínica.
>
> **Slide 17** — Los detalles finos sobreviven el viaje por la U. En medicina, el borde es el dato.

### Las frases-ancla del deck (verbatim, por slide)

> - **Slide 4** — "segmentar es darle un significado pixel por pixel a la imagen."
> - **Slide 7** — "la máscara es lo que se mide, se documenta y se compara entre estudios."
> - **Slide 11** — "convertí un clasificador de imágenes en un clasificador de píxeles."
> - **Slide 17** — "En medicina, el borde es el dato."
> - **Slide 18** — "SAM no aprende una tarea — aprende qué es un objeto, y deja que vos le digas cuál querés."
> - **Slide 20** — "el secreto está tanto en el modelo como en los datos."
> - **Slide 27** — "Esto cierra el paradigma puramente visual y abre el matrimonio entre lenguaje y visión."
> - **Slide 29** — "un text encoder convierte una oración humana en un vector que captura su significado."
> - **Slide 30** — "CLIP traduce de 'humano' a 'espacio que la red puede usar'."
> - **Slide 31** — "la condición no es un input opcional al costado. Es lo que dirige cada paso del proceso de generación."
> - **Slide 33** — "Stable Diffusion no construye la imagen, la talla — empezando por un bloque de ruido y removiendo lo que sobra hasta dejar la figura."
> - **Slide 39 (imagen)** — "el VAE es un compresor inteligente — convierte el problema de 'generar 800K píxeles' en el problema de 'generar 16K números latentes'."
> - **Slide 41 (imagen)** — "UNET no es solo una red — es un patrón arquitectónico poderosamente reutilizable."
> - **Slide 43 (imagen)** — "No es un modelo monolítico mágico; son tres piezas modulares orquestadas por un loop iterativo."
> - **Slide 45** — "Saber dónde falla es tan importante como saber qué puede hacer."
> - **Slide 49 (imagen)** — "Stable Diffusion les resuelve el motor. El producto final requiere muchas decisiones más — sobre datos, ética, cómputo y UX."
