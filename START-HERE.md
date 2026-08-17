# START HERE - GTM Engineering stack (portable)

**You (Claude): read this file and set up everything below. Confirm before anything that installs
software, spends money, or needs my credentials.**

This is a self-contained, company-agnostic GTM-engineering toolkit. Point a fresh Claude Code
session at this folder and paste the kick-off prompt below.

---

## The kick-off prompt (copy-paste this into a fresh Claude Code session in this folder)

```
Read START-HERE.md in this folder and set up the entire GTM Engineering stack exactly as it
specifies. Work through its Setup Checklist in order (steps 1-7). For EACH step, do it then report
status: done / needs-my-input / skipped-and-why.

Before anything that installs software, registers an MCP server, writes a secret, edits a config
file, or spends money, STOP and ask me first. Never skip a step silently, and never guess or fake a
key, path, or account you don't have - pause and ask.

Also read blueprints/README.md and gtm-engineering/PLAYBOOK.md so you understand the system.

When finished: (1) run the free verification step and show the output; (2) give me a checklist of
every step done vs pending and exactly what you still need from me; (3) list the files you read so I
can confirm nothing was missed.
```

---

## What this is
A portable system for walking into any business and standing up signal-based revenue "plays",
plus the full tradecraft behind it. No company's private data is in here - only method, tooling,
and templates.

## What's in this folder
| Path | What |
|---|---|
| `blueprints/` | 21 how-to blueprints + glossary - the full tradecraft. Start at `blueprints/README.md`. |
| `gtm-engineering/` | The audit → play → freeze system. Start at `gtm-engineering/README.md`, then `PLAYBOOK.md`. |
| `skills/` | The 3 generic skills: `gtm-audit`, `gtm-play`, `gtm-skill-builder`. |
| `scripts/` | Runnable: `gtm_formation_signal.py` (CH signal), `sheets_api.py`, `sheets_helper.py`, `derive_domains.py`. |
| `.env.example` | The API keys to fill in. |
| `.mcp.json.example` | The MCP servers to register. |

---

## Setup checklist (run these in order)

### 1. Prerequisites
- **uv** (Python runner) - https://docs.astral.sh/uv/ . Scripts run via `uv run --with <pkg> python ...`, so no global pip installs.
- **Node.js** (for the npx-based MCP servers: firecrawl, tavily, companies-house).
- Confirm both are installed before continuing.

### 2. API keys → `.env`
- Copy `.env.example` to `.env` in this folder.
- Fill in the keys you have. All are free-tier capable except where noted. Parallel Search needs no key.
- `.env` is secret - never commit it.

### 3. MCP servers → `.mcp.json`
- Copy `.mcp.json.example` to `.mcp.json`.
- **Update every absolute path** to where this folder actually lives on this machine, and to the local
  `uvx`/`npx` paths. Update the `-e <path>\.env` references to this folder's `.env`.
- Restart Claude Code so the servers load.

### 4. Google Workspace (Sheets / Gmail / Calendar) - optional but recommended
- For **Sheets writes**, set up a **service account** (most reliable): create one in Google Cloud,
  download its JSON to `service_account.json`, enable the Sheets + Drive APIs. See
  `blueprints/data-home-google-sheets.md`.
- For **creating sheets / Gmail / Calendar**, the workspace MCP uses OAuth - point
  `GOOGLE_CLIENT_SECRET_PATH` at your downloaded `client_secret` JSON.
- Note the gotcha (documented): a service account **can't create** new sheets - create via the MCP, write via the service account.

### 5. Skills → make them loadable
- Claude Code discovers skills in a `.claude/skills/` folder. Copy `skills/gtm-audit`, `skills/gtm-play`,
  `skills/gtm-skill-builder` into `.claude/skills/` at your project root (or symlink them).
- The `/gtm-audit`, `/gtm-play`, `/gtm-skill-builder` commands will then be available.

### 6. Fix hard-coded paths in the scripts
- The scripts resolve paths from the repo root and read config from environment variables. Override
  in each `scripts/*.py` to this folder's location, or they'll read the wrong `.env`/output dir.

### 7. Verify (free, no spend)
- Run the Companies House signal runner - it's free and proves the whole chain (env → API → output):
  ```
  uv run --with requests python scripts/gtm_formation_signal.py --sic 47710 --days 14 --limit 5
  ```
- A short list of real new companies = the stack is live.

---

## How to use it once set up
1. Read `gtm-engineering/PLAYBOOK.md` (the framework) and `blueprints/README.md` (the tradecraft).
2. `/gtm-audit <a business>` → writes a client brief + a ranked play roadmap.
3. `/gtm-play <play>` → runs + measures one play (spends only with your OK).
4. `/gtm-skill-builder` → freezes a winning play into a reusable skill.

## What's deliberately NOT in here
- **No company's private data** - no prospect lists, case studies, brand assets, or house voice.
  Those are rebuilt per employer (see `blueprints/client-onboarding.md`).
- **No secrets** - you supply your own keys in `.env`.
- **Company-specific skills** (a house-voice outreach skill, ICP-specific tiering) are rebuilt fresh;
  the blueprints tell you how. `gtm-engineering/EXAMPLE-audit.md` is an illustrative worked
  example only - replace it with your own.

## The rules that travel with this stack (non-negotiable)
- No guessed data · Per-call OK for spend · New sheet never overwrite · Drafts not sends ·
  Signal-based or it's not a play · Free/verified-first. (Full list: `blueprints/README.md`.)
