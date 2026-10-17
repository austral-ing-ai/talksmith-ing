# memory.md — redes-generativas-antagonicas

**Current step:** 6 — Polish complete (final.md re-derivado; output/ desactualizado hasta re-renderizar Step 7)
**Topic:** Redes generativas antagónicas (GANs) — clase importada tal cual desde AIG4B (Clase 8, Biomedicina)
**Folder:** talks/redes-generativas-antagonicas/
**Started:** 2026-10-17

---

## Talk briefing

"Busca en /Users/pveiga/Documents/Austral/talksmith-aig4b la clase de adversarial networks" → "Ok. Copiala tal cual." → "La idea es que vamos a tomar esa clasa tal como esta y va a ser una nueva clase."

---

## 2026-10-17 — Steps 1–5 (importación)
- Status: complete
- Asks log:
  - 2026-10-17 — "¿Armo la clase 12 combinando GANs + Stable Diffusion, solo GANs, u otra cosa?" → "Ok. Copiala tal cual." / "vamos a tomar esa clase tal como esta y va a ser una nueva clase."
- What was decided: Talk importada byte a byte desde talksmith-aig4b/talks/clase-08-gans/ (draft.md 52 slides, pptx original, research/ con corpus de 15 registros). Contenido sin cambios. Solo se actualizó el frontmatter a esta materia: presentation (profile Subject), class sin "Clase 8 —", presenter y audience del profile, date 2026-10-28 (clase 12 del README: "Vision: Stable Diffusion y Adversarial Networks"). Duración original conservada (120 min).
- Key inputs: talksmith-aig4b/talks/clase-08-gans (sin memory.md, final.md ni output/ en el origen).
- Files created/modified: talks/redes-generativas-antagonicas/ (copia; importada como clase-08-gans y renombrada el 2026-10-17 a kebab-case por tema), draft.md (frontmatter), memory.md (este archivo)
- Pending open questions: dos bullets [open] heredados del origen (tesis no escrita; falta slide de cierre) — se conservan; el contenido sigue orientado a Biomedicina (público original). [encuadre resuelto 2026-10-17 — ver entrada «Step 5 (Review) — reencuadre para ingenieros»; ejemplos resueltos 2026-10-17 — ver «Step 5 (Review) — reemplazo de ejemplos»] Carpeta renombrada de "clase-08-gans" a "redes-generativas-antagonicas" (2026-10-17) para seguir la convención de nombres por tema.

## 2026-10-17 — Step 6 (Polish)
- Status: complete
- What was decided: cp draft.md → final.md; 0 ASCII blocks (nothing to render); 0 generate-image directives; rescue-open: 2 [open] bullets → # Open questions; strip_feedback: 60 blocks; 72 image refs consolidated from research/corpus/…/images/ into images/ (png/jpg, 0 missing).
- Files created/modified: final.md, images/ (72 files)
- Pending open questions: tesis vacía y slide de cierre sin escribir (heredado).

## 2026-10-17 — Step 5 (Review) — quitar agendas
- Status: complete
- Asks log:
  - 2026-10-17 — Presenter: "Lo que estoy buscando es seguro del PPT extraer todas las imagenes y ningun cambio en los slides por ahora." → verified: 86/86 pptx media already extracted (research/articles/AIG4B-Clase-8-GANs-media, + _manifest.json); 72 raster used by slides. Render stopped.
  - 2026-10-17 — Presenter: "Listo, tomemos el daft (confirmemos que no hay cambio con respecto a el PPTx). Si boremos las agenda etc por que vas a regenerala." → fidelity check: 51/51 slides, 723/723 text runs present, per-slide raster images identical by hash, pptx has no speaker notes. Removed to Cut material: slide 1 (portada), slides 2/9/17/38/48 (agenda repetida), "# 0. Portada" section, empty Conclusions "Key takeaways" placeholder (not in pptx). 45 slides remain, unchanged; ## renumbered per section.
- Files created/modified: draft.md, final.md (regenerated: rescue-open, strip_feedback, image refs → images/)

## 2026-10-17 — Step 5 (Review) — quitar agendas
- Status: complete
- Asks log:
  - 2026-10-17 — Presenter: "Lo que estoy buscando es seguro del PPT extraer todas las imagenes y ningun cambio en los slides por ahora." → verified: 86/86 pptx media already extracted (research/articles/AIG4B-Clase-8-GANs-media, + _manifest.json); 72 raster used by slides. First render stopped.
  - 2026-10-17 — Presenter: "Listo, tomemos el daft (confirmemos que no hay cambio con respecto a el PPTx). Si boremos las agenda etc por que vas a regenerala." → fidelity check: 51/51 slides, 723/723 text runs present, per-slide raster images identical by hash, pptx has no speaker notes. Removed to Cut material: slide 1 (portada), slides 2/9/17/38/48 (agenda repetida), "# 0. Portada" section, empty Conclusions "Key takeaways" placeholder (not in pptx). 45 slides remain, unchanged; ## renumbered per section.
