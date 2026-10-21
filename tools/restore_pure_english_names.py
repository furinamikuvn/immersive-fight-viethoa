# -*- coding: utf-8 -*-
"""
restore_pure_english_names.py
Restores pure Item, Block, and Entity names to their official English values,
ensuring zero over-translations while preserving 100% Vietnamese descriptions,
tooltips, lore, combat skills, passives, and combos.
"""

import os
import sys
import json
import re
import zipfile

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

ROOT_DIR = r"D:\minecraft mod trung"
ASSETS_BASE = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9 Viet Hoa\resources\assets")
RAW_ASSETS = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9 Viet Hoa\raw_sources\en_us\assets")
MODS_DIR = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9\mods")

viet_chars = re.compile(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]', re.IGNORECASE)

print("=" * 70)
print("  TAWA RESTORE PURE ENGLISH NAMES & ZERO OVER-TRANSLATION ENGINE")
print("=" * 70)

# 1. Build authoritative English dictionary
master_en = {}

# 1.1 From raw_sources
if os.path.exists(RAW_ASSETS):
    for ns in os.listdir(RAW_ASSETS):
        p = os.path.join(RAW_ASSETS, ns, 'lang', 'en_us.json')
        if os.path.exists(p):
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as f:
                    for k, v in json.load(f).items():
                        if isinstance(v, str) and not viet_chars.search(v):
                            master_en[k] = v
            except Exception:
                pass

# 1.2 From original mod jars
if os.path.exists(MODS_DIR):
    for jar in os.listdir(MODS_DIR):
        if jar.endswith('.jar'):
            try:
                with zipfile.ZipFile(os.path.join(MODS_DIR, jar), 'r') as z:
                    for fname in z.namelist():
                        if fname.startswith('assets/') and fname.endswith('/lang/en_us.json'):
                            try:
                                d = json.loads(z.read(fname).decode('utf-8', errors='ignore'))
                                for k, v in d.items():
                                    if k not in master_en and isinstance(v, str) and not viet_chars.search(v):
                                        master_en[k] = v
                            except Exception:
                                pass
            except Exception:
                pass

print(f"Loaded {len(master_en)} authoritative English keys from raw_sources and mod jars.")

# 1.3 Add vanilla Minecraft & special overrides
authoritative_overrides = {
    'item.minecraft.enchanted_book': 'Enchanted Book',
    'item.minecraft.diamond_sword': 'Diamond Sword',
    'item.minecraft.iron_sword': 'Iron Sword',
    'item.minecraft.golden_sword': 'Golden Sword',
    'item.minecraft.netherite_sword': 'Netherite Sword',
    'item.minecraft.shield': 'Shield',
    'item.minecraft.bow': 'Bow',
    'item.minecraft.crossbow': 'Crossbow',
    'itemGroup.tabblock_borin_chaos': 'Born in Chaos: Blocks',
    'skill_tree.efn.efn_skills': 'Epic Fight: Nightfall',
    'item.touhou_little_maid.favorability_tool_add': 'Favorability Tool (Add)',
    'item.touhou_little_maid.favorability_tool_reduce': 'Favorability Tool (Reduce)',
    'item.touhou_little_maid.favorability_tool_full': 'Favorability Tool (Max)',
    'item.spice.soulmob_spawn_egg': 'Soul Mob Spawn Egg',
    'entity.spice.warden_boss': 'Nether Warden',
    'item.spice.warden_boss_spawn_egg': 'Nether Warden Spawn Egg',
    'entity.spice.soul': 'Soul',
    'entity.spice.soulmob': 'Soul Mob',
}
master_en.update(authoritative_overrides)

def id_to_title(name_id):
    parts = name_id.replace('-', '_').split('_')
    # Filter out empty parts
    parts = [p for p in parts if p]
    title_parts = [p.capitalize() for p in parts]
    return ' '.join(title_parts)

name_patterns = [
    re.compile(r'^item\.[a-z0-9_]+\.[a-z0-9_]+$'),
    re.compile(r'^block\.[a-z0-9_]+\.[a-z0-9_]+$'),
    re.compile(r'^entity\.[a-z0-9_]+\.[a-z0-9_]+$'),
]

