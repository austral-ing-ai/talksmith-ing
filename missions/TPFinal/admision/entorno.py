"""El entorno de la ficha de admisión: cinco herramientas que devuelven texto. La cátedra corre el test secreto con
este mismo entorno.

`paso(herramienta, argumentos)` devuelve (observación, terminó) y anota todo en `log`. Un error de herramienta o de
argumentos no termina el caso: vuelve como observación. Después de MAX_LLAMADAS llamadas el caso termina sin ficha, y
una llamada a un caso terminado devuelve ("El caso ya terminó.", True) sin anotarse.

`buscar_normativa` usa el buscador del grupo: `buscador.recuperar(consulta, k)` con k = `buscador.k_entorno` si lo
define (si no, K_POR_DEFECTO), y une los textos de lo que devuelve (objetos con `.texto` o strings). Si el buscador
falla, la llamada vuelve como error ("Error: el buscador falló: <tipo de error>.") y el caso sigue.

El agente no recibe el `Entorno` sino una `VistaDelAgente`, que solo tiene `paciente_id` y `paso`."""

import unicodedata

from .casos import Caso
from .catalogo import ARTS, OBRAS_SOCIALES, PREPAGAS

MAX_LLAMADAS = 40
K_POR_DEFECTO = 2
CAMPOS = ["registro", "numero_documento", "box_antes_del_registro", "circuito", "plazo_circuito_min", "cobertura",
          "entidad_a_notificar", "aviso_al_voluntariado"]
VALORES = {
    "registro": {"definitivo", "provisorio"},
    "circuito": {"ecg", "codigo_acv", "codigo_sepsis", "ninguno"},
    "cobertura": {"obra_social", "prepaga", "art", "sin_cobertura"},
}


def _norm(texto) -> str:
    t = unicodedata.normalize("NFD", str(texto).strip().lower())
    return " ".join("".join(c for c in t if unicodedata.category(c) != "Mn").split())


def _credencial(c: tuple[str, str, str]) -> str:
    tipo = "obra social" if c[0] == "obra_social" else "prepaga"
    return f"la credencial de {c[1]} ({tipo}), número de afiliado {c[2]}"


def nota_de_triage(c: Caso) -> str:
    lineas = [f"Nota de triage del paciente {c.paciente_id}",
              f"Paciente: {c.nombre}, {c.edad} años.",
              f"Nivel de triage: {c.nivel}.",
              f"Motivo de consulta: {c.motivo}.",
              f"Llegada: {c.llegada}.",
              f"Nota de enfermería: {c.nota}",
              f"Sospecha de sepsis: {c.sepsis}."]
    lineas.append(f"Documento: presentó {c.documento_tipo} {c.documento_numero}." if c.documento_numero
                  else "Documento: no presentó documento.")
    if len(c.credenciales) == 2:
        lineas.append(f"Credenciales de cobertura: presentó dos, {_credencial(c.credenciales[0])}, "
                      f"y {_credencial(c.credenciales[1])}.")
    elif c.credenciales:
        lineas.append(f"Credencial de cobertura: presentó {_credencial(c.credenciales[0])}.")
    else:
        lineas.append("Credencial de cobertura: no presentó credencial.")
    lineas.append("Puede responder preguntas: sí." if c.puede_responder
                  else f"Puede responder preguntas: no ({c.no_responde_porque}).")
    lineas.append(f"Acompañante: {c.acompanante}." if c.acompanante else "Acompañante: ninguno.")
    lineas.append("Se lesionó o enfermó trabajando o en el trayecto al trabajo: "
                  + (f"sí, {c.trabajo}." if c.trabajo else "no."))
    return "\n".join(lineas)


def _texto(fragmento) -> str:
    return fragmento if isinstance(fragmento, str) else fragmento.texto


