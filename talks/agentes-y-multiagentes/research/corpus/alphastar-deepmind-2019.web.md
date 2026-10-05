---
source_file: alphastar-deepmind-2019/
source_type: web-capture
ingested_at: 2026-10-04
---

# AlphaStar: Mastering the real-time strategy game StarCraft II (Google DeepMind blog, January 2019)

## Provenance
- Original location: research/web/alphastar-deepmind-2019/ (text from `page.md`, 28 KB, complete article)
- Format: html (DeepMind blog post, web capture via talksmith:ingest)
- URL: https://deepmind.google/blog/alphastar-mastering-the-real-time-strategy-game-starcraft-ii/
- Fetched: 2026-10-04T19:22:57Z (HTTP 200)
- Author / source (if known): "The AlphaStar team" (byline). Team list: Oriol Vinyals, Igor Babuschkin, Junyoung Chung, Michael Mathieu, Max Jaderberg, Wojtek Czarnecki, Andrew Dudzik, Aja Huang, Petko Georgiev, Richard Powell, Timo Ewalds, Dan Horgan, Manuel Kroiss, Ivo Danihelka, John Agapiou, Junhyuk Oh, Valentin Dalibard, David Choi, Laurent Sifre, Yury Sulsky, Sasha Vezhnevets, James Molloy, Trevor Cai, David Budden, Tom Paine, Caglar Gulcehre, Ziyu Wang, Tobias Pfaff, Toby Pohlen, Yuhuai Wu, Dani Yogatama, Julia Cohen, Katrina McKinney, Oliver Smith, Tom Schaul, Timothy Lillicrap, Chris Apps, Koray Kavukcuoglu, Demis Hassabis, David Silver.
- Date of original (if known): January 24, 2019 (matches played 19 December [2018]). Clarification added 29/01/19 on the APM figure.
- Note: this is the **January 2019** announcement, not the October 2019 *Nature* paper ("AlphaStar: Grandmaster level in StarCraft II using multi-agent reinforcement learning"), which appears only as a "Related posts" link.

## Key claims
- AlphaStar is "the first Artificial Intelligence to defeat a top professional player" in StarCraft II: beat Grzegorz "MaNa" Komincz 5-0, after a 5-0 benchmark against Dario "TLO" Wünsch; "under professional match conditions on a competitive ladder map and without any game restrictions."
- Plays the full game, "using a deep neural network that is trained directly from raw game data by supervised learning and reinforcement learning."
- StarCraft challenges: game theory (no single best strategy, like rock-paper-scissors), imperfect information (scouting), long-term planning (games up to one hour), real time, large action space ("approximately 10 to the 26 legal actions at every time-step").
- Architecture: "a transformer torso to the units (similar to relational deep reinforcement learning), combined with a deep LSTM core, an auto-regressive policy head with a pointer network, and a centralised value baseline."
- "AlphaStar also uses a novel multi-agent learning algorithm": supervised imitation from anonymised human replays first (this initial agent beat the built-in "Elite" AI — "around gold level for a human player" — in 95% of games), then **a multi-agent reinforcement learning process — the AlphaStar league**.
- League: "A continuous league was created, with the agents of the league - competitors - playing games against each other... New competitors were dynamically added to the league, by branching from existing competitors; each agent then learns from games against other competitors." It extends "population-based and multi-agent reinforcement learning", "while ensuring that each competitor performs well against the strongest strategies, and does not forget how to defeat earlier ones."
- Diversity: "each agent has its own learning objective" (which competitors to beat, internal motivations, e.g., build more of a particular unit); objectives are adapted during training.
- Weight update: "an efficient and novel off-policy actor-critic reinforcement learning algorithm with experience replay, self-imitation learning and policy distillation."
- Compute: league run 14 days, 16 TPUs (v3) per agent; each agent experienced up to 200 years of real-time play; final agent = components of the league's Nash distribution, running "on a single desktop GPU".
- Play: average APM around 280 (lower than pros); average observation-to-action delay 350 ms; raw interface (no camera) in the matches; agents "switched context" about 30 times per minute.
- Camera-interface version trained afterwards: almost as strong (>7000 MMR internal); a 7-day prototype **lost** to MaNa in an exhibition match.
- Conclusion claimed: success was "due to superior macro and micro-strategic decision-making, rather than superior click-rate, faster reaction times, or the raw interface."
- Protoss-only (Protoss v Protoss, StarCraft II v4.6.2, CatalystLE map).

