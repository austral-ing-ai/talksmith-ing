# 🏛️ Misión: "El vigía regulatorio de Atlas"

> **Tu desafío como CEO:** dirigís **Atlas**, una empresa de insumos de perforación para Vaca Muerta, y querés **escalar sin llenar la empresa de gente**. Ya automatizaste una parte en **Paperclip**: un equipo de agentes de IA que produce tu contenido de marca. Pero un cambio regulatorio se te coló por el costado y te costó caro. En vez de sumar personas, vas a **enseñarle a esa automatización a vigilar el riesgo por su cuenta**: sumás un agente nuevo. Tres pasos. Sin escribir una línea de código. **Empezamos.**

---

## 🎬 La situación

Sos **CEO de Atlas**, insumos de perforación para **Vaca Muerta**. Para crecer sin duplicar la nómina, automatizaste una parte de la empresa en **Paperclip**: un equipo de **agentes de IA** —marketing, contenido, legales— que publica contenido técnico y posiciona la marca, con vos como la firma final.

Funcionaba. Hasta que, el trimestre pasado, un cliente grande —ligado a YPF— te avisó: *"Desde el próximo trimestre solo contratamos proveedores que certifiquen su programa de integridad (Ley 27.401)."* Venía en una reforma que se discutía hacía semanas. **Nadie en Atlas la vio venir.**

Traducción: te enteraste tarde, **quedaste afuera de una preselección**, y cuando le pediste al **agente de marketing** un blog para reaccionar, salió sin revisión legal, **sonó a denuncia política y lo tuviste que bajar**. Dos golpes, una sola causa.

Hasta ahora, tu automatización en Paperclip **solo escribe lo que le pedís**: cada pedido es una **task** que marketing lleva por un pipeline, con tu visto bueno al final. Nadie —ni humano ni agente— **vigila el horizonte regulatorio**. Ese es el hueco. **A menos que…**

A menos que la escales. Vas a sumar un **Director de Relaciones Institucionales**: un agente que cada semana vigila el riesgo regulatorio y, cuando algo aparece, le pasa el trabajo —bien encuadrado— al agente de marketing. Lo configurás una vez. Después, vigila solo.

El verdadero premio no es el Director: **sos vos, dominando Paperclip** — orquestando agentes que hacen crecer a Atlas sin sumar cabezas.

> 🔑 **Antes de arrancar — con qué cuenta entrás.** Toda la misión se hace con **`austral-admin@example.com`**, el único usuario humano de Atlas. Con esa cuenta hacés lo estructural —goals, proyectos, contratar al agente— y también el trabajo del día a día: crear los tickets, seguirlos y **aprobar cada compuerta**. No tenés que cambiar de sesión en ningún momento.

> ⚠️ **Al entrar, el navegador te va a decir que el sitio «no es seguro».** Es esperado: esta es la máquina del curso, no un sitio público. Elegí **Avanzado → Continuar al sitio** (el botón cambia de nombre según el navegador) y seguí normal.

---

## 🎯 Lo que vamos a hacer

Escalar esa automatización: que la IA **también vigile el riesgo**, no solo escriba. Son cuatro pasos, y el primero es solo mirar:

0. **Explorar:** recorrés la empresa que ya está corriendo — el organigrama, y las fichas del CMO y el CLO. Así aprendés de qué está hecho un agente antes de crear uno.
1. **A mano:** le pedís al **agente de marketing (CMO)** que reaccione. Funciona, pero el arranque depende de vos: si no te enterás del cambio, no pasa nada — y el CMO encuadra un tema sensible sin mirada legal. Así nació el blog que hubo que bajar.
2. **Automatizado:** sumás un **Director de Relaciones Institucionales** —un agente, con su **goal** y su **proyecto**— y un **heartbeat semanal** que detecta el riesgo y le pasa el trabajo al agente de marketing.
3. **Una corrida:** lo disparás una vez y ves el ciclo completo.

Todo sin código: creás y conectás piezas de Paperclip (agentes, goals, proyectos, tasks, heartbeats).

---

## 🎓 Qué enseña esta misión (conceptos de Paperclip)

