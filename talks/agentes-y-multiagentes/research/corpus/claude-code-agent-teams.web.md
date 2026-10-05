---
source_file: claude-code-agent-teams
source_type: web-capture
ingested_at: 2026-10-04
---

# Orchestrate teams of Claude Code sessions (Claude Code Docs — "Agent teams")

## Provenance
- Original location: web/claude-code-agent-teams/ (text from `page.md`, 42 KB; `original.html` not needed as fallback — `page.md` has full headings and body)
- Format: html (web capture via talksmith:ingest)
- URL: https://code.claude.com/docs/en/agent-teams
- Author / source (if known): Anthropic, Claude Code official documentation (section "Agents and parallel work")
- Date of original (if known): not stated on page; captured 2026-10-04T19:31:26Z (HTTP 200, 723,739 bytes). Page references Claude Code versions up to v2.1.281.

## Key claims
- Agent teams are **experimental and disabled by default**; enabled with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` (env or `settings.json` `env` block). Without it, "no team is set up at session start, no team directories are written, and Claude does not spawn or propose teammates."
- "One session acts as the team lead, coordinating work, assigning tasks, and synthesizing results. Teammates work independently, each in its own context window, and communicate directly with each other. You can also talk to any teammate directly without going through the lead."
- The page recommends checking lighter options first: **subagents** (within one session) and **cross-session messaging** (Claude passes findings between sessions the user runs).
- Strongest use cases: research and review; new modules/features (each teammate owns a piece); debugging with competing hypotheses; cross-layer coordination (frontend/backend/tests).
- "Agent teams add coordination overhead and use significantly more tokens than a single session. They work best when teammates can operate independently. For sequential tasks, same-file edits, or work with many dependencies, a single session or subagents are more effective."
- Subagents vs. agent teams: subagents report results back to the main agent (hub-and-spoke); in agent teams teammates share a task list, claim work, and message each other directly (see table under Definitions).
- Enabling agent teams changes ordinary delegation: a subagent that Claude **names** launches as a teammate, so "teams can form even when you didn't ask for one." Claude Code does not ask for confirmation to launch a teammate.
- Teammates require an **interactive session**; in non-interactive mode (`-p`, including Agent SDK sessions) named subagents run as ordinary subagents.
- **Model selection per teammate** (first that applies): (1) model named in the spawn prompt; (2) the subagent definition's `model` (`inherit` = lead's model); (3) `CLAUDE_CODE_SUBAGENT_MODEL` if not `inherit`; (4) the lead's current model. `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` disables sources 1–2 (requires v2.1.257+). Example prompt: "Spawn 4 teammates to refactor these modules in parallel. Use Sonnet for each teammate." Teammates inherit the lead's effort level by default. A teammate's model and fast mode are fixed at spawn.
- Organization `availableModels` allowlist is enforced; blocked family aliases are substituted with the newest permitted version (Anthropic API / Claude Platform on AWS), otherwise teammate falls back to the lead's model.
- **Plan mode**: a teammate spawned while the lead is in plan mode works read-only until its plan is ready, then sends a plan approval request; "Claude Code approves the plan in the lead's session as soon as the request arrives, without the lead reviewing it."
- Shared task list: states pending / in progress / completed; dependencies block claiming; lead assigns or teammates self-claim; claiming uses **file locking** to prevent race conditions. Dependencies auto-unblock when a task completes.
- Shutdown: the lead sends a shutdown request; the teammate can approve or reject with an explanation.
- Quality-gate hooks: `TeammateIdle`, `TaskCreated`, `TaskCompleted` (exit code 2 = block and send feedback).
- Waking / messaging: messages are delivered automatically (no polling). Idle teammates notify the lead with their final answer; a teammate failing on API error notifies the lead with the error. "When Claude messages an in-process teammate that is no longer running, Claude Code brings it back in the same session, restores any conversation saved for it, and gives it the message as its next prompt." A message also wakes a teammate waiting to retry a failed API request.
- Security between agents: the receiving agent is told a `SendMessage` message came from another Claude session, not the user; a teammate cannot approve permission prompts or supply consent on the user's behalf, nor relay a denied action to another teammate. In auto mode, the classifier treats relayed approval claims as untrusted and reviews each inter-agent message before delivery.
- Permissions: teammates start with the lead's permission mode (except `dontAsk`); `--dangerously-skip-permissions` propagates to all; teammate permission prompts surface in the lead session.
- Context: each teammate loads project context (CLAUDE.md, MCP servers, skills) and receives the spawn prompt; "The lead's conversation history does not carry over."
- Token usage scales with number of active teammates; for research/review/new features "the extra tokens are usually worthwhile"; for routine tasks a single session is more cost-effective. In-process teammate cache TTL is 5 minutes by default (`subagentPromptCacheTtl` = `1h` to extend).
- Best practices: give enough context in the spawn prompt; start with **3–5 teammates**; "Three focused teammates often outperform five scattered ones"; 5–6 tasks per teammate; avoid two teammates editing the same file; monitor and steer; start with research/review tasks; tell the lead to wait if it starts implementing itself.
- Limitations: no session resumption of in-process teammates (`/resume`, `/rewind`); task status can lag; slow shutdown; one team per session; **no nested teams** (teammates cannot spawn teammates; only the lead manages the team); in-process teammates cannot run background subagents; lead is fixed for the session's lifetime; per-teammate permission modes can't be set at spawn; split panes need tmux or iTerm2 (not VS Code terminal, Windows Terminal, Ghostty).

## Definitions and terminology
- **Agent team**: multiple coordinated Claude Code instances with shared tasks, inter-agent messaging, and centralized management.
- **Team lead**: "The main Claude Code session that spawns teammates and coordinates work." Agent type `team-lead` in the team config.
- **Teammate**: "Separate Claude Code instances that each work on assigned tasks." Each is "a full, independent Claude Code session."
- **Task list**: "Shared list of work items that teammates claim and complete." Stored at `~/.claude/tasks/{team-name}/` (persists; never uploaded).
- **Mailbox**: "Messaging system for communication between agents." One JSON file per agent at `~/.claude/teams/{team-name}/inboxes/{agent-name}.json`. A message counts as sent only when the write to the recipient's mailbox file succeeds.
- **Team config**: `~/.claude/teams/{team-name}/config.json`, with a `members` array (name, agent ID, agent type); removed at session end; not to be hand-edited. Team name = `session-` + first 8 chars of the session ID.
- **Display modes**: `in-process` (default; all teammates in the main terminal, agent panel navigated with arrows/Enter/Escape, `x` stops, Ctrl+T toggles task list) vs. **split panes** (`tmux`, `iterm2`, or `auto`); setting `teammateMode` or flag `--teammate-mode` (experimental, not in `--help`).
- **Cross-session messaging**: separate sessions passing messages without a team (linked page, not described here).
- **Fork / isolation**: an Agent tool call that is a fork or passes `isolation` does not launch a teammate even if named.

Subagents vs. agent teams comparison table (reconstructed from flattened capture):

| | Subagents | Agent teams |
|---|---|---|
| **Context** | Own context window; results return to the caller | Own context window; fully independent |
| **Communication** | Return a result to the caller. Subagents that Claude named when it spawned them can also message each other | Teammates message each other directly |
| **Coordination** | Main agent manages all work | Self-coordination through messages, plus a shared task list for agents that have the Task tools |
| **Best for** | Focused tasks where only the result matters | Complex work requiring discussion and collaboration |
| **Token cost** | Lower: results summarized back to main context | Higher: each teammate is a separate Claude instance |

## Evidence and examples
- Starter prompt (TODO-tracking CLI): "Spawn three teammates to explore this from different angles: one on UX, one on technical architecture, one playing devil's advocate." Works "because the three roles are independent and can explore the problem without waiting on each other."
- Parallel code review of PR #142 with three lenses (security, performance, test coverage); "A single reviewer tends to gravitate toward one type of issue at a time." The lead synthesizes findings.
- Competing hypotheses: 5 teammates debate why "the app exits after one message"; "Sequential investigation suffers from anchoring ... the theory that survives is much more likely to be the actual root cause."
- Spawn prompt with full context example: security reviewer for `src/auth/` (JWT in httpOnly cookies, report with severity ratings).
- Subagent definitions reused as teammates ("Spawn a teammate using the security-reviewer agent type to audit the auth module"): `tools` applied (+ `SendMessage` and `TaskCreate/TaskGet/TaskList/TaskUpdate` added for in-process), `model` applied, `disallowedTools`/`effort` for in-process only, body appended (in-process) or replaces system prompt (split-pane), `skills` not applied, `mcpServers` only for split-pane.
- Sizing heuristic: "If you have 15 independent tasks, 3 teammates is a good starting point."
- Version-history notes: before v2.1.251 `CLAUDE_CODE_SUBAGENT_MODEL` came first in the model order; `teammateDefaultModel` removed in v2.1.234; malformed-mailbox bug fixed in v2.1.207; split-pane effort inheritance from v2.1.186; `--setting-sources` respected by split-pane teammates from v2.1.281.

## Inconsistencies / open questions
- [verified] Plan approval is automatic, not a review step: the section "Have teammates plan before implementing" implies a gate, but the same section states the lead's session approves "as soon as the request arrives, without the lead reviewing it," and the Permissions section repeats it ("the lead session grants teammate plan approvals without a separate prompt to you") — checked both passages in `page.md`. Matters if the talk presents plan mode as human/lead review.
- [verified] The subagent/team distinction on communication is not clean-cut in the source: the comparison table says subagents "return a result to the caller" but adds that named subagents "can also message each other," and the Troubleshooting section says a named subagent's name "keeps working as a SendMessage address" — checked in `page.md`. A slide that says "subagents can't talk to each other" would overstate the doc.
- [verified] For the "expensive lead, cheaper workers" framing: the doc does NOT make teammates cheaper by default — the fallback is "The lead's current model"; cheaper teammates require naming the model in the spawn prompt, in the subagent definition, or via `CLAUDE_CODE_SUBAGENT_MODEL` — checked in "Specify teammates and models."
- [verified] "No nested teams: teammates cannot spawn their own teammates" — only one level of hierarchy (lead → teammates); in-process teammates may still spawn foreground subagents (Limitations section). Checked in `page.md`.
- [open question] Version numbers (v2.1.186 … v2.1.281) and the experimental status reflect the page as captured on 2026-10-04; the feature moves fast — re-check the live page before a live demo, especially whether the env flag is still required.
- [open question] The page links to but does not describe "cross-session messaging" (`/docs/en/cross-session-messaging`), which is the mechanism closest to "the lead messages/wakes other sessions"; if the talk relies on it, capture that page too.
- [open question] Display-mode prose contains capture artifacts (doubled backticks before links such as ``[it2 CLI]``); content is intact, only formatting is noisy — no action needed unless quoting verbatim.

## Images / diagrams

### claude-code-agent-teams.web/images/subagents-vs-agent-teams-light.png
- Provenance: `web/claude-code-agent-teams/assets/subagents-vs-agent-teams-light.png` (4245×1615 PNG), embedded in section "Compare with subagents"; original URL https://mintcdn.com/claude-code/nsvRFSDNfpSU5nT7/images/subagents-vs-agent-teams-light.png. Alt text: "Diagram comparing subagent and agent team architectures. Subagents are spawned by the main agent, do work, and report results back. Agent teams coordinate through a shared task list, with teammates communicating directly with each other." Caption: "Subagents report results back to the main agent. In agent teams, teammates share a task list, claim work, and communicate directly with each other."
- Depiction: Hand-drawn-style side-by-side comparison. Left panel "Subagents": a Main Agent spawns three Subagents ("Spawn Subagent"); each does "Work" producing a dotted-circle "Result"; the three results merge into one line labelled "Report" that returns to the Main Agent. No arrows between subagents. Right panel "Agent Teams": a "Main Agent (Team Lead)" does "Spawn Team & Assign Tasks" into a dotted "Shared Task List"; three Teammates are linked to the list by bidirectional "Communicate & Claim Tasks" arrows, are linked to each other by bidirectional "Communicate" arrows, and each has its own "Work" self-loop. Nothing reports back directly to the lead.
- Why it matters: The clearest contrast in the corpus between hub-and-spoke delegation (subagents only talk to the parent, results are summarised back) and a peer topology (shared task list + direct teammate messaging). Directly usable to explain coordination topologies and their trade-offs.
- Transcribed text:

  ```text
  Subagents
  Main Agent
  Spawn Subagent (x3)
  Subagent (x3)
  Work (x3)
  Result (x3)
  Report

  Agent Teams
  Main Agent (Team Lead)
  Spawn Team & Assign Tasks
  Shared Task List
  Communicate & Claim Tasks (x3)
  Teammate (x3)
  Communicate
  Communicate
  Work (x3)
  ```


### claude-code-agent-teams.web/images/subagents-vs-agent-teams-dark.png
- Provenance: `web/claude-code-agent-teams/assets/subagents-vs-agent-teams-dark.png` (4245×1615 PNG), dark-theme variant of the same diagram, same section and alt text; original URL https://mintcdn.com/claude-code/nsvRFSDNfpSU5nT7/images/subagents-vs-agent-teams-dark.png.
- Depiction: Dark-theme rendering of the same diagram as subagents-vs-agent-teams-light.png (checked visually: identical layout, boxes, arrows and labels; only the colour palette differs).
- Why it matters: Same content as the light variant; keep only one in the deck (choose by deck theme).
- Transcribed text:

  ```text
  Subagents
  Main Agent
  Spawn Subagent (x3)
  Subagent (x3)
  Work (x3)
  Result (x3)
  Report

  Agent Teams
  Main Agent (Team Lead)
  Spawn Team & Assign Tasks
  Shared Task List
  Communicate & Claim Tasks (x3)
  Teammate (x3)
  Communicate
  Communicate
  Work (x3)
  ```


### claude-code-agent-teams.web/images/light.svg
- Provenance: `web/claude-code-agent-teams/assets/light.svg`, site header logo (alt "light logo") of Claude Code Docs. Decorative chrome, not content.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### claude-code-agent-teams.web/images/dark.svg
- Provenance: `web/claude-code-agent-teams/assets/dark.svg`, site header logo (alt "dark logo"), dark-theme variant. Decorative chrome, not content.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

## Raw / preserved excerpts

> Agent teams are experimental and disabled by default. Enable them by setting `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in your settings.json or environment. Without that variable, no team is set up at session start, no team directories are written, and Claude does not spawn or propose teammates. Agent teams have known limitations around session resumption, task coordination, and shutdown behavior. Agent teams let you coordinate multiple Claude Code instances working together. One session acts as the team lead, coordinating work, assigning tasks, and synthesizing results. Teammates work independently, each in its own context window, and communicate directly with each other. You can also talk to any teammate directly without going through the lead. Before you set up a team, check whether a lighter option does the job. Subagents work within a single session, and with cross-session messaging Claude can pass findings between the sessions you run yourself.

