"""Multiagente en estrella con LangGraph: un orquestador que delega en subagentes.

    Usuario → orquestador ──(delegar_investigacion)──→ subagente 1 ┐
                  ↑        ──(delegar_investigacion)──→ subagente 2 ┤  (en paralelo)
                  └──────────── solo vuelven las respuestas ────────┘

- El **orquestador** es un agente con una sola tool: `delegar_investigacion`.
  Decide en qué subpreguntas partir el pedido y después sintetiza.
- Cada **subagente** es el agente ReAct de `samples/react-langgraph`, con sus
  tools de Wikipedia. Arranca con el contexto vacío: solo ve la subpregunta
  que le pasan, no la conversación del orquestador ni la de su hermano.
- Al orquestador vuelve solo la respuesta final de cada subagente, no su
  trayectoria. Eso es el aislamiento de contexto.

Uso:
    python orquestador.py
    python orquestador.py "¿Quién nació primero, el director de Parasite o el de Roma (2018)?"
    python orquestador.py --grafo
"""

import argparse
import sys
from pathlib import Path

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

# El subagente es el agente ReAct del otro ejemplo.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "react-langgraph"))
import react_agent  # noqa: E402

PREGUNTA_DEFAULT = (
    "¿Quién nació primero: el director de la película Parasite (2019) "
    "o el director de Roma (2018)?"
)

PROMPT_ORQUESTADOR = """Sos un orquestador. No buscás información vos mismo.

Partí el pedido en subpreguntas independientes y delegá cada una con la tool
delegar_investigacion; si no dependen entre sí, delegalas todas en el mismo
turno para que corran en paralelo. Cuando tengas las respuestas, escribí
"Respuesta final:" y la respuesta en español."""

contador_subagentes = 0


@tool
def delegar_investigacion(subpregunta: str) -> str:
    """Delega una subpregunta a un subagente investigador con acceso a Wikipedia.
    El subagente arranca sin contexto: la subpregunta tiene que ser autocontenida."""
    global contador_subagentes
    contador_subagentes += 1
    n = contador_subagentes
    subagente = react_agent.construir_grafo(react_agent.construir_modelo())

    print(f"    ┌─ subagente {n} · recibe 1 mensaje: {subpregunta!r}")
    final = ""
    for actualizacion in subagente.stream(
        {"messages": [HumanMessage(subpregunta)]},
        config={"recursion_limit": 20},
        stream_mode="updates",
    ):
        for salida in actualizacion.values():
            for mensaje in salida["messages"]:
                if isinstance(mensaje, AIMessage):
                    for llamada in mensaje.tool_calls:
                        args = ", ".join(f"{k}={v!r}" for k, v in llamada["args"].items())
                        print(f"    │  acción: {llamada['name']}({args})")
                    if not mensaje.tool_calls:
                        final = react_agent._texto(mensaje)
                elif isinstance(mensaje, ToolMessage):
                    print(f"    │  observación: {mensaje.content[:90]}…")
    print(f"    └─ subagente {n} devuelve: {final!r}\n")
    return final


def construir_orquestador(modelo):
    modelo_con_tools = modelo.bind_tools([delegar_investigacion])

    def orquestador(estado: MessagesState):
        mensajes = [SystemMessage(PROMPT_ORQUESTADOR)] + estado["messages"]
        return {"messages": [modelo_con_tools.invoke(mensajes)]}

    grafo = StateGraph(MessagesState)
    grafo.add_node("orquestador", orquestador)
    grafo.add_node("subagentes", ToolNode([delegar_investigacion]))
    grafo.add_edge(START, "orquestador")
    grafo.add_conditional_edges(
        "orquestador", tools_condition, {"tools": "subagentes", END: END}
    )
    grafo.add_edge("subagentes", "orquestador")
    return grafo.compile()


def correr(pregunta: str) -> None:
    app = construir_orquestador(react_agent.construir_modelo())
    print(f"\nPedido: {pregunta}\n")
    for actualizacion in app.stream(
        {"messages": [HumanMessage(pregunta)]},
        config={"recursion_limit": 12},
        stream_mode="updates",
    ):
        for nodo, salida in actualizacion.items():
            for mensaje in salida["messages"]:
                if isinstance(mensaje, AIMessage):
                    print("── orquestador " + "─" * 40)
                    if texto := react_agent._texto(mensaje):
                        print(texto)
                    for llamada in mensaje.tool_calls:
                        print(f"Delega: {llamada['args']['subpregunta']!r}")
                    print()
    print(f"{contador_subagentes} subagentes, cada uno con su propio contexto.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("pregunta", nargs="?", default=PREGUNTA_DEFAULT)
    parser.add_argument("--grafo", action="store_true",
                        help="imprime el grafo del orquestador en Mermaid y sale")
    args = parser.parse_args()

    if args.grafo:
        modelo_falso = type("SinLLM", (), {"bind_tools": lambda self, tools: self})()
        print(construir_orquestador(modelo_falso).get_graph().draw_mermaid())
    else:
        correr(args.pregunta)
