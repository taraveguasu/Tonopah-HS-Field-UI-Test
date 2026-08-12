# RFP-031 — notes for the Attachment A review

Henderson Masonry, LLC · Contract amount **$189,449.00** · GMP R2 BackSheet row 56

These are the judgment calls and the open commercial gaps. None of them appear in
the exhibit — an Attachment A is not the place to record a question.

The exhibit is drafted to the Contract Documents, not to Henderson's proposal.
Where the two differ, the difference is written up below rather than quietly
resolved in either direction.

---

## 0. Rewritten against your 08.11.26 markup rules — 55 scope items down to 13

This package was first drafted before your ITB-072 markup landed. It has been
rewritten to rule 14: **42 scope items were struck as duplicates of the specs,
the drawings, Division 01, or the Subcontract's own terms.** Everything struck
was true and correctly sourced — that is the point of the rule, not an objection
to it. What is left is the trade boundary and the one obligation the documents
fail to carry.

**The strike list is now in the exhibit itself**, per your 08.11.26 request — a
trailing page titled `DRAFT REVIEW ONLY - DELETE BEFORE ISSUE`, 39 items with a
tick box each and the document that already carries them. Build with
`--final` to drop the page; Stage 7 exhibits must be built that way.

The page groups them by where the obligation actually lives, because that is the
question you are answering:

| | | |
|---|---:|---|
| **A** Already in the Project Manual or on the drawings | 24 | Safe to leave out |
| **B** Only in a Scope of Work narrative | 14 | **The decision group** |
| **C** In no document at all | 1 | Scaffolding. Trade means |

**Group B is the one to read.** If the Scope of Work narrative is not an exhibit
to the executed Subcontract, striking those 14 deletes the obligation rather than
relocating it — and five of them are items Henderson has already excluded in
writing (bucks, testing ×3, barricades). That is the same list as section 3
below, arrived at from the opposite direction.

The summary table below is the short version:

| Struck | Lives in |
|---|---|
| CMU standards, medium weight, 2,800 psi units, f'm 2,000 psi, mortar and grout mixes | 04 2016 ¶2.02, S0-00 |
| Fully grouted walls and stem walls | S0-00 note 8, "grout cells solid in all walls" |
| Control joints at 30'-0" and not within 4'-0" of an opening | S4-00 detail 5, 04 2016 ¶3.10 |
| Tooling joints to match existing, 50 units of extra stock | 04 2016 ¶3.03.E, ¶1.12.B |
| 8' x 8' mock-up, samples, shop drawings, product data, prism testing | 04 2016 ¶1.08, ¶1.04, Division 01 |
| Temporary shoring and bracing, weather protection and curing | 04 2016 ¶3.02.B, ¶1.10 |
| Cleanup, dust control, wet saw, wash-out containment, hoisting, scaffolding, foreman, mobilizations | Division 01, the Subcontract terms, and PROJECT SPECIFIC PROVISIONS below |

**The one item kept on rule 14's second half is the integral water repellent.**
It survives for exactly the reason your exterior-signage line survived on
ITB-072: it is not in the specification. Section 04 2016 cross-references
07 19 00 Water Repellents twice and that section does not exist in the manual,
so the Scope of Work narrative is the only place the obligation is written down.
See section 2.

Three consequences worth knowing:

- **Exclusions went 18 → 5** under rule 16. The five kept are the ones a mason
  would ordinarily assume are his. Everything a mason would never claim —
  demolition, structural steel, gypsum and furring, coiling doors, sheet metal
  flashing, masonry veneer, site masonry, temporary power — is gone.
- **Exhibit B is no longer referenced anywhere**, per rule 14a. I read it for
  real exclusions. Its only masonry content is the testing and special-inspection
  exclusion, which is now written as its own clause, and a clarification that
  normal shrinkage cracking of fully grouted CMU walls is expected — an
  Owner-facing acceptance term, not something to push onto the sub.
