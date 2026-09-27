---
source_file: nvidia-nemotron-nano-9b-v2-card
source_type: web-capture
ingested_at: 2026-09-27
---

# NVIDIA-Nemotron-Nano-9B-v2 — Hugging Face model card (NVIDIA, 2025)

## Provenance
- Original location: web/nvidia-nemotron-nano-9b-v2-card/ (text from `page.md`. `page.md` is 51056 chars with 52 heading lines, so no `original.html` fallback was needed. The code blocks, including the full Jinja chat template, came through intact in `page.md`.)
- Format: html (web capture via talksmith:ingest of the Hugging Face model page)
- URL: https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2
- Captured at: 2026-09-27T20:48:45Z (HTTP 200, 392568 bytes)
- Page title: nvidia/NVIDIA-Nemotron-Nano-9B-v2 · Hugging Face
- Author / source (if known): NVIDIA Corporation ("Model Developer: NVIDIA Corporation"). A vendor model card. License: "NVIDIA Open Model License Agreement". Tags on the page: Text Generation, Transformers, Safetensors, PyTorch, nemotron_h, conversational, custom_code; arxiv 2504.03624 (Nemotron-H), 2508.14444 (Nemotron Nano 2 report), 2412.02595 (Nemotron-CC).
- Date of original (if known): "Model Dates: June 2025 - August 2025". "Release Date: 08/18/2025" (Hugging Face and NVIDIA API Catalog). "Model Version: v1.0". The page is a living document; this is its state on 2026-09-27 (page counters at capture: "Like 520", "Downloads last month 368,132"; the "Articles mentioning" list includes posts dated Feb 17 and Mar 17, i.e. after release). Earlier or later versions of the card may differ.
- Focus note (why this source was added): the Talk's section on **reasoning control**. This card documents the **user-facing interface**: the `/think` and `/no_think` keywords in the system (or user) message, the chat template that turns them into `<think>\n` or `<think></think>` at the start of the assistant turn, the `max_thinking_tokens` budget, and a reference client that enforces the budget. Companion record: `nvidia-2025-nemotron-nano-2.web.md` (the technical report: **how** the on/off switch and budget were trained, and the Figure 5 evaluation). Related: `qwen-2025-qwen3-technical-report.pdf.md` (the same `/think` / `/no_think` convention in Qwen3).
- Images: the capture saved 4 distinct assets (the NVIDIA avatar is referenced 5 times and deduped). Kept: `acc-vs-budget.png` (the Reasoning Budget Control plot), copied to the companion folder `nvidia-nemotron-nano-9b-v2-card.web/images/`. Dropped, as the caller instructed (keep only images ≥300 px on one side **and** relevant to the reasoning-control focus): `huggingface_logo-noborder.svg` (site logo, 95 x 88), `Vs5FPVCH-VZBipV3qKTuy.png` (NVIDIA org avatar, actually WebP, 200 x 200), and `accuracy_chart.png` (2460 x 1030, the benchmark bar chart at the top of the card; content, but not about reasoning control). The dropped `accuracy_chart.png` is still at `web/nvidia-nemotron-nano-9b-v2-card/assets/accuracy_chart.png` if a later pass wants it; its numbers are transcribed from the card's table under Evidence.

## Key claims
Relevance for the Talk: the card shows that **reasoning on/off is a text switch in the prompt**, turned into a pre-filled `<think>` block by the chat template, and that the **thinking budget is enforced outside the model** by the serving client (it stops generation, closes `</think>` itself, then asks the model for the answer). The model is never told the budget number. How the model was trained to cope with that is in the companion paper record.

- **One model, both modes (Model Overview, verbatim):** "NVIDIA-Nemotron-Nano-9B-v2 is a large language model (LLM) trained from scratch by NVIDIA, and designed as a unified model for both reasoning and non-reasoning tasks. It responds to user queries and tasks by first generating a reasoning trace and then concluding with a final response. The model's reasoning capabilities can be controlled via a system prompt. If the user prefers the model to provide its final answer without intermediate reasoning traces, it can be configured to do so, albeit with a slight decrease in accuracy for harder prompts that require reasoning. Conversely, allowing the model to generate reasoning traces first generally results in higher-quality final solutions to queries and tasks."
- **The on/off interface (Use it with Transformers, verbatim):**
  - "Case 1: `/think` or no reasoning signal is provided in the system prompt, reasoning will be set to `True`"
    ```
    messages = [
        {"role": "system", "content": "/think"},
        {"role": "user", "content": "Write a haiku about GPUs"},
    ]
    ```
  - "Case 2: `/no_think` is provided, reasoning will be set to `False`"
    ```
    messages = [
        {"role": "system", "content": "/no_think"},
        {"role": "user", "content": "Write a haiku about GPUs"},
    ]
    ```
  - "Note: `/think` or `/no_think` keywords can also be provided in “user” messages for turn-level reasoning control."
  - Default is ON: "If no reasoning signal is added, the model defaults to reasoning "on" mode."
