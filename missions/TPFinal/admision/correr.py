"""Corre una entrega sobre un conjunto de casos y deja todo lo que hace falta para auditarla sin volver a correrla.
Trabaja en dos fases separadas, para que el agente nunca tenga a mano las fichas esperadas:

1. **jugar**: arma el buscador (con una copia de las normas en una carpeta aparte) y el agente del grupo, y juega los
   casos. No lee las fichas esperadas. Escribe `trazas.jsonl` (por caso: la conversación con el modelo, cada llamada a
   herramienta con su observación, la ficha y los segundos) y `tiempos.json`.
2. **puntuar**: compara las fichas de las trazas con las esperadas. Escribe `resultados.jsonl` (el veredicto por caso,
   con las búsquedas, los caracteres de contexto que se le pasaron al modelo y los segundos) y `resumen.json`.

    python -m admision.correr jugar --entrega entrega.py --casos entradas/casos.jsonl \\
        --normas entradas/normas/original --salida corridas/original
    python -m admision.correr puntuar --trazas corridas/original/trazas.jsonl \\
        --esperadas esperadas/esperadas-original.jsonl --salida corridas/original

Para la práctica, `practica` hace las dos cosas (juega en este proceso y puntúa en otro):

    python -m admision.correr practica --entrega entrega.py --casos practica/casos.jsonl \\
        --esperadas practica/esperadas-original.jsonl --normas normas/original --salida corridas/original

`practica` copia los casos y las normas a una carpeta temporal y juega ahí, así que sirve con la carpeta `practica/`
del kit, que tiene los casos y las esperadas juntos.

La cátedra corre `jugar` con la entrega del grupo en una máquina que tiene solo `entradas/` (`casos.jsonl` y
`normas/<variante>/`), y `puntuar` después, en otra, con `esperadas/`. Por eso `jugar` se niega a arrancar si encuentra un
archivo `esperadas-*.jsonl` en la carpeta desde la que se corre, en la de los casos, en la de las normas o en cualquiera
de las tres carpetas de arriba de la de las normas."""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
from pathlib import Path

from .casos import cargar_casos, cargar_esperadas, escribir_jsonl, leer_jsonl
from .comparar import comparar, resumir
from .contrato import cargar_entrega
from .entorno import Entorno, VistaDelAgente


def caracteres_de_contexto(mensajes) -> int:
    """Lo que se le pasó al modelo en todo el caso: en cada respuesta del modelo, el largo de todos los mensajes
    anteriores. Es una medida del gasto que no depende del tokenizador. Sale de la conversación que devuelve el agente."""
    if not isinstance(mensajes, list):
        return 0
    total = acumulado = 0
    for m in mensajes:
        rol, contenido = (m.get("role"), m.get("content", "")) if isinstance(m, dict) else (None, m)
        if rol == "assistant":
            total += acumulado
        acumulado += len(str(contenido))
    return total


def _segundos(desde: float) -> float:
    return round(time.perf_counter() - desde, 3)


def _jugar(entrega, casos, ruta_normas: Path, salida: Path | None = None) -> tuple[list[dict], dict]:
    if not casos:
        raise ValueError("no hay casos")
    tiempos: dict = {"casos": len(casos)}
    with tempfile.TemporaryDirectory(prefix="admision-normas-") as carpeta:
        # El buscador recibe una copia de las normas en una carpeta que no tiene nada más.
        copia = Path(carpeta) / "normas"
        shutil.copytree(Path(ruta_normas), copia)
        t = time.perf_counter()
        buscador = entrega.construir_buscador(copia)
        tiempos["construir_buscador"] = _segundos(t)
        t = time.perf_counter()
        agente = entrega.construir_agente()
        tiempos["construir_agente"] = _segundos(t)

        entornos = [Entorno(c, buscador) for c in casos]
        ultima_llamada: list[float | None] = [None] * len(casos)
        inicio = time.perf_counter()

        def paso_del_caso(i):
            def paso(herramienta, argumentos):
                try:
                    return entornos[i].paso(herramienta, argumentos)
                finally:
                    ultima_llamada[i] = _segundos(inicio)
            return paso

        vistas = [VistaDelAgente(c.paciente_id, paso_del_caso(i)) for i, c in enumerate(casos)]
        tiempos["error"] = None
        try:
            conversaciones = agente.jugar_lote(vistas)
            if not isinstance(conversaciones, list) or len(conversaciones) != len(casos):
                n = len(conversaciones) if isinstance(conversaciones, list) else type(conversaciones).__name__
                raise ValueError(f"jugar_lote devolvió {n} conversaciones para {len(casos)} casos")
        except Exception as e:  # lo que ya jugó queda en las trazas, con el error anotado
            tiempos["error"] = f"{type(e).__name__}: {e}"
            tiempos["error_detalle"] = traceback.format_exc()
            print(f"jugar_lote falló: {tiempos['error']}", file=sys.stderr)
            conversaciones = [[] for _ in casos]
        tiempos["jugar_lote"] = _segundos(inicio)
        tiempos["jugar_lote_por_caso"] = round(tiempos["jugar_lote"] / len(casos), 3)

    trazas = [{"caso": c.id, "mensajes": m, "log": e.log, "decision": e.decision, "segundos": s}
              for c, e, m, s in zip(casos, entornos, conversaciones, ultima_llamada, strict=True)]
    # Ida y vuelta por JSON: en memoria queda exactamente lo que se escribe en el archivo.
    trazas = json.loads(json.dumps(trazas, ensure_ascii=False, default=str))
    if salida is not None:
        salida = Path(salida)
        escribir_jsonl(trazas, salida / "trazas.jsonl")
        (salida / "tiempos.json").write_text(json.dumps(tiempos, ensure_ascii=False, indent=2), encoding="utf-8")
    return trazas, tiempos


