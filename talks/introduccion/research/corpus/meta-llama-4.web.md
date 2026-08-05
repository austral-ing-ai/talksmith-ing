---
source_file: meta-llama-4
source_type: web-capture
ingested_at: 2026-08-05
---

# La colección de modelos Llama 4: Una nueva era de innovación multimodal nativa para Inteligencia Artificial

## Provenance
- Ubicación original: `research/web/meta-llama-4/`
- Formato: captura web (`original.html` 296.317 bytes + `page.md` 12.017 bytes + `assets/`)
- URL: https://about.fb.com/ltam/news/2025/04/la-coleccion-de-modelos-llama-4-el-inicio-de-una-nueva-era-de-innovacion-multimodal-nativa-para-inteligencia-artificial/
- Autor / fuente: **Meta** — sala de prensa oficial (Newsroom), edición Latinoamérica
- Fecha del original: **5 de abril de 2025** (la página muestra "abril 5, 2025abril 5, 2025",
  probablemente fecha de publicación y de última modificación duplicadas por la extracción)
- Capturado el: 2026-08-05T12:20:10Z · HTTP 200
- Categorías declaradas por Meta: IA, Innovación
- **Fuente en español.** Es la traducción latinoamericana del anuncio; el original en inglés y el
  post técnico completo están en `ai.meta.com/blog/llama-4-multimodal-intelligence` y **no fueron
  capturados**.

## Key claims

Síntesis que la propia página destaca al inicio:

- Meta presenta los primeros modelos del conjunto **Llama 4**: **Llama 4 Maverick** y **Llama 4
  Scout**, "que permitirán a las personas crear experiencias multimodales más personalizadas".
- Ambos son **los primeros modelos multimodales nativos de peso abierto** de Meta, con "una longitud
  de soporte de contexto sin precedentes", y **los primeros construidos con arquitectura de mezcla de
  expertos (MoE)**.
- Son sus mejores modelos hasta el momento **gracias a la destilación de Llama 4 Behemoth**, "un
  modelo de 288 mil millones de parámetros activos con 16 expertos", descrito como el más poderoso de
  Meta y "entre los LLMs más inteligentes del mundo".
- **Llama 4 Behemoth supera a GPT-4.5, Claude Sonnet 3.7 y Gemini 2.0 Pro** en diversas pruebas de
  referencia STEM, como **MATH-500 y GPQA Diamond**.
- Behemoth **todavía está en entrenamiento** y no se libera.

Especificaciones de los dos modelos liberados:

| Modelo | Parámetros | Expertos | Requisito de hardware declarado |
|---|---|---|---|
| **Llama 4 Scout** | 17 mil millones | 16 | Cabe en **una sola GPU H100** (con cuantización Int4) |
| **Llama 4 Maverick** | 17 mil millones | 128 | Corre en **un solo host H100** |
| **Llama 4 Behemoth** (no liberado) | 288 mil millones **activos** | 16 | — |

Disponibilidad y distribución:
- Descarga desde el día del anuncio en **llama.com** y **Hugging Face**.
- Disponibles "a través de nuestros socios en los próximos días".
- Meta AI construido con Llama 4 disponible en **WhatsApp, Messenger, Instagram Direct y meta.ai**.

Posicionamiento estratégico:
- Meta reafirma que "el enfoque abierto para la inteligencia artificial impulsa la innovación y es
  bueno para los desarrolladores, bueno para Meta y bueno para el mundo".
- Visión declarada: "los sistemas más inteligentes deben ser capaces de tomar acciones generales,
  conversar naturalmente con los humanos y resolver problemas complejos que no han visto antes".
- Anuncio de **LlamaCon el 29 de abril** (de 2025).

## Definitions and terminology

- **Mezcla de expertos (MoE, Mixture of Experts)**: arquitectura en la que solo un subconjunto de
  parámetros ("expertos") se activa por token. Es la primera vez que Meta la usa en Llama. La página
  la nombra pero **no la explica**.
- **Multimodal nativo**: multimodalidad incorporada desde el entrenamiento, no agregada después. La
  página usa el término sin definirlo.
