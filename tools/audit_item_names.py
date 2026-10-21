import os, json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

viet_chars = re.compile(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]', re.IGNORECASE)
assets_dir = r'D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\resources\assets'

desc_suffixes = (
    '_desc', '.desc', '_description', '.description',
    '_tooltip', '.tooltip', '_info', '.info', '_lore', '.lore',
    '_comment', '.comment', '_summary', '.summary',
    '.innate', '_innate', '.passive', '_passive', '.combo', '_combo',
    '.skill', '_skill', '.ability', '_ability', '.line', '_line',
    '.help', '_help', '.tip', '_tip'
)

name_keys_vi = []
for ns in sorted(os.listdir(assets_dir)):
    p = os.path.join(assets_dir, ns, 'lang', 'vi_vn.json')
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
            for k, v in d.items():
                if any(k.endswith(s) for s in desc_suffixes):
                    continue
                # item, block, entity names
                if k.startswith(('item.', 'block.', 'entity.')):
                    # Check if it has 3 parts or specific name format
                    parts = k.split('.')
                    if len(parts) == 3 or (len(parts) == 4 and parts[1] == 'minecraft'):
                        if viet_chars.search(v):
                            name_keys_vi.append((ns, k, v))

print(f'Total item/block/entity names still in Vietnamese: {len(name_keys_vi)}')
for ns, k, v in name_keys_vi[:50]:
    print(f'  [{ns}] {k}: "{v}"')
