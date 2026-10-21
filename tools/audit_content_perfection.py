import os, sys, json, re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

deployed_dir = Path(r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\resources\assets")

CHINESE_RE = re.compile(r'[\u4e00-\u9fff]')

print("=== PHA 3: KIỂM TOÁN NỘI DUNG MÔ TẢ & TIẾNG TRUNG/TIẾNG ANH ===")

total_keys = 0
chinese_keys = []
english_desc_keys = []

desc_markers = (
    '.tooltip', '.desc', '.description', '.lore', '.ability', '.info',
    'skill.', 'ability.', 'effect.', 'enchantment.',
    'potion.effect.', 'tipped_arrow.effect.'
)

for f in deployed_dir.rglob("vi_vn.json"):
    ns = f.parent.parent.name
    try:
        data = json.load(open(f, encoding='utf-8'))
        for k, v in data.items():
            if not isinstance(v, str): continue
            total_keys += 1
            
            # Kiểm tra tiếng Trung
            if CHINESE_RE.search(v):
                chinese_keys.append((ns, k, v))
                
            # Kiểm tra mô tả tiếng Anh
            kl = k.lower()
            if any(m in kl for m in desc_markers):
                # Bỏ qua đĩa nhạc
                if 'music_disc' in kl or 'disc.' in kl:
                    continue
                # Bỏ qua nếu có dấu tiếng Việt
                has_vn = any(ord(c) > 127 and c not in '§©®™°±×÷•…–—“”’‘' for c in v)
                words = [w for w in re.split(r'[^a-zA-Z]', v) if len(w) >= 2]
                if not has_vn and len(words) >= 3:
                    english_desc_keys.append((ns, k, v))
    except Exception as e:
        print(f"Lỗi đọc file {f}: {e}")

print(f"Tổng số keys đã kiểm toán trong vi_vn.json: {total_keys:,}")
print(f"Keys chứa tiếng Trung: {len(chinese_keys)}")
print(f"Keys mô tả còn thuần tiếng Anh: {len(english_desc_keys)}")

if chinese_keys:
    print("\n--- PHÁT HIỆN TIẾNG TRUNG ---")
    for ns, k, v in chinese_keys[:10]:
        print(f"[{ns}] {k} -> {v}")

if english_desc_keys:
    print("\n--- SAMPLE MÔ TẢ CÒN TIẾNG ANH ---")
    for ns, k, v in english_desc_keys[:20]:
        print(f"[{ns}] {k} -> {v}")
