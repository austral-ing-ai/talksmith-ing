"""Un caso es un paciente que ingresa por la guardia. Guarda solo lo que el entorno necesita para contestar las
herramientas: lo que dice el triage, lo que contestan el paciente o su acompañante y lo que informa cada entidad."""

import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Caso:
    id: str
    paciente_id: str
    nombre: str
    edad: int
    nivel: int
    motivo: str
    nota: str
    sepsis: str
    llegada: str                       # «en ambulancia» o «por sus propios medios»
    documento_tipo: str | None
    documento_numero: str | None
    # Credenciales presentadas, (tipo, entidad, número) con tipo obra_social | prepaga, en el orden de la nota.
    credenciales: tuple[tuple[str, str, str], ...]
    puede_responder: bool
    no_responde_porque: str | None
    acompanante: str | None
    trabajo: str | None                # None | trabajando | en el trayecto
    # Lo que contesta quien corresponda si se le pregunta la cobertura (None: no tiene).
    declarada: tuple[str, str, str] | None
    art: tuple[str, str] | None        # (ART del empleador, CUIL)
    # Estado de cada afiliación al verificarla: "entidad|numero" -> activa.
    afiliaciones: dict[str, bool]

    @classmethod
    def desde_dict(cls, d: dict) -> "Caso":
        d = dict(d)
        d["credenciales"] = tuple(tuple(x) for x in d["credenciales"])
        for k in ("declarada", "art"):
            if d[k] is not None:
                d[k] = tuple(d[k])
        return cls(**d)

    def como_dict(self) -> dict:
        return asdict(self)


def leer_jsonl(ruta: Path) -> list[dict]:
    return [json.loads(x) for x in Path(ruta).read_text(encoding="utf-8").splitlines() if x.strip()]


def escribir_jsonl(filas, ruta: Path) -> None:
    Path(ruta).parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        f.writelines(json.dumps(x, ensure_ascii=False, default=str) + "\n" for x in filas)


def cargar_casos(ruta: Path) -> list[Caso]:
    return [Caso.desde_dict(d) for d in leer_jsonl(ruta)]


def cargar_esperadas(ruta: Path) -> dict[str, dict]:
    """{id del caso: {"caso", "ficha", "verificacion": {"requerida": [entidad, número] | None, "prohibidas": [...]}}}."""
    return {d["caso"]: d for d in leer_jsonl(ruta)}
