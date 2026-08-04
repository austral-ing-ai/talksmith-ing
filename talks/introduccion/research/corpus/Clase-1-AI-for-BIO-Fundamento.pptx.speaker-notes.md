---
source: ../articles/Clase-1-AI-for-BIO-Fundamento.pptx
extracted: 2026-08-03
slides: 45
nonempty_notes: 16
---

# Notas del orador del PPTX

Extracción literal de las notas no vacías del archivo fuente. Se conserva la numeración original de las diapositivas.

## Diapositiva 1

Discurso Sugerido: "Bienvenidos. Hoy vamos a desmitificar la Inteligencia Artificial. Intuitivamente, solemos pensar en la IA como 'máquinas haciendo cosas que requerirían inteligencia si las hiciera un humano'. Pero si queremos ser rigurosos, como proponen Russell y Norvig, la IA es el diseño de agentes racionales: sistemas que perciben su entorno y toman acciones para maximizar sus posibilidades de éxito en un objetivo dado. No se trata de crear humanos sintéticos, sino de resolver problemas complejos con matemáticas a gran escala."

Contexto Técnico Profundo: La definición de agente racional evita el debate filosófico sobre la "conciencia" y se centra en la función matemática que mapea secuencias de percepciones a acciones (arquitectura de agentes).

Enlace Recomendado: Sitio oficial del libro "Artificial Intelligence: A Modern Approach" (Russell & Norvig)

## Diapositiva 2

Primera vez que dictamos esta materia (contar brevemente la historia de la materia).

## Diapositiva 8

Aquí tienes una oportunidad de oro para lucirte mencionando a AlphaFold (de Google DeepMind). Antes, descubrir cómo se plegaba una proteína en 3D tomaba años de ensayos en laboratorio y millones de dólares; la IA resolvió este problema biológico en minutos, cambiando la ciencia para siempre. Por otro lado, es fundamental que le hables a la clase sobre los riesgos: la IA a veces 'alucina' (inventa información confiable). Por eso, en medicina se utiliza el concepto de 'Human-in-the-loop' (el humano en el circuito). La frase de cabecera que puedes usar con tus alumnos es: 'La inteligencia artificial no reemplazará a los médicos, pero los médicos que usan inteligencia artificial reemplazarán a los que no lo hacen'.







Our analysis finds that generative AI could have a significant impact on the pharmaceutical and medical-product industries—from 2.6 to 4.5 percent of annual revenues across the pharmaceutical and medical-product industries, or $60 billion to $110 billion annually. This big potential reflects the resource-intensive process of discovering new drug compounds. Pharma companies typically spend approximately 20 percent of revenues on R&D,1 and the development of a new drug takes an average of ten to 15 years. With this level of spending and timeline, improving the speed and quality of R&D can generate substantial value. For example, lead identification—a step in the drug discovery process in which researchers identify a molecule that would best address the target for a potential new drug—can take several months even with “traditional” deep learning techniques. Foundation models and generative AI can enable organizations to complete this step in a matter of weeks.

Generative AI at work in pharmaceuticals and medical products

Drug discovery involves narrowing the universe of possible compounds to those that could effectively treat specific conditions. Generative AI’s ability to process massive amounts of data and model options can accelerate output across several use cases:

Improve automation of preliminary screening

In the lead identification stage of drug development, scientists can use foundation models to automate the preliminary screening of chemicals in the search for those that will produce specific effects on drug targets. To start, thousands of cell cultures are tested and paired with images of the corresponding experiment. Using an off-the-shelf foundation model, researchers can cluster similar images more precisely than they can with traditional models, enabling them to select the most promising chemicals for further analysis during lead optimization.

Enhance indication finding

An important phase of drug discovery involves the identification and prioritization of new indications—that is, diseases, symptoms, or circumstances that justify the use of a specific medication or other treatment, such as a test, procedure, or surgery. Possible indications for a given drug are based on a patient group’s clinical history and medical records, and they are then prioritized based on their similarities to established and evidence-backed indications.

Researchers start by mapping the patient cohort’s clinical events and medical histories—including potential diagnoses, prescribed medications, and performed procedures—from real-world data. Using foundation models, researchers can quantify clinical events, establish relationships, and measure the similarity between the patient cohort and evidence-backed indications. The result is a short list of indications that have a better probability of success in clinical trials because they can be more accurately matched to appropriate patient groups.

