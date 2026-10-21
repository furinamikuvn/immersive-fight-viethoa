# -*- coding: utf-8 -*-
"""
run_bytecode_patcher.py
Applies BytecodeChinesePatcher across the target mod JARs in:
1. Game instance mods folder
2. Immersive Fight 4.2.9/mods
3. Immersive Fight 4.2.9 Viet Hoa/mods
"""

import os, subprocess

java_bin = r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\jre\java-runtime-gamma\windows-x64\java-runtime-gamma\bin\java.exe"
cp = r"tools;C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\org\ow2\asm\asm\9.10.1\asm-9.10.1.jar;C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\libraries\org\ow2\asm\asm-tree\9.10.1\asm-tree-9.10.1.jar"
tsv = r"tools\bytecode_replacements.tsv"

target_jar_patterns = [
    "soul_like_armors_reworked",
    "soul like mobs",
    "womalt",
    "EpicFight Nightfall",
    "promaid"
]

mods_dirs = [
    r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\mods",
    r"Immersive Fight 4.2.9\mods",
    r"Immersive Fight 4.2.9 Viet Hoa\mods"
]

for d in mods_dirs:
    if not os.path.exists(d):
        continue
    print(f"\n================ Scanning: {d} ================")
    for fname in os.listdir(d):
        if not fname.endswith(".jar"):
            continue
        if any(p.lower() in fname.lower() for p in target_jar_patterns):
            jar_path = os.path.join(d, fname)
            print(f"\nPatching: {jar_path}")
            cmd = [java_bin, "-Dfile.encoding=UTF-8", "-cp", cp, "BytecodeChinesePatcher", tsv, jar_path]
            res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
            print(res.stdout)
            if res.stderr:
                print("ERR:", res.stderr)

print("\nAll target bytecode jars patched successfully!")
