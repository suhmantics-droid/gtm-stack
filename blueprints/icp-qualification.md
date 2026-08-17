# Blueprint 3 - ICP qualification (tech-stack → tiering → call sheet)

## What it does
Takes a list of companies, detects the marketing/commerce tech each one runs, scores them by
ICP fit, and writes a sorted call sheet. Turns a flat list into a prioritised "call these first".

## Tools / scripts
- **urlscan.io** - martech/tech fingerprinting from a domain (header `API-Key`). Free tier.
- Scripts: `urlscan_run.py`, the `dotdigital_scan*.ps1` family (submit / fetch / top-up),
  `derive_domains.py` (LinkedIn-company URL → root domain), `build_callsheet.py`.
- Cache: `urlscan_results.json`, keyed so a domain is never re-scanned.
- Skill: `/qualify-batch` wraps the whole flow.

## How we used it
- **Detect, then tier.** A detected enterprise CRM/ESP (e.g. the platforms your product integrates
  with or displaces) + the right vertical + a size proxy = Tier 1. Vertical but no detected stack =
  cold/discovery tier. Out-of-ICP = parked. **Never tier something Tier 1 without a real signal.**
- **Throttle hard.** urlscan free tier is **50 scans/day, 5/min**. We learned to leave **≥13s
  between submits** and **≥1.5s between fetches** - tighter trips 429s after ~5 scans.
- **Cache by domain-root.** Dedup `www.`, `shop.`, `m.` to one root so two contacts at the same
  company cost one scan. The enrichment pipeline reads the same cache.
- **Lesson on partner/old lists:** re-qualifying a 2-year-old "runs platform X" partner list found
  **~82% had churned** off it. Always re-qualify before pitching a stack-based angle.
- **Sheet gotcha:** write the phone column as **RAW** so `+44…` stays literal - `USER_ENTERED`
  reads the leading `+` as a formula and throws a parse error.

## Blueprint: stand it up at a new company
1. Define the **Tier-1 signal** for the new ICP: which detected platform = a buying trigger.
2. Add `URLSCAN_API_KEY` to `.env`. (Or swap in BuiltWith/Wappalyzer if budget allows - urlscan
   was chosen because it has a real free tier.)
3. Reuse `derive_domains.py` → dedup → throttled scan → cache → tiering rules → call sheet.
4. Set the tier rules as explicit, signal-based logic. Document them so they're auditable.

## Gotchas / hard rules
- **Throttle: ≥13s/submit, ≥1.5s/fetch.** Check remaining quota before a batch and chunk over days.
- **Cache everything** - never re-scan a known domain.
- **No Tier-1 without a CRM/stack signal.** Signal-based qualification is the whole point.
- **RAW input** for phone columns in Sheets.

## Cost
Free at 50 scans/day. For bigger batches, chunk across days or pay for a higher urlscan tier.
