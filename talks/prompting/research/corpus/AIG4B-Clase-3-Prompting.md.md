---
source_file: AIG4B-Clase-3-Prompting.md
source_type: article
ingested_at: 2026-08-14
---

# AIG4B — Clase 3: Ingeniería de Prompts y Técnicas Avanzadas

## Provenance

- Original location: `research/articles/AIG4B-Clase-3-Prompting.md` (+ carpeta de assets `research/articles/AIG4B-Clase-3-Prompting-media/`)
- Format: Markdown — extracción 1:1 de un deck PowerPoint. El `.pptx` original vive en la raíz del Talk: `AIG4B-Clase-3-Prompting.pptx` (2,4 MB).
- Author / source (if known): la slide 1 acredita **"Paulo Veiga/Marcos Sanchez Sorondo"**. (El encargo de ingesta indicaba "Marcos Sorondo" como autor único; la slide firma a dos personas. Se preserva la redacción literal del deck.)
- Date of original (if known): "Última Modificación: **Marzo, 2026**" (slide 1). El deck se presenta como material de 2026 y cita precios "a marzo 2026".
- Curso: *Inteligencia Artificial Generativa Aplicada en Biomedicina* (AIG4B), Universidad Austral — **Clase 3**.
- Extensión: **63 slides**, 43 bloques de tabla, 201 colocaciones de imagen (133 archivos únicos).
- **Notas del orador: ninguna.** Verificado sobre el `.pptx`: hay 126 partes `notesSlide` en el paquete, pero **0 de las 63 slides contiene texto de nota real** (todas vacías o con solo el número de diapositiva). No existe guion hablado; todo lo que el deck comunica está en el cuerpo visible de las slides.

### Estructura declarada (agenda, repetida en las slides 4, 16, 21, 25, 44, 49 y 56)

| # | Módulo | Bajada |
|---|---|---|
| 1 | Fundamentos de Foundational Models | Ventana de contexto, tokens, limitaciones y modelos mentales |
| 2 | Ingeniería de Prompts Estructurada | 6 componentes, XML tags, salidas JSON y optimización por modelo |
| 3 | In-Context Learning | Zero-shot, Few-shot y Many-shot con ejemplos clínicos |
| 4 | Técnicas Avanzadas de Prompting | CoT, Self-Consistency, Extended Thinking y Prompt Chaining |
| 5 | Selección de Modelos y Costos | Framework de decisión, prompt caching, model cascading y TOON |
| 6 | Foundational Models en Medicina | Aplicaciones reales, recorrido del paciente, research biomédica y marco ético OMS |
| 7 | Resumen y Práctica | Módulos interactivos de aitutorial.dev + sistema de triage con LLM |

### Mapa de slides

| Slides | Contenido |
|---|---|
| 1 | Portada |
| 2–3 | **Vacías** (sin texto ni imágenes) |
| 4 | Agenda |
| 5–15 | Módulo 1 — Fundamentos (prompt, componentes, ventana de contexto, tokens, costo, limitaciones, alucinaciones, mitigación, modelo mental) |
| 16 | Agenda |
| 17–20 | Módulo 2 — Prompting estructurado (6 componentes, JSON Schema, XML tags, optimización por modelo) |
| 21 | Agenda |
| 22–24 | Módulo 3 — In-Context Learning (ICL, few-shot, many-shot) |
| 25 | Agenda |
| 26–43 | Módulo 4 — Técnicas avanzadas (CoT, Self-Consistency, Extended Thinking, ToT, Prompt Chaining, por qué funcionan, latencia, testing, DSPy, versionado) |
| 44 | Agenda |
| 45–48 | Módulo 5 — Selección de modelos y costos (paisaje, prompt caching, cascading) |
| 49 | Agenda |
| 50–55 | Módulo 6 — Medicina (benchmarks, recorrido del paciente, research, casos de éxito, OMS, mitigaciones) |
| 56 | Agenda |
| 57 | Módulo 7 — ¡A Practicar! (cierre) |
| **58–63** | **Bloque duplicado**: repiten exactamente las slides 42, 30, 31, 32, 33 y 34 — después del cierre |

---

## Key claims

Recorrido de las 63 slides en orden. Los números entre corchetes indican la slide de origen.

### Módulo 1 — Fundamentos de Foundational Models (slides 5–15)

- **[5] Definición de prompt:** "Un prompt es la instrucción, pregunta o entrada textual que proporcionas a un Modelo de Lenguaje Grande (LLM) para que genere una respuesta."
- **[5]** Tres funciones del prompt, en tabla:

| Medio de Comunicación | Define Tarea y Contexto | Calidad = Resultado |
|---|---|---|
| La interfaz principal entre el humano y la IA. | Establece qué hacer y bajo qué condiciones. | Un mejor prompt produce respuestas más útiles y precisas. |

- **[5] Analogía central del deck:** "Un prompt es como una receta para un chef experto — cuanto más clara y específica, mejor el resultado."
- **[6] Qué se guarda en un prompt** — cuatro componentes que compiten por la ventana:
  - *System prompt*: "Instrucciones base del sistema que definen el comportamiento general del modelo."
  - *Historial de mensajes*: "Toda la conversación previa entre usuario y modelo." "Cada mensaje nuevo se concatena al historial, consumiendo espacio progresivamente (chat)."
  - *Datos inyectados*: "Archivos, resultados de búsqueda, datos de APIs externos."
  - *Respuestas del modelo*: "Sus propias respuestas previas también consumen espacio en la ventana."
- **[6] Tesis contraintuitiva:** "Más contexto no siempre es mejor: puede diluir lo importante." "El modelo no 'elige' qué leer; procesa todo el contexto junto." "Todo compite por la atención del modelo simultáneamente."
- **[7] Ventana de contexto:** "es la memoria de trabajo activa del LLM: todo lo que el modelo puede «ver» en un momento dado para generar su respuesta." "Es finita, cuando se llena, el modelo pierde acceso a la información más antigua."
- **[7] Tamaños típicos en 2026** (según el deck):

| Ventana | Modelo |
|---|---|
| 1M | GPT-5.4 (OpenAI) |
| 1M | Claude Opus 4.6 (Anthropic) |
| 2M | Gemini 3 Pro (Google) |
| 10M | Llama 4 (Meta) |

  - "La carrera por ventanas más largas es la nueva frontera competitiva en 2026."
- **[8] Cuánto es 1 millón de tokens** (encuadre por analogía con Tolkien):

| 📚 ~750K tokens | 🏥 ~800K tokens |
|---|---|
| Toda la obra de Tolkien (El Hobbit + trilogía LOTR) | Años de historial clínico completo de un paciente |

- **[9] Tokens:** "Los tokens son subpalabras, no palabras completas. Por ejemplo, 'Ingeniería Biomédica' equivale a aproximadamente 4-5 tokens. El modelo procesa y factura en unidades de tokens, tanto de entrada como de salida."
- **[10] Fórmula del costo:** `Costo Total = (Tokens de Entrada × Precio Entrada) + (Tokens de Salida × Precio Salida)`
- **[10] Efecto bola de nieve:** "para que el modelo recuerde el contexto, la aplicación le tiene que reenviar la historia del chat":

| Turno | Lo que tú escribes | Lo que la app le envía al LLM (Entrada) | Lo que te cobran |
|---|---|---|---|
| Mensaje 1 | "Hola, haz un código..." | Solo tu mensaje 1. | Barato. |
| Mensaje 2 | "Ahora cámbiale esto..." | Mensaje 1 + Respuesta 1 + Mensaje 2. | Un poco más caro. |
| Mensaje 3 | "Y agrégale esto otro..." | Mensaje 1 + Resp. 1 + Mensaje 2 + Resp. 2 + Mensaje 3. | Más caro que el anterior. |

- **[11] Tarifario Anthropic** (tal como lo lista el deck):

| Modelo | Entrada ($/MTok) | Salida ($/MTok) | Otros costos |
|---|---|---|---|
| Fable 5 | $10.00 | $50.00 | Batch: $5/$25 · Cache hit: $1.00 · Solo US: ×1.1 |
| Opus 4.8 | $5.00 | $25.00 | Fast Mode: $10/$50 · Cache hit: $0.50 · Cache write 1h: $10.00 |
| Sonnet 4.6 | $3.00 | $15.00 | Cache hit: $0.30 · Cache write 1h: $6.00 |
| Haiku 4.5 | $1.00 | $5.00 | Cache hit: $0.10 · Cache write 1h: $2.00 |

  - Costos adicionales (todos los modelos): "Búsqueda web: $10 / 1,000 búsquedas"; "Ejecución de código: 50 hs gratis/día, luego $0.05/hora".
- **[11] Impacto del effort en el costo:** "El nivel de effort (esfuerzo de razonamiento) afecta el costo porque determina cuántos tokens de 'thinking' genera el modelo, y esos tokens se facturan a tarifa de salida aunque no se devuelvan en la respuesta. Opus 4.8 introdujo controles de effort (low / high / xhigh / max), y el default se movió de medium a high,". *(La frase queda cortada con coma en el original.)*
- **[12] Tres limitaciones estructurales:**

| Alucinaciones | No-Determinismo | Sesgo de Recencia |
|---|---|---|
| Predicen texto plausible, no verifican hechos. Mitigación: restringir al contexto dado + revisión humana. | El mismo prompt produce respuestas diferentes (temperature > 0). Temperature 0 = mínima creatividad; 2.0 = máxima. En producción: usar temperature baja + múltiples iteraciones. | El modelo presta más atención al inicio y al final del prompt; el contenido del medio recibe menos atención. Estrategia: instrucciones críticas al inicio, queries específicas al final. |

- **[13] Cuatro causas de alucinación:** (a) *sin acceso a hechos verificados* — "Generan el token más probable dado el contexto, lo que puede producir texto fluido pero factualmente incorrecto"; (b) *entrenamiento sesgado* — "Datos de entrenamiento incompletos o desactualizados. El modelo extrapola más allá de lo que sabe"; (c) *confianza sin verificación* — "El modelo no distingue entre lo que sabe y lo que inventa. Responde con igual seguridad en ambos casos"; (d) *presión de completado* — "El modelo siempre intenta completar el texto, incluso cuando no tiene información suficiente".
- **[14] Ocho estrategias de mitigación:** grounding en contexto ("Instruir al modelo a responder solo con el contexto dado"); dataset de evaluación ("Mínimo 50-100 casos con ground truth del dominio clínico"); métricas de alucinación ("Faithfulness score, hallucination rate, ROUGE-L"); RAG ("Inyectar únicamente información verificada y relevante por consulta"); regression testing ("Ejecutar el eval set en cada cambio de prompt"); temperature = 0 ("Minimizar aleatoriedad en tareas de extracción o clasificación"); red teaming ("Probar con casos ambiguos y contradictorios antes de producción"); self-consistency ("Generar múltiples respuestas y seleccionar por votación de mayoría"); revisión humana en el loop ("El output es siempre un borrador; el clínico valida antes de actuar").
- **[14] Regla de oro (1 de 2 en el deck):** "si no puedes medir la tasa de alucinación de tu sistema, no puedes desplegarlo en un entorno clínico."
- **[15] Modelo mental — motores de completado:**

| Cómo piensan los LLMs | Implicancia práctica |
|---|---|
| Completan patrones del entrenamiento; no "entienden" la intención humana. | Pensar en el LLM como un autocompletado muy sofisticado cambia cómo construimos los prompts. |

  - Fortaleza: "Excelente pattern matching sobre datos conocidos." · Debilidad: "Alucinan sobre patrones no vistos en el entrenamiento." · "Sin razonamiento interno: predicen el siguiente token más probable."
  - Prompt vago → "'Extrae nombre y email' → puede fallar sin patrón explícito." Prompt estructurado → dar un patrón de completado explícito (`Nombre: [campo]` / `Email: [campo]` / `De: [texto]`).

### Módulo 2 — Ingeniería de Prompts Estructurada (slides 17–20)

- **[17] Los 6 componentes de un prompt:**
  1. **Rol / Persona** — "Establece expertise y patrones de comportamiento. Ej: 'Eres un médico especialista en cardiología.'"
  2. **Contexto** — "Información de fondo relevante: datos del paciente, guías clínicas aplicables, situación específica."
  3. **Instrucciones** — "Direcciones paso a paso de qué hacer. Cuanto más específicas y detalladas, mejor el resultado."
  4. **Restricciones** — "Define límites, reglas y formato de salida. Especifica qué NO debe hacer o incluir el modelo."
  5. **Ejemplos (Few-shot)** — "Demuestra el comportamiento esperado con casos resueltos. **3-5 ejemplos suelen ser suficientes.**"
  6. **Input** — "Los datos reales a procesar: el caso concreto que el modelo debe resolver en esta llamada."
  - *(El prompt completo de 6 bloques está preservado verbatim en «Raw / preserved excerpts».)*
- **[18] Salidas estructuradas — JSON Schema.** "Schema enforcement reduces parsing errors and retries — making outputs machine-checkable." *(Única frase del deck íntegramente en inglés.)*
  - Dos enfoques: **Schema en el Prompt** — "Incluir el formato JSON directamente en las instrucciones. Más flexible, menos garantías." · **JSON Mode (API)** — "Usar `response_format: json_object`. Más fiable, garantiza estructura válida."
  - Beneficios en producción: "✓ Validación automática — Outputs verificables programáticamente"; "✓ Menos errores de parsing — Reducción de fallos en el pipeline"; "✓ Integración directa — Conectable with sistemas clínicos" *(sic, "with")*; "✓ Casos clínicos — Extracción, clasificación, reportes".
- **[19] XML tags — estructura semántica.** "Los LLMs fueron entrenados extensivamente con datos HTML/XML de la web. Los tags crean límites semánticos explícitos entre secciones, reduciendo la ambigüedad."
  - **40%** — "Reducción mínima en alucinaciones con XML + validación"
  - **60%** — "Reducción máxima reportada en algunos benchmarks"
  - "El overhead de tokens por los tags se compensa ampliamente con menos reintentos y errores."
- **[20] Optimización por modelo:**

| GPT-4 / GPT-4o | Claude (Sonnet/Opus) | Gemini 1.5 Pro |
|---|---|---|
| Mejor en structured outputs y JSON/schema compliance. Usar roles explícitos y schemas bien definidos. | Mejor en razonamiento natural, chain-of-thought y contexto largo. Usar bloques `<thinking>` y formato XML. | Mejor en ventanas de 2M tokens y multimodal. Queries al final del contexto, ideal para documentos largos y PDFs. |

  - "Un prompt óptimo para GPT-4 puede no serlo para Claude o Gemini. Probar y evaluar en cada modelo antes de llevar a producción."

