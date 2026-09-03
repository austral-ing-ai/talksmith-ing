---
source_file: tool-space-interference-msr
source_type: web-capture
ingested_at: 2026-08-14
---

# Tool-space interference in the MCP era: Designing for agent compatibility at scale (Microsoft Research Blog, 2025)

## Provenance
- Original location: `research/web/tool-space-interference-msr/`
- Format: html (entrada del blog de Microsoft Research). Texto tomado de `page.md` (~41.300 caracteres, 26 encabezados). La extracción trajo además todo el cromo de navegación corporativa de microsoft.com al principio del archivo (~4.000 caracteres de menú), que se descarta acá. El cuerpo del artículo se extrajo completo, incluidas las dos tablas.
- URL: https://www.microsoft.com/en-us/research/blog/tool-space-interference-in-the-mcp-era-designing-for-agent-compatibility-at-scale/
- Autores: **Adam Fourney** (Senior Principal Researcher), **Tyler Payne** (Senior Research Software Engineer), **Maya Murad** (Principal PM, AI Frontiers) y **Saleema Amershi** (Partner Research Manager). Lab: Microsoft Research AI Frontiers.
- Fecha del original: **11 de septiembre de 2025**.
- HTTP status: 200. `fetched_at`: 2026-08-14T16:57:38Z.

**Naturaleza de la fuente.** Es un **post del blog de Microsoft Research**, no un paper con revisión de pares. Reporta una encuesta empírica propia (1.470 servidores MCP) y libera una herramienta open source (MCP Interviewer). Es la fuente con evidencia medida más sólida del bloque de selección de herramientas.

## Key claims

- **Tesis central — *tool-space interference*.** Definida textualmente: *"Tool-space interference describes situations where otherwise reasonable tools or agents, when co-present, reduce end-to-end effectiveness. This can look like longer action sequences, higher token cost, brittle recovery from errors, or, in some cases, task failure."*
- **El problema nace del éxito de MCP, no de su fracaso.** Los avances agénticos de 2025 se apoyaron en **integración vertical** (herramientas y agentes co-diseñados, co-entrenados y testeados juntos). MCP habilita **integración horizontal** entre proveedores, y con ella aparecen modos de falla nuevos. Los autores llaman a ese escenario una *society of agents*.
- **Un servidor MCP no sabe con qué cliente ni con qué modelo habla.** Es el hilo conductor de todo el análisis: *"MCP servers do not know which clients or models they are working with, and present one common set of tools, prompts, and resources to everyone."* Distintos modelos toleran contextos y espacios de herramientas muy distintos, con límites duros divergentes. Eso pone a MCP en desventaja frente a las integraciones verticales.
- **El servidor promedio es razonable; el problema son los outliers.** *"On balance, along any given dimension, the average MCP server is quite reasonable—but, as we have seen, outliers and diverging assumptions can introduce trouble."* La mayoría de los servidores exponen cuatro herramientas o menos.
- **Cinco ejes de interferencia medidos**: (1) cantidad de herramientas, (2) longitud de las respuestas, (3) complejidad de los parámetros, (4) colisiones y ambigüedad de nombres, (5) errores mal señalizados. Un sexto eje, el de recursos, se analiza como adopción casi nula.
- **MCP carece de un mecanismo formal de namespaces.** Si dos servidores registran herramientas con el mismo nombre, desambiguar es imposible. El OpenAI Agents SDK directamente lanza un error; Claude Code prefija los nombres con identificadores únicos como workaround.
- **MCP no dice nada sobre cuántos tokens puede devolver una herramienta.** *"MCP offers no guidance on how many tokens a tool call can produce."* La gestión de contexto queda indefinida en la especificación y los desarrolladores de servidores no pueden contar con ningún comportamiento particular del cliente.
- **Los servidores señalizan mal los errores.** Es común devolver el error como string dejando el flag `IsError` en false, es decir, señalizando salida normal.
- **Recomendación principal a los desarrolladores del protocolo**: namespaces formales (y jerárquicos, para poder agrupar catálogos grandes en *tool sets*) y una especificación para recursos provistos por el cliente.
- **Recomendación a los desarrolladores de servidores**: publicar una *MCP Server card* con las características de runtime (tokens esperados, latencia esperada, modelos y clientes con los que se testeó, incompatibilidades conocidas).
- **Recomendación a los desarrolladores de clientes**: cachear esquemas de herramientas, usarlos como blanco de optimización de prompts o **como índice para selección de herramientas al estilo RAG**, resolver colisiones generando namespaces a partir de los nombres de servidor, y resumir o paginar respuestas largas.
- **Recomendación a los marketplaces**: servir esquemas de herramientas optimizados por modelo/cliente, análogo a cómo PyPI distribuye wheels según sistema operativo y procesador.

## Definitions and terminology

**Tool-space interference.** El término que acuña el artículo. Situación en que herramientas o agentes individualmente razonables, al coexistir, degradan la efectividad de punta a punta. Manifestaciones: secuencias de acciones más largas, mayor costo en tokens, recuperación frágil ante errores, o fallo de tarea.

**Vertical integration vs. horizontal integration.** La integración vertical es el modo en que se construyeron los sistemas agénticos exitosos hasta ahora: herramientas y agente diseñados, entrenados y probados en conjunto (el ejemplo que dan es que los modelos recientes de OpenAI *presuponen* la disponibilidad de herramientas de búsqueda web y de recuperación de documentos). La integración horizontal es lo que habilita MCP: cualquier agente contra cualquier herramienta, sin co-diseño. La tesis del artículo es que la segunda compra capacidad al precio de interferencia.

**Society of agents.** El escenario en que agentes de distintos desarrolladores y empresas se encuentran y deben cooperar. Varían en cuán coordinados están, cuán alineados están sus objetivos y cuánta información comparten. La pregunta que abre el artículo: *"Can heterogenous agents and tools cooperate in this setting, or will they hinder one another and slow progress?"*

