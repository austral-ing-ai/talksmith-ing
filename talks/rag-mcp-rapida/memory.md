# memory.md — rag-mcp-rapida

**Current step:** 7 — Render complete (html-strict). Step 8 (Learnings) pendiente.
**Awaiting:** nada. Deck listo para dictar: `output/html/index.html` (cover + 31 laminas, 16 diagramas PNG embebidos). Falta decidir si se pushea (Marco no lo pidio todavia).
**Mode:** B (Agent Draft) — el borrador se deriva de `talks/rag-y-mcp/` (deck grande de Paulo), que hace de corpus.
**Topic:** Presentación rápida sobre RAG y MCP: formas de RAG, hiperparámetros del pipeline, evaluación y seguridad, y el bloque de MCP del deck grande.
**Folder:** talks/rag-mcp-rapida/
**Started:** 2026-09-16

---

## Talk briefing

Presentación rápida sobre RAG y MCP. Temario:

- Formas de RAG: similitud de embeddings a la query, índice invertido, tool-using (herramientas de agentes que llaman a documentos). La búsqueda híbrida se menciona como posibilidad y cómo funciona a muy grandes rasgos. Sin menores (query rewriting, caso sin retrieval).
- "Hiperparámetros" de RAG: top-k, similitud mínima, chunking y metadatos; el reranking va acá, como parte de los hiperparámetros.
- Evaluación y seguridad.
- Todo lo que ya está de MCP en la presentación grande de RAG (`talks/rag-y-mcp/`).

Fuente: `talks/rag-y-mcp/draft.md` (AIG4B-Clase-5 importada por Paulo) y su corpus (`research/corpus/`: Lewis 2020, RRF Cormack 2009, tool-space interference de MSR, aitutorial.dev). Collect y Corpus se saltean: la fuente ya está estructurada.

## Parte práctica (anunciada por Marco el 2026-09-16, fuera de esta charla)

Tres ejercicios encadenados, a escribir como misión:

1. Un RAG vectorial evaluado con Context Relevance sobre un dataset sintético simple. Los alumnos eligen el encoder y tunean los hiperparámetros (top-k, umbral, chunking, etc.) para maximizar el benchmark.
2. Un agente que usa ese RAG vectorial como fuente y además hace RAG con tool-use contra una fuente externa (información que no está en la base vectorial). Se evalúa con Context Relevance, Answer Faithfulness y Answer Relevance. Modelo de OpenRouter fijado por la cátedra.
3. Convertir las herramientas del agente en un servidor MCP y probarlo con un modelo *mejor*: al cambiar el agente, las herramientas se reutilizan.

---

## 2026-09-16 — Step 1 (Frame)
- Status: complete
- Asks log:
  - "¿Falta algo importante en las formas de RAG?" → híbrida solo como mención a grandes rasgos; reranking dentro de hiperparámetros; descartar los menores.
  - carpeta: rag-mcp-rapida / rag-y-mcp-express / intro-rag-mcp → "rag-mcp-rapida".
- What was decided: charla derivada del deck grande, temario de cuatro bloques, modo B.

## 2026-09-16 — Steps 4-5 (Draft + Review)
- Status: complete
- 25 laminas de contenido en 6 secciones (5 + 4 + 2 + 8 + 5 + 1), 16 diagramas ASCII. Frontmatter: "Clase 7: MCP y herramientas, con repaso de RAG", 90 min, presentadores Veiga, Righetti, Sorondo.
- Revision lamina por lamina con /desrobotizar (1.1 a 3.2); agregados: HNSW explicado en notas (capas = mismos vectores, menos, nivel aleatorio; grafo, no arbol), "Metadatos como texto buscable" (contextual retrieval, parent-document / summary embeddings) en 2.3.
- Marco revirtio mi reescritura del pie del diagrama 1.4 ("mas slop"): cuando el original es concreto, no tocar.
- Sin revisar a fondo: 1.2 (rotulos "El orden lo decide un score" / "Cuándo conviene:") y las laminas 4.x y 5.x (heredadas casi textuales del deck grande).

## 2026-09-16 — Step 6 (Polish)
- Status: complete
- 16 diagramas renderizados a SVG/PNG con critica ciega: 13 limpios a la primera, 3 con una revision (s1-2-1, s2-2-1, s2-4-1, s4-5-1). Logs en `images/.critique/`.
- Quirk del harness: los veredictos del diagram-critic llegan al orquestador y no al worker; hubo que reenviarlos a mano via SendMessage a `rag-<block-id>`.
- final.md: stamp-renders → cleanup → strip_feedback → post-fix python (Resolution:/[closed] residuales, .svg→.png).

## 2026-09-16 — Step 7 (Render html-strict)
- Status: complete
- `output/slide-model.json` (31 laminas: 6 section-agenda, content+cards+image, concept-breakdown, content-image, comparison, code-example, icon-list), notas inyectadas por titulo con `inject_notes.py` del scratchpad, freshness stamp, audits degenerate_enum / field_coverage / image_coverage ok. `build_html.py` → `output/html/index.html` (2.3 MB, imagenes embebidas).
- Sin revision visual lamina por lamina (Marco pidio terminar).
