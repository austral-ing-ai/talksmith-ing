---
presentation: "Inteligencia General Generativa — materia optativa de grado de Ingeniería de Software, Universidad Austral"
class: "Inteligencia General Generativa: curso, reglas y fundamentos"
research: research/corpus/
description: Slides are grouped into Sections. Each Section contains one or more Slides.
presenter: "Paulo Veiga, Claudio Riguetti y Marco Sorondo — docentes, Universidad Austral"
audience: "Estudiantes universitarios de Ingeniería de Software con una base técnica fuerte."
duration: "90 minutos"
date: "2026-08"
---

# Thesis

**Claim:** La IA generativa amplía la capacidad de quienes diseñan, construyen y operan software cuando la usan con criterio técnico, validación y responsabilidad.

**Why it matters:** La materia aporta fundamentos para evaluar modelos, construir prototipos y reconocer límites antes de incorporar IA a productos y procesos de ingeniería.

**Presenter feedback:**

---

# Agenda

**Narrative arc:** La clase conserva la secuencia completa del PPTX de referencia: encuadre de la materia, fundamentos de IA, taxonomía de problemas, modelos fundacionales, conclusiones y anexo. Cada diapositiva mantiene su posición; la adaptación reemplaza el dominio de Biomedicina por Ingeniería de Software sin condensar el texto ni las notas.

**Sections (in delivery order):

- 1. Bienvenidos
- 2. Por qué cursarla
- 3. Logística
- 4. Fundamento de AI
- 5. Taxinomia de Problemas
- 6. Modelos Fundacionales
- 7. Datos
- 8. Ecosistema Actual
- 9. Cierre y anexo

**Presenter feedback:**

---

# 1. Bienvenidos

**Goal of this section:** Presentar la materia y alinear expectativas sobre el enfoque, los docentes y el modo de trabajo.

**Presenter feedback:**

---

## 1. Inteligencia General Generativa

<!-- template: statement -->

### Content

Clase 1: Bienvenida y Logistica

Autor: Paulo Gustavo Veiga
Ultima Modification: Marzo, 2026

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 1; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 1.

Discurso Sugerido: "Bienvenidos. Hoy vamos a desmitificar la Inteligencia Artificial. Intuitivamente, solemos pensar en la IA como 'máquinas haciendo cosas que requerirían inteligencia si las hiciera un humano'. Pero si queremos ser rigurosos, como proponen Russell y Norvig, la IA es el diseño de agentes racionales: sistemas que perciben su entorno y toman acciones para maximizar sus posibilidades de éxito en un objetivo dado. No se trata de crear humanos sintéticos, sino de resolver problemas complejos con matemáticas a gran escala."

Contexto Técnico Profundo: La definición de agente racional evita el debate filosófico sobre la "conciencia" y se centra en la función matemática que mapea secuencias de percepciones a acciones (arquitectura de agentes).

Enlace Recomendado: Sitio oficial del libro "Artificial Intelligence: A Modern Approach" (Russell & Norvig)

### Presenter feedback

---

## 2. Bienvenidos!

<!-- template: content-image -->
<!-- design: column-right -->

### Content

Inteligencia General Generativa

![Ilustración de bienvenida](images/bienvenida-hello.jpeg)

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 2; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 2.

Primera vez que dictamos esta materia (contar brevemente la historia de la materia).

### Presenter feedback

---

## 3. Que es Inteligencia Artificial Generativa ?

<!-- template: content-image -->
<!-- design: column-right -->

### Content

Bienvenidos! Este curso explorará los fundamentos, aplicaciones y desafíos de la Inteligencia Artificial Generativa, un campo revolucionario que está transformando nuestra interacción con la tecnología.​
A lo largo de este cuatrimestre, analizaremos los conceptos básicos de la GenAI, los modelos de lenguaje generativos, la visión artificial, y los aspectos éticos relacionados con esta tecnología emergente.​

![Ilustración sobre inteligencia artificial](images/que-es-ia-generativa.jpeg)

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 3; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 3.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## Qué esperamos que se lleven

<!-- template: concept-breakdown -->

### Content

Una materia para entender cómo funcionan los modelos y aprender a construir con ellos con criterio de Ingeniería de Software.

Meternos en los modelos

Van a poder explicar qué hacen los transformers, cómo intervienen los datos, el entrenamiento, la inferencia y la evaluación; no sólo usar una interfaz de chat.

Práctica hands-on

Las clases combinan teoría y práctica: notebooks, repositorios, prompts, herramientas y casos concretos para experimentar, implementar, probar y documentar.

Criterio de ingeniería

El objetivo es usar IA generativa sin delegar el juicio técnico: evaluar salidas, reconocer límites y diseñar flujos con trazabilidad, seguridad y control humano.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 11; adaptación y reubicación)

### Speaker notes

Este slide anticipa el tipo de materia: no se trata sólo de aprender a usar una herramienta. Vamos a entrar en cómo se construyen y evalúan los modelos, y en cada clase llevar los conceptos a una práctica concreta de ingeniería.

### Presenter feedback

---

## 4. Antes que nada…

<!-- template: figures -->

### Content

![Ilustración de Paulo Veiga](images/docente-paulo-veiga.jpeg)

Paulo Veiga

Email: pveiga@austral.edu.ar

![Ilustración de Marco Sanchez Sorondo](images/docente-marco-sorondo.jpeg)

Marco Sanchez Sorondo

Email: msanchezSorondo@austral.edu.ar

![Foto de Claudio Riguetti](images/docente-claudio-riguetti.png)

Claudio Riguetti

Docente

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 4; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 4.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

# 2. Por qué cursarla

**Goal of this section:** Explicar por qué la IA generativa importa para la formación y la práctica de Ingeniería de Software.

**Presenter feedback:**

---

## 5. ¿Por qué esta materia?

<!-- template: concept-breakdown -->

### Content

¿Por qué esto es relevante para tu carrera?

La IA generativa cambia la forma de analizar requisitos, escribir código, crear pruebas, mantener documentación y operar sistemas.

El mercado ya la incorpora

Las organizaciones suman asistentes de IA a sus flujos de desarrollo. Quienes entiendan sus límites y sepan evaluarlos pueden aportar criterio técnico desde el primer día.

Ingeniería de Software es un área de alto impacto

Copilotos de código, revisión de cambios, generación de pruebas, búsqueda sobre repositorios y soporte a incidentes ya afectan tareas reales de los equipos.

Diferenciación profesional

Un ingeniero que entiende IA puede liderar proyectos, definir controles de calidad y conversar con producto, seguridad, datos y negocio.

El futuro ya está disponible

ChatGPT, Claude, Gemini, GitHub Copilot y modelos abiertos ya forman parte del entorno de trabajo. La decisión relevante consiste en usarlos con evidencia, pruebas y responsabilidad.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 5; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 5.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 6. ¿Por qué esta materia?

<!-- template: concept-breakdown -->

### Content

El Impacto de GenAI en la Economía

Impulso histórico a la productividad

Automatización de tareas cognitivas y repetitivas, actuando como un "copiloto" para los trabajadores.

Creación de valor masivo

Se estima que la GenAI podría añadir entre 2,6 y 4,4 billones de dólares anuales a la economía global (equivalente al PIB de un país como Reino Unido).

Transformación de funciones corporativas

Impacto directo en operaciones, marketing, ventas, atención al cliente y desarrollo de software.

Nuevas industrias

Aparición de modelos de negocio inéditos y roles especializados (ej. ingeniería de prompts, auditoría algorítmica).

Fuente: McKinsey & Company — The economic potential of generative AI

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 6; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 6.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 7. ¿Por qué esta materia?

<!-- template: image-full -->

### Content

Impacto Por Industria y Funcionalistas

![Impacto de la IA generativa por industria y función](images/impacto-por-industria.jpeg)

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 7; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 7.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 8. ¿Por qué esta materia?

<!-- template: concept-breakdown -->

### Content

Transformación en Ingeniería de Software

Aceleración del desarrollo de software

Los modelos pueden asistir en lectura de repositorios, generación de código, explicación de errores y creación de pruebas. El equipo conserva la responsabilidad de revisar, integrar y desplegar.

Productos más adaptables

La IA permite explorar interfaces, personalizar flujos y analizar grandes volúmenes de feedback, tickets y telemetría. La personalización exige datos autorizados y criterios explícitos.

