---
presentation: Inteligencia Artificial Generativa (AI Gen)
class: "Agentes y sistemas multiagente"
research: research/corpus/
description: Slides are grouped into Sections. Each Section contains one or more Slides.
presenter: Paulo Veiga, Claudio Righetti, Marco Sorondo (Universidad Austral)
audience: Estudiantes de grado de Ingeniería de Software con base técnica fuerte. Clase presencial en vivo.
duration: ~131 min con pausa de 10 (clase de 2 h)
date: 2026-10-07
---

# Thesis

**Claim:** Un agente basado en LLM es un loop en el que el modelo elige su próxima acción según lo que observó. Los tipos de agente cambian cuándo se planifica y cuántas veces se vuelve a razonar, y las arquitecturas multiagente cambian cómo se reparte el contexto entre varios loops.

**Why it matters:** Cada una de esas decisiones se paga en llamadas al LLM, tokens, latencia y confiabilidad. Según Anthropic, un sistema multiagente gasta cerca de 15× los tokens de un chat, y LangChain recomienda agregar tools antes que agentes. Quien sabe qué resuelve cada forma puede elegir la más simple que alcanza para su problema.

---

# Agenda

**Narrative arc:** La clase abre con una pregunta que la sala contesta mal con frecuencia: si un LLM es un agente. La sección 1 responde con la definición clásica de Russell & Norvig (sensores, actuadores, ambiente, racionalidad, función y programa de agente, arquitecturas clásicas) y llena la ficha PEAS para una aspiradora y para un LLM. La sección 2 formaliza al agente LLM con la notación del paper de ReAct (observación, acción, contexto, política), lo ubica en la descomposición de Weng y termina en cuándo conviene construir un agente y cuándo alcanza un workflow. La sección 3 toma la pieza que convierte a un LLM en algo que actúa, la tool: qué es, cómo se ve en código, cómo falla y cómo se diseña. La sección 4 fija las dos preguntas con las que se comparan los tipos de agente y recorre ReAct, el tipo base: el pensamiento como acción, una trayectoria del paper, el prompt de completado que la produce y el grafo en LangGraph. La sección 5 sigue de a uno con Plan-and-Execute, Reflexion, ReWOO y orquestador con workers, y junta los cinco en una tabla; el quinto reparte el contexto entre varios loops. Después de la pausa, la sección 6 retoma el contexto como recurso finito y pago y muestra los límites de un solo agente: el contexto se degrada, las tools compiten y un solo prompt no especializa. Con eso define sistema multiagente y sus tres palancas, y frena con la recomendación de LangChain de empezar por un agente con buenas tools. La sección 7 precisa qué hace un subagente y presenta los cuatro patrones de LangChain con su costo, más cuatro topologías: red adaptativa, pipeline, pizarra y jerarquía. La sección 8 muestra cuatro sistemas publicados, de MetaGPT a Magentic-One, y los separa del debate y de Mixture-of-Agents, que ponen varios LLM sin tools sobre una misma pregunta. La sección 9 da el criterio para repartir: el precio en tokens, cómo fallan según MAST, el aislamiento que hay que configurar y el debate entre Cognition y Anthropic, que se resuelve preguntando si el trabajo lee o escribe; un caso de Kore.ai aplica esa regla. El cierre deja un árbol de decisión para elegir la arquitectura más simple que alcanza.

**Sections (in delivery order):**

- 1. Qué es un agente
- 2. El agente basado en LLM
- 3. Los agentes tienen tools
- 4. ReAct
- 5. Otros cuatro tipos
- 6. Límites de un agente
- 7. Patrones multiagente
- 8. Implementaciones reales
- 9. Cuándo repartir

---

# 1. Qué es un agente

**Goal of this section:** Llegar a la definición clásica de agente de Russell & Norvig: sensores, actuadores, ambiente, racionalidad, función y programa de agente, y las arquitecturas clásicas. La sección cierra con la ficha PEAS llenada para una aspiradora y para un agente LLM. Al salir, la sala distingue un agente de un LLM suelto.

---

## 1. ¿Un LLM es un agente?

<!-- template: quiz -->

### Content

¿Un LLM que recibe una pregunta y devuelve una respuesta es un agente?

- A. Sí, cualquier LLM es un agente.
- B. Sí, siempre que el modelo sea lo bastante grande.
- C. Por sí solo, no.
- D. No, porque un agente tiene que ser un robot.

**Respuesta:** C. En el uso diario se llama "agente" a cualquier LLM o sistema basado en LLM. Un LLM no es un agente por sí solo, y existen muchos agentes que no usan modelos de lenguaje.

### Sources

- `corpus/AIG4B-Clase-6-Agent.pptx.md` — slide 3, "Agentes – Una palabra mal utilizada": "Un LLM no es un agente por sí solo. Además, existen muchos tipos de agentes que no involucran en absoluto modelos de lenguaje."

### Speaker notes

Abrir con la votación a mano alzada antes de revelar. La pregunta funciona porque la mayoría de la sala llega con el uso popular de la palabra, y la clase entera se apoya en desarmarlo.

A es el uso popular, y es justo lo que la lámina corrige. B confunde tamaño con forma de trabajo: el modelo más grande sigue recibiendo texto y devolviendo texto. D es el extremo opuesto, y la lámina 1.7 lo desarma con una aspiradora autónoma y con un agente LLM en la misma tabla.

La respuesta deja una pregunta abierta a propósito: si un LLM solo no es un agente, ¿qué le falta? Las secciones 1 y 2 contestan en dos pasos. Primero la definición clásica, que no habla de LLMs. Después la formalización del paper de ReAct, donde el LLM pasa a elegir acciones en un loop.

Tiempo: unos 3 minutos con la votación.

---

## 2. La definición de Russell & Norvig

### Content

> "An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators..."
> — Russell & Norvig, *Artificial Intelligence: A Modern Approach*

![El loop agente-ambiente de Russell y Norvig](images/s1-2-1-lazo-agente-ambiente.png)
<!-- ascii-source:
+------------------------------------------+
|                 AMBIENTE                 |
+------------------------------------------+
       |                           ^
       | percepciones              | acciones
       v                           |
+--------------+           +--------------+
|   Sensores   |           |  Actuadores  |
+--------------+           +--------------+
       |                           ^
       v                           |
+------------------------------------------+
|      AGENTE: decide qué acción tomar     |
|      a partir de lo que percibió         |
+------------------------------------------+
-->
<!-- ascii-note:
intent: el loop agente-ambiente de la definicion clasica; es el lazo cerrado que todas las demas laminas de la seccion refinan.
emphasize: la caja AGENTE como unico punto de decision (acento rojo); el lazo cerrado percepciones -> decision -> acciones -> ambiente.
labels: AMBIENTE, Sensores, Actuadores, AGENTE, percepciones, acciones.
-->

### Sources

- `corpus/AIG4B-Clase-6-Agent.pptx.md` — slide 4, cita verbatim de Russell & Norvig; slide 3, versión en español ("cualquier entidad que percibe su entorno mediante sensores y actúa sobre él mediante actuadores").

### Speaker notes

Leer la cita completa. Es la definición canónica de toda la teoría de agentes en IA clásica, y la clase vuelve a ella en la lámina 1.7 y en la sección 2 para ver qué le agrega un LLM.

En español, para quien la quiera anotar: un agente es cualquier entidad que percibe su entorno mediante sensores y actúa sobre él mediante actuadores. Es una traducción del deck del curso, no una cita de una edición en español.

Señalar en el diagrama que la única caja que decide es la del agente. Sensores y actuadores son interfaces. El ambiente es todo lo que no es el agente.

---

## 3. Lo que la definición no menciona

### Content

La definición es amplia a propósito.

- **Sin ML ni LLMs** No nombra machine learning, deep learning, LLMs, tools ni RAG. Son implementaciones posibles de un agente.
- **Sin software** Tampoco exige un programa. Un sistema mecánico o electrónico también encaja.
- **Sistemas biológicos** Células, insectos, animales y personas son agentes bajo esta definición.

### Sources

- `corpus/AIG4B-Clase-6-Agent.pptx.md` — slide 5, "Comentarios sobre la definición": Sin ML ni LLMs, Sin programas, Sistemas biológicos.

### Speaker notes

Esta lámina cierra la pregunta del quiz desde el otro lado: la palabra "agente" es anterior a los LLMs y mucho más amplia que ellos.

La consecuencia práctica para ingeniería: cuando alguien dice "agente" en una reunión de diseño, conviene preguntar qué percibe, qué puede hacer y en qué ambiente. La lámina 1.7 da esas preguntas en forma de plantilla.

---

## 4. Racionalidad: actuar bien según una medida

### Content

Un agente racional elige la acción que maximiza su medida de performance, dada la evidencia de sus percepciones y lo que ya sabe.

- **Medida de performance** El criterio que define el éxito del agente. Sin ella no hay racionalidad posible.
- **Conocimiento previo** Lo que el agente sabe del ambiente antes de empezar a actuar.
- **Acciones disponibles** El conjunto de acciones que el agente puede ejecutar en su entorno.
- **Secuencia de percepciones** El historial de todo lo que el agente observó hasta el momento.

### Sources

- `corpus/AIG4B-Clase-6-Agent.pptx.md` — slide 6, cita de Russell & Norvig sobre agente racional; slide 7, "Racionalidad" y sus cuatro factores.

### Speaker notes

**Original:** "A rational agent is one that does the right thing... This notion of desirability is captured by a performance measure that evaluates any given sequence of environment states." — Russell & Norvig.

La racionalidad agrega optimización a la definición: percibir y actuar no alcanza, hay que hacerlo bien según un criterio definido.

Guardar el cuarto factor para la lámina 2.1. La secuencia de percepciones es lo que el paper de ReAct va a llamar contexto, y en un agente LLM es el texto que el modelo tiene a la vista.

La medida de performance reaparece en la sección 5 con Reflexion, que solo funciona cuando hay un criterio claro de éxito.

---

## 5. Función de agente y programa de agente

### Content

El comportamiento de un agente se especifica con una función y se implementa con un programa.

- **Función de agente** `f: P* → A`. Asigna una acción a cada secuencia de percepciones posible; P* es el conjunto de todas esas secuencias. Es una descripción matemática y nadie la ejecuta.
- **Programa de agente** El código que corre en el agente. Recibe la percepción actual y devuelve una acción. Si necesita la historia, la tiene que guardar él.

El programa de un termostato entra en una regla: si la temperatura bajó del umbral, encender; si no, apagar.

### Sources

- `corpus/wikipedia-intelligent-agent.web.md` — Definitions: agent function f : P* → A, "maps the agent's entire history of percepts to an action" (cita Russell & Norvig 2003, p. 33), descripción matemática abstracta; P* = "the set of all possible percept sequences" ("zero or more percepts"); agent program, "the actual code that runs on the agent", "takes the *current* percept as input and produces an action as output"; termostato como agente reflejo simple (el registro marca que ese ejemplo se lo cita a un blog y a IBM, no a Russell & Norvig).

### Speaker notes

Es la distinción que más se pierde en el uso diario. La función describe qué haría el agente ante cualquier historia posible; escrita como tabla, para casi cualquier agente sería infinita. El programa es el código que corre y solo ve la percepción de ahora. Si el agente necesita recordar, el programa guarda un estado, y ese es el agente con modelo de la lámina siguiente.

P* lleva la estrella porque una secuencia puede tener cero, una o muchas percepciones.

Para el agente LLM, la lámina 2.1 escribe la función como una política π(a_t | c_t) sobre el contexto. El programa es el código que arma ese contexto, llama al modelo y ejecuta las tools. La sección 4 muestra ese código para ReAct.

El termostato sale de Wikipedia, que lo cita a un blog y a IBM. Acá se usa como ejemplo de regla condición-acción, sin atribuírselo a Russell & Norvig.

---

## 6. Arquitecturas clásicas de agente

### Content

Russell & Norvig ordenan los agentes según lo que hay entre la percepción y la acción. Cada tipo agrega una pieza al anterior.

![Agente basado en modelo y en utilidad: sensores, estado interno, modelo de cómo evoluciona el mundo y de qué producen las acciones, utilidad de cada estado previsto y actuadores](images/500px-Model_based_utility_based.png)

- **Reflejo simple** Aplica una regla "si condición, entonces acción" a la percepción actual. Funciona solo si el ambiente es completamente observable.
- **Reflejo con modelo** Guarda un estado interno con la parte del mundo que no ve.
- **Basado en objetivos** Predice qué produce cada acción y elige la que lleva a un estado meta.
- **Basado en utilidad** Puntúa los estados con una función de utilidad y elige la acción de mayor utilidad esperada.
- **Que aprende** Un crítico le dice cómo le va, y un elemento de aprendizaje mejora al resto del agente.

### Sources

- `corpus/wikipedia-intelligent-agent.web.md` — "Classic taxonomy", las cinco clases de Russell & Norvig (2003, cap. 2) con sus definiciones; regla "if condition, then action" y "only succeeds when the environment is fully observable"; estado interno del agente con modelo; estados meta; "chooses the action that maximizes the expected utility"; agente que aprende con elemento de aprendizaje, elemento de performance, crítico y generador de problemas, que le permite "gradually surpass the bounds of their initial knowledge"; racionalidad "does not require an agent to be omniscient" (notas). Imagen `wikipedia-intelligent-agent.web/images/500px-Model_based_utility_based.png` ("Model-based, utility-based agent"; el registro transcribe "Precepts" con error de tipeo).
- `corpus/bdi-agents.web.md` — creencias, deseos e intenciones; BDI separa elegir un plan de ejecutarlo y no describe la interacción entre agentes (solo en notas).

### Speaker notes

El diagrama es el más completo de la serie de Wikipedia: estado interno, un modelo del mundo y una utilidad que puntúa cada estado previsto. Los tipos anteriores salen de sacarle piezas.

El agente que aprende cubre la autonomía: lo que le cargó su diseñador puede estar incompleto, y aprender le permite superarlo. Racional tampoco quiere decir omnisciente. Se le pide que decida bien con lo que sabe y lo que percibió.

Lectura de la cátedra: Reflexion (lámina 5.4) se parece al agente que aprende, con un evaluador que hace de crítico. Lo que aprende queda escrito en el contexto; los pesos no cambian.

BDI modela un solo agente con creencias, deseos e intenciones. La coordinación entre varios la resuelven protocolos como Contract Net (lámina 7.10).

---

## 7. La misma ficha, dos agentes

### Content

Russell & Norvig especifican un agente con la ficha PEAS: performance, ambiente (*environment*), actuadores y sensores. La misma ficha sirve para una aspiradora y para un agente LLM.

| Campo | Aspiradora autónoma | Agente basado en LLM |
|---|---|---|
| Agente | Aspiradora autónoma (robot o modelo abstracto) | LLM con razonamiento y acceso a tools externas |
| Sensores | Detector de suciedad, posición actual en la grilla | Texto del usuario, contexto previo, resultados de tools |
| Actuadores | Motor de movimiento (izq/der/adelante/atrás), motor de succión | Generar texto, razonar, ejecutar comandos, llamar APIs, producir planes |
| Ambiente | Grilla n×m, parcialmente observable, determinístico | Digital, simbólico, parcialmente observable, dinámico |
| Performance | +10 limpiar celda sucia · −1 moverse · −5 aspirar celda limpia · −10 chocar | Calidad, relevancia y precisión de las respuestas; satisfacción del usuario |

### Sources

- `corpus/AIG4B-Clase-6-Agent.pptx.md` — slide 8 (Vacuum Cleaner, valores de performance verbatim) y slide 18 (formulación del agente basado en LLM); slide 12, dimensión "un solo agente o multiagente" (solo en notas).
- `corpus/aig4b-clase-6-agentes-biomedica.pdf.md` — formulaciones "PEAS-like" de la aspiradora, el robot móvil y AlphaGo. La sigla PEAS y su expansión vienen del capítulo 2 de Russell & Norvig, que no está en el corpus (`corpus/russell-norvig-aima.web.md` es solo el índice).

### Speaker notes

La tabla responde el quiz del arranque. El LLM se vuelve agente cuando tiene sensores (lo que entra a su contexto, incluidos los resultados de tools) y actuadores (llamar APIs, ejecutar comandos). Sin tools, el único actuador que le queda es generar texto. La sección 3 define qué es una tool.

Leer la columna de la aspiradora fila por fila y pedirle a la sala que complete la del LLM antes de revelarla. Funciona bien porque la plantilla obliga a pensar en ambiente y performance, que son las filas que se suelen olvidar al diseñar un agente.

Notar la fila Ambiente del agente LLM: parcialmente observable y dinámico. Por eso el agente tiene que observar después de cada acción. Una base de datos cambia mientras el agente piensa, y una búsqueda devuelve solo una parte del mundo.

El deck del curso clasifica los ambientes en siete dimensiones (slide 12). Una importa para esta clase: si en el ambiente actúa un solo agente o varios. Las secciones 6 a 9 tratan el caso en que varios agentes LLM se reparten una misma tarea.

Las acciones de la aspiradora en el deck original: Aspirar, MoverIzquierda, MoverDerecha, Esperar.

Cierre de la sección 1. Tiempo acumulado: unos 14 minutos.

---

# 2. El agente basado en LLM

**Goal of this section:** Leer al agente basado en LLM con la definición de la sección 1 y formalizarlo con la notación del paper de ReAct (observación, acción, contexto, política). Al salir, la sala distingue un agente de un workflow y sabe cuándo conviene construir uno.

---

## 1. El agente LLM, formalizado

### Content

El paper de ReAct (Yao et al., 2022) escribe el loop del agente con cuatro piezas.

- **Observación** `o_t ∈ O`, lo que el agente recibe del ambiente en el paso t.
- **Acción** `a_t ∈ A`, lo que el agente hace sobre el ambiente.
- **Contexto** `c_t = (o_1, a_1, …, o_{t−1}, a_{t−1}, o_t)`, todo lo observado y hecho hasta ese paso.
- **Política** `π(a_t | c_t)`, la regla que elige la acción a partir del contexto. En ReAct, un LLM genera las acciones y cumple ese papel.

![El loop del agente LLM con la notación de ReAct](images/s2-1-1-lazo-formalizado.png)
<!-- ascii-source:
     +----------------------------------+
     |  contexto  c_t                   |
     |  (o_1, a_1, ..., a_{t-1}, o_t)   |
     +----------------------------------+
                      |
                      v
            +-------------------+
            |  política (LLM)   |
            |   π(a_t | c_t)    |
            +-------------------+
                      |
                      v   a_t ∈ A
            +-------------------+
            |     AMBIENTE      |
            +-------------------+
                      |
                      v   o_{t+1} ∈ O
     se suma al contexto c_{t+1} y el loop sigue
-->
<!-- ascii-note:
intent: el mismo lazo de la lamina 1.2, ahora con la notacion del paper de ReAct; el contexto crece en cada vuelta.
emphasize: la caja de la politica (LLM) en rojo; la flecha final que devuelve la observacion al contexto.
labels: contexto c_t, politica pi(a_t | c_t), AMBIENTE, a_t en A, o_{t+1} en O.
-->

### Sources

- `corpus/yao-2022-react.pdf.md` — Sección 2, verbatim: "At time step t, an agent receives an observation o_t ∈ O from the environment and takes an action a_t ∈ A following some policy π(a_t | c_t), where c_t = (o_1, a_1, ···, o_{t−1}, a_{t−1}, o_t) is the context to the agent." El LLM congelado (PaLM-540B) genera acciones y pensamientos por few-shot prompting. Sección 3.1: una API de Wikipedia con tres acciones (search, lookup, finish); el paper no usa la palabra "tool" (notas).

### Speaker notes

Es la misma figura de la lámina 1.2 escrita con símbolos. Los sensores son la observación, los actuadores son la acción, y la decisión es una política que mira el contexto.

El contexto es la secuencia de percepciones de Russell & Norvig con un nombre nuevo. En un agente LLM es el texto que el modelo tiene a la vista en cada llamada. Por eso crece en cada vuelta, y por eso se termina llenando. La sección 6 vuelve sobre esto.

En el vocabulario de la lámina 1.5, la política es la función de agente escrita sobre el contexto, y el código que arma el contexto y llama al LLM es el programa.

Vocabulario, para decirlo en voz alta: el paper nunca usa la palabra "tool". Habla de acciones y de una API de Wikipedia con tres (search, lookup, finish). Lo que hoy se llama tool es una acción de A, y la sección 3 la define.

El paper dice que aprender esta política es difícil cuando el paso de c_t a a_t pide razonamiento complejo. Su respuesta, ReAct, abre la sección 4.

Fecha del paper: primera versión de arXiv en octubre de 2022, publicado en ICLR 2023.

---

## 2. Agente = LLM + planificación + tools

### Content

Lilian Weng (2023) describe al LLM como el cerebro del agente. Dos de los componentes que le suma organizan esta clase.

- **Planificación** Descomponer la tarea en subobjetivos, y reflexionar sobre acciones pasadas para corregirlas.
- **Uso de tools** Llamar APIs externas para obtener lo que no está en los pesos del modelo: información actual, ejecución de código, fuentes propietarias.

`Lilian Weng, jun-2023. Su tercer componente, la memoria, queda fuera de esta clase.`

### Sources

- `corpus/lilianweng-llm-powered-agents.web.md` — "LLM functions as the agent's brain", tres componentes Planning / Memory / Tool use y sus definiciones; ReAct y Reflexion clasificados bajo Planning → Self-Reflection.
- `corpus/anthropic-building-effective-agents.web.md` — el "augmented LLM" (retrieval, tools, memory) como bloque básico.

