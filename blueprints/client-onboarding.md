# Blueprint 20 - Client / role onboarding

## What it does
The first-week checklist for standing the stack up against a new client or employer: intake,
access, accounts, and a clean kickoff so you're producing inside days.

## Tools
- The intake step in `/gtm-audit` (writes the client brief) - the discovery half.
- The `/onboard`-type setup flow - standing up MCP servers, `.env` keys, the OAuth/service-account
  auth, skills, and scripts on a new machine/accounts.
- The client brief template (`../gtm-engineering/clients/_TEMPLATE.md`) as the intake artifact.

## How we used it
- We built both halves: the **discovery intake** (gtm-audit → brief) and a **technical setup flow**
  for getting the whole toolkit running on a new person's machine and accounts. That setup flow is
  the model for onboarding into any new environment.

## Onboarding checklist
1. **Intake** - fill the client brief: ICP, geography, system of record, data access, first-party
   data, suppression list, sending identity, current numbers, lawful basis.
2. **Access** - API keys into `.env` (their accounts or yours, agreed), CRM/Sheets access, OAuth /
   service-account auth set up (Blueprint 5/6).
3. **Tooling** - register MCP servers in `.mcp.json` with full paths; secrets via `.env`.
4. **Skills** - port the generic skills; rebuild only the company-specific ones (voice, ICP tiers).
5. **Guardrails** - seed memory with the standing rules + the new house voice/ICP.
6. **Kickoff play** - run one quick-win play end to end to prove the motion in week one.

## Blueprint: stand it up at a new company
Run the checklist top to bottom. The brief is the source of truth everything else reads; fill it
*first*. Prove value with one play fast - momentum beats a perfect setup.

## Gotchas / hard rules
- **Whose accounts/keys?** Agree this up front (theirs vs yours) and record it; don't run a new
  employer's work on a previous one's keys.
- **Lawful basis + access in writing** before you touch data.
- **Brief first** - don't improvise context; fill the brief, then build.

## Cost
Free (process). The cost is doing it thoroughly before producing - a day saved here loses a week later.