- **What the chat template does with the switch (Prompt Format, verbatim):** "This template conditionally adds `<think>\n` to the start of the Assistant response if `/think` is found in either the system prompt or any user message. If no reasoning signal is added, the model defaults to reasoning "on" mode. The chat template adds `<think></think>` to the start of the Assistant response if `/no_think` is found in the system prompt. Thus enforcing reasoning on/off behavior."
  - From the template code: the keywords are **removed** from the text the model sees (`.replace('/think', '').replace('/no_think', '')` on the system message and on each user message). The model sees the effect (an open `<think>\n` or an already-closed `<think></think>`), not the keyword.
  - From the template code: the flag is scanned over every user and system message in order, and **the last one found wins** (`ns.enable_thinking` is overwritten on each hit).
  - From the template code: earlier assistant turns are stored **without their thinking**: `{%- if '</think>' in content -%}{%- set content = content.split('</think>')[1].strip() %}`.
- **Budget definition (Using Budget Control with a vLLM Server, verbatim):** "`max_thinking_tokens`: This is a threshold that will attempt to end the reasoning trace at the next newline encountered in the reasoning trace. If no newline is encountered within 500 tokens, it will abruptly end the reasoning trace at `max_thinking_tokens + 500`." This matches the paper's §3.4 rule.
- **Why budget control (verbatim):** "The thinking budget allows developers to keep accuracy high and meet response‑time targets - which is especially crucial for customer support, autonomous agent steps, and edge devices where every millisecond counts." And: "With budget control, you can set a limit for internal reasoning".
- **Reasoning Budget Control section (verbatim, complete text):** "This model supports runtime “thinking” budget control. During inference, the user can specify how many tokens the model is allowed to "think"." Followed only by the image `acc-vs-budget.png` (no caption, no alt text).
- **The reference client enforces the budget in two calls** (`ThinkingBudgetClient.chat_completion`): (1) a chat completion with `max_tokens=max_thinking_budget`; if the returned text has no `</think>`, the client appends `".\n</think>\n\n"` (code comment: "reasoning content is too long, closed with a period (.)"); (2) it appends that text as an assistant message, renders the prompt with `continue_final_message=True`, and calls plain completions with `max_tokens = max_tokens - reasoning_tokens_len` to get the answer. Assertions require `max_tokens > max_thinking_budget` and a positive remainder.
- **Worked example (verbatim):** budget 32 tokens, system `"You are a helpful assistant. /think"`, user `"What is 2+2?"` → `{'reasoning_content': "Okay, the user asked, What is 2+2? Let me think. Well, 2 plus 2 equals 4. That's a basic.", 'content': '2 + 2 equals **4**.\n', 'finish_reason': 'stop'}`. The trace is cut mid-sentence ("That's a basic") and the client's "." is visible; the answer is still correct and short.
- **Recommended decoding (verbatim):** "We recommend setting `temperature` to `0.6`, `top_p` to `0.95` for reasoning True and greedy search for reasoning False, and increase `max_new_tokens` to `1024` or higher for reasoning True."
- **Evaluation mode (verbatim):** "We evaluated our model in **Reasoning-On** mode across all benchmarks, except RULER, which is evaluated in **Reasoning-Off** mode."
- **Architecture (verbatim):** "The model uses a hybrid architecture consisting primarily of Mamba-2 and MLP layers combined with just four Attention layers." "The model was trained using Megatron-LM and NeMo-RL."
- **Tool calling:** the template injects tools as `<AVAILABLE_TOOLS>[...]</AVAILABLE_TOOLS>`, asks for calls in `<TOOLCALL>[{"name": ..., "arguments": ...}]</TOOLCALL>`, and returns results as `<TOOL_RESPONSE>[...]</TOOL_RESPONSE>` inside a User turn. The vLLM example shows a `<think>` trace followed by a `calculate_tip` call with `{"bill_total": 100, "tip_percentage": 18}`.
- **Post-training data sources (Training datasets, verbatim):** "For several of the domains listed above we used synthetic data, specifically reasoning traces, from DeepSeek R1/R1-0528, Qwen3-235B-A22B, Nemotron 4 340B, Qwen2.5-32B-Instruct-AWQ, Qwen2.5-14B-Instruct, Qwen 2.5 72B."

