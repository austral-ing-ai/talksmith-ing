---
source_file: aig4b-clase-6-agentes-biomedica.pdf
source_type: article
ingested_at: 2026-10-04
---

# Inteligencia Artificial Generativa Aplicada en Biomedicina — Módulo 6: Agents (deck en PDF)

## Provenance
- Original location: research/articles/aig4b-clase-6-agentes-biomedica.pdf
- Format: pdf (44 páginas, una lámina por página; generado con pdf-lib)
- Author / source (if known): Paulo Veiga / Marco Sanchez Sorondo — Universidad Austral, Facultad de Ingeniería, Departamento de Inteligencia Artificial
- Date of original (if known): "Abril, 2026" (portada); PDF creado el 2026-04-08
- Texto extraído con `pdftotext -layout`. Es la versión exportada del deck `AIG4B-Clase-6-Agentes.pptx`; el borrador Talksmith de Paulo (`aig4b-clase-6-agentes-draft-paulo.md.md`) restaura el mismo deck lámina por lámina.

## Key claims
- Antes de hablar de agentes basados en LLMs hay que partir de la definición formal: "An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators..." (Russell & Norvig, AIMA). La palabra "agente" está mal usada: en el uso popular se llama agente a un LLM o a cualquier sistema basado en LLM; "Un LLM no es un agente por sí solo" y existen agentes que no involucran modelos de lenguaje.
- La definición no menciona ML ni LLMs, ni siquiera programas o software, y contempla sistemas biológicos (células, humanos, animales, insectos).
- Racionalidad: "A rational agent is one that does the right thing... This notion of desirability is captured by a performance measure that evaluates any given sequence of environment states." Un agente racional selecciona la acción que maximiza su medida de performance dada la evidencia de sus percepciones y su conocimiento previo. Depende de cuatro factores: medida de performance, conocimiento previo, acciones disponibles, secuencia de percepciones.
- Tipos de ambientes (dimensiones): completamente vs. parcialmente observable; un agente vs. multi-agente; determinístico vs. estocástico; episódico vs. secuencial; estático vs. dinámico; discreto vs. continuo; conocido vs. desconocido.
- Dificultad de ambientes: crucigrama (fácil: observable, determinístico, estático, un solo agente) → ajedrez (medio: observable, determinístico, competitivo) → taxi autónomo (difícil: parcialmente observable, estocástico, dinámico, continuo, multi-agente).
- La formalización sirve para: análisis riguroso, reutilización de frameworks agnósticos ("Un mismo algoritmo puede ganar en ajedrez y dirigir un robot") y decisión informada sobre cuándo vale la pena un agente.
- Cuándo vale la pena usar agentes: múltiples herramientas en orden variable; interpretación dinámica de resultados; orquestación variable de sistemas; solución determinística insuficiente.
- Agente basado en LLM formulado como agente inteligente: sensores = texto del usuario, contexto previo, resultados de herramientas; actuadores = generar texto, razonar, ejecutar comandos, llamar APIs, producir planes; ambiente digital, simbólico, parcialmente observable, dinámico; performance = calidad, relevancia y precisión, satisfacción del usuario.
- Valor del LLM en un agente: observar el lenguaje natural, usar herramientas con lenguaje, reflexionar sobre outputs (query con error → corrige → reintenta), instruir sistemas complejos con lenguaje desestructurado.
- ReAct (Reason + Act) es "la arquitectura más simple y fundamental": ciclo Thought → Action → Observation hasta tener información suficiente para la respuesta final.
- Componentes de un agente basado en LLM: (1) memoria y contexto, (2) tools descriptas en el contexto, (3) información contextual (RAG), que puede incrustarse en el prompt o invocarse como herramienta.
- Desafíos de producción: 95%+ de accuracy requerida; la selección de herramientas cae de 92% (5 tools) a 58% (20+ tools); los LLMs cumplen reglas basadas en prompt ~85% del tiempo. "Las fallas en producción vienen de tool design inadecuado, estructuras de memoria y mecanismos de validación — no del modelo en sí."
- MCP: estándar emergente de integración; compatibilidad entre Claude, ChatGPT, Cursor; multi-servidor vía `MultiServerMCPClient`; ciclo estandarizado de descubrimiento, llamada y resultado de herramientas.
- **Sistemas multiagente — limitaciones de un solo agente:** sobrecarga de tools (~92% con 5 → ~58% con 20+), contexto desbordado (información clínica, farmacológica, radiológica y administrativa en un solo contexto degrada el razonamiento), falta de especialización (un único system prompt no puede ser experto en todo).
- Ejemplo de soporte a decisiones clínicas (paciente con NSCLC): agente único con 15+ tools mezcladas, prompt genérico, contexto que se llena rápido y precisión que se degrada vs. multiagente con 3–5 tools por agente, instrucciones por dominio y contexto relevante por agente. "El problema no es la capacidad del LLM, sino la arquitectura. Dividir en agentes especializados es una decisión de ingeniería, no de modelo."
- Definición: "Un sistema multiagente consta de múltiples agentes que interactúan entre sí — de forma colaborativa, competitiva, o ambas — para resolver un problema que excede las capacidades de un agente individual." Ventajas: modularidad, especialización, control. Ejemplos ya vistos: AlphaGo (competitivo), taxi autónomo (competitivo + colaborativo); en biomedicina el patrón típico es colaborativo.
- **Arquitecturas multiagente:** Supervisor (agente central deriva cada consulta; "patrón más común y predecible"); Supervisor tool-calling (los agentes especializados se exponen como tools del supervisor, que usa function calling; "es lo que los alumnos van a implementar en la Parte 3 del proyecto"); Network (todos se comunican con todos; más flexible, menos predecible); Hierarchical (supervisor de supervisores; ejemplo: hospital con departamentos con coordinador interno).
- **Workflows vs agentes — el espectro:** workflows deterministas (prompt chaining, paralelización) → workflows dirigidos por LLM (routing, orchestrator-worker, evaluator-optimizer) → agentes autónomos (ReAct con tool-calling). "La magia está en mezclarlos. Un sistema real puede tener routing determinista entre agentes que internamente son autónomos."
- Memoria: arquitectura de dos niveles (working memory de sesión con `MemorySaver` + `thread_id`, analogía caché L1; long-term memory persistente en vector DB o servicio gestionado). Tres patrones de integración: code-driven (recomendado para empezar), LLM-driven (tool-based), background extraction. Soluciones: Redis Agent Memory Server, Mem0, Zep, LangChain Memory. Patrón universal: store → search → inject.
- Objetivos: construir agentes con `createAgent` de LangChain (ReAct), diseñar servidores MCP con `MultiServerMCPClient`, memoria con `MemorySaver`, reglas determinísticas, detección de PII y mitigación de jailbreak. Ejercicio: elegir problema real → modelarlo formalmente (agente, sensores, actuadores, ambiente, performance) → implementarlo sobre la notebook de práctica.

