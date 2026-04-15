# AGENTS.md

## Cursor Cloud specific instructions

This is a static HTML slide deck repository with no build system, no package manager, and no automated tests. See `README.md` for the file layout.

### Serving the slides locally

Run `python3 -m http.server 8080 --directory /workspace` and open any `.html` file in a browser at `http://localhost:8080/`. All three slide decks are self-contained HTML/CSS/JS — no bundler or framework is involved.

### Helper scripts

`_patch_layer_svg.py` and `_read_pptx8.py` are optional maintenance utilities. They use only Python stdlib modules (`re`, `pathlib`, `zipfile`, `xml.etree.ElementTree`). Note: both scripts contain hardcoded Windows paths that must be edited before running on Linux.

### Lint / Test / Build

There is no linter, test suite, or build step configured for this repository.