- **Paragraphs 27 and 28 are both kept** per rule 17. My first pass cut 28 as
  disproportionate on a 12-day package; your rule says they stay in all
  Attachment A's.

---

## 1. The carried price is on the wrong block, and CORE already knows the number

This is the one that costs money.

| Source | What it says |
|---|---|
| Section 04 2016 ¶2.02.A | CMU shall be ASTM C90, Grade N, Type II/V cement, Type I moisture controlled, **medium weight**, 2000 psi minimum |
| S0-00 general notes | Concrete masonry units **ASTM C90, MEDIUM WEIGHT**; individual units **2800 psi** |
| Henderson, 06.01.26 | *"Original block was standard normal weight block"* |
| Dawn's request, 05.29.26 | *"Precision CMU ILO specified CMU"* — Henderson answered **+$4,516.00** |
| Leveling tab `31` row 31 | `Descope ALT · Precision CMU ILO Standard CMU · + · *4516` — asterisked, **not carried** |

So CORE spotted the deviation during descope, priced it, and then did not carry
it. Base price, base-plus-accepted-alternates and base-plus-all-alternates on tab
`31` are all $189,449.

Two things are unresolved inside that $4,516, and they should not be conflated:

- **Weight.** Medium weight is specified in two places. Henderson bid normal
  weight. That is a straight deviation from the Contract Documents.
- **Texture.** Nothing in the set specifies a CMU texture at all — Section 04 2016
  ¶2.02 is silent, and A10-10's finish legend has **no Division 04 entry**. All CMU
  is painted (PT-1 inside, EPT-2 outside), so texture is a paint-substrate question,
  not an appearance one.

**Watch the name collision.** Project **Alternate #9 on the same tab, "Precision
CMU ILO Painted CMU," is marked Not Accepted** — that was the Owner declining to
leave block exposed. It is a different question from Henderson's $4,516, which is
a product change underneath paint either way.

**The exhibit requires medium weight CMU per the specification.** Under the GMP's
own reasonable-inference clause, which Henderson's proposal does not except, the
specified unit is arguably already bought. But he has stated in writing that it
is an add, so this will be argued at execution unless you settle it first.

Three options, in the order I would take them:

1. Hold him to medium weight at $189,449 as reasonably inferable, and confirm it
   in writing before the subcontract issues.
2. Accept the $4,516, raise the contract to $193,965, and add it to the buildup on
   the cover sheet. (That is the figure the GMP R2 workbook itself already carries
   at `Bid Tally` row 483 — $193,965 sits in its all-alternates column while the
   BackSheet and leveling tab both show $189,449.)
3. Pull one competitor's price on medium weight precision block as a check. XL
   Concrete Masonry's masonry-only line was **$267,417** and Kemper's **$355,230**,
   both with integral water repellent included, so $189,449 + $4,516 is still far
   below the field.

---

## 2. Integral water repellent: required by the narrative, priced out by the sub

Scope of Work #031 line 3 is unambiguous:

> *"Provide integral silicone water repellent/sealer for all block, mortar, and
> grout exposed above grade."*

Henderson's proposal marks **Waterproofing — EXCLUDED** and **Sealing/Antigrafitti
— EXCLUDED**, and the 05.21.26 scope review agenda records *"Did not assume any
waterproofing."*

Both competitors who addressed it priced it in:

- **John Jackson:** *"CMU is 2,000 psi; Medium Weight; Natural Gray Color;
  Precision Texture; IWR"*
- **XL Concrete Masonry:** *"Integral Water Repellants in CMU and Mortar"*

That is the clearest available signal that the item is real, cheap and routinely
carried — which is exactly why the exhibit includes it and excludes only
*surface applied waterproofing and dampproofing* and *anti-graffiti coatings*
alongside it. Integral repellent is an admixture in the units and the mortar; the
two are different work and Henderson's exclusion reads as though it covers both.