> Agent teams add coordination overhead and use significantly more tokens than a single session. They work best when teammates can operate independently. For sequential tasks, same-file edits, or work with many dependencies, a single session or subagents are more effective.

> Use subagents when you need quick, focused workers that report back. Use agent teams when teammates need to share findings, challenge each other, and coordinate on their own.

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

> Enabling agent teams also changes ordinary delegation. Claude may name a subagent on its own, and while agent teams are enabled, a subagent that Claude names launches as a teammate, so teams can form even when you didn't ask for one. [...] Spawning teammates also requires an interactive session. In non-interactive mode with the `-p` flag, including Agent SDK sessions, Claude doesn't spawn teammates, and a subagent that Claude names runs as an ordinary subagent even with agent teams enabled.

```
I'm designing a CLI tool that helps developers track TODO comments across
their codebase. Spawn three teammates to explore this from different angles:
one on UX, one on technical architecture, one playing devil's advocate.
```

> From there, Claude populates a shared task list in a session that has the Task tools, spawns teammates for each perspective, has them explore the problem, and synthesizes findings when finished. Claude may sometimes use subagents instead of creating a team. Subagents appear in the same agent panel as teammates, so the panel alone doesn't confirm a team formed. If Claude spawned subagents instead, ask again and explicitly request an agent team.

