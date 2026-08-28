# memory.md — prompting

**Current step:** 6 (Polish) — `final.md` producido y limpio; listo para Step 7 (render) o cierre
**Awaiting:** confirmación de a qué clase del README corresponde (candidata: clase 5, miércoles 2 de septiembre)
**Topic:** Trabajar con LLMs: prompts, costos y producción — fundamentos de foundational models, ventana de contexto, tokens, técnicas de prompting
**Folder:** talks/prompting/
**Started:** 2026-08-28 (importada; original de 2026-08-14)

---

## Talk briefing

Importada desde `talksmith-aig4b/talks/clase-03-prompting`, donde había sido reconstruida 1:1 desde `AIG4B-Clase-3-Prompting.pptx`. No nació del workflow de este repo: llega con `draft.md` completo y corpus ya procesado, sin haber pasado por Frame/Collect/Corpus acá.

---

## 2026-08-28 — Importación
- Status: complete
- What was decided: adaptar la Talk al sujeto de este repo en lugar de re-derivarla.
- Cambios aplicados al frontmatter de `draft.md`:
  - `presentation:` "Inteligencia Artificial Generativa Aplicada en Biomedicina" → "Inteligencia Artificial Generativa (AI Gen)"
  - `class:` se quitó el prefijo "Clase 3 —" (la numeración de este repo es otra)
  - `presenter:` "Paulo Veiga, Docente de Universidad Austral" → los tres docentes de `config/profile.md`
  - `audience:` bioingeniería → Ingeniería de Software
  - `duration:` 120 min (clase doble) → 90 min (default del repo)
  - `date:` vacío → 2026-09-02
- Estructura normalizada a la convención del repo:
  - `images/` creada con las 337 imágenes que el draft referencia (venían solo en `research/articles/AIG4B-Clase-3-Prompting-media/`)
  - `AIG4B-Clase-3-Prompting.pptx` movido de la raíz a `research/articles/`
  - `output/` y `research/llm-chats/` creadas vacías
- Files created/modified: `draft.md` (frontmatter), `images/` (337), `memory.md`, `output/`, `research/llm-chats/`
- Pending open questions:
  - ~~Duración: 120 min de contenido contra 90 de presupuesto~~ → **resuelto 2026-08-28: la clase se dicta en 2:30 h (150 min). No se recorta.**
  - **Tesis sin escribir:** el `# Thesis` está vacío, con un bullet `[open]` heredado del original.
  - **Sin `final.md`:** nunca pasó por Step 6 (Polish), así que tampoco hay deck renderizado ni enlace para el README.

## 2026-08-28 — Revisión + título
- Status: complete
- What was decided: el título "Ingeniería de prompts y técnicas avanzadas" subestimaba el alcance. Solo 3 de las 6 secciones son prompting; las otras son selección de modelo, economía de tokens y disciplina de producción. Nuevo título: **"Trabajar con LLMs: prompts, costos y producción"**.
- Aplicado en: frontmatter `class:`, portada (slide 0.1, que además seguía diciendo "Aplicada en Biomedicina" y acreditaba a dos autores de la materia vieja), fila 5 del README raíz.
- Revisión editorial completa: 10 blockers, 12 majors, 8 minors. Los tres movimientos que desbloquean el resto:
  1. Fijar la tesis (vacía). Recomendación: "el LLM no razona, completa tokens — escribir los pasos intermedios ES el cómputo", con el trade-off calidad/costo como *why it matters*.
  2. Recorte de 24 slides: 110-130 min estimados contra 90 de presupuesto. Incluye 7 slides duplicadas verbatim (residuo del PPTX, después del cierre), 6 de 7 agendas repetidas y la sección médica completa.
  3. Re-emparejado etiqueta→definición en ~17 slides, desapareadas al reconstruir desde el PPTX.
- Pending open questions:
  - Cifras sin respaldo en el slide de CoT ("70% mejora / 35% menos errores") y las dos donas dibujadas sobre ellas.
  - Los 14 papers del corpus no se citan en ninguna slide; ReAct está procesado y no aparece.
  - El slide 22 importado debe moverse a abrir el bloque de razonamiento y normalizar el voseo.

