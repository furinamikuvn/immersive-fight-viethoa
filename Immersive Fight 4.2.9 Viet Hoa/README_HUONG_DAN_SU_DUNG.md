# 🎮 HƯỚNG DẪN BẢN VIỆT HÓA TOÀN DIỆN: IMMERSIVE FIGHT 4.2.9
*Tawa System Archives - Prepared for Master*

---

## 📌 1. TỔNG QUAN HỆ THỐNG
Dự án Việt hóa toàn diện đã hoàn tất với **37.035 translation keys** phủ khắp **230 mod namespaces** và **23 chương nhiệm vụ FTB Quests**. Không còn bất kỳ ký tự tiếng Trung nào còn sót lại trên giao diện, mô tả vũ khí, chỉ số hay nhiệm vụ!

Dự án cung cấp 2 giải pháp song hành:
1. **Trọn gói Modpack Việt Hóa sẵn (`Immersive Fight 4.2.9 Viet Hoa`)**: Dành cho người tải mới, vào game là chơi ngay 100% Tiếng Việt mà không cần chỉnh thêm bất kỳ cài đặt nào.
2. **Gói Resource Pack Độc Lập (`dist/IMF-VietHoa.zip`)**: Dành cho người chơi đã có sẵn modpack gốc bản Trung Quốc, chỉ cần nạp gói tài nguyên là chuyển ngữ sạch sẽ.

---

## 📐 2. BẢO TỒN NGUYÊN TẮC QUY CHUẨN (THE BLUEPRINT)
* **100% Tên Vũ khí, Vật phẩm, Khối, Cổ vật bằng Tiếng Anh (`en_us`)**: Giữ nguyên tên gốc (như *Stormbringer, Sunfire, Agony, Ruine, Diamond Sword...*) để tìm kiếm mượt mà trong JEI, không bị lỗi công thức chế tạo.
* **100% Tên Rồng, Boss, Quái vật bằng Tiếng Anh (`en_us`)**: Giữ nguyên các thực thể huyền thoại (*Raevyx, Ignivorus, Dwemer Centurion, Void Blossom, Night Lich...*) giúp dễ tra cứu wiki.
* **100% Chỉ số, Thuộc tính, Hiệu ứng, Tooltip, Lore bằng Tiếng Việt**: Chuẩn phong cách Dark Fantasy / Souls-like (*Lực xung kích, Xuyên giáp, Thể lực, Kháng choáng, Kháng kết liễu, Thiên Giáng Đột Kích, Anh Hoa Kiếm Trảm...*).
* **Cơ chế Triple-Fallback độc quyền của Tawa**: Trong gói Resource Pack, bản dịch được ánh xạ đồng bộ vào cả 3 tệp `vi_vn.json`, `zh_cn.json` và `en_us.json`. Bất kể người chơi để ngôn ngữ game là Tiếng Việt, Tiếng Anh hay Tiếng Trung mặc định, toàn bộ chữ tiếng Trung đều bị triệt tiêu 100%!
* **Zero-Crash**: Bảo toàn nguyên vẹn 100% các biến định dạng `%s`, `%d`, `{0}`, mã màu Minecraft `§` và FTB Quests `&`.

---

## 🚀 3. HƯỚNG DẪN SỬ DỤNG CHO TỪNG ĐỐI TƯỢNG

### CÁCH 1: DÀNH CHO NGƯỜI TẢI MỚI (CHƠI NGAY - ZERO CONFIG)
Master chỉ cần nén hoặc chia sẻ nguyên vẹn thư mục:
`D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa`
* Người chơi trỏ Launcher (TLauncher, Prism, CurseForge, Modrinth, v.v...) vào thư mục này.
* Khởi động game bằng **Forge 1.20.1** (phiên bản `47.3.0` trở lên).
* **Vào game là chiến ngay:** Game đã được cấu hình sẵn Tiếng Việt (`lang:vi_vn`), gói tài nguyên `IMF-VietHoa.zip` đã được kích hoạt mặc định, toàn bộ 23 chương nhiệm vụ FTB Quests đã được Việt hóa sẵn trong thế giới!

### CÁCH 2: DÀNH CHO NGƯỜI ĐANG DÙNG MODPACK TRUNG QUỐC GỐC
Người chơi chỉ cần lấy thành phẩm tại thư mục:
`D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\dist\`

1. **Bước 1 (Giao diện & Mô tả trang bị):**
   * Sao chép file `dist/IMF-VietHoa.zip`.
   * Dán vào thư mục `resourcepacks/` trong modpack gốc của họ.
   * Vào game -> **Tùy chọn (Options)** -> **Gói tài nguyên (Resource Packs)** -> Kéo `IMF-VietHoa.zip` lên vị trí trên cùng.
2. **Bước 2 (Nhiệm vụ & Cốt truyện FTB Quests):**
   * Sao chép toàn bộ 23 file `.snbt` trong thư mục `dist/quests/chapters/`.
   * Dán đè vào thư mục `config/ftbquests/quests/chapters/` của modpack gốc.
   * Mở sổ nhiệm vụ và thưởng thức trọn vẹn!

---

*Bản quyền kiến trúc & tự động hóa: Tawa System (The Peak Entity)*
