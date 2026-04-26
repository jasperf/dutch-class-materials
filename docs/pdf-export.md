# Exporting Markdown to PDF

This repo uses [Pandoc](https://pandoc.org/) + [LuaLaTeX](https://www.luatex.org/) to convert lesson plans and schedules to print-ready PDFs.

> **DOCX vs PDF:** Converting to `.docx` requires only plain Pandoc — no LuaLaTeX needed.
> LuaLaTeX is required only for PDF output, because it handles Unicode characters and
> system fonts during rendering. Word and Google Docs handle that themselves.
> See `handouts/docx/README.md` for DOCX conversion commands.

---

## Prerequisites

### 1. Homebrew

Install Homebrew if not already present:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Pandoc

```bash
brew install pandoc
```

Verify:

```bash
pandoc --version
```

### 3. LuaLaTeX (via BasicTeX)

BasicTeX is a lightweight TeX distribution (~100 MB) that includes LuaLaTeX:

```bash
brew install --cask basictex
```

After installing, reload your shell so `/Library/TeX/texbin` is on your `PATH`:

```bash
eval "$(/usr/libexec/path_helper)"
```

Verify:

```bash
lualatex --version
```

---

## Generating a PDF

```bash
pandoc lessons/2026-Q2_Apr-Jun/schedule.md \
  -o lessons/2026-Q2_Apr-Jun/schedule.pdf \
  --pdf-engine=lualatex \
  -V mainfont="Arial Unicode MS" \
  -V geometry:margin=2cm \
  -V fontsize=11pt
```

| Flag | Purpose |
|------|---------|
| `--pdf-engine=lualatex` | Uses LuaLaTeX (supports Unicode and system fonts) |
| `-V mainfont="Arial Unicode MS"` | System font with broad Unicode coverage |
| `-V geometry:margin=2cm` | Page margins |
| `-V fontsize=11pt` | Base font size |

### Convert any lesson plan

```bash
pandoc lessons/2026-Q2_Apr-Jun/week-01/lesson-plan.md \
  -o lessons/2026-Q2_Apr-Jun/week-01/lesson-plan.pdf \
  --pdf-engine=lualatex \
  -V mainfont="Arial Unicode MS" \
  -V geometry:margin=2cm \
  -V fontsize=11pt
```

### Batch convert all lesson plans

```bash
for f in lessons/2026-Q2_Apr-Jun/week-*/lesson-plan.md; do
  pandoc "$f" \
    -o "${f%.md}.pdf" \
    --pdf-engine=lualatex \
    -V mainfont="Arial Unicode MS" \
    -V geometry:margin=2cm \
    -V fontsize=11pt
done
```

---

## Fonts

`Arial Unicode MS` ships with macOS and Microsoft Office and covers Dutch special characters without issue. Alternative system fonts that work well:

| Font | Notes |
|------|-------|
| `Helvetica Neue` | Clean sans-serif, macOS built-in |
| `Georgia` | Readable serif, macOS built-in |
| `Gill Sans` | macOS built-in, good for print |

List all available system fonts:

```bash
fc-list | sort
```

---

## Troubleshooting

**`lualatex: command not found`**
Reload your shell after installing BasicTeX, or add TeX to your PATH manually:
```bash
export PATH="/Library/TeX/texbin:$PATH"
```

**`Font … not found`**
Run `fc-list | grep -i "arial"` to confirm the font name, or swap for `Helvetica Neue`.

**Missing LaTeX packages**
BasicTeX is minimal. Install extra packages with `tlmgr`:
```bash
sudo tlmgr update --self
sudo tlmgr install <package-name>
```
