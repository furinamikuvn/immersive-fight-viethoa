import os
import sys
import zipfile
import json
import re
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
mods_dir = os.path.join(base_dir, "mods")
rp_assets = os.path.join(base_dir, "resourcepack", "IMF-VietHoa", "assets")
tools_dir = os.path.join(base_dir, "tools")

dict_path = os.path.join(tools_dir, "books_translation_dict.json")
books_dict = {}
if os.path.exists(dict_path):
    try:
        with open(dict_path, 'r', encoding='utf-8') as f:
            books_dict = json.load(f)
    except:
        pass

def translate_text(text, sl='zh-CN', tl='vi'):
    if not text.strip() or not re.search(r'[\u4e00-\u9fff]', text):
        return text

    if text in books_dict:
        return books_dict[text]

    # Protect tags like <NEWLINE>, $(...), §a, &a, %s, etc.
    placeholders = {}
    def repl_spec(m):
        idx = len(placeholders)
        key = f"XYZBPH{idx}XYZ"
        placeholders[key] = m.group(0)
        return key

    pattern = r'(?:<NEWLINE>|\$\([^)]*\)|§[0-9a-fk-or]|&[0-9a-fk-or]|%[0-9]*\$?[a-zA-Z]|(?:\{[0-9]+\}))'
    protected = re.sub(pattern, repl_spec, text)

    url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl={sl}&tl={tl}&q={urllib.parse.quote(protected)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=6) as r:
                res = json.loads(r.read().decode('utf-8'))
                translated = res[0]
                for k, orig in placeholders.items():
                    translated = translated.replace(k, orig)
                books_dict[text] = translated
                return translated
        except Exception:
            pass

    return text

print("=== TRANSLATING ALL IN-GAME GUIDEBOOKS ===")

# -------------------------------------------------------------
# 1. Simply Swords - Runic Grimoire (Patchouli)
# -------------------------------------------------------------
print("\n--- 1. Processing Simply Swords Patchouli Books ---")
swords_jar = os.path.join(mods_dir, "simplyswords-forge-1.56.0-1.20.1.jar")

# Load existing patchouli mapping
patchouli_script = os.path.join(tools_dir, "translate_patchouli_full.py")
swords_map = {}
if os.path.exists(patchouli_script):
    with open(patchouli_script, 'r', encoding='utf-8') as f:
        code = f.read()
        m = re.search(r'trans_map\s*=\s*(\{[\s\S]*?\n\})', code)
        if m:
            try:
                swords_map = eval(m.group(1))
                print(f"Loaded {len(swords_map)} translations for Simply Swords.")
            except:
                pass

with zipfile.ZipFile(swords_jar, 'r') as z:
    for n in z.namelist():
        if n.startswith('assets/simplyswords/patchouli_books/runic_grimoire/zh_cn/'):
            if n.endswith('/'):
                continue
            data_bytes = z.read(n)
            rel_path = n[len('assets/simplyswords/patchouli_books/runic_grimoire/zh_cn/'):]
            
            content = data_bytes.decode('utf-8', errors='ignore')
            for src, dst in swords_map.items():
                if src in content:
                    content = content.replace(src, dst)
            
            # Write to zh_cn, vi_vn, en_us in IMF-VietHoa
            for lang_tag in ('zh_cn', 'vi_vn', 'en_us'):
                out_p = os.path.join(rp_assets, 'simplyswords', 'patchouli_books', 'runic_grimoire', lang_tag, rel_path.replace('/', os.sep))
                os.makedirs(os.path.dirname(out_p), exist_ok=True)
                with open(out_p, 'w', encoding='utf-8') as fp:
                    fp.write(content)

print("Simply Swords Runic Grimoire patched into Resource Pack successfully!")

# -------------------------------------------------------------
# 2. Saint's Dragons - Codex
# -------------------------------------------------------------
print("\n--- 2. Processing Saint's Dragons Codex ---")
dragons_jar = os.path.join(mods_dir, "saintsdragons-0.9.5+forge-1.20.1.jar")