### Módulo 3 — In-Context Learning (slides 22–24)

- **[22] Definición de ICL:** "Capacidad del LLM de aprender patrones a partir de ejemplos en el prompt, sin modificar sus pesos. El modelo no se re-entrena: reconoce patrones en los ejemplos y los aplica al caso nuevo."
- **[22] Los tres regímenes:**
  - *Zero-shot*: "Solo instrucción, sin ejemplos. Depende del conocimiento preentrenado del modelo."
  - *Few-shot*: "2–10 ejemplos resueltos antes del caso a resolver. **El más utilizado en producción.**"
  - *Many-shot*: "Decenas o cientos de ejemplos para tareas complecias o con alta variabilidad." *(sic, "complecias" por "complejas")*
- **[23] Buenas prácticas de few-shot:** "Incluir 2-10 ejemplos en el prompt para guiar al modelo"; "Estructura: Instrucción + Ejemplo 1 + Ejemplo 2 + ... + Caso nuevo"; "Ejemplos representativos: cubrir casos positivos, negativos y edge cases"; "Formato consistente entre todos los ejemplos"; "**3-5 ejemplos suelen ser suficientes (calidad > cantidad)**".
- **[24] Cuándo usar many-shot:** "Decenas o cientos de ejemplos, aprovechando ventanas de contexto grandes"; "Útil cuando few-shot no captura suficiente variabilidad del problema"; "Para tareas con muchas categorías (ej: 20+ diagnósticos posibles)"; "Modelo en producción: agregar ejemplos al prompt según surgen errores"; "**Es mejorar el modelo sin re-entrenarlo.**"

### Módulo 4 — Técnicas Avanzadas de Prompting (slides 26–43)

- **[26] Cuadro resumen de las cinco técnicas:**

| Chain of Thought (CoT) | Self-Consistency | Extended Thinking |
|---|---|---|
| Razonamiento paso a paso para mejorar precisión. Fuerza tokens intermedios que guían la predicción final. | Genera múltiples respuestas y selecciona por votación de mayoría. Reduce errores por no-determinismo. | Modelos Claude exponen su razonamiento interno con tags `<thinking>`. Ideal para tareas críticas y complejas. |

| Tree of Thought (ToT) | Prompt Chaining |
|---|---|
| Explora múltiples caminos de razonamiento en paralelo. Útil para problemas con múltiples soluciones posibles. | Divide tareas complejas en secuencia de prompts simples. El output de cada paso alimenta al siguiente. |

- **[27] CoT — cómo funciona:** "Mostrar al modelo el razonamiento paso a paso, no solo el resultado final. Es como pensar en voz alta." Dos vías: *instrucción directa* ("Agregar frases como «Pensemos paso a paso» o «Razona antes de responder»") y *ejemplos con razonamiento explícito* ("Mostrar ejemplos donde el proceso de resolución es visible, no solo la respuesta final").
- **[27] Impacto medido:** **70%** de "Mejora en precisión — Problemas matemáticos complejos"; **35%** de "Menos errores — Generación de código con Chain of Thought (CoT)".
- **[27] Relación CoT ↔ ICL:** "Few-Shot CoT es ICL donde los ejemplos incluyen el razonamiento explícito, no solo la respuesta. **ICL enseña qué responder; CoT enseña cómo razonar.**"
- **[28] CoT en acción** — contraste sin/con CoT sobre el cálculo de una propina; sin CoT "No se puede auditar ni depurar el razonamiento", con CoT "Razonamiento auditable. Los errores son detectables". "En diagnóstico médico: CoT produce patrones de razonamiento clínico más auditables y fiables. **Costo: mayor latencia por outputs más largos.**"
- **[29] Self-Consistency — problema y solución:** "Problema: una sola respuesta puede ser incorrecta por no-determinismo o ambigüedad del prompt. Solución: generar múltiples respuestas independientes e implementar un mecanismo de votación sobre los resultados."
  - "**5 agentes = 5× el coste, pero la precisión mejora significativamente. CoT + Self-Consistency combinados producen ganancias adicionales (Wang et al., 2022).**" *(Única cita académica formal del deck.)*
  - Cuándo usarlo: alto riesgo ("Decisiones médicas, financieras o legales donde los errores son costosos"); razonamiento complejo ("Problemas donde múltiples cadenas de pensamiento pueden divergir"); clasificación con confianza ("Tareas que requieren evaluar la confianza del modelo"); evaluación previa ("Siempre validar en tu evaluation set; **no asumir ganancias universales**").
- **[30] Self-Consistency — ejemplo con votación 2/3 → "Confianza: 67%".** Consideración de costo: "3-5 llamadas al modelo = 3-5x costo. Usar solo cuando la precisión lo justifica."
- **[31] Extended Thinking (Anthropic):** "Los modelos Claude con extended thinking exponen el proceso interno de razonamiento mediante tags `<thinking>`, habilitando capacidades avanzadas para aplicaciones críticas":

| Debugging | Calidad | Transparencia |
|---|---|---|
| Revela exactamente dónde falló el razonamiento del modelo. Los bloques `<thinking>` exponen el proceso interno paso a paso, permitiendo identificar y corregir errores sistemáticos. | Fuerza al modelo a pensar deliberadamente antes de responder. Ejemplo en análisis de contratos: analizar documento → identificar obligaciones → evaluar riesgos → generar recomendación. | Habilita audit trails completos para decisiones críticas. El contenido de thinking se almacena separadamente para compliance regulatorio y revisión clínica. |

- **[32] Extended Thinking — ejemplo clínico.** "El bloque `<thinking>` se puede guardar como trazabilidad para cumplimiento normativo (compliance) en aplicaciones clínicas."
- **[33] Tree of Thought:** "ToT extiende CoT explorando múltiples caminos de razonamiento en paralelo, como ramas de un árbol de decisión."
  - **Analogía médica (clave del deck):** "ToT es similar al diagnóstico diferencial clínico: considerar múltiples hipótesis, evaluar la evidencia disponible para cada una y descartar las menos probables."
  - Ciclo de tres pasos: *Generar ramas → Evaluar ramas → Seleccionar camino*.
  - Limitaciones: "Mayor coste computacional que CoT lineal"; "Mayor complejidad de implementación"; "Útil para problemas con múltiples soluciones posibles"; "No siempre justifica el overhead en tareas simples."
- **[34] ToT — caso clínico** (35F, sospecha de TEP). Tres ramas evaluadas:
  - *Rama A: TEP (Tromboembolismo Pulmonar)* — "Viaje largo, disnea, taquicardia → **Score Wells: 6 (alta probabilidad)**. Rama seleccionada."
  - *Rama B: Neumotórax espontáneo* — "Posible, pero sin trauma ni factores de riesgo claros. Probabilidad media-baja."
  - *Rama C: SCA (Síndrome Coronario Agudo)* — "Dolor torácico compatible, pero perfil joven sin factores cardiovasculares. Descartado."
  - Resultado: "Diagnóstico prioritario: TEP → Recomendación: angioTC pulmonar urgente → Transparencia: razonamiento auditable para decisión clínica."
- **[35] Prompt Chaining:** "Dividir una tarea compleja en una secuencia de prompts simples, donde el output de un paso alimenta al siguiente. Cada paso puede ser más preciso al enfocarse en una sola sub-tarea. Es decir, se ejecutan varias llamadas en vez de una lo cual incre" *(la frase queda truncada en el original)*.
  - Pipeline médico de triage en 5 pasos: (1) Ticket / consulta recibida → (2) Clasificar urgencia: alta / media / baja → (3) Extraer detalles clínicos relevantes → (4) Buscar en base de conocimiento (RAG) → (5) Generar respuesta estructurada.
  - Cuatro beneficios: *Debugging* ("Se identifica exactamente en qué paso ocurre el fallo"); *Resiliencia* ("Pasos fallidos se reintentan de forma independiente"); *Optimización* ("Cada prompt se optimiza para su tarea específica"); *Escalabilidad* ("Escala a pipelines de producción complejos").
  - **"Prompt Chaining convierte tareas imposibles en secuencias manejables. Es la base de los agentes de IA modernos."**
- **[36] Prompt Chaining — trade-offs.** Ventajas: "Cada paso es simple → menos errores"; "Pasos fallidos pueden reintentarse de forma independiente"; "Más barato: solo llamar pasos costosos cuando se necesitan"; "Más fácil de evaluar y mejorar". Contras: "Mayor latencia (llamadas secuenciales)"; "Código más complejo"; "Múltiples llamadas al LLM (pero frecuentemente más barato en total)".
- **[37] Pros y contras de las cinco técnicas:**

| Técnica | Pros | Cons |
|---|---|---|
| Chain of Thought (CoT) | Razonamiento auditable; mejora precisión en diagnóstico; errores detectables | Mayor latencia y costo; poco útil para tareas simples; no garantiza corrección |
| Self-Consistency | Reduce errores por no-determinismo; aumenta confianza en decisiones críticas | Multiplica el costo (3-5x llamadas); mayor latencia |
| Extended Thinking | Razonamiento visible y auditable; ideal para tareas críticas; facilita trazabilidad | Solo en modelos Claude; mayor costo por tokens de thinking |
| Tree of Thought (ToT) | Explora múltiples caminos; mejor que CoT en planificación | Muy costoso; complejo de implementar; difícil de controlar |
| Prompt Chaining | Pasos simples y reintentables; más fácil de evaluar y mejorar | Mayor latencia total; código más complejo; múltiples llamadas al LLM |

- **[38] Por qué funcionan — la explicación mecánica del deck.** "El LLM no 'piensa': predice tokens." "Un LLM no razona internamente antes de responder. Genera el texto token a token, de izquierda a derecha, de forma autoregresiva. Cada token nuevo depende únicamente de los tokens anteriores en el contexto." "**No hay un 'motor de razonamiento' oculto. Lo que ves en la respuesta ES el razonamiento.**"
  - *Los tokens intermedios son cálculo real*: "Al escribir los pasos, el modelo genera representaciones intermedias que condicionan mejor los tokens siguientes. El razonamiento escrito actúa como **memoria de trabajo explícita**."
  - *Más contexto = mejor predicción final*: "Un razonamiento de 200 tokens guía mejor la respuesta final que un prompt de 10 tokens."
  - *Reduce el espacio de error*: "Sin CoT, el modelo debe 'saltar' directamente a la respuesta. Con CoT, cada paso intermedio reduce la incertidumbre acumulada antes de la conclusión."
  - **Analogía:** "es como pedirle a alguien que resuelva un problema matemático en su cabeza vs. que lo escriba paso a paso en papel. **El papel no lo hace más inteligente, pero sí más preciso.**"
- **[39] Por qué tardan más — presupuesto de latencia por técnica.** "Mayor calidad tiene un costo directo: más tokens generados = más tiempo de cómputo. **No es magia, es aritmética.**"

| Técnica | Latencia |
|---|---|
| Chain of Thought (CoT) | Genera 100-500 tokens de razonamiento antes de la respuesta final. Latencia: **2-5× mayor** que sin CoT. |
| Self-Consistency | Ejecuta el mismo prompt N veces (típicamente 5-10). Latencia y coste: **N×** el de una sola llamada. |
| Extended Thinking | El modelo genera un bloque `<thinking>` interno de miles de tokens antes de responder. Latencia: **puede ser 10-30 segundos** en casos complejos. |
| Prompt Chaining | Cada paso es una llamada API independiente. Un pipeline de 5 pasos tiene **5× la latencia base** más el tiempo de procesamiento entre pasos. |
| Tree of Thought (ToT) | Explora múltiples ramas de razonamiento en paralelo antes de seleccionar la mejor. Latencia: proporcional al número de ramas evaluadas, **típicamente 3-5× CoT**. |
| Testing Sistemático | Evalúa el prompt contra N casos de prueba en cada iteración. Latencia de desarrollo: proporcional al tamaño del dataset de evaluación. |

  - "Regla práctica: usar estas técnicas solo cuando la precisión justifica el coste. Para tareas simples o de baja criticidad, un prompt directo es más eficiente."
- **[40] El problema: prompts sin verificación.** Tres fallas: *evaluación subjetiva* ("'Parece que funciona bien' no es suficiente. Un prompt que funciona en 10 ejemplos puede fallar en producción con miles de casos"); *regresiones invisibles* ("Mejorar el prompt para un caso puede romper otros. Sin tests, los cambios son ciegos"); *sin baseline* ("Sin métricas de referencia, es imposible saber si un cambio mejoró o empeoró el sistema").
  - Lo que hace falta: dataset de evaluación con ground truth; métricas definidas ("Exactitud, F1, BLEU, o métricas de dominio específico (ej. sensibilidad clínica)"); versionado de prompts; testing automatizado ("Ejecutar el eval set en cada cambio, como CI/CD para código").
  - **"Un prompt sin datos de evaluación es una hipótesis sin experimento. El testing sistemático convierte la ingeniería de prompts en una disciplina reproducible."** *(Repetida idéntica en la slide 43.)*
- **[41] DSPy:** "DSPy (Declarative Self-improving Python) es un framework de Stanford que trata los prompts como parámetros optimizables, no como texto fijo. En lugar de escribir prompts a mano, defines el comportamiento deseado y DSPy los optimiza automáticamente contra un dataset de evaluación. Creado por **Omar Khattab** (Stanford NLP). Disponible en: **dspy.ai**"
  - Cuatro pasos: (1) *Definir el programa* — "Declaras módulos (ChainOfThought, ReAct, etc.) y cómo se conectan, sin escribir el prompt"; (2) *Proveer ejemplos* — "puede ser tan pequeño como **10-20 ejemplos**"; (3) *Elegir un optimizador* — "**BootstrapFewShot, MIPRO, BayesianSignatureOptimizer.** DSPy prueba variantes automáticamente"; (4) *Compilar* — "DSPy genera y evalúa prompts candidatos, seleccionando el que maximiza la métrica definida."
  - **Analogía:** "es como el backpropagation del deep learning, pero para prompts. En vez de ajustar pesos, ajusta instrucciones."

|  | Prompt manual | DSPy |
|---|---|---|
| Tiempo de iteración | Horas/días | Minutos |
| Reproducibilidad | Baja | Alta |
| Escala a nuevos modelos | Manual | Automática |
| Requiere expertise en prompting | Sí | Reducido |