Mejora de calidad y seguridad

Los equipos pueden usar IA para detectar patrones de fallas, proponer casos de prueba, resumir incidentes y encontrar documentación relevante. Ninguna sugerencia reemplaza una validación técnica.

Eficiencia operativa

La automatización de runbooks, soporte y documentación puede devolver tiempo para resolver problemas de mayor valor. Los procesos necesitan registros, permisos y mecanismos de reversión.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 8; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 8.

Discurso sugerido:

“La IA generativa puede acelerar partes del trabajo de ingeniería, pero no convierte un problema ambiguo en una solución correcta por sí sola. Puede leer un repositorio, proponer una migración, escribir pruebas o resumir un incidente. El equipo sigue teniendo que definir el objetivo, revisar el cambio y hacerse cargo de las consecuencias.”

Contexto técnico: los asistentes de código trabajan sobre representaciones incompletas del sistema. Pueden desconocer dependencias privadas, decisiones de arquitectura, reglas de negocio, restricciones de seguridad o el estado actual de producción. Un equipo confiable combina la velocidad de propuesta del modelo con pruebas automatizadas, revisión de pares, despliegues graduales y observabilidad.

Caso 1. Desarrollo y mantenimiento

Un modelo puede explicar una función compleja, proponer un refactor y generar pruebas para los casos que el desarrollador enumera. El equipo debe ejecutar esas pruebas, revisar cambios de comportamiento y comprobar que el resultado respeta las convenciones del repositorio.

Caso 2. Conocimiento técnico

Un sistema de búsqueda semántica puede recuperar decisiones de arquitectura, tickets y documentación. El resultado debe mostrar de dónde obtuvo cada respuesta para que quien consulta pueda verificar si esa información sigue vigente.

Caso 3. Calidad y seguridad

Un asistente puede proponer reglas de análisis estático, casos de prueba y correcciones para vulnerabilidades conocidas. Las recomendaciones no reemplazan una revisión de seguridad ni dan permiso para ejecutar código sin aislamiento.

Caso 4. Operación

Un agente puede resumir alertas, sugerir hipótesis y ejecutar acciones acotadas de un runbook. El diseño debe limitar permisos, registrar cada acción y permitir detener o revertir una automatización.

Pregunta para la clase: “¿Qué evidencia pedirían antes de aceptar una modificación de código generada por un modelo?”

Punto clave: la IA amplifica las habilidades de un equipo cuando el proceso conserva responsabilidad, trazabilidad y controles humanos.

### Presenter feedback

- [closed] 2026-08-03 — "Borra Fuente de referencia: el PPTX original usa ejemplos de impacto sectorial; esta versión los traslada a Ingeniería de Software."
  Resolution: Se eliminó la referencia editorial del contenido visible de la diapositiva 8.

---

## 9. ¿Por qué esta materia?

<!-- template: concept-breakdown -->

### Content

Problemas actuales de la IA en software

Alucinaciones y respuestas falsas

Los modelos pueden generar código, APIs, librerías o explicaciones incorrectas con tono convincente. Una salida debe pasar por pruebas, revisión y contraste con documentación oficial.

Sesgos en los datos

Los datos de entrenamiento y los repositorios históricos contienen decisiones, desigualdades y prácticas inseguras. Un modelo puede reproducirlas sin advertirlo.

Privacidad y protección de datos

Prompts, adjuntos y contexto pueden incluir código propietario, secretos, datos personales o información de clientes. El equipo debe conocer dónde se procesa y retiene cada dato.

Sesgo de automatización

Un resultado sugerido por una herramienta puede recibir confianza excesiva. La revisión humana necesita criterios y tiempo asignado, no solo una aprobación nominal.

Acceso desigual

El costo de modelos, cómputo y conectividad condiciona quién puede experimentar, construir y desplegar soluciones.

Impacto ambiental

Entrenar y operar modelos a gran escala requiere energía, agua e infraestructura. El costo ambiental forma parte de la decisión de arquitectura.

Degradación de habilidades técnicas

Un uso sin comprensión puede erosionar la capacidad de depurar, diseñar y operar sistemas cuando la herramienta falla o entrega una respuesta errónea.

Fuente de referencia: el PPTX original organiza estos riesgos a partir de la guía de la OMS; esta adaptación los aplica al trabajo de software.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 9; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 9.

Cómo presentar este slide

Apertura: “Vimos qué puede aportar la IA generativa a un equipo de software. Ahora revisemos los problemas que aparecen cuando una salida se acepta sin evidencia, cuando los datos no tienen controles o cuando un sistema obtiene permisos que no debería tener.”

1. Alucinaciones y respuestas falsas

Explicación: los modelos generan secuencias plausibles a partir de patrones. Pueden inventar una API, recomendar un paquete inexistente, omitir una condición de seguridad o explicar de forma convincente un comportamiento equivocado.

Ejemplo: un desarrollador pide una integración con una librería y el modelo produce funciones que no existen en esa versión. El código puede compilar si se agregan sustitutos improvisados, pero falla en producción o deja un comportamiento inseguro. Una revisión debe contrastar la propuesta con documentación oficial, pruebas y el contexto del repositorio.

Pregunta para la clase: “¿Aceptarían un cambio que el modelo no puede justificar con una fuente y una prueba reproducible?”

2. Sesgos en los datos

Explicación: los modelos aprenden de datos históricos. Repositorios públicos y documentación contienen decisiones de diseño, dependencias desactualizadas, prácticas inseguras y sesgos sobre quién usa un producto.

Ejemplo: un sistema entrenado con tickets históricos puede asignar menor prioridad a problemas que afectan a un grupo poco representado. Un asistente de código puede sugerir patrones antiguos porque aparecen con frecuencia en sus datos, aunque el proyecto ya los haya reemplazado.

Punto clave: los equipos necesitan revisar qué datos entran a un sistema, qué casos faltan y cómo miden errores por segmento o contexto.

3. Privacidad y protección de datos

Explicación: un prompt puede incluir código propietario, claves, información de clientes, registros de incidentes o decisiones internas. El proveedor puede almacenar, procesar o usar ese contexto según el contrato y la configuración elegida.

Ejemplo: si alguien copia una traza con un token de acceso o una base de datos de prueba con datos personales, el equipo puede exponer información sensible fuera de su perímetro. Las políticas deben definir qué puede enviarse, qué se debe anonimizar y qué modelos se autorizan para cada clase de dato.

Punto clave: un chat no reemplaza un canal seguro ni una revisión de cumplimiento.

4. Sesgo de automatización

Explicación: una respuesta bien escrita puede recibir más confianza que una respuesta verificada. El riesgo aumenta cuando una herramienta aparece dentro del editor, el pipeline o el panel de operaciones.

Ejemplo: un asistente propone silenciar una alerta porque la clasifica como ruido. Si el operador acepta sin revisar señales relacionadas, puede ocultar un incidente real. La interfaz debe mostrar evidencia, incertidumbre y mecanismos para inspeccionar la decisión.

5. Acceso desigual

Explicación: los modelos de mayor capacidad requieren suscripciones, infraestructura y datos que no todos los equipos pueden pagar. La calidad también varía por idioma, contexto cultural y disponibilidad de datos locales.

Ejemplo: una empresa grande puede integrar modelos privados con sus repositorios y telemetría. Un equipo pequeño puede depender de una herramienta pública con límites de uso y menor control sobre privacidad. La diferencia modifica quién puede experimentar y quién puede construir productos competitivos.

6. Impacto ambiental

Explicación: entrenar y servir modelos consume energía, agua e infraestructura. Una arquitectura que invoca un modelo en cada interacción puede elevar costo y consumo sin mejorar la experiencia.

Ejemplo: antes de agregar una llamada a un modelo, el equipo puede comparar alternativas: una regla determinista, una búsqueda, un modelo pequeño, un caché o una revisión asíncrona. La decisión debe considerar precisión, latencia, costo y consumo.

7. Degradación de habilidades técnicas

Explicación: un uso continuo de asistentes sin comprensión puede reducir la práctica de depurar, modelar datos, leer documentación y diseñar pruebas. El problema aparece con fuerza cuando una herramienta falla, cambia de proveedor o produce una salida incorrecta.

Ejemplo: si un equipo acepta parches generados durante meses sin revisar arquitectura ni pruebas, pierde contexto sobre el sistema. Durante un incidente grave, ese equipo tarda más en decidir qué hipótesis descartar y qué acción es segura.

