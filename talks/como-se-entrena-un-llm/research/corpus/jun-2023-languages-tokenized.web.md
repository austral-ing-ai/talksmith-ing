---
source_file: jun-2023-languages-tokenized
source_type: web-capture
ingested_at: 2026-09-25
---

# All languages are NOT created (tokenized) equal

## Provenance
- Original location: web/jun-2023-languages-tokenized/ (text from `page.md`; `page.md` is 33105 chars with headings, so no `original.html` fallback was needed)
- Format: html (web capture via talksmith:ingest)
- URL: https://www.artfish.ai/p/all-languages-are-not-created-tokenized
- Captured at: 2026-09-25T22:37:10Z
- Page title: All languages are NOT created (tokenized) equal
- Author / source (if known): Yennie Jun, *Art Fish Intelligence* (Substack newsletter, artfish.ai); subtitle 'Language models cost much more in some languages than others'
- Date of original (if known): May 03, 2023 (as printed in the byline); some chart data sourced on May 2, 2023 and April 30, 2023

## Key claims
- LLMs like ChatGPT process text by splitting it into **tokens**; short/common words ("you", "say", "loud", "always") are single tokens while longer/rarer words ("atrocious", "precocious", "supercalifragilisticexpialidocious") are split into subwords.
- Tokenization "is not uniform across languages, leading to disparities in the number of tokens produced for equivalent expressions in different languages."
- "a sentence in Burmese or Amharic may require 10x more tokens than a similar message in English."
- "Some languages, such as Armenian or Burmese, require 9 to 10 times more tokens than English to tokenize comparable messages".
- The phenomenon "is not new to AI — this is consistent with what we observe in Morse code and computer fonts".
- Data: Amazon's MASSIVE parallel dataset (1 million short texts, 52 languages, 18 domains); the `dev` split, 2033 texts per language; CC BY 4.0.
- Focus on OpenAI's BPE tokenizer (ChatGPT, GPT-4) because (1) Denys Linkov found GPT-2's tokenizer had the highest token-length disparity among tokenizers compared; (2) ChatGPT's training data is opaque, so probing the black box helps; (3) ChatGPT's wide adoption (Duolingo, Snapchat) makes equitable processing important.
- Token counts computed with `cl100k_base` (tiktoken), used by `gpt-3.5-turbo` and `gpt-4`.
- English's token-length distribution is "tall and narrow" (consistently few tokens); Hindi and Burmese are "short and wide" (many more tokens).
- "English texts had the smallest median length of 7 tokens and Burmese texts had the largest median length of 72 tokens."
- "Romance languages such as Spanish, French, and Portuguese tended to result in a similar number of tokens as English."
- Hindi and Bengali ("over 800 million people speak either of these languages") have a median token length "about 5 times that of English"; Armenian 9x; Burmese "over 10 times". "to express the same sentiment, some languages require up to 10 times more tokens".
- Implications of more tokens: limited prompt information (fixed context window — "As of March 2023, GPT-3 could take up to 4K tokens and GPT-4 could take up to 8K or 32K tokens"), higher monetary cost, longer run time.
- "According to SimilarWeb.com, the United States only accounted for 10% of the traffic sent to ChatGPT in Jan-March 2023."
- ChatGPT was used "in Pakistan to grant bail in a juvenile kidnapping case" and "in Japan for administrative tasks".
- NLP language divide: "70% of research papers published in a computational linguistics conference only evaluated English"; multilingual models perform worse on low-resource languages; English is "more than half (55.6%) of the content on the Internet" (W3Techs).
- "English makes up over 46% of the Common Crawl corpus", versions of which trained T5 and GPT-3 "(and likely ChatGPT and GPT-4)"; "Common Crawl makes up 60% of GPT-3 training data."
- Call to action: researchers, developers, and linguists should "prioritize and invest in the development of low-resource languages".
- Historical parallel — telegraphy: encoding a Chinese message vs English was "2 times as expensive" and "Took 15-20 times longer"; telegraphy was "designed first and foremost for Western alphabetic languages, English above all"; Viguier's code mapped each Chinese ideogram to a four-digit code then to Morse.
- Font inequity: no single Google Font renders all 52 scripts; the author "manually downloaded the 17 font files necessary".
- Conclusion: "As models like ChatGPT are predominantly trained on English, non-Indo-European and non-Latin script languages face barriers due to prohibitive tokenization costs."
- Appendix: Indo-European, Austronesian, and Uralic languages tokenize shorter; Dravidian (Tamil, Kannada) longer. European-region languages shorter; Middle East, Central Asia, Horn of Africa longer. Unique scripts (Korean, Hebrew, Georgian, …) tokenize longer than Latin scripts.
- "English almost always ranked number one" (fewest tokens per text), with rare exceptions (some Indonesian or Norwegian examples); "there was no clear #2 or #3."
- Earth mover's (Wasserstein) distance shows e.g. "Arabic and Russian have similar distributions even though the languages themselves are not similar in a linguistic sense."

## Definitions and terminology
- **Token** — a smaller unit into which LLMs split text before processing/generation; may be a whole word or a subword.
- **Tokenization** — the process of splitting text into tokens; "Different models use different methods for tokenizing a sentence, such as splitting it into words, into characters, or into parts of words (also known as subwords; e.g. splitting "constantly" into "constant" and "ly")."
- **Byte-Pair Encoding (BPE)** — "meant to decompose rare words into meaningful subwords while keeping frequently used words intact"; the encoding used by OpenAI for ChatGPT models.
- **cl100k_base** — the BPE tokenizer in tiktoken used by `gpt-3.5-turbo` and `gpt-4`.
- **Parallel dataset** — the same short texts translated across languages (MASSIVE: 52 languages, 18 domains).
- **Median token length** — per-language median number of tokens across the 2033 dev texts; ratio to English's median used as the disparity measure.
- **Low-resource vs high-resource languages** — languages with little vs abundant data (English as the high-resource reference).
- **Earth mover's distance / Wasserstein distance** — "calculates the minimum amount of "work" required to transform one distribution into another"; larger = more different distributions; "says nothing about the length of the tokens".
- **Context window** — fixed maximum input length in tokens (GPT-3 4K; GPT-4 8K or 32K as of March 2023).
- **Digital divide in NLP** — disparity in research attention, data, and model performance across languages.
- **Language vs dialect** — author notes debate (Chinese, Arabic as single languages with mutually unintelligible forms; Hindi and Urdu sometimes grouped as Hindustani).

