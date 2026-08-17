# gtm-stack

A portable GTM-engineering system. Point it at a business, map what signals it can actually
reach, and get back a ranked list of revenue plays. Then run one, measure it, and either kill it
or freeze it into a one-command skill.

No company's private data is in here. Only method, tooling and templates.

```
signal  ->  enrich  ->  score  ->  route  ->  act  ->  measure  ->  kill or freeze
```

The discipline is the last two steps. Most teams build signals and never close the measurement
loop, so nothing gets killed and nothing gets templated.

---

## Why this exists

"Hire more SDRs" is the default answer to a pipeline problem, and it is usually the expensive
one. The alternative is to spend the effort on prioritisation instead of volume: work out which
accounts have a reason to buy this week, and reach those.

That only works if you can answer three questions honestly:

1. **What signals can this business actually reach?** Not what a vendor deck says. What is
   genuinely available given its data, its market and its budget.
2. **Is the data foundation clean enough to trust the answer?** A signal play on duplicated,
   domainless records produces confident nonsense.
3. **Did it work?** Measured against a control, not against a feeling.

This repo is the method for answering all three, plus the runners for the plays that are free.

## What's in here

| Path | What |
|---|---|
| `blueprints/` | 21 how-to blueprints plus a glossary. The full tradecraft. Start at [`blueprints/README.md`](blueprints/README.md) |
| `gtm-engineering/` | The audit, play, freeze system. Start at [`gtm-engineering/README.md`](gtm-engineering/README.md), then [`PLAYBOOK.md`](gtm-engineering/PLAYBOOK.md) |
| `gtm-engineering/PLAYS.md` | The plays library. Every card carries a runner status, so you can see what is a button and what is still a strategy |
| `gtm-engineering/EXAMPLE-audit.md` | A filled-in audit, so the output format is concrete |
| `scripts/` | Runnable: Companies House formation signal, domain derivation, Sheets I/O |
| `.env.example` | The API keys. Every one has a free tier |
| `.mcp.json.example` | The MCP servers to register |

## Quickstart

Prerequisites: [uv](https://docs.astral.sh/uv/) and Node.js.

```bash
cp .env.example .env          # add a free Companies House key
```

Then prove the whole chain works, for free, in one command:

```bash
uv run --with requests python scripts/gtm_formation_signal.py --sic 47710 --days 14 --limit 5
```

A short list of real UK companies incorporated in the last fortnight means env, API and output
are all live. Full setup, including MCP servers and Google Workspace, is in
[`START-HERE.md`](START-HERE.md).

## The plays library

Plays are grouped by signal family. Each one is the same loop with the trigger swapped.

| Family | Example signal | Source | Cost |
|---|---|---|---|
| A. Formation | A company just incorporated in a target SIC code | Companies House | Free |
| B. Hiring | Hiring a role that implies a budget you serve | Careers-page scrape | Free |
| C. Tech stack | Runs a platform you integrate with or displace | urlscan, DNS | Free tier |
| D. Funding | Recent raise, so new budget and a mandate | News search, CH filings | Free tier |
| E. Web intent | High-intent page visit | The client's own analytics | Client-provided |
| F. Reputation | New store, venue, award or press mention | Scrape, news | Free tier |

Family E is deliberately marked as unavailable by default. It is the highest-ceiling signal
family and it is impossible without the client's first-party data. Saying so is more useful than
pretending otherwise.

## Honest labelling

Blueprints are marked for whether they are **lived** or **recommended practice**. Blueprints
1-6, 9, 11, 13, 14 and 20 came out of work that actually ran. 12, 15, 17, 19 and 21 are
recommended practice that was deliberately not run, and each says so in its own text.

Do not present a recommended-practice document as battle-tested. The distinction is the point.

## The rules that travel with this stack

These are not style preferences. Each one exists because the alternative went wrong.

| Rule | Why |
|---|---|
| **No guessed data** | Verified or blank. A pattern-guessed email list once came back 75% NXDOMAIN. The fix was not a better guess |
| **Free path first** | Exhaust free and verified sources before anything metered |
| **Spend needs a yes** | Show the count and the cost, then wait for it |
| **New sheet, never overwrite** | The source list is sacred |
| **Drafts, not sends** | A human sends outreach. Every time |
| **Signal-based or it isn't a play** | Spraying a list is not engineering |
| **Measure before you trust** | Know your own false-positive rate before calling a change a signal |

## What's deliberately not here

- **No company's private data.** No prospect lists, case studies, brand assets or house voice. Those are rebuilt per engagement. [`blueprints/client-onboarding.md`](blueprints/client-onboarding.md) covers how.
- **No secrets.** You supply your own keys in `.env`, which is gitignored.
- **No send-at-volume tooling.** [`blueprints/sequencing-deliverability.md`](blueprints/sequencing-deliverability.md) documents the method, but this stack drafts and a human sends.

## Adapting it

Swap the ICP, the vertical signals and the house voice. Those are company data and are kept out
of here by design. Keep the pipelines, the API patterns and the guardrails. Those are the
transferable asset.

## Licence

MIT. See [`LICENSE`](LICENSE).
