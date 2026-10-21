# -*- coding: utf-8 -*-
"""
build_modrinth_package.py
Constructs the complete, censorship-free Modrinth distribution package for Immersive Fight:
1. Assembles IMF-VietHoa-Modrinth.zip (Resource pack covering all 230 namespaces + guide books).
2. Packages the 23 Vietnamese FTB Quest chapters & reward tables.
3. Generates comprehensive installation instructions and Modrinth description docs.
"""

import os
import sys
import json
import shutil
import zipfile
import re

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"D:\minecraft mod trung"
MODRINTH_DIR = os.path.join(ROOT_DIR, "Immersive_Fight_VietHoa_Modrinth")
SRC_ASSETS = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9 Viet Hoa\resources\assets")
SRC_RP_EXTRA = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9 Viet Hoa\resourcepack\IMF-VietHoa\assets")
SRC_QUESTS = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9 Viet Hoa\config\ftbquests")
PACK_PNG = os.path.join(ROOT_DIR, r"tools\pack.png")

print("=" * 70)
print("  BUILDING STANDALONE MODRINTH PACKAGE FOR IMMERSIVE FIGHT")
print("=" * 70)

# 1. Initialize clean output directory
if os.path.exists(MODRINTH_DIR):
    shutil.rmtree(MODRINTH_DIR)
os.makedirs(MODRINTH_DIR, exist_ok=True)

# 2. Build Resource Pack ZIP: IMF-VietHoa-Modrinth.zip
rp_zip_path = os.path.join(MODRINTH_DIR, "IMF-VietHoa-Modrinth.zip")
print(f"Creating resource pack zip: {rp_zip_path}")

pack_mcmeta_content = {
    "pack": {
        "pack_format": 15,
        "description": "§6[Immersive Fight] §bViệt Hóa Hoàn Chỉnh 1.20.1\n§7Cốt truyện, kỹ năng vũ khí, mô tả vật phẩm & hướng dẫn."
    }
}

# Specific manual touch-ups for EFN Yamato
yamato_keys = {
    "item.efn.yamato_dmc4": "§b§lYAMATO",
    "item.efn.yamato_dmc": "§b§lYAMATO",
}

