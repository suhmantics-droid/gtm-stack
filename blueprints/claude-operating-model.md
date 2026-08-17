# Blueprint 8 — The Claude operating model (skills + memory + CLAUDE.md)

## What it does
The meta-blueprint: how Claude Code itself was set up to run all of the above as a repeatable
operation, so a new person (or a new employer) can rebuild the *way of working*, not just the tools.

## The three pillars
- **`CLAUDE.md`** (project root) — the always-loaded brief: what the project is, the providers,
  the data shape, the plan. The single doc that orients every session.
- **Skills** (`.claude/skills/<name>/SKILL.md`) — one-command workflows (`/enrich`, `/qualify-batch`,
  `/gtm-audit`, …). Each is a frozen, proven pipeline with its own hard rules and run commands.
- **Memory** (`memory/` + `MEMORY.md` index) — durable facts, preferences, and lessons that persist
  across sessions: tool quirks, guardrails, what worked, what didn't.

## How we used it
- **Lessons became memory; proven pipelines became skills.** Every non-obvious thing we learned
  (the NXDOMAIN bust, the subagent MCP wall, the Sheets create-gotcha, throttle limits) was written
  to memory so it never had to be re-learned. Every workflow we ran more than a few times was frozen
  into a skill.
- **Hard rules were enforced in code and in every skill**, not left to good intentions: no guessed
  data, per-call OK for spend, new-sheet-never-overwrite, drafts-not-sends.
- **`update-config` / settings** handled the automation that memory can't (hooks, permissions),
  since the harness — not the model — runs "whenever X, do Y" behaviours.
- **Skills were built with `skill-creator`** and kept namespaced so company-specific ones never
  shadowed generic tooling.

## Blueprint: stand it up at a new company
1. Run `/init` to write a fresh `CLAUDE.md` describing the new project, providers, and data shape.
2. Seed `memory/` with the standing guardrails (copy the "rules that survive any move" from the
   blueprints index) + the new employer's voice/ICP facts.
3. Port the **generic** skills (enrichment, qualification, discovery, GTM-E); rebuild only the
   company-specific ones (house voice, ICP tiers).
4. Register the MCP stack (`.mcp.json`) and keys (`.env`) per Blueprint 6.
5. As you work: **write lessons to memory in the moment**, and **freeze proven workflows into skills.**
   That loop is the actual asset — it compounds wherever you go.

## Gotchas / hard rules
- **Automation needs hooks, not memory** — "every time / whenever" behaviours live in settings.json.
- **Don't write memory autonomously** for trivia — capture reusable facts, surfaced and confirmed.
- **Keep secrets out of committed files** — `.env` + `.gitignore`, always.
- Namespace company-specific skills so they don't collide when you move.

## Cost
Free (it's configuration). The cost is discipline: actually writing the lessons down and freezing
the winners. That discipline is what makes the whole thing portable.
