# Misión: Corta, del caos a producción

## La historia

Se incorporan al equipo de desarrollo de una empresa. El desarrollador anterior, que se fue hace un mes y no dejó documentación, era el dueño de **Corta**, el acortador de URLs interno que usa toda la empresa. Antes de irse, lo único que entregó fue una carpeta copiada de su computadora.

Eso es lo que tienen: la carpeta `corta/`. Sin git. Sin README. Con archivos duplicados, versiones viejas, notas sueltas, dependencias que nadie usa... y una app que "más o menos anda" en local, tiene errores conocidos por los usuarios, y una funcionalidad que quedó a medio hacer.

Su trabajo: **llevar Corta a producción**, con historia completa en GitHub desde el estado en que la recibieron.

## Las herramientas

Trabajan con un agente de código y dos MCP servers. Pueden usar la herramienta de IA que prefieran, pero recomendamos **Claude Code** o **Codex**.

Los MCP servers:

- **GitHub MCP server**, para versionado y repositorio remoto: https://github.com/github/github-mcp-server
- **Railway MCP server**, para infraestructura: servidores, bases de datos y deploy: https://docs.railway.com/ai/mcp-server

### Requisitos

- Una cuenta de **GitHub** (la de algún integrante del grupo).
- Una cuenta de **Railway** (el plan gratuito alcanza).

## Antes de todo (obligatorio)

Lo primero que tienen que lograr, antes de tocar un solo archivo:

1. **Parar el agente en la carpeta** `corta/` (abrir Claude Code, Codex o la herramienta que hayan elegido con esa carpeta como directorio de trabajo).
2. **Configurar los dos MCP servers** (GitHub y Railway) en el agente.
3. **Hacer que el agente lea la documentación de ambos MCP servers** (los links de arriba). El criterio: el agente tiene que poder explicarles qué herramientas expone cada server y para qué las va a usar en esta misión.

Recién ahí empieza la misión.

## La forma de trabajo: SPEC.md y TDD

El dueño de Corta tenía todo el conocimiento del proyecto en la cabeza y nunca lo plasmó en un documento. Ustedes van a hacer lo que él no hizo. Dos prácticas obligatorias que atraviesan todos los milestones:

1. **SPEC.md**: escriban un archivo `SPEC.md` en la raíz del repo donde se plasme, con lujo de detalle, lo que se espera de Corta: qué hace cada endpoint, qué pasa en los casos borde (códigos repetidos, URLs inválidas, links inexistentes), qué cuenta como "las estadísticas dicen la verdad". Se escribe temprano (con lo que vayan descubriendo del proyecto heredado) y se actualiza cuando el entendimiento cambia.
2. **TDD**: deriven de `SPEC.md` una batería de tests bien grande, escrita **antes** de implementar cada corrección o feature. El agente implementa hasta que los tests pasen; ustedes revisan contra criterios que ya estaban acordados.

**Criterio de éxito:** `SPEC.md` está en el repo y refleja el comportamiento real de la app; la batería de tests lo cubre y corre verde en cada milestone; la historia de git muestra tests que aparecen antes que las implementaciones que los hacen pasar.

## Milestones

### Milestone 1: trackear desde el principio

Creen el repositorio en GitHub **usando el MCP de GitHub** y pusheen la carpeta **tal cual está, antes de cualquier cambio**. El desorden inicial tiene que quedar registrado en la historia: todo lo que hagan después va a ser un diff visible sobre ese punto de partida.

**Criterio de éxito:** el primer commit del repo muestra la carpeta original desordenada, y cada cambio posterior es trazable desde ahí.

> Ojo: "tal cual está" es una decisión con matices. ¿Todo lo que hay en la carpeta merece viajar a un repositorio remoto? Lo que decidan, tienen que poder defenderlo.

### Milestone 2: ordenar

Dejen el repositorio en un estado del que no haya que pedir perdón: estructura clara, sin archivos muertos ni duplicados, sin dependencias que nadie usa, con `README` y `.gitignore`.

