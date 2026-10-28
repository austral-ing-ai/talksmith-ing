---
source_file: stylegan-karras-2019
source_type: web-capture
ingested_at: 2026-08-14
---

# A Style-Based Generator Architecture for Generative Adversarial Networks — StyleGAN (arXiv:1812.04948) — página de abstract

## Provenance
- Original location: `research/web/stylegan-karras-2019/`
- Format: web-capture (arXiv `abs` page; `page.md` + `original.html` + `assets/`)
- URL: https://arxiv.org/abs/1812.04948
- Author / source (if known): Tero Karras, Samuli Laine, Timo Aila (NVIDIA)
- Date of original (if known): enviado 12 dic 2018; última revisión 29 mar 2019 (v3, versión final de CVPR). CVPR 2019.
- Fetched at: 2026-08-14T17:03:10Z (HTTP 200, 41.949 bytes)
- **Rol en la Clase 9 — encuadre importante:** esta fuente **no es tema central**. Aparece como el **"antes"** contra el que la clase contrasta la difusión (slides 26, 27, 31): el estado del arte en generación de imágenes *previo* a los modelos de difusión, basado en GANs. Debe registrarse con ese rol —punto de comparación histórica— y no como si el deck enseñara StyleGAN.

## Key claims

- **Autores:** Tero Karras, Samuli Laine, Timo Aila (NVIDIA). **Año:** 2018 (v1) / 2019 (v3). **Venue:** **CVPR 2019** (el campo `Comments` dice "CVPR 2019 final version"). **arXiv ID:** arXiv:1812.04948 [cs.NE, cs.LG, stat.ML]. **DOI:** 10.48550/arXiv.1812.04948.
- Proponen una **arquitectura alternativa de generador para GANs**, tomando prestado de la literatura de **transferencia de estilo**.
- La arquitectura produce una **separación automática y no supervisada** entre **atributos de alto nivel** (pose e identidad, cuando se entrena con caras humanas) y **variación estocástica** (pecas, pelo).
- Habilita **control intuitivo y específico por escala** de la síntesis.
- Mejora el estado del arte en **métricas tradicionales de calidad de distribución**, tiene **mejores propiedades de interpolación** y **desenreda mejor los factores latentes de variación**.
- Proponen **dos métodos automáticos nuevos** para cuantificar calidad de interpolación y desenredo (*disentanglement*), aplicables a **cualquier** arquitectura de generador.
- Introducen **un dataset nuevo de caras humanas, muy variado y de alta calidad** (es FFHQ, aunque el abstract no lo nombra).

## Definitions and terminology

- **GAN (red generativa antagónica).** El paradigma que este paper representa en el deck. **El abstract no define qué es una GAN** — ni menciona al discriminador, ni el entrenamiento adversarial. Asume el conocimiento. Si la clase necesita definir GAN para contrastarla con difusión, la definición **no está en el corpus**.
- **Generador basado en estilo.** La contribución: la arquitectura del generador se reorganiza tomando ideas de style transfer, de modo que el vector latente controle "estilos" a distintas escalas en lugar de alimentar la red sólo por la entrada.
- **Desenredo (*disentanglement*).** Que factores de variación distintos queden controlados por direcciones distintas del espacio latente. El abstract lo nombra y afirma mejorarlo, sin definirlo formalmente.
- **Control específico por escala (*scale-specific control*).** Distintos niveles de la red controlan distintos niveles de detalle: pose y forma general arriba, textura fina abajo.
- **Variación estocástica.** El ruido que produce detalles irrelevantes para la identidad (pecas, mechones), separado de los atributos de alto nivel.
- **Propiedades de interpolación.** Qué tan suaves y semánticamente coherentes son las transiciones al moverse por el espacio latente.

### Contraste con difusión — el punto que le interesa a la clase

Nada de esto está en el abstract, pero es el eje del contraste que el deck plantea en las slides 26, 27 y 31, y conviene registrarlo explícitamente porque el corpus lo respalda sólo de a pedazos:

- **StyleGAN genera en un solo paso** (una pasada por el generador); **la difusión genera iterativamente** (decenas de pasos de denoising). Los abstracts de difusión latente y CFG describen ese proceso secuencial y su costo ("inference is expensive due to sequential evaluations"), así que el lado "difusión" del contraste sí está respaldado; el lado "GAN" hay que darlo por conocido.
- **StyleGAN es de dominio estrecho:** caras, y para eso hace falta un dataset dedicado de caras. **La difusión con condicionamiento por texto es de dominio abierto.** El abstract de StyleGAN lo deja ver sin decirlo: introduce un dataset de caras porque el modelo se entrena sobre caras.
- **StyleGAN no toma texto.** No hay prompt. El control es por manipulación del vector latente, que es potente pero requiere pericia. Es exactamente la diferencia de interfaz que hace que la difusión con texto se haya vuelto masiva.
- **Lo que StyleGAN hacía mejor y sigue haciendo bien:** control fino y desenredado por escala, e interpolación suave. La difusión ganó en generalidad y en interfaz, no en todas las dimensiones. Un contraste honesto lo dice.

## Evidence and examples

