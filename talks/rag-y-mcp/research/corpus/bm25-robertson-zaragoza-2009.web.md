---
source_file: bm25-robertson-zaragoza-2009
source_type: web-capture
ingested_at: 2026-08-14
---

# The Probabilistic Relevance Framework: BM25 and Beyond (Robertson & Zaragoza, 2009)

## Provenance
- Original location: `research/web/bm25-robertson-zaragoza-2009/`
- Format: captura web de un PDF académico. **El `page.md` (~102.000 caracteres) no es un abstract ni un resumen: es el texto completo del monográfico extraído del PDF con pdfminer.** La captura guardó el binario como `original.html` y como `original.pdf` (mismo archivo, 10 páginas según `file`, 57 páginas de contenido real). La extracción es fiel en prosa y fórmulas simples, pero las ecuaciones LaTeX complejas y las tablas quedaron desarmadas en columnas verticales de números; las figuras se extrajeron aparte a la carpeta compañera.
- URL: https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf
- Autor / fuente: Stephen Robertson (Microsoft Research, Cambridge) y Hugo Zaragoza (Yahoo! Research, Barcelona). *Foundations and Trends in Information Retrieval*, vol. 3, n.º 4 (2009), pp. 333–389. DOI 10.1561/1500000019.
- Fecha del original: 2009 (PDF producido el 16 de diciembre de 2009).
- `http_status`: 200 · `fetched_at`: 2026-08-14T16:57:34Z · sin assets web (las imágenes salen del PDF).

## Key claims

- **BM25 no es una heurística: se deriva de un marco probabilístico.** El Probabilistic Relevance Framework (PRF) parte de tratar la relevancia como una variable oculta asociada al par consulta–documento, estima una probabilidad de relevancia para cada par y ordena los documentos en orden descendente de esa probabilidad. BM25 es la instanciación más conocida del marco. Este es el argumento que la clase puede usar para contestar "¿por qué esa fórmula tan rara?".
- **El modelo se desarrolló en etapas a lo largo de unos 30 años**, con un precursor en 1960. No es un algoritmo publicado de una vez.
- **Dos propiedades hacen a BM25 distinto de tf·idf clásico: saturación de la frecuencia de término y normalización suave por longitud.** Ninguna de las dos aparece en tf·idf lineal.
- **La saturación se justifica desde el modelo 2-Poisson y la noción de "eliteness"** (que un término sea "elite" en un documento = que el documento trate de ese concepto). Bajo esos supuestos, el peso del término crece monótonamente con tf pero se acerca asintóticamente a un máximo. Ese máximo es exactamente el peso que tendría la eliteness si fuera observable.
- **La normalización por longitud es "suave" a propósito**, porque la variación de longitud entre documentos se explica por dos causas opuestas: *verbosity* (el autor usa más palabras para decir lo mismo → habría que normalizar dividiendo por la longitud) y *scope* (el autor tiene más para decir → no habría que normalizar). El parámetro `b` interpola entre ambas hipótesis.
- **El modelo no dice cómo fijar `k1` y `b`.** Los autores lo reconocen explícitamente como una limitación: "the model provides no guidance on how these should be set". Los valores usuales salen de experimentación empírica, no de teoría.
- **La variante con `(k1 + 1)` en el numerador no cambia el ranking.** Es cosmética: se agrega para que el peso de una sola ocurrencia coincida con el peso RSJ usado por sí solo. Útil si en clase aparece la fórmula con `(k1+1)` y alguien pregunta por qué a veces está y a veces no.
- **Sin información de relevancia, el peso RSJ colapsa en una aproximación cercana al idf clásico.** Es decir, el idf de BM25 no es una elección arbitraria sino un caso límite del modelo probabilístico.
- **BM25 y BM25F son robustos frente a sus parámetros**: cambios chicos en los valores (o en la colección) no producen cambios grandes en la calidad. Optimizarlos sí da ganancias significativas, sobre todo en una colección nueva.
- **Optimizar métricas de IR es difícil**: son caras de evaluar, tienen máximos locales y mesetas, no son suaves y no tienen gradientes. Por eso el capítulo 5 recurre a búsqueda exhaustiva acelerada con heurísticas (caché, grilla, robust line search) en vez de optimización estándar.
- **BM25F extiende BM25 a documentos con campos/streams** (título, cuerpo, anchor text) ponderando la frecuencia total por stream **antes** de aplicar la saturación, no después. Es la variante que los autores señalan como exitosa en búsqueda web y corporativa.

