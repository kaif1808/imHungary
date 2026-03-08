#!/usr/bin/env python3
"""
Regenerate year_tally_2f.tex, year_tally_3f.tex, sectoral_tally_2f.tex, sectoral_tally_3f.tex
from the full year_tally.tex and sectoral_tally.tex.

NOTE: backcast_labqi.ipynb now exports these subset tables directly with sector names and
print-ready column labels. This script is for backward compatibility when regenerating
from raw tables. For full labels, run scripts/apply_table_labels.py after the notebook.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TABLES = ROOT / "output" / "tables"


def parse_tabular(content: str) -> tuple[list[str], list[list[str]]]:
    """Extract header and data rows from a LaTeX tabular."""
    lines = content.strip().split("\n")
    header = None
    rows = []
    in_table = False
    for line in lines:
        if "\\toprule" in line:
            in_table = True
            continue
        if "\\midrule" in line:
            continue
        if "\\bottomrule" in line or "\\end{tabular}" in line:
            break
        if in_table and "&" in line:
            cells = [c.strip().rstrip("\\") for c in line.split("&")]
            if header is None:
                header = cells
            else:
                rows.append(cells)
    return header or [], rows


def write_tabular(header: list[str], rows: list[list[str]], col_indices: list[int], path: Path) -> None:
    """Write a subset tabular to path."""
    sub_header = [header[i] for i in col_indices]
    sub_rows = [[r[i] for i in col_indices] for r in rows]
    ncols = len(col_indices)
    col_spec = "l" + "r" * (ncols - 1) if sub_header[0] in ("nace_r2_code", "nace\\_r2\\_code") else "r" * ncols
    lines = [
        "",
        "\\begin{tabular}{" + col_spec + "}",
        "\\toprule",
        " & ".join(sub_header) + "\\\\",
        "\\midrule",
    ]
    for i, row in enumerate(sub_rows):
        lines.append(" & ".join(row) + "\\\\")
        if (i + 1) % 5 == 0 and i + 1 < len(sub_rows):
            lines.append("\\addlinespace")
    lines.extend(["\\bottomrule", "\\end{tabular}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    TABLES.mkdir(parents=True, exist_ok=True)

    # year_tally: year, g_y, cap, hc, tfp, cap_2f, tfp_2f
    year_path = TABLES / "year_tally.tex"
    if year_path.exists():
        content = year_path.read_text(encoding="utf-8")
        header, rows = parse_tabular(content)
        if header and rows:
            # Normalize header (year_tally uses g_y, cap_2f, tfp_2f)
            write_tabular(header, rows, [0, 1, 5, 6], TABLES / "year_tally_2f.tex")
            write_tabular(header, rows, [0, 1, 2, 3, 4], TABLES / "year_tally_3f.tex")
            print("Generated year_tally_2f.tex, year_tally_3f.tex")
        else:
            print("Could not parse year_tally.tex")
    else:
        print("year_tally.tex not found, skipping")

    # sectoral_tally: nace_r2_code, lp_growth, cap, hc, tfp, cap_2f, tfp_2f
    sector_path = TABLES / "sectoral_tally.tex"
    if sector_path.exists():
        content = sector_path.read_text(encoding="utf-8")
        header, rows = parse_tabular(content)
        if header and rows:
            write_tabular(header, rows, [0, 1, 5, 6], TABLES / "sectoral_tally_2f.tex")
            write_tabular(header, rows, [0, 1, 2, 3, 4], TABLES / "sectoral_tally_3f.tex")
            print("Generated sectoral_tally_2f.tex, sectoral_tally_3f.tex")
        else:
            print("Could not parse sectoral_tally.tex")
    else:
        print("sectoral_tally.tex not found, skipping")


if __name__ == "__main__":
    main()