## Evidence and examples
- **Header image (90481db3…_800x600)** — ""hey" translated to 52 different languages. The size of the text is scaled to corresponds to the number of tokens needed to represent the message in the corresponding language. [Edited to fix right-to-left languages]".
- **Tokenizer visualization (a4324946…_1109x872)** — OpenAI tokenizer website coloring each token of a short text.
- **Five-language example (b1282f0a…_1014x410)** — same MASSIVE message in five languages with token counts under OpenAI's tokenizer (exact numbers only in the image).
- **Dashboard screenshot (2c0b4c98…_1037x660)** — HuggingFace space `yenniejun/tokenizers-languages` for comparing token lengths across languages/tokenizers.
- **Distribution plot (97eb1a91…_715x371)** — "Distribution of token lengths for all 2033 messages and 52 languages. Five of the languages have been bolded and colored; the rest are shown in gray."
- **Median token length chart (a0e4ff67…_871x444)** — "A subset of the 52 languages and their median token length." Text-stated: English 7, Burmese 72.
- **Ratio-to-English chart (efc0e934…_871x444)** — "A subset of the 52 languages and the ratio of that language's median token length to that of English." Text-stated: Hindi/Bengali ~5x, Armenian 9x, Burmese >10x.
- **ChatGPT traffic (f65045d2…_737x352)** — "Top 5 countries sending the most traffic to chat.openai.com in Jan-March 2023. Sourced from similarweb.com on May 2, 2023." Text: US only 10%.
- **Web content languages (3df087f2…_896x346)** — "Percentages of websites using various content languages (as of April 30, 2023)" from W3Techs; English 55.6%.
- **Common Crawl** — English "over 46%"; Common Crawl = 60% of GPT-3 training data (Brown et al., 2020).
- **Telegraphy manuscript (c82f52d5…_792x357)** — "Manuscript on left from Zhang Deyim Dianxin xinfa 電信新法, 1873. Danish National Archives." (red circle drawn by author).
- **Broken word cloud (0abed3e3…_1175x790)** — ""hey" in 52 languages" in DroidSansMono; "Many of the languages (including Arabic, Hindi, and Korean) cannot be rendered using a single font".
- **Google Fonts comparison (45003d72…_1470x862)** — 52 languages rendered in 3 Google Fonts, none rendering all.
- **Appendix charts** — by 12 most spoken languages (92cd14d2…), by language family (a55beb79…), by geographic region (815182d2…), by writing script (6f3fc34f…), ranking distribution (d6e02cf2…), earth mover's distance matrix (d11115ae…); values only in images.
- **Deployment anecdotes** — Duolingo (Duolingo Max), Snapchat (My AI); Pakistani court bail decision; Yokosuka (Japan) administrative trial.
- **Reader comments** — Dan Ma (May 19, 2023): "It is strange why the median token length of the Armenian language is so large. The language belongs to the Indo-European family and has much in common with the modern languages of this family, except for the alphabet." Shreeya (Mar 15, 2024) links an extension of the analysis. 13 more comments and a HackerNews thread (item 35983707) not captured.

## Inconsistencies / open questions
- [verified] The headline disparity is phrased with varying language lists across sections: "Burmese or Amharic may require 10x" (intro), "Armenian or Burmese, require 9 to 10 times" (bullets), and "9 times … for Armenian and over 10 times … for Burmese" (Results); Amharic's ratio is never stated in the text — checked across intro, bullet list, and Results.
- [verified] Medians are consistent: 72 / 7 ≈ 10.3, matching "over 10 times that of English for Burmese".
- [verified] Conclusion wording "some languages require up to 10 times more tokens to express the same message in English" is garbled (means "than English").
- [verified] Citation block year mismatch: BibTeX key `Jun2024aimusic` while `year = {2023}` and the plain citation says 2023.
- [verified] Typos in source: "which I explore the reader to do on their own" (likely "encourage"), "This was took a long time", "scaled to corresponds".
- [verified] Author-stated limitations: only OpenAI tokenizers analyzed ("different tokenizers (which was not explored in this article…)"); relies on Wikipedia/WALS/MASSIVE assumptions ("Since I am not a linguistics expert…"); language-vs-dialect ambiguity.
- [verified] Only the MASSIVE `dev` split (2033 texts) was used — short, voice-assistant-style messages; results may not generalize to long-form text (the source does not discuss this, but the dataset description is explicit).
- [open question] All model-specific numbers are dated (cl100k_base; GPT-3 4K / GPT-4 8K–32K context "As of March 2023"; US 10% of ChatGPT traffic Jan–Mar 2023; English 55.6% of web content as of April 30, 2023; English >46% of Common Crawl) — newer tokenizers (e.g., larger-vocabulary ones) may reduce the gap; check current tokenizer comparisons before presenting as current.
- [open question] "Common Crawl makes up 60% of GPT-3 training data" and "likely ChatGPT and GPT-4" were trained on Common Crawl versions — the first can be checked against Brown et al. (2020) Table 2.2; the second is speculation.
- [open question] Telegraphy figures ("2 times as expensive", "15-20 times longer") are from Jing Tsu's book (cited as "Jin Tsu", p. 124) — verify against the book.
- [verified] Extraction gaps: most quantitative results (per-language medians, ratios, family/region/script breakdowns, ranking and EMD charts) exist only as images, not in the captured text; bullet lists are split into empty "- " items; Substack boilerplate ("SubscribeSign in", share buttons, "3015" like/comment counters, "© 2026 Yennie") is interleaved; only 2 of ~15 reader comments are captured.