Punto clave: la IA debe ampliar la capacidad de ingeniería, no sustituir el aprendizaje ni la responsabilidad técnica.

Cierre para debate:

“¿Qué controles deberían exigir una universidad, una empresa y un equipo de producto antes de permitir que un agente modifique datos, despliegue código o responda a usuarios?”

### Presenter feedback

---

## 10. ¿Por qué esta materia?

<!-- template: concept-breakdown -->

### Content

El riesgo macroeconómico y la transición abrupta

La crisis global de capacidades, escenario hipotético

El escenario permite discutir qué ocurre si la productividad crece más rápido que la formación, la redistribución de oportunidades y los controles de adopción.

El “PIB fantasma”

Las empresas pueden registrar más producción gracias a la automatización mientras parte del mercado laboral pierde tareas de entrada y capacidad de consumo.

Desplazamiento del empleo inicial

Roles junior y tareas repetitivas pueden cambiar antes de que universidades y empresas ofrezcan nuevas rutas de aprendizaje, mentoría y especialización.

Espiral deflacionaria y concentración

Pocos proveedores de cómputo, modelos y datos pueden capturar una porción desproporcionada del valor. Los equipos quedan atados a precios, políticas y capacidades ajenas.

Pregunta para debate: ¿qué decisiones de diseño, formación y regulación reducen estos riesgos sin bloquear la innovación?

Fuente de referencia: el PPTX original presenta un escenario hipotético de transición abrupta.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 10; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 10.

. Technology improved slowly enough that humans could adapt. Intelligence, the ability to analyze, decide, create, persuade, and coordinate, was the thing that could not be replicated at scale.

Human intelligence derived its inherent premium from its scarcity. Every institution in our economy, from the labor market to the mortgage market to the tax code, was designed for a world in which that assumption held.

We are now experiencing the unwind of that premium. Machine intelligence is now a competent and rapidly improving substitute for human intelligence across a growing range of tasks

### Presenter feedback

---

# 3. Logística

**Goal of this section:** Acordar cómo se cursa, cómo se entrega el trabajo y cómo se compone la evaluación.

**Presenter feedback:**

---

## 13. Logística de la materia

<!-- template: concept-breakdown -->
<!-- format: grid -->

### Content

Cómo vamos a trabajar

01 · Clases

Son 14 clases, los miércoles. En cada una vamos a mezclar conceptos, modelos, ejemplos y práctica.

02 · De la idea a la práctica

Primero vemos la idea y la discutimos; después la llevamos a notebooks, repositorios, herramientas y casos concretos.

03 · Trabajo en equipo

Van a trabajar en equipo, probar cosas, comparar resultados y dejar registro de las decisiones.

04 · Participación y evaluación

Esperamos presencia y participación activa. Cada dos clases habrá un entregable práctico; la nota final combina esos trabajos con el proyecto final. Las reglas y la ponderación estarán claras antes de la primera entrega.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 13; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 13.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 14. Logística de la materia

<!-- template: concept-breakdown -->
<!-- format: grid -->

### Content

Entregables de clase

Forman parte de la evaluación junto con el trabajo final.

01 · Ritmo

Un entregable cada dos clases, relacionado con los temas vistos.

02 · Equipo

Se trabaja en equipos de cuatro personas.

03 · Trabajo durante la clase

La mayor parte del trabajo se completa durante la clase.

04 · Evidencia

Cada equipo debe dejar trazabilidad de decisiones, prompts, código, pruebas y fuentes usadas.

05 · Entrega obligatoria

Se entrega por el canal que indique la cátedra, con repositorio o artefactos reproducibles cuando corresponda.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 14; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 14.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 15. Logística de la materia

<!-- template: concept-breakdown -->
<!-- format: grid -->

### Content

Trabajo final

Un proyecto propio que aplique conceptos de la materia a un problema de Ingeniería de Software.

Equipo y alcance

Equipos de cuatro personas.

El equipo debe ser el mismo que realizó los trabajos prácticos.

La cátedra orientará el alcance, la evidencia y la forma de evaluar el resultado.

Entregables

Video breve de demostración que explique el problema, la solución y sus límites.

Código desplegado o ejecutable, con instrucciones de reproducción.

Documentación del diseño, datos utilizados, estrategia de evaluación, riesgos y decisiones de seguridad.

Evaluación

Máximo detalle y evidencia técnica; la evaluación considera tanto el resultado como la capacidad de justificarlo.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 15; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 15.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## Evaluación

<!-- template: stat -->

### Content

Cómo se compone la nota final

40%

Entregables de clase

60%

Trabajo final

**Importante:** Las entregas fuera de término impactan en la nota final.

### Sources

- Criterio de evaluación de la cátedra (2026)

### Speaker notes

La evaluación combina el trabajo sostenido durante la cursada con la capacidad de integrar lo aprendido en un proyecto final.

### Presenter feedback

---

## 16. Contenidos de la Materia

<!-- template: concept-breakdown -->
<!-- format: editorial -->

### Content

01

Módulo 1: Fundamentos de IA, arquitectura de LLM y entrenamiento

Clases 1–4

02

Módulo 2: Ingeniería de prompts, RAG y desarrollo asistido por IA

Clases 5–8

03

Módulo 3: Generación multimodal, visión e interfaces

Clases 9–12

04

Módulo 4: Agentes, evaluación, ética, seguridad y regulación

Clases 12–14

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 16; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 16.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 17. Preguntas

<!-- template: closing-hero -->

### Content

Abrimos la conversación.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 17; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 17.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

# 4. Fundamento de AI

**Goal of this section:** Construir un lenguaje compartido sobre IA, redes neuronales e historia del campo.

**Presenter feedback:**

---

## 1. Inteligencia General Generativa

<!-- template: statement -->

### Content

Clase 1: Fundamentos, Modelos y el Ecosistema Actual

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 18; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 18.

Discurso Sugerido: "Bienvenidos. Hoy vamos a desmitificar la Inteligencia Artificial. Intuitivamente, solemos pensar en la IA como 'máquinas haciendo cosas que requerirían inteligencia si las hiciera un humano'. Pero si queremos ser rigurosos, como proponen Russell y Norvig, la IA es el diseño de agentes racionales: sistemas que perciben su entorno y toman acciones para maximizar sus posibilidades de éxito en un objetivo dado. No se trata de crear humanos sintéticos, sino de resolver problemas complejos con matemáticas a gran escala."

Contexto Técnico Profundo: La definición de agente racional evita el debate filosófico sobre la "conciencia" y se centra en la función matemática que mapea secuencias de percepciones a acciones (arquitectura de agentes).

Enlace Recomendado: Sitio oficial del libro "Artificial Intelligence: A Modern Approach" (Russell & Norvig)

### Presenter feedback

- [closed] 2026-08-03 — "La diapositiva 'Inteligencia General Generativa — Clase 1: Fundamentos, modelos y ecosistema actual' necesita un estilo mucho mejor, quote o similar."
  Resolution: Se cambió la diapositiva de divider a statement para separar el título principal del subtítulo de clase, sin tratarlo como una cita.

---

## 2. ¿Qué es la Inteligencia Artificial?

<!-- template: single-point -->

### Content

De la teoría a la intuición

Intuicion

No se trata de programar reglas explícitas para cada situación. Se trata de construir sistemas que aprenden patrones a partir de datos y los generalizan a situaciones nuevas, de forma parecida a cómo aprende el cerebro humano.

Un Poco mas Formal

La IA es el diseño de agentes racionales: sistemas que perciben su entorno y toman acciones para maximizar sus posibilidades de éxito en un objetivo dado. No se trata de crear humanos sintéticos, sino de resolver problemas complejos con matemáticas a gran escala.
— Russell & Norvig

La IA no es magia: es estadística, álgebra lineal y grandes cantidades de datos bien organizados.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 19; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 19.

Diapositiva 1: ¿Qué es la Inteligencia Artificial? (De la teoría a la intuición)

Discurso Sugerido: "Bienvenidos. Hoy vamos a desmitificar la Inteligencia Artificial. Intuitivamente, solemos pensar en la IA como 'máquinas haciendo cosas que requerirían inteligencia si las hiciera un humano'. Pero si queremos ser rigurosos, como proponen Russell y Norvig, la IA es el diseño de agentes racionales: sistemas que perciben su entorno y toman acciones para maximizar sus posibilidades de éxito en un objetivo dado. No se trata de crear humanos sintéticos, sino de resolver problemas complejos con matemáticas a gran escala."

