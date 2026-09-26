---
source_file: petrov-2023-tokenizer-unfairness.pdf
source_type: article
ingested_at: 2026-09-25
---

# Language Model Tokenizers Introduce Unfairness Between Languages

## Provenance
- Original location: articles/petrov-2023-tokenizer-unfairness.pdf
- Format: pdf (28 pages)
- Author / source (if known): Aleksandar Petrov, Emanuele La Malfa, Philip H.S. Torr, Adel Bibi — University of Oxford (contact: aleks@robots.ox.ac.uk). Published at the 37th Conference on Neural Information Processing Systems (NeurIPS 2023). Funding: Amazon Research Awards (AB), UKRI Turing AI Fellowship (EP/W002981/1), EPSRC CDT in Autonomous Intelligent Machines and Systems (EP/S024050/1), Royal Academy of Engineering, FiveAI.
- Date of original (if known): 2023 (NeurIPS 2023 camera-ready; no arXiv identifier or exact date printed in the extracted text). Pricing statements refer to OpenAI and Google Cloud pricing "at the time of writing".
- Extraction: `pdftotext` (poppler, UTF-8, reading order). Math, tables and multi-column layout are flattened; equations and table cells may be garbled in the verbatim text below — consult the page renders in the companion folder for exact figures/tables.

