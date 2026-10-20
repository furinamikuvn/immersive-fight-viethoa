import os
import sys
import re
import zipfile

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

chinese_regex = re.compile(r'[\u4e00-\u9fff]+')

base_folder = r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh"

files_to_inspect = [
    os.path.join(base_folder, "hotai", "com", "latxx", "fight_more", "events", "SculkWardenSummoner.badiff"),
    os.path.join(base_folder, "hotai", "dev", "ftb", "mods", "ftbultimine", "FTBUltimineCommands.badiff"),
    os.path.join(base_folder, "hotai", "it", "hurts", "sskirillss", "relics", "items", "relics", "HorseFluteItem.badiff"),
    os.path.join(base_folder, "hotai", "it", "hurts", "sskirillss", "relics", "items", "relics", "MagicMirrorItem.badiff"),
    os.path.join(base_folder, "hotai", "net", "m3tte", "tactical_imbuements", "item", "FlameFlaskItem.badiff"),
    os.path.join(base_folder, "hotai", "net", "mcreator", "borninchaosv", "procedures", "WarningSoundProcedure.badiff"),
    os.path.join(base_folder, "hotai", "net", "mcreator", "mofusbetterend", "item", "EndWarriorArmorItem$Chestplate.badiff"),
    os.path.join(base_folder, "hotai", "net", "mcreator", "mofusbetterend", "item", "GuardianCannonItem.badiff"),
    os.path.join(base_folder, "hotai", "net", "mcreator", "mofusbetterend", "item", "MechanicalFosendEyeItem.badiff"),
    os.path.join(base_folder, "hotai", "net", "shelmarow", "nightfall_invade", "entity", "scarlet_hunter", "ScarletHunter.badiff"),
    os.path.join(base_folder, "config", "sword_soaring-common.toml")
]

for fp in files_to_inspect:
    if os.path.exists(fp):
        with open(fp, "rb") as f:
            data = f.read()
        text = data.decode("utf-8", errors="ignore")
        matches = chinese_regex.findall(text)
        print(f"=== {os.path.basename(fp)} ===")
        for m in set(matches):
            if len(m) > 1 or ord(m[0]) > 0x4e00:
                print(f"  '{m}'")

# Check Reimagined splashes
reimagined = os.path.join(base_folder, "resourcepacks", "Reimagined.zip")
with zipfile.ZipFile(reimagined, "r") as zf:
    splashes = zf.read("assets/minecraft/texts/splashes.txt").decode("utf-8", errors="ignore")
    ch = chinese_regex.findall(splashes)
    print(f"=== Reimagined splashes.txt ===\n  Chinese found: {set(ch)}")