Contexto Técnico Profundo: La definición de agente racional evita el debate filosófico sobre la "conciencia" y se centra en la función matemática que mapea secuencias de percepciones a acciones (arquitectura de agentes).

Enlace Recomendado: Sitio oficial del libro "Artificial Intelligence: A Modern Approach" (Russell & Norvig)

### Presenter feedback

---

## 3. Una Breve Historia (Parte 1)

<!-- template: timeline -->

### Content

De Turing al primer invierno — 1948 a 1997

1

1948 — La Teoría de la Información (Claude Shannon)

Shannon publica "A Mathematical Theory of Communication". Define conceptos como bit, entropía y canal de comunicación, sentando las bases matemáticas para el procesamiento de datos.

2

1950 — El test de Turing

Alan Turing propone la pregunta: "¿Pueden pensar las máquinas?" Nace el marco conceptual de la IA.

3

1956 — Nacimiento oficial

Conferencia de Dartmouth. John McCarthy acuña el término "Inteligencia Artificial". Comienza la primera era de optimismo.

4

1958 — El Perceptrón (Frank Rosenblatt)

Rosenblatt crea la primera red neuronal artificial capaz de aprender. Minsky y Papert demostrarían en 1969 sus limitaciones, desencadenando el primer "invierno de la IA".

5

1980-90s — Sistemas expertos e inviernos

Auge y caída de los sistemas basados en reglas. Los "inviernos de la IA" frenan la inversión y la investigación.

6

1986 — Backpropagation revoluciona el aprendizaje

Rumelhart, Hinton y Williams popularizan el algoritmo de retropropagación del error, permitiendo entrenar redes neuronales multicapa.

7

1997 — Deep Blue vence a Kasparov

La supercomputadora de IBM derrota al campeón mundial de ajedrez Garry Kasparov. Primera victoria de la IA sobre el mejor humano en un juego de estrategia complejo.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 20; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 20.

Diapositiva 2: Una Breve Historia (De Turing a la Generación)

Discurso Sugerido: "La IA no nació con ChatGPT. Sus bases matemáticas tienen más de 70 años. Desde el Test de Turing en 1950 y la Conferencia de Dartmouth en 1956, pasamos por 'inviernos de la IA' por falta de cómputo. El punto de inflexión llegó en 2012 con las redes neuronales profundas (AlexNet) y en 2017 con una arquitectura llamada 'Transformer', creada por Google, que cambió las reglas del juego y nos trajo a la era generativa en la que estamos hoy."

Contexto Técnico Profundo: El artículo "Attention Is All You Need" (2017) introdujo el mecanismo de autoatención (self-attention), eliminando la necesidad de procesamiento secuencial (RNNs) y permitiendo la paralelizabilidad masiva en GPUs, lo que habilitó el entrenamiento de los LLMs modernos.

Enlace Recomendado: Paper original: "Attention Is All You Need" (arXiv:1706.03762)

--

Excelente elección! Vamos a sumergirnos El Juego de la Imitación .

Para entender por qué Alan Turing propuso este experimento, primero debemos notar que en 1950 era casi imposible definir qué es "pensar" de una forma que todos aceptaran. Turing decidió que, si una máquina podía actuar de manera indistinguible a un ser humano, entonces debíamos tratarla como si tuviera inteligencia.

¿Cómo funciona el juego?

El experimento original involucra a tres participantes en habitaciones separadas:

Un interrogador humano.

Un hombre (o una máquina, en la versión de IA).

Una mujer (o un humano, que sirve de control).



-

Máquina de Turing/Universal no es un objeto físico con engranajes o cables, sino un modelo matemático que Alan Turing ideó en 1936. Su objetivo era definir, de una vez por todas, qué significa que algo sea "calculable".



-> Aunque suena extremadamente simple, Turing demostró que este modelo puede resolver cualquier problema matemático que tenga una solución lógica. Es el "plano" original de cómo funciona cualquier procesador moderno.

--

El Problema de la Parada

Turing demostró que existen límites fundamentales en lo que una máquina puede calcular, sin importar cuánta memoria o velocidad tenga. El ejemplo más famoso es el Problema de la Parada (Halting Problem) .

Imagina que quieres crear un programa maestro que pueda analizar cualquier otro programa y decirte, antes de ejecutarlo, si ese programa eventualmente terminará su tarea o si se quedará "colgado" en un bucle infinito para siempre.

Turing demostró mediante la lógica que es imposible construir tal programa.

Para probarlo, utilizó una técnica llamada "reducción al absurdo":

Supongamos que existe un programa llamado CALCULADOR_DE_PARADA.

Creamos un segundo programa "rebelde" que consulta al primero.

Si el CALCULADOR dice que el programa parará, el rebelde entra en un bucle infinito. Si el CALCULADOR dice que no parará, el rebelde se detiene inmediatamente.

Esto crea una paradoja lógica (como decir "esta oración es falsa"). Si el programa intenta analizarse a sí mismo, la lógica se rompe.





Un sistema experto es un programa que intenta imitar el razonamiento de un experto humano en un dominio específico.

Deap blue - IA = búsqueda + poder de cómputo + heurísticas

### Presenter feedback

---

## 4. Redes Neuronales — Estructura y Celda Básica

<!-- template: content-image -->
<!-- design: split-left -->

### Content

De la neurona biológica al perceptrón artificial

Red Neuronal Simple

Anatomía de una Neurona Artificial

🔢 Entradas (x₁, x₂, ..., xₙ)

Señales de entrada — datos crudos o salidas de neuronas anteriores.

⚖️ Pesos (w₁, w₂, ..., wₙ)

Cada entrada se multiplica por un peso. El modelo aprende ajustando estos valores durante el entrenamiento.

∑ Suma Ponderada + Bias

z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
El bias permite desplazar la función de activación.

⚡ Función de Activación f(z)

Introduce no-linealidad. Ejemplos: ReLU, Sigmoid, Tanh. Determina si la neurona "se activa" y con qué intensidad.

Output: ŷ = f(z)

![Estructura de una neurona artificial](images/neurona-artificial.jpeg)

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 21; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 21.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 5. Una Breve Historia (Parte 2)

<!-- template: timeline -->

### Content

Del deep learning a la era generativa — 2011 a 2022

1

2011 — Watson gana en Jeopardy!

IBM Watson derrota a los mejores campeones humanos del concurso de preguntas. Demuestra comprensión del lenguaje natural a gran escala.

2

2012 — La revolución del deep learning

AlexNet gana ImageNet con una ventaja histórica. Las redes neuronales profundas y las GPUs cambian todo. Codificar a entrenar.

3

2016 — AlphaGo vence a Lee Sedol

DeepMind derrota al campeón mundial de Go, un juego con más combinaciones posibles que átomos en el universo. Considerado imposible para la IA hasta ese momento. Toma decisiones estratégicas en un espacio de búsqueda enorme.

4

2017 — Atención es todo

Google publica "Attention Is All You Need". Nace la arquitectura Transformer, base de todos los modelos modernos.

5

2020s — Era generativa

GPT-3, ChatGPT, Gemini, Claude. Los Foundation Models democratizan el acceso a capacidades de IA sin precedentes.

6

2022 — ChatGPT rompe internet

OpenAI lanza ChatGPT. Alcanza 100 millones de usuarios en 2 meses, el producto de mayor crecimiento en la historia.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 22; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 22.

AlexNet

Más de 14 millones de imágenes

Más de 20.000 categorías

2017

Eliminar las redes recurrentes (RNN/LSTM) y usar solo mecanismos de atención.

¿Por qué fue tan revolucionario?

1. Paralelización total

Las RNN procesaban secuencialmente.

Los Transformers pueden procesar todo en paralelo.

 Mucho más rápidos en GPUs.

2. Mejor manejo de contexto largo

Las RNN olvidaban información lejana.

La atención permite conectar cualquier palabra con cualquier otra directamente.

3. Escalabilidad

La arquitectura escala muy bien con:

Más datos

Más parámetros

Más cómputo

Y eso abrió la puerta a modelos gigantes.

### Presenter feedback

---

# 5. Taxinomia de Problemas

**Goal of this section:** Distinguir familias de problemas y vincularlas con sistemas de software.