## Key claims
- "Disparity in the treatment of different languages arises at the tokenization stage, well before a model is even invoked." "The same text translated into different languages can have drastically different tokenization lengths, with differences up to 15 times in some cases."
- Disparities "persist even for tokenizers that are intentionally trained for multilingual support"; "Character-level and byte-level models also exhibit over 4 times the difference in the encoding length for some language pairs."
- LLM multilingualism "is currently treated as a curious emergent phenomenon rather than a carefully designed, controlled and managed process"; LLMs trained on "large swaths of internet content regardless of language" "end up being multilingual, even if not by design" (e.g., ChatGPT).
- ChatGPT/GPT-4's tokenizer (cl100k_base) "uses about 1.6 times more tokens to encode the same text in Italian as it does in English, 2.6 times for Bulgarian and 3 times for Arabic. For Shan ... that difference can be as high as 15 times."
- Three fairness implications: (1) **Cost** — per-token or per-character pricing means "users of some languages paying at least 2.5 times more for the same task as users of English"; (2) **Latency** — "Some languages can require twice the time to process the same content as English"; (3) **Long context processing** — users of token-efficient languages can process texts "more than an order of magnitude longer".
- Proposal: "multilingual tokenization parity: tokenizers should produce similar encoded lengths for the same content across languages"; "we should train future language models using multilingually fair subword tokenizers."
- Tokenizer vocabularies reflect "the biases of the corpus source": GPT-2 has glitch tokens like "BuyableInstoreAndOnline", "rawdownloadcloneembedreportprint", "ゼウス", "サ–ティワン", yet splits the Arabic word for "why" into letters and needs 6 tokens for the 4-letter Bulgarian "защо"; "more than half of the Japanese kanji characters require three tokens" in GPT-2; cl100k_base still needs two tokens for some Cyrillic letters and three tokens for "more than 65% of kanji characters".
- English-centric tokenizers (GPT-2/RoBERTa, ChatGPT/GPT-4, FlanT5) "are far from tokenization parity": for GPT-2/RoBERTa even the cheapest language (Pangasinan) is 66% more expensive than English; for ChatGPT/GPT-4 the cheapest (Portuguese, Pangasinan, German) still carry ~50% premium, and Shan is ~15× (Shan is worst for all four models).
- FlanT5 has >10% UNK tokens for 42% of languages; its premium range 1.37–3.41 covers only 54% of languages, so it cannot be called more fair.
- Non-English-target tokenizers still favour English: GottBERT (German) English 1.35 vs Dutch 1.73, Luxembourgish 1.75; CamemBERT (French) English 1.20 vs Catalan 1.59, Friulian 1.66; PhoBERT (Vietnamese) English lowest at 1.20; MuRIL (16 Indian languages + English) "remains most token-efficient for English". "We conclude that tokenizers for other languages give English preferential treatment," likely due to "extensive incorporation of English in documents written in other languages".
- Shared scripts help: RoCBert (Chinese), BERT Japanese and ArabicBERT have lowest premiums for languages sharing their script.
- Multilingual models (XLM-R, NLLB, mT5, M2M100, BLOOM) are better than English-centric ones, but "none of the models uniformly reaches parity across all languages"; all five have languages with premiums above 2.5.
- Byte/character-level models are not a fix: CANINE (UTF-32 codepoints) gives Shan 4.58× the length of Yue Chinese; ByT5 (UTF-8 bytes) ranges 0.87 (Yue Chinese) to 3.94 (Shan). Two sources of disparity: natural differences in number of characters per content, and UTF-8 using 1–3+ bytes depending on script.
- Cost: for ChatGPT/GPT-4, German or Italian cost ~50% more than English; "Dzongkha, Odia, Santali or Shan ... costs more than 12 times more than in English". Per-character pricing (Google Cloud Natural Language) also disadvantages Burmese, Dzongkha, Shan, Tok Pisin, Tumbuka (>4× the characters of Yue Chinese).
- Latency: RoBERTa processing time appears "linear in the tokenization length rather than quadratic"; Shan takes almost twice English's time; Latin/Greek-derived scripts fastest, then CJK and Arabic, then other Asian and African scripts. Speech recognition and synthesis are affected too.
- Long context: with fixed context windows "one can process less than a tenth of the content in languages like Burmese and Dzongkha than they can in English"; this can degrade automated systems like content moderation, with "severe real-world impacts".
- Remedies: subword tokenization is necessary (character/byte-level can't reach parity); a separate billing tokenizer "is not sufficient" (does not fix latency or context); tokenization must support all Unicode codepoints (UTF-8 base preferred); a balanced, diverse parallel corpus is needed; proposed two-stage method — train monolingual tokenizers, then merge starting from 256 byte tokens by "repeatedly adding the most frequently used token for the language with the highest premium".
- Vocabulary has diminishing returns: "with only a third of the vocabulary, English sequences will become just 10% longer for ChatGPT/GPT-4"; a 10-fold vocabulary reduction gives only 30% longer English sequences — so reallocating tokens to other languages is likely a net benefit.
- Dialects: GottBERT gives Swiss German dialects premiums 1.38 (Zürich) – 1.59 (Bern), worse than English (1.35); ArabicBERT is near parity across 25 Arabic dialects (0.91–1.17); BERT Japanese near parity across 20 dialects (1.01–1.15); CamemBERT: Mauritian Creole 1.20, Haitian Creole 1.64 (QEDv2) / 1.58 (FLORES-200) vs English 1.20.
- Claimed novelty: "we are the first to leverage a parallel corpus to compare tokenization lengths across languages" (concurrent work by Ahia et al. 2023 reaches similar conclusions).

## Definitions and terminology
- **Tokenization** — "the process of turning natural language into sequences of tokens coming from a finite and pre-determined set called vocabulary"; each token is associated with an integer.
- **Tokenizer parity** — a tokenizer t achieves parity for language A with respect to B at translated sentences s_A and s_B if |t(s_A)| / |t(s_B)| ≈ 1.
- **Tokenization premium** — the ratio |t(s_A)| / |t(s_B)|: the premium for A relative to B (usually B = English or the tokenizer's target language).
- **Multilingual tokenization parity / multilingually fair tokenizer** — tokenizers that "produce similar encoded lengths for the same content across languages".
- **FLORES-200** — parallel corpus of "the same 2000 sentences taken from Wikipedia and human-translated to 200 different languages".
- **Glitch tokens** — odd dedicated tokens arising from corpus artefacts (usernames, game concepts, store back-end strings), e.g. "BuyableInstoreAndOnline".
- **Word tokenization** — splitting at whitespace, one token per word; fails for open vocabularies and space-less scripts.
- **Subword tokenization** — breaking complex words into multiple tokens, e.g. "Cottonshopeburnfoot" → "Cotton"+"shop"+"e"+"burn"+"foot".
- **WordPiece / BPE / Unigram / SentencePiece** — WordPiece (Schuster and Nakajima, 2012); Byte-Pair Encoding merges most frequent pairs (Sennrich et al., 2016); Unigram prunes a large vocabulary (Kudo, 2018); SentencePiece treats whitespace as a symbol and supports both; "SentencePiece with BPE is by far the most popular".
- **UNK token** — special token for symbols outside the vocabulary; languages with >10% UNK characters are excluded (—) in the tables.
- **Unicode / codepoint** — standard assigning one of 1,114,112 integer codepoints to every grapheme, modifier, punctuation, control or formatting character.
- **UTF-8 / UTF-32** — variable-width (1–4 bytes per codepoint) vs fixed-width (4 bytes) encodings; ASCII = 1 byte; Latin (non-ASCII), Greek, Cyrillic, Coptic, Armenian, Hebrew, Arabic, Syriac = 2 bytes; Chinese, Japanese, Korean = 3 bytes.
- **Byte-level BPE** — BPE run on UTF-8 bytes; unseen characters fall back to bytes (e.g., "I love açaí" → "I "+"love "+"a"+C3+A7+"a"+C3+AD).
- **Byte-level / character-level tokenization** — CANINE ≈ UTF-32 (implicit vocabulary 1,114,112); ByT5 = UTF-8 (implicit vocabulary 256).
- **cl100k_base** — the tokenizer shared by ChatGPT and GPT-4; r50k_base, p50k_base, p50k_edit behave like GPT-2/RoBERTa (difference < 0.005).
- **Diglossia** — "the situation of two dialects or languages being used by a single language community".
- **Dialect vs pidgin/creole** — dialects are regional variations; pidgins and creoles are contact languages emerging from interaction of speakers of different languages.

## Evidence and examples
- **Glitch-token examples (GPT-2)** — "BuyableInstoreAndOnline" and "rawdownloadcloneembedreportprint" have dedicated tokens; Arabic "لماذا" ("why") → one token per letter; Bulgarian "защо" → 6 tokens (IDs 140 115 16142 141 231 15166); Japanese "言" ("to say") → 3 tokens (164 101 222).
- **Shan example** — "မႂ်း" (one Shan word for "you") is tokenized by ChatGPT/GPT-4 into 9 tokens (25870 247 157 224 224 25870 118 25870 116): one consonant + three diacritics = four Unicode codepoints; English "you" = 1 token. ByT5 encodes it as 12 tokens vs 3 for "you".
- **Table 1** (English-centric; premium vs English; columns GPT-2/RoBERTa, ChatGPT/GPT-4, FlanT5; reconstructed from flattened extraction and cross-checked with prose): Bulgarian 5.51 / 2.64 / —; Burmese 16.89 / 11.70 / —; Chinese (Simplified) 3.21 / 1.91 / —; Dzongkha 16.36 / 12.33 / —; English 1.00 / 1.00 / 1.00; French 2.00 / 1.60 / 1.60; German 2.14 / 1.58 / 1.37; Italian 2.01 / 1.64 / 2.18; Japanese 3.00 / 2.30 / —; Jingpho 2.65 / 2.35 / 3.41; Maori 2.45 / 2.35 / 3.28; Norwegian Bokmål 1.86 / 1.56 / 2.24; Odia 13.38 / 12.48 / —; Pangasinan 1.66 / 1.57 / 2.18; Portuguese 1.94 / 1.48 / 2.21; Romanian 2.48 / 1.88 / 1.50; Santali 12.86 / 12.80 / —; Shan 18.76 / 15.05 / —; Spanish 1.99 / 1.55 / 2.23; Standard Arabic 4.40 / 3.04 / —; Tumbuka 2.78 / 2.57 / 3.29; Vietnamese 4.54 / 2.45 / —.
- **Table 2** (non-English-target models; premium vs target language), selected: ArabicBERT — English 1.83, N. Levantine Arabic 1.00, Greek 4.93; RoCBert — Chinese (Trad.) 0.94, Yue 0.92, English 2.60; CamemBERT — English 1.20, Catalan 1.59, Friulian 1.66; GottBERT — English 1.35, Dutch 1.73, Luxembourgish 1.75, Dzongkha 16.12, Shan 16.88; BERT Japanese — Chinese (Simp.) 0.82, (Trad.) 0.84, English 1.49; PhoBERT — English 1.20.
- **Table 3** (MuRIL vs English) — English 1.00, Nepali 1.01, Bengali 1.01, Tamil/Marathi/Kannada 1.06, Hindi 1.16, Malayalam 1.18, Gujarati 1.19, Sanskrit/Telugu/Odia 1.21, Sindhi 1.22, Assamese 1.24, Urdu 1.26, Eastern Panjabi 1.35, Kashmiri (Arabic) 1.75, Kashmiri (Devanagari) 1.75.
- **Table 4** (multilingual; premium vs English; column assignment inferred from the flattened layout and the "—" pattern): XLM-R — Shan 4.43, Kabiyè 2.98, Central Kanuri 2.60; NLLB — max Central Kanuri 2.54, Shan 1.94; mT5 — Dzongkha 4.24, Std. Tibetan 3.68, Shan 3.28; M2M100 — Shan 4.63, Uyghur 3.00; BLOOM — Santali 12.71, Shan 12.06, Dzongkha 7.36, Std. Tibetan 6.66. Chinese/Yue near or below 1.0 for most.
- **Table 5** (byte-level; premium vs English; CANINE / ByT5): Bulgarian 1.04 / 1.89; Burmese 1.24 / 3.51; Chinese (Simp.) 0.34 / 0.93; Chinese (Trad.) 0.32 / 0.89; Dzongkha 1.25 / 3.64; English 1.00 / 1.00; Italian 1.18 / 1.19; Japanese 0.44 / 1.27; Shan 1.42 / 3.94; Standard Arabic 0.88 / 1.60; Standard Tibetan 1.13 / 3.31; Tok Pisin 1.28 / 1.28; Tumbuka 1.30 / 1.32; Yue Chinese 0.31 / 0.87.
- **Figure 1** — XLM-R vs RoBERTa premiums for languages XLM-R encodes with <10% UNK: XLM-R much closer to parity.
- **Figure 2** — RoBERTa average processing time vs tokenized length on FLORES-200 (20 runs per sentence), coloured by script family; roughly linear; English lower-left, Shan upper-right (~2× time).
- **Figure 3** — tokens needed to encode English FLORES-200 vs cl100k_base vocabulary subset size: "A 10-fold reduction in the vocabulary would result in only 30% longer sequences for English. With one-third of the vocabulary, English sequences will become just 10% longer for ChatGPT/GPT-4".
- **Figure 4** — UTF-8 (variable-width) vs UTF-32 (fixed-width) encodings; emoji example: waving hand F0+9F+91+8B, skin-tone modifier F0+9F+8F+BD.
- **"hotel" example** — spelled identically in English, Spanish, Italian, Portuguese, Dutch, Danish, Hungarian, Polish; Korean "호텔" shares tokens with no other language — languages from larger families get shorter tokenizations.
- **Context sizes cited** — RoBERTa 512; GPT-2 "768, 1024, 1280, or 1600"; GPT-4 "8,000 and 16,000 context variants".
- **Table 6** (GottBERT, SwissDial, vs High German) — Zürich 1.38, St. Gallen 1.40, Basel 1.41, Graubünden 1.44, Luzern 1.52, Aargau 1.53, Wallis 1.58, Bern 1.59; Bernese close to Swedish (1.64) and Norwegian Bokmål (1.65). Example "Like he's waiting for something": High German "Als warte er auf etwas ." vs a Bernese rendering almost twice as many tokens.
- **Table 7** (ArabicBERT, MADAR, 25 dialects vs Standard Arabic) — Jeddah 0.91 … Rabat 1.17; about half below Standard Arabic.
- **Table 8** (BERT Japanese, CPJD, 20 dialects, 250 sentences) — Saitama-ben 1.01 … Morokata-ben and Okayama-ben 1.15; English 1.49.
- **Creoles** (CamemBERT) — Mauritian Creole 1.20 (MorisienMT); Haitian Creole 1.64 (QEDv2) and 1.58 (FLORES-200), vs English 1.20, Pangasinan 1.49, Nigerian Fulfulde 1.54.
- **Appendix C** — extended premium tables for all 200 languages also covering LLaMA, MBart50, SeamlessM4T and Qwen-VL (flattened/garbled in extraction).

## Inconsistencies / open questions
- [verified] Magnitude of multilingual-tokenizer disparity is stated differently: abstract/intro say differences "up to 15 times" (that is ChatGPT/GPT-4 on Shan, an English-centric tokenizer), while the Conclusion says "even tokenizers explicitly trained for multilingual support exhibit tokenization lengths that vary by up to a factor of 13" (consistent with BLOOM's 12.71 for Santali in Table 4) — two different claims that are easy to conflate.
- [verified] Introduction: "byte-level representation of the same text is over 4 times longer for Burmese or Tibetan than Chinese", but Table 5 ByT5 gives Burmese 3.51 and Std. Tibetan 3.31 vs Chinese (Simp.) 0.93 / Yue 0.87 — ratios ≈3.6–4.0, so the "over 4 times" holds only for Burmese vs Yue (4.03), not for Tibetan (3.80 vs Yue).
- [verified] ArabicBERT's English premium is 1.82 in §4.2 prose but 1.83 in Table 2 and Appendix B.
- [verified] Table 4 contains "1,08" (comma) for mT5 Indonesian — typo in source. Other typos: "XML-R" for XLM-R; "monolinugal"; "them them"; "speling" (possibly intentional example of misspelling).
- [verified] Extraction garbling: Tables 1, 2, 4 and 5 are flattened into column runs with the sidebar text of §4.1 interleaved; Table 1/Table 4 cell assignments above were reconstructed and cross-checked against prose (e.g., Shan 15.05, Portuguese 1.48, Pangasinan 1.66, FlanT5 range 1.37–3.41, CANINE Shan/Yue = 4.58); right-to-left Arabic and Shan glyphs render out of order; Appendix C tables are unreadable without the page renders.
- [verified] Author-stated limitation: FLORES-200 "there are many English-centric names and institutions, which might skew the results in favour of English"; translations vary in length; topics must be balanced — "These limitations also hold for the results in this paper."
- [verified] Author-stated caveat on latency: attention is quadratic but "the full model architecture contains other submodules and therefore the overall complexity might be different"; measured only for RoBERTa.
- [verified] Author-stated caveat on dialect data: parallel corpora for dialects/creoles "are far and few in between"; city dialects may vary within regions.
- [verified] FlanT5 comparisons exclude languages with >10% UNK (42% of languages), so its apparent fairness is not comparable.
- [open question] "GPT-2 has 768, 1024, 1280, or 1600" is given as block/context size; those numbers look like GPT-2 model widths rather than context lengths — settled by the GPT-2 paper (Radford et al., 2019).
- [open question] "GPT-4 comes in 8,000 and 16,000 context variants" — date-dependent product claim (as of 2023); OpenAI's model documentation from that period would settle the exact variants.
- [open question] Pricing claims (OpenAI per-token, Google Cloud per-character) are "at the time of writing" (2023) — current price lists would settle whether they still hold.
- [open question] Whether newer tokenizers (e.g., larger-vocabulary tokenizers released after 2023) have reduced these premiums is outside this source — the authors' interactive project website or later studies would settle it.

## Images / diagrams
### `petrov-2023-tokenizer-unfairness.pdf/images/raster-p019-00.png`
- Provenance: raster image embedded in `articles/petrov-2023-tokenizer-unfairness.pdf`, page 19, 760x271 px, extracted with `pdfimages -png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `petrov-2023-tokenizer-unfairness.pdf/images/fig-01-p006.png`
- Provenance: Figure 1 of `articles/petrov-2023-tokenizer-unfairness.pdf`, page 6, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 908x559 px. Replaces the earlier whole-page render `page-006-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `petrov-2023-tokenizer-unfairness.pdf/images/fig-02-p006.png`
- Provenance: Figure 2 of `articles/petrov-2023-tokenizer-unfairness.pdf`, page 6, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 912x583 px. Replaces the earlier whole-page render `page-006-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `petrov-2023-tokenizer-unfairness.pdf/images/fig-03-p009.png`
- Provenance: Figure 3 of `articles/petrov-2023-tokenizer-unfairness.pdf`, page 9, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 895x337 px. Replaces the earlier whole-page render `page-009-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `petrov-2023-tokenizer-unfairness.pdf/images/fig-04-p019.png`
- Provenance: Figure 4 of `articles/petrov-2023-tokenizer-unfairness.pdf`, page 19, vector figure; cropped from the page with PyMuPDF (graphics bbox + labels + caption), rendered at 160 dpi, 909x246 px. Replaces the earlier whole-page render `page-019-figures.png`.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->


## Raw / preserved excerpts
> Recent language models have shown impressive multilingual performance, even when not explicitly trained for it. Despite this, there are concerns about the quality of their outputs across different languages. In this paper, we show how disparity in the treatment of different languages arises at the tokenization stage, well before a model is even invoked. The same text translated into different languages can have drastically different tokenization lengths, with differences up to 15 times in some cases. These disparities persist even for tokenizers that are intentionally trained for multilingual support. Character-level and byte-level models also exhibit over 4 times the difference in the encoding length for some language pairs. This induces unfair treatment for some language communities in regard to the cost of accessing commercial language services, the processing time and latency, as well as the amount of content that can be provided as context to the models. Therefore, we make the case that we should train future language models using multilingually fair subword tokenizers.

— Abstract

> However, this multilingualism is currently treated as a curious emergent phenomenon rather than a carefully designed, controlled and managed process. The performance of LLMs has been shown to be generally lower in non-target languages, a problem especially pronounced for low-resource languages (Virtanen et al., 2019; Ahuja et al., 2023).

— §1 Introduction

> This work demonstrates how the unequal treatment of languages arises at the tokenization stage, well before the language model sees any data at all. For instance, the tokenizer employed by ChatGPT (OpenAI, 2022) and GPT-4 (OpenAI, 2023) uses about 1.6 times more tokens to encode the same text in Italian as it does in English, 2.6 times for Bulgarian and 3 times for Arabic. For Shan —the native language of people from the Shan State in Myanmar— that difference can be as high as 15 times. Unicode character and byte-level tokenization also result in drastically different encoding lengths across languages: byte-level representation of the same text is over 4 times longer for Burmese or Tibetan than Chinese.

— §1 Introduction

> 1. Cost: Commercial services charge users per token or Unicode character. In either case, these discrepancies lead to users of some languages paying at least 2.5 times more for the same task as users of English.
> 2. Latency: The number of tokens has a direct effect on the processing time for a task. Some languages can require twice the time to process the same content as English. This may be critical for real-time applications like emergency services.
> 3. Long context processing: Many models have a fixed-size context. Users of languages that are more token-efficient can use these systems to process or generate texts that may be more than an order of magnitude longer than users of other languages. This may lead to significant discrepancies in the quality of service.

— §1 Introduction, three fairness implications

> Using large corpora scraped from the internet results in peculiar choices for tokens. For instance, GPT-2 contains glitch tokens which can be usernames or concepts from games (Rumbelow and Watkins, 2023b; Miles and Riley, 2023). As an example, BuyableInstoreAndOnline, likely coming from an online store backend, has a dedicated token. Another such token is rawdownloadcloneembedreportprint.

— §2 Intriguing Properties of Tokenization Across Languages

> The existence of glitch tokens like “ゼウス” and “サ–ティワン” despite the lack of a dedicated token for “言” shows that tokenizers are heavily influenced by the biases of the corpus source. If one uses non-natural inputs, log files, or specialist forums, the tokenizer vocabulary would reflect this. While cl100k_base, the tokenizer used for the newer ChatGPT and GPT-4, may not have glitch tokens it still requires two tokens to represent some Cyrillic letters and three tokens for more than 65% of kanji characters.

— §2

> Parity occurs when a tokenizer exhibits similar tokenized lengths for the same sentence in different languages. Take a sentence sA in language A and its translation sB to language B. Then, a tokenizer t achieves parity for A with respect to B at sA and sB if |t(sA)|/|t(sB)| ≈ 1, where t(sA) is the tokenization of the sentence sA and |t(sA)| represents its length. The ratio |t(sA)|/|t(sB)| is the premium for A relative to B.

— §3 Measuring Tokenizer Parity

> Summary. All four English-centric tokenizers we consider are far from tokenization parity. Portuguese is closest to parity with English for the ChatGPT and GPT-4 tokenizer but still requires about 50% more tokens for the same content. Shan is furthest from parity for this tokenizer with 15 times longer encodings compared to English. FlanT5 is closer to parity with its premium range 1.37–3.41 but it encodes only 54% of the languages, so we cannot say that it is more multilingually fair than the other tokenizers.

— §4.1 Parity for English-centric Models

> Across all tokenizers, the premium for English relative to the respective target language is significantly lower than the premium of RoBERTa for that target language. This asymmetry between English and all other languages likely stems from the extensive incorporation of English in documents written in other languages (Zhang et al., 2022).

— §4.2 Parity for Models with Other Target Languages

> Summary. We observed that the tokenizers targeting French, German and Vietnamese have English as the language closest to parity, rather than more linguistically close languages. On the other hand, tokenizers for Arabic, Chinese and Japanese have lower premiums for languages they share a script with. Notably, despite targeting Indian languages, MuRIL still has the shortest tokenizations for English. Finally, across all tokenizers, the premium for English is lower than the premium for the same language for the English-centric RoBERTa. Hence, we conclude that tokenizers for other languages give English preferential treatment.

— §4.2

> Summary: Multilingual models can improve the tokenization parity for different languages but challenges remain in achieving tokenization parity across all languages.

— §4.3 Parity for Multilingual Models

> Summary. Byte-level models also fail to achieve parity among the languages from FLORES-200 exhibiting a premium of over 4 times for some language pairs. There are two sources of multilingual tokenizer disparities. First, there are natural differences in the number of characters used in different languages to communicate the same content. Second, the UTF-8 standard uses different number of bytes to encode codepoints of different scripts.

— §4.4 Parity for Byte-level Tokenization Models

> It is increasingly common to access LLMs as paid API services. One pricing approach, employed by OpenAI at the time of writing, is to charge per token. Therefore, the tokenization premiums discussed in Section 4 directly map to cost premiums. For ChatGPT and GPT-4, the cost to process a text in German or Italian is about 50% higher than to process the same text in English (Table 1). Using them in Dzongkha, Odia, Santali or Shan, the most expensive languages for these services, costs more than 12 times more than in English.

— §5.1 Cost

> To assess the effect of the tokenization length on the latency, in Figure 2 we plot the computation time of RoBERTa against the tokenization lengths. It appears that the processing time is linear in the tokenization length rather than quadratic, showing a strong correlation between sequence length and execution time. Therefore, tokenization disparities across languages also affect the latency and processing time for text in these languages.

— §5.2 Latency

> For example, RoBERTa has a fixed block size of 512, GPT-2 has 768, 1024, 1280, or 1600 Radford et al. (2019), GPT-4 comes in 8,000 and 16,000 context variants. These models cannot process inputs longer than that. Therefore, one can process less than a tenth of the content in languages like Burmese and Dzongkha than they can in English.

— §5.3 Long context processing

> A separate tokenizer for determining the processing cost is not sufficient. An easy patch for existing models is to use a separate tokenizer for calculating how much a user should be charged. Using one tokenizer for computing the cost and another to process the input can easily be applied to existing systems without the need to retrain the LLM itself. However, as the tokenizer for the language model is unchanged, this approach would still suffer from latency and inability to process long contexts. Therefore, to ensure similar processing times and long context capabilities across languages, the language model has to be trained with a multilingually fair tokenizer.

— §6 Towards Multilingual Tokenization Fairness

> To address this issue, we suggest a two-stage process towards building a multilingually fair tokenizer. First, train individual monolingual tokenizers for all target languages. Then, merge them while maintaining parity. The merging can be done by starting with the 256 tokens corresponding to each value a byte can take and then repeatedly adding the most frequently used token for the language with the highest premium.
> While a multilingually fair tokenizer would lead to more tokens being needed for the dominant language, this additional cost would likely be much smaller than the benefit for the rest of the languages. The vocabulary size has diminishing returns: the additional tokens correspond to increasingly rare (parts of) words. For example, with only a third of the vocabulary, English sequences will become just 10% longer for ChatGPT/GPT-4 (see Figure 3).

— §6

> This paper highlights the significant disparities in tokenization across different languages which can lead to unequal treatment and disadvantages for certain language communities. The findings reveal that even tokenizers explicitly trained for multilingual support exhibit tokenization lengths that vary by up to a factor of 13. Furthermore, character-level and byte-level models also demonstrate encoding length discrepancies that are more than 4 times longer. These disparities have important real-world implications including increased costs for accessing commercial language services, longer processing times and limitations on the amount of contextual information provided to language models.

— §8 Conclusion

> UTF-8 can therefore represent any string in any language as a string of bytes. As each byte can take only one out of 256 values, 256 tokens can be sufficient to encode all texts. In practice this is usually combined with the BPE tokenizer. At first, the corpus is encoded as UTF-8 bytes and then BPE is ran on top of it. As most characters occur frequently, BPE would assign them a dedicated token. If the model encounters a character that didn’t exist in the training corpus (e.g., the medium skin tone waving hand), it can still represent it byte-by-byte (F0+9F+91+8B for the waving hand and F0+9F+8F+BD for the skin tone modifier).

— Appendix A, Background on Tokenization (emoji glyph dropped by extraction)

### Full extracted text (verbatim)
Complete `pdftotext` output of all 28 pages (page breaks removed). Preserved in full so any passage can be restored.

~~~~~text
Language Model Tokenizers Introduce
Unfairness Between Languages

Aleksandar Petrov, Emanuele La Malfa, Philip H.S. Torr, Adel Bibi
University of Oxford
aleks@robots.ox.ac.uk

Abstract
Recent language models have shown impressive multilingual performance,
even when not explicitly trained for it. Despite this, there are concerns
about the quality of their outputs across different languages. In this paper, we show how disparity in the treatment of different languages arises
at the tokenization stage, well before a model is even invoked. The same
text translated into different languages can have drastically different tokenization lengths, with differences up to 15 times in some cases. These
disparities persist even for tokenizers that are intentionally trained for multilingual support. Character-level and byte-level models also exhibit over 4
times the difference in the encoding length for some language pairs. This
induces unfair treatment for some language communities in regard to the
cost of accessing commercial language services, the processing time and latency, as well as the amount of content that can be provided as context
to the models. Therefore, we make the case that we should train future
language models using multilingually fair subword tokenizers.

1

Introduction

Language models are increasingly important in natural language processing tasks, as they
can understand and generate human-like language. They have been deployed in applications
such as virtual assistants (Chen et al., 2021; Ouyang et al., 2022), chatbots (Kuhail et al.,
2023; Lee et al., 2023), machine translation (Stahlberg, 2020; Ranathunga et al., 2023), and
text summarization (Kryściński et al., 2019; Xu et al., 2020). As general-purpose technologies,
it is also projected that Large Language Models (LLMs) will have a significant impact on
the economy and the labour market (Teubner et al., 2023; Eloundou et al., 2023).
Such LLMs are often trained using large swaths of internet content regardless of language.
Hence, these models often end up being multilingual, even if not by design. ChatGPT
(OpenAI, 2022) is a prominent recent example (Bang et al., 2023; Jiao et al., 2023; Johnson,
2023). Given the economic benefits of LLMs and LLM-derived technology, it’s beneficial
that they support multiple languages. Equal access is crucial, and multilingual support is a
key component of this.
However, this multilingualism is currently treated as a curious emergent phenomenon rather
than a carefully designed, controlled and managed process. The performance of LLMs has
been shown to be generally lower in non-target languages, a problem especially pronounced
for low-resource languages (Virtanen et al., 2019; Ahuja et al., 2023). Providing access to the
same technology in different languages but moderation and safety tools only for some has
resulted in dire societal consequences before (Stecklow, 2018; Facebook, 2021; Leung, 2022).
Differing cost of access could also reinforce inequality in opportunities for economic mobility
and social participation (Lythreatis et al., 2022). Therefore, as LLM multilingualism emerges,
37th Conference on Neural Information Processing Systems (NeurIPS 2023).


we should pay attention to ensuring comparable performance and accessibility across the
supported languages, regardless of whether by design or by chance.
This work demonstrates how the unequal treatment of languages arises at the tokenization
stage,1 well before the language model sees any data at all. For instance, the tokenizer
employed by ChatGPT (OpenAI, 2022) and GPT-4 (OpenAI, 2023) uses about 1.6 times
more tokens to encode the same text in Italian as it does in English, 2.6 times for Bulgarian
and 3 times for Arabic. For Shan —the native language of people from the Shan State in
Myanmar— that difference can be as high as 15 times. Unicode character and byte-level
tokenization also result in drastically different encoding lengths across languages: byte-level
representation of the same text is over 4 times longer for Burmese or Tibetan than Chinese.
We discuss three fairness implications of these differences in tokenization:
1. Cost: Commercial services charge users per token or Unicode character. In either
case, these discrepancies lead to users of some languages paying at least 2.5 times
more for the same task as users of English.
2. Latency: The number of tokens has a direct effect on the processing time for a
task. Some languages can require twice the time to process the same content as
English. This may be critical for real-time applications like emergency services.
3. Long context processing: Many models have a fixed-size context. Users of
languages that are more token-eﬀicient can use these systems to process or generate
texts that may be more than an order of magnitude longer than users of other
languages. This may lead to significant discrepancies in the quality of service.
Therefore, we make the case for multilingual tokenization parity: tokenizers should produce
similar encoded lengths for the same content across languages. Hence, we advocate for
multilingually fair tokenizers for the next generation of language models.

2

Intriguing Properties of Tokenization Across Languages

Subword tokenization is currently the preferred approach for state of the art language models
(Kudo and Richardson, 2018). In this section, we show how artefacts from data collection
might result in technical terms or rare words having dedicated tokens, while more commonly
used words and non-Latin characters end up requiring multiple tokens.
Using large corpora scraped from the internet results in peculiar choices for tokens.
For instance, GPT-2 contains glitch tokens which can be usernames or concepts
from games (Rumbelow and Watkins, 2023b; Miles and Riley, 2023). As an example,
BuyableInstoreAndOnline, likely coming from an online store backend, has a dedicated
token. Another such token is rawdownloadcloneembedreportprint.
While such obscure terms get their own tokens, the frequently used Arabic word “‫”ملاذا‬
(meaning “why”) is broken into letters with each letter having its own token. The same
word in Bulgarian (“защо”) is not only broken down to letters, but some of the letters require two tokens to be represented, resulting in 6 tokens for this 4 letter word.
5821 56434 5821 10386 8700
140 115 16142 141 231 15166
‫م‬
щ
‫ل‬
а
о
‫ذ‬
з
‫ا‬
‫ا‬
One may argue that this is because Arabic and Bulgarian are not target languages for GPT-2.
However, glitch tokens also exist for Japanese: there are dedicated tokens for “ゼウス”, the
name of the ancient Greek god Zeus and “サ–ティワン”, the name of an ice cream chain
(Rumbelow and Watkins, 2023a). At the same time, GPT-2 requires 3 tokens to represent
the much more commonly used kanji character for “to say”:
164 101 222
言
In fact, more than half of the Japanese kanji characters require three tokens.
1

We offer a summary of the relevant tokenization approaches in Appendix A.

2


The existence of glitch tokens like “ゼウス” and “サ–ティワン” despite the lack of a dedicated
token for “言” shows that tokenizers are heavily influenced by the biases of the corpus source.
If one uses non-natural inputs, log files, or specialist forums, the tokenizer vocabulary would
reflect this. While cl100k_base, the tokenizer used for the newer ChatGPT and GPT-4,
may not have glitch tokens it still requires two tokens to represent some Cyrillic letters and
three tokens for more than 65% of kanji characters. Therefore, to place all languages on an
equal footing, it is important to have the tokens balanced across languages.

3

Measuring Tokenizer Parity

To demonstrate that the above examples are not anecdotal evidence, we introduce the notion
of tokenizer parity to systematically assess how fairly tokenizers treat equivalent sentences
in different languages. Parity occurs when a tokenizer exhibits similar tokenized lengths
for the same sentence in different languages. Take a sentence sA in language A and its
translation sB to language B. Then, a tokenizer t achieves parity for A with respect to B
at sA and sB if |t(sA )|/|t(sB )| ≈ 1, where t(sA ) is the tokenization of the sentence sA and
|t(sA )| represents its length. The ratio |t(sA )|/|t(sB )| is the premium for A relative to B. 2

4

Tokenization Length Differences Across Languages

Languages vary significantly in the number of tokens required to encode the same content,
as demonstrated in the examples in Section 2. Hence, following Section 3, we measure the
tokenization premium of different tokenizers. To this end, we use the FLORES-200 parallel
corpus, comprising of the same 2000 sentences taken from Wikipedia and human-translated
to 200 different languages (Guzmán et al., 2019; Goyal et al., 2021; Costa-jussà et al., 2022).
We look at subword tokenization models which target English, languages other than English,
language varieties, multi-lingual tokenizers, as well as tokenizer-free (byte-level) modelling.
4.1

Parity for English-centric Models

Table 1: Premiums with respect to English on FLORES-200 for several EnglishAs most models target English, we report in centric models. The languages in the top
Table 1 the tokenization parity for a subset of or bottom three for any tokenizer, as well as
languages in FLORES-200. The parities for the ones discussed in the text, are shown.
all 200 languages are in Appendix C. 3 GPT2 (Radford et al., 2019), RoBERTa (Liu et al.,
GPT-2 ChatGPT
FlanT5
RoBERTa
GPT-4
2019), and the r50k_base, p50k_base and
p50k_edit tokenizers (OpenAI, 2022) have Bulgarian
5.51
2.64
—
16.89
11.70
—
close4 tokenization lengths so we report them Burmese
3.21
1.91
—
together. ChatGPT and GPT-4 share the Chinese (Simplified)
16.36
12.33
—
same cl100k_base tokenizer and are also Dzongkha
English
1.00
1.00
1.00
reported together. Some models, such as French
2.00
1.60
1.60
2.14
1.58
1.37
FlanT5 (Chung et al., 2022), use a special UNK German
2.01
1.64
2.18
token to model unknown symbols not encoun- Italian
Japanese
3.00
2.30
—
tered during training. Hence, to ensure a fair Jingpho
2.65
2.35
3.41
comparison, we report only languages where Maori
2.45
2.35
3.28
1.86
1.56
2.24
no more than 10% of the input characters are Norwegian Bokmål
Odia
13.38
12.48
—
mapped to UNK tokens (marked with —).
Table 1 shows large variations in the tokenizer
parity for all tokenizers. For GPT-2 and
RoBERTa, Pangasinan, the language with
shortest tokenization, is already 66% more expensive to process than English. ChatGPT
and GPT-4 are slightly closer to parity, likely

Pangasinan
Portuguese
Romanian
Santali
Shan
Spanish
Standard Arabic
Tumbuka
Vietnamese

1.66
1.94
2.48
12.86
18.76
1.99
4.40
2.78
4.54

1.57
1.48
1.88
12.80
15.05
1.55
3.04
2.57
2.45

2.18
2.21
1.50
—
—
2.23
—
3.29
—

2
The concurrent work by Ahia et al. (2023) also evaluates the tokenization premiums for different
languages and reaches similar conclusions.
3
An interactive table of all the languages and tokenizers is also available on the project website.
4
The largest tokenizer parity difference between them is less than 0.005.

3


Table 2: Tokenizer premiums on the FLORES-200 dataset for
non-English centric models. The premium is computed with
respect to the target language (Modern Standard Arabic was
used for Arabic BERT and Simplified Chinese for RoCBert). The
languages that are in the top or bottom two for any tokenizer as
well as the ones discussed are shown.
Arabic RoCBert CamemBERT GottBERT
BERT
PhoBERT
BERT (Chinese)
(French) (German) Japanese (Vietnamese)
Belarusian
Bulgarian
Catalan
Chinese (Simp.)
Chinese (Trad.)
Dutch
Dzongkha
English
French
Friulian
German
Greek
Italian
Japanese
Jingpho
Luxembourgish
N. Lev. Arabic
Shan
Standard Arabic
Tagalog
Tosk Albanian
Tsonga
Tumbuka
Vietnamese
Yue Chinese

4.74
4.30
2.36
—
—
2.52
—
1.83
2.42
2.33
2.63
4.93
2.58
1.85
3.12
2.56
1.00
—
1.00
2.84
2.66
3.01
3.27
2.52
—

—
—
2.86
1.00
0.94
2.92
—
2.60
3.10
2.79
3.12
3.00
3.10
1.34
3.12
2.97
—
—
—
3.28
2.90
3.09
3.49
2.55
0.92

—
—
1.59
—
—
1.68
—
1.20
1.00
1.66
1.85
—
1.63
—
2.13
1.82
—
—
—
2.00
2.17
2.03
2.21
—
—

5.62
4.73
1.89
3.95
3.82
1.73
16.12
1.35
1.99
1.98
1.00
6.73
1.93
4.35
2.55
1.75
6.52
16.88
7.03
2.20
2.39
2.29
2.61
4.12
3.75

—
—
1.95
0.82
0.84
1.98
—
1.49
2.03
1.92
2.04
—
2.04
1.00
2.47
1.96
—
—
—
2.39
—
2.46
—
—
—

3.46
3.09
1.57
—
—
1.58
—
1.20
1.66
1.59
1.67
3.73
1.60
—
1.84
1.72
—
—
—
1.74
2.02
1.76
2.00
1.00
—

Table 3:
Tokenizer
premiums
on
the
FLORES-200
dataset
for the MuRIL model
focusing on 16 Indian
languages and English. The premium is
computed with respect
to English.
MuRIL
English
Nepali
Bengali
Tamil
Marathi
Kannada
Hindi
Malayalam
Gujarati
Sanskrit
Telugu
Odia
Sindhi
Assamese
Urdu
Eastern Panjabi
Kashmiri (Arabic)
Kashmiri (Devanagari)

1.00
1.01
1.01
1.06
1.06
1.06
1.16
1.18
1.19
1.21
1.21
1.21
1.22
1.24
1.26
1.35
1.75
1.75

due to their larger vocabulary size. However, the cheapest languages, Portuguese, Pangasinan and German, still see a premium of 50% when compared to English. Shan has the worst
tokenizer parity for all four models. Take as an example “မ
ႂ ်း”, one of the Shan words for
“you”. It is tokenized by ChatGPT and GPT-4 as:
25870 247 157 224 224 25870 118 25870 116
ႂ◌
◌်
◌း
မ

This word is constructed from one consonant and three diacritics. As the diacritics are
encoded separately, there are four Unicode codepoints for this Shan character, resulting in
9 tokens. The English “you” has three characters but a single token.
FlanT5 has more than 10% UNK tokens for 42% of languages (— in Table 1). It has a higher
premium than the other tokenizers for all other languages except German and Romanian.
Summary. All four English-centric tokenizers we consider are far from tokenization parity.
Portuguese is closest to parity with English for the ChatGPT and GPT-4 tokenizer but still
requires about 50% more tokens for the same content. Shan is furthest from parity for this
tokenizer with 15 times longer encodings compared to English. FlanT5 is closer to parity
with its premium range 1.37–3.41 but it encodes only 54% of the languages, so we cannot
say that it is more multilingually fair than the other tokenizers.
4.2

Parity for Models with Other Target Languages

There are models targeting languages other than English as well. Table 2 shows six such
models based on the BERT architecture (Devlin et al., 2019): ArabicBERT (Safaya et al.,
2020), RoCBert for Chinese (Su et al., 2022), CamemBERT for French (Martin et al., 2020),
GottBERT for German (Scheible et al., 2020), BERT Japanese (Tohoku NLP Group, 2019)
and PhoBERT for Vietnamese (Nguyen and Nguyen, 2020).
4


Table 4: Tokenizer premiums with respect
to English on FLORES-200 for multilingual
models. The languages that are in the top or
bottom two for any tokenizer, as well as the
ones discussed in the text, are shown.

Table 5: Tokenizer premiums with respect
to English on FLORES-200 for byte-level
models. The languages that are in the top
or bottom two for any tokenizer, as well as
the ones discussed in the text, are shown.

XLM-R NLLB mT5 M2M100 BLOOM

CANINE
ByT5
UTF-32 bytes UTF-8 bytes

Bulgarian
Central Kanuri
Chinese (Simp.)
Dzongkha
English
Indonesian
Italian
Japanese
Kabiyè
Santali
Shan
Std. Arabic
Std. Tibetan
Uyghur
Yue Chinese

1.16
2.60
0.97
—
1.00
0.94
1.19
1.11
2.98
—
4.43
1.18
—
1.41
0.93

1.31 1.28
2.54 2.43
1.11 0.92
1.48 4.24
1.00 1.00
0.93 1,08
1.25 1.34
1.01 0.90
1.56 2.83
2.49 —
1.94 3.28
1.40 1.35
1.44 3.68
1.40 2.57
1.05 0.95

1.23
2.49
1.05
—
1.00
0.98
1.25
1.20
2.71
—
4.63
1.29
—
3.00
1.03

2.49
2.10
0.95
7.36
1.00
0.96
1.62
1.81
3.34
12.71
12.06
1.14
6.66
3.67
0.93

Bulgarian
Burmese
Chinese (Simplified)
Chinese (Traditional)
Dzongkha
English
Italian
Japanese
Shan
Standard Arabic
Standard Tibetan
Tok Pisin
Tumbuka
Yue Chinese

1.04
1.24
0.34
0.32
1.25
1.00
1.18
0.44
1.42
0.88
1.13
1.28
1.30
0.31

1.89
3.51
0.93
0.89
3.64
1.00
1.19
1.27
3.94
1.60
3.31
1.28
1.32
0.87

The English premium for GottBERT (1.35) is lower than those for Dutch (1.73) and Luxembourgish (1.75), which are more linguistically similar to German. CamemBERT is similar:
English has the lowest premium (1.20), while Catalan (1.59) and Friulian (1.66) have higher
premiums. PhoBERT also has English with the lowest tokenizer premium (1.20). Thus,
even models targeting other languages exhibit a preference for English tokenization.
RoCBert and BERT Japanese differ by having the other target language as the one closest
to parity, possibly due to the partially shared script. ArabicBERT demonstrates a similar
behaviour, with Central Kanuri (1.27) and Acehnese (1.73), both written in Arabic script,
and with English at 1.82. Sharing writing systems seems to improve tokenization parity.
Across all tokenizers, the premium for English relative to the respective target language is
significantly lower than the premium of RoBERTa for that target language. This asymmetry
between English and all other languages likely stems from the extensive incorporation of
English in documents written in other languages (Zhang et al., 2022).
We also consider MuRIL, a BERT-based model trained on 16 Indian languages and English
(Khanuja et al., 2021). Despite the model’s focus on Indian languages, it remains most
token-eﬀicient for English (see Table 3).
Unequal treatment of dialects or linguistic varieties can lead to social and economic disadvantages making it important to also study the tokenization differences between the “standard”
language and its varieties. For Swiss German and the Mauritian and Haitian Creoles, there
are large differences in tokenization lengths compared respectively to High German (on GottBERT) and French (on CamemBERT). English is much closer to parity for both models
than these language varieties. Therefore subword tokenizers might not be able to generalize to language varieties, such as dialects and creoles. The tokenizers of ArabicBERT
and BERT Japanese, however, are close to parity across various dialects of both languages
and have lower premiums for the dialects than for English. This is likely due to the good
representation of the dialects in the dataset as well as the dialects being linguistically closer
to the respective standard languages. The detailed analysis is deferred to Appendix B.
Summary. We observed that the tokenizers targeting French, German and Vietnamese
have English as the language closest to parity, rather than more linguistically close languages.
On the other hand, tokenizers for Arabic, Chinese and Japanese have lower premiums for
languages they share a script with. Notably, despite targeting Indian languages, MuRIL still
has the shortest tokenizations for English. Finally, across all tokenizers, the premium for
English is lower than the premium for the same language for the English-centric RoBERTa.
Hence, we conclude that tokenizers for other languages give English preferential treatment.
5


Shan
Tamil

24

Burmese
Dzongkha
22

RoBERTa execution time [s]

Asturian
Bulgarian
Burmese
Catalan
Central Kanuri (Arabic sc.)
Central Kurdish
Chinese (Simplified)
Chinese (Traditional)
Danish
English
Fon
Galician
Georgian
Haitian Creole
Indonesian
Italian
Japanese
Javanese
Kabiyè
Kannada
Khmer
Kikuyu
Lao
Malayalam
Meitei (Bengali sc.)
Norwegian Bokmål
Norwegian Nynorsk
Nuer
Odia
Pangasinan
Shan
Std. Arabic
Std. Malay
Swedish
Tajik
Tamil
Telugu
Thai
Turkish
Yoruba
Yue Chinese

Odia

20

Santali
Sango
18

Hebrew

Script family:

French
Bulgarian
Standard
German
Arabic
Italian

16
Portuguese

English

RoBERTa
XLM-RoBERTa
1

5

10
Tokenization premium

14

Spanish
Malay

15

0.0

Arabic
Armenian
Northern Brahmi
Southern Brahmi
CJK
Greek
Ge ez
Georgian
Hebrew
Berber

Korean
Japanese

Vietnamese
Chinese (Simp.)
Yue Chinese
Chinese (Trad.)
Zulu
0.2

0.4

Bhojpuri

0.6

0.8

Tokenisation length for the FLORES-200 parallel corpus

1.0
1e6

Figure 1: Comparison of the tokenization pre- Figure 2: Average processing time and length
miums for XLM-R and RoBERTa for the sub- of the tokenized inputs of RoBERTa. Each
set of languages that XLM-R encodes with FLORES-200 sentence is processed for 20 inless than 10% to the UNK token.
dependent runs. The script family designation is only for illustration purposes.
4.3

Parity for Multilingual Models

There has been a growing interest in multilingual language models, particularly for translation (Dabre et al., 2020). As these models are intended to support a variety of languages,
one would expect them to be close to tokenizer parity. We compare several such multilingual models: XML-R (Conneau et al., 2020), NLLB (Costa-jussà et al., 2022), M2M100
(Fan et al., 2021) and mT5 (Xue et al., 2020). All of these models use the SentencePiece
tokenizer with upsampling for rare languages. The final model, BLOOM (Scao et al., 2022),
uses byte-level BPE instead of SentencePiece and is designed to maintain similar ratios of
tokens per word for each language as reference monolingual tokenizers.
BLOOM and NLLB encode all languages with less than 10% UNK tokens, respectively thanks
to byte-level BPE tokenization and being trained on the same 200 languages as FLORES200 (see Table 4). The other three models fail to encode at least one language. All five
models have languages with premiums of more than 2.5. Still, all models are better than
the English-centric models in Table 1. Figure 1 shows how XLM-R is much closer to parity
than RoBERTa (on which it is based), over all languages it can encode. However, none of
the models uniformly reaches parity across all languages. Therefore even models which are
intentionally designed to be multilingual suffer from a lack of tokenization parity.
Summary: Multilingual models can improve the tokenization parity for different languages but challenges remain in achieving tokenization parity across all languages.
4.4

Parity for Byte-level Tokenization Models

Byte-level representation is crucial for multilingual support, as it encodes any Unicode
codepoint, even if unseen during training. One can also bypass vocabulary construction and
directly employ the 256 byte values, enabling end-to-end training (byte-level tokenization).
CANINE (Clark et al., 2022) is a large model that operates at the Unicode codepoint level
rather than the byte level. The CANINE tokenizer is thus equivalent to the UTF-32 encoding, resulting in an implicit tokenizer with a vocabulary of 1,114,112. ByT5 (Xue et al.,
2022), on the other hand, uses the UTF-8 encoding: an implicit vocabulary of 256 tokens.5
5
To be consistent, we will refer to the characters and bytes in the encoding of the CANINE and
ByT5 tokenizers as tokens as they fulfil a similar role.

6


These byte-level models can represent any Unicode codepoint without an explicit tokenization step but there are still significant tokenization disparities. For CANINE, Shan has a
premium of 4.58 relative to Yue Chinese. This can be attributed to the fact that CANINE
provides a single token for each Unicode codepoint, which results in Chinese being more
token-eﬀicient (with a premium range 0.31–0.34 relative to English for the three Chinese
languages) as each character is treated as a single token. This encoding also puts Shan at a
disadvantage, as its encoding relies on diacritics represented as separate Unicode codepoints.
Other languages, such as Tok Pisin and Tumbuka, which use the Latin script but require
more characters than English for the same text, also face similar challenges.
Tokenization disparity is also present in the ByT5 model. The tokenization premium for
ByT5 ranges from 0.87 (for Yue Chinese) to 3.94 (for Shan). The introduction of the variablewidth UTF-8 encoding of Unicode characters in ByT5 creates another issue of unequal
treatment. ASCII characters, which are suﬀicient for English, require only one byte. Other
Latin script characters, as well as Greek, Cyrillic, Coptic, Armenian, Hebrew, Arabic and
Syriac, require two bytes, while Chinese, Japanese and Korean characters require three
bytes. Therefore, the tokenization of Chinese and Japanese is about three times as long
for ByT5 as it is for CANINE (Table 5). Shan’s premium of 3.94 is due to the fact that
all its consonants and diacritics require three bytes. For example, the word “မ
ႂ ်း” is encoded
by ByT5 as 12 tokens, whereas the corresponding “you” requires 3 tokens. The situation is
similar for other languages like Dzongkha, Tibetan and Burmese.
Summary. Byte-level models also fail to achieve parity among the languages from
FLORES-200 exhibiting a premium of over 4 times for some language pairs. There are
two sources of multilingual tokenizer disparities. First, there are natural differences in the
number of characters used in different languages to communicate the same content. Second,
the UTF-8 standard uses different number of bytes to encode codepoints of different scripts.

5

Fairness Implications of Tokenization Length Differences

We showed that no matter whether one uses subword, multilingual, or byte-level tokenization, none of the tokenizers gets close to parity for all languages in FLORES-200. This lack
of tokenization parity is not merely a curiosity: it leads to unfairness in the cost to access
language models, the latency of the service and the amount of data that can be processed.
5.1

Cost

It is increasingly common to access LLMs as paid API services. One pricing approach, employed by OpenAI at the time of writing,6 is to charge per token. Therefore, the tokenization
premiums discussed in Section 4 directly map to cost premiums. For ChatGPT and GPT-4,
the cost to process a text in German or Italian is about 50% higher than to process the
same text in English (Table 1). Using them in Dzongkha, Odia, Santali or Shan, the most
expensive languages for these services, costs more than 12 times more than in English.
Another pricing strategy is per Unicode character: the approach currently taken by the
Google Cloud Natural Language service.7 However, as we showed in Section 4.4, the same
content can have very different lengths when measured in Unicode characters. Burmese,
Dzongkha, Shan, Tok Pisin or Tumbuka require more than 4 times more characters than
Yue Chinese for the same text, resulting in a proportional cost difference. Therefore, both
the per-token and the per-character approaches result in large disparities in the cost for
users of different languages to use the exact same service.
5.2

Latency

High latency of real-time interactions for users of certain languages can result in a suboptimal
experience and communication breakdowns. For customer support or emergency services,
delays in response time can lead to miscommunication or delayed assistance.
6
7

https://openai.com/pricing
https://cloud.google.com/natural-language/pricing

7


As some languages have significantly longer tokenized inputs, they would also experience
longer processing times. The transformer attention mechanism has a quadratic complexity
in the number of input tokens (Keles et al., 2023). However, the full model architecture
contains other submodules and therefore the overall complexity might be different.
To assess the effect of the tokenization length on the latency, in Figure 2 we plot the computation time of RoBERTa against the tokenization lengths. It appears that the processing
time is linear in the tokenization length rather than quadratic, showing a strong correlation between sequence length and execution time. Therefore, tokenization disparities across
languages also affect the latency and processing time for text in these languages.
As expected, English is on the left lower corner, having the shortest tokenization and one
of the fastest processing times. Shan is on the other extreme with the longest tokenization length and execution time (almost twice that of English). We can also observe clear
trends dependent on the script used. Latin script and other Greek-derived scripts show the
shortest tokenization lengths and processing times followed by the Chinese-Japanese-Korean
(CJK) and Arabic languages. Other predominantly Asian and African scripts have longer
tokenization lengths and processing times.
The latency implications of tokenization disparity are not limited to text models. Speech
recognition models often produce a series of tokens as their output sequentially. Similarly,
speech synthesis takes as an input tokenized text (Latif et al., 2023). Therefore, differences
in tokenization affect speech models too.
5.3

Long context processing

Transformers models have diﬀiculty processing long inputs (Liu et al., 2023). Given that
the size of the input is contingent upon the tokenization process, inputs of greater length
may impose a challenge for language models to adequately reason over. Such a predicament
may result in reduced abilities or limited applicability for languages with high tokenization
premiums. For example, RoBERTa has a fixed block size of 512, GPT-2 has 768, 1024, 1280,
or 1600 Radford et al. (2019), GPT-4 comes in 8,000 and 16,000 context variants.8 These
models cannot process inputs longer than that. Therefore, one can process less than a tenth
of the content in languages like Burmese and Dzongkha than they can in English.
Alongside inconveniencing the users of these languages, this can also result in diminished
performance on automated systems, such as content moderation. Reliable content moderation is crucial for tackling hate speech and diminished performance has already been
shown to fail to prevent its spread (Stecklow, 2018; Facebook, 2021). Therefore, reduced
long context capabilities for some languages could have severe real-world impacts.

6

Towards Multilingual Tokenization Fairness

Section 5 showed that high values of tokenization parity for a language lead to increased cost
and latency and decreased capacity for long context processing. In this section, we argue
that training language models from scratch with a multilingually fair subword tokenizer is
the only approach that can effectively address all these aspects of tokenization unfairness.
Subword tokenization is necessary to achieve parity. In Section 4.4, we showed that
neither character-level nor byte-level input representation can achieve tokenization parity.
Therefore, a variation of subword tokenization is necessary. For example, Chinese characters
could be individual tokens, Latin characters might be represented as tokens with an average
length of about 3 characters while pairs of Burmese characters and their diacritics being
assigned single tokens. Such an approach would account for Chinese requiring one-third the
characters English does (as shown in Table 5).
A separate tokenizer for determining the processing cost is not suﬀicient. An
easy patch for existing models is to use a separate tokenizer for calculating how much a
user should be charged. Using one tokenizer for computing the cost and another to process
8

https://openai.com/pricing

8


80000

Figure 3: How much longer will English
language tokenization be if we dedicate
a fraction of the cl100k_base vocabulary to other languages? This plot
shows how many tokens will be necessary to encode the English language corpus of FLORES-200 for different subsets of the cl100k_base vocabulary.

Tokens necessary to encode FLORES-200

78000
76000
74000
72000
70000
68000
66000
64000
62000
60000

A 10-fold reduction in the vocabulary
would result in only
30% longer sequences for English.
With one-third of the vocabulary,
English sequences will become
just 10% longer for ChatGPT/GPT-4

58000
56000
54000
52000
0

10000 20000 30000 40000 50000 60000 70000 80000 90000100000
Vocabulary size

the input can easily be applied to existing systems without the need to retrain the LLM
itself. However, as the tokenizer for the language model is unchanged, this approach would
still suffer from latency and inability to process long contexts. Therefore, to ensure similar
processing times and long context capabilities across languages, the language model has to
be trained with a multilingually fair tokenizer.
The tokenization needs to support all Unicode codepoints. Amongst all tokenizers
we examine in this paper, the ones which encode all FLORES-200 languages all have one
thing in common: they build their tokenization on top of Unicode representation, allowing
them them to represent all characters. Therefore, a multilingually fair tokenizer should also
start from a Unicode (or equivalent) encoding. Considering that subword tokenization is
necessary, building the vocabulary from UTF-8 would likely result in a smaller dictionary
than building it on top of UTF-32. Hence, UTF-8 is likely the more appropriate choice.
Building a multilingually fair parallel corpus. Building and evaluating multilingually
fair tokenizers requires attention to the parallel corpus used. One must ensure a balanced
representation of topics, otherwise, the resulting tokenizer might end up being multilingually
fair only for a subset of topics. The presence of named entities must also be balanced. For
example, in FLORES-200, there are many English-centric names and institutions, which
might skew the results in favour of English. Additionally, the same sentence can have
different translations with varying tokenization lengths. To account for this, a diversity of
translations could ensure tokenization fairness across languages. These limitations also hold
for the results in this paper. Hence, developing a well-curated and diverse parallel corpus is
crucial for the development and evaluation of a multilingually fair tokenizer.
Building a multilingually fair tokenizer from monolinugal tokenizers. As discussed in Section 4, byte-level, character-level and word-level tokenizers cannot achieve
tokenization parity and subword tokenization is needed. However, simply training a subword tokenizer on a balanced dataset is also not suﬀicient as languages can share tokens. For
example, “hotel” is written the same way in English, Spanish, Italian, Portuguese, Dutch,
Danish, Hungarian, Polish, etc. Hence, languages from more numerous language families
will also witness shorter tokenization lengths while more isolated languages and scripts, e.g.
Korean, would see larger language premiums: “hotel” in Korean is “호텔” and no other
language has the same spelling as no other language uses the Korean script.
To address this issue, we suggest a two-stage process towards building a multilingually fair
tokenizer. First, train individual monolingual tokenizers for all target languages. Then,
merge them while maintaining parity. The merging can be done by starting with the 256
tokens corresponding to each value a byte can take and then repeatedly adding the most
frequently used token for the language with the highest premium.
While a multilingually fair tokenizer would lead to more tokens being needed for the dominant language, this additional cost would likely be much smaller than the benefit for the
rest of the languages. The vocabulary size has diminishing returns: the additional tokens
correspond to increasingly rare (parts of) words. For example, with only a third of the vocab9


ulary, English sequences will become just 10% longer for ChatGPT/GPT-4 (see Figure 3).
Therefore, by removing rarely used tokens of the dominant language and replacing them
with frequently used tokens in other languages, we would likely see an overall net benefit.

7

Related Works

Fairness and bias in language models. The rapid increase in the size of language
models has raised concerns regarding their biases and unfairness (Bender et al., 2021). For
example, Bolukbasi et al. (2016), May et al. (2019) and Nadeem et al. (2021) showed that
stereotypes and biases exist in language models, while Magee et al. (2021) identified the
presence of intersectional biases which may be resistant to debiasing techniques. Language
models were also shown to rely on social biases in question answering (Parrish et al., 2022).
Another challenge is the generation of toxic content which can occur even without prompting
(Gehman et al., 2020). Interestingly, Gururangan et al. (2022) point out that datasets
consider one type of English as a higher quality depending on the location of the writer
rather than on factuality or literary acclaim. Moreover, Ramesh et al. (2023) and Levy
et al. (2023) highlighted the need to consider fairness issues of languages other than English,
as they may have distinct sources of bias and solutions for English may not be applicable.
Multilingual performance. One approach towards similar multilingual performance is
to frame languages as entities as recently proposed by Choudhury and Deshpande (2021).
Another method is to separately train vocabularies for different language clusters to balance
cross-lingual and language-specific tokens (Chung et al., 2020). Still, multilingual models
struggle to deliver on the promises of deep transfer learning for lower-resourced languages
(Virtanen et al., 2019) and perform differently depending on the script and resource level of
the language (Bang et al., 2023). Ahuja et al. (2023) found that generative models perform
better on higher-resource languages and languages that use the Latin script, possibly due
to the context length restrictions for some languages. Zhang et al. (2022) show that a
balanced tokenizer corpus results in better translation performance. Separately, Hofmann
et al. (2021, 2022) show that the BPE results in suboptimal token choices even for English
and demonstrate that addressing this issue boosts performance. Similarly, Rajab (2022) and
Oladipo et al. (2022) discuss how tokenization affects performance for African languages.
Measuring tokenization lengths. Zhang et al. (2022) suggested using the ratio of the
average sentence length in tokens to the length in characters as a measure of closeness to the
character level. However, this method may not be suitable for comparing languages due to
differences in sentence length across languages. On the other hand, Ács (2019) and Scao et al.
(2022) measure the number of tokens created per word, but this method may not be effective
for comparing languages due to differences in semantic content per word and the lack of
word delineation in some languages. Rust et al. (2021) show that mBERT (Devlin et al.,
2019) breaks down English words the least, in line with our findings of English receiving
special treatment. However, to the best of our knowledge, we are the first to leverage a
parallel corpus to compare tokenization lengths across languages.

8

Conclusion

This paper highlights the significant disparities in tokenization across different languages
which can lead to unequal treatment and disadvantages for certain language communities.
The findings reveal that even tokenizers explicitly trained for multilingual support exhibit
tokenization lengths that vary by up to a factor of 13. Furthermore, character-level and
byte-level models also demonstrate encoding length discrepancies that are more than 4
times longer. These disparities have important real-world implications including increased
costs for accessing commercial language services, longer processing times and limitations on
the amount of contextual information provided to language models. To address these issues,
we propose the development of multilingually fair tokenizers for future language models
emphasizing the importance of ensuring comparable performance and accessibility across
supported languages. By achieving tokenization parity, we can mitigate inequalities and
promote fair access to language technologies across diverse linguistic communities.
10


Acknowledgements
We would like to thank Puyu Wang, Francisco Eiras, Ambre Bertrand and Carmen Scheidemann for their linguistic advice. Janet Pierrehumbert introduced us to many relevant prior
works. We also extend special gratitude to Shinnosuke Takamichi and Hiroshi Saruwatari
for open-sourcing the CPJD corpus for this project. Finally, we thank the reviewers; their
feedback greatly improved this manuscript.
AB has received funding from the Amazon Research Awards. This work is supported by a
UKRI grant Turing AI Fellowship (EP/W002981/1) and the EPSRC Centre for Doctoral
Training in Autonomous Intelligent Machines and Systems (EP/S024050/1). We also thank
the Royal Academy of Engineering and FiveAI.

References
Ahmed Abdelali, Francisco Guzman, Hassan Sajjad, and Stephan Vogel. 2014. The AMARA
corpus: Building parallel language resources for the educational domain. In Proceedings
of the Ninth International Conference on Language Resources and Evaluation (LREC’14).
European Language Resources Association (ELRA).
Orevaoghene Ahia, Sachin Kumar, Hila Gonen, Jungo Kasai, David R. Mortensen, Noah A.
Smith, and Yulia Tsvetkov. 2023. Do all languages cost the same? Tokenization in the
era of commercial language models. arXiv preprint arXiv:2305.13707.
Kabir Ahuja, Rishav Hada, Millicent Ochieng, Prachi Jain, Harshita Diddee, Samuel Maina,
Tanuja Ganu, Sameer Segal, Maxamed Axmed, Kalika Bali, and Sunayana Sitaram. 2023.
MEGA: Multilingual evaluation of generative AI. arXiv preprint arXiv:2303.12528.
Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin,
Chang Zhou, and Jingren Zhou. 2023. Qwen-VL: A versatile vision-language model for
understanding, localization, text reading, and beyond. arXiv preprint arXiv:2308.12966.
Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy
Lovenia, Ziwei Ji, Tiezheng Yu, Willy Chung, Quyet V. Do, Yan Xu, and Pascale Fung.
2023. A multitask, multilingual, multimodal evaluation of ChatGPT on reasoning, hallucination, and interactivity. arXiv preprint arXiv:2302.04023.
Loïc Barrault, Yu-An Chung, Mariano Cora Meglioli, David Dale, Ning Dong, PaulAmbroise Duquenne, Hady Elsahar, Hongyu Gong, Kevin Heffernan, John Hoffman, et al.
2023. SeamlessM4T – massively multilingual & multimodal machine translation. arXiv
preprint arXiv:2308.11596.
Reem Bassiouney. 2009. Arabic Sociolinguistics. Edinburgh University Press.
Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell.
2021. On the dangers of stochastic parrots: Can language models be too big? In
Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency.
Yoshua Bengio, Réjean Ducharme, and Pascal Vincent. 2000. A neural probabilistic language
model. Advances in Neural Information Processing Systems.
Tolga Bolukbasi, Kai-Wei Chang, James Y Zou, Venkatesh Saligrama, and Adam T Kalai.
2016. Man is to computer programmer as woman is to homemaker? Debiasing word
embeddings. In Advances in Neural Information Processing Systems.
Houda Bouamor, Nizar Habash, Mohammad Salameh, Wajdi Zaghouani, Owen Rambow,
Dana Abdulrahim, Ossama Obeid, Salam Khalifa, Fadhl Eryani, Alexander Erdmann,
et al. 2018. The MADAR Arabic dialect corpus and lexicon. In Proceedings of the
Eleventh International Conference on Language Resources and Evaluation (LREC 2018).
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto,
Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. 2021.
Evaluating large language models trained on code. arXiv preprint arXiv:2107.03374.
11


Monojit Choudhury and Amit Deshpande. 2021. How linguistically fair are multilingual
pre-trained language models? In Proceedings of the AAAI Conference on Artificial Intelligence.
Hyung Won Chung, Dan Garrette, Kiat Chuan Tan, and Jason Riesa. 2020. Improving
multilingual models with language-clustered vocabularies. In Proceedings of the 2020
Conference on Empirical Methods in Natural Language Processing (EMNLP).
Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Eric Li,
Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, et al. 2022. Scaling instructionfinetuned language models. arXiv preprint arXiv:2210.11416.
Junyoung Chung, Kyunghyun Cho, and Yoshua Bengio. 2016. A character-level decoder
without explicit segmentation for neural machine translation. In Proceedings of the 54th
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers).
Jonathan H. Clark, Dan Garrette, Iulia Turc, and John Wieting. 2022. Canine: Pre-training
an Eﬀicient Tokenization-Free Encoder for Language Representation. Transactions of the
Association for Computational Linguistics.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Édouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020. Unsupervised cross-lingual representation learning at scale. In Annual Meeting
of the Association for Computational Linguistics.
Marta R Costa-jussà, James Cross, Onur Çelebi, Maha Elbayad, Kenneth Heafield, Kevin
Heffernan, Elahe Kalbassi, Janice Lam, Daniel Licht, Jean Maillard, et al. 2022. No
language left behind: Scaling human-centered machine translation. arXiv preprint
arXiv:2207.04672.
Raj Dabre, Chenhui Chu, and Anoop Kunchukuttan. 2020. A survey of multilingual neural
machine translation. ACM Computing Surveys.
Raj Dabre and Aneerav Sukhoo. 2022. MorisienMT: A dataset for Mauritian Creole machine
translation. arXiv preprint arXiv:2206.02421.
Michel DeGraff. 2007. Kreyòl Ayisyen, or Haitian Creole (Creole French).
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pretraining of deep bidirectional transformers for language understanding. In Conference of
the North American Chapter of the Association for Computational Linguistics: Human
Language Technologies.
Pelin Dogan-Schönberger, Julian Mäder, and Thomas Hofmann. 2021. SwissDial: Parallel
multidialectal corpus of spoken Swiss German. arXiv preprint arXiv:2103.11401.
Tyna Eloundou, Sam Manning, Pamela Mishkin, and Daniel Rock. 2023. GPTs are GPTs:
An early look at the labor market impact potential of large language models. arXiv
preprint arXiv:2303.10130.
Facebook. 2021. Sri Lanka human rights impact assessment. Accessed on April 11, 2023.
Angela Fan, Shruti Bhosale, Holger Schwenk, Zhiyi Ma, Ahmed El-Kishky, Siddharth Goyal,
Mandeep Baines, Onur Celebi, Guillaume Wenzek, Vishrav Chaudhary, et al. 2021. Beyond English-centric multilingual machine translation. The Journal of Machine Learning
Research.
Philip Gage. 1994. A new algorithm for data compression. C Users Journal.
Yingqiang Gao, Nikola I. Nikolov, Yuhuang Hu, and Richard H.R. Hahnloser. 2020.
Character-level translation with self-attention. In Proceedings of the 58th Annual Meeting
of the Association for Computational Linguistics.
12


Samuel Gehman, Suchin Gururangan, Maarten Sap, Yejin Choi, and Noah A. Smith. 2020.
RealToxicityPrompts: Evaluating neural toxic degeneration in language models. In Findings of the Association for Computational Linguistics: EMNLP. Association for Computational Linguistics.
Naman Goyal, Cynthia Gao, Vishrav Chaudhary, Peng-Jen Chen, Guillaume Wenzek,
Da Ju, Sanjana Krishnan, Marc’Aurelio Ranzato, Francisco Guzmán, and Angela Fan.
2021. The FLORES-101 evaluation benchmark for low-resource and multilingual machine
translation. Transactions of the Association for Computational Linguistics.
Suchin Gururangan, Dallas Card, Sarah K. Dreier, Emily K. Gade, Leroy Z. Wang,
Zeyu Wang, Luke Zettlemoyer, and Noah A. Smith. 2022. Whose language counts
as high quality? Measuring language ideologies in text data selection. arXiv preprint
arXiv:2201.10474.
Francisco Guzmán, Peng-Jen Chen, Myle Ott, Juan Pino, Guillaume Lample, Philipp Koehn,
Vishrav Chaudhary, and Marc’Aurelio Ranzato. 2019. Two new evaluation datasets for
low-resource machine translation: Nepali-English and Sinhala-English. In Proceedings of
the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th
International Joint Conference on Natural Language Processing (EMNLP-IJCNLP).
Shiro Hattori. 1973. Japanese dialects. In Diachronic, areal, and typological linguistics.
Valentin Hofmann, Janet Pierrehumbert, and Hinrich Schütze. 2021. Superbizarre is not
superb: Derivational morphology improves BERT’s interpretation of complex words. In
Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics
and the 11th International Joint Conference on Natural Language Processing (Volume 1:
Long Papers).
Valentin Hofmann, Hinrich Schuetze, and Janet Pierrehumbert. 2022. An embarrassingly
simple method to mitigate undesirable properties of pretrained language model tokenizers.
In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics
(Volume 2: Short Papers).
Michael A. Hogg, Nicholas Joyce, and Dominic Abrams. 1984. Diglossia in Switzerland? A
social identity analysis of speaker evaluations. Journal of Language and Social Psychology.
Wenxiang Jiao, Wenxuan Wang, Jen-tse Huang, Xing Wang, and Zhaopeng Tu. 2023.
Is ChatGPT a good translator? Yes with GPT-4 as the engine. arXiv preprint
arXiv:2301.08745.
Johnson. 2023. ChatGPT is a marvel of multilingualism. The Economist.
Alan S. Kaye. 2001. Diglossia: The state of the art. International Journal of the Sociology
of Language.
Feyza Duman Keles, Pruthuvi Mahesakya Wijewardena, and Chinmay Hegde. 2023. On the
computational complexity of self-attention. In International Conference on Algorithmic
Learning Theory.
Simran Khanuja, Diksha Bansal, Sarvesh Mehtani, Savya Khosla, Atreyee Dey, Balaji
Gopalan, Dilip Kumar Margam, Pooja Aggarwal, Rajiv Teja Nagipogu, Shachi Dave,
Shruti Gupta, Subhash Chandra Bose Gali, Vish Subramanian, and Partha Talukdar. 2021. MuRIL: Multilingual representations for Indian languages. arXiv preprint
arXiv:2103.10730.
Wojciech Kryściński, Nitish Shirish Keskar, Bryan McCann, Caiming Xiong, and Richard
Socher. 2019. Neural text summarization: A critical evaluation. In Proceedings of the
2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), Hong
Kong, China.
13


Taku Kudo. 2018. Subword regularization: Improving neural network translation models
with multiple subword candidates. In Proceedings of the 56th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers).
Taku Kudo and John Richardson. 2018. SentencePiece: A simple and language independent
subword tokenizer and detokenizer for neural text processing. In Proceedings of the 2018
Conference on Empirical Methods in Natural Language Processing: System Demonstrations.
Mohammad Amin Kuhail, Nazik Alturki, Salwa Alramlawi, and Kholood Alhejori. 2023.
Interacting with educational chatbots: A systematic review. Education and Information
Technologies.
Siddique Latif, Aun Zaidi, Heriberto Cuayahuitl, Fahad Shamshad, Moazzam Shoukat,
and Junaid Qadir. 2023. Transformers in speech processing: A survey. arXiv preprint
arXiv:2303.11607.
Jason Lee, Kyunghyun Cho, and Thomas Hofmann. 2017. Fully character-level neural
machine translation without explicit segmentation. Transactions of the Association for
Computational Linguistics.
Peter Lee, Sebastien Bubeck, and Joseph Petro. 2023. Benefits, limits, and risks of GPT-4
as an AI chatbot for medicine. New England Journal of Medicine.
Heather Lent, Emanuele Bugliarello, Miryam de Lhoneux, Chen Qiu, and Anders Søgaard.
2021. On language models for creoles. In Proceedings of the 25th Conference on Computational Natural Language Learning. Association for Computational Linguistics.
Heather Lent, Kelechi Ogueji, Miryam de Lhoneux, Orevaoghene Ahia, and Anders Søgaard.
2022. What a creole wants, what a creole needs. In Proceedings of the Thirteenth Language
Resources and Evaluation Conference.
Janny Leung. 2022. Shortcuts and shortfalls in Meta’ s content moderation practices: A
glimpse from its oversight board’ s first year of operation. Comparative Law and Language.
Sharon Levy, Neha Anna John, Ling Liu, Yogarshi Vyas, Jie Ma, Yoshinari Fujinuma, Miguel
Ballesteros, Vittorio Castelli, and Dan Roth. 2023. Comparing biases and the impact of
multilingual training across multiple languages. arXiv preprint arXiv:2305.11242.
Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio
Petroni, and Percy Liang. 2023. Lost in the middle: How language models use long
contexts. arXiv preprint arXiv:2307.03172.
Yinhan Liu, Jiatao Gu, Naman Goyal, Xian Li, Sergey Edunov, Marjan Ghazvininejad,
Mike Lewis, and Luke Zettlemoyer. 2020. Multilingual denoising pre-training for neural
machine translation. Transactions of the Association for Computational Linguistics.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy,
Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. RoBERTa: A robustly optimized bert pretraining approach. arXiv preprint arXiv:1907.11692.
Georges Lüdi. 2007. The Swiss model of plurilingual communication. Receptive multilingualism: Linguistic analyses, language policies and didactic concepts.
Sophie Lythreatis, Sanjay Kumar Singh, and Abdul-Nasser El-Kassar. 2022. The digital
divide: A review and future research agenda. Technological Forecasting and Social Change.
Liam Magee, Lida Ghahremanlou, Karen Soldatic, and Shanthi Robertson. 2021. Intersectional bias in causal language models. arXiv preprint arXiv:2107.07691.
Louis Martin, Benjamin Muller, Pedro Javier Ortiz Suárez, Yoann Dupont, Laurent Romary,
Éric Villemonte de La Clergerie, Djamé Seddah, and Benoît Sagot. 2020. CamemBERT:
A tasty French language model. In Annual Meeting of the Association for Computational
Linguistics.
14


