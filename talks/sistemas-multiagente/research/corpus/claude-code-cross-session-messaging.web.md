---
source_file: claude-code-cross-session-messaging
source_type: web-capture
ingested_at: 2026-10-04
---

# Message your other Claude Code sessions (Claude Code Docs — "Cross-session messaging")

## Provenance
- Original location: web/claude-code-cross-session-messaging/ (text from `page.md`, 36 KB; `original.html` not needed as fallback — `page.md` has full headings and body)
- Format: html (web capture via talksmith:ingest)
- URL: https://code.claude.com/docs/en/cross-session-messaging
- Author / source (if known): Anthropic, Claude Code official documentation (section "Agents and parallel work")
- Date of original (if known): not stated on page; captured 2026-10-04T19:33:09Z (HTTP 200, 588,959 bytes). Page references Claude Code versions v2.1.224 to v2.1.248.
- Companion of `claude-code-agent-teams.web.md` (the agent-teams page links here for "separate sessions that pass messages to each other without a team").

## Key claims
- "Cross-session messaging lets Claude deliver a message from one of your Claude Code sessions to another." Requires Claude Code v2.1.224+ on macOS/Linux/WSL 2, v2.1.234+ on native Windows. "When a session meets the requirements, messaging is on with nothing to enable." (Unlike agent teams, it is not behind an experimental flag.)
- "A message is a piece of text one Claude writes to another, never the sender's conversation history or files. To move a whole conversation or its context, resume the session instead."
- Claude can send a message **on its own** when it sees the need (e.g., after a change that affects another session's work), or when the user asks. Claude discovers targets with `ListAgents` and sends with `SendMessage`; the user never calls either tool.
- Use cases: hand over a finding; coordinate parallel worktrees; get status from long-running work; message across machines (other machines or cloud).
- Target by `@`-mention of the session's name (v2.1.232+), e.g. "Let @api-worker know the schema migration finished"; names with spaces use quotes (`@"release notes"`); if several live sessions share the name, Claude asks which one.
- **Delivery semantics ("waking")**: "The receiving Claude reads the message between tool calls during an active turn, so a running tool is never interrupted. When the receiving session is idle, Claude Code starts a new turn with the message." Messages arrive as plain text; `@` file/MCP mentions inside are not attached.
- Each arriving message ends **Delivered**, **Held** (until user approves or a mode/settings change allows), or **Refused** (dropped). Sender-side refusals: over size cap, rapid burst limit, target listed as unable to receive, reply target fails a safety check (e.g., symlinked).
- Once delivered, a message "counts toward usage like a prompt you type," and the receiver can reply (except one-way cross-machine messages).
- Permission boundaries stay per-session: Claude is instructed never to ask another session for an action denied/blocked in its own session, and the receiver's own permission prompts and rules apply.
- **Idle notice** (`SendMessage` input `notify_when_idle`, v2.1.236+ in both sessions): Claude can ask a local session to send one notice when it next goes idle (finished a turn with nothing queued) or exits. Subscribing on its own "without starting a turn or spending tokens in the watched session"; immediate notice if already idle; subscription dropped after **12 hours** without a notice. "Only the Claude in your main conversation can subscribe, and only to your sessions on this machine" — asking a teammate, subagent, or remote session for a notice refuses the whole call.
- `/list-agents` (alias `/peers`) shows what Claude can reach: subagents, the session's own agent-team teammates, other local sessions (incl. background sessions; only those binding an inbox socket), cloud sessions and Remote Control sessions on other machines (only while connected to Remote Control).
- Transport: same machine → per-session Unix domain socket (macOS/Linux) or named pipe (Windows), "never through Anthropic servers"; another machine → through Anthropic servers over that machine's Remote Control connection; cloud → through Anthropic servers straight to the cloud session.
- Isolation boundaries: container vs. host sessions cannot reach each other; WSL 2 vs. native Windows sessions on the same computer cannot either. Without Remote Control, a message to a remote session goes one-way (no reply address).
- **Inbound message safety**: "Claude Code tells B's Claude that the message came from another session, not from you"; a message can't approve anything, can't change configuration (permission settings, `CLAUDE.md`), slash commands in it don't run, and permission prompts still fire.
- `crossSessionInbound`: `accept` / `hold` / `refuse`. With no value set, the default depends on the two sessions' permission-mode classes (bypassing vs. prompting): a prompting receiver delivers unless the sender bypasses; a bypassing receiver holds unless the sender also bypasses. Held messages open an approval dialog (Approve / Deny), dropped after `dialogExpiry` (default 5 min); at most 100 held messages, oldest dropped.
- Non-interactive `claude -p` sessions bind an inbox socket and can receive messages ("a long-running `-p` worker can receive messages and appears in the listing"); bare mode does not. To let a `-p` worker take messages unattended, start it with `crossSessionInbound: accept` in its `--settings`.
- Scripts/hooks can post into their own session via `CLAUDE_CODE_MESSAGING_SOCKET` (+ optional/required `CLAUDE_CODE_MESSAGING_TOKEN` auth line); socket restricted to the OS user; connection closed if no complete line within 30 s; own-child messages delivered by default when verifiable.
- Restrictions: `isolatePeerMachines: true` requires approval before any message leaves the machine (even in `bypassPermissions`); `refuse` stops receiving; deny rules on `SendMessage` and `ListAgents` stop sending/listing. "Denying `SendMessage` also removes messaging to subagents and agent-team teammates, since the same tool serves both."
- Limitations: plain text only ("Structured agent team protocol messages stay within a team"); same-machine message capped at ~1 million serialized characters; rapid bursts refused at sender; message loops throttled (per-sender rate limit, identical repeats dropped, at most 50 accepted messages queued) — "A message loop between two sessions therefore stops on its own."

## Definitions and terminology
- **Cross-session messaging**: delivering text from one Claude Code session to another of the same user's sessions (local, other machine, or cloud), without a team.
- **`ListAgents` / `SendMessage`**: the tools Claude uses to discover targets and send. `SendMessage` is the same tool used for subagents and agent-team teammates.
- **Session name**: set with `/rename` or `--name`, otherwise generated by Claude Code; duplicate names on the same machine get renamed to a variant (with exceptions).
- **Inbox socket / Peer address**: per-session Unix socket (or Windows named pipe) where local messages are delivered; shown in `/status` as `Peer address` (`uds:` prefix); fallback directory `/tmp/cc-socks-<uid>`.
- **Remote Control**: connection that lets a session reach the user's sessions on other machines and in the cloud (requires claude.ai sign-in; not available with an API key or on Bedrock / Claude Platform on AWS / Google Cloud Agent Platform / Microsoft Foundry).
- **Idle**: "the session finished a turn with nothing queued."
- **Held / Delivered / Refused**: the three outcomes of the inbound check.
- **`crossSessionInbound`, `isolatePeerMachines`, `dialogExpiry`**: the settings that govern inbound policy, cross-machine approval, and how long held messages wait.
- **One-way cross-machine message**: sent to a remote session from a session not connected to Remote Control; carries no reply address.

Transport table (reconstructed from flattened capture):

| Where the other session runs | How the message travels |
|---|---|
| On this machine | Over a per-session socket on macOS and Linux, or a per-session named pipe on native Windows, never through Anthropic servers |
| On another of your machines | Through Anthropic servers, arriving over that machine's Remote Control connection |
| In the cloud | Through Anthropic servers, straight to the cloud session |

Inbound control table (reconstructed):

| Value | Behavior |
|---|---|
| `accept` | Claude Code delivers each message to Claude |
| `hold` | Claude Code shows a notice for each message and doesn't deliver it. If an `accept` later applies, per the precedence rules, Claude Code releases the held messages |
| `refuse` | Claude Code drops each message without delivering it |

## Evidence and examples
- User prompts (typed by the user, not messages): "Ask the session running in my other terminal whether the migration finished"; "Explain what we just did to the session working on the payments API"; "Let @api-worker know the schema migration finished"; "Tell me when the migration session finishes what it's working on".
- Example message as received (one Claude to another): "Schema migration finished / The new column is tenant_id, and rebasing on main is safe now." Shown as a dim preview line: `› Message from @api-worker: Schema migration finished (ctrl+o to expand)`.
- Org-wide shutdown via managed settings: `{"permissions": {"deny": ["SendMessage", "ListAgents"]}, "crossSessionInbound": "refuse"}`.
- Version gates: v2.1.224 (base, macOS/Linux), v2.1.225 (start conversations with other machines), v2.1.232 (@-mention, `/config` row), v2.1.234 (native Windows), v2.1.236 (idle notice), v2.1.248 (same-machine on third-party providers / flag fetching off).

## Inconsistencies / open questions
- [verified] OS availability is stated two ways on the page: the opening note and the Availability heading list macOS and Linux/WSL 2 with v2.1.224 and native Windows with v2.1.234, while the Availability bullet says simply "available on macOS, Windows, and Linux". These are consistent (Windows needs the later version) — checked both passages; a slide should keep the version split if it cites versions.
- [verified] This page and the agent-teams page draw the team boundary sharply in one respect: cross-session messages are plain text only, while "Structured agent team protocol messages stay within a team" (plan approvals, shutdown requests) — checked Limitations here against the Architecture section of `claude-code-agent-teams.web.md`. Relevant if the class contrasts "team" vs "independent sessions that message each other."
- [verified] The idle notice is restricted: only the main-conversation Claude can subscribe, and only to local sessions; a teammate or subagent target refuses the whole call — checked in "Limits". So "the lead gets woken when a worker session finishes" works for local sessions, not via this mechanism for teammates (teammates have their own idle notifications, per the agent-teams page).
- [open question] Version numbers and feature behavior reflect the page as captured on 2026-10-04; re-check the live page before a live demo (especially whether `/list-agents` / `@`-mentions behave as described in the installed Claude Code version — run `claude --version` and `/list-agents`).
- [open question] Remote Control, background sessions ("agent view"), and Channels are linked but not described; if the class demos cross-machine or background workers, those pages would need capturing.
- [open question] Capture artifacts: doubled backticks before links (e.g. ``[crossSessionInbound]``) and nested sub-bullets flattened; content intact.

## Images / diagrams

### claude-code-cross-session-messaging.web/images/light.svg
- Provenance: `web/claude-code-cross-session-messaging/assets/light.svg`, site header logo (alt "light logo") of Claude Code Docs. Decorative chrome, not content.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

### claude-code-cross-session-messaging.web/images/dark.svg
- Provenance: `web/claude-code-cross-session-messaging/assets/dark.svg`, site header logo (alt "dark logo"), dark-theme variant. Decorative chrome, not content.
- Depiction: Decorative site chrome — not transcribed (presenter decision 2026-10-04)
- Why it matters: n/a
- Transcribed text: n/a

## Raw / preserved excerpts

> Cross-session messaging requires Claude Code v2.1.224 or later on macOS and Linux, including Linux inside WSL 2. On native Windows, it requires Claude Code v2.1.234 or later. When a session meets the requirements, messaging is on with nothing to enable. [...] Cross-session messaging lets Claude deliver a message from one of your Claude Code sessions to another. When a change in one session breaks what another is building on, Claude can warn that session before you notice. When one session settles a question another is blocked on, Claude can send the answer across. A message is a piece of text one Claude writes to another, never the sender's conversation history or files. To move a whole conversation or its context, resume the session instead.

> Use messaging when one of your sessions has something another session needs mid-task. Claude can send a message on its own when it sees the need, for example after making a change that affects work another session is doing, or you can ask it to send one. The common cases:
> - Hand over a finding: when one session discovers a breaking change or makes a decision, Claude summarizes it for the session working on the affected area, instead of you re-explaining it there.
> - Coordinate parallel worktrees: when sessions work the same repository in separate worktrees, Claude can tell the other sessions what landed.
> - Get status from long-running work: have a migration or test run report back to the session you're watching, or ask it yourself from there. If that session is on this machine, Claude can also ask it for one notice when it next goes idle or exits.
> - Message across machines: reach one of your sessions on another machine or in the cloud.

> When one of your sessions learns something another session needs, such as a finding, a status, or a decision, Claude passes it along instead of you copy-pasting between terminals. Claude discovers the target with `ListAgents` and sends with `SendMessage`, so you never call either tool yourself. Claude can decide to send a message without being asked, and you can also prompt for one.

```
Ask the session running in my other terminal whether the migration finished
```

```
Explain what we just did to the session working on the payments API
```

```
Let @api-worker know the schema migration finished
```

> The receiving Claude reads the message between tool calls during an active turn, so a running tool is never interrupted. When the receiving session is idle, Claude Code starts a new turn with the message. A message from another session arrives as plain text.

> The receiving session checks each arriving message against its own inbound controls, and the check ends in one of three outcomes:
> - Delivered: Claude Code passes the message to the receiving Claude.
> - Held: Claude Code sets the message aside undelivered. A held message reaches Claude only when you approve it or a later mode or settings change allows it.
> - Refused: Claude Code drops the message without delivering it.
>
> Once delivered, the message counts toward usage like a prompt you type, and the receiving Claude can reply to the sender the same way, except in the one-way cross-machine case. Permission boundaries stay per-session. Claude is instructed never to ask another session for an action that was denied or blocked in its own session, or that its own permission settings would block, and to route that work back to you instead.

> Claude can ask one of your sessions on this machine to send back one notice when that session next goes idle or exits. Idle here means the session finished a turn with nothing queued. Use it when you're waiting on a long task in another session and want to hear when it's done instead of checking. Requires Claude Code v2.1.236 or later in both sessions.

```
Tell me when the migration session finishes what it's working on
```

> Claude subscribes with the `SendMessage` tool's `notify_when_idle` input, either attached to a message it's sending anyway or on its own. On its own, Claude Code subscribes without starting a turn or spending tokens in the watched session, and sends the notice right away if that session is already idle. Attached to a message, Claude Code delivers the message first and sends the notice later.

> If no notice arrives within 12 hours, Claude Code drops the subscription and tells Claude, so it doesn't keep waiting. [...] Only the Claude in your main conversation can subscribe, and only to your sessions on this machine. When Claude asks for a notice from any other target, such as a teammate, a subagent, or a session beyond this machine, Claude Code refuses the whole call, including any message attached to it.

> - Subagents: agents running inside the current session.
> - Teammates: this session's own agent team teammates.
> - Your other local sessions: Claude Code sessions running on the same machine, including background sessions. A session appears only when it binds an inbox socket.
> - Your cloud sessions: shown while this session is connected to Remote Control.
> - Your Remote Control sessions on other machines: shown while this session is connected to Remote Control, and labeled `Remote Control`. Claude Code shows `offline` as the status of a session whose Remote Control connection has dropped.

> When session A messages session B, Claude Code tells B's Claude that the message came from another session, not from you, and limits what the message can do:
> - It can't approve anything: a message from another session never counts as your consent, so it can't answer a pending permission prompt on your behalf.
> - It can't change configuration: Claude Code instructs the receiving Claude never to change permission settings, `CLAUDE.md`, or other configuration because another session asked.
> - Commands don't run: a command in the message's text, such as `/compact`, arrives as plain text. Claude Code never executes it.
> - Permission prompts still fire: if acting on the message requires a permission the receiving session doesn't have, you see the same prompt you'd see for any other work.

```
Schema migration finished
The new column is tenant_id, and rebasing on main is safe now.
```

> When no value applies, Claude Code decides per message from the two sessions' permission modes. It groups sessions that bypass permission prompts into one class, and every other session into the other. [...]
> - The receiving session prompts for permissions: Claude Code delivers each message. It holds one for your approval only when the sending session identifies itself as bypassing permission prompts.
> - The receiving session bypasses permission prompts: Claude Code holds each message for your approval. It delivers one only when the sending session identifies itself as also bypassing.

> Claude Code binds an inbox socket for a `claude -p` session like an interactive one, so a long-running `-p` worker can receive messages and appears in the listing. When you start a session in bare mode, Claude Code doesn't bind the socket, so that session can't receive messages and doesn't appear in the agent list. [...] To let a `-p` worker take messages unattended, start it with `crossSessionInbound` set to `accept` in its `--settings` value.

```json
{
  "isolatePeerMachines": true
}
```

```json
{
  "permissions": {
    "deny": ["SendMessage", "ListAgents"]
  },
  "crossSessionInbound": "refuse"
}
```

> With this in place, Claude Code still binds each session's inbox socket, but drops every message that arrives on it without delivering anything to Claude. Denying `SendMessage` also removes messaging to subagents and agent-team teammates, since the same tool serves both.

> - Plain text only: Claude sends only plain text across sessions. Structured agent team protocol messages stay within a team.
> - Same-machine message size is capped: Claude Code refuses a message to a session on this machine once its serialized form passes about a million characters. [...] Nothing reaches the receiving session.
> - Rapid bursts to one session are refused at the sender: once a rapid burst of messages to a session on this machine reaches what that session's inbox accepts, Claude Code refuses further sends in the sending session. The refusal names the burst and tells Claude to batch the rest into one message or wait.
> - Message loops are throttled: in the receiving session, Claude Code rate-limits repeated messages per sender, drops identical repeats arriving within a short window, and queues at most 50 accepted messages for Claude to read. A message loop between two sessions therefore stops on its own.