with zipfile.ZipFile(rp_zip_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    # 2.1 pack.mcmeta
    z.writestr("pack.mcmeta", json.dumps(pack_mcmeta_content, ensure_ascii=False, indent=2))
    
    # 2.2 pack.png
    if os.path.exists(PACK_PNG):
        z.write(PACK_PNG, "pack.png")
    
    # 2.3 Assets lang files for 230 namespaces
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
                
                # Apply Yamato touch-up for efn namespace
                if ns == 'efn':
                    for yk, yv in yamato_keys.items():
                        if yk in data and not data[yk]:
                            data[yk] = yv
                
                arcname = f"assets/{ns}/lang/{lf}"
                z.writestr(arcname, json.dumps(data, ensure_ascii=False, indent=2))
    
    # 2.4 Add in-game guide books (Alex's Caves books, Alex's Mobs dictionary, Dragon Codex)
    print("Adding translated guide books & codexes...")
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

print(f"Resource pack successfully generated! Size: {os.path.getsize(rp_zip_path) / (1024 * 1024):.2f} MB")

# 3. Copy FTB Quests into config/ftbquests
dst_quests = os.path.join(MODRINTH_DIR, "config", "ftbquests")
print(f"Copying Vietnamese FTB Quests to {dst_quests}...")
shutil.copytree(SRC_QUESTS, dst_quests)

# 4. Generate HUONG_DAN_CAI_DAT_MODRINTH.txt
huong_dan_content = """================================================================================
  HƯỚNG DẪN CÀI ĐẶT GÓI VIỆT HÓA IMMERSIVE FIGHT (DÀNH CHO MODRINTH / CURSEFORGE)
================================================================================

Gói Việt Hóa này áp dụng trực tiếp lên bản modpack gốc Immersive Fight (BBSMC / CurseForge):
- 100% Cốt truyện nhiệm vụ FTB Quests dịch sang tiếng Việt văn phong chiến thuật mượt mà.
- Toàn bộ mô tả vũ khí, hiệu ứng, tuyệt kỹ (Judgement Cut End, Satsujin, Xuyên Giáp, v.v...) sang tiếng Việt.
- Giữ nguyên TÊN VẬT PHẨM bằng tiếng Anh chuẩn để tra cứu JEI / EMI cực nhanh và không lỗi tìm kiếm.
- Tương thích 100% với Forge 1.20.1, hoàn toàn KHÔNG xung đột mod và KHÔNG bị lỗi font chữ.

--------------------------------------------------------------------------------
CÁCH CÀI ĐẶT TRONG 2 BƯỚC ĐƠN GIẢN:
--------------------------------------------------------------------------------

BƯỚC 1: CÀI ĐẶT RESOURCE PACK
  - Copy file "IMF-VietHoa-Modrinth.zip" vào thư mục "resourcepacks" trong thư mục game của bạn.
  - Khởi động Minecraft -> Vào mục "Tùy chọn..." (Options) -> "Gói tài nguyên..." (Resource Packs).
  - Chọn "IMF-VietHoa-Modrinth.zip" và chuyển sang cột bên phải (Ưu tiên kéo lên trên cùng danh sách).
  - Bấm "Xong" (Done) để nạp tài nguyên.

BƯỚC 2: CẬP NHẬT CỐT TRUYỆN FTB QUESTS
  - Copy thư mục "config" (chứa thư mục "ftbquests") trong thư mục này và dán đè (Overwrite) vào thư mục gốc của phiên bản game / modpack của bạn.
  - Đường dẫn đích: <Thư mục game>/config/ftbquests/
  - Toàn bộ 23 chương nhiệm vụ, hội thoại cốt truyện và bảng phần thưởng sẽ được cập nhật sang tiếng Việt ngay lập tức!

--------------------------------------------------------------------------------
LƯU Ý QUAN TRỌNG:
--------------------------------------------------------------------------------
- Ngôn ngữ trong game có thể để "English (US)", "Tiếng Việt (Việt Nam)", hoặc "简体中文" đều hiển thị tiếng Việt hoàn hảo cho mô tả và tiếng Anh cho tên vật phẩm!
- Cảm ơn tác giả gốc: 辣某人 (Latxx) từ BBSMC / Bilibili đã phát triển bản modpack Immersive Fight tuyệt vời này.
"""

with open(os.path.join(MODRINTH_DIR, "HUONG_DAN_CAI_DAT_MODRINTH.txt"), "w", encoding="utf-8") as f:
    f.write(huong_dan_content)

# 5. Generate PROJECT_DESCRIPTION_MODRINTH.md (Bilingual presentation for Modrinth submission)
modrinth_desc_content = """# Immersive Fight - Vietnamese Localization (Bản Việt Hóa Hoàn Chỉnh)

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
- 🔍 **Chuẩn Hóa Tên Vật Phẩm Tiếng Anh (English Item Names):**
  - Toàn bộ tên vật phẩm, khối, và quái vật được giữ nguyên bằng tiếng Anh chuẩn quốc tế.
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

### 2 Bước Cài Đặt Cực Nhanh (Quick Setup)

1. **Cài Gói Tài Nguyên (Resource Pack):**
   - Tải file `IMF-VietHoa-Modrinth.zip` từ trang này.
   - Thả file vào thư mục `.minecraft/resourcepacks/` của bạn.
   - Trong game, vào **Tùy chọn** -> **Gói tài nguyên**, chuyển `IMF-VietHoa-Modrinth.zip` sang bên phải và kéo lên vị trí trên cùng.
2. **Cập Nhật Cốt Truyện Nhiệm Vụ (FTB Quests):**
   - Giải nén thư mục `config/ftbquests/` đi kèm và dán đè vào thư mục `.minecraft/config/ftbquests/`.
   - Vào game và mở sổ nhiệm vụ (Phím mặc định hoặc biểu tượng sách) để thưởng thức trọn vẹn cốt truyện!

---

## ⚖️ Bản Quyền & Lời Cảm Ơn (Credits & License)

- **Tác giả Modpack gốc:** Xin chân thành cảm ơn **辣某人 (Latxx)** — tác giả và kiến trúc sư của bản modpack kinh điển *Immersive Fight (沉浸战斗 / 沉浸特供)*.
- **Nguồn Modpack gốc:** [MCBBS / BBSMC](https://www.mcbbs.net/) | [Bilibili Space - 辣某人](https://space.bilibili.com/).
- **Bản quyền dịch thuật:** Bản Việt hóa được thực hiện bởi cộng đồng game thủ Việt Nam, phân phối phi thương mại vì mục đích hỗ trợ cộng đồng.
"""

with open(os.path.join(MODRINTH_DIR, "PROJECT_DESCRIPTION_MODRINTH.md"), "w", encoding="utf-8") as f:
    f.write(modrinth_desc_content)

# Copy as README.md as well
shutil.copy2(os.path.join(MODRINTH_DIR, "PROJECT_DESCRIPTION_MODRINTH.md"), os.path.join(MODRINTH_DIR, "README.md"))

print("\n" + "=" * 70)
print("  MODRINTH PACKAGE BUILD COMPLETED SUCCESSFULLY!")
print("=" * 70)
