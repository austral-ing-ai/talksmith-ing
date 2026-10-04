---
presentation: Inteligencia Artificial Generativa (AI Gen)
class: "Sistemas multiagente: especialización, contexto y orquestación"
research: research/corpus/
description: Slides are grouped into Sections. Each Section contains one or more Slides.
presenter: Paulo Veiga, Claudio Righetti, Marco Sorondo (Universidad Austral)
audience: Estudiantes de grado de Ingeniería Informática y Ciencia de Datos con base técnica fuerte; ya vieron prompting, RAG, MCP (FastMCP y OpenAI Agents SDK), transformers y entrenamiento de LLMs
duration: 90 min
date: 2026-10-07
---

# Thesis

**Claim:** Un sistema multiagente conviene cuando partir el trabajo le da a cada agente un contexto chico y limpio, sus propias herramientas y la posibilidad de correr en paralelo con los demás. Elegir la arquitectura es decidir quién elige el próximo paso y qué ve cada agente, y esa decisión se mide en llamadas al modelo, tokens y fallas.

**Why it matters:** En el trabajo práctico los alumnos van a resolver un benchmark con un LLM débil y barato. Con un solo agente, ese modelo se pierde entre herramientas y contexto acumulado. Con agentes especializados y contexto aislado, el mismo modelo puede alcanzar; sumar un agente sin LLM que verifique es optativo y da puntos extra. Para defender su arquitectura van a comparar un agente único con todas las herramientas contra al menos tres arquitecturas más, con logs, tokens y rendimiento de cada una.

**Presenter feedback:**

---

# Agenda

**Narrative arc:** La clase arranca por la definición formal de agente de Russell y Norvig, término por término y con agentes de ejemplo muy distintos, y lee con ella al agente basado en LLM que los alumnos ya programaron con el Agents SDK (1). Después muestra por qué un solo agente se queda corto: el contexto es finito, las herramientas se pisan y un único system prompt no especializa; de ahí salen las tres palancas de un sistema multiagente (2). El bloque central toma un caso ficticio, Pampa Viajes, y reparte los mismos cuatro roles en siete arquitecturas, con lo que gana y pierde cada una y una tabla de costos para elegir (3). Siguen las implementaciones publicadas que llevan esas arquitecturas a la práctica (4) y un bloque propio para la arquitectura más flexible: un agente principal caro que despierta subagentes cuando los necesita, con el caso de Anthropic, el contrapunto de Cognition y una demo en vivo con Claude Code (5). Dos bloques cortos cierran el panorama: multiagente antes de los LLM y agentes simbólicos dentro de un sistema con LLM (6), y cómo fallan estos sistemas (7). El cierre resume y anuncia el trabajo práctico.

**Sections (in delivery order):**

- 1. Qué es un agente, formalmente
- 2. Por qué un solo agente no alcanza
- 3. Arquitecturas base con un mismo ejemplo
- 4. Implementaciones reales
- 5. El agente principal que delega bajo demanda
- 6. Multiagente sin LLM
- 7. Cómo fallan
- Conclusiones

**Presenter feedback:**
- [closed] 2026-10-04 — "si, aplica lo que sugeris"
  Resolution: Compresión de 5,5 min aplicada: paso 4 de la demo 5.7 reducido a un solo mensaje de CODE-AGENT a los otros dos con nombre, texto y link fijados (demo de 6 a 4,5 min); 4.6 de 2 a 1 min con notas recortadas; 3.9 y 5.2 de 2,5 a 2; Conclusiones 2 de 3 a 2 con notas recortadas; 2.1 y 2.2 de 2 a 1,5. Total del deck: 84 de 90 min; salió la pregunta abierta de tiempos.

---

# 1. Qué es un agente, formalmente

**Goal of this section:** Definir uno por uno los términos de Russell y Norvig (ambiente, sensores, percepciones, actuadores, acciones, función y programa de agente, medida de performance, racionalidad, autonomía, PEAS y tipos de ambiente), instanciarlos en agentes bien distintos (aspiradora, termostato, robot móvil, AlphaGo, taxi autónomo, asistente con LLM) y usarlos para leer al agente basado en LLM. La sección deja instalada la distinción entre workflow y agente, que reaparece en cada arquitectura del bloque 3.

**Presenter feedback:**
- [closed] 2026-10-04 — "estas definiendo que es un agente suponiendo que los alumnos saben que es performance, ambiente, actuadores, sensores, etc. no das definiciones de los terminos elementales de los agentes. das solo el ejemplo de la grilla como instancia de todo eso sin variantes, agrega todo esto que falta al principio a pesar de que implique agregar diapositivas"
  Resolution: La sección 1 pasó de 7 a 13 láminas: seis nuevas definen uno por uno ambiente, sensores, percepción y secuencia (1.2), actuadores y acciones con el lazo en ASCII (1.3), función y programa de agente con el termostato (1.4), omnisciencia y autonomía con el diagrama del agente que aprende y AlphaGo Zero (1.6), PEAS de aspiradora, robot móvil, AlphaGo y taxi lado a lado (1.7) y siete ambientes clasificados en tabla con crucigrama, ajedrez, taxi y asistente con LLM (1.9); 1.5 define la medida de performance, 1.8 vuelve a poner las siete dimensiones con definición y ejemplo, y 1.10 y 1.11 usan los términos ya definidos; tiempo de la sección de 10,5 a 18 min, total 89,5 de 90, compresiones propuestas en Open questions.

---

## 1. Agente: percibe y actúa
<!-- template: quote -->

### Content

**"An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators."**
Russell y Norvig, *Artificial Intelligence: A Modern Approach*

- **Lo que la definición no menciona.** Machine learning, LLMs, herramientas o RAG. Tampoco software: un termostato o un insecto también entran.
- **Un LLM solo no es un agente.** Le faltan el ambiente, los sensores y los actuadores. El agente es el sistema que lo rodea.

<!-- generate-image: right | percibir y actuar: una entidad abierta al mundo por un lado que recibe y por otro que modifica -->

### Sources

- `aig4b-clase-6-agentes-biomedica.pdf.md` (láminas "¿Qué es un agente?" y "Comentarios sobre la definición"): la cita de Russell y Norvig, "Un LLM no es un agente por sí solo", y la lista de lo que la definición no menciona.
- `russell-norvig-aima.web.md`: el libro dedica el capítulo 2 a "Intelligent Agents" y el 18 a "Multiagent Decision Making" (la captura es solo el índice).
- `wikipedia-intelligent-agent.web.md` (Key claims, General definition): "A basic thermostat or control system is considered an intelligent agent".

### Speaker notes

La tensión de la clase en una línea: un LLM débil, solo, se pierde entre herramientas y contexto, y el trabajo práctico les va a pedir que lo hagan rendir repartiendo el trabajo entre agentes. Arrancamos por la definición de libro porque la palabra "agente" se usa para cualquier cosa que tenga un LLM adentro. La definición es amplia a propósito: no dice nada de cómo está hecho el agente, solo que percibe y actúa. Eso nos deja comparar un agente con LLM con un robot de depósito o con un jugador de StarCraft, que van a aparecer en el bloque 6. La segunda viñeta es la que hay que dejar clara: el modelo es una pieza; el agente es el modelo más el lazo con el ambiente. Las próximas láminas definen cada palabra de la cita, una por una. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 2. Ambiente, sensores y percepciones
<!-- template: concept-breakdown -->

### Content

**Todo lo que el agente sabe del mundo le llega por sus sensores, una percepción a la vez.**

- **Ambiente.** La parte del mundo en la que el agente actúa y que cambia con sus acciones. La grilla de la aspiradora, el tablero de go, las calles por las que maneja un taxi.
- **Sensores.** Los canales por los que el agente recibe información del ambiente. El detector de suciedad de la aspiradora; la cámara y el LiDAR de un robot móvil.
- **Percepción.** Lo que entra por los sensores en un instante (en inglés, *percept*). Para un auto autónomo, las imágenes de cámara, los datos del LiDAR, la posición GPS y la velocidad de ese momento.
- **Secuencia de percepciones.** Todo lo que el agente percibió desde que arrancó. Para un termostato, cada lectura de temperatura desde que se encendió. El conjunto de todas las secuencias posibles se escribe P\*.

### Sources

- `wikipedia-intelligent-agent.web.md` (Definitions y Raw excerpts, "Agent function"): percept = "the agent's sensory inputs at a single point in time", con el ejemplo del auto autónomo ("camera images, lidar data, GPS coordinates, and speed readings at a specific instant"); P\* = "the set of all possible *percept sequences* (the agent's entire perceptual history)"; Russell y Norvig describen la IA como "the study of agents that receive percepts from an environment and perform actions".
- `aig4b-clase-6-agentes-biomedica.pdf.md` (láminas "Ejemplo: Vacuum Cleaner", "Ejemplo: Robot Móvil", "Ejemplo: DeepMind AlphaGo" y "Racionalidad"): sensores de la aspiradora (detector de suciedad, posición en la grilla) y del robot móvil (cámara, LiDAR, GPS, giroscopio, proximidad); tablero de go como ambiente; secuencia de percepciones como "el historial de todo lo que el agente ha observado del ambiente hasta el momento".

### Speaker notes

Cuatro términos para todo lo que entra al agente. El ambiente es lo que está afuera y el agente modifica; los sensores son la puerta de entrada. La percepción es de un instante y la secuencia las acumula todas. La distinción importa enseguida: la función de agente de la próxima lámina toma la secuencia entera, mientras que el programa ve una percepción por vez. P\* lleva la estrella porque una secuencia puede tener cero, una o muchas percepciones. Si alguien pregunta por el agente con LLM: sus percepciones son los mensajes y los resultados de herramientas que le entran al contexto, y lo vamos a ver en la lámina 1.11. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 3. Actuadores y acciones
<!-- template: concept-breakdown -->

### Content

**El agente modifica el ambiente con sus actuadores, y en cada paso elige una acción de un conjunto fijo.**

- **Actuadores.** Las piezas con las que el agente modifica el ambiente. El motor de succión de la aspiradora; el acelerador, el freno y la dirección de un taxi.
- **Acciones.** Las órdenes que el agente puede dar a sus actuadores. El conjunto de todas se escribe A. La aspiradora elige entre Aspirar, MoverIzquierda, MoverDerecha y Esperar; el taxi, entre acelerar, frenar y girar.

```ascii
+------------------------+             +------------------+
|        AGENTE          |             |     AMBIENTE     |
|                        |  percepción |                  |
|   sensores  <----------+-------------+                  |
|      |                 |             |                  |
|      v                 |             |                  |
|   ¿qué acción?         |             |                  |
|      |                 |   acción    |                  |
|      v                 |             |                  |
|   actuadores ----------+------------>|                  |
+------------------------+             +------------------+
```
<!-- ascii-note:
intent: el lazo mínimo agente-ambiente: la percepción entra por los sensores, la acción sale por los actuadores y cambia el ambiente
emphasize: la caja "¿qué acción?", que es lo que las láminas siguientes formalizan (función y programa de agente)
labels: "AGENTE", "AMBIENTE", "sensores", "actuadores", "percepción", "acción", "¿qué acción?"
-->

### Sources

- `wikipedia-intelligent-agent.web.md` (Key claims y Raw excerpts): un agente "acts upon that environment through actuators"; A = "the set of all possible *actions* the agent can take"; para el auto autónomo, "decide on its next action (e.g., accelerate, brake, turn)". Imagen de referencia del lazo: `wikipedia-intelligent-agent.web/images/IntelligentAgent-SimpleReflex.png` (percepts → Sensors … Actuators → actions), que no se usa porque agrega las reglas del agente reflejo.
- `aig4b-clase-6-agentes-biomedica.pdf.md` (lámina "Ejemplo: Vacuum Cleaner"): actuadores (motor de movimiento, motor de succión) y acciones (Aspirar, MoverIzquierda, MoverDerecha, Esperar).

### Speaker notes

Actuador y acción se confunden fácil. El actuador es la pieza: el motor, el volante, la API que se llama. La acción es la orden concreta que el agente elige en un paso, y A es el menú completo de órdenes posibles. La caja del medio del diagrama, "¿qué acción?", es lo único que distingue a un agente de otro con los mismos sensores y actuadores; las dos láminas que siguen la formalizan. Los actuadores del taxi salen de sus acciones (acelerar, frenar, girar). Tiempo objetivo: ~1 min.

### Presenter feedback

---

## 4. Función de agente y programa de agente
<!-- template: concept-columns -->

### Content

**El comportamiento de un agente se describe con una función matemática y se implementa con un programa.**

- **Función de agente.** f: P\* → A. Asigna una acción a cada secuencia de percepciones posible. Es una especificación abstracta y nadie la ejecuta. Para el termostato, asigna "encender" a toda historia de lecturas cuya última quedó bajo el umbral, y "apagar" al resto.
- **Programa de agente.** El código que corre en el agente, sobre su arquitectura: el dispositivo con sus sensores y actuadores. Recibe la percepción actual y devuelve una acción; si necesita la historia, la tiene que guardar él. El del termostato entra en una regla: si la temperatura está bajo el umbral, encender; si no, apagar.

### Sources

- `wikipedia-intelligent-agent.web.md` (Definitions y Raw excerpts, "Agent function"): f : P\* → A "maps the agent's entire history of percepts to an action" (Russell y Norvig 2003, p. 33); "the agent function (an abstract mathematical concept)" y "the agent program (the concrete implementation of that function)"; el programa "is the actual code that runs on the agent" y "takes the *current* percept as input"; el termostato "turns on or off when the temperature drops below a certain point"; el agente con modelo mantiene un estado "that depends on the percept history".

### Speaker notes

Esta es la distinción que más se pierde en el uso diario. La función es la descripción completa de qué haría el agente ante cualquier historia; como tabla, para casi cualquier agente sería infinita. El programa es lo que efectivamente corre, y ve solo la percepción de ahora. Si el agente necesita recordar, el programa guarda un estado: eso es el agente con modelo de la lámina 1.10. Ojo con la palabra arquitectura: acá es el hardware o la plataforma donde corre el programa; en el bloque 3 vamos a usar "arquitectura" para la forma en que se conectan varios agentes. Para un agente con LLM, la función es todo lo que el sistema haría ante cualquier conversación; el programa es el código del runner más el modelo. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 5. Racionalidad y medida de performance

### Content

**Un agente racional elige la acción que maximiza su medida de performance esperada, dada la secuencia de percepciones que vio y lo que sabía de antemano.**

- **Medida de performance.** El criterio que puntúa la secuencia de estados del ambiente que produjo el agente. La fija quien diseña el agente. La aspiradora suma 10 por limpiar una celda sucia y resta 1 por moverse, 5 por aspirar una celda limpia y 10 por chocar.
- **Cuatro factores.** La racionalidad depende de la medida de performance, el conocimiento previo, las acciones disponibles y la secuencia de percepciones.

### Sources