Pharma companies that have used this approach have reported high success rates in clinical trials for the top five indications recommended by a foundation model for a tested drug. This success has allowed these drugs to progress smoothly into Phase 3 trials, significantly accelerating the drug development process.

Factors for pharmaceuticals and medical products organizations to consider

Before integrating generative AI into operations, pharma executives should be aware of some factors that could limit their ability to capture its benefits:

The need for a human in the loop. Companies may need to implement new quality checks on processes that shift from humans to generative AI, such as representative-generated emails, or more detailed quality checks on AI-assisted processes, such as drug discovery. The increasing need to verify whether generated content is based on fact or inference elevates the need for a new level of quality control.

Explainability. A lack of transparency into the origins of generated content and traceability of root data could make it difficult to update models and scan them for potential risks; for instance, a generative AI solution for synthesizing scientific literature may not be able to point to the specific articles or quotes that led it to infer that a new treatment is very popular among physicians. The technology can also “hallucinate,” or generate responses that are obviously incorrect or inappropriate for the context. Systems need to be designed to point to specific articles or data sources, and then do human-in-the-loop checking.

Privacy considerations. Generative AI’s use of clinical images and medical records could increase the risk that protected health information will leak, potentially violating regulations that require pharma companies to protect patient privacy.

“will be more

important to doctors than the stethoscope in the past” (20). Several LMMs have passed the

US medical licensing examination; however, passing a written medical test by regurgitating

medical knowledge is not the same as providing safe, effective clinical services (21), and LMMs

have failed tests with material not previously published online or that could be easily solved

by children (22). One study of the clinical knowledge of a large language model concluded that

“transitioning from a large language model that is used for answering medical questions to

a tool that can be used by healthcare providers, administrators, and consumers will require

considerable additional research to ensure the safety, reliability, efficacy and privacy of the

technology”



-

Inaccurate, incomplete, biased or false responses: One concern with respect to LMMs

. LMMs trained on health

data often encode such biases, as most data are collected in high-income settings.

For example, genetic data tend to be collected disproportionately on people of

European descent (1). LMMs are also often trained on electronic health records, which

are full of errors and inaccurate information (24) or rely on information obtained

from physical examinations that may be inaccurate, thus affecting the output of an

LMM (25).

## Diapositiva 9

CÓMO PRESENTAR ESTE SLIDE

Apertura: "Vimos todo lo que la IA puede hacer en medicina. Ahora veamos el otro lado — lo que la OMS identifica como los problemas actuales."



---



1. ALUCINACIONES Y RESPUESTAS FALSAS

Explicación: Los LMMs no generan hechos, generan texto que estadísticamente "parece" un hecho. No tienen noción de verdad ni de mentira — simplemente predicen la siguiente palabra más probable.

Ejemplo (OMS): Un estudio citado por la OMS encontró que al pedirle a un LMM resumir hechos médicos simples, alucinó al menos el 3% del tiempo y hasta el 27% en casos complejos. Otro caso real: abogados en EE.UU. presentaron ante un tribunal citas de jurisprudencia inventadas por ChatGPT — el juez los sancionó. En medicina, el riesgo es aún mayor: una referencia bibliográfica inventada puede llevar a un tratamiento incorrecto.

Pregunta para la clase: "¿Confiarían en un médico que se equivoca 1 de cada 4 veces?"



---



2. SESGOS EN LOS DATOS

Explicación: Los modelos aprenden de los datos con los que fueron entrenados. Si esos datos son sesgados, las respuestas también lo serán — y el modelo no lo sabe ni lo advierte.

Ejemplo (OMS): Los datos genéticos usados para entrenar modelos provienen desproporcionadamente de personas de ascendencia europea. Si un médico en Argentina o Nigeria consulta a una IA sobre riesgo genético de su paciente, la respuesta puede ser incorrecta para esa población. Además, los historiales clínicos electrónicos están llenos de errores de transcripción y sesgos de género — las mujeres históricamente han sido subdiagnosticadas en enfermedades cardíacas, y esos sesgos se replican en la IA.



---



3. PRIVACIDAD Y PROTECCIÓN DE DATOS

Explicación: Cuando un médico escribe un caso clínico en ChatGPT para pedir consejo, esos datos pueden ser retenidos por la empresa, usados para reentrenar el modelo, o expuestos a terceros.

