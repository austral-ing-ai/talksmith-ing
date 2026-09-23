# memory.md — transformers-a-fondo

**Current step:** 7 — Render html-strict hecho (Polish completo)
**Awaiting:** revision del presentador sobre el deck renderizado; pendientes: ampliar entrenamiento, quiz final, post-LN vs pre-LN en el ejercicio a mano.
**Mode:** B (Agent Draft)
**Topic:** El transformer por dentro: self-attention con numeros, multi-head, el bloque completo, encoder/decoder/decoder-only y las arquitecturas derivadas; variantes modernas solo cualitativas.
**Folder:** talks/transformers-a-fondo/
**Started:** 2026-09-22

---

## Talk briefing

Clase 8 (miercoles 2026-09-23, 90 min; presentadores Veiga, Righetti, Sorondo). Continua `talks/palabra-al-transformer/` (dictada el 16/9), que se frena a proposito en la intuicion de la atencion: sus notas dicen que self-attention, multi-head, positional encoding, scaled dot-product y layer norm "estan en el paper". Esta clase es ese hueco.

Temario acordado con Marco (2026-09-22):

1. Repaso en dos laminas: el ciclo token a token y "cada token mira a todos".
2. Self-attention con numeros reales chicos: Q, K, V como proyecciones; scaled dot-product paso a paso con 4 tokens y d=4; por que se divide por sqrt(d); softmax; mezcla ponderada de V; mascara causal.
3. Multi-head y el bloque completo: cabezas como preguntas en paralelo, concatenacion y proyeccion; FFN por posicion (donde vive la mayoria de los parametros); residuales y layer norm (pre-LN vs post-LN); positional encoding sinusoidal; cuenta de parametros de un bloque.
4. Encoder, decoder y decoder-only: las dos columnas del paper y la cross-attention; GPT-2 como decoder-only; BERT como encoder-only (el que usa la practica para RAG); T5/encoder-decoder. Arquitecturas y modelos derivados: ViT (imagenes), Sentence-BERT (embeddings de oraciones), y el mapa de familias.
5. Variantes modernas SOLO cualitativas, cada una en una lamina o menos: costo cuadratico, KV cache, GQA/MQA, FlashAttention, RoPE, MLA, MoE. Se van a fondo en la clase 9 "Transformers Avanzados", que apunta a llegar a las arquitecturas del articulo "22580: From GPT2 to Kimi3" (linear attention, DeltaNet, Gated DeltaNet, KDA/Kimi Linear, Kimi K3: MLA, latent MoE, AttnRes, SiTU). Fuente guardada en `research/raw/gpt2-to-kimi3-waterloo-intern.md`.
6. Entrenamiento a vuelo de pajaro: next-token, cross-entropy sobre |V|, scaling laws en una lamina.

Decisiones de Marco: (1) matrices con numeros reales chicos en el bloque 2, notacion en el resto; (2) hay practica (ver abajo); (3) variantes modernas cualitativas, a fondo en la clase 9.

## Practica asociada (mision a escribir, fuera de esta charla)

"RAG, MCP y Transformers", en tres partes mas ejercicios de papel:

1. RAG vectorial evaluado con Context Relevance sobre un dataset sintetico simple; el encoder es un transformer encoder (BERT o derivado); los alumnos eligen el encoder y tunean hiperparametros para maximizar el benchmark.
2. Agente que usa ese RAG y ademas hace RAG con tool-use contra una fuente externa (info que no esta en la base vectorial); evaluado con Context Relevance, Answer Faithfulness y Answer Relevance; modelo de OpenRouter fijado por la catedra.
3. Las herramientas del agente convertidas en servidor MCP y probadas con un modelo mejor: al cambiar el agente, las herramientas se reutilizan.
4. Notebook de atencion en NumPy desde cero (una capa de self-attention sobre embeddings de juguete), como sugirio Claude.
5. Ejercicio a mano: escribir las operaciones de una capa de atencion sobre matrices chicas y, en cada aplicacion de una funcion (proyeccion, producto punto, escala, softmax, mezcla, residual, layer norm), justificar por escrito la razon y la utilidad de esa operacion.