- `aig4b-clase-6-agentes-biomedica.pdf.md` (láminas "Racionalidad" y "Ejemplo: Vacuum Cleaner"): la cita "This notion of desirability is captured by a performance measure that evaluates any given sequence of environment states"; los cuatro factores; las recompensas de la aspiradora (+10 limpiar celda sucia, −1 moverse, −5 aspirar celda limpia, −10 chocar).
- `wikipedia-intelligent-agent.web.md` (Key claims): "A rational agent selects the action expected to maximize its performance measure, given its percept sequence, prior knowledge, and available actions"; la función de recompensa "allows programmers to shape its desired behavior".

### Speaker notes

La medida de performance es lo que convierte "hace algo" en "hace lo correcto". Dos detalles de la definición. Puntúa estados del ambiente, lo que pasó en el mundo, y la escribe el diseñador: si el agente se pusiera su propia nota, podría convencerse de que lo hizo bien. Con la aspiradora se ve que la recompensa define el comportamiento: si moverse no costara nada, el agente pasearía. La palabra "esperada" importa y la retomamos en la lámina siguiente. Vamos a volver a esta idea en el trabajo práctico, porque el benchmark es la medida de performance del sistema y cada agente interno va a necesitar la suya. Tiempo objetivo: ~1 min.

### Presenter feedback

---

## 6. Omnisciencia y autonomía

### Content

**Un agente racional decide bien con la información que tiene. Puede fallar y seguir siendo racional.**

- **Omnisciencia.** Conocer el resultado real de cada acción antes de elegirla. La racionalidad no la exige: juzga el resultado esperado con la información disponible. Un taxi que frena bien ante lo que ve y recibe un choque de un auto que no podía ver actuó de forma racional.
- **Autonomía.** Apoyarse en lo que el agente percibe y aprende más que en el conocimiento previo de quien lo diseñó. Aprender le permite corregir un conocimiento inicial incompleto o equivocado. AlphaGo Zero aprendió go sin partidas humanas, jugando contra sí mismo.

![Agente que aprende: crítico, elemento de aprendizaje, elemento de performance y generador de problemas](research/corpus/wikipedia-intelligent-agent.web/images/500px-IntelligentAgent-Learning.svg.png)

### Sources

- `wikipedia-intelligent-agent.web.md` (Key claims y Raw excerpts): la racionalidad "does not require an agent to be omniscient or always successful; it concerns the expected outcome of an action on the basis of the information available to the agent"; los agentes que aprenden pueden "begin in unknown environments and gradually surpass the bounds of their initial knowledge", con cuatro componentes (elemento de aprendizaje, elemento de performance, crítico, generador de problemas); imagen `wikipedia-intelligent-agent.web/images/500px-IntelligentAgent-Learning.svg.png` ("A general learning agent"; dice "Effectors" por actuadores y "Perfomance Standard" con error de tipeo).
- `aig4b-clase-6-agentes-biomedica.pdf.md` (lámina "De AlphaGo Zero a AlphaZero"): AlphaGo Zero "aprende desde cero sin datos humanos, solo autojuego y retroalimentación".

### Speaker notes

Racional y omnisciente son cosas distintas. Si exigiéramos omnisciencia, ningún agente real sería racional, porque ninguno ve el futuro. Lo que se le pide es que use bien lo que sabe y lo que percibió. Con la autonomía va la otra cara: un agente que solo ejecuta lo que le cargó su diseñador falla cuando ese conocimiento está incompleto o equivocado, y aprender le permite corregirlo. El diagrama es el agente que aprende: el crítico compara lo que pasó con el estándar de performance y el elemento de aprendizaje ajusta al elemento de performance, que es el agente de las láminas anteriores. "Effectors" en el diagrama es otro nombre de los actuadores. Tiempo objetivo: ~1 min.

### Presenter feedback

---

## 7. PEAS en cuatro agentes
<!-- template: value-columns -->
<!-- design: full -->

### Content

**PEAS (Performance, Environment, Actuators, Sensors) es la ficha con la que se especifica un agente antes de programarlo. Los mismos cuatro casilleros se llenan de formas muy distintas.**

| | Aspiradora | Robot móvil | AlphaGo | Taxi autónomo |
|---|---|---|---|---|
| **Performance** | celdas limpias, con penalidad por moverse, aspirar en vano y chocar | llegar rápido al destino, sin colisiones y con poco consumo de energía | ganar la partida (1 si gana, 0 si pierde) | seguridad, velocidad y comodidad del pasajero |
| **Ambiente** | grilla n × m | interior o exterior, con obstáculos | tablero de go de 19 × 19 | calles con tráfico |
| **Actuadores** | motor de movimiento, motor de succión | tracción, dirección, frenos, brazo robótico | colocar una piedra o pasar el turno | acelerador, freno, dirección |
| **Sensores** | detector de suciedad, posición en la grilla | cámara, LiDAR, GPS, giroscopio, proximidad | estado del tablero | cámaras, LiDAR, GPS, velocímetro |

### Sources

- `aig4b-clase-6-agentes-biomedica.pdf.md` (láminas "Ejemplo: Vacuum Cleaner", "Ejemplo: Robot Móvil" y "Ejemplo: DeepMind AlphaGo"): las tres primeras columnas (formulaciones "PEAS-like").
- `wikipedia-intelligent-agent.web.md` (Raw excerpts, "Agent function" y "Objective function"; Evidence): taxi a partir del auto autónomo (percepciones: "camera images, lidar data, GPS coordinates, and speed readings"; acciones: "accelerate, brake, turn"; objetivo que balancea "safety, speed, and passenger comfort"); go: "1 for a win, 0 for a loss". Los actuadores del taxi se derivan de sus acciones.
- La sigla PEAS como nombre de la ficha viene del capítulo 2 de Russell y Norvig, que no está en el corpus (ver Open questions).

### Speaker notes

La ficha obliga a pensar el problema antes de escribir código. Leer la tabla por filas. La performance va de un puntaje con penalidades a ganar o perder; el ambiente, de una grilla a una ciudad; los actuadores, de un motor a una piedra sobre un tablero. AlphaGo mide 1 o 0 por partida, y lo que maximiza en cada jugada es la probabilidad de ganar, que es la performance esperada de la lámina 1.5. El termostato tiene la ficha más chica posible: mantener la temperatura, una habitación, la caldera y un sensor de temperatura. El asistente con LLM tiene su ficha en la lámina 1.11. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 8. Tipos de ambiente
<!-- template: concept-breakdown -->
<!-- format: editorial -->

### Content

**El ambiente define cuán difícil es el problema. Russell y Norvig lo clasifican en siete dimensiones.**

- **Observable.** Completo si los sensores captan en cada momento todo lo que importa para decidir; parcial si una parte queda oculta. El ajedrez es completo; el taxi no ve detrás de un camión.
- **Agentes.** Uno solo o varios. Con varios, interactúan de forma colaborativa, competitiva o ambas, y cada uno es parte del ambiente de los demás. El crucigrama es de uno; el ajedrez, competitivo.
- **Determinismo.** Determinístico si el estado actual y la acción fijan el estado siguiente; estocástico si interviene el azar. Una jugada de ajedrez tiene un solo resultado; al taxi se le puede pinchar una goma.
- **Episódico o secuencial.** Episódico si cada decisión es independiente de las anteriores; secuencial si una acción tiene consecuencias a largo plazo. Clasificar mails como spam de a uno es episódico; una partida de ajedrez, secuencial.
- **Estático o dinámico.** Dinámico si el ambiente cambia mientras el agente delibera. El crucigrama espera; el tráfico sigue.
- **Discreto o continuo.** Discreto si los estados y las acciones son finitos. El ajedrez es discreto; la velocidad del taxi y el giro del volante son continuos.
- **Conocido o desconocido.** Conocido si el agente sabe las reglas del ambiente, qué produce cada acción. Las reglas del ajedrez se conocen; ante un videojuego nuevo, el agente tiene que descubrir qué hace cada botón.

### Sources

- `aig4b-clase-6-agentes-biomedica.pdf.md` (lámina "Tipos de Ambientes"): las siete dimensiones y las definiciones de episódico ("acciones independientes vs. acciones con consecuencias a largo plazo"), dinámico ("el ambiente cambia o no mientras el agente delibera"), discreto ("estados y acciones finitos vs. infinitos") y conocido ("el agente conoce o no las reglas del ambiente"); (lámina "Dificultad de Ambientes") crucigrama, ajedrez y taxi; (Key claims, sistemas multiagente) agentes que interactúan "de forma colaborativa, competitiva, o ambas".
- `wikipedia-intelligent-agent.web.md` (Raw excerpts, "Model-based reflex agents"): parcialmente observable, con "the part of the world which cannot be seen".
- Las definiciones de observable y determinístico, y los ejemplos de spam, goma pinchada y videojuego, son redacción del editor sobre el capítulo 2 de Russell y Norvig, que no está en el corpus (ver Open questions).

### Speaker notes

Siete dimensiones, cada una con un ejemplo de cada lado. La que más importa hoy es la cantidad de agentes. Con más de uno, lo que otro agente hace le llega a cada uno como una percepción. Colaborativo es el caso de Pampa Viajes y del trabajo práctico; competitivo es el ajedrez o StarCraft, que vamos a ver al final. Los sistemas con LLM que vamos a estudiar son casi todos colaborativos. Dos que se confunden: parcialmente observable habla de lo que el agente ve ahora; desconocido, de si sabe qué producen sus acciones. Un agente puede conocer las reglas de un juego de cartas y aun así no ver la mano del rival. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 9. Cuatro ambientes clasificados
<!-- template: value-columns -->
<!-- design: full -->

### Content

**Crucigrama, ajedrez y taxi van de fácil a difícil. El asistente con LLM queda del lado del taxi en casi todas las dimensiones.**

| | Crucigrama | Ajedrez | Taxi autónomo | Asistente con LLM |
|---|---|---|---|---|
| **Observable** | completo | completo | parcial | parcial |
| **Agentes** | uno | dos, competitivo | muchos, competitivo y colaborativo | uno o varios, colaborativo |
| **Determinismo** | determinístico | determinístico | estocástico | estocástico |
| **Episódico o secuencial** | secuencial | secuencial | secuencial | secuencial |
| **Estático o dinámico** | estático | estático (sin reloj) | dinámico | dinámico |
| **Discreto o continuo** | discreto | discreto | continuo | discreto |
| **Conocido o desconocido** | conocido | conocido | conocido | en parte |

### Sources

- `aig4b-clase-6-agentes-biomedica.pdf.md` (lámina "Dificultad de Ambientes"): crucigrama "observable, determinístico, estático. Un solo agente"; ajedrez "observable y determinístico, pero competitivo"; taxi "parcialmente observable, estocástico, dinámico, continuo, multi-agente"; (lámina de sistemas multiagente) taxi "competitivo + colaborativo"; (lámina "Agente basado en LLM como agente inteligente") el agente con LLM en un "entorno digital, simbólico, parcialmente observable, dinámico".
- Las demás celdas (episódico o secuencial en las cuatro columnas; discreto y conocido en crucigrama y ajedrez; conocido en el taxi; agentes, determinismo, discreto y conocido en el asistente; "sin reloj" en el ajedrez) son clasificación del editor con los criterios de la lámina 1.8 (ver Open questions).

### Speaker notes

Leer la columna del asistente al final, porque es la que vamos a usar toda la clase. Es parcialmente observable: solo sabe lo que le entra al contexto. Es estocástico aunque el modelo respondiera siempre igual, porque el ambiente incluye herramientas, APIs y un usuario cuyas respuestas no controla. Es dinámico: un archivo o una página pueden cambiar mientras razona. Es discreto, porque todo lo que entra y sale es texto. Y es conocido en parte: sabe qué hace cada herramienta solo por su descripción, hasta que la llama. La fila de agentes es la que abre el bloque 2: con un asistente solo, el otro agente del ambiente es el usuario; en un sistema multiagente, son los demás agentes. El ajedrez con reloj pasa a ser dinámico. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 10. Arquitecturas clásicas de agente
### Content

**Russell y Norvig ordenan los agentes según lo que hay entre la percepción y la acción. Cada tipo agrega una pieza al anterior.**

![Agente basado en modelo y en utilidad](research/corpus/wikipedia-intelligent-agent.web/images/500px-Model_based_utility_based.png)

- **Reflejo simple.** Una regla condición-acción ("si condición, entonces acción") sobre la percepción actual, como el programa del termostato. Solo funciona si el ambiente es completamente observable.
- **Reflejo con modelo.** Guarda un estado interno con la parte del mundo que no ve.
- **Con objetivos.** Predice qué pasaría con cada acción y elige la que lleva a un estado meta.
- **Con utilidad.** Puntúa los estados con una función de utilidad y elige la acción de mayor utilidad esperada.
- **BDI.** Creencias, deseos e intenciones (los planes a los que se comprometió). Separa elegir un plan de ejecutarlo.

### Sources

- `wikipedia-intelligent-agent.web.md` (Key claims, "Classic taxonomy"): las clases de Russell y Norvig (2003, cap. 2) con sus definiciones; la regla condición-acción "if condition, then action"; imagen `wikipedia-intelligent-agent.web/images/500px-Model_based_utility_based.png` ("Model-based, utility-based agent"), última de una serie que agrega un bloque por diagrama.
- `bdi-agents.web.md` (Key claims y Definitions): creencias, deseos e intenciones; BDI "provides a mechanism for separating the activity of selecting a plan … from the execution of currently active plans"; es la arquitectura de un solo agente racional y "does not explicitly describe mechanisms for interaction with other agents".

### Speaker notes

Contexto rápido; si el tiempo aprieta, se pasa en medio minuto. El diagrama es el más completo de la serie: estado interno, modelo de cómo evoluciona el mundo, predicción de cada acción y una utilidad que la puntúa. El quinto tipo de Russell y Norvig, el agente que aprende, ya apareció en la lámina 1.6: mejora cualquiera de estos cuatro con un crítico. BDI vale la mención porque es lo más parecido, en el mundo simbólico, a un agente que planifica y se compromete con un plan, y porque el propio artículo aclara que BDI no dice nada sobre cómo hablan varios agentes entre sí. Esa parte la cubren protocolos como Contract Net, en el bloque 6. Tiempo objetivo: ~1 min.

### Presenter feedback

---

## 11. El agente basado en LLM, con la misma definición

### Content

**Un agente basado en LLM es un modelo de lenguaje que usa herramientas en un lazo con el ambiente. Su ficha PEAS tiene los mismos cuatro casilleros que la del taxi.**

| | Agente basado en LLM |
|---|---|
| **Performance** | calidad y precisión de la respuesta, éxito de la tarea |
| **Ambiente** | digital y simbólico |
| **Actuadores** | generar texto, llamar herramientas y APIs, ejecutar comandos |
| **Sensores** | texto del usuario, contexto previo, resultados de herramientas |

- **Definición operativa.** "LLMs autonomously using tools in a loop", la que usa Anthropic.
- **En el Agents SDK.** "An agent is an LLM equipped with instructions, tools and handoffs": el mismo objeto que usaron en la misión de RAG y MCP.

### Sources

