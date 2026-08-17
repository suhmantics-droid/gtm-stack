# GTM-E Resources

Curated reference layer for the GTM Engineering playbook. Voices to learn from, benchmarks to quote, the vendor landscape, and where signals come from. Keep this current; prune dead links.

---

## 1. Voices & sources worth following

Sagar already follows these (see memory `reference_gtm_voices_and_stack_prefs`) — treat as the canon:

- **Nathan @ Clay Bootcamp** — Clay-native GTM engineering, hands-on plays.
- **gtmepulse.com** — GTM operator newsletter/community.
- **Clay GTM blog** — https://www.clay.com/blog/gtm-engineering — the reference definition piece (role, three rungs, hiring rubric).
- **Clay community** — case studies and play teardowns: https://community.clay.com
- **HubSpot "Science of Scaling" GTM Engineer Playbook** — https://offers.hubspot.com/gtm-engineer-playbook (note: Sagar **declined HubSpot** as a tool — use the playbook as reading, not a buying signal).
- **Apollo GTM-engineer guides** — role/skills/job-description explainers: https://www.apollo.io/insights

## 2. Benchmarks to quote (verified from research, June 2026)

Use these to size a play's ROI in `/gtm-audit`:

| Metric | Figure | Source |
|---|---|---|
| Fully-loaded SDR cost | ~$180K/yr for 3–5 meetings/mo | Clay GTM blog |
| GTM engineer output | ~30+ meetings/mo at similar cost | Clay GTM blog |
| Waterfall enrichment lift | valid-email rate 55–60% → 90%+ | Octave / industry waterfall data |
| AI-augmented outbound | +15–20% pipeline at 40–60% lower cost/opp vs SDR-only | HBR 2024 AI-sales research |
| GTM engineer comp band | ~$132K–$241K | Apollo / Cleanlist 2026 |

These are *industry* figures for framing, not any client's numbers. Don't present them as client-specific results.

## 3. Vendor landscape (the canonical GTM-E stack)

What the market uses, mapped to what this project uses instead. Useful when a client already runs one of these and you're explaining the equivalent.

| Layer | Market-standard tools | What this stack uses |
|---|---|---|
| Orchestration / enrichment hub | **Clay** (50+ source waterfall, the default) | `enrich.py` + Firecrawl + CH + Parallel/Tavily (DIY waterfall) |
| Contact data | Apollo (275M), ZoomInfo (enterprise), Prospect AI (530M, NL search) | Blitz (email), Lusha (email+phone, metered) |
| ICP / firmographics | Clearbit, ZoomInfo | urlscan (martech), Companies House (UK firmographics) |
| Sequencing / sending | Smartlead, Instantly (~40% combined share of new outbound), Outreach, Salesloft, Lemlist | Gmail drafts via Workspace MCP (human-reviewed, not bulk-send) |
| Full-stack AI SDR | 11x, Artisan, Amplemarket, Prospect AI | Claude skills (`draft-outreach`, your house-voice skill) |
| Data home | CRM (HubSpot/Salesforce) | Google Sheets (service account), Notion Hub |
| Workflow glue | n8n, Zapier, Make | Claude Code + Python scripts + scheduled tasks |

**Positioning note:** this stack is a *lean, verified-data-first* GTM-E setup — no Clay subscription, no bulk-send infra. The trade-off is more manual orchestration in exchange for cost and data-quality control. That's a feature for cost-sensitive clients, a limit for ones who want millions of CRM rows touched.

## 4. Signal sources available in this stack

What you can actually detect today, by play family (see `PLAYS.md`):

| Signal family | Available via | Cost |
|---|---|---|
| Company formation / officers / PSC / charges (UK) | Companies House MCP + REST (`COMPANIES_HOUSE_API_KEY`) | Free (600 req/5min) |
| Martech / tech install | urlscan (`qualify-batch`) | Free 50/day, 5/min |
| Headcount / ICP firmographics | Parallel Search MCP (LinkedIn excerpts, employee_count inline) | Free, main-thread only |
| News / funding / press / reviews | Tavily MCP, Parallel Search | Free tiers |
| Site content / store counts / careers pages | Firecrawl MCP | Metered |
| Email verification | Blitz (primary), Lusha (fallback, metered, per-call OK) | Blitz default; Lusha credits |
| First-party web intent (pricing visits) | **Not in stack** — client must provide reverse-IP/analytics | — |

**Geography caveat:** Companies House is **UK-only** — formation/officer/funding plays don't have a non-UK equivalent wired. Outside the UK, lean on tech-stack (urlscan), news/firmographics (Parallel/Tavily), and site signals (Firecrawl), which are geography-agnostic. Record buyer geography in the client brief; it decides which plays are real.

**Subagent MCP wall:** spawned subagents get permission-denied on `companies-house` and `parallel-search` MCP tools (verified — see memory). For bulk signal/firmographic work, call the **direct REST API** from a Python script (the `gtm_formation_signal.py` / `events_ch_lookup.py` pattern; CH key in `.env`, HTTP Basic auth). Don't fan out MCP-heavy work to subagents — they bail and waste tokens. Keep MCP calls on the main thread.

## 5. Data-quality guardrails (non-negotiable)

Pulled forward from project memory because they decide whether a play works at scale:

- **No guessed data** — verified only; unknown = blank + "Needs research". (180-row pattern-email pass → 75% NXDOMAIN. Never again.)
- **Per-call OK for paid APIs** — Lusha and any metered source. Show count + cost first.
- **Verify the entity** — name + location + role match before recording.
- **New sheet, never overwrite** the source.
- **Drafts not sends.**
- **Compliance basis recorded** — UK/EU cold B2B leans on legitimate interest under GDPR/PECR; record the lawful basis per engagement (PLAYBOOK §6c). On a client engagement, their legal/DPO owns the basis; you implement to it.

## 6. Glossary

- **Play** — a single signal→action strategy.
- **Waterfall** — querying data sources in sequence, stopping at first verified hit, paying only for hits.
- **Rung** — maturity level (Foundation / Modeling / Activation).
- **ICP** — Ideal Customer Profile.
- **Signal** — a time-bound reason to reach out now.
- **Speed-to-lead** — time from signal/inbound to first human touch (the metric that most often moves conversion).
- **Templating** — freezing a proven play as a one-command skill.

## 7. Update log

- 2026-06-08 — File created. Research synthesised from Clay GTM blog, Apollo, Octave, SyncGTM, DevCommX, HBR 2024. Benchmarks are industry figures, not any client result.
