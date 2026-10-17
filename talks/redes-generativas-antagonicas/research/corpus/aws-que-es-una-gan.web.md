---
source_file: aws-que-es-una-gan
source_type: web-capture
ingested_at: 2026-08-14
---

# ¿Qué es una GAN? — Explicación sobre las redes generativas antagónicas (AWS)

## Provenance
- Original location: `research/web/aws-que-es-una-gan/`
- Format: html (captura web de `talksmith:ingest` — `page.md` + `original.html` + `assets/`)
- Author / source (if known): **Amazon Web Services** — página de marketing técnico de la serie "¿Qué es…?", sin autor individual. Versión en español del sitio.
- Date of original (if known): la página no lleva fecha de publicación ni de actualización. Las imágenes están servidas desde una ruta de CloudFront fechada **2021/11/11**, lo que sugiere que el contenido gráfico es de noviembre de 2021 o anterior. Captura: 2026-08-14T17:03:00Z, HTTP 200, URL `https://aws.amazon.com/es/what-is/gan/`
- **Nivel de la fuente**: material educativo de un proveedor cloud. **No es fuente primaria.** Ver *Inconsistencies* para el alcance exacto de lo que puede sostener.
- **Relevancia particular**: es **el único hipervínculo del deck fuera de YouTube** (slide 15).

## Key claims

- **Definición de entrada**: "Una red generativa antagónica (GAN) es una arquitectura de aprendizaje profundo. Entrena dos redes neuronales de modo que compitan entre sí para generar nuevos datos más auténticos a partir de un conjunto de datos de entrenamiento determinado."
- **De dónde viene el nombre**: "Una GAN se denomina *antagónica* porque entrena dos redes diferentes y las enfrenta entre sí." Es la explicación etimológica que la clase usa en la slide 15.
- **El criterio de terminación, en prosa**: "El sistema genera versiones nuevas y mejoradas de valores de datos falsos hasta que la red de predicción ya no puede distinguir el falso del original." Es la versión no formal del `D = 1/2` de Goodfellow et al.
- **El proceso en seis pasos** (transcrito completo en *Raw / preserved excerpts*), con la aclaración honesta de la propia página de que "una ecuación matemática compleja constituye la base de todo el proceso" y que lo que sigue es "una visión general simplista".
- **La dinámica del equilibrio**: "El generador intenta maximizar la probabilidad de error del discriminador, pero este último intenta minimizar la probabilidad de error." Es el juego minimax dicho sin la palabra minimax.
- **Cuatro casos de uso**: generar imágenes; generar datos de entrenamiento para otros modelos (aumento de datos); completar información faltante; generar modelos 3D a partir de datos 2D.
- **Cuatro tipos de GAN** con definición breve cada uno: Vanilla GAN, Conditional GAN, Deep convolutional GAN, Super-resolution GAN (más LAPGAN como variante). Menciona además StyleGAN, CycleGAN y DiscoGAN "que resuelven diferentes tipos de problemas", sin desarrollarlos.
- **Cierre comercial**: SageMaker, Bedrock y DeepComposer como servicios de AWS para trabajar con GANs.

## Definitions and terminology

Esta página es, para varios términos, **la única fuente en español y a nivel didáctico del corpus**. Vale la pena aprovecharla para eso — y solo para eso.

