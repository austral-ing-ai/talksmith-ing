---
source_file: hf-chat-templates-tools
source_type: web-capture
ingested_at: 2026-09-27
---

# Expanding Chat Templates with Tools and Documents (Hugging Face Transformers docs)

## Provenance
- Original location: web/hf-chat-templates-tools/ (text from `page.md`; `page.md` is 17779 chars with 16 heading lines, so no `original.html` fallback was needed.)
- Format: html (web capture via talksmith:ingest of a Hugging Face doc-builder page)
- URL: https://huggingface.co/docs/transformers/main/en/chat_template_tools_and_documents
- Captured at: 2026-09-27T18:17:17Z (HTTP 200, 283521 bytes)
- Page title: Expanding Chat Templates with Tools and Documents · Hugging Face
- Author / source (if known): Hugging Face (official Transformers documentation; source file `docs/source/en/chat_template_tools_and_documents.md` in `github.com/huggingface/transformers`). This is **library documentation**: Hugging Face describing its own `apply_chat_template` API. Not an independent source.
- Date of original (if known): Not printed on the page. The capture is the `main` docs version; the banner says the latest stable is v5.17.0. Treat it as the live state on 2026-09-27. Docs captured 2026-09-27. The example model is described as top-performing "at the time of writing", which suggests the text is older than the capture.
- Images: the capture carried 1 SVG asset, `huggingface_logo-noborder.svg` (the Hugging Face site logo, 95 x 88 px per its `width`/`height` attributes; referenced twice, deduped by the capture). It is below the Talk's 300 px threshold on both sides, so it was not kept in the companion folder and there is no stub for it. The raw copy under `web/hf-chat-templates-tools/assets/` was left untouched. The companion folder `hf-chat-templates-tools.web/images/` is empty.

## Key claims
Relevance for the Talk: this page describes the **chat template** component of a serving stack from the library side: how tool definitions become JSON schema text the model sees, and how tool calls and tool results are written back into the conversation and re-rendered.

- **Any keyword argument reaches the template:** "The only argument that `apply_chat_template` requires is `messages`. However, you can pass any keyword argument to `apply_chat_template` and it will be accessible inside the template."
- **Recommended convention across models:** "We encourage model authors to make their chat templates compatible with this format, to make it easy to transfer tool-calling code between models."
- **Tools are passed as Python functions:** "When passing tools to a tool-use model, you can simply pass a list of functions to the `tools` argument", e.g. `tokenizer.apply_chat_template(messages, tools=tools)`.
- **Functions are converted to JSON schema, then passed to the template (verbatim, core quote):** "Each function you pass to the `tools` argument of `apply_chat_template` is converted into a JSON schema. These schemas are then passed to the model chat template. In other words, tool-use models do not see your functions directly, and they never see the actual code inside them. What they care about is the function **definitions** and the **arguments** they need to pass to them - they care about what the tools do and how to use them, not how they work! It is up to you to read their outputs, detect if they have requested to use a tool, pass their arguments to the tool function, and return the response in the chat."
- **Rules for a parseable function:** "descriptive name"; "Every argument must have a type hint"; "docstring in the standard Google style" with an `Args:` block; "Do not include types in the `Args:` block"; return type and `Returns:` "are optional because most tool-use models ignore them."
- **The four steps when the model calls a tool (verbatim):** "1. Parse the model’s output to get the tool name(s) and arguments. 2. Add the model’s tool call(s) to the conversation. 3. Call the corresponding function(s) with those arguments. 4. Add the result(s) to the conversation"
- **Raw model output is model-specific; parsing is on you:** "The output format above is specific to the `Hermes-2-Pro` model we’re using in this example. Other models may emit different tool call formats, and you may need to do some manual parsing at this step. For example, `Llama-3.1` models will emit slightly different JSON, with `parameters` instead of `arguments`. Regardless of the format the model outputs, you should add the tool call to the conversation in the format below, with `tool_calls`, `function` and `arguments` keys."
- **Tool call is appended as an assistant message:** `messages.append({"role": "assistant", "tool_calls": [{"type": "function", "function": tool_call}]})`.
- **dict vs JSON string (difference from OpenAI):** "If you’re familiar with the OpenAI API, you should pay attention to an important difference here - the `tool_call` is a dict, but in the OpenAI API it’s a JSON string. Passing a string may cause errors or strange model behaviour!"
- **Tool result is appended as a `tool` message:** `messages.append({"role": "tool", "name": "get_current_temperature", "content": "22.0"})`.
- **Mistral/Mixtral need IDs:** "Some model architectures, notably Mistral/Mixtral, also require a `tool_call_id` here, which should be 9 randomly-generated alphanumeric characters, and assigned to the `id` key of the tool call dictionary. The same key should also be assigned to the `tool_call_id` key of the tool response dictionary below, so that tool calls can be matched to tool responses."
- **Re-render and generate again:** "Finally, let’s let the assistant read the function outputs and continue chatting with the user:" followed by the same `apply_chat_template(messages, tools=tools, add_generation_prompt=True, ...)` + `model.generate(...)` call. Output: "The current temperature in Paris, France is 22.0 ° Celsius.<|im_end|>".
- **Schemas can be written by hand:** "JSON schemas can be passed directly to the `tools` argument of `apply_chat_template`". Warning: "the more complex your schemas, the more likely the model is to get confused when dealing with them! We recommend simple function signatures where possible".
- **RAG `documents` argument:** each document "a single dict with `title` and `contents` keys". "The `documents` input for retrieval-augmented generation is not widely supported, and many models have chat templates which simply ignore this input." Supported by Cohere Command-R / Command-R+ via their `rag` template.

