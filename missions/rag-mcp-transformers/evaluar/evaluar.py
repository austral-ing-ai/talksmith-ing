"""Evaluacion de la catedra. Todos los grupos miden con este script, sin modificarlo.

Parte 1, recuperacion (sin LLM, gratis y reproducible):
  python3 evaluar/evaluar.py recuperacion --preguntas datos/preguntas_recuperacion_dev.jsonl --resultados resultados.jsonl

  resultados.jsonl: una linea por pregunta, {"id": "R01", "fragmentos": ["texto 1", "texto 2", ...]}
  en el orden en que los devolvio el recuperador.

Partes 2 y 3, agente (con un modelo juez via OpenRouter; necesita OPENROUTER_API_KEY):
  python3 evaluar/evaluar.py agente --preguntas datos/preguntas_agente_dev.jsonl --respuestas respuestas.jsonl

  respuestas.jsonl: {"id": "A01", "respuesta": "...", "contextos": ["...", ...], "herramientas": ["buscar_documentos", ...]}
  "contextos" es todo lo que el agente recibio de sus herramientas (fragmentos y JSON de la API), como texto.

Escribe el resumen por pantalla y el detalle por pregunta en <archivo>.eval.json.
"""
import argparse, json, os, re, sys, time, unicodedata, urllib.request
from pathlib import Path

JUEZ = "google/gemini-3.7-flash"
URL = "https://openrouter.ai/api/v1/chat/completions"


def leer(path):
    return [json.loads(l) for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip()]


def norm(t):
    t = unicodedata.normalize("NFKC", t).lower()
    return re.sub(r"\s+", " ", t)