Chandler May, Alex Wang, Shikha Bordia, Samuel R. Bowman, and Rachel Rudinger. 2019.
On measuring social biases in sentence encoders. In Proceedings of the 2019 Conference
of the North American Chapter of the Association for Computational Linguistics: Human
Language Technologies, Volume 1 (Long and Short Papers).
Sabrina J Mielke, Zaid Alyafeai, Elizabeth Salesky, Colin Raffel, Manan Dey, Matthias
Gallé, Arun Raja, Chenglei Si, Wilson Y Lee, Benoît Sagot, et al. 2021. Between words
and characters: A brief history of open-vocabulary modeling and tokenization in NLP.
arXiv preprint arXiv:2112.10508.
Rob Miles and Sean Riley. 2023. Glitch tokens – Computerphile. Accessed on April 11,
2023.
Robert Munro. 2010. Crowdsourced translation for emergency response in Haiti: the global
collaboration of local knowledge. In Proceedings of the Workshop on Collaborative Translation: technology, crowdsourcing, and the translator perspective. Association for Machine
Translation in the Americas.
Pieter Muysken and Norval Smith. 1994. The study of pidgin and creole languages. In
Pidgins and creoles: An introduction.
Moin Nadeem, Anna Bethke, and Siva Reddy. 2021. StereoSet: Measuring stereotypical
bias in pretrained language models. In Proceedings of the 59th Annual Meeting of the
Association for Computational Linguistics and the 11th International Joint Conference
on Natural Language Processing (Volume 1: Long Papers).
Dat Quoc Nguyen and Anh-Tuan Nguyen. 2020. PhoBERT: Pre-trained language models
for Vietnamese. In Findings of the Association for Computational Linguistics: EMNLP.
Akintunde Oladipo, Odunayo Ogundepo, Kelechi Ogueji, and Jimmy Lin. 2022. An exploration of vocabulary size and transfer effects in multilingual language models for African
languages. In 3rd Workshop on African Natural Language Processing.
OpenAI. 2022. Introducing ChatGPT. Accessed on April 11, 2023.
OpenAI. 2022. tiktoken. Git commit: 82facf9.
OpenAI. 2023. GPT-4 technical report. arXiv preprint arXiv:2303.08774.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin,
Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. 2022. Training language models to follow instructions with human feedback. Advances in Neural Information
Processing Systems.
Alicia Parrish, Angelica Chen, Nikita Nangia, Vishakh Padmakumar, Jason Phang, Jana
Thompson, Phu Mon Htut, and Samuel Bowman. 2022. BBQ: A hand-built bias benchmark for question answering. In Findings of the Association for Computational Linguistics:
ACL 2022.
Jonas Pfeiffer, Ivan Vulić, Iryna Gurevych, and Sebastian Ruder. 2021. UNKs everywhere:
Adapting multilingual language models to new scripts. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing.
Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. 2019.
Language models are unsupervised multitask learners.
Jenalea Rajab. 2022. Effect of tokenisation strategies for low-resourced Southern African
languages. In 3rd Workshop on African Natural Language Processing.
Krithika Ramesh, Sunayana Sitaram, and Monojit Choudhury. 2023. Fairness in language
models beyond English: Gaps and challenges. In Findings of the Association for Computational Linguistics: EACL 2023. Association for Computational Linguistics.
15


