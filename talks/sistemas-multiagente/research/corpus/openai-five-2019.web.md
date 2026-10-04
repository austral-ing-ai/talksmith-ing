---
source_file: openai-five-2019/
source_type: web-capture
ingested_at: 2026-10-04
---

# Dota 2 with Large Scale Deep Reinforcement Learning (OpenAI et al., arXiv:1912.06680) — "OpenAI Five" paper

## Provenance
- Original location: research/web/openai-five-2019/ (text from `page.md`, 166 KB — full paper incl. appendices A–Q, rendered by ar5iv)
- Format: html (ar5iv rendering of the arXiv paper, web capture via talksmith:ingest)
- URL: https://ar5iv.labs.arxiv.org/html/1912.06680 (arXiv abs: https://arxiv.org/abs/1912.06680)
- Fetched: 2026-10-04T19:22:39Z (HTTP 200)
- Author / source (if known): OpenAI; Christopher Berner, Greg Brockman, Brooke Chan, Vicki Cheung, Przemysław "Psyho" Dębiak, Christy Dennison, David Farhi, Quirin Fischer, Shariq Hashme, Chris Hesse, Rafal Józefowicz, Scott Gray, Catherine Olsson, Jakub Pachocki, Michael Petrov, Henrique Pondé de Oliveira Pinto, Jonathan Raiman, Tim Salimans, Jeremy Schlatter, Jonas Schneider, Szymon Sidor, Ilya Sutskever, Jie Tang, Filip Wolski, Susan Zhang ("Authors listed alphabetically. Please cite as OpenAI et al.")
- Date of original (if known): arXiv 1912.06680 (December 2019). Training run June 30, 2018 – April 22, 2019; match vs OG April 13, 2019.
- Extraction note: ar5iv renders math twice (Unicode + LaTeX source, e.g. "∼16,000\sim 16,000"); in excerpts below the LaTeX duplicate was dropped and footnote markers glued to words (e.g. "OG11 1") were removed. Wording is otherwise verbatim.

## Key claims
- "On April 13th, 2019, OpenAI Five became the first AI system to defeat the world champions at an esports game." Beat Team OG best-of-three, 2-0.
- "OpenAI Five leveraged existing reinforcement learning techniques, scaled to learn from batches of approximately 2 million frames every 2 seconds." Trained for 10 months with a distributed system and "surgery" tools.
- "self-play reinforcement learning can achieve superhuman performance on a difficult task."
- Public "OpenAI Five Arena" (April 18–21, 2019): played 3,193 teams in 7,257 games, winning 99.4% (abandoned games counted as wins: 3,140 of the 7,215 wins).
- **Five agents = five replicas of one policy.** "Separate replicas of the same policy function (with identical parameters θ) are used to control each of the five heroes on the team." Observations are nearly identical because visibility/fog of war is shared across the team; the LSTM receives an extra input indicating which hero is controlled. A "cross-hero pool" (max-pool of the first 25% of the vector across the five replicas) lets replicas use each other's non-identical inputs.
- Policy: recurrent network ≈159 million parameters (158,502,815 in the final version), mainly a single-layer 4096-unit LSTM (84% of parameters). Trained with PPO + GAE; Adam; truncated BPTT over 16 timesteps.
- Training system: Rollout CPUs run games; Forward Pass GPUs sample actions; Optimizer GPUs compute gradients (NCCL2 allreduce); Controller (Redis) stores parameter versions. Peak 1536 optimizer GPUs; batch up to 2,949,120 timesteps.
- **Self-play**: "play the latest policy against itself for 80% of games, and play against older policies for 20% of games" — to "avoid strategy collapse".
- **Team spirit τ**: reward interpolates between each hero's own reward and the team mean, rᵢ = (1−τ)ρᵢ + τ·ρ̄. "If team spirit is 0, then it's every hero for themselves… If team spirit is 1, then every reward is split equally among all five heroes." Lower team spirit helps early training (lower gradient variance); the target is τ = 1.
- Rewards made zero-sum by subtracting the average of the enemies' rewards; game-time weighting ρᵢ × 0.6^(T/10 min).
- Some mechanics were **hand-scripted**, not learned: ability builds, item purchasing, item swap, courier control. Hero drafting done with a minimax over precomputed win-probabilities, not a separate drafting agent.
- Limitations vs. normal game: 17 of 117 heroes; no items that let a player control multiple units (Illusion Rune, Helm of the Dominator, Manta Style, Necronomicon).
- Compute: 770±50 PFlops/s·days to the OG match (820±50 at shutdown); "Rerun" from scratch with the final setup: 150±5 PFlops/s·days, ≈20% of OpenAI Five's resources, reached >98% winrate against the final OpenAI Five.
- **Surgery**: ~20 major surgeries (≈ one per two weeks) to continue training across code/environment/game-version changes; naive estimate: 40 months instead of 10 if restarted each time. But "the model ultimately plateaued at a weaker skill level than the from-scratch model was able to achieve."
- Data quality > compute: staleness of ~8 versions causes significant slowdowns; reusing samples 2–3× can halve speed, 8× may prevent learning.
- Long-term credit assignment: horizons up to 6–12 minutes of game time improve the trained agent.
- Reaction time: 217 ms average (range 167–267 ms by design of frameskip + action offset); human visual reaction ≈250 ms.
- Conclusion: methods "can solve any zero-sum two-team continuous environment which can be simulated in parallel across hundreds of thousands of instances."

## Definitions and terminology
- **Policy (π)** — "a function from the history of observations to a probability distribution over actions".
- **Timestep / frameskip** — the agent acts every 4th frame (7.5 actions/s); ≈20,000 steps per ≈45-min game.
- **Team spirit (τ)** — hyperparameter that "measures how much agents on the team share in the spoils of their teammates" (Appendix G).
- **Solo vs Team rewards** — some rewards go only to the acting hero, others to every hero on the team.
- **Self-play / opponent manager** — current agent plays itself or past versions sampled by a softmax over quality scores qᵢ (Appendix N).
- **Strategy collapse** — agent "forgets how to play against a wide variety of opponents because it only requires a narrow set of strategies to defeat its immediate past version."
- **Surgery** — "a collection of tools to perform offline operations to the old model πθ to obtain a new model π̂θ̂ compatible with the new environment, which performs at the same level of skill"; generalizes Net2Net function-preserving transformations.
- **Staleness** — M−N, where N is the parameter version that generated a sample and M the version being optimized.
- **Sample reuse** — ratio of optimizer consumption rate to rollout production rate.
- **TrueSkill** — automated rating vs. fixed reference agents; 0 = random agent; ≈8.3 difference ≈ 80% winrate.
- **Horizon H = T/(1−γ)** — game time over which rewards are integrated (T = 0.133 s per step).
- **Scripted actions** — "a rudimentary rules-based system to handle these decisions."
- **Lane assignments** — environment randomization assigning heroes to lanes with a penalty for leaving.

## Evidence and examples
- **Dota 2 challenges**: long horizons (≈20,000 steps vs chess ≈80 moves, Go ≈150); partial observability; ≈16,000 observed values per timestep (1,200 categorical + 14,534 continuous/boolean per hero); 8,000–80,000 available actions per step depending on hero; factorized action space up to 30×4×189×81 = 1,837,080.
- **Match history (Appendix I, Table 6)**: June 6, 2018 internal event (4 wins, restricted mirror matches); Aug 5, 2018 casters (2 wins, 1 loss); Aug 9, 2018 Team Secret (1 win, 2 losses); Aug 22–23, 2018 The International: lost to Pain Gaming (52:29) and Chinese Legends (45:44); Oct 5, 2018 Team Lithium 3 wins; Jan 16, 2019 SG Esports 4 wins; Feb 1, 2019 Alliance 3 wins; April 13, 2019 OG 2 wins (38:18, 20:51) on 7.21d.
- **Emergent team playstyle** (Section 4.1): early — large group fights, no comeback when behind; later — concentrate resources on strongest heroes (as humans do); moved heroes across the map more often than humans; consumed resources and long-cooldown abilities more readily.
- **Agent coordination evidence (Appendix D)**: per-hero predictions of participation in destroying enemy buildings; "In several cases all heroes predict they will participate in the attack (and they do). In few cases one or two heroes are left out, and indeed by watching the game replay we see that those heroes are busy in the different part of the map during that time."
- **Local minimum from multi-agent behavior** (Appendix O.2): "our agents developed a preference to stick together as a group of 5 on a single lane, and fighting any opponent coming their way. This represents a large local minimum" — led to lane-assignment randomization (later found probably unnecessary by ablation).
- **Sparse-reward ablation** (Appendix G): with only win/loss reward the model still beat a hand-coded scripted agent (TrueSkill 155 vs 100), "with a large penalty to sample efficiency".
- **Bloopers (Appendix Q)**: humans hand-tuning learning rate before The International 2018 ("designing skyscrapers"); zeroing a vestigial 128-dim team-spirit embedding raised winrate ≈55%; Divine Rapier item created a negative feedback loop in Rerun (hypothesized variance from transferable high-value item).
- **Compute cost split** (Appendix A): optimizer GPUs ≈30% of dollar cost, forward-pass GPUs ≈30%, rollout CPUs ≈30%, overhead ≈10%.
- **Comparison with AlphaStar** (Section 5): both LSTM core + actor-critic; OpenAI Five hard-codes some subsystems (item buying) while AlphaStar conditioned on human-replay statistics; "OpenAI Five trained using self play, while AlphaStar used a league consisting of multiple agents"; AlphaStar's value network saw full game state.

## Inconsistencies / open questions
- [verified] Rerun's dates conflict within the paper: Section 4.2 says "between May 18, 2019 and June 12, 2019", Appendix A says "between May 18th and July 12th, 2019"; Section 4.2 also says "Rerun took 2 months", which matches July 12, not June 12 — checked both passages in page.md. Prefer "~2 months (May–July 2019)" or flag.
- [verified] "Twenty-nine teams managed to defeat OpenAI Five for a total of 4242 games lost" is an extraction artifact (footnote marker glued to the number): 7,257 games − 7,215 wins = **42** losses — checked by arithmetic against the same paragraph and footnote ("3140 of the 7215 wins").
- [verified] The 99.4% Arena winrate counts abandoned games as wins (3,140 of 7,215 wins were abandonments, ≈43%) — stated in the paper's own footnote; any slide quoting 99.4% should carry that caveat.
- [verified] The "five agents" are not independently trained agents: they are five replicas of one network with shared parameters and nearly identical observations, plus a cross-hero pool — checked in Section 3.1 and Appendix H. For the talk's taxonomy this is cooperative MARL with parameter sharing (centralized learning, per-hero execution), not five distinct specialists.
- [verified] OpenAI Five was not fully learned end-to-end: item purchasing, ability builds, item swap, courier and drafting were scripted/heuristic, and 17 of 117 heroes were supported — checked in Sections 2, 3.1 and Appendix F.1 / D.2.
- [verified] The match record is not uniformly winning: two losses at The International 2018 (Pain Gaming, Chinese Legends) and losses to Team Secret and casters in Aug 2018 — checked in Appendix I Table 6 and Appendix Q.1 ("we lost both games at that event").
- [verified] The capture is missing 37 figures: ar5iv embeds most figures as `<object type="image/svg+xml">`, which talksmith:ingest did not download — checked by listing `<object data=…svg>` in `original.html`. Missing include Figure 1 (`smallarchdiagram.svg`, model architecture with 5 replicas), Figure 2 (`Training-Architecture.svg`, system overview), Figure 3 (`og_trueskill_human.svg`), Figure 4 (`rerun-vs-five-trueskill.svg`), Figure 5 (6 SVGs), Figure 6 (`horizon_resume.svg`), Figure 9 (`winrates-OG-game-1.svg`), Figure 18 (`action_space_diagram.svg`), Figure 27 (`opponent_relative_distribution_contour.svg`), Figure 29 (team spirit sweep, 2 SVGs) and others in Appendices A13–A16. Captions are preserved in text; the images are not in the companion folder. Re-ingest or fetch from `https://ar5iv.labs.arxiv.org/html/1912.06680/assets/<name>.svg` if the deck needs them.
- [open question] "first AI system to defeat the world champions at an esports game" is OpenAI's own claim — not independently checked.
- [verified] Team spirit schedule: OpenAI Five went 0.3 → 1.0 over training; Rerun 0.3 → 0.8 (planned to reach 1.0 but matched OpenAI Five before getting there) — checked in Appendix C, Table 2 and Figure 7 caption (preserved below).
- [open question] Figure 12 caption cites a win-probability update "from 52.8% to 65.1%"; the captured `hero-selection.png` (Phase 2, viewed) shows 65.1% on the first pick but no 52.8% anywhere — the pre-draft value may simply not be displayed in that screenshot. Not checked against other frames or the paper PDF.

## Images / diagrams

### openai-five-2019.web/images/timescales.png
- Provenance: `research/web/openai-five-2019/assets/timescales.png` (from ar5iv `/html/1912.06680/assets/figures/timescales.png`, alt "Refer to caption"). Appendix C, Figure 8: "Timescales and Staleness: The breakdown of a rollout game."
- Depiction: Four stacked horizontal timelines linked by dotted funnels, each zooming out one level: game-engine frames (black ticks) -> policy time steps (blue) -> samples (red) -> segments (green) -> whole episode.
- Why it matters: Shows the nested timescales of training: a decision every 4 frames, LSTM unrolled 16 steps, 16 samples per optimizer segment, episodes of 30+ minutes. Useful to explain long-horizon credit assignment in a multi-agent game.
- Transcribed text: Dota game engine: 30 frames per second | 4 game engine frames (0.133 seconds) per policy time step | 16 time steps (2.1 seconds) per sample (LSTM unroll length) | 16 samples (34 seconds) per segment labelled together (GAE) and sent to optimizer | One episode (30+ minutes) broken down into many segments.

