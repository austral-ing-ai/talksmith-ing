# memory.md — como-se-entrena-un-llm

**Current step:** 8 — Learnings in_progress
**Mode:** B (Agent Draft)
**Topic:** Cómo se entrena un LLM (LLM model training).
**Folder:** talks/como-se-entrena-un-llm/
**Started:** 2026-09-25

---

## Talk briefing

The popoc va a ser sobre LLM model training.

---

## 2026-09-25 — Step 1 (Frame)
- Status: complete
- Asks log:
  - 2026-09-25 15:23 — "What's this talk about?" → "The popoc va a ser sobre LLM model training."
  - 2026-09-25 15:23 — "¿Querés sumar algo de contexto? / Nombre de la carpeta: entrenamiento-llm · como-se-entrena-un-llm · llm-training" → "como-se-entrena-un-llm" (sin contexto adicional)
- What was decided: Talk nueva sobre entrenamiento de LLMs; carpeta talks/como-se-entrena-un-llm/. Hereda defaults de config/profile.md (español, 90 min, alumnos de Ing. de Software).
- Key inputs: tema del presentador; relación con talks/transformers-a-fondo/ (su bloque 6 "Entrenamiento a vuelo de pájaro" y el pendiente "ampliar entrenamiento").
- Files created/modified: talks/como-se-entrena-un-llm/{memory.md, research/{articles,llm-chats,web,corpus}/, images/, output/}
- Pending open questions: alcance (pre-training / SFT / RLHF-DPO / escalado / datos) y profundidad — a definir en Step 4.

## 2026-09-25 — Step 2 (Collect)
- Status: complete
- Asks log:
  - 2026-09-25 15:23 — "Traé tus fuentes (archivos, ZIPs de chats, URLs o exploración en vivo) y avisá cuando termines." → "Listo, usemos todo esto como fuentes a ingestar." (sumó ~/Downloads/Data.pdf: notas e imágenes)
