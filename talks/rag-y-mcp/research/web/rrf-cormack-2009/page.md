# Rrf Cormack 2009

_Extraído del PDF original con pdfminer._

Reciprocal Rank Fusion outperforms Condorcet and
individual Rank Learning Methods

G. V. Cormack
University of Waterloo
Waterloo, Ontario, Canada

C. L. A. Clarke
University of Waterloo
Waterloo, Ontario, Canada

Stefan B ¨uttcher
Google
Redmond, WA, USA

ABSTRACT
Reciprocal Rank Fusion (RRF), a simple method for com-
bining the document rankings from multiple IR systems,
consistently yields better results than any individual sys-
tem, and better results than the standard method Condorcet
Fuse. This result is demonstrated by using RRF to combine
the results of several TREC experiments, and to build a
meta-learner that ranks the LETOR 3 dataset better than
any previously reported method.

Categories and Subject Descriptors: H.3.3 [Informa-
tion Search and Retrieval]:retrieval models
General Terms: Experimentation, Measurement
Keywords: fusion, aggregation, ranking

1. RECIPROCAL RANK FUSION

While supervised learning-to-rank methods have garnered
much attention of late, unsupervised methods are attractive
because they require no training examples.
In the search
for such a method we came up with Reciprocal Rank Fu-
sion (RRF) to serve as a baseline. We found that RRF,
when used to combine the results of IR methods (including
learning to rank), almost invariably improved on the best
of the combined results. We also found that RRF consis-
tently equaled or bettered other methods we tried, includ-
ing established metaranking standards Condorcet Fuse and
CombMNZ (cf. [4]).

RRF simply sorts the documents according to a naive
scoring formula. Given a set D of documents to be ranked
and a set of rankings R, each a permutation on 1..|D|, we
compute

RRFscore(d ∈ D) = X
r∈R

1
k + r(d)

,

where k = 60 was ﬁxed during a pilot investigation and
not altered during subsequent validation. Our intuition in
choosing this formula derived from fact that while highly-
ranked documents are more important, the importance of

Permission to make digital or hard copies of all or part of this work for
personal or classroom use is granted without fee provided that copies are
not made or distributed for proﬁt or commercial advantage and that copies
bear this notice and the full citation on the ﬁrst page. To copy otherwise, to
republish, to post on servers or to redistribute to lists, requires prior speciﬁc
permission and/or a fee.
SIGIR’09, July 19–23, 2009, Boston, Massachusetts, USA.
Copyright 2009 ACM 978-1-60558-483-6/09/07 ...$5.00.

lower-ranked documents does not vanish as it would were,
say, an exponential function used. The constant k mitigates
the impact of high rankings by outlier systems.

Condorcet Fuse combines rankings by sorting the doc-
uments according to the pairwise relation r(d1) < r(d2),
which is determined for each (d1, d2) by majority vote among
the input rankings. CombMNZ requires for each r a corre-
sponding scoring function sr : D → R and a cutoﬀ rank c
which all contribute to the CombMNZ score:

CMNZscore(d ∈ D) = |{r ∈ R|r(d) ≤ c}| · X

sr(d) .

{r|r(d)≤c}

We conducted four pilot experiments, each combining the
results of 30 conﬁgurations of Wumpus Search applied to
four diﬀerent TREC collections. The results of the ﬁrst,
shown in table 1, indicated that k = 60 was near-optimal,
but that the choice was not critical. The results also showed,
somewhat unexpectedly, that RRF bested competing ap-
proaches, as well as more sophisticated learning methods
whose investigation was the original impetus for our work.
We repeated our experiment with four sets of submissions
to TREC tasks; the particular sets were selected because
they have been used in previous metaranking evaluation.
It is worthy of note that, while our pilot runs used ex-
actly the same set of Wumpus conﬁgurations to generate
the individual rankings on diﬀerent datasets, the individual
rankings in these experiments were exactly those submitted
by TREC participants. Table 2 shows the RRF result, as
well as the best individual, Condorcet and CombMNZ re-
sults. The MAP score for RRF exceeds that of Condorcet
Fuse in all cases, and CombMNZ in all but one. RRF also
outperforms the best ranking in each experiment, with the
exception of TREC 9, where the best ranking was derived
using a human-in-the-loop. RRF outperforms the next-best
ranking, which was automated.

The pilot and TREC experiments indicate that RRF out-
performs Condorcet, CombMNZ and the best system by 4%
to 5% on average. We use a simple sign test to establish sig-
niﬁcance. Discounting the ﬁrst pilot run, RRF outperformed
Condorcet all 7 times (p ≈ 0.008), outperformed CombMNZ
6 of 7 times (p ≈ .04), and outperformed the best individual
result either 6 or 7 times (0.008 ≤ p ≤ 0.04), depending on
whether or not the manual result is considered. Thus all
measured diﬀerences are signiﬁcant.

Our ﬁnal experiment used the sample learning results
supplied with the LETOR 31 dataset, as well as a logis-

1research.microsoft.com/en-us/um/beijing/projects/letor

k
M AP

0
.2072

10
.2123

