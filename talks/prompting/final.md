---
presentation: Inteligencia Artificial Generativa (AI Gen)
class: "Trabajar con LLMs: prompts, costos y producción"
research: research/corpus/
description: Slides are grouped into Sections. Each Section contains one or more Slides.
presenter: Paulo Veiga, Claudio Righetti, Marco Sorondo (Universidad Austral)
audience: Estudiantes de grado de Ingeniería de Software con base técnica fuerte
duration: 150 min (clase de 2:30 h)
date: 2026-09-02
---

# Thesis

**Claim:** El LLM completa tokens de izquierda a derecha y no tiene un motor de razonamiento aparte, así que toda técnica de prompting que funciona lo hace por la misma razón: obliga al modelo a escribir los pasos intermedios, y esos pasos escritos son el cómputo.

**Why it matters:** Cada punto de calidad se paga en tokens, en latencia y en dinero, así que la habilidad central de la clase es emparejar la técnica y el modelo con la dificultad real de la tarea.

- [closed] 2026-08-14 — "Restaurado 1:1 desde `AIG4B-Clase-3-Prompting.pptx`. La tesis no estaba explícita en el deck original: falta escribirla."
  Resolution: tesis escrita a partir del argumento de la slide 38 del deck original ("El LLM no 'piensa': predice tokens", corpus §Raw excerpts [38]), con el trade-off calidad/costo como *why it matters*. Los objetivos de las ocho secciones se derivaron de ella.

---

# Agenda

**Narrative arc:**

La clase abre por la máquina: qué entra en la ventana de contexto, qué cuesta cada token y por qué el modelo inventa cuando se queda sin patrón. De ahí pasa a las decisiones que tienen precio (qué modelo, qué caching, qué cascada) y después al oficio de escribir el prompt: anatomía, ejemplos y encadenamiento del razonamiento. El bloque de técnicas avanzadas termina explicando por qué funcionan, que es la tesis de la clase. Las dos últimas secciones bajan todo al ciclo de vida de un producto de software y dejan la práctica como trabajo domiciliario.

**Sections (in delivery order):**

- 1. Fundamentos
- 2. Modelos y costos
- 3. Prompts estructurados
- 4. In-context learning
- 5. Prompting avanzado
- 6. Effort y thinking
- 7. LLMs en ingeniería
- 8. Resumen y práctica

<!-- Agenda tal como figuraba en el deck original (registro histórico, no se entrega así). -->
<!-- Difería del orden real de entrega, prometía TOON (ninguna slide lo cubre) y un -->
<!-- "sistema de triage con LLM" que la slide de práctica no entrega. Ver corpus -->
<!-- AIG4B-Clase-3-Prompting.md.md, Inconsistencias 15 y 16. -->
<!-- **1** Fundamentos de Foundational Models — Ventana de contexto, tokens, limitaciones y modelos mentales -->
<!-- **2** Ingeniería de Prompts Estructurada — 6 componentes, XML tags, salidas JSON y optimización por modelo -->
<!-- **3** In-Context Learning — Zero-shot, Few-shot y Many-shot con ejemplos clínicos -->
<!-- **4** Técnicas Avanzadas de Prompting — CoT, Self-Consistency, Extended Thinking y Prompt Chaining -->
<!-- **5** Selección de Modelos y Costos — Framework de decisión, prompt caching, model cascading y TOON -->
<!-- **6** Foundational Models en Medicina — Aplicaciones reales, recorrido del paciente, research biomédica y marco ético OMS -->
<!-- **7** Resumen y Práctica — Módulos interactivos de aitutorial.dev + sistema de triage con LLM -->

- [closed] 2026-08-28 — "Las siete agendas in-deck declaran un orden distinto al de entrega, prometen TOON y un sistema de triage que el deck no da."
  Resolution: las siete agendas repetidas (0.4, 1.13, 2.8, 3.6, 4.5, 5.21, 6.7) se alinearon al orden real de entrega, se les quitaron los ordinales escritos (L3), se sacaron las promesas de TOON y del sistema de triage, y cada una marca en negrita la sección en curso para que la repetición sirva de navegación.

---

# 0. Portada

**Goal of this section:** Abrir la clase: portada, encuadre y el mapa de las siete secciones.

---

## 1. Trabajar con LLMs

### Content

**Inteligencia Artificial Generativa (AI Gen) · Clase 5**

- **Prompts, costos y producción**
- **Paulo Veiga, Claudio Righetti y Marco Sorondo (Universidad Austral)**
- **Última modificación: agosto 2026**

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 1)

### Speaker notes

Portada. Presentate y presentá a los otros dos docentes. Encuadre de una frase antes de arrancar: esta clase no es un catálogo de trucos de prompting, es la clase donde se entiende qué hace el modelo por dentro cuando lo promptean, y por qué cada mejora de calidad tiene un precio en tokens y en latencia. Avisá acá que la clase dura dos horas y media y que los módulos de práctica de aitutorial.dev quedan como trabajo domiciliario.

---

# 1. Fundamentos

**Goal of this section:** Dejar instalado un modelo mental correcto de qué es un LLM por dentro: una ventana de contexto finita que se factura por token y un motor de completado que inventa cuando se queda sin patrón.

---

## 1. ¿Qué es un prompt?

### Content

- **Un prompt es la instrucción, pregunta o entrada textual que se le da a un modelo de lenguaje grande (LLM) para que genere una respuesta.**

| Medio de comunicación | Define tarea y contexto | Calidad = resultado |
|---|---|---|
| La interfaz principal entre la persona y el modelo. | Establece qué hacer y bajo qué condiciones. | Un prompt mejor produce respuestas más útiles y precisas. |

- **💡 Un prompt se parece a un ticket bien escrito: cuanto más claro el enunciado y las condiciones de aceptación, menos vueltas da quien lo resuelve.**

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 5)

### Speaker notes

Arranque suave, pero conviene no darlo por sabido. El punto que sí hay que dejar clavado es el tercero: la calidad del prompt no es cortesía, es la única palanca de control que queda una vez elegido el modelo. La analogía del ticket funciona mejor que la de la receta para esta audiencia: todos escribieron alguna vez un issue de dos líneas y recibieron una implementación que no era la que querían. El prompt tiene el mismo problema y la misma solución.

---

## 2. ¿Qué se guarda en un prompt?

### Content

**Todo lo que el modelo ve en un turno vive en la ventana de contexto, y todo compite por su atención al mismo tiempo.**

![Ventana contexto contenedor](images/s1-2-1-ventana-contexto-contenedor.svg)
<!-- ascii-source:
  +===================== VENTANA DE CONTEXTO =====================+
  |                                                 (limite duro) |
  |   +--------------------------------------------------------+  |
  |   | SYSTEM PROMPT      instrucciones base, fijas            |  |
  |   +--------------------------------------------------------+  |
  |   | HISTORIAL          todos los turnos previos             |  |
  |   |                    crece en cada mensaje  >>>>          |  |
  |   +--------------------------------------------------------+  |
  |   | DATOS INYECTADOS   archivos, busquedas, APIs            |  |
  |   +--------------------------------------------------------+  |
  |   | RESPUESTAS         las salidas previas del modelo       |  |
  |   +--------------------------------------------------------+  |
  |                                                               |
  |        todo compite por la atencion, al mismo tiempo          |
  +===============================================================+
                              |
                    se llena  v
              se pierde el acceso a lo mas viejo
-->
<!-- ascii-note:
intent: mostrar la ventana de contexto como un contenedor finito con cuatro tipos de contenido apilados adentro, y su borde como limite duro que se desborda
emphasize: el marco exterior como limite duro; la banda HISTORIAL, unica que crece sola en cada turno; la flecha de desborde al pie
labels: "VENTANA DE CONTEXTO (limite duro)", "SYSTEM PROMPT", "HISTORIAL", "DATOS INYECTADOS", "RESPUESTAS", "todo compite por la atencion, al mismo tiempo", "se pierde el acceso a lo mas viejo"
-->

- ⚠️ Más contexto no es mejor contexto: el modelo no elige qué leer, procesa todo junto y lo importante se diluye.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 6)

### Speaker notes

Recorré el contenedor banda por banda, porque las definiciones ya no están en la lámina. **System prompt**: las instrucciones base que fijan el comportamiento general del modelo, fijas entre turnos. **Historial**: toda la conversación previa; cada mensaje nuevo se concatena y ocupa lugar de forma acumulativa. **Datos inyectados**: archivos, resultados de búsqueda, respuestas de APIs externas. **Respuestas del modelo**: sus propias salidas previas, que también ocupan lugar. Cuatro cosas entran en la ventana y solo una la escribe el usuario en ese momento. Es la slide donde conviene romper la ilusión de que "el chat se acuerda": no se acuerda, la aplicación le reenvía todo el historial en cada turno. De ahí salen dos consecuencias que se cobran más adelante en la clase. La primera es de plata: el historial se paga entero, otra vez, en cada mensaje (la slide de la fórmula del costo lo cuantifica). La segunda es de calidad: el modelo reparte atención sobre todo lo que entra, así que meter más contexto puede empeorar la respuesta en lugar de mejorarla. Si el grupo pregunta por qué, adelantá el sesgo de recencia de la slide de limitaciones: el modelo mira más el principio y el final del prompt que el medio.

---

## 3. Ventana de contexto

### Content

- **La ventana de contexto es la memoria de trabajo activa del modelo. Contiene todo lo que puede ver en un momento dado para generar la respuesta: system prompt, historial, datos inyectados y sus propias respuestas.**
- **Es finita. Cuando se llena, el modelo pierde acceso a lo más viejo.**

**Tamaños en 2026**

![Escala ventanas modelos](images/s1-3-1-escala-ventanas-modelos.svg)
<!-- ascii-source:
  Escala relativa de la ventana de contexto   (1M = 10 unidades)

  Haiku 4.5          200K   ##
  Opus 5 / Opus 4.8  1M     ##########
  Sonnet 5 / 4.6     1M     ##########
  GPT-5.4            1M     ##########
  Gemini 3 Pro       2M     ####################
  Llama 4            10M    ##################################### ->

  Anthropic: verificado (2026-06-24)  |  resto: sin verificar
-->
<!-- ascii-note:
intent: comparar por magnitud, de un vistazo, lo que una tabla de cifras no transmite; la barra de 10M se corta al borde porque a escala real no entra en el lienzo
emphasize: el salto de 200K a 1M, y que 1M es hoy la meseta comun de casi todos los modelos; la barra truncada de Llama 4 con su flecha de continuidad
labels: nombre del modelo a la izquierda, cifra de ventana en el medio, barra proporcional a la derecha, y el pie que separa lo verificado de lo no verificado
-->

- La carrera por ventanas más largas es la frontera competitiva del momento.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 7)
- Ventanas de los modelos Anthropic verificadas contra el catálogo vigente de la API de Claude (corte 2026-06-24).

### Speaker notes

La definición primero y la tabla después: la ventana es memoria de trabajo, no memoria a largo plazo. La analogía útil acá es la RAM contra el disco. Nada de lo que está en la ventana persiste entre sesiones, y nada de lo que quedó afuera existe para el modelo. Sobre la tabla: la fila de Anthropic está verificada contra el catálogo vigente de la API; las tres filas de otros proveedores vienen del deck original y no las pude verificar, así que decilas como orden de magnitud y no como dato preciso. El punto pedagógico está en otro lado: un millón de tokens ya dejó de ser una restricción práctica para casi todo trabajo de software, y que el cuello de botella se mudó del tamaño de la ventana al costo de llenarla.

---

## 4. ¿Cuánto es 1 millón de ~~Tolkien~~ tokens?

<!-- El tachado de "Tolkien" es deliberado: es el chiste de la lamina. NO corregir como errata. -->

<!-- design: column-right -->

### Content

![Gandalf, de El Señor de los Anillos](images/slide-08-1.jpg)

- **"Claude Code tiene ahora una ventana de contexto de 1 millón de tokens por defecto. Un millón de tokens es mucho: la trilogía de El Señor de los Anillos más El Hobbit tienen unas 576.000 palabras, lo que equivale a ~750.000 tokens. Las cuatro obras caben en un único prompt... y aún sobra espacio."**

| 📚 ~750K tokens | 💾 ¿Y un repositorio con código? |
|---|---|
| Toda la obra de Tolkien: El Hobbit más la trilogía de El Señor de los Anillos. | El código, los tests y la documentación de un servicio de tamaño medio entran cómodos. La cuenta exacta depende del repo. |

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 8) — cita verbatim en §Raw excerpts [8]. El deck original no atribuye la cita a un autor ni a una publicación.

### Speaker notes

Esta es la slide del "ah, mirá". Sirve para que la cifra deje de ser abstracta: 576.000 palabras de Tolkien son unos 750.000 tokens, y todavía sobran 250.000. La segunda columna es la traducción al mundo de ellos, y conviene decirla con honestidad: no tengo una medición del repo, tengo un orden de magnitud. Si querés hacerlo vivo, pediles que estimen cuántos tokens tiene el repositorio del trabajo práctico y después lo miden con el tokenizador en la slide siguiente. Aviso de derechos, por si el material se republica: el fotograma de Gandalf es de la película y el deck original no lo acredita.

---

## 5. Cómo se tokeniza

<!-- design: split-left -->

### Content

**Antes de llegar al modelo, todo texto se parte en piezas de un vocabulario fijo. Ese vocabulario es lo que decide cuántos tokens cuesta una frase, y cada familia de modelos tiene el suyo.**

| Encoding de `tiktoken` (OpenAI) | Vocabulario | Modelos que lo usan |
|---|---|---|
| `r50k_base` (gpt2) | 50.257 | GPT-2 y los primeros GPT-3 |
| `p50k_base` | 50.281 | Codex, text-davinci-002/003 |
| `cl100k_base` | 100.257 | GPT-3.5-turbo, GPT-4, embeddings v2/v3 |
| `o200k_base` | 199.999 | GPT-4o y la serie o |
| `o200k_harmony` | 201.087 | variante del anterior, formato *harmony* |

- **BPE — *byte pair encoding*** Arranca de caracteres sueltos y fusiona los pares más frecuentes hasta llenar el vocabulario. Por eso lo común es un token y lo raro se parte en pedazos.
- **Vocabulario creciente** De cincuenta mil entradas a doscientas mil. Uno más grande corta menos: el mismo texto rinde menos tokens.

### Sources

- Vocabularios verificados contra el código fuente de `tiktoken` (`tiktoken_ext/openai_public.py`, consultado el 2026-09-01): `r50k_base` 50.257, `p50k_base` 50.281, `cl100k_base` 100.257, `o200k_base` 199.999, `o200k_harmony` 201.087. **El archivo no mapea encodings a modelos**: esa columna viene de la documentación de OpenAI y de fuentes secundarias, no del código.
- Catálogo vigente de la API de Claude: el conteo de tokens para modelos Claude se hace con el endpoint `count_tokens`, no con tokenizadores de otros proveedores.
- `gpt-tokenizer.web.md` — el playground interactivo, para verlo en vivo.

### Speaker notes

---

## 6. Economía de tokens

### Content

**Los tokens son subpalabras, no palabras completas. El modelo procesa y factura en tokens, tanto los de entrada como los de salida.**

- "Ingeniería de Software" no cuenta como dos palabras: el tokenizador la parte en varios trozos, y la cuenta exacta cambia según el modelo.
- Un prompt de 2.000 tokens de entrada más una respuesta de 500 de salida cuesta unos **$0,014** con Claude Sonnet 4.6.

<!-- enlace de la forma: https://gpt-tokenizer.dev -->
- [Probarlo en tiempo real: gpt-tokenizer.dev](https://gpt-tokenizer.dev)

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 9)
- `gpt-tokenizer.web.md` — tokenizador interactivo, para verificar el corte en subpalabras en vivo.
- Derivación del costo: $0,0135 = (2.000 / 1.000.000 × $3) + (500 / 1.000.000 × $15), con la tarifa vigente de Claude Sonnet 4.6 ($3 / $15 por MTok). Redondeado a $0,014.

### Speaker notes

Momento de abrir gpt-tokenizer.dev en vivo y pegar una línea de código. El efecto es inmediato: un identificador en camelCase se parte en cuatro o cinco tokens, y un bloque de JSON con indentación se come muchísimos más de los que cualquiera estimaría a ojo. Ese es el punto: la intuición de "una palabra, un token" está mal, y está mal justo en la dirección que más importa, porque el código y el JSON tokenizan peor que la prosa. El costo de $0,014 parece nada, y lo es hasta que se multiplica por diez mil llamadas diarias. Guardá esa multiplicación para la slide siguiente, que es donde el número empieza a doler.

---

## 7. La fórmula del costo

### Content

**Costo total = (tokens de entrada × precio de entrada) + (tokens de salida × precio de salida)**

![Lo que el usuario escribe no crece; lo que la app le manda al modelo sí, porque reenvía toda la conversación anterior](images/s1-7-1-costo-crece-reenvio.svg)
<!-- ascii-source:
  LO QUE EL USUARIO ESCRIBE          LO QUE LA APP LE MANDA AL MODELO
  (siempre parecido)                 (crece en cada turno)

  turno 1   [M1]                     [M1]                          1 bloque
  turno 2   [M2]                     [M1][R1][M2]                  3
  turno 3   [M3]                     [M1][R1][M2][R2][M3]          5
  turno 4   [M4]                     [M1][R1][M2][R2][M3][R3][M4]  7
                                      \____________________/  \__/
                                       ya se pago 3 veces     lo nuevo

  M = mensaje del usuario     R = respuesta del modelo

  El usuario escribe lo mismo en cada turno. La cuenta crece igual,
  porque cada llamada reenvia toda la conversacion anterior.
-->
<!-- ascii-note:
intent: mostrar la desproporcion entre lo que el usuario escribe (constante) y lo que la aplicacion manda al modelo (crece en cada turno); que el crecimiento no viene del usuario sino del reenvio del historial
emphasize: las dos columnas contrastadas, la izquierda que no crece y la derecha que si; la llave que separa lo ya pagado varias veces de lo nuevo del turno; la linea de cierre
labels: "LO QUE EL USUARIO ESCRIBE (siempre parecido)", "LO QUE LA APP LE MANDA AL MODELO (crece en cada turno)", "turno 1..4", "M = mensaje del usuario", "R = respuesta del modelo", "ya se pago 3 veces", "lo nuevo"
-->


- 💡 **¿Por qué no explota el consumo?** Para que el modelo mantenga el contexto, la aplicación le reenvía toda la conversación previa en cada turno: el modelo no recuerda nada entre llamadas, así que cada turno vuelve a leer todo desde cero. Con esa aritmética un chat largo debería costar una fortuna. No la cuesta, y la razón es lo que viene.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 10)

### Speaker notes

Esta es la slide que explica por qué la factura de un chatbot crece sin que crezca el uso. La fórmula tiene dos términos y el interesante es el primero: los tokens de entrada de un turno incluyen todo lo anterior. Un chat de veinte turnos paga el turno uno veinte veces. Señalá la tabla de izquierda a derecha una fila por vez y dejá que la tercera columna hable sola. Acá conviene sembrar dos cosas que se cobran después en la clase: prompt caching existe justo para atacar este crecimiento, y las técnicas avanzadas de la sección cinco compran calidad gastando tokens de salida, que son los caros. Si alguien pregunta por qué la salida cuesta cinco veces más que la entrada, la respuesta corta es que se genera token por token y no se paraleliza como la lectura del prompt.

---

## 8. Cómo funciona el caching

### Content

**El proveedor no guarda respuestas: guarda el estado ya calculado de un prefijo de tokens. De ahí sale la regla única que gobierna todo — coincidencia por prefijo — y también la facilidad con la que se rompe.**

- **Coincide por prefijo, no por contenido** No es "¿ya vi este texto antes?". El proveedor guarda el cómputo de los primeros N tokens del pedido; si esos N coinciden byte a byte con los de la llamada anterior, se reutilizan en vez de recalcularse.
- **Un byte distinto invalida todo lo que sigue** Y el orden del pedido es fijo: primero las herramientas, después el system prompt, después los mensajes. Por eso lo estable va adelante y lo que cambia en cada llamada va al final.
- **Hay un mínimo, y falla en silencio** Un prefijo por debajo del mínimo del modelo no se cachea: sin error, sin aviso. Un prompt corto puede estar marcado para cachear y no cachear nunca.
- **Se verifica en la respuesta** El contador de tokens leídos del caché dice si funcionó. Si da cero en llamadas repetidas, hay un invalidador escondido: una fecha en el system prompt, un JSON sin ordenar, una lista de herramientas que cambia de orden.

- 🎯 **Por qué encaja acá.** La bola de nieve de la lámina anterior es un prefijo que crece: cada turno agrega al final y deja intacto lo de antes. El caso ideal para el caching.

### Sources

- Catálogo vigente de la API de Claude (corte 2026-06-24): el caching es coincidencia por prefijo; cualquier cambio de byte en el prefijo invalida lo que sigue; el orden de armado es herramientas → system → mensajes; el prefijo mínimo cacheable depende del modelo y por debajo de ese umbral no cachea sin emitir error; el contador de tokens leídos del caché es la forma de verificarlo.

### Speaker notes

Esta lámina existe para que el caching no se lea como magia cuando lleguen a la sección de costos. La idea que tienen que llevarse es una sola: no se cachean respuestas, se cachea el cómputo de un prefijo. Y de ahí sale todo lo demás por deducción, así que en vez de enumerar reglas, deducilas en voz alta con ellos. Si lo que se guarda es el prefijo, entonces lo estable tiene que ir adelante — obvio. Si un byte cambia, todo lo que viene después se recalcula — también obvio. Los dos puntos que más les van a servir en la práctica son los dos últimos, porque fallan en silencio. Un prompt corto marcado para cachear puede no cachear nunca, y nadie te avisa. Y el invalidador clásico es meter la fecha y hora en el system prompt: cambia en cada llamada, está al principio, y tira abajo el caché entero. Por eso se verifica mirando el contador de tokens leídos del caché en la respuesta: si da cero en llamadas repetidas, hay un invalidador escondido. Cerrá conectando con la lámina anterior: la conversación que crece es un prefijo que crece, y por eso es el caso ideal.

