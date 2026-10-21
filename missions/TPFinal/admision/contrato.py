"""El contrato de la entrega. El repo del grupo tiene un archivo de Python (por ejemplo `entrega.py`) con dos funciones:

    def construir_buscador(ruta_normas: Path) -> Buscador
        # Arma el buscador con las normas de `ruta_normas` (en el test, los valores cambian).
    def construir_agente() -> Agente
        # Carga el modelo una sola vez.

Buscador: `recuperar(consulta: str, k: int) -> list` de objetos con atributo `texto` (o strings), de más a menos
relevante. Si define `k_entorno`, es la cantidad que devuelve `buscar_normativa` en el entorno (si no, 2).

Agente: `jugar_lote(entornos: list[VistaDelAgente]) -> list[list[dict]]`. Cada elemento de `entornos` es la vista
del agente sobre un caso: tiene solo `paciente_id` y `paso(herramienta, argumentos) -> (observación, terminó)`. El
agente juega cada caso llamando a `paso(...)` hasta `registrar_decision` y devuelve, por caso, la conversación completa
con el modelo (cada mensaje que entró y cada uno que salió), en el mismo orden que `entornos`. El agente no llama a
servicios externos.

La vista no es una barrera de seguridad: saca el acceso obvio al caso, al log y a la ficha, que guarda el runner.
`construir_buscador` recibe una copia de las normas en una carpeta aparte, y el runner juega sin cargar las fichas
esperadas (ver `admision.correr`)."""

import importlib.util
import sys
from pathlib import Path


def cargar_entrega(ruta: Path):
    ruta = Path(ruta).resolve()
    nombre = f"entrega_{ruta.stem}"
    if str(ruta.parent) not in sys.path:
        sys.path.insert(0, str(ruta.parent))  # para que importe los módulos vecinos del repo del grupo
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[nombre] = modulo  # lo necesitan los @dataclass con `from __future__ import annotations`
    spec.loader.exec_module(modulo)
    for nombre in ("construir_buscador", "construir_agente"):
        if not callable(getattr(modulo, nombre, None)):
            raise AttributeError(f"{ruta.name} no define {nombre}()")
    return modulo
