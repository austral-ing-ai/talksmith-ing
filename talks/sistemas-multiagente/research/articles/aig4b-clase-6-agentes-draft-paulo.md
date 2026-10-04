---
presentation: Inteligencia Artificial Generativa Aplicada en Biomedicina
class: "Clase 6 — Agentes de IA"
research: research/corpus/
description: Slides are grouped into Sections. Each Section contains one or more Slides.
presenter: Paulo Veiga, Docente de Universidad Austral
audience: Estudiantes de grado en ingeniería biomédica / bioingeniería. Base técnica sólida, poca exposición previa a deep learning.
duration: 120 min (clase doble)
date:
---

# Thesis

**Claim:**

**Why it matters:**

**Presenter feedback:**

- [open] 2026-08-14 — "Restaurado 1:1 desde `AIG4B-Clase-6-Agentes.pptx`. La tesis no estaba explícita en el deck original: falta escribirla."

---

# Agenda

**Narrative arc:**

Reconstruido desde la slide de agenda del deck original.

**Sections (in delivery order):**

- 1. ¿qué es un agente?
- 2. Agenda
- 3. Agentes basados en llms
- 4. Desafíos de producción
- 5. Sistemas multiagente
- 6. Memoria de agentes
- 7. Objetivos y práctica

<!-- agenda tal como figura en el deck original: -->
<!-- - **¿Qué es un Agente?** -->
<!-- **1** -->
<!-- - Definición formal, racionalidad, ejemplos y tipos de ambientes -->
<!-- **2** -->
<!-- - **Agentes basados en LLMs** -->
<!-- - Formulación, valor del LLM, arquitectura ReAct y componentes -->
<!-- - **Desafíos de Producción** -->
<!-- **3** -->
<!-- - Brecha prototipo-producción y Model Context Protocol -->
<!-- **4** -->
<!-- - **Sistemas Multiagente** -->
<!-- - Limitaciones de un agente, arquitecturas multiagente y el espectro workflows-agentes -->
<!-- **5** -->
<!-- - **Memoria de Agentes** -->
<!-- - Arquitectura de dos niveles, patrones de integración y soluciones -->
<!-- **6** -->
<!-- - **Objetivos y Práctica** -->
<!-- - Objetivos de aprendizaje, proyectos prácticos y ejercicio final -->

**Presenter feedback:**


---

# 0. Portada

**Goal of this section:** Apertura del deck original — portada y material previo a la primera sección.

**Presenter feedback:**


---

## 1. Inteligencia Artificial Generativa Aplicada en Biomedicina

<!-- slide 1 del pptx original -->

### Content

**Módulo 6: Agents**

- Profesores: Paulo Veiga / Marco Sanchez Sorondo
- Universidad Austral · Facultad de Ingeniería · Departamento de Inteligencia Artificial
- Abril, 2026

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-01-1.png)

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 1)

### Speaker notes

### Presenter feedback


---

## 2. Agenda

<!-- slide 2 del pptx original -->

### Content

- **¿Qué es un Agente?**

**1**

- Definición formal, racionalidad, ejemplos y tipos de ambientes

**2**

- **Agentes basados en LLMs**

- Formulación, valor del LLM, arquitectura ReAct y componentes

- **Desafíos de Producción**

**3**

- Brecha prototipo-producción y Model Context Protocol

**4**

- **Sistemas Multiagente**

- Limitaciones de un agente, arquitecturas multiagente y el espectro workflows-agentes

**5**

- **Memoria de Agentes**

- Arquitectura de dos niveles, patrones de integración y soluciones

**6**

- **Objetivos y Práctica**

- Objetivos de aprendizaje, proyectos prácticos y ejercicio final

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 2)

### Speaker notes

### Presenter feedback


---

## 3. Agentes – Una palabra mal utilizada

<!-- slide 3 del pptx original -->

### Content

- ¿QUÉ ES UN AGENTE?

**¿Qué es un Agente?**

- En el uso cotidiano, la palabra "agente" se aplica con demasiada frecuencia a sistemas basados en LLMs, pero esa simplificación suele ocultar distinciones importantes.

- Antes de hablar de agentes basados en LLMs, necesitamos entender la definición formal y rigurosa del concepto.

- En IA clásica, un agente es cualquier entidad que percibe su entorno mediante sensores y actúa sobre él mediante actuadores. — Russell & Norvig

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-03-1.png)

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-03-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-03-2.svg -->

**¿Qué se suele llamar agente?**

- En el uso popular, se denomina "agente" simplemente a un LLM o a cualquier sistema basado en LLM, sin más distinción.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-03-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-03-3.svg -->

**¿Por qué esto es incorrecto?**

- Un LLM no es un agente por sí solo. Además, existen muchos tipos de agentes que no involucran en absoluto modelos de lenguaje.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-03-4.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-03-4.svg -->

