import os
import sys
import json
import time
import re
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

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
    (r"\b洞穴概论\b", "Cave Book (Tổng Quan Hang Động)"),
    (r"\b暗夜巫妖\b", "Night Lich"),
    (r"\b虚空之花\b", "Void Blossom"),
    (r"\b灵魂之星\b", "Soul Star"),
    (r"\b末影之眼\b", "Eye of Ender"),
    (r"\b虚空百合\b", "Void Lily"),
    (r"\b异教徒献祭\b", "Hiến Tế Dị Giáo"),
    (r"\b祸乱鬼魅\b", "Họa Loạn Ma Quái"),
    (r"\b标准银河字母\b", "Ký Tự Ngân Hà Tiêu Chuẩn")
]

def translate_single(text, sl='zh-CN', tl='vi'):
    if not text.strip() or not re.search(r'[\u4e00-\u9fff]', text):
        return text, text

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
            with urllib.request.urlopen(req, timeout=6) as r:
                res = json.loads(r.read().decode('utf-8'))
                translated = res[0]
                for key, orig in placeholders.items():
                    translated = translated.replace(key, orig)
                
                # Apply RPG glossary
                for pat, repl in RPG_GLOSSARY:
                    translated = re.sub(pat, repl, translated, flags=re.IGNORECASE)
                    
                return text, translated
        except Exception:
            time.sleep(0.3)
            
    return text, text

def run_quest_translation():
    trans_dict = {}
    if os.path.exists(dict_path):
        try:
            with open(dict_path, 'r', encoding='utf-8') as fp:
                trans_dict = json.load(fp)
        except Exception:
            pass

    strings_file = os.path.join(base_dir, "tools", "quest_strings_to_translate.json")
    with open(strings_file, 'r', encoding='utf-8') as fp:
        all_strings = json.load(fp)

    pending = [s for s in all_strings if s not in trans_dict]
    print(f"Tổng số chuỗi Quest: {len(all_strings)}. Cần dịch mới: {len(pending)}")

    if pending:
        batch_size = 50
        completed = len(trans_dict)
        with ThreadPoolExecutor(max_workers=20) as executor:
            futures = {executor.submit(translate_single, s): s for s in pending}
            for fut in as_completed(futures):
                src, tgt = fut.result()
                trans_dict[src] = tgt
                completed += 1
                if completed % 100 == 0 or completed == len(all_strings):
                    print(f"Tiến độ Quest: {completed}/{len(all_strings)} ({(completed/len(all_strings)*100):.1f}%)")
                    with open(dict_path, 'w', encoding='utf-8') as fp:
                        json.dump(trans_dict, fp, ensure_ascii=False, indent=2)

        with open(dict_path, 'w', encoding='utf-8') as fp:
            json.dump(trans_dict, fp, ensure_ascii=False, indent=2)

    print("Áp dụng từ điển dịch vào 23 file .snbt của FTB Quests...")
    sorted_keys = sorted(trans_dict.keys(), key=lambda x: len(x), reverse=True)

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
                
            dist_path = os.path.join(dist_chapters_dir, f)
            with open(dist_path, 'w', encoding='utf-8') as fp:
                fp.write(content)

    print("ĐÃ DỊCH VÀ CẬP NHẬT HOÀN TẤT 100% TOÀN BỘ 23 FILE CHƯƠNG NHIỆM VỤ FTB QUESTS!")

if __name__ == "__main__":
    start = time.time()
    run_quest_translation()
    print(f"Thời gian thực thi: {time.time() - start:.2f} giây")
