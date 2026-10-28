---
source_file: fcn-long-2015
source_type: web-capture
ingested_at: 2026-08-14
---

# Fully Convolutional Networks for Semantic Segmentation (arXiv:1411.4038) — página de abstract

## Provenance
- Original location: `research/web/fcn-long-2015/`
- Format: web-capture (arXiv `abs` page; `page.md` + `original.html` + `assets/`)
- URL: https://arxiv.org/abs/1411.4038
- Author / source (if known): Jonathan Long, Evan Shelhamer, Trevor Darrell (UC Berkeley)
- Date of original (if known): enviado 14 nov 2014; última revisión 8 mar 2015 (v2). Publicado en CVPR 2015.
- Fetched at: 2026-08-14T17:03:10Z (HTTP 200, 42.204 bytes)
- Rol en la Clase 9: primera parada del bloque de segmentación — el paper que convierte una red de clasificación en una red que predice píxel a píxel.

## Key claims

- **Autores:** Jonathan Long, Evan Shelhamer, Trevor Darrell. **Año:** 2014 (v1) / 2015 (v2). **Venue:** CVPR 2015. **arXiv ID:** arXiv:1411.4038 [cs.CV]. **DOI:** 10.48550/arXiv.1411.4038.
- Las redes convolucionales entrenadas *end-to-end, pixels-to-pixels* superan por sí solas el estado del arte en segmentación semántica: no hace falta pipeline externo de post-procesamiento.
- La idea central es construir redes **"fully convolutional"**: aceptan entrada de tamaño arbitrario y producen salida del tamaño correspondiente, con inferencia y aprendizaje eficientes.
- Redes de clasificación contemporáneas (AlexNet, VGG, GoogLeNet) se **adaptan** a fully convolutional y sus representaciones aprendidas se **transfieren por fine-tuning** a la tarea de segmentación. Este es el argumento de reutilización de preentrenamiento que la clase repite después con SAM y CLIP.
- Arquitectura nueva que **combina información semántica de una capa profunda y gruesa con información de apariencia de una capa superficial y fina** para producir segmentaciones precisas y detalladas. Es el antecedente directo de las *skip connections* de U-Net.
- Resultado: estado del arte en PASCAL VOC (mejora relativa del 20%, hasta **62,2% mean IU** en 2012), NYUDv2 y SIFT Flow, con inferencia de **un tercio de segundo** por imagen típica.

## Definitions and terminology

- **Segmentación semántica.** La tarea que el paper ataca: asignar una etiqueta de clase a cada píxel. El abstract no la define formalmente ni la contrasta con segmentación de instancias o panóptica — esas distinciones, que la clase sí enseña, no aparecen en esta fuente.
- **Fully convolutional network (FCN) / convolucionalización.** "Build 'fully convolutional' networks that take input of arbitrary size and produce correspondingly-sized output with efficient inference and learning." Es exactamente el concepto que la clase llama *convolucionalización*: reemplazar las capas densas finales de una red de clasificación por convoluciones, de modo que la salida deje de ser un vector de clases y pase a ser un mapa espacial. El abstract enuncia la propiedad (entrada arbitraria → salida del tamaño correspondiente) pero **no explica el mecanismo** de reescritura de la capa densa como convolución 1×1.
- **Predicción densa espacial** (*spatially dense prediction*). La familia de tareas a la que el paper aplica las FCN.
- **Fusión profundo/superficial (skip).** "Combines semantic information from a deep, coarse layer with appearance information from a shallow, fine layer". El abstract nombra la combinación pero no usa el término *skip connection* ni describe la arquitectura FCN-32s/16s/8s.
- **mean IU** (mean intersection-over-union). Métrica de evaluación que el abstract reporta sin definir.

## Evidence and examples

- **62,2% mean IU en PASCAL VOC 2012**, con **20% de mejora relativa** sobre el estado del arte previo. Es el único número de calidad de segmentación del abstract.
- Datasets adicionales donde alcanza estado del arte: **NYUDv2** y **SIFT Flow**.
- **Velocidad de inferencia: un tercio de segundo** por imagen típica (hardware no especificado en el abstract).
- Redes base adaptadas: **AlexNet, VGG, GoogLeNet**.
- Tamaño de los envíos a arXiv: v1 5.641 KB, v2 4.333 KB (dato de la página, sin valor de contenido).

### Verificación de cifras del deck

El deck no cita ninguna cifra de FCN, así que no hay nada que contrastar en esa dirección. Lo relevante va al revés: **esta fuente aporta la métrica que al deck le falta** (ver más abajo).