## 2026-08-28 — Duración
- Status: complete
- What was decided: **la clase 5 se dicta en 2:30 h (150 min), no en los 90 min del default del repo.** El presentador decidió no recortar contenido.
- Efecto sobre la revisión: cae el blocker de duración y con él el plan de recorte de 24 slides. La estimación de entrega del deck completo era 110-130 min, así que entra en 150 con margen.
- Lo que NO cae: los cortes que la revisión pedía por razones ajenas a la duración siguen en pie — el bloque de 7 slides duplicadas verbatim (residuo del PPTX, quedaron después del slide de cierre), las 6 agendas repetidas y la sección médica (materia distinta, audiencia equivocada). Son problemas de coherencia, no de presupuesto.
- Pending: los módulos de práctica de 7.1 declaran "45-60 minutos". Sumados al deck dan 155-190 min y no entran ni en 2:30. Falta declarar en la slide si son clase o tarea.

## 2026-08-28 — Ronda de revisión aplicada (recontextualización a software)
- Status: complete
- What was decided: aplicar el punch-list del Composer bajo tres restricciones del presentador: la clase dura 150 min (sin recorte por duración), **no se borra ninguna slide** (lo que había que cortar se recontextualiza, se parte en dos o se marca), y **todo ejemplo médico o clínico pasa al dominio de ingeniería de software**, incluida la sección 6, que se reconvierte en lugar de cortarse.
- Key inputs: `research/corpus/AIG4B-Clase-3-Prompting.md.md` (§Raw excerpts, §Inconsistencies), los 14 registros web del corpus, `config/learnings.md` (L1-L10), `config/profile.md`, `${CLAUDE_PLUGIN_ROOT}/config/principles.md`, la skill `claude-api` (catálogo de modelos Claude, corte 2026-06-24) y la skill `talksmith:desrobotizar`.
- Qué se hizo, por bloque:
  - **Tesis y objetivos.** Se escribió `Claim` + `Why it matters` ("el modelo completa tokens; escribir los pasos intermedios ES el cómputo" / "cada punto de calidad se paga en tokens, latencia y dinero"). Se llenaron los 8 `Goal of this section` y el `Narrative arc`. Se cerró el `[open]` heredado del 2026-08-14.
  - **Recontextualización médica → software.** 3.1/3.2 (revisor de código senior), 3.3 (JSON severidad/archivo/línea/fix), 3.4 (XML sobre issues de GitHub, traducido del inglés), 4.4 (triage de issues), 5.5 (¿este diff introduce un bug?), 5.8 (stack trace), 5.10 (tres estrategias de refactor), 5.13 (pipeline de tickets), 2.6 (system prompt = guía de estilo + ADRs), 1.9 (alucinación de APIs y paquetes). Limpieza local en 1.10, 1.11, 2.8, 5.19, 5.20. **Sección 6 completa reconvertida** (ciclo de vida del software, exploración de código, casos de uso, riesgos de software, mitigaciones) y la slide de "Prompting y Medicina" movida allí como "Benchmarks: qué miden".
  - **Re-emparejado etiqueta→definición (L8)** en las ~17 slides que la reconstrucción desde el PPTX había desapareado, más conversión de todos los bullets etiquetados a la forma canónica del catálogo de plantillas (`- **Etiqueta** cuerpo`, sin em-dash).
  - **Texto truncado.** El párrafo del effort (2.1) y el de prompt chaining (5.12) **no se pudieron reponer verbatim**: el corpus los preserva igual de truncados. Se cerraron con información verificada (niveles de effort de la API de Claude) y con el trade-off que la propia slide declara, y quedó anotado en `Sources` de cada slide.
  - **Cifras.** 5.2: se retiraron el "70% de mejora" y el "35% menos errores" (sin fuente) y se pusieron ToT 4%→74% (Yao et al., 2023) y self-consistency +17,9% GSM8K / +11,0% SVAMP (Wang et al., 2022), aclarando que son mejoras **sobre el baseline de CoT**. 3.4: se retiraron el 40%/60% de reducción de alucinaciones (la fuente los atribuye a "teams report", sin estudio) y la afirmación quedó cualitativa. 2.4/2.5: un solo enunciado de ahorro, y la aritmética recalculada paso a paso ($1.503,00 → $423,00, ahorro $1.080,00 = 72%; el deck decía $450 y 70%).
  - **Catálogo de modelos.** Unificado contra la skill `claude-api` (corte 2026-06-24): Fable 5, Opus 5, Opus 4.8, Sonnet 5, Sonnet 4.6 y Haiku 4.5, con generación y ventana por fila. Correcciones: Sonnet 4.6 tiene 1M (el deck le daba 200K en 2.2), la lista de niveles de effort incluye `medium` (el deck lo omitía) y **"Fable 5" sí es un modelo real** con la tarifa que el deck declaraba, contra lo que sugería la inconsistencia 18 del corpus. Los precios de OpenAI, Google y Meta no se pudieron verificar: quedaron declarados como generación 2024 y marcados `[open]`.
  - **Agendas.** Las 7 agendas in-deck se alinearon al orden real de entrega, se les quitaron los ordinales escritos (L3), se sacaron las promesas de TOON y del "sistema de triage" que el deck no entrega, y cada una marca la sección en curso para que la repetición sirva de navegación.
  - **Slide 22 importada.** Movida a abrir el bloque de razonamiento (5.6), voseo y encuadre de negocio normalizados al registro del deck, bullet de effort retirado por solaparse con 2.1 (L6), `Sources` re-ancladas al corpus de esta Talk (`parametros-llm.md.md` no existe acá) y **reconciliada la contradicción terminológica**: *extended thinking* es el mecanismo, *thinking* / *deep thinking* son los modos de interfaz que lo gradúan.
  - **Títulos y slides sin título.** 7 títulos promovidos de cuerpo a H2 con la línea duplicada retirada (L5); todos los H2 dentro de 40 caracteres y todos los H1 de sección dentro de 25. 0.2 y 0.3 quedan vacías con un `[open]` cada una.
  - **Citas al corpus.** Los 14 registros web dejaron de estar sin usar: Wei, Wang, Yao (ToT), Yao (ReAct), Brown, DSPy, gpt-tokenizer y los dos de aitutorial se citan ahora en las slides que sostienen. **Se agregó una slide de ReAct** (5.11) y una de zero-shot vs. few-shot (4.2), que llenaba un vacío real del deck original.
  - **Notas del orador.** Escritas para **72 de 74 slides**. Las dos sin notas son 0.2 y 0.3, que están vacías a propósito.
  - **Slides partidas** (agrega, no borra): 1.8/1.9 (alucinaciones), 1.10/1.11 (mitigaciones), 2.2/2.3 (paisaje + árbol de decisión), 2.4/2.5 (caching + números), 2.7/2.8 (cascading), 3.1/3.2 (6 componentes + prompt completo), 6.5/6.6 (mitigaciones + para pensar).
