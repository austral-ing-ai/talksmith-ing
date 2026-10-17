---
source_file: adain-huang-belongie-2017
source_type: web-capture
ingested_at: 2026-08-14
---

# Arbitrary Style Transfer in Real-time with Adaptive Instance Normalization — AdaIN (Huang & Belongie, 2017) — página abstract de arXiv

## Provenance
- Original location: `research/web/adain-huang-belongie-2017/`
- Format: html (captura web de `talksmith:ingest` — `page.md` + `original.html` + `assets/`)
- Author / source (if known): Xun Huang, Serge Belongie (Cornell; afiliación no visible en la captura) — arXiv
- Date of original (if known): enviado el 20 de marzo de 2017 (v1), última revisión 30 de julio de 2017 (v2, la capturada). Captura: 2026-08-14T17:02:50Z, HTTP 200, URL `https://arxiv.org/abs/1703.06868`

## Key claims

- **Contexto del problema**: Gatys et al. mostraron cómo renderizar una imagen de contenido en el estilo de otra (*style transfer*), pero su marco requiere un proceso de optimización iterativo lento que limita su aplicación práctica. Las aproximaciones rápidas con redes feed-forward aceleraron el proceso, **pero al costo de quedar atadas a un conjunto fijo de estilos**.
- **La contribución: la capa AdaIN.** *"At the heart of our method is a novel adaptive instance normalization (AdaIN) layer that aligns the mean and variance of the content features with those of the style features."* La definición operativa cabe en una línea: **alinear media y varianza de las features de contenido con las de estilo.**
- **Primera transferencia de estilo arbitraria en tiempo real.** Reclaman ser los primeros en habilitar *arbitrary style transfer* en tiempo real, con velocidad comparable al método más rápido existente y sin la restricción a un conjunto predefinido de estilos.
- **Controles flexibles para el usuario con una sola red feed-forward**: trade-off contenido-estilo, interpolación de estilos, controles de color y espaciales — todo *"using a single feed-forward neural network"*.
- **Por qué está en el corpus de una clase de GANs**: AdaIN no es una GAN. Es el mecanismo que **StyleGAN toma prestado** de la literatura de transferencia de estilo — el abstract de StyleGAN dice explícitamente *"borrowing from style transfer literature"*. Este registro es la fuente primaria de esa deuda técnica.

Datos bibliográficos para la cita:
- Autores: Xun Huang, Serge Belongie
- Año: 2017
- arXiv ID: **arXiv:1703.06868 [cs.CV]** (v2)
- DOI: `https://doi.org/10.48550/arXiv.1703.06868`
- Materias: Computer Vision and Pattern Recognition (cs.CV)
- Venue: Comments dice **"ICCV 2017"**, con código disponible en `https://github.com/xunhuang1995/AdaIN-style`.

## Definitions and terminology

- **AdaIN (adaptive instance normalization)**: capa que **alinea la media y la varianza de las features de contenido con las de las features de estilo**. Esta es la definición primaria y verbatim del término, y es la que la clase necesita cuando explica cómo StyleGAN inyecta el estilo `w` en cada resolución del generador. En StyleGAN, "estilo" no es una imagen de referencia sino un vector aprendido, pero **la operación es la misma**: normalizar y re-escalar por media y varianza aprendidas.
- **Instance normalization**: normalización por instancia (por muestra y canal). El paper la vuelve *adaptativa* al hacer que los parámetros de escala y desplazamiento vengan de las features de estilo en vez de ser aprendidos y fijos. El abstract no desarrolla esto; se infiere del nombre y de la descripción de la operación.
- **Transferencia de estilo arbitraria (arbitrary style transfer)**: aplicar cualquier estilo, incluido uno nunca visto en entrenamiento, sin reentrenar. Se opone a los métodos feed-forward previos, atados a un conjunto fijo de estilos.
- **Trade-off contenido-estilo (content-style trade-off)**: control continuo sobre cuánto pesa cada uno. Es el antecedente directo del *truncation trick* y del *style mixing* en el vocabulario de StyleGAN.
- **Interpolación de estilos (style interpolation)**: mezclar dos o más estilos. Antecedente conceptual del *style mixing*.
- **Feed-forward único**: una sola pasada, sin optimización iterativa por imagen. Es lo que compra la velocidad de tiempo real.