```
Spawn 4 teammates to refactor these modules in parallel. Use Sonnet for
each teammate.
```

> Claude Code picks each teammate's model from the first of these that applies:
> 1. The model your spawn prompt names for that teammate.
> 2. For a teammate spawned from a subagent definition, the definition's `model`, where `inherit` selects the lead's model.
> 3. `CLAUDE_CODE_SUBAGENT_MODEL`, when it's set to anything other than `inherit`.
> 4. The lead's current model.

> When a teammate finishes planning, it sends a plan approval request to the lead. Claude Code approves the plan in the lead's session as soon as the request arrives, without the lead reviewing it. The teammate's edits and commands still go through the permission prompts described in Permissions. Once approved, the teammate exits plan mode and begins implementation.

> The shared task list coordinates work across the team. The lead creates tasks and teammates work through them. Tasks have three states: pending, in progress, and completed. Tasks can also depend on other tasks: a pending task with unresolved dependencies cannot be claimed until those dependencies are completed. [...] Task claiming uses file locking to prevent race conditions when multiple teammates try to claim the same task simultaneously.

> To start a team, ask Claude for teammates. Claude launches a teammate when it calls the Agent tool with a `name` while agent teams are enabled, unless the call is a fork or passes `isolation` on the call itself. Claude Code doesn't ask you to confirm the launch.

