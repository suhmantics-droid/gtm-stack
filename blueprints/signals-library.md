# Blueprint 9 - Signals library

## What it does
The full catalogue of **buying signals** - time-bound reasons to reach out *now* - with where to
source each, how fresh it is, and which play it feeds. The 6 families in `../gtm-engineering/PLAYS.md`
are the summary; this is the deep reference.

## The signal catalogue
| Signal | What it indicates | Source in this stack | Freshness |
|---|---|---|---|
| New company formation | Brand-new entity, earliest-mover advantage | Companies House (`gtm_formation_signal.py`) | Daily |
| Officer / director change | New buyer, new mandate | Companies House officers/PSC | Days |
| Funding round | Fresh budget, growth mandate | Tavily/Parallel news; CH filings | Days |
| Hiring a role | Explicit budget/project (e.g. "CRM Manager") | Firecrawl careers / LinkedIn jobs | Weekly |
| Headcount band crossed | Scaling pains | Parallel Search (employee_count inline) | Monthly |
| Tech install / stack | Runs a platform you integrate with or displace | urlscan martech | On scan |
| Stack change | Churned onto/off a platform | urlscan re-scan vs cache | On scan |
| Pricing/high-intent page visit | Active buying intent | Client first-party (reverse-IP) - **not in stack** | Real-time |
| Inbound sign-up | Hand-raise | Client CRM/webhook | Real-time |
| New review / press / award | Timely, public moment | Tavily/Parallel news + review sites | Days |
| Physical expansion (new store/venue) | Point-of-presence moment | Firecrawl store-locator counts, news | Weekly |
| Podcast / conference appearance | Person is reachable + on-message | Web/Tavily search | Days |

## How we used it
- **Signal first, list second.** Every list we built carried a reason-to-reach-out with the source
  cited per row - a funded-company list, a tech-stack list, a new-formation list. Flat lists got parked.
- **The strongest signals we ran live:** tech-stack (urlscan), new formation (CH), recent funding
  (news). Each turned a cold name into a warm, specific opener.
- **First-party intent is the highest-impact signal we can't get** without the client's own
  analytics/CRM - we flag that dependency rather than fake it.

## Blueprint: stand it up at a new company
1. Pick the 2-3 signals that map to the new ICP's buying triggers.
2. Wire each to its source (table above); cite the source on every row.
3. Rank candidate signals on **predictiveness × ease-of-detection**; start with the easiest strong one.
4. Schedule the recurring ones (Blueprint 16) so the signal pipeline runs without you.

## Gotchas / hard rules
- **A signal you check once isn't a system** - recurring signals need a cadence.
- **No guessed data** - every signal row needs a real, sourced trigger.
- **First-party intent (E-family) needs client data** - never assume you have it.
- Geography gates some signals (CH = UK only) - match signal to buyer geography.

## Cost
Most signals are free (CH, Parallel, Tavily, urlscan tiers). First-party intent requires the
client's own tooling.
