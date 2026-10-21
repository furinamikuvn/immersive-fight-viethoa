import os, json, sys, re, zipfile

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"D:\minecraft mod trung"
ASSETS_BASE = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9 Viet Hoa\resources\assets")
RAW_ASSETS = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9 Viet Hoa\raw_sources\en_us\assets")
MODS_DIR = os.path.join(ROOT_DIR, r"Immersive Fight 4.2.9\mods")

viet_chars = re.compile(r'[àáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ]', re.IGNORECASE)

# 1. Build English dictionary
master_en = {}

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

print(f"Loaded {len(master_en)} authoritative English keys.")

def to_title(text):
    parts = text.replace('-', '_').split('_')
    return ' '.join(p.capitalize() for p in parts if p)

# Specific curated overrides for all 126 enchantments and tabs
overrides = {
    # Enchantments
    'enchantment.alexscaves.energy_efficiency': 'Energy Efficiency',
    'enchantment.alexscaves.explosive_flavor': 'Explosive Flavor',
    'enchantment.alexscaves.triple_splash': 'Triple Splash',
    'enchantment.alexscaves.sightless': 'Sightless',
    'enchantment.alexscaves.taxing_bellow': 'Taxing Bellow',
    'enchantment.alexscaves.ferrous_haste': 'Ferrous Haste',
    'enchantment.alexscaves.field_extension': 'Field Extension',
    'enchantment.alexscaves.chomping_spirit': 'Chomping Spirit',
    'enchantment.alexscaves.detonating_death': 'Detonating Death',
    'enchantment.alexscaves.multiple_mint': 'Multiple Mint',
    'enchantment.alexscaves.swiftwood': 'Swiftwood',
    'enchantment.alexscaves.soak_seeking': 'Soak Seeking',
    'enchantment.alexscaves.sharp_cane': 'Sharp Cane',
    'enchantment.alexscaves.triple_split': 'Triple Split',
    'enchantment.alexscaves.charting_call': 'Charting Call',
    'enchantment.alexscaves.seekcandy': 'Seekcandy',
    'enchantment.alexscaves.flinging': 'Flinging',
    'enchantment.alexscaves.spell_lasting': 'Spell Lasting',
    'enchantment.alexscaves.solar': 'Solar',
    'enchantment.alexscaves.lasting_morale': 'Lasting Morale',
    'enchantment.alexscaves.targeted_ricochet': 'Targeted Ricochet',
    'enchantment.alexscaves.herd_phalanx': 'Herd Phalanx',
    'enchantment.alexscaves.bouncing_bolt': 'Bouncing Bolt',
    'enchantment.alexscaves.dark_nock': 'Dark Nock',
    'enchantment.alexscaves.impending_stab': 'Impending Stab',
    'enchantment.alexscaves.seapairing': 'Seapairing',
    'enchantment.alexscaves.humungous_hex': 'Humungous Hex',
    'enchantment.alexscaves.peppermint_punting': 'Peppermint Punting',
    'enchantment.alexscaves.sea_swing': 'Sea Swing',
    'enchantment.alexscaves.far_flung': 'Far Flung',
    'enchantment.alexscaves.enveloping_bubble': 'Enveloping Bubble',
    'enchantment.alexscaves.plummeting_flight': 'Plummeting Flight',
    'enchantment.alexscaves.double_stab': 'Double Stab',
    'enchantment.alexscaves.heavy_slam': 'Heavy Slam',
    'enchantment.alexscaves.bouncy_ball': 'Bouncy Ball',
    'enchantment.alexscaves.precise_volley': 'Precise Volley',
    'enchantment.alexscaves.shaded_respite': 'Shaded Respite',
    'enchantment.alexscaves.relentless_darkness': 'Relentless Darkness',
    'enchantment.alexscaves.bonking': 'Bonking',
    'enchantment.alexscaves.dazing_sweep': 'Dazing Sweep',
    'enchantment.alexscaves.twilight_perfection': 'Twilight Perfection',
    'enchantment.alexscaves.straight_hook': 'Straight Hook',
    'enchantment.alexscaves.tsunami': 'Tsunami',
    'enchantment.alexscaves.rapid_possession': 'Rapid Possession',
    'enchantment.alexscaves.sated_blade': 'Sated Blade',
    'enchantment.alexscaves.astral_transferring': 'Astral Transferring',
    'enchantment.alexscaves.crystallization': 'Crystallization',
    'enchantment.alexscaves.second_wave': 'Second Wave',
    'enchantment.alexscaves.arrow_inducting': 'Arrow Inducting',
    'enchantment.alexscaves_torpedoes.universal_magnetism': 'Universal Magnetism',
    'enchantment.alexsmobs.board_return': 'Board Return',
    'enchantment.alexsmobs.lavawax': 'Lavawax',
    'enchantment.alexsmobs.serpentfriend': 'Serpentfriend',
    'enchantment.alexsmobs.straddle_jump': 'Straddle Jump',
    'enchantment.backpacked.funnelling': 'Funnelling',
    'enchantment.backpacked.repairman': 'Repairman',
    'enchantment.backpacked.looted': 'Looted',
    'enchantment.backpacked.imbued_hide': 'Imbued Hide',
    'enchantment.backpacked.marksman': 'Marksman',
    'enchantment.betterend.end_veil': 'End Veil',
    'enchantment.celestisynth.pulsation': 'Pulsation',
    'enchantment.combat_evolution.intimidate': 'Intimidate',
    'enchantment.combat_evolution.massacre': 'Massacre',
    'enchantment.efn.yamato_summoned_sword_end': 'Yamato: Summoned Swords End',
    'enchantment.efn.yamato_heavy_rain': 'Yamato: Heavy Rain Swords',
    'enchantment.efn.yamato_summoned_sword': 'Yamato: Summoned Swords',
    'enchantment.efn.scythe_enhance:': 'Devil Scythe Enhancement',
    'enchantment.efn.yamato_judgement_cut_end': 'Yamato: Judgement Cut End',
    'enchantment.enchantmentsplus.stormstrike': 'Stormstrike',
    'enchantment.enchantmentsplus.flashforge': 'Flashforge',
    'enchantment.enchantmentsplus.toxicstrike': 'Toxicstrike',
    'enchantment.enchantmentsplus.dualleap': 'Dual Leap',
    'enchantment.enchantmentsplus.lifesteal': 'Lifesteal',
    'enchantment.enchantmentsplus.moonwalker': 'Moonwalker',
    'enchantment.enchantmentsplus.endslayer': 'Endslayer',
    'enchantment.enchantmentsplus.thunderlord': 'Thunderlord',
    'enchantment.enchantmentsplus.lunarsight': 'Lunarsight',
    'enchantment.enchantmentsplus.levitation': 'Levitation',
    'enchantment.enchantmentsplus.raider': 'Raider',
    'enchantment.enchantmentsplus.mysticmind': 'Mystic Mind',
    'enchantment.enchantmentsplus.frostbite': 'Frostbite',
    'enchantment.enchantmentsplus.cubical': 'Cubical',
    'enchantment.enchantmentsplus.sniper': 'Sniper',
    'enchantment.enchantmentsplus.payback': 'Payback',
    'enchantment.enchantmentsplus.excavator': 'Excavator',
    'enchantment.endlessbiomes.shared_pain': 'Shared Pain',
    'enchantment.fight_more.health_boost': 'Health Boost',
    'enchantment.fight_more.basic_regeneration': 'Basic Regeneration',
    'enchantment.mebahelcreaturesdraugr.soul_gem_quick_cast': 'Soul Gem: Quick Cast',
    'enchantment.mebahelcreaturesdraugr.soul_gem_spell_power': 'Soul Gem: Spell Power',
    'enchantment.mebahelcreaturesdraugr.soul_gem_multishot': 'Soul Gem: Multishot',
    'enchantment.mofus_better_end_.scrap_harpoon_enchantment': 'Scrap Harpoon Enchantment',
    'enchantment.mofus_better_end_.ink_speed': 'Ink Speed',
    'enchantment.mofus_better_end_.endermite_idol_saturated': 'Endermite Idol: Saturated',
    'enchantment.mofus_better_end_.harpoon_feather_edge': 'Harpoon: Feather Edge',
    'enchantment.mofus_better_end_.endermite_idol_experience': 'Endermite Idol: Experience',
    'enchantment.mofus_better_end_.crystal_staff_stinger_enchantment': 'Crystal Staff: Stinger Enchantment',
    'enchantment.mofus_better_end_.drill_strengh': 'Drill Strength',
    'enchantment.mofus_better_end_.ink_recycling': 'Ink Recycling',
    'enchantment.mofus_better_end_.sparing': 'Sparing',
    'enchantment.mofus_better_end_.endermite_idol_hunger': 'Endermite Idol: Hunger',
    'enchantment.mofus_better_end_.harpoon_duplicate': 'Harpoon: Duplicate',
    'enchantment.mofus_better_end_.excavation': 'Excavation',
    'enchantment.mofus_better_end_.ink_pressure': 'Ink Pressure',
    'enchantment.mofus_better_end_.harpoon_chain_length': 'Harpoon: Chain Length',
    'enchantment.mofus_better_end_.staff_multiply': 'Staff Multiply',
    'enchantment.mofus_better_end_.queen_scythe_endurance': "Queen's Scythe Endurance",
    'enchantment.mofus_better_end_.exsanguination': 'Exsanguination',
    'enchantment.netherexp.artemis': 'Artemis',
    'enchantment.netherexp.recoil': 'Recoil',
    'enchantment.netherexp.phantasm_hull': 'Phantasm Hull',
    'enchantment.netherexp.barrage': 'Barrage',
    'enchantment.netherexp.cartridge': 'Cartridge',
    'enchantment.nethers_exorcism_reborn.genetic_anomally': 'Genetic Anomaly',
    'enchantment.nethers_exorcism_reborn.lasting_baloon': 'Lasting Balloon',
    'enchantment.obscure_api.mirror': 'Mirror',
    'enchantment.obscure_api.distance': 'Distance',
    'enchantment.soul_like_armors_reworked.infinitemagic': 'Infinite Magic',
    'enchantment.supplementaries.stasis': 'Stasis',
    'enchantment.too_many_bows.spectral': 'Spectral',
    'enchantment.too_many_bows.ricochet': 'Ricochet',
    'enchantment.touhou_little_maid.enders_ender': "Ender's Ender",
    'enchantment.touhou_little_maid.impeding': 'Impeding',
    'enchantment.touhou_little_maid.speedy': 'Speedy',
    'enchantment.wom.invigoration': 'Invigoration',
    'enchantment.womalt.invigoration': 'Invigoration',
    
    # Tabs & Mod Names
    'item_group.block_factorys_bosses.blockfactorysbossestab': "Block Factory's Bosses",
    'item_group.born_in_chaos_v1.bornin_chaos_mobs': 'Born in Chaos | Entities',
    'item_group.born_in_chaos_v1.bornin_chaos_items': 'Born in Chaos | Items',
    'item_group.born_in_chaos_v1.debugging_bornin_chaos': 'Born in Chaos | Debug Items',
    'item_group.born_in_chaos_v1.block_borin_chaos': 'Born in Chaos | Blocks',
    'item_group.born_in_chaos_v1.weapons_bornin_chaos': 'Born in Chaos | Weapons',
    'item_group.eeeabsmobs.creative_tab': "EEEAB's Mobs",
    'item_group.friendsandfoes.main_tab': 'Friends & Foes',
    'item_group.mofus_better_end_.asteroid_path_biome': "Mofu's Better End: Asteroids",
    'item_group.mofus_better_end_.custom_end': "Mofu's Better End",
    'item_group.nethers_exorcism_reborn.nethers_exorcism': "Nether's Exorcism",
    'item_group.oddities.oddities': 'Oddities',
    'item_group.plenty_of_golems.plenty_of_golems': 'Plenty of Golems',
    'item_group.realmrpg_skeletons.realm_rpg_skeletons_tab': 'Realm RPG: Fallen Adventurers',
    'item_group.soul_like_armors_reworked.tab_1': 'Soul-Like Armors: Armors',
    'item_group.soul_like_armors_reworked.tab_2': 'Soul-Like Armors: Misc',
    'item_group.soul_like_armors_reworked.tab_3': 'Soul-Like Armors: Weapons',
    'item_group.soul_like_armors_reworked.tab_4': 'Soul-Like Armors: Shields',
    'item_group.soul_like_armors_reworked.tab_5': 'Soul-Like Armors: Updates',
    'item_group.soul_like_armors_reworked.armor_tab': 'Soul-Like Armors',
    'item_group.soul_like_armors_reworked.other_items_tab': 'Soul-Like Armors: Other Items',
    
    # Class enhancement lang refinement
    'class.linggango.class_enhancement.tank.name': 'Thiết Vệ',
    'class.linggango.class_enhancement.tank.desc': 'Thể chất kiên cường phi thường, chống chịu lượng lớn sát thương từ kẻ địch.',
    'class.linggango.class_enhancement.ranger.name': 'Du Hiệp',
    'class.linggango.class_enhancement.ranger.desc': 'Thân thủ nhanh nhẹn, bách phát bách trúng, làm chủ tầm nhìn chiến trường.',
    'class.linggango.class_enhancement.warrior.name': 'Chiến Binh',
    'class.linggango.class_enhancement.warrior.desc': 'Sinh ra để làm chủ chiến trận, thành thạo cận chiến áp đảo.',
    'class.linggango.class_enhancement.civilian.name': 'Thường Dân',
    'class.linggango.class_enhancement.civilian.desc': 'Không có thuộc tính cộng thêm. Xuất thân bình dị, dấn thân vào hiểm nguy bằng chính thực lực.',
    'gui.linggango.class_enhancement.confirm': '§lXác Nhận',
    'gui.linggango.class_enhancement.screen_title': '§lLựa Chọn Nghề Nghiệp',
    'gui.linggango.class_enhancement.title': '§lLựa Chọn Nghề Nghiệp',
    'gui.linggango.class_enhancement.starting_equipment': '§lTrang Bị Khởi Đầu',
    'gui.linggango.class_enhancement.loading': '§lĐang phân phát trang bị khởi đầu...',
    'gui.linggango.class_enhancement.navigation_guide': '§l↑↓ / W/S chọn • ENTER để xác nhận',
    'class.linggango.class_enhancement.custom.name': 'Nghề Nghiệp Mới',
    'class.linggango.class_enhancement.custom.desc': 'Một hành trình tùy chỉnh đầy thử thách.',
    'class.linggango.class_enhancement.custom.desc0': 'Hồi phục sinh lực mạnh mẽ cho bản thân và đồng minh.',
    'class.linggango.class_enhancement.custom.desc1': 'Khả năng sinh tồn và thích nghi thượng thừa trong môi trường khắc nghiệt.',
    'class.linggango.class_enhancement.custom.desc2': 'Kỹ năng cận chiến đỉnh cao, phản xạ và đỡ đòn xuất quỷ nhập thần.',
    'class.linggango.class_enhancement.custom.desc3': 'Khả năng tiêu hóa đặc biệt, chuyển hóa thức ăn thành lớp giáp hấp thụ sát thương.',
    'class.linggango.class_enhancement.custom.desc4': 'Đại sư vũ khí, phát huy uy lực tối đa của cả vũ khí nhẹ lẫn trọng khí.'
}

