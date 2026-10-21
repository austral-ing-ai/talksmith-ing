"""Las normas del hospital: una sección por archivo (`NOR-XXX-NN.md`) más `parametros.yaml` con los valores.

Cada sección cita sus parámetros por código («P-ADM-1»), y el texto que ve el agente termina con una línea con los
valores que cita («Valores: P-ADM-1 = nivel 2.»). En el test de la cátedra los valores cambian, así que el buscador se
arma siempre con las normas que recibe, nunca con valores fijos."""

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

PATRON_PARAMETRO = re.compile(r"(P-[A-Z]{3})-(\d+)(?: a \1-(\d+))?")
UNIDADES = {"nivel": "nivel {v}", "min": "{v} min", "dias": "{v} días", "anios": "{v} años"}


@dataclass(frozen=True)
class Seccion:
    id: str
    # El texto de la sección, con su encabezado y sin la línea de valores.
    cuerpo: str
    # «Valores: ...» con los parámetros que cita el cuerpo ("" si no cita ninguno).
    valores: str = ""

    @property
    def texto(self) -> str:
        return f"{self.cuerpo}\n{self.valores}" if self.valores else self.cuerpo


def valor_como_texto(valor: int, unidad: str) -> str:
    if unidad == "camas":
        return f"{valor} {'cama' if valor == 1 else 'camas'}"
    return UNIDADES.get(unidad, "{v}").format(v=valor)


def cargar_parametros(ruta: Path) -> dict[str, str]:
    """{código: valor con su unidad}, desde `ruta/parametros.yaml`."""
    datos = yaml.safe_load((Path(ruta) / "parametros.yaml").read_text(encoding="utf-8"))
    return {p["codigo"]: valor_como_texto(p["valor"], p["unidad"]) for p in datos["parametros"]}


def linea_de_valores(cuerpo: str, valores: dict[str, str]) -> str:
    """«Valores: P-TDE-3 = 15 min; P-TDE-4 = 60 min.» con los parámetros que cita el cuerpo, en orden de aparición."""
    citados = list(dict.fromkeys(f"{prefijo}-{n}" for prefijo, desde, hasta in PATRON_PARAMETRO.findall(cuerpo)
                                 for n in range(int(desde), int(hasta or desde) + 1)))
    return ("Valores: " + "; ".join(f"{c} = {valores[c]}" for c in citados) + ".") if citados else ""


def cargar_normas(ruta: Path) -> list[Seccion]:
    """Las secciones de `ruta`, en orden alfabético de archivo."""
    valores = cargar_parametros(ruta)
    secciones = []
    for archivo in sorted(Path(ruta).glob("NOR-*.md")):
        cuerpo = archivo.read_text(encoding="utf-8").strip()
        secciones.append(Seccion(archivo.stem, cuerpo, linea_de_valores(cuerpo, valores)))
    return secciones
