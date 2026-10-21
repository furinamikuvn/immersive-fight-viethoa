import zipfile, re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

CHINESE_RE = re.compile(r'[\u4e00-\u9fff]+')

mods_dir = Path(r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\mods")

results = {}

for jar in sorted(mods_dir.glob("*.jar")):
    try:
        with zipfile.ZipFile(jar) as z:
            for n in z.namelist():
                if n.endswith(".class"):
                    raw = z.read(n)
                    text = raw.decode("utf-8", errors="ignore")
                    matches = CHINESE_RE.findall(text)
                    if matches:
                        # filter out single char artifacts from binary data
                        real_matches = [m for m in matches if len(m) >= 2]
                        if real_matches:
                            results.setdefault(jar.name, {})[n] = real_matches
    except:
        pass

print(f"Total jars with real Chinese strings: {len(results)}")
for jar_name, class_dict in results.items():
    print(f"\n==================================================")
    print(f"JAR: {jar_name} ({len(class_dict)} classes)")
    print(f"==================================================")
    for clz, strings in class_dict.items():
        # Deduplicate
        unique_strings = list(dict.fromkeys(strings))
        print(f"  {clz}: {unique_strings}")