### openai-five-2019.web/images/objectives-OG-game-1.png
- Provenance: `research/web/openai-five-2019/assets/objectives-OG-game-1.png` (alt "Refer to caption"). Appendix D.1, Figure 10: "Continuous prediction of destroying enemy buildings by OpenAI Five in Finals game 1. Predictions by different heroes differ as they specifically predict whether they will participate in bringing given building down. Predictions should not be read as calibrated probabilities, because they are trained with a discount factor."
- Depiction: 3x3 grid of line plots (rows: tower 1/2/3; columns: bottom/mid/top lane). Each plot shows five coloured curves (one per OpenAI Five hero) of the predicted probability (0-1) that this hero will take part in destroying that building, over game minutes; a dashed vertical line marks when the tower fell. Two inset screenshots point to Fig 11a (bottom tower 1) and Fig 11b (mid tower 2).
- Why it matters: Evidence that each of the five replica agents carries its own, individual 'plan' signal: curves diverge by hero and rise/fall as heroes commit to or abandon an objective — visible per-agent intention inside a cooperative team.
- Transcribed text: Panel titles: bottom tower 1, mid tower 1, top tower 1, bottom tower 2, mid tower 2, top tower 2, bottom tower 3, mid tower 3, top tower 3. Legend: sven, gyrocopter, crystal maiden, death prophet, sniper. Insets: 'See Fig 11a', 'See Fig 11b'. X-axis ticks (minutes): bottom tower 1 10-12; mid tower 1 11-13; top tower 1 10-12; bottom tower 2 29-31; mid tower 2 18-20; top tower 2 24-26; bottom tower 3 30-32; mid tower 3 18-20; top tower 3 30-32. Y-axis 0.0-1.0.

### openai-five-2019.web/images/OG-game-1-tower-1-bot-small.png
- Provenance: `research/web/openai-five-2019/assets/OG-game-1-tower-1-bot-small.png` (alt "Refer to caption"). Appendix D.1, Figure 11(a): "Gyrocopter and Crystal Maiden attack the bottom tower 1 … and plan perhaps to kill it (their predictions go up). But they are chased away by the incoming dire (human) heroes, and their plan changes … Radiant creeps kill the tower half a minute later."
- Depiction: Dota 2 replay screenshot (game time 11:28, replay 0:11:28 / 1:44:40): Gyrocopter labelled 'OpenAI 2 (Bot)' and Crystal Maiden 'OpenAI 3 (Bot)' near the bottom tower, with a human enemy hero ('major first timer') arriving from the top; Drow Ranger HUD at the bottom.
- Why it matters: Concrete moment behind the bottom-tower-1 curve: two agents commit to an objective and then abandon it when human enemies arrive — illustrates a plan change in reaction to other agents.
- Transcribed text: Scoreboard 9 - 9, clock 11:28; labels 'OpenAI 3 (Bot)', 'OpenAI 2 (Bot)', 'major first timer'; HUD 'DROW RANGER', 629 / 940, 443 / 495; replay controls 'Free Camera', 'No Broadcaster', 'Fog: Both Teams', 'COPY TO CLIPBOARD', 'JUMP AHEAD'; K/D/A 2/3/2, LH/DN 26/7; gold 553; 2:32.

### openai-five-2019.web/images/OG-game-1-tower-2-mid-small.png
- Provenance: `research/web/openai-five-2019/assets/OG-game-1-tower-2-mid-small.png` (alt "Refer to caption"). Appendix D.1, Figure 11(b): "all radiant heroes attack mid tower 2 … However just before it falls, few dire heroes show up trying to save it, and most radiant heroes end up chasing them a fair distance away from the building. The prediction for those heroes to participate in the tower kill drops accordingly."
- Depiction: Dota 2 replay screenshot (game time 18:59, replay 0:18:59 / 1:44:40): three OpenAI bots ('OpenAI 4', 'OpenAI 1', 'OpenAI 5') near the mid lane, a projectile heading toward the enemy tower area; chat line '[Allies] major first timer: Affirmative'.
- Why it matters: Moment behind the mid-tower-2 curve: radiant heroes leave the tower to chase defenders, so their participation predictions drop — coordination visibly reacting to opponents.
- Transcribed text: Scoreboard 19 - 20, clock 18:59; labels 'OpenAI 4 (Bot)', 'OpenAI 1 (Bot)', 'OpenAI 5 (Bot)'; 'Show Fight Recap'; chat '[Allies] major first timer: > Affirmative'; K/D/A 0/1/1, LH/DN 12/1; gold 247; 'Drag items to add to quick buy'.

### openai-five-2019.web/images/hero-selection.png
- Provenance: `research/web/openai-five-2019/assets/hero-selection.png` (alt "Refer to caption"). Appendix D.2, Figure 12: drafting program picks "the one that maximizes worst-case scenario of opponent hero selection (minimax algorithm)"; example from Finals game 1 where win probability updates from 52.8% to 65.1% after the humans' first pick.
- Depiction: Screenshot of the drafting tool UI. Top band 'OpenAI Five / Radiant' and 'Human / Dire' with alternating hero portraits along a pick timeline, each labelled with OpenAI Five's win-probability estimate after that pick (65.1%, 65.1%, 65.1%, 66.9%, 66.9%, 67.6%, 67.6%, 67.6%, 67.6%) and an empty highlighted slot for the next pick; big '67.6% OpenAI Five Win Probability Estimate' at top right. Below, a row of 9 candidate heroes with the resulting estimate for each (67.6% ... 59.3%, and -100.0% for an unavailable one) and a greyed-out row of already-picked heroes. Bottom buttons.
- Why it matters: Shows that hero selection is solved by a separate minimax search over a learned win-probability estimate — the 'team composition' decision sits outside the five playing agents.
- Transcribed text: OpenAI Five / Radiant; Human / Dire; per-pick estimates: 65.1%, 65.1%, 65.1%, 66.9%, 66.9%, 67.6%, 67.6%, 67.6%, 67.6%; '67.6% OpenAI Five Win Probability Estimate'; candidate estimates: 67.6%, 66.5%, 66.4%, 62.9%, 62.2%, 61.1%, 60.9%, 59.3%, -100.0%; buttons: Radiant Pick | Dire Pick | DRRDRDRDDR | Dire Humans | Radiant Humans | Reset | Probabilities | Undo.

### openai-five-2019.web/images/unit-observations.png
- Provenance: `research/web/openai-five-2019/assets/unit-observations.png` (alt "Refer to caption"). Appendix E, Figure 14: "Observation Space Overview: The arrays that OpenAI Five observes at each timestep." 189 units; per hero 1,200 categorical + 14,534 continuous/boolean values.
- Depiction: Block diagram of the observation arrays. Columns: Heroes (Allied 5, Enemy 5) and Non-Heroes (Allied 82, Enemy 82, Neutral 15). Rows give per-unit observation blocks with categorical (cat) and continuous (cont) counts; stacked cards indicate modifiers, abilities and items per hero. Side boxes: 'Non-Unit Observations' and 'Individual Observations'.
- Why it matters: Quantifies what each agent perceives: a large, mostly shared, structured state (189 units) plus a small per-hero individual part — useful to discuss full vs. partial observability in a team of agents.
- Transcribed text: Title: Unit Observations. Per-unit obs (2 categorical + 43 continuous): Allied heroes 10 cat / 215 cont; Enemy heroes 10 cat / 215 cont; Allied non-heroes 164 cat / 3,526 cont; Enemy non-heroes 164 cat / 3,526 cont; Neutral 30 cat / 645 cont. Modifiers (1 categorical + 2 continuous): 50 cat/100 cont; 50 cat/100 cont; 164 cat/328 cont; 164 cat/328 cont; 30 cat/60 cont — '10 mods per hero, 2 per non-hero'. Per-hero extra obs (25 continuous): 125 cont; 125 cont. Abilities (1 categorical + 7 continuous): 30 cat/210 cont; 30 cat/210 cont — '6 abilities per hero'. Items (1 categorical + 13 continuous): 80 cat/1,040 cont; 80 cat/1,040 cont — '16 items per hero'. Per-allied-hero extra obs (2 categorical + 211 continuous): 10 cat/1,055 cont. Non-Unit Observations: Global 22 cont; Pickups (6) (1 cat, 15 cont each) 6 cat/90 cont; Minimap (10x10) 9 channels 900 cont. Individual Observations: Previous Action 310 cont; Nearby map (8x8 map) (2 cat, 6 cont channels) 128 cat/384 cont.

### openai-five-2019.web/images/delay_head.png
- Provenance: `research/web/openai-five-2019/assets/delay_head.png` (alt "Refer to caption"). Appendix F, Figure 15(a): "Delay: An integer from 0 to 3 indicating which frame during the next frameskip to take the action on."
- Depiction: Small thumbnail: four frames of a spell animation (top row) above four squares, the fourth shaded blue — choosing which of the 4 frames in the next frameskip the action is executed on.
- Why it matters: Shows the action 'delay' parameter (0-3); minor technical detail of the action space.
- Transcribed text: No text in image.

### openai-five-2019.web/images/unit_head.png
- Provenance: `research/web/openai-five-2019/assets/unit_head.png` (alt "Refer to caption"). Appendix F, Figure 15(b): "Unit Selection: One of the 189 visible units in the observation."
- Depiction: Small in-game thumbnail: one hero with lines drawn to circled candidate units around it — the unit-selection target among visible units.
- Why it matters: Illustrates the 'unit selection' action parameter (choose one of 189 visible units); minor detail of the action space.
- Transcribed text: No text in image.

### openai-five-2019.web/images/offset_head.png
- Provenance: `research/web/openai-five-2019/assets/offset_head.png` (alt "Refer to caption"). Appendix F, Figure 15(c): "Offset: A 2D (X,Y) coordinate indicating a spatial offset … a grid of 81 possible coordinate pairs."
- Depiction: Small in-game thumbnail: a 9x9 white grid overlaid on the ground around a hero, one cell highlighted — spatial offset target.
- Why it matters: Illustrates the 'offset' action parameter (81 possible coordinate pairs); minor detail of the action space.
- Transcribed text: No text in image.

### openai-five-2019.web/images/unit_observations_tree.png
- Provenance: `research/web/openai-five-2019/assets/unit_observations_tree.png` (alt "Refer to caption"). Appendix H, Figure 17(a): "Flattening the observation space: First we process the complicated observation space into a single vector. The observation space has a tree structure…"
- Depiction: Tree diagram: root 'Game State' branches into Global Obs, Minimap (10x10), Nearby Map (8x8), 6 Pickups, 5 Enemy Heroes, 5 Allied Heroes, 82 Allied Nonheroes, 82 Enemy Nonheroes, 15 Neutral Nonheroes; dotted lines link unit groups to 'Unit Embeddings'. Leaves are small coloured squares by data type; Allied Heroes expand into 10 Modifiers, 6 Abilities, 16 Items. Legend box and a zoomed 'Process Set' box (NxK -> 2x FC -> NxS -> max-pool).
- Why it matters: Explains how a heterogeneous, set-structured world is flattened into one vector, and the 'Process Set' (FC + max-pool) trick — the same pooling idea reused for cross-hero pooling.
- Transcribed text: Game State; Unit Embeddings; Global Obs; Minimap (10x10); Nearby Map (8x8); 6 Pickups; 5 Enemy Heroes; 5 Allied Heroes; 82 Allied Nonheroes; 82 Enemy Nonheroes; 15 Neutral Nonheroes; 10 Modifiers; 6 Abilities; 16 Items. Legend 'Data type dictates processing:' Continuous Data: normalization only; no learned processing | Categorical Data: Embed | Spatial Data: 2 layer conv net | Unordered Set: "Process Set". Box 'Process Set — Summarizes an unordered set of N elements into a vector of size S': NxK -> 2x FC -> NxS -> max-pool; "Embedding output" output of shape N x S gives embedding of each element.; Primary output of shape S describes the whole set.

### openai-five-2019.web/images/prelstm.png
- Provenance: `research/web/openai-five-2019/assets/prelstm.png` (alt "Refer to caption"). Appendix H, Figure 17(b): "Preparing for LSTM: In order to tell each LSTM which of the team's heroes it controls, we append the controlled hero's Unit Embedding … we add a 'cross-hero pool' operation, in which we maxpool the first 25% of the vector across the five replica networks." **Most relevant captured image for the talk (how 5 replicas share information).**
- Depiction: Simple left-to-right block diagram: 'Game State' and 'My Hero Unit Embedding' (grey box, joined from below) feed into 'FC', whose output goes into 'Cross-Hero Pool', with an arrow continuing right (to the LSTM).
- Why it matters: The key multi-agent mechanism of OpenAI Five: five replica networks share the same state; each is told which hero it controls via its own unit embedding, and a cross-hero max-pool over part of the vector lets the replicas exchange information without explicit messages. Core figure for explaining implicit coordination.
- Transcribed text: Game State | My Hero Unit Embedding | FC | Cross-Hero Pool

