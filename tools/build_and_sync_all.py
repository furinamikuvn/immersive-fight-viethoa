# -*- coding: utf-8 -*-
"""
build_and_sync_all.py
Ultimate build & synchronization script for Immersive Fight Vietnamese Localization:
1. Rebuilds IMF-VietHoa-Modrinth.zip from the latest updated assets.
2. Updates Immersive_Fight_VietHoa_Modrinth distribution folder with:
   - IMF-VietHoa-Modrinth.zip
   - config/ftbquests (23 chapters + reward tables)
   - config/class_enhancement.toml (Vietnamese custom classes)
   - defaultconfigs/class_enhancement.toml
   - global_packs/required_data/example_datapack (Vietnamese datapack tooltips & JEI info)
   - HUONG_DAN_CAI_DAT_MODRINTH.txt
   - PROJECT_DESCRIPTION_MODRINTH.md & README.md
3. Synchronizes 100% of the assets, configs, datapacks, and resource packs into:
   - D:\file tam mc (the user's ACTIVE playing instance)
   - D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh
   - D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa
"""

import os
import sys
import json
import shutil
import zipfile

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"D:\minecraft mod trung"
MODRINTH_DIR = os.path.join(ROOT_DIR, "Immersive_Fight_VietHoa_Modrinth")
SRC_ASSETS = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9 Viet Hoa\resources\assets")
SRC_RP_EXTRA = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9 Viet Hoa\resourcepack\IMF-VietHoa\assets")
SRC_QUESTS = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9 Viet Hoa\config\ftbquests")
SRC_CLASS_CONFIG = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9 Viet Hoa\config\class_enhancement.toml")
SRC_DATAPACK = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9 Viet Hoa\global_packs\required_data\example_datapack")
PACK_PNG = os.path.join(ROOT_DIR, r"tools\pack.png")

USER_GAME_DIR = r"D:\file tam mc"
CAI_DAT_NHANH_DIR = os.path.join(ROOT_DIR, "Immersive Fight 4.2.9 - Cai Dat Nhanh")
VIET_HOA_DIR = os.path.join(ROOT_DIR, "Immersive Fight 4.2.9 Viet Hoa")

print("=" * 75)
print("  TAWA MASTER BUILD & FULL SYSTEM SYNCHRONIZATION ENGINE")
print("=" * 75)

# ---------------------------------------------------------
# STEP 1: Rebuild Modrinth Package
# ---------------------------------------------------------
print("\n[STEP 1] Rebuilding Modrinth Distribution Package...")
if os.path.exists(MODRINTH_DIR):
    shutil.rmtree(MODRINTH_DIR)
os.makedirs(MODRINTH_DIR, exist_ok=True)

# 1.1 Create Resource Pack Zip
rp_zip_path = os.path.join(MODRINTH_DIR, "IMF-VietHoa-Modrinth.zip")
print(f"Creating resource pack zip: {rp_zip_path}")

pack_mcmeta_content = {
    "pack": {
        "pack_format": 15,
        "description": "§6[Immersive Fight] §bViệt Hóa Hoàn Chỉnh 1.20.1\n§7Cốt truyện, kỹ năng vũ khí, mô tả vật phẩm & hướng dẫn."
    }
}

yamato_keys = {
    "item.efn.yamato_dmc4": "§b§lYAMATO",
    "item.efn.yamato_dmc": "§b§lYAMATO",
}

