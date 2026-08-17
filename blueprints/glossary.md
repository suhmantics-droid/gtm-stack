# Blueprint glossary

Plain-English definitions for the terms used across the blueprints and the GTM-E system.

| Term | Meaning |
|---|---|
| **GTM** | Go-to-market — how a business reaches and wins customers. |
| **GTM Engineering (GTM-E)** | Building revenue *systems* (signal → action pipelines) instead of adding headcount. |
| **Play** | A single strategy: this signal → this action. The unit of work. |
| **Signal** | A time-bound reason to reach out now (funding, hiring, tech install, new store…). |
| **The loop** | signal → enrich → score → route → act → measure → (kill or template). |
| **Waterfall** | Querying data providers cheapest→dearest, stopping at first verified hit, paying only for hits. |
| **Enrichment** | Filling in missing data (email, phone, firmographics) for a known target. |
| **Discovery / prospecting** | Finding *new* companies/people that match an ICP. |
| **Firmographics** | Company-level facts: size, sector, location, age, structure. |
| **ICP** | Ideal Customer Profile — who you're actually trying to reach. |
| **Tiering** | Ranking records by fit (Tier 1/2/3/X) so you work the best first. |
| **Fit × intent** | Scoring model: does it match (fit) × is there a reason now (intent). |
| **Maturity rung** | Foundation → Modeling → Activation: how data-mature a business is. |
| **Data home** | The single live place records live (a Sheet or CRM). |
| **Source of truth** | The one authoritative record everything else references. |
| **Suppression list** | Contacts that must never be emailed (opt-outs, do-not-contact). |
| **Deliverability** | Whether your email reaches the inbox vs spam (SPF/DKIM/DMARC, warmup). |
| **Sequencer** | Tool that sends multi-touch outbound at volume (Smartlead, Instantly…). |
| **Speed-to-lead** | Time from a signal/inbound to first human touch — the metric that most moves conversion. |
| **Kill / scale / iterate** | The verdict on a play from its scorecard. |
| **Templating** | Freezing a proven play into a one-command skill. |
| **MCP** | Model Context Protocol — servers that give Claude live tools/data. |
| **Subagent MCP wall** | Spawned subagents are permission-denied on some MCP tools; use REST on the main thread. |
| **Skill** | A one-command Claude Code workflow (`/name`) — a frozen, proven pipeline. |
| **Service account** | A non-human Google identity for reliable automated Sheets writes. |
| **Legitimate interest** | The usual GDPR lawful basis for B2B cold email (must be justifiable). |
| **NXDOMAIN** | A domain that doesn't resolve — the tell of a guessed/dead email. |
| **No guessed data** | The core rule: verified, sourced data only; unknown = blank + flag. |