## Definitions and terminology
- **Agente** (Russell & Norvig): entidad que percibe su entorno mediante sensores y actúa sobre él mediante actuadores.
- **Agente racional**: el que selecciona la acción que maximiza la medida de performance esperada dada la secuencia de percepciones y el conocimiento previo.
- **Sistema multiagente**: múltiples agentes que interactúan (colaborativa, competitivamente o ambas) para un problema que excede a un agente individual.
- **Supervisor / Supervisor (tool-calling) / Network / Hierarchical**: las cuatro arquitecturas multiagente del deck (ver Key claims).
- **Workflow determinista / workflow dirigido por LLM / agente autónomo**: los tres puntos del espectro.
- **ReAct**: Reason + Act, ciclo Thought → Action → Observation.
- **Working memory / long-term memory**; **code-driven / LLM-driven / background extraction**.
- **MCP**: Model Context Protocol.

## Evidence and examples
- Formulaciones PEAS-like: aspiradora (performance: +10 limpiar celda sucia, −1 moverse, −5 aspirar celda limpia, −10 chocar; ambiente grilla n×m parcialmente observable y determinístico), robot móvil (cámara, LiDAR, GPS…), AlphaGo (red neuronal + MCTS, tablero 19×19 determinístico, completamente observable, competitivo).
- AlphaGo → AlphaGo Zero (autojuego, sin datos humanos, red política-valor unificada + MCTS) → AlphaZero (ajedrez, shogi y go con el mismo algoritmo).
- Cifras de producción: 95%+, 92% → 58% (selección de tools), ~85% (cumplimiento de reglas por prompt). Sin fuente citada en la lámina.
- Caso NSCLC (cáncer de pulmón de células no pequeñas) como ejemplo de soporte a decisiones clínicas multiagente.
- Enlaces a AI Tutorial: "Introduction to AI Agents" (aitutorial.dev/agents/intro), "Agent Memory" (aitutorial.dev/agents/memory), guía de ejercicios (aitutorial.dev/agents/hands-on-exercise).
- Bibliografía: Russell & Norvig (2020) AIMA 4th ed.; LangGraph Docs; AI Tutorial – Agents Module; LangChain Memory.

## Inconsistencies / open questions
- [open question] Las cifras de producción (95%+ de accuracy requerida; 92% → 58% de selección de tools de 5 a 20+ herramientas; ~85% de cumplimiento de reglas) no tienen fuente en el deck — se resolvería encontrando el estudio o benchmark del que salen antes de repetirlas en la clase de Ingeniería.
- [verified] La tabla de la lámina 30 (soporte a decisiones clínicas) sale del PDF como una sola línea sin estructura ("Tools 15+ tools mezcladas … Cada agente es experto en lo suyo") — se comparó la extracción `pdftotext -layout` con la del borrador de Paulo, que tiene el mismo texto aplanado; las filas son Tools / System prompt / Contexto / Precisión y las columnas agente único vs. multiagente (reconstrucción en Key claims).
- [verified] El diagrama de ReAct se extrae partido ("Observatio / n") por el layout — es artefacto de extracción del texto dentro de una forma; la palabra es "Observation", como confirma la frase siguiente de la misma lámina.
- [verified] El URL de bibliografía aparece cortado en la lámina ("aitutorial.dev/agents/overvie") — el borrador de Paulo conserva el hipervínculo completo `https://aitutorial.dev/agents/overview`.
- [open question] La lámina de arquitecturas atribuye "Supervisor (tool-calling)" a "la Parte 3 del proyecto" de la materia de biomedicina; para la clase de Ingeniería Informática ese ejemplo no aplica tal cual — a decidir por el presentador.
- [open question] La taxonomía del deck (Supervisor / tool-calling / Network / Hierarchical) no incluye handoffs/swarm ni pipeline, que la charla nueva sí quiere cubrir — se resuelve cruzando con las fuentes de LangGraph/OpenAI Swarm del corpus.
- [open question] Los diagramas vectoriales de las láminas (íconos de tarjetas, diagrama de ReAct, diagramas de arquitecturas dibujados como formas) no son imágenes embebidas y no se extrajeron; solo se extrajeron las 9 imágenes ráster del PDF — se resolvería renderizando las páginas (p. ej. `pdftoppm`) si el presentador quiere las láminas como imagen.