## Definitions and terminology
- **`/think`**: keyword in the system or user message that turns reasoning on. Optional, because ON is the default. The template adds `<think>\n` to the start of the assistant turn.
- **`/no_think`**: keyword that turns reasoning off. The template adds `<think></think>` (an empty, closed thinking block) to the start of the assistant turn.
- **Turn-level reasoning control**: putting `/think` or `/no_think` in a user message instead of the system prompt. The last flag across messages wins.
- **Reasoning-On / Reasoning-Off mode**: the card's names for the two modes (used in the evaluation note).
- **`max_thinking_tokens`**: "a threshold that will attempt to end the reasoning trace at the next newline encountered in the reasoning trace. If no newline is encountered within 500 tokens, it will abruptly end the reasoning trace at `max_thinking_tokens + 500`."
- **`max_thinking_budget`**: the parameter name in the reference client code (default 512) for the same idea; see Inconsistencies.
- **`reasoning_content` / `content`**: the client's output fields for the thinking text and the final answer.
- **`<SPECIAL_10>`, `<SPECIAL_11>`, `<SPECIAL_12>`**: special tokens in the chat template. `<SPECIAL_10>System\n` opens the system turn, `<SPECIAL_11>User\n` / `<SPECIAL_11>Assistant\n` open user/assistant turns, `<SPECIAL_12>` ends an assistant turn (inferred from where the template emits them).
- **`--mamba_ssm_cache_dtype float32`**: vLLM flag the card says is required "for accurate quality".

## Evidence and examples
- **Benchmark Results (Reasoning On), Qwen3-8B vs NVIDIA-Nemotron-Nano-9B-v2:** AIME25 69.3% vs 72.1%; MATH500 96.3% vs 97.8%; GPQA 59.6% vs 64.0%; LCB 59.5% vs 71.1%; BFCL v3 66.3% vs 66.9%; IFEval (Instruction Strict) 89.4% vs 90.3%; HLE 4.4% vs 6.5%; RULER (128K) 74.1% vs 78.9% (RULER in Reasoning-Off). "All evaluations were done using NeMo-Skills." A reproduction tutorial is linked (https://nvidia.github.io/NeMo-Skills/tutorials/2025/08/22/reproducing-nvidia-nemotron-nano-9b-v2-evals/, not followed).
- **Budget-control client, call pattern** (from the code; the full code is under Raw):
  ```
  call 1: chat.completions(messages, max_tokens = max_thinking_budget)
          if "</think>" not in text:  text += ".\n</think>\n\n"
  call 2: messages += {"role": "assistant", "content": text}
          prompt = apply_chat_template(..., continue_final_message=True)
          completions(prompt, max_tokens = max_tokens - len(tokens(text)))
  ```
- **Deployment facts:** Transformers tested on 4.48.3 with `trust_remote_code=True`; vLLM `>=0.10.1`; Docker image `vllm/vllm-openai:v0.10.1` with `--max-model-len 131072`; TRT-LLM example with `max_seq_len=32678`; hardware A10G, H100-80GB, A100, Jetson AGX Thor; runtime engine "NeMo 25.07.nemotron-nano-v2". Context "up to 128K".
- **Data summary:** "Text Training Data Size: More than 10 Trillion Tokens"; "The model was pre-trained for approximately twenty trillion tokens"; English Common Crawl 3.360T tokens, Multilingual Common Crawl 812.7B, GitHub Crawl 747.4B. The long dataset tables (public, private, NVIDIA-sourced synthetic) are summarized, not reproduced; notable synthetic post-training sets: OpenMathReasoning from DeepSeek-R1-0528 (1.5M), OpenCodeReasoning from DeepSeek-R1-0528 (1.1M), Science from DeepSeek-R1-0528 (1.5M), ToolBench from Qwen3-235B-A22B (400K), LMSYS-Chat-1M from Qwen3-235B-A22B (1M), HelpSteer from Qwen3-235B-A22B (120K), safety from DeepSeek-R1-0528 (52K), Multilingual Reasoning (25M and 5M). These sample counts line up with the paper's Table 7 (Math 1.5M, Coding 1.1M, Science 2.0M, Tool-calling 400K) except Science (1.5M here vs 2.0M in the paper; the card's HLE set of 460K may account for part of the gap — unverified).
- **Model tree:** base model `nvidia/NVIDIA-Nemotron-Nano-12B-v2-Base` → finetuned `nvidia/NVIDIA-Nemotron-Nano-12B-v2` → this model (the pruned 9B).