# Apply to all 3 lang files in resources/assets
count_applied = 0
for ns in sorted(os.listdir(ASSETS_BASE)):
    lang_dir = os.path.join(ASSETS_BASE, ns, 'lang')
    if not os.path.exists(lang_dir):
        continue
    
    for lf in ['en_us.json', 'zh_cn.json', 'vi_vn.json']:
        lp = os.path.join(lang_dir, lf)
        if os.path.exists(lp):
            with open(lp, 'r', encoding='utf-8') as f:
                d = json.load(f)
            
            modified = False
            for k, target_val in overrides.items():
                if k in d and d[k] != target_val:
                    d[k] = target_val
                    modified = True
                    count_applied += 1
            
            # Also check any enchantment.<ns>.<id> that might not be in explicit overrides
            for k, v in list(d.items()):
                if k.startswith('enchantment.') and not any(k.endswith(s) for s in ['.desc', '_desc', '.description', '_description', '.info', '_info']):
                    if viet_chars.search(str(v)):
                        # Look in master_en
                        if k in master_en and not viet_chars.search(master_en[k]):
                            eng_val = master_en[k]
                        else:
                            parts = k.split('.')
                            eng_val = to_title(parts[-1])
                        d[k] = eng_val
                        modified = True
                        count_applied += 1
            
            if modified:
                with open(lp, 'w', encoding='utf-8') as f:
                    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"Applied {count_applied} enchantment and tab updates across language files!")
