"""
Patch notebook: restrict time period to 1995-2011.
Works on the actual list-of-strings source format.
"""
import json, copy

NB = 'hungary_growth_accounting-2.ipynb'

def patch(source, replacements):
    """Apply (old_line, new_line) replacements to a list-of-strings source."""
    src = ''.join(source)
    for old, new in replacements:
        if old not in src:
            raise ValueError(f'Pattern not found: {repr(old[:80])}')
        src = src.replace(old, new, 1)
    return list(src.splitlines(keepends=True))

# cell_id -> list of (old, new) pairs
PATCHES = {

    # ── bff430ae: agg line chart ──────────────────────────────────────────────
    'bff430ae': [
        (
            '  filter(!is.na(g_y)) |>\n',
            '  filter(!is.na(g_y), year <= 2011) |>\n'
        ),
        (
            '    title = "Hungary \u2014 Aggregate Output & Labour Productivity Growth",\n',
            '    title = "Hungary \u2014 Aggregate Output & Labour Productivity Growth (1995\u20132011)",\n'
        ),
    ],

    # ── 448a7909: total vs market index ──────────────────────────────────────
    '448a7909': [
        (
            '  mutate(index = y_per_hour / y_per_hour[year == 1995] * 100) |>\n',
            '  filter(year <= 2011) |>\n  mutate(index = y_per_hour / y_per_hour[year == 1995] * 100) |>\n'
        ),
        (
            '    title = "Hungary \u2014 Output per Hour: Total vs Market Economy (1995 = 100)",\n',
            '    title = "Hungary \u2014 Output per Hour: Total vs Market Economy (1995\u20132011, 1995 = 100)",\n'
        ),
    ],

    # ── 7779f8e7: decomp_agg_plot + stacked bar ───────────────────────────────
    '7779f8e7': [
        (
            '# Stacked bar decomposition (2009\u20132021 where all components are available)\n'
            'decomp_agg_plot <- decomp_agg |>\n'
            '  filter(!is.na(tfp_contrib))\n',
            '# Stacked bar decomposition (2009\u20132011 where all components are available)\n'
            'decomp_agg_plot <- decomp_agg |>\n'
            '  filter(!is.na(tfp_contrib), year <= 2011)\n'
        ),
        (
            '    title = "Hungary \u2014 LP Growth Decomposition (\u03b1 = 1/3, 2009\u20132021)",\n',
            '    title = "Hungary \u2014 LP Growth Decomposition (\u03b1 = 1/3, 2009\u20132011)",\n'
        ),
    ],

    # ── 9e714a28: cumulative decomposition ────────────────────────────────────
    '9e714a28': [
        (
            '    title = "Hungary \u2014 Cumulative LP Growth Decomposition (\u03b1 = 1/3)",\n',
            '    title = "Hungary \u2014 Cumulative LP Growth Decomposition (\u03b1 = 1/3, 2009\u20132011)",\n'
        ),
    ],

    # ── 77b92e3c: two-factor decomp ───────────────────────────────────────────
    '77b92e3c': [
        (
            '# Alternative: two-factor decomposition (capital + TFP residual) for full period 1996\u20132021\n'
            'decomp_agg_2f <- decomp_agg |>\n'
            '  filter(!is.na(g_y)) |>\n',
            '# Alternative: two-factor decomposition (capital + TFP residual) for 1996\u20132011\n'
            'decomp_agg_2f <- decomp_agg |>\n'
            '  filter(!is.na(g_y), year <= 2011) |>\n'
        ),
        (
            '    title = "Hungary \u2014 LP Growth: Two-Factor Decomposition (\u03b1 = 1/3, 1996\u20132021)",\n',
            '    title = "Hungary \u2014 LP Growth: Two-Factor Decomposition (\u03b1 = 1/3, 1996\u20132011)",\n'
        ),
    ],

    # ── 4b8b9f71: decomp_sect + sect_avg_3f ──────────────────────────────────
    '4b8b9f71': [
        (
            '# Average annual contributions per sector (full three-factor: 2009\u20132021)\n'
            'sect_avg_3f <- decomp_sect |>\n'
            '  filter(!is.na(tfp_contrib)) |>\n',
            '# Average annual contributions per sector (three-factor: 2009\u20132011)\n'
            'sect_avg_3f <- decomp_sect |>\n'
            '  filter(!is.na(tfp_contrib), year <= 2011) |>\n'
        ),
    ],

    # ── 5b94b289: sectoral stacked bar ───────────────────────────────────────
    '5b94b289': [
        (
            '# Bar chart: average LP growth by sector (three-factor, 2009\u20132021)\n',
            '# Bar chart: average LP growth by sector (three-factor, 2009\u20132011)\n'
        ),
        (
            '    title = "Hungary \u2014 Avg Annual LP Growth Decomposition by Sector (2009\u20132021)",\n',
            '    title = "Hungary \u2014 Avg Annual LP Growth Decomposition by Sector (2009\u20132011)",\n'
        ),
    ],

    # ── aa0a34eb: sect_avg_2f ─────────────────────────────────────────────────
    'aa0a34eb': [
        (
            'sect_avg_2f <- decomp_sect |>\n'
            '  filter(!is.na(g_y)) |>\n',
            'sect_avg_2f <- decomp_sect |>\n'
            '  filter(!is.na(g_y), year <= 2011) |>\n'
        ),
        (
            'cat("=== Highest LP growth (1996\u20132021 average) ===\\n")\n',
            'cat("=== Highest LP growth (1996\u20132011 average) ===\\n")\n'
        ),
    ],

    # ── f9de6631: three-factor rankings ──────────────────────────────────────
    'f9de6631': [
        (
            '# Three-factor rankings (2009\u20132021 only, where LAB_QI is available)\n',
            '# Three-factor rankings (2009\u20132011 only, where LAB_QI is available)\n'
        ),
        (
            'cat("=== Highest TFP growth (2009\u20132021) ===\\n")\n',
            'cat("=== Highest TFP growth (2009\u20132011) ===\\n")\n'
        ),
        (
            'cat("\\n=== Lowest TFP growth (2009\u20132021) ===\\n")\n',
            'cat("\\n=== Lowest TFP growth (2009\u20132011) ===\\n")\n'
        ),
    ],

    # ── deea0976: decomp_sect_alpha + sect_avg_alpha ──────────────────────────
    'deea0976': [
        (
            'sect_avg_alpha <- decomp_sect_alpha |>\n'
            '  filter(!is.na(tfp_contrib_s)) |>\n',
            'sect_avg_alpha <- decomp_sect_alpha |>\n'
            '  filter(!is.na(tfp_contrib_s), year <= 2011) |>\n'
        ),
    ],

    # ── ace6d869: α comparison bar ────────────────────────────────────────────
    'ace6d869': [
        (
            '# Compare TFP: \u03b1 = 1/3 vs sector-specific \u03b1 (both over 2009\u20132021)\n',
            '# Compare TFP: \u03b1 = 1/3 vs sector-specific \u03b1 (both over 2009\u20132011)\n'
        ),
        (
            '    title = "Hungary \u2014 TFP Contribution: \u03b1 = 1/3 vs Sector-Specific \u03b1 (2009\u20132021)",\n',
            '    title = "Hungary \u2014 TFP Contribution: \u03b1 = 1/3 vs Sector-Specific \u03b1 (2009\u20132011)",\n'
        ),
    ],

    # ── b317de41: Tornqvist aggregation + comparison ──────────────────────────
    'b317de41': [
        (
            'comparison <- decomp_agg |>\n'
            '  filter(!is.na(g_y)) |>\n',
            'comparison <- decomp_agg |>\n'
            '  filter(!is.na(g_y), year <= 2011) |>\n'
        ),
    ],

    # ── d4777a65: reported vs sectoral LP plot ────────────────────────────────
    'd4777a65': [
        (
            '    title = "Hungary \u2014 Reported vs Sector-Aggregated LP Growth",\n',
            '    title = "Hungary \u2014 Reported vs Sector-Aggregated LP Growth (1995\u20132011)",\n'
        ),
    ],

    # ── 1c92e1e1: heatmap ─────────────────────────────────────────────────────
    '1c92e1e1': [
        (
            'decomp_sect |>\n'
            '  filter(!is.na(g_y)) |>\n',
            'decomp_sect |>\n'
            '  filter(!is.na(g_y), year <= 2011) |>\n'
        ),
        (
            '    title = "Hungary \u2014 Annual TFP+HC Residual by Sector (1996\u20132021)",\n',
            '    title = "Hungary \u2014 Annual TFP+HC Residual by Sector (1996\u20132011)",\n'
        ),
    ],

    # ── c88a446a: policy-events time-series ───────────────────────────────────
    'c88a446a': [
        (
            'decomp_agg |>\n'
            '  filter(!is.na(g_y)) |>\n',
            'decomp_agg |>\n'
            '  filter(!is.na(g_y), year <= 2011) |>\n'
        ),
        (
            '    title = "Hungary \u2014 LP Growth Decomposition with Key Policy Events",\n',
            '    title = "Hungary \u2014 LP Growth Decomposition with Key Policy Events (1995\u20132011)",\n'
        ),
    ],
}

nb = json.load(open(NB))
ok, failed = 0, []
for cell in nb['cells']:
    cid = cell.get('id')
    if cid in PATCHES:
        try:
            cell['source'] = patch(cell['source'], PATCHES[cid])
            print(f'  OK  {cid}')
            ok += 1
        except ValueError as e:
            print(f'  FAIL {cid}: {e}')
            failed.append(cid)

json.dump(nb, open(NB, 'w'), ensure_ascii=False, indent=1)
print(f'\n{ok} cells patched, {len(failed)} failed: {failed}')
