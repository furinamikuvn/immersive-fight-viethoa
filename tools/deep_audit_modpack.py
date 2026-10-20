import os
import sys
import re
import zipfile
import json

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

chinese_regex = re.compile(r'[\u4e00-\u9fff]')

base_folder = r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh"

print("=====================================================================")
print("          TĂNG CƯỜNG QUÉT SÂU TOÀN DIỆN MODPACK (DEEP AUDIT)          ")
print("=====================================================================")

# 1. Quét hotai .badiff
print("\n--- 1. KIỂM TRA TOÀN BỘ FILE BADIFF TRONG HOTAI ---")
hotai_dir = os.path.join(base_folder, "hotai")
badiff_chinese_found = 0
for root, dirs, files in os.walk(hotai_dir):
    for f in files:
        if f.endswith(".badiff"):
            p = os.path.join(root, f)
            with open(p, "rb") as fp:
                data = fp.read()
            text = data.decode("utf-8", errors="ignore")
            matches = chinese_regex.findall(text)
            if matches:
                badiff_chinese_found += 1
                rel = os.path.relpath(p, hotai_dir)
                unique_ch = "".join(list(set(matches))[:15])
                print(f"  [HOTAI CHINESE] {rel} ({len(matches)} ký tự): {unique_ch}")

if badiff_chinese_found == 0:
    print("  -> Tuyệt vời! Không còn bất kỳ ký tự tiếng Trung nào trong bytecode hotai active.")

# 2. Quét config & ftbquests & global_packs
print("\n--- 2. KIỂM TRA CONFIG, FTBQUESTS, GLOBAL_PACKS ---")
for sub in ["ftbquests", "config", "global_packs", "minemenu"]:
    target = os.path.join(base_folder, sub)
    found_sub = 0
    if os.path.exists(target):
        for root, dirs, files in os.walk(target):
            for f in files:
                if f.endswith((".snbt", ".json", ".txt", ".toml", ".cfg", ".yaml", ".yml")):
                    p = os.path.join(root, f)
                    try:
                        content = open(p, "r", encoding="utf-8", errors="ignore").read()
                        matches = chinese_regex.findall(content)
                        if matches:
                            found_sub += 1
                            rel = os.path.relpath(p, base_folder)
                            print(f"  [{sub.upper()}] {rel} ({len(matches)} ký tự): {''.join(list(set(matches))[:10])}")
                    except:
                        pass
    if found_sub == 0:
        print(f"  -> Thư mục '{sub}': Sạch 100% tiếng Trung.")

# 3. Quét toàn bộ resourcepacks
print("\n--- 3. KIỂM TRA CÁC GÓI TÀI NGUYÊN TRONG RESOURCEPACKS ---")
rp_dir = os.path.join(base_folder, "resourcepacks")
for rpf in sorted(os.listdir(rp_dir)):
    if rpf.endswith(".zip"):
        rp_path = os.path.join(rp_dir, rpf)
        chinese_in_rp = []
        try:
            with zipfile.ZipFile(rp_path, "r") as zf:
                for n in zf.namelist():
                    if n.endswith((".json", ".lang", ".txt", ".snbt")):
                        # Nếu là zh_cn.json của vanilla/resourcepack không bắt buộc, nhưng hãy xem nếu là vi_vn.json mà có tiếng Trung thì phải bắt
                        try:
                            c = zf.read(n).decode("utf-8", errors="ignore")
                            matches = chinese_regex.findall(c)
                            if matches:
                                if "zh_cn" not in n:
                                    chinese_in_rp.append((n, len(matches), "".join(list(set(matches))[:10])))
                        except:
                            pass
        except Exception as e:
            print(f"  Lỗi đọc {rpf}: {e}")
        
        if chinese_in_rp:
            print(f"  [RESOURCEPACK CHINESE] {rpf}:")
            for n, cnt, sample in chinese_in_rp[:10]:
                print(f"    - {n} ({cnt} ký tự): {sample}")
            if len(chinese_in_rp) > 10:
                print(f"    ... và {len(chinese_in_rp) - 10} file khác.")
        else:
            print(f"  [RESOURCEPACK CLEAN] {rpf}: Hoàn toàn sạch tiếng Trung trong file không phải zh_cn!")

print("\n--- QUÉT SÂU HOÀN TẤT BƯỚC 1 ---")