- **Peso abierto (open weight)**: los pesos se pueden descargar. Nótese que Meta dice "peso abierto",
  no "código abierto" — la distinción importa y la página no la aclara.
- **Destilación**: entrenar modelos más chicos usando uno grande como "maestro". Acá Behemoth es el
  modelo profesor de Scout y Maverick.
- **Parámetros activos**: para Behemoth se declaran "288 mil millones de parámetros activos", que en
  una arquitectura MoE es distinto del total de parámetros. **El total no se declara.**

## Evidence and examples

Lo que la página ofrece como evidencia es escaso y todo auto-reportado:

- **Comparaciones de Behemoth**: supera a **GPT-4.5**, **Claude Sonnet 3.7** y **Gemini 2.0 Pro** en
  pruebas STEM. Benchmarks nombrados: **MATH-500** y **GPQA Diamond**.
  **No se publica ni un solo número.** Ni el puntaje de Behemoth, ni el de los competidores, ni el
  margen.
- **Requisitos de hardware** como evidencia de eficiencia: Scout en una H100 con Int4; Maverick en un
  host H100.
- **Contexto**: "longitud de soporte de contexto sin precedentes" — sin cifra.

## Inconsistencies / open questions

- **Cero números de rendimiento.** El anuncio afirma superioridad sobre tres modelos frontier
  nombrados y no publica una sola cifra. Una diapositiva que diga "Llama 4 Behemoth supera a GPT-4.5"
  estaría citando una afirmación de marketing sin respaldo verificable **en esta fuente**. Los
  números, si existen, están en el blog técnico que no se capturó.
- **Se compara un modelo no liberado.** Todas las comparaciones competitivas son de **Behemoth**, que
  "todavía está en entrenamiento" y no se puede descargar ni verificar. Los modelos que sí se liberan
  (Scout y Maverick) no tienen ninguna comparación en esta página.
- **"Contexto sin precedentes" sin cifra.** Es la afirmación más destacada del anuncio y no está
  cuantificada.
- **Ambigüedad en los parámetros de Behemoth.** "288 mil millones de parámetros activos con 16
  expertos": en MoE, parámetros activos ≠ parámetros totales. El total no se declara, así que no se
  puede comparar con modelos densos.
- **Los competidores citados eran, ya en abril de 2025, generaciones anteriores** en algunos casos.
  Comparar contra Gemini 2.0 Pro y Claude Sonnet 3.7 es una elección de línea base que la página no
  justifica.
- **Fuente de sala de prensa, no técnica.** Es un comunicado. Su función es anunciar, no documentar.
  Para cualquier afirmación técnica hay que ir al blog completo
  (`ai.meta.com/blog/llama-4-multimodal-intelligence`), **no capturado**.
- **Antigüedad.** Abril de 2025, capturado en agosto de 2026: **16 meses**. La página misma muestra
  una nota relacionada de abril de 2026 anunciando **"Muse Spark"**, descrito como *"el primero de una
  nueva serie de modelos de lenguaje a gran escala creados por Meta Superintelligence Labs"*, lo que
  indica que la línea de producto avanzó bastante desde este anuncio. Usar Llama 4 como "lo último de
  Meta" sería incorrecto.