- Files created/modified: `draft.md` (reescritura completa: 65 → **74 slides**, 2.965 → 2.722 líneas), `memory.md`.
- Pending open questions: 19 bullets `[open]` en `draft.md`, listados también en `# Open questions`. Los de mayor impacto:
  - Slides 0.2 y 0.3 vacías: falta decidir contenido o retirarlas.
  - Cifras de proveedores no-Anthropic (ventanas en 1.3, precios en 2.2) sin verificar.
  - Las 4 donas (`slide-19-1/2.png`, `slide-27-1/2.png`) ya no representan ningún dato: falta re-render o reemplazo en el Polish.
  - Bloque duplicado 5.22-5.27 (6 slides): conservado por la restricción de no borrar; falta decidir si se entrega.
  - Sección 6 quedó sin cifras: falta incorporar al corpus evidencia citable de adopción o benchmarks de software (SWE-bench, HumanEval, DORA).
  - Trabajo práctico de "triage con LLM": la agenda original lo prometía y nunca existió.
- **No se escribió `config/feedback-backlog.md`.** La ronda cerró 51 bullets de feedback en `draft.md` sin espejarlos al backlog, porque el encargo restringía la escritura a `draft.md` y `memory.md`. `feedback_cycle.py find-closed-unmirrored` los reporta como pendientes de `mirror-row`.

