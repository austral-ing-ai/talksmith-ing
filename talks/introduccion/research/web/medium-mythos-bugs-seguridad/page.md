# Mythos Found Bugs That 50 Million Security Tests Missed. Nobody Asked It To.

_Source: <https://medium.com/data-science-collective/mythos-found-bugs-that-50-million-security-tests-missed-nobody-asked-it-to-92c204d6e738>_

> Extracción manual. `talksmith:ingest` recibe **HTTP 403** de Medium, así que no hay
> `original.html`. El contenido de abajo se obtuvo con la herramienta de fetch de la sesión
> (WebFetch), que devuelve la porción del artículo accesible sin suscripción. **La captura es
> parcial**: el cuerpo detrás del muro de pago no se alcanzó.

## Metadatos

- **Autor:** Satyam Sahu
- **Publicación:** Data Science Collective (Medium)
- **Fecha:** 13 de abril de 2026
- **Acceso:** parcial (muro de pago)

## Qué afirma la porción accesible

- **Claude Mythos Preview** es un modelo de Anthropic publicado el **7 de abril de 2026**, con
  acceso restringido a **12 empresas socias** y **40 organizaciones de infraestructura crítica**
  bajo el programa **Project Glasswing**.
- Anthropic no lo liberó al público por motivos de seguridad, con el argumento de que
  *"the model is too capable to release safely"*.
- El artículo sostiene que Mythos encontró vulnerabilidades en firewalls bancarios, sistemas
  operativos de redes hospitalarias y códecs de video, que habían pasado desapercibidas para
  equipos de seguridad profesionales durante décadas.

## Lo que NO contiene la porción accesible

- **Ninguna mención a BSD, FreeBSD, OpenBSD, NetBSD, NFS, kernel, códec, CVE ni firewall**
  como caso concreto. Las referencias a firewall bancario / hospital / códec son ilustrativas,
  no casos documentados.
- Sin números de CVE, sin reportes de bug, sin estudios de caso con nombre.
- La cifra de "50 millones de tests" del título no aparece desarrollada en la porción accesible.

## Nota para quien cite esta fuente

El **bug de FreeBSD** (ejecución remota de 17 años en NFS) **no sale de este artículo**. Está
documentado en `freebsd-forums-mythos-zero-days.web.md`. Las cifras de impacto salen de
`engadget-mythos-glasswing-10000.web.md`. Este registro sirve para fechar el anuncio y el
encuadre de Project Glasswing, no como respaldo del caso técnico.
