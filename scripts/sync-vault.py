#!/usr/bin/env python3
"""Mirror the publishable part of the Machi Obsidian vault into content/.

Only paths listed in INCLUDE are copied; everything else in the vault
(private/, daily/, documents/, templates, plugin folders...) never reaches
this repo. A note can also opt out with `publish: false` in its frontmatter.

Dataview blocks cannot run on the static site, so each one is evaluated here
against the published notes and replaced with a plain list or table.

Usage: scripts/sync-vault.py [--vault PATH]
"""

import argparse
import os
import re
import shutil
import sys
from datetime import date, datetime
from pathlib import Path
from urllib.parse import unquote

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "content"
DEFAULT_VAULT = Path.home() / "Documents/personal/obsidian/Machi"

# Vault-relative paths that get published.
INCLUDE = [
    "notes/cs",
    "notes/hacking",
    "notes/cheatsheets",
    "notes/leetcode",
    "notes/university",
    "notes/inbox",
    "notes/knowledge-hub.md",
]

# Vault-relative paths that are never published, even inside INCLUDE.
# Prefer `publish: false` in the note itself: this file is public.
EXCLUDE = []

# Files in content/ owned by this repo rather than the vault.
KEEP = {"index.md"}

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


# --- notes ----------------------------------------------------------------


class Note:
    def __init__(self, vault, path):
        self.path = path
        self.rel = path.relative_to(vault).as_posix()
        self.stem = path.stem
        self.folder = path.parent.relative_to(vault).as_posix()
        self.text = path.read_text(encoding="utf-8")
        self.meta = parse_frontmatter(self.text)
        self.mtime = datetime.fromtimestamp(path.stat().st_mtime)
        created = self.meta.get("created")
        try:
            self.ctime = datetime.fromisoformat(str(created))
        except (TypeError, ValueError):
            self.ctime = self.mtime

    @property
    def title(self):
        return self.meta.get("title") or self.stem

    @property
    def tags(self):
        tags = self.meta.get("tags") or []
        if isinstance(tags, str):
            tags = [tags]
        inline = re.findall(r"(?<![\w&/])#([\w/-]+)", strip_code(self.text))
        return {t.lstrip("#") for t in list(tags) + inline}

    def link(self):
        return f"[{self.title}]({self.rel})"


def parse_frontmatter(text):
    """Minimal YAML frontmatter reader: scalars and simple lists."""
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    meta, key = {}, None
    for line in m.group(1).splitlines():
        item = re.match(r"\s+-\s*(.*)", line)
        if item and key:
            if not isinstance(meta.get(key), list):
                meta[key] = []
            meta[key].append(item.group(1).strip().strip("\"'"))
            continue
        kv = re.match(r"([\w-]+):\s*(.*)", line)
        if kv:
            key, value = kv.group(1), kv.group(2).strip().strip("\"'")
            meta[key] = value if value else None
    return meta


def strip_code(text):
    return re.sub(r"```.*?```", "", text, flags=re.S)


def is_published(rel, meta):
    if any(rel == e or rel.startswith(e + "/") for e in EXCLUDE):
        return False
    return str(meta.get("publish", "true")).lower() != "false"


def collect_notes(vault):
    notes = []
    for inc in INCLUDE:
        root = vault / inc
        paths = [root] if root.is_file() else sorted(root.rglob("*.md"))
        for p in paths:
            note = Note(vault, p)
            if is_published(note.rel, note.meta):
                notes.append(note)
    return notes


# --- dataview -------------------------------------------------------------


class Unsupported(Exception):
    pass


def field(note, name):
    return {
        "file.name": note.stem,
        "file.folder": note.folder,
        "file.mtime": note.mtime,
        "file.ctime": note.ctime,
        "title": note.title,
    }.get(name, note.meta.get(name))


def fmt(value):
    if isinstance(value, datetime):
        return value.strftime("%d %b %Y")
    return "" if value is None else str(value)


def eval_condition(expr, note):
    """Evaluate a Dataview WHERE clause (and/or of simple comparisons)."""
    for op in (" or ", " and "):
        parts = split_top(expr, op)
        if len(parts) > 1:
            results = (eval_condition(p, note) for p in parts)
            return any(results) if op == " or " else all(results)
    expr = expr.strip()
    neg = expr.startswith("!")
    if neg:
        expr = expr[1:].strip()
    m = re.fullmatch(r'contains\(\s*([\w.]+)\s*,\s*"([^"]*)"\s*\)', expr)
    if m:
        result = m.group(2) in fmt(field(note, m.group(1)))
        return not result if neg else result
    m = re.fullmatch(r'([\w.]+)\s*(!=|=)\s*"([^"]*)"', expr)
    if m:
        equal = fmt(field(note, m.group(1))) == m.group(3)
        return equal if m.group(2) == "=" else not equal
    raise Unsupported(f"where: {expr}")