| Concepto | Dónde aparece |
|---|---|
| **Anatomía de un agente** (rol, `reportsTo`, `capabilities`, presupuesto) | Paso 0: leés las fichas del CMO y el CLO |
| **Leer un organigrama de agentes** | Paso 0: ubicás quién reporta a quién |
| **Delegar en un agente existente** | Paso 1: le pedís al agente de marketing un blog |
| **El pipeline con compuertas humanas** | El blog fluye CMO → Blog Content Manager → tus aprobaciones |
| **Crear un goal y colgarlo del goal padre** | Paso 2: creás el goal «Anticipación regulatoria» |
| **Crear un proyecto como casa del agente** | Paso 2: creás el proyecto «Radar Regulatorio» |
| **Contratar un agente** (Board Direct Hire) | Paso 2: levantás al Director de Relaciones Institucionales |
| **Escribir las `capabilities` de un agente** | Paso 2: le escribís la rutina del heartbeat y las reglas de delegación |
| **Heartbeats** (corridas autónomas recurrentes) | Paso 2–3: el Director investiga cada semana |
| **Delegación entre agentes vía tasks** | Paso 3: el Director crea una task de blog asignada al CMO |
| **Observar una corrida autónoma** | Paso 3: un ciclo, de punta a punta |

---

## 🧵 Cómo se conecta la historia

Tres piezas enganchan todo — una **escalera de goals** y una **costura**:

![Cómo se conecta la historia: el goal y el proyecto del Director, y la costura hacia Marketing](img/diagrama-conexion.png)

1. **Escalera de goals (el porqué).** El goal nuevo del Director —*Anticipación regulatoria*— es un **sub-goal del goal de compañía** (posicionamiento de marca): los riesgos regulatorios son materia prima para el contenido. Sin esta escalera, el Director sería un agente suelto.
2. **El proyecto como casa (el dónde).** El goal vive en un **proyecto propio, «Radar Regulatorio»**: ahí corre el heartbeat y quedan las notas de riesgo. Es donde el Director *piensa y trabaja*.
3. **La task como costura (el cómo cruza).** Cuando hay riesgo material, el Director **crea una task de blog en el proyecto de marca existente, asignada al CMO**. Ese es el único punto donde los dos dominios se tocan.

**El pago:** el círculo se cierra. Un riesgo entra por el radar del Director → sale como blog publicado en el proyecto de marca —visible en `https://<maquina>/blogs/`— → cumple el goal de compañía.

---

## 🪜 La misión, paso a paso

### Paso 0 — Explorar: mirá lo que ya existe

Antes de crear nada, **entendé la empresa que ya está corriendo**. Son cinco minutos y te ahorran todo el Paso 2: la mejor forma de aprender a crear un agente es leer dos que ya funcionan.

**Hacé esto** — acá solo mirás, no cambiás nada:

1. **Abrí el organigrama (org chart) de Atlas.** Ubicá al **CEO** arriba y de quién cuelga cada uno: **CMO** (marketing), **CLO** (legales), y el **Blog Content Manager** colgando del CMO. Registrá también que **no existe** ningún Director de Relaciones Institucionales — ese es el hueco que vas a llenar vos.
2. **Leé la ficha del CMO y la del CLO, completas.** No te importa tanto *qué dicen* como **de qué partes están hechas**. Mirá las casillas: nombre y título, **`reportsTo`** (de quién depende), el rol / expertise, presupuesto y heartbeat. Después **entrá a la definición del agente y recorré sus solapas**: hay varias, y cada una te muestra una parte distinta del puesto. La que más importa es **Instructions** — ahí está el texto plano de sus **`capabilities`**, que es lo que define cómo se comporta, y es la pieza que más vas a trabajar en el Paso 2. **La ficha es, casilla por casilla, el mismo formulario que vas a completar entonces.**
3. **Mirá el timeline.** Es la historia de la empresa en orden cronológico: cuándo se contrató cada agente, cuándo arrancó cada proyecto, cómo se fue armando Atlas hasta hoy. Te da el "cómo llegamos acá" que el organigrama, que es una foto, no te cuenta.
4. **Abrí el tab de *Activity*.** Acá ves a los agentes **trabajando**: cada corrida, cada task que alguien tomó, cada handoff, cada decisión, con su marca de tiempo. Es la prueba de que esto no es un chatbot esperando que le escribas — hay una empresa moviéndose sola. Prestale atención al **ritmo**: quién se despierta, cada cuánto, y qué deja hecho.
5. **Date una vuelta por lo que ya produjo:** el proyecto **«Aumentar el reconocimiento de marca»** y los blogs ya publicados en `https://<maquina>/blogs/`. Eso es el output que la máquina genera hoy, antes de que vos la toques.

**Qué tenés que notar:** dos cosas. Primero, un agente **no es un prompt suelto**: es un rol con **jefe** (`reportsTo`), un **para qué** (goal), un **dónde** (proyecto), un **comportamiento escrito** (`capabilities`) y un **presupuesto** — el CMO y el CLO son tus dos ejemplos de referencia, y cuando crees al Director vas a llenar esas mismas casillas. Segundo, entre el **timeline** y el **Activity** ya viste el ciclo completo funcionando **sin vos**: eso es exactamente lo que en el Paso 3 vas a ver arrancar desde tu propio agente.

