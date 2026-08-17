# Blueprints - portable GTM / RevOps tradecraft

Reusable playbooks for the tooling and methods built in this project, **stripped of any
company-specific data**. The point: walk into any business or role and stand the same
capabilities up fast, from a known-good recipe instead of from scratch.

Each blueprint follows the same shape:
1. **What it does**
2. **Tools / scripts**
3. **How we used it** - the real workflow + the lessons we actually learned
4. **Blueprint: stand it up at a new company** - the transferable steps
5. **Gotchas / hard rules**
6. **Cost**

## The blueprints

**Plumbing - how to get and move data**
| # | Blueprint | Capability |
|---|---|---|
| 1 | [enrichment.md](enrichment.md) | Contact data - work email + phone (waterfall) |
| 2 | [firmographics-companies-house.md](firmographics-companies-house.md) | Company facts - size, officers, formations (UK) |
| 3 | [icp-qualification.md](icp-qualification.md) | Tech-stack detection → ICP tiering → call sheet |
| 4 | [prospecting-discovery.md](prospecting-discovery.md) | Finding NEW companies that match an ICP |
| 5 | [data-home-google-sheets.md](data-home-google-sheets.md) | Sheets as the live data home (service account) |
| 6 | [mcp-stack.md](mcp-stack.md) | The MCP servers and what each is for |
| 7 | [outreach-workflow.md](outreach-workflow.md) | Enrich → research → draft → measure (never auto-send) |
| 8 | [claude-operating-model.md](claude-operating-model.md) | How skills + memory + CLAUDE.md run the whole thing |

**Layer A - Strategy & signals (the "why it works")**
| # | Blueprint | Capability |
|---|---|---|
| 9 | [signals-library.md](signals-library.md) | The full buying-signal catalogue + sources |
| 10 | [gtm-e-narrative.md](gtm-e-narrative.md) | First principles + how to talk about GTM-E |
| 11 | [ai-in-the-loop.md](ai-in-the-loop.md) | Claude as a GTM primitive (classify, research, draft) |

**Layer B - Complete operating stack**
| # | Blueprint | Capability |
|---|---|---|
| 12 | [crm-integration.md](crm-integration.md) | Working a client's HubSpot / Salesforce |
| 13 | [data-hygiene.md](data-hygiene.md) | Dedup, identity resolution, the Rung-1 fix |
| 14 | [scoring-and-routing.md](scoring-and-routing.md) | Fit × intent scoring + routing |
| 15 | [sequencing-deliverability.md](sequencing-deliverability.md) | Send-at-volume (the piece we don't do) |
| 16 | [automation-scheduling.md](automation-scheduling.md) | Running signals on a cadence |
| 17 | [reporting-analytics.md](reporting-analytics.md) | Funnels, scorecards, cost-per-meeting |
| 18 | [compliance-data-protection.md](compliance-data-protection.md) | GDPR/PECR, suppression, lawful basis |

**Layer C - Commercial / operating**
| # | Blueprint | Capability |
|---|---|---|
| 19 | [proposals-and-sow.md](proposals-and-sow.md) | Proposals + statement-of-work templates |
| 20 | [client-onboarding.md](client-onboarding.md) | First-week intake, access, kickoff |
| 21 | [case-study-capture.md](case-study-capture.md) | Turning a win into a reference asset |
| 22 | [sales-enablement-system.md](sales-enablement-system.md) | Call-mined knowledge base, competency framework, claims policy |

**Reference:** [glossary.md](glossary.md) - plain-English definitions.

The full **GTM Engineering system** (audit → play → freeze) is its own thing - see
`../gtm-engineering/README.md`. These blueprints are the primitives it's built on.

## What's lived vs. recommended
Honest labelling matters. Blueprints 1-6, 9, 11, 13, 14, 20, 22 are grounded in what we **actually did**.
12 (CRM), 15 (sequencing), 17 (dashboards), 19 (SOW), 21 (case study) are **recommended practice** we
deliberately didn't run in-project - each says so in its "how it fits" section. Don't present
recommended-practice docs as battle-tested.

## The standing rules that survive any move
These showed up across every capability and are non-negotiable:
- **No guessed data.** Verified contacts only; unknown = blank + "needs research".
- **Per-call OK for spend.** Any metered API (Lusha, etc.) - show the count + cost, wait for yes.
- **New sheet, never overwrite** the source.
- **Drafts, not sends.** A human sends outreach.
- **Signal-based or it's not a play.** No targeting without a reason to reach out.
- **Free/verified-first.** Reach for paid sources only when the free ones are exhausted.

## Adapting these to a new employer
- Swap the **ICP**, the **vertical signals**, and the **house voice** - those are company data, kept out of here.
- Keep the **pipelines, the API patterns, and the guardrails** - those are the transferable asset.
- Re-key everything: each blueprint notes which API keys / accounts it needs in `.env`.
