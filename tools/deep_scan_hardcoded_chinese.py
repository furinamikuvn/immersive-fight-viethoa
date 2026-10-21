import zipfile, re, sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

CHINESE_RE = re.compile(r'[\u4e00-\u9fff]{2,}')

mods_dir = Path(r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\mods")
print(f"Deep scanning all jars in {mods_dir} for hardcoded Chinese in .class files...")

jar_results = {}

for jar in sorted(mods_dir.glob("*.jar")):
    try:
        with zipfile.ZipFile(jar) as z:
            for n in z.namelist():
                if n.endswith(".class"):
                    try:
                        raw = z.read(n)
                        # decode ignoring errors to find Chinese unicode sequences
                        text = raw.decode("utf-8", errors="ignore")
                        matches = CHINESE_RE.findall(text)
                        if matches:
                            # Filter out false positives (single random bytes)
                            real_matches = [m for m in matches if len(m) >= 2]
                            if real_matches:
                                jar_results.setdefault(jar.name, []).append((n, real_matches))
                    except:
                        pass
    except Exception as e:
        print(f"Error reading {jar.name}: {e}")

print(f"\nFound {len(jar_results)} jars with hardcoded Chinese strings in bytecode:")
total_classes = 0
total_strings = 0

for jar_name, classes in jar_results.items():
    print(f"\n=== {jar_name} ({len(classes)} classes) ===")
    total_classes += len(classes)
    for clz, matches in classes[:10]:
        print(f"  {clz}: {matches[:5]}")
        total_strings += len(matches)
    if len(classes) > 10:
        print(f"  ... and {len(classes) - 10} more classes")

print(f"\nTotal: {total_classes} classes in {len(jar_results)} jars contain {total_strings}+ hardcoded Chinese strings!")