### openai-five-2019.web/images/ti-lr.png
- Provenance: `research/web/openai-five-2019/assets/ti-lr.png` (alt "Refer to caption"). Appendix Q.1, Figure 32: "Learning Rate during The International: This is what happens when humans under time pressure choose hyperparameters. … our team began to internally refer to the act of frantically searching over hyperparameters as 'designing skyscrapers.'"
- Depiction: Step-like line chart of the learning rate (y from 0 to 1.5e-5) versus wall-clock time from about 11 AM 20 Aug 2018 to after 12 AM 23 Aug 2018. The value jumps repeatedly: ~1e-6, then 1e-5 for many hours, drops to 0, 5e-6, a spike to 1.5e-5, then decreasing steps (5e-6, 3e-6, 2e-6, 1.5e-6, 1e-6, 5e-7), with two later bumps to 3e-6 and a final drop to 0 and back to 1e-6.
- Why it matters: Anecdotal evidence of manual, ad-hoc hyperparameter tuning under deadline ('designing skyscrapers') during The International — a counterpoint to the polished narrative of large-scale RL.
- Transcribed text: Y-axis: 0, 2e-6, 4e-6, 6e-6, 8e-6, 1e-5, 1.2e-5, 1.4e-5. X-axis: 11 AM / 06 PM August 20, 2018; 12 AM / 06 AM / 12 PM / 06 PM August 21, 2018; 12 AM / 06 AM / 12 PM / 06 PM August 22, 2018; 12 AM.

### openai-five-2019.web/images/ar5iv.png
- Provenance: `research/web/openai-five-2019/assets/ar5iv.png` (alt "ar5iv homepage"). ar5iv site logo, page chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

## Raw / preserved excerpts

**Abstract**

> On April 13th, 2019, OpenAI Five became the first AI system to defeat the world champions at an esports game. The game of Dota 2 presents novel challenges for AI systems such as long time horizons, imperfect information, and complex, continuous state-action spaces, all challenges which will become increasingly central to more capable AI systems. OpenAI Five leveraged existing reinforcement learning techniques, scaled to learn from batches of approximately 2 million frames every 2 seconds. We developed a distributed training system and tools for continual training which allowed us to train OpenAI Five for 10 months. By defeating the Dota 2 world champion (Team OG), OpenAI Five demonstrates that self-play reinforcement learning can achieve superhuman performance on a difficult task.

**1 Introduction** (excerpt)

> Relative to previous AI milestones like Chess or Go, complex video games start to capture the complexity and continuous nature of the real world. Dota 2 is a multiplayer real-time strategy game produced by Valve Corporation in 2013, which averaged between 500,000 and 1,000,000 concurrent players between 2013 and 2019. The game is actively played by full time professionals; the prize pool for the 2019 international championship exceeded $35 million (the largest of any esports game in the world). The game presents challenges for reinforcement learning due to long time horizons, partial observability, and high dimensionality of observation and action spaces. Dota 2's rules are also complex — the game has been actively developed for over a decade, with game logic implemented in hundreds of thousands of lines of code.
>
> The key ingredient in solving this complex environment was to scale existing reinforcement learning systems to unprecedented levels, utilizing thousands of GPUs over multiple months. We built a distributed training system to do this which we used to train a Dota 2-playing agent called OpenAI Five. In April 2019, OpenAI Five defeated the Dota 2 world champions (Team OG), the first time an AI system has beaten an esport world champion. We also opened OpenAI Five to the Dota 2 community for competitive play; OpenAI Five won 99.4% of over 7000 games.
>
> One challenge we faced in training was that the environment and code continually changed as our project progressed. In order to train without restarting from the beginning after each change, we developed a collection of tools to resume training with minimal loss in performance which we call surgery. Over the 10-month training process, we performed approximately one surgery per two weeks. These tools allowed us to make frequent improvements to our strongest agent within a shorter time than the typical practice of training from scratch would allow. As AI systems tackle larger and harder problems, further investigation of settings with ever-changing environments and iterative development will be critical.

**2 Dota 2**

> Dota 2 is played on a square map with two teams defending bases in opposite corners. Each team's base contains a structure called an ancient; the game ends when one of these ancients is destroyed by the opposing team. Teams have five players, each controlling a hero unit with unique abilities. During the game, both teams have a constant stream of small "creep" units, uncontrolled by the players, which walk towards the enemy base attacking any opponent units or buildings. Players gather resources such as gold from creeps, which they use to increase their hero's power by purchasing items and improving abilities.
>
> To play Dota 2, an AI system must address various challenges:
>
> - Long time horizons. Dota 2 games run at 30 frames per second for approximately 45 minutes. OpenAI Five selects an action every fourth frame, yielding approximately 20,000 steps per episode. By comparison, chess usually lasts 80 moves, Go 150 moves.
> - Partially-observed state. Each team in the game can only see the portion of the game state near their units and buildings; the rest of the map is hidden. Strong play requires making inferences based on incomplete data, and modeling the opponent's behavior.
> - High-dimensional action and observation spaces. Dota 2 is played on a large map containing ten heroes, dozens of buildings, dozens of non-player units, and a long tail of game features such as runes, trees, and wards. OpenAI Five observes ∼16,000 total values (mostly floats and categorical values with hundreds of possibilities) each time step. We discretize the action space; on an average timestep our model chooses among 8,000 to 80,000 actions (depending on hero). For comparison Chess requires around one thousand values per observation (mostly 6-possibility categorical values) and Go around six thousand values (all binary). Chess has a branching factor of around 35 valid actions, and Go around 250.
>
> Our system played Dota 2 with two limitations from the regular game:
>
> - Subset of 17 heroes --- in the normal game players select before the game one from a pool of 117 heroes to play; we support 17 of them.
> - No support for items which allow a player to temporarily control multiple units at the same time (Illusion Rune, Helm of the Dominator, Manta Style, and Necronomicon). We removed these to avoid the added technical complexity of enabling the agent to control multiple units.

**3.1 Playing Dota using AI** (excerpt)

> Certain game mechanics were controlled by hand-scripted logic rather than the policy: the order in which heroes purchase items and abilities, control of the unique courier unit, and which items heroes keep in reserve. While we believe the agent could ultimately perform better if these actions were not scripted, we achieved superhuman performance before doing so.

> Figure 1: Simplified OpenAI Five Model Architecture: The complex multi-array observation space is processed into a single vector, which is then passed through a 4096-unit LSTM. The LSTM state is projected to obtain the policy outputs (actions and value function). Each of the five heroes on the team is controlled by a replica of this network with nearly identical inputs, each with its own hidden state. The networks take different actions due to a part of the observation processing's output indicating which of the five heroes is being controlled. The LSTM composes 84% of the model's total parameter count.

> We define a policy (π) as a function from the history of observations to a probability distribution over actions, which we parameterize as a recurrent neural network with approximately 159 million parameters (θ). The neural network consists primarily of a single-layer 4096-unit LSTM (see Figure 1). Given a policy, we play games by repeatedly passing the current observation as input and sampling an action from the output distribution at each timestep.
>
> Separate replicas of the same policy function (with identical parameters θ) are used to control each of the five heroes on the team. Because visible information and fog of war (area that is visible to players due to proximity of friendly units) are shared across a team in Dota 2, the observations are nearly identical for each hero. [Footnote: We do include a very small number of derived features which depend on the hero being controlled, for example the "distance to me" feature of each unit in the game.]

> Because of the expansive nature of the problem and the size and expense of each experiment, it was not practical to investigate all the details of the policy and training system. Many details, even some large ones, were set for historical reasons or on the basis of preliminary investigations without full ablations.

**3.2 Optimizing the Policy** (excerpts)

> Our goal is to find a policy which maximizes the probability of winning the game against professional human experts. In practice, we maximize a reward function which includes additional signals such as characters dying, collecting resources, etc. We also apply several techniques to exploit the zero-sum multiplayer structure of the problem when computing the reward function — for example, we symmetrize rewards by subtracting the reward earned by the opposing team.

> Figure 2: System Overview: Our training system consists of 4 primary types of machines. Rollouts run the Dota 2 game on CPUs. They communicate in a tight loop with Forward Pass GPUs, which sample actions from the policy given the current observation. Rollouts send their data to Optimizer GPUs, which perform gradient updates. The Optimizers publish the parameter versions to storage in the Controller, and the Forward Pass GPUs occasionally pull the latest parameter version. Machine numbers are for the Rerun experiment described in subsection 4.2; OpenAI Five's numbers fluctuated between this scale and approximately 3x larger.

> The policy is trained using Proximal Policy Optimization (PPO), a variant of advantage actor critic. [Footnote: Early on in the project, we considered other algorithms including other policy gradient methods, q-learning, and evolutionary strategies. PPO was the first to show initial learning progress.]

> "Rollout" worker machines run self-play games. They run these games at approximately 1/2 real time, because we found that we could run slightly more than twice as many games in parallel at this speed, increasing total throughput. … They play the latest policy against itself for 80% of games, and play against older policies for 20% of games (for details of opponent sampling, see Appendix N).

**4 Experiments and Evaluation** (excerpt)

> OpenAI Five is a single training run that ran from June 30th, 2018 to April 22nd, 2019. After ten months of training using 770±50 PFlops/s·days of compute, it defeated the Dota 2 world champions in a best-of-three match and 99.4% of human players during a multi-day online showcase.
>
> In order to utilize this level of compute effectively we had to scale up along three axes. First, we used batch sizes of 1 to 3 million timesteps (grouped in unrolled LSTM windows of length 16). Second, we used a model with over 150 million parameters. Finally, OpenAI Five trained for 180 days (spread over 10 months of real time due to restarts and reverts). Compared AlphaGo, we use 50 to 150 times larger batch size, 20 times larger model, and 25 times longer training time.

**4.1 Human Evaluation** (excerpts)

> Machine Learning systems often behave poorly when confronted with unexpected situations. While winning a single high-stakes showmatch against the world champion indicates a very high level of skill, it does not prove a broad understanding of the variety of challenges the human community can present. To explore whether OpenAI Five could be consistently exploited by creative or out-of-distribution play, we ran OpenAI Five Arena, in which we opened OpenAI Five to the public for competitive online games from April 18-21, 2019. In total, Five played 3,193 teams in 7,257 total games, winning 99.4%. [Footnote: Human players often abandoned losing games rather than playing them to the end, even abandoning games right after an unfavorable hero selection draft before the main game begins. OpenAI Five does not abandon games, so we count abandoned games as wins for OpenAI Five. These abandoned games (3140 of the 7215 wins) likely includes a small number of games that were abandoned for technical or personal reasons.] Twenty-nine teams managed to defeat OpenAI Five for a total of 42 games lost. [rendered as "4242" in the capture; see Inconsistencies]

> OpenAI Five's "playstyle" is difficult to analyze rigorously (and is likely influenced by our shaped reward function) but we can discuss in broad terms the flavor of comments human players made to describe how our agent approached the game. Over the course of training, OpenAI Five developed a distinct style of play with noticeable similarities and differences to human playstyles. Early in training, OpenAI Five prioritized large group fights in the game as opposed to accumulating resources for later, which led to games where they were significantly behind if the enemy team avoided fights early. This playstyle was risky and would result in quick wins in under 20 minutes if OpenAI Five got an early advantage, but had no way to recover from falling behind, leading to long and drawn out losses often over 45 minutes.
>
> As the agents improved, the playstyle evolved to align closer with human play while still maintaining many of the characteristics learned early on. OpenAI Five began to concentrate resources in the hands of its strongest heroes, which is common in human play. Five relied heavily on large group battles, effectively applying pressure when holding a significant advantage, but also avoided fights and focused on gathering resources if behind.
>
> The final agent played similar to humans in many broad areas, but had a few interesting differences. Human players tend to assign heroes to different areas of the map and only reassign occasionally, but OpenAI Five moved heroes back and forth across the map much more frequently. Human players are often cautious when their hero has low health; OpenAI Five seemed to have a very finely-tuned understanding of when an aggressive attack with a low-health hero was worth a risk. Finally OpenAI Five tended to more readily consume resources, as well as abilities with long cooldowns (time it takes to reload), while humans tend to hold on to those in case a better opportunity arises later.

**4.2 Validating Surgery with Rerun** (excerpts)

> Rerun took 2 months and 150±5 PFlops/s·days of compute (see Figure 4). This timeframe is significantly longer than the frequency of our surgery changes (which happened every 1-2 weeks). As a naive comparison, if we had trained from scratch after each of our twenty major surgeries, the project would have taken 40 months instead of 10 (in practice we likely would have made fewer changes).

> Rerun continued to improve beyond OpenAI Five's skill, and reached over 98% winrate against the final version of OpenAI Five.

> This process of surgery successfully allowed us to change the environment every week. However, the model ultimately plateaued at a weaker skill level than the from-scratch model was able to achieve. Learning how to continue long-running training without affecting final performance is a promising area for future work.

**4.4 Data Quality** (conclusion)

> These experiments on the early part of training indicate that high quality data matters even more than compute consumed; small degradations in data quality have severe effects on learning.

**5 Related Work — AlphaStar comparison**

> AlphaStar is particularly relevant to this paper. In that effort, which ran concurrently to our own, researchers trained agents to play Starcraft 2, another complex game with real-time performance requirements, imperfect information, and long time horizons. The model for AlphaStar used a similar hand-designed architecture to embed observations and an autoregressive action decoder, with an LSTM core to handle partial observability. Both systems used actor critic reinforcement learning methods as part of the overall objective. OpenAI Five has certain sub-systems hard-coded (such as item buying), whereas AlphaStar handled similar decisions (e.g. building order) by conditioning (during training) on statistics derived from human replays. OpenAI Five trained using self play, while AlphaStar used a league consisting of multiple agents, where agents were trained to beat certain subsets of other agents. Finally, AlphaStar's value network observed full information about the game state (including observations hidden from the policy); this method improved their training and exploring its application to Dota 2 is a promising direction for future work.

