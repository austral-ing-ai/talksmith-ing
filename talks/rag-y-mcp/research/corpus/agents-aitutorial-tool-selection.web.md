---
source_file: agents-aitutorial-tool-selection
source_type: web-capture
ingested_at: 2026-08-14
---

# Tool Selection & Optimization (AI Tutorial)

## Provenance
- Original location: `research/web/agents-aitutorial-tool-selection/`
- Format: html (página de documentación, sitio construido con Mintlify). Texto tomado de `page.md` (~5.600 caracteres, 10 encabezados); la extracción es limpia y cubre la página entera.
- URL: https://aitutorial.dev/agents/tool-selection-and-optimization
- Autor / fuente: **aitutorial.dev**, sección "AI Agents". No hay autor firmante, ni fecha de publicación, ni bibliografía. El favicon y los logos (`logo-light-full.svg` / `logo-dark-full.svg`) se sirven desde un CDN de Mintlify bajo el identificador `digibee-1a4db0d2`, lo que sugiere que el sitio está operado por **Digibee**.
- Fecha del original: no declarada en la página. `fetched_at`: 2026-08-14T16:56:59Z.
- HTTP status: 200.

**Naturaleza de la fuente (importante para citarla).** Es un sitio de tutoriales comerciales, no un paper ni un estudio. Todas sus cifras se presentan bajo la fórmula "**Research shows:**" sin citar un solo trabajo. Es, sin embargo, la fuente **real** de las cifras que el deck de la Clase 5 usa en las slides 57-59 (y, con toda probabilidad, también de las de la slide 49) — ver `Inconsistencies / open questions`.

## Key claims

- **La precisión del agente cae a medida que crece la cantidad de herramientas.** Es la afirmación central de la página, presentada como una escalera de cuatro tramos (ver `Evidence and examples`). El titular de la página lo resume así: *"Agent accuracy drops from 92% to 58% as tool count grows from 5 to 20+."*
- **La causa que propone es de reconocimiento de patrones, no de razonamiento**: *"LLMs pattern-match descriptions. Large option spaces overwhelm them."*
- **Con 20 herramientas planas, el agente elige mal el 42 % de las veces.** Textual: *"The LLM sees all 20 at once and picks the wrong one 42% of the time."* El 42 % es simplemente el complemento del 58 % de la escalera, no una medición independiente.
- **Primera solución: enrutamiento jerárquico (hierarchical routing).** En vez de exponer 20 herramientas, se expone **una** herramienta de ruteo que toma `domain` + `action` y resuelve internamente a cuál llamar. La página le atribuye "90%+ accuracy".
- **Segunda solución: grupos de herramientas por contexto (context-based tool groups).** Una conversación tiene fases (saludo/autenticación, diagnóstico/búsqueda, resolución/ticketing); en cada fase se exponen sólo las 2-4 herramientas de esa fase. También se le atribuye "90%+".
- **El problema no es sólo la cantidad: la superposición semántica también destruye la precisión.** *"Even with just 3 tools, overlapping descriptions destroy accuracy."* Con `search_products`, `find_products` y `product_lookup` el LLM "picks randomly or calls all three".
- **La solución a la superposición es la diferenciación explícita en la descripción**, con guías de tipo "Use when" / "Do NOT use".
- **Recomienda instrumentar el uso de herramientas en producción** (analytics) para detectar herramientas no usadas, con alta tasa de fallo, o lentas.

## Definitions and terminology

**Hierarchical routing (enrutamiento jerárquico).** Patrón donde el agente ve una única herramienta de despacho cuyo esquema es un par de enumeraciones cerradas (`domain`, `action`), y un segundo paso resuelve el par a la herramienta concreta mediante un mapa. El punto de diseño es que el espacio de decisión que ve el LLM pasa de "20 nombres en lenguaje natural" a "4 × 5 valores de enum". Es el mismo mecanismo que Microsoft Research (ver `tool-space-interference-msr.web.md`) llama *hierarchical tool-calling* y recomienda que se estandarice a nivel de protocolo.

**Context-based tool groups / phases.** Filtrado dinámico del conjunto de herramientas expuesto según el estado de la conversación. La página modela la conversación como una máquina de estados de tres fases: `greeting` → `diagnosis` → `resolution`. Equivalente conceptual del *tool grouping* de VS Code y del *dynamic tool discovery* del GitHub MCP Server que cita el artículo de MSR.

**Overlapping functionality (superposición).** Dos o más herramientas cuyas descripciones cubren el mismo territorio semántico. El fallo asociado no es "elige mal por saturación" sino "elige al azar o llama a todas".

**"Use when" / "Do NOT use" guidance.** Convención de redacción de la descripción de una herramienta: cada descripción declara explícitamente su caso de uso *y* su caso de exclusión. Es el contenido concreto detrás del consejo genérico "escribí buenas descripciones".

**Tool usage analytics.** Telemetría por llamada (tasa de uso, tasa de fallo, latencia) usada para podar el catálogo de herramientas.