## Definitions and terminology
- **AlphaStar league** — population of agents ("competitors") playing each other; new competitors branched, originals frozen, matchmaking probabilities and learning-objective hyperparameters adapted.
- **Nash distribution** — "the least exploitable set of complementary competitors"; "the most effective mixture of strategies that have been discovered". The final agent is sampled (without replacement) from it.
- **Macro / micro** — big-picture economy management vs. low-level unit control.
- **MMR** — Match Making Rating, "an approximate measure of a player's skill".
- **APM** — actions per minute.
- **Raw interface vs camera interface** — direct observation of all visible units vs. human-like camera-restricted perception and action.
- **"Cheesy" strategies** — risky quick rushes (Photon Cannons, Dark Templars) favoured early in the league, later discarded.

## Evidence and examples
- Results: 5-0 vs TLO; 5-0 vs MaNa (after an additional week of training); exhibition loss vs MaNa with the camera prototype.
- Strategy evolution in the league: cheesy rushes early → over-extending a base with more workers, sacrificing two Oracles to disrupt the opponent's economy.
- Quotes: TLO — "I was surprised by how strong the agent was... AlphaStar takes well-known strategies and turns them on their head." MaNa — "I've realised how much my gameplay relies on forcing mistakes and being able to exploit human reactions, so this has put the game in a whole new light for me."
- Claimed broader use: long-sequence prediction (weather, climate, language); safety/robustness — "league-based training process finds the approaches that are most reliable and least likely to go wrong."
- Competitions mentioned: AIIDE StarCraft AI Competition, CIG StarCraft Competition, Student StarCraft AI Tournament, StarCraft II AI Ladder; PySC2 released with Blizzard 2016–2017.

## Inconsistencies / open questions
- [verified] The multi-agent aspect is in **training** (a league of competing agents), while the deployed player is one agent per side sampled from the Nash distribution — checked against "How AlphaStar is trained" and the league figure caption. For the talk, AlphaStar is MARL-by-population (competitive self-play league), not a team of cooperating agents at inference time.
- [verified] APM figures are consistent but the caveat matters: text says "around 280", chart alt says mean 277 (AlphaStar), 390 (MaNa), 678 (TLO); the 29/01/19 clarification says TLO's APM is inflated by hot-key habits and that "AlphaStar's effective APM bursts are sometimes higher than both players" — checked within the page. The "lower APM" claim therefore applies to averages only.
- [verified] TLO is described as "a top professional Zerg player and a GrandMaster level Protoss player" — the 5-0 against TLO was played off his main race (Protoss v Protoss) — checked in "Evaluating AlphaStar".
- [verified] Link list item 5 is mislabelled in the source: "Watch game highlights of AlphaStar versus TLO and MaNa" (duplicate of item 4) points to a BibTeX file — checked in page.md.
- [open question] The claim that success was due to decision-making "rather than... the raw interface" rests on an internal-leaderboard MMR comparison, while the only public camera-interface game was a loss to MaNa; the later *Nature* paper (Oct 2019, not captured) would be needed for the stronger, restricted-conditions results.
- [open question] "first Artificial Intelligence to defeat a top professional player" — DeepMind's own claim; not independently checked.

## Images / diagrams

