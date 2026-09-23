"""Arma el modelo de laminas html-strict.
  sin argumentos: draft.md -> output/slide-model.draft.json (vista en vivo --draft)
  --final:        final.md -> output/slide-model.json (render final, con los diagramas ya en PNG)
Uso, desde la raiz del repo: python3 talks/transformers-a-fondo/research/build_model_draft.py [--final]"""
import json, re, sys
from pathlib import Path
T = Path("talks/transformers-a-fondo")
FINAL = "--final" in sys.argv
src = (T / ("final.md" if FINAL else "draft.md")).read_text(encoding="utf-8")
fm = dict(re.findall(r'^(\w+): "?(.*?)"?$', src.split("---")[1], flags=re.M))
body = src.split("# Open questions")[0]

def clean(t): return re.sub(r"\*\*(.+?)\*\*", r"\1", t).strip()

def parse(chunk):
    content = chunk.split("### Sources")[0]
    content_noascii = re.sub(r"```.*?```", "", content, flags=re.S)
    lead = re.search(r"^\*\*(.+?)\*\*\s*$", content, flags=re.M)
    bullets = []
    for b in re.findall(r"^- \*\*(.+?)\*\*[:]?\s*(.*)$", content, flags=re.M):
        label, rest = b[0].strip(), b[1].strip()
        bullets.append({"label": label, "body": rest})
    asc = re.findall(r"```ascii\n(.*?)```", content, flags=re.S)
    tables = re.findall(r"((?:^\|.*\|\s*\n)+)", content_noascii, flags=re.M)
    img = re.search(r"!\[(.*?)\]\((.*?)\)", content)
    notes = re.search(r"### Speaker notes\n\n(.*?)(?=\n\*\*Presenter feedback|\n### |\Z)", chunk, flags=re.S)
    return dict(lead=clean(lead.group(1)) if lead else "", bullets=bullets, ascii=[a.rstrip("\n") for a in asc],
                tables=tables, img=img, notes=notes.group(1).strip() if notes else "")

def mono(table):
    rows = [[clean(c) for c in r.strip().strip("|").split("|")] for r in table.strip().splitlines() if not re.match(r"^\|[-| ]+\|$", r.strip())]
    n = max(len(r) for r in rows); rows = [r + [""] * (n - len(r)) for r in rows]
    w = [max(len(r[i]) for r in rows) for i in range(n)]
    return "\n".join("  ".join(c.rjust(w[i]) if i else c.ljust(w[i]) for i, c in enumerate(r)).rstrip() for r in rows)

def squeeze(a, n=18):
    lines = [l for l in a.split("\n")]
    if len(lines) > n: lines = [l for l in lines if l.strip()]
    return "\n".join(lines[:n])

def btxt(b):
    l = b["label"]
    if not b["body"]: return l
    return f"{l} {b['body']}" if l.endswith((".", ":")) else f"{l}: {b['body']}"

def code_slide(base, p, code):
    exp = ([p["lead"]] if p["lead"] else []) + [btxt(b) for b in p["bullets"]]
    code = code.replace(" ", "\u00a0")  # el codebox del renderer colapsa espacios (ver talksmith_bugs.md)
    return {**base, "template": "code-example", "language": "text", "code": code,
            "explanation": exp[:3], **({"highlights": [{"body": x, "kind": "note"} for x in exp[3:]]} if exp[3:] else {})}


# Versiones angostas de los diagramas que no entran en el recuadro de codigo (solo para la vista en vivo;
# en Polish se renderizan como SVG desde draft.md).
ANGOSTOS = {
"La posición entra con el embedding": """token:        the     cat     sat
               |       |       |
embedding    e_the   e_cat   e_sat
               +       +       +
posicion      p_0     p_1     p_2
               |       |       |
               v       v       v
fila de X    x_the   x_cat   x_sat   (n x d)

sin p: "the cat sat" y "sat cat the"
dan las mismas filas en otro orden""",
"El problema de apilar: el gradiente se pierde": """salida <- bloque N <- ... <- bloque 1 <- embedding

grad. en capa 1 = dL/dx_N . J_N . ... . J_1

norma de J < 1:  0,9^12 = 0,28
                 0,9^48 = 0,006
norma de J > 1:  1,1^48 = 97""",
"Del encoder al embedding de oración": """frag. A -> [BERT] -> tokens (n x d)
                   -> MEDIA -> u (d)
                                    \\
                                     coseno(u, v)
                                    /
frag. B -> [BERT] -> tokens (n x d)
                   -> MEDIA -> v (d)
          (mismos pesos)

entrenamiento: pares de frases (NLI, STS)
para que coseno alto = significado parecido""",
}

