---
source_file: cyclegan-zhu-2017
source_type: web-capture
ingested_at: 2026-08-14
---

# Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks — CycleGAN (Zhu et al., 2017) — página abstract de arXiv

## Provenance
- Original location: `research/web/cyclegan-zhu-2017/`
- Format: html (captura web de `talksmith:ingest` — `page.md` + `original.html` + `assets/`)
- Author / source (if known): Jun-Yan Zhu, Taesung Park, Phillip Isola, Alexei A. Efros (Berkeley AI Research; afiliación no visible en la captura) — arXiv
- Date of original (if known): enviado el 30 de marzo de 2017 (v1), última revisión 24 de agosto de 2020 (v7, la capturada). Captura: 2026-08-14T17:02:59Z, HTTP 200, URL `https://arxiv.org/abs/1703.10593`

## Key claims

- **Definen el problema y su límite en la misma línea**: la traducción imagen a imagen aprende el mapeo entre una imagen de entrada y una de salida "usando un conjunto de entrenamiento de **pares de imágenes alineadas**". Y acto seguido: **"sin embargo, para muchas tareas, no habrá datos de entrenamiento apareados disponibles."** Esta es **la** cita que hace inteligible la contraposición pix2pix / CycleGAN de la slide 44, y la fuente correcta para ella (el abstract de pix2pix no menciona el requisito de pares).
- **Aprenden a traducir de un dominio origen `X` a un dominio destino `Y` en ausencia de ejemplos apareados.**
- **El objetivo adversarial solo**: aprender `G: X → Y` tal que la distribución de `G(X)` sea indistinguible de la distribución `Y`.
- **El problema técnico y su solución — la idea central del paper**: como ese mapeo está **fuertemente subdeterminado** (*highly under-constrained*), lo acoplan con un mapeo inverso `F: Y → X` e introducen una **pérdida de consistencia de ciclo** que fuerza `F(G(X)) ≈ X` (y viceversa). En castellano de aula: *si traduzco de ida y vuelta tengo que volver al punto de partida*.
- **Resultados cualitativos en varias tareas sin datos apareados**: transferencia de estilo de colección, transfiguración de objetos, transferencia de estación, mejora de fotos, entre otras.
- **Comparaciones cuantitativas contra varios métodos previos** demuestran la superioridad del enfoque.

Datos bibliográficos para la cita:
- Autores: Jun-Yan Zhu, Taesung Park, Phillip Isola, Alexei A. Efros
- Año: 2017
- arXiv ID: **arXiv:1703.10593 [cs.CV]** (v7)
- DOI: `https://doi.org/10.48550/arXiv.1703.10593`
- Materias: Computer Vision and Pattern Recognition (cs.CV)
- Venue: Comments dice **"An extended version of our ICCV 2017 paper, v7 fixed the typos and updated the implementation details"** — **ICCV 2017**. Código y datos: `https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix`.

## Definitions and terminology

- **Consistencia de ciclo (cycle consistency)**: la restricción `F(G(X)) ≈ X` y su recíproca. Definición primaria y verbatim, con notación incluida. Es el término que la clase reutiliza.
- **Pérdida de consistencia de ciclo (cycle consistency loss)**: el término de la función objetivo que penaliza el desvío en ese viaje de ida y vuelta.
- **Datos no apareados / unpaired data**: dos colecciones de imágenes de dominios distintos **sin correspondencia uno a uno**. Un montón de fotos y un montón de cuadros de Monet, sin que ninguna foto sea "la misma escena" que ningún cuadro.
- **Datos apareados / aligned image pairs**: lo que pix2pix necesita y CycleGAN no. Definido acá por contraste.
- **Mapeo fuertemente subdeterminado (highly under-constrained)**: hay infinitos `G` que hacen que `G(X)` se parezca a `Y` en distribución sin preservar el contenido de cada imagen individual. Es **exactamente** el hueco que llena la consistencia de ciclo, y explicarlo así evita que la restricción parezca arbitraria.
- **Transfiguración de objetos (object transfiguration)**: convertir un objeto en otro — el caso cebra ↔ caballo.
- **Transferencia de estilo de colección (collection style transfer)**: tomar el estilo de un corpus entero (todo Monet) y no de una imagen sola. Se opone a AdaIN (`adain-huang-belongie-2017.web.md`), que transfiere el estilo de **una** imagen de referencia.

## Evidence and examples