## Images / diagrams

- `aig4b-clase-6-agentes-biomedica.pdf/images/fig-001-000.jpg`
  - Provenance: PDF página 1 (portada), imagen JPEG 421×348 embebida.
  - Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04) — logo institucional de la Universidad Austral (sello con árbol y leyenda «STVDIORVM AVSTRALIS VNIVERSITAS», texto «UNIVERSIDAD AUSTRAL»).
  - Why it matters: n/a
  - Transcribed text: n/a
- `aig4b-clase-6-agentes-biomedica.pdf/images/fig-001-001.png`
  - Provenance: PDF página 1, máscara alfa (smask) de la imagen anterior, 421×348 escala de grises.
  - Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04) — máscara alfa (smask) de otra imagen, sin contenido propio.
  - Why it matters: n/a
  - Transcribed text: n/a
- `aig4b-clase-6-agentes-biomedica.pdf/images/fig-021-002.png`
  - Provenance: PDF página 21, imagen 1200×492 — tarjeta/preview de "Introduction to AI Agents - AI Tutorial" (enlace a aitutorial.dev/agents/intro).
  - Depiction: Tarjeta de vista previa (fondo oscuro con degradé verde, logo «AI» en un círculo arriba a la izquierda) del enlace a aitutorial.dev/agents/intro: categoría «AI Agents», título «Introduction to AI Agents» y subtítulo.
  - Why it matters: Recurso de lectura recomendado en la clase (qué es un agente, loop ReAct, primer agente con tool calling en LangChain); prerrequisito conceptual para la parte multiagente. No aporta contenido más allá del título del enlace.
  - Transcribed text:

    ```text
    AI Agents
    Introduction to AI Agents
    What agents are, the ReAct loop, and building your first agent with LangChain tool calling
    ```

- `aig4b-clase-6-agentes-biomedica.pdf/images/fig-021-003.png`
  - Provenance: PDF página 21, imagen 180×180 (ícono/logo de AI Tutorial, por contexto).
  - Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04) — ícono/logo de AI Tutorial.
  - Why it matters: n/a
  - Transcribed text: n/a
- `aig4b-clase-6-agentes-biomedica.pdf/images/fig-021-004.png`
  - Provenance: PDF página 21, máscara alfa (smask) de la imagen anterior, 180×180.
  - Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04) — máscara alfa (smask) de otra imagen, sin contenido propio.
  - Why it matters: n/a
  - Transcribed text: n/a
- `aig4b-clase-6-agentes-biomedica.pdf/images/fig-032-005.jpg`
  - Provenance: PDF página 32 (lámina "Arquitecturas Multiagente"), JPEG 1068×1600 — la imagen grande de la lámina de arquitecturas.
  - Depiction: Ilustración fotorrealista/3D, sin rótulos: una red de nodos cilíndricos rojos translúcidos e iluminados, conectados por varillas metálicas rojas sobre una superficie blanca; algunos nodos tienen forma de letras o glifos (se distinguen una «G» y formas parecidas a «c» y «a»). No es un diagrama: no hay etiquetas, flechas ni estructura legible.
  - Why it matters: Imagen de ambientación de la lámina «Arquitecturas Multiagente» (metáfora visual de agentes como nodos de una red). No aporta información técnica; el contenido de la lámina está en el texto del record.
  - Transcribed text: (none — no text in image)
- `aig4b-clase-6-agentes-biomedica.pdf/images/fig-038-006.png`
  - Provenance: PDF página 38, imagen 1200×492 — tarjeta/preview de "Agent Memory - AI Tutorial" (enlace a aitutorial.dev/agents/memory).
  - Depiction: Tarjeta de vista previa (mismo diseño que fig-021-002) del enlace a aitutorial.dev/agents/memory: categoría «AI Agents», título «Agent Memory» y subtítulo.
  - Why it matters: Recurso de lectura recomendado sobre memoria de agentes (memoria de trabajo con MemorySaver de LangGraph y memoria de largo plazo entre sesiones). Sólo título del enlace.
  - Transcribed text:

    ```text
    AI Agents
    Agent Memory
    Working memory with MemorySaver and long-term memory for cross-session persistence
    ```

- `aig4b-clase-6-agentes-biomedica.pdf/images/fig-038-007.png`
  - Provenance: PDF página 38, imagen 180×180 (ícono/logo de AI Tutorial, por contexto; mismos bytes de tamaño que fig-021-003).
  - Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04) — ícono/logo de AI Tutorial.
  - Why it matters: n/a
  - Transcribed text: n/a
- `aig4b-clase-6-agentes-biomedica.pdf/images/fig-038-008.png`
  - Provenance: PDF página 38, máscara alfa (smask) de la imagen anterior, 180×180.
  - Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04) — máscara alfa (smask) de otra imagen, sin contenido propio.
  - Why it matters: n/a
  - Transcribed text: n/a

## Raw / preserved excerpts

### Texto completo extraído del PDF (pdftotext -layout, verbatim)

