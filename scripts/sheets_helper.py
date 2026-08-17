"""
Direct Google Sheets writer using service account credentials.
Run via: uvx --from google-api-python-client --with google-auth python sheets_helper.py <ops.json>

ops.json schema:
{
  "spreadsheet_id": "...",
  "operations": [
    {"type": "write",      "range": "Tab!A1:Z100", "values": [["x", "y"], ...], "value_input_option": "RAW"},
    {"type": "read",       "range": "Tab!A1:Z100"},
    {"type": "create_tab", "title": "New Tab",     "rows": 1000, "cols": 26},
    {"type": "list_tabs"},
    {"type": "ping"}
  ]
}

Prints a JSON result list, one per op.
"""
import json
import os
import sys
from pathlib import Path
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

REPO_ROOT = Path(__file__).resolve().parent.parent
# Point GOOGLE_SERVICE_ACCOUNT_JSON at your key file, or drop it at the repo root.
SA_PATH = str(Path(os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", REPO_ROOT / "service_account.json")))
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "no ops file given"}))
        sys.exit(1)
    ops_path = Path(sys.argv[1])
    if not ops_path.exists():
        print(json.dumps({"error": f"ops file not found: {ops_path}"}))
        sys.exit(1)

    ops_doc = json.loads(ops_path.read_text(encoding="utf-8-sig"))
    spreadsheet_id = ops_doc["spreadsheet_id"]
    operations = ops_doc["operations"]

    creds = service_account.Credentials.from_service_account_file(SA_PATH, scopes=SCOPES)
    service = build("sheets", "v4", credentials=creds, cache_discovery=False)
    sheets = service.spreadsheets()

    results = []
    for op in operations:
        op_type = op["type"]
        try:
            if op_type == "ping":
                meta = sheets.get(spreadsheetId=spreadsheet_id, fields="properties.title").execute()
                results.append({"op": "ping", "ok": True, "title": meta["properties"]["title"]})

            elif op_type == "list_tabs":
                meta = sheets.get(spreadsheetId=spreadsheet_id,
                                  fields="sheets.properties").execute()
                tabs = [{"title": s["properties"]["title"],
                         "sheetId": s["properties"]["sheetId"]} for s in meta.get("sheets", [])]
                results.append({"op": "list_tabs", "ok": True, "tabs": tabs})

            elif op_type == "read":
                r = sheets.values().get(spreadsheetId=spreadsheet_id, range=op["range"]).execute()
                results.append({"op": "read", "ok": True,
                                "range": r.get("range"),
                                "values": r.get("values", [])})

            elif op_type == "write":
                rng = op["range"]
                values = op["values"]
                value_input_option = op.get("value_input_option", "RAW")
                r = sheets.values().update(
                    spreadsheetId=spreadsheet_id,
                    range=rng,
                    valueInputOption=value_input_option,
                    body={"values": values}
                ).execute()
                results.append({
                    "op": "write", "ok": True,
                    "range": r.get("updatedRange"),
                    "rows": r.get("updatedRows"),
                    "cols": r.get("updatedColumns"),
                    "cells": r.get("updatedCells"),
                })

            elif op_type == "create_tab":
                title = op["title"]
                rows = op.get("rows", 1000)
                cols = op.get("cols", 26)
                req = {
                    "addSheet": {
                        "properties": {
                            "title": title,
                            "gridProperties": {"rowCount": rows, "columnCount": cols}
                        }
                    }
                }
                r = sheets.batchUpdate(spreadsheetId=spreadsheet_id,
                                       body={"requests": [req]}).execute()
                new_sheet = r["replies"][0]["addSheet"]["properties"]
                results.append({"op": "create_tab", "ok": True,
                                "title": new_sheet["title"],
                                "sheetId": new_sheet["sheetId"]})

            else:
                results.append({"op": op_type, "ok": False, "error": "unknown op type"})

        except HttpError as e:
            results.append({"op": op_type, "ok": False,
                            "error": f"HTTP {e.resp.status}: {e._get_reason()}",
                            "details": e.error_details if hasattr(e, "error_details") else None})
        except Exception as e:
            results.append({"op": op_type, "ok": False, "error": str(e)})

    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
