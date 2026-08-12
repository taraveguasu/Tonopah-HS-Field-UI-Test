# Tonopah HS Field UI Test

A working-files clone of [`taraveguasu/tonopah-sports-field-complex`](https://github.com/taraveguasu/tonopah-sports-field-complex),
created for UI development and testing against the project's structured data.

## Attachment A Build Console

`docs/index.html` is an HTML console for the drafting pipeline. Pick a bid package,
tick the open PM items the build has to settle, add any extra requirements, and it
assembles a build request you can paste into a Claude Code session or file as an
issue. For packages already drafted it links the three files the PM reviews — the
review cover sheet, the draft exhibit, and `PM-NOTES.md` — straight off this repo.

```bash
python3 scripts/build_attachment_a_console.py   # rebuild after every package build
```

It reads `01-index/buyout-log.json` and the files actually present in `02-drafts/`,
so a package moves from "not started" to live download buttons the moment its build
lands and the console is regenerated. Two outputs: `docs/index.html` (a full page,
ready for GitHub Pages from the `docs/` folder) and `docs/artifact.html` (the same
page as a body-only fragment for publishing as a Claude Artifact).

## What this repo is

Everything from the source repo **except the source-document PDFs**. That means the
structured index, the drafted exhibits, the build scripts, and the skill/agent
definitions are all here and complete — but the 500 MB of drawings, specifications,
subcontractor proposals and addenda are not.

| Path | Status |
|---|---|
| `CLAUDE.md` | ✅ complete — project memory, rulings log, open items |
| `01-index/` | ✅ complete — package records, proposal content, spec catalog, sheet assignments, budget codes, buy-out log |
| `02-drafts/` | ✅ complete — the 11 drafted Attachment A packages |
| `04-output/` | ✅ complete — buy-out log and release priority |
| `scripts/` | ✅ complete |
| `.claude/` | ✅ complete — `attachment-a-generator` skill, three subagent definitions, voice profile |
| `00-source-docs/` | ⚠️ **partial by design** — see below |

## What was left out

`00-source-docs/` retains only the derived and template files the tooling actually
reads:

- `02-trade-scopes-bidform/_extracted/*.txt` — all 35 extracted scope narratives
  (the primary scope authority; the `.docx` originals they came from are omitted)
- `04-specs-reports/spec-manual-split/_manifest.json` — the split manifest, without the 22 division PDFs
- `07-budget/Procore Project Budget.csv`
- `05-supplemental/attachment-a-process/` and
  `SUBCONTRACTOR FILES/0 - ATTACHMENT A - Scope of Work/` — the CORE Attachment A
  templates that `build_attachment_a.py`, `build_att_a_cover.py` and
  `build_voice_corpus.py` import

Omitted: all drawing sets, the specification manual and its split, geotech and
asbestos reports, addenda, the GMP workbook, and every subcontractor proposal,
descope and scope-review agenda.

Note that much of that omitted content survives in extracted form under
`01-index/document-text/`, `01-index/proposal-content.json` and
`01-index/sheets/`, so most analysis still works.

## What this means in practice

Scripts that read the structured index run normally. Scripts that reach for an
omitted PDF will fail on a missing path — re-clone the source repo, or copy
`00-source-docs/` across from it, if you need the full document set.

**This is a test/development clone. It is not the buy-out system of record** —
that remains `taraveguasu/tonopah-sports-field-complex`.
