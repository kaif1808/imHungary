"""
Apply 1995-2011 time-period filter to all relevant cells.
Each entry: (cell_id, list_of_(old_line, new_line) tuples)
"""
import json, copy

NB = 'hungary_growth_accounting-2.ipynb'

# ------------------------------------------------------------------
# Helper: apply a list of (old, new) line replacements to a cell
# ------------------------------------------------------------------
def patch_source(source, replacements):
    src = ''.join(source)
    for old, new in replacements:
        if old not in src:
            print(f'  WARNING: pattern not found: {repr(old[:60])}')
        src = src.replace(old, new, 1)
    return list(line + ('' if line.endswith('\n') else '') for line in src.splitlines(keepends=True))

# ------------------------------------------------------------------
# Patches: (cell_id, [(old_text, new_text), ...])
# ------------------------------------------------------------------
patches = {

    # ── cell 3 (bff430ae) ─ agg plot (LP growth chart) ──────────────
    'bff430ae': [
        (
            '  filter(!is.na(g_y)) |>\n',
            '  filter(!is.na(g_y), year <= 2011) |>\n'
        ),
        (
            'title = "Hungary \u2014 Aggregate Output & Labour Productivity Growth",\n',
            'title = "Hungary \u2014 Aggregate Output & Labour Productivity Growth (1995\u20132011)",\n'
        ),
    ],

    # ── cell 5 (448a7909) ─ total vs market economy index ────────────
    '448a7909': [
        (
            '  mutate(index = y_per_hour / y_per_hour[year == 1995] * 100) |>\n',
            '  filter(year <= 2011) |>\n  mutate(index = y_per_hour / y_per_hour[year == 1995] * 100) |>\n'
        ),
        (
            'title = "Hungary \u2014 Output per Hour: Total vs Market Economy (1995 = 100)",\n',
            'title = "Hungary \u2014 Output per Hour: Total vs Market Economy (1995\u20132011, 1995 = 100)",\n'
        ),
    ],

    # ── cell 7 (327cdd04) ─ decomp_agg + stacked bar (3-factor) ──────
    '327cdd04': [
        (
            '    title = "Hungary \u2014 LP Growth Decomposition (\u03b1 = 1/3, 2009\u20132021)",\n',
            '    title = "Hungary \u2014 LP Growth Decomposition (\u03b1 = 1/3, 2009\u20132011)",\n'
        ),
        # decomp_agg_plot filter
        (
            'decomp_agg_plot <- decomp_agg |>\n  filter(!is.na(tfp_contrib))\n',
            'decomp_agg_plot <- decomp_agg |>\n  filter(!is.na(tfp_contrib), year <= 2011)\n'
        ),
    ],

    # ── cell 9 (7779f8e7) ─ cumulative decomposition ─────────────────
    '7779f8e7': [
        (
            'title = "Hungary \u2014 Cumulative LP Growth Decomposition (\u03b1 = 1/3)",\n',
            'title = "Hungary \u2014 Cumulative LP Growth Decomposition (\u03b1 = 1/3, 2009\u20132011)",\n'
        ),
    ],

    # ── cell 11 (9e714a28) ─ two-factor decomp ───────────────────────
    '9e714a28': [
        (
            'decomp_agg_2f <- decomp_agg |>\n  filter(!is.na(g_y)) |>\n',
            'decomp_agg_2f <- decomp_agg |>\n  filter(!is.na(g_y), year <= 2011) |>\n'
        ),
        (
            'title = "Hungary \u2014 LP Growth: Two-Factor Decomposition (\u03b1 = 1/3, 1996\u20132021)",\n',
            'title = "Hungary \u2014 LP Growth: Two-Factor Decomposition (\u03b1 = 1/3, 1996\u20132011)",\n'
        ),
    ],

    # ── cell 13 (77b92e3c) ─ sectoral decomp (decomp_sect) ───────────
    # sect_avg_3f filter (LAB_QI only 2008-2011 in new window → keep as-is,
    # just restrict the 2f average to ≤2011)
    '77b92e3c': [
        (
            '# Average annual contributions per sector (full three-factor: 2009\u20132021)\nsect_avg_3f <- decomp_sect |>\n  filter(!is.na(tfp_contrib)) |>\n',
            '# Average annual contributions per sector (three-factor: 2009\u20132011)\nsect_avg_3f <- decomp_sect |>\n  filter(!is.na(tfp_contrib), year <= 2011) |>\n'
        ),
    ],

    # ── cell 15 (4b8b9f71) ─ sectoral bar chart ──────────────────────
    '4b8b9f71': [
        (
            'title = "Hungary \u2014 Avg Annual LP Growth Decomposition by Sector (2009\u20132021)",\n',
            'title = "Hungary \u2014 Avg Annual LP Growth Decomposition by Sector (2009\u20132011)",\n'
        ),
    ],

    # ── cell 17 (5b94b289) ─ sect_avg_2f rankings ────────────────────
    '5b94b289': [
        (
            'sect_avg_2f <- decomp_sect |>\n  filter(!is.na(g_y)) |>\n',
            'sect_avg_2f <- decomp_sect |>\n  filter(!is.na(g_y), year <= 2011) |>\n'
        ),
        (
            'cat("=== Highest LP growth (1996\u20132021 average) ===\\n")\n',
            'cat("=== Highest LP growth (1996\u20132011 average) ===\\n")\n'
        ),
    ],

    # ── cell 19 (aa0a34eb) ─ three-factor rankings ───────────────────
    '19': [],   # placeholder; actual id below

    # ── cell 21 (f9de6631) ─ sector-specific alpha decomp ────────────
    'f9de6631': [
        (
            'sect_avg_alpha <- decomp_sect_alpha |>\n  filter(!is.na(tfp_contrib_s)) |>\n',
            'sect_avg_alpha <- decomp_sect_alpha |>\n  filter(!is.na(tfp_contrib_s), year <= 2011) |>\n'
        ),
    ],

    # ── cell 23 (2c4ca067) ─ α comparison bar chart ──────────────────
    '2c4ca067': [
        (
            'title = "Hungary \u2014 TFP Contribution: \u03b1 = 1/3 vs Sector-Specific \u03b1 (2009\u20132021)",\n',
            'title = "Hungary \u2014 TFP Contribution: \u03b1 = 1/3 vs Sector-Specific \u03b1 (2009\u20132011)",\n'
        ),
    ],

    # ── cell 25 (deea0976) ─ Tornqvist aggregation ───────────────────
    'deea0976': [
        (
            'comparison <- decomp_agg |>\n  filter(!is.na(g_y)) |>\n',
            'comparison <- decomp_agg |>\n  filter(!is.na(g_y), year <= 2011) |>\n'
        ),
    ],

    # ── cell 27 (ace6d869) ─ reported vs sectoral LP plot ────────────
    'ace6d869': [
        (
            'title = "Hungary \u2014 Reported vs Sector-Aggregated LP Growth",\n',
            'title = "Hungary \u2014 Reported vs Sector-Aggregated LP Growth (1995\u20132011)",\n'
        ),
    ],

    # ── cell 29 (b317de41) ─ heatmap ─────────────────────────────────
    'b317de41': [
        (
            'decomp_sect |>\n  filter(!is.na(g_y)) |>\n',
            'decomp_sect |>\n  filter(!is.na(g_y), year <= 2011) |>\n'
        ),
        (
            'title = "Hungary \u2014 Annual TFP+HC Residual by Sector (1996\u20132021)",\n',
            'title = "Hungary \u2014 Annual TFP+HC Residual by Sector (1996\u20132011)",\n'
        ),
    ],

    # ── cell 31 (d4777a65) ─ policy-events time-series ───────────────
    'd4777a65': [
        (
            'decomp_agg |>\n  filter(!is.na(g_y)) |>\n',
            'decomp_agg |>\n  filter(!is.na(g_y), year <= 2011) |>\n'
        ),
        (
            'title = "Hungary \u2014 LP Growth Decomposition with Key Policy Events",\n',
            'title = "Hungary \u2014 LP Growth Decomposition with Key Policy Events (1995\u20132011)",\n'
        ),
    ],
}

# Remove the placeholder
del patches['19']

# ------------------------------------------------------------------
# Apply patches
# ------------------------------------------------------------------
nb = json.load(open(NB))
changed = 0
for cell in nb['cells']:
    cid = cell.get('id')
    if cid in patches and patches[cid]:
        print(f'Patching cell {cid}')
        cell['source'] = patch_source(cell['source'], patches[cid])
        changed += 1

json.dump(nb, open(NB, 'w'), ensure_ascii=False, indent=1)
print(f'\nDone. {changed} cells patched.')
