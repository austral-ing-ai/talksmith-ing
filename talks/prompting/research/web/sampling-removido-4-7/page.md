# Claude 4.7 Migration Guide

_Source: <https://openrouter.ai/docs/cookbook/evaluate-and-optimize/model-migrations/claude-4-7>_

> 

## Documentation Index

Fetch the complete documentation index at: [/docs/llms.txt](/docs/llms.txt)

Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)![light logo](https://mintcdn.com/openrouter-d02e98a0/ksNSeB_K7gD-BUDh/assets/logo-v2-light.svg?fit=max&auto=format&n=ksNSeB_K7gD-BUDh&q=85&s=690e45873843519efe02bcbe45795dac)![dark logo](https://mintcdn.com/openrouter-d02e98a0/ksNSeB_K7gD-BUDh/assets/logo-v2-dark.svg?fit=max&auto=format&n=ksNSeB_K7gD-BUDh&q=85&s=8ba2f49b11cd9839c37dd03c62537ebd)[OpenRouter | Documentation home page](https://openrouter.ai)Search...⌘KAsk Assistant⌘ISearch...NavigationModel MigrationsClaude 4.7 Migration Guide[Docs](/docs/quickstart)[API Reference](/docs/api_reference/overview)[Client SDKs](/docs/client-sdks/overview)[Agent SDK](/docs/agent-sdk/overview)[Cookbook](/docs/cookbook/get-started/quickstart)Model Migrations

# Claude 4.7 Migration Guide

Copy pageCopy page

Migrate to Claude 4.7 Opus — sampling parameters removed, adaptive-only thinking, and new xhigh effort level

Copy pageCopy page**Update · June 22, 2026**As of June 22, 2026, OpenRouter maps `reasoning.effort` to Anthropic’s `output_config.effort` on Claude 4.6 and newer models — previously it was ignored. `verbosity` is unchanged: it still sets `output_config.effort`, and wins if both are passed. 

## [​](#what’s-new)What’s New

See Anthropic’s [Migrating to Claude Opus 4.7](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-to-claude-opus-4-7) for a full overview of changes. Claude 4.7 Opus introduces three major changes: 

1. **Sampling parameters removed** — `temperature`, `top_p`, and `top_k` are no longer supported and will be ignored 
2. **Adaptive-only thinking** — when reasoning is enabled the only supported mode is adaptive; `thinking.budget_tokens` is no longer supported and `reasoning.max_tokens` is ignored 
3. **New `'xhigh'` effort level** — a new effort level between `'high'` and `'max'` via `verbosity` / `output_config.effort` 

## [​](#sampling-parameters-removed)Sampling Parameters Removed

Claude 4.7 Opus no longer accepts `temperature`, `top_p`, or `top_k`. If you pass these parameters, they will be silently ignored — your request will still succeed, but the parameters will have no effect. 

```
// These parameters are ignored on Claude 4.7 Opus
{
  "model": "anthropic/claude-4.7-opus",
  "temperature": 0.5,
  "top_p": 0.9,
  "top_k": 50,
  "messages": [{ "role": "user", "content": "Hello" }]
}

```

## [​](#adaptive-only-thinking)Adaptive-Only Thinking

Claude 4.7 Opus supports only adaptive thinking. On 4.6, reasoning could be controlled via a token budget (`reasoning.max_tokens` / `thinking.budget_tokens`) or left adaptive; on 4.7, budget-based thinking is removed and adaptive is the only remaining mode when reasoning is on. Reasoning itself remains opt-in on all Anthropic models via ``[reasoning.enabled=true](/docs/guides/best-practices/reasoning-tokens) — 4.7 does not change that. Concretely on 4.7: 

- `reasoning.max_tokens` is accepted but ignored 
- `reasoning.effort` maps to Anthropic’s `output_config.effort` (see [Parameter Summary](#parameter-summary)) rather than a thinking budget 
- `thinking.budget_tokens` is no longer supported upstream 
To influence overall response effort (not reasoning-specific), use ``[verbosity](#new-xhigh-effort-level). It maps to Anthropic’s `output_config.effort` and applies whether or not reasoning is enabled. 

```
// Opt in to adaptive thinking — the only thinking mode on 4.7 Opus
{
  "model": "anthropic/claude-4.7-opus",
  "reasoning": { "enabled": true },
  "messages": [{ "role": "user", "content": "Solve this problem step by step" }]
}

```

```
// reasoning.max_tokens is ignored (adaptive used)
{
  "model": "anthropic/claude-4.7-opus",
  "reasoning": { "enabled": true, "max_tokens": 10000 },
  "messages": [{ "role": "user", "content": "Hello" }]
}
// ↑ Equivalent to just { "reasoning": { "enabled": true } }

```

```
// reasoning.effort maps to output_config.effort (thinking stays adaptive)
{
  "model": "anthropic/claude-4.7-opus",
  "reasoning": { "enabled": true, "effort": "low" },
  "messages": [{ "role": "user", "content": "Hello" }]
}
// ↑ Equivalent to { "reasoning": { "enabled": true }, "verbosity": "low" }

```

## [​](#new-xhigh-effort-level)New `'xhigh'` Effort Level

A new `'xhigh'` effort level is available between `'high'` and `'max'` via the `verbosity` parameter. This maps to Anthropic’s `output_config.effort`. 

```
{
  "model": "anthropic/claude-4.7-opus",
  "verbosity": "xhigh"
}

```

The full effort scale is now: `low` → `medium` → `high` → `xhigh` → `max`. `'xhigh'` is only supported on Claude 4.7 Opus. `'max'` is supported on Claude 4.6+. For older models, both automatically fall back to `'high'`. 

## [​](#parameter-summary)Parameter Summary

With sampling parameters and reasoning budgets removed on 4.7, `output_config.effort` is the remaining lever for influencing overall response effort. You can set it via `verbosity`, or via `reasoning.effort` when reasoning is enabled (`verbosity` wins if both are passed; `'minimal'` maps to `'low'`, and `'none'` disables reasoning entirely so no `output_config.effort` is sent). ParameterClaude 4.7 Opus Behavior`temperature`, `top_p`, `top_k`Ignored`reasoning.max_tokens`Ignored (adaptive used)`reasoning.effort`Sets `output_config.effort` (when reasoning is enabled)`verbosity`Sets `output_config.effort` 

```
{ "model": "anthropic/claude-4.7-opus", "verbosity": "xhigh" }

```

## [​](#breaking-changes)Breaking Changes

FeatureOpus 4.6Opus 4.7`temperature` / `top_p` / `top_k`SupportedIgnoredThinking modes (when `reasoning.enabled=true`)Adaptive or budget-basedAdaptive only`reasoning.max_tokens`Sets a thinking budgetIgnored (adaptive used)`reasoning.effort`Sets `output_config.effort`Sets `output_config.effort``'xhigh'` effort levelFalls back to `'high'`Supported`'max'` effort levelSupportedSupportedAssistantResponses are generated using AI and may contain mistakes.
