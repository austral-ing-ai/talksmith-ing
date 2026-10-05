# GitHub - langchain-ai/react-agent: LangGraph template for a simple ReAct agent · GitHub

_Source: <https://github.com/langchain-ai/react-agent>_

[Skip to content](#start-of-content) 

## Navigation Menu

</>[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Flangchain-ai%2Freact-agent)Appearance settingsSearch/[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Flangchain-ai%2Freact-agent)[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=langchain-ai%2Freact-agent)Appearance settings You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert {{ message }} [langchain-ai](/langchain-ai) / ** [react-agent](/langchain-ai/react-agent) ** Public template 

- [Notifications](/login?return_to=%2Flangchain-ai%2Freact-agent) You must be signed in to change notification settings 
- [Fork 698](/login?return_to=%2Flangchain-ai%2Freact-agent) 
- [Star 852](/login?return_to=%2Flangchain-ai%2Freact-agent) 
</langchain-ai/react-agent> main[Branches](/langchain-ai/react-agent/branches)[Tags](/langchain-ai/react-agent/tags)</langchain-ai/react-agent/branches></langchain-ai/react-agent/tags>Go to fileCodeOpen more actions menu

## Latest commit

## History

[99 Commits](/langchain-ai/react-agent/commits/main/)</langchain-ai/react-agent/commits/main/>99 Commits

## Folders and files

NameNameLast commit messageLast commit date[.github](/langchain-ai/react-agent/tree/main/.github)[.github](/langchain-ai/react-agent/tree/main/.github) [src/react_agent](/langchain-ai/react-agent/tree/main/src/react_agent)[src/react_agent](/langchain-ai/react-agent/tree/main/src/react_agent) [static](/langchain-ai/react-agent/tree/main/static)[static](/langchain-ai/react-agent/tree/main/static) [tests](/langchain-ai/react-agent/tree/main/tests)[tests](/langchain-ai/react-agent/tree/main/tests) [.codespellignore](/langchain-ai/react-agent/blob/main/.codespellignore)[.codespellignore](/langchain-ai/react-agent/blob/main/.codespellignore) [.env.example](/langchain-ai/react-agent/blob/main/.env.example)[.env.example](/langchain-ai/react-agent/blob/main/.env.example) [.gitignore](/langchain-ai/react-agent/blob/main/.gitignore)[.gitignore](/langchain-ai/react-agent/blob/main/.gitignore) [LICENSE](/langchain-ai/react-agent/blob/main/LICENSE)[LICENSE](/langchain-ai/react-agent/blob/main/LICENSE) [Makefile](/langchain-ai/react-agent/blob/main/Makefile)[Makefile](/langchain-ai/react-agent/blob/main/Makefile) [README.md](/langchain-ai/react-agent/blob/main/README.md)[README.md](/langchain-ai/react-agent/blob/main/README.md) [langgraph.json](/langchain-ai/react-agent/blob/main/langgraph.json)[langgraph.json](/langchain-ai/react-agent/blob/main/langgraph.json) [pyproject.toml](/langchain-ai/react-agent/blob/main/pyproject.toml)[pyproject.toml](/langchain-ai/react-agent/blob/main/pyproject.toml) [uv.lock](/langchain-ai/react-agent/blob/main/uv.lock)[uv.lock](/langchain-ai/react-agent/blob/main/uv.lock) View all files

## Repository files navigation

# LangGraph ReAct Agent Template

<#langgraph-react-agent-template> 

![CI](https://github.com/langchain-ai/react-agent/actions/workflows/unit-tests.yml/badge.svg)<https://github.com/langchain-ai/react-agent/actions/workflows/unit-tests.yml> ![Open in - LangGraph Studio](https://camo.githubusercontent.com/95de7ff0b618be50f56a01baf2dbe05e63bd638167af20fbb005b2559c06a6c5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f70656e5f696e2d4c616e6747726170685f53747564696f2d3030333234642e7376673f6c6f676f3d646174613a696d6167652f737667253262786d6c3b6261736536342c50484e325a79423462577875637a30696148523063446f764c336433647935334d793576636d63764d6a41774d43397a646d6369494864705a48526f505349344e53347a4d7a4d694947686c6157646f644430694f4455754d7a4d7a496942325a584a7a61573975505349784c6a416949485a705a58644362336739496a41674d4341324e4341324e43492b50484268644767675a4430695454457a494463754f474d744e69347a49444d754d5330334c6a45674e69347a4c5459754f4341794e5334334c6a51674d6a51754e69347a494449304c6a55674d6a55754f5341794e433431517a55334c6a55674e5467674e5467674e5463754e5341314f43417a4d69347a49445534494463754d7941314e693433494459674d7a49674e6d4d744d5449754f4341774c5445324c6a45754d7930784f5341784c6a68744d7a63754e6941784e693432597a49754f4341794c6a67674d793430494451754d69417a4c6a51674e793432637930754e6941304c6a67744d793430494463754e6b77304e7934794944517a534445324c6a68734c544d754e43307a4c6a526a4c5451754f4330304c6a67744e4334344c5445774c6a51674d4330784e53347962444d754e43307a4c6a526f4d7a41754e486f694c7a3438634746306143426b50534a4e4d5467754f5341794e533432597930784c6a45674d53347a4c5445674d5334334c6a51674d6934314c6a6b754e6941784c6a63674d533434494445754e7941794c6a63674d43417849433433494449754f4341784c6a59674e433478494445754e4341784c6a6b674d533430494449754e53347a49444d754d693078494334324c5334324c6a6b674d5334304c6a6b674d533431494441674d6934334c533431494449754e793078494441744c6a59674d5334784c533434494449754e6930754e4777794c6a59754e7930784c6a67744d693435597930314c6a6b744f53347a4c546b754e4330784d69347a4c5445784c6a55744f53343454544d3549444932597a41674d5334784c533435494449754e53307949444d754d6930794c6a51674d5334314c5449754e69417a4c6a51744c6a55674e4334794c6a67754d794179494445754e7941794c6a55674d7934784c6a59674d533431494445754e4341794c6a4d674d694179494445754e5330754f5341784c6a49744d7934314c5334304c544d754e5330794c6a45674d4330794c6a67744d6934344c5334344c544d754d7941784c6a59744c6a51674d5334324c533431494441744c6a59744d5334784c5334784c5445754e5330754e6930784c6a49744d5334324c6a63744d53343349444d754d7930794c6a45674d7934314c5334314c6a45754e533479494445754e69347a494449754d694177494334334c6a6b674d533430494445754f5341784c6a59674d6934784c6a51674d69347a4c5449754d7934794c544d754d6930754f4330754d7930794c5445754e7930794c6a55744d7934784c5445754d53307a4c544d744d79347a4c544d744c6a55694c7a34384c334e325a7a343d)<https://langgraph-studio.vercel.app/templates/open?githubUrl=https://github.com/langchain-ai/react-agent>

This template showcases a [ReAct agent](https://arxiv.org/abs/2210.03629) implemented using [LangGraph](https://github.com/langchain-ai/langgraph), designed for [LangGraph Studio](https://github.com/langchain-ai/langgraph-studio). ReAct agents are uncomplicated, prototypical agents that can be flexibly extended to many tools.

![Graph view in LangGraph studio UI](/langchain-ai/react-agent/raw/main/static/studio_ui.png)</langchain-ai/react-agent/blob/main/static/studio_ui.png>

The core logic, defined in `src/react_agent/graph.py`, demonstrates a flexible ReAct agent that iteratively reasons about user queries and executes actions, showcasing the power of this approach for complex problem-solving tasks.

## What it does

<#what-it-does> 

The ReAct agent:

1. Takes a user **query** as input 
2. Reasons about the query and decides on an action 
3. Executes the chosen action using available tools 
4. Observes the result of the action 
5. Repeats steps 2-4 until it can provide a final answer 

By default, it's set up with a basic set of tools, but can be easily extended with custom tools to suit various use cases.

## Getting Started

<#getting-started> 

Assuming you have already [installed LangGraph Studio](https://github.com/langchain-ai/langgraph-studio?tab=readme-ov-file#download), to set up:

1. Create a `.env` file. 

```
cp .env.example .env
```

1. Define required API keys in your `.env` file. 

The primary [search tool](/langchain-ai/react-agent/blob/main/src/react_agent/tools.py) [1](#user-content-fn-1-6d0d082f21aabeeb05928084ca8d819d) used is [Tavily](https://tavily.com/). Create an API key [here](https://app.tavily.com/sign-in).

### Setup Model

<#setup-model> 

The defaults values for `model` are shown below:

```
model: claude-sonnet-4-5-20250929
```

Follow the instructions below to get set up, or pick one of the additional options.

#### Anthropic

<#anthropic> 

To use Anthropic's chat models:

1. Sign up for an [Anthropic API key](https://console.anthropic.com/) if you haven't already. 
2. Once you have your API key, add it to your `.env` file: 

```
ANTHROPIC_API_KEY=your-api-key

```

#### OpenAI

<#openai> 

To use OpenAI's chat models:

1. Sign up for an [OpenAI API key](https://platform.openai.com/signup). 
2. Once you have your API key, add it to your `.env` file: 

```
OPENAI_API_KEY=your-api-key

```

1. Customize whatever you'd like in the code. 
2. Open the folder LangGraph Studio! 

## How to customize

<#how-to-customize> 

1. **Add new tools**: Extend the agent's capabilities by adding new tools in [tools.py](/langchain-ai/react-agent/blob/main/src/react_agent/tools.py). These can be any Python functions that perform specific tasks. 
2. **Select a different model**: We default to Anthropic's Claude 3 Sonnet. You can select a compatible chat model using `provider/model-name` via runtime context. Example: `openai/gpt-4-turbo-preview`. 
3. **Customize the prompt**: We provide a default system prompt in [prompts.py](/langchain-ai/react-agent/blob/main/src/react_agent/prompts.py). You can easily update this via context in the studio. 

You can also quickly extend this template by:

- Modifying the agent's reasoning process in [graph.py](/langchain-ai/react-agent/blob/main/src/react_agent/graph.py). 
- Adjusting the ReAct loop or adding additional steps to the agent's decision-making process. 

## Development

<#development> 

While iterating on your graph, you can edit past state and rerun your app from past states to debug specific nodes. Local changes will be automatically applied via hot reload. Try adding an interrupt before the agent calls tools, updating the default system message in `src/react_agent/context.py` to take on a persona, or adding additional nodes and edges!

Follow up requests will be appended to the same thread. You can create an entirely new thread, clearing previous history, using the `+` button in the top right.

You can find the latest (under construction) docs on [LangGraph](https://github.com/langchain-ai/langgraph) here, including examples and other references. Using those guides can help you pick the right patterns to adapt here for your use case.

LangGraph Studio also integrates with [LangSmith](https://smith.langchain.com/) for more in-depth tracing and collaboration with teammates.

## Footnotes

1. 

[https://python.langchain.com/docs/concepts/#tools](https://python.langchain.com/docs/concepts/#tools) [↩](#user-content-fnref-1-6d0d082f21aabeeb05928084ca8d819d)

## About

LangGraph template for a simple ReAct agent

### Topics

[langgraph](/topics/langgraph)[langgraph-python](/topics/langgraph-python)[langgraph-template](/topics/langgraph-template)

### Resources

[Readme](#readme-ov-file)[MIT license](#MIT-1-ov-file)

### Code of conduct

[Code of conduct](/langchain-ai/react-agent#coc-ov-file)

### Contributing

[Contributing](#contributing-ov-file)

### Security policy

[Security policy](#security-ov-file)[Activity](/langchain-ai/react-agent/activity)[Custom properties](/langchain-ai/react-agent/custom-properties)

### Stars

**852** stars

### Watchers

**8** watching

### Forks

****[698 forks](/langchain-ai/react-agent/forks)[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Flangchain-ai%2Freact-agent&report=langchain-ai+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

 You can’t perform that action at this time.
