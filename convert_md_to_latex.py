#!/usr/bin/env python3
"""
Convert Hungary_Growth_Accounting.md to LaTeX.
Extracts base64 figures, converts tables, and produces a compilable .tex file.
"""

import re
import base64
from pathlib import Path


def escape_latex(s: str, escape_dollar: bool = True) -> str:
    """Escape LaTeX special characters in plain text (e.g. table cells)."""
    s = s.replace("\\", "\\textbackslash{}")
    s = s.replace("&", "\\&")
    s = s.replace("%", "\\%")
    s = s.replace("#", "\\#")
    s = s.replace("_", "\\_")
    if escape_dollar:
        s = s.replace("$", "\\$")
    s = s.replace("{", "\\{")
    s = s.replace("}", "\\}")
    s = s.replace("~", "\\textasciitilde{}")
    s = s.replace("^", "\\textasciicircum{}")
    return s


def normalize_unicode(s: str) -> str:
    """Replace Unicode chars that break pdflatex."""
    s = s.replace("\u2009", " ")   # thin space
    s = s.replace("\u202f", " ")   # narrow no-break space
    s = s.replace("\u00a0", " ")   # non-breaking space
    s = s.replace("\u2248", r"$\approx$")  # ≈
    s = s.replace("αₛ", r"$\alpha_s$")  # alpha subscript s
    s = s.replace("α", r"$\alpha$")  # Greek alpha (standalone)
    s = s.replace("\u209b", "_s")  # subscript s (ₛ) standalone
    s = s.replace("\u2090", "_a")  # subscript a
    s = s.replace("\u1d62", "_i")  # subscript i
    s = s.replace("\u2099", "_n")  # subscript n
    return s


def escape_latex_plain(s: str) -> str:
    """Escape LaTeX special chars except backslash (for body text with existing commands)."""
    s = s.replace("&", "\\&")
    s = s.replace("%", "\\%")
    s = s.replace("#", "\\#")
    s = s.replace("_", "\\_")
    s = s.replace("$", "\\$")
    return s


