"""API del Hospital Provincial Arroyo Claro: estado del dia (camas, guardias, turnos, farmacia, espera).

Uso:  python3 servidor.py            (escucha en http://localhost:8765)
      python3 servidor.py --puerto 9000

Solo biblioteca estandar. Los datos salen de datos_api.json y son una foto fija del dia de la mision.
"""
import argparse, json, unicodedata
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

DATOS = json.loads((Path(__file__).parent / "datos_api.json").read_text(encoding="utf-8"))


def clave(texto):
    t = unicodedata.normalize("NFKD", texto.strip().lower())
    return "".join(c for c in t if not unicodedata.combining(c)).replace(" ", "_")


def buscar(tabla, nombre, param):
    if not nombre:
        return 400, {"error": f"falta el parametro '{param}'", "opciones": sorted(tabla)}
    k = clave(nombre)
    for nombre_tabla, valor in tabla.items():
        if clave(nombre_tabla) == k:
            return 200, {param: nombre_tabla, "fecha": DATOS["fecha"], "datos": valor}
    return 404, {"error": f"'{nombre}' no existe", "opciones": sorted(tabla)}


def camas(q):
    code, cuerpo = buscar(DATOS["camas"], q.get("sector"), "sector")
    if code == 200:
        d = cuerpo["datos"]
        cuerpo["datos"] = {**d, "libres": d["total"] - d["ocupadas"]}
    return code, cuerpo


RUTAS = {
    "/camas": camas,
    "/guardia": lambda q: buscar(DATOS["guardia_hoy"], q.get("especialidad"), "especialidad"),
    "/turnos": lambda q: buscar(DATOS["turnos"], q.get("especialidad"), "especialidad"),
    "/farmacia": lambda q: buscar(DATOS["farmacia"], q.get("medicamento"), "medicamento"),
    "/espera": lambda q: (200, {"fecha": DATOS["fecha"], "minutos_por_nivel": DATOS["espera_guardia_minutos"]}),
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(url.query).items()}
        ruta = RUTAS.get(url.path)
        code, cuerpo = ruta(q) if ruta else (404, {"error": "ruta inexistente", "rutas": sorted(RUTAS)})
        data = json.dumps(cuerpo, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--puerto", type=int, default=8765)
    a = ap.parse_args()
    print(f"API del hospital en http://localhost:{a.puerto}  (rutas: {', '.join(sorted(RUTAS))})")
    ThreadingHTTPServer(("localhost", a.puerto), Handler).serve_forever()
