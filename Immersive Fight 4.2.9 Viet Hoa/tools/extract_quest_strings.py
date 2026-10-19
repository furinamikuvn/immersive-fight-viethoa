import os
import sys
import re
import json

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

chapters_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\ftbquests\chapters"
chinese_strings = set()
file_stats = {}

for f in os.listdir(chapters_dir):
    if f.endswith('.snbt'):
        path = os.path.join(chapters_dir, f)
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.read()
            matches = re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', content)
            matched_chinese = [m for m in matches if re.search(r'[\u4e00-\u9fff]', m)]
            file_stats[f] = len(matched_chinese)
            for m in matched_chinese:
                chinese_strings.add(m)

print(f"Total unique Chinese strings found across 23 chapters: {len(chinese_strings)}")
print("Top 5 chapters with most strings:")
for f, count in sorted(file_stats.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"  {f}: {count} strings")

out_path = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\tools\quest_strings_to_translate.json"
with open(out_path, 'w', encoding='utf-8') as fp:
    json.dump(sorted(list(chinese_strings)), fp, ensure_ascii=False, indent=2)

print(f"Saved to {out_path}")
