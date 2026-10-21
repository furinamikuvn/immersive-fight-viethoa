# ⚔️ IMMERSIVE FIGHT (沉浸战斗) v4.2.9 — BẢN VIỆT HÓA

[![Minecraft 1.20.1](https://img.shields.io/badge/Minecraft-1.20.1-brightgreen.svg?style=for-the-badge&logo=minecraft)](https://www.minecraft.net/)
[![Forge](https://img.shields.io/badge/Forge-47.3.0%2B-orange.svg?style=for-the-badge)](https://files.minecraftforge.net/)
[![Release](https://img.shields.io/badge/Release-v4.2.9-purple.svg?style=for-the-badge)](https://github.com/furinamikuvn/immersive-fight-viethoa/releases)

Dự án bản địa hóa toàn diện modpack **Immersive Fight (沉浸战斗) v4.2.9** dành cho Minecraft Java Edition (Forge 1.20.1).

---

## 🌟 Điểm Nhấn Cốt Lõi (Core Highlights)

- 🗡️ **Quy Chuẩn Thuật Ngữ Song Ngữ Chuẩn Mực:**
  - **Tên Vũ khí, Cổ vật, Vật phẩm, Khối:** Giữ nguyên danh xưng gốc tiếng Anh (*Stormbringer, Sunfire, Agony, Ruine, Diamond Sword...*) để tìm kiếm mượt mà trong JEI, tra cứu công thức chế tạo không bị lỗi font hay đứt gãy từ khóa.
  - **Tên Rồng, Boss, Quái vật, Thực thể:** Giữ chuẩn tiếng Anh (*Raevyx, Ignivorus, Dwemer Centurion, Void Blossom, Night Lich...*) giúp tra cứu Wiki chuẩn xác phong cách Dark Souls.
  - **Mô tả, Kỹ năng, Tuyệt kỹ, Tooltip, Lore:** Dịch thuật thuần Việt sắc sảo, trau chuốt theo phong cách Dark Fantasy hào hùng (*Lực xung kích, Xuyên giáp, Thể lực, Kháng choáng, Thiên Giáng Đột Kích, Anh Hoa Kiếm Trảm...*).
- 📜 **23 Chương Nhiệm Vụ FTB Quests:** Sổ nhiệm vụ, hướng dẫn từng bước phát triển nhân vật được dịch sang Tiếng Việt.
- 📖 **Sách Hướng Dẫn In-Game (Patchouli):** Sách hướng dẫn của các mod lớn như *Simply Swords*, *Epic Fight*, v.v. được chuyển ngữ.
- 🔧 **Việt Hóa Nhúng Trực Tiếp (Direct Embed):** Bản dịch được deploy thẳng vào `resources/assets/` — Forge tự động load, **không cần bật Resource Pack thủ công**, không thể bị tắt nhầm.

---

## 📥 Tải Về (Download Links)

Truy cập tab **[Releases](https://github.com/furinamikuvn/immersive-fight-viethoa/releases/latest)** để tải thành phẩm:

| Gói Tải | Dung Lượng | Mô Tả & Đối Tượng Sử Dụng |
| :--- | :---: | :--- |
| 📦 **[Bản Cài Đặt Full Modpack](https://github.com/furinamikuvn/immersive-fight-viethoa/releases/latest)** | **~1.27 GB** | **Khuyến nghị:** Dành cho người mới. Bao gồm đầy đủ 310+ mod, cấu hình tối ưu sẵn tiếng Việt. Việt hóa nhúng trực tiếp — **không cần bật Resource Pack!** Chỉ cần giải nén dán đè là vào game chơi ngay. |

---

## 🚀 Hướng Dẫn Cài Đặt (1 Chạm — Dành Cho Mọi Người)

1. Tải tệp `Immersive Fight 4.2.9 - Viet Hoa (Forge 1.20.1).zip` từ mục **[Releases](https://github.com/furinamikuvn/immersive-fight-viethoa/releases/latest)**.
2. Mở Launcher Minecraft bạn đang sử dụng (*Prism Launcher, CurseForge, TLauncher, Modrinth App...*).
3. Tạo một profile hoặc phiên bản **Forge 1.20.1** (khuyến nghị phiên bản Forge `47.3.0` trở lên).
4. Mở thư mục chứa game của phiên bản vừa tạo.
5. Giải nén và **dán đè toàn bộ** các thư mục/tệp trong file zip (*config, ftbquests, global_packs, hotai, minemenu, mods, resources, shaderpacks, options.txt...*) vào thư mục game.
6. Bấm **Vào game (Play)** và tận hưởng thế giới Souls-like Việt hóa!

> ✅ **Không cần** vào Options → Resource Packs để bật gì thêm. Bản dịch đã hoạt động ngay lập tức.

---

## ⚙️ Thứ Tự Resource Pack Khuyến Nghị

Bản dịch ngôn ngữ đã được nhúng trực tiếp và **không yêu cầu** resource pack ngôn ngữ. Tuy nhiên để đảm bảo hiệu ứng vệt chém kiếm quang và hoạt ảnh chiến đấu chuẩn, sắp xếp các gói còn lại như sau:

```
1. Better-Leaves-9.3 (Lá cây rậm rạp - Tùy chọn)
2. IMF-Trail (Vệt chém kiếm quang)
3. IMF-Modify (Cấu hình sửa đổi chiến đấu)
4. BDHill Reforge the Sword Edge 沉浸特供
5. Reimagined (Gói giao diện/texture chính)
6. Fragmentum Layer (Dưới tầng này là tài nguyên nội bộ của các Mod)
```

> ⚠️ **LƯU Ý:** Khi thay đổi gói tài nguyên hoặc bấm `F3 + T` (nạp lại tài nguyên), hoạt ảnh chiến đấu có thể bị lệch. Bạn nên khởi động lại game để modpack nạp chuẩn xác nhất.

---

## 📂 Cấu Trúc Mã Nguồn (Repository Layout)

```
├── Immersive Fight 4.2.9 Viet Hoa/   # Thư mục mã nguồn và tài nguyên Việt Hóa chính
│   ├── config/                        # File cấu hình mod đã tối ưu
│   ├── ftbquests/                     # 23 chương nhiệm vụ FTB Quests tiếng Việt
│   ├── global_packs/                  # Datapacks kỹ năng & tiến trình
│   ├── hotai/                         # Dữ liệu thuộc tính tùy biến
│   ├── minemenu/                      # Cấu hình phím tắt nhanh
│   ├── resources/assets/              # ★ Bản dịch nhúng trực tiếp (230 namespace, 37.288 keys)
│   ├── resourcepack/IMF-VietHoa/      # Mã nguồn Resource Pack (tham khảo / legacy)
│   ├── resources/                     # Tài nguyên đồ họa & âm thanh bổ trợ
│   └── shaderpacks/                   # Gói shader khuyên dùng
├── tools/                             # Bộ công cụ build, patch, đóng gói tự động
│   └── deploy_direct_viethoa.py       # ★ Script deploy bản dịch trực tiếp
├── TRANSLATION_SPECS.md               # Quy chuẩn và tài liệu kỹ thuật dịch thuật chi tiết
└── README.md                          # Hướng dẫn sử dụng & cài đặt
```

---

## 👥 Tác Quyền & Lời Cảm Ơn

- **Tác giả Modpack gốc:** [Latxx (辣某人)](https://bbsmc.net/modpack/immersive-fight/versions) — Người tạo modpack *Immersive Fight*. Cảm ơn vì đã cho phép tôi đăng tải Modpack công khai. Đây là đường dẫn tới Modpack chính thức do tác giả đăng [Immersive Fight](https://bbsmc.net/modpack/immersive-fight/versions)
- **Người thực hiện việt hóa:** Nukumizu
