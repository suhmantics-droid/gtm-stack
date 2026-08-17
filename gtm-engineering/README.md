# GTM Engineering System - index

Walk into any business, stand up signal-based revenue "plays", freeze the winners as skills.
This folder is the knowledge layer. Open `PLAYBOOK.md` first.

## What's in this folder (`gtm-engineering/`)
| File | What it is |
|---|---|
| `PLAYBOOK.md` | The framework: the loop, maturity rungs, engagement shape, hard rules, boundaries, geography, compliance |
| `PLAYS.md` | 12 reusable plays (signal → enrich → score → act → measure), tagged by runner status |
| `RESOURCES.md` | Voices, benchmarks, vendor map, signal sources, caveats |
| `MEASUREMENT.md` | How to close the loop: funnel, results sheet, kill-vs-scale |
| `ENGAGEMENT.md` | Packaging it as a freelance service: tiers, deliverables, sprint, pricing frame |
| `clients/_TEMPLATE.md` | Per-client brief (the single source of truth each skill reads/writes) |
| `EXAMPLE-audit.md` | A worked, filled-in audit |
| `target-lists/` | Generated prospect lists (CSV + markdown). First: `uk-saas-funded-2026-06` |

## Parts that live ELSEWHERE in this project
If you copy this folder to use the full system, you also need:
- **Skills** - `.claude/skills/gtm-audit/`, `gtm-play/`, `gtm-skill-builder/` (the `/gtm-*` commands)
- **Runner** - `gtm_formation_signal.py` at the project root (verified CH new-formations signal; play A1)
- **Shared infra** - `.env` (API keys), `service_account.json` (Sheets writes), the MCP servers in `.mcp.json`

## How it flows
`/gtm-audit <business>` → writes a client brief → `/gtm-play <play>` → runs + measures → `/gtm-skill-builder` → freezes the winner as a reusable skill. Repeat for the next play.

## Using this with a personal Claude account
- The docs (this folder) are plain markdown - open or upload them anywhere, including a claude.ai Project.
- To RUN plays you need the skills + `.env` keys + MCP servers on the machine you run from. Point Claude Code at this repo (or wherever you copy it) and the `/gtm-*` skills load from `.claude/skills/`.
- The target lists are saved as CSV so they open in Excel/Sheets without any Google account.
