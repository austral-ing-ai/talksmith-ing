# Misión: el prompt mínimo

## La idea

Resolver un target de programación en la **mínima cantidad de prompts posible**, con distintos modelos, midiendo todo: tokens de entrada, de salida, de pensamiento, tokens cacheados y gasto en dólares. La clase de prompting dio las técnicas; esta misión las pone bajo presupuesto.

Cada punto de calidad se paga en tokens, latencia y dinero, y la API se paga por uso: cada prompt de más queda registrado en la factura.

## Qué es OpenRouter

Todo pasa por **OpenRouter** (https://openrouter.ai). Es una **API unificada** sobre los modelos de todos los proveedores: una sola key, un solo endpoint (compatible con el formato de OpenAI) y el mismo request sirve para llamar a GPT, Claude, Gemini, DeepSeek, Grok, Qwen o Kimi cambiando solo el id del modelo.

Los servicios que provee:

- **Catálogo y comparación**: fichas por modelo con precios, ventana de contexto, benchmarks y parámetros soportados, más una vista comparativa en paralelo.
- **Routing**: el Auto Router elige el modelo por vos según la tarea, y hay fallbacks automáticos entre proveedores cuando uno se cae o se satura.
- **Contabilidad centralizada**: cada respuesta trae su usage y su costo, y el dashboard de actividad acumula el gasto de toda la cuenta, venga del modelo que venga.

Para qué lo usa la gente, más allá de esta misión:

- **Cambiar el modelo backend de sus herramientas**: Codex, Claude Code y otras aceptan un endpoint compatible, así que se las puede apuntar a OpenRouter y trabajar con el modelo que cada uno prefiera.
- **Probar modelos nuevos** apenas salen, sin crear una cuenta en cada proveedor.
- **Eficientizar el gasto**: mandar cada tarea a un modelo barato que la resuelva igual, a mano o vía routing.

### Requisitos

- Una cuenta de OpenRouter por grupo, con crédito cargado (el monto lo define la cátedra; eligiendo bien los modelos, la misión entera cuesta centavos).
- Python y su IA para programar de preferencia: Claude Code, Antigravity, Copilot o Codex.

## Antes de todo (obligatorio)

Antes de escribir código, exploren la plataforma y anoten lo que encuentren (lo van a usar en el ejercicio 1):

1. **Qué es un router.** Miren https://openrouter.ai/models?arch=Router&model_authors=openrouter y la ficha del **Auto Router** (https://openrouter.ai/openrouter/auto), que elige el modelo según lo que el mercado de OpenRouter usó para tareas parecidas en los últimos 7 días. Contesten en una línea: ¿qué hace un router de modelos y qué problema resuelve?
2. **El mapa de modelos.** En https://openrouter.ai/discover, busquen el **modelo más avanzado de cada proveedor conocido**: OpenAI, Anthropic, Grok, Gemini, DeepSeek, Qwen y Kimi. Anoten para cada uno: precio por millón de tokens de entrada y de salida, tamaño de ventana de contexto, y qué posición ocupa en los benchmarks que muestra la página. Para verlos en paralelo está la **vista comparativa**: `openrouter.ai/compare/<proveedor>/<modelo>/<proveedor>/<modelo>/...` compara precios, contexto, benchmarks y parámetros en una misma pantalla (por ejemplo, los cuatro modelos del ejercicio 1: https://openrouter.ai/compare/openai/gpt-5.6-luna/anthropic/claude-haiku-4.5/google/gemini-3.7-flash/deepseek/deepseek-v4-flash-0731).
3. **Parámetros comunes.** En https://openrouter.ai/models, el click en un modelo abre su ficha (`openrouter.ai/<proveedor>/<modelo>`), con descripción, ventana de contexto, precios y parámetros. Comparen dos o tres fichas de proveedores distintos: qué parámetros acepta cada uno (reasoning/effort, salidas estructuradas, temperatura y demás perillas de sampling). La versión programática de lo mismo: `GET https://openrouter.ai/api/v1/models` devuelve cada modelo con su campo `supported_parameters`. No todos aceptan lo mismo, y esa diferencia es la base del ejercicio 1.

## Ejercicio 1: una interfaz de chat, cuatro modelos

Armen una **interfaz de chat** que sirva estos **4 modelos** vía OpenRouter. No tiene que estar "linda" ni tener nada alrededor: es simplemente un chat que permite elegir el modelo y guarda las conversaciones. CLI alcanza y sobra; la pueden codear con su IA para programar (Claude Code, Antigravity, Copilot, Codex). Los modelos ya están elegidos para que el tiempo vaya al código y no a la elección:

| Slot | Modelo | Capacidad que ejercita | Qué aplica de la clase |
|---|---|---|---|
| 1 | `openai/gpt-5.6-luna` | **Effort configurable**: la interfaz permite elegir el nivel de `reasoning_effort` | Effort y thinking |
| 2 | `anthropic/claude-haiku-4.5` | **Prompt caching explícito** (`cache_control`), con un contexto estático grande para provocar hits | Caching y su economía |
| 3 | `google/gemini-3.7-flash` | **Salidas estructuradas** (JSON Schema) | Prompts estructurados |
| 4 | `deepseek/deepseek-v4-flash-0731` | **El escalón barato**: 15 veces más barato que el slot 2; comparen el costo de la misma pregunta | Elegir modelo, cascading |

(IDs verificados al 2026-09-02; si alguno desaparece del catálogo, reemplácenlo por el equivalente vigente del mismo proveedor y anótenlo en el informe.)

Datos verificados de la plataforma (2026-09-02) que les ahorran búsqueda:

- El **usage llega solo** en cada respuesta, sin parámetros extra: `usage.prompt_tokens`, `completion_tokens`, `prompt_tokens_details.cached_tokens`, `completion_tokens_details.reasoning_tokens`, `cost` y `cache_discount`.
- El **razonamiento** se controla con el parámetro unificado `reasoning`: `{"effort": "low" | "medium" | "high" | ...}` en el modelo del slot 1 (OpenAI); Claude y Gemini aceptan además `{"max_tokens": N}` como presupuesto de pensamiento.
- El **caching** es automático en OpenAI, Gemini y DeepSeek; en Anthropic y Qwen se activa marcando los bloques estáticos con `"cache_control": {"type": "ephemeral"}`. El hit se ve en `cached_tokens` y en `cache_discount`.

Requisitos de la interfaz:

- Muestra, **después de cada respuesta**, el usage que devuelve la API: tokens de entrada, de salida, de razonamiento y cacheados, y el costo.
- Permite **switchear de modelo**; cambiar de modelo inicia una conversación nueva.
- **Guarda el log de cada conversación en un archivo `.md`** (rol, mensaje, usage). Ese log es la entrega del ejercicio 2, así que esto no es opcional.
- Cuatro modelos, cuatro proveedores distintos.

**Criterio de éxito:** desde la interfaz se puede chatear con los 4 modelos, ver el usage de cada respuesta, y queda un log `.md` por conversación. En el slot 1 se ve el efecto de cambiar el effort; en el slot 2 se ve un cache hit (el costo de entrada baja en la segunda pasada del mismo contexto).

## Ejercicio 2: el target en 1 prompt

El target: **el juego de la vida de Conway**, en un solo script de Python (`vida.py`), solo con la biblioteca estándar. El modelo para resolverlo también está fijado: **`deepseek/deepseek-v4-flash-0731`** (el del slot 4), con el razonamiento activado.

El contrato exacto (esto es lo que su prompt tiene que transmitir completo):

- Uso: `python3 vida.py <archivo_estado_inicial> <generaciones>`.
- El archivo de estado es una grilla rectangular: una línea por fila, `#` célula viva, `.` célula muerta.
- El mundo es **finito**, del tamaño de la grilla: fuera de los bordes todo está muerto. Sin wrap-around.
- El script imprime por stdout la grilla resultante tras N generaciones, en el mismo formato.
- Con `generaciones = 0` imprime el estado inicial tal cual.

La cátedra provee los tests: `tests/test_vida.py` (9 casos: osciladores, naturalezas muertas, el glider, nacimiento, muerte por soledad, bordes y generación cero). Se corren con el script al lado: `python3 test_vida.py`.

Las reglas:

1. **A través de su chat** del ejercicio 1, pidan el script al modelo indicado.
2. Tiene que quedar **correcto en 1 prompt, o a lo sumo 2** (el segundo solo para pulir detalles).
3. Si se pasan de 2, **la corrida quedó quemada**: conversación nueva, prompt reescrito desde cero, y de vuelta. Prohibido parchear a mano o seguir chateando: lo que se mejora entre intentos es **el prompt**, no el código.
4. "Correcto" significa: **los 9 tests de `test_vida.py` pasan** con el script tal cual salió del chat.
5. **Usar caching es obligatorio.** En DeepSeek el cache es automático por prefijo repetido: no hay nada que configurar, pero sí que diseñar. La parte estática del prompt (el contrato, las instrucciones, los ejemplos) va al principio, idéntica en todos los intentos; lo que cambia entre corridas va al final. A partir del segundo intento, el usage tiene que mostrar `cached_tokens` mayor que cero, y eso va al informe.

Un prompt que sale bien a la primera es una **especificación completa**. Los 6 componentes de la clase (rol, contexto, instrucciones, restricciones, ejemplos, input) más few-shot de los casos clave (el contrato de arriba trae varios listos para convertir en ejemplos) rinden más que cualquier pedido de "hacelo bien".

**Criterio de éxito:** el log de la conversación ganadora muestra 1 o 2 prompts en total, `test_vida.py` corre con los 9 tests en verde, y los intentos posteriores al primero muestran cache hits en el usage.

## Ejercicio 3: la cuenta final

Documenten, para **todos** los intentos del ejercicio 2 (los quemados también):

- Tokens de entrada y de salida por intento, y totales.
- Tokens de pensamiento (si usaron un razonador) y qué se facturó por ellos. Ojo: algunos modelos (la serie o de OpenAI) razonan sin devolver esos tokens en la respuesta; si les pasa, documéntenlo como hallazgo.
- Tokens cacheados y cuánto ahorraron.
- Gasto total en USD, contrastado contra el dashboard de actividad de OpenRouter.
- Una conclusión de tres líneas: qué cambiarían del prompt, del modelo o de los parámetros para bajar el costo sin perder el "1 prompt".

**Criterio de éxito:** los números del informe cierran contra el dashboard, y la conclusión nombra una decisión concreta (no "mejorar el prompt").

## La entrega

- **El log del chat** (`.md`) de la conversación con la que crearon el script, con su usage.
- **El script** `vida.py` resultante.
- **El informe** del ejercicio 3.
- El código de la interfaz del ejercicio 1, en un repo con la forma de trabajo de la clase 2: CLAUDE.md, SPEC.md e historia de commits limpia.
