import os
import sys
import json
import re

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
ns_dir = os.path.join(base_dir, "tools", "master_extracted", "namespaces")
re_chinese = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]')

# Check existing dict
existing_dict_path = os.path.join(base_dir, "tools", "rp_translation_dict.json")
existing_dict = {}
if os.path.exists(existing_dict_path):
    with open(existing_dict_path, 'r', encoding='utf-8') as f:
        existing_dict = json.load(f)

# Patterns that indicate an item/block/entity NAME rather than a description/tooltip
NAME_PREFIXES = ('item.', 'block.', 'entity.', 'biome.')
DESC_PATTERNS = (
    '.desc', '.description', '.tooltip', '.lore', '.info', '.effect', 
    '.skill', '.ability', '.title', '.subtitle', 'tooltip', 'desc'
)

def is_name_key(key):
    # Check if key represents a name
    is_name_type = any(key.startswith(p) for p in NAME_PREFIXES)
    has_desc_tag = any(p in key.lower() for p in DESC_PATTERNS)
    return is_name_type and not has_desc_tag

already_resolved = 0
name_keys_to_en = 0
need_zh_to_vi = {} # zh_text -> list of (ns, key)
need_en_to_vi = {} # en_text -> list of (ns, key)
untranslated_count = 0

for ns_file in os.listdir(ns_dir):
    if not ns_file.endswith('.json'): continue
    ns = ns_file[:-5]
    with open(os.path.join(ns_dir, ns_file), 'r', encoding='utf-8') as f:
        keys = json.load(f)
        
    for k, v in keys.items():
        vi = v.get('vi')
        en = v.get('en')
        zh = v.get('zh')
        
        # Check if already resolved with valid Vietnamese
        if vi and not re_chinese.search(vi):
            already_resolved += 1
            continue
            
        # If it's an Item/Block/Entity name and English is available
        if is_name_key(k) and en and not re_chinese.search(en):
            name_keys_to_en += 1
            continue
            
        # Otherwise, this key needs translation into Vietnamese!
        # Prefer translating from Chinese if original mod author wrote custom Chinese lore (IMF-Trans or Chinese mod)
        if zh and re_chinese.search(zh):
            if zh in existing_dict:
                already_resolved += 1
            else:
                if zh not in need_zh_to_vi: need_zh_to_vi[zh] = []
                need_zh_to_vi[zh].append((ns, k))
                untranslated_count += 1
        elif en:
            if en in existing_dict:
                already_resolved += 1
            else:
                if en not in need_en_to_vi: need_en_to_vi[en] = []
                need_en_to_vi[en].append((ns, k))
                untranslated_count += 1
        elif zh: # Chinese without Chinese characters (ascii)
            already_resolved += 1

print(f"=== TRANSLATION ANALYSIS REPORT ===")
print(f"Total already resolved: {already_resolved}")
print(f"Item/Block/Entity names mapped to English: {name_keys_to_en}")
print(f"Unique Chinese strings needing translation to Vietnamese: {len(need_zh_to_vi)}")
print(f"Unique English strings needing translation to Vietnamese: {len(need_en_to_vi)}")
print(f"Total untranslated occurrences: {untranslated_count}")

# Save the unique Chinese strings needing translation
with open(os.path.join(base_dir, "tools", "master_extracted", "unique_zh_needed.json"), 'w', encoding='utf-8') as f:
    json.dump(list(need_zh_to_vi.keys()), f, ensure_ascii=False, indent=2)

with open(os.path.join(base_dir, "tools", "master_extracted", "unique_en_needed.json"), 'w', encoding='utf-8') as f:
    json.dump(list(need_en_to_vi.keys()), f, ensure_ascii=False, indent=2)

print("Saved unique_zh_needed.json and unique_en_needed.json successfully.")