- **Red generativa antagónica (GAN)**: arquitectura de aprendizaje profundo que entrena dos redes neuronales enfrentadas para generar datos nuevos más auténticos. **La traducción "antagónica"** (frente a "adversaria" o "adversarial") es la que usa AWS en español, y conviene que el deck sea consistente con la que elija.
- **Red generadora / red discriminadora**: "Un sistema de redes generativas antagónicas consta de dos redes neuronales profundas: la *red generadora* y la *red discriminadora*."
- **Vanilla GAN**: "el modelo GAN básico que genera variaciones de datos con poca o ninguna retroalimentación de la red discriminadora. Un Vainilla GAN suele requerir mejoras para la mayoría de los casos de uso en el mundo real." **Este es el término para el que el deck usa esta página (slide 15)**, y la fuente lo cubre bien.
- **Conditional GAN (cGAN)** — la definición útil, en español: "introduce el concepto de condicionamiento, lo que permite la generación de datos específicos. El generador y el discriminador reciben información adicional, por lo general, **etiquetas de clase** u otra forma de datos condicionantes." Coincide con `cgan-mirza-osindero-2014.web.md`, que es la fuente primaria.
- **Deep convolutional GAN (DCGAN)** — **la mejor cobertura del corpus para dos términos que la clase necesita y que el abstract de DCGAN no da**: "el generador utiliza **convoluciones transpuestas** para aumentar la distribución de los datos, y el discriminador también utiliza capas convolucionales para clasificar los datos. El DCGAN también introduce **directrices de arquitectura para hacer que la capacitación sea más estable**." Es decir: convoluciones transpuestas y recetas de estabilidad, nombradas explícitamente. Con la salvedad de nivel (ver abajo), es la cita disponible.
- **Super-resolution GAN (SRGAN)**: "se centran en la ampliación de imágenes de baja resolución a alta resolución... mantener la calidad y los detalles". Sin mencionar la pérdida perceptual — para eso, `srgan-ledig-2017.web.md`.
- **LAPGAN (Laplacian Pyramid GAN)**: enfoque jerárquico con múltiples generadores y discriminadores a distintas escalas, empezando en baja resolución y mejorando por etapas. **Nota importante para la clase**: esto se parece mucho al *progressive growing* de ProGAN pero **no es lo mismo** — LAPGAN usa varios pares generador/discriminador simultáneos; ProGAN hace crecer **un solo** par agregándole capas durante el entrenamiento. Confundirlos es fácil.
- **Ruido**: aparece en el paso 3 del proceso — "El generador modifica algunos atributos de los datos al agregar ruido (o cambios aleatorios)" — y en el paso 6, "reducir la aleatorización del **vector de ruido**". Es la única mención de "vector de ruido" en el corpus fuera del contexto formal. **Ojo: la descripción de AWS es imprecisa** (ver *Inconsistencies*).
- La página **no** usa las expresiones *espacio latente*, *juego minimax*, *mode collapse*, *FID* ni *Inception Score*.

## Evidence and examples

- **Ejemplo de entrenamiento desarrollado** (transcrito completo abajo): una GAN que agrega anteojos de sol a caras. El discriminador recibe una mezcla de fotos reales de gente con anteojos y de imágenes generadas con anteojos agregados; si distingue, el generador ajusta sus parámetros; si es engañado, ajusta el discriminador. "La competencia mejora ambas redes hasta que se alcanza el equilibrio." Es un ejemplo didáctico limpio y en español.
- **Aplicación en salud, la única del corpus**: "en el cuidado de la salud, GAN combina radiografías y otras exploraciones corporales para crear imágenes realistas de los órganos destinadas a la planificación y simulación quirúrgicas." **Sin cita, sin estudio, sin caso concreto.** Es el punto de contacto más cercano entre este corpus y el marco biomédico de la materia, y es una afirmación de marketing.
- **Aumento de datos**: el ejemplo es generar datos sintéticos de transacciones fraudulentas para entrenar un detector de fraude.
- **Completar información faltante**: generar imágenes del subsuelo a partir de datos de superficie, para cartografía geotérmica o captura de carbono.
- **Sin datasets nombrados, sin métricas, sin números, sin referencias bibliográficas.** La página no cita ni un paper — ni siquiera a Goodfellow et al.
- **Dos imágenes**, transcritas abajo: la figura cebra ↔ caballo (que es de CycleGAN) y un diagrama de arquitectura GAN.

## Inconsistencies / open questions

