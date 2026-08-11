# Misión: Corta — del caos a producción

## 📖 La historia

Se incorporan al equipo de desarrollo de una empresa. El desarrollador anterior —que se fue hace un mes y no dejó documentación— era el dueño de **Corta**, el acortador de URLs interno que usa toda la empresa. Antes de irse, lo único que entregó fue una carpeta copiada de su computadora.

Eso es lo que tienen: la carpeta `corta/`. Sin git. Sin README. Con archivos duplicados, versiones viejas, notas sueltas, dependencias que nadie usa... y una app que "más o menos anda" en local, tiene errores conocidos por los usuarios, y una funcionalidad que quedó a medio hacer.

Su trabajo: **llevar Corta a producción**, con historia completa en GitHub desde el estado en que la recibieron.

## 🛠️ Las herramientas

Trabajan con un agente de código — **Claude Code** o **Codex**, el que use su grupo — y dos MCP servers:

- **GitHub MCP server** — versionado y repositorio remoto: https://github.com/github/github-mcp-server
- **Railway MCP server** — infraestructura: servidores, bases de datos y deploy: https://docs.railway.com/ai/mcp-server

## 🚦 Antes de todo (obligatorio)

Lo primero que tienen que lograr, antes de tocar un solo archivo:

1. **Parar el agente en la carpeta** `corta/` (abrir Claude Code o Codex con esa carpeta como directorio de trabajo).
2. **Configurar los dos MCP servers** (GitHub y Railway) en el agente.
3. **Hacer que el agente lea las especificaciones de ambos MCPs** (los links de arriba). El criterio: el agente tiene que poder explicarles qué herramientas expone cada server y para qué las va a usar en esta misión.

Recién ahí empieza la misión.

## 🎯 Milestones

### Milestone 1 — Trackear desde el principio

Creen el repositorio en GitHub **usando el MCP de GitHub** y pusheen la carpeta **tal cual está, antes de cualquier cambio**. El desorden inicial tiene que quedar registrado en la historia: todo lo que hagan después va a ser un diff visible sobre ese punto de partida.

**Criterio de éxito:** el primer commit del repo muestra la carpeta original desordenada, y cada cambio posterior es trazable desde ahí.

> Ojo: "tal cual está" es una decisión con matices. ¿Todo lo que hay en la carpeta merece viajar a un repositorio remoto? Lo que decidan, tienen que poder defenderlo.

### Milestone 2 — Ordenar

Dejen el repositorio en un estado del que no haya que pedir perdón: estructura clara, sin archivos muertos ni duplicados, sin dependencias que nadie usa, con `README` y `.gitignore`.

**Criterio de éxito:** una persona que clona el repo entiende qué es el proyecto, cómo correrlo y qué hace cada archivo en menos de dos minutos.

### Milestone 3 — Corregir los errores

La app tiene errores. Encontrarlos es parte del trabajo — la mejor pista es **usar la app** como la usaría un empleado de la empresa, y leer con atención lo que dejó el desarrollador anterior.

**Criterio de éxito:** acortar funciona, el link corto **te lleva** a destino, y las estadísticas cuentan la verdad. Además tienen que poder responder: *¿qué pasa si dos URLs reciben el mismo código corto?* — y que la respuesta sea "nada malo, lo arreglamos".

### Milestone 4 — Completar lo que falta

La página de estadísticas (`public/stats.html`) quedó maquetada pero no consulta nada. El encargo pendiente del equipo:

- Un endpoint `GET /api/links/:codigo/stats` que devuelva clicks, URL original y fecha de creación.
- Que `stats.html` lo consulte y muestre los datos reales.

**Criterio de éxito:** entrás un código en la página de estadísticas y ves sus números de verdad.

### Milestone 5 — Producción

Deployen Corta en Railway **usando su MCP**: servicio corriendo, URL pública, y la configuración que haga falta.

Una pregunta va a aparecer sola cuando piensen este milestone: **¿dónde viven los datos en producción?** La respuesta del desarrollador anterior no sobrevive a un deploy. Railway también resuelve esa parte — la base de datos se crea desde el mismo MCP.

**Criterio de éxito:** cualquiera de la clase, desde su celular, acorta una URL en la app de ustedes y el link corto funciona. Y la prueba de fuego: **los links y sus clicks sobreviven a un redeploy**.

> Sobre secretos: si en algún punto manejan credenciales (de la base de datos, por ejemplo), pregúntense dónde deben vivir. Spoiler: en el código no. Ni en un `.txt`.

## 📦 La entrega

- **La URL pública** de Corta en producción.
- **El link al repositorio** en GitHub, con la historia completa: del caos del primer commit a producción.
