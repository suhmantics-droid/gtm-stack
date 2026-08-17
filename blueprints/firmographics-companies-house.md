# Blueprint 2 - Firmographics (Companies House, UK)

## What it does
Pulls verified company facts for UK entities - legal name, status, size class, incorporation date,
SIC codes, officers/directors, persons with significant control, charges/filings - and surfaces
**new-formation** and **officer-change** signals.

## Tools / scripts
- **Companies House MCP** (`mcp__companies-house__*`) - good for small, interactive lookups.
- **Companies House REST API** - for bulk. Key `COMPANIES_HOUSE_API_KEY`, HTTP Basic auth
  (key as username, empty password). Base `https://api.company-information.service.gov.uk`.
- Scripts: `events_ch_lookup.py` (name → size-class, the reference pattern), `gtm_formation_signal.py`
  (new incorporations by SIC + date window, via `/advanced-search/companies`).

## How we used it
- **Size-class derivation** from `accounts.last_accounts.type` + company type, falling back to
  officer count when accounts were absent (≤5 officers ≈ SMB, ≤20 ≈ Mid, else Enterprise).
- **Bulk via REST, not the MCP.** The MCP is fine for a handful, but for hundreds we hit a wall:
  **spawned subagents get permission-denied** on CH MCP tools. The fix was a direct-REST Python
  script on the main thread. Benchmark: **449 companies size-classed in ~4 minutes** at 4 threads.
- **New-formation signal** (`gtm_formation_signal.py`): query `/advanced-search/companies` with
  `sic_codes` + `incorporated_from` → a list of brand-new companies in a target vertical, before
  anyone else is calling them. Verified live against the API.

## Blueprint: stand it up at a new company
1. Get a free CH API key, add `COMPANIES_HOUSE_API_KEY` to `.env`.
2. For interactive use, the MCP is enough. For anything bulk, copy the REST pattern from
   `events_ch_lookup.py` (env loader → `auth=(KEY, "")` → 429 retry → `ThreadPoolExecutor`).
3. Pick the SIC codes that map to the new ICP - that's the one company-specific input.
4. For signals, schedule `gtm_formation_signal.py` (or an officer-change poller) on a cadence.

## Gotchas / hard rules
- **UK only.** No equivalent for US/EU here - outside the UK, fall back to Parallel/Tavily/Firecrawl.
- **Subagents can't use the CH MCP** - use REST for bulk, keep MCP calls on the main thread.
- Rate limit **600 requests / 5 min**; 4 threads is safe.
- `search_companies` returns candidates - always best-match (active status + normalised-name overlap)
  before trusting a result; don't grab the first hit blindly.

## Cost
**Free.** This is the highest-value free firmographic source in the stack for UK work.