### alphastar-deepmind-2019.web/images/team-watching.jpg
- Provenance: `research/web/alphastar-deepmind-2019/assets/5lmq3iuq…=w1440-h810-n-nu.bin` (JPEG 1440×810, renamed). Hero image. Alt: "Members of the AlphaStar team watching a match with surprised and tense expressions."
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### alphastar-deepmind-2019.web/images/ingame-vs-tlo.jpg
- Provenance: `research/web/alphastar-deepmind-2019/assets/OhYgzlmP…=w1440.bin` (JPEG 1440×809, renamed). In "The Challenge of StarCraft". Alt: "In-game screenshot of a StarCraft II match between AlphaStar and LiquidTLO, showing Protoss structures and units harvesting resources, with a status overlay showing AlphaStar ahead in supply, minerals, and army size."
- Depiction: StarCraft II broadcast screenshot of a Protoss base (Nexus, workers, assimilators) at 14:32 on map Catalyst LE, with the observer bar comparing AlphaStar (blue) and LiquidTLO (red).
- Why it matters: Gives concrete scale for the matches; the APM row (AlphaStar 940 vs TLO 1377 at that moment) connects to the APM-fairness debate.
- Transcribed text: 14:32; Catalyst LE; score 0 AlphaStar / 0 LiquidTLO. AlphaStar: SUPPLY 177/200, MINERALS 945 (+2015), GAS 758 (+873), WORKERS 64, ARMY 113, APM 940. LiquidTLO: SUPPLY 147/172, MINERALS 335 (+1595), GAS 442 (+1030), WORKERS 61, ARMY 86, APM 1377. PRODUCTION. Overlays: 'Workers: 3/3', 'Workers: 25/16'.

### alphastar-deepmind-2019.web/images/62271e2f604e640534eeca99_AlphaStar2003.gif
- Provenance: `research/web/alphastar-deepmind-2019/assets/62271e2f604e640534eeca99_AlphaStar2003.gif` (animated GIF, 2.7 MB). Caption: "A visualisation of the AlphaStar agent during game two of the match against MaNa. This shows the game from the agent's point of view: the raw observation input to the neural network, the neural network's internal activations, some of the considered actions the agent can take such as where to click and what to build, and the predicted outcome. MaNa's view of the game is also shown, although this is not accessible to the agent."
- Depiction: Animated GIF (78 frames, inspected via 5 sampled frames). Black background; top-left the game rendered from the agent's view labelled 'AlphaStar' ('Render of Agent's view'), top-right MaNa's own screen labelled 'MaNa'. Below, a pipeline: 'Raw Observations' (map outline) -> 'Neural Network Activations' (three coloured blobs) -> 'Considered Location' (heat map over the map) and 'Considered Build/Train' (row of circles over unit/building names, one highlighted), plus an 'Outcome Prediction' area chart from Lose to Win staying near the top.
- Why it matters: Visual of a single agent's perception-to-action loop (observe -> network -> where to click / what to build -> value estimate); good to contrast what the agent 'sees' (raw observations, no camera) with the human view.
- Transcribed text: Labels: AlphaStar; MaNa; Render of Agent's view; Raw Observations; Neural Network Activations; Considered Location; Considered Build/Train; Outcome Prediction; Win; Draw; Lose. Build/Train item names are too small to read reliably.

### alphastar-deepmind-2019.web/images/alphastar-league-diagram.jpg
- Provenance: `research/web/alphastar-deepmind-2019/assets/5D7zdXHx…=w1440.bin` (JPEG 1440×644, renamed). Caption: "The AlphaStar league. Agents are initially trained from human game replays, and then trained against other competitors in the league. At each iteration, new competitors are branched, original competitors are frozen, and the matchmaking probabilities and hyperparameters determining the learning objective for each agent may be adapted, increasing the difficulty while preserving diversity. The parameters of the agent are updated by reinforcement learning from the game outcomes against competitors. The final agent is sampled (without replacement) from the Nash distribution of the league." Alt: "Diagram showing the AlphaStar League training process, where human data seeds a branching multi-agent reinforcement learning structure across hundreds of iterations, producing a Nash distribution of agents to play against professional StarCraft II players." **Likely the most relevant image for the talk (MARL league).**
- Depiction: Left: column 'Human Data' (league-rank badges) feeding the 'AlphaStar League'. Columns 'Iteration 1..4' show agent IDs branching (001 -> 003, 002; 002 -> 006, 005, 004 ...) with green = learning agents and blue = frozen copies accumulating each iteration. Centre: a green panel zooming on agent '006' with three parts — Neural Network, Matchmaking Probability (bars over opponents 009, 008, 007 ...), Hyperparameters — feeding a 'StarCraft II' match '006 vs 008' (Player vs Opponent) whose 'Rewards' loop back into the panel ('Reinforcement Learning'). Right: column 'Iteration 800' (agents 877 ... 865), a 'Nash Distribution' bar column (875 highlighted), and an arrow to 'StarCraft II Pro Match: 875 vs MaNa'.
- Why it matters: The central multi-agent training figure: population-based league, branching + freezing past agents, learned matchmaking against chosen opponents, and selection of final agents from the Nash distribution — the reference diagram for 'self-play generalised to a population'.
- Transcribed text: Human Data; AlphaStar League; Iteration 1, Iteration 2, Iteration 3, Iteration 4, ..., Iteration 800; agent IDs 001-009 (iterations 1-4), 865-877 (iteration 800); Reinforcement Learning; Neural Network 006; Matchmaking Probability (009, 008, 007, ...); Hyperparameters; Rewards; StarCraft II: 006 vs 008, Player / Opponent; Nash Distribution; StarCraft II Pro Match: 875 vs MaNa, Player / Opponent; legend 'Learning Agent' (green), 'Frozen Agent' (blue).