**MCP Interviewer.** La herramienta que construyeron para automatizar la inspección de servidores MCP en ejecución. Procedimiento en tres etapas: (1) cataloga tools, prompts, resources, resource templates y capabilities, y calcula estadísticas descriptivas; (2) usa un LLM (GPT-4.1) para construir un **plan de testeo funcional** que llame a cada herramienta al menos una vez, recolectando salidas, errores y estadísticas; (3) califica criterios cualitativos aplicando rúbricas hechas a medida sobre los esquemas y las salidas. Liberada como CLI open source en `github.com/microsoft/mcp-interviewer`.

**Namespace (en el sentido de MCP).** Mecanismo formal — **inexistente hoy en la especificación** — para calificar los nombres de herramientas por servidor de origen. Los autores piden además que sea **jerárquico**, porque eso daría de paso una forma de organizar catálogos grandes en conjuntos temáticos.

**Tool sets / hierarchical tool-calling.** Agrupación de herramientas en conjuntos temáticos que el cliente puede habilitar y deshabilitar. Ya aparece en el *dynamic tool discovery* del GitHub MCP Server y en el *tool grouping (with virtual tools)* de VS Code. La visión que proponen: *"a standardized mechanism for grouping tools would allow clients to engage in hierarchical tool-calling, where they first select a category, then select a tool, without needing to keep all possible tools in context."* Es exactamente el patrón que `agents-aitutorial-tool-selection.web.md` llama *hierarchical routing*, pero acá pedido a nivel de protocolo en vez de implementado a mano por el desarrollador.

**Input schema depth (profundidad del esquema de entrada).** Métrica que definen para medir complejidad de parámetros. La escala es explícita: profundidad 0 = herramienta sin propiedades; 1 = propiedades nombradas pero sin anotaciones (sin descripción ni tipo); 2 = propiedades nombradas **y** anotadas; 3+ = propiedades estructuradas con anotaciones anidadas.

**`resource_link`.** Resultado que una herramienta puede devolver para que el cliente recupere un recurso. Los autores argumentan que sería el comportamiento ideal para herramientas que devuelven respuestas largas tipo documento — y encontraron que **sólo 4 herramientas** en toda la encuesta lo hacen.

**`IsError`.** Flag del protocolo para señalizar que una llamada falló. El hallazgo es que muchos servidores lo dejan en false y devuelven el error como texto.

**Context rot.** Concepto que citan (vía research.trychroma.com) para sostener que los límites prácticos de contexto son mucho más bajos que los límites duros: aun dentro de la ventana, los contextos grandes suben el costo y bajan el rendimiento.

## Evidence and examples

**Metodología de la encuesta.** Muestrearon dos registros: **smithery.ai** (más de 7.000 servidores de primera parte y de la comunidad, muestreados vía la API de Smithery) y **Docker MCP Hub** (entradas populares recolectadas a mano). Lanzaron cada servidor para inspeccionarlo. Tras excluir los vacíos o que no arrancaron, y deduplicar los de features idénticas, quedaron **1.470 servidores** en el catálogo.

**Limitación declarada por los propios autores**: la autorización. Muchos de los servidores más populares dan acceso a servicios que requieren credenciales, lo que impide el análisis automatizado. De esos se pueden sacar features estáticas pero el testeo funcional queda limitado.

**Cantidad de herramientas por servidor** (Figura 2, estadísticas leídas del gráfico):

| Estadístico | Valor |
|---|---|
| Media | 8,60 |
| Mediana | 4,00 |
| Desvío estándar | 15,85 |
| Mínimo | 0 |
| **Máximo** | **256** |

Complementado en prosa: los 10 servidores siguientes al más grande agregan más de 100 herramientas cada uno. Casos concretos y citables: **Playwright-MCP con 29 herramientas** y **GitHub MCP con 91** (con subconjuntos disponibles en endpoints alternativos). El gráfico marca dos líneas de referencia: el **límite de la API de OpenAI (128 herramientas)** y la **recomendación de OpenAI (20)**.

**Recomendación de OpenAI, citada verbatim por el artículo:**

> "*Keep the number of functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions at any one time, though this is just a soft suggestion.*"

**Degradación por espacio de herramientas grande**: *"large tool spaces can lower performance by up to 85% for some models"*, citando arXiv:2505.10570v1.

**Longitud de las respuestas** (Figura 3). Base: **2.443 llamadas exitosas sobre 1.312 herramientas únicas**.

| Estadístico | Valor |
|---|---|
| Total de herramientas | 1.312 |
| Media | 4.431 tokens |
| **Mediana** | **98 tokens** |
| Mínimo | 0 tokens |
| **Máximo** | **557.766 tokens** |

La distancia entre mediana (98) y media (4.431) es el dato: la distribución está dominada por outliers. **16 herramientas producen más de 128.000 tokens**, desbordando GPT-4o. La herramienta top devuelve en promedio 557.766 tokens, suficiente para desbordar incluso GPT-5. Los autores agregan que aun cuando la respuesta entra en la ventana, las respuestas excesivamente largas degradan el rendimiento **hasta un 91 %** según arXiv:2505.10570v1.

**Tabla de desborde de contexto (verbatim del artículo)** — cantidad de herramientas que desbordarían el contexto en N llamadas:

| Modelo | Ventana de contexto | 1 llamada | 2 llamadas | 3-5 llamadas | 6-10 llamadas |
|---|---|---|---|---|---|
| GPT-4.1 | 1.000.000 | 0 | 1 | 7 | 11 |
| GPT-5 | 400.000 | 1 | 7 | 15 | 25 |
| GPT-4o, Llama 3.1 | 128.000 | 16 | 15 | 33 | 40 |
| Qwen 3 | 32.000 | 56 | 37 | 86 | 90 |
| Phi-4 | 16.000 | 93 | 60 | 116 | 109 |

