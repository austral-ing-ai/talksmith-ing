# Advanced Prompting Techniques - AI Tutorial

_Source: <https://aitutorial.dev/prompting/advanced-techniques>_

> 

## Documentation Index

Fetch the complete documentation index at: [/llms.txt](/llms.txt)

Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)![light logo](https://mintcdn.com/digibee-1a4db0d2/qVB-_urhSn1RCBv0/logo/logo-light-full.svg?fit=max&auto=format&n=qVB-_urhSn1RCBv0&q=85&s=720536383dc8eb2a95e11611fc7839b4)![dark logo](https://mintcdn.com/digibee-1a4db0d2/qVB-_urhSn1RCBv0/logo/logo-dark-full.svg?fit=max&auto=format&n=qVB-_urhSn1RCBv0&q=85&s=dde82d875ffc50b174137cb594049e8e)[AI Tutorial home page](/)Search...⌘KSearch...NavigationContext Engineering & Prompt DesignAdvanced Prompting TechniquesContext Engineering & Prompt Design

# Advanced Prompting Techniques

Copy pageCopy page

Apply advanced techniques to improve the performance of your prompts

Copy pageCopy pageWhen a single prompt isn’t enough, you need techniques that improve reasoning and reliability. This page covers Chain-of-Thought, self-consistency, extended thinking, and prompt chaining. 

## [​](#chain-of-thought-cot--making-reasoning-visible)Chain-of-Thought (CoT): Making Reasoning Visible

Chain-of-Thought (CoT) is less common with reasoning models, since they already perform an explicit reasoning step. With SLMs and other non-reasoning models, however, CoT can still make a meaningful difference.That said, it’s still valuable to learn CoT techniques—they help you understand how these models think and how to effectively influence their behavior. **The Problem:** But what if you need to debug a wrong answer? You can’t see the reasoning. The expected response would be something like (note: the response shown below is a placeholder example, not a real API response): **In Production:** 

- Use CoT for complex reasoning; avoid for deterministic extraction/classification at temperature=0. 
- Consider privacy/compliance: avoid logging sensitive intermediate reasoning. 
- Cost/latency rise with longer outputs—use selectively. 
**Why It Works:** 

- Often improves performance on reasoning tasks (magnitude varies by task/model) 
- Creates “intermediate tokens” that guide the model 
- Makes errors debuggable 
**Production Pattern:** **Real-World Impact:** 

- Code generation: 35% fewer bugs with CoT 
- Math problems: 50-70% accuracy improvement 
- Medical diagnosis: More reliable clinical reasoning 

## [​](#self-consistency-voting-for-reliability)Self-Consistency: Voting for Reliability

**The Problem:** One response might be wrong due to non-determinism, ambiguous tasks, and/or valid solution paths. **The Solution:** Generate multiple responses and vote. **When to Use:** 

- High-stakes decisions (medical, financial, legal) 
- Complex reasoning where errors are costly 
- Classification tasks where confidence matters 
**Cost Consideration:** 

- 5x Agent tasks = 5x cost 
- Use only when accuracy justifies expense 
**Performance Data:** 

- CoT often improves performance on reasoning benchmarks; magnitude varies by task/model (see Wei et al., 2022) 
- Combining CoT + Self-Consistency can yield additional gains; magnitude varies by task/model (see Wang et al., 2022) 
- Always validate on your evaluation set; do not assume universal gains 

## [​](#extended-thinking-anthropic’s-secret-weapon)Extended Thinking: Anthropic’s Secret Weapon

**Claude-Specific Feature:** Claude can expose its “thinking” before answering using special tags. Prompt

```
<thinking>
Let me analyze this complex legal document...
- First, I'll identify the key clauses
- Then, I'll look for any conflicting terms
- Finally, I'll assess risk level
</thinking>

[Your actual task here]

```

**Why This Matters:** 

1. **Debugging:** See where reasoning went wrong 
2. **Quality:** Forces model to think before answering 
3. **Transparency:** Clients can audit AI decisions 
**Thinking tags can also be used to guide Claude steps:** TypeScript

```
async function analyzeContract(contractText: string): Promise<{
    analysis: any;
    reasoning: string;
}> {
    const prompt = `
<document>
${contractText}
</document>

<thinking>
I need to analyze this contract for:
1. Key obligations
2. Termination clauses
3. Liability limits
4. Red flags

Let me work through each section...
</thinking>

Provide a JSON response with:
- obligations: list of key obligations
- risks: list of potential risks
- recommendations: list of recommended actions
`;
    
    const response = await claude.generate(prompt);
    
    // Parse thinking section for audit trail
    const thinking = extractBetweenTags(response, "thinking");
    const result = extractJson(response);
    
    return {
        analysis: result,
        reasoning: thinking  // Store for compliance/review
    };
}

```

## [​](#prompt-chaining-breaking-complex-tasks)Prompt Chaining: Breaking Complex Tasks

**Single Prompt Limitations:** 

- Context window fills up 
- Errors compound 
- Hard to debug 
- Expensive to retry 
**Chaining Solution:** Break one complex task into sequential simple tasks. **Benefits:** 

- Each step is simple → fewer errors 
- Failed steps can retry independently 
- Cheaper: Only call expensive steps when needed 
- Easier to evaluate and improve 
**Trade-off:** 

- More latency (sequential calls) 
- More complex code 
- Multiple LLM calls (but often cheaper overall) 

---

Was this page helpful?

YesNo⌘I
