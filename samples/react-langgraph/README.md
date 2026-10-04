# Agente ReAct con LangGraph

Un agente ReAct mínimo: el LLM **piensa**, pide una **acción** (una tool), recibe la **observación** y vuelve a pensar, hasta que puede responder. El ciclo está escrito como grafo, así que se ve en el código y en la salida.

```
START → agente ──(¿pidió una tool?)──sí──→ tools ──┐
          ↑                                         │
          └─────────────────────────────────────────┘
        agente ──no──→ END
```

- **`agente`**: el LLM lee el historial completo y decide si llama a una tool o responde.
- **`tools`**: ejecuta la tool y agrega el resultado al historial. Después vuelve al agente.

Las dos tools son las acciones del paper de ReAct (Yao et al., 2022): `buscar_wikipedia` (su `search[entidad]`) y `buscar_en_pagina` (su `lookup[texto]`). Consultan la Wikipedia en inglés, sin API key.

## Correrlo

```bash
cd samples/react-langgraph
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

export OPENROUTER_API_KEY=sk-or-...
python react_agent.py                       # la pregunta del paper (Apple Remote)
python react_agent.py "¿En qué año nació el director de Parasite?"
python react_agent.py --grafo               # el grafo en Mermaid, sin llamar al LLM
```

El modelo por defecto es `anthropic/claude-haiku-4.5` vía OpenRouter. Se cambia con `MODEL=<proveedor>/<modelo>`; tiene que soportar tool calling.

## Qué se ve al correrlo

La pregunta por defecto necesita dos saltos: primero averiguar para qué programa se diseñó el Apple Remote, después qué otro dispositivo controla ese programa.

La salida de abajo se generó con un **modelo simulado** que devuelve pensamientos y acciones fijos, para mostrar la forma del ciclo. Las **observaciones son reales**: son las respuestas de Wikipedia. Con un LLM real los pensamientos cambian y el número de vueltas puede variar.

```
Pregunta: Además del Apple Remote, ¿qué otro dispositivo puede controlar el programa con el que el Apple Remote fue diseñado originalmente para interactuar?

── vuelta 1 · nodo agente ──────────────────────────────
Pensamiento: tengo que averiguar con qué programa interactuaba el Apple Remote.
Acción: buscar_wikipedia(entidad='Apple Remote')
── nodo tools ─────────────────────────────────────────
Observación: [Apple Remote] The Apple Remote is a remote control introduced in October 2005 by Apple Inc. for use with a number of its products with infrared capability. It was originally designed to control the Front Row media center program on the iMac G5 and is compatible with many subsequent Macintosh computers. […]

── vuelta 2 · nodo agente ──────────────────────────────
Pensamiento: fue diseñado para Front Row. Busco qué otro dispositivo lo controla.
Acción: buscar_en_pagina(pagina='Front Row (software)', texto='keyboard')
── nodo tools ─────────────────────────────────────────
Observación: [Front Row (software)] The software relies on iTunes and iPhoto and is controlled by an Apple Remote or the keyboard function keys. […]

── vuelta 3 · nodo agente ──────────────────────────────
Respuesta final: las teclas de función del teclado.

3 llamadas al LLM.
```

## Para jugar

- **Bajar `--max-pasos`** (por ejemplo a 3) y ver cómo LangGraph corta el loop con `GraphRecursionError`: es el freno que evita que un agente gire para siempre.
- **Sacar `buscar_en_pagina`** de `TOOLS` y ver cómo el agente tiene que arreglarse solo con búsquedas.
- **Cambiar el prompt** para que no escriba "Pensamiento:" y comparar: es la diferencia entre ReAct y un agente que solo actúa (*Act-only* en el paper).