**¿Cuál es el camino correcto?**

- Entender la definición formal de agente antes de hablar de agentes basados en LLMs es indispensable para razonar con rigor.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 3)

### Speaker notes

### Presenter feedback


---

# 1. ¿qué es un agente?

**Goal of this section:**

**Presenter feedback:**


---

## 1. "An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators..."

<!-- slide 4 del pptx original -->

### Content

- — Russell & Norvig, Artificial Intelligence: A Modern Approach

- Esta es la definición canónica y punto de partida de toda la teoría de agentes inteligentes en IA clásica.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 4)

### Speaker notes

### Presenter feedback


---

## 2. Comentarios sobre la definición

<!-- slide 5 del pptx original -->

### Content

- La elegancia de esta definición radica en su amplitud y generalidad. Veamos lo que no menciona:

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-05-1.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-05-1.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-05-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-05-2.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-05-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-05-3.svg -->

| Sin ML ni LLMs | Sin programas | Sistemas biológicos |
|---|---|---|
| No se mencionan Machine Learning, Deep Learning, LLMs, tools ni RAG. Son implementaciones posibles, no la definición. | Ni siquiera se mencionan programas o software. Un sistema mecánico o electrónico también encaja perfectamente. | La definición contempla sistemas biológicos: células, humanos, animales e insectos son todos agentes válidos bajo esta definición. |

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 5)

### Speaker notes

### Presenter feedback


---

## 3. "A rational agent is one that does the right thing... This notion of desirability is captured by a performance measure that evaluates any given sequence of environment states."

<!-- slide 6 del pptx original -->

### Content

- — Russell & Norvig, Artificial Intelligence: A Modern Approach

- La racionalidad introduce el concepto de optimización: no basta con percibir y actuar, hay que hacerlo bien según un criterio definido.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 6)

### Speaker notes

### Presenter feedback


---

## 4. Racionalidad

<!-- slide 7 del pptx original -->

### Content

- Un agente racional selecciona la acción que maximiza su medida de performance, dada la evidencia de sus percepciones y su conocimiento previo. La racionalidad depende de cuatro factores clave:

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-07-1.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-07-1.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-07-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-07-2.svg -->

| Medida de performance | Conocimiento previo |
|---|---|
| El criterio que define el éxito del agente. Sin esta medida, no hay racionalidad posible. | Lo que el agente ya sabe sobre el ambiente antes de comenzar a actuar. |

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-07-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-07-3.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-07-4.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-07-4.svg -->

| Acciones disponibles | Secuencia de percepciones |
|---|---|
| El conjunto de acciones que el agente puede ejecutar en su entorno. | El historial de todo lo que el agente ha observado del ambiente hasta el momento. |

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 7)

### Speaker notes

### Presenter feedback


---

## 5. Ejemplo: Vacuum Cleaner

<!-- slide 8 del pptx original -->

### Content

- Formulación como agente inteligente — Mantener limpio un entorno (grilla n×m) eliminando la suciedad con el mínimo de acciones posibles.

| Agente | Aspiradora autónoma (robot o modelo abstracto) |
|---|---|
| Sensores | Detector de suciedad, posición actual en la grilla |
| Actuadores | Motor de movimiento (izq/der/adelante/atrás), motor de succión |
| Ambiente | Grilla n×m, parcialmente observable, determinístico |
| Acciones | Aspirar, MoverIzquierda, MoverDerecha, Esperar |
| Performance | +10 limpiar celda sucia · −1 moverse · −5 aspirar celda limpia · −10 chocar |

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 8)

### Speaker notes

### Presenter feedback


---

## 6. Ejemplo: Robot Móvil

<!-- slide 9 del pptx original -->

### Content

- Formulación como agente inteligente — Desplazarse desde un punto inicial hasta un destino evitando obstáculos en entornos complejos.

| Agente | Robot móvil autónomo con sistema de control y planificación |
|---|---|
| Sensores | Cámara, LiDAR, GPS, giroscopio, sensores de proximidad |
| Actuadores | Motores de tracción, dirección, frenos, brazo robótico |
| Ambiente | Entorno físico (indoor/outdoor), continuo, parcialmente observable, dinámico |
| Acciones | Avanzar, girar, frenar, recalcular ruta |
| Performance | Llegar al destino rápido, sin colisiones y con mínimo consumo de energía |

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 9)

### Speaker notes

### Presenter feedback


---

## 7. Ejemplo: DeepMind AlphaGo

<!-- slide 10 del pptx original -->

### Content

- Formulación como agente inteligente — Jugar al Go a nivel superhumano mediante redes neuronales profundas y búsqueda Monte Carlo.

