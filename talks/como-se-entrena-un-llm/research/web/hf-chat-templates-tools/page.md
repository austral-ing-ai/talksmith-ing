# Expanding Chat Templates with Tools and Documents · Hugging Face

_Source: <https://huggingface.co/docs/transformers/main/en/chat_template_tools_and_documents>_

![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg) [Hugging Face](/) 

Transformers documentation

Expanding Chat Templates with Tools and Documents

# Transformers

🏡 View all docsAWS Trainium & InferentiaAccelerateArgillaAutoTrainBitsandbytesCLIChat UIDataset viewerDatasetsDeploying on AWSDiffusersDistilabelEvaluateGoogle CloudGoogle TPUsGradioHubHub Python LibraryHuggingface.jsInference Endpoints (dedicated)Inference ProvidersKernelsLeRobotLeaderboardsLightevalMicrosoft AzureOpenEnvOptimumPEFTReachy MiniSafetensorsSentence TransformersTRLTasksText Embeddings InferenceText Generation InferenceTokenizersTrackioTransformersTransformers.jsXetsmolagentstimm Search documentation mainv5.17.0v5.15.1v5.14.0v5.13.1v5.12.0v5.11.0v5.10.4v5.9.0v5.8.1v5.7.0v5.6.2v5.5.4v5.4.0v5.3.0v5.2.0v5.1.0v5.0.0v4.57.6v4.56.2v4.55.4v4.53.3v4.52.3v4.51.3v4.50.0v4.49.0v4.48.2v4.47.1v4.46.3v4.45.2v4.44.2v4.43.4v4.42.4v4.41.2v4.40.2v4.39.3v4.38.2v4.37.2v4.36.1v4.35.2v4.34.1v4.33.3v4.32.1v4.31.0v4.30.0v4.29.1v4.28.1v4.27.2v4.26.1v4.25.1v4.24.0v4.23.1v4.22.2v4.21.3v4.20.1v4.19.4v4.18.0v4.17.0v4.16.2v4.15.0v4.14.1v4.13.0v4.12.5v4.11.3v4.10.1v4.9.2v4.8.2v4.7.0v4.6.0v4.5.1v4.4.2v4.3.3v4.2.2v4.1.1v4.0.1v3.5.1v3.4.0v3.3.1v3.2.0v3.1.0v3.0.2v2.11.0v2.10.0v2.9.1v2.8.0v2.7.0v2.6.0v2.5.1v2.4.1v2.3.0v2.2.2v2.1.1v2.0.0v1.2.0v1.1.0v1.0.0doc-builder-html ARDEENESFRHIITJAKOPTROTETRZH <https://github.com/huggingface/transformers> You are viewing main version, which requires [installation from source](/docs/transformers/installation#install-from-source). If you'd like regular pip install, checkout the latest stable version ([v5.17.0](/docs/transformers/v5.17.0/chat_template_tools_and_documents)). ![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg) Join the Hugging Face community 

and get access to the augmented documentation experience

Collaborate on models, datasets and Spaces Faster examples with accelerated inference Switch between documentation themes [Sign Up](/join) 

to get started

# <#expanding-chat-templates-with-tools-and-documents> Expanding Chat Templates with Tools and Documents

The only argument that `apply_chat_template` requires is `messages`. However, you can pass any keyword argument to `apply_chat_template` and it will be accessible inside the template. This gives you a lot of freedom to use chat templates for many things. There are no restrictions on the names or the format of these arguments - you can pass strings, lists, dicts or whatever else you want.

That said, there are some common use-cases for these extra arguments, such as passing tools for function calling, or documents for retrieval-augmented generation. In these common cases, we have some opinionated recommendations about what the names and formats of these arguments should be, which are described in the sections below. We encourage model authors to make their chat templates compatible with this format, to make it easy to transfer tool-calling code between models.

## <#tool-use--function-calling> Tool use / function calling