*(Nota de extracción: en `page.md` esta tabla llegó como una tira de texto sin separadores — `GPT 4.11,000,00001711` — y se reconstruyó columna por columna a partir de las ventanas de contexto conocidas de cada modelo. La reconstrucción es fiel pero conviene verificarla contra `original.html` antes de proyectarla en una slide.)*

**Complejidad de parámetros** (Figura 4). Base: **12.643 herramientas**.

| Estadístico | Valor |
|---|---|
| Total de herramientas | 12.643 |
| Media | 2,24 |
| Mediana | 2,00 |
| Desvío estándar | 1,38 |
| Mínimo | 0,00 |
| **Máximo** | **20,00** |

Es decir: la enorme mayoría de las herramientas tiene profundidad 2 (propiedades nombradas y anotadas), y existe **al menos un caso con 20 niveles de anidamiento**. Evidencia externa que citan: **composio** encontró que aplanar el espacio de parámetros mejora el tool-calling **un 47 %** respecto de la línea de base.

**Colisiones de nombres.** Encontraron colisiones entre **775 herramientas**. La más común es `search`, que aparece en **32 servidores MCP distintos**. Top 10 (verbatim):

| Nombre de herramienta | Instancias |
|---|---|
| `search` | 32 |
| `get_user` | 11 |
| `execute_query` | 11 |
| `list_tables` | 10 |
| `update_task` | 9 |
| `generate_image` | 9 |
| `send_message` | 9 |
| `execute_command` | 8 |
| `list_tasks` | 8 |
| `search_files` | 8 |

**Similaridad semántica sin colisión exacta.** Listan 24 nombres distintos de herramientas de búsqueda web que conviven en el ecosistema — el ejemplo perfecto del problema de "superposición" en escala real:

```
websearch            brave_web_search      search-web            tavily_web_search
web_search           google_news_search    search_web            google-play-search
search_webkr         google_search_parsed  google_search         search_google_images
search_google        get_webset_search_exa ai_web_search         search_google_scholar
web_search_exa       duckduckgo_web_search search_web_tool       google_search_scraper
web_search_agent     answer_query_websearch batch-web-search
```

**Errores mal señalizados.** Sobre **5.983 resultados de llamada sin flag de error**, GPT-4.1 juzgó que **3.536 indicaban errores en su contenido** — casi el 60 %. Y la calidad de los mensajes es mala: dos ejemplos verbatim que dan, una herramienta de búsqueda web que falló con el string **"error: job"**, y una de búsqueda académica que devolvió **"Please retry with 0 or fewer IDs."**

**Adopción de recursos.** Sólo **112 servidores (7,6 %)** reportaron algún recurso, y **74 (5 %)** proveyeron templates. Sólo **4 herramientas** devolvieron un `resource_link`.

**Escala del ecosistema (datos de terceros que cita).** Zapier: catálogo de 30.000 herramientas sobre 7.000 servicios. Composio: más de 100 servidores MCP gestionados. Hugging Face sirviendo Spaces por MCP. Shopify con MCP habilitado para millones de tiendas.

**Mejora reportada por Anthropic**: usar un agente de testeo de herramientas para reescribir los prompts de servidores MCP defectuosos mejoró el tiempo de completitud de tareas **un 40 %**.

## Inconsistencies / open questions

1. **VERIFICACIÓN PEDIDA — el gráfico de la slide 52 del deck NO está respaldado por este artículo.** El deck atribuye a *"Tool Space Interference in the MCP Era — Microsoft Research"* un gráfico de barras con **1-3 parámetros → 90 %, 4-6 → 80 %, 7+ → 65 %** de "Precisión del Agente". **Ese gráfico no existe en esta fuente y esas cifras tampoco.** Revisión exhaustiva del artículo:
   - Los **únicos porcentajes** que aparecen en todo el texto son: **85 %** (caída de rendimiento por espacios de herramientas grandes, de arXiv:2505.10570v1), **91 %** (degradación por respuestas largas, misma referencia), **47 %** (mejora de composio al aplanar parámetros), **40 %** (mejora de Anthropic reescribiendo prompts), **7,6 %** (servidores con recursos) y **5 %** (servidores con templates). No hay 90 %, no hay 80 %, no hay 65 %.
   - El artículo **sí trata** la complejidad de parámetros, pero **no la mide contra precisión del agente**. Lo que mide es la *profundidad del esquema* (media 2,24, mediana 2,00, máximo 20) sobre 12.643 herramientas — una estadística descriptiva del ecosistema, no una curva de precisión. La única cifra que vincula parámetros con rendimiento es la de composio (47 % de mejora al aplanar), que es de un tercero, apunta en la dirección contraria (mejora, no precisión absoluta) y no está desglosada por cantidad de parámetros.
   - El artículo **nunca cuenta parámetros por herramienta** en los tramos "1-3 / 4-6 / 7+". Esa segmentación no aparece.
   - **Conclusión: la atribución del deck es falsa.** Las cifras 90/80/65 no provienen de Microsoft Research. La slide 52 le adjudica a una fuente real un gráfico que esa fuente no contiene.

2. **VERIFICACIÓN PEDIDA — el "42 % de error con 20+ herramientas" tampoco sale de acá.** Ese número no aparece en el artículo en ninguna forma. Su origen real es `agents-aitutorial-tool-selection.web.md` (aitutorial.dev), donde figura como *"the LLM sees all 20 at once and picks the wrong one 42% of the time"* — y donde es, a su vez, el mero complemento del 58 % de una escalera de precisión sin fuente. **Lo más cercano que dice Microsoft Research** es la recomendación de OpenAI que cita ("apuntar a menos de 20 funciones a la vez, aunque es sólo una sugerencia blanda") y la caída de "hasta 85 % para algunos modelos" de arXiv:2505.10570v1. Ninguna de las dos es un 42 %, ninguna se expresa por tramo de cantidad de herramientas, y la de 85 % es un límite superior ("up to") sobre "algunos modelos", no una media.

