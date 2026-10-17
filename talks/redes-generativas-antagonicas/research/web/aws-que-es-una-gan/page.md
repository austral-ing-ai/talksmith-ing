# ¿Qué es una GAN? - Explicación sobre las redes generativas antagónicas - AWS

_Source: <https://aws.amazon.com/es/what-is/gan/>_

[Saltar al contenido principal](#aws-page-content-main) 

# ¿Qué es una GAN?

[Cree una cuenta de AWS](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?pg=what_is_header) [¿Qué es una GAN?](#ams#what-isc1#pattern-data) [¿Cuáles son algunos casos de uso de las redes generativas antagónicas?](#ams#what-isc2#pattern-data) [¿Cómo funciona una red generativa antagónica?](#ams#what-isc3#pattern-data) [¿Cuáles son los tipos de redes generativas antagónicas?](#ams#what-isc4#pattern-data) [¿Cómo puede AWS respaldar sus requisitos redes generativas antagónicas?](#ams#what-isc5#pattern-data) 

## ¿Qué es una GAN?

Una red generativa antagónica (GAN) es una arquitectura de [aprendizaje profundo](/es/what-is/deep-learning/). Entrena dos redes neuronales de modo que compitan entre sí para generar nuevos datos más auténticos a partir de un conjunto de datos de entrenamiento determinado. Por ejemplo, es posible generar nuevas imágenes a partir de una base de datos de imágenes existente, así como música original a partir de una base de datos de canciones. Una GAN se denomina *antagónica* porque entrena dos redes diferentes y las enfrenta entre sí. Una red genera nuevos datos al tomar una muestra de datos de entrada y modificarla en la medida de lo posible. La otra red intenta predecir si la salida de datos generada pertenece al conjunto de datos original. En otras palabras, la red de predicción determina si los datos generados son falsos o reales. El sistema genera versiones nuevas y mejoradas de valores de datos falsos hasta que la red de predicción ya no puede distinguir el falso del original.

## ¿Cuáles son algunos casos de uso de las redes generativas antagónicas?

La arquitectura GAN tiene varias aplicaciones en diferentes sectores. A continuación, presentamos algunos ejemplos.

### **Generar imágenes**

Las redes generativas antagónicas crean imágenes realistas mediante indicaciones basadas en texto o modificando las imágenes existentes. Pueden ayudar a crear experiencias visuales realistas e inmersivas en videojuegos y entretenimiento digital.

GAN también puede editar imágenes, como convertir una imagen de baja resolución en una de alta resolución o convertir una imagen en blanco y negro en color. También puede crear rostros, personajes y animales realistas para animación y video.

### **Generar datos de entrenamiento para otros modelos **

En el [aprendizaje automático (ML)](/es/what-is/machine-learning/), el aumento de datos aumenta artificialmente el conjunto de entrenamiento mediante la creación de copias modificadas de un conjunto de datos a partir de los datos existentes.

Puede utilizar modelos generativos para el aumento de datos a fin de crear datos sintéticos con todos los atributos de los datos del mundo real. Por ejemplo, puede generar datos de transacciones fraudulentas que luego se utilizan para entrenar a otro sistema de ML de detección de fraudes. Estos datos pueden enseñar al sistema a distinguir con precisión entre transacciones sospechosas y auténticas.

### **Completar la información faltante **

En ocasiones, es posible que desee que el modelo generativo adivine con precisión y complete alguna información faltante en un conjunto de datos.

Por ejemplo, puede entrenar a GAN para que genere imágenes de la superficie subterránea (subsuelo) mediante la comprensión de la correlación entre los datos de la superficie y las estructuras subterráneas. Al estudiar las imágenes conocidas de la subsuelo, puede crear otras nuevas utilizando mapas del terreno para aplicaciones energéticas como la cartografía geotérmica o la captura y el almacenamiento de carbono.

### **Generar modelos 3D a partir de datos 2D**

GAN puede generar modelos 3D a partir de fotografías 2D o imágenes escaneadas. Por ejemplo, en el cuidado de la salud, GAN combina radiografías y otras exploraciones corporales para crear imágenes realistas de los órganos destinadas a la planificación y simulación quirúrgicas.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2021/11/11/ML-6149-image005-500.jpg)<https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2021/11/11/ML-6149-image005-500.jpg>   

## ¿Cómo funciona una red generativa antagónica?

*Un sistema de redes generativas antagónicas consta de dos redes neuronales profundas: la *red generadora* y la red discriminadora*. Ambas redes se entrenan en un juego antagónico, en el que una intenta generar nuevos datos y la otra intenta predecir si la salida es falsa o real.

Técnicamente, GAN funciona de la siguiente manera. Una ecuación matemática compleja constituye la base de todo el proceso de computación, pero esta es una visión general simplista:

1. La red neuronal del generador analiza el conjunto de entrenamiento e identifica los atributos de los datos 
2. La red neuronal discriminadora también analiza los datos de entrenamiento inicial y distingue entre los atributos de forma independiente 
3. El generador modifica algunos atributos de los datos al agregar ruido (o cambios aleatorios) a determinados atributos 
4. El generador transfiere los datos modificados al discriminador 
5. El discriminador calcula la probabilidad de que la salida generada pertenezca al conjunto de datos original 
6. El discriminador proporciona alguna orientación al generador para reducir la aleatorización del vector de ruido en el siguiente ciclo 

El generador intenta maximizar la probabilidad de error del discriminador, pero este último intenta minimizar la probabilidad de error. En las iteraciones de entrenamiento, tanto el generador como el discriminador evolucionan y se enfrentan de forma continua hasta alcanzar un estado de equilibrio. En el estado de equilibrio, el discriminador ya no puede reconocer los datos sintetizados. En este punto, termina el proceso de formación.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2021/11/11/ML-6149-image025.jpg)<https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2021/11/11/ML-6149-image025.jpg>   