Ejemplo (OMS): Varios LMMs están bajo investigación en Europa por violar el GDPR. Italia bloqueó temporalmente ChatGPT en 2023. En EE.UU., médicos que ingresan datos de pacientes en chatbots pueden estar violando la ley HIPAA sin saberlo. Samsung tuvo un incidente donde empleados filtraron código propietario al usar ChatGPT — en salud, el equivalente sería filtrar datos de pacientes oncológicos o psiquiátricos.

Punto clave: "La IA no tiene secreto profesional."



---



4. SESGO DE AUTOMATIZACIÓN

Explicación: Es la tendencia humana a confiar excesivamente en sistemas automatizados, incluso cuando están equivocados. Cuanto más "inteligente" parece el sistema, más difícil es cuestionarlo.

Ejemplo (OMS): La OMS advierte que los médicos que usan IA para diagnóstico pueden dejar de ejercer su juicio crítico. Un experimento mostró que ChatGPT puede influir en el juicio moral de las personas incluso cuando saben que hablan con una IA. En radiología: si un algoritmo dice "normal" y el médico confía sin revisar, una lesión pequeña puede pasar desapercebida. La OMS también señala que los LMMs pueden ser "muy inconsistentes como asesores morales", lo que es especialmente peligroso en decisiones clínicas difíciles.

Concepto clave: "Human-in-the-loop" — el humano siempre debe estar en el circuito de decisión.



---



5. ACCESO DESIGUAL

Explicación: La IA más poderosa está detrás de muros de pago y requiere infraestructura digital que no existe en muchos países, profundizando la brecha en salud global.

Ejemplo (OMS): ChatGPT cuesta aproximadamente USD 700.000 por día para operar. La OMS proyecta un déficit de 10 millones de trabajadores de salud para 2030, principalmente en países de bajos ingresos — donde la IA podría ser una solución, pero si no es accesible, el problema se agrava. Además, la mayoría de los LMMs funcionan principalmente en inglés, generando respuestas menos precisas en otros idiomas. Paradoja: los pobres podrían quedar limitados a usar IA gratuita de menor calidad, mientras los ricos acceden a atención médica real.

Reflexión: "¿La IA democratiza la salud o la privatiza aún más?"



---



6. IMPACTO AMBIENTAL

Explicación: Entrenar y operar modelos de IA a gran escala consume cantidades masivas de energía y agua — recursos escasos en muchas regiones.

Ejemplo (OMS): Entrenar un LMM de gran escala consumió 700.000 litros de agua fresca. Una conversación de 20-50 preguntas consume el equivalente a una botella de 500ml de agua. Un centro de datos de una gran empresa tecnológica usó más del 25% del agua de una ciudad entera en Oregon, EE.UU. Otro caso: una empresa planificó construir un data center en un país en sequía severa donde los residentes ya bebían agua salada. La OMS señala que el cambio climático causará ~250.000 muertes adicionales por año entre 2030-2050 — y la IA contribuye a ese problema.

Conexión: "Cuando usamos IA para descubrir fármacos, también estamos tomando una decisión ambiental."



---



7. DEGRADACIÓN DE HABILIDADES CLÍNICAS

Explicación (OMS, sección 2.1): Existe un riesgo a largo plazo de que el uso creciente de IA en la práctica médica degrade o erosione la competencia de los clínicos como profesionales, a medida que transfieren responsabilidades rutinarias a las computadoras.

Ejemplo concreto: Si un médico lleva años confiando en que la IA lee sus radiografías, ¿qué pasa cuando el sistema falla por un ciberataque o corte de red? La OMS advierte que la pérdida de habilidades podría resultar en que los médicos sean incapaces de contradecir o cuestionar con confianza la decisión de un algoritmo. Analogía: los pilotos de avión que dependen demasiado del piloto automático pierden habilidades de vuelo manual — con consecuencias potencialmente fatales en emergencias. En medicina, el equivalente podría ser un médico que ya no sabe interpretar una radiografía sin asistencia de IA.

Punto clave: La IA debe usarse para amplificar las habilidades del médico, no para reemplazarlas. La formación médica debe adaptarse para mantener las competencias clínicas fundamentales.



---



 CIERRE PARA DEBATE:

