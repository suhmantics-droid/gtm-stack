# Blueprint 13 — Data hygiene (dedup, identity, normalisation)

## What it does
Turns a messy list into a clean one: one row per entity, consistent keys, no duplicates. This is
the **Rung-1 foundation fix** — the step before any scoring or activation can be trusted.

## Tools / scripts
- `derive_domains.py` — LinkedIn-company URL → root domain (the canonical join key).
- Dedup-by-domain-root logic (collapse `www.` / `shop.` / `m.` to one root).
- LLM-assisted matching (Blueprint 11) for fuzzy "same entity?" calls.
- Companies House (Blueprint 2) to resolve a name to a canonical legal entity.

## How we used it
- **Domain-root as the join key.** We deduped by collapsing subdomains to a root so the same company
  never got scanned, enriched, or contacted twice. The enrichment and qualification pipelines shared
  one cache off this key.
- **Best-match, not first-match.** Resolving a name to a CH entity used active-status + normalised-name
  overlap scoring, not "grab the first search hit" — which prevents wrong-entity contamination.
- **Normalise before you trust counts.** "5,000 rows" means nothing if 1,500 are dupes; we counted
  *after* dedup.

## Blueprint: stand it up at a new company
1. Pick the **canonical key** (domain root is usually best; LinkedIn URL or CRM ID otherwise).
2. Normalise: lowercase, strip subdomains/`www`, trim legal suffixes for name matching.
3. Dedup on the key; for fuzzy cases use LLM "same entity?" reasoning with a confidence threshold.
4. Resolve names to canonical entities (CH for UK) before recording.
5. Stand up **one** source-of-truth list; everything else references it.

## Gotchas / hard rules
- **Dedup before you report** — vanity counts on dirty data mislead.
- **Best-match scoring**, never blind first-hit, when resolving names.
- **One source of truth** — never let two competing "master" lists exist.
- Keep the dedup key stable across the whole pipeline so caches line up.

## Cost
Free (logic + CH). The cost is doing it *first*, before activation — skipping it reproduces the
75% NXDOMAIN failure at scale.
