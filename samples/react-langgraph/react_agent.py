"""Agente ReAct con LangGraph: pensar → actuar → observar, un paso a la vez.

El grafo tiene dos nodos y un ciclo:

    START → agente ──(¿pidió una tool?)──sí──→ tools ──┐
              ↑                                         │
              └─────────────────────────────────────────┘
            agente ──no──→ END

- `agente`: el LLM lee todo el historial (el contexto c_t) y decide la próxima
  acción: llamar a una tool o responder.
- `tools`: ejecuta la tool pedida y agrega el resultado al historial como una
  observación. Después vuelve al agente.

La pregunta por defecto es la del paper de ReAct (Yao et al., 2022), que
necesita dos búsquedas encadenadas en Wikipedia.

Uso:
    python react_agent.py
    python react_agent.py "¿En qué año nació el director de Parasite?"
    python react_agent.py --grafo     # imprime el grafo en Mermaid y sale
"""

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

PREGUNTA_DEFAULT = (
    "Además del Apple Remote, ¿qué otro dispositivo puede controlar el programa "
    "con el que el Apple Remote fue diseñado originalmente para interactuar?"
)

PROMPT_SISTEMA = """Sos un agente que responde preguntas usando Wikipedia.

Trabajás en un loop: antes de cada acción escribí una línea que empiece con
"Pensamiento:" explicando qué sabés hasta ahora y qué te falta. Después llamá
a UNA tool. Cuando tengas la respuesta, escribí "Respuesta final:" seguida de
la respuesta en español, sin llamar a ninguna tool.

No inventes datos: si la observación no alcanza, buscá de nuevo."""

WIKIPEDIA_API = "https://en.wikipedia.org/w/api.php"
USER_AGENT = "austral-ai-gen-react-sample/1.0 (clase de agentes)"


# --- Tools ------------------------------------------------------------------
# Son las mismas dos acciones del paper: search[entidad] y lookup[texto].


def _wikipedia(params: dict) -> dict:
    url = WIKIPEDIA_API + "?" + urllib.parse.urlencode({**params, "format": "json"})
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp)


def _texto_de_pagina(titulo: str, solo_intro: bool) -> tuple[str, str]:
    params = {
        "action": "query",
        "prop": "extracts",
        "explaintext": 1,
        "redirects": 1,
        "titles": titulo,
    }
    if solo_intro:
        params["exintro"] = 1
    paginas = _wikipedia(params)["query"]["pages"]
    pagina = next(iter(paginas.values()))
    return pagina.get("title", titulo), pagina.get("extract", "")


@tool
def buscar_wikipedia(entidad: str) -> str:
    """Busca una entidad en Wikipedia (en inglés) y devuelve el primer párrafo de
    la página más relevante. Si no hay una página exacta, lista títulos parecidos."""
    resultados = _wikipedia(
        {"action": "query", "list": "search", "srsearch": entidad, "srlimit": 5}
    )["query"]["search"]
    if not resultados:
        return f"No encontré nada para '{entidad}'."
    titulo, intro = _texto_de_pagina(resultados[0]["title"], solo_intro=True)
    parecidos = ", ".join(r["title"] for r in resultados[1:])
    return f"[{titulo}] {intro[:1200]}\n(Otras páginas: {parecidos})"


@tool
def buscar_en_pagina(pagina: str, texto: str) -> str:
    """Busca un texto dentro de una página de Wikipedia y devuelve las oraciones
    que lo contienen. Sirve para encontrar un dato puntual en una página larga."""
    titulo, contenido = _texto_de_pagina(pagina, solo_intro=False)
    if not contenido:
        return f"No existe la página '{pagina}'."
    contenido = re.sub(r"^=+ .* =+$", "", contenido, flags=re.MULTILINE)  # títulos de sección
    oraciones = re.split(r"(?<=[.!?])\s+", contenido)
    hallazgos = [o for o in oraciones if texto.lower() in o.lower()]
    if not hallazgos:
        return f"'{texto}' no aparece en [{titulo}]."
    return f"[{titulo}] " + " … ".join(hallazgos[:4])


TOOLS = [buscar_wikipedia, buscar_en_pagina]


# --- Grafo ------------------------------------------------------------------


def construir_modelo():
    """LLM vía OpenRouter, como en las misiones de la materia."""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        sys.exit("Falta la variable de entorno OPENROUTER_API_KEY.")
    return ChatOpenAI(
        model=os.environ.get("MODEL", "anthropic/claude-haiku-4.5"),
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        temperature=0,
    )


def construir_grafo(modelo):
    modelo_con_tools = modelo.bind_tools(TOOLS)

    def agente(estado: MessagesState):
        mensajes = [SystemMessage(PROMPT_SISTEMA)] + estado["messages"]
        return {"messages": [modelo_con_tools.invoke(mensajes)]}

    grafo = StateGraph(MessagesState)
    grafo.add_node("agente", agente)
    grafo.add_node("tools", ToolNode(TOOLS))
    grafo.add_edge(START, "agente")
    # Si el último mensaje del agente pide una tool, va a "tools"; si no, termina.
    grafo.add_conditional_edges("agente", tools_condition, {"tools": "tools", END: END})
    grafo.add_edge("tools", "agente")  # el ciclo: la observación vuelve al agente
    return grafo.compile()


# --- Salida -----------------------------------------------------------------


def _texto(mensaje: AIMessage) -> str:
    if isinstance(mensaje.content, str):
        return mensaje.content.strip()
    partes = [p.get("text", "") for p in mensaje.content if isinstance(p, dict)]
    return "\n".join(partes).strip()


def correr(pregunta: str, max_pasos: int) -> None:
    app = construir_grafo(construir_modelo())
    print(f"\nPregunta: {pregunta}\n")

    vuelta = 0
    for actualizacion in app.stream(
        {"messages": [HumanMessage(pregunta)]},
        config={"recursion_limit": max_pasos},
        stream_mode="updates",
    ):
        for nodo, salida in actualizacion.items():
            for mensaje in salida["messages"]:
                if isinstance(mensaje, AIMessage):
                    vuelta += 1
                    print(f"── vuelta {vuelta} · nodo agente " + "─" * 30)
                    if texto := _texto(mensaje):
                        print(texto)
                    for llamada in mensaje.tool_calls:
                        args = ", ".join(f"{k}={v!r}" for k, v in llamada["args"].items())
                        print(f"Acción: {llamada['name']}({args})")
                elif isinstance(mensaje, ToolMessage):
                    print(f"── nodo {nodo} " + "─" * 41)
                    print(f"Observación: {mensaje.content}\n")

    print(f"\n{vuelta} llamadas al LLM.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("pregunta", nargs="?", default=PREGUNTA_DEFAULT)
    parser.add_argument("--max-pasos", type=int, default=20,
                        help="límite de nodos visitados (recursion_limit de LangGraph)")
    parser.add_argument("--grafo", action="store_true",
                        help="imprime el grafo en Mermaid y sale, sin llamar al LLM")
    args = parser.parse_args()

    if args.grafo:
        modelo_falso = type("SinLLM", (), {"bind_tools": lambda self, tools: self})()
        print(construir_grafo(modelo_falso).get_graph().draw_mermaid())
    else:
        correr(args.pregunta, args.max_pasos)
