# CLAUDE.md: talks/clase2 (talksmith-ing)

Plan de trabajo para armar las diapositivas de la **clase 2** de la materia de
ingeniería informática (Universidad Austral). Este deck es la **versión
adaptada a ingeniería** de la clase Claude Cowork que se dio en el MiM (IAE):
mismos conceptos, pero en el mundo del código con **Claude Code / Codex**, y
con la misión "Corta" integrada en la misma clase. Leé esto entero antes de
empezar.

## La idea central

El deck del MiM (`talks/claude-cowork/`, de Paulo Veiga, también presente en
este repo) enseña a delegar trabajo en un agente de escritorio (Cowork) usando
carpetas, archivos .md, Projects, Skills y subagentes, y remata con la misión
Faro. Esta clase enseña **lo mismo pero para programadores**: delegar trabajo
de desarrollo en un agente de código, con el repo como contexto, MCP servers
como herramientas, y la misión Corta como práctica.

La audiencia sabe programar, así que:

- No se explica qué es una terminal, un repo ni un deploy.
- Se va más rápido por los conceptos y más profundo en los mecanismos
  (qué contexto ve el agente, cómo decide usar una herramienta MCP).
- Es **una sola clase**: teoría + presentación de la misión juntas, sin
  kickoffs separados como en el MiM.

## Cómo se arma el deck: mapeo desde las clases del MiM

Se usan **las dos** clases del MiM como fuente (decisión de Marco,
2026-08-12): `talks/claude-cowork/draft.md` (estructura base) y
`talks/claude-desktop-chat/draft.md` (aporta el encuadre introductorio,
el argumento de contexto, el material MCP de la sección Connectors y
Schedule). La traducción propuesta, sección por sección (a validar con
Marco antes de escribir):

| Deck MiM (Cowork) | Deck ingeniería (Claude Code/Codex) |
|---|---|
| 1. Claude Cowork: de propósito general, de chatear a delegar, el mapa de piezas, dónde se empieza | 1. Agentes de código: qué son Claude Code y Codex, de autocompletar/chatear a delegar tareas enteras, el mapa de piezas (modelo, agente, contexto, herramientas, tareas), instalación y arranque en una carpeta |
| 2. Knowledge & Output: qué lee el agente en la carpeta, qué es un .md, iterar en .md | 2. El repo como contexto: qué lee el agente al pararse en una carpeta (código, README, configs), CLAUDE.md / AGENTS.md como memoria e instrucciones del repo, iterar con el agente sobre el código |
| 3. Projects: conceder carpeta, contexto, Instrucciones como contrato | 3. El contrato de trabajo: CLAUDE.md del proyecto (equivalente de las Instrucciones del Project), qué conviene fijar ahí y qué no |
| 4. Skills | 4. Skills y comandos en Claude Code/Codex (versión breve: la audiencia las va a descubrir sola; mostrar una de ejemplo) |
| 5. Subagentes | 5. Subagentes en Claude Code (versión breve) |
| (los conectores aparecen dentro de la misión del MiM) | 6. **MCP servers** (sección central y nueva): qué es MCP, cómo un agente descubre y usa herramientas, los dos de la misión: GitHub MCP y Railway MCP, leer la spec antes de usar |
| Conclusions + cuidados | Conclusions + cuidados (secretos, revisar diffs antes de commitear, el agente se equivoca con confianza) |
| 6. La misión parte 2 | 7. La misión: Corta (enunciado, reglas de trabajo, entrega) |

Aportes de `talks/claude-desktop-chat/draft.md` por sección destino:

| Deck MiM (Desktop Chat) | Va a la sección de ingeniería |
|---|---|
| 1. Introducción: el problema, cómo lo atacamos, quién es Anthropic, las cuatro herramientas | 1. Agentes de código (encuadre del problema y catálogo, adaptado a desarrollo) |
| 2. Context augmentation: el chat responde de memoria, dos formas de enriquecer | 2. El repo como contexto (el argumento de por qué el contexto importa) |
| 4. Connectors, slides 6 a 8: todo pasa por MCP, agregar un external connector, dónde buscar servidores publicados | 6. MCP servers (base principal de la sección) |
| 6. Schedule: describir una vez, que corra sola; dónde vive; local o nube | 7. La misión (extra de equipo: la tarea programada de reporte de cambios) |
| Conclusions y cuidados (prompt injection) | Conclusions + cuidados |

