---
source_file: react-repo-hotpotqa-prompt.md
source_type: article
ingested_at: 2026-10-04
---

# ReAct: the actual prompt and loop from the official repository (HotpotQA)

> **Librarian scope note.** This source is a verbatim capture made by the orchestrator on 2026-10-04, after the presenter asked "¿cuál es el system prompt de la trayectoria ReAct?". It copies two files from the ReAct paper's public repository: the notebook cell that builds the prompt and runs the loop (`hotpotqa.ipynb`), and the six few-shot trajectories under the key `webthink_simple6` (`prompts/prompts_naive.json`). Its framing prose is in Spanish; the code and exemplars are in English. The whole file is preserved verbatim in *Raw / preserved excerpts*.

## Provenance
- Original location: `research/articles/react-repo-hotpotqa-prompt.md`
- Format: md (orchestrator capture; 1 notebook cell in a ```` ```python ```` block + 6 exemplars in a ```` ```text ```` block; 9,264 bytes)
- Author / source (if known): repository https://github.com/ysymyth/ReAct, which the capture describes as the public code for Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models* (ICLR 2023). Files: https://raw.githubusercontent.com/ysymyth/ReAct/master/hotpotqa.ipynb and https://raw.githubusercontent.com/ysymyth/ReAct/master/prompts/prompts_naive.json (key `webthink_simple6`). Captured by the Talksmith orchestrator.
- Date of original (if known): capture 2026-10-04 (from the `master` branch). The paper is ICLR 2023 (arXiv 2210.03629). No commit hash recorded.
- Related records in this corpus: `yao-2022-react.pdf.md` (the paper; Appendix C.1 shows the exemplars) and `react-yao-2022.web.md` (arXiv abstract page).

## Key claims
- **ReAct has no "system prompt".** The capture says so directly: "No hay 'system prompt' en el sentido de una API de chat: el modelo (PaLM-540B / GPT-3 text-davinci-002) es de completado, y todo es un único texto: instrucción + 6 ejemplos + la pregunta nueva + 'Thought i:'." The prompt is **one completion text**, not a set of chat messages with roles.
- **How the prompt is assembled** (from the code, verbatim identifiers):
  1. `instruction`: one paragraph that defines the task and the three actions, ending "Here are some examples."
  2. `webthink_examples = prompt_dict['webthink_simple6']`: six full Question → Thought/Action/Observation → Finish trajectories.
  3. `webthink_prompt = instruction + webthink_examples`.
  4. Per question: `prompt += question + "\n"`, then each step calls `llm(prompt + f"Thought {i}:", stop=[f"\nObservation {i}:"])`.
- **The stop sequence is what makes it a loop.** The model generates the Thought and the Action and is cut at `"\nObservation {i}:"`. The code runs the action against Wikipedia (`step(env, ...)`), writes the real observation itself, appends `"Thought {i}: …\nAction {i}: …\nObservation {i}: …\n"` to the prompt, and asks for the next step. The model never writes the Observation; the environment does.
- **Where the instruction lives.** "el PDF del paper (Apéndice C.1) muestra solo las trayectorias de ejemplo; la línea de instrucción que define las tres acciones está en este código, no en el PDF." Checked: the string "Here are some examples" does not appear in `yao-2022-react.pdf.md` (grep, 0 hits).
- **The action space is three actions:** `Search[entity]` ("searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search."), `Lookup[keyword]` ("returns the next sentence containing keyword in the current passage"), `Finish[answer]` ("returns the answer and finishes the task").
- **Step budget:** `for i in range(1, 8)`, so at most 7 Thought/Action/Observation steps. If the episode has not finished, the code forces `step(env, "finish[]")` (an empty answer).
- **Malformed-output fallback:** if the generated text does not split on `"\nAction {i}: "`, the code prints `'ohh...'`, counts a bad call (`n_badcalls += 1`), keeps the first line as the Thought, and makes a second call `llm(prompt + f"Thought {i}: {thought}\nAction {i}:", stop=[f"\n"])` to get only the Action.
- **Action normalization:** the action is passed to the environment with its first letter lowercased (`action[0].lower() + action[1:]`), so `Search[...]` in the prompt becomes `search[...]` for the environment.
- **Return value:** reward `r` and `info` extended with `n_calls`, `n_badcalls` and `traj` (the full final prompt text, i.e. the whole trajectory).