---

## 9. Del chat al caché programático
### Content

**En un chat el prefijo crece solo: cada turno agrega al final y deja intacto todo lo anterior. En una aplicación no hay esa suerte — el pedido lo armás vos, y sos vos quien decide dónde corta la frontera entre lo que se reutiliza y lo que cambia.**

![Caching prefijo sufijo](images/s1-9-1-caching-prefijo-sufijo.svg)
<!-- ascii-source:
  UN REQUEST  =  PREFIJO ESTATICO  +  SUFIJO DINAMICO

  |<----------- se cachea: 10% del precio -----------&gt;|<-- precio lleno --&gt;|
  +---------------------------------------------------+--------------------+
  | system prompt | guia de estilo | ADRs | base cod.  | el diff del user   |
  +---------------------------------------------------+--------------------+
   50.000 tokens, identicos en cada llamada             100 tokens, cambian
                                                     ^
                                                     |
                                    [ cache_control ] marca el corte

  Request 1    MISS  ->  se procesa entero y se guarda el prefijo
  Request 2+   HIT   ->  se reutiliza el prefijo y se cobra al 10%

  !!  un byte distinto en CUALQUIER punto del prefijo  ->  hit rate 0
      y no hay ningun error: solo una factura mas alta
-->
<!-- ascii-note:
intent: mostrar que el caching hace match por PREFIJO, no por contenido: la frontera entre lo estatico y lo dinamico es lo que decide si hay hit, y por eso el orden dentro del prompt es load-bearing
emphasize: la linea divisoria entre prefijo y sufijo con la marca [ cache_control ]; la desproporcion 50.000 contra 100 tokens; la advertencia final del fallo silencioso
labels: "PREFIJO ESTATICO", "SUFIJO DINAMICO", "se cachea: 10% del precio", "precio lleno", "cache_control", "MISS", "HIT", "hit rate 0"
-->

- **Monitorear el hit rate** Si `cache_read_input_tokens` da cero, algo está invalidando el prefijo en silencio.

**El caso típico de un equipo de software:** la guía de estilo, las decisiones de arquitectura ya documentadas —los *ADR*— y el fragmento de base de código que el asistente necesita son idénticos en cada consulta; el pedido del usuario son doscientos tokens. Ese reparto es el que el caching premia, y `cache_control` es la marca que dice dónde termina uno y empieza el otro.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 46)
- Precio del cache hit (10% de la entrada) verificado contra el catálogo vigente de la API de Claude.

### Speaker notes

Esta es la lámina que cierra el puente, y conviene abrirla con una pregunta: cuando chatean con un asistente, ¿quién marca el corte? Nadie: el prefijo crece solo porque cada turno se agrega al final, y el proveedor lo aprovecha sin que ellos hagan nada. En una aplicación propia eso no pasa, porque el pedido lo arman ellos en cada llamada, y por eso hay que marcar el corte a mano. Ahí entra `cache_control`. Caminá el diagrama señalando las tres decisiones que se deducen del match por prefijo: cachear lo estático — base de conocimiento, system prompt, documentación de arquitectura, guía de estilo—, no cachear el input del usuario porque rompe el prefijo, y poner primero lo cacheable. La advertencia del pie es la que más les va a servir: si el system prompt lleva un `datetime.now()` adentro, el prefijo cambia en cada llamada y el hit rate es cero sin que nadie se entere, porque no hay error, solo una factura más alta. El caso del equipo de software es el ideal y vale decirlo: cincuenta mil tokens idénticos contra doscientos que cambian. Los números del ahorro los ven en la sección de costos; acá el foco es el mecanismo y quién marca el corte.

---

## 10. Prompt caching: implementación

### Content

**El caching se activa marcando las partes estáticas del prompt con un bloque `cache_control`.**

<!-- ascii-render: documentation-only -->
```python
import anthropic
client = anthropic.Anthropic()

# ESTATICO -- se cachea (50K tokens)
system_prompt = """Sos un revisor de codigo senior.
Guia de estilo, ADRs y convenciones: [... 50K ...]"""

response = client.messages.create(
    model="claude-sonnet-5",
    system=[{"type": "text", "text": system_prompt,
             "cache_control": {"type": "ephemeral"}}],
    # DINAMICO -- cambia en cada request
    messages=[{"role": "user",
               "content": "Revisa este diff: [... 100 ...]"}])

# Request 1     cache MISS  ->  se procesa y se guarda
# Request 2+    cache HIT   ->  se cobra al 10%
```

- **Parte estática (cacheable)** System prompt, guía de estilo, decisiones de arquitectura, base de conocimiento. Se marca con `cache_control`.
- **Parte dinámica (no cacheable)** El diff, el ticket, la consulta puntual. Cambia en cada request, así que va después del corte.
- **Hit de caché** Si el prefijo ya fue procesado, el proveedor lo reutiliza en vez de recalcularlo.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 47)
- Derivación del ejemplo: 50.000 tokens a $3/MTok = $0,15 sin caché; con hit, 10% = $0,015.

### Speaker notes

Veinte líneas de código y una sola idea: la frontera entre lo que se cachea y lo que no la dibuja el programador, poniendo `cache_control` en el bloque correcto. Señalá el orden. Lo estático arriba, lo dinámico abajo, siempre, porque el match es por prefijo. Si alguien pone el diff arriba del system prompt, el caché no sirve para nada y no hay ningún error que lo avise. El ejemplo pasó de un system prompt de guías clínicas a la guía de estilo y los ADRs del repo, que es el caso real de un asistente de revisión de código: cincuenta mil tokens de convenciones que no cambian, cien tokens de diff que cambian siempre.

---

## 11. La economía de los tokens

### Content

**La economía del consumo de tokens de IA: cuánto cuesta correr modelos de lenguaje —tokens de entrada contra salida, cacheados contra no cacheados, precio por proveedor— y cómo medir el retorno real que eso genera para el negocio.**

- **Lo que ya vimos** Entrada contra salida, la bola de nieve del historial, el prefijo que se cachea y el que no, y el precio distinto de cada proveedor. Todo eso es el lado del costo.
- **Lo que falta** La otra mitad de la ecuación: cuánto valor devuelve ese gasto. Es la pregunta que ninguna factura responde.

### Sources

- Síntesis de la sección, sin fuente externa: recoge lo visto en las láminas de economía de tokens, fórmula del costo y caching.

### Speaker notes

Lámina de transición, corta. Sirve para nombrar lo que venimos haciendo sin darle nombre: todo lo anterior —entrada contra salida, la bola de nieve, el prefijo cacheado, el precio por proveedor— es economía de tokens. Decilo y hacé la pausa, porque lo que sigue es que esto tiene nombre propio, tiene una fundación detrás y tiene treinta empresas grandes tratando de estandarizarlo. El giro que importa es el de la segunda viñeta: hasta acá midieron el costo, y la pregunta abierta es el valor. Ninguna factura te dice si valió la pena.

---

## 12. La Tokenomics Foundation

### Content

**La Linux Foundation anunció el lanzamiento de la [Tokenomics Foundation](https://www.tokeneconomics.com/), enfocada en establecer estándares abiertos, benchmarks y mejores prácticas para la economía de la infraestructura de IA. Se lanzó el 4 de agosto de 2026 con 30 empresas fundadoras, entre ellas Accenture, IBM, JPMorganChase, Oracle, SAP, ServiceNow, Broadcom y Lenovo.**

- **El token es la unidad, no el total** Buena parte del costo no está en los tokens: cómputo, almacenamiento, base de datos, caché y el trabajo de los ingenieros. Pero el token los atraviesa a todos, y por eso sirve para contarlos.
- **Falta un lenguaje común** No hay forma compartida de conectar gasto con valor, y cada proveedor cobra distinto. Esa fragmentación vuelve incomparable el costo total entre organizaciones.
- **Costo por llamada, no por token** Uno de sus entregables es un método estándar de *costo de servir*: la cuenta completa expresada por llamada, que es la unidad con la que uno diseña un sistema.
- **Medición de valor** Un marco que relacione el gasto con resultados, empezando por la proporción de trabajo que se completa sin intervención humana, medida contra lo que ese proceso cuesta hoy.

- 🎯 **Lo más cercano a esta clase.** Su proyecto *Big-T* clasifica la complejidad de costo de una carga de trabajo **antes** de decidir a qué modelo enrutarla: es el árbol de decisión que vimos, convertido en método. Y el número que explica la urgencia: Goldman Sachs proyecta que el consumo de tokens se multiplique por **24 hacia 2030**.

### Sources

- `research/web/tokenomics-foundation-linux/` — Linux Foundation, comunicado del 4 de agosto de 2026, capturado el 2026-08-28. Aporta verbatim los 30 miembros fundadores, que el token es "una unidad atómica consistente de uso" mientras el costo real abarca cómputo, almacenamiento, base de datos, caché y trabajo humano, los entregables del plan (definiciones, costo de servir por llamada, marco de medición de valor, telemetría sobre la especificación FOCUS), el proyecto Big-T, y la proyección de Goldman Sachs de 24x hacia 2030.
- Sitio de la iniciativa: <https://www.tokeneconomics.com/>

### Speaker notes

Esta lámina existe para que lo anterior no se lea como una preocupación nuestra: hay una fundación de la Linux Foundation, con treinta empresas grandes adentro, tratando de estandarizarlo. Y es material fresco, de hace tres semanas. Cuatro cosas y ninguna es la lista de miembros. La primera es la buena noticia: aunque el token no sea todo el costo, es la unidad que atraviesa a todos los demás y por eso sirve para contar. La segunda es la incómoda: hoy no hay forma estándar de comparar el costo total entre proveedores, y por eso el ejercicio de la tabla de tarifas que vieron antes es necesariamente parcial. La tercera es la que más les sirve como ingenieros: pasar de costo por token a costo por llamada, porque el token es una unidad interna del proveedor y la llamada es la unidad con la que uno diseña. La cuarta tiene una definición operativa linda: empiezan por la proporción de trabajo que se completa sin que intervenga una persona. Es medible, no es retórica. Cerrá con Big-T, que es el puente directo al árbol de decisión de la sección de costos, y con el 24x, que es el número que explica por qué esto se volvió urgente ahora.

---

## 13. Limitaciones de los LLM

### Content

| Alucinaciones | No-determinismo | Sesgo de recencia |
|---|---|---|
| El modelo predice texto plausible y no verifica hechos. Mitigación: restringirlo al contexto dado más revisión humana. | El mismo prompt produce respuestas distintas con temperature > 0. Temperature 0 da la mínima variabilidad; 2.0 la máxima. En producción: temperature baja más varias iteraciones. | El modelo presta más atención al principio y al final del prompt que al medio. Estrategia: instrucciones críticas al inicio, la consulta concreta al final. |

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 12)

### Speaker notes

Tres fallas de familia, no tres bugs. Ninguna se arregla con un modelo mejor, todas se administran con diseño del sistema alrededor del modelo. La de no-determinismo suele ser la que más molesta a esta audiencia, porque rompe la intuición de función pura: mismo input, distinto output. Y ojo con el atajo de "pongo temperature 0 y listo": baja la variabilidad, no la elimina, y en tareas creativas la degrada. El sesgo de recencia es el que menos se conoce y el más accionable: si el prompt tiene cincuenta mil tokens de contexto y la pregunta está en el medio, la respuesta empeora. Instrucción arriba, pregunta abajo. Las tres se retoman en la sección de técnicas avanzadas, así que dejalas planteadas y seguí.

---

## 14. ¿Por qué alucina un modelo?

### Content

**El modelo genera el token más probable dado el contexto. Cuando no tiene el dato, igual genera algo: la fluidez del texto no depende de que sea cierto.**

- **Sin acceso a hechos verificados** El modelo no consulta una base de verdad. Produce texto plausible a partir de patrones, y plausible no es lo mismo que correcto.
- **Entrenamiento incompleto o viejo** Con datos parciales o desactualizados, el modelo extrapola más allá de lo que sabe.
- **Confianza sin verificación** No distingue entre lo que sabe y lo que inventa. Responde con la misma seguridad en los dos casos.
- **Presión de completado** Siempre intenta terminar el texto, incluso sin información suficiente. Un espacio en blanco no es una salida válida para él.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 13)

### Speaker notes

Cuatro causas y ninguna es un defecto de implementación: son consecuencias directas de cómo funciona un motor de completado. La tercera es la que hay que subrayar, porque es la que hace peligrosa a la alucinación en un equipo de software: el modelo no tiene un canal separado para decir "no sé". La probabilidad del token siguiente es alta tanto cuando recita algo que vio mil veces como cuando arma algo verosímil de la nada, y el texto sale con el mismo tono en ambos casos. La cuarta explica por qué la alucinación aparece justo en el peor momento: cuanto más raro el pedido, menos patrón hay y más inventa. Sembrá acá el vínculo con la tesis: si el modelo es un completador, el trabajo del ingeniero es acorralarlo con contexto y con verificación.

---

## 15. Alucinaciones: casos reales

### Content

- **Air Canada (2024)** El chatbot inventó una política de tarifas de duelo que no existía. La aerolínea se defendió diciendo que el chatbot era **una entidad legal separada**, responsable de sus propios actos; el tribunal calificó el argumento de notable y lo rechazó: quien despliega el modelo responde por lo que el modelo dice. [Moffatt v. Air Canada, 2024 BCCRT](https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html)
- **Abogados: ya no es anecdótico** Hay **más de 1.148 casos documentados** de alucinaciones en tribunales de EE.UU., y las sanciones escalaron: en el Sexto Circuito, honorarios, costas dobles, **15.000 dólares de sanción punitiva a cada abogado** y derivación disciplinaria. [Norton Rose Fulbright, 2026](https://www.nortonrosefulbright.com/en/knowledge/publications/792d8bf3/ai-in-litigation-update-on-gen-ai-sanctions-in-2026)
- **El 19,7% de los paquetes no existe** Sobre 576.000 muestras de código de 16 modelos, **uno de cada cinco paquetes recomendados no existe en ningún registro**: 205.000 nombres únicos inventados. Los modelos abiertos alucinan 21,7% contra 5,2% de los propietarios. [Socket, análisis del paper](https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks)
- **Slopsquatting** El ataque que se monta sobre lo anterior: el atacante **registra el nombre que el modelo alucina** en npm o PyPI y espera. No hay typo humano que explotar; la puerta la abre el asistente de código. El término se acuñó en abril de 2025. [Slopsquatting](https://en.wikipedia.org/wiki/Slopsquatting)

### Sources

- `research/web/alucinaciones-sanciones-2026/` — Norton Rose Fulbright, actualización 2026 sobre sanciones por IA generativa en litigio; aporta el conteo de casos documentados y las sanciones de *Whiting v. City of Athens* (Sexto Circuito).
- `research/web/slopsquatting-socket/` y `research/web/slopsquatting-wikipedia/` — análisis del paper *We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs*: 19,7% sobre 576.000 muestras de 16 modelos, 205.000 nombres únicos, 21,7% en modelos abiertos contra 5,2% en propietarios. Término acuñado en abril de 2025.
- *Moffatt v. Air Canada*, 2024 BCCRT — citado por su referencia oficial; **no ingestado**, la fuente devolvió 403.

### Speaker notes

Cuatro casos y un orden deliberado: primero el costo legal de desplegar, después el costo legal de usar, y al final los dos que les tocan como ingenieros. El de Air Canada es el más útil de los dos primeros por la defensa que intentó la empresa: sostuvo que el chatbot era una entidad legal separada, responsable de sus propios actos. El tribunal lo rechazó, y esa es la línea que hay que subrayar: el que despliega el modelo responde por lo que el modelo dice. El segundo instala escala: más de mil cien casos documentados y sanciones que ya incluyen dinero punitivo y derivación disciplinaria, no un tirón de orejas. El tercero es el número que quiero que se lleven: uno de cada cinco paquetes que recomienda un modelo no existe. Preguntales si les pasó; la respuesta suele ser que sí. Y marcá la diferencia entre modelos abiertos y propietarios, que es de cuatro veces, porque es un criterio de selección concreto. El cuarto cierra el arco y es el que engancha con la sección de seguridad del final: el código alucinado compila mal y se detecta rápido, pero un nombre de dependencia alucinado que alguien registró antes que vos es un vector de ataque real, y ahí no hay compilador que te salve.

---

## 16. Mitigar alucinaciones: el prompt

### Content

**Lo que se puede hacer dentro de la llamada al modelo, sin cambiar el sistema alrededor.**

- **Grounding en contexto** Instruir al modelo a responder solo con el contexto provisto, y a decir que no sabe cuando ese contexto no alcanza.
- **RAG (retrieval-augmented generation)** Recuperar e inyectar solo la información verificada y relevante para esa consulta, en vez de confiar en la memoria del modelo.
- **Temperature = 0** Minimizar la aleatoriedad en tareas de extracción y clasificación, donde la creatividad es un defecto.
- **Self-consistency** Generar varias respuestas independientes y quedarse con la más frecuente.
- **Revisión humana en el loop** El output es siempre un borrador. Alguien del equipo lo valida antes de que llegue a producción.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 14)
- `self-consistency-wang.web.md` — Wang et al. (2022), la fuente primaria de self-consistency.

### Speaker notes

Cinco palancas ordenadas de la más barata a la más cara. Grounding es una línea de texto en el system prompt y ya cambia el comportamiento. RAG es infraestructura: alguien tiene que indexar, recuperar y decidir qué entra. Temperature 0 es gratis pero no es gratis en todas las tareas, así que aclará el alcance: extracción y clasificación sí, generación de texto no. Self-consistency se ve en detalle en la sección cinco, acá solo nombrala. Y la quinta es la que ningún equipo puede saltear: mientras la tasa de alucinación del sistema no esté medida, la revisión humana no es una etapa opcional del proceso, es la única garantía que hay.

---

## 17. Mitigar alucinaciones: el proceso

### Content

**El testing formal es la ventaja competitiva de un equipo de software acá: es la disciplina que ya se tiene y que la mayoría de los equipos de producto no aplica a los prompts.**

- **Dataset de evaluación** Mínimo 50 a 100 casos con ground truth del dominio, anotados por quien sabe.
- **Métricas de alucinación** Faithfulness score, hallucination rate, ROUGE-L. Sin métrica no hay umbral de aceptación.
- **Regression testing** Correr el eval set completo en cada cambio de prompt, igual que la suite de tests en cada commit.
- **Red teaming** Probar con casos ambiguos y contradictorios antes de salir a producción.

- 🎯 **Regla de oro: un sistema cuya tasa de alucinación no se puede medir no se despliega.**

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 14)

### Speaker notes

Acá la clase les habla en su idioma y conviene decirlo de frente: las cuatro prácticas de esta slide son CI/CD aplicado a un artefacto que casi nadie versiona ni testea. El dataset de evaluación es el fixture, las métricas son los asserts, el regression testing es el pipeline y el red teaming es el fuzzing. La pregunta que suele aparecer es de dónde salen los 50 a 100 casos. Respuesta honesta: de producción, mirando lo que el sistema ya respondió mal, y anotando a mano. No hay atajo. La regla de oro del cierre es la frase para llevarse, y se retoma en la sección cinco con la slide de prompts sin verificación.

---

## 18. Modelo mental: motores de completado

### Content

**Los LLM completan patrones vistos en el entrenamiento y no entienden la intención. Pensarlos como un autocompletado muy sofisticado cambia cómo se escribe el prompt.**

**Cómo es el modelo**

- **Fortaleza** Muy bueno reconociendo patrones que vio muchas veces.
- **Debilidad** Alucina cuando el patrón no estaba en el entrenamiento.
- **Sin razonamiento interno** Predice el siguiente token más probable, y nada más.

**Qué hacer con eso**

- **Prompt vago** "Extraé nombre y email" puede fallar, porque no hay un patrón explícito que completar.
- **Prompt estructurado** Darle el patrón de completado servido:
  `Nombre: [campo]` / `Email: [campo]` / `De: [texto]`

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 15)

### Speaker notes

Esta slide es el ensayo de la tesis, y por eso vale la pena bajar la velocidad. Si el modelo completa patrones, entonces un prompt bien escrito es un patrón fácil de completar, y uno mal escrito es un patrón ambiguo. El ejemplo de la derecha lo muestra en cuatro líneas: el mismo pedido, escrito como plantilla, deja de tener grados de libertad. Es el mismo mecanismo que explica por qué funcionan las etiquetas XML de la sección tres y los ejemplos few-shot de la sección cuatro. Anticipá que en la sección cinco esto mismo va a explicar por qué chain of thought mejora la precisión: escribir los pasos es generar el patrón que hace más probable el token correcto al final.

---

# 2. Modelos y costos

**Goal of this section:** Convertir la elección de modelo en una decisión con números: qué cobra cada uno, cuánto ahorra el caching y cuándo conviene encadenar un modelo barato con uno caro.

---

## 1. Tarifas: familia Claude

### Content

| Modelo | Generación | Ventana | Entrada ($/MTok) | Salida ($/MTok) |
|---|---|---|---|---|
| Fable 5 | 2026 | 1M | $10,00 | $50,00 |
| Opus 5 | 2026 | 1M | $5,00 | $25,00 |
| Opus 4.8 | 2026 | 1M | $5,00 | $25,00 |
| Sonnet 5 | 2026 | 1M | $2,00 | $10,00 |
| Sonnet 4.6 | 2026 | 1M | $3,00 | $15,00 |
| Haiku 4.5 | 2025 | 200K | $1,00 | $5,00 |