## Images / diagrams
### `jun-2023-languages-tokenized.web/images/0abed3e3-042d-4335-bb11-d4a57280ae80_1175x790.jpg`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0abed3e3-042d-4335-bb11-d4a57280ae80_1175x790.png` (JPEG image data, Exif standard: [TIFF image data), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/2c0b4c98-2263-4415-8a62-54ad4683c542_1037x660.png`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c0b4c98-2263-4415-8a62-54ad4683c542_1037x660.png` (PNG image data, 1037 x 660), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/3df087f2-834a-481f-920b-4ada423cf71a_896x346.png`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3df087f2-834a-481f-920b-4ada423cf71a_896x346.png` (PNG image data, 896 x 346), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/45003d72-14fd-4860-9d80-a98014217d23_1470x862.jpg`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45003d72-14fd-4860-9d80-a98014217d23_1470x862.png` (JPEG image data, Exif standard: [TIFF image data), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/6f3fc34f-4fd3-431e-b95b-48676513e695_1105x212.jpg`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f3fc34f-4fd3-431e-b95b-48676513e695_1105x212.png` (JPEG image data, Exif standard: [TIFF image data), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/815182d2-8b7b-4c2e-95e0-f4bae6343af1_1105x405.jpg`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F815182d2-8b7b-4c2e-95e0-f4bae6343af1_1105x405.png` (JPEG image data, Exif standard: [TIFF image data), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/90481db3-97f8-480e-b436-629a8f80b837_800x600.jpg`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90481db3-97f8-480e-b436-629a8f80b837_800x600.png` (JPEG image data, Exif standard: [TIFF image data), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/92cd14d2-78b4-446e-a553-eb2a66eb0810_1105x559.jpg`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92cd14d2-78b4-446e-a553-eb2a66eb0810_1105x559.png` (JPEG image data, Exif standard: [TIFF image data), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/97eb1a91-9420-4986-9333-cf387a331549_715x371.jpg`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97eb1a91-9420-4986-9333-cf387a331549_715x371.png` (JPEG image data, Exif standard: [TIFF image data), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/a0e4ff67-72ff-486f-97e0-059aa9ac37ff_871x444.png`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0e4ff67-72ff-486f-97e0-059aa9ac37ff_871x444.png` (PNG image data, 871 x 444), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/a4324946-3557-4e75-accf-f0755c169164_1109x872.png`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4324946-3557-4e75-accf-f0755c169164_1109x872.png` (PNG image data, 1109 x 872), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/a52a68b4-f42d-49c5-8623-daa9dad806a8_1060x222.png`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa52a68b4-f42d-49c5-8623-daa9dad806a8_1060x222.png` (PNG image data, 788 x 140), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "Art Fish Intelligence".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/a55beb79-10e0-4ecb-a370-2229d82671e5_1105x405.jpg`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa55beb79-10e0-4ecb-a370-2229d82671e5_1105x405.png` (JPEG image data, Exif standard: [TIFF image data), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/b1282f0a-4273-41b7-b325-65a55dfea350_1014x410.jpg`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1282f0a-4273-41b7-b325-65a55dfea350_1014x410.png` (JPEG image data, Exif standard: [TIFF image data), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/c82f52d5-2a6a-4c26-88f3-0253e05893b0_792x357.png`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc82f52d5-2a6a-4c26-88f3-0253e05893b0_792x357.png` (PNG image data, 792 x 357), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/d11115ae-cc33-42e6-aa49-9b38cb16e751_817x733.jpg`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd11115ae-cc33-42e6-aa49-9b38cb16e751_817x733.png` (JPEG image data, Exif standard: [TIFF image data), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/d6e02cf2-7698-4476-8563-a88136874a6d_694x371.jpg`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6e02cf2-7698-4476-8563-a88136874a6d_694x371.png` (JPEG image data, Exif standard: [TIFF image data), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/efc0e934-0f0f-4dd9-8ea6-4953ea538ce0_871x444.png`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefc0e934-0f0f-4dd9-8ea6-4953ea538ce0_871x444.png` (PNG image data, 871 x 444), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### `jun-2023-languages-tokenized.web/images/f65045d2-27d2-4481-86a3-3fc5f6472285_737x352.png`
- Provenance: web asset `web/jun-2023-languages-tokenized/assets/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff65045d2-27d2-4481-86a3-3fc5f6472285_737x352.png` (PNG image data, 737 x 352), captured from https://www.artfish.ai/p/all-languages-are-not-created-tokenized. Alt text: "".
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->


## Raw / preserved excerpts
> "Large language models such as ChatGPT process and generate text sequences by first splitting the text into smaller units called tokens. In the image below, each colored block represents a unique token. Short or common words such as "you", "say", "loud", and "always" are its own token, whereas longer or less common words such as "atrocious", "precocious", and "supercalifragilisticexpialidocious" are broken into smaller subwords."
— Introduction

> "This process of tokenization is not uniform across languages, leading to disparities in the number of tokens produced for equivalent expressions in different languages. For example, a sentence in Burmese or Amharic may require 10x more tokens than a similar message in English."
— Introduction

> "MASSIVE is a parallel dataset introduced by Amazon consisting of 1 million realistic, parallel short texts translated across 52 languages and 18 domains. I used the `dev` split of the dataset, which consists of 2033 texts translated into each of the languages."
— Data

> "To calculate the number of tokens a text contains, I use the `cl100k_base` tokenizer available on tiktoken, which is the BPE tokenizer used by OpenAI's ChatGPT models (`gpt-3.5-turbo` and `gpt-4`)."
— A focus on OpenAI's Tokenizers

> "For each language, I calculated the median token length for all of the texts in the dataset. The following chart compares a subset of the languages. English texts had the smallest median length of 7 tokens and Burmese texts had the largest median length of 72 tokens. Romance languages such as Spanish, French, and Portuguese tended to result in a similar number of tokens as English."
— Results: English has the shortest median token length

> "As English had the shortest median token length, I calculated the ratio of the other languages' median token length to that of English. Languages such as Hindi and Bengali (over 800 million people speak either of these languages) resulted in a median token length of about 5 times that of English. The ratio is 9 times that of English for Armenian and over 10 times that of English for Burmese. In other words, to express the same sentiment, some languages require up to 10 times more tokens."
— Results

