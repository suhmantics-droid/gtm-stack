# Blueprint 5 - Data home (Google Sheets via service account)

## What it does
Gives the team a live, shared data home that scripts can read and write reliably - the call
sheets, prospect lists, and enrichment results all land here.

## Tools / scripts
- **Service account** (`service_account.json`) - the reliable write path. Scope `spreadsheets`.
- Scripts: `sheets_api.py` (Python import: `from sheets_api import service, write_range, read_range`),
  `sheets_helper.py` (JSON-ops runner via `uvx` for shell/PowerShell use).
- **Google Workspace MCP** (`mcp__google-workspace__*`) - used to **create** new sheets and for
  Gmail/Calendar.

## How we used it
- **Service account for all writes.** We migrated off OAuth Desktop because its refresh tokens got
  revoked every 7 days while the consent screen sat in "Testing". The service account has no browser
  flow, no expiry - it just needs to be added as **Editor** on each sheet it writes to.
- **The create gotcha (learned the hard way):** a service account **cannot create new sheets** -
  it 403s ("caller does not have permission") because it has no Drive storage quota. It can only
  write to sheets already shared with it. **Fix:** create the sheet with the **Workspace MCP**
  (`create_spreadsheet`, owned by the real user, lands in their Drive), then either write via the
  MCP or share the service account onto it and write via `sheets_api.py`.
- **Write gotchas:** phone columns as **RAW** (preserve `+44`); chunk big writes (~75 rows/batch);
  always write to a **new** sheet, never overwrite the source.

## Blueprint: stand it up at a new company
1. Create a Google Cloud project, enable the **Sheets** (and **Drive**, for sharing) APIs.
2. Create a service account, download its JSON key → `service_account.json` (gitignored).
3. Drop in `sheets_api.py` / `sheets_helper.py`, point `SA_PATH` at the key.
4. **To create a sheet:** use the Workspace MCP as the real user; **to write at scale:** add the
   service-account email as Editor, then use the script.
5. For Gmail/Calendar, register the Workspace MCP in `.mcp.json` (OAuth as the real user).

## Gotchas / hard rules
- **Service account ≠ creator.** Create via the user (MCP); write via the service account.
- **RAW for phone columns;** new sheet, never overwrite.
- Keep `service_account.json` and `client_secret.json` **out of git** (`.gitignore`).
- The Workspace MCP's Docs API may be disabled on a given project - Drive export is the fallback.

## Cost
Free. Google Cloud APIs + Sheets are free at this volume.