> Our use of self-play is similar in spirit to fictitious play, which has been successfully applied to poker - in this work we learn a distribution over opponents and use the latest policy rather than an average policy.

**6 Conclusion**

> When successfully scaled up, modern reinforcement learning techniques can achieve superhuman performance in competitive esports games. The key ingredients are to expand the scale of compute used, by increasing the batch size and total training time. In order to extend the training time of a single run to ten months, we developed surgery techniques for continuing training across changes to the model and environment. While we focused on Dota 2, we hypothesize these results will apply more generally and these methods can solve any zero-sum two-team continuous environment which can be simulated in parallel across hundreds of thousands of instances. In the future, environments and tasks will continue to grow in complexity. Scaling will become even more important (for current methods) as the tasks become more challenging.

**Appendix G — Reward function, Zero sum and Team Spirit** (excerpts)

> Our agent's ultimate goal is to win the game. In order to simplify the credit assignment problem (the task of figuring out which of the many actions the agent took during the game led to the final positive or negative reward), we use a more detailed reward function. … We give the agent reward (or penalty) for a set of actions which humans playing the game generally agree to be good (gaining resources, killing enemies, etc).
>
> All the results that we reward can be found in Table 5, with the amount of the reward. Some are given to every hero on the team ("Team") and some just to the hero who took the action "Solo." Note that this means that when team spirit is 1.0, the total amount of reward is five times higher for "Team" rewards than "Solo" rewards.

> - Zero sum: The game is zero sum (only one team can win), everything that benefits one team necessarily hurts the other team. We ensure that all our rewards are zero-sum, by subtracting from each hero's reward the average of the enemies' rewards.
> - Team Spirit: Because we have multiple agents on one team, we have an additional dimension to the credit assignment problem, where the agents need learn which of the five agent's behavior cause some positive outcome. The partial rewards defined in Table 5 are an attempt to make the credit assignment easier, but they may backfire and in fact add more variance if an agent receives reward when a *different* agent takes a good action. To attempt dealing with this, we have introduced team spirit. It measures how much agents on the team share in the spoils of their teammates. If each hero earns raw individual reward ρᵢ, then we compute the hero's final reward rᵢ as follows:
>
>   rᵢ = (1−τ)ρᵢ + τρ̄   (12)
>
>   with scalar ρ̄ being equal to mean of ρ. If team spirit is 0, then it's every hero for themselves; each hero only receives reward for their own actions rᵢ = ρᵢ. If team spirit is 1, then every reward is split equally among all five heroes; rᵢ = ρ̄. For a team spirit τ in between, team spirit-adjusted rewards are linearly interpolated between the two.
>
> Ultimately we care about optimizing for team spirit τ=1; we want the actions to be chosen to optimize the success of the entire team. However we find that lower team spirit reduces gradient variance in early training, ensuring that agents receive clearer reward for advancing their mechanical and tactical ability to participate in fights individually.

Table 5 (Shaped Reward Weights), flattened as captured: Win 5 Team · Hero Death −1 Solo · Courier Death −2 Team · XP Gained 0.002 Solo · Gold Gained 0.006 Solo · Gold Spent 0.0006 Solo · Health Changed 2 Solo · Mana Changed 0.75 Solo · Killed Hero −0.6 Solo · Last Hit −0.16 Solo · Deny 0.15 Solo · Gained Aegis 5 Team · Ancient HP Change 5 Team · Megas Unlocked 4 Team · T1 Tower 2.25 Team · T2 Tower 3 Team · T3 Tower 4.5 Team · T4 Tower 2.25 Team · Shrine 2.25 Team · Barracks 6 Team · Lane Assign −0.15 Solo (per second in wrong lane).

**Appendix H — Five replica networks** (excerpt)

> The policy network is designed to receive observations from our bot-API observation space, and interact with the game using a rich factorized action space. These structured observation and action spaces heavily inform the neural network architecture used. We use five replica neural networks, each responsible for the observations and actions of one of the heroes in the team. At a high level, this network consists of three parts: first the observations are processed and pooled into a single vector summarizing the state, then that is processed by a single-layer large LSTM, then the outputs of that LSTM are projected to produce outputs using linear projections.
>
> 1. In practice the Observation Processing portion of the model is also cloned 5 times for the five different heroes. The weights are identical and the observations are nearly identical — but there are a handful of derived features which are different for each replica (such as "distance to me" for each unit). Thus the five replicas produce nearly identical, but perhaps not entirely identical, LSTM inputs. These non-identical features form a small portion of the observation space, and were not ablated; it is possible that they are not needed at all.
> 2. The "Flattened Observation" and "Hero Embedding" are processed before being sent into the LSTM by a fully-connected layer and a "cross-hero pool" operation, to ensure that the non-identical observations can be used by other members of the team if needed.
> 3. The "Unit Embeddings" from the observation processing are carried along beside the LSTM, and used by the action heads to choose a unit to target.

**Appendix N — Self-play** (excerpt)

> OpenAI Five is trained without any human gameplay data through a self-improvement process named self-play. … In self-play training, we continually pit the current best version of an agent against itself or older versions, and optimize for new strategies that can defeat these past and present opponents.
>
> In training OpenAI Five 80% of the games are played against the latest set of parameters, and 20% play against past versions. We play occasionally against past parameter versions in order to obtain more robust strategies and avoid strategy collapse in which the agent forgets how to play against a wide variety of opponents because it only requires a narrow set of strategies to defeat its immediate past version.
>
> OpenAI Five uses a dynamic sampling system in which each past opponent i=1..N is given a quality score qᵢ. Opponent agents are sampled according to a softmax distribution; agent i is chosen with probability pᵢ proportional to e^{qᵢ}. Every 10 iterations we add the current agent to past opponent pool and initialize its quality score to the maximum of the existing qualities. After each rollout game is completed, if the past opponent defeats the current agent, no update is applied. If the current agent defeats a past opponent, an update is applied proportional to a learning rate constant η (which we fix at 0.01): qᵢ ← qᵢ − η/(N pᵢ).