## Definitions and terminology
- **`apply_chat_template`**: tokenizer method that renders `messages` (plus extra kwargs such as `tools`, `documents`) through the model's Jinja chat template into prompt text or token ids.
- **Chat template**: the model-specific template that turns messages, tools and documents into the model's prompt format.
- **Tool use / function calling**: "“Tool use” LLMs can choose to call functions as external tools before generating an answer."
- **JSON schema (tool schema)**: the `{"type": "function", "function": {"name", "description", "parameters": {"type": "object", "properties", "required"}}}` form each tool is converted to.
- **`get_json_schema`**: `transformers.utils` helper that converts a Python function to that schema.
- **`tool_calls`**: key on the assistant message holding `[{"type": "function", "function": {"name", "arguments"}}]`; `arguments` is a dict here.
- **`tool` role**: message carrying a tool result; keys `name`, `content` (and `tool_call_id` for Mistral/Mixtral).
- **`tool_call_id`**: ID linking a tool response to its call; needed by Mistral/Mixtral templates.
- **`add_generation_prompt=True`**: appends the assistant-turn opener so the model generates a reply.
- **`documents`**: recommended RAG kwarg; list of dicts with `title` and `contents`.

## Evidence and examples
- **Worked example model:** `NousResearch/Hermes-2-Pro-Llama-3-8B` ("one of the highest-performing tool-use models in its size category at the time of writing"). Alternatives named: Command-R, Mixtral-8x22B.
- **Raw generated text containing the call (verbatim):**
  ```
  <tool_call>
  {"arguments": {"location": "Paris, France", "unit": "celsius"}, "name": "get_current_temperature"}
  </tool_call><|im_end|>
  ```
  Commentary: "The model has called the function with valid arguments, in the format requested by the function docstring. It has inferred that we’re most likely referring to the Paris in France, and it remembered that, as the home of SI units, the temperature in France should certainly be displayed in Celsius."