## Definitions and terminology

**Saturación de TF (*saturation*).** El aporte de un mismo término al score del documento no puede superar un punto de saturación, por muy frecuentemente que aparezca. Cita textual: "any one term's contribution to the document score cannot exceed a saturation point (the asymptotic limit), however, frequently it occurs in the document. This turns out to be a very valuable property of the BM25 weighting function". La función paramétrica elegida para aproximar esa forma es, con `k > 0`:

```
    tf / (k + tf)
```

Comportamiento del parámetro (importante para explicarlo en clase, sección 3.4.4): con **`k` alto**, los incrementos de tf siguen contribuyendo de manera significativa al score; con **`k` bajo**, el aporte de una ocurrencia nueva se apaga muy rápido. En la Figura 3.3 los autores grafican `k = 0.2`, `k = 1`, `k = 3` y `k = 10`. Como la función se aplica a todos los términos, la altura absoluta no importa: lo que importa son los incrementos relativos.

**Normalización suave por longitud.** Se define la longitud del documento `dl` como la suma de las tf sobre el vocabulario, y `avdl` como el promedio de la colección. El componente de normalización es:

```
    B = (1 - b) + b · (dl / avdl),    con 0 ≤ b ≤ 1
```

`b = 1` aplica normalización completa por longitud; `b = 0` la apaga. Detalle práctico que la clase puede citar: como la normalización se define *en relación al promedio*, la definición concreta de longitud casi no importa — se puede usar cantidad de caracteres, cantidad de palabras antes de parsear, o incluso cantidad de términos únicos, y los resultados son muy similares.

**Fórmula final de BM25 (Ecuación 3.15).** Se normaliza tf con `B` y recién después se aplica la saturación:

```
    tf' = tf / B

    w_i^BM25(tf) = [ tf' / (k1 + tf') ] · w_i^RSJ
                 = tf / ( k1 · ((1 - b) + b · dl/avdl) + tf ) · w_i^RSJ
```

El score total del documento es la suma de estos pesos sobre los términos de la consulta (original o expandida).

**Valores de `k1` y `b`.** Cita textual: "values such as `0.5 < b < 0.8` and `1.2 < k1 < 2` are reasonably good in many circumstances. However, there is also evidence that optimal values do depend on other factors (such as the type of documents or queries)". Aparte, los autores mencionan que algunas versiones publicadas fijan `b = 0.5` y `k1 = 2`, aunque "many experiments suggest a somewhat lower value of `k1` and a somewhat higher value of `b`". **Nota para la clase: el rango citado con más frecuencia en la industria (`k1 = 1.2`, `b = 0.75`) cae dentro de estos intervalos, pero este paper no lo enuncia como default — enuncia rangos.**

**Peso RSJ (Robertson/Spärck Jones), Ecuación 3.2.** Con `N` = tamaño de la muestra juzgada, `n_i` = documentos que contienen `t_i`, `R` = tamaño del conjunto relevante, `r_i` = relevantes que contienen `t_i`:

```
    w_i^RSJ = log [ (r_i + 0.5)(N - R - n_i + r_i + 0.5) ] / [ (n_i - r_i + 0.5)(R - r_i + 0.5) ]
```

Los `0.5` son pseudo-conteos que evitan infinitos y hacen el estimador más robusto.

**Idf como caso límite (Ecuación 3.3).** Sin ninguna información de relevancia se pone `R = r_i = 0` (equivalente a asumir `P(t_i | rel) = 0.5`) y queda:

```
    w_i^IDF = log [ (N - n_i + 0.5) / (n_i + 0.5) ]
```

que es "a close approximation to classical idf".