- `aig4b-clase-6-agentes-biomedica.pdf.md` (lámina "Agente basado en LLM como agente inteligente"): sensores, actuadores, ambiente ("entorno digital, simbólico") y performance del agente con LLM.
- `anthropic-multi-agent-research-system.web.md` (Definitions): "LLMs autonomously using tools in a loop".
- `anthropic-context-engineering.web.md` (Key claims): la misma definición, atribuida a Simon Willison.
- `openai-agents-sdk-multi-agent.web.md` (Key claims): "An agent is an LLM equipped with instructions, tools and handoffs."

### Speaker notes

Acá se cruzan las dos mitades de la materia. Ya armaron un agente con el SDK de OpenAI y un servidor MCP; lo que hicieron, leído con Russell y Norvig, es un agente cuyos sensores son mensajes y resultados de herramientas y cuyos actuadores son llamadas a herramientas. Cada mensaje o resultado que entra es una percepción, y el historial de la conversación es la secuencia de percepciones. Las acciones son las llamadas que el modelo puede emitir, y el conjunto A lo fija la lista de herramientas. El programa de agente es el runner del SDK más el modelo. El ambiente ya lo clasificamos en la lámina 1.9: es parcialmente observable, porque el agente solo sabe lo que entra en su contexto. Esa frase va a sostener toda la clase, porque un sistema multiagente es, en buena medida, una forma de decidir qué entra en el contexto de cada uno. Tiempo objetivo: ~1 min.

### Presenter feedback

---

## 12. El ciclo ReAct

### Content

**ReAct intercala razonamiento y acción: el modelo piensa, llama una herramienta, lee el resultado y repite hasta tener la respuesta.**

```ascii
        +-----------+
        |  pregunta |
        +-----+-----+
              |
              v
     +-----------------+
 +-->|   Thought       |  el modelo razona
 |   +--------+--------+
 |            |
 |            v
 |   +-----------------+
 |   |   Action        |  llama una herramienta
 |   +--------+--------+
 |            |
 |            v
 |   +-----------------+
 +---|   Observation   |  lee el resultado
     +--------+--------+
              |  alcanza
              v
       +-------------+
       | respuesta   |
       +-------------+
```
<!-- ascii-note:
intent: mostrar el lazo Thought -> Action -> Observation que se repite hasta la respuesta final
emphasize: la flecha de vuelta de Observation a Thought (el lazo); la salida "alcanza" hacia la respuesta
labels: "pregunta", "Thought", "Action", "Observation", "respuesta", "alcanza"
-->

- **Por qué funciona.** El razonamiento arma y corrige el plan; las acciones traen información de afuera y bajan la alucinación.
- **Es la unidad.** Cada agente de un sistema multiagente corre su propio ciclo como este.

### Sources

- `react-yao-2022.web.md` (Key claims): ReAct genera "both reasoning traces and task-specific actions in an interleaved manner"; los razonamientos "help the model induce, track, and update action plans", las acciones "interface with external sources"; en HotpotQA y Fever "overcomes issues of hallucination and error propagation".
- `aig4b-clase-6-agentes-biomedica.pdf.md` (lámina ReAct): ciclo Thought → Action → Observation, "la arquitectura más simple y fundamental".

### Speaker notes

Lo vieron implícito en el SDK: el runner del Agents SDK hace este lazo por ustedes. Lo dibujamos para tener la unidad a mano, porque en el bloque 3 cada caja de cada diagrama es uno de estos lazos. Cuando digamos "el subagente gasta muchos tokens y devuelve un resumen", lo que gasta tokens es este ciclo dando vueltas. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 13. Workflow o agente: quién decide el próximo paso

### Content

**La diferencia entre un workflow y un agente es quién elige el siguiente paso: el código o el modelo.**

- **Workflow.** "LLMs and tools are orchestrated through predefined code paths." El programador fija el orden; el modelo resuelve cada paso.
- **Agente.** El modelo "dynamically direct[s] [its] own processes and tool usage". Decide qué herramienta usar, cuándo y cuándo parar.
- **Se mezclan.** Un sistema real puede tener ruteo fijo entre agentes que adentro son autónomos.
- **La regla de Anthropic.** Empezar por lo más simple y sumar complejidad solo cuando mejora el resultado de forma medible.

### Sources

- `anthropic-building-effective-agents.web.md` (Key claims): las definiciones de workflow y agente citadas; "find the simplest solution possible, and only increasing complexity when needed"; "consider adding complexity *only* when it demonstrably improves outcomes".
- `openai-agents-sdk-multi-agent.web.md` (Key claims): dos formas de orquestar, "letting the LLM make decisions" y "orchestrating via code"; se pueden mezclar.
- `aig4b-clase-6-agentes-biomedica.pdf.md` (lámina del espectro): "La magia está en mezclarlos. Un sistema real puede tener routing determinista entre agentes que internamente son autónomos."

### Speaker notes

Esta distinción organiza el bloque 3. El pipeline y el router son workflows: el código decide. El orquestador, los handoffs y la red le dan cada vez más decisiones al modelo. Más decisiones al modelo significa más flexibilidad y menos previsibilidad, y eso se paga en depuración. Agentless, que vamos a mencionar en el bloque 7, es el extremo workflow: un pipeline fijo que en su momento le ganó a varios agentes autónomos en SWE-bench Lite. Tiempo objetivo: ~2 min.

### Presenter feedback

---

# 2. Por qué un solo agente no alcanza

**Goal of this section:** Mostrar los tres límites de un agente único (contexto finito, herramientas que se interfieren, un solo system prompt) y derivar de ellos las tres palancas de un sistema multiagente.

**Presenter feedback:**

---

## 1. El contexto es un recurso finito

### Content

**A medida que crece el contexto, el modelo recuerda peor lo que tiene adentro. Anthropic lo llama *context rot*.**

- **Presupuesto de atención.** El contexto es "a finite resource with diminishing marginal returns". Cada token que entra compite con los demás.
- **Degrada de a poco.** Es "a performance gradient rather than a hard cliff": el rendimiento baja a medida que entra contexto.
- **El objetivo.** Encontrar "the *smallest* *possible* set of high-signal tokens that maximize the likelihood of some desired outcome".
- **Un agente que trabaja mucho acumula.** Resultados de búsqueda, logs y archivos leídos quedan en su historia aunque no los vuelva a usar.

### Sources

- `anthropic-context-engineering.web.md` (Key claims): definición de context rot; "a finite resource with diminishing marginal returns"; "attention budget"; "a performance gradient rather than a hard cliff"; la frase del conjunto mínimo de tokens.
- `claude-code-subagents.web.md` (Key claims): un subagente sirve cuando una tarea lateral "would flood your main conversation with search results, logs, or file contents you won't reference again".

### Speaker notes

Conectar con la clase de transformers: la atención compara cada token con todos, y Anthropic atribuye parte de la degradación a eso y a que los modelos se entrenan sobre todo con secuencias más cortas. No hace falta volver a la matemática. El punto práctico es que un agente con un contexto lleno de basura razona peor, aunque la ventana todavía tenga lugar. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 2. Demasiadas herramientas se interfieren

### Content

**Cada herramienta que se agrega es una opción más para el modelo y una descripción más en su contexto. Pasado cierto punto, elige mal.**

- **El criterio de Anthropic.** "If a human engineer can't definitively say which tool should be used in a given situation, an AI agent can't be expected to do better." Los conjuntos de herramientas inflados están entre las fallas más comunes.
- **El criterio de LangChain.** Multiagente se justifica "when a single agent has too many tools and makes poor decisions about which to use".
- **Lo que hace Magentic-One.** El orquestador no elige entre docenas de acciones: elige qué agente llamar, y ese agente elige entre unas pocas propias.

### Sources

- `anthropic-context-engineering.web.md` (Key claims): la cita del ingeniero humano; "Bloated tool sets are one of the most common failure modes".
- `langgraph-multi-agent.web.md` (Key claims): la cita sobre demasiadas herramientas.
- `magentic-one-2024.web.md` (Key claims): "rather than deciding between dozens of possible actions, the Orchestrator needs only to decide which agent to call".

### Speaker notes

La versión de esta clase para Biomédica tenía una cifra de caída de precisión con la cantidad de herramientas; la sacamos porque no encontramos de dónde sale. El argumento se sostiene sin número: las herramientas que se parecen compiten, y sus descripciones ocupan contexto. En el trabajo práctico van a ver el efecto con el LLM débil, que es el primero en confundirse. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 3. Un solo system prompt no puede ser experto en todo

### Content

**Un agente tiene un único system prompt. Si tiene que ser experto en vuelos, hoteles y presupuestos a la vez, las instrucciones de un dominio diluyen las del otro.**

- **Especialistas rinden más.** El Agents SDK recomienda: "Have specialized agents that excel in one task, rather than having a general purpose agent that is expected to be good at anything."
- **El rol importa.** En ChatDev, sacar las descripciones de rol de los system prompts es lo que más baja la calidad: de 0,3953 a 0,2212.
- **Conocimiento extenso.** LangChain recomienda partir cuando una tarea pide "specialized knowledge with extensive context (long prompts and domain-specific tools)".

### Sources

- `openai-agents-sdk-multi-agent.web.md` (Raw excerpts, táctica 4): la recomendación citada textual.
- `chatdev-2023.web.md` (Evidence, Table 4): Quality 0,3953 con todo, 0,2212 sin roles.
- `langgraph-multi-agent.web.md` (Key claims): la cita sobre conocimiento especializado con contexto extenso.

### Speaker notes

El caso de ChatDev es útil porque es una ablación concreta: mismo sistema, mismo modelo, se quitan las descripciones de rol y la calidad cae casi a la mitad. Ojo con generalizar el número: es la métrica propia de ChatDev sobre su propio dataset. Lo que sí generaliza es la dirección. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 4. Las tres palancas: especialización, aislamiento de contexto, paralelismo

### Content

**Partir el trabajo entre agentes mueve tres palancas. Todo el resto de la clase es ver cuánto mueve cada arquitectura cada una.**

- **Especialización.** Cada agente tiene su system prompt, sus herramientas y, si conviene, su modelo.
- **Aislamiento de contexto.** Cada agente trabaja con su propia ventana y devuelve un resumen. Un subagente puede gastar decenas de miles de tokens y devolver 1.000 a 2.000.
- **Paralelismo.** Las subtareas independientes corren a la vez, y el sistema gasta más tokens en menos tiempo.

```ascii
            un agente                     varios agentes

   +----------------------------+     +--------+ +--------+ +--------+
   | prompt general             |     |prompt A| |prompt B| |prompt C|
   | todas las herramientas     |     |tools A | |tools B | |tools C |
   | todo el historial          |     |ctx A   | |ctx B   | |ctx C   |
   | una tarea por vez          |     +---+----+ +---+----+ +---+----+
   +----------------------------+         |  en paralelo |        |
                                          v          v          v
                                        resumen    resumen    resumen
```
<!-- ascii-note:
intent: contrastar un agente con todo en un contexto contra varios agentes con prompt, herramientas y contexto propios que corren en paralelo y devuelven resumenes
emphasize: las tres columnas separadas a la derecha; la etiqueta "en paralelo"
labels: "un agente", "varios agentes", "prompt general", "todas las herramientas", "todo el historial", "una tarea por vez", "prompt A/B/C", "tools A/B/C", "ctx A/B/C", "resumen"
-->

### Sources

- `anthropic-context-engineering.web.md` (Key claims, sub-agent architectures): cada subagente "might explore extensively, using tens of thousands of tokens or more, but returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens)".
- `langgraph-multi-agent.web.md` (Key claims): las tres capacidades que se buscan, context management, distributed development y parallelization.
- `mast-why-mas-fail-2025.web.md` (Key claims): un MAS habilita "task decomposition, performance parallelization, context isolation, specialized model ensembling".

### Speaker notes

Si se llevan una sola idea de la primera mitad, que sea esta. Las tres palancas son el vocabulario para comparar arquitecturas: un pipeline especializa pero no paraleliza, los handoffs especializan pero por defecto no aíslan, el orquestador mueve las tres. LangChain agrega una cuarta razón que no es técnica, el desarrollo distribuido: cada equipo mantiene su agente. En el trabajo práctico eso va a ser literal, cada integrante del grupo puede ser dueño de un agente. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 5. Qué es un sistema multiagente

### Content

**Un sistema multiagente son varios agentes que interactúan, de forma cooperativa, competitiva o ambas, para resolver un problema que excede a uno solo.**

- **Con LLM.** "A multi-agent system consists of multiple agents (LLMs autonomously using tools in a loop) working together."
- **Con orquestación.** MAST lo define como "a collection of agents designed to interact through orchestration".
- **No siempre hace falta.** "A single agent with the right (sometimes dynamic) tools and prompt can often achieve similar results." La carga de la prueba la tiene la arquitectura multiagente.

### Sources

- `aig4b-clase-6-agentes-biomedica.pdf.md` (lámina "Sistemas multiagente"): la definición en castellano.
- `anthropic-multi-agent-research-system.web.md` (Key claims): la definición con LLM.
- `mast-why-mas-fail-2025.web.md` (Key claims): la definición con orquestación.
- `langgraph-multi-agent.web.md` (Key claims): la advertencia sobre el agente único.

### Speaker notes

Tres definiciones que dicen lo mismo con distinto énfasis. La última viñeta es la postura de la clase: multiagente es una decisión que hay que justificar con números, y en el TP la van a justificar comparando contra un agente único. Tiempo objetivo: ~1 min.

### Presenter feedback

---

# 3. Arquitecturas base con un mismo ejemplo

**Goal of this section:** Repartir los mismos cuatro roles de un caso ficticio, Pampa Viajes, en siete arquitecturas, con un diagrama por arquitectura, lo que gana, lo que pierde y el caso real que se ve en los bloques 4 y 5. Cerrar con la tabla de costos de LangChain y una guía para elegir.

**Presenter feedback:**

---

## 1. El caso Pampa Viajes

### Content

**Pampa Viajes es una agencia ficticia. Un cliente escribe: "5 días en Bariloche para dos personas, con 1.500 dólares".**

- **Vuelos.** Busca vuelos de ida y vuelta para dos y devuelve opciones con precio.
- **Alojamiento.** Busca dónde dormir cinco noches para dos, en las fechas de los vuelos.
- **Actividades.** Arma un plan de excursiones y salidas para los cinco días.
- **Presupuesto.** Suma vuelos, alojamiento y actividades, compara con el tope de 1.500 dólares y aprueba o rechaza con el faltante o el sobrante. **No usa un LLM:** son reglas en código.

```ascii
   cliente: "5 dias en Bariloche, 2 personas, USD 1.500"
                          |
        +-----------+-----+------+-------------+
        |           |            |             |
        v           v            v             v
   +---------+ +-----------+ +-----------+ +-------------+
   | vuelos  | |alojamiento| |actividades| | presupuesto |
   |  (LLM)  | |   (LLM)   | |   (LLM)   | |  (reglas)   |
   +---------+ +-----------+ +-----------+ +-------------+
```
<!-- ascii-note:
intent: presentar los cuatro roles del caso y marcar que presupuesto es un agente sin LLM
emphasize: la caja "presupuesto (reglas)" con el acento; las otras tres iguales entre si
labels: "cliente", "5 dias en Bariloche, 2 personas, USD 1.500", "vuelos (LLM)", "alojamiento (LLM)", "actividades (LLM)", "presupuesto (reglas)"
-->