| Agente | Red neuronal profunda + búsqueda Monte Carlo (MCTS) |
|---|---|
| Sensores | Estado actual del tablero (disposición de fichas blancas y negras) |
| Actuadores | Colocar una piedra en una intersección válida o pasar turno |
| Ambiente | Tablero de Go 19×19, determinístico, completamente observable, competitivo |
| Performance | Probabilidad de victoria en la partida |

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 10)

### Speaker notes

### Presenter feedback


---

## 8. De AlphaGo Zero a AlphaZero

<!-- slide 11 del pptx original -->

### Content

- La evolución de AlphaGo ilustra uno de los saltos más significativos en la historia de los agentes inteligentes: pasar del aprendizaje con datos humanos a la generalización pura.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-11-1.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-11-1.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-11-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-11-2.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-11-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-11-3.svg -->

| AlphaGo | AlphaGo Zero | AlphaZero |
|---|---|---|
| Aprende de partidas humanas. Requiere datos de expertos como punto de partida. | Aprende desde cero sin datos humanos, solo autojuego y retroalimentación. Red neuronal unificada política-valor + MCTS. | Generaliza a múltiples juegos (ajedrez, shogi, go) sin conocimiento previo. Mismo algoritmo, distintos juegos. |

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-11-4.png)

- La métrica de performance es universal: tasa de victorias (ganar > empatar > perder).

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 11)

### Speaker notes

### Presenter feedback


---

## 9. Tipos de Ambientes

<!-- slide 12 del pptx original -->

### Content

- La naturaleza del ambiente determina en gran medida la complejidad del agente necesario para operar en él. Estas son las dimensiones fundamentales de clasificación:

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-12-1.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-12-1.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-12-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-12-2.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-12-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-12-3.svg -->

| Observable | Agentes | Determinismo |
|---|---|---|
| Completamente observable vs. Parcialmente observable | Un agente vs. Multi-agente | Determinístico vs. Estocástico |

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-12-4.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-12-4.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-12-5.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-12-5.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-12-6.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-12-6.svg -->

**Episódico vs. Secuencial**

**Estático vs. Dinámico**

**Discreto vs. Continuo**

- El ambiente cambia o no mientras el agente delibera

- Estados y acciones finitos vs. infinitos

- Acciones independientes vs. acciones con consecuencias a largo plazo

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-12-7.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-12-7.svg -->

**Conocido vs. Desconocido**

- El agente conoce o no las reglas del ambiente

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 12)

### Speaker notes

### Presenter feedback


---

## 10. Dificultad de Ambientes

<!-- slide 13 del pptx original -->

### Content

- Las dimensiones del ambiente se combinan para determinar cuán desafiante resulta operar en él. El espectro va de problemas triviales a extraordinariamente complejos.

**Crucigrama**

**1**

- Fácil: observable, determinístico, estático. Un solo agente.

**Ajedrez**

**2**

- Medio: observable y determinístico, pero competitivo. Requiere anticipar al oponente.

**Taxi Autónomo**

**3**

- Difícil: parcialmente observable, estocástico, dinámico, continuo, multi-agente.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 13)

### Speaker notes

### Presenter feedback


---

## 11. ¿Por qué todas estas definiciones?

<!-- slide 14 del pptx original -->

### Content

- La formalización agentica no es un ejercicio académico vacío. Tiene tres utilidades prácticas concretas y poderosas:

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-14-1.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-14-1.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-14-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-14-2.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-14-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-14-3.svg -->

**Análisis riguroso**

**Reutilización de frameworks**

**Decisión informada**

- Nos obliga a pensar bien en el problema a resolver y analizar todos sus aspectos antes de implementar.

- Es fundamental saber cuándo vale la pena usar un agente y cuándo una solución más simple es suficiente.

- Permite usar frameworks agnósticos que resuelven la formulación agentica. Un mismo algoritmo puede ganar en ajedrez y dirigir un robot.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 14)

### Speaker notes

### Presenter feedback


---

## 12. ¿Cuándo vale la pena usar agentes?

<!-- slide 15 del pptx original -->

### Content

- Los agentes no son la solución a todo. Estas son las condiciones que justifican su uso frente a soluciones determinísticas más simples:

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-15-1.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-15-1.svg -->

**Múltiples herramientas en orden variable**

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-15-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-15-2.svg -->

**Interpretación dinámica de resultados**

- Cuando hay que interpretar y relacionar apropiadamente resultados en tiempo de ejecución, adaptando el comportamiento.

- Cuando la solución requiere usar varias herramientas, en múltiples órdenes y de distintas maneras según el contexto.

| Orquestación variable de sistemas | Solución determinística insuficiente |
|---|---|
| Cuando hay que sincronizar y/u orquestar distintos sistemas de manera variable según las circunstancias. | Cuando el espacio de posibilidades es demasiado grande o dinámico para ser cubierto con reglas fijas. |

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 15)

