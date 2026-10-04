---
source_file: alphago-zero-deepmind/
source_type: web-capture
ingested_at: 2026-10-04
---

# AlphaGo Zero: Starting from scratch (Google DeepMind blog, 2017)

## Provenance
- Original location: research/web/alphago-zero-deepmind/ (text from `page.md`)
- Format: html (DeepMind blog post, web capture via talksmith:ingest)
- URL: https://deepmind.google/blog/alphago-zero-starting-from-scratch/
- Fetched: 2026-08-14T16:56:57Z (HTTP 200)
- Author / source (if known): David Silver, Demis Hassabis (byline). Work credited to David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur Guez, Thomas Hubert, Lucas Baker, Matthew Lai, Adrian Bolton, Yutian Chen, Timothy Lillicrap, Fan Hui, Laurent Sifre, George van den Driessche, Thore Graepel and Demis Hassabis.
- Date of original (if known): October 18, 2017. Companion paper in *Nature* (https://www.nature.com/articles/nature24270).

## Key claims
- AlphaGo Zero "is even more powerful and is arguably the strongest Go player in history."
- Previous AlphaGo versions "initially trained on thousands of human amateur and professional games"; AlphaGo Zero "skips this step and learns to play simply by playing games against itself, starting from completely random play."
- It "defeated the previously published champion-defeating version of AlphaGo by 100 games to 0."
- Mechanism: "AlphaGo Zero becomes its own teacher. The system starts off with a neural network that knows nothing about the game of Go. It then plays games against itself, by combining this neural network with a powerful search algorithm. As it plays, the neural network is tuned and updated to predict moves, as well as the eventual winner of the games." The updated network is recombined with search "to create a new, stronger version of AlphaGo Zero, and the process begins again."
- "no longer constrained by the limits of human knowledge. Instead, it is able to learn tabula rasa from the strongest player in the world: AlphaGo itself."
- Differences vs. earlier versions: only black/white stones as input (no hand-engineered features); one network instead of separate policy and value networks; no rollouts.
- "But it is the algorithmic change that makes the system much more powerful and efficient."
- Timeline: after 3 days of self-play, beat the published version (which beat Lee Sedol) 100–0; after 40 days, outperformed "Master" (which had beaten world number one Ke Jie).
- "Over the course of millions of AlphaGo vs AlphaGo games, the system progressively learned the game of Go from scratch, accumulating thousands of years of human knowledge during a period of just a few days."

## Definitions and terminology
- **Self-play** — the system plays against itself; the opponent is a copy of the same agent.
- **Tabula rasa** — learning from scratch with no human game data.
- **Policy network / value network** — earlier AlphaGo used one network to select moves and another to predict the winner; Zero merges them into one.
- **Rollouts** — "fast, random games used by other Go programs to predict which player will win from the current board position"; Zero does not use them.
- **Elo rating** — "a measure of the relative skill levels of players in competitive games such as Go".

## Evidence and examples
- 100–0 vs. AlphaGo Lee (published version) after 3 days.
- 40 days → surpasses AlphaGo Master.
- Hardware/power chart: AlphaGo Fan (176 GPUs), AlphaGo Lee (48 TPUs), AlphaGo Master (4 TPUs), AlphaGo Zero (4 TPUs) — per image alt text; caption: "AlphaGo has become progressively more efficient thanks to hardware gains and more recently algorithmic advances".
- Elo chart (per alt text): Crazy Stone ≈1900, AlphaGo Fan ≈3100, AlphaGo Lee ≈3700, AlphaGo Master ≈4800, AlphaGo Zero >5000.

## Inconsistencies / open questions
- [open question] The Elo values above come from the page's alt text and from reading bar heights, not from the paper. Phase 2 inspected both charts: they really do plot different reference values — the 40-day line chart draws AlphaGo Lee at ≈3500 and Master at ≈4750, while the bar chart draws Lee ≈3700 and Master ≈4850 (verified by viewing both images). Which one is right was not checked against the *Nature* paper; neither chart has numeric labels, so do not quote exact Elo figures from this page.
- [verified] The alt text of `62266eee4bfb80301e18f60b_Games.gif` ("A bar chart comparing the Elo ratings…") is wrong: it duplicates the Elo bar chart's alt. Phase 2 inspected sampled frames of the GIF: it shows three Go boards from self-play games at 3, 19 and 70 hours of training with text panels (beginner-like greedy capturing → fundamentals such as life-and-death, influence and territory → super-human disciplined play). Use the Phase-2 transcription, not the alt text.
- Relevance note: self-play is a single-agent learning a two-player game; for the talk it is the bridge between RL and multi-agent RL (AlphaStar league, OpenAI Five), not a MAS in itself.

## Images / diagrams

### alphago-zero-deepmind.web/images/go-stone-hero.jpg
- Provenance: `research/web/alphago-zero-deepmind/assets/szhZ2EwO…=w1440-h810-n-nu.bin` (JPEG 1440×810, renamed). Hero image. Alt: "A close-up of a glossy, translucent Go stone resting on a wooden board, reflecting a starry galaxy and a room interior."
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### alphago-zero-deepmind.web/images/62266dad5dd02443ba577b4e_unnamed.gif
- Provenance: `research/web/alphago-zero-deepmind/assets/62266dad5dd02443ba577b4e_unnamed.gif` (animated GIF). Placed after the "100 games to 0" paragraph. Alt: "A line graph showing the Elo rating comparison of AlphaGo versions over 40 days, with baseline dashed lines for AlphaGo Lee (at approximately 3500 Elo) and AlphaGo Master (at approximately 4750 Elo)."
- Depiction: Animated GIF (480 frames; last frame inspected). Line chart of Elo Rating (-2000 to 5000+) vs days 0-40: the 'AlphaGo Zero 40 blocks' curve starts near -2000, climbs steeply in the first ~3 days past the green dashed 'AlphaGo Lee' line (~3500), then slowly, crossing the blue dashed 'AlphaGo Master' line (~4750) late and ending ~5100 at day 40. Overlaid caption box '40 days'.
- Why it matters: Visual of learning from pure self-play: from random to superhuman in days, with no human data — the bridge from RL to multi-agent self-play (AlphaStar league, OpenAI Five).
- Transcribed text: Overlay: '40 days — AlphaGo Zero surpasses all other versions of AlphaGo and, arguably, becomes the best Go player in the world. It does this entirely from self-play, with no human intervention and using no historical data.' Axes: Elo Rating (-2000, -1000, 0, 1000, 2000, 3000, 4000, 5000); 0-40 (days). Legend: AlphaGo Zero 40 blocks; AlphaGo Lee; AlphaGo Master.

### alphago-zero-deepmind.web/images/power-consumption.jpg
- Provenance: `research/web/alphago-zero-deepmind/assets/QFTNOIvG…=w1440.bin` (JPEG 1440×732, renamed). Caption: "AlphaGo has become progressively more efficient thanks to hardware gains and more recently algorithmic advances". Alt: "A bar chart comparing power consumption (TDP) across AlphaGo versions, showing a dramatic decrease from AlphaGo Fan (176 GPUs, over 40,000 TDP) and AlphaGo Lee (48 TPUs, approx. 10,000 TDP) down to AlphaGo Master (4 TPUs) and AlphaGo Zero (4 TPUs), which both require minimal power."
- Depiction: Bar chart of Power Consumption (TDP), y 0-50000: AlphaGo Fan (176 GPUs) ~40,800; AlphaGo Lee (48 TPUs) ~10,200; AlphaGo Master (4TPUs) ~1,000; AlphaGo Zero (4 TPUs) ~1,000. Values read from bar heights (no numeric labels).
- Why it matters: Shows that algorithmic progress (self-play, single network) cut compute by more than an order of magnitude — supports cost/efficiency arguments.
- Transcribed text: Power Consumption (TDP) 0, 10000, 20000, 30000, 40000, 50000; AlphaGo Fan (176 GPUs); AlphaGo Lee (48 TPUs); AlphaGo Master (4TPUs); AlphaGo Zero (4 TPUs).

### alphago-zero-deepmind.web/images/elo-programs.jpg
- Provenance: `research/web/alphago-zero-deepmind/assets/yq94Hk34…=w1440.bin` (JPEG 1440×700, renamed). Caption: "Elo ratings - a measure of the relative skill levels of players in competitive games such as Go - show how AlphaGo has become progressively stronger during its development". Alt: "Bar chart comparing Elo ratings of different Go programs: Crazy Stone (approx. 1900), AlphaGo Fan (approx. 3100), AlphaGo Lee (approx. 3700), AlphaGo Master (approx. 4800), and AlphaGo Zero, which achieves the highest rating at over 5000."
- Depiction: Bar chart of Elo Rating (0-5000+): Crazy Stone ~1900 (grey), AlphaGo Fan ~3100, AlphaGo Lee ~3700, AlphaGo Master ~4850, AlphaGo Zero ~5150 (light blue, exceeds the top gridline). Values read from bar heights (no numeric labels).
- Why it matters: Summary of strength across program generations; AlphaGo Zero on top without human data.
- Transcribed text: Elo Rating 0, 1000, 2000, 3000, 4000, 5000; Crazy Stone; AlphaGo Fan; AlphaGo Lee; AlphaGo Master; AlphaGo Zero.

### alphago-zero-deepmind.web/images/62266eee4bfb80301e18f60b_Games.gif
- Provenance: `research/web/alphago-zero-deepmind/assets/62266eee4bfb80301e18f60b_Games.gif` (animated GIF, 2.2 MB). Placed after the "new knowledge… creative new moves" paragraph. Alt (possibly copy-pasted, see open questions): "A bar chart comparing the Elo ratings of different Go programs, showing AlphaGo Zero achieving the highest rating at over 5000."
- Depiction: Animated GIF (88 frames, inspected via 5 sampled frames). **Not a bar chart** (the alt text is wrong): it shows three Go board diagrams with numbered stones from self-play games at successive training times, each with a text panel; the panels fade in one after another, and two boards carry 'Captured Stones' notes.
- Why it matters: Qualitative view of self-play learning stages: greedy beginner -> fundamentals -> superhuman, disciplined play. Corrects the page's alt text.
- Transcribed text: '3 hours — AlphaGo Zero plays like a human beginner, forgoing long term strategy to focus on greedily capturing as many stones as possible.' '19 hours — AlphaGo Zero has learnt the fundamentals of more advanced Go strategies such as life-and-death, influence and territory.' '70 hours — AlphaGo Zero plays at super-human level. The game is disciplined and involves multiple challenges across the board.' 'Captured Stones' (lists of the form 'N at M', e.g. '68 at 61').

### alphago-zero-deepmind.web/images/untitled-1920x1080.jpg
- Provenance: `research/web/alphago-zero-deepmind/assets/st59vnlF…=w2464-h2464-n-nu.bin` (JPEG 1920×1080, renamed). Thumbnail of the "Related posts → AlphaGo" card; no alt.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### alphago-zero-deepmind.web/images/untitled-704x704.jpg
- Provenance: `research/web/alphago-zero-deepmind/assets/HUUyrBSv…=w704-h704-n-nu.bin` (JPEG 704×704, renamed). Thumbnail of the "Related posts → AlphaGo's next move" card; no alt.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### alphago-zero-deepmind.web/images/nav__gdm-lockup__light.height-25.svg
- Provenance: `research/web/alphago-zero-deepmind/assets/nav__gdm-lockup__light.height-25.svg`. Google DeepMind logo (light), navigation chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### alphago-zero-deepmind.web/images/nav__gdm-lockup__dark.height-25.svg
- Provenance: `research/web/alphago-zero-deepmind/assets/nav__gdm-lockup__dark.height-25.svg`. Google DeepMind logo (dark), navigation chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

## Raw / preserved excerpts

> Artificial intelligence research has made rapid progress in a wide variety of domains from speech recognition and image classification to genomics and drug discovery. In many cases, these are specialist systems that leverage enormous amounts of human expertise and data.
>
> However, for some problems this human knowledge may be too expensive, too unreliable or simply unavailable. As a result, a long-standing ambition of AI research is to bypass this step, creating algorithms that achieve superhuman performance in the most challenging domains with no human input. In our most recent paper, published in the journal Nature, we demonstrate a significant step towards this goal.
>
> The paper introduces AlphaGo Zero, the latest evolution of AlphaGo, the first computer program to defeat a world champion at the ancient Chinese game of Go. Zero is even more powerful and is arguably the strongest Go player in history.
>
> Previous versions of AlphaGo initially trained on thousands of human amateur and professional games to learn how to play Go. AlphaGo Zero skips this step and learns to play simply by playing games against itself, starting from completely random play. In doing so, it quickly surpassed human level of play and defeated the previously published champion-defeating version of AlphaGo by 100 games to 0.

> It is able to do this by using a novel form of reinforcement learning, in which AlphaGo Zero becomes its own teacher. The system starts off with a neural network that knows nothing about the game of Go. It then plays games against itself, by combining this neural network with a powerful search algorithm. As it plays, the neural network is tuned and updated to predict moves, as well as the eventual winner of the games.
> This updated neural network is then recombined with the search algorithm to create a new, stronger version of AlphaGo Zero, and the process begins again. In each iteration, the performance of the system improves by a small amount, and the quality of the self-play games increases, leading to more and more accurate neural networks and ever stronger versions of AlphaGo Zero.
>
> This technique is more powerful than previous versions of AlphaGo because it is no longer constrained by the limits of human knowledge. Instead, it is able to learn tabula rasa from the strongest player in the world: AlphaGo itself.
> It also differs from previous versions in other notable ways.
>
> - AlphaGo Zero only uses the black and white stones from the Go board as its input, whereas previous versions of AlphaGo included a small number of hand-engineered features.
> - It uses one neural network rather than two. Earlier versions of AlphaGo used a "policy network" to select the next move to play and a "value network" to predict the winner of the game from each position. These are combined in AlphaGo Zero, allowing it to be trained and evaluated more efficiently.
> - AlphaGo Zero does not use "rollouts" - fast, random games used by other Go programs to predict which player will win from the current board position. Instead, it relies on its high quality neural networks to evaluate positions.
>
> All of these differences help improve the performance of the system and make it more general. But it is the algorithmic change that makes the system much more powerful and efficient.

> After just three days of self-play training, AlphaGo Zero emphatically defeated the previously published version of AlphaGo - which had itself defeated 18-time world champion Lee Sedol - by 100 games to 0. After 40 days of self training, AlphaGo Zero became even stronger, outperforming the version of AlphaGo known as "Master", which has defeated the world's best players and world number one Ke Jie.

> Over the course of millions of AlphaGo vs AlphaGo games, the system progressively learned the game of Go from scratch, accumulating thousands of years of human knowledge during a period of just a few days. AlphaGo Zero also discovered new knowledge, developing unconventional strategies and creative new moves that echoed and surpassed the novel techniques it played in the games against Lee Sedol and Ke Jie.
>
> These moments of creativity give us confidence that AI will be a multiplier for human ingenuity, helping us with our mission to solve some of the most important challenges humanity is facing.
>
> While it is still early days, AlphaGo Zero constitutes a critical step towards this goal. If similar techniques can be applied to other structured problems, such as protein folding, reducing energy consumption or searching for revolutionary new materials, the resulting breakthroughs have the potential to positively impact society.
