---
source_file: dspy-framework
source_type: web-capture
ingested_at: 2026-08-14
---

# DSPy — "Program, don't prompt, your LLMs" (sitio oficial del framework)

## Provenance
- Original location: `research/web/dspy-framework/`
- Format: web capture (HTML + `page.md` extraído), landing page del proyecto
- URL: https://dspy.ai
- `fetched_at`: 2026-08-14T16:56:54Z
- `http_status`: 200
- Título capturado: `DSPy`
- Autor / fuente: Stanford NLP y comunidad. No es un paper: es la página de producto del framework. Licencia MIT, Python ≥ 3.10.
- Fecha del original: sin fecha de publicación. La captura muestra la versión **DSPy 3.3.0** en el banner ("New ReActV2 Module and improved LM/BaseLM"). El proyecto se declara "Built in the open, since Dec 2022".
- Repositorio: https://github.com/stanfordnlp/dspy

Advertencia de encuadre: esta es una fuente **promocional**, no revisada por pares. Los números de adopción y las métricas de mejora los publica el propio proyecto. Es material legítimo para presentar el framework, no para respaldar afirmaciones comparativas de rendimiento.

## Key claims

- Tesis central, y es el eslogan de la página: **"Program, don't prompt, your LLMs."** El argumento es que el prompt manual es el problema, no la solución.
- DSPy es un framework de Python para construir sistemas de IA. La propuesta: **expresar las tareas como *signatures* estructuradas, no como prompts**, para producir programas mantenibles, modulares y optimizables.
- Signatures: "Define your task as typed inputs and outputs instead of managing messy prompts. Portable, maintainable, and easy to iterate on." La crítica al prompt como artefacto ("messy prompts") es explícita.
- Modules: "Same interface, different strategy." Los módulos controlan **cómo** se ejecuta una signature. Se puede razonar paso a paso, correr ensambles, usar herramientas o agregar un REPL **sin reescribir la tarea**. Este es el punto que más le sirve a una clase de prompting: las técnicas de prompting quedan reificadas como intercambiables.
  - El ejemplo de la página lo muestra en tres líneas: `dspy.Predict` (completado directo) → `dspy.ChainOfThought` (razonamiento paso a paso) → `dspy.ReAct` (herramientas y bucle de razonamiento), todas sobre la misma signature `Triage`. **Chain-of-thought y ReAct — o sea, `chain-of-thought-wei.web.md` y `react-yao.web.md` — aparecen acá convertidos en un parámetro de una línea de código.**
- Optimizers: "Compile your program against a metric." Se le dan a DSPy ejemplos y una función de scoring, y **ajusta los prompts automáticamente hasta que la calidad converge**. Es la afirmación más fuerte de la página y la más relevante para una clase de prompting: el prompt deja de escribirse a mano y pasa a compilarse.
- Las imágenes son un tipo de campo de signature (`dspy.Image`), lo que habilita tareas multimodales.
- Los módulos se componen con control de flujo Python común (el ejemplo `FactCheck` compone dos `ChainOfThought` dentro de un `dspy.Module`).
- El proyecto nació en Stanford NLP y creció como comunidad de investigación: "New optimizers and module types land here first — then show up in production systems at companies you've heard of."

## Definitions and terminology

Vocabulario propio de DSPy, útil si la clase quiere presentar la alternativa "programática" al prompting manual:

- **Signature (firma)** — la declaración de la tarea como entradas y salidas tipadas. Ejemplo de la página:
  ```python
  class ExtractEvent(dspy.Signature):
      """Extract event details from an email."""
      email: str = dspy.InputField()
      event_name: str = dspy.OutputField()
      date: str = dspy.OutputField()
  ```
  El docstring hace de instrucción; los campos, de contrato. **Sustituye al prompt en prosa.**
