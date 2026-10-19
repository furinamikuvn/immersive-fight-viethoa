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
rp_dir = os.path.join(base_dir, "resourcepack", "IMF-VietHoa", "assets")
dist_dir = os.path.join(base_dir, "dist")
dict_path = os.path.join(base_dir, "tools", "rp_translation_dict.json")
strings_path = os.path.join(base_dir, "tools", "rp_unique_strings.json")

# Termbase replacements for high-quality Dark Fantasy tone
RPG_GLOSSARY = [
    (r"\bTác động\b", "Lực xung kích"),
    (r"\bđánh rơi\b", "rơi ra"),
    (r"\bChế tạo\s*洞穴概论\b", "Chế tạo Cave Book (Tổng Quan Hang Động)"),
    (r"\b洞穴概论\b", "Cave Book"),
    (r"\b耐力\b", "Thể lực"),
    (r"\b冷却时间\b", "Thời gian hồi chiêu"),
    (r"\b生命值\b", "Sinh lực"),
    (r"\b护甲穿透\b", "Xuyên giáp"),
    (r"\b暴击率\b", "Tỷ lệ chí mạng"),
    (r"\b暴击伤害\b", "Sát thương chí mạng")
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

def run_rp_translation():
    trans_dict = {}
    if os.path.exists(dict_path):
        try:
            with open(dict_path, 'r', encoding='utf-8') as fp:
                trans_dict = json.load(fp)
        except Exception:
            pass

    with open(strings_path, 'r', encoding='utf-8') as fp:
        all_strings = json.load(fp)

    pending = [s for s in all_strings if s not in trans_dict]
    print(f"Tổng số chuỗi Resource Pack: {len(all_strings)}. Cần dịch mới: {len(pending)}")

    if pending:
        completed = len(trans_dict)
        with ThreadPoolExecutor(max_workers=25) as executor:
            futures = {executor.submit(translate_single, s): s for s in pending}
            for fut in as_completed(futures):
                src, tgt = fut.result()
                trans_dict[src] = tgt
                completed += 1
                if completed % 200 == 0 or completed == len(all_strings):
                    print(f"Tiến độ Resource Pack: {completed}/{len(all_strings)} ({(completed/len(all_strings)*100):.1f}%)")
                    with open(dict_path, 'w', encoding='utf-8') as fp:
                        json.dump(trans_dict, fp, ensure_ascii=False, indent=2)

        with open(dict_path, 'w', encoding='utf-8') as fp:
            json.dump(trans_dict, fp, ensure_ascii=False, indent=2)

    print("Áp dụng bản dịch vào toàn bộ tệp vi_vn.json trong resourcepack...")
    updated_files = 0
    total_replaced = 0

    for root, dirs, files in os.walk(rp_dir):
        for f in files:
            if f == "vi_vn.json":
                p = os.path.join(root, f)
                try:
                    with open(p, 'r', encoding='utf-8') as fp:
                        data = json.load(fp)
                    
                    changed = False
                    for k, v in data.items():
                        if isinstance(v, str) and v in trans_dict and trans_dict[v] != v:
                            data[k] = trans_dict[v]
                            changed = True
                            total_replaced += 1
                            
                    if changed:
                        with open(p, 'w', encoding='utf-8') as fp:
                            json.dump(data, fp, ensure_ascii=False, indent=2)
                        updated_files += 1
                except Exception as e:
                    print(f"Lỗi khi cập nhật {p}: {e}")

    print(f"Đã cập nhật {total_replaced} keys trên {updated_files} tệp vi_vn.json!")
    
    # Run packager
    print("Bắt đầu kiểm thử và đóng gói tự động...")
    os.system(f'python "{os.path.join(base_dir, "tools", "validator_and_packager.py")}"')

if __name__ == "__main__":
    start = time.time()
    run_rp_translation()
    print(f"Hoàn thành toàn bộ quy trình Resource Pack trong {time.time() - start:.2f} giây")
