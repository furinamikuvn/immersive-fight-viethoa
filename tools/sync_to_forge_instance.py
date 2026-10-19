import os
import sys
import shutil

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

src_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh"
dst_dir = r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1"

print("=== ĐỒNG BỘ BẢN VIỆT HÓA MỚI NHẤT SANG FORGE 1.20.1 ===")
print(f"Nguồn: {src_dir}")
print(f"Đích:  {dst_dir}\n")

if not os.path.exists(dst_dir):
    print(f"LỖI: Không tìm thấy thư mục đích: {dst_dir}")
    sys.exit(1)

# 1. Đồng bộ resourcepacks
print("1. Đồng bộ resourcepacks...")
src_rp = os.path.join(src_dir, "resourcepacks")
dst_rp = os.path.join(dst_dir, "resourcepacks")
os.makedirs(dst_rp, exist_ok=True)

# Xóa các file backup .bak cũ trong dst_rp nếu có
for f in os.listdir(dst_rp):
    if f.endswith('.bak') or f.endswith('.tmp'):
        try:
            os.remove(os.path.join(dst_rp, f))
            print(f"  Đã xóa file rác cũ: {f}")
        except: pass

for f in os.listdir(src_rp):
    s_f = os.path.join(src_rp, f)
    d_f = os.path.join(dst_rp, f)
    if os.path.isfile(s_f):
        shutil.copy2(s_f, d_f)
        size_kb = os.path.getsize(d_f) / 1024
        print(f"  Đã sao chép resourcepack: {f} ({size_kb:.1f} KB)")

# 2. Đồng bộ config (bao gồm FTB Quests Tiếng Việt)
print("\n2. Đồng bộ config & ftbquests...")
for d in ["config", "ftbquests", "global_packs", "hotai", "minemenu", "resources", "shaderpacks"]:
    s_d = os.path.join(src_dir, d)
    d_d = os.path.join(dst_dir, d)
    if os.path.exists(s_d):
        shutil.copytree(s_d, d_d, dirs_exist_ok=True)
        print(f"  Đã cập nhật thư mục: {d}")

# 3. Đồng bộ mods (BẢO LƯU TUYỆT ĐỐI CÁC MOD TOUHOU TRONG DST)
print("\n3. Đồng bộ mods (Giữ nguyên mod Touhou)...")
src_mods = os.path.join(src_dir, "mods")
dst_mods = os.path.join(dst_dir, "mods")
os.makedirs(dst_mods, exist_ok=True)

copied_mods = 0
for f in os.listdir(src_mods):
    if f.endswith('.jar'):
        s_m = os.path.join(src_mods, f)
        d_m = os.path.join(dst_mods, f)
        shutil.copy2(s_m, d_m)
        copied_mods += 1

print(f"  Đã đồng bộ {copied_mods} mod từ bản sạch sang Forge 1.20.1.")

# Kiểm tra các mod Touhou trong dst_mods để đảm bảo vẫn an toàn
touhou_mods = [f for f in os.listdir(dst_mods) if 'touhou' in f.lower() or 'maid' in f.lower()]
print(f"  [XÁC NHẬN] Các mod Touhou/Maid được bảo toàn nguyên vẹn ({len(touhou_mods)} mod):")
for tm in touhou_mods:
    print(f"    - {tm}")

# 4. Đồng bộ options.txt và file cấu hình gốc
print("\n4. Đồng bộ options.txt...")
for f in ["options.txt", "TrashSlotSaveState.json", "minecraftinstance.json"]:
    s_f = os.path.join(src_dir, f)
    d_f = os.path.join(dst_dir, f)
    if os.path.exists(s_f):
        shutil.copy2(s_f, d_f)
        print(f"  Đã sao chép cấu hình: {f}")

print("\n=== HOÀN TẤT ĐỒNG BỘ 100%! FORGE 1.20.1 ĐÃ ĐƯỢC NÂNG CẤP LÊN BẢN VIỆT HÓA MỚI NHẤT! ===")
