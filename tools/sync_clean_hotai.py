import os
import shutil
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

src_hotai = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\hotai"
dest_targets = [
    r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh\hotai",
    r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\hotai"
]

copied_count = 0
for root, dirs, files in os.walk(src_hotai):
    for f in files:
        if f.endswith(".badiff") and not f.endswith(".bak"):
            src_file = os.path.join(root, f)
            rel_p = os.path.relpath(src_file, src_hotai)
            for dest in dest_targets:
                dest_file = os.path.join(dest, rel_p)
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copy2(src_file, dest_file)
            copied_count += 1

# Make sure no .bak files exist in dest targets
for dest in dest_targets:
    for root, dirs, files in os.walk(dest):
        for f in files:
            if f.endswith(".bak"):
                os.remove(os.path.join(root, f))

print(f"Đã đồng bộ {copied_count} file .badiff sạch sang cả 2 thư mục đích!")
