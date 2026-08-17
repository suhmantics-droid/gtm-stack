"""Derive a company-domain mapping from the deduped CSV.

Strategy: for each unique company name, generate domain candidates
(name.com / name.co.uk / name.io), DNS-resolve each, keep the first hit.
Stores resolved + unresolved separately so the unresolved can be manually
filled later.
"""
import csv
import json
import os
import re
import socket
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
# Override either with an env var, e.g. DERIVE_SRC=data/my-companies.csv
SRC = Path(os.environ.get("DERIVE_SRC", REPO_ROOT / "companies.csv"))
OUT = Path(os.environ.get("DERIVE_OUT", REPO_ROOT / "company_domains.json"))

SUFFIXES = [
    " limited", " ltd", " inc", " inc.", " plc", " corporation",
    " corp", " corp.", " group", " co ltd", " co. ltd", " holdings",
    " uk", " (uk)",
]


def clean_name(company: str) -> str:
    name = company.strip().lower()
    for suffix in SUFFIXES:
        if name.endswith(suffix):
            name = name[: -len(suffix)].strip()
    # Replace & → and, drop apostrophes/quotes, collapse spaces
    name = name.replace("&", "and").replace("'", "").replace("’", "")
    name = name.replace("/", "-")
    # Strip everything except alphanumeric and hyphens
    name = re.sub(r"[^\w\-]", "", name)
    name = re.sub(r"_+", "", name)
    return name


def candidates(company: str) -> list[str]:
    base = clean_name(company)
    if not base:
        return []
    out = [
        f"{base}.com",
        f"{base}.co.uk",
        f"www.{base}.com",
        f"www.{base}.co.uk",
        f"{base}.io",
    ]
    # Dedupe preserving order
    seen = set()
    result = []
    for d in out:
        if d not in seen:
            seen.add(d)
            result.append(d)
    return result


def resolves(domain: str) -> bool:
    try:
        socket.setdefaulttimeout(2.0)
        socket.gethostbyname(domain)
        return True
    except (socket.gaierror, socket.timeout, OSError):
        return False


with open(SRC, encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

companies = sorted(set(r["Company"].strip() for r in rows))
print(f"Unique companies: {len(companies)}")

resolved: dict[str, str] = {}
unresolved: list[str] = []
for i, c in enumerate(companies, 1):
    hit = None
    for cand in candidates(c):
        # Strip www. for the final stored domain
        bare = cand[4:] if cand.startswith("www.") else cand
        if resolves(cand):
            hit = bare
            break
    if hit:
        resolved[c] = hit
    else:
        unresolved.append(c)
    if i % 25 == 0:
        print(f"  ...{i}/{len(companies)} processed")

print(f"\nResolved:   {len(resolved)}")
print(f"Unresolved: {len(unresolved)}")
if unresolved:
    print(f"First 10 unresolved: {unresolved[:10]}")

OUT.write_text(
    json.dumps({"resolved": resolved, "unresolved": unresolved}, ensure_ascii=False, indent=2),
    encoding="utf-8",
)
print(f"\nSaved → {OUT}")