**Eliteness.** Propiedad oculta por término y documento: el documento es "elite" para un término si trata del concepto que ese término denota. La única asociación entre `tf` y relevancia pasa por la eliteness. Es el puente conceptual entre el modelo 2-Poisson y la forma saturante.

**Verbosity vs. scope.** Las dos hipótesis rivales que explican por qué un documento es más largo, y la razón de que `b` sea un parámetro interpolador y no un interruptor.

**BIM (Binary Independence Model).** Caso en el que `TF_i` es binaria (presencia/ausencia). Da el peso de la Ecuación 3.1 y, con estimación, el RSJ.

**BM25F.** Extensión a documentos estructurados en `S` streams con pesos `v_s`: se calcula una tf total ponderada `tf̃_i = Σ_s v_s · tf_si` y una longitud ponderada `dl̃ = Σ_s v_s · sl_s`, y recién sobre esas cantidades se aplican normalización y saturación. El vector de parámetros crece a `θ = (k1, b1, …, b_S, v1, …, v_S)`.

**PRF (Probabilistic Relevance Framework).** El nombre que los autores dan a la familia de modelos que desarrollan, para distinguirla de los language models (LM) y de divergence from randomness (DFR), que también son probabilísticos pero no tienen la relevancia como noción primitiva.

## Evidence and examples

- **Rangos de parámetros reportados como buenos en muchas circunstancias**: `0.5 < b < 0.8`, `1.2 < k1 < 2`. Combinación común en versiones publicadas: `b = 0.5`, `k1 = 2`.
- **Las tres variantes históricas de la fórmula que los autores descartan como poco importantes**: (a) el componente `qtf` con su propia constante `k3` para consultas largas — los experimentos sugirieron que el efecto de saturación en `qtf` no era importante, y la fórmula quedó lineal en `qtf`; (b) una corrección adicional por longitud sobre el score total — "again found to be unimportant"; (c) el `(k1 + 1)` en el numerador — no afecta el ranking.
- **Comparación con tf·idf tradicional**: las funciones de tf habituales en la literatura son `tf` misma y `(1 + log tf)`. La segunda tiene una curva de forma parecida a la saturante, "but does not have an asymptotic maximum — it goes to infinity, even if somewhat slower than tf itself". Es un buen contraejemplo para una slide.
- **Caso especial en que la saturación no aplica** (sección 3.4.3): si se asume que la eliteness de cada término de consulta coincide con la relevancia (`p_i1 = 1`, `p_i0 = 0`), el límite es infinito y el peso queda lineal en tf — es decir, el tf·idf tradicional "encaja" con ese modelo. Los autores señalan que la función no lineal saturante funciona mejor en la práctica.
- **Costo de la optimización de parámetros**: requiere evaluación humana de muchos resultados de consulta, los parámetros óptimos son específicos de la colección evaluada y pueden no transferir, y el procedimiento puede requerir más cómputo que el propio motor de búsqueda. Los autores lo justifican sólo para colecciones de alto valor: la Web, colecciones corporativas grandes, sitios de noticias o de ayuda.
- **Conclusión de los autores** (cita, sección 6): "One of the reasons of the success of the PRF, we believe, is the powerful combination of sound theoretical modelling and a pragmatic parameterisation that exploits our prior knowledge in IR."

## Inconsistencies / open questions