Surangika Ranathunga, En-Shiun Annie Lee, Marjana Prifti Skenduli, Ravi Shekhar,
Mehreen Alam, and Rishemjit Kaur. 2023. Neural machine translation for low-resource
languages: A survey. ACM Computing Surveys.
Jessica Rumbelow and Matthew Watkins. 2023a. SolidGoldMagikarp III: Glitch token
archaelogy. Accessed on April 11, 2023.
Jessica Rumbelow and Matthew Watkins. 2023b. SolidGoldMagikarp (plus, prompt generation). Accessed on April 11, 2023.
Charles Russ. 1990. The Dialects of Modern German: A Linguistic Survey.
Phillip Rust, Jonas Pfeiffer, Ivan Vulić, Sebastian Ruder, and Iryna Gurevych. 2021. How
good is your tokenizer? On the monolingual performance of multilingual language models.
In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics
and the 11th International Joint Conference on Natural Language Processing (Volume 1:
Long Papers).
Ali Safaya, Moutasem Abdullatif, and Deniz Yuret. 2020. KUISAIL at SemEval-2020 task
12: BERT-CNN for offensive speech identification in social media. In Proceedings of the
Fourteenth Workshop on Semantic Evaluation.
Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana Ilić, Daniel Hesslow,
Roman Castagné, Alexandra Sasha Luccioni, François Yvon, Matthias Gallé, et al. 2022.
BLOOM: A 176B-parameter open-access multilingual language model. arXiv preprint
arXiv:2211.05100.
Raphael Scheible, Fabian Thomczyk, Patric Tippmann, Victor Jaravine, and Martin Boeker.
2020. GottBERT: A pure German language model. arXiv preprint arXiv:2012.02110.
Mike Schuster and Kaisuke Nakajima. 2012. Japanese and Korean voice search. In IEEE
International Conference on Acoustics, Speech and Signal Processing (ICASSP).
Rico Sennrich, Barry Haddow, and Alexandra Birch. 2016. Neural machine translation
of rare words with subword units. In Proceedings of the 54th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers).
Pieter A. M. Seuren. 1995. Notes on the history and the syntax of Mauritian Creole. Linguistics.
Yan Shao, Christian Hardmeier, and Joakim Nivre. 2018. Universal word segmentation:
Implementation and interpretation. Transactions of the Association for Computational
Linguistics.
Peter Sieber and Horst Sitta. 1987. Deutsch in der Schweiz. Zeitschrift für Germanistik.
Felix Stahlberg. 2020. Neural machine translation: A review. Journal of Artificial Intelligence Research.
Steve Stecklow. 2018. Hatebook. Reuters. Accessed on April 11, 2023.
Hui Su, Weiwei Shi, Xiaoyu Shen, Zhou Xiao, Tuo Ji, Jiarui Fang, and Jie Zhou. 2022.
RoCbert: Robust Chinese BERT with multimodal contrastive pretraining. In Annual
Meeting of the Association for Computational Linguistics.
Lichao Sun, Kazuma Hashimoto, Wenpeng Yin, Akari Asai, Jia Li, Philip Yu, and Caiming Xiong. 2020. Adv-BERT: BERT is not robust on misspellings! Generating nature
adversarial samples on BERT. arXiv preprint arXiv:2003.04985.
Shinnosuke Takamichi and Hiroshi Saruwatari. 2018. CPJD corpus: Crowdsourced parallel
speech corpus of Japanese dialects. In Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018).
16


