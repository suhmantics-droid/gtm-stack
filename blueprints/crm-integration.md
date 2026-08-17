# Blueprint 12 - CRM integration (HubSpot / Salesforce)

## What it does
Reads and writes a client's system of record (HubSpot, Salesforce, Pipedrive) so plays land where
the revenue team actually works - instead of, or alongside, a Google Sheet.

## Tools / patterns
- The CRM's REST API (HubSpot CRM API, Salesforce REST/Bulk API) with an API key / OAuth app.
- An MCP server for the CRM if one exists; otherwise a thin Python client (same shape as our CH/Sheets clients).
- Field mapping: your pipeline's columns → the CRM's properties/objects.

## How it fits (and what we deliberately didn't do)
- **We stayed Sheets-only** in this project - Google Sheets was the data home, by choice, for a lean
  human-in-the-loop motion. We did **not** integrate a CRM. So treat this as recommended practice,
  not lived experience.
- **When you'd add it:** the client's system of record is a CRM and they want plays writing there
  (lead creation, enrichment write-back, signal flags on existing records). Capture CRM access in the
  client brief (`../gtm-engineering/clients/_TEMPLATE.md` §3) before assuming it.

## Blueprint: stand it up at a new company
1. Confirm access level: read, read-write, or none. Get an API key / connected OAuth app.
2. Map fields once: define which pipeline fields map to which CRM properties/objects.
3. **Write idempotently** - dedup on a stable key (domain, email, CRM record ID) so re-runs don't
   create duplicates. This is where CRM hygiene lives or dies.
4. Mirror, don't fight: if the CRM is the source of truth, the sheet becomes a staging area, not a
   competing record.
5. Respect their schema and required fields; never bulk-write untested - test one record first.

## Gotchas / hard rules
- **Idempotent writes only** - match-or-create on a stable key, never blind-insert.
- **Their schema wins** - adapt to it; don't impose yours.
- **Test one record** before any batch (same rule as `/gtm-play`).
- API limits vary wildly (Salesforce Bulk vs HubSpot rate caps) - read the limits first.

## Cost
The CRM is the client's existing spend; integration cost is build time. No new tool needed.
