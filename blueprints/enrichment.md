# Blueprint 1 - Contact enrichment (email + phone)

## What it does
Takes a known person (name + company, or a LinkedIn URL) and returns a **verified** work
email and/or direct phone, by querying providers in sequence and stopping at the first real hit.

## Tools / scripts
- **Blitz** - work-email from a LinkedIn URL (`POST /v2/enrichment/email`, header `x-api-key`).
- **Lusha** - emails + direct/mobile phones, credit-metered (`GET /v2/person`, header `api_key`).
- Local scripts: `enrich.py` (the waterfall), `lusha_poc_batch.py`, `enrich_emails.ps1`.
- Verification helpers: brand-match against the company domain before recording.

## How we used it
- **Waterfall order, free/cheap first:** website scrape + Companies House officers + Parallel/Tavily
  for the LinkedIn URL → Blitz for the email → Lusha only as a last resort (it costs credits).
- **One company at a time**, verifying name + location + role match before writing anything.
- **The expensive lesson:** a 180-row pass of *pattern-guessed* emails (`first.last@domain`)
  produced a **~75% NXDOMAIN bust rate**. We banned guessed data outright after that. Blank +
  "needs research" beats a plausible-but-wrong address every time.
- **Lusha economics observed:** ~4 credits per successful lookup; re-fetching an already-revealed
  contact didn't re-charge (cached server-side). On a 16-company batch: 14/16 emails, 11/16 phones.
- We concluded **Blitz wasn't worth paying for** at our volume and leaned on free verified paths.

## Blueprint: stand it up at a new company
1. Decide the providers for the new ICP. Email-only? Add a phone provider only if you cold-call.
2. Put keys in `.env` (`BLITZ_API_KEY`, `LUSHA_API_KEY`, or whatever the new stack uses).
3. Define the **waterfall order** cheapest→dearest; wire each as a function that returns
   `{value, source, confidence}` and stops the chain on first verified hit.
4. Add a **brand-match check**: the returned email's domain must match the company's real domain.
5. Default every unknown to blank + a "needs research" flag. Never synthesise an address.
6. Gate any credit-metered call behind an explicit human "yes" with a cost estimate.

## Gotchas / hard rules
- **No pattern-guessed emails/phones/URLs - ever.** This is the rule the whole pipeline exists to enforce.
- **Verify the person** (name + location + role) before recording.
- **Per-call OK for credit spend.** Show "N lookups × cost ≈ X credits (balance: Y). Proceed?".
- Email **verification ≠ discovery** - a found address still needs an MX/validity check.

## Cost
Free paths first (scrape, CH, Parallel). Blitz ~per-call. Lusha ~4 credits/lookup. Budget by
capping credits in code and confirming before every paid batch.
