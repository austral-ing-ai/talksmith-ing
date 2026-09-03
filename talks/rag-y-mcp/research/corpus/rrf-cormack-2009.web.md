---
source_file: rrf-cormack-2009
source_type: web-capture
ingested_at: 2026-08-14
---

# Reciprocal Rank Fusion outperforms Condorcet and individual Rank Learning Methods (Cormack, Clarke & Büttcher, SIGIR 2009)

## Provenance
- Original location: `research/web/rrf-cormack-2009/`
- Format: captura web de un PDF académico. **El `page.md` (~9.700 caracteres) es el texto completo del paper extraído del PDF con pdfminer, no un abstract.** Es un paper corto (2 páginas, formato poster/short paper de SIGIR), así que la extracción cubre todo: abstract, sección 1, discusión, las tres tablas y las referencias. La captura guardó el binario como `original.html` y como `original.pdf`.
- URL: https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf
- Autor / fuente: Gordon V. Cormack y Charles L. A. Clarke (University of Waterloo, Ontario, Canadá) y Stefan Büttcher (Google, Redmond, WA). Publicado en SIGIR'09, 19–23 de julio de 2009, Boston, Massachusetts, EE. UU. ACM 978-1-60558-483-6/09/07.
- Fecha del original: 2009.
- `http_status`: 200 · `fetched_at`: 2026-08-14T16:57:33Z · sin assets web.

## Key claims

- **RRF es un método no supervisado y deliberadamente ingenuo, y aun así gana.** Los autores lo diseñaron como *baseline* para comparar contra métodos de learning-to-rank, y descubrieron que "almost invariably improved on the best of the combined results". El framing histórico importa: RRF no nació como la propuesta del paper, nació como el control del experimento.
- **RRF supera consistentemente a Condorcet Fuse y a CombMNZ**, los dos estándares de metaranking de la época, y también supera al mejor sistema individual de cada experimento.
- **La ventaja medida es de 4% a 5% en promedio** sobre Condorcet, CombMNZ y el mejor sistema individual, en los experimentos piloto y de TREC.
- **La significancia estadística se estableció con un test de signos simple.** Descartando la primera corrida piloto: RRF superó a Condorcet las 7 veces (p ≈ 0.008), a CombMNZ 6 de 7 veces (p ≈ 0.04), y al mejor resultado individual 6 o 7 veces (0.008 ≤ p ≤ 0.04, según se considere o no un resultado obtenido con humano en el loop).
- **RRF combina rangos, no scores.** Comparte con Condorcet Fuse la propiedad valiosa de ser indiferente a los scores arbitrarios que devuelve cada método de ranking. Es la razón por la que sirve para fusionar BM25 (scores no acotados) con búsqueda vectorial (similitud coseno en [-1,1]) sin normalizar nada.
- **RRF es barato de implementar y de operar.** No requiere algoritmo de votación especial ni información global; los rangos se pueden computar y sumar **de a un sistema por vez**, evitando tener que mantener todos los rankings en memoria simultáneamente.
- **Hipótesis de los autores sobre por qué RRF le gana a Condorcet**: RRF aprovecha mejor la diversidad entre los rankings individuales. Uno o dos sistemas que rankeen un documento muy alto pueden mejorar sustancialmente su posición final; con Condorcet, una mayoría simple de preferencias débiles puede sobreescribir preferencias sustancialmente más fuertes.
- **El meta-learner formado aplicando RRF a los baselines de LETOR 3 es, hasta donde los autores saben, el mejor método reportado** para ese dataset, y eleva la cota inferior de lo que se sabe aprendible de él.
- **MAP es la métrica reportada por brevedad; P@k, R-precision y NDCG dan resultados comparables.**

## Definitions and terminology

**Reciprocal Rank Fusion (RRF).** Dado un conjunto `D` de documentos a rankear y un conjunto `R` de rankings, cada uno una permutación sobre `1..|D|`:

```
    RRFscore(d ∈ D) = Σ_{r ∈ R}  1 / ( k + r(d) )
```

donde `r(d)` es la posición (rango) del documento `d` en el ranking `r`. Los documentos se ordenan por ese score sumado.

**De dónde sale `k = 60` — la respuesta que el deck necesita.** Este es el punto crítico de la fuente. El paper dice, textualmente:

> where k = 60 was fixed during a pilot investigation and not altered during subsequent validation.

Y más abajo, sobre el primer experimento piloto:

> The results of the first, shown in table 1, indicated that k = 60 was near-optimal, but that the choice was not critical.

Es decir: **`k = 60` no es una constante derivada teóricamente ni un valor "óptimo" en ningún sentido fuerte. Es el valor que salió de una investigación piloto sobre los tópicos 351–400 de TREC, que resultó cercano al óptimo en esa corrida, y que los autores fijaron y no volvieron a tocar durante la validación posterior — precisamente para no contaminar la validación con tuning.** Los propios autores subrayan que la elección "was not critical". La Tabla 1 lo respalda numéricamente: el MAP varía entre .2123 (`k=10`) y .2147 (`k=80`) en todo el rango `k = 10…100`, una diferencia de 0.0024, mientras que `k = 0` (sin constante) cae a .2072 y `k = 500` a .2098. La conclusión honesta para una slide es: **`k` amortigua, importa que no sea 0 y que no sea enorme, y 60 es simplemente el valor que quedó del piloto y que la industria copió del paper.**

**Intuición detrás de la fórmula (justificación de los autores, sección 1).** La forma `1/(k + r)` se eligió porque, si bien los documentos rankeados alto son más importantes, "the importance of lower-ranked documents does not vanish as it would were, say, an exponential function used". Y sobre el rol específico de la constante: **"The constant k mitigates the impact of high rankings by outlier systems."** Es decir, `k` existe para que un sistema atípico que ponga algo en el puesto 1 no domine la fusión: sin `k`, el salto entre el rango 1 (score 1) y el rango 2 (score 0.5) es brutal; con `k = 60`, es 1/61 vs 1/62, casi nada.

**Condorcet Fuse.** Combina rankings ordenando los documentos según la relación por pares `r(d1) < r(d2)`, determinada para cada par por voto mayoritario entre los rankings de entrada. Referencia: Montague & Aslam, CIKM 2002.

**CombMNZ.** Requiere, para cada ranking `r`, una función de scoring correspondiente `s_r : D → R` y un rango de corte `c`:

```
    CMNZscore(d ∈ D) = |{ r ∈ R | r(d) ≤ c }| · Σ_{ {r | r(d) ≤ c} }  s_r(d)
```

Es decir, multiplica la suma de scores no calibrados por la cantidad de sistemas que colocaron el documento dentro del corte. Los autores señalan que por eso tiene mayor varianza: depende de que los scores de los distintos sistemas sean comparables, cosa que ocurre "by happenstance".

**Metaranking / rank fusion.** El problema de combinar los rankings de varios sistemas de IR en un único ranking. Keywords declaradas del paper: *fusion, aggregation, ranking*.

**LETOR 3.** Dataset de learning-to-rank de Microsoft Research Asia, con 583.850 pares documento-consulta repartidos en siete conjuntos, usado aquí como banco de pruebas para el meta-learner.

**MAP (Mean Average Precision).** Métrica reportada en las tres tablas del paper.

## Evidence and examples

**Tabla 1 — Piloto: efecto de `k` sobre MAP.** Fusión RRF de 30 configuraciones de Wumpus Search sobre los tópicos 351–400 de TREC. (Reconstruida de la extracción del PDF, donde la tabla quedó desarmada en columnas verticales.)

| `k` | 0 | 10 | 20 | 30 | 40 | 50 | **60** | 70 | 80 | 90 | 100 | 500 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MAP | .2072 | .2123 | .2134 | .2139 | .2138 | .2144 | **.2145** | .2146 | .2147 | .2145 | .2142 | .2098 |

Comparación en la misma corrida: mejor sistema individual .2039 · Condorcet .2016 · CombMNZ .2074. Los autores señalan que se vieron resultados similares aplicando los mismos sistemas a otras tres colecciones de prueba.

**Lectura para la clase:** el máximo de la tabla está en `k = 80` (.2147), no en `k = 60` (.2145). La diferencia es de 0.0002. Eso confirma literalmente lo que dice el texto: la elección no es crítica.

**Tabla 2 — TREC: fusión de corridas efectivamente enviadas por participantes.** MAP para las tareas ad hoc de TREC 3, TREC 5 y TREC 9, más el track Robust de TREC 2004. (Reconstruida; los valores del PDF quedaron en columnas verticales y el orden de columnas se infiere del encabezado `RRF / Best individual / Condorcet / CombMNZ` y del texto.)

