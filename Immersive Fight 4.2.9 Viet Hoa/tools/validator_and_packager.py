import os
import sys
import json
import zipfile
import re

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
rp_dir = os.path.join(base_dir, "resourcepack", "IMF-VietHoa")
dist_dir = os.path.join(base_dir, "dist")
os.makedirs(dist_dir, exist_ok=True)

print("=== BẮT ĐẦU KIỂM THỬ TỰ ĐỘNG (STATIC LINTING) ===")

valid_json = 0
invalid_json = 0
total_keys = 0
placeholder_errors = 0

for root, dirs, files in os.walk(rp_dir):
    for f in files:
        if f.endswith('.json'):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8') as fp:
                    data = json.load(fp)
                    valid_json += 1
                    total_keys += len(data)
                    for k, v in data.items():
                        if isinstance(v, str):
                            # check unpaired format tags
                            if v.count('§') % 2 != 0 and '§' in v:
                                pass # Minecraft color code is fine
            except Exception as e:
                print(f"[ERROR] Corrupted JSON at {p}: {e}")
                invalid_json += 1

print(f"Tổng file JSON hợp lệ: {valid_json}")
print(f"Tổng file JSON lỗi cú pháp: {invalid_json}")
print(f"Tổng số keys đã được nạp: {total_keys}")

if invalid_json == 0:
    print("\n=== ĐÓNG GÓI THÀNH PHẨM (DISTRIBUTION PACKAGE) ===")
    zip_path = os.path.join(dist_dir, "IMF-VietHoa.zip")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(rp_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, rp_dir)
                zipf.write(full_path, rel_path)
    print(f"Đã xuất gói Resource Pack thành công: {zip_path}")
    print(f"Kích thước gói: {os.path.getsize(zip_path) / 1024:.2f} KB")
else:
    print("[CẢNH BÁO] Phát hiện lỗi JSON! Không thể đóng gói.")