## Evidence and examples

**La escalera de precisión (la cifra que el deck reutiliza).** Presentada bajo el encabezado "**Research shows:** Agent accuracy decreases with tool count":

| Cantidad de herramientas | Selección correcta |
|---|---|
| 1-5 | 92 % |
| 6-10 | 84 % |
| 11-20 | 71 % |
| 20+ | 58 % |

**Sin fuente.** No hay cita, ni enlace, ni nombre de estudio, ni tamaño de muestra, ni modelo evaluado, ni definición de "selección correcta".

**Anti-patrón, verbatim (20 herramientas CRUD en lista plana):**

```
// Agent sees all 20 tools at once → 58% accuracy
const tools = [
    searchCustomers, searchProducts, searchOrders, searchTickets,
    getCustomer, getProduct, getOrder, getTicket,
    updateCustomer, updateProduct, updateOrder, updateTicket,
    createCustomer, createProduct, createOrder, createTicket,
    deleteCustomer, deleteProduct, deleteOrder, deleteTicket,
];
```

Es una matriz 4 dominios × 5 acciones — el ejemplo está construido para que el ruteo jerárquico sea la respuesta obvia.

**Solución 1 — ruteo jerárquico, verbatim:**

```
// Agent sees 1 tool instead of 20 → 90%+ accuracy
const routeTool = tool(async ({ domain, action }) => {
    const mapping = {
        "customers,search": searchCustomers,
        "customers,get": getCustomer,
        "orders,search": searchOrders,
        // ... 20 mappings
    };
    return mapping[`${domain},${action}`];
}, {
    name: "route_to_domain",
    schema: z.object({
        domain: z.enum(["customers", "products", "orders", "tickets"]),
        action: z.enum(["search", "get", "update", "create", "delete"]),
    })
});
```

**Solución 2 — grupos por fase, verbatim:**

```
function getToolsForPhase(phase: string) {
    const groups = {
        greeting:  [authenticateCustomer],
        diagnosis: [searchKnowledgeBase, checkSystemStatus],
        resolution: [createTicket, scheduleCallback],
    };
    return groups[phase];  // Agent sees 2-3 tools, not 20
}
```

**Ejemplo de diferenciación de herramientas superpuestas (e-commerce), verbatim:**

```
tool("search_products_by_text", {
    description: `Full-text search.
    Use when: customer describes product ("wireless mouse").
    Do NOT use when: you have exact SKU.`,
    schema: { query: z.string() }
});

tool("get_product_by_sku", {
    description: `Exact SKU lookup.
    Use when: customer provides SKU ("PROD-001").
    Do NOT use for search.`,
    schema: { sku: z.string() }
});

tool("filter_products_by_attributes", {
    description: `Structured filter.
    Use when: customer specifies category, price, brand.
    Do NOT use for text search.`,
    schema: { category: z.string().optional(), priceMax: z.number().optional() }
});
```

Con el resultado esperado, que es el ejemplo pedagógico más aprovechable de la página:

- "wireless mouse" → `search_products_by_text`
- "PROD-001" → `get_product_by_sku`
- "mice under $20" → `filter_products_by_attributes`

**Recomendaciones que la analítica debería producir (ejemplos de la página):**

- "Remove unused tool: `legacy_search`"
- "`flaky_tool` fails 40% — review error handling"
- "`slow_api` averages 3000ms — consider caching"

## Inconsistencies / open questions

1. **Ninguna cifra de esta página tiene fuente.** El "Research shows:" no apunta a nada. Es la debilidad estructural de la fuente: es la página que **origina** los números que el deck presenta como hallazgos de investigación, y ella misma no cita a nadie. Cualquier slide que use el 92/84/71/58 está, en última instancia, citando a un sitio de tutoriales sin autor ni fecha.
2. **El 42 % no es un dato independiente.** Es `100 − 58`. La página lo presenta en prosa ("picks the wrong one 42% of the time") como si fuera una observación separada de la escalera, y no lo es.
3. **El "90%+" de las dos soluciones no tiene ningún respaldo, ni siquiera un "Research shows".** Aparece dentro de un comentario de pseudocódigo (`// Agent sees 1 tool instead of 20 → 90%+ accuracy`). Es la promesa de mejora del tutorial, no una medición. Es la cifra más frágil de toda la página y es la que más incentivo tiene un deck a citar.
4. **El ruteo jerárquico esconde un costo que la página no menciona.** Reemplazar 20 herramientas por 1 no elimina la decisión: la traslada al esquema (`domain` × `action` = las mismas 20 combinaciones) y agrega un salto extra. La página no discute latencia adicional, ni qué pasa cuando el par `(domain, action)` no existe en el mapa, ni cómo se le devuelve al modelo un error de ruteo.
5. **"90%+" para grupos por fase presupone que la fase se conoce.** El ejemplo `getToolsForPhase(phase)` recibe la fase ya resuelta. Quién clasifica la fase, con qué precisión, y qué pasa cuando se equivoca, queda fuera de la página. Si la clasificación de fase la hace el mismo LLM, el problema de selección se reintrodujo un nivel más arriba.
6. **La sección de analytics no muestra código**, sólo dice "Track every tool call" y salta a las recomendaciones de salida. La extracción no perdió nada: la página realmente no incluye la implementación (el `page.md` pasa directo de "Track every tool call to find unused tools..." a la lista de recomendaciones).
7. **Relación con `tool-space-interference-msr.web.md`.** Las dos fuentes dicen cosas compatibles en dirección, pero sólo MSR aporta evidencia medida (encuesta de 1.470 servidores, recomendación de OpenAI de <20 funciones, 85 % de caída reportada en arXiv:2505.10570). Si una slide necesita respaldo real para "más herramientas = peor", el respaldo es MSR, no esta página. Esta página aporta los **patrones de solución** (ruteo, fases, "Use when / Do NOT use"), que es donde sí es útil.