### **Ejemplo de formación GAN **

Contextualicemos lo anterior con un ejemplo del modelo GAN en la traducción de imagen a imagen.

Tenga en cuenta que la imagen de entrada es un rostro humano que GAN intenta modificar. Por ejemplo, los atributos pueden ser las formas de los ojos o de las orejas. Supongamos que el generador cambia las imágenes reales agregándoles gafas de sol. El discriminador recibe un conjunto de imágenes, algunas de personas reales con gafas de sol y algunas imágenes generadas que se modificaron para incluir gafas de sol.

Si el discriminador puede diferenciar entre lo falso y lo real, el generador actualiza sus parámetros para generar imágenes falsas aún mejores. Si el generador produce imágenes que engañan al discriminador, el discriminador actualiza sus parámetros. La competencia mejora ambas redes hasta que se alcanza el equilibrio.

## ¿Cuáles son los tipos de redes generativas antagónicas?

Existen diferentes tipos de modelos GAN según las fórmulas matemáticas utilizadas y las diferentes formas en que el generador y el discriminador interactúan entre sí.

A continuación, damos algunos modelos de uso común, pero la lista no es exhaustiva. Existen muchos otros tipos de GAN, como StyleGAN, CycleGAN y DiscoGAN, que resuelven diferentes tipos de problemas.

### **Vanilla GAN**

Este es el modelo GAN básico que genera variaciones de datos con poca o ninguna retroalimentación de la red discriminadora. Un Vainilla GAN suele requerir mejoras para la mayoría de los casos de uso en el mundo real.

### **Conditional GAN**

Una conditional GAN (cGAN) introduce el concepto de condicionamiento, lo que permite la generación de datos específicos. El generador y el discriminador reciben información adicional, por lo general, etiquetas de clase u otra forma de datos condicionantes.

Por ejemplo, si se generan imágenes, la condición podría ser una etiqueta que describa el contenido de la imagen. El condicionamiento permite al generador producir datos que cumplen condiciones específicas.

### **Deep convolutional GAN**

Al reconocer el poder de las redes neuronales convolucionales (CNN) en el procesamiento de imágenes, Deep convolutional GAN (DCGAN) integra arquitecturas CNN en GAN.

Con DCGAN, el generador utiliza convoluciones transpuestas para aumentar la distribución de los datos, y el discriminador también utiliza capas convolucionales para clasificar los datos. El DCGAN también introduce directrices de arquitectura para hacer que la capacitación sea más estable.

### **Super-resolution GAN**

Los Super-resolution GANS (SRGANs) se centran en la ampliación de imágenes de baja resolución a alta resolución. El objetivo es mejorar las imágenes a una resolución más alta y, al mismo tiempo, mantener la calidad y los detalles de la imagen.

Las Laplacian Pyramid GANs (LAPGANs) enfrentan el desafío de generar imágenes de alta resolución al dividir el problema en etapas. Utilizan un enfoque jerárquico, con múltiples generadores y discriminadores que trabajan en diferentes escalas o resoluciones de la imagen. El proceso comienza con la generación de una imagen de baja resolución cuya calidad mejora en las etapas progresivas de GAN.

## ¿Cómo puede AWS respaldar sus requisitos redes generativas antagónicas?

Amazon Web Services (AWS) ofrece muchos servicios para satisfacer sus requisitos de GAN.

[Amazon SageMaker](/es/sagemaker/) es un servicio totalmente administrado que puede usar para preparar datos y crear, entrenar e implementar modelos de aprendizaje automático. Estos modelos se pueden utilizar en muchos escenarios, y SageMaker incluye una infraestructura, herramientas y flujos de trabajo totalmente administrados. Cuenta con una amplia gama de características para acelerar el desarrollo y la formación de GAN para cualquier aplicación.

[Amazon Bedrock](/es/bedrock/) es un servicio totalmente gestionado. Puede utilizarlo para acceder a modelos fundacionales (FM), o redes neuronales profundas entrenadas, de Amazon y de las principales startups de inteligencia artificial (IA). Estos FM están disponibles a través de las API, por lo que puede elegir entre varias opciones para encontrar el modelo que mejor se adapte a sus necesidades. Puede utilizar estos modelos en sus propias aplicaciones de GAN. Con Amazon Bedrock, puede desarrollar e implementar aplicaciones de IA generativa escalables, confiables y seguras con mayor rapidez. Y no tiene que administrar la infraestructura.

[AWS DeepComposer](/) le ofrece una forma creativa de comenzar con el aprendizaje automático. Ponga manos a la obra con un teclado musical y las técnicas de machine learning más novedosas, diseñadas para aumentar sus habilidades de ML. Cualquiera que sea su experiencia en ML o música, sus desarrolladores pueden empezar a trabajar con GAN. Y pueden entrenar y optimizar modelos GAN para crear música original.

Cree una [cuenta](https://portal.aws.amazon.com/billing/signup) hoy mismo para comenzar con las redes generativas de adversarios en AWS.

## Siguientes pasos en AWS

### 

[Descubra otros recursos relacionados con el productoGenere innovaciones más rápido con los servicios de IA generativa de AWS](/es/ai/generative-ai/services/) 

### 

[Regístrese para obtener una cuenta gratuitaObtenga acceso instantáneo al nivel gratuito de AWS.Regístrese](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) 

### 

[Comience a crear en la consolaComience a crear en la Consola de administración de AWS.Inicie sesión](https://console.aws.amazon.com) 

## Browse all cloud computing concepts

Browse all cloud computing concepts content here:

Cargando Cargando Cargando Cargando Cargando 

## Did you find what you were looking for today?

Let us know so we can improve the quality of the content on our pages

Yes No