**Presenter feedback:**

---

## 1. La Taxonomía de Problemas

<!-- template: concept-breakdown -->

### Content

¿Qué tipos de problemas resuelve la IA?

Predicción

Aprender X → Y a partir de datos etiquetados. Incluye clasificación y regresión.

Percepción

Extraer estructura de señales sensoriales: imagen, audio, video.

Representación

Aprender embeddings y espacios latentes que capturan relaciones entre datos.

Decisión Secuencial

Maximizar recompensa acumulada. Formalizado como Reinforcement Learning.

Búsqueda / Planificación

Encontrar la mejor secuencia de acciones en un espacio de estados.

Razonamiento Simbólico

Manipular símbolos y reglas IF–THEN para derivar conclusiones lógicas.

Generación

Producir nuevas muestras coherentes: texto, imagen, audio, código. Infinita cantidad de outputs.

💡 Un auto autónomo combina percepción + decisión secuencial + planificación

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 23; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 23.

Diapositiva 3: La Taxonomía de Problemas: ¿Qué resolvemos?

Discurso Sugerido: "Para entender la IA, hay que verla como una caja de herramientas. ¿Qué problemas resuelve? Principalmente, podemos categorizarlos en siete áreas clave. Por ejemplo, en Predicción, la IA puede predecir categorías o valores continuos, como si una planta tiene una plaga o estimar el rendimiento de una cosecha. En Percepción, la IA extrae significado de imágenes o audio. La Generación nos permite crear nuevo contenido. Los sistemas de Decisión Secuencial aprenden a tomar series de acciones para lograr objetivos, como en los juegos. Y el Razonamiento Simbólico permite a la IA usar reglas lógicas."

Contexto Técnico Profundo: La Predicción mapea entradas $X$ a salidas $Y$ (discretas o continuas). La Percepción extrae características de datos crudos. La Representación busca estructuras subyacentes (embeddings). La Generación modela distribuciones de probabilidad. La Decisión Secuencial optimiza acciones a lo largo del tiempo (Reinforcement Learning). La Búsqueda y Planificación encuentran secuencias óptimas de acciones. El Razonamiento Simbólico se basa en sistemas expertos y lógica.

### Presenter feedback

---

## Predicción

<!-- template: statement -->

### Content

Aprender una función X → Y a partir de datos etiquetados.

El modelo mapea entradas a salidas conocidas y minimiza el error. Esta categoría sostiene muchas aplicaciones industriales.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 24; adaptación separada)

### Speaker notes

Presentar Predicción como una de las familias más frecuentes de problemas de IA antes de recorrer sus variantes.

### Presenter feedback

---

## 2. La taxonomía de problemas

<!-- template: concept-breakdown -->
<!-- format: editorial -->

### Content

Ejemplos de problemas predictivos

Clasificación binaria

Spam/no spam · fraude/legítimo · incidente crítico/no crítico

Clasificación multiclase

Tipo de ticket · categoría de error · prioridad de soporte

Regresión

Esfuerzo estimado · demanda de infraestructura · tiempo de resolución

Series temporales

Ventas · uso de recursos · tráfico · volumen de alertas

Herramientas: Scikit-learn · XGBoost · LightGBM · TensorFlow · PyTorch · AutoML

Métricas: Accuracy · F1-Score · AUC-ROC · MAE · RMSE · R²

Hito de referencia: AlexNet mostró en 2012 que una red profunda entrenada a escala podía mejorar de forma sustancial la clasificación de imágenes.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 24; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 24.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 3. La taxonomía de problemas

<!-- template: concept-breakdown -->

### Content

Percepción

Extraer estructura significativa de señales sensoriales y documentos.

Problemas típicos

Clasificación de imágenes · detección de objetos · OCR · reconocimiento de voz · análisis de video.

Aplicaciones en software

Procesamiento de facturas y formularios · accesibilidad · moderación de contenido · análisis de capturas de interfaz · extracción de información de documentos.

Herramientas: OpenCV · YOLO · PyTorch · TensorFlow · Whisper · modelos multimodales.

Hito de referencia: los modelos de visión modernos superaron benchmarks cerrados y habilitaron productos basados en imágenes, documentos y video.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 25; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 25.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 4. La taxonomía de problemas

<!-- template: concept-breakdown -->
<!-- format: editorial -->

### Content

Representación

Aprender estructuras internas que capturan relaciones entre datos.

Embeddings de texto

Palabras, fragmentos de código, documentos y tickets se convierten en vectores comparables.

Búsqueda semántica

Los equipos recuperan documentación y decisiones pasadas por significado, no solo por coincidencia exacta de palabras.

Recomendación

Un sistema propone librerías, componentes, ejemplos, expertos o documentación relevante.

Detección de anomalías

El modelo señala patrones alejados del comportamiento habitual.

Herramientas: Scikit-learn · Sentence Transformers · FAISS · Pinecone · Qdrant.

Hito de referencia: los embeddings permiten relacionar texto, código y documentación en un espacio común.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 26; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 26.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 5. La taxonomía de problemas

<!-- template: concept-breakdown -->
<!-- format: editorial -->

### Content

Decisión secuencial

Maximizar una recompensa acumulada a través de acciones en el tiempo.

Formalizado como Reinforcement Learning: un agente interactúa con un entorno, toma acciones, observa resultados y ajusta su política.

Juegos

Ajedrez · Atari · StarCraft · Go.

Robótica

Control de brazos · navegación · manipulación.

Optimización de redes

Asignación de recursos · balanceo de carga · ajuste de capacidad.

Trading algorítmico

Decisiones bajo incertidumbre y restricciones.

RLHF

Alineación de modelos mediante preferencias humanas.

Herramientas: OpenAI Gym · Stable Baselines3 · Ray RLlib · MuJoCo · RLHF tooling.

Riesgo central: una recompensa mal definida puede inducir comportamientos útiles para la métrica y dañinos para el objetivo real.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 27; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 27.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 6. La taxonomía de problemas

<!-- template: concept-breakdown -->
<!-- format: editorial -->

### Content

Búsqueda y planificación

Encontrar la mejor secuencia de acciones en un espacio de estados.

Logística

Rutas óptimas, planificación de capacidad y preparación de despliegues.

Manufactura y operación

Secuenciación de tareas, asignación de recursos y mantenimiento.

Planificación de software

Resolución de dependencias · orden de pruebas · orquestación de runbooks · asignación de recursos en la nube.

Robótica y juegos de estrategia

Trayectorias, espacios físicos y decisiones de varios pasos.

Herramientas: Google OR-Tools · A* · Dijkstra · PDDL · Fast Downward · OptaPlanner.

Diferencia clave: el razonamiento genera alternativas; la planificación verifica precondiciones y organiza acciones factibles.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 28; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 28.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 7. La taxonomía de problemas

<!-- template: concept-breakdown -->
<!-- format: editorial -->

### Content

Razonamiento y simbólico

Manipular símbolos y reglas explícitas para derivar conclusiones lógicas.

Sistemas expertos

Políticas, reglas de negocio y validaciones trazables.

Validación formal

Verificación de configuraciones, propiedades de código y restricciones de seguridad.

Reglas de negocio

Decisiones de crédito, seguros, facturación y cumplimiento.

Diagnóstico basado en reglas técnicas

Árboles de decisión, runbooks y clasificación de incidentes mediante condiciones verificables.

Demostración formal

Propiedades de código, contratos y restricciones de arquitectura.

Herramientas: Prolog · Datalog · OWL · RDF/SPARQL · Graph Rules · Knowledge Graphs.

Hito de referencia: los LLMs pueden proponer pasos de razonamiento; un sistema simbólico permite verificarlos cuando el caso exige trazabilidad.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 29; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 29.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 8. La taxonomía de problemas

<!-- template: concept-breakdown -->

### Content

Generación

Modelar la distribución de los datos y producir nuevas muestras coherentes.

Texto

Respuestas · resúmenes · traducción · documentación · pruebas.

Imágenes

Diseño de interfaz · prototipos · íconos · síntesis visual.

Audio y música

Voz · síntesis · composición · edición.

Video

Animación · escenas · demostraciones de producto.

Moléculas y ciencia aplicada

Diseño de componentes, estructuras y simulaciones; el ejemplo se preserva como antecedente de la presentación original.

