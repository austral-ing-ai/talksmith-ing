---
source_file: sam-kirillov-2023
source_type: web-capture
ingested_at: 2026-08-14
---

# Segment Anything (arXiv:2304.02643) — página de abstract

## Provenance
- Original location: `research/web/sam-kirillov-2023/`
- Format: web-capture (arXiv `abs` page; `page.md` + `original.html` + `assets/`)
- URL: https://arxiv.org/abs/2304.02643
- Author / source (if known): Alexander Kirillov et al. (Meta AI Research, FAIR) — 12 autores
- Date of original (if known): 5 abr 2023 (v1, única versión)
- Fetched at: 2026-08-14T17:03:10Z (HTTP 200, 41.618 bytes)
- Rol en la Clase 9: el modelo fundacional de segmentación — bisagra del bloque, y la fuente contra la que hay que verificar dos cifras del deck.

## Key claims

- **Autores:** Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao, Chloe Rolland, Laura Gustafson, Tete Xiao, Spencer Whitehead, Alexander C. Berg, Wan-Yen Lo, Piotr Dollár, Ross Girshick. **Año:** 2023. **Venue:** preprint arXiv; el paper se presentó luego en ICCV 2023 (la página `abs` **no** menciona venue: el campo `Comments` sólo enlaza el sitio del proyecto). **arXiv ID:** arXiv:2304.02643 [cs.CV, cs.AI, cs.LG]. **DOI:** 10.48550/arXiv.2304.02643.
- El proyecto Segment Anything (SA) presenta **tres cosas a la vez: una tarea nueva, un modelo y un dataset** para segmentación de imágenes. Esa tripleta es la estructura del paper.
- Usando el propio modelo dentro de un **bucle de recolección de datos**, construyeron el mayor dataset de segmentación hasta la fecha "por lejos": **más de 1.000 millones de máscaras sobre 11 millones de imágenes** licenciadas y respetuosas de la privacidad.
- El modelo está **diseñado y entrenado para ser *promptable***, de modo que transfiere *zero-shot* a nuevas distribuciones de imágenes y a nuevas tareas.
- El desempeño zero-shot es "impresionante", **a menudo competitivo con o superior a resultados previos totalmente supervisados**.
- Liberan modelo (SAM) y dataset (SA-1B) en `https://segment-anything.com` para fomentar la investigación en modelos fundacionales de visión.

## Definitions and terminology

- **Tarea promptable (*promptable segmentation*).** "The model is designed and trained to be promptable, so it can transfer zero-shot to new image distributions and tasks." El abstract enuncia la propiedad y la consecuencia (transferencia zero-shot) pero **no define qué es un prompt en este contexto** — puntos, cajas, máscaras gruesas, texto — ni describe la ambigüedad de prompt (un clic puede referirse a la camisa, a la persona o al grupo). La clase sí enseña esos detalles; no salen de acá.
- **Image encoder / prompt encoder / mask decoder.** **Ausentes del abstract.** Los tres componentes de la arquitectura SAM que la clase desmenuza no se nombran ni una vez en la página capturada. Están en la figura 4 y la sección 3 del paper, fuera de la captura. Esto es central para la verificación de la cifra de "~95% del cómputo" (ver abajo).
- **Data engine (bucle de recolección de datos).** "Using our efficient model in a data collection loop, we built the largest segmentation dataset to date". El abstract describe el mecanismo en una frase —el modelo se usa para anotar, las anotaciones mejoran el modelo— pero **no lo llama "data engine"** ni describe sus tres etapas (asistida manual, semiautomática, totalmente automática). El término *data engine* sí aparece explícito en los abstracts de SAM 2 y SAM 3.
- **Zero-shot transfer.** Aplicar el modelo a distribuciones y tareas no vistas en entrenamiento sin ajuste adicional.
- **Modelo fundacional de visión** (*foundation model for computer vision*). El encuadre que el paper reclama para SAM.
- **SA-1B.** El dataset liberado: 1.000 M de máscaras, 11 M de imágenes.

## Evidence and examples

- **"over 1 billion masks on 11M licensed and privacy respecting images"** — el dato central del paper.
- **SA-1B** liberado públicamente junto con los pesos de SAM.
- Evaluación en "numerous tasks" con desempeño zero-shot competitivo o superior a supervisados. **El abstract no da ni un solo número de benchmark** — ni mIoU, ni AP, ni tasa de acierto, ni latencia.
- Peso del envío a arXiv: 14.399 KB (v1), coherente con un paper cargado de figuras.

### Verificación de cifras del deck