### alphastar-deepmind-2019.web/images/mmr-14-days.jpg
- Provenance: `research/web/alphastar-deepmind-2019/assets/iTlSuHDy…=w1440.bin` (JPEG 1139×600, renamed). Caption: "Estimate of the Match Making Rating (MMR) - an approximate measure of a player's skill - for competitors in the AlphaStar league, throughout training, in comparison to Blizzard's online leagues." Alt: "Scatter plot showing AlphaStar's estimated MMR rating over 14 days of reinforcement learning. Initial supervised learning agents cluster around 3000 MMR, while agents in the AlphaStar Training League show a steady upward trajectory. Notable milestones indicate AlphaStar defeating professional players TLO (Protoss) at approximately 5500 MMR around day 9, and MaNa at nearly 7000 MMR near day 14, placing the final agents well above Grandmaster rank."
- Depiction: Scatter plot of Estimated MMR (0-8000) vs Training Days (0-14). Grey left area 'Previously Trained Agents' (supervised agents, mostly 2000-4300, marked 'Supervised Learning' at ~2700); right area 'AlphaStar Training League' where points rise from ~4000 to ~7400 over 14 days. Callouts 'TLO (Protoss)' at ~5500 around day 9 and 'MaNa' at ~6800 around day 14. Horizontal reference lines at the right for league ranks Bronze, Silver, Gold, Platinum, Diamond, Master, Grandmaster.
- Why it matters: Shows the league's progression in skill and that supervised imitation alone stays at human-mid ranks; RL in the league is what reaches pro level within days.
- Transcribed text: Previously Trained Agents; AlphaStar Training League; Supervised Learning; TLO (Protoss); MaNa; Estimated MMR (0, 1000 ... 8000); Training Days (0, 2, 4, 6, 8, 10, 12, 14); ranks: Grandmaster, Master, Diamond, Platinum, Gold, Silver, Bronze.

### alphastar-deepmind-2019.web/images/nash-unit-composition.jpg
- Provenance: `research/web/alphastar-deepmind-2019/assets/pT5uBqzo…=w1440.bin` (JPEG 1139×600, renamed). Caption: "As training progressed, the league creating AlphaStar changed the blend of units that it builds." Alt: "A colorful area chart showing the unit counts of the Nash distribution in the AlphaStar League over 14 training days, illustrating the evolution of different Protoss units produced, such as Stalkers, Adepts, and Disruptors."
- Depiction: Ridgeline (joy) plot titled 'Units Counts of Nash of AlphaStar League': one coloured band per Protoss unit type (Stalker at the back to Tempest at the front) showing how many of each the Nash mixture builds over 14 training days. Callouts on the right.
- Why it matters: Shows strategy diversity and drift inside the league (Stalker-heavy at the end) — evidence that the population explores and then converges on compositions.
- Transcribed text: Units Counts of Nash of AlphaStar League. Units: Stalker, Zealot, Adept, Immortal, Observer, DarkTemplar, HighTemplar, Phoenix, Sentry, Oracle, Archon, VoidRay, WarpPrism, Disruptor, Carrier, Colossus, Mothership, Tempest. Callouts: '50 Stalkers made on average'; '2 Adepts made on average'; '2 Disruptors made on average'. X-axis Training Days 0-14.

