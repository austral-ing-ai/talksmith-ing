"""Compara la ficha que registró el agente con la esperada. No sabe calcular fichas: las esperadas vienen como datos
(`esperadas-<variante>.jsonl`). Un caso está resuelto si pasan los 9 controles: los 8 campos y la verificación de la
afiliación (consultó a la entidad correcta con el número correcto y a ninguna de las prohibidas)."""

from .entorno import CAMPOS, _norm

CONTROLES = CAMPOS + ["verificacion"]


def _doc(x) -> str | None:
    return None if x is None else "".join(ch for ch in str(x).upper() if ch.isalnum())


def _igual(campo: str, esperado, obtenido) -> bool:
    if campo == "numero_documento":
        return _doc(esperado) == _doc(obtenido)
    if campo == "entidad_a_notificar":
        return (esperado is None and obtenido is None) or (
            esperado is not None and obtenido is not None and _norm(esperado) == _norm(obtenido))
    return esperado == obtenido


def _verifico(verificacion: dict, log: list[dict]) -> bool:
    hechas = [(_norm(e["argumentos"].get("entidad", "")), _norm(e["argumentos"].get("numero_afiliado", "")))
              for e in log if e["herramienta"] == "verificar_afiliacion" and isinstance(e["argumentos"], dict)]
    if any(e in {_norm(x) for x in verificacion["prohibidas"]} for e, _ in hechas):
        return False
    requerida = verificacion["requerida"]
    return requerida is None or (_norm(requerida[0]), _norm(requerida[1])) in hechas


def comparar(esperada: dict, decision: dict | None, log: list[dict]) -> dict:
    ficha = esperada["ficha"]
    if decision is None:
        controles = {k: False for k in CONTROLES}
    else:
        controles = {k: _igual(k, ficha[k], decision.get(k)) for k in CAMPOS}
        controles["verificacion"] = _verifico(esperada["verificacion"], log)
    return {
        "caso": esperada["caso"],
        "resuelto": all(controles.values()),
        "parcial": round(sum(controles.values()) / len(controles), 3),
        "controles": controles,
        "esperada": ficha,
        "obtenida": decision,
        "llamadas": len(log),
        "invalidas": sum(not e["valida"] for e in log),
    }


def resumir(resultados: list[dict]) -> dict:
    n = len(resultados)
    if not n:
        return {"casos": 0}
    return {
        "casos": n,
        "resueltos": sum(r["resuelto"] for r in resultados),
        "parcial_medio": round(sum(r["parcial"] for r in resultados) / n, 3),
        "por_control": {k: round(sum(r["controles"][k] for r in resultados) / n, 3) for k in CONTROLES},
        "sin_decision": sum(r["obtenida"] is None for r in resultados),
        "llamadas_medio": round(sum(r["llamadas"] for r in resultados) / n, 1),
    }