- **"1.000 M de máscaras sobre 11 M de imágenes" — CIERRA.** El abstract dice literalmente "over 1 billion masks on 11M licensed and privacy respecting images" y repite "1B masks and 11M images" al describir SA-1B. Única precisión menor: la fuente dice **"más de"** 1.000 M; el deck redondea a 1.000 M, lo cual subestima levemente pero no distorsiona.
- **"~95% del cómputo" para el image encoder (slide 20) — NO CIERRA: la cifra no está en la fuente.** La página capturada **no publica ninguna descomposición del costo de inferencia**. Más aún: el abstract ni siquiera nombra al image encoder. Lo que el paper sí sostiene en su cuerpo (fuera de esta captura) es una afirmación *cualitativa* de la misma familia — el image encoder se corre **una sola vez por imagen** y es pesado (un ViT-H), mientras que el prompt encoder y el mask decoder son livianos y se ejecutan **por prompt** en el navegador en ~50 ms, lo que permite interacción en tiempo real. Esa asimetría es real y es el punto pedagógico que la slide quiere transmitir; el problema es el **número**: "~95%" se presenta como dato medido y **el paper no lo publica**. Recomendación para el deck: reformular en términos cualitativos ("el image encoder concentra casi todo el costo y se ejecuta una vez por imagen; el decoder corre en milisegundos por cada prompt") o, si se quiere conservar un número, atribuirlo explícitamente como estimación propia y no al paper.

## Inconsistencies / open questions

1. **La página capturada trae solo el abstract.** Lo que la clase necesitaría y no está:
   - **La figura de arquitectura** (image encoder → prompt encoder → mask decoder), que es la imagen que sostiene todo el bloque SAM del deck.
   - La descripción del **data engine** y sus tres etapas.
   - Las **cifras de latencia** (~50 ms por prompt en navegador) y el desglose de costo entre encoder y decoder — precisamente lo que haría falta para juzgar la cifra del "~95%".
   - Los **números de benchmark zero-shot** en las 23 tareas evaluadas.
   - La discusión de **ambigüedad de prompt** y la salida de tres máscaras con puntajes de confianza.
   Todo eso está en el PDF (`https://arxiv.org/pdf/2304.02643`) y en el sitio del proyecto, no capturados.
2. **"~95% del cómputo" no tiene respaldo en la fuente.** Ver el detalle en *Verificación de cifras del deck*. Es la afirmación del deck con el respaldo documental más débil de las cuatro verificadas.
3. **Cero números de desempeño en el abstract.** "Often competitive with or even superior to prior fully supervised results" es una afirmación fuerte enunciada sin una sola medición. Para citarla en clase hace falta o bien atenuar el fraseo, o bien traer los números del cuerpo del paper.
4. **Métrica de evaluación:** consistente con el hueco general del deck, esta fuente tampoco define ni reporta métrica alguna de segmentación. La única fuente del conjunto que lo hace con número en la página capturada es FCN (mean IU 62,2%), y la figura de resultados del post de Meta (cgF1, pHOTA, J&F, mIoU, gIoU).
5. **Venue no declarado:** la página `abs` no dice dónde se publicó. Si el deck lo cita como "ICCV 2023", el dato es correcto pero **no proviene de esta fuente**.

## Images / diagrams

La captura de una página `abs` de arXiv **no incluye ninguna figura del paper** — en particular, no trae el diagrama de arquitectura de SAM. Los tres archivos guardados son cromo del sitio, copiados a la carpeta compañera por completitud.

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

> We introduce the Segment Anything (SA) project: a new task, model, and dataset for image segmentation. Using our efficient model in a data collection loop, we built the largest segmentation dataset to date (by far), with over 1 billion masks on 11M licensed and privacy respecting images. The model is designed and trained to be promptable, so it can transfer zero-shot to new image distributions and tasks. We evaluate its capabilities on numerous tasks and find that its zero-shot performance is impressive -- often competitive with or even superior to prior fully supervised results. We are releasing the Segment Anything Model (SAM) and corresponding dataset (SA-1B) of 1B masks and 11M images at https://segment-anything.com to foster research into foundation models for computer vision.

**Metadatos de la página, verbatim:**

> Computer Science > Computer Vision and Pattern Recognition
> arXiv:2304.02643 (cs)
> [Submitted on 5 Apr 2023]
> Title: Segment Anything
> Authors: Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao, Chloe Rolland, Laura Gustafson, Tete Xiao, Spencer Whitehead, Alexander C. Berg, Wan-Yen Lo, Piotr Dollár, Ross Girshick
> Comments: Project web-page: https://segment-anything.com
> Subjects: Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
> Cite as: arXiv:2304.02643 [cs.CV]
> https://doi.org/10.48550/arXiv.2304.02643

**Historial de envíos:**

> From: Alexander Kirillov
> [v1] Wed, 5 Apr 2023 17:59:46 UTC (14,399 KB)
