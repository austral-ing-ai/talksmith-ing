"""Genera casos de pacientes, sin la respuesta, para que los grupos armen trazas sintéticas.

    from admision.generador import generar
    casos = generar(semilla=42, n=1000)

Cada caso combina una situación de cobertura con un motivo de consulta. La ficha correcta no viene: hay que deducirla
de las normas y del historial."""

import random

from .casos import Caso
from .catalogo import APELLIDOS, ARTS, NOMBRES, NOMBRES_ACOMPANANTE, OBRAS_SOCIALES, PREPAGAS

COBERTURAS = ["credencial_activa", "credencial_inactiva", "declara_activa", "declara_inactiva", "declara_ninguna",
              "acompanante_responde", "sin_nadie", "trabajo_con_credencial", "trabajo_sin_credencial",
              "dos_credenciales"]
CIRCUITOS = ["ecg", "codigo_acv", "sepsis_probable", "sepsis_posible", "ninguno"]
MOTIVOS = {
    "ecg": ("dolor torácico", [
        "Dolor opresivo en el pecho desde hace {n} minutos, que se le va al brazo izquierdo.",
        "Dolor en el centro del pecho que empezó hace {n} minutos mientras caminaba.",
    ], (2, 3)),
    "codigo_acv": ("signos neurológicos focales de inicio súbito", [
        "Hace {n} minutos empezó a hablar con dificultad y perdió fuerza en el brazo derecho.",
        "Se le torció la boca y perdió fuerza en la pierna izquierda de golpe, hace {n} minutos.",
    ], (1, 2)),
    "sepsis_probable": ("sospecha de sepsis", [
        "Fiebre de 39 °C y escalofríos desde ayer; presión baja y somnolencia.",
        "Fiebre alta y confusión desde la mañana; frecuencia cardíaca alta.",
    ], (1, 2)),
    "sepsis_posible": ("sospecha de sepsis", [
        "Fiebre y ardor al orinar desde hace dos días; signos vitales estables.",
        "Fiebre de 38,4 °C desde anoche y malestar general.",
    ], (3, 3)),
}
OTROS_MOTIVOS = [
    ("dolor abdominal", "Dolor abdominal intenso desde hace {n} horas, con vómitos.", (2, 4)),
    ("fiebre y tos", "Fiebre de 38,5 °C y tos con flema desde hace cuatro días.", (3, 4)),
    ("cefalea", "Dolor de cabeza desde hace {n} horas, igual a otros que tuvo; sin otros síntomas.", (3, 5)),
    ("palpitaciones", "Palpitaciones desde hace una hora, con mareo.", (2, 3)),
    ("traumatismo de miembro", "Se torció el tobillo; dolor e hinchazón, puede apoyar el pie.", (4, 5)),
    ("herida cortante", "Corte en la mano con un vidrio; sangrado controlado con presión.", (3, 5)),
]
NOTAS_TRABAJO = [
    ("trabajando", "Se lesionó trabajando: {m}"),
    ("en el trayecto", "Se lesionó en el trayecto entre su casa y el trabajo: {m}"),
]
MOTIVOS_TRABAJO = [
    ("traumatismo de miembro", "Se cayó de una escalera y le duele mucho la muñeca.", (3, 4)),
    ("herida cortante", "Se cortó el antebrazo con una chapa; sangrado controlado.", (3, 4)),
    ("dolor torácico", "Dolor en el pecho desde hace {n} minutos, después de un golpe con una máquina.", (2, 3)),
]
NO_RESPONDE = ["está somnoliento y no contesta preguntas", "está confuso y no puede dar datos",
               "llegó inconsciente"]
VINCULOS = ["su hija", "su hijo", "su esposa", "su esposo", "su hermana", "su hermano"]
DOCUMENTOS = ["DNI", "DNI", "DNI", "pasaporte", "cédula"]


def _numero_documento(r, tipo):
    if tipo == "pasaporte":
        return "".join(r.choice("ABCDEFGHJKLMNPRSTUVWXYZ") for _ in range(3)) + str(r.randint(100000, 999999))
    n = r.randint(10_000_000, 45_999_999)
    return f"{n:,}".replace(",", ".")


def _afiliado(r, tipo):
    if tipo == "obra_social":
        return f"{r.randint(10, 99)}-{r.randint(100000, 999999)}-{r.randint(0, 9)}"
    return f"{r.randint(100000, 999999)}/{r.randint(0, 9):02d}"


def _cuil(r, documento):
    digitos = documento.replace(".", "") if documento and documento.replace(".", "").isdigit() else \
        str(r.randint(10_000_000, 45_999_999))
    return f"{r.choice(['20', '23', '27'])}-{digitos}-{r.randint(0, 9)}"


def _entidad(r):
    tipo = r.choice(["obra_social", "prepaga"])
    return tipo, r.choice(OBRAS_SOCIALES if tipo == "obra_social" else PREPAGAS)


def _acompanante(r):
    vinculo = r.choice(VINCULOS)
    sexo = "F" if vinculo in ("su hija", "su esposa", "su hermana") else "M"
    return f"{vinculo} {r.choice(NOMBRES_ACOMPANANTE[sexo])}"


