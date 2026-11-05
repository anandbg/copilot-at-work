#!/usr/bin/env python3
"""Builds docs/index.html from template.html and data/features.json."""
import json, pathlib
root = pathlib.Path(__file__).parent
data = json.loads((root / "data/features.json").read_text())
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
html = (root / "template.html").read_text().replace("/*DATA*/null", blob)
(root / "docs").mkdir(exist_ok=True)
(root / "docs/index.html").write_text(html)
print("built", len(html), "bytes,", len(data["features"]), "features")