**Criterio de éxito:** una persona que clona el repo entiende qué es el proyecto, cómo correrlo y qué hace cada archivo en menos de dos minutos.

### Milestone 3: corregir los errores

La app tiene errores. Encontrarlos es parte del trabajo. La mejor pista es **usar la app** como la usaría un empleado de la empresa, y leer con atención lo que dejó el desarrollador anterior.

**Criterio de éxito:** acortar funciona, el link corto **te lleva** a destino, y las estadísticas cuentan la verdad. Además tienen que poder responder: *¿qué pasa si dos URLs reciben el mismo código corto?*, y que la respuesta sea "nada malo, lo arreglamos".

### Milestone 4: completar lo que falta

La página de estadísticas (`public/stats.html`) quedó maquetada pero no consulta nada. El encargo pendiente del equipo:

- Un endpoint `GET /api/links/:codigo/stats` que devuelva clicks, URL original y fecha de creación.
- Que `stats.html` lo consulte y muestre los datos reales.

**Criterio de éxito:** entrás un código en la página de estadísticas y ves sus números de verdad.

### Milestone 5: producción

Deployen Corta en Railway **usando su MCP**: servicio corriendo, URL pública, y la configuración que haga falta.

Una pregunta va a aparecer sola cuando piensen este milestone: **¿dónde viven los datos en producción?** La respuesta del desarrollador anterior no sobrevive a un deploy. Railway también resuelve esa parte: la base de datos se crea desde el mismo MCP.

**Criterio de éxito:** cualquiera de la clase, desde su celular, acorta una URL en la app de ustedes y el link corto funciona. Y la prueba de fuego: **los links y sus clicks sobreviven a un redeploy**.

> Sobre secretos: si en algún punto manejan credenciales (de la base de datos, por ejemplo), pregúntense dónde deben vivir. Spoiler: en el código no. Ni en un `.txt`.

## Extra: trabajo en equipo

Hasta acá alcanza con una cuenta de GitHub. Este extra convierte el repo en un proyecto de equipo de verdad:

1. **Todos colaboradores**: cada integrante del grupo, con su propia cuenta de GitHub, se suma al repositorio como colaborador (la invitación también sale por el MCP de GitHub). A partir de ahí, los cambios entran con autor real: se tiene que poder ver quién hizo qué en la historia.
2. **Una tarea programada por integrante**: cada uno deja configurada, en su propia máquina y con su agente, una tarea programada que:
   - actualiza su copia local del repositorio desde el remote, y
   - genera un **reporte de los cambios del repositorio** (qué commits nuevos entraron, de quién, qué archivos tocaron) en el formato que elijan.

**Criterio de éxito:** el repo muestra commits de todos los integrantes, y cada uno puede mostrar su tarea programada disparándose y produciendo el reporte con los cambios reales del repo.

## Extra: la memoria del agente

Durante la misión le van a explicar cosas al agente más de una vez: cómo correr la app, qué decidieron sobre los archivos dudosos, qué formato de commits usan. Este extra convierte ese aprendizaje en una pieza permanente:

1. **Creen una Skill `/collect-memory`**: al invocarla, revisa la conversación en curso y actualiza la memoria y las instrucciones del agente (el `CLAUDE.md` / `AGENTS.md` del repo) con dos cosas: los avances (qué milestones están hechos, qué quedó a medias, qué decisiones se tomaron) y las preferencias que ustedes expresaron en la conversación (convenciones, reglas, gustos del equipo).
2. **Úsenla de verdad**: al cerrar cada sesión de trabajo, `/collect-memory`. La sesión siguiente arranca con el contrato al día.

**Criterio de éxito:** en una sesión nueva, el agente ya sabe qué está hecho y qué reglas rigen sin que nadie se lo repita, y la historia de git de `CLAUDE.md` muestra las actualizaciones que la Skill fue haciendo.

## La entrega

- **La URL pública** de Corta en producción.
- **El link al repositorio** en GitHub, con la historia completa: del caos del primer commit a producción.
