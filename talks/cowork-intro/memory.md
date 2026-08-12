# memory.md — cowork-intro (ex clase2)

**Current step:** 8 — Learnings awaiting_presenter (promociones de reglas y biblioteca pendientes)
**Nota de rename:** la carpeta paso de `talks/clase2/` a `talks/cowork-intro/` en el remoto (commit f66f9ee); todas las referencias internas a `talks/clase2/` en este archivo y en CLAUDE.md se leen como `talks/cowork-intro/`.
Render vigente 2026-08-12: `html-strict` post ronda 5, 33 laminas (portada + 8 section-agenda + 24 de contenido + El manejo del contexto) en `output/html/index.html`; reemplaza al render de 32 laminas que otra sesion habia subido desde el contenido pre-ronda-5. Preflights limpios. La directiva generate-image de la 1.1 sigue sin generar (sesion sin capacidad de imagenes).
Ronda 6 (2026-08-12): se realizaron y se integraron dos ilustraciones editoriales laterales: derecha en 1.1 (el trabajo de desarrollo que excede escribir código) e izquierda en 7.1 (la historia de Corta). `final.md` fue re-pulido y el HTML se reconstruyó con el renderer y CSS de Talksmith 0.83.3; las columnas laterales usan los diseños `column-right` y `column-left` actuales.
Ronda 5 (2026-08-12, sobre el deck renderizado): lamina nueva "El manejo del contexto" (/compact, ventana finita, contexto > prompting); iterar reescrita (tests como unidad de revision, TDD, SPEC.md); retitulados anti-slop (El cerebro en Markdown; El conocimiento del proyecto en .md; Conclusiones; "El nuevo rol: Diseñar, delegar y revisar"); directorios MCP oficiales en 6.4; "specs" del paso 0 renombrado a "documentacion de los MCP servers"; premisa sin-specs + seccion SPEC.md/TDD en mission.md.
**Post-proceso obligatorio del render:** despues de cada `build_html.py`, correr `python3 talks/cowork-intro/postprocess-subagent-colors.py` (colores por campo en la lamina del subagente; idempotente).
Polish 2026-08-12: 6 diagramas ASCII renderizados a SVG+PNG, todos clean a la primera pasada del critico (logs en images/.critique/). Ronda 5 de Review absorbida en el mismo paso: laminas nuevas 2.3 (Markdown, formato del ecosistema) y 2.4 (conocimiento en .md) por pedido del presentador; iterar paso a 2.5; 24 laminas, ~74 min. La directiva generate-image de la 1.1 quedo sin generar (sesion sin capacidad de generacion de imagenes); reintentar en una sesion con esa capacidad re-corriendo Polish. final.md limpio: refs a .png, sin campos de feedback.
Ronda 3 (2026-08-12): nuevo extra de la mision, la Skill /collect-memory (mission.md + lamina 7.2).
Ronda 4 (2026-08-12): bullets del presentador en el draft: dos frases slop cortadas de la 1.4 (y de Conclusions 1) y la 3.2 reescrita con las dos fuentes del CLAUDE.md (repo + instrucciones de la conversacion).
**Awaiting:** siguiente ronda de feedback del presentador sobre `draft.md`, o el ready-signal para pasar a Polish. Ronda 1 (2026-08-12) aplicada: la mision descentrada de la teoria (secciones 1 a 6 generalizadas) y la seccion MCP ampliada al ecosistema de desarrollo (nueva 6.3); detalle de GitHub/Railway movido a la 7.1.
**Mode:** B (Agent Draft) — el borrador sale del plan de `CLAUDE.md` y de los dos decks del MiM como fuente.
**Topic:** Clase 2 de la materia de ingeniería informática: agentes de código (Claude Code / Codex), el repo como contexto, CLAUDE.md como contrato, Skills, subagentes, MCP servers y la misión Corta.
**Folder:** talks/cowork-intro/ (ex talks/clase2/)
**Started:** 2026-08-12

---

## Talk briefing

Versión adaptada a ingeniería de la clase Claude Cowork del MiM (IAE): mismos conceptos, pero en el mundo del código con Claude Code / Codex, y con la misión Corta integrada en la misma clase. El plan completo, el mapeo de secciones y las decisiones viven en `talks/clase2/CLAUDE.md` (leerlo entero antes de tocar el draft). Fuentes: `talks/claude-cowork/draft.md` (estructura base, territorio de Paulo, no se edita) y `talks/claude-desktop-chat/draft.md` (encuadre introductorio, argumento de contexto, material MCP, Schedule).

---

## 2026-08-12 — Steps 1 a 4 (Frame + Draft inicial)

- Status: complete (draft inicial), esperando Review
- Asks log:
  - 2026-08-12 — "¿MCP antes o después de Skills/Subagentes?" → como recomendado: MCP al final de la teoría, pegada a la misión.
  - 2026-08-12 — "¿Profundidad de Skills y Subagentes?" → breve, 2 slides cada una.
  - 2026-08-12 — "¿Duración?" → 90 minutos.
  - 2026-08-12 — "¿Byline?" → Paulo Veiga y Marco Sánchez Sorondo.
  - 2026-08-12 — "Fuentes" → usar también `claude-desktop-chat`, no solo `claude-cowork`.
- What was decided: mapeo de secciones validado; deck de 8 bloques (6 secciones + Conclusions + misión), 22 laminas.
- Files created/modified: `talks/clase2/draft.md` (nuevo), `talks/clase2/memory.md` (nuevo), árbol `research/ images/ output/`, `talks/clase2/CLAUDE.md` (decisiones y mapeo actualizados).
- Pending open questions: ver `# Open questions` del draft (fecha exacta de la clase; URLs de docs de Claude Code y Codex pendientes de verificación; confirmar tiempos contra 90 min tras la primera pasada del presentador).