- **Modificadores de tarifa** Cache hit: 10% del precio de entrada · Batch: 50% de la tarifa · Fast Mode (Opus 5 y Opus 4.8): $10 / $50 · Búsqueda web: $10 por cada 1.000 búsquedas · Ejecución de código: 50 h gratis por día, después $0,05/hora.

![Selector de modelo y de effort en la interfaz de Claude](images/slide-11-1.jpg)

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 11) — tarifario y captura del selector de modelo.
- Precios, ventanas y niveles de effort verificados contra el catálogo vigente de la API de Claude (corte 2026-06-24). Correcciones respecto del deck original: se agregaron Opus 5 y Sonnet 5, y la lista de niveles de effort incluye `medium`, que el deck omitía.
- Derivación del cache hit: $0,50 en Opus 4.8 = 10% de $5,00 de entrada; la misma relación se cumple en las cuatro filas del deck original.

### Speaker notes

Dos cosas y ninguna es la tabla. La primera: la salida cuesta cinco veces la entrada en toda la familia, así que la variable que hay que vigilar es cuánto habla el modelo, no cuánto se le manda. La segunda: entre Haiku 4.5 y Fable 5 hay un factor diez de precio, y esa distancia es la que hace que valga la pena la cascada que viene después. Mostrales la captura: el selector de modelo y de esfuerzo está a la vista en la interfaz, no escondido en la API — el esfuerzo lo trabajamos en detalle en la sección de técnicas avanzadas. Si preguntan por Fable 5, aclará que la captura lo muestra como no disponible en ese momento y que la tabla sí le pone precio: son dos estados del mismo producto en fechas distintas.

---

## 2. Elegir modelo: árbol de decisión

### Content

**Cuatro preguntas en orden. La primera que dé "sí" define el modelo.**

![Arbol eleccion modelo](images/s2-2-1-arbol-eleccion-modelo.svg)
<!-- ascii-source:
  ¿La tarea es simple?
  (clasificar, extraer, rotular)
       |
       +-- SI --&gt; modelo chico y barato
       |            Haiku 4.5 / GPT-4o Mini / Gemini Flash
       NO
       |
  ¿Necesita mas de 1M de contexto?
       |
       +-- SI --&gt; el de ventana mas grande disponible
       |            (hoy: Gemini Pro, 2M)
       NO
       |
  ¿Necesita JSON garantizado por la API?
       |
       +-- SI --&gt; modelo con structured outputs
       |
       NO --&gt; el mejor modelo para la calidad que se necesita
       |
  ¿El costo es critico por volumen?
       |
       +-- SI --&gt; model cascading (barato primero, caro si hace falta)
-->
<!-- ascii-note:
intent: mostrar la eleccion de modelo como una cascada de cuatro preguntas en orden fijo, donde la primera que da "si" corta la decision; el orden de las preguntas es el contenido, no los nombres de modelo que devuelve
emphasize: la columna de decisiones encadenadas y las salidas de cada rama SI; que la pregunta de costo va ultima, despues de resolver dificultad, contexto y formato
labels: "¿La tarea es simple?", "¿Necesita mas de 1M de contexto?", "¿Necesita JSON garantizado por la API?", "¿El costo es critico por volumen?", y las salidas de cada rama
-->

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 45)
- Nombres de modelo actualizados: el árbol original recomendaba GPT-3.5 y Gemini 1.5 Pro, dos generaciones atrás del resto del deck.

### Speaker notes

El árbol vale más por el orden de las preguntas que por los nombres que devuelve. Primero la dificultad de la tarea, porque es la que más plata mueve: si clasificar tickets se puede hacer con un modelo chico, cualquier discusión sobre caching es secundaria. Segundo el contexto, que es una restricción dura y no negociable. Tercero el formato de salida, que en la práctica decide quién queda en carrera cuando el output alimenta código. Y recién al final el costo, porque optimizar costo antes de saber si la calidad alcanza es optimizar lo que no importa. Decí también por qué el árbol nombra familias y no versiones: los nombres cambian cada seis meses, las preguntas no.

---

## 3. Prompt caching: los números

### Content

**El mismo workload de 10.000 consultas, con 80% de hit rate.**

| Escenario | Cuenta | Costo |
|---|---|---|
| Sin caching | 10.000 × 50.100 tokens = 501M | **$1.503,00** |
| Misses (20%) | 2.000 × 50.100 tokens = 100,2M | $300,60 |
| Hits (80%) | 8.000 × (50.000 × 0,10 + 100) = 40,8M equivalentes | $122,40 |
| **Con caching** | | **$423,00** |

- 🎯 **Ahorro: $1.080,00 sobre $1.503,00, un 72%.**
- ⚠️ La cuenta ignora el costo de escritura del caché, que se cobra por encima de la tarifa de entrada la primera vez. Con 10.000 consultas sobre el mismo prefijo, ese costo se diluye.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 46)
- Derivaciones, a $3/MTok (Claude Sonnet 4.6): sin caching = 501.000.000 / 1.000.000 × $3 = $1.503,00 · misses = 100.200.000 / 1.000.000 × $3 = $300,60 · hits = 8.000 × 5.100 tokens equivalentes = 40.800.000, × $3/MTok = $122,40 · total = $423,00 · ahorro = $1.503,00 − $423,00 = $1.080,00 = 71,9% de $1.503,00.

### Speaker notes

Esta slide corrige un error del deck original, y vale la pena decirlo en voz alta porque enseña algo: el deck declaraba $450 de costo con caching y un ahorro del 70%, y la cuenta no cerraba. Rehecha da $423 y 72%. La diferencia es chica en plata y grande en método: una cifra que nadie recalculó sobrevivió a todas las revisiones porque sonaba razonable. Es el mismo problema que van a tener con las salidas de un LLM. Sobre la fila de hits: los 5.100 tokens equivalentes salen de 50.000 cacheados al 10% más los 100 dinámicos a precio completo. La advertencia del final es honesta y conviene no saltearla, porque en un workload de pocas llamadas por prefijo la escritura del caché se puede comer el ahorro.

---

## 4. Model cascading

### Content

**Intentar primero con el modelo barato. Si la confianza es baja, escalar al caro. El ahorro depende de que el gating de confianza sea confiable.**

![Cascada dos modelos](images/s2-4-1-cascada-dos-modelos.svg)
<!-- ascii-source:
  Request entra
       |
       v
  +---------------------------+
  |  Modelo barato            |
  |  (Haiku 4.5)              |
  |  intenta resolver         |
  +---------------------------+
       |
       v
  ¿confianza suficiente?
       |
       +-- SI --&gt; retornar respuesta      (costo minimo, latencia baja)
       |
       +-- NO --&gt; +---------------------------+
                  |  Modelo caro             |
                  |  (Opus 4.8)              |
                  |  resuelve                |
                  +---------------------------+
                            |
                            v
                     retornar respuesta      (solo cuando hace falta)
-->

<!-- ascii-note:
intent: mostrar el flujo de dos etapas del model cascading, con el gate de confianza como el punto de decision que define si el ahorro existe
emphasize: el rombo de decision "¿confianza suficiente?" y las dos ramas con su costo asociado; la rama SI es la que produce el ahorro
labels: "Modelo barato (Haiku 4.5)", "¿confianza suficiente?", "Modelo caro (Opus 4.8)", costo minimo / solo cuando hace falta
-->

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 48)
- Nombres de modelo actualizados: el deck original nombraba "Haiku/GPT-3.5" y "GPT-4/Sonnet", dos generaciones atrás del resto del deck.

### Speaker notes

La idea es de una línea y la trampa está en el rombo del medio. Todo el ahorro del cascading depende de que el sistema sepa cuándo la respuesta barata no alcanza, y esa señal casi nunca viene servida. Algunos proveedores devuelven log-probabilities y sirven; con otros hay que armar el gate a mano, por ejemplo pidiéndole al modelo chico que declare su confianza, con el problema obvio de que un modelo mal calibrado declara alta confianza sobre cosas que inventó. Preguntales cómo lo resolverían. Suele salir la idea de una segunda llamada de verificación, y ahí conviene señalar que esa llamada también cuesta y puede comerse el ahorro. La slide siguiente da los criterios para decidir si vale la pena.

---

## 5. Cascading: cuándo sí y cuándo no

### Content

**Cuándo conviene**

- **Alto volumen de tareas parecidas** Muchas consultas con una distribución de dificultad predecible.
- **Señal de confianza clara** El sistema puede saber cuándo la respuesta barata no alcanza.
- **Presión de costo con piso de calidad** Hay que ahorrar sin bajar la precisión.

**Cuándo evitarlo**

- **Latencia baja requerida** Cada escalón agrega una llamada más.
- **Confianza difícil de medir** Sin señal confiable, el routing falla en silencio.
- **Bajo volumen** La complejidad de mantener el routing no se paga.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 48)

### Speaker notes

La fila que decide es la última de la tabla. El cascading no es una configuración, es un componente más del sistema: hay que rutear, monitorear el porcentaje de escalados y detectar cuándo el gate se desalinea. Un equipo chico que procesa cien consultas por día está pagando esa complejidad para ahorrar unos dólares. Un equipo que procesa cien mil, no. Si querés cerrar con una regla práctica: medí primero cuánto cuesta hacer todo con el modelo bueno a effort bajo. Muchas veces eso alcanza y no hace falta cascada, porque un modelo nuevo a effort bajo suele rendir como el anterior a effort alto, y un solo modelo mantiene un solo namespace de caché.

---

# 3. Prompts estructurados

**Goal of this section:** Pasar del prompt escrito a mano al prompt con anatomía: seis componentes, delimitadores explícitos y un contrato de salida que el código pueda validar.

---

## 1. Los 6 componentes

### Content

**La diferencia entre un prototipo que a veces anda y un sistema de producción suele estar en la estructura del prompt, no en la redacción.**

![Anatomia prompt seis partes](images/s3-1-1-anatomia-prompt-seis-partes.svg)
<!-- ascii-source:
  ANATOMIA DE UN PROMPT DE PRODUCCION

  atencion
  del modelo
            +--------------------------------------------------+
    ALTA >  | 1  ROL / PERSONA     quien es el modelo           |
            +--------------------------------------------------+
            | 2  CONTEXTO          que necesita saber           |
            +--------------------------------------------------+
    BAJA >  | 3  INSTRUCCIONES     que tiene que hacer, paso    |
            |                      a paso                       |
            +--------------------------------------------------+
            | 4  RESTRICCIONES     que NO debe hacer, y en que  |
            |                      formato responde             |
            +--------------------------------------------------+
            | 5  EJEMPLOS          como se ve una respuesta     |
            |    (few-shot)        correcta -- 3 a 5 alcanzan   |
            +--------------------------------------------------+
    ALTA >  | 6  INPUT             el dato de ESTA llamada      |
            +--------------------------------------------------+

  El orden no es cosmetico: el modelo lee mejor el principio y el final
  que el medio, por eso el rol va arriba y el input abajo.
-->
<!-- ascii-note:
intent: mostrar el prompt como un bloque compuesto de seis partes apiladas en un orden que importa, y ligar ese orden al sesgo de recencia (el modelo atiende mejor el principio y el final que el medio)
emphasize: la pila de seis bandas numeradas como una sola unidad; los marcadores ALTA / BAJA / ALTA de la izquierda, que son el argumento de por que ese orden y no otro
labels: "ROL / PERSONA", "CONTEXTO", "INSTRUCCIONES", "RESTRICCIONES", "EJEMPLOS (few-shot)", "INPUT", eje de atencion ALTA / BAJA / ALTA, y la linea de cierre sobre el orden
-->

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 17)
- `aitutorial-structured-prompt-engineering.web.md` — anatomía de seis componentes y la tesis de apertura ("the difference between a flaky prototype and a reliable production system often comes down to prompt structure").

### Speaker notes

Seis componentes y el orden importa. Las definiciones ya no están en la lámina, así que van habladas mientras señalás cada banda. **Rol**: fija el nivel de expertise y los patrones de comportamiento. **Contexto**: la información de fondo que la tarea necesita, el servicio, las convenciones del equipo. **Instrucciones**: qué hacer, paso a paso, y cuanto más específicas mejor. **Restricciones**: los límites y el formato de salida. **Ejemplos**: casos resueltos que demuestran el comportamiento esperado. **Input**: los datos concretos de esta llamada. Rol y contexto van arriba porque condicionan todo lo que sigue, y porque el modelo presta más atención al principio del prompt. El input va último por la misma razón invertida: es lo que tiene que estar fresco cuando empieza a generar. La discusión que suele aparecer es si hace falta todo esto para pedir un resumen. No, y conviene decirlo: los seis componentes son la anatomía de un prompt de producción, el que corre diez mil veces por día y tiene que dar el mismo formato siempre. Para una consulta única en el chat, alcanza con instrucciones e input. El ejemplo de la slide siguiente muestra los seis armados.

---

## 2. Un prompt completo

### Content

**Los seis componentes armados, sobre una tarea real: revisar un pull request.**

<!-- ascii-render: documentation-only -->
```
# [1] ROL / PERSONA
Sos un revisor de codigo senior, con experiencia en sistemas de alta disponibilidad.

# [2] CONTEXTO
Estas revisando un pull request sobre el servicio de facturacion.
Las convenciones del equipo estan en CONTRIBUTING.md y en la guia de estilo del lenguaje.

# [3] INSTRUCCIONES
1. Lee el diff completo antes de comentar.
2. Lista los problemas mas graves (maximo 3).
3. Para cada uno, indica archivo y linea.
4. Propone un fix concreto.

# [4] RESTRICCIONES
- No reescribas el modulo entero: solo el fragmento afectado.
- Comenta unicamente lo que aparece en el diff.
- Formato de salida: JSON con las claves severidad, archivo, linea, problema, fix.

# [5] EJEMPLOS (Few-shot)
Diff: se agrega open(path) sin with ni close() en billing/export.py, linea 42.
-> {"severidad": "alta", "archivo": "billing/export.py", "linea": 42,
    "problema": "El descriptor no se cierra si la escritura lanza excepcion.",
    "fix": "Usar with open(path) as f: en lugar de open(path)."}

# [6] INPUT
Diff: en billing/invoice.py, linea 118, se concatena input del usuario
dentro de una query SQL con un f-string.
```

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 17) — estructura de seis bloques del prompt original.
- `aitutorial-structured-prompt-engineering.web.md` — la fuente promete el prompt armado pero la extracción lo perdió; este ejemplo es propio, escrito sobre el esqueleto de la fuente.

### Speaker notes

Leé el prompt en voz alta, bloque por bloque, y hacé notar dos cosas. La primera: el bloque de restricciones es el que más trabajo hace, y es el que la gente saltea. "Comentá solo lo que aparece en el diff" es lo que impide que el modelo se ponga a opinar sobre archivos que no se tocaron. La segunda: el ejemplo few-shot no muestra solo la respuesta, muestra el formato exacto, y por eso el modelo lo copia. Buen momento para una pregunta al grupo: qué pasa si sacamos el bloque 5. Respuesta: el JSON sale, pero con claves distintas cada vez, y el código que lo parsea empieza a romperse. Aclará que este prompt es propio: la fuente que lo promete lo perdió en la extracción.

---

## 3. Salidas estructuradas: JSON Schema

### Content

**Imponer un esquema de salida reduce los errores de parseo y los reintentos, y vuelve la salida verificable por código.**

**Dos enfoques**

- **Esquema en el prompt** Incluir el formato JSON en las instrucciones. Más flexible, sin garantías.
- **Modo JSON de la API** Usar `response_format: json_object`. Más confiable: garantiza estructura válida.

<!-- ascii-render: documentation-only -->
```
{
  "severidad": "alta | media | baja",
  "archivo": "string",
  "linea": "number",
  "problema": "string",
  "fix": "string"
}
```

- ✅ **Validación automática** La salida se verifica con el esquema, sin leerla a mano.
- ✅ **Menos errores de parseo** Menos fallos en el pipeline y menos reintentos.
- ✅ **Integración directa** El JSON entra al issue tracker o al bot de review sin traducción intermedia.

<!-- enlace de la forma: https://aitutorial.dev/prompting/structured-prompt-engineering -->
- [Ver ejemplo interactivo en aitutorial.dev →](https://aitutorial.dev/prompting/structured-prompt-engineering)

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 18)
- `aitutorial-structured-prompt-engineering.web.md` — la distinción entre incluir el esquema en el prompt y usar la funcionalidad de salidas estructuradas de la API, y la afirmación sobre parseo y reintentos.

### Speaker notes

La distinción entre los dos enfoques es la que hay que dejar clara, porque se confunde todo el tiempo. Pedir el formato en el prompt es una sugerencia: el modelo casi siempre obedece y ese casi es el problema, porque el uno por ciento que falla aparece en producción a las tres de la mañana. La funcionalidad de salidas estructuradas de la API es una garantía a nivel de decodificación, no una instrucción. Si el output alimenta código, se usa la segunda. El esquema de la slide es el del revisor de código de la slide anterior, así que se ve el circuito completo: el prompt pide, el esquema define, el código valida. Y una advertencia útil: un esquema muy estricto sobre una tarea ambigua no arregla la ambigüedad, la esconde en un campo con un valor plausible.

---

## 4. XML: estructura semántica

<!-- design: split-right -->

### Content

**Las etiquetas marcan dónde empieza y termina cada parte del prompt. El modelo no tiene que inferir la estructura: se la das dibujada.**

<!-- ascii-render: documentation-only -->
```
<tarea>Clasificar issues de GitHub</tarea>
<instruccion>
Devolve UNA sola palabra: bug, feature o pregunta.
Para cada <entrada>, produci la <salida> correspondiente.
</instruccion>
<ejemplos>
  <ejemplo>
    <entrada>Al exportar a CSV con mas de 10.000 filas, el proceso corta en la 8.192.</entrada>
    <salida>bug</salida>
  </ejemplo>
  <ejemplo>
    <entrada>Estaria bueno poder filtrar el listado por fecha de creacion.</entrada>
    <salida>feature</salida>
  </ejemplo>
  <ejemplo>
    <entrada>¿El endpoint /v2/orders soporta paginacion por cursor?</entrada>
    <salida>pregunta</salida>
  </ejemplo>
</ejemplos>
<entrada>
Despues de actualizar a la 3.2, el login con SSO devuelve 500 en staging.
</entrada>
```

- **Fronteras explícitas** Tarea, instrucciones, ejemplos y entrada quedan separados sin ambigüedad. Nada se confunde con nada.
- **Formato que ya conocen** Los LLM se entrenaron con enormes cantidades de HTML y XML de la web, así que la notación les resulta familiar.
- **La salida también se delimita** Pedir la respuesta dentro de una etiqueta vuelve trivial el parseo y evita que el modelo mezcle explicación con resultado.
- **El overhead se paga solo** Las etiquetas suman tokens, pero se compensan con menos reintentos y menos errores de parseo. Si el prompt es estable, el caching lo absorbe.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 19)
- `aitutorial-structured-prompt-engineering.web.md` — por qué funcionan las etiquetas (entrenamiento sobre HTML/XML, fronteras claras en el contexto) y el overhead de tokens compensado por caching. La misma fuente atribuye un "40-60% menos de alucinaciones" a "teams report", sin estudio ni medición: por eso la afirmación queda cualitativa acá.

### Speaker notes

El argumento de por qué funcionan las etiquetas es el mismo de la slide del motor de completado: el modelo vio millones de documentos con esta forma, así que una etiqueta de apertura es un patrón fortísimo. La segunda razón es más práctica: sin delimitadores, el modelo no sabe dónde termina la instrucción y dónde empieza el dato, y ese es el agujero por donde entra una inyección de prompt. Sobre las dos donas: el deck original les ponía 40% y 60% de reducción de alucinaciones, y esa cifra no tiene respaldo. La fuente la atribuye a "lo que reportan los equipos", sin estudio. Así que la afirmación queda cualitativa y las donas están marcadas para rehacer o retirar en el polish.

---

# 4. In-context learning

**Goal of this section:** Mostrar que los ejemplos dentro del prompt cambian el comportamiento del modelo sin tocar sus pesos, y dar el criterio para elegir cuántos poner.

---

## 1. In-context learning (ICL)

### Content

**Capacidad del modelo de aprender un patrón a partir de ejemplos puestos en el prompt, sin modificar sus pesos. No se re-entrena: reconoce el patrón en los ejemplos y lo aplica al caso nuevo.**

![Tres regimenes icl](images/s4-1-1-tres-regimenes-icl.svg)
<!-- ascii-source:
  Lo que viaja dentro del prompt, en cada regimen

  ZERO-SHOT            FEW-SHOT                  MANY-SHOT
  sin ejemplos         2 a 10 ejemplos           decenas o cientos

  [ instruccion ]      [ instruccion ]           [ instruccion ]
                       [ ej ][ ej ]              [ ej ][ ej ][ ej ][ ej ]
                       [ ej ]                    [ ej ][ ej ][ ej ][ ej ]
                                                 [ ej ][ ej ]  ...
  [ caso nuevo  ]      [ caso nuevo  ]           [ caso nuevo  ]

  tokens por llamada  -----------------------------------------&gt;  suben
  precision           -----------------------------------------&gt;  sube y satura
  costo               -----------------------------------------&gt;  sube siempre

  Los pesos del modelo no cambian en ningun punto de la progresion.
