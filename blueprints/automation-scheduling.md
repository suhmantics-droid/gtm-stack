# Blueprint 16 - Automation & scheduling

## What it does
Runs signal pipelines on a cadence so they work without you - daily formation scans, weekly funding
sweeps, monthly headcount checks. A signal you check once isn't a system; this makes it one.

## Tools
- **Claude Code scheduling** - the `schedule` skill (cron-style remote agents) and `loop` (interval runs).
- **Scheduled tasks** (OS task scheduler / cron) to run the Python signal scripts.
- **Firecrawl monitors** for site-change watching.
- General workflow glue (n8n, Make, Zapier) where a no-code trigger fits better.

## How it fits (what we did vs didn't)
- We **built the runnable pieces** (e.g. `gtm_formation_signal.py`) and have the scheduling tools
  available, but in-project we ran signals **on-demand**, not yet wired to a recurring cadence. So the
  scheduling pattern below is the recommended next step, lightly lived.
- The intent is explicit in the system: `MEASUREMENT` and the plays assume signals recur.

## Blueprint: stand it up at a new company
1. Identify which signals are **recurring** (formations daily, funding weekly, hiring weekly).
2. Wrap each as a script that writes to the data home and de-dupes against what's already seen.
3. Schedule it: `schedule` skill for agent-driven runs, OS cron for plain scripts, Firecrawl monitors
   for site changes.
4. **Suppress what's already actioned** - a recurring scan must not re-surface a contact you've touched.
5. Pipe new hits into the measurement sheet so the loop closes automatically.

## Gotchas / hard rules
- **De-dup across runs** - a daily scan needs a "seen" set or it re-surfaces the same companies.
- **Respect API caps on a schedule** - a cron job ignoring rate limits trips bans (urlscan 50/day, PB ≤4 launches/day).
- **Headless auth:** OAuth MCPs may be absent in cron/headless runs - use API keys / service accounts for scheduled work (Blueprint 6).
- Log what each run did, so a silent failure is visible.

## Cost
Free (the schedulers are built-in / OS). Cost is the underlying API usage, which the caps bound.