## Definitions and terminology
- **`webthink`**: the repository's name for the ReAct (Thought + Action) variant on HotpotQA with a Wikipedia environment. `webthink_simple6` = the six-exemplar prompt set.
- **Trajectory (`traj`)**: the complete prompt string at the end of an episode: instruction + exemplars + question + all Thought/Action/Observation steps.
- **Completion model vs. chat API**: the capture's own contrast. A completion model receives one text and continues it; there are no system/user/assistant roles.
- **Stop sequence**: `stop=[f"\nObservation {i}:"]`, the string at which generation is cut so that the code, not the model, supplies the observation.
- **Prompt layout as the model sees it at step i** (derived by the librarian from the code; not a quote):
  ```text
  <instruction ... Here are some examples.>
  <6 exemplar trajectories>
  <question>
  Thought 1: <model>
  Action 1: <model>
  Observation 1: <code, from Wikipedia>
  ...
  Thought i:          <- generation starts here, stops at "\nObservation i:"
  ```

## Evidence and examples
- **The six exemplars** (all in Raw excerpts, verbatim):
  1. Colorado orogeny elevation range: 5 steps; Search, Lookup, Search (ambiguous "High Plains"), Search "High Plains (United States)", `Finish[1,800 to 7,000 ft]`. Shows recovery from an ambiguous search.
  2. Milhouse named after whom: Search, `Lookup[named after]`, `Finish[Richard Nixon]`. Shows Lookup inside a page.
  3. Adam Clayton Powell vs. The Saimaa Gesture: Search fails ("Could not find … Similar: [...]"), the model picks "Adam Clayton Powell (film)", then reasons by elimination: `Finish[The Saimaa Gesture]`. Shows handling a failed search.
  4. Nicholas Ray and Elia Kazan profession: two Searches, `Finish[director, screenwriter, actor]`.
  5. Arthur's Magazine vs. First for Women: two Searches, a comparison in the Thought ("1844 (Arthur's Magazine) < 1989 (First for Women)"), `Finish[Arthur's Magazine]`.
  6. Pavel Urysohn and Leonid Levin: two Searches, `Finish[yes]`.
- Exemplars 1 and 2 match the ReAct trajectories reproduced in `yao-2022-react.pdf.md` (Appendix C.1, "the prompt contains 6 such questions"). One cosmetic difference: the repo's Observation 3 ends "two distinct land regions:" and the PDF record's ends "regions" without the colon.
- The paper reports results with PaLM-540B and GPT-3 text-davinci-002 (`yao-2022-react.pdf.md`, Table 5). The `llm()` function and the environment (`env`, `step`) are not in the source capture. The librarian read them in the raw notebook that the orchestrator downloaded, and they are kept below as a separate, labelled supplementary excerpt. They show `text-davinci-002` at temperature 0, a Wikipedia environment on the HotpotQA dev split, and evaluation on 500 shuffled questions with exact match.

## Inconsistencies / open questions
- [verified] The capture is faithful. The notebook cell in the source is identical to cell 4 of `hotpotqa.ipynb`, and the exemplar block is identical to `webthink_simple6` apart from the leading and trailing newlines that the fence absorbs. Checked by a Python string comparison against the raw `hotpotqa.ipynb` and `prompts_naive.json` that the orchestrator downloaded to the session scratchpad on 2026-10-04.
- [verified] Exemplar 6 contains mojibake: "February 3, 1898 â August 17, 1924". It is an en dash (U+2013) whose UTF-8 bytes were decoded as Latin-1. The defect is **upstream**: the raw `prompts_naive.json` stores it literally as `â\u0080\u0093`, so the model saw "â" followed by two invisible control characters. Checked with `xxd` on the source and by reading the raw JSON bytes. If quoted on a slide, either write it as "February 3, 1898 – August 17, 1924" and note the fix, or keep the "â" as evidence that the prompt was used as-is.
- [verified] The model this notebook calls is **GPT-3 `text-davinci-002` through `openai.Completion.create`**, with `temperature=0`, `max_tokens=100`, `top_p=1` and a `stop` list. PaLM-540B was used in the paper's main tables but is not what this public notebook runs. Checked in cell 1 of the downloaded `hotpotqa.ipynb` (see the supplementary excerpt below; it is not in the source capture).
- [verified] The exemplar string starts with `"\n"` and ends with `"\n"`, so there is a blank line between "Here are some examples." and the first "Question:". Checked with `repr()` on the downloaded JSON.
- [verified] The notebook's evaluation runs `webthink` on 500 questions: `idxs = list(range(7405))`, shuffled with `random.Random(233)`, first 500, scored by `info['em']` (exact match). The environment is `wikienv.WikiEnv()` wrapped in `wrappers.HotPotQAWrapper(env, split="dev")` and `wrappers.LoggingWrapper`. This matches the paper's "random subset of 500 validation questions" for the GPT-3 runs (`yao-2022-react.pdf.md`, Table 5 caption). Checked in cells 2 and 5 of the downloaded notebook.
- [open question] The exact text that `env.reset(idx=idx)` returns as `question` is not in the capture or the notebook. The exemplars start with "Question: …", so the wrapper probably returns the question with that prefix. Settled by reading `wrappers.py` in the repo.
- [open question] The capture names the repository as the paper's official code. The paper itself points to https://react-lm.github.io/ (`yao-2022-react.pdf.md`), not directly to `github.com/ysymyth/ReAct`; the link between the two was not checked by the librarian. Settled by opening the project page.
- [verified] Call accounting: the loop makes at most 7 model calls per question, plus one extra call for each malformed step. On a malformed step `n_calls` goes up twice, once in the loop and once in the `except`, which matches the extra call. This is how the code counts, not a defect in the capture. Checked by reading the cell.

