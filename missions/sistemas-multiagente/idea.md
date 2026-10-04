# TP «Sistemas multiagente»: idea y decisiones abiertas

Documento de diseño, no es el enunciado. Lo escribió Marco el 2026-10-04 para que la cátedra termine de definir la misión. El enunciado final va en `mission.md`, en esta misma carpeta.

La clase que lo presenta es `talks/sistemas-multiagente/`, del miércoles 7 de octubre. Su última lámina, «El trabajo práctico», anuncia lo que está decidido.

## Lo que pidió Marco (textual)

> el trabajo práctico va a implicar reutilizar estas tecnologías creando un sistema multiagente (quizas varias arquitecturas para resolver un benchmark usando un "LLM malo" en donde la especializacion y aislamiento de contexto se use para poder resolver los problemas del benchmark bajo restricciones)

> en la parte practica si bien el enfoque va a ser en agentes basados en LLM tambien quizas agreguemos agentes no basados en LLMs como parte requerida del sistema

> vamos a pedirles reportar con logs también auditabilidad, rendimiento, uso de tokens, colaboración distribuida entre miembros del grupo en github (medimos esto para notas conceptuales de cada alumno), y demas conceptos de desarrollo, arquitectura y eficiencia importante

## Decidido

- **Arquitecturas.** La línea de base es un solo agente con todas las herramientas. Sobre ella, al menos tres arquitecturas multiagente.
- **Agente sin LLM.** Es un adicional optativo y suma puntos. Puede ser un solver, un planificador o un validador con reglas.
- **Modelo.** Un LLM débil y barato. La especialización y el aislamiento de contexto son lo que tiene que hacer alcanzable el benchmark.
- **Tecnologías.** Se reutilizan el RAG y el MCP del TP 3: FastMCP con `mcp<2`, y OpenAI Agents SDK o LangChain, en Python.
- **Reporte.** Los grupos entregan:
  - logs auditables de cada corrida;
  - rendimiento de cada arquitectura en el benchmark;
  - uso de tokens y costo;
  - la colaboración del grupo en GitHub, que se mide por alumno para la nota conceptual individual;
  - decisiones de desarrollo, arquitectura y eficiencia.

## Abierto

1. **Benchmark.** Hay tres opciones, sin elegir:
   - **Extender el hospital Arroyo Claro del TP 3.** Preguntas de varios saltos que cruzan los documentos con la API. Reutiliza todo lo hecho y la cátedra ya tiene el generador del caso.
   - **Pampa Viajes, el ejemplo del deck.** Pedidos de viaje con restricciones de presupuesto, fechas y cupos, verificables por código. Un agente sin LLM entra solo, porque el presupuesto se valida con reglas. Hay que generar el caso.
   - **Un subconjunto de un benchmark público de agentes con herramientas.** Sirve uno del estilo de tau-bench o un multi-hop QA. Es más creíble afuera, pero obliga a adaptar el entorno.
2. **Qué LLM débil.** Hay que fijarlo por OpenRouter, igual que en los TP anteriores.
3. **Qué restricciones fuerzan el multiagente.** Hay tres candidatas, combinables:
   - un tope de tokens por llamada o una ventana de contexto chica;
   - un máximo de herramientas por agente;
   - un presupuesto de costo por corrida.

   Sin alguna restricción, un agente único puede resolverlo todo y la comparación pierde sentido.
4. **Cómo se mide la colaboración en GitHub.** Commits por autor, PR revisados, issues o ramas. Hay que definirlo en la rúbrica.
5. **Fecha de entrega y rúbrica de 100 puntos.** La rúbrica queda fuera del repo público: la de prompting estaba publicada y un grupo la usó.

## Contexto útil

- **El deck ya trae todo el contenido que el TP necesita:**
  - las arquitecturas base, con el ejemplo Pampa Viajes;
  - los casos reales;
  - el agente principal que delega bajo demanda;
  - los agentes sin LLM;
  - las fallas del MAST;
  - que los frameworks de handoff comparten todo el historial por defecto, así que el aislamiento hay que configurarlo.
- **El corpus de la clase** está en `talks/sistemas-multiagente/research/corpus/`. Las cifras citables vienen de ahí: Anthropic, MAST y la tabla de LangGraph con llamadas y tokens por patrón.
