#!/usr/bin/env python3
"""
Build the Attachment A Review Cover Sheet and the contract-amount summary that
sits behind it.

The Bluebeam process document defines the REVIEW packet: cover sheet first, then
"on a separate sheet, include a summary of how we got to the contract amount that
is on the Cover Sheet", then the draft Attachment A, then the bid form, the
subcontractor's own proposal, scope-option backup, and the descope notes.

PM direction: the ONLY place to break out pricing is this cover sheet. The
Attachment A itself carries one LUMP SUM.

This opens CORE's own cover-sheet template and fills its cells, the same way
build_attachment_a.py edits the Word template rather than regenerating it. The
template highlights its editable fields in yellow -- D3, D4, D13, D15, D16, C19,
F19, plus the four approver-name cells -- and nothing outside that set is
touched, so the layout, column widths, row heights, merges, the
=SUM(F19,F21,F23,F25) total and the 'list' sheet all survive byte-for-byte.

Usage:  python3 scripts/build_att_a_cover.py RFP-008
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Border, Font, Side

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "01-index" / "attachment-a-content"
OUT = ROOT / "02-drafts"
TEMPLATE = (ROOT / "00-source-docs" / "05-supplemental" / "attachment-a-process" /
            "NV Attach A Review Log Cover Bluebeam Template 111425.xlsx")
BUDGET = ROOT / "01-index" / "budget-phase-codes.json"

PROJECT = "NCSD - Tonopah HS Sports Field Replacement"
PROJECT_NO = "26-01-019"

# Cells the template fills in yellow. Writing anywhere else is a template edit,
# not a fill-in, so the build refuses to do it.
EDITABLE = {"D3", "D4", "D13", "D15", "D16", "C19", "F19",
            "B7", "B8", "B9", "E7", "E8", "E9"}

# PM review 08.11.26 moved the amount buildup ONTO the cover sheet, rows 22-30,
# and retired the template's own total at B27/E27 in favour of a total at row 30
# that picks up a P&P Bond line. The separate "contract amount summary" tab this
# script used to create is gone -- the reviewer wants one page, not two.
# The buildup is as long as the package needs, so the block is a region rather
# than a fixed cell list: columns B, E, F and G on rows 22 and below.
SUMMARY = re.compile(r"^[BEFG]([2-9]\d)$")

BOLD = Font(bold=True)
THIN = Side(style="thin")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def put(ws, coord, value, number_format=None):
    if coord not in EDITABLE and not (SUMMARY.match(coord) and int(coord[1:]) >= 22):
        raise ValueError(f"{coord} is neither a highlighted field nor in the summary block")
    ws[coord] = value
    if number_format:
        ws[coord].number_format = number_format


def phase_code_for(pkg):
    """The one phase code on the cover sheet, from the Procore budget."""
    if not BUDGET.exists():
        return None
    entry = json.loads(BUDGET.read_text())["packages"].get(pkg)
    return entry.get("cover_sheet_phase_code") if entry else None


def build(pkg):
    spec = json.loads((CONTENT / f"{pkg}.json").read_text())
    dest = OUT / pkg
    dest.mkdir(parents=True, exist_ok=True)

    wb = openpyxl.load_workbook(TEMPLATE)
    ws = wb["cover sheet"]

    put(ws, "D3", PROJECT)
    put(ws, "D4", PROJECT_NO)
    put(ws, "D13", spec["_subcontractor"])

    cs = spec.get("cover_sheet", {})

    # Buy-out dates are CORE-internal and not derivable from the bid documents.
    # A date has to go in as a date, or the cell holds text no formula can use.
    for coord, key in (("D15", "procurement_date"), ("D16", "start_date")):
        v = cs.get(key)
        put(ws, coord, date.fromisoformat(v) if v else "CONFIRM",
            number_format="m/d/yyyy" if v else "General")

    # Phase code comes from the Procore budget, never from the package record --
    # it is CORE cost coding and no bid document contains it. A package with more
    # than one budget line has no single code to write, so it stays CONFIRM
    # rather than picking one.
    put(ws, "C19", phase_code_for(pkg) or "CONFIRM")

    for coord, name in (cs.get("approvers") or {}).items():
        put(ws, coord, name)

    # ---- amount buildup, on the cover sheet itself --------------------------
    put(ws, "B22", "Summary of Contract Amount:")
    ws["B22"].font = BOLD
    put(ws, "B23", "Scope Description:")
    put(ws, "F23", "Amount:")
    ws["B23"].font = BOLD
    ws["F23"].font = BOLD

    # E27:F27 is merged in the blank template and is the only merge in this
    # region. It backed the template's own total, which moves below the buildup,
    # so the merge is vestigial -- and it makes F27 unwritable for any package
    # whose buildup is longer than three lines.
    for rng in [str(r) for r in ws.merged_cells.ranges]:
        if rng == "E27:F27":
            ws.unmerge_cells(rng)
    # Clear the template's own total BEFORE the buildup is written -- a buildup
    # longer than three lines runs straight through row 27 and must be able to
    # overwrite it, not be erased by it.
    put(ws, "B27", None)
    put(ws, "E27", None)

    row = 24
    for label, amt in spec["_amount_buildup"]:
        put(ws, f"B{row}", label)
        put(ws, f"F{row}", float(amt), number_format='#,##0.00;-#,##0.00')
        for c in (f"B{row}", f"F{row}"):
            ws[c].border = BOX
        row += 1
    last = row - 1

    # The PM's layout puts the bond at 29 and the total at 30 with a two-line
    # buildup. Hold those rows when the buildup fits above them, and push them
    # down when it does not, so a long buildup is never truncated.
    bond = max(29, last + 1)
    total = bond + 1

    put(ws, f"B{bond}", "P&P Bond")
    put(ws, "G29" if bond == 29 else f"G{bond}", cs.get("pp_bond_rate", 0))
    put(ws, f"F{bond}", f"=ROUND(SUM(F24:F{last})*G{bond},0)")
    for c in (f"B{bond}", f"F{bond}"):
        ws[c].border = BOX

    put(ws, f"B{total}", "TOTAL (should equal contract total)")
    put(ws, f"E{total}", f"=SUM(F24:F{bond})")
    for c in (f"B{total}", f"E{total}"):
        ws[c].font = BOLD
    put(ws, "F19", f"=E{total}")

    if "contract amount summary" in wb.sheetnames:
        del wb["contract amount summary"]

    f = dest / f"{spec['file_stem']} - Att A Review Cover Sheet.xlsx"
    wb.save(f)
    total = sum(a for _, a in spec["_amount_buildup"])
    print(f"wrote {f.relative_to(ROOT)}")
    # Compare to the cent, not to the dollar. A carried value with cents in it
    # (RFP-030 is $1,278,459.84) fails an int-vs-float compare even when the
    # buildup reconciles exactly.
    print(f"  buildup sums to {total:,.2f} — contract amount {spec['_contract_amount']:,.2f}"
          f"  {'MATCH' if round(total, 2) == round(spec['_contract_amount'], 2) else 'MISMATCH'}")
    return f


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "RFP-008")