- **[42] Versionado de prompts:** "**Un prompt es código.** Debe tratarse con el mismo rigor que el código fuente: control de versiones, historial de cambios, rollback ante regresiones."
  - Por qué versionar: *trazabilidad* ("Saber exactamente qué prompt generó qué output en producción. Crítico para auditorías clínicas y regulatorias"); *rollback seguro* ("Si una nueva versión degrada las métricas, revertir en segundos al prompt anterior").
  - Herramientas: **Git para prompts** ("Guardar prompts en archivos .txt o .md versionados en Git. Simple y efectivo para equipos pequeños"); **LangSmith (LangChain)** ("Plataforma de observabilidad: traza cada llamada LLM, versiona prompts y compara métricas entre versiones"); **PromptLayer** ("Logging y versionado de prompts con dashboard de métricas. Integración directa con OpenAI y Anthropic"); **A/B Testing** ("Comparar dos versiones del prompt en producción con tráfico real antes de hacer el cambio definitivo"); **Weights & Biases (W&B)** ("Usado en ML tradicional, ahora con soporte para experimentos de prompts y evaluación de LLMs").
- **[43] Datos y testing sistemático.** Construir el eval set en 4 pasos: (01) *Recolectar casos reales* — "**Mínimo 50-100 ejemplos** representativos del problema. Incluir casos edge y casos difíciles deliberadamente"; (02) *Definir ground truth* — "Respuestas esperadas anotadas por expertos del dominio (ej. médicos para aplicaciones clínicas)"; (03) *Estratificar por dificultad* — "Separar en fácil / medio / difícil. Un buen prompt debe rendir bien en todos los estratos"; (04) *Separar train / eval / test* — "**Nunca optimizar el prompt sobre el test set.** Usar eval para iterar, test solo para la evaluación final."
  - Pipeline de testing: 🔁 *Eval automatizado* — "Script que ejecuta el prompt sobre todo el eval set y calcula métricas automáticamente. **Debe correr en < 5 minutos** para no frenar la iteración"; 📏 *Métricas por tarea* — "Clasificación: accuracy, F1, AUC. Generación: BLEU, ROUGE, BERTScore. Clínico: sensibilidad, especificidad, valor predictivo"; 🚨 *Regression tests* — "Suite de casos críticos que NUNCA deben fallar. Si el prompt los rompe, el cambio se rechaza automáticamente."
  - **Regla de oro (2 de 2):** "si no puedes medir la mejora, no puedes saber si mejoraste. **El eval set es tan importante como el prompt mismo.**"

### Módulo 5 — Selección de Modelos y Costos (slides 45–48)

- **[45] El paisaje de modelos:** "No existe un modelo universal. La elección depende de la tarea, el volumen, el contexto necesario y el presupuesto. **Elegir mal puede multiplicar los costos por 10x o degradar la calidad.**"

| Modelo | Contexto | Costo (entrada/salida por 1M tokens) | Mejor para |
|---|---|---|---|
| GPT-4o | 128K | $2.50 / $10.00 | Razonamiento complejo, salida estructurada |
| GPT-4o Mini | 128K | $0.15 / $0.60 | Tareas simples, alto volumen |
| Claude Sonnet 4.6 | 200K | $3.00 / $15.00 | Documentos largos, análisis matizado |
| Claude Haiku 3 | 200K | $0.25 / $1.25 | Clasificación rápida, extracción simple |
| Gemini 1.5 Pro | 2M | $1.25 / $5.00 | Contexto masivo, multimodal |
| Gemini 2.0 Flash | 1M | $0.075 / $0.30 | Budget, alta velocidad |
| Llama 3.3 70B | 128K | Self-hosted ~$0.03/$0.10 | Requisitos on-premise |

  - "Precios a marzo 2026. Verificar en: openai.com/api/pricing, anthropic.com/pricing, ai.google.dev/pricing"
  - Árbol de decisión (preservado verbatim en «Raw / preserved excerpts»).
- **[46] Prompt caching — "Reducción de Costos 50-90%".**
  - Problema: "Envías la misma base de conocimiento de 50K tokens con CADA request. Sin caching, 10.000 queries × 50K tokens = 501M tokens de entrada. A $3/1M: **$1.503**."
  - Solución: "Marcar las partes reutilizables del prompt para caching. El proveedor almacena esos tokens y los reutiliza en requests posteriores."
  - Cuatro buenas prácticas: (1) "Cachear contenido estático — Bases de conocimiento, system prompts, protocolos clínicos"; (2) "No cachear input del usuario — Cambia en cada request"; (3) "Estructura: cacheable primero — Poner partes estáticas al inicio del prompt"; (4) "Monitorear hit rates — Ajustar patrones de query para maximizar hits".
  - Casos de uso en biomedicina: *protocolos clínicos* ("Mismo protocolo de 30K tokens enviado con cada consulta de triage"); *literatura médica* ("Base de artículos indexados reutilizada en múltiples queries"); *historial del paciente* ("Contexto de sesión cacheado durante la consulta").
- **[47] Prompt caching — implementación.** "El caching funciona marcando las partes estáticas del prompt con un bloque de `cache_control`. El proveedor almacena esos tokens y los reutiliza en requests posteriores sin recalcularlos."
  - Anatomía: (1) parte estática cacheable — "System prompt, base de conocimiento, protocolos clínicos. Se marca con `cache_control`"; (2) parte dinámica no cacheable — "Input del usuario, datos del paciente, query específica"; (3) hit de caché — "Si la parte estática ya fue procesada, el proveedor la reutiliza. **Costo: 10% del precio normal.**"
  - "**Ahorro típico: 70-90% en costos de entrada** para workloads con contexto repetido."
- **[48] Model cascading:** "Intentar primero con el modelo más barato/rápido. Si la confianza es baja, escalar al modelo más caro/inteligente. Reduce costos manteniendo calidad **cuando el gating de confianza es confiable**."
  - Flujo: Query entra al sistema → Modelo barato (Haiku/GPT-3.5) intenta resolver con alta confianza → ¿Confianza suficiente? → Sí: retornar respuesta (costo mínimo, latencia baja) / No: escalar a GPT-4/Sonnet ("Solo cuando realmente se necesita").
  - Cuándo usarlo: "Alto volumen de tareas similares"; "Señales de confianza claras — Algunos modelos proveen log-probabilities"; "Presión de costos con requisitos de calidad — No se puede sacrificar precisión clínica".
  - Cuándo evitarlo: "Baja latencia requerida — El cascading agrega delay por llamadas adicionales"; "Confianza difícil de medir — Sin señal confiable, el routing falla"; "Bajo volumen — La complejidad no vale la pena".

| Factor | Modelo único | Cascading |
|---|---|---|
| Precisión | Estable, predecible | Depende de la calidad del routing |
| Latencia | Menor (una llamada) | Mayor (fallback agrega llamadas) |
| Costo | Mayor por llamada | Menor en promedio si hay muchos wins baratos |
| Complejidad | Menor | Mayor (routing, monitoreo) |

### Módulo 6 — Foundational Models en Medicina (slides 50–55)

- **[50] Benchmarks clínicos (2024–2025) y modelos especializados:**
  - **Med-PaLM 2 (Google) — 86,5%**: "86.5% en MedQA. Fine-tuning médico + chain of retrieval. **Preferido sobre médicos en 8 de 9 ejes clínicos.** (2023) - **No es publico**"
  - **GPT-4o / o3 (OpenAI) — 81,4%**: "Aprueba USMLE (United States Medical Licensing Examination) con puntuaciones competitivas. **o3 supera el 90% en exámenes de medicina general (MRCGP, 2025).**" (la cifra 81,4% se rotula "GPT-4 en USMLE (5-shot)")
  - **Claude 3 Opus (Anthropic) — 62%**: "62% de precisión en diagnóstico diferencial radiológico, superando a GPT-4o y Gemini 1.5 Pro."
  - **Gemini Mosaic (Google DeepMind) — 65%**: "65% de informes de Rx de tórax evaluados como equivalentes o mejores que los de radiólogos expertos."
- **[51] Recorrido del paciente — 5 etapas con éxito documentado y futuro proyectado:**

| Etapa | Éxito documentado | Futuro |
|---|---|---|
| **1. Síntomas** — "Los LLMs triangulan urgencia y orientan al paciente antes de la consulta." | "GPT-3.5 redujo preguntas repetidas del **14,4% al 3,2%** y emociones negativas del **7,8% al 2,4%** (**2.164 pacientes**)." | "Asistentes virtuales que derivan al especialista correcto en tiempo real." |
| **2. Diagnóstico** — "Apoyo al clínico con análisis de imágenes y extracción de datos de medicación." | "MedGemma logró **81% de informes de rayos X equivalentes al clínico** y **98,7% de precisión en extracción de medicación**." | "Diagnóstico diferencial asistido integrado." |
| **3. Tratamiento** — "Automatización de notas clínicas y borradores de comunicación médica." | "ChatGLM2-6B redujo la transcripción clínica en un **80,7%**; **197 clínicos** ya utilizan borradores automáticos; **50% menos tiempo** en notas clínicas (dato agregado de múltiples implementaciones)." | "Ambient listening: notas generadas en tiempo real durante la consulta." |
| **4. Seguimiento** — "Soporte personalizado post-consulta y monitoreo de adherencia." | "GPT-4 en terapia cognitiva grupal con **244 participantes** redujo la tasa de deserción en **23 puntos**." | "Monitoreo continuo, alertas tempranas y soporte de salud mental 24/7." |
| **5. Educación y Salud Mental** — "Los LLMs simulan pacientes y apoyan la formación clínica y el bienestar mental." | "Simulación de pacientes diversos para entrenamiento médico." | "Agentes de soporte emocional 24/7 y entornos de simulación clínica adaptativos para residentes." |

  - Fuentes citadas: "Frontiers in Digital Health (2025) — LLMs in real-world clinical workflows · MedGemma, Google DeepMind (2025) · Nature Medicine (2025) — Reliability of LLMs as medical assistants · WHO — Ethics & Governance of AI for Health: LMMs (2024)"
- **[52] Research biomédica — 4 etapas:**

| Etapa | Éxito documentado | Futuro |
|---|---|---|
| **Hipótesis y Literatura** — "Los LLMs aceleran la revisión de literatura y la generación de hipótesis a escala." | "BioGPT extrae relaciones gen-enfermedad de PubMed; **Elicit supera 1M de búsquedas de revisión sistemática**." | "Agentes que generan hipótesis falsificables a partir del corpus completo de literatura biomédica." |
| **Target y Diseño Molecular** — "Los LLMs predicen estructuras proteicas y optimizan candidatos a fármacos." | "**AlphaFold predijo estructuras de 200M+ proteínas**; **ISM001-055 (Insilico Medicine) es el primer fármaco diseñado con IA en Fase II** (fibrosis pulmonar)." | "Diseño de novo optimizado para eficacia, toxicidad y manufacturabilidad simultáneamente." |
| **Preclínica y Validación** — "Los LLMs combinan datos multimodales para predecir indicaciones y contraindicaciones." | "**TxGNN (Harvard) predice indicaciones para 17.000 enfermedades**; Recursion Pharmaceuticals integra LLMs con microscopía." | "Gemelos digitales celulares que reducen la necesidad de ensayos en animales." |
| **Ensayos Clínicos** — "Los LLMs simplifican el reclutamiento y automatizan la gestión de protocolos." | "GPT-4 mejora el reclutamiento simplificando criterios de elegibilidad (**Nature Medicine, 2024**); matching de pacientes en **Mayo Clinic** con NLP. Detección automática de interacciones medicamentosas en sistemas de HCE." | "Protocolos adaptativos por IA, análisis intermedio automatizado y reportes regulatorios generados automáticamente." |

  - Fuentes citadas: "BioGPT, Microsoft Research (2022) · AlphaFold 2/3, DeepMind (2022/2024) · ESMFold, Meta AI (2022) · Insilico Medicine — ISM001-055 Fase II · TxGNN, Harvard (Nature Medicine, 2024) · Recursion Pharmaceuticals · Consensus · Elicit"
- **[53] Casos de éxito — dónde se aplica hoy.** "Evidencia clínica real de implementaciones en entornos hospitalarios y de atención primaria documentadas entre 2023 y 2025."

| Documentación Clínica | Diagnóstico y Soporte Clínico | Comunicación con Pacientes | Educación y Salud Mental |
|---|---|---|---|
| 50% menos tiempo en notas clínicas<br>80,7% de reducción en transcripción (ChatGLM2-6B)<br>197 clínicos usan borradores automáticos en atención primaria, gastroenterología y hepatología | MedGemma (Google): 81% de informes de rayos X con decisiones equivalentes<br>98,7% de precisión en extracción de datos de medicación<br>Detección automática de interacciones medicamentosas | 2.164 pacientes atendidos vía GPT-3.5 en recepción ambulatoria<br>Preguntas repetidas: 14,4% → 3,2%<br>Emociones negativas: 7,8% → 2,4% | GPT-4 en terapia cognitiva grupal: 244 participantes, deserción cayó 23 puntos<br>Simulación de pacientes diversos para entrenamiento médico<br>Cadena de razonamiento paso a paso para el aprendizaje clínico |

- **[54] Oportunidades vs. riesgos — Marco de la OMS para Grandes Modelos Multimodales (2024):**

| Oportunidades | Riesgos (OMS) |
|---|---|
| **Democratizar el acceso** — "Información médica personalizada para pacientes y cuidadores, también en zonas de baja cobertura sanitaria." | **Alucinaciones y desinformación** — "Respuestas plausibles pero falsas que pueden parecer autoritativas, con consecuencias graves en contextos clínicos." |
| **Liberar tiempo clínico** — "Automatización de notas, registros electrónicos y traducción médica, reduciendo la carga administrativa." | **Sesgo y equidad** — "Datos de entrenamiento sesgados hacia países de altos ingresos, lo que puede perpetuar desigualdades en salud." |
| **Acelerar la investigación** — "Análisis de grandes volúmenes de datos, diseño de fármacos y revisión de literatura a escala." | **Privacidad y datos sensibles** — "Cumplimiento de normativas de protección de datos (RGPD), consentimiento informado y anonimización robusta." |
| **Mejorar la educación** — "Simulación adaptativa, razonamiento paso a paso y escenarios clínicos virtuales para profesionales en formación." | **Dependencia tecnológica** — "Riesgo de degradación de habilidades clínicas y **automation bias** cuando el médico delega en exceso al modelo." |

