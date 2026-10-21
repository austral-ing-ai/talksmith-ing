# Kit del TP final: la ficha de admisión de guardia

El enunciado (qué hay que hacer, qué se entrega y cómo se corrige) está en [mission.md](mission.md), y el video que lo presenta en dos partes: [Parte 1](https://www.loom.com/share/2c56572757124aaf8e2a1e1398efe27d) y [Parte 2](https://www.loom.com/share/12f6cb81c76440cd8a86563dcc02b2f2). Esto explica qué trae el kit y cómo se usa.

## Qué trae

| Carpeta | Contenido |
|---|---|
| `normas/original/` | 20 secciones de las normas del hospital, una por archivo, y `parametros.yaml` con los valores |
| `normas/b/`, `normas/c/` | Las mismas normas con otros números, como hará el test de la cátedra |
| `practica/` | 50 casos de práctica (`casos.jsonl`) y la ficha esperada de cada uno con cada versión de las normas (`esperadas-<versión>.jsonl`) |
| `historial/historial.csv` | 2.000 admisiones pasadas, sin marcar |
| `rag/consultas_dev.jsonl` | Consultas con la evidencia esperada, para evaluar el buscador |
| `admision/` | El entorno, el comparador, el generador de casos, el agente de ejemplo, el programa que corre los casos y la evaluación del buscador |

Las normas citan a veces disposiciones generales (`NOR-GEN`) que no están entre los archivos. No hacen falta para
completar la ficha.

## Instalarlo

`admision/` es un paquete de Python que usa solo la biblioteca estándar y pyyaml.

- Para trabajar desde esta carpeta: `uv sync`, y los comandos de abajo se corren desde acá.
- Para usarlo desde el repositorio del grupo, agréguenlo a su entorno con la ruta a esta carpeta:
  `uv add <ruta a esta carpeta>` (o `pip install <ruta a esta carpeta>`). Así `import admision` funciona desde su código, y los mismos
  comandos corren desde su repositorio, con las rutas al kit.

No hace falta copiar `admision/` adentro del repositorio. Si lo copian, la cátedra lo reemplaza por su propia copia al
correr la entrega.

## El contrato de la entrega

El repositorio del grupo tiene un archivo de Python, por ejemplo `entrega.py`, con dos funciones:

```python
def construir_buscador(ruta_normas):   # arma el buscador con las normas de esa carpeta
    ...
def construir_agente():                # carga el modelo una sola vez
    ...
```

- **El buscador** tiene `recuperar(consulta, k)`, que devuelve una lista de objetos con atributo `texto` (o strings),
  de más a menos relevante. Si define `k_entorno`, esa es la cantidad que devuelve la herramienta `buscar_normativa`;
  si no, 2. En el test, los números de las normas cambian, así que el buscador se arma siempre con la carpeta que
  recibe (es una copia de las normas en una carpeta aparte). Si el buscador falla en una búsqueda, esa llamada vuelve
  como error (`Error: el buscador falló: <tipo de error>.`) y el caso sigue.
- **El agente** tiene `jugar_lote(entornos)`. Cada elemento de `entornos` es un caso, y tiene solo dos cosas: el id
  del paciente (`paciente_id`) y `paso(herramienta, argumentos)`, que devuelve la observación y si el caso terminó. El
  agente juega cada caso llamando a `paso` hasta `registrar_decision` y devuelve, por caso, la conversación completa
  con el modelo: cada mensaje que entró y cada uno que salió, en el mismo orden que `entornos`.
- **Tope de llamadas:** cada caso admite hasta 40 llamadas a herramientas. Si llega a 40 sin registrar la ficha, el
  caso termina sin ficha. Una llamada a un caso terminado devuelve `El caso ya terminó.` y no cuenta.
- **Fijos:** los nombres y argumentos de las cinco herramientas y los 8 campos de la ficha (ver
  `admision/ejemplo.py`). `registrar_decision` acepta además `fundamentos`, la lista de secciones de las normas que
  justifican la ficha: es optativo y no se corrige.
- **Libres:** el mensaje de sistema, el formato de los mensajes al modelo, la cantidad de búsquedas y la estrategia.
- En operación, el agente no llama a ningún servicio externo.

`admision/ejemplo.py` es el agente de la referencia de la cátedra, con su mensaje de sistema. Pueden usarlo o
reemplazarlo entero.

## Correr la práctica

```bash
uv run python -m admision.correr practica --entrega entrega.py --casos practica/casos.jsonl \
    --esperadas practica/esperadas-original.jsonl --normas normas/original --salida corridas/original
```

Trabaja en dos fases, que también se pueden correr por separado:

1. **Jugar** (`python -m admision.correr jugar --entrega ... --casos ... --normas ... --salida ...`): arma el buscador
   y el agente y juega los casos, sin mirar las fichas esperadas. Deja en `--salida` las trazas (`trazas.jsonl`: por
   caso, la conversación completa, cada llamada a herramienta con lo que devolvió, y la ficha) y los tiempos
   (`tiempos.json`).
2. **Puntuar** (`python -m admision.correr puntuar --trazas .../trazas.jsonl --esperadas ... --salida ...`): compara
   cada ficha con la esperada. Deja el resultado caso por caso (`resultados.jsonl`) y el resumen (`resumen.json`).

`jugar` no arranca si encuentra un archivo `esperadas-*.jsonl` en la carpeta desde la que se corre, en la de los casos,
en la de las normas o en alguna de las tres carpetas de arriba de la de las normas. Como `practica/` tiene los casos y
las esperadas juntos, para correr `jugar` solo, copien `practica/casos.jsonl` a otra carpeta. `practica` lo hace por su
cuenta: copia los casos y las normas a una carpeta temporal y juega ahí.

Un caso está resuelto si pasan los 9 controles: los 8 campos de la ficha y la verificación de la afiliación. Es el
formato que se exige para cada número que se reporta.

**Tiempos y contexto.** El tiempo lo mide `admision.correr`, no el agente: cuánto tarda `construir_agente`, cuánto
tarda `jugar_lote` entero y, por caso, en qué segundo hizo su última llamada (los casos de un lote corren a la vez).
Los caracteres de contexto (lo que se le pasó al modelo en todo el caso) salen de la conversación que devuelve el
agente, así que esa conversación tiene que ser completa.

Si `jugar_lote` se cae a mitad de camino, las trazas igual se escriben con lo que llegó a pasar en cada caso, y el
error queda anotado en `tiempos.json` y en el resumen.

## Cómo corre la cátedra su entrega

- Cada entrega corre en un proceso propio, en una GPU A100 de 40 GB (no la de 80 GB), sin tiempo máximo.
- La cátedra instala las dependencias fijadas en el repositorio del grupo y su propia copia de `admision` (si el
  repositorio trae una, la reemplaza).
- El modelo se baja del repositorio de Hugging Face del grupo. Por eso `construir_agente()` lee el id del repositorio
  y la revisión (el commit o la etiqueta exacta del modelo) desde el código o la configuración del grupo. La cátedra
  pone en el entorno `HF_TOKEN`, la clave que le da acceso a ese repositorio privado.
- Las dos fases corren por separado: primero `jugar`, en una máquina que tiene solo los casos y las normas del test
  secreto, y después `puntuar`, en otra, con las fichas esperadas. El agente nunca ve las fichas esperadas.

## Evaluar el buscador

```bash
uv run python -m admision.evaluar_rag --entrega entrega.py --normas normas/original --consultas rag/consultas_dev.jsonl
```

Mide si el buscador trae la evidencia (recall), qué parte de lo que trae sirve (precisión) y cuántos tokens trae, con lo
que el buscador devuelve en el entorno (`k_entorno`) y con presupuestos fijos de 256, 512 y 1024 tokens. Es una
evaluación obligatoria antes de empezar el agente, y se documenta. No es la nota: el buscador cuenta por lo que rinde
el agente con él.

## Generar casos

```python
from admision.generador import generar
casos = generar(semilla=42, n=1000)
```

Son casos sin la respuesta. La ficha correcta hay que deducirla de las normas y del historial.

## El historial

Una fila por admisión pasada, como la exportación del sistema de admisión:

- **Identificación:** id de la fila, fecha y operador.
- **Lo que decía el triage:** edad, nivel, motivo, nota de enfermería, sospecha de sepsis, llegada, documento,
  credenciales, si podía responder, acompañante y si se lesionó trabajando.
- **Lo que averiguó el operador:** cobertura declarada, ART declarada y la entidad y el número que verificó, con la
  respuesta de la entidad.
- **La ficha que completó:** los 8 campos.

No está marcado. Hay filas correctas, errores y ruido, y el hospital tiene costumbres que no están escritas en las
normas.

**Qué se entrega de la clasificación:**

- `historial_clasificado.csv`, con dos columnas, `id,tipo`, y una fila por cada fila del historial (las 2.000).
  `tipo` es uno de estos tres valores:
  - `correcta`: la fila sigue las normas escritas y hace lo que hacen casi todos los operadores;
  - `error`: la fila viola una norma escrita;
  - `ruido`: la fila hace algo que las normas no cubren, distinto de lo que hacen casi todos los operadores en esa
    situación (o sea, se aparta de una costumbre).
- `costumbres.md`, en texto libre: cada costumbre que descubrieron, explicada, con los ids de las filas que la
  respaldan.
