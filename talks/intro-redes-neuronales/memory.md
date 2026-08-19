# memory.md — intro-redes-neuronales

**Current step:** 7 — Render complete
**Topic:** Introducción a redes neuronales — de la intuición a la red, la neurona y la capa, redes profundas, el recorrido completo, funciones de activación y backpropagation
**Folder:** talks/intro-redes-neuronales/
**Started:** 2026-08-19

---

## Talk briefing

"Ingestar @Intro-Redes-Neuronales-105min.pptx como una presentacion."

"Esta es una presetacion que se tiene que transformar en un nuevo talk."

Nombre de carpeta elegido: `intro-redes-neuronales`.

El material de origen es un mazo de 51 diapositivas, seis capítulos más cierre y anexo, con 41 imágenes y ninguna tabla. La portada dice "Inteligencia Artificial Generativa Aplicada en Biomedicina", o sea que viene de otra materia distinta a la de este repositorio (Ingeniería de Software). El archivo declara 105 minutos y el perfil del repositorio tiene 90 como default.

---

## 2026-08-19 — Step 1 (Frame)
- Status: complete
- Asks log:
  - 2026-08-19 — "¿Qué querés hacer con esta clase? ¿Adaptás el dominio a Ingeniería de Software o lo dejás en biomedicina? ¿Va antes o después de modelado-redes-neuronales?" → pendiente, el presentador respondió solo el nombre de carpeta
  - 2026-08-19 — "Nombre de carpeta: intro-redes-neuronales / de-la-intuicion-a-backpropagation / fundamentos-redes-neuronales" → intro-redes-neuronales
- What was decided: Talk nuevo a partir de un PPTX existente que se usa como fuente, no como deck a reconciliar. No corresponde el pipeline inverso (pptx-extract): eso sirve para recuperar ediciones hechas sobre un deck ya generado por Talksmith, y este mazo es material de origen.
- Key inputs: Intro-Redes-Neuronales-105min.pptx (12 MB, 51 diapositivas).
- Files created/modified: talks/intro-redes-neuronales/ (árbol completo), memory.md
- Pending open questions: (1) adaptación de dominio, biomedicina contra Ingeniería de Software; (2) orden respecto de modelado-redes-neuronales, que ya cubre neurona, capa, activaciones y el recorrido completo; (3) duración, 105 min declarados contra 90 del perfil. Las tres se deciden en Step 4, no bloquean la Colecta ni el Corpus.

## 2026-08-19 — Step 2 (Collect)
- Status: complete
- Asks log: none (la fuente vino con el pedido)
- What was decided: Una sola fuente, el PPTX, movido desde la raíz del repositorio a research/articles/. No estaba versionado en git, así que el movimiento no rompe nada.
- Key inputs: research/articles/Intro-Redes-Neuronales-105min.pptx
- Files created/modified: research/articles/Intro-Redes-Neuronales-105min.pptx (movido)
- Pending open questions: none

## 2026-08-19 — Step 3 (Corpus)
- Status: complete
- Asks log: none
- What was decided: Un registro de corpus a partir del PPTX, Phase 1. Se leyeron las 51 diapositivas respetando el orden vertical de los cuadros de texto dentro de cada una, y se extrajeron las imágenes deduplicando por hash sha256: el mazo tenía repeticiones y quedaron 41 únicas, nombradas s<NN>-<hash>.<ext> para conservar la diapositiva de origen. El registro reconstruye las tres tablas que en el PPTX eran cuadros de texto sueltos (parámetros contra hiperparámetros, las cuatro activaciones, y el glosario de símbolos), que aplanadas eran ilegibles.
- Key inputs: research/articles/Intro-Redes-Neuronales-105min.pptx
- Files created/modified: research/corpus/Intro-Redes-Neuronales-105min.pptx.md (445 líneas), research/corpus/Intro-Redes-Neuronales-105min.pptx/images/ (41 archivos, 12 MB)
- Pending open questions: (1) Phase 2 sin correr, las 41 imágenes tienen stub y esperan transcripción; es mucho volumen y conviene decidir si se transcriben todas o solo las del recorrido principal. (2) Siete inconsistencias del mazo quedaron anotadas en el registro, entre ellas el salto sin explicar de la tabla de dimensiones (el ejemplo es 8x9 y la tabla pasa a 100x4 sin decir de dónde salen las 100 unidades) y que la sigmoide se presenta como default en el capítulo 2 mientras que ReLU recién aparece como estándar en el 5. (3) El mazo no tiene notas del orador en ninguna diapositiva: todo el guion hay que escribirlo.

## 2026-08-19 — Step 4 (Draft)
- Status: complete
- Asks log:
  - 2026-08-19 — "Escribir el draft haciendo ingeniería inversa del PPTX" → Modo B, reconstrucción 1 a 1
  - 2026-08-19 — "El draft tiene que ser 1 a 1 con el pptx" → confirmado el criterio
