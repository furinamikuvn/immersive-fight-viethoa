import os, sys, zipfile, json, re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

game_dir = Path(r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1")
mods_dir = game_dir / "mods"
deployed_assets = game_dir / "resources" / "assets"

print("=== PHA 2: SO SÁNH KEYS GIỮA JAR GỐC VÀ RESOURCES/ASSETS ĐÃ DEPLOY ===")

missing_keys_by_ns = {}
extra_keys_in_jars = 0

for jar in sorted(mods_dir.glob("*.jar")):
    try:
        with zipfile.ZipFile(jar, 'r') as zf:
            for name in zf.namelist():
                # Tìm các file lang trong jar
                m = re.match(r'^assets/([^/]+)/lang/([^/]+)\.json$', name)
                if not m: continue
                ns, lang_type = m.group(1), m.group(2)
                
                # Đọc json từ jar
                try:
                    jar_data = json.loads(zf.read(name).decode('utf-8-sig'))
                except Exception:
                    continue
                
                # Đọc json đã deploy
                dep_file = deployed_assets / ns / "lang" / "vi_vn.json"
                if not dep_file.exists():
                    missing_keys_by_ns.setdefault(ns, []).extend(list(jar_data.keys()))
                    continue
                
                try:
                    dep_data = json.loads(dep_file.read_text(encoding='utf-8'))
                except Exception:
                    dep_data = {}
                
                # Tìm các key có trong jar nhưng thiếu trong deployed
                missing = [k for k in jar_data.keys() if k not in dep_data]
                if missing:
                    missing_keys_by_ns.setdefault(ns, []).extend(missing)
                    extra_keys_in_jars += len(missing)
    except Exception:
        pass

print(f"Tổng số namespaces có key bị thiếu so với jar gốc: {len(missing_keys_by_ns)}")
print(f"Tổng số keys có trong jar nhưng chưa có trong deployed: {extra_keys_in_jars}")

for ns, keys in sorted(missing_keys_by_ns.items(), key=lambda x: -len(x[1]))[:20]:
    unique_keys = list(set(keys))
    print(f"\n[{ns}] thiếu {len(unique_keys)} keys so với jar:")
    for k in unique_keys[:5]:
        print(f"   - {k}")
