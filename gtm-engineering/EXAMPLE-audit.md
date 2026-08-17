# Worked Example - `/gtm-audit` output

A filled-in audit so the format is concrete and testable.

> **This subject is illustrative.** "Meridian Talent" is a composite of the kind of business
> this stack is usually pointed at, not a real client. The point is the *reasoning and the
> format*, not the company. Real audits get their own `clients/<name>.md`.
>
> Numbers framed as industry benchmarks are exactly that. They are not results from any
> engagement, and they must never be presented as such.

---

## Snapshot

- **What they sell:** contract and permanent recruitment into UK engineering and manufacturing.
- **Deal shape:** placement fee, 15-22% of first-year salary. Average fee about £9k.
- **ICP:** UK manufacturers and engineering consultancies, 50-500 headcount, hiring 5+ technical roles a year.
- **Buyer:** Head of Talent / HR Director, with the hiring manager as the day-to-day champion.
- **Current motion:** consultants sourcing from a 2019-era CRM, plus referrals. No outbound system.
- **Geography:** UK only. So UK firmographic plays (Companies House) are fully available.
- **Unknowns flagged:** their own website analytics. Not shared at audit stage, so no first-party intent play can be scoped yet.

## Maturity rung

**Rung 1 → 2.** The data foundation is the blocker, not the ambition. The CRM holds roughly
11,000 company records with no dedup and no domain field, so the same employer appears under
three spellings. Nothing downstream is trustworthy until that is fixed.

**Read this honestly:** proposing signal plays before the Rung-1 fix would produce impressive
demos on dirty data. Do the hygiene pass first, even though it is the least exciting slide.

## Signal inventory (for this business)

| Family | Status | Why |
|---|---|---|
| A formation (UK) | **Available** | CH `gtm_formation_signal.py` - new manufacturers in target SIC codes |
| B hiring | **Available (flagship)** | Their entire product *is* a hiring event. Careers-page scrape is the core signal |
| C tech-stack | Partial | Useful for sizing, weak as a trigger. Recruitment fit is not stack-dependent |
| D funding | **Available** | A raise usually precedes a hiring wave. Strong leading indicator here |
| E web-intent | **Not available** | Needs their analytics. Correctly out of scope, not faked |
| F reputation/expansion | Available | New site or factory opening implies local hiring |

## Play roadmap (ranked Impact × Ease)

| Play | Signal | Impact | Ease | Score | Pick |
|---|---|---|---|---|---|
| **B1** hiring | target is advertising 3+ technical roles | 5 | 4 | 20 | **Quick win** - the signal *is* the offer |
| **D1** funding | recent raise at an in-ICP manufacturer | 5 | 3 | 15 | **Structural** - leads the hiring wave by weeks |
| **A1** formation | new company in target SIC | 3 | 5 | 15 | cheap, verified runner ready, lower hit rate |
| F2 expansion | new site or facility announced | 4 | 2 | 8 | high relevance, mostly manual sourcing |
| C1 tech-stack | ATS in use | 2 | 4 | 8 | sizing context, not a trigger |

**Quick-win pick:** B1. A company advertising four technical roles has already declared both the
budget and the pain. No inference required.

**Structural pick:** D1. Funding leads hiring, so it reaches the buyer before the vacancy is
public and before every competing agency calls.

**Deliberately not picked:** E1/E2. Their data foundation is Rung 1. Sequencing a first-party
intent play now would fail for reasons that have nothing to do with the play.

## Opportunity sizing (industry framing, not promises)

- Waterfall enrichment typically lifts valid-email rate from roughly 55% to 90%+. On a 2,000-row list that is about 700 more reachable contacts.
- AI-augmented outbound is commonly reported at +15-20% pipeline for 40-60% lower cost per opportunity versus SDR-only.

Both are industry figures. Treat them as a reason to run the test, never as a forecast.

## The 90-day shape

| Phase | Work | Proof it worked |
|---|---|---|
| Weeks 1-2 | Rung-1 hygiene: dedup by domain, add the domain field, suppression list | One company, one row. Counts reconcile |
| Weeks 3-5 | B1 live: careers-page scrape → enrich → score → drafts | First meeting booked from a detected vacancy |
| Weeks 6-9 | D1 added, weekly cadence, measurement tab instrumented | Reply rate by signal type, versus an aged-list control |
| Weeks 10-13 | Kill or freeze. Winner becomes a one-command skill | A play that runs without the person who built it |

## Not yet, and why

A roadmap that recommends everything is a sales document.

- **First-party intent (E1/E2):** blocked on data access and on the Rung-1 fix. Revisit at week 10.
- **Multi-channel sequencing at volume:** they have one shared mailbox with no domain warm-up. Sending at volume from it would burn the domain they depend on.
- **CRM replacement:** the CRM is not the problem. The data in it is. Replacing it first would move dirty data into a more expensive box.

## Dependency / honesty note

The highest-ceiling family here (E, first-party web intent) is off the table without their
analytics, and is flagged rather than quietly dropped. The roadmap leans on the families that
can be detected for real, today, with free sources.
