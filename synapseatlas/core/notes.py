import os, re, json
from typing import List, Dict, Optional

ROOT = os.path.dirname(os.path.dirname(__file__))
BASE = os.path.dirname(ROOT)
NOTES = os.path.join(BASE, "notes")
META  = os.path.join(BASE, "data", "meta")

RX_LINK = re.compile(r"\[\[([^\[\]]+)\]\]")
RX_TAG  = re.compile(r"(?<!\w)#([a-zA-Z0-9_\-]+)")

def ensure():
    os.makedirs(NOTES, exist_ok=True)
    os.makedirs(META,  exist_ok=True)

def slug(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^a-z0-9\-_]+", "", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "note"

def list_notes(max_mb: int = 1) -> List[str]:
    ensure()
    out = []
    for name in os.listdir(NOTES):
        if name.startswith('.') or name.startswith('_'): continue
        if not name.endswith('.md'): continue
        if name.endswith(('.swp','.tmp','.bak','~')): continue
        p = os.path.join(NOTES, name)
        if not os.path.isfile(p): continue
        try:
            if os.path.getsize(p) > max_mb * 1024 * 1024: continue
        except OSError:
            continue
        out.append(name)
    return sorted(out)

def read_note(filename: str) -> Optional[str]:
    p = os.path.join(NOTES, filename)
    return open(p, "r", encoding="utf-8").read() if os.path.exists(p) else None

def write_note(title: str, content: str) -> str:
    ensure()
    fname = slug(title) + ".md"
    p = os.path.join(NOTES, fname)
    with open(p, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{content.strip()}\n")
    return p

def extract(text: str) -> Dict[str, List[str]]:
    return {
        "links": sorted(set(RX_LINK.findall(text or ""))),
        "tags":  sorted(set(RX_TAG.findall(text or ""))),
    }

def build_index() -> str:
    ensure()
    idx = {}
    for fn in list_notes():
        idx[fn] = extract(read_note(fn) or "")
    out = os.path.join(META, "index.json")
    json.dump(idx, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return out
# tweak 2025-10-22T17:20:31.879099+00:00

# autosave 2025-11-05T13:16:48.107587+00:00

# autosave 2025-11-14T11:55:17.369756+00:00

# autosave 2026-01-30T15:34:37.523658+00:00
