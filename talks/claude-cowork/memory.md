# memory.md — claude-cowork

**Current step:** complete — Talk cerrado el 2026-08-01; regenerado con plugin 0.75.0 el 2026-08-01
**Awaiting:** nada. El Talk sigue **completo** al 2026-08-01: 24 laminas de contenido, `final.md` y el deck `html-strict` (31 laminas) al dia contra el `draft.md` actual, ahora con el plugin en **0.75.0**. El paso 8 (Learnings) **no se corrio** — se cerro directo por pedido del presentador. Lo que quedo sin decidir vive en las Pending open questions de la ultima entrada del log; nada de eso bloquea dictar la clase.

**Topic:** Claude Cowork — capacidades funcionales y de uso para el trabajo diario (enfoque de alto nivel).
**Folder:** talks/claude-cowork/
**Started:** 2026-06-05

---

## Talk briefing

Charla nueva sobre Claude Cowork. En espíritu, similar a la charla existente de Claude (`claude-code-y-cowork`), pero más alto nivel: foco en la parte funcional / de uso de Cowork, dejando de lado Claude Code y los detalles de persistencia y archivos.

---

## Estado actual — 2026-07-31

### El Talk

- **Parte 2** del split del 2026-07-31, que partió en dos la clase combinada de 120 min. La parte 1 (chat, conectores, Schedule, misión parte 1) vive en `talks/claude-desktop-chat`. Esta carpeta conservó nombre e historia.
- Frontmatter: `class: "Claude Cowork"` · `duration: 60 min (a confirmar)` · `date: Julio 2026` · presenters Paulo Veiga y Marco Sánchez Sorondo.
- **6 secciones + Conclusions, 23 slides:** 1 Claude Cowork (4) · 2 Knowledge & Output (3) · 3 Projects (5) · 4 Skills (5) · 5 Subagentes (3) · Conclusions (2: wrap-up · cuidados) · 6 La misión · parte 2 (1).
- **Orden nuevo (2026-07-31):** Conclusions va **antes** de la Sección 6. El deck cierra en la placa de la misión, no en la lámina de gobernanza. La Sección 6 conserva su número aunque vaya última.
- **Tiempo objetivo total: 61,0 min** sobre 23 slides, contra `duration: 60 min (a confirmar)`. **1 min pasado.** Fue a 58,0 al borrar Conclusions.1 y volvió a 61,0 con la lámina nueva 5.2 (+3). Recortes de reserva anotados y **no aplicados**: 5.3 «Un subagente, por dentro» (~1 min, la más salteable del deck) y 3.5 «Un ejemplo de Instrucciones» de 3 a 2. Y la lámina de catálogo de skills sigue sin entrar.
- **Modo de Draft: C** (Presenter Outline).

### Artefactos

- `draft.md` — **canónico y al día**. Bloques de fence: **8 render-driving** (todos `ascii`), **2 documentation-only** (`s3-5-1` el ejemplo de Instrucciones y `s4-3-1` el menú Agregar, que la lámina cubre con captura) y **1 fence `markdown` en 5.3** con hint `documentation-only` (el ejemplo de subagente; el scan no lo detecta de todos modos). Más 5 archivados en `Cut material`. **14 image refs** que resuelven. 31 campos `Presenter feedback`, **todos vacíos**.
- `final.md`, `output/slide-model.json`, `output/html/index.html` — **al día**, derivados del `draft.md` actual el 2026-07-31 (Polish 5ª corrida + Render html-strict 5ª vuelta). `final.md` referencia solo `.png`.
- `images/` — **36 archivos** tras el `gc` del 2026-07-31, que borró 30 (10 tripletes huérfanos de numeraciones viejas). Quedan **8 tripletes vivos** (`.ascii`/`.svg`/`.png`) + 6 screenshots referenciados + 4 imágenes del presentador sin referencia (`connector_browser`, `connectors_directory`, `mockup-tablero`, `schedule`) + `create-skill.png` y `screenshot-cowork-tab.png`, sin referencia. Los borrados quedaron en `_to_delete/images-viejas/` del repo, para revisar y borrar a mano.
- La directiva `<!-- generate-image -->` de la slide 1.1 **sigue sin generar** (el pase del image-illustrator nunca corrió sobre este deck).
- `draft.feedback-archive-2026-07-30.md` y `memory.archive-2026-07-31.md` — históricos, no se leen en el flujo.

### Decisiones permanentes

- **El tiempo dejó de ser restricción (2026-08-01, instrucción explícita del presentador).** Los 61,0 min contra el bloque de 60 se dan por buenos; los recortes de reserva (5.3, y 3.5 de 3 a 2) quedan anulados y no se aplican. Sumar láminas ya no está bloqueado por presupuesto de tiempo.
- Los campos `Presenter feedback` se dejan **vacíos**; el registro de feedback va solo a `config/feedback-backlog.md`.
- ~~El deck cierra en la lámina de gobernanza (Conclusions.3)~~ — **revertido el 2026-07-31 por instrucción explícita del presentador**: las conclusiones cierran la charla y la placa de la misión va última, porque después de la misión termina la clase. Orden interno de Conclusions sin cambios: loop de Faro → wrap-up → cuidados.
- **Faro solo en la misión.** Desde el 2026-07-31 las láminas de enseñanza (secciones 1-5) usan un hilo genérico, **el informe mensual del equipo** (Project "Informe mensual del equipo" · carpeta `Documentos/Informe-Mensual` · Skill `informe-mensual` sobre `notas/`). Faro sobrevive solo en Conclusions.1 (el loop) y en la Sección 6 (la placa), donde es la misión y no un ejemplo.
- **`/skill-creator` no existe en Cowork** (verificado por el presentador, 2026-07-31). Fuera de todo el deck. Se conserva el tip de tipear `/` y el set reducido de slash commands.
- **Sin lámina de repaso de la parte 1** al abrir la Sección 1 — decisión explícita del presentador, nunca ensayada.
- **Subagentes:** el deck no afirma que se creen o configuren a mano en Cowork (los coordina Claude por debajo, sin panel). Verificado contra el corpus y contra dominios oficiales de Anthropic, sin fuente que diga lo contrario.
- **Audit trail:** la actividad de Cowork no entra en la Compliance API; el registro por OpenTelemetry es de Team/Enterprise y no exporta nada por defecto.
- Este repo **no tiene** `config/principles.md` ni `config/diagram-style.md`: se usan las copias del plugin.

### Pendientes abiertos

- **Lámina de catálogo de skills (Sección 4), sin crear.** Reemplaza a la borrada 4.4. Falta que el presentador elija el catálogo y los 5 skills. Candidatos relevados el 2026-07-31: el **directorio dentro de la app** (Personalizar → Habilidades → "+" → Explorar, instalación de un clic, support 14328846) · **skills.sh** (+91.000, se instala con `npx skills add`) · **github.com/anthropics/skills** (~20, oficial) · **vercel.com/docs/agent-resources/skills** (el link que pasó el presentador, perfil developer).
- **Duración: 61,0 min contra 60 — 1 min pasado.** Recortes de reserva anotados y no aplicados: 5.3 (~1 min, la lámina más salteable) y 3.5 de 3 a 2. La lámina de catálogo sumaría 2-3 más.
- ~~**Nombres de skills desalineados**~~ — **cerrado el 2026-07-31**: el diagrama que mostraba `buscar-accion` y `reporte-semanal` vivía en Conclusions.1, que se borró. El deck entero enseña ahora un solo hilo, `informe-mensual`, y los nombres reales de la misión solo aparecen en la Sección 6.
- **Activación automática de Skills, sin fuente oficial.** La lámina nueva 4.2 afirma que Claude carga una Skill sola cuando el pedido coincide con su `description` (semántico, no por palabra clave). Hoy eso lo sostiene **solo el deck interno** (`corpus/agentic-ai-deck.zip.md`), no documentación de producto. Está marcado como pendiente de verificación en las Sources y en las Speaker notes de la lámina; **re-verificar contra la doc oficial antes de la clase**.
- **Layout ASCII-izquierda / bullets-derecha** (slide 1.2): pedido del presentador **no aplicado**, no existe el template. La intención quedó como hint en la slide (`<!-- layout: image-left -->` debajo del heading, hoy ignorado por el render). Espera un cambio en el plugin.
- **Modos de Cowork** (slide 1.4): la lámina no afirma cuál es el default. La captura vieja decía `Ask`, la nueva dice `Auto`. Confirmar contra la app antes de la clase.
- **`screenshot-cowork-tab.png` y `create-skill.png` sin referencia.** El `gc` **no los toca** por diseño (no están estampados ni tienen sidecar, así que cuentan como imágenes del presentador). Si no se usan, borrarlos a mano.
- **Nivel de la 5.2 / 5.3.** Son las dos láminas más técnicas del deck para una audiencia de management (encabezado YAML, `plugin.json`, `agents/`). Quedaron marcadas como opcionales en el Goal de la Sección 5 y en las notes. Decidir si se dan, se saltean o se recortan.
- **4 majors y 7 minors** del audit del Composer (scope=full, 2026-07-31) sin aplicar, a releer contra el deck partido.
- **Resaltado por template.** El pedido de 1.3 se resolvió con un rótulo en negrita (`**Idea clave:**`) al frente de la línea de lead. No es límite del template: la lámina no tiene slot de callout porque su Content es lead + diagrama, y el blockquote la bajaría a nota al pie. Si el presentador quiere más peso visual, el cambio es de template, no de texto.
- La **placa ASCII de 6.1** es gemela de la de `talks/claude-desktop-chat` (slide 5.1); desde el split la verificación de gemeleo es cross-talk y manual.
- ~~Anglicismo **"Connector MT Newswires" / "Connector Gmail"**~~ — **cerrado el 2026-07-31**: vivía en el ASCII del loop de Conclusions.1, borrado. Sobrevive solo dentro de `Cut material`.
- **Bonus M6** de la misión (subagente a pedido) sin verificar de primera mano; una demo en vivo sí lo necesitaría.
- **Watch item:** el registro por OpenTelemetry pide Desktop 1.1.4173+ y la doc dice "not captured … at this time" — re-verificar antes de la clase.
- Stubs de Phase 2 del librarian y la carpeta `skills/` de la misión, sin resolver.

