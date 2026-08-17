# Blueprint 17 — Reporting & analytics

## What it does
Shows whether the motion is working: the funnel per play, cost per meeting, and which signals
actually convert — so you scale winners and kill losers on evidence.

## Tools / method
- The per-play results sheet + scorecard from `../gtm-engineering/MEASUREMENT.md`.
- Gmail-Sent reconcile (Workspace MCP) to fill "sent" and "replied" from truth, not assumption.
- A simple roll-up (a summary tab / Looker Studio / a sheet pivot) across plays.

## How it fits (what we did vs didn't)
- We **defined** the measurement standard in `MEASUREMENT.md` (the SOURCED→…→WON funnel, the
  kill-vs-scale rule, the Gmail-Sent reconcile) and built the results-sheet shape. We did **not**
  build live dashboards in-project — so dashboards are recommended practice; the funnel discipline is lived.
- The anti-vanity rule is the core: sourced/enriched counts are **not** success. Replied, meeting,
  won, and cost-per-meeting are.

## The numbers that matter (per play, per window)
```
Sourced → Enriched (%) → Tier1 → Sent → Replied (%) → Meetings → Won
Cost: <spend>     Cost per meeting: <£>
Verdict: SCALE / ITERATE / KILL
```
- **Actioned→Replied** tells you if the signal+message lands.
- **Replied→Meeting** tells you if the targeting is right.
- **Enriched %** < ~70% means the enrichment chain, not the play, is broken.

## Blueprint: stand it up at a new company
1. One results tab per play (Blueprint 5 columns), filled by the play run.
2. Reconcile against Gmail Sent on a cadence to fill sent/replied from truth.
3. Roll up to one scorecard view across plays; lead with replied/meeting/cost-per-meeting.
4. Tune scoring (Blueprint 14) and kill dead plays based on this — and **log what you killed and why**.

## Gotchas / hard rules
- **Anti-vanity:** never report volume as success. Downstream numbers only.
- **Reconcile against real Sent** — don't assume a draft was sent.
- **Log kills** — a killed play is learning, not failure.

## Cost
Free (sheets + reconcile). Optional BI tool (Looker Studio is free) if a client wants dashboards.