Yuqing Tang, Chau Tran, Xian Li, Peng-Jen Chen, Naman Goyal, Vishrav Chaudhary,
Jiatao Gu, and Angela Fan. 2020. Multilingual translation with extensible multilingual
pretraining and finetuning. arXiv preprint arXiv:2008.00401.
Timm Teubner, Christoph M Flath, Christof Weinhardt, Wil van der Aalst, and Oliver Hinz.
2023. Welcome to the era of ChatGPT et al: The prospects of large language models.
Business & Information Systems Engineering.
The Unicode Consortium. 2022. The Unicode standard, Version 15.0.0.
Jörg Tiedemann. 2012. Parallel data, tools and interfaces in OPUS. In Proceedings of the
Eight International Conference on Language Resources and Evaluation (LREC’12).
Tohoku NLP Group. 2019. BERT models for Japanese NLP.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux,
Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al.
2023. LLaMA: Open and eﬀicient foundation language models. arXiv preprint
arXiv:2302.13971.
Emma Trentman and Sonia Shiri. 2020. The mutual intelligibility of Arabic dialects: Implications for the language classroom. Critical Multilingualism Studies.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez,
Łukasz Kaiser, and Illia Polosukhin. 2017. Attention is all you need. Advances in Neural
Information Processing Systems.
Antti Virtanen, Jenna Kanerva, Rami Ilo, Jouni Luoma, Juhani Luotolahti, Tapio Salakoski,
Filip Ginter, and Sampo Pyysalo. 2019. Multilingual is not enough: BERT for Finnish.
arXiv preprint arXiv:1912.07076.
Jonathan J. Webster and Chunyu Kit. 1992. Tokenization as the initial phase in NLP. In
The International Conference on Computational Linguistics.
Jiacheng Xu, Zhe Gan, Yu Cheng, and Jingjing Liu. 2020. Discourse-aware neural extractive
text summarization. In Proceedings of the 58th Annual Meeting of the Association for
Computational Linguistics. Association for Computational Linguistics.
Linting Xue, Aditya Barua, Noah Constant, Rami Al-Rfou, Sharan Narang, Mihir Kale,
Adam Roberts, and Colin Raffel. 2022. ByT5: Towards a token-free future with pretrained byte-to-byte models. Transactions of the Association for Computational Linguistics.
Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya Siddhant,
Aditya Barua, and Colin Raffel. 2020. mT5: A massively multilingual pre-trained textto-text transformer. In Conference of the North American Chapter of the Association for
Computational Linguistics: Human Language Technologies.
Joseph K. Yamagiwa. 1967. On dialect intelligibility in Japan. Anthropological Linguistics.
Shiyue Zhang, Vishrav Chaudhary, Naman Goyal, James Cross, Guillaume Wenzek, Mohit Bansal, and Francisco Guzman. 2022. How robust is neural machine translation to
language imbalance in multilingual tokenizer training? In Proceedings of the 15th Biennial Conference of the Association for Machine Translation in the Americas (Volume 1:
Research Track).
Judit Ács. 2019. Exploring BERT’s vocabulary. Accessed on April 11, 2023.
Slavomír Čéplö, Ján Bátora, Adam Benkato, Jiří Milička, Christophe Pereira, and Petr
Zemánek. 2016. Mutual intelligibility of spoken Maltese, Libyan Arabic, and Tunisian
Arabic functionally tested: A pilot study. Folia Linguistica.

17


A

Background on Tokenization

To enable automatic processing of language, it must first be represented in a suitable form.
The current practice is to use tokenization which is the process of turning natural language
into sequences of tokens coming from a finite and pre-determined set called vocabulary
(Webster and Kit, 1992). Each token is typically associated with an integer value. Language
models process such sequences of integers, rather than sequences of characters or words. In
this section, we offer a brief overview of the contemporary tokenization methods. For further
details, we recommend the comprehensive survey by Mielke et al. (2021).
Word tokenization. The simplest tokenization method is splitting at white spaces, where
each word is assigned its own token (Bengio et al., 2000). This approach, however, requires
that all possible words are in the vocabulary which is not possible in practice. Therefore word
tokenization often fails to handle cases like “won’t”, words spelled with accented characters
like “naïve” or “açaí”, speling mistakes and named entities like “Cottonshopeburnfoot” (Sun
et al., 2020). This makes it unsuitable for representing open vocabularies, where the words
encountered are not limited to a predetermined set. Furthermore, languages that do not use
spaces to separate words, such as Chinese, Japanese and Burmese, pose additional challenges
for this approach (Shao et al., 2018).
Subword tokenization. Hence, most current models use subword tokenization, where
complex words are broken down into multiple tokens. Subword tokenization can eﬀiciently
handle complex terms by breaking them down into parts, e.g., “Cottonshopeburnfoot” →
“Cotton”+“shop”+“e”+“burn”+“foot”. This approach can represent novel words, including
misspelled ones, in an open vocabulary setting.
Subword vocabularies are usually data-based approaches which use large corpora to learn
which subword sequences occur frequently in practice. Schuster and Nakajima (2012) introduced one of the first subword tokenizers, WordPiece, as a way to handle Japanese and
Korean. Sennrich et al. (2016) proposed using Byte-Pair Encoding (BPE) (Gage, 1994) for
learning subwords by merging the most frequently occurring pairs. BPE has since been
widely used for most of the popular tokenizers. Kudo (2018) proposed an alternative approach via gradually pruning a large vocabulary. It removes tokens that are less likely to
improve the performance of a simple unigram language model. Both methods rely on pretokenization (splitting on whitespaces, when available), which is not an invertible process.
SentencePiece (Kudo and Richardson, 2018) addresses this de-tokenization ambiguity by
treating whitespace as a special symbol, including it in the vocabulary, and supports both
methods. SentencePiece with BPE is by far the most popular tokenization method for the
models considered in this paper.
Unicode support. Even if subword tokenization ensures that individual characters are in
the vocabulary, this still leaves the question of which characters are to be included. Simple
solution is to take the ASCII characters. However, this means that words in other scripts
or accented letters will fall out of it. A common workaround is to represent strings outside
the vocabulary as a special UNK token. However, if there are too many UNK tokens in an
input, the performance of the model tends to deteriorate (Pfeiffer et al., 2021). Therefore, it
is desirable that the number of UNK tokens in the input is kept as low as possible. A simple
and commonly used solution is to base the vocabulary building on Unicode.
Unicode is a computing industry standard for representing text characters (The Unicode
Consortium, 2022). Unicode supports virtually all languages (including many ancient ones,
emojis and special characters) by assigning every grapheme, modifier, punctuation mark,
control character or formatting character one of 1,114,112 integer codepoints. The codepoints
can be represented in binary as the variable-width encoding UTF-8, which encodes every
codepoint with one to four bytes, or the fixed-width UTF-32 which encodes all codepoints
with four bytes (see Figure 4).
UTF-8 can therefore represent any string in any language as a string of bytes. As each
byte can take only one out of 256 values, 256 tokens can be suﬀicient to encode all texts.
In practice this is usually combined with the BPE tokenizer. At first, the corpus is en18


Figure 4: Comparison of variable width Unicode encoding (UTF-8) and fixed width encoding
(UTF-32). Image adapted from (The Unicode Consortium, 2022).
coded as UTF-8 bytes and then BPE is ran on top of it. As most characters occur frequently, BPE would assign them a dedicated token. If the model encounters a character
that didn’t exist in the training corpus (e.g., the medium skin tone waving hand
), it can
still represent it byte-by-byte (F0+9F+91+8B for the waving hand and F0+9F+8F+BD for
the skin tone modifier). This allows the vocabulary to eﬀiciently represent frequently occurring words and rare characters. For example, the sentence “I love açaí” could be tokenized
as “I ”+“love ”+“a”+C3+A7+“a”+C3+AD.
Byte-level and character-level tokenization. If we can represent any input with just
256 characters, then why bother with subword tokens? A key consideration is sequence
length. This is since transformers (Vaswani et al., 2017), the currently predominant deep
learning architecture for language models, have attention layers with a quadratic complexity
in the input length. Hence, as the number of characters is much longer than the sub-word
tokenization, working on the character level has been traditionally considered computationally ineﬀicient. However, Chung et al. (2016), Lee et al. (2017), Gao et al. (2020), Clark
et al. (2022) and Xue et al. (2022) proposed various architectures working around this issue
and operating directly on characters or UTF-8 bytes.

B

Parity for Linguistic Varieties

A language can vary according to factors such as geography, history, social class and culture.
As a result, different dialects, pidgin and creole language variations emerge, each with its
own distinct set of grammar, vocabulary and pronunciation rules.9 Unequal treatment of
certain dialects or languages can lead to social and economic disadvantages for those who
speak them. Therefore, it is important to also study the tokenization differences between the
“standard” language and its varieties.10 Unfortunately, parallel corpora for dialects, pidgin
and creole language variations are far and few in between. In this section, however, we show
results on regional Swiss German varieties, Arabic and Japanese dialects, as well as Haitian
and Mauritian creoles.
Swiss German dialects. Swiss German is a dialect continuum which significantly differs
from the formal High German. German-speaking Switzerland is diglossic:11 High German
is used alongside regional dialects (Hogg et al., 1984). In contrast to other dialects, the use
of Swiss dialects is increasing (Sieber and Sitta, 1987) especially online (Lüdi, 2007). Swiss
German dialects are often considered unintelligible to High German speakers and sometimes
even speakers of different dialects may find diﬀiculty understanding each other (Russ, 1990).
Therefore, ensuring that German-targeting NLP applications can process Swiss German
dialects is important.
To this end, we compare the tokenization parity relative to High German of GottBERT
(Scheible et al., 2020) on the regional dialects of Aargau, Bern, Basel, Graubünden, Luzern,
9

While no standard definitions exist, dialects are usually considered to be regional variations
of a language, whereas pidgin and creole languages are contact languages that emerge from the
interaction of speakers of different languages (Muysken and Smith, 1994).
10
We refer to the language that the datasets label as “standard”, “oﬀicial” or “dominant” without
necessarily endorsing this designation.
11
Diglossia is the situation of two dialects or languages being used by a single language community (Kaye, 2001).

19


Table 6: GottBERT tokenizer premiums on the SwissDial dataset for Swiss German
dialects. The premium is computed with respect to High German.
Region

GottBERT parity

High German
Zürich
St. Gallen
Basel
Graubünden
Luzern
Aargau
Wallis
Bern

1.00
1.38
1.40
1.41
1.44
1.52
1.53
1.58
1.59

Table 7: ArabicBERT tokenizer premiums on the MADAR dataset for Arabic dialects.
The premium is computed relative to Standard Arabic.
City

ArabicBERT

Jeddah
Doha
Riyadh
Muscat
Basra
Salt
Baghdad
Damascus
Aleppo
Jerusalem
Khartoum
Amman
Std. Arabic

City

0.91
0.92
0.92
0.94
0.95
0.95
0.96
0.97
0.97
0.97
0.98
0.99
1.00

ArabicBERT

Sanaa
Beirut
Benghazi
Cairo
Sfax
Tripoli
Aswan
Alexandria
Tunis
Algiers
Mosul
Fes
Rabat

1.01
1.02
1.02
1.03
1.03
1.05
1.06
1.06
1.06
1.07
1.10
1.11
1.17

St. Gallen, Wallis and Zürich. We use SwissDial, a parallel multidialectal corpus, as the
basis of comparison (Dogan-Schönberger et al., 2021). It is worth noting, that the dialect
of each city and its corresponding region may differ significantly. Therefore there might be
large variations within regions as well.
The results in Table 6 show a disparity between the tokenization lengths for High German and the Swiss dialects with a premium ranging from 1.38 for the Zürich dialect, or
Züritüütsch, to 1.59 for the Bernese Bärndütsch. In fact, English has a lower premium than
any Swiss dialect (1.35 on FLORES-200, Table 2) and the premium for Bernese German is
close to the linguistically further Swedish (1.64) and Norwegian Bokmål (1.65). The following example from SwissDial shows how the sentence “Like he’s waiting for something” has
almost twice as long tokenization in Bernese German compared to High German:
963
Als

15628
warte

63
er

18
auf

145
4
etwas .

1134 8808 226 751 2912 13621 288 361 67 11769 4
p is war tä .
Aus wür der
uf
ö

The fact that the GottBERT tokenizer results in better parity for English, Swedish and
Norwegian Bokmål than for Swiss German dialects highlights that it does not likely pick
out stable linguistic constructs.
Arabic dialects. Similarly to Swiss German, Arabic is usually spoken in diglossic speech
communities, where Modern Standard Arabic is spoken alongside at least one prestigious
vernacular particular to the country or region (Bassiouney, 2009). As both Standard Arabic
20


Table 8: BERT Japanese tokenizer premiums on the CPJD dataset for Japanese dialects.
The premium is computed with respect to Standard Japanese. The CPJD dataset consists
of two parallel corpora with the dialects split across the two. Hence, we have also indicated
the corpus for each dialect. Nara-ben has two entries as the dataset has transcriptions for
two separate speakers. The suﬀix “-ben” (弁) means “speech” or “dialect”.
Dialect

Corpus Parity

Akita-ben
Awa-ben
Fukui-ben
Fukuoka-ben
Hiroshima-ben
Hokkaido-ben
Iwaki-ben
Iyo-ben
Izumo-ben
Kanazawa-ben
Kyokotoba

2
2
2
1
1
2
2
1
1
2
2

1.09
1.09
1.04
1.03
1.02
1.06
1.08
1.05
1.10
1.11
1.07

Dialect
Miyazaki-ben
Morokata-ben
Nara-ben
Nara-ben
Okayama-ben
Oosaka-ben
Saitama-ben
Tosa-ben
Toshu-ben
Tsugaru-ben

Corpus Parity
1
1
2
2
1
2
1
1
1
1

1.05
1.15
1.09
1.03
1.15
1.03
1.01
1.03
1.06
1.09

