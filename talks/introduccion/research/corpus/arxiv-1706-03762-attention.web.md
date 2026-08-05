---
source_file: arxiv-1706-03762-attention
source_type: web-capture
ingested_at: 2026-08-05
---

# Attention Is All You Need (arXiv:1706.03762) — página de abstract

## Provenance
- Ubicación original: `research/web/arxiv-1706-03762-attention/`
- Formato: captura web (`original.html` 44.193 bytes + `page.md` 8.213 bytes + `assets/`)
- URL: https://arxiv.org/abs/1706.03762
- Autores: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones,
  Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin
- Fecha del original: enviado el **12 de junio de 2017** (v1); última revisión **2 de agosto de 2023** (v7)
- Capturado el: 2026-08-05T12:19:22Z · HTTP 200
- **Alcance de la captura: solo la página de abstract.** No se capturó el PDF ni el HTML del cuerpo
  del paper. Todo lo que sigue proviene del abstract y de los metadatos bibliográficos.

## Key claims

- Los modelos dominantes de transducción de secuencias (a 2017) se basan en redes recurrentes o
  convolucionales complejas en configuración encoder-decoder; los mejores conectan encoder y decoder
  mediante un mecanismo de atención.
- Los autores proponen una arquitectura nueva y simple, el **Transformer**, basada *únicamente* en
  mecanismos de atención, **prescindiendo por completo de recurrencia y convoluciones**.
- Experimentos en dos tareas de traducción automática muestran que estos modelos son superiores en
  calidad, **más paralelizables** y requieren **significativamente menos tiempo de entrenamiento**.
- Resultado WMT 2014 inglés→alemán: **28,4 BLEU**, mejorando los mejores resultados existentes
  (incluidos ensembles) por más de 2 BLEU.
- Resultado WMT 2014 inglés→francés: nuevo estado del arte de modelo único con **41,8 BLEU** tras
  entrenar **3,5 días en ocho GPUs**, una fracción pequeña del costo de entrenamiento de los mejores
  modelos de la literatura.
- El Transformer **generaliza bien a otras tareas**: se aplicó con éxito a análisis sintáctico de
  constituyentes en inglés, tanto con datos de entrenamiento abundantes como limitados.

## Definitions and terminology

- **Transformer**: la arquitectura propuesta; red basada exclusivamente en atención, sin recurrencia
  ni convolución. El paper la introduce; la página de abstract no la describe en detalle.
- **Sequence transduction model**: modelo que mapea una secuencia de entrada a una secuencia de
  salida (por ejemplo, traducción).
- **Encoder-decoder**: configuración en dos bloques, uno que codifica la entrada y otro que genera
  la salida.
- **Attention mechanism**: mecanismo que conecta encoder y decoder; en el Transformer pasa de ser
  un complemento a ser el único componente.
- **BLEU**: métrica de calidad de traducción automática usada para los dos resultados citados.

## Evidence and examples

| Tarea | Resultado | Comparación |
|---|---|---|
| WMT 2014 inglés→alemán | 28,4 BLEU | +2 BLEU sobre el mejor resultado previo, incluidos ensembles |
| WMT 2014 inglés→francés | 41,8 BLEU | nuevo estado del arte de modelo único |
| Costo de entrenamiento (en→fr) | 3,5 días × 8 GPUs | "una fracción pequeña" del costo de los mejores modelos previos |
| English constituency parsing | "aplicado con éxito" | con datos abundantes y limitados; sin cifras en el abstract |

Metadatos bibliográficos:
- **Comments:** 15 páginas, 5 figuras
- **Subjects:** Computation and Language (cs.CL); Machine Learning (cs.LG)
- **DOI:** https://doi.org/10.48550/arXiv.1706.03762
- **Licencia:** arXiv non-exclusive distribution license 1.0
- **Trackbacks:** 123 blog links registrados por arXiv
- Historial de envíos: v1 12-jun-2017 (1.102 KB) · v2 19-jun-2017 · v3 20-jun-2017 · v4 30-jun-2017 ·
  v5 6-dic-2017 · v6 24-jul-2023 · v7 2-ago-2023 (1.124 KB). Enviado por Llion Jones.

## Inconsistencies / open questions

- **La captura no contiene el paper.** Solo hay abstract + metadatos. Las 5 figuras (incluido el
  diagrama de arquitectura del Transformer, que es lo que suele querer una diapositiva) **no están
  en esta captura**. Habría que traer el PDF (`/pdf/1706.03762`) o el HTML experimental
  (`https://arxiv.org/html/1706.03762v7`) por separado.
- Ninguna cifra interna del paper (número de capas, dimensiones, cabezas de atención, tamaño del
  modelo) está disponible acá. Una diapositiva que las cite necesita otra fuente.
- El abstract no dice **por qué** la atención sola alcanza; solo que alcanza. La explicación
  mecánica vive en el cuerpo del paper.
- Hay 6 años entre v1 (2017) y v7 (2023) sin registro de qué cambió entre versiones. La captura no
  incluye diff ni changelog.
- El `page.md` contiene basura de navegación de arXiv (barras de herramientas, arXivLabs,
  recomendadores) mezclada con el contenido. Es ruido de extracción, no contenido de la fuente.

## Images / diagrams

Las 4 imágenes que la captura descargó son **cromo del sitio arXiv**, no figuras del paper. Se
copiaron a la carpeta companion por completitud, pero ninguna tiene valor expositivo.

- `arxiv-1706-03762-attention.web/images/arxiv-logo-primary-light.svg`
  - Provenance: `research/web/arxiv-1706-03762-attention/assets/`; origen
    `https://arxiv.org/static/base/1.0.1/images/arxiv-logo-primary-light.svg`; alt = "archive"
  - Depiction: logotipo de arXiv (versión clara), elemento de cabecera del sitio.
  - Why it matters: no aplica. Cromo del sitio.
- `arxiv-1706-03762-attention.web/images/smileybones-small.svg`
  - Provenance: `assets/`; origen `https://arxiv.org/static/base/1.0.1/images/icons/smileybones-small.svg`; alt vacío
  - Depiction: ícono decorativo del banner "arXiv is now an independent nonprofit".
  - Why it matters: no aplica. Cromo del sitio.
- `arxiv-1706-03762-attention.web/images/bibsonomy.png`
  - Provenance: `assets/`; origen `https://arxiv.org/static/browse/0.3.4/images/icons/social/bibsonomy.png`; alt = "BibSonomy"
  - Depiction: ícono social de BibSonomy en la sección "Bookmark".
  - Why it matters: no aplica. Cromo del sitio.
- `arxiv-1706-03762-attention.web/images/reddit.png`
  - Provenance: `assets/`; origen `https://arxiv.org/static/browse/0.3.4/images/icons/social/reddit.png`; alt = "Reddit"
  - Depiction: ícono social de Reddit en la sección "Bookmark".
  - Why it matters: no aplica. Cromo del sitio.

**Las 5 figuras del paper no fueron capturadas.**

## Raw / preserved excerpts

Abstract completo, verbatim:

> Abstract:The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

Bloque bibliográfico, verbatim:

> Comments: 15 pages, 5 figures Subjects: Computation and Language (cs.CL); Machine Learning (cs.LG) Cite as: arXiv:1706.03762 [cs.CL] (or arXiv:1706.03762v7 [cs.CL] for this version) https://doi.org/10.48550/arXiv.1706.03762

Lista de autores, verbatim y en orden:

> Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin
