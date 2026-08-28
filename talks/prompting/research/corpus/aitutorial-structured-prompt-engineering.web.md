---
source_file: aitutorial-structured-prompt-engineering
source_type: web-capture
ingested_at: 2026-08-14
---

# Structured Prompt Engineering — AI Tutorial (aitutorial.dev)

## Provenance
- Original location: `research/web/aitutorial-structured-prompt-engineering/`
- Format: web capture (HTML + `page.md` extraído), página de documentación
- URL: https://aitutorial.dev/prompting/structured-prompt-engineering
- `fetched_at`: 2026-08-14T16:56:18Z
- `http_status`: 200
- Título capturado: `Structured Prompt Engineering - AI Tutorial`
- Autor / fuente: AITutorial.dev. Sitio de documentación construido sobre Mintlify; los logos se sirven desde un CDN de Digibee (`mintcdn.com/digibee-...`), lo que sugiere vinculación con esa empresa. **Autoría individual no declarada en la página.**
- Fecha del original: **sin fecha**. La página no trae fecha de publicación ni de última actualización. Las referencias que cita están fechadas en 2025.
- Sección del sitio: "Context Engineering & Prompt Design"
- Subtítulo de la página: "Design structured prompts that often reduce hallucinations"

Encuadre: es material didáctico / documentación práctica, **no una fuente académica**. Varias de sus afirmaciones cuantitativas no tienen referencia. Ver `Inconsistencies`.

## Key claims

- Tesis de apertura: **"The difference between a flaky prototype and a reliable production system often comes down to prompt structure."** La confiabilidad viene de la estructura, no de la redacción.
- **Anatomía de un prompt de producción — seis componentes.** Es el aporte más directamente utilizable de la página para la clase (una slide entera sale de acá):
  1. **Role/Persona** — fija comportamiento y nivel de expertise (valores: user, assistant, system)
  2. **Context** — información de fondo necesaria
  3. **Instructions** — qué hacer, paso a paso
  4. **Constraints** — qué NO hacer, formato de salida
  5. **Examples** — demostraciones few-shot (opcional)
  6. **Input** — los datos concretos a procesar
- El prompt resultante es más complejo que uno ingenuo, pero "this reflects the complexity of the task and the context needed to complete it when you use the API".
- **Etiquetas XML.** Por qué funcionan, según la página: (a) los LLM fueron entrenados sobre HTML/XML (datos web); (b) las etiquetas crean fronteras claras en el contexto; (c) hay reducción de alucinaciones en estudios controlados.
- **Few-shot: cuándo usarlo** — tareas complejas o subjetivas, formato de salida específico requerido, casos borde que necesitan aclaración.
- **Few-shot: calidad sobre cantidad** — "3-5 examples usually enough"; más ejemplos = más tokens = más costo; los ejemplos deberían cubrir **casos borde, no solo los obvios**. Este último punto es una recomendación práctica valiosa y contraintuitiva.
- **Salidas estructuradas con JSON Schema**: la imposición de esquema reduce errores de parseo y reintentos, y vuelve las salidas verificables por máquina.
- Distinción operativa importante que la página hace dos veces (para XML y para JSON): **incluir el esquema en el prompt** no es lo mismo que **usar la funcionalidad de salidas estructuradas de la API** (`response_format: json_object`). La segunda es más confiable. Para XML aclara que **la API de OpenAI no tiene un formato de respuesta XML nativo**, así que ahí solo queda prompt engineering más parseo.
- **Cada modelo tiene "personalidad" distinta** y conviene optimizar el prompt por modelo:
  - **GPT-4 / GPT-4 Turbo** — fuerte en salida estructurada y en seguir instrucciones complejas; sobresale con JSON y definiciones de rol claras.
  - **Claude (Sonnet/Opus)** — fuerte en lenguaje natural, razonamiento complejo y contexto largo; **se beneficia de bloques de pensamiento explícitos** (`<thinking>`); excelente con etiquetas XML y markdown.
  - **Gemini 1.5 Pro** — contexto masivo (2 M tokens) y multimodal; "many teams place the query at the end; validate per task".

## Definitions and terminology

