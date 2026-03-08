#!/usr/bin/env python3
"""
Apply sector names and print-ready column labels to output tables.
Run after backcast_labqi.ipynb to update tables for LaTeX. The notebook
now exports with these labels; this script can regenerate from raw tables
if needed.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TABLES = ROOT / "output" / "tables"

SECTOR_NAMES = {
    "A": "A – Agriculture",
    "B": "B – Mining \\& quarrying",
    "C": "C – Manufacturing",
    "D-E": "D-E – Utilities",
    "F": "F – Construction",
    "G": "G – Wholesale \\& retail trade",
    "H": "H – Transport \\& storage",
    "I": "I – Accommodation \\& food",
    "J": "J – ICT",
    "K": "K – Finance \\& insurance",
    "L": "L – Real estate",
    "M-N": "M-N – Professional services",
    "O-Q": "O-Q – Public admin, education, health",
    "R-S": "R-S – Arts \\& other services",
}


def parse_tabular(path: Path) -> tuple[list[str], list[list[str]]]:
    """Parse LaTeX tabular into header and rows."""
    content = path.read_text(encoding="utf-8")
    lines = content.strip().split("\n")
    header, rows = None, []
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


def write_tabular(header: list[str], rows: list[list[str]], path: Path, addlinespace_every: int = 5) -> None:
    """Write tabular to path."""
    ncols = len(header)
    col_spec = "l" + "r" * (ncols - 1) if any("Sector" in h or "–" in h for h in header) else "r" * ncols
    lines = ["", "\\begin{tabular}{" + col_spec + "}", "\\toprule", " & ".join(header) + "\\\\", "\\midrule"]
    for i, row in enumerate(rows):
        lines.append(" & ".join(row) + "\\\\")
        if (i + 1) % addlinespace_every == 0 and i + 1 < len(rows):
            lines.append("\\addlinespace")
    lines.extend(["\\bottomrule", "\\end{tabular}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    TABLES.mkdir(parents=True, exist_ok=True)

    # Year tally (handle both raw and LaTeX-escaped header names)
    year_path = TABLES / "year_tally.tex"
    if year_path.exists():
        header, rows = parse_tabular(year_path)
        if header and rows:
            h_map = {"year": "Year", "g_y": "LP Growth (pp)", "cap": "Cap. Deepening (pp)", "hc": "HC (LAB\\_QI) (pp)",
                     "tfp": "TFP (pp)", "cap_2f": "Capital Deepening (pp)", "tfp_2f": "TFP + HC Residual (pp)"}
            new_h = [h_map.get(h.replace("\\_", "_"), h) for h in header]
            write_tabular(new_h, rows, year_path)
            write_tabular([new_h[0], new_h[1], new_h[5], new_h[6]], [[r[0], r[1], r[5], r[6]] for r in rows], TABLES / "year_tally_2f.tex")
            write_tabular([new_h[0], new_h[1], new_h[2], new_h[3], new_h[4]], [[r[0], r[1], r[2], r[3], r[4]] for r in rows], TABLES / "year_tally_3f.tex")
            print("Updated year_tally, year_tally_2f, year_tally_3f")

    # Sectoral tally
    sect_path = TABLES / "sectoral_tally.tex"
    if sect_path.exists():
        header, rows = parse_tabular(sect_path)
        if header and rows:
            code_idx = header.index("nace_r2_code") if "nace_r2_code" in header else 0
            new_rows = [[SECTOR_NAMES.get(r[code_idx], r[code_idx])] + r[1:] for r in rows]
            new_h = ["Sector", "LP Growth (pp)", "Cap. Deepening (pp)", "HC (pp)", "TFP (pp)", "Capital Deepening (pp)", "TFP + HC Residual (pp)"]
            write_tabular(new_h, new_rows, sect_path)
            write_tabular([new_h[0], new_h[1], new_h[5], new_h[6]], [[r[0], r[1], r[5], r[6]] for r in new_rows], TABLES / "sectoral_tally_2f.tex")
            write_tabular([new_h[0], new_h[1], new_h[2], new_h[3], new_h[4]], [[r[0], r[1], r[2], r[3], r[4]] for r in new_rows], TABLES / "sectoral_tally_3f.tex")
            print("Updated sectoral_tally, sectoral_tally_2f, sectoral_tally_3f")

    # Lab share
    lab_path = TABLES / "lab_share_alpha.tex"
    if lab_path.exists():
        header, rows = parse_tabular(lab_path)
        if header and rows:
            code_idx = header.index("nace_r2_code") if "nace_r2_code" in header else 0
            new_rows = [[SECTOR_NAMES.get(r[code_idx], r[code_idx]), r[1], r[2]] for r in rows]
            new_h = ["Sector", "Labour Share (1-$\\alpha_s$)", "Implied $\\alpha_s$"]
            write_tabular(new_h, new_rows, lab_path)
            print("Updated lab_share_alpha")

    # TFP compare
    tfp_path = TABLES / "tfp_compare.tex"
    if tfp_path.exists():
        header, rows = parse_tabular(tfp_path)
        if header and rows:
            code_idx = header.index("nace_r2_code") if "nace_r2_code" in header else 0
            tfp_13_idx = header.index("tfp_alpha_13") if "tfp_alpha_13" in header else 1
            tfp_s_idx = header.index("tfp_alpha_s") if "tfp_alpha_s" in header else 3
            delta_idx = header.index("delta_tfp") if "delta_tfp" in header else 5
            new_rows = [[SECTOR_NAMES.get(r[code_idx], r[code_idx]), r[tfp_13_idx], r[tfp_s_idx], r[delta_idx]] for r in rows]
            new_h = ["Sector", "TFP ($\\alpha$=1/3)", "TFP (sector $\\alpha_s$)", "Difference (pp)"]
            write_tabular(new_h, new_rows, tfp_path)
            print("Updated tfp_compare")


if __name__ == "__main__":
    main()
