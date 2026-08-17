# Blueprint 6 - The MCP stack

## What it does
The set of Model Context Protocol servers that give Claude live hands: data sources, the web,
and the workspace. Registered in `.mcp.json` at the project root.

## The servers and what each is for
| Server | Use it for |
|---|---|
| **Companies House** | UK firmographics, officers, formations (Blueprint 2) |
| **Parallel Search** | ICP discovery with inline firmographics (Blueprint 4) |
| **Tavily** | News, funding, press, general web verification |
| **Firecrawl** | Scraping sites, careers pages, store locators |
| **Google Workspace** | Create sheets, Gmail drafts, Calendar (Blueprint 5) |
| (optional) **Slack / Notion** | Team comms + a knowledge hub, where used |

## How we used it
- **Free/verified-first ordering:** Companies House and Parallel Search (both free) did most of the
  work; Firecrawl (metered) and paid lookups came last.
- **The big cross-cutting lesson - the subagent MCP wall:** spawned subagents get
  **permission-denied** on several MCP tools (Companies House, Parallel Search). So **MCP-heavy work
  stays on the main thread**, and for bulk we drop to the **direct REST API** in a Python script
  (keys from `.env`). Don't fan MCP work out to subagents - they bail and waste tokens.
- **Per-tool quirks live in the relevant blueprint** (urlscan throttles, PB caps, Sheets create-gotcha).

## Blueprint: stand it up at a new company
1. Install the servers you need; register them in `.mcp.json` with full executable paths
   (so Claude's subprocess finds them regardless of PATH).
2. Put every secret in `.env` and reference it from `.mcp.json` env blocks - **never inline keys**
   in the committed file.
3. Decide the **free-first ordering** for the new ICP and write it into your skills/scripts.
4. Assume the **subagent wall**: design bulk work as main-thread REST scripts from day one.

## Gotchas / hard rules
- **Subagents can't use most data MCPs** - main thread for MCP, REST for bulk.
- **Full paths in `.mcp.json`**; secrets via `.env`, never committed.
- Interactively-authenticated servers (OAuth) can be absent in headless/cron runs - prefer
  service accounts / API keys for anything automated.

## Cost
Mostly free (CH, Parallel, Tavily free tiers). Firecrawl metered; the rest are subscriptions if used.
