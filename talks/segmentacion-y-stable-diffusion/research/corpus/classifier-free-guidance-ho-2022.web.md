---
source_file: classifier-free-guidance-ho-2022
source_type: web-capture
ingested_at: 2026-08-14
---

# Classifier-Free Diffusion Guidance (arXiv:2207.12598) — página de abstract

## Provenance
- Original location: `research/web/classifier-free-guidance-ho-2022/`
- Format: web-capture (arXiv `abs` page; `page.md` + `original.html` + `assets/`)
- URL: https://arxiv.org/abs/2207.12598
- Author / source (if known): Jonathan Ho, Tim Salimans (Google Research, Brain Team)
- Date of original (if known): 26 jul 2022 (v1, única versión). Una versión corta apareció antes en el NeurIPS 2021 Workshop on Deep Generative Models and Downstream Applications.
- Fetched at: 2026-08-14T17:03:10Z (HTTP 200, 41.121 bytes)
- Rol en la Clase 9: el paper detrás del parámetro que todo el mundo toca sin saber qué es — la escala de guidance del prompt.

## Key claims

- **Autores:** Jonathan Ho, Tim Salimans. **Año:** 2022 (el workshop de la versión corta es de 2021). **Venue:** preprint arXiv; versión corta en el NeurIPS 2021 Workshop on Deep Generative Models and Downstream Applications. **arXiv ID:** arXiv:2207.12598 [cs.LG, cs.AI]. **DOI:** 10.48550/arXiv.2207.12598.
- **El punto de partida — classifier guidance:** un método para intercambiar **cobertura de modos por fidelidad de la muestra** en modelos de difusión condicionales, **después de entrenados**. El abstract lo emparenta explícitamente con el *low temperature sampling* y el *truncation* de otros modelos generativos.
- **Su problema:** classifier guidance combina el score del modelo de difusión con **el gradiente de un clasificador de imágenes**, lo que obliga a **entrenar un clasificador aparte** del modelo de difusión.
- **La pregunta del paper:** ¿se puede hacer guiado **sin clasificador**?
- **La respuesta:** sí. En *classifier-free guidance* se **entrenan conjuntamente un modelo de difusión condicional y uno incondicional**, y se **combinan los dos estimadores de score** —el condicional y el incondicional— para obtener un compromiso entre **calidad y diversidad** de las muestras similar al de classifier guidance.

## Definitions and terminology

- **Classifier-free guidance (CFG).** "We jointly train a conditional and an unconditional diffusion model, and we combine the resulting conditional and unconditional score estimates to attain a trade-off between sample quality and diversity." Es la definición completa del método en una oración, y está en el abstract. Lo que la clase enseña como "el modelo genera dos veces, con prompt y sin prompt, y exagera la diferencia" es exactamente esto, dicho en criollo.
- **Escala de guidance (w / guidance scale).** **Ausente del abstract.** El abstract habla de "a trade-off" pero **no introduce el parámetro que lo controla**, ni le pone nombre, ni le da rango, ni sugiere un valor. La fórmula de combinación lineal de los dos scores —donde la escala aparece como coeficiente— está en el cuerpo del paper, fuera de la captura. Esto es decisivo para verificar la cifra del deck.
- **Classifier guidance.** El método previo que CFG reemplaza: score del difusor + gradiente de un clasificador entrenado por separado.
- **Trade-off calidad ↔ diversidad** (o "mode coverage vs sample fidelity"). El eje conceptual del paper: subir el guiado da imágenes más nítidas y más pegadas al condicionamiento, a costa de menos variedad. Es la intuición que la clase necesita transmitir, y está bien respaldada por el abstract.
- **Analogías declaradas:** *low temperature sampling* y *truncation* — dos técnicas conocidas de otros modelos generativos que hacen el mismo compromiso. Útil como puente pedagógico, especialmente para un público que ya vio temperatura en LLMs.
- **Score estimate.** El objeto que se combina. El abstract lo usa sin definirlo — asume conocimiento de modelos de difusión basados en score.

## Evidence and examples

- **El abstract no contiene un solo número.** Ni FID, ni IS, ni valores de escala, ni tamaños de modelo, ni datasets. Es un abstract puramente conceptual, de dos oraciones de método.
- Única referencia externa: la versión corta en OpenReview (`https://openreview.net/pdf?id=qw8AKxfYbI`).

### Verificación de cifras del deck

