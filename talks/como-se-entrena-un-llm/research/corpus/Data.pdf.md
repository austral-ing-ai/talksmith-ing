---
source_file: Data.pdf
source_type: article
ingested_at: 2026-09-25
---

# Data — presenter's working notes for "Cómo se entrena un LLM"

## Provenance
- Original location: articles/Data.pdf
- Format: pdf (4 pages; exported from Apple Notes — PDF Creator "Notes", Producer "macOS Version 26.6.2 Quartz PDFContext")
- Author / source (if known): the presenter (own notes). The two embedded photos are of figures from Chip Huyen, *AI Engineering: Building Applications with Foundation Models* (O'Reilly, 2025), chapter 2 (identification per the orchestrator's briefing and the printed captions visible in the photos).
- Date of original (if known): PDF CreationDate 2026-09-25 15:25:09 -03 (export date; the notes themselves may be older).
- Language: mixed English/Spanish, with typos preserved verbatim below ("ComonCrawl", "billon", "Underrepresentacion", "Distribuciónn", "evolucuon", "langages", "C0mmon", "Post-Trainned", "finetunning", "Ingredientes", "IntrudctGPT", "regard model").

## Key claims
These are the presenter's outline bullets, not sourced claims. Grouped as in the notes:
- **Training data:** Common Crawl ("2 billon websites"); Google C4 ("curated").
- **Languages:** under-representation of languages; distribution per person (speakers); a chart of the evolution of languages and models; "Lost language"; models are "More expensive on other languages" — with the presenter's own question: is this due to the language or to the dataset?
- **Common Crawl:** "Data distribution per category is not the same."
- **Model size:** Chinchilla model; FLOPs; "Number of training tokens must be 20x the number of parameters" — "3b models needs 60 b tokens"; "scaling law: model quality giving compute budget".
- **Scaling bottlenecks:** How much can it grow? Projection of running out of data (Fig. 2-9 photo). Lots of AI-generated data. "Deals and more deals on different type of data."
- **Pre-trained model:** output is optimized for auto-completion, not conversation; open question "Is it possible to find an example of this?"; "Bias, racism, things that are not aligned to company objectives."
- **Post-training:** SFT "Supervised with high quality instruction"; preference finetuning ("Usualmente RL", RLHF); "Only 2% of total training"; planned "Slides con ejemplo de dataset de SFT".
- **SFT:** the pizza-ingredients example — a pre-trained model asked for pizza ingredients "will bring completion instead of 'returning what it's a pizza ingredientes'"; demonstration data = (prompt, response); generating it can be expensive (InstructGPT); "What to say and how to say it?"
- **RLHF:** relies on a reward model; for (Q, R) the model scores / ranks. (Fig. 2-10 photo shows the full pipeline.)
- **Training for tools and web search:** "Expand on several slides on how is this achieved." "This is part of SFT /" (sentence left unfinished).
- **Effort:** "example on how is trained for that" (reasoning effort).
- **"Model just try to respond"** — "How is this prevented?" (hallucination / always answering).

## Definitions and terminology
- **Pre-trained model** — output optimized for auto-completion, not conversation.
- **SFT** — supervised finetuning with high-quality instruction (demonstration) data in (prompt, response) form.
- **Preference finetuning** — usually RL; RLHF as the main example.
- **RLHF reward model** — scores a (question, response) pair; used for ranking.
- **Scaling law** — "model quality giving compute budget" (i.e., best model quality attainable for a given compute budget).
- **Chinchilla rule** — training tokens ≈ 20 × parameters.

## Evidence and examples
- Numeric examples in the notes: Common Crawl ≈ "2 billon websites"; 20× tokens-per-parameter; 3B params → 60B tokens; post-training ≈ "2% of total training".
- Worked example planned: pizza ingredients (completion vs. answering).
- Two book figures photographed (see *Images / diagrams*): Fig. 2-9 (data-stock projection, Villalobos et al. 2024) and Fig. 2-10 (pre-training → SFT → RLHF workflow).