> 🏁 **Éxito:** podés dibujar el organigrama de Atlas de memoria, mirando la ficha del CMO podés enumerar qué hay que definir para dar de alta un agente nuevo, y en el *Activity* podés señalar una corrida concreta que ningún humano pidió.

---

### Paso 1 — La forma manual (la línea de base reactiva)

Te enterás del cambio legislativo y hacés lo obvio: le **pedís al agente de marketing (CMO)** que escriba un blog sobre el tema.

**Hacé esto** — esto es trabajo de tickets:

1. **Abrí el proyecto «Aumentar el reconocimiento de marca»** — el mismo que miraste en el Paso 0. Toda task tiene que colgar de un proyecto: es lo que la liga a un goal. Una task suelta, sin proyecto, Paperclip la rechaza.
2. **Creá la task** (*Create Task*, dentro del proyecto). Estas son las casillas que importan:

   | Casilla | Qué poner |
   |---|---|
   | **Título** | `Blog: reforma de integridad en la cadena de suministro (Ley 27.401)` |
   | **Descripción** | Impacto en proveedores de Vaca Muerta. Enfoque técnico, para ingenieros de perforación y compras. Que salga esta semana. → el tema completo está en *Ejemplo de trabajo*, abajo |
   | **Proyecto** | **«Aumentar el reconocimiento de marca»** — el que abriste en el paso anterior |
   | **Asignado a** | **CMO** (el agente de marketing). **Un solo dueño por task**: no se asigna a un equipo. |
   | **Estado inicial** | `todo` — así queda en la cola que el CMO levanta en su próxima corrida |

3. **Guardate el identificador** que le queda (`ACMA-###`): es con lo que vas a seguir el ticket el resto del paso.
4. **Ahora no la toques.** Dejá que fluya por el pipeline normal: CMO → Blog Content Manager (concept brief → draft) → **tus compuertas de aprobación** → publicación. La gracia es ver quién la levanta, no empujarla vos.

**Dónde lo vas monitoreando** — cuatro lugares, tenelos a mano:

| Dónde mirás | Qué te muestra |
|---|---|
| **La task misma** (`ACMA-###`) | Su **estado** y su **thread**: cada agente que la toca deja escrito qué hizo y qué sigue. Es el registro del trabajo, no un chat. |
| **El proyecto «Aumentar el reconocimiento de marca»** | El árbol de tasks. Si el CMO abre subtareas para el Blog Content Manager, te aparecen colgando de la tuya. |
| **El tab de *Activity*** | El movimiento en vivo — el mismo que miraste en el Paso 0, ahora con tu ticket adentro: cuándo el CMO lo toma, el handoff al Blog Content Manager, cada decisión con su marca de tiempo. |
| **`https://<maquina>/blogs/`** | El resultado, una vez que aprobás la última compuerta. |

**El recorrido de estados**, para saber qué estás mirando:

`todo` → *(el CMO lo toma en su corrida)* `in_progress` → `in_review` **← acá frena y te espera** → `done` → blog publicado.

Cada `in_review` es una **compuerta humana**: nada avanza hasta que vos aprobás o rechazás. Vas a pasar por más de una (concept brief, draft, publicación).

> ⏱️ **Paciencia con los tiempos.** El CMO levanta la cola en su **heartbeat**, no en el instante en que guardás la task: puede pasar un rato hasta que el estado se mueva de `todo`. Si nunca arranca, revisá dos cosas — que el **asignado** sea el CMO, y que la task esté **dentro del proyecto** de marca.

> 🌐 **Dónde se publica.** Una vez aprobado, el blog queda publicado en **`https://<maquina>/blogs/`** — reemplazá `<maquina>` por la dirección de tu instancia de Paperclip. Ahí es donde vas a ver el resultado final del pipeline, y es el mismo lugar donde aparecerá el blog que dispare el Director en el Paso 3.

**Qué tenés que notar:** funciona, pero es *reactivo, frágil y encima riesgoso*. Pasó solo porque **vos** detectaste el cambio y lo pediste. Nadie vigila el horizonte de forma sistemática; el encuadre de un tema sensible quedó **improvisado por Marketing**, que no tiene la expertise regulatoria ni la conciencia del riesgo reputacional; y no hubo evaluación de riesgo ni chequeo legal antes de escribir. En un tema de **corrupción / transparencia**, improvisar así es peligroso — es, palabra por palabra, cómo nació el blog que hubo que bajar el trimestre pasado. **Esa es la limitación que arregla el Paso 2.**

