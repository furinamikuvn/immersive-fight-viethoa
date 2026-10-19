import os
import sys
import zipfile
import json

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

search_phrases = [
    'chống Nhật', 
    'Trận chiến hoành tráng', 
    'áo giáp tưởng tượng', 
    'đêm mùa thu', 
    'Vật phẩm thức tỉnh',
    'Nightfall',
    'Revolution',
    'immersive_armors'
]

print("=== TÌM KIẾM CÁC TỪ KHÓA DỊCH LỎ ===")

def search_in_zip(zip_path):
    found = []
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            for n in zf.namelist():
                if n.endswith(('.json', '.snbt', '.lang')):
                    try:
                        content = zf.read(n).decode('utf-8', errors='ignore')
                        for sp in search_phrases:
                            if sp in content:
                                found.append((zip_path, n, sp))
                    except:
                        pass
    except:
        pass
    return found

# 1. Search in resourcepacks
base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh"
rp_dir = os.path.join(base_dir, "resourcepacks")
for f in os.listdir(rp_dir):
    if f.endswith('.zip'):
        for p, n, sp in search_in_zip(os.path.join(rp_dir, f)):
            print(f"[FOUND in RP] {os.path.basename(p)} -> {n}: contains '{sp}'")

# 2. Search in tools/
tools_dir = r"D:\minecraft mod trung\tools"
for root, dirs, files in os.walk(tools_dir):
    for f in files:
        if f.endswith(('.json', '.txt', '.py')):
            p = os.path.join(root, f)
            try:
                c = open(p, 'r', encoding='utf-8', errors='ignore').read()
                for sp in search_phrases:
                    if sp in c:
                        print(f"[FOUND in TOOLS] {os.path.relpath(p, tools_dir)}: contains '{sp}'")
            except:
                pass

# 3. Check mod jars in mods
mods_dir = os.path.join(base_dir, "mods")
for f in os.listdir(mods_dir):
    if any(m in f.lower() for m in ['epicfight', 'nightfall', 'armors', 'efn']):
        for p, n, sp in search_in_zip(os.path.join(mods_dir, f)):
            print(f"[FOUND in MOD] {f} -> {n}: contains '{sp}'")
