# Blueprint 18 — Compliance & data protection

## What it does
Keeps cold outbound and data handling legal — especially when run **on a client's behalf**. The
guardrails that protect you, the client, and the people in the list.

## The essentials (UK/EU focus)
- **Lawful basis:** B2B cold email to corporate addresses generally relies on **legitimate interest**
  under GDPR, with PECR governing electronic marketing. You must be able to *justify* the interest,
  not just assert it.
- **Opt-out / suppression:** every contact can opt out; opt-outs are honoured **automatically and
  permanently**. Maintain a suppression list and check it before every send.
- **Personal vs corporate data:** prefer role/corporate addresses; treat individuals' personal data
  with more care. Don't process more than you need.
- **Retention:** keep data only as long as there's a basis; delete on request.

## How we used it
- We enforced the **data-quality side** as a compliance practice: **no guessed/scraped personal data**,
  verified sourced contacts only. That's both a quality rule and a lawful-processing one.
- Compliance is referenced in the system (`../gtm-engineering/PLAYBOOK.md` §6c, RESOURCES guardrails),
  and each client brief records the lawful basis (`clients/_TEMPLATE.md` §7).
- We did **not** run high-volume sending, which is where most compliance risk concentrates — see
  Blueprint 15.

## Blueprint: stand it up at a new company
1. **Record the lawful basis per engagement** in the client brief. On a client's behalf, *their*
   legal/DPO owns the basis — you implement to it, you don't invent it.
2. Stand up a **suppression list** from day one; wire it into every send and every recurring scan.
3. Default to **corporate/role data**; minimise personal data; document retention.
4. Make opt-out one-click and permanent; honour it across all future runs.
5. Keep sources auditable — every contact traces to where it came from.

## Gotchas / hard rules
- **Legitimate interest must be justifiable**, not assumed.
- **Suppression is mandatory and permanent** — re-contacting an opt-out is a breach, not a metric slip.
- **Client owns the lawful basis** on their engagements; get it in writing.
- **No guessed personal data** — it's a compliance rule as much as a quality one.

## Cost
Free (it's discipline + a suppression list). The cost of skipping it is regulatory and reputational —
far higher than any tool.
