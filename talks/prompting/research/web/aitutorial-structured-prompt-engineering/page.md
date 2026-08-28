# Structured Prompt Engineering - AI Tutorial

_Source: <https://aitutorial.dev/prompting/structured-prompt-engineering>_

> 

## Documentation Index

Fetch the complete documentation index at: [/llms.txt](/llms.txt)

Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)![light logo](https://mintcdn.com/digibee-1a4db0d2/qVB-_urhSn1RCBv0/logo/logo-light-full.svg?fit=max&auto=format&n=qVB-_urhSn1RCBv0&q=85&s=720536383dc8eb2a95e11611fc7839b4)![dark logo](https://mintcdn.com/digibee-1a4db0d2/qVB-_urhSn1RCBv0/logo/logo-dark-full.svg?fit=max&auto=format&n=qVB-_urhSn1RCBv0&q=85&s=dde82d875ffc50b174137cb594049e8e)[AI Tutorial home page](/)Search...⌘KSearch...NavigationContext Engineering & Prompt DesignStructured Prompt EngineeringContext Engineering & Prompt Design

# Structured Prompt Engineering

Copy pageCopy page

Design structured prompts that often reduce hallucinations

Copy pageCopy pageThe difference between a flaky prototype and a reliable production system often comes down to prompt structure. This page covers XML tags, few-shot examples, and structured outputs that make LLM responses consistent and parseable. 

## [​](#the-anatomy-of-a-production-prompt)The Anatomy of a Production Prompt

**The Core Components:** 

1. **Role/Persona** - Sets behavior and expertise level ( values: user, assistant, system) 
2. **Context** - Background information needed 
3. **Instructions** - What to do, step by step 
4. **Constraints** - What NOT to do, output format 
5. **Examples** - Few-shot demonstrations (optional) 
6. **Input** - The actual data to process 
If we put all these components together, we get the following prompt. This promt looks more complex than the previous one, but this reflects the complexity of the task and the context needed to complete it when you use the API. The playground constructs the final prompt from these components, which is then sent to the OpenAI API as part of the JSON message payload. You can see the exact JSON payload that will be sent in the “OpenAI JSON Message” section after submitting. **Let’s put all this together in code** **Practice Check:** 

- Write a prompt that includes role, context, instructions, constraints, examples, and input. 
- Expected: All 6 components present with explicit constraints and a clear output schema. 
- **Try this too:** Compare the outputs if you remove the structure and use less powerful models 
**In Production:** 

- Cost impact: Clear output schemas reduce parsing errors and retries (fewer re-runs). 
- Reliability: Structured prompts are easier to validate and monitor. 
- Performance: Slight token overhead; mitigate with caching (see Model Selection & Cost Optimization) 

## [​](#xml-tags-your-secret-weapon)XML Tags: Your Secret Weapon

**Why XML Tags Work:** 

- LLMs were trained on HTML/XML (web data) 
- Tags create clear boundaries in the context 
- Reduced hallucinations in controlled studies 

### [​](#practical-implication)Practical Implication

Compare these two approaches to structuring prompts: 

#### [​](#-antipattern)❌ Antipattern

#### [​](#-best-practice)✅ Best Practice

**In Production:** 

- **Cost Impact:** Tagging adds tokens; mitigate with caching . 
- **Reliability:** Clear boundaries reduce off-context responses; improves evaluability. 
- **Performance:** Slight overhead; offset by fewer retries and clearer parsing. 
- **Real Example:** Teams report 40–60% fewer hallucinations when tags + validation are combined. 
**Pattern:** Compare these two approaches: 

### [​](#example-1-schema-in-prompt)Example 1: Schema in Prompt

This approach includes the XML schema and example in the prompt itself, instructing the model to follow the XML structure. 

### [​](#example-2-structured-outputs-xml-mode)Example 2: Structured Outputs (XML Mode)

This approach uses prompt instructions to request XML output combined with XML parsing and validation. Note that OpenAI’s API doesn’t have a native XML response format like json_object, so we rely on prompt engineering and parsing. 

## [​](#few-shot-examples-teaching-by-showing)Few-Shot Examples: Teaching by Showing

**When to Use Few-Shot:** 

- Complex or subjective tasks 
- Specific output format required 
- Edge cases need clarification 
**Quality Over Quantity:** 

- 3-5 examples usually enough 
- More examples = more tokens = higher cost 
- Examples should cover edge cases, not just obvious ones 

## [​](#structured-outputs-with-json-schemas)Structured Outputs with JSON Schemas

**Why:** Schema enforcement reduces parsing errors and retries; makes outputs machine-checkable. Compare these two approaches: 

### [​](#example-1-schema-in-prompt-2)Example 1: Schema in Prompt

This approach includes the JSON schema in the prompt itself, instructing the model to follow the schema structure. 

### [​](#example-2-structured-outputs-json-mode)Example 2: Structured Outputs (JSON Mode)

This approach uses OpenAI’s structured outputs feature (`response_format: json_object`) combined with schema validation. This is more reliable than just including the schema in the prompt. See: [OpenAI Structured Outputs](https://openai.com/index/introducing-structured-outputs-in-the-api/) (2025), [Anthropic Prompt Engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) (2025), [Gemini Prompting Strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) (2025) in Additional Resources. 

## [​](#model-specific-prompt-optimization)Model-Specific Prompt Optimization

Different models have different “personalities.” Here’s what works best for each: 

### [​](#gpt-4-/-gpt-4-turbo)GPT-4 / GPT-4 Turbo

Prompt

```
# Strengths: Structured output, following complex instructions
# Best practices:
{
  "role": "senior_analyst",
  "task": "financial_analysis",
  "output_format": {
    "summary": "string",
    "key_metrics": ["string"],
    "recommendation": "buy|hold|sell"
  }
}

Input: Company revenue: $50M, growth: 15% YoY, market share: 8%
# GPT-4 excels at JSON, clear role definitions

```

### [​](#claude-sonnet/opus)Claude (Sonnet/Opus)

Prompt

```
# Strengths: Natural language, complex reasoning, long context
# Best practices:
<thinking>
Let me work through this step by step...
</thinking>

Analyze the quarterly financial report and identify key trends and risks.
# Claude benefits from explicit thinking blocks
# Excellent with XML tags and markdown

```

### [​](#gemini-1-5-pro)Gemini 1.5 Pro

Prompt

```
# Strengths: Massive context (2M tokens), multimodal
# Best practices:
[Upload entire 500-page PDF]
[Upload 10 images]
[Provide conversation history]

Based on ALL of the above context, answer: What are the main findings from the research study?
# Many teams place the query at the end; validate per task (see Gemini prompting strategies)
# Can handle entire codebases or document sets

```

---

Was this page helpful?

YesNo⌘I
