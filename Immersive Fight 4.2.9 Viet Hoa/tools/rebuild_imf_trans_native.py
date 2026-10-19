import os
import sys
import zipfile
import shutil

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
orig_trans_zip = os.path.join(base_dir, "resourcepacks", "IMF-Trans.zip")
backup_trans_zip = os.path.join(base_dir, "resourcepacks", "IMF-Trans.zip.bak")
translated_assets_dir = os.path.join(base_dir, "resourcepack", "IMF-VietHoa", "assets")

# Backup original IMF-Trans.zip
if not os.path.exists(backup_trans_zip) and os.path.exists(orig_trans_zip):
    shutil.copy2(orig_trans_zip, backup_trans_zip)
    print(f"Backed up original IMF-Trans.zip to {backup_trans_zip}")

# Load all translated vi_vn.json contents
vi_lang_map = {} # path in zip -> bytes
for root, dirs, files in os.walk(translated_assets_dir):
    for f in files:
        if f == "vi_vn.json":
            full_p = os.path.join(root, f)
            rel_p = os.path.relpath(full_p, translated_assets_dir)
            parts = rel_p.split(os.sep) # [modid, 'lang', 'vi_vn.json']
            modid = parts[0]
            
            with open(full_p, 'rb') as fp:
                data = fp.read()
                
            vi_path = f"assets/{modid}/lang/vi_vn.json"
            zh_path = f"assets/{modid}/lang/zh_cn.json"
            vi_lang_map[vi_path] = data
            vi_lang_map[zh_path] = data

print(f"Loaded {len(vi_lang_map)} translated language entries for injection.")

# Read original zip, keep non-lang files, and replace/add lang files
temp_zip = os.path.join(base_dir, "resourcepacks", "IMF-Trans-temp.zip")

added_or_replaced = set()
with zipfile.ZipFile(backup_trans_zip, 'r') as src_zip:
    with zipfile.ZipFile(temp_zip, 'w', zipfile.ZIP_DEFLATED) as dst_zip:
        for item in src_zip.infolist():
            name = item.filename
            if name in vi_lang_map:
                # Write translated version
                dst_zip.writestr(name, vi_lang_map[name])
                added_or_replaced.add(name)
            else:
                # Keep original (e.g. textures, properties, pack.mcmeta)
                dst_zip.writestr(item, src_zip.read(name))
                
        # Write any new mod lang files that weren't in original zip
        for name, data in vi_lang_map.items():
            if name not in added_or_replaced:
                dst_zip.writestr(name, data)
                added_or_replaced.add(name)

# Replace IMF-Trans.zip with temp_zip
if os.path.exists(orig_trans_zip):
    os.remove(orig_trans_zip)
os.rename(temp_zip, orig_trans_zip)

print(f"ĐÃ TÁI CẤU TRÚC VÀ GHI ĐÈ THÀNH CÔNG: {orig_trans_zip}")
print(f"Kích thước mới: {os.path.getsize(orig_trans_zip) / 1024:.2f} KB")
print(f"Tổng số mục ngôn ngữ được cấy ghép: {len(added_or_replaced)}")