### alphastar-deepmind-2019.web/images/62271f231cd532f91c5d4663_AlphaStar2007.gif
- Provenance: `research/web/alphastar-deepmind-2019/assets/62271f231cd532f91c5d4663_AlphaStar2007.gif` (animated GIF, 2.4 MB). Caption: "The figure shows how one agent (black dot), which was ultimately selected to play against MaNa, evolved its strategy and competitors (coloured dots) during the course of training. Each dot represents a competitor in the AlphaStar league. The position of the dot represents its strategy (inset), and the size of the dot represents how frequently it is selected as an opponent for the MaNa agent during training." Alt: "An animated scatter plot showing the strategic exploration of "MaNa Agent 4" during its training progression, alongside a changing bar chart of its game unit composition."
- Depiction: Animated GIF (144 frames, inspected via 5 sampled frames). Title 'MaNa Agent 4 Training Progression', subtitle 'Size indicates Matchmaking Distribution'. A 2D scatter of league competitors coloured by strategy cluster; a black dot 'MaNa Agent 4' moves through the strategy space across frames, and dot sizes change as matchmaking weight shifts. Inset bar chart 'Unit Composition' (Stalker ... Tempest) that becomes dominated by Stalkers in later frames.
- Why it matters: Shows one agent's trajectory through strategy space and how its chosen opponents change over training — matchmaking as a lever for diversity in multi-agent training.
- Transcribed text: MaNa Agent 4 Training Progression; Size indicates Matchmaking Distribution; MaNa Agent 4; Unit Composition; bar labels: Stalker, Zealot, Adept, Immortal, Observer, DarkTemplar, HighTemplar, Phoenix, Sentry, Oracle, Archon, VoidRay, WarpPrism, Disruptor, Carrier, Colossus, Mothership, Tempest.

### alphastar-deepmind-2019.web/images/nash-distribution-joyplot.jpg
- Provenance: `research/web/alphastar-deepmind-2019/assets/a_Fnn_8q…=w1440.bin` (JPEG 1139×600, renamed). Caption: "The Nash distribution over competitors as the AlphaStar league progressed and new competitors were created. The Nash distribution, which is the least exploitable set of complementary competitors, weights the newest competitors most highly, demonstrating continual progress against all previous competitors." Alt: "A 3D joyplot showing the progression of the Nash distribution of the AlphaStar League over 14 training days, where newer agents (with higher Agent IDs up to 600) shift to the right as training time progresses."
- Depiction: Diagonal ridgeline plot titled 'Progression of Nash of AlphaStar League': each horizontal line is a training moment (Training Days 0-14 along the diagonal axis), with peaks over Agent ID (0-600 on the x-axis). Peaks move right steadily — the Nash mixture always concentrates on the most recent agents. Colours shift cyan -> magenta with time.
- Why it matters: Evidence of continual progress: the least-exploitable mixture keeps favouring newer agents, i.e. new agents beat the whole previous population, not just the last one.
- Transcribed text: Progression of Nash of AlphaStar League; Training Days 0-14; Agent ID 0, 100, 200, 300, 400, 500, 600.

### alphastar-deepmind-2019.web/images/apm-comparison.jpg
- Provenance: `research/web/alphastar-deepmind-2019/assets/5GBTec2t…=w1440.bin` (JPEG 1139×600, renamed). Caption: "The distribution of AlphaStar's APMs in its matches against MaNa and TLO and the total delay between observations and actions. CLARIFICATION (29/01/19): TLO's APM appears higher than both AlphaStar and MaNa because of his use of rapid-fire hot-keys and use of the "remove and add to control group" key bindings. Also note that AlphaStar's effective APM bursts are sometimes higher than both players." Alt: "Line graph comparing the actions per minute (APM) of AlphaStar, TLO (Protoss), and MaNa, showing AlphaStar's mean APM at 277, MaNa's at 390, and TLO's at 678, alongside an inset histogram showing AlphaStar's action delay in milliseconds."
- Depiction: Overlaid density curves of Actions Per Minute (0-2000) for AlphaStar (blue), TLO (Protoss) (orange) and MaNa (red), with vertical lines for mean APM. Inset histogram of AlphaStar's 'Total Delay (ms)' between observation and action, with min and mean markers.
- Why it matters: Fairness constraint of agent-vs-human comparisons: AlphaStar's mean APM is lower than both pros, but the blue tail (and the page's clarification) shows bursts — relevant when discussing evaluating agents against humans.
- Transcribed text: Mean APM: 277 (AlphaStar), 390 (MaNa), 678 (TLO). Legend: AlphaStar, TLO (Protoss), MaNa. X-axis: Actions Per Minute (APM) 0, 500, 1000, 1500, 2000. Inset: Total Delay (ms) 0-1400; markers '67 (min)' and '350 (mean)'.

