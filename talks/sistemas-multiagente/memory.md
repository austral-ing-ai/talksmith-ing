# memory.md — sistemas-multiagente

**Current step:** 5 — Review awaiting_presenter
**Awaiting:** 2026-10-04 — Traspaso de Marco a Paulo. La revisión sigue abierta: el próximo presentador puede mandar más feedback o decir "listo" para pasar a Polish (Step 6). Pendientes: (1) armar el repo de la demo en vivo (design/, code/, outreach/; propuesta: empresa Pampa Viajes; sin decidir si va en un repo aparte o en demos/pampa-viajes/); (2) la vista HTML (output/html/) está una ronda atrás: no incluye el split de "Tipos de ambiente"; regenerar antes de mostrarla; (3) confirmar las Open questions que se apoyan en AIMA cap. 2 (PEAS, autonomía, medida de performance fijada por el diseñador) y las celdas de la tabla de ambientes del asistente LLM; (4) reverificar versiones y defaults de Claude Code el 2026-10-06 (lista en las notas de 5.6/5.7); (5) la misión del TP está como documento de diseño en missions/sistemas-multiagente/idea.md, sin enunciado.
**Mode:** C (Presenter Outline: Marco aprobó bloques y títulos antes de redactar)
**Topic:** Agentes y sistemas multiagente para Ing. Informática y Ciencia de Datos: versión más completa y formal de la clase 6 de AIG4B, con implementaciones reales de distintas arquitecturas, y TP multiagente sobre un benchmark con un LLM débil.
**Folder:** talks/sistemas-multiagente/
**Started:** 2026-10-04

---

## Talk briefing

"vamos a hacer una version mas completa y refinada de esta clase de Agentes, que dimos el cuatrimestre pasado para Ingenieria Biomedica y ahora la vamos a dar para estos alumnos de Ingenieria Informatica y Ciencia de Datos

recorda que ya vimos MCP y RAG, asique esta clase va a ser algo mas formal y el trabajo práctico va a implicar reutilizar estas tecnologías creando un sistema multiagente (quizas varias arquitecturas para resolver un benchmark usando un "LLM malo" en donde la especializacion y aislamiento de contexto se use para poder resolver los problemas del benchmark bajo restricciones)"

"ponele sistemas multiagente. queremos agregar tambien ejemplos de implementaciones reales de sistemas multiagente con distintas artquitecturas en la clase
por otro lado tambien en la parte practica si bien el enfoque va a ser en agentes basados en LLM tambien quizas agreguemos agentes no basados en LLMs como parte requerida del sistema"

Contexto: clase 12 del README (miércoles 2026-10-28, "Agentes"). Ya dictadas: prompting (clase 5), RAG (6), MCP (7), transformers (8), entrenamiento de LLMs (9). La fuente base es el PDF de la clase 6 de AIG4B (Biomédica, abril 2026, Veiga/Sorondo) y su draft textual en `talksmith-aig4b`.

---

## 2026-10-04 — Step 1 (Frame)
- Status: complete
- Asks log:
  - 2026-10-04 — "¿Qué nombre le ponemos a la carpeta de la clase?" → "sistemas multiagente"
- What was decided: carpeta `talks/sistemas-multiagente/`; la clase suma implementaciones reales de MAS con distintas arquitecturas; el TP (misión aparte) puede exigir agentes no basados en LLM como parte del sistema.
- Key inputs: PDF de AIG4B clase 6; draft de Paulo.
- Files created/modified: memory.md; árbol de carpetas.
- Pending open questions: none

## 2026-10-04 — Step 2 (Collect)
- Status: complete
- Asks log:
  - 2026-10-04 — "¿Capturo las fuentes propuestas de sistemas multiagente reales?" → "me gusta todo" (todas). Pedido nuevo: por cada arquitectura base (orquestador, tool-use, swarm, etc.) un ejemplo ficticio con reparto de roles fácil de entender, mostrando cómo se reparten los roles en cada arquitectura, con ventajas y desventajas.