### Sources

- Ejemplo ficticio armado para la clase; sin fuente.

### Speaker notes

Este es el ejemplo que vamos a usar en las próximas siete láminas. Elegimos un dominio que todos entienden para que la atención quede en la arquitectura. Hay dependencias reales: el alojamiento depende de las fechas de los vuelos y el presupuesto depende de los tres. Y el presupuesto es a propósito un agente sin LLM: una suma y una comparación no se le piden a un modelo de lenguaje. En el TP, un agente así es optativo y suma puntos. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 2. Agente único con todas las herramientas

### Content

**La línea de base: un agente, un system prompt, cuatro herramientas y un solo historial.**

```ascii
   cliente
      |
      v
  +-------------------------------------------+
  |            agente de viajes               |
  |  prompt: experto en vuelos, hoteles,      |
  |          actividades y presupuesto        |
  |                                           |
  |  tools: buscar_vuelos  buscar_hoteles     |
  |         buscar_actividades                |
  |         calcular_presupuesto (codigo)     |
  |                                           |
  |  historial: todo lo que trajo cada tool   |
  +-------------------------------------------+
```
<!-- ascii-note:
intent: mostrar un unico agente con las cuatro herramientas y todo el historial en el mismo contexto
emphasize: la linea "historial: todo lo que trajo cada tool" como el punto debil
labels: "cliente", "agente de viajes", "prompt", "tools", "buscar_vuelos", "buscar_hoteles", "buscar_actividades", "calcular_presupuesto (codigo)", "historial"
-->

- **Ventajas.** Es lo más simple de construir y depurar. Todas las decisiones salen del mismo contexto, así que no se contradicen.
- **Desventajas.** El historial crece con cada búsqueda, el prompt mezcla cuatro especialidades y las búsquedas van una detrás de otra.
- **Caso real.** El agente lineal que defiende Cognition (lámina 5.4).

### Sources

- `cognition-dont-build-multi-agents.web.md` (Key claims): el default recomendado es "a single-threaded linear agent" con contexto continuo.
- `anthropic-context-engineering.web.md` (Key claims): context rot y herramientas infladas como fallas comunes.

### Speaker notes

Siempre conviene construir primero esta versión, porque es contra la que se compara todo lo demás. Noten que acá el presupuesto es una herramienta, no un agente: el mismo cálculo en código, pero llamado por el LLM. La ventaja que hay que retener es la coherencia: un solo contexto no puede contradecirse a sí mismo entre ramas. Esa ventaja es el centro del argumento de Cognition. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 3. Pipeline

### Content

**Los agentes se encadenan en un orden fijo que decide el código. La salida de uno es la entrada del siguiente.**

```ascii
 cliente
   |
   v
+--------+    +-------------+    +-------------+    +-------------+
| vuelos | -> | alojamiento | -> | actividades | -> | presupuesto |
| (LLM)  |    |    (LLM)    |    |    (LLM)    |    |  (reglas)   |
+--------+    +-------------+    +-------------+    +------+------+
                                                          |
                     ^          se pasa del tope          |
                     +------------------------------------+
                                                          |
                                                    ok    v
                                                      propuesta
```
<!-- ascii-note:
intent: mostrar la cadena fija vuelos -> alojamiento -> actividades -> presupuesto, con un unico retorno cuando el presupuesto rechaza
emphasize: el orden fijo de izquierda a derecha; la flecha de retorno "se pasa del tope"
labels: "cliente", "vuelos (LLM)", "alojamiento (LLM)", "actividades (LLM)", "presupuesto (reglas)", "se pasa del tope", "ok", "propuesta"
-->

- **Ventajas.** Predecible, barato y fácil de depurar: se sabe qué paso falló. Las salidas se acumulan a lo largo de la cadena y el presupuesto recibe los tres totales.
- **Desventajas.** Rígido. Si el presupuesto rechaza, el retorno hay que programarlo a mano, y un error temprano se arrastra hasta el final.
- **Caso real.** MetaGPT y ChatDev (láminas 4.1 y 4.2), y Agentless en reparación de código.

### Sources

- `anthropic-building-effective-agents.web.md` (Key claims): prompt chaining, secuencia de llamadas con "gates" programáticas.
- `openai-agents-sdk-multi-agent.web.md` (Key claims): "chaining agents (output of one is input of the next)".
- `metagpt-2023.web.md` (Key claims): "assembly-line paradigm"; MAST lo clasifica como "Assembly Line" (`mast-why-mas-fail-2025.web.md`, Table 3).
- `agentless-2024.web.md` (Key claims): pipeline fijo de localización, reparación y validación.

### Speaker notes

Es un workflow: el modelo no decide el orden. Para Pampa Viajes funciona bien mientras el primer intento entre en el presupuesto. Cuando no entra, hay que decidir a mano a qué paso volver; acá volvemos al alojamiento, que suele ser lo más caro, pero esa es una decisión del programador. Esa rigidez es el precio de la previsibilidad. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 4. Router
### Content

**Un paso de ruteo clasifica el pedido y lo manda a uno o varios especialistas. Después se combinan los resultados.**

```ascii
                    cliente
                       |
                       v
               +---------------+
               |    router     |  clasifica el pedido
               +-------+-------+
        "cambiar hotel"|  "viaje completo"
          +------------+-------------+
          |            |             |
          v            v             v
     +---------+ +-----------+ +-----------+
     | vuelos  | |alojamiento| |actividades|
     +---------+ +-----------+ +-----------+
          |            |             |
          +------------+------+------+
                              v
                        +-----------+
                        | sintesis  |
                        +-----+-----+
                              v
                       +-------------+
                       | presupuesto |  controla el total
                       |  (reglas)   |
                       +-------------+
```
<!-- ascii-note:
intent: mostrar un router que clasifica y despacha a uno o varios especialistas, una sintesis y el presupuesto como control final
emphasize: el router arriba; las dos etiquetas de clasificacion; el presupuesto al final como control
labels: "cliente", "router", "clasifica el pedido", "cambiar hotel", "viaje completo", "vuelos", "alojamiento", "actividades", "sintesis", "presupuesto (reglas)", "controla el total"
-->

- **Ventajas.** Barato: el pedido "solo quiero cambiar el hotel" va directo al agente de alojamiento. Vuelos y actividades pueden correr en paralelo.
- **Desventajas.** El ruteo se decide una vez, al principio. Si vuelos y alojamiento tienen que negociar fechas, el router no lo resuelve, y el presupuesto recién controla cuando todo está armado. Un error de clasificación arruina lo que sigue.
- **Caso real.** El patrón Router de la documentación de LangChain (lámina 3.9).

### Sources

- `anthropic-building-effective-agents.web.md` (Key claims): routing, "classify input and direct to specialized follow-up".
- `langgraph-multi-agent.web.md` (Definitions; Evidence): "A routing step classifies input and directs it to one or more specialized agents. Results are synthesized into a combined response."; el Router "uses an LLM for routing, then invokes agents in parallel".

### Speaker notes

El router es el workflow más barato con varios especialistas. El ruteo puede ser un LLM chico o un clasificador común. El presupuesto queda al final porque necesita los tres totales; no puede correr en paralelo con los demás. La debilidad aparece cuando los especialistas dependen entre sí: el router reparte y junta, pero no coordina en el medio. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 5. Orquestador y trabajadores

### Content

**Un agente orquestador planifica, llama a los especialistas como herramientas, revisa lo que devuelven y decide si hace falta otra vuelta.**

```ascii
                     cliente
                        ^ |
                        | v
              +---------------------+
              |    orquestador      |  planifica, decide, responde
              +--+------+------+--+-+
                 |      |      |  |
     en paralelo v      v      v  v   como herramientas
           +--------+ +------+ +------+ +-------------+
           | vuelos | |aloj. | |activ.| | presupuesto |
           +---+----+ +--+---+ +--+---+ |  (reglas)   |
               |         |        |     +------+------+
               +---------+--------+------------+
                  resumenes vuelven al orquestador
```
<!-- ascii-note:
intent: mostrar un orquestador central que llama en paralelo a los especialistas como herramientas y recibe sus resumenes
emphasize: que todo vuelve al orquestador; la etiqueta "en paralelo"
labels: "cliente", "orquestador", "planifica, decide, responde", "en paralelo", "como herramientas", "vuelos", "aloj.", "activ.", "presupuesto (reglas)", "resumenes vuelven al orquestador"
-->

- **Ventajas.** Mueve las tres palancas: cada trabajador tiene su contexto, los independientes corren en paralelo y el orquestador mantiene el control y una sola voz ante el cliente. Las subtareas no están fijas: el orquestador las decide según el pedido.
- **Desventajas.** Una llamada más por pedido, porque todo vuelve por el orquestador. Lo que el trabajador no resume se pierde en el camino, y si el orquestador planifica mal, todos trabajan mal.
- **Caso real.** El sistema de investigación de Anthropic y Magentic-One (láminas 5.2 y 4.4).

### Sources

- `anthropic-building-effective-agents.web.md` (Key claims): orchestrator-workers, "a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results"; "subtasks aren't pre-defined".
- `openai-agents-sdk-multi-agent.web.md` (Key claims): agents as tools, "a manager agent keeps control of the conversation and calls specialists via `Agent.as_tool()`".
- `langgraph-multi-agent.web.md` (Key claims): Subagents necesita 4 llamadas contra 3 "because results flow back through the main agent"; el sobrecosto "provides centralized control".
- `anthropic-multi-agent-research-system.web.md` (Key claims): "game of telephone" cuando todo pasa por el coordinador.

### Speaker notes

La usaron sin saberlo si en la misión anterior pusieron un agente como herramienta de otro con `as_tool`. Para Pampa Viajes, el orquestador puede lanzar vuelos y actividades en paralelo, esperar las fechas para alojamiento y recién al final pasar todo por el agente de presupuesto. Si el presupuesto rechaza, el orquestador decide qué recortar. El bloque 5 desarrolla la versión más ambiciosa de esta arquitectura. Tiempo objetivo: ~2,5 min.

### Presenter feedback

---

## 6. Handoffs y swarm
### Content

**Un agente le pasa la conversación entera a otro, que pasa a ser el agente activo y le habla al cliente.**

```ascii
 cliente <-----------------------------------------------+
   |                                                     |
   v       handoff          handoff          handoff     |
+--------+ -------> +--------+ -------> +-------+ -------> +-------+
| triage |          | vuelos |          | aloj. |          | activ.|
+--------+          +--------+          +-------+          +---+---+
                                                               |
       el historial viaja con cada handoff                     | handoff
                                                               v
                                                        +-------------+
                                                        | presupuesto |
                                                        +-------------+
```
<!-- ascii-note:
intent: mostrar la conversacion pasando de agente en agente (triage, vuelos, alojamiento, actividades, presupuesto), con el agente activo hablando directo con el cliente
emphasize: la cadena de handoffs; la leyenda "el historial viaja con cada handoff"
labels: "cliente", "triage", "vuelos", "aloj.", "activ.", "presupuesto", "handoff", "el historial viaja con cada handoff"
-->

- **Ventajas.** El especialista responde directo, sin intermediario. Si el cliente vuelve a escribir, sigue con el último agente activo, y eso ahorra llamadas en pedidos repetidos.
- **Desventajas.** Es secuencial, no paraleliza, y la conversación crece de handoff en handoff. El aislamiento de contexto no viene por defecto (lámina 7.2).
- **Caso real.** Los handoffs del OpenAI Agents SDK (lámina 4.7). Swarm, la versión educativa anterior de OpenAI, está deprecada y la reemplazó el SDK.

### Sources

- `openai-agents-sdk-handoffs.web.md` (Key claims): "Handoffs are represented as tools to the LLM" (`transfer_to_<agent_name>`); el agente que recibe toma la conversación.
- `langgraph-swarm.web.md` (Key claims): definición de swarm, "remembers which agent was last active".
- `openai-swarm.web.md` (Key claims): Swarm "is now replaced by the OpenAI Agents SDK".
- `langgraph-multi-agent.web.md` (Evidence): pedido repetido, Handoffs 5 llamadas contra 8 de Subagents.

### Speaker notes

Es la arquitectura de los call centers: "te paso con el área de reclamos". En Pampa Viajes funciona si el cliente quiere conversar con cada especialista; el de actividades puede quedar fuera de la cadena si el cliente no lo pide. El detalle de qué historial ve cada agente lo dejamos para la lámina 7.2. Swarm se nombra solo porque aparece en muchos tutoriales; OpenAI lo marcó como educativo y lo reemplazó por el SDK que ya usan. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 7. Red y pizarra compartida

### Content

**No hay jefe. Los agentes publican en un espacio común y cada uno toma lo que le interesa y actúa cuando tiene lo que necesita.**

```ascii
   +--------+                                  +-------------+
   | vuelos |---publica---+        +---lee-----| presupuesto |
   +--------+             |        |           |  (reglas)   |
                          v        |           +------+------+
                 +--------------------------+         |
                 |   pizarra del viaje      |<--alerta+
                 |  fechas, vuelos, hotel,  |  "faltan 120"
                 |  actividades, total      |
                 +--------------------------+
                          ^        |
   +-------------+        |        |           +-------------+
   | alojamiento |-publica+        +---lee---->| actividades |
   +-------------+                             +-------------+
```
<!-- ascii-note:
intent: mostrar agentes pares que publican y leen en una pizarra comun, con el agente de presupuesto publicando una alerta
emphasize: la pizarra central; la alerta del presupuesto
labels: "vuelos", "alojamiento", "actividades", "presupuesto (reglas)", "pizarra del viaje", "fechas, vuelos, hotel, actividades, total", "publica", "lee", "alerta"
-->

- **Ventajas.** Flexible y desacoplado: se agrega un agente sin tocar a los demás. Cada uno se suscribe solo a lo que necesita, y el agente de alojamiento arranca cuando aparecen las fechas.
- **Desventajas.** Menos predecible. Hay que definir quién termina, cómo se evitan los ciclos y quién resuelve dos escrituras contradictorias. Es la más difícil de depurar.
- **Caso real.** El pool de mensajes de MetaGPT y el pueblo de Generative Agents (láminas 4.1 y 4.6).

### Sources

- `metagpt-2023.web.md` (Key claims): "Publish-subscribe via a shared message pool"; la suscripción por rol evita "information overload"; "an agent activates its action only after receiving all its prerequisite dependencies".
- `aig4b-clase-6-agentes-biomedica.pdf.md` (lámina de arquitecturas): Network, todos se comunican con todos, "más flexible, menos predecible".
- `generative-agents-2023.web.md` (Key claims): 25 agentes en un mundo compartido que se coordinan conversando.

### Speaker notes

El "faltan 120" del diagrama es solo una etiqueta de ejemplo de lo que el agente de presupuesto publicaría; no es un dato. En la versión pura de red cada agente puede hablar con cualquiera; la pizarra ordena eso con un lugar único de verdad. MetaGPT es el ejemplo más limpio: los agentes no conversan, publican documentos con formato fijo y se suscriben por rol. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 8. Jerárquica

