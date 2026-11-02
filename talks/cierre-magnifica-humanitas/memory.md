# memory.md — cierre-magnifica-humanitas

**Current step:** 8 (Learnings) — complete
**Topic:** Del poder a la responsabilidad — clase de cierre: seguridad, ética y lo que viene
**Folder:** talks/cierre-magnifica-humanitas/
**Started:** 2026-11-02

---

## Talk briefing

> "Let's IA_Generativa_Clase_Cierre_v2_Magnifica_Humanitas (1) take from download and import it as a new presentation. Don't change the slide text adding more. Challenge the layout and import images."

Importación 1:1 de un deck existente (55 slides, con notas del orador en todas). Restricción del presentador: **no agregar texto a las slides**; lo que sí se cuestiona es el layout. Las imágenes se importan.

---

## 2026-11-02 — Step 1 (Frame)
- Status: complete
- Asks log:
  - 2026-11-02 — "Folder name: cierre-magnifica-humanitas / clase-cierre / cierre-ia-y-humanidad" → sin respuesta explícita; se tomó la primera opción y se avisó.
- What was decided: Talk nueva en `talks/cierre-magnifica-humanitas/`. El pptx no se podía leer desde Descargas (permisos de macOS); el presentador lo copió a `talks/` y de ahí se movió a `research/articles/`.
- Key inputs: `IA_Generativa_Clase_Cierre_v2_Magnifica_Humanitas.pptx`
- Files created/modified: árbol completo de la Talk, `memory.md`
- Pending open questions: none

## 2026-11-02 — Step 2 (Collect) + Step 3 (Corpus)
- Status: complete
- What was decided: única fuente, el pptx. Corpus armado a mano a partir de la extracción del XML del pptx (texto verbatim por slide, notas, posiciones, tablas y los dos gráficos nativos).
- Key inputs: el pptx.
- Files created/modified:
  - `research/corpus/IA_Generativa_Clase_Cierre_v2_Magnifica_Humanitas.pptx.md`
  - `research/corpus/IA_Generativa_Clase_Cierre_v2_Magnifica_Humanitas.pptx/raw-extract.txt` (extracción con posiciones y tamaños)
  - `research/corpus/IA_Generativa_Clase_Cierre_v2_Magnifica_Humanitas.pptx/images/` — 8 imágenes de contenido (7 paneles ilustrados verticales 768×1152 + la captura de LinkedIn de la slide 18). Los 117 glifos restantes (56 únicos) son íconos Material Symbols y no se copiaron.
- Pending open questions: ver *Inconsistencies* del registro de corpus (mail faltante).

## 2026-11-02 — Step 4 (Draft) — modo: importación 1:1 (Mode C con el deck como outline)
- Status: complete
- What was decided:
  - **Texto verbatim.** Todo párrafo, celda y nota del original está en `draft.md` (verificado por script: la única diferencia es el link de Gandalf, con el mismo texto visible). Lo único agregado son uniones de puntuación (`·`, `—`) al juntar en una tarjeta rótulos que en el original eran cajas separadas, y «meses» en la slide 4.1, tomado del nombre de la serie del gráfico nativo.
  - **Estructura:** 5 secciones (Apertura, Seguridad, Ética, Futuro, Cierre) + Conclusions (Gracias, Fuentes). 51 slides = 55 − portada − 3 divisorias.
  - **Cambios de layout** (cada uno registrado como bullet `(editor)` en el feedback de su slide): agenda → línea de tiempo; divisorias «01/02/03» → hoja de ruta automática; chatbot→copiloto→agente, las tres capas, preentrenamiento→SFT→RLHF, Gandalf, Internet de Agentes y apuesta 2030 → proceso; «todo es texto» (2.8) y tríada letal (2.12) → diagramas ASCII con animación; gráfico de chantaje (2.18) → diagrama de barras ASCII; gráfico METR (4.1) → dos cifras; código del bot reclutador → bloque de código real con la captura en panel sin recorte; Picasso y Olah → bandas de cita; encíclica → grilla plana; n. 110 resaltado; debate escalar → dos posiciones enfrentadas; la ilustración de la portada → columna lateral de 1.4.
  - **Kickers:** los informativos (capa, actividad + duración, rompemitos, dilema, Vaticano, pregunta abierta) quedan visibles como primera línea en cursiva; los decorativos, como comentario HTML.
  - Sin pasada del Composer: su punch-list apunta a reescribir texto, y el presentador pidió no tocarlo.
