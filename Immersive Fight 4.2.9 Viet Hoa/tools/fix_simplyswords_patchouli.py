import os
import sys
import zipfile
import json
import re
import urllib.request
import urllib.parse

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
swords_jar = os.path.join(base_dir, "mods", "simplyswords-forge-1.56.0-1.20.1.jar")
rp_assets = os.path.join(base_dir, "resourcepack", "IMF-VietHoa", "assets")
tools_dir = os.path.join(base_dir, "tools")

# Load existing patchouli mapping
patchouli_script = os.path.join(tools_dir, "translate_patchouli_full.py")
swords_map = {}
with open(patchouli_script, 'r', encoding='utf-8') as f:
    code = f.read()
    m = re.search(r'trans_map\s*=\s*(\{[\s\S]*?\n\})', code)
    swords_map = eval(m.group(1))

re_ch = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]')

def translate_api(text):
    if not text.strip() or not re_ch.search(text):
        return text
    placeholders = {}
    def repl_spec(m):
        idx = len(placeholders)
        key = f"XYZPPH{idx}XYZ"
        placeholders[key] = m.group(0)
        return key
    pattern = r'(?:<NEWLINE>|\$\([^)]*\)|§[0-9a-fk-or]|&[0-9a-fk-or]|%[0-9]*\$?[a-zA-Z]|(?:\{[0-9]+\}))'
    protected = re.sub(pattern, repl_spec, text)
    url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=zh-CN&tl=vi&q={urllib.parse.quote(protected)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            res = json.loads(r.read().decode('utf-8'))
            t = res[0]
            for k, orig in placeholders.items():
                t = t.replace(k, orig)
            return t
    except Exception as e:
        print(f"API Error translating {text}: {e}")
        return text

def translate_value(val):
    if isinstance(val, str):
        if not re_ch.search(val):
            return val
        if val in swords_map and not re_ch.search(swords_map[val]):
            return swords_map[val]
        # Otherwise translate
        trans = translate_api(val)
        swords_map[val] = trans
        return trans
    elif isinstance(val, list):
        return [translate_value(item) for item in val]
    elif isinstance(val, dict):
        return {k: translate_value(v) for k, v in val.items()}
    return val

print("=== FIXING SIMPLY SWORDS PATCHOULI BOOKS ===")

total_patched = 0
with zipfile.ZipFile(swords_jar, 'r') as z:
    for n in z.namelist():
        if n.startswith('assets/simplyswords/patchouli_books/runic_grimoire/zh_cn/') and n.endswith('.json'):
            rel_p = n[len('assets/simplyswords/patchouli_books/runic_grimoire/zh_cn/'):]
            raw_data = json.loads(z.read(n).decode('utf-8'))
            
            translated_data = translate_value(raw_data)
            
            # Write to zh_cn, vi_vn, en_us
            for lang_tag in ('zh_cn', 'vi_vn', 'en_us'):
                target_p = os.path.join(rp_assets, 'simplyswords', 'patchouli_books', 'runic_grimoire', lang_tag, rel_p.replace('/', os.sep))
                os.makedirs(os.path.dirname(target_p), exist_ok=True)
                with open(target_p, 'w', encoding='utf-8') as fp:
                    json.dump(translated_data, fp, ensure_ascii=False, indent=2)
            total_patched += 1

print(f"Patched and saved {total_patched} Patchouli JSON files across zh_cn, vi_vn, en_us!")

# Verify no Chinese remains
remaining_ch = 0
for root, dirs, files in os.walk(os.path.join(rp_assets, 'simplyswords', 'patchouli_books')):
    for f in files:
        if f.endswith('.json'):
            with open(os.path.join(root, f), 'r', encoding='utf-8') as fp:
                content = fp.read()
                m = re_ch.findall(content)
                if m:
                    print(f"Warning: {f} still has {len(m)} Chinese chars!")
                    remaining_ch += len(m)

print(f"Verification: {remaining_ch} Chinese characters remaining in Simply Swords Patchouli!")