- What was decided: Borrador completo por ingeniería inversa, 1 a 1 con el mazo original. Las 51 diapositivas del PPTX se mapean a 42 de contenido: la portada, la agenda, los seis separadores de capítulo y el separador del anexo los genera Talksmith y no se escriben como diapositivas. Siete secciones (los seis capítulos más el anexo) y Conclusions con las dos de cierre. Se conservaron verbatim las tres tablas (parámetros contra hiperparámetros, las cuatro activaciones, glosario de símbolos), los números del ejemplo del clima (8 entradas, 9 unidades, 72 conexiones, 81 parámetros, matriz 8x9) y las frases que el mazo remarca.
- Decisiones de criterio tomadas sin preguntar, porque "ingeniería inversa" las define: dominio sin adaptar (contenido tal cual, salvo la portada que sale del perfil del repositorio), duración 105 min como declara el mazo, y modo B.
- Imágenes: no se dibujó ningún ASCII. Se aplicó la regla de imagen primero del Editor y cada diapositiva referencia la imagen de su diapositiva de origen en el companion del corpus. El mapeo es fiable porque es 1 a 1, aunque las imágenes no estén transcritas.
- Notas del orador: el mazo original no tiene ninguna. Las 42 están escritas de cero, y varias avisan de problemas del original: el salto del 100x4 en la tabla de dimensiones (4.6), la sigmoide presentada como default antes de que aparezca ReLU (2.3 y 5.4), y qué diapositiva del anexo responde cada pregunta previsible.
- Key inputs: research/corpus/Intro-Redes-Neuronales-105min.pptx.md
- Files created/modified: draft.md (1120 líneas, 42 diapositivas)
- Pending open questions: siete, registradas en Open questions del borrador. Las tres que bloquean decisiones editoriales: adaptación de dominio en la diapositiva de cierre, orden respecto de modelado-redes-neuronales, y Phase 2 de las 41 imágenes sin correr.
- Defecto de proceso corregido en el momento: el primer intento usó heredoc sin comillas y el shell ejecutó los backticks del Markdown, comiéndose los nombres de variable en el texto. Se detectó verificando el archivo escrito y se rehízo con heredoc citado. Vale como recordatorio: al escribir Markdown con backticks desde bash, el heredoc va siempre citado.

## 2026-08-19 — Step 6 (Polish)
- Status: complete
- Asks log: none (paso automático)
- What was decided: cp draft.md a final.md. Cero bloques ASCII, porque el borrador referencia las imágenes del mazo original en vez de dibujar diagramas nuevos, así que no hubo pase de Diagram-Illustrator. Las 40 imágenes referenciadas se consolidaron del companion del corpus a talks/intro-redes-neuronales/images/ y las referencias se reescribieron a images/<basename>. Sin [open] que rescatar. 51 bloques de Presenter feedback quitados.
- Key inputs: draft.md, research/corpus/Intro-Redes-Neuronales-105min.pptx/images/
- Files created/modified: final.md, images/ (40 archivos, 12 MB)
- Pending open questions: las referencias siguen siendo .png porque las imágenes del mazo original ya son raster; no hay SVG en esta Talk.

## 2026-08-19 — Step 7 (Render)
- Status: complete
- Asks log:
  - 2026-08-19 — "generá el strict-html" → html-strict
- What was decided: slide-model.json derivado del borrador con un parser, no escrito a mano: con 42 diapositivas el riesgo de error de transcripción era mayor que el de un parser verificable. El parser extrae título, lead, cards, tablas, imágenes y notas, y asigna plantilla por forma del contenido. 50 diapositivas: 42 de contenido, 7 separadores de sección y el divisor de conclusiones. Reparto de plantillas: 14 content+cards+image, 9 content-image, 8 figures, 7 concept-breakdown, 4 value-columns.
- Tres defectos del parser detectados y corregidos por las auditorías, no a ojo: (1) el bucle hacía continue en el bloque de la sección y se saltaba todas sus diapositivas, con lo que el modelo salía con 10 en vez de 50; (2) las ocho diapositivas del mazo que traen dos o tres imágenes (diagrama más fórmula) usaban solo la primera, y pasaron a plantilla figures para que entren todas, con las cards bajadas a highlights para no perder texto; (3) el campo image de figures es un objeto {src, alt} y no un string, que es lo que espera el resolvedor de imágenes del renderer.
- Key inputs: final.md, schemas/slide-model.md
- Files created/modified: output/slide-model.json, output/html/index.html (16 MB, 44 imágenes embebidas, cero placeholders vacíos), /index.html
- Pending open questions: el deck pesa 16 MB porque las imágenes del mazo original son grandes y van embebidas en base64. Si molesta para compartir, conviene reescalarlas antes de un próximo render. El ícono 'remove_red_eye' cae a 'info', cosmético.
