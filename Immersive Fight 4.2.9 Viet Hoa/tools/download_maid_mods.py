import os
import sys
import urllib.request
import zipfile

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
dl_dir = os.path.join(base_dir, "downloads", "maid_mods")
os.makedirs(dl_dir, exist_ok=True)

targets = [
    {
        "name": "touhoulittlemaid-1.5.3-forge+mc1.20.1.jar",
        "url": "https://cdn.modrinth.com/data/R0bDWFAW/versions/g1SKoGQJ/touhoulittlemaid-1.5.3-forge%2Bmc1.20.1.jar"
    },
    {
        "name": "promaid-1.3.2-forge-1.20.1.jar",
        "url": "https://edge.forgecdn.net/files/9194/461/promaid-1.3.2-forge-1.20.1.jar"
    },
    {
        "name": "1.20.1-maid_useful_task-1.4.2.jar",
        "url": "https://edge.forgecdn.net/files/7909/118/1.20.1-maid_useful_task-1.4.2.jar"
    }
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for t in targets:
    out_path = os.path.join(dl_dir, t["name"])
    print(f"Downloading {t['name']}...")
    req = urllib.request.Request(t["url"], headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
        with open(out_path, 'wb') as f:
            f.write(data)
    size_mb = os.path.getsize(out_path) / (1024 * 1024)
    print(f"  -> Saved {t['name']} ({size_mb:.2f} MB)")
    
    # Verify it is a valid zip
    with zipfile.ZipFile(out_path, 'r') as z:
        print(f"  -> Valid JAR! Total entries: {len(z.namelist())}")

print("\nAll 3 mods downloaded and verified successfully!")
