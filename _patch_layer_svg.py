import re
from pathlib import Path

ROOT = Path(r"c:\Users\muchu\Software Testing Notes PP")
embed = (ROOT / "_layer_diagram_embed.svg").read_text(encoding="utf-8").strip()
# Indent SVG lines for HTML (12 spaces to match slide wrap)
indented = "\n".join("            " + line for line in embed.splitlines())

def patch(path: Path) -> None:
    t = path.read_text(encoding="utf-8")
    if "\r\n" in t:
        t = t.replace("\r\n", "\n")
    # Capture only through newline after <div>; strip old indent before <svg> so we do not double-indent
    pat = r'(<div class="waterfall-svg-wrap belief-slide__layers-wrap">\n)\s*<svg class="waterfall-svg belief-slide__layers-svg belief-slide__layers-svg--hero"[\s\S]*?</svg>'
    new_t, n = re.subn(pat, r"\1" + indented + "\n          ", t, count=1)
    if n != 1:
        raise SystemExit(f"{path}: expected 1 match, got {n}")
    path.write_text(new_t, encoding="utf-8")
    print("OK", path)

patch(ROOT / "complete-software-testing-course-preview.html")
