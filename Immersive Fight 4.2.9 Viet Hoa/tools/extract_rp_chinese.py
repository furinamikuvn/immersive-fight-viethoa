import os
import sys
import re
import json

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

rp_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\resourcepack\IMF-VietHoa\assets"
chinese_keys = {}

for root, dirs, files in os.walk(rp_dir):
    for f in files:
        if f == "vi_vn.json":
            p = os.path.join(root, f)
            rel_mod = os.path.relpath(p, rp_dir).split(os.sep)[0]
            with open(p, 'r', encoding='utf-8') as fp:
                try:
                    data = json.load(fp)
                    for k, v in data.items():
                        if isinstance(v, str) and re.search(r'[\u4e00-\u9fff]', v):
                            chinese_keys[f"{rel_mod}::{k}"] = v
                except Exception:
                    pass

print(f"Total remaining Chinese key-values in resourcepack vi_vn.json: {len(chinese_keys)}")
out_path = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\tools\rp_chinese_keys.json"
with open(out_path, 'w', encoding='utf-8') as fp:
    json.dump(chinese_keys, fp, ensure_ascii=False, indent=2)

print(f"Saved to {out_path}")