### Speaker notes

Es la descomposición más citada y conviene tenerla como mapa del resto de la clase. La sección 3 es la caja de tools. Las secciones 4 y 5 son la caja de planificación: Weng ubica ahí a ReAct y a Reflexion.

Anthropic dice algo parecido con otro nombre: su bloque básico es el "augmented LLM", un LLM con retrieval, tools y memoria.

El post es de junio de 2023. Sus ejemplos (AutoGPT, BabyAGI) son la primera ola de agentes; el marco de tres componentes sigue vigente.

---

## 3. Workflow o agente

### Content

Anthropic llama *agentic systems* a los dos y los separa por quién decide el camino.

| | Workflow | Agente |
|---|---|---|
| Quién decide el camino | El código, de antemano | El LLM, en cada paso |
| Definición | LLMs y tools orquestados por caminos de código predefinidos | LLMs que dirigen su propio proceso y el uso de tools |
| Conviene para | Tareas bien definidas que piden previsibilidad | Tareas que piden flexibilidad y decisiones del modelo |
| Patrones | Prompt chaining, routing, paralelización, orchestrator-workers, evaluator-optimizer | Un LLM que usa tools según el feedback del ambiente, en un loop |

`Anthropic, 2024 (revisado)`

### Sources

- `corpus/anthropic-building-effective-agents.web.md` — definiciones verbatim de workflows ("systems where LLMs and tools are orchestrated through predefined code paths") y agents ("systems where LLMs dynamically direct their own processes and tool usage"); los cinco patrones de workflow; "typically just LLMs using tools based on environmental feedback in a loop". Captura de una versión revisada del post del 19 dic 2024.

### Speaker notes

**Original:** "Agents … are typically just LLMs using tools based on environmental feedback in a loop." — [Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).

La pregunta que separa las dos columnas es una sola: ¿quién decide el próximo paso, el código o el modelo? En un workflow el LLM está embebido en pasos fijos. En un agente, el LLM elige qué tool usar, en qué orden y cuándo tiene suficiente para responder.

Un sistema real mezcla las dos columnas. Puede tener un routing determinista entre agentes que por dentro son autónomos.

Marcar que orchestrator-workers aparece acá como workflow. La lámina 5.9 lo retoma como quinto tipo de agente.

La captura es una versión revisada del post de diciembre de 2024; por eso la cita dice "2024 (revisado)".

---

## 4. Cuándo vale la pena un agente

### Content

Anthropic recomienda la solución más simple posible, y eso puede significar no construir un agente.

- **Varias tools en orden variable** La solución usa varias tools, en órdenes distintos según el caso.
- **Resultados que hay que interpretar** El paso siguiente depende de leer lo que devolvió el anterior.
- **Reglas fijas insuficientes** El espacio de posibilidades es demasiado grande o dinámico para cubrirlo con reglas.
- **Éxito verificable** Hay un criterio claro de éxito y feedback en cada paso, como los tests en un agente de código.

### Sources

- `corpus/AIG4B-Clase-6-Agent.pptx.md` — slide 15, "¿Cuándo vale la pena usar agentes?": múltiples herramientas en orden variable, interpretación dinámica de resultados, solución determinística insuficiente.
- `corpus/anthropic-building-effective-agents.web.md` — "finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all"; tareas con "clear success criteria, enable feedback loops"; "Agentic systems often trade latency and cost for better task performance"; coding agents verificables por tests.

### Speaker notes