class EsperadasAlAlcance(RuntimeError):
    """Hay fichas esperadas en una carpeta que el agente puede encontrar sin buscar mucho."""


def revisar_que_no_haya_esperadas(ruta_normas: Path, ruta_casos: Path | None = None) -> None:
    """Levanta `EsperadasAlAlcance` si hay un `esperadas-*.jsonl` en la carpeta desde la que se corre, en la de los
    casos, en la de las normas o en alguna de las tres carpetas de arriba de la de las normas."""
    normas = Path(ruta_normas).resolve()
    carpetas = [Path.cwd().resolve(), *([Path(ruta_casos).resolve().parent] if ruta_casos is not None else []),
                normas, *list(normas.parents)[:3]]
    for carpeta in dict.fromkeys(carpetas):
        encontradas = sorted(carpeta.glob("esperadas-*.jsonl"))
        if encontradas:
            raise EsperadasAlAlcance(
                f"no se puede jugar con fichas esperadas a mano: está {encontradas[0]}. Para jugar hace falta solo "
                "la carpeta con los casos y las normas; las esperadas van en otra carpeta y se usan después, con "
                "`puntuar`. Para practicar con la carpeta practica/ del kit, usen `practica`, que copia los casos y "
                "las normas aparte.")


def _jugar_revisado(entrega, casos, ruta_normas: Path, salida: Path | None = None,
                    ruta_casos: Path | None = None) -> tuple[list[dict], dict]:
    revisar_que_no_haya_esperadas(ruta_normas, ruta_casos)
    return _jugar(entrega, casos, ruta_normas, salida)


def jugar(entrega, casos, ruta_normas: Path, salida: Path | None = None, ruta_casos: Path | None = None) -> list[dict]:
    """Primera fase: juega los casos con la entrega y devuelve las trazas (si hay `salida`, escribe `trazas.jsonl` y
    `tiempos.json`). El agente recibe una `VistaDelAgente` por caso. No usa las fichas esperadas.

    Antes de arrancar revisa que no haya fichas esperadas cerca (`revisar_que_no_haya_esperadas`; `ruta_casos` es el
    archivo de donde salieron los casos, si se quiere revisar también su carpeta). Para la corrida de un grupo, la
    máquina tiene solo `entradas/` (`casos.jsonl` y `normas/<variante>/`), y `puntuar` corre en otra, con
    `esperadas/`."""
    return _jugar_revisado(entrega, casos, ruta_normas, salida, ruta_casos)[0]


def _copiar_entradas(carpeta: Path, ruta_normas: Path, ruta_casos: Path | None = None) -> tuple[Path, Path | None]:
    """Copia las normas (y los casos, si hay ruta) a `carpeta`, que no tiene nada más: para practicar con la carpeta
    `practica/` del kit, que tiene los casos y las esperadas juntos."""
    normas = Path(carpeta) / "normas" / Path(ruta_normas).resolve().name
    shutil.copytree(Path(ruta_normas), normas)
    casos = None
    if ruta_casos is not None:
        casos = Path(carpeta) / "casos.jsonl"
        shutil.copy(Path(ruta_casos), casos)
    return normas, casos


