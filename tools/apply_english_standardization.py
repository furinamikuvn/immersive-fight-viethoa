import os
import sys
import json
import zipfile
import shutil
import time

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

print("=== TIÊU CHUẨN HÓA TIẾNG ANH & DIỆT TẬN GỐC DỊCH LỎ ===")

source_assets_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\resourcepack\IMF-VietHoa\assets"

# Master dictionary of overrides for clean, professional, gamer-intuitive English / Vietnamese
standard_overrides = {
    # --- EFN (Epic Fight Nightfall) ---
    "itemGroup.efn.items": "Epic Fight: Nightfall",
    "itemGroup.efn.items_extra": "Epic Fight: Nightfall (Extra)",
    "key.efn.category": "Epic Fight: Nightfall",
    "enchantment.efn.broad_blade_enhance": "BroadBlade - Revolution",
    "enchantment.efn.broad_blade_enhance.desc": "Mở khóa nội tại của BroadBlade: Revolution",
    "epicfight.style.board_blade": "Two Handed: BroadBlade",
    "enchantment.efn.yamato_summoned_sword": "Yamato - Summoned Sword",
    "enchantment.efn.yamato_summoned_sword.desc": "Mở khóa kỹ năng Summoned Swords cho Yamato",
    "enchantment.efn.yamato_summoned_sword_end": "Yamato - Summoned Sword: End",
    "enchantment.efn.yamato_summoned_sword_end.desc": "Mở khóa chiêu thức tối thượng Summoned Swords cho Yamato",
    "enchantment.efn.yamato_doppelganger": "Yamato - Doppelgänger",
    "enchantment.efn.yamato_doppelganger.desc": "Mở khóa kỹ năng phân thân Doppelgänger cho Yamato",
    "enchantment.efn.yamato_judgement_cut_end": "Yamato - Judgement Cut End",
    "enchantment.efn.yamato_judgement_cut_end.desc": "Mở khóa tuyệt kỹ Judgement Cut End cho Yamato",
    "enchantment.efn.yamato_heavy_rain": "Yamato - Heavy Rain Blades",
    "enchantment.efn.yamato_heavy_rain.desc": "Mở khóa chiêu thức Mưa Kiếm Heavy Rain cho Yamato",
    "enchantment.efn.yamato_guard": "Yamato - Guard",
    "enchantment.efn.yamato_guard.desc": "Tăng cường khả năng phòng thủ và phản đòn của Yamato",
    "enchantment.efn.scythe_enhance": "Crimson Moon - Demonized",
    "enchantment.efn.scythe_enhance.desc": "Mở khóa cường hóa Quỷ Hóa Mặt Trăng Đỏ của Lưỡi Hái",
    "skill_tree.efn.efn_skills": "Epic Fight: Nightfall",
    "skill.epicfight.efn_arts.category": "Nightfall Arts",
    "skill.epicfight.efn_sekiro.category": "Sekiro Arts",
    "skill.epicfight.efn_zansetsu.category": "BLADE MODE",
    "skill.epicfight.judgmentcut_end.category": "Judgement Cut End",
    "skill.efn.judgementcutend": "Judgement Cut End",
    "skill.efn.judgementcutend.unlock_tip": "Mở khóa sau khi học từ sách kỹ năng",
    "stat.efn.judgementcutend_unlock": "Đã mở khóa Judgement Cut End",
    "skill.efn.zansetsu": "Blade Mode",
    "skill.efn.execution": "Soul Hunt",
    "skill.efn.mortal_blade": "Mortal Blade - HaiRui",
    "skill.efn.efn_dodge": "Soul-like Dodge",
    "skill.efn.efn_step": "Soul-like Step",
    "skill.efn.yamato_step": "YAMATO STEP",
    "skill.efn.parry_master": "Parry Master",
    "skill.efn.indestructible": "Indestructible",
    "skill.efn.precise_parry": "Precise Parry",
    "skill.efn.beastclaw.tooltip": "Feral Claw",
    "skill.efn.shortsword.tooltip": "Reenactment",
    "skill.efn.crescentmoon.tooltip": "Soul Fusion",
    "skill.efn.broadblade.tooltip": "Breaking Edge",
    "advancement.efn.obtain_yamato_dmc4.title": "YAMATO (DMC4)",
    "advancement.efn.obtain_yamato_dmc.title": "[YAMATO - Sparda]",
    "advancement.efn.obtain_hf_murasama.title": "HF-Murasama",
    "advancement.efn.obtain_hf_blade.title": "HF-Blade",
    "advancement.efn.obtain_mortal_blade.title": "Mortal Blade",
    "key.efn.doppelganger": "Doppelgänger (Yamato)",
    "key.efn.doppelganger_delay": "Độ trễ Doppelgänger",
    "key.efn.summoned_sword": "Summoned Swords (Ảo Ảnh Kiếm)",
    "key.efn.arts": "Nightfall Arts",
    "key.efn.angel": "Angel Stance",
    "key.efn.demon": "Devil Stance",
    "key.efn.zansetsu_input_switch": "Chuyển đổi kiểu điều khiển Blade Mode",
    "prompt.efn.judgementcut": "Judgement Cut",
    "prompt.efn.helmbreaker": "Helm Breaker",
    "prompt.efn.repaidslash": "Repaid Slash",
    "prompt.efn.flarecut": "Flare Cut",
    "prompt.efn.flarecut_rise": "Flare Cut - Rise",
    "prompt.efn.upperslash": "Upper Slash",
    "prompt.efn.drive": "Drive",
    "prompt.efn.stomp": "Stomp",
    "prompt.efn.flush": "Flush",
    "prompt.efn.killerbee": "Killer Bee",

    # --- EpicFight Awaken ---
    "key.category.epicfight_awaken": "Epic Fight: Awakening",
    "creativetab.epicfight_awaken.efa_items": "Epic Fight: Awakening",
    "skill.epicfight_awaken.darknight_pursuiters": "Darknight Pursuiters",
    "skill.epicfight_awaken.focused_strike": "Focused Strike",
    "skill.epicfight_awaken.darknight_pursuiters.tooltip4": "-[Đòn đánh thường] §f N N N N",
    "skill.epicfight_awaken.darknight_pursuiters.tooltip5": "-[Heavy Attack] §f H H H H",
    "skill.epicfight_awaken.darknight_pursuiters.tooltip6": "-[Sunset] §f N H",
    "skill.epicfight_awaken.darknight_pursuiters.tooltip7": "-[Sunset Harvest] §f N N H",
    "skill.epicfight_awaken.darknight_pursuiters.tooltip8": "-[Shadow Flurry] §f N N N H H ... H",
    "skill.epicfight_awaken.darknight_pursuiters.tooltip9": "-[Shadow Assault] §f Dash N H H H",
    "skill.epicfight_awaken.darknight_pursuiters.tooltip10": "-[Shadow Fall] §f Nhảy N H",
    "skill.epicfight_awaken.darknight_pursuiters.tooltip11": "-[Shadow Step] §f Sau đòn đánh S1 H",
    "effect.epicfight_awaken.curse_of_night": "Curse of Night",
    "effect.epicfight_awaken.flame_enchant": "Flame Enchant",
    "effect.epicfight_awaken.lightning_enchant": "Lightning Enchant",

    # --- Fantasy Armor ---
    "itemGroup.fantasy_armor.fa_tab": "Fantasy Armor",

    # --- Nightfall Invade ---
    "key.nightfall_invade.category": "Nightfall Invade",
    "creativetab.nightfall_invade.items": "Nightfall Invade",
    "advancements.nightfall_invade.root.title": "Nightfall Invade",

    # --- Epic Fight Core ---
    "itemGroup.epicfight.items": "Epic Fight",
    "key.epicfight.combat": "Chế độ Epic Fight",
    "key.epicfight.camera": "Camera Epic Fight",
    "key.epicfight.system": "Hệ thống Epic Fight",
    "key.epicfight.gui": "Giao diện Epic Fight",
    "epicfight.gui.attribute": "Thuộc tính Epic Fight:",
    "gui.epicfight.configurations": "Cấu hình Epic Fight",
    "gui.epicfight.graphic_options": "Cài đặt đồ họa Epic Fight",
    "gui.epicfight.control_options": "Cài đặt điều khiển Epic Fight",
    "gui.epicfight.filter_animation.tooltip": "Bật/tắt hoạt ảnh Epic Fight khi đang khai thác",
    "gui.epicfight.show_attributes.tooltip": "Hiển thị thuộc tính Epic Fight trong mô tả vật phẩm",
    "pack.epicfight_legacy.title": "Epic Fight Legacy",
    "datapack_edit.mob_patch.disabled.tooltip": "Vô hiệu hóa phong cách Epic Fight",
    "epicfight.gui.tooltip_battle": "Tự động đăng ký tất cả các vật phẩm có thuộc tính Epic Fight.",

    # --- Creative Tabs (Chuẩn hóa toàn bộ tên Tab sáng tạo sang Tiếng Anh) ---
    "itemGroup.alexscaves": "Alex's Caves",
    "itemGroup.alexscaves.magnetic_caves": "Alex's Caves: Magnetic Caves",
    "itemGroup.alexscaves.primordial_caves": "Alex's Caves: Primordial Caves",
    "itemGroup.alexscaves.toxic_caves": "Alex's Caves: Toxic Caves",
    "itemGroup.alexscaves.abyssal_chasm": "Alex's Caves: Abyssal Chasm",
    "itemGroup.alexscaves.forlorn_hollows": "Alex's Caves: Forlorn Hollows",
    "itemGroup.alexscaves.candy_cavity": "Alex's Caves: Candy Cavity",
    "itemGroup.alexsmobs": "Alex's Mobs",
    "itemGroup.aquamirae": "Aquamirae",
    "itemGroup.tabaquamirae_tab": "Aquamirae",
    "itemGroup.arsenal": "Arsenal",
    "itemGroup.backpacked": "Backpacked",
    "itemGroup.beachparty.creative_tab": "Beach Party",
    "creativetab.beachparty.tab": "Beach Party",
    "itemGroup.betterend.blocks": "BetterEnd: Blocks",
    "itemGroup.betterend.items": "BetterEnd: Items",
    "itemGroup.betterend.nature": "BetterEnd: Nature",
    "creativetab.beyonddimensions.items": "Beyond Dimensions: Items",
    "creativetab.beyonddimensions.blocks": "Beyond Dimensions: Blocks",
    "itemGroup.biomeswevegone.biomes_weve_gone": "Biomes We've Gone",
    "itemGroup.biomeswevegone.biomes_weve_gone_wood": "Biomes We've Gone: Wood",
    "itemGroup.tabblock_borin_chaos": "Born in Chaos: Blocks",
    "itemGroup.tabbornin_chaos_items": "Born in Chaos: Items",
    "itemGroup.tabbornin_chaos_mobs": "Born in Chaos: Mobs",
    "itemGroup.tabdebugging_bornin_chaos": "Born in Chaos: Debug",
    "itemGroup.tabweapons_bornin_chaos": "Born in Chaos: Weapons",
    "itemGroup.bosses_of_mass_destruction.items": "Bosses of Mass Destruction",
    "itemGroup.cataclysm": "Cataclysm",
    "itemGroup.cataclysm.item": "Cataclysm: Items",
    "itemGroup.cataclysm.block": "Cataclysm: Blocks",
    "creativetab.celestisynth_tab": "Celestisynth",
    "itemGroup.celestisynth.celestisynth_tab": "Celestisynth",
    "creativetab.clockwork.title": "Clockwork",
    "creativetab.combat_evolution.items": "Combat Evolution",
    "itemGroup.creeperoverhaul.item_group": "Creeper Overhaul",
    "itemGroup.dodosmobs.item": "Dodo's Mobs",
    "itemGroup.endermanoverhaul.main": "Enderman Overhaul",
    "itemGroup.efx.items": "Epic Fight: Extra",
    "itemGroup.ftbquests.ftbquests": "FTB Quests",
    "itemGroup.gateways": "Gateways to Eternity",
    "itemGroup.geckolib.geckolib_examples": "GeckoLib",
    "itemGroup.graveyard.group": "The Graveyard",
    "itemGroup.illageandspillage.creative_tab": "Illage and Spillage",
    "itemGroup.illageradditions": "Illager Additions",
    "itemGroup.itemfilters.main": "Item Filters",
    "itemGroup.itemfilters.itemfilters": "Item Filters",
    "itemGroup.my_mod.items": "Custom Items",
    "creativetab.legendary_monsters": "Legendary Monsters",
    "itemGroup.libraryferret.libraryferret": "Library Ferret",
    "itemGroup.lootbags.main": "Loot Bags",
    "itemGroup.lootr": "Lootr",
    "itemgroup.mebahelcreaturesdraugr": "Mebahel's Creatures: Draugr",
    "itemgroup.mebahelcreaturesdwarven": "Mebahel's Creatures: Dwarven",
    "creativetab.dungeons_tab": "Minecraft Dungeons",
    "itemGroup.modifiers_books": "Modifiers",
    "itemGroup.modifiers.books": "Modifiers",
    "creativetab.monsterexpansion_tab": "Monster Expansion",
    "itemGroup.mowziesmobs.creativeTab": "Mowzie's Mobs",
    "creativetab.mythical_weaponry_main": "Mythical Weaponry",
    "itemGroup.naraka": "Naraka",
    "itemGroup.naraka.soul_materials": "Naraka: Soul Materials",
    "itemGroup.naraka.test": "Naraka: Debug",
    "itemGroup.netherexp.netherexp_tab": "Nether Expansion",
    "itemGroup.notsoshrimple": "Not So Shrimple",
    "itemGroup.tabplenty_of_golems": "Plenty of Golems",
    "itemGroup.raidsenhanced": "Raids Enhanced",
    "itemGroup.tab_quests_tab": "RPG Quests",
    "itemGroup.tabrealm_rpg_skeletons_tab": "Realm RPG: Skeletons",
    "creativetab.rapiers_tab": "Rapiers",
    "itemGroup.regions_unexplored_main": "Regions Unexplored",
    "itemGroup.regions_unexplored.title.main": "Regions Unexplored: Building Blocks",
    "itemGroup.regions_unexplored.title.nature": "Regions Unexplored: Nature",
    "itemGroup.regions_unexplored.title.nether": "Regions Unexplored: Nether",
    "itemGroup.regions_unexplored_natural": "Regions Unexplored: Nature",
    "itemGroup.regions_unexplored_nether": "Regions Unexplored: Nether",
    "itemGroup.relics": "Relics",
    "itemGroup.ringsofascension": "Rings of Ascension",
    "itemGroup.saintsdragons": "Saints Dragons",
    "itemGroup.simplyswords.simplyswords": "Simply Swords",
    "itemGroup.tabtab_1": "Souls-like Armors: Armor",
    "itemGroup.tabtab_2": "Souls-like Armors: Misc",
    "itemGroup.tabtab_3": "Souls-like Armors: Weapons",
    "itemGroup.tabtab_4": "Souls-like Armors: Shields",
    "itemGroup.tabtab_5": "Souls-like Armors: Rusted Steel",
    "itemGroup.tabtab_6": "Souls-like Armors: Alloy",
    "itemGroup.tabtab_7": "Souls-like Armors: Black Knight",
    "itemGroup.tabtab_8": "Souls-like Armors: Black Baron",
    "itemGroup.tabtab_9": "Souls-like Armors: Victorious Knight",
    "itemGroup.tabsoullikemobstab": "Souls-like Mobs",
    "itemGroup.species.species": "Species",
    "itemGroup.supplementaries": "Supplementaries",
    "itemGroup.jars": "Supplementaries: Jars",
    "itemGroup.sword_soaring.items": "Sword Soaring",
    "itemGroup.valhelsia_structures_main": "Valhelsia Structures",
    "itemGroup.valhelsia_structures": "Valhelsia Structures",
    "itemGroup.waystones.waystones": "Waystones",
    "itemGroup.whaleborne.whaleborne": "Whaleborne",
    "itemGroup.wom.items": "Weapons of Miracle",
    "itemGroup.womalt.items": "Weapons of Miracle: Alternate",
    "creativetab.womplus": "Weapons of Miracle: Plus",

    # --- Subtitles / Specific fixes ---
    "subtitles.saintsdragons.ignivorus_die": "Ignivorus: Tiếng rống khi chết"
}