(Note: Appendix N's own text says self-play was used for "StarCraft 2" among prior successes, while Section 5 contrasts OpenAI Five's self-play with AlphaStar's league.)

**Appendix O — Team spirit sweep and lane assignments** (excerpts)

> As discussed in Appendix G, we introduced a hyperparameter team spirit to control whether agents optimize for their individual reward or the shared reward of the team. … We see evidence that early in training, lower team spirits do better. At the very start team spirit 0 is the best, quickly ovdertaken by team spirit 0.3 and 0.5. We hypothesize that later in training team spirit 1.0 will be best, as it is optimizing the actual reward signal of interest.

> Lane Assignments: From a strategic perspective it makes sense for heroes to act in certain area of the map more than the others. Most inter-team skirmishes happen on lanes (3 distinct paths that connect opposing bases). At a certain stage of our work, we noticed that our agents developed a preference to stick together as a group of 5 on a single lane, and fighting any opponent coming their way. This represents a large local minimum, with higher short-term reward but lower long-term one as the resources from the other lanes are lost. After that we introduced lane assignments, which randomly assigned each hero to a subset of lanes, and penalized them with negative reward for leaving those lanes. However, the ablation study in Figure 30 indicates that this may not have been necessary in the end.

**Appendix D.1 — Per-hero participation predictions** (excerpt)

> We also looked at heroes participation in destroying objectives. In Figure 10 we can see different heroes' predictions for each of the objectives in game 1 of OpenAI Five Finals. In several cases all heroes predict they will participate in the attack (and they do). In few cases one or two heroes are left out, and indeed by watching the game replay we see that those heroes are busy in the different part of the map during that time.

**Appendix F.1 — Scripted Actions** (excerpt)

> Not all actions that a human takes in a game of Dota 2 are controlled by our RL agent. Some of the actions are scripted, meaning that we have written a rudimentary rules-based system to handle these decisions. Most of these are for historical reasons — at the start of the project we gave the model control over a small set of the actions, and we gradually expanded it over time. Each additional action that we remove from the scripted logic and hand to the model's control gives the RL system a higher potential skill cap, but comes with an cost measured in engineering effort to set it up and risks associated with learning and exploration. … The full set of remaining scripted actions is: Ability Builds … Item Purchasing … Item Swap … Courier Control: Each side has a single "Courier" unit which cannot fight but can carry items from the shop to the player which purchased them. We use a state-machine based logic to control this character.

**Appendix Q — Bloopers** (excerpts)

> Leading into The International competition in August 2018, we already a very good agent, but we felt it was likely not yet as good as the very best humans (as indeed turned out to be the case; we lost both games at that event). In the final few days before the games, we sought to explore high-variance options which had a chance of offering a surprising improvement. In the end, however, we ultimately believe that human intuition, especially under time pressure, is not the best way to set hyperparameters.

> One of our team members stumbled upon a very strange phenomenon while debugging a failed surgery. It turned out that replacing a certain set of 128 learned parameters in the model with zero increased the model's performance significantly (about 55% winrate after versus before). We believe that the optimizers were unable to find this direction for improvement because although the win rate was higher, the shaped reward was approximately the same. … In the early stages of applying team spirit, we attempted to randomize the team spirit parameter in each game. We had a fixed list of four possible team spirit values; each rollout game one was chosen at random. The agent was allowed to observe the current team spirit, via an embedding table with four entries. We hoped this might encourage exploring games of different styles, some very selfless games and some very selfish games.

> The initial training of OpenAI Five was done as a single consecutive experiment over multiple months. During that time new items, observations, heroes, and neural network components were added. The order of introduction of these changes was a priori not critical to learning, however when reproducing this result in Rerun with all the final observations, heroes, and items included, we found that one item — Divine Rapier — could cause the agents to enter a negative feedback loop that reduced their skill versus reference opponents. … We hypothesize that this effect was not observed during our initial long-lasting training because Rapier was only added after the team spirit hyperparamater was raised to 1. Rapier is a unique item which does not stay in your inventory when you die, but instead falls to the ground and can be picked up by enemies or allies. Because of this ability to transfer a high-value item, it is possible that the reward collected in a game increases in variance, thereby preventing OpenAI Five from learning a reliable value function.

**Appendix A — Compute caveat** (excerpt)

> In addition to the GPU machines doing optimization (roughly 30% of the cost by dollars spent) there are approximately the same number of GPUs running forward passes for the rollout workers (30%), as well as the actual rollouts CPUs running the selfplay games (30%) and the overhead of controllers, TrueSkill evaluators, CPUs on the GPU machines, etc (10%). … For these reasons the compute number for OpenAI Five should be taken with a large grain of salt, but this caveat does not apply to Rerun, which was trained without surgery.

**Appendix C — Hyperparameters, Rerun schedule** (Figure 7 caption, verbatim)

> Iteration 0 15k 23k 43k 54k · Time (days) 0 13 20 33 42 · TrueSkill 0 210 232 245 258 · Team Spirit 0.3 0.8 · GAE Horizon 180 secs 360 secs · Entropy coefficient 0.01 0.001 · Learning Rate 5e-5 5e-6. Figure 7: Hyperparameter changes during Rerun. … Each hyperparameter change was applied gradually over the course of 1-2 days, corresponding to several thousand iterations (the reported time in the table is the start of the change). Our pre-planned schedule included further changes to bring the experiment into line with OpenAI Five's final hyperparameters (Horizon to 840 sec, team spirit to 1.0, and learning rate to 1e-6), but Rerun reached OpenAI Five's skill level before we reached those hyperparameters.

Table 2 (Hyperparameters; columns Rerun / OpenAI Five / Baseline; "→" smooth monotonic transition, "↔" uncontrolled variation), as captured:

| Param | Rerun | OpenAI Five | Baseline |
|---|---|---|---|
| Frameskip | 4 | 4 | 4 |
| LSTM unroll length | 16 | 16 | 16 |
| Samples per segment | 16 | 16 | 16 |
| Number of optimizer GPUs | 512 | 480↔1,536 | 64 |
| Batch size / optimizer GPU (samples) | 120 | 120↔128 | 120 |
| Total batch size (samples) | 61,440 | 61,440↔196,608 | 7,680 |
| Total batch size (timesteps) | 983,040 | 983,040↔3,145,728 | 122,880 |
| Number of rollout GPUs | 512 | 500↔1,440 | 64 |
| Number of rollout CPUs | 51,200 | 80,000↔172,800 | 6,400 |
| Steps per iteration | 32 | 32 | 32 |
| LSTM size | 4096 | 2048 → 4096 | 4096 |
| Sample reuse | 1.0↔1.1 | 0.8↔2.7 | 1.0↔1.1 |
| Team spirit | 0.3 → 0.8 | 0.3 → 1.0 | 0.3 |
| GAE horizon | 180 s → 360 s | 60 s → 840 s | 180 s |
| GAE λ | 0.95 | 0.95 | 0.95 |
| PPO clipping | 0.2 | 0.2 | 0.2 |
| Value loss weight | 1.0 | 0.25↔1.0 | 1.0 |
| Entropy coefficient | 0.01 → 0.001 | 0.01 → 0.001 | 0.01 |
| Learning rate | 5e-5 → 5e-6 | 5e-5 ↔ 1e-6 | 5e-5 |
| Adam β1 / β2 | 0.9 / 0.999 | 0.9 / 0.999 | 0.9 / 0.999 |
| Past opponents (fraction of games) | 20% | 20% | 20% |
| Past opponents learning rate | 0.01 | 0.01 | 0.01 |

(The capture rendered the value-loss-weight cell for OpenAI Five as "0.25↔1.00.25 1.0"; read here as 0.25↔1.0.)

**Remaining sections, verbatim from the capture** (ar5iv rendering: math appears twice, Unicode then LaTeX source; footnote numbers are glued to words). Included so the record is self-contained.


```text
#### 3.3 Continual Transfer via Surgery

As the project progressed, our code and environment gradually changed for three different reasons:

1. 1. 

As we experimented and learned, we implemented changes to the training process (reward structure, observations, etc) or even to the architecture of the policy neural network.

2. 2. 

Over time we expanded the set of game mechanics supported by the agent’s action and observation spaces. These were not introduced gradually in an effort to build a perfect curriculum. Rather they were added incrementally as a consequence of following the standard engineering practice of building a system by starting simple and adding complexity piece by piece over time.

3. 3. 

From time to time, Valve publishes a new Dota 2 version including changes to the core game mechanics and the properties of heroes, items, maps, etc; to compare to human players our agent must play on the latest game version.

These changes can modify the shapes and sizes of the model’s layers, the semantic meaning of categorical observation values, etc.

When these changes occur, most aspects of the old model are likely relevant in the new environment. But cherry-picking parts of the parameter vector to carry over is challenging and limits reproducibility. For these reasons training from scratch is the safe and common response to such changes.

However, training OpenAI Five was a multi-month process with high capital expenditure, motivating the need for methods that can persist models across domain and feature changes. It would have been prohibitive (in time and money) to train a fresh model to a high level of skill after each such change (approximately every two weeks). For example, we changed to Dota 2 version 7.21d, eight days before our match against the world champions (OG); this would not have been possible if we had not continued from the previous agent.

Our approach, which we term “surgery”, can be viewed as a collection of tools to perform offline operations to the old model πθ\pi_{\theta} to obtain a new model π^θ^\hat{\pi}_{\hat{\theta}} compatible with the new environment, which performs at the same level of skill even if the parameter vectors θ^\hat{\theta} and θ\theta have different sizes and semantics. We then begin training in the new environment using π^θ^\hat{\pi}_{\hat{\theta}}. In the simplest case where the environment, observation, and action spaces did not change, our standard reduces to insisting that the new policy implements the same function from observed states to action probabilities as the old:

∀o​π^θ^​(o)=πθ​(o)\forall o~\hat{\pi}_{\hat{\theta}}(o)=\pi_{\theta}(o) (1) 

This case is a special case of Net2Net-style function preserving transformations [[23](#bib.bibx23)]. We have developed tools to implement [Equation 1](#S3.E1) exactly when possible (adding observations, expanding layers, and other situations), and approximately when the type of modification to the environment, observation space, or action space precludes satisfying it exactly. See [Appendix B](#A2) for further discussion of surgery.

In the end, we performed over twenty surgeries (along with many unsuccessful surgery attempts) over the ten-month lifetime of OpenAI Five (see [Table 1](#A2.T1) in [Appendix B](#A2) for a full list). Surgery enabled continuous training without loss in performance (see [Figure 4](#S4.F4)). In [subsection 4.2](#S4.SS2) we discuss our experimental verification of this method.
```

```text
#### 4.3 Batch Size

In this section, we evaluate the benefits of increasing the batch size using small scale experiments. Increasing the batch size in our case means two things: first, using twice as many optimizer GPUs to optimize over the larger batch, and second, using twice as many rollout machines and forward pass GPUs to produce twice as many samples to feed the increased optimizer pool.

One compelling benchmark to compare against when increasing the batch size is linear speedup: using 2x as much compute gets to the same skill level in 1/2 the time. If this scaling property holds, it is possible to use the same total amount of GPU-days (and thus dollars) to reach a given result[[28](#bib.bibx28)]. In practice we see less than this ideal speedup, but the speedup from increasing batch size is still noticeable and allows us to reach the result in less wall time.

To understand how batch size affects training speed, we calculate the “speedup” of an experiment to reach various TrueSkill thresholds, defined as:

speedup​(T)=Versions for baseline to first reach TrueSkill TVersions for experiment to first reach TrueSkill T\textrm{speedup}(T)=\frac{\textrm{Versions for baseline to first reach TrueSkill $T$}}{\textrm{Versions for experiment to first reach TrueSkill $T$}} (2) 

The results of varying batch size in the early part of training can be seen in [Figure 5](#S4.F5). Full details of the experimental setup can be found in [Appendix M](#A13). We find that increasing the batch size speeds up training through the regime we tested, up to batches of millions of observations.

Using the scale of Rerun, we were able to reach superhuman performance in two months. In [5(a)](#S4.F5.sf1), we see that Rerun’s batch size (983k time steps) had a speedup factor of around 2.5x over the baseline batch size (123k). If we had instead used the smaller batch size, then, we might expect to wait 5 months for the same result. We speculate that it would likely be longer, as the speedup factor of 2.5 applies at TrueSkill 175 early in training, but it appears to increase with higher TrueSkill.

Per results in [[28](#bib.bibx28)], we hoped to find (in the early part of training) linear speedup from increasing batch size; i.e. that it would be 2x faster to train an agent to certain thresholds if we use 2x the compute and data. Our results suggest that speedup is less than linear. However, we speculate that this may change later in training when the problem becomes more difficult. Also, given the relevant compute costs, in this ablation study we did not tune hyperparameters such as learning rate separately for each batch size.

#### 4.4 Data Quality

(a) Batch size: Larger batch size speeds up training. In the early part of training studied here, the speedup is sublinear in the computation and samples required. See [subsection M.1](#A13.SS1) for experiment details. (b) Data Staleness: Training on stale rollout data causes significant losses in training speed. Queue length estimates the amount of artificial staleness introduced; see [subsection M.2](#A13.SS2) for experiment details. (c) Sample Reuse: Reusing each sample of training data causes significant slowdowns. See [subsection M.3](#A13.SS3) for experiment details. Figure 5: Batch Size and data quality in early training: For each parameter, we ran multiple training runs varying only that parameter. These runs cover early training (approximately one week) at small scale (8x smaller than Rerun). On the left we plot TrueSkill over time for each run. On the right, we plot the “speedup” to reach fixed TrueSkill thresholds of 100, 125, 150, and 175 as a function of the parameter under study compared to the baseline (marked with ‘b’); see [Equation 2](#S4.E2). Higher speedup means that training was faster and more efficient. These four thresholds are chosen arbitrarily; a few are omitted when the uncertainties are too large (for example in [5(c)](#S4.F5.sf3) fewer than half the experiments reach 175, so that speedup curve would not be informative). 

One unusual feature of our task is the length of the games; each rollout can take up to two hours to complete. For this reason it is infeasible for us to optimize entirely on fully on-policy trajectories; if we waited to apply gradient updates for an entire rollout game to be played using the latest parameters, we could make only one update every two hours. Instead, our rollout workers and optimizers operate asynchronously: rollout workers download the latest parameters, play a small portion of the game, and upload data to the experience buffer, while optimizers continually sample from whatever data is present in the experience buffer to optimize ([Figure 2](#S3.F2)).

Early on in the project, we had rollout workers collect full episodes before sending it to the optimizers and downloading new parameters. This means that once the data finally enters the optimizers, it can be several hours old, corresponding to thousands of gradient steps. Gradients computed from these old parameters were often useless or destructive. In the final system rollout workers send data to optimizers after only 256 timesteps, but even so this can be a problem.

We found it useful to define a metric for this called staleness. If a sample was generated by parameter version NN and we are now optimizing version MM, then we define the staleness of that data to be M−NM-N. In [5(b)](#S4.F5.sf2), we see that increasing staleness by ∼8\sim 8 versions causes significant slowdowns. Note that this level of staleness corresponds to a few minutes in a multi-month experiment. Our final system design targeted a staleness between 0 and 1 by sending game data every 30 seconds of gameplay and updating to fresh parameters approximately once a minute, making the loop faster than the time it takes the optimizers to process a single batch (32 PPO gradient steps). Because of the high impact of staleness, in future work it may be worth investigating whether optimization methods more robust to off-policy data could provide significant improvement in our asynchronous data collection regime.

Because optimizers sample from an experience buffer, the same piece of data can be re-used many times. If data is reused too often, it can lead to overfitting on the reused data[[18](#bib.bibx18)]. To diagnose this, we defined a metric called the sample reuse of the experiment as the instantaneous ratio between the rate of optimizers consuming data and rollouts producing data. If optimizers are consuming samples twice as fast as rollouts are producing them, then on average each sample is being used twice and we say that the sample reuse is 2. In [5(c)](#S4.F5.sf3), we see that reusing the same data even 2-3 times can cause a factor of two slowdown, and reusing it 8 times may prevent the learning of a competent policy altogether. Our final system targets sample reuse ∼1\sim 1 in all our experiments.

These experiments on the early part of training indicate that high quality data matters even more than compute consumed; small degradations in data quality have severe effects on learning. Full details of the experiment setup can be found in [Appendix M](#A13).

#### 4.5 Long term credit assignment

Figure 6: Effect of horizon on agent performance. We resume training from a trained agent using different horizons (we expect long-horizon planning to be present in highly-skilled agents, but not from-scratch agents). The base agent was trained with a horizon of 180 seconds (γ=0.9993\gamma=0.9993), and we include as a baseline continued training at horizon 180s. Increasing horizon increases win rate over the trained agent at the point training was resumed, with diminishing returns at high horizons. 

Dota 2 has extremely long time dependencies. Where many reinforcement learning environment episodes last hundreds of steps ([[4](#bib.bibx4), [29](#bib.bibx29), [30](#bib.bibx30), [31](#bib.bibx31)]), games of Dota 2 can last for tens of thousands of time steps. Agents must execute plans that play out over many minutes, corresponding to thousands of timesteps. This makes our experiment a unique platform to test the ability of these algorithms to understand long-term credit assignment.

In [Figure 6](#S4.F6), we study the time horizon over which our agent discounts rewards, defined as

H=T1−γH=\frac{T}{1-\gamma} (3) 

Here γ\gamma is the discount factor [[17](#bib.bibx17)] and TT is the real game time corresponding to each step (0.133 seconds). This measures the game time over which future rewards are integrated, and we use it as a proxy for the long-term credit assignment which the agent can perform.

In [Figure 6](#S4.F6), we see that resuming training a skilled agent using a longer horizon makes it perform better, up to the longest horizons we explored (6-12 minutes). This implies that our optimization was capable of accurately assigning credit over long time scales, and capable of learning policies and actions which maximize rewards 6-12 minutes into the future. As the environments we attempt to solve grow in complexity, long-term planning and thinking will become more and more important for intelligent behavior.
```

```text
### Appendix B Surgery

 Date Iteration # params Change 6/30/2018 1 43,436,520 Experiment started 8/17/2018 81,821 43,559,322 Dota 2 version 7.19 adds new items, abilities, etc. 8/18/2018 84,432 43,805,274 Change environment to single courier;   
remove “cheating” observations 8/26/2018 91,471 156,737,674 Double LSTM size 9/27/2018 123,821 156,809,485 Support for more heroes 10/3/2018 130,921 156,809,501 Obs: Roshan spawn timing 10/12/2018 140,402 156,811,805 Item: Bottle 10/19/2018 144,121 156,286,925 Obs: Stock counts;   
Obs: Remove some obsolete obs 10/24/2018 150,111 156,286,867 Obs: Neutral creep & rune spawn timers 11/7/2018 161,482 156,221,309 Obs: Item swap cooldown;   
Obs: Remove some obsolete obs 11/28/2018 185,749 156,221,669 Item: Divine rapier;   
Obs: Improve observation of stale enemy heroes 12/10/2018 193,701 157,378,165 Obs: Modifiers on nonhero units. 12/14/2018 196,800 157,650,795 Action: Consumables on allies;   
Obs: Line of sight information;   
Obs: next item this hero will purchase;   
Action: buyback 12/20/2018 203,241 157,679,655 Dota 2 version 7.20 adds new items, new item slot, changes map, etc;   
Obs: number of empty inventory slots 1/23/2019 211,191 158,495,991 Obs: Improve observations of area of effects;   
Obs: improve observation of modifiers’ duration;   
Obs: Improve observations about item Power Treads. 4/5/2019 220,076 158,502,815 Dota 2 version 7.21 adds new items, abilities, etc. Table 1: All successful surgeries and major environment changes performed during the training of OpenAI Five. This table does not include surgeries which were ultimately reverted due to training failures, nor minor environment changes (such as improvements to partial reward weights or scripted logic). “Obs” indicates than a new observation was added as an input to the model or an existing one was changed. “Action” indicates that a new game action was made available, along with appropriate observations about the state of that action. “Item” indicates that a new item was introduced, including observation of the item and the action to use the item. The Dota 2 version updates (7.19, 7.20 and 7.21) include many new items, actions, and observations. 

As discussed in [3.3](#S3.SS3), we designed “surgery” tools for continuing to train a single set of paramters across changes to the environment, model architecture, observation space, and action space. The goal in each case is to resume training after the change without the agent losing any skill from the change. [Table 1](#A2.T1) lists the major surgeries we performed in the lifetime of the OpenAI Five experiment.

For changes which add parameters, one of the key questions to ask is how to initialize the new parameters. If we initialize the parameters randomly and continue optimization, then noise will flow into other parts of the model, causing the model to play badly and causing large gradients which destroy the learned behaviors.

In the rest of this appendix we provide details of the tools we used to continue training across each type of change. In general we had a high-skill model πθ\pi_{\theta} trained to act in one environment, and due to a change to the problem design we need to begin training a newly-shaped model π^θ^\hat{\pi}_{\hat{\theta}} in a new environment. Ultimately the goal is for the TrueSkill of agent π^θ^\hat{\pi}_{\hat{\theta}} to match that of πθ\pi_{\theta}.

##### Changing the architecture

In the most straightforward situation, the observation space, action space, and environment do not change. In this case, per [Equation 1](#S3.E1), we can insist that the new policy π^θ^\hat{\pi}_{\hat{\theta}} implement exactly the same mathematical function from observations to actions as the old policy.

A simple example here would be adding more units to an internal fully-connected layer of the model. Suppose that before the change, some part of the interior of the model contained an input vector xx (dimension dxd_{x}), which is transformed to an activation vector y=W1​x+B1y=W_{1}x+B_{1} (dimension dyd_{y}), which is then consumed by another fully-connected layer z=W2​y+B2z=W_{2}y+B_{2} (dimension dzd_{z}). We desire to increase the dimension of of yy from dyd_{y} to d^y\hat{d}_{y}. This causes the shapes of three parameter arrays to change: W1W_{1} (from [dx,dy][d_{x},d_{y}] to [dx,d^y][d_{x},\hat{d}_{y}]), B1B_{1} (from [dy][d_{y}] to [d^y][\hat{d}_{y}]), and W2W_{2} (from [dy,dz][d_{y},d_{z}] to [d^y,dz][\hat{d}_{y},d_{z}]).

In this case we initialize the new variables in the first layer as:

W^1=[W1R⁡()]B^1=[B1R⁡()]W^2=[W20]\hat{W}_{1}=\left[\begin{array}[]{c}W_{1}\\ R()\end{array}\right]\hskip 56.9055pt\hat{B}_{1}=\left[\begin{array}[]{c}B_{1}\\ R()\end{array}\right]\hskip 56.9055pt\hat{W}_{2}=\left[\begin{array}[]{cc}W_{2}&0\end{array}\right] (6) 

Where R⁡()R() indicates a random initialization. The initializations of W^1\hat{W}_{1} and B^1\hat{B}_{1} ensure that the first dyd_{y} dimensions of activations y^\hat{y} will be the same data as the old activations yy, and the remained will be randomized. The randomization ensures that symmetry is broken among the new dimensions. The initialization of W^2\hat{W}_{2}, on the other hand, ensures that the next layer will ignore the new random activations, and the next layer’s activations will be the same as in the old model; z^=z\hat{z}=z. The weights which are initialized to zero will move away from zero due to the gradients, if the corresponding new dimensions in yy are useful to the downstream function.

Initializing neural network weights to zero is a dangerous business, because it can introduce undesired symmetries between the indices of the output vector. However we found that in most cases of interest, this was easy to avoid by only zero-ing the minimal set of weights. In the example above, the symmetry is broken by the randomization of W^1\hat{W}_{1} and B^1\hat{B}_{1}.

A more advanced version of this surgery was required when we wanted to increase the model capacity dramatically, by increasing the hidden dimension of our LSTM from 2048 units to 4096 units. Because the LSTM state is recurrent, there was no way to achieve the separation present in [Equation 6](#A2.E6); if we randomize the new weights they will impact performance, but if we set them to zero then the new hidden dimensions will be symmetric and gradient updates will never differentiate them. In practice we set the new weights to random small values — rather than randomize new weight values on the same order of magnitude as the existing weights, we randomized new weights significantly smaller. The scale of randomization was set empirically by choosing the highest scale which did not noticeably decrease the agent’s TrueSkill.

##### Changing the Observation Space

Most of our surgeries caused the observation space changes, for example when we added 3 new float observations encoding the time until neutral creeps, bounties, and runes would spawn. In these cases it is impossible to insist that the new policy implement the same function from observation space to action space, as the input domain has changed. However, in some sense the input domain has not changed; the game state is still the same. In reality our system is not only a function π:o→a\pi:o\to a; before the policy sees the observation arrays, an “encoder” function EE has turned a game state ss into an input array oo:

(Game State Protobuf ​s)→𝐸(Observation Arrays ​o)→𝜋(Action ​a)\left(\textrm{Game State Protobuf }s\right)\xrightarrow{E}\left(\textrm{Observation Arrays }o\right)\xrightarrow{\pi}\left(\textrm{Action }a\right) (7) 

By adding new observations we are enhancing the encoder function EE, making it take the same game state and simply output richer arrays for the model to consume. Thus in this case while we cannot ensure that π^θ^=πθ\hat{\pi}_{\hat{\theta}}=\pi_{\theta}, we can ensure the functions are identical if we go one step back:

∀sπ^θ^​(E^​(s))=πθ​(E⁡(s))\forall s\hskip 10.00002pt\hat{\pi}_{\hat{\theta}}(\hat{E}(s))=\pi_{\theta}(E(s)) (8) 

When the change is simply additive, this can then be enforced as in the previous section. Suppose the new observations extend a vector xx from dimension dxd_{x} to dimension d^x\hat{d}_{x}, and the input vector xx is consumed by a weight matrix WW via y=W​xy=Wx (and yy is then processed by the rest of the model downstream). Then we initialize the new weights W^\hat{W} as:

W^=[W0]\hat{W}=\left[\begin{array}[]{cc}W&0\end{array}\right] (9) 

As before, this ensures that the rest of the model is unchanged, as the output is unchanged (y^=y\hat{y}=y). The weights which are initialized to zero will move away from zero due to the gradients, if the corresponding observations are found to be useful.

##### Changing the Environment or Action Space

The second broad class of changes are those which change the environment itself, either by making new actions available to the policy (e.g. when we replaced scripted logic for the Buyback action with model-controlled logic) or by simply changing the Dota 2 rules (for example when we moved to Dota 2 version 7.21, or when we added new items). For some of these changes, such as upgrading Dota 2 version, we found simply making the change on the rollout workers to be relatively stable; the old policy played well enough in the new environment that it was able to smoothly adapt.

Even so, whenever possible, we attempted to “anneal” in these new features, starting with 0% of rollout games played with the new environment or actions, and slowly ramping up to 100%. This prevents a common problem where a change in one part of the agent’s behavior could force unnecessary relearning large portions of the strategy. For example, when we attempted to give the model control of the Buyback action without annealing, the model-based control of the action was (at first) worse than the scripted version had been, causing the agent to adapt its overall strategies to games where allies and enemies alike often misuse this action. This would cause the agent to significantly drop in overall skill; while it would likely eventually recover, it may require “repeating" the investment of a large amount of compute. By annealing the new action in gradually, we ensure that the model never loses overall skill due to a sudden change of one part of the environment; when we observe the model losing TrueSkill during the annealing process, we revert and attempt the anneal at a slower rate. This annealing process makes sense even if the environment is becoming fundamentally “harder" because our agent’s skill is measured through winrates against other models; the opponent also has to play in the new environment.

##### Removing Model Parts

Requiring exact policy equivalence after the surgery outlaws many types of surgery. For example, most surgeries which remove parameters are not possible in this framework. For this reason our model continued to observe some “deprecated” observations, which were simply always set to constants. Further work such as [[24](#bib.bibx24)] has already begun to explore alternate methods of surgery which avoid this constraint.

##### Smooth Training Restart

The gradient moments stored by the Adam optimizer present a nuisance when restarting training with new parameter shape. To ensure that the moments have enough time to properly adjust, we use a learning rate of 0 for the first several hours of training after surgery. This also ensures that the distribution of rollout games has entered steady state by the time we begin training in earnest.

One additional nuisance when changing the shape of the model is the entire history of parameters which are stored (in the past opponent manager, see [Appendix N](#A14)), and used as opponents in rollouts. Because the rollout GPUs will be running the newest code, all of these past versions must be updated in the same way as the current version to ensure compatibility. If the surgery operation fails to exactly preserve the policy function, these frozen past agents will forever play worse, reducing the quality of the opponent pool. Therefore it is crucial to ensure agent behavior is unchanged after surgery.

##### Benefits of Surgery

These surgeries primarily permitted us to have a tighter iteration loop for these features. When we added a new game feature which we expect to only matter at high skill, it would simply be impossible to test and iterate on it by training from scratch. Using surgery from the current OpenAI Five, we could have a more feasible process, which allowed us to safely include many minor features and improvements that otherwise would have been impossible to verify, such as adding long-tail items (Bottle, Rapier), minor improvements to the observation space (stock counts, modifiers on nonheroes), and others.
```

```text
### Appendix E Observation Space

Figure 13: Dota 2’s human “Observation Space” ![Refer to caption](/html/1912.06680/assets/figures/unit-observations.png) Figure 14: Observation Space Overview: The arrays that OpenAI Five observes at each timestep. Most of OpenAI Five’s observations are unit-centered; for 189 different units on the map, we observe a set of basic properties. These units are grouped along the top of the figure. We observe some data about all units, some extra data about the primary units (the heroes), and even more data about the heroes on our team. A few observations are not tied to any unit. Finally, two observations having to do with hero control (terrain near me, and my previous action) are only observed about the individual hero that this LSTM replica operates. In this diagram blue bands represent categorical data and yellow bands represent continuous or boolean data; most entities (units, modifiers, abilities, items, and pickups), have some of each. Each piece of the figure summarizes the total dimensionality of that portion of the input. All together, an OpenAI Five hero observes 1,200 categorical values and 14,534 continuous/boolean values. Global data 22 time since game started 1 is it day or night? time to next day/night change 2 time to next spawn: creep, neutral, bounty, runes 4 time since seen enemy courier is that >> 40 seconds?a 2 min&max time to Rosh spawn 2 Roshan’s current max hp 1 is Roshan definitely alive? 1 is Roshan definitely dead? 1 Next Roshan drops cheese? 1 Next Roshan drops refresher? 1 Roshan health randomizationb 1 Glyph cooldown (both teams) 2 Stock countsc 4 Per-unit (189 units) 43 position (x, y, z) 3 facing angle (cos, sin) 2 currently attacking?e time since last attackd 2 max health last 16 timesteps’ hit points 17 attack damage, attack speed 2 physical resistance 1 invulnerable due to glyph? glyph timer 2 movement speed 1 on my team? neutral? 2 animation cycle time 1 eta of incoming ranged & tower creep projectile (if any) # melee creeps atking this unitd 3 [Shrine only] shrine cooldown 1 vector to me (dx, dy, length)e 3 am I attacking this unit?e is this unit attacking me?d,e eta projectile from unit to mee 3 unit type 1 current animation 1 Per-hero add’l (10 heroes) 25 is currently alive? 1 number of deaths 1 hero currently in sight? time since this hero last seen 2 hero currently teleporting? if so, target coordinates (x, y) time they’ve been channeling 4 respawn time 1 current gold (allies only) 1 level 1 mana: max, current, & regen 3 health regen rate 1 magic resistance 1 strength, agility, intelligence 3 currently invisible? 1 is using ability? 1 # allied/enemy creeps/heroes in line btwn me and this heroe 4 Per-allied-hero additional (5 allied heroes) 211 Scripted purchasing settingsb 7 Buyback: has?, cost, cooldown 3 Empty inventory & backpack slots 2 Lane Assignmentsb 3 Flattened nearby terrain: 14x14 grid of passable/impassable? 196 scripted build id next item to purchaseb 2 Nearby map (8x8)e 6 terrain: elevation, passable? 2 allied & enemy creep density 2 area of effect spells in effect.f 2 area of effect spells in effect.f 2 Previous Sampled Actione 310 Offset? (Regular, Caster, Ward) 3x2x9 Unit Target’s Embedding 128 Primary Action’s Embedding 128 Per-modifier (10 heroes x 10 modifiers & 179 non-heroes x 2 modifiers) 2 remaining duration 1 stack count 1 modifier name 1 Per-item (10 heroes x 16 items) 13 location one-hot (inventory/backpack/stash) 3 charges 1 is on cooldown? cooldown time 2 is disabled by recent swap? item swap cooldown 2 toggled state 1 special Power Treads one-hot (str/agi/int/none) 4 item name 1 Per-ability (10 heroes x 6 abilities) 7 cooldown time 1 in use? 1 castable 1 Level 1/2/3/4 unlocked?d 4 ability name 1 Per-pickup (6 pickups) 15 status one-hot (present/not present/unknown) 3 location (x, y) 2 distance from all 10 heroes 10 pickup name 1 Minimap (10 tiles x 10 tiles) 9 fraction of tile visible 1 # allied & enemy creeps 2 # allied & enemy wards 2 # enemy heroes 1 cell (x, y, id) 3 

- a 

These observations are leftover from an early version of Five which played a restricted 1v1 version of the game. They are likely obsolete and not needed, but this was not tested.

- b 

These observations are about our per-game randomizations. See [Appendix O](#A15).

- c 

For items: gem, smoke of deciept, observer ward, infused raindrop.

- d 

Observations are not visible per-se, but can be estimated. We use scripted logic to estimate them from visible observations.

- e 

These observations (only) are different for the five different heroes on the team.

- f 

This observation appears twice, and serves as an example of the difficulties of surgery. Although this is a categorical input, we began by treating it as a float input to save on engineering work (this observation is unlikely to be very important). Later the time came to upgrade it to a properly embedded categorical input, but our surgery tools do not support removing existing observations. Hence we added the new observation, but were forced to leave the deprecated observation as well.

Table 3: Full Observation Space:  All observations OpenAI Five receives at each time step. Blue rows are categorical data. Entries with a question mark are boolean observations (only take values 0 or 1 but treated as floats otherwise). The bulk of the observations are per-unit observations, observed for each of 189 units: heroes (5), creeps (30), buildings (21), wards (30), and courier (1) for each team, plus 15 neutrals. If the number of visible units in a category is less than the allotted number, the rest are padded with zeroes. If more, we observe only the units closest to allied heroes. Units in fog of war are not observed. When enemy heroes are in fog of war, we reuse the observation from the last time step when the unit was visible. 

At each time step one of our heroes observes ∼16,000\sim 16,000 inputs about the game state (mostly real numbers with some integer categorical data as well). See [Figure 14](#A5.F14) for a schematic outline of our observation space and [Table 3](#A5.T3) for a full listing of the observations.

Instead of using the pixels on the screen, we approximate the information available to a human player in a set of data arrays. This approximation is imperfect; there are small pieces of information which humans can gain access to which we have not encoded in the observations. On the flip side, while we were careful to ensure that all the information available to the model is also available to a human, the model does get to see *all* the information available simultaneously every time step, whereas a human needs to click into various menus and options to get that data. Although these discrepancies are a limitation, we do not believe they meaningfully detract from our ability to benchmark against human players.

Humans observe the game via a rendered screen, depicted in [Figure 13](#A5.F13). OpenAI Five uses a more semantic observation space than this for two reasons: First, because our goal is to study strategic planning and gameplay rather than focus on visual processing. Second, it is infeasible for us to render each frame to pixels in all training games; this would multiply the computation resources required for the project manyfold.

All float observations (including booleans which are treated as floats that happen to take values 0 or 1) are normalized before feeding into the neural network. For each observation, we keep a running mean and standard deviation of all data ever observed; at each timestep we subtract the mean and divide by the st dev, clipping the final result to be within (-5, 5).

### Appendix F Action Space

Dota 2 is usually controlled using a mouse and keyboard. The majority of the actions involve a high-level command (attack, use a certain spell, or activate a certain item), along with a target (which might be an enemy unit for an attack, or a spot on the map for a movement). For that reason we represent the action our agent can choose at each timestep as a single primary action along with a number of parameter actions.

The number of primary actions available varies from time step to time step, averaging 8.1 in the games against OG. The primary actions available at a given time include universal actions like noop, move, attack, and others; use or activate one of the hero’s spells; use or activate one of the hero’s items; situational actions such as Buyback (if dead), Shrine (if near a shrine), or Purchase (if near a shop); and more. For many of the actions we wrote simple action filters, which determine whether the action is available; these check if there is a valid target nearby, if the ability/item is on cooldown, etc. At each timestep we restrict the set of available actions using these filters and present the final choices to the model.

In addition to a primary action, the model chooses action parameters. At each timestep the model outputs a value for each of them; depending on the primary action, some of them are read and others ignored (when optimizing, we mask out the ignored ones since their gradients would be pure noise). There are 3 parameter outputs, Delay (4 dim), unit selection (189 dim), and offset (81 dim), described in [Figure 15](#A6.F15).

![Refer to caption](/html/1912.06680/assets/figures/delay_head.png) (a) Delay: An integer from 0 to 3 indicating which frame during the next frameskip to take the action on (see [Appendix L](#A12)). If 0, the action will be taken immediately when the game engine processes this time step; if 3, the action will be taken on the last game frame before the next policy observation. This parameter is never ignored. ![Refer to caption](/html/1912.06680/assets/figures/unit_head.png) (b) Unit Selection: One of the 189 visible units in the observation. For actions and abilities which target units, either enemy units or friendly units. For many actions, some of the possible unit targets will be invalid; attempting an action with an invalid target results in a noop. ![Refer to caption](/html/1912.06680/assets/figures/offset_head.png) (c) Offset: A 2D (X,Y)(X,Y) coordinate indicating a spatial offset, used for abilities which target a location on the map. The offset is interpreted relative to the caster or the unit selected by the Unit Selection parameter, depending on the ability. Both XX and YY are discrete integer outputs ranging from -4 to +4 inclusive, producing a grid of 81 possible coordinate pairs. Figure 15: Action Parameters 

All together this produces a combined factorized action space size of up to 30×4×189×81=1,837,08030\times 4\times 189\times 81=1,837,080 dimensions (30 being the maximum number of primary actions we support). This number ignores the fact that the number of primary actions is usually much lower; some parameters are masked depending on the primary action; and some parameter combinations are invalid and those actions are treated as no-ops.

To get a better picture, we looked at actual data from the two games played against Team OG, and simply counted number of available actions at each step. The average number of available actions varies significantly across heroes, as different heroes have different numbers spells and items with larger parameter counts. Across the two games the average number of actions for a hero varied from 8,000 to 80,000.

Unit Selection and Offset are actually implemented within the model as several different, mutually exclusive parameters depending on the primary action. For Unit Selection, we found that using a single output head caused that head to learn very well to target tactical spells and abilities. One ability called “teleport,” however, is significantly different from all the others — rather than being used in a tactical fight, it is used to strategically reposition units across the map. Because the action is much more rare, the learning signal for targeting this ability would be drowned out if we used a single model output head for both. For this reason the model outputs a normal Unit Selection parameter and a separate Teleport Selection parameter, and one or the other is used depending on the primary action. Similarly, the Offset parameter is split into “Regular Offset,” “Caster Offset” (for actions which only make sense offset from the caster), and “Ward Placement Offset” (for the rare action of placing observer wards).

We categorize all primary actions into 6 “Action target types” which determines which parameters the action uses, listed in [Table 4](#A6.T4).

Action Target Type Example Parameters No Target Power Treads Delay Point Target Move Delay, Offset (Caster) Unit Target Attack Delay, Unit Selection (Regular) Unit Offset Target Sniper’s Shrapnel Delay, Unit Selection (Regular), Offset (Regular) Teleport Target Town Portal Scroll Delay, Unit Selection (Teleport), Offset (Regular) Ward Target Place Observer Ward Delay, Offset (Ward) Table 4: Action Target Types 

#### F.1 Scripted Actions

Not all actions that a human takes in a game of Dota 2 are controlled by our RL agent. Some of the actions are scripted, meaning that we have written a rudimentary rules-based system to handle these decisions. Most of these are for historical reasons — at the start of the project we gave the model control over a small set of the actions, and we gradually expanded it over time. Each additional action that we remove from the scripted logic and hand to the model’s control gives the RL system a higher potential skill cap, but comes with an cost measured in engineering effort to set it up and risks associated with learning and exploration. Indeed even when adding these new actions gradually and systematically, we occasionally encountered instabilities; for example the agent might quickly learn never to take a new action (and thus fail to explore the small fraction of circumstances where that action helps), and thus moreover fail to learn (or unlearn) the dependent parts of the gameplay which require competent use of the new action.

In the end there were still several systems that we had not yet removed from the scripted logic by the time the agent reached superhuman performance. While we believe the agent could ultimately perform better if these actions were not scripted, we saw no reason to do remove the scripting because superhuman performance had already been achieved. The full set of remaining scripted actions is:

1. 1. 

Ability Builds: Each hero has four spell abilities. Over the course of the game, a player can choose which of these to “level up,” making that particular skill more powerful. For these, in evaluation games we follow a fixed schedule (improve ability X at level 1, then Y at level 2, then Z at level 3, etc). In training, we randomize around this fixed script somewhat to ensure the model is robust to the opponent choosing a different schedule.

2. 2. 

Item Purchasing: As a hero gains gold, they can purchase items. We divide items into *consumables* --- items which are consumed for a one-time benefit such as healing --- and everything else. For consumables, we use a simple logic which ensures that the agent always has a certain set of consumables; when the agent uses one up, we then purchase a new one. After a certain time in the game, we stop purchasing consumables. For the non-consumables we use a system similar to the ability builds - we follow a fixed schedule (first build X, then Y, then Z, etc). Again at training time we randomly perturb these builds to ensure robustness to opponents using different items.1111 11 This randomization is done randomly deleting items from the build order and randomly inserting new items sampled from the distribution of which items that hero usually buys in human games. This is the only place in our system which relies on data from human games.

3. 3. 

Item Swap: Each player can choose 6 of the items they hold to keep in their “inventory” where they are actively usable, leaving up to 3 inactive items in their “backpack.” Instead of letting the model control this, we use a heuristic which approximately keeps the most valuable items in the inventory.

4. 4. 

Courier Control: Each side has a single “Courier” unit which cannot fight but can carry items from the shop to the player which purchased them. We use a state-machine based logic to control this character.

```

```text
### Appendix J TrueSkill: Evaluating a Dota 2 Agent Automatically

We use the TrueSkill [[27](#bib.bibx27)] rating system to evaluate our agents.

We first establish a pool of many reference agents of known skill. We evaluate the reference agents’ TrueSkill by playing many games between the the various reference agents, and using the outcome of the games to compute a TrueSkill for each agent. Our TrueSkill environment use the parameters σ=25/3\sigma=25/3, β=σ/2\beta=\sigma/2, τ=0.0\tau=0.0, draw_probability=0.02. Reference agents’ μ\mu are aligned so that an agent playing randomly has μ=0\mu=0. A hand-crafted scripted agent which we wrote, which can defeat beginners but not amateur players, has TrueSkill around 105.

During our experiments we continually added new reference agents as our agent “outgrew” the existing ones. For all results in this work, however, use a single reference agent pool containing mostly agents from OpenAI Five’s training history along with some other smaller experiments at the lower end. The 83 reference agents range in TrueSkill from 0 (random play) to 254 (the version that beat the world champions).

To evaluate a training run during training, a dedicated set of computers continually download the latest agent parameters and plays games between the latest trained agent and the reference agents. We attempt to only play games against reference agents that are nearby in skill in order to gain maximally useful information; we avoid playing agents more than 10 TrueSkill points away (corresponding to a winrate less than 15% or more than 85%). When a game finishes, we use the TrueSkill algorithm to update the test agent’s TrueSkill, but treat the reference agent’s TrueSkill as a constant. After 750 games have been reported, we log that version’s TrueSkill and move on to the new current version. New agents are initialized with μ\mu equal to the final μ\mu of the previous agent. This system gives us updates approximately once every two hours during running experiments.

One difficulty in using TrueSkill across a long training experiment was maintaining consistent metrics with a changing environment. Two agents that were trained on different game versions must ultimately play on a single version of the game, which will result in an inherent advantage for the agent that trained on it. Older agents had their code upgraded in order to always be compatible with the newest version, but this still leads to metric inflation for newer agents who got to train on the same code they are evaluated on. This included any updates to the hero pool (adding new heroes that old agents didn’t train with), game client updates or balancing changes, and adding any new actions (using a particular consumable or item differently).

### Appendix K Dota 2 Gym Environment

#### K.1 Data flow between the training environment and Dota 2

Dota 2 includes a scripting API designed for building bots. The provided API is exposed through Lua and has methods for querying the visible state of the game as well as submitting actions for bots to take. Parts of the map that are out of sight are considered to be in the fog of war and cannot be queried through the scripting API, which prevents us from accidentally “cheating” by observing anything a human player would not be able to see (although see [Appendix Q](#A17)).

We designed our Dota 2 environment to behave like a standard OpenAI Gym environment[[59](#bib.bibx59)]. This standard respects an API contract where a step method takes action parameters and returns an observation from the next state of the environment. To send actions to Dota 2, we implemented a helper process in Go that we load into Dota 2 through an attached debugger that exposes a gRPC server. This gRPC server implements methods to configure a game and perform an environment step. By running the game with an embedded server, we are able to communicate with it over the network from any remote process.

When the step method is called in the gRPC server, it gets dispatched to the Lua code and then the method blocks until an observation arrives back from Lua to be returned to the caller. In parallel, the Dota 2 engine runs our Lua code on every step, sending the current game state observation1212 12 Originally the Lua scripting API was used to iterate and gather the visible game state, however this was somewhat slow and our final system used an all-in-one game state collection method that was added through cooperation with Valve to the gRPC server and waiting for it to return the current action. The game blocks until an action is available. These two parallel processes end up meeting in the middle, exchanging actions from gRPC in return for observations from Lua. Go was chosen to make this architecture easy to implement through its channels feature.

Putting the game environment behind a gRPC server allowed us to package the game into a Docker image and easily run many isolated game instances per machine. It also allowed us to easily setup, reset, and use the environment from anywhere where Docker is running. This design choice significantly improved researcher productivity when iterating on and debugging this system.

### Appendix L Reaction time

Figure 19: Reaction Time:  OpenAI Five observes four frames bundled together, so any surprising new information will become available at a random frame in the red region. The model then processes the observation in parallel while the game engine runs forward four more frames. The soonest it can submit an action based on the red observations is marked in yellow. This is between 5 and 8 frames (167-267ms) after the surprising event. 

The Dota 2 game engine runs at 30 steps per second so in theory a bot could submit an action every 33ms. Both to speed up our game execution and in order to bring reactions of our model closer to the human scale we downsample to every 4th frame, which we call frameskip. This yields an effective observation and action rate of 7.5 frames per second. To allow the model to take precisely timed actions, the action space includes a “delay” which indicates which frame during the frameskip the model wants this action to evaluate on. Thus the model can still take actions at a particular frame if so desired, although in practice we found that the model did not learn to do this and simply taking the action at the start of the frameskip was better.

Moreover, we reduce our computational requirements by allowing the game and the machine learning model to run concurrently by asynchronously issuing actions with an action offset. When the model receives an observation at time TT, rather than making the game engine wait for the model to produce an action at time TT, we let the game engine carry on running until it produces an observation at time T+1T+1. The game engine then sends the observation at time T+1T+1 to the model, and by this time the model has produced its action choice based on the observation at time TT. In this way the action which the model takes at time T+1T+1 is based upon the observation at time TT. In exchange for this penalty in available “reaction time,” we are able to utilize our compute resources much more efficiently by preventing the two major computations from blocking one another (see [Figure 19](#A12.F19)).

Taken together, these effects mean that the agent can react to new information with a reaction time randomly distributed between 5 and 8 frames (167ms to 267ms), depending on when during the frameskip the new information happens to occur. For comparison, human reaction time has been measured at 250ms in controlled experimental settings[[26](#bib.bibx26)]. This is likely an underestimate of reaction time during a Dota game.

### Appendix M Scale and Data Quality Ablation Details

As shown in [Figure 5](#S4.F5) of the main text, we studied several key ingredients of RL at this scale, and learned important lessons which we conjecture should generalize beyond this environment. In this section we explain the details of these experiments.

Training runs the size of OpenAI Five are expensive; running a scan of 4 different variants would be prohibitively expensive. For this reason we use the normal Dota 2 environment, simply using a batch size 8x smaller than Rerun (which itself was 2-3 times smaller than OpenAI Five). See [Figure 20](#A13.F20) for an estimate of the variation in these training runs.

Figure 20: Variation in 5v5 baseline training: On the left, the TrueSkill over the course of training for different “baseline” experiments, using identical settings and hyperparameters. On the right, the standard deviation in TrueSkill across four runs. See [Appendix C](#A3) for the hyperparameters used. Although we only have 4 runs, we can estimate that different runs tend to vary by about 2 TrueSkill. 

Throughout the following sections we scan over various parameters of the experimental setup and monitor the results in terms of TrueSkill (see [Appendix J](#A10)) and speedup (see [Equation 2](#S4.E2)).

Our the uncertainty on speedup comes from uncertainty in both the numerator and the denominator. Although we have some understanding in the variance in the number of iterations for a baseline to reach each TrueSkill (see [Figure 20](#A13.F20)), we do not have the luxury of multiple runs of every experiment. Instead, we use as proxy for the uncertainty on the number of iterations to reach TrueSkill TT, the number of iterations to reach to reach T±Δ​TT\pm\Delta T where Δ​T\Delta T is the variance in TrueSkill across the variations in [Figure 20](#A13.F20), approximately 2 TrueSkill points. We combine the numerator and denominator uncertainty in quadrature to attain an overall uncertainty for the speedup.

In each experiment the baseline uses hyperparameters given in [Appendix C](#A3), except as noted.

#### M.1 Batch Size

Training using small mini-batches is a generally accepted trade-off between convergence time and number of optimization steps. However, recent literature on large-scale supervised learning of image classifiers [[44](#bib.bibx44), [45](#bib.bibx45), [46](#bib.bibx46)] explored much larger batch sizes and showed that strong scaling was possible by carefully tuning learning rate and initialization of the neural network. This renewed interest in reducing convergence-time and treating batch-size as a key design parameter also motivated the work of [[28](#bib.bibx28)], where an analytical tool is derived to estimate a training-time optimal batch size on per task basis by studying the “noise scale” of the gradients.

While existing literature on large-scale training of neural networks had focused on supervised learning, as far as we know using large batch sizes for reinforcement learning was novel when we began the Dota 2 project. These observations were later shown to be consistent with the analytical tools derived in [[28](#bib.bibx28)]. In this section we demonstrate how large batch-sizes affect optimization time.

Because we average gradients across the pool of optimizer machines, the effective total batch size is given by the product of the number of GPU optimizers with the batch size on each optimizer. We always use the maximum batch size on each optimizer which will fit within the GPU’s memory constraints (120 for our setup). Thus in order to change the overall batch size we increase the number of optimizer GPUs. We increase the size of the other machine pools in the experiment (rollout CPU workers, forward pass GPUs, etc), such that the larger batch size experiment is truly optimizing over more data, not simply reusing the same data more. This means that doubling the batch size causes the experiment to use twice as much computing power in almost all respects. Because we do not have the resources to separately optimize these hyperparameters at each individual batch size, we keep all other hyperparameters fixed to those listed under “baseline” in [Table 2](#A3.T2).

Figure 21: Effect of batch size on training speed: (Replicated from main text [5(a)](#S4.F5.sf1)) TrueSkill over the course of training (see [Appendix J](#A10)) and speedup measured by the rate to attain different TrueSkill thresholds (computed using [Equation 2](#S4.E2)) granted by increasing the batch size. The dotted line indicates perfect linear scaling (using 2x more data gives 2x speedup). Larger batch size significantly speeds up training, but the speedup is sublinear in the resources consumed. Later training (TrueSkill 175) benefits more from increased scale than earlier training (TrueSkill 100). Note that TrueSkill 175 is still quite early in the overall training of OpenAI Five which ultimately reaches above 250 (see [Figure 3](#S4.F3)), so these results are inconclusive about whether large batch size causes linear speedup for the bulk of the training time. 

Results can be seen in [5(a)](#S4.F5.sf1), with discussion in the main text.

#### M.2 Sample Quality — Staleness

In an ideal world, each piece of data in the optimizer would be perfectly on-policy (to obtain unbiased gradients), would be used exactly once and then thrown out (to avoid overfitting), would be from a completely different episode than every other piece of data (to eliminate correlations), and more. Because of our enormous batch size and small learning rate, we hypothesized that loosening the above constraints would not be a large price to pay in exchange for the benefits of asynchronous processing. However, we actually learned that issues like this surrounding data quality can be quite significant. In this and next section we will focus on two of these issues, which we call staleness and sample reuse.

Early on in the development of our agent we would play the whole game of Dota 2 using single set of parameters, then send this huge package of sample data to optimizers for training. One of the negative effects of this approach was that this would render data stale; the policy parameters which played the start of the game would be an hour old or more, making the gradients estimated from them incorrect. Therefore we have switched to accumulating small amount of training data; sending it over to optimizers and updating agent parameters; then continuing with the same game.

In order to generate rollouts with a certain version of the parameters, a long round-trip has to happen (see [Figure 2](#S3.F2)). This new set of parameters is published to the controller, then independently pulled by forward pass machines, which only then will start using this version of parameters to perform forward-passes of our agent. Then some amount of gameplay must be rolled forward and after that the data is finally sent to the optimizers. In the meanwhile, the optimizers have been running on previously-collected data and advanced by some number of new gradient descent steps. In our setup where rollouts send about 30 seconds of gameplay in each chunk, this loop takes 1-2 minutes. Because our learning rate is small, and this is only a few minutes on the scale of a multi-week learning endeavor, one might expect this to be a minor concern — but to the contrary, we observe that this it can be a crucial detail.

In this study we artificially introducing additional delay to see the effect. This is implemented on the rollout workers; instead of sending their data immediately back to the optimizers, they now put it in a queue, and pop data off the end of it to send to the optimizers. Thus the length of the queue determines the amount of artificial staleness introduced. See [Figure 23](#A13.F23); we observe the desired increase in measured staleness with the length of the queue.

The results can be found in the main text in [5(b)](#S4.F5.sf2), and are reproduced in [Figure 22](#A13.F22). Staleness negatively affects speed of training, and the drop can be quite severe when the staleness is larger than a few versions. For this reason we attempt to keep staleness as low as possible in our experiments.

Figure 22: Effect of Staleness on training speed. (Replicated from main text [5(b)](#S4.F5.sf2)) TrueSkill over the course of training (see [Appendix J](#A10)) and speedup measured by the rate to attain different TrueSkill thresholds (computed using [Equation 2](#S4.E2)) granted by increasing Staleness. Increasing staleness of data causes significant losses in training speed. Figure 23: Adding a queue that buffers rollout data on the way to optimizers increases measured staleness in a predictable manner. Error bars indicate the standard deviation of measured staleness as it varied over the course of training due to distributed systems fluctuations. 

#### M.3 Sample Quality — Sampling and Sample Reuse

Our asynchronous training system reuses samples in multiple optimization steps. Each optimizer’s experience buffer is constantly asynchronously collecting data from rollout machines. At each optimization step, a batch of data is sampled from this buffer. The buffer is configured to hold 4096 samples. Our optimizers compute the average sample reuse as the ratio between data arrival and consumption rates:

Sample Reuse≡(samples per batch)×(batches per second)(experience buffer intake samples per second)\textrm{Sample Reuse}\equiv\frac{\left(\textrm{samples per batch}\right)\times\left(\textrm{batches per second}\right)}{\left(\textrm{experience buffer intake samples per second}\right)} (13) 

Sample reuse is a function of the round trip time between rollout machines and optimizers, the ratio of rollout machines to optimizers, and other factors, and thus we only approximately hit target values but do not set them exactly. We measure the effect of sample reuse by varying the rate of incoming samples to the optimizers. In practice, the rate of data production from each rollout worker stays relatively stable, so we vary this rate by changing the number of rollout CPU workers and forward pass GPUs while keeping the number of optimizers and everything else fixed.

Our baseline experiment is tuned to have a sample reuse of approximately 1. To measure the effect of sample reuse we reduced the number of rollouts by 2, 4, and 8x to induce higher sample reuse. Additionally we also doubled the number of rollouts for one experiment to investigate the regime where sample reuse is lower than 1. These adjustments yielded sample reuse measurements between 0.57 and 6.3 (see [Figure 25](#A13.F25)). It is important to highlight that adjusting the number of rollouts directly affects the number of simultaneous games being played, which affects the diversity of games that are used for training.

The results can be found in the main text in [5(c)](#S4.F5.sf3), and are reproduced in [Figure 24](#A13.F24). We found that increasing sample reuse causes a significant decrease in performance. As long as the optimizers are reusing data, adding additional rollout workers appears to be a relatively cheap way to accelerate training. CPUs are often easier and cheaper to scale up than GPUs and this can be a significant performance boost in some setups.

Figure 24: Effect of Sample Reuse on training speed. (Replicated from main text [5(c)](#S4.F5.sf3)) TrueSkill over the course of training (see [Appendix J](#A10)) and speedup measured by the rate to attain different TrueSkill thresholds (computed using [Equation 2](#S4.E2)) granted by increasing Sample Reuse. Increasing sample reuse causes significant slowdowns. In fact, the run with 1/8th as many rollout workers (sample reuse around 6.3), seems to have converged to less than 75 TrueSkill. Figure 25: As our target sample reuse increases measured sample reuse increases predictably. Error bars indicate the standard deviation of measured sample reuse as it varied over the course of training. 

The fact that our algorithms benefit from extremely low sample reuse underlines how sample inefficient they are. Ideally, our training methods could take a small amount of experience and use that to learn a great deal, but currently we cannot even usefully optimize over that experience for more than a couple of gradient steps. Learning to use rollout data more efficiently is one of the major areas for future work in RL research.

This investigation suggests that sample reuse below one can be beneficial. This experiment out performed all others after around iteration 5,000, including the experiment with sample reuse 1. The improvement over sample reuse 1 is minor compared to the gaps between more severe sample reuses, but it is significant. Intuitively one might expect that using each sample exactly once would be the most optimal, as no data would get wasted and no data would get used twice; collecting more data and then not optimizing over it would not help.

However, the sample reuse is measured as an average rate of data production to consumption ([Equation 13](#A13.E13)). Because the optimizers sample each batch randomly from the buffer, sample reuse 1 just means that on *average* each sample is used once, but in fact many samples are used twice, and some not used at all. For this reason producing twice as much data as we can consume still reduces the number of samples which get selected multiple times. Of course the magnitude of improvement is relatively small and the cost (doubling the number of rollout workers and forward pass GPUs) is significant. Doubling the number of rollout workers may also decrease correlation across samples; using two adjacent samples from the same game (when very little has changed between them) may have similar drawbacks to using the same sample twice.

Figure 26: Asynchronous training: Plots of TrueSkill over the course of training for a “baseline” experiment together with a “synchronous” run using only on-policy data (staleness = 0) and restricting each sample to be used at most once (max sample reuse = 1). On the left, the x-axis is wall time. On the right, the x-axis is iterations. Asynchronous training is nearly 3x faster at achieving TrueSkill 150 when measuring by wall time, even though the two runs perform similarly as a function of the number of iterations. 
```

```text
### Appendix P Hero Pool Size

Figure 31: Effect of hero pool size on training speed: TrueSkill over the course of training (see [Appendix J](#A10)) and speedup measured by the rate to attain different TrueSkill thresholds (computed using [Equation 2](#S4.E2)) granted by varying the size of the hero pool. Additional heroes slows down early training only slightly. The severe underperformance of the 5-hero run for the first 4k versions was not investigated in detail. It is likely not due to the hero count but rather some instability in that particular training run. 

One of the primary limitations of our agent is its inability to play all the heroes in the game. We compared the progress in early training from training with various numbers of heroes. In all cases, each training game is played using an independent random sampling of five heroes from the pool for each team. To ensure a fair comparison across the runs, evaluation games are played using only the smallest set of heroes. Because the test environment uses only five heroes, the runs which train with fewer heroes are training closer to the test distribution, and thus can be expected to perform better; the question is how much better?

In [Figure 31](#A16.F31), we see that training with more heroes causes only a modest slowdown. Training with 80 heroes has a speedup factor of approximately 0.8, meaning early training runs 20% slower than with the base 17 heroes. From this we hypothesize that an agent trained on the larger set of heroes using the full resources of compute of Rerun would attain a similar high level of skill with approximately 20% more training time. Of course this experiment only compares the very early stages of training; it could be that the speedup factor becomes worse later in training.

```