-->
<!-- ascii-note:
intent: mostrar que los tres regimenes de in-context learning son el MISMO prompt con distinta cantidad de ejemplos intercalados entre la instruccion y el caso nuevo, y que la progresion tiene un costo monotono contra una precision que satura
emphasize: las tres columnas como variaciones de una misma estructura; el bloque de ejemplos que crece de vacio a saturado; el contraste entre "precision sube y satura" y "costo sube siempre"
labels: "ZERO-SHOT", "FEW-SHOT", "MANY-SHOT", "instruccion", "ej", "caso nuevo", ejes tokens / precision / costo, y la linea de cierre sobre los pesos
-->

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 22)
- `few-shot-learners-brown.web.md` — Brown et al. (2020), el paper de GPT-3: "with tasks and few-shot demonstrations specified purely via text interaction with the model", sin actualizaciones de gradiente ni fine-tuning. El término *in-context learning* y la taxonomía zero/one/few-shot son del cuerpo del paper, no del abstract capturado.

### Speaker notes

La frase que hay que dejar clavada es "sin modificar los pesos", y el diagrama la sostiene: las tres columnas son el mismo prompt, con más o menos ejemplos metidos entre la instrucción y el caso. Las definiciones van habladas. **Zero-shot**: solo la instrucción, sin ejemplos, todo depende del conocimiento preentrenado. **Few-shot**: entre 2 y 10 casos resueltos antes del caso a resolver, y es el régimen más usado en producción. **Many-shot**: decenas o cientos de ejemplos, para tareas complejas o con mucha variabilidad. Señalá los tres ejes del pie, porque ahí está la decisión: la precisión satura y el costo no. Para esta audiencia el contraste natural es con fine-tuning: fine-tuning cambia el artefacto y cuesta una corrida de entrenamiento, in-context learning cambia el prompt y cuesta tokens. Eso reordena la intuición de cuándo conviene cada cosa. El dato histórico ayuda: la capacidad se documentó en el paper de GPT-3 en 2020, y lo llamativo entonces fue que nadie la había programado, apareció al escalar. Un matiz de honestidad, por si alguien va a la fuente: el término "in-context learning" y la taxonomía de zero, one y few-shot están en el cuerpo del paper, no en el abstract.

---

## 2. Zero-shot vs. few-shot

<!-- slide nueva: el deck original define zero-shot y nunca lo ejemplifica -->

### Content

**Mismo modelo, misma tarea, mismo input. Lo único que cambia es si hay ejemplos.**

| Zero-shot | Few-shot |
|---|---|
| `Clasifica la severidad de este issue.`<br><br>`Issue: el export a CSV corta en la fila 8.192.`<br><br>→ `"Parece un problema de tamaño de buffer. Severidad media-alta, dependiendo del uso."` | `Clasifica la severidad como CRITICO, ALTO o BAJO.`<br><br>`Issue: caen todos los checkouts en produccion. -> CRITICO`<br>`Issue: el tooltip esta en ingles. -> BAJO`<br><br>`Issue: el export a CSV corta en la fila 8.192.`<br><br>→ `ALTO` |
| Formato libre, vocabulario propio, imposible de parsear. | Una etiqueta del conjunto pedido. El código la consume directo. |

- 💡 Los ejemplos no le enseñan al modelo qué es la severidad. Le enseñan qué forma tiene la respuesta y dónde están los cortes entre categorías.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 22) — el deck original define los tres regímenes y da ejemplo de few-shot y many-shot, pero nunca de zero-shot.
- `few-shot-learners-brown.web.md` — Brown et al. (2020).

### Speaker notes

Slide nueva, y llena un agujero real del deck original: definía zero-shot y nunca lo mostraba. El contraste sobre el mismo input es lo que hace el trabajo. En zero-shot el modelo responde bien en el sentido humano y mal en el sentido operativo: la respuesta es correcta y no se puede parsear, porque inventó su propia escala. Con dos ejemplos, la escala deja de ser suya. Ese es el punto de la línea de cierre y conviene decirlo despacio, porque contradice la intuición de que los ejemplos "enseñan el concepto". No enseñan el concepto: fijan el formato y ubican las fronteras entre categorías. Si el grupo pregunta cuántos ejemplos, la respuesta viene en la slide siguiente.

---

## 3. Few-shot learning

### Content

**Buenas prácticas**

- Incluir entre 2 y 10 ejemplos en el prompt.
- Estructura: instrucción, ejemplo 1, ejemplo 2, ..., caso nuevo.
- Ejemplos representativos: casos claros de cada categoría más los casos borde.
- Formato idéntico en todos los ejemplos.
- Tres a cinco suelen alcanzar. Calidad antes que cantidad.

**Ejemplo: clasificar el sentimiento de un comentario**

<!-- ascii-render: documentation-only -->
```
Clasifica el sentimiento como POSITIVO, NEGATIVO o NEUTRO.

"La bateria dura muchisimo"        -> POSITIVO
"Se trabo a los dos dias"          -> NEGATIVO
"El dispositivo llego el martes"   -> NEUTRO
```

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 23)
- `aitutorial-structured-prompt-engineering.web.md` — "3-5 examples usually enough"; más ejemplos son más tokens y más costo; los ejemplos deberían cubrir casos borde y no solo los obvios.
- `few-shot-learners-brown.web.md` — Brown et al. (2020).

### Speaker notes

La práctica que más rinde y menos se aplica es la tercera. Casi todo el mundo pone tres ejemplos fáciles, y el modelo aprende a resolver lo fácil, que ya resolvía solo. Los ejemplos tienen que cubrir los casos borde: el comentario ambiguo, el que mezcla dos categorías, el que está en otro idioma. Esa es la fuente que lo dice, no una opinión. La cuarta práctica parece cosmética y no lo es: si el formato varía entre ejemplos, el modelo tiene dos patrones para elegir y elige por turno. Y la quinta tiene una razón de plata que ya vieron: cada ejemplo viaja en cada request, así que veinte ejemplos son veinte veces ese costo, multiplicado por el volumen.

---

## 4. Many-shot learning

### Content

**Cuándo pasar a many-shot**

- Decenas o cientos de ejemplos, aprovechando las ventanas de contexto grandes.
- Cuando few-shot no captura la variabilidad del problema.
- Cuando hay muchas categorías, o categorías con fronteras finas.
- En producción: agregar ejemplos al prompt a medida que aparecen los errores. Es mejorar el sistema sin re-entrenar nada.

**Ejemplo: triage de issues de GitHub**

<!-- ascii-render: documentation-only -->
```
# INSTRUCCION
Clasifica la severidad del issue como CRITICO, ALTO o BAJO.

# EJEMPLOS
Issue: en produccion, todos los checkouts fallan con 500 desde el deploy de las 14:20.
-> CRITICO (caida total de una ruta que genera ingresos)

Issue: el export a CSV corta en la fila 8.192 con datasets grandes.
-> ALTO (perdida silenciosa de datos, hay workaround manual)

Issue: el tooltip del boton Guardar aparece en ingles en la version en espanol.
-> BAJO (cosmetico, no bloquea)

# INPUT
Issue: /v2/orders devuelve 200 con body vacio cuando el token expiro, en lugar de 401.
Tres clientes ya cachearon la respuesta vacia.

-> ALTO (contrato de API roto, y el error se propaga silencioso a los consumidores)
```

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 24)
- `few-shot-learners-brown.web.md` — Brown et al. (2020).

### Speaker notes

El punto fuerte de esta slide es la cuarta línea, porque describe un bucle de mejora que ningún equipo asocia con machine learning: cada vez que el sistema clasifica mal, ese caso se agrega al prompt como ejemplo, y el sistema mejora sin tocar el modelo. Es la forma más barata de aprendizaje continuo que existe, y el costo es lineal en tokens. El caso resuelto del final es el que el deck original dejaba abierto con signos de pregunta: fijate que la respuesta correcta no sale del texto del issue sino de la consecuencia, que es un contrato de API roto propagándose a tres clientes. Si querés hacerlo participativo, tapá la respuesta y pediles que voten CRITICO, ALTO o BAJO antes de mostrarla. Suele haber desacuerdo, y ese desacuerdo es el argumento de por qué hacen falta ejemplos con la frontera explicitada.

---

# 5. Prompting avanzado

**Goal of this section:** Recorrer las técnicas que hacen escribir al modelo antes de responder, medir lo que cuestan y explicar por qué funcionan, que es la tesis de la clase.

- [closed] 2026-09-01 — "tal vez mejor poner todo en el subtítulo reducido. Queda más en mini-bloques. Revisar todos los slides de esa sección con lo mismo."
  Resolution: criterio de mini-bloques aplicado a las láminas de la sección cuyos ítems eran párrafos, sin tocar la estructura de la sección ni los cuatro diagramas. En 5.4 (self-consistency) el par 'El problema / La solución' se fundió en el encabezado y 'Cuándo usarlo' quedó en cuatro bloques cortos. Además: 5.1 pasó de dos tablas (una con las celdas vacías) a cuatro ítems etiquetados con recuadro de cierre; 5.6 convirtió 'Limitaciones' de viñetas sueltas a bloques etiquetados; 5.3, 5.7 y 5.12 cortaron los ítems a una línea; 5.3 y 5.7 ganaron encabezado de síntesis. La prosa sacada bajó a `### Speaker notes`.

---

## 1. Cuatro técnicas, una sola idea

### Content

**Cuatro técnicas distintas y una sola idea de fondo: todas hacen que el modelo escriba más antes de responder.**

- **Chain of Thought (CoT)** Razonamiento paso a paso antes de la respuesta.
- **Self-consistency** Varias respuestas independientes y voto por mayoría.
- **Tree of Thought (ToT)** Ramas exploradas en paralelo, con poda de las peores.
- **Prompt chaining** Una secuencia de prompts simples encadenados.

- 🎯 **Cada una compra calidad con un recurso distinto.** CoT agrega pasos, self-consistency agrega muestras, ToT agrega ramas y el encadenamiento agrega llamadas. Todas se pagan.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 26)

### Speaker notes

Mapa de la sección. Cuatro técnicas y una sola idea de fondo, que se explica recién al final: todas hacen que el modelo escriba más antes de responder. Conviene anticipar ese cierre acá, porque le da sentido al recorrido y evita que se lea como una lista de recetas sueltas. Dos precisiones que no están en la lámina y vale decir en voz alta. Una: lo que CoT fuerza son tokens intermedios que condicionan la predicción final, y por eso funciona. La otra: self-consistency se queda con la respuesta más frecuente y con eso reduce el error por no-determinismo, que es un problema distinto del de razonar mal. El recuadro de cierre es el que ordena la sección entera: cada técnica compra calidad con un recurso distinto, y ninguna la compra gratis.

---

## 2. Chain of Thought (CoT)

### Content

**Mostrarle al modelo el razonamiento paso a paso, no solo el resultado. Es pensar en voz alta.**

![Cot salto vs cadena](images/s5-2-1-cot-salto-vs-cadena.svg)
<!-- ascii-source:
  SIN CoT
  +-----------+                                        +------------+
  | pregunta  | -------------------------------------&gt; | respuesta  |
  +-----------+           un solo salto                +------------+
                    nada escrito entre medio

  CON CoT
  +-----------+    +--------+    +--------+    +--------+    +------------+
  | pregunta  | -> | paso 1 | -> | paso 2 | -> | paso 3 | -> | respuesta  |
  +-----------+    +--------+    +--------+    +--------+    +------------+
                       |             |             |
                       +-------------+-------------+
                         cada paso escrito entra al contexto
                         y condiciona la prediccion del siguiente

  Los tokens intermedios no son la explicacion de la respuesta:
  son el calculo que la produce.
-->
<!-- ascii-note:
intent: mostrar que CoT no agrega una explicacion al final sino pasos escritos EN EL MEDIO, y que cada paso escrito entra al contexto y condiciona el siguiente; contrastar con el salto unico de la version sin CoT
emphasize: el contraste entre la flecha larga sin nada en el medio y la cadena de pasos; la llave que muestra que cada paso realimenta el contexto; la linea de cierre que es la tesis de la clase
labels: "SIN CoT", "CON CoT", "pregunta", "paso 1/2/3", "respuesta", "un solo salto", "cada paso escrito entra al contexto", y la linea de cierre sobre los tokens intermedios
-->

- **Instrucción directa** Pedirle que razone antes de responder, en el propio prompt.
- **Ejemplos con razonamiento explícito** Dar ejemplos donde se ve el proceso de resolución, no solo la respuesta final.

- 🔗 CoT e in-context learning son la misma familia: few-shot CoT es ICL donde los ejemplos incluyen el razonamiento. ICL enseña qué responder; CoT enseña cómo razonar.

- 💡 Con thinking disponible, la instrucción general ("pensar a fondo") rinde más que un plan paso a paso escrito a mano. El CoT manual queda como *fallback* para cuando el thinking está apagado.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 27)
- `chain-of-thought-wei.web.md` — Wei et al. (2022), la fuente primaria de CoT. El abstract declara *state of the art* en GSM8K con 8 ejemplares de cadena de pensamiento, **sin dar el porcentaje**: por eso las cifras de esta slide son de los dos papers que construyen sobre CoT y sí publican números.
- `self-consistency-wang.web.md` — Wang et al. (2022): +17,9% en GSM8K y +11,0% en SVAMP, **mejoras relativas al baseline de CoT**, no accuracy absoluta.

### Speaker notes

Esta slide cambió respecto del deck original y conviene contar por qué, porque enseña método. El deck afirmaba 70% de mejora en precisión y 35% menos errores en código, y esas dos cifras no salen de ninguna fuente: son plausibles, suenan bien y no existen. Las que están ahora sí tienen paper. Al leerlas, marcá la trampa: son mejoras **sobre CoT**, no accuracy absoluta. Decir "self-consistency alcanza 17,9% en GSM8K" es leer mal el abstract, y es el error más común con esas cifras. El salto de 4% a 74% del Game of 24 es el número más impresionante de toda la clase y vale detenerse: mismo modelo, mismo problema, solo cambia la estrategia de inferencia. La última línea conecta con la sección anterior y sirve de puente.

---

## 3. Chain of Thought: ejemplo

### Content

**El mismo cálculo con y sin pasos escritos. Las dos respuestas coinciden y solo una se puede auditar.**

```markdown
### Sin CoT
Prompt:    ¿Cuánto es el 15% de propina sobre una cuenta de $47,83?
Respuesta: $7,17

### Con CoT
Prompt:    ¿Cuánto es el 15% de propina sobre una cuenta de $47,83?
           Pensá paso a paso.
Respuesta: 10% de 47,83 = 4,78
           5% es la mitad de eso = 2,39
           15% = 4,78 + 2,39 = 7,17
```

- **Sin CoT** Llega el número y hay que creerle.
- **Con CoT** Cada paso queda escrito y el error se ve donde ocurre.

- 💡 En revisión de código y análisis de incidentes, CoT produce un rastro que otra persona puede seguir. Cuesta más latencia, porque la salida es más larga.

<!-- enlace de la forma: https://aitutorial.dev/prompting/advanced-techniques -->
- [Ejemplo interactivo en aitutorial.dev →](https://aitutorial.dev/prompting/advanced-techniques)

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 28)
- `aitutorial-advanced-techniques.web.md`
- `chain-of-thought-wei.web.md` — Wei et al. (2022).

### Speaker notes

El ejemplo es trivial a propósito y hay que decirlo, porque la pregunta obvia es por qué molestarse con una cuenta de una línea. La respuesta está en la fila de abajo: las dos respuestas son iguales, lo que cambia es que una se puede auditar. Sin los pasos escritos, el razonamiento tampoco se puede depurar: cuando el modelo se equivoca queda un número mal y ninguna pista. Con CoT, el error está en el paso 2 y se ve. Trasladalo al terreno de ellos con un ejemplo hablado: un modelo que dice "este diff no introduce bugs" es inútil; uno que enumera lo que revisó y por qué descartó cada riesgo es revisable. La contra que hay que nombrar es la latencia, y se cuantifica dos slides más adelante.

---

## 4. Self-consistency: votación

### Content

**Una sola respuesta puede estar mal por no-determinismo o por ambigüedad del prompt. Self-consistency genera varias respuestas independientes y vota entre ellas.**

![Self consistency votacion](images/s5-4-1-self-consistency-votacion.svg)
<!-- ascii-source:
                        UN MISMO PROMPT
                               |
          +----------+---------+---------+----------+
          |          |         |         |          |
          v          v         v         v          v
       camino 1   camino 2  camino 3  camino 4   camino 5
       (muestreo independiente, con temperatura > 0)
          |          |         |         |          |
          v          v         v         v          v
         "A"        "A"       "B"       "A"        "A"
          |          |         |         |          |
          +----------+----+----+---------+----------+
                          |
                          v
                  +-----------------+
                  |    VOTACION     |
                  +-----------------+
                          |
                          v
                  "A"  --  4 de 5  --  confianza 80%

  Los caminos correctos convergen; los equivocados divergen entre si.
-->
<!-- ascii-note:
intent: mostrar self-consistency como un fan-out y un fan-in sobre el MISMO prompt: se muestrean varios caminos de razonamiento independientes y se agrega el resultado por frecuencia, no por calidad individual
emphasize: la simetria abanico-que-abre / abanico-que-cierra; el camino 3 disidente ("B"), que es lo que el metodo detecta y una sola llamada esconde; la caja de VOTACION como punto de convergencia
labels: "UN MISMO PROMPT", "camino 1..5", "muestreo independiente, con temperatura > 0", las salidas "A"/"B", "VOTACION", "4 de 5 -- confianza 80%", y la linea de cierre sobre convergencia
-->

**Cuándo usarlo**

- **Alto riesgo** Un deploy, una migración de datos, un cambio en facturación.
- **Razonamiento complejo** Varias cadenas de pensamiento pueden divergir.
- **Clasificación con confianza** Importa cuán seguro está el modelo.
- **Validación previa** Medirlo siempre en el eval set propio.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 29)
- `self-consistency-wang.web.md` — Wang et al. (2022). El paper la presenta como **estrategia de decodificación**, no como técnica de prompting: reemplaza la decodificación greedy por muestreo diverso más marginalización sobre los caminos. "Votación por mayoría" es una glosa didáctica, no el término del abstract.

### Speaker notes

Antes del diagrama, el número que sostiene la decisión y que ya no está en la lámina: cinco llamadas cuestan cinco veces, la precisión mejora de forma medible, y CoT más self-consistency combinados dan ganancias adicionales (Wang et al., 2022). Precisión terminológica que vale la pena hacer, porque ordena la cabeza: self-consistency no es un prompt distinto, es una forma distinta de muestrear y agregar las salidas del mismo prompt. El paper habla de marginalizar sobre los caminos de razonamiento; "votación por mayoría" es cómo lo explicamos, y funciona como explicación. La intuición que lo sostiene es elegante: un problema difícil admite varios caminos correctos que convergen a la misma respuesta, y los caminos equivocados divergen entre sí. Si tres de cinco muestras coinciden, esa coincidencia es señal. De la tercera viñeta vale sacar el matiz que la lámina ya no dice: lo que se gana es saber cuán seguro está el modelo, y no solamente qué respondió. La cuarta es la más importante para producción y suele saltearse: las ganancias no son universales, hay tareas donde cinco muestras dan cinco respuestas distintas, y ahí la votación no agrega nada más que costo.

---

## 5. Self-consistency: ejemplo

### Content

**Tres corridas independientes del mismo prompt sobre el mismo diff, y una votación.**

<!-- ascii-render: documentation-only -->
```
# CASO
Diff en billing/invoice.py:
-   total = subtotal + tax
+   total = subtotal + tax * quantity

Pregunta: ¿este diff introduce un bug?

# RUN 1
SI. tax ya viene calculado sobre el subtotal completo.
Multiplicarlo por quantity lo cobra de mas.

# RUN 2
SI. Mismo razonamiento: doble conteo de la cantidad.

# RUN 3
NO. Si tax fuera un monto unitario, el cambio seria correcto.

# RESULTADO (votacion)
-> SI, introduce un bug   (2 de 3 votos)
-> Confianza: 67%
```

- **Cuándo usarlo** Cambios donde el error sale caro y el razonamiento admite más de un camino.
- **Costo** Tres a cinco llamadas al modelo, es decir tres a cinco veces el precio y la latencia.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 30)
- `self-consistency-wang.web.md` — Wang et al. (2022).

### Speaker notes

Lo interesante del ejemplo es la corrida 3, y conviene señalarla. No es una alucinación: es una lectura distinta y coherente del mismo diff, bajo un supuesto distinto sobre qué representa `tax`. Eso es lo que self-consistency detecta y lo que una sola llamada esconde. La confianza del 67% no es una probabilidad calibrada, es la proporción de votos, y conviene decirlo para que nadie la reporte como si fuera otra cosa. El uso práctico en un equipo: cuando la votación no es unánime, el sistema no decide, escala a una persona. Ese es el valor real, más que el voto en sí.

---

## 6. Tree of Thought (ToT)

### Content

**ToT extiende CoT explorando varios caminos de razonamiento en paralelo, como las ramas de un árbol de decisión. El modelo evalúa cada rama y elige la más prometedora.**

![Arbol ramificar podar](images/s5-6-1-arbol-ramificar-podar.svg)
<!-- ascii-source:
                        [ problema ]
                             |
              +--------------+--------------+        1. GENERAR
              |              |              |           ramas
              v              v              v
          [ rama A ]     [ rama B ]     [ rama C ]
           score 8         score 5        score 2      2. EVALUAR
              |              |              X             cada rama
              |              |           podada
       +------+------+       X
       |             |    podada                       3. EXPANDIR
       v             v                                    la mejor
   [ A.1 ]        [ A.2 ]
   score 9        score 4
       |             X
       |          podada
       v
   [ solucion ]                                       4. SELECCIONAR

  CoT es este arbol con una sola rama y sin vuelta atras.
-->

**Limitaciones**