### Historial

El registro paso a paso completo (Steps 1-8, todas las rondas de Review, Polish, Render y Learnings desde 2026-06-05) está en `memory.archive-2026-07-31.md`.

---

## 2026-07-31 — Step 4 (Draft, reabierto)

- Status: awaiting_presenter
- Asks log:
  - 2026-07-31 — "Volvemos a Draft. ¿Por dónde arrancamos: (1) recorte de tiempo ~6 min, (2) los 4 majors + 7 minors del audit del Composer releídos contra el deck partido, (3) material o slides nuevas, (4) repaso completo con audit fresco?" → pending
  - 2026-07-31 — "Hacé clean de la memoria, que solo quede el estado." → aplicado: `memory.md` reducido a header + briefing + estado actual; historial completo movido a `memory.archive-2026-07-31.md`.
- What was decided: <filled at closure>
- Key inputs: <filled at closure>
- Files created/modified: `memory.md` (reescrito), `memory.archive-2026-07-31.md` (nuevo)
- Pending open questions: ver *Estado actual → Pendientes abiertos*.

---

## 2026-07-31 — Step 4 (Draft, ronda de feedback: Sección 1)

- Status: complete
- What was decided:
  - Slide 1.2 "La nueva habilidad base" **borrada**; la analogía del Excel entró como bullet de 1.1 con la atribución intacta (analistas/industria, NO Anthropic) y su fuente `nextword.substack.com` movida a las Sources de 1.1. Las notes de 1.2 se fundieron en las de 1.1 (2 → 3 min). El ASCII de la lámina quedó archivado entero en `Cut material`: no pasó a 1.1 porque esa slide ya lleva una directiva `generate-image`.
  - Salió **"Eso cambia la forma de trabajar."** del primer bullet de 1.1. Sigue, a propósito, en el Claim de la Thesis y en el Goal de la Sección 1, que no se proyectan.
  - Primer bullet de "De chatear a delegar" reescrito: *"Lo que cambia ahora es el rol: **delegar**. ¿Qué delegamos?"*. La referencia a la clase anterior vive ahora solo en las Speaker notes.
  - **No aplicado:** ASCII a la izquierda y bullets a la derecha. No existe el template; queda en `Open questions` esperando un cambio del plugin.
  - Sección 1 renumerada a 4 slides (3→2, 4→3, 5→4) y barridas las 11 referencias cruzadas a la numeración vieja.
- Key inputs: los dos campos `### Presenter feedback` con contenido (slides 1.2 y 1.3 de la numeración vieja); `slide-templates.md` y `principles.md` del plugin.
- Files created/modified: `draft.md`, `config/feedback-backlog.md` (4 filas), `memory.md`.
- Pending open questions: template de layout imagen-izquierda (bloqueado del lado del plugin); duración 64,0 min contra 60; feedback sin procesar en 1.3, 1.4 y 2.1.

---

## 2026-07-31 — Step 4 (Draft, ronda de feedback: segunda tanda)

- Status: complete
- What was decided:
  - **1.3 El mapa** quedó en el diagrama solo, con una línea de lead arriba. Los tres bullets se fundieron en esa línea y en las Speaker notes; el ASCII y su `ascii-note` siguen intactos byte a byte. ~3 min, sin cambio.
  - **1.4 dejó de ser demo en vivo.** Retitulada **"Dónde se empieza en Cowork"**, con `images/cowork.png` (captura propia de la interfaz actual) en lugar de `screenshot-cowork-tab.png`, que quedó desactualizada y sin referencia. Content reescrito con el patrón de las otras láminas de screenshot (3.2, 4.2, 4.3). El banner ASCII DEMO TIME se archivó en `Cut material`. La Misión 0 sobrevive en notes como demo opcional. De ~6 a ~2 min. La lámina **no afirma cuál es el modo por defecto**.
  - **Sección 2 abre con una lámina nueva**, `2.1 "Qué lee el agente en la carpeta"`: la bisagra entre delegar y la mecánica del `.md`. Resto renumerado (1→2, 2→3, 3→4). Fuente nueva: el post de MindStudio sobre el "LLM wiki" de Karpathy, con la atribución desagregada (post de MindStudio, propuesta de Karpathy). ~2 min.
- Key inputs: los tres campos `### Presenter feedback` que quedaron fuera de alcance en la primera tanda; `images/cowork.png` y su descripción verificada por el orquestador; el post de MindStudio verificado por el orquestador; el patrón de las láminas de screenshot 3.2 / 4.2 / 4.3 del propio deck.
- Files created/modified: `draft.md`, `config/feedback-backlog.md` (4 filas), `memory.md`.
- Pending open questions: nombres y default de los modos de Cowork, a confirmar contra la app; `screenshot-cowork-tab.png` sin referencia; duración 62,0 min contra 60.

---

## 2026-07-31 — Step 4 (Draft, hint de layout)

- Status: complete
- What was decided: la intención de layout de la slide 1.2 quedó registrada como metadata en `draft.md`, debajo del heading `## 2. De chatear a delegar`: `<!-- layout: image-left -->` más una línea de comentario con el pedido y el bloqueo. La forma y la ubicación siguen los hints de autor del schema (`template:` / `reveal:` / `aside:`, bajo el `##` de la slide); la clave `layout:` la elegí por analogía con el vocabulario del catálogo (`content+image` → `layout: text-left | image-top`) y **no está reconocida todavía**, así que hoy el render la ignora.
- Key inputs: `schemas/draft.md` (fila de slide hints), `config/pptx-styles/slide-templates.md` (`content+image`), `polish_ascii.py scan` corrido sobre el archivo antes y después.
- Files created/modified: `draft.md` (3 líneas), `config/feedback-backlog.md` (fila existente ampliada, sin fila nueva), `memory.md`.
- Pending open questions: el cambio en el plugin. Dos archivos temporales (`.scan-before.md`, `.scan-after.md`) quedaron en la raíz del repo con una línea que dice que se pueden borrar; `device_bash` no tiene permiso de borrado.

---

## 2026-07-31 — Step 4 (Draft, tercera tanda de feedback)

- Status: complete
- What was decided:
  - **2.1** — el bullet del "LLM wiki" bajó a nota al pie en blockquote con la URL de MindStudio visible; el Content queda en 3 bullets. Se sumó que la carpeta es de **lectura y escritura**, fundido en el primer bullet.
  - **Ejemplos genéricos en vez de Faro** en las secciones 1-5. Hilo único: el informe mensual del equipo. Tocó 1.2 (notes), 2.2 (el bloque `markdown`), 2.3 (el ASCII, que renderiza el mismo archivo), 2.4, 3.1, 3.2, 3.3 (las Instrucciones completas, con regla de oro nueva: toda cifra lleva fuente y fecha) y 4.1. Las Sources que citaban `corpus/mision - auto.zip.md` se conservan, reformuladas.
  - **`/skill-creator` fuera** del Narrative arc, el Goal de la Sección 4, el ASCII de 4.2 (rediseñado a tres caminos convergiendo en la compuerta), sus Sources y notes, y 4.3.
  - **4.3 adelgazada** a menú "+" + trampa del Save, de ~3 a ~2 min. Se conserva Code execution y el tip de tipear `/`.
  - **4.4 "Un SKILL.md por dentro" borrada** y archivada íntegra en `Cut material`. La Sección 4 queda en 3 láminas, esperando la de catálogo.
  - **Conclusions movido antes de la Sección 6.** Orden final: 1-5 → Conclusions → 6. Agenda, Goal de la Sección 6 y las tres transiciones de notes (6.1, Conclusions.2, Conclusions.3) reescritas.