### Speaker notes

### Presenter feedback


---

# 2. Agenda

**Goal of this section:**

**Presenter feedback:**


---

## 1. Agenda

<!-- slide 16 del pptx original -->

### Content

- ¿Qué es un Agente?

**1**

- Definición formal, racionalidad, ejemplos y tipos de ambientes

**2**

- Agentes basados en LLMs

- Formulación, valor del LLM, arquitectura ReAct y componentes

- Desafíos de Producción

**3**

- Brecha prototipo-producción y Model Context Protocol

**4**

- Sistemas Multiagente

- Limitaciones de un agente, arquitecturas multiagente y el espectro workflows-agentes

- Memoria de Agentes

**5**

- Arquitectura de dos niveles, patrones de integración y soluciones

**6**

- Objetivos y Práctica

- Objetivos de aprendizaje, proyectos prácticos y ejercicio final

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 16)

### Speaker notes

### Presenter feedback


---

## 2. Agenda

<!-- slide 23 del pptx original -->

### Content

- ¿Qué es un Agente?

**1**

- Definición formal, racionalidad, ejemplos y tipos de ambientes

**2**

- Agentes basados en LLMs

- Formulación, valor del LLM, arquitectura ReAct y componentes

- Desafíos de Producción

**3**

- Brecha prototipo-producción y Model Context Protocol

**4**

- Sistemas Multiagente

- Limitaciones de un agente, arquitecturas multiagente y el espectro workflows-agentes

- Memoria de Agentes

**5**

- Arquitectura de dos niveles, patrones de integración y soluciones

**6**

- Objetivos y Práctica

- Objetivos de aprendizaje, proyectos prácticos y ejercicio final

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 23)

### Speaker notes

### Presenter feedback


---

## 3. Agenda

<!-- slide 27 del pptx original -->

### Content

- **¿Qué es un Agente?**

**1**

- Definición formal, racionalidad, ejemplos y tipos de ambientes

**2**

- **Agentes basados en LLMs**

- Formulación, valor del LLM, arquitectura ReAct y componentes

- **Desafíos de Producción**

**3**

- Brecha prototipo-producción y Model Context Protocol

**4**

- **Sistemas Multiagente**

- Limitaciones de un agente, arquitecturas multiagente y el espectro workflows-agentes

**5**

- **Memoria de Agentes**

- Arquitectura de dos niveles, patrones de integración y soluciones

**6**

- **Objetivos y Práctica**

- Objetivos de aprendizaje, proyectos prácticos y ejercicio final

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 27)

### Speaker notes

### Presenter feedback


---

## 4. Agenda

<!-- slide 34 del pptx original -->

### Content

- ¿Qué es un Agente?

**1**

- Definición formal, racionalidad, ejemplos y tipos de ambientes

**2**

- Agentes basados en LLMs

- Formulación, valor del LLM, arquitectura ReAct y componentes

- Desafíos de Producción

**3**

- Brecha prototipo-producción y Model Context Protocol

**4**

- Sistemas Multiagente

- Limitaciones de un agente, arquitecturas multiagente y el espectro workflows-agentes

- Memoria de Agentes

**5**

- Arquitectura de dos niveles, patrones de integración y soluciones

**6**

- Objetivos y Práctica

- Objetivos de aprendizaje, proyectos prácticos y ejercicio final

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 34)

### Speaker notes

### Presenter feedback


---

## 5. Agenda

<!-- slide 40 del pptx original -->

### Content

- ¿Qué es un Agente?

**1**

- Definición formal, racionalidad, ejemplos y tipos de ambientes

**2**

- Agentes basados en LLMs

- Formulación, valor del LLM, arquitectura ReAct y componentes

- Desafíos de Producción

**3**

- Brecha prototipo-producción y Model Context Protocol

**4**

- Sistemas Multiagente

- Limitaciones de un agente, arquitecturas multiagente y el espectro workflows-agentes

- Memoria de Agentes

**5**

- Arquitectura de dos niveles, patrones de integración y soluciones

**6**

- Objetivos y Práctica

- Objetivos de aprendizaje, proyectos prácticos y ejercicio final

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 40)

### Speaker notes

### Presenter feedback


---

# 3. Agentes basados en llms

**Goal of this section:**

**Presenter feedback:**


---

## 1. Agentes basados en LLMs

<!-- slide 17 del pptx original -->

### Content

- Con la base teórica asentada, exploramos cómo los modelos de lenguaje encajan en el marco formal de agentes inteligentes.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 17)

### Speaker notes

### Presenter feedback


---

## 2. Agentes basados en LLMs

<!-- slide 18 del pptx original -->

### Content

