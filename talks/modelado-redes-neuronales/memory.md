# memory.md — modelado-redes-neuronales

**Current step:** complete
**Topic:** Diseño y modelado de una red neuronal — entradas/salidas, matriz de confusión, overfitting y regularización L2
**Folder:** talks/modelado-redes-neuronales/
**Started:** 2026-08-18

---

## Talk briefing

quiero crear una nueva presentacion que va a cubrir aspectos del diseno y input, output de una red neuronal. Como se modela, red de confusion y overfitting y L2.

---

## 2026-08-18 — Step 1 (Frame)
- Status: in_progress
- Asks log:
  - 2026-08-18 — "¿Nueva presentación o retomar una existente?" → Nueva
  - 2026-08-18 — "¿Qué buscás con esta clase? + candidatos de nombre de carpeta" → Eligió carpeta `modelado-redes-neuronales` (opción 3); detalle de objetivos pendiente
  - 2026-08-18 — "Nombre de carpeta (kebab-case)" → modelado-redes-neuronales
- What was decided: Nueva presentación sobre diseño/modelado de una red neuronal (input/output, matriz de confusión, overfitting, L2). Carpeta `modelado-redes-neuronales`.
- Key inputs: Briefing verbatim (arriba). Profile completo (Español, 90 min, estudiantes de Ing. de Software).
- Files created/modified: talks/modelado-redes-neuronales/ (tree), memory.md
- Pending open questions: Objetivos finos de la clase sin detallar; nivel de la audiencia (intro vs. profundización) por confirmar en Step 4.

## 2026-08-18 — Step 2 (Collect)
- Status: complete
- Asks log:
  - 2026-08-18 — "¿Cómo querés traer material? (4 canales)" → Soltó 1 archivo en research/llm-chats/ y dijo "listo"
- What was decided: 1 fuente aportada (chat.md), avanzar a corpus.
- Key inputs: research/llm-chats/chat.md — guía de referencia "Modelado de inputs y outputs en redes neuronales" (~1070 líneas, sin imágenes).
- Files created/modified: research/llm-chats/chat.md (aportado por el presentador)
- Pending open questions: none

## 2026-08-18 — Step 3 (Corpus)
- Status: complete
- Asks log: none
- What was decided: 1 registro de corpus creado (chat-export), sin imágenes que procesar.
- Key inputs: chat.md → registro losless con las 13 secciones.
- Files created/modified: research/corpus/chat.md.md, research/corpus/chat.md/images/ (companion vacío)
- Pending open questions: **La fuente NO cubre matriz de confusión** (mencionada en el briefing) — gap a cubrir en Step 4 con conocimiento del agente o fuente extra.

## 2026-08-18 — Step 4 (Draft)
- Status: complete
- Asks log:
  - 2026-08-18 — "class, date, y modo de borrador (A/B/C)" → Modo B; class y date se defaultearon (class="Diseño de redes neuronales: del dato a la predicción", date="a definir") para no bloquear, ajustables en Review
- What was decided: Borrador completo end-to-end (Modo B) desde el corpus + conocimiento del área para la matriz de confusión. 6 secciones + Conclusiones, ~25 slides para 90 min. Revisión interna (Composer scope=full) aplicada: títulos de sección/slide dentro de presupuesto, slide 5.1 dividida (tenía tabla+diagrama), estilo anti-slop y sin em-dashes. Verificado contra learnings.md L1–L7 (respetados).
- Key inputs: corpus/chat.md.md (secciones 1,2,3,5,6 + conclusiones); conocimiento del área (sección 4, matriz de confusión — no en corpus).
- Files created/modified: draft.md
- Pending open questions: (1) Sección 4 sin fuente en corpus — sumar fuente propia si se quiere anclar números. (2) Duración: sección 2 cargada; candidatas a recorte 4.4 y 6.2. (3) class/date por confirmar.

## 2026-08-18 — Step 5 (Review)
- Status: complete
- Asks log:
  - 2026-08-18 — "Revisá draft.md y dejá bullets de feedback / avisá cuando esté listo" → "Hay introduccion a matriz de confusion cobierto?" (consulta, respondida: sí, sección 4; no viene del corpus) + "Listo, dalo por completo y generá la presentación"