Herramientas: GPT-4 · Claude · Gemini · Stable Diffusion · VAE · GAN · modelos de difusión.

Hito de referencia: ChatGPT mostró cómo un producto generativo puede alcanzar adopción masiva y transformar expectativas de interacción.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 30; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 30.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

# 6. Modelos Fundacionales

**Goal of this section:** Explicar qué son los modelos fundacionales y por qué cambiaron la forma de construir productos de IA.

**Presenter feedback:**

---

## 1. Conceptos clave

<!-- template: concept-columns -->

### Content

LLMs, Foundation Models y Multimodal

Language Models

Un modelo que asigna probabilidades a secuencias de palabras. Dado un contexto, predice cuál es la siguiente palabra más probable.

Características:

Existen desde los años 1950
Basados en la idea: P(palabra | contexto)
Primero estadísticos (n-gramas), luego neuronales

Ejemplos: N-gramas · Shannon (1948) · Modelos de Markov · RNNs

Foundation Model

Un modelo entrenado a escala masiva sobre datos generales, que puede adaptarse a múltiples tareas con poco o ningún reentrenamiento (fine-tuning o prompting).

Características:

Entrenado con billones de tokens
Generalista por naturaleza
Base para construir aplicaciones específicas

Ejemplos: GPT-4, Gemini, Claude, LLaMA, DALL·E, Stable Diffusion

LLM (Large Language Model)

Un Foundation Model especializado en texto. Aprende la distribución del lenguaje natural y puede generar, resumir, traducir, razonar y escribir código.

Características:

Solo procesa y genera texto (tokens)
Arquitectura Transformer con atención
Escala: desde 7B hasta +1T parámetros

Ejemplos: GPT-4, Claude 3, Gemini Pro, LLaMA 3, Mistral

Modelo Multimodal

Un Foundation Model que procesa y genera múltiples tipos de datos simultáneamente: texto, imágenes, audio, video y código en un mismo modelo unificado.

Características:

Combina encoders de distintas modalidades
Un solo modelo para ver, escuchar y hablar
Permite razonamiento cruzado entre modalidades

Ejemplos: GPT-4o, Gemini 1.5 Pro, Claude 3.5, LLaVA

🔑 Relación: Todo LLM es un Foundation Model, pero no todo Foundation Model es un LLM. Todo modelo Multimodal es un Foundation Model, pero va un paso más allá al integrar múltiples modalidades.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 31; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 31.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 2. Concepto clave

<!-- template: concept-columns -->

### Content

Por que Foundation models es relevante ?

IA Tradicional vs. Foundation Models

IA Tradicional (Machine Learning/InHouse)

Un modelo por tarea específica
Requiere datos etiquetados abundantes para cada caso de uso
Difícil de reutilizar entre dominios distintos
Ejemplo: un detector de fallos en autopartes en Pilar solo detecta eso

Foundation Models

Modelos gigantescos entrenados con datos a gran escala que adquieren una comprensión general del mundo y se adaptan a múltiples tareas: traducir texto, escribir código, analizar contratos legales o generar imágenes.
Se exponen como SaaS o se pueden correr localmente. No es necesario tener un data science en tu empresa para empezar a hacer uso de los mismos.

Lectura recomendada: On the Opportunities and Risks of Foundation Models (Stanford HAI, arXiv:2108.07258)

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 32; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 32.

Diapositiva 5: El Salto Cuantitativo: IA Tradicional vs. Foundation Models



Discurso Sugerido: "Hasta hace pocos años, la IA era 'artesanal'. Si una empresa en el Parque Industrial de Pilar quería un modelo para detectar fallas en autopartes, entrenaba una IA solo para eso. Hoy entramos en la era de los Foundation Models (Modelos Fundacionales). Son modelos gigantescos, entrenados con datos a gran escala, que no saben hacer una sola cosa, sino que tienen una comprensión general del mundo y pueden adaptarse a múltiples tareas: desde traducir texto hasta escribir código o analizar un contrato legal."

Contexto Técnico Profundo: El término fue acuñado por el Stanford Institute for Human-Centered AI (HAI) en 2021 para describir modelos entrenados con datos amplios a gran escala que pueden adaptarse (fine-tuning o in-context learning) a una amplia gama de tareas downstream.

Enlace Recomendado: On the Opportunities and Risks of Foundation Models (Stanford HAI, arXiv:2108.07258)

### Presenter feedback

---

# 7. Datos

**Goal of this section:** Entender cómo aprenden los modelos, con qué datos se entrenan y qué implica operar a escala.

**Presenter feedback:**

---

## 3. Paradigmas de Aprendizaje

<!-- template: concept-breakdown -->

### Content

¿Cómo aprenden las máquinas?

Supervisado

Definición: requiere pares (X, Y) etiquetados por personas.
Dataset: limpio, balanceado y representativo. Cuanto más grande y diverso, mejor generaliza.
Ejemplos: ticket → prioridad · transacción → fraude/normal.
Casos: clasificación de incidencias asistida · detección de fraude bancario.

No supervisado

Definición: solo entradas X, sin etiquetas. El modelo descubre estructura latente.
Dataset: no requiere anotación, pero sí limpieza y normalización. Es sensible a outliers y ruido.
Ejemplos: agrupar clientes por comportamiento · detectar anomalías sin etiquetas.
Casos: segmentación en retail · análisis exploratorio de riesgo financiero.

Self-supervised

Definición: el propio dato genera las etiquetas, por ejemplo al predecir la próxima palabra. Permite usar grandes volúmenes sin anotación humana y sostiene el preentrenamiento de LLMs.
Dataset: masivo, diverso y con curación selectiva.
Ejemplos: predecir la próxima palabra · embeddings de código e imágenes.
Casos: entrenamiento de LLMs · búsqueda semántica corporativa.

Semi-supervisado

Definición: combina pocos datos etiquetados con muchos sin etiquetar. Resulta útil cuando etiquetar cuesta tiempo o requiere expertos.
Dataset: una fracción etiquetada y una mayoría sin etiquetar.
Ejemplos: 5% de tickets etiquetados + 95% sin etiqueta.
Casos: clasificación de documentos técnicos · sistemas con revisión humana.

Reinforcement Learning

Definición: no hay dataset fijo. El agente genera experiencias al interactuar con el entorno. La calidad del simulador y la función de recompensa resultan críticas.
Ejemplos: agente aprende Go · optimización dinámica de precios.
Casos: optimización de inventario · control autónomo en robótica industrial.

Active Learning

Definición: el modelo selecciona ejemplos inciertos o informativos para que una persona los etiquete.
Dataset: pequeño, pero seleccionado de forma estratégica.
Ejemplos: modelo elige qué cambios de código revisar · sistema pide resolver casos ambiguos.
Casos: revisión de seguridad asistida · clasificación legal con revisión mínima.

Regla general: supervisado maximiza precisión si existen datos etiquetados; self-supervised escala con datos crudos; RL aprende de interacción; active learning reduce el costo de etiquetado.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 33; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 33.

¿Por qué tantos datos?

Self-supervised learning no requiere etiquetas humanas:

el texto mismo genera sus propios objetivos (por ejemplo, predecir la próxima palabra), lo que permite entrenar con volúmenes masivos de datos crudos sin costo de etiquetado explícito.

 Evolución histórica de la escala

En 2018-2020, cientos de miles de millones de tokens eran “enorme”.

Para 2024-2025, los modelos de vanguardia usan decenas de trillones de tokens, con algunos conjuntos de datos incluso públicos superando 100 trillones de tokens.

 Implicaciones

Más datos → mejor comprensión y generalización del lenguaje.

Escala de datos y tamaño del modelo (parámetros) suelen crecer juntos.

Necesita infraestructura enorme (clusters de GPUs / TPUs).

### Presenter feedback

---

## 4. Es todo escala

<!-- template: timeline -->

### Content

La Escala es Masiva

Tokens de entrenamiento por modelo — 2020 a 2024

2020 — 300B tokens

GPT-3 · OpenAI · ≈45 TB de texto

2022 — 780B tokens

PaLM · Google · Tokens de alta calidad multilingüe

2022 — 1.4T tokens

Chinchilla · DeepMind · Demostró que más datos > más parámetros

2023 — 1.4T tokens

LLaMA · Meta · Primer modelo open-source competitivo

2023 — 2T tokens

LLaMA-2 · Meta · Versión mejorada con RLHF

