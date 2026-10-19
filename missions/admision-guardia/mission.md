# Misión: el agente de admisión de guardia

## La idea

El Hospital General de Prueba (ficticio) quiere un agente que complete la ficha de admisión de cada paciente que ingresa por la guardia. El agente es un programa que usa un modelo de lenguaje. No toma decisiones clínicas: lee la nota de triage (la nota de enfermería que clasifica la urgencia del paciente), pregunta lo que falta, verifica la cobertura, consulta las normas del hospital y registra la ficha.

Este hospital tiene tres particularidades, y por ellas un modelo que responde con lo que ya sabe se equivoca:

- **Sus normas tienen reglas que contradicen lo habitual.** Hay que leerlas, y en el test de la cátedra los números de las normas cambian.
- **Tiene costumbres que no están escritas en ninguna norma.** Se descubren mirando los datos, no las normas.
- **El historial de admisiones pasadas no está limpio.** Hay operadores que se equivocan y otros que hacen las cosas a su manera.

Cada grupo construye el agente completo sobre un modelo libre chico que entrena el propio grupo: cura el historial y lo convierte en datos de entrenamiento, arma su buscador sobre las normas, optimiza el prompt, entrena el modelo y lo deja listo para producción. Lo que más pesa en la nota es el modelo final: cuántos casos de un test secreto resuelve y cuánto cuesta y tarda cada caso.

Todo el código de la misión tiene que estar escrito en **Python**.

La fecha de entrega y el tamaño de los grupos los comunica la cátedra.

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

| Ruta | Qué es |
|---|---|
| `README.md` | Cómo se instala y se usa lo que hay acá, y el contrato de la entrega: lo que la cátedra va a llamar para correr su agente |
| `normas/original/` | Las 20 secciones de las normas del hospital, una por archivo, y `parametros.yaml` con sus valores |
| `normas/b/`, `normas/c/` | Las mismas normas con otros números, como va a hacer el test de la cátedra |
| `practica/` | 50 casos de práctica y la ficha esperada de cada uno con cada versión de las normas |
| `historial/historial.csv` | 2.000 admisiones pasadas, sin marcar |
| `rag/consultas_dev.jsonl` | 60 consultas con la evidencia que el buscador tiene que traer |
| `admision/` | Un paquete de Python con el entorno (el simulador de la guardia), el comparador de fichas, un generador de casos sin respuesta, el agente de ejemplo de la cátedra con su mensaje de sistema, el programa que corre los casos (`admision.correr`) y la evaluación del buscador (`admision.evaluar_rag`) |

Los casos de práctica son para desarrollar. La cátedra evalúa la entrega con un test secreto, con otros casos y otros números en las normas. Un agente que aprendió de memoria los números de las normas de práctica falla en el test.

No modifiquen `admision/`: la cátedra corre la entrega con su propia copia.

## Modelo y cómputo

- **Modelo:** Gemma 4 E4B (`google/gemma-4-E4B-it` en Hugging Face, el sitio donde se publican modelos; es el que vimos en clase) o cualquier otro modelo libre y entrenable de **a lo sumo 8.000 millones de parámetros**. Los parámetros son los números que se ajustan al entrenar, y el tamaño de un modelo se mide en cantidad de parámetros: 8.000 millones ocupan 16 GB de memoria en bf16, un formato numérico de 16 bits por parámetro.
- **Cómputo:** en Modal o en Hugging Face, servicios en la nube para correr GPU (Hugging Face sirve además para guardar modelos). Guarden puntos de control (copias guardadas del modelo) durante el entrenamiento, para retomar si algo se corta y para documentar cada corrida.
- **GPU:** una A100 de 40 GB, **no la de 80 GB**, tanto para su entrenamiento como para la corrida de la cátedra. El entrenamiento, el agente y el buscador tienen que entrar y funcionar ahí.
- **No hay tiempo máximo**, ni para su entrenamiento ni para la corrida de la cátedra. Entrenar mucho tiempo sin sobreajustar (aprender de memoria los ejemplos de entrenamiento y fallar con casos nuevos) se ve como una ventaja. Igual, lo que cuesta y tarda cada caso del test cuenta en la nota.
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

