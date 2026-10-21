import os, sys, zipfile, json, re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

game_dir = Path(r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1")
mods_dir = game_dir / "mods"
deployed_assets = game_dir / "resources" / "assets"

print("=== AUDIT CHUẨN XÁC: SO SÁNH EN_US VÀ ZH_CN TRONG JAR VỚI DEPLOYED ASSETS ===")

missing_real = {}

for jar in sorted(mods_dir.glob("*.jar")):
    try:
        with zipfile.ZipFile(jar, 'r') as zf:
            for name in zf.namelist():
                m = re.match(r'^assets/([^/]+)/lang/(en_us|zh_cn)\.json$', name)
                if not m: continue
                ns, lang_type = m.group(1), m.group(2)
                
                try:
                    jar_data = json.loads(zf.read(name).decode('utf-8-sig', errors='replace'))
                    if not isinstance(jar_data, dict): continue
                except Exception:
                    continue
                
                dep_file = deployed_assets / ns / "lang" / "vi_vn.json"
                if not dep_file.exists():
                    missing_real.setdefault(ns, set()).update(jar_data.keys())
                    continue
                
                try:
                    dep_data = json.loads(dep_file.read_text(encoding='utf-8'))
                except Exception:
                    dep_data = {}
                
                missing = [k for k in jar_data.keys() if k not in dep_data]
                if missing:
                    missing_real.setdefault(ns, set()).update(missing)
    except Exception:
        pass

total_missing = sum(len(v) for v in missing_real.values())
print(f"Tổng số namespaces còn thiếu key en_us/zh_cn thực tế từ jar: {len(missing_real)}")
print(f"Tổng số keys en_us/zh_cn còn thiếu: {total_missing}")

for ns, keys in sorted(missing_real.items(), key=lambda x: -len(x[1])):
    print(f"\n[{ns}] thiếu {len(keys)} keys:")
    for k in list(keys)[:5]:
        print(f"   - {k}")