- **El paper no fija `k1 = 1.2` ni `b = 0.75`.** Da rangos (`1.2 < k1 < 2`, `0.5 < b < 0.8`) y menciona `k1 = 2`, `b = 0.5` como combinación publicada frecuente. Si el deck presenta `k1 = 1.2, b = 0.75` como "los valores del paper", eso es una atribución incorrecta: son los defaults de implementaciones (Lucene/Elasticsearch), compatibles con los rangos pero no enunciados aquí.
- **Los autores admiten que el modelo no orienta la elección de parámetros.** Es una limitación reconocida, no un detalle menor: "This may be regarded as a limitation of the model."
- **Extracción del PDF con pérdidas estructurales.** Todas las tablas del monográfico (incluida la tabla de pesos de streams para BM25F alrededor de la línea 1900 del `page.md`) quedaron como columnas verticales de números sueltos, sin encabezados alineados. Las ecuaciones con símbolos LaTeX aparecen con artefactos `(cid:1)`, `(cid:2)`, `(cid:4)`. Las fórmulas centrales (3.10, 3.12, 3.13–3.15, 3.2, 3.3) se reconstruyeron a mano en este registro y están verificadas contra el texto circundante; cualquier cifra tomada de las tablas del PDF debe verificarse contra el `original.pdf` antes de citarse en una slide.
- **La Figura 3.3** (funciones de saturación con `k = 0.2, 1, 3, 10` y con normalización por longitud para `dl = avdl·0.1`, `avdl`, `avdl·10`) es un gráfico vectorial, no un raster incrustado: **no se pudo extraer como imagen** y no está en la carpeta compañera. Sus etiquetas sí quedaron en el texto (líneas 1300-1440 del `page.md`). Si la clase quiere mostrar el efecto de `k1`, hay que regenerar el gráfico o capturar la página 27 del PDF.
- **Este paper no habla de RAG, embeddings ni búsqueda híbrida** — es de 2009. Toda conexión con el pipeline moderno (BM25 como rama léxica de un retriever híbrido) es de la clase, no de la fuente.

## Images / diagrams

Siete figuras raster extraídas del PDF con `pdfimages`. Se descartaron doce decoraciones de portada (logos de la editorial, <600 bytes, duplicadas entre las páginas 1 y 3).

### `bm25-robertson-zaragoza-2009.web/images/pdf-page-012-012.png`
- **Provenance**: PDF `original.pdf`, página 12. Corresponde a la **Fig. 2.1 — "Graphical model indicating basic independence assumptions"**.
- **Depiction**: modelo gráfico (notación de placas) en blanco y negro. Un nodo circular arriba, etiquetado `Rel`. Una flecha vertical baja hacia una placa rectangular que contiene un nodo circular `tf_i`. La placa lleva el índice `i ∈ V` en su borde inferior.
- **Why it matters**: es la formalización de "la relevancia es la causa oculta de las frecuencias observadas". Sirve para justificar visualmente por qué el score es una suma sobre términos: los `tf_i` son condicionalmente independientes dado `Rel`.
- **Transcribed text**: `Rel` · `tf_i` · `i ∈ V`.

### `bm25-robertson-zaragoza-2009.web/images/pdf-page-013-013.png`
- **Provenance**: PDF `original.pdf`, página 13. Corresponde a la **Fig. 2.2 — "Graphical model for restriction to query terms"**.
- **Depiction**: idéntico al anterior salvo el índice de la placa, que ahora es `i ∈ q` en vez de `i ∈ V`.
- **Why it matters**: muestra el paso de "todo el vocabulario" a "sólo los términos de la consulta", que es lo que hace computable el modelo. Puede usarse en pareja con la figura anterior para una slide de dos pasos.
- **Transcribed text**: `Rel` · `tf_i` · `i ∈ q`.

### `bm25-robertson-zaragoza-2009.web/images/pdf-page-023-014.png`
- **Provenance**: PDF `original.pdf`, página 23. Corresponde a la **Fig. 3.1 — "Graphical model of eliteness (E)"**.
- **Depiction**: misma notación de placas, ahora con tres nodos en cadena: `Rel` arriba, flecha hacia `E_i` dentro de la placa, y de `E_i` una flecha hacia `tf_i`. Índice de la placa: `i ∈ q`.
- **Why it matters**: es *la* figura que explica de dónde sale la saturación. La frecuencia observada no depende de la relevancia directamente, sino a través de la variable oculta de eliteness; por eso lo máximo que puede aportar un término es la evidencia de que el documento es elite para él, y de ahí el techo asintótico.
- **Transcribed text**: `Rel` · `E_i` · `tf_i` · `i ∈ q`.

