# Misión: RAG, MCP y Transformers en el Hospital Arroyo Claro

## La idea

El Hospital Provincial Arroyo Claro (ficticio) quiere un asistente que conteste preguntas de pacientes y familiares: horarios de visita, preparación para estudios, turnos, camas, farmacia. La información está en dos lugares. Las normas y los procedimientos están en documentos que casi no cambian. El estado del día (camas libres, quién está de guardia, qué hay en farmacia) está en una API que cambia todo el tiempo.

Cada grupo tiene que construir ese asistente en tres pasos (un RAG vectorial, un agente con herramientas y un servidor MCP) y medir cada paso con un benchmark. También tiene que resolver dos ejercicios sobre el transformer, que es la arquitectura de los modelos del asistente: una capa de atención en NumPy y un bloque completo calculado a mano.

El hospital es inventado, así que ningún modelo conoce las respuestas de antemano. El asistente solo contesta bien si recupera la información correcta.

**Entrega: viernes 9 de octubre de 2026.**

## Qué hay en esta carpeta

| Ruta | Qué es |
|---|---|
| `datos/corpus/` | 20 documentos del hospital en Markdown: la base de conocimiento de la parte 1 |
| `datos/preguntas_recuperacion_dev.jsonl` | 20 preguntas con la evidencia que el recuperador tiene que traer (parte 1) |
| `datos/preguntas_agente_dev.jsonl` | 12 preguntas con las herramientas esperadas y una respuesta de referencia (partes 2 y 3) |
| `api/servidor.py` | La API del hospital, que cada grupo levanta en su computadora (ver `api/README.md`) |
| `evaluar/evaluar.py` | El evaluador de la cátedra. Todos miden con este script, sin modificarlo |
| `atencion/test_atencion.py` | Los tests de la parte 4 |
| `a_mano/ejercicio.md` | La consigna de la parte 5 |

Las preguntas `dev` son para desarrollar y tunear. La cátedra va a evaluar la entrega con otro conjunto de preguntas, de la misma forma y sobre los mismos documentos, que no se publica. Un sistema tuneado solo para acertar las preguntas `dev` va a rendir peor en el conjunto de test.

## Modelos

Todo lo que usa un LLM pasa por OpenRouter, como en la misión de prompting. Tienen que usar los siguientes modelos:

| Uso | Modelo | Precio por millón de tokens (entrada / salida) |
|---|---|---|
| Agente de las partes 2 y 3 | `deepseek/deepseek-v4-flash-0731` | USD 0,04 / 0,64 |
| Juez del evaluador (lo llama `evaluar.py`) | `google/gemini-3.7-flash` | USD 0,75 / 3,75 |

(Precios verificados en la API de OpenRouter el 2026-09-23. Si algún id desaparece del catálogo, reemplácenlo por el equivalente vigente del mismo proveedor y anótenlo en el informe.)

Cada evaluación con juez cuesta centavos y se paga con la cuenta del grupo. Conviene correr el evaluador cuando haya un cambio que valga la pena medir.

## Parte 1: RAG vectorial (25 puntos)

Construyan un recuperador sobre `datos/corpus/` que corte los documentos en fragmentos, calcule un embedding por fragmento con un **transformer encoder** y, para cada pregunta, devuelva los fragmentos más parecidos.

**Contrato:**

```bash
python3 recuperar.py --preguntas datos/preguntas_recuperacion_dev.jsonl --salida resultados.jsonl
```

`resultados.jsonl` tiene una línea por pregunta: `{"id": "R01", "fragmentos": ["texto", "texto", ...]}`, en orden de relevancia. La configuración ganadora tiene que quedar fija en el código o en un archivo de configuración, porque la cátedra va a correr este comando sobre las preguntas de test.

**La métrica: Context Relevance.** Cada pregunta trae una o más frases de evidencia, textuales del corpus. El evaluador mide:

- *recall*: qué parte de la evidencia aparece en los fragmentos devueltos;
- *precision*: qué parte de los fragmentos devueltos contiene evidencia;
- *context_relevance*: la media armónica de las dos, promediada sobre las preguntas. **Es el número a maximizar.**

```bash
python3 evaluar/evaluar.py recuperacion --preguntas datos/preguntas_recuperacion_dev.jsonl --resultados resultados.jsonl
```

La métrica castiga los dos extremos: traer pocos fragmentos pierde evidencia, y traer muchos baja la precisión. Un recuperador léxico ingenuo, que devuelve los tres párrafos con más palabras en común, saca 0,35.