**Say this one out loud at the scope review.** It is a small number that becomes a
change order the day the block is ordered without it.

One documentation note behind it: Section 04 2016 cross-references **Section 07 19
00 Water Repellents twice**, and 07 19 00 **is not in the Project Manual**. Per
your global ruling D (08.06.26) it is not cited in the exhibit; the obligation is
drafted from the scope narrative instead.

---

## 3. Henderson's proposal excludes 27 of 29 line items. The descope fixed two.

The included/excluded table on proposal #26-65 marks **only Shop Drawings and
Reinforcement (CMU only) as INCLUDED**. Everything else on that table is in the
EXCLUDED column at $0.00. I read the column positions off the PDF geometry rather
than the text layer, because the extraction flattens the two columns into one — the
X marks sit at x=183.0 and x=409.8, which are the exact centers of the two EXCLUDED
headers.

The 05.21.26 scope review closed two of them, and the leveling sheet confirms:

| Item | Proposal | Descope / leveling | Status |
|---|---|---|---|
| Embeds | Excluded | *"Includes setting any provided embeds"* | **Closed** |
| Setting door frames | Excluded | Tab `31` row 27 `Install HM in CMU Openings` = √ | **Closed** |

These are still open, and all four are express obligations of Scope of Work #031:

| Excluded by Henderson | Scope of Work #031 requires |
|---|---|
| **Testing** | Mortar and grout test samples; preconstruction prism testing as a separate grout pour; a qualified representative onsite; scheduling testing and walking inspectors to sign-off |
| **Dry Pack** | *"Grout and/or drypack under all bearing plates in masonry construction as indicated"* — and S4-01 details drypack or grout below every joist bearing plate |
| **Window/Door Bucks** | *"Provide layout for formwork/rough bucks for all wall openings"* |
| **Barricades** | *"Provide dust control, street cleaning, barricades, and flagging … per Nye County Air Quality requirements"* |

Two more are worth a sentence each rather than a fight:

- **Flashing.** Excluded by Henderson, but #031 line 6 has him installing
  *"flashings"* among the embeds provided by others. The exhibit includes
  installation of masonry flashings and excludes sheet metal cap flashing and
  counterflashing over masonry, which is 07 62 00 and sits with RFP-045.
- **Beam Dovetail Slots.** Excluded, and harmlessly so — dovetail slots are veneer
  anchorage and BackSheet #048 Masonry Veneer is carried at $0, N/A. There is no
  veneer on this job.

**On testing specifically, he is closer to right than the narrative is.** Section
01 4000 ¶1.04.A: *"Nye County School District will employ and pay for services of
an independent testing agency to perform specified testing and inspection."* So
the exhibit puts the cooperation obligations on him — samples, prism pour,
representative onsite, scheduling, walking inspectors — and excludes *cost of
independent testing laboratory and special inspection services*. That matches both
the specification and the GMP's own exclusion of testing and special inspections.

---

## 4. The $400-per-frame trap, and why it is really a schedule item

Henderson's proposal note, carried into the subcontract at his request:

> *"Hollow metal door frames that are not on-site at the time of wall construction
> will be post Installed at an additional cost of $400 per door frame. Punch and
> dimple by others."*

The descope restates it as an assumption: *"Assume doors to be on-site when
setting block."* A11-10 schedules 22 openings — every one a hollow metal frame
except the overhead coiling door at 102B, which mounts to the face of the CMU.

The exhibit does not carry the $400 adder — it is a condition on his price, not a
scope item, and writing it in would convert an assumption into an entitlement. What
the exhibit does carry is the coordination obligation: *"Coordinate delivery of all
hollow metal frames with the Doors, Frames & Hardware Subcontractor for setting
during masonry construction."*

