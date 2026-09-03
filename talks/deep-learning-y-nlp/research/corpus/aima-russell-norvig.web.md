---
source_file: research/web/aima-russell-norvig/
source_type: web-capture
ingested_at: 2026-08-14
---

# Artificial Intelligence: A Modern Approach, 4th US ed. — sitio oficial del libro

## Provenance
- Original location: `research/web/aima-russell-norvig/`
- Format: web-capture (`page.md` extraído de `original.html`; asset en `assets/`)
- URL: https://aima.cs.berkeley.edu/
- Título de la captura: `Artificial Intelligence: A Modern Approach, 4th US ed.`
- HTTP status: 200 · byte_size: 6018
- fetched_at: 2026-08-14T16:38:24Z
- Author / source (if known): Stuart Russell (UC Berkeley) y Peter Norvig; sitio alojado en `aima.cs.berkeley.edu`
- Date of original (if known): 4.ª edición estadounidense; el pie de página declara "Modified: Aug 22, 2022"

**Nota de tipo de fuente**: esta captura **no es un paper**. Es la página de aterrizaje del libro de texto — índice, ediciones y recursos. Se trata en consecuencia: lo que aporta al corpus es *qué ofrece el sitio* y *dónde está cada cosa*, no un argumento técnico.

## Key claims

- **Qué es**: el sitio oficial de *Artificial Intelligence: A Modern Approach*, 4.ª edición estadounidense, de Stuart Russell y Peter Norvig. Es el enlace recomendado en las notas del orador de la slide 1.
- **Reclamo de autoridad, textual**: "The authoritative, most-used AI textbook, adopted by over 1500 schools". Los tres adjetivos están enlazados: "authoritative" a una búsqueda de Google por "artificial intelligence textbook", "most-used" a Open Syllabus, y el número 1500 a la propia página de adopciones del sitio. Es autopromoción del libro, no un dato de tercero verificado — aunque las dos primeras referencias sí apuntan a fuentes externas.
- **Dos ediciones vivas**: la estadounidense (US Edition) y la Global Edition, con índices separados. El sitio mantiene también una página de traducciones ("Editions").
- **El libro abre por donde abre la clase**: los dos primeros capítulos son *1 Introduction* (p. 1) y *2 Intelligent Agents* (p. 36). La definición de IA como agente racional que la clase usa en la apertura sale de ahí — de los capítulos 1 y 2. **El sitio lista los capítulos pero no reproduce su contenido**: la definición en sí no está en esta captura, aunque el prefacio sí está disponible como PDF enlazado (`newchap00.pdf`).
- **Cobertura relevante para Clase 2**: el índice ubica exactamente dónde el libro cubre el temario de esta clase — *21 Deep Learning* (p. 750), *23 Natural Language Processing* (p. 823), *24 Deep Learning for Natural Language Processing* (p. 856). El capítulo 24 es el mapa más directo al contenido de la clase.
- **Extensión**: 28 capítulos en siete partes, más dos apéndices; bibliografía en la p. 1033 e índice en la p. 1069 — más de mil páginas.

## Definitions and terminology

El sitio **no define ningún término**: es un índice, no texto expositivo. Lo que sí aporta es la nomenclatura estructural del libro, que la clase puede usar para ubicar temas:

- **Intelligent Agents** — título del capítulo 2. Es el marco conceptual (el agente racional) del que la clase toma la definición de IA con la que abre. El término aparece en la captura sólo como título de capítulo.
- Las siete partes del libro, que son la taxonomía del campo según Russell y Norvig: *I Artificial Intelligence*, *II Problem-solving*, *III Knowledge, reasoning, and planning*, *IV Uncertain knowledge and reasoning*, *V Machine Learning*, *VI Communicating, perceiving, and acting*, *VII Conclusions*.
- **Deep Learning**, **Natural Language Processing**, **Deep Learning for Natural Language Processing** — títulos de los capítulos 21, 23 y 24: el vocabulario de esta clase, ubicado dentro de la parte V (Machine Learning) y la parte VI (Communicating, perceiving, and acting).

**Advertencia para el uso en clase**: la expresión **"agente racional"** — el término que la clase efectivamente usa — **no aparece literalmente en esta captura**. El capítulo se titula "Intelligent Agents". La definición completa vive en el libro, no en el sitio.

## Evidence and examples

Lo que la página *ofrece* como recurso, que es su valor real para el corpus:

| Recurso | Enlace en el sitio | Formato |
|---|---|---|
| Prefacio | `newchap00.pdf` | PDF, descarga libre |
| Índice con subsecciones | `contents.html` | página web |
| Código de los algoritmos | https://github.com/aimacode | repositorios GitHub (organización `aimacode`, multi-lenguaje) |
| Pseudocódigo de todos los algoritmos | `algorithms.pdf` | PDF, descarga libre |
| Todas las figuras del libro | `figures.pdf` | PDF, descarga libre |
| Ejercicios | https://aimacode.github.io/aima-exercises/ | sitio web |
| Bibliografía | `Bibliography.pdf`, `aima4e.bib`, `bibcounts.html` | PDF + archivo BibTeX + datos |
| Índice analítico | `Index.pdf` | PDF |
| Errata | `errata.html` | página web |
| Página para instructores | `instructors.html` | página web |
| Adopciones / cursos | `adoptions.html` | página web (respalda el número de 1500 escuelas) |
| Ediciones y traducciones | `translations.html` | página web |
| Reseñas | `comments.html` | página web |
| Portadas | `cover.jpg` (US), `global-cover.jpg` (Global) | imágenes |

- **El dato citable más concreto**: adoptado por más de **1500** instituciones educativas (afirmación del propio sitio, enlazada a su página de adopciones).
- **Recursos abiertos**: pseudocódigo, figuras, prefacio, bibliografía y ejercicios están disponibles gratis sin comprar el libro. El código está en GitHub bajo la organización `aimacode`, con implementaciones en varios lenguajes. Para una clase que quiera dar un enlace útil de verdad, esto es más aprovechable que la portada.
- **Paginación de los capítulos relevantes**: Deep Learning p. 750, NLP p. 823, Deep Learning for NLP p. 856 — sirve para mandar a los alumnos a una página exacta.

## Inconsistencies / open questions

- **El sitio no contiene la definición que la clase le atribuye.** La slide 1 lo cita como "la fuente de la definición de IA como agente racional", pero la captura sólo lista el título del capítulo 2 ("Intelligent Agents"). El texto de la definición está en el libro impreso o en el PDF del prefacio, no en esta página. Si la slide muestra una definición entrecomillada, **su respaldo no está en este corpus**.
- **La expresión "agente racional" no figura en la captura.** El sitio dice "Intelligent Agents".
- **Página desactualizada**: el pie declara la última modificación el 22 de agosto de 2022, casi cuatro años antes de la captura. El número de 1500 adopciones y las ediciones listadas pueden haber cambiado.
- **"The authoritative, most-used AI textbook" es marketing del propio sitio.** Las referencias enlazadas (una búsqueda de Google, Open Syllabus) son endebles como evidencia; Open Syllabus es una fuente razonable, pero el enlace apunta al campo entero de Computer Science, no a un ranking específico del libro. Si el deck repite la frase, conviene atribuirla ("según el sitio del libro") en lugar de afirmarla.
- **HTML antiguo y desprolijo.** `original.html` usa tablas de layout, tiene un `<td align=right>` huérfano dentro del formulario de búsqueda y un `<H2>` que se cierra como `</h2>` sin abrir bien. La extracción a `page.md` funcionó igual — el índice completo, la portada, la línea de autores y el pie salieron bien. **No hizo falta recurrir al fallback a `original.html`**: `page.md` tiene 3.025 caracteres y varios encabezados. Se leyó `original.html` de todos modos para verificar, y no aporta contenido que `page.md` no tenga (lo único adicional es el formulario de búsqueda de Google y el script de Analytics, ambos sin valor).
- **El sitio no dice nada de lo que la clase necesita técnicamente**: no hay contenido sobre transformers, embeddings ni LLMs, más allá de los títulos de capítulo. Es un enlace de referencia y lectura complementaria, no una fuente de contenido para las slides.
- **La 4.ª edición es de 2020** (según se conoce del libro), pero **el año de publicación no aparece en la captura** — sólo dice "4th US ed." y la fecha de modificación de la página.

## Images / diagrams

La captura trajo una sola imagen, y a diferencia de los cuatro casos de arXiv, esta sí es contenido: la portada del libro.