def convert_unicode_math(text: str) -> str:
    """Convert Unicode math symbols to LaTeX."""
    replacements = [
        ("gᵧ", r"$g_y$"),
        ("gᵏ", r"$g_k$"),
        ("gʰ", r"$g_h$"),
        ("gₐ", r"$g_A$"),
        ("α", r"$\alpha$"),
        ("·", r"$\cdot$"),
        ("−", "-"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def convert_inline_formatting(text: str) -> str:
    """Convert *italic* and **bold** to LaTeX, escaping content."""
    def repl_bold(m):
        return "\\textbf{" + escape_latex(m.group(1)) + "}"
    def repl_italic(m):
        content = m.group(1)
        # If it's an equation (contains = and math symbols), output as math only
        if "=" in content and any(c in content for c in ["α", "gᵧ", "gᵏ", "gʰ", "gₐ", "$"]):
            eq = content.replace("gᵧ", "g_y").replace("gᵏ/y", "g_{k/y}").replace("gᵏ", "g_k").replace("gʰ", "g_h").replace("gₐ", "g_A")
            eq = eq.replace("α", "\\alpha").replace("·", "\\cdot").replace("−", "-")
            if "\\alpha/(1-\\alpha)" in eq:
                eq = eq.replace("\\alpha/(1-\\alpha)", "\\frac{\\alpha}{1-\\alpha}")
            return f"${eq}$"
        return "\\textit{" + escape_latex(content) + "}"
    text = re.sub(r"\*\*(.+?)\*\*", repl_bold, text)
    text = re.sub(r"\*([^*]+?)\*", repl_italic, text)
    return text


def parse_markdown_table(lines: list[str], start: int) -> tuple[str, int]:
    """Parse a markdown table starting at line start. Returns (latex_tabular, next_line)."""
    rows = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|"):
        row = lines[i].strip()
        if re.search(r"^\|[\s\-:|]+\|$", row):
            i += 1
            continue  # separator row
        cells = [c.strip() for c in row.split("|")[1:-1]]
        if cells:
            rows.append(cells)
        i += 1

    if not rows:
        return "", start

    ncols = len(rows[0])
    align = ["l"] * ncols
    for r in rows[1:]:
        for j, c in enumerate(r):
            if j < len(align) and re.match(r"^-?[\d.]+$", c.strip().replace("−", "-")):
                align[j] = "r"

    colspec = "".join(align)
    latex = ["\\begin{tabular}{" + colspec + "}\n\\toprule\n"]
    for idx, row in enumerate(rows):
        def escape_cell(c):
            c = normalize_unicode(c).replace("−", "-")
            # Preserve $...$ math, escape the rest
            parts = re.split(r"(\$[^$]+\$)", c)
            out_parts = []
            for p in parts:
                if p.startswith("$") and p.endswith("$"):
                    out_parts.append(p)
                else:
                    out_parts.append(escape_latex(p))
            return "".join(out_parts)
        escaped = [escape_cell(c) for c in row]
        latex.append(" & ".join(escaped) + " \\\\\n")
        if idx == 0:
            latex.append("\\midrule\n")
    latex.append("\\bottomrule\n\\end{tabular}")
    return "\n".join(latex), i


def extract_base64_images(content: str) -> list[tuple[str, str]]:
    """Extract (alt_text, base64_data) from ![](data:image/...;base64,...)"""
    pattern = r"!\[(.*?)\]\((data:image/[^;]+;base64,([A-Za-z0-9+/=]+))\)"
    matches = re.findall(pattern, content)
    return [(alt, b64) for alt, full, b64 in matches]


def process_body_text(text: str) -> str:
    """Convert body text: formatting, math, escaping."""
    text = normalize_unicode(text)
    text = convert_inline_formatting(text)  # first: handles *equation* -> $...$
    # Only run convert_unicode_math on parts outside $...$ (avoid double-wrapping)
    parts = re.split(r"(\$[^$]+\$)", text)
    result = []
    for p in parts:
        if p.startswith("$") and p.endswith("$"):
            result.append(p)
        else:
            result.append(convert_unicode_math(p))
    text = "".join(result)
    # Escape remaining special chars in non-math parts (preserve \commands)
    parts = re.split(r"(\$[^$]+\$|\\[a-zA-Z]+\{[^}]*\})", text)
    result = []
    for p in parts:
        if (p.startswith("$") and p.endswith("$")) or (p.startswith("\\") and "{" in p):
            result.append(p)
        else:
            result.append(escape_latex_plain(p))
    return "".join(result)


def main():
    project_root = Path(__file__).resolve().parent
    md_path = project_root / "Hungary_Growth_Accounting.md"
    tex_path = project_root / "Hungary_Growth_Accounting.tex"
    figures_dir = project_root / "output" / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    content = md_path.read_text(encoding="utf-8")
    lines = content.split("\n")

    # Extract base64 images and save
    images = extract_base64_images(content)
    fig_paths = []
    for i, (alt, b64) in enumerate(images):
        fname = f"hungary_ga_fig{i+1:02d}.png"
        out_path = figures_dir / fname
        out_path.write_bytes(base64.b64decode(b64))
        fig_paths.append(f"output/figures/{fname}")
        print(f"Extracted {fname}")

    # Replace base64 blocks with placeholder for parsing
    def repl_img(m):
        return "\n<<<FIGURE>>>\n"
    content_no_img = re.sub(r"!\[.*?\]\(data:image/[^)]+\)", repl_img, content)
    # Join lines that end with \ (line continuation)
    content_no_img = re.sub(r"\\\s*\n\s*", " ", content_no_img)
    lines = content_no_img.split("\n")

    # Build LaTeX output
    out = []
    out.append(r"\documentclass[11pt]{article}")
    out.append(r"\usepackage[utf8]{inputenc}")
    out.append(r"\usepackage[T1]{fontenc}")
    out.append(r"\usepackage{geometry, booktabs, graphicx, amsmath, hyperref}")
    out.append(r"\geometry{margin=1in}")
    out.append(r"\title{Hungary Growth Accounting}")
    out.append(r"\author{}")
    out.append(r"\date{}")
    out.append(r"\begin{document}")
    out.append(r"\maketitle")
    out.append("")

    fig_idx = 0
    pending_caption = None
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Standalone "Figure N" that precedes a figure - save as pending caption
        if re.match(r"^Figure \d+$", stripped):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].strip() == "<<<FIGURE>>>":
                pending_caption = stripped
                i += 1
                continue

        # Figure placeholder
        if stripped == "<<<FIGURE>>>":
            if fig_idx < len(fig_paths):
                caption = pending_caption or "Figure " + str(fig_idx + 1)
                if pending_caption is None and i + 1 < len(lines) and lines[i + 1].strip().startswith("Figure"):
                    caption = lines[i + 1].strip()
                    i += 1
                pending_caption = None
                out.append("\\begin{figure}[htbp]")
                out.append("  \\centering")
                out.append(f"  \\includegraphics[width=\\linewidth]{{{fig_paths[fig_idx]}}}")
                out.append(f"  \\caption{{{escape_latex(caption)}}}")
                out.append(f"  \\label{{fig:{fig_idx+1}}}")
                out.append("\\end{figure}")
                out.append("")
                fig_idx += 1
            i += 1
            continue

        # Main section: # **(a) Title**
        m = re.match(r"^# \*\*\([a-g]\) (.+)\*\*$", stripped)
        if m:
            title = escape_latex(normalize_unicode(m.group(1)))
            out.append(f"\\section{{{title}}}")
            out.append("")
            i += 1
            continue

        # Subsection: ## **Title**
        m = re.match(r"^## \*\*(.+)\*\*$", stripped)
        if m and "<<<FIGURE>>>" not in line and "data:image" not in line:
            title = escape_latex(normalize_unicode(m.group(1)))
            out.append(f"\\subsection{{{title}}}")
            out.append("")
            i += 1
            continue

        # Table
        if stripped.startswith("|") and "---" in stripped:
            tab_latex, i = parse_markdown_table(lines, i - 1)
            if tab_latex:
                out.append(tab_latex)
                out.append("")
            continue

        if stripped.startswith("|") and i > 0 and not lines[i - 1].strip().startswith("|"):
            tab_latex, i = parse_markdown_table(lines, i)
            if tab_latex:
                out.append(tab_latex)
                out.append("")
            continue

        # Skip image-only "headers" (## with base64 - already replaced)
        if stripped.startswith("##") and len(stripped) < 20:
            i += 1
            continue

        # Body paragraph
        if stripped:
            processed = process_body_text(stripped)
            out.append(processed)
            out.append("")
        elif out and out[-1] != "":
            out.append("")

        i += 1

    out.append("\\end{document}")
    tex_content = "\n".join(out)
    # Fix malformed equation (nested $ from convert_unicode_math)
    tex_content = tex_content.replace(
        "$g_y = $\\alpha$/(1-$\\alpha$) \\cdot g_{k/y} + g_h + g_a$",
        "$g_y = \\frac{\\alpha}{1-\\alpha} \\cdot g_{k/y} + g_h + g_A$"
    )
    tex_path.write_text(tex_content, encoding="utf-8")
    print(f"Wrote {tex_path}")


if __name__ == "__main__":
    main()