- **Structured prompt engineering** — el objeto de la página: diseñar prompts por componentes explícitos en lugar de escribirlos como prosa corrida.
- **Role / Persona** — componente que "sets behavior and expertise level". La página aclara que los valores son los roles de la API: user, assistant, system.
- **Constraints (restricciones)** — definidas como "What NOT to do, output format". Explicitar lo prohibido es tan parte del prompt como explicitar lo pedido.
- **Antipattern vs. Best practice** — la página estructura la comparación de XML así (❌ Antipattern / ✅ Best practice), aunque **el contenido concreto de ambos ejemplos no sobrevivió a la extracción**: los encabezados están, los bloques comparados no.
- **Structured outputs (salidas estructuradas)** — funcionalidad de API que fuerza el formato de salida (`response_format: json_object` en OpenAI), distinta de pedir el formato en el prompt.
- **JSON Schema** — el contrato de salida. "Schema enforcement reduces parsing errors and retries; makes outputs machine-checkable."
- **Thinking blocks / `<thinking>` tags** — bloques donde Claude explicita su razonamiento. La página los presenta como buena práctica específica de ese modelo.
- **Caching (caché)** — mitigación recomendada para el costo en tokens que agregan las etiquetas y la estructura. Se menciona tres veces como contrapeso al overhead.

## Evidence and examples

**Afirmaciones cuantitativas de la página** (ver advertencias en `Inconsistencies`):

| Afirmación | Valor |
|---|---|
| Reducción de alucinaciones con etiquetas + validación | **40–60 % menos**, "Teams report" |
| Ejemplos few-shot recomendados | **3–5** "usually enough" |
| Contexto de Gemini 1.5 Pro | **2 M tokens** |

**Notas de producción, verbatim y organizadas por tema** — este material es exactamente lo que una clase aplicada necesita:

Sobre el prompt de seis componentes:
- Costo: los esquemas de salida claros reducen errores de parseo y reintentos (menos re-ejecuciones).
- Confiabilidad: los prompts estructurados son más fáciles de validar y monitorear.
- Rendimiento: leve overhead de tokens; mitigar con caché.

Sobre las etiquetas XML:
- Costo: etiquetar agrega tokens; mitigar con caché.
- Confiabilidad: las fronteras claras reducen respuestas fuera de contexto y mejoran la evaluabilidad.
- Rendimiento: leve overhead, compensado por menos reintentos y parseo más claro.

**Ejemplos de código por modelo** (los tres bloques que sí sobrevivieron a la extracción — preservados completos en `Raw / preserved excerpts`): un JSON de rol + tarea + esquema de salida para GPT-4; un bloque `<thinking>` para Claude; una carga masiva de contexto multimodal para Gemini.

**Ejercicio propuesto (Practice Check)**, útil si la clase quiere una consigna de práctico:
- Escribir un prompt que incluya rol, contexto, instrucciones, restricciones, ejemplos e input.
- Esperado: los 6 componentes presentes, con restricciones explícitas y un esquema de salida claro.
- Extra: comparar las salidas al remover la estructura y usar modelos menos potentes.

**Referencias externas que la página cita** (todas de 2025, ninguna capturada en este corpus):
- OpenAI Structured Outputs — https://openai.com/index/introducing-structured-outputs-in-the-api/
- Anthropic Prompt Engineering — https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- Gemini Prompting Strategies — https://ai.google.dev/gemini-api/docs/prompting-strategies

## Inconsistencies / open questions

- **Extracción parcial: faltan los ejemplos de prompt centrales.** La página está construida con componentes interactivos de Mintlify (pestañas, bloques comparativos) que no rindieron texto. Concretamente se perdieron:
  - El **prompt completo de seis componentes** que la página promete ("If we put all these components together, we get the following prompt"). El prompt no está.
  - El contenido de **❌ Antipattern** y **✅ Best practice** para XML. Solo quedaron los encabezados.
  - Los dos ejemplos de XML (schema-in-prompt vs. XML mode) y los dos de JSON (schema-in-prompt vs. JSON mode). Quedaron las descripciones, no el código.
  - El bloque "Let's put all this together in code".
  
  Solo sobrevivieron los tres bloques de optimización por modelo. **Si la clase quiere mostrar el prompt de seis componentes armado, ese ejemplo hay que escribirlo, no está en la captura.** El HTML original (490 kB) está en `research/web/aitutorial-structured-prompt-engineering/original.html` por si se quiere reintentar la extracción.