"¿Cómo equilibramos la velocidad de adopción de la IA con la necesidad de regulación y seguridad? ¿Quién debería ser responsable cuando la IA se equivoca en un diagnóstico — el médico, la empresa que desarrolló el modelo, o el hospital que lo implementó?"

## Diapositiva 10

. Technology improved slowly enough that humans could adapt. Intelligence, the ability to analyze, decide, create, persuade, and coordinate, was the thing that could not be replicated at scale.

Human intelligence derived its inherent premium from its scarcity. Every institution in our economy, from the labor market to the mortgage market to the tax code, was designed for a world in which that assumption held.

We are now experiencing the unwind of that premium. Machine intelligence is now a competent and rapidly improving substitute for human intelligence across a growing range of tasks

## Diapositiva 18

Discurso Sugerido: "Bienvenidos. Hoy vamos a desmitificar la Inteligencia Artificial. Intuitivamente, solemos pensar en la IA como 'máquinas haciendo cosas que requerirían inteligencia si las hiciera un humano'. Pero si queremos ser rigurosos, como proponen Russell y Norvig, la IA es el diseño de agentes racionales: sistemas que perciben su entorno y toman acciones para maximizar sus posibilidades de éxito en un objetivo dado. No se trata de crear humanos sintéticos, sino de resolver problemas complejos con matemáticas a gran escala."

Contexto Técnico Profundo: La definición de agente racional evita el debate filosófico sobre la "conciencia" y se centra en la función matemática que mapea secuencias de percepciones a acciones (arquitectura de agentes).

Enlace Recomendado: Sitio oficial del libro "Artificial Intelligence: A Modern Approach" (Russell & Norvig)

## Diapositiva 19

Diapositiva 1: ¿Qué es la Inteligencia Artificial? (De la teoría a la intuición)

Discurso Sugerido: "Bienvenidos. Hoy vamos a desmitificar la Inteligencia Artificial. Intuitivamente, solemos pensar en la IA como 'máquinas haciendo cosas que requerirían inteligencia si las hiciera un humano'. Pero si queremos ser rigurosos, como proponen Russell y Norvig, la IA es el diseño de agentes racionales: sistemas que perciben su entorno y toman acciones para maximizar sus posibilidades de éxito en un objetivo dado. No se trata de crear humanos sintéticos, sino de resolver problemas complejos con matemáticas a gran escala."

Contexto Técnico Profundo: La definición de agente racional evita el debate filosófico sobre la "conciencia" y se centra en la función matemática que mapea secuencias de percepciones a acciones (arquitectura de agentes).

Enlace Recomendado: Sitio oficial del libro "Artificial Intelligence: A Modern Approach" (Russell & Norvig)

## Diapositiva 20

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

## Diapositiva 22

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

## Diapositiva 23

Diapositiva 3: La Taxonomía de Problemas: ¿Qué resolvemos?

Discurso Sugerido: "Para entender la IA, hay que verla como una caja de herramientas. ¿Qué problemas resuelve? Principalmente, podemos categorizarlos en siete áreas clave. Por ejemplo, en Predicción, la IA puede predecir categorías o valores continuos, como si una planta tiene una plaga o estimar el rendimiento de una cosecha. En Percepción, la IA extrae significado de imágenes o audio. La Generación nos permite crear nuevo contenido. Los sistemas de Decisión Secuencial aprenden a tomar series de acciones para lograr objetivos, como en los juegos. Y el Razonamiento Simbólico permite a la IA usar reglas lógicas."

Contexto Técnico Profundo: La Predicción mapea entradas $X$ a salidas $Y$ (discretas o continuas). La Percepción extrae características de datos crudos. La Representación busca estructuras subyacentes (embeddings). La Generación modela distribuciones de probabilidad. La Decisión Secuencial optimiza acciones a lo largo del tiempo (Reinforcement Learning). La Búsqueda y Planificación encuentran secuencias óptimas de acciones. El Razonamiento Simbólico se basa en sistemas expertos y lógica.

## Diapositiva 32

Diapositiva 5: El Salto Cuantitativo: IA Tradicional vs. Foundation Models



