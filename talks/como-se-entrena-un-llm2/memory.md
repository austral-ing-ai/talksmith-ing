# memory.md — como-se-entrena-un-llm2

**Current step:** 7 — Render complete
**Mode:** B (Agent Draft)
**Topic:** Cómo se entrena un LLM — versión alternativa con arco propio del Editor.
**Folder:** talks/como-se-entrena-un-llm2/
**Started:** 2026-09-26

---

## Talk briefing

Creá un draft2.md que siga lo que pensás vos como recomendado sin basarte en mi guidance.

Move el draft2 como una presentacion nueva de como-se-entrena-un-llm2.

---

## 2026-09-26 — Step 1 (Frame)
- Status: complete
- Asks log:
  - 2026-09-26 08:35 — (sin pregunta) "Move el draft2 como una presentacion nueva de como-se-entrena-un-llm2." → carpeta creada por el orquestador.
- What was decided: Talk hermana de talks/como-se-entrena-un-llm/, mismo tema y mismo corpus, pero con tesis, arco y secciones propuestos por el Editor sin seguir las notas del presentador (Data.pdf).
- Key inputs: pedido verbatim del presentador (arriba).
- Files created/modified: talks/como-se-entrena-un-llm2/{memory.md, research/ (copia completa de talks/como-se-entrena-un-llm/research/ salvo plan-de-fuentes.md), images/, output/}
- Pending open questions: clase y fecha (provisorias: "Clase 9: Cómo se entrena un LLM", 2026-09-30).

## 2026-09-26 — Step 2 (Collect)
- Status: complete
- What was decided: sin intake propio; hereda las fuentes de talks/como-se-entrena-un-llm/ (Data.pdf, 19 papers, 7 capturas web).
- Pending open questions: none

## 2026-09-26 — Step 3 (Corpus)
- Status: complete
- What was decided: corpus copiado (27 records, imágenes incluidas) desde talks/como-se-entrena-un-llm/research/corpus/.
- Pending open questions: none

## 2026-09-26 — Step 4 (Draft)
- Status: complete
- Asks log:
- What was decided: Mode B. Tesis: un LLM se entrena dos veces; el pre-entrenamiento fija lo que sabe y el post-entrenamiento (de decenas de miles a ~1 millón de ejemplos, o un verificador) fija cómo se comporta; cada conducta sale de la señal que la premió. Arco causal en 6 secciones + conclusiones, 29 láminas, 81 min (~9 min de margen): 1 Dos entrenamientos (3), 2 Tamaño y datos (4), 3 De dónde salen los tokens (5), 4 Post-entrenamiento (6), 5 Conductas premiadas (5), 6 Ajustar un modelo (4), Conclusions (2). Se aplicaron los 2 [blocker], los 8 [major] y los [minor] de la revisión scope=full del Composer; las láminas ex 3.6 y ex 5.6 pasaron a Cut material, con su idea en las notas de 3.5 y 5.5. Step 5 (Review del presentador) salteado por decisión del presentador: draft.md queda congelado para Polish.
- Key inputs: el Editor empezó el borrador como talks/como-se-entrena-un-llm/draft2.md y lo movió acá como draft.md; corpus completo (27 records) sin seguir el orden de Data.pdf; aprendizajes L3, L5–L10 de config/learnings.md; revisión scope=full del Composer.
- Files created/modified: draft.md
- Pending open questions: portada provisoria y conflicto con el anuncio de la clase 8 ("variantes en la clase 9"); Kalai t = 0,75 (penalización 2 vs 3 por fórmula); tabla de Petrov reconstruida (verificar 1,55); proporción de inglés en Common Crawl (45 % vs 46 %); imágenes con stub pending de la fase 2 del librarian; recorte limpio de la figura de 3.5; posible selección manual del ejemplo de 1.1; sin reparto de cómputo post/pre para modelos actuales; Llama 3 solo vía Villalobos; ejercicios de cierre como sugerencia; libro AI Engineering solo por resúmenes; inferencia del Editor sobre logits en 6.4. Detalle en draft.md → Open questions.
- 2026-09-26 08:38 — "Luego, generá para ambas pasando a polish" → al cerrar la revisión del Composer y aplicar [blocker]+[major]: saltear la ronda de Review del presentador, Step 6 Polish y Step 7 Render con defaults (formats: html, style: default).
- 2026-09-26 — draft.md escrito por el Editor en Mode B como versión alternativa con arco propio (31 slides, 6 secciones + conclusiones); movido desde talks/como-se-entrena-un-llm/draft2.md. El orquestador agregó la sección 6, Conclusions, Open questions y Cut material (el append del Editor fue bloqueado por permisos; el presenter autorizó el append).
- 2026-09-26 — research/ reemplazado por symlink a ../como-se-entrena-un-llm/research (pedido del presentador: "No dupliques el corpus"). Corpus compartido entre las dos Talks.

