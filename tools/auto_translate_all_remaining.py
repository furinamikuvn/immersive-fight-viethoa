import os, sys, json, re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(r"D:\minecraft mod trung")
TARGET_DIRS = [
    ROOT_DIR / "Immersive Fight 4.2.9 Viet Hoa" / "resourcepack" / "IMF-VietHoa" / "assets",
    ROOT_DIR / "Immersive Fight 4.2.9" / "resources" / "assets",
    Path(r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\resources\assets")
]

# Từ điển ánh xạ từ vựng Potion
POTION_WORDS = {
    "soulsteal": "Đoạt Hồn (Soulsteal)",
    "swiftness": "Tốc Độ (Swiftness)",
    "speed": "Tốc Độ (Speed)",
    "speed iii": "Tốc Độ III",
    "speed_iii": "Tốc Độ III",
    "bug pheromones": "Pheromone Côn Trùng",
    "bug_pheromones": "Pheromone Côn Trùng",
    "clinging": "Bám Dính (Clinging)",
    "lava vision": "Thị Giác Dung Nham",
    "lava_vision": "Thị Giác Dung Nham",
    "knockback resistance": "Kháng Đẩy Lùi",
    "knockback_resistance": "Kháng Đẩy Lùi",
    "poison resistance": "Kháng Độc Tố",
    "poison_resistance": "Kháng Độc Tố",
    "sugar rush": "Hưng Phấn Tăng Tốc",
    "sugar_rush": "Hưng Phấn Tăng Tốc",
    "haste": "Mau Lẹ (Haste)",
    "magnetizing": "Từ Tính (Magnetizing)",
    "deepsight": "Tầm Nhìn Vực Sâu",
    "glowing": "Phát Quang (Glowing)",
    "end veil": "Màn Che Hư Không",
    "end_veil": "Màn Che Hư Không",
    "intoxication": "Say Mềm (Intoxication)",
    "intoxicated": "Say Mềm",
    "stimulations": "Kích Thích Tinh Thần",
    "magical depletion": "Hao Tổn Ma Lực",
    "living cocoon": "Kén Sống (Living Cocoon)",
    "antidote": "Giải Độc (Antidote)",
    "blindness": "Mù Lòa (Blindness)",
    "guardian creator": "Kiến Tạo Hộ Vệ",
    "frozen resistance": "Kháng Băng Giá",
    "fatal oath": "Lời Thề Tử Vong",
    "gigant": "Khổng Lồ Hóa (Gigant)",
    "levitation": "Bay Lơ Lửng (Levitation)",
    "reaching": "Gia Tăng Tầm Với",
    "piercing": "Xuyên Thấu (Piercing)",
    "blooming": "Nở Hoa (Blooming)",
    "instant cure": "Trị Liệu Tức Thì",
    "weaker instant cure": "Trị Liệu Tức Thì Yếu",
    "weakness": "Yếu Đuối",
    "leaping": "Nhảy Cao",
    "jump boost": "Nhảy Cao",
    "slowness": "Làm Chậm",
    "poison": "Độc Tố",
    "strength": "Sức Mạnh",
    "healing": "Trị Liệu",
    "harming": "Sát Thương",
    "regeneration": "Hồi Máu",
    "night vision": "Thị Giác Ban Đêm",
    "water breathing": "Thở Dưới Nước",
    "slow falling": "Rơi Chậm",
    "turtle master": "Bậc Thầy Rùa Biển",
    "fire resistance": "Kháng Lửa",
    "invisibility": "Tàng Hình",
    "luck": "May Mắn"
}

def translate_english_phrase(val: str, key: str) -> str:
    """Tự động chuyển ngữ câu mô tả tiếng Anh sang tiếng Việt chuẩn xác."""
    k_lower = key.lower()
    v_clean = val.strip()
    
    # 1. Potion phrases
    if "potion of" in v_clean.lower() or "arrow of" in v_clean.lower():
        prefix = ""
        if v_clean.lower().startswith("lingering potion of "):
            prefix = "Thuốc Kéo Dài "
            eff = v_clean[len("Lingering Potion of "):]
        elif v_clean.lower().startswith("splash potion of "):
            prefix = "Thuốc Ném "
            eff = v_clean[len("Splash Potion of "):]
        elif v_clean.lower().startswith("potion of "):
            prefix = "Thuốc "
            eff = v_clean[len("Potion of "):]
        elif v_clean.lower().startswith("arrow of "):
            prefix = "Mũi Tên "
            eff = v_clean[len("Arrow of "):]
        elif "splash" in v_clean.lower() and "potion" in v_clean.lower():
            prefix = "Thuốc Ném "
            eff = v_clean.replace("Splash", "").replace("Potion", "").replace("of", "").strip()
        elif "lingering" in v_clean.lower() and "potion" in v_clean.lower():
            prefix = "Thuốc Kéo Dài "
            eff = v_clean.replace("Lingering", "").replace("Potion", "").replace("of", "").strip()
        else:
            prefix = "Thuốc "
            eff = v_clean.replace("Potion", "").replace("of", "").strip()
            
        eff_lower = eff.lower().strip()
        is_long = "long " in eff_lower or "longer " in eff_lower
        is_strong = "strong " in eff_lower or "stronger " in eff_lower
        eff_clean = eff_lower.replace("long ", "").replace("longer ", "").replace("strong ", "").replace("stronger ", "").strip()
        
        eff_vn = POTION_WORDS.get(eff_clean, eff.title())
        suffix = ""
        if is_long: suffix = " Kéo Dài"
        elif is_strong: suffix = " Cường Lực"
        return f"{prefix}{eff_vn}{suffix}"

    # 2. Smithing descriptions
    if v_clean.startswith("Add a ") or v_clean.startswith("Add "):
        item_text = v_clean.replace("Add a ", "").replace("Add ", "").strip()
        # Dịch một số từ khoá thông dụng
        item_vn = item_text
        replaces = [
            ("Thallasium Ingot", "Thỏi Thallasium"),
            ("Aeternium Ingot", "Thỏi Aeternium"),
            ("Netherite Ingot", "Thỏi Netherite"),
            ("Terminite Ingot", "Thỏi Terminite"),
            ("Diamond Hammer", "Búa Kim Cương"),
            ("Elytra or Terminite Anvil", "Cánh Cứng Elytra hoặc Đe Terminite"),
            ("Aeternium Tool Head", "Đầu Công Cụ Aeternium"),
            ("forged Aeternium Plate", "Tấm Rèn Aeternium"),
            ("Leather Wrapped Stick", "Gậy Bọc Da"),
            ("Terminite Piece", "Mảnh Terminite"),
            ("Stick or a Thallasium Anvil", "Gậy hoặc Đe Thallasium"),
            ("Sword Blade", "Lưỡi Kiếm"),
            ("Sword Handle", "Chuôi Kiếm")
        ]
        for en_sub, vn_sub in replaces:
            if en_sub.lower() in item_vn.lower():
                item_vn = vn_sub
                break
        return f"Đặt {item_vn}"

    # 3. Các vật phẩm & mô tả cụ thể
    specific_rules = {
        "Underground Cabin Map": "Bản Đồ Nhà Gỗ Dưới Lòng Đất",
        "Worn in a Goofy Fashion": "Đội Theo Phong Cách Hài Hước",
        "Grants Dolphin's Grace": "Ban tặng hiệu ứng Ân Huệ Cá Heo",
        "Allows you to catch more fish at night when held off-hand.": "Cho phép câu được nhiều cá hơn vào ban đêm khi cầm trên tay phụ.",
        "Makes the NPC forget the current quest and immediately start the next one.": "Khiến NPC lập tức hủy nhiệm vụ hiện tại và bắt đầu nhiệm vụ tiếp theo.",
        "+25% Chance to Catch Extra Item": "+25% Cơ hội câu được thêm vật phẩm",
        "Skill and power were not enough": "Kỹ năng và sức mạnh là chưa đủ...",
        "Obtain a Cursed Soul": "Thu thập được một Linh Hồn Bị Nguyền Rủa",
        "Defeat Kamath and obtain his Essence": "Đánh bại Kamath và thu thập Tinh Hoa của hắn",
        "Get a Giant Scorpion Claw": "Thu thập Càng Bọ Cạp Khổng Lồ",
        "Good, bad, depends on who pays more": "Thiện hay ác, chỉ phụ thuộc vào kẻ trả giá cao hơn",
        "Obtain Ebony Raw": "Khai thác được Quặng Gỗ Mun Thô (Ebony Raw)",
        "You sacrificed yourself to protect them, however...": "Ngươi đã hy sinh thân mình để bảo vệ họ, tuy nhiên...",
        "Your are not special": "Ngươi chẳng có gì đặc biệt cả",
        "Hold §2ALT§7 to view gem sockets": "Giữ §2ALT§7 để xem các khe khảm ngọc",
        "- Hold §2ALT§7 to view gem sockets -": "- Giữ §2ALT§7 để xem các khe khảm ngọc -",
    }
    for s_en, s_vn in specific_rules.items():
        if s_en.lower() in v_clean.lower():
            return s_vn

    return val


def main():
    print("=== TỰ ĐỘNG DỊCH TRIỆT ĐỂ TOÀN BỘ MÔ TẢ TIẾNG ANH CÒN SÓT ===")
    
    total_modified = 0
    
    for target in TARGET_DIRS:
        print(f"Xử lý target: {target}")
        for ns_dir in sorted(target.iterdir()):
            if not ns_dir.is_dir(): continue
            lang_dir = ns_dir / "lang"
            if not lang_dir.exists(): continue
            
            for lang_file in ["vi_vn.json", "zh_cn.json", "en_us.json"]:
                p = lang_dir / lang_file
                if not p.exists(): continue
                try:
                    data = json.load(open(p, encoding='utf-8'))
                    changed = False
                    
                    for k, v in list(data.items()):
                        if not isinstance(v, str): continue
                        
                        # Không can thiệp nếu là key tên vật phẩm block/item thuần túy
                        kl = k.lower()
                        if kl.startswith("block.") or (kl.startswith("item.") and not any(m in kl for m in ['.desc', '.tooltip', '.lore', '.ability', 'potion.', 'tipped_arrow.'])):
                            continue
                            
                        # Nếu là đĩa nhạc thì giữ nguyên tên bài hát
                        if "music_disc" in kl or "disc." in kl:
                            continue
                            
                        # Kiểm tra xem có phải chuỗi tiếng Anh cần dịch không
                        has_vn = any(ord(c) > 127 and c not in '§©®™°±×÷•…–—“”’‘' for c in v)
                        has_cjk = any(0x4e00 <= ord(c) <= 0x9fff for c in v)
                        
                        if not has_vn and not has_cjk:
                            new_val = translate_english_phrase(v, k)
                            if new_val != v:
                                data[k] = new_val
                                changed = True
                                total_modified += 1
                                
                    if changed:
                        with open(p, 'w', encoding='utf-8', newline='\n') as fp:
                            json.dump(data, fp, ensure_ascii=False, indent=2)
                            fp.write('\n')
                except Exception as e:
                    pass

    print(f"\n[HOÀN TẤT] Đã chuyển ngữ thành công {total_modified} chuỗi mô tả sang Tiếng Việt chuẩn!")

if __name__ == "__main__":
    main()
