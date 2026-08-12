#!/usr/bin/env python3
"""
Build a package's Attachment A by editing CORE's Word template in place.

The process document is explicit: "Only modify items that are highlighted."  So
this does not regenerate the document from scratch -- it opens the template's
XML, replaces the text inside HIGHLIGHTED runs, and leaves every other run
untouched byte for byte.  The contract language, the numbering definitions, the
styles and the unhighlighted boilerplate come out identical to the template.

Where a section needs more (or fewer) bullets than the template provides, the
template's own paragraph is cloned as the prototype so the new bullets inherit
its numbering level and formatting rather than being invented.

Two things this deliberately does NOT do:
  - Put a price breakout anywhere in the Attachment A. PM direction: the only
    place to break out pricing is the Bluebeam cover sheet. The exhibit carries
    one LUMP SUM. (SCOPE OPTIONS carry their own dollar figure because the
    template provides that field for them -- that is an option price, not a
    breakout of the lump sum.)
  - Cite a specification section absent from the Project Manual. PM ruling
    08.06.26 (D): the obligation goes in by TITLE instead.

One thing it does ONLY on a draft, never on an issued exhibit:
  - Append the RULE 14 REVIEW appendix. PM request 08.11.26: rule 14 strips every
    obligation the specs and drawings already carry, and he wants to see what was
    stripped, next to the scope, so he can put any of it back. The appendix is a
    review aid on the draft. It starts on its own page, is titled DRAFT REVIEW
    ONLY - DELETE BEFORE ISSUE, and `--final` refuses to write it at all.

Usage:  python3 scripts/build_attachment_a.py RFP-008
        python3 scripts/build_attachment_a.py RFP-008 --final   # no review appendix
Writes: 02-drafts/<package_id>/<Subcontractor> Draft Att A.docx
"""

import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = (ROOT / "00-source-docs" / "05-supplemental" / "attachment-a-process" /
            "2601019 NV 002 Attach A Subcontract DS Template 050925.docx")
CONTENT = ROOT / "01-index" / "attachment-a-content"
OUT = ROOT / "02-drafts"

P_RE = re.compile(r'<w:p(?: [^>]*)?>(?:(?!</w:p>).)*?</w:p>', re.S)
R_RE = re.compile(r'<w:r(?: [^>]*)?>(?:(?!</w:r>).)*?</w:r>', re.S)
T_RE = re.compile(r'(<w:t(?: [^>]*)?>)(.*?)(</w:t>)', re.S)


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def para_text(p):
    return "".join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', p, re.S))


def is_highlighted(run):
    return "<w:highlight" in run


def set_para_text(p, new):
    """Put `new` into the paragraph's highlighted runs, leaving the rest alone.

    `new` may be a string (all text into the first highlighted run, any further
    highlighted runs emptied) or a list of strings, one per highlighted run --
    which is what the address block needs, since "Address" and "City, ST, Zip"
    are two highlighted runs separated by a line break in one paragraph.

    Unhighlighted runs are never touched. That is what keeps "Phone:",
    "Contact Person:" and every contract sentence exactly as the template has
    them, which is the rule the process document states.
    """
    runs = list(R_RE.finditer(p))
    hi = [m for m in runs if is_highlighted(m.group(0))]
    if not hi:
        return p
    vals = list(new) if isinstance(new, (list, tuple)) else [new]

    def fill(run, text):
        seen = [0]

        def sub(mm):
            seen[0] += 1
            if seen[0] == 1:
                return f'<w:t xml:space="preserve">{esc(text)}</w:t>'
            return f"{mm.group(1)}{mm.group(3)}"       # blank the extras
        return T_RE.sub(sub, run)

    out, last, n = [], 0, 0
    for m in runs:
        out.append(p[last:m.start()])
        r = m.group(0)
        # A highlighted run with no <w:t> carries no text -- in the address
        # paragraph it is the line break between "Address" and "City, ST, Zip".
        # Counting it would shift every following value by one and blank the
        # last real run, which silently dropped the city line.
        if is_highlighted(r) and T_RE.search(r):
            r = fill(r, vals[n] if n < len(vals) else "")
            n += 1
        out.append(r)
        last = m.end()
    out.append(p[last:])
    return "".join(out)