20
.2134

30
.2139

40
.2138

50
.2144

60
.2145

70
.2146

80
.2147

90
.2145

100
.2142

500
.2098

method Best individual Condorcet CombMNZ
M AP

.2039

.2016

.2074

Table 1: Pilot results. Eﬀect of k on MAP for RR Fusion of 30 model system results on TREC topics 351-400.
Results of best model system and competing fusion methods shown for comparison. Similar results were seen
for the same systems applied to three other test collections.

Collection
TREC Robust
TREC 3
TREC 5
TREC 9

Method
RRF Best individual Condorcet CombMNZ
.3686
.4350
.3394
.2830

.3586
.4226
.3165
.3519 (.2801)

.3575
.4381
.3237
.2671

.3652
.4256
.3213
.2750

Table 2: MAP scores for fusion of submitted runs for TREC 3, TREC 5 and TREC 9 ad hoc tasks, plus
TREC 2004 Robust track.

method
RRF
Condorcet
CombMNZ
ListNet [1]
LGD
AdaRank-MAP [6]
RankSVM [3]
RankBoost [2]

M APmethod
0.6051 (0.58 - 0.63)
0.5917 (0.56 - 0.62)
0.6107 (0.58 - 0.64)
0.5846 (0.56 - 0.61)
0.5837 (0.56 - 0.61)
0.5778 (0.55 - 0.61)
0.5737 (0.55 - 0.60)
0.5622 (0.53 - 0.59)

M APRRF − M APmethod
–
0.0134 (0.00 - 0.02)
-0.0056 (-0.01 - 0)
0.0205 (0.01 - 0.03)
0.0214 (0.01 - 0.04)
0.0273 (0.01 - 0.04)
0.0314 (0.02 - 0.04)
0.0429 (0.03 - 0.06)

p
–
.004
.2
.001
.003
.000
.000
.000

Table 3: Individual rankings and fusion for 583,850 document-query pairs in LETOR 3 corpus. MAP score
for each method, plus diﬀerence between fusion and individual MAP score with 95% conﬁdence limits.

tic gradient descent method (LGD) which we are develop-
ing. For the purpose of analysis, we combined the seven sets
of document-query pairs into one and computed an overall
MAP score. We also computed the diﬀerence between RRF
and individual MAP scores, 95% conﬁdence intervals, and
p-value (likelihood under the null hypothesis that the dif-
ference is 0). Table 3 shows these results. RRF betters all
individual rankings (p < .003), the best by a margin of 0.02
(4%); Condorcet is inferior to RRF (p ≈ .004) while appar-
ently bettering the individual rankings (p ≈ .2). CombMNZ
edges RRF by a small margin (p ≈ .2). None of the mea-
sured diﬀerences among the baseline systems is signiﬁcant.

2. DISCUSSION

For brevity, we report MAP as the measure of system per-
formance. P @k, R-precision, and N DCG yield comparable
results.

RRF is simpler and more eﬀective than Condorcet Fuse,
while sharing the valuable property that it combines ranks
without regard to the arbitrary scores returned by partic-
ular ranking methods [4]. RRF requires no special voting
algorithm or global information; ranks may be computed
and summed one system at a time, avoiding the necessity of
keeping all rankings in memory. We conjecture that RRF
outperforms Condorcet because it is better able to harness
diversity within individual rankings. One or two systems
that rank a document highly can substantially improve its
rank relative to the more popular documents. With Con-
dorcet, a simple majority of weak preferences may overrule
substantially stronger ones.

CombMNZ multiplies the sum of the uncalibrated scores

of individual system by the sum of a binary quantization of
each rank. It is perhaps not surprising that its results have
higher variance, ranging from insubstantially better than
RRF to substantially worse than Condorcet. We conjecture
that this eﬀect is due to the fact that, by happenstance,
some scores are more amenable than others.

To our knowledge, no reported result matches or exceeds
the performance of the meta-learner formed by applying fu-
sion to the LETOR baseline rank learning methods. So the
meta-learner constitutes the best known method, and the re-
sult raises the lower bound of what is known to be learnable
from the dataset. This latter question is a matter of some
interest, as the MAP scores for LETOR 3 approach the 65%
considered achievable with human-adjudicated relevance [5].

References
[1] Cao, Z., Qin, T., Liu, T.-Y., Tsai, M.-F., and Li,

H. Learning to rank: from pairwise approach to listwise
approach. In ICML ’07 (2007).

[2] Freund, Y., Iyer, R., Schapire, R. E., and
Singer, Y. An eﬃcient boosting algorithm for
combining preferences. JMLR 4 (2003).

[3] Joachims, T. Optimizing search engines using

clickthrough data. In KDD ’02 (2002).

[4] Montague, M., and Aslam, J. A. Condorcet fusion

for improved retrieval. In CIKM (2002).

[5] Voorhees, E. M., and Harman, D. K., Eds. TREC -
Experiment and Evaluation in IR. MIT Press, 2005.
[6] Xu, J., and Li, H. Adarank: a boosting algorithm for

information retrieval. In SIGIR ’07 (2007).