## Inconsistencies / open questions
- [verified] **The card's own reference client does not implement the newline / +500 rule it describes.** The `max_thinking_tokens` text says the trace ends "at the next newline" or at `max_thinking_tokens + 500`. The `ThinkingBudgetClient` code stops the first call at exactly `max_tokens=max_thinking_budget` and, if `</think>` is missing, appends `".\n</think>\n\n"` right away. There is no newline wait and no 500-token grace window in the code. The example output shows this: the trace ends mid-sentence ("That's a basic."). Checked by reading the description against the code in `page.md`. The paper's §3.4 describes the newline rule as what "the inference setup" does, so the client is a simplified version.
- [verified] **Two names for the budget parameter.** The description says `max_thinking_tokens`; the client code uses `max_thinking_budget`. Checked in `page.md`.
- [verified] **The prose says `/no_think` is detected only "in the system prompt"; the template also detects it in user messages.** The template's loop checks `message['role'] == 'user' or message['role'] == 'system'` for both keywords, and the Transformers note says both keywords "can also be provided in “user” messages". Checked by reading the Jinja template in `page.md`.
- [verified] **The client's `.strip("</think>")` strips a character set, not the tag.** In Python, `str.strip("</think>")` removes any of the characters `<`, `/`, `t`, `h`, `i`, `n`, `k`, `>` from both ends. A trace that starts "this is thin" comes back as "s is thin". Checked by running the expression in Python 3; the card's own example output is reproduced exactly, so the bug does not show there. A cosmetic code defect, not a model property; relevant only if the code is shown on a slide.
- [verified] **Two different language lists on the same card.** Model Overview: "English, German, Spanish, French, Italian, and Japanese" (6). Input: "German, Spanish, French, Italian, Korean, Portuguese, Russian, Japanese, Chinese and English" (10). Use Case: English plus "German, French, Italian, Spanish and Japanese". Checked in `page.md`.
- [verified] **Data freshness conflicts with the data listed.** The card says "Data Freshness: September 2024" and "The pretraining data has a cutoff date of September 2024", but the same card lists Common Crawl snapshots "CC-MAIN-2013-20 through CC-MAIN-2025-13" and multilingual snapshots up to "CC-MAIN-2025-18", and the paper (`nvidia-2025-nemotron-nano-2.web.md`, §2.2.1) says "we used data from CC-NEWS through April 23, 2025, to help improve the knowledge cutoff of the model". Checked in both `page.md` files.
- [verified] **Two training-size statements.** "Text Training Data Size: More than 10 Trillion Tokens" and "The model was pre-trained for approximately twenty trillion tokens" (paper: 20T). Compatible in the strict sense, but a slide should quote 20T. Checked in `page.md`.
- [verified] **Card benchmark numbers are for the 9B; the paper's Table 8 is for the 12B.** E.g. AIME25 72.1% (9B, card) vs 76.25 (12B, paper). The Qwen3-8B columns agree after rounding (69.3 vs 69.31; 59.6 vs 59.61). Do not mix the two. Checked against Table 8 in the paper record.
- [open question] **The card does not say how the switch or the budget were trained.** Nothing on the card mentions reasoning-stripped SFT samples or truncated traces (checked by reading the full `page.md`). Those facts come only from the paper (Stage 1 SFT ~10% stripped; Stage 3 SFT traces truncated to 1–2k tokens; GRPO/RLHF with and without traces). Whether the training data used the literal `/think` / `/no_think` strings and the `<think></think>` form is not documented anywhere in either source; settled by inspecting Nemotron-Post-Training-Dataset-v1/v2.
- [open question] **Is the empty-`<think></think>` form in the template the same form as the "empty" traces in training?** It is the natural reading (the paper's Stage 1 "empty" traces, the template's `<think></think>`), but neither source says so. Settled by the released post-training data.
- [open question] **Is `/no_think` in a user message fully equivalent to the system prompt?** The template treats them the same (last flag wins), but the card evaluates and documents mainly the system-prompt form. Settled by testing or by the ThinkFollow-style evaluation, which this card does not report.
- [open question] **"slight decrease in accuracy for harder prompts" with reasoning off is not quantified.** The card gives no Reasoning-Off accuracy numbers (only RULER is run in that mode). Settled by the NeMo-Skills reproduction tutorial or NVIDIA.
- [open question] **"Improved using Qwen."** appears as a bare sentence after the language list. It probably reflects the Qwen3-235B-A22B-generated training data (a license-style attribution), but the card does not explain it. Settled by NVIDIA.
- [open question] **The Transformers snippet uses `max_new_tokens=32`**, while the card recommends "`1024` or higher for reasoning True". With reasoning on, 32 tokens would usually end inside the trace. Presumably a placeholder; settled by running it.

