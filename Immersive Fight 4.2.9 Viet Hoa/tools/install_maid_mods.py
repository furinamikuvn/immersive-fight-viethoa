import os
import sys
import shutil
import json
import zipfile

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
dl_dir = os.path.join(base_dir, "downloads", "maid_mods")
game_dir = r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1"

vh_mods_dir = os.path.join(base_dir, "mods")
game_mods_dir = os.path.join(game_dir, "mods")

jar_files = [
    "touhoulittlemaid-1.5.3-forge+mc1.20.1.jar",
    "promaid-1.3.2-forge-1.20.1.jar",
    "1.20.1-maid_useful_task-1.4.2.jar"
]

print("=== STEP 1: COPYING MOD JARS ===")
for jf in jar_files:
    src_p = os.path.join(dl_dir, jf)
    dst_vh = os.path.join(vh_mods_dir, jf)
    dst_gm = os.path.join(game_mods_dir, jf)
    
    shutil.copy2(src_p, dst_vh)
    shutil.copy2(src_p, dst_gm)
    print(f"Copied {jf} to Viet Hoa and Game mods directories!")

# -------------------------------------------------------------
# STEP 2: PREPARE VIETNAMESE TRANSLATIONS FOR MAID ADDONS
# -------------------------------------------------------------
print("\n=== STEP 2: PREPARING VIETNAMESE LOCALIZATION ===")
vh_assets = os.path.join(base_dir, "resourcepack", "IMF-VietHoa", "assets")

# 1. maid_useful_task
maid_useful_task_vi = {
    "task.maid_useful_task.maid_tree": "Đốn Gỗ (Logging)",
    "task.maid_useful_task.maid_tree.desc": "Hầu gái sẽ tự động chặt cây xung quanh và trồng lại mầm cây.",
    "task.maid_useful_task.locate": "Định Vị (Locate)",
    "task.maid_useful_task.locate.desc": "Hầu gái có thể định vị cấu trúc hoặc nhà của bạn bằng vật phẩm chỉ định.",
    "task.maid_useful_task.revive_player": "Cứu Hộ Người Chơi",
    "task.maid_useful_task.revive_player.desc": "Hầu gái sẽ cứu hồi sinh người chơi đang bị chảy máu/hấp hối ở gần.",
    "key.maid_useful_tasks.switch_vehicle_control": "Chuyển Đổi Chế Độ Điều Khiển Phương Tiện",
    "maid_useful_task.allow_handle_vehicle.none": "Không cho phép hầu gái điều khiển phương tiện",
    "maid_useful_task.allow_handle_vehicle.rot_only": "Chỉ cho phép hầu gái xoay hướng phương tiện",
    "maid_useful_task.allow_handle_vehicle.full": "Cho phép hầu gái toàn quyền điều khiển phương tiện",
    "key.maid_useful_tasks.categories.main": "Maid Useful Tasks",
    "gui.maid_useful_task.logging.plant": "Trồng Lại Mầm Cây",
    "gui.maid_useful_task.no": "Không",
    "gui.maid_useful_task.yes": "Có",
    "gui.maid_useful_task.revive.ownerOnly": "Chỉ cứu chủ nhân",
    "gui.maid_useful_task.logging.block_up": "Xếp Khối Leo Lên",
    "gui.maid_useful_task.logging.skip_non_nature": "Bỏ qua gỗ nhân tạo (không tự nhiên)"
}

mut_lang = os.path.join(vh_assets, "maid_useful_task", "lang")
os.makedirs(mut_lang, exist_ok=True)
with open(os.path.join(mut_lang, "vi_vn.json"), 'w', encoding='utf-8') as f:
    json.dump(maid_useful_task_vi, f, ensure_ascii=False, indent=2)
with open(os.path.join(mut_lang, "zh_cn.json"), 'w', encoding='utf-8') as f:
    json.dump(maid_useful_task_vi, f, ensure_ascii=False, indent=2)
print("Saved maid_useful_task translations!")

# 2. promaid (maid_smart)
# Extract promaid en_us and translate all keys
promaid_jar = os.path.join(dl_dir, "promaid-1.3.2-forge-1.20.1.jar")
promaid_vi = {}
with zipfile.ZipFile(promaid_jar, 'r') as z:
    promaid_en = json.loads(z.read("assets/maid_smart/lang/en_us.json").decode('utf-8'))
    