- **El abstract no contiene ni un solo número.** Ni FID, ni resolución, ni cantidad de parámetros, ni tiempo de entrenamiento.
- Ejemplos cualitativos nombrados: **pose e identidad** como atributos de alto nivel; **pecas y pelo** como variación estocástica.
- Dominio de entrenamiento: **caras humanas**.
- Contribuciones metodológicas: dos métricas automáticas nuevas (calidad de interpolación y desenredo) + un dataset nuevo de caras.
- Tres versiones en arXiv (dic 2018 → mar 2019), señal de iteración hasta la versión final de CVPR.

### Verificación de cifras del deck

El deck no cita cifras de StyleGAN entre las que este encargo pide verificar, y esta fuente no ofrece ninguna: el abstract es enteramente cualitativo. Si el deck acompaña las slides 26/27/31 con algún número sobre GANs (FID, resolución, año), **no sale de acá**.

## Inconsistencies / open questions

1. **La página capturada trae solo el abstract.** Lo que la clase necesitaría y no está:
   - **Las imágenes generadas** — que en este paper son el argumento entero. StyleGAN se hizo famoso por las caras de "This Person Does Not Exist"; sin una sola imagen, la captura no transmite nada de lo que hizo relevante al trabajo.
   - **El diagrama del generador** (mapping network z → w, AdaIN, inyección de ruido por nivel).
   - Los **números de FID** que respaldan "improves the state-of-the-art".
   - El nombre y la composición de **FFHQ**, el dataset introducido.
   - Las **definiciones formales** de las dos métricas nuevas (perceptual path length, linear separability).
2. **Ninguna definición de GAN en todo el corpus.** Si el deck contrasta GAN vs. difusión (slides 26, 27, 31), la mitad "GAN" del contraste no tiene respaldo documental: ni este abstract ni el de pix2pix explican el mecanismo adversarial. Es el hueco más claro del bloque de contraste.
3. **Abstract sin un solo número**, en un paper cuya contribución incluye dos métricas nuevas. Es llamativo y limita mucho lo citable.
4. **Los términos técnicos vienen sin traducción.** "Disentangles the latent factors of variation" es una frase que este público no va a decodificar sin ayuda; la fuente no la ofrece.
5. **Cuidado con el marco temporal.** StyleGAN es de 2018-2019; StyleGAN2 (2019) y StyleGAN3 (2021) siguieron mejorando la línea, y las GANs no se detuvieron cuando aparecieron los modelos de difusión. Presentar a StyleGAN como "lo que había antes" es correcto como recorte narrativo, pero decir o sugerir que la difusión terminó con las GANs sería incorrecto — y esta fuente, de 2019, no puede sostener ninguna afirmación sobre lo que pasó después.

## Images / diagrams

La captura de una página `abs` de arXiv **no incluye ninguna figura del paper** — y en este caso la pérdida es mayor que en los demás, porque las imágenes generadas *eran* el argumento. Los tres archivos guardados son cromo del sitio, copiados a la carpeta compañera por completitud.

  - **Depiction:** logotipo institucional de arXiv en la barra superior del sitio (vectorial, tema claro).
  - **Why it matters:** nada. Cromo de navegación.
  - **Transcribed text:** "arXiv" (atributo `alt`: "archive").
  - **Depiction:** ícono de 16×16 px de BibSonomy — grafo de nodos gris con el nodo central en magenta.
  - **Why it matters:** nada. Botón de marcador.
  - **Transcribed text:** ninguno (atributo `alt`: "BibSonomy").
  - **Depiction:** ícono de 18×18 px de Reddit — mascota "Snoo" en gris con ojos rojos.
  - **Why it matters:** nada. Botón de compartir.
  - **Transcribed text:** ninguno (atributo `alt`: "Reddit").

## Raw / preserved excerpts

**Abstract completo, verbatim (inglés):**

> We propose an alternative generator architecture for generative adversarial networks, borrowing from style transfer literature. The new architecture leads to an automatically learned, unsupervised separation of high-level attributes (e.g., pose and identity when trained on human faces) and stochastic variation in the generated images (e.g., freckles, hair), and it enables intuitive, scale-specific control of the synthesis. The new generator improves the state-of-the-art in terms of traditional distribution quality metrics, leads to demonstrably better interpolation properties, and also better disentangles the latent factors of variation. To quantify interpolation quality and disentanglement, we propose two new, automated methods that are applicable to any generator architecture. Finally, we introduce a new, highly varied and high-quality dataset of human faces.

**Metadatos de la página, verbatim:**

> Computer Science > Neural and Evolutionary Computing
> arXiv:1812.04948 (cs)
> [Submitted on 12 Dec 2018 (v1), last revised 29 Mar 2019 (this version, v3)]
> Title: A Style-Based Generator Architecture for Generative Adversarial Networks
> Authors: Tero Karras, Samuli Laine, Timo Aila
> Comments: CVPR 2019 final version
> Subjects: Neural and Evolutionary Computing (cs.NE); Machine Learning (cs.LG); Machine Learning (stat.ML)
> Cite as: arXiv:1812.04948 [cs.NE]
> https://doi.org/10.48550/arXiv.1812.04948
