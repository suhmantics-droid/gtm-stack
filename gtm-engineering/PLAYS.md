# GTM-E Plays Library

A catalogue of reusable plays. Each is the same loop — **signal → enrich → score → act → measure** — with the trigger and the action swapped. Pick by what data/signal the client business can actually access (the `/gtm-audit` skill maps that).

**How to read a play card:**
- **Signal** — the time-bound trigger.
- **Source** — where the signal comes from (which tool in this stack, or what the client provides).
- **Enrich** — the waterfall to get a verified contact + context.
- **Score** — the fit/priority rule.
- **Act** — the personalised touch.
- **Measure** — the readout that tells you to kill or scale.
- **Rung** — minimum maturity rung (see PLAYBOOK §3) the business needs.
- **Effort / Impact** — rough triage for the roadmap.

Plays are grouped by the signal family. Most businesses start with 1 inbound play + 1 outbound signal play.

**Runner status** — which plays have an executable runner today vs. need building in `/gtm-play`:
- ✅ **Built & verified:** C1 (tech-stack, `qualify-batch`), A1 (formation, `gtm_formation_signal.py`), enrichment chain (`enrich.py`).
- 🔧 **Scaffold-on-demand:** B1/B2 (hiring/headcount — Firecrawl careers + Parallel), C2 (stack-change — urlscan re-scan vs cache), D1 (funding — Tavily/Parallel news), F1/F2 (reputation/expansion — Firecrawl + news). `/gtm-play` wires these from proven primitives when first run.
- ⛔ **Needs client data:** E1/E2 (first-party web intent / inbound) — no runner possible without the client's analytics/CRM.
A play card without a ✅ Runner line is a strategy, not yet a button — `/gtm-play` builds it, tests one record, then it's real.

---

## A. New-company / formation signals

### A1 — Fresh incorporation in an ICP vertical
- **Signal:** a company just incorporated in a target SIC code / vertical.
- **Source:** Companies House `/advanced-search/companies` (incorporated_from date + SIC). Free.
- **Runner:** ✅ `gtm_formation_signal.py` (verified live). `uv run --with requests python scripts/gtm_formation_signal.py --sic <code(s)> --days 30 --limit 100` → JSON of new formations, newest-first.
- **Enrich:** CH officers → director names; Firecrawl their site for domain + contact; Tavily for LinkedIn.
- **Score:** vertical match + size proxy (officer count, SIC). Tier 1 if ICP vertical.
- **Act:** "saw you just launched X" opener — earliest-mover advantage, nobody else is calling them yet.
- **Measure:** reply rate vs aged-list control.
- **Rung:** 2 · **Effort:** Low · **Impact:** Med (depends on ICP fit of new formations).

### A2 — Officer / director change at a target account
- **Signal:** a new director or significant-control person appears.
- **Source:** Companies House `get_officers` / PSC endpoints, polled.
- **Enrich:** new officer → LinkedIn (Tavily) → email (Blitz, Lusha only with OK).
- **Score:** is the new officer a buyer-persona title? Tier on that.
- **Act:** congratulate the appointment, tie to a relevant outcome.
- **Measure:** reply rate.
- **Rung:** 2 · **Effort:** Med · **Impact:** Med.

---

## B. Hiring / headcount signals

### B1 — Hiring for a role that implies a budget you serve
- **Signal:** company is hiring for a role that signals a project/budget (e.g. hiring a "CRM Manager" → martech budget; "Retail Expansion Manager" → new stores).
- **Source:** job-board scrape (Firecrawl on careers page), LinkedIn jobs via Tavily/Parallel.
- **Enrich:** hiring manager / department head → contact waterfall.
- **Score:** role-to-offer fit. Strong signal = Tier 1.
- **Act:** "noticed you're building out X — here's how teams solve the gap before the hire lands."
- **Measure:** reply rate, meeting rate.
- **Rung:** 2 · **Effort:** Med · **Impact:** High (intent is explicit).

### B2 — Headcount growth spike
- **Signal:** company crossed a headcount band (e.g. 50→100) → scaling pains.
- **Source:** Parallel Search LinkedIn-company excerpts (employee_count inline), repeat monthly.
- **Enrich:** ops/growth leader contact.
- **Score:** band + vertical.
- **Act:** scaling-pain angle.
- **Measure:** reply rate by band.
- **Rung:** 2 · **Effort:** Med · **Impact:** Med.

---

## C. Tech-stack / martech install signals

