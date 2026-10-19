import os
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

src_base = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
dst_base = r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1"

if not os.path.exists(dst_base):
    print(f"ERROR: Destination directory does not exist: {dst_base}")
    sys.exit(1)

print(f"Synchronizing from:\n  {src_base}\nto:\n  {dst_base}\n")

# 1. Sync resourcepacks
rp_files = [
    "IMF-Trans.zip",
    "IMF-Modify.zip",
    "BDHill Reforge the Sword Edge 沉浸特供.zip",
    "THU_TU_RESOURCEPACK_MAC_DINH.txt"
]

src_rp = os.path.join(src_base, "resourcepacks")
dst_rp = os.path.join(dst_base, "resourcepacks")
os.makedirs(dst_rp, exist_ok=True)

for f in rp_files:
    sp = os.path.join(src_rp, f)
    dp = os.path.join(dst_rp, f)
    if os.path.exists(sp):
        shutil.copy2(sp, dp)
        print(f"Copied resourcepack: {f} ({os.path.getsize(dp) / 1024:.1f} KB)")

# Remove any old garbled txt in game dst_rp
for f in os.listdir(dst_rp):
    if f.endswith('.txt') and f != "THU_TU_RESOURCEPACK_MAC_DINH.txt":
        try:
            os.remove(os.path.join(dst_rp, f))
            print(f"Removed old txt: {f}")
        except:
            pass

# 2. Sync config/class_enhancement.toml and others
configs_to_sync = [
    "class_enhancement.toml",
    "beyonddimensions-common.toml",
    "epicfightx.toml",
    "epicgoop-client.toml",
    "fight_more-client.toml",
    "invincible-common.toml",
    "nightfall_invade-common.toml",
    "petconnect-common.toml",
    "simplyusekey-client.toml",
    "smartkeyprompts-client.toml",
    "sword_soaring-common.toml"
]

src_cfg = os.path.join(src_base, "config")
dst_cfg = os.path.join(dst_base, "config")

for c in configs_to_sync:
    sp = os.path.join(src_cfg, c)
    dp = os.path.join(dst_cfg, c)
    if os.path.exists(sp):
        shutil.copy2(sp, dp)
        print(f"Copied config: {c}")

# Sync config/ftbquests
src_ftb = os.path.join(src_cfg, "ftbquests")
dst_ftb = os.path.join(dst_cfg, "ftbquests")
if os.path.exists(src_ftb):
    if os.path.exists(dst_ftb):
        shutil.rmtree(dst_ftb)
    shutil.copytree(src_ftb, dst_ftb)
    print("Copied full ftbquests config directory")

# 3. Sync global_packs
src_gp = os.path.join(src_base, "global_packs")
dst_gp = os.path.join(dst_base, "global_packs")
if os.path.exists(src_gp):
    if os.path.exists(dst_gp):
        shutil.rmtree(dst_gp)
    shutil.copytree(src_gp, dst_gp)
    print("Copied full global_packs directory")

print("\nSYNCHRONIZATION COMPLETED SUCCESSFULLY! All changes are live in game folder!")