> An agent team consists of: Team lead — The main Claude Code session that spawns teammates and coordinates work; Teammates — Separate Claude Code instances that each work on assigned tasks; Task list — Shared list of work items that teammates claim and complete; Mailbox — Messaging system for communication between agents. Each agent's mailbox is a JSON file at `~/.claude/teams/{team-name}/inboxes/{agent-name}.json`. [...] Claude Code reports a message as sent only when the write to the recipient's mailbox file succeeds, whether the message is plain text or a structured protocol message such as a plan approval or shutdown request.

> When Claude messages an in-process teammate that is no longer running, Claude Code brings it back in the same session, restores any conversation saved for it, and gives it the message as its next prompt.

> When one agent sends another a message over `SendMessage`, Claude Code tells the receiving agent the message came from another Claude session, not from you. A teammate can't approve a permission prompt or supply consent on your behalf, and a teammate that was denied an action can't relay it to another teammate to bypass the check.

> Each teammate has its own context window. When spawned, a teammate loads the same project context as a regular session: CLAUDE.md, MCP servers, and skills. [...] A teammate also receives the spawn prompt from the lead. The lead's conversation history does not carry over.
> - Automatic message delivery: when teammates send messages, they're delivered automatically to recipients. The lead doesn't need to poll for updates.
> - Idle notifications: when a teammate finishes and stops, it automatically notifies the lead and includes its final answer in the notification. A teammate whose turn ends on an API error notifies the lead that it failed and includes the error text.
> - Shared task list: agents that have the Task tools can see task status and claim available work.
> - Teammate messaging: send a message to one specific teammate by name. To reach everyone, send one message per recipient.