# 1. Update source assets in IMF-VietHoa
print("1. Cập nhật các file JSON trong thư mục nguồn IMF-VietHoa...")
updated_files_count = 0
for root, dirs, files in os.walk(source_assets_dir):
    for f in files:
        if f.endswith(".json") and "lang" in root:
            filepath = os.path.join(root, f)
            try:
                with open(filepath, "r", encoding="utf-8") as jf:
                    data = json.load(jf)
                modified = False
                for k, v in standard_overrides.items():
                    if k in data or (f.endswith("vi_vn.json") and any(part in k for part in root.split(os.sep))):
                        data[k] = v
                        modified = True
                if modified:
                    with open(filepath, "w", encoding="utf-8") as jf:
                        json.dump(data, jf, ensure_ascii=False, indent=2)
                    updated_files_count += 1
            except Exception as e:
                pass

print(f"  -> Đã cập nhật {updated_files_count} file JSON trong nguồn IMF-VietHoa!")

# 2. Re-pack IMF-VietHoa.zip
def build_zip_from_dir(src_dir, dest_zip):
    print(f"2. Đóng gói {os.path.basename(dest_zip)}...")
    with zipfile.ZipFile(dest_zip, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                full_p = os.path.join(root, file)
                rel_p = os.path.relpath(full_p, src_dir)
                zf.write(full_p, rel_p)
    print(f"  -> Hoàn tất: {dest_zip} ({os.path.getsize(dest_zip)/(1024*1024):.2f} MB)")

source_root = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\resourcepack\IMF-VietHoa"
dist_zip = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\dist\IMF-VietHoa.zip"
build_zip_from_dir(source_root, dist_zip)

# 3. Synchronize IMF-VietHoa.zip to all locations
print("3. Đồng bộ IMF-VietHoa.zip sang các vị trí đích...")
target_locations = [
    r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\resourcepacks\IMF-VietHoa.zip",
    r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh\resourcepacks\IMF-VietHoa.zip",
    r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\resourcepacks\IMF-VietHoa.zip"
]
for target in target_locations:
    os.makedirs(os.path.dirname(target), exist_ok=True)
    shutil.copy2(dist_zip, target)
    print(f"  -> Đã chép sang: {target}")

# 4. Also update IMF-Trans.zip in all locations so there is zero conflict
print("4. Cập nhật các tệp JSON trong IMF-Trans.zip...")
imf_trans_paths = [
    r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh\resourcepacks\IMF-Trans.zip",
    r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\resourcepacks\IMF-Trans.zip",
    r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\resourcepacks\IMF-Trans.zip"
]

def update_zip_internal(zip_path, overrides):
    if not os.path.exists(zip_path):
        return
    temp_zip = zip_path + ".temp"
    with zipfile.ZipFile(zip_path, 'r') as zin, zipfile.ZipFile(temp_zip, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zout:
        for item in zin.infolist():
            content = zin.read(item.filename)
            if item.filename.endswith('.json') and 'lang' in item.filename:
                try:
                    d = json.loads(content.decode('utf-8'))
                    changed = False
                    for k, v in overrides.items():
                        if k in d:
                            d[k] = v
                            changed = True
                    if changed:
                        content = json.dumps(d, ensure_ascii=False, indent=2).encode('utf-8')
                except:
                    pass
            zout.writestr(item, content)
    shutil.move(temp_zip, zip_path)
    print(f"  -> Đã cập nhật đè nội dung JSON trong: {zip_path}")

for itp in imf_trans_paths:
    update_zip_internal(itp, standard_overrides)

print("\nHoàn tất 100% cập nhật chuẩn hóa ngôn ngữ!")