## Images / diagrams
### `nvidia-nemotron-nano-9b-v2-card.web/images/acc-vs-budget.png`
- Provenance: web asset `web/nvidia-nemotron-nano-9b-v2-card/assets/acc-vs-budget.png` (PNG image data, 3564 x 2363, RGB), from https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2/resolve/main/acc-vs-budget.png. No alt text and no caption. It is the only content of the card's "Reasoning Budget Control" section, right after "During inference, the user can specify how many tokens the model is allowed to "think"." The filename suggests accuracy vs thinking budget; which benchmarks and budgets it shows is not stated in the text.
- Depiction: <!-- pending: process_images -->
- Why it matters: <!-- pending: process_images -->
- Transcribed text: <!-- pending: process_images -->

### Dropped (not copied)
- `accuracy_chart.png` (PNG, 2460 x 1030, RGBA), from https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2/resolve/main/accuracy_chart.png. The unlabelled chart at the top of the card, under the model title. Dropped because the caller limited this pass to reasoning-budget images; its numbers appear to correspond to the "Benchmark Results (Reasoning On)" table transcribed under Evidence (not verified against the image). Bytes remain in the raw asset folder.
- `Vs5FPVCH-VZBipV3qKTuy.png`: the NVIDIA organization avatar (WebP despite the `.png` name, 200 x 200, under 300 px). Site chrome, referenced 5 times on the page.
- `huggingface_logo-noborder.svg`: the Hugging Face logo (95 x 88). Site chrome.

## Raw / preserved excerpts
### Header facts
"Model Developer: NVIDIA Corporation. Model Dates: June 2025 - August 2025. Data Freshness: September 2024. The pretraining data has a cutoff date of September 2024."

### Model Overview (full)
"NVIDIA-Nemotron-Nano-9B-v2 is a large language model (LLM) trained from scratch by NVIDIA, and designed as a unified model for both reasoning and non-reasoning tasks. It responds to user queries and tasks by first generating a reasoning trace and then concluding with a final response. The model's reasoning capabilities can be controlled via a system prompt. If the user prefers the model to provide its final answer without intermediate reasoning traces, it can be configured to do so, albeit with a slight decrease in accuracy for harder prompts that require reasoning. Conversely, allowing the model to generate reasoning traces first generally results in higher-quality final solutions to queries and tasks.

The model uses a hybrid architecture consisting primarily of Mamba-2 and MLP layers combined with just four Attention layers. For the architecture, please refer to the Nemotron-H tech report. The model was trained using Megatron-LM and NeMo-RL.

The supported languages include: English, German, Spanish, French, Italian, and Japanese. Improved using Qwen.

This model is ready for commercial use."

### Evaluation Results
"We evaluated our model in **Reasoning-On** mode across all benchmarks, except RULER, which is evaluated in **Reasoning-Off** mode."

### Reasoning Budget Control (full section)
"This model supports runtime “thinking” budget control. During inference, the user can specify how many tokens the model is allowed to "think"."
[image: acc-vs-budget.png]

### Use it with Transformers (reasoning switch, verbatim)
```
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("nvidia/NVIDIA-Nemotron-Nano-9B-v2")
model = AutoModelForCausalLM.from_pretrained(
    "nvidia/NVIDIA-Nemotron-Nano-9B-v2",
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto"
)
```

Case 1: `/think` or no reasoning signal is provided in the system prompt, reasoning will be set to `True`

```
messages = [
    {"role": "system", "content": "/think"},
    {"role": "user", "content": "Write a haiku about GPUs"},
]
```

Case 2: `/no_think` is provided, reasoning will be set to `False`

```
messages = [
    {"role": "system", "content": "/no_think"},
    {"role": "user", "content": "Write a haiku about GPUs"},
]
```