## 2026-09-26 — Step 6 (Polish)
- Status: complete
- Asks log:
- What was decided: final.md producido desde draft.md congelado. (a) 1 bloque ASCII renderizado (s3-1-1-embudo-limpieza-c4) y reescrito a imagen con eco ascii-source + ascii-note conservados. (a′) 1 directiva generate-image (Conclusions lámina 2, sc-2-1) quedó sin generar: la sesión no tenía capacidad de imagen; la directiva queda en final.md para un Polish futuro y la lámina conserva su texto. (b) 10 referencias de imágenes del corpus copiadas a images/ y reescritas (colisión fig-01-p002.png → fig-01-p002-2.png para la figura de DPO); la ref .svg del diagrama pasó a su compañero .png; auditoría: las 11 refs son .png y resuelven. (c) rescue-open: 0 bullets [open]. (d) strip: 37 bloques Presenter feedback quitados (29 H3 + 8 de párrafo).
- Key inputs: draft.md congelado → final.md (cp). Verificado: 29 slides, 81 min, títulos en presupuesto, imágenes resuelven vía symlink. Plan anotado del diagram-illustrator; resultado `unavailable` del image-illustrator.
- Files created/modified: final.md; images/ (10 PNG copiados del corpus + diagrama s3-1-1-embudo-limpieza-c4 .ascii/.svg/.png del diagram-illustrator).
- Pending open questions: aside de sc-2-1 pendiente de una sesión con generación de imágenes; las Open questions de Step 4 siguen en final.md → Open questions.

## 2026-09-26 — Step 7 (Render)
- Status: complete
- Asks log:
- What was decided: deck HTML con defaults (formats: html, style: default), por pedido previo del presentador ("generá para ambas pasando a polish"). 36 slides + portada. Revisión de clasificación: 25 confirmadas, 3 cambios de formato (slides 20, 29, 34: fila → grilla, pisan la pista `format: row` del borrador). Pistas retiradas traducidas: `comparison` (slides 3, 23), `format: list` (26). Controles: 405/405 líneas, 29/29 notas.
- Key inputs: verificación visual del orquestador (capturas de las 37 vistas): slide 15 "El español paga más tokens" recorta la 8.ª fila de la tabla (Shan 15,05) sin aviso — bug de recorte silencioso de 1.0.0, corregido en 1.0.1 (que lo reporta). Slide 16 usa la foto del libro en lugar de la figura limpia de Villalobos. Slide 36: el cuerpo de las tarjetas sale en monoespaciado rojo.
- Files created/modified: output/slide-model.json, output/html/index.html; index.html raíz reescrito.
- Pending open questions: arreglar slide 15 (partir la tabla o quitar una fila) → requiere editar draft.md y re-Polish/re-render.
- 2026-09-26 18:38 — "Las charlas dejalas así." → el presentador acepta ambos decks como están; los pendientes visuales y de contenido quedan registrados en este memory.md, sin re-Polish ni re-render.