3. **En resumen, para la clase**: el deck tiene **dos** conjuntos de cifras sobre selección de herramientas (la escalera 92/84/71/58 de las slides 57-59 y la curva de parámetros 90/80/65 de la slide 52), y **ninguno de los dos** proviene de Microsoft Research. El primero viene de aitutorial.dev sin fuente; el segundo no tiene origen identificable en ninguna de las capturas de este corpus. Lo que **sí** puede citarse de MSR con respaldo textual: la mediana de 4 herramientas por servidor, el máximo de 256, GitHub MCP con 91 herramientas, la recomendación de OpenAI de <20 funciones, la mediana de 98 tokens contra el máximo de 557.766, las 775 colisiones de nombres, `search` en 32 servidores, y los 3.536 errores mal señalizados sobre 5.983.

4. **Las dos referencias cuantitativas fuertes del artículo apuntan al mismo preprint.** Tanto el 85 % (espacios de herramientas grandes) como el 91 % (respuestas largas) salen de **arXiv:2505.10570v1**, que no está capturado en este corpus. Si una slide quiere apoyarse en esas cifras, la fuente primaria es ese preprint y no se verificó.

5. **La encuesta es de servidores, no de agentes.** Mide propiedades del catálogo (cuántas herramientas, qué tan profundos los esquemas, qué tan largas las respuestas). **No mide tasa de acierto de ningún agente.** Es la razón de fondo por la que no puede respaldar ninguna curva de "precisión del agente": no es el tipo de estudio que produce ese dato. Usarlo como fuente de una curva de precisión es un error de categoría, no sólo de cifra.

6. **El sesgo de autorización, admitido por los autores, corta justo donde más importa.** Los servidores más populares son los que requieren credenciales, y son precisamente los que quedaron fuera del testeo funcional. Las estadísticas de longitud de respuesta y de errores están calculadas, entonces, sobre el subconjunto de servidores que se pueden ejecutar sin autenticar — probablemente los más simples y menos usados.

7. **Los dos denominadores no coinciden y conviene no mezclarlos.** La profundidad de esquema se calcula sobre **12.643 herramientas** (análisis estático, no requiere ejecutar nada), mientras que la longitud de respuesta se calcula sobre **1.312 herramientas** (sólo las que se pudieron llamar con éxito). Citar "12.643 herramientas analizadas" junto a la mediana de 98 tokens sería incorrecto.

8. **El conteo de herramientas es un instantáneo.** Nota al pie de la Figura 2, verbatim: *"servers can change the tools they list at any time, but only 226 servers in our catalog declare this capability."* De 1.470 servidores, sólo 226 declaran la capacidad de cambiar su lista.

9. **Fecha y obsolescencia.** El artículo es de **septiembre de 2025** y describe el ecosistema MCP de ese momento. El deck es de abril de 2026. Cualquier recuento del ecosistema (7.000 servidores en Smithery, 30.000 herramientas en Zapier) está desactualizado por diseño y debería citarse con la fecha adjunta.

10. **El título capturado trae basura.** `metadata.yaml` registra el título como `"Tool-space interference in the MCP era: Designing for agent compatibility at scale - Microsoft ResearchYour Privacy Choices Opt-Out Icon"` — el sufijo del banner de privacidad quedó pegado al `<title>`. No afecta al contenido.

## Images / diagrams

Once assets. Cuatro tienen contenido técnico real (las Figuras 1 a 4 del artículo); el resto es hero image, retratos de los autores y logos institucionales. Los cuatro gráficos son **la mejor evidencia visual disponible en todo el corpus** para el bloque de selección de herramientas — y ninguno de ellos es el gráfico de la slide 52.

### `tool-space-interference-msr.web/images/image.png`
- **Provenance**: `https://www.microsoft.com/en-us/research/wp-content/uploads/2025/09/image.png`. **Figura 1** del artículo. 140.559 bytes.
- **Depiction**: diagrama de la arquitectura multi-agente de Magentic-One, anotado en rojo. Arriba al centro, una flecha roja gruesa baja desde la leyenda **"Any git-related task"** (con "Any" en negrita) hacia una caja apilada rotulada **"⚙ Orchestrator"**. De esa caja bajan cuatro flechas hacia una fila de cajas de agentes, cada una con su ícono y su descripción debajo: **Coder** (`</>`) — "Write code and reason to solve tasks"; **ComputerTerminal** (monitor) — "Execute code written by the coder agent"; **WebSurfer** (globo) — "Browse the internet (navigate pages, fill forms, etc)"; **FileSurfer** (documento) — "Navigate files (e.g., PDFs, pptx, WAV, etc)". A la izquierda de la fila, la etiqueta "Agents / Observe and act based on Orchestrator instruction". A la derecha, separada por un borde marrón, una quinta caja con código: `AssistantAgent( "You are a help… GitHubMCP )`. Sobre esa caja, en rojo, **"on every orchestration step…"**. Debajo de tres de las cajas, tres preguntas en rojo que son el chiste del diagrama: **"Use git cli?"**, **"Visit GitHub in the browser?"**, **"Use GitHub MCP?"**.
- **Why it matters**: es la ilustración más limpia de qué es la interferencia de espacio de herramientas, y no necesita ninguna cifra para funcionar. Tres caminos igualmente válidos hacia el mismo recurso (GitHub), y el orquestador tiene que elegir **en cada paso**. Sirve directo para una slide sobre por qué agregar un servidor MCP no es gratis. Además introduce el problema de divergencia de estado que el texto explica: cambiar de branch en el navegador no cambia el branch en la terminal.
- **Transcribed text**: `Any git-related task` · `⚙ Orchestrator` · `Agents / Observe and act based on Orchestrator instruction` · `</> Coder` / `Write code and reason to solve tasks` · `ComputerTerminal` / `Execute code written by the coder agent` · `WebSurfer` / `Browse the internet (navigate pages, fill forms, etc)` · `FileSurfer` / `Navigate files (e.g., PDFs, pptx, WAV, etc)` · `AssistantAgent( "You are a help… GitHubMCP )` · `on every orchestration step…` · `Use git cli?` · `Visit GitHub in the browser?` · `Use GitHub MCP?`