- **Afirmaciones cuantitativas sin fuente.** El "40–60 % fewer hallucinations" se atribuye a "Teams report" — no hay estudio, ni empresa, ni medición. La página también dice "Reduced hallucinations in controlled studies" sin citar ninguno. **Esta cifra no debería ir a una slide como dato.** Si la clase quiere afirmar que la estructura reduce alucinaciones, esta fuente no la respalda con evidencia verificable.
- **Sin fecha ni autor.** No hay forma de fechar la página ni de atribuirla a una persona. Las referencias que cita son de 2025, así que el material es al menos de ese año. Para una clase universitaria esto es una debilidad de la fuente que conviene tener presente al citarla.
- **Riesgo de obsolescencia rápida.** Las recomendaciones por modelo (GPT-4, Claude Sonnet/Opus, Gemini 1.5 Pro) están atadas a generaciones concretas. La afirmación sobre Gemini ("2M tokens") y la de que OpenAI no tiene formato XML nativo pueden dejar de ser ciertas.
- Matiz honesto de la propia página, que conviene conservar: sobre la ubicación de la consulta en Gemini dice "many teams place the query at the end; **validate per task**". El material se autolimita en varios puntos — buena señal de calidad.

## Images / diagrams

La página no trae ningún diagrama ni figura de contenido. Los únicos assets son las dos variantes del logotipo del sitio. Todo el material sustantivo son bloques de código, preservados como texto en `Raw / preserved excerpts`.

### `aitutorial-structured-prompt-engineering.web/images/logo-light-full.svg`
- **Provenance**: `research/web/aitutorial-structured-prompt-engineering/assets/logo-light-full.svg`, `alt="light logo"`, servido desde `mintcdn.com/digibee-1a4db0d2/.../logo/logo-light-full.svg`.
- **Depiction**: logotipo de cabecera del sitio en variante para fondo claro. SVG apaisado, `viewBox="0 0 1462 220"`. Combina un isotipo — dos `<circle>` y seis `<path>`, más un `<image>` raster embebido en base64 — con un bloque de texto tipográfico. El texto del wordmark está en **azul institucional `#234c7c`**, que es también el color del trazo del isotipo. Fondo transparente (todos los `fill` declarados son `none` salvo el del texto).
- **Why it matters**: nada de contenido. Sirve solo para identificar la fuente si el deck reproduce una captura de pantalla de la página.
- **Transcribed text**: **"AITutorial.dev"** — es un elemento `<text>` real dentro del SVG (a diferencia de los logos de arXiv, que son trazados), tipografiado a 192 px con la familia declarada `Noto Sans Linear A`, `fill:#234c7c`.

### `aitutorial-structured-prompt-engineering.web/images/logo-dark-full.svg`
- **Provenance**: `research/web/aitutorial-structured-prompt-engineering/assets/logo-dark-full.svg`, `alt="dark logo"`.
- **Depiction**: la misma marca, variante para fondo oscuro. Estructura idéntica (dos círculos, seis paths, una imagen raster embebida); la única diferencia real es el color del texto, que pasa a **blanco `#ffffff`** mientras el isotipo mantiene el trazo azul `#234c7c`. Los dos archivos no son idénticos byte a byte, pero difieren solo en eso.
- **Why it matters**: ninguna.
- **Transcribed text**: **"AITutorial.dev"**, `fill:#ffffff`.

## Raw / preserved excerpts

**Encabezado y tesis, verbatim:**

> # Structured Prompt Engineering
> Design structured prompts that often reduce hallucinations
> The difference between a flaky prototype and a reliable production system often comes down to prompt structure. This page covers XML tags, few-shot examples, and structured outputs that make LLM responses consistent and parseable.

**La anatomía de seis componentes, verbatim** (el material más citable de la página):

> ## The Anatomy of a Production Prompt
> **The Core Components:**
> 1. **Role/Persona** - Sets behavior and expertise level ( values: user, assistant, system)
> 2. **Context** - Background information needed
> 3. **Instructions** - What to do, step by step
> 4. **Constraints** - What NOT to do, output format
> 5. **Examples** - Few-shot demonstrations (optional)
> 6. **Input** - The actual data to process

> If we put all these components together, we get the following prompt. This promt looks more complex than the previous one, but this reflects the complexity of the task and the context needed to complete it when you use the API. The playground constructs the final prompt from these components, which is then sent to the OpenAI API as part of the JSON message payload. You can see the exact JSON payload that will be sent in the "OpenAI JSON Message" section after submitting.

*(Nota: el prompt prometido en esa frase no está en la captura — ver `Inconsistencies`. El "promt" mal escrito es del original.)*

> **Practice Check:**
> - Write a prompt that includes role, context, instructions, constraints, examples, and input.
> - Expected: All 6 components present with explicit constraints and a clear output schema.
> - **Try this too:** Compare the outputs if you remove the structure and use less powerful models

> **In Production:**
> - Cost impact: Clear output schemas reduce parsing errors and retries (fewer re-runs).
> - Reliability: Structured prompts are easier to validate and monitor.
> - Performance: Slight token overhead; mitigate with caching (see Model Selection & Cost Optimization)

**Etiquetas XML, verbatim:**

> ## XML Tags: Your Secret Weapon
> **Why XML Tags Work:**
> - LLMs were trained on HTML/XML (web data)
> - Tags create clear boundaries in the context
> - Reduced hallucinations in controlled studies

> **In Production:**
> - **Cost Impact:** Tagging adds tokens; mitigate with caching .
> - **Reliability:** Clear boundaries reduce off-context responses; improves evaluability.
> - **Performance:** Slight overhead; offset by fewer retries and clearer parsing.
> - **Real Example:** Teams report 40–60% fewer hallucinations when tags + validation are combined.

> ### Example 1: Schema in Prompt
> This approach includes the XML schema and example in the prompt itself, instructing the model to follow the XML structure.
> ### Example 2: Structured Outputs (XML Mode)
> This approach uses prompt instructions to request XML output combined with XML parsing and validation. Note that OpenAI's API doesn't have a native XML response format like json_object, so we rely on prompt engineering and parsing.

**Few-shot, verbatim:**

> ## Few-Shot Examples: Teaching by Showing
> **When to Use Few-Shot:**
> - Complex or subjective tasks
> - Specific output format required
> - Edge cases need clarification
> **Quality Over Quantity:**
> - 3-5 examples usually enough
> - More examples = more tokens = higher cost
> - Examples should cover edge cases, not just obvious ones

**Salidas estructuradas, verbatim:**

> ## Structured Outputs with JSON Schemas
> **Why:** Schema enforcement reduces parsing errors and retries; makes outputs machine-checkable.
> ### Example 1: Schema in Prompt
> This approach includes the JSON schema in the prompt itself, instructing the model to follow the schema structure.
> ### Example 2: Structured Outputs (JSON Mode)
> This approach uses OpenAI's structured outputs feature (`response_format: json_object`) combined with schema validation. This is more reliable than just including the schema in the prompt.

> See: [OpenAI Structured Outputs](https://openai.com/index/introducing-structured-outputs-in-the-api/) (2025), [Anthropic Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) (2025), [Gemini Prompting Strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) (2025) in Additional Resources.

**Optimización por modelo, verbatim con los tres bloques de código completos:**

> ## Model-Specific Prompt Optimization
> Different models have different "personalities." Here's what works best for each:

> ### GPT-4 / GPT-4 Turbo

```
# Strengths: Structured output, following complex instructions
# Best practices:
{
  "role": "senior_analyst",
  "task": "financial_analysis",
  "output_format": {
    "summary": "string",
    "key_metrics": ["string"],
    "recommendation": "buy|hold|sell"
  }
}

Input: Company revenue: $50M, growth: 15% YoY, market share: 8%
# GPT-4 excels at JSON, clear role definitions
```

> ### Claude (Sonnet/Opus)

```
# Strengths: Natural language, complex reasoning, long context
# Best practices:
<thinking>
Let me work through this step by step...
</thinking>

Analyze the quarterly financial report and identify key trends and risks.
# Claude benefits from explicit thinking blocks
# Excellent with XML tags and markdown
```

> ### Gemini 1.5 Pro

```
# Strengths: Massive context (2M tokens), multimodal
# Best practices:
[Upload entire 500-page PDF]
[Upload 10 images]
[Provide conversation history]

Based on ALL of the above context, answer: What are the main findings from the research study?
# Many teams place the query at the end; validate per task (see Gemini prompting strategies)
# Can handle entire codebases or document sets
```
