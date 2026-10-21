import os, sys, json
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(r"D:\minecraft mod trung")
TARGET_DIRS = [
    ROOT_DIR / "Immersive Fight 4.2.9 Viet Hoa" / "resourcepack" / "IMF-VietHoa" / "assets",
    ROOT_DIR / "Immersive Fight 4.2.9" / "resources" / "assets",
    Path(r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\resources\assets")
]

FINAL_DIRECT_REPLACES = {
    # Alex's Caves & Mobs
    "item.alexscaves.underground_cabin_explorer_map": "Bản Đồ Nhà Gỗ Dưới Lòng Đất",
    "item.alexsmobs.sombrero.special_desc": "Đội Theo Phong Cách Hài Hước",
    
    # BetterEnd smithing templates
    "item.betterend.smithing_template.thallasium_upgrade.additions_slot_description": "Đặt Thỏi Thallasium",
    "item.betterend.smithing_template.aeternium_upgrade.base_slot_description": "Đặt Cánh Cứng Elytra hoặc Đe Terminite",
    "item.betterend.smithing_template.netherite_upgrade.base_slot_description": "Đặt Búa Kim Cương",
    "item.betterend.smithing_template.netherite_upgrade.additions_slot_description": "Đặt Thỏi Netherite",
    "item.betterend.smithing_template.leather_handle_attachment.base_slot_description": "Đặt Đầu Công Cụ Aeternium",
    "item.betterend.smithing_template.plate_upgrade.additions_slot_description": "Đặt Tấm Rèn Aeternium",
    "item.betterend.smithing_template.aeternium_upgrade.additions_slot_description": "Đặt Thỏi Aeternium",
    "item.betterend.smithing_template.leather_handle_attachment.additions_slot_description": "Đặt Gậy Bọc Da",
    "item.betterend.smithing_template.plate_upgrade.base_slot_description": "Đặt Mảnh Terminite",
    "item.betterend.smithing_template.terminite_upgrade.base_slot_description": "Đặt Gậy hoặc Đe Thallasium",
    
    # Dungeons and Combat effects
    "effect.dungeons_and_combat.bronze_barbarian_helmet_bonus": "Hiệu Ứng Mũ Man Tộc Đồng",
    "effect.dungeons_and_combat.scorpion_claw_effect": "Hiệu Ứng Càng Bọ Cạp",
    "effect.dungeons_and_combat.broken_armor_iii": "Giáp Vỡ Nát III",
    "effect.dungeons_and_combat.scarlet_restoration_iii": "Hồi Phục Huyết Sắc III",
    "effect.dungeons_and_combat.man_of_steel": "Người Thép (Man of Steel)",
    "effect.dungeons_and_combat.hunter_boots_effect": "Hiệu Ứng Giày Thợ Săn",
    "effect.dungeons_and_combat.berserk_fury": "Cơn Thịnh Nộ Cuồng Nộ (Berserk)",
    
    # Elytra Utilities
    "gui.elytrautilities.config.simpleTakeoff.description": "Nếu bật, nhấn giữ phím kích hoạt Elytra sẽ dùng pháo hoa từ túi đồ để cất cánh.",
    "gui.elytrautilities.config.enableElytra.description": "Nếu bật, người chơi có thể bay lượn bằng cánh cứng Elytra.",
    "gui.elytrautilities.config.jumpTriggerable.description": "Nếu bật, có thể kích hoạt bay lượn bằng cách nhấn nhảy giữa không trung.",
    "gui.elytrautilities.config.restrictFireworks.description": "Nếu bật, pháo hoa chỉ có thể dùng khi đang bay lượn.",
    
    # Maid Smart
    "item.maid_smart.patrol_chart.desc1": "§7Ở chế độ cưỡi chổi + chế độ nhà, hầu gái sẽ tuần tra dọc theo lộ trình bạn đã vẽ (thay thế lộ trình mặc định).",
    "item.maid_smart.patrol_chart.desc2": "§fNhấp chuột phải§7 để mở biểu đồ: tạo / đổi tên lộ trình, liên kết hầu gái, bật / tắt tuần tra.",
    "item.maid_smart.combat_leash.desc1": "§7Dùng lên hầu gái đang bay để treo mình bên dưới làm xạ thủ; hầu gái tiếp tục bay, bạn thỏa sức bắn. Nhấp chuột phải để thả mình xuống.",
    "item.maid_smart.ride_baton.desc1": "§7Dùng lên thú cưỡi đã đặt yên để chọn, sau đó dùng lên hầu gái để liên kết cưỡi thú.",
    "item.maid_smart.ride_baton.desc3": "§7Hầu gái cưỡi thú đi theo bạn; ngồi xổm + sử dụng để xuống thú.",
    
    # Advancements
    "advancements.the_cursed_soul.descr": "Thu thập được một Linh Hồn Bị Nguyền Rủa",
    "advancements.now_you_can_rest.descr": "Đánh bại Kamath và thu thập Tinh Hoa của hắn",
    "advancements.is_this_my_size.descr": "Thu thập Càng Bọ Cạp Khổng Lồ",
    "advancements.the_bounty_hunter.descr": "Thiện hay ác, chỉ phụ thuộc vào kẻ trả giá cao hơn",
    "advancements.the_oni_slayer.descr": "Kỹ năng và sức mạnh là chưa đủ...",
    "advancements.hiddeninthe_cult.descr": "Khai thác được Quặng Gỗ Mun Thô (Ebony Raw)",
    "advancements.the_titan.descr": "Ngươi đã hy sinh thân mình để bảo vệ họ, tuy nhiên...",
    "advancements.the_vagabond.descr": "Ngươi chẳng có gì đặc biệt cả",
}

count = 0
for target in TARGET_DIRS:
    for ns_dir in target.iterdir():
        if not ns_dir.is_dir(): continue
        lang_dir = ns_dir / "lang"
        if not lang_dir.exists(): continue
        for lang_file in ["vi_vn.json", "zh_cn.json", "en_us.json"]:
            p = lang_dir / lang_file
            if not p.exists(): continue
            try:
                data = json.load(open(p, encoding='utf-8'))
                changed = False
                for k, v in FINAL_DIRECT_REPLACES.items():
                    if k in data:
                        data[k] = v
                        changed = True
                        count += 1
                if changed:
                    with open(p, 'w', encoding='utf-8', newline='\n') as fp:
                        json.dump(data, fp, ensure_ascii=False, indent=2)
                        fp.write('\n')
            except:
                pass

print(f"Hoàn thành ghi đè chính xác {count} vị trí!")