- **Full loop in code (verbatim core):**
  ```
  inputs = tokenizer.apply_chat_template(messages, tools=tools, add_generation_prompt=True, return_dict=True, return_tensors="pt")
  inputs = {k: v.to(model.device) for k, v in inputs.items()}
  out = model.generate(**inputs, max_new_tokens=128)
  print(tokenizer.decode(out[0][len(inputs["input_ids"][0]):]))
  ...
  tool_call = {"name": "get_current_temperature", "arguments": {"location": "Paris, France", "unit": "celsius"}}
  messages.append({"role": "assistant", "tool_calls": [{"type": "function", "function": tool_call}]})
  messages.append({"role": "tool", "name": "get_current_temperature", "content": "22.0"})
  # then apply_chat_template + generate again
  ```
  Final output: `The current temperature in Paris, France is 22.0 ° Celsius.<|im_end|>`.
- **`get_json_schema(multiply)` output (verbatim):**
  ```
  {
    "type": "function", 
    "function": {
      "name": "multiply", 
      "description": "A function that multiplies two numbers", 
      "parameters": {
        "type": "object", 
        "properties": {
          "a": {
            "type": "number", 
            "description": "The first number to multiply"
          }, 
          "b": {
            "type": "number",
            "description": "The second number to multiply"
          }
        }, 
        "required": ["a", "b"]
      }
    }
  }
  ```
  The Python `float` type hint becomes JSON `"number"`; docstring `Args:` lines become `description`s; both arguments land in `required`.
- **In the example, the tool call is re-typed by hand** (`tool_call = {...}` literal), not parsed from the model output in code. The page gives no parsing code.

## Inconsistencies / open questions
- [verified] The first code example does `import datetime` and then calls `datetime.now()`, which raises `AttributeError` (the module needs `datetime.datetime.now()` or `from datetime import datetime`). Check: Python semantics of the `datetime` module applied to the code in `page.md`. Only matters if the snippet is shown on a slide.
- [verified] The RAG prose says each document has "`title` and `contents` keys", but the code example uses `"title"` and `"text"`. Check: `page.md`. Which key the Command-R `rag` template reads is an [open question], settled by reading that template.
- [verified] The page never shows code that parses the model's raw output into a tool call; step 1 "Parse the model’s output" is left to the reader, and the example hard-codes the parsed dict. Check: `page.md`. For a serving-platform slide this is the gap a server-side tool-call parser (e.g. vLLM's `--tool-call-parser`, sibling record `vllm-tool-calling.web.md`) fills.
- [open question] Mistral `tool_call_id` format: "9 randomly-generated alphanumeric characters" here vs "exactly 9 digits" in `vllm-tool-calling.web.md`. Settled by Mistral's chat template in `tokenizer_config.json`.
- [verified] "`Llama-3.1` models will emit slightly different JSON, with `parameters` instead of `arguments`" is consistent with Meta's own format doc. Check: the sibling record `meta-llama3-1-prompt-format.web.md` shows the Llama 3.1 JSON custom-tool response as `<|python_tag|>{"type": "function", "name": "trending_songs", "parameters": {"n": "10", "genre": "all"}}<|eom_id|>`. Librarian's inference, not stated by either source: a server-side parser that returns the OpenAI shape has to map this `parameters` key to `arguments`.
- [open question] The example model is described as top in its size class "at the time of writing"; that ranking is dated and was not checked. Not needed for the slide's mechanism.

## Images / diagrams
None retained. The one captured asset (`huggingface_logo-noborder.svg`, the Hugging Face site logo, 95 x 88 px) was below the 300 px threshold on both sides and was not copied, per the Talk's instruction. The companion folder `hf-chat-templates-tools.web/images/` is empty.

## Raw / preserved excerpts
The complete article body as captured in `page.md` (from the H1 "Expanding Chat Templates with Tools and Documents" to the end), with the site header, docs navigation, version list, sign-up banner, "Copied" button labels, `<#anchor>` heading markup and the trailing "Update on GitHub" / "Transformers→" links removed. Headings are demoted by two levels. Code blocks are verbatim.

### Expanding Chat Templates with Tools and Documents

The only argument that `apply_chat_template` requires is `messages`. However, you can pass any keyword argument to `apply_chat_template` and it will be accessible inside the template. This gives you a lot of freedom to use chat templates for many things. There are no restrictions on the names or the format of these arguments - you can pass strings, lists, dicts or whatever else you want.