def puntuar(trazas: list[dict], esperadas: dict, salida: Path | None = None,
            tiempos: dict | None = None) -> tuple[list[dict], dict]:
    """Segunda fase: el veredicto de cada traza contra su ficha esperada y el resumen. Si hay `salida`, escribe
    `resultados.jsonl` y `resumen.json`. Con `tiempos` (lo que escribió jugar), los suma al resumen."""
    if not trazas:
        raise ValueError("no hay trazas")
    for t in trazas:
        if t["caso"] not in esperadas:
            raise KeyError(f"no hay ficha esperada para el caso {t['caso']}")
    resultados = []
    for t in trazas:
        r = comparar(esperadas[t["caso"]], t["decision"], t["log"])
        r["busquedas"] = sum(x["herramienta"] == "buscar_normativa" for x in t["log"])
        r["caracteres_de_contexto"] = caracteres_de_contexto(t["mensajes"])
        r["segundos"] = t.get("segundos")
        resultados.append(r)
    resumen = resumir(resultados)
    resumen["busquedas_por_caso"] = round(sum(r["busquedas"] for r in resultados) / len(resultados), 2)
    resumen["caracteres_de_contexto_por_caso"] = round(
        sum(r["caracteres_de_contexto"] for r in resultados) / len(resultados))
    if tiempos is not None:
        resumen["segundos"] = {k: tiempos.get(k) for k in
                               ("construir_buscador", "construir_agente", "jugar_lote", "jugar_lote_por_caso")}
        resumen["error"] = tiempos.get("error")
    if salida is not None:
        salida = Path(salida)
        escribir_jsonl(resultados, salida / "resultados.jsonl")
        (salida / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    return resultados, resumen


def correr(entrega, casos, esperadas: dict | Path, ruta_normas: Path, salida: Path | None = None):
    """Las dos fases seguidas, en el mismo proceso: para la práctica. `esperadas` es el dict de `cargar_esperadas` o la
    ruta del archivo; con una ruta, se lee recién después de jugar. Juega con una copia de las normas en una carpeta
    temporal, así que las esperadas pueden estar al lado de los casos."""
    if isinstance(esperadas, dict):
        for c in casos:
            if c.id not in esperadas:
                raise KeyError(f"no hay ficha esperada para el caso {c.id}")
    with tempfile.TemporaryDirectory(prefix="admision-practica-") as carpeta:
        normas, _ = _copiar_entradas(Path(carpeta), ruta_normas)
        trazas, tiempos = _jugar_revisado(entrega, casos, normas, salida)
    if not isinstance(esperadas, dict):
        esperadas = cargar_esperadas(esperadas)
    return puntuar(trazas, esperadas, salida, tiempos)


def _leer_tiempos(ruta_trazas: Path) -> dict | None:
    ruta = Path(ruta_trazas).parent / "tiempos.json"
    return json.loads(ruta.read_text(encoding="utf-8")) if ruta.exists() else None


def _puntuar_en_otro_proceso(trazas: Path, esperadas: Path, salida: Path) -> int:
    paquete = str(Path(__file__).resolve().parent.parent)  # el mismo `admision` que está corriendo
    env = dict(os.environ, PYTHONPATH=os.pathsep.join(filter(None, [paquete, os.environ.get("PYTHONPATH")])))
    return subprocess.run([sys.executable, "-m", "admision.correr", "puntuar", "--trazas", str(trazas),
                           "--esperadas", str(esperadas), "--salida", str(salida)], env=env).returncode


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    fases = ap.add_subparsers(dest="fase", required=True)
    j = fases.add_parser("jugar", help="juega los casos con la entrega (sin las fichas esperadas)")
    p = fases.add_parser("puntuar", help="compara las trazas con las fichas esperadas")
    pr = fases.add_parser("practica", help="jugar y después puntuar, en otro proceso")
    for sub in (j, pr):
        sub.add_argument("--entrega", type=Path, required=True)
        sub.add_argument("--casos", type=Path, required=True)
        sub.add_argument("--normas", type=Path, required=True)
    p.add_argument("--trazas", type=Path, required=True)
    for sub in (p, pr):
        sub.add_argument("--esperadas", type=Path, required=True)
    for sub in (j, p, pr):
        sub.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args(argv)

    if a.fase == "puntuar":
        _, resumen = puntuar(leer_jsonl(a.trazas), cargar_esperadas(a.esperadas), a.salida, _leer_tiempos(a.trazas))
        print(json.dumps(resumen, ensure_ascii=False, indent=2))
        return 0
    if a.fase == "practica" and not a.esperadas.exists():
        ap.error(f"no existe {a.esperadas}")
    salida = a.salida.resolve()
    if a.fase == "jugar":
        try:
            revisar_que_no_haya_esperadas(a.normas, a.casos)
        except EsperadasAlAlcance as e:
            print(e, file=sys.stderr)
            return 2
        trazas, tiempos = _jugar(cargar_entrega(a.entrega), cargar_casos(a.casos), a.normas, salida)
        print(json.dumps({"casos": len(trazas), "con_ficha": sum(t["decision"] is not None for t in trazas),
                          **{k: v for k, v in tiempos.items() if k != "error_detalle"}}, ensure_ascii=False, indent=2))
        return 0
    with tempfile.TemporaryDirectory(prefix="admision-practica-") as carpeta:
        normas, casos = _copiar_entradas(Path(carpeta), a.normas, a.casos)
        try:
            revisar_que_no_haya_esperadas(normas, casos)
        except EsperadasAlAlcance as e:
            print(e, file=sys.stderr)
            return 2
        _jugar(cargar_entrega(a.entrega), cargar_casos(casos), normas, salida)
    return _puntuar_en_otro_proceso(salida / "trazas.jsonl", a.esperadas.resolve(), salida)


if __name__ == "__main__":
    sys.exit(main())