2023 — 6T tokens

GPT-4 · OpenAI · ~6 trillion tokens (estimado)

2024 — 15T tokens

LLaMA-3 · Meta · Estado del arte open-source

💡 Self-supervised learning no requiere etiquetas humanas: el texto genera sus propios objetivos (predecir la próxima palabra), permitiendo entrenar con volúmenes masivos sin costo de etiquetado.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 34; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 34.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 5. ¿Con qué datos se entrenan?

<!-- template: concept-breakdown -->

### Content

¿Con qué datos se entrenan?

Fuentes de datos de los foundation models

Web pública

Common Crawl, C4 y OpenWebText: escala masiva y diversidad temática.

Libros digitalizados

BooksCorpus y Project Gutenberg: lenguaje estructurado y coherente.

Enciclopedias

Wikipedia: conocimiento factual organizado.

Código fuente

GitHub y The Stack: entrenamiento para generación y comprensión de código.

Artículos y papers

arXiv y conjuntos académicos: lenguaje técnico y especializado.

Foros y preguntas frecuentes

Stack Overflow, Reddit y comunidades: conversación natural y resolución de problemas.

Datos licenciados

Contratos con publishers y bases privadas: mayor control de calidad y de uso.

Datos humanos curados

Conjuntos internos de fine-tuning: alineación, seguridad y comportamiento.

Cada fuente introduce decisiones de calidad, licencias, privacidad y sesgo.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 35; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 35.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 6. Es todo escala

<!-- template: value-columns -->

### Content

La escala es masiva

Escala, datos y poder de cómputo

Dimensión | Valor aproximado | Contexto real

Parámetros | cientos de miles de millones | capacidad representacional de modelos frontier.

Tokens entrenados | decenas de trillones | web filtrada, libros, código y datos sintéticos.

GPUs utilizadas | miles o decenas de miles | clusters especializados que operan de forma continua.

Duración | meses | entrenamiento industrial con infraestructura dedicada.

GPU-horas totales | decenas de millones | consumo de cómputo acumulado.

Consumo eléctrico | decenas de GWh | costo ambiental y de infraestructura.

Costo total | decenas o cientos de millones de dólares | hardware, energía, ingeniería y datos.

La tabla conserva el orden de magnitud del PPTX original para explicar por qué muchos equipos consumen modelos existentes en vez de entrenarlos desde cero.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 36; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 36.

Diapositiva 6: La Anatomía de un Foundation Model (Escala y Datos)

Discurso Sugerido: "La magia de estos modelos no radica en un algoritmo místico, sino en la fuerza bruta y la escala. Estamos hablando de modelos entrenados con billones de palabras (prácticamente todo el internet público). Sus 'cerebros' tienen cientos o miles de millones de 'parámetros', que son las conexiones neuronales artificiales. Entrenar uno de estos modelos requiere miles de tarjetas gráficas (GPUs) funcionando durante meses y millones de dólares en electricidad."

Contexto Técnico Profundo: La relación entre el volumen de datos (tokens), el tamaño del modelo (parámetros) y el cómputo (FLOPs) se rige por las "Scaling Laws" (Leyes de Escalamiento). Modelos actuales como GPT-4 o Gemini manejan arquitecturas Mixture-of-Experts (MoE) con billones de parámetros dispersos.

Enlace Recomendado: Scaling Laws for Neural Language Models (OpenAI, arXiv:2001.08361)

### Presenter feedback

---

## Estimar lo que los laboratorios no publican

<!-- template: image-full -->

### Content

![Curva de calibración IKP: conocimiento factual y tamaño total estimado de modelos](images/ikp-calibration-curve.png)

### Sources

