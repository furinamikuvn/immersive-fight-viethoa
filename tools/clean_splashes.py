import os
import zipfile
import shutil
import re
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

reimagined_paths = [
    r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh\resourcepacks\Reimagined.zip",
    r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\resourcepacks\Reimagined.zip",
    r"D:\minecraft mod trung\Immersive Fight 4.2.9\resourcepacks\Reimagined.zip",
    r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\resourcepacks\Reimagined.zip"
]

for rp in reimagined_paths:
    if os.path.exists(rp):
        temp_zip = rp + ".tmp"
        with zipfile.ZipFile(rp, "r") as zin, zipfile.ZipFile(temp_zip, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                content = zin.read(item.filename)
                if item.filename == "assets/minecraft/texts/splashes.txt":
                    text = content.decode("utf-8", errors="ignore")
                    lines = [l for l in text.splitlines() if not re.search(r'[\u4e00-\u9fff]', l)]
                    lines.append("Immersive Fight 4.2.9!")
                    lines.append("Bản Việt Hóa Souls-like Chuẩn Nhất!")
                    lines.append("Chém mượt, né chuẩn!")
                    content = "\n".join(lines).encode("utf-8")
                zout.writestr(item, content)
        shutil.move(temp_zip, rp)
        print(f"Sạch 100% tiếng Trung trong splashes: {rp}")
