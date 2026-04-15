import re, zipfile, xml.etree.ElementTree as ET
from pathlib import Path
pptx = Path(r"c:\Users\muchu\Downloads\Untitled presentation (8).pptx")
with zipfile.ZipFile(pptx, "r") as z:
    names = sorted(
        [n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)],
        key=lambda x: int(re.search(r"slide(\d+)", x).group(1)),
    )
    print(f"Found {len(names)} slides\n")
    for path in names:
        n = int(re.search(r"slide(\d+)", path).group(1))
        root = ET.fromstring(z.read(path))
        texts = []
        for t in root.iter("{http://schemas.openxmlformats.org/drawingml/2006/main}t"):
            if t.text:
                texts.append(t.text)
            if t.tail:
                texts.append(t.tail)
        blob = "".join(texts)
        blob = re.sub(r"\s+", " ", blob).strip()
        print(f"--- Slide {n} ---")
        print(blob[:5000])
        print()
