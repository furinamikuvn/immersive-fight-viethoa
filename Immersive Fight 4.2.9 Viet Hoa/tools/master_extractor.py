import os
import sys
import zipfile
import json
import re

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
mods_dir = os.path.join(base_dir, "mods")
orig_trans_zip = os.path.join(base_dir, "resourcepacks", "IMF-Trans.zip.bak")
existing_vh_dir = os.path.join(base_dir, "resourcepack", "IMF-VietHoa", "assets")
output_dir = os.path.join(base_dir, "tools", "master_extracted")
os.makedirs(output_dir, exist_ok=True)

re_chinese = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]')

print("=== STEP 1: COLLECTING ALL NAMESPACES & KEYS ACROSS MODPACK ===")

# Master structure:
# namespace -> {
#     key: {
#         'en': str or None,
#         'zh': str or None,
#         'vi': str or None,
#         'source': 'jar' | 'imf_trans' | 'vh_existing'
#     }
# }
master_data = {}

def get_ns_dict(ns):
    if ns not in master_data:
        master_data[ns] = {}
    return master_data[ns]

# 1. Load existing Viet Hoa translations
print("1. Loading existing IMF-VietHoa translations...")
vh_count = 0
for root, dirs, files in os.walk(existing_vh_dir):
    for f in files:
        if f.endswith('.json'):
            p = os.path.join(root, f)
            rel = os.path.relpath(p, existing_vh_dir).replace('\\', '/')
            parts = rel.split('/')
            ns = parts[0]
            ns_dict = get_ns_dict(ns)
            try:
                with open(p, 'r', encoding='utf-8') as fp:
                    data = json.load(fp)
                    for k, v in data.items():
                        if k not in ns_dict:
                            ns_dict[k] = {'en': None, 'zh': None, 'vi': None}
                        ns_dict[k]['vi'] = str(v)
                        vh_count += 1
            except Exception as e:
                pass
print(f"   Loaded {vh_count} existing Vietnamese keys across {len(master_data)} namespaces.")

# 2. Load from IMF-Trans.zip.bak
print("2. Loading keys from IMF-Trans.zip.bak...")
imf_count = 0
if os.path.exists(orig_trans_zip):
    with zipfile.ZipFile(orig_trans_zip, 'r') as z:
        for n in z.namelist():
            if n.startswith('assets/') and '/lang/' in n and n.endswith('.json'):
                parts = n.split('/')
                if len(parts) >= 4:
                    ns = parts[1]
                    ns_dict = get_ns_dict(ns)
                    try:
                        data = json.loads(z.read(n).decode('utf-8', errors='ignore'))
                        for k, v in data.items():
                            if k not in ns_dict:
                                ns_dict[k] = {'en': None, 'zh': None, 'vi': None}
                            ns_dict[k]['zh'] = str(v)
                            imf_count += 1
                    except:
                        pass
print(f"   Loaded {imf_count} keys from IMF-Trans.zip.bak.")

# 3. Load from all 307 jar files in mods/
print("3. Scanning all 307 mod .jars in mods/...")
jar_en_count = 0
jar_zh_count = 0
for jar in os.listdir(mods_dir):
    if jar.endswith('.jar'):
        p = os.path.join(mods_dir, jar)
        try:
            with zipfile.ZipFile(p, 'r') as z:
                for n in z.namelist():
                    if n.startswith('assets/') and '/lang/' in n and n.endswith('.json'):
                        parts = n.split('/')
                        if len(parts) >= 4:
                            ns = parts[1]
                            lang_f = parts[-1]
                            ns_dict = get_ns_dict(ns)
                            
                            if lang_f == 'en_us.json':
                                try:
                                    data = json.loads(z.read(n).decode('utf-8', errors='ignore'))
                                    for k, v in data.items():
                                        if k not in ns_dict:
                                            ns_dict[k] = {'en': None, 'zh': None, 'vi': None}
                                        ns_dict[k]['en'] = str(v)
                                        jar_en_count += 1
                                except: pass
                            elif lang_f == 'zh_cn.json':
                                try:
                                    data = json.loads(z.read(n).decode('utf-8', errors='ignore'))
                                    for k, v in data.items():
                                        if k not in ns_dict:
                                            ns_dict[k] = {'en': None, 'zh': None, 'vi': None}
                                        if not ns_dict[k]['zh']: # prefer IMF-Trans if present, otherwise jar
                                            ns_dict[k]['zh'] = str(v)
                                        jar_zh_count += 1
                                except: pass
        except:
            pass

print(f"   Loaded {jar_en_count} English keys and {jar_zh_count} Chinese keys from JARs.")
print(f"Total namespaces found: {len(master_data)}")
total_all_keys = sum(len(v) for v in master_data.values())
print(f"Total unique keys across entire modpack: {total_all_keys}")

# Save master_data to json
summary_path = os.path.join(output_dir, "master_inventory_stats.json")
stats = {
    'total_namespaces': len(master_data),
    'total_keys': total_all_keys,
    'namespaces': {ns: len(keys) for ns, keys in master_data.items()}
}
with open(summary_path, 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)

print(f"Summary saved to {summary_path}")

# Write raw master data partitioned by namespace for high performance
raw_out_dir = os.path.join(output_dir, "namespaces")
os.makedirs(raw_out_dir, exist_ok=True)
for ns, keys in master_data.items():
    ns_file = os.path.join(raw_out_dir, f"{ns}.json")
    with open(ns_file, 'w', encoding='utf-8') as f:
        json.dump(keys, f, ensure_ascii=False, indent=2)

print(f"Wrote all {len(master_data)} namespace json files to {raw_out_dir}")
