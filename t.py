import os
import pathlib

dirs = [
    "docs/images",
    "docs/media",
    "cad/v1",
    "cad/v2",
    "cad/v3-final",
    "firmware",
]

files = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "docs/mechanism-overview.md",
    "docs/wiring-guide.md",
    "docs/fc-configuration.md",
    "docs/media/links.md",
    "firmware/radiomaster-config.md",
]

base = pathlib.Path(__file__).parent

for d in dirs:
    (base / d).mkdir(parents=True, exist_ok=True)

for f in files:
    p = base / f
    p.parent.mkdir(parents=True, exist_ok=True)
    p.touch()