def plain_header(p):
    """Drop the template's instruction styling (bold, red) from a prototype."""
    p = re.sub(r"<w:b/>|<w:bCs/>", "", p)
    return re.sub(r'<w:color w:val="FF0000"\s*/>', '<w:color w:val="000000"/>', p)


def left_align(p):
    """Justified -> left. PM review 08.11.26 on the address block."""
    return p.replace('<w:jc w:val="both"/>', '<w:jc w:val="left"/>')


def clone(prototype, texts):
    """One paragraph per string, each a copy of the prototype's formatting."""
    return "".join(set_para_text(prototype, t) for t in texts)


# --------------------------------------------------------------------------
# RULE 14 REVIEW appendix.
#
# Written from scratch rather than cloned. Every body paragraph in the template
# is a numbered ListParagraph, so cloning one would fold the appendix into the
# exhibit's own A./B./C. numbering and make it read as scope. It must not read
# as scope: it is a list of obligations deliberately LEFT OUT, and if it ever
# reaches a subcontractor unlabelled it says the opposite of what it means.
# --------------------------------------------------------------------------
FONT = ('<w:rFonts w:ascii="Segoe UI" w:hAnsi="Segoe UI" w:cs="Segoe UI"/>'
        '<w:sz w:val="20"/><w:szCs w:val="20"/>')
RED = "C00000"


def para(text, bold=False, color=None, indent=0, before=0, size=None):
    rpr = FONT
    if size:
        rpr = rpr.replace('w:val="20"', f'w:val="{size}"')
    if bold:
        rpr += "<w:b/><w:bCs/>"
    if color:
        rpr += f'<w:color w:val="{color}"/>'
    ppr = (f'<w:pPr><w:spacing w:before="{before}" w:after="40"/>'
           f'<w:ind w:left="{indent}"/><w:jc w:val="left"/>'
           f"<w:rPr>{rpr}</w:rPr></w:pPr>")
    run = f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{esc(text)}</w:t></w:r>'
    return f"<w:p>{ppr}{run}</w:p>"


def review_appendix(spec):
    """The struck-item list, as its own page at the end of the draft."""
    ap = spec.get("review_appendix") or {}
    groups = ap.get("groups") or []
    if not groups:
        return "", 0

    out = ['<w:p><w:r><w:br w:type="page"/></w:r></w:p>']
    out.append(para("DRAFT REVIEW ONLY - DELETE BEFORE ISSUE", bold=True,
                    color=RED, size=24))
    out.append(para("This page is not part of the Subcontract and is not Scope of Work.",
                    bold=True, color=RED))
    out.append(para("RULE 14 REVIEW - obligations removed from the Scope of Work above",
                    bold=True, before=240))
    for line in ap.get("intro", []):
        out.append(para(line, before=60))

    n = 0
    for g in groups:
        out.append(para(g["header"], bold=True, before=200))
        for line in g.get("note", []):
            out.append(para(line, indent=180))
        label = g.get("source_label", "already stated in")
        for it in g["items"]:
            n += 1
            out.append(para(f"☐  {it['item']}", indent=360, before=60))
            out.append(para(f"{label}: {it['source']}", indent=720))
            if it.get("flag"):
                out.append(para(it["flag"], indent=720, bold=True, color=RED))
    return "".join(out), n


