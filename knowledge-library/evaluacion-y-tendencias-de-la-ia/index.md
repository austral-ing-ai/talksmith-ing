---
topic: "Evaluación y tendencias de la IA (2026): autonomía de agentes, saturación de benchmarks y el debate sobre escalar"
language: Español
sources:
  - talk: cierre-magnifica-humanitas
    date: 2026-11-02
    contributed: Las cifras de ritmo (SWE-bench, Humanity's Last Exam, horizonte temporal de METR) con sus correcciones, la evaluación como cuello de botella, AlphaFold como ejemplo de métrica acordada, el debate escalar contra paradigma nuevo, las tres apuestas más allá del LLM con su financiación corregida y tres escenarios. Fotografía a noviembre de 2026; los números envejecen rápido.
last_updated: 2026-11-02
---

# Evaluación y tendencias de la IA (2026)

**Fotografía a noviembre de 2026.** Las cifras de este tema caducan en meses; antes de reusarlas, verificar si hay una versión más nueva de cada fuente.

La tensión que atraviesa el tema: las capacidades crecen más rápido que nuestra capacidad de medirlas y gobernarlas. El AI Index 2026 lo resume así: «Las capacidades avanzan más rápido que los marcos para gobernarlas, evaluarlas y entenderlas» (paráfrasis de la introducción de HAI; verificado).

## El ritmo, en tres cifras

| Medida | Cifra | Estado |
|---|---|---|
| SWE-bench Verified (resolver issues reales de repositorios) | De 60% a casi 100% en un año | Verificado (AI Index 2026: "near 100%") |
| Humanity's Last Exam, mejor modelo | De 8,8% (AI Index 2025) a **38,3%** (AI Index 2026) | Corregido. El ">50%" del deck original sale solo de IEEE Spectrum (13/4/2026), no del AI Index |
| Horizonte temporal de METR | Se duplica cada **4,3 meses** (tendencia desde 2023) | Verificado |

Fuente: [clase-cierre](../../talks/cierre-magnifica-humanitas/research/corpus/IA_Generativa_Clase_Cierre_v2_Magnifica_Humanitas.pptx.md), slide 6 y §Fact-check.

## Autonomía: el horizonte temporal de METR

METR mide qué tan larga (en horas de trabajo humano) es la tarea de software que un agente completa con 50% de éxito, y cada cuánto se duplica ese largo:

- **7 meses:** tendencia 2019–2024 (196 días sobre 2019–2025 en la versión 1.1).
- **4,3 meses:** tendencia desde 2023 (130,8 días).

La duplicación se aceleró. Pero METR advierte que sus mediciones por encima de **16 horas no son confiables**: el instrumento llega a su techo (Time Horizon 1.1, ene. 2026; página de horizontes temporales actualizada en sep. 2026; Kwa et al., 2025). Más autonomía es más tiempo sin supervisión, y todo lo de [seguridad-de-llms-y-agentes](../seguridad-de-llms-y-agentes/index.md) se amplifica (slide 43).

## Evaluar es el nuevo cuello de botella

| Problema | Qué significa |
|---|---|
| Saturación | Los benchmarks se agotan en meses (SWE-bench Verified) |
| Techo del instrumento | Las mediciones de autonomía dejan de ser confiables por encima de 16 horas |
| Validez externa | Un buen puntaje no garantiza buen desempeño en un contexto real de uso |

La lección de T. Bedrax-Weiss (Google DeepMind): AlphaFold funcionó porque había una métrica acordada por la comunidad (CASP). Sin métrica no se sabe si se avanza (slide 44).

## IA para la ciencia: AlphaFold

Antes, determinar la estructura 3D de una proteína llevaba meses o años de trabajo experimental. Después, hay una predicción computacional precisa disponible para cualquier investigador. Cifras de DeepMind (*AlphaFold: five years of impact*, nov. 2025): **3,3 millones de usuarios en 190 países** (verificado) y **más de 35.000 citas**. El "47.000 citas" del deck original no tiene respaldo en la fuente oficial; puede venir de la conferencia de Bedrax-Weiss, y solo debería usarse citándola a ella. El costo experimental de "cientos de miles de dólares por estructura" se quitó: la mejor fuente encontrada da unos US$ 120.000 y no tiene fecha (no verificado).

El criterio de DeepMind: buscar saltos de 10x a 100x en problemas con una métrica que la comunidad ya acepta. Otras áreas: materiales (GNoME), fusión, matemáticas (AlphaProof), clima (GraphCast) y agentes científicos (slide 46).

## El debate: ¿alcanza con escalar?

| Escalar sigue funcionando | Falta algo fundamental |
|---|---|
| No hay evidencia firme de que el escalado se frene | LeCun: escalar LLMs no lleva a una IA de nivel humano (TechCrunch, 2024) |
| El RL con recompensas verificables explica buena parte del avance en razonamiento y código | Sutskever: volvimos a la era de la investigación, ahora con grandes computadoras (Dwarkesh, 2025) |
| Los LLMs podrían cruzar un umbral general antes que otro paradigma | Hassabis: ~50% de chances de que falten una o dos grandes ideas |

Las tres citas de la derecha están verificadas. La columna izquierda se atribuye a C. Ford (Transformer, 2026), y el argumento del RL con recompensas verificables **no se pudo verificar**: no se encontró el artículo (slide 47).

## Tres apuestas más allá del LLM

| Apuesta | Idea | Quién y cuánto |
|---|---|---|
| Modelos del mundo | Aprender cómo funciona el mundo físico, no solo el lenguaje | LeCun (AMI Labs, JEPA): US$ 1.030M. Fei-Fei Li (World Labs): US$ 1.000M |
| Experiencia (RL) | Refuerzo puro, sin imitar datos humanos; linaje de AlphaZero y de Sutton | D. Silver (Ineffable Intelligence): US$ 1.100M |
| Neurosimbólica | LLM más razonamiento simbólico estructurado | Y. Cao (Unreasonable Labs): US$ 13,5M, para generar hipótesis científicas |

**Corrección del fact-check:** el deck original decía "más de US$ 3.000 millones en rondas semilla". World Labs no fue una ronda semilla: solo semilla suman ≈ US$ 2.140M, y con World Labs ≈ US$ 3.140M en rondas de inversión. El marco teórico de la segunda apuesta es Silver y Sutton, "The Era of Experience" (2025; verificado). Los modelos del mundo retoman la idea de generar para entender, como las GANs y la difusión (slide 48).

## Tres escenarios

- **Continuidad:** los LLMs, con innovaciones incrementales, siguen marcando la frontera.
- **Ruptura:** un nuevo paradigma (modelos del mundo, RL) desplaza al LLM.
- **Convergencia:** sistemas híbridos, o LLMs que ayudan a investigar a su propio sucesor (Anthropic, "When AI Builds Itself", 2026; verificado).

En los tres, las preguntas de seguridad y ética siguen abiertas (slide 49).

## Un mapa: consolidado, promesa, pregunta abierta

| Consolidado | Promesa | Pregunta abierta |
|---|---|---|
| Razonamiento con más cómputo en inferencia | Autonomía de horas a días | Evaluar más allá de los benchmarks |
| MCP como estándar agente–herramienta | Coordinación multiagente entre organizaciones | Alinear lo que no podemos supervisar |
| Agentes en flujos acotados | Modelos abiertos para despliegue local | Gobernar sistemas que actúan |
| La inyección de prompts como riesgo nº 1 | IA como acelerador de la ciencia | ¿Escalar o cambiar de paradigma? |

Síntesis de la cátedra a noviembre de 2026 (slide 51).

## References

- [clase-cierre](../../talks/cierre-magnifica-humanitas/research/corpus/IA_Generativa_Clase_Cierre_v2_Magnifica_Humanitas.pptx.md): slides 6 y 43–51, gráfico nativo de la slide 43 en §Evidence and examples, §Fact-check.
- Stanford HAI, AI Index 2026: https://hai.stanford.edu/ai-index/2026-ai-index-report · técnico: https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance · 12 conclusiones: https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report
- IEEE Spectrum (13/4/2026): https://spectrum.ieee.org/state-of-ai-index-2026
- METR, Time Horizon 1.1: https://metr.org/blog/2026-1-29-time-horizon-1-1/ · https://metr.org/time-horizons/
- Google DeepMind, AlphaFold: five years of impact: https://deepmind.google/blog/alphafold-five-years-of-impact/
- Silver y Sutton, "The Era of Experience": https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf
- Anthropic, "When AI builds itself": https://www.anthropic.com/institute/recursive-self-improvement
- Sutskever (Dwarkesh): https://www.dwarkesh.com/p/ilya-sutskever-2