### `tool-space-interference-msr.web/images/tool-counts-per-server-1024x1024.png`
- **Provenance**: `https://www.microsoft.com/en-us/research/wp-content/uploads/2025/09/tool-counts-per-server-1024x1024.png`, `alt="chart"`. **Figura 2**. 27.570 bytes.
- **Depiction**: gráfico de dispersión cuadrado, fondo gris claro, titulado **"Tool Counts per Server"**. Eje horizontal: **"Server (index, sorted)"**, de 0 a ~1.470. Eje vertical **logarítmico**: **"Number of Tools (log scale)"**, de 10⁰ a algo más de 10². Los puntos forman una escalera de mesetas planas: un tramo largo en 1 herramienta (índices 0 a ~350), luego 2 (~350-420), 3 (~510-670), 4 (~670-800), 5, 6, 7… y a partir del índice ~1.300 la curva se dispara casi vertical, con los puntos cambiando de azul a verde, amarillo y rojo. Un único punto rojo aislado arriba a la derecha marca el máximo. Dos líneas horizontales punteadas rosadas cruzan el gráfico, identificadas en la leyenda inferior derecha como **"OAI API Limit (128)"** y **"OAI Recommendation (20)"**. Arriba a la izquierda, un recuadro de fondo violeta claro con las estadísticas.
- **Why it matters**: es **la** figura para la slide de "¿cuántas herramientas es demasiado?". Cuenta dos cosas a la vez: que el ecosistema es sano en la mediana (4 herramientas) y que la cola es brutal (256). La línea punteada de la recomendación de OpenAI en 20 permite mostrar visualmente qué fracción del ecosistema ya la excede. Reemplaza con ventaja al gráfico sin fuente de la slide 52.
- **Transcribed text**: `Tool Counts per Server` · recuadro de estadísticas: `Mean: 8.60` / `Median: 4.00` / `Std: 15.85` / `Min: 0.00` / `Max: 256.00` · eje Y: `Number of Tools (log scale)` · eje X: `Server (index, sorted)` · leyenda: `OAI API Limit (128)` / `OAI Recommendation (20)` · marcas de eje: `10⁰`, `10¹`, `10²`, `0`, `200`, `400`, `600`, `800`, `1000`, `1200`, `1400`.

### `tool-space-interference-msr.web/images/image-1.png`
- **Provenance**: `https://www.microsoft.com/en-us/research/wp-content/uploads/2025/09/image-1.png`. **Figura 3**. 104.937 bytes.
- **Depiction**: gráfico de dispersión titulado **"Average Tool Call Output Lengths by Tool"**. Eje horizontal: **"Tool (index, sorted)"**, de 0 a ~1.312. Eje vertical logarítmico: **"Average Tool Call Output Length (tokens) (log scale)"**, de 10⁰ a 10⁶. La nube de puntos azules sube de forma suave y continua desde 1 token hasta ~10⁴ alrededor del índice 1.250, y después se dispara: los últimos puntos escalan a 10⁵ y más, cambiando de azul a verde, amarillo y rojo. Un punto rojo solitario arriba de todo marca el máximo. Dos líneas horizontales punteadas: la inferior en 128k y la superior en 400k, identificadas en la leyenda inferior derecha. Recuadro violeta claro arriba a la izquierda con las estadísticas.
- **Why it matters**: es el argumento visual de "una sola llamada a herramienta te puede volar la ventana de contexto". La distancia entre la mediana (98 tokens) y el máximo (557.766) es de casi cuatro órdenes de magnitud y el gráfico la hace evidente de un vistazo. Buena figura para una slide sobre por qué conviene paginar o resumir respuestas de herramientas.
- **Transcribed text**: `Average Tool Call Output Lengths by Tool` · recuadro: `Total tools: 1312` / `Mean: 4,431 tokens` / `Median: 98 tokens` / `Min: 0 tokens` / `Max: 557,766 tokens` · eje Y: `Average Tool Call Output Length (tokens) (log scale)` · eje X: `Tool (index, sorted)` · leyenda: `GPT-4o Context Limit (128k)` / `GPT-5 Context Limit (400k)`.

### `tool-space-interference-msr.web/images/input_schema_depth-scaled.png`
- **Provenance**: `https://www.microsoft.com/en-us/research/wp-content/uploads/2025/09/input_schema_depth-scaled.png`. **Figura 4**. 87.924 bytes.
- **Depiction**: gráfico de dispersión cuadrado titulado **"Tool Input Schema Max Property Depth"**. Eje horizontal: **"Tool (index, sorted)"**, de 0 a ~12.643. Eje vertical **lineal** con marcas enteras de 0 a 20: **"Max Property Schema Depth"**. La estructura es de mesetas horizontales: una barra azul en profundidad 0 (índices 0 a ~1.400), un punto aislado en 1 (~1.400), una **barra larguísima en profundidad 2** que cubre de ~1.700 a ~9.500 —la enorme mayoría del catálogo—, luego 3 (~9.500-11.300), 4 (~11.300-12.000), 5, 6, y a partir de ahí puntos sueltos cada vez más aislados en 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 y finalmente **un único punto rojo en 20**. Los colores van de azul a rojo con la profundidad. Recuadro violeta claro arriba a la izquierda.
- **Why it matters**: es la figura que el deck **debería** haber usado si quería hablar de complejidad de parámetros con fuente real. Ojo con lo que dice y lo que no: mide **profundidad de anidamiento del esquema**, no cantidad de parámetros, y **no la cruza contra precisión**. Sirve para "la mayoría de las herramientas son planas, pero existen monstruos de 20 niveles", no para "más parámetros = menos precisión".
- **Transcribed text**: `Tool Input Schema Max Property Depth` · recuadro: `Total Tools: 12643` / `Mean: 2.24` / `Median: 2.00` / `Std: 1.38` / `Min: 0.00` / `Max: 20.00` · eje Y: `Max Property Schema Depth` con marcas `0`–`20` · eje X: `Tool (index, sorted)` con marcas `0`, `2000`, `4000`, `6000`, `8000`, `10000`, `12000`.

