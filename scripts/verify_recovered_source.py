#!/usr/bin/env python3
"""Verify the verbatim source snapshot against the recovery manifest."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "configs/recovered_source_manifest.json").read_text())
for record in manifest["files"]:
    path = root / "recovered-aeic" / record["path"]
    content = path.read_bytes()
    if len(content) != record["bytes"] or hashlib.sha256(content).hexdigest() != record["sha256"]:
        raise SystemExit(f"Recovered source checksum mismatch: {record['path']}")
print(f"Verified {len(manifest['files'])} recovered source files.")
