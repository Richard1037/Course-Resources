"""Extract clean UTF-8 text from every PDF in the workspace (control chars stripped)."""
import os
import re
import unicodedata
import pymupdf

ROOT = r"D:\Note\linear-algebra"
OUT = os.path.join(ROOT, "Dpsk", "_extract")
os.makedirs(OUT, exist_ok=True)

CTRL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")


def clean(text: str) -> str:
    text = text.replace("\u00ad", "")
    text = CTRL.sub("", text)
    text = "".join(
        ch if ch in "\n\t" else (ch if unicodedata.category(ch) != "Cc" else "")
        for ch in text
    )
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


targets = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    if "_extract" in dirpath or "_img" in dirpath:
        continue
    for fn in filenames:
        if fn.lower().endswith(".pdf"):
            targets.append(os.path.join(dirpath, fn))
targets.sort()

for path in targets:
    rel = os.path.relpath(path, ROOT)
    safe = rel.replace("\\", "__").replace("/", "__")
    dest = os.path.join(OUT, safe + ".txt")
    try:
        doc = pymupdf.open(path)
        chunks = []
        for i, page in enumerate(doc, 1):
            chunks.append("\n===== PAGE %d =====\n%s" % (i, clean(page.get_text("text"))))
        with open(dest, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("".join(chunks))
        print("OK  %-46s pages=%d" % (rel, doc.page_count))
        doc.close()
    except Exception as exc:
        print("ERR %-46s %s" % (rel, exc))
