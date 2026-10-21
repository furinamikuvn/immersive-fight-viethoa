# -*- coding: utf-8 -*-
"""
sync_all_resources.py
Synchronizes all assets from 'Immersive Fight 4.2.9 Viet Hoa/resources/assets' to:
1. C:/Users/ADMIN/.../Forge 1.20.1/resources/assets
2. Immersive Fight 4.2.9/resources/assets
AND also creates flat namespace mappings 'resources/<namespace>' in both places
so that keksuccino's LMRPackResources can load them natively if it inspects either path.
"""

import os, shutil

src_assets = r"Immersive Fight 4.2.9 Viet Hoa\resources\assets"

destinations = [
    r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\resources",
    r"Immersive Fight 4.2.9\resources"
]

namespaces = [d for d in os.listdir(src_assets) if os.path.isdir(os.path.join(src_assets, d))]
print(f"Syncing {len(namespaces)} namespaces to destinations...")

for dest_root in destinations:
    if not os.path.exists(dest_root):
        continue
    dest_assets = os.path.join(dest_root, "assets")
    os.makedirs(dest_assets, exist_ok=True)
    
    for ns in namespaces:
        src_ns_dir = os.path.join(src_assets, ns)
        dest_ns_dir = os.path.join(dest_assets, ns)
        
        # 1. Sync to dest/assets/<ns>
        shutil.copytree(src_ns_dir, dest_ns_dir, dirs_exist_ok=True)
        
        # 2. Also sync to dest/<ns> (flat structure for LMR fallback)
        dest_flat_ns = os.path.join(dest_root, ns)
        shutil.copytree(src_ns_dir, dest_flat_ns, dirs_exist_ok=True)

print("Resource sync completed successfully across all destinations!")
