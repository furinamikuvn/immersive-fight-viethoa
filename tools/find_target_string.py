# -*- coding: utf-8 -*-
import os, sys, zipfile

sys.stdout.reconfigure(encoding='utf-8')

targets = ['需穿戴', '自由飞行', '全套末地战士', '背部槽', '职业', 'Sinh ra từ']

base_dir = r"D:\minecraft mod trung"
game_dir = r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1"

scan_dirs = [base_dir, game_dir]

print("Scanning for targets:", targets)

for sdir in scan_dirs:
    if not os.path.exists(sdir):
        continue
    for root, dirs, files in os.walk(sdir):
        # Skip git
        if '.git' in root or '.system_generated' in root or 'temp_mod' in root:
            continue
        for f in files:
            p = os.path.join(root, f)
            if f.endswith(('.json', '.snbt', '.toml', '.txt', '.badiff', '.class', '.js')):
                try:
                    with open(p, 'rb') as fp:
                        content = fp.read()
                        for t in targets:
                            if t.encode('utf-8') in content:
                                print(f"Found '{t}' in file: {p}")
                except Exception:
                    pass
            elif f.endswith(('.zip', '.jar')):
                try:
                    with zipfile.ZipFile(p, 'r') as zf:
                        for n in zf.namelist():
                            try:
                                raw = zf.read(n)
                                for t in targets:
                                    if t.encode('utf-8') in raw:
                                        print(f"Found '{t}' in {p} -> {n}")
                            except Exception:
                                pass
                except Exception:
                    pass

print("Scan complete.")
