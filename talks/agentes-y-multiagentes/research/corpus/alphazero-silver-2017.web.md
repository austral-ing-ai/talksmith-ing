---
source_file: alphazero-silver-2017/
source_type: web-capture
ingested_at: 2026-10-04
---

# Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm (Silver et al., arXiv:1712.01815) — abstract page only

## Provenance
- Original location: research/web/alphazero-silver-2017/ (text from `page.md`)
- Format: html (arXiv abstract page, web capture via talksmith:ingest)
- URL: https://arxiv.org/abs/1712.01815
- Fetched: 2026-08-14T16:56:50Z (HTTP 200)
- Author / source (if known): David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai, Arthur Guez, Marc Lanctot, Laurent Sifre, Dharshan Kumaran, Thore Graepel, Timothy Lillicrap, Karen Simonyan, Demis Hassabis (DeepMind)
- Date of original (if known): submitted 5 Dec 2017 (v1, 18:45:38 UTC). Subjects cs.AI, cs.LG. DOI 10.48550/arXiv.1712.01815
- **Scope of capture: abstract page only; the paper body (PDF / HTML) was NOT captured.**

## Key claims
- "The game of chess is the most widely-studied domain in the history of artificial intelligence."
- The strongest chess programs combine "sophisticated search techniques, domain-specific adaptations, and handcrafted evaluation functions that have been refined by human experts over several decades."
- AlphaGo Zero "recently achieved superhuman performance in the game of Go, by tabula rasa reinforcement learning from games of self-play."
- The paper generalises this into "a single AlphaZero algorithm that can achieve, tabula rasa, superhuman performance in many challenging domains."
- "Starting from random play, and given no domain knowledge except the game rules, AlphaZero achieved within 24 hours a superhuman level of play in the games of chess and shogi (Japanese chess) as well as Go, and convincingly defeated a world-champion program in each case."

## Definitions and terminology
- **Tabula rasa** — learning with no domain knowledge except the game rules, starting from random play.
- **Self-play** — the agent learns by playing games against itself (relevant to the talk as the degenerate "multi-agent" case where the opponent is a copy of the same policy).

## Evidence and examples
- 24 hours of training to superhuman level in chess, shogi and Go (per the abstract).
- "convincingly defeated a world-champion program in each case" — the abstract does not name the opponent programs.

## Inconsistencies / open questions
- [verified] The capture holds only the abstract — checked `page.md` (8 KB, arXiv chrome + abstract); no figures, numbers of games, hardware, or opponent names. Specifics (e.g., which world-champion programs, match scores) need the paper.
- [open question] The opponent programs (commonly reported as Stockfish for chess, Elmo for shogi, AlphaGo Zero for Go) are not named in this capture; cite the paper body before using names.
- [open question] This arXiv preprint (2017) precedes the peer-reviewed *Science* version (2018); figures may differ between versions — not checked.

## Images / diagrams

### alphazero-silver-2017.web/images/arxiv-logo-primary-light.svg
- Provenance: `research/web/alphazero-silver-2017/assets/arxiv-logo-primary-light.svg` (alt "archive"). arXiv logo, site chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### alphazero-silver-2017.web/images/bibsonomy.png
- Provenance: `research/web/alphazero-silver-2017/assets/bibsonomy.png` (alt "BibSonomy"). Social bookmark icon, site chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### alphazero-silver-2017.web/images/reddit.png
- Provenance: `research/web/alphazero-silver-2017/assets/reddit.png` (alt "Reddit"). Social bookmark icon, site chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

## Raw / preserved excerpts

**Abstract** (verbatim, complete):

> The game of chess is the most widely-studied domain in the history of artificial intelligence. The strongest programs are based on a combination of sophisticated search techniques, domain-specific adaptations, and handcrafted evaluation functions that have been refined by human experts over several decades. In contrast, the AlphaGo Zero program recently achieved superhuman performance in the game of Go, by tabula rasa reinforcement learning from games of self-play. In this paper, we generalise this approach into a single AlphaZero algorithm that can achieve, tabula rasa, superhuman performance in many challenging domains. Starting from random play, and given no domain knowledge except the game rules, AlphaZero achieved within 24 hours a superhuman level of play in the games of chess and shogi (Japanese chess) as well as Go, and convincingly defeated a world-champion program in each case.

Cite as: arXiv:1712.01815 [cs.AI]; https://doi.org/10.48550/arXiv.1712.01815