> 🏁 **Éxito:** un blog sobre el tema legislativo llega al menos a la compuerta del concept brief, y podés explicar *por qué* hacerlo a mano no escala (y por qué es riesgoso).

![Reactivo (Paso 1) vs. proactivo (Paso 2–3): mismo pipeline, distinta forma de disparar el trabajo](img/diagrama-reactivo-vs-proactivo.png)

*El Paso 1 funciona, pero depende de vos y no tiene dueño. El Paso 2 le pone un agente, un goal y un proyecto detrás.*

---

### Paso 2 — Crear al vigía: el Director de Relaciones Institucionales

En lugar de pedir blogs uno por uno, **contratás al agente cuyo trabajo es verlos venir** — y le das un **goal** y un **proyecto** propios para que la historia quede conectada (ver *Cómo se conecta la historia*).

**Hacé esto** — seguís con la misma cuenta: crear agentes es facultad del board, y `austral-admin` la tiene.
1. **Creá el goal** del Director: *«Anticipación regulatoria»*. En el campo **parent** elegí el **goal de compañía**: todo goal nuevo tiene que colgar de un padre, si no queda suelto (los riesgos regulatorios son materia prima del contenido de marca).
2. **Creá el proyecto** *«Radar Regulatorio»*, propiedad del Director: es la casa del heartbeat y de las notas de riesgo.
3. **Contratá el agente** con la definición de rol existente (abajo). Como entrás como **board** (la cuenta admin), es contratación directa (**Board Direct Hire**): no hace falta approval. Confirmá que reporta al **CEO**, junto al CMO y el CLO.
4. **Escribí sus `capabilities` / instrucciones** con la rutina del heartbeat y las reglas de delegación (abajo) — el detalle nuevo de "qué tiene que hacer".

#### 2a. Definición de rol base (la existente — pegar tal cual)

> **Director de Relaciones Institucionales** — Asuntos gubernamentales en el sector de petróleo y gas de Argentina: monitoreo regulatorio, vínculo con actores clave (stakeholders) y posicionamiento institucional ante organismos de gobierno y cámaras del sector.

#### 2b. Sus instrucciones / `capabilities` (el detalle nuevo)

> **Heartbeat semanal — Barrido de riesgo regulatorio.** Cada semana, de forma automática:
> 1. **Investigá** los desarrollos regulatorios y legislativos —vigentes y en trámite— relevantes para el negocio de Atlas: actividad de perforación en Vaca Muerta, régimen de hidrocarburos y RIGI, normativa provincial (Neuquén / Río Negro), regulación ambiental / de emisiones, estándares de certificación técnica (IRAM / API / ISO) e **integridad y transparencia en la cadena de suministro**.
> 2. **Evaluá la materialidad** de cada uno: ¿un cambio propuesto o sancionado **impacta los intereses comerciales de Atlas o la actividad de perforación de sus clientes** —como riesgo *o* como oportunidad—? Asignale un nivel (bajo / medio / alto) con una línea de justificación.
> 3. **Si hay algo material:** creá una **task «nota de riesgo»** en el proyecto *Radar Regulatorio* y **proponé un blog** creando una **task en el proyecto «Aumentar el reconocimiento de marca», asignada al CMO**, con un brief acotado (plantilla abajo). En temas de **alta sensibilidad** (corrupción/transparencia), la revisión del **CLO es obligatoria** antes de que el blog avance; en baja/media, opcional.
> 4. **Si no hay nada material esta semana:** dejá una **task visible de "sin acción"** y cerrá la corrida.
>
> **Barreras (guardrails):** el contenido es *técnico y factual*, nunca militancia partidaria ni lobby, y **no acusa a personas ni empresas puntuales**; posiciona a Atlas como autoridad técnica y de cumplimiento (consistente con el objetivo SEO de marca); la **aprobación humana** sigue siendo la compuerta final; el Director **propone y arma el brief**, no escribe ni publica el blog.

#### 2c. Plantilla de brief del blog (lo que el Director pone en la descripción de la task)

- **Título tentativo**
- **Por qué ahora** — el cambio regulatorio y su estado
- **Impacto en Atlas** — interés comercial / clientes / ángulo Vaca Muerta
- **Ángulo editorial recomendado** — técnico, no partidario
- **Puntos clave a cubrir**
- **Audiencia objetivo** — ingenieros de perforación, compras, operadores
- **Sensibilidad / urgencia** — y si requiere revisión del CLO

