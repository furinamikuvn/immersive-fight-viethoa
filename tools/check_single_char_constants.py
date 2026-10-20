import os
import sys

base_folder = r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh"
hotai_dir = os.path.join(base_folder, "hotai")

single_char_files = [
    "com/asanginxst/epicfightx/capabilities/item/WeaponCapabilityPresetsX.badiff",
    "com/asanginxst/epicfightx/mixin/PlayerPatchMixin.badiff",
    "com/dudenduke/hudalternatives/minimalmodern/MinimalModernOverlay.badiff",
    "com/misanthropy/linggango/class_enhancement/client/ClassSelectionScreen$StyledButton.badiff",
    "com/peeko32213/notsoshrimple/common/entity/EntityCrayfish$CrayfishMeleeAttackGoal.badiff",
    "reascer/wom/skill/guard/CounterAttack.badiff",
    "reascer/wom/skill/weaponpassive/SolarPassiveSkill.badiff"
]

for rel in single_char_files:
    p = os.path.join(hotai_dir, rel.replace('/', os.sep))
    if os.path.exists(p):
        with open(p, "rb") as fp:
            data = fp.read()
        # Find if it occurs as a CONSTANT_Utf8 (tag 1: 0x01, len_high, len_low, bytes)
        print(f"File {rel}: {len(data)} bytes")
        # Let's search for UTF-8 patterns
        for i in range(len(data) - 4):
            if data[i] == 1: # Tag Utf8
                l = (data[i+1] << 8) | data[i+2]
                if l < 200 and i + 3 + l <= len(data):
                    try:
                        s = data[i+3 : i+3+l].decode('utf-8')
                        if any(ord(c) >= 0x4e00 and ord(c) <= 0x9fa5 for c in s):
                            print(f"  -> Constant UTF-8: '{s}'")
                    except:
                        pass
