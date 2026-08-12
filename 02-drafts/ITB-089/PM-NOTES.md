# ITB-089 — notes for the Attachment A review

YESCO · Contract amount **$99,483.00** · Procore `11-0101-10000`

These are the judgment calls and the open commercial gaps; none appear in the exhibit.

---

## 0. The package record said "not yet awarded." It is wrong.

`01-index/packages/ITB-089.json` carries a bare `{"status": "not-yet-awarded"}`. It
was built 07.10.26 and **predates the GMP.** The BackSheet (line 89) and Procore both
carry **YESCO at $99,483**, matching YESCO's own itemized scoreboard pricing exactly.

Same stale-record pattern already documented for ITB-072, RFP-094 and RFP-109 — and
found again on ITB-008 in this same batch. This exhibit is drafted against YESCO.
**The mapping should be updated** so the next session does not re-draft it as
unawarded.

---

## 1. ⚠️ HIGHEST PRIORITY — the foundation is priced here and drafted elsewhere

The carried $99,483 reconciles exactly:

| | |
|---|---:|
| Base scope | 67,030 |
| Mobilization | 3,103 |
| **Add alternate — footing excavation and concrete** | **29,350** |
| **Carried** | **99,483** |

But **the exhibit does not carry foundation construction.** Scope of Work #030
explicitly assigns *"Scoreboard footings. Coordinate with Scoreboard Subcontractor
for requirements"* — the identical construction it uses for the Press Box, Ticket
Booth, Bleacher and Athletic Equipment footings, and consistent with your 07.31.26
ruling that athletic-equipment footings are RFP-030. RFP-030's exhibit carries the
scoreboard footing by name.

So this exhibit is drafted so YESCO **designs** the foundation (it is a deferred
submittal) and coordinates embeds and anchor bolts with the Concrete Subcontractor,
but does not excavate or place concrete — while **the money still has the concrete
in it.**

Two ways to close it, and one has to be chosen before either subcontract issues:

- **(a)** The alternate was genuinely accepted and YESCO does build the foundation —
  then **RFP-030's exhibit must exclude the scoreboard footing and deduct
  accordingly.**
- **(b)** The $29,350 does not belong in this package — then **the Subcontract Amount
  drops to $70,133.**

**Do not issue both subcontracts with the scoreboard foundation priced twice.** This
is one of three instances of the same problem in this batch; see
`02-drafts/RFP-030/PM-NOTES.md` §1 for the consolidated view.

## 2. Galvanizing — the drawings require it, the price does not include it

**S0-00 General Note 9** requires all steel exposed to weather to be **hot-dip
galvanized after fabrication.** YESCO's carried proposal says only *"Prime and paint
structural steel."*

The exhibit states the documented galvanized requirement rather than quietly
accepting the cheaper finish the sub priced. That means **the price is likely light.**
Decide whether galvanizing is actually required — if prime-and-paint is acceptable
for this structure, the carried price already matches scope and the exhibit should
be relaxed.

## 3. Basis of design — FB-2021, not the specified FB-2022

Section 11 6843 Part 2 names the **Daktronics FB-2022**, which **Clarification No. 1
RFI #5 confirms is discontinued**. The RFI response gives **FB-2021**, which matches
the Site Equipment Matrix on A1-20 (Addendum #1) and all three itemized bidder
proposals — YESCO, Image360 and Y C Signs all priced FB-2021.

The exhibit follows the RFI. No action; recorded so the spec's model number does not
resurface at submittal as a rejection basis.

## 4. Electrical feed boundary — drafted to YESCO's number, worth a spot check

Scope of Work #103 puts *"power and data to Scoreboard"* inside Electrical's site
conduit and wiring scope. YESCO excludes *"Site Electrical & Low Voltage Systems"*
and asks only that power be brought **within 10 feet** for final connections.

The exhibit follows YESCO's 10-foot boundary because it is the more specific sourced
figure. **But sheet note 3/E1-10 — cited by Scope of Work #089 itself — was not
opened**, because E1-10 is not on this package's assigned sheet list. Worth a look
before issue; it may set the boundary differently.

## 5. Deferred submittal — the schedule has nothing for it

G0-00 lists the scoreboard as a **deferred submittal**, so the design goes through
the AHJ, not just the EOR. The 04.21.26 schedule carries **no procurement activity
for it at all.** Its foundation is RFP-030's pour and its feed is RFP-103's conduit,
so both of those need its layout — which is why it ranks 5th despite being a
$99,483 package.

## 6. YESCO holds three packages

ITB-072 Building Signage, ITB-078 Flagpoles and this one. The release-priority log
flags that one agreement would pull all three to **2026-10-19**, ITB-089's date.
That is your call, not an assumption this exhibit makes — drafted standalone per the
one-exhibit-per-package practice.

## 7. Data quality — Monument's descope files belong to another package

The package record links a Monument "Scope Review Meeting Agenda" and "Homework
Response" under ITB-089. **Both actually contain RFP-016/022 irrigation and turf
content** — *"Sprinturf as 2nd tier sub," "Includes geo-fabric, base, filter, and
turf."* Misindexed by the doc-indexer pass.

Monument's real Scoreboards Bid Form ($75,334.14) carries no scope breakdown and was
used instead. Flagged so the index gets corrected.

---

## Rule 14 review page

**8 struck items** on the trailing page. Build with `--final` to drop it.
Voice check: clean.