# ---------------- parte 1 ----------------
def recuperacion(args):
    preg = {p["id"]: p for p in leer(args.preguntas)}
    res = {r["id"]: r for r in leer(args.resultados)}
    faltan = sorted(set(preg) - set(res))
    if faltan:
        sys.exit(f"faltan resultados para: {', '.join(faltan)}")
    filas = []
    for pid, p in preg.items():
        frags = [norm(f) for f in res[pid]["fragmentos"]]
        evs = [norm(e) for e in p["evidencia"]]
        encontradas = [e for e in evs if any(e in f for f in frags)]
        recall = len(encontradas) / len(evs)
        utiles = [f for f in frags if any(e in f for e in evs)]
        precision = len(utiles) / len(frags) if frags else 0.0
        cr = 0.0 if recall + precision == 0 else 2 * recall * precision / (recall + precision)
        rank = next((i + 1 for i, f in enumerate(frags) if any(e in f for e in evs)), None)
        filas.append({"id": pid, "k": len(frags), "recall": recall, "precision": precision,
                      "context_relevance": cr, "rr": 1 / rank if rank else 0.0,
                      "caracteres": sum(len(f) for f in res[pid]["fragmentos"])})
    n = len(filas)
    resumen = {k: round(sum(f[k] for f in filas) / n, 4) for k in ["context_relevance", "recall", "precision", "rr", "k", "caracteres"]}
    resumen["mrr"] = resumen.pop("rr")
    Path(args.resultados + ".eval.json").write_text(json.dumps({"resumen": resumen, "detalle": filas}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(resumen, ensure_ascii=False, indent=1))


# ---------------- partes 2 y 3 ----------------
ESQUEMA = {
    "type": "object",
    "properties": {
        "context_relevance": {"type": "integer", "minimum": 1, "maximum": 5},
        "faithfulness": {"type": "integer", "minimum": 1, "maximum": 5},
        "answer_relevance": {"type": "integer", "minimum": 1, "maximum": 5},
        "justificacion": {"type": "string"},
    },
    "required": ["context_relevance", "faithfulness", "answer_relevance", "justificacion"],
    "additionalProperties": False,
}

INSTRUCCIONES = """Sos un evaluador de un sistema de preguntas y respuestas de un hospital. Recibís una pregunta, los contextos que el sistema recuperó con sus herramientas, la respuesta del sistema y una respuesta de referencia escrita por la cátedra.

Puntuá de 1 a 5 cada criterio, con estas anclas:

context_relevance: ¿los contextos contienen la información necesaria para responder, sin ruido de más? 5 = está todo lo necesario y casi nada irrelevante. 3 = está lo necesario pero mezclado con mucho contenido ajeno, o falta una parte. 1 = los contextos no sirven para responder.

faithfulness: ¿cada afirmación de la respuesta está respaldada por los contextos? Juzgá SOLO contra los contextos, no contra la referencia ni contra tu conocimiento. 5 = todo está respaldado. 3 = hay alguna afirmación sin respaldo que no cambia el sentido. 1 = la respuesta inventa datos centrales.

answer_relevance: ¿la respuesta contesta lo que se preguntó, completa y sin desviarse? Usá la referencia para saber qué se esperaba. 5 = contesta todo lo pedido. 3 = contesta una parte. 1 = no contesta la pregunta.

Devolvé solo el JSON pedido. La justificación, en una o dos oraciones."""


def juzgar(key, p, r):
    ctx = "\n\n---\n\n".join(r.get("contextos", [])) or "(sin contextos)"
    usuario = (f"PREGUNTA:\n{p['pregunta']}\n\nCONTEXTOS RECUPERADOS:\n{ctx}\n\n"
               f"RESPUESTA DEL SISTEMA:\n{r.get('respuesta', '')}\n\nRESPUESTA DE REFERENCIA:\n{p['respuesta_referencia']}")
    body = {"model": JUEZ, "temperature": 0,
            "messages": [{"role": "system", "content": INSTRUCCIONES}, {"role": "user", "content": usuario}],
            "response_format": {"type": "json_schema", "json_schema": {"name": "evaluacion", "strict": True, "schema": ESQUEMA}}}
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    for intento in range(3):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                d = json.loads(resp.read())
            return json.loads(d["choices"][0]["message"]["content"]), d.get("usage", {})
        except Exception as e:
            if intento == 2:
                raise
            time.sleep(3 * (intento + 1))


def agente(args):
    key = os.environ.get("OPENROUTER_API_KEY") or sys.exit("falta la variable OPENROUTER_API_KEY")
    preg = {p["id"]: p for p in leer(args.preguntas)}
    res = {r["id"]: r for r in leer(args.respuestas)}
    faltan = sorted(set(preg) - set(res))
    if faltan:
        sys.exit(f"faltan respuestas para: {', '.join(faltan)}")
    filas, costo = [], 0.0
    for pid, p in preg.items():
        r = res[pid]
        esperadas, usadas = set(p["herramientas_esperadas"]), set(r.get("herramientas", []))
        ruteo = len(esperadas & usadas) / len(esperadas)
        notas, usage = juzgar(key, p, r)
        costo += usage.get("cost", 0) or 0
        filas.append({"id": pid, "ruteo": ruteo, "herramientas_usadas": sorted(usadas),
                      **{k: notas[k] for k in ["context_relevance", "faithfulness", "answer_relevance"]},
                      "justificacion": notas["justificacion"]})
        print(f"{pid}  ruteo {ruteo:.2f}  CR {notas['context_relevance']}  F {notas['faithfulness']}  AR {notas['answer_relevance']}")
    n = len(filas)
    resumen = {k: round(sum(f[k] for f in filas) / n, 3) for k in ["context_relevance", "faithfulness", "answer_relevance", "ruteo"]}
    resumen["juez"] = JUEZ
    resumen["costo_juez_usd"] = round(costo, 5)
    Path(args.respuestas + ".eval.json").write_text(json.dumps({"resumen": resumen, "detalle": filas}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(resumen, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="modo", required=True)
    a = sub.add_parser("recuperacion"); a.add_argument("--preguntas", required=True); a.add_argument("--resultados", required=True)
    b = sub.add_parser("agente"); b.add_argument("--preguntas", required=True); b.add_argument("--respuestas", required=True)
    args = ap.parse_args()
    recuperacion(args) if args.modo == "recuperacion" else agente(args)