## Images / diagrams

Dos assets, ambos el logotipo del sitio en sus dos variantes de tema. **La página no contiene ningún gráfico, diagrama ni captura**: la escalera 92/84/71/58 es una lista de viñetas en HTML, no una imagen. Si el deck muestra un gráfico de barras con esas cifras, el gráfico es de elaboración propia del deck, no de esta fuente.

### `agents-aitutorial-tool-selection.web/images/logo-light-full.svg`
- **Provenance**: `https://mintcdn.com/digibee-1a4db0d2/.../logo/logo-light-full.svg`, atributo `alt="light logo"`. Logo de cabecera para tema claro. 50.354 bytes.
- **Depiction**: logotipo vectorial del sitio "AI Tutorial" en su variante para fondo claro. El peso del archivo (~50 KB para un logo) indica trazados vectorizados, no tipografía viva.
- **Why it matters**: nada para la clase. Marca del sitio capturado. Sirve, eso sí, como rastro de procedencia: el identificador de CDN `digibee-1a4db0d2` vincula el sitio a Digibee, dato relevante al evaluar la independencia de la fuente.
- **Transcribed text**: sin texto legible extraíble del vector como cadena; el logotipo corresponde a la marca "AI Tutorial".

### `agents-aitutorial-tool-selection.web/images/logo-dark-full.svg`
- **Provenance**: `https://mintcdn.com/digibee-1a4db0d2/.../logo/logo-dark-full.svg`, `alt="dark logo"`. Variante para tema oscuro. 50.236 bytes.
- **Depiction**: el mismo logotipo, invertido para fondo oscuro.
- **Why it matters**: ninguna. Decoración de la interfaz.
- **Transcribed text**: ídem anterior.

## Raw / preserved excerpts

**Encabezado de la página (verbatim):**

> Hierarchical routing, context-based filtering, and analytics to improve tool selection accuracy
>
> Agent accuracy drops from 92% to 58% as tool count grows from 5 to 20+. This page covers hierarchical routing, context-based filtering, and tool analytics.

**"The Tool Selection Problem" (verbatim, completo):**

> **Scenario:** You give your agent 20 tools. The agent uses wrong ones constantly. **Research shows:** Agent accuracy decreases with tool count:
>
> - 1-5 tools: 92% correct selection
> - 6-10 tools: 84% correct selection
> - 11-20 tools: 71% correct selection
> - 20+ tools: 58% correct selection
>
> **Why:** LLMs pattern-match descriptions. Large option spaces overwhelm them.

**"Challenge 1: Too Many Tools" (verbatim):**

> Your customer support agent handles customers, products, orders, and tickets. The naive approach: register all 20 CRUD tools in a flat list. The LLM sees all 20 at once and picks the wrong one 42% of the time. **Anti-pattern:** All 20 tools in a flat list.

**"Solution 1: Hierarchical Routing" (verbatim):**

> Instead of 20 flat tools, give the agent 1 routing tool. It picks the domain + action, then a second step calls the specific tool.

**"Solution 2: Context-Based Tool Groups" (verbatim):**

> A support conversation has phases: greeting (authentication), diagnosis (searching), resolution (ticketing). During diagnosis, the agent doesn't need ticket creation tools. During resolution, it doesn't need search. Show only the tools relevant to the current phase — the agent sees 2-4 instead of 20.

**"Challenge 2: Overlapping Functionality" (verbatim):**

> Your e-commerce agent has three product tools: `search_products`, `find_products`, and `product_lookup`. They all sound the same — the LLM picks randomly or calls all three. Even with just 3 tools, overlapping descriptions destroy accuracy.

**"Solution: Clear Differentiation" (verbatim):**

> Each tool has a distinct purpose with "Use when" / "Do NOT use" guidance

**"Advanced: Tool Usage Analytics" (verbatim):**

> Track every tool call to find unused tools, high-failure tools, and latency bottlenecks: Run this in production to get recommendations like:
>
> - "Remove unused tool: `legacy_search`"
> - "`flaky_tool` fails 40% — review error handling"
> - "`slow_api` averages 3000ms — consider caching"