- **"Guidance 7,5 por defecto" — NO CIERRA CONTRA ESTA FUENTE, y la atribución es engañosa.** La página capturada **no menciona ningún valor de escala de guidance**; de hecho no menciona ninguna cifra en absoluto. Más importante: **7,5 no es un valor de este paper**. Es el valor por defecto del pipeline de **Stable Diffusion** — el `guidance_scale=7.5` de `StableDiffusionPipeline` en la librería `diffusers` de Hugging Face, heredado por prácticamente todas las interfaces de usuario. Es una **convención de implementación**, no un resultado de investigación: no hay un experimento que establezca 7,5 como óptimo, y de hecho el valor apropiado depende del modelo, del sampler y de la cantidad de pasos.
  **Recomendación para el deck:** presentar 7,5 como "el valor por defecto de Stable Diffusion" y no como un parámetro del paper de CFG. La idea de fondo (subir la escala pega más la imagen al prompt y reduce diversidad; pasarse quema la imagen) sí es del paper y es lo que vale la pena enseñar. El respaldo documental para el 7,5 **no está en el corpus**: haría falta la documentación de `diffusers` o la tarjeta del modelo de Stable Diffusion.

## Inconsistencies / open questions

1. **La página capturada trae solo el abstract, y este abstract es especialmente magro.** Es el más corto del conjunto y el único sin ningún dato cuantitativo. Lo que la clase necesitaría y no está:
   - **La fórmula de guidance** — la combinación lineal de los scores condicional e incondicional, donde aparece el coeficiente que la clase llama "escala".
   - **El barrido de valores de la escala** con las imágenes resultantes: la grilla de "guidance bajo → borroso y diverso / guidance alto → nítido y saturado" es *la* figura que el deck querría mostrar.
   - El truco de entrenamiento: **descartar el condicionamiento con cierta probabilidad** durante el entrenamiento para que el mismo modelo aprenda las dos versiones (condicional e incondicional) sin entrenar dos redes. Este detalle —que es lo que hace práctico al método— **no está en el abstract**.
   - Las curvas **FID vs IS** que cuantifican el compromiso.
   Todo eso está en el PDF (`https://arxiv.org/pdf/2207.12598`), no capturado.
2. **El "7,5" del deck no pertenece a este paper.** Detalle arriba. Es la segunda cifra del deck (después del "~95%" de SAM) que se presenta con una atribución que la fuente no sostiene, aunque acá el problema es de procedencia y no de existencia: el número existe y es correcto como default de Stable Diffusion.
3. **El abstract asume mucho.** Habla de "score estimate", "mode coverage" y "diffusion models" sin definir nada. Es un paper escrito para especialistas; ninguna oración es citable tal cual frente a un público de biomedicina sin traducción previa.
4. **Fechas confusas.** El preprint de arXiv es de julio de 2022, pero la versión corta del workshop es de diciembre de 2021 — anterior al paper de difusión latente (dic 2021) y muy anterior a Stable Diffusion (ago 2022). Si el deck ordena cronológicamente los papers del bloque de generación, conviene decidir qué fecha usar y ser consistente.

## Images / diagrams

La captura de una página `abs` de arXiv **no incluye ninguna figura del paper** — no trae la grilla de barrido de la escala de guidance. Los tres archivos guardados son cromo del sitio, copiados a la carpeta compañera por completitud.

  - **Depiction:** logotipo institucional de arXiv en la barra superior del sitio (vectorial, tema claro).
  - **Why it matters:** nada. Cromo de navegación.
  - **Transcribed text:** "arXiv" (atributo `alt`: "archive").
  - **Depiction:** ícono de 16×16 px de BibSonomy — grafo de nodos gris con el nodo central en magenta.
  - **Why it matters:** nada. Botón de marcador.
  - **Transcribed text:** ninguno (atributo `alt`: "BibSonomy").
  - **Depiction:** ícono de 18×18 px de Reddit — mascota "Snoo" en gris con ojos rojos.
  - **Why it matters:** nada. Botón de compartir.
  - **Transcribed text:** ninguno (atributo `alt`: "Reddit").

## Raw / preserved excerpts

**Abstract completo, verbatim (inglés):**

> Classifier guidance is a recently introduced method to trade off mode coverage and sample fidelity in conditional diffusion models post training, in the same spirit as low temperature sampling or truncation in other types of generative models. Classifier guidance combines the score estimate of a diffusion model with the gradient of an image classifier and thereby requires training an image classifier separate from the diffusion model. It also raises the question of whether guidance can be performed without a classifier. We show that guidance can be indeed performed by a pure generative model without such a classifier: in what we call classifier-free guidance, we jointly train a conditional and an unconditional diffusion model, and we combine the resulting conditional and unconditional score estimates to attain a trade-off between sample quality and diversity similar to that obtained using classifier guidance.

**Metadatos de la página, verbatim:**

> Computer Science > Machine Learning
> arXiv:2207.12598 (cs)
> [Submitted on 26 Jul 2022]
> Title: Classifier-Free Diffusion Guidance
> Authors: Jonathan Ho, Tim Salimans
> Comments: A short version of this paper appeared in the NeurIPS 2021 Workshop on Deep Generative Models and Downstream Applications: https://openreview.net/pdf?id=qw8AKxfYbI
> Subjects: Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
> Cite as: arXiv:2207.12598 [cs.LG]
> https://doi.org/10.48550/arXiv.2207.12598