Discurso Sugerido: "Hasta hace pocos años, la IA era 'artesanal'. Si una empresa en el Parque Industrial de Pilar quería un modelo para detectar fallas en autopartes, entrenaba una IA solo para eso. Hoy entramos en la era de los Foundation Models (Modelos Fundacionales). Son modelos gigantescos, entrenados con datos a gran escala, que no saben hacer una sola cosa, sino que tienen una comprensión general del mundo y pueden adaptarse a múltiples tareas: desde traducir texto hasta escribir código o analizar un contrato legal."

Contexto Técnico Profundo: El término fue acuñado por el Stanford Institute for Human-Centered AI (HAI) en 2021 para describir modelos entrenados con datos amplios a gran escala que pueden adaptarse (fine-tuning o in-context learning) a una amplia gama de tareas downstream.

Enlace Recomendado: On the Opportunities and Risks of Foundation Models (Stanford HAI, arXiv:2108.07258)

## Diapositiva 33

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

## Diapositiva 36

Diapositiva 6: La Anatomía de un Foundation Model (Escala y Datos)

Discurso Sugerido: "La magia de estos modelos no radica en un algoritmo místico, sino en la fuerza bruta y la escala. Estamos hablando de modelos entrenados con billones de palabras (prácticamente todo el internet público). Sus 'cerebros' tienen cientos o miles de millones de 'parámetros', que son las conexiones neuronales artificiales. Entrenar uno de estos modelos requiere miles de tarjetas gráficas (GPUs) funcionando durante meses y millones de dólares en electricidad."

Contexto Técnico Profundo: La relación entre el volumen de datos (tokens), el tamaño del modelo (parámetros) y el cómputo (FLOPs) se rige por las "Scaling Laws" (Leyes de Escalamiento). Modelos actuales como GPT-4 o Gemini manejan arquitecturas Mixture-of-Experts (MoE) con billones de parámetros dispersos.

Enlace Recomendado: Scaling Laws for Neural Language Models (OpenAI, arXiv:2001.08361)

## Diapositiva 37

Diapositiva 7: El Ecosistema Actual: Actores y Competencia

Discurso Sugerido: "¿Quiénes están construyendo estos gigantes? El ecosistema está dominado por unos pocos actores con el capital para costear este nivel de cómputo. Por un lado, modelos cerrados y comerciales como los de OpenAI (ChatGPT), Google DeepMind (Gemini) y Anthropic (Claude). Por otro lado, un ecosistema de código abierto liderado por Meta (Llama) y Mistral, que permite a universidades y startups descargar los pesos de los modelos y ejecutarlos localmente, democratizando el acceso a la tecnología."

Contexto Técnico Profundo: La distinción entre pesos abiertos (open weights) y modelos propietarios es el debate central en la seguridad y monopolización de la IA. Modelos como Llama democratizan el fine-tuning local (ej. QLoRA) sin depender de APIs en la nube.

Enlace Recomendado: State of AI Report (Análisis anual de la industria)

## Diapositiva 42

Diapositiva 9: El Futuro: Agentes Autónomos e IA Multimodal (Tema Crítico Sugerido 2)

Discurso Sugerido: "¿Hacia dónde vamos? La IA ya no solo es un 'chatbot' al que le haces preguntas. Estamos entrando en la era de los Agentes Autónomos e IA Multimodal. Pronto veremos sistemas que no solo generan texto, sino que 'ven' tu pantalla, 'escuchan' tu voz y ejecutan tareas complejas de forma independiente, como gestionar toda la logística de una exportación para una PyME en Pilar interactuando con otros softwares, sin intervención humana constante."

Contexto Técnico Profundo: La multimodalidad nativa permite procesar diferentes tensores de entrada (audio, visión, texto) en un mismo espacio latente. La "Agentic AI" implica el uso de LLMs como motores de razonamiento que utilizan herramientas externas (Tool Calling/Function Calling) y memoria a largo plazo.

Enlace Recomendado: Gartner: Top Strategic Technology Trends (Agentic AI)

## Diapositiva 44

Para darle dinamismo a tu clase, podés usar esta tabla para mostrar que el gran salto de la IA en los últimos años fue salir de la columna del "Entorno Simple" (donde triunfaba en los años 90) para empezar a dominar la columna del "Entorno Complejo".

Con las bases de "Qué es un agente" y "Dónde opera" ya resueltas de forma muy visual, el siguiente bloque lógico en el enfoque de Russell y Norvig es cómo la IA toma acción.