- Formulación como agente inteligente — Resolver tareas lingüísticas o de razonamiento a partir de instrucciones en lenguaje natural.

| Agente | Modelo de lenguaje grande (LLM) con razonamiento, memoria y acceso a herramientas externas |
|---|---|
| Sensores | Texto de entrada del usuario, contexto previo, resultados de herramientas |
| Actuadores | Generar texto, razonar, ejecutar comandos, llamar APIs, producir planes |
| Ambiente | Entorno digital, simbólico, parcialmente observable, dinámico |
| Performance | Calidad, relevancia y precisión de respuestas; satisfacción del usuario |

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 18)

### Speaker notes

### Presenter feedback


---

## 3. ¿Cuál es el valor de un LLM en un agente?

<!-- slide 19 del pptx original -->

### Content

- El LLM no es simplemente un chatbot dentro de un agente. Su valor radica en capacidades genuinamente novedosas que ningún sistema anterior podía ofrecer:

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-19-1.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-19-1.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-19-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-19-2.svg -->

| Observar el lenguaje natural | Usar herramientas con lenguaje |
|---|---|
| Abre las puertas a un agente genérico para "percibir" el ambiente del lenguaje natural y actuar en él de forma fluida. | Emplea el lenguaje natural como medio universal para interactuar con herramientas de cualquier tipo y API. |

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-19-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-19-3.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-19-4.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-19-4.svg -->

| Reflexionar sobre outputs | Instruir sistemas complejos |
|---|---|
| Puede analizar el resultado de una herramienta (ej: query con error → corrige → reintenta) en un ciclo reflexivo. | Permite comunicarse con sistemas informáticos complejos usando lenguaje desestructurado y natural. |

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 19)

### Speaker notes

### Presenter feedback


---

## 4. Arquitectura ReAct (Reason + Act)

<!-- slide 20 del pptx original -->

### Content

- ReAct es la arquitectura más simple y fundamental para agentes basados en LLMs. Combina razonamiento y acción en un ciclo iterativo hasta alcanzar una respuesta final.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-20-1.png)

**Observation**

**Thought**

**Action**

**Razonar**

**Respuesta**

- El ciclo Thought → Action → Observation se repite hasta que el agente determina que tiene suficiente información para producir una respuesta final de calidad.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 20)

### Speaker notes

### Presenter feedback


---

## 5. (sin título)

<!-- slide 21 del pptx original -->

### Content

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-21-1.png)
<!-- enlace de la imagen: https://aitutorial.dev/agents/intro -->

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 21)

### Speaker notes

### Presenter feedback


---

## 6. Componentes de un Agente basado en LLM

<!-- slide 22 del pptx original -->

### Content

- Todo agente basado en LLM se construye sobre tres componentes esenciales que definen qué sabe, qué puede hacer y de qué contexto dispone:

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-22-1.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-22-1.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-22-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-22-2.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-22-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-22-3.svg -->

**1. Memoria y Contexto**

**2. Tools (Herramientas)**

**3. Información Contextual (RAG)**

- Historial de conversación, último prompt y contexto activo. Es la "conciencia" inmediata del agente sobre la situación actual.

- Conjunto de herramientas a las que puede llamar, descriptas en el contexto. El agente decide cuándo y cómo invocarlas.

- Información asociada al historial mediante recuperación semántica. Puede incrustarse en el prompt o invocarse como herramienta.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 22)

### Speaker notes

### Presenter feedback


---

# 4. Desafíos de producción

**Goal of this section:**

**Presenter feedback:**


---

## 1. Desafíos de Producción

<!-- slide 24 del pptx original -->

### Content

- Llevar agentes del prototipo funcional a un sistema de producción confiable es uno de los mayores retos de la ingeniería de IA actual.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 24)

### Speaker notes

### Presenter feedback


---

## 2. ¿Por qué importa en producción?

<!-- slide 25 del pptx original -->

### Content

- Existe una brecha significativa entre un demo que funciona y un sistema de producción confiable. Los datos son reveladores:

| 95%+ | 58% | ~85% |
|---|---|---|
| Accuracy requerida | Tool selection con 20+ tools | Rule enforcement |
| El umbral mínimo para sistemas de producción confiables. Los demos funcionales no llegan a este nivel. | La accuracy de selección de herramientas cae de 92% (5 tools) a solo 58% con más de 20 herramientas disponibles. | Los LLMs cumplen reglas basadas en prompt el 85% del tiempo. Insuficiente para sectores regulados. |

- Las fallas en producción vienen de tool design inadecuado, estructuras de memoria y mecanismos de validación — no del modelo en sí.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-25-1.png)

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 25)

### Speaker notes

### Presenter feedback


---

## 3. MCP: Model Context Protocol

<!-- slide 26 del pptx original -->