## 2026-08-28 — Pasada de diagramas
- Status: complete
- What was decided: cubrir el `[major]` del Composer sobre apoyo visual. El deck reconstruido desde el PPTX no traía ni un esquema: de 16 bloques con fence, 14 eran código y solo 2 eran diagramas (el árbol de decisión y el flujo de cascading, agregados en la ronda anterior). Las 331 imágenes que se limpiaron al importar eran íconos y flechas decorativas, nunca diagramas de contenido.
- Key inputs: lista de candidatos del coordinador, `config/learnings.md` L1 y L2, el presupuesto de densidad de `principles.md`, y la convención de bloque ` ```ascii ` + `<!-- ascii-note: -->` del rol Editor.
- Resultado: **12 diagramas ASCII render-driving**, todos con `ascii-note` (`intent` / `emphasize` / `labels`). Antes eran 2.
  - **Reemplazaron contenido** (9). La prosa desplazada bajó a las notas del orador en cada caso:
    - `1.2` contenedor de la ventana de contexto, con límite duro y desborde. Reemplazó las 4 tarjetas de componentes.
    - `1.3` barras proporcionales de ventanas (200K a 10M, con la de Llama 4 truncada). Reemplazó la tabla de tamaños.
    - `2.4` match por prefijo del caching, con la frontera `cache_control` y el fallo silencioso. Reemplazó 3 de las 4 buenas prácticas.
    - `3.1` los 6 componentes como bloque apilado, con el eje de atención alta-baja-alta que liga el orden al sesgo de recencia. Reemplazó los 6 bullets.
    - `4.1` progresión zero / few / many-shot como el mismo prompt con más ejemplos intercalados, más los ejes de tokens, precisión y costo. Reemplazó los 3 bullets de régimen.
    - `5.9` árbol de ToT con scores y ramas podadas, que es el punto entero de la técnica, cerrando con "CoT es este árbol con una sola rama". Reemplazó la línea "Generar → Evaluar → Seleccionar". La imagen del corpus (`slide-33-1.png`) no se borró: pasó a `<!-- aside: right -->`.
    - `5.11` lazo de ReAct (pensar → actuar → observar → repetir) cerrado contra la caja MUNDO. Reemplazó los 2 bullets con las afirmaciones del paper.
    - `5.12` tubería de triage de tickets, con el dato que viaja entre etapas rotulado y el modelo caro solo en el último paso. Reemplazó la lista de 5 pasos.
    - `6.1` ciclo de vida cerrado de seis estadios, con el retorno de incidente a issue. La columna "Hacia dónde va" de la tabla bajó a notas para respetar el presupuesto de densidad.
  - **Se sumó sin reemplazar** (1): `5.4` fan-out y fan-in de self-consistency, con un camino disidente visible. El bullet de costo bajó a notas por densidad.
  - **Ya existían** (2): `2.3` árbol de decisión de modelo y `2.7` flujo de cascading. Al 2.3 le faltaba el `ascii-note`, que se agregó en esta ronda.
  - Aparte de estos 12, la slide `5.6` (razonamiento en tres escalones) ya traía su diagrama renderizado como PNG desde la Talk de origen, con su `ascii-source` y su `ascii-note` intactos.
- Casos evaluados y descartados por decorativos: la bola de nieve del costo (1.6) y las tablas de caching (2.5), donde la tabla ya transmite la proporción; y las listas de mitigación (1.10, 1.11), que no tienen forma propia.
- Consistencia visual (L1): dentro de cada sección los diagramas comparten tratamiento, y la forma cambia solo cuando el concepto lo pide. Contenedor para lo que contiene, barras para lo que compara magnitudes, tubería para lo que encadena, lazo cerrado para lo que interactúa con un entorno, árbol para lo que ramifica y poda.
- **Los 14 bloques de código siguen intactos**, cada uno con su `<!-- ascii-render: documentation-only -->`: verificado con `polish_ascii.py scan` (0 bloques de código sin tag, 0 diagramas suprimidos por error). El árbol de ToT necesitó `<!-- ascii-render: force -->` porque su slide lleva un aside con imagen, que por defecto habría suprimido el bloque.
- Files created/modified: `draft.md` (2.724 → 2.971 líneas; 74 slides, sin altas ni bajas), `memory.md`.
- Pending open questions: sin cambios respecto de la ronda anterior (19 `[open]`). Los diagramas nuevos no abrieron ninguno: todos se apoyan en contenido que ya estaba verificado en la lámina.
## 2026-08-28 — Step 6 (Polish), paso 2: limpieza de entrega de `final.md`
- Status: complete
- What was decided: cerrar el Polish sobre `final.md` sin tocar contenido. La pasada es mecánica — consolidación de imágenes, rescate de feedback abierto y eliminación del andamiaje de proceso. No se corrió anti-slop (la prosa ya se autoró bajo ese estándar en Steps 4-5) ni se reescribió ninguna slide.
- Key inputs: `final.md` tal como lo dejó el ilustrador (2.816 líneas, 72 slides, 12 diagramas ya renderizados con sello de idempotencia), `research/corpus/AIG4B-Clase-3-Prompting.md/images/`, y las skills `talksmith:feedback-cycle` (`rescue-open`, `strip_feedback.py`).
- Qué se hizo, por acción del contrato:
  - **(a) Inline SVG — no aplica.** Los 12 diagramas ya venían renderizados con sus `.svg`, su `.png` entregable y su `<!-- ascii-source: -->`. No se re-renderizó ninguno ni se tocaron los sellos. Los 14 bloques de código con `<!-- ascii-render: documentation-only -->` quedaron **byte por byte idénticos**, verificado por hash SHA-256 del conjunto de bloques con fence antes y después de la pasada (`d1a1d99f…5af7` en ambos extremos).
  - **(a′) Asides generados — no aplica.** Cero directivas `generate-image` en el deck.
  - **(b) Consolidación de imágenes.** **9 archivos copiados** de `research/corpus/AIG4B-Clase-3-Prompting.md/images/` a `images/` (`slide-01-1.png`, `slide-08-1.jpg`, `slide-11-1.jpg`, `slide-19-1.png`, `slide-19-2.png`, `slide-27-1.png`, `slide-27-2.png`, `slide-33-1.png`, `slide-62-1.png`). Copia, no movimiento: el corpus queda intacto como fuente. Sin colisiones de nombre.
  - **(b) Auditoría Keynote-safe.** **21 referencias reescritas** en total: las 9 de corpus más **12 de `.svg` a su `.png` compañero** (Keynote no rasteriza SVG embebido y lo muestra como caja vacía al importar el `.pptx`). Los `.svg` siguen en `images/` como fuente de verdad. No hizo falta rasterizar nada: el corpus solo traía PNG y JPG, sin WebP, AVIF ni HEIC. **`final.md` referencia hoy 22 imágenes, todas `.png` o `.jpg`, y las 22 resuelven en disco** — verificado archivo por archivo.
  - Los dos `<!-- aside: right ![...](...) -->` (Gandalf en la slide del millón de tokens, y el diagrama de tres pasos en la de Tree of Thought) se preservaron como hints: solo se les reescribió la ruta a `images/`.
  - **(c) Rescate de feedback abierto.** `feedback_cycle.py rescue-open` levantó los **17 bullets `[open]`** y los agregó verbatim al final de `# Open questions`, cada uno con la slide que lo originó. Ninguno se perdió al borrar la sección de feedback en el paso siguiente. Conviven con el resumen curado de 12 entradas que ya estaba en esa sección, que sigue siendo la vista corta para el presentador.
  - **(d) Eliminación del andamiaje.** `strip_feedback.py` quitó **82 bloques**: 72 campos `### Presenter feedback` (uno por slide) y 10 en forma de párrafo `**Presenter feedback:**` (tesis, agenda y niveles de sección). Cero bullets legacy. El script garantiza la línea en blanco antes de cada `---`, así que ningún borde de slide quedó convertible en subrayado setext. `final.md` bajó de 2.816 a 2.468 líneas y de 182 KB a 155 KB.