class Entorno:
    def __init__(self, caso: Caso, buscador):
        self.caso = caso
        self.buscador = buscador
        self.log: list[dict] = []
        self.decision: dict | None = None
        self.terminado = False

    @property
    def paciente_id(self) -> str:
        """Lo único que el agente sabe al empezar: el id del paciente que ingresó."""
        return self.caso.paciente_id

    def paso(self, herramienta: str, argumentos: dict) -> tuple[str, bool]:
        if self.terminado:
            return "El caso ya terminó.", True
        try:
            obs = self._ejecutar(herramienta, argumentos if isinstance(argumentos, dict) else {})
            ok = True
        except ValueError as e:
            obs, ok = f"Error: {e}", False
        self.log.append({"herramienta": herramienta, "argumentos": argumentos, "observacion": obs, "valida": ok})
        if not self.terminado and len(self.log) >= MAX_LLAMADAS:
            self.terminado = True
        return obs, self.terminado

    def _paciente(self, a: dict) -> None:
        if str(a.get("paciente_id", "")).strip().upper() != self.caso.paciente_id:
            raise ValueError(f"no hay ningún paciente con id {a.get('paciente_id')!r} en la guardia.")

    def _ejecutar(self, h: str, a: dict) -> str:
        c = self.caso
        if h == "leer_triage":
            self._paciente(a)
            return nota_de_triage(c)
        if h == "preguntar":
            self._paciente(a)
            quien, tema = _norm(a.get("a_quien", "")), _norm(a.get("tema", ""))
            if quien not in ("paciente", "acompanante") or tema not in ("cobertura", "art"):
                raise ValueError("a_quien tiene que ser paciente o acompanante, y tema, cobertura o art.")
            if quien == "paciente" and not c.puede_responder:
                return "El paciente no está en condiciones de responder."
            if quien == "acompanante" and not c.acompanante:
                return "El paciente no tiene acompañante en la guardia."
            sujeto = "El paciente" if quien == "paciente" else f"El acompañante ({c.acompanante})"
            if tema == "art":
                if not c.trabajo:
                    return f"{sujeto} dice que no se lesionó ni enfermó trabajando ni en el trayecto."
                return (f"{sujeto} dice que la ART de su empleador es {c.art[0]}. CUIL del paciente: {c.art[1]}.")
            if c.declarada is None:
                return f"{sujeto} dice que no tiene obra social ni prepaga."
            tipo = "obra social" if c.declarada[0] == "obra_social" else "prepaga"
            return (f"{sujeto} dice que tiene {c.declarada[1]} ({tipo}), número de afiliado {c.declarada[2]}.")
        if h == "verificar_afiliacion":
            entidad, numero = _norm(a.get("entidad", "")), _norm(a.get("numero_afiliado", ""))
            conocidas = {}
            for clave, activa in c.afiliaciones.items():
                e, n = clave.split("|")
                conocidas.setdefault(_norm(e), {})[_norm(n)] = (e, activa)
            if entidad not in {_norm(x) for x in OBRAS_SOCIALES + PREPAGAS + ARTS}:
                return "No hay ninguna entidad con ese nombre."
            if numero not in conocidas.get(entidad, {}):
                return "La entidad no encuentra ese número de afiliado."
            nombre, activa = conocidas[entidad][numero]
            return f"{nombre} informa que la afiliación {numero} está {'activa' if activa else 'inactiva'}."
        if h == "buscar_normativa":
            consulta = str(a.get("consulta", "")).strip()
            if not consulta:
                raise ValueError("falta la consulta.")
            try:
                frs = self.buscador.recuperar(consulta, getattr(self.buscador, "k_entorno", K_POR_DEFECTO))
                return "\n\n".join(_texto(f) for f in frs) if frs else "No se encontró ninguna sección."
            except Exception as e:  # un error del buscador del grupo no corta la corrida
                raise ValueError(f"el buscador falló: {type(e).__name__}.") from e
        if h == "registrar_decision":
            self.decision = validar_decision(a)
            self.terminado = True
            return "Ficha registrada."
        raise ValueError(f"no existe la herramienta {h!r}.")


class VistaDelAgente:
    """Lo que recibe el agente de cada caso: el id del paciente y `paso(herramienta, argumentos)`, nada más. El runner
    se queda con el `Entorno` (el caso, el log y la ficha) para escribir las trazas.

    No es una barrera de seguridad: en Python, con empeño, se llega a cualquier objeto. Saca el acceso obvio a `.caso`,
    `.log` y `.decision`; leerlos por otro camino es hacer trampa."""

    __slots__ = ("__paciente_id", "__paso")

    def __init__(self, paciente_id: str, paso):
        self.__paciente_id = paciente_id
        self.__paso = paso

    @property
    def paciente_id(self) -> str:
        """Lo único que el agente sabe al empezar: el id del paciente que ingresó."""
        return self.__paciente_id

    def paso(self, herramienta: str, argumentos: dict) -> tuple[str, bool]:
        """Llama a una herramienta. Devuelve (observación, terminó)."""
        return self.__paso(herramienta, argumentos)

    def __repr__(self) -> str:
        return f"VistaDelAgente({self.__paciente_id!r})"


def validar_decision(a: dict) -> dict:
    if "aviso_al_voluntariado" not in a:
        raise ValueError("faltan campos: aviso_al_voluntariado.")
    aviso = a["aviso_al_voluntariado"]
    if not isinstance(aviso, bool):
        if _norm(aviso) not in ("true", "false"):
            raise ValueError("aviso_al_voluntariado tiene que ser true o false.")
        aviso = _norm(aviso) == "true"
    faltan = [k for k in CAMPOS[:-1] if k not in a]
    if faltan:
        raise ValueError(f"faltan campos: {', '.join(faltan)}.")
    d = {k: a[k] for k in CAMPOS[:-1]}
    for k, permitidos in VALORES.items():
        if _norm(d[k]) not in permitidos:
            raise ValueError(f"{k} tiene que ser uno de: {', '.join(sorted(permitidos))}.")
        d[k] = _norm(d[k])
    if not isinstance(d["box_antes_del_registro"], bool):
        if _norm(d["box_antes_del_registro"]) in ("true", "false"):
            d["box_antes_del_registro"] = _norm(d["box_antes_del_registro"]) == "true"
        else:
            raise ValueError("box_antes_del_registro tiene que ser true o false.")
    plazo = d["plazo_circuito_min"]
    if plazo in ("", "null", "None"):
        plazo = None
    if plazo is not None:
        try:
            plazo = int(plazo)
        except (TypeError, ValueError):
            raise ValueError("plazo_circuito_min tiene que ser un número de minutos o null.") from None
    d["plazo_circuito_min"] = plazo
    for k in ("numero_documento", "entidad_a_notificar"):
        if d[k] in ("", "null", "None"):
            d[k] = None
    f = a.get("fundamentos", [])
    d["fundamentos"] = [str(x).strip().upper() for x in f] if isinstance(f, list) else [str(f).strip().upper()]
    d["aviso_al_voluntariado"] = aviso
    return d