### Content

- El Model Context Protocol es el estándar emergente de integración para agentes, diseñado para resolver la fragmentación del ecosistema y garantizar interoperabilidad a largo plazo.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-26-1.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-26-1.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-26-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-26-2.svg -->

| Estándar universal | Servidores MCP |
|---|---|
| Asegura compatibilidad entre Claude, ChatGPT, Cursor y futuras plataformas. Diseña una vez, integra en todas partes. | Permite diseñar y operar servidores MCP con especificaciones completas de herramientas, recursos y capacidades. |

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-26-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-26-3.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-26-4.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-26-4.svg -->

| Multi-servidor | Ciclo estandarizado |
|---|---|
| Los agentes pueden integrarse con múltiples servidores MCP simultáneamente via MultiServerMCPClient. | Define cómo los agentes descubren, llaman y reciben resultados de herramientas de manera consistente. |

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 26)

### Speaker notes

### Presenter feedback


---

# 5. Sistemas multiagente

**Goal of this section:**

**Presenter feedback:**


---

## 1. Sistemas Multiagente

<!-- slide 28 del pptx original -->

### Content

- Cuando un solo agente no alcanza: motivación, arquitecturas y aplicación en biomedicina.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 28)

### Speaker notes

### Presenter feedback


---

## 2. Limitaciones de un solo agente

<!-- slide 29 del pptx original -->

### Content

- Ya vimos que un agente con tools puede resolver problemas complejos. Pero a medida que crece el número de herramientas y dominios, aparecen problemas concretos:

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-29-1.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-29-1.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-29-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-29-2.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-29-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-29-3.svg -->

| Sobrecarga de tools | Contexto desbordado | Falta de especialización |
|---|---|---|
| La accuracy de selección de herramientas cae drásticamente cuando el agente tiene demasiadas opciones (de ~92% con 5 tools a ~58% con 20+). Un agente generalista pierde precisión. | Si el agente debe manejar información clínica, farmacológica, radiológica y administrativa en un solo contexto, la calidad de razonamiento se degrada. | Un único system prompt no puede ser simultáneamente experto en interacciones farmacológicas Y en interpretación de ensayos clínicos Y en análisis de imágenes. |

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 29)

### Speaker notes

### Presenter feedback


---

## 3. Ejemplo: Soporte a Decisiones Clínicas

<!-- slide 30 del pptx original -->

### Content

- Queremos asistir a un equipo médico en la toma de decisiones para un paciente con cáncer de pulmón (NSCLC), integrando datos clínicos, farmacológicos y de evidencia.
- Tools 15+ tools mezcladas de todos los dominios 3–5 tools por agente, especializadas System prompt Genérico, intenta cubrir todo Cada agente tiene instrucciones de su dominio Contexto Se llena rápidamente con info de todos los dominios Cada agente mantiene solo su contexto relevante Precisión Se degrada con la complejidad Cada agente es experto en lo suyo

- El problema no es la capacidad del LLM, sino la arquitectura. Dividir en agentes especializados es una decisión de ingeniería, no de modelo.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 30)

### Speaker notes

### Presenter feedback


---

## 4. ¿Qué es un Sistema Multiagente?

<!-- slide 31 del pptx original -->

### Content

- Un sistema multiagente consta de múltiples agentes que interactúan entre sí — de forma colaborativa, competitiva, o ambas — para resolver un problema que excede las capacidades de un agente individual.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-31-1.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-31-1.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-31-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-31-2.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-31-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-31-3.svg -->

| Modularidad | Especialización | Control |
|---|---|---|
| Agentes independientes facilitan el desarrollo, testing y mantenimiento. Se puede mejorar un agente sin tocar los demás. | Cada agente tiene su propio dominio de expertise, sus tools y su system prompt optimizado para una tarea concreta. | Se define explícitamente cómo se comunican los agentes y quién decide el flujo, en vez de depender de un único LLM para todo. |

- Ya vimos ejemplos multiagente: AlphaGo (competitivo), Taxi Autónomo (competitivo + colaborativo). En biomedicina, el patrón típico es colaborativo.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 31)

### Speaker notes

### Presenter feedback


---

## 5. Arquitecturas Multiagente

<!-- slide 32 del pptx original -->

### Content

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-1.jpg)

- Hay varias formas de conectar agentes. La elección depende del nivel de control, complejidad y autonomía que necesite el sistema.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-2.svg -->

- Supervisor

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-3.svg -->

- Un agente central decide a qué agente especializado derivar cada consulta. Patrón más común y predecible. Ejemplo: un agente coordinador recibe la pregunta del médico y la deriva al agente clínico o al farmacológico según corresponda.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-4.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-4.svg -->

- Supervisor (tool-calling)