- **Costo** Cuesta bastante más que un CoT lineal.
- **Implementación** Hay que generar ramas, puntuarlas y podar.
- **Cuándo rinde** Sirve si el problema admite varias soluciones posibles.
- **Cuándo no** En tareas simples el overhead no se justifica.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 33)
- `tree-of-thoughts-yao.web.md` — Yao et al. (2023), NeurIPS 2023. ToT generaliza CoT: la unidad de decisión deja de ser el token y pasa a ser el *thought*, una unidad coherente de texto. Habilita autoevaluación, lookahead y backtracking. Game of 24 con GPT-4: CoT 4% → ToT 74%.

### Speaker notes

El árbol de la lámina es el punto entero de la técnica, así que caminalo: se generan varias ramas, cada una recibe un score, las malas se podan y solo la mejor se expande. Marcá que CoT es este mismo árbol con una sola rama y sin vuelta atrás. El aporte teórico del paper vale la pena decirlo porque reordena todo lo anterior: la generación autoregresiva decide token por token y de izquierda a derecha, sin manera de volver atrás, y si el primer paso fue malo el resto está condenado. ToT cambia la unidad de decisión: en vez de tokens, pensamientos completos, y con eso aparecen dos operaciones que CoT no tiene, mirar hacia adelante y retroceder. Recordá el número de la slide de CoT: 4% a 74% en Game of 24, mismo modelo. La analogía médica del deck original se reemplazó por el ejemplo de refactor de la slide siguiente.

---

## 7. Tree of Thought: ejemplo

### Content

**Tres estrategias de refactor generadas por el modelo, evaluadas una por una y podadas hasta quedarse con la mejor.**

<!-- ascii-render: documentation-only -->
```
# CASO
El modulo billing/invoice.py tiene 1.400 lineas, 38 metodos y ningun test.
Hay que agregarle IVA por jurisdiccion sin romper la facturacion actual.

# INSTRUCCION (Tree of Thought)
1. Genera 3 estrategias de refactor posibles
2. Evalua evidencia a favor y en contra de cada una
3. Elegi la mas prometedora y justifica
```

**Razonamiento del modelo**

- **Rama A: módulo de impuestos aparte** Aísla el cambio y el riesgo queda acotado. **Seleccionada.**
- **Rama B: reescribir el módulo con tests** Lo más limpio a largo plazo, y sin tests previos no hay red.
- **Rama C: condicionales in situ** Lo más rápido, y suma complejidad a un módulo que ya no la tolera.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 34)
- `tree-of-thoughts-yao.web.md` — Yao et al. (2023).

### Speaker notes

Este ejemplo funciona porque las tres ramas son defendibles, y eso es justo el tipo de problema donde ToT rinde. Un problema con una sola respuesta correcta no necesita ramas. Lo que hace ganar a la rama A es que permite testear la parte nueva sin tocar lo viejo, así que el riesgo queda acotado; el criterio no es la elegancia. La rama B es la trampa útil: es la respuesta que da un modelo sin evaluación de ramas porque es la más limpia en abstracto, y es la peor decisión concreta porque rompe la mayor superficie de una sola vez y no hay tests que sostengan la reescritura. La rama C queda descartada por complejidad ciclomática sobre un módulo que ya no la tolera. Si querés hacerlo participativo, mostrá las tres ramas sin la selección y pediles que elijan. La discusión que se arma es el trabajo que hace ToT.

---

## 8. Prompt chaining

### Content

**Dividir una tarea compleja en una secuencia de prompts simples, donde el output de cada paso alimenta al siguiente. Cada paso es más preciso porque se enfoca en una sola sub-tarea.**

**Ejemplo: pipeline de triage de tickets**

![Cadena cuatro etapas](images/s5-8-1-cadena-cuatro-etapas.svg)
<!-- ascii-source:
  [ ticket ]
      |
      v
  +---------------+  urgencia     +---------------+  detalles
  | 1 CLASIFICAR  | ------------&gt; | 2 EXTRAER     | -----------+
  |   urgencia    | alta/med/baja |   detalles    |            |
  +---------------+               +---------------+            |
    modelo chico                    modelo chico               |
                                                               v
  +---------------+  runbooks     +---------------+            |
  | 4 REDACTAR    | <------------ | 3 BUSCAR      | <----------+
  |   respuesta   |  + contexto   |   (RAG)       |
  +---------------+               +---------------+
    modelo caro                     sin modelo
      |
      v
  [ respuesta estructurada ]

  La salida de cada paso ES la entrada del siguiente.
  El modelo caro entra solo en el paso 4, con el contexto ya filtrado.
-->
<!-- ascii-note:
intent: mostrar el encadenamiento como una tuberia de etapas donde la salida de cada una es la entrada de la siguiente, y hacer visible por que sale mas barato: los pasos baratos filtran antes de que intervenga el modelo caro
emphasize: las flechas etiquetadas entre etapas (urgencia, detalles, runbooks, contexto), que son el dato concreto que viaja; la anotacion de que modelo usa cada paso, con el caro solo al final
labels: "ticket", "1 CLASIFICAR urgencia", "2 EXTRAER detalles", "3 BUSCAR (RAG)", "4 REDACTAR respuesta", "modelo chico / sin modelo / modelo caro", "respuesta estructurada"
-->

- 🎯 **Prompt chaining convierte tareas imposibles en secuencias manejables. Es la base de los agentes de IA modernos.**

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 35) — el párrafo de definición está truncado a mitad de palabra en el original: "…se ejecutan varias llamadas en vez de una lo cual **incre**" (corpus §Raw excerpts [35], inconsistencia 22). La frase no se pudo reponer verbatim porque el corpus la preserva igual de truncada; el cierre se reformuló con el trade-off que la propia slide 5.13 declara (más latencia y más llamadas, a cambio de pasos simples y evaluables).

### Speaker notes

El texto de esta slide venía cortado a mitad de palabra en el deck original y no se pudo reponer verbatim, porque el material fuente está igual de cortado. Lo que decía la frase se deduce de la propia slide de ejemplo: varias llamadas en vez de una incrementan latencia y costo total de orquestación, a cambio de que cada paso sea simple y evaluable por separado. Decilo así. El otro punto es el de la línea de cierre y es el más importante de la slide: un pipeline de cinco pasos con lógica de control escrita por el programador ya es, en lo esencial, un agente con el bucle fijo. La diferencia con un agente de verdad es quién decide el próximo paso, y eso es lo que agrega ReAct, que acaban de ver.

---

## 9. Prompt chaining: ejemplo

### Content

<!-- ascii-render: documentation-only -->
```
# PASO 1 -- Clasificar urgencia
Input:  ticket del usuario
-> Output: ALTA / MEDIA / BAJA

# PASO 2 -- Extraer detalles
Input:  ticket + clasificacion
-> Output: componente afectado, version, pasos para reproducir

# PASO 3 -- Buscar en la base de conocimiento (RAG)
Input:  detalles extraidos
-> Output: incidentes previos parecidos, runbooks aplicables

# PASO 4 -- Generar respuesta
Input:  todo lo anterior
-> Output: respuesta estructurada para el equipo de guardia
```

| Ventajas | Trade-offs |
|---|---|
| **Debugging:** se identifica en qué paso falló, no solo que falló. | Más latencia: las llamadas son secuenciales. |
| **Resiliencia:** los pasos que fallan se reintentan por separado. | El código de orquestación es más complejo. |
| **Optimización:** cada prompt se ajusta a su tarea, y los pasos caros se llaman solo cuando hacen falta. | Varias llamadas al modelo, aunque el total suele salir más barato. |
| **Escalabilidad:** cada paso se evalúa y se mejora por separado. | |

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 36)

### Speaker notes

La tercera ventaja es la que suele sorprender, y merece medio minuto: encadenar es más barato aunque haya más llamadas. La razón es que el paso 1 corre con un modelo chico sobre doscientos tokens, y el modelo caro solo se invoca en el paso 4 y con el contexto ya filtrado. Un prompt monolítico manda todo al modelo caro siempre. Es el mismo argumento del cascading, aplicado a las etapas en vez de a los modelos. La contra real es la de la primera fila de la derecha: cuatro llamadas secuenciales son cuatro latencias sumadas, y en un flujo interactivo eso se nota. Si el sistema es asincrónico, no importa.

---
## 10. Las cuatro técnicas: pros y contras

### Content

| Técnica | Pros | Contras |
|---|---|---|
| **Chain of Thought (CoT)** | Razonamiento auditable, mejora la precisión, los errores se detectan. | Más latencia y más costo; poco útil en tareas simples; no garantiza corrección. |
| **Self-consistency** | Reduce el error por no-determinismo; da una señal de confianza. | Multiplica el costo por 3 a 5 llamadas; más latencia. |
| **Tree of Thought (ToT)** | Explora varios caminos; mejor que CoT en planificación. | Muy costoso; complejo de implementar; difícil de controlar. |
| **Prompt chaining** | Pasos simples y reintentables; fácil de evaluar y mejorar. | Más latencia total; código de orquestación más complejo. |

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 37)
- `research/web/anthropic-docs-effort/page.md` y `research/web/anthropic-docs-adaptive-thinking/page.md` — para la fila de thinking nativo.

### Speaker notes

Tabla de referencia, para consultar más que para leer. Si hay que decir una sola cosa, que sea el patrón de la columna de la derecha: todas las contras son la misma contra escrita de cuatro maneras, que es más tokens o más llamadas. Ninguna técnica de esta sección compra calidad gratis. Y una lectura transversal útil: las dos primeras filas mejoran cómo piensa el modelo, las dos últimas cambian la arquitectura del sistema alrededor. Las primeras son un cambio de prompt, las segundas son un cambio de diseño, con todo lo que eso implica para el equipo que lo mantiene.

---

## 11. ¿Por qué tardan más?

### Content

**Más calidad cuesta tiempo de cómputo: más tokens generados, más segundos. No es magia, es aritmética.**

| Técnica | Efecto en latencia |
|---|---|
| **Chain of Thought (CoT)** | Genera 100 a 500 tokens de razonamiento antes de la respuesta. Latencia 2 a 5 veces mayor. |
| **Self-consistency** | Corre el mismo prompt N veces (5 a 10). Latencia y costo: N veces una sola llamada. |
| **Tree of Thought (ToT)** | Proporcional a la cantidad de ramas evaluadas: 3 a 5 veces CoT en los casos habituales. |
| **Prompt chaining** | Cada paso es una llamada independiente. Un pipeline de 5 pasos suma 5 latencias más el procesamiento intermedio. |

- 🎯 **Usar estas técnicas solo cuando la precisión justifica el costo. Para tareas simples, un prompt directo es más eficiente.**

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 39) — la tabla de latencia por técnica, con sus rangos verificados en §Raw excerpts [39] y en la tabla de cifras del registro.
- `research/web/inference-time-scaling/page.md` — Balachandran et al., Microsoft Research, *Inference-Time Scaling for Complex Tasks: Where We Stand and What Lies Ahead*, arXiv:2504.00294 (31 mar 2025). "the advantages of inference-time scaling vary across tasks and diminish as problem complexity increases. In addition, simply using more tokens does not necessarily translate to higher accuracy in these challenging regimes"; Apéndice C (GPQA Diamond): "Claude 3.7 Sonnet spends 3x more tokens than O3-mini, which in turn spends 2x more tokens than O1, while all these models perform in a very similar accuracy range." Derivación usada en las notas del orador: 6× = 3× (Sonnet 3.7 vs O3-mini) × 2× (O3-mini vs O1), Sonnet 3.7 contra O1 — `research/web/inference-time-scaling/page.md`, Apéndice C.

### Speaker notes

Esta slide es el contrapeso de las anteriores y por eso va acá, justo después de la que explica por qué funcionan. La regla del cierre es la que se llevan escrita. Un detalle que conviene marcar porque cambia decisiones de producto: la latencia de self-consistency es N veces solo si las llamadas van en serie, y no tienen por qué. Cinco muestras en paralelo cuestan cinco veces en plata y una vez en tiempo. Es de las pocas veces en que se puede comprar calidad sin pagar latencia. La advertencia nueva es la que cierra la sección con honestidad y evita que se vayan pensando que más razonamiento siempre es mejor. Tres modelos, uno gastando seis veces más tokens que el otro, y la precisión queda en el mismo rango. Si alguien te pregunta cuál elegir, esa comparación es la respuesta: mide en tu tarea, porque el gasto de tokens no predice la calidad.

---

## 12. ¿Por qué funcionan?

### Content

**El LLM no piensa: predice tokens de izquierda a derecha, y cada uno depende solo de los anteriores. No hay motor de razonamiento oculto, así que lo escrito en la respuesta es el razonamiento.**

- **Los tokens intermedios son cálculo** Cada paso escrito condiciona la predicción del siguiente.
- **Más contexto, mejor predicción** Un razonamiento de 200 tokens guía mejor que un prompt de 10.
- **Se achica el espacio de error** Cada paso recorta la incertidumbre antes de la conclusión.

- 💡 Es la diferencia entre resolver un problema de cabeza y resolverlo escribiéndolo en papel. El papel no vuelve más inteligente a nadie, y hace la cuenta más precisa.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 38) — argumento completo en §Raw excerpts [38].
- `chain-of-thought-wei.web.md` — Wei et al. (2022).
- `tree-of-thoughts-yao.web.md` — Yao et al. (2023): el diagnóstico de partida del paper es la decisión "a nivel de token y de izquierda a derecha" durante la inferencia.
- `research/web/deepseek-r1-nature/page.md` — evidencia empírica del mismo argumento: durante el entrenamiento por refuerzo el largo promedio de la respuesta crece por sí solo mientras sube la precisión (Fig. 1b).

### Speaker notes

Esta es la slide de la tesis y merece el tiempo que haga falta. Todo lo que vieron en la sección se explica desde acá: si el modelo genera token por token y cada token se condiciona solo con lo anterior, entonces escribir los pasos no es documentar el razonamiento, es hacerlo. Los tokens intermedios son cómputo en sentido estricto: son estados que el modelo puede leer para producir el siguiente, y funcionan como memoria de trabajo explícita. Por eso pedirle que piense paso a paso funciona, y por eso pedirle que "sea más cuidadoso" no funciona. El tercer argumento se entiende mejor por contraste: sin CoT el modelo tiene que saltar directo a la respuesta, y cada paso intermedio que escribe le baja la incertidumbre acumulada antes de la conclusión. La analogía del papel es la que engancha, y tiene un matiz que conviene decir: el papel no agrega inteligencia, agrega memoria de trabajo. Ahora tienes además un argumento empírico que antes no estaba, y es el más fuerte de la sección: en el paper de DeepSeek el modelo alarga sus respuestas solo, sin que nadie se lo pida, a medida que aprende a acertar. Si escribir más pasos no fuera cómputo, alargar no le daría ninguna ventaja. Si te queda tiempo, cierra volviendo a la slide del motor de completado del principio, porque es la misma idea vista dos horas antes.

---

# 6. Effort y thinking

**Goal of this section:** Separar cuatro cosas que comparten la palabra "thinking" y que hoy se pisan en el deck: el mecanismo por el que el modelo escribe un bloque de razonamiento, el entrenamiento por refuerzo del que salió ese comportamiento, el parámetro `effort` que gradúa cuánto gasta al responder, y las etiquetas `<thinking>` que se escriben en el prompt. Cierra recapitulando las técnicas de la sección anterior con su costo en latencia.

- [closed] 2026-09-01 — "La sección 6 tiene demasiado texto. Está bien agregar láminas si hace falta."
  Resolution: la sección pasó de 9 a 13 láminas, sin borrar contenido. Cuatro particiones: 'Thinking: el mecanismo' soltó la deprecación de `budget_tokens` a la nueva 6.3; 'Effort: un parámetro de la petición' soltó la tabla de niveles a la nueva 6.8; 'Pedirle al modelo que piense' soltó las tres frases verbatim a la nueva 6.10; y 'Qué cuesta el thinking' soltó la facturación y el caché a la nueva 6.13. En las nueve láminas preexistentes los ítems de dos y tres oraciones se cortaron a etiqueta más una línea, y la prosa que sacaron bajó a `### Speaker notes`. Los tres diagramas ASCII, sus `ascii-note` y el bloque de código quedaron intactos byte por byte. La lámina 'Etiquetas `<thinking>` en el prompt' no se repuso.

---

## 1. Cuatro palabras, cuatro cosas

### Content

**La palabra "thinking" aparece en cuatro lugares de esta clase. En cada uno significa algo distinto, y confundirlos es lo que hace incomprensible la documentación.**

- **El mecanismo** El modelo escribe un bloque de razonamiento antes de la respuesta y decide en cada petición si piensa.
- **El parámetro `effort`** Viaja en `output_config` y gradúa cuántos tokens gasta el modelo al responder.
- **Los modos de la interfaz** "Thinking" y "Deep Thinking" son nombres de producto, ajenos al vocabulario de la API.
- **Las etiquetas `<thinking>`** Una técnica de prompting que funciona en cualquier modelo, sin tocar un solo parámetro.

- 🎯 **Los cuatro descansan sobre el mismo hecho.** El modelo escribe pasos intermedios antes de responder, y esos pasos son el cómputo.

![Mapa desambiguacion thinking](images/s6-1-1-mapa-desambiguacion-thinking.svg)
<!-- ascii-source:
        LA MISMA PALABRA EN CUATRO LUGARES DISTINTOS

  +-------------------------------+  +-------------------------------+
  | MECANISMO            [API]    |  | PARAMETRO effort     [API]    |
  | thinking: {"adaptive"}        |  | output_config.effort          |
  | el modelo escribe un bloque   |<-| gradua cuanto gasta el modelo |
  | de razonamiento y decide      |  | al responder; es la perilla   |
  | por peticion si piensa        |  | de profundidad del thinking   |
  +-------------------------------+  +-------------------------------+

  +-------------------------------+  +-------------------------------+
  | MODOS DE INTERFAZ  [producto] |  | ETIQUETAS <thinking> [prompt] |
  | "Thinking" / "Deep Thinking"  |  | se escriben en el prompt      |
  | nombres de las apps de chat   |  | tecnica de prompting          |
  | NO son vocabulario de la API  |  | sirve en cualquier modelo     |
  +-------------------------------+  +-------------------------------+

  COMUN A LOS CUATRO: el modelo escribe pasos intermedios antes de
  responder. Esos pasos son el computo.
-->
<!-- ascii-note:
intent: mapa de desambiguacion; cuatro cuadrantes etiquetados por donde vive cada cosa (API, producto, prompt), con una flecha del parametro effort al mecanismo porque es la perilla que lo gradua
emphasize: la etiqueta de origen de cada cuadrante ([API] / [producto] / [prompt]); el cuadrante "MODOS DE INTERFAZ" debe verse como el ajeno al resto; la linea de cierre comun a los cuatro
labels: MECANISMO, PARAMETRO effort, MODOS DE INTERFAZ, ETIQUETAS <thinking>
-->

### Sources

- `research/web/anthropic-docs-effort/page.md` — `effort` se setea en `output_config.effort`; "Where adaptive thinking is available, effort is the recommended way to control thinking depth"; `adaptive` es un modo de thinking y no un valor de effort.
- `research/web/anthropic-docs-adaptive-thinking/page.md` — el thinking es adaptativo y el modelo decide por petición si piensa y cuánto.
- `aitutorial-structured-prompt-engineering.web.md` — las etiquetas `<thinking>` como técnica de prompt de la familia Claude.
- "Thinking" y "Deep Thinking" vienen de la lámina importada de `talksmith-mim/talks/hiperparametros-ai/final.md` y no figuran en ninguna de las tres capturas de la documentación de la plataforma.

### Speaker notes

Esta lámina existe porque la clase venía usando la misma palabra para cuatro cosas y el bloque entero se volvía incomprensible. Dedícale tiempo. El orden importa: primero el mecanismo, que es lo que el modelo hace; después el parámetro, que es lo que configuras en la petición; tercero los modos de la interfaz, que son nombres comerciales y conviene decir en voz alta que no aparecen en la documentación de la API; y último las etiquetas del prompt, que son la técnica más vieja de las cuatro y la única que funciona en cualquier modelo. Tres precisiones que la lámina ya no carga y conviene decir. El mecanismo, en los modelos actuales de Anthropic, es adaptativo: el modelo decide por petición si piensa y también cuánto. El parámetro no es una perilla suelta: donde hay razonamiento adaptativo, la documentación lo señala como la forma recomendada de controlar la profundidad del thinking. Y de los modos de interfaz, lo que importa es que ni "Thinking" ni "Deep Thinking" figuran en la documentación de la plataforma. Lo que separa a los cuatro es quién pide los pasos intermedios y quién los paga. Si alguien pregunta por qué la interfaz usa nombres distintos de la API, la respuesta honesta es que son capas de producto distintas y que los nombres comerciales cambian seguido. La línea de cierre es la que sostiene toda la sección: los cuatro se apoyan en el mismo hecho, que el modelo escribe pasos intermedios y esos pasos son el cómputo. Es la tesis de la clase, dicha por cuarta vez.

---

## 2. Thinking: el mecanismo

### Content

**El modelo produce un bloque de razonamiento antes de la respuesta. En los modelos actuales el thinking es adaptativo, así que el modelo evalúa cada petición y decide solo si piensa y cuánto.**

- **La decisión es por petición** Una pregunta factual simple vuelve sin bloque; un problema de varios pasos lo dispara.
- **El código no puede asumir el bloque** Una misma conversación mezcla turnos con y sin thinking.
- **El bloque viaja aparte de la respuesta** Llega con tipo propio, distinto del texto, y `display` decide si vuelve resumido o vacío.
- **También piensa entre herramientas** Razona entre llamadas y evalúa cada resultado antes de decidir el paso siguiente.

