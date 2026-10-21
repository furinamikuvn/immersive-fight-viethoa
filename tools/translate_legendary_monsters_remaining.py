# -*- coding: utf-8 -*-
"""
translate_legendary_monsters_remaining.py
Translates all remaining split and numbered keys in legendary_monsters into Vietnamese.
"""

import os, json

legendary_patches = {
    "item.legendary_monsters.axe_of_lightning1": "§6Kỹ Năng Đặc Biệt: §7Chuột phải để triệu hồi Sét Đánh §6[9 Sát Thương/Tick, Xuyên Giáp],",
    "item.legendary_monsters.axe_of_lightning2": "§7Chuột Phải vào khối để tạo Sóng Xung Kích Điện phóng theo hướng",
    "item.legendary_monsters.axe_of_lightning3": "§7hướng bạn đang nhìn §6[Sát thương sóng xung kích mỗi lần trúng, Xuyên Giáp]",
    "item.legendary_monsters.blast_proof_helmet1": "§6Kỹ Năng Đặc Biệt: §7Giảm 35% sát thương nổ",
    "item.legendary_monsters.blast_proof_helmet2": "§6(Creeper nhảy bổ vào không còn quá nguy hiểm nữa!)",
    "item.legendary_monsters.buckler_of_annihilation1": "§7Giữ Shift + Chuột Phải trong 0.5s để tung đòn quét diện rộng và bắn 3 Bom Hủy Diệt nhỏ [8 sát thương xuyên giáp]. Hồi chiêu sau khi quét trúng mục tiêu",
    "item.legendary_monsters.chorus_blade2": "§7rất hữu ích để né tránh đòn tấn công bất ngờ. §6[CHUỘT PHẢI ĐỂ DÙNG]",
    "item.legendary_monsters.chorus_helmet2": "§7khỏi hiệu ứng Lây Nhiễm Chorus.",
    "item.legendary_monsters.corrupted_soul1": "Ta đã.. tự do.. Ta sẽ đối mặt với trận quyết chiến cuối cùng một lần nữa",
    "item.legendary_monsters.frost_shield1": "§6Kỹ Năng Đặc Biệt: §7Đóng băng kẻ địch trong 3 giây khi đỡ đòn",
    "item.legendary_monsters.frost_shield2": "§6[ĐỠ ĐÒN ĐỂ KÍCH HOẠT]",
    "item.legendary_monsters.mossy_hammer3": "§7bột xương trong túi đồ, khối rêu phong sẽ lập tức mọc dưới chân mọi kẻ địch bị thương trong bán kính 3 khối!",
    "item.legendary_monsters.mossy_hammer4": "§6[CHUỘT PHẢI VÀO KHỐI ĐỂ DÙNG]",
    "item.legendary_monsters.sand_cannon1": "§6Kỹ Năng Đặc Biệt: §7Giữ chuột 1.5 giây để bắn Bom Đá Cát",
    "item.legendary_monsters.shattered_greatsword1": "'Thanh Kiếm Của Các Hiệp Sĩ Vương Triều Sụp Đổ'",
    "item.legendary_monsters.soul_great_sword1": "Chuột Phải để Đỡ Đòn (Diện Rộng), gây sát thương",
    "item.legendary_monsters.soul_great_sword3": "Không thể đỡ đòn trước nguồn sát thương Xuyên Giáp",
    "item.legendary_monsters.soul_great_sword5": "Giữ Shift + Chuột Phải trong 1s khi nhìn vào thực thể trong bán kính 10 khối để phóng Phi Dao Linh Hồn tầm nhiệt",
    "item.legendary_monsters.totem_of_moss3": "§fShift + Chuột Phải lên golem để bật '§aChế Độ Đứng Yên§7'",
    "item.legendary_monsters.withered_ribcage1": "§6Kỹ Năng Đặc Biệt: §7Giáp ngực này bảo vệ người chơi",
    "item.legendary_monsters.withered_scythe1": "§6Kỹ Năng Đặc Biệt: Giữ Chuột Phải để lao vọt về phía trước",
    "item.legendary_monsters.withered_scythe2": "§7và chém xé mọi thực thể trên đường lao",
    "item.legendary_monsters.smithing_template.annihilator_upgrade4": "Nguyên liệu:",
    "item.legendary_monsters.smithing_template.enderitium_upgrade4": "Nguyên liệu:",
    "block.legendary_monsters.ender_anchor1": "Đặt Đèn Lồng Hủy Diệt vào để đặt điểm hồi sinh tại The End",
    "block.legendary_monsters.skeletosaurus_egg4": "§6-Đặt trên cát linh hồn để rút ngắn thời gian ấp nở.",
    "block.legendary_monsters.somber_trapdoor1": "Chuột phải vào giữa bằng Chìa Khóa U Tối để phá khóa"
}

assets_base = r"Immersive Fight 4.2.9 Viet Hoa\resources\assets\legendary_monsters\lang"
for lang in ['en_us.json', 'vi_vn.json', 'zh_cn.json']:
    fp = os.path.join(assets_base, lang)
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            d = json.load(f)
        d.update(legendary_patches)
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)

print(f"Applied {len(legendary_patches)} legendary_monsters keys across all lang files!")
