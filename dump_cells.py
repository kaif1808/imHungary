import json
nb = json.load(open('hungary_growth_accounting-2.ipynb'))
ids = ['VSC-8d8404b5','VSC-509816e9','VSC-7589a253','VSC-b6809645',
       'VSC-9c150669','VSC-d7a9fd71','VSC-2582c688','VSC-c45b6b36',
       'VSC-aa588704','VSC-7241507c','VSC-dc023796','VSC-1933730e',
       'VSC-1ae0108c','VSC-a7f4578a','VSC-3967c7ef']
for i, cell in enumerate(nb['cells']):
    if cell.get('id') in ids:
        print('--- cell', cell['id'], 'index', i, '---')
        for j, line in enumerate(cell['source']):
            print(' ', j, repr(line))
        print()
