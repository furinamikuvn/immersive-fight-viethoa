# -*- coding: utf-8 -*-
"""
inject_translations_into_mod_jars.py
Injects the translated en_us.json, zh_cn.json, and vi_vn.json directly into:
1. Every matching mod JAR across all 3 mods/ directories.
2. IMF-Modify.zip in all resourcepacks/ directories.
This achieves true DIRECT TRANSLATION (dịch trực tiếp vào file mod),
completely removing dependency on resource packs or external loaders.
"""

import os, zipfile, json, shutil

assets_base = r"Immersive Fight 4.2.9 Viet Hoa\resources\assets"

mods_dirs = [
    r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\mods",
    r"Immersive Fight 4.2.9\mods",
    r"Immersive Fight 4.2.9 Viet Hoa\mods"
]

rp_dirs = [
    r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\resourcepacks",
    r"Immersive Fight 4.2.9\resourcepacks",
    r"Immersive Fight 4.2.9 Viet Hoa\resourcepacks"
]

# Load all translation files in memory
translations_cache = {}
namespaces = [d for d in os.listdir(assets_base) if os.path.isdir(os.path.join(assets_base, d))]
print(f"Loading translations for {len(namespaces)} namespaces...")

for ns in namespaces:
    lang_dir = os.path.join(assets_base, ns, "lang")
    if not os.path.exists(lang_dir):
        continue
    translations_cache[ns] = {}
    for lang in ["en_us.json", "zh_cn.json", "vi_vn.json"]:
        p = os.path.join(lang_dir, lang)
        if os.path.exists(p):
            with open(p, "rb") as f:
                translations_cache[ns][lang] = f.read()

print(f"Cached {len(translations_cache)} namespaces.")

def patch_zip_archive(zip_path, is_resourcepack=False):
    if not os.path.exists(zip_path):
        return 0

    temp_path = zip_path + ".injecting.tmp"
    injected_count = 0

    try:
        with zipfile.ZipFile(zip_path, "r") as zin:
            namelist = zin.namelist()
            # Detect namespaces in this jar/zip
            matched_ns = set()
            for name in namelist:
                if name.startswith("assets/"):
                    parts = name.split("/")
                    if len(parts) >= 2:
                        candidate = parts[1]
                        if candidate in translations_cache:
                            matched_ns.add(candidate)

            if not matched_ns:
                return 0

            with zipfile.ZipFile(temp_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
                # Set of entry paths to override
                override_paths = {}
                for ns in matched_ns:
                    for lang, data in translations_cache[ns].items():
                        target_entry = f"assets/{ns}/lang/{lang}"
                        override_paths[target_entry] = data

                # Copy existing entries, skipping any that we are overriding
                for item in zin.infolist():
                    if item.filename in override_paths:
                        continue
                    # Also skip any uppercase or weird variations if needed
                    zout.writestr(item, zin.read(item.filename))

                # Now write all our updated / new lang files
                for entry_name, data in override_paths.items():
                    zout.writestr(entry_name, data)
                    injected_count += 1

        # Replace original
        os.replace(temp_path, zip_path)
        return injected_count
    except Exception as e:
        print(f"Error patching {zip_path}: {e}")
        if os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except:
                pass
        return 0


# 1. Patch all mod JARs
total_patched_jars = 0
total_injected_files = 0

for mdir in mods_dirs:
    if not os.path.exists(mdir):
        continue
    print(f"\n================ Injecting into mods in: {mdir} ================")
    jar_files = [f for f in os.listdir(mdir) if f.endswith(".jar")]
    for jf in jar_files:
        jp = os.path.join(mdir, jf)
        count = patch_zip_archive(jp)
        if count > 0:
            total_patched_jars += 1
            total_injected_files += count
            print(f"  Injected {count} lang files into {jf}")

print(f"\nSuccessfully injected translations into {total_patched_jars} mod JARs ({total_injected_files} lang files total)!")

# 2. Patch IMF-Modify.zip in resourcepacks
print("\n================ Updating IMF-Modify.zip in resourcepacks ================")
for rdir in rp_dirs:
    if not os.path.exists(rdir):
        continue
    imf_mod = os.path.join(rdir, "IMF-Modify.zip")
    if os.path.exists(imf_mod):
        count = patch_zip_archive(imf_mod, is_resourcepack=True)
        print(f"  Updated IMF-Modify.zip in {rdir}: {count} lang files synchronized.")

print("\nDirect mod translation injection complete!")