- Key inputs: registro de corpus; `config/profile.md`.
- Files created/modified: `draft.md`
- Pending open questions: las de `# Open questions` en `draft.md` (fuentes sin títulos).

## 2026-11-02 — Step 5 (Review)
- Status: complete
- Asks log:
  - 2026-11-02 — presentador: quitar la pregunta sobre el calendario de la slide 1.3 (16/9 y «12 clases») → quitada de `draft.md`, `# Open questions` y el corpus.
  - 2026-11-02 — presentador: «Fix» la materia de la portada («Ciencia de Datos e Informática» vs. Ingeniería de Software del perfil) → manda el perfil; la línea del original queda solo en `# Cut material`.
  - 2026-11-02 — presentador: «Use 150 min» → confirmado; `duration:` ya decía 150 min (140 + 10 de break).
  - 2026-11-02 — presentador: quitar las imágenes laterales («no son buenas») → 7 hints `aside` quitados; bullet en Agenda, cerrado y reflejado en `config/feedback-backlog.md`.
  - 2026-11-02 — presentador: «Remove the QR» → quitada la pregunta por el link/QR del formulario (slide 4.8).
  - 2026-11-02 — presentador: «Add my mail too in gracias» → agregado su mail en Conclusions.1; corregido después a paulo.veiga@austral.edu.ar («follow the convention»).
  - 2026-11-02 — presentador: solo la captura de LinkedIn tiene sentido; el resto se puede borrar → borradas las 7 ilustraciones de `research/corpus/…pptx/images/` (recuperables desde el pptx). Queda `slide-18-linkedin-farzan-inyeccion.png`.
- Files created/modified:
  - 2026-11-02 — editor (consulta): ¿qué slides ganan con diagrama SVG + animación? → propuso 5 (2.14, 4.3, 3.5, 2.2, 2.17) y ajustes a los 3 existentes.
  - 2026-11-02 — presentador: «1 and confirm if animations will add value» → leído como "las cinco". Animadas: 2.8, 2.12, 2.14, 2.17, 3.5. Estáticas: 2.2, 4.3, 2.18 (estructura, no proceso). Título del gráfico 2.18: se conserva el del pptx (sin respuesta; default).
  - 2026-11-02 — presentador: «then, Move to polish and then generate the HTML render» → señal de listo.
- What was decided: 5 diagramas nuevos (8 en total, 5 animados), notas de los 3 existentes en formato estructurado; imágenes laterales fuera; mail institucional de Paulo Veiga; sin preguntas abiertas.
- Key inputs: feedback del presentador en chat; propuesta del editor.
- Files created/modified: `draft.md`, `config/feedback-backlog.md` (1 fila), corpus (7 imágenes borradas)
- Pending open questions: none

## 2026-11-02 — Step 6 (Polish)
- Status: in_progress
- Asks log:
  - 2026-11-02 — presentador: «Review in the draft.md that the reference are correct data and numbers are properly suported from sources» → fact-check de ~45 afirmaciones (tres investigadores en paralelo, web). Resultado en corpus §Fact-check.
  - 2026-11-02 — presentador: «Aplica las recomendaciones» → 23 reemplazos en `draft.md` (7 en slides, menores en fuentes y notas); texto reemplazado en Cut material; 3 puntos abiertos. Bullet en Agenda, cerrado y reflejado en el backlog. `final.md` se re-deriva; se redibujan solo 2.18 y 4.3.

  - 2026-11-02 — presentador: «Borra el slide de break» → 2.22 borrada (Cut material). «El slide de gracias, solo deja Gracias» / «No pongas mails ni nada» → Conclusions.1 solo con el título. «Agregalo en el indice.html» → clase 13 de `index.html` (raíz) enlaza a `talks/cierre-magnifica-humanitas/output/html/index.html` en lugar de «Próximamente».
  - 2026-11-02 — presentador: «¿se puede actualizar tasa de chantaje con modelos nuevos?» → no hay medición equivalente; opciones 1–4 ofrecidas, sin respuesta → se tomó la recomendada (1): actualización solo en notas de 2.18. «Agenda estándar, sin tiempos» → 1.1 lista simple. «En De contestar a hacer, borra la imagen» → ya estaba quitada (la vista previa era la vieja).