- Los agentes especializados se exponen como tools del supervisor. El LLM supervisor usa function calling para invocarlos. Ejemplo: es lo que los alumnos van a implementar en la Parte 3 del proyecto.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-5.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-5.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-6.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-6.svg -->

- Network

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-7.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-7.svg -->

- Todos los agentes se comunican entre sí. Más flexible pero menos predecible. Ejemplo: agente clínico y farmacológico dialogan directamente para resolver una interacción.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-8.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-8.svg -->

- Hierarchical

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-9.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-32-9.svg -->

- Supervisor de supervisores. Para sistemas muy complejos. Ejemplo: hospital con departamentos, cada uno con su coordinador interno.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 32)

### Speaker notes

### Presenter feedback


---

## 6. Workflows vs Agentes — El espectro

<!-- slide 33 del pptx original -->

### Content

- No todo sistema con múltiples LLMs es un 'agente'. Existe un espectro entre flujos deterministas y agentes autónomos.

**Workflows (deterministas)**

**Workflows (dirigidos por LLM)**

**Agentes (autónomos)**

- Rutas de código predefinidas. El LLM se embebe en pasos fijos.
- Patrones: prompt chaining, paralelización.
- Ejemplo: Pipeline que siempre ejecuta análisis clínico → verificación farmacológica → informe.

- El LLM decide sus propias acciones basado en feedback del ambiente.
- Patrón: ReAct con tool-calling.
- Ejemplo: El agente decide qué tools usar, en qué orden, y cuándo tiene suficiente información para responder.

- El LLM dirige el flujo entre rutas predefinidas.
- Patrones: routing, orchestrator-worker, evaluator-optimizer.
- Ejemplo: Un router decide si la pregunta va al agente clínico o al farmacológico.

- La magia está en mezclarlos. Un sistema real puede tener routing determinista entre agentes que internamente son autónomos.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 33)

### Speaker notes

### Presenter feedback


---

# 6. Memoria de agentes

**Goal of this section:**

**Presenter feedback:**


---

## 1. Memoria de Agentes

<!-- slide 35 del pptx original -->

### Content

- La memoria es uno de los componentes más críticos y menos intuitivos de los agentes en producción. Sin una estrategia adecuada, los agentes son caros, incoherentes y frustrantes.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 35)

### Speaker notes

### Presenter feedback


---

## 2. Arquitectura de Memoria: Dos Niveles

<!-- slide 36 del pptx original -->

### Content

- La solución al problema de memoria es una arquitectura que combina velocidad con persistencia, inspirada en los sistemas de caché de hardware:

| Working Memory (Sesión) | Long-Term Memory (Persistente) |
|---|---|
| Duración: Una sola sesión activa<br>Propósito: Estado activo de conversación<br>Ejemplo: Detalles del pedido en el chat actual<br>Implementación: MemorySaver + thread_id<br>Analogía: Caché L1 — rápida y temporal | Duración: Entre sesiones, indefinidamente<br>Propósito: Conocimiento persistente del usuario<br>Ejemplo: Preferencias de usuario a lo largo de meses<br>Implementación: Vector DB o servicio gestionado<br>Analogía: Base de datos — persistente y buscable |

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 36)

### Speaker notes

### Presenter feedback


---

## 3. Patrones de Integración de Memoria

<!-- slide 37 del pptx original -->

### Content

- Existen tres patrones principales para integrar la memoria en un agente, con distintos niveles de control y autonomía:

| 01 | 02 | 03 |
|---|---|---|
| Code-Driven (Programático) | LLM-Driven (Tool-Based) | Background Extraction (Automático) |

- Tu código decide explícitamente cuándo guardar y recuperar. Comportamiento predecible y eficiente. Punto de partida recomendado.

- El agente recibe tools de memoria y decide autónomamente qué recordar. Más natural y flexible, pero menos predecible.

- Almacena toda la conversación; procesos en segundo plano extraen hechos importantes de forma asíncrona.

- Recomendación: Empezar con code-driven, agregar background extraction para enriquecimiento, y usar LLM-driven cuando la autonomía sea un requisito funcional.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-37-1.png)

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 37)

### Speaker notes

### Presenter feedback


---

## 4. (sin título)

<!-- slide 38 del pptx original -->

### Content

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-38-1.png)
<!-- enlace de la imagen: https://aitutorial.dev/agents/memory -->

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 38)

### Speaker notes

### Presenter feedback


---

## 5. Soluciones de Memoria en Producción

<!-- slide 39 del pptx original -->

### Content

- El ecosistema de memoria para agentes ha madurado rápidamente. Estas son las soluciones más relevantes y el patrón universal que todas implementan:

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-39-1.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-39-1.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-39-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-39-2.svg -->

