# Blueprint 14 - Scoring & routing

## What it does
Turns enriched records into a prioritised, assigned queue: a **fit × intent** score, a tier, and a
rule for who/what handles each record next.

## The model
- **Fit** (firmographic): does this match the ICP? (vertical, size, geography, stack.)
- **Intent** (behavioural/signal): how strong is the reason to reach out *now*? (funding, hiring, intent.)
- **Score = fit × intent.** High-fit + high-intent = act now; high-fit + low-intent = nurture;
  low-fit = park regardless of intent.
- **Route:** score/tier → destination (call sheet, sequence, a rep, a nurture track).

## How we used it
- We ran the **scoring half** for real: ICP tiering in `/qualify-batch` (Tier 1/2/3/X off a
  stack-signal + vertical + size proxy), and **Impact × Ease** ranking for plays. Both are fit×intent
  in practice.
- **Hard rule we enforced:** no Tier-1 without a real signal - scoring is signal-based or it's noise.
- **Routing we did lightly** - sorted call sheets (Tier → size → name). We did **not** build
  automated rep-assignment/round-robin; that's recommended practice below, not lived.

## Blueprint: stand it up at a new company
1. Define **fit** explicitly (the ICP as scoreable attributes) and **intent** (the signals that matter).
2. Make the score **legible** - a human should be able to see why a record is Tier 1.
3. Set routing rules: Tier 1 → act now / best rep; Tier 2 → nurture; out-of-ICP → park.
4. Keep it **auditable** - write the rules down; don't bury scoring in a black box.
5. Revisit thresholds against outcomes (Blueprint 17) - scores that don't predict meetings are wrong.

## Gotchas / hard rules
- **No top-tier without a signal** - fit alone isn't a buying reason.
- **Legible > clever** - a score nobody can explain won't be trusted or improved.
- **Tune on outcomes** - re-weight when the data says a factor isn't predictive.

## Cost
Free (logic). The discipline is keeping the model explicit and outcome-tuned, not elaborate.
