import urllib.request
import os
import shutil

url = "https://cdn.modrinth.com/data/rOUBggPv/versions/eTAXn3Y2/supermartijn642corelib-1.1.25a-forge-mc1.20.1.jar"
new_jar_name = "supermartijn642corelib-1.1.25a-forge-mc1.20.1.jar"
temp_download = os.path.join(r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\tools", new_jar_name)

print("Downloading updated supermartijn642corelib from Modrinth...")
req = urllib.request.Request(url, headers={"User-Agent": "Antigravity/1.0"})
with urllib.request.urlopen(req, timeout=30) as r, open(temp_download, 'wb') as f:
    f.write(r.read())

print(f"Downloaded {os.path.getsize(temp_download)} bytes.")

targets = [
    r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\mods",
    r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\mods"
]

for t in targets:
    if os.path.exists(t):
        old_jar = os.path.join(t, "supermartijn642corelib-1.1.15-forge-mc1.20.jar")
        if os.path.exists(old_jar):
            os.remove(old_jar)
            print(f"Removed old jar: {old_jar}")
        target_jar = os.path.join(t, new_jar_name)
        shutil.copy2(temp_download, target_jar)
        print(f"Installed updated jar to: {target_jar}")

print("Fix completed successfully!")