- Files created/modified: draft.md, final.md (regenerated: rescue-open 2, strip_feedback 60, 71 image refs → images/)

## 2026-10-17 — Step 7 (Render)
- Status: in_progress
- Key inputs: HTML, style default (como el resto de la materia).
- 2026-10-17 — Presenter: "El grafico de ARquirectura de un Vanilla Gan cambialo a un SVG." → slide 2.6 image redrawn as flat SVG (images/vanilla-gan-arquitectura.svg + .png 2000px; same elements/labels as slide-15-1.jpg; Generator as red focal; validate_svg ok; aspect ok) and referenced as .svg in draft/final.

## 2026-10-17 — Step 7 (Render) — cierre
- Status: complete
- What was decided: folder renamed by presenter (clase-08-gans → redes-generativas-antagonicas); stale render agent (old path) stopped. Reused the complete slide model it had filled (45 content + 5 section-agenda; Vanilla GAN slide already on the SVG); stamped; audits: text/image/notes/block/degenerate ok; field_coverage flags 8 untitled slides (pptx has no title on them — the on-screen heading is the slide's own bold body text; kept as-is per presenter, nothing invented). Rendered 50 slides + cover; fresh. README class 12 links the deck; index.html regenerated via tools/build-index.py (Talksmith wrote its own list to talksmith-index.html).
- Files created/modified: output/slide-model.json, output/html/index.html, README.md, index.html, talksmith-index.html
- 2026-10-17 — Presenter: "Slide 7 no renderizo bien" + "Lo mismo que 'Lo que la IA Generativa hace posible…'" → diagnosis: FILL used pptx icons/frames as figures (~20 slides). Added 37 deck-omit waivers (icons + card frames) to draft/final; 5 formula images kept. Re-fill + render dispatched. Logged BUG-20261017-02.
- 2026-10-17 — Presenter: "eg: slide-12-2. Remove this and all other files similar to the size of it." → deleted the 32 pptx icon files (40–125 px) from images/ and their refs + deck-omit waivers from draft.md/final.md. research/articles/AIG4B-Clase-8-GANs-media (raw pptx extraction) left intact. 5 card-frame waivers remain.

## 2026-10-17 — Step 7 — re-fill íconos/fórmulas
- Status: complete
- What was decided: re-filled the slides that used pptx icons / card frames as figures (plugin 1.1.0 scripts). No slide references a deleted or waived image; no Material `icon` names on any item, and no icon-drawing card template (concept-breakdown / content+cards+image) remains, per presenter ("demasiados íconos"). Text verbatim; audits ok (field_coverage only flags the 9 untitled slides).
- Template changes (pptx slide → new): 5 ¿Por qué importa → concept-columns + highlight; 6 Línea de tiempo → timeline, icon media removed; 7 Modelos del curso → concept-columns (Pregunta as closing line); 12 El origen → content-image + 70K+/LeCun highlights; 13, 29, 40, 47 → same value-columns, icon media removed; 16 Entrenamiento paso a paso → process (5 labelled steps); 18 Slanted Land → content-image facts; 19 El mundo → content-image facts (banded strip); 20, 24 (sin título) → content-image labelled facts; 32 Backprop → content-image facts + diagram; 41 StyleGAN arquitectura, 42 Innovaciones, 46 Fortaleza 4, 50 Limitaciones 2 → concept-columns; 43 Fortaleza 1, 45 Fortaleza 3 → content-image facts; 49 Limitaciones 1 → concept-columns (critic).
- Formula slides split in two (renderer places one media per slide, formulas must not be card thumbnails): 25 Sigmoid (formula banded | properties + graph), 30 Log-loss (Label=1 + Error_D | Label=0 + Error_G), 36 Error del D (image-full formula | prose + diagram), 37 Derivada (image-full formula | explanation + diagram). Deck 50 → 54 slides.
- Pending: slide-36-1.png / slide-37-1.png have very wide white margins (52:1, 36:1) and read small even full-width — cropping the PNG margins would fix it (presenter's call). Renderer issues logged in the report: banded + concept-columns collapses the image; 2-column value-columns styles the first column as a factor column.
- Files created/modified: output/slide-model.json, output/html/index.html, talksmith-index.html
- 2026-10-17 — presenter chose to continue in this session (another session had added images/arquitectura-gan.svg for 2.5 at 15:57): model slide 12 media → arquitectura-gan.svg; 9 empty images deleted (slide-39-1..4, slide-07-1..3, slide-49-2/3) + refs/waivers removed; Tipos de GANs → concept-columns (no images/icons); slide-31-1/2 cropped to the graphs (stray fragments erased; originals in research/); re-rendered with 1.1.0, all audits ok, fresh (54 slides + cover).
- 2026-10-17 — Presenter: "'Loss Function Visualmente' has toon of space on the right… 3 columns instead of 2." → figures has a fixed 3-col grid (BUG-20261017-04). Composed slide-31-1/2 side by side into images/slide-31-graficos.png (draft/final refs updated, sources note), model slide 31 → content-image split-left with the two labeled facts verbatim; tried value-columns banded first (plots illegible) and discarded. Rendered; fresh.
- 2026-10-17 — Presenter: "Check with the editor how can this be improved" (3.10 + 3.13) → editor review, presenter chose option A for both. Applied in draft.md + final.md (not rendered; output/ untouched, model now stale): 3.10 → «El Generador: el objetivo opuesto», value-columns Factor · D · G (entrada/salida/quiere) + transposed-conv takeaway, slide-27-1.png removed (Discriminator figure, corpus #4), notes written; 3.13 → «Log-loss: los dos casos del Discriminador», value-columns with formulas as text in D(x)/D(G(z)) notation, "Generador entrenando" mislabel fixed, slide-30-1/2.png removed (Error_G label contradicted 3.19), notes written; 3.12 duplicate takeaway removed (kept in 3.13); 3.7 pixel inputs z₁…z₄ → x₁…x₄ (z reserved for noise; matches xᵢ in 3.17). Original text in Cut material (both files). Numbers unchanged (−ln 0.9 = 0.105, −ln 0.1 = 2.303). 3 presenter bullets mirrored to backlog.

## 2026-10-17 — Step 7 — re-fill incremental (3.10 / 3.13 / 3.12 / 3.7 / 2.5)
- Status: complete
- What was decided: incremental re-fill of output/slide-model.json (other entries byte-identical): 2.5 Arquitectura de una GAN keeps value-columns + images/arquitectura-gan.svg, text-box labels note removed (now inside the SVG); 3.7 Entradas (x), x₁…x₄; 3.10 → value-columns Factor · D · G + "En redes reales" note, slide-27-1.png gone, notes added; 3.12 duplicate takeaway removed; 3.13 two content-image halves (slide-30-1/2.png) merged into one value-columns slide (formulas as text, takeaway, notes). 2.6 Vanilla GAN unchanged (redrawn SVG re-inlined). Deck 54 → 53 slides. Classification critique done inline for the 4 re-filled slides (all confirm; 3.10/3.13 pinned by template directive). Audits: text/notes/block/image/degenerate/diversity ok; field_coverage only the 7 known untitled slides. Stamped; rendered (style default, light); fresh.
- Files created/modified: output/slide-model.json, output/html/index.html, talksmith-index.html

## 2026-10-17 — Step 5 (Review) — reencuadre para ingenieros
- Status: complete
- What was decided: Presenter: "Revisá y reformulá en el draft que la audiencia no es biomédica sino ingenieros. Revisá si los ejemplos son relevantes todavía." Parte 1 aplicada en draft.md (solo el encuadre; hechos, cifras y ejemplos clínicos intactos): 1.1 columna «¿Por qué importa en ingeniería?»; 1.2 lead generalizado (clasificar, detectar objetos, medir estructuras); 1.3 título «¿Por qué importa en ingeniería?», barreras escritas para cualquier modelo de visión, notas nuevas (pipeline de datos, lectura del Dice); 1.5 GANs → datos sintéticos, pregunta de SAM generalizada; 2.2 ítem «Dónde se aplican»; sección 4 y agenda «Tipos de GANs y aplicaciones»; 4.1 usos de cGAN/SRGAN generalizados (4× de Ledig et al.); 4.6 lead con Pix2Pix (pares) vs CycleGAN (sin pares), MRI→CT como ejemplo médico; 4.8 encabezado «El cuello de botella: los datos de entrenamiento»; 4.9 sin «En Biomedicina», consejo impersonal; 5.3 celda 05 sin «en Biomedicina». Numeric fidelity: ninguna cifra cambiada (Dice 0.9524/0.9459, +30%, 4× verificado en srgan-ledig-2017). Parte 2 (qué ejemplos reemplazar) entregada como propuesta al orquestador, sin escribir.
- Key inputs: corpus (aws-que-es-una-gan, sam-kirillov-2023, srgan-ledig-2017, cyclegan-zhu-2017, pix2pix-isola-2017), profile (audiencia de Ingeniería de Software).
- Files created/modified: draft.md (11 bullets [closed] presenter-origin + 3 Open questions nuevas), config/feedback-backlog.md (11 filas). final.md y output/ sin tocar.
- Pending open questions: decisión de reemplazo de ejemplos clínicos (1.2, 1.3, 1.6, 4.1, 4.5, 4.6, 4.7, 4.8, 5.1); bonus de privacidad de 4.8 discutible (memorización); 1.5 describe el plan del curso original (¿esta materia cubre SAM?). [ejemplos y bonus de privacidad cerrados en la entrada siguiente]

## 2026-10-17 — Step 5 (Review) — reemplazo de ejemplos
- Status: complete
- What was decided: el presentador aplicó los reemplazos ★ del editor, solo con fuentes del corpus. 1.2 tabla → MNIST («¿Este dígito es un 7?» / «Genera un 7», cGAN); 1.3 U-Net/Dice → Salimans 2016 (semi-supervisado SOTA en MNIST, CIFAR-10, SVHN), notas actualizadas; 1.6 fila → «Caso de uso típico» (SRGAN, Pix2Pix/CycleGAN; Stable Diffusion/DALL·E/Midjourney; SAM + etiquetado asistido); 3.1 crédito Rowel Atienza → Luis Serrano; 4.1 «carcinoma ductal» → «Genera un 7»; 4.5 tarjeta neurorradiólogos → test de Turing visual de Salimans (21,3 % en CIFAR-10), notas nuevas; 4.6 día→noche → Pix2Pix; 4.7 queda solo la TC de baja dosis; 4.8 biopsias +30 % → Salimans, bonus de privacidad quitado (decisión del editor: sin fuente y falso tal como estaba escrito, por memorización), notas nuevas; 5.1 mode collapse → MNIST con un solo dígito (conocimiento general). Todo lo quitado está en Cut material. Numeric fidelity: 21,3 % copiado del registro de Salimans; ninguna cifra derivada. Deepfakes: idea en Open questions (necesita captura).
- Key inputs: inception-score-salimans-2016, cgan-mirza-osindero-2014, serrano-gans-lab, sam-kirillov-2023, srgan/pix2pix/cyclegan.
- Files created/modified: draft.md (10 bullets [closed] presenter-origin, Cut material, Open questions), config/feedback-backlog.md (10 filas). final.md y output/ sin tocar por este paso (final.md tiene mtime 16:35:45 de otra sesión).
- Pending open questions: tarjeta de deepfakes (sin fuente en corpus); 1.5 describe el plan del curso original (¿esta materia cubre SAM?).
- 2026-10-17 — Presenter: "Pongamos todo junto del Discriminador has also the prolem of being 2 colums" → model slide 25 figures → content-image split-left with a 1.2.0 media set {images:[slide-26-1.jpg, slide-26-2.jpg]} + two labeled facts verbatim. Rendered with 1.2.0 scripts; all audits ok; fresh (53 slides).

## 2026-10-17 — Step 6 (Polish) — re-derivación tras reencuadre y reemplazo de ejemplos
- Status: complete
- What was decided: cp draft.md → final.md (derivado primero en scratch; final.md anterior respaldado en scratchpad/gan/final.before-rederive.md). polish-ascii scan: 0 bloques; polish-images scan: 0 directivas. 24 refs research/corpus/…/images → images/ (todas ya presentes y byte-idénticas; 0 copias, 0 faltantes); 2 refs .svg (arquitectura-gan, vanilla-gan-arquitectura) se mantienen por pedido del presentador, con .png companion en disco. rescue-open: 2; strip_feedback: 60 bloques. Diff slide a slide contra el final.md previo (mtime 16:35:45): todas las diferencias de contenido vienen de los dos pasos Step 5 de hoy; además, líneas en blanco sobrantes (residuo del borrado de íconos/imágenes vacías, solo en final) y 3 rutas en Cut material con la convención de draft (research/corpus/…) o images/. Ninguna edición exclusiva de final.md; nada portado a draft.md.
- Key inputs: draft.md (16:40:48), final.md previo.
- Files created/modified: final.md. draft.md y output/ sin tocar.
- Pending open questions: tarjeta de deepfakes (sin fuente); 1.5 ¿esta materia cubre SAM?; output/slide-model.json desactualizado (re-fill Step 7).