### `tool-space-interference-msr.web/images/ToolSpaceInterference-BlogHeroFeature-1400x788-1-1024x576.jpg`
- **Provenance**: hero image del post. 42.879 bytes.
- **Depiction**: imagen decorativa apaisada con un degradado que va de azul (izquierda) a violeta (centro) a rosa salmón (derecha). Tres íconos de línea blanca, equiespaciados: un **globo terráqueo con una lupa** superpuesta (búsqueda en internet), un **nodo central conectado a seis nodos menores** por líneas radiales (conectividad de red), y una **lista de tareas** de tres renglones, el primero con un cuadrado vacío y los dos siguientes con tildes (gestión de tareas).
- **Why it matters**: puramente decorativa. Podría servir de fondo de una slide de sección sobre MCP si el deck necesita imagen, pero no aporta contenido.
- **Transcribed text**: ninguno.

### `tool-space-interference-msr.web/images/avatar_user_30820_1510640389-180x180.jpg`
- **Provenance**: `alt="Portrait of Adam Fourney"`. Retrato del primer autor, sección "Meet the authors". 6.616 bytes, 180×180.
- **Depiction**: fotografía de retrato en formato cuadrado pequeño.
- **Why it matters**: ninguna para la clase, salvo atribución de autoría.
- **Transcribed text**: ninguno.

### `tool-space-interference-msr.web/images/Generated-Image-September-02-2025-4_23PM-180x180.jpeg`
- **Provenance**: `alt="Portrait of Tyler Payne"`. Retrato del segundo autor. 6.004 bytes, 180×180. El nombre del archivo ("Generated-Image-September-02-2025") sugiere un retrato generado o procesado automáticamente.
- **Depiction**: fotografía de retrato en formato cuadrado pequeño.
- **Why it matters**: ninguna.
- **Transcribed text**: ninguno.

### `tool-space-interference-msr.web/images/thumbnail_MayaMurad_Square_LowRes_Desat-180x180.jpg`
- **Provenance**: `alt="Portrait of Maya Murad"`. Retrato de la tercera autora. 4.952 bytes, 180×180.
- **Depiction**: fotografía de retrato cuadrada, desaturada (según el nombre del archivo, "LowRes_Desat").
- **Why it matters**: ninguna.
- **Transcribed text**: ninguno.

### `tool-space-interference-msr.web/images/saleema.profile-scaled.jpg`
- **Provenance**: `alt="Portrait of Saleema Amershi"`. Retrato de la cuarta autora. 651.308 bytes — el asset más pesado de la captura, servido sin redimensionar pese a mostrarse a 180×180.
- **Depiction**: fotografía de retrato en alta resolución.
- **Why it matters**: ninguna para la clase. Anecdóticamente, es un ejemplo de la misma clase de descuido de ingeniería que el artículo denuncia en los servidores MCP: servir un asset enorme donde hace falta uno chico.
- **Transcribed text**: ninguno.

### `tool-space-interference-msr.web/images/RE1Mu3b.png`
- **Provenance**: `https://uhf.microsoft.com/images/microsoft/RE1Mu3b.png`, `alt="Microsoft"`. Logo de la barra de navegación corporativa. 4.054 bytes.
- **Depiction**: logotipo de Microsoft — el cuadrado de cuatro colores seguido de la palabra "Microsoft".
- **Why it matters**: ninguna. Cromo del sitio.
- **Transcribed text**: `Microsoft`.

### `tool-space-interference-msr.web/images/msr-ai-2x.png`
- **Provenance**: `https://www.microsoft.com/en-us/research/wp-content/uploads/2020/07/msr-ai-2x.png`, `alt=""`. Ícono de la sección "Research Areas", junto al enlace "Artificial intelligence". 764 bytes.
- **Depiction**: ícono diminuto del área de investigación de inteligencia artificial de MSR.
- **Why it matters**: ninguna. Decoración de la interfaz.
- **Transcribed text**: ninguno legible al tamaño del ícono.

## Raw / preserved excerpts

**Apertura del artículo (verbatim):**

> This year we've seen remarkable advances in agentic AI, including systems that conduct deep research, operate computers, complete substantial software engineering tasks, and tackle a range of other complex, multi-step goals. In each case, the industry relied on careful vertical integration: tools and agents were co-designed, co-trained, and tested together for peak performance. For example, OpenAI's recent models presume the availability of web search and document retrieval tools. Likewise, the prompts and actions of Magentic-One are set up to make hand-offs easy—for example, allowing the WebSurfer agent to pass downloaded files to the Coder agent. But as agents proliferate, we anticipate strategies relying heavily on vertical integration will not age well. Agents from different developers or companies will increasingly encounter each other and must work together to complete tasks, in what we refer to as a *society of agents*. These systems can vary in how coordinated they are, how aligned their goals are, and how much information they share. Can heterogenous agents and tools cooperate in this setting, or will they hinder one another and slow progress?

**Definición del término (verbatim):**

> Tool-space interference describes situations where otherwise reasonable tools or agents, when co-present, reduce end-to-end effectiveness. This can look like longer action sequences, higher token cost, brittle recovery from errors, or, in some cases, task failure.

**El ejemplo de encuadre — Magentic-One + GitHub (verbatim):**