| Colección | RRF | Mejor individual | Condorcet | CombMNZ |
|---|---|---|---|---|
| TREC Robust | .3686 | .3586 | .3575 | .3652 |
| TREC 3 | .4350 | .4226 | .4381 | .4256 |
| TREC 5 | .3394 | .3165 | .3237 | .3213 |
| TREC 9 | .2830 | .3519 (.2801) | .2671 | .2750 |

Notas de los autores sobre esta tabla: el MAP de RRF supera al de Condorcet Fuse **en todos los casos**, y al de CombMNZ **en todos menos uno**. RRF también supera al mejor ranking individual en cada experimento **con la excepción de TREC 9**, donde el mejor ranking se obtuvo con un humano en el loop; contra el siguiente mejor ranking, que era automático, RRF gana (de ahí el `.2801` entre paréntesis). Diferencia importante respecto del piloto: acá los rankings individuales no son 30 configuraciones del mismo motor sino las corridas reales enviadas por participantes distintos de TREC.

**Tabla 3 — LETOR 3: RRF como meta-learner sobre 583.850 pares documento-consulta.** MAP de cada método, más la diferencia contra RRF con intervalos de confianza del 95% y p-valor.

| Método | MAP (IC 95%) | MAP_RRF − MAP_método (IC 95%) | p |
|---|---|---|---|
| **RRF** | 0.6051 (0.58 – 0.63) | — | — |
| Condorcet | 0.5917 (0.56 – 0.62) | 0.0134 (0.00 – 0.02) | .004 |
| CombMNZ | 0.6107 (0.58 – 0.64) | −0.0056 (−0.01 – 0) | .2 |
| ListNet | 0.5846 (0.56 – 0.61) | 0.0205 (0.01 – 0.03) | .001 |
| LGD | 0.5837 (0.56 – 0.61) | 0.0214 (0.01 – 0.04) | .003 |
| AdaRank-MAP | 0.5778 (0.55 – 0.61) | 0.0273 (0.01 – 0.04) | .000 |
| RankSVM | 0.5737 (0.55 – 0.60) | 0.0314 (0.02 – 0.04) | .000 |
| RankBoost | 0.5622 (0.53 – 0.59) | 0.0429 (0.03 – 0.06) | .000 |

Lectura de los autores: RRF supera a todos los rankings individuales (p < .003), al mejor por un margen de 0.02 (4%). Condorcet es inferior a RRF (p ≈ .004) aunque aparentemente supera a los rankings individuales (p ≈ .2). **CombMNZ le gana a RRF por un margen pequeño y no significativo (p ≈ .2)** — es el único resultado del paper en que RRF no queda primero. Ninguna de las diferencias medidas entre los sistemas baseline es significativa.

**Contexto adicional:** los autores señalan que los MAP de LETOR 3 se acercan al 65% que se considera alcanzable con relevancia adjudicada por humanos (Voorhees & Harman, 2005).

## Inconsistencies / open questions

- **`k = 60` es empírico y explícitamente no crítico.** Si el deck lo presenta como "el default estándar" sin más, la fuente permite decir algo mucho mejor: es el valor que quedó fijado en un experimento piloto de 2009 sobre tópicos TREC 351–400, que el propio paper reporta como "near-optimal, but ... not critical", y cuyo único rol declarado es "mitigate the impact of high rankings by outlier systems". La tabla 1 muestra que cualquier `k` entre 10 y 100 rinde prácticamente igual, y que el máximo de esa corrida estuvo en `k = 80`.
- **CombMNZ le gana a RRF en LETOR 3.** El paper no lo esconde, pero es el único resultado adverso y suele omitirse en las citas de segunda mano. Si la clase dice "RRF gana siempre", es una simplificación que esta fuente no sostiene: gana en 7 de 8 comparaciones de TREC y pierde (no significativamente) contra CombMNZ en LETOR 3.
- **El paper no evalúa RRF sobre búsqueda híbrida léxica + vectorial.** Todo el trabajo es sobre fusión de rankings de sistemas de IR clásicos (Wumpus Search, corridas de TREC, baselines de learning-to-rank de LETOR). El uso moderno de RRF para fusionar BM25 con búsqueda por embeddings es una extrapolación posterior, razonable por la propiedad de independencia de scores, pero no algo que este paper haya medido.
- **El paper no da guía sobre cuántos rankings fusionar ni sobre profundidad de corte.** Los experimentos usan 30 configuraciones (piloto) o las corridas disponibles de TREC. En un pipeline de RAG con dos retrievers, el régimen es muy distinto y la ganancia de 4-5% no está validada ahí.
- **Extracción del PDF con pérdidas estructurales.** Las tres tablas quedaron desarmadas: los valores aparecen como columnas verticales de números sin encabezados alineados. Las tablas de este registro fueron reconstruidas cruzando los valores con los encabezados y con el texto de la discusión; el orden de columnas de la Tabla 2 se infiere del encabezado `Método RRF Best individual Condorcet CombMNZ` y de las afirmaciones verificables del texto (RRF > Condorcet en todos los casos; el `.3519 (.2801)` de TREC 9 corresponde al mejor individual con humano en el loop). **Antes de poner cualquiera de estos números en una slide, conviene verificar contra `research/web/rrf-cormack-2009/original.pdf`.** La fórmula de RRF y la justificación de `k = 60` sí están en prosa continua y son fiables.
- **La fórmula quedó partida en la extracción** (`RRFscore(d ∈ D) = X` / `r∈R` / `1` / `k + r(d)`) porque el sumatorio `Σ` se extrajo como `X`. La reconstrucción de este registro es inequívoca a partir del texto circundante.