### Content

**Un supervisor coordina supervisores, y cada uno coordina su propio equipo. Es el orquestador repetido en niveles.**

```ascii
                       +------------+
                       |  director  |
                       +-----+------+
             +---------------+----------------+
             |                                |
             v                                v
   +-------------------+            +-------------------+
   | sup. logistica    |            | sup. experiencia  |
   +----+---------+----+            +---------+---------+
        |         |                           |
        v         v                           v
   +--------+ +-------------+          +-------------+
   | vuelos | | alojamiento |          | actividades |
   +--------+ +-------------+          +-------------+

          presupuesto (reglas) valida cada propuesta del director
```
<!-- ascii-note:
intent: mostrar dos niveles de supervision sobre los especialistas, con el presupuesto como validador del director
emphasize: los dos niveles; la nota del presupuesto validando
labels: "director", "sup. logistica", "sup. experiencia", "vuelos", "alojamiento", "actividades", "presupuesto (reglas) valida cada propuesta del director"
-->

- **Ventajas.** Escala: cada supervisor maneja un equipo chico y el director solo ve dos resúmenes. Los equipos se desarrollan por separado.
- **Desventajas.** Cada nivel agrega llamadas, latencia y otro resumen donde se pierde información. Para cuatro roles es exagerada.
- **Caso real.** ChatDev, que MAST clasifica como flujo jerárquico (lámina 4.2), y los subagentes anidados de Claude Code (lámina 5.6). Contract Net ya la permitía en 1980 (lámina 6.1).

### Sources

- `aig4b-clase-6-agentes-biomedica.pdf.md` (lámina de arquitecturas): Hierarchical, supervisor de supervisores.
- `mast-why-mas-fail-2025.web.md` (Key claims, Table 3): ChatDev e HyperAgent como "Hierarchical Workflow".
- `claude-code-subagents.web.md` (Key claims): un subagente puede lanzar subagentes "up to three layers below the main conversation".
- `contract-net-protocol.web.md` (Key claims): "a manager assigns tasks to contractors, who in turn decompose into lower-level task and assign them to the lower level".

### Speaker notes

Para Pampa Viajes la jerarquía sobra, y conviene decirlo: la mostramos para completar el mapa. Se justifica cuando hay decenas de agentes, o cuando cada sub-equipo es un producto de otra gente. El costo es el teléfono descompuesto: cada nivel resume lo que le dicen y algo se pierde. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 9. Las mismas tareas medidas: llamadas, tokens y control
<!-- template: value-columns -->

### Content

**LangChain cuenta llamadas al modelo y tokens de cuatro patrones sobre los mismos escenarios. Ningún patrón gana en todos.**

| Patrón | Un pedido | Pedido repetido | Tres dominios |
|---|---|---|---|
| **Subagentes** (orquestador) | 4 llamadas | 8 llamadas | 5 llamadas, ~9K tokens |
| **Handoffs** | 3 llamadas | 5 llamadas | 7+ llamadas, ~14K+ tokens |
| **Skills** (un agente carga contexto) | 3 llamadas | 5 llamadas | 3 llamadas, ~15K tokens |
| **Router** | 3 llamadas | 6 llamadas | 5 llamadas, ~9K tokens |

- **Skills.** Un solo agente que carga prompts y conocimiento especializados cuando los necesita, sin delegar en otros agentes.
- **Pedido único.** Subagentes paga una llamada extra porque la respuesta vuelve por el agente principal.
- **Pedido repetido.** Los patrones con estado (handoffs, skills) no repiten el ruteo.
- **Varios dominios en paralelo.** Subagentes y router ganan: cada especialista ve solo su contexto. Skills hace pocas llamadas pero arrastra los 6K tokens de documentación en cada una.

### Sources

- `langgraph-multi-agent.web.md` (Definitions): Skills, "Specialized prompts and knowledge loaded on-demand. A single agent stays in control"; (Evidence, tabla Summary): todos los números de la tabla; escenarios "Buy coffee", "Buy coffee again" y "Compare Python, JavaScript, and Rust for web development" con ~2.000 tokens de documentación por lenguaje. Son escenarios ilustrativos de la documentación, no un benchmark medido.

### Speaker notes

Aclarar que son cuentas de un ejemplo armado por LangChain, no mediciones. Sirven porque muestran la forma del trade-off. La página dice que Subagents procesa "67% fewer tokens"; con sus propios números es al revés, Skills usa cerca de 67 % más, o Subagents usa cerca de 40 % menos. Por eso en la lámina no ponemos ese porcentaje. Este tipo de tabla es lo que les vamos a pedir en el TP, pero con sus mediciones reales. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 10. Cómo elegir

### Content

**Elegir arquitectura es responder cuatro preguntas sobre la tarea, en este orden.**

1. **¿Un agente con buenas herramientas alcanza?** Si alcanza, no hay sistema multiagente que construir.
2. **¿El orden de los pasos se conoce de antemano?** Pipeline o router.
3. **¿Las subtareas son independientes y leen más de lo que escriben?** Orquestador con trabajadores en paralelo.
4. **¿El especialista tiene que hablar con el usuario o hay pedidos repetidos?** Handoffs, con filtro de historial si hace falta aislar.

- **Red y jerárquica** quedan para cuando hay muchos agentes o equipos que los desarrollan por separado.

### Sources

- `anthropic-building-effective-agents.web.md` (Key claims): empezar por lo más simple; "optimizing single LLM calls with retrieval and in-context examples is usually enough".
- `langgraph-multi-agent.web.md` (Evidence, tabla "Optimize for"): Handoffs y Skills para pedidos repetidos, Subagents y Router para ejecución en paralelo y dominios con contexto grande.
- `anthropic-multi-agent-research-system.web.md` (Key claims): multiagente rinde con "heavy parallelization, information that exceeds single context windows, and interfacing with numerous complex tools", y no en dominios que comparten contexto o tienen muchas dependencias.
- `openai-agents-sdk-multi-agent.web.md` (Key claims): handoffs "when routing itself is part of the workflow".

### Speaker notes

La guía es nuestra, armada con lo que dicen las cuatro fuentes. La pregunta 3 vuelve en el bloque 5. Anthropic reporta que la investigación en paralelo rinde y que el código con dependencias encaja peor; Cognition recomienda no paralelizar. Los dos coinciden en que delegar trabajo de solo lectura mantiene limpio el contexto principal. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

# 4. Implementaciones reales

**Goal of this section:** Mostrar sistemas publicados que implementan las arquitecturas del bloque 3, cada uno con su arquitectura, una idea propia y un resultado citado del paper.

**Presenter feedback:**

---

## 1. MetaGPT: una empresa de software en línea de montaje

### Content

**MetaGPT simula una empresa de software con cinco roles que se pasan documentos con formato fijo, siguiendo los procedimientos de un equipo humano.**

![MetaGPT: pool de mensajes compartido y ciclo de ejecución del Engineer](research/corpus/metagpt-2023.web/images/2-message_sharing.jpg)

- **Arquitectura.** Pipeline: Product Manager → Architect → Project Manager → Engineer → QA Engineer.
- **Idea propia.** Los agentes no conversan: publican documentos estructurados en un pool compartido y cada rol se suscribe a lo que necesita.
- **Resultado.** Pass@1 de 85,9 % en HumanEval y 87,7 % en MBPP. En su ablación, agregar roles alrededor del Engineer sube la ejecutabilidad de 1,0 a 4,0 sobre 4.

### Sources

- `metagpt-2023.web.md` (Key claims): los cinco roles, "structured communication interfaces", publish-subscribe; resultados de HumanEval y MBPP; (Evidence, Table 3) ejecutabilidad 1,0 con solo Engineer y 4,0 con los cuatro roles agregados.
- Imagen: `metagpt-2023.web/images/2-message_sharing.jpg` (Figura 2 del paper).

### Speaker notes

MetaGPT combina dos arquitecturas del bloque 3: el flujo es un pipeline, la comunicación es una pizarra con suscripción. La motivación de los documentos con formato es evitar el teléfono descompuesto del lenguaje libre, y el paper lo ilustra con un diálogo de relleno entre dos agentes que se preguntan si almorzaron. Ojo con los números: compara contra baselines reportados en otros papers, no corridos por ellos. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 2. ChatDev: fases y diálogos de a dos

### Content

**ChatDev arma una empresa con CEO, CTO, programador, revisor y tester, y resuelve cada subtarea con un diálogo entre dos agentes.**

![ChatDev: cadena de chat por fases](research/corpus/chatdev-2023.web/images/chat_chain.png)

- **Arquitectura.** Fases en cadena (diseño, código, pruebas); cada subtarea es un par instructor y asistente que conversa hasta acordar.
- **Idea propia.** Entre fases pasa solo la solución, no la conversación entera. Es aislamiento de contexto explícito.
- **Resultado.** Quality 0,3953 contra 0,1523 de MetaGPT y 0,1419 de GPT-Engineer, en su propio dataset.

### Sources

- `chatdev-2023.web.md` (Key claims): roles, chat chain, diálogo instructor-asistente; "By sharing only the solutions of each subtask rather than the entire communication history"; (Evidence, Table 1) valores de Quality.
- `mast-why-mas-fail-2025.web.md` (Table 3): ChatDev clasificado como "Hierarchical Workflow".
- Imagen: `chatdev-2023.web/images/chat_chain.png` (Figura 2 del paper).

### Speaker notes

Juntar esta lámina con la anterior: MetaGPT dice que le gana a ChatDev y ChatDev dice que le gana a MetaGPT. Cada paper evalúa en su propio dataset con sus propias métricas, y ninguno ofrece un benchmark independiente. Es una buena lección para el TP: comparar arquitecturas exige un benchmark común, y por eso se lo vamos a dar. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 3. AutoGen: agentes que conversan

### Content

**AutoGen modela todo como agentes que se mandan mensajes. Un agente puede tener atrás un LLM, una persona, código o una combinación.**

![AutoGen: chat grupal con un manager que elige quién habla](research/corpus/autogen-2023.web/images/app_groupchat.png)

- **Arquitectura.** Conversaciones de a dos, anidadas o en grupo, donde un manager elige al siguiente que habla y difunde la respuesta.
- **Idea propia.** Agregar un agente especializado arregla fallas de un lazo. En ALFWorld, un agente que inyecta reglas de sentido común sube el éxito de 54 % a 69 %. En ajedrez, un agente tablero valida cada jugada con reglas programadas.
- **Resultado.** Separar escritor y verificador de seguridad en dos agentes sube el F1 de detección de código inseguro un 8 % con GPT-4 y un 35 % con GPT-3.5-turbo.

### Sources

- `autogen-2023.web.md` (Key claims): agentes conversables, dynamic group chat; Safeguard separado, F1 +8 % (GPT-4) y +35 % (GPT-3.5-turbo); (Evidence, Table 3) ALFWorld ReAct 54, ALFChat 2 agentes 54, 3 agentes 69; agente tablero en A6.
- Imagen: `autogen-2023.web/images/app_groupchat.png` (Figura 12 del paper).

### Speaker notes

El dato que conecta con el TP es el del verificador con GPT-3.5: la ganancia de separar roles es mucho mayor con el modelo más débil, que es la apuesta del trabajo práctico. El agente tablero del ajedrez combina un LLM con código: conversa en lenguaje natural y valida las jugadas con reglas programadas. Lo retomamos en la lámina 6.2. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 4. Magentic-One: un orquestador con dos ledgers

### Content

**Magentic-One es un sistema generalista de Microsoft: un orquestador planifica y dirige a cuatro especialistas, uno de ellos sin LLM.**

![Magentic-One: lazo externo con el task ledger y lazo interno con el progress ledger](research/corpus/magentic-one-2024.web/images/orchestrator.png)

- **Arquitectura.** Orquestador y trabajadores: WebSurfer (navegador), FileSurfer (lector de archivos), Coder y ComputerTerminal, que ejecuta código y comandos sin LLM.
- **Idea propia.** Dos registros. El task ledger guarda hechos y plan; el progress ledger contesta en cada paso si se avanza, si se está en un ciclo y quién habla. Con un contador de estancamiento, el orquestador replanifica.
- **Resultado.** 38 % en GAIA (con GPT-4o y o1) y 32,8 % en WebArena (con GPT-4o). Cada tarea cuesta "perhaps several US dollars, and tens of minutes".

### Sources

- `magentic-one-2024.web.md` (Key claims): los cuatro agentes y ComputerTerminal "no LLM"; task ledger, progress ledger, stall counter; costo y latencia; (Inconsistencies) 38 % y 32,8 % vienen de configuraciones distintas.
- Imagen: `magentic-one-2024.web/images/orchestrator.png` (Figura 2 del paper).

### Speaker notes

Es el orquestador del bloque 3 con la bitácora explícita. El progress ledger es una idea que pueden copiar en el TP: un agente que en cada paso responde cinco preguntas fijas sobre el avance. Los autores reportan además que reemplazar el orquestador por un chat grupal simple baja el rendimiento, pero ese número sale de una figura que no capturamos, así que no lo citamos. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 5. Debate y Mixture-of-Agents

### Content

**Dos formas de poner varios LLM sobre la misma pregunta: que discutan, o que propongan en capas y uno sintetice.**

- **Debate.** Varias instancias del mismo modelo responden, leen las respuestas de las otras y corrigen la suya durante varias rondas. Con 3 agentes y 2 rondas, aritmética pasa de 67,0 % a 81,8 % y GSM8K de 77,0 % a 85,0 %.
- **Mixture-of-Agents.** Capas de modelos proponentes; cada capa lee todas las respuestas de la anterior y un agregador escribe la final. Con solo modelos abiertos llega a 65,1 % de win rate controlado por largo (LC) en AlpacaEval 2.0, contra 57,5 % de GPT-4o.
- **El costo.** Más llamadas y más latencia: MoA no puede empezar a responder hasta que terminan todas las capas.

### Sources

- `multiagent-debate-2023.web.md` (Key claims; Evidence, Table 1): el procedimiento y los valores de Single Agent contra Multi-Agent (Debate).
- `mixture-of-agents-2024.web.md` (Key claims): arquitectura en capas, proponentes y agregador, 65,1 % contra 57,5 % de GPT-4 Omni; latencia del primer token como limitación.

### Speaker notes

Son arquitecturas de red y de capas, pero con agentes sin herramientas: todos responden la misma pregunta. El debate muestra algo interesante, hay casos donde todos arrancan mal y llegan bien. También el contrario: debates que convergen con confianza a una respuesta incorrecta. MoA cita un trabajo que encontró que un solo agente con un prompt fuerte y demostraciones alcanza calidad comparable. Los números son de muestras chicas, cien problemas por tarea en el debate. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 6. Generative Agents: un pueblo de 25 agentes

### Content

**Veinticinco agentes viven en un pueblo simulado, Smallville. Cada uno tiene memoria, reflexiona y planifica su día, y se coordinan conversando.**