- **Nivel de la fuente — el asiento pedido.** Es material educativo de un proveedor cloud, con finalidad comercial explícita (la página termina vendiendo SageMaker, Bedrock y DeepComposer). **No cita ni una sola fuente primaria.** Sirve para: la intuición de la arquitectura vanilla, el vocabulario en español, y la taxonomía informal de tipos de GAN — que es exactamente para lo que el deck la usa en la slide 15, y para eso está bien. **No sirve para**: afirmaciones técnicas finas, resultados, fechas, atribuciones, ni nada cuantitativo. Cada vez que una afirmación de esta página también esté en un paper del corpus, hay que citar el paper.
- **Imprecisión técnica concreta, que importa si la clase reutiliza el texto.** Los pasos 3 y 6 describen al generador como algo que "modifica atributos de los datos al agregar ruido" a datos de entrenamiento, y al discriminador como algo que le indica "reducir la aleatorización del vector de ruido". **Eso no es lo que hace una GAN vanilla.** El generador transforma un vector de ruido `z` muestreado de una distribución previa **en una imagen nueva**; no parte de una imagen real para modificarla. La descripción de AWS se parece más a un autoencoder con perturbaciones que a la formulación de Goodfellow et al. El ejemplo de los anteojos de sol arrastra el mismo problema ("la imagen de entrada es un rostro humano que GAN intenta modificar"). Si el deck toma la explicación de acá, hereda el error. **La formulación correcta está en `gan-goodfellow-2014.web.md`.**
- **[Punto 5 del encargo] "+30 % de precisión" (slide 46).** Esta página es la que más se acerca al tema — es la única fuente del corpus que argumenta a favor del **aumento de datos con GANs** ("puede utilizar modelos generativos para el aumento de datos a fin de crear datos sintéticos con todos los atributos de los datos del mundo real") — y **no da ningún número**. Ni +30 %, ni ningún otro. Ninguna de las 14 fuentes del corpus respalda esa cifra. Si la slide 46 la conserva, necesita fuente propia; el argumento cualitativo de aumento de datos sí se puede citar desde acá, la cuantificación no.
- **La afirmación sobre salud no tiene respaldo.** "GAN combina radiografías y otras exploraciones corporales para crear imágenes realistas de los órganos destinadas a la planificación y simulación quirúrgicas" es una oración sin cita en una página de marketing. Dado que la materia es biomedicina, es tentador usarla; conviene no hacerlo sin una fuente primaria detrás.
- **Figura de CycleGAN sin atribución.** La imagen cebra ↔ caballo (`ML-6149-image005-500.jpg`) es la figura característica de Zhu et al. 2017 y la página la usa **sin citar el paper**. Si la clase la proyecta, hay que atribuirla a CycleGAN (`cyclegan-zhu-2017.web.md`), no a AWS.
- **Sin fecha**: no hay fecha de publicación ni de última actualización. Las rutas de las imágenes apuntan a 2021-11-11. Para citarla hay que dar fecha de consulta (2026-08-14).
- **Menciona StyleGAN, CycleGAN y DiscoGAN al pasar**, sin fechas ni autores, en una lista que declara no ser exhaustiva. No sirve para el linaje de la slide 39.

## Images / diagrams

- `aws-que-es-una-gan.web/images/ML-6149-image025.jpg`
  - Depiction: **diagrama de flujo de la arquitectura GAN vanilla**, dibujado en estilo diagrams.net sobre una grilla clara, orientación horizontal. De izquierda a derecha: un pequeño triángulo violeta rotulado "Random z" alimenta con una flecha una caja tridimensional amarilla rotulada **"Generator"**. Del generador sale una flecha hacia un pergamino rotulado **"Fake Sample"**, que apunta a una caja tridimensional azul rotulada **"Discriminator"**. Por abajo, un cilindro verde de base de datos rotulado **"Real Data"** conecta con otro pergamino, **"Real Sample"**, que también apunta al discriminador. Del discriminador sale una flecha a un rombo rotulado **"Real or Fake"**. Del rombo salen dos líneas hacia dos íconos de documento a la derecha: arriba **"Generator Loss"** y abajo **"Discriminator Loss"**. Y de vuelta, dos flechas gruesas grises de retroalimentación: una larga desde "Generator Loss" hasta el generador (atravesando todo el diagrama de derecha a izquierda) y otra desde "Discriminator Loss" hasta el discriminador.
  - Why it matters: **es el diagrama canónico que la clase necesita para la slide 15 y es exactamente aquello para lo que esta fuente sirve.** Muestra las dos rutas de datos (ruido → generador → muestra falsa; datos reales → muestra real), la decisión binaria del discriminador, y — lo más importante y lo que suele faltar en los diagramas simplificados — **las dos pérdidas separadas y sus dos caminos de retropropagación distintos**. Ese detalle es justamente lo que hace visible que son dos redes entrenadas con objetivos opuestos y no un solo modelo. Notar además que el diagrama **sí muestra el flujo correcto** (ruido `z` → generador → imagen), contradiciendo la descripción textual imprecisa de la propia página (ver *Inconsistencies*). Si la clase usa una de las dos cosas, que use el diagrama.
  - Transcribed text: `Random z` · `Generator` · `Fake Sample` · `Real Data` · `Real Sample` · `Discriminator` · `Real or Fake` · `Generator Loss` · `Discriminator Loss`.
