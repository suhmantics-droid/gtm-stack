# GTM-E Measurement

The loop PLAYBOOK §2 step 6 demands. A play without a fired/replied/converted readout is an
experiment you can't learn from. This file is the standard for closing that loop. `/gtm-play`
sets it up when it runs a play; the client brief (`clients/<name>.md` §8) points at the results home.

The discipline is deliberately lightweight - a sheet + a weekly reconcile, not a BI stack. The
point is to make **kill-vs-scale** decisions on evidence, fast.

---

## 1. The funnel every play reports

```
SOURCED  →  ENRICHED  →  SCORED (tiered)  →  ACTIONED (drafted/sent)  →  REPLIED  →  MEETING  →  WON
```

Each play tracks the counts at each stage. The two ratios that decide a play's fate:
- **Actioned → Replied** (is the signal + message landing?)
- **Replied → Meeting** (is the targeting right?)

## 2. Results sheet (one tab per play)

Create a tab in the client's data home. Columns:

| Col | Field | Filled when |
|---|---|---|
| A | Company | sourced |
| B | Contact | enriched |
| C | Signal detail | sourced (e.g. "incorporated 2026-06-05", "runs Klaviyo") |
| D | Tier | scored |
| E | Action type | actioned (email/LinkedIn/call) |
| F | Drafted (date) | actioned |
| G | Sent (date) | sent (human-confirmed) |
| H | Replied (Y/N + date) | measure |
| I | Meeting (Y/N + date) | measure |
| J | Outcome | measure (won / lost / nurture) |
| K | Notes | any |

Sourced/enriched/scored/drafted are filled by the play run. Sent/replied/meeting/outcome are
filled by the **reconcile** (below) + the operator.

## 3. The reconcile (how "sent" and "replied" get filled)

Outreach is created as **drafts** (hard rule - never auto-sent). So the system can't assume a draft
was sent. Reconcile against Gmail truth on a cadence:

1. **Sent:** pull Gmail **Sent** for the window (`search_gmail_messages` / Workspace MCP), match by
   recipient email → fill col G. A drafted-but-never-sent row stays blank in G (that itself is a
   signal: drafts piling up unsent = a throughput problem, not a play problem).
2. **Replied:** search threads for replies from those recipients → fill col H.
3. This is the same "pull Gmail Sent before EOD" muscle already standard here - reuse it.

> Per memory: always pull **real** Gmail Sent + activity, never rely on recollection.

## 4. Per-play scorecard (what you report)

After each review window, one block per play:

```
Play: <id/name>   Window: <dates>
Sourced 120 → Enriched 96 (80%) → Tier1 31 → Sent 28 → Replied 6 (21%) → Meetings 2
Cost: <£/credits spent>     Cost per meeting: <£>
Verdict: SCALE / ITERATE / KILL - <one-line why>
```

## 5. Kill-vs-scale rule of thumb

Defaults - tune per client in the brief (§8):
- **Scale:** Actioned→Replied ≥ ~10% AND ≥1 meeting in the first ~25 actioned. Template it via `/gtm-skill-builder`.
- **Iterate:** replies but no meetings → targeting/message off, not the signal. Change ONE variable, rerun.
- **Kill:** < ~3% reply across ≥30 actioned → the signal isn't predictive for this ICP. Stop, free the budget.

Always `log()` what you killed and why in the client brief §9 - a killed play is learning, not failure.

## 6. Benchmarks to compare against (industry, not promises)

From RESOURCES.md §2 - frame, don't guarantee:
- Waterfall enrichment lifts valid-email rate ~55% → 90%+ (watch your Enriched% - if it's < ~70%, the enrichment chain, not the play, is the problem).
- AI-augmented outbound: +15-20% pipeline at 40-60% lower cost/opp vs SDR-only.

## 7. Anti-vanity rule

Don't report sourced/enriched counts as success. A play that sourced 5,000 companies and booked
zero meetings failed. The only numbers that matter downstream are **Replied, Meeting, Won** and
**cost per meeting**. Lead the scorecard with those.
