# GTM Engineering Playbook

**Purpose:** a business-agnostic framework for walking into *any* company and standing up signal-based revenue systems ("plays"), then formalising the winners as repeatable Claude skills.

**Audience:** anyone running this Claude Code stack as a GTM-engineering consultancy-in-a-box. Everything here is written to apply to a client business, whoever that client is.

Companion files:
- `PLAYS.md` - the reusable plays library (signal → enrich → score → act → measure).
- `RESOURCES.md` - voices, benchmarks, vendor map, signal sources.
- `MEASUREMENT.md` - how to close the loop (the funnel, the results sheet, kill-vs-scale).
- `ENGAGEMENT.md` - packaging this as a sellable engagement (tiers, deliverables, sprint shape).
- `clients/_TEMPLATE.md` - the per-client brief; the single source of truth all three skills read.
- `EXAMPLE-audit.md` - a worked, filled-in audit.
- Skills: `/gtm-audit` (discovery → writes the client brief), `/gtm-play` (scaffold + run a play), `/gtm-skill-builder` (formalise a winner as a skill).

---

## 1. What GTM Engineering is

GTM Engineering (GTM-E) replaces "hire more SDRs" with **revenue systems**: automated pipelines that detect a buying signal, enrich the contact, score fit, route it, and fire a personalised action - then measure what converted and kill what didn't.

The economics are the whole reason it exists. A fully-loaded SDR runs ~$180K/yr for 3-5 meetings/month. One GTM engineer (or an operator with this kind of stack) reportedly produces 30+ meetings at similar cost. HBR's 2024 research on AI-augmented selling found 15-20% more pipeline at 40-60% lower cost per opportunity vs SDR-only motions.

The mindset shift: **think in systems, not headcount.** Run GTM like product engineering - sprint-based, iterative, a roadmap of *plays* rather than a static playbook.

---

## 2. The core loop

Every play, in every business, is a variation of this loop:

```
SIGNAL  →  ENRICH  →  SCORE  →  ROUTE  →  ACT  →  MEASURE  →  (kill | template)
```

1. **Signal** - a time-bound reason to reach out *now* (job change, funding, tech install, pricing-page visit, new store opening, hiring spike, review going live).
2. **Enrich** - waterfall multiple data sources until you have a verified contact + company context. Pay only for successful matches.
3. **Score** - ICP-fit + signal-strength → a priority tier. No outreach on unscored data.
4. **Route** - send the scored record to the right person/queue/sheet.
5. **Act** - a personalised touch that references the signal (email, LinkedIn, a pass mockup, a call task).
6. **Measure** - what fired, what replied, what converted. Then either **kill** the play or **template** it (formalise as a skill).

The discipline is in steps 5→6: most teams build signals and never close the measurement loop. The win is killing dead plays fast and templating live ones.

---

## 3. The three maturity rungs

A business climbs these in order. Diagnose which rung a client is on before proposing plays (the `/gtm-audit` skill does this).

| Rung | Name | What "good" looks like | This stack's tools |
|---|---|---|---|
| 1 | **Data Foundation** | CRM/sheet records are clean, deduped, one row per entity, trustworthy keys (domain, LinkedIn URL). | Google Sheets (service account), `derive_domains.py`, dedup-by-domain-root |
| 2 | **Data Modeling** | Records carry predictive attributes: ICP tier, firmographics, tech stack, propensity signals. | `qualify-batch`, urlscan martech, Companies House size-class, Firecrawl site counts |
| 3 | **Data Activation** | Unique data points fire revenue workflows automatically. | `draft-outreach`, your house-voice skill, cold-email/email skills, mail drafts |

Rule: **don't sell a Rung-3 play to a Rung-1 business.** If their data foundation is broken, the activation play produces garbage at scale (see the 75% NXDOMAIN lesson in memory - pattern-guessed data activated at scale busts hard).

---

## 4. This stack mapped to the GTM-E layers

The toolkit already wired into this project *is* a GTM-E stack. The map:

| GTM-E layer | What it does | Tools in this system |
|---|---|---|
| **Signals / discovery** | Find time-bound reasons to reach out; build target lists with the story attached | `wallet-alpha` skill, Parallel Search MCP (ICP excerpts w/ employee_count inline), Tavily, Companies House (incorporations, officers, charges) |
| **Waterfall enrichment** | Verify email/phone/contact across multiple sources, pay per hit | `enrich.py` (Blitz → Lusha fallback), Firecrawl (site scrape), CH officers, Tavily (LinkedIn find) |
| **Scoring / ICP tiering** | Tier records by fit + signal strength | `qualify-batch` (urlscan CRM detect → Tier 1/2/3/X), CH size-class derivation |
| **Routing / data home** | One trustworthy place the team works from | Google Sheets via service account (`sheets_api.py`, `sheets_helper.py`), or a Notion hub |
| **Activation / outreach** | Personalised, signal-referencing touch | `draft-outreach`, your house-voice skill, `cold-email`, `emails`, mail drafts (never auto-send) |
| **Measurement** | Did it fire, reply, convert? | Gmail Sent pull, Sheet status columns, call-sheet `Call Status` / `Notes` columns |
| **Formalising winners** | Turn a proven play into a one-command skill | `skill-creator`, `/gtm-skill-builder` |

The gap GTM-E fills is the **orchestration + framing layer** on top - which the three new skills provide.

---

## 5. Standing up GTM-E in a client business (the engagement shape)

This is the repeatable motion for "go into any business and set up skills for them."