> 🏁 **Éxito:** existen el **goal** «Anticipación regulatoria» (colgado del goal de compañía) y el **proyecto** «Radar Regulatorio»; el Director está en el organigrama (Board Direct Hire) y reporta al CEO; y sus `capabilities` incluyen el heartbeat semanal, el test de materialidad y la regla de "crear una task para el CMO en el proyecto de marca".

---

### Paso 3 — Correr un ciclo y verlo funcionar

Disparás una única corrida del heartbeat y seguís la cadena.

**Hacé esto:**
1. Dispará una corrida del heartbeat del Director a mano (**Run heartbeat now** / on-demand).
2. Miralo en el **tab de *Activity*** y en el **timeline** —las mismas vistas del Paso 0, ahora con tu agente adentro—: **investiga → encuentra el riesgo legislativo → crea la task «nota de riesgo» en Radar → crea la task de blog en el proyecto de marca, asignada al CMO.**
3. Dejá que el CMO tome la task y arranque el pipeline normal (concept brief → draft), y **aprobá las compuertas**. Una vez aprobado, **abrí `https://<maquina>/blogs/` para ver el blog publicado**.

> 🏁 **Éxito:** un solo heartbeat produjo (a) una task «nota de riesgo» y (b) una **task de blog en el proyecto de marca, a cargo del CMO**, y el blog entró al pipeline — **sin ningún pedido manual de tu parte.** El flujo reactivo del Paso 1 ahora es proactivo y lo posee el agente correcto.

---

## 📄 Ejemplo de trabajo (el tema legislativo)

*Podés cambiarlo por el tema que prefieras.*

> **Proyecto de reforma de integridad y transparencia en la cadena de suministro de hidrocarburos.** Exigiría a los proveedores que contratan con operadores ligados al Estado (como YPF) declarar **beneficiarios finales**, adoptar **programas de integridad** (en línea con la Ley 27.401 de responsabilidad penal empresaria) y certificar cumplimiento para poder facturar en Vaca Muerta. Es **sensible**: toca corrupción y transparencia, un terreno políticamente cargado. Y es **directamente material** para Atlas: sus programas de compliance y su trazabilidad se vuelven una ventaja de acceso, pero el tema debe tratarse como una historia de **estándares e integridad** —qué necesita saber un proveedor, cómo cumple Atlas— y **nunca** como una denuncia ni una toma de posición política. Exactamente el tipo de encuadre que corresponde a Relaciones Institucionales, no a una improvisación de Marketing.

**Temas alternativos** por si preferís:
- Un cambio al **RIGI** (régimen de incentivo a grandes inversiones) que afecte el capex y la demanda de perforación en Vaca Muerta.
- Nueva regulación de **metano / venteo y quema** que suba las exigencias de cumplimiento a los operadores.
- Reforma de **certificación técnica obligatoria** (IRAM / API / ISO) para insumos de perforación.

---

## 🪞 Reflexión final (para el participante)

Cerrá la misión respondiendo estas tres preguntas — son el verdadero aprendizaje:

1. **De reactivo a proactivo.** ¿Qué tarea de tu trabajo real hoy es *reactiva* —depende de que alguien la detecte y la pida— y podría convertirse en un agente con *heartbeat* que la vigile solo? ¿Qué tendría que investigar en cada corrida?
2. **El rol que falta.** En tu organización, ¿qué expertise termina hoy "improvisada" por el equipo equivocado —como Marketing encuadrando un tema regulatorio sin conciencia del riesgo—? ¿Qué agente (o persona) debería ser dueño de eso, y qué barreras le pondrías?
3. **Delegación con compuertas.** Ver a un agente delegar en otro (Director → CMO) sin que intervengas, ¿qué te sugiere para tu trabajo? ¿Dónde una cadena así de traspasos automáticos te ahorraría tiempo — y dónde querrías mantener, sí o sí, una **compuerta humana** antes de publicar o ejecutar?

---

## 🧭 Decisiones tomadas

- **Cadencia:** heartbeat **semanal**; una semana sin riesgo material igual deja una **task de "sin acción"** visible (para ver el caso negativo).
- **CLO:** en temas de **alta sensibilidad** (corrupción/transparencia), la revisión del **CLO es obligatoria** antes de pasar el blog al CMO; en baja/media, opcional.
- **Handoff:** el Director **asigna la task directo al CMO** (asignación entre pares, permitida por la doc).

El detalle de implementación en Paperclip está en `mission-res.md` (verificado contra la documentación oficial). **La misión está lista para correr.**
