import json
nb = json.load(open('hungary_growth_accounting-2.ipynb'))

for cell in nb['cells']:
    cid = cell.get('id')

    # c88a446a: heatmap
    if cid == 'c88a446a':
        src = ''.join(cell['source'])
        src = src.replace(
            'decomp_sect |>\n  filter(!is.na(g_y)) |>\n',
            'decomp_sect |>\n  filter(!is.na(g_y), year <= 2011) |>\n'
        )
        src = src.replace(
            'title = "Hungary \u2014 Annual TFP+HC Residual by Sector (1996\u20132021)",',
            'title = "Hungary \u2014 Annual TFP+HC Residual by Sector (1996\u20132011)",'
        )
        cell['source'] = list(src.splitlines(keepends=True))
        print('patched c88a446a')

    # 1c92e1e1: policy events
    if cid == '1c92e1e1':
        src = ''.join(cell['source'])
        src = src.replace(
            'decomp_agg |>\n  filter(!is.na(g_y)) |>\n',
            'decomp_agg |>\n  filter(!is.na(g_y), year <= 2011) |>\n'
        )
        src = src.replace(
            'title = "Hungary \u2014 LP Growth Decomposition with Key Policy Events",',
            'title = "Hungary \u2014 LP Growth Decomposition with Key Policy Events (1995\u20132011)",'
        )
        cell['source'] = list(src.splitlines(keepends=True))
        print('patched 1c92e1e1')

json.dump(nb, open('hungary_growth_accounting-2.ipynb', 'w'), ensure_ascii=False, indent=1)
print('done')