“Tool use” LLMs can choose to call functions as external tools before generating an answer. When passing tools to a tool-use model, you can simply pass a list of functions to the `tools` argument:

 Copied 

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

### <#passing-tool-results-to-the-model> Passing tool results to the model

The sample code above is enough to list the available tools for your model, but what happens if it wants to actually use one? If that happens, you should:

1. Parse the model’s output to get the tool name(s) and arguments. 
2. Add the model’s tool call(s) to the conversation. 
3. Call the corresponding function(s) with those arguments. 
4. Add the result(s) to the conversation

### <#a-complete-tool-use-example> A complete tool use example

Let’s walk through a tool use example, step by step. For this example, we will use an 8B `Hermes-2-Pro` model, as it is one of the highest-performing tool-use models in its size category at the time of writing. If you have the memory, you can consider using a larger model instead like [Command-R](https://huggingface.co/CohereForAI/c4ai-command-r-v01) or [Mixtral-8x22B](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1), both of which also support tool use and offer even stronger performance.

First, let’s load our model and tokenizer:

 Copied 

```
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "NousResearch/Hermes-2-Pro-Llama-3-8B"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint, torch_dtype=torch.bfloat16, device_map="auto")
```

Next, let’s define a list of tools:

 Copied 

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

 Copied 

```
messages = [
  {"role": "system", "content": "You are a bot that responds to weather queries. You should reply with the unit used in the queried location."},
  {"role": "user", "content": "Hey, what's the temperature in Paris right now?"}
]
```

Now, let’s apply the chat template and generate a response:

 Copied 

```
inputs = tokenizer.apply_chat_template(messages, tools=tools, add_generation_prompt=True, return_dict=True, return_tensors="pt")
inputs = {k: v.to(model.device) for k, v in inputs.items()}
out = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(out[0][len(inputs["input_ids"][0]):]))
```

And we get:

 Copied 

```
<tool_call>
{"arguments": {"location": "Paris, France", "unit": "celsius"}, "name": "get_current_temperature"}
</tool_call><|im_end|>
```

The model has called the function with valid arguments, in the format requested by the function docstring. It has inferred that we’re most likely referring to the Paris in France, and it remembered that, as the home of SI units, the temperature in France should certainly be displayed in Celsius.

The output format above is specific to the `Hermes-2-Pro` model we’re using in this example. Other models may emit different tool call formats, and you may need to do some manual parsing at this step. For example, `Llama-3.1` models will emit slightly different JSON, with `parameters` instead of `arguments`. Regardless of the format the model outputs, you should add the tool call to the conversation in the format below, with `tool_calls`, `function` and `arguments` keys.

Next, let’s append the model’s tool call to the conversation.

 Copied 

```
tool_call = {"name": "get_current_temperature", "arguments": {"location": "Paris, France", "unit": "celsius"}}
messages.append({"role": "assistant", "tool_calls": [{"type": "function", "function": tool_call}]})
```

If you’re familiar with the OpenAI API, you should pay attention to an important difference here - the `tool_call` is a dict, but in the OpenAI API it’s a JSON string. Passing a string may cause errors or strange model behaviour!

Now that we’ve added the tool call to the conversation, we can call the function and append the result to the conversation. Since we’re just using a dummy function for this example that always returns 22.0, we can just append that result directly.

 Copied 

```
messages.append({"role": "tool", "name": "get_current_temperature", "content": "22.0"})
```

Some model architectures, notably Mistral/Mixtral, also require a `tool_call_id` here, which should be 9 randomly-generated alphanumeric characters, and assigned to the `id` key of the tool call dictionary. The same key should also be assigned to the `tool_call_id` key of the tool response dictionary below, so that tool calls can be matched to tool responses. So, for Mistral/Mixtral models, the code above would be:

 Copied 

```
tool_call_id = "9Ae3bDc2F"  # Random ID, 9 alphanumeric characters
tool_call = {"name": "get_current_temperature", "arguments": {"location": "Paris, France", "unit": "celsius"}}
messages.append({"role": "assistant", "tool_calls": [{"type": "function", "id": tool_call_id, "function": tool_call}]})
```

and

 Copied 

```
messages.append({"role": "tool", "tool_call_id": tool_call_id, "name": "get_current_temperature", "content": "22.0"})
```

Finally, let’s let the assistant read the function outputs and continue chatting with the user:

 Copied 

```
inputs = tokenizer.apply_chat_template(messages, tools=tools, add_generation_prompt=True, return_dict=True, return_tensors="pt")
inputs = {k: v.to(model.device) for k, v in inputs.items()}
out = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(out[0][len(inputs["input_ids"][0]):]))
```

And we get:

 Copied 

```
The current temperature in Paris, France is 22.0 ° Celsius.<|im_end|>
```

Although this was a simple demo with dummy tools and a single call, the same technique works with multiple real tools and longer conversations. This can be a powerful way to extend the capabilities of conversational agents with real-time information, computational tools like calculators, or access to large databases.

### <#understanding-tool-schemas> Understanding tool schemas

Each function you pass to the `tools` argument of `apply_chat_template` is converted into a [JSON schema](https://json-schema.org/learn/getting-started-step-by-step). These schemas are then passed to the model chat template. In other words, tool-use models do not see your functions directly, and they never see the actual code inside them. What they care about is the function **definitions** and the **arguments** they need to pass to them - they care about what the tools do and how to use them, not how they work! It is up to you to read their outputs, detect if they have requested to use a tool, pass their arguments to the tool function, and return the response in the chat.

Generating JSON schemas to pass to the template should be automatic and invisible as long as your functions follow the specification above, but if you encounter problems, or you simply want more control over the conversion, you can handle the conversion manually. Here is an example of a manual schema conversion.

 Copied 

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

 Copied 

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

 Copied 

```
# A simple function that takes no arguments
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

# A more complete function that takes two numerical arguments
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

## <#retrieval-augmented-generation> Retrieval-augmented generation

“Retrieval-augmented generation” or “RAG” LLMs can search a corpus of documents for information before responding to a query. This allows models to vastly expand their knowledge base beyond their limited context size. Our recommendation for RAG models is that their template should accept a `documents` argument. This should be a list of documents, where each “document” is a single dict with `title` and `contents` keys, both of which are strings. Because this format is much simpler than the JSON schemas used for tools, no helper functions are necessary.

Here’s an example of a RAG template in action:

 Copied 

```
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the model and tokenizer
model_id = "CohereForAI/c4ai-command-r-v01-4bit"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
device = model.device # Get the device the model is loaded on

# Define conversation input
conversation = [
    {"role": "user", "content": "What has Man always dreamed of?"}
]

# Define documents for retrieval-based generation
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

# Tokenize conversation and documents using a RAG template, returning PyTorch tensors.
input_ids = tokenizer.apply_chat_template(
    conversation=conversation,
    documents=documents,
    chat_template="rag",
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt").to(device)

# Generate a response 
gen_tokens = model.generate(
    input_ids,
    max_new_tokens=100,
    do_sample=True,
    temperature=0.3,
    )

# Decode and print the generated text along with generation prompt
gen_text = tokenizer.decode(gen_tokens[0])
print(gen_text)
```

The `documents` input for retrieval-augmented generation is not widely supported, and many models have chat templates which simply ignore this input.

To verify if a model supports the `documents` input, you can read its model card, or `print(tokenizer.chat_template)` to see if the `documents` key is used anywhere.

One model class that does support it, though, is Cohere’s [Command-R](https://huggingface.co/CohereForAI/c4ai-command-r-08-2024) and [Command-R+](https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024), through their `rag` chat template. You can see additional examples of grounded generation using this feature in their model cards.

[<>Update on GitHub](https://github.com/huggingface/transformers/blob/main/docs/source/en/chat_template_tools_and_documents.md) 

[Transformers→](/docs/transformers/main/en/index)