> Consider MCP as a means for extending Magentic-One, a generalist multi-agent system we released last year, to cover more software engineering tasks. Magentic-One ships with agents to write code, interact with the computer terminal, browse the web, and access local files. To help Magentic-One navigate version control, find issues to solve, and make pull requests, we could add an agent equipped with the GitHub MCP Server. However, now each time the team encounters a task involving GitHub, it must choose whether to visit github.com in the browser, execute a git command at the command line, or engage the GitHub MCP server. As the task progresses, agent understanding of state can also diverge: changing the branch in the browser won't change the branch in the terminal, and an authorized MCP tool does not imply authorization in the browser. Thus, while any single agent might complete the task efficiently, the larger set of agents might misunderstand or interfere with one another, leading to additional rounds of debugging, or even complete task failure.

**Metodología de la encuesta (verbatim):**

> To better understand the potential interference patterns and the current state of the MCP ecosystem, we conducted a survey of MCP servers listed on two registries: smithery.ai and Docker MCP Hub. Smithery is an MCP Server registry with over 7,000 first-party and community-contributed servers, which we sampled from the Smithery API. Likewise, Docker MCP Hub is a registry that distributes MCP servers as Docker images, and we manually collected popular entries. We then launched each server for inspection. After excluding servers that were empty or failed to launch, and deduplicating servers with identical features, 1,470 servers remained in our catalog.

**El MCP Interviewer (verbatim):**

> To automate the inspection of running MCP servers, we developed an MCP Interviewer tool. The MCP Interviewer begins by cataloging the server's tools, prompts, resources, resource templates, and capabilities. From this catalog we can compute descriptive statistics such as the number of tools, or the depth of the parameter schemas. Then, given the list of available tools, the interviewer uses an LLM (in our case, OpenAI's GPT-4.1) to construct a functional testing plan that calls each tool at least once, collecting outputs, errors, and statistics along the way. Finally, the interviewer can also grade more qualitative criteria by using an LLM to apply purpose-built rubrics to tool schemas and tool call outputs.

**Limitación admitida (verbatim):**

> While our survey provides informative initial results, it also faces significant limitations, the most obvious of which is authorization: many of the most popular MCP servers provide access to services that require authorization to use, hindering automated analysis. We are often still able to collect static features from these servers but are limited in the functional testing that can be done.

**"One-size fits all (but some more than others)" — el tema de fondo (verbatim):**

> So, what does our survey of MCP servers tell us about the MCP ecosystem? We will get into the numbers in a moment, but as we contemplate the statistics, there is one overarching theme to keep in mind: MCP servers do not know which clients or models they are working with, and present one common set of tools, prompts, and resources to everyone. However, some models handle long contexts and large tool spaces better than others (with diverging hard limits), and respond quite differently to common prompting patterns. […] So already, this places MCP at a disadvantage over vertical integrations that optimize to the operating environment.

**Sección "Tool count" (verbatim):**

> While models generally vary in their proficiency for tool calling, the general trend has been that performance drops as the number of tools increases. For example, OpenAI limits developers to 128 tools, but recommends that developers: "*Keep the number of functions small for higher accuracy. Evaluate your performance with different numbers of functions. Aim for fewer than 20 functions at any one time, though this is just a soft suggestion.*" While we expect this to improve with each new model generation, at present, large tool spaces can lower performance by up to 85% for some models. Thankfully, the majority of servers in our survey contain four or fewer tools. But there are outliers: the largest MCP server we cataloged adds 256 distinct tools, while the 10 next-largest servers add more than 100 tools each. Further down the list we find popular servers like Playwright-MCP (29 tools, at the time of this writing), and GitHub MCP (91 tools, with subsets available at alternative endpoint URLs), which might be too large for some models.

**Sección "Response length" (verbatim):**

> Tools are generally called in agentic loops, where the output is then fed back into the model as input context. Models have hard limits on input context, but even within these limits, large contexts can drive costs up and performance down, so practical limits can be much lower. MCP offers no guidance on how many tokens a tool call can produce, and the size of some responses can come as a surprise. In our analysis, we consider the 2,443 tool calls across 1,312 unique tools that the MCP Interviewer was able to call successfully during the active testing phase of server inspection. While a majority of tools produced 98 or fewer tokens, some tools are extraordinarily heavyweight: the top tool returned an average of 557,766 tokens, which is enough to swamp the context windows of many popular models like GPT-5. Further down the list, we find that 16 tools produce more than 128,000 tokens, swamping GPT-4o and other popular models. Even when responses fit into the context window length, overly long responses can significantly degrade performance (up to 91% in one study), and limit the number of future calls that can be made. Of course, agents are free to implement their own context management strategies, but this behavior is left undefined in the MCP specification and server developers cannot count on any particular client behavior or strategy.

**Sección "Tool parameter complexity" (verbatim, completa — nótese que no hay ninguna cifra de precisión por cantidad de parámetros):**

> Mirroring the challenges from increasing the number of tools, increasing the complexity of a tool's parameter space can also lead to degradation. For example, while MCP tools can take complex object types and structures as parameters, composio found that flattening the parameter space could improve tool-calling performance by 47% compared to baseline performance. In our analysis, we find numerous examples of deeply nested structure—in one case, going 20 levels deep.

**Pie de la Figura 4 (verbatim):**

> Figure 4: The maximum depth of each tool's input properties schema. A depth of 0 indicates a tool with no properties. A depth of 1 indicates a tool with named properties but no annotations (e.g., no description or type). A depth of 2 indicates a tool with named and annotated properties. A depth of 3+ indicates a tool with structured properties that have additional nested annotations.

**Sección "Namespacing issues and naming ambiguity" (verbatim):**

> Another often-cited issue with the current MCP specification is the lack of a formal namespace mechanism. If two servers are registered to the same agent or application, and the servers have tool names in common, then disambiguation becomes impossible. Libraries like the OpenAI Agents SDK raise an error under this circumstance. Clients, like Claude Code, prefix tool names with unique identifiers to work around this issue. In our analysis of MCP servers, we found name collisions between 775 tools. The most common collision was "search", which appears across 32 distinct MCP servers.

