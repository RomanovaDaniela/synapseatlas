import re
HDR = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)
def headings(md: str): return [(m.group(1), m.group(2).strip()) for m in HDR.finditer(md or "")]

# autosave 2025-10-06T10:48:06.382817+00:00

# autosave 2026-03-04T12:37:20.610353+00:00