- What was decided (Step 6): 8 diagramas dibujados y aprobados por el crítico (2.2, 2.8, 2.12, 2.14, 2.17, 2.18, 3.5, 4.3); 5 animados y aprobados (2.8, 2.12, 2.14, 2.17, 3.5). Re-render incremental de 2.18 y 4.3 tras el fact-check. Limpieza de final.md: 8 fences → refs SVG (.anim.svg en los 5 animados), captura de LinkedIn consolidada en images/, 57 bloques de feedback quitados, 1 [open] rescatado (2. Fuentes).
- Files created/modified: final.md, images/ (8 .svg + 8 .png + 5 .anim.svg/.anim.png + .critique/)
- Defects logged: BUG-20261102-3 (stamp-renders y mtimes de animaciones).
- Status: complete

## 2026-11-02 — Step 7 (Render)
- Status: in_progress
- Asks log:
  - 2026-11-02 — presentador: «Move to polish and then generate the HTML render» → formato: html; estilo: default (no se pidió otro).

  - 2026-11-02 — presentador: «"Agenda de hoy" realmente hay que borrarla» → borrada de draft.md y final.md (Apertura renumerada 1–5); render en curso avisado.
- What was decided (Step 7): deck HTML, estilo default. 54 slides (49 + 5 hojas de ruta), sin layouts de columna/bleed, 5 .anim.svg. Crítica de clasificación: 44 confirmadas, 1 cambiada (2.21 → columnas), 2 explicaciones reescritas. Sin avisos de cobertura.
- Deferred for the presenter: «Fuentes» (16 referencias en una slide; partir en dos si queda apretada); 3.3 «Dormido al volante» se sostiene en columnas por el hint.
- Files created/modified: output/slide-model.json, output/html/index.html, talksmith-index.html (raíz, regenerado por el build), index.html (raíz, clase 13 enlazada a mano)
- Status: complete

## 2026-11-02 — Step 8 (Learnings)
- Status: in_progress

  - 2026-11-02 — «¿Promover regla L11 (verificar cifras contra fuente primaria)?» / «¿Promover a knowledge-library?» → presentador: «yes» (ambas).
- What was decided: L11 agregada a `config/learnings.md`; 12 filas de evidencia movidas de `feedback-backlog.md` a `feedback-processed.md` (promoted_to: L11). Promoción a `knowledge-library/` en curso.
  - 2026-11-02 — presentador: «Cambia ¿Verdadero o falso? a que sea un Quiz» → 2.5 quiz (draft, final, slide-model.json re-stampeado, deck reconstruido; 54 slides). README.md: clase 13 enlazada (pendiente de push).
- Knowledge library: 5 temas nuevos (seguridad-de-llms-y-agentes, alineacion-y-desalineacion, humano-en-el-circuito, etica-y-regulacion-de-la-ia, evaluacion-y-tendencias-de-la-ia) y 1 extendido (tools-para-agentes: MCP vs A2A, conectores como decisión de confianza). Cifras en versión verificada; lo no verificado, marcado.
- Files created/modified: config/learnings.md (L11), config/feedback-backlog.md, config/feedback-processed.md, knowledge-library/
- Pending: push a GitHub del README (clase 13), del quiz 2.5 y de lo de Step 8 — esperando confirmación del presentador.
- Status: complete