> "Overall, requiring more tokens (to tokenize the same message in a different language) means: You're limited by how much information you can put in the prompt (because the context window is fixed). As of March 2023, GPT-3 could take up to 4K tokens and GPT-4 could take up to 8K or 32K tokens in its input. It costs more money. It takes longer to run"
— Discussion: Implications of tokenization language disparity

> "OpenAI's models are increasingly being used in countries where English is not the dominant language. According to SimilarWeb.com, the United States only accounted for 10% of the traffic sent to ChatGPT in Jan-March 2023."
— Discussion

> "This digital divide in natural language processing (NLP) is an active area of research. 70% of research papers published in a computational linguistics conference only evaluated English. Multilingual models perform worse on several NLP tasks on low resource languages than on high resource languages such as English. According to W3Techs (World Wide Web Technology Surveys), English dominates more than half (55.6%) of the content on the Internet."
— Language Disparity in Natural Language Processing

> "Similarly, English makes up over 46% of the Common Crawl corpus (billions of webpages from the Internet crawled for over a decade), versions of which have been used to train many large languages such as Google's T5 and OpenAI's GPT-3 (and likely ChatGPT and GPT-4). Common Crawl makes up 60% of GPT-3 training data."
— Language Disparity in Natural Language Processing

> "Over a hundred years ago, telegraphy, a revolutionary technology of its time ("the internet of its era"), faced language inequities similar to those we see in today's large language models. Despite its promises of open exchange and collaboration, telegraphy exhibited discrepancies in speed and cost across languages. For instance, encoding and transmitting a message in Chinese (compared to an equivalent message in English) was 2 times as expensive. Took 15-20 times longer. Sound familiar?"
— Historical example: Chinese typography in Morse code

> "Essentially, each Chinese ideogram was mapped to a four-digit code, which had to then be translated into Morse code. This was took a long time looking up the codes in the codebook (which lacked meaningful correlations) and was more costly to transmit (as each character was represented by four digits, and a single digit was more expensive to transmit than a single letter)."
— Historical example

> "Language disparities in NLP tokenization reveal a pressing issue in AI: equity and inclusivity. As models like ChatGPT are predominantly trained on English, non-Indo-European and non-Latin script languages face barriers due to prohibitive tokenization costs. Addressing these disparities is essential to ensure a more inclusive and accessible future for artificial intelligence, ultimately benefiting diverse linguistic communities worldwide."
— Conclusion

> "One common tokenization is called Byte-Pair Encoding (BPE). This is the encoding used by OpenAI for their ChatGPT models. BPE is meant to decompose rare words into meaningful subwords while keeping frequently used words intact."
— Appendix: Byte-Pair Encoding Tokenization

> "Breakdown by writing script. Other than the Latin, Arabic, and Cyrillic alphabets, all other languages use their own unique script. While the latter combines many very different unique scripts (such as Korean, Hebrew, and Georgian scripts), these unique scripts definitely tokenize to longer values. Compared to Latin-based scripts, which tokenize to shorter values."
— Appendix

> "While there were a few cases where some languages' tokens were fewer than that of English (such as a few examples in Indonesian or Norwegian), English almost always ranked number one. Does this come as a surprise to anyone? What surprised me most was that there was no clear #2 or #3. English language texts consistently produce the shortest tokens, and the ranking fluctuates a bit more for other languages."
— Appendix: English almost always ranks #1

### Full extracted text (verbatim)
Complete `page.md` as captured, verbatim (image links inside point to the raw `assets/` names; see *Images / diagrams* above for the companion-folder paths).

~~~~~text
# All languages are NOT created (tokenized) equal

_Source: <https://www.artfish.ai/p/all-languages-are-not-created-tokenized>_

