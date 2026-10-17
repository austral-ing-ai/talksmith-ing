---
source_file: pix2pix-isola-2017
source_type: web-capture
ingested_at: 2026-08-14
---

# Image-to-Image Translation with Conditional Adversarial Networks — pix2pix (Isola et al., 2017) — página abstract de arXiv

## Provenance
- Original location: `research/web/pix2pix-isola-2017/`
- Format: html (captura web de `talksmith:ingest` — `page.md` + `original.html` + `assets/`)
- Author / source (if known): Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, Alexei A. Efros (Berkeley AI Research; afiliación no visible en la captura) — arXiv
- Date of original (if known): enviado el 21 de noviembre de 2016 (v1), última revisión 26 de noviembre de 2018 (v3, la capturada). Captura: 2026-08-14T17:02:59Z, HTTP 200, URL `https://arxiv.org/abs/1611.07004`

## Key claims

- **Investigan las redes adversariales condicionales como solución de propósito general para los problemas de traducción imagen a imagen.** El término clave es *general-purpose*: una misma receta para tareas que antes exigían formulaciones de pérdida muy distintas.
- **La idea que hay que llevarse a la clase: estas redes no solo aprenden el mapeo de imagen de entrada a imagen de salida, sino que aprenden también la función de pérdida con la que entrenar ese mapeo.** *"These networks not only learn the mapping from input image to output image, but also learn a loss function to train this mapping."*
- **Por eso el mismo enfoque genérico sirve para problemas que tradicionalmente requerían formulaciones de pérdida muy diferentes.**
- **Tareas demostradas**: sintetizar fotos a partir de mapas de etiquetas, reconstruir objetos a partir de mapas de bordes, y colorizar imágenes, entre otras.
- **Evidencia de adopción, no solo de laboratorio**: desde la publicación del software pix2pix, "un gran número de usuarios de internet (muchos de ellos artistas)" publicaron sus propios experimentos, demostrando su amplia aplicabilidad y su facilidad de adopción **sin necesidad de ajustar parámetros** (*without the need for parameter tweaking*).
- **El cierre del abstract es la frase con más filo retórica del corpus**, y funciona muy bien como cita de slide: *"As a community, we no longer hand-engineer our mapping functions, and this work suggests we can achieve reasonable results without hand-engineering our loss functions either."*
- **pix2pix es una cGAN aplicada.** Es el eslabón que conecta `cgan-mirza-osindero-2014.web.md` (condicionamiento por etiqueta) con la traducción imagen a imagen: acá la condición **es una imagen entera**, no una etiqueta de clase.

Datos bibliográficos para la cita:
- Autores: Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, Alexei A. Efros
- Año: 2016 (arXiv v1) / **2017 (CVPR)**
- arXiv ID: **arXiv:1611.07004 [cs.CV]** (v3)
- DOI: `https://doi.org/10.48550/arXiv.1611.07004`
- Materias: Computer Vision and Pattern Recognition (cs.CV)
- Venue: Comments dice **"Website: https://phillipi.github.io/pix2pix/, CVPR 2017"**.

## Definitions and terminology

- **Traducción imagen a imagen (image-to-image translation)**: clase de problemas cuyo objetivo es aprender el mapeo entre una imagen de entrada y una imagen de salida. Definición operativa del paper.
- **Condicionamiento por imagen**: la extensión de la cGAN de Mirza & Osindero en la que el dato condicionante `y` es una imagen completa. La captura no usa esa expresión, pero es la lectura correcta del título ("Conditional Adversarial Networks").
- **Pérdida aprendida (learned loss)**: la idea central. El discriminador **es** la función de pérdida: en vez de escribir a mano qué significa "buena salida" para cada tarea, se la aprende.
- **Mapa de etiquetas (label map)**: imagen de segmentación semántica usada como entrada (por ejemplo, fachadas etiquetadas → foto).
- **Mapa de bordes (edge map)**: contornos usados como entrada (boceto → objeto).
- **Datos apareados (paired data)**: **el abstract no lo dice, pero pix2pix requiere pares alineados de entrada/salida.** Es el supuesto que CycleGAN elimina un año después, y sin nombrarlo la contraposición pix2pix/CycleGAN de la slide 44 no se entiende. La afirmación explícita está en el abstract de `cyclegan-zhu-2017.web.md` ("using a training set of aligned image pairs... for many tasks, paired training data will not be available"), que es de los mismos autores. Citar esa, no esta.

## Evidence and examples