## Images / diagrams
The source carries no images. The companion folder `react-repo-hotpotqa-prompt.md/images/` exists and is intentionally empty.

## Raw / preserved excerpts
The complete source file, verbatim (wrapped in a four-backtick fence so its inner code fences survive):

````markdown
# ReAct — prompt y loop reales del repositorio oficial (HotpotQA)

Fuente capturada el 2026-10-04 por el orquestador, a pedido del presentador ("¿cuál es el system prompt de la trayectoria ReAct?").

- Repositorio: https://github.com/ysymyth/ReAct (código público asociado al paper Yao et al., ICLR 2023)
- Archivo 1: https://raw.githubusercontent.com/ysymyth/ReAct/master/hotpotqa.ipynb — celda que arma el prompt y corre el loop (verbatim abajo)
- Archivo 2: https://raw.githubusercontent.com/ysymyth/ReAct/master/prompts/prompts_naive.json — clave `webthink_simple6`: las 6 trayectorias de ejemplo (few-shot) que se concatenan después de la instrucción (verbatim abajo)

Nota: el PDF del paper (Apéndice C.1) muestra solo las trayectorias de ejemplo; la línea de instrucción que define las tres acciones está en este código, no en el PDF. No hay "system prompt" en el sentido de una API de chat: el modelo (PaLM-540B / GPT-3 text-davinci-002) es de completado, y todo es un único texto: instrucción + 6 ejemplos + la pregunta nueva + "Thought i:". El código corta la generación en "\nObservation i:", ejecuta la acción contra Wikipedia y pega la observación antes de pedir el siguiente paso.

## Celda del notebook (verbatim)

```python
import json
import sys

folder = './prompts/'
prompt_file = 'prompts_naive.json'
with open(folder + prompt_file, 'r') as f:
    prompt_dict = json.load(f)

webthink_examples = prompt_dict['webthink_simple6']
instruction = """Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be three types: 
(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists. If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.
Here are some examples.
"""
webthink_prompt = instruction + webthink_examples

def webthink(idx=None, prompt=webthink_prompt, to_print=True):
    question = env.reset(idx=idx)
    if to_print:
        print(idx, question)
    prompt += question + "\n"
    n_calls, n_badcalls = 0, 0
    for i in range(1, 8):
        n_calls += 1
        thought_action = llm(prompt + f"Thought {i}:", stop=[f"\nObservation {i}:"])
        try:
            thought, action = thought_action.strip().split(f"\nAction {i}: ")
        except:
            print('ohh...', thought_action)
            n_badcalls += 1
            n_calls += 1
            thought = thought_action.strip().split('\n')[0]
            action = llm(prompt + f"Thought {i}: {thought}\nAction {i}:", stop=[f"\n"]).strip()
        obs, r, done, info = step(env, action[0].lower() + action[1:])
        obs = obs.replace('\\n', '')
        step_str = f"Thought {i}: {thought}\nAction {i}: {action}\nObservation {i}: {obs}\n"
        prompt += step_str
        if to_print:
            print(step_str)
        if done:
            break
    if not done:
        obs, r, done, info = step(env, "finish[]")
    if to_print:
        print(info, '\n')
    info.update({'n_calls': n_calls, 'n_badcalls': n_badcalls, 'traj': prompt})
    return r, info
```

## webthink_simple6 — las 6 trayectorias few-shot (verbatim)