![Art Fish Intelligence](https://substackcdn.com/image/fetch/$s_!8_QG!,w_40,h_40,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c6d96a8-9e6c-421e-b411-211798d04fe4_256x256.png)</>

# ![Art Fish Intelligence](https://substackcdn.com/image/fetch/$s_!Ta7E!,e_trim:10:white/e_trim:10:transparent/h_140,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa52a68b4-f42d-49c5-8623-daa9dad806a8_1060x222.png)</>

SubscribeSign in

# All languages are NOT created (tokenized) equal

### Language models cost much more in some languages than others

![Yennie Jun's avatar](https://substackcdn.com/image/fetch/$s_!LD8N!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd4bfb60-9b3c-495d-932b-904448517e72_2419x3513.png)<https://substack.com/@artfish>[Yennie Jun](https://substack.com/@artfish)May 03, 20233015Share![](https://substackcdn.com/image/fetch/$s_!zdyf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90481db3-97f8-480e-b436-629a8f80b837_800x600.png)<https://substackcdn.com/image/fetch/$s_!zdyf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90481db3-97f8-480e-b436-629a8f80b837_800x600.png>“hey” translated to 52 different languages. The size of the text is scaled to corresponds to the number of tokens needed to represent the message in the corresponding language. [Edited to fix right-to-left languages]

Large language models such as ChatGPT process and generate text sequences by first splitting the text into smaller units called **tokens**. In the image below, each colored block represents a unique token. Short or common words such as “you”, “say”, “loud”, and “always” are its own token, whereas longer or less common words such as “atrocious”, “precocious”, and “supercalifragilisticexpialidocious” are broken into smaller subwords.

![](https://substackcdn.com/image/fetch/$s_!zunw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4324946-3557-4e75-accf-f0755c169164_1109x872.png)<https://substackcdn.com/image/fetch/$s_!zunw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa4324946-3557-4e75-accf-f0755c169164_1109x872.png>Visualization of tokenization of a short text using [OpenAI’s tokenizer website](https://platform.openai.com/tokenizer).

This process of **tokenization** is not uniform across languages, leading to disparities in the number of tokens produced for equivalent expressions in different languages. For example, **a sentence in Burmese or Amharic may require 10x more tokens than a similar message in English.** 

![](https://substackcdn.com/image/fetch/$s_!9Cco!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1282f0a-4273-41b7-b325-65a55dfea350_1014x410.png)<https://substackcdn.com/image/fetch/$s_!9Cco!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb1282f0a-4273-41b7-b325-65a55dfea350_1014x410.png>An example of the same message translated into five languages and the corresponding number of tokens required to tokenize that message (using OpenAI’s tokenizer). The text comes from [Amazon’s MASSIVE dataset](https://www.amazon.science/blog/amazon-releases-51-language-dataset-for-language-understanding).

In this article, I explore the tokenization process and how it varies across different languages:

- 

Analysis of token distributions in a parallel dataset of short messages that have been translated into 52 different languages

- 

Some languages, such as Armenian or Burmese, require **9 to 10 times more tokens than English** to tokenize comparable messages

- 

The impact of this language disparity

- 

**This phenomenon is not new to AI **— this is consistent with what we observe in Morse code and computer fonts** **

#### Try it yourself!

[Try out the exploratory dashboard I made, available on HuggingFace spaces](https://huggingface.co/spaces/yenniejun/tokenizers-languages). Here, you can compare the token lengths for different languages and for different tokenizers (which was not explored in this article, but which I explore the reader to do on their own).

![](https://substackcdn.com/image/fetch/$s_!40kv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c0b4c98-2263-4415-8a62-54ad4683c542_1037x660.png)<https://substackcdn.com/image/fetch/$s_!40kv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c0b4c98-2263-4415-8a62-54ad4683c542_1037x660.png>

🎨 art fish intelligence 🐡 is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

# Data

[MASSIVE](https://arxiv.org/abs/2204.08582) is a parallel dataset [introduced by Amazon](https://github.com/alexa/massive) consisting of 1 million realistic, parallel short texts translated across 52 languages and 18 domains. I used the `dev` split of the dataset, which consists of **2033 texts translated into each of the languages**. The dataset is [available on HuggingFace](https://huggingface.co/datasets/AmazonScience/massive) and is licensed under the [CC BY 4.0 license](https://huggingface.co/datasets/AmazonScience/massive/blob/main/massive.py).

## A focus on OpenAI’s Tokenizers

While many other language model tokenizers exist, this article mainly focuses on [OpenAI's Byte Pair Encoding (BPE) tokenizer](https://platform.openai.com/tokenizer) (used by ChatGPT and GPT-4) for three main reasons:

- 

First, [Denys Linkov's article](https://denyslinkov.medium.com/why-is-gpt-3-15-77x-more-expensive-for-certain-languages-2b19a4adc4bc) compared several tokenizers and found that GPT-2's tokenizer had the highest token length disparity among different languages. This prompted me to concentrate on OpenAI models, including GPT-2 and its successors.

- 

Second, since we lack insight into ChatGPT's full training dataset, investigating OpenAI's black box models and tokenizers help to better understand their behaviors and outputs.

- 

Finally, the widespread adoption of ChatGPT in various applications (from language learning platforms like [Duolingo](https://blog.duolingo.com/duolingo-max/) to social media apps like [Snapchat](https://newsroom.snap.com/say-hi-to-my-ai)) highlights the importance of understanding tokenization nuances to ensure equitable language processing across diverse linguistic communities.

To calculate the number of tokens a text contains, I use the `cl100k_base` tokenizer available on [tiktoken](https://github.com/openai/tiktoken), which is the BPE tokenizer used by OpenAI’s ChatGPT models (`gpt-3.5-turbo` and `gpt-4`). 

Thanks for reading 🎨 art fish intelligence 🐡. This post is public so feel free to share it.

[Share](https://www.artfish.ai/p/all-languages-are-not-created-tokenized?utm_source=substack&utm_medium=email&utm_content=share&action=share)

# Results

#### Some languages consistently tokenize to longer lengths

The following distribution plot compares the distribution of token lengths for five languages. The curve for English is tall and narrow, meaning that English texts consistently tokenize to a smaller number of tokens. On the other hand, the curve for languages such as Hindi and Burmese are short and wide, meaning that these languages tokenize texts into many more tokens.

![](https://substackcdn.com/image/fetch/$s_!WzwO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97eb1a91-9420-4986-9333-cf387a331549_715x371.png)<https://substackcdn.com/image/fetch/$s_!WzwO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97eb1a91-9420-4986-9333-cf387a331549_715x371.png>Distribution of token lengths for all 2033 messages and 52 languages. Five of the languages have been bolded and colored; the rest are shown in gray.

#### English has the shortest median token length

For each language, I calculated the median token length for all of the texts in the dataset. The following chart compares a subset of the languages. English texts had the smallest median length of 7 tokens and Burmese texts had the largest median length of 72 tokens. Romance languages such as Spanish, French, and Portuguese tended to result in a similar number of tokens as English.

![](https://substackcdn.com/image/fetch/$s_!2lVh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0e4ff67-72ff-486f-97e0-059aa9ac37ff_871x444.png)<https://substackcdn.com/image/fetch/$s_!2lVh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0e4ff67-72ff-486f-97e0-059aa9ac37ff_871x444.png>A subset of the 52 languages and their median token length.

As English had the shortest median token length, I calculated the ratio of the other languages’ median token length to that of English. Languages such as Hindi and Bengali (over 800 million people speak either of these languages) resulted in a median token length of about 5 times that of English. The ratio is 9 times that of English for Armenian and over 10 times that of English for Burmese. In other words, **to express the same sentiment, some languages require up to 10 times more tokens**.

![](https://substackcdn.com/image/fetch/$s_!S_iw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefc0e934-0f0f-4dd9-8ea6-4953ea538ce0_871x444.png)<https://substackcdn.com/image/fetch/$s_!S_iw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fefc0e934-0f0f-4dd9-8ea6-4953ea538ce0_871x444.png>A subset of the 52 languages and the ratio of that language’s median token length to that of English.

Thanks for reading 🎨 art fish intelligence 🐡. This post is public so feel free to share it.

[Share](https://www.artfish.ai/p/all-languages-are-not-created-tokenized?utm_source=substack&utm_medium=email&utm_content=share&action=share)

# Discussion

### Implications of tokenization language disparity

Overall, requiring more tokens (to tokenize the same message in a different language) means:

- 

You’re limited by how much information you can put in the prompt (because the context window is fixed). As of March 2023, GPT-3 could take up to 4K tokens and GPT-4 could take up to 8K or 32K tokens in its input.[1](#footnote-1) 

- 

It costs more money

- 

It takes longer to run

OpenAI’s models are increasingly being used in countries where English is not the dominant language. According to SimilarWeb.com, the United States only accounted for 10% of the traffic sent to ChatGPT in Jan-March 2023. 

![](https://substackcdn.com/image/fetch/$s_!44GO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff65045d2-27d2-4481-86a3-3fc5f6472285_737x352.png)<https://substackcdn.com/image/fetch/$s_!44GO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff65045d2-27d2-4481-86a3-3fc5f6472285_737x352.png>Top 5 countries sending the most traffic to chat.openai.com in Jan-March 2023. Sourced from [similarweb.com](https://www.similarweb.com/website/chat.openai.com/#traffic) on May 2, 2023.

Additionally, ChatGPT was used [in Pakistan to grant bail in a juvenile kidnapping case](https://interestingengineering.com/culture/pakistani-court-utilizes-chatgpt-4-to-grant-bail) and [in Japan for administrative tasks](https://www.japantimes.co.jp/news/2023/04/20/national/chatgpt-yokosuka-trial/). As ChatGPT and similar models are becoming increasingly integrated into products and services worldwide, it is crucial to understand and address such inequalities.

### Language Disparity in Natural Language Processing

This digital divide in natural language processing (NLP) is an active area of research. 70% of research papers published in a computational linguistics conference only evaluated English.[2](#footnote-2) Multilingual models perform worse on several NLP tasks on low resource languages than on high resource languages such as English.[3](#footnote-3) According to [W3Techs](https://w3techs.com/) (World Wide Web Technology Surveys), English dominates more than half (55.6%) of the content on the Internet.[4](#footnote-4) 

![](https://substackcdn.com/image/fetch/$s_!p50p!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3df087f2-834a-481f-920b-4ada423cf71a_896x346.png)<https://substackcdn.com/image/fetch/$s_!p50p!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3df087f2-834a-481f-920b-4ada423cf71a_896x346.png>Percentages of websites using various content languages (as of April 30, 2023). Data source: https://w3techs.com/technologies/overview/content_language.

Similarly, English makes up [over 46% of the Common Crawl corpus](https://commoncrawl.github.io/cc-crawl-statistics/plots/languages) (billions of webpages from the Internet [crawled for over a decade](https://commoncrawl.org/the-data/)), versions of which have been used to train many large languages such as Google’s T5 and OpenAI’s GPT-3 (and likely ChatGPT and GPT-4). Common Crawl makes up 60% of GPT-3 training data.[5](#footnote-5)

Addressing the digital divide in NLP is crucial to ensure equitable language representation and performance in AI-driven technologies. Bridging this gap calls for a concerted effort from researchers, developers, and linguists to prioritize and invest in the development of low-resource languages, fostering a more inclusive and diverse linguistic landscape in the realm of natural language processing.

### Historical example: Representing Chinese Typography using Morse Code

Such a disparity of technological costs for different languages is not new to AI or even to computing. 

Over a hundred years ago, telegraphy, a revolutionary technology of its time (“the internet of its era”), faced language inequities similar to those we see in today’s large language models. Despite its promises of open exchange and collaboration, telegraphy exhibited discrepancies in speed and cost across languages. For instance, encoding and transmitting a message in Chinese (compared to an equivalent message in English) was 

- 

2 times as expensive

- 

Took 15-20 times longer

Sound familiar?

Telegraphy was “designed first and foremost* *for Western alphabetic languages, English above all.”[6](#footnote-6) Morse code assigned different lengths and costs to dots and dashes, resulting in a cost-efficient system for English. However, the Chinese language, which relies on ideograms, faced challenges in telegraphy. A Frenchman named Viguier devised a mapping system for Chinese characters to Morse code.

Essentially, each Chinese ideogram was mapped to a four-digit code, which had to then be translated into Morse code. This was took a long time looking up the codes in the codebook (which lacked meaningful correlations) and was more costly to transmit (as each character was represented by four digits, and a single digit was more expensive to transmit than a single letter). This practice put the Chinese language at a disadvantage compared to other languages in terms of telegraphic speed and cost.

![](https://substackcdn.com/image/fetch/$s_!C0Gw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc82f52d5-2a6a-4c26-88f3-0253e05893b0_792x357.png)<https://substackcdn.com/image/fetch/$s_!C0Gw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc82f52d5-2a6a-4c26-88f3-0253e05893b0_792x357.png>Manuscript on left from Zhang Deyim *Dianxin xinfa* 電信新法, 1873. Danish National Archives. http://www5.kb.dk/permalink/2006/manus/350/eng/32/. Red circle drawn in by author.

### Another example: Inequity in representing fonts

Initially, I tried to visualize all 52 languages in a single word cloud. I ended up with something like this, where a majority of the languages were not rendered properly.

![](https://substackcdn.com/image/fetch/$s_!VkX6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0abed3e3-042d-4335-bb11-d4a57280ae80_1175x790.png)<https://substackcdn.com/image/fetch/$s_!VkX6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0abed3e3-042d-4335-bb11-d4a57280ae80_1175x790.png>Word cloud visualizing “hey” in 52 languages. Many of the languages (including Arabic, Hindi, and Korean) cannot be rendered using a single font (depicted is the [default WordCloud font](https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html) DroidSansMono). Size corresponds to the number of tokens required to represent “hey” in that language.

This led me down a rabbit hole of trying to find a font that could render all of the language scripts. I went on Google Fonts to find this perfect font and found that one did not exist. Below is a screenshot showing how these 52 languages would render in 3 different fonts from Google Fonts. 

![](https://substackcdn.com/image/fetch/$s_!w3aN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45003d72-14fd-4860-9d80-a98014217d23_1470x862.png)<https://substackcdn.com/image/fetch/$s_!w3aN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45003d72-14fd-4860-9d80-a98014217d23_1470x862.png>

To generate the word cloud at the beginning of this article, I (ehm) manually downloaded the 17 font files necessary to render all of the language scripts and displayed words one at a time. While I got the desired effect, it was a lot more work than it would have been if, for example, all of my languages used the same script (such as the Latin alphabet).

# Conclusion

In this article, I explored the language disparity in language models by looking at how they process text through tokenization.

- 

Using a dataset of parallel texts translated into 52 languages, I showed that some languages require up to 10 times more tokens to express the same message in English

- 

I shared a [dashboard where you can explore different languages and tokenizers](https://huggingface.co/spaces/yenniejun/tokenizers-languages)

- 

I discussed the impacts of this disparity on certain languages in terms of performance, monetary cost, and time

- 

I showed how this pattern of linguistic technological disparity is not new, comparing the phenomenon to the historical case of Chinese Morse code and telegraphy

Language disparities in NLP tokenization reveal a pressing issue in AI: equity and inclusivity. As models like ChatGPT are predominantly trained on English, non-Indo-European and non-Latin script languages face barriers due to prohibitive tokenization costs. Addressing these disparities is essential to ensure a more inclusive and accessible future for artificial intelligence, ultimately benefiting diverse linguistic communities worldwide.

🎨 art fish intelligence 🐡 is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

[Leave a comment](https://www.artfish.ai/p/all-languages-are-not-created-tokenized/comments)

*[Interested in more discussions? Read the comments on [HackerNews](https://news.ycombinator.com/item?id=35983707)!]*

---

# APPENDIX

### Byte-Pair Encoding Tokenization

In the realm of natural language processing, tokenizers play a crucial role in enabling language models to process and understand text. Different models use different methods for tokenizing a sentence, such as splitting it into words, into characters, or into parts of words (also known as subwords; e.g. splitting "constantly" into "constant" and "ly"). 

One common tokenization is called [Byte-Pair Encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding) (BPE). This is the encoding used by OpenAI for their ChatGPT models. BPE is meant to decompose rare words into meaningful subwords while keeping frequently used words intact. A comprehensive explanation of the BPE algorithm can be found on the [HuggingFace Transformers course](https://huggingface.co/docs/transformers/tokenizer_summary).

### Deeper Dive into Token Distribution for Languages 

I augmented Amazon’s MASSIVE dataset by using information about each of the 52 languages using the infobox section of that language’s Wikipedia page, obtaining information such as writing script (e.g. Latin, Arabic alphabet) and main geographic region the language is predominant in (if relevant). I additionally use metadata from [The World Atlas of Language Structures](https://wals.info) to obtain information such as [language family](https://en.wikipedia.org/wiki/Language_family) (e.g. Indo-European, Sino-Tibetan).[7](#footnote-7)

Note that the following analyses in this article uphold the assumptions made by Wikipedia, The World Atlas of Language Structures, and by the Amazon MASSIVE dataset. Since I am not a linguistics expert, I had to assume that whatever on Wikipedia and the World Atlas were canonically accepted as correct with regards to dominant geographic region or language family. 

Also, there are debates about what constitutes a language versus a dialect. For example, while languages such as Chinese and Arabic have different forms that people may not understand, they are still called single languages. On the other hand, Hindi and Urdu are very similar and are sometimes grouped together as one language called Hindustani. Because of these challenges, we need to be careful when deciding what counts as a language or a dialect.

**Breakdown by language. **I chose the [12 most spoken languages](https://en.wikipedia.org/wiki/List_of_languages_by_total_number_of_speakers) (a combination of both first-language and second-language speakers). 

![](https://substackcdn.com/image/fetch/$s_!aCeG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92cd14d2-78b4-446e-a553-eb2a66eb0810_1105x559.png)<https://substackcdn.com/image/fetch/$s_!aCeG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92cd14d2-78b4-446e-a553-eb2a66eb0810_1105x559.png>

**Breakdown by language family. **Indo-European (e.g. Swedish, French), Austronesian languages (e.g. Indonesian, Tagalog), and Uralic languages (e.g. Hungarian, Finnish) resulted in shorter tokens. Dravidian languages (e.g. Tamil, Kannada) tended to have longer tokens.

![](https://substackcdn.com/image/fetch/$s_!hYna!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa55beb79-10e0-4ecb-a370-2229d82671e5_1105x405.png)<https://substackcdn.com/image/fetch/$s_!hYna!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa55beb79-10e0-4ecb-a370-2229d82671e5_1105x405.png>

**Breakdown by main geographic region. **Not all languages were specific to a single geographic region (such as Arabic, English, and Spanish, which are spread across many regions) — these languages were removed from this section. Languages spoken mostly in Europe tend to be shorter in token length, while languages spoken mostly in the Middle East, Central Asia, and the Horn of Africa tended to be longer in token length.

![](https://substackcdn.com/image/fetch/$s_!h0Q8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F815182d2-8b7b-4c2e-95e0-f4bae6343af1_1105x405.png)<https://substackcdn.com/image/fetch/$s_!h0Q8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F815182d2-8b7b-4c2e-95e0-f4bae6343af1_1105x405.png>

**Breakdown by writing script. **Other than the Latin, Arabic, and Cyrillic alphabets, all other languages use their own unique script. While the latter combines many very different unique scripts (such as Korean, Hebrew, and Georgian scripts), these unique scripts definitely tokenize to longer values. Compared to Latin-based scripts, which tokenize to shorter values.

![](https://substackcdn.com/image/fetch/$s_!485P!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f3fc34f-4fd3-431e-b95b-48676513e695_1105x212.png)<https://substackcdn.com/image/fetch/$s_!485P!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f3fc34f-4fd3-431e-b95b-48676513e695_1105x212.png>

### English almost always ranks #1

For each text in the dataset, I ranked all languages based on number of tokens — the language with the least tokens was ranked #1 and the one with the most tokens was ranked #52. Then, I plotted the distribution of each language’s *ranking*. Essentially, this should show how each language’s token length compares with the other languages in this dataset. In the below figure, I labeled a few of the languages (the other languages show up as gray lines in the background).

While there were a few cases where some languages’ tokens were fewer than that of English (such as a few examples in Indonesian or Norwegian), English almost always ranked number one. Does this come as a surprise to anyone? What surprised me most was that there was no clear #2 or #3. English language texts consistently produce the shortest tokens, and the ranking fluctuates a bit more for other languages.

![](https://substackcdn.com/image/fetch/$s_!m5h_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6e02cf2-7698-4476-8563-a88136874a6d_694x371.png)<https://substackcdn.com/image/fetch/$s_!m5h_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6e02cf2-7698-4476-8563-a88136874a6d_694x371.png>

### Quantifying token distributions differences using Earth Mover’s Distance

To quantify how different the token length distribution between two languages were, I calculated the [earth mover’s distance](https://en.wikipedia.org/wiki/Earth_mover%27s_distance) (also known as the [Wasserstein distance](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wasserstein_distance.html)) between two distributions. Essentially, this metric calculates the minimum amount of “work” required to transform one distribution into another. Larger values mean the distributions are farther apart (more different) while smaller values mean the distributions are quite similar. 

Here is a small subset of languages. Note that the distance says nothing about the length of the tokens, just how similar the distribution of token lengths are for two languages. For example, Arabic and Russian have similar distributions even though the languages themselves are not similar in a linguistic sense.

![](https://substackcdn.com/image/fetch/$s_!1uuM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd11115ae-cc33-42e6-aa49-9b38cb16e751_817x733.png)<https://substackcdn.com/image/fetch/$s_!1uuM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd11115ae-cc33-42e6-aa49-9b38cb16e751_817x733.png>

[Leave a comment](https://www.artfish.ai/p/all-languages-are-not-created-tokenized/comments)

## **Citation**

For attribution in academic contexts or books, please cite this work as

```
Yennie Jun, "All languages are NOT created (tokenized) equal," Art Fish Intelligence, 2023.
```

```
@article{Jun2024aimusic,
    author = {Yennie Jun},
    title = {All languages are NOT created (tokenized) equal},
    journal = {Art Fish Intelligence},
    year = {2023},
    howpublished = {\url{https://www.artfish.ai/p/all-languages-are-not-created-tokenized},
}
```

[1](#footnote-anchor-1)

OpenAI. ["Models"](https://platform.openai.com/docs/models). *OpenAI API*. [Archived](https://web.archive.org/web/20230317000210/https://platform.openai.com/docs/models) from the original on March 17, 2023. Retrieved March 18, 2023.

[2](#footnote-anchor-2)

Sebastian Ruder, Ivan Vulić, and Anders Søgaard. 2022.[Square One Bias in NLP: Towards a Multi-Dimensional Exploration of the Research Manifold](https://aclanthology.org/2022.findings-acl.184). In *Findings of the Association for Computational Linguistics: ACL 2022*, pages 2340–2354, Dublin, Ireland. Association for Computational Linguistics.

[3](#footnote-anchor-3)

Shijie Wu and Mark Dredze. 2020.[Are All Languages Created Equal in Multilingual BERT?](https://aclanthology.org/2020.repl4nlp-1.16). In *Proceedings of the 5th Workshop on Representation Learning for NLP*, pages 120–130, Online. Association for Computational Linguistics.

[4](#footnote-anchor-4)

[Usage statistics of content languages for websites"](https://w3techs.com/technologies/overview/content_language).[Archived](https://archive.ph/RzLBr) from the original on 30 April 2023.

[5](#footnote-anchor-5)

Brown, Tom, et al. "Language models are few-shot learners." *Advances in neural information processing systems* 33 (2020): 1877-1901.

[6](#footnote-anchor-6)

Jin Tsu. Kingdom of Characters: The Language Revolution That Made China Modern. New York: Riverhead Books, 2022 (p. 124).

[7](#footnote-anchor-7)

Dryer, Matthew S. & Haspelmath, Martin (eds.) 2013. WALS Online (v2020.3) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7385533. Available online at https://wals.info, Accessed on 2023-04-30.

3015SharePreviousNext

#### Discussion about this post

CommentsRestacks![Shreeya's avatar](https://substackcdn.com/image/fetch/$s_!SCru!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ccf9e7e-b918-482e-b8ed-800ad52e084e_1176x982.jpeg)<https://substack.com/profile/104468357-shreeya?utm_source=comment>[Shreeya](https://substack.com/profile/104468357-shreeya?utm_source=substack-feed-item)[Mar 15, 2024](https://www.artfish.ai/p/all-languages-are-not-created-tokenized/comment/51697536)Liked by Yennie Jun

Hey, I enjoyed reading this and did some exploration on my own here: [https://www.icodeformybhasa.com/p/beyond-the-abcs-exploring-the-nuances](https://www.icodeformybhasa.com/p/beyond-the-abcs-exploring-the-nuances). I was hoping if I could merge some parts of my dashboard with yours! 

ReplyShare[1 reply by Yennie Jun](https://www.artfish.ai/p/all-languages-are-not-created-tokenized/comment/51697536)![Dan Ma's avatar](https://substackcdn.com/image/fetch/$s_!Cbt7!,w_32,h_32,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F68530587-cb63-4727-9bda-ae123c51b370_144x144.png)<https://substack.com/profile/3525701-dan-ma?utm_source=comment>[Dan Ma](https://substack.com/profile/3525701-dan-ma?utm_source=substack-feed-item)[May 19, 2023](https://www.artfish.ai/p/all-languages-are-not-created-tokenized/comment/16310974)Liked by Yennie Jun

It is strange why the median token length of the Armenian language is so large. The language belongs to the Indo-European family and has much in common with the modern languages of this family, except for the alphabet. 

ReplyShare[1 reply by Yennie Jun](https://www.artfish.ai/p/all-languages-are-not-created-tokenized/comment/16310974)[13 more comments...](https://www.artfish.ai/p/all-languages-are-not-created-tokenized/comments)TopLatestDiscussions

No posts

### Ready for more?

© 2026 Yennie · [Privacy](https://substack.com/privacy) ∙ [Terms](https://substack.com/tos) ∙ [Collection notice](https://substack.com/ccpa#personal-data-collected)[Start your Substack](https://substack.com/signup?utm_source=substack&utm_medium=web&utm_content=footer)[Get the app](https://substack.com/app/app-store-redirect?utm_campaign=app-marketing&utm_content=web-footer-button)[Substack](https://substack.com) is the home for great culture
~~~~~