![Difusión de la invitación a la fiesta entre los agentes de Smallville](research/corpus/generative-agents-2023.web/images/figure_info_diff2.png)

- **Arquitectura.** Red sobre un mundo compartido: cada agente percibe una parte del pueblo y habla con quien se cruza.
- **Idea propia.** Un flujo de memoria por agente con recuperación por recencia, importancia y relevancia, más reflexión periódica.
- **Resultado.** A partir de una agente que quiere hacer una fiesta, la noticia pasa de 1 agente (4 %) a 13 (52 %) en dos días simulados, y 5 de los 12 invitados se presentan.

### Sources

- `generative-agents-2023.web.md` (Key claims): 25 agentes, memory stream con recency, importance, relevance; reflection; planning; (Evidence) difusión de la fiesta 1 (4 %) a 13 (52 %), 5 de 12 asistentes; costo de "thousands of dollars in token credits".
- Imagen: `generative-agents-2023.web/images/figure_info_diff2.png` (Figura 9 del paper).

### Speaker notes

Es el único caso de la sección que no resuelve una tarea: simula comportamiento. Lo mostramos porque es la red pura, sin orquestador, y la coordinación aparece sin que nadie la programe. Alcanza con la imagen y el número de difusión. También muestra el costo: dos días simulados con 25 agentes costaron miles de dólares en tokens. Tiempo objetivo: ~1 min.

### Presenter feedback

---

## 7. OpenAI Agents SDK: el del trabajo práctico

### Content

**El SDK que usaron en la misión de RAG y MCP trae dos patrones multiagente, y se pueden combinar.**

| | Agentes como herramientas | Handoffs |
|---|---|---|
| **Cómo** | un manager llama a especialistas con `Agent.as_tool()` | el triage transfiere con `transfer_to_<agente>` |
| **Quién responde** | el manager | el especialista, que queda activo |
| **Contexto** | el especialista recibe solo lo que el manager le pasa | por defecto, todo el historial (lámina 7.2) |
| **Arquitectura del bloque 3** | orquestador y trabajadores | handoffs |

- **Orquestación por código.** El mismo SDK permite encadenar agentes, iterar con un evaluador o lanzarlos en paralelo con `asyncio.gather`.

### Sources

- `openai-agents-sdk-multi-agent.web.md` (Key claims): agents as tools con `Agent.as_tool()`, handoffs, combinación de ambos; orquestación por código con encadenamiento, evaluador y `asyncio.gather`.
- `openai-agents-sdk-handoffs.web.md` (Key claims): `transfer_to_<agent_name>`; el agente nuevo "gets to see the entire previous conversation history".

### Speaker notes

Con lo que saben del SDK pueden construir cuatro de las siete arquitecturas: pipeline y router por código, orquestador con `as_tool`, handoffs con `handoffs=[...]`. La celda de contexto de agentes como herramientas es una inferencia del patrón, el especialista corre con la entrada que le arma el manager; verifiquen el comportamiento con sus propios logs. Tiempo objetivo: ~2 min.

### Presenter feedback

---

# 5. El agente principal que delega bajo demanda

**Goal of this section:** Presentar la arquitectura más robusta y flexible de la clase: un agente principal con un modelo pesado y caro que en principio hace todo él, y que crea, despierta o le escribe a subagentes u otros agentes cuando le conviene, aprovechando el paralelismo. Sostenerla con el sistema de investigación de Anthropic, contrastarla con Cognition, mostrar dónde coinciden y verla funcionar en Claude Code con una demo en vivo.

**Presenter feedback:**

---

## 1. Un agente principal caro que despierta subagentes

### Content

**El agente principal tiene el modelo más capaz y caro y resuelve él mismo todo lo que puede. Cuando una parte del trabajo ensuciaría su contexto o se puede hacer en paralelo, lanza un subagente, despierta a uno que ya existe o le escribe a otra sesión.**

```ascii
                         usuario
                            |
                            v
        +---------------------------------------+
        |  agente principal  (modelo caro)      |
        |  planifica, decide, escribe, responde |
        +---+-----------+-----------+-------+---+
            |           |           |       |
     crea   |    crea   |  despierta|       | mensaje
            v           v           v       v
       +---------+ +---------+ +---------+ +-----------+
       |subagente| |subagente| |subagente| | otra      |
       | barato  | | barato  | | (pausa) | | sesion    |
       +----+----+ +----+----+ +----+----+ +-----+-----+
            |   en paralelo         |            |
            +-----------+-----------+------------+
                        v
               solo resumenes vuelven
```
<!-- ascii-note:
intent: mostrar un agente principal con modelo caro que crea, despierta o le escribe a otros agentes bajo demanda, y recibe solo resumenes
emphasize: el agente principal (modelo caro) como unico que responde; los tres verbos crea, despierta, mensaje
labels: "usuario", "agente principal (modelo caro)", "planifica, decide, escribe, responde", "crea", "despierta", "mensaje", "subagente barato", "subagente (pausa)", "otra sesion", "en paralelo", "solo resumenes vuelven"
-->

- **Bajo demanda.** No hay un equipo fijo: los agentes existen cuando el principal los necesita.
- **Modelo por rol.** El principal usa el modelo caro; los subagentes pueden usar uno más barato.
- **El principal decide y escribe.** Los subagentes exploran, buscan y verifican, y devuelven un resumen.

### Sources

- `anthropic-multi-agent-research-system.web.md` (Key claims): el lead agent con Claude Opus 4 y subagentes con Claude Sonnet 4; subagentes "operate in parallel" con sus propias ventanas.
- `anthropic-context-engineering.web.md` (Key claims): "The main agent coordinates with a high-level plan while subagents perform deep technical work"; resúmenes de 1.000 a 2.000 tokens.
- `claude-code-subagents.web.md` (Key claims): subagentes con modelo propio para "control costs (route to cheaper models like Haiku)"; un subagente terminado se retoma con `SendMessage`.
- `claude-code-cross-session-messaging.web.md` (Key claims): mensajes entre sesiones; una sesión inactiva arranca un turno nuevo cuando le llega un mensaje.
- `magentic-one-2024.web.md` (Key claims, limitaciones): equipo fijo, "When agents are not needed, they simply serve as a distraction to the Orchestrator" (notas).

### Speaker notes

La arquitectura que más robusta y flexible nos parece hoy tiene un bloque propio. Es el orquestador del bloque 3 con dos diferencias. La primera: el principal es un agente completo, resuelve solo lo que puede y delega cuando le conviene. La segunda: los otros agentes no están fijos, se crean o se despiertan cuando hacen falta. Esa combinación evita los dos extremos: el agente único que se ahoga en su contexto y el equipo fijo de Magentic-One, donde los agentes que sobran distraen al orquestador. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 2. El sistema de investigación de Anthropic

### Content

**La función Research de Claude usa un agente líder que planifica, guarda el plan en memoria y lanza subagentes de búsqueda en paralelo. Un agente aparte agrega las citas al final.**

![Arquitectura del sistema de investigación multiagente de Anthropic](research/corpus/anthropic-multi-agent-research-system.web/images/image.png)

- **Resultado.** Con Claude Opus 4 como líder y subagentes Claude Sonnet 4, supera en **90,2 %** a Claude Opus 4 solo en la evaluación interna de investigación de Anthropic.
- **Por qué funciona.** "The essence of search is compression": cada subagente explora con su contexto y le entrega al líder lo importante.
- **Esfuerzo escalado en el prompt.** Un agente con 3 a 10 llamadas para un dato puntual; 2 a 4 subagentes con 10 a 15 llamadas cada uno para comparar; más de 10 subagentes para investigación compleja.

### Sources

- `anthropic-multi-agent-research-system.web.md` (Key claims): arquitectura LeadResearcher, Memory, subagentes y CitationAgent; el plan va a memoria porque el contexto se trunca pasados 200.000 tokens; +90,2 % "on our internal research eval"; "The essence of search is compression"; reglas de escalado del esfuerzo. (Inconsistencies) el 90,2 % es una mejora relativa sobre una evaluación interna no publicada.
- Imagen: `anthropic-multi-agent-research-system.web/images/image.png`.

### Speaker notes

Hay que decir el 90,2 % con su aclaración: es una evaluación interna de Anthropic, no publicada, y el número es una mejora relativa, sin valores absolutos. El ejemplo que dan es encontrar a todos los miembros de directorio de las empresas de tecnología del S&P 500: el agente solo fallaba con búsquedas secuenciales lentas y el sistema lo resolvió repartiendo empresas entre subagentes. Las reglas de esfuerzo son interesantes para el TP: las tuvieron que escribir en el prompt porque al principio el líder lanzaba 50 subagentes para preguntas simples. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 3. Lo que cuesta

### Content

**Un sistema multiagente rinde porque gasta más tokens, y eso hay que pagarlo.**

- **Los tokens explican el rendimiento.** En BrowseComp, tres factores explican el 95 % de la varianza; el uso de tokens solo explica el 80 %. Los otros dos son la cantidad de llamadas a herramientas y el modelo.
- **El multiplicador.** Un agente usa cerca de 4 veces los tokens de un chat; un sistema multiagente, cerca de 15 veces.
- **Las primeras fallas.** Lanzar 50 subagentes para consultas simples, buscar sin fin fuentes que no existen y distraerse entre ellos con actualizaciones.
- **El cuello de botella.** Con ejecución sincrónica, el líder espera a cada tanda de subagentes y no los puede corregir mientras trabajan.

### Sources

- `anthropic-multi-agent-research-system.web.md` (Key claims): "Multi-agent systems work mainly because they help spend enough tokens to solve the problem"; 95 % y 80 % de la varianza en BrowseComp; ~4× y ~15× respecto de un chat; las tres fallas tempranas citadas; "synchronous execution creates bottlenecks".

### Speaker notes

La anterior mostraba la ganancia; acá va el costo. Anthropic dice sin vueltas que el sistema funciona porque gasta más. Para el TP es la advertencia central: con un LLM barato pueden permitirse gastar más tokens, pero tienen que medirlos, porque una arquitectura que gana gastando quince veces más puede no ser mejor. Por eso les vamos a pedir el reporte de tokens por arquitectura. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 4. El contrapunto: Cognition

### Content

**Cognition, la empresa de Devin, publicó "Don't Build Multi-Agents" el mismo mes que Anthropic publicó su sistema.**

- **Principio 1.** "Share context, and share full agent traces, not just individual messages."
- **Principio 2.** "Actions carry implicit decisions, and conflicting decisions carry bad results."
- **El ejemplo.** Para clonar Flappy Bird, un subagente hace un fondo estilo Super Mario y otro un pájaro que no combina. Ninguno vio lo que hacía el otro.
- **Lo que recomiendan.** Un agente lineal de un solo hilo, con contexto continuo, y un modelo que comprima la historia cuando la tarea es muy larga.

![La arquitectura que Cognition descarta: subagentes en paralelo que no se ven](research/corpus/cognition-dont-build-multi-agents.web/images/721e44474051c62156e15b5ffb1a249c996f0607-1404x1228.png)

![La que recomienda: un agente lineal con contexto continuo](research/corpus/cognition-dont-build-multi-agents.web/images/06f64ae3557594588f702b2608d43564edc98c3d-1404x1230.png)

### Sources

- `cognition-dont-build-multi-agents.web.md` (Key claims): los dos principios citados; ejemplo de Flappy Bird; "single-threaded linear agent"; modelo de compresión de historia; fecha 12 de junio de 2025.
- `anthropic-multi-agent-research-system.web.md` (Provenance): publicado el 13 de junio de 2025.
- Imágenes: `cognition-dont-build-multi-agents.web/images/721e44474051c62156e15b5ffb1a249c996f0607-1404x1228.png` ("Almost Surely Unreliable") y `06f64ae3557594588f702b2608d43564edc98c3d-1404x1230.png` ("Simple & Reliable").

### Speaker notes

Las dos publicaciones salieron con un día de diferencia y parecen opuestas. El argumento de Cognition es sobre decisiones implícitas: cada acción de un agente toma decisiones que no escribe en ningún lado, como el estilo visual, y otro agente que no las vio toma las contrarias. El post describía además los subagentes de Claude Code de junio de 2025 como secuenciales y sin escribir código; la documentación actual ya no dice eso, así que hay que tomarlo como foto de esa fecha. El argumento es por ejemplos, sin una evaluación cuantitativa. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 5. Dónde coinciden
### Content

**Leídos juntos, Anthropic y Cognition coinciden en una cosa: delegar trabajo de solo lectura mantiene limpio el contexto principal.**

| | Conviene delegar | Conviene un solo hilo |
|---|---|---|
| **Tipo de trabajo** | buscar, leer, investigar, verificar | escribir código con dependencias, diseñar algo coherente |
| **Lo que comparten las partes** | poco: cada una devuelve hallazgos | decisiones implícitas que las demás necesitan ver |
| **Anthropic** | subagentes de investigación en paralelo | "most coding tasks involve fewer truly parallelizable tasks than research" |
| **Cognition** | un subagente que contesta una pregunta, sin paralelo (Claude Code, jun. 2025) | el agente lineal con contexto continuo |

- **Donde difieren.** En el paralelismo: Anthropic lo usa para investigar; Cognition advierte que varios subagentes en paralelo "might give conflicting responses".
- **Para la arquitectura del bloque.** El principal se queda con las decisiones y la escritura; los subagentes hacen el trabajo de lectura y devuelven resúmenes.

### Sources

- `anthropic-multi-agent-research-system.web.md` (Key claims): no conviene en "domains that require all agents to share the same context or involve many dependencies between agents"; la cita sobre tareas de código.
- `cognition-dont-build-multi-agents.web.md` (Key claims; Raw excerpts): los subagentes de Claude Code de junio de 2025 "never [do] work in parallel with the subtask agent" y solo contestan preguntas, lo que mantiene la investigación fuera de la historia del agente principal; "if they were to run multiple parallel subagents, they might give conflicting responses".

### Speaker notes

Síntesis del bloque. Los dos dicen que lo que rompe un sistema multiagente es que dos agentes tomen decisiones que dependen entre sí sin verse. El acuerdo está en delegar lectura: un subagente que investiga y devuelve un resumen no ensucia el contexto del que decide. El desacuerdo está en el paralelismo: Anthropic lo aprovecha para investigar, Cognition prefiere no correr riesgos. La arquitectura del agente principal toma de los dos: concentra las decisiones en un solo contexto, delega lo que es de solo lectura y paraleliza solo cuando las ramas no comparten decisiones. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 6. Claude Code: subagentes, equipos y mensajes entre sesiones

### Content

**Claude Code implementa la arquitectura del agente principal con tres mecanismos, de más liviano a más pesado.**

![Subagentes contra equipos de agentes en Claude Code](research/corpus/claude-code-agent-teams.web/images/subagents-vs-agent-teams-light.png)