Construyan su buscador, o sea el programa que le trae al agente los fragmentos de las normas que necesita (esa técnica se llama RAG). Las normas incluyen secciones de otras áreas del hospital que no deciden la ficha pero se le parecen, así que el buscador tiene que elegir bien.

- **Lo que cuenta es cuánto le sirve al agente**: los casos que resuelve y lo que cuesta cada caso con ese buscador.
- **Antes de empezar el agente**, evalúen el buscador por separado y documenten el resultado:

  ```bash
  uv run python -m admision.evaluar_rag --entrega entrega.py --normas normas/original --consultas rag/consultas_dev.jsonl
  ```

  Mide tres cosas: qué parte de la evidencia necesaria trae (recall de evidencia), qué parte de lo que trae sirve (precisión) y cuántos tokens trae (un token es un trozo de texto, más o menos una sílaba; la evaluación cuenta 4 caracteres por token). Esta evaluación es obligatoria, pero no es la nota.
- **Referencia:** el buscador de la cátedra es BM25, un buscador clásico que puntúa cada sección de las normas por las palabras que comparte con la consulta, con una sección entera por fragmento. Con las consultas de esta carpeta, las normas originales y las dos secciones que trae `buscar_normativa`, da recall de evidencia 0,875, precisión 0,492, 580 tokens por consulta y 51 de 60 consultas con toda su evidencia.
- Pueden ajustar el buscador mirando cómo rinde el agente, aunque eso empeore la evaluación aparte.
- Lo que trae el buscador ocupa contexto (el texto que el modelo puede leer a la vez). En la referencia de la cátedra, más de la mitad de cada conversación es texto de las búsquedas. Traer menos permite procesar más casos a la vez y entrenar con menos tokens.

## Parte 3: optimización de prompt, antes de entrenar

Es obligatoria y va **antes** del entrenamiento.

- Optimicen el mensaje de sistema (el texto fijo de instrucciones que recibe el modelo en cada llamada) y el formato de los mensajes al modelo, con el modelo sin entrenar. Sugerimos DSPy, una librería que optimiza prompts de forma automática, por ejemplo con su optimizador GEPA.
- Valoramos la calidad del resultado y también el largo del prompt. El prompt se repite en cada llamada al modelo: cuesta cómputo y ocupa VRAM (la memoria de la GPU) al usar el modelo y al entrenarlo. En la referencia de la cátedra, el mensaje de sistema es la quinta parte de cada conversación.
- **Nunca optimicen sobre el test.** El test solo sirve para evaluar.
- Después entrenen con el prompt optimizado.

## Parte 4: entrenamiento

Cualquier estrategia de post-entrenamiento, o sea cualquier entrenamiento posterior al preentrenamiento original del modelo. Por ejemplo:

- fine-tuning (seguir entrenando un modelo ya hecho con ejemplos propios), como el fine-tuning supervisado (SFT): entrenar con ejemplos de conversaciones correctas;
- DPO: entrenar con pares de respuestas a la misma pregunta, una buena y una mala, para que el modelo prefiera la buena;
- aprendizaje por refuerzo: el modelo prueba, recibe un puntaje por lo que hizo y aprende a subirlo.

## Parte 5: recursos y producción

Antes y después de llegar a un resultado satisfactorio:

- el tiempo de entrenamiento, el aprovechamiento de la VRAM y el costo de punta a punta del desarrollo y del mantenimiento;
- el paralelismo, o sea cuántos casos procesan a la vez al entrenar y al evaluar, que valoramos;
- cuántos casos simultáneos tolera el sistema en producción, la proyección de consumo y cómo lo escalarían si sube la demanda;
- trabajos futuros para mejorarlo en todo sentido.

## Auditabilidad

**No aceptamos entregas, números ni afirmaciones que no sean 100% auditables y reproducibles, ni entregas que obliguen a volver a entrenar para verificarlas.**

