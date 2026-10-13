---
title: "Pi Cheatsheet"
tags:
  - cheatsheet
  - help
created: 2026-08-27
type: cheatsheet
---

# Pi Cheatsheet

> [!nav]
> [[cheatsheets-hub|Cheatsheets]] [[_index|Home]]

**Pi** is a terminal AI agent. It's set up here to run [amosblomqvist's `learn`
config](https://github.com/amosblomqvist/learn) — a teaching system that explains
things from first principles, quizzes you, and draws diagrams into a note.

It runs in the **Koshi** vault, not this one. Koshi *is* the learning workspace;
this note is just where the manual lives.

## Start a session

```sh
cd ~/Documents/personal/obsidian/Koshi
tmux new -A -s pi 'pi'
```

**It has to run inside tmux.** Subagents open real tmux panes — outside tmux they
can't spawn and you silently lose the researcher and the diagram makers.

## The teaching loop

Just ask. The `teach` skill fires on anything explanation-shaped, so "explain TCP
handshakes" already gets the full treatment: unconditional truths first, then every
fact derived so you could have discovered it yourself.

| Command | What it does |
|---|---|
| `/skill:teach <topic>` | Force the teaching skill if a plain question got a plain answer |
| `/skill:visualize` | Force a diagram for what was just explained |
| `/md-log <path>` | Mirror the session into an Obsidian note — **the note must already exist** |
| `/md-unlog` | Stop mirroring |
| `/subagent <agent> <task>` | Spawn a subagent by hand |

Mid-lesson you'll get **popups**: quiz questions (graded, with the correct answer and
an explanation) and freeform questions from the agent. Answer them in the TUI — they
block until you do.

The usual shape of a session:

1. `cd` to Koshi, start pi in tmux
2. Create the lesson note in Obsidian first, then `/md-log notes/whatever.md`
3. Ask your question
4. Answer the quizzes as they come
5. The note fills in as you go, diagrams embedded inline

## Subagents

Three, defined in `.pi/agents/`. They run in their own tmux pane (a right split) and
steer their result back when done, so the main session stays interactive.

| Agent | Does | Tools |
|---|---|---|
| `researcher` | Web research and fact-checking | `websearch`, `webfetch`, `safe_bash` |
| `mermaid-maker` | Nodes-and-edges diagrams — dependency graphs, flows, sequences, state machines | `write_mermaid`, `render_mermaid` |
| `svg-maker` | Positions-and-shapes — geometry, number lines, vectors, plots | `write_svg`, `render_svg` |

Both makers **render the image and look at it** before returning, then publish the PNG
into the vault so it embeds inline in the log.

| Tool | What it does |
|---|---|
| `subagents_list` | Show which agents are available |
| `subagent_message` | Send a running subagent more instructions |

## Keys

| Key | Does |
|---|---|
| `Esc` | Interrupt the agent |
| `Ctrl+C` / `Ctrl+D` | Clear / exit |
| `/` | Commands |
| `!` | Run a bash command |
| `Ctrl+O` | Full startup help and loaded resources |
| `Ctrl+P` | Cycle models |

## Models and what they cost

| Model | Cost | Use |
|---|---|---|
| `google/gemini-3.7-flash` | **Free tier** — no card | Default. Everything runs on this. |
| `google/gemini-3.6-flash` | Free tier | Fallback if 3.7 gets rejected (2.5 is retired — 404) |
| `anthropic/claude-*` | **Bills per token** | Only if a lesson genuinely needs it |

The free tier is roughly **1,500 requests/day and 15/minute**, Flash-class only — Pro
models left the free tier in April 2026.

> [!warning] The Claude fallback is not free
> Your Claude subscription does **not** cover pi. Since April 2026 Anthropic bills
> third-party tools from *extra usage*, per token, not your plan limits. `Ctrl+P` to
> Claude is a spending decision, not a quality toggle. The warning pi prints at startup
> is telling you exactly this.

## Where everything lives

| Path | What |
|---|---|
| `~/Documents/personal/obsidian/Koshi/.pi/` | The whole learn config (a git clone) |
| `.pi/agents/*.md` | The three subagents — model and tools in frontmatter |
| `.pi/skills/teach/`, `.pi/skills/visualize/` | The teaching philosophy and the diagram rules |
| `.pi/extensions/` | `ask-user-question`, `quiz`, `md-log`, `visual-tools` |
| `~/.pi/agent/settings.json` | Default model, installed packages |
| `~/.pi/agent/auth.json` | Credentials |
| `~/.local/bin/pi` | Shim that forces pi to run under Node 22 |

To change which model an agent uses, edit `model:` in its `.md` frontmatter. To change
the session default, edit `defaultModel` in `~/.pi/agent/settings.json`.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `npm warn EBADENGINE` / old version banner | Old pi on Node 20. `rehash`, then `pi --version` should say 0.84.3+ |
| `[Extensions]` list is missing entries | The project isn't trusted — accept the prompt on first launch in that directory |
| Subagents don't spawn | You're not inside tmux |
| Status bar shows a `claude-*` model | The session drifted onto Anthropic auth. `Ctrl+P` to a `google/` model, or check `.pi/settings.json` |
| "Working..." forever, no output | Check the status bar model first — a hung Anthropic call looks identical to thinking. `Esc` to interrupt |
| 429 / quota errors | Free tier is 15 req/min. Several subagents at once will trip it — wait, or `Ctrl+P` |
| Model rejected as unavailable | `sed -i 's|gemini-3.7-flash|gemini-3.6-flash|' ~/Documents/personal/obsidian/Koshi/.pi/agents/*.md` |
| Researcher comes back empty | Web tools are `websearch`/`webfetch` (one word). If it's flaky, swap to [pi-web-access](https://github.com/nicobailon/pi-web-access), which keeps its tools always on |
| `/md-log` says file does not exist | It links to an existing note, it never creates one. Make the note first. |

> [!indexcard] Things I always forget
> - Run it from **Koshi**, inside **tmux**
> - `/md-log` needs the note to exist first
> - Free tier is 15 requests/minute — parallel subagents trip it
> - Claude costs real money here; Gemini doesn't

## Reference
- [pi](https://github.com/earendil-works/pi) — the agent
- [learn](https://github.com/amosblomqvist/learn) — the teaching config, and [the video](https://www.youtube.com/watch?v=kzcI5F4tGiU) behind it
- [pi-interactive-subagents](https://github.com/amosblomqvist/pi-interactive-subagents) — tmux subagents
- [Gemini free tier limits](https://ai.google.dev/gemini-api/docs/rate-limits)


> [!nav]
> [[cheatsheets-hub|Cheatsheets]] [[_index|Home]]