That said, there are some common use-cases for these extra arguments, such as passing tools for function calling, or documents for retrieval-augmented generation. In these common cases, we have some opinionated recommendations about what the names and formats of these arguments should be, which are described in the sections below. We encourage model authors to make their chat templates compatible with this format, to make it easy to transfer tool-calling code between models.

#### Tool use / function calling

“Tool use” LLMs can choose to call functions as external tools before generating an answer. When passing tools to a tool-use model, you can simply pass a list of functions to the `tools` argument:

```
import datetime

def current_time():
    """Get the current local time as a string."""
    return str(datetime.now())

def multiply(a: float, b: float):
    """
    A function that multiplies two numbers
    
    Args:
        a: The first number to multiply
        b: The second number to multiply
    """
    return a * b

tools = [current_time, multiply]

model_input = tokenizer.apply_chat_template(
    messages,
    tools=tools
)
```

In order for this to work correctly, you should write your functions in the format above, so that they can be parsed correctly as tools. Specifically, you should follow these rules:

- The function should have a descriptive name 
- Every argument must have a type hint 
- The function must have a docstring in the standard Google style (in other words, an initial function description  
 followed by an `Args:` block that describes the arguments, unless the function does not have any arguments.) 
- Do not include types in the `Args:` block. In other words, write `a: The first number to multiply`, not `a (int): The first number to multiply`. Type hints should go in the function header instead. 
- The function can have a return type and a `Returns:` block in the docstring. However, these are optional because most tool-use models ignore them.

##### Passing tool results to the model

The sample code above is enough to list the available tools for your model, but what happens if it wants to actually use one? If that happens, you should:

1. Parse the model’s output to get the tool name(s) and arguments. 
2. Add the model’s tool call(s) to the conversation. 
3. Call the corresponding function(s) with those arguments. 
4. Add the result(s) to the conversation

##### A complete tool use example