**Qué tienen que decidir y medir:**

1. **El encoder.** Comparen al menos tres. Uno es obligatorio y es la línea de base: **BERT sin ajustar para similitud**, `google-bert/bert-base-multilingual-cased` o `dccuchile/bert-base-spanish-wwm-cased`, con el embedding del fragmento calculado como el promedio de los vectores de sus tokens en la última capa. Los otros tienen que ser modelos entrenados para embeddings de oraciones, por ejemplo `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, `intfloat/multilingual-e5-small` o `intfloat/multilingual-e5-base` (este último pide anteponer `query: ` y `passage: `), o `BAAI/bge-m3`. Todos corren en CPU.
2. **El chunking:** tamaño del fragmento y solapamiento, o corte por estructura (secciones del Markdown).
3. **Top-k y similitud mínima:** cuántos fragmentos devolver y a partir de qué coseno descartar.
4. **Opcional:** metadatos (el título del documento y de la sección antepuestos al fragmento) y reranking con un cross-encoder.

**Evidencia obligatoria:** una tabla de experimentos en el informe, con una fila por configuración probada (encoder, chunking, top-k, umbral) y su resultado del evaluador. Cada fila tiene que tener su archivo `.eval.json` en `experimentos/`. Una configuración sin su archivo de evaluación no cuenta.

**Criterio de éxito:** la configuración entregada tiene que ganarle con claridad a la línea de base de BERT, y el informe tiene que explicar con los números por qué ganó el encoder elegido.

## Parte 2: un agente con dos fuentes (30 puntos)

Armen un agente con **tool calling** sobre `deepseek/deepseek-v4-flash-0731` que conteste las preguntas de pacientes con dos fuentes: el recuperador de la parte 1 y la API del hospital (`python3 api/servidor.py`, en `http://localhost:8765`).

El agente tiene que estar hecho con **LangChain**. El modelo se conecta con `ChatOpenAI` de `langchain-openai`, apuntando a OpenRouter (`base_url="https://openrouter.ai/api/v1"`), y cada herramienta es una tool de LangChain.

Las herramientas tienen que llevar estos nombres, porque el evaluador los usa para verificar si el agente llamó a las que correspondían:

| Herramienta | Qué hace |
|---|---|
| `buscar_documentos(consulta)` | Llama al recuperador de la parte 1 |
| `consultar_camas(sector)` | `GET /camas` |
| `consultar_guardia(especialidad)` | `GET /guardia` |
| `consultar_turnos(especialidad)` | `GET /turnos` |
| `consultar_farmacia(medicamento)` | `GET /farmacia` |
| `consultar_espera()` | `GET /espera` |

Las preguntas son de tres tipos: las que se responden con los documentos, las que se responden con la API, y las que necesitan las dos (por ejemplo, si hay camas en pediatría y si los padres se pueden quedar). Escriban con cuidado la descripción de cada herramienta, porque el modelo decide cuál llamar leyendo esas descripciones.

**Contrato:**

```bash
python3 agente.py --preguntas datos/preguntas_agente_dev.jsonl --salida respuestas.jsonl
```

`respuestas.jsonl`: `{"id": "A01", "respuesta": "...", "contextos": ["...", ...], "herramientas": ["buscar_documentos", ...]}`. En `contextos` tiene que ir todo lo que el agente recibió de sus herramientas, como texto (fragmentos y JSON de la API).

**Las métricas:**

```bash
export OPENROUTER_API_KEY=...
python3 evaluar/evaluar.py agente --preguntas datos/preguntas_agente_dev.jsonl --respuestas respuestas.jsonl
```

El evaluador puntúa de 1 a 5, con un modelo juez y un prompt fijos:

- **Context Relevance:** los contextos traen lo necesario, sin ruido de más.
- **Answer Faithfulness:** cada afirmación de la respuesta está respaldada por los contextos. Un dato inventado baja este número aunque sea correcto.
- **Answer Relevance:** la respuesta contesta lo que se preguntó, completa.

Sin juez, el evaluador también calcula el **ruteo**, que es la proporción de herramientas esperadas que el agente usó.

**Evidencia obligatoria:** un log `.md` por corrida del benchmark, con cada pregunta, las llamadas a herramientas con sus argumentos y resultados, la respuesta y el usage de cada llamada al modelo (tokens y costo). **Sin logs, esta parte vale cero:** no hay forma de verificar qué hizo el agente.

