#!/usr/bin/env python3
"""
Build the Attachment A Build Console -- the HTML front end for the drafting
pipeline.

The console does three things, in the order a package actually moves:

  1. Pick the package.  The list is the buy-out log's own release ranking, so
     the package at the top is the one that has to issue first, not the one
     that happens to sort first alphabetically.
  2. State the requirements.  Open PM items come straight off the buy-out log
     as tick boxes; anything else goes in free text.  Both are written into a
     build request that can be pasted into a Claude Code session or filed as an
     issue on the repo.
  3. Download the three files the PM reviews, once the package has been built:
     the draft exhibit, the review cover sheet, and PM-NOTES.md.

It is generated, not hand-maintained.  Every fact on the page comes from
01-index/buyout-log.json or from the files actually present in 02-drafts/, so
rerunning this after a build is what moves a package from "not started" to a
row with live download buttons.  Nothing here is a second copy of the record.

Two outputs, same page:
  docs/index.html      full document, for GitHub Pages
  docs/artifact.html   body-only fragment, for publishing as a Claude Artifact

Usage:  python3 scripts/build_attachment_a_console.py
"""

import json
import re
import subprocess
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHELL = Path(__file__).resolve().parent / "attachment-a-console.shell.html"
BUYOUT = ROOT / "01-index" / "buyout-log.json"
DRAFTS = ROOT / "02-drafts"
DOCS = ROOT / "docs"

TITLE = "Attachment A Build Console"
DESCRIPTION = ("Pick a Tonopah bid package, set the requirements, and download the "
               "three Attachment A files the PM reviews.")

# The three files a completed package hands to the PM, listed in the order the
# Bluebeam process document builds the review packet: cover sheet first, then
# the draft exhibit, then the notes behind it.
#
# `view` decides how the browser gets each one. raw comes back as
# application/octet-stream and downloads; markdown raw is served as text/plain
# and would open as an unreadable wall of text, so PM-NOTES.md points at
# GitHub's rendered blob view instead.
FILE_KINDS = [
    (re.compile(r"Att A Review Cover Sheet\.xlsx$"),   "XLSX", "Review cover sheet",  "raw"),
    (re.compile(r"Draft Att A\.docx$"),                "DOCX", "Draft Attachment A",  "raw"),
    (re.compile(r"^PM-NOTES\.md$"),                    "MD",   "PM notes",            "blob"),
]


def repo_url():
    """Origin URL, normalised to a browsable https form without the .git suffix."""
    try:
        url = subprocess.run(["git", "remote", "get-url", "origin"], cwd=ROOT,
                             capture_output=True, text=True, check=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "https://github.com/taraveguasu/Tonopah-HS-Field-UI-Test"
    if url.startswith("git@"):
        url = "https://" + url[4:].replace(":", "/", 1)
    return url[:-4] if url.endswith(".git") else url


def tier_number(tier):
    """'2 - next 60 work days' -> 2.  A removed package sorts last."""
    m = re.match(r"\s*(\d+)", tier or "")
    return int(m.group(1)) if m else 9


def review_files(package_id):
    """The three review files, if the package has actually been built.

    Matched by suffix rather than by subcontractor name so a package survives a
    change of carried sub.  PM markup copies are deliberately left out -- those
    are the PM's own returns, not the draft going out to him.
    """
    folder = DRAFTS / package_id
    if not folder.is_dir():
        return []
    found = []
    for name in sorted(p.name for p in folder.iterdir() if p.is_file()):
        if "PM markup" in name:
            continue
        for rank, (pattern, kind, label, view) in enumerate(FILE_KINDS):
            if pattern.search(name):
                found.append({
                    "name": name,
                    "path": f"02-drafts/{package_id}/{name}",
                    "kind": kind,
                    "label": label,
                    "view": view,
                    "rank": rank,
                    "size": (folder / name).stat().st_size,
                })
                break
    found.sort(key=lambda f: f["rank"])
    # Only a complete set counts as built: a package missing its cover sheet or
    # its notes is a half-finished build, and offering two of three buttons
    # would read as if the third were never required.
    return found if len(found) == len(FILE_KINDS) else []


def build_packages():
    log = json.loads(BUYOUT.read_text())
    out = []
    for p in log["packages"]:
        pid = p["package_id"]
        files = review_files(pid)
        removed = "not released" in (p.get("tier") or "")
        out.append({
            "id": pid,
            "title": p.get("title") or "",
            "source": p.get("source") or "",
            "tier": p.get("tier") or "—",
            "tier_n": tier_number(p.get("tier")),
            "rank": p.get("priority_rank"),
            "sub": p.get("carried_sub") if p.get("carried_sub") not in (None, "—") else None,
            "value": p.get("carried_value"),
            "phase_code": p.get("phase_code") if p.get("phase_code") not in (None, "—") else None,
            "release_by": p.get("latest_release_date"),
            "draft_by": p.get("draft_by"),
            "binding_chain": p.get("binding_chain"),
            "chain_days": p.get("chain_days"),
            "open_items": p.get("open_items") or [],
            "other_factors": p.get("other_factors") or [],
            "drafted": bool(files),
            "removed": removed,
            "files": files,
        })
    # Release priority is the running order of the job. Anything unranked (the
    # removed package) falls to the bottom rather than to the top.
    out.sort(key=lambda p: (p["rank"] is None, p["rank"] or 0))
    return out


def main():
    packages = build_packages()
    url = repo_url()
    data = {
        "generated": date.today().strftime("%m.%d.%y"),
        "repo": url,
        "repo_name": "/".join(url.split("/")[-2:]),
        "branch": "main",
        "packages": packages,
    }

    core = SHELL.read_text()
    if "/*__DATA__*/null" not in core:
        raise SystemExit("shell is missing its /*__DATA__*/null token")
    core = core.replace("/*__DATA__*/null",
                        json.dumps(data, separators=(",", ":"), ensure_ascii=False))

    DOCS.mkdir(exist_ok=True)

    # Full document for GitHub Pages.
    (DOCS / "index.html").write_text(
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f'<meta name="description" content="{DESCRIPTION}">\n'
        '</head>\n<body>\n' + core + '\n</body>\n</html>\n'
    )

    # Body-only fragment: the Artifact host supplies the document skeleton and
    # reads the <title> out of the first 8KB, which is why it stays at the top.
    (DOCS / "artifact.html").write_text(core)

    built = sum(1 for p in packages if p["drafted"])
    print(f"docs/index.html + docs/artifact.html — {len(packages)} packages, "
          f"{built} with a complete review set")
    for p in packages:
        if p["drafted"]:
            print(f"  ✓ {p['id']:8} {sum(f['size'] for f in p['files'])//1024:>4} KB "
                  f"across {len(p['files'])} files")


if __name__ == "__main__":
    main()