### `bm25-robertson-zaragoza-2009.web/images/pdf-page-027-015.png`
- **Provenance**: PDF `original.pdf`, página 27. Panel **izquierdo** de la **Fig. 3.2 — "Left: some possible saturation functions"**.
- **Depiction**: gráfico a color, ejes negros. Eje horizontal etiquetado `term frequency (tf_i)`, de `0` a `∞`. Eje vertical de `0` a `1`, con una línea punteada horizontal en `1` marcando la asíntota. Tres curvas de formas muy distintas suben desde el origen hacia esa asíntota: una turquesa que sube rápido y escalonada, una roja con forma de S clásica, y una azul-violeta que se mantiene pegada al eje hasta muy tarde y luego sube casi vertical. Una línea vertical clara marca un punto de referencia sobre el eje.
- **Why it matters**: ilustra que las cuatro propiedades listadas (pasa por 0, monótona creciente, asintótica, con límite `w^BIM`) **no determinan una única función**. Es el argumento de que hubo que elegir una forma paramétrica, no derivarla.
- **Transcribed text**: `1` (eje vertical) · `0` (origen) · `term frequency ( tf_i )` · `∞`.

### `bm25-robertson-zaragoza-2009.web/images/pdf-page-027-016.png`
- **Provenance**: PDF `original.pdf`, página 27. Panel **derecho** de la **Fig. 3.2 — "Right: saturation functions generated by the 2-Poisson model"**.
- **Depiction**: mismo sistema de ejes, ahora en gris. Tres curvas suaves, todas convexas o casi, que suben desde el origen y convergen a la asíntota punteada en `1`. La curva superior sube muy rápido; la del medio es casi lineal en el tramo inicial; la inferior tiene una concavidad inicial antes de subir.
- **Why it matters**: es el contraste con el panel izquierdo — el modelo 2-Poisson genera curvas *mucho más suaves* que las arbitrarias, y "for most realistic combinations of the parameters the curve is convex, as the top two lines; for some combinations it has an initial concavity, as the bottom line". Esta es la forma que la función `tf/(k+tf)` va a aproximar. Es la mejor figura del paper para una slide sobre saturación.
- **Transcribed text**: `1` · `0` · `term frequency ( tf_i )` · `∞`.

### `bm25-robertson-zaragoza-2009.web/images/pdf-page-050-017.png`
- **Provenance**: PDF `original.pdf`, página 50. Corresponde a la **Fig. 5.1 — "Greedy Optimisation example: robust line search"**.
- **Depiction**: diagrama en escala de grises. Eje vertical rotulado `retrieval performance`, eje horizontal rotulado `1-D parametere space` (sic — con la errata "parametere" en el original). Una curva irregular con varios máximos locales y una meseta describe la métrica de recuperación en función del parámetro. Debajo, filas horizontales de puntos grises unidos por líneas punteadas representan iteraciones sucesivas de la búsqueda; los puntos evaluados en cada iteración están numerados a la derecha (`1`, `2 (z)`, `3 (z)`, `4 (t)`, `5 (z)`, `6 (t)`, `7 (z)`), y flechas verticales y una flecha gris horizontal indican cómo la región de búsqueda se re-centra y se escala hacia el mejor punto.
- **Why it matters**: evidencia visual de por qué tunear `k1` y `b` es caro: la función objetivo no es suave, tiene máximos locales y mesetas. Si la clase menciona "y después hay que tunearlo", esta figura muestra el costo real.
- **Transcribed text**: `retrieval performance` · `1-D parametere space` · `1` · `2 (z)` · `3 (z)` · `4 (t)` · `5 (z)` · `6 (t)` · `7 (z)`.

### `bm25-robertson-zaragoza-2009.web/images/pdf-page-051-018.png`
- **Provenance**: PDF `original.pdf`, página 51. Corresponde a la **Fig. 5.2 — "Greedy optimisation example: promising directions"**.
- **Depiction**: cuadrado de fondo celeste que representa un espacio de parámetros bidimensional. Líneas de trazo y punto horizontales, verticales y diagonales lo cruzan, rotuladas en los bordes `(1a)`, `(1b)`, `(1c)`, `(2a)`, `(2b)`, `(2c)`. Sobre ellas, marcadores de distintas formas (punto lleno, círculo, triángulos huecos apuntando en varias direcciones, un círculo con cruz) marcan puntos evaluados, y flechas rectas conectan la secuencia de movimientos desde el punto superior izquierdo hacia el centro-derecha y luego hacia abajo.
- **Why it matters**: complemento de la anterior para el caso multidimensional (`θ = (k1, b)` en BM25, y muchos más en BM25F). Secundaria para la clase salvo que se quiera argumentar que BM25F es caro de calibrar.
- **Transcribed text**: `(1a)` · `(1b)` · `(1c)` · `(2a)` · `(2b)` · `(2c)`.