- Key inputs: los 6 campos `Presenter feedback` con contenido; verificación web del 2026-07-31 sobre catálogos de skills (support 14328846, skills.sh, anthropics/skills, docs de Vercel).
- Files created/modified: `draft.md`, `config/feedback-backlog.md` (6 filas), `memory.md`.
- Pending open questions: la lámina de catálogo de skills; nombres de skills desalineados entre Sección 4 y Conclusions.1; layout ASCII-izquierda.

---

## 2026-07-31 — Step 4 (lámina nueva) + Step 6 (Polish, 2ª corrida)

- Status: complete
- What was decided:
  - Lámina nueva **4.4 «Grabar una Skill»**, última de la Sección 4, a pedido del presentador ("Let's add in the skill section at the end the 'Record a Skill' slide"). Cubre propósito, uso y límites: es el **tercer camino de creación** y el de menor barrera — se hace la tarea narrándola y Claude propone la Skill.
  - Hechos, todos de la doc oficial (support 12512198, verificado 2026-07-31): planes **Pro, Max y Team**, **Cowork en Claude para Mac**; se entra por el menú **"+"** del chat (el mismo de 4.3) o por Configuración → Habilidades → Agregar; captura **pantalla, clicks, tipeo y voz** hasta **~10 min**; el producto avisa de **no tipear contraseñas ni datos sensibles**; Claude abre una tarea de Cowork, revisa la grabación y **propone** la Skill, nueva o como actualización de una existente; la Skill resultante se edita como cualquier otra. El anuncio en X de la cuenta oficial de Claude (21/07/2026) se cita como cobertura, separado de la doc.
  - **La lámina NO afirma nada sobre retención de las grabaciones ni sobre entrenamiento** — la doc no lo cubre. Queda como pregunta abierta en las Speaker notes.
  - Diagrama nuevo `s4-4-1-flujo-grabar-skill`: flujo vertical de 4 pasos bajando a "SKILL ACTIVA", con el paso 4 destacado como **la trampa del Save**, pariente visual de la compuerta del diagrama de 4.2.
  - Polish re-corrido entero: 10 bloques, **1 renderizado** (el nuevo) y **7 reusados por digest**; `s3-3-1` y `s4-2-1` siguen documentation-only. 13 refs, todas `.png`. Strip: 20 campos H3 + 8 de párrafo.
- Key inputs: support.claude.com/en/articles/12512198 (verificado 2026-07-31); anuncio oficial en X del 21/07/2026; el diagrama de 4.2 como referencia visual.
- Files created/modified: `draft.md`, `final.md`, `images/s4-4-1-flujo-grabar-skill.{ascii,svg,png}`, `config/feedback-backlog.md` (1 fila), `memory.md`.
- Pending open questions:
  - **Duración: 61,0 min contra un bloque de 60**, y la lámina de catálogo todavía no entró.
  - **Disponibilidad de "Record a skill" a confirmar contra la app antes de la clase**: despliegue gradual, solo Mac, planes Pro/Max/Team.
  - La crítica visual ciega automática tampoco se pudo lanzar esta corrida; la revisión del diagrama nuevo la hizo el orquestador a mano sobre el PNG y quedó aprobada.
  - Huérfano nuevo en `images/`: `s4-4-1-anatomia-skill-md.*` sigue compartiendo prefijo con el bloque vivo `s4-4-1-flujo-grabar-skill.*`. El `gc` los distingue por digest, pero conviene correrlo.

---

## 2026-07-31 — Step 7 (Render, html-strict)

- Status: complete
- What was decided:
  - Estilo elegido: **`html-strict`** (Reveal.js, sin `.pptx`). Salida: `output/html/index.html`, 2,0 MB autocontenido (Reveal + fuentes + las 13 imágenes inlineadas). Modelo intermedio en `output/slide-model.json`, estampado con el digest de `final.md`.
  - **28 láminas** en el deck: portada + 7 divisorias de sección + las 20 de contenido. `Open questions` y `Cut material` quedaron fuera, como corresponde. Orden 1-5 → Conclusions → 6, respetado.
  - Las 20 láminas llevan sus Speaker notes verbatim en el panel de notas (tecla `s`).
  - **El hint `<!-- layout: image-left -->` SÍ está soportado hoy** por el render html — la nota vieja de `Open questions` que decía que el catálogo no lo soportaba quedó desactualizada. Se aplicó en 1.2 (el pedido original del presentador, por fin cumplido) y también en 2.3.
- Key inputs: `final.md` polished; `config/profile.md` y `config/logo.png` (portada).
- Files created/modified: `output/html/index.html`, `output/slide-model.json`, `memory.md`.
- Pending open questions:
  - **4.2 perdió la captura `skills-panel.png`.** El template de superficie de código no tiene ranura de imagen y la lámina traía captura + fence. Se priorizó el fence. Arreglos posibles: partir 4.2 en dos láminas, o dejar que el ASCII se renderice a imagen y que la captura entre como lámina visual.
  - **3.2 apretada:** las dos capturas (`project.png`, `context.png`) caen en una grilla de 3 columnas y quedan a ~1/3 del ancho, ilegibles en proyección. Candidata a partirse en dos láminas.
  - **1.3** (el mapa) y **1.4** (`cowork.png`): las imágenes quedan chicas para su nivel de detalle; chequear en sala.
  - **4.3** quedó visualmente vacía a la izquierda.
  - El roadmap de las divisorias numera por posición, así que Conclusions sale `06` y la Sección 6 sale `07`. Es cromo del renderer, no del contenido.
  - En la superficie de código la sangría se preservó codificando espacios duros, porque la caja no fija `white-space: pre`. Si el plugin lo agrega, se puede revertir (afecta 2.2, 3.3, 4.2).

---

## 2026-07-31 — Step 4 (lámina 3.3) + Polish + Render, 3ª vuelta

- Status: complete
- What was decided:
  - Lámina nueva **3.3 «¿Los lee todos?»** en la Sección 3, entre "Conceder una carpeta" y las Instrucciones, que pasó a **3.4**. La sección queda en 4 láminas. Contenido del presentador: los tres casos (pocos archivos → lectura completa · muchos archivos → búsqueda de fragmentos, 10x capacidad · trabajar sobre los archivos → abrir, modificar y guardar) más tres reglas prácticas (subir lo que importa, nombres claros, PDFs escaneados sin capa de texto).
  - **Choque de fuentes, resuelto a propósito.** El presentador escribió que con búsqueda "ahora depende de que la búsqueda encuentre lo correcto"; la doc oficial (support 11473015, verificado 2026-07-31) afirma lo contrario: *"Response accuracy remains consistent with in-context processing"*. La **lámina quedó neutral** (describe el mecanismo, no la fiabilidad) y las **Speaker notes llevan las dos posiciones con nombre**. El 10x sí está respaldado por esa misma fuente, igual que el carácter automático del cambio; **no hay umbral numérico documentado** y el deck no inventa uno.
  - "Consume mucho de tu límite de uso" se bajó a "ocupar la ventana de contexto entera en cada vuelta", que es lo defendible.
  - Polish y Render re-corridos. Polish: 10 bloques, **0 renderizados** (ninguno nuevo, la lámina no lleva diagrama), 8 reusados por digest, 2 documentation-only (`s3-4-1` Instrucciones, `s4-2-1`). 13 refs, todas `.png`. Render html-strict: **29 láminas** (portada + 7 divisorias + 21 de contenido), 2,03 MB.
- Key inputs: el comentario del presentador en el `Presenter feedback` de 3.2; support.claude.com/en/articles/11473015 (RAG for projects, verificado 2026-07-31).
- Files created/modified: `draft.md`, `final.md`, `config/feedback-backlog.md` (1 fila), `output/html/index.html`, `output/slide-model.json`, `memory.md`.
- Pending open questions:
  - **Duración: 64,0 min contra un bloque de 60 — 4 min pasado.** El recorte de reserva (Conclusions.1 de 5 a 3) ya no alcanza solo: devuelve a 62,0. Candidatos adicionales anotados: 3.4 Instrucciones de 5 a 4 (la lámina más larga) y 2.4 de 4 a 3. Y la lámina de catálogo de skills todavía no entró.
  - **3.3 quedó la lámina más densa del deck** (auto-ajuste a ~0,64 contra 0,78-0,97 de sus pares). Entra completa y se lee, pero la salida natural si molesta es partirla en dos: los tres modos por un lado, las tres reglas por otro.
  - En el render, los tres emoji de las reglas (📁 🏷️ 📄) se colapsan a un único glifo de nota, porque el ícono de un bloque destacado lo fija su tipo y no se elige por ítem. El encabezado "Tres reglas prácticas" no se imprime: el grupo se lee por la banda acentuada.
  - Sigue abierto lo de 4.2 (pierde la captura) y 3.2 (dos capturas apretadas en grilla de 3 columnas).

---

## 2026-07-31 — Step 4/5 (5ª ronda) + Polish + Render, 4ª vuelta

