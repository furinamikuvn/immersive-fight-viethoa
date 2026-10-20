import os
import sys
import re

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

chinese_regex = re.compile(r'[\u4e00-\u9fff]+')

base_folder = r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh"
hotai_dir = os.path.join(base_folder, "hotai")

all_badiffs_chinese = {}

for root, dirs, files in os.walk(hotai_dir):
    for f in files:
        if f.endswith(".badiff"):
            p = os.path.join(root, f)
            with open(p, "rb") as fp:
                data = fp.read()
            text = data.decode("utf-8", errors="ignore")
            matches = chinese_regex.findall(text)
            # Filter matches with actual Chinese words (length >= 1)
            real_matches = [m for m in matches if any(ord(c) >= 0x4e00 and ord(c) <= 0x9fa5 for c in m)]
            if real_matches:
                rel = os.path.relpath(p, hotai_dir)
                all_badiffs_chinese[rel] = list(set(real_matches))

print(f"Tổng số file badiff còn chứa tiếng Trung: {len(all_badiffs_chinese)}")
for rel, strings in sorted(all_badiffs_chinese.items()):
    print(f"\n[{rel}]")
    for s in strings:
        print(f"  - '{s}'")