def _caso(r, indice, cobertura, circuito, prefijo) -> Caso:
    dos = cobertura == "dos_credenciales"
    cobertura_base = "credencial_activa" if dos else cobertura
    sexo = r.choice("FM")
    nombre = f"{r.choice(NOMBRES[sexo])} {r.choice(APELLIDOS)}"
    trabajo = None
    if cobertura_base.startswith("trabajo"):
        trabajo = "trabajando" if cobertura_base == "trabajo_con_credencial" else "en el trayecto"
        motivo, plantilla, rango = r.choice(MOTIVOS_TRABAJO)
        circuito = "ecg" if motivo == "dolor torácico" else "ninguno"
        cuerpo = plantilla.format(n=r.randint(15, 50))
        nota = dict(NOTAS_TRABAJO)[trabajo].format(m=cuerpo[0].lower() + cuerpo[1:])
    elif circuito == "ninguno":
        motivo, plantilla, rango = r.choice(OTROS_MOTIVOS)
        nota = plantilla.format(n=r.randint(2, 8))
    else:
        motivo, plantillas, rango = MOTIVOS[circuito]
        nota = r.choice(plantillas).format(n=r.randint(15, 50))
    sepsis = {"sepsis_probable": r.choice(["probable", "con signos de shock"]),
              "sepsis_posible": "posible, sin signos de shock"}.get(circuito, "no")

    puede = cobertura_base not in ("acompanante_responde", "sin_nadie")
    if not puede:
        rango = (1, 2)
    nivel = r.randint(*rango)

    tipo_doc = r.choice(DOCUMENTOS) if r.random() < 0.6 else None
    numero_doc = _numero_documento(r, tipo_doc) if tipo_doc else None

    acompanante = None
    if cobertura_base == "acompanante_responde":
        acompanante = _acompanante(r)

    afiliaciones: dict[str, bool] = {}
    credencial = declarada = art = None
    if cobertura_base in ("credencial_activa", "credencial_inactiva", "trabajo_con_credencial"):
        tipo, entidad = _entidad(r)
        credencial = declarada = (tipo, entidad, _afiliado(r, tipo))
        afiliaciones[f"{entidad}|{credencial[2]}"] = cobertura_base != "credencial_inactiva"
    elif cobertura_base in ("declara_activa", "declara_inactiva", "acompanante_responde"):
        tipo, entidad = _entidad(r)
        declarada = (tipo, entidad, _afiliado(r, tipo))
        afiliaciones[f"{entidad}|{declarada[2]}"] = cobertura_base != "declara_inactiva"
    elif cobertura_base == "trabajo_sin_credencial" and r.random() < 0.5:
        tipo, entidad = _entidad(r)
        declarada = (tipo, entidad, _afiliado(r, tipo))
        afiliaciones[f"{entidad}|{declarada[2]}"] = True
    if trabajo:
        art = (r.choice(ARTS), _cuil(r, numero_doc))
        afiliaciones[f"{art[0]}|{art[1]}"] = True

    # El orden de estos sorteos fija los casos que salen de cada semilla: no cambiarlo.
    paciente_id = f"P-{r.randint(1000, 9999)}"
    edad = r.randint(18, 88)
    no_responde = None if puede else r.choice(NO_RESPONDE)
    credenciales = [credencial] if credencial else []
    if dos:
        prepaga = ("prepaga", r.choice(PREPAGAS), _afiliado(r, "prepaga"))
        obra_social = ("obra_social", r.choice(OBRAS_SOCIALES), _afiliado(r, "obra_social"))
        afiliaciones = {f"{prepaga[1]}|{prepaga[2]}": r.random() < 0.75,
                        f"{obra_social[1]}|{obra_social[2]}": True}
        declarada = prepaga
        credenciales = [prepaga, obra_social]
        if int(paciente_id[2:]) % 2:
            credenciales.reverse()
    if acompanante is None and puede and r.random() < 0.4:
        acompanante = _acompanante(r)
    llegada = "en ambulancia" if r.random() < 0.35 else "por sus propios medios"
    return Caso(id=f"{prefijo}-{indice:03d}", paciente_id=paciente_id, nombre=nombre, edad=edad, nivel=nivel,
                motivo=motivo, nota=nota, sepsis=sepsis, llegada=llegada, documento_tipo=tipo_doc,
                documento_numero=numero_doc, credenciales=tuple(credenciales), puede_responder=puede,
                no_responde_porque=no_responde, acompanante=acompanante,
                trabajo=trabajo, declarada=declarada, art=art, afiliaciones=afiliaciones)


def generar(semilla: int, n: int, prefijo: str = "sim") -> list[Caso]:
    r = random.Random(semilla)
    combinaciones = [(r.choice(COBERTURAS), r.choice(CIRCUITOS)) for _ in range(n)]
    return [_caso(r, i + 1, c, k, prefijo) for i, (c, k) in enumerate(combinaciones)]
