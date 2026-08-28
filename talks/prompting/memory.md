# memory.md — prompting

**Current step:** 5 (Review) — importada desde otro repo; pendiente de revisión y Polish
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
