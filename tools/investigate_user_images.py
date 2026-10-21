import zipfile, os, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

queries = [
    '右键获得伤害吸收', 
    '活尸掉落', 
    'The demon is sealed inside this blade', 
    'Satsujin', 
    'Armor Negation', 
    'to see Innate skill',
    'Doppelganger',
    'other_items_tab'
]

mods_dir = Path(r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\mods")
print(f"Searching in {mods_dir}...")

for jar in sorted(mods_dir.glob("*.jar")):
    try:
        with zipfile.ZipFile(jar) as z:
            for n in z.namelist():
                # only check text files or class files
                if n.endswith(('.json', '.class', '.lang', '.toml', '.txt', '.snbt', '.mcmeta')):
                    try:
                        raw = z.read(n)
                        # search binary string or decode utf-8
                        for q in queries:
                            q_bytes = q.encode('utf-8')
                            if q_bytes in raw:
                                print(f"[JAR] {jar.name} -> {n} (matched: {q})")
                    except:
                        pass
    except:
        pass

print("\nSearching in game resources/...")
res_dir = Path(r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\resources")
for p in res_dir.rglob("*.json"):
    try:
        txt = p.read_text(encoding='utf-8', errors='ignore')
        for q in queries:
            if q in txt:
                print(f"[RES] {p.relative_to(res_dir)} (matched: {q})")
    except:
        pass

print("\nSearching in global_packs/ and config/...")
game_dir = Path(r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1")
for folder in ['config', 'global_packs', 'kubejs']:
    fpath = game_dir / folder
    if fpath.exists():
        for p in fpath.rglob("*"):
            if p.is_file() and p.suffix in ('.json', '.js', '.snbt', '.toml', '.txt'):
                try:
                    txt = p.read_text(encoding='utf-8', errors='ignore')
                    for q in queries:
                        if q in txt:
                            print(f"[{folder}] {p.relative_to(game_dir)} (matched: {q})")
                except:
                    pass