## Corpus (research/raw, bajado 2026-09-22)

attention-is-all-you-need (ar5iv, paper completo), illustrated-transformer-alammar, bert-devlin-2018, gpt2-radford-2019 (pdf), rope-su-2021, gqa-ainslie-2023, flashattention-dao-2022, deepseek-v2-mla-2024, vit-dosovitskiy-2020, sentence-bert-reimers-2019, scaling-laws-kaplan-2020, gpt2-to-kimi3-waterloo-intern (md).

---

## 2026-09-22 — Step 1 (Frame)
- Status: complete
- Asks log: nivel de matematica → numeros chicos en el bloque 2; practica → si, la de RAG+MCP mas notebook NumPy mas ejercicio a mano con justificaciones; variantes modernas → cualitativas, a fondo en la clase 9.
- What was decided: temario de 6 bloques, modo B, carpeta transformers-a-fondo.
- Files created/modified: talks/transformers-a-fondo/{memory.md, research/raw/*}

## 2026-09-22 — Step 2 (Collect)
- Status: complete (Claude bajo las fuentes; Marco aporto el articulo de X)

## 2026-09-22 — Step 3 (Corpus)
- Status: complete. 12 registros en research/corpus/ (librarian; ninguna fuente fallo). Caveats anotados en los registros: 41,8 vs 41,0 BLEU en el paper de Attention; GPT-2 117M declarados vs 124M reales; Kaplan superado por Chinchilla.

## 2026-09-22 — Step 4 (Draft)
- Status: complete. Composer (scope=full): 0 blockers, 6 majors y 21 minors, todos aplicados; ejemplo numerico verificado celda por celda; 83 min de contenido. Desrobotizado lamina por lamina el 2026-09-22 a pedido de Marco.
- 28 laminas de contenido: 1 Donde quedamos (2), 2 La atencion con numeros (6), 3 El bloque completo (6), 4 Encoder, decoder y la familia (6), 5 Lo que cambio desde 2017 (5), 6 Entrenamiento a vuelo de pajaro (2), Conclusiones (1). 9 diagramas ASCII.
- Ejemplo numerico de toda la clase: "the cat sat" (3 tokens, d = 4, para que n y d no coincidan), X con enteros chicos, Wq = I, Wk permuta pares de columnas, Wv suma pares y baja a d_v = 2; script `ejemplo_atencion.py` en el scratchpad de la sesion (copiar a la mision).
- Cada lamina de operacion lleva en las notas la justificacion de la operacion, pensada para el ejercicio a mano de la practica.

## 2026-09-22 — Step 5 (Review), ronda 1
- Status: aplicada. Draft pusheado con el feedback de Marco (a46c147) antes de aplicarlo.
- Feedback y resolucion: (1) 1.1 la atencion enriquece los embeddings con contexto → agregado; (2) n = d confundia → ejemplo pasa a 3 tokens x d = 4, todas las tablas recalculadas (QK^T 3x3, softmax fila cat [0,45 0,10 0,45], A·V cat [1,80 1,20], con mascara [1,64 0,55]); (3) intuicion de Q/K/V segun Marco → viñeta nueva en 2.1; (4) W entrenables → viñeta en 2.2; (5) QK^T es *casi* la matriz de atencion → viñeta en 2.3; (6) el softmax da la matriz de atencion A → claim de 2.4; (7) explicar el problema antes de las residuales → lamina nueva 3.3 "El problema de apilar: el gradiente se pierde" (regla de la cadena, 0,9^48), y 3.4 explica por que x + f(x) lo resuelve; (8) embeddings posicionales desde el principio → lamina nueva 1.3 "La posicion entra con el embedding"; la 3.6 queda solo con la formula sinusoidal.
- Pendiente de decision: nada; esperar ronda 2.

## 2026-09-23 — Step 5 (Review), ronda 2
- "GPT-2 es la columna derecha sola" → encoder/decoder por nombre en todo el deck; regla nueva en reglas-propias ("apodos visuales").
- "Entrenamiento a vuelo de pajaro" → "Como se entrena"; otros modismos figurados corregidos.
- Seccion 5: Marco pidio mencion conceptual y habia 5 laminas con mecanismo, numeros y diagramas. Queda UNA lamina: tabla tecnica → problema que ataca, sin explicar como funciona; todo el detalle va a la clase 9 (Transformers Avanzados).
- Lamina "Las leyes de escala" eliminada; seccion 6 queda con una lamina (que se minimiza).

## 2026-09-23 — Mision asociada escrita
- `missions/rag-mcp-transformers/` (ver su mission.md). Decisiones de Marco: dominio hospital; dataset y API los genera la catedra y los alumnos levantan la API localmente; parte 5 con "El banco aguanta" / "El banco presta"; parte 3 con un solo LLM barato (deepseek-v4-flash, el mismo de la parte 2; el "agente mejor" se descarto el 2026-09-23) y el MCP Inspector como segundo cliente sin LLM; juez gemini-3.7-flash; entrega 9 de octubre.
- Pendientes del deck, en este orden, despues de terminar la mision (pedido de Marco 2026-09-23):
  1. Ampliar el contenido sobre entrenamiento.
  2. Quiz inicial de repaso (de la clase anterior, palabra-al-transformer).
  3. Quizas un quiz final post presentacion.

## 2026-09-23 — Step 6 (Polish) y Step 7 (Render)
- 8 diagramas ASCII renderizados con critica ciega (ascii-notes agregadas al draft antes): 6 limpios a la primera, mezcla de valores limpio tras 1 revision (margen), posicion limpio tras 2 revisiones (recorte; Claude autorizo una pasada extra). Embedding de oracion: el critico marco "pooling" en ingles; aceptado como termino tecnico. La lamina 4.1 conserva la figura del paper (bloque documentation-only).
- final.md: stamp-renders, cleanup, strip_feedback. (Ese primer modelo salio de un builder en python; quedo reemplazado por el Polish 1.0, ver abajo.)
- Quirk del harness repetido: los veredictos de los criticos llegan al orquestador y hay que reenviarlos a cada worker.

## 2026-09-23 — Polish de las matrices
- Marco pidio las matrices como imagenes: las 6 tablas (X, Q y K, Q K^T, A, mascara causal, tabla de posicion) pasaron a bloques ASCII con ascii-note en el draft y se renderizaron a SVG con critica ciega. 5 limpias a la primera; la mascara causal, limpia tras 1 revision (etiquetas de fila pegadas al corchete). Los 8 diagramas anteriores se reutilizaron sin re-render (digest estampado). Deck: 41 laminas, 14 diagramas.

## 2026-09-23 — Polish y Render de nuevo con Talksmith 1.0.0
- Plugin actualizado a 1.0.0 (mas templates, `design` para ubicar la imagen, `_choice` obligatorio). El clon local del plugin quedo sin cambios, a pedido de Marco.
- Polish rehecho desde cero: 14 diagramas con critica ciega (log "Run 2026-09-23 (1.0.0)" en cada `.critique/*.md`).
- El FILL de `output/slide-model.json` se escribe a mano, segun la spec. Marco marco como bug el builder en python y `research/build_model*.py` se borraron. Las notas se copian textuales de final.md.
- El critico de clasificacion confirmo las elecciones; se corrigieron las trazas de 16, 17, 18, 30 y 33.
- Las 14 laminas con diagrama usan content+cards+image con `design` split-left/split-right, porque sin design no se ve la imagen.
- "Cuenta de parametros" se partio en dos laminas: tabla + conclusion, y las dos notas como tarjetas. Con las tres notas abajo, el ajuste llegaba al minimo de escala y recortaba las dos ultimas filas.
- Deck: 42 laminas. Todas las audits dan ok. Los warnings de template_diversity estan justificados: domina content+cards+image y el repaso son 8 quiz seguidos.
