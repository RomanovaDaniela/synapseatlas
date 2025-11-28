import os, csv
from ..graph.build import load_index

ROOT = os.path.dirname(os.path.dirname(__file__))
BASE = os.path.dirname(ROOT)
REPORTS = os.path.join(BASE, "reports")

def export_tags_csv() -> str:
    os.makedirs(REPORTS, exist_ok=True)
    idx = load_index()
    p = os.path.join(REPORTS, "tags.csv")
    with open(p, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(["file","tags"])
        for fn, meta in idx.items():
            w.writerow([fn, ",".join(meta.get("tags", []))])
    return p

# autosave 2025-11-28T13:08:56.450503+00:00