slides, sections = [], []
for sec in re.finditer(r"^# (?:\d+\. )?(.+?)\n(.*?)(?=^# |\Z)", body, flags=re.M | re.S):
    name, stext = sec.group(1).strip(), sec.group(2)
    if name in ("Thesis", "Agenda"): continue
    sections.append(name)
    slides.append({"template": "section-agenda", "title": name, "notes": ""})
    for m in re.finditer(r"^## (\d+)\. (.+?)\n(.*?)(?=^## |\Z)", stext, flags=re.M | re.S):
        title, p = m.group(2).strip(), parse(m.group(3))
        base = {"section": name, "title": title, "notes": p["notes"]}
        if "<!-- template: quiz -->" in m.group(3):
            c = m.group(3)
            opts = re.findall(r"^- [A-D]\. (.+)$", c, flags=re.M)
            ans = re.search(r"^\*\*Respuesta: ([A-D])\.\*\* (.+)$", c, flags=re.M)
            s = {**base, "template": "quiz", "title": title.replace("Quiz: ", ""), "question": p["lead"], "options": opts,
                 "correct": ans.group(1), "answer": ans.group(2)}
        elif title.startswith("Encoder y decoder en el paper"):
            s = {**base, "template": "content-image", "lead": p["lead"], "image": {"src": p["img"].group(2), "alt": p["img"].group(1)},
                 "facts": [{"label": b["label"].rstrip(".:"), "body": b["body"]} for b in p["bullets"]]}
        elif title == "El mapa de la familia":
            rows = [[clean(c) for c in r.strip().strip("|").split("|")] for r in p["tables"][0].strip().splitlines() if not re.match(r"^\|[-| ]+\|$", r.strip())]
            s = {**base, "template": "comparison", "columns": [{"header": rows[0][j], "cells": [f"{r[0]}: {r[j]}" for r in rows[1:]]} for j in (1, 2, 3)],
                 "highlights": [{"body": btxt(b), "kind": "takeaway"} for b in p["bullets"]]}
        elif title == "Qué cambió desde 2017":
            rows = [[clean(c) for c in r.strip().strip("|").split("|")] for r in p["tables"][0].strip().splitlines()[2:]]
            s = {**base, "template": "concept-breakdown", "cards": [{"label": r[0], "body": r[1]} for r in rows],
                 "highlights": [{"body": p["lead"], "kind": "note"}] + [{"body": btxt(b), "kind": "takeaway"} for b in p["bullets"]]}
        elif title == "Cuenta de parámetros de un bloque":
            rows = [[clean(c).replace("\x00", "|") for c in r.replace("\\|", "\x00").strip().strip("|").split("|")] for r in p["tables"][0].strip().splitlines()[2:]]
            s = {**base, "template": "comparison", "columns": [
                    {"header": "Paper 2017 (d = 512, N = 6)", "cells": [f"{r[0]} ({r[1]}): {r[2]}" if r[1] else f"{r[0]}: {r[2]}" for r in rows]},
                    {"header": "GPT-2 chico (d = 768, N = 12)", "cells": [f"{r[0]}: {r[3]}" for r in rows]}],
                 "highlights": [{"body": p["lead"], "kind": "important"}] + [{"body": btxt(b), "kind": "note"} for b in p["bullets"][:2]]}
        elif FINAL and p["img"] and not title.startswith("Encoder y decoder en el paper"):
            img = {"src": p["img"].group(2).replace(".svg", ".png"), "alt": p["img"].group(1)}
            exp = [btxt(b) for b in p["bullets"]]
            s = {**base, "template": "content-image", "lead": p["lead"], "image": img,
                 "facts": [{"label": b["label"].rstrip(".:"), "body": b["body"]} for b in p["bullets"]][:3],
                 **({"highlights": [{"body": x, "kind": "note"} for x in exp[3:]]} if exp[3:] else {})}
            if p["tables"]:
                s["facts"].append({"label": "Salida", "body": " · ".join(" ".join(r) for r in [[clean(c) for c in l.strip().strip("|").split("|")] for l in p["tables"][0].strip().splitlines()[2:]])})
        elif p["ascii"] or p["tables"]:
            parts = ([ANGOSTOS[title]] if title in ANGOSTOS else [squeeze(a) for a in p["ascii"]]) + [mono(t) for t in p["tables"]]
            s = code_slide(base, p, "\n\n".join(parts))
        else:
            s = {**base, "template": "icon-list", "lead": p["lead"], "rows": [{"label": b["label"].rstrip(".:"), "body": b["body"]} for b in p["bullets"][:5]]}
        slides.append(s)

deck = {"title": fm.get("presentation"), "lang": "es", "institution": "Universidad Austral", "class": fm.get("class"),
        "presenter": fm.get("presenter"), "date": fm.get("date"), "logo": None, "sections": sections}
out = T / "output" / ("slide-model.json" if FINAL else "slide-model.draft.json"); out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps({"deck": deck, "slides": slides}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(slides), "slides;", sum(1 for s in slides if s["template"] != "section-agenda"), "de contenido")
for s in slides:
    if s["template"] == "code-example" and s["code"].count("\n") >= 18: print("CODIGO LARGO:", s["title"], s["code"].count("\n") + 1)
