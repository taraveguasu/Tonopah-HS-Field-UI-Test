# ITB-008 — notes for the Attachment A review

Prewitt Land Surveying · Contract amount **$80,767.50** · Procore `02-1010-10000`

First sub that has to be under contract in Tier 2 — control has to be set before the
first field activity, so mobilization on 11/24/26 is the need date. These are the
judgment calls; none appear in the exhibit.

---

## 0. The package record said "not yet awarded." It is wrong.

`01-index/packages/ITB-008.json` carries a bare `{"status": "not-yet-awarded"}`,
generated 07.10.26, **predating the GMP**. The BackSheet carries line **#7 "Horizontal
Survey & Staking — Prewitt Land Surveying $80,768."**

Same stale-record pattern as ITB-072, RFP-094, RFP-109 — and ITB-089 in this same
batch. This exhibit is drafted against Prewitt. **The record needs updating** so the
next session does not re-draft it as unawarded.

## 1. The carried value is Prewitt's price plus exactly 10%

| | |
|---|---:|
| Prewitt proposal 05.11.26, priced tasks | 73,425.00 |
| Unexplained variance — **exactly 10.0%** | 7,342.50 |
| **Carried** | **80,767.50** |

$73,425 × 1.10 = $80,767.50, to the cent. That is too clean to be a coincidence and
too undocumented to rely on — **there is no descope, homework response or leveling
tab on file that explains it.** It reads like a markup or contingency applied during
GMP assembly rather than a negotiated scope change.

Worth knowing which, because if it is a GMP-level markup then the subcontract should
probably issue at $73,425 and the 10% stays with CORE. **Resolve before issue.** The
variance is written onto the cover sheet as its own line.

## 2. This exhibit IS the specification for this trade

**ITB-008 holds no CSI spec section at all** — confirmed against the split manual.
Requirements come from the Scope of Work narrative and Division 01, nothing else. So
unlike every other package in this batch, there is no spec behind the exhibit to fall
back on: what is written here is the whole obligation.

Worth a conscious confirmation that this is acceptable before issuing, rather than
discovering it at a dispute.

Related: **nothing in the Basis of GMP addresses surveying at all** — no scope
assumption, no exclusion. Nothing to reconcile against.

## 3. Three Prewitt exclusions contradict the narrative — none adopted

| Prewitt excludes | Against |
|---|---|
| Exhibit A item 11 — *"As-Built Survey and Drawing Requirements"* | narrative Survey items f, g, h (offsite elevation verification, record as-built utility survey, Project Monument Survey) |
| Exhibit A item 6 — *"staking for landscaping, hardscape and irrigation"* | narrative Utility Staking item c.ii, *"Irrigation water mains and RPPA"* |
| Exhibit A item 3 — no staking for *"Landscape, Structural, Architectural or Mechanical"* portions | **his own priced tasks** |

The third one is self-contradicting and was read as boilerplate rather than a carve-out:
Prewitt's own **priced** Final Staking and Building Corner/Grid Line Staking tasks
explicitly cover bleacher ADA, sport features, scoreboards, flagpole, goal posts,
press box, and building corners and grid lines. He priced the very work item 3
disclaims.

The first two are real disagreements and stay flagged. **The as-built exclusion is
the one that matters** — as-builts are a closeout deliverable and their absence
surfaces at the worst possible time.

## 4. His own pricing found scope the narrative missed

Going the other way: Prewitt's priced **Final Staking** task lists **high jump** and
**track text, striping and logo layout**, which the narrative's own list omits. Those
are in the exhibit. This is reconciliation working in CORE's favor — the awarded sub
priced more than the narrative asked for, and the subcontract should capture it.

## 5. "as required for City of Las Vegas"

Narrative Survey item h requires a Project Monument Survey *"as required for City of
Las Vegas."* **This project is in Nye County.** Leftover boilerplate from another
project's template — Rosevear's proposal silently corrected it to "NCSD."

Drafted as **"as required by the Owner"** so the wrong jurisdiction is not carried
into an executed subcontract. **The narrative should be corrected at source**; it is
a live document and this is not the only package reading from that template.

## 6. Commercial terms that are trade practice but appear in no contract document

Prewitt's Exhibit A items 12–14: entire site assumed available when scheduled with
additional mobilizations "to be discussed"; two-business-day minimum notice to
schedule field crews; **re-staking after vandalism or damage billed as additional
work**, two-hour minimum, at their prevailing wage fee schedule.

All ordinary surveying practice. None of it is in the Contract Documents, and none of
it is adopted here. **The one worth a decision is re-staking** — on a site this
exposed, whether re-staking after damage to Contractor-protected stakes is base scope
or a T&M add is a real number over the life of the job.

## 7. Who signs, and where do we email them

**No email address appears anywhere in Prewitt's proposal** — not the letter, not
Exhibit A. `simple.12` is left TBD.

The signatory is **Thomas L. Prewitt, P.L.S., W.R.S., Owner**, but a later addendum on
the same document (covering field light poles and the ticket booth pad) is initialed
by **Janet Prewitt, 05/20/2026**. Confirm which individual is the Attachment A contact
before issue.

## 8. Rosevear

Rosevear's proposal restates the narrative almost verbatim. Read for diagnostic
comparison only; not the reconciliation basis now that Prewitt is confirmed.

---

## Rule 14 review page

**1 struck item** on the trailing page — the smallest in the batch, which follows from
§2: with no spec section behind this package, there is almost nothing that another
document already carries. Build with `--final` to drop it.

Voice check passes with 2 warnings, both `CAD` (as in the Civil Engineer's CAD
background file) — a term of art, left as written.
