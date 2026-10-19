import os
import sys
import json
import time
import re
import urllib.request
import urllib.parse

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
chapters_dir = os.path.join(base_dir, "ftbquests", "chapters")
dist_chapters_dir = os.path.join(base_dir, "dist", "quests", "chapters")
os.makedirs(dist_chapters_dir, exist_ok=True)
dict_path = os.path.join(base_dir, "tools", "quest_translation_dict.json")

# Termbase replacements for high-quality Dark Fantasy tone
RPG_GLOSSARY = [
    (r"\bTác động\b", "Lực xung kích"),
    (r"\bđánh rơi\b", "rơi ra"),
    (r"\bChế tạo\s*洞穴概论\b", "Chế tạo Cave Book (Tổng Quan Hang Động)"),
    (r"\b洞穴概论\b", "Cave Book"),
    (r"\b暗夜巫妖\b", "Night Lich"),
    (r"\b虚空之花\b", "Void Blossom"),
    (r"\b灵魂之星\b", "Soul Star"),
    (r"\b末影之眼\b", "Eye of Ender"),
    (r"\b虚空百合\b", "Void Lily"),
]

def translate_single(text, sl='zh-CN', tl='vi'):
    if not text.strip() or not re.search(r'[\u4e00-\u9fff]', text):
        return text

    placeholders = {}
    def repl_spec(m):
        idx = len(placeholders)
        key = f"XYZPH{idx}XYZ"
        placeholders[key] = m.group(0)
        return key
        
    pattern = r'(?:§[0-9a-fk-or]|&[0-9a-fk-or]|%[0-9]*\$?[a-zA-Z]|(?:\{[0-9]+\})|\\n|\\")'
    protected = re.sub(pattern, repl_spec, text)
    
    url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl={sl}&tl={tl}&q={urllib.parse.quote(protected)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=7) as r:
                res = json.loads(r.read().decode('utf-8'))
                translated = res[0]
                for key, orig in placeholders.items():
                    translated = translated.replace(key, orig)
                
                # Apply RPG glossary
                for pat, repl in RPG_GLOSSARY:
                    translated = re.sub(pat, repl, translated, flags=re.IGNORECASE)
                    
                return translated
        except Exception as e:
            time.sleep(0.5)
            
    return text

# Load existing dictionary if available
trans_dict = {}
if os.path.exists(dict_path):
    try:
        with open(dict_path, 'r', encoding='utf-8') as fp:
            trans_dict = json.load(fp)
    except Exception:
        pass

# Load strings to translate
strings_file = os.path.join(base_dir, "tools", "quest_strings_to_translate.json")
with open(strings_file, 'r', encoding='utf-8') as fp:
    all_strings = json.load(fp)

total = len(all_strings)
print(f"Bắt đầu dịch {total} chuỗi FTB Quests...")
translated_count = 0

for i, s in enumerate(all_strings):
    if s not in trans_dict:
        res = translate_single(s)
        trans_dict[s] = res
        translated_count += 1
        time.sleep(0.04)
        if translated_count % 100 == 0:
            print(f"Đã dịch {i+1}/{total} chuỗi ({(i+1)/total*100:.1f}%)...")
            # Save checkpoint
            with open(dict_path, 'w', encoding='utf-8') as fp:
                json.dump(trans_dict, fp, ensure_ascii=False, indent=2)

# Final save
with open(dict_path, 'w', encoding='utf-8') as fp:
    json.dump(trans_dict, fp, ensure_ascii=False, indent=2)

print("Đã hoàn tất toàn bộ từ điển Quest. Đang áp dụng vào 23 file .snbt...")

# Apply dictionary to all 23 files
# Sort keys by length descending to prevent partial prefix replacement
sorted_keys = sorted(trans_dict.keys(), key=lambda x: len(x), reverse=True)

modified_files = 0
for f in os.listdir(chapters_dir):
    if f.endswith('.snbt'):
        src_path = os.path.join(chapters_dir, f)
        with open(src_path, 'r', encoding='utf-8') as fp:
            content = fp.read()
            
        for k in sorted_keys:
            if k in content and k != trans_dict[k]:
                content = content.replace(f'"{k}"', f'"{trans_dict[k]}"')
                
        with open(src_path, 'w', encoding='utf-8') as fp:
            fp.write(content)
            
        # Copy to dist
        dist_path = os.path.join(dist_chapters_dir, f)
        with open(dist_path, 'w', encoding='utf-8') as fp:
            fp.write(content)
            
        modified_files += 1

print(f"Đã cập nhật thành công {modified_files} file FTB Quests sang Tiếng Việt!")
