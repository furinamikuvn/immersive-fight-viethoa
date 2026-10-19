import json
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

path = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\tools\rp_chinese_keys.json"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

unique_values = set(data.values())
print(f"Total keys with Chinese: {len(data)}")
print(f"Total UNIQUE Chinese values: {len(unique_values)}")

with open(r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\tools\rp_unique_strings.json", 'w', encoding='utf-8') as f:
    json.dump(sorted(list(unique_values)), f, ensure_ascii=False, indent=2)
