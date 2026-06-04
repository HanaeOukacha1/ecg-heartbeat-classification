import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\hanae\Desktop\projet ia\notebooka20fc60088.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb['cells']
print(f"Nombre de cellules : {len(cells)}\n")

for i, cell in enumerate(cells):
    src = ''.join(cell['source'])
    ctype = cell['cell_type'].upper()
    preview = src[:200].replace('\n', ' ')
    # Get outputs if any
    outputs = cell.get('outputs', [])
    out_text = ''
    for o in outputs:
        if 'text' in o:
            out_text = ''.join(o['text'])[:300]
        elif 'data' in o and 'text/plain' in o['data']:
            out_text = ''.join(o['data']['text/plain'])[:300]
    print(f"[{i+1}] {ctype}")
    print(f"    CODE: {preview[:180]}")
    if out_text:
        print(f"    OUT : {out_text[:200].replace(chr(10),' ')}")
    print()
