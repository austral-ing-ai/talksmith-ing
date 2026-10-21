"""El agente de la referencia de la cátedra: protocolo JSON sobre mensajes de chat comunes. En cada turno el modelo
responde {"herramienta": ..., "argumentos": {...}} y el resultado vuelve como mensaje del usuario.

Es un ejemplo: el mensaje de sistema, el formato y la estrategia se pueden cambiar enteros. `modelo_lote` es cualquier
función que recibe una lista de conversaciones y devuelve una respuesta por conversación."""

import json
import re

HERRAMIENTAS = [
    {"nombre": "leer_triage", "argumentos": {"paciente_id": "id del paciente, por ejemplo P-1234"},
     "descripcion": "Devuelve la nota de triage del paciente: edad, nivel, motivo de consulta, cómo llegó, documento "
                    "y credenciales presentados, si puede responder preguntas, acompañante y si se lesionó "
                    "trabajando."},
    {"nombre": "preguntar", "argumentos": {"paciente_id": "id del paciente", "a_quien": "paciente | acompanante",
                                           "tema": "cobertura | art"},
     "descripcion": "Le pregunta al paciente o a su acompañante por su obra social o prepaga (tema cobertura) o por "
                    "la ART de su empleador (tema art)."},
    {"nombre": "verificar_afiliacion", "argumentos": {"entidad": "nombre de la entidad, tal como lo informaron",
                                                      "numero_afiliado": "número de afiliado (en una ART, el CUIL)"},
     "descripcion": "Consulta a la entidad si la afiliación está activa."},
    {"nombre": "buscar_normativa", "argumentos": {"consulta": "texto libre"},
     "descripcion": "Busca en las normas del hospital y devuelve las 2 secciones más relevantes."},
    {"nombre": "registrar_decision", "argumentos": {
        "registro": "definitivo | provisorio",
        "numero_documento": "número del documento tal como figura en él, o null",
        "box_antes_del_registro": "true si se ubica al paciente en el box antes de registrarlo, si no false",
        "circuito": "ecg | codigo_acv | codigo_sepsis | ninguno",
        "plazo_circuito_min": "plazo del circuito en minutos desde el ingreso, o null si no hay circuito",
        "cobertura": "obra_social | prepaga | art | sin_cobertura",
        "entidad_a_notificar": "nombre de la entidad a la que se notifica la atención, o null",
        "aviso_al_voluntariado": "true o false",
        "fundamentos": "lista de los códigos de sección que fundamentan la ficha, por ejemplo [\"NOR-ADM-01\"]"},
     "descripcion": "Registra la ficha de admisión. Termina el caso."},
]


def mensaje_de_sistema() -> str:
    herramientas = []
    for h in HERRAMIENTAS:
        args = ", ".join(f'"{k}": {v}' for k, v in h["argumentos"].items())
        herramientas.append(f"- {h['nombre']}: {h['descripcion']}\n  argumentos: {{{args}}}")
    return "\n\n".join([
        "Sos el agente de admisión de la guardia del Hospital General de Prueba. Para cada paciente que ingresa "
        "completás su ficha de admisión siguiendo las normas del hospital. No tomás decisiones clínicas.",
        "Herramientas:\n" + "\n".join(herramientas),
        "En cada turno respondé solo con un objeto JSON, sin texto antes ni después:\n"
        '{"herramienta": "<nombre>", "argumentos": {...}}\n'
        "Usá una herramienta por turno. El caso termina cuando llamás a registrar_decision.",
        "Las normas que aplican son NOR-ADM-01 a NOR-ADM-03 (registro), NOR-COB-01 a NOR-COB-04 (coberturas) y "
        "NOR-TDE-01 a NOR-TDE-04 (circuitos tiempo-dependientes). Buscalas con buscar_normativa antes de decidir.",
    ])


def primer_mensaje(paciente_id: str) -> str:
    return f"Ingresó a la guardia el paciente {paciente_id}. Completá su ficha de admisión."


def extraer_json(texto: str) -> dict | None:
    """El primer objeto JSON balanceado del texto que tenga 'herramienta' (acepta bloques ```json)."""
    for inicio in [m.start() for m in re.finditer(r"\{", texto)]:
        profundidad, en_cadena, escape = 0, False, False
        for i in range(inicio, len(texto)):
            ch = texto[i]
            if en_cadena:
                if escape:
                    escape = False
                elif ch == "\\":
                    escape = True
                elif ch == '"':
                    en_cadena = False
                continue
            if ch == '"':
                en_cadena = True
            elif ch == "{":
                profundidad += 1
            elif ch == "}":
                profundidad -= 1
                if profundidad == 0:
                    try:
                        obj = json.loads(texto[inicio:i + 1])
                    except json.JSONDecodeError:
                        break
                    if isinstance(obj, dict) and "herramienta" in obj:
                        return obj
                    break
    return None


class _Partida:
    def __init__(self, entorno, max_turnos: int, max_sin_json: int):
        self.entorno, self.max_turnos, self.max_sin_json = entorno, max_turnos, max_sin_json
        self.mensajes = [{"role": "system", "content": mensaje_de_sistema()},
                         {"role": "user", "content": primer_mensaje(entorno.paciente_id)}]
        self.turnos = self.sin_json = 0
        self.activa = True

    def recibir(self, respuesta: str) -> None:
        self.turnos += 1
        self.mensajes.append({"role": "assistant", "content": respuesta})
        obj = extraer_json(respuesta)
        if obj is None:
            self.sin_json += 1
            if self.sin_json >= self.max_sin_json:
                self.activa = False
                return
            self.mensajes.append({"role": "user", "content":
                                  'No entendí tu respuesta. Respondé solo con un objeto JSON: '
                                  '{"herramienta": "<nombre>", "argumentos": {...}}'})
        else:
            self.sin_json = 0
            herramienta = str(obj.get("herramienta", ""))
            obs, fin = self.entorno.paso(herramienta, obj.get("argumentos") or {})
            if fin:
                self.activa = False
                return
            self.mensajes.append({"role": "user", "content": f"Resultado de {herramienta}:\n{obs}"})
        if self.turnos >= self.max_turnos:
            self.activa = False


class AgenteJSON:
    def __init__(self, modelo_lote, max_turnos: int = 16, max_sin_json: int = 3):
        self.modelo_lote, self.max_turnos, self.max_sin_json = modelo_lote, max_turnos, max_sin_json

    def jugar_lote(self, entornos: list) -> list[list[dict]]:
        """Juega todos los casos a la vez: en cada vuelta, una llamada al modelo con las partidas activas."""
        partidas = [_Partida(e, self.max_turnos, self.max_sin_json) for e in entornos]
        while activas := [x for x in partidas if x.activa]:
            for partida, respuesta in zip(activas, self.modelo_lote([x.mensajes for x in activas]), strict=True):
                partida.recibir(respuesta)
        return [x.mensajes for x in partidas]