with zipfile.ZipFile(dragons_jar, 'r') as z:
    for n in z.namelist():
        if n.startswith('assets/saintsdragons/codex/zh_cn/ecology/') and n.endswith('.txt'):
            fname = os.path.basename(n)
            zh_text = z.read(n).decode('utf-8', errors='ignore')
            vi_text = translate_text(zh_text, 'zh-CN', 'vi')
            
            for lang_tag in ('zh_cn', 'vi_vn', 'en_us'):
                out_p = os.path.join(rp_assets, 'saintsdragons', 'codex', lang_tag, 'ecology', fname)
                os.makedirs(os.path.dirname(out_p), exist_ok=True)
                with open(out_p, 'w', encoding='utf-8') as fp:
                    fp.write(vi_text)
            print(f"Translated dragon codex: {fname}")

# -------------------------------------------------------------
# 3. Alex's Caves - Cave Book
# -------------------------------------------------------------
print("\n--- 3. Processing Alex's Caves Book ---")
caves_jar = os.path.join(mods_dir, "alexscaves-2.0.2.jar")

caves_files = []
with zipfile.ZipFile(caves_jar, 'r') as z:
    for n in z.namelist():
        if n.startswith('assets/alexscaves/books/zh_cn/') and n.endswith(('.txt', '.json')):
            caves_files.append((n, z.read(n).decode('utf-8', errors='ignore')))

print(f"Translating {len(caves_files)} Alex's Caves book files...")
def process_cave_file(item):
    n, text = item
    rel = n[len('assets/alexscaves/books/zh_cn/'):]
    vi_text = translate_text(text, 'zh-CN', 'vi')
    return rel, vi_text

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(process_cave_file, item) for item in caves_files]
    for fut in as_completed(futures):
        rel, vi_text = fut.result()
        for lang_tag in ('zh_cn', 'vi_vn', 'en_us'):
            out_p = os.path.join(rp_assets, 'alexscaves', 'books', lang_tag, rel.replace('/', os.sep))
            os.makedirs(os.path.dirname(out_p), exist_ok=True)
            with open(out_p, 'w', encoding='utf-8') as fp:
                fp.write(vi_text)

print("Alex's Caves books translated successfully!")

# -------------------------------------------------------------
# 4. Alex's Mobs - Animal Dictionary
# -------------------------------------------------------------
print("\n--- 4. Processing Alex's Mobs Animal Dictionary ---")
mobs_jar = os.path.join(mods_dir, "alexsmobs-1.22.9.jar")

mobs_files = []
with zipfile.ZipFile(mobs_jar, 'r') as z:
    for n in z.namelist():
        if n.startswith('assets/alexsmobs/book/animal_dictionary/zh_cn/') and n.endswith(('.txt', '.json')):
            mobs_files.append((n, z.read(n).decode('utf-8', errors='ignore')))

print(f"Translating {len(mobs_files)} Alex's Mobs dictionary files...")
def process_mobs_file(item):
    n, text = item
    rel = n[len('assets/alexsmobs/book/animal_dictionary/zh_cn/'):]
    vi_text = translate_text(text, 'zh-CN', 'vi')
    return rel, vi_text

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(process_mobs_file, item) for item in mobs_files]
    for fut in as_completed(futures):
        rel, vi_text = fut.result()
        for lang_tag in ('zh_cn', 'vi_vn', 'en_us'):
            out_p = os.path.join(rp_assets, 'alexsmobs', 'book', 'animal_dictionary', lang_tag, rel.replace('/', os.sep))
            os.makedirs(os.path.dirname(out_p), exist_ok=True)
            with open(out_p, 'w', encoding='utf-8') as fp:
                fp.write(vi_text)

print("Alex's Mobs Animal Dictionary translated successfully!")

# Save dictionary cache
with open(dict_path, 'w', encoding='utf-8') as f:
    json.dump(books_dict, f, ensure_ascii=False, indent=2)

print("\n=== ALL IN-GAME GUIDEBOOKS HAVE BEEN TRANSLATED AND INJECTED! ===")