- Status: complete
- What was decided:
  - **3.1 «Qué es un Project»** ganó una nota al pie: Cowork trabaja la carpeta concedida **con herramientas de archivo** — abre, busca y escribe lo que la tarea necesita, en vez de traer el contenido entero a la conversación. Fuente: Claude docs, *Desktop and filesystem access* (https://claude.com/docs/cowork/3p/local-access, verificado 2026-07-31): *"the agent can then read, create, and modify files anywhere inside those folders"* y *"read, write, and **search** files … with its **file tools**"*. **La doc no dice nada sobre "memoria" ni sobre consumo de contexto**, así que la lámina no lo afirma. Las notes separan explícitamente este caso (carpeta de Cowork, herramientas) del de 3.3 (base de conocimiento, leer todo vs fragmentos).
  - **La lámina de Instrucciones se partió en dos.** `3.4 Instrucciones: el contrato de trabajo` es la de **concepto**, con la captura nueva **`images/instructions.png`** (panel de contexto de un Project, con Instructions rodeado en violeta y debajo Memory, Context y Scheduled). `3.5 Un ejemplo de Instrucciones` se lleva el fence ```text completo, byte por byte, con su hint `ascii-render: documentation-only` **intacto** — sin ese hint el pipeline lo tomaría por diagrama, porque la lámina no lleva imagen. Los 5 min originales se repartieron en ~2 + ~3.
  - **La Sección 3 quedó en 5 láminas:** Qué es un Project · Conceder una carpeta · ¿Los lee todos? · Instrucciones (concepto) · Un ejemplo.
  - Polish: 10 bloques, **0 renderizados** (ninguno nuevo), 8 reusados por digest, 2 documentation-only (`s3-5-1`, `s4-2-1`). 14 refs, todas `.png`. Render html-strict: **30 láminas** (portada + 7 divisorias + 22 de contenido), 2,55 MB.
  - En el render: 3.4 quedó `content-image` (texto izquierda, captura derecha, sin recorte); 3.5 quedó superficie de código, 11 líneas contra un tope de 18, con la sangría preservada; la nota de 3.1 renderizó como banda destacada bajo las tarjetas, no como una tarjeta más.
- Key inputs: los 3 bullets del presentador; claude.com/docs/cowork/3p/local-access; `images/instructions.png` (aportada por el presentador, verificada por el orquestador).
- Files created/modified: `draft.md`, `final.md`, `images/instructions.png`, `config/feedback-backlog.md` (3 filas), `output/html/index.html`, `output/slide-model.json`, `memory.md`.
- Pending open questions:
  - **Duración: 64,0 min contra 60 — 4 min pasado**, sin cambio respecto de la ronda anterior (la partición repartió los minutos, no los sumó). Plan de recorte que cierra en 60: Conclusions.1 de 5 a 3, 3.5 de 3 a 2, y 2.4 de 4 a 3. Y la lámina de catálogo de skills sigue sin entrar.
  - **Idioma mezclado en las capturas:** `instructions.png` muestra la app **en inglés** ("Instructions"), mientras `skills-panel.png` y `skills-menu-chat.png` están en español. O se menciona al pasar, o se resacan (implica rehacer los círculos violeta).
  - **Posible solape** entre `instructions.png` (3.4) y `context.png` (3.2): las dos muestran el panel de contexto. Decidir si una sobra; sacar `context.png` bajaría 3.2 de 2 a 1,5 min.
  - Sigue abierto: 4.2 pierde su captura; 3.2 con dos capturas apretadas; 3.3 es la lámina más densa del deck.

---

## 2026-07-31 — Step 4/5 (6ª ronda de feedback)

- Status: complete
- What was decided:
  - **1.3 El mapa** — la línea de lead pasó a llevar el rótulo **`**Idea clave:**`** al frente. Respuesta a la pregunta del presentador: **no es límite del template**; la lámina no tiene slot de callout porque su Content es lead + diagrama, y el blockquote la degradaría a nota al pie. Más peso visual = cambio de template.
  - **1.4 Dónde se empieza en Cowork — solo la imagen.** El Content quedó con `images/cowork.png` sola; los cuatro bullets (`+ New`, toggle Chat/Cowork, `Project or folder`, selector de modo) bajaron a Speaker notes sin perder nada, incluido el cuidado sobre el modo por defecto. ~2 min, sin cambio.
  - **Las dos láminas del `.md` se fusionaron en una** (opción elegida por el presentador entre tres). La ex 2.2 (fence `markdown`, el archivo crudo) y la ex 2.3 (fence `ascii`, el render) son ahora **2.2 «Qué es un .md: el texto y lo que se ve»**, con **un** bloque ASCII de dos paneles lado a lado unidos por `==>`: `LO QUE SE ESCRIBE` / `LO QUE SE VE`, con las etiquetas que atan cada marca a su elemento. Ese bloque es el que Polish renderiza a imagen, así que la "imagen" pedida sale del pipeline de ASCII y no de generación de imagen. Sources y notes fusionadas. La Sección 2 bajó a **3 láminas** y el deck recuperó ~2 min. La ex 2.3 quedó archivada íntegra en `Cut material`.
  - **Lámina nueva 4.2 «Cómo se usa una Skill»**, ubicada después de 4.1 y antes de los caminos de creación (decisión del presentador: primero usar, después fabricar). Los dos modos: **explícito** (`/informe-mensual`) y **automático** (Claude compara el pedido contra la `description`). De ahí el consejo: la descripción es el disparador, no decoración. Diagrama ASCII nuevo con los dos caminos convergiendo en `SKILL EN EJECUCIÓN`. **Certeza declarada:** el camino explícito está verificado de primera mano; el mecanismo semántico lo sostiene solo el deck interno → marcado pendiente de verificación en Sources y notes. ~2 min. Sección 4 a **5 láminas**.
  - **Conclusions.1 «El loop completo de Faro» borrada** y archivada íntegra en `Cut material`. Conclusions queda en 2 láminas; **−5 min**. Se limpió el arrastre: las notes de «Lo que se llevan» abrían citando el loop y retomaban su pregunta abierta — reescritas para llegar desde Subagentes y replantear la pregunta dentro de la propia lámina. También se reescribió la transición de salida de 5.1.
  - Renumeración completa de las Secciones 2 y 4 y de Conclusions, con barrido de referencias cruzadas en agenda, Narrative arc, Goals de sección, Sources, notes y ascii-notes.
- Key inputs: los 5 campos `Presenter feedback` con contenido; dos decisiones del presentador vía pregunta (fusionar vs. agregar lámina; ubicación de la lámina de uso de Skills). Sin acceso web esta corrida — no se citó ninguna fuente nueva.
- Files created/modified: `draft.md`, `config/feedback-backlog.md` (5 filas), `memory.md`.
- Pending open questions:
  - **Polish y Render no se corrieron.** `final.md` y `output/` quedaron atrás de `draft.md`. El próximo Polish tiene que renderizar **2 bloques nuevos** (el de dos paneles de 2.2 y el de 4.2) y correr `gc` sobre `images/`, donde el diagrama del loop de Faro queda huérfano.
  - **Activación semántica de Skills sin fuente oficial** (ver *Pendientes abiertos*).
  - **Duración resuelta en 58,0 min**; el aire de ~2 min es exactamente el presupuesto de la lámina de catálogo de skills, que sigue sin crearse.

---

## 2026-07-31 — Step 4/5 (7ª ronda: la lámina 2.3)

- Status: complete
- What was decided:
  - **2.3 reenfocada de "trabajar en `.md`" a "iterar en `.md`".** El presentador retituló la lámina en el draft (a "Interar", typo) y pidió alinear el contenido: *"El foco no es sobre trabajar sino como usar el .md para iterar."* Título corregido a **«3. Iterar en .md, exportar al final»**.
  - Content reescrito entero. Abre con lead destacado (**con la IA nada sale bien a la primera; el trabajo son muchas vueltas sobre el mismo archivo**) y sigue con: qué es una vuelta (pedidos chicos sobre el archivo que ya existe, con tres ejemplos), por qué la vuelta sale barata en `.md` (reescribe el archivo entero sin romper nada vs. las capas de formato de `.docx`/`.xlsx`), la regla de bolsillo reformulada de *"se edita"* a **"se itera"**, y la entrega como paso único al final. Salieron los dos bullets viejos de trabajo en general; lo de la memoria del agente sobrevive en las notes.
  - **Diagrama rediseñado:** dejó de ser un flujo lineal de tres cajas; la caja central lleva ahora un **bucle explícito** con los tres pedidos de ejemplo adentro, retitulado `DONDE VIVE LA ITERACION`. `ascii-note` reescrito entero.
  - Speaker notes reescritas en cinco párrafos, abriendo con el permiso explícito de que nada sale bien a la primera (el que espera el resultado perfecto en el primer prompt se frustra y abandona).
  - Sources **sin cambio**: ninguna afirmación nueva. Tiempo objetivo sin cambio (~4 min); el deck sigue en **58,0**.
  - Actualizados el Goal de la Sección 2, el Narrative arc y las dos menciones del título viejo en `Open questions` y `Cut material`.
- Key inputs: el único campo `Presenter feedback` con contenido y el retítulo que el presentador dejó en el propio draft.
- Files created/modified: `draft.md`, `config/feedback-backlog.md` (1 fila), `memory.md`.
- Pending open questions:
  - **El bloque ASCII de 2.3 cambió**, así que ahora el próximo Polish tiene **3 bloques para renderizar** (los dos paneles de 2.2, el de 4.2 y el bucle de 2.3) — este último ya no reusa por digest.
  - Un archivo temporal, `draft.current.md`, se movió a `_to_delete/` del repo (`device_bash` no puede borrar). Se puede borrar a mano.


---

## 2026-07-31 — Rondas 8-10 de feedback

- Status: complete
- What was decided:
  - **Ronda 8 — 3.3 «¿Los lee todos?»:** fuera los tres emoji (📁 🏷️ 📄) del grupo "Tres reglas prácticas". Los bullets quedaron con el mismo patrón que el grupo de arriba de la misma lámina. Cierra de paso la anotación vieja de que el render colapsaba los tres emoji a un único glifo: sin emoji, el problema desaparece.
  - **Ronda 8 — 4.1 «Qué es una Skill», rehecha en tarjetas.** Diagnóstico de la confusión que señaló el presentador: el primer bullet metía tres cosas en una línea (qué es, cuándo se activa, un trabajo por Skill) y el "cuándo se activa" ya no le pertenece desde que existe la 4.2. Ahora abre con la frase ancla como lead y baja a **4 tarjetas**: es un instructivo escrito · se enseña una vez · un trabajo por Skill · queda disponible. Cierra con `informe-mensual` presentado como el hilo de toda la sección.
  - **Ronda 9 — 4.3 «Crear una Skill desde el panel»:** al diagrama del menú Agregar le faltaba la cuarta entrada, **"Grabá tu pantalla"**. Entró como caja propia y se aprovechó para marcar cada entrada con **CREAR** o **IMPORTAR** (tres crean, una importa). Fuente nueva: support.claude.com/12512198, la misma de 4.5. **Cuidado anotado:** `skills-panel.png` es del 21 de julio y puede no mostrar esa entrada todavía — re-mirar el panel y resacar antes de la clase.
  - **Ronda 10 — lámina nueva 5.2 «Armar un subagente propio»** (+ 5.3, ver abajo). El pedido chocaba de frente con una decisión verificada del deck ("los subagentes no se crean ni se configuran a mano en Cowork"), así que **se preguntó antes de escribir**; el presentador respondió con un briefing completo que **resuelve** la tensión en vez de contradecirla: no hay panel (sigue siendo cierto) **y** un subagente es un archivo, así que se puede armar uno propio. La lámina lo dice explícitamente en una cita al pie, para que las dos afirmaciones no se lean como contradicción.
  - **Todo el briefing se re-verificó contra fuente oficial antes de escribir** — no se tomó como fuente en sí mismo. `code.claude.com/docs/en/sub-agents` sostiene "Subagents are Markdown files with YAML frontmatter", que `name` y `description` son los **dos únicos campos obligatorios** (el briefing no lo distinguía) y que cada subagente corre en su propia ventana de contexto; `code.claude.com/docs/en/plugins` sostiene el manifiesto `.claude-plugin/plugin.json` y la carpeta `agents/` **en la raíz** del plugin; `claude.com/docs/cowork/guide/plugins` es la que ata todo a Cowork. Las rutas `.claude/agents/` y `~/.claude/agents/` son de **Claude Code** y quedaron fuera de la lámina, solo en notes.
  - **5.3 «Un subagente, por dentro», partida de 5.2 durante el Render.** El FILL del modelo detectó que **ningún template del catálogo combina tarjetas y superficie de código**, así que el bloque de ejemplo se caía silenciosamente de la lámina. Se partió siguiendo el precedente ya aprobado de la Sección 3 (3.4 concepto + 3.5 ejemplo): 5.2 se queda con las 4 tarjetas (~2 min) y 5.3 con el archivo completo (~1 min). **La partición repartió los minutos, no los sumó.**
- Key inputs: los campos `Presenter feedback` de cada ronda; una pregunta al presentador sobre el choque de los subagentes; verificación web del 2026-07-31 (tres fuentes oficiales).
- Files created/modified: `draft.md`, `config/feedback-backlog.md` (5 filas), `memory.md`.

---

## 2026-07-31 — Step 6 (Polish, 5ª corrida) + Step 7 (Render html-strict, 5ª vuelta)

- Status: complete
- What was decided:
  - **Polish.** 10 bloques escaneados: **8 render-driving**, 2 documentation-only (`s3-5-1`, `s4-3-1`). **4 renderizados** (`s2-2-1` los dos paneles del `.md`, `s2-3-1` el bucle de iteración, `s4-2-1` las dos formas de usar una Skill, `s4-5-1` el flujo de grabar) y **4 reusados por digest**. El de grabar era un **renombre puro** (s4-4-1 → s4-5-1 por la renumeración): el PNG resultante es byte-idéntico al anterior, el deck no cambió un píxel ahí. Los cuatro PNG se revisaron a ojo y quedaron aprobados; las tres validaciones (`validate_svg`, `rasterize`, `audit_aspect`) pasaron en verde en los cuatro.
  - **`gc` corrido y aplicado:** 10 tripletes huérfanos, **30 archivos borrados**, todos de numeraciones viejas. `images/` bajó a 36.
  - `final.md` limpio: 14 refs, **todas `.png`** (los `.svg` quedan en disco como fuente); 31 campos `Presenter feedback` strippeados; `rescue-open` sin nada que rescatar.
  - **Render `html-strict`: 30 láminas** (portada + 7 divisorias + 23 de contenido), **2,6 MB** autocontenido en `output/html/index.html`. Las tres auditorías del modelo (`degenerate_enum`, `field_coverage`, `image_coverage`) dieron **ok**. Las 23 láminas llevan sus Speaker notes verbatim (tecla `s`).
  - El hint `<!-- layout: image-left -->` de 1.2 **sí está soportado** por este render y se aplicó.
- Files created/modified: `final.md`, `output/slide-model.json`, `output/html/index.html`, `images/` (4 tripletes nuevos, 30 archivos borrados), `memory.md`.
- Pending open questions:
  - **Un ícono no resolvió** en el render (`person_4`): salió `info` en su lugar. Cosmético, en una sola tarjeta.
  - **La numeración de las divisorias sigue por posición**, así que Conclusions sale `06` y la Sección 6 sale `07`. Es cromo del renderer, no del contenido.
  - Láminas **densas para mirar en sala**: 4.5 (6 tarjetas + imagen), 5.1 (5 tarjetas + imagen) y 3.3 (6 tarjetas mezclando dos grupos, candidata natural a partirse en dos).
  - **1.2 «De chatear a delegar»** quedó en `content-image` para honrar el hint de layout y no perder el diagrama; la tabla chatear/delegar sobrevive como cuatro hechos etiquetados. Si se prefiere la grilla comparativa, hay que sacrificar la imagen.
  - Sigue abierto: **3.2 con dos capturas apretadas**; posible solape entre `instructions.png` (3.4) y `context.png` (3.2); idioma mezclado en las capturas (`instructions.png` en inglés, las de la Sección 4 en español).
  - **La crítica visual ciega automática no se lanzó** esta corrida; los cuatro diagramas los revisó el orquestador a mano sobre el PNG.


---

## 2026-08-01 — Plugin 0.72.0 + regeneración end-to-end

- Status: complete
- **Los tres requerimientos que salieron de este Talk entraron al plugin** (`0.72.0`, commit `1cf93c2`). Los pedidos quedaron escritos en la raíz del repo: `req-layout-cci.md`, `req-highlights-arriba.md`, `req-citext-vacio.md`.
  - `layout` dejó de ser exclusivo de `content-image`: vale en `content+cards+image`, `process` y `quiz`. `image-top` sigue siendo solo de `content-image`.
  - `highlights[].position` (`bottom` default / `top`), **por entrada**, no por lámina. El de arriba está en pantalla desde que abre la lámina; el de abajo sigue llegando en el último clic.
  - La lámina de **imagen sola** es de primera clase: `content-image` sin `lead` ni `facts` no emite la columna y la imagen va a ancho completo. El mismo guard se aplicó a `code-example`, `callout`, `single-point`, `quiz`, `content-text` y `pros-cons`.
  - **Bonus, no pedido:** se arregló el *discriminator walk* del catálogo, que nombraba solo ~14 de 25 templates. Señales nuevas (`date_labels`, `is_voiced`, `is_question`, `polarity`, `one_metric`, `is_cta`, `image_only`) y dos bugs de orden — entre ellos el que mandaba *cualquier* set etiquetado con imagen a `content-image`, que es lo que disolvía las tarjetas en `facts`.
- **Hints anotados en `draft.md`** (se copian a `final.md` en cada Polish):
  - **1.2** — `template: content+cards+image` + `layout: image-left` pineados, más la recomendación de tratar la cita de Anthropic como `highlights` con `position: top`. El `template` está pineado **a propósito**: la lámina lleva una tabla y el discriminador manda las tablas a `comparison`, que no tiene ranura de imagen y perdería el diagrama.
  - **1.3** — nota de que la línea "Idea clave" es el `lead`, no un highlight de cierre.
  - **1.4** — nota de que es lámina de imagen sola y que **no** hay que forzarla a `image-grid` (el parche del 2026-07-31 ya no hace falta).
  - **2.2** — la recomendación del presentador de usar el estilo `code-example`, revisada contra 0.72.0 y **todavía sin salida limpia**: ese template sigue sin ranura de imagen. Las tres opciones siguen abiertas.
- **Cambios de clasificación** al rehacer el FILL de cero (5 láminas): 1.2 y 3.4 y 6.1 `content-image` → `content+cards+image` (recuperan el ícono por concepto); 1.4 `image-grid` → `content-image` (revertido el parche); 5.2 `concept-breakdown` → `icon-list` (su primera línea es `lead`, y `concept-breakdown` no tiene esa ranura). `layout` en 3 láminas (1.2 y 6.1 `image-left`, 1.3 `image-top`) y `position: top` en 3 (1.2, 4.1, 3.3).
- Polish: **0 renders nuevos**, los 8 bloques reusados por digest; `gc` limpio. Render: 30 láminas, 2,6 MB.
- Pending open questions:
  - **Falso positivo del propio plugin:** `audits/field_coverage.py` avisa `ignored: layout` en `content+cards+image` porque su tabla `_CONSUMES` no se actualizó en 0.72.0. El renderer **sí** lo consume (`content-cards-image.j2` → `m.imgpos(s)`; `theme.css` `.cci.imgleft`). Es advisory, no bloquea. Mismo caso en `process` y `quiz`.
  - **`layout: image-left` en 6.1** es juicio del FILL, no pedido del presentador. Fácil de revertir.
  - **1.1** pasó de 4 tarjetas a 3 + una cita (`is_voiced`): la línea de Anthropic es fuente, no concepto paralelo. Si el presentador la quiere de vuelta como tarjeta, son dos líneas.
  - **4.5** quedó con 6 tarjetas al lado de la imagen; el recorte natural es bajar "no tipear contraseñas" a `highlights` `kind: important`.
  - **3.3** dispara `is_question` y podría ser `quiz`, pero ese template no tiene dónde poner los seis bloques etiquetados. Quedó `concept-breakdown` con la pregunta arriba. Si se quiere quiz de verdad, hay que partirla.

---

## 2026-08-01 (2a sesion) — Lamina nueva del directorio + Polish + Render html-strict

- Status: complete
- **Decision permanente nueva: el tiempo dejo de ser restriccion.** Instruccion explicita del presentador. Los recortes de reserva anotados (5.3, y 3.5 de 3 a 2) quedan **anulados** y no se aplican.
- **Lamina nueva `## 3. Antes de escribir una: el directorio`** en la Seccion 4, entre «Como se usa una Skill» y las tres de metodo. Cierra la «lamina de catalogo de skills» que estaba abierta desde el 2026-07-30.
  - Se elegio el **directorio interno de la app** (Personalizar > Habilidades > "+" > Explorar habilidades > Instalar) mas las **cuatro habilidades incorporadas** (Excel, Word, PowerPoint, PDF), en vez de skills.sh / anthropics-skills / Vercel: es lo que mas le sirve a una audiencia de negocios y no exige linea de comandos.
  - 5 tarjetas + lead + cierre. Sin ASCII y sin `generate-image` **a proposito**: no hay captura del directorio en `images/`. Queda como watch item sacar la captura o mostrarlo en vivo.
  - Fuentes: support.claude.com/14328846 (ruta, boton Install, view-only, skills compartidas de la organizacion en Team/Enterprise) y support.claude.com/12512180 (las 4 incorporadas, requisito de Code execution, disparo automatico con el ejemplo del Q3). Ambas verificadas el 2026-08-01.
  - **Riesgo anotado:** los rotulos de UI en espanol son traduccion de la doc en ingles, sin leer la app en espanol. Confirmar antes de la clase.
- **La Seccion 4 pasa de 5 a 6 laminas** y las tres de metodo se renumeran a `## 4.` / `## 5.` / `## 6.`. Se arreglaron dos referencias cruzadas internas que la renumeracion rompia (Sources de la del panel: "4.5" -> "4.6"; ascii-note de Grabar: "4.3" -> "4.4").
- **Drift detectado entre `draft.md` y el `final.md` anterior.** La lamina del panel (hoy 4.4) habia perdido en `draft.md` su bullet de lead y su captura `skills-panel.png` — el `final.md` del 2026-08-01 00:10 todavia las tenia. Al re-derivar, la lamina quedo **solo con el diagrama**: el bloque ASCII dejo de ser documentation-only y se renderizo por primera vez como `s4-4-1-crear-skill-desde-el-panel.svg`. `skills-panel.png` quedo **sin referenciar**. Si la captura tiene que volver, es un bullet de feedback.
- **Polish (6a corrida).** 10 bloques escaneados: 9 render-driving + 1 documentation-only (`s3-5-1`). **1 render nuevo** (`s4-4-1`, las 4 entradas del menu Agregar; las tres validaciones en verde, revisado a ojo sobre el PNG), **1 renombre** (`s4-5-1` -> `s4-6-1`, se conservo el SVG aprobado y solo se re-estampo, asi que el dibujo no cambio un pixel), **7 reusados por digest**. `gc` aplicado: el triplete `s4-5-1` viejo se movio a `_to_delete/images-viejas-2026-08-01/`. `rescue-open` sin nada que rescatar; 32 campos `Presenter feedback` strippeados.
- **`final.md` ahora referencia `.svg`, no `.png`.** Confirmado sobre el archivo generado: los 9 diagramas salen como `images/<stem>.svg` y las 5 capturas siguen en `.png`. Los `.png` de los diagramas quedan en disco solo como companion para el camino `.pptx` (Keynote no embebe SVG). Es el comportamiento nuevo de 0.72.0.
- **Render html-strict (6a vuelta): 31 laminas, 1,8 MB** (bajo de 2,6 MB porque los diagramas ahora van como vector inline y no como PNG en base64). **Verificado en el HTML: los 9 SVG generados estan inlineados como vector** (9 stamps `talksmith-ascii-sha256` presentes) y **cero diagramas rasterizados**; los 8 `data:image/png` que quedan son las capturas y el logo.
- **FILL rehecho sobre el baseline aprobado**, no de cero. Una sola reclasificacion: la del panel, `content+cards+image` -> `content-image` imagen-sola (se quedo sin tarjetas ni lead). La lamina nueva del directorio salio **`icon-list`** (5 items etiquetados con cuerpos largos + lead), con el cierre "Regla practica" como `highlights` `kind: takeaway`. Las otras 29 entradas se copiaron tal cual. Las tres auditorias (`degenerate_enum`, `field_coverage`, `image_coverage`) en **ok**.
- Files created/modified: `draft.md` (+ backup `draft.bak-catalogo.md`), `final.md`, `output/slide-model.json`, `output/html/index.html`, `images/` (2 tripletes nuevos, 1 viejo movido a `_to_delete/`), `memory.md`.
- Pending open questions:
  - **Dos bullets de `Presenter feedback` sin procesar en `draft.md`**, anteriores a esta sesion: en 3.5, borrar las Instrucciones completas y dejar solo el texto de ejemplo; en 4.4, falta una lamina indice que liste las 3 formas de crear una Skill. Ninguno se aplico.
  - **`skills-panel.png` quedo huerfana** tras el drift descrito arriba. No se borro.
  - **La captura del directorio no existe.** Sacarla o mostrar el directorio en vivo.
  - **Nomenclatura en espanol de la lamina nueva sin verificar** contra la app.
  - Siguen abiertas las de la corrida anterior: el icono `person_4` que no resuelve, la numeracion de divisorias por posicion (Conclusions sale 06), las laminas densas 4.5 / 5.1 / 3.3, y el idioma mezclado entre capturas.
  - **La critica visual ciega automatica no se lanzo**; el diagrama nuevo lo reviso el orquestador a mano sobre el PNG.

---

## 2026-08-01 (3a sesion) — Reescritura de la Seccion 4 + Polish + Render

- Status: complete
- Ronda de 5 items del presentador, toda sobre la Seccion 4:
  1. **La 4.3 se reemplazo entera.** Salio «Antes de escribir una: el directorio» (escrita horas antes en esta misma jornada) y entro **`## 3. Tres formas de crear una Skill`**, una lamina indice con **solo tarjetas**: lead de una linea, 3 tarjetas (desde el panel / desde el prompt / grabando la pantalla) y cierre en la compuerta de guardar-habilitar. Cierra el bullet de feedback que estaba abierto desde el 2026-08-01 00:25 («Falta un slide que explique que hay 3 formas de crear un skill y listarlas»).
  2. **La 4.5 «Metodo 2» se reescribio entera.** El presentador senalo que la lamina no ensenaba lo que decia su titulo: mostraba el menu "+" del chat y la trampa del Save, no la creacion conversacional. Ahora son 5 tarjetas con el flujo real: se describe lo que se quiere > Claude pregunta por el proceso > se le suben materiales > Claude escribe el `SKILL.md` y empaqueta > se prueba y aparece «Usando [nombre]». **Fuente nueva y verificada el 2026-08-01:** claude.com/resources/tutorials/how-to-create-a-skill-with-claude-through-conversation (la URL de support 12599426 redirige ahi). Anotado que support 12512198 **no** documenta el camino conversacional, asi que la procedencia de cada afirmacion queda separada.
  3-5. **Renombres:** «Metodo 1: Crear desde el panel», «Metodo 2: Crear desde el prompt», «Metodo 3: Crear grabando una Skill».
- **El titulo del Metodo 3 se normalizo.** El presentador escribio «Metodo 3: Crear grabando una skill una Skill», con una repeticion evidente de tipeo. Se aplico «Crear grabando una Skill», que hace juego con los otros dos. **Queda por confirmar.**
- **Nada se borro en silencio.** Van a `Cut material`, verbatim y con nota de fecha y motivo: (a) la lamina entera del directorio — con el aviso de que, fuera del deck, el directorio de la app y las cuatro habilidades incorporadas ya no aparecen en ninguna parte de la charla; (b) el material de la ex 4.5 (bullet del menu "+", la captura `skills-menu-chat.png` y el bullet de la trampa del Save).
- **`skills-menu-chat.png` quedo sin referencia.** No se borro. Candidata natural a reponerse en la 4.2, que hoy explica la invocacion sin mostrar interfaz. Igual que `skills-panel.png`, huerfana desde la corrida anterior.
- Referencias cruzadas arregladas en 9 lugares (Narrative arc, Goal de la Seccion 4, notes de 4.1 / 4.4 / 4.6, el bullet «Donde» de 4.6, y dos entradas de Open questions que quedaron marcadas [SUPERADA]).
- **Polish (7a corrida): 0 renders nuevos**, los 9 bloques reusados por digest; `gc` limpio. `final.md` sigue referenciando **9 diagramas en `.svg`** y 4 capturas en `.png`.
- **Render html-strict (7a vuelta): 31 laminas, 1,7 MB.** Los 9 SVG inlineados como vector, cero diagramas rasterizados (7 `data:image/png` = capturas + logo). Las tres auditorias del modelo en **ok**.
- **FILL — dos clasificaciones nuevas.** La lamina indice salio **`card-row`** y no `icon-list`: el discriminador puro apuntaba a `icon-list` por el largo de los cuerpos, pero `icon-list` renderiza filas y no tarjetas, y el pedido del presentador fue explicito («idealmente solo con cards»). **Recomendacion pendiente: pinear `<!-- template: card-row -->` bajo el `## 3.`** para que el proximo FILL no re-derive `icon-list`. La 4.5 salio **`process`** (5 tarjetas numeradas): perdio la imagen, asi que `content-image` ya no aplicaba, y los pasos forman una secuencia real.
- Files created/modified: `draft.md` (+ backup `draft.bak-seccion4.md` en el contenedor), `final.md`, `output/slide-model.json`, `output/html/index.html`, `memory.md`, `config/feedback-backlog.md`.
- Pending open questions:
  - **Confirmar el titulo del Metodo 3.**
  - **Pinear `template: card-row` en la 4.3** o aceptar que el proximo FILL la pase a `icon-list`.
  - **Bullet de `Presenter feedback` sin procesar en la 3.5** (Seccion 3): borrar las Instrucciones completas y dejar solo el texto de ejemplo. Sigue abierto, no se toco.
  - **Dos capturas huerfanas:** `skills-panel.png` y `skills-menu-chat.png`.
  - **`images/create-skill.png`, sin usar, parece mejor que `skills-panel.png`**: muestra el panel con el menu Add desplegado y sus **cuatro** entradas, incluida «Record your screen», que es justo lo que la captura del 2026-07-21 no alcanza a mostrar. Dos peros: la 4.4 hoy no lleva ninguna imagen en su Content, y `create-skill.png` esta en ingles, asi que entra en el problema abierto de idioma mezclado entre capturas.
  - Siguen abiertas las anteriores: icono `person_4` sin resolver, numeracion de divisorias por posicion, laminas densas 4.5-vieja / 5.1 / 3.3, idioma mezclado entre capturas.

---

## 2026-08-01 (4a sesion) — Feedback Seccion 3 + incidente de sincronizacion + Polish/Render

- Status: complete
- **Feedback aplicado (2 items, Seccion 3):**
  - **3.2 «Conceder una carpeta y ver el contexto» quedo IMAGEN SOLA.** El bullet decia «De solo la images/context.png». Se interpreto primero como "de las dos capturas, quedate con context.png" y se dejaron los dos bullets de texto; **el presentador corrigio editando el archivo a mano**: saco todo el texto y dejo unicamente `images/context.png`. Version final: `content-image` sin `lead` ni `facts` — la forma imagen-sola de primera clase de 0.72.0, a ancho completo. El recorrido (explorador de archivos, alcance de la carpeta, mensaje de seguridad) vive entero en las Speaker notes. **Leccion: cuando el presentador nombra una sola imagen, el default es imagen sola.**
  - **3.5 «Un ejemplo de Instrucciones» quedo solo con el bloque de ejemplo.** Se borraron la linea de entrada y el bullet de la REGLA DE ORO. Template `code-example` **sin `explanation`**, que con el guard de 0.72.0 colapsa a ancho completo en vez de dejar medio panel vacio. La regla de oro no se perdio: sigue en las Speaker notes.
- **DECISION PERMANENTE NUEVA: el presentador borro `# Cut material` del `draft.md` y pidio expresamente NO recuperarlo** («esta bien perderlas, no las rescates»). Tambien se vacio el cuerpo de `# Open questions`. **A partir de ahora el material que sale de una lamina se borra, no se archiva** — la convencion de "nunca borrar en silencio, mover a Cut material" queda anulada para este Talk por instruccion explicita.
- **Incidente de sincronizacion (importante para futuras sesiones en Cowork remoto).** `device_stage_files` **devolvio una copia vieja** de `draft.md`: reporto los bytes correctos del archivo del dispositivo pero el destino en `/mnt/user-data/uploads/` quedo read-only con el contenido de la primera bajada, varias horas anterior. Consecuencia: una ronda de feedback se aplico sobre una base sin la reescritura de la Seccion 4 y hubo que descartarla. **Workaround que funciona: copiar el archivo a un nombre nuevo en el dispositivo (`.transfer-<hhmm>.md`), stagear ESE, y verificar `md5sum` de los dos lados antes de usarlo.** Se uso en las dos ultimas corridas y quedo verificado.
- **Polish (9a corrida): 0 renders**, por pedido explicito del presentador («pasamos a polish pero no regeneramos las imagenes»). Los 9 bloques reusados por digest; `gc` sin huerfanos.
- **`final.md`: 12 refs de imagen — 9 diagramas en `.svg` + 3 capturas en `.png`** (`cowork.png`, `context.png`, `instructions.png`). Salieron del deck `project.png` (3.2) y `skills-menu-chat.png` (ex 4.5); las dos siguen en `images/`, sin referencia.
- **Render html-strict: 31 laminas, 1,6 MB.** 9 SVG inlineados como vector, 6 `data:image/png` (capturas + logo). Auditorias `degenerate_enum` / `field_coverage` / `image_coverage` en **ok**.
- **Tres laminas quedaron en forma imagen-sola:** 1.4 «Donde se empieza en Cowork» (`cowork.png`), **3.2** (`context.png`) y 4.4 «Metodo 1: Crear desde el panel» (el diagrama SVG).
- Files created/modified: `draft.md` (editado por el presentador + los dos items de feedback), `final.md`, `output/slide-model.json`, `output/html/index.html`, `memory.md`. Backup de rescate: `draft.rescue-backup-0206.md`.
- Pending open questions:
  - **Confirmar el titulo «Metodo 3: Crear grabando una Skill»** (el pedido original traia una repeticion de tipeo).
  - **`4.3` esta pineada a `card-row` a mano en el FILL, no en el archivo.** El discriminador la manda a `icon-list` por el largo de los cuerpos. Si no se escribe `<!-- template: card-row -->` bajo el `## 3.`, un FILL futuro la va a cambiar.
  - **Dos capturas sin referencia:** `project.png` y `skills-menu-chat.png`.
  - `images/create-skill.png`, sin usar, muestra el panel con las cuatro entradas del menu Add — mejor que `skills-panel.png` para la 4.4, pero esta en ingles.
  - Siguen abiertas: icono `person_4` sin resolver, numeracion de divisorias por posicion, idioma mezclado entre capturas.

---

## 2026-08-01 (5a sesion) — Plugin a 0.74.1 + regeneracion del HTML

- Status: complete
- **La sesion arranco con el plugin en 0.72.0**, pero en GitHub ya estaban **0.73.0, 0.74.0 y 0.74.1**. Se actualizo la copia de la sesion a **0.74.1** clonando el repo publico. **Ojo: eso NO actualiza el plugin de la cuenta** — una sesion nueva de Cowork sincroniza lo que este publicado en la cuenta del usuario, no lo de GitHub.
- **`image-full` (0.73.0) es la categoria que el presentador estaba pidiendo.** Es el tipo propio para la lamina que ES una imagen: encabezado normal (pill de seccion + titulo, con `lead` opcional de una linea) y la imagen ocupa todo lo de abajo, sangrando a izquierda, derecha y borde inferior, sin padding, sin marco y sin epigrafe. **Contenida, nunca recortada**: una imagen mas angosta que el espacio se centra en vez de rellenar. `content-image` volvio a exigir su prosa.
- **Tres laminas pasaron de `content-image` sin texto a `image-full`:** 1.4 «Donde se empieza en Cowork», 3.2 «Conceder una carpeta y ver el contexto» y 4.4 «Metodo 1: Crear desde el panel».
- **0.74.0 — el conjunto etiquetado volvio a ser UN template.** `concept-breakdown`, `card-row` e `icon-list` eran tres reglas de Match para una misma forma, y era la familia que el FILL erraba mas seguido. Ahora la forma es la clasificacion (`concept-breakdown`) y la disposicion es un campo **`format`**: `grid` (default), `row`, `list` — el mismo patron que sigue `layout` para las imagenes. `card-row` e `icon-list` **siguen siendo valores validos** y emiten markup byte a byte identico, asi que no hay que migrar nada. **Consecuencia para el pin de la 4.3:** en vez de pinear `card-row`, lo limpio es `concept-breakdown` + `format: row`.
- **0.74.1 — el HTML ahora es un documento bien formado:** `<!doctype html>`, `<html lang="es">`, `<head>` y `<body>` explicitos. Antes era un fragmento suelto y el navegador lo levantaba en quirks mode; cualquier cosa que lo *embeba* (un panel de preview, un iframe, un sanitizador) podia descartar el `<meta>` y el `<style>` por estar fuera de un `<head>`. Render pixel-identico, es correccion sin cambio visual.
- **Render regenerado con 0.74.1: 31 laminas, 1,6 MB.** 0 diagramas re-renderizados. Auditorias aplicables al modo html (`degenerate_enum`, `field_coverage`, `image_coverage`) en **ok**; el resto del suite es solo para `.pptx`.
- Files created/modified: `output/slide-model.json`, `output/html/index.html`, `memory.md`. `draft.md` y `final.md` sin cambios.

---

## 2026-08-01 — Cierre del Talk

- Status: **complete**
- El presentador dio el Talk por terminado. **No se corrio el paso 8 (Learnings)**, asi que no se promovio ningun patron a `config/learnings.md` ni se curo nada a `knowledge-library/`. Si en algun momento se quiere cerrar formalmente, el material esta: `config/feedback-backlog.md` tiene el historial completo de las rondas, incluidas las cinco filas del 2026-08-01.
- **Estado entregable al cerrar:** `talks/claude-cowork/final.md` + `output/html/index.html` (deck Reveal.js autocontenido, 31 laminas, 1,6 MB, se abre con doble clic). Los 9 diagramas van como SVG vector inline. `output/final.pptx` **no existe** — este Talk nunca se rindio a PowerPoint.
- **Cosas para mirar antes de dictar la clase**, ninguna bloqueante:
  - Confirmar los rotulos de UI en espanol de la Seccion 4 contra la app en espanol.
  - El titulo «Metodo 3: Crear grabando una Skill» quedo normalizado por el orquestador, sin confirmar.
  - `skills-panel.png` es del 21 de julio y puede no mostrar la entrada «Graba tu pantalla».
  - Idioma mezclado entre capturas: `instructions.png` en ingles, las de la Seccion 4 en espanol.
  - Tres capturas quedaron en `images/` sin referencia: `project.png`, `skills-menu-chat.png`, `skills-panel.png`.

---

## 2026-08-01 (6a sesion) — Plugin 0.75.0: la lamina 1.2 con tabla + diagrama

- Status: complete
- **Plugin verificado en 0.75.0** antes de tocar nada (era la precondicion del pedido: con 0.74.1 no tenia sentido seguir).
- **La 1.2 «De chatear a delegar» pasa de `content+cards+image` a `value-columns`.** El pin ya venia hecho de la sesion anterior en `draft.md` (`<!-- template: value-columns -->` + `<!-- layout: image-left -->`); esta sesion solo lo llevo al render. En 0.75.0 `comparison` se renombro a **`value-columns`** (breaking, sin alias) y gano `image`, `layout` y `lead`, asi que la tabla `factor | Chatear | Delegar` ya no colapsa a tarjetas con las dos columnas concatenadas en el mismo `body`.
- **Ninguna otra lamina usaba `comparison`**, asi que el rename no obligo a migrar nada mas del modelo.
- **Step 6 (Polish) — 0 diagramas re-renderizados.** Los 9 bloques ASCII se reusaron por digest (`prepare-render-args` no emitio ningun args file); 1 bloque documentation-only omitido; sidecars sin cambios; `Presenter feedback` limpiado (24 campos H3 + 8 etiquetas de parrafo). El unico delta de `final.md` contra la corrida anterior es la lamina 1.2.
- **La directiva `generate-image` de la 1.1 quedo sin cumplir otra vez** — la sesion no tiene capacidad de generacion de imagenes. Degrada sin romper, igual que en 0.74.1.
- **Step 7 (Render html-strict) — 31 laminas, sin warnings en el build.** Auditorias aplicables al modo html en **ok**: `degenerate_enum`, `field_coverage`, `image_coverage`. **Sin aviso de densidad**: la grilla es 3 columnas x 4 filas, dentro del techo de 3x5 que impone `value-columns` al lado de una imagen.
- **Verificado sobre el HTML generado** (markup + captura del render): la 1.2 sale con `data-kind="value-columns"`, `<div class="compare" style="--cc:3">` con encabezado de 3 columnas y 4 filas alineadas (no tarjetas), `<div class="cmpgrid imgleft">` con `s1-2-1-chat-vs-agente.svg` inline a la izquierda (digest `7714d91a…`), y `<p class="lead">Lo que cambia ahora es el rol: delegar. ¿Que delegamos?</p>`. La cita de Anthropic quedo como highlight `position: top`, segun el hint del FILL.
- **Nota de entorno:** la sesion corrio en la nube, con el repo traido por el puente de dispositivo. Se devolvieron a disco `final.md`, `output/slide-model.json`, `output/html/index.html` y `memory.md`.
- **`req-comparison-imagen.md` no existe en la raiz del repo** (estan `req-citext-vacio.md`, `req-highlights-arriba.md` y `req-layout-cci.md`). No bloqueo nada: el requerimiento esta documentado en la memoria del proyecto (`catalogo-tabla-mas-imagen.md`) y en el propio comentario pineado de la lamina.
- Files created/modified: `final.md`, `output/slide-model.json`, `output/html/index.html`, `memory.md`. `draft.md` sin cambios (read-only desde Step 6).

---

## 2026-08-01 (6a sesion, ronda 2) — Fuera la cita de Anthropic de la 1.2

- Status: complete
- **Feedback del presentador:** sacar «Anthropic: Menos una sesion de chat, mas asignarle tareas a un colega.» de la lamina 1.2.
- **Se edito `draft.md`, no solo el modelo.** La cita no vivia en `### Content` sino en la RECOMENDACION para el FILL del comentario pineado (`highlights[].position: "top"`, kind quote). Borrar el `highlights` del `slide-model.json` sin tocar el hint la habria devuelto en la proxima corrida. El hint ahora dice explicitamente que la lamina **no lleva `highlights`** y que la cita no se devuelve a la cara.
- **Sigue viva donde corresponde:** en `### Sources` (atribucion de la pagina de producto de Anthropic) y en las speaker notes («Cerrar citando a Anthropic…»), asi que se puede decir al cerrar la lamina sin que ocupe lugar en pantalla. Si tambien hay que sacarla de ahi, es otro pedido.
- **Polish + Render re-corridos:** 0 diagramas re-renderizados (los 9 reusados por digest), 31 laminas, build sin warnings, `degenerate_enum` / `field_coverage` / `image_coverage` en ok, sin aviso de densidad.
- **Verificado sobre el HTML:** la 1.2 ya no tiene `class="highlights"`; conserva `data-kind="value-columns"`, la grilla `--cc:3` de 3 columnas x 4 filas, `cmpgrid imgleft` con el SVG inline y el `<p class="lead">`. La cadena de la cita solo aparece ya dentro del `<aside class="notes">`.
- Files created/modified: `draft.md`, `final.md`, `output/slide-model.json`, `output/html/index.html`, `memory.md`.
