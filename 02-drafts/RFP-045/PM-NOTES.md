# RFP-045 — notes for the Attachment A review

Foursquare Roofs & Walls, Inc. · Contract amount **$142,585.00** · Procore `07-4100-10000`

These are the judgment calls and the open commercial gaps. None of them appear in
the exhibit — an Attachment A is not the place to record a question.

---

## 0. The amount is $142,585, and there is a stainless steel counter inside it

`01-index/packages/RFP-045.json` states Foursquare's price as **$135,698**. That is
the roofing line only. The GMP R2 line 45 and the Procore budget both carry
**$142,585**, which is the exact sum of Foursquare's two 05.05.26 proposal lines:

| | |
|---|---:|
| Standing seam roof system, underlayment, fascia, gutters, downspouts, trim, flashing | 135,698 |
| Fabricate and install stainless steel pass-through counter, window header and jambs (3/A7-10) | 6,887 |
| **Carried** | **142,585** |

So the roofing package owns a **stainless steel concessions pass-through counter**.
That is not obvious from the package title and it is easy to lose. It is drafted as
its own scope group so it cannot be missed at descope. **The package record should
be corrected** to the carried value.

---

## 1. Berridge vs. RFI #23 — decided, but two contract documents still disagree

Your 08.06.26 B1 ruling puts the GMP over RFI #23: the system is **Berridge
Cee-Lock**. The exhibit is drafted that way, and the drawings support it — A4-20
carries Berridge Tee-Panel, Cee-Lock, fascia and wall panel details even in the base
bid, and Foursquare's own scope review recorded a *"berrage z lock standing seam
roof"* assumption.

The problem is that **Clarification No. 1 says the opposite in writing, to every
bidder**: *"Metal roofing specifications take precedence"* over the drawn Berridge
callout. Both are contract documents. The ruling resolves which one CORE buys; it
does not erase the other from the record.

This is the item the release-priority log calls blocking, and it is right to.
Settle it before release or the sub orders the wrong panel and a **100-day
procurement starts over**. Expect it to resurface at shop drawing review.

## 2. Sole bidder, late, unsigned — on a 1% package

Foursquare is the only bidder CORE carried an award on. Their only proposal on file
is flagged **"LATE - not submitted to BuildingConnected"** and carries **no signed
Subcontractor Proposal (Bid) Form**.

This is an NRS 338.16995 1% list package. That combination — sole bidder, out of
process, unsigned — is worth confirming a properly submitted proposal or Bid Form
exists somewhere before relying on this record. Same missing-Form pattern as
RFP-031.

## 3. Pricing expired 06.04.26

The 05.05.26 proposal states 30-day validity. Nothing has issued. Confirm current
pricing.

## 4. Which entity is signing

The proposal letterhead reads **"Foursquare Roofs & Walls Inc."** The GMP's 1%
Subcontractor Listing (05.27.26) reads **"Foursquare Roof and Walls."** Confirm the
legal entity before the subcontract issues. The exhibit uses the letterhead form.

## 5. Contact and bond

- **No email on file for LaMar Noorda**, who signed the proposal and is named as
  Foursquare's PM on the scope-review agenda. The only Foursquare email in the
  project record is Gerrit Noorda's (`Gerrit@foursquarenv.com`), used as the best
  available. Confirm.
- **No bond rate on file.** The only other bidder, Canyon State, is recorded at 0%,
  which the leveling notes themselves flag as a likely BuildingConnected parse
  artifact rather than a real bond-free quote. Confirm Foursquare's actual rate.

## 6. The same dollar figures appear on ITB-072 — do not buy them twice

Foursquare's 05.19.26 homework response also priced **exterior building letters**
($6,780 flat metal / $12,892 channel) and the **outdoor bulletin cabinet** ($1,480),
at keynotes 6-04 and 6-01/A5-10. Those are the same figures already open on ITB-072
Building Signage, carried to YESCO.

Neither is inside the $142,585 — the amount reconciliation in section 0 proves it.
The exhibit excludes them **without routing them** (rule 12), so this exhibit makes
no representation about what YESCO's subcontract contains. Flagged so the same
numbers are not read into two packages.

## 7. FM Global

The Scope of Work narrative requires *"compliance with requirements of FM Global."*
**No other document on this package references an FM Global rating** for any
material or assembly. It is in the rule 14 review page rather than the exhibit,
pending confirmation that it actually applies. If it does, it is a real cost — FM
approval drives fastening patterns and can change the panel.

## 8. Boundary with ITB-040 is already set

Per your 07.31.26 ruling, the self-adhered membrane under the metal roof is RFP-045
and ITB-040 is below-grade only; they share 07 25 00. The exhibit follows that. No
action, noted so it is not relitigated at descope.

---

## Rule 14 review page

The DRAFT carries a trailing `RULE 14 REVIEW` page — **18 struck items**, grouped
A (already in the Manual or on the drawings), B (only in a Scope of Work narrative —
the decision group), C (in no document at all; here, scaffolding, which is trade
means).

Build with `--final` to drop the page. Stage 7 exhibits must be built that way.