### alphastar-deepmind-2019.web/images/raw-vs-camera-interface.jpg
- Provenance: `research/web/alphastar-deepmind-2019/assets/ch78YBvL…=w1440.bin` (JPEG 1139×600, renamed). Caption: "Performance of AlphaStar using the raw interface and the camera interface, showing the newly trained camera agent rapidly catching up with and almost equalling the performance of the agent using the raw interface." Alt: "Line graph comparing the estimated MMR of AlphaStar agents trained using either the Raw Interface (red line) or Camera Interface (blue line) over 7 training days. Both interfaces show an upward trajectory exceeding 7000 MMR, placing them well above the skill level of professional players TLO (Protoss) and MaNa."
- Depiction: Line chart 'Comparison of Interfaces for Training': Estimated MMR (3500-8000) vs Training Days (0-7). Red 'Raw Interface' rises from ~4550 to ~7650; blue 'Camera Interface' starts ~4000, dips to ~3700, then rises to ~7450, close to the red line by day 7. Grey reference lines for MaNa (~6800) and TLO (Protoss) (~5500).
- Why it matters: Shows that restricting the agent to a human-like camera view costs little after training — relevant to how an agent's perception interface is designed.
- Transcribed text: Comparison of Interfaces for Training; Raw Interface; Camera Interface; MaNa; TLO (Protoss); Estimated MMR 3500-8000; Training Days 0-7.

### alphastar-deepmind-2019.web/images/untitled-704x704.jpg
- Provenance: `research/web/alphastar-deepmind-2019/assets/VxM6VzUX…=w704-h704-n-nu.bin` (JPEG 704×704, renamed). Thumbnail of the "Related posts → AlphaStar: Grandmaster level in StarCraft II using multi-agent reinforcement learning (October 2019)" card; no alt.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### alphastar-deepmind-2019.web/images/nav__gdm-lockup__light.height-25.svg
- Provenance: `research/web/alphastar-deepmind-2019/assets/nav__gdm-lockup__light.height-25.svg`. Google DeepMind logo (light), navigation chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### alphastar-deepmind-2019.web/images/nav__gdm-lockup__dark.height-25.svg
- Provenance: `research/web/alphastar-deepmind-2019/assets/nav__gdm-lockup__dark.height-25.svg`. Google DeepMind logo (dark), navigation chrome.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

## Raw / preserved excerpts

**Intro**

> Games have been used for decades as an important way to test and evaluate the performance of artificial intelligence systems. As capabilities have increased, the research community has sought games with increasing complexity that capture different elements of intelligence required to solve scientific and real-world problems. In recent years, StarCraft, considered to be one of the most challenging Real-Time Strategy (RTS) games and one of the longest-played esports of all time, has emerged by consensus as a "grand challenge" for AI research.
>
> Now, we introduce our StarCraft II program AlphaStar, the first Artificial Intelligence to defeat a top professional player. In a series of test matches held on 19 December, AlphaStar decisively beat Team Liquid's Grzegorz "MaNa" Komincz, one of the world's strongest professional StarCraft players, 5-0, following a successful benchmark match against his team-mate Dario "TLO" Wünsch. The matches took place under professional match conditions on a competitive ladder map and without any game restrictions.
>
> Although there have been significant successes in video games such as Atari, Mario, Quake III Arena Capture the Flag, and Dota 2, until now, AI techniques have struggled to cope with the complexity of StarCraft. The best results were made possible by hand-crafting major elements of the system, imposing significant restrictions on the game rules, giving systems superhuman capabilities, or by playing on simplified maps. Even with these modifications, no system has come anywhere close to rivalling the skill of professional players. In contrast, AlphaStar plays the full game of StarCraft II, using a deep neural network that is trained directly from raw game data by supervised learning and reinforcement learning.