- **Cada entrenamiento** deja el archivo exacto de conversaciones que usó, la configuración, la semilla (el número que fija los sorteos al azar), la corrida en Weights & Biases (W&B, una herramienta para registrar cada corrida de entrenamiento) y cada punto de control en Hugging Face, con su versión.
- **Cada número reportado** deja todas las conversaciones de la evaluación, con cada mensaje que entró al modelo y cada uno que salió, el resultado caso por caso y qué punto de control y qué prompt se usaron. `admision.correr` ya lo escribe así.
- **Todo archivo generado** (datos, conversaciones, resultados) sale de un script del repositorio, y el README o el informe dice qué script genera cada uno.
- **Se documenta cada pasada del desarrollo**, no solo la final, incluidos los experimentos que no funcionaron.
- **Reproducible** quiere decir que, con el mismo código, los mismos datos, la misma semilla y el mismo punto de control, la evaluación da el mismo resultado. Si hay una diferencia mínima (evaluar en lote en GPU puede mover algún caso), se documenta.
- **Cada commit es un cambio acotado con un solo propósito**: una mejora, la corrección de un error, un experimento o documentación. El mensaje dice qué cambia y por qué. Valoramos mucho que los commits se repartan de manera pareja entre los integrantes.

## Antes de empezar

```bash
cd missions/admision-guardia
uv sync
```

Lean el `README.md` de esta carpeta: ahí está el contrato de la entrega (un `entrega.py` con `construir_buscador` y `construir_agente`) y cómo se corren los casos de práctica.

Trabajen con la herramienta de programación con IA que prefieran (Claude Code, Codex, Gemini CLI, Cursor u otra).

## La entrega

- **El repositorio de código del grupo:** agente, buscador, curado, generación de conversaciones, optimización de prompt, entrenamiento y evaluación, con el `entrega.py` que pide el contrato.
- **El modelo final y sus puntos de control**, en un repositorio privado de Hugging Face compartido con la cátedra.
- **El proyecto de W&B**, compartido con la cátedra.
- **El historial clasificado y las costumbres**, en dos archivos:
  - `historial_clasificado.csv`, con dos columnas, `id,tipo`, y una fila por cada fila del historial (las 2.000); `tipo` es `correcta`, `error` o `ruido`;
  - `costumbres.md`, en texto libre: cada costumbre que descubrieron, explicada, con los ids de las filas que la respaldan. La cátedra controla también si las costumbres que describen son las verdaderas.
- **El informe** (`INFORME.md`): la comparación entre solo prompt, solo entrenamiento y las dos cosas juntas, los costos, la proyección a producción y los trabajos futuros.

Pueden hacer una **pre-entrega** cuando tengan todo y seguir mejorando hasta la entrega final.

## Cómo se corrige

En orden de importancia:

1. **Lo más importante, lejos: el modelo final en producción.** Cuenta cuántos casos del test secreto resuelve y cuánto cuesta y tarda cada caso. Entre dos modelos que resuelven lo mismo, gana el más barato de correr. El costo del desarrollo pesa poco, porque se paga una sola vez.
2. **Documentación, auditabilidad y explicación** de la entrega final y de todo el proceso de desarrollo.
3. **Curado, creación e ingeniería de datos**, incluido el acierto de la clasificación del historial.
4. **Optimización de recursos**, con sus costos y la proyección a producción.

El buscador cuenta por lo que rinde el agente con él. La evaluación aparte del buscador y la optimización de prompt cuentan como prácticas obligatorias documentadas. `admision.correr` informa, por caso, cuántas búsquedas hizo el agente, cuánto contexto le pasó al modelo y cuánto tardó.

**Referencia de la cátedra.** Se midió sobre los 50 casos de práctica, con las tres versiones de las normas (la original y las dos con los números cambiados), siempre con las normas completas, incluidas las secciones de otras áreas del hospital. Gemma 4 E4B sin entrenar resuelve 12, 15 y 12 casos en cada versión. Con un fine-tuning supervisado simple, resuelve 25, 24 y 25. Ese entrenamiento usó datos perfectos, generados por la cátedra. Ustedes van a entrenar con lo que curen.