## Inconsistencies / open questions
- [verified] "3b models needs 60 b tokens" is consistent with the note's own 20× rule (3B × 20 = 60B) — checked arithmetically within the note.
- [open question] "ComonCrawl (2 billon websites)" — the note gives no date or unit definition (pages vs. websites/domains); Common Crawl's size varies by crawl. Settle against the book's cap. 2 text or a Common Crawl statistics page before putting a number on a slide.
- [open question] "Only 2% of total training" for post-training — the note gives no source; the book's cap. 2 (Post-Training) is the likely origin (the orchestrator's plan-de-fuentes maps it there). Confirm against the book text, which is not in the corpus.
- [open question] "More expensive on other languages. ?. Is due to the language or dataset." — the presenter's own open question; `petrov-2023-tokenizer-unfairness.pdf` and `web/jun-2023-languages-tokenized/` address it (tokenizer-driven length disparity).
- [open question] "(?). Is it possible to find an example of this ?" — presenter wants a concrete autocomplete-vs-conversation example; `ouyang-2022-instructgpt.pdf` has GPT-3 vs InstructGPT sample outputs.
- [open question] "Chart de le evolucuon de langages y modelos" and "Lost language" — intent unclear from the note alone (a chart of language coverage across model generations? endangered/lost languages?). Needs the presenter's clarification.
- [open question] "This is part of SFT /" (tools and web search) — sentence is unfinished; whether tool-use training is presented as SFT only, or also RL, is undecided in the note. `lambert-rlhfbook-tool-use.web.md` covers both.
- [open question] "Effort, example on how is trained for that" — ambiguous: likely "reasoning effort" (thinking budget). `deepseek-2025-r1.pdf` is the mapped source; confirm intent with the presenter.

## Images / diagrams
### `Data.pdf/images/p002-fig-2-9-data-stock-projection.png`
- Provenance: raster photo embedded on page 2 of `articles/Data.pdf` (1440×960 px, extracted with `pdfimages -png`). Photo of a printed book page: Chip Huyen, *AI Engineering*, Figure 2-9 (printed caption visible in the photo credits Villalobos et al., 2024). Placed in the notes next to the "Scaling Bottlenecks" bullets. Stored as extracted (already upright).
- Depiction: Line chart on a log-scale y-axis ("Effective stock (number of tokens)", 10^11 to 10^15) against years 2020–2034. A flat teal band ("Stock of data") sits around 10^14 tokens (band roughly 3×10^13 to 10^15). A rising blue line with a shaded band ("Dataset size projection") climbs from ~5×10^11 in 2020 and flattens into the stock band around 2030. Dots mark real training sets: GPT-3 (2020), FLAN (~2021.5), PaLM (~2022.5), Falcon-180B (~2024), DBRX and Llama 3 (~2024.5, near 10^13). Two dashed verticals mark the median dates of full stock utilization: ~2028 with 5× overtraining (blue) and ~2028.7 without (red). Below the figure, the page text notes that people publish text on the internet to influence future models' training data, and that this can be used for prompt injection (ch. 5).
- Why it matters: The single visual for the "Scaling bottlenecks → projection of running out of data" bullet: dataset sizes grow ~an order of magnitude every ~2 years and meet the finite stock of public human text before 2030. Pairs with `villalobos-2024-run-out-of-data.pdf.md` (original source of the chart).
- Transcribed text: "Figure 2-9. Projection of historical trend of training dataset sizes and available data stock. Source: Villalobos et al., 2024." Legend: "Stock of data"; "Median date of full stock utilization"; "Dataset size projection"; "Median date of full stock utilization (5x overtraining)". Axis: "Effective stock (number of tokens)"; "Year". Labels: GPT-3, FLAN, PaLM, Falcon-180B, DBRX, Llama 3.