**The Challenge of StarCraft** (challenge list)

> - **Game theory:** StarCraft is a game where, just like rock-paper-scissors, there is no single best strategy. As such, an AI training process needs to continually explore and expand the frontiers of strategic knowledge.
> - **Imperfect information:** Unlike games like chess or Go where players see everything, crucial information is hidden from a StarCraft player and must be actively discovered by "scouting".
> - **Long term planning:** Like many real-world problems cause-and-effect is not instantaneous. Games can also take anywhere up to one hour to complete, meaning actions taken early in the game may not pay off for a long time.
> - **Real time:** Unlike traditional board games where players alternate turns between subsequent moves, StarCraft players must perform actions continually as the game clock progresses.
> - **Large action space:** Hundreds of different units and buildings must be controlled at once, in real-time, resulting in a combinatorial space of possibilities. On top of this, actions are hierarchical and can be modified and augmented. Our parameterization of the game has an average of approximately 10 to the 26 legal actions at every time-step.

**How AlphaStar is trained** (complete section text)

> AlphaStar's behaviour is generated by a deep neural network that receives input data from the raw game interface (a list of units and their properties), and outputs a sequence of instructions that constitute an action within the game. More specifically, the neural network architecture applies a transformer torso to the units (similar to relational deep reinforcement learning), combined with a deep LSTM core, an auto-regressive policy head with a pointer network, and a centralised value baseline. We believe that this advanced model will help with many other challenges in machine learning research that involve long-term sequence modelling and large output spaces such as translation, language modelling and visual representations.
>
> AlphaStar also uses a novel multi-agent learning algorithm. The neural network was initially trained by supervised learning from anonymised human games released by Blizzard. This allowed AlphaStar to learn, by imitation, the basic micro and macro-strategies used by players on the StarCraft ladder. This initial agent defeated the built-in "Elite" level AI - around gold level for a human player - in 95% of games.
>
> These were then used to seed a multi-agent reinforcement learning process. A continuous league was created, with the agents of the league - competitors - playing games against each other, akin to how humans experience the game of StarCraft by playing on the StarCraft ladder. New competitors were dynamically added to the league, by branching from existing competitors; each agent then learns from games against other competitors. This new form of training takes the ideas of population-based and multi-agent reinforcement learning further, creating a process that continually explores the huge strategic space of StarCraft gameplay, while ensuring that each competitor performs well against the strongest strategies, and does not forget how to defeat earlier ones.
>
> As the league progresses and new competitors are created, new counter-strategies emerge that are able to defeat the earlier strategies. While some new competitors execute a strategy that is merely a refinement of a previous strategy, others discover drastically new strategies consisting of entirely new build orders, unit compositions, and micro-management plans. For example, early on in the AlphaStar league, "cheesy" strategies such as very quick rushes with Photon Cannons or Dark Templars were favoured. These risky strategies were discarded as training progressed, leading to other strategies: for example, gaining economic strength by over-extending a base with more workers, or sacrificing two Oracles to disrupt an opponent's workers and economy. This process is similar to the way in which players have discovered new strategies, and were able to defeat previously favoured approaches, over the years since StarCraft was released.
>
> To encourage diversity in the league, each agent has its own learning objective: for example, which competitors should this agent aim to beat, and any additional internal motivations that bias how the agent plays. One agent may have an objective to beat one specific competitor, while another agent may have to beat a whole distribution of competitors, but do so by building more of a particular game unit. These learning objectives are adapted during training.
>
> The neural network weights of each agent are updated by reinforcement learning from its games against competitors, to optimise its personal learning objective. The weight update rule is an efficient and novel off-policy actor-critic reinforcement learning algorithm with experience replay, self-imitation learning and policy distillation.
>
> In order to train AlphaStar, we built a highly scalable distributed training setup using Google's v3 TPUs that supports a population of agents learning from many thousands of parallel instances of StarCraft II. The AlphaStar league was run for 14 days, using 16 TPUs for each agent. During training, each agent experienced up to 200 years of real-time StarCraft play. The final AlphaStar agent consists of the components of the Nash distribution of the league - in other words, the most effective mixture of strategies that have been discovered - that run on a single desktop GPU.
>
> A full technical description of this work is being prepared for publication in a peer-reviewed journal.

