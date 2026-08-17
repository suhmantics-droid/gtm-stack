# Blueprint 11 - AI in the loop (Claude as a GTM primitive)

## What it does
Uses an LLM (Claude) as a reusable step inside GTM pipelines - to classify, research, extract,
and personalise at scale. This is the modern core of GTM engineering: the judgement steps that
used to need a human now run as a prompt.

## The patterns (each is a reusable step)
- **Classify ICP fit** - "given this company's site + firmographics, is it [ICP]? Tier + reason."
- **Research & summarise** - turn a homepage + news into a 3-line brief (what they do, to whom, signals).
- **Extract structured data** - pull clean fields (stack, store count, persona) from messy text → JSON.
- **Match / dedup reasoning** - "are these two records the same entity?" beyond exact-string matching.
- **Personalise** - draft a signal-referencing opener in a house voice (gated, draft-only).
- **Completeness critic** - "what's missing / unverified here?" before a list is called done.

## How we used it
- We ran **all** of these this project: classifying companies for ICP tiering, researching a target
  end-to-end (e.g. building an audit from a homepage + a urlscan + news), extracting tech stacks into
  structured rows, and drafting outreach in a house voice.
- **The guardrail that makes it safe:** the LLM **reasons and drafts; it does not invent facts.**
  Any *data* point (email, phone, company fact) must trace to a real source - the model classifies
  and writes, it never fabricates a contact. This is the same no-guessed-data rule, applied to AI.
- **Structured output** (force a JSON schema) beats free-text parsing for anything downstream.
- **Verify before trust:** for high-stakes claims, a second pass ("refute this") catches plausible-
  but-wrong output.

## Blueprint: stand it up at a new company
1. Identify the **judgement steps** in your pipeline (fit, research, extraction, personalisation).
2. Write each as a prompt with a **schema** for the output, so it slots into a script.
3. Keep a hard line: **LLM for reasoning/drafting, sourced data for facts.** Never let it author a
   contact detail.
4. For scale, run these as steps inside the workflow (classify 500 companies, summarise each, etc.),
   with a verification pass on anything that triggers spend or outreach.

## Gotchas / hard rules
- **No hallucinated facts.** The model classifies and writes; data comes from sources. Non-negotiable.
- **Schema-constrain outputs** for anything a script consumes.
- **Verify high-stakes claims** with an adversarial second pass.
- Keep a human on the **send** - AI drafts, a person sends (Blueprint 7).

## Cost
The LLM subscription is the engine cost (flat). The leverage is enormous - judgement steps at the
cost of a prompt. The discipline is the guardrail, not the spend.