- **Module (módulo)** — la estrategia de ejecución de una signature. Misma interfaz, distinta estrategia: `dspy.Predict`, `dspy.ChainOfThought`, `dspy.ReAct`.
- **Optimizer (optimizador)** — compila el programa contra una métrica, ajustando prompts automáticamente. En la captura aparecen `dspy.GEPA` y, en la línea de tiempo, `MIPROv2`.
- **Compile (compilar)** — el verbo que DSPy usa para lo que en prompting manual sería "iterar el prompt". `optimizer.compile(programa, trainset)`.
- **Metric (métrica)** — la función de scoring contra la que se optimiza (en el ejemplo, `semantic_f1` o `accuracy`).
- **ReActV2** — módulo nuevo anunciado en la versión 3.3.0 del banner.
- **GEPA** — "Reflective Prompt Evolution", optimizador de julio 2025 (arXiv 2507.19457 según la línea de tiempo de la página).

## Evidence and examples

**Números de adopción declarados por el propio proyecto** (autorreportados, sin verificación independiente):

| Dato | Valor |
|---|---|
| Descargas mensuales | 7,5 M+ |
| Contribuidores | 441+ |
| Estrellas en GitHub | 37 k |
| Miembros de Discord | 8,4 k |
| PRs mergeados por año | 479+ |
| Tutoriales y recetas | 60+ |
| En producción en | Databricks, Shopify, Dropbox (logos en la página) |

**Métricas de mejora que muestra la página** (ejemplos ilustrativos dentro de bloques de código, no resultados de un estudio):

- Optimizador sobre RAG: `# Before: 0.41 F1` → `# After: 0.63 F1`
- Optimización de extracción: `# Baseline 62% (gpt-5.4-mini, zero-shot)` → `# Optimized 89% (gpt-5.4-mini + GEPA compile)`, con `# Cost $2.18 · 200 examples`

Ese último bloque es el más citable para una clase, porque pone las tres cosas juntas: **62 % zero-shot → 89 % optimizado, por 2,18 dólares y 200 ejemplos**. Pero es un ejemplo de la documentación, no un experimento reportado.

**Casos de producción listados** (cada uno con enlace propio en la página):

| Empresa | Caso |
|---|---|
| Shopify | Extracción de metadatos en todas las tiendas; **~550× de reducción de costo** |
| Dropbox | Optimización del juez de relevancia de Dash para ranking y evaluación |
| AWS | Migración de prompts de modelos grandes a chicos en Amazon Nova |
| JetBlue | Múltiples casos de chatbot sobre Databricks |
| Replit | Pipeline de reparación de código sintetizando diffs |
| Databricks | Jueces LM, RAG, clasificación, soluciones a clientes |
| Nous Research | Automejora evolutiva para el agente Hermes |

**Línea de tiempo de investigación asociada** (cada entrada con su arXiv):

| Fecha | Trabajo | arXiv |
|---|---|---|
| Dic 2025 | Recursive Language Models | 2512.24601 |
| Jul 2025 | GEPA: Reflective Prompt Evolution | 2507.19457 |
| Jul 2024 | BetterTogether: Fine-Tuning + Prompt Opt. | 2407.10930 |
| Jun 2024 | MIPROv2: Optimizing Instructions & Demos | 2406.11695 |
| Feb 2024 | STORM: Writing Wikipedia-like Articles | 2402.14207 |
| Oct 2023 | DSPy: Compiling Declarative LM Calls | 2310.03714 |
| Dic 2022 | Demonstrate-Search-Predict | 2212.14024 |

Si la clase quiere citar DSPy con una referencia académica y no con una landing page, **el paper es arXiv:2310.03714** (Oct 2023). No está capturado en este corpus.

## Inconsistencies / open questions