## Evidence and examples

- **Velocidad**: "comparable to the fastest existing approach" — comparación relativa, **sin milisegundos ni FPS en la captura**.
- **Capacidades demostradas**, todas con una sola red: trade-off contenido-estilo, interpolación de estilos, controles de color y espaciales.
- **Código público**: `https://github.com/xunhuang1995/AdaIN-style` — enlazado desde el campo Comments. Es la única fuente del corpus, junto con `cyclegan-zhu-2017` y `serrano-gans-lab`, que ofrece código ejecutable.
- **Sin datasets nombrados** en la captura. (El paper usa MS-COCO como contenido y WikiArt como estilo; no está en este registro.)
- Peso de la subida: 9.696 KB en ambas versiones.

## Inconsistencies / open questions

- **Riesgo de confusión conceptual en clase**: AdaIN es de 2017 y **no es una GAN** — no hay generador, discriminador ni entrenamiento adversarial. Si aparece en la tabla del linaje de GANs (slide 39) sin aclaración, sugiere una filiación que no existe. Su lugar correcto es como **influencia externa** sobre StyleGAN, no como eslabón de la cadena GAN. Lo mismo, con más razón todavía, vale para `sam-kirillov-2023.web.md`.
- **El vínculo con StyleGAN es real pero indirecto en las fuentes**: el abstract de StyleGAN dice "borrowing from style transfer literature" **sin nombrar AdaIN ni a Huang & Belongie**. La conexión explícita está en el cuerpo del paper de StyleGAN, no en ninguna de las dos capturas. Es una inferencia bien fundada, no una cita directa — conviene presentarla así.
- **Datasets**: la captura no nombra ninguno. No ayuda a cerrar el hueco de datasets del deck.
- **Gap de extracción**: sin figuras. La comparación visual de estilos y la Figura 2 (el diagrama encoder–AdaIN–decoder) están en el PDF.

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

> Abstract: Gatys et al. recently introduced a neural algorithm that renders a content image in the style of another image, achieving so-called style transfer. However, their framework requires a slow iterative optimization process, which limits its practical application. Fast approximations with feed-forward neural networks have been proposed to speed up neural style transfer. Unfortunately, the speed improvement comes at a cost: the network is usually tied to a fixed set of styles and cannot adapt to arbitrary new styles. In this paper, we present a simple yet effective approach that for the first time enables arbitrary style transfer in real-time. At the heart of our method is a novel adaptive instance normalization (AdaIN) layer that aligns the mean and variance of the content features with those of the style features. Our method achieves speed comparable to the fastest existing approach, without the restriction to a pre-defined set of styles. In addition, our approach allows flexible user controls such as content-style trade-off, style interpolation, color & spatial controls, all using a single feed-forward neural network.

Bloque bibliográfico verbatim:

> Computer Science > Computer Vision and Pattern Recognition
> **arXiv:1703.06868** (cs) [Submitted on 20 Mar 2017 (v1), last revised 30 Jul 2017 (this version, v2)]
> Title: Arbitrary Style Transfer in Real-time with Adaptive Instance Normalization
> Authors: Xun Huang, Serge Belongie
> Comments: ICCV 2017. Code is available: https://github.com/xunhuang1995/AdaIN-style
> Subjects: Computer Vision and Pattern Recognition (cs.CV)
> Cite as: arXiv:1703.06868 [cs.CV] (or arXiv:1703.06868v2 [cs.CV] for this version)
> https://doi.org/10.48550/arXiv.1703.06868

> Submission history
> From: Xun Huang
> **[v1]** Mon, 20 Mar 2017 17:51:31 UTC (9,696 KB)
> **[v2]** Sun, 30 Jul 2017 09:32:17 UTC (9,696 KB)