Let’s walk through a tool use example, step by step. For this example, we will use an 8B `Hermes-2-Pro` model, as it is one of the highest-performing tool-use models in its size category at the time of writing. If you have the memory, you can consider using a larger model instead like [Command-R](https://huggingface.co/CohereForAI/c4ai-command-r-v01) or [Mixtral-8x22B](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1), both of which also support tool use and offer even stronger performance.

First, let’s load our model and tokenizer:

```
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "NousResearch/Hermes-2-Pro-Llama-3-8B"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint, torch_dtype=torch.bfloat16, device_map="auto")
```

Next, let’s define a list of tools:

```
def get_current_temperature(location: str, unit: str) -> float:
    """
    Get the current temperature at a location.
    
    Args:
        location: The location to get the temperature for, in the format "City, Country"
        unit: The unit to return the temperature in. (choices: ["celsius", "fahrenheit"])
    Returns:
        The current temperature at the specified location in the specified units, as a float.
    """
    return 22.  # A real function should probably actually get the temperature!

def get_current_wind_speed(location: str) -> float:
    """
    Get the current wind speed in km/h at a given location.
    
    Args:
        location: The location to get the temperature for, in the format "City, Country"
    Returns:
        The current wind speed at the given location in km/h, as a float.
    """
    return 6.  # A real function should probably actually get the wind speed!

tools = [get_current_temperature, get_current_wind_speed]
```

Now, let’s set up a conversation for our bot:

```
messages = [
  {"role": "system", "content": "You are a bot that responds to weather queries. You should reply with the unit used in the queried location."},
  {"role": "user", "content": "Hey, what's the temperature in Paris right now?"}
]
```

Now, let’s apply the chat template and generate a response:

```
inputs = tokenizer.apply_chat_template(messages, tools=tools, add_generation_prompt=True, return_dict=True, return_tensors="pt")
inputs = {k: v.to(model.device) for k, v in inputs.items()}
out = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(out[0][len(inputs["input_ids"][0]):]))
```

And we get:

```
<tool_call>
{"arguments": {"location": "Paris, France", "unit": "celsius"}, "name": "get_current_temperature"}
</tool_call><|im_end|>
```

The model has called the function with valid arguments, in the format requested by the function docstring. It has inferred that we’re most likely referring to the Paris in France, and it remembered that, as the home of SI units, the temperature in France should certainly be displayed in Celsius.

The output format above is specific to the `Hermes-2-Pro` model we’re using in this example. Other models may emit different tool call formats, and you may need to do some manual parsing at this step. For example, `Llama-3.1` models will emit slightly different JSON, with `parameters` instead of `arguments`. Regardless of the format the model outputs, you should add the tool call to the conversation in the format below, with `tool_calls`, `function` and `arguments` keys.

Next, let’s append the model’s tool call to the conversation.

```
tool_call = {"name": "get_current_temperature", "arguments": {"location": "Paris, France", "unit": "celsius"}}
messages.append({"role": "assistant", "tool_calls": [{"type": "function", "function": tool_call}]})
```

If you’re familiar with the OpenAI API, you should pay attention to an important difference here - the `tool_call` is a dict, but in the OpenAI API it’s a JSON string. Passing a string may cause errors or strange model behaviour!

Now that we’ve added the tool call to the conversation, we can call the function and append the result to the conversation. Since we’re just using a dummy function for this example that always returns 22.0, we can just append that result directly.

```
messages.append({"role": "tool", "name": "get_current_temperature", "content": "22.0"})
```

Some model architectures, notably Mistral/Mixtral, also require a `tool_call_id` here, which should be 9 randomly-generated alphanumeric characters, and assigned to the `id` key of the tool call dictionary. The same key should also be assigned to the `tool_call_id` key of the tool response dictionary below, so that tool calls can be matched to tool responses. So, for Mistral/Mixtral models, the code above would be:

```
tool_call_id = "9Ae3bDc2F"  # Random ID, 9 alphanumeric characters
tool_call = {"name": "get_current_temperature", "arguments": {"location": "Paris, France", "unit": "celsius"}}
messages.append({"role": "assistant", "tool_calls": [{"type": "function", "id": tool_call_id, "function": tool_call}]})
```

and

```
messages.append({"role": "tool", "tool_call_id": tool_call_id, "name": "get_current_temperature", "content": "22.0"})
```

Finally, let’s let the assistant read the function outputs and continue chatting with the user:

```
inputs = tokenizer.apply_chat_template(messages, tools=tools, add_generation_prompt=True, return_dict=True, return_tensors="pt")
inputs = {k: v.to(model.device) for k, v in inputs.items()}
out = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(out[0][len(inputs["input_ids"][0]):]))
```

And we get:

```
The current temperature in Paris, France is 22.0 ° Celsius.<|im_end|>
```

Although this was a simple demo with dummy tools and a single call, the same technique works with multiple real tools and longer conversations. This can be a powerful way to extend the capabilities of conversational agents with real-time information, computational tools like calculators, or access to large databases.

##### Understanding tool schemas

Each function you pass to the `tools` argument of `apply_chat_template` is converted into a [JSON schema](https://json-schema.org/learn/getting-started-step-by-step). These schemas are then passed to the model chat template. In other words, tool-use models do not see your functions directly, and they never see the actual code inside them. What they care about is the function **definitions** and the **arguments** they need to pass to them - they care about what the tools do and how to use them, not how they work! It is up to you to read their outputs, detect if they have requested to use a tool, pass their arguments to the tool function, and return the response in the chat.

Generating JSON schemas to pass to the template should be automatic and invisible as long as your functions follow the specification above, but if you encounter problems, or you simply want more control over the conversion, you can handle the conversion manually. Here is an example of a manual schema conversion.

```
from transformers.utils import get_json_schema

def multiply(a: float, b: float):
    """
    A function that multiplies two numbers
    
    Args:
        a: The first number to multiply
        b: The second number to multiply
    """
    return a * b

schema = get_json_schema(multiply)
print(schema)
```

This will yield:

```
{
  "type": "function", 
  "function": {
    "name": "multiply", 
    "description": "A function that multiplies two numbers", 
    "parameters": {
      "type": "object", 
      "properties": {
        "a": {
          "type": "number", 
          "description": "The first number to multiply"
        }, 
        "b": {
          "type": "number",
          "description": "The second number to multiply"
        }
      }, 
      "required": ["a", "b"]
    }
  }
}
```

If you wish, you can edit these schemas, or even write them from scratch yourself without using `get_json_schema` at all. JSON schemas can be passed directly to the `tools` argument of `apply_chat_template` - this gives you a lot of power to define precise schemas for more complex functions. Be careful, though - the more complex your schemas, the more likely the model is to get confused when dealing with them! We recommend simple function signatures where possible, keeping arguments (and especially complex, nested arguments) to a minimum.

Here is an example of defining schemas by hand, and passing them directly to `apply_chat_template`:

```
### A simple function that takes no arguments
current_time = {
  "type": "function", 
  "function": {
    "name": "current_time",
    "description": "Get the current local time as a string.",
    "parameters": {
      'type': 'object',
      'properties': {}
    }
  }
}

### A more complete function that takes two numerical arguments
multiply = {
  'type': 'function',
  'function': {
    'name': 'multiply',
    'description': 'A function that multiplies two numbers', 
    'parameters': {
      'type': 'object', 
      'properties': {
        'a': {
          'type': 'number',
          'description': 'The first number to multiply'
        }, 
        'b': {
          'type': 'number', 'description': 'The second number to multiply'
        }
      }, 
      'required': ['a', 'b']
    }
  }
}

model_input = tokenizer.apply_chat_template(
    messages,
    tools = [current_time, multiply]
)
```

#### Retrieval-augmented generation

“Retrieval-augmented generation” or “RAG” LLMs can search a corpus of documents for information before responding to a query. This allows models to vastly expand their knowledge base beyond their limited context size. Our recommendation for RAG models is that their template should accept a `documents` argument. This should be a list of documents, where each “document” is a single dict with `title` and `contents` keys, both of which are strings. Because this format is much simpler than the JSON schemas used for tools, no helper functions are necessary.

Here’s an example of a RAG template in action:

```
from transformers import AutoTokenizer, AutoModelForCausalLM

### Load the model and tokenizer
model_id = "CohereForAI/c4ai-command-r-v01-4bit"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
device = model.device # Get the device the model is loaded on

### Define conversation input
conversation = [
    {"role": "user", "content": "What has Man always dreamed of?"}
]

### Define documents for retrieval-based generation
documents = [
    {
        "title": "The Moon: Our Age-Old Foe", 
        "text": "Man has always dreamed of destroying the moon. In this essay, I shall..."
    },
    {
        "title": "The Sun: Our Age-Old Friend",
        "text": "Although often underappreciated, the sun provides several notable benefits..."
    }
]

### Tokenize conversation and documents using a RAG template, returning PyTorch tensors.
input_ids = tokenizer.apply_chat_template(
    conversation=conversation,
    documents=documents,
    chat_template="rag",
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt").to(device)

### Generate a response 
gen_tokens = model.generate(
    input_ids,
    max_new_tokens=100,
    do_sample=True,
    temperature=0.3,
    )

### Decode and print the generated text along with generation prompt
gen_text = tokenizer.decode(gen_tokens[0])
print(gen_text)
```

The `documents` input for retrieval-augmented generation is not widely supported, and many models have chat templates which simply ignore this input.

To verify if a model supports the `documents` input, you can read its model card, or `print(tokenizer.chat_template)` to see if the `documents` key is used anywhere.

One model class that does support it, though, is Cohere’s [Command-R](https://huggingface.co/CohereForAI/c4ai-command-r-08-2024) and [Command-R+](https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024), through their `rag` chat template. You can see additional examples of grounded generation using this feature in their model cards.
