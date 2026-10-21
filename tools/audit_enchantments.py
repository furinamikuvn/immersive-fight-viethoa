import os, json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

viet_chars = re.compile(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]', re.IGNORECASE)
assets_dir = r'D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\resources\assets'

enchant_names_vi = []
for ns in sorted(os.listdir(assets_dir)):
    p = os.path.join(assets_dir, ns, 'lang', 'vi_vn.json')
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
            for k, v in d.items():
                if k.startswith('enchantment.') and not any(k.endswith(s) for s in ['.desc', '_desc', '.description', '_description', '.info', '_info']):
                    if viet_chars.search(v):
                        enchant_names_vi.append((k, v))

print(f'Total enchantment names translated to Vietnamese: {len(enchant_names_vi)}')
for k, v in enchant_names_vi:
    print(f'  {k}: "{v}"')