- corpus/arxiv-2604-24827-ikp.web.md
- [Incompressible Knowledge Probes: Estimating Black-Box LLM Parameter Counts via Factual Capacity](https://arxiv.org/abs/2604.24827)

### Speaker notes

La figura calibra puntajes de conocimiento factual contra el tamaño conocido de modelos abiertos. Las líneas punteadas de la derecha son estimaciones para modelos cerrados, no revelaciones de arquitectura por parte de los laboratorios. El paper presenta estas cifras como capacidad efectiva de orden de magnitud: su intervalo de predicción al 90% es aproximadamente un factor de 3 en cada dirección. La figura indica 89 modelos abiertos; la versión 2 del abstract reporta una calibración sobre 93.

### Presenter feedback

---

# 8. Ecosistema Actual

**Goal of this section:** Ubicar las familias y actores relevantes del ecosistema de modelos actual.

**Presenter feedback:**

---

## 7. El Ecosistema Actual

<!-- template: concept-breakdown -->
<!-- format: editorial -->

### Content

El ecosistema actual

Modelos de propósito general relevantes en agosto de 2026

OpenAI — GPT-5.2

Razonamiento, herramientas y desarrollo de software.

Google DeepMind — Gemini 3.6 Flash

Modelo multimodal rápido para tareas agentic y de código.

Anthropic — Claude 4

Familia Opus y Sonnet para razonamiento, análisis y programación.

Meta — Llama 4 Maverick y Scout

Pesos abiertos y multimodalidad para despliegue propio.

DeepSeek — V4 Pro y V4 Flash

Razonamiento y agentes con fuerte relación costo-rendimiento.

Moonshot AI — Kimi K3

Código, análisis y automatización agentic.

Alibaba — Qwen3.7-Max

Modelo orientado a coding, razonamiento y agentes de larga duración.

El mercado combina modelos cerrados por API, familias abiertas y modelos diseñados específicamente para agentes. La disponibilidad y las versiones cambian con rapidez.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 37; referencia de estructura)
- [OpenAI Models](https://platform.openai.com/docs/api-reference/models/object)
- [Google Gemini API Models](https://ai.google.dev/gemini-api/docs/models)
- [Anthropic Claude](https://docs.anthropic.com/en/docs/welcome)
- [Meta Llama 4](https://about.fb.com/ltam/news/2025/04/la-coleccion-de-modelos-llama-4-el-inicio-de-una-nueva-era-de-innovacion-multimodal-nativa-para-inteligencia-artificial/)
- [DeepSeek API — novedades](https://api-docs.deepseek.com/updates/)
- [Moonshot AI](https://www.moonshot.ai/)
- [Alibaba Qwen3.7-Max](https://www.alibabagroup.com/en-US/document-1994119844504535040)

### Speaker notes

Actualizado el 4 de agosto de 2026. Esta slide ofrece un mapa de familias y modelos representativos, no un ranking. Antes de adoptar un modelo, verificar versión, disponibilidad regional, licencia, precio, límites de uso y políticas de datos.

### Presenter feedback

---

# 9. Cierre y anexo

**Goal of this section:** Cerrar los conceptos centrales y preservar el material complementario en su orden original.

**Presenter feedback:**

---

## 1. Conclusiones Clave

<!-- template: concept-breakdown -->

### Content

Conclusiones clave

Lo que debes llevarte de esta sesión

1

La IA aprende de datos, objetivos y retroalimentación; no funciona como un conjunto fijo de reglas escritas a mano.

2

Los foundation models cambiaron las reglas del juego: un modelo entrenado a escala puede adaptarse a texto, código, imágenes y tareas de producto.

3

La escala importa, pero también la alineación, la seguridad, la evaluación y el control sobre los datos.

4

Los agentes y la multimodalidad amplían las capacidades de los sistemas. Los equipos deben diseñar permisos, trazabilidad y mecanismos de supervisión.

Preguntas: este es el momento para conectar los conceptos con problemas concretos de Ingeniería de Software.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 38; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 38.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 2. Anexo

<!-- template: divider -->

### Content

[Sin contenido visible en el PPTX de referencia.]

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 39; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 39.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 3. Modelos Discriminativos vs Generativos

<!-- template: concept-columns -->

### Content

La distinción entre modelos discriminativos y generativos ayuda a elegir el enfoque técnico adecuado. Los modelos discriminativos dibujan fronteras de decisión para clasificar datos existentes. Los generativos aprenden una distribución y producen nuevas instancias.

Atributo

Discriminativo

Generativo

¿Qué aprenden?

p(y|x): la probabilidad de una etiqueta dado un input.

p(x) o p(x,y): la distribución completa de los datos.

¿Qué responden?

“¿A qué clase pertenece este dato?”

“¿Cómo se vería una instancia compatible con esta distribución?”

Ejemplos

Clasificación de tickets · detección de fraude · priorización de alertas.

Generación de código de prueba · documentación · GPT-4 · Stable Diffusion.

Conexión moderna: los LLMs son generativos, pero pueden asistir en tareas discriminativas mediante prompting, herramientas y validación externa.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 40; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 40.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 4. El Desafío del Mundo Real

<!-- template: concept-columns -->

### Content

De la teoría a la práctica

Entorno Ideal (Laboratorio)

Totalmente observable, determinista, episódico, estático, discreto, conocido y de agente único.

Ejemplo: Resolver un Sudoku o jugar al Tres en Raya (Tic-Tac-Toe).
Resultado: Problemas resueltos hace décadas con algoritmos simples.

Entorno Real (El campo de batalla)

Parcialmente observable, estocástico, secuencial, dinámico, continuo, multiagente y desconocido.

Ejemplo: Conducción autónoma en una ciudad con tráfico impredecible o robótica de rescate.
Resultado: Requiere agentes que aprenden, planifican con incertidumbre y optimizan utilidades.

¿Por qué ganarle al campeón mundial de ajedrez (1997) fue 'fácil' comparado con lograr que un coche se conduzca solo bajo la lluvia? El entorno lo explica todo.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 41; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 41.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 5. Tema crítico

<!-- template: content+cards+image -->
<!-- design: column-right -->

### Content

El futuro: agentes autónomos e IA multimodal

Agentes autónomos

Los LLMs evolucionan de herramientas de pregunta-respuesta a agentes capaces de planificar, usar APIs, navegar, consultar repositorios, ejecutar código y completar tareas de varios pasos.

Frameworks como LangGraph, AutoGen u OpenAI Agents permiten orquestar agentes que colaboran para investigar, operar un flujo de trabajo, asistir a soporte o coordinar herramientas de desarrollo.

IA multimodal

Los modelos procesan y generan texto, imágenes, audio, video y código dentro de una misma experiencia.

Modelos multimodales: texto + visión + audio en tiempo real.

Generación de video: prototipos, demostraciones y contenido audiovisual.

Implicaciones: análisis de interfaces, accesibilidad, educación inmersiva, soporte técnico y automatización de tareas con herramientas.

La autonomía requiere permisos acotados, auditoría de acciones, evaluación y capacidad de detener el sistema.

![Agente autónomo operando herramientas y flujos](images/agentes-autonomos.jpeg)

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 42; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 42.

Diapositiva 9: El Futuro: Agentes Autónomos e IA Multimodal (Tema Crítico Sugerido 2)

Discurso Sugerido: "¿Hacia dónde vamos? La IA ya no solo es un 'chatbot' al que le haces preguntas. Estamos entrando en la era de los Agentes Autónomos e IA Multimodal. Pronto veremos sistemas que no solo generan texto, sino que 'ven' tu pantalla, 'escuchan' tu voz y ejecutan tareas complejas de forma independiente, como gestionar toda la logística de una exportación para una PyME en Pilar interactuando con otros softwares, sin intervención humana constante."

Contexto Técnico Profundo: La multimodalidad nativa permite procesar diferentes tensores de entrada (audio, visión, texto) en un mismo espacio latente. La "Agentic AI" implica el uso de LLMs como motores de razonamiento que utilizan herramientas externas (Tool Calling/Function Calling) y memoria a largo plazo.

Enlace Recomendado: Gartner: Top Strategic Technology Trends (Agentic AI)

### Presenter feedback

---

## 6. Tipos de Agentes en IA

<!-- template: value-columns -->

### Content

De la reacción simple al aprendizaje autónomo

Tipo de Agente

Base de Decisión

Capacidad Clave

Limitación Principal

Reactivo Simple

Percepción actual (Condición ➔ Acción)

Rápido y directo

Sin memoria; falla si no puede ver todo el entorno en el momento.

Basado en Modelos

Percepción + Estado Interno (Memoria)

Entiende el contexto continuo y recuerda lo que ya no ve

No planifica hacia el futuro; solo reacciona a la situación actual.

Basado en Objetivos

Estado Interno + Metas a futuro

Planifica secuencias de acciones para lograr un resultado

No distingue si un camino es eficiente o costoso, solo si llega a la meta.

Basado en Utilidad

Metas + Función de "Felicidad/Eficiencia"

Optimiza; evalúa y elige la mejor opción posible

No sabe adaptarse de forma autónoma a entornos o reglas totalmente nuevas.

Que Aprende

Utilidad + Evaluación (Crítico) y Exploración

Evoluciona, corrige errores pasados y se adapta a lo desconocido

Mayor complejidad de diseño y requiere procesamiento de entrenamiento.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 43; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 43.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

---

## 7. Dimensiones del Entorno

<!-- template: value-columns -->

### Content

Simple (Laboratorio) vs. Complejo (Mundo Real)

Dimensión

Entorno Simple (Laboratorio)

Entorno Complejo (Mundo Real)

Implicancia para la IA

Observabilidad

Totalmente Observable: Sensores captan todo.
(Ej: Ajedrez, ves todo el tablero)

Parcialmente Observable: Información oculta.
(Ej: Póker, cartas ocultas; conducir con niebla)

Debe decidir asumiendo la información que le falta.

Certeza

Determinista: Resultado exacto garantizado.
(Ej: Cubo Rubik, las piezas van donde las movés)

Estocástico: Azar o probabilidad.
(Ej: Frenar sobre asfalto mojado)

Requiere manejar el riesgo y la incertidumbre.

Impacto Temporal

Episódico: Decisiones aisladas.
(Ej: IA que clasifica fotos de gatos)

Secuencial: Acciones afectan el futuro.
(Ej: Inversiones financieras a largo plazo)

Obliga a planificar a futuro y prever consecuencias.

Estabilidad

Estático: El entorno espera.
(Ej: Resolver un Sudoku en papel)

Dinámico: Cambia mientras "piensa".
(Ej: Conducir en el tráfico del centro)

La velocidad de procesamiento es cuestión de supervivencia.

Valores

Discreto: Estados y opciones finitas.
(Ej: Casillas y turnos de las Damas)

Continuo: Variables fluidas e infinitas.
(Ej: Ángulos, viento y fuerza al volar un dron)

Aumenta drásticamente la cantidad de cálculos.

Participantes

Agente Único: Opera solo.
(Ej: IA resolviendo un laberinto)

Multiagente: Otros actores interactúan.
(Ej: Robots jugando fútbol, vehículos cooperando)

Debe predecir el comportamiento ajeno.

Reglas

Conocido: Sabe cómo funciona todo.
(Ej: Solitario, las reglas vienen programadas)

Desconocido: Ignora las reglas.
(Ej: Robot explorando terreno en Marte)

Exige explorar y aprender mediante ensayo y error.

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 44; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 44.

Para darle dinamismo a tu clase, podés usar esta tabla para mostrar que el gran salto de la IA en los últimos años fue salir de la columna del "Entorno Simple" (donde triunfaba en los años 90) para empezar a dominar la columna del "Entorno Complejo".

Con las bases de "Qué es un agente" y "Dónde opera" ya resueltas de forma muy visual, el siguiente bloque lógico en el enfoque de Russell y Norvig es cómo la IA toma acción.

### Presenter feedback

---

## 8. Diapositiva de reserva

<!-- template: divider -->

### Content

[Sin contenido visible en el PPTX de referencia.]

### Sources

- corpus/Clase-1-AI-for-BIO-Fundamento.pptx.md (diapositiva 45; adaptación íntegra)

### Speaker notes

Referencia PPTX: diapositiva 45.

[Sin notas en el PPTX de referencia.]

### Presenter feedback

# Conclusions

La diapositiva de conclusiones se conserva como 5.1 porque el PPTX original continúa con un anexo técnico.

# Open questions

- El contenido completo se conserva por instrucción del presentador, aunque algunas diapositivas excedan la densidad habitual para una proyección en vivo.
- Confirmar días, horarios, aula, plataforma de entregas y ponderación final de la cursada.
- Decidir qué diapositivas del anexo se mostrarán dentro de los 90 minutos y cuáles quedarán como material de consulta.
- Validar qué recursos visuales del PPTX original se reutilizarán en la versión de Ingeniería de Software.

# Cut material

Ninguno. El contenido del PPTX de referencia permanece preservado en el corpus y en este borrador 1:1.