Criterio general de adaptación: **el concepto se mantiene, el ejemplo cambia
de mundo**. Donde el MiM muestra una carpeta de finanzas desordenada, acá hay
un repo desordenado; donde el MiM programa un email semanal, acá una tarea
programada que reporta cambios del repo; donde el MiM conecta Gmail y Massive,
acá GitHub y Railway por MCP.

Para la parte de la misión, la referencia de tono y estructura son nuestros
kickoffs del MiM: `talksmith-mim/talks/mision-kickoff-parte1/` y `-parte2/`
(reglas de trabajo en grupo, checklist, entrega). Acá se condensa en pocas
slides porque el enunciado completo vive en `missions/clase2/mission.md`.

## El pipeline de producción

El mismo de Talksmith que usamos en el MiM:

1. `draft.md` en esta carpeta (canónico, con Thesis, Agenda, secciones y
   slides; seguir el formato de los drafts existentes en `talks/`).
2. Review y polish; `final.md` se deriva del draft.
3. `output/slide-model.json` (FILL manual sobre los templates) y render HTML
   con el skill `talksmith:md-to-deck` (estilo `html-strict`).
4. Export a PDF solo si hace falta: chrome headless con `?print-pdf` es
   intermitente, reintentar hasta que la cantidad de páginas coincida.

Trampas de templates conocidas (del MiM): 4 cards en 2x2 desbordan (usar 3,
la tercera va full-width, o 5+ en 3 columnas); listas de 4 items van bien en
`icon-list`; `content-image` con `facts:[]` deja la barra de cita vacía;
`divider` no soporta imagen.

## La misión ya construida (contexto para las slides)

`../../missions/clase2/`: enunciado `mission.md` + carpeta `corta/` (acortador
de URLs Node/Express, real y funcionando con `npm start`).

Arco: (0) obligatorio: parar el agente en `corta/`, configurar los MCPs de
GitHub y Railway y hacerle leer las specs de ambos; (1) crear repo y pushear
el desorden tal cual; (2) ordenar; (3) corregir los errores; (4) completar
stats (`GET /api/links/:codigo/stats` + `stats.html`); (5) deploy en Railway,
donde `links.json` muere con el filesystem efímero y fuerza Postgres vía MCP;
(6) extra de equipo: todos colaboradores del repo y una tarea programada por
integrante que actualiza desde el remote y genera un reporte de cambios;
(7) extra de memoria (agregado 2026-08-12): una Skill `/collect-memory` que
actualiza la memoria y las instrucciones del agente (CLAUDE.md / AGENTS.md)
con los avances de la conversación y las preferencias expresadas por el equipo.

Bugs plantados (verificados): redirect con `res.send` en vez de
`res.redirect`; clicks que no se persisten; colisión de códigos
(`Math.random()` de 3 chars sin chequeo); `links.json` como base de datos.
Extras: puerto 3000 hardcodeado, credencial vieja en `notas.txt`.

Requisitos de los alumnos: cuenta de GitHub y cuenta gratuita de Railway.
Herramienta libre, recomendadas Claude Code o Codex.

## Decisiones ya tomadas

- Mapeo validado por Marco (2026-08-12): MCP queda como sección 6, al final
  de la teoría y pegada a la misión; Skills y Subagentes van breves, 2 slides
  cada una.
- Duración: 90 minutos.
- Byline: Paulo Veiga y Marco Sánchez Sorondo.
- Una sola clase, un solo deck (teoría + misión).
- Enunciado en `.md` dentro de la misión, no PDF.
- Sin fechas ni deadlines en los materiales.
- Sin em dashes ni emojis en los documentos de este repo (pedido de Marco).
- Idioma: español rioplatense, registro profesional cercano; términos
  técnicos en inglés.
- `talks/claude-cowork/` es territorio de Paulo: se lee como referencia, NO se
  edita.
- Commit/push solo si Marco lo pide explícitamente.

## Pendiente

1. `draft.md` escrito (2026-08-12, 22 laminas, 8 bloques). Falta: review de
   Marco (feedback como bullets en los `Presenter feedback` del draft o en
   chat), y resolver las Open questions del final del draft (fecha de la
   clase, re-verificar URLs de docs, presupuesto de tiempo, mecanismo
   sugerido para la tarea programada del extra).
2. Al cerrar tareas, actualizar la sección `talksmith-ing/` de
   `~/Escritorio/austral/CLAUDE.md`.