### Phase 0 - Discovery (`/gtm-audit`)
Map the business: ICP, current GTM motion, what data they hold, which signals are *available* to them, and which maturity rung they're on. Two inputs: **intake** (what the client tells you - CRM access, real numbers, first-party data; research can't see these) + **research** (outside-in, free sources). Output: a prioritised roadmap of 3-8 candidate plays ranked by **impact × ease**, written to **`clients/<name>.md`** - the single source of truth every later step reads. Before proposing plays, run the fit gate (§5a).

### Phase 5a - Fit gate (do this inside Phase 0)
Not every business suits signal-based outbound. Down-scope or decline if: TAM is tiny and local; no repeatable ICP; no system of record and no appetite to start one (stuck at Rung 1 unwilling to fix); or the buyer can't be reached by email/LinkedIn at all. Record the verdict in the brief. A clean "not a fit" beats a dead engagement.

### Phase 1 - Pick 1-2 plays
Choose plays that match their rung and have a clear, measurable outcome. Bias toward **one quick win** (proves the model in days) + **one structural play** (compounds).

### Phase 2 - Scaffold (`/gtm-play`)
For each chosen play, scaffold the implementation: the signal source, the enrichment chain, the scoring rule, the action, and the sheet/columns it writes to. Run it on a small batch first (one row, like the Amy Chen test).

### Phase 3 - Measure
Run the play for a defined window. Capture fired / replied / converted in the data home. Decide: kill or scale.

### Phase 4 - Formalise (`/gtm-skill-builder`)
Wrap the winning play as a named `/skill` for that business so it's a one-command motion they (or you) can re-run. Log it in their own SKILLS index.

### Phase 5 - Handover / repeat
Document the live plays, the data home, and the run commands. Either hand the keys over or keep operating it. Then loop back to Phase 1 with the next play.

---

## 6. Operating principles (hard rules)

These carry over from how this stack already runs - they are not optional:

- **No guessed data, ever.** Pattern-guessed emails/phones/LinkedIn URLs never enter a sheet. Verified data only (CH / Blitz / Lusha / Firecrawl with brand-match). Unknown → blank + "Needs research" flag. A 180-row pattern-email pass once produced a 75% NXDOMAIN bust rate - that is the failure mode this rule prevents.
- **Paid actions need per-call OK.** Lusha credits, any metered API - show the count + cost estimate, wait for explicit yes. Free verified paths (site scrape, CH officers, Parallel Search excerpts) are the default.
- **Verify the entity before recording.** Match name + location + role. Don't rush enrichment; one company at a time, right API for each step.
- **Never overwrite the source.** Always write to a new sheet/file. The source list is sacred.
- **Drafts, not sends.** Outreach is created as a Gmail draft for human review - never auto-sent.
- **Signal-based or it's not a play.** No Tier-1 without a signal. "Spray a list" is not GTM engineering.
- **Close the measurement loop.** A play without a fired/replied/converted readout is an experiment you can't learn from. Always wire the readout - see `MEASUREMENT.md`.

---

## 6a. Boundaries (what this system deliberately does NOT do)

Name these up front so expectations are set (and so nobody mistakes a boundary for a bug):

- **No bulk auto-send / sequencing.** Outreach stops at a human-reviewed **draft**. Multi-touch cadence, send infrastructure, domain warmup, and deliverability are out of scope by design. If a client needs volume sending, that's a sequencer (Smartlead/Instantly) bolted on downstream - flag it, don't fake it.
- **Not a million-row operation.** This is surgical, signal-led, verified-data outbound. Right fit for SMB/mid-market; wrong fit for "touch our entire CRM."
- **No CRM by default - Sheets is the data home.** If the client's system of record is HubSpot/Salesforce and they want plays writing there, that's a per-engagement integration (capture access in brief §3); don't assume it.

## 6b. Geography

Companies House (the firmographic backbone) is **UK-only**. For UK buyers, formation/officer/funding plays (families A, D) are fully available. **Outside the UK**, those families have no equivalent source wired - fall back to Parallel Search / Tavily / Firecrawl (site + news + LinkedIn excerpts), and lean on the tech-stack (C) and reputation (F) families, which are geography-agnostic. Always record the client's buyer geography in the brief §1 - it decides which plays are real.

## 6c. Compliance

Cold outbound and scraping carry legal duties, especially when run **on a client's behalf**:
- **UK/EU:** GDPR + PECR. B2B email to corporate addresses generally relies on **legitimate interest**, but you must be able to justify it, honour opt-outs, and avoid individuals' personal addresses. Record the lawful basis in the brief §7.
- **No personal-data guessing** - the data-quality rule is also a compliance rule: verified, sourced contacts only.
- On a client engagement the client's own legal/DPO signs off the basis - you implement to it, you don't invent it.

## 6d. Fixing a Rung-1 foundation

If the audit finds Rung 1 (messy/no central data), the fix comes **before** any activation play: dedup by domain-root (the `qualify-batch` / `derive_domains.py` pattern), collapse to one row per entity, normalise keys (domain, LinkedIn URL), and stand up a single source-of-truth sheet. Only then climb to modeling/activation. Selling activation onto a broken foundation reproduces the 75% NXDOMAIN failure at scale.

---

## 7. How to think about "plays" vs "skills"

- A **play** is a strategy (this signal → this action). It lives in `PLAYS.md`.
- A **skill** is a play that's been proven and frozen into a one-command Claude motion (`/foo`). `/gtm-skill-builder` does the freezing.
- Not every play becomes a skill. Only template the ones that (a) worked and (b) you'll run more than ~3 times.

The roadmap of plays is the product. The skills are the compounding asset.