> Agent teams use significantly more tokens than a single session. Each teammate has its own context window, and token usage scales with the number of active teammates. For research, review, and new feature work, the extra tokens are usually worthwhile. For routine tasks, a single session is more cost-effective.

```
Spawn three teammates to review PR #142:
- One focused on security implications
- One checking performance impact
- One validating test coverage
Have them each review and report findings.
```

```
Users report the app exits after one message instead of staying connected.
Spawn 5 agent teammates to investigate different hypotheses. Have them talk to
each other to try to disprove each other's theories, like a scientific
debate. Update the findings doc with whatever consensus emerges.
```

> The debate structure is the key mechanism here. Sequential investigation suffers from anchoring: once one theory is explored, subsequent investigation is biased toward it. With multiple independent investigators actively trying to disprove each other, the theory that survives is much more likely to be the actual root cause.

> There's no hard limit on the number of teammates, but practical constraints apply:
> - Token costs scale linearly: each teammate has its own context window and consumes tokens independently.
> - Coordination overhead increases: more teammates means more communication, task coordination, and potential for conflicts
> - Diminishing returns: beyond a certain point, additional teammates don't speed up work proportionally
>
> Start with 3-5 teammates for most workflows. This balances parallel work with manageable coordination. If you have 15 independent tasks, 3 teammates is a good starting point. Scale up only when the work benefits from having teammates work simultaneously. Three focused teammates often outperform five scattered ones.