## Raw / preserved excerpts

**Abstract (verbatim, inglés):**

> The Probabilistic Relevance Framework (PRF) is a formal framework for document retrieval, grounded in work done in the 1970–1980s, which led to the development of one of the most successful text-retrieval algorithms, BM25. In recent years, research in the PRF has yielded new retrieval models capable of taking into account document meta-data (especially structure and link-graph information). Again, this has led to one of the most successful Web-search and corporate-search algorithms, BM25F. This work presents the PRF from a conceptual point of view, describing the probabilistic modelling assumptions behind the framework and the different ranking algorithms that result from its application: the binary independence model, relevance feedback models, BM25 and BM25F. It also discusses the relation between the PRF and other statistical models for IR, and covers some related topics, such as the use of non-textual features, and parameter optimisation for models with free parameters.

**Sección 3.4.2, Saturación — las cuatro propiedades y la definición (verbatim):**

> Clearly its exact behaviour depends on the parameters, but some generalisations are possible. We note in particular that:
> 1. w_i^elite(0) = 0 (this is by design);
> 2. w_i^elite(tf) increases monotonically with tf;
> 3. . . . but asymptotically approaches a maximum value as tf → ∞; and
> 4. the asymptotic limit being
>    lim_{tf→∞} w_i^elite(tf) = log [ p1(1 − p0) / ((1 − p1) p0) ] = w_i^BIM.
>
> This last formulation is the weight that the eliteness feature on its own would have. That is, if eliteness were observable, instead of being hidden, we could treat it like a simple binary attribute and weight it in exactly the same way as we weighted term presence in the binary independence model.
>
> This asymptotic property makes perfect sense. Given (as we have assumed) that the only association between tf and relevance is via eliteness, the best information we can hope to get from a term is that the document is indeed elite for that term. In reality our information on this score is probabilistic, and thus the term weight is correspondingly reduced. [...]
>
> We refer to this behaviour as saturation. That is, any one term's contribution to the document score cannot exceed a saturation point (the asymptotic limit), however, frequently it occurs in the document. This turns out to be a very valuable property of the BM25 weighting function defined below.

**Sección 3.4.4, elección de la función paramétrica y efecto de `k` (verbatim):**

> The next step in the development of BM25 is to approximate this shape. Lacking an appropriate generative corpus model from which to derive a convenient formula, the authors of BM25 decided to fit a simple parametric curve to this shape. The following one-parameter function was chosen:
>
>     tf / (k + tf)   for some k > 0        (3.10)
>
> This function satisfies the properties listed above, and fits well the possible convex curves. We show values of this function for three different values of k in Figure 3.3; the middle line is for k = 1, the upper line for lower k and the lower line for higher k. Note that because we apply this to all terms, the absolute height does not matter; what matters is the relative increments for different increments in tf. Thus for high k, increments in tf continue to contribute significantly to the score, whereas for low k, the additional contribution of a newly observed occurrence tails off very rapidly.

**Sección 3.4.5, longitud de documento — verbosity vs. scope (verbatim):**

> We suppose that there is something like a standard length for a document, but that an author may decide to make a document longer or shorter; we consider only the longer case. Why might an author so decide? We can postulate two extreme cases:
>
> **Verbosity:** Some authors are simply more verbose than others, using more words to say the same thing.
>
> **Scope:** Some authors have more to say: they may write a single document containing or covering more ground. An extreme version would have the author writing two or more documents and concatenating them.
>
> The verbosity hypothesis suggests that we should simply normalise any observed tfs by dividing by document length. The scope hypothesis, on the other hand, at least in its extreme version, suggests the opposite. In a real collection of documents we will observe variations in length, which might be due to either effect, or to a combination. We suppose in general a combination: that each hypothesis represents some partial explanation for the observed variation. This in turn suggests that we should apply some kind of soft normalisation.