- **Subagentes.** Corren dentro de una sesión, cada uno con su ventana, su prompt, sus herramientas y su modelo, y devuelven solo el resumen. Pueden anidarse hasta tres niveles y correr hasta 20 a la vez. Un subagente terminado se retoma con `SendMessage`.
- **Mensajes entre sesiones.** Una sesión le escribe texto a otra sesión del mismo usuario; si la receptora está inactiva, arranca un turno con el mensaje. **Activo por defecto** desde la versión 2.1.224 (2.1.234 en Windows nativo).
- **Equipos de agentes.** Un líder y compañeros que son sesiones completas, con lista de tareas compartida y mensajes directos entre ellos. **Experimental y desactivado por defecto.**

### Sources

- `claude-code-subagents.web.md` (Key claims): contexto aislado por subagente; anidamiento "up to three layers below the main conversation"; límite de 20 subagentes concurrentes; retomar con `SendMessage`. (Inconsistencies) los valores dependen de la versión; documentación capturada el 2026-10-04.
- `claude-code-cross-session-messaging.web.md` (Key claims): "When a session meets the requirements, messaging is on with nothing to enable"; requiere v2.1.224 en macOS y Linux; la sesión inactiva arranca un turno nuevo con el mensaje.
- `claude-code-agent-teams.web.md` (Key claims): "experimental and disabled by default", `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`; líder, compañeros, lista de tareas y buzón; "use significantly more tokens than a single session".
- Imagen: `claude-code-agent-teams.web/images/subagents-vs-agent-teams-light.png`.

### Speaker notes

Los tres mecanismos son los tres verbos del diagrama de 5.1: crear (subagentes), despertar y escribir (mensajes entre sesiones, `SendMessage` a un subagente terminado). Detalles que conviene saber. Los compañeros de un equipo usan por defecto el modelo del líder; para que sean más baratos hay que pedirlo en el prompt o en la definición. No hay equipos anidados: un compañero no puede crear compañeros. La documentación recomienda empezar con tres a cinco compañeros. Todos estos números son de la documentación del 4 de octubre de 2026 y cambian seguido. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 7. Demo en vivo
<!-- template: process -->

### Content

**Demo: un sistema en tres repositorios, un agente especializado por repositorio y los tres coordinándose por mensajes.**

1. **Inspeccionar.** Una sesión en la raíz lanza tres subagentes nuevos en paralelo, uno por carpeta: `design/`, `code/` y `outreach/`. Vuelven tres resúmenes.
2. **Especializar.** Con esos resúmenes, la sesión principal escribe un `CLAUDE.md` en cada carpeta.
3. **Nombrar.** Una sesión nueva por carpeta. Lo primero en cada una es `/rename`: DESIGN-AGENT, CODE-AGENT y OUTREACH-AGENT.
4. **Coordinar.** CODE-AGENT les manda un solo mensaje a los otros dos para sacar una promoción: la pieza gráfica, el cambio en la web y el mail.

### Sources

- `claude-code-subagents.web.md` (Key claims): Explore es de solo lectura y no carga CLAUDE.md; general-purpose explora y modifica; cada subagente "starts with a fresh, isolated context window"; un fork "inherits the entire conversation so far" y pierde el aislamiento; fork mode activo por defecto en sesiones interactivas desde v2.1.232, y con fork mode los subagentes corren en segundo plano. (Evidence): el prompt "Research the authentication, database, and API modules in parallel using separate subagents"; transcripts en `~/.claude/projects/{project}/{sessionId}/subagents/`.
- `anthropic-context-engineering.web.md` (Key claims): Claude Code carga los CLAUDE.md al contexto desde el arranque ("naively dropped into context up front").
- `claude-code-cross-session-messaging.web.md` (Key claims; Definitions; Evidence): nombre de sesión con `/rename` o `--name`; `@`-mención de una sesión con nombre (v2.1.232+), ejemplo "Let @api-worker know the schema migration finished"; Claude descubre con `ListAgents` y envía con `SendMessage`; `/list-agents` (alias `/peers`); la sesión inactiva arranca un turno nuevo con el mensaje; el mensaje es texto, nunca el historial; un mensaje no puede aprobar permisos ni cambiar `CLAUDE.md`; política por defecto de `crossSessionInbound` según el modo de permisos de cada sesión. Versiones de la documentación capturada el 2026-10-04.
- `claude-code-agent-teams.web.md` (Key claims): los equipos son experimentales y desactivados por defecto; la demo usa sesiones independientes, sin equipo.

### Speaker notes

Pasos de la demo, unos 4,5 minutos en total. El sistema es el de Pampa Viajes repartido en tres carpetas: `design/` con la marca y las maquetas, `code/` con la aplicación web (frontend y backend) y `outreach/` con campañas y mails. Si se usa otra empresa, conviene mantener esos tres nombres de carpeta.

0. Antes de la clase, el 2026-10-06: `claude --version` tiene que dar 2.1.224 o más para los mensajes entre sesiones y 2.1.232 o más para la mención con `@`. Volver a leer las páginas de subagentes y de mensajes, que cambian rápido, y probar cómo toma el nombre `/rename` en la versión instalada (la alternativa documentada es abrir con `claude --name DESIGN-AGENT`). Probar también que la mención con `@` encuentra nombres en mayúsculas. Abrir las cuatro sesiones con el mismo modo de permisos y ninguna en `bypassPermissions`: una sesión que pide permisos retiene los mensajes de otra que los saltea. Borrar los `CLAUDE.md` de ensayos anteriores.
1. Inspeccionar (1,5 min). En la raíz, abrir `claude` y pedir: "Lanzá tres subagentes Explore nuevos en paralelo, uno para `design/`, otro para `code/` y otro para `outreach/`. Que no sean forks. Cada uno inspecciona solo su carpeta y me devuelve en diez líneas qué contiene, cómo está organizada y qué toma de las otras dos carpetas". El modo fork viene activado por defecto en sesiones interactivas desde la v2.1.232 y un fork hereda la conversación entera, por eso hay que pedir subagentes nuevos. Mostrar que los tres corren a la vez y que al hilo principal solo llegan los resúmenes. Si sobra tiempo, abrir uno de los transcripts en `~/.claude/projects/.../subagents/` para mostrar cuánto trabajo quedó afuera.
2. Especializar (1 min). En la misma sesión: "Con esos tres resúmenes, escribí un `CLAUDE.md` en cada carpeta para un agente que va a trabajar solo en ese repositorio: qué hay, cómo se trabaja ahí, qué no tiene que tocar y qué necesita de los otros dos. Anotá en cada uno que los agentes se llaman DESIGN-AGENT, CODE-AGENT y OUTREACH-AGENT". Remarcar que los subagentes leyeron y la sesión principal escribió, como en la lámina 5.5.
3. Nombrar (1 min). Abrir tres terminales, cada una en su carpeta (`cd design && claude`, y lo mismo con `code` y `outreach`). Lo primero en cada una: `/rename DESIGN-AGENT`, `/rename CODE-AGENT`, `/rename OUTREACH-AGENT`. Cada sesión arranca con el `CLAUDE.md` de su carpeta en el contexto, así que ya es un agente especializado. En CODE-AGENT correr `/list-agents` (alias `/peers`) para ver que aparecen los otros dos.
4. Coordinar (1 min). En CODE-AGENT mandar un solo mensaje: "Vamos a lanzar una promoción de Bariloche en primavera, con el nombre 'Bariloche en flor' y el link /promo/bariloche. @DESIGN-AGENT, armá la pieza gráfica; @OUTREACH-AGENT, escribí el mail de la campaña. Yo hago el cambio en la web". Nombre, texto y link van fijados en el pedido, así que no hay ida y vuelta para acordarlos. Mostrar que las otras dos sesiones, que estaban quietas, arrancan solas un turno cuando les llega el mensaje y que cada una trabaja en su carpeta. Remarcar dos cosas: el mensaje es texto, así que la otra sesión no ve el historial de CODE-AGENT; y un mensaje no puede aprobar permisos ni cambiar el `CLAUDE.md` de otra sesión, así que cada terminal puede pedir permiso y hay que aprobarlo ahí.

Esto no es un equipo de agentes de Claude Code (experimental, lámina 5.6): son tres sesiones independientes que se escriben. Si la clase viene atrasada, el mensaje va solo a DESIGN-AGENT.

Plan B si algo falla en vivo: los pasos 1 y 2 no dependen de los mensajes entre sesiones. Si fallan los mensajes, hacer el paso 4 copiando a mano el pedido entre terminales y señalar que eso es lo que los mensajes ahorran; si falla todo, mostrar la captura de la lámina 5.6.

### Presenter feedback

- [closed] 2026-10-04 — "no me gusta. me interesa mas que el ejemplo sea un repositorio con un sistema que tiene frontend, backend y sistema de “outreach”. se usan subagentes en el prompt inicial para inspeccionar cada repositorio por separado y luego se le pide crear un CLAUDE.md por cada repositorio para tener un agente especializado en cada repositorio. luego se abre cada chat correspondiente a cada agente y se le pide a uno de ellos que se comunique con los otros dos para sincronizarse y trabajar en equipo. importante que al abrir cada uno de los 3 chats lo primero que hagan es renombrar el agente por FRONTEND-AGENT , BACKEND-AGENT y OUTREACH-AGENT. o mejor en vez de frontend, backend, outreach que sea design, code y outreach agents"
  Resolution: Demo rehecha en cuatro pasos sobre un sistema de tres carpetas design/, code/ y outreach/ (propuesta: Pampa Viajes): subagentes Explore nuevos en paralelo inspeccionan cada carpeta, la sesión principal escribe un CLAUDE.md por carpeta, tres sesiones nuevas se renombran con /rename como DESIGN-AGENT, CODE-AGENT y OUTREACH-AGENT, y CODE-AGENT coordina por mensajes entre sesiones una promoción con los otros dos. Notas con prompts, tiempos (6 min), verificaciones del 2026-10-06 y plan B; plantilla cambiada de statement a process; la demo anterior pasó a Cut material.

---

# 6. Multiagente sin LLM

**Goal of this section:** Recordar que los sistemas multiagente son anteriores a los LLM y que dentro de un sistema con LLM puede haber agentes simbólicos, algo que en el trabajo práctico es optativo y suma puntos.

**Presenter feedback:**

---

## 1. Multiagente antes de los LLM
<!-- template: concept-breakdown -->

### Content

**Cuatro sistemas multiagente sin modelos de lenguaje, cada uno con una lección para hoy.**

- **Contract Net (1980).** Un manager anuncia una tarea, los contratistas ofertan y el manager adjudica. El contratista puede subdividir y subcontratar, así que el protocolo arma jerarquías. Es el antecesor del orquestador que reparte trabajo.
- **Kiva (2006).** Robots autónomos que llevan las estanterías hasta el operario. Una instalación grande puede usar 500 robots o más, y los autores reportan productividad doble o mayor.
- **OpenAI Five (2019).** Ganó a los campeones mundiales de Dota 2. Los cinco jugadores son **cinco copias de la misma red** con parámetros compartidos. Compras y habilidades estaban programadas a mano, y la elección de héroes salía de un minimax sobre probabilidades de victoria precalculadas.
- **AlphaStar (2019).** Ganó 5-0 a un profesional de StarCraft II. Lo multiagente está en el **entrenamiento**: una liga de agentes que juegan entre sí. En la partida juega un solo agente.

### Sources

- `contract-net-protocol.web.md` (Key claims): protocolo de 1980 de Reid G. Smith, manager y contractor, "can implement hierarchical organizations".
- `kiva-warehouse-wurman-2008.web.md` (Key claims): 500 o más vehículos, productividad "by a factor of two or more", primera instalación permanente en el verano de 2006. (Inconsistencies) la captura no describe cómo se coordinan los robots.
- `openai-five-2019.web.md` (Key claims): victoria contra OG el 13 de abril de 2019; "Separate replicas of the same policy function (with identical parameters θ)"; partes programadas (compras, habilidades, courier) y draft por minimax.
- `alphastar-deepmind-2019.web.md` (Key claims): 5-0 contra MaNa; la liga de AlphaStar; (Inconsistencies) lo multiagente es el entrenamiento y el jugador desplegado es un agente por lado.

### Speaker notes

La lámina corrige dos ideas que circulan. OpenAI Five no son cinco especialistas: es una misma red copiada cinco veces, con un parámetro, team spirit, que regula cuánto comparte cada héroe la recompensa del equipo. AlphaStar no juega en equipo: la población de agentes existe para entrenar, y en la partida queda uno. De Kiva solo tenemos el resumen del artículo, que no dice si la coordinación es central o distribuida, así que no lo afirmamos. Contract Net es el que más se parece a lo que hacemos hoy con LLM. Tiempo objetivo: ~2 min.

### Presenter feedback

---

## 2. Agentes simbólicos dentro de un sistema con LLM
### Content

**Un agente sin LLM dentro de un sistema con LLM hace lo que un modelo de lenguaje hace mal: contar, validar reglas, ejecutar.**

- **El terminal de Magentic-One.** ComputerTerminal ejecuta código y comandos de forma determinística, sin LLM.
- **El presupuesto de Pampa Viajes.** Suma y compara contra el tope con reglas.
- **El tablero de AutoGen, mitad y mitad.** Conversa a través de un LLM y valida cada jugada con reglas programadas. Sin esa validación, los jugadores LLM hacían jugadas ilegales aunque el prompt les pidiera no hacerlas.
- **En el trabajo práctico.** Un agente sin LLM es optativo y suma puntos.

### Sources

- `magentic-one-2024.web.md` (Key claims): ComputerTerminal "deterministically executes code and shell commands, no LLM"; algunas subtareas pueden ir a "non-AI tools".
- `autogen-2023.web.md` (Images, Figura 14): "Chess Board agent (LLM + Python)"; (Evidence A6): sin el agente tablero "prompting alone … still led to illegal moves".

### Speaker notes

El criterio para decidir qué agente no lleva LLM: si la respuesta correcta se puede escribir como regla y verificar, no hace falta un modelo. El agente simbólico además es auditable, cosa que les vamos a pedir. El tablero de AutoGen muestra el caso intermedio, un agente que habla con LLM y decide con código. Un detalle de vocabulario: en Pampa Viajes el presupuesto aparece primero como herramienta (en el agente único) y después como agente. Como agente tiene su lugar en la arquitectura, recibe mensajes y puede rechazar. Tiempo objetivo: ~2 min.

### Presenter feedback

---

# 7. Cómo fallan

**Goal of this section:** Dar la taxonomía de fallas de MAST con sus porcentajes y advertir que el aislamiento de contexto no viene por defecto en los frameworks.

**Presenter feedback:**

---

## 1. Cómo fallan

### Content

**MAST analizó 1.642 trazas de 7 sistemas multiagente abiertos y encontró tasas de falla de 41 % a 86,7 %. Las fallas caen en tres categorías.**

| Categoría | Parte de las fallas | Modos más frecuentes |
|---|---|---|
| **Diseño del sistema** | 44,2 % | repetir pasos (15,7 %), no saber cuándo terminar (12,4 %), desobedecer la tarea (11,8 %) |
| **Desalineación entre agentes** | 32,35 % | razonamiento que no coincide con la acción (13,2 %), descarrilarse (7,4 %), no pedir aclaración (6,8 %) |
| **Verificación** | 23,5 % | verificación incorrecta (9,1 %), incompleta (8,2 %), terminar antes de tiempo (6,2 %) |


