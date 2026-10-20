import zipfile
import json
import sys
import re

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

rp = r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh\resourcepacks\IMF-VietHoa.zip"

print("=== QUÉT SÂU CÁC CHUỖI VIỆT HÓA BỊ LỖI HOẶC DỊCH LỎ ===")

bad_keywords = [
    "chống nhật",
    "đêm mùa thu",
    "được phù phép",
    "áo giáp tưởng tượng",
    "vật phẩm thức tỉnh",
    "trận chiến hoành tráng",
    "tiểu sử của",
    "con rối",
    "thanh kiếm đơn giản",
    "vũ khí thần thoại",
    "quái vật huyền thoại",
    "cá voi"
]

found = []
with zipfile.ZipFile(rp, "r") as zf:
    for n in zf.namelist():
        if n.endswith("vi_vn.json"):
            try:
                data = json.loads(zf.read(n).decode("utf-8"))
                for k, v in data.items():
                    s = str(v).lower()
                    for b in bad_keywords:
                        if b in s:
                            found.append((n, k, str(v), b))
            except:
                pass

print(f"Tổng số chuỗi nghi vấn tìm thấy: {len(found)}")
for n, k, v, b in found:
    print(f"  [{b.upper()}] {n} -> {k} = \"{v}\"")