### `aima-russell-norvig.web/images/cover2.jpg`
- **Provenance**: `research/web/aima-russell-norvig/assets/cover2.jpg`, desde `https://aima.cs.berkeley.edu/cover2.jpg`. Es la miniatura de la barra lateral izquierda del sitio (`<img title="US Edition" src="cover2.jpg" width=134>`), enlazada a la versión de resolución completa en `cover.jpg`. El atributo `alt` está vacío; el `title` dice "US Edition". JPEG de 142×180 px, RGB — resolución baja, sirve para pantalla pequeña, **no para proyectar a página completa**.
- **Depiction**: la portada de la 4.ª edición estadounidense. Sobre un tablero de ajedrez en perspectiva, en tonos morados y grises, se disponen viñetas y figuras: piezas de ajedrez blancas en primer plano a la izquierda, retratos y escenas en los cuadros del tablero (entre ellos un jugador de ajedrez, un rostro histórico en blanco y negro sobre fondo azul en el cuadro derecho, y varias imágenes pequeñas en la fila superior), y en la franja inferior una escena en tonos cálidos anaranjados. Los apellidos de los autores corren verticalmente por el borde izquierdo. En la parte inferior derecha aparece el logotipo de Pearson. El título ocupa la banda inferior central en tipografía blanca sobre el tablero.
- **Why it matters**: valor ilustrativo, no informativo. Sirve para una slide de "lectura recomendada" o para la apertura de la clase, dándole cara al libro del que sale la definición de agente racional. No contiene ningún dato citable. Si se usa en el deck, conviene bajar la versión grande (`https://aima.cs.berkeley.edu/cover.jpg`): a 142×180 px esta se pixela en cuanto se agranda.
- **Transcribed text**: `Russell` · `Norvig` (verticales, borde izquierdo) · `Artificial Intelligence` · `A Modern Approach` · `Fourth Edition` · `Pearson` (logotipo, esquina inferior derecha).

## Raw / preserved excerpts

**Cabecera y reclamo de autoridad, verbatim:**

> # Artificial Intelligence: A Modern Approach, 4th US ed.
>
> ## by [Stuart Russell](http://www.cs.berkeley.edu/~russell) and [Peter Norvig](http://www.norvig.com)
>
> The [authoritative](http://www.google.com/search?q=artificial+intelligence+textbook&ie=UTF-8&oe=UTF-8), [most-used](https://opensyllabus.org/result/field?id=Computer+Science) AI textbook, adopted by over ****[1500](adoptions.html) schools.

**Navegación lateral completa, verbatim:**

> - [⌂ US Edition](index.html)
> - [⌂ Global Edition](global-index.html)
> - [Acknowledgements](ack.html)
> - [Code](https://github.com/aimacode)
> - [Courses](adoptions.html)
> - [Editions](translations.html)
> - [Errata](errata.html)
> - [Exercises](https://aimacode.github.io/aima-exercises/)
> - [Figures](figures.pdf)
> - [Instructors Page](instructors.html)
> - [Pseudocode](algorithms.pdf)
> - [Reviews](comments.html)

**Índice completo de la 4.ª edición estadounidense, verbatim:**

> **Table of Contents** for the US Edition (or see the [Global Edition](global-index.html))
> [Preface (pdf)](newchap00.pdf); [Contents with subsections](contents.html)
> **I Artificial Intelligence**
>  1 Introduction ... 1
>  2 Intelligent Agents ... 36
> **II Problem-solving**
>  3 Solving Problems by Searching ... 63
>  4 Search in Complex Environments ... 110
>  5 Adversarial Search and Games ... 146
>  6 Constraint Satisfaction Problems ... 180
> **III Knowledge, reasoning, and planning**
>  7 Logical Agents ... 208
>  8 First-Order Logic ... 251
>  9 Inference in First-Order Logic ... 280
>  10 Knowledge Representation ... 314
>  11 Automated Planning ... 344
> **IV Uncertain knowledge and reasoning**
>  12 Quantifying Uncertainty ... 385
>  13 Probabilistic Reasoning ... 412
>  14 Probabilistic Reasoning over Time ... 461
>  15 Probabilistic Programming ... 500
>  16 Making Simple Decisions ... 528
>  17 Making Complex Decisions ... 562
>  18 Multiagent Decision Making ... 599
> **V Machine Learning**
>  19 Learning from Examples ... 651
>  20 Learning Probabilistic Models ... 721
>  21 Deep Learning ... 750
>  22 Reinforcement Learning ... 789
> **VI Communicating, perceiving, and acting**
>  23 Natural Language Processing ... 823
>  24 Deep Learning for Natural Language Processing ... 856
>  25 Computer Vision ... 881
>  26 Robotics ... 925
> **VII Conclusions**
>  27 Philosophy, Ethics, and Safety of AI ... 981
>  28 The Future of AI ... 1012
>  Appendix A: Mathematical Background ... 1023
>  Appendix B: Notes on Languages and Algorithms ... 1030
>  Bibliography ... 1033 ([pdf](Bibliography.pdf) and [LaTeX .bib file](aima4e.bib) and [bib data](bibcounts.html))
>  Index ... 1069 ([pdf](Index.pdf))

**Bloque de recursos abiertos, verbatim:**

> [Exercises (website)](https://aimacode.github.io/aima-exercises/)
> [Figures (pdf)](figures.pdf)
> [Code (website)](https://github.com/aimacode); [Pseudocode (pdf)](algorithms.pdf)
> Covers: [US](cover.jpg), [Global](global-cover.jpg)

**Pie de página, verbatim:**

> *⌂ AI: A Modern Approach*Modified: Aug 22, 2022