- **La captura es completa** (esta página sí rindió texto sustancial, ~7,6 kB de Markdown), pero **es una landing page de producto, no una fuente académica**. Todos los números de mejora y de adopción son autorreportados. Ninguna afirmación de esta fuente debería presentarse como evidencia comparativa.
- La página muestra código de ejemplo con modelos ficticios o futuros (`openai/gpt-5.4-nano`, `gpt-5.4-mini`). Son placeholders de la documentación; no tomarlos como referencia de modelos disponibles.
- **Tensión conceptual que vale la pena señalar en clase**: el eslogan "Program, don't prompt" es una crítica directa al objeto mismo de la Clase 3. DSPy sostiene que escribir prompts a mano no escala y que hay que compilarlos. Presentarlo al cierre de la clase da un contrapunto honesto: es la respuesta ingenieril a las limitaciones del prompting artesanal. Presentarlo como "otra técnica de prompting" sería contradecir su propia tesis.
- Lo que no está en la captura y la clase podría necesitar:
  - Cómo funciona realmente un optimizador (qué hace GEPA internamente). La página lo describe como caja negra: "It tunes your prompts automatically until quality converges."
  - Cuánto cuesta compilar en el caso general, y cuántos ejemplos etiquetados hacen falta.
  - Qué pasa cuando no hay métrica automática disponible — que es la situación habitual en tareas clínicas abiertas. La página asume que existe una función de scoring.
  - Evidencia independiente de las ganancias.

## Images / diagrams

La página trae solo logos corporativos de la sección "in production at". Ningún diagrama, ninguna figura conceptual. Los ejemplos de la página son bloques de código, no imágenes — y están preservados como texto en `Raw / preserved excerpts`.

### `dspy-framework.web/images/databricks-wordmark.svg`
- **Provenance**: `research/web/dspy-framework/assets/databricks-wordmark.svg`, `alt="Databricks"`, desde `https://dspy.ai/static/img/logos/databricks-wordmark.svg`. Aparece en la franja "in production at".
- **Depiction**: wordmark corporativo de Databricks. SVG vectorial muy apaisado, `viewBox="0 0 132 22"` — proporción típica de logotipo horizontal con isotipo más nombre. Letras trazadas como paths, sin texto seleccionable.
- **Why it matters**: solo como prueba social de adopción. Sin valor de contenido para la clase; si el deck reproduce logos corporativos, hay consideraciones de marca ajenas al material didáctico.
- **Transcribed text**: "databricks" (renderizado como trazados vectoriales, no como texto).

### `dspy-framework.web/images/shopify-wordmark.svg`
- **Provenance**: `research/web/dspy-framework/assets/shopify-wordmark.svg`, `alt="Shopify"`.
- **Depiction**: wordmark corporativo de Shopify. SVG vectorial, `viewBox="0 302.1 612 192"`, letras como paths.
- **Why it matters**: ídem — prueba social, sin valor de contenido.
- **Transcribed text**: "shopify" (trazados vectoriales).


## Raw / preserved excerpts

**Encabezado y propuesta de valor, verbatim:**

> DSPy 3.3.0 — New ReActV2 Module and improved LM/BaseLM · learn more →

> # Program, don't prompt, your LLMs.

> DSPy is a Python framework for building AI systems. Express your tasks as structured signatures, not prompts, to produce maintainable, modular, and optimizable programs.

> `$ pip install -U dspy` · **python** ≥ 3.10 · MIT license · Stanford NLP · github.com/stanfordnlp/dspy

**Ejemplo de portada — extracción de eventos desde un email (`extract_events.py`), verbatim:**

```python
lm = dspy.LM("openai/gpt-5.4-nano")

class ExtractEvent(dspy.Signature):
    """Extract event details from an email."""
    email: str = dspy.InputField()
    event_name: str = dspy.OutputField()
    date: str = dspy.OutputField()

extract = dspy.Predict(ExtractEvent)
extract(email=inbox_message)

# output
Prediction(
  event_name="Team Offsite",
  date="Thursday, June 5"
)
```

**Las tres primitivas, verbatim:**

> ## Compose programs with reusable primitives.

> ### Signatures — Declare your task.
> Define your task as typed inputs and outputs instead of managing messy prompts. Portable, maintainable, and easy to iterate on.

```python
class Triage(dspy.Signature):
    """Route a support ticket."""
    ticket: str = dspy.InputField()
    urgency: Literal["low", "high"] = dspy.OutputField()
    team: str = dspy.OutputField()
```

> ### Modules — Same interface, different strategy.
> Modules control how your signature executes. Reason, run ensembles, use tools, add a REPL, and more without rewriting your task.

