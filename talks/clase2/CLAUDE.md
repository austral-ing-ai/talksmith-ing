# CLAUDE.md: talks/clase2 (talksmith-ing)

Contexto de traspaso para continuar el trabajo empezado en una sesión sobre
`talksmith-mim`. Leé esto entero antes de tocar nada.

## Qué es esto

Deck de la **clase 2** de la materia de **ingeniería informática (Universidad
Austral)**: la variante técnica de la clase Claude Cowork que se dio en el MiM
(IAE). Mismos conceptos (agente, contexto, herramientas, tareas, verificación),
pero traducidos al mundo del código con **Claude Code / Codex**; cada grupo usa
el que tenga.

Diferencias clave con el MiM:

- **Audiencia técnica**: estudiantes de ingeniería informática, saben programar.
- **Una sola clase**: toda la presentación junta. En el MiM la misión se partió
  en 2 partes con un kickoff cada una; acá NO, es un solo deck.
- **Enunciado en `.md`**, no PDF: vive dentro de la propia misión.

## La misión ya está construida

`../../missions/clase2/` (relativo a esta carpeta):

- **`mission.md`**: el enunciado. Historia: heredan "Corta" (acortador de URLs
  interno de una empresa) del desarrollador que se fue; la carpeta está
  desordenada, sin git, con errores y una feature a medio hacer.
- **`corta/`**: la carpeta desordenada, real y funcionando (`npm start`, puerto
  3000). Node + Express, persistencia en `links.json`.

**El arco de la misión** (todo con los MCP servers de GitHub y Railway):

0. *Obligatorio antes de todo*: parar el agente en `corta/`, configurar ambos
   MCPs y hacerle **leer las especificaciones** de los dos
   (github.com/github/github-mcp-server y docs.railway.com/ai/mcp-server).
1. Crear repo en GitHub vía MCP y **pushear la carpeta tal cual está**: el
   desorden queda en la historia y todo lo posterior es diff visible.
2. Ordenar el repo (muertos, duplicados, deps sin uso, README, .gitignore).
3. Corregir los errores (encontrarlos es parte del trabajo; la pista es usar la app).
4. Completar la feature faltante: endpoint `GET /api/links/:codigo/stats` y
   conectar `public/stats.html`.
5. Deploy a producción en Railway vía MCP. La persistencia en `links.json` no
   sobrevive al filesystem efímero, lo que **obliga a crear Postgres desde el
   MCP de Railway**. Criterio: la clase acorta links desde el celular y los
   datos sobreviven a un redeploy.
6. Extra de trabajo en equipo: todos los integrantes se suman como
   colaboradores del repo (cada uno con su GitHub, invitación vía MCP), y cada
   uno configura una tarea programada en su máquina que actualiza la copia
   local desde el remote y genera un reporte de los cambios del repositorio
   (commits nuevos, autores, archivos tocados).

**Los 4 bugs plantados** (verificados en vivo):

1. Estructural: `links.json` como base de datos (`fs.writeFileSync`); anda
   local, inviable en producción. Es el que fuerza la DB.
2. Lógica: el redirect hace `res.send(url)` en vez de `res.redirect(url)`;
   devuelve 200 con la URL como texto.
3. Datos: los clicks se incrementan en memoria pero nunca se persisten (falta
   `guardarLinks` en el handler del redirect); quedan clavados.
4. Colisión: `utils.js` genera códigos de 3 chars con `Math.random()` sin
   chequear existencia.

Extra sutil: puerto 3000 hardcodeado (Railway necesita `process.env.PORT`).
Extra de secretos: `notas.txt` tiene la credencial de un postgres viejo, que
habilita la conversación de secretos/variables de entorno y qué se pushea.

Desorden fabricado: `server_OLD.js`, `index_v2_FINAL.js`, `test.js` a medio
hacer, `notas.txt` (los TODOs funcionan como pistas), `links_backup_marzo.json`,
`estilos_viejos.css`, `logo (1).png`, `Nueva carpeta/` vacía, lodash/moment sin
uso, `node_modules/` instalado (18MB).

## Material de referencia en talksmith-mim

`~/Escritorio/austral/talksmith-mim/talks/`:

- **`claude-cowork/`**: la clase Cowork del MiM (deck de Paulo Veiga). Es la
  base conceptual a traducir. OJO: ese talk es territorio de Paulo; se lee, NO
  se edita.
- **`mision-kickoff-parte1/` y `-parte2/`**: nuestros kickoffs de la misión del
  MiM (draft.md, slide-model.json, HTML). Útiles como referencia de tono,
  templates y del pipeline completo.
- El enunciado del MiM: `talksmith-mim/missions/CoWork/mission.md` (misión
  "Faro", analista financiero con conectores y tarea programada).

Notas de pipeline aprendidas en el MiM (ver `memory.md` de esos talks): export
a PDF con chrome headless `?print-pdf` es intermitente, reintentar hasta que
las páginas coincidan; templates: 4 cards en 2x2 desbordan, con 3 cards la
tercera va full-width; `content-image` con `facts:[]` deja la barra de cita
vacía.

## Decisiones ya tomadas

- Caso elegido: **acortador de URLs** ("Corta") por ser técnicamente simple; la
  DB es obligatoria vía el bug estructural, no por capricho del enunciado.
- El enunciado exige leer las specs de los MCPs **antes** de empezar.
- Herramienta: pueden usar cualquier herramienta de IA, pero se recomienda
  Claude Code o Codex. Requisitos: cuenta de GitHub y cuenta gratuita de
  Railway por grupo.
- Sin fechas ni deadlines en los materiales (regla heredada del MiM).
- Sin em dashes ni emojis en los documentos de este repo (pedido de Marco).
- Idioma: español rioplatense, registro profesional cercano; términos técnicos
  en inglés.

## Pendiente (en orden)

1. **Este deck**: la presentación de la clase, análoga a `claude-cowork` del MiM
   pero para Claude Code/Codex, más la presentación de la misión (una sola
   clase, todo junto). Falta definir estructura y contenido; ese es el trabajo
   a continuar acá.
2. `/talksmith:init` en la raíz de `talksmith-ing`: Marco dijo "todavía no";
   preguntar antes de correrlo. OJO: el repo NO estaba vacío, ya tiene `talks/`
   (claude-cowork, introduccion, claude-desktop-chat), `config/`, README y
   AGENTS.md propios; revisar qué hay antes de pisar nada.
3. **Byline de autores**: sin definir para esta materia (en el MiM era
   Paulo Veiga, Marco Sánchez Sorondo, Claudio Righetti y Juan Pablo
   Cosentino). Preguntar a Marco quiénes van.
4. Commit/push **solo si Marco lo pide** explícitamente.

## Estado de la memoria

`~/Escritorio/austral/CLAUDE.md` ya tiene la sección `talksmith-ing/` con el
estado del subproyecto; mantenerla al día al cerrar tareas.
