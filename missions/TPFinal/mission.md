# Misión: el agente de admisión de guardia
## Trabajo final — Inteligencia Artificial Generativa
**Universidad Austral · Ingeniería de Software · Noviembre 2026**

---

| | |
|---|---|
| **Proyecto** | El agente de admisión de guardia — completa la ficha de admisión de cada paciente que ingresa por la guardia |
| **Materia** | Inteligencia Artificial Generativa (AI Gen) |
| **Entrega** | Repositorio de GitHub + modelo en Hugging Face y corridas en W&B + presentación en Loom |
| **Fecha de entrega** | **Viernes 20 de noviembre de 2026** |
| **Kit** | [`missions/TPFinal/`](.) — normas, casos de práctica, historial y el paquete `admision`. Cómo instalarlo y correrlo está en su [README](README.md) |
| **Envío** | Mail a Paulo Veiga y Marco, con todos los integrantes del grupo en copia |
| **Video del enunciado** | [Parte 1](https://www.loom.com/share/2c56572757124aaf8e2a1e1398efe27d) · [Parte 2](https://www.loom.com/share/12f6cb81c76440cd8a86563dcc02b2f2) (Loom) |

> **Video de presentación del TP:** [Parte 1](https://www.loom.com/share/2c56572757124aaf8e2a1e1398efe27d) y [Parte 2](https://www.loom.com/share/12f6cb81c76440cd8a86563dcc02b2f2). Mírenlo antes de leer el resto.

> **Este enunciado dice qué hacer. Cómo correrlo está en el [README del kit](README.md)**, en esta misma carpeta: cómo [instalarlo](README.md#instalarlo), el [contrato de `entrega.py`](README.md#el-contrato-de-la-entrega), cómo [correr los casos de práctica](README.md#correr-la-práctica), cómo [corre la cátedra su entrega](README.md#cómo-corre-la-cátedra-su-entrega) y cómo [evaluar el buscador](README.md#evaluar-el-buscador). Léanlo antes de escribir código.

---

## Tabla de contenidos

1. [La idea](#la-idea)
2. [La ficha](#la-ficha)
3. [Qué hay en esta carpeta](#qué-hay-en-esta-carpeta)
4. [Modelo y cómputo](#modelo-y-cómputo)
5. [Parte 1: curado e ingeniería de datos](#parte-1-curado-e-ingeniería-de-datos)
6. [Parte 2: buscador propio (RAG)](#parte-2-buscador-propio-rag)
7. [Parte 3: optimización de prompt, antes de entrenar](#parte-3-optimización-de-prompt-antes-de-entrenar)
8. [Parte 4: entrenamiento](#parte-4-entrenamiento)
9. [Parte 5: recursos y producción](#parte-5-recursos-y-producción)
10. [Auditabilidad](#auditabilidad)
11. [Antes de empezar](#antes-de-empezar)
12. [La entrega](#la-entrega)
   - [1. Repositorio de GitHub](#1-repositorio-de-github)
   - [2. Modelo y corridas](#2-modelo-y-corridas)
   - [3. Presentación en Loom](#3-presentación-en-loom)
   - [Cómo se envía](#cómo-se-envía)
13. [Cómo se corrige](#cómo-se-corrige)

---

## La idea

El Hospital General de Prueba (ficticio) quiere un agente que complete la ficha de admisión de cada paciente que ingresa por la guardia. El agente no toma decisiones clínicas: lee la nota de triage (la nota de enfermería que clasifica la urgencia del paciente), pregunta lo que falta, verifica la cobertura, consulta las normas del hospital y registra la ficha.

Este hospital tiene tres particularidades, y por ellas un modelo que responde con lo que ya sabe se equivoca:

- **Sus normas tienen reglas que contradicen lo habitual.** Hay que leerlas, y en el test de la cátedra los números de las normas cambian.
- **Tiene costumbres que no están escritas en ninguna norma.** Se descubren mirando los datos, no las normas.
- **El historial de admisiones pasadas no está limpio.** Hay operadores que se equivocan y otros que hacen las cosas a su manera.

Cada grupo construye el agente completo sobre un modelo libre chico que entrena el propio grupo: cura el historial y lo convierte en datos de entrenamiento, arma su buscador sobre las normas, optimiza el prompt, entrena el modelo y lo deja listo para producción. Lo que más pesa en la nota es el modelo final: cuántos casos de un test secreto resuelve y cuánto cuesta y tarda cada caso.

La entrega es el **viernes 20 de noviembre de 2026**. El tamaño de los grupos lo comunica la cátedra.

## La ficha

La ficha tiene 8 campos:

- el tipo de registro: si el registro es definitivo (con documento) o provisorio;
- el número de documento;
- si el paciente pasa al box (el consultorio de la guardia) antes de registrarlo;
- el circuito tiempo-dependiente que corresponde, o sea si hay que activar un aviso urgente (electrocardiograma por dolor de pecho, código ACV, código sepsis);
- el plazo de ese circuito, en minutos desde el ingreso;
- la cobertura del paciente;
- la entidad a notificar: la obra social, prepaga o ART (la aseguradora de riesgos del trabajo del empleador) a la que se avisa de la atención;
- si se avisa al voluntariado del hospital.

Además se controla que el agente haya verificado la afiliación con la entidad correcta. Son 9 controles: los 8 campos más esa verificación. **Un caso está resuelto si los 9 están bien.**

El agente tiene cinco herramientas: `leer_triage`, `preguntar` (al paciente o a su acompañante), `verificar_afiliacion`, `buscar_normativa` (que usa el buscador del grupo) y `registrar_decision`.

## Qué hay en esta carpeta

El kit está en [`missions/TPFinal/`](.), la misma carpeta que este enunciado.

| Ruta | Qué es |
|---|---|
| [`README.md`](README.md) | **El manual del kit:** cómo se instala, el contrato de `entrega.py` (lo que la cátedra llama para correr su agente), los comandos para correr la práctica y evaluar el buscador, y cómo corre la cátedra la entrega |
| `normas/original/` | Las 20 secciones de las normas del hospital, una por archivo, y `parametros.yaml` con sus valores |
| `normas/b/`, `normas/c/` | Las mismas normas con otros números, como va a hacer el test de la cátedra |
| `practica/` | 50 casos de práctica y la ficha esperada de cada uno con cada versión de las normas |
| `historial/historial.csv` | 2.000 admisiones pasadas, sin marcar |
| `rag/consultas_dev.jsonl` | 60 consultas con la evidencia que el buscador tiene que traer |
| `admision/` | Un paquete de Python con el entorno (el simulador de la guardia), el comparador de fichas, un generador de casos sin respuesta, el agente de ejemplo de la cátedra con su mensaje de sistema, el programa que corre los casos (`admision.correr`) y la evaluación del buscador (`admision.evaluar_rag`) |

Los casos de práctica son para desarrollar. La cátedra evalúa la entrega con un test secreto, con otros casos y otros números en las normas. Un agente que aprendió de memoria los números de las normas de práctica falla en el test.

No modifiquen `admision/`: la cátedra corre la entrega con su propia copia.

## Modelo y cómputo

- **Modelo:** Gemma 4 E4B (`google/gemma-4-E4B-it` en Hugging Face, el que vimos en clase) o cualquier otro modelo libre y entrenable de **a lo sumo 8.000 millones de parámetros**, que en bf16 ocupan 16 GB.
- **Cómputo:** usen [Modal](https://modal.com). Cada integrante del grupo tiene **30 USD de crédito gratis por mes** con su cuenta en el plan Starter. Una A100 de 40 GB cuesta unos 2,10 USD por hora, así que alcanza para unas 14 horas de GPU por persona por mes: planifiquen las corridas largas. Hugging Face queda para guardar los modelos. Guarden puntos de control durante el entrenamiento, para retomar si algo se corta y para documentar cada corrida.
- **GPU:** una A100 de 40 GB, **no la de 80 GB**, tanto para su entrenamiento como para la corrida de la cátedra. El entrenamiento, el agente y el buscador tienen que entrar y funcionar ahí.
- **No hay tiempo máximo**, ni para su entrenamiento ni para la corrida de la cátedra. Entrenar mucho tiempo sin sobreajustar se ve como una ventaja. Igual, lo que cuesta y tarda cada caso del test cuenta en la nota.
- **En operación, el agente no llama a ningún servicio externo.** Los modelos grandes, también los pagos, se pueden usar para programar y para generar datos, no dentro del agente.
- **Las dependencias van fijadas en el repositorio**, con sus versiones exactas, porque la cátedra corre el agente en su propia cuenta.

## Parte 1: curado e ingeniería de datos

1. **Clasifiquen cada fila del historial** como correcta, error o ruido:
   - **error**: la fila viola una norma escrita;
   - **ruido**: la fila hace algo que las normas no cubren, distinto de lo que hacen casi todos los operadores en esa situación (o sea, se aparta de una costumbre);
   - **correcta**: todas las demás.
2. **Describan las costumbres que descubrieron**, con las filas que las respaldan.
3. **Conviertan las filas que sirven en conversaciones de entrenamiento** del agente.
4. Pueden **generar conversaciones sintéticas**, inventadas por un programa propio o por cualquier modelo, también uno pago. Por ejemplo, para tener más casos de los que más cuestan.

## Parte 2: buscador propio (RAG)

Construyan su propio RAG sobre las normas. **El RAG es complementario al entrenamiento:** el entrenamiento le enseña al modelo el oficio (cómo se completa la ficha, qué preguntar, las costumbres del hospital), y el RAG le trae en cada caso el conocimiento que cambia. Las normas cambian: en el test de la cátedra tienen otros números. Por eso lo que cambia va en el buscador, no en los pesos: un modelo que aprendió de memoria los números de las normas de práctica falla en el test, y uno que los busca no.

Las normas incluyen secciones de otras áreas del hospital que no deciden la ficha pero se le parecen, así que el buscador tiene que elegir bien.

- **Lo que cuenta es cuánto le sirve al agente**: los casos que resuelve y lo que cuesta cada caso con ese buscador.
- **Antes de empezar el agente**, evalúen el buscador por separado y documenten el resultado:

  ```bash
  uv run python -m admision.evaluar_rag --entrega entrega.py --normas normas/original --consultas rag/consultas_dev.jsonl
  ```

  Mide tres cosas: qué parte de la evidencia necesaria trae (recall de evidencia), qué parte de lo que trae sirve (precisión) y cuántos tokens trae (la evaluación cuenta 4 caracteres por token). Esta evaluación es obligatoria, pero no es la nota.
- **Referencia:** el buscador de la cátedra es BM25, con una sección entera de las normas por fragmento. Con las consultas de esta carpeta, las normas originales y las dos secciones que trae `buscar_normativa`, da recall de evidencia 0,875, precisión 0,492, 580 tokens por consulta y 51 de 60 consultas con toda su evidencia.
- Pueden ajustar el buscador mirando cómo rinde el agente, aunque eso empeore la evaluación aparte.
- Lo que trae el buscador ocupa contexto. En la referencia de la cátedra, más de la mitad de cada conversación es texto de las búsquedas. Traer menos permite procesar más casos a la vez y entrenar con menos tokens.

## Parte 3: optimización de prompt, antes de entrenar

Es obligatoria y va **antes** del entrenamiento.

- Optimicen el mensaje de sistema y el formato de los mensajes al modelo, con el modelo sin entrenar. Sugerimos DSPy, por ejemplo con su optimizador GEPA.
- Valoramos la calidad del resultado y también el largo del prompt. El prompt se repite en cada llamada al modelo: cuesta cómputo y ocupa VRAM al usar el modelo y al entrenarlo. En la referencia de la cátedra, el mensaje de sistema es la quinta parte de cada conversación.
- **Nunca optimicen sobre el test.** El test solo sirve para evaluar.
- Después entrenen con el prompt optimizado.

## Parte 4: entrenamiento

Cualquier estrategia de post-entrenamiento. Por ejemplo:

- fine-tuning supervisado (SFT), con las conversaciones que armaron en la Parte 1;
- DPO, con pares de respuestas al mismo paso del caso, una buena y una mala;
- aprendizaje por refuerzo, con los 9 controles de la ficha como puntaje.

## Parte 5: recursos y producción

Antes y después de llegar a un resultado satisfactorio:

- el tiempo de entrenamiento, el aprovechamiento de la VRAM y el costo de punta a punta del desarrollo y del mantenimiento;
- el paralelismo, o sea cuántos casos procesan a la vez al entrenar y al evaluar, que valoramos;
- cuántos casos simultáneos tolera el sistema en producción, la proyección de consumo y cómo lo escalarían si sube la demanda;
- trabajos futuros para mejorarlo en todo sentido.

## Auditabilidad

**No aceptamos entregas, números ni afirmaciones que no sean 100% auditables y reproducibles, ni entregas que obliguen a volver a entrenar para verificarlas.**

- **Cada entrenamiento** deja el archivo exacto de conversaciones que usó, la configuración, la semilla, la corrida en Weights & Biases (W&B) y cada punto de control en Hugging Face, con su versión.
- **Cada número reportado** deja todas las conversaciones de la evaluación, con cada mensaje que entró al modelo y cada uno que salió, el resultado caso por caso y qué punto de control y qué prompt se usaron. `admision.correr` ya lo escribe así.
- **Todo archivo generado** (datos, conversaciones, resultados) sale de un script del repositorio, y el README o el informe dice qué script genera cada uno.
- **Se documenta cada pasada del desarrollo**, no solo la final, incluidos los experimentos que no funcionaron.
- **Reproducible** quiere decir que, con el mismo código, los mismos datos, la misma semilla y el mismo punto de control, la evaluación da el mismo resultado. Si hay una diferencia mínima (evaluar en lote en GPU puede mover algún caso), se documenta.
- **Cada commit es un cambio acotado con un solo propósito**: una mejora, la corrección de un error, un experimento o documentación. El mensaje dice qué cambia y por qué. Valoramos mucho que los commits se repartan de manera pareja entre los integrantes.

## Antes de empezar

```bash
cd missions/TPFinal
uv sync
```

Lean el [README del kit](README.md) antes de escribir código. Ahí está todo lo que hace falta para correrlo:

- cómo [usar el kit desde el repositorio del grupo](README.md#instalarlo), sin copiar `admision/`;
- el [contrato de la entrega](README.md#el-contrato-de-la-entrega): un `entrega.py` con `construir_buscador` y `construir_agente`, y qué tiene que devolver cada uno;
- cómo [correr los casos de práctica](README.md#correr-la-práctica) y qué deja cada corrida;
- cómo [corre la cátedra su entrega](README.md#cómo-corre-la-cátedra-su-entrega) con el test secreto;
- cómo [evaluar el buscador](README.md#evaluar-el-buscador) y [generar casos](README.md#generar-casos).

El kit no trae un `entrega.py` listo: el primer paso es armar uno mínimo, con un buscador simple, el agente de ejemplo (`admision/ejemplo.py`) y el modelo sin entrenar, y correr con él los 50 casos de práctica como indica el README. Esa es su línea de base.

Trabajen con la herramienta de programación con IA que prefieran (Claude Code, Codex, Gemini CLI, Cursor u otra).

## La entrega

Se entregan tres cosas. Entre las tres tienen que alcanzar para que la cátedra corra su agente con el test secreto **sin volver a entrenar** y pueda auditar cada número que reportan.

| Qué | Dónde | Para qué la usa la cátedra |
|---|---|---|
| **Repositorio** | GitHub privado, con acceso para la cátedra | Corre su `entrega.py` con el test secreto y corrige el historial clasificado, las costumbres y el informe |
| **Modelo y corridas** | Repositorio privado de Hugging Face y proyecto de W&B, los dos compartidos con la cátedra | Carga el punto de control final y revisa cada entrenamiento |
| **Presentación** | Video en Loom, de 15 a 20 minutos | Escucha cómo llegaron al modelo final y por qué tomaron cada decisión |

### 1. Repositorio de GitHub

Todo el código del grupo. La estructura la decide el grupo, pero tienen que estar estos archivos:

| Archivo | Qué tiene |
|---|---|
| `entrega.py` | `construir_buscador` y `construir_agente`, según el [contrato del README del kit](README.md#el-contrato-de-la-entrega). Es lo único que llama la cátedra: de acá salen el punto de control de Hugging Face, el prompt optimizado y el buscador del grupo. |
| `pyproject.toml` y `uv.lock` | Las dependencias con sus versiones exactas: `uv sync` alcanza para levantar el entorno en la cuenta de la cátedra. |
| `historial_clasificado.csv` | La clasificación de la Parte 1: dos columnas, `id,tipo`, y una fila por cada una de las 2.000 filas del historial; `tipo` es `correcta`, `error` o `ruido`. La cátedra la compara con la clasificación verdadera. |
| `costumbres.md` | Cada costumbre que descubrieron, explicada, con los ids de las filas que la respaldan. La cátedra controla si son las costumbres verdaderas. |
| `INFORME.md` | El desarrollo completo, parte por parte (ver abajo). |
| `README.md` | Cómo correr todo con lo publicado (ver abajo). |

Más el código de cada parte: el curado, la generación de conversaciones, el buscador, la optimización de prompt, el entrenamiento y la evaluación. No incluyan `admision/` modificado: la cátedra corre con su copia.

#### El informe

Un apartado por parte de la misión, con cada pasada del desarrollo y no solo la final, incluidos los experimentos que no funcionaron:

- **Parte 1, curado:** cómo clasificaron el historial, cuántas filas quedaron de cada tipo, cómo encontraron las costumbres y cuántas conversaciones de entrenamiento armaron, reales y sintéticas.
- **Parte 2, buscador:** el resultado de `admision.evaluar_rag` al lado de la referencia BM25 (recall de evidencia 0,875, precisión 0,492, 580 tokens por consulta, 51 de 60 consultas completas) y cuánto rinde el agente con su buscador.
- **Parte 3, prompt:** con el modelo sin entrenar, los casos resueltos y el largo del prompt en tokens, antes y después de optimizar.
- **Parte 4, entrenamiento:** la estrategia y una tabla de casos resueltos sobre los 50 de práctica, con las normas original, b y c, para el modelo sin entrenar, solo prompt, solo entrenamiento y las dos cosas juntas, al lado de la referencia de la cátedra (12, 15 y 12 sin entrenar; 25, 24 y 25 con fine-tuning supervisado).
- **Parte 5, recursos:** tiempo de entrenamiento, VRAM usada, costo y tiempo por caso en la A100 de 40 GB, casos que procesan a la vez, cuántos casos simultáneos tolera en producción, la proyección de consumo, cómo escalarían y los trabajos futuros.

Cada número del informe dice qué comando, qué punto de control y qué prompt lo producen.

#### El README

Cualquier persona con el repositorio tiene que poder seguirlo línea por línea, **con el punto de control publicado y sin entrenar**:

1. **Entorno:** `uv sync` y un `.env.example` con las variables que hacen falta (por ejemplo, el token de Hugging Face y la clave de W&B), sin valores reales.
2. **Un caso:** el comando de `admision.correr` con su `entrega.py` sobre un caso de práctica, y qué se ve: la conversación, las búsquedas en las normas, la ficha registrada y los 9 controles.
3. **El buscador:** el comando de `admision.evaluar_rag` sobre `rag/consultas_dev.jsonl`.
4. **La evaluación completa:** el comando que corre los 50 casos de práctica con las normas original, b y c y produce la tabla del informe.
5. **De dónde sale cada archivo:** qué script genera `historial_clasificado.csv`, las conversaciones de entrenamiento, el prompt optimizado y cada entrenamiento, con su configuración y su semilla.
6. **Un diagrama** de cómo se conectan el agente, sus cinco herramientas, el buscador y el modelo.

Volver a entrenar se documenta con su comando, pero no puede hacer falta para verificar nada (ver [Auditabilidad](#auditabilidad)).

### 2. Modelo y corridas

- **Hugging Face:** el punto de control final, que es el que carga `entrega.py`, y cada punto de control que aparece en el informe, con su versión. Todos entran y corren en una A100 de 40 GB.
- **W&B:** todas las corridas de entrenamiento, también las que no funcionaron. Cada corrida dice qué archivo de conversaciones, qué configuración, qué semilla y qué punto de control de Hugging Face le corresponden.

### 3. Presentación en Loom

Una presentación grabada en Loom, de **15 a 20 minutos**. El orden sigue al de [cómo se corrige](#cómo-se-corrige): primero el resultado, después cómo llegaron.

| # | Sección | Qué se espera |
|---|---|---|
| 1 | **El modelo final** | Cuántos de los 50 casos de práctica resuelve con cada versión de las normas, cuánto cuesta y tarda cada caso, y cómo se compara con la referencia de la cátedra. |
| 2 | **Demo** | El agente corriendo con las normas b o c, no con las originales, sobre al menos dos casos de práctica: uno que activa un circuito tiempo-dependiente y uno que se decide por una costumbre. Se ven las llamadas a las herramientas, lo que trae el buscador, la ficha y los 9 controles. |
| 3 | **El historial** | Cómo separaron errores de ruido, qué costumbres encontraron, con filas de ejemplo, y cómo armaron las conversaciones de entrenamiento. |
| 4 | **Buscador y prompt** | Cuánta evidencia trae el buscador y cuánto contexto ocupa, y qué ganaron al optimizar el prompt, en casos y en largo. |
| 5 | **Entrenamiento** | La estrategia, las corridas que no funcionaron y por qué, y la comparación entre solo prompt, solo entrenamiento y las dos cosas juntas. |
| 6 | **Recursos y producción** | VRAM, casos que procesan a la vez, cuántos casos simultáneos tolera en producción, costo proyectado y cómo escalarían si sube la demanda. Cierren con los trabajos futuros. |

### Cómo se envía

La entrega se envía **por mail a Paulo Veiga y a Marco**, antes del **viernes 20 de noviembre de 2026**, con **todos los integrantes del grupo en copia**. Un solo mail por grupo:

```text
Para:     Paulo Veiga, Marco Sorondo
CC:       todos los integrantes del grupo
Asunto:   [AI Gen] TP final — Agente de admisión de guardia — Grupo <número>

Integrantes:
- <Nombre y apellido> — <mail> — <usuario de GitHub>
- ...

Repositorio de GitHub:   <link>
Commit entregado:        <hash del commit o tag>
Modelo en Hugging Face:  <link> — versión del punto de control final: <revisión>
Proyecto de W&B:         <link>
Presentación en Loom:    <link>
```

El commit y la versión del punto de control fijan qué se corrige: la cátedra corre exactamente esa versión de `entrega.py` con ese punto de control. Todos los links tienen que estar activos y accesibles al momento de la corrección.

Pueden hacer una **pre-entrega** cuando tengan todo y seguir mejorando hasta la entrega final.

## Cómo se corrige

En orden de importancia:

1. **Lo más importante, lejos: el modelo final en producción.** Cuenta cuántos casos del test secreto resuelve y cuánto cuesta y tarda cada caso. Entre dos modelos que resuelven lo mismo, gana el más barato de correr. El costo del desarrollo pesa poco, porque se paga una sola vez.
2. **Documentación, auditabilidad y explicación** de la entrega final y de todo el proceso de desarrollo.
3. **Curado, creación e ingeniería de datos**, incluido el acierto de la clasificación del historial.
4. **Optimización de recursos**, con sus costos y la proyección a producción.

El buscador cuenta por lo que rinde el agente con él. La evaluación aparte del buscador y la optimización de prompt cuentan como prácticas obligatorias documentadas. `admision.correr` informa, por caso, cuántas búsquedas hizo el agente, cuánto contexto le pasó al modelo y cuánto tardó.

**Referencia de la cátedra.** Se midió sobre los 50 casos de práctica, con las tres versiones de las normas (la original y las dos con los números cambiados), siempre con las normas completas, incluidas las secciones de otras áreas del hospital. Gemma 4 E4B sin entrenar resuelve 12, 15 y 12 casos en cada versión. Con un fine-tuning supervisado simple, resuelve 25, 24 y 25. Ese entrenamiento usó datos perfectos, generados por la cátedra. Ustedes van a entrenar con lo que curen.