- **Riesgo de doble traducción.** La fuente es una traducción al español del anuncio en inglés.
  Algunas construcciones son literales del inglés ("una longitud de soporte de contexto sin
  precedentes"). Si se cita textualmente en la presentación, conviene indicar que es la versión en
  español de Meta y no una traducción propia.
- Ruido de extracción: el `page.md` incluye un enlace `mailto:` gigantesco con el artículo entero
  percent-encoded en el cuerpo del mail (el botón "compartir por email"), más el banner de cookies.

## Images / diagrams

Una imagen de contenido, pendiente de transcripción.

- `meta-llama-4.web/images/image1.png`
  - Provenance: `research/web/meta-llama-4/assets/`; origen
    `https://about.fb.com/ltam/wp-content/uploads/sites/14/2025/04/image1.png`. Sin texto alt.
    Es la imagen de cabecera del comunicado, ubicada inmediatamente después del título y la fecha,
    antes de la sección "Síntesis". 1.003.188 bytes.
  - <!-- pending: process_images -->

## Raw / preserved excerpts

Síntesis completa, verbatim:

> ## Síntesis
>
> - Compartimos los primeros modelos del conjunto Llama 4, que permitirán a las personas crear experiencias multimodales más personalizadas: Llama 4 Maverick y Llama 4 Scout.
> - Estos modelos son nuestros mejores hasta ahora gracias a la destilación de Llama 4 Behemoth, un modelo de 288 mil millones de parámetros activos con 16 expertos que es nuestro más poderoso hasta ahora y entre los LLMs más inteligentes del mundo. Supera a GPT-4.5, Claude Sonnet 3.7 y Gemini 2.0 Pro en diversas pruebas de referencia STEM. Llama 4 Behemoth todavía está en entrenamiento y nos emociona compartir más detalles sobre él incluso mientras aún está en desarrollo.
> - Descarga los modelos Llama 4 Scout y Llama 4 Maverick desde hoy en [llama.com](https://www.llama.com/) y [Hugging Face](https://huggingface.co/meta-llama). Prueba Meta AI construido con Llama 4 en WhatsApp, Messenger, Instagram Direct y en la [web](http://meta.ai/).

Párrafo de especificaciones, verbatim:

> Estos modelos Llama 4 marcan el comienzo de una nueva era para el ecosistema Llama. Diseñamos dos modelos eficientes en la serie Llama 4: Llama 4 Scout, un modelo de 17 mil millones de parámetros entrenado en 16 expertos y Llama 4 Maverick, un modelo de 17 mil millones de parámetros entrenado en 128 expertos. El primero cabe en una sola GPU H100 (con cuantización Int4) mientras que el segundo corre en un solo host H100. También entrenamos un modelo profesor, Llama 4 Behemoth, que supera a GPT-4.5, Claude Sonnet 3.7 y Gemini 2.0 Pro en pruebas de referencia centrados en STEM, como MATH-500 y GPQA Diamond. Aunque aún no estamos liberando Llama 4 Behemoth, porque aún está en entrenamiento, nos emociona compartir más detalles técnicos sobre nuestro enfoque.

Párrafo de apertura, verbatim:

> A medida que más personas utilizan la inteligencia artificial para mejorar su vida diaria, es importante que los modelos y sistemas líderes estén disponibles con un enfoque abierto para que todos puedan construir el futuro de las experiencias personalizadas. Hoy, nos entusiasma anunciar el conjunto de modelos más avanzado que respalda todo el ecosistema de Llama. Presentamos Llama 4 Scout y Llama 4 Maverick, los primeros modelos multimodales nativos de peso abierto con una longitud de soporte de contexto sin precedentes y nuestros primeros construidos con arquitectura de mezcla de expertos (MoE por sus siglas en inglés). También presentamos Llama 4 Behemoth, uno de los LLMs más inteligentes del mundo y el más poderoso hasta ahora que sirve como maestro para nuestros nuevos modelos.

Postura sobre apertura, verbatim:

> Seguimos creyendo que el enfoque abierto para la inteligencia artificial impulsa la innovación y es bueno para los desarrolladores, bueno para Meta y bueno para el mundo.

Visión de producto, verbatim:

> Este es solo el comienzo para la colección de modelos Llama 4. Creemos que los sistemas más inteligentes deben ser capaces de tomar acciones generales, conversar naturalmente con los humanos y resolver problemas complejos que no han visto antes. Dar superpoderes a Llama en estas áreas conducirá a mejores productos para las personas en nuestras plataformas y más oportunidades para que los desarrolladores innoven en los próximos grandes casos de uso para consumidores y empresas.

Nota relacionada visible en la captura (contexto temporal posterior), verbatim:

> ### [Presentamos Muse Spark: el primer modelo de lenguaje a gran escala diseñado para priorizar a las personas]
>
> Muse Spark es el primero de una nueva serie de modelos de lenguaje a gran escala creados por Meta Superintelligence Labs, y que impulsará una Meta AI más inteligente y rápida. abril 8, 2026mayo 14, 2026