## Inconsistencies / open questions

1. **La página capturada trae solo el abstract.** No hay figuras, ni cuerpo, ni tablas. Lo que la clase necesitaría y acá no está:
   - El diagrama de convolucionalización (la capa densa reescrita como convolución), que es la imagen que explica el concepto de un vistazo.
   - La arquitectura FCN-32s / FCN-16s / FCN-8s y la explicación de qué gana cada nivel de fusión.
   - La definición de *mean IU* y las tablas comparativas por clase.
   - El mecanismo de *upsampling* / convolución transpuesta que devuelve el mapa a resolución original.
   Para cualquiera de esas cosas hay que ir al PDF (`https://arxiv.org/pdf/1411.4038`) o al HTML experimental (`https://arxiv.org/html/1411.4038v2`), ninguno de los dos capturado.
2. **Métrica de evaluación — el hueco del deck.** El deck dedica 22 slides a segmentación **sin definir ninguna métrica de evaluación**: ni Dice ni IoU aparecen en ningún lado. Esta fuente reporta **mean IU (intersection-over-union promediado sobre clases) = 62,2% en PASCAL VOC 2012**. Es justo el gancho que el deck necesita: la métrica canónica de segmentación aparece, con número concreto, en el primer paper del bloque. Anotado también en `unet-ronneberger-2015.web.md` y `sam31-meta-2026.web.md`.
3. El abstract enuncia la fusión profundo/superficial pero **no la llama skip connection**. Si la clase presenta a FCN como el origen de las skip connections de U-Net, la atribución es defendible por contenido pero no es literal en esta fuente.

## Images / diagrams

La captura de una página `abs` de arXiv **no incluye ninguna figura del paper**. Los tres archivos de imagen que arrastró son cromo del sitio; se copiaron a la carpeta compañera por completitud, no por valor didáctico.

  - **Depiction:** logotipo institucional de arXiv en la barra superior del sitio (vectorial, tema claro).
  - **Why it matters:** nada. Cromo de navegación.
  - **Transcribed text:** "arXiv" (atributo `alt` del HTML: "archive").
  - **Depiction:** ícono de 16×16 px del gestor de marcadores BibSonomy — un grafo de nodos gris con el nodo central en magenta.
  - **Why it matters:** nada. Botón de "guardar en" del pie de página.
  - **Transcribed text:** ninguno (atributo `alt`: "BibSonomy").
  - **Depiction:** ícono de 18×18 px de Reddit — la mascota "Snoo" en gris con los ojos en rojo.
  - **Why it matters:** nada. Botón de compartir.
  - **Transcribed text:** ninguno (atributo `alt`: "Reddit").

## Raw / preserved excerpts

**Abstract completo, verbatim (inglés):**

> Convolutional networks are powerful visual models that yield hierarchies of features. We show that convolutional networks by themselves, trained end-to-end, pixels-to-pixels, exceed the state-of-the-art in semantic segmentation. Our key insight is to build "fully convolutional" networks that take input of arbitrary size and produce correspondingly-sized output with efficient inference and learning. We define and detail the space of fully convolutional networks, explain their application to spatially dense prediction tasks, and draw connections to prior models. We adapt contemporary classification networks (AlexNet, the VGG net, and GoogLeNet) into fully convolutional networks and transfer their learned representations by fine-tuning to the segmentation task. We then define a novel architecture that combines semantic information from a deep, coarse layer with appearance information from a shallow, fine layer to produce accurate and detailed segmentations. Our fully convolutional network achieves state-of-the-art segmentation of PASCAL VOC (20% relative improvement to 62.2% mean IU on 2012), NYUDv2, and SIFT Flow, while inference takes one third of a second for a typical image.

**Metadatos de la página, verbatim:**

> Computer Science > Computer Vision and Pattern Recognition
> arXiv:1411.4038 (cs)
> [Submitted on 14 Nov 2014 (v1), last revised 8 Mar 2015 (this version, v2)]
> Title: Fully Convolutional Networks for Semantic Segmentation
> Authors: Jonathan Long, Evan Shelhamer, Trevor Darrell
> Comments: to appear in CVPR (2015)
> Subjects: Computer Vision and Pattern Recognition (cs.CV)
> Cite as: arXiv:1411.4038 [cs.CV]
> https://doi.org/10.48550/arXiv.1411.4038

**Historial de envíos:**

> From: Jonathan Long
> [v1] Fri, 14 Nov 2014 20:46:03 UTC (5,641 KB)
> [v2] Sun, 8 Mar 2015 22:16:40 UTC (4,333 KB)
