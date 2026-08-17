# Blueprint 15 — Sequencing & deliverability

## What it does
The send-at-volume layer: multi-touch sequences, sending infrastructure, and inbox health. This is
the piece our own motion **deliberately stops short of** — documented here so you know how to add it
when a client genuinely needs volume.

## Tools
- **Sequencers:** Smartlead, Instantly (together ~40% of new outbound starts), Lemlist, Outreach, Salesloft.
- **Deliverability:** dedicated sending domains, warmup tools, SPF / DKIM / DMARC records.
- **Validation:** an email-verification step before any send.

## How it fits (what we did vs didn't)
- **We did NOT send at volume.** Our motion is **drafts-not-sends** (Blueprint 7): every message is a
  human-reviewed Gmail draft. No sequencer, no warmup, no bulk-send. That's a deliberate trust and
  compliance boundary, not a gap.
- **When you'd add this:** a client wants real outbound volume across many recipients. Then sequencing
  + deliverability become essential — and so does the discipline below, or you torch domains.

## Blueprint: stand it up at a new company
1. **Never send from the primary domain.** Buy dedicated sending domains; warm them for weeks before volume.
2. Set **SPF, DKIM, DMARC** correctly on every sending domain — non-negotiable for inbox placement.
3. Verify every address (Blueprint 1) before it enters a sequence — bounces wreck sender reputation.
4. Keep volume per inbox low and ramp slowly; rotate inboxes.
5. Honour **suppression lists and opt-outs** automatically (Blueprint 18).
6. Measure deliverability (inbox vs spam), not just opens.

## Gotchas / hard rules
- **Warm domains first** — cold-blasting a fresh domain gets it blacklisted fast.
- **Auth records (SPF/DKIM/DMARC) before anything** — skip these and you land in spam.
- **Verify before send** — bounces destroy reputation.
- **Suppression is mandatory** — one un-honoured opt-out is a compliance problem, not a metric.
- This is a different risk profile from our draft-only motion — adopt it eyes-open.

## Cost
Sequencer (~$80-100/mo), sending domains (~$8 each/mo), warmup tooling (~$25-40/mo). A real line
item — only justified when volume is genuinely needed.