`````markdown
Inteligencia Artificial
Generativa Aplicada en
Biomedicina
Módulo 6: Agents
Profesores: Paulo Veiga / Marco Sanchez Sorondo

Universidad Austral · Facultad de Ingeniería · Departamento de
Inteligencia Artificial

Abril, 2026
Agenda
                                   ¿Qué es un Agente?                1
   Definición formal, racionalidad, ejemplos y tipos de ambientes


                                                                     2   Agentes basados en LLMs
                                                                         Formulación, valor del LLM, arquitectura ReAct y componentes


                            Desafíos de Producción                   3
           Brecha prototipo-producción y Model Context Protocol


                                                                     4   Sistemas Multiagente
                                                                         Limitaciones de un agente, arquitecturas multiagente y el espectro
                                                                         workflows-agentes
                                   Memoria de Agentes                5
 Arquitectura de dos niveles, patrones de integración y soluciones


                                                                     6   Objetivos y Práctica
                                                                         Objetivos de aprendizaje, proyectos prácticos y ejercicio final
 ¿QUÉ ES UN AGENTE?
                                                               Agentes – Una palabra mal
¿Qué es un Agente?                                             utilizada
Antes de hablar de agentes basados en LLMs, necesitamos        En el uso cotidiano, la palabra "agente" se aplica con demasiada frecuencia a
                                                               sistemas basados en LLMs, pero esa simplificación suele ocultar distinciones
entender la definición formal y rigurosa del concepto.
                                                               importantes.

       En IA clásica, un agente es cualquier entidad que              ¿Qué se suele llamar agente?
       percibe su entorno mediante sensores y actúa sobre él
       mediante actuadores. — Russell & Norvig                        En el uso popular, se denomina "agente" simplemente a un LLM o a
                                                                      cualquier sistema basado en LLM, sin más distinción.



                                                                      ¿Por qué esto es incorrecto?
                                                                      Un LLM no es un agente por sí solo. Además, existen muchos tipos de
                                                                      agentes que no involucran en absoluto modelos de lenguaje.



                                                                      ¿Cuál es el camino correcto?
                                                                      Entender la definición formal de agente antes de hablar de agentes
                                                                      basados en LLMs es indispensable para razonar con rigor.
 ¿QUÉ ES UN AGENTE?




   "An agent is anything that can be viewed
   as perceiving its environment through
   sensors and acting upon that environment
   through actuators..."
   — Russell & Norvig, Artificial Intelligence: A Modern Approach


Esta es la definición canónica y punto de partida de toda la teoría de agentes inteligentes en IA clásica.
 ¿QUÉ ES UN AGENTE?



Comentarios sobre la definición
La elegancia de esta definición radica en su amplitud y generalidad. Veamos lo que no menciona:


       Sin ML ni LLMs                                   Sin programas                             Sistemas biológicos
       No se mencionan Machine Learning,                Ni siquiera se mencionan programas o      La definición contempla sistemas
       Deep Learning, LLMs, tools ni RAG. Son           software. Un sistema mecánico o           biológicos: células, humanos, animales
       implementaciones posibles, no la                 electrónico también encaja                e insectos son todos agentes válidos
       definición.                                      perfectamente.                            bajo esta definición.
 ¿QUÉ ES UN AGENTE?




   "A rational agent is one that does the
   right thing... This notion of desirability
   is captured by a performance measure that
   evaluates any given sequence of
   environment states."
   — Russell & Norvig, Artificial Intelligence: A Modern Approach


La racionalidad introduce el concepto de optimización: no basta con percibir y actuar, hay que hacerlo bien según un criterio definido.
 ¿QUÉ ES UN AGENTE?



Racionalidad
Un agente racional selecciona la acción que maximiza su medida de performance, dada la evidencia de sus percepciones y su conocimiento previo.
La racionalidad depende de cuatro factores clave:


       Medida de performance                                                   Conocimiento previo
       El criterio que define el éxito del agente. Sin esta medida, no hay     Lo que el agente ya sabe sobre el ambiente antes de comenzar a
       racionalidad posible.                                                   actuar.



       Acciones disponibles                                                    Secuencia de percepciones
       El conjunto de acciones que el agente puede ejecutar en su              El historial de todo lo que el agente ha observado del ambiente
       entorno.                                                                hasta el momento.
 ¿QUÉ ES UN AGENTE?



Ejemplo: Vacuum Cleaner
Formulación como agente inteligente — Mantener limpio un entorno (grilla n×m) eliminando la suciedad con el mínimo de acciones posibles.


  Agente                       Aspiradora autónoma (robot o modelo abstracto)

  Sensores                     Detector de suciedad, posición actual en la grilla

  Actuadores                   Motor de movimiento (izq/der/adelante/atrás), motor de succión

  Ambiente                     Grilla n×m, parcialmente observable, determinístico

  Acciones                     Aspirar, MoverIzquierda, MoverDerecha, Esperar

  Performance                  +10 limpiar celda sucia · −1 moverse · −5 aspirar celda limpia · −10 chocar
 ¿QUÉ ES UN AGENTE?



Ejemplo: Robot Móvil
Formulación como agente inteligente — Desplazarse desde un punto inicial hasta un destino evitando obstáculos en entornos complejos.


  Agente                      Robot móvil autónomo con sistema de control y planificación

  Sensores                    Cámara, LiDAR, GPS, giroscopio, sensores de proximidad

  Actuadores                  Motores de tracción, dirección, frenos, brazo robótico

  Ambiente                    Entorno físico (indoor/outdoor), continuo, parcialmente observable, dinámico

  Acciones                    Avanzar, girar, frenar, recalcular ruta

  Performance                 Llegar al destino rápido, sin colisiones y con mínimo consumo de energía
 ¿QUÉ ES UN AGENTE?



Ejemplo: DeepMind AlphaGo
Formulación como agente inteligente — Jugar al Go a nivel superhumano mediante redes neuronales profundas y búsqueda Monte Carlo.


  Agente                      Red neuronal profunda + búsqueda Monte Carlo (MCTS)

  Sensores                    Estado actual del tablero (disposición de fichas blancas y negras)

  Actuadores                  Colocar una piedra en una intersección válida o pasar turno

  Ambiente                    Tablero de Go 19×19, determinístico, completamente observable, competitivo

  Performance                 Probabilidad de victoria en la partida
 ¿QUÉ ES UN AGENTE?



De AlphaGo Zero a AlphaZero
La evolución de AlphaGo ilustra uno de los saltos más significativos en la historia de los agentes inteligentes: pasar del aprendizaje con datos
humanos a la generalización pura.


       AlphaGo                                            AlphaGo Zero                                       AlphaZero
       Aprende de partidas humanas. Requiere              Aprende desde cero sin datos humanos,              Generaliza a múltiples juegos (ajedrez,
       datos de expertos como punto de                    solo autojuego y retroalimentación. Red            shogi, go) sin conocimiento previo.
       partida.                                           neuronal unificada política-valor +                Mismo algoritmo, distintos juegos.
                                                          MCTS.


       La métrica de performance es universal: tasa de victorias (ganar > empatar > perder).
 ¿QUÉ ES UN AGENTE?



Tipos de Ambientes
La naturaleza del ambiente determina en gran medida la complejidad del agente necesario para operar en él. Estas son las dimensiones
fundamentales de clasificación:


       Observable                                       Agentes                                          Determinismo
       Completamente observable vs.                     Un agente vs. Multi-agente                       Determinístico vs. Estocástico
       Parcialmente observable



       Episódico vs.                                    Estático vs. Dinámico                            Discreto vs. Continuo
       Secuencial                                       El ambiente cambia o no mientras el              Estados y acciones finitos vs. infinitos
       Acciones independientes vs. acciones             agente delibera
       con consecuencias a largo plazo



       Conocido vs.
       Desconocido
       El agente conoce o no las reglas del
       ambiente
 ¿QUÉ ES UN AGENTE?



Dificultad de Ambientes
Las dimensiones del ambiente se combinan para determinar cuán desafiante resulta operar en él. El espectro va de problemas triviales a
extraordinariamente complejos.


                                                  Crucigrama
                                   1
                                                  Fácil: observable, determinístico, estático. Un solo agente.



                                                              Ajedrez
                                   2                          Medio: observable y determinístico, pero competitivo. Requiere anticipar al
                                                              oponente.



                                                                           Taxi Autónomo
                                   3                                       Difícil: parcialmente observable, estocástico, dinámico, continuo,
                                                                           multi-agente.
 ¿QUÉ ES UN AGENTE?



¿Por qué todas estas definiciones?
La formalización agentica no es un ejercicio académico vacío. Tiene tres utilidades prácticas concretas y poderosas:


       Análisis riguroso                                 Reutilización de                                  Decisión informada
       Nos obliga a pensar bien en el problema           frameworks                                        Es fundamental saber cuándo vale la
       a resolver y analizar todos sus aspectos          Permite usar frameworks agnósticos                pena usar un agente y cuándo una
       antes de implementar.                             que resuelven la formulación agentica.            solución más simple es suficiente.
                                                         Un mismo algoritmo puede ganar en
                                                         ajedrez y dirigir un robot.
 ¿QUÉ ES UN AGENTE?



¿Cuándo vale la pena usar agentes?
Los agentes no son la solución a todo. Estas son las condiciones que justifican su uso frente a soluciones determinísticas más simples:

       Múltiples herramientas en orden                                            Interpretación dinámica de resultados
       variable                                                                   Cuando hay que interpretar y relacionar apropiadamente
       Cuando la solución requiere usar varias herramientas, en                   resultados en tiempo de ejecución, adaptando el
       múltiples órdenes y de distintas maneras según el contexto.                comportamiento.


       Orquestación variable de sistemas                                          Solución determinística insuficiente
       Cuando hay que sincronizar y/u orquestar distintos sistemas de             Cuando el espacio de posibilidades es demasiado grande o
       manera variable según las circunstancias.                                  dinámico para ser cubierto con reglas fijas.
AGENDA



Agenda
                                           ¿Qué es un Agente?                1
           Definición formal, racionalidad, ejemplos y tipos de ambientes


                                                                             2   Agentes basados en LLMs
                                                                                 Formulación, valor del LLM, arquitectura ReAct y componentes


                                    Desafíos de Producción                   3
                   Brecha prototipo-producción y Model Context Protocol


                                                                             4   Sistemas Multiagente
                                                                                 Limitaciones de un agente, arquitecturas multiagente y el espectro
                                                                                 workflows-agentes
                                           Memoria de Agentes                5
         Arquitectura de dos niveles, patrones de integración y soluciones


                                                                             6   Objetivos y Práctica
                                                                                 Objetivos de aprendizaje, proyectos prácticos y ejercicio final
 AGENTES BASADOS EN LLMS



Agentes basados en LLMs
Con la base teórica asentada, exploramos cómo los modelos de lenguaje encajan en el marco formal de agentes inteligentes.
 AGENTES BASADOS EN LLMS



Agentes basados en LLMs
Formulación como agente inteligente — Resolver tareas lingüísticas o de razonamiento a partir de instrucciones en lenguaje natural.


  Agente                       Modelo de lenguaje grande (LLM) con razonamiento, memoria y acceso a herramientas externas

  Sensores                     Texto de entrada del usuario, contexto previo, resultados de herramientas

  Actuadores                   Generar texto, razonar, ejecutar comandos, llamar APIs, producir planes

  Ambiente                     Entorno digital, simbólico, parcialmente observable, dinámico

  Performance                  Calidad, relevancia y precisión de respuestas; satisfacción del usuario
 AGENTES BASADOS EN LLMS



¿Cuál es el valor de un LLM en un agente?
El LLM no es simplemente un chatbot dentro de un agente. Su valor radica en capacidades genuinamente novedosas que ningún sistema anterior
podía ofrecer:




Observar el lenguaje natural                                              Usar herramientas con lenguaje
Abre las puertas a un agente genérico para "percibir" el ambiente del     Emplea el lenguaje natural como medio universal para interactuar con
lenguaje natural y actuar en él de forma fluida.                          herramientas de cualquier tipo y API.




Reflexionar sobre outputs                                                 Instruir sistemas complejos
Puede analizar el resultado de una herramienta (ej: query con error   →   Permite comunicarse con sistemas informáticos complejos usando
corrige   → reintenta) en un ciclo reflexivo.                             lenguaje desestructurado y natural.
 AGENTES BASADOS EN LLMS



Arquitectura ReAct (Reason + Act)
ReAct es la arquitectura más simple y fundamental para agentes basados en LLMs. Combina razonamiento y acción en un ciclo iterativo hasta alcanzar una
respuesta final.




                                                                          Observatio
                       Thought                     Action                                               Razonar                  Respuesta
                                                                              n


El ciclo Thought   → Action → Observation se repite hasta que el agente determina que tiene suficiente información para producir una respuesta final de calidad.
   AI Tutorial

Introduction to AI Agents - AI Tutorial
What agents are, the ReAct loop, and building your first agent with LangChain tool calling
 AGENTES BASADOS EN LLMS



Componentes de un Agente basado en LLM
Todo agente basado en LLM se construye sobre tres componentes esenciales que definen qué sabe, qué puede hacer y de qué contexto dispone:


      1. Memoria y Contexto                           2. Tools (Herramientas)                         3. Información
      Historial de conversación, último               Conjunto de herramientas a las que              Contextual (RAG)
      prompt y contexto activo. Es la                 puede llamar, descriptas en el contexto.        Información asociada al historial
      "conciencia" inmediata del agente sobre         El agente decide cuándo y cómo                  mediante recuperación semántica.
      la situación actual.                            invocarlas.                                     Puede incrustarse en el prompt o
                                                                                                      invocarse como herramienta.
AGENDA



Agenda
                                           ¿Qué es un Agente?                1
           Definición formal, racionalidad, ejemplos y tipos de ambientes


                                                                             2   Agentes basados en LLMs
                                                                                 Formulación, valor del LLM, arquitectura ReAct y componentes


                                    Desafíos de Producción                   3
                   Brecha prototipo-producción y Model Context Protocol


                                                                             4   Sistemas Multiagente
                                                                                 Limitaciones de un agente, arquitecturas multiagente y el espectro
                                                                                 workflows-agentes
                                           Memoria de Agentes                5
         Arquitectura de dos niveles, patrones de integración y soluciones


                                                                             6   Objetivos y Práctica
                                                                                 Objetivos de aprendizaje, proyectos prácticos y ejercicio final
 DESAFÍOS DE PRODUCCIÓN



Desafíos de Producción
Llevar agentes del prototipo funcional a un sistema de producción confiable es uno de los mayores retos de la ingeniería de IA actual.
 DESAFÍOS DE PRODUCCIÓN



¿Por qué importa en producción?
Existe una brecha significativa entre un demo que funciona y un sistema de producción confiable. Los datos son reveladores:



              95%+                                                58%                                            ~85%
        Accuracy requerida                       Tool selection con 20+ tools                                Rule enforcement
El umbral mínimo para sistemas de producción      La accuracy de selección de herramientas cae      Los LLMs cumplen reglas basadas en prompt
confiables. Los demos funcionales no llegan a      de 92% (5 tools) a solo 58% con más de 20        el 85% del tiempo. Insuficiente para sectores
                  este nivel.                               herramientas disponibles.                                regulados.


       Las fallas en producción vienen de tool design inadecuado, estructuras de memoria y mecanismos de validación — no del modelo en sí.
 DESAFÍOS DE PRODUCCIÓN



MCP: Model Context Protocol
El Model Context Protocol es el estándar emergente de integración para agentes, diseñado para resolver la fragmentación del ecosistema y
garantizar interoperabilidad a largo plazo.


   Estándar universal                                                       Servidores MCP
   Asegura compatibilidad entre Claude, ChatGPT, Cursor y futuras           Permite diseñar y operar servidores MCP con especificaciones
   plataformas. Diseña una vez, integra en todas partes.                    completas de herramientas, recursos y capacidades.



   Multi-servidor                                                           Ciclo estandarizado
   Los agentes pueden integrarse con múltiples servidores MCP               Define cómo los agentes descubren, llaman y reciben resultados
   simultáneamente via MultiServerMCPClient.                                de herramientas de manera consistente.
AGENDA



Agenda
                                           ¿Qué es un Agente?                1
           Definición formal, racionalidad, ejemplos y tipos de ambientes


                                                                             2   Agentes basados en LLMs
                                                                                 Formulación, valor del LLM, arquitectura ReAct y componentes


                                    Desafíos de Producción                   3
                   Brecha prototipo-producción y Model Context Protocol


                                                                             4   Sistemas Multiagente
                                                                                 Limitaciones de un agente, arquitecturas multiagente y el espectro
                                                                                 workflows-agentes
                                           Memoria de Agentes                5
         Arquitectura de dos niveles, patrones de integración y soluciones


                                                                             6   Objetivos y Práctica
                                                                                 Objetivos de aprendizaje, proyectos prácticos y ejercicio final
 SISTEMAS MULTIAGENTE



Sistemas Multiagente
Cuando un solo agente no alcanza: motivación, arquitecturas y aplicación en biomedicina.
 SISTEMAS MULTIAGENTE



Limitaciones de un solo agente
Ya vimos que un agente con tools puede resolver problemas complejos. Pero a medida que crece el número de herramientas y dominios, aparecen
problemas concretos:




  Sobrecarga de tools                            Contexto desbordado                             Falta de especialización
  La accuracy de selección de herramientas       Si el agente debe manejar información           Un único system prompt no puede ser
  cae drásticamente cuando el agente tiene       clínica, farmacológica, radiológica y           simultáneamente experto en interacciones
  demasiadas opciones (de ~92% con 5             administrativa en un solo contexto, la          farmacológicas Y en interpretación de
  tools a ~58% con 20+). Un agente               calidad de razonamiento se degrada.             ensayos clínicos Y en análisis de
  generalista pierde precisión.                                                                  imágenes.
 SISTEMAS MULTIAGENTE



Ejemplo: Soporte a Decisiones Clínicas
Queremos asistir a un equipo médico en la toma de decisiones para un paciente con cáncer de pulmón (NSCLC), integrando datos clínicos,
farmacológicos y de evidencia.

Tools 15+ tools mezcladas de todos los dominios 3–5 tools por agente, especializadas System prompt Genérico, intenta cubrir todo Cada agente
tiene instrucciones de su dominio Contexto Se llena rápidamente con info de todos los dominios Cada agente mantiene solo su contexto relevante
Precisión Se degrada con la complejidad Cada agente es experto en lo suyo




El problema no es la capacidad del LLM, sino la arquitectura. Dividir en agentes especializados es una decisión de ingeniería, no de modelo.
 SISTEMAS MULTIAGENTE



¿Qué es un Sistema Multiagente?
Un sistema multiagente consta de múltiples agentes que interactúan entre sí — de forma colaborativa, competitiva, o ambas — para resolver un
problema que excede las capacidades de un agente individual.




  Modularidad                                      Especialización                                   Control
  Agentes independientes facilitan el              Cada agente tiene su propio dominio de            Se define explícitamente cómo se
  desarrollo, testing y mantenimiento. Se          expertise, sus tools y su system prompt           comunican los agentes y quién decide el
  puede mejorar un agente sin tocar los            optimizado para una tarea concreta.               flujo, en vez de depender de un único LLM
  demás.                                                                                             para todo.


Ya vimos ejemplos multiagente: AlphaGo (competitivo), Taxi Autónomo (competitivo + colaborativo). En biomedicina, el patrón típico es
colaborativo.
 SISTEMAS MULTIAGENTE



Arquitecturas Multiagente
Hay varias formas de conectar agentes. La elección depende del nivel de control, complejidad y autonomía
que necesite el sistema.


          Supervisor
          Un agente central decide a qué agente especializado derivar cada consulta. Patrón más
          común y predecible. Ejemplo: un agente coordinador recibe la pregunta del médico y la deriva
          al agente clínico o al farmacológico según corresponda.



          Supervisor (tool-calling)
          Los agentes especializados se exponen como tools del supervisor. El LLM supervisor usa
          function calling para invocarlos. Ejemplo: es lo que los alumnos van a implementar en la
          Parte 3 del proyecto.



          Network
          Todos los agentes se comunican entre sí. Más flexible pero menos predecible. Ejemplo:
          agente clínico y farmacológico dialogan directamente para resolver una interacción.



          Hierarchical
          Supervisor de supervisores. Para sistemas muy complejos. Ejemplo: hospital con
          departamentos, cada uno con su coordinador interno.
 SISTEMAS MULTIAGENTE



Workflows vs Agentes — El espectro
No todo sistema con múltiples LLMs es un 'agente'. Existe un espectro entre flujos deterministas y agentes autónomos.


  Workflows (deterministas)                        Workflows (dirigidos por                         Agentes (autónomos)
  Rutas de código predefinidas. El LLM se          LLM)                                             El LLM decide sus propias acciones
  embebe en pasos fijos.                           El LLM dirige el flujo entre rutas               basado en feedback del ambiente.
                                                   predefinidas.
  Patrones: prompt chaining, paralelización.                                                        Patrón: ReAct con tool-calling.
                                                   Patrones: routing, orchestrator-worker,
  Ejemplo: Pipeline que siempre ejecuta                                                             Ejemplo: El agente decide qué tools usar,
                → verificación
  análisis clínico
                                                   evaluator-optimizer.
                                                                                                    en qué orden, y cuándo tiene suficiente
  farmacológica → informe.                         Ejemplo: Un router decide si la pregunta va      información para responder.
                                                   al agente clínico o al farmacológico.


La magia está en mezclarlos. Un sistema real puede tener routing determinista entre agentes que internamente son autónomos.
AGENDA



Agenda
                                           ¿Qué es un Agente?                1
           Definición formal, racionalidad, ejemplos y tipos de ambientes


                                                                             2   Agentes basados en LLMs
                                                                                 Formulación, valor del LLM, arquitectura ReAct y componentes


                                    Desafíos de Producción                   3
                   Brecha prototipo-producción y Model Context Protocol


                                                                             4   Sistemas Multiagente
                                                                                 Limitaciones de un agente, arquitecturas multiagente y el espectro
                                                                                 workflows-agentes
                                           Memoria de Agentes                5
         Arquitectura de dos niveles, patrones de integración y soluciones


                                                                             6   Objetivos y Práctica
                                                                                 Objetivos de aprendizaje, proyectos prácticos y ejercicio final
 MEMORIA DE AGENTES



Memoria de Agentes
La memoria es uno de los componentes más críticos y menos intuitivos de los agentes en producción. Sin una estrategia adecuada, los agentes son
caros, incoherentes y frustrantes.
 MEMORIA DE AGENTES



Arquitectura de Memoria: Dos Niveles
La solución al problema de memoria es una arquitectura que combina velocidad con persistencia, inspirada en los sistemas de caché de hardware:


  Working Memory (Sesión)                                                Long-Term Memory (Persistente)
  Duración: Una sola sesión activa                                       Duración: Entre sesiones, indefinidamente
  Propósito: Estado activo de conversación                               Propósito: Conocimiento persistente del usuario
  Ejemplo: Detalles del pedido en el chat actual                         Ejemplo: Preferencias de usuario a lo largo de meses
  Implementación: MemorySaver + thread_id                                Implementación: Vector DB o servicio gestionado
  Analogía: Caché L1 — rápida y temporal                                 Analogía: Base de datos — persistente y buscable
 MEMORIA DE AGENTES



Patrones de Integración de Memoria
Existen tres patrones principales para integrar la memoria en un agente, con distintos niveles de control y autonomía:

01                                                02                                                 03

Code-Driven (Programático)                        LLM-Driven (Tool-Based)                            Background Extraction
Tu código decide explícitamente cuándo            El agente recibe tools de memoria y decide         (Automático)
guardar y recuperar. Comportamiento               autónomamente qué recordar. Más natural y          Almacena toda la conversación; procesos en
predecible y eficiente. Punto de partida          flexible, pero menos predecible.                   segundo plano extraen hechos importantes de
recomendado.                                                                                         forma asíncrona.



       Recomendación: Empezar con code-driven, agregar background extraction para enriquecimiento, y usar LLM-driven cuando la autonomía
       sea un requisito funcional.
   AI Tutorial

Agent Memory - AI Tutorial
Working memory with MemorySaver and long-term memory for cross-session persistence
 MEMORIA DE AGENTES



Soluciones de Memoria en Producción
El ecosistema de memoria para agentes ha madurado rápidamente. Estas son las soluciones más relevantes y el patrón universal que todas implementan:




  Redis Agent Memory Server                                                       Mem0
  Working + long-term con búsqueda semántica integrada. Alta                      Capa de memoria gestionada para agentes. API simple, ideal para
  performance para producción.                                                    integración rápida.




  Zep                                                                             LangChain Memory
  Long-term memory con extracción automática de hechos desde                      Integración nativa con LangChain/LangSmith. La opción más directa si
  conversaciones.                                                                 ya usás el stack de LangChain.



      Patrón universal: store   → search → inject en prompt o tool results. Independientemente de la solución elegida, este flujo es constante.
AGENDA



Agenda
                                           ¿Qué es un Agente?                1
           Definición formal, racionalidad, ejemplos y tipos de ambientes


                                                                             2   Agentes basados en LLMs
                                                                                 Formulación, valor del LLM, arquitectura ReAct y componentes


                                    Desafíos de Producción                   3
                   Brecha prototipo-producción y Model Context Protocol


                                                                             4   Sistemas Multiagente
                                                                                 Limitaciones de un agente, arquitecturas multiagente y el espectro
                                                                                 workflows-agentes
                                           Memoria de Agentes                5
         Arquitectura de dos niveles, patrones de integración y soluciones


                                                                             6   Objetivos y Práctica
                                                                                 Objetivos de aprendizaje, proyectos prácticos y ejercicio final
 OBJETIVOS Y PRÁCTICA



Objetivos y Práctica
Esta parte del módulo traduce toda la teoría en competencias concretas y proyectos prácticos implementables.
 OBJETIVOS Y PRÁCTICA



Objetivos de Aprendizaje
Al finalizar este módulo, el estudiante será capaz de diseñar, implementar y operar agentes basados en LLMs en entornos de producción:


       Construir agentes con                            Diseñar y operar                                 Implementar memoria y
       tool capabilities                                servidores MCP                                   seguridad
       Usando createAgent de LangChain con              Con especificaciones completas e                 Memoria con MemorySaver, reglas de
       patrones ReAct completos.                        integración multi-servidor via                   negocio determinísticas, detección de
                                                        MultiServerMCPClient.                            PII y mitigación de jailbreak.
 OBJETIVOS Y PRÁCTICA



Ejercicio Práctico
El siguiente ejercicio busca integrar todos los conceptos del módulo en un problema original elegido por cada estudiante:


             Paso 1: Elegir un problema
    1        Pensar en un problema real a ser resuelto por un agente basado en LLMs. Cuanto más cercano a la realidad, mejor.


             Paso 2: Modelar como agente
    2        Formularlo con las definiciones formales: agente, sensores, actuadores, ambiente y medida de performance.


             Paso 3: Implementar
    3        Resolverlo usando como base la notebook de la práctica. Se puede usar información hardcodeada (JSONs, CSVs, .txt, etc.).


Guia de ejercicios: https://aitutorial.dev/agents/hands-on-exercise
 OBJETIVOS Y PRÁCTICA



Bibliografía y Recursos
Recursos fundamentales para profundizar en los conceptos de este módulo:


   Russell & Norvig (2020)                                                 LangGraph Docs
   Artificial Intelligence: A Modern Approach, 4th ed. Pearson. La         Documentación oficial del framework para construcción de
   referencia canónica para la teoría formal de agentes inteligentes.      agentes stateful con grafos. langchain-ai.github.io/langgraph



   AI Tutorial – Agents Module                                             LangChain Memory
   Guía práctica sobre el módulo de agentes con ejemplos de código.        Documentación de los módulos de memoria de LangChain para
   aitutorial.dev/agents/overvie                                           agentes. python.langchain.com/docs/modules/memory
`````