**How AlphaStar plays and observes the game** (complete section text)

> Professional StarCraft players such as TLO and MaNa are able to issue hundreds of actions per minute (APM) on average. This is far fewer than the majority of existing bots, which control each unit independently and consistently maintain thousands or even tens of thousands of APMs.
>
> In its games against TLO and MaNa, AlphaStar had an average APM of around 280, significantly lower than the professional players, although its actions may be more precise. This lower APM is, in part, because AlphaStar starts its training using replays and thus mimics the way humans play the game. Additionally, AlphaStar reacts with a delay between observation and action of 350ms on average.
>
> During the matches against TLO and MaNa, AlphaStar interacted with the StarCraft game engine directly via its raw interface, meaning that it could observe the attributes of its own and its opponent's visible units on the map directly, without having to move the camera - effectively playing with a zoomed out view of the game. In contrast, human players must explicitly manage an "economy of attention" to decide where to focus the camera. However, analysis of AlphaStar's games suggests that it manages an implicit focus of attention. On average, agents "switched context" about 30 times per minute, similar to MaNa or TLO.
>
> Additionally, and subsequent to the matches, we developed a second version of AlphaStar. Like human players, this version of AlphaStar chooses when and where to move the camera, its perception is restricted to on-screen information, and action locations are restricted to its viewable region.
>
> We trained two new agents, one using the raw interface and one that must learn to control the camera, against the AlphaStar league. Each agent was initially trained by supervised learning from human data followed by the reinforcement learning procedure outlined above. The version of AlphaStar using the camera interface was almost as strong as the raw interface, exceeding 7000 MMR on our internal leaderboard. In an exhibition match, MaNa defeated a prototype version of AlphaStar using the camera interface, that was trained for just 7 days. We hope to evaluate a fully trained instance of the camera interface in the near future.
>
> These results suggest that AlphaStar's success against MaNa and TLO was in fact due to superior macro and micro-strategic decision-making, rather than superior click-rate, faster reaction times, or the raw interface.

**Evaluating AlphaStar against professional players**

> The game of StarCraft allows players to select one of three alien races: Terran, Zerg or Protoss. We elected for AlphaStar to specialise in playing a single race for now - Protoss - to reduce training time and variance when reporting results from our internal league. Note that the same training pipeline could be applied to any race. Our agents were trained to play StarCraft II (v4.6.2) in Protoss v Protoss games, on the CatalystLE ladder map. To evaluate AlphaStar's performance, we initially tested our agents against TLO: a top professional Zerg player and a GrandMaster level Protoss player. AlphaStar won the match 5-0, using a wide variety of units and build orders. "I was surprised by how strong the agent was," he said. "AlphaStar takes well-known strategies and turns them on their head. The agent demonstrated strategies I hadn't thought of before, which means there may still be new ways of playing the game that we haven't fully explored yet."
>
> After training our agents for an additional week, we played against MaNa, one of the world's strongest StarCraft II players, and among the 10 strongest Protoss players. AlphaStar again won by 5 games to 0, demonstrating strong micro and macro-strategic skills. "I was impressed to see AlphaStar pull off advanced moves and different strategies across almost every game, using a very human style of gameplay I wouldn't have expected," he said. "I've realised how much my gameplay relies on forcing mistakes and being able to exploit human reactions, so this has put the game in a whole new light for me. We're all excited to see what comes next."

**AlphaStar and other complex problems** (excerpt)

> We also think some of our training methods may prove useful in the study of safe and robust AI. One of the great challenges in AI is the number of ways in which systems could go wrong, and StarCraft pros have previously found it easy to beat AI systems by finding inventive ways to provoke these mistakes. AlphaStar's innovative league-based training process finds the approaches that are most reliable and least likely to go wrong. We're excited by the potential for this kind of approach to help improve the safety and robustness of AI systems in general, particularly in safety-critical domains like energy, where it's essential to address complex edge cases.