and its dialects are commonly used in written communication, it is vital that tokenizers
handle them equally well.
To assess the performance of Arabic tokenizers, we compare the tokenization lengths of
ArabicBERT (Safaya et al., 2020) across 25 Arabic dialects. To this end, we use the MADAR
parallel corpus of Arabic dialects (Bouamor et al., 2018).
Table 7 shows the premiums relative to Standard Modern Arabic. The premium varies
from 0.91 for the Jeddah dialect to 1.17 for the Rabat dialect. This is significantly lower
than the premium for English (1.83 on FLORES-200 Table 2). The range is also much
smaller than for the Swiss German dialects and approximately half of the considered dialects
have a lower premium than Standard Modern Arabic. Therefore, one could say that the
tokenizer of ArabicBERT achieves tokenization parity for these 25 Arabic vernaculars. This
is likely because the corpus and vocabulary set on which ArabicBERT was trained contained
dialectical Arabic. It is also possible that Arabic dialects are closer to Modern Standard
Arabic and more mutually intelligible than Swiss German dialects are to High German
(Čéplö et al., 2016; Trentman and Shiri, 2020). Still, this difference between the parity for
Swiss and Arabic dialects indicates that including a broader set of vernaculars and dialects
in the corpus results in improved tokenization parity.
Japanese dialects. Japanese also has a number of regional dialects (Hattori, 1973). We
compare the tokenization parity of BERT Japanese (Tohoku NLP Group, 2019) across them.
We employ the CPJD dataset by Takamichi and Saruwatari (2018) which contains transcriptions of the voice recordings of 250 sentences across 20 dialects.
The results in Table 8 show that the premium compared to Standard Japanese (Tokyo
dialect) ranges from 1.01 (for Saitama prefecture, neighbouring Tokyo) to 1.15 (for Morokataben and Okayama-ben). These all are significantly lower than the premium for English (1.49,
as shown in Table 2). Therefore, similarly to ArabicBERT, this is an example of the tokenizer
being relatively well-aligned with the dialects. This is likely because Japanese dialects are
more closely related (and intelligible (Yamagiwa, 1967) to Standard Japanese speakers) than
the Swiss dialects are to High German speakers.
Mauritian and Haitian Creoles. While creoles often have some similarities with a highresource language (usually English or French), the differences are significant to necessitate
special attention to their support (Lent et al., 2021, 2022). This is especially critical for
emergency services and disaster management (Munro, 2010).
Mauritian Creole is based on French as well as the languages of slaves imported from Madagascar and East Africa. As the British gained control of Mauritius, they brought indentured
labourers from India who further had an effect on the formation of the modern Mauritian
21


Creole (Seuren, 1995). Similarly, Haitian Creole (Kreyòl) emerged from the interaction of
French and the various Niger-Congo languages spoken by the Africans brought as slaves
(DeGraff, 2007).
Considering that both languages have their basis in French, one would expect that tokenizers targeting French would have low tokenization parities for Mauritian and Haitian
Creoles. However, taking the tokenizer of CamemBERT (Martin et al., 2020), the premium
for Mauritian Creole is 1.20 using the MorisienMT parallel corpus (Dabre and Sukhoo, 2022).
The premium for Haitian Creole is 1.64 when using the QEDv2 corpus (Tiedemann, 2012;
Abdelali et al., 2014). Haitian Creole is also represented in the FLORES-200 dataset where
the premium relative to French is 1.58. This is significantly larger than linguistically further
languages such as English (1.20), Pangasinan (1.49) and Nigerian Fulfulde (1.54). Therefore,
CamemBERT is not well-placed to tokenize French-related creoles despite the model being
trained for French.

C

Extended Tables of Tokenization Premiums

In addition to the models presented in the main text, these extended tables also include
LLAMA (Touvron et al., 2023), MBart50 (Liu et al., 2020; Tang et al., 2020), SeamlessM4T
(Barrault et al., 2023) and Qwen-VL (Bai et al., 2023).

22


23

PhoBERT

RoCBert

XLM-RoBERTa

M2M100

4.00
4.78
4.78 4.78 4.78 3.78 4.78 4.95
1.89
2.16 2.16 2.16 2.16 1.98 2.16 1.56
3.34
4.27 4.27 4.27 4.27 2.99 4.27 5.10
3.38
4.34
4.34 4.34 4.34 3.01 4.34 5.16
3.31
4.20
4.20 4.20 4.20 2.93 4.20 5.03
1.55
1.94
1.94 1.94 1.94 1.69 1.94 1.25
3.20
4.02
4.02 4.02 4.02 2.84 4.02 4.84
2.20
2.80
2.80 2.80 2.80 2.68 2.80 1.90
2.26
2.65
2.65 2.65 2.65 2.25 2.65 1.77
7.32
7.79
7.79 7.79 7.79 7.68 7.79 5.19
3.19
4.04
4.04 4.04 4.04 2.83 4.04 4.83
3.42
4.40
4.40 4.40 4.40 3.04 4.40 5.21
2.31 2.51
2.51 2.51 2.51 2.45 2.51 1.76
3.43 4.41
4.41 4.41 4.41 3.04 4.41 5.22
3.35 4.21
4.21 4.21 4.21 2.96 4.21 5.08
3.36 4.23
4.23 4.23 4.23 2.96 4.23 5.10
6.14 9.79
9.79 9.78 9.78 6.20 9.79 8.32
1.48 1.89
1.89 1.89 1.89 1.58 1.89 1.33
4.53 7.19
7.19 7.19 7.19 4.78 7.19 8.19
2.03 2.32
2.32 2.32 2.32 2.17 2.32 1.62
3.76 5.16
5.16 5.16 5.16 3.34 5.16 5.32
2.61 3.47
3.47 3.47 3.47 2.64 3.47 2.31
2.91 6.01
6.01 6.01 6.01 4.28 6.01 3.97
1.99 2.66
2.66 2.66 2.66 2.57 2.66 1.84
1.77 1.97
1.97 1.97 1.97 1.80 1.97 1.39
2.38 6.56
6.56 6.56 6.56 3.55 6.56 4.17
2.15 2.46
2.46 2.46 2.46 2.23 2.46 1.69
5.38 9.65
9.65 9.65 9.65 5.84 9.65 8.54
4.52 7.18
7.18 7.18 7.18 4.69 7.18 8.08
4.22
5.03 5.03 5.03 5.03 3.80 5.03 5.53
1.75
1.98
1.98 1.98 1.98 1.71 1.98 1.38
6.67 14.93 14.93 14.93 14.93 11.27 14.93 10.87
1.69
2.19
2.19 2.19 2.19 1.87 2.19 1.47
1.87
2.20
2.20 2.20 2.20 1.98 2.20 1.49
1.78
5.51
5.51 5.51 5.51 2.64 5.51 3.51
1.51
1.92
1.92 1.92 1.92 1.71 1.92 1.40
1.96
2.24
2.24 2.24 2.24 1.93 2.24 1.57
1.69
2.62
2.62 2.62 2.62 2.11 2.62 1.73
1.91
2.16
2.16 2.16 2.16 1.98 2.16 1.51
4.43
6.49
6.49 6.49 6.49 4.80 6.49 5.82
2.13
2.49
2.49 2.49 2.49 2.12 2.49 1.67
2.09
2.34
2.34 2.34 2.34 2.12 2.34 1.66
1.54
1.90
1.90 1.90 1.90 1.62 1.90 1.26
1.41
2.14
2.14 2.14 2.14 1.58 2.14 0.74
1.88
2.48
2.48 2.48 2.48 2.25 2.48 1.60
1.88
2.20
2.20 2.20 2.20 2.05 2.20 1.54
7.42 16.36 16.36 16.36 16.36 12.33 16.36 11.95
4.99
6.54
6.54 6.54 6.54 5.15 6.54 4.99
1.00
1.00
1.00 1.00 1.00 1.00 1.00 1.00
1.67
2.03
2.03 2.03 2.03 1.87 2.03 1.37
1.76
2.11
2.11 2.11 2.11 1.87 2.11 1.39
1.79
2.10
2.10 2.10 2.10 1.88 2.10 1.39
2.28
2.90
2.90 2.90 2.90 2.75 2.90 1.97
1.92
2.38
2.38 2.38 2.38 2.07 2.38 1.66
2.02
2.30
2.30 2.30 2.30 2.15 2.30 1.67
1.91
2.28
2.28 2.28 2.28 1.99 2.28 1.46
2.83
4.08
4.08 4.08 4.08 3.67 4.08 2.75
1.47
2.00
2.00 2.00 2.00 1.60 2.00 1.47
1.70
2.07
2.07 2.07 2.07 1.85 2.07 1.47
1.72
1.99
1.99 1.99 1.99 1.85 1.99 1.37
2.22
2.53
2.53 2.53 2.53 2.32 2.53 1.72
2.33
2.70
2.70 2.70 2.70 2.42 2.70 1.86
2.17
2.56
2.56 2.56 2.56 2.33 2.56 1.76
1.48
1.91
1.91 1.91 1.91 1.56 1.91 1.39
1.99
2.46
2.46 2.46 2.46 2.17 2.46 1.68
9.98 12.27 12.27 12.27 12.27 7.69 12.27 8.17
1.58
1.90
1.90 1.90 1.90 1.74 1.90 1.35
1.89
2.15
2.15 2.15 2.15 2.00 2.15 1.49

CamemBERT

GottBERT

RoBERTa

cl100k_base

p50k_edit

p50k_base

r50k_base

LLAMA

Acehnese (Arabic script)
Acehnese (Latin script)
Mesopotamian Arabic
Ta’izzi-Adeni Arabic
Tunisian Arabic
Afrikaans
South Levantine Arabic
Akan
Tosk Albanian
Amharic
North Levantine Arabic
Standard Arabic
Standard Arabic (Romanized)
Najdi Arabic
Moroccan Arabic
Egyptian Arabic
Assamese
Asturian
Awadhi
Central Aymara
South Azerbaijani
North Azerbaijani
Bashkir
Bambara
Balinese
Belarusian
Bemba
Bengali
Bhojpuri
Banjar (Arabic script)
Banjar (Latin script)
Standard Tibetan
Bosnian
Buginese
Bulgarian
Catalan
Cebuano
Czech
Chokwe
Central Kurdish
Crimean Tatar
Welsh
Danish
German
Southwestern Dinka
Dyula
Dzongkha
Greek
English
Esperanto
Estonian
Basque
Ewe
Faroese
Fijian
Finnish
Fon
French
Friulian
Nigerian Fulfulde
West Central Oromo
Scottish Gaelic
Irish
Galician
Guarani
Gujarati
Haitian Creole
Hausa

GPT-2

Language

—
1.55
—
—
—
1.38
—
1.64
1.82
—
—
—
1.72
—
—
—
—
1.31
—
1.62
—
—
—
1.54
1.43
—
1.68
—
—
—
1.35
—
1.46
1.45
—
1.33
1.59
—
1.49
—
1.68
1.68
1.39
1.55
1.43
1.43
—
—
1.00
1.35
1.42
1.44
1.69
1.64
1.52
1.56
—
0.84
1.38
1.29
1.73
1.80
1.75
1.36
1.55
—
1.32
1.47

—
1.37
—
—
—
1.26
—
1.45
1.69
—
—
—
1.55
—
—
—
—
1.24
—
1.47
—
1.90
—
1.40
1.28
2.88
1.53
—
—
—
1.21
—
1.35
1.35
2.57
1.31
1.41
1.48
1.32
—
1.54
1.53
1.29
1.40
1.32
1.30
—
3.11
1.00
1.26
1.33
1.33
1.46
1.46
1.39
1.47
—
1.38
1.33
1.16
1.61
1.61
1.55
1.30
1.45
—
1.15
1.26

—
1.10
—
—
—
1.06
—
—
1.12
—
—
—
1.19
—
—
—
—
1.04
—
1.09
—
—
—
—
1.14
—
1.26
—
—
—
1.08
—
1.02
1.10
—
1.10
1.20
0.99
1.10
—
—
1.06
1.04
1.20
0.75
0.98
—
1.15
1.00
1.01
1.03
1.11
—
—
1.13
1.13
—
1.20
1.07
0.86
1.24
1.24
1.15
1.11
1.05
—
0.89
1.02

1.94
1.57
1.16
1.17
1.20
1.20
1.12
1.98
1.32
1.34
1.15
1.18
1.94
1.18
1.25
1.17
1.90
1.27
1.37
1.70
1.43
1.15
2.06
1.82
1.32
1.46
1.76
1.38
1.47
1.92
1.21
—
1.12
1.51
1.16
1.26
1.52
1.17
1.55
2.30
1.38
1.43
1.09
1.17
1.68
1.65
—
1.45
1.00
1.20
1.12
1.16
2.01
1.44
1.72
1.14
2.51
1.30
1.56
1.46
1.78
1.75
1.50
1.13
1.72
1.42
1.39
1.40

1.89
1.47
1.27
1.28
1.29
1.22
1.22
1.83
1.36
1.42
1.24
1.29
1.83
1.30
1.33
1.27
2.24
1.15
1.47
1.64
1.50
1.26
1.23
1.72
1.29
1.56
1.67
1.55
1.54
1.93
1.16
—
1.17
1.49
1.23
1.26
1.38
1.23
1.47
2.48
1.37
1.44
1.12
1.24
1.55
1.53
—
1.58
1.00
1.38
1.20
1.23
1.86
1.41
1.62
1.23
2.31
1.33
1.47
1.27
1.49
1.61
1.50
1.14
1.63
1.58
1.16
1.29


Language

MBart50

mT5

FlanT5

ByT5

CANINE

BLOOM

ArabicBERT

MuRIL

UTF-32

BERT Japanese

SeamlessM4T

NLLB

Qwen

Acehnese (Arabic script)
Acehnese (Latin script)
Mesopotamian Arabic
Ta’izzi-Adeni Arabic
Tunisian Arabic
Afrikaans
South Levantine Arabic
Akan
Tosk Albanian
Amharic
North Levantine Arabic
Standard Arabic
Standard Arabic (Romanized)
Najdi Arabic
Moroccan Arabic
Egyptian Arabic
Assamese
Asturian
Awadhi
Central Aymara
South Azerbaijani
North Azerbaijani
Bashkir
Bambara
Balinese
Belarusian
Bemba
Bengali
Bhojpuri
Banjar (Arabic script)
Banjar (Latin script)
Standard Tibetan
Bosnian
Buginese
Bulgarian
Catalan
Cebuano
Czech
Chokwe
Central Kurdish
Crimean Tatar
Welsh
Danish
German
Southwestern Dinka
Dyula
Dzongkha
Greek
English
Esperanto
Estonian
Basque
Ewe
Faroese
Fijian
Finnish
Fon
French
Friulian
Nigerian Fulfulde
West Central Oromo
Scottish Gaelic
Irish
Galician
Guarani
Gujarati
Haitian Creole
Hausa

1.94
1.57
1.16
1.17
1.20
1.20
1.12
1.98
1.32
1.34
1.15
1.18
1.94
1.18
1.25
1.17
1.90
1.27
1.37
1.70
1.43
1.15
2.06
1.82
1.32
1.46
1.76
1.38
1.47
1.92
1.21
—
1.12
1.51
1.16
1.26
1.52
1.17
1.55
2.30
1.38
1.43
1.09
1.17
1.68
1.65
—
1.45
1.00
1.20
1.12
1.16
2.01
1.44
1.72
1.14
2.51
1.30
1.56
1.46
1.78
1.75
1.50
1.13
1.72
1.42
1.39
1.40

1.79
1.44
1.28
1.32
1.29
1.20
1.24
1.82
1.48
1.73
1.23
1.35
1.73
1.35
1.29
1.28
1.94
1.28
1.62
1.57
1.42
1.35
1.60
1.65
1.29
1.59
1.57
1.58
1.63
1.76
1.16
3.68
1.33
1.44
1.28
1.36
1.42
1.27
1.41
1.75
1.32
1.70
1.14
1.19
1.58
1.55
4.24
1.65
1.00
1.19
1.12
1.22
1.82
1.40
1.59
1.16
2.36
1.40
1.52
1.32
1.69
1.85
1.67
1.31
1.62
1.73
1.22
1.37

—
2.55
—
—
—
2.15
—
2.96
3.09
—
—
—
2.94
—
—
—
—
2.07
—
2.71
—
—
—
2.70
2.37
—
3.01
—
—
—
2.20
—
2.48
2.51
—
2.14
2.86
2.72
2.66
—
2.80
3.12
2.26
1.37
—
2.68
—
—
1.00
2.19
2.43
2.33
2.85
2.73
3.02
2.61
—
1.60
2.30
2.14
3.16
3.24
3.14
2.18
2.57
—
2.32
2.61

1.51
1.09
1.56
1.58
1.54
1.07
1.49
1.10
1.20
1.72
1.48
1.60
1.17
1.60
1.56
1.56
2.54
1.07
2.50
1.07
1.63
1.26
1.85
1.04
1.11
2.06
1.23
2.61
2.47
1.69
1.05
3.31
1.03
1.09
1.89
1.12
1.20
1.08
1.07
1.78
1.13
1.07
1.05
1.18
0.96
1.07
3.64
2.17
1.00
1.02
1.01
1.07
1.07
1.09
1.17
1.11
1.26
1.24
1.13
0.96
1.20
1.28
1.23
1.13
1.09
2.50
0.95
1.08

0.85
1.07
0.86
0.87
0.85
1.06
0.83
1.00
1.12
0.67
0.82
0.88
1.17
0.88
0.86
0.86
0.96
1.03
0.98
1.05
0.89
1.09
1.01
0.96
1.11
1.13
1.23
0.98
0.97
0.93
1.05
1.13
1.01
1.06
1.04
1.10
1.20
0.97
1.07
0.97
1.03
1.07
1.03
1.17
0.86
1.01
1.25
1.20
1.00
1.00
0.98
1.06
0.97
1.02
1.17
1.07
1.02
1.19
1.10
0.93
1.19
1.24
1.16
1.11
1.01
0.96
0.92
1.07

2.65
1.74
1.15
1.15
1.19
1.69
1.12
2.05
2.17
5.07
1.13
1.14
2.15
1.15
1.26
1.16
1.41
1.31
1.43
1.94
1.81
2.30
3.57
1.89
1.46
3.24
1.92
1.17
1.53
2.47
1.30
6.66
1.84
1.71
2.49
1.18
1.78
2.03
1.72
3.21
2.07
2.09
1.67
1.68
1.82
1.80
7.36
3.81
1.00
1.65
1.77
1.14
2.11
1.95
1.99
1.89
2.21
1.20
1.70
1.66
2.19
2.25
2.15
1.27
1.87
1.35
1.56
1.78

—
1.44
0.55
0.55
0.57
1.33
0.55
—
1.46
—
0.55
0.55
1.60
0.55
0.63
0.57
—
1.24
—
1.44
1.11
1.74
—
—
1.40
2.60
1.65
—
—
1.04
1.32
—
1.39
1.45
2.35
1.29
1.51
1.31
1.47
1.65
1.45
1.55
1.28
1.44
—
1.30
—
2.70
1.00
1.24
1.28
1.41
—
1.41
1.65
1.42
—
1.33
1.28
1.16
1.63
1.57
1.45
1.30
1.40
—
1.18
1.34

—
2.02
1.93
1.94
1.90
1.84
1.82
—
2.52
—
1.83
1.97
2.28
1.97
1.91
1.89
1.24
1.81
1.29
1.98
1.72
—
—
—
1.83
—
2.17
1.01
1.39
—
1.71
—
—
1.96
—
1.90
2.10
—
1.94
—
—
2.32
1.83
2.02
—
2.06
—
—
1.00
—
1.71
1.90
—
—
2.01
2.05
—
1.96
1.94
1.54
2.17
2.27
2.46
1.91
1.99
1.19
1.68
1.78

0.85
1.07
0.86
0.87
0.85
1.06
0.83
1.00
1.12
0.67
0.82
0.88
1.17
0.88
0.86
0.86
0.96
1.03
0.98
1.05
0.89
1.09
1.01
0.96
1.11
1.13
1.23
0.98
0.97
0.93
1.05
1.13
1.01
1.06
1.04
1.10
1.20
0.97
1.07
0.97
1.03
1.07
1.03
1.17
0.86
1.01
1.25
1.20
1.00
1.00
0.98
1.06
0.97
1.02
1.17
1.07
1.02
1.19
1.10
0.93
1.19
1.24
1.16
1.11
1.01
0.96
0.92
1.07