| Redis Agent Memory Server | Mem0 |
|---|---|
| Working + long-term con búsqueda semántica integrada. Alta performance para producción. | Capa de memoria gestionada para agentes. API simple, ideal para integración rápida. |

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-39-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-39-3.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-39-4.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-39-4.svg -->

| Zep | LangChain Memory |
|---|---|
| Long-term memory con extracción automática de hechos desde conversaciones. | Integración nativa con LangChain/LangSmith. La opción más directa si ya usás el stack de LangChain. |

- Patrón universal: store → search → inject en prompt o tool results. Independientemente de la solución elegida, este flujo es constante.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-39-5.png)

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 39)

### Speaker notes

### Presenter feedback


---

# 7. Objetivos y práctica

**Goal of this section:**

**Presenter feedback:**


---

## 1. Objetivos y Práctica

<!-- slide 41 del pptx original -->

### Content

- Esta parte del módulo traduce toda la teoría en competencias concretas y proyectos prácticos implementables.

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 41)

### Speaker notes

### Presenter feedback


---

## 2. Objetivos de Aprendizaje

<!-- slide 42 del pptx original -->

### Content

- Al finalizar este módulo, el estudiante será capaz de diseñar, implementar y operar agentes basados en LLMs en entornos de producción:

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-42-1.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-42-1.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-42-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-42-2.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-42-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-42-3.svg -->

| Construir agentes con tool capabilities | Diseñar y operar servidores MCP | Implementar memoria y seguridad |
|---|---|---|
| Usando createAgent de LangChain con patrones ReAct completos. | Con especificaciones completas e integración multi-servidor via MultiServerMCPClient. | Memoria con MemorySaver, reglas de negocio determinísticas, detección de PII y mitigación de jailbreak. |

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 42)

### Speaker notes

### Presenter feedback


---

## 3. Ejercicio Práctico

<!-- slide 43 del pptx original -->

### Content

- El siguiente ejercicio busca integrar todos los conceptos del módulo en un problema original elegido por cada estudiante:

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-43-1.png)

**Paso 1: Elegir un problema**

- Pensar en un problema real a ser resuelto por un agente basado en LLMs. Cuanto más cercano a la realidad, mejor.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-43-2.png)

**Paso 2: Modelar como agente**

- Formularlo con las definiciones formales: agente, sensores, actuadores, ambiente y medida de performance.

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-43-3.png)

**Paso 3: Implementar**

- Resolverlo usando como base la notebook de la práctica. Se puede usar información hardcodeada (JSONs, CSVs, .txt, etc.).

<!-- enlace de la forma: https://aitutorial.dev/agents/hands-on-exercise -->
- [Guia de ejercicios:](https://aitutorial.dev/agents/hands-on-exercise)

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 43)

### Speaker notes

### Presenter feedback


---

## 4. Bibliografía y Recursos

<!-- slide 44 del pptx original -->

### Content

- Recursos fundamentales para profundizar en los conceptos de este módulo:

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-44-1.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-44-1.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-44-2.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-44-2.svg -->

| Russell & Norvig (2020) | LangGraph Docs |
|---|---|
| Artificial Intelligence: A Modern Approach, 4th ed. Pearson. La referencia canónica para la teoría formal de agentes inteligentes. | Documentación oficial del framework para construcción de agentes stateful con grafos. langchain-ai.github.io/langgraph (https://langchain-ai.github.io/langgraph/) (https://langchain-ai.github.io/langgraph/) |

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-44-3.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-44-3.svg -->

![](research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-44-4.png)
<!-- original vectorial: research/corpus/AIG4B-Clase-6-Agentes.md/images/slide-44-4.svg -->

| AI Tutorial – Agents Module | LangChain Memory |
|---|---|
| Guía práctica sobre el módulo de agentes con ejemplos de código. aitutorial.dev/agents/overvie (https://aitutorial.dev/agents/overview) (https://aitutorial.dev/agents/overview) | Documentación de los módulos de memoria de LangChain para agentes. python.langchain.com/docs/modules/memory (https://python.langchain.com/docs/modules/memory/) (https://python.langchain.com/docs/modules/memory/) |

### Sources

- `AIG4B-Clase-6-Agentes.md.md` (slide 44)

### Speaker notes

### Presenter feedback


---

# Conclusions

## 1. Key takeaways

### Content

### Sources

- `AIG4B-Clase-6-Agentes.md.md`

### Speaker notes

### Presenter feedback

- [open] 2026-08-14 — "El deck original no tiene slide de cierre; hay que escribirla."

---

# Open questions

- Tesis y objetivo de cada sección quedaron vacíos: el deck original no los declara.
- Ver `research/corpus/AIG4B-Clase-6-Agentes.md.md` → *Inconsistencies / open questions* para los problemas detectados en el material original.

# Cut material