### `Data.pdf/images/p003-fig-2-10-training-workflow-rotated-upright.png`
- Provenance: raster photo embedded on page 3 of `articles/Data.pdf` (3024×4032 px as embedded, extracted with `pdfimages -png`). Photo of a printed book page: Chip Huyen, *AI Engineering*, Figure 2-10 (overall training workflow: pre-training, SFT, RLHF). The photo is embedded rotated 90° in the PDF; the companion copy was **rotated 90° counter-clockwise to upright** (now 4032×3024 px) — the only transformation applied. Placed in the notes next to the Pre-Trained / Post-Training bullets.
- Depiction: Three-column workflow diagram. Column 1: "Low-quality data (e.g., Internet data)" → "Self-supervised pretraining" → "Pretrained model", annotated "Optimized for completion". Column 2: "High-quality data — Demonstration data" → "Supervised finetuning" → "SFT model", annotated "Fine-tuned for dialogue". Column 3, inside a dashed box labeled "RLHF": "Human feedback — Comparison data" → "Classification" → "Reward model", annotated "Trained to give a scalar score for (prompt, response)"; then "Prompts" → "Reinforcement learning" → "Final model", annotated "Optimized to generate responses that maximize scores by reward model". Arrows: the pretrained model feeds SFT; the SFT model feeds both the reward-model classification and the RL step; the reward model feeds RL.
- Why it matters: The backbone of the talk's arc (pre-training → SFT → preference finetuning/RLHF), with the data type, objective and output of each stage in one picture. Matches the notes' "Pre-Trained: optimizado para auto-completion", "SFT: demonstration data (prompt, response)" and "RLHF relies on a reward model that scores (Q, R)". Same pipeline as InstructGPT Fig. 2 (`ouyang-2022-instructgpt.pdf.md`).
- Transcribed text: Page text above the figure: "Figure 2-10 shows the overall workflow of pre-training, SFT, and preference finetuning, assuming you use RLHF for the last step. You can approximate how well a model aligns with human preference by determining what steps the model creators have taken." Caption: "Figure 2-10. The overall training workflow with pre-training, SFT, and RLHF." Below: "If you squint, Figure 2-10 looks very similar to the meme depicting the monster…" (cut off).

## Raw / preserved excerpts

### Full extracted text (verbatim, `pdftotext -layout`, all 4 pages)

~~~~~text
Data
Training Data
 – ComonCrawl (2 billon websites)
 – Google C4 (curated)

Languages
    - Underrepresentacion of languages.
    - Distribuciónn por persona
    - Chart de le evolucuon de langages y modelos.
    - Lost language
    - More expensive on other languages. ?. Is due to the language or dataset.



C0mmon Crawl.
   - Data distribution per category is not the same.
   -

Size of the Parameters of the models
     - Chinchilla Model
     - FLOPS
     - Number of training tokens must be 20x the number of parameters.
          -3b models needs 60 b tokens
          - scaling law: model quality giving compute budget.
     -
 – Scaling Bottlenecks.
     – How much can in grow ?
     – Projection of running out if data.
     – Lot of AI generated data.
     – Deals and more deals on different type of data.
– Pre-Trained
           – Lo que sale esta optimizado para auto-completion, no
             conversation.
          – (?). Is it possible to find an example of this ?
          – Bias, racism, things that are not aligned to company objectives
      – Post-Trainned
   – Post Training
      – SFT: Supervised with high quality instruction
      – Preferences finetunning:
          – Usualmente RL
          – RLHF
      – Only 2% of total training
   – Slides con ejemplo de dataset de SFT
  -SFT
    - Ingredientes for a pizza, it will bring completion instead of “returning
  what it’s a pizza ingredientes”
    - Demonstration data (prompt, response)
    - Generate this can be expensive and (IntrudctGPT)
    - —> What to say and how to say it ?

   – RLHF
      – This relies on regard model. For (Q, R), model score a ranking
– Training for Tools and WebSearch
   – Expand on several slides on how is this achieved.
   – This is part of SFT /
– Effort, example on how is trained for that.
– Model just try to respond.
   – How is this prevented ?.
~~~~~
<!-- truncated-in-source: no complete version available -->
Note: several bullets in the original are empty ("-" after "Data distribution per category is not the same." and after "scaling law…") and "This is part of SFT /" ends mid-sentence; that is how the notes were written, not an extraction loss.