—
1.41
—
—
—
1.27
—
1.45
—
—
—
—
1.64
—
—
—
—
1.26
—
1.45
—
—
—
1.34
1.35
—
1.64
—
—
—
1.29
—
1.30
1.39
—
1.30
1.53
—
1.42
—
—
1.47
—
1.37
—
1.39
—
—
1.00
—
—
1.35
—
—
1.53
1.45
—
1.36
1.29
1.21
1.63
1.49
1.51
1.32
—
—
1.19
1.35

1.89
1.24
1.37
1.39
1.39
1.22
1.31
1.40
1.35
1.32
1.33
1.40
1.86
1.40
1.39
1.36
1.39
1.17
1.22
1.32
1.37
1.33
1.22
1.27
1.08
1.72
1.39
1.28
1.28
1.88
1.08
1.44
1.19
1.30
1.31
1.25
1.29
1.26
1.34
1.30
1.25
1.38
1.11
1.29
1.25
1.44
1.48
1.65
1.00
1.23
1.16
1.27
1.27
1.31
1.32
1.21
1.59
1.35
1.37
1.24
1.42
1.56
1.42
1.16
1.34
1.35
1.11
1.18

1.89
1.24
1.37
1.39
1.39
1.22
1.31
1.40
1.35
1.32
1.33
1.40
1.86
1.40
1.39
1.36
1.39
1.17
1.22
1.32
1.37
1.33
1.22
1.27
1.08
1.72
1.39
1.28
1.28
1.88
1.08
1.44
1.19
1.30
1.31
1.25
1.29
1.26
1.34
1.30
1.25
1.38
1.11
1.29
1.25
1.44
1.48
1.65
1.00
1.23
1.16
1.27
1.27
1.31
1.32
1.21
1.59
1.35
1.37
1.24
1.42
1.56
1.42
1.16
1.34
1.35
1.11
1.18

2.66
1.95
1.63
1.63
1.66
1.67
1.55
2.28
2.23
4.16
1.58
1.63
2.42
1.63
1.70
1.64
5.46
1.56
4.36
2.15
2.62
2.49
3.14
2.14
1.79
3.00
2.20
5.09
4.33
2.63
1.70
7.33
1.86
1.96
2.20
1.69
1.91
2.07
1.94
3.46
1.95
2.09
1.61
1.55
2.01
1.96
8.19
4.95
1.00
1.80
1.85
1.87
2.36
2.04
2.13
1.97
2.87
1.57
1.83
1.75
2.29
2.38
2.28
1.54
2.09
6.78
1.72
1.95

24


25

4.39 4.52
7.46 8.34
7.21 8.05
2.15 1.46
2.66 1.79
10.01 6.67
3.42 2.33
2.26 1.59
1.98 1.37
2.43 1.72
2.01 1.43
1.93 1.36
3.00 3.23
2.50 1.74
2.65 1.89
2.32 1.62
13.69 9.27
6.19 5.63
7.03 7.76
13.85 9.22
5.92 3.91
4.87 3.28
1.93 1.32
6.42 4.24
15.33 10.22
3.44 2.36
2.37 1.61
5.74 3.79
2.33 1.64
2.45 1.66
4.74 5.20
2.57 1.78
2.17 1.61
5.07 3.86
13.19 8.79
2.29 1.57
2.05 1.34
2.03 1.47
2.45 1.63
2.37 1.58
2.39 1.67
2.25 1.30
2.13 1.50
2.17 1.48
2.04 1.40
2.09 1.53
2.54 1.76
7.22 8.07
7.43 8.27
15.24 10.16
7.87 8.76
5.25 5.71
1.97 1.40
5.46 3.48
2.69 1.80
10.22 9.06
2.54 1.74
2.45 1.77
16.89 11.26
1.97 1.28
1.93 1.25
1.86 1.23
7.59 8.37
2.32 1.63
4.23 2.79
2.26 1.57
2.07 1.47
13.38 8.94

M2M100

4.39 3.66
7.46 4.79
7.21 4.69
2.15 1.85
2.66 2.15
10.01 9.98
3.42 2.44
2.26 2.05
1.98 1.55
2.43 2.15
2.01 1.64
1.93 1.73
3.00 2.30
2.50 2.47
2.65 2.35
2.32 2.17
13.68 8.90
6.19 4.62
7.03 4.69
13.85 9.85
5.92 3.79
4.87 4.74
1.93 1.72
6.42 3.77
15.33 8.88
3.44 3.29
2.37 2.14
5.74 3.51
2.33 2.13
2.45 2.20
4.74 3.63
2.57 2.37
2.17 1.99
5.07 2.38
13.19 9.62
2.29 1.98
2.05 1.80
2.03 1.86
2.45 2.21
2.37 2.04
2.39 2.20
2.25 1.99
2.13 1.94
2.17 1.96
2.04 1.82
2.09 1.96
2.54 2.35
7.22 4.70
7.43 4.90
15.24 9.00
7.87 5.07
5.25 3.97
1.97 1.77
5.46 2.77
2.69 2.41
10.22 6.71
2.54 2.32
2.45 2.35
16.89 11.70
1.97 1.59
1.93 1.64
1.86 1.56
7.59 4.79
2.32 2.18
4.23 4.00
2.26 2.08
2.07 1.83
13.38 12.48

XLM-RoBERTa

4.39
7.46
7.21
2.15
2.66
10.01
3.42
2.26
1.98
2.43
2.01
1.93
3.00
2.50
2.65
2.32
13.68
6.19
7.03
13.85
5.92
4.87
1.93
6.42
15.33
3.44
2.37
5.74
2.33
2.45
4.74
2.57
2.17
5.07
13.19
2.29
2.05
2.03
2.45
2.37
2.39
2.25
2.13
2.17
2.04
2.09
2.54
7.22
7.43
15.24
7.87
5.25
1.97
5.46
2.69
10.22
2.54
2.45
16.89
1.97
1.93
1.86
7.59
2.32
4.23
2.26
2.07
13.38

RoCBert

p50k_edit

4.39
7.46
7.21
2.15
2.66
10.01
3.42
2.26
1.98
2.43
2.01
1.93
3.00
2.50
2.65
2.32
13.69
6.19
7.03
13.85
5.92
4.87
1.93
6.42
15.33
3.44
2.37
5.74
2.33
2.45
4.74
2.57
2.17
5.07
13.19
2.29
2.05
2.03
2.45
2.37
2.39
2.25
2.13
2.17
2.04
2.09
2.54
7.22
7.43
15.24
7.87
5.25
1.97
5.46
2.69
10.22
2.54
2.45
16.89
1.97
1.93
1.86
7.59
2.32
4.23
2.26
2.07
13.38

PhoBERT

p50k_base

4.39
7.46
7.21
2.15
2.66
10.01
3.42
2.26
1.98
2.43
2.01
1.93
3.00
2.50
2.65
2.32
13.69
6.19
7.03
13.85
5.92
4.87
1.93
6.42
15.33
3.44
2.37
5.74
2.33
2.45
4.74
2.57
2.17
5.07
13.19
2.29
2.05
2.03
2.45
2.37
2.39
2.25
2.13
2.17
2.04
2.09
2.54
7.22
7.43
15.24
7.87
5.25
1.97
5.46
2.69
10.22
2.54
2.45
16.89
1.97
1.93
1.86
7.59
2.32
4.23
2.26
2.07
13.38

CamemBERT

r50k_base

3.29
4.60
4.44
1.67
1.79
5.11
2.32
2.01
1.76
1.98
1.46
1.72
2.24
2.00
2.27
1.91
10.83
4.43
4.44
4.87
2.51
3.48
1.58
2.76
10.26
2.52
2.04
2.44
2.02
2.05
3.82
2.15
1.93
3.18
11.47
1.84
1.64
1.79
1.89
1.85
1.99
1.80
1.89
1.90
1.76
1.86
2.10
4.49
4.63
5.54
4.58
4.32
1.77
1.84
2.16
5.84
2.12
2.18
8.37
1.46
1.54
1.50
4.49
2.02
2.83
2.02
1.66
11.59

GottBERT

GPT-2

Hebrew
Hindi
Chhattisgarhi
Croatian
Hungarian
Armenian
Igbo
Ilocano
Indonesian
Icelandic
Italian
Javanese
Japanese
Kabyle
Jingpho
Kamba
Kannada
Kashmiri (Arabic script)
Kashmiri (Devanagari script)
Georgian
Kazakh
Kabiye
Kabuverdianu
Halh Mongolian
Khmer
Kikuyu
Kinyarwanda
Kyrgyz
Kimbundu
Northern Kurdish
Central Kanuri (Arabic script)
Central Kanuri (Latin script)
Kikongo
Korean
Lao
Ligurian
Limburgish
Lingala
Lithuanian
Lombard
Latgalian
Luxembourgish
Luba-Kasai
Ganda
Luo
Mizo
Standard Latvian
Magahi
Maithili
Malayalam
Marathi
Minangkabau (Arabic script)
Minangkabau (Latin script)
Macedonian
Maltese
Meitei (Bengali script)
Mossi
Maori
Burmese
Dutch
Norwegian Nynorsk
Norwegian Bokmål
Nepali
Northern Sotho
Nuer
Nyanja
Occitan
Odia

RoBERTa

LLAMA

cl100k_base

Language

—
—
—
1.43
1.78
—
1.77
1.61
1.40
—
1.36
1.39
—
1.59
1.78
1.48
—
—
—
—
—
—
1.30
—
—
—
1.59
—
1.58
1.65
—
1.60
1.44
—
—
1.50
1.39
1.37
1.53
1.52
1.62
1.52
1.44
1.47
1.39
1.52
1.68
—
—
—
—
—
1.39
—
1.72
—
1.51
1.69
—
1.40
1.40
1.37
—
1.58
—
1.55
1.40
—

—
—
—
1.33
1.57
—
1.48
1.41
1.25
1.50
1.33
1.21
—
1.43
1.54
1.30
—
—
—
—
2.66
—
1.21
2.72
—
1.66
1.47
2.67
1.43
1.40
—
1.44
1.37
—
—
1.43
1.32
1.26
1.42
1.41
1.48
1.43
1.31
1.36
1.27
1.29
1.56
—
—
—
—
—
1.25
2.58
1.57
—
1.38
1.47
—
1.32
1.29
1.27
—
1.48
—
1.42
1.38
—

—
—
—
1.00
1.09
—
0.99
1.21
1.12
—
1.19
1.06
0.52
0.90
1.20
0.98
—
—
—
—
—
—
0.98
—
—
1.18
1.15
—
1.12
0.99
—
—
1.12
0.99
—
1.09
1.04
1.08
1.04
1.04
1.02
1.15
1.09
1.07
1.03
1.06
1.05
—
—
—
—
—
1.09
—
1.03
—
0.85
1.05
—
1.13
1.02
1.01
—
1.12
—
1.17
1.14
—

1.12
1.25
1.41
1.10
1.18
1.38
2.12
1.61
0.94
1.23
1.19
1.15
1.11
1.84
1.94
1.62
1.36
1.93
1.82
1.34
1.15
2.98
1.35
1.21
1.62
2.31
1.72
1.16
1.64
1.38
2.60
1.74
1.58
1.16
1.39
1.65
1.45
1.52
1.17
1.71
1.57
1.64
1.54
1.55
1.52
1.65
1.23
1.41
1.58
1.38
1.22
2.02
1.31
1.17
1.96
2.56
1.78
1.86
1.72
1.14
1.17
1.07
1.13
1.75
2.62
1.59
1.50
1.45

1.22
1.36
1.51
1.15
1.28
1.50
1.47
1.33
0.98
1.29
1.25
1.10
1.20
1.71
1.78
1.52
1.53
1.93
1.86
1.56
1.28
2.71
1.30
1.34
1.87
2.17
1.63
1.66
1.54
1.66
2.49
1.65
1.48
1.21
1.61
1.59
1.38
1.26
1.25
1.56
1.51
1.32
1.43
1.38
1.43
1.54
1.29
1.50
1.64
1.59
1.38
1.99
1.25
1.24
1.87
2.59
1.66
1.74
2.21
1.18
1.17
1.10
1.28
1.52
2.44
1.55
1.31
1.56


Language

MBart50

mT5

FlanT5

ByT5

CANINE

BLOOM

ArabicBERT

MuRIL

UTF-32

BERT Japanese

SeamlessM4T

NLLB

Qwen

Hebrew
Hindi
Chhattisgarhi
Croatian
Hungarian
Armenian
Igbo
Ilocano
Indonesian
Icelandic
Italian
Javanese
Japanese
Kabyle
Jingpho
Kamba
Kannada
Kashmiri (Arabic script)
Kashmiri (Devanagari script)
Georgian
Kazakh
Kabiye
Kabuverdianu
Halh Mongolian
Khmer
Kikuyu
Kinyarwanda
Kyrgyz
Kimbundu
Northern Kurdish
Central Kanuri (Arabic script)
Central Kanuri (Latin script)
Kikongo
Korean
Lao
Ligurian
Limburgish
Lingala
Lithuanian
Lombard
Latgalian
Luxembourgish
Luba-Kasai
Ganda
Luo
Mizo
Standard Latvian
Magahi
Maithili
Malayalam
Marathi
Minangkabau (Arabic script)
Minangkabau (Latin script)
Macedonian
Maltese
Meitei (Bengali script)
Mossi
Maori
Burmese
Dutch
Norwegian Nynorsk
Norwegian Bokmål
Nepali
Northern Sotho
Nuer
Nyanja
Occitan
Odia

1.12
1.25
1.41
1.10
1.18
1.38
2.12
1.61
0.94
1.23
1.19
1.15
1.11
1.84
1.94
1.62
1.36
1.93
1.82
1.34
1.15
2.98
1.35
1.21
1.62
2.31
1.72
1.16
1.64
1.38
2.60
1.74
1.58
1.16
1.39
1.65
1.45
1.52
1.17
1.71
1.57
1.64
1.54
1.55
1.52
1.65
1.23
1.41
1.58
1.38
1.22
2.02
1.31
1.17
1.96
2.56
1.78
1.86
1.72
1.14
1.17
1.07
1.13
1.75
2.62
1.59
1.50
1.45

1.22
1.59
1.60
1.30
1.26
1.58
1.79
1.61
1.08
1.32
1.34
1.21
0.90
1.82
1.79
1.52
1.44
2.00
1.79
1.55
1.20
2.83
1.28
1.48
1.43
2.18
1.51
1.32
1.48
1.42
2.43
1.58
1.46
1.27
1.27
1.69
1.38
1.38
1.23
1.70
1.46
1.46
1.37
1.40
1.41
1.57
1.30
1.61
1.74
1.35
1.52
1.84
1.25
1.29
1.69
2.21
1.80
1.69
1.56
1.17
1.18
1.12
1.47
1.57
2.42
1.35
1.48
3.11

—
—
—
2.43
2.99
—
3.17
2.82
2.24
2.81
2.18
2.21
—
2.83
3.41
2.69
—
—
—
—
—
—
2.21
—
—
—
2.76
—
2.91
2.74
—
2.82
3.01
—
—
2.54
2.25
2.73
2.58
2.58
2.70
2.24
2.48
2.65
2.55
2.76
2.78
—
—
—
—
—
2.35
—
2.94
—
2.90
3.28
—
2.19
2.29
2.24
—
2.81
—
2.71
2.26
—

1.39
2.55
2.46
1.01
1.16
2.04
1.21
1.21
1.08
1.09
1.19
1.04
1.27
1.06
1.27
1.01
2.83
1.72
2.40
2.95
1.89
1.37
1.02
1.91
3.33
1.30
1.13
1.88
1.11
1.10
1.60
1.11
1.14
1.20
2.73
1.17
1.07
1.08
1.06
1.16
1.05
1.15
1.08
1.03
1.05
1.10
1.11
2.46
2.53
3.10
2.67
1.74
1.07
1.89
1.16
2.77
1.03
1.16
3.51
1.11
1.04
1.03
2.56
1.17
1.32
1.12
1.17
2.73

0.78
1.00
0.97
0.98
1.05
1.11
1.02
1.21
1.08
0.99
1.18
1.04
0.44
0.99
1.28
0.98
1.05
0.96
0.96
1.10
1.03
1.09
0.99
1.04
1.18
1.17
1.11
1.02
1.11
1.00
0.88
1.05
1.14
0.51
0.99
1.10
1.04
1.08
1.00
1.07
0.99
1.12
1.08
1.02
1.05
1.10
1.02
0.96
0.98
1.13
1.01
0.96
1.07
1.04
1.11
1.03
0.96
1.11
1.24
1.11
1.01
1.01
0.96
1.15
1.08
1.12
1.14
1.03

2.92
1.28
1.44
1.80
2.07
4.31
1.72
1.90
0.96
1.99
1.62
1.40
1.81
2.02
2.14
1.77
1.31
2.32
1.85
4.98
3.23
3.34
1.51
3.38
6.40
2.48
1.58
3.02
1.81
2.03
2.10
2.00
1.75
2.79
8.70
1.81
1.75
1.65
1.94
1.84
1.99
1.89
1.68
1.67
1.68
1.83
2.08
1.45
1.56
1.38
1.21
2.58
1.44
2.50
2.25
2.35
1.99
2.12
10.05
1.71
1.65
1.62
1.17
1.94
2.79
1.78
1.49
1.36

1.72
—
—
1.36
1.40
—
1.50
1.55
1.35
1.34
1.41
1.36
1.01
1.29
1.71
1.33
—
1.26
—
—
—
—
1.25
—
—
1.56
1.54
—
1.55
1.29
—
—
1.59
1.30
—
1.38
1.32
1.47
1.33
1.29
1.36
1.40
1.44
1.46
1.35
1.43
1.35
—
—
—
—
1.13
1.36
—
1.44
—
1.19
1.49
—
1.38
1.28
1.26
—
1.48
—
1.52
1.33
—

—
1.16
1.34
—
2.31
—
—
2.01
1.74
—
1.92
1.74
—
—
2.32
—
1.06
1.75
1.75
—
—
—
1.81
—
—
—
2.15
—
1.99
—
2.37
—
1.97
—
—
2.05
1.92
1.90
—
1.96
—
2.17
1.89
1.94
1.87
1.92
—
1.34
1.50
1.18
1.06
—
1.77
—
—
2.34
—
2.12
—
1.91
1.82
1.79
1.01
2.18
—
2.02
1.93
1.21

0.78
1.00
0.97
0.98
1.05
1.11
1.02
1.21
1.08
0.99
1.18
1.04
0.44
0.99
1.28
0.98
1.05
0.96
0.96
1.10
1.03
1.09
0.99
1.04
1.18
1.17
1.11
1.02
1.11
1.00
0.88
1.05
1.14
0.51
0.99
1.10
1.04
1.08
1.00
1.07
0.99
1.12
1.08
1.02
1.05
1.10
1.02
0.96
0.98
1.13
1.01
0.96
1.07
1.04
1.11
1.03
0.96
1.11
1.24
1.11
1.01
1.01
0.96
1.15
1.08
1.12
1.14
1.03

—
—
—
1.27
—
—
—
1.55
1.33
—
1.37
1.29
0.67
—
1.65
—
—
—
—
—
—
—
1.29
—
—
—
1.50
—
1.52
—
—
—
1.54
—
—
—
1.28
1.41
—
—
—
1.31
1.41
1.41
1.35
1.37
—
—
—
—
—
—
1.32
—
—
—
—
1.45
—
1.33
1.22
1.18
—
1.48
—
1.44
1.33
—

1.24
1.22
1.26
1.17
1.27
1.51
1.32
1.33
0.93
1.29
1.25
1.03
1.01
1.56
1.47
1.28
1.37
1.81
1.69
1.61
1.18
1.56
1.28
1.36
1.80
1.52
1.30
1.25
1.35
1.44
2.54
1.55
1.21
1.03
1.47
1.60
1.44
1.12
1.18
1.61
1.42
1.44
1.21
1.26
1.24
1.31
1.20
1.23
1.24
1.49
1.26
1.97
1.15
1.24
1.46
1.73
1.36
1.38
1.59
1.19
1.16
1.10
1.18
1.35
1.89
1.15
1.40
1.38