- **[55] Mitigaciones clave y preguntas abiertas.**
  - Mitigaciones que funcionan: (01) *Human-in-the-loop* — "Supervisión humana obligatoria en todas las implementaciones clínicas exitosas documentadas. **Sin excepción**"; (02) *RAG + Fine-tuning local* — "Retrieval-augmented generation con datos específicos del entorno clínico local"; (03) *Monitoreo continuo* — "Evaluación pre/post intervención, encuestas de usabilidad y métricas de calidad clínica de forma sistemática"; (04) *Gobernanza por etapa* — "La OMS propone regulación diferenciada para **desarrollo, provisión y despliegue** de los modelos en salud."
  - Para reflexionar:
    - *Escasez de evidencia robusta* — "**Solo 4 estudios (2024–2025) cumplen criterios rigurosos de implementación real clínica.** La mayor parte de la evidencia es observacional o en entornos controlados."
    - *La brecha de uso es real* — "**Precisión del LLM solo: 94,9%. Uso por el público general sin guía: <34,5%.** El modelo no es el único factor; el contexto de uso importa tanto como la tecnología."
    - *¿Quién responde cuando falla?* — "La OMS exige marcos de responsabilidad claros para cuando un LMM cause daño. **Hoy esa pregunta sigue sin respuesta regulatoria definitiva en la mayoría de países.**"
    - *Los 6 principios OMS* — "**Autonomía · Bienestar · Transparencia · Responsabilidad · Equidad · Sostenibilidad.** Un marco ético ineludible para cualquier despliegue en salud."
  - Fuentes: "WHO (2024), Frontiers in Digital Health (2025), Nature Medicine (2025), PMC Reviews"

### Módulo 7 — Resumen y Práctica (slide 57)

- **[57] ¡A Practicar!** "Completa los siguientes módulos interactivos en aitutorial.dev. **Tiempo estimado: 45-60 minutos.**"

| Módulo | URL | Contenido |
|---|---|---|
| Foundational Models Fundamentals | `aitutorial.dev/prompting/llm-foundamentals` | Ventana de contexto, tokens, limitaciones y modelo mental del completado. |
| Técnicas Avanzadas de Prompting | `aitutorial.dev/prompting/advanced-techniques` | CoT, Self-Consistency, Extended Thinking y Prompt Chaining aplicados. |
| Structured Prompt Engineering | `aitutorial.dev/prompting/structured-prompt-engineering` | Los 6 componentes, XML tags y salidas JSON en la práctica. |
| Prompt Optimization & Testing | `aitutorial.dev/prompting/prompt-optimization-and-testing` | Evaluar, iterar y llevar prompts a producción de forma rigurosa. |

### Slides 58–63 — bloque duplicado

Repiten sin variación el contenido de slides anteriores: **58 = 42** (Versionado de Prompts), **59 = 30** (Self-Consistency: Ejemplo), **60 = 31** (Extended Thinking), **61 = 32** (Extended Thinking: Ejemplo), **62 = 33** (Tree of Thought), **63 = 34** (ToT: Ejemplo). Quedan *después* de la slide de cierre (57). No aportan claims nuevos.

---

## Definitions and terminology

Con la redacción del propio deck.

| Término | Definición del deck | Slide |
|---|---|---|
| **Prompt** | "La instrucción, pregunta o entrada textual que proporcionas a un Modelo de Lenguaje Grande (LLM) para que genere una respuesta." | 5 |
| **System prompt** | "Instrucciones base del sistema que definen el comportamiento general del modelo." | 6 |
| **Historial de mensajes** | "Toda la conversación previa entre usuario y modelo." | 6 |
| **Datos inyectados** | "Archivos, resultados de búsqueda, datos de APIs externos." | 6 |
| **Ventana de contexto** | "La memoria de trabajo activa del LLM: todo lo que el modelo puede «ver» en un momento dado para generar su respuesta." | 7 |
| **Token** | "Subpalabras, no palabras completas. Por ejemplo, 'Ingeniería Biomédica' equivale a aproximadamente 4-5 tokens." | 9 |
| **Alucinación** | "Predicen texto plausible, no verifican hechos." / "Generan el token más probable dado el contexto, lo que puede producir texto fluido pero factualmente incorrecto." | 12, 13 |
| **No-determinismo** | "El mismo prompt produce respuestas diferentes (temperature > 0)." | 12 |
| **Temperature** | "Temperature 0 = mínima creatividad; 2.0 = máxima." | 12 |
| **Sesgo de recencia** | "El modelo presta más atención al inicio y al final del prompt; el contenido del medio recibe menos atención." | 12 |
| **Motor de completado** (modelo mental) | "Completan patrones del entrenamiento; no 'entienden' la intención humana… un autocompletado muy sofisticado." | 15 |
| **Grounding en contexto** | "Instruir al modelo a responder solo con el contexto dado." | 14 |
| **RAG (Retrieval-Augmented Generation)** | "Inyectar únicamente información verificada y relevante por consulta." | 14 |
| **Red teaming** | "Probar con casos ambiguos y contradictorios antes de producción." | 14 |
| **Los 6 componentes de un prompt** | Rol/Persona · Contexto · Instrucciones · Restricciones · Ejemplos (Few-shot) · Input | 17 |
| **JSON Mode (API)** | "Usar `response_format: json_object`. Más fiable, garantiza estructura válida." | 18 |
| **Schema en el Prompt** | "Incluir el formato JSON directamente en las instrucciones. Más flexible, menos garantías." | 18 |
| **XML tags** | "Los tags crean límites semánticos explícitos entre secciones, reduciendo la ambigüedad." | 19 |
| **In-Context Learning (ICL)** | "Capacidad del LLM de aprender patrones a partir de ejemplos en el prompt, sin modificar sus pesos." | 22 |
| **Zero-shot** | "Solo instrucción, sin ejemplos. Depende del conocimiento preentrenado del modelo." | 22 |
| **Few-shot** | "2–10 ejemplos resueltos antes del caso a resolver. El más utilizado en producción." | 22 |
| **Many-shot** | "Decenas o cientos de ejemplos para tareas comple[j]as o con alta variabilidad." | 22 |
| **Chain of Thought (CoT)** | "Razonamiento paso a paso para mejorar precisión. Fuerza tokens intermedios que guían la predicción final." / "Es como pensar en voz alta." | 26, 27 |
| **Few-Shot CoT** | "ICL donde los ejemplos incluyen el razonamiento explícito, no solo la respuesta." | 27 |
| **Self-Consistency** | "Genera múltiples respuestas y selecciona por votación de mayoría. Reduce errores por no-determinismo." | 26 |
| **Extended Thinking** | "Modelos Claude exponen su razonamiento interno con tags `<thinking>`." | 26, 31 |
| **Tree of Thought (ToT)** | "Explora múltiples caminos de razonamiento en paralelo. Útil para problemas con múltiples soluciones posibles." | 26, 33 |
| **Prompt Chaining** | "Divide tareas complejas en secuencia de prompts simples. El output de cada paso alimenta al siguiente." | 26, 35 |
| **Autoregresivo** | "Genera el texto token a token, de izquierda a derecha… Cada token nuevo depende únicamente de los tokens anteriores en el contexto." | 38 |
| **Memoria de trabajo explícita** | "El razonamiento escrito actúa como memoria de trabajo explícita." | 38 |
| **DSPy** | "Declarative Self-improving Python — framework de Stanford que trata los prompts como parámetros optimizables, no como texto fijo." | 41 |
| **Prompt caching** | "Marcar las partes reutilizables del prompt para caching. El proveedor almacena esos tokens y los reutiliza en requests posteriores." | 46 |
| **`cache_control`** | Bloque con el que se marca la parte estática del prompt (ejemplo Anthropic: `{"type": "ephemeral"}`). | 47 |
| **Model cascading** | "Intentar primero con el modelo más barato/rápido. Si la confianza es baja, escalar al modelo más caro/inteligente." | 48 |
| **Effort** | "Esfuerzo de razonamiento… determina cuántos tokens de 'thinking' genera el modelo (low / high / xhigh / max)." | 11 |
| **Automation bias** | "Riesgo de degradación de habilidades clínicas… cuando el médico delega en exceso al modelo." | 54 |
| **Los 6 principios OMS** | "Autonomía · Bienestar · Transparencia · Responsabilidad · Equidad · Sostenibilidad." | 55 |
| **Regression tests (de prompts)** | "Suite de casos críticos que NUNCA deben fallar. Si el prompt los rompe, el cambio se rechaza automáticamente." | 43 |

---

## Evidence and examples

Toda cifra del deck, con la slide de origen y una nota sobre su atribución.

### Cifras de rendimiento de técnicas

| Cifra | Afirmación | Slide | Atribución en el deck |
|---|---|---|---|
| **70%** | Mejora en precisión en problemas matemáticos complejos con CoT | 27 | **Ninguna** |
| **35%** | Menos errores en generación de código con CoT | 27 | **Ninguna** |
| **40%** | Reducción mínima de alucinaciones con XML + validación | 19 | **Ninguna** |
| **60%** | Reducción máxima "reportada en algunos benchmarks" con XML | 19 | **Ninguna** (no dice qué benchmarks) |
| 5× coste | "5 agentes = 5× el coste, pero la precisión mejora significativamente" | 29 | **Wang et al., 2022** ← única cita académica formal |
| 2-5× latencia | CoT vs. sin CoT | 39 | Ninguna |
| N× latencia/coste | Self-Consistency con N=5-10 repeticiones | 39 | Ninguna |
| 10-30 s | Latencia de Extended Thinking en casos complejos | 39 | Ninguna |
| 3-5× CoT | Latencia de ToT | 39 | Ninguna |
| 100-500 tokens | Razonamiento intermedio típico de CoT | 39 | Ninguna |
| 3-5 llamadas = 3-5× costo | Self-Consistency | 30, 37 | Ninguna |
| 2/3 votos → 67% confianza | Ejemplo de votación por mayoría | 30, 59 | Ejemplo sintético |

### Cifras de práctica y presupuesto

| Cifra | Afirmación | Slide |
|---|---|---|
| **3-5 ejemplos** | "suelen ser suficientes (calidad > cantidad)" en few-shot | 17, 23 |
| **2–10 ejemplos** | Rango del régimen few-shot | 22, 23 |
| **50-100 casos** | Tamaño mínimo del eval set con ground truth clínico | 14, 43 |
| **10-20 ejemplos** | Dataset mínimo para que DSPy optimice | 41 |
| **< 5 minutos** | Tiempo máximo de corrida del eval automatizado | 43 |
| **45-60 minutos** | Tiempo estimado de la práctica en aitutorial.dev | 57 |
| **20+ diagnósticos** | Umbral de categorías que justifica many-shot | 24 |

### Cifras de costo y contexto

| Cifra | Afirmación | Slide |
|---|---|---|
| 1M / 1M / 2M / 10M tokens | Ventanas de GPT-5.4 / Claude Opus 4.6 / Gemini 3 Pro / Llama 4 | 7 |
| ~750K tokens | Obra completa de Tolkien (576.000 palabras) | 8 |
| ~800K tokens | "Años de historial clínico completo de un paciente" | 8 |
| 4-5 tokens | "Ingeniería Biomédica" | 9 |
| **~$0,01** | 2.000 tokens de entrada + 500 de salida con GPT-4o | 9 |
| $1.503 | 10.000 queries × 50K tokens sin caching, a $3/1M | 46 |
| $450 | Mismo workload con 80% de hit rate → ahorro de $1.053 (70%) | 46 |
| $0,15 → $0,015 | Cache MISS vs. HIT de 50K tokens (90% de ahorro) | 47 |
| 10% del precio normal | Costo de un hit de caché | 47 |
| 50-90% / 70-90% | Rango de reducción de costos por caching (título vs. cuerpo) | 46, 47 |
| 10x | "Elegir mal puede multiplicar los costos por 10x" | 45 |
| $10 / 1.000 búsquedas | Búsqueda web (Anthropic) | 11 |
| 50 hs gratis/día, luego $0,05/hora | Ejecución de código (Anthropic) | 11 |

### Cifras clínicas y de investigación

| Cifra | Afirmación | Slide | Fuente citada |
|---|---|---|---|
| **86,5%** | Med-PaLM 2 en MedQA (USMLE); preferido sobre médicos en 8 de 9 ejes clínicos (2023); "no es público" | 50 | Solo el nombre del modelo |
| **81,4%** | GPT-4 en USMLE (5-shot) | 50 | Ninguna |
| **>90%** | o3 en exámenes de medicina general (MRCGP, 2025) | 50 | "MRCGP, 2025" |
| **62%** | Claude 3 Opus en diagnóstico diferencial radiológico, sobre GPT-4o y Gemini 1.5 Pro | 50 | Ninguna |
| **65%** | "Gemini Mosaic": informes de Rx de tórax equivalentes o mejores que radiólogos expertos | 50 | Ninguna — **nombre de producto no verificable** |
| **81%** | MedGemma: informes de rayos X equivalentes al clínico | 51, 53 | MedGemma, Google DeepMind (2025) |
| **98,7%** | MedGemma: precisión en extracción de datos de medicación | 51, 53 | Ídem |
| **14,4% → 3,2%** | Preguntas repetidas con GPT-3.5 en recepción ambulatoria | 51, 53 | Frontiers in Digital Health (2025), sin DOI |
| **7,8% → 2,4%** | Emociones negativas, mismo estudio | 51, 53 | Ídem |
| **2.164 pacientes** | Tamaño de muestra del estudio anterior | 51, 53 | **Sin identificación del estudio** |
| **80,7%** | Reducción de transcripción clínica con ChatGLM2-6B | 51, 53 | Ninguna |
| **197 clínicos** | Usan borradores automáticos (atención primaria, gastro, hepatología) | 51, 53 | Ninguna |
| **50%** | Menos tiempo en notas clínicas — "dato agregado de múltiples implementaciones" | 51, 53 | **Agregado, sin desglose** |
| **244 participantes / −23 puntos** | GPT-4 en terapia cognitiva grupal: caída de la deserción | 51, 53 | **Sin identificación del estudio** |
| **94,9% vs. <34,5%** | Precisión del LLM solo vs. uso por el público general sin guía | 55 | WHO / Frontiers / Nature Medicine / "PMC Reviews" (genérico) |
| **Solo 4 estudios (2024–2025)** | Cumplen criterios rigurosos de implementación clínica real | 55 | Ídem |
| **200M+ proteínas** | Estructuras predichas por AlphaFold | 52 | AlphaFold 2/3, DeepMind (2022/2024) |
| **1M búsquedas** | Elicit, revisiones sistemáticas | 52 | Elicit |
| **17.000 enfermedades** | Indicaciones predichas por TxGNN (Harvard) | 52 | TxGNN, Harvard (Nature Medicine, 2024) |
| **ISM001-055** | "Primer fármaco diseñado con IA en Fase II" (fibrosis pulmonar), Insilico Medicine | 52 | Insilico Medicine |

### Casos reales documentados de alucinación (slide 13)