**Criterio de éxito:** ruteo cercano a 1 y las tres métricas por encima de 4 en el conjunto `dev`, con los logs que lo respaldan.

## Parte 3: las mismas herramientas como servidor MCP (15 puntos)

Muevan las seis herramientas a un **servidor MCP** (`servidor_mcp.py`, transporte stdio, con el SDK oficial `mcp` de Python) y armen un agente cliente que las descubra con `tools/list` y las llame con `tools/call`, con el mismo modelo de la parte 2.

```bash
python3 agente_mcp.py --preguntas datos/preguntas_agente_dev.jsonl --salida respuestas_mcp.jsonl
```

El agente cliente también tiene que estar hecho con LangChain. Las herramientas del servidor se cargan como tools de LangChain con `langchain-mcp-adapters`.

Las herramientas tienen que quedar en un solo lugar: `agente_mcp.py` no puede tener código propio para consultar la API ni el recuperador, y tiene que obtener todo del servidor.

Para comprobar que el servidor funciona con cualquier cliente MCP, conéctenlo también al **MCP Inspector** (`npx @modelcontextprotocol/inspector python3 servidor_mcp.py`), que no usa ningún LLM, y llamen desde ahí a cada una de las seis herramientas. Guarden capturas de pantalla en `experimentos/inspector/`.

**Criterio de éxito:** la corrida del benchmark con el agente MCP, con su log y su evaluación, y una tabla que compare sus cuatro métricas y su costo con los de la parte 2. Si los números cambian, el informe tiene que explicar por qué, a partir de los logs.

## Parte 4: una capa de atención en NumPy (15 puntos)

Escriban `atencion.py`, solo con NumPy, con las funciones que describe `atencion/test_atencion.py`: `softmax`, `atencion`, `autoatencion` (con máscara causal opcional), `multicabeza` y `layer_norm`. Los valores de referencia son los del ejemplo de la clase ("the cat sat", d = 4).

```bash
python3 atencion/test_atencion.py atencion.py
```

**Criterio de éxito:** los 14 tests en verde, con el archivo de tests tal cual lo entregó la cátedra.

## Parte 5: un bloque de transformer a mano (15 puntos)

La consigna completa está en `a_mano/ejercicio.md`: tienen que pasar las frases "El banco aguanta" y "El banco presta" por un bloque completo, con y sin máscara, en papel. **En cada operación tienen que escribir la razón y la utilidad de esa operación**, y en la nota esa justificación va a pesar más que la cuenta. Hay que entregar las hojas escaneadas y las respuestas a las cinco preguntas del final.

La parte 4 sirve para verificar las cuentas de la parte 5, pero las hojas tienen que mostrar el cálculo a mano.

Antes de hacer las cuentas, miren [Attention in transformers, step-by-step](https://www.youtube.com/watch?v=eMlx5fFNoYc) (3Blue1Brown, Deep Learning Chapter 6).

## Antes de empezar

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 api/servidor.py &          # la API del hospital, en otra terminal
```

Trabajen con su IA para programar de preferencia (Claude Code, Codex, Copilot, Antigravity), con la forma de trabajo de la clase 2: CLAUDE.md, SPEC.md, TDD e historia de commits limpia. Esa forma de trabajo aplica al código de las partes 1 a 4. La parte 5 se resuelve a mano, sin IA.

## La entrega

La entrega se hace **pusheando al repo de GitHub del grupo**, a más tardar el viernes 9 de octubre de 2026. El repo tiene que contener:

- `recuperar.py`, `agente.py`, `servidor_mcp.py`, `agente_mcp.py` y `atencion.py`, corriendo con los comandos de este enunciado.
- `experimentos/` con la evaluación de cada configuración de la parte 1.
- Los `respuestas*.jsonl` y sus `.eval.json` de las partes 2 y 3, con los logs `.md` de cada corrida, y las capturas del MCP Inspector.
- `test_atencion.py` tal cual se entregó, en verde contra su `atencion.py`.
- `a_mano/` con las hojas escaneadas de la parte 5.
- **El informe** (`INFORME.md`): la tabla de experimentos y la elección de la parte 1, los resultados de la parte 2 con un análisis de las preguntas donde el agente falló, la comparación entre el agente de la parte 2 y el agente MCP de la parte 3, y el costo total de la misión en OpenRouter, contrastado con el dashboard de actividad.

No modifiquen `evaluar/evaluar.py`, `api/`, `datos/` ni `atencion/test_atencion.py`: la cátedra va a correr sus propias copias.