The real exposure is on the other side of that boundary. The buy-out log already
flags it: **ITB-056's frame procurement chain has to beat the same 04.05.27 CMU
erection date.** ITB-056 (All 5's Construction, $43,186) is not bought either. If
frames land late, this becomes a claim against CORE, not against ITB-056.

Also note *"Punch and dimple by others"* — that is frame preparation for masonry
anchors, and it belongs to whoever supplies the frames. It is excluded here by way
of *supply of hollow metal doors, frames and hardware*.

---

## 5. No signed Bid Form on file for the awarded sub

The proposal is filed as **"031 Masonry - Henderson (backup, no Form)"**, and the
file is a BuildingConnected print plus Henderson's own proposal #26-65. No signed
Subcontractor Proposal (Bid) Form is in `SUBCONTRACTOR FILES/`.

This is a 1% package under NRS 338.16995, so the listing matters. Henderson is on
the GMP's 1% Subcontractor Listing, license 0052532A, so the listing itself is
clean — but confirm a signed Form exists somewhere before relying on it as a
contract-basis document. John Jackson is filed the same way; Kemper and XL both
have Forms.

---

## 6. Bond is not in the $189,449

Henderson's BuildingConnected header carries **Payment & Performance at 1.50%**,
quoted separately, and his proposal table marks Bond Costs excluded. The exhibit
prints the template's **"No Bond Included"** line and the template's own *Bonds*
exclusion, so the document is consistent with the carried number.

At 1.50% a P&P bond on this package is roughly **$2,842**. If CORE is bonding
subcontractors on this job, it is not in the GMP for #031.

---

## 7. Two document conflicts the exhibit no longer speaks to

Both were written into the first draft on the stricter side. Rule 14 struck them,
because both sides of each conflict are already in a contract document. The
conflicts are still real, and they now live only here.

| | Specification | Drawings | Stricter reading |
|---|---|---|---|
| **Control joint spacing** | 04 2016 ¶3.10.F — max 40 ft, nor twice wall height | S4-00 detail 5 note 1 — **max 30'-0"** | 30'-0" |
| **Unit compressive strength** | 04 2016 ¶2.02.A — 2000 psi minimum | S0-00 — individual units **2800 psi**, assembly f'm 2000 psi | 2800 psi units, f'm 2000 psi |

Neither is likely to move the price — 30'-0" joints and 2800 psi units are
ordinary. The place they surface is the control joint layout submittal, which the
mason submits for approval; a 40 ft assumption gets caught there rather than in
the field. If you would rather it be caught before he prices the submittal, the
spacing line is the one item of the 42 I would put back.

Grout runs the other way and needs no action: Henderson assumed **3500 psi** at
descope, against 2000 psi specified. He is over, not under.

---

## 8. Bearing plates: RFP-033 claims installation in one line and disclaims it in the next

Scope of Work #033, two lines apart:

> line 4: *"Supply and install all angles, ledger angles, **CMU wall beam bearing
> plates**, and all related structural steel components…"*
> line 6: *"Provide layout shop drawings for and **supply only, F.O.B. jobsite**,
> all structural steel embeds, **masonry wall embeds**, and anchor bolts…
> Coordinate delivery and layout of embeds with Masonry and Concrete
> Subcontractors."*

Scope of Work #031 resolves it in this package's favour — layout and installation
of all embeds including bearing plates, plus non-shrink grout and drypack under
them — and S4-01 makes it physical: the bearing plates sit in a continuous grouted
bond beam with anchors at 6", which only the mason can build.

**The exhibit follows #031.** But RFP-033 (Corona Steel, $166,281) is not bought
either, and its exhibit must be written so that line 4 does not re-claim the same
plates. Worth carrying forward to whoever drafts #033.

---

## 9. Top-of-wall nailers have no home

XL Concrete Masonry excluded *"Supply / Install Top of Wall Nailers on CMU Walls"*
explicitly — the kind of line a losing bidder writes precisely because the
documents left it ambiguous.

A7-10 shows a continuous nailer and 3/4" pressure treated plywood over the 8" CMU
bond beam at the concession serving opening. Checking the other narratives:

- **RFP-045** covers *"furring, backing, straps, nailers, etc. as necessary to
  support the roofing, fascia & soffit systems"* — that closes the roof-line
  nailers, not this one.
- **RFP-060** covers metal blocking and backing for wall-mounted items, and
  plywood termination boards. Neither is a wood nailer on masonry.

The exhibit excludes *wood nailers, blocking and pressure treated plywood* — it is
not masonry work under any reading of #031. Per rule 12 it does not name who has it,
because on this evidence nobody does. **This needs an owner.**

---

## 10. Smaller things, no decision needed unless you disagree

These are all spec obligations that rule 14 keeps out of the exhibit. They are
real, they bind him through the Subcontract, and they are here so nobody has to
rediscover them at the scope review.

- **Section 04 2016 ¶3.03.E, "Mortar Joints: Match existing CMU at site."** There
  is nothing to match — the existing concessions building is demolished under
  RFP-008. The practical answer is a standard concave joint under paint. Marnell's
  reference-only proposal raised the same point about colour match.
- **Extra materials.** ¶1.12.B requires **50 of each size, colour and type of unit**
  as attic stock. No bidder mentioned it, so nobody has priced delivery of it.
- **Mock-up.** ¶1.08 requires an 8' x 8' wall including mortar and accessories,
  which may not remain. Marnell priced *"Additional Mock Up"* as an add, so one is
  understood to be in the base.
- **Hot weather.** ¶1.10.B requires materials and surrounding air below 90°F prior
  to, during, and for 48 hours after. Masonry is scheduled early April 2027 in
  Tonopah, so this is manageable.
- **Scaffolding** is nobody's stated obligation, but John Jackson, Kemper and XL
  all priced it as their own. It is plainly the mason's means and no longer needs
  saying.
- **Paragraphs 27 and 28 are both kept** per rule 17, and **paragraph 26**
  (underground utility notification) is **cut** — this scope starts at the top of
  a footing placed by others, so there is no underground work to notify for.
- **Phase code 04-1000-10000** (Structural Masonry). The Procore budget confirms
  it independently: RFP-031 has a single budget line, 04-1000-10000 Masonry at
  $189,449, **delta vs carried $0.00**. The cover sheet now reads the code from
  the budget rather than from the package record.
- **Cover sheet dates print CONFIRM.** Anticipated material procurement and start
  dates are CORE-internal and no bid document carries them. The buy-out log's
  own numbers, if you want them as a starting point: release by 2026-12-07,
  CMU procurement 40 days, first field activity "Erect CMU" 2027-04-05.
- **The cover sheet's P&P Bond line is 0%,** so its TOTAL equals the contract
  amount. Henderson's 1.50% is real but separate — see section 6.
- **Open item BID-B02 is now moot.** XL bid #030 and #031 as one bundled scope, but
  #030 is carried with Sahara Concrete and #031 with Henderson, so nothing needs
  to be split.

---

## Where the money sits

| | |
|---|---|
| Henderson base bid, 05.08.26 | **$189,449** |
| Carried on GMP R2 BackSheet row 56 | $189,449 |
| Available and not carried — precision/specified CMU delta | +$4,516 |
| Not in the price — P&P bond at 1.50% | ≈ $2,842 |
| Next bidder (XL, masonry line only) | $267,417 |
| High bidder (John Jackson) | $425,394 |

Henderson is **29% below** the next bidder. That gap is roughly the size of the
items in sections 1, 2 and 3 above, which is the reason to close them in writing
before the subcontract issues rather than after.

## Schedule

Buy-out log ranks this **priority 15, tier 3**. Binding chain is CMU: 15 days
submit, 15 review, 40 procure, 15 execute — **release by 2026-12-07** against an
04.05.27 "Erect CMU" date, with 86 working days of slack. Comfortable, and the
only coupled package is ITB-056 (section 4).
