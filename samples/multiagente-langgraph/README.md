# Multiagente en estrella con LangGraph

Un **orquestador** que parte el pedido en subpreguntas y las delega en **subagentes**. Es la topología estrella de la lámina 6.5: los subagentes no se hablan entre sí, solo con el orquestador.

```
Usuario → orquestador ──(delegar_investigacion)──→ subagente 1 ┐
              ↑        ──(delegar_investigacion)──→ subagente 2 ┤  en paralelo
              └──────────── solo vuelven las respuestas ────────┘
```

- **El orquestador** es un agente con una sola tool, `delegar_investigacion`. No busca nada: decide en qué subpreguntas partir el pedido y después sintetiza.
- **Cada subagente** es el agente ReAct de [`../react-langgraph`](../react-langgraph/), con sus tools de Wikipedia. Arranca con el contexto vacío y solo ve su subpregunta.
- **Al orquestador vuelve solo la respuesta final** de cada subagente, no su trayectoria. Eso es el aislamiento de contexto.

En LangGraph, los subagentes son tools del orquestador: un subagente es una función que corre otro grafo. Si el modelo pide varias tools en el mismo turno, `ToolNode` las ejecuta en paralelo.

## Correrlo

Usa el mismo entorno que el ejemplo de ReAct:

```bash
cd samples/react-langgraph
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cd ../multiagente-langgraph

export OPENROUTER_API_KEY=sk-or-...
python orquestador.py            # ¿quién nació primero, el director de Parasite o el de Roma?
python orquestador.py --grafo    # el grafo del orquestador en Mermaid
```

## Qué se ve al correrlo

La salida de abajo se generó con **modelos simulados** que devuelven decisiones fijas, para mostrar la forma de la ejecución. Las **observaciones son reales**: son las respuestas de Wikipedia. Como los dos subagentes corren en paralelo, sus líneas se intercalan.

```
── orquestador ────────────────────────────────────────
Son dos subpreguntas independientes; las delego en paralelo.
Delega: '¿En qué año nació Bong Joon-ho?'
Delega: '¿En qué año nació Alfonso Cuarón?'

    ┌─ subagente 1 · recibe 1 mensaje: '¿En qué año nació Bong Joon-ho?'
    │  acción: buscar_wikipedia(entidad='Bong Joon-ho')
    ┌─ subagente 2 · recibe 1 mensaje: '¿En qué año nació Alfonso Cuarón?'
    │  acción: buscar_wikipedia(entidad='Alfonso Cuarón')
    │  observación: [Bong Joon Ho] Bong Joon Ho (Korean: 봉준호; …; born September 14, 19…
    └─ subagente 1 devuelve: 'Respuesta final: 1969.'

    │  observación: [Alfonso Cuarón] Alfonso Cuarón Orozco (…; born …
    └─ subagente 2 devuelve: 'Respuesta final: 1961.'

── orquestador ────────────────────────────────────────
Respuesta final: Alfonso Cuarón (1961) nació antes que Bong Joon-ho (1969).

2 subagentes, cada uno con su propio contexto.
```

## Para jugar

- **Hacer que dependan:** "¿Dónde nació el director de Parasite?" no se puede partir en paralelo. Mirar si el orquestador delega una vez o dos, y en qué orden.
- **Pasarle más contexto al subagente:** cambiar `delegar_investigacion` para que reciba también el pedido original. El subagente sabe más, pero gasta más tokens y pierde el aislamiento.
- **Comparar con un solo agente:** correr la misma pregunta con `../react-langgraph/react_agent.py` y contar las llamadas al LLM.
