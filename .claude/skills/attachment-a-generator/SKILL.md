---
name: attachment-a-generator
description: Generates subcontract scope-of-work exhibits (Attachment A) for CMAR/GMP bid packages from RFP/ITB/spec/drawing/bid-form source documents, reconciled against awarded subcontractor proposals where available. Use when indexing bid package source docs, drafting per-package Attachment A scope exhibits, or QA'ing a set of drafted exhibits for gaps/overlaps before subcontract issuance.
---

# Attachment A Generator

Orchestrates a 4-stage pipeline that turns a CMAR project's bid documents into subcontract
scope-of-work exhibits (Attachment A), one per bid package: **index → draft → QA → final exhibit**.

Full architectural rationale: `Tonopah-Attachment-A-System-Master-Plan.md` at the project repo root
(or the equivalent master plan doc for whatever project invokes this skill).

This skill is project-agnostic. Everything project-specific (package list, key dates, folder layout,
drafting-source-of-truth decision) lives in that project's `CLAUDE.md` — read it first.

## Why this is 3 subagents, not 1 loop

A single pass holding the RFP, every package's spec sections, the full drawing set, and the bid form
in context at once produces shallow output — it'll miss spec section references or hallucinate
exclusions because it's spread too thin. Each package also needs to stay grounded in its own slice of
the index; batching all packages in one drafting context risks cross-contamination (Package #030
Concrete language bleeding into #031 Masonry exclusions). So:

- **`doc-indexer`** runs once, builds the full per-package index
- **`scope-drafter`** runs once *per package* (parallelizable), drafts from its own index slice only
- **`scope-qa`** runs once at the end, holding everything, specifically to catch what the narrow
  per-package view can't

## Stage 1 — Index (`doc-indexer` subagent)

Input: the project's `00-source-docs/` tree (read directly via Read/Glob — no Files API upload needed
when running inside Claude Code; that indirection is only for standalone-script use).

Output: one drafting record per package, plus a manifest.

```
01-index/packages/<package_id>.json   what a drafter reads — one package, nothing else
01-index/package-index.json           manifest only: title, award status, counts, file pointer
```

ONE FILE PER PACKAGE is deliberate. A single merged index gets read in full by every drafter run for the
few percent of it that run needs, and it puts all 33 packages' scope in one context — which is the
cross-contamination this pipeline is built to avoid.

### What each package record carries

| Key | Purpose |
|---|---|
| `document_authority_hierarchy` | Restated in every record, because it is the rule the drafter is most likely to invert |
| `scope_narrative.file` | The trade-boundary authority. Read in full, first |
| `spec_sections.primary` | With `basis` (`scope_doc` / `pm_ruling` / `trade_judgment`) and the rationale for each |
| `spec_sections.added_by_pm_ruling` | Sections granted by ruling that the scope doc never cited |
| `spec_sections.flow_down_from_other_packages` | Sections this package complies with but does not carry |
| `spec_sections.cited_but_absent_from_manual` | Real spec gaps, with status and any PM resolution |
| `drawings.draft_from` | Sheets at their current revision. **Retrieval only — never reproduced in the exhibit** |
| `drawings.leads_to_verify` | Weak matches. Open before relying on one; never draft from it unverified |
| `bidders[]` | **Every** bidder's inclusions, exclusions, clarifications and priced line items, with the supersession chain per firm |
| `gmp_basis_exhibit_b` | Scope assumptions, exclusions, prevailing wage and sales tax |
| `open_pm_items` | Unresolved decisions touching this package, carried into the draft as visible notes |

On this project the records are built by `scripts/build_package_index.py`, which merges the outputs of
`index_proposals.py`, `index_spec_sections.py` and `assign_sheets.py`. The `doc-indexer` agent and the
legacy single-file schema it writes are superseded by those scripts — deterministic extraction beats an
agent re-reading 343 documents, and it is re-runnable when an addendum lands.