- **Air Canada (2024)** — "El chatbot alucinó una política de reembolso inexistente. El tribunal falló en contra de la aerolínea, que debió compensar al pasajero."
- **Abogados en EE.UU. (2023)** — "Dos abogados presentaron citas de jurisprudencia generadas por ChatGPT que no existían. Fueron sancionados por el tribunal."
- **Med-PaLM en diagnóstico** — "Modelos médicos pueden generar diagnósticos plausibles pero incorrectos con alta confianza aparente."
- **Wikipedia falsa** — "LLMs pueden generar referencias bibliográficas con autores, títulos y DOIs completamente inventados."

### Casos clínicos sintéticos usados como ejemplos

| Caso | Uso | Slides |
|---|---|---|
| 60M, dolor precordial irradiado al brazo izquierdo, diaforesis | Ejemplo few-shot dentro del prompt de 6 componentes → IAM / angina inestable / disección aórtica | 17 |
| 45F, disnea progresiva 3 días, edemas MMII, ortopnea, PAS 160, FC 110, SpO2 92% | Input del prompt de 6 componentes (sin resolver) | 17 |
| 65M dolor torácico opresivo → EMERGENCIA (SCA); 8M caída de bicicleta → URGENTE (fractura); 30F fiebre 38.5 °C + odinofagia → NO URGENTE (faringitis) | Few-shot de triage | 24 |
| 45F, cefalea intensa súbita "la peor de su vida", rigidez de nuca | Input abierto del triage (`→ ???`) — **el deck no da la respuesta** | 24 |
| 45M, dolor abdominal derecho, fiebre 38.5 °C, náuseas 12h | Self-Consistency (apendicitis 2/3) y Extended Thinking | 30, 32, 59, 61 |
| 35F, dolor torácico agudo, disnea, taquicardia 110bpm, vuelo largo 48h | ToT — TEP con Score Wells 6 → angioTC pulmonar urgente | 34, 63 |
| Propina del 15% sobre $47,83 → $7,17 | Contraste sin CoT / con CoT | 28 |
| Clasificación de sentimiento (batería / se trabó / llegó el martes) | Few-shot en español | 23 |
| Customer sentiment (positive / neutral / negative) | Ejemplo XML **en inglés** | 19 |

### Herramientas y recursos nombrados

- **Tokenizador:** `gpt-tokenizer.dev` ("Pruébalo en tiempo real") — slide 9.
- **DSPy:** `dspy.ai`, Omar Khattab (Stanford NLP); optimizadores BootstrapFewShot, MIPRO, BayesianSignatureOptimizer — slide 41.
- **Versionado/observabilidad:** Git, LangSmith (LangChain), PromptLayer, Weights & Biases — slides 42, 58.
- **Research:** BioGPT (Microsoft Research), AlphaFold 2/3 (DeepMind), ESMFold (Meta AI), TxGNN (Harvard), Recursion Pharmaceuticals, Consensus, Elicit, Insilico Medicine — slide 52.
- **Práctica:** cuatro módulos de `aitutorial.dev` — slide 57; enlaces sueltos a `aitutorial.dev` también en las slides 18, 28, 30 y 59.
- **Precios:** openai.com/api/pricing, anthropic.com/pricing, ai.google.dev/pricing — slide 45.

---

## Inconsistencies / open questions

### Enlaces rotos o inaccesibles

1. **[51] Hipervínculo a MedGemma roto (404).** El enlace `https://deepmind.google/technologies/medgemma/` de la línea de fuentes no resuelve. Es la referencia que respalda las dos cifras más fuertes de la slide (81% de informes de rayos X, 98,7% de extracción de medicación).
2. **[51] Enlace a la guía de la OMS devuelve 403.** `https://iris.who.int/handle/10665/375579` (WHO — *Ethics & Governance of AI for Health: LMMs*, 2024) rechaza el acceso. Es la fuente del marco ético que estructura las slides 54 y 55.
3. **[51, 52] Los bloques de fuentes están malformados.** La extracción muestra hipervínculos anidados unos dentro de otros (`[[[[Fuentes: … ](url1)](url2)](url3)](url4)`): en el `.pptx` original, un único párrafo de texto lleva cuatro (u ocho, en la slide 52) hipervínculos superpuestos sobre distintos tramos. En la práctica el lector no puede saber qué URL corresponde a qué fuente sin abrirlas una por una.
4. **[51, 52] Fuentes citadas sin identificador.** "Frontiers in Digital Health (2025)", "Nature Medicine (2025)" y "PMC Reviews" son nombres de revista/repositorio, no artículos: sin DOI, título ni autores no son rastreables. Los enlaces apuntan a la portada de la revista (`frontiersin.org/journals/digital-health`, `nature.com/nm`), no al paper.

### Cifras sin atribución

5. **[19] 40% / 60% de reducción de alucinaciones con XML.** Sin fuente. La propia slide se cubre con "reportada en algunos benchmarks" sin decir cuáles. Un rango de 20 puntos sin metodología no es verificable.
6. **[27] 70% de mejora en precisión matemática y 35% menos errores en código con CoT.** Sin fuente. Son plausiblemente ecos del paper original de CoT (Wei et al., 2022), pero el deck no lo cita — cita a Wang et al. (2022) recién en la slide 29, y para self-consistency.
7. **[51, 53] El estudio de 2.164 pacientes.** Sin autor, título ni DOI. Se le atribuyen cuatro cifras precisas (14,4% → 3,2%; 7,8% → 2,4%).
8. **[51, 53] El estudio de 244 participantes** (GPT-4 en terapia cognitiva grupal, deserción −23 puntos). Sin identificación. Además "23 puntos" no aclara si es porcentual absoluto o relativo.
9. **[50] "Gemini Mosaic (Google DeepMind)" — nombre de producto no verificable.** No corresponde a ningún modelo publicado por Google/DeepMind bajo ese nombre. La cifra del 65% en informes de Rx de tórax queda huérfana.
10. **[51, 53] "50% menos tiempo en notas clínicas (dato agregado de múltiples implementaciones)".** El propio deck admite que es un agregado, pero no dice de cuántas implementaciones ni con qué método se agregó.
11. **[51, 53] 80,7% de reducción con ChatGLM2-6B y 197 clínicos.** Sin fuente. Además, ChatGLM2-6B es un modelo chino de 6B parámetros; el deck no aclara en qué idioma ni sistema sanitario se midió, lo que condiciona la transferibilidad.
12. **[55] "Precisión del LLM solo: 94,9%. Uso por el público general sin guía: <34,5%."** Dos cifras muy específicas sin fuente puntual: la línea de fuentes de la slide es genérica ("WHO (2024), Frontiers in Digital Health (2025), Nature Medicine (2025), PMC Reviews"). Tampoco se dice sobre qué tarea se midió el 94,9%.

### Inconsistencias internas del deck

13. **Bloque duplicado: slides 58–63 repiten 42, 30, 31, 32, 33 y 34**, y quedan *después* de la slide de cierre ("¡A Practicar!", 57). Seis de 63 slides (≈10% del deck) son material redundante fuera de lugar. Probable residuo de edición.
14. **[2, 3] Dos slides completamente vacías** al inicio, entre la portada y la agenda.
15. **La agenda promete "TOON" y ninguna slide lo cubre.** El módulo 5 se anuncia como "Framework de decisión, prompt caching, model cascading **y TOON**" en las slides 4, 16, 21, 25, 44 y 56, pero las slides 45–48 no mencionan TOON en ningún momento. *(Nota: la slide 49, que también es una agenda, ya trae la bajada **sin** TOON — "Framework de decisión, prompt caching y model cascading". Dos versiones distintas de la misma agenda conviven en el deck.)*
16. **La agenda promete un "sistema de triage con LLM" como práctica y no existe.** El módulo 7 se anuncia como "Módulos interactivos de aitutorial.dev + **sistema de triage con LLM**" en las siete slides de agenda; la slide 57 solo lista los cuatro módulos de aitutorial.dev. El ejercicio de triage nunca aparece.
17. **Inconsistencia en el catálogo de modelos entre las slides 7, 11, 20 y 45.**
    - La slide 7 (2026) lista *Claude Opus 4.6* con 1M de contexto; la slide 11 (tarifario Anthropic, 2026) lista *Opus 4.8*, *Sonnet 4.6*, *Haiku 4.5* y *Fable 5*; la slide 45 ("Precios a marzo 2026") lista *Claude Sonnet 4.6* con **200K** y *Claude Haiku 3*.
    - La slide 7 dice *Gemini 3 Pro* con 2M; las slides 20 y 45 dicen *Gemini 1.5 Pro* con 2M.
    - La slide 45 mezcla generaciones incompatibles en una misma tabla "a marzo 2026": GPT-4o, GPT-4o Mini, Claude Haiku 3 y Gemini 1.5 Pro (todos de 2024) junto a Claude Sonnet 4.6.
    - El árbol de decisión de la slide 45 recomienda *"Gemini 2.0 Flash o GPT-4o Mini"* y *"Claude Sonnet 4.6 o Gemini 1.5 Pro (2M)"*, y la slide 48 nombra *"Haiku/GPT-3.5"* y *"GPT-4/Sonnet"* — otro salto generacional dentro de la misma sección.
18. **[11] ~~"Fable 5" no corresponde a ningún modelo Anthropic conocido.~~ — CORREGIDO 2026-09-01.** Esta inconsistencia era **falsa**. Fable 5 (`claude-fable-5`) es un modelo real, con ventana de 1M y tarifa de $10/$50 por millón de tokens, verificado contra el catálogo vigente de la API de Claude (corte 2026-06-24) — exactamente la tarifa que declaraba el deck. El *"Currently unavailable"* de la captura refleja el estado del selector en el momento de la captura, no la inexistencia del modelo: son dos estados del mismo producto en fechas distintas. **No actuar sobre esta nota borrando el dato del tarifario.**
19. **[11] La frase sobre el effort queda cortada:** "…y el default se movió de medium a high," — termina en coma, sin cerrar. Además, la captura de la misma slide muestra el selector en *"Medium"*, contradiciendo el texto que dice que el default pasó a *high*.
20. **[46] Aritmética del caching que no cierra del todo.** El deck plantea 10.000 queries × 50.100 tokens = 501M tokens → $1.503 (correcto a $3/MTok). Con 80% de hit rate: misses 2.000 × 50.100 ≈ $301 + hits 8.000 × ~5.010 ≈ $120 = **≈$421**, no los **$450** que declara la slide. El ahorro reportado ($1.053, 70%) es internamente consistente con $450, así que la discrepancia está en el cálculo del costo con caching (~7% de diferencia).
21. **[46 vs. 47] Rangos de ahorro por caching distintos:** el título de la slide 46 dice "**50-90%**", el cuerpo de la 47 dice "**70-90%**", y el ejemplo trabajado da **70%**.
22. **[35] Frase truncada a mitad de palabra:** "…se ejecutan varias llamadas en vez de una lo cual **incre**". El texto se corta.
23. **[7] Fragmento suelto sin contexto:** "historial, respuestas," aparece como bullet aislado al final de la slide.
24. **[14] Fragmento suelto:** "Formal Testing como ventaja clave" aparece sin desarrollo.
25. **[45] La tabla comparativa de modelos está partida en dos bloques** por el árbol de decisión intercalado: el primer bloque tiene solo la fila de GPT-4o, y las seis filas restantes forman una segunda tabla con encabezado repetido. Es un artefacto de layout del deck, no de la extracción.
26. **[50 vs. 51] Tensión no resuelta entre dos cifras de radiología de Google.** La slide 50 atribuye 65% en informes de Rx de tórax a "Gemini Mosaic"; la slide 51 atribuye 81% en informes de rayos X a MedGemma. Nunca se explica si son la misma línea de trabajo, dos productos distintos o dos mediciones de lo mismo.
27. **[50] Etiquetas que no coinciden con el texto.** El bloque titulado "GPT-4o / o3 (OpenAI)" con 81,4% lleva como rótulo de la cifra "GPT-4 en USMLE (5-shot)" — el 81,4% es de GPT-4, no de GPT-4o ni de o3, pero el encabezado sugiere lo contrario.
28. **Anglicismos y errores de tipeo por sustitución automática.** Aparece "with" en lugar de "con" en tres lugares: "[18] Conectable **with** sistemas clínicos", "[27] Relación **with** ICL", "[32, 61] Responde en JSON **with**: diagnosis, urgency, next_steps". También: "[22] tareas comple**cias**" (por complejas), "[29] **¿Ç**uándo usarlo?", "[8] título '¿Cuanto es 1 millón de **Tolkien** tokens ?' " (Tolkien intercalado y espacio antes del signo de cierre).
29. **[18, 19] Ejemplos en inglés dentro de un deck en español.** La frase "Schema enforcement reduces parsing errors and retries — making outputs machine-checkable" (slide 18) y todo el ejemplo XML de clasificación de sentimiento (slide 19: `<task>Classify customer sentiment</task>`, "Your product is amazing!", etc.) están íntegramente en inglés, mientras el resto del módulo va en español.
30. **[1] Autoría doble no resuelta.** La portada acredita "Paulo Veiga/Marcos Sanchez Sorondo" sin distinguir roles. El encargo de ingesta describía el deck como autoría de Marcos Sorondo.
31. **[50] "Med-PaLM 2 … (2023) - No es publico".** El deck presenta como headline de benchmarks clínicos un modelo que él mismo señala como no accesible, sin discutir qué implica eso para la reproducibilidad de la cifra del 86,5%.

### Vacíos de contenido

32. **El deck no cubre el ejemplo de zero-shot.** Define los tres regímenes de ICL (slide 22) y dedica slides propias a few-shot (23) y many-shot (24), pero zero-shot nunca recibe un ejemplo trabajado.
33. **[24] El caso de triage queda abierto sin respuesta.** "Paciente: 45F, cefalea intensa súbita 'la peor de su vida', rigidez de nuca. → ???" — clínicamente es una hemorragia subaracnoidea (EMERGENCIA), pero el deck deja el `???` sin resolver y no hay notas del orador que lo cierren. **Sin guion hablado, un lector del deck no tiene forma de saber la respuesta esperada.**
34. **No hay notas del orador en ninguna de las 63 slides.** Consecuencia práctica: toda la carga narrativa recae en el cuerpo de las slides, y los saltos entre bloques densos (por ejemplo, de la slide 38 "por qué funcionan" a la 39 "por qué tardan") no tienen puente escrito.
35. **[54] Cuatro oportunidades y cuatro riesgos, pero sin priorización ni criterio de decisión.** Se presenta el marco OMS como listado plano; no se dice qué riesgo pesa más ni cómo se resuelve el trade-off en un despliegue concreto.
36. **El deck no discute privacidad de datos en las llamadas a API.** Menciona RGPD y anonimización como riesgo (slide 54), pero todos los ejemplos prácticos (prompt caching de historiales de paciente, triage, extracción de medicación) envían datos clínicos a APIs de terceros sin abordar ese punto.