desc_suffixes = (
    '_desc', '.desc', '_description', '.description',
    '_tooltip', '.tooltip', '_info', '.info', '_lore', '.lore',
    '_comment', '.comment', '_summary', '.summary',
    '.innate', '_innate', '.passive', '_passive', '.combo', '_combo',
    '.skill', '_skill', '.ability', '_ability'
)

viet_chars = re.compile(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]', re.IGNORECASE)

restored_count = 0
modified_namespaces = set()

# We will apply this to all 230 namespaces across en_us.json, zh_cn.json, vi_vn.json
for ns in sorted(os.listdir(ASSETS_BASE)):
    lang_dir = os.path.join(ASSETS_BASE, ns, 'lang')
    if not os.path.exists(lang_dir):
        continue

    # Read en_us.json first as the primary
    en_path = os.path.join(lang_dir, 'en_us.json')
    if not os.path.exists(en_path):
        continue

    with open(en_path, 'r', encoding='utf-8') as f:
        en_data = json.load(f)

    changed_keys = {}
    for k, v in list(en_data.items()):
        if any(k.endswith(s) for s in desc_suffixes):
            continue
        
        # Check if it's a pure name or creative tab/modpack title that has Vietnamese text
        is_name = any(pat.match(k) for pat in name_patterns)
        is_tab = k.startswith('itemGroup.') or k.startswith('creativetab.')
        is_special = k in authoritative_overrides

        if is_name or is_tab or is_special:
            if isinstance(v, str) and (viet_chars.search(v) or is_special):
                # Determine correct English target
                if k in master_en and not viet_chars.search(master_en[k]):
                    target_val = master_en[k]
                else:
                    # Try fallback for mapped namespaces (e.g. ob_aquamirae -> aquamirae)
                    equiv = k.replace('.ob_aquamirae.', '.aquamirae.')
                    if equiv in master_en and not viet_chars.search(master_en[equiv]):
                        target_val = master_en[equiv]
                    else:
                        parts = k.split('.')
                        target_val = id_to_title(parts[-1])
                
                if en_data[k] != target_val:
                    changed_keys[k] = target_val

    if changed_keys:
        modified_namespaces.add(ns)
        restored_count += len(changed_keys)
        
        # Apply changes across all 3 language files for complete consistency
        for lang_file in ['en_us.json', 'zh_cn.json', 'vi_vn.json']:
            lp = os.path.join(lang_dir, lang_file)
            if os.path.exists(lp):
                with open(lp, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                for k, target_val in changed_keys.items():
                    data[k] = target_val
                with open(lp, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Restored {restored_count} pure item/block/entity keys across {len(modified_namespaces)} namespaces!")

# Also sync to 'Immersive Fight 4.2.9 - Cai Dat Nhanh' resources
cai_dat_assets = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9 - Cai Dat Nhanh\resources\assets")
if os.path.exists(cai_dat_assets):
    import shutil
    print("Syncing restored assets to 'Immersive Fight 4.2.9 - Cai Dat Nhanh'...")
    for ns in modified_namespaces:
        src_ns = os.path.join(ASSETS_BASE, ns, 'lang')
        dst_ns = os.path.join(cai_dat_assets, ns, 'lang')
        if os.path.exists(src_ns) and os.path.exists(dst_ns):
            for lf in ['en_us.json', 'zh_cn.json', 'vi_vn.json']:
                shutil.copy2(os.path.join(src_ns, lf), os.path.join(dst_ns, lf))
    print("Sync to Cai Dat Nhanh completed.")

# Also sync to User Forge 1.20.1 instance if exists
game_assets = r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\resources\assets"
if os.path.exists(game_assets):
    import shutil
    print("Syncing restored assets to active game instance Forge 1.20.1...")
    for ns in modified_namespaces:
        src_ns = os.path.join(ASSETS_BASE, ns, 'lang')
        dst_ns = os.path.join(game_assets, ns, 'lang')
        if os.path.exists(src_ns) and os.path.exists(dst_ns):
            for lf in ['en_us.json', 'zh_cn.json', 'vi_vn.json']:
                shutil.copy2(os.path.join(src_ns, lf), os.path.join(dst_ns, lf))
    print("Sync to Forge 1.20.1 instance completed.")

print("\n" + "=" * 70)
print("  RESTORATION COMPLETED SUCCESSFULLY!")
print("=" * 70)