**Human Checkpoint #1**: the PM reviews the per-package records in `01-index/packages/` by hand
before any drafting starts. This is
the highest-leverage review point in the pipeline — every draft downstream inherits whatever's wrong here.

## Stage 2 — Draft (`scope-drafter` subagent, run once per package)

Input: one package's record (`01-index/packages/<package_id>.json`) plus the specific
source files it cites. Never the full index — that's the cross-contamination risk.

Output: `01-index/attachment-a-content/<package_id>.json` — the content record that
`scripts/build_attachment_a.py` renders into CORE's Word template. Not a markdown draft; the
markdown form was the original design and it could not be built from.

Per package, end to end:

```
# 1. draft — writes 01-index/attachment-a-content/<id>.json
Task(scope-drafter, "<package_id>")

# 2. check the voice before building
python3 scripts/voice_check.py <package_id>

# 3. build the exhibit and its Bluebeam review cover sheet
python3 scripts/build_attachment_a.py <package_id>
python3 scripts/build_att_a_cover.py <package_id>

# 4. track it in the buy-out log
#    add <package_id> to ATT_A_DRAFTED in scripts/build_buyout_log.py, then:
python3 scripts/build_buyout_log.py
```

Everything lands in `02-drafts/<package_id>/` — `<Sub> Draft Att A.docx`,
`<Sub> - Att A Review Cover Sheet.xlsx`, and `PM-NOTES.md` for judgment calls that do not belong
in an exhibit.

### Drafting rules

- **Write in the PM's voice.** Read `references/voice-profile.md` before drafting a scope group.
  It is measured from 40 exhibits he wrote and CORE executed, across two jobs, and it settles
  what a drafter would otherwise guess at: the group-header formula, item length (his median is
  **13 words** — drafts written without it run double), which verbs open an item, that
  `Includes …` carries 15.7% of them, how numbers and citations are written, and that exclusions
  are terse and do not route. It is also the record of what earlier versions got wrong, so read
  the withdrawn rules too — they are the mistakes most likely to be made again.
- **Cite in `_sources`, not inline.** His exhibits carry no parenthetical citation after each
  bullet. They cite a detail or sheet where it fixes an obligation (`per 5/S5.44`) and otherwise
  say `as indicated`. Record everything read — spec sections, sheets at their revision, the
  awarded sub's proposal and descopes — in the content record's `_sources`, so `scope-qa` and the
  PM can trace every claim without the exhibit reading like a research memo.
- **Not-yet-awarded packages**: draft strictly from generic RFP/ITB/spec/scope-of-work language, and add a
  visible header note: `> Awarded subcontractor TBD as of [index date] — draft based on generic RFP scope.`
- **Structure**: trade groups in build order, then a bare `General Scope Requirements` closing
  group. No separate "Coordination with Adjacent Trades" group — coordination rides with the item
  it qualifies, naming the counterparty by its subcontract role.
- **No uncited scope language.** If you cannot ground an item in a source, don't claim it either
  way — record it in `_open_pm_items`. That's the "plausible-sounding filler" failure mode this
  pipeline exists to avoid; the fix is grounding, not a parenthetical.
- **Never put a drawing roster in the exhibit.** The sheet→package index is a retrieval tool that tells the
  drafter what to read; it is not exhibit content. Do not emit an "Applicable Drawings" or "Sheets Included"
  list, and do not enumerate a package's sheets anywhere in the draft. An enumerated sheet list in a
  subcontract works against the GC: it creates the negative implication that unlisted sheets do not apply,
  which narrows a broad "complete scope per plans and specifications" obligation into a bounded one and
  hands the subcontractor an argument in the first change-order dispute. It also goes stale the moment an
  addendum reissues a sheet. Cite a sheet only where it does work a citation should do — fixing a trade
  boundary, resolving an ambiguity, or pinning a basis of design — exactly as the Scope of Work narratives
  themselves do ("See A1-20 for Gate Schedule and details").