> The soft length normalisation component is:
>
>     B := (1 − b) + b · (dl / avdl),    0 ≤ b ≤ 1        (3.12)
>
> Thus setting b = 1 will perform full document-length normalisation, while b = 0 will switch normalisation off.

> The length normalisation component will be defined in relation to the average; this ensures that the definition of document length used is not critical. In practice, we could take (for example) the number of characters in the document, or the number of words before parsing, or even the number of unique terms, and still get very similar results.

**Sección 3.5, valores de los parámetros (verbatim):**

> Concerning the internal parameters, the model provides no guidance on how these should be set. This may be regarded as a limitation of the model. However, it provides an opportunity for optimisation, given some evaluated set of queries and relevance judgements in the traditional retrieval experiment style. A significant number of such experiments have been done, and suggest that in general values such as 0.5 < b < 0.8 and 1.2 < k1 < 2 are reasonably good in many circumstances. However, there is also evidence that optimal values do depend on other factors (such as the type of documents or queries).

**Sección 3.5.1, variantes de la fórmula (verbatim):**

> • The original had a component for within-query term frequency qtf, for longer queries where a term might occur multiple times. In its full generality, this had a similar saturation function to that used for tf, but with its own k3 constant. However, experiments suggested that the saturation effect for qtf was unimportant, leading to a formula which was linear in qtf. In other words, one could simply treat multiple occurrences of a term in the query as different terms.
>
> • The original also had a further correction for document length, to the total document score. This correction was again found to be unimportant.
>
> • A common variant is to add a (k1 + 1) component to the numerator of the saturation function. This is the same for all terms, and therefore does not affect the ranking produced. The reason for including it was to make the final formula more compatible with the RSJ weight used on its own. If it is included, then a single occurrence of a term would have the same weight in both schemes.
>
> • Some published versions are based on specific values assigned to b and k1. A common combination would be b = 0.5 and k1 = 2. (However, many experiments suggest a somewhat lower value of k1 and a somewhat higher value of b.)

**Sección 3.5, BM25 frente a tf·idf tradicional (verbatim):**

> In the absence of relevance information, it reduces as before to a form of idf. In this case, the BM25 weight looks very much like a traditional tf∗idf weight — a product of two components, one based on tf and one on idf. However, there is one significant difference. The tf component involves the saturation function discussed, and is therefore somewhat unlike most other tf functions seen in the literature, where common choices are tf itself and (1 + log tf). The latter has a somewhat similar shape curve, but does not have an asymptotic maximum — it goes to infinity, even if somewhat slower than tf itself.

**Sección 5, dificultad de la optimización (verbatim):**

> Like most IR models, the models in the PRF have free parameters that need to be set to appropriate values. The BM25 and BM25F models are known to be quite robust with respect to their parameters, meaning that small changes in the parameter values (or in the collection) do not produce large changes in accuracy or relevance. Nevertheless significant gains in relevance can be obtained by properly optimising the parameters, specially when we deal with a new collection.
>
> Parameter optimisation comes with considerable costs: it will require the human evaluation of many query results, which is expensive, and the optimised parameters will be specific to the collection evaluated and may not work well for other collections. Furthermore, the optimisation procedure can be computationally costly, requiring more computing power that the search engine itself. For these reasons this approach is only appropriate for specific collections which merit the cost needed to optimise the ranking function.

> Optimising standard IR measures, however, is not easy: they are very expensive to evaluate, they have local maxima and plateaus, they are not smooth and they don't have gradients [49].

**Sección 6, Conclusiones (verbatim):**

> The classical probabilistic relevance framework has provided a series of well-founded scoring formula, as well as some significant insights into different aspects of search. One of the reasons of the success of the PRF, we believe, is the powerful combination of sound theoretical modelling and a pragmatic parameterisation that exploits our prior knowledge in IR. We do not believe that the PRF has reached the end of its useful life. When it is well understood, the PRF model can provide a solid ground on which to analyse new IR problems and derive new solutions.