## Images / diagrams

Ninguna. El PDF de 2 páginas no contiene figuras: `pdfimages` sólo detectó 26 stencils de 1×1 píxel (líneas de tabla, 88 bytes cada uno), que no son imágenes en ningún sentido útil. La carpeta compañera `research/corpus/rrf-cormack-2009.web/images/` existe y está vacía. La captura web tampoco trajo assets (`assets: []` en `metadata.yaml`).

## Raw / preserved excerpts

**Abstract (verbatim, inglés):**

> Reciprocal Rank Fusion (RRF), a simple method for combining the document rankings from multiple IR systems, consistently yields better results than any individual system, and better results than the standard method Condorcet Fuse. This result is demonstrated by using RRF to combine the results of several TREC experiments, and to build a meta-learner that ranks the LETOR 3 dataset better than any previously reported method.

> Categories and Subject Descriptors: H.3.3 [Information Search and Retrieval]: retrieval models
> General Terms: Experimentation, Measurement
> Keywords: fusion, aggregation, ranking

**Sección 1, apertura — RRF nació como baseline (verbatim):**

> While supervised learning-to-rank methods have garnered much attention of late, unsupervised methods are attractive because they require no training examples. In the search for such a method we came up with Reciprocal Rank Fusion (RRF) to serve as a baseline. We found that RRF, when used to combine the results of IR methods (including learning to rank), almost invariably improved on the best of the combined results. We also found that RRF consistently equaled or bettered other methods we tried, including established metaranking standards Condorcet Fuse and CombMNZ (cf. [4]).

**Sección 1, la fórmula, el origen de `k = 60` y su justificación (verbatim — el pasaje clave):**

> RRF simply sorts the documents according to a naive scoring formula. Given a set D of documents to be ranked and a set of rankings R, each a permutation on 1..|D|, we compute
>
>     RRFscore(d ∈ D) = Σ_{r∈R} 1 / (k + r(d)) ,
>
> where k = 60 was fixed during a pilot investigation and not altered during subsequent validation. Our intuition in choosing this formula derived from fact that while highly-ranked documents are more important, the importance of lower-ranked documents does not vanish as it would were, say, an exponential function used. The constant k mitigates the impact of high rankings by outlier systems.

**Sección 1, los pilotos y la no-criticidad de `k` (verbatim):**

> We conducted four pilot experiments, each combining the results of 30 configurations of Wumpus Search applied to four different TREC collections. The results of the first, shown in table 1, indicated that k = 60 was near-optimal, but that the choice was not critical. The results also showed, somewhat unexpectedly, that RRF bested competing approaches, as well as more sophisticated learning methods whose investigation was the original impetus for our work.

**Sección 1, experimentos con corridas de TREC (verbatim):**

> We repeated our experiment with four sets of submissions to TREC tasks; the particular sets were selected because they have been used in previous metaranking evaluation. It is worthy of note that, while our pilot runs used exactly the same set of Wumpus configurations to generate the individual rankings on different datasets, the individual rankings in these experiments were exactly those submitted by TREC participants. Table 2 shows the RRF result, as well as the best individual, Condorcet and CombMNZ results. The MAP score for RRF exceeds that of Condorcet Fuse in all cases, and CombMNZ in all but one. RRF also outperforms the best ranking in each experiment, with the exception of TREC 9, where the best ranking was derived using a human-in-the-loop. RRF outperforms the next-best ranking, which was automated.