![Thinking bifurcacion peticion](images/s6-2-1-thinking-bifurcacion-peticion.svg)
<!-- ascii-source:
                LO QUE PASA EN UNA PETICION

   +----------+     +----------------------+
   |  prompt  | --&gt; | el modelo evalua la  |
   +----------+     | dificultad y decide  |
                    +----------------------+
                       |                |
        tarea simple   |                |  tarea de varios pasos
        no piensa      |                v
                       |     +------------------------+
                       |     | BLOQUE DE THINKING     |
                       |     | tipo propio, aparte    |
                       |     | del texto              |
                       |     | display: summarized    |
                       |     |          u omitted     |
                       |     +------------------------+
                       |                |
                       v                v
              +------------------------------------+
              |       TEXTO DE LA RESPUESTA        |
              +------------------------------------+

   max_tokens es el techo duro de TODA la salida: thinking + texto
-->
<!-- ascii-note:
intent: mostrar que el thinking es una rama condicional decidida por el modelo dentro de una misma peticion, y que el bloque de razonamiento es una salida separada del texto
emphasize: la bifurcacion (tarea simple no genera bloque), el bloque de thinking como caja aparte, y la linea de max_tokens que abarca las dos salidas
labels: prompt, evaluacion, BLOQUE DE THINKING, TEXTO DE LA RESPUESTA, max_tokens
-->

### Sources

- `research/web/anthropic-docs-adaptive-thinking/page.md` — el thinking es adaptativo; la decisión ocurre por petición; los turnos del asistente no necesitan arrancar con un bloque de thinking; el thinking se intercala con el uso de herramientas sin beta header ni configuración adicional; `max_tokens` es el tope duro de la salida total, thinking más texto.

### Speaker notes

Esta es la lámina del mecanismo, y la palabra que hay que fijar es "adaptativo". El modelo decide, petición por petición, si le conviene pensar. La consecuencia práctica que más les va a servir en un trabajo real son los dos primeros bullets juntos: si escribes código que asume que todo turno del asistente empieza con un bloque de thinking, se te rompe el día que el modelo decide que la pregunta era fácil. La documentación es explícita en que eso es válido y esperable. Del tercero, el detalle útil es que el bloque llega con un tipo propio, así que se lo trata aparte del texto en el parseo. Del cuarto, que el razonamiento entre herramientas no necesita ninguna configuración extra en los modelos adaptativos. Cierra con `max_tokens`, que es el techo duro y cubre las dos salidas juntas; vuelves sobre eso en la lámina de costo.

---

## 3. El presupuesto fijo quedó atrás

### Content

**`budget_tokens` fijaba un techo de tokens de pensamiento. Los modelos actuales lo reemplazaron por thinking adaptativo más `effort`, y la migración depende de qué modelo se esté usando.**

- **En los 4.6** Está deprecado, y las peticiones todavía funcionan.
- **Desde los 4.7** La API lo rechaza con error 400.
- **En los 4.5 y anteriores** Sigue siendo el único modo disponible en los modelos que soportan thinking.
- **La migración** Sacar `budget_tokens`, poner `thinking: {"type": "adaptive"}` y graduar con `output_config.effort`.

### Sources

- `research/web/anthropic-docs-extended-thinking/page.md` — `thinking.type: "enabled"` con `budget_tokens` está deprecado en los modelos 4.6 (las peticiones todavía funcionan) y los 4.7 en adelante lo rechazan con error 400; en los 4.5 y anteriores que soportan thinking es el único modo disponible; la migración consiste en sacar `budget_tokens`, poner `thinking: {"type": "adaptive"}` y controlar la profundidad con `output_config.effort`.

### Speaker notes

Esta lámina ordena la confusión con los tutoriales viejos, y por eso vale la pena aunque parezca menor. Si buscan "extended thinking" en Google van a encontrar `budget_tokens`, que era un techo fijo de tokens de pensamiento y hoy ya no es el camino. Explica el estado actual sin exagerar, porque las tres filas dicen cosas distintas: en los 4.6 está deprecado y las peticiones todavía andan, los 4.7 en adelante devuelven un 400, y en los 4.5 y anteriores sigue siendo el único modo que hay. Esa última fila es la que evita que alguien "migre" un modelo viejo y lo rompa. La migración en sí es de tres líneas y conviene escribirla en la pizarra si alguien pregunta: se saca `budget_tokens`, se pone el modo adaptativo y la profundidad pasa a graduarse con effort, que es la lámina que viene después de las de entrenamiento.

---

## 4. Cómo se aprendió a razonar

### Content

**DeepSeek-R1, publicado en Nature en 2025, mostró que las capacidades de razonamiento se pueden incentivar con refuerzo puro, sin trayectorias de razonamiento anotadas por humanos.**

- **Sin ejemplos de razonamiento humano** El trabajo saltea el ajuste supervisado previo al refuerzo.
- **La señal premia solo el resultado** Se mide la predicción final contra la respuesta verdadera, sin mirar el proceso.
- **Los patrones emergen** Autorreflexión, verificación y cambio de estrategia aparecen sin que nadie los enseñe.
- **Los números** En AIME 2024 el pass@1 promedio va de 15,6% a 77,9%; con self-consistency llega a 86,7%.

- 🎯 **La self-consistency de la sección anterior aparece acá como técnica de evaluación.**

![Curva refuerzo deepseek](images/s6-4-1-curva-refuerzo-deepseek.svg)
<!-- ascii-source:
      DEEPSEEK-R1-ZERO DURANTE EL ENTRENAMIENTO POR REFUERZO
      (AIME 2024, pass@1 promedio)

  100% |
       |                                          86,7%  <- con
   80% |                              77,9%  <-*  self-consistency
       |                        _____/               (cons@16)
   60% |                  _____/
       |             ____/
   40% |        ____/
       |    ___/
   20% |___/  15,6%
       |
    0% +---------------------------------------------------&gt;
        inicio                                 pasos de RL

  EN PARALELO: el largo promedio de la respuesta CRECE solo.
  Nadie le pide al modelo que escriba mas. Le conviene, y lo hace.
-->
<!-- ascii-note:
intent: mostrar las dos curvas del paper a la vez -- la precision sube durante el entrenamiento por refuerzo, y el largo de la respuesta crece por su cuenta como efecto emergente
emphasize: los tres numeros (15,6% inicio / 77,9% final / 86,7% con self-consistency) y la linea de cierre sobre el largo de respuesta creciendo sin que nadie lo pida
labels: eje Y precision AIME 2024 pass@1, eje X pasos de entrenamiento por refuerzo
-->

### Sources

- `research/web/deepseek-r1-nature/page.md` — DeepSeek-AI et al., *DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning*, Nature vol. 645, pp. 633-638 (2025), DOI 10.1038/s41586-025-09422-z. Abstract: "the reasoning abilities of LLMs can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories. The proposed RL framework facilitates the emergent development of advanced reasoning patterns, such as self-reflection, verification, and dynamic strategy adaptation." Método: "we bypass the conventional supervised fine-tuning (SFT) phase before RL training"; "The reward signal is only based on the correctness of final predictions against ground-truth answers, without imposing constraints on the reasoning process itself". Cifras: "the average pass@1 score on AIME 2024 shows a marked increase, jumping from an initial value of 15.6% to 77.9%. Also, by using the self-consistency decoding, the performance of the model can be further improved, achieving an accuracy of 86.7%. This performance greatly surpasses the average performance across all human competitors of the AIME." Largo de respuesta: Fig. 1b, "DeepSeek-R1-Zero naturally learns to solve reasoning tasks with more thinking time".
- `research/web/deepseek-r1-arxiv/page.md` — arXiv:2501.12948 (v1 22 ene 2025, v2 4 ene 2026), misma obra, abstract limpio para citar.
- `self-consistency-wang.web.md` — la técnica que el paper usa como decodificación (cons@16) es la misma que se enseñó en 5.x.

### Speaker notes

Esta lámina es nueva y es la que responde la pregunta que la sección nunca contestaba: cómo se logró que un modelo razone. La fuente es fuerte y conviene decirlo, porque cambia cómo la escuchan: está publicada en Nature, no es un post de blog. Y DeepSeek ya les apareció en la tabla de modelos de la sección de costos, así que no es un nombre nuevo. El hallazgo central en una frase: nadie le enseñó al modelo a razonar mostrándole razonamientos humanos. Se lo premió por acertar y los patrones aparecieron solos. El argumento del primer bullet es el que más discusión genera y vale sacarlo a flote: los autores sostienen que entrenar con trayectorias humanas le pone un techo al modelo, porque lo obliga a copiar la forma en que pensamos nosotros y le limita la exploración. Si a alguien le suena a exageración, el segundo bullet lo aterriza: la recompensa mira el resultado final y no impone ninguna restricción sobre cómo llegar. Del tercero, el dato que no está escrito es que el modelo también empieza a generar respuestas más largas por su cuenta, porque le conviene. Los números están para que quede el orden de magnitud, no para memorizarlos; el de 86,7% con self-consistency queda por encima del promedio de los participantes humanos de la competencia, y ese es el que impresiona. El recuadro cierra con la idea de que los autores usan self-consistency como técnica de evaluación, la misma que se enseñó en la sección anterior, para medir el techo del modelo. Y el remate del gráfico es lo mejor que tiene el paper para esta clase: la longitud de la respuesta crece sola durante el entrenamiento. El modelo descubre que escribir más lo hace acertar más. Eso es la tesis de la clase, medida experimentalmente por otra gente.

---

## 5. La recompensa tiene que ser verificable

### Content

**El refuerzo puro funciona mientras la señal de recompensa sea confiable. DeepSeek-R1 la construye con reglas escritas a mano en vez de con un modelo aprendido, y explica por qué.**

- **Recompensa de exactitud** En matemática, la respuesta va en un formato fijado de antemano y un verificador por reglas la comprueba.
- **En código, decide el compilador** Corre la respuesta contra una batería de tests predefinidos.
- **Recompensa de formato** Premia encerrar el razonamiento en las etiquetas `<think>` y `</think>`, por interpretabilidad.
- **Sin modelos de recompensa neuronales** Los autores los descartan: son vulnerables al reward hacking cuando el refuerzo escala.
- **El límite del método** Sin verificador confiable, como al escribir, el refuerzo puro sigue siendo un problema abierto.

- 🎯 **La etiqueta `<think>` no es una convención de documentación.** Es parte de la función de recompensa con la que se entrenó el modelo.

### Sources

- `research/web/deepseek-r1-nature/page.md`, sección Methods → *Reward design*: "Our rule-based reward system mainly consists of two types of reward: accuracy rewards and format rewards"; "in the case of maths problems with deterministic results, the model is required to provide the final answer in a specified format (for example, within a box), enabling reliable rule-based verification of correctness. Similarly, for code competition prompts, a compiler can be used to evaluate the responses of the model against a suite of predefined test cases"; "the model is incentivized to encapsulate its reasoning process within designated tags, specifically `<think>` and `</think>`"; "we abstain from applying neural reward models—whether outcome-based or process-based—to reasoning tasks. This decision is predicated on our observation that neural reward models are susceptible to reward hacking during large-scale RL". Sección *Reward hacking*: "for complex tasks that cannot be effectively evaluated by a reliable reward model, scaling up pure RL methods remains an open challenge"; "for tasks that cannot obtain a reliable signal, DeepSeek-R1 uses human annotation to create supervised data".

### Speaker notes

Esta lámina es de ingeniería pura y por eso funciona con este grupo. La pregunta que contesta es cómo se le pone una nota a un razonamiento sin leerlo. La respuesta del paper es elegante: no lo leas, verifica el resultado. En matemática se exige la respuesta en un formato fijo y se compara; en código se compila y se corre contra tests. Un detalle concreto que ayuda: en matemática el formato fijado de antemano suele ser una caja, y eso es lo que hace comprobable la respuesta sin leer el razonamiento. Del tercer bullet, conviene agregar que la justificación de las etiquetas es doble: interpretabilidad, y poder analizar después las trazas. Detente en el cuarto, que es el argumento más interesante. Podrían haber entrenado un modelo que puntúe razonamientos, y decidieron no hacerlo porque un modelo de recompensa se puede hackear cuando escalas el entrenamiento; un compilador con tests no. Pregúntales qué haría un agente optimizador contra un evaluador aprendido: van a llegar solos a que aprende a agradarle al evaluador en vez de a resolver el problema. Es el mismo problema que ya conocen de las métricas de proxy en producción. El quinto es la honestidad del paper y conviene no saltearlo, porque marca el borde del método: donde no hay verificador, esto no escala, y ahí vuelve la anotación humana. Y el remate es el que le cierra el círculo a la sección entera: la etiqueta `<think>` estaba en la función de recompensa, así que las etiquetas del prompt y el bloque nativo comparten ancestro. Cuando escriban `<thinking>` en un prompt, van a estar usando la misma convención con la que se entrenó el modelo.

---

## 6. Del prompt al entrenamiento

### Content

**Lo que Chain of Thought conseguía pidiéndolo en el prompt, los modelos de razonamiento lo traen del entrenamiento. El mecanismo es el mismo y cambió quién pide los pasos.**

- **El mecanismo no cambió** Wei et al. mostraron que escribir pasos intermedios mejora el desempeño en tareas complejas.
- **Antes lo pedía el prompt** "Pensemos paso a paso" producía la cadena; hoy el modelo la produce por su cuenta.
- **Ahora lo pide el entrenamiento** El refuerzo con recompensa verificable instala el comportamiento.
- **Y también la plataforma** Con el thinking activo, la API incluye un system prompt especializado para soportarlo.
- **Por eso algunas técnicas pierden filo** Pedir el paso a paso agrega poco contra un modelo que ya lo hace.
- **El costo es invisible** Los tokens de pensamiento se facturan como salida y no vuelven en la respuesta.

- 🎯 **Es la tesis de la clase otra vez: los pasos escritos son el cómputo.** Lo que se movió es la autoría del pedido, del prompt del usuario al entrenamiento del modelo y al system prompt del proveedor.

### Sources

- `chain-of-thought-wei.web.md` — Wei et al. (2022). Generar una cadena de pasos intermedios mejora el desempeño en razonamiento aritmético, de sentido común y simbólico; la capacidad emerge en modelos suficientemente grandes.
- `research/web/deepseek-r1-nature/page.md` — el comportamiento de razonamiento se incentiva con refuerzo puro y los patrones emergen del entrenamiento (ver Sources de la lámina 6.4).
- `research/web/anthropic-docs-adaptive-thinking/page.md` — "When thinking is active, a specialized system prompt is automatically included to support this feature"; los tokens que el modelo usa mientras piensa se facturan como tokens de salida.

### Speaker notes

Esta es la lámina conceptual que le da sentido al bloque y ahora tiene la fuente que le faltaba. Vuelve a la tesis: el modelo no tiene un motor de razonamiento aparte, completa tokens de izquierda a derecha, y lo que llamamos razonar es que escriba los pasos intermedios antes de la respuesta. Chain of Thought descubrió eso y lo explotó desde el prompt. Lo que cambió después es dónde se pide. El tercer y el cuarto bullet son dos momentos distintos y conviene separarlos al decirlos. Uno es el entrenamiento, que es lo que acaban de ver en la lámina de DeepSeek. El otro es tiempo de ejecución, y es el dato que sorprende: la documentación dice que cuando el thinking está activo la API inyecta sola un system prompt especializado. O sea que abajo de todo sigue habiendo un prompt pidiéndole al modelo que razone. Solo que no lo escribes tú. La consecuencia práctica es incómoda y vale decirla: parte de lo que enseñamos en la sección anterior pierde filo contra un modelo de razonamiento, porque ya lo hace solo y encima se lo están pidiendo. El cierre es el costo, y ahí el matiz es que la factura sube sin que aparezca una línea de texto en pantalla; lo retomas en detalle al final de la sección. Del recuadro sale además la consecuencia para el trabajo de ellos: escribir mejores instrucciones importa menos que elegir cuánto conviene que el modelo piense.

---

## 7. Effort: un parámetro de la petición

### Content

**`effort` es un parámetro de la petición. Gradúa cuántos tokens gasta el modelo al responder e intercambia exhaustividad por eficiencia dentro de un mismo modelo.**

```python
response = client.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    thinking={"type": "adaptive"},        # el modelo decide si piensa y cuanto
    output_config={"effort": "medium"},   # low | medium | high | xhigh | max
    messages=[{"role": "user", "content": "Clasifica este issue..."}],
)
```

- **`effort` va en `output_config`** Nunca adentro del objeto `thinking`.
- **`adaptive` es un modo de thinking** Nunca un valor de `effort`.
- **`high` es el default** Pasarlo produce exactamente el mismo comportamiento que omitirlo.

- ⚠️ **Son los tres errores más frecuentes al configurarlo por primera vez.**

### Sources

- `research/web/anthropic-docs-effort/page.md` — "The effort parameter lets you control how many tokens Claude spends when responding to requests. You can trade off between response thoroughness and token efficiency with a single model"; `output_config.effort`; "Setting `effort` to `"high"` produces exactly the same behavior as omitting the `effort` parameter entirely".
- `research/web/anthropic-docs-adaptive-thinking/page.md` — "Effort is set at `output_config.effort`, not inside the `thinking` object".

### Speaker notes

Esta es la lámina que desarma el malentendido más común, así que la primera línea va despacio: el effort no es una propiedad del modelo ni algo que se decidió en el entrenamiento. Es un parámetro que viaja en la petición y que cambia cuánto gasta el mismo modelo. Del código, marca dónde va: adentro de `output_config`. Es el error que todos cometen la primera vez, y es el primero de los tres que conviene que se lleven anotados. El tercero tiene una consecuencia práctica que suele sorprender: si alguien está pasando `high` creyendo que sube algo, no está subiendo nada, porque es el default. Sobre cómo elegir el nivel, la documentación recomienda arrancar en `high` en Opus 5 y en Fable 5.1 y bajar a `medium` o `low` cuando los evals muestren que la calidad aguanta; en Opus 4.7 y 4.8 el punto de partida recomendado para código y tareas agénticas es `xhigh`. Al cambiar de modelo conviene volver a barrer los niveles en vez de reusar el que traían.

---

## 8. Los cinco niveles de effort

### Content

**Cinco niveles, del más rápido al más exhaustivo. La disponibilidad no es uniforme: hay modelos que soportan `max` y no soportan `xhigh`.**

| Nivel | Comportamiento del thinking | Disponibilidad |
|---|---|---|
| `max` | Piensa siempre, sin restricción de profundidad. | Fable 5.1, Mythos 5.1, Fable 5, Mythos 5, Mythos Preview, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5, Sonnet 4.6 |
| `xhigh` | Piensa siempre y en profundidad, con exploración extendida. | Fable 5.1, Mythos 5.1, Fable 5, Mythos 5, Opus 5, Opus 4.8, Opus 4.7, Sonnet 5 |
| `high` (default) | Piensa casi siempre. Razonamiento profundo en tareas complejas. | Todos los modelos que soportan `effort` |
| `medium` | Thinking moderado. Puede saltear el thinking en consultas simples. | Todos los modelos que soportan `effort` |
| `low` | Minimiza el thinking. Lo saltea en tareas simples donde manda la velocidad. | Todos los modelos que soportan `effort` |

- **Alcanza a toda la salida** Texto, llamadas a herramientas y thinking, con el thinking activo o sin él.
- **Con effort bajo el modelo también usa menos herramientas** Hace menos llamadas y más escuetas.

- 🎯 **Es una señal de comportamiento, no un presupuesto de tokens.** Con effort bajo el modelo sigue pensando en los problemas difíciles, y piensa menos que con effort alto para el mismo problema.

### Sources

- `research/web/anthropic-docs-effort/page.md` — "The effort parameter affects **all tokens** in the response"; "Effort is a behavioral signal, not a strict token budget"; "Not every model that supports `max` supports `xhigh`"; tabla de niveles con disponibilidad por modelo (copiada sin simplificar).
- `research/web/anthropic-docs-adaptive-thinking/page.md` — tabla "Effort level / Thinking behavior" (columna 2 de la tabla de esta lámina, copiada verbatim en su contenido); "Level availability varies by model".

### Speaker notes

Esta es la lámina de referencia del bloque y la que más plata les puede ahorrar. De la tabla no leas las filas, que están para consultar; lee la columna de la derecha y di lo importante, que la disponibilidad no es uniforme y que hay modelos que soportan `max` sin soportar `xhigh`. Si el que pregunta necesita el detalle, la tabla de la documentación es la autoridad. El remate tiene un matiz que se pierde si vas rápido: el effort no es un presupuesto de tokens, es una señal. Con effort bajo el modelo sigue pensando cuando el problema es difícil de verdad. Piensa menos que con effort alto, y no deja de pensar. El segundo bullet es el que se le escapa a todo el mundo y vale marcarlo: bajar el effort no solo acorta el razonamiento, también hace que el modelo llame menos herramientas y de forma más escueta, lo cual cambia el comportamiento de un agente entero.

---

## 9. Pedirle al modelo que piense

### Content

**Que el modelo piense en un turno dado es promptable. El effort fija la postura general y el lenguaje natural corrige el disparo caso por caso.**

- **Primero el effort** Fijar el nivel que corresponde al balance de calidad y latencia de la carga de trabajo.
- **Después el prompt** Agregar guía en lenguaje natural solo si el disparo del thinking todavía no coincide con lo que hace falta.
- **En el system prompt** Cambia el umbral para todas las peticiones de la conversación.
- **Por mensaje** Empuja o suprime el thinking en ese turno, sin tocar el system prompt ni cambiar un parámetro.

- ⚠️ **Bajar el effort es la primera palanca, porque es un control calibrado.** La guía por prompt depende de las palabras exactas, y empujar al modelo a pensar menos puede bajar la calidad en las tareas que se benefician del razonamiento.

### Sources

- `research/web/anthropic-docs-adaptive-thinking/page.md` — "Whether Claude thinks on a given turn is promptable. Effort sets the overall posture, but you can also shape the decision directly with natural-language guidance, either globally in the system prompt or per message from the user turn"; el orden de las dos palancas; "Lowering the effort level is usually the better first lever, since it is a calibrated control rather than a wording-sensitive instruction"; qué medir para verificar el steering.