- What was decided: Presentador aprobó el borrador sin bullets de feedback. draft.md congelado.
- Key inputs: ninguna edición; consulta sobre cobertura de matriz de confusión (sección 4, desde conocimiento del área).
- Files created/modified: ninguno (sin ronda de feedback)
- Pending open questions: none

## 2026-08-18 — Step 6 (Polish)
- Status: complete
- Asks log: none (paso automático)
- What was decided: cp draft.md → final.md; 5 diagramas ASCII dibujados a SVG y validados (viewBox ok); fences reemplazadas por refs de imagen; campos Presenter feedback quitados (33 bloques); sin [open] que rescatar. Dos pistas de plantilla corregidas en final.md (1.1 y 4.1). Sin cairosvg/PNG (no hace falta para HTML).
- Key inputs: final.md, 5 SVGs en images/.
- Files created/modified: final.md, images/s1-3-1-neurona.svg, images/s2-4-1-one-hot.svg, images/s4-2-1-matriz-confusion.svg, images/s5-2-1-curvas-overfitting.svg, images/s6-1-1-objetivo-l2.svg
- Pending open questions: none

## 2026-08-18 — Step 7 (Render)
- Status: complete
- Asks log:
  - 2026-08-18 — "Formato de render (pptx-strict / pptx-free-form / html-strict / skip)" → html-strict (único viable: Cowork no disponible para .pptx)
- What was decided: Deck HTML (html-strict, Reveal.js) renderizado. Toolchain: venv en scratchpad con jinja2/markupsafe; slide-model.json FILLeado a mano (30 slides + portada = 33 render); model_freshness stamp; build_html.py. Sin avisos tras corregir 2 slides editorial→grid. Los 5 SVGs quedaron inlineados. pptx NO disponible (sin Cowork).
- Key inputs: output/slide-model.json, output/html/index.html, index.html (raíz).
- Files created/modified: output/slide-model.json, output/html/index.html, /index.html (índice raíz)
- Pending open questions: pptx pendiente si en el futuro hay Cowork; entorno de render usa venv en scratchpad (jinja2).

## 2026-08-18 — Step 8 (Learnings)
- Status: complete
- Asks log:
  - 2026-08-18 — "Promover esta Talk a la biblioteca de conocimiento compartida" → omitido al cerrar por pedido del presentador.
- What was decided: Se volvió a Draft para procesar 6 observaciones; se cerraron y registraron en el backlog. Se reabrió el flujo completo, se rehízo final.md y se renderizó html-strict. La Talk queda cerrada sin promoción a biblioteca.
- Key inputs: Feedback del presentador sobre foco tabular, ejemplos, activaciones, eliminación de una slide y un quiz de precisión/recall. Se detectaron dos oportunidades de imagen atmosférica; quedaron como directivas porque esta sesión no tenía capacidad de generación disponible.
- Files created/modified: draft.md, final.md, images/ (diagrama de matriz actualizado y sidecars), output/slide-model.json, output/html/index.html, config/feedback-backlog.md, /index.html.
- Pending open questions: Las dos directivas de imagen se pueden generar al reabrir esta Talk en una sesión con capacidad de imágenes.

## 2026-08-18 — Step 7 (Render) — re-render html-strict
- Status: complete
- Asks log: none (pedido directo: "completa la generacion de strict html para modelado")
- What was decided: Re-render limpio de html-strict tras confirmar que slide-model.json seguía fresco (sha256 == final.md; freshness check [fresh]). 33 slides. Se eliminó SVG huérfano images/s4-2-1-matriz-confusion.svg (final.md ahora referencia s4-3-1). Dos íconos inferidos ('email', 'remove_red_eye') sin entrada en el set → fallback a 'info' (cosmético, por diseño del renderer).
- Key inputs: output/slide-model.json (fresco), final.md.
- Files created/modified: output/html/index.html, output/html/.render.json, /index.html (raíz); eliminado images/s4-2-1-matriz-confusion.svg.
- Pending open questions: los 2 íconos fallback quedan como 'info'; para el glifo exacto habría que ajustar el wording de esas cards o aliasar en el plugin.
