# Client Brief - <Business Name>

> One brief per client business. Copy this file to `clients/<business-slug>.md` and fill it.
> `/gtm-audit` writes/updates this from intake + research. `/gtm-play` and
> `/gtm-skill-builder` READ it as the single source of truth - they never re-derive
> context. Unknown = leave blank + `(needs intake)`. Never guess.

**Slug:** `<business-slug>`
**Last updated:** <YYYY-MM-DD>
**Maturity rung:** <1 Foundation | 2 Modeling | 3 Activation> - <one-line reason>
**GTM-E fit:** <Yes | Partial | No> - <reason; see PLAYBOOK §5a fit gate>

---

## 1. The business (verified facts only)
- **What they sell:**
- **To whom (their ICP):**
- **Geography of their buyers:** <UK | US | EU | global> - drives which signal sources work (see §6)
- **Size / stage:** <headcount, revenue band, funding stage if known>
- **Physical presence:** <stores / venues / none>
- **Detected tech stack:** <urlscan result - CRM/ESP/e-comm>
- **Source notes:** <where each fact came from - CH number, site URL, Parallel excerpt>

## 2. Current GTM motion (what they do today)
- **Primary motion:** <inbound / outbound / PLG / retail-field / partner>
- **Team:** <do they have SDRs? marketers? RevOps?>
- **Current numbers (from intake):** <meetings/mo, reply rate, list size, conversion - blank if not shared>
- **What's broken / the ask:** <why they want help>

## 3. Data & access (from intake - the part research can't see)
- **System of record:** <CRM name / Google Sheet / spreadsheet chaos / none>
- **CRM access for us?** <read | read-write | none>
- **First-party data available?** <reverse-IP / analytics / form webhook / none> - gates plays E1, E2
- **Existing contact list?** <size, freshness, format>
- **Do-not-contact / suppression list?** <exists? where?>
- **Sending identity:** <whose domain/inbox sends; warmed?>

## 4. ICP definition (sharpened with the client)
- **Firmographic:** <vertical, size, geography, tech>
- **Persona / buying committee titles:**
- **Disqualifiers:** <who is NOT a fit>
- **SIC codes (UK):** <for formation/CH plays>

## 5. Selected plays (the roadmap)
| Play | Signal | Rung | Impact×Ease | Status | Data home | Runner |
|---|---|---|---|---|---|---|
| <C1> | <tech-stack> | 2 | <score> | <proposed/testing/live/killed> | <sheet> | `qualify-batch` |
| <A1> | <formation> | 2 | <score> | <...> | <sheet> | `gtm_formation_signal.py` |

**Quick-win pick:** <play> · **Structural pick:** <play>

## 6. Signal availability for THIS client
Mark each PLAYS.md family: available now / needs client data / not applicable.
- A formation (UK only): <>
- B hiring: <>
- C tech-stack: <>
- D funding: <>
- E web-intent (needs first-party): <>
- F reputation/expansion: <>

## 7. Hard rules / guardrails for this engagement
Carry the standing rules (no guessed data · per-call OK for spend · new-sheet-never-overwrite ·
drafts-not-sends) PLUS anything client-specific:
- **Spend cap:** <e.g. Lusha credits/week>
- **Source-of-truth doc/sheet:**
- **Compliance basis:** <legitimate interest / consent; GDPR-PECR if UK/EU - see PLAYBOOK §6c>
- **Other:**

## 8. Measurement
- **Results home:** <sheet/tab - see MEASUREMENT.md>
- **What "working" means here:** <reply rate / meeting / pipeline threshold to scale vs kill>
- **Review cadence:** <weekly / per-play window>

## 9. Log
- <YYYY-MM-DD> - <what happened: audit run / play X tested / play X went live / killed>
