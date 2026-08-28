# memory.md — prompting

**Current step:** 5 (Review) — importada desde otro repo; pendiente de revisión y Polish
**Awaiting:** confirmación de a qué clase del README corresponde (candidata: clase 5, miércoles 2 de septiembre)
**Topic:** Ingeniería de prompts y técnicas avanzadas — fundamentos de foundational models, ventana de contexto, tokens, técnicas de prompting
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
  - **Duración:** el deck fue escrito para 120 min y acá el default son 90. Sin recorte, la clase se pasa.
  - **Tesis sin escribir:** el `# Thesis` está vacío, con un bullet `[open]` heredado del original.
  - **Sin `final.md`:** nunca pasó por Step 6 (Polish), así que tampoco hay deck renderizado ni enlace para el README.