- **Tareas concretas nombradas**: fotos a partir de mapas de etiquetas; reconstrucción de objetos a partir de mapas de bordes; colorización. Sirven como ejemplos de aula sin necesidad de ir al PDF.
- **Adopción pública**: gran número de usuarios de internet, muchos artistas, publicando experimentos propios. Es evidencia sociológica, no cuantitativa — el abstract no da un número.
- **Sin necesidad de ajuste de parámetros**: reclamo explícito del abstract.
- **Sitio del proyecto**: `https://phillipi.github.io/pix2pix/` — con demos y galería.
- **Sin datasets nombrados y sin métricas** en la captura. El paper usa Cityscapes, CMP Facades y otros, y evalúa con "FCN-score" y estudios de percepción en Amazon Mechanical Turk; **nada de eso está acá**.
- Historial de versiones extendido: v1 nov-2016, v2 nov-2017, v3 nov-2018 (8.044 → 9.126 KB).

## Inconsistencies / open questions

- **Falta el supuesto de datos apareados**, que es el punto que hace inteligible la pareja pix2pix/CycleGAN de la slide 44. El abstract de pix2pix **no menciona** que requiere pares alineados. Sin ese contraste, "pix2pix hace traducción imagen a imagen" y "CycleGAN hace traducción imagen a imagen" suenan idénticos y la slide pierde su razón de ser. La cita correcta para el contraste está en `cyclegan-zhu-2017.web.md`.
- **Datasets**: ninguno nombrado. No ayuda a cerrar el hueco de datasets del deck.
- **Métricas**: ninguna. Si el deck sostiene que pix2pix "funciona mejor", este registro no lo respalda con números.
- **Gap de extracción**: la captura no trae la Figura 1 (la grilla de tareas: bordes→foto, mapa→aérea, día→noche, B&N→color), que es exactamente la figura que la clase querría proyectar en la slide 44. Está en el PDF y en el sitio del proyecto.
- **Año**: arXiv 2016, CVPR 2017. Otra fila donde el criterio de año de la tabla del linaje importa.

## Images / diagrams

La captura solo trajo chrome de la interfaz de arXiv. Ninguna imagen del paper.

  - Depiction: logotipo de arXiv en versión clara, SVG vectorial de 246.98 × 111.12, siete trazados agrupados. Texto convertido a curvas.
  - Why it matters: branding del sitio, sin valor de contenido.
  - Transcribed text: (el logo dibuja "arXiv"; sin texto seleccionable). `alt="archive"`.
  - Depiction: ícono social de BibSonomy, 16×16 px, huesos cruzados en rojo.
  - Why it matters: chrome de UI.
  - Transcribed text: ninguno. `alt="BibSonomy"`.
  - Depiction: ícono social de Reddit, 16×16 px, mascota Snoo en naranja y blanco.
  - Why it matters: chrome de UI.
  - Transcribed text: ninguno. `alt="Reddit"`.

## Raw / preserved excerpts

Abstract completo, verbatim (inglés original):

> Abstract: We investigate conditional adversarial networks as a general-purpose solution to image-to-image translation problems. These networks not only learn the mapping from input image to output image, but also learn a loss function to train this mapping. This makes it possible to apply the same generic approach to problems that traditionally would require very different loss formulations. We demonstrate that this approach is effective at synthesizing photos from label maps, reconstructing objects from edge maps, and colorizing images, among other tasks. Indeed, since the release of the pix2pix software associated with this paper, a large number of internet users (many of them artists) have posted their own experiments with our system, further demonstrating its wide applicability and ease of adoption without the need for parameter tweaking. As a community, we no longer hand-engineer our mapping functions, and this work suggests we can achieve reasonable results without hand-engineering our loss functions either.

Bloque bibliográfico verbatim:

> Computer Science > Computer Vision and Pattern Recognition
> **arXiv:1611.07004** (cs) [Submitted on 21 Nov 2016 (v1), last revised 26 Nov 2018 (this version, v3)]
> Title: Image-to-Image Translation with Conditional Adversarial Networks
> Authors: Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, Alexei A. Efros
> Comments: Website: https://phillipi.github.io/pix2pix/, CVPR 2017
> Subjects: Computer Vision and Pattern Recognition (cs.CV)
> Cite as: arXiv:1611.07004 [cs.CV] (or arXiv:1611.07004v3 [cs.CV] for this version)
> https://doi.org/10.48550/arXiv.1611.07004

> Submission history
> From: Jun-Yan Zhu
> **[v1]** Mon, 21 Nov 2016 20:48:16 UTC (8,044 KB)
> **[v2]** Wed, 22 Nov 2017 11:48:39 UTC (8,963 KB)
> **[v3]** Mon, 26 Nov 2018 13:54:12 UTC (9,126 KB)