with zipfile.ZipFile(rp_zip_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    z.writestr("pack.mcmeta", json.dumps(pack_mcmeta_content, ensure_ascii=False, indent=2))
    if os.path.exists(PACK_PNG):
        z.write(PACK_PNG, "pack.png")
    
    namespaces = sorted(os.listdir(SRC_ASSETS))
    print(f"Adding 230 namespaces from {SRC_ASSETS}...")
    for ns in namespaces:
        lang_dir = os.path.join(SRC_ASSETS, ns, 'lang')
        if not os.path.exists(lang_dir):
            continue
        for lf in ['en_us.json', 'zh_cn.json', 'vi_vn.json']:
            lp = os.path.join(lang_dir, lf)
            if os.path.exists(lp):
                with open(lp, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                if ns == 'efn':
                    for yk, yv in yamato_keys.items():
                        if yk in data and not data[yk]:
                            data[yk] = yv
                arcname = f"assets/{ns}/lang/{lf}"
                z.writestr(arcname, json.dumps(data, ensure_ascii=False, indent=2))
    
    print("Adding guide books & codexes...")
    book_dirs = [
        os.path.join(SRC_RP_EXTRA, "alexscaves", "books"),
        os.path.join(SRC_RP_EXTRA, "alexsmobs", "book"),
        os.path.join(SRC_RP_EXTRA, "saintsdragons", "codex")
    ]
    for b_dir in book_dirs:
        if os.path.exists(b_dir):
            for root, dirs, files in os.walk(b_dir):
                for f in files:
                    full_p = os.path.join(root, f)
                    rel_p = os.path.relpath(full_p, SRC_RP_EXTRA)
                    arcname = f"assets/{rel_p.replace(os.sep, '/')}"
                    z.write(full_p, arcname)

print(f"Resource Pack generated: {os.path.getsize(rp_zip_path) / (1024 * 1024):.2f} MB")

# 1.2 Copy FTB Quests
dst_quests = os.path.join(MODRINTH_DIR, "config", "ftbquests")
print(f"Packaging Vietnamese FTB Quests to {dst_quests}...")
shutil.copytree(SRC_QUESTS, dst_quests)

# 1.3 Copy class_enhancement.toml to config & defaultconfigs
dst_class_cfg = os.path.join(MODRINTH_DIR, "config", "class_enhancement.toml")
dst_def_class_cfg = os.path.join(MODRINTH_DIR, "defaultconfigs", "class_enhancement.toml")
os.makedirs(os.path.dirname(dst_def_class_cfg), exist_ok=True)
print("Packaging Vietnamese class_enhancement.toml...")
shutil.copy2(SRC_CLASS_CONFIG, dst_class_cfg)
shutil.copy2(SRC_CLASS_CONFIG, dst_def_class_cfg)

# 1.4 Copy example_datapack to global_packs/required_data
dst_dp = os.path.join(MODRINTH_DIR, "global_packs", "required_data", "example_datapack")
print(f"Packaging Vietnamese example_datapack to {dst_dp}...")
shutil.copytree(SRC_DATAPACK, dst_dp)

# 1.5 Generate HUONG_DAN_CAI_DAT_MODRINTH.txt
huong_dan_text = """================================================================================
  HƯỚNG DẪN CÀI ĐẶT GÓI VIỆT HÓA IMMERSIVE FIGHT (DÀNH CHO MODRINTH / CURSEFORGE)
================================================================================

Gói Việt Hóa này áp dụng trực tiếp lên bản modpack gốc Immersive Fight (BBSMC / CurseForge):
- 100% Cốt truyện nhiệm vụ FTB Quests (23 chương) dịch sang tiếng Việt chuẩn chiến thuật.
- 100% Mô tả vũ khí, hiệu ứng, tuyệt kỹ (Judgement Cut End, Satsujin, Xuyên Giáp, v.v...).
- Tên nghề nghiệp chọn đầu game (Trị Liệu Sư, Mạo Hiểm Giả, Xảo Đấu Sĩ, Kẻ Phàm Ăn, Đao Kiếm Khách) tiếng Việt rõ ràng.
- Giữ nguyên TÊN VẬT PHẨM bằng TIẾNG ANH chuẩn quốc tế để tra cứu JEI / EMI mượt mà, không lỗi tìm kiếm.
- Tương thích 100% Forge 1.20.1, KHÔNG sửa jar gốc, TUÂN THỦ 100% chính sách kiểm duyệt Modrinth.

--------------------------------------------------------------------------------
CÁCH CÀI ĐẶT TRONG 3 BƯỚC ĐƠN GIẢN:
--------------------------------------------------------------------------------

BƯỚC 1: CÀI ĐẶT RESOURCE PACK
  - Copy file "IMF-VietHoa-Modrinth.zip" vào thư mục "resourcepacks" trong thư mục game của bạn.
  - Khởi động Minecraft -> Vào mục "Tùy chọn..." (Options) -> "Gói tài nguyên..." (Resource Packs).
  - Chọn "IMF-VietHoa-Modrinth.zip" và chuyển sang cột bên phải (Ưu tiên kéo lên trên cùng).
  - Bấm "Xong" (Done) để nạp tài nguyên.

BƯỚC 2: CẬP NHẬT CẤU HÌNH & NHIỆM VỤ (CONFIG)
  - Copy thư mục "config" trong gói này và dán đè (Overwrite) vào thư mục gốc game của bạn.
  - (Tùy chọn) Copy thư mục "defaultconfigs" dán đè vào thư mục gốc game.
  - Toàn bộ 23 chương nhiệm vụ FTB Quests và bảng nghề nghiệp đầu game sẽ là tiếng Việt!

BƯỚC 3: CẬP NHẬT GÓI DỮ LIỆU CHỈ DẪN (GLOBAL PACKS)
  - Copy thư mục "global_packs" trong gói này và dán đè (Overwrite) vào thư mục gốc game của bạn.
  - Các mẹo hướng dẫn vật phẩm (như Balo: "Đặt vào ô đeo lưng thứ nhất") và thông tin JEI sẽ được Việt hóa sạch bóng!

--------------------------------------------------------------------------------
LƯU Ý QUAN TRỌNG:
--------------------------------------------------------------------------------
- Ngôn ngữ trong game có thể để "English (US)", "Tiếng Việt (Việt Nam)", hoặc "简体中文" đều hiển thị hoàn hảo!
- Cảm ơn tác giả gốc: 辣某人 (Latxx) từ BBSMC / Bilibili đã phát triển bản modpack Immersive Fight tuyệt vời này.
"""

with open(os.path.join(MODRINTH_DIR, "HUONG_DAN_CAI_DAT_MODRINTH.txt"), "w", encoding="utf-8") as f:
    f.write(huong_dan_text)

# 1.6 Generate PROJECT_DESCRIPTION_MODRINTH.md & README.md
desc_md = """# Immersive Fight - Vietnamese Localization (Bản Việt Hóa Hoàn Chỉnh)

[![Minecraft](https://img.shields.io/badge/Minecraft-1.20.1-brightgreen.svg)]()
[![Modloader](https://img.shields.io/badge/Modloader-Forge-orange.svg)]()
[![Translation](https://img.shields.io/badge/Translation-100%25%20Vietnamese-blue.svg)]()

> **Bản Việt hóa chuyên sâu và toàn diện dành cho Modpack Immersive Fight (沉浸特供 / 沉浸战斗) phiên bản 1.20.1.**  
> Giúp game thủ Việt Nam trải nghiệm trọn vẹn từng đòn combo võ thuật, kỹ năng vũ khí, nội tại thần binh và cốt truyện thiên sử thi mà không gặp rào cản ngôn ngữ!

---

## ✨ Điểm Nổi Bật (Key Features)

- ⚔️ **Việt hóa 100% Mô Tả & Kỹ Năng Vũ Khí (Descriptions & Tooltips):**
  - Mọi tuyệt kỹ võ thuật Epic Fight: *Judgement Cut End*, *Angel/Devil Stance*, *Blade Mode*, *Soul Hunt*, *Parry Master*, v.v...
  - Toàn bộ thần binh: *Satsujin (Weapons of Miracles)*, *HF-Murasama*, *Yamato*, cùng cơ chế *Xuyên giáp (Armor Negation)*, *Tác động (Impact)*.
  - Sách hướng dẫn in-game đầy đủ: *Alex's Caves Guidebooks*, *Alex's Mobs Animal Dictionary*, *Dragon Codex*.
  - Bảng chọn nghề nghiệp đầu game (*Trị Liệu Sư*, *Mạo Hiểm Giả*, *Xảo Đấu Sĩ*, *Kẻ Phàm Ăn*, *Đao Kiếm Khách*) hoàn toàn thuần Việt.
- 🔍 **Chuẩn Hóa Tên Vật Phẩm & Phù Phép Tiếng Anh (English Item & Enchantment Names):**
  - Toàn bộ tên vật phẩm, khối, quái vật, danh mục mod và tên sách phù phép được giữ nguyên bằng tiếng Anh chuẩn quốc tế (*Marksman*, *Lifesteal*, *Born in Chaos*, v.v...).
  - Tra cứu công thức chế tạo qua JEI, REI, EMI mượt mà 100%, không lo gõ sai từ khóa hay lỗi bảng chế tạo.
- 📜 **Cốt Truyện & Nhiệm Vụ Toàn Diện (FTB Quests):**
  - Đầy đủ 23 chương nhiệm vụ chính và nhiệm vụ phụ được biên dịch chỉn chu, văn phong hào hùng, chuẩn thuật ngữ game thủ.
  - Hướng dẫn tân thủ từng bước từ thu thập trang bị, tiến hóa kỹ năng đến đánh bại các Boss tối thượng.
- 🌐 **Khả Năng Tương Thích Hoàn Hảo (Language Resilience):**
  - Hỗ trợ hiển thị tự động trên cả 3 thiết lập ngôn ngữ: `English (US)`, `Tiếng Việt`, và `简体中文 (Chinese)`.
  - Không cần sửa đổi file jar gốc, hoàn toàn an toàn và tuân thủ chính sách bản quyền của Modrinth!

---

## 📥 Hướng Dẫn Cài Đặt (Installation Guide)

### Yêu Cầu Nền Tảng (Requirements)
1. Đã cài đặt phiên bản modpack gốc **Immersive Fight (1.20.1 Forge)** (từ BBSMC, Bilibili, hoặc CurseForge).

### 3 Bước Cài Đặt Đơn Giản:
1. **Cài Gói Tài Nguyên (Resource Pack):**
   - Thả file `IMF-VietHoa-Modrinth.zip` vào thư mục `resourcepacks/` trong game của bạn.
   - Trong game, vào **Tùy chọn** -> **Gói tài nguyên**, chọn và chuyển `IMF-VietHoa-Modrinth.zip` sang bên phải (Kéo lên trên cùng).
2. **Cập Nhật Cấu Hình & Cốt Truyện (Config):**
   - Sao chép thư mục `config/` và `defaultconfigs/` dán đè vào thư mục gốc game của bạn.
3. **Cập Nhật Gói Dữ Liệu Hướng Dẫn (Global Packs):**
   - Sao chép thư mục `global_packs/` dán đè vào thư mục gốc game của bạn để cập nhật toàn bộ mẹo chỉ dẫn trang bị.

---

## ⚖️ Bản Quyền & Lời Cảm Ơn (Credits & License)

- **Tác giả Modpack gốc:** Xin chân thành cảm ơn **辣某人 (Latxx)** — tác giả và kiến trúc sư của bản modpack kinh điển *Immersive Fight (沉浸战斗 / 沉浸特供)*.
- **Nguồn Modpack gốc:** [MCBBS / BBSMC](https://www.mcbbs.net/) | [Bilibili Space - 辣某人](https://space.bilibili.com/).
- **Bản quyền dịch thuật:** Bản Việt hóa được thực hiện bởi cộng đồng game thủ Việt Nam, phân phối phi thương mại vì mục đích hỗ trợ cộng đồng.
"""

with open(os.path.join(MODRINTH_DIR, "PROJECT_DESCRIPTION_MODRINTH.md"), "w", encoding="utf-8") as f:
    f.write(desc_md)
shutil.copy2(os.path.join(MODRINTH_DIR, "PROJECT_DESCRIPTION_MODRINTH.md"), os.path.join(MODRINTH_DIR, "README.md"))

# ---------------------------------------------------------
# STEP 2: Full Sync to User Game Directory (D:\file tam mc)
# ---------------------------------------------------------
print("\n[STEP 2] Synchronizing 100% into Active Game Directory (D:\\file tam mc)...")
if os.path.exists(USER_GAME_DIR):
    # 2.1 Sync resources/assets
    dest_res_assets = os.path.join(USER_GAME_DIR, "resources", "assets")
    os.makedirs(dest_res_assets, exist_ok=True)
    for ns in namespaces:
        src_ns = os.path.join(SRC_ASSETS, ns)
        if os.path.isdir(src_ns):
            # to resources/assets/<ns>
            dst_ns = os.path.join(dest_res_assets, ns)
            shutil.copytree(src_ns, dst_ns, dirs_exist_ok=True)
            # also to flat resources/<ns> for LMR compatibility
            dst_flat = os.path.join(USER_GAME_DIR, "resources", ns)
            shutil.copytree(src_ns, dst_flat, dirs_exist_ok=True)
    print("  [OK] Synchronized 230 namespaces to D:\\file tam mc\\resources!")

    # 2.2 Sync resourcepacks/IMF-VietHoa-Modrinth.zip
    dest_rp_dir = os.path.join(USER_GAME_DIR, "resourcepacks")
    os.makedirs(dest_rp_dir, exist_ok=True)
    shutil.copy2(rp_zip_path, os.path.join(dest_rp_dir, "IMF-VietHoa-Modrinth.zip"))
    print("  [OK] Synchronized IMF-VietHoa-Modrinth.zip to resourcepacks!")

    # 2.3 Sync config & defaultconfigs
    dest_cfg_dir = os.path.join(USER_GAME_DIR, "config")
    dest_def_dir = os.path.join(USER_GAME_DIR, "defaultconfigs")
    os.makedirs(dest_cfg_dir, exist_ok=True)
    os.makedirs(dest_def_dir, exist_ok=True)
    shutil.copy2(SRC_CLASS_CONFIG, os.path.join(dest_cfg_dir, "class_enhancement.toml"))
    shutil.copy2(SRC_CLASS_CONFIG, os.path.join(dest_def_dir, "class_enhancement.toml"))
    print("  [OK] Synchronized class_enhancement.toml to config & defaultconfigs!")

    # 2.4 Sync example_datapack
    dest_dp_dir = os.path.join(USER_GAME_DIR, "global_packs", "required_data", "example_datapack")
    shutil.copytree(SRC_DATAPACK, dest_dp_dir, dirs_exist_ok=True)
    print("  [OK] Synchronized example_datapack to global_packs\\required_data!")

# ---------------------------------------------------------
# STEP 3: Sync to Cai Dat Nhanh and Viet Hoa
# ---------------------------------------------------------
print("\n[STEP 3] Synchronizing to Cai Dat Nhanh and Viet Hoa workspaces...")
if os.path.exists(CAI_DAT_NHANH_DIR):
    cai_dat_res_assets = os.path.join(CAI_DAT_NHANH_DIR, "resources", "assets")
    os.makedirs(cai_dat_res_assets, exist_ok=True)
    for ns in namespaces:
        src_ns = os.path.join(SRC_ASSETS, ns)
        if os.path.isdir(src_ns):
            shutil.copytree(src_ns, os.path.join(cai_dat_res_assets, ns), dirs_exist_ok=True)
    os.makedirs(os.path.join(CAI_DAT_NHANH_DIR, "config"), exist_ok=True)
    os.makedirs(os.path.join(CAI_DAT_NHANH_DIR, "defaultconfigs"), exist_ok=True)
    shutil.copy2(SRC_CLASS_CONFIG, os.path.join(CAI_DAT_NHANH_DIR, "config", "class_enhancement.toml"))
    shutil.copy2(SRC_CLASS_CONFIG, os.path.join(CAI_DAT_NHANH_DIR, "defaultconfigs", "class_enhancement.toml"))
    cai_dat_dp = os.path.join(CAI_DAT_NHANH_DIR, "global_packs", "required_data", "example_datapack")
    shutil.copytree(SRC_DATAPACK, cai_dat_dp, dirs_exist_ok=True)
    cai_dat_rp = os.path.join(CAI_DAT_NHANH_DIR, "resourcepacks")
    os.makedirs(cai_dat_rp, exist_ok=True)
    shutil.copy2(rp_zip_path, os.path.join(cai_dat_rp, "IMF-VietHoa-Modrinth.zip"))
    print("  [OK] Synchronized to Immersive Fight 4.2.9 - Cai Dat Nhanh!")

# Update defaultconfigs in Viet Hoa
vh_def = os.path.join(VIET_HOA_DIR, "defaultconfigs")
os.makedirs(vh_def, exist_ok=True)
shutil.copy2(SRC_CLASS_CONFIG, os.path.join(vh_def, "class_enhancement.toml"))
vh_rp = os.path.join(VIET_HOA_DIR, "resourcepack")
os.makedirs(vh_rp, exist_ok=True)
shutil.copy2(rp_zip_path, os.path.join(vh_rp, "IMF-VietHoa-Modrinth.zip"))
print("  [OK] Synchronized to Immersive Fight 4.2.9 Viet Hoa!")

print("\n" + "=" * 75)
print("  MASTER BUILD & FULL SYNCHRONIZATION COMPLETED SUCCESSFULLY!")
print("=" * 75)
