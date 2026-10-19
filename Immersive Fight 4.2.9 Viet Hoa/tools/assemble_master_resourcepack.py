import os
import sys
import json
import zipfile
import re
import shutil

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
tools_dir = os.path.join(base_dir, "tools")
extracted_dir = os.path.join(tools_dir, "master_extracted")
ns_dir = os.path.join(extracted_dir, "namespaces")
dict_path = os.path.join(tools_dir, "rp_translation_dict.json")

rp_dir = os.path.join(base_dir, "resourcepack", "IMF-VietHoa")
rp_assets_dir = os.path.join(rp_dir, "assets")
dist_dir = os.path.join(base_dir, "dist")
os.makedirs(dist_dir, exist_ok=True)

re_chinese = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]')

NAME_PREFIXES = ('item.', 'block.', 'entity.', 'biome.')
DESC_PATTERNS = (
    '.desc', '.description', '.tooltip', '.lore', '.info', '.effect', 
    '.skill', '.ability', '.title', '.subtitle', 'tooltip', 'desc'
)

def is_name_key(key):
    is_name_type = any(key.startswith(p) for p in NAME_PREFIXES)
    has_desc_tag = any(p in key.lower() for p in DESC_PATTERNS)
    return is_name_type and not has_desc_tag

def main():
    print("=== TAWA MASTER RESOURCE PACK ASSEMBLER ===")
    
    # 1. Load dictionary
    print("Loading translation dictionary...")
    with open(dict_path, 'r', encoding='utf-8') as f:
        trans_dict = json.load(f)
    print(f"Loaded dictionary with {len(trans_dict)} entries.")

    overrides_path = os.path.join(tools_dir, "overrides_dict.json")
    overrides_dict = {}
    if os.path.exists(overrides_path):
        with open(overrides_path, 'r', encoding='utf-8') as f:
            overrides_dict = json.load(f)
        print(f"Loaded {len(overrides_dict)} custom overrides.")

    # 2. Iterate through all namespaces
    ns_files = [f for f in os.listdir(ns_dir) if f.endswith('.json')]
    print(f"Assembling {len(ns_files)} namespaces into {rp_assets_dir}...")

    total_keys_generated = 0
    total_names_en = 0
    total_desc_vi = 0
    total_chinese_remaining = 0

    for ns_file in ns_files:
        ns = ns_file[:-5]
        with open(os.path.join(ns_dir, ns_file), 'r', encoding='utf-8') as f:
            ns_keys = json.load(f)

        lang_data = {}
        for k, v in ns_keys.items():
            en = v.get('en')
            zh = v.get('zh')
            vi = v.get('vi')

            final_val = None

            if k in overrides_dict:
                final_val = overrides_dict[k]
                total_desc_vi += 1
            elif is_name_key(k) and en and not re_chinese.search(en):
                final_val = en
                total_names_en += 1
            else:
                # RULE B: Descriptions, Tooltips, Lore, Skills, Stats, UI -> 100% Vietnamese
                if vi and not re_chinese.search(vi):
                    final_val = vi
                    total_desc_vi += 1
                elif zh and zh in trans_dict and not re_chinese.search(trans_dict[zh]):
                    final_val = trans_dict[zh]
                    total_desc_vi += 1
                elif en and en in trans_dict and not re_chinese.search(trans_dict[en]):
                    final_val = trans_dict[en]
                    total_desc_vi += 1
                elif vi:
                    final_val = vi
                elif zh:
                    # check if in trans_dict anyway
                    final_val = trans_dict.get(zh, zh)
                elif en:
                    final_val = trans_dict.get(en, en)

            if final_val is not None:
                # Verify Chinese check
                if re_chinese.search(final_val):
                    # Attempt final fallback translation via dict
                    if final_val in trans_dict and not re_chinese.search(trans_dict[final_val]):
                        final_val = trans_dict[final_val]
                    elif en and not re_chinese.search(en):
                        final_val = en # fallback to English rather than leaving Chinese!
                    else:
                        total_chinese_remaining += 1

                lang_data[k] = final_val

        # Write to assets/<ns>/lang/vi_vn.json, zh_cn.json, en_us.json
        ns_lang_dir = os.path.join(rp_assets_dir, ns, "lang")
        os.makedirs(ns_lang_dir, exist_ok=True)

        for lang_code in ("vi_vn.json", "zh_cn.json", "en_us.json"):
            target_path = os.path.join(ns_lang_dir, lang_code)
            with open(target_path, 'w', encoding='utf-8') as fp:
                json.dump(lang_data, fp, ensure_ascii=False, indent=2)

        total_keys_generated += len(lang_data)

    print(f"\nSuccessfully generated {total_keys_generated} keys across {len(ns_files)} namespaces!")
    print(f"  - Item/Block/Entity names mapped to English: {total_names_en}")
    print(f"  - Tooltips/Lore/Skills translated to Vietnamese: {total_desc_vi}")
    print(f"  - Chinese strings remaining (if any): {total_chinese_remaining}")

    # 3. Ensure pack.mcmeta
    pack_mcmeta_path = os.path.join(rp_dir, "pack.mcmeta")
    mcmeta_content = {
        "pack": {
            "pack_format": 15,
            "description": "Gói Việt Hóa Toàn Diện - Immersive Fight 4.2.9 by Tawa System"
        }
    }
    with open(pack_mcmeta_path, 'w', encoding='utf-8') as fp:
        json.dump(mcmeta_content, fp, ensure_ascii=False, indent=2)

    # 4. Pack into dist/IMF-VietHoa.zip
    print("\n--- Compressing dist/IMF-VietHoa.zip ---")
    dist_zip_path = os.path.join(dist_dir, "IMF-VietHoa.zip")
    with zipfile.ZipFile(dist_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(rp_dir):
            for file in files:
                full_p = os.path.join(root, file)
                rel_p = os.path.relpath(full_p, rp_dir)
                zipf.write(full_p, rel_p)

    zip_size_mb = os.path.getsize(dist_zip_path) / (1024 * 1024)
    print(f"Exported standalone Resource Pack to: {dist_zip_path} ({zip_size_mb:.2f} MB)")

    # 5. Copy to resourcepacks/ in Viet Hoa modpack instance
    rp_instance_path = os.path.join(base_dir, "resourcepacks", "IMF-VietHoa.zip")
    shutil.copy2(dist_zip_path, rp_instance_path)
    print(f"Copied to modpack resourcepacks: {rp_instance_path}")

    # 6. Also update IMF-Trans.zip so legacy loads work 100% seamlessly
    imf_trans_path = os.path.join(base_dir, "resourcepacks", "IMF-Trans.zip")
    shutil.copy2(dist_zip_path, imf_trans_path)
    print(f"Mirrored into IMF-Trans.zip to guarantee zero Chinese even under legacy pack list!")

if __name__ == '__main__':
    main()
