import os
import sys
import shutil
import zipfile

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

src_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
target_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 - Cai Dat Nhanh"

print(f"=== KHỞI TẠO THƯ MỤC CÀI ĐẶT 1 CHẠM ===")
print(f"Nguồn: {src_dir}")
print(f"Đích:  {target_dir}\n")

if os.path.exists(target_dir):
    print(f"Dọn dẹp thư mục đích cũ: {target_dir}...")
    shutil.rmtree(target_dir, ignore_errors=True)

os.makedirs(target_dir, exist_ok=True)

# 1. Các thư mục cốt lõi CẦN THIẾT cho game
essential_dirs = [
    "config",
    "ftbquests",
    "global_packs",
    "hotai",
    "minemenu",
    "mods",
    "resourcepacks",
    "resources",
    "shaderpacks"
]

# Các file rác hoặc backup cần loại trừ tuyệt đối
excluded_extensions = {".bak", ".tmp", ".log"}
excluded_filenames = {
    "IMF-Trans.zip.bak",
    "IMF-Trans-temp.zip",
    ".git",
    ".gitignore"
}

for d in essential_dirs:
    s_path = os.path.join(src_dir, d)
    t_path = os.path.join(target_dir, d)
    if os.path.exists(s_path):
        print(f"Sao chép thư mục: {d}...")
        
        # Với resourcepacks, lọc bỏ các file .bak
        if d == "resourcepacks":
            os.makedirs(t_path, exist_ok=True)
            for f in os.listdir(s_path):
                if f in excluded_filenames or any(f.endswith(ext) for ext in excluded_extensions):
                    print(f"  [BỎ QUA FILE RÁC]: {f}")
                    continue
                f_src = os.path.join(s_path, f)
                f_dst = os.path.join(t_path, f)
                if os.path.isfile(f_src):
                    shutil.copy2(f_src, f_dst)
                elif os.path.isdir(f_src):
                    shutil.copytree(f_src, f_dst, dirs_exist_ok=True)
        else:
            shutil.copytree(s_path, t_path, dirs_exist_ok=True, ignore=shutil.ignore_patterns('*.bak', '*.tmp', '*.log'))

# 2. Các file cấu hình gốc quan trọng
essential_files = [
    "options.txt",
    "minecraftinstance.json",
    "TrashSlotSaveState.json"
]

for f in essential_files:
    s_f = os.path.join(src_dir, f)
    t_f = os.path.join(target_dir, f)
    if os.path.exists(s_f):
        shutil.copy2(s_f, t_f)
        print(f"Sao chép file cấu hình: {f}")

# 3. Tạo file hướng dẫn cực kỳ ngắn gọn, dễ hiểu đặt ngay ở gốc
guide_text = """======================================================================
     IMMERSIVE FIGHT 4.2.9 - BẢN VIỆT HÓA 100% (CHUẨN 1 CHẠM)
     Tác giả modpack: Latxx (辣某人) | Bản quyền Việt Hóa: Tawa System
======================================================================

HƯỚNG DẪN CÀI ĐẶT CỰC NHANH TRONG 10 GIÂY:
----------------------------------------------------------------------
1. Mở Launcher Minecraft bạn đang dùng (TLauncher, Prism, CurseForge, Modrinth, v.v...).
2. Tạo hoặc mở một phiên bản Forge 1.20.1 (Khuyến nghị Forge 47.3.0 trở lên).
3. Mở thư mục của phiên bản Forge 1.20.1 đó (nơi có các thư mục .minecraft / mods).
4. Sao chép TOÀN BỘ các file và thư mục trong thư mục này:
   - config/
   - ftbquests/
   - global_packs/
   - hotai/
   - minemenu/
   - mods/
   - resourcepacks/
   - resources/
   - shaderpacks/
   - options.txt
   - ...
5. DÁN ĐÈ TRỰC TIẾP vào thư mục Forge 1.20.1 đó.
6. Bấm "Vào game" (Launch) và tận hưởng 100% Tiếng Việt chuẩn Souls-like!

LƯU Ý:
- Toàn bộ ngôn ngữ (Tiếng Việt), thứ tự gói tài nguyên và nhiệm vụ đã được cấu hình sẵn.
- Tên vũ khí/vật phẩm giữ chuẩn Tiếng Anh để tìm kiếm JEI mượt mà không lỗi.
- Toàn bộ mô tả, chiêu thức, chỉ số, nhiệm vụ và sách hướng dẫn dịch 100% Tiếng Việt.
======================================================================
"""

with open(os.path.join(target_dir, "HUONG_DAN_CAI_DAT_1_CHAM.txt"), "w", encoding="utf-8") as fp:
    fp.write(guide_text)

print("\nĐã tạo thành công file HUONG_DAN_CAI_DAT_1_CHAM.txt!")

# 4. Thống kê dung lượng và số lượng file
total_files = 0
total_size = 0
for root, dirs, files in os.walk(target_dir):
    for f in files:
        total_files += 1
        total_size += os.path.getsize(os.path.join(root, f))

print(f"\n=== HOÀN TẤT DỰNG THƯ MỤC CÀI ĐẶT NHANH ===")
print(f"Vị trí: {target_dir}")
print(f"Tổng số file: {total_files}")
print(f"Tổng dung lượng: {total_size / (1024 * 1024):.2f} MB")