```python
# Direct completion
classify = dspy.Predict(Triage)
# Add step-by-step reasoning
classify = dspy.ChainOfThought(Triage)
# Add tools and a reasoning loop
classify = dspy.ReAct(Triage, tools=[search])
```

> ### Optimizers — Compile your program against a metric.
> Give DSPy examples and a scoring function. It tunes your prompts automatically until quality converges.

```python
tp = dspy.GEPA(
  metric=semantic_f1,
  auto="medium")
opt = tp.compile(rag, trainset)
# Before: 0.41 F1
# After: 0.63 F1
opt.save("rag.v2.json")
```

**Ejemplo de agente con herramientas (muestra una traza estilo ReAct), verbatim:**

```python
def search(query: str) -> list[str]:
    """Search a knowledge base."""
    return kb.query(query, k=3)

def calc(expr: str) -> float:
    """Evaluate a math expression."""
    return dspy.PythonInterpreter({}).execute(expr)

agent = dspy.ReAct(
  "question -> answer",
  tools=[search, calc])
agent(question="GDP per capita of France?")

# output/stdout
# thought 1: I need France's GDP and population.
# action 1: search("France GDP") → ...
# thought 2: Now divide GDP by population.
# action 2: calc("3.13e12 / 68e6") → 46029.4
Prediction(answer="$46,029")
```

**Ejemplo de composición de módulos (`FactCheck`), verbatim** — interesante para la clase porque es verificación de afirmaciones, patrón trasladable a texto biomédico:

```python
class FactCheck(dspy.Module):
    def __init__(self):
        self.find = dspy.ChainOfThought(
            "article -> claims: list[str]")
        self.verify = dspy.ChainOfThought(
            "claim, source -> verdict")

    def forward(self, article):
        found = self.find(article=article)
        return [
            self.verify(claim=c, source=article)
            for c in found.claims]

# >>> FactCheck()(article=news_article)
[Prediction(verdict="supported"),
 Prediction(verdict="unsupported"),
 Prediction(verdict="supported")]
```

**Ejemplo multimodal, verbatim:**

```python
class AnalyzeChart(dspy.Signature):
    """Describe the trend and key data points in a chart."""
    chart: dspy.Image = dspy.InputField()
    title: str = dspy.OutputField()
    trend: str = dspy.OutputField()
    data_points: list[dict] = dspy.OutputField()

analyze = dspy.Predict(AnalyzeChart)
analyze(chart=dspy.Image("quarterly_revenue.png"))
```

**Ejemplo de optimización con cifras, verbatim** — el bloque más citable de la página:

```python
optimizer = dspy.GEPA(
  metric=accuracy, auto="medium")
optimized = optimizer.compile(
  extract, trainset=labeled_emails)
optimized.save("extract_v2.json")

# Baseline 62% (gpt-5.4-mini, zero-shot)
# Optimized 89% (gpt-5.4-mini + GEPA compile)
# Cost $2.18 · 200 examples
# Saved to → extract_v2.json
```

**Glosas de las primitivas, verbatim:**

> Signatures define tasks and enforce output types
> Define tools as functions and pass them to a ReAct module
> Compose multiple Signatures into new modules with plain Python control flow
> Images are a Signature field types, enabling multimodal tasks
> Optimizers improve your program against a defined metric

**Sección de historia, verbatim:**

> ## Built in the open, since Dec 2022.
> DSPy started at Stanford NLP and grew into a research community. New optimizers and module types land here first — then show up in production systems at companies you've heard of.

**Casos de producción, verbatim:**

> ### DSPy in production
> **Shopify** — Metadata extraction across all shops; ~550× cost reduction
> **Dropbox** — Optimized Dash relevance judge for ranking and evaluation
> **AWS** — Prompt migration from larger to smaller models on Amazon Nova
> **JetBlue** — Multiple chatbot use cases on Databricks
> **Replit** — Code repair pipeline using code LLMs to synthesize diffs
> **Databricks** — LM judges, RAG, classification, and customer solutions
> **Nous Research** — Evolutionary self-improvement for the Hermes agent

> Community: 441+ contributors · 8.4k discord members · 479+ merged PRs / yr · 60+ tutorials & recipes