> - Too small: coordination overhead exceeds the benefit
> - Too large: teammates work too long without check-ins, increasing risk of wasted effort
> - Just right: self-contained units that produce a clear deliverable, such as a function, a test file, or a review
>
> The lead breaks work into tasks and assigns them to teammates automatically. If it isn't creating enough tasks, ask it to split the work into smaller pieces. Having 5-6 tasks per teammate keeps everyone productive and lets the lead reassign work if someone gets stuck.

```
Wait for your teammates to complete their tasks before proceeding
```

> Two teammates editing the same file leads to overwrites. Break the work so each teammate owns a different set of files.

> Teammates may stop after encountering errors instead of recovering. [...] A message from the lead or another teammate wakes an in-process teammate that is waiting to retry a failed API request, so it retries immediately instead of waiting for the full retry delay. The lead can stop early too, deciding the team is finished before all tasks are actually complete. If that happens, tell it to keep going.

> Agent teams are experimental. Current limitations to be aware of:
> - No session resumption with in-process teammates: `/resume` and `/rewind` do not restore in-process teammates. After resuming a session, the lead may attempt to message teammates that no longer exist. If this happens, tell the lead to spawn new teammates.
> - Task status can lag: teammates sometimes fail to mark tasks as completed, which blocks dependent tasks.
> - Shutdown can be slow: teammates finish their current request or tool call before shutting down.
> - One team per session: a session has exactly one team, scoped to that session. You can't create additional named teams or share a team across sessions.
> - No nested teams: teammates cannot spawn their own teammates. Only the lead can manage the team.
> - No background subagents from in-process teammates: an in-process teammate's own subagents run in the foreground, because a teammate's background work can't outlive the lead's process.
> - Lead is fixed: the main session is the lead for its lifetime. You can't promote a teammate to lead or transfer leadership.
> - Permissions set at spawn.
> - Split panes require tmux or iTerm2: the default in-process mode works in any terminal. Split-pane mode isn't supported in VS Code's integrated terminal, Windows Terminal, or Ghostty.

> Next steps — Lightweight delegation: subagents spawn helper agents for research or verification within your session, better for tasks that don't need inter-agent coordination. Messaging between your own sessions: cross-session messaging lets Claude pass findings between the sessions you run yourself. Manual parallel sessions: Git worktrees let you run multiple Claude Code sessions yourself without automated team coordination.