Note: `/think` or `/no_think` keywords can also be provided in “user” messages for turn-level reasoning control.

The rest of the inference snippet remains the same

```
tokenized_chat = tokenizer.apply_chat_template(
    messages,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

outputs = model.generate(
    tokenized_chat,
    max_new_tokens=32,
    eos_token_id=tokenizer.eos_token_id
)
print(tokenizer.decode(outputs[0]))
```

We recommend setting `temperature` to `0.6`, `top_p` to `0.95` for reasoning True and greedy search for reasoning False, and increase `max_new_tokens` to `1024` or higher for reasoning True.

### Using Budget Control with a vLLM Server (full section, verbatim)
The thinking budget allows developers to keep accuracy high and meet response‑time targets - which is especially crucial for customer support, autonomous agent steps, and edge devices where every millisecond counts.

With budget control, you can set a limit for internal reasoning:

- `max_thinking_tokens`: This is a threshold that will attempt to end the reasoning trace at the next newline encountered in the reasoning trace. If no newline is encountered within 500 tokens, it will abruptly end the reasoning trace at `max_thinking_tokens + 500`.

Start a vLLM server:

```
vllm serve nvidia/NVIDIA-Nemotron-Nano-9B-v2 \
    --trust-remote-code \
    --mamba_ssm_cache_dtype float32
```

Client for supporting budget control:

```
from typing import Any, Dict, List

import openai
from transformers import AutoTokenizer

class ThinkingBudgetClient:
   def __init__(self, base_url: str, api_key: str, tokenizer_name_or_path: str):
       self.base_url = base_url
       self.api_key = api_key
       self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name_or_path)
       self.client = openai.OpenAI(base_url=self.base_url, api_key=self.api_key)

   def chat_completion(
       self,
       model: str,
       messages: List[Dict[str, Any]],
       max_thinking_budget: int = 512,
       max_tokens: int = 1024,
       **kwargs,
   ) -> Dict[str, Any]:
       assert (
           max_tokens > max_thinking_budget
       ), f"thinking budget must be smaller than maximum new tokens. Given {max_tokens=} and {max_thinking_budget=}"

       # 1. first call chat completion to get reasoning content
       response = self.client.chat.completions.create(
           model=model, messages=messages, max_tokens=max_thinking_budget, **kwargs
       )
       content = response.choices[0].message.content

       reasoning_content = content
       if not "</think>" in reasoning_content:
           # reasoning content is too long, closed with a period (.)
           reasoning_content = f"{reasoning_content}.\n</think>\n\n"
       reasoning_tokens_len = len(
           self.tokenizer.encode(reasoning_content, add_special_tokens=False)
       )
       remaining_tokens = max_tokens - reasoning_tokens_len
       assert (
           remaining_tokens > 0
       ), f"remaining tokens must be positive. Given {remaining_tokens=}. Increase the max_tokens or lower the max_thinking_budget."

       # 2. append reasoning content to messages and call completion
       messages.append({"role": "assistant", "content": reasoning_content})
       prompt = self.tokenizer.apply_chat_template(
           messages,
           tokenize=False,
           continue_final_message=True,
       )
       response = self.client.completions.create(
           model=model, prompt=prompt, max_tokens=remaining_tokens, **kwargs
       )

       response_data = {
           "reasoning_content": reasoning_content.strip().strip("</think>").strip(),
           "content": response.choices[0].text,
           "finish_reason": response.choices[0].finish_reason,
       }
       return response_data
```

Calling the server with a budget (Restricted to 32 tokens here as an example)

```
tokenizer_name_or_path = "nvidia/NVIDIA-Nemotron-Nano-9B-v2"
client = ThinkingBudgetClient(
   base_url="http://localhost:8000/v1",  # Nano 9B v2 deployed in thinking mode
   api_key="EMPTY",
   tokenizer_name_or_path=tokenizer_name_or_path,
)

result = client.chat_completion(
   model="nvidia/NVIDIA-Nemotron-Nano-9B-v2",
   messages=[
       {"role": "system", "content": "You are a helpful assistant. /think"},
       {"role": "user", "content": "What is 2+2?"},
   ],
   max_thinking_budget=32,
   max_tokens=512,
   temperature=0.6,
   top_p=0.95,
)
print(result)
```

You should see output similar to the following:

