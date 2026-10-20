import os
import zipfile

mods_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\mods"
targets = [
    "com/latxx/fight_more/events/SculkWardenSummoner.class",
    "dev/ftb/mods/ftbultimine/FTBUltimineCommands.class",
    "it/hurts/sskirillss/relics/items/relics/MagicMirrorItem.class",
    "net/mcreator/borninchaosv/procedures/WarningSoundProcedure.class"
]

for t in targets:
    found = False
    for f in os.listdir(mods_dir):
        if f.endswith('.jar'):
            try:
                with zipfile.ZipFile(os.path.join(mods_dir, f), 'r') as zf:
                    if t in zf.namelist():
                        print(f"Found {t} in {f}")
                        found = True
                        break
            except:
                pass
    if not found:
        print(f"NOT FOUND: {t}")
