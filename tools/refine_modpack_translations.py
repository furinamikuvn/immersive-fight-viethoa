import os
import sys
import json
import re

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

assets_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\resourcepack\IMF-VietHoa\assets"

print("=== TIẾN HÀNH TINH CHỈNH VĂN PHONG VÀ XÓA TẬN GỐC DỊCH LỎ ===")

# Danh sách từ điển thay thế toàn cục cho các từ dịch máy ngô nghê
replacements = {
    "con rối": "Golem",
    "Con rối": "Golem",
    "Tiểu sử của Alex": "Alex's Mobs",
    "Thanh kiếm đơn giản": "Simply Swords",
    "áo giáp tưởng tượng": "Fantasy Armor",
    "Áo giáp tưởng tượng": "Fantasy Armor",
    "Trận chiến hoành tráng": "Epic Fight",
    "trận chiến hoành tráng": "Epic Fight",
    "ĐêmMùa thu": "Epic Fight: Nightfall",
    "ĐêmMùa Thu": "Epic Fight: Nightfall",
    "vật phẩm thức tỉnh": "Vật phẩm Awakening",
    "Vật phẩm thức tỉnh": "Vật phẩm Awakening",
    "[Quái vật huyền thoại]": "[Legendary Monsters]",
    "quái vật huyền thoại": "quái vật Legendary Monsters",
    "AAB [Con rối]": "[Plenty of Golems]",
    "AAB[Con rối]": "[Plenty of Golems]",
    "Thêm con rối": "Plenty of Golems"
}

modified_files = 0
total_strings_modified = 0

for root, dirs, files in os.walk(assets_dir):
    for f in files:
        if f.endswith(".json") and "lang" in root:
            p = os.path.join(root, f)
            try:
                with open(p, "r", encoding="utf-8") as jf:
                    data = json.load(jf)
                changed = False
                for k, v in list(data.items()):
                    val_str = str(v)
                    new_val = val_str
                    for old_term, new_term in replacements.items():
                        if old_term in new_val:
                            new_val = new_val.replace(old_term, new_term)
                    
                    if new_val != val_str:
                        data[k] = new_val
                        changed = True
                        total_strings_modified += 1
                
                # Đặc biệt cho minecraft lang: thêm Sách Phù Phép
                if "assets" in p and "minecraft" in p and f.endswith("vi_vn.json"):
                    data["item.minecraft.enchanted_book"] = "Sách Phù Phép"
                    changed = True

                if changed:
                    with open(p, "w", encoding="utf-8") as jf:
                        json.dump(data, jf, ensure_ascii=False, indent=2)
                    modified_files += 1
            except Exception as e:
                pass

# Đảm bảo assets/minecraft/lang/vi_vn.json có item.minecraft.enchanted_book
mc_lang_dir = os.path.join(assets_dir, "minecraft", "lang")
os.makedirs(mc_lang_dir, exist_ok=True)
for lang_name in ["vi_vn.json", "en_us.json", "zh_cn.json"]:
    mc_file = os.path.join(mc_lang_dir, lang_name)
    mc_data = {}
    if os.path.exists(mc_file):
        try:
            with open(mc_file, "r", encoding="utf-8") as f:
                mc_data = json.load(f)
        except:
            pass
    mc_data["item.minecraft.enchanted_book"] = "Sách Phù Phép"
    with open(mc_file, "w", encoding="utf-8") as f:
        json.dump(mc_data, f, ensure_ascii=False, indent=2)

print(f"Hoàn tất: Đã sửa {total_strings_modified} chuỗi trong {modified_files} file JSON!")