def build(pkg, final=False):
    spec = json.loads((CONTENT / f"{pkg}.json").read_text())

    with zipfile.ZipFile(TEMPLATE) as z:
        parts = {n: z.read(n) for n in z.namelist()}
    xml = parts["word/document.xml"].decode("utf-8")

    paras = [m.group(0) for m in P_RE.finditer(xml)]
    idx = {i: p for i, p in enumerate(paras)}

    # Prototypes cloned for repeated content, taken from the template itself so
    # cloned bullets inherit real numbering levels rather than invented ones.
    # Template paragraph 29 is the "<Begin your Scope of Work Here>" example, and
    # it is styled as an instruction to the drafter: bold, red. Cloning it carried
    # that styling onto every real group header. PM review 08.11.26: "This should
    # not be bold. Change text to Black." Strip it from the prototype, once.
    proto_group = plain_header(idx[29])   # ilvl=1 -- "A./B./C." scope group header
    proto_bullet = idx[30]     # ilvl=2 -- "i./ii./iii." bullet
    proto_section = idx[63]    # spec section line
    proto_directive = idx[82]  # Addendum/Clarification/RFI line
    proto_option = idx[51]     # SCOPE OPTIONS line with its own $ field
    proto_excl = idx[107]      # exclusion line

    repl = {}                                  # paragraph index -> new XML
    for i, t in spec["simple"].items():
        repl[int(i)] = set_para_text(idx[int(i)], t)
    # The address block is a two-line block, not prose; justifying it stretches
    # the street line across the column.
    if 9 in repl:
        repl[9] = left_align(repl[9])

    # --- SCOPE OF WORK body: template paragraphs 29-43 ---------------------
    body = []
    for grp in spec["scope_groups"]:
        body.append(set_para_text(proto_group, grp["header"]))
        body.append(clone(proto_bullet, grp["items"]))
    repl[29] = "".join(body)
    for i in range(30, 44):
        repl[i] = ""                           # consumed by the block above

    # --- SCOPE OPTIONS ------------------------------------------------------
    if spec["scope_options"]:
        # Two highlighted runs on this line: the scope text, then the amount that
        # follows the template's own "for a total amount of $".
        opts = [set_para_text(proto_option, [o["scope"], o["amount"]])
                for o in spec["scope_options"]]
        repl[49] = ""                          # drop the "None." line
        repl[51] = "".join(opts)
    else:
        repl[51] = ""

    # --- CONSTRUCTION DOCUMENTS: spec sections ------------------------------
    repl[62] = ""                              # "None"
    repl[63] = clone(proto_section, spec["spec_sections"])
    repl[64] = ""

    # --- Directives ---------------------------------------------------------
    repl[78] = ""                              # "None."
    repl[80] = ""                              # BIM line (no BIM on this job)
    repl[82] = clone(proto_directive, spec["directives"])
    for i in (84, 86, 88, 90):
        repl[i] = ""

    # --- EXCLUSIONS ---------------------------------------------------------
    repl[107] = clone(proto_excl, spec["exclusions"])
    repl[108] = ""

    # Optional standard clauses the template highlights so they can be kept or cut
    for i, keep in spec["standard_clauses"].items():
        if not keep:
            repl[int(i)] = ""

    # --- reassemble ---------------------------------------------------------
    out, last = [], 0
    for i, m in enumerate(P_RE.finditer(xml)):
        out.append(xml[last:m.start()])
        out.append(repl.get(i, m.group(0)))
        last = m.end()
    out.append(xml[last:])
    new_xml = "".join(out)

    # --- RULE 14 REVIEW appendix, drafts only -------------------------------
    n_review = 0
    if not final:
        block, n_review = review_appendix(spec)
        if block:
            new_xml = new_xml.replace("<w:sectPr", block + "<w:sectPr", 1)

    dest = OUT / pkg
    dest.mkdir(parents=True, exist_ok=True)
    f = dest / f"{spec['file_stem']} Draft Att A.docx"
    with zipfile.ZipFile(f, "w", zipfile.ZIP_DEFLATED) as z:
        for n, data in parts.items():
            z.writestr(n, new_xml.encode("utf-8") if n == "word/document.xml" else data)

    print(f"wrote {f.relative_to(ROOT)}")
    n_items = sum(len(g["items"]) for g in spec["scope_groups"])
    print(f"  scope groups {len(spec['scope_groups'])}, items {n_items}, "
          f"sections {len(spec['spec_sections'])}, "
          f"directives {len(spec['directives'])}, exclusions {len(spec['exclusions'])}")
    if n_review:
        print(f"  ** RULE 14 REVIEW appendix: {n_review} struck items on a trailing page.")
        print(f"  ** This is a DRAFT. Rebuild with --final before the exhibit is issued.")
    elif final and (spec.get("review_appendix") or {}).get("groups"):
        print("  final build — review appendix suppressed")
    return f


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    build(args[0] if args else "RFP-008", final="--final" in sys.argv)