> Even when names are unique, they can be semantically similar. If these tools behave similarly, then the redundancy may not be immediately problematic, but if you are expecting to call a particular tool then the name similarities raise the potential for confusion.

**Sección "Errors and error messages" (verbatim):**

> Like all software libraries, MCP will occasionally encounter error conditions. In these cases, it is important to provide sufficient information for the agent to handle the error and plan next steps. In our analysis, we found this was not always the case. While MCP provides an "IsError" flag to signal errors, we found that it was common for servers to handle errors by returning strings while leaving this flag set to false, signaling a normal exit. Out of 5,983 tool call results with no error flag, GPT-4.1 judged that 3,536 indicated errors in their content. More worrisome: the error messages were often of low quality. For instance, one tool providing web search capabilities failed with the string "error: job," while another tool providing academic search returned "Please retry with 0 or fewer IDs."

**Sección "Resource sharing conventions" (verbatim):**

> Finally, in addition to tools, MCP allows servers to share resources and resource templates with clients. In our survey, only 112 (7.6%) servers reported any resources, while 74 (5%) provided templates. One potential reason for low adoption is that the current MCP specification provides limited guidance for when resources are retrieved, or how they are incorporated into context. One clearcut situation where a client might retrieve a resource is in response to a tool returning a resource_link as a result — but only 4 tools exhibited this behavior in our survey (arguably, this would be the ideal behavior for tools that return very long, document-like responses, as outlined earlier).

> Conversely, a whole different set of issues arises when there is a need to share resources from the client to the server. Consider for example a tool that provides some analysis of a *local* PDF file. In the case of a local MCP server utilizing STDIO transport, a local file path can be provided as an argument to the tool, but no similar conventions exist for delivering a local file to a remote MCP server. These issues are challenging enough when implementing a single server. When multiple tools or servers need to interact within the same system, the risk of interoperability errors compounds.

**Recomendaciones a los desarrolladores del protocolo (verbatim):**

> We recognize the advantages of keeping MCP relatively lightweight, avoiding being overly prescriptive in an environment where AI models and use cases are rapidly changing. However, a few small recommendations are warranted. First, we believe MCP should be extended to include a specification for client-provided resources so that tools on remote servers have a mechanism for operating on specified local files or documents. This would more effectively position MCP as a clearinghouse for resources passed between steps of agentic workflows. The MCP specification would also benefit from taking a more opinionated stance on when resources are retrieved and used overall.

> Likewise, we believe MCP should quickly move to provide formal namespaces to eliminate tool name collisions. If namespaces are hierarchical, then this also provides a way of organizing large catalogs of functions into thematically related tool sets. Tool sets, as an organizing principle, are already showing some promise in GitHub MCP Server's dynamic tool discovery, and VS Code's tool grouping (with virtual tools), where agents or users can enable and disable tools as needed. In the future, a standardized mechanism for grouping tools would allow *clients* to engage in hierarchical tool-calling, where they first select a category, then select a tool, without needing to keep all possible tools in context.

**Recomendaciones a los desarrolladores de servidores (verbatim):**

> While our MCP Interviewer tool can catalog many outward-facing properties of MCP servers, developers are often in a much better position to characterize the nature of their tools. To this end, we believe developers should publish an MCP Server card alongside their servers or services, clearly outlining the runtime characteristics of the tools (e.g., the expected number of tokens generated, or expected latency of a tool call). Ideally developers should also indicate which models, agents and clients the server was tested with, how the tools were tested (e.g., provide sample tasks), list any known incompatibilities, and be mindful of limitations of various models throughout development.

**Recomendaciones a los desarrolladores de clientes (verbatim):**

> Client developers have the opportunity to experiment with various mitigations or optimizations that might help the average MCP server work better for a given system or environment. For example, clients could cache tool schemas, serving them as targets for prompt optimizations, or as an index for RAG-like tool selection approaches. To this end, Anthropic recently reported using a tool testing agent to rewrite the prompts of defective MCP servers, improving task completion time by 40%. Likewise, rather than waiting for the protocol to evolve, clients could take proactive steps to resolve name collisions— for example, generating namespaces from server names—and could reduce token outputs by summarizing or paginating long tool results.

**Recomendaciones a los marketplaces (verbatim):**

> Finally, we see an opportunity for marketplaces to codify best-practices, spot compatibility issues at a global level, and perhaps centralize the generation and serving of model or agent-specific optimizations. Mirroring how a market like PyPI distributes Python wheels matched to a developer's operating system or processor, an MCP marketplace could serve tool schemas optimized for a developer's chosen LLM, agent or client library. We are already seeing small steps in this direction, with registries like Smithery providing customized launch configurations to match users' clients.

**Conclusión (verbatim):**

> In summary, the MCP ecosystem offers significant value for AI agent development, despite some early growing pains. Grounded in insights from the MCP Interviewer and our survey of live servers, the evidence is clear: horizontal integration is expanding capability, yet it also exposes forms of toolspace interference that can erode end to end effectiveness. Anticipating rapid advances in model capability and growing architectural diversity, the recommendations provided here aim to ensure that protocol, server, client, and marketplace developers are well positioned to adapt and thrive. Key steps include implementing formal namespaces to eliminate collisions, enhancing protocol support for client provided resources, and encouraging transparent server documentation to foster interoperability and robust development practices across the ecosystem.

**Escala del ecosistema, párrafo de contexto (verbatim):**

> Early clues have emerged from an unexpected source: namely, Model Context Protocol (MCP). Since January 2025, MCP has grown from a promising spec to a thriving market of tool servers. As an example, Zapier boasts a catalog of 30,000 tools across 7,000 services. Composio provide over 100 managed MCP servers, surfacing hundreds of tools. Hugging Face is now serving many Spaces apps over MCP, and Shopify has enabled MCP for millions of storefronts. A society of *tools* is already here, and it promises to extend agent capabilities through cross-provider horizontal integration.
