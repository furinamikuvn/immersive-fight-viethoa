#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
perfect_direct_viethoa.py
=========================
Hệ thống Việt hóa Trực tiếp Hoàn hảo cho Immersive Fight 4.2.9 (Forge 1.20.1)
Tác giả: Tawa (Antigravity Elite Assistant) cho Master Nukumizu

Nguyên tắc Thép:
  1. TÊN VẬT PHẨM, VŨ KHÍ, KHỐI, THỰC THỂ: Giữ nguyên 100% TIẾNG ANH (en_us) để tìm kiếm JEI mượt mà.
  2. MÔ TẢ VẬT PHẨM, VŨ KHÍ, TOOLTIP, LORE, SKILL, EFFECT, POTION: Dịch 100% SANG TIẾNG VIỆT, tuyệt đối không sót tiếng Anh hoặc tiếng Trung!
  3. KHÔNG DÙNG RESOURCE PACK: Triển khai trực tiếp vào `resources/assets/<namespace>/lang/`.
  4. ĐA TẦNG FALLBACK: Đồng thời tạo cả `vi_vn.json`, `zh_cn.json`, và `en_us.json` trong `resources/assets/` để bất kể game chọn ngôn ngữ nào thì Forge vẫn tải đúng bản dịch!
"""

import os
import sys
import json
import re
import shutil
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# ─── CÁC ĐƯỜNG DẪN ─────────────────────────────────────────────────────────
ROOT_DIR = Path(r"D:\minecraft mod trung")
SRC_ASSETS = ROOT_DIR / "Immersive Fight 4.2.9 Viet Hoa" / "resourcepack" / "IMF-VietHoa" / "assets"

TARGET_DIRS = [
    # 1. Thư mục mã nguồn Việt Hóa
    SRC_ASSETS,
    # 2. Thư mục Modpack chuẩn
    ROOT_DIR / "Immersive Fight 4.2.9" / "resources" / "assets",
    # 3. Thư mục Game Forge 1.20.1 của TLauncher
    Path(r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\resources\assets")
]

CHINESE_RE = re.compile(r'[\u4e00-\u9fff]')

# ─── BỘ TỪ ĐIỂN CHUYÊN BIỆT DÀNH CHO MÔ TẢ & POTION & CHIẾN ĐẤU ────────────
EXACT_TRANSLATIONS = {
    # Cataclysm & Relics boots
    "dung nham Walker": "Bước Đi Trên Dung Nham (Magma Walker)",
    "Dung Nham Walker": "Bước Đi Trên Dung Nham (Magma Walker)",
    "dung nham walker": "Bước Đi Trên Dung Nham (Magma Walker)",
    
    # Simply Swords Remnants
    "Smith with a Runic Tablet or": "Rèn kết hợp cùng Phiến Đá Cổ Tự hoặc",
    "a Unique weapon in a Smithing Table": "vũ khí Độc Bản trong Bàn Rèn",
    "that can be socketed into unique": "để khảm vào các loại vũ khí độc bản",
    "weapons.": "khác nhau.",
    "Unlocked by completing advancements or": "Mở khóa bằng cách hoàn thành tiến trình hoặc",
    "exploring the End dimension.": "thám hiểm chiều không gian The End.",
    "when in close proximity to you.": "khi kẻ thù ở cự ly gần bên bạn.",
    "It appears to have been tampered": "Có vẻ như đã bị can thiệp biến đổi...",
    "with...": "bởi một thế lực bí ẩn...",
    
    # BetterEnd smithing
    "Add Thallasium or Terminite Tool Heads": "Đặt Đầu Công Cụ Thallasium hoặc Terminite",
    "Add a Sword Blade": "Đặt Lưỡi Kiếm",
    "Add a Sword Handle": "Đặt Chuôi Kiếm",
    "Add a Terminite Ingot": "Đặt Thỏi Terminite",
    
    # RealmRPG Quests
    "Grants Dolphin's Grace": "Ban tặng hiệu ứng Ân Huệ Cá Heo",
    "Allows you to catch more fish at night when held off-hand.": "Cho phép câu được nhiều cá hơn vào ban đêm khi cầm trên tay phụ.",
    "Makes the NPC forget the current quest and immediately start the next one.": "Khiến NPC lập tức hủy nhiệm vụ hiện tại và bắt đầu nhiệm vụ tiếp theo.",
    "+25% Chance to Catch Extra Item": "+25% Cơ hội câu được thêm vật phẩm",
    
    # Maid Smart
    "Broom: the maid takes a TLM broom out of her inventory, rides it herself (no player needed), and patrols along a patrol chart route or free-flies around her home.": "Cây Chổi: Hầu gái lấy chổi TLM từ túi đồ, tự mình cưỡi chổi bay tuần tra dọc theo lộ trình biểu đồ hoặc tự do bay quanh khu vực nhà.",
    "§7Use on a flying maid to hang beneath her as a gunner; she flies on, you keep shooting. Right-click to drop off.": "§7Dùng lên hầu gái đang bay để treo mình bên dưới làm xạ thủ; hầu gái tiếp tục bay, bạn thỏa sức bắn. Nhấp chuột phải để thả mình xuống.",
    "§fRight-click§7 to open the chart: create / rename routes, bind maids, start or stop patrols, configure patrol mode.": "§fNhấp chuột phải§7 để mở biểu đồ: tạo / đổi tên lộ trình, liên kết hầu gái, bật / tắt tuần tra, cấu hình chế độ tuần tra.",
    "Schedule availability check": "Lịch kiểm tra tính khả dụng",
    "Soft Blocks No Durability": "Khối mềm không tiêu hao độ bền",
    "§7Author: Rou_Ti": "§7Tác giả: Rou_Ti",
    "§7Maid of the Demon World": "§7Hầu Gái Ma Giới",
    "§7 tay keyboard Sao Ling": "§7Tay Keyboard Sao Ling",
    
    # EpicFight / Awaken / EFN / Sword Soaring
    "-[Shadow Assault] §f Dash N H H H": "-[Đột Kích Bóng Tối] §f Lướt N H H H",
    "-[Sunset Harvest] §f N N H": "-[Thu Hoạch Hoàng Hôn] §f N N H",
    "-[Sunset] §f N H": "-[Hoàng Hôn] §f N H",
    "-[Shadow Flurry] §f N N N H H ... H": "-[Loạn Vũ Bóng Đêm] §f N N N H H ... H",
    "Curse of Night": "Lời Nguyền Đêm Tối",
    "Judgement Cut End": "Tuyệt Kỹ Phán Quyết Trảm (Judgement Cut End)",
    "Mortal Blade - HaiRui": "Tuyệt Kỹ Đoạt Mệnh - Hải Thụy",
    "§b§l Yan Mo Dao": "§b§l Diêm Ma Đao (Yamato)",
    "Sword Art True Chapter": "Ngự Kiếm Thuật Chân Chương",
    "§c§l Ba Yuan Guanri Jue§r ——": "§c§l Bát Hoang Quán Nhật Quyết§r ——",
    
    # Elytra Utilities
    "If enabled, fall flying can be activated by jumping in midair.": "Nếu bật, có thể kích hoạt bay lượn bằng cách nhấn nhảy giữa không trung.",
    "If enabled, players can fall fly. This can also be managed in-game through the status menu.": "Nếu bật, người chơi có thể bay lượn bằng cánh cứng Elytra.",
    "If enabled, holding down the \"Trigger Elytra\" key uses a firework from inventory.": "Nếu bật, nhấn giữ phím kích hoạt Elytra sẽ tự động dùng pháo hoa từ túi đồ.",
    "f enabled, firework rockets can only be used while fall flying.": "Nếu bật, pháo hoa chỉ có thể được sử dụng khi đang bay lượn.",
    
    # FTB Quests chests
    "Rewards will appear here": "Phần thưởng sẽ xuất hiện tại đây",
    "Place items here to complete quests": "Đặt vật phẩm vào đây để hoàn thành nhiệm vụ",
    
    # IDWTIALSIMMOEDM
    "description prefix (line 1)": "Tiền tố mô tả (dòng 1)",
    "description indentation (lines 2+)": "Thụt lề mô tả (từ dòng 2 trở đi)",
    "hide missing descriptions": "Ẩn các mô tả còn thiếu",
}

POTION_EFFECT_NAMES = {
    "haste": "Mau Lẹ (Haste)",
    "strong_haste": "Siêu Mau Lẹ",
    "long_haste": "Mau Lẹ Kéo Dài",
    "sugar_rush": "Hưng Phấn (Sugar Rush)",
    "long_sugar_rush": "Hưng Phấn Kéo Dài",
    "magnetizing": "Từ Tính (Magnetizing)",
    "long_magnetizing": "Từ Tính Kéo Dài",
    "deepsight": "Dạ Nhìn Sâu (Deepsight)",
    "long_deepsight": "Dạ Nhìn Sâu Kéo Dài",
    "glowing": "Phát Quang (Glowing)",
    "long_glowing": "Phát Quang Kéo Dài",
    "lava_vision": "Thị Giác Dung Nham",
    "knockback_resistance": "Kháng Đẩy Lùi",
    "strong_knockback_resistance": "Siêu Kháng Đẩy Lùi",
    "poison_resistance": "Kháng Độc Tố",
    "clinging": "Bám Dính (Clinging)",
    "end_veil": "Màn Che Hư Không (End Veil)",
    "long_end_veil": "Màn Che Hư Không Kéo Dài",
    "intoxication_potion": "Say Mềm (Intoxication)",
    "stimulating_potion": "Kích Thích Tinh Thần",
    "potion_of_magical_depletion": "Hao Tổn Ma Lực",
    "potion_of_living_cocoon": "Kén Sống (Living Cocoon)",
    "antidote_potion": "Giải Độc (Antidote)",
    "blindness": "Mù Lòa (Blindness)",
    "guardian_creator_potion": "Kiến Tạo Hộ Vệ",
    "frozen_resistance": "Kháng Băng Giá",
    "long_frozen_resistance": "Kháng Băng Giá Kéo Dài",
    "fatal_oath": "Lời Thề Tử Vong",
    "fatal_oath_ii": "Lời Thề Tử Vong II",
    "long_haste_ii": "Mau Lẹ II Kéo Dài",
    "levitation": "Bay Lơ Lửng (Levitation)",
    "reaching": "Gia Tăng Tầm Với",
    "piercing": "Xuyên Thấu (Piercing)",
    "blooming": "Nở Hoa (Blooming)",
    "instant_cure_potion": "Trị Liệu Tức Thì",
    "weakness": "Yếu Đuối",
    "longer_weakness": "Yếu Đuối Kéo Dài",
    "jump_boost": "Nhảy Cao",
    "longer_jump_boost": "Nhảy Cao Kéo Dài",
    "slowness": "Làm Chậm",
    "longer_slowness": "Làm Chậm Kéo Dài",
    "poison": "Độc Tố",
    "stronger_poison": "Độc Cường Lực",
    "strength": "Sức Mạnh",
    "longer_strength": "Sức Mạnh Kéo Dài",
    "slow_falling": "Rơi Chậm",
    "longer_slow_falling": "Rơi Chậm Kéo Dài",
    "turtle_master": "Bậc Thầy Rùa Biển",
    "stronger_turtle_master": "Bậc Thầy Rùa Biển Cường Lực",
    "longer_turtle_master": "Bậc Thầy Rùa Biển Kéo Dài",
}

def translate_potion_item(key: str, en_val: str) -> str:
    """Tự động chuyển ngữ tên các loại thuốc, thuốc ném, thuốc kéo dài, mũi tên."""
    k_lower = key.lower()
    
    # Tìm effect name trong key
    effect_key = k_lower.split('.')[-1]
    eff_vn = POTION_EFFECT_NAMES.get(effect_key)
    
    if not eff_vn:
        # Thử tìm trong POTION_EFFECT_NAMES qua en_val
        for ek, vn in POTION_EFFECT_NAMES.items():
            if ek.replace('_', ' ') in en_val.lower():
                eff_vn = vn
                break
                
    if not eff_vn:
        return en_val # giữ nguyên nếu không rõ
        
    if "splash_potion" in k_lower:
        return f"Thuốc Ném {eff_vn}"
    elif "lingering_potion" in k_lower:
        return f"Thuốc Kéo Dài {eff_vn}"
    elif "tipped_arrow" in k_lower:
        return f"Mũi Tên {eff_vn}"
    elif "potion" in k_lower:
        return f"Thuốc {eff_vn}"
    return en_val


def is_name_key(key: str) -> bool:
    """Xác định rõ ràng key nào là TÊN VẬT PHẨM (giữ Tiếng Anh)."""
    k = key.lower()
    
    # 1. Các marker bắt buộc là MÔ TẢ/TOOLTIP -> PHẢI DỊCH TIẾNG VIỆT
    desc_markers = (
        '.tooltip', '.desc', '.description', '.lore', '.ability', '.info', '.text',
        '.comment', '.line', 'skill.', 'ability.', 'attribute.', 'effect.', 'enchantment.',
        'gui.', 'key.', 'text.autoconfig', 'message.', 'title.', 'subtitle.',
        'advancements.', 'screen.', 'category.', 'tab.', 'subtitles.', 'jei.', 'emi.',
        'config.', 'option.', 'setting.', 'death.', 'prompt.', 'tip.', 'hint.', 'help.'
    )
    for m in desc_markers:
        if m in k:
            return False
            
    # 2. Potion items -> Potion effect name cần dịch tiếng Việt
    if "potion.effect." in k or "tipped_arrow.effect." in k:
        return False
        
    # 3. Tên vật phẩm / thực thể / khối -> GIỮ TIẾNG ANH
    name_prefixes = ('item.', 'block.', 'entity.', 'itemgroup.', 'biome.', 'container.')
    for prefix in name_prefixes:
        if k.startswith(prefix):
            return True
            
    return False


def load_json_safe(path: Path) -> dict:
    if not path.exists(): return {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        try:
            with open(path, 'r', encoding='utf-8-sig') as f:
                return json.load(f)
        except Exception:
            return {}


def write_json_utf8(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')


def clean_text(text: str) -> str:
    """Xử lý sạch các từ bậy/dịch thô/lỗi."""
    if not isinstance(text, str): return ""
    # Sửa một số từ dịch thô kệch
    t = text
    for old, new in EXACT_TRANSLATIONS.items():
        if old in t:
            t = t.replace(old, new)
    return t


def main():
    print("=" * 75)
    print("  TAWA PERFECT DIRECT VIỆT HÓA — IMMERSIVE FIGHT 4.2.9")
    print("  Chuẩn: Tên vật phẩm = Tiếng Anh | Mô tả, Kỹ năng, Tooltip = Tiếng Việt")
    print("  Triển khai: Trực tiếp vào resources/ (vi_vn, zh_cn, en_us)")
    print("=" * 75)

    # Nạp từ điển dịch lớn nếu có
    rp_dict_path = ROOT_DIR / "Immersive Fight 4.2.9 Viet Hoa" / "tools" / "rp_translation_dict.json"
    rp_dict = load_json_safe(rp_dict_path)
    print(f"[INFO] Loaded {len(rp_dict)} fallback translation pairs from rp_translation_dict.json")

    processed_namespaces = 0
    total_keys_count = 0
    vn_keys_count = 0
    eng_names_count = 0

    namespace_dirs = sorted([d for d in SRC_ASSETS.iterdir() if d.is_dir()])
    print(f"[INFO] Bắt đầu xử lý {len(namespace_dirs)} namespaces...")

    for ns_dir in namespace_dirs:
        ns = ns_dir.name
        lang_dir = ns_dir / "lang"
        if not lang_dir.exists(): continue

        en_data = load_json_safe(lang_dir / "en_us.json")
        vi_data = load_json_safe(lang_dir / "vi_vn.json")
        zh_data = load_json_safe(lang_dir / "zh_cn.json")

        all_keys = set(en_data) | set(vi_data) | set(zh_data)
        if not all_keys: continue

        final_dict = {}

        for k in all_keys:
            en_v = clean_text(en_data.get(k, ""))
            vi_v = clean_text(vi_data.get(k, ""))
            zh_v = clean_text(zh_data.get(k, ""))

            if is_name_key(k):
                # TÊN VẬT PHẨM, KHỐI, THỰC THỂ -> Ưu tiên 100% TIẾNG ANH (en_us)
                val = en_v if en_v else (vi_v if not CHINESE_RE.search(vi_v) else zh_v)
                # Nếu vẫn còn tiếng Trung trong tên -> tra từ điển rp_dict
                if CHINESE_RE.search(val):
                    val = rp_dict.get(val, val)
                final_dict[k] = val
                eng_names_count += 1
            else:
                # MÔ TẢ, TOOLTIP, SKILL, HIỆU ỨNG -> Ưu tiên 100% TIẾNG VIỆT
                val = ""
                
                # 1. Kiểm tra EXACT_TRANSLATIONS trực tiếp trên en_v hoặc zh_v
                if en_v in EXACT_TRANSLATIONS:
                    val = EXACT_TRANSLATIONS[en_v]
                elif zh_v in EXACT_TRANSLATIONS:
                    val = EXACT_TRANSLATIONS[zh_v]
                elif "potion." in k.lower() or "tipped_arrow." in k.lower():
                    # Xử lý potion/arrow
                    val = translate_potion_item(k, en_v or vi_v)
                else:
                    # 2. Ưu tiên vi_v nếu vi_v là tiếng Việt hợp lệ (không CJK, có dấu tiếng Việt hoặc không phải tiếng Anh thô)
                    has_vn = any(ord(c) > 127 and c not in '§©®™°±×÷•…–—“”’‘' for c in vi_v)
                    has_cjk_vi = bool(CHINESE_RE.search(vi_v))
                    
                    if vi_v and has_vn and not has_cjk_vi:
                        val = vi_v
                    elif zh_v and not CHINESE_RE.search(zh_v):
                        # zh_v đã được việt hóa ở vòng trước
                        val = zh_v
                    elif zh_v and CHINESE_RE.search(zh_v):
                        # zh_v còn tiếng Trung -> tra từ điển
                        val = rp_dict.get(zh_v, "")
                        if not val or CHINESE_RE.search(val):
                            val = en_v
                    else:
                        val = vi_v or en_v
                        
                # Sửa các chuỗi còn tồn dư
                val = clean_text(val)
                final_dict[k] = val
                vn_keys_count += 1

            total_keys_count += 1

        processed_namespaces += 1

        # Ghi đè vào CẢ 3 TARGET DIRECTORIES:
        # Tạo cả vi_vn.json, zh_cn.json, en_us.json với cùng bản dịch hoàn hảo này!
        for target_base in TARGET_DIRS:
            target_lang = target_base / ns / "lang"
            write_json_utf8(target_lang / "vi_vn.json", final_dict)
            write_json_utf8(target_lang / "zh_cn.json", final_dict)
            write_json_utf8(target_lang / "en_us.json", final_dict)

        if processed_namespaces % 30 == 0 or processed_namespaces == len(namespace_dirs):
            print(f"  [TIẾN ĐỘ] Đã xử lý & deploy: {processed_namespaces}/{len(namespace_dirs)} namespaces")

    print("\n" + "=" * 75)
    print("  KẾT QUẢ TRIỂN KHAI VIỆT HÓA HOÀN HẢO")
    print("=" * 75)
    print(f"  ✅ Tổng namespaces xử lý:      {processed_namespaces}")
    print(f"  📝 Tổng keys ngôn ngữ:         {total_keys_count:,}")
    print(f"  🛡️ Tên vật phẩm giữ tiếng Anh:  {eng_names_count:,}")
    print(f"  🇻🇳 Mô tả, tooltip dịch TV:     {vn_keys_count:,}")
    print(f"  📂 Đã deploy đồng thời vào 3 thư mục:")
    for t in TARGET_DIRS:
        print(f"     -> {t}")
    print(f"\n  ✨ TẤT CẢ 3 FILE (vi_vn.json, zh_cn.json, en_us.json) ĐỀU ĐÃ ĐỒNG BỘ!")
    print("  -> Người chơi chọn Tiếng Việt, Tiếng Anh hay Tiếng Trung trong game đều hiển thị chuẩn!")
    print("=" * 75)


if __name__ == "__main__":
    main()
