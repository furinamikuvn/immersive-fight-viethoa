import zipfile
import json
import sys
import os

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

rp_path = r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh\resourcepacks\IMF-VietHoa.zip"

print(f"=== KIỂM TOÁN TABS VÀ CÁC CHUỖI DỊCH THÔ ===")

tabs = {}
cringe_candidates = {}

with zipfile.ZipFile(rp_path, 'r') as zf:
    for n in zf.namelist():
        if n.endswith('vi_vn.json'):
            try:
                data = json.loads(zf.read(n).decode('utf-8'))
                for k, v in data.items():
                    val = str(v)
                    kl = k.lower()
                    if 'itemgroup' in kl or 'creativetab' in kl:
                        tabs[f"{n} -> {k}"] = val
                    
                    # Scan for suspicious machine translation patterns
                    suspicious = [
                        'trận chiến hoành tráng',
                        'tưởng tượng',
                        'chống nhật',
                        'mùa thu',
                        'chiến tranh',
                        'được phù phép',
                        'xâm lược đêm',
                        'sách được phù phép'
                    ]
                    for s in suspicious:
                        if s in val.lower():
                            cringe_candidates[f"{n} -> {k}"] = val
            except Exception as e:
                pass

print(f"\n--- DANH SÁCH CREATIVE TABS ({len(tabs)}) ---")
for k, v in sorted(tabs.items()):
    print(f"{k}: \"{v}\"")

print(f"\n--- DANH SÁCH CHUỖI DỊCH LỎ / NGHI VẤN ({len(cringe_candidates)}) ---")
for k, v in sorted(cringe_candidates.items()):
    print(f"{k}: \"{v}\"")
