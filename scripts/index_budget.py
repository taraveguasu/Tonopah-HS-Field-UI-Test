#!/usr/bin/env python3
"""
Index the Procore project budget and map every phase code to a bid package.

The phase code is the one field on the Attachment A Review Cover Sheet that
cannot be derived from any bid document -- it is CORE cost coding. This budget
supplies it for 31 of the 33 packages.

Code format, per PM direction: strip the cost-type suffix and the trailing
hyphen. Procore exports `31-2000-10000-.S`; the cover sheet carries
`31-2000-10000`. The suffix (.O other direct, .L direct labor, .S
subcontractor) is a Procore cost-type dimension, not part of the code.

Reconciles every subcontractor line against the carried value in
01-index/buyout-log.json and reports anything that does not agree, rather than
assuming the two sources match.

Usage:  python3 scripts/index_budget.py
"""

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "00-source-docs" / "07-budget" / "Procore Project Budget.csv"
LOG = ROOT / "01-index" / "buyout-log.json"
OUT = ROOT / "01-index" / "budget-phase-codes.json"

# Budget code (normalized) -> bid package. Built by matching the budget's own
# line description against the package title, then confirmed against the
# dollar amount; every one of these is checked below, none are assumed.
CODE_TO_PACKAGE = {
    "02-1010-10000": "ITB-008",
    "02-1110-10000": "RFP-002",
    "03-1000-10000": "RFP-030",
    "04-1000-10000": "RFP-031",
    "05-1000-10000": "RFP-033",
    "07-1000-10000": "ITB-040",
    "07-4100-10000": "RFP-045",
    "08-1000-10000": "ITB-056",
    "08-3050-10000": "ITB-054",
    "09-2000-10000": "RFP-060",
    "09-8100-10000": "ITB-067",
    "10-1020-10000": "ITB-071",
    "10-2020-10000": "ITB-074",
    "10-3050-10000": "ITB-078",
    "10-3070-10000": "ITB-072",
    "10-3120-10000": "ITB-077",
    "11-0080-10000": "ITB-085",
    "11-0101-10000": "ITB-089",
    "12-7340-10000": "RFP-094",
    "12-7400-10000": "RFP-109",
    "22-1000-10000": "RFP-098",
    "23-8000-10000": "RFP-100",
    "26-1000-10000": "RFP-103",
    "31-2000-10000": "RFP-008",
    "32-7100-10000": "RFP-023",
    "32-7600-10000": "ITB-018",
    "32-7605-10000": "ITB-019",     # supply
    "32-7610-10000": "ITB-019",     # track equipment install
    "32-7615-10000": "ITB-019",     # field equipment install
    "32-7620-10000": "RFP-021",
    "32-7650-10000": "RFP-022",
    "32-8000-10000": "RFP-016",
    "50-1000-10000": "ITB-070",
}

# Lines that are real cost but are not a bid package.
CORE_SELF_PERFORM = {"00-0010-10000", "00-0020-10000", "00-0021-10000", "26-7000-10000"}

SUFFIX = re.compile(r"-\.(O|L|S)$")


def normalize(code):
    """`31-2000-10000-.S` -> `31-2000-10000`."""
    return SUFFIX.sub("", (code or "").strip()).rstrip("-")


def classify(code):
    div = code.split("-")[0]
    if code in CODE_TO_PACKAGE:
        return "bid_package"
    if code in CORE_SELF_PERFORM:
        return "core_self_perform"
    if div == "01":
        return "general_conditions"
    if div == "80":
        return "allowance"
    if div == "85":
        return "bonds_and_insurance"
    if div == "90":
        return "contingency"
    if div == "98":
        return "fee"
    return "unclassified"


def build():
    rows = []
    with CSV_PATH.open(newline="", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            raw = (r.get("Budget Code") or "").strip()
            if not raw:
                continue
            code = normalize(raw)
            amt = (r.get("Original Budget Amount (A)") or "0").strip()
            rows.append(dict(
                budget_code_raw=raw,
                phase_code=code,
                cost_type=(r.get("Cost Type") or "").strip(),
                description=(r.get("Budget Code Description") or "").strip(),
                tier1=(r.get("Cost Code Tier 1") or "").strip(),
                amount=float(amt or 0),
                category=classify(code),
                package_id=CODE_TO_PACKAGE.get(code),
            ))

    log = {p["package_id"]: p for p in json.loads(LOG.read_text())["packages"]}

    # ---- one entry per package, summing its budget lines -------------------
    per_package, problems = {}, []
    for r in rows:
        if not r["package_id"]:
            continue
        e = per_package.setdefault(r["package_id"], dict(
            package_id=r["package_id"], phase_codes=[], budget_total=0.0, lines=[]))
        if r["phase_code"] not in e["phase_codes"]:
            e["phase_codes"].append(r["phase_code"])
        e["budget_total"] += r["amount"]
        e["lines"].append(dict(phase_code=r["phase_code"], description=r["description"],
                               cost_type=r["cost_type"], amount=r["amount"]))

    for pid, e in per_package.items():
        carried = log.get(pid, {}).get("carried_value")
        e["carried_value"] = carried
        e["cover_sheet_phase_code"] = (e["phase_codes"][0] if len(e["phase_codes"]) == 1
                                       else None)
        if carried is None:
            problems.append(f"{pid}: budget line exists but the package is not in the buy-out log")
            continue
        delta = e["budget_total"] - carried
        e["delta_vs_carried"] = round(delta, 2)
        # The budget is rounded to whole dollars, so anything inside $1 per
        # contributing line is rounding, not a discrepancy.
        if abs(delta) > len(e["lines"]):
            problems.append(
                f"{pid}: budget ${e['budget_total']:,.2f} vs carried ${carried:,.2f} "
                f"— delta ${delta:,.2f}")
        if len(e["phase_codes"]) > 1:
            problems.append(
                f"{pid}: {len(e['phase_codes'])} phase codes "
                f"({', '.join(e['phase_codes'])}) — the cover sheet allows one per "
                f"subcontractor")

    # ---- packages with no budget line at all -------------------------------
    for pid, p in log.items():
        if pid in per_package or not p["priority_rank"]:
            continue
        problems.append(f"{pid}: no budget line (carried ${p['carried_value']:,.2f})")

    totals = {}
    for r in rows:
        totals[r["category"]] = round(totals.get(r["category"], 0) + r["amount"], 2)

    out = dict(
        _generated="2026-08-08",
        _source=str(CSV_PATH.relative_to(ROOT)),
        _code_format="Cost-type suffix (-.O / -.L / -.S) and trailing hyphen stripped, "
                     "per PM direction: 31-2000-10000-.S is written 31-2000-10000",
        _totals_by_category=totals,
        _grand_total=round(sum(r["amount"] for r in rows), 2),
        _problems=problems,
        packages=dict(sorted(per_package.items())),
        lines=rows,
    )
    OUT.write_text(json.dumps(out, indent=1))

    print(f"wrote {OUT.relative_to(ROOT)} — {len(rows)} budget lines, "
          f"{len(per_package)} packages coded")
    print(f"\ngrand total  ${out['_grand_total']:,.2f}")
    for k, v in sorted(totals.items()):
        print(f"  {k:22} ${v:>14,.2f}")
    print(f"\n{len(problems)} item(s) to look at:")
    for p in problems:
        print("  •", p)
    return out


if __name__ == "__main__":
    build()