### Speaker notes

Esta lámina es la que ata la sección con el resto de la clase y por eso vale la pena marcarla como tal. Durante dos horas les enseñaste a escribir prompts. Acá el círculo se cierra: la profundidad del razonamiento, que parecía una perilla de infraestructura, también se controla con lenguaje natural. El orden de los dos primeros bullets es una recomendación explícita de la documentación y conviene decirlo con esas palabras: primero el effort, después el prompt. La razón está en la advertencia final. El effort es un control calibrado; una frase en el system prompt es una instrucción y su efecto depende de cómo la escribiste. Antes de mandar cualquiera de las dos a producción, hay que medir sobre una muestra representativa del tráfico, y la documentación dice qué mirar: cuántas veces se dispara el thinking, cuántos tokens de salida, latencia y calidad. Si te queda tiempo, pregúntales qué medirían ellos. La primera de las cuatro es la que nadie dice: contar cuántas respuestas traen bloque de thinking.

---

## 10. Frases que suben o bajan el thinking

<!-- format: list -->

### Content

**Las tres redacciones que la documentación da textuales. Están en inglés porque en la práctica los system prompts se escriben en inglés.**

- **Para que piense menos, en el system prompt** *"Extended thinking adds latency and should only be used when it will meaningfully improve answer quality, typically for problems that require multistep reasoning. When in doubt, respond directly."*
- **Para que piense en este turno** *"Please think hard before responding."*
- **Para que responda directo en este turno** *"Answer directly without deliberating."*

- ⚠️ **La redacción exacta importa.** Si una frase no produce el comportamiento buscado, la documentación sugiere probar una variante más directa.

### Sources

- `research/web/anthropic-docs-adaptive-thinking/page.md` — los tres ejemplos de redacción, citados verbatim; "Steering effectiveness can be sensitive to exact wording"; la guía por mensaje desde el turno del usuario.

### Speaker notes

Las tres frases están en inglés a propósito, porque son las que la documentación da textuales y porque cambiarles una palabra cambia el efecto. La primera va en el system prompt y mueve el umbral de toda la conversación. Las otras dos van en el turno del usuario y valen solo para ese turno. El ejemplo que mejor aterriza esto para un ingeniero es el del harness agéntico: la misma aplicación pone *"Please think hard before responding."* en los pasos de planificación y *"Answer directly without deliberating."* en las confirmaciones de rutina, sin tocar el system prompt ni cambiar un parámetro entre turnos. Es steering en tiempo de ejecución, decidido por el código. La advertencia final no es un detalle: la documentación misma admite que la efectividad depende de la formulación, y la receta cuando algo no funciona es probar una variante más directa, no insistir con la misma frase.

---

## 11. Prompting con un modelo que razona

### Content

**Con un modelo que razona por su cuenta el prompting sigue importando, y cambia qué conviene escribir.**

- **Instrucción general antes que plan** Un "pensar a fondo" produce mejor razonamiento que un plan escrito a mano.
- **Los ejemplos con razonamiento siguen sirviendo** El modelo generaliza ese estilo a sus propios bloques de thinking.
- **El CoT manual pasó a ser el plan B** Sigue vigente para cuando el thinking está apagado.
- **El modelo se autorregula** Calibra según el effort y la complejidad de la consulta, y en preguntas fáciles responde directo.

- 🎯 **La palanca de calidad se mudó al parámetro.** Escribir buenas instrucciones sigue importando, y la decisión que más mueve el resultado es cuánto conviene que el modelo razone.

### Sources

- `research/web/anthropic-prompting-best-practices/` — guía de prompting de Anthropic, sección *Leverage thinking & interleaved thinking capabilities*, capturada el 2026-09-01. Aporta verbatim: preferir instrucciones generales sobre pasos prescriptivos porque "el razonamiento de Claude frecuentemente excede lo que un humano prescribiría"; que los ejemplos multishot funcionan con thinking y el modelo generaliza el estilo; y el CoT manual como *fallback* para cuando el thinking está apagado.
- `research/web/anthropic-docs-adaptive-thinking/` — la calibración por dos factores (effort y complejidad de la consulta) y la respuesta directa en consultas fáciles.

### Speaker notes

Esta lámina cierra el círculo con la sección de técnicas y conviene decirlo así: allá aprendieron cuatro formas de hacer que el modelo escriba los pasos intermedios; acá aparece un modelo que ya los escribe solo. La pregunta natural del alumno es si entonces el prompting sobra, y la respuesta es que no, pero cambia qué conviene escribir. El primer punto es el más contraintuitivo y el que más les va a servir: escribirle el plan paso a paso es peor que pedirle que piense a fondo. La documentación lo dice sin vueltas, y vale citarlo: el razonamiento del modelo frecuentemente excede lo que un humano prescribiría. Es incómodo de aceptar para un ingeniero acostumbrado a especificar. El segundo salva algo que ya enseñamos: mostrarle el patrón de razonamiento dentro de ejemplos few-shot sigue valiendo, y ahora además le enseña un estilo que el modelo aplica a sus propios bloques. El tercero da la regla práctica: CoT a mano solo si el thinking está apagado; si está disponible, conviene dejarlo activo y graduar con effort. Y el cuarto explica por qué subir el effort no siempre cambia nada: si la pregunta es fácil, el modelo responde directo aunque el thinking esté activo. Cierra con el recuadro, que es la tesis de la sección, y agrega la parte que la lámina ya no dice: además de decidir cuánto razona, hay que saber leer la traza que devuelve.

---

## 12. Qué cuesta el thinking

### Content

**No existe un presupuesto de tokens de pensamiento. `max_tokens` pone el techo duro de toda la salida y `effort` orienta cuánto de esa salida se va en pensar.**

- **`max_tokens` cubre thinking más texto** El modelo nunca lo pasa.
- **Un techo dimensionado sin razonamiento queda corto** Las respuestas se truncan apenas el modelo empieza a pensar.
- **En un bucle de herramientas, cada petición tiene el suyo** No acota el gasto del turno completo.
- **Si aparece `stop_reason: "max_tokens"`** Subir el techo si ese razonamiento hacía falta, o bajar el effort si hubo exceso de pensamiento.

### Sources

- `research/web/anthropic-docs-adaptive-thinking/page.md` — sección *Cost control*: "You don't set a thinking token budget"; `max_tokens` como tope duro de la salida total y su comportamiento en un bucle de herramientas; los dos remedios ante `stop_reason: "max_tokens"`.

### Speaker notes

Arranca por la distinción de arriba, que es la que ordena todo: `max_tokens` es un techo duro y el modelo nunca lo pasa; `effort` es una guía blanda y no garantiza ninguna cuenta de tokens. El error clásico es dimensionar `max_tokens` como si no hubiera razonamiento, y después ver respuestas cortadas a la mitad. El tercer bullet es el que rompe la intuición de quien construye un agente: el techo es por petición, así que un bucle de veinte llamadas a herramientas no tiene ningún tope agregado, y ahí es donde el gasto se dispara sin que nadie lo vea. El cuarto da la regla de diagnóstico, y lo importante es que las dos salidas son opuestas: si las respuestas se cortaron y ese razonamiento hacía falta, sube el techo; si lo que hubo fue exceso de pensamiento, baja el effort. Elegir mal empeora el problema.

---

## 13. Qué se factura del thinking

### Content

**Se cobra el proceso de pensamiento completo, y el ajuste `display` cambia lo que se ve sin mover la factura.**

- **Los tokens de razonamiento** Se facturan como salida, aunque no se muestren.
- **Los bloques de turnos previos** Se facturan como entrada mientras siguen en contexto, y el default de preservación varía por modelo.
- **`display: "omitted"`** El campo de thinking vuelve vacío y se paga exactamente lo mismo.
- **Cómo auditarlo** `usage.output_tokens_details.thinking_tokens` informa cuántos tokens facturados fueron razonamiento interno.

- ⚠️ **Cambiar el effort invalida el caché.** El valor resuelto se renderiza dentro del prompt, así que cambiarlo entre peticiones rompe los breakpoints. El effort por mensaje, en beta y con su header, conserva el caché.

### Sources

- `research/web/anthropic-docs-adaptive-thinking/page.md` — sección *Pricing*: los tres conceptos facturados (tokens de thinking como salida; bloques de thinking de turnos previos que quedan en contexto como entrada, con default de preservación por modelo; texto de salida normal); "The billed output token count does **not** match the visible token count in the response. You are billed for the full thinking process, not the thinking content visible in the response"; tabla `display: "summarized"` vs `"omitted"`; `usage.output_tokens_details.thinking_tokens`. Sección *Prompt caching*: "The resolved effort value is rendered into the prompt, so changing it between requests invalidates cache breakpoints".
- `research/web/anthropic-docs-effort/page.md` — el effort por mensaje (beta `mid-conversation-output-config-2026-07-01`) preserva el caché; el cambio de valor de primer nivel lo reinicia.

### Speaker notes

Esta es la lámina que les va a ahorrar una sorpresa en la factura, y tiene un dato que casi nadie conoce. El segundo bullet no está en ningún tutorial y conviene detenerse: los bloques de razonamiento de turnos anteriores que siguen en el contexto se pagan como tokens de entrada, turno tras turno. Algunos modelos conservan todos los turnos y otros solo el último, así que el default hay que mirarlo por modelo. Conéctalo con la bola de nieve del contexto que vieron en fundamentos, porque es exactamente el mismo fenómeno aplicado al razonamiento. El tercero es el más contraintuitivo y vale decirlo dos veces: `display` cambia lo que ves, no lo que pagas. Si configuras `omitted` para no mostrar el razonamiento, el campo vuelve vacío y la factura es idéntica. Si alguien quiere auditar cuánto se le está yendo en pensar, el campo del cuarto bullet se lo dice. La advertencia de caché es un enlace directo con la sección de fundamentos y vale la pena hacerlo explícito: el nivel de effort resuelto se escribe adentro del prompt, así que cambiarlo es cambiar el prefijo, y ya saben qué pasa cuando el prefijo cambia. Cambiar el valor de primer nivel reinicia el caché; el effort por mensaje, que todavía está en beta y necesita su header, lo conserva.

---

## 14. Las perillas de sampling ya no están

### Content

**Con thinking activo no podés tocar el azar de la generación. En Opus 4.7 y posteriores, `temperature`, `top_p` y `top_k` directamente dejaron de estar soportados.**

- **Qué controlaban** El azar al elegir el próximo token: temperatura baja, salida más conservadora; alta, más variedad. Era la perilla clásica para ajustar creatividad contra consistencia.
- **Qué pasa hoy** En los modelos con thinking adaptativo ya no se aceptan. La migración recomendada es sacarlas del pedido y guiar el comportamiento por prompt y por effort.
- **Por qué, probablemente** El razonamiento se entrenó por refuerzo sobre una distribución de muestreo determinada. Tocarla desde afuera cambia las reglas a un proceso calibrado bajo reglas fijas, y degrada justo las bifurcaciones y las vueltas atrás que hacen útil al thinking.
- **Qué queda en su lugar** El `effort`. Un dial más abstracto, calibrado por el proveedor, en lugar de tres parámetros de bajo nivel que interactuaban mal con una capacidad entrenada.

- 🎯 **La forma de la evolución.** Se pierde control fino y se gana robustez. No es una decisión de producto arbitraria: es consecuencia de que razonar dejó de ser algo que se pide en el prompt y pasó a ser algo que se entrenó.

### Sources

- `research/web/sampling-removido-4-7/` — guía de migración a Claude Opus 4.7, capturada el 2026-09-01: *"Sampling parameters removed — `temperature`, `top_p`, and `top_k` are no longer supported"*, junto con thinking adaptativo como único modo y la aparición del nivel `xhigh`.
- `research/web/deepseek-r1-nature/` — el entrenamiento por refuerzo del razonamiento, que es lo que sostiene la explicación del tercer punto.

### Speaker notes

Lámina de cierre de la sección, y sirve para dejar una idea de forma más que un dato. Empezá preguntando quién tocó alguna vez la temperatura de un modelo; en un curso de software varios van a levantar la mano, porque es la perilla que aparece en todos los tutoriales. Y ahora no está. Las tres desaparecieron en Opus 4.7: no es que haya que ponerlas en un valor concreto, es que dejaron de estar soportadas y la migración recomendada es sacarlas del pedido. El tercer punto es el interesante y conviene decirlo con la reserva que lleva: la explicación más razonable es que el razonamiento se entrenó por refuerzo bajo una distribución de muestreo determinada, y meterle mano desde afuera rompe esa calibración — el modelo puede volverse repetitivo o dejar de explorar las ramas que necesita. Es coherente con lo que vieron dos láminas antes sobre cómo se entrenó, pero no está documentado como la razón oficial, así que presentalo como lo que es. Y cerrá con la idea de forma: se pierde control fino, se gana robustez, y el effort es lo que ocupa ese lugar. Es la misma historia de toda la sección: lo que antes se pedía en el prompt ahora viene entrenado, y lo que se ajustaba a mano ahora se gradúa con un dial calibrado.

---

# 7. LLMs en ingeniería

**Goal of this section:** Situar todo lo anterior en el ciclo de vida real de un producto de software, con los riesgos que trae y las mitigaciones que un equipo ya sabe practicar.

---

## 1. Ciclo de vida: dónde entra el LLM

### Content

**El mismo recorrido que hace un cambio desde que alguien lo pide hasta que llega a producción, con lo que un LLM aporta en cada estadio.**

![Ciclo vida seis estadios](images/s7-1-1-ciclo-vida-seis-estadios.svg)
<!-- ascii-source:
     +----------+     +----------+     +----------------+     +----------+
     |  ISSUE   | --&gt; |  DISENO  | --&gt; | IMPLEMENTACION | --&gt; |  REVIEW  |
     |  triage  |     |  ADRs    |     | codigo, tests  |     |   diff   |
     +----------+     +----------+     +----------------+     +----------+
          ^                                                        |
          |                                                        v
          |           +-------------+                        +----------+
          +---------- | INCIDENTE   | <--------------------- |  DEPLOY  |
                      | logs        |                        | release  |
                      | post-mortem |                        |  notes   |
                      +-------------+                        +----------+

  El post-mortem vuelve como issue: el ciclo se cierra, no termina.
  Hay un LLM util en los seis estadios, no solo en "escribir codigo".
-->
<!-- ascii-note:
intent: mostrar el ciclo de vida de un cambio como un lazo cerrado de seis estadios, y que el aporte del LLM esta repartido en los seis y no concentrado en la implementacion, que es donde la intuicion lo pone
emphasize: la flecha de retorno de INCIDENTE a ISSUE, que es lo que convierte la secuencia en ciclo; la caja IMPLEMENTACION como uno mas entre seis y no como el centro
labels: "ISSUE / triage", "DISENO / ADRs", "IMPLEMENTACION / codigo, tests", "REVIEW / diff", "DEPLOY / release notes", "INCIDENTE / logs, post-mortem", y las dos lineas de cierre
-->

| Etapa | Qué hace hoy |
|---|---|
| **Issue y triage** | Clasifica, deduplica y enruta al equipo correcto. |
| **Diseño** | Redacta ADRs, contrasta alternativas, encuentra precedentes en el propio repo. |
| **Implementación** | Completa código, genera tests, traduce entre lenguajes y frameworks. |
| **Review** | Detecta bugs, marca desvíos de la guía de estilo, resume el diff para el revisor. |
| **Deploy** | Redacta release notes y verifica checklists de salida. |
| **Incidente** | Correlaciona logs, propone hipótesis, redacta el post-mortem. |

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 51) — la slide original recorría el trayecto de un paciente. Se conserva la forma argumental (etapa, qué se hace hoy, hacia dónde va) y se cambió el dominio.
- Fuentes del original, desanidadas del bloque de hipervínculos superpuestos y conservadas acá como procedencia de la versión médica: Frontiers in Digital Health (2025) · MedGemma, Google DeepMind (2025) · Nature Medicine (2025) · WHO — *Ethics & Governance of AI for Health: LMMs* (2024). Ninguna respalda el contenido de software de esta versión.

### Speaker notes

Esta slide reordena toda la clase en el eje que a ellos les resulta natural: el flujo de trabajo. La columna "hacia dónde va" salió de la lámina y va hablada, estadio por estadio: en **issue**, priorización con el contexto del roadmap y de la deuda técnica; en **diseño**, exploración de alternativas con costo y riesgo estimados; en **implementación**, agentes que abren un pull request completo a partir del issue; en **review**, revisión con el contexto histórico del módulo y de sus incidentes; en **deploy**, estimación de riesgo del despliegue a partir del diff; y en **incidente**, diagnóstico asistido mientras el incidente sigue abierto. Marcalas como especulación, que es lo que son. Vale la pena decir de entrada que las seis etapas no son igual de maduras, y que la columna del medio es lo que ya se usa hoy en equipos reales, no una promesa. La fila de review es la que más pega, porque es donde el LLM aporta y donde más rápido se ve el límite: encuentra el bug obvio y no entiende por qué ese módulo está escrito así. La fila de incidente es la que más entusiasma y la más peligrosa, porque un post-mortem con una causa raíz inventada es peor que no tener post-mortem. Aviso de honestidad: la versión original de esta slide traía cifras del dominio médico, y no las traduje a números de software porque no tengo fuente. Lo que queda es cualitativo a propósito.

---

## 2. Explorar y entender código

### Content

**El otro uso grande no es escribir código: es entender el que ya existe.**

| Búsqueda semántica en repos grandes | Comprensión de sistemas legados |
|---|---|
| Preguntar "dónde se decide si un pedido se factura en dos cuotas" y recibir los tres archivos que importan, en vez de 400 coincidencias de `grep`. | Reconstruir el modelo mental de un módulo sin autor vivo: qué hace, qué invariantes asume y qué rompe si se toca. |

| Síntesis de documentación | Arqueología de decisiones |
|---|---|
| Generar el README que nunca se escribió, a partir del código, los tests y los nombres de las cosas. | Recorrer historial de Git, ADRs y tickets viejos para responder por qué se eligió esto y no aquello. |

- ⚠️ Las cuatro tareas comparten el mismo riesgo: el modelo produce una explicación coherente aunque el código haga otra cosa. La respuesta se verifica contra el código, siempre.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 52) — la slide original recorría el pipeline de research biomédica. Se conserva la forma (cuatro cuadrantes de oportunidad) y se cambió el dominio.
- Fuentes del original, desanidadas del bloque de ocho hipervínculos superpuestos y conservadas acá como procedencia de la versión biomédica: BioGPT, Microsoft Research (2022) · AlphaFold 2/3, DeepMind (2022/2024) · ESMFold, Meta AI (2022) · Insilico Medicine, ISM001-055 Fase II · TxGNN, Harvard (Nature Medicine, 2024) · Recursion Pharmaceuticals · Consensus · Elicit. Ninguna respalda el contenido de software de esta versión. Los registros `biogpt-luo.web.md`, `alphafold-db.web.md`, `esm-atlas.web.md` y `txgnn-nature-medicine.web.md` del corpus corresponden a esa versión.

### Speaker notes

Esta es la slide donde más gente se sorprende, porque el uso famoso de los LLM es generar código y el uso que más tiempo ahorra en un equipo real es leerlo. La primera fila tiene el mejor argumento: la diferencia entre buscar por texto y buscar por intención. `grep` encuentra el nombre; el modelo encuentra el lugar donde se toma la decisión, aunque la variable se llame distinto. La cuarta es la que menos se piensa y la que más valor tiene en un equipo con rotación: la respuesta a "por qué está hecho así" vive repartida entre commits, tickets y una conversación de Slack de 2023. La advertencia del cierre no es retórica: una explicación fluida de un código que hace otra cosa es la alucinación más difícil de detectar, porque suena a documentación.

---

## 3. Casos de uso hoy

### Content

**Lo que ya está desplegado en equipos de software, no lo que se promete.**

| Asistentes de código | Generación de tests | Triage automático | Revisión y documentación |
|---|---|---|---|
| Completado en el editor y agentes que resuelven un issue completo. Es el uso más adoptado y el más medido. | Tests unitarios a partir del código existente, y casos borde que el autor no había pensado. | Clasificación, deduplicación y ruteo de issues y tickets entrantes. | Comentarios de review sobre el diff, resúmenes de pull request y documentación generada del código. |

- ⚠️ Ninguno reemplaza al revisor humano. Los cuatro producen borradores que alguien del equipo aprueba antes de que el cambio entre.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 53) — la slide original listaba cuatro categorías de casos clínicos con métricas. Se conserva la forma (cuatro categorías) y se cambió el dominio.

### Speaker notes

Slide corta y a propósito. Lo que hay que sostener es la advertencia del final, porque es la bisagra con las dos slides de riesgos que siguen. La columna de generación de tests merece una aclaración que suele hacer ruido: un test generado por el modelo a partir del código verifica que el código hace lo que hace, no que hace lo correcto. Es útil como red contra regresiones y no sirve como especificación. Si alguien pregunta por números de adopción o de productividad, decí la verdad: la versión original de esta slide tenía cifras de estudios clínicos y no las reemplacé por cifras de software inventadas. Quedó marcado como pendiente buscar evidencia citable.

---

## 4. Seguridad: el caso Glasswing

### Content

**En abril de 2026 un modelo de frontera sin publicar encontró miles de vulnerabilidades críticas —de forma autónoma, sin dirección humana— en todos los sistemas operativos y navegadores importantes. Doce empresas formaron Project Glasswing para poner esa capacidad del lado de la defensa.**

