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
3. **Hacer que el agente lea las especificaciones de ambos MCPs** (los links de arriba). El criterio: el agente tiene que poder explicarles qué herramientas expone cada server y para qué las va a usar en esta misión.

Recién ahí empieza la misión.

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

## La entrega

- **La URL pública** de Corta en producción.
- **El link al repositorio** en GitHub, con la historia completa: del caos del primer commit a producción.