- **Agentless, en una línea.** Un pipeline fijo sin agentes autónomos resolvió 32 % de SWE-bench Lite a 0,70 dólares por problema, más que los agentes abiertos de ese momento.

### Sources

- `mast-why-mas-fail-2025.web.md` (Key claims, §4): 1.642 trazas, 7 frameworks, 41 % a 86,7 %, los porcentajes de cada modo; los totales por categoría (44,2; 32,35; 23,5) suman los modos de §4; el ejemplo de las notas es la Figura 3 (FM-2.4, information withholding).
- `agentless-2024.web.md` (Key claims): 32,00 % (96 de 300) en SWE-bench Lite con costo de 0,70 dólares, "compared with all existing open-source software agents".

### Speaker notes

Un ejemplo de retención de información del paper, para contar sin imagen: el agente de teléfono lee en la documentación que el usuario es el número de teléfono, falla el login y le pide al supervisor credenciales nuevas sin contarle lo que aprendió. Del paper hay dos conclusiones para llevarse. Las fallas entre agentes no se arreglan con un protocolo de mensajes como MCP: los agentes no modelan qué necesita saber el otro. Y tener un verificador ayuda, pero no alcanza si verifica cosas superficiales, como que el código compile. Agentless va en una línea como recordatorio de que un workflow bien diseñado puede ganarle a un agente. Tiempo objetivo: ~2,5 min.

### Presenter feedback

---

## 2. El aislamiento no viene de fábrica

### Content

**Los frameworks comparten contexto por defecto. Si quieren aislamiento, lo tienen que configurar.**

- **OpenAI Agents SDK.** En un handoff, el agente que recibe ve todo el historial. Se recorta con `input_filter`.
- **LangGraph Swarm.** El handoff pasa el historial completo y todos los agentes escriben en una sola lista de mensajes. Se aísla con un esquema de estado propio por agente.
- **Claude Code.** Un subagente arranca con contexto limpio, pero un *fork* hereda la conversación entera y pierde ese aislamiento.

### Sources

- `openai-agents-sdk-handoffs.web.md` (Key claims; Inconsistencies): historial completo por defecto, `input_filter`.
- `langgraph-swarm.web.md` (Key claims): "passes **full** message history"; "messages from **all** of the agents will be combined into a single, shared list"; esquema de estado separado para aislar.
- `claude-code-subagents.web.md` (Key claims): "Each subagent starts with a fresh, isolated context window"; un fork "drops the input isolation that subagents otherwise provide".

### Speaker notes

Para el TP esta lámina es práctica: la palanca de aislamiento de contexto es la que más les va a ayudar con un modelo débil, y es la que los frameworks no les dan sola. Revisen en los logs qué contexto recibe cada agente. Si un agente ve el historial de todos, no está aislado aunque tenga su propio prompt. Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

# Conclusiones

**Goal of this section:** Resumir la clase en una lámina y anunciar el trabajo práctico con sus requisitos de reporte.

**Presenter feedback:**

---

## 1. Lo que hay que llevarse

### Content

**Un sistema multiagente compra especialización, aislamiento de contexto y paralelismo, y los paga en llamadas, tokens y nuevas formas de fallar.**

1. **Un agente percibe y actúa.** El LLM es una pieza; el agente es el lazo con el ambiente.
2. **La arquitectura decide quién elige el próximo paso y qué ve cada agente.** Pipeline y router dejan la decisión en el código; orquestador, handoffs y red se la dan al modelo.
3. **Primero el agente único.** Toda arquitectura se compara contra él, con las mismas tareas y midiendo llamadas y tokens.
4. **El agente principal que delega bajo demanda** concentra las decisiones en un contexto y manda afuera el trabajo de lectura, en paralelo.
5. **El aislamiento hay que configurarlo**, y un agente sin LLM resuelve lo que se puede escribir como regla.

### Sources

- Síntesis de la clase; sin fuentes nuevas.

### Speaker notes

Leer la lámina de arriba abajo en un minuto y medio y pasar al TP. Si queda tiempo para una pregunta, la buena es: "¿qué arquitectura usarían para Pampa Viajes y por qué?". Tiempo objetivo: ~1,5 min.

### Presenter feedback

---

## 2. El trabajo práctico: LLM débil, benchmark, varias arquitecturas
### Content

**Van a resolver un benchmark con un LLM débil y barato, construyendo varias arquitecturas multiagente donde la especialización y el aislamiento de contexto sean lo que lo hace resolvible bajo restricciones.**

- **Arquitecturas.** Un agente único con todas las herramientas como línea de base y al menos tres arquitecturas más, comparadas sobre el mismo benchmark.
- **Agente sin LLM (optativo).** Un agente simbólico de reglas, validación o ejecución no es obligatorio y suma puntos.
- **Reutilizar.** El RAG y el servidor MCP de la misión anterior, como herramientas de los agentes.
- **Reporte.** Logs de cada ejecución, auditabilidad de qué vio y qué decidió cada agente, rendimiento en el benchmark, uso de tokens por arquitectura y la colaboración entre integrantes en GitHub, que se mide para la nota conceptual de cada alumno. Se evalúan también las decisiones de desarrollo, arquitectura y eficiencia.

### Sources

- Consigna de la cátedra (nota de Marco del 2026-10-04 registrada en `memory.md`, Step 4); sin fuente de corpus.

### Speaker notes

Es un anuncio: la consigna completa, el benchmark, el modelo y las fechas están en la misión. Lo que hay que transmitir es el espíritu: con un modelo fuerte cualquier arquitectura parece funcionar; con uno débil se nota cuál le limpia el contexto y le da tareas chicas. La comparación contra el agente único es obligatoria porque es lo que justifica todo lo demás. Insistir en la colaboración: commits de cada integrante, revisiones y discusiones en el repositorio. Tiempo objetivo: ~2 min.

### Presenter feedback

- [closed] 2026-10-04 — "un solo agente con todas las tools de base y al menos 3 arquitecturas mas"
  Resolution: La viñeta Arquitecturas pide un agente único con todas las herramientas como línea de base y al menos tres arquitecturas más; la tesis y las notas de esta lámina dicen lo mismo.
- [closed] 2026-10-04 — "adicional no obligatorio, suma puntos"
  Resolution: El agente sin LLM pasó a optativo con puntos extra en la tesis, las notas de 3.1, el objetivo de la sección 6, la lámina 6.2 y esta lámina (viñeta y notas); salió la pregunta abierta sobre requisitos del TP.

---

# Open questions

- Lámina 1.7: la sigla PEAS no está en ningún registro con definición textual (`wikipedia-intelligent-agent.web.md` no la menciona; el deck de Biomédica habla de formulaciones "PEAS-like"). Capturar el capítulo 2 de Russell y Norvig si se quiere cita.
- Lámina 1.10: `wikipedia-intelligent-agent.web.md` dice que Russell y Norvig (2003) agrupan los agentes en cinco clases; algunas ediciones presentan cuatro programas básicos más el agente que aprende. La lámina 1.10 muestra cuatro y el quinto (el agente que aprende) aparece en la 1.6.
- Lámina 1.4: "el programa corre sobre la arquitectura del agente" (agente = arquitectura + programa) es la formulación del capítulo 2 de Russell y Norvig, que no está en el corpus; `wikipedia-intelligent-agent.web.md` solo dice que el programa "is the actual code that runs on the agent". Las notas advierten el choque con "arquitectura" del bloque 3.
- Lámina 1.5: que la medida de performance la fija el diseñador, y el motivo de las notas (un agente que se pone su propia nota puede convencerse de que lo hizo bien), descansan en el capítulo 2 de Russell y Norvig. El corpus solo sostiene que la función de recompensa "allows programmers to shape its desired behavior" y que la medida evalúa "any given sequence of environment states".
- Lámina 1.6: la definición de autonomía (apoyarse en lo que el agente percibe y aprende más que en el conocimiento previo del diseñador, y aprender para compensar un conocimiento inicial incompleto o equivocado) es del capítulo 2 de Russell y Norvig; el corpus sostiene solo que aprender permite "gradually surpass the bounds of their initial knowledge". "Racional no exige omnisciencia" sí está en `wikipedia-intelligent-agent.web.md`. El ejemplo del taxi chocado es ilustrativo, sin fuente.
- Lámina 1.8: las definiciones de completamente observable y de determinístico, y los ejemplos de spam, goma pinchada y videojuego nuevo, son redacción del editor sobre el capítulo 2 de Russell y Norvig; el deck de Biomédica solo nombra esas dos dimensiones. Capturar el capítulo 2 si se quiere cita textual.
- Lámina 1.9: del corpus salen solo las celdas de Biomédica (crucigrama observable, determinístico, estático, un agente; ajedrez observable, determinístico, competitivo; taxi parcial, estocástico, dinámico, continuo, multiagente competitivo y colaborativo; asistente parcial y dinámico). El resto es clasificación del editor: la fila episódico o secuencial completa, discreto y conocido en crucigrama y ajedrez, "sin reloj" en ajedrez, conocido en el taxi, y agentes, determinismo, discreto y "en parte" en el asistente. Revisar antes de la clase, sobre todo "uno o varios, colaborativo" y "en parte" del asistente.
- Láminas 1.2, 1.4 y 1.10: el termostato como agente mínimo está en el lead de `wikipedia-intelligent-agent.web.md`; como ejemplo de agente reflejo simple, la página lo cita a un blog y a IBM (`[open question]` en el registro). Las láminas lo usan como regla condición-acción, sin atribuírselo a Russell y Norvig.
- Láminas 1.3 y 1.7: en Biomédica, la aspiradora tiene un motor de movimiento con cuatro direcciones (izq/der/adelante/atrás) pero solo dos acciones de movimiento (MoverIzquierda, MoverDerecha); las láminas copian la fuente tal cual. La columna del taxi se armó con el auto autónomo de `wikipedia-intelligent-agent.web.md`; los actuadores (acelerador, freno, dirección) se derivan de sus acciones.
- Lámina 4.7: la celda "el especialista recibe solo lo que el manager le pasa" para agentes como herramientas es inferencia del patrón; `openai-agents-sdk-multi-agent.web.md` no lo dice textual. Verificar en la documentación de tools del SDK o con un log antes de la clase.
- Lámina 4.4: el −31 % al reemplazar el orquestador de Magentic-One por un GroupChat sale de la Figura 3 del paper, que no se capturó; no se cita. Capturar la figura si se quiere el número.
- Lámina 5.6 y demo 5.7: versiones y comportamientos de Claude Code (anidamiento de 3 niveles, 20 subagentes concurrentes, v2.1.224 para mensajes, v2.1.232 para la mención con `@` y el fork mode por defecto, `/rename` con el nombre como argumento, `@`-mención de nombres en mayúsculas, flag experimental de equipos) son de la documentación capturada el 2026-10-04; re-verificar con `claude --version` y las páginas en vivo antes del 2026-10-07.
- Lámina 5.2: el 90,2 % es una mejora relativa sobre una evaluación interna no publicada de Anthropic; se presenta con esa aclaración.
- Lámina 6.1: `kiva-warehouse-wurman-2008.web.md` solo trae el resumen; no sostiene cómo se coordinan los robots ni la compra por Amazon. La lámina no lo afirma.
- Lámina 3.9: los números de LangChain son escenarios ilustrativos de la documentación; el "67% fewer tokens" de la página no coincide con su propia tabla y no se usa.
- Conclusiones 2: benchmark, modelo débil y fechas del TP quedan para la misión.
- Demo 5.7: hace falta preparar antes del 2026-10-07 el repositorio de la demo, con tres carpetas `design/`, `code/` y `outreach/` y contenido chico pero realista en cada una. Propuesta: el sistema de Pampa Viajes (marca y maquetas; aplicación web con frontend y backend; campañas y mails). A confirmar por la cátedra la empresa y quién arma el repositorio.

# Cut material

- Cifras de producción del deck de Biomédica (95 %+ de accuracy requerida, caída de 92 % a 58 % de 5 a 20+ herramientas, ~85 % de cumplimiento de reglas por prompt): sin fuente identificable en el corpus (`aitutorial-agents-overview.web.md` las da sin cita). Fuera de la clase.
- Sección MCP del deck de Biomédica: ya vista en la clase 7.
- Memoria de agentes como bloque propio (dos niveles, MemorySaver, Mem0, Zep, patrones code-driven, LLM-driven y background extraction): queda fuera; la memoria aparece solo como aislamiento de contexto y como pizarra.
- Valores Elo de AlphaGo Zero: el registro advierte que las dos figuras de la página no coinciden; no se citan. AlphaGo, AlphaGo Zero y AlphaZero quedan fuera del bloque 6, que usa OpenAI Five y AlphaStar.
- Caso NSCLC (soporte a decisiones clínicas) del deck de Biomédica: reemplazado por Pampa Viajes.
- Arena pública de OpenAI Five (99,4 % de victorias): cuenta como victorias las partidas abandonadas; no aporta a la clase.
- Lámina 1.3, dimensiones del ambiente como viñetas (observable, determinístico, episódico, estático, discreto, conocido): pasaron a las notas para bajar la densidad. Volvieron al cuerpo en la ronda 2 (2026-10-04), con definición y ejemplo, en la lámina 1.8.
- Lámina 1.3 (ahora 1.8), notas: "Las otras seis dimensiones las nombramos de pasada, porque ya las vieron o se entienden solas": el presentador pidió definirlas en la lámina.
- Lámina 3.6, viñeta "Por defecto **el agente que recibe ve todo el historial**, así que no hay aislamiento de contexto" y la frase de notas "en los tres frameworks del corpus, el handoff comparte todo el historial por defecto. Si quieren aislamiento, lo tienen que pedir con un filtro": el punto vive en la lámina 7.2.
- Lámina 4.7, viñeta "Para aislar en handoffs. `input_filter` decide qué historial ve el agente que recibe": el punto vive en la lámina 7.2.
- Lámina 4.3, notas: "El agente tablero del ajedrez es un agente sin LLM … sin él, los jugadores LLM hacían jugadas ilegales": era incorrecto (el tablero es LLM + Python) y repetía la lámina 6.2.
- Lámina 3.7, AutoGen group chat como caso real de red: tiene un manager que elige quién habla, así que no es una red sin jefe.
- Lámina 7.1, imagen `research/corpus/mast-why-mas-fail-2025.web/images/phone-agent-narrow.png`: la lámina queda con la tabla; el ejemplo se cuenta en las notas.
- Conclusiones 2, viñetas separadas "Trabajo en GitHub" y "Criterio" (fusionadas en "Reporte") y la línea "La consigna completa, el benchmark, el modelo y las fechas están en la misión" (pasó a las notas).
- Demo 5.7 anterior (subagentes Explore sobre `missions/rag-mcp-transformers/`, `missions/prompting/` y `talks/`; un mensaje a una sesión `revisor`; un equipo experimental de tres compañeros para diseñar Pampa Viajes): reemplazada por la demo de tres repositorios pedida por el presentador el 2026-10-04.
