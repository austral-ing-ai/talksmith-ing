"""Evaluación aparte del buscador. Es obligatoria antes de empezar el agente y se documenta, pero no es la nota: el
buscador cuenta por lo que rinde el agente con él.

El dataset tiene pares consulta → evidencia, y la evidencia son fragmentos textuales de las normas, no chunks: cada
grupo parte el corpus como quiere. Un chunk es relevante si contiene completo algún fragmento de evidencia. Tres
números, sin combinar:
- recall de evidencia: fracción de los fragmentos de evidencia que quedan completos dentro de lo que trae;
- precisión: fracción de los chunks traídos que son relevantes;
- tokens por consulta: cuánto contexto ocupa lo que trae (4 caracteres por token).

Dos modos:
- con lo que el buscador devuelve en el entorno (`k_entorno`, o 2), que es lo que va a ver el agente;
- con presupuestos fijos de tokens, para comparar buscadores con distinto tamaño de chunk.

    python -m admision.evaluar_rag --entrega entrega.py --normas normas/original --consultas rag/consultas_dev.jsonl
"""

import argparse
import json
import re
from pathlib import Path

CARACTERES_POR_TOKEN = 4


def _normalizar(texto: str) -> str:
    return re.sub(r"\s+", " ", texto).strip()


def _texto(x) -> str:
    return x if isinstance(x, str) else x.texto


def cargar_dataset(ruta: Path) -> list[dict]:
    return [json.loads(x) for x in Path(ruta).read_text(encoding="utf-8").splitlines() if x.strip()]


def recortar_al_presupuesto(textos: list[str], presupuesto_tokens: int) -> list[str]:
    restante = presupuesto_tokens * CARACTERES_POR_TOKEN
    tomados = []
    for texto in textos:
        if restante <= 0:
            break
        tomados.append(texto[:restante])
        restante -= len(texto)
    return tomados


def _medir(dataset: list[dict], traidos) -> dict:
    """traidos(item) -> lista de textos ya recortados."""
    recalls, precisiones, cantidades, caracteres, por_tipo = [], [], [], [], {}
    for item in dataset:
        tomados = [_normalizar(t) for t in traidos(item)]
        evidencia = [_normalizar(e["texto"]) for e in item["evidencia"]]
        recall = sum(any(e in t for t in tomados) for e in evidencia) / len(evidencia)
        recalls.append(recall)
        relevantes = sum(any(e in t for e in evidencia) for t in tomados)
        precisiones.append(relevantes / len(tomados) if tomados else 0.0)
        cantidades.append(len(tomados))
        caracteres.append(sum(len(t) for t in tomados))
        if "tipo" in item:
            por_tipo.setdefault(item["tipo"], []).append(recall)
    n = len(dataset)
    resultado = {
        "consultas": n,
        "recall_evidencia": round(sum(recalls) / n, 3),
        "precision": round(sum(precisiones) / n, 3),
        "chunks_por_consulta": round(sum(cantidades) / n, 2),
        "tokens_por_consulta": round(sum(caracteres) / n / CARACTERES_POR_TOKEN),
        "consultas_con_toda_la_evidencia": sum(r == 1.0 for r in recalls),
    }
    if por_tipo:
        resultado["recall_por_tipo"] = {t: round(sum(v) / len(v), 3) for t, v in sorted(por_tipo.items())}
    return resultado


def evaluar_recuperador(recuperar, dataset: list[dict], presupuesto_tokens: int = 512, k: int = 20) -> dict:
    r = _medir(dataset, lambda item: recortar_al_presupuesto([_texto(f) for f in recuperar(item["consulta"], k)],
                                                             presupuesto_tokens))
    return {"presupuesto_tokens": presupuesto_tokens, **r}


def evaluar_buscador(buscador, dataset: list[dict]) -> dict:
    k = getattr(buscador, "k_entorno", 2)
    return {"k_entorno": k, **_medir(dataset, lambda item: [_texto(f) for f in buscador.recuperar(item["consulta"], k)])}


def main():
    from .contrato import cargar_entrega

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--entrega", type=Path, required=True)
    ap.add_argument("--normas", type=Path, required=True)
    ap.add_argument("--consultas", type=Path, required=True)
    a = ap.parse_args()
    buscador = cargar_entrega(a.entrega).construir_buscador(a.normas)
    dataset = cargar_dataset(a.consultas)
    informe = {"entorno": evaluar_buscador(buscador, dataset),
               "presupuesto": [evaluar_recuperador(buscador.recuperar, dataset, b) for b in (256, 512, 1024)]}
    print(json.dumps(informe, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