- **OpenBSD: veintisiete años escondida** En uno de los sistemas más endurecidos que existen, el que se usa para correr firewalls e infraestructura crítica. La falla permitía tirar abajo cualquier máquina de forma remota con solo conectarse a ella.
- **FFmpeg: el test que no alcanzó** Vulnerabilidad de dieciséis años, en una línea de código que las herramientas de testing automático habían recorrido **cinco millones de veces** sin detectar nunca el problema.
- **Linux: encadenar para escalar** El modelo encontró varias vulnerabilidades del kernel y las combinó solo, hasta pasar de usuario común a control total de la máquina.

- 🎯 **Por qué el pipeline se vuelve urgente.** Si un modelo encuentra en semanas lo que sobrevivió décadas de revisión humana y millones de tests, entonces la revisión y los tests que tenés hoy dejaron de ser suficientes. Y la capacidad no es exclusiva de los defensores: el mismo modelo que encuentra la falla para parcharla sabe escribir el exploit.

### Sources

- `research/web/anthropic-glasswing/` — Anthropic, Project Glasswing, 7 de abril de 2026, capturado el 2026-09-01. Socios fundadores: AWS, Anthropic, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, Linux Foundation, Microsoft, NVIDIA y Palo Alto Networks. Aportan verbatim los tres casos (OpenBSD 27 años, FFmpeg 16 años con cinco millones de ejecuciones de test, cadena de escalada en el kernel de Linux), que las tres fallas ya fueron parcheadas, y que el modelo las encontró "enteramente de forma autónoma, sin dirección humana". En el benchmark CyberGym el modelo marca 83,1% contra 66,6% del siguiente mejor.
- Nota: la captura todavía no tiene registro en `research/corpus/` — falta la pasada del librarian.

### Speaker notes

Esta lámina es la cara incómoda de todo lo que vimos hoy, y va acá a propósito: recién les mostré los casos de uso lindos, y esto es el reverso. El dato que más impacta no es el número de vulnerabilidades, es la antigüedad: veintisiete años en OpenBSD, que es el sistema que la industria pone de ejemplo cuando habla de código endurecido. Y el de FFmpeg es el que les va a doler como ingenieros: la línea estaba cubierta, los tests la recorrieron cinco millones de veces, y el problema no se veía. No es que faltaba cobertura; es que el tipo de error no era detectable con esas herramientas. De ahí sale la conclusión práctica, y conviene decirla sin dramatismo: el pipeline de revisión y testing que hoy consideran suficiente fue construido contra un atacante humano. La simetría es lo último y lo más importante: la misma capacidad que encuentra la falla para parcharla sirve para escribir el exploit. Por eso el proyecto existe y por eso hay doce empresas grandes adentro. Si alguien pregunta si esto es marketing, señalá el detalle verificable: las tres fallas están parcheadas y reportadas a los mantenedores.

---

## 5. Oportunidades vs. riesgos

### Content

**Oportunidades**

- **Bajar el piso de entrada** Tareas que antes exigían un especialista quedan al alcance de más gente del equipo.
- **Liberar tiempo** Menos horas en documentación, boilerplate y tickets repetidos, más horas en diseño.
- **Acelerar la exploración** Evaluar tres alternativas de diseño en el tiempo que antes llevaba evaluar una.
- **Mejorar el onboarding** Alguien que entra puede preguntarle al repositorio en vez de interrumpir a un colega.

**Riesgos**

- **Alucinación de APIs y dependencias** Funciones, parámetros y paquetes que no existen, escritos con sintaxis convincente. Una dependencia inventada que alguien registra con ese nombre es un vector de ataque.
- **Código inseguro** El modelo reproduce patrones que vio, y vio mucho código vulnerable: concatenación en SQL, secretos en el repositorio, validación ausente.
- **Dependencia excesiva** Sesgo de automatización: el equipo deja de revisar lo que el modelo produce, y la habilidad de revisar se atrofia.
- **Licencias y procedencia** El código generado puede reproducir fragmentos de código con licencia, y hoy no hay forma simple de rastrear de dónde salió.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 54) — la slide original presentaba cuatro oportunidades y cuatro riesgos del marco de la OMS para grandes modelos multimodales (2024). Se conserva la forma (4 + 4) y se cambió el dominio.

### Speaker notes

Ocho ítems, y conviene ordenar el énfasis en lugar de leerlos todos. De las oportunidades, la cuarta es la que más rápido se nota en un equipo real y la que menos se nombra en las presentaciones. De los riesgos, los dos primeros son técnicos y se atacan con herramientas, y los dos últimos son organizacionales y no. La dependencia excesiva es el que hay que dejar instalado porque es lento y silencioso: no rompe nada el primer mes, y a los seis meses hay un equipo que aprueba pull requests sin leerlos. El de licencias suele generar debate y no tiene respuesta cerrada todavía; si sale, decí que está sin resolver en vez de improvisar una.

---

## 6. Mitigaciones que funcionan

### Content

**Ninguna es nueva. Son las prácticas de ingeniería de siempre, aplicadas a un artefacto que casi nadie trata como código.**

- **Revisión humana obligatoria** Sin excepción. El output del modelo entra como borrador y una persona lo aprueba. Es la única mitigación que aparece en todas las implementaciones documentadas que funcionan.
- **Tests como red** La suite de tests es lo que hace seguro aceptar código que nadie escribió a mano. Sin tests, el código generado es deuda que todavía no se declaró.
- **Linters y SAST en el pipeline** El análisis estático agarra la concatenación en SQL y el secreto hardcodeado antes del merge, sin depender de que el revisor esté atento ese día.
- **RAG sobre el propio repositorio** Darle al modelo la guía de estilo, los ADRs y el código real del equipo, en vez de confiar en lo que recuerde del entrenamiento.
- **Monitoreo continuo** Medir antes y después: tasa de aceptación de sugerencias, defectos que llegan a producción, tiempo de review. Sin medición no hay decisión.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 55) — la slide original listaba mitigaciones para despliegues clínicos. Se conserva la forma (lista de mitigaciones) y se cambió el dominio.

### Speaker notes

La primera es la única no negociable y conviene decirlo con esas palabras. Todo lo demás es gradiente; la revisión humana es un piso. La segunda tiene un matiz que a ellos les va a sonar: aceptar código generado sin tests no es más rápido, es tomar deuda a una tasa que no está declarada, porque el costo aparece cuando alguien tiene que modificar código que nadie entiende y nadie escribió. La tercera es la de mejor relación entre esfuerzo y resultado, y suele estar ya instalada en el pipeline: no hay que comprar nada, hay que dejar de saltearla. La cuarta cierra el círculo con toda la clase, porque es prompt caching más grounding aplicado al caso de ellos.

---

## 7. Para pensar

### Content

- **La evidencia todavía es floja** La mayor parte de lo que se publica sobre productividad con LLMs es observacional o en entornos controlados. Los estudios rigurosos sobre implementaciones reales se cuentan con los dedos.
- **La brecha de uso es real** Un modelo capaz usado sin criterio rinde mucho menos que el mismo modelo usado con criterio. El contexto de uso pesa tanto como la tecnología, y esa parte no la resuelve la próxima versión.
- **¿Quién responde cuando falla?** Si el código generado introduce una vulnerabilidad que llega a producción, la responsabilidad no es del modelo. Falta acordar de quién es dentro del equipo, y esa conversación conviene tenerla antes.
- **Marco ético de referencia** El deck original apoyaba esta sección en los seis principios de la OMS para grandes modelos multimodales: autonomía, bienestar, transparencia, responsabilidad, equidad y sostenibilidad. Fuera de salud siguen sirviendo como checklist de gobernanza.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 55)
- WHO — *Ethics & Governance of AI for Health: LMMs* (2024), procedencia del marco de seis principios. El enlace del deck original (`iris.who.int/handle/10665/375579`) devuelve 403 (corpus, inconsistencia 2).

### Speaker notes

Slide de discusión, no de contenido. Si hay tiempo, la tercera viñeta es la mejor pregunta para abrir al grupo, y suele generar debate real: quién firma. La respuesta correcta es la misma de siempre en software, quien mergea, y hacerles llegar solos a esa conclusión vale más que decirla. La primera viñeta es un ejercicio de honestidad intelectual que esta clase se debe: la mayoría de las cifras de productividad que circulan no resistirían una revisión metodológica, incluidas varias que estaban en la versión original de estas slides. La segunda es la que más les va a servir en la práctica, porque explica por qué dos personas con la misma herramienta obtienen resultados tan distintos, y por qué esta clase existe.

---

## 8. Benchmarks: qué miden

<!-- ventana de contexto y tokens. Movida aca y reconvertida del dominio medico al de software. -->

### Content

**Un benchmark mide una tarea acotada en condiciones de laboratorio. Sirve para comparar modelos entre sí y dice poco sobre cómo va a rendir en el repositorio de cada equipo.**

- **Qué mide bien** Capacidad relativa entre modelos sobre una misma tarea cerrada: resolver un problema de programación con tests, responder una pregunta con respuesta única, completar una función.
- **Qué no mide** Trabajar sobre una base de código de años, con convenciones propias, deuda técnica y contexto que no está escrito en ninguna parte.
- **Contaminación** Un benchmark público lleva años circulando en la web cuando el modelo se entrena. Parte del puntaje puede ser memoria y no capacidad.
- **La medición que importa** El eval set propio, con casos reales del dominio. Es la misma conclusión de la sección de testing sistemático.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 50) — la slide original presentaba benchmarks clínicos (Med-PaLM 2 con 86,5% en MedQA, GPT-4 con 81,4% en USMLE, Claude 3 Opus con 62% en diagnóstico radiológico, "Gemini Mosaic" con 65%).
- `medpalm2-singhal.web.md` — registro de la versión médica de esta slide.
- `few-shot-learners-brown.web.md` — los autores de GPT-3 ya identifican la contaminación de datos como problema metodológico de los benchmarks sobre corpus web grandes.

### Speaker notes

Esta slide estaba al final de la sección de fundamentos, cortando el hilo entre ventana de contexto y economía de tokens con una tanda de benchmarks médicos. Acá funciona mejor, porque cierra la sección de aplicación con la pregunta correcta: qué significa de verdad que un modelo saque un puntaje. Las cifras médicas del original se retiraron y no las reemplacé por equivalentes de software inventadas. La tercera viñeta es la que más le sirve a esta audiencia y la que menos se dice: los benchmarks públicos llevan años indexados en la web, así que parte del puntaje puede ser recuerdo. La cuarta cierra el círculo con la sección cinco y es el mensaje que se llevan: el único benchmark que decide algo es el eval set propio.

---

# 8. Resumen y práctica

**Goal of this section:** Cerrar con lo que hay que retener y dejar los cuatro módulos de práctica como trabajo domiciliario.

---

## 1. ¡A practicar!

### Content

**📌 Trabajo domiciliario.** Los cuatro módulos son para hacer fuera de clase: 45 a 60 minutos en total. No entran en las dos horas y media de cursada.

| Foundational Models Fundamentals | Técnicas Avanzadas de Prompting |
|---|---|
| [aitutorial.dev/prompting/llm-foundamentals](https://aitutorial.dev/prompting/llm-foundamentals)<br>Ventana de contexto, tokens, limitaciones y modelo mental del completado. | [aitutorial.dev/prompting/advanced-techniques](https://aitutorial.dev/prompting/advanced-techniques)<br>CoT, self-consistency, extended thinking y prompt chaining aplicados. |

| Structured Prompt Engineering | Prompt Optimization & Testing |
|---|---|
| [aitutorial.dev/prompting/structured-prompt-engineering](https://aitutorial.dev/prompting/structured-prompt-engineering)<br>Los 6 componentes, etiquetas XML y salidas JSON en la práctica. | [aitutorial.dev/prompting/prompt-optimization-and-testing](https://aitutorial.dev/prompting/prompt-optimization-and-testing)<br>Evaluar, iterar y llevar prompts a producción con rigor. |

### Sources

- `AIG4B-Clase-3-Prompting.md.md` (slide 57)
- `aitutorial-advanced-techniques.web.md` y `aitutorial-structured-prompt-engineering.web.md` — los dos módulos que están procesados en el corpus.

### Speaker notes

Dejá claro el encuadre antes que nada: esto es tarea, no actividad de clase. Sumados al deck no entran en las dos horas y media. Recomendá el orden: primero fundamentos, último el de optimización y testing, que es el que más se apoya en los otros tres. Si vas a evaluar algo de esto, decilo acá. Y un aviso de honestidad: la agenda del deck original prometía además un "sistema de triage con LLM" como práctica, que nunca existió. La promesa se sacó de las siete agendas. Si querés reponerlo como trabajo práctico, el ejemplo de triage de issues de la sección cuatro y el pipeline de tickets de la sección cinco ya dejan la consigna casi armada.

---

# Conclusions

## 1. Key takeaways

### Content

- **El modelo completa, no razona.** Genera token a token, de izquierda a derecha, sin un motor de razonamiento aparte. Escribir los pasos intermedios es el cómputo, y por eso CoT, self-consistency, ToT, ReAct y prompt chaining tienen todas la misma forma: hacen que el modelo escriba más antes de responder.
- **Cada punto de calidad se paga.** En tokens, en latencia y en dinero. La habilidad central no es conocer las técnicas, es emparejar la técnica y el modelo con la dificultad real de la tarea. Pensar de más en una tarea fácil cuesta plata y a veces empeora la respuesta.
- **Un prompt es código.** Se versiona, se testea contra un eval set y se mide antes y después de cada cambio. Sin medición, cualquier mejora es una opinión, y eso vale igual para un chatbot que para un asistente de revisión de código.

### Sources

- `AIG4B-Clase-3-Prompting.md.md` — el deck original no tiene slide de cierre.
- `chain-of-thought-wei.web.md`, `self-consistency-wang.web.md`, `tree-of-thoughts-yao.web.md`, `react-yao.web.md` — las cuatro fuentes primarias detrás del primer takeaway.

### Speaker notes

Tres frases y ninguna es un resumen de la agenda. Son la tesis desplegada. La primera es el mecanismo y explica todo lo demás: si el modelo completa, entonces el trabajo del ingeniero es darle un patrón fácil de completar y hacerlo escribir antes de concluir. La segunda es la economía: no hay técnica gratis, y elegir de más es tan error como elegir de menos. La tercera es la disciplina, y es la que más rápido pueden aplicar el lunes. Cerrá con una pregunta abierta si te queda tiempo: cuál de las seis técnicas de la sección cinco usarían para el trabajo práctico que están cursando, y por qué. La respuesta correcta casi siempre es la más barata que alcanza.

---

# Open questions

- **Ventanas de contexto de proveedores no-Anthropic (1.3)** — GPT-5.4 (1M), Gemini 3 Pro (2M) y Llama 4 (10M) vienen del deck original, sin fuente en el corpus.
- **Tokens de un repositorio real (1.4)** — La segunda columna quedó cualitativa; falta medir un repo concreto para dar el número.
- **Caso citable de alucinación de APIs o paquetes (1.9)** — El fenómeno es conocido y no hay fuente con nombre y fecha en el corpus, a diferencia de Air Canada y el caso de los abogados.
- **Precios de OpenAI, Google y Meta (2.2)** — Cuatro filas de generación 2024 declaradas a marzo de 2026, sin verificar.
- **Donas de 3.4 (`slide-19-1.png`, `slide-19-2.png`)** — Dibujadas sobre el 40% y el 60% que se retiraron por falta de fuente. Falta decidir si se retiran o se reemplazan.
- **Donas de 5.2 (`slide-27-1.png` al 70%, `slide-27-2.png` al 35%)** — Ya no representan las cifras nuevas (74% y +17,9%). Falta re-render o reemplazo por un gráfico de barras del par 4% → 74%.
- **Ubicación de la slide de ReAct (5.11)** — Agregada después de ToT; podría ir pegada a prompt chaining.
- **Bloque duplicado 5.22 a 5.27** — Seis slides que repiten 5.19, 5.5, 5.7, 5.8, 5.9 y 5.10, residuo de edición del pptx. Se conservan por decisión del presentador; falta decidir si se entregan, se saltean en vivo o se retiran.
- **Cifras de la sección 6** — Las de la versión médica se retiraron al reconvertir al dominio de software (6.1, 6.3, 6.7) y no se reemplazaron por equivalentes inventados. Falta incorporar al corpus evidencia citable de adopción, productividad o benchmarks de software.
- **Trabajo práctico de triage con LLM (7.1)** — La agenda original lo prometía y nunca existió. Falta decidir si se arma.
- **Orden de las secciones** — El deck se entrega con "Modelos y costos" en segundo lugar (tokens → precio de los tokens). Las agendas del pptx original lo ponían quinto, después de las técnicas. Se alinearon las siete agendas al orden de entrega actual, sin reordenar secciones.
- **Sin registro en el corpus para las seis capturas nuevas (6.1 a 6.12)** — `anthropic-docs-effort`, `anthropic-docs-adaptive-thinking`, `anthropic-docs-extended-thinking`, `deepseek-r1-nature`, `deepseek-r1-arxiv` e `inference-time-scaling` viven en `research/web/` y las Sources de la sección 6 las citan por esa ruta. Falta correr el librarian para que existan como registros en `research/corpus/` y re-anclar las citas.
- **Largo de la sección 6** — pasó de 8 a 12 láminas al separar mecanismo, entrenamiento, configuración y costo. Falta decidir si entra en el tiempo de la clase; el candidato natural a fusión es 6.3 con 6.4 (la historia del refuerzo y el diseño de la recompensa), que se separaron porque el argumento del verificador le habla directo a esta audiencia.
- **Nombre de la sección 6** — se sigue llamando "Effort y thinking", que ya no cubre lo que hay adentro (mecanismo, entrenamiento por refuerzo, configuración, costo y la técnica de prompt). Falta decidir el nombre nuevo.
- **PNG obsoleto de 6.1 (`images/s4-1-1-tres-niveles-razonamiento.png`)** — dibuja la progresión de tres escalones que se retiró. El ASCII de 6.1 se reescribió como bloque ```ascii``` para que Polish lo vuelva a renderizar; el PNG viejo queda sin referencia.
- **Registro de las notas del orador** — las notas de la sección 6 quedaron en tuteo neutro por pedido explícito; las de las otras ocho secciones usan voseo ("Cerrá", "Decilo", "pagás"). Falta decidir si se normaliza el deck entero o si la sección 6 vuelve al voseo.
- **"10 o 30 segundos" de thinking nativo (6.12)** — la cifra viene de `AIG4B-Clase-3-Prompting.md.md` (slide 39), donde describía el extended thinking de presupuesto fijo. Ninguna de las capturas de la documentación da números de latencia, y el razonamiento adaptativo puede saltear el thinking por completo. Falta verificar o retirar.
- **Retrocompatibilidad del vocabulario "Thinking" / "Deep Thinking" (6.1)** — la lámina afirma que son nombres de producto de las apps de chat y que no figuran en la documentación de la plataforma. Lo segundo está verificado contra las tres capturas; lo primero viene de la lámina importada de `talksmith-mim`, sin fuente propia en este corpus.
- **Backlog cruzado desfasado** — `feedback_cycle.py find-closed-unmirrored` reporta 62 bullets `[closed]` de este Talk que nunca se espejaron a `config/feedback-backlog.md` (deuda anterior a esta ronda; las cinco de la sección 6 sí se espejaron). Falta decidir si se recuperan.
- Ver `research/corpus/AIG4B-Clase-3-Prompting.md.md` → *Inconsistencies / open questions* para el resto de los problemas detectados en el material original.

# Cut material

*(Ninguna slide fue retirada. Lo que sigue son fragmentos de contenido que salieron de la sección 6 en la reescritura del 2026-09-01, con su motivo. Todo lo demás que la revisión pedía cortar se recontextualizó, se partió en dos slides o se marcó con un `[open]`.)*

- **Sección 6, lámina "Del prompt al entrenamiento"** — "Y varios proveedores deshabilitan temperatura y top-p en esos modelos: la generación del bloque de razonamiento la controlan ellos, no vos." Motivo: ninguna de las capturas de la documentación oficial sostiene la afirmación; la fuente que la respaldaba ("Catálogo vigente de la API de Claude, corte 2026-06-24") no tiene registro en `research/corpus/`. Se puede reponer si se ingesta una fuente que la verifique.
- **Sección 6, lámina de effort** — "El default es `high`: una llamada que nunca lo tocó viene pagando razonamiento de sobra en cada tarea trivial." y "el default `high` es caro". Motivo: la documentación recomienda `high` como punto de partida y bajarlo cuando los evals muestren que la calidad aguanta, así que presentar el default como derroche contradice la fuente. El hecho verificable que reemplaza al juicio quedó en la lámina: `high` equivale a no setear el parámetro.
- **Sección 6, lámina de effort** — "`xhigh` es el mejor punto para código y tareas agénticas" como afirmación general. Motivo: es una recomendación por modelo, no global. Bajó a las notas del orador, calificada (Opus 4.7 y 4.8 arrancan en `xhigh`; Opus 5 y Fable 5.1 arrancan en `high`).
- **Sección 6, lámina "Extended thinking (Anthropic)"** — la tabla de tres columnas Debugging / Calidad / Trazabilidad. Motivo: duplicaba las tres razones de la lámina del ejemplo. El contenido sobrevive reescrito en 6.9 (Debugging / Estructura / Portabilidad); la lámina de origen quedó dedicada al mecanismo.
- **Sección 6, lámina "Razonamiento: cuánto piensa el modelo"** — la progresión de tres escalones "respuesta directa / thinking / deep thinking" como contenido principal, con su diagrama de calidad, latencia y costo subiendo juntos. Motivo: es vocabulario de interfaz de productos de chat, no de la API, y era el origen de la confusión que el presentador marcó. Sobrevive como uno de los cuatro cuadrantes del mapa de desambiguación de 6.1, etiquetado como vocabulario de producto.
