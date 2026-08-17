"""Direct Google Sheets API client - service-account backed.

Why a service account and not OAuth: a Desktop OAuth client whose consent screen
sits in 'Testing' mode has its refresh token revoked every 7 days. A service
account has no browser flow, no refresh tokens and no expiry, so unattended jobs
keep working.

Usage:
    from sheets_api import service, write_range, read_range
    write_range(SHEET_ID, "Master!A1:B2", [["x", "y"], ["1", "2"]], "RAW")

Setup:
    1. Google Cloud Console -> IAM -> Service Accounts -> create one.
    2. Keys -> Add key -> JSON. Save it as service_account.json next to this repo.
    3. Enable the Sheets API (and Drive API if you also read file metadata).
    4. Share any target sheet with the service account's email as Editor.
       The email is in the JSON as "client_email".

Config (both optional, sensible defaults):
    GOOGLE_SERVICE_ACCOUNT_JSON  path to the key file. Default: ./service_account.json
    SHEETS_SELFTEST_ID           sheet id used by the __main__ self-test.

Known gotcha: a service account CANNOT create a new spreadsheet in a normal
Drive. Create the sheet by hand (or via an OAuth client), share it with the
service account, then write to it here.

Required packages: google-api-python-client, google-auth
    uv run --with google-api-python-client --with google-auth python scripts/sheets_api.py
"""
import os
import sys
from pathlib import Path

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Default to a key file sitting at the repo root. Override with the env var.
REPO_ROOT = Path(__file__).resolve().parent.parent
SA_PATH = Path(os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", REPO_ROOT / "service_account.json"))


def _get_creds():
    from google.oauth2 import service_account

    if not SA_PATH.exists():
        raise RuntimeError(
            f"Service account key missing at {SA_PATH}.\n"
            "Create one at Google Cloud Console -> IAM -> Service Accounts -> Keys -> "
            "Add key -> JSON, save it there, and share your sheet with its client_email "
            "as Editor. Or set GOOGLE_SERVICE_ACCOUNT_JSON to the key's path."
        )
    return service_account.Credentials.from_service_account_file(str(SA_PATH), scopes=SCOPES)


def service():
    from googleapiclient.discovery import build

    return build("sheets", "v4", credentials=_get_creds(), cache_discovery=False)


def write_range(spreadsheet_id, range_name, values, value_input_option="RAW"):
    return (
        service()
        .spreadsheets()
        .values()
        .update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption=value_input_option,
            body={"values": values},
        )
        .execute()
    )


def read_range(spreadsheet_id, range_name):
    r = (
        service()
        .spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range=range_name)
        .execute()
    )
    return r.get("values", [])


if __name__ == "__main__":
    # Self-test: round-trips one throwaway cell on a sheet you nominate.
    # Set SHEETS_SELFTEST_ID to a sheet the service account can edit.
    sys.stdout.reconfigure(encoding="utf-8")

    sid = os.environ.get("SHEETS_SELFTEST_ID")
    if not sid:
        sys.exit(
            "Set SHEETS_SELFTEST_ID to a spreadsheet id the service account can edit, "
            "then re-run. Nothing was changed."
        )

    probe_range = os.environ.get("SHEETS_SELFTEST_RANGE", "Sheet1!Z1:Z1")

    print(f"loading service-account creds from {SA_PATH}")
    creds = _get_creds()
    print(f"  service account: {creds.service_account_email}")
    print(f"  scopes: {creds.scopes}")

    print(f"\nwrite test -> {probe_range}")
    print(write_range(sid, probe_range, [["probe-ok"]], "RAW"))
    print("read test ->", read_range(sid, probe_range))

    print("clearing probe cell")
    write_range(sid, probe_range, [[""]], "RAW")
    print("\nDONE. Service-account Sheets API is live.")
