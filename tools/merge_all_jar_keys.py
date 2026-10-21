import os, sys, zipfile, json, re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

game_dir = Path(r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1")
mods_dir = game_dir / "mods"
deployed_assets = game_dir / "resources" / "assets"

ROOT_DIR = Path(r"D:\minecraft mod trung")
SRC_ASSETS = ROOT_DIR / "Immersive Fight 4.2.9 Viet Hoa" / "resourcepack" / "IMF-VietHoa" / "assets"
MODPACK_ASSETS = ROOT_DIR / "Immersive Fight 4.2.9" / "resources" / "assets"

CHINESE_RE = re.compile(r'[\u4e00-\u9fff]')

print("=== BƯỚC 1: TRÍCH XUẤT TẤT CẢ KEYS TỪ 310 JARS MODS ===")

jar_en_data = {} # ns -> {k: v}
jar_zh_data = {} # ns -> {k: v}

for jar in sorted(mods_dir.glob("*.jar")):
    try:
        with zipfile.ZipFile(jar, 'r') as zf:
            for name in zf.namelist():
                m = re.match(r'^assets/([^/]+)/lang/([^/]+)\.json$', name)
                if not m: continue
                ns, lang_type = m.group(1), m.group(2)
                
                try:
                    raw = zf.read(name)
                    text = raw.decode('utf-8-sig', errors='replace')
                    d = json.loads(text)
                    if not isinstance(d, dict): continue
                    
                    if 'en_us' in lang_type:
                        jar_en_data.setdefault(ns, {}).update(d)
                    elif 'zh_cn' in lang_type:
                        jar_zh_data.setdefault(ns, {}).update(d)
                except Exception:
                    pass
    except Exception:
        pass

print(f"Đã trích xuất {len(jar_en_data)} namespaces en_us và {len(jar_zh_data)} namespaces zh_cn từ jars.")

# Nạp rp_translation_dict.json
rp_dict_path = ROOT_DIR / "Immersive Fight 4.2.9 Viet Hoa" / "tools" / "rp_translation_dict.json"
rp_dict = {}
if rp_dict_path.exists():
    try:
        rp_dict = json.load(open(rp_dict_path, encoding='utf-8'))
        print(f"Đã nạp {len(rp_dict)} cặp dịch từ điển rp_dict.")
    except Exception:
        pass

# Bộ từ điển dịch bổ trợ chuyên sâu cho các mod combat / attributes
EXTRA_DICT = {
    # Attributes & Combat
    "attribute.cataclysm.talisman_slots": "Ô Khảm Bùa Hộ Mệnh",
    "attribute.name.epicfight.staminaar.skillbook_tooltip": "Hồi Phục Thể Lực: +%s",
    "attribute.name.epicfight.offhand_armor_negation": "Xuyên Giáp Tay Phụ: +%s",
    "skill.epicfight.forbidden_strength.consume.tooltip": "Tiêu hao thể lực mỗi giây",
    "datapack_edit.weapon_type.combos.combo_attacks.tooltip": "Chuỗi đòn đánh kết hợp",
    
    # EFN
    "item.efn.yamato_dmc4": "Yamato (DMC4)",
    "efn.style.board_blade": "Phong Cách Đại Kiếm Bản Rộng",
    "efn.style.falchion": "Phong Cách Trảm Kiếm (Falchion)",
    "skill.efn.murasama.tooltip1": "Murasama - Lưỡi Kiếm Cao Tần Bộc Phát",
    "item.efn.nf_shortsword.description1": "Đoản Kiếm Dạ Lạc",
    
    # Relics
    "tooltip.relics.arrow_quiver.ability.agility.stat.modifier": "Gia tăng tốc độ bắn cung và tốc độ di chuyển",
    "tooltip.relics.ice_breaker.ability.sustainability.stat.modifier": "Tăng cường độ bền và hiệu ứng đóng băng",
    "tooltip.relics.bastion_ring.lore": "Chiếc nhẫn cổ xưa thấm đẫm ý chí phòng thủ bất diệt của các chiến binh Bastion.",
    "tooltip.relics.holy_locket.lore": "Mề đay thánh tỏa ánh hào quang xua tan bóng tối và tà khí.",
    "tooltip.relics.relic.leveling_points.title": "Điểm Nâng Cấp Cổ Vật",
    
    # Mowzie's Mobs
    "item.mowziesmobs.barakoa_mask_fear.text.0": "Mặt nạ Barakoa gieo rắc sự sợ hãi kinh hoàng lên kẻ thù xung quanh.",
    "item.mowziesmobs.earth_talisman.text.5": "Hộ phù Đất Mẹ ban cho người nắm giữ khả năng điều khiển đất đá.",
    "config.mowziesmobs.grottol.tooltip": "Cấu hình xuất hiện sinh vật Grottol",
    
    # Nether Exp & Legendary Monsters
    "item.netherexp.netherite_artifact.tooltip": "Cổ vật Netherite chứa đựng ngọn lửa nguyên sơ của cõi Địa Ngục.",
    "advancements.nether.witwicky.description": "Khám phá bí mật sâu thẳm trong lòng nham thạch",
    "effect.legendary_monsters.soul_eater": "Kẻ Nuốt Chửng Linh Hồn",
    
    # Touhou Little Maid
    "config.touhou_little_maid.part_ai.tts_language.tooltip": "Ngôn ngữ chuyển văn bản thành giọng nói (TTS) cho Hầu Gái",
    "config.touhou_little_maid.render.enable_ai_chat_tip": "Bật hiển thị bóng thoại AI trò chuyện trên đầu hầu gái",
    "ai.touhou_little_maid.tts.connect.fail": "Kết nối máy chủ giọng nói AI thất bại",
    "message.touhou_little_maid.script_book.copy": "Đã sao chép kịch bản hầu gái vào bộ nhớ tạm",
    
    # Enchdesc & Apotheosis
    "tooltip.enchlib.4": "Cấp Độ Tối Đa: %s",
    "enchantment.apotheosis.rebounding": "Bật Lùi Phản Đòn (Rebounding)",
    "advancements.apotheosis.30ench": "Đạt 30 Cấp Độ Cường Hóa Ma Pháp",
}

def is_name_key(key: str) -> bool:
    k = key.lower()
    desc_markers = (
        '.tooltip', '.desc', '.description', '.lore', '.ability', '.info', '.text',
        '.comment', '.line', 'skill.', 'ability.', 'attribute.', 'effect.', 'enchantment.',
        'gui.', 'key.', 'text.autoconfig', 'message.', 'title.', 'subtitle.',
        'advancements.', 'screen.', 'category.', 'tab.', 'subtitles.', 'jei.', 'emi.',
        'config.', 'option.', 'setting.', 'death.', 'prompt.', 'tip.', 'hint.', 'help.',
        'sub.', 'stat.modifier'
    )
    for m in desc_markers:
        if m in k:
            return False
            
    if "potion.effect." in k or "tipped_arrow.effect." in k:
        return False
        
    name_prefixes = ('item.', 'block.', 'entity.', 'itemgroup.', 'biome.', 'container.')
    for prefix in name_prefixes:
        if k.startswith(prefix):
            return True
            
    return False

def translate_str(k: str, zh_v: str, en_v: str) -> str:
    """Dịch chuỗi sang tiếng Việt chuẩn."""
    if k in EXTRA_DICT:
        return EXTRA_DICT[k]
        
    if zh_v and zh_v in rp_dict:
        return rp_dict[zh_v]
        
    if zh_v and not CHINESE_RE.search(zh_v):
        return zh_v
        
    # Nếu là mô tả/tooltip và có zh_v tiếng Trung, thử dịch từng phần
    if zh_v and CHINESE_RE.search(zh_v):
        res = zh_v
        for c_k, c_v in sorted(rp_dict.items(), key=lambda x: -len(x[0])):
            if len(c_k) >= 2 and c_k in res:
                res = res.replace(c_k, c_v)
        if not CHINESE_RE.search(res):
            return res
            
    # Fallback en_v nếu không còn cách nào
    return en_v or zh_v

print("\n=== BƯỚC 2: HỢP NHẤT TOÀN DIỆN VÀ BỔ SUNG CÁC KEYS THIẾU ===")

all_namespaces = sorted(set(SRC_ASSETS.iterdir()) | set(jar_en_data.keys()) | set(jar_zh_data.keys()), key=lambda x: x.name if isinstance(x, Path) else x)

total_added_keys = 0

for ns_item in all_namespaces:
    ns = ns_item.name if isinstance(ns_item, Path) else ns_item
    
    # Nạp bản dịch hiện có trong SRC_ASSETS
    src_lang = SRC_ASSETS / ns / "lang"
    existing_data = {}
    if src_lang.exists() and (src_lang / "vi_vn.json").exists():
        try:
            existing_data = json.load(open(src_lang / "vi_vn.json", encoding='utf-8'))
        except Exception:
            existing_data = {}
            
    # Lấy keys từ jar
    en_dict = jar_en_data.get(ns, {})
    zh_dict = jar_zh_data.get(ns, {})
    all_jar_keys = set(en_dict.keys()) | set(zh_dict.keys())
    
    # Tìm keys còn thiếu
    missing_keys = all_jar_keys - set(existing_data.keys())
    
    if missing_keys:
        total_added_keys += len(missing_keys)
        for k in missing_keys:
            en_val = en_dict.get(k, "")
            zh_val = zh_dict.get(k, "")
            
            if is_name_key(k):
                # Tên vật phẩm -> Giữ tiếng Anh
                existing_data[k] = en_val or (zh_val if not CHINESE_RE.search(zh_val) else rp_dict.get(zh_val, en_val))
            else:
                # Mô tả / Tooltip -> Dịch tiếng Việt
                existing_data[k] = translate_str(k, zh_val, en_val)

    # Ghi lại vào CẢ 3 VỊ TRÍ TARGET
    targets = [SRC_ASSETS, MODPACK_ASSETS, deployed_assets]
    for target_dir in targets:
        target_lang = target_dir / ns / "lang"
        target_lang.mkdir(parents=True, exist_ok=True)
        for lang_file in ["vi_vn.json", "zh_cn.json", "en_us.json"]:
            with open(target_lang / lang_file, 'w', encoding='utf-8', newline='\n') as fp:
                json.dump(existing_data, fp, ensure_ascii=False, indent=2)
                fp.write('\n')

print(f"\n[THÀNH CÔNG] Đã bổ sung tổng cộng {total_added_keys:,} keys còn thiếu từ toàn bộ 310 file JAR!")
print("Đã đồng bộ đầy đủ vi_vn.json, zh_cn.json, en_us.json vào cả 3 thư mục.")