- `aws-que-es-una-gan.web/images/ML-6149-image005-500.jpg`
  - Depiction: **la figura cebra ↔ caballo de CycleGAN.** Cuatro fotografías en dos filas de dos, con rótulos entre medio. Fila superior: a la izquierda, tres cebras paradas en un pastizal verde con colinas al fondo; a la derecha, la misma foto con las cebras convertidas en caballos de pelaje marrón claro — las rayas desaparecieron, el fondo quedó intacto. Debajo, el rótulo **"zebra → horse"**. Fila inferior: a la izquierda, un caballo marrón galopando en un campo abierto; a la derecha, la misma foto con el caballo convertido en cebra, rayas incluidas, y con el fondo virado a tonos más apagados y verdosos. Debajo, el rótulo **"horse → zebra"**.
  - Why it matters: es la ilustración más reconocible de la **traducción imagen a imagen no apareada** y sirve directamente a la slide 44. Muestra bien las dos direcciones del ciclo (`G: X → Y` y `F: Y → X`) que definen CycleGAN. Y muestra también, si uno mira el fondo de la fila inferior, un artefacto típico: la conversión caballo→cebra le cambió el color a todo el pasto, no solo al animal. **Advertencia de atribución: esta figura es de Zhu et al. 2017 (CycleGAN), y la página de AWS la usa sin citarla.** Al proyectarla, atribuir a `cyclegan-zhu-2017.web.md`.
  - Transcribed text: `zebra → horse` · `horse → zebra`.

## Raw / preserved excerpts

**Definición de apertura**, verbatim:

> Una red generativa antagónica (GAN) es una arquitectura de aprendizaje profundo. Entrena dos redes neuronales de modo que compitan entre sí para generar nuevos datos más auténticos a partir de un conjunto de datos de entrenamiento determinado. Por ejemplo, es posible generar nuevas imágenes a partir de una base de datos de imágenes existente, así como música original a partir de una base de datos de canciones. Una GAN se denomina *antagónica* porque entrena dos redes diferentes y las enfrenta entre sí. Una red genera nuevos datos al tomar una muestra de datos de entrada y modificarla en la medida de lo posible. La otra red intenta predecir si la salida de datos generada pertenece al conjunto de datos original. En otras palabras, la red de predicción determina si los datos generados son falsos o reales. El sistema genera versiones nuevas y mejoradas de valores de datos falsos hasta que la red de predicción ya no puede distinguir el falso del original.

**El proceso en seis pasos**, verbatim:

> *Un sistema de redes generativas antagónicas consta de dos redes neuronales profundas: la *red generadora* y la red discriminadora*. Ambas redes se entrenan en un juego antagónico, en el que una intenta generar nuevos datos y la otra intenta predecir si la salida es falsa o real.
>
> Técnicamente, GAN funciona de la siguiente manera. Una ecuación matemática compleja constituye la base de todo el proceso de computación, pero esta es una visión general simplista:
>
> 1. La red neuronal del generador analiza el conjunto de entrenamiento e identifica los atributos de los datos
> 2. La red neuronal discriminadora también analiza los datos de entrenamiento inicial y distingue entre los atributos de forma independiente
> 3. El generador modifica algunos atributos de los datos al agregar ruido (o cambios aleatorios) a determinados atributos
> 4. El generador transfiere los datos modificados al discriminador
> 5. El discriminador calcula la probabilidad de que la salida generada pertenezca al conjunto de datos original
> 6. El discriminador proporciona alguna orientación al generador para reducir la aleatorización del vector de ruido en el siguiente ciclo
>
> El generador intenta maximizar la probabilidad de error del discriminador, pero este último intenta minimizar la probabilidad de error. En las iteraciones de entrenamiento, tanto el generador como el discriminador evolucionan y se enfrentan de forma continua hasta alcanzar un estado de equilibrio. En el estado de equilibrio, el discriminador ya no puede reconocer los datos sintetizados. En este punto, termina el proceso de formación.

**Ejemplo de entrenamiento (los anteojos de sol)**, verbatim:

> Contextualicemos lo anterior con un ejemplo del modelo GAN en la traducción de imagen a imagen.
>
> Tenga en cuenta que la imagen de entrada es un rostro humano que GAN intenta modificar. Por ejemplo, los atributos pueden ser las formas de los ojos o de las orejas. Supongamos que el generador cambia las imágenes reales agregándoles gafas de sol. El discriminador recibe un conjunto de imágenes, algunas de personas reales con gafas de sol y algunas imágenes generadas que se modificaron para incluir gafas de sol.
>
> Si el discriminador puede diferenciar entre lo falso y lo real, el generador actualiza sus parámetros para generar imágenes falsas aún mejores. Si el generador produce imágenes que engañan al discriminador, el discriminador actualiza sus parámetros. La competencia mejora ambas redes hasta que se alcanza el equilibrio.

**Tipos de GAN**, verbatim:

