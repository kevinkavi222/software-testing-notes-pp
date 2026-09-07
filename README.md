# Software testing course (HTML slides)

Static HTML slide decks and presenter notes for a software testing course. Open any `.html` file in a browser (double-click or “Open with Live Server”).

## Files

| File | Purpose |
|------|---------|
| `complete-software-testing-course-preview.html` | Learner-facing slide deck |
| `complete-software-testing-course-presenters-guide.html` | Same slides + presenter notes at the bottom |
| `software-testing-course-slides-instructor-template.html` | Instructor template variant |
| `complete-software-testing-student-programme-guide.html` | Student Programme Guide (print/PDF source) |
| `complete-software-testing-student-programme-guide.pdf` | Student Programme Guide PDF (8 pages) |
| `complete-software-testing-instructor-guide.html` | Instructor Guide (facilitation, labs, ISTQB, CV) |
| `complete-software-testing-instructor-guide.pdf` | Instructor Guide PDF |
| `assets/` | Images, icons, and diagrams referenced by the HTML |

Helper scripts (`_patch_layer_svg.py`, `_read_pptx8.py`, `_export_programme_guide_pdf.sh`, `_export_instructor_guide_pdf.sh`) are optional tooling for maintenance and PDF regeneration.

## Push this folder to a new GitHub repository

1. On [GitHub](https://github.com/new), create a **new repository** (any name, e.g. `software-testing-notes-pp`). Do **not** add a README or `.gitignore` there (this folder already has them).

2. In a terminal **in this folder**, run:

```bash
git remote add origin https://github.com/kevinkavi222/software-testing-notes-pp.git
git push -u origin main
```

Use SSH instead if you prefer: `git@github.com:kevinkavi222/software-testing-notes-pp.git`

## Clone and continue on another machine

```bash
git clone https://github.com/kevinkavi222/software-testing-notes-pp.git
cd software-testing-notes-pp
```

Then edit in Cursor, VS Code, or GitHub’s web editor; commit and push as usual.