- What was decided: Fuente principal: libro AI Engineering (Chip Huyen), caps. de entrenamiento; como no hay copia del texto, se usan los papers que cita + resúmenes públicos del libro. Mapa bullet → fuente en research/plan-de-fuentes.md.
- Key inputs: Data.pdf (notas + 2 figuras del libro); pedido de una fuente sobre entrenamiento para tools (→ Lambert, RLHF Book cap. 13); pedido de páginas con resumen del libro (→ 4 páginas).
- Files created/modified: research/articles/Data.pdf (copiado de ~/Downloads/Data.pdf, 23 MB — notas + imágenes del presentador). 4 páginas (export de Apple Notes), mismo texto que el presentador pegó en chat. 2 imágenes: pág. 2 = foto de la Fig. 2-9 "Projection of historical trend of training dataset sizes and available data stock" (Villalobos et al., 2024); pág. 3 = foto rotada 90° de la Fig. 2-10 "The overall training workflow with pre-training, SFT, and RLHF". Ambas del libro AI Engineering (Chip Huyen, O'Reilly), cap. 2.
  - Plan de fuentes: research/plan-de-fuentes.md (bullets de Data.pdf → libro AI Engineering + papers citados).
  - 2026-09-25 19:37 — 15 papers de arXiv en research/articles/ (villalobos-2024, hoffmann-2022, kaplan-2020, ouyang-2022, raffel-2020, dodge-2021, shumailov-2023, longpre-2024, petrov-2023, rafailov-2023, touvron-2023, nakano-2021, schick-2023, deepseek-2025-r1, kalai-2025) y 3 web en research/web/ (huyen-2023-rlhf, jun-2023-languages-tokenized, lambert-rlhfbook-tool-use — pedido explícito del presentador: una fuente sobre cómo se entrena el uso de tools).
- Files created/modified (cont.): research/web/{huyen-aie-chapter-summaries, tonytvo-aie-summary, bagerbach-aie-notes, softwarephilosopher-aie-notes}
- Pending open questions: texto del libro AI Engineering (caps. 2, 7, 8) — lo tiene que aportar el presentador.

## 2026-09-25 — Step 3 (Corpus)
- Status: complete
- Asks log:
  - 2026-09-25 20:00 — "¿Qué hago con las 294 imágenes? 1 figuras clave (~25) / 2 todas / 3 solo texto / 4 más adelante" → "No las miremos en detalle, solo las que estaban en el PDF que te pasé. Borrá también todas las imágenes chicas."
- What was decided: corpus cerrado con 23 records (16 PDF + 7 web). Imágenes: solo se transcriben las 2 de Data.pdf; chicas borradas; páginas enteras reemplazadas por recortes de figura. El deck de la Clase 4 (fine-tuning) queda pendiente: se suma cuando el presentador lo copie a research/ (macOS bloquea la lectura de ~/Downloads).
- Key inputs: "Tomemos también de ~/Downloads/AIG4B-Clase-4-Fine-Tunning la sección de fine-tuning" (bloqueado por permisos); "Veo también imágenes de lo que parece PDF, no son solo figuras" → recorte; "2. Listá el corpus" → cerrar sin el deck.
- Files created/modified: research/corpus/ — 23 records (fase 1, todos ok), 294 imágenes extraídas; borradas 29 chicas (ambos lados < 300 px: avatares, íconos, logos, tapa) junto con sus stubs; transcriptas solo las 2 de Data.pdf; las demás quedan en disco con stub pending (diferidas por decisión del presentador). Luego, a pedido del presentador ("veo imágenes que parecen PDF, no son solo figuras" → opción 2, recortar): las 164 páginas enteras renderizadas se reemplazaron por 209 recortes de figura (206 automáticos + 3 a mano) y se borraron 2 páginas sin figura. Total en disco: 310 imágenes (2 transcriptas, resto pending).
- Pending open questions: deck Clase 4 (sección fine-tuning) por sumar; 3 bullets ambiguos de Data.pdf ("Chart de evolución… / Lost language", "This is part of SFT /", "Effort"); cifras "2 billion websites" y "Only 2%" sin fuente del libro; tonytvo-aie-summary mezcla dos libros (no citar su segunda mitad como AI Engineering).
- Asks log (cierre):
  - 2026-09-25 20:11 — "¿Espero el deck o cierro el corpus?" → "2. Listá el corpus."

## 2026-09-25 — Step 4 (Draft)
- Status: complete
- Asks log:
  - 2026-09-25 20:11 — "Clase (portada), fecha y modo de borrador" → "2. Quiero el borrador tuyo pero que tengas en cuenta esto: [notas de Data.pdf + nuevo bullet 'Fine Tuning (expand all in multiple sections)']" → Mode B. Clase y fecha sin responder: se usan provisorios (Clase 9: Cómo se entrena un LLM · 2026-09-30) y se confirman en Review.
- What was decided: Mode B (Agent Draft). draft.md final antes del Polish: 7 secciones más Apertura y Conclusiones, 43 láminas (Apertura 1; datos e idiomas 7; escala 5; del modelo base al chat 5; SFT y preferencias 6; herramientas y esfuerzo 9; cuando el modelo no sabe 3; fine-tuning 6; conclusión 1). Encuadre: dos fases (pre-training y post-training; el post tiene SFT y preferencias más habilidades; fine-tuning = post a escala chica), elegido por el Editor a partir del Composer. Se aplicaron todos los [blocker] y [major] del Composer (scope=full) y los [minor] baratos. La ronda de Review (Step 5) se saltea por decisión del presentador; se pasa directo al Polish.
- Key inputs: notas del presentador (Data.pdf + bloque de fine-tuning); corpus de 25 records (23 originales + gpt-oss y Qwen3 sumados el 2026-09-26); aclaraciones del presentador sobre effort, "2 billion websites" y compresión de secciones; punch-list del Composer; 6 bullets de Presenter feedback en draft.md (4 cerrados y espejados en config/feedback-backlog.md; 2 aplicados y dejados [open]: torta de 1.3 y términos en inglés de 3.4).
- Files created/modified: talks/como-se-entrena-un-llm/draft.md (creado y revisado tres veces); talks/como-se-entrena-un-llm/images/villalobos-2024-fig5-data-stock-projection.png (recorte del Editor de la Figura 5 de Villalobos); config/feedback-backlog.md (4 filas nuevas); memory.md.
- Pending open questions: frontmatter provisorio (¿Clase 9 o 10?, fecha); alcance de "términos en inglés" y torta de C4 (feedback [open]); cifra "2 mil millones" sin fuente; "Lost language" y gráfico de evolución de idiomas; acuerdos de datos sin fuente; deck de la Clase 4; claims de segunda mano del libro AI Engineering; imágenes con stub pendiente; figura de Villalobos en baja resolución. Detalle completo en # Open questions de draft.md.
- Notas del presentador para el borrador (verbatim, pegadas en Step 4; idénticas a Data.pdf salvo el bloque final):
  ```
      - Effort, example on how is trained for that.
      - Model just try to respond.
          - How is this prevented ?.
  	- Fine Tuning
  		(expand all in multiple sections)
  ```
- Fuentes agregadas en Step 4 para cubrir Fine-tuning: research/articles/hu-2021-lora.pdf, research/articles/dettmers-2023-qlora.pdf.
- Estado 2026-09-26 01:35: draft.md completo (50 slides, 15 secciones + conclusiones, escrito por el Editor en Mode B). Review completa pendiente: la revisión scope=full del Composer se cortó dos veces porque la Mac entró en reposo (tapa cerrada, a batería). Al retomar: correr Composer scope=full → Editor aplica [blocker]+[major] → handoff a Step 5 + live view (5.5).
- 2026-09-26 08:21 — Aclaraciones del presentador:
  - "effort: Sí, es cómo soporta el concepto de Effort Low, Medium, etc." → fuentes agregadas: research/articles/openai-2025-gpt-oss-model-card.pdf, research/articles/qwen-2025-qwen3-technical-report.pdf (corpus: gpt-oss no dice cómo entrena los niveles; Qwen3 entrena el switch /think-/no_think, el budget no se entrena).
  - "'2 billion websites': Es métricas sobre CommonCrawl y luego 'Google C4 (curated)' cómo lo depuró. La idea es mostrar fuentes de donde sale este tipo de info."
  - "La cantidad de secciones creo que se puede comprimir."
  - "Creá un draft2.md que siga lo que pensás vos como recomendado sin basarte en mi guidance." → draft2.md = versión alternativa del Editor con arco propio (no reemplaza a draft.md).
- Borrador del Editor (Mode B), 2026-09-25: draft.md con 15 secciones y 50 láminas, escrito desde el corpus y las notas del presentador.
- Revisión del Editor antes del Composer, 2026-09-26, con tres aclaraciones del presentador:
  - "effort: Sí, es cómo soporta el concepto de Effort Low, Medium, etc." → la parte de razonamiento se rehízo alrededor de low/medium/high (gpt-oss) y del interruptor y el presupuesto de pensamiento (Qwen3), con DeepSeek-R1 como base. Fuentes nuevas: research/corpus/openai-2025-gpt-oss-model-card.pdf.md, research/corpus/qwen-2025-qwen3-technical-report.pdf.md.
  - "Es métricas sobre CommonCrawl y luego 'Google C4 (curated)' cómo lo depuró. La idea es mostrar fuentes de donde sale este tipo de info." → la lámina 2.1 muestra cada cifra de escala de Common Crawl con su fuente.
  - "La cantidad de secciones creo que se puede comprimir." → 15 secciones pasan a 9 y 50 láminas a 43. Las láminas sacadas quedan con su texto completo en `# Cut material`.
- 2026-09-26 08:35 — "Move el draft2 como una presentacion nueva de como-se-entrena-un-llm2." → draft2.md pasa a talks/como-se-entrena-un-llm2/draft.md (Talk hermana, corpus copiado). Este Talk sigue con draft.md (43 slides, 9 secciones) en revisión del Composer.
- 2026-09-26 08:38 — "Luego, generá para ambas pasando a polish" → al cerrar la revisión del Composer y aplicar [blocker]+[major]: saltear la ronda de Review del presentador, Step 6 Polish y Step 7 Render con defaults (formats: html, style: default).

## 2026-09-26 — Step 6 (Polish)
- Status: complete
- Asks log:
- What was decided: polish-ascii cleanup rewrote the 15 ASCII fences to image refs, sa-1-1 (Apertura) included, so no hand fix was needed. 9 corpus images copied into images/ (one name clash: hu-2021 fig-01-p001.png → fig-01-p001-2.png, next to schick fig-01-p001.png). 15 diagram refs switched from .svg to their .png companion. villalobos-2024-fig1 kept as it was. rescue-open moved 2 [open] bullets (1.3 pie chart, 3.4 SFT/terms in English) to # Open questions. strip_feedback removed 53 blocks (43 H3 + 10 paragraph). No generate-image directives. final.md: 25 image refs, all PNG under images/, none broken.
- Key inputs: draft.md congelado → final.md (cp). Villalobos Fig. 1 re-render a 300 dpi por el orquestador antes del cp.
- Files created/modified: final.md; images/ (9 corpus PNGs copied in: efc0e934-…_871x444.png, fig-08-p015.png, p003-fig-2-10-training-workflow-rotated-upright.png, tool_use_generation.png, fig-01-p001.png, fig-01-p004.png, fig-03-p008.png, rag-vs-finetune.png, fig-01-p001-2.png); draft.md untouched.
- Pending open questions: 1.3 pie chart (the s1-3-1 render is already a pie; confirm it covers the request). 3.4 spell out SFT and settle whether the terms stay in English. Pending corpus stubs on the 9 images (already listed in # Open questions).

## 2026-09-26 — Step 7 (Render)
- Status: complete
- Asks log:
- What was decided: deck HTML con defaults (formats: html, style: default), por pedido previo del presentador. 52 slides + portada (43 de contenido + 9 de sección; la Apertura sin número quedó como primera sección). Revisión de clasificación: 42 confirmadas, 1 reclasificada (slide 21 → tarjetas + panel de código). Controles: 595/595 líneas, 43/43 notas, 25/25 imágenes.
- Key inputs: verificación visual del orquestador (53 capturas con fragmentos abiertos): sin recortes; la tabla de 8 filas de las conclusiones entra completa. Observaciones menores: la figura de GPT-3 vs InstructGPT (slide 19) queda chica para leer en proyección; la slide 21 usa la foto del libro (Fig. 2-10).
- Files created/modified: output/slide-model.json, output/html/index.html; index.html raíz reescrito.
- Pending open questions: none

## 2026-09-26 — Step 8 (Learnings)
- Status: in_progress
- Asks log:
- What was decided: <filled at closure>
- Key inputs: <filled at closure>
- Files created/modified: <list>
- Pending open questions: <list or "none">
- 2026-09-26 18:38 — "Las charlas dejalas así." → el presentador acepta ambos decks como están; los pendientes visuales y de contenido quedan registrados en este memory.md, sin re-Polish ni re-render.
