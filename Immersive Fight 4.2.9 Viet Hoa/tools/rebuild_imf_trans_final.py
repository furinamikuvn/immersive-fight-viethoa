import os
import sys
import zipfile
import shutil
import json

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
orig_trans_zip = os.path.join(base_dir, "resourcepacks", "IMF-Trans.zip")
backup_trans_zip = os.path.join(base_dir, "resourcepacks", "IMF-Trans.zip.bak")
translated_assets_dir = os.path.join(base_dir, "resourcepack", "IMF-VietHoa", "assets")
mods_dir = os.path.join(base_dir, "mods")

# 1. Collect all translated language files from IMF-VietHoa
lang_injections = {} # path in zip -> bytes

for root, dirs, files in os.walk(translated_assets_dir):
    for f in files:
        if f == "vi_vn.json":
            full_p = os.path.join(root, f)
            rel_p = os.path.relpath(full_p, translated_assets_dir)
            modid = rel_p.split(os.sep)[0]
            
            with open(full_p, 'rb') as fp:
                data = fp.read()
                
            vi_path = f"assets/{modid}/lang/vi_vn.json"
            zh_path = f"assets/{modid}/lang/zh_cn.json"
            lang_injections[vi_path] = data
            lang_injections[zh_path] = data

print(f"Loaded {len(lang_injections)} translated lang entries from IMF-VietHoa.")

# 2. Extract clean en_us.json from mod jars for mods that had Chinese in en_us
clean_en_mods = {
    'soul_like_armors_reworked': 'soul_like_armors_reworked_1.20.1_(v140).jar',
    'endermanoverhaul': 'endermanoverhaul-forge-1.20.1-1.0.4.jar',
    'regions_unexplored': 'RegionsUnexploredForge-0.5.6+1.20.1.jar',
    'ftbessentials': 'ftb-essentials-forge-2001.2.2.jar'
}

for modid, jarname in clean_en_mods.items():
    jp = os.path.join(mods_dir, jarname)
    if os.path.exists(jp):
        with zipfile.ZipFile(jp, 'r') as z:
            internal_en = f"assets/{modid}/lang/en_us.json"
            if internal_en in z.namelist():
                lang_injections[internal_en] = z.read(internal_en)
                print(f"Extracted clean en_us.json for {modid} from {jarname}")

# 3. Extract clean English patchouli files from simplyswords jar to replace Chinese ones
ss_jar = os.path.join(mods_dir, "simplyswords-forge-1.56.0-1.20.1.jar")
patchouli_injections = {}
if os.path.exists(ss_jar):
    with zipfile.ZipFile(ss_jar, 'r') as z:
        prefix = "data/simplyswords/patchouli_books/runic_grimoire/en_us/"
        for n in z.namelist():
            if n.startswith(prefix) and not n.endswith('/'):
                rel = n[len(prefix):]
                data = z.read(n)
                # Put in zh_cn, en_us, vi_vn locations
                patchouli_injections[f"assets/simplyswords/patchouli_books/runic_grimoire/zh_cn/{rel}"] = data
                patchouli_injections[f"assets/simplyswords/patchouli_books/runic_grimoire/en_us/{rel}"] = data
                patchouli_injections[f"assets/simplyswords/patchouli_books/runic_grimoire/vi_vn/{rel}"] = data
    print(f"Prepared {len(patchouli_injections)} clean patchouli entries from simplyswords jar.")

# 4. Build new IMF-Trans.zip
temp_zip = os.path.join(base_dir, "resourcepacks", "IMF-Trans-temp.zip")

added_files = set()
with zipfile.ZipFile(backup_trans_zip, 'r') as src_zip:
    with zipfile.ZipFile(temp_zip, 'w', zipfile.ZIP_DEFLATED) as dst_zip:
        for item in src_zip.infolist():
            name = item.filename
            
            # If it's an old patchouli book file in zh_cn, replace with clean or skip
            if name.startswith("assets/simplyswords/patchouli_books/runic_grimoire/zh_cn/"):
                if name in patchouli_injections:
                    dst_zip.writestr(name, patchouli_injections[name])
                    added_files.add(name)
                # If not in jar, skip it
                continue
                
            if name in lang_injections:
                dst_zip.writestr(name, lang_injections[name])
                added_files.add(name)
            else:
                dst_zip.writestr(item, src_zip.read(name))
                added_files.add(name)
                
        # Write any new injections not in original zip
        for name, data in lang_injections.items():
            if name not in added_files:
                dst_zip.writestr(name, data)
                added_files.add(name)
                
        for name, data in patchouli_injections.items():
            if name not in added_files:
                dst_zip.writestr(name, data)
                added_files.add(name)

# Replace target zip
if os.path.exists(orig_trans_zip):
    os.remove(orig_trans_zip)
os.rename(temp_zip, orig_trans_zip)

print(f"IMF-Trans.zip rebuilt successfully! New size: {os.path.getsize(orig_trans_zip) / (1024*1024):.2f} MB")