> Existen diferentes tipos de modelos GAN según las fórmulas matemáticas utilizadas y las diferentes formas en que el generador y el discriminador interactúan entre sí. A continuación, damos algunos modelos de uso común, pero la lista no es exhaustiva. Existen muchos otros tipos de GAN, como StyleGAN, CycleGAN y DiscoGAN, que resuelven diferentes tipos de problemas.
>
> **Vanilla GAN** — Este es el modelo GAN básico que genera variaciones de datos con poca o ninguna retroalimentación de la red discriminadora. Un Vainilla GAN suele requerir mejoras para la mayoría de los casos de uso en el mundo real.
>
> **Conditional GAN** — Una conditional GAN (cGAN) introduce el concepto de condicionamiento, lo que permite la generación de datos específicos. El generador y el discriminador reciben información adicional, por lo general, etiquetas de clase u otra forma de datos condicionantes. Por ejemplo, si se generan imágenes, la condición podría ser una etiqueta que describa el contenido de la imagen. El condicionamiento permite al generador producir datos que cumplen condiciones específicas.
>
> **Deep convolutional GAN** — Al reconocer el poder de las redes neuronales convolucionales (CNN) en el procesamiento de imágenes, Deep convolutional GAN (DCGAN) integra arquitecturas CNN en GAN. Con DCGAN, el generador utiliza convoluciones transpuestas para aumentar la distribución de los datos, y el discriminador también utiliza capas convolucionales para clasificar los datos. El DCGAN también introduce directrices de arquitectura para hacer que la capacitación sea más estable.
>
> **Super-resolution GAN** — Los Super-resolution GANS (SRGANs) se centran en la ampliación de imágenes de baja resolución a alta resolución. El objetivo es mejorar las imágenes a una resolución más alta y, al mismo tiempo, mantener la calidad y los detalles de la imagen. Las Laplacian Pyramid GANs (LAPGANs) enfrentan el desafío de generar imágenes de alta resolución al dividir el problema en etapas. Utilizan un enfoque jerárquico, con múltiples generadores y discriminadores que trabajan en diferentes escalas o resoluciones de la imagen. El proceso comienza con la generación de una imagen de baja resolución cuya calidad mejora en las etapas progresivas de GAN.

**Casos de uso**, verbatim (los cuatro encabezados con su desarrollo):

> **Generar imágenes** — Las redes generativas antagónicas crean imágenes realistas mediante indicaciones basadas en texto o modificando las imágenes existentes. Pueden ayudar a crear experiencias visuales realistas e inmersivas en videojuegos y entretenimiento digital. GAN también puede editar imágenes, como convertir una imagen de baja resolución en una de alta resolución o convertir una imagen en blanco y negro en color. También puede crear rostros, personajes y animales realistas para animación y video.
>
> **Generar datos de entrenamiento para otros modelos** — En el aprendizaje automático (ML), el aumento de datos aumenta artificialmente el conjunto de entrenamiento mediante la creación de copias modificadas de un conjunto de datos a partir de los datos existentes. Puede utilizar modelos generativos para el aumento de datos a fin de crear datos sintéticos con todos los atributos de los datos del mundo real. Por ejemplo, puede generar datos de transacciones fraudulentas que luego se utilizan para entrenar a otro sistema de ML de detección de fraudes. Estos datos pueden enseñar al sistema a distinguir con precisión entre transacciones sospechosas y auténticas.
>
> **Completar la información faltante** — En ocasiones, es posible que desee que el modelo generativo adivine con precisión y complete alguna información faltante en un conjunto de datos. Por ejemplo, puede entrenar a GAN para que genere imágenes de la superficie subterránea (subsuelo) mediante la comprensión de la correlación entre los datos de la superficie y las estructuras subterráneas. Al estudiar las imágenes conocidas de la subsuelo, puede crear otras nuevas utilizando mapas del terreno para aplicaciones energéticas como la cartografía geotérmica o la captura y el almacenamiento de carbono.
>
> **Generar modelos 3D a partir de datos 2D** — GAN puede generar modelos 3D a partir de fotografías 2D o imágenes escaneadas. Por ejemplo, en el cuidado de la salud, GAN combina radiografías y otras exploraciones corporales para crear imágenes realistas de los órganos destinadas a la planificación y simulación quirúrgicas.

**Cierre comercial** (resumido — es marketing de producto): la página termina ofreciendo Amazon SageMaker (preparar datos, construir, entrenar y desplegar modelos), Amazon Bedrock (acceso a modelos fundacionales por API) y AWS DeepComposer (teclado musical para entrenar GANs de música), más una llamada a crear una cuenta.