**Original:** "finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all." — [Anthropic](https://www.anthropic.com/engineering/building-effective-agents).

El costo de un agente es latencia y plata a cambio de desempeño. Anthropic agrega un tercer riesgo: la autonomía permite que los errores se acumulen, así que recomienda probar en sandbox y poner condiciones de parada, como un máximo de iteraciones.

Para muchas aplicaciones, según el mismo post, alcanza con optimizar una sola llamada al LLM con retrieval y ejemplos en el prompt.

El cuarto criterio prepara Reflexion en la sección 5: un agente que se autocorrige necesita algo que le diga si salió bien.

Cierre de la sección 2. Tiempo acumulado: unos 22 minutos.

---

# 3. Los agentes tienen tools

**Goal of this section:** Fijar qué es una tool como concepto, independiente del protocolo que la transporte: una función descripta en el contexto que el LLM pide y el programa ejecuta. Al salir, la sala puede escribir una tool, sabe cómo falla un agente que las usa y qué principios hacen buena a una tool. MCP queda fuera de la sección; la clase de RAG y MCP ya lo cubrió.

---

## 1. Qué es una tool

### Content

Una tool es una función que el agente puede pedir. Su nombre, su descripción y sus parámetros están en el contexto; el LLM decide cuándo llamarla y el programa la ejecuta.

![El LLM pide la tool y el programa la ejecuta](images/s3-1-1-llm-pide-programa-ejecuta.png)
<!-- ascii-source:
  contexto: instrucciones + descripción de cada tool
                        |
                        v
                +---------------+
                |      LLM      |
                +---------------+
                  |           ^
  1. pide la tool |           | 3. el resultado
  con nombre y    |           |    vuelve al
  argumentos      v           |    contexto
                +---------------+
                |   programa    |
                |   (ejecuta)   |
                +---------------+
                        |
                        v
          2. API, base de datos, búsqueda
-->
<!-- ascii-note:
intent: separar quien decide (el LLM) de quien ejecuta (el programa); el LLM solo emite el pedido.
emphasize: la caja programa (ejecuta) en rojo, porque es la que la sala suele olvidar; las tres flechas numeradas.
labels: contexto, LLM, programa (ejecuta), pasos 1-3.
-->

### Sources

- `corpus/AIG4B-Clase-6-Agent.pptx.md` — slide 22: tools "descriptas en el contexto. El agente decide cuándo y cómo invocarlas".
- `corpus/langchain-planning-agents.web.md` — loop genérico: el LLM propone la acción (texto para el usuario o para una función), "your code" la ejecuta, el LLM observa el resultado.
- `corpus/medium-react-langgraph-agent.web.md` — el docstring de la función decorada con `@tool` es la descripción que recibe el modelo.

### Speaker notes

La aclaración que más ordena la sección: el LLM no ejecuta nada. Genera un pedido estructurado (nombre de la tool y argumentos), y es el programa que lo rodea el que llama a la API, corre la consulta o lee el archivo. El resultado vuelve como texto al contexto, y ahí el LLM decide de nuevo.

Por eso la descripción importa tanto: es lo único que el modelo sabe de la tool. Una tool mal descripta es una tool que el modelo usa mal o no usa.

La conexión con la sección 2: la tool es el actuador del agente LLM, y su resultado es la observación.

Si alguien pregunta por MCP: es una forma estándar de exponer tools y se vio en la clase de RAG y MCP. Lo que sigue vale para cualquier tool, venga o no de un servidor MCP.

---

## 2. Un contrato con un sistema no determinístico

### Content

> "tools are a new kind of software which reflects a contract between deterministic systems and non-deterministic agents"
> — Anthropic, *Writing effective tools for agents*, sep-2025

Ante la pregunta "¿Llevo paraguas hoy?", un agente puede llamar a la tool del clima, contestar con lo que sabe o pedir una aclaración. También puede alucinar o usar mal la tool.

### Sources

- `corpus/anthropic-writing-tools-for-agents.web.md` — cita verbatim del contrato; ejemplo del paraguas; deterministic vs. non-deterministic systems. Publicado el 11 sep 2025.

### Speaker notes

Una función tradicional es un contrato entre dos sistemas determinísticos: misma entrada, misma salida, y quien la llama sabe cuándo llamarla. Con un agente, el que llama es no determinístico. Puede llamarla cuando no corresponde, no llamarla cuando sí, o pasarle argumentos que un programador nunca pasaría.

La conclusión de Anthropic es de diseño: una tool se escribe pensando en un agente que la llama, con otros criterios que una API para desarrolladores. Y agrega una observación que a la sala le va a resultar útil: las tools más cómodas para un agente suelen ser también las más fáciles de entender para una persona.

---

## 3. Una tool en código

### Content

El docstring es la descripción que lee el modelo; `bind_tools` le pasa al modelo el esquema de cada tool.

```python
from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """Evaluates a math expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

@tool
def search_wikipedia(query: str) -> str:
    """Simulates a Wikipedia lookup."""
    import wikipedia
    return wikipedia.summary(query, sentences=2)

tools = [calculator, search_wikipedia]
model = ChatOpenAI(model="gpt-4o-mini").bind_tools(tools)
```

### Sources

- `corpus/medium-react-langgraph-agent.web.md` — Step 2 y Step 3 del walkthrough, verbatim (una copia de cada bloque duplicado). El registro marca dos defectos: `calculator` ejecuta `eval()` sobre un string generado por el modelo, y el docstring de `search_wikipedia` dice "Simulates" aunque llama a la biblioteca real.

### Speaker notes

Leer el código como lo lee el modelo: lo único que ve de cada tool es el nombre, los parámetros con sus tipos y el docstring. El cuerpo de la función no le llega nunca.

Dos defectos del ejemplo que sirven para enseñar. Primero, `calculator` corre `eval()` sobre un texto que escribió el modelo: eso ejecuta código arbitrario. Sirve para una demo y es inaceptable en producción. Segundo, el docstring de `search_wikipedia` dice que simula una búsqueda y la función llama a la biblioteca real de Wikipedia. Para el modelo, la descripción es la verdad; una descripción que miente produce un agente que se equivoca.

El ejemplo es de un tutorial en Medium (julio de 2025) sobre LangGraph. La lámina 4.6 muestra el grafo que convierte estas tools en un agente ReAct.

---

## 4. Cómo falla un agente con tools

### Content

Anthropic identifica cuatro fallas típicas al evaluar agentes con tools.

- **Tool equivocada** El agente llama a una tool que no corresponde a la tarea.
- **Parámetros equivocados** Elige bien la tool y la llama con argumentos incorrectos.
- **Pocas llamadas** Responde antes de juntar la información que hacía falta.
- **Resultado mal leído** Procesa de forma incorrecta lo que la tool devolvió.

### Sources

- `corpus/anthropic-writing-tools-for-agents.web.md` — modos de falla: "call the wrong tools, call the right tools with the wrong parameters, call too few tools, process responses incorrectly"; métricas más allá de la accuracy.

### Speaker notes

Además de si la tarea salió bien, Anthropic recomienda medir el tiempo por llamada y por tarea, la cantidad de llamadas, el consumo de tokens y los errores de las tools. Esas métricas dicen cuál de las cuatro fallas está pasando.

Un caso del artículo que ilustra la segunda falla: el agente agregaba "2025" a cada consulta de una tool de búsqueda web y sesgaba los resultados. Lo arreglaron mejorando la descripción de la tool, sin tocar el modelo.

Otra recomendación concreta: las tareas de evaluación tienen que ser realistas y tener un resultado verificable. "Agendá una reunión con Jane la semana que viene" es una tarea débil; "agendá la reunión, adjuntá las notas y reservá una sala" obliga a encadenar tools.

---

## 5. Principios para diseñar tools

### Content

- **Pocas y consolidadas** Más tools no garantizan mejores resultados; una tool que resuelve la tarea entera evita encadenar varias. Ejemplo: `schedule_event` en lugar de `list_users`, `list_events` y `create_event`.
- **Nombres con espacio de nombres** Un prefijo por servicio o por recurso separa tools parecidas. Ejemplo: `asana_search` y `jira_search`.
- **Contexto con significado** Traducir identificadores a nombres reduce las alucinaciones. Ejemplo: devolver `name` en lugar de `uuid`.
- **Respuestas que cuidan tokens** Cada respuesta trae solo lo que el agente necesita. Ejemplo: `search_contacts` en lugar de `list_contacts`; en Slack, la respuesta concisa ocupó 72 tokens y la detallada, 206.
- **Descripciones para alguien nuevo** Cada descripción se escribe como para alguien que recién llega al equipo. Entra al contexto y orienta cuándo y cómo usar la tool.

`Anthropic, sep-2025`

### Sources

- `corpus/anthropic-writing-tools-for-agents.web.md` — principios (choose the right tools, namespacing, meaningful context, token efficiency, prompt-engineer descriptions); ejemplos de consolidación; `search_contacts` vs `list_contacts`; respuesta Slack 72 vs 206 tokens (≈ 0,35 = 72 / 206, verificado por el librarian); "More tools don't always lead to better outcomes".

### Speaker notes

El hilo común: el contexto de un agente es limitado y la memoria de la computadora es barata. Una tool que devuelve todo (`list_contacts`) llena el contexto con cosas que el agente no necesita; una que busca (`search_contacts`) devuelve lo justo.

Consolidar también resuelve un problema de decisión. Con tres tools separadas, el agente tiene que acertar el orden; con una que agenda, el orden queda en el código.

El dato de Slack, por si piden el detalle: la versión concisa omite `thread_ts`, `channel_id` y `user_id`, y ocupa cerca de un tercio de los tokens. Anthropic propone exponer un parámetro `response_format` para que el agente elija entre concisa y detallada.

Sobre las descripciones: según el mismo post, pequeños ajustes en la descripción de una tool producen mejoras grandes en las evaluaciones.

---

## 6. La interfaz agente-computadora

### Content

Anthropic propone invertir en la interfaz agente-computadora (ACI) tanto esfuerzo como en la interfaz humano-computadora (HCI).

- **Más tiempo en las tools que en el prompt** Para su agente de SWE-bench, Anthropic dedicó más tiempo a optimizar las tools que el prompt general.
- **Poka-yoke** Cambiar los argumentos para que equivocarse sea más difícil. Exigir rutas absolutas eliminó los errores del modelo con rutas relativas.

`Anthropic, 2024 (revisado)`

### Sources

- `corpus/anthropic-building-effective-agents.web.md` — ACI vs HCI; "spent more time optimizing our tools than the overall prompt"; Appendix 2: errores con rutas relativas, tool cambiada para exigir rutas absolutas, "the model used this method flawlessly"; poka-yoke.

### Speaker notes

El término viene de la manufactura japonesa: diseñar la pieza para que no se pueda montar mal. Aplicado a tools, es elegir parámetros que hagan difícil el error en vez de explicarle al modelo cómo no cometerlo.

El caso de las rutas: el modelo se equivocaba con rutas relativas después de moverse fuera del directorio raíz. Anthropic no agregó instrucciones; cambió la tool para que solo acepte rutas absolutas, y según el post el modelo la usó sin errores.

Un detalle de formato del mismo apéndice, útil para esta sala: escribir un diff exige saber cuántas líneas cambian antes de escribirlo, y escribir código dentro de JSON exige escapar comillas. Los dos formatos le cuestan más al modelo que el mismo código en markdown.

Cierre de la sección 3. Tiempo acumulado: unos 34 minutos.

---

# 4. ReAct

**Goal of this section:** Fijar las dos preguntas con las que se comparan los tipos de agente y recorrer el primero, ReAct: su definición con diagrama, una trayectoria del paper, el prompt y el código que la producen, el grafo en LangGraph y lo que mostraron sus resultados. ReAct es la base contra la que se comparan los otros cuatro tipos.

---

## 1. Dos preguntas para cada tipo

### Content

Todos los tipos repiten el loop de la lámina 3.1. Los cuatro primeros que recorre la clase se distinguen por dos preguntas.

1. **Cuándo se planifica** Nunca de antemano, al inicio o entre intentos completos.
2. **Cuántas veces vuelve a razonar el LLM** En cada paso, al replanificar o solo al final.

El quinto tipo, orquestador con workers, mueve otra variable: cómo se reparte el contexto entre varios loops.

### Sources

- `corpus/langchain-planning-agents.web.md` — loop genérico de un agente LLM ("Propose action", "Execute action", "Observe"), el mismo de la lámina 3.1.
- `corpus/anthropic-building-effective-agents.web.md` · `corpus/anthropic-multi-agent-research-system.web.md` — orchestrator-workers y subagentes con ventanas propias (quinto tipo, lámina 5.9).

### Speaker notes

El loop ya está dibujado en la lámina 3.1: el LLM pide, el programa ejecuta y el resultado vuelve al contexto. Esta lámina solo agrega el eje de comparación.

Pedirle a la sala que retenga las dos preguntas. La tabla de la lámina 5.11 se lee con ellas, y ahí están las respuestas de cada tipo.

El quinto tipo queda fuera de las dos preguntas a propósito: su variable es el eje de las secciones 6 a 9.

---

## 2. ReAct: pensar también es una acción

### Content

ReAct amplía el espacio de acciones con el lenguaje, `Â = A ∪ L`, e intercala pensamientos y acciones hasta tener lo necesario para responder.

- **Acción en A** Toca el ambiente, por ejemplo `search[entity]`, y vuelve una observación.
- **Pensamiento en L** No toca el ambiente ni produce observación. Agrega razonamiento al contexto: `c_{t+1} = (c_t, â_t)`.

![ReAct: la bifurcación entre pensar y actuar](images/s4-2-1-bifurcacion-pensar-actuar.png)
<!-- ascii-source:
                 π(â_t | c_t)
                       |
          +------------+-------------+
          |                          |
          v                          v
   â_t ∈ A  (acción)        â_t ∈ L  (pensamiento)
          |                          |
          v                          |
   +-------------+                   |
   |  AMBIENTE   |                   |
   +-------------+                   |
          |                          |
          v                          v
   hay observación            no hay observación
   c_{t+1} suma a_t           c_{t+1} = (c_t, â_t)
   y o_{t+1}
-->
<!-- ascii-note:
intent: la bifurcacion que define ReAct; una rama toca el ambiente y la otra solo escribe en el contexto.
emphasize: la rama del pensamiento (L) en rojo, que no pasa por el ambiente.
labels: pi, accion en A, pensamiento en L, AMBIENTE, c_{t+1}.
consistency: los cinco diagramas de tipos de agente (4.2, 5.1, 5.4, 5.7 y 5.9) comparten lienzo, tipografia y tratamiento de cajas; cambia solo la forma.
-->

### Sources

- `corpus/yao-2022-react.pdf.md` — Sección 2, verbatim: "we augment the agent's action space to Â = A ∪ L … a thought or a reasoning trace, does not affect the external environment, thus leading to no observation feedback … update the context c_{t+1} = (c_t, â_t)"; Sección 3.1, acciones `search[entity]`, `lookup[string]`, `finish[answer]`; trayectorias thought-action-observation ("dense thought") en razonamiento y pensamientos esparcidos en decisión (notas).
- `corpus/AIG4B-Clase-6-Agent.pptx.md` — slide 20: "ReAct es la arquitectura más simple y fundamental para agentes basados en LLMs"; ciclo Thought → Action → Observation hasta la respuesta final (notas).
- `corpus/langchain-planning-agents.web.md` — ReAct como "a great prototypical design" que elige una acción por paso.

### Speaker notes

La idea entera de ReAct entra en esta lámina. El modelo puede hacer algo en el mundo o escribir un razonamiento, y el razonamiento queda en el contexto para la próxima decisión. El paper lo resume en dos direcciones: razonar para actuar y actuar para razonar.

El deck del curso la presenta como la arquitectura más simple para agentes basados en LLM. Es la base contra la que se comparan los otros cuatro tipos.

Un matiz del paper: en tareas de razonamiento cada paso lleva su pensamiento ("dense thought"). En tareas de decisión con muchas acciones, el modelo escribe un pensamiento solo donde hace falta.

---

## 3. Una trayectoria ReAct

### Content

Pregunta de HotpotQA, un conjunto de preguntas multi-salto sobre Wikipedia: además del Apple Remote, ¿qué otro dispositivo controla el programa para el que se diseñó el Apple Remote?

```text
Thought 1: I need to search Apple Remote and find the program it was
           originally designed to interact with.
Act 1:     Search[Apple Remote]
Obs 1:     The Apple Remote is a remote control introduced in October 2005
           by Apple … originally designed to control the Front Row media
           center program …
Thought 2: … I need to search Front Row next and find what other device
           can control it.
Act 2:     Search[Front Row]
Obs 2:     Could not find [Front Row]. Similar: ['Front Row Seat to Earth',
           'Front Row Motorsports', 'Front Row (software)', …]
Thought 3: Front Row is not found. I need to search Front Row (software).
Act 3:     Search[Front Row (software)]
Obs 3:     Front Row is a discontinued media center software …
Thought 4: Front Row (software) is controlled by an Apple Remote or the
           keyboard function keys. So the answer is keyboard function keys.
Act 4:     Finish[keyboard function keys]
```

### Sources

- `corpus/yao-2022-react.pdf.md` — Figure 1 (1d), texto decodificado verbatim; HotpotQA descripto como "multi-hop QA over ≥2 Wikipedia passages"; Thought 2 recortado con "…" respecto del original. Comparación con (1a) Standard, (1b) CoT y (1c) Act-only en la misma figura. Sección 2: tipos de pensamiento útiles (descomponer la tarea, extraer lo importante de una observación, seguir el progreso, manejar excepciones, ajustar el plan) (notas).

### Speaker notes

Leer la trayectoria en voz alta y marcar qué hace cada pensamiento, con los usos que el paper le da a pensar. El primero descompone la pregunta. El segundo extrae lo importante de la observación. El tercero maneja una excepción: la búsqueda falló y el agente reformula. El cuarto sintetiza la respuesta.

La misma pregunta en la misma figura del paper, con los otros métodos: el modelo sin razonamiento ni acciones responde "iPod" (mal). Con chain-of-thought solo, alucina que Apple Remote controla Apple TV y responde "iPhone, iPad, iPod Touch" (mal). Con acciones sin pensamientos, busca lo mismo que ReAct y termina respondiendo "yes" (mal). Solo ReAct llega a "keyboard function keys".

Ese último caso es el más instructivo: las búsquedas eran correctas y el agente igual falló, porque sin pensamientos no pudo razonar sobre lo que había observado.

Las dos láminas siguientes muestran el prompt y el código que producen esta trayectoria.

---

## 4. Las tools y la instrucción

### Content

La trayectoria anterior no usa un system prompt. El modelo completa un solo texto, y ese texto abre con esta instrucción, que define las tres acciones.

```text
Solve a question answering task with interleaving Thought, Action,
Observation steps. Thought can reason about the current situation,
and Action can be three types:
(1) Search[entity], which searches the exact entity on Wikipedia and
    returns the first paragraph if it exists. If not, it will return
    some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing
    keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
Here are some examples.
```

### Sources

- `corpus/react-repo-hotpotqa-prompt.md.md` — variable `instruction` de `hotpotqa.ipynb`, repositorio github.com/ysymyth/ReAct, verbatim; las líneas se partieron por ancho. La captura dice que no hay "system prompt" en el sentido de una API de chat y que la instrucción no está en el PDF del paper (verificado por el librarian: 0 apariciones de "Here are some examples" en el registro del paper). Segundo ejemplo de `webthink_simple6` (Milhouse, con `Lookup[named after]`) solo en notas. El registro deja abierto que el repositorio sea el código oficial: el paper apunta a react-lm.github.io.
- `corpus/yao-2022-react.pdf.md` — Sección 3.1: espacio de acciones search, lookup y finish sobre una API de Wikipedia; 6 trayectorias de HotpotQA elegidas al azar del set de entrenamiento y escritas a mano ("more examples do not improve performance"); Apéndice C.1 ("the prompt contains 6 such questions"); Table 5: corridas con GPT-3 text-davinci-002, cuyo código el paper ubica en react-lm.github.io.

### Speaker notes

Ninguna API de chat interviene. PaLM-540B y text-davinci-002 son modelos de completado: reciben un texto y lo continúan, sin roles de sistema, usuario y asistente. El paper corrió sobre todo con PaLM-540B. El notebook público usa text-davinci-002 por la API de completado, con temperatura 0 y hasta 100 tokens por paso.

La instrucción describe tres tools en su forma más cruda: nombre y efecto en una línea de texto. El pedido de la acción también es texto (`Search[Front Row]`), y el código lo parsea. El Obs 2 de la lámina anterior es lo que la instrucción promete cuando la entidad no existe.

Lookup aparece en el segundo ejemplo del prompt, sobre Milhouse, el personaje de Los Simpson: `Lookup[named after]` encuentra que le pusieron el nombre por Richard Nixon.

---

## 5. El prompt completo y el corte

### Content

Cada paso es una llamada de completado. El modelo escribe Thought y Action; la generación se detiene antes de Observation, y el código ejecuta la acción y escribe el resultado.

![El prompt completo de ReAct y el punto de corte](images/s4-5-1-prompt-completo-corte.png)
<!-- ascii-source:
 +------------------------------------------------------+
 | Solve a question answering task ... three types:     |  instrucción
 | (1) Search[entity] (2) Lookup[keyword] (3) Finish    |  (3 tools)
 +------------------------------------------------------+
 | Question: ... Milhouse, who Matt Groening named      |  6 ejemplos
 |   after who?                                         |  escritos
 | Thought 1 / Action 1 / Observation 1 ...             |  a mano
 | Action 3: Finish[Richard Nixon]          (y 5 más)   |
 +------------------------------------------------------+
 | Question: Aside from the Apple Remote, what other    |  pregunta
 |   device can control the program ...?                |  nueva
 | Thought 1:                                           |
 +------------------------------------------------------+
                           |
                           |  el LLM continúa el texto
                           v
     Thought 1: I need to search Apple Remote ...
     Action 1: Search[Apple Remote]
                           |
                           |  se detiene en "Observation 1:"
                           v
     el código ejecuta search[Apple Remote] en Wikipedia
     y agrega "Observation 1: The Apple Remote is ..."
                           |
                           |  nueva llamada con "Thought 2:"
                           v
          sigue hasta Finish[...] o 7 pasos
-->
<!-- ascii-note:
intent: un solo texto de completado armado con tres bloques (instruccion, ejemplos, pregunta); el modelo escribe Thought y Action, la generacion corta en "Observation 1:" y el codigo pega la observacion antes de la llamada siguiente.
emphasize: el corte "se detiene en Observation 1:" en rojo; los tres bloques del prompt apilados como un unico texto.
labels: instruccion (3 tools), 6 ejemplos escritos a mano, pregunta nueva, Thought 1, Action 1, Observation 1, Finish o 7 pasos.
-->

### Sources

- `corpus/react-repo-hotpotqa-prompt.md.md` — celda de `hotpotqa.ipynb`, verbatim: `webthink_prompt = instruction + webthink_examples`; `prompt += question + "\n"`; `llm(prompt + f"Thought {i}:", stop=[f"\nObservation {i}:"])`; `step(env, action[0].lower() + action[1:])`; `for i in range(1, 8)` (a lo sumo 7 pasos) y `step(env, "finish[]")` si no terminó; segunda llamada y `n_badcalls` cuando falta "Action i:". Extracto suplementario (celda 1): `text-davinci-002` por `openai.Completion.create`, `temperature=0`, `max_tokens=100`. El ejemplo de Milhouse, recortado con "...", es el segundo de `webthink_simple6`. El registro deja abierto el texto exacto que devuelve `env.reset()`; el prefijo "Question:" de la pregunta nueva sigue el formato de los ejemplos.
- `corpus/yao-2022-react.pdf.md` — Figure 1 (1d): la pregunta del Apple Remote, verbatim, y los Thought 1, Act 1 y Obs 1, recortados con "...".

### Speaker notes

Es el loop de ReAct de la lámina 4.2 en código de 2022. El notebook llama al modelo con el prompt más "Thought 1:" y le pasa como stop "\nObservation 1:". El modelo escribe el pensamiento y la acción, y la API corta ahí. El código ejecuta la acción contra un ambiente de Wikipedia, pega la observación al final del prompt y repite. Termina en Finish o a los 7 pasos.

Sin el stop, el modelo seguiría el formato de los ejemplos y escribiría él mismo la observación.

Rótulos: la figura del paper abrevia Act y Obs, y su sección 3.1 escribe las acciones en minúscula (`search[entity]`). El notebook usa Action y Observation, y el código pasa la primera letra de la acción a minúscula antes de ejecutarla.

El prompt crece en cada vuelta: es el contexto c_t de la lámina 2.1.

---

## 6. ReAct en LangGraph

### Content

Dos nodos y una arista condicional: si el último mensaje del LLM no pide tools, el grafo termina; si pide, las ejecuta y vuelve al LLM.

```python
def is_done(state: AgentState):
    messages = state['messages']
    last_message = messages[-1]
    if not last_message.tool_calls:
        return "end"
    return "continue"

builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)
tool_node = ToolNode(tools=tools)
builder.add_node("tools", tool_node)
builder.set_entry_point("agent")
builder.add_conditional_edges(
    "agent",
    is_done,
    {"end": END, "continue": "tools"}
)
builder.add_edge("tools", "agent")
agent = builder.compile()
```

### Sources

- `corpus/medium-react-langgraph-agent.web.md` — Step 5, "Graph with Loops", verbatim salvo dos cambios: se quitó la anotación `-> bool` de `is_done` (el registro marca que devuelve strings) y el docstring. El registro marca que faltan imports (`TypedDict`, `ToolNode`, etc.) y que el código completo está en el repositorio del autor.
- `samples/react-langgraph/react_agent.py` — ejemplo del repositorio de la materia, no es un registro del corpus; solo en notas.

### Speaker notes

El `agent_node` llama al modelo con las tools de la lámina 3.3 ya enlazadas. El `ToolNode` es un nodo prearmado de LangGraph que ejecuta las llamadas a tools del último mensaje.

El loop de ReAct es la arista `tools → agent`: después de ejecutar, siempre se vuelve al LLM. La condición de salida la decide el modelo, cuando responde sin pedir tools.

Dos cambios respecto del artículo, por honestidad: el original anota `is_done` como `-> bool` y devuelve strings, y no importa varias de las clases que usa. Si alguien lo copia tal cual, no corre.

Contraste con las dos láminas anteriores. El modelo de chat recibe la descripción de cada tool como un esquema aparte (`bind_tools`) y devuelve la llamada como un mensaje estructurado (`tool_calls`). Nadie parsea texto ni corta con un stop, y el loop es el mismo.

El ejemplo `samples/react-langgraph/` del repositorio de la materia corre la misma pregunta del Apple Remote con LangGraph y dos tools, `buscar_wikipedia` y `buscar_en_pagina`, que hacen el papel de Search y Lookup. Ese ejemplo sí tiene system prompt: le pide al modelo un pensamiento antes de cada tool.

Falta la condición de parada de la lámina 2.4, un máximo de iteraciones además de la decisión del modelo. Es un buen ejercicio para la práctica.

---

## 7. Qué mostró el paper, y dónde falla

<!-- template: stat -->

### Content

Resultados del paper (2022–23, PaLM-540B con pocos ejemplos en el prompt).

- **0% contra 56%** de los fallos se deben a alucinación: ReAct contra chain-of-thought, en HotpotQA.
- **47%** de los fallos de ReAct son errores de razonamiento, incluido un loop que repite pensamientos y acciones.
- **71% contra 45%** de éxito en ALFWorld, tareas domésticas en un entorno de texto: ReAct contra el mismo agente sin pensamientos, mejor de 6 corridas.

### Sources

- `corpus/yao-2022-react.pdf.md` — ALFWorld descripto como "text-based household game"; Table 2 (HotpotQA, modos de falla: hallucination 0% ReAct vs 56% CoT; reasoning error 47% ReAct; search result error 23%); Table 3 (ALFWorld, ReAct best of 6 = 71, Act best of 6 = 45). Modelo: PaLM-540B por few-shot prompting.

### Speaker notes

Fechar los números en voz alta: son de 2022–23, con PaLM-540B, un modelo que no es público. Sirven para entender el mecanismo, no como benchmark actual.

La primera cifra es la que justifica las tools: cuando el agente busca, deja de inventar hechos. La segunda es el costo: ReAct falla más por razonamiento, y su falla característica es un loop que repite el mismo pensamiento y la misma acción. Otro 23% de sus fallos viene de búsquedas que no devolvieron nada útil.

Un dato que la sala puede preguntar: en HotpotQA, chain-of-thought solo saca un poco más que ReAct (29,4 contra 27,4 de exact match). La mejor combinación del paper usa las dos: ReAct cuando hace falta buscar y chain-of-thought con votación cuando el modelo ya sabe.

La crítica de LangChain lleva al tipo siguiente: ReAct hace una llamada al LLM por cada tool y planifica un subproblema por vez, sin pensar la tarea entera.

Cierre de la sección 4. Tiempo acumulado: unos 49 minutos.

---

# 5. Otros cuatro tipos

**Goal of this section:** Recorrer de a uno, en orden, los otros cuatro tipos de agente que más se comparan: Plan-and-Execute, Reflexion, ReWOO y multiagente con orquestador y workers. Cada tipo tiene su lámina de definición con diagrama y después una de ejemplo. La sección cierra con la tabla que compara los cinco. Los tres primeros responden distinto a las dos preguntas de la lámina 4.1; el orquestador con workers reparte el contexto y lleva a las secciones 6 a 9.

---

## 1. Plan-and-Execute: planificar primero

### Content

Un planner escribe el plan completo al inicio. Un executor resuelve cada paso con sus tools, y un re-planner decide si termina o planifica de nuevo.

![Plan-and-Execute: planner, executor y re-planner](images/s5-1-1-plan-and-execute.png)
<!-- ascii-source:
  Pedido
    |
    v
 +----------+   lista de pasos   +--------------------+
 | Planner  | -----------------&gt; | Executor           |
 |  (LLM)   |   1. ...           | un paso a la vez,  |
 +----------+   2. ...           | con sus tools      |
      ^         3. ...           +--------------------+
      |                                    |
      |                                    v resultados
      |                          +--------------------+
      +------ replanificar ----- | Re-planner (LLM)   |
                                 | ¿terminó?          |
                                 +--------------------+
                                           |
                                           v  sí
                                 Respuesta al usuario
-->
<!-- ascii-note:
intent: separar el planner de la ejecucion; el LLM grande planifica al inicio y al replanificar, no despues de cada accion.
emphasize: la caja Planner en rojo; la flecha de replanificar que cierra el lazo largo.
labels: Pedido, Planner (LLM), lista de pasos, Executor, Re-planner (LLM), Respuesta al usuario.
consistency: mismo lienzo y tratamiento de cajas que el diagrama de ReAct (4.2).
-->

### Sources

- `corpus/langchain-planning-agents.web.md` — arquitectura Plan-and-Execute: planner, executor(s), re-planning prompt; basada en Plan-and-Solve (Wang et al.) y BabyAGI. Post de LangChain, 13 feb 2024.

### Speaker notes

La diferencia con ReAct está en el momento del razonamiento. ReAct piensa antes de cada acción; Plan-and-Execute piensa todo al inicio, ejecuta, y vuelve a pensar solo al replanificar.

En el diagrama de LangChain, cada executor es un agente de una sola tarea que hace su propio loop con tools. O sea que adentro de Plan-and-Execute hay pequeños ReAct, cada uno con un paso del plan.

La idea viene de dos fuentes que el post cita: el paper Plan-and-Solve de Wang et al. y el proyecto BabyAGI de Yohei Nakajima.

---

## 2. Un plan para la misma pregunta

### Content

La pregunta de la lámina 4.3, resuelta con Plan-and-Execute. La cátedra armó este plan para comparar los dos tipos.

```text
Planner:     1. Buscar Apple Remote y anotar el programa para el que se diseñó.
             2. Buscar ese programa y anotar qué otros dispositivos lo controlan.

Executor 1:  Search[Apple Remote]
             -> Front Row media center program
Executor 2:  Search[Front Row]  -> no encontrado
             Search[Front Row (software)]
             -> controlled by an Apple Remote or the keyboard function keys

Re-planner:  ¿terminó? Sí. Respuesta: keyboard function keys
```

### Sources

- Construcción ilustrativa de la cátedra: no proviene de ninguna fuente ni de una corrida real de un sistema Plan-and-Execute.
- `corpus/yao-2022-react.pdf.md` — Figure 1 (1d): la pregunta, las búsquedas y los resultados, tomados de la trayectoria ReAct de la lámina 4.3. El resultado del executor 1 sale de Obs 1; el del executor 2 sale de Thought 4, porque el Obs 3 de la figura está recortado en la fuente.
- `corpus/langchain-planning-agents.web.md` — los roles planner, executor y re-planner, y el executor como agente de una sola tarea con su propio loop.

### Speaker notes

Aclarar de entrada que este plan lo armó la cátedra. El corpus no tiene una traza publicada de Plan-and-Execute, y usar la misma pregunta que en ReAct permite comparar las dos formas sobre el mismo caso.

Señalar dónde quedó el razonamiento. El planner piensa una vez, al principio, y escribe dos pasos. La búsqueda fallida de Front Row la resuelve el executor del paso 2 adentro de su propio loop, sin volver al planner. El re-planner mira los resultados una vez y decide que alcanza.

En la trayectoria ReAct de la lámina 4.3, el mismo LLM escribió un pensamiento antes de cada una de las cuatro acciones. Acá el LLM que planifica interviene dos veces: al armar el plan y al decidir que terminó. Es el ahorro que LangChain promete en la lámina siguiente.

---

## 3. Qué gana y qué cuesta planificar

<!-- template: pros-cons -->

### Content

### Ventajas, según LangChain

- **Más rápido** El LLM grande no se consulta después de cada acción.
- **Más barato** Los pasos pueden ir a modelos más chicos; el grande solo planifica, replanifica y responde.
- **Mejor resultado** El planner tiene que pensar todos los pasos antes de empezar.

### Límites

- **Ejecución en serie** Las tools se siguen llamando de a una.
- **Un LLM por paso** Cada paso pasa por un executor, y no hay variables que conecten el resultado de un paso con el siguiente.

### Sources

- `corpus/langchain-planning-agents.web.md` — "Faster", "Cheaper", "Better" como mejoras sobre ReAct; limitaciones del Plan-and-Execute básico (serial tool calling, an LLM per task, no variable assignment). El registro marca que las tres ventajas se afirman en el post sin benchmark.

### Speaker notes

Decir con qué peso llegan las ventajas: el post de LangChain las afirma y no las mide. Son razonables por construcción (menos llamadas al modelo grande), pero no hay un número detrás.

El segundo límite prepara ReWOO, que agrega lo que falta: variables que conectan los pasos, para que el plan se ejecute sin volver al LLM.

Cuándo conviene, según la tabla del final: tareas largas y predecibles, donde se pueden ahorrar llamadas al LLM.

---

## 4. Reflexion: intentar, evaluar, reflexionar

### Content

Reflexion ejecuta, evalúa el resultado y, si falló, escribe una crítica en lenguaje natural que guarda como memoria para el intento siguiente. No toca los pesos del modelo.

![Reflexion: actor, evaluador y auto-reflexión entre intentos](images/s5-4-1-lazo-reflexion.png)
<!-- ascii-source:
                +----------------------------+
  intento k --&gt; | Actor (LLM, tipo ReAct)    | <------+
                +----------------------------+        |
                              |                       |
                              v trayectoria           |
                +----------------------------+        |
                | Evaluator: ¿pasó?          |        |
                | (tests, heurística o LLM)  |        |
                +----------------------------+        |
                   |                     |            |
                sí v                  no v            |
            Respuesta      +-----------------------+  |
                           | Self-Reflection (LLM) |  |
                           | escribe la crítica    |  |
                           +-----------------------+  |
                                       |              |
                                       v              |
                           +-----------------------+  |
                           | memoria: 1 a 3        |--+
                           | reflexiones previas   | intento k+1
                           +-----------------------+
-->
<!-- ascii-note:
intent: el lazo largo de Reflexion, entre intentos completos; tres roles LLM distintos (Actor, Evaluator, Self-Reflection) y una memoria de reflexiones.
emphasize: la caja Self-Reflection en rojo; la flecha de la memoria que vuelve al Actor para el intento siguiente.
labels: Actor, Evaluator, Self-Reflection, memoria, intento k / k+1, Respuesta.
consistency: mismo lienzo y tratamiento de cajas que 4.2 y 5.1.
-->

### Sources

- `corpus/shinn-2023-reflexion.pdf.md` — Sección 3, verbatim: Actor (CoT o ReAct), Evaluator, Self-Reflection; memoria de corto plazo (trayectoria) y largo plazo (reflexiones, acotada a Ω, "usually set to 1-3"); refuerzo "not by updating weights, but instead through linguistic feedback". Algorithm 1: el diagrama sigue la condición que describe la prosa (repetir mientras no pase y queden intentos); el registro marca que el pseudocódigo dice "or" donde corresponde "and".

### Speaker notes

Reflexion es el primer tipo con más de un rol de LLM. El Actor produce la trayectoria, y en los experimentos de decisión y de preguntas es un agente ReAct. El Evaluator decide si salió bien. El Self-Reflection convierte ese veredicto en una crítica escrita. Son tres llamadas al LLM con tres trabajos distintos, y ese reparto anticipa el último tipo de la sección. El Evaluator hace de crítico, como en el agente que aprende de la lámina 1.6.

Los autores lo llaman refuerzo verbal: en lugar de actualizar pesos como en reinforcement learning, el agente guarda en su contexto una frase que le dice qué cambiar. El paper lo describe como un gradiente semántico.

Un detalle para quien lea el paper: el pseudocódigo del Algorithm 1 dice "while not pass or t < max trials", que como está escrito nunca terminaría bien. La prosa aclara que el loop sigue hasta que el Evaluator aprueba, con un máximo de intentos.

---

## 5. Una reflexión, en código

### Content

Tarea de programación: decidir si dos strings de paréntesis se pueden concatenar en un orden balanceado.

```text
(b) Trayectoria:  def match_parens(lst):
                      if s1.count('(') + s2.count('(') ==
                         s1.count(')') + s2.count(')'): [...]
                      return 'No'
(c) Evaluación:   Self-generated unit tests fail: assert match_parens(...)
(d) Reflexión:    [...] wrong because it only checks if the total count
                  of open and close parentheses is equal [...] order of
                  the parentheses [...]
(e) Nuevo intento: [...]
                      return 'Yes' if check(S1) or check(S2) else 'No'
```

### Sources

- `corpus/shinn-2023-reflexion.pdf.md` — Figure 1, fila "2. Programming", texto decodificado verbatim (los "[...]" son del original). La condición del `if` se partió en dos líneas por ancho.

### Speaker notes

El ejemplo muestra las cuatro piezas con un caso que la sala reconoce. El Actor escribe una solución que solo cuenta paréntesis. El Evaluator son tests unitarios que el mismo agente generó, y fallan. La reflexión nombra el error en lenguaje natural: contar no alcanza, importa el orden. El intento siguiente arranca con esa frase en el contexto.

Que los tests los genere el agente es parte del método. Por eso el paper puede reportar pass@1: la solución se entrega una sola vez y nunca vio los tests ocultos del benchmark.

La misma figura del paper tiene dos ejemplos más, uno de decisión en ALFWorld (el agente creyó que la sartén estaba en una hornalla equivocada) y uno de preguntas (supuso que dos escritores compartían varias profesiones).

---

## 6. Qué mostró Reflexion

<!-- template: stat -->

### Content

Resultados del paper (2023). HumanEval mide si el modelo escribe una función correcta a partir de su descripción; pass@1 es el acierto con la primera solución entregada.

- **91,0% contra 80,1%** pass@1 en HumanEval Python: Reflexion contra GPT-4, el mejor resultado publicado en ese momento.
- **130 de 134** tareas de ALFWorld resueltas con ReAct + Reflexion, en 12 intentos.
- **52% contra 60%** pass@1 en Rust al quitar los tests autogenerados: sin tests que evalúen el intento, la reflexión queda por debajo del modelo base.

### Sources

- `corpus/shinn-2023-reflexion.pdf.md` — pass@1 definido como "accuracy of a single submitted solution"; HumanEval: "measure function body generation accuracy given natural language descriptions"; Table 1 (HumanEval PY: SOTA GPT-4 80,1, Reflexion 91,0); Sección 4.1 (130/134 tareas de ALFWorld, 12 intentos); Table 3 (HumanEval Rust, 50 problemas más difíciles, GPT-4: base 0,60; sin generación de tests 0,52; sin self-reflection 0,60; Reflexion completo 0,68); Table 4 (starchat-beta 0,26 → 0,26). Las fracciones de pass@1 se muestran como porcentaje (0,52 = 52%) para usar el mismo formato que la primera cifra.

### Speaker notes

Fechar las cifras: son de 2023 y el "estado del arte" de la primera es el de ese momento. No son benchmarks actuales.

La tercera cifra es la que justifica la fila de la tabla final ("cuando hay un criterio claro de éxito"). En la ablación de Rust, Reflexion completo llega a 68%. Sin tests autogenerados cae a 52%, por debajo del modelo base (60%). Sin la reflexión, se queda en 60%. Las dos piezas hacen falta, y la que más pesa es tener algo que diga si salió bien.

Un límite que el paper reporta: con un modelo chico (starchat-beta), Reflexion no mejora nada, 26% antes y 26% después. La autocorrección aparece en modelos más capaces. Y en WebShop, una tarea que pide explorar mucho, Reflexion no logró mejorar y los autores cortaron después de 4 intentos.

---

## 7. ReWOO: planificar con variables

### Content

ReWOO (Reasoning WithOut Observations) escribe el plan completo con variables y ejecuta todas las tools sin volver a razonar entre medio.

![ReWOO: planner, worker y solver en tubería](images/s5-7-1-tuberia-rewoo.png)
<!-- ascii-source:
  Pedido
    |
    v
 +----------------------------------------------+
 | Planner (LLM): escribe todo el plan          |
 |   Plan: ...   E1 = Search[...]               |
 |   Plan: ...   E2 = LLM[... #E1]              |
 |   Plan: ...   E3 = Search[... #E2]           |
 +----------------------------------------------+
    |
    v
 +----------------------------------------------+
 | Worker: ejecuta E1, E2, E3 en orden y        |
 | reemplaza cada #E por su resultado           |
 +----------------------------------------------+
    |
    v
 +----------------------------------------------+
 | Solver (LLM): plan + evidencias -> respuesta |
 +----------------------------------------------+
-->
<!-- ascii-note:
intent: tuberia sin lazo; el LLM razona al principio (Planner) y al final (Solver), y el Worker ejecuta sin consultarlo.
emphasize: las variables #E1 y #E2 dentro del plan, que conectan un paso con el siguiente; la ausencia de flecha de vuelta al Planner.
labels: Pedido, Planner (LLM), Worker, Solver (LLM), E1-E3.
consistency: mismo lienzo y tratamiento de cajas que 4.2, 5.1 y 5.4; aca la forma es una tuberia porque no hay lazo.
-->

### Sources

- `corpus/langchain-planning-agents.web.md` — ReWOO (Xu et al., arXiv 2305.18323): planner con líneas "Plan" y "E#" que referencian resultados previos (`#E2`), worker que completa las variables, solver que integra; "the task list executes without re-planning"; límite: ejecución secuencial.

### Speaker notes

La diferencia con Plan-and-Execute es la variable. En Plan-and-Execute cada paso pasa por un executor con su propio LLM; en ReWOO el plan ya dice de dónde sale cada dato (`#E1`), así que el worker solo reemplaza y ejecuta. El LLM razona dos veces: al planificar y al resolver.

El costo de esa eficiencia: si una búsqueda devuelve algo inesperado, nadie replanifica. Por eso el nombre, razonar sin observaciones.

Mención: LLMCompiler (Kim et al.) lleva la idea un paso más allá. El planner emite un grafo de tareas con dependencias (un DAG) y un scheduler ejecuta cada tarea apenas sus dependencias están listas, en paralelo. LangChain dice que el paper reporta una aceleración de 3,6×; no está verificado en el corpus, así que conviene decirlo como cifra del paper y no como medición propia.

---

## 8. Un plan ReWOO

### Content

Pedido: "What are the stats for the quarterbacks of the super bowl contenders this year".

```text
Plan: I need to know the teams playing in the superbowl this year
E1: Search[Who is competing in the superbowl?]
Plan: I need to know the quarterbacks for each team
E2: LLM[Quarterback for the first team of #E1]
Plan: I need to know the quarterbacks for each team
E3: LLM[Quarter back for the second team of #E1]
Plan: I need to look up stats for the first quarterback
E4: Search[Stats for #E2]
Plan: I need to look up stats for the second quarterback
E5: Search[Stats for #E3]
```

### Sources

- `corpus/langchain-planning-agents.web.md` — plan ReWOO verbatim del post (incluido el typo "Quarter back" en E3).

### Speaker notes

Señalar dos cosas en el plan. Primero, `#E1`, `#E2` y `#E3` son las variables: E4 no sabe todavía quién es el quarterback, pero el plan ya dice que lo va a sacar de E2. Segundo, algunos pasos llaman a un LLM como si fuera una tool (`LLM[...]`). El worker lo trata como cualquier otra tool.

El plan entero sale de una sola llamada al planner. Después vienen cinco ejecuciones y una llamada final al solver. Con ReAct, la misma tarea habría pasado por el LLM antes de cada una de las cinco acciones.

Cuándo conviene, según la tabla: cuando el objetivo es bajar costo y latencia, y el plan se puede escribir completo de antemano.

---

## 9. Multiagente: orquestador y workers

### Content

Un orquestador descompone la tarea en tiempo de ejecución, delega cada subtarea en un worker y sintetiza los resultados. Anthropic lo cuenta entre los workflows. Cuando cada worker es un agente con su propio loop de tools, el worker es un subagente, y el conjunto es la forma básica de un sistema multiagente, que define la sección 6.

![Orquestador que reparte subtareas a workers en paralelo](images/s5-9-1-orquestador-workers.png)
<!-- ascii-source:
                    Pedido
                       |
                       v
            +----------------------+
            |  Orquestador (LLM)   |
            |  decide subtareas    |
            +----------------------+
               |         |        |
               v         v        v
         +--------+ +--------+ +--------+
         |Worker 1| |Worker 2| |Worker 3|
         +--------+ +--------+ +--------+
               |         |        |
               v         v        v
            +----------------------+
            |  Orquestador:        |
            |  sintetiza           |
            +----------------------+
                       |
                       v
                   Respuesta
-->
<!-- ascii-note:
intent: fan-out / fan-in; las subtareas no estan predefinidas, las decide el orquestador para cada pedido.
emphasize: el orquestador en rojo arriba y abajo (es el mismo agente); los workers en paralelo.
labels: Pedido, Orquestador (LLM), Worker 1-3, sintetiza, Respuesta.
consistency: mismo lienzo y tratamiento de cajas que los otros cuatro tipos (4.2, 5.1, 5.4 y 5.7).
-->

### Sources

- `corpus/anthropic-building-effective-agents.web.md` — orchestrator-workers: "a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results"; las subtareas no están predefinidas, las determina el orquestador según el pedido.
- `corpus/anthropic-multi-agent-research-system.web.md` — patrón orchestrator-worker del sistema de Research: un agente que planifica crea subagentes, cada uno con su propia ventana, que buscan en paralelo.
- `corpus/AIG4B-Clase-6-Agent.pptx.md` — slide 33: espectro workflows deterministas (prompt chaining, paralelización) / dirigidos por LLM (routing, orchestrator-worker, evaluator-optimizer) / agentes autónomos (solo en notas).

### Speaker notes

La diferencia con Reflexion: ahí los tres roles se turnaban sobre una misma tarea. Acá el orquestador reparte la tarea en pedazos y cada worker es un agente con su propio loop.

La diferencia con la paralelización de la lámina 2.3, según Anthropic: en la paralelización las subtareas están escritas en el código; en orchestrator-workers el orquestador las decide para cada pedido. Anthropic clasifica a los dos como workflows.

El deck del curso (slide 33) dibujaba un espectro con tres puntos: workflows deterministas, workflows dirigidos por LLM (ahí ubicaba al orquestador con workers) y agentes autónomos. Esta clase lo cuenta como tipo de agente con esa lectura: cuando cada worker tiene su propio loop, el sistema entero es un conjunto de agentes.

Desde esta lámina, worker y subagente nombran lo mismo. La sección 6 define sistema multiagente y la 7 recorre los patrones.

---

## 10. Dónde aparece el orquestador con workers

### Content

- **Código en muchos archivos** Un agente de código que tiene que cambiar varios archivos reparte los cambios según el pedido.
- **Búsqueda en muchas fuentes** Una tarea de investigación junta y analiza información de fuentes distintas.
- **Claude Research** Un orquestador planifica la investigación y crea subagentes que buscan en paralelo.

`Anthropic, 2024 (revisado) · jun-2025`

### Sources

- `corpus/anthropic-building-effective-agents.web.md` — ejemplos de orchestrator-workers: productos de código que cambian múltiples archivos; tareas de búsqueda que juntan información de múltiples fuentes.
- `corpus/anthropic-multi-agent-research-system.web.md` — la función Research de Claude: lead agent que planifica y crea subagentes paralelos.

### Speaker notes

Los dos primeros ejemplos son de Anthropic en el post de workflows. El tercero es su propio producto. La sección 9 vuelve a él con sus cifras: el 90,2% y el 15× de tokens.

Dejar planteada la pregunta que la sección 9 contesta: ¿qué pasa cuando dos subagentes cambian el mismo archivo? Para buscar no importa; para escribir código sí.

---

## 11. Los cinco tipos, comparados

### Content

| Tipo | Cómo funciona | Cuándo conviene |
|---|---|---|
| ReAct | Loop pensar → actuar → observar, un paso a la vez | Tareas exploratorias, donde el siguiente paso depende del resultado anterior |
| Plan-and-Execute | Planifica todo al inicio, luego ejecuta los pasos | Tareas largas y predecibles; menos llamadas al LLM |
| Reflexion | Ejecuta, se autoevalúa y reintenta con esa crítica como memoria | Cuando hay un criterio claro de éxito (tests, validaciones) |
| ReWOO | Planifica con variables y ejecuta las tools sin volver a razonar entre medio | Optimizar costo/latencia |
| Multiagente (orquestador + workers) | Un orquestador decide las subtareas en ejecución, las delega en workers con contexto propio y sintetiza | Tareas amplias y paralelizables cuya información no entra en un solo contexto |

### Sources

- Tabla provista por el presentador (memory.md, Step 4, nota de alcance del 2026-10-04), filas 1 a 4 verbatim.
- `corpus/anthropic-building-effective-agents.web.md` · `corpus/anthropic-multi-agent-research-system.web.md` — fila 5, escrita por el editor: orchestrator-workers; "valuable tasks that involve heavy parallelization, information that exceeds single context windows, and interfacing with numerous complex tools".
- `corpus/langchain-planning-agents.web.md` · `corpus/yao-2022-react.pdf.md` · `corpus/shinn-2023-reflexion.pdf.md` — respaldo de las filas 1 a 4.

### Speaker notes

Leer las cuatro primeras filas con las dos preguntas de la lámina 4.1. Cuándo se planifica: ReAct nunca de antemano; Plan-and-Execute y ReWOO al inicio; Reflexion entre intentos. Cuántas veces vuelve a razonar el LLM: ReAct en cada paso; Plan-and-Execute al replanificar; ReWOO solo al final; Reflexion después de cada intento fallido.

La quinta fila cambia otra variable. El orquestador reparte el contexto entre varios loops, y cada worker planifica y razona como cualquiera de los cuatro anteriores. Por eso abre las secciones 6 a 9.

Los tipos se combinan. El executor de Plan-and-Execute es un pequeño ReAct, y el Actor de Reflexion también.

Cierre de la sección 5. Tiempo acumulado: unos 70 minutos.

**Pausa de 10 minutos acá.** Es el corte natural entre los tipos de agente y las arquitecturas multiagente. Retomar a los 80 minutos con la lámina 6.1.

---

# 6. Límites de un agente

**Goal of this section:** Retomar después de la pausa con el contexto como recurso finito y pago, y mostrar los límites de un agente único: el contexto se degrada, las tools compiten y un solo system prompt no especializa. Definir sistema multiagente con las tres palancas que mueve, y frenar con la recomendación de LangChain de empezar por un agente con buenas tools.

---

## 1. ¿Qué es el contexto de un modelo?

<!-- template: quiz -->

### Content

¿Qué es el contexto de un modelo?

- A. Lo que el modelo aprendió cuando lo entrenaron.
- B. Todo lo que el modelo tiene a la vista en una sola corrida: instrucciones, archivos, lo que devolvieron las tools y la conversación hasta ahí.
- C. Las instrucciones del system prompt, y nada más.
- D. El historial de la cuenta del usuario.

**Respuesta:** B. Es finito y se paga por token.

### Sources

- `corpus/orquestacion-de-agentes-clase.md.md` — quiz 1.5, "Qué es el contexto de un modelo": definición y consecuencias (finito, se paga por token).
- `corpus/anthropic-multi-agent-research-system.web.md` — la ventana de contexto del lead agent se trunca pasados los 200.000 tokens (notas).

### Speaker notes

Recapitulación después de la pausa. La sala ya vio la definición en la lámina 2.1: el contexto es el c_t del paper de ReAct. La pregunta vuelve para fijar las dos propiedades que usa la segunda mitad.

A confunde entrenamiento con contexto: lo aprendido está congelado en los pesos, y lo que está a la vista cambia en cada corrida. C se queda con una parte, porque el system prompt entra al contexto junto con todo lo demás. D es una respuesta de producto.

Las dos propiedades: se paga por token, así que repartir trabajo cuesta plata; y es finito, así que un agente con muchas tools y mucho conocimiento lo llena rápido. En el sistema de Research de Anthropic, la ventana del orquestador se trunca pasados los 200.000 tokens.

---

## 2. El contexto se degrada

### Content

A medida que crece el contexto, el modelo recuerda peor lo que tiene adentro. Anthropic lo llama *context rot*.

- **Presupuesto de atención** El contexto es "a finite resource with diminishing marginal returns". Cada token que entra compite con los demás.
- **Degradación gradual** Es "a performance gradient rather than a hard cliff". El rendimiento baja a medida que entra contexto, sin un punto de quiebre.
- **Contexto mínimo** El objetivo de diseño es el conjunto más chico de tokens con mucha señal que maximice la probabilidad del resultado buscado.
- **Acumulación** Un agente que trabaja mucho junta resultados de búsqueda, logs y archivos leídos en su historial, aunque no los vuelva a usar.

`Anthropic, sep-2025`

### Sources

- `corpus/anthropic-context-engineering.web.md` — context rot: "as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases"; "a finite resource with diminishing marginal returns"; "attention budget"; "a performance gradient rather than a hard cliff"; "find the *smallest* *possible* set of high-signal tokens that maximize the likelihood of some desired outcome"; causas (n² relaciones de atención, entrenamiento con secuencias más cortas); tres técnicas (compaction, structured note-taking, sub-agent architectures). Publicado el 29 sep 2025. El registro marca que el post no da cifras y remite a un estudio de Chroma.
- `corpus/claude-code-subagents.web.md` — un subagente sirve cuando una tarea lateral "would flood your main conversation with search results, logs, or file contents you won't reference again".

### Speaker notes

**Original:** "find the *smallest* *possible* set of high-signal tokens that maximize the likelihood of some desired outcome." — [Anthropic, *Effective context engineering for AI agents*](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

Conectar con la clase de transformers. Anthropic atribuye parte de la degradación a la atención, que relaciona cada token con todos los demás, y a que los modelos se entrenan sobre todo con secuencias más cortas. No hace falta volver a la matemática. Lo práctico: un agente con el contexto lleno de resultados viejos razona peor, aunque todavía le quede ventana.

El post no da números; cita un estudio de Chroma que no está en el material de la clase. Si alguien pide una cifra, no la hay.

Anthropic propone tres técnicas contra esto: compactar la conversación, tomar notas fuera del contexto y repartir el trabajo entre subagentes. Esta clase sigue la tercera.

---

## 3. Muchas tools y un solo prompt

### Content

Un agente único carga todas las tools y un solo system prompt. Con muchas capacidades, las dos cosas le juegan en contra.

- **Tools que compiten** Cada tool es una opción más y una descripción más en el contexto. "If a human engineer can't definitively say which tool should be used in a given situation, an AI agent can't be expected to do better."
- **Un prompt generalista** Un único system prompt tiene que ser experto en todos los dominios a la vez. La guía del Agents SDK de OpenAI recomienda lo contrario: "Have specialized agents that excel in one task, rather than having a general purpose agent that is expected to be good at anything."

### Sources

- `corpus/anthropic-context-engineering.web.md` — la cita del ingeniero humano, verbatim; "Bloated tool sets are one of the most common failure modes".
- `corpus/openai-agents-sdk-multi-agent.web.md` — táctica 4 de orquestación con LLM, verbatim (Raw excerpts).
- `corpus/aig4b-clase-6-agentes-biomedica.pdf.md` — limitaciones de un solo agente: sobrecarga de tools, contexto desbordado, "un único system prompt no puede ser experto en todo".
- `corpus/langgraph-multi-agent.web.md` — multiagente vale "when a single agent has too many tools and makes poor decisions about which to use, when tasks require specialized knowledge with extensive context (long prompts and domain-specific tools)" (notas).
- `corpus/chatdev-2023.web.md` — Table 4, ablación: Quality 0,3953 completo, 0,2212 sin descripciones de rol (notas).
- `corpus/magentic-one-2024.web.md` — "rather than deciding between dozens of possible actions, the Orchestrator needs only to decide which agent to call" (notas).

### Speaker notes

La lámina 3.5 dijo que más tools no garantizan mejores resultados, desde el diseño de cada tool. Acá el mismo hecho se lee como un límite del agente único.

La documentación de LangChain lo escribe como criterio para pasar a multiagente: un agente con demasiadas tools que elige mal cuál usar, o una tarea que pide prompts largos y tools propias de un dominio.

En la ablación de ChatDev (lámina 8.1), quitar las descripciones de rol de los system prompts baja la calidad de 0,3953 a 0,2212, con la métrica propia del paper. Muestra que el rol escrito pesa. No compara un agente generalista contra especialistas.

Magentic-One (lámina 8.1) responde con un orquestador de un nivel: elige qué agente llamar, y ese agente elige entre unas pocas acciones propias.

---

## 4. Qué es un sistema multiagente

### Content

Un sistema multiagente son varios agentes que interactúan, de forma colaborativa, competitiva o ambas, para resolver un problema que excede a uno solo. Repartir el trabajo mueve tres palancas.

- **Especialización** Cada agente tiene su system prompt, sus tools y, si conviene, su modelo.
- **Aislamiento de contexto** Cada agente trabaja en su propia ventana y devuelve un resumen. Un subagente puede gastar decenas de miles de tokens y devolver a menudo entre 1.000 y 2.000.
- **Paralelismo** Las subtareas independientes corren a la vez. El sistema gasta más tokens en menos tiempo.

![Un agente con todo en un contexto contra varios agentes](images/s6-4-1-un-agente-vs-varios.png)
<!-- ascii-source:
          UN AGENTE                       VARIOS AGENTES

 +----------------------------+   +--------+ +--------+ +--------+
 | prompt general             |   |prompt A| |prompt B| |prompt C|
 | todas las tools            |   |tools A | |tools B | |tools C |
 | todo el historial          |   |ctx A   | |ctx B   | |ctx C   |
 | una tarea por vez          |   +--------+ +--------+ +--------+
 +----------------------------+       |   en paralelo  |      |
                                      v          v          v
                                   resumen    resumen    resumen
-->
<!-- ascii-note:
intent: contrastar un agente con todo en un solo contexto contra varios agentes con prompt, tools y contexto propios que corren en paralelo y devuelven resumenes.
emphasize: las tres columnas separadas a la derecha y la etiqueta "en paralelo" (acento rojo); el bloque unico de la izquierda como lo que se parte.
labels: UN AGENTE, VARIOS AGENTES, prompt general, todas las tools, todo el historial, una tarea por vez, prompt A/B/C, tools A/B/C, ctx A/B/C, resumen.
-->

### Sources

- `corpus/aig4b-clase-6-agentes-biomedica.pdf.md` — definición de sistema multiagente: múltiples agentes que interactúan "de forma colaborativa, competitiva, o ambas" para resolver un problema que excede las capacidades de un agente individual (parafraseada).
- `corpus/anthropic-context-engineering.web.md` — cada subagente "might explore extensively, using tens of thousands of tokens or more, but returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens)".
- `corpus/mast-why-mas-fail-2025.web.md` — un MAS es "a collection of agents designed to interact through orchestration" y habilita "task decomposition, performance parallelization, context isolation, specialized model ensembling" (notas).
- `corpus/anthropic-multi-agent-research-system.web.md` — "A multi-agent system consists of multiple agents (LLMs autonomously using tools in a loop) working together" (notas).
- `corpus/langchain-multi-agent-architectures.web.md` — context management, distributed development y paralelización como motivos (notas).
- `corpus/sistemas-multiagente-clase.md.md` — lámina 2.4 del deck hermano: las tres palancas y el diagrama de un agente contra varios (estructura reutilizada; las cifras salen de los registros de arriba).

### Speaker notes

**Original:** "A multi-agent system consists of multiple agents (LLMs autonomously using tools in a loop) working together" — [Anthropic, jun-2025](https://www.anthropic.com/engineering/multi-agent-research-system).

La definición de la lámina es la del deck del curso; la de Anthropic es su versión con LLMs. MAST, el paper sobre fallas de la sección 9, agrega la palabra que importa para lo que sigue: agentes que interactúan a través de una orquestación.

Las tres palancas son el vocabulario para leer los patrones de la sección 7, junto con el costo que compara la lámina 7.8. Un pipeline especializa y no paraleliza. Los handoffs especializan y, por defecto, no aíslan. Subagents mueve las tres.

LangChain agrega un cuarto motivo, que no es técnico: el desarrollo distribuido, con equipos distintos dueños de agentes distintos. Aparece en la lámina siguiente.

Volver al diagrama de la izquierda: es el agente de las secciones 3 a 5. Su prompt, sus tools y su historial se reparten entre los agentes de la derecha.

---

## 5. Primero, un solo agente

### Content

LangChain recomienda empezar con un solo agente y buenas tools. Dos restricciones empujan a repartir cuando las capacidades crecen.

- **Manejo del contexto** El conocimiento especializado de cada capacidad no entra cómodo en un solo prompt, y hay que mostrarlo de forma selectiva.
- **Desarrollo distribuido** Equipos distintos mantienen capacidades distintas, y un único prompt monolítico se vuelve inmanejable entre equipos.

"Add tools before adding agents."

### Sources

- `corpus/langchain-multi-agent-architectures.web.md` — "Many agentic tasks are best handled by a single agent with well-designed tools. You should start here"; las dos restricciones (Context management, Distributed development); cierre: "Start with a single agent and good prompt engineering. Add tools before adding agents. Graduate to multi-agent patterns only when you hit clear limits." Post de Sydney Runkle, 14 ene 2026.
- `corpus/langgraph-multi-agent.web.md` — "a single agent with the right (sometimes dynamic) tools and prompt can often achieve similar results" (notas).

### Speaker notes

**Original:** "Start with a single agent and good prompt engineering. Add tools before adding agents. Graduate to multi-agent patterns only when you hit clear limits." — [LangChain, ene-2026](https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture).

Cerrar la sección con este freno es deliberado: las secciones 7 a 9 son para cuando un agente no alcanza. LangChain lo escribe en cursiva, el multiagente *puede* ser la opción correcta.

Las dos restricciones son distintas en naturaleza. La primera es técnica (el contexto es finito). La segunda es organizacional (equipos distintos), y es la que más se parece a una decisión de arquitectura de software clásica: separar módulos por equipo dueño.

La primera restricción es la que mostraron las láminas 6.2 y 6.3. La documentación de LangChain la cierra con otra frase: "a single agent with the right (sometimes dynamic) tools and prompt can often achieve similar results". La carga de la prueba la tiene el multiagente.

Cierre de la sección 6. Tiempo acumulado: unos 89 minutos.

---

# 7. Patrones multiagente

**Goal of this section:** Precisar qué hace un subagente, presentar los cuatro patrones multiagente de LangChain (subagents, skills, handoffs, router) con lo que cuesta cada uno, y completar el mapa con cuatro topologías: red adaptativa, pipeline, pizarra y jerarquía. Cada patrón se lee con las tres palancas de la lámina 6.4. Al salir, la sala sabe qué patrón corresponde a qué requisito.

---

## 1. Qué es un subagente

### Content

Un subagente es el worker de la lámina 5.9: un agente que otro agente crea para una parte del trabajo, con su propia ventana de contexto.

- **Encargo** El agente que lo crea decide qué entra en esa ventana, desde un pedido de dos líneas hasta todo lo que sabía.
- **Hermanos** Mientras trabaja, un subagente no ve lo que hace otro.
- **Decisión** Una tool se ejecuta y devuelve un resultado. Un subagente decide qué hacer con su encargo.

![Cada subagente con su propia ventana de contexto](images/s7-1-1-subagentes-ventana-propia.png)
<!-- ascii-source:
 +--------------------------------------------+
 |  Orquestador            [ventana propia]   |
 +--------------------------------------------+
    | encargo   ^                | encargo  ^
    v           | hallazgo       v          | hallazgo
 +----------------+         +----------------+
 |  Subagente A   |         |  Subagente B   |
 | [ventana       |  no se  | [ventana       |
 |  propia]       |   ven   |  propia]       |
 +----------------+         +----------------+
-->
<!-- ascii-note:
intent: cada agente tiene su propia ventana de contexto; el orquestador le pasa un encargo a cada subagente y recibe un hallazgo.
emphasize: las tres etiquetas [ventana propia] (acento rojo); el hueco "no se ven" entre hermanos queda como rotulo secundario.
labels: Orquestador, Subagente A, Subagente B, encargo, hallazgo, ventana propia, no se ven.
-->

### Sources

- `corpus/orquestacion-de-agentes-clase.md.md` — lámina 2.1 "Qué es un subagente" y quiz 1.4: definición, ventana de contexto propia, fan-out / fan-in, "hallazgos destilados, no su historial completo"; "una herramienta se ejecuta y devuelve, un subagente decide".
- `corpus/anthropic-multi-agent-research-system.web.md` — "The essence of search is compression": los subagentes trabajan en paralelo con sus propias ventanas y condensan lo importante para el agente principal.

### Speaker notes

**Original:** "The essence of search is compression" — [Anthropic, jun-2025](https://www.anthropic.com/engineering/multi-agent-research-system). Cada subagente lee mucho y devuelve poco; la lámina 6.4 ya dio el orden de magnitud.

La pregunta donde la sala se confunde es si los subagentes comparten el contexto. Cada uno tiene su propia ventana, siempre. Lo que cambia es cuánto pone adentro el agente que lo crea. La lámina 9.5 muestra que ni pasarle todo alcanza.

---

## 2. Cuatro patrones

### Content

Orquestar es decidir quién hace qué, en qué orden, con qué información y bajo qué límite de gasto. LangChain agrupa la mayoría de las aplicaciones multiagente en cuatro patrones de orquestación.

- **Subagents** Un agente principal llama a subagentes especializados como si fueran tools.
- **Skills** Un solo agente carga prompts y conocimiento especializado cuando los necesita.
- **Handoffs** El agente activo cambia según el estado de la conversación.
- **Router** Un paso de ruteo clasifica el pedido, lo despacha a agentes en paralelo y sintetiza.

`LangChain, ene-2026`

### Sources

- `corpus/orquestacion-de-agentes-clase.md.md` — lámina 1.7 "Qué es orquestar", definición.
- `corpus/langchain-multi-agent-architectures.web.md` — "Four architectural patterns form the foundation of most multi-agent applications: subagents, skills, handoffs, and routers."

### Speaker notes

Presentar los cuatro de un vistazo antes de verlos uno por uno. Cada uno se lee con las tres palancas de la lámina 6.4: qué especializa, cuánto aísla el contexto y qué corre en paralelo. La lámina 7.8 compara lo que cuestan.

El deck del curso (slide 32) nombraba estas formas con otro vocabulario. Subagents corresponde a la variante en la que los especialistas se exponen como tools del orquestador. La red adaptativa y la jerarquía vuelven en las láminas 7.9 y 7.10.

---

## 3. Subagents: orquestación centralizada

### Content

![Patrón subagents de LangChain: el pedido entra al Main Agent, que llama y recibe resultados de los subagentes A, B y C, y produce la respuesta final](images/69cbaa03649e3ebd9d135314_image--9--1.png)

- **Estado** El principal mantiene la conversación; los subagentes no recuerdan interacciones previas. El aislamiento de contexto es fuerte.
- **Costo** Una llamada extra al modelo por interacción, porque los resultados vuelven por el agente principal.

### Sources

- `corpus/langchain-multi-agent-architectures.web.md` — sección "Subagents: Centralized orchestration", How it works, Key tradeoff; imagen `69cbaa03649e3ebd9d135314_image--9--1.png` (stub pendiente de Phase 2; contenido verificado a la vista por el editor: User Request → Main Agent ↔ Subagent A/B/C → Final Response).
- `corpus/openai-agents-sdk-multi-agent.web.md` — agents as tools: un manager "keeps control of the conversation and calls specialists via `Agent.as_tool()`" (notas).

### Speaker notes

Es el orquestador con workers de la lámina 5.9 en la versión de LangChain, y el que Anthropic usa en su sistema de Research. LangChain llama agente principal al orquestador. El agente principal puede llamar a varios subagentes en paralelo.

Señalar en el diagrama las flechas de ida y vuelta entre el agente principal y cada subagente. Todo pasa por el centro: es control centralizado, y es también la llamada extra que el patrón paga.

Mejor para, según LangChain: aplicaciones con varios dominios distintos donde los subagentes no necesitan hablar con el usuario. Ejemplo: un asistente personal que coordina calendario, email y CRM.

En el Agents SDK de OpenAI este patrón se llama agentes como tools: el orquestador llama a especialistas con `Agent.as_tool()` y conserva la conversación.

---

## 4. Skills: divulgación progresiva

### Content

![Patrón skills de LangChain: el pedido entra al Main Agent, que carga las skills A, B y C y produce la respuesta final](images/69cbaa0feea3104c341d0d4f_image--10.png)

- **Cómo funciona** Al arrancar, el agente conoce solo el nombre y la descripción de cada skill. Cuando una se vuelve relevante, carga su contenido completo, y los archivos adicionales son un tercer nivel de detalle.
- **Estado** Un solo agente, que interactúa con el usuario todo el tiempo.
- **Costo** El contexto se acumula en la conversación a medida que se cargan skills.

### Sources

- `corpus/langchain-multi-agent-architectures.web.md` — sección "Skills: Progressive disclosure": "perhaps controversially, we consider skills to be a quasi-multi-agent architecture"; directorios con instrucciones, scripts y recursos; tres niveles de detalle; Key tradeoff (token bloat); imagen `69cbaa0feea3104c341d0d4f_image--10.png` (stub pendiente de Phase 2; verificada a la vista por el editor: Main Agent → Skill A/B/C, flechas de ida solamente).

### Speaker notes

Es el patrón polémico de los cuatro, y LangChain lo dice: técnicamente hay un solo agente, que adopta personalidades especializadas. Lo cuentan como cuasi multiagente porque da beneficios parecidos (desarrollo distribuido, control fino del contexto) sin manejar varias instancias de agente.

Comparar el diagrama con el anterior: acá las flechas van solo de ida. El agente carga la skill y sigue él; no hay un subagente que devuelva un resultado.

La sala ya trabajó con skills en clases anteriores. Es el mismo mecanismo: el nombre y la descripción siempre están en el contexto, el contenido entra cuando hace falta.

Mejor para: un agente con muchas especializaciones posibles, como agentes de código o asistentes creativos.

---

## 5. Handoffs: transiciones por estado

### Content

![Patrón handoffs de LangChain: el pedido entra al Agent A, que transfiere el control a los agentes B y C, y cualquiera de los tres puede producir la respuesta final](images/69cbaa10eea3104c341d0d5e_image--11.png)

- **Cómo funciona** Cada agente puede transferir el control a otro con una llamada a una tool de handoff, que actualiza el estado y decide qué agente se activa.
- **Estado** El estado sobrevive entre turnos de la conversación y habilita flujos en secuencia.
- **Costo** Es el patrón más stateful de los cuatro, y pide manejar ese estado con cuidado.

### Sources

- `corpus/langchain-multi-agent-architectures.web.md` — sección "Handoffs: State-driven transitions", How it works, Best for, Key tradeoff; imagen `69cbaa10eea3104c341d0d5e_image--11.png` (stub pendiente de Phase 2; verificada a la vista por el editor: Agent A ↔ B ↔ C, los tres con salida a Final Response).
- `corpus/openai-agents-sdk-handoffs.web.md` — "Handoffs are represented as tools to the LLM" (`transfer_to_<agent_name>`). `corpus/openai-swarm.web.md` — Swarm "is now replaced by the OpenAI Agents SDK" (notas).

### Speaker notes

La diferencia con los dos anteriores: no hay un agente principal fijo. El que atiende cambia, y cualquiera de los tres puede responder al usuario.

Un handoff puede ser cambiar de agente o cambiar el system prompt y las tools del agente actual. Para el modelo es lo mismo: una tool más que, en vez de traer datos, mueve el control.

Mejor para: flujos de soporte que juntan información por etapas, o cualquier caso donde una capacidad se habilita recién cuando se cumplió una condición previa.

En el Agents SDK de OpenAI cada handoff es una tool `transfer_to_<agente>`, y el agente que recibe pasa a ser el activo. Swarm, la versión educativa anterior de OpenAI, quedó reemplazada por el SDK. Qué historial ve el agente que recibe: lámina 9.3.

---

## 6. Router: despacho en paralelo y síntesis

### Content

![Patrón router de LangChain: el pedido pasa por un Router que lo despacha a los agentes A, B y C en paralelo, y un Synthesizer combina sus resultados en la respuesta final](images/69cbaa10eea3104c341d0d5b_image--12.png)

- **Cómo funciona** El router descompone el pedido, invoca a cero o más agentes especializados en paralelo y sintetiza los resultados.
- **Estado** Típicamente sin estado: cada pedido se maneja por separado.
- **Costo** Si la conversación necesita historial, el ruteo se repite en cada turno. Se mitiga envolviendo el router como tool de un agente conversacional.

### Sources

- `corpus/langchain-multi-agent-architectures.web.md` — sección "Router: Parallel dispatch and synthesis", How it works, Best for, Key tradeoff; imagen `69cbaa10eea3104c341d0d5b_image--12.png` (stub pendiente de Phase 2; verificada a la vista por el editor: User Request → Router → Agent A/B/C → Synthesizer → Final Response).

### Speaker notes

Es el único de los cuatro que tiene forma de tubería: entra, se reparte, se junta, sale. Por eso es predecible y sin estado.

La diferencia con subagents: el router decide una vez al inicio y no vuelve a razonar sobre los resultados intermedios; el agente principal de subagents puede llamar a un subagente, leer lo que devolvió y decidir a quién llamar después.

Mejor para: verticales separadas que hay que consultar en paralelo, como una base de conocimiento empresarial o un soporte que cubre varias áreas.

---

## 7. Qué patrón para qué requisito

### Content

| Requisito | Patrón | Ejemplo |
|---|---|---|
| Varios dominios distintos y ejecución en paralelo | Subagents | Asistente personal que coordina calendario, email y CRM |
| Un solo agente con muchas especializaciones posibles, composición liviana | Skills | Agentes de código, asistentes creativos |
| Flujo secuencial con transiciones de estado; el agente conversa con el usuario todo el tiempo | Handoffs | Soporte al cliente que junta información por etapas |
| Verticales distintas; consultar varias fuentes en paralelo y sintetizar | Router | Base de conocimiento empresarial, soporte multi-vertical |

`LangChain, ene-2026`

### Sources

- `corpus/langchain-multi-agent-architectures.web.md` — Table 1 "Matching requirements to patterns" (recuperada de `original.html`); ejemplos por patrón de las secciones "Best for".

### Speaker notes

Es la lámina que la sala se lleva para decidir. Leerla al revés también sirve: si el flujo es secuencial y el usuario conversa todo el tiempo, subagents es mala idea, porque los subagentes no hablan con el usuario.

El artículo tiene una segunda tabla con estrellas por requisito (desarrollo distribuido, paralelización, multi-hop, interacción directa con el usuario). La más útil para discutir: subagents tiene la puntuación mínima en interacción directa con el usuario, y handoffs no soporta ni desarrollo distribuido ni paralelización.

Esta tabla cumple el papel de lámina de ejemplos para los cuatro patrones: los diagramas ya se vieron, y acá aparece dónde se usa cada uno.

---

## 8. Cuánto cuesta cada patrón

### Content

Tres escenarios de LangChain: un pedido único ("buy coffee"), el mismo pedido repetido en un segundo turno, y una consulta sobre tres dominios ("Compare Python, JavaScript, and Rust for web development").

| Patrón | Pedido único: llamadas | Pedido repetido: llamadas totales | Tres dominios: llamadas | Tres dominios: tokens |
|---|---|---|---|---|
| Subagents | 4 | 8 | 5 | ~9K |
| Skills | 3 | 5 | 3 | ~15K |
| Handoffs | 3 | 5 | 7+ | ~14K+ |
| Router | 3 | 6 | 5 | ~9K |

Subagents paga una llamada extra por turno y, con varios dominios, usa un 40% menos de tokens que skills.

### Sources

- `corpus/langchain-multi-agent-architectures.web.md` — Table 3 (escenario 1, llamadas al modelo), Table 4 (escenario 2, llamadas totales en dos turnos), Table 5 (escenario 3, llamadas y tokens; ~2000 tokens de documentación por agente de lenguaje). Derivaciones: 40% = 1 − 9K / 15K (subagents contra skills, Table 5); ahorro de skills y handoffs en el pedido repetido = (8 − 5) / 8 = 37,5%, que la tabla redondea a 40%; router = (8 − 6) / 8 = 25%. El texto del artículo dice "40-50%" y "67% fewer tokens"; sus propias tablas no lo sostienen (marcado [verified] por el librarian).

### Speaker notes

Leer por columna. En un pedido único gana cualquiera menos subagents, que paga la vuelta por el agente principal. En un pedido repetido ganan los patrones con estado, skills y handoffs: no tienen que volver a cargar nada, y bajan de 8 a 5 llamadas, un 37,5% menos (LangChain lo redondea a 40%). En la consulta de tres dominios ganan los que paralelizan, subagents y router: cada agente trabaja solo con su documentación, unos 9K tokens en total contra los 15K de skills, que acumula las tres en una conversación.

Dos correcciones al artículo, por si alguien lo lee: el texto dice que los patrones con estado ahorran "40-50%" de llamadas, y su tabla da 40% como máximo. También dice que subagents procesa "67% menos tokens" que skills; con sus números es 40% menos (o skills usa cerca de 67% más). La dirección del argumento se mantiene.

Son escenarios ilustrativos de LangChain, no benchmarks medidos. Sirven para razonar la forma del costo.

---

## 9. Red adaptativa

### Content

En la red adaptativa de Kore.ai no hay un nodo que coordine. Cada agente ejecuta su parte, delega o enriquece la tarea, y la pasa al siguiente.

![Red adaptativa: agentes sin nodo central](images/s7-9-1-red-adaptativa.png)
<!-- ascii-source:
            Usuario
               |
               v
        +-------------+
        |  Agente A   |
        +-------------+
          |         |
          v         v
    +---------+   +---------+
    | Agente  |<->| Agente  |
    |    B    |   |    C    |
    +---------+   +---------+

  cada agente ejecuta, delega o enriquece
-->
<!-- ascii-note:
intent: una topologia sin nodo central; la coordinacion se replica en cada agente y el control pasa de uno a otro.
emphasize: la arista directa entre Agente B y Agente C (acento rojo).
labels: Usuario, Agente A/B/C, cada agente ejecuta, delega o enriquece.
-->

Frente al orquestador central de las láminas 5.9 y 7.3, la red ahorra los saltos por el centro y pierde el único lugar donde mirar qué pasó.

`Kore.ai, oct-2025 (act. jul-2026)`

### Sources

- `corpus/koreai-orchestration-patterns.web.md` — Adaptive agent network (decentralized collaboration): definición, Use / Avoid; Supervisor (centralized command and control) como la forma con nodo central (notas).
- `corpus/AIG4B-Clase-6-Agent.pptx.md` — slide 32: Network, "Más flexible pero menos predecible" (notas).
- `corpus/generative-agents-2023.web.md` — 25 agentes en Smallville; la invitación a la fiesta pasa de 1 agente (4%) a 13 (52%) en dos días simulados; 5 de los 12 invitados asisten (notas).

### Speaker notes

Kore.ai llama Supervisor a la forma con un orquestador central, la de las láminas 5.9 y 7.3, así que no hace falta dibujarla de nuevo. La red adaptativa se parece a handoffs (lámina 7.5): el control pasa de agente en agente. Esa correspondencia es lectura de la cátedra.

Según Kore.ai, la red sirve para tiempo real, voz y conversaciones con continuidad. La desaconseja cuando la trazabilidad y el debugging son prioridad, o cuando no está claro qué agente es dueño de la tarea.

Un ejemplo sin pizarra ni orquestador es Generative Agents: 25 agentes en un pueblo simulado que se pasan información conversando. En dos días simulados, la invitación a una fiesta pasó de 1 agente (4%) a 13 (52%), y 5 de los 12 invitados fueron.

---

## 10. Pipeline, pizarra y jerarquía

### Content

Tres topologías más completan el mapa.

![Pipeline, pizarra y jerarquía lado a lado](images/s7-10-1-pipeline-pizarra-jerarquia.png)
<!-- ascii-source:
     PIPELINE              PIZARRA                    JERARQUIA

    +-------+       +---+           +---+         +-------------+
    |   A   |       | A |           | B |         | orquestador |
    +-------+       +---+           +---+         +-------------+
        |             |  publica      ^  lee         |        |
        v             v               |              v        v
    +-------+      +-------------------+         +------+  +------+
    |   B   |      |  espacio comun    |         | orq. |  | orq. |
    +-------+      +-------------------+         +------+  +------+
        |             ^               |           |    |       |
        v             |  publica      v  lee      v    v       v
    +-------+       +---+           +---+        +--+ +--+   +--+
    |   C   |       | C |           | D |        |A | |B |   |C |
    +-------+       +---+           +---+        +--+ +--+   +--+
-->
<!-- ascii-note:
intent: tres topologias lado a lado; una cadena fija, un espacio comun sin orquestador donde los agentes publican y leen, y un arbol de orquestadores.
emphasize: el espacio comun de la pizarra (acento rojo); la forma distinta de cada topologia (cadena, estrella sin centro que decide, arbol).
labels: PIPELINE, PIZARRA, JERARQUIA, A-D, espacio comun, publica, lee, orquestador, orq.
-->

- **Pipeline** El código fija el orden, y la salida de un agente es la entrada del siguiente. MetaGPT lo usa (lámina 8.1).
- **Pizarra** Cada agente publica en un espacio común y actúa cuando aparece lo que necesita, sin un orquestador que reparta. MetaGPT también la usa.
- **Jerarquía** Un orquestador coordina a otros orquestadores, y cada uno coordina su equipo. Contract Net ya lo permitía en 1980; en Claude Code, un subagente puede crear subagentes hasta tres niveles abajo.

### Sources

- `corpus/metagpt-2023.web.md` — "assembly-line paradigm"; "Publish-subscribe via a shared message pool" (el mecanismo se cuenta en la lámina 8.1).
- `corpus/contract-net-protocol.web.md` — "introduced in 1980 by Reid G. Smith"; manager, propuestas y adjudicación; "a manager assigns tasks to contractors, who in turn decompose into lower-level task and assign them to the lower level"; "This task can then be divided and subcontracted". El registro deja abierto si el origen es 1980 o el trabajo de Smith de 1977–1978.
- `corpus/claude-code-subagents.web.md` — un subagente puede lanzar subagentes "up to three layers below the main conversation"; el registro marca que el valor cambió entre versiones (documentación capturada el 2026-10-04).
- `corpus/AIG4B-Clase-6-Agent.pptx.md` — slide 32: Hierarchical.
- `corpus/anthropic-building-effective-agents.web.md` — prompt chaining como workflow (notas).
- `corpus/sistemas-multiagente-clase.md.md` — láminas 3.3, 3.7 y 3.8 del deck hermano (pipeline, red y pizarra, jerárquica); se tomó la estructura, sin el caso Pampa Viajes.

### Speaker notes

El pipeline es un workflow en el sentido de la lámina 2.3: el código decide el orden. Es predecible y fácil de depurar. Un error temprano se arrastra hasta el final, y la vuelta atrás hay que programarla a mano. Es el prompt chaining de Anthropic con un agente en cada paso.

La pizarra es flexible, porque se agrega un agente sin tocar a los demás, y hay que decidir quién termina y quién resuelve dos escrituras contradictorias. MetaGPT combina las dos primeras: su flujo es una línea de montaje y su comunicación es una pizarra.

Contract Net funciona así: un agente anuncia una tarea, los contratistas ofertan y el que anunció adjudica. Un contratista puede subdividir la tarea y subcontratar, y así se arma la jerarquía.

La jerarquía escala a decenas de agentes, y cada nivel agrega llamadas, latencia y otro resumen donde se pierde información. Con pocos agentes sobra. El dato de Claude Code es de la documentación de octubre de 2026 y cambió entre versiones.

Cierre de la sección 7. Tiempo acumulado: unos 108 minutos.

---

# 8. Implementaciones reales

**Goal of this section:** Mostrar sistemas publicados que llevan los patrones de la sección 7 a la práctica, cada uno con su idea propia y un resultado de su paper, y separarlos de las arquitecturas que ponen varios LLM sin tools sobre una misma pregunta.

---

## 1. Cuatro sistemas publicados

### Content

| Sistema | Patrón | Idea propia | Resultado que reporta |
|---|---|---|---|
| MetaGPT (2023) | Línea de montaje de cinco roles, con pizarra | Los agentes publican documentos con formato fijo en vez de conversar | pass@1 de 85,9% en HumanEval y 87,7% en MBPP |
| ChatDev (2023) | Fases en cadena | Cada subtarea es un diálogo entre un instructor y un asistente; entre fases pasa solo la solución | Calidad de 0,3953 contra 0,1523 de MetaGPT, en su propio dataset |
| AutoGen (2023) | Agentes que conversan; en el chat grupal, un `GroupChatManager` elige quién habla | Sumar un agente corrige fallas del resto: en ALFWorld, uno que inyecta reglas de sentido común | Éxito en ALFWorld de 54% a 69% con ese tercer agente |
| Magentic-One (2024) | Orquestador con cuatro workers, uno sin LLM | Dos registros: el del plan (task ledger) y el del avance (progress ledger) | 38% en GAIA y 32,8% en WebArena, con configuraciones distintas |

### Sources

- `corpus/metagpt-2023.web.md` — cinco roles y "assembly-line paradigm"; "structured communication interfaces" en vez de diálogo; pool de mensajes; Pass@1 85,9% (HumanEval) y 87,7% (MBPP); SoftwareDev: ejecutabilidad 3,75 contra 2,25 de ChatDev (notas).
- `corpus/chatdev-2023.web.md` — chat chain por fases (diseño, código, pruebas), diálogo instructor-asistente, "By sharing only the solutions of each subtask rather than the entire communication history"; Table 1: Quality 0,3953 (ChatDev), 0,1523 (MetaGPT), 0,1419 (GPT-Engineer), sobre su dataset SRDD.
- `corpus/mast-why-mas-fail-2025.web.md` — Table 3: ChatDev como "Hierarchical Workflow" (notas).
- `corpus/autogen-2023.web.md` — conversable agents, dynamic group chat con `GroupChatManager`; Table 3 (ALFWorld, 134 tareas, éxito promedio con GPT-3.5-turbo): ReAct 54, ALFChat 2 agentes 54, ALFChat 3 agentes 69; mejor de 3: 66 / 63 / 77; el ReAct de esa tabla corre con text-davinci-003 (notas).
- `corpus/magentic-one-2024.web.md` — Orchestrator, WebSurfer, FileSurfer, Coder y ComputerTerminal ("deterministically executes code and shell commands, no LLM"); task ledger y progress ledger; 38% en GAIA (GPT-4o + o1) y 32,8% en WebArena (GPT-4o), configuraciones distintas según el registro.
- `corpus/yao-2022-react.pdf.md` — Table 3: ALFWorld, ReAct best of 6 = 71 con PaLM-540B (notas).
- `corpus/sistemas-multiagente-clase.md.md` — láminas 4.1 a 4.4 del deck hermano (selección de sistemas); cada cifra se tomó del registro de su paper.

### Speaker notes

Cada fila es una topología de la sección 7 llevada a un sistema, con resultados de 2023 y 2024. GAIA y WebArena son tareas de asistente general y de navegación web.

MetaGPT y ChatDev se contradicen: cada uno le gana al otro en su propio dataset (MetaGPT reporta ejecutabilidad 3,75 contra 2,25).

ChatDev tiene dos lecturas: fases en cadena y, adentro de cada fase, pares instructor-asistente. MAST (sección 9) lo clasifica como flujo jerárquico.

El 54% y el 69% de AutoGen en ALFWorld son promedios con GPT-3.5-turbo. El 71% de ReAct de la lámina 4.7 es el mejor de 6 corridas con PaLM-540B, así que las cifras no se comparan.

El ComputerTerminal de Magentic-One ejecuta código sin LLM. Criterio de la cátedra: si la respuesta correcta se puede escribir como regla y verificar, ese agente no necesita modelo.

---

## 2. Varios modelos sobre una misma pregunta

### Content

Debate y Mixture-of-Agents ponen varios LLM sobre la misma pregunta, sin tools. Los papers llaman agente a cada instancia. Con la definición de esta clase ninguna actúa sobre un ambiente, así que tampoco forman un sistema multiagente.

- **Debate** Varias instancias del mismo modelo responden, leen las respuestas de las otras y corrigen la suya durante varias rondas. Con 3 instancias y 2 rondas, la aritmética pasa de 67,0% a 81,8% de acierto.
- **Mixture-of-Agents** Capas de modelos que proponen respuestas; cada capa lee todas las de la anterior y un agregador escribe la final. Solo con modelos abiertos llega a 65,1% en AlpacaEval 2.0, contra 57,5% de GPT-4o.

Las dos pagan en llamadas y en latencia: MoA no empieza a responder hasta que terminan todas las capas.

`Du et al., 2023 · Wang et al., 2024`

### Sources

- `corpus/multiagent-debate-2023.web.md` — procedimiento de debate; Table 1 (3 agentes, 2 rondas): Arithmetic 67,0 → 81,8, GSM8K 77,0 → 85,0 (Single Agent contra Multi-Agent Debate); `gpt-3.5-turbo-0301`; 100 problemas por tarea; debates que convergen a una respuesta incorrecta (notas).
- `corpus/mixture-of-agents-2024.web.md` — arquitectura en capas, proponentes y agregador; Table 2(a): MoA 65,1% de LC win rate contra 57,5% de GPT-4 Omni (05/13); LC win rate definido como el win rate de AlpacaEval 2.0 controlado por largo, contra `gpt-4-1106-preview`, con un juez basado en GPT-4; latencia del primer token como limitación; cita a Wang et al. 2024b (un agente con un prompt fuerte alcanza calidad comparable, notas). El registro marca que el §1 del paper dice 65,8%, valor que no aparece en ninguna tabla; la lámina usa el de la tabla.

### Speaker notes

La lámina sirve de contraste con la 1.1 y la 1.7. Un LLM sin tools ni ambiente no es un agente, y varias llamadas a LLMs sobre una misma pregunta mejoran la respuesta gastando más llamadas. Los papers usan la palabra agente en ese sentido amplio.

El debate tiene un caso interesante: a veces todos arrancan mal y llegan bien. También el contrario, debates que convergen con confianza a una respuesta incorrecta. En GSM8K, un set de problemas de matemática, la mejora fue de 77,0% a 85,0%. Son muestras chicas, cien problemas por tarea, con gpt-3.5-turbo de 2023.

AlpacaEval 2.0 compara las respuestas contra las de un modelo de referencia, con un juez basado en GPT-4 y una corrección por largo. El mismo paper de MoA cita un trabajo que encontró que un solo agente con un prompt fuerte y buenos ejemplos alcanza una calidad comparable. Vuelve la advertencia de la lámina 6.5.

Cierre de la sección 8. Tiempo acumulado: unos 113 minutos.

---

# 9. Cuándo repartir

**Goal of this section:** Dar el criterio para decidir si conviene repartir el trabajo entre varios agentes. La sección pone precio en tokens al paralelismo, muestra cómo fallan los sistemas multiagente según MAST y que el aislamiento hay que configurarlo, y resuelve el debate entre Cognition y Anthropic con una pregunta sobre el trabajo: si lee o si escribe. Cierra con un caso que aplica esa regla.

---

## 1. El precio de paralelizar

<!-- template: stat -->

### Content

- **~4×** los tokens de un chat, para un agente.
- **~15×** los tokens de un chat, para un sistema multiagente.
- **80%** de la varianza de desempeño en BrowseComp se explica solo por el uso de tokens. BrowseComp mide si un agente que navega la web encuentra información difícil de hallar.

Anthropic concluye que el multiagente pide tareas cuyo valor alcance para pagar la mejora de desempeño.

`Anthropic, jun-2025`

### Sources

- `corpus/anthropic-multi-agent-research-system.web.md` — BrowseComp "tests the ability of browsing agents to locate hard-to-find information"; "agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats"; en BrowseComp, tres factores explican el 95% de la varianza y el uso de tokens solo explica el 80%; "multi-agent systems require tasks where the value of the task is high enough to pay for the increased performance". Cifras internas de Anthropic, sin metodología publicada.

### Speaker notes

**Original:** "multi-agent systems require tasks where the value of the task is high enough to pay for the increased performance." — [Anthropic, jun-2025](https://www.anthropic.com/engineering/multi-agent-research-system).

La tercera cifra trae una lectura incómoda que Anthropic escribe en su propio post: los sistemas multiagente funcionan sobre todo porque gastan suficientes tokens para resolver el problema. Los tres factores que explican el 95% son uso de tokens, cantidad de llamadas a tools y elección de modelo.

Ejercicio para la sala: tomar el costo de una tarea como chat, multiplicarlo por 15 y preguntarse si la tarea lo vale. El precio por millón de tokens del proveedor hay que traerlo actualizado el día de la clase; el corpus no tiene una lista de precios.

Son cifras de Anthropic sobre su propio sistema. Se citan como lo que reporta, no como evidencia independiente.

---

## 2. Cómo fallan

### Content

MAST analizó 1.642 trazas de 7 sistemas multiagente abiertos y encontró tasas de falla de entre 41% y 86,7%. Las fallas caen en tres categorías.

| Categoría | Parte de las fallas | Modos más frecuentes |
|---|---|---|
| Diseño del sistema | 44,2% | repetir pasos (15,7%), no saber cuándo terminar (12,4%), desobedecer la tarea (11,8%) |
| Desalineación entre agentes | 32,35% | razonamiento que no coincide con la acción (13,2%), desviarse de la tarea (7,4%), no pedir aclaración (6,8%) |
| Verificación | 23,5% | verificación incorrecta (9,1%), ausente o incompleta (8,2%), terminar antes de tiempo (6,2%) |

`Cemri et al. (UC Berkeley), mar-2025`

### Sources

- `corpus/mast-why-mas-fail-2025.web.md` — "41% to 86.7% failure rate on 7 state-of-the-art (SOTA) open-source MAS"; 1642 trazas anotadas (MAST-Data); 14 modos en 3 categorías con sus porcentajes (§4). Totales por categoría = suma de los modos: 44,2 = 11,8 + 1,5 + 15,7 + 2,8 + 12,4; 32,35 = 2,2 + 6,8 + 7,4 + 0,85 + 1,9 + 13,2; 23,5 = 6,2 + 8,2 + 9,1; suman 100,05% por redondeo (verificado por el librarian). Ejemplo de FM-2.4 de la Figura 3 e insights 2 y 3 (notas). El registro marca que el rango 41%–86,7% viene de la Figura 5, que no se capturó; el texto lo afirma.
- `corpus/agentless-2024.web.md` — 32,00% (96 correctos) en SWE-bench Lite a 0,70 dólares, "compared with all existing open-source software agents" (notas).

### Speaker notes

MAST es un paper de Berkeley de 2025 que anotó a mano trazas de siete sistemas abiertos, entre ellos ChatDev, MetaGPT y Magentic-One, y armó una taxonomía de catorce modos de falla.

Un ejemplo de la segunda categoría, para contarlo sin imagen: el agente que maneja el teléfono lee en la documentación que el usuario es el número de teléfono, falla el login y le pide credenciales nuevas al orquestador sin contarle lo que aprendió. El orquestador tampoco pregunta. Repiten logins fallidos.

Dos conclusiones del paper. Las fallas entre agentes no se arreglan con un protocolo de mensajes común: los agentes no modelan qué necesita saber el otro. Y tener un verificador ayuda pero no alcanza, si verifica cosas superficiales como que el código compile.

Agentless, en una línea, como recordatorio de la lámina 2.3: un pipeline fijo, sin agente que decida el próximo paso, resolvió el 32% de SWE-bench Lite (issues reales de GitHub) a 0,70 dólares por problema, más que todos los agentes de código abierto de ese momento.

---

## 3. El aislamiento hay que configurarlo

### Content

En un handoff o en un fork, el agente que recibe hereda la conversación por defecto. El aislamiento entre agentes hay que pedirlo.

- **OpenAI Agents SDK** En un handoff, el agente que recibe ve todo el historial anterior. Se recorta con un `input_filter`.
- **LangGraph Swarm** El handoff pasa el historial completo, y todos los agentes escriben en una sola lista de mensajes. Se aísla con un esquema de estado propio por agente.
- **Claude Code** Un subagente arranca con una ventana limpia; un *fork* hereda la conversación entera y pierde ese aislamiento.

### Sources

- `corpus/openai-agents-sdk-handoffs.web.md` — "When a handoff occurs, it's as though the new agent takes over the conversation, and gets to see the entire previous conversation history"; `input_filter`; handoffs como tools `transfer_to_<agent_name>`.
- `corpus/langgraph-swarm.web.md` — "by default `create_handoff_tool` passes **full** message history"; "messages from **all** of the agents will be combined into a single, shared list of messages"; esquema de estado separado para aislar.
- `corpus/claude-code-subagents.web.md` — "Each subagent starts with a fresh, isolated context window"; un fork "inherits the entire conversation so far instead of starting fresh. This drops the input isolation that subagents otherwise provide". Documentación capturada el 2026-10-04; el registro marca que los valores por defecto cambian entre versiones.
- `corpus/sistemas-multiagente-clase.md.md` — lámina 7.2 del deck hermano, "El aislamiento no viene de fábrica" (selección de los tres casos).

### Speaker notes

La palanca de aislamiento de la lámina 6.4 es la que los frameworks no dan solos. Para verificarlo, revisar en los logs qué contexto recibe cada agente: si ve el historial de todos, no está aislado, aunque tenga su propio prompt.

En el Agents SDK y en LangGraph Swarm el handoff funciona como en la lámina 7.5: el agente que recibe toma la conversación entera. LangGraph Swarm es una biblioteca de LangGraph para handoffs; el Swarm de OpenAI que menciona la lámina 7.5 es otro proyecto, ya reemplazado por el Agents SDK. En Claude Code el subagente arranca limpio por defecto, y el fork es más barato porque comparte el caché del prompt del padre, pero hereda la conversación entera.

La lámina siguiente trae la posición contraria. Cognition pide compartir la traza completa entre agentes, justo lo que este aislamiento corta.

---

## 4. El debate: ¿construir multiagentes?

### Content

| | Cognition | Anthropic |
|---|---|---|
| Publicación | 12 jun 2025 | 13 jun 2025 |
| Posición | "Don't Build Multi-Agents": un solo hilo con contexto continuo | A favor del multiagente, para investigación |
| Argumento | Las acciones llevan decisiones implícitas; si los agentes no comparten la traza completa, sus decisiones chocan | Cada subagente comprime en su propia ventana; repartir permite gastar los tokens que el problema pide |
| Evidencia | Principios y un ejemplo, sin números | Eval interna: "outperformed single-agent Claude Opus 4 by 90.2%" |
| Dominio | Agentes de código (Devin) | Claude Research |

### Sources

- `corpus/cognition-dont-build-multi-agents.web.md` — Walden Yan, Cognition, fecha "06.12.25" = 12 jun 2025; dos principios ("Share context, and share full agent traces, not just individual messages"; "Actions carry implicit decisions, and conflicting decisions carry bad results"); single-threaded linear agent; ensayo de opinión sin evidencia cuantitativa.
- `corpus/anthropic-multi-agent-research-system.web.md` — publicado 13 jun 2025; "outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval" (el registro marca que no dice si es mejora relativa o puntos porcentuales; se cita tal como está escrito); "The essence of search is compression"; "Multi-agent systems work mainly because they help spend enough tokens to solve the problem".
- `corpus/orquestacion-de-agentes-clase.md.md` — Cut material, lámina "La misma figura, dos veredictos" (par Cognition / Anthropic con fechas y tipo de evidencia).

### Speaker notes

Dos equipos serios publicaron con un día de diferencia conclusiones opuestas sobre la misma arquitectura. No hay respuesta de uno al otro.

Leer los principios de Cognition en su versión original: "Share context, and share full agent traces, not just individual messages" y "Actions carry implicit decisions, and conflicting decisions carry bad results". Su alternativa es un agente de un solo hilo; para tareas muy largas, agrega un LLM que comprime el historial, y admite que es difícil hacerlo bien.

Sobre el 90,2% de Anthropic: el post no aclara si es una mejora relativa o en puntos porcentuales, ni el tamaño de la eval. Se cita tal como está escrito, entre comillas, y no como "90% más preciso". La configuración era Claude Opus 4 como orquestador y Claude Sonnet 4 como subagentes; son modelos de mediados de 2025.

Las dos son empresas que venden el producto que describen. Aun así el desacuerdo es real, y las dos láminas siguientes muestran que se resuelve con una variable concreta. LangChain, siete meses después, toma una posición intermedia: empezar con un agente y repartir solo cuando aparece un límite claro.

Cognition también describe los subagentes de Claude Code "a junio de 2025" (no trabajan en paralelo, responden preguntas puntuales); es una descripción fechada y puede no valer hoy.

---

## 5. Compartir el contexto no alcanza

### Content

Aun con todo el contexto del orquestador, cada subagente sigue sin ver el trabajo de su hermano. Los dos toman decisiones que el otro no conoce, y el choque aparece al combinar.

![Cada subagente hereda el contexto del orquestador pero no el de su hermano](images/s9-5-1-contexto-no-compartido.png)
<!-- ascii-source:
                       Tarea
                         |
                         v
          +------------------------------+
          | Orquestador: divide la tarea |   [G]
          +------------------------------+
                |                  |
                v                  v
       +--------------+    +--------------+
       | Subagente 1  |    | Subagente 2  |
       +--------------+    +--------------+
          [G] [B1]            [G] [B2]
                |                  |
                v                  v
          +------------------------------+
          |  Orquestador: combina        |   [G] [B1] [B2] [P]
          +------------------------------+
                         |
                         v
                     Resultado

  [G] contexto del orquestador   [B1] [B2] trabajo de cada subtarea
  [P] trabajo de combinación
-->
<!-- ascii-note:
intent: cada subagente hereda el contexto del orquestador pero no ve el de su hermano; la pila de fichas junto a cada caja es lo que ese agente puede ver.
emphasize: que Subagente 1 tiene [G][B1] y NO [B2], y Subagente 2 tiene [G][B2] y NO [B1] (acento rojo en las fichas ausentes); la pila completa aparece recien en la caja que combina.
labels: leyenda [G] [B1] [B2] [P] al pie.
-->

`Cognition, jun-2025`

### Sources

- `corpus/cognition-dont-build-multi-agents.web.md` — ejemplo Flappy Bird; con contexto compartido, el pájaro y el fondo salen en "completely different visual styles" porque los subagentes no ven el trabajo del otro; principios 1 y 2.
- `corpus/orquestacion-de-agentes-clase.md.md` — lámina 2.3 "Compartir el contexto no alcanza", diagrama de pilas de fichas (fuente ASCII reutilizada y traducida).

### Speaker notes

El ejemplo de Cognition, contado en voz alta: la tarea es clonar Flappy Bird. Un subagente hace el fondo con los caños verdes, el otro hace el pájaro. Sin contexto compartido, el primero entiende mal y hace un fondo estilo Super Mario Bros, y el segundo hace un pájaro que no se mueve como el de Flappy Bird. Con todo el contexto compartido, igual salen en estilos visuales distintos, porque ninguno vio lo que decidía el otro.

Leer las pilas de fichas: el subagente 1 tiene el contexto del orquestador y su propio trabajo, nada del hermano; el subagente 2, al revés. La pila completa aparece recién en la caja que combina, que es donde se descubre el problema.

---

## 6. ¿El trabajo lee o escribe?

### Content

- **El trabajo lee** Investigación, búsqueda, lectura de fuentes. Dos subagentes que leen cosas distintas no se pisan y devuelven un hallazgo. Repartir paga.
- **El trabajo escribe sobre algo compartido** Código, un mismo documento, una misma base. Cada acción cambia el terreno del otro: un solo hilo, o límites explícitos entre quienes escriben.

> "most coding tasks involve fewer truly parallelizable tasks than research, and LLM agents are not yet great at coordinating and delegating to other agents in real time"
> — Anthropic, jun-2025

### Sources

- `corpus/anthropic-multi-agent-research-system.web.md` — límite del dominio, verbatim; buen encaje: "valuable tasks that involve heavy parallelization, information that exceeds single context windows, and interfacing with numerous complex tools"; mal encaje: dominios donde todos los agentes necesitan el mismo contexto o con muchas dependencias entre agentes; reglas de esfuerzo (1 agente con 3 a 10 llamadas a tools; 2 a 4 subagentes con 10 a 15 llamadas cada uno; más de 10 subagentes para investigación compleja).
- `corpus/cognition-dont-build-multi-agents.web.md` — el dominio de Cognition es código, donde las acciones cambian estado compartido.
- `corpus/orquestacion-de-agentes-clase.md.md` — lámina 2.4 "Cuándo repartir, y cuándo no".

### Speaker notes

Esta lámina resuelve el debate. Cognition y Anthropic no discuten la forma de la arquitectura; discuten si los hermanos necesitan verse. En investigación de solo lectura no hace falta, y el sistema de Anthropic está armado así. En código que modifica un mismo repositorio sí hace falta, y ese es el dominio de Cognition.

La pregunta que la sala se lleva para sus propios casos: el trabajo que quiero repartir, ¿lee o escribe?

Si preguntan por el caso intermedio, repartir escritura sobre archivos distintos: funciona mientras los límites estén escritos de antemano y nadie los cruce. Anthropic sugiere además que cada subagente escriba su salida en un archivo y devuelva solo una referencia liviana.

Para dimensionar, las reglas de esfuerzo que Anthropic le enseña a su orquestador: una búsqueda simple es un agente con 3 a 10 llamadas a tools; una comparación directa, 2 a 4 subagentes con 10 a 15 llamadas cada uno; una investigación compleja, más de 10 subagentes. Un error temprano de su sistema fue crear 50 subagentes para preguntas simples.

---

## 7. Un caso: cómo se descompone

### Content

Pedido: "Pagá el crédito del auto con la plata de mi caja de ahorro".

![Un caso de descomposición en subagentes](images/s9-7-1-caso-descomposicion.png)
<!-- ascii-source:
              +-----------------------------+
              |  Orquestador: descompone    |
              +-----------------------------+
                  |                     |
                  v    en paralelo      v
        +-----------------+   +---------------------+
        |   Loan Agent    |   | Transaction Manager |
        |  cotiza saldo   |   |  verifica fondos    |
        |     (lee)       |   |       (lee)         |
        +-----------------+   +---------------------+
                  |                     |
                  v                     v
              +-----------------------------+
              |  Orquestador: valida        | --- no cierra ---&gt; replanifica
              +-----------------------------+
                             |
                             v  cierra
              +-----------------------------+
              |  Payment Processor          |
              |  transfiere (escribe)       |
              +-----------------------------+
-->
<!-- ascii-note:
intent: el caso aplica la regla de la lamina anterior; dos lecturas en paralelo, validacion, y la unica escritura sola y al final.
emphasize: la caja Payment Processor en rojo (la unica que escribe); la bifurcacion en paralelo de las dos lecturas.
labels: Orquestador (descompone / valida), Loan Agent, Transaction Manager, Payment Processor, lee / escribe, replanifica.
-->

`Kore.ai, oct-2025 (act. jul-2026)`

### Sources

- `corpus/koreai-orchestration-patterns.web.md` — ejemplo Supervisor "loan payoff in banking", pasos 1 a 8: descomposición en cuatro acciones, tres agentes, datos mínimos por agente, Loan Agent y Transaction Manager en paralelo, validación, replanificación, registro para auditoría.
- `corpus/orquestacion-de-agentes-clase.md.md` — lámina 2.9 "Un caso: cómo se descompone" y su lectura (dos lecturas en paralelo, la escritura sola y al final).

### Speaker notes

**Original:** "Pay off my car loan using my savings account." — [Kore.ai](https://www.kore.ai/blog/choosing-the-right-orchestration-pattern-for-multi-agent-systems).

Kore.ai lo presenta como ejemplo de su patrón Supervisor, con un orquestador central. Reparte dos lecturas en paralelo, que no se pisan, y deja la única escritura, la transferencia, sola y al final, después de validar. Es la regla de la lámina anterior aplicada.

El orquestador descompone el pedido en cuatro acciones: cotizar el saldo, verificar los fondos, transferir y confirmar. El Loan Agent cotiza saldo, interés y penalidades. El Transaction Manager verifica saldo, límites diarios y umbrales de fraude. Si algo no cierra, el orquestador replanifica.

Cada agente recibe solo los datos que necesita, enmascarados o seudonimizados, y la transacción queda registrada para auditoría.

Es material de un proveedor, sin implementación ni cliente citado. Sirve como ejercicio de descomposición.

Cierre de la sección 9. Tiempo acumulado: unos 126 minutos; con las conclusiones, unos 131.

---

# Conclusions

## 1. Lo que queda de la clase

### Content

1. **Agente** Percibe su ambiente y actúa sobre él. Un LLM se vuelve agente cuando elige acciones en un loop según lo que observa.
2. **Tools** Funciones descriptas en el contexto que el LLM pide y el programa ejecuta. Se diseñan para quien las llama, que no es determinístico.
3. **Tipos de agente** Cuatro cambian cuándo se planifica y cuántas veces vuelve a razonar el LLM: ReAct paso a paso, Plan-and-Execute y ReWOO con plan previo, Reflexion con crítica entre intentos. El quinto, orquestador con workers, es la forma básica del multiagente.
4. **Multiagente** Reparte el contexto entre varios loops para especializar, aislar y paralelizar. Conviene cuando la información no entra en uno y el trabajo lee más de lo que escribe.
5. **Empezar simple** Un agente con buenas tools antes que varios agentes.

### Sources

- `corpus/AIG4B-Clase-6-Agent.pptx.md` · `corpus/wikipedia-intelligent-agent.web.md` · `corpus/yao-2022-react.pdf.md` — definición y formalización (secciones 1 y 2).
- `corpus/anthropic-writing-tools-for-agents.web.md` — tools (sección 3).
- `corpus/langchain-planning-agents.web.md` · `corpus/shinn-2023-reflexion.pdf.md` · `corpus/react-repo-hotpotqa-prompt.md.md` — tipos (secciones 4 y 5).
- `corpus/anthropic-context-engineering.web.md` · `corpus/anthropic-multi-agent-research-system.web.md` · `corpus/cognition-dont-build-multi-agents.web.md` · `corpus/langchain-multi-agent-architectures.web.md` · `corpus/mast-why-mas-fail-2025.web.md` — multiagente, sus tres palancas y "Add tools before adding agents" (secciones 6 a 9).

### Speaker notes

Una idea por bloque de la clase, más la regla que las ordena. Leerlas en voz alta y pedirle a la sala que diga, para cada una, en qué lámina apareció.

La quinta es la que conviene repetir: las tres fuentes más serias de la clase (Anthropic, LangChain y, desde la otra vereda, Cognition) coinciden en empezar por lo más simple que alcanza.

---

## 2. Cómo elegir la arquitectura

### Content

![Árbol de decisión para elegir la arquitectura](images/sc-2-1-arbol-decision.png)
<!-- ascii-source:
 ¿Alcanza una llamada al LLM, con RAG o ejemplos?
   |-- sí --&gt; una llamada; sin agente
   no
   v
 ¿Los pasos se conocen de antemano?
   |-- sí --&gt; workflow: pasos fijos en código
   no
   v
 Un agente con buenas tools
 (ReAct; planificar o reflexionar si la tarea lo pide;
 skills si tiene muchas especializaciones)
   |
   v
 ¿La información no entra en un contexto, hay equipos
 dueños de dominios distintos, o el trabajo se reparte
 en lecturas paralelas que valen ~15× tokens?
   |-- no --&gt; quedarse con un agente
   sí
   v
 Multiagente: subagents, handoffs, router
 (o red adaptativa, pipeline, pizarra, jerarquía)
-->
<!-- ascii-note:
intent: arbol de decision que resume la clase; cada pregunta descarta la opcion mas compleja si la simple alcanza.
emphasize: la hoja "Multiagente" en rojo, al final del camino mas largo; las salidas laterales "si" / "no" que cortan antes.
labels: las cuatro preguntas y sus salidas.
-->

### Sources

- `corpus/anthropic-building-effective-agents.web.md` — "optimizing single LLM calls with retrieval and in-context examples is usually enough"; workflows para tareas bien definidas; agentes cuando hace falta flexibilidad.
- `corpus/langchain-multi-agent-architectures.web.md` — las dos restricciones (contexto y desarrollo distribuido); "Add tools before adding agents".
- `corpus/anthropic-multi-agent-research-system.web.md` — ~15× tokens para multiagente; buen encaje en tareas con mucha paralelización e información que excede una ventana de contexto.

### Speaker notes

Recorrer el árbol con un caso que proponga la sala. Lo habitual es que la mayoría de los casos se detenga en la segunda o tercera pregunta.

La tercera pregunta junta las dos restricciones de LangChain con el criterio de Anthropic. Si ninguna se cumple, repartir solo agrega llamadas y tokens.

Skills quedó en la rama de un agente porque LangChain lo cuenta como cuasi multiagente: hay un solo agente (lámina 7.4).

Si se llega a la última hoja, volver a la tabla de la lámina 7.7 para elegir el patrón, a las 7.9 y 7.10 para las otras topologías, y a la 9.6 para decidir si el trabajo se puede repartir sin que los agentes se pisen.

---

## 3. Para leer después

### Content

- **ReAct** [Yao et al., 2022, *ReAct: Synergizing Reasoning and Acting in Language Models*](https://arxiv.org/abs/2210.03629)
- **Reflexion** [Shinn et al., 2023, *Reflexion: Language Agents with Verbal Reinforcement Learning*](https://arxiv.org/abs/2303.11366)
- **Agentes y workflows** [Anthropic, *Building effective agents*](https://www.anthropic.com/engineering/building-effective-agents)
- **Tools** [Anthropic, *Writing effective tools for agents*](https://www.anthropic.com/engineering/writing-tools-for-agents)
- **Agentes con planificación** [LangChain, *Plan-and-Execute Agents*](https://www.langchain.com/blog/planning-agents)
- **Patrones multiagente** [LangChain, *Choosing the Right Multi-Agent Architecture*](https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture)
- **El debate** [Anthropic, *How we built our multi-agent research system*](https://www.anthropic.com/engineering/multi-agent-research-system) y [Cognition, *Don't Build Multi-Agents*](https://cognition.com/blog/dont-build-multi-agents)
- **Panorama** [Lilian Weng, *LLM Powered Autonomous Agents*](https://lilianweng.github.io/posts/2023-06-23-agent/)
- **Contexto** [Anthropic, *Effective context engineering for AI agents*](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- **Cómo fallan** [Cemri et al., 2025, *Why Do Multi-Agent LLM Systems Fail?*](https://arxiv.org/abs/2503.13657)

### Sources

- URLs de los registros: `corpus/yao-2022-react.pdf.md` (arXiv 2210.03629), `corpus/shinn-2023-reflexion.pdf.md` (arXiv 2303.11366), `corpus/anthropic-building-effective-agents.web.md`, `corpus/anthropic-writing-tools-for-agents.web.md`, `corpus/langchain-planning-agents.web.md`, `corpus/langchain-multi-agent-architectures.web.md`, `corpus/anthropic-multi-agent-research-system.web.md`, `corpus/cognition-dont-build-multi-agents.web.md`, `corpus/lilianweng-llm-powered-agents.web.md`, `corpus/anthropic-context-engineering.web.md`, `corpus/mast-why-mas-fail-2025.web.md` (arXiv 2503.13657).

### Speaker notes

Si hay que elegir una sola lectura, la de LangChain sobre patrones multiagente: es corta y tiene las tablas de costo. Si hay que elegir un paper, ReAct: su sección 2 entra en una página y es la base de todo lo demás. El repositorio github.com/ysymyth/ReAct tiene el notebook con el prompt de las láminas 4.4 y 4.5.

Para la definición clásica, el libro de Russell & Norvig, *Artificial Intelligence: A Modern Approach* (4.ª edición, Pearson, 2020).

Dejar tiempo para preguntas.

---

# Open questions

- Slide 5.11: la fila "Multiagente (orquestador + workers)" llegó sin descripción en la tabla del presentador. El editor completó "Cómo funciona" y "Cuándo conviene" desde `corpus/anthropic-building-effective-agents.web.md` y `corpus/anthropic-multi-agent-research-system.web.md`. Confirmar o reescribir.
- Slide 5.2: el ejemplo de Plan-and-Execute es una construcción de la cátedra sobre la pregunta de HotpotQA de 4.3; el corpus no tiene una traza publicada de este tipo. Está marcado así en la lámina, en Sources y en notas. Confirmar que el presentador lo quiere o proponer otro caso.
- Slide 5.9: Anthropic clasifica orchestrator-workers como workflow. La lámina agrega que, cuando cada worker es un agente con su propio loop, el worker es un subagente y el conjunto es la forma básica de un sistema multiagente (definido en 6.4); las notas lo cuentan como tipo de agente con la lectura del espectro del deck del curso (slide 33), atribuida a la cátedra.
- Slides 7.3, 7.4, 7.5 y 7.6 citan imágenes de `corpus/langchain-multi-agent-architectures.web.md` que siguen como stub `<!-- pending: process_images -->`. El editor verificó su contenido a la vista; re-verificar después de librarian Phase 2 si se corre.
- Slides 7.3–7.6: los cuatro patrones usan las imágenes de LangChain (estilo dibujado a mano), y el resto de la sección 7 usa diagramas ASCII que se renderizan en Polish. L1 pide consistencia visual dentro de una sección. Opciones: dejar las imágenes de LangChain (son el material del artículo que el presentador pidió cubrir) o redibujar los cuatro patrones en ASCII con la gramática de la sección.
- Slide 7.8: corrección numérica. El texto del artículo de LangChain dice "40-50%" de llamadas ahorradas y "67% fewer tokens"; sus propias tablas dan 37,5% (8 → 5, redondeado a 40%) y 40% menos (~9K contra ~15K). La lámina usa los valores de las tablas y las notas explican la diferencia.
- Slide 9.4: "outperformed single-agent Claude Opus 4 by 90.2%" (`corpus/anthropic-multi-agent-research-system.web.md`) no aclara si es mejora relativa o en puntos porcentuales. Se cita verbatim, en inglés y entre comillas.
- Slide 5.7: la aceleración de "3,6×" de LLMCompiler que menciona `corpus/langchain-planning-agents.web.md` no está verificada contra el paper. Quedó solo en notas, atribuida al paper.
- Slides 4.7 y 5.6: las cifras de ReAct (PaLM-540B, 2022–23) y Reflexion (GPT-4 como estado del arte de 2023) están fechadas en lámina y en notas. Confirmar que el presentador quiere mostrar cifras de modelos históricos.
- Slide 7.9: la correspondencia red adaptativa ≈ handoffs es lectura del editor (el registro de Kore.ai lo marca así); va solo en notas y dicha como lectura de la cátedra.
- Slide 9.4: los nombres de modelo (Claude Opus 4, Claude Sonnet 4) son de junio de 2025 y la descripción de los subagentes de Claude Code que hace Cognition está fechada "a junio de 2025". Van en notas como datos fechados.
- Slide 9.4: el debate Cognition vs Anthropic fue cortado del deck previo a pedido del presentador ("Ni lo mencionemos"); en esta clase se incluye por indicación del orquestador. El presentador puede cortarlo en Review (9.4 y 9.5 se sostienen juntas; 9.6 funciona sola).
- Slide 3.1: la sección no repite el circuito de tool calling que la clase de entrenamiento de LLMs pudo haber mostrado (SFT que enseña a emitir llamadas a tools). Si el presentador quiere el puente explícito, no hay registro en este corpus que lo respalde.
- Slides 4.4 y 4.5 (prompt de ReAct): la instrucción y el loop salen del notebook `hotpotqa.ipynb` de github.com/ysymyth/ReAct, que corre GPT-3 text-davinci-002; las tablas principales del paper son con PaLM-540B. Quedan abiertos en `corpus/react-repo-hotpotqa-prompt.md.md` el texto exacto que devuelve `env.reset()` (la lámina 4.5 muestra "Question:" siguiendo el formato de los ejemplos) y si el repositorio es el código oficial (el paper apunta a react-lm.github.io).
- Slide 1.7: la sigla PEAS y su expansión vienen del capítulo 2 de Russell & Norvig, que no está en el corpus; los registros del deck del curso hablan de formulaciones "PEAS-like". Capturar el capítulo 2 si se quiere cita.
- Slide 1.6: `corpus/wikipedia-intelligent-agent.web.md` dice que Russell & Norvig agrupan los agentes en cinco clases; algunas ediciones presentan cuatro programas más el agente que aprende. La lámina muestra los cinco como lista; las notas lo aclaran.
- Slide 1.5: el termostato como regla condición-acción sale de Wikipedia, que lo cita a un blog y a IBM; se usa sin atribuírselo a Russell & Norvig.
- Slides 7.10 y 8.1: MetaGPT se nombra en 7.10 como ejemplo de pipeline y de pizarra; su mecanismo (línea de montaje, pool de mensajes) se cuenta solo en 8.1. La clasificación de ChatDev según MAST va solo en las notas de 8.1.
- Slide 8.1: MetaGPT y ChatDev reportan cada uno que le gana al otro, en su propio dataset; las notas lo dicen. Las cifras de los cuatro sistemas son de 2023–24 y de los papers de cada uno, no de un benchmark común. El 54%/69% de AutoGen en ALFWorld (promedio, GPT-3.5-turbo) y el 71% de ReAct en 4.7 (mejor de 6, PaLM-540B) no se comparan; las notas de 8.1 lo dicen.
- Slide 8.2: debate y Mixture-of-Agents quedan como contraste (varios LLM sin tools, que con la definición de la clase no forman un sistema multiagente). Los papers llaman "agentes" a cada instancia; la lámina lo dice. Confirmar que el presentador quiere conservar la lámina con ese encuadre.
- Slides 7.10 y 9.3: los datos de Claude Code (anidamiento de subagentes hasta tres niveles, aislamiento del subagente, fork que hereda la conversación) son de la documentación capturada el 2026-10-04 y cambiaron entre versiones. Re-verificar antes del 2026-10-07.
- Slide 9.2: el rango 41%–86,7% de MAST está en el texto del paper, pero viene de la Figura 5, que no se capturó. Los totales por categoría (44,2 / 32,35 / 23,5) son sumas de los modos de §4 y suman 100,05% por redondeo.
- Slide 2.2: la frase "la memoria queda fuera de esta clase" bajó a la línea de fuente al pie de la lámina (L9). Si el render la muestra como cita y no como nota, pasarla a las notas del orador.
- Merge con `talks/sistemas-multiagente` (deck hermano, `corpus/sistemas-multiagente-clase.md.md`): se tomaron conceptos, no láminas, y cada cifra se rastreó al registro que el deck hermano cita. No se usó su caso ficticio Pampa Viajes: esta clase ya tiene sus casos (la pregunta de HotpotQA, el crédito de Kore.ai), y recorrer siete arquitecturas con un caso propio costaba unas diez láminas. Su lámina 1.12 dibuja la acción de ReAct como llamada a tool; esta clase explica el original de completado con stop (4.4 y 4.5) y el tool calling moderno en las notas de 4.6. Su diagrama de handoffs que termina en un agente de presupuesto sin LLM no se trajo.
- Candidatos del deck hermano que quedaron fuera y el presentador puede sumar: MCP (fuera de alcance por el briefing); memoria de agentes (Mem0, Zep, persistencia de LangGraph, memoria de LangChain; fuera de alcance); el trabajo práctico de su Conclusiones 2; la demo en vivo con Claude Code (DESIGN-AGENT, CODE-AGENT, OUTREACH-AGENT); equipos de agentes y mensajes entre sesiones de Claude Code; su sección 5, "El agente principal que delega bajo demanda" (lo esencial, el sistema de Anthropic y Cognition, ya está en 9.1 y 9.4–9.6); la tabla de siete dimensiones del ambiente con cuatro ambientes clasificados (esta clase cortó "Tipos de ambiente" en Step 4); la ficha PEAS de cuatro agentes (robot móvil, AlphaGo, taxi); omnisciencia y autonomía como lámina propia (quedaron en las notas de 1.6); Generative Agents como lámina propia (quedó en las notas de 7.9); la tabla del Agents SDK de OpenAI (quedó en las notas de 7.3 y 7.5); "Dónde coinciden" Anthropic y Cognition (lo cubre 9.6).

**Composer, revisión scope=full del 2026-10-04: [minor] diferidos a Step 5 que siguen abiertos** (locators en la numeración actual; los de 4.1/5.11, 4.1 contra 3.1, 7.2 contra 7.3 y Timing quedaron resueltos en la ronda de consistencia):

- [minor] Slide 7.8 (densidad): párrafo de entrada, tabla de 4×5 y una línea de conclusión rodean la tabla. Sugerencia: pasar la descripción de los escenarios a los encabezados de columna o a las notas.
- [minor] Títulos de más de 40 caracteres: 1.4 (42), 3.2 (44) y 5.4 (41). Sugerencia: quedarse con la cláusula de la derecha.
- [minor] Notas de más de ~120 palabras en 2.3, 4.7, 7.8, 9.4 y 9.6 (sobre todo apartes del tipo "si preguntan"). Las de 2.3 se acortaron en esta ronda al sacar el espectro del deck del curso. Sugerencia: recortar los apartes o partir la lámina si son dos ideas.
- [minor] Conclusions.3: el mazo termina en una lista de lecturas, y la imagen de cierre es el árbol de conclusions.2. Sugerencia: intercambiarlas o pasar la lista a las notas o a un handout.

# Cut material

- **pptx slides 9–11 (Robot móvil, AlphaGo, AlphaGo → AlphaZero)** — ejemplos de formulación PEAS. La lámina 1.7 usa la aspiradora y el agente LLM, que alcanzan para mostrar la plantilla; los otros tres repetían la misma forma.
- **pptx slide 13 (Dificultad de ambientes: crucigrama / ajedrez / taxi)** — estaba en las notas de la lámina "Tipos de ambiente", que se cortó (ver abajo).
- **pptx slide 14 (¿Por qué todas estas definiciones?: análisis riguroso, reutilización de frameworks, decisión informada)** — el tercer punto queda cubierto por 2.4; los otros dos no sostienen la tesis de esta clase.
- **pptx slide 19 (Valor de un LLM en un agente: observar lenguaje natural, usar herramientas con lenguaje, reflexionar sobre outputs, instruir sistemas complejos)** — se superpone con 1.7 (actuadores y sensores del agente LLM) y con Reflexion en 5.4.
- **pptx slide 22 (Componentes: Memoria y Contexto, Tools, Información contextual RAG)** — reemplazado por la descomposición de Weng en 2.2; la línea de tools se usa en 3.1.
- **pptx slides 29–30 (Limitaciones de un solo agente; ejemplo clínico NSCLC)** — la cifra de selección de tools (~92% con 5 tools → ~58% con 20+) no tiene fuente (registro: [open question]); el ejemplo es del curso de biomedicina. Las dos restricciones de LangChain (6.5) cubren la motivación.
- **pptx slides 24–26 (producción, MCP) y 35–39 (memoria)** — fuera de alcance por indicación del presentador.
- **LangChain, Table 2 (estrellas por requisito) y Table 6 (resumen de desempeño)** — tercera y cuarta tabla del artículo; mencionadas en notas de 7.8. Con Table 1 y las tablas de escenarios alcanza para decidir.
- **Kore.ai, tabla de decisión Supervisor / Red adaptativa / Custom (figura `implementation-recomendation.webp`)** — sus valores salen de una imagen que en este corpus está sin transcribir; la transcripción existe en `corpus/orquestacion-de-agentes-clase.md.md` (lámina 2.8). Las notas de 7.10 usan el texto de Kore.ai (Use / Avoid).
- **Deck previo de orquestación: tres niveles de gestión de agentes, cambio de modelo mental, la Task como unidad de gobierno, audit trail, seis decisiones para armar una compañía** — conceptos ligados a Paperclip y a la gobernanza; fuera del alcance que pidió el presentador para esta clase.
- **Anthropic multi-agent research: ocho principios de prompting, evaluación con LLM-as-judge, rainbow deployments, Citation agent** — material de producción; no sostiene la tesis.
- **LLMCompiler como tipo propio** — queda como mención en las notas de 5.7.
- **Weng: Tree of Thoughts, LLM+P, Chain of Hindsight, Algorithm Distillation, Generative Agents, HuggingGPT, MRKL** — panorama de 2023 más amplio que la clase.
- **Cognition: agente lineal con LLM compresor de historial (y su figura de desborde de contexto)** — mencionado en notas de 9.4.
- **Lámina "Tipos de ambiente" de la sección 1 (cortada entera en Step 4, major del Composer)** — de las siete dimensiones solo una sostiene la tesis; esa dimensión (un agente o varios) pasó a las notas de 1.7. Contenido cortado, verbatim:
  - Lead: "La forma del ambiente decide cuán difícil es el agente que hace falta."
  - Observabilidad: completamente observable o parcialmente observable. Cantidad de agentes: un solo agente o multiagente. Determinismo: determinístico o estocástico. Episódico o secuencial: acciones independientes, o acciones con consecuencias a largo plazo. Estático o dinámico: el ambiente cambia, o no, mientras el agente delibera. Discreto o continuo: estados y acciones finitos, o infinitos. Conocido o desconocido: el agente conoce, o no, las reglas del ambiente.
  - Notas: escala del deck original (crucigrama fácil; ajedrez medio; taxi autónomo difícil: parcialmente observable, estocástico, dinámico, continuo, multiagente). Sources: `corpus/AIG4B-Clase-6-Agent.pptx.md` slides 12 y 13. La frase sobre el ambiente del agente LLM pasó a las notas de 1.7.
- **Lámina 2.4 (hoy 2.2), bullet "Memoria"** — "De corto plazo, lo que está en el contexto. De largo plazo, un almacén externo con recuperación rápida." Fuera de alcance por indicación del presentador; la lámina deja una sola línea que dice que la memoria queda fuera de esta clase. También salió "memoria" del título ("Agente = LLM + planificación + memoria + tools") y de las notas la frase "Basta con la distinción de corto y largo plazo: el contexto es memoria de corto plazo y se pierde entre corridas; lo que tiene que durar se escribe afuera."
- **Lámina 7.1, bullet "Fan-out y fan-in"** — "El agente principal reparte subtareas y después junta los resultados." Repetía la definición de 5.9 (L6); quedó un puntero a 5.9.
- **Lámina 7.4 (hoy 7.3), bullet "Cómo funciona"** — "El agente principal decide a qué subagentes invocar, con qué entrada, y cómo combinar los resultados. Puede invocar varios en paralelo." Repetía 5.9 (L6); la lámina queda con lo propio del patrón (estado, costo) y el paralelismo pasó a las notas.
- **Lámina 9.4, celda Posición de Anthropic** — "Orchestrator-worker con subagentes en paralelo". Repetía 5.9 y 5.10; ahora dice "A favor del multiagente, para investigación". La celda Dominio pasó de "Investigación (Claude Research)" a "Claude Research".
- **Lámina 7.10, tabla Supervisor / Red adaptativa (Control, Conviene, Evitar)** — la lámina tenía diagrama y tabla; la tabla pasó completa a las notas de 7.10; en la ronda de consistencia la mitad Supervisor se cortó (ver abajo) y la mitad Red adaptativa quedó en las notas de 7.9.
- **Lámina 9.7, cuatro pasos numerados** — reemplazados en la lámina por un diagrama ASCII; el texto de los pasos pasó a las notas de 9.7 y en la ronda de consistencia se resumió (ver abajo).
- **Lámina 7.10, notas: "El deck del curso agregaba un tercer caso, el jerárquico: un supervisor de supervisores, para sistemas muy grandes."** — la jerarquía pasó a tener su card en la lámina 7.11 (hoy 7.10) (Review reabierta, ronda 1); la nota quedó como puntero.

**Ronda de consistencia y repetición (Review reabierta, 2026-10-04).** Pedido del presentador: "Solo que sea consistente" y "que no se esté dando contenido repetido".

- **Lámina 4.1 "El loop común", pasos numerados** — "1. **Proponer** El LLM genera texto para el usuario o una llamada a una función. 2. **Ejecutar** El programa invoca el software: una consulta a una base, una llamada a una API. 3. **Observar** El resultado vuelve al LLM, que llama a otra función o responde." Repetían el loop de 3.1 (L6). La lámina pasó a "Dos preguntas para cada tipo" con un puntero a 3.1. De sus notas salió la lista de respuestas de cada tipo a las dos preguntas, que ya está en las notas de 5.11.
- **Lámina 4.2 "ReAct: pensar, actuar, observar" (versión anterior)** — lead "ReAct intercala pensamientos y acciones, un paso por vez, hasta tener lo necesario para responder." y diagrama de lazo Pregunta → Thought (razonar) → Action (usar tool) → Observation (resultado) → vuelta, con salida "cuando alcanza" a la Respuesta final. ReAct se presentaba dos veces (2.2 y 4.2): la lámina 2.2 "Pensar también es una acción" pasó a ser la 4.2 con su diagrama de bifurcación, el lead absorbió la frase de intercalar y el lazo se retiró. Sus notas ("dense thought", la cita del deck del curso, slide 20) pasaron a la nueva 4.2.
- **Lámina 2.2 (hoy 4.2), card "Para qué sirve pensar"** — "Descomponer la tarea, extraer lo importante de una observación, seguir el progreso, manejar excepciones y ajustar el plan." Las notas de 4.3 ya leen cada pensamiento de la trayectoria con esos usos; la lista quedó en las Sources de 4.3. De sus notas salió "La sección 4 vuelve a ReAct como primer tipo de agente, con la trayectoria completa. Acá alcanza con la forma." y la aclaración de que el paper no usa "tool" pasó a las notas de 2.1.
- **Lámina 2.3, notas: espectro del deck del curso (slide 33) y diferencia con la paralelización** — quedan solo en las notas de 5.9; la 2.3 deja un puntero.
- **Lámina 6.1, respuesta y distractor** — respuesta "B. Es finito, se llena y se paga por token. No persiste entre corridas: lo que tiene que durar se escribe afuera."; opción "C. Una base de datos donde el agente guarda lo que quiere recordar."; notas "C describe algo que existe, pero es otra cosa: escribir afuera es lo que se hace porque el contexto no alcanza." y "por eso el plan se escribe en una memoria externa antes de crear subagentes". Repetían la idea de memoria que la clase declara fuera de alcance (2.2). La lámina queda como recapitulación de "finito y se paga por token", con un distractor nuevo (C, solo el system prompt).
- **Lámina 1.7, celda Agente** — "memoria" salió de "LLM con razonamiento, memoria y acceso a herramientas externas"; la memoria está fuera de alcance.
- **Lámina 7.1, cards y notas anteriores** — "**Ventana propia** Ve solo lo que le pasa el agente que lo creó, y no ve lo que hace su hermano." "**Uno por subtarea** Es el worker del orquestador de la lámina 5.9." "**Hallazgos destilados** Devuelve un resultado comprimido, sin su historial completo." (repetía la palanca de aislamiento de 6.4). Notas: "Tres cosas, en este orden. Uno: cada subagente tiene su propia ventana, siempre. Dos: qué entra en esa ventana lo decide quien lo crea, desde un encargo de dos líneas hasta todo lo que el padre sabía. Tres: un subagente no ve lo que hace su hermano mientras trabaja." — hoy son las cards Encargo, Hermanos y Decisión. El acento rojo del diagrama pasó de "no se ven" a "ventana propia"; el remate de los hermanos lo da 9.5.
- **Lámina 7.2 "Qué es orquestar" (cortada entera)** — lead "Orquestar es decidir quién hace qué, en qué orden, con qué información y bajo qué límite de gasto." (pasó al lead de la hoy 7.2 "Cuatro patrones"). Cards de Kore.ai: "**Costo en tokens** Los patrones difieren en cuántas vueltas de razonamiento y capas de coordinación pagan." "**Latencia** Un control centralizado agrega demora, crítica en voz y tiempo real." "**Velocidad de desarrollo o control** Configurar es más rápido; programar la coordinación da más control." "**Escala y mantenimiento** Costo operativo y comportamiento bajo carga." Fuente `Kore.ai, oct-2025 (act. jul-2026)`. Notas: cita "the challenge shifts from building AI agents to coordinating them effectively"; "a veces más de 200%" de diferencia de tokens entre patrones, sin datos ni método; Kore.ai como material de proveedor. Era un tercer lente para leer los patrones; la clase usa uno solo, las tres palancas de 6.4 más los costos de 7.8.
- **Lámina "Cuatro patrones" (hoy 7.2)** — cola del lead "que difieren en cómo coordinan las tareas, cómo manejan el estado y cómo desbloquean pasos en secuencia" y notas "Para cada uno conviene preguntar tres cosas: quién decide a qué agente va el trabajo, dónde vive el estado y cuántas llamadas al modelo cuesta." Otro lente; reemplazado por las tres palancas de 6.4.
- **Lámina 7.10 (hoy 7.9) "Supervisor o red adaptativa", mitad Supervisor** — diagrama SUPERVISOR (Usuario → Orquestador → A, B, C; "todo pasa por el centro"), tercer dibujo de la misma estrella de 5.9 y 7.3. Notas: "El supervisor se parece a subagents y router: un nodo decide."; "el supervisor paga latencia y tokens en cada salto por el centro, y a cambio da un solo lugar donde mirar qué pasó. La red ahorra esos saltos y nadie tiene la foto completa." (condensado en la línea de trade-off de la lámina); "El supervisor centraliza el control: descompone, delega, valida y sintetiza. Conviene en workflows multidominio que piden supervisión y trazabilidad. Kore.ai lo desaconseja en tiempo real, con alta escala o con un presupuesto de tokens ajustado."; "Kore.ai agrega un tercer patrón, Custom, con la orquestación escrita en código, para entornos regulados."; regla de Kore.ai "choose the simplest pattern that effectively meets your business requirements" (la idea ya la dan Anthropic en 2.4 y LangChain en 6.5).
- **Lámina 7.11 (hoy 7.10), mecanismo de MetaGPT en las cards** — "MetaGPT encadena producto, arquitectura, gestión de proyecto, desarrollo y QA como una línea de montaje." y "Los agentes de MetaGPT no conversan: publican documentos en un pool de mensajes y cada rol se suscribe a lo suyo." El mecanismo se cuenta en 8.1; 7.10 solo nombra a MetaGPT. Notas: "MAST clasifica a ChatDev como flujo jerárquico; la sección 8 lo muestra con sus dos lecturas." (la clasificación queda solo en las notas de 8.1). El párrafo de Generative Agents pasó a las notas de 7.9.
- **Lámina 8.1, celda Patrón de ChatDev** — "MAST lo clasifica como flujo jerárquico" pasó a las notas de 8.1, con "(sección 9)". Notas cortadas: la segunda definición de HumanEval y MBPP (HumanEval se define en 5.6); "El dato de AutoGen que más enseña está en su paper: separar al que escribe código del que revisa su seguridad sube el F1 de detección de código inseguro un 8% con GPT-4 y un 35% con GPT-3.5-turbo. La ganancia de repartir roles es mayor con el modelo más débil."; "Magentic-One divide el trabajo por herramienta (navegador, archivos, código, terminal) y no por rol humano. [...] Los autores reconocen el costo: cada tarea puede llevar varios dólares y decenas de minutos." Las cifras siguen en `corpus/autogen-2023.web.md` y `corpus/magentic-one-2024.web.md`.
- **Lámina 8.3 "Multiagente antes de los LLM" (cortada entera)** — lead "Cuatro sistemas multiagente sin modelos de lenguaje." Cards: "**Contract Net (1980)** Un manager anuncia una tarea, los contratistas ofertan y el manager adjudica. Un contratista puede subdividir la tarea y subcontratar, así que el protocolo arma jerarquías." (pasó a las notas de 7.10) "**Kiva (2006)** Robots autónomos que llevan las estanterías hasta el operario. Una instalación grande puede usar 500 robots o más, y los autores reportan una productividad doble o mayor." "**OpenAI Five (2019)** Le ganó a los campeones mundiales de Dota 2 con cinco copias de la misma red, con parámetros compartidos. Las compras y las habilidades estaban programadas a mano." "**AlphaStar (2019)** Le ganó 5-0 a un profesional de StarCraft II. Lo multiagente está en el entrenamiento, una liga de agentes que juegan entre sí; en la partida juega uno solo." Línea final: "Un sistema con LLM también puede tener agentes sin LLM: el ComputerTerminal de Magentic-One ejecuta código y comandos sin modelo." (sobrevive como una línea en las notas de 8.1). Notas: team spirit de OpenAI Five; AlphaStar despliega un agente por lado; Kiva sin datos de coordinación; criterio de la cátedra sobre agentes sin modelo (pasó a 8.1); agente tablero de ajedrez de AutoGen ("prompting alone … still led to illegal moves"). Repetía la respuesta de 1.1 y la card "Sin ML ni LLMs" de 1.3; Kiva, OpenAI Five y AlphaStar no se retomaban. Registros: `corpus/contract-net-protocol.web.md`, `corpus/kiva-warehouse-wurman-2008.web.md`, `corpus/openai-five-2019.web.md`, `corpus/alphastar-deepmind-2019.web.md`.
- **Lámina 9.5, notas** — "La regla de Cognition en una línea: toda acción lleva adentro una decisión que nadie enunció, y dos decisiones en paralelo que se contradicen dan un mal resultado." Tercera mención del principio (tabla y notas de 9.4).
- **Notas de 4.3 y 4.4, system prompt** — "Si alguien pregunta cuál es el system prompt de esta trayectoria: no hay." (4.3) y "Respuesta a la pregunta de qué system prompt usa ReAct: ninguno." (4.4). La lámina 4.4 lo dice una vez. El detalle de modelo (PaLM-540B contra text-davinci-002, temperatura, tokens) quedó solo en las notas de 4.4; salió de las de 4.5 ("Detalle de época: [...] Las tablas principales del paper son con PaLM-540B.").
- **Recortes de notas largas** — 4.4: "Después de 'Here are some examples.' vienen seis trayectorias escritas a mano por los autores [...] reportan que más ejemplos no mejoraban." (lo muestra el diagrama de 4.5 y lo citan sus Sources); 4.5: los cuatro pasos numerados del notebook (condensados en un párrafo) y "Si el texto generado no trae 'Action i:', el código hace una segunda llamada que pide solo la acción, y la cuenta como llamada mala. Son a lo sumo 7 llamadas por pregunta, más una por cada paso mal formado." (sigue en las Sources); 6.3: "El deck de Biomédica traía una cifra de caída de precisión con la cantidad de tools. No tiene fuente y quedó en Cut material."; 9.7: los cuatro pasos numerados (resumidos en dos párrafos) y el detalle de qué dato ve cada agente ("datos del préstamo enmascarados", "saldo y umbrales sin datos del préstamo", "identificadores seudonimizados", condensado en una frase).
- **Texto de duración obsoleto** — retirado por indicación del presentador ("No te preocupes del tiempo"): la frase de 9.7 sobre los 138 minutos y la lista de cortes, el cierre de 8.3 con "unos 120 minutos", "Si el tiempo aprieta, se pasa en un minuto." (1.6), "Se pueden mencionar si hay tiempo." (5.5), "Si falta tiempo, esta lámina se puede saltear." (8.2), y en Open questions el ítem "Duración" con sus 12 cortes y el [minor] "Timing". Los tiempos acumulados de las notas se recalcularon (total ~131 min con la pausa).