---

## Images / diagrams

**Inventario.** 201 colocaciones de imagen en el `.pptx` → **133 archivos raster únicos** (por MD5) + **136 SVG** (originales vectoriales de los PNG). Todos los bytes están copiados en la carpeta compañera `AIG4B-Clase-3-Prompting.md/images/` (337 archivos de imagen + el `_manifest.json` original, 2,6 MB).

Clasificación del manifiesto: **22 `figura`** (≥ 0,75 in de lado) · **111 `icono`** (pictogramas de plantilla) · **`vectorial`** (los SVG detrás de cada PNG).

**Hallazgo importante para consumidores downstream:** de las 22 imágenes clasificadas como `figura` por tamaño, **solo 11 llevan contenido visual real**. Las otras **11 son marcos de tarjeta vacíos** — rectángulos blancos con una barra de acento roja a la izquierda, sin texto ni gráfico — que el deck usa como fondo detrás de cajas de texto. El texto que "parece" estar dentro de esas tarjetas vive en cajas de texto separadas del PPTX y **ya está capturado en el Markdown**, no en el píxel. **Ninguna imagen del deck contiene texto transcribible**: todas las etiquetas, cifras y rótulos son texto nativo de PowerPoint.

### Figuras con contenido real (11)

- **`AIG4B-Clase-3-Prompting.md/images/slide-01-1.png`** — slide 1 · 2,14 × 1,77 in · `role: figura`
  - **Representa:** logo institucional de la Universidad Austral: un óvalo azul marino con un árbol estilizado y cuatro estrellas de cuatro puntas en el follaje, rodeado por la leyenda circular `· AVSTRALIS · VNIVERSITAS · STVDIORVM ·`. Debajo, en tipografía serif azul: `UNIVERSIDAD` (versalitas espaciadas) sobre `AUSTRAL` (mayúsculas de mayor cuerpo).
  - **Por qué importa:** ancla institucional de la portada; identifica el deck como material de curso universitario y no divulgación suelta.
  - **Texto transcripto:** `AVSTRALIS · VNIVERSITAS · STVDIORVM` (latín) / `UNIVERSIDAD AUSTRAL` (español). **Único caso del deck en que una imagen contiene texto.**

- **`AIG4B-Clase-3-Prompting.md/images/slide-08-1.jpg`** — slide 8 · 5,00 × 7,50 in · `role: figura`
  - **Representa:** fotograma en formato vertical de Gandalf el Gris (Ian McKellen) en *El Señor de los Anillos*: plano medio, sombrero puntiagudo gris de ala ancha, barba larga y cana, capa gris oscura, mano izquierda sosteniendo su bastón en el borde inferior izquierdo. Fondo desenfocado de colinas verdes con montañas nevadas y cielo brumoso.
  - **Por qué importa:** soporte visual único de la analogía del millón de tokens ("la trilogía de LOTR más El Hobbit ≈ 750.000 tokens, y aún sobra espacio"). Es la imagen que hace concreta la escala de la ventana de contexto para una audiencia no técnica. **Nota de derechos:** es un fotograma de película con copyright, sin crédito en el deck — a considerar si el material se republica.
  - **Texto transcripto:** ninguno.

- **`AIG4B-Clase-3-Prompting.md/images/slide-11-1.jpg`** — slide 11 · 3,67 × 2,24 in · `role: figura`
  - **Representa:** captura de pantalla de la interfaz de Claude en modo oscuro, mostrando el selector de modelo y de effort. Dos menús superpuestos. El menú izquierdo: `Opus 4.8` con la bajada `For complex tasks` y un tilde azul de selección; debajo, separadas por líneas, las filas `Effort   Medium >` y `More models >` (esta última resaltada). El menú derecho (desplegado desde "More models") lista, de arriba abajo: `Fable 5` con una insignia gris `ⓘ Currently unavailable`, `Sonnet 4.6`, `Haiku 4.5`, línea divisoria, `Opus 4.7`, `Opus 4.6`, `Opus 3`. En la barra inferior de la composición, la píldora del compositor: `Opus 4.8  Medium ⌄` junto a un icono de micrófono y un icono de forma de onda.
  - **Por qué importa:** es la única evidencia visual del deck para la afirmación sobre controles de effort (slide 11) y la fuente de los nombres de modelo del tarifario. También es la fuente de dos inconsistencias registradas arriba: muestra "Fable 5" como *no disponible* pese a que la tabla le pone precio, y muestra el effort en **Medium** mientras el texto afirma que el default pasó a **high**.
  - **Texto transcripto (en inglés, tal como aparece):** `Opus 4.8` · `For complex tasks` · `Effort` · `Medium` · `More models` · `Fable 5` · `Currently unavailable` · `Sonnet 4.6` · `Haiku 4.5` · `Opus 4.7` · `Opus 4.6` · `Opus 3` · `Opus 4.8 Medium`.
  - *Idioma de la figura: **inglés** (interfaz sin traducir), dentro de un deck en español.*

- **`AIG4B-Clase-3-Prompting.md/images/slide-19-1.png`** — slide 19 · 1,69 × 1,69 in · `role: figura`
  - **Representa:** gráfico de dona (anillo grueso, sin relleno central). El arco rojo carmesí arranca en las 12 en punto y avanza en sentido horario hasta aproximadamente las 5 en punto — **≈40% de la circunferencia**. El resto del anillo es gris muy claro.
  - **Por qué importa:** es el soporte gráfico del "40% — Reducción mínima en alucinaciones con XML + validación". El porcentaje está dibujado, no escrito: el número "40%" es texto de PowerPoint colocado encima, no parte del PNG.
  - **Texto transcripto:** ninguno (la dona no lleva etiquetas).

- **`AIG4B-Clase-3-Prompting.md/images/slide-19-2.png`** — slide 19 · 1,69 × 1,69 in · `role: figura`
  - **Representa:** misma dona, arco rojo desde las 12 en punto en sentido horario hasta cerca de las 7:30 — **≈60% de la circunferencia**.
  - **Por qué importa:** soporte del "60% — Reducción máxima reportada en algunos benchmarks".
  - **Texto transcripto:** ninguno.

- **`AIG4B-Clase-3-Prompting.md/images/slide-27-1.png`** — slide 27 · 1,73 × 1,73 in · `role: figura`
  - **Representa:** dona con arco rojo desde las 12 en punto, horario, hasta cerca de las 8:30 — **≈70% de la circunferencia**. Es la más "llena" de las cuatro donas del deck.
  - **Por qué importa:** soporte del "70% — Mejora en precisión / Problemas matemáticos complejos" con CoT.
  - **Texto transcripto:** ninguno.

- **`AIG4B-Clase-3-Prompting.md/images/slide-27-2.png`** — slide 27 · 1,73 × 1,73 in · `role: figura`
  - **Representa:** dona con arco rojo desde las 12 en punto, horario, hasta cerca de las 4:30 — **≈35% de la circunferencia**.
  - **Por qué importa:** soporte del "35% — Menos errores / Generación de código con CoT".
  - **Texto transcripto:** ninguno.

- **`AIG4B-Clase-3-Prompting.md/images/slide-22-1.png`** — slide 22 · 11,89 × 1,04 in · `role: figura`
  - **Representa:** flecha horizontal muy alargada, gris rosado muy claro, apuntando a la derecha; cuerpo rectangular de altura constante que termina en punta triangular. Ocupa casi todo el ancho de la slide.
  - **Por qué importa:** es la barra que sostiene la fila "Zero-shot" en la progresión ICL de la slide 22. Su longitud (la mayor de las tres) codifica visualmente la posición del régimen en el eje.
  - **Texto transcripto:** ninguno.

- **`AIG4B-Clase-3-Prompting.md/images/slide-22-2.png`** — slide 22 · 11,64 × 1,04 in · `role: figura`
  - **Representa:** flecha idéntica a la anterior, levemente más corta.
  - **Por qué importa:** barra de la fila "Few-shot".
  - **Texto transcripto:** ninguno.

- **`AIG4B-Clase-3-Prompting.md/images/slide-22-3.png`** — slide 22 · 11,39 × 1,04 in · `role: figura`
  - **Representa:** flecha idéntica, la más corta de las tres.
  - **Por qué importa:** barra de la fila "Many-shot". Las tres juntas forman el escalonado zero → few → many. *(Observación: el escalonado es decreciente en longitud mientras la cantidad de ejemplos crece — la codificación visual va en sentido contrario a la magnitud que representa.)*
  - **Texto transcripto:** ninguno.

- **`AIG4B-Clase-3-Prompting.md/images/slide-33-1.png`** — slides 33 y 62 · 4,42 × 2,62 in · `role: figura`
  - **Representa:** diagrama de proceso de tres pasos: tres circunferencias gruesas rojo carmesí, encadenadas y solapadas de modo que la intersección de cada par forma una cuña roja que apunta a la derecha (efecto de flujo). Dentro de cada círculo, un pictograma de línea gris oscuro:
    1. **Círculo 1:** una rama con hojas (tres hojas ovaladas sobre un tallo diagonal) — *ramificar*.
    2. **Círculo 2:** una balanza de dos platillos con fiel y base — *evaluar*.
    3. **Círculo 3:** un documento con líneas de texto y una tilde de verificación superpuesta en el ángulo inferior derecho — *seleccionar / validar*.
  - **Por qué importa:** es el **único diagrama conceptual real del deck**. Ilustra el ciclo ToT que el texto de la slide nombra como "Generar ramas → Evaluar ramas → Seleccionar camino". La metáfora visual (rama → balanza → documento validado) hace legible el paralelo con el diagnóstico diferencial clínico que plantea la misma slide.
  - **Texto transcripto:** ninguno — los rótulos "Generar ramas", "Evaluar ramas" y "Seleccionar camino" son texto de PowerPoint colocado debajo, ya capturado en el Markdown.
  - **Repetido en:** `slide-62-1.png` (slide 62, el duplicado de la 33) — mismo archivo, mismo MD5.

### Figuras que resultaron ser marcos de tarjeta vacíos (11)

Todas comparten la misma descripción: **rectángulo blanco con borde gris muy claro y una barra vertical de acento rojo carmesí sobre el lado izquierdo** (en tres casos la barra es gris claro en lugar de roja). Sin texto, sin gráfico, sin iconos. Son fondos decorativos de tarjeta; el contenido que aparenta estar dentro son cajas de texto independientes ya capturadas en el Markdown. Se listan de todos modos porque el manifiesto las clasifica como `figura` y downstream podría intentar usarlas.

| Archivo (en `AIG4B-Clase-3-Prompting.md/images/`) | Slide | Tamaño | Acento | Repetido en |
|---|---|---|---|---|
| `slide-06-5.png` | 6 | 2,80 × 1,39 in | rojo, izq. | `slide-06-6.png` |
| `slide-06-7.png` | 6 | 2,80 × 1,14 in | rojo, izq. | `slide-06-8.png` |
| `slide-42-1.png` | 42 | 5,74 × 1,19 in | rojo, izq. | `slide-42-2.png`, `slide-42-3.png`, `slide-58-1.png`, `slide-58-2.png`, `slide-58-3.png` (6 colocaciones en total, slides 42 y 58) |
| `slide-51-1.png` | 51 | 5,91 × 1,31 in | rojo, izq. | `slide-51-2.png`, `slide-51-5.png` |
| `slide-51-3.png` | 51 | 5,91 × 1,48 in | rojo, izq. | `slide-51-4.png` |
| `slide-52-1.png` | 52 | 5,90 × 1,95 in | rojo, izq. | `slide-52-2.png`, `slide-52-3.png`, `slide-52-4.png` |
| `slide-54-5.png` | 54 | 2,82 × 1,83 in | rojo, izq. | `slide-54-6.png` |
| `slide-54-7.png` | 54 | 2,82 × 2,04 in | rojo, izq. | `slide-54-8.png` |
| `slide-57-1.png` | 57 | 5,71 × 1,82 in | gris claro, izq. | `slide-57-3.png` |
| `slide-57-2.png` | 57 | 5,42 × 1,82 in | gris claro, izq. | — |
| `slide-57-4.png` | 57 | 5,42 × 2,09 in | gris claro, izq. | — |

Todas tienen SVG original correspondiente (ver más abajo).

### Iconos (111 únicos, 162 colocaciones)

**Caracterización del set** (a partir de una muestra abierta de 10: `slide-12-1`, `slide-12-2`, `slide-12-3`, `slide-06-1`, `slide-17-1`, `slide-17-2`, `slide-17-7`, `slide-34-1`, `slide-48-1`, `slide-54-1`). Es un set de pictogramas de plantilla, homogéneo, en cuatro familias:

1. **Pictogramas de línea rojo carmesí** (≈0,2–0,6 in), trazo uniforme sin relleno, sobre fondo transparente. Muestra verificada: un robot de frente con antena, ojos circulares y "boca" de tres guiones (`slide-12-1`, alucinaciones); un dado / cuadrado redondeado con cinco puntos en disposición de "cinco" (`slide-12-2`, no-determinismo); un pin de mapa con círculo interior sobre una elipse de sombra (`slide-12-3`, sesgo de recencia).
2. **Flechas rojas de trazo fino** apuntando a la derecha, con punta en V abierta (`slide-06-1`, `slide-54-1`) — conectores entre elementos de lista.
3. **Flechas gruesas gris rosado apuntando hacia abajo** (`slide-34-1`, `slide-48-1`), en dos proporciones (más larga y más corta) — conectores verticales de diagramas de flujo (ramas ToT, cascada de modelos).
4. **Marcos y fragmentos decorativos**: pequeños corchetes de esquina rojo oscuro que enmarcan bloques de código (`slide-17-7`, 0,14 in) y filas de tarjeta vacías anchas y bajas que el manifiesto clasifica como `icono` por tener menos de 0,75 in de alto pese a medir 5,81 in de ancho (`slide-17-1`, `slide-17-2`).

**Ninguno de los iconos contiene texto.** Todos son decorativos o de señalización; ninguno aporta información que no esté ya en el texto de las slides. Se despachan uno por línea, agrupados por archivo único (MD5), con su slide de origen y sus repeticiones.

