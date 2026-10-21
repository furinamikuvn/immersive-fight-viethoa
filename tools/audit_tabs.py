import os, json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

viet_chars = re.compile(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]', re.IGNORECASE)
assets_dir = r'D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\resources\assets'

tab_names_vi = []
for ns in sorted(os.listdir(assets_dir)):
    p = os.path.join(assets_dir, ns, 'lang', 'vi_vn.json')
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
            for k, v in d.items():
                if ('item_group.' in k or 'itemgroup.' in k.lower() or 'creativetab.' in k.lower() or k.startswith('mod.') or k.endswith('.mod_name') or k.endswith('.tab')):
                    if viet_chars.search(v):
                        tab_names_vi.append((ns, k, v))

print(f'Total tab/mod name keys translated to Vietnamese: {len(tab_names_vi)}')
for ns, k, v in tab_names_vi:
    print(f'  [{ns}] {k}: "{v}"')