# Common task & GUI translations for promaid
promaid_core_trans = {
    "task.maid_smart.mine": "Khai Khoáng (Mining)",
    "task.maid_smart.mine.desc": "Tự động tìm kiếm quặng xung quanh và khai thác bằng cuốc",
    "task.maid_smart.woodcut": "Chặt Gỗ (Woodcutting)",
    "task.maid_smart.woodcut.desc": "Tự động tìm cây, chặt bằng rìu và đốn ngã toàn bộ chuỗi thân gỗ liên kết",
    "task.maid_smart.organize": "Sắp Xếp Rương",
    "task.maid_smart.organize.desc": "Tự cất giữ các vật phẩm trong ba lô vào các rương chứa lân cận",
    "task.maid_smart.cook": "Nấu & Nung Đồ",
    "task.maid_smart.cook.desc": "Tiếp nhiên liệu và nạp vật phẩm vào lò nung / lò hun khói / lò luyện kim, thu gom thành phẩm",
    "task.maid_smart.brew": "Pha Chế Thuốc",
    "task.maid_smart.brew.desc": "Tiếp bột quỷ lửa và nguyên liệu vào giàn pha thuốc, thu gom độc dược",
    "task.maid_smart.build": "Xây Dựng",
    "task.maid_smart.build.desc": "Xây dựng công trình từng khối một theo bản thiết kế kiến trúc",
    "task.maid_smart.slaughter": "Mổ Thịt / Đồ Tể",
    "task.maid_smart.slaughter.desc": "Tự động giết động vật dư thừa trong trang trại khi số lượng vượt ngưỡng",
    "task.maid_smart.combat": "Tác Chiến Chuyên Nghiệp",
    "task.maid_smart.combat.desc": "Chiến đấu thông minh, tự động đổi vũ khí phù hợp và hỗ trợ chủ nhân",
    "itemGroup.maid_smart.main": "ProMaid",
    "config.promaid.combat.assistRadius": "Bán kính hỗ trợ chiến đấu (khối)",
    "config.promaid.combat.takeOverMovement": "Tiếp quản di chuyển chiến đấu",
    "config.promaid.broom.unstick": "Chổi bay: Tự gỡ khi bị kẹt",
    "config.promaid.broom.idleLand": "Chổi bay: Tự hạ cánh khi rảnh rỗi",
    "config.promaid.broom.followEnd": "Chổi bay: Khoảng cách dừng theo sau (khối)",
    "config.promaid.broom.followStart": "Chổi bay: Khoảng cách bắt đầu theo sau (khối)",
}

for k, v in promaid_en.items():
    if k in promaid_core_trans:
        promaid_vi[k] = promaid_core_trans[k]
    else:
        # Keep clean English as fallback for technical config keys
        promaid_vi[k] = v

ms_lang = os.path.join(vh_assets, "maid_smart", "lang")
os.makedirs(ms_lang, exist_ok=True)
with open(os.path.join(ms_lang, "vi_vn.json"), 'w', encoding='utf-8') as f:
    json.dump(promaid_vi, f, ensure_ascii=False, indent=2)
with open(os.path.join(ms_lang, "zh_cn.json"), 'w', encoding='utf-8') as f:
    json.dump(promaid_vi, f, ensure_ascii=False, indent=2)
print(f"Saved promaid translations ({len(promaid_vi)} keys)!")

# -------------------------------------------------------------
# STEP 3: REBUILD IMF-TRANS.ZIP & SYNC
# -------------------------------------------------------------
print("\n=== STEP 3: REBUILDING IMF-TRANS.ZIP ===")
trans_zip = os.path.join(base_dir, "resourcepacks", "IMF-Trans.zip")
tmp_zip = trans_zip + ".tmp"

injections = {
    "assets/maid_useful_task/lang/vi_vn.json": json.dumps(maid_useful_task_vi, ensure_ascii=False, indent=2).encode('utf-8'),
    "assets/maid_useful_task/lang/zh_cn.json": json.dumps(maid_useful_task_vi, ensure_ascii=False, indent=2).encode('utf-8'),
    "assets/maid_smart/lang/vi_vn.json": json.dumps(promaid_vi, ensure_ascii=False, indent=2).encode('utf-8'),
    "assets/maid_smart/lang/zh_cn.json": json.dumps(promaid_vi, ensure_ascii=False, indent=2).encode('utf-8')
}

with zipfile.ZipFile(trans_zip, 'r') as zin, zipfile.ZipFile(tmp_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        if item.filename not in injections:
            zout.writestr(item, zin.read(item.filename))
    for fname, data in injections.items():
        zout.writestr(fname, data)

os.replace(tmp_zip, trans_zip)
print("Updated IMF-Trans.zip with new maid addon translations!")

# Sync IMF-Trans.zip to game directory
shutil.copy2(trans_zip, os.path.join(game_dir, "resourcepacks", "IMF-Trans.zip"))
print("Synchronized IMF-Trans.zip to Game directory!")

print("\nINSTALLATION AND INTEGRATION OF MAID MODS COMPLETED!")
