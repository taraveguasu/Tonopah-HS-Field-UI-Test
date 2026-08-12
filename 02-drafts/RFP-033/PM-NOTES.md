# RFP-033 — notes for the Attachment A review

Corona Steel, Inc. · Contract amount **$166,281.00** · GMP R2 BackSheet, Procore `05-1000-10000`

These are the judgment calls and the open commercial gaps. None of them appear in
the exhibit — an Attachment A is not the place to record a question.

The exhibit is drafted to the Contract Documents, not to Corona's proposal. Where
the two differ, the difference is written up below rather than quietly resolved in
either direction.

---

## 0. The amount reconciles, and it is not the number in the package record

`01-index/packages/RFP-033.json` carries Corona's base proposal at **$145,468**.
That is not the carried value. The GMP BackSheet and the Procore budget both carry
**$166,281**, and it reconciles to the dollar against four dated homework adds:

| | |
|---|---:|
| Base proposal 05.12.26 | 145,468 |
| New canopy posts | 7,832 |
| Bollards | 1,960 |
| Roof-deck opening bracing | 2,237 |
| Remobilization | 8,784 |
| **Carried** | **166,281** |

The exhibit is drafted to $166,281. **The package record should be corrected** —
left alone it will keep propagating the base-bid number into anything downstream
that reads it.

---

## 1. Countertop supports are required by the narrative and appear in no priced line

Scope of Work #033 requires countertop supports. They are in none of the four
homework adds above, and Corona's base proposal separately excludes
*"Miscellaneous and Ornamental Metals"* outright (Standard General Exclusion #4,
cover letter item 3.f).

The exhibit carries the requirement, because the narrative is the trade-boundary
authority and a proposal does not narrow the subcontract. **But it is very likely
unpriced.** Confirm before issue.

## 2. Joist reinforcement for MEP loads at the concessions roof is unresolved

Corona's scope-review correspondence states that no load beyond the 366TL/251LL
shown on S2-10 was called out, and asks whether FCU, duct and piping loads are
covered by the 43.7 PSF snow / 17.3 PSF dead load already used to size the joists.
**The EOR has not answered.**

No price is carried for this and the exhibit does not assert it as an inclusion —
claiming it without an engineering answer would be inventing scope. This needs to
go back to the EOR, and it needs to happen before the joist submittal, not after:
the joist and deck chain is the longest on the job at 170 working days and a
re-design lands on the critical path.

## 3. The canopy alternate changed shape between the proposal and the carried price

Alternate 033.01 (canopy at the abandoned Elementary School campus) was originally
proposed at **$53,519** to reinstall *salvaged* HSS posts with new channels, plates
and anchor bolts per AD1.15 details 4 and 4A. What is carried is a **$7,832**
homework add priced for *"new 3-inch post columns."*

Those are different scopes at a seventh of the price. Confirm the alternate is now
new-post supply rather than salvage reinstallation, and confirm whether $7,832
includes installation labor or is supply only.

## 4. Three narrative obligations Corona excluded in writing

Corona's base proposal excludes all three, and none of the later homework responses
walk any of them back:

| Obligation | Corona's basis |
|---|---|
| Steel erection layout | Standard General Exclusion #2 |
| Hoisting, shoring, lift plan | Standard General Exclusion #3 |
| Third-party inspection costs | Standard General Exclusion #8 |

The exhibit carries all three per the narrative. On inspection specifically, check
this against the RFP-031 precedent — **Section 01 4000 ¶1.04.A puts the independent
testing agency on the District's account**, which is how the masonry exhibit was
resolved (cooperation obligations in, cost of the agency out). The same reading may
apply here.

## 5. Forklift

Corona's scope-review agenda records *"Assume CORE to provide forklift"* for
offloading. The narrative places all offloading and hoisting equipment with the
Subcontractor and says nothing about a CORE forklift. Unpriced either way until
someone decides. Confirm who furnishes it.

## 6. AESS

Section 05 12 23 ¶1.01.A.6 brings Architecturally Exposed Structural Steel into the
section's scope, and both Corona and Adams & Smith reserved the right to exclude it
unless specifically shown. **No AESS was identified on any sheet reviewed** —
S0-00 through S4-01, A1-20, A9-20, A10-30. Confirm none is designated, so the
question is closed rather than latent.

## 7. CMU wall beam bearing plates — settled, and it has to stay settled

Scope of Work #033 claims the plates in line 4 (*"supply and install"*) and
disclaims them two lines later (line 6, *"supply only, F.O.B. jobsite … masonry wall
embeds"*). Scope of Work #031 and S4-01 both put installation with the mason, and
the RFP-031 exhibit was drafted that way.

**This exhibit follows the same boundary: supply only.** The two exhibits now agree.
Nothing to decide unless you want to move it — in which case both have to move.

---

## Sole-source and commercial

- Corona is one of two bidders (Adams & Smith the other). Adams & Smith's 25
  exclusions were read in full and are the reason several items above are written
  explicitly rather than left to "complete scope."
- The **anchor bolts are needed 2/15/27**, two and a half months before the 5/3/27
  erection, and they are embedded in RFP-030's concrete. Buying this package
  against the erection date misses them.
- **Goal post structural design** is listed as a deferred submittal on G0-00 and is
  assigned to no package. Not this exhibit's problem to solve, but it is still
  homeless.

---

## Rule 14 review page

The DRAFT carries a trailing `RULE 14 REVIEW` page — **18 struck items** with a tick
box each and the document that already carries them, grouped A (already in the
Manual or on the drawings), B (only in a Scope of Work narrative — the decision
group), C (in no document at all).

Group B is the one to read. Items 1–2 there are the layout and hoisting obligations
from section 4 above: if the Scope of Work narrative is not an exhibit to the
executed Subcontract, striking them deletes the obligation rather than relocating it.

Build with `--final` to drop the page. Stage 7 exhibits must be built that way.