```
{'reasoning_content': "Okay, the user asked, What is 2+2? Let me think. Well, 2 plus 2 equals 4. That's a basic.", 'content': '2 + 2 equals **4**.\n', 'finish_reason': 'stop'}
```

### Tool-calling example output (verbatim)
```
<think>
Okay, let's see. The user has a bill of $100 and wants to know the amount for an 18% tip. Hmm, I need to calculate the tip based on the bill total and the percentage. The tools provided include calculate_tip, which takes bill_total and tip_percentage as parameters. So the bill_total here is 100, and the tip_percentage is 18. I should call the calculate_tip function with these values. Wait, do I need to check if the parameters are integers? The bill is $100, which is an integer, and 18% is also an integer. So that fits the function's requirements. I don't need to convert any currency here because the user is asking about a tip in the same currency. So the correct tool to use is calculate_tip with those parameters.
</think>

[ChatCompletionMessageToolCall(id='chatcmpl-tool-e341c6954d2c48c2a0e9071c7bdefd8b', function=Function(arguments='{"bill_total": 100, "tip_percentage": 18}', name='calculate_tip'), type='function')]
```
(Server launched with `--enable-auto-tool-choice --tool-parser-plugin "NVIDIA-Nemotron-Nano-9B-v2/nemotron_toolcall_parser_no_streaming.py" --tool-call-parser "nemotron_json"`; request with tools `calculate_tip` and `convert_currency`, empty system message, user "My bill is $100. What will be the amount for 18% tip?", `temperature=0.6, top_p=0.95, max_tokens=32768`.)

### Prompt Format (full, verbatim)
We follow the jinja chat template provided below. This template conditionally adds `<think>\n` to the start of the Assistant response if `/think` is found in either the system prompt or any user message. If no reasoning signal is added, the model defaults to reasoning "on" mode. The chat template adds `<think></think>` to the start of the Assistant response if `/no_think` is found in the system prompt. Thus enforcing reasoning on/off behavior.