def split_top(expr, sep):
    """Split on sep outside parentheses and quotes."""
    parts, depth, quote, start, i = [], 0, False, 0, 0
    while i < len(expr):
        c = expr[i]
        if c == '"':
            quote = not quote
        elif not quote and c == "(":
            depth += 1
        elif not quote and c == ")":
            depth -= 1
        elif not quote and depth == 0 and expr.startswith(sep, i):
            parts.append(expr[start:i])
            i += len(sep)
            start = i
            continue
        i += 1
    parts.append(expr[start:])
    return parts


def matches_source(source, note):
    terms = [t.strip() for t in source.split(" or ")]
    for t in terms:
        if t.startswith('"'):
            folder = t.strip('"').rstrip("/")
            if note.rel.startswith(folder + "/") or folder == "":
                return True
        elif t.startswith("#"):
            tag = t[1:]
            if any(x == tag or x.startswith(tag + "/") for x in note.tags):
                return True
        else:
            raise Unsupported(f"from: {t}")
    return False


def column(expr, note):
    expr = expr.strip()
    m = re.fullmatch(r'dateformat\(\s*([\w.]+)\s*,\s*"[^"]*"\s*\)', expr)
    if m:
        return fmt(field(note, m.group(1)))
    if expr == "file.link":
        return note.link()
    return fmt(field(note, expr)).replace("|", "\\|")


def render_query(query, notes, here):
    q = " ".join(query.split())
    m = re.match(
        r"(?i)(list|table)(?: without id)?\s*(.*?)\s*\bfrom\s+(.+?)"
        r"(?:\s+where\s+(.+?))?(?:\s+sort\s+([\w.]+)\s+(asc|desc))?"
        r"(?:\s+limit\s+(\d+))?\s*$",
        q,
    )
    if not m:
        raise Unsupported(q)
    kind, cols, source, where, sort_key, order, limit = m.groups()
    rows = [n for n in notes if n is not here and matches_source(source, n)]
    if where:
        rows = [n for n in rows if eval_condition(where, n)]
    if sort_key:
        rows.sort(
            key=lambda n: (field(n, sort_key) is None, field(n, sort_key) or ""),
            reverse=order.lower() == "desc",
        )
    if limit:
        rows = rows[: int(limit)]
    if not rows:
        return "*Nothing here yet.*"
    if kind.lower() == "list":
        return "\n".join(f"- {n.link()}" for n in rows)
    headers, exprs = [], []
    for c in split_top(cols, ","):
        cm = re.fullmatch(r'\s*(.+?)\s+as\s+"([^"]*)"\s*', c)
        exprs.append(cm.group(1) if cm else c.strip())
        headers.append(cm.group(2) if cm else c.strip())
    lines = ["| " + " | ".join(headers) + " |", "|" + " --- |" * len(headers)]
    for n in rows:
        lines.append("| " + " | ".join(column(e, n) for e in exprs) + " |")
    return "\n".join(lines)


def render_dataview(note, notes, warnings):
    def repl(m):
        lang, body = m.group(1), m.group(2)
        if lang == "dataviewjs":
            return ""
        try:
            return render_query(body, notes, note)
        except Unsupported as e:
            warnings.append(f"{note.rel}: dropped dataview block ({e})")
            return ""

    return re.sub(r"```(dataviewjs|dataview)\n(.*?)```", repl, note.text, flags=re.S)


# --- images ---------------------------------------------------------------


def referenced_images(text):
    names = re.findall(r"!\[\[([^\]|#]+)", text)
    for p in re.findall(r"!\[[^\]]*\]\(([^)\s]+)", text):
        if not re.match(r"[a-z]+://", p):
            names.append(unquote(os.path.basename(p)))
    return {n.strip() for n in names if Path(n.strip()).suffix.lower() in IMAGE_EXTS}


def index_images(vault):
    """Map image basename to path, skipping folders that are never published."""
    skip = {".obsidian", ".stversions", ".trash", "private", "copilot"}
    index = {}
    for p in vault.rglob("*"):
        rel = p.relative_to(vault)
        if rel.parts[0] in skip or p.suffix.lower() not in IMAGE_EXTS:
            continue
        index.setdefault(p.name, p)
    return index


# --- main -----------------------------------------------------------------


def clean_content():
    for p in CONTENT.iterdir():
        if p.name in KEEP:
            continue
        shutil.rmtree(p) if p.is_dir() else p.unlink()


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    args = ap.parse_args()
    vault = args.vault.expanduser().resolve()
    if not (vault / ".obsidian").is_dir():
        sys.exit(f"error: {vault} is not an Obsidian vault")

    notes = collect_notes(vault)
    warnings, wanted = [], set()
    clean_content()
    for note in notes:
        out = CONTENT / note.rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_dataview(note, notes, warnings), encoding="utf-8")
        mtime = note.path.stat().st_mtime
        os.utime(out, (mtime, mtime))
        wanted |= referenced_images(note.text)

    images = index_images(vault)
    (CONTENT / "images").mkdir(exist_ok=True)
    for name in sorted(wanted):
        if name in images:
            shutil.copy2(images[name], CONTENT / "images" / name)
        else:
            warnings.append(f"missing image: {name}")

    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)
    copied = len(wanted) - sum(w.startswith("missing image") for w in warnings)
    print(f"synced {len(notes)} notes and {copied} images from {vault}")


if __name__ == "__main__":
    main()
