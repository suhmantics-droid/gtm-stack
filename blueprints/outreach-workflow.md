# Blueprint 7 - Outreach workflow (enrich → research → draft → measure)

## What it does
Turns a target into a personalised, human-reviewed outreach draft - and tracks whether it worked.
The *method* is transferable; the house voice and proof points are company data, kept out of here.

## Tools / scripts
- Enrichment (Blueprint 1) for the contact; firmographics (Blueprint 2) + web (Blueprint 4) for context.
- **Google Workspace MCP** - creates **Gmail drafts** (never sends).
- A drafting skill that holds the house style (e.g. a `/draft-outreach`-type skill - voice is per-company).
- Measurement (see `../gtm-engineering/MEASUREMENT.md`) - the fired/replied/converted readout.

## How we used it
- **One repeatable chain:** identify the buyer persona → enrich one verified contact (gated) →
  research the company + role for a specific opener → draft in the house voice referencing a real
  signal → create a **Gmail draft** for a human to review and send.
- **Never auto-send.** Every message is a draft. A person sends. This is a hard line, not a setting.
- **Signal-referencing openers** (their stack, a new store, a raise) consistently beat generic ones.
- **Close the loop:** reconcile drafts against **Gmail Sent** to see what actually went out, then
  track replies/meetings. Drafts piling up unsent is itself a signal (a throughput problem).
- **Style rules are company-specific** and live in memory/skills, not here - e.g. a house may ban
  em-dashes, ban emojis to prospects, or fix a standard CTA. Capture those per employer.

## Blueprint: stand it up at a new company
1. Write the **house voice** as a skill + a memory note (opener style, CTA, banned tokens, proof
   points). This is the one genuinely company-specific asset - rebuild it per employer.
2. Wire the chain: persona → gated enrichment → context research → draft → Gmail draft.
3. Stand up the **measurement sheet** (Blueprint 5) and the Gmail-Sent reconcile from day one.
4. Keep the **drafts-not-sends** rule regardless of employer - it's a trust and compliance safeguard.

## Gotchas / hard rules
- **Drafts, not sends.** Always.
- **No guessed contacts** in the draft - verified email or don't send.
- **Compliance:** cold B2B in the UK/EU leans on legitimate interest (GDPR/PECR) - honour opt-outs;
  on a client's behalf, their legal owns the basis.
- Voice/style is **company data** - don't carry one employer's proof points into another's outreach.

## Cost
Free (Gmail drafts via Workspace MCP). Cost sits in the enrichment step, which is gated.