### C1 — Runs a stack you integrate with / displace
- **Signal:** company's site shows a specific platform (CRM, ESP, e-comm, analytics).
- **Source:** urlscan martech detection (`qualify-batch`). 50/day, 5/min free tier.
- **Enrich:** marketing/CRM owner contact.
- **Score:** Tier 1 if the detected stack is your ICP trigger (e.g. Klaviyo/HubSpot/Shopify for a wallet/CRM offer).
- **Act:** stack-specific talk track ("you run Klaviyo — the wallet channel sits next to it and lifts X").
- **Measure:** reply rate by detected platform.
- **Rung:** 2 · **Effort:** Low (already built) · **Impact:** High. **This is the flagship play in this stack.**

### C2 — Stack *change* (churned off a partner platform)
- **Signal:** company that used to run platform X no longer does (or vice versa).
- **Source:** urlscan re-scan vs cached `urlscan_results.json`. (Memory: 2-yr-old partner lists are ~82% churned — this play monetises that churn.)
- **Enrich:** as C1.
- **Score:** direction of change → which talk track.
- **Act:** "saw you moved off X" / "saw you added Y".
- **Measure:** reply rate vs cold.
- **Rung:** 2 · **Effort:** Low · **Impact:** Med-High.

---

## D. Funding / financial signals

### D1 — Recent raise
- **Signal:** company raised a round → new budget, expansion mandate.
- **Source:** Tavily/Parallel news search; Companies House filing history (charges, share allotments) as a UK proxy.
- **Enrich:** budget-owner contact.
- **Score:** round size + vertical.
- **Act:** "congrats on the raise — teams at this stage usually tackle X next."
- **Measure:** meeting rate (funded accounts convert higher).
- **Rung:** 2 · **Effort:** Med · **Impact:** High.

### D2 — Filing-history event (charge, mortgage, accounts overdue)
- **Signal:** a UK-specific financial event in CH filing history.
- **Source:** Companies House `get_filing_history` / `get_charges`.
- **Enrich / Score / Act:** event-dependent.
- **Rung:** 3 · **Effort:** High · **Impact:** Niche.

---

## E. Web-intent signals (first-party)

### E1 — Pricing-page / high-intent page visit
- **Signal:** a known or de-anonymised visitor hits a high-intent page.
- **Source:** client's reverse-IP / analytics (client-provided; not in this stack by default).
- **Enrich:** de-anon company → buying-committee contacts.
- **Score:** page + frequency.
- **Act:** same-day personalised follow-up referencing the interest.
- **Measure:** speed-to-lead vs conversion.
- **Rung:** 3 · **Effort:** High (needs client's first-party data) · **Impact:** Very High.

### E2 — Inbound sign-up routing & auto-draft
- **Signal:** a new inbound sign-up / form fill.
- **Source:** client CRM/form webhook.
- **Enrich:** firmographics + ICP fit on the sign-up.
- **Score:** auto-tier, auto-assign.
- **Act:** draft a tailored follow-up for the rep to send.
- **Measure:** speed-to-first-touch, sign-up→meeting rate.
- **Rung:** 3 · **Effort:** Med · **Impact:** High.

---

## F. Content / reputation signals

### F1 — New review or press going live
- **Signal:** a notable review, award, or press mention publishes.
- **Source:** Tavily/Parallel news + review-site search.
- **Enrich:** relevant contact.
- **Act:** reference the moment — high reply rate because it's genuinely timely.
- **Measure:** reply rate.
- **Rung:** 2 · **Effort:** Med · **Impact:** Med.

### F2 — Physical-presence / expansion event
- **Signal:** new store / venue / location opening (ties to the "Has App? / Retail Stores" enrichment signals already standard here).
- **Source:** Firecrawl store-locator count over time, news search.
- **Act:** expansion-moment angle.
- **Rung:** 2 · **Effort:** Med · **Impact:** Med-High for physical-retail ICPs.

---

## Roadmap triage

When `/gtm-audit` proposes a roadmap, rank candidate plays on **Impact × Ease**, then pick:

| Pick | Why |
|---|---|
| 1 quick win (low effort, ready signal) | Proves the model in days. Usually **C1** (urlscan stack play) since it's already built. |
| 1 structural play (compounds) | Builds a durable signal pipeline. Often **B1** (hiring) or **D1** (funding). |

Avoid: starting with Rung-3 first-party plays (E1/E2) at a business whose data foundation isn't clean yet.

---

## Adding a play

When a new repeatable play is proven, add a card here in the same shape, then consider freezing it as a skill via `/gtm-skill-builder`. Keep the library to plays that have actually run at least once — speculative plays go in a separate "ideas" note, not here.