- What was decided: capturar las 22 fuentes propuestas (Anthropic multi-agent research + context engineering, subagentes de Claude Code, Magentic-One, MetaGPT, ChatDev, AutoGen, OpenAI Agents SDK multi-agent + handoffs, OpenAI Swarm, LangGraph Swarm, multiagent debate, Mixture-of-Agents, Generative Agents, Cognition, MAST, Agentless, OpenAI Five, AlphaStar, Contract Net, BDI, Kiva/Wurman 2008). Los ejemplos ficticios por arquitectura se escriben en el Draft, sin fuente.
- Key inputs: copiados a research/articles el PDF de Biomédica y el draft de Paulo; a research/web las 15 capturas web de Paulo (AIMA, ReAct, Building effective agents, LangGraph multi-agent, MCP spec, Mem0, Zep, AlphaGo Zero/AlphaZero, etc.).
- Files created/modified: research/articles/*, research/web/* (37 capturas)
- Pending open questions: none
- Asks log (cierre): 2026-10-04 — "¿Paso a armar la base de conocimiento?" → "si, segui"

## 2026-10-04 — Step 3 (Corpus)
- Status: complete
- Asks log:
  - 2026-10-04 — "¿Transcribo las imágenes de las fuentes?" → "1": solo los diagramas con contenido; logos y chrome marcados como decorativos
- What was decided: corpus completo, 0 marcadores pendientes; diagramas con contenido transcriptos (~150), chrome marcado decorativo.
- Key inputs: 41 fuentes, procesadas en 5 tandas paralelas (solo texto en la fase 1); 41 registros de corpus, ~280 imágenes pendientes (~45% logos y chrome).
- Pedido nuevo de Marco (2026-10-04, verbatim): "tambien quiero que se haga mencion explicita a la arquitectura "mas robusta" y flexible para hacerlo: un agente principal que en principio hace todo y tiene un LLM muy pesado y costoso atrás, y crea o despierta o manda un mensaje a subagentes u otros agentes de manera on-demand, aprovechando tambien paralelismo. quizas hagamos un ejemplo en vivo con claude code (mensajes entre sesiones, subagentes, etc)"
- Fuente agregada por ese pedido: research/web/claude-code-agent-teams/ (docs de Claude Code, agent teams).
- Files created/modified: research/corpus/*.md (44 registros) + carpetas de imágenes
- Pending open questions: hallazgos para el draft — (1) los números de la clase de Biomédica (95%, 92%→58% con 20+ tools, 85% de reglas) no tienen fuente: sacarlos o reemplazarlos por MAST; (2) OpenAI Five = 5 copias de una red con parámetros compartidos, draft/ítems programados; AlphaStar multiagente solo en entrenamiento (liga); (3) Anthropic (+90,2%) vs Cognition coinciden en el motivo: paralelo de solo lectura sí, código con dependencias no; (4) handoffs comparten todo el historial por defecto en OpenAI SDK, Swarm y LangGraph; (5) no citar Elo exactos de AlphaGo Zero; MAST: citar los % de §4; (6) Swarm de OpenAI está deprecado (reemplazado por el Agents SDK); (7) agent teams experimental (CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1, tmux/iTerm2), cross-session messaging activo por defecto; re-verificar versiones antes de la demo.

## 2026-10-04 — Step 4 (Draft)
- Status: complete
- Asks log:
  - 2026-10-04 — "Nombre de la clase, fecha y modo de borrador" → class: "Sistemas multiagente: especialización, contexto y orquestación". Duda sobre el número ("Clase 12? Crei que vamos menos"). Pide primero bloques temáticos y título de cada diapositiva antes de redactar.
  - 2026-10-04 — "Propuesta de bloques y títulos" → "Me gusta aunque los bloques 6 y 7 tienen que ser mas resumidos y cortos" → resumidos a 2 láminas cada uno
  - 2026-10-04 — "Fecha" → "me parece bien. la clase será el miercoles 7" → 2026-10-07 (adelanta Agentes, que el README tenía en la clase 12)
- What was decided: class "Sistemas multiagente: especialización, contexto y orquestación" (sin número de clase); date 2026-10-07; Modo C con el esquema aprobado de 8 bloques y 42 láminas (ver Esquema aprobado abajo). Ejemplo ficticio transversal: "Pampa Viajes" (vuelos, alojamiento, actividades, presupuesto; presupuesto = agente sin LLM, reglas). Sale de la clase de Biomédica: sección MCP (vista en clase 7), memoria como bloque propio (queda en láminas de pizarra y aislamiento), cifras sin fuente.
- Key inputs: nota de Marco para el TP (verbatim): "vamos a pedirles reportar con logs también auditabilidad, rendimiento, uso de tokens, colaboración distribuida entre miembros del grupo en github (medimos esto para notas conceptuales de cada alumno), y demas conceptos de desarrollo, arquitectura y eficiencia importante"
- Files created/modified: draft.md (borrador completo en Modo C: frontmatter, tesis, agenda, 8 bloques y 42 láminas según el esquema aprobado; 11 diagramas ASCII, 10 imágenes del corpus, 1 directiva generate-image; anti-slop con desrobotizar aplicado al redactar; cifras sin fuente de Biomédica movidas a Cut material). Revisión del Composer (scope full) aplicada el 2026-10-04: 2 blockers, 9 majors y todos los minors; tiempos por lámina suman ~82 de 90 min; agente sin LLM y cantidad de arquitecturas del TP en condicional y en Open questions.
- Pending open questions: TP: ¿al menos dos arquitecturas multiagente + línea de base? ¿agente sin LLM obligatorio? (quizás); escenario de la demo (sesión principal + subagentes Explore sobre missions/rag-mcp-transformers y missions/prompting, luego mensajes entre sesiones); 12 títulos > 40 caracteres; PEAS sin fuente directa; reverificar datos de Claude Code el 2026-10-06; ¿actualizar README (la clase ocupa el 7/10, lugar de la clase 10)?
- Composer scope=full: 2 blockers, 9 majors, 17 minors, todos aplicados.

### Esquema aprobado (2026-10-04)
B1 Qué es un agente, formalmente: 1 Agente: percibe y actúa (Russell & Norvig) · 2 Racionalidad y medida de performance (PEAS) · 3 Tipos de ambiente, entre ellos el multiagente cooperativo y el competitivo · 4 Arquitecturas clásicas: reflejo, con modelo, con objetivos, con utilidad, BDI · 5 El agente basado en LLM leído con la misma definición · 6 El ciclo ReAct · 7 Workflow o agente: quién decide el próximo paso
B2 Por qué un solo agente no alcanza: 8 El contexto es un recurso finito · 9 Demasiadas herramientas se interfieren · 10 Un solo system prompt no puede ser experto en todo · 11 Las tres palancas: especialización, aislamiento de contexto, paralelismo · 12 Qué es un sistema multiagente
B3 Arquitecturas base con el mismo ejemplo (reparto de roles en Pampa Viajes + ventajas/desventajas): 13 El caso Pampa Viajes · 14 Agente único con todas las herramientas (línea de base) · 15 Pipeline · 16 Router · 17 Orquestador y trabajadores (agentes como herramientas) · 18 Handoffs y swarm · 19 Red y pizarra compartida · 20 Jerárquica · 21 Las mismas tareas medidas: llamadas, tokens y control (tabla LangGraph) · 22 Cómo elegir
B4 Implementaciones reales: 23 MetaGPT · 24 ChatDev · 25 AutoGen · 26 Magentic-One · 27 Debate y Mixture-of-Agents · 28 Generative Agents · 29 OpenAI Agents SDK (el del TP)
B5 El agente principal que delega bajo demanda: 30 Agente principal caro que despierta subagentes · 31 Sistema de investigación de Anthropic · 32 Lo que cuesta · 33 Contrapunto Cognition · 34 Dónde coinciden · 35 Claude Code: subagentes, equipos, mensajes entre sesiones · 36 Demo en vivo
B6 Sin LLM (resumido): 37 Multiagente antes de los LLM (4 tarjetas: Contract Net, Kiva, OpenAI Five, AlphaStar) · 38 Agentes simbólicos dentro de un sistema con LLM
B7 Cómo fallan (resumido): 39 Cómo fallan (MAST 3 categorías + traza + Agentless en una línea) · 40 El aislamiento no viene de fábrica
B8 Cierre: 41 Lo que hay que llevarse · 42 El TP: LLM débil, benchmark, varias arquitecturas (+ logs, auditabilidad, rendimiento, tokens, colaboración en GitHub)


## 2026-10-04 — Step 5 (Review)
- Status: awaiting_presenter
- Asks log:
  - 2026-10-04 — "partilo en laminas" (Tipos de ambiente) → aplicado: 1.8 "Tipos de ambiente" + 1.9 "Más dimensiones del ambiente"; deck en 49 láminas, 84 de 90 min.
  - 2026-10-04 — "ahora paulo va a seguir con todo esto. asegurate de que este todo en el repo como para que pueda seguir desarrollando la clase" → todo pusheado, incluido research/web/; idea del TP en missions/sistemas-multiagente/idea.md.
  - 2026-10-04 — "Revisión del borrador (5 preguntas)" → (1) "un solo agente con todas las tools de base y al menos 3 arquitecturas mas"; (2) agente sin LLM: "adicional no obligatorio, suma puntos"; (3) demo nueva: repo con tres repositorios design/code/outreach; subagentes inspeccionan cada uno, CLAUDE.md por repo, tres chats renombrados DESIGN-AGENT, CODE-AGENT, OUTREACH-AGENT, uno se comunica con los otros dos para sincronizarse; (4) títulos largos: "dejalos por ahora como estan"; (5) README: "si" → clase 10 (7/10) = Agentes, Visión CNN pasa a la 11 y SD/GANs a la 12.
  - 2026-10-04 — feedback ronda 2 (verbatim): "estas definiendo que es un agente suponiendo que los alumnos saben que es performance, ambiente, actuadores, sensores, etc. no das definiciones de los terminos elementales de los agentes. das solo el ejemplo de la grilla como instancia de todo eso sin variantes, agrega todo esto que falta al principio a pesar de que implique agregar diapositivas" → en curso (sección 1 ampliada)
- What was decided: 
- Key inputs: 
- Files created/modified: draft.md (ronda 1, 2026-10-04: requisitos del TP fijados en tesis, 3.1, sección 6, 6.2 y conclusions.2: agente único con todas las herramientas + al menos tres arquitecturas más, agente sin LLM optativo con puntos extra; demo 5.7 rehecha con tres repositorios design/code/outreach, subagentes Explore nuevos, un CLAUDE.md por repositorio, /rename a DESIGN-AGENT, CODE-AGENT y OUTREACH-AGENT, coordinación por mensajes entre sesiones; hints de plantilla corregidos: 3.9 table → value-columns, 5.7 statement → process; Open questions y Cut material actualizados; 3 bullets del presentador estampados, cerrados y espejados); config/feedback-backlog.md (3 filas nuevas); draft.md (ronda 2, 2026-10-04: sección 1 rehecha de 7 a 13 láminas para definir los términos elementales uno por uno, con varios agentes de ejemplo. Nuevas: 1.2 Ambiente, sensores y percepciones; 1.3 Actuadores y acciones (lazo agente-ambiente en ASCII); 1.4 Función de agente y programa de agente (termostato); 1.6 Omnisciencia y autonomía (imagen del agente que aprende, AlphaGo Zero); 1.7 PEAS en cuatro agentes (aspiradora, robot móvil, AlphaGo, taxi); 1.9 Cuatro ambientes clasificados (crucigrama, ajedrez, taxi, asistente con LLM). Reescritas: 1.1 (notas), 1.5 Racionalidad y medida de performance (sin tabla ni PEAS), 1.8 Tipos de ambiente (siete dimensiones con definición y ejemplo, formato editorial), 1.10 y 1.11 (usan los términos ya definidos; ficha PEAS del LLM en orden P-E-A-S); renumeradas 1.12 ReAct y 1.13 Workflow. Objetivo de la sección y arco de la agenda ajustados. Deck: 48 láminas, 89,5 de 90 min. Open questions: 7 entradas nuevas sobre lo que descansa en el capítulo 2 de Russell y Norvig o en clasificación del editor, y propuesta de compresión de 5,5 min sin aplicar; Cut material: notas viejas de 1.3; 1 bullet del presentador estampado, cerrado y espejado); config/feedback-backlog.md (1 fila nueva, ronda 2); draft.md (ronda 3, 2026-10-04: compresión de 5,5 min aprobada por la cátedra, sin tocar títulos ni orden: demo 5.7 de 6 a 4,5 min con el paso 4 reducido a un solo mensaje de CODE-AGENT a DESIGN-AGENT y OUTREACH-AGENT con nombre, texto y link fijados (cuerpo de la lámina ajustado en el paso 4); 4.6 de 2 a 1 min con notas recortadas; 3.9 y 5.2 de 2,5 a 2; Conclusiones 2 de 3 a 2 con notas recortadas; 2.1 y 2.2 de 2 a 1,5. Total: 84 de 90 min (79,5 en notas más 4,5 de la demo). Los objetivos de sección no llevan tiempos, no hubo nada que cambiar ahí. Salió la pregunta abierta de tiempos; 1 bullet del presentador en Agenda estampado, cerrado y espejado); config/feedback-backlog.md (1 fila nueva, ronda 3); draft.md (ronda 4, 2026-10-04: lámina 1.8 partida en dos por desborde del render: 1.8 Tipos de ambiente con observable, agentes y determinismo, y 1.9 Más dimensiones del ambiente con episódico, dinámico, discreto y conocido; cuerpos cortos, definiciones y ejemplos largos a las notas; 2 min repartidos 1 + 1, total sin cambios; renumeradas 1.10 a 1.14 con referencias cruzadas y Open questions; 1 bullet del presentador estampado, cerrado y espejado); config/feedback-backlog.md (1 fila nueva, ronda 4)
- Pending open questions: 
