"""GTM-E signal runner: NEW UK COMPANY FORMATIONS in a target vertical.

Powers play A1 (fresh incorporation in an ICP vertical) from gtm-engineering/PLAYS.md.
Free - uses COMPANIES_HOUSE_API_KEY from .env. No spend, no paid enrichment, no
guessed data: every row is a real Companies House record.

Get a free API key at:
  https://developer.company-information.service.gov.uk/

Usage:
  uv run --with requests python scripts/gtm_formation_signal.py --sic 56101 --days 30 --limit 100

Reads .env from the repo root by default. Override with GTM_ENV_PATH.

Args:
  --sic     One or more SIC codes (repeat or comma-separate). REQUIRED.
  --days    Look-back window in days for incorporation date. Default 30.
  --status  Company status filter (default: active). Use 'any' to disable.
  --limit   Max rows to return. Default 200 (account-safety / sanity cap).
  --out     Output JSON path. Default gtm_formation_<firstsic>_<stamp>.json
            (stamp passed in so the script stays deterministic / testable).
  --stamp   Optional label for the output filename (e.g. a date). Cosmetic only.

Output: a JSON list of {company_number, company_name, date_of_creation,
sic_codes, address, status} sorted newest-first, plus a console summary.
The JSON is ready to hand to /gtm-play for enrichment + scoring.
"""
import os, sys, json, argparse
from datetime import date, timedelta
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = Path(os.environ.get("GTM_ENV_PATH", REPO_ROOT / ".env"))
B = "https://api.company-information.service.gov.uk"


def load_key():
    """Prefer a real environment variable; fall back to the repo .env file."""
    key = os.environ.get("COMPANIES_HOUSE_API_KEY")
    if key:
        return key
    if not ENV_PATH.exists():
        sys.exit(
            f"No COMPANIES_HOUSE_API_KEY in the environment and no .env at {ENV_PATH}.\n"
            "Copy .env.example to .env and add a free key from "
            "https://developer.company-information.service.gov.uk/"
        )
    env = {}
    for line in ENV_PATH.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            k, _, v = line.partition("=")
            env[k.strip()] = v.strip()
    if not env.get("COMPANIES_HOUSE_API_KEY"):
        sys.exit(f"COMPANIES_HOUSE_API_KEY is empty in {ENV_PATH}.")
    return env["COMPANIES_HOUSE_API_KEY"]


def fetch(auth, sics, inc_from, status, limit):
    """Page through CH advanced-search until limit or exhaustion."""
    rows, start, page = [], 0, 100
    while len(rows) < limit:
        params = {
            "sic_codes": sics,            # list -> repeated param (AND-free OR match)
            "incorporated_from": inc_from,
            "size": page,
            "start_index": start,
        }
        if status and status.lower() != "any":
            params["company_status"] = status
        r = requests.get(f"{B}/advanced-search/companies", params=params, auth=auth, timeout=30)
        if r.status_code == 429:
            # CH limit is 600/5min; a single paged run won't hit it, but be safe.
            import time
            time.sleep(2)
            r = requests.get(f"{B}/advanced-search/companies", params=params, auth=auth, timeout=30)
        if r.status_code != 200:
            print(f"  ! HTTP {r.status_code} at start_index={start}: {r.text[:200]}")
            break
        items = r.json().get("items", [])
        if not items:
            break
        for it in items:
            addr = it.get("registered_office_address") or {}
            rows.append({
                "company_number": it.get("company_number"),
                "company_name": it.get("company_name"),
                "date_of_creation": it.get("date_of_creation"),
                "sic_codes": it.get("sic_codes"),
                "status": it.get("company_status"),
                "locality": addr.get("locality"),
                "postal_code": addr.get("postal_code"),
            })
        start += len(items)
        if len(items) < page:
            break
    # newest first, then trim to limit
    rows.sort(key=lambda x: x.get("date_of_creation") or "", reverse=True)
    return rows[:limit]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sic", required=True, nargs="+", help="SIC code(s): space- or comma-separated")
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--status", default="active")
    ap.add_argument("--limit", type=int, default=200)
    ap.add_argument("--out", default=None)
    ap.add_argument("--stamp", default=None)
    a = ap.parse_args()

    sics = [s.strip() for tok in a.sic for s in tok.replace(",", " ").split() if s.strip()]
    inc_from = (date.today() - timedelta(days=a.days)).isoformat()
    auth = (load_key(), "")

    print(f"SIC {sics} | incorporated since {inc_from} | status={a.status} | limit={a.limit}")
    rows = fetch(auth, sics, inc_from, a.status, a.limit)

    stamp = a.stamp or date.today().isoformat()
    out = a.out or str(P / f"gtm_formation_{sics[0]}_{stamp}.json")
    Path(out).write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nFound {len(rows)} new formations.")
    for r in rows[:10]:
        print(f"  {r['date_of_creation']}  {r['company_number']}  {r['company_name']}  "
              f"({r.get('locality') or '?'})")
    if len(rows) > 10:
        print(f"  ... +{len(rows) - 10} more")
    print(f"\nwrote -> {out}")
    print("Next: hand this JSON to /gtm-play A1 for enrichment + scoring (no spend yet).")


if __name__ == "__main__":
    main()