```text

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas.
Thought 2: It does not mention the eastern sector. So I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The eastern sector extends into the High Plains and is called the Central Plains orogeny.
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains. So I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]
Observation 3: High Plains refers to one of two distinct land regions:
Thought 4: I need to instead search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains. From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]
Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous. 
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[Richard Nixon]
Question: Which documentary is about Finnish rock groups, Adam Clayton Powell or The Saimaa Gesture?
Thought 1: I need to search Adam Clayton Powell and The Saimaa Gesture, and find which documentary is about Finnish rock groups.
Action 1: Search[Adam Clayton Powell]
Observation 1: Could not find [Adam Clayton Powell]. Similar: ['Adam Clayton Powell III', 'Seventh Avenue (Manhattan)', 'Adam Clayton Powell Jr. State Office Building', 'Isabel Washington Powell', 'Adam Powell', 'Adam Clayton Powell (film)', 'Giancarlo Esposito'].
Thought 2: To find the documentary, I can search Adam Clayton Powell (film).
Action 2: Search[Adam Clayton Powell (film)]
Observation 2: Adam Clayton Powell is a 1989 American documentary film directed by Richard Kilberg.
The film is about the rise and fall of influential African-American politician Adam Clayton Powell Jr.[3][4] It was later aired as part of the PBS series The American Experience.
Thought 3: Adam Clayton Powell (film) is a documentary about an African-American politician, not Finnish rock groups. So the documentary about Finnish rock groups must instead be The Saimaa Gesture.
Action 3: Finish[The Saimaa Gesture]
Question: What profession does Nicholas Ray and Elia Kazan have in common?
Thought 1: I need to search Nicholas Ray and Elia Kazan, find their professions, then find the profession they have in common.
Action 1: Search[Nicholas Ray]
Observation 1: Nicholas Ray (born Raymond Nicholas Kienzle Jr., August 7, 1911 – June 16, 1979) was an American film director, screenwriter, and actor best known for the 1955 film Rebel Without a Cause.
Thought 2: Professions of Nicholas Ray are director, screenwriter, and actor. I need to search Elia Kazan next and find his professions.
Action 2: Search[Elia Kazan]
Observation 2: Elia Kazan was an American film and theatre director, producer, screenwriter and actor.
Thought 3: Professions of Elia Kazan are director, producer, screenwriter, and actor. So profession Nicholas Ray and Elia Kazan have in common is director, screenwriter, and actor.
Action 3: Finish[director, screenwriter, actor]
Question: Which magazine was started first Arthur's Magazine or First for Women?
Thought 1: I need to search Arthur's Magazine and First for Women, and find which was started first.
Action 1: Search[Arthur's Magazine]
Observation 1: Arthur's Magazine (1844-1846) was an American literary periodical published in Philadelphia in the 19th century. 
Thought 2: Arthur's Magazine was started in 1844. I need to search First for Women next.
Action 2: Search[First for Women]
Observation 2: First for Women is a woman's magazine published by Bauer Media Group in the USA.[1] The magazine was started in 1989. 
Thought 3: First for Women was started in 1989. 1844 (Arthur's Magazine) < 1989 (First for Women), so Arthur's Magazine was started first.
Action 3: Finish[Arthur's Magazine]
Question: Were Pavel Urysohn and Leonid Levin known for the same type of work?
Thought 1: I need to search Pavel Urysohn and Leonid Levin, find their types of work, then find if they are the same.
Action 1: Search[Pavel Urysohn]
Observation 1: Pavel Samuilovich Urysohn (February 3, 1898 â August 17, 1924) was a Soviet mathematician who is best known for his contributions in dimension theory.
Thought 2: Pavel Urysohn is a mathematician. I need to search Leonid Levin next and find its type of work.
Action 2: Search[Leonid Levin]
Observation 2: Leonid Anatolievich Levin is a Soviet-American mathematician and computer scientist. 
Thought 3: Leonid Levin is a mathematician and computer scientist. So Pavel Urysohn and Leonid Levin have the same type of work. 
Action 3: Finish[yes]

```
````


### Supplementary excerpt (not in the source capture): other cells of the same `hotpotqa.ipynb`

These are verbatim from the raw `hotpotqa.ipynb` that the orchestrator downloaded to the session scratchpad on 2026-10-04 (https://raw.githubusercontent.com/ysymyth/ReAct/master/hotpotqa.ipynb). The notebook has 6 cells: 0 "# Setup" (markdown), 1 `llm()`, 2 environment and `step()`, 3 "# ReAct" (markdown), 4 the cell already captured above, and 5 the evaluation loop. The `step()` function in cell 2 is shown exactly as it appears in the notebook, ending at `attempts += 1` with no return or raise after the loop.

**Cell 1**

```python
import os
import openai
 
openai.api_key = os.environ["OPENAI_API_KEY"]

def llm(prompt, stop=["\n"]):
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=prompt,
      temperature=0,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.0,
      stop=stop
    )
    return response["choices"][0]["text"]
```

**Cell 2**

```python
import wikienv, wrappers
env = wikienv.WikiEnv()
env = wrappers.HotPotQAWrapper(env, split="dev")
env = wrappers.LoggingWrapper(env)

def step(env, action):
    attempts = 0
    while attempts < 10:
        try:
            return env.step(action)
        except requests.exceptions.Timeout:
            attempts += 1
```

**Cell 5**

```python
import random
import time
idxs = list(range(7405))
random.Random(233).shuffle(idxs)

rs = []
infos = []
old_time = time.time()
for i in idxs[:500]:
    r, info = webthink(i, to_print=True)
    rs.append(info['em'])
    infos.append(info)
    print(sum(rs), len(rs), sum(rs) / len(rs), (time.time() - old_time) / len(rs))
    print('-----------')
    print()
```