- `AIG4B-Clase-3-Prompting.md/images/slide-05-1.png` — `role: icono` · slide 5 · 0.55×0.55 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-05-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-05-2.png` — `role: icono` · slide 5 · 0.55×0.55 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-05-2.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-05-3.png` — `role: icono` · slide 5 · 0.55×0.55 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-05-3.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-05-4.png` — `role: icono` · slide 5 · 0.27×0.22 in
- `AIG4B-Clase-3-Prompting.md/images/slide-06-1.png` — `role: icono` · slide 6 · 0.27×0.27 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-06-1.svg` · repetido en: `slide-06-2.png`, `slide-06-3.png`, `slide-06-4.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-09-1.png` — `role: icono` · slide 9 · 0.24×0.19 in · repetido en: `slide-23-1.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-10-1.png` — `role: icono` · slide 10 · 0.25×0.20 in
- `AIG4B-Clase-3-Prompting.md/images/slide-12-1.png` — `role: icono` · slide 12 · 0.58×0.58 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-12-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-12-2.png` — `role: icono` · slide 12 · 0.58×0.58 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-12-2.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-12-3.png` — `role: icono` · slide 12 · 0.58×0.58 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-12-3.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-13-1.png` — `role: icono` · slide 13 · 0.33×0.33 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-13-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-13-2.png` — `role: icono` · slide 13 · 0.33×0.33 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-13-2.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-13-3.png` — `role: icono` · slide 13 · 0.33×0.33 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-13-3.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-14-1.png` — `role: icono` · slide 14 · 0.27×0.27 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-14-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-14-2.png` — `role: icono` · slide 14 · 0.27×0.27 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-14-2.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-14-3.png` — `role: icono` · slide 14 · 0.27×0.27 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-14-3.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-14-4.png` — `role: icono` · slide 14 · 0.27×0.27 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-14-4.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-14-5.png` — `role: icono` · slide 14 · 0.27×0.27 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-14-5.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-14-6.png` — `role: icono` · slide 14 · 0.17×0.14 in
- `AIG4B-Clase-3-Prompting.md/images/slide-15-1.png` — `role: icono` · slide 15 · 0.39×0.39 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-15-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-15-2.png` — `role: icono` · slide 15 · 0.39×0.39 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-15-2.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-15-3.png` — `role: icono` · slide 15 · 0.39×0.39 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-15-3.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-17-1.png` — `role: icono` · slide 17 · 5.81×0.72 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-17-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-17-2.png` — `role: icono` · slide 17 · 5.81×0.66 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-17-2.svg` · repetido en: `slide-17-3.png`, `slide-17-4.png`, `slide-17-5.png`, `slide-17-6.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-17-7.png` — `role: icono` · slide 17 · 0.14×0.11 in · repetido en: `slide-47-1.png`, `slide-47-2.png`, `slide-51-6.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-18-1.png` — `role: icono` · slide 18 · 0.21×0.21 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-18-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-18-2.png` — `role: icono` · slide 18 · 0.21×0.21 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-18-2.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-20-1.png` — `role: icono` · slide 20 · 0.47×0.47 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-20-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-20-2.png` — `role: icono` · slide 20 · 0.47×0.47 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-20-2.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-20-3.png` — `role: icono` · slide 20 · 0.47×0.47 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-20-3.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-20-4.png` — `role: icono` · slide 20 · 0.29×0.23 in
- `AIG4B-Clase-3-Prompting.md/images/slide-24-1.png` — `role: icono` · slide 24 · 0.17×0.14 in · repetido en: `slide-45-1.png`, `slide-55-1.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-26-1.png` — `role: icono` · slide 26 · 0.48×0.48 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-26-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-26-2.png` — `role: icono` · slide 26 · 0.48×0.48 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-26-2.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-26-3.png` — `role: icono` · slide 26 · 0.48×0.48 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-26-3.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-26-4.png` — `role: icono` · slide 26 · 0.48×0.48 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-26-4.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-26-5.png` — `role: icono` · slide 26 · 0.48×0.48 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-26-5.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-27-3.png` — `role: icono` · slide 27 · 0.14×0.12 in
- `AIG4B-Clase-3-Prompting.md/images/slide-28-1.png` — `role: icono` · slide 28 · 0.22×0.18 in · repetido en: `slide-39-7.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-30-1.png` — `role: icono` · slide 30 · 0.18×0.15 in · repetido en: `slide-40-8.png`, `slide-59-1.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-31-1.png` — `role: icono` · slide 31 · 0.58×0.58 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-31-1.svg` · repetido en: `slide-60-1.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-31-2.png` — `role: icono` · slide 31 · 0.58×0.58 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-31-2.svg` · repetido en: `slide-60-2.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-31-3.png` — `role: icono` · slide 31 · 0.58×0.58 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-31-3.svg` · repetido en: `slide-60-3.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-32-1.png` — `role: icono` · slide 32 · 0.20×0.16 in · repetido en: `slide-32-5.png`, `slide-61-1.png`, `slide-61-5.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-32-2.png` — `role: icono` · slide 32 · 0.33×0.33 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-32-2.svg` · repetido en: `slide-61-2.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-32-3.png` — `role: icono` · slide 32 · 0.33×0.33 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-32-3.svg` · repetido en: `slide-61-3.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-32-4.png` — `role: icono` · slide 32 · 0.33×0.33 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-32-4.svg` · repetido en: `slide-61-4.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-33-2.png` — `role: icono` · slide 33 · 0.26×0.21 in · repetido en: `slide-62-2.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-34-1.png` — `role: icono` · slide 34 · 0.48×1.04 in · repetido en: `slide-34-2.png`, `slide-34-3.png`, `slide-63-1.png`, `slide-63-2.png`, `slide-63-3.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-34-4.png` — `role: icono` · slide 34 · 0.20×0.16 in · repetido en: `slide-63-4.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-35-1.png` — `role: icono` · slide 35 · 0.20×0.20 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-35-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-35-2.png` — `role: icono` · slide 35 · 0.20×0.20 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-35-2.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-35-3.png` — `role: icono` · slide 35 · 0.20×0.20 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-35-3.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-35-4.png` — `role: icono` · slide 35 · 0.20×0.20 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-35-4.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-35-5.png` — `role: icono` · slide 35 · 0.20×0.20 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-35-5.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-35-6.png` — `role: icono` · slide 35 · 0.17×0.14 in · repetido en: `slide-43-1.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-36-1.png` — `role: icono` · slide 36 · 0.19×0.15 in
- `AIG4B-Clase-3-Prompting.md/images/slide-37-1.png` — `role: icono` · slide 37 · 0.31×0.31 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-37-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-37-10.png` — `role: icono` · slide 37 · 0.31×0.31 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-37-10.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-37-2.png` — `role: icono` · slide 37 · 0.31×0.31 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-37-2.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-37-3.png` — `role: icono` · slide 37 · 0.31×0.31 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-37-3.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-37-4.png` — `role: icono` · slide 37 · 0.31×0.31 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-37-4.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-37-5.png` — `role: icono` · slide 37 · 0.31×0.31 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-37-5.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-37-6.png` — `role: icono` · slide 37 · 0.31×0.31 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-37-6.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-37-7.png` — `role: icono` · slide 37 · 0.31×0.31 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-37-7.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-37-8.png` — `role: icono` · slide 37 · 0.31×0.31 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-37-8.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-37-9.png` — `role: icono` · slide 37 · 0.31×0.31 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-37-9.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-38-1.png` — `role: icono` · slide 38 · 0.21×0.17 in
- `AIG4B-Clase-3-Prompting.md/images/slide-38-2.png` — `role: icono` · slide 38 · 0.34×0.34 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-38-2.svg` · repetido en: `slide-42-4.png`, `slide-58-4.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-38-3.png` — `role: icono` · slide 38 · 0.34×0.34 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-38-3.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-38-4.png` — `role: icono` · slide 38 · 0.34×0.34 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-38-4.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-39-1.png` — `role: icono` · slide 39 · 0.36×0.36 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-39-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-39-2.png` — `role: icono` · slide 39 · 0.36×0.36 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-39-2.svg` · repetido en: `slide-39-6.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-39-3.png` — `role: icono` · slide 39 · 0.36×0.36 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-39-3.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-39-4.png` — `role: icono` · slide 39 · 0.36×0.36 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-39-4.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-39-5.png` — `role: icono` · slide 39 · 0.36×0.36 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-39-5.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-40-1.png` — `role: icono` · slide 40 · 0.30×0.30 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-40-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-40-2.png` — `role: icono` · slide 40 · 0.30×0.30 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-40-2.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-40-3.png` — `role: icono` · slide 40 · 0.30×0.30 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-40-3.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-40-4.png` — `role: icono` · slide 40 · 0.15×0.15 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-40-4.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-40-5.png` — `role: icono` · slide 40 · 0.15×0.15 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-40-5.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-40-6.png` — `role: icono` · slide 40 · 0.15×0.15 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-40-6.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-40-7.png` — `role: icono` · slide 40 · 0.15×0.15 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-40-7.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-41-1.png` — `role: icono` · slide 41 · 0.16×0.13 in
- `AIG4B-Clase-3-Prompting.md/images/slide-41-2.png` — `role: icono` · slide 41 · 0.39×1.04 in
- `AIG4B-Clase-3-Prompting.md/images/slide-41-3.png` — `role: icono` · slide 41 · 0.39×1.04 in · repetido en: `slide-41-4.png`, `slide-41-5.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-42-5.png` — `role: icono` · slide 42 · 0.34×0.34 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-42-5.svg` · repetido en: `slide-58-5.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-42-6.png` — `role: icono` · slide 42 · 0.34×0.34 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-42-6.svg` · repetido en: `slide-58-6.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-42-7.png` — `role: icono` · slide 42 · 0.34×0.34 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-42-7.svg` · repetido en: `slide-58-7.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-46-1.png` — `role: icono` · slide 46 · 0.15×0.12 in
- `AIG4B-Clase-3-Prompting.md/images/slide-46-2.png` — `role: icono` · slide 46 · 0.36×1.04 in · repetido en: `slide-46-3.png`, `slide-46-4.png`, `slide-46-5.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-46-6.png` — `role: icono` · slide 46 · 0.24×0.24 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-46-6.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-46-7.png` — `role: icono` · slide 46 · 0.24×0.24 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-46-7.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-46-8.png` — `role: icono` · slide 46 · 0.24×0.24 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-46-8.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-48-1.png` — `role: icono` · slide 48 · 0.34×1.04 in · repetido en: `slide-48-2.png`, `slide-48-3.png`, `slide-48-4.png`, `slide-48-5.png`
- `AIG4B-Clase-3-Prompting.md/images/slide-48-10.png` — `role: icono` · slide 48 · 0.23×0.23 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-48-10.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-48-11.png` — `role: icono` · slide 48 · 0.23×0.23 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-48-11.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-48-6.png` — `role: icono` · slide 48 · 0.23×0.23 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-48-6.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-48-7.png` — `role: icono` · slide 48 · 0.23×0.23 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-48-7.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-48-8.png` — `role: icono` · slide 48 · 0.23×0.23 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-48-8.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-48-9.png` — `role: icono` · slide 48 · 0.23×0.23 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-48-9.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-50-1.png` — `role: icono` · slide 50 · 0.32×0.32 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-50-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-50-2.png` — `role: icono` · slide 50 · 0.32×0.32 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-50-2.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-50-3.png` — `role: icono` · slide 50 · 0.32×0.32 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-50-3.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-50-4.png` — `role: icono` · slide 50 · 0.32×0.32 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-50-4.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-52-5.png` — `role: icono` · slide 52 · 0.15×0.12 in
- `AIG4B-Clase-3-Prompting.md/images/slide-53-1.png` — `role: icono` · slide 53 · 0.48×0.48 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-53-1.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-53-2.png` — `role: icono` · slide 53 · 0.48×0.48 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-53-2.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-53-3.png` — `role: icono` · slide 53 · 0.48×0.48 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-53-3.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-53-4.png` — `role: icono` · slide 53 · 0.48×0.48 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-53-4.svg`
- `AIG4B-Clase-3-Prompting.md/images/slide-54-1.png` — `role: icono` · slide 54 · 0.24×0.24 in · SVG original: `AIG4B-Clase-3-Prompting.md/images/slide-54-1.svg` · repetido en: `slide-54-2.png`, `slide-54-3.png`, `slide-54-4.png`

### Originales vectoriales (SVG) — 136 archivos

Cada uno es el SVG fuente detrás de un PNG rasterizado por PowerPoint. **No se abrieron para transcripción** (`role: vectorial` — son el mismo contenido que su PNG hermano, en formato escalable). Los bytes están todos en la carpeta compañera y son la mejor opción si un consumidor downstream necesita reescalar o recolorear un icono sin pérdida.

Convención de nombre: `slide-NN-M.svg` es el vectorial de `slide-NN-M.png`. De los 133 rasters únicos, **87 iconos y las 11 tarjetas vacías** tienen SVG; las tres imágenes fotográficas o de captura (`slide-01-1.png`, `slide-08-1.jpg`, `slide-11-1.jpg`), las cuatro donas (`slide-19-1/2`, `slide-27-1/2`), las tres flechas de la slide 22 y el diagrama de la slide 33 **no** tienen vectorial: son raster puro.

Listado completo en `AIG4B-Clase-3-Prompting.md/images/_manifest.json` (copiado junto a las imágenes), campo `svg_original`.

### Manifiesto

- **`AIG4B-Clase-3-Prompting.md/images/_manifest.json`** — copia del manifiesto original de extracción. 201 entradas, una por colocación, con `slide`, `file`, `shape`, `w_emu`, `h_emu`, `svg_original`, `md5`, `role`, `primera_aparicion` y `repetida_en`. Es la referencia autoritativa para resolver duplicados: si un consumidor downstream necesita una imagen y encuentra varias con el mismo `md5`, debe usar la de `primera_aparicion`.

---

## Raw / preserved excerpts

Preservados verbatim, en el idioma original. Son el material más reutilizable del deck.

### [17] Prompt estructurado completo — los 6 componentes (español)

```
# [1] ROL / PERSONA
Eres un médico especialista en medicina interna con 15 años de experiencia clínica.

# [2] CONTEXTO
Estás asistiendo en la guardia de un hospital de tercer nivel.
Las guías clínicas vigentes son las de la AHA 2023.

# [3] INSTRUCCIONES
1. Analiza los síntomas del paciente.
2. Lista los diagnósticos diferenciales más probables (máximo 3).
3. Recomienda los estudios complementarios iniciales.
4. Sugiere el manejo inmediato.

# [4] RESTRICCIONES
- No prescribas medicamentos con dosis específicas.
- Responde SOLO en base a los datos provistos.
- Formato de salida: JSON con claves: diagnosticos, estudios, manejo.

# [5] EJEMPLOS (Few-shot)
Paciente: 60M, dolor precordial irradiado al brazo izquierdo, diaforesis.
→ {"diagnosticos": ["IAM", "angina inestable", "disección aórtica"],
   "estudios": ["ECG", "troponinas", "Rx tórax"],
   "manejo": "Activar código infarto, AAS 300mg, monitoreo continuo"}

# [6] INPUT
Paciente: 45F, disnea progresiva de 3 días, edemas en MMII,
ortopnea, PAS 160mmHg, FC 110bpm, SpO2 92%.
```

