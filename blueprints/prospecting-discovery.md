# Blueprint 4 — Prospecting & discovery (finding NEW companies)

## What it does
Generates *new* companies that match an ICP — versus enriching ones you already have. Best when
the discovery method carries a **signal** (recently funded, hiring, new formation) so the list
arrives with the story already attached.

## Tools / scripts
- **Parallel Search MCP** (`mcp__parallel-search__web_search`) — best for ICP discovery; LinkedIn-company
  excerpts include `employee_count` / `founded_year` / `country_iso` inline.
- **Tavily MCP** — news/funding/press discovery and verification.
- **Firecrawl MCP** — careers pages, store locators, site content.
- **Phantom Buster** — LinkedIn / Sales Navigator scrapers ("Phantoms"), triggered via API.
- Signal runner: `gtm_formation_signal.py` (new UK formations). Funding lists pulled from
  reputable sources (Vestbee, The SaaS News, etc.) with each round cited.

## How we used it
- **Parallel Search was the surprise winner for discovery** — its inline firmographics gave a
  ~100% in-ICP hit rate for SMB discovery, versus a much lower hit rate when we asked a LinkedIn
  scraper to backfill employers from contact URLs.
- **Signal-led lists beat flat lists.** A "recently raised seed/Series A" list comes with budget +
  timing built in; a "hiring a CRM manager" list comes with intent. We always paired discovery with
  a reason-to-reach-out and cited the source per row (no guessed data).
- **Phantom Buster quirks we hit:** LinkedIn People Search **rejects boolean queries** (parens+AND)
  — use a single quoted phrase + a `geoUrn`. Account-safety cap ~**200 results/launch, ≤4 launches/day**.
  Some configured Phantoms get stuck and can't launch — keep a note of which IDs actually work.
- **Subagents can't use Parallel Search** (permission wall) — discovery runs on the main thread.

## Blueprint: stand it up at a new company
1. Write the ICP as a query: vertical + size band + geography + a signal.
2. **Prefer Parallel Search** for cold discovery (firmographics inline = instant qualification).
   Use Tavily for funding/press signals, Firecrawl for site-derived signals.
3. Only reach for Phantom Buster when you specifically need LinkedIn-scraped fields, and respect
   the per-day caps and the boolean-query limitation.
4. Cite the signal source on every row. Then hand the list to enrichment (Blueprint 1) — gated.

## Gotchas / hard rules
- **Discovery on the main thread** — subagents hit the MCP permission wall.
- **No guessed companies/data** — every row needs a real, sourced signal.
- **Respect scraper caps** (Phantom Buster ≤4 launches/day) — over-running risks the account.
- LinkedIn-URL → employer backfill is **weak** in Parallel; it shines at *discovery*, not backfill.

## Cost
Parallel Search and Tavily have free tiers; Firecrawl is metered; Phantom Buster is subscription.
Lead with the free discovery sources.