**Sección 1, significancia estadística (verbatim):**

> The pilot and TREC experiments indicate that RRF outperforms Condorcet, CombMNZ and the best system by 4% to 5% on average. We use a simple sign test to establish significance. Discounting the first pilot run, RRF outperformed Condorcet all 7 times (p ≈ 0.008), outperformed CombMNZ 6 of 7 times (p ≈ .04), and outperformed the best individual result either 6 or 7 times (0.008 ≤ p ≤ 0.04), depending on whether or not the manual result is considered. Thus all measured differences are significant.

**Sección 1, resultado sobre LETOR 3 (verbatim):**

> Our final experiment used the sample learning results supplied with the LETOR 3 dataset, as well as a logistic gradient descent method (LGD) which we are developing. For the purpose of analysis, we combined the seven sets of document-query pairs into one and computed an overall MAP score. We also computed the difference between RRF and individual MAP scores, 95% confidence intervals, and p-value (likelihood under the null hypothesis that the difference is 0). Table 3 shows these results. RRF betters all individual rankings (p < .003), the best by a margin of 0.02 (4%); Condorcet is inferior to RRF (p ≈ .004) while apparently bettering the individual rankings (p ≈ .2). CombMNZ edges RRF by a small margin (p ≈ .2). None of the measured differences among the baseline systems is significant.

**Sección 2, Discusión — completa (verbatim):**

> For brevity, we report MAP as the measure of system performance. P@k, R-precision, and NDCG yield comparable results.
>
> RRF is simpler and more effective than Condorcet Fuse, while sharing the valuable property that it combines ranks without regard to the arbitrary scores returned by particular ranking methods [4]. RRF requires no special voting algorithm or global information; ranks may be computed and summed one system at a time, avoiding the necessity of keeping all rankings in memory. We conjecture that RRF outperforms Condorcet because it is better able to harness diversity within individual rankings. One or two systems that rank a document highly can substantially improve its rank relative to the more popular documents. With Condorcet, a simple majority of weak preferences may overrule substantially stronger ones.
>
> CombMNZ multiplies the sum of the uncalibrated scores of individual system by the sum of a binary quantization of each rank. It is perhaps not surprising that its results have higher variance, ranging from insubstantially better than RRF to substantially worse than Condorcet. We conjecture that this effect is due to the fact that, by happenstance, some scores are more amenable than others.
>
> To our knowledge, no reported result matches or exceeds the performance of the meta-learner formed by applying fusion to the LETOR baseline rank learning methods. So the meta-learner constitutes the best known method, and the result raises the lower bound of what is known to be learnable from the dataset. This latter question is a matter of some interest, as the MAP scores for LETOR 3 approach the 65% considered achievable with human-adjudicated relevance [5].

**Definiciones de los métodos competidores (verbatim):**

> Condorcet Fuse combines rankings by sorting the documents according to the pairwise relation r(d1) < r(d2), which is determined for each (d1, d2) by majority vote among the input rankings. CombMNZ requires for each r a corresponding scoring function s_r : D → R and a cutoff rank c which all contribute to the CombMNZ score:
>
>     CMNZscore(d ∈ D) = |{r ∈ R | r(d) ≤ c}| · Σ_{ {r|r(d)≤c} } s_r(d) .

**Referencias del paper (verbatim):**

> [1] Cao, Z., Qin, T., Liu, T.-Y., Tsai, M.-F., and Li, H. Learning to rank: from pairwise approach to listwise approach. In ICML '07 (2007).
> [2] Freund, Y., Iyer, R., Schapire, R. E., and Singer, Y. An efficient boosting algorithm for combining preferences. JMLR 4 (2003).
> [3] Joachims, T. Optimizing search engines using clickthrough data. In KDD '02 (2002).
> [4] Montague, M., and Aslam, J. A. Condorcet fusion for improved retrieval. In CIKM (2002).
> [5] Voorhees, E. M., and Harman, D. K., Eds. TREC - Experiment and Evaluation in IR. MIT Press, 2005.
> [6] Xu, J., and Li, H. Adarank: a boosting algorithm for information retrieval. In SIGIR '07 (2007).
