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
tools_dir = os.path.join(base_dir, "tools")
extracted_dir = os.path.join(tools_dir, "master_extracted")
dict_path = os.path.join(tools_dir, "rp_translation_dict.json")

zh_path = os.path.join(extracted_dir, "unique_zh_needed.json")
en_path = os.path.join(extracted_dir, "unique_en_needed.json")

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
    if not text.strip():
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

                for pat, repl in RPG_GLOSSARY:
                    translated = re.sub(pat, repl, translated, flags=re.IGNORECASE)

                return text, translated
        except Exception:
            time.sleep(0.3)

    return text, text

def main():
    print("=== TAWA MULTI-THREADED TRANSLATION ENGINE ===")
    trans_dict = {}
    if os.path.exists(dict_path):
        try:
            with open(dict_path, 'r', encoding='utf-8') as f:
                trans_dict = json.load(f)
            print(f"Loaded existing translation dictionary with {len(trans_dict)} entries.")
        except Exception as e:
            print(f"Could not load existing dictionary: {e}")

    # Load unique needed strings
    with open(zh_path, 'r', encoding='utf-8') as f:
        zh_needed = json.load(f)

    with open(en_path, 'r', encoding='utf-8') as f:
        en_needed = json.load(f)

    pending_zh = [s for s in zh_needed if s not in trans_dict and s.strip()]
    pending_en = [s for s in en_needed if s not in trans_dict and s.strip()]

    print(f"Pending Chinese strings: {len(pending_zh)}")
    print(f"Pending English strings: {len(pending_en)}")
    total_pending = len(pending_zh) + len(pending_en)

    if total_pending == 0:
        print("All strings are already translated!")
        return

    # Translate Chinese strings
    if pending_zh:
        print(f"\n--- Translating {len(pending_zh)} Chinese strings ---")
        done = 0
        with ThreadPoolExecutor(max_workers=30) as executor:
            futures = {executor.submit(translate_single, s, 'zh-CN', 'vi'): s for s in pending_zh}
            for fut in as_completed(futures):
                src, tgt = fut.result()
                trans_dict[src] = tgt
                done += 1
                if done % 250 == 0 or done == len(pending_zh):
                    print(f"ZH -> VI: {done}/{len(pending_zh)} ({done/len(pending_zh)*100:.1f}%)")
                    with open(dict_path, 'w', encoding='utf-8') as f:
                        json.dump(trans_dict, f, ensure_ascii=False, indent=2)

    # Translate English strings
    if pending_en:
        print(f"\n--- Translating {len(pending_en)} English strings ---")
        done = 0
        with ThreadPoolExecutor(max_workers=30) as executor:
            futures = {executor.submit(translate_single, s, 'en', 'vi'): s for s in pending_en}
            for fut in as_completed(futures):
                src, tgt = fut.result()
                trans_dict[src] = tgt
                done += 1
                if done % 250 == 0 or done == len(pending_en):
                    print(f"EN -> VI: {done}/{len(pending_en)} ({done/len(pending_en)*100:.1f}%)")
                    with open(dict_path, 'w', encoding='utf-8') as f:
                        json.dump(trans_dict, f, ensure_ascii=False, indent=2)

    with open(dict_path, 'w', encoding='utf-8') as f:
        json.dump(trans_dict, f, ensure_ascii=False, indent=2)

    print(f"\nFinished translation! Total dictionary size: {len(trans_dict)} entries.")

if __name__ == '__main__':
    start_t = time.time()
    main()
    print(f"Execution took: {time.time() - start_t:.2f}s")