- **Tareas nombradas en el abstract**: transferencia de estilo de colección, transfiguración de objetos, transferencia de estación (verano ↔ invierno), mejora de fotos.
- **El ejemplo cebra ↔ caballo** no aparece en esta captura, pero **sí está en el corpus**: la figura de CycleGAN con las cuatro imágenes (cebra→caballo, caballo→cebra) fue capturada, sin atribución, en la página de AWS — ver `aws-que-es-una-gan.web/images/ML-6149-image005-500.jpg`, transcrita en `aws-que-es-una-gan.web.md`. Si la clase quiere proyectar esa figura, conviene atribuirla a Zhu et al. 2017 y no a AWS.
- **Comparaciones cuantitativas** contra métodos previos: mencionadas, **sin números en la captura**.
- **Código y datos públicos**: `https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix` — el mismo repositorio sirve pix2pix y CycleGAN, lo cual refuerza el parentesco de la slide 44.
- **Sin datasets nombrados** en la captura (horse2zebra, summer2winter_yosemite, los conjuntos de Monet/Van Gogh/Cézanne están en el paper y en el repo, no acá).
- Historial de versiones muy largo: siete versiones entre marzo 2017 y agosto 2020. El salto de tamaño en v7 (7.235 → 35.571 KB) sugiere que se rehicieron las figuras en alta resolución.

## Inconsistencies / open questions

- **Este registro es el que sostiene la slide 44, no `pix2pix-isola-2017.web.md`.** El contraste apareado / no apareado solo está enunciado explícitamente acá. Si el deck cita a pix2pix para afirmar "requiere pares", la cita es incorrecta aunque la afirmación sea verdadera.
- **Datasets**: ninguno nombrado en la captura. No ayuda a cerrar el hueco de datasets del deck.
- **Advertencia honesta que el abstract no da y la clase debería**: la consistencia de ciclo **no garantiza** que la traducción sea semánticamente correcta. La red puede aprender a esconder información en el ciclo para poder reconstruir la entrada (el fenómeno se documentó después como *"CycleGAN is a master of steganography"*). Esto **no está en ninguna fuente de este corpus** — si el deck lo menciona, necesita una cita adicional; si no lo menciona, es un matiz que vale la pena tener a mano para preguntas.
- **Gap de extracción**: sin figuras. La Figura 1 (Monet ↔ foto, cebras ↔ caballos, verano ↔ invierno) y el diagrama de los dos ciclos están en el PDF.
- **Fecha de la v7 (2020) vs. venue (ICCV 2017)**: la captura muestra la versión 2020. Para citar, el año correcto es 2017.

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

Nota: la figura cebra ↔ caballo de este paper existe en el corpus, pero bajo otro registro — `aws-que-es-una-gan.web/images/ML-6149-image005-500.jpg`.

## Raw / preserved excerpts

Abstract completo, verbatim (inglés original). **Las dos primeras oraciones son la cita para el contraste apareado / no apareado de la slide 44:**

> Abstract: Image-to-image translation is a class of vision and graphics problems where the goal is to learn the mapping between an input image and an output image using a training set of aligned image pairs. However, for many tasks, paired training data will not be available. We present an approach for learning to translate an image from a source domain $X$ to a target domain $Y$ in the absence of paired examples. Our goal is to learn a mapping $G: X \rightarrow Y$ such that the distribution of images from $G(X)$ is indistinguishable from the distribution $Y$ using an adversarial loss. Because this mapping is highly under-constrained, we couple it with an inverse mapping $F: Y \rightarrow X$ and introduce a cycle consistency loss to push $F(G(X)) \approx X$ (and vice versa). Qualitative results are presented on several tasks where paired training data does not exist, including collection style transfer, object transfiguration, season transfer, photo enhancement, etc. Quantitative comparisons against several prior methods demonstrate the superiority of our approach.

Bloque bibliográfico verbatim:

> Computer Science > Computer Vision and Pattern Recognition
> **arXiv:1703.10593** (cs) [Submitted on 30 Mar 2017 (v1), last revised 24 Aug 2020 (this version, v7)]
> Title: Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks
> Authors: Jun-Yan Zhu, Taesung Park, Phillip Isola, Alexei A. Efros
> Comments: An extended version of our ICCV 2017 paper, v7 fixed the typos and updated the implementation details. Code and data: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
> Subjects: Computer Vision and Pattern Recognition (cs.CV)
> Cite as: arXiv:1703.10593 [cs.CV] (or arXiv:1703.10593v7 [cs.CV] for this version)
> https://doi.org/10.48550/arXiv.1703.10593

> Submission history
> From: Jun-Yan Zhu
> **[v1]** Thu, 30 Mar 2017 17:44:17 UTC (8,452 KB)
> **[v2]** Thu, 5 Oct 2017 01:19:36 UTC (8,738 KB)
> **[v3]** Fri, 24 Nov 2017 01:37:05 UTC (8,737 KB)
> **[v4]** Mon, 19 Feb 2018 06:27:55 UTC (8,736 KB)
> **[v5]** Thu, 30 Aug 2018 06:48:43 UTC (7,235 KB)
> **[v6]** Thu, 15 Nov 2018 14:38:20 UTC (7,235 KB)
> **[v7]** Mon, 24 Aug 2020 16:51:03 UTC (35,571 KB)