```
{%- set ns = namespace(enable_thinking = true) %}

{%- for message in messages -%}
    {%- set content = message['content'] -%}
    {%- if message['role'] == 'user' or message['role'] == 'system' -%}
        {%- if '/think' in content -%}
            {%- set ns.enable_thinking = true -%}
        {%- elif '/no_think' in content -%}
            {%- set ns.enable_thinking = false -%}
        {%- endif -%}
    {%- endif -%}
{%- endfor -%}

{%- if messages[0]['role'] != 'system' -%}
    {%- set ns.non_tool_system_content = '' -%}
    {{- '<SPECIAL_10>System\n' -}}
{%- else -%}
    {%- set ns.non_tool_system_content = messages[0]['content']
        .replace('/think', '')
        .replace('/no_think', '')
        .strip()
    -%}
    {{- '<SPECIAL_10>System\n' + ns.non_tool_system_content }}
{%- endif -%}

{%- if tools -%}
    {%- if ns.non_tool_system_content is defined and ns.non_tool_system_content != '' -%}
        {{- '\n\n' -}}
    {%- endif -%}

    {{- 'You can use the following tools to assist the user if required:' -}}
    {{- '\n<AVAILABLE_TOOLS>[' -}}
    {%- for tool in tools -%}
        {{- (tool.function if tool.function is defined else tool) | tojson -}}
        {{- ', ' if not loop.last else '' -}}
    {%- endfor -%}
    {{- ']</AVAILABLE_TOOLS>\n\n' -}}

    {{- 'If you decide to call any tool(s), use the following format:\n' -}}
    {{- '<TOOLCALL>[{{"name": "tool_name1", "arguments": "tool_args1"}}, ' -}}
    {{- '{{"name": "tool_name2", "arguments": "tool_args2"}}]</TOOLCALL>\n\n' -}}

    {{- 'The user will execute tool-calls and return responses from tool(s) in this format:\n' -}}
    {{- '<TOOL_RESPONSE>[{{"tool_response1"}}, {{"tool_response2"}}]</TOOL_RESPONSE>\n\n' -}}

    {{- 'Based on the tool responses, you can call additional tools if needed, correct tool calls if any errors are found, or just respond to the user.' -}}
{%- endif -%}

{{- '\n' -}}

{%- set messages = messages[1:] if messages[0]['role'] == 'system' else messages -%}

{%- if messages[-1]['role'] == 'assistant' -%}
    {%- set ns.last_turn_assistant_content = messages[-1]['content'].strip() -%}
    {%- set messages = messages[:-1] -%}
{%- endif -%}

{%- for message in messages -%}
    {%- set content = message['content'] -%}

    {%- if message['role'] == 'user' -%}
        {{- '<SPECIAL_11>User\n' + content.replace('/think', '').replace('/no_think', '').strip() + '\n' }}

    {%- elif message['role'] == 'tool' -%}
        {%- if loop.first or (messages[loop.index0 - 1].role != 'tool') -%}
            {{- '<SPECIAL_11>User\n' + '<TOOL_RESPONSE>[' }}
        {%- endif -%}
        {{- message['content'] -}}
        {{- ', ' if not loop.last and (messages[loop.index0 + 1].role == 'tool') else '' -}}
        {%- if loop.last or (messages[loop.index0 + 1].role != 'tool') -%}
            {{- ']</TOOL_RESPONSE>\n' -}}
        {%- endif -%}

    {%- elif message['role'] == 'assistant' -%}
        {%- if '</think>' in content -%}
            {%- set content = content.split('</think>')[1].strip() %}
        {%- endif -%}

        {{- '<SPECIAL_11>Assistant\n' + content.strip() }}

        {%- if message.tool_calls -%}
            {%- if content.strip() != '' -%}
                {{- '\n\n' -}}
            {%- endif -%}
            {{- '<TOOLCALL>[' -}}
            {%- for call in message.tool_calls -%}
                {%- set fn = call.function if call.function is defined else call -%}
                {{- '{"name": "' + fn.name + '", "arguments": ' -}}
                {%- if fn.arguments is string -%}
                    {{- fn.arguments -}}
                {%- else -%}
                    {{- fn.arguments | tojson -}}
                {%- endif -%}
                {{- '}' + (', ' if not loop.last else '') -}}
            {%- endfor -%}
            {{- ']</TOOLCALL>' -}}
        {%- endif -%}

        {{- '\n<SPECIAL_12>\n' -}}
    {%- endif -%}
{%- endfor -%}

{%- if add_generation_prompt -%}
    {{- '<SPECIAL_11>Assistant\n' -}}
    {%- if ns.enable_thinking is defined and ns.enable_thinking is false -%}
        {{- '<think></think>' -}}
    {%- else -%}
        {{- '<think>\n' -}}
    {%- endif -%}
    {%- if ns.last_turn_assistant_content is defined and ns.last_turn_assistant_content != '' -%}
        {{- ns.last_turn_assistant_content -}}
    {%- endif -%}

{%- else -%}
    {%- if ns.last_turn_assistant_content is defined and ns.last_turn_assistant_content != '' -%}
        {{- '<SPECIAL_11>Assistant\n' -}}
        {%- if ns.enable_thinking is defined and ns.enable_thinking is false -%}
            {{- '<think></think>' -}}
        {%- else -%}
            {{- '<think>\n' -}}
        {%- endif -%}
        {{- ns.last_turn_assistant_content -}}

        {%- if continue_final_message is defined -%}
            {%- if continue_final_message is false -%}
                {{- '\n<SPECIAL_12>\n' -}}
            {%- endif -%}
        {%- else -%}
            {{- '\n<SPECIAL_12>\n' -}}
        {%- endif -%}
    {%- endif -%}
{%- endif -%}
```

### Training datasets (properties, verbatim)
"**Properties:** The post-training corpus for NVIDIA-Nemotron-Nano-9B-v2 consists of English and multilingual text (German, Spanish, French, Italian, Korean, Portuguese, Russian, Japanese, Chinese and English). Our sources cover a variety of document types such as: webpages, dialogue, articles, and other written materials. The corpus spans domains including code, legal, math, science, finance, and more. We also include a small portion of question-answering, and alignment style data to improve model accuracies. For several of the domains listed above we used synthetic data, specifically reasoning traces, from DeepSeek R1/R1-0528, Qwen3-235B-A22B, Nemotron 4 340B, Qwen2.5-32B-Instruct-AWQ, Qwen2.5-14B-Instruct, Qwen 2.5 72B.

The pre-training corpus for NVIDIA-Nemotron-Nano-9B-v2 consists of high-quality curated and synthetically-generated data. It is trained in the English language, as well as 15 multilingual languages and 43 programming languages. Our sources cover a variety of document types such as: webpages, dialogue, articles, and other written materials. The corpus spans domains including legal, math, science, finance, and more. We also include a small portion of question-answering, and alignment style data to improve model accuracy. The model was pre-trained for approximately twenty trillion tokens."