### [18] Schema JSON para output clínico estructurado

```json
{
  "diagnosticos": ["string"],
  "estudios": ["string"],
  "manejo": "string",
  "urgencia": "alta | media | baja"
}
```

### [19] Ejemplo de prompting con XML tags (**en inglés en el original**)

```xml
<task>Classify customer sentiment</task>
<instruction>
Return ONLY one word: positive, neutral, or negative.
For each <input>, produce the corresponding <output>.
</instruction>
<examples>
<example>
<input>Your product is amazing! Best purchase ever.</input>
<output>positive</output>
</example>
<example>
<input>It's okay, does the job but nothing special.</input>
<output>neutral</output>
</example>
<example>
<input>Terrible quality. Broke after one week. Demanding refund!</input>
<output>negative</output>
</example>
</examples>
<input>
The shipping was fast and the product arrived in perfect condition. Would buy again!
</input>
```

### [15] Patrón de completado explícito (prompt vago vs. prompt estructurado)

> **Prompt vago:** "Extrae nombre y email" → puede fallar sin patrón explícito.
>
> **Prompt estructurado** — dar un patrón de completado explícito:
> ```
> Nombre: [campo]
> Email: [campo]
> De: [texto]
> ```

### [23] Few-shot — clasificación de sentimiento (español)

```
Clasifica el sentimiento como
POSITIVO, NEGATIVO o NEUTRO.

"La batería dura muchísimo"
→ POSITIVO

"Se trabó a los dos días"
→ NEGATIVO

"El dispositivo llegó el martes"
→ NEUTRO"
```

*(El cierre de comillas sobrante después de NEUTRO está en el original.)*

### [24] Few-shot en triage clínico

```
# INSTRUCCIÓN
Clasifica la urgencia clínica como EMERGENCIA, URGENTE o NO URGENTE.

# EJEMPLOS (Few-shot)
Paciente: 65M, dolor torácico opresivo, irradiado a brazo izquierdo, diaforesis.
→ EMERGENCIA (Sospecha de SCA)

Paciente: 8M, caída de bicicleta, deformidad en antebrazo, pulsos distales presentes.
→ URGENTE (Probable fractura)

Paciente: 30F, fiebre 38.5°C por 2 días, odinofagia, sin dificultad respiratoria.
→ NO URGENTE (Compatible con faringitis)

# INPUT
Paciente: 45F, cefalea intensa súbita "la peor de su vida", rigidez de nuca.
→ ???
```

*(El deck deja el `???` sin resolver y no hay notas del orador que lo cierren.)*

### [28] CoT — contraste sin / con

> **Sin CoT**
> - Prompt: "¿Cuánto es el 15% de propina en una cuenta de $47.83?"
> - Respuesta: $7.17
> - No se puede auditar ni depurar el razonamiento.
>
> **Con CoT**
> - Prompt: "¿Cuánto es el 15% de propina en una cuenta de $47.83? **Piensa paso a paso.**"
> - Respuesta:
>   1. Cuenta total: $47.83
>   2. 15% = 47.83 × 0.15
>   3. = $7.17
>   Propina: $7.17
> - Razonamiento auditable. Los errores son detectables.

### [30 y 59] Self-Consistency — votación por mayoría

```
# CASO CLÍNICO
Paciente: 45M, dolor abdominal derecho, fiebre 38.5°C, náuseas 12h.

# RUN 1
Diagnóstico: Apendicitis aguda → Urgencia: ALTA

# RUN 2
Diagnóstico: Apendicitis aguda → Urgencia: ALTA

# RUN 3
Diagnóstico: Cólico renal → Urgencia: MEDIA

# RESULTADO (votación)
→ Apendicitis aguda — ALTA urgencia (2/3 votos)
→ Confianza: 67%
```

### [32 y 61] Extended Thinking — prompt con `<thinking>`

```xml
<document>
Paciente: 45M, dolor abdominal derecho, fiebre 38.5°C, náuseas 12h
</document>

<thinking>
Necesito analizar este caso para:
1. Síntomas principales y su duración
2. Diagnósticos diferenciales posibles
3. Nivel de urgencia
4. Próximos pasos recomendados
Déjame trabajar cada sección...
</thinking>

Responde en JSON with: diagnosis, urgency, next_steps
```

*(El "with" en lugar de "con" está en el original.)*

### [34 y 63] Tree of Thought — caso clínico

```
# CASO CLÍNICO
Paciente: 35F, dolor torácico agudo, disnea,
taquicardia 110bpm, viaje largo en avión hace 48h.

# INSTRUCCIÓN (Tree of Thought)
1. Genera 3 hipótesis diagnósticas posibles
2. Evalúa la evidencia a favor y en contra de cada una
3. Selecciona el diagnóstico más probable con justificación

# RESULTADO
→ Diagnóstico prioritario: TEP
→ Recomendación: angioTC pulmonar urgente
→ Transparencia: razonamiento auditable para decisión clínica
```

Razonamiento del modelo, rama por rama:

> **Rama A: TEP (Tromboembolismo Pulmonar)** — Viaje largo, disnea, taquicardia → Score Wells: 6 (alta probabilidad). Rama seleccionada.
>
> **Rama B: Neumotórax espontáneo** — Posible, pero sin trauma ni factores de riesgo claros. Probabilidad media-baja.
>
> **Rama C: SCA (Síndrome Coronario Agudo)** — Dolor torácico compatible, pero perfil joven sin factores cardiovasculares. Descartado.

### [36] Prompt Chaining — pipeline clínico

```
# PASO 1 — Clasificar urgencia
Input: Mensaje del paciente
→ Output: ALTA / MEDIA / BAJA

# PASO 2 — Extraer detalles
Input: Mensaje + clasificación
→ Output: síntomas, duración, antecedentes

# PASO 3 — Buscar en KB (RAG)
Input: Detalles extraídos
→ Output: protocolos clínicos relevantes

# PASO 4 — Generar respuesta
Input: Todo lo anterior
→ Output: respuesta estructurada para el médico
```

### [45] Árbol de decisión para elegir modelo

```
¿La tarea es simple (clasificación, extracción básica)?
├─ Sí → Gemini 2.0 Flash o GPT-4o Mini
└─ No → Continuar

¿Necesitas >200K tokens de contexto?
├─ Sí → Claude Sonnet 4.6 o Gemini 1.5 Pro (2M)
└─ No → Continuar

¿Necesitas salida JSON estructurada?
├─ Sí → GPT-4o
└─ No → Claude Sonnet 4.6 (mejor prosa)

¿El costo es crítico (alto volumen)?
├─ Sí → Model cascading + Gemini 2.0 Flash
└─ No → Usar el mejor modelo para calidad
```

### [46] Cálculo de ahorro por prompt caching

```
// Sin caching: 10.000 queries × 50.100 tokens
// Costo: $1.503

// Con caching (80% hit rate):
// Misses (20%): 2.000 × 50K tokens
// Hits (80%): 8.000 × 5K tokens (90% reducción)
// Costo total: $450 → Ahorro: $1.053 (70%)
```

### [47] Prompt caching — implementación con Anthropic Cache Control

```python
import anthropic
client = anthropic.Anthropic()

# Parte ESTÁTICA — se cachea (50K tokens)
system_prompt = """
Eres un médico especialista en medicina interna.
Guías clínicas AHA 2023: [... 50K tokens ...]
"""

response = client.messages.create(
    model="claude-sonnet-4-6",
    system=[{
        "type": "text",
        "text": system_prompt,
        "cache_control": {"type": "ephemeral"}
    }],
    messages=[{
        "role": "user",
        # Parte DINÁMICA — cambia por request
        "content": "Paciente: 45F, disnea, SpO2 92%"
    }]
)

# Request 1: cache MISS → $0.15 (50K tokens)
# Request 2: cache HIT  → $0.015 (90% ahorro)
# Request 1000: cache HIT → $0.015
```

### [8] Cita textual sobre la ventana de 1M de tokens

> "Claude Code tiene ahora una ventana de contexto de 1 millón de tokens por defecto. Un millón de tokens es mucho: la trilogía de El Señor de los Anillos más El Hobbit tienen unas 576.000 palabras, lo que equivale a ~750.000 tokens. Las cuatro obras caben en un único prompt... y aún sobra espacio."

*(El deck presenta la cita entre comillas y en negrita, pero no la atribuye a un autor ni a una publicación.)*

### [11] Impacto del effort en el costo (párrafo completo, truncado en el original)

> "El nivel de effort (esfuerzo de razonamiento) afecta el costo porque determina cuántos tokens de 'thinking' genera el modelo, y esos tokens se facturan a tarifa de salida aunque no se devuelvan en la respuesta. Opus 4.8 introdujo controles de effort (low / high / xhigh / max), y el default se movió de medium a high,"

### [35] Concepto de Prompt Chaining (párrafo completo, truncado en el original)

> "Dividir una tarea compleja en una secuencia de prompts simples, donde el output de un paso alimenta al siguiente. Cada paso puede ser más preciso al enfocarse en una sola sub-tarea. Es decir, se ejecutan varias llamadas en vez de una lo cual incre"

### [38] Por qué funcionan CoT y ToT — argumento completo

> **El LLM no 'piensa': predice tokens**
>
> Un LLM no razona internamente antes de responder. Genera el texto token a token, de izquierda a derecha, de forma autoregresiva. Cada token nuevo depende únicamente de los tokens anteriores en el contexto.
>
> No hay un 'motor de razonamiento' oculto. Lo que ves en la respuesta ES el razonamiento.
>
> **Por qué Chain of Thought (CoT) y Tree of Thought (ToT) mejoran los resultados**
>
> - *Los tokens intermedios son cálculo real.* Al escribir los pasos, el modelo genera representaciones intermedias que condicionan mejor los tokens siguientes. El razonamiento escrito actúa como memoria de trabajo explícita.
> - *Más contexto = mejor predicción final.* Cada paso escrito enriquece el contexto disponible para el siguiente token. Un razonamiento de 200 tokens guía mejor la respuesta final que un prompt de 10 tokens.
> - *Reduce el espacio de error.* Sin CoT, el modelo debe 'saltar' directamente a la respuesta. Con CoT, cada paso intermedio reduce la incertidumbre acumulada antes de la conclusión.
>
> **Analogía:** es como pedirle a alguien que resuelva un problema matemático en su cabeza vs. que lo escriba paso a paso en papel. El papel no lo hace más inteligente, pero sí más preciso.

### [41] DSPy — descripción completa

> "DSPy (Declarative Self-improving Python) es un framework de Stanford que trata los prompts como parámetros optimizables, no como texto fijo. En lugar de escribir prompts a mano, defines el comportamiento deseado y DSPy los optimiza automáticamente contra un dataset de evaluación.
> Creado por Omar Khattab (Stanford NLP). Disponible en: dspy.ai"
>
> **Analogía:** "es como el backpropagation del deep learning, pero para prompts. En vez de ajustar pesos, ajusta instrucciones."
>
> 1. **Definir el programa** — "Declaras módulos (ChainOfThought, ReAct, etc.) y cómo se conectan, sin escribir el prompt."
> 2. **Proveer ejemplos** — "Un pequeño dataset de inputs y outputs esperados (puede ser tan pequeño como 10-20 ejemplos)."
> 3. **Elegir un optimizador** — "BootstrapFewShot, MIPRO, BayesianSignatureOptimizer. DSPy prueba variantes automáticamente."
> 4. **Compilar** — "DSPy genera y evalúa prompts candidatos, seleccionando el que maximiza la métrica definida."

### [55] Las cuatro preguntas abiertas, verbatim

> **Escasez de evidencia robusta** — "Solo 4 estudios (2024–2025) cumplen criterios rigurosos de implementación real clínica. La mayor parte de la evidencia es observacional o en entornos controlados."
>
> **La brecha de uso es real** — "Precisión del LLM solo: 94,9%. Uso por el público general sin guía: <34,5%. El modelo no es el único factor; el contexto de uso importa tanto como la tecnología."
>
> **¿Quién responde cuando falla?** — "La OMS exige marcos de responsabilidad claros para cuando un LMM cause daño. Hoy esa pregunta sigue sin respuesta regulatoria definitiva en la mayoría de países."
>
> **Los 6 principios OMS** — "Autonomía · Bienestar · Transparencia · Responsabilidad · Equidad · Sostenibilidad. Un marco ético ineludible para cualquier despliegue en salud."

### Las dos "reglas de oro" del deck

> **[14]** "Regla de oro: si no puedes medir la tasa de alucinación de tu sistema, no puedes desplegarlo en un entorno clínico."
>
> **[43]** "Regla de oro: si no puedes medir la mejora, no puedes saber si mejoraste. El eval set es tan importante como el prompt mismo."

### Frases-bisagra reutilizables

- **[5]** "Un prompt es como una receta para un chef experto — cuanto más clara y específica, mejor el resultado."
- **[6]** "Más contexto no siempre es mejor: puede diluir lo importante."
- **[6]** "El modelo no 'elige' qué leer; procesa todo el contexto junto."
- **[15]** "Pensar en el LLM como un autocompletado muy sofisticado cambia cómo construimos los prompts."
- **[27]** "ICL enseña qué responder; CoT enseña cómo razonar."
- **[33]** "ToT es similar al diagnóstico diferencial clínico: considerar múltiples hipótesis, evaluar la evidencia disponible para cada una y descartar las menos probables."
- **[35]** "Prompt Chaining convierte tareas imposibles en secuencias manejables. Es la base de los agentes de IA modernos."
- **[38]** "No hay un 'motor de razonamiento' oculto. Lo que ves en la respuesta ES el razonamiento."
- **[39]** "Mayor calidad tiene un costo directo: más tokens generados = más tiempo de cómputo. No es magia, es aritmética."
- **[40, 43]** "Un prompt sin datos de evaluación es una hipótesis sin experimento."
- **[42]** "Un prompt es código."
- **[45]** "No existe un modelo universal… Elegir mal puede multiplicar los costos por 10x o degradar la calidad."
- **[55]** "Supervisión humana obligatoria en todas las implementaciones clínicas exitosas documentadas. Sin excepción."