1.24
1.22
1.26
1.17
1.27
1.51
1.32
1.33
0.93
1.29
1.25
1.03
1.01
1.56
1.47
1.28
1.37
1.81
1.69
1.61
1.18
1.56
1.28
1.36
1.80
1.52
1.30
1.25
1.35
1.44
2.54
1.55
1.21
1.03
1.47
1.60
1.44
1.12
1.18
1.61
1.42
1.44
1.21
1.26
1.24
1.31
1.20
1.23
1.24
1.49
1.26
1.97
1.15
1.24
1.46
1.73
1.36
1.38
1.59
1.19
1.16
1.10
1.18
1.35
1.89
1.15
1.40
1.38

1.48
4.47
4.26
1.83
2.12
5.34
2.37
2.03
1.54
2.11
1.62
1.72
1.46
2.14
2.32
1.99
6.98
3.48
4.41
5.25
3.02
3.35
1.70
3.10
6.61
2.66
2.12
2.74
2.10
2.16
3.15
2.16
1.98
1.64
5.79
1.95
1.78
1.85
2.06
2.00
2.14
1.96
1.92
1.94
1.81
1.94
2.29
4.23
4.42
7.31
4.65
2.79
1.75
2.26
2.24
5.64
2.06
2.33
8.99
1.58
1.63
1.55
4.45
2.17
3.39
2.06
1.81
9.79

26


cl100k_base

RoBERTa

CamemBERT

PhoBERT

RoCBert

XLM-RoBERTa

M2M100

1.66
7.90
1.98
5.39
5.32
2.58
2.69
1.94
5.11
2.20
2.48
2.33
5.74
2.23
7.94
12.86
2.27
18.76
12.86
2.52
2.11
2.57
2.29
5.00
2.36
2.34
1.99
2.26
5.34
2.31
2.02
1.95
2.13
2.60
15.58
2.39
10.43
5.82
13.09
6.09
2.28
9.05
7.88
2.21
2.39
2.45
2.82
2.78
2.43
2.62
10.39
7.16
5.75
2.24
6.30
2.30
2.00
4.54
2.38
2.14
2.26
6.63
3.89
3.09
3.21
3.16
2.05
2.41

1.66
7.90
1.98
5.39
5.32
2.58
2.69
1.94
5.11
2.20
2.48
2.33
5.74
2.23
7.94
12.86
2.27
18.76
12.86
2.52
2.11
2.57
2.29
5.00
2.36
2.34
1.99
2.26
5.34
2.31
2.02
1.95
2.13
2.60
15.58
2.39
10.43
5.82
13.09
6.09
2.28
9.05
7.88
2.21
2.39
2.45
2.82
2.78
2.43
2.62
10.39
7.16
5.75
2.24
6.30
2.30
2.00
4.54
2.38
2.14
2.26
6.63
3.89
3.09
3.21
3.16
2.05
2.41

1.57
7.87
1.75
3.83
3.28
2.26
1.91
1.48
3.16
2.08
1.88
2.13
2.49
2.08
5.00
12.80
2.01
15.05
8.83
2.14
1.88
2.29
2.13
4.00
2.18
2.21
1.55
1.99
2.92
2.16
1.82
1.58
1.95
2.18
7.65
2.22
10.13
3.75
8.34
3.64
2.06
4.39
7.80
2.04
2.28
2.26
2.40
2.57
1.91
2.51
10.04
5.19
3.00
2.01
4.39
2.17
1.70
2.45
1.95
1.92
2.06
5.57
2.96
2.12
1.91
2.18
1.62
2.20

1.66 1.27 1.25
7.90 8.47
—
1.98 1.33 1.37
5.39 5.37
—
5.32 5.47
—
2.58 1.74 1.69
2.69 1.79 1.71
1.94 1.38 1.36
5.11 5.31
—
2.20 1.61 1.54
2.48 1.69 1.54
2.33 1.63 1.59
5.74 3.67
—
2.23 1.54 1.50
7.94 8.60
—
12.86 8.56
—
2.27 1.57 1.43
18.76 12.51
—
12.86 8.59
—
2.52 1.65 1.60
2.11 1.46 1.44
2.57 1.69 1.63
2.29 1.58 1.58
5.00 5.22
—
2.36 1.66 1.69
2.34 1.64 1.63
1.99 1.45 1.44
2.26 1.53 1.48
5.34 3.41
—
2.31 1.59 1.60
2.02 1.39 1.39
1.95 1.22 1.41
2.13 1.49 1.42
2.60 1.74 1.70
15.58 10.38
—
2.39 1.62 1.50
10.43 6.95
—
5.82 3.84
—
13.09 8.73
—
6.09 4.00
—
2.28 1.63 1.67
9.05 6.59
—
7.88 5.25
—
2.21 1.55 1.66
2.39 1.68 1.67
2.45 1.70 1.70
2.82 1.76 1.78
2.78 1.93 1.85
2.43 1.61 1.65
2.62 1.80 1.57
10.39 6.92
—
7.16 6.44
—
5.75 3.69
—
2.24 1.53 1.48
6.30 5.74
—
2.30 1.63 1.59
2.00 1.38 1.34
4.54 3.06
—
2.38 1.61 1.66
2.14 1.49 1.43
2.26 1.57 1.57
6.63 6.34
—
3.89 2.63
—
3.09 2.78
—
3.21 2.93
—
3.16 2.83
—
2.05 1.42 1.45
2.41 1.65 1.64

1.11
—
1.25
—
—
1.49
1.58
1.30
—
1.40
1.46
1.47
2.71
1.32
—
—
1.37
—
—
1.46
1.32
1.50
1.44
—
1.48
1.48
1.36
1.40
2.45
1.45
1.24
1.31
1.32
1.59
—
1.29
—
—
—
2.82
1.45
2.83
—
1.45
1.55
1.46
1.62
1.67
1.51
1.38
—
—
2.58
1.36
—
1.48
1.23
0.83
1.42
1.28
1.40
—
1.66
—
—
—
1.28
1.47

1.00
—
1.03
—
—
1.26
1.00
1.09
—
1.14
1.13
1.15
1.03
1.02
—
—
1.06
—
—
1.02
1.01
1.09
1.18
—
1.16
1.18
1.19
1.16
—
1.21
1.07
1.02
1.06
0.99
—
—
—
—
—
—
1.27
—
—
1.25
1.21
1.19
1.11
1.34
—
—
—
—
—
1.05
—
1.19
—
0.98
1.25
0.93
1.13
—
0.88
0.36
0.39
0.36
1.15
1.20

1.29
1.57
1.37
1.38
1.10
1.57
1.19
1.11
1.09
1.59
1.24
1.71
1.17
1.66
1.43
—
1.58
4.43
1.35
1.18
1.13
1.92
1.63
1.28
1.39
1.78
1.20
1.61
1.18
1.61
1.22
1.07
1.16
1.65
1.35
1.71
—
1.81
1.33
2.14
1.43
1.08
1.97
1.73
1.85
1.79
1.78
1.92
1.04
1.88
—
1.41
1.21
1.57
1.23
1.33
1.36
1.18
1.55
1.60
1.50
1.58
2.27
0.93
0.97
0.96
0.95
1.55

1.23
1.68
1.32
1.40
1.17
1.49
1.26
1.14
1.15
1.54
1.29
1.63
1.22
1.53
1.69
—
1.53
4.63
1.53
1.24
1.19
1.80
1.58
1.30
1.37
1.60
1.21
1.51
1.26
1.44
1.10
1.10
1.20
1.59
1.55
1.57
—
1.54
—
2.06
1.43
1.27
1.91
1.65
1.68
1.69
1.71
1.88
1.15
1.74
—
3.00
1.28
1.49
1.30
1.37
1.31
1.15
1.45
1.40
1.37
1.61
1.74
1.03
1.05
1.06
1.00
1.35

27

GottBERT

p50k_edit

Pangasinan
1.50 1.66
1.66
Eastern Panjabi
9.44 7.90
7.90
Papiamento
1.65 1.98
1.98
Southern Pashto
4.27 5.39
5.39
Western Persian
3.98 5.32
5.32
Plateau Malagasy
2.12 2.58
2.58
Polish
1.70 2.69
2.69
Portuguese
1.42 1.94
1.94
Dari
3.88 5.11
5.11
Ayacucho Quechua
1.96 2.20
2.20
Romanian
1.70 2.48
2.48
Rundi
2.05 2.33
2.33
Russian
1.64 5.74
5.74
Sango
1.95 2.23
2.23
Sanskrit
4.59 7.94
7.94
Santali
11.92 12.86 12.86
Sicilian
1.81 2.27
2.27
Shan
11.85 18.76 18.76
Sinhala
7.86 12.86 12.86
Slovak
1.82 2.52
2.52
Slovenian
1.67 2.11
2.11
Samoan
2.14 2.57
2.57
Shona
2.01 2.29
2.29
Sindhi
4.20 5.00
5.00
Somali
2.14 2.36
2.36
Southern Sotho
2.07 2.34
2.34
Spanish
1.45 1.99
1.99
Sardinian
1.82 2.26
2.26
Serbian
1.73 5.34
5.34
Swati
2.03 2.31
2.31
Sundanese
1.76 2.02
2.02
Swedish
1.44 1.95
1.95
Swahili
1.86 2.13
2.13
Silesian
1.95 2.60
2.60
Tamil
5.87 15.58 15.58
Tamasheq (Latin script)
1.93 2.39
2.39
Tamasheq (Tifinagh script)
8.42 10.43 10.43
Tatar
2.53 5.82 5.82
Telugu
10.71 13.09 13.09
Tajik
2.70 6.09 6.09
Tagalog
2.00 2.28 2.28
Thai
4.35 9.05 9.05
Tigrinya
7.47 7.88 7.88
Tok Pisin
1.95 2.21 2.21
Tswana
2.12 2.39 2.39
Tsonga
2.16 2.45 2.45
Turkmen
2.23 2.82 2.82
Tumbuka
2.46 2.78 2.78
Turkish
2.09 2.43 2.43
Twi
2.01 2.62 2.62
Central Atlas Tamazight
8.86 10.39 10.39
Uyghur
4.89 7.16 7.16
Ukrainian
1.72 5.75 5.75
Umbundu
1.89 2.24 2.24
Urdu
4.37 6.30 6.30
Northern Uzbek
2.03 2.30 2.30
Venetian
1.56 2.00 2.00
Vietnamese
2.92 4.54 4.54
Waray
2.02 2.38 2.38
Wolof
1.80 2.14 2.14
Xhosa
1.97 2.26 2.26
Eastern Yiddish
4.57 6.63 6.63
Yoruba
2.70 3.89 3.89
Yue Chinese
2.11 3.09 3.09
Chinese (Simplified)
2.00 3.21 3.21
Chinese (Traditional)
2.16 3.16 3.16
Standard Malay
1.83 2.05 2.05
Zulu
2.09 2.41 2.41

p50k_base

r50k_base

GPT-2

LLAMA

Language


mT5

FlanT5

ByT5

CANINE

ArabicBERT

MuRIL

UTF-32

BERT Japanese

SeamlessM4T

NLLB

1.29
1.57
1.37
1.38
1.10
1.57
1.19
1.11
1.09
1.59
1.24
1.71
1.17
1.66
1.43
—
1.58
4.43
1.35
1.18
1.13
1.92
1.63
1.28
1.39
1.78
1.20
1.61
1.18
1.61
1.22
1.07
1.16
1.65
1.35
1.71
—
1.81
1.33
2.14
1.43
1.08
1.97
1.73
1.85
1.79
1.78
1.92
1.04
1.88
—
1.41
1.21
1.57
1.23
1.33
1.36
1.18
1.55
1.60
1.50
1.58
2.27
0.93
0.97
0.96
0.95
1.55

1.22
2.11
1.36
1.64
1.34
1.59
1.31
1.29
1.31
1.42
1.37
1.52
1.27
1.63
1.65
—
1.53
3.28
1.66
1.30
1.20
1.92
1.35
1.74
1.48
1.59
1.31
1.57
1.30
1.41
1.22
1.11
1.25
1.57
1.26
1.64
3.59
1.41
1.42
1.62
1.46
0.99
2.03
1.65
1.68
1.61
1.68
1.61
1.12
1.71
3.48
2.57
1.33
1.47
1.52
1.38
1.36
1.95
1.45
1.44
1.35
1.66
2.06
0.95
0.92
0.98
1.11
1.40

2.18
—
2.28
—
—
3.00
2.82
2.21
—
2.59
1.50
2.78
—
3.14
—
—
2.46
—
—
2.74
2.42
3.09
2.79
—
3.06
2.92
2.23
2.46
—
2.80
2.32
2.22
2.66
2.87
—
2.55
—
—
—
—
2.85
—
—
2.76
3.01
3.13
2.87
3.29
2.67
2.85
—
—
—
2.72
—
2.80
2.21
—
2.66
2.62
2.73
—
—
—
—
—
2.32
2.84

1.00
2.59
1.08
1.66
1.70
1.26
1.13
1.12
1.63
1.08
1.19
1.12
1.98
1.12
2.63
2.79
1.11
3.94
2.64
1.09
1.02
1.22
1.12
1.60
1.14
1.21
1.21
1.19
1.80
1.12
1.05
1.04
1.05
1.10
3.17
1.01
2.29
1.85
2.68
2.01
1.26
2.75
1.75
1.28
1.25
1.20
1.17
1.32
1.12
1.05
2.28
1.97
1.86
1.05
1.76
1.13
1.06
1.39
1.25
1.00
1.06
1.94
1.28
0.87
0.93
0.89
1.12
1.12

1.00 1.45 1.24
1.01 1.43
—
1.05 1.54 1.25
0.95 2.55
—
0.94 1.78 1.11
1.22 2.07 1.64
1.06 2.14 1.52
1.09 1.12 1.30
0.92 1.64 1.09
1.07 1.83 1.47
1.13 1.91 1.33
1.12 1.64 1.54
1.09 2.48 2.50
1.09 1.80 1.45
0.98 1.63
—
1.06 12.71
—
1.05 1.80 1.41
1.42 12.06
—
1.00 8.21
—
1.00 2.01 1.35
1.00 1.81 1.37
1.16 2.13 1.57
1.12 1.80 1.55
0.91 2.51
—
1.14 2.03 1.52
1.20 1.96 1.61
1.19 1.21 1.38
1.16 1.73 1.38
0.99 2.57
—
1.13 1.83 1.55
1.04 1.48 1.33
1.01 1.65 1.21
1.05 1.24 1.45
1.04 2.16 1.52
1.17 1.27
—
0.95 1.90
—
0.94 7.74
—
1.01 3.15
—
1.01 1.33
—
1.11 3.29 2.39
1.26 1.85 1.56
0.96 4.63
—
0.69 5.16
—
1.28 1.92 1.61
1.25 2.02 1.62
1.20 2.01 1.65
1.06 2.19 1.44
1.30 2.19 1.79
1.03 1.96 1.45
0.98 1.81
—
0.89 7.69
—
1.07 3.67
—
1.02 2.75 2.35
1.01 1.74 1.46
0.99 1.36 1.45
1.13 1.98 1.58
1.01 1.57 1.24
1.05 1.27 1.38
1.25 1.80 1.60
0.96 1.68 1.28
1.06 1.67 1.52
1.08 4.42 2.41
0.97 1.64 1.24
0.31 0.93
—
0.34 0.95
—
0.32 0.97
—
1.11 1.07 1.39
1.12 1.76 1.62

1.54
1.35
1.80
—
1.62
2.33
—
1.88
1.58
1.95
—
2.13
—
2.05
1.21
—
1.84
—
—
—
—
2.22
2.06
1.22
2.05
2.16
1.98
1.98
—
2.09
1.80
1.90
1.86
—
1.06
—
—
—
1.21
—
2.08
—
—
2.10
2.25
2.19
—
—
—
—
—
—
—
1.94
1.26
2.12
1.84
—
2.15
1.93
2.05
—
—
—
—
—
1.80
2.15

1.00
1.01
1.05
0.95
0.94
1.22
1.06
1.09
0.92
1.07
1.13
1.12
1.09
1.09
0.98
1.06
1.05
1.42
1.00
1.00
1.00
1.16
1.12
0.91
1.14
1.20
1.19
1.16
0.99
1.13
1.04
1.01
1.05
1.04
1.17
0.95
0.94
1.01
1.01
1.11
1.26
0.96
0.69
1.28
1.25
1.20
1.06
1.30
1.03
0.98
0.89
1.07
1.02
1.01
0.99
1.13
1.01
1.05
1.25
0.96
1.06
1.08
0.97
0.31
0.34
0.32
1.11
1.12

1.21
—
1.30
—
—
1.59
—
1.24
—
1.42
—
1.50
—
1.49
—
—
—
—
—
—
1.30
1.55
1.48
—
1.52
1.54
1.41
1.36
—
1.52
1.31
1.20
1.43
—
—
—
—
—
—
—
1.60
—
—
1.57
1.57
1.64
—
—
—
1.40
—
—
—
1.33
—
1.53
1.23
—
1.52
1.26
1.45
—
—
0.55
0.55
0.57
1.36
1.54

1.11
1.50
1.27
1.45
1.13
1.39
1.37
1.17
1.11
1.28
1.35
1.33
1.34
1.39
1.40
2.49
1.44
1.94
1.68
1.21
1.17
1.60
1.23
1.33
1.39
1.39
1.24
1.44
1.24
1.28
1.04
1.13
1.13
1.52
1.42
1.52
2.43
1.21
1.34
1.57
1.34
1.52
1.44
1.39
1.45
1.30
1.36
1.43
1.14
1.25
2.06
1.40
1.28
1.29
1.30
1.32
1.29
1.18
1.36
1.31
1.21
1.69
1.52
1.05
1.11
1.08
0.96
1.24

1.11 1.56
1.50 7.30
1.27 1.73
1.45 2.87
1.13 2.60
1.39 2.23
1.37 1.76
1.17 1.45
1.11 2.50
1.28 2.06
1.35 1.86
1.33 2.11
1.34 1.75
1.39 2.04
1.40 4.58
2.49 8.99
1.44 1.95
1.94 10.51
1.68 7.02
1.21 2.08
1.17 1.87
1.60 2.26
1.23 2.11
1.33 2.87
1.39 2.16
1.39 2.19
1.24 1.52
1.44 1.97
1.24 2.34
1.28 2.14
1.04 1.80
1.13 1.57
1.13 1.93
1.52 2.09
1.42 6.15
1.52 1.99
2.43 5.37
1.21 2.88
1.34 7.06
1.57 2.90
1.34 2.04
1.52 2.59
1.44 4.24
1.39 2.02
1.45 2.26
1.30 2.23
1.36 2.20
1.43 2.51
1.14 1.61
1.25 2.15
2.06
5.09
1.40 3.74
1.28 2.51
1.29 1.97
1.30 3.19
1.32 2.15
1.29 1.68
1.18 1.41
1.36 1.93
1.31 1.89
1.21 2.04
1.69 2.77
1.52 2.69
1.05 1.17
1.11 1.07
1.08 1.21
0.96 1.61
1.24 2.18

28

Qwen

MBart50

Pangasinan
Eastern Panjabi
Papiamento
Southern Pashto
Western Persian
Plateau Malagasy
Polish
Portuguese
Dari
Ayacucho Quechua
Romanian
Rundi
Russian
Sango
Sanskrit
Santali
Sicilian
Shan
Sinhala
Slovak
Slovenian
Samoan
Shona
Sindhi
Somali
Southern Sotho
Spanish
Sardinian
Serbian
Swati
Sundanese
Swedish
Swahili
Silesian
Tamil
Tamasheq (Latin script)
Tamasheq (Tifinagh script)
Tatar
Telugu
Tajik
Tagalog
Thai
Tigrinya
Tok Pisin
Tswana
Tsonga
Turkmen
Tumbuka
Turkish
Twi
Central Atlas Tamazight
Uyghur
Ukrainian
Umbundu
Urdu
Northern Uzbek
Venetian
Vietnamese
Waray
Wolof
Xhosa
Eastern Yiddish
Yoruba
Yue Chinese
Chinese (Simplified)
Chinese (Traditional)
Standard Malay
Zulu

BLOOM

Language
~~~~~