- **Write to the schedule and the specification, not to a model number.** A subcontract naming a specific
  model buys that model and nothing else; when a submittal returns a superseded part number the sub has an
  argument it was not in scope. Write *"all fan coil units and heat pumps as indicated on the mechanical
  schedule, including any additional parts and accessories for a complete installation"*, not *"one Daikin
  FXSA18AAVJU at the restrooms"*. Name a product only where a contract document establishes it as basis of
  design — an RFI answer, an addendum, a GMP Basis assumption, a drawn BOD keynote — then cite that
  instrument and still require a complete installation around it.
- **Never cite a specification section absent from the Project Manual.** The obligation stays in the
  subcontract, carried by the scope verbiage using the section's *title*, never its number — "metal roof
  panels", not "07 41 13". A number the sub cannot look up makes an obligation look documented when
  nothing stands behind it. Draft those from the scope narrative, the drawings and the proposals.
- **Think past what the documents happen to say.** This is a subcontract, not an RFP summary. If the manual
  has a masonry section and this is the masonry package, it belongs in the subcontract whether or not the
  scope narrative cited it — as do the ordinary obligations of a complete trade scope (layout from
  established control, protection of adjacent work, receiving and offloading, cleanup of own debris,
  warranty, submittal coordination). Assignments made by trade judgment are marked as such in the record;
  they belong in the subcontract, but only citation-backed items may be written as citations.
- If a package's `awarded_sub.flags` includes a PM-review flag (e.g. "awarded sub was not low bidder," "no
  signed Bid Form on file"), carry it forward as a visible note at the top of the draft, not silently.

Run 33 times (or however many packages the project has), one Task/Agent invocation per package_id.
Can be parallelized freely — each run is independent by design.

### Voice check before build

`scripts/voice_check.py <package_id>` checks a package's content record against the
mechanical half of the voice profile — header formula, weak openers, banned abbreviations,
longhand dimensions, item length, and whether enough items name who has the adjacent work.
Run it before `build_attachment_a.py`; it reads the content record, so a violation gets fixed
at its source rather than typed into a generated file the next build overwrites.

It deliberately reports only what a pattern can decide without judgment. The substantive
rules stay drafting instructions — a check that cries wolf gets switched off.

## Stage 3 — QA (`scope-qa` subagent, run once)

Input: all drafts in `02-drafts/`, every record in `01-index/packages/`, and the bid form.

Output: `03-qa/scope-leveling-register.xlsx` (or `.csv`/`.md` table if no xlsx writer is available —
columns: gap/overlap description, packages involved, severity, recommended resolution).

Checks:
1. **Gaps** — work documented somewhere in the source docs with no home in any Attachment A. Specifically
   check known gap zones: temp power, roof curbs/equipment pads, fire caulking, final grade/seed, access panels.
2. **Overlaps** — two packages both claiming the same scope.
3. **Proposal-vs-RFP contradictions** — for reconciled packages, does the awarded sub's proposal exclude
   something the RFP scope-of-work assumed was included (or vice versa)? This is the check unique to the
   "reconciled to awarded sub" drafting mode — flag every contradiction found, don't silently resolve it.

This step needs to hold the full leveling matrix in mind at once and catch what's missing rather than
generate forward from a template — use Opus-class reasoning (see `.claude/agents/scope-qa.md` model setting).

**Human Checkpoint #2**: PM resolves every flagged gap/overlap/contradiction — this is judgment the PM has
to own, not something to auto-resolve. Decide negotiable-vs-non-negotiable language per project norms.

## Stage 4 — Final Exhibit

Convert PM-approved drafts into the project's branded Attachment A exhibit format (docx), one per package,
landing in `04-output/`, ready to attach to the subcontract agreement template. This step is manual/PM-driven
once drafts are approved — no subagent needed unless the project has a docx-templating skill available.

## Reference

- `references/csi-divisions.md` — CSI MasterFormat division numbers, used to tag `csi_divisions` in the index
  and to map spec-manual-split filenames (`div-XX-*.pdf`) to package scope.
