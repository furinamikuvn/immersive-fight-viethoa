import os
import sys
import zipfile
import time

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

src_folder = r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh"
zip_out = r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Viet Hoa (Forge 1.20.1).zip"

print(f"=== ĐÓNG GÓI ZIP PHÁT HÀNH ===")
print(f"Nguồn: {src_folder}")
print(f"Đích:  {zip_out}\n")

start_t = time.time()
with zipfile.ZipFile(zip_out, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=1) as z:
    for root, dirs, files in os.walk(src_folder):
        for f in files:
            full_p = os.path.join(root, f)
            rel_p = os.path.relpath(full_p, src_folder)
            z.write(full_p, rel_p)

size_mb = os.path.getsize(zip_out) / (1024 * 1024)
print(f"Đóng gói hoàn tất trong {time.time() - start_t:.1f}s!")
print(f"File thành phẩm: {zip_out} ({size_mb:.2f} MB)")