- Preservado a propósito: los **6 comentarios `<!-- DUPLICADO ... -->`** del bloque duplicado que sigue a la lámina de cierre. Son el único marcador que queda para encontrar esas slides y la decisión sobre ellas sigue abierta. No se movieron ni se editaron.
- Files created/modified: `final.md` (limpieza de entrega), 9 imágenes nuevas en `images/`, `memory.md`. **`draft.md` no se tocó** — sigue congelado como fuente de verdad del contenido, con su registro de feedback completo.
- Pending open questions: los mismos 17, ahora todos visibles en `# Open questions` de `final.md`. Los que bloquean una entrega tranquila: las cifras de proveedores no-Anthropic (ventanas en 1.3, precios en 2.2) siguen sin verificar; las 4 donas (`slide-19-1/2.png`, `slide-27-1/2.png`) están consolidadas en `images/` pero **siguen dibujadas sobre cifras retiradas**, así que falta decidir si se re-renderizan o se sacan; y el bloque duplicado 5.22-5.27 sigue sin resolución.
- Nota de herramienta: la slide 5.6 referencia `images/s4-1-1-tres-niveles-razonamiento.png`, que tiene su `<!-- ascii-source: -->` pero **no tiene `.svg` ni `.ascii` sidecar** en `images/` — vino ya renderizada como PNG desde la Talk de origen. La referencia resuelve y la entrega no corre riesgo, pero ese diagrama no se puede re-renderizar desde su fuente si hiciera falta.
