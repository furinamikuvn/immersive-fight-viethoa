#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_deep_descriptions_viethoa.py
===================================
Chuyên trách dịch toàn bộ các mô tả vật phẩm, vũ khí, kỹ năng, bùa chú,
hiệu ứng chiến đấu, tooltip và thông báo hệ thống còn sót sang Tiếng Việt.
Tuân thủ nghiêm ngặt:
  - Tên vật phẩm / vũ khí / thực thể / khối: 100% TIẾNG ANH.
  - Toàn bộ mô tả, thuộc tính, kỹ năng: 100% TIẾNG VIỆT chuẩn phong cách Dark Fantasy / Souls-like.
  - Đồng bộ cả 3 file: vi_vn.json, zh_cn.json, en_us.json vào 3 thư mục:
      1. Source: D:\\minecraft mod trung\\Immersive Fight 4.2.9 Viet Hoa\\resourcepack\\IMF-VietHoa\\assets
      2. Modpack: D:\\minecraft mod trung\\Immersive Fight 4.2.9\\resources\\assets
      3. Game: C:\\Users\\ADMIN\\AppData\\Roaming\\.tlauncher\\legacy\\Minecraft\\game\\home\\Forge 1.20.1\\resources\\assets
"""

import sys, json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(r"D:\minecraft mod trung")
TARGET_DIRS = [
    ROOT_DIR / "Immersive Fight 4.2.9 Viet Hoa" / "resourcepack" / "IMF-VietHoa" / "assets",
    ROOT_DIR / "Immersive Fight 4.2.9" / "resources" / "assets",
    Path(r"C:\Users\ADMIN\AppData\Roaming\.tlauncher\legacy\Minecraft\game\home\Forge 1.20.1\resources\assets")
]

DEEP_TRANSLATIONS = {
    # ─── CELESTISYNTH ──────────────────────────────────────────────────────────
    # Breezebreaker
    "item.celestisynth.breezebreaker.skill_1": "Ngọn Gió Ôn Hòa",
    "item.celestisynth.breezebreaker.skill_2": "Song Cuồng Phong Bão Tố",
    "item.celestisynth.breezebreaker.skill_3": "Toàn Lực Cuồng Phong Trảm",
    "item.celestisynth.breezebreaker.skill_4": "Tiếng Gầm Của Gió",
    "item.celestisynth.breezebreaker.skill_5": "Vòng Quay Tử Vong Phong Thần",
    "item.celestisynth.breezebreaker.passive_1": "Ngọn Gió Chở Che",
    "item.celestisynth.breezebreaker.passive_2": "Linh Hồn Nhân Từ",
    "item.celestisynth.breezebreaker.condition_1": "Kích hoạt: Nhấp chuột phải",
    "item.celestisynth.breezebreaker.condition_2": "Kích hoạt: Nhấn giữ chuột phải từ 0.5 giây trở lên",
    "item.celestisynth.breezebreaker.condition_3": "Kích hoạt: Nhấp chuột phải khi đang chạy",
    "item.celestisynth.breezebreaker.condition_4": "Kích hoạt: Chuột phải khi đang chạy nước rút",
    "item.celestisynth.breezebreaker.condition_5": "Kích hoạt: Chuột phải khi đang ở trên không",
    
    # Solaris
    "item.celestisynth.solaris.skill_1": "Hỏa Luân Xoay Tròn - Toàn Vòng",
    "item.celestisynth.solaris.skill_2": "Hỏa Luân Xoay Tròn - Đột Kích Thẳng Hồn",
    "item.celestisynth.solaris.passive_1": "Phúc Lành Tàn Lửa",
    "item.celestisynth.solaris.passive_2": "Trận Pháp Bom Mặt Trời",
    "item.celestisynth.solaris.condition_1": "Kích hoạt: Nhấp chuột phải",
    "item.celestisynth.solaris.condition_2": "Kích hoạt: Nhấn giữ chuột phải",

    # Aquaflora
    "item.celestisynth.aquaflora.skill_1": "Cánh Hoa Xuyên Thấu",
    "item.celestisynth.aquaflora.skill_2": "Đồng Loạt Nổ Tung",
    "item.celestisynth.aquaflora.skill_3": "Cuồng Loạn Trảm Kích Vô Biên",
    "item.celestisynth.aquaflora.skill_4": "Vạn Hoa Tiêu Tán",
    "item.celestisynth.aquaflora.passive_1": "Hương Hoa Nở Rộ",
    "item.celestisynth.aquaflora.condition_1": "Kích hoạt: Nhấp chuột phải",
    "item.celestisynth.aquaflora.condition_2": "Kích hoạt: Nhấn giữ chuột phải",
    "item.celestisynth.aquaflora.condition_3": "Kích hoạt: Chuột phải trong Trạng Thái Hoa Nở",
    "item.celestisynth.aquaflora.skill_3.notice": "Không thể định vị thực thể ở gần.",

    # Frostbound
    "item.celestisynth.frostbound.skill_1": "Vũ Điệu Thất Thiên Băng Tuyết",
    "item.celestisynth.frostbound.skill_2": "Băng Họa Giáng Trần",
    "item.celestisynth.frostbound.passive_1": "Hơi Lạnh Thì Thầm",
    "item.celestisynth.frostbound.passive_2": "Thập Lục Băng Xà Cận Trận",
    "item.celestisynth.frostbound.condition_1": "Kích hoạt: Nhấp chuột phải",
    "item.celestisynth.frostbound.condition_2": "Kích hoạt: Nhấn giữ chuột phải",

    # Poltergeist
    "item.celestisynth.poltergeist.skill_1": "Vũ Trụ Thần Cương Hủy Diệt",
    "item.celestisynth.poltergeist.skill_2": "Hiệu Triệu Kết Giới",
    "item.celestisynth.poltergeist.passive_1": "Dấu Ấn U Hồn",
    "item.celestisynth.poltergeist.condition_1": "Kích hoạt: Nhấp chuột phải",

    # Crescentia
    "item.celestisynth.crescentia.skill_1": "Oanh Tạc Lễ Hội Ánh Trăng",
    "item.celestisynth.crescentia.skill_2": "Long Mục (Eye of the Dragon)",
    "item.celestisynth.crescentia.passive_1": "Trọng Kích Đập Tan",
    "item.celestisynth.crescentia.condition_1": "Kích hoạt: Nhấp chuột phải",

    # Keres
    "item.celestisynth.keres.skill_1": "Huyết Sắc Nghiêm Trị",
    "item.celestisynth.keres.skill_2": "Nỗi Bi Ai Kinh Hoàng",
    "item.celestisynth.keres.skill_3": "Phán Quyết Đoạt Hồn Kẻ Trừng Phạt",
    "item.celestisynth.keres.passive_1": "Liên Hoàn Diệt Ngục",
    "item.celestisynth.keres.passive_2": "Huyết Tế (Blood Sacrifice)",
    "item.celestisynth.keres.passive_3": "Thống Khổ Trừ Tà Huyết Nguyền",
    "item.celestisynth.keres.condition_1": "Kích hoạt: Nhấp chuột phải",
    "item.celestisynth.keres.condition_3": "Nhấn giữ chuột phải từ 10 giây trở lên",
    "item.celestisynth.keres.notice": "Không thể hiến tế máu. Yêu cầu phải có hiệu ứng Hồi Máu (Regeneration).",

    # Rainfall Serenity
    "item.celestisynth.rainfall_serenity.skill_1": "Vạn Cổ Vượt Không Gian",
    "item.celestisynth.rainfall_serenity.skill_2": "Mưa Sao Chuẩn Tinh (Quasar Rainfall)",
    "item.celestisynth.rainfall_serenity.skill_3": "Chân Thực Tĩnh Lặng",
    "item.celestisynth.rainfall_serenity.condition_1": "Kích hoạt: Giương cung kéo căng tối đa",
    "item.celestisynth.rainfall_serenity.condition_2": "Kích hoạt: Đánh trúng thực thể bằng vũ khí",
    "item.celestisynth.rainfall_serenity.condition_4": "Kích hoạt: Thả vật phẩm trên mặt phẳng vững chắc",

    # Celestisynth UI notices
    "item.celestisynth.scroll_notice": "[Cuộn chuột để xem danh sách kỹ năng]",
    "item.celestisynth.shift_notice": "[Nhấn Shift hoặc Ctrl để chuyển trang]",

    # ─── MOWZIE'S MOBS ─────────────────────────────────────────────────────────
    "item.mowziesmobs.spear.text.0": "Tăng tầm đánh thêm 1.5 ô",
    "item.mowziesmobs.spear.text.1": "1/3 tỉ lệ hạ gục tức thì sinh vật có máu dưới 30",
    "item.mowziesmobs.blowgun.text.0": "Nạp nhanh",
    "item.mowziesmobs.blowgun.text.1": "Tầm bắn ngắn",
    "item.mowziesmobs.blowgun.text.2": "Chỉ bắn được phi tiêu ống xì",
    "item.mowziesmobs.dart.text.0": "Chỉ có thể dùng với ống xì",
    "item.mowziesmobs.dart.text.1": "Gây trúng độc mục tiêu",
    "item.mowziesmobs.wrought_axe.text.0": "Không bao giờ bị vỡ",
    "item.mowziesmobs.wrought_axe.text.1": "Nhấp chuột phải để chém xoay một vòng cung lớn",
    "item.mowziesmobs.wrought_axe.text.2": "Ngồi xổm + Chuột phải để nện mạnh xuống đất tạo sóng xung kích",
    "item.mowziesmobs.wrought_helmet.text.0": "Không bao giờ bị vỡ",
    "item.mowziesmobs.sol_visage.text.0": "Không bao giờ bị vỡ",
    "item.mowziesmobs.sol_visage.text.1": "Trang bị, sau đó nhấp chuột phải khi cầm mặt nạ khác để triệu hồi tiểu quỷ hầu cận",
    "item.mowziesmobs.sol_visage.text.2": "Nhấp chuột phải vào hầu cận để thu hồi nó về lại mặt nạ",
    "item.mowziesmobs.naga_fang_dagger.text.0": "Gây trúng độc mục tiêu",
    "item.mowziesmobs.naga_fang_dagger.text.1": "Gây gấp đôi sát thương khi đâm sau lưng",
    "item.mowziesmobs.ice_crystal.text.0": "Nhấn giữ chuột phải để niệm một cơn lốc băng giá",
    "item.mowziesmobs.ice_crystal.text.1": "Tự động hồi năng lượng khi ở trong túi đồ",
    "item.mowziesmobs.foliaath_seed.text.0": "Trồng trên cỏ",
    "item.mowziesmobs.foliaath_seed.text.1": "Cứ mỗi nửa ngày, Foliaath con sẽ bị đói",
    "item.mowziesmobs.foliaath_seed.text.2": "Ném thịt bất kỳ để cho nó ăn",
    "item.mowziesmobs.foliaath_seed.text.3": "Sau 2 ngày, Foliaath sẽ trưởng thành hoàn toàn",
    "item.mowziesmobs.glowing_jelly.text.0": "Ăn để nhận hiệu ứng Nhìn Trong Bóng Tối trong chốc lát",
    "item.mowziesmobs.naga_fang.text.0": "Dùng để pha chế Thuốc Kháng Độc Tố, chế tạo Dao Găm Nanh Naga, hoặc chế tạo phi tiêu",
    "item.mowziesmobs.sand_rake.text.0": "Dùng trên cát để cào họa tiết hoa văn cát\nSửa chữa bằng các tấm ván gỗ",
    "item.mowziesmobs.mob_remover.text.0": "Nhấp chuột trái để xóa bỏ sinh vật của Mowzie's Mobs",
    "item.mowziesmobs.bluff_rod.text.0": "Dùng để sửa chữa trang bị Địa Thuật, hoặc đưa cho Điêu Khắc Gia (Sculptor) để bắt đầu thử thách",
    
    # Mowzie Geomancy
    "item.mowziesmobs.earthrend_gauntlet.text.0": "§lNhấc Tảng Đá§r§7\nNhấp chuột phải vào nền đất để nâng tảng đá lên\nĐấm vào tảng đá để bắn nó đi\nTụ lực chuột phải để nâng tảng đá to hơn",
    "item.mowziesmobs.earthrend_gauntlet.text.1": "§lĐộn Thổ§r§7\nNhấp chuột phải vào không khí để bắt đầu độn thổ chui qua lòng đất\nNhấn giữ chuột phải và nhìn theo hướng muốn đào\nThả chuột phải để trồi lên mặt đất và dừng độn thổ\n",
    "item.mowziesmobs.earthrend_gauntlet.text.2": "§lTrụ Đá Thăng Hoa§r§7\nNhấn giữ đồng thời Ngồi xổm và Nhảy để nâng mình lên bằng một cột trụ đất\nĐộ rộng của trụ đá sẽ tăng lên nếu mọc xuyên qua các tảng đá địa thuật",
    "item.mowziesmobs.earthrend_gauntlet.text.3": "Tự động hồi năng lượng khi ở trong túi đồ",
    "item.mowziesmobs.geomancer_robe.text.0": "Tỉ lệ tạo ra một tảng đá địa thuật gần bên khi bạn gây hoặc nhận sát thương",
    "item.mowziesmobs.geomancer_beads.text.0": "+3 sát thương khi đấm (bao gồm các đòn tấn công bằng Earthrend Gauntlet)",
    "item.mowziesmobs.geomancer_belt.text.0": "+4 giáp và +1 kháng đẩy lùi khi bạn bị dính hiệu ứng Làm Chậm",
    "item.mowziesmobs.geomancer_sandals.text.0": "Tăng tốc độ di chuyển trong 3 giây sau khi rơi từ độ cao trên 4 ô",
    "item.mowziesmobs.sculptor_staff.text.0": "Triệu hồi 3 viên đá nhỏ tự động phóng đi sau một khoảng chờ ngắn",
    "entity.mowziesmobs.sculptor.trade.button.text": "Bắt Đầu Thử Thách",
    "entity.mowziesmobs.sculptor.boss_info.timer.text": "Thời Gian Còn Lại",

    # Mowzie Sun's Blessing
    "item.mowziesmobs.grant_suns_blessing.text.0": "Ban tặng Phúc Lành Mặt Trời trong",
    "item.mowziesmobs.grant_suns_blessing.text.2": "Đếm ngược chỉ bắt đầu sau khi bạn sử dụng một kỹ năng\n",
    "item.mowziesmobs.grant_suns_blessing.text.3": "§lThần Nhật Giáng Trần§r§7\nKhi tay không, nhấp chuột phải vào mặt đất để giáng đòn sấm sét mặt trời từ bầu trời xuống\n",
    "item.mowziesmobs.grant_suns_blessing.text.4": "§lLửa Mặt Trời (Solar Flare)§r§7\nKhi tay không, ngồi xổm + nhấp chuột trái để đánh bay đối thủ ra xa\n",
    "item.mowziesmobs.grant_suns_blessing.text.5": "§lTia Sáng Mặt Trời§r§7\nKhi tay không, ngồi xổm + nhấp chuột phải để bắn chùm tia sáng theo hướng nhìn (tiêu hao",
    "item.mowziesmobs.grant_suns_blessing.text.7": "§lVụ Nổ Siêu Tân Tinh (Supernova)§r§7\nKhi tay không, ngồi xổm và nhấn đồng thời chuột trái + phải để tạo một vụ nổ hủy diệt khổng lồ quanh bản thân (tiêu hao",
    "item.mowziesmobs.grant_suns_blessing.text.8": " toàn bộ phúc lành)",

    # Mowzie Masks
    "item.mowziesmobs.umvuthana_mask_fury.text.0": "Ban tặng hiệu ứng Sức Mạnh (Strength)",
    "item.mowziesmobs.umvuthana_mask_fury.text.1": "Liệu có phải là...?",
    "item.mowziesmobs.umvuthana_mask_fear.text.0": "Ban tặng hiệu ứng Tốc Độ (Swiftness)",
    "item.mowziesmobs.umvuthana_mask_fear.text.1": "Liệu có phải là...?",
    "item.mowziesmobs.umvuthana_mask_rage.text.0": "Ban tặng hiệu ứng Mau Lẹ (Haste)",
    "item.mowziesmobs.umvuthana_mask_rage.text.1": "Liệu có phải là...?",
    "item.mowziesmobs.umvuthana_mask_bliss.text.0": "Ban tặng hiệu ứng Nhảy Cao (Jump Boost)",
    "item.mowziesmobs.umvuthana_mask_bliss.text.1": "Liệu có phải là...?",
    "item.mowziesmobs.umvuthana_mask_misery.text.0": "Ban tặng hiệu ứng Kháng Cự (Resistance)",
    "item.mowziesmobs.umvuthana_mask_misery.text.1": "Liệu có phải là...?",
    "item.mowziesmobs.umvuthana_mask_faith.text.0": "Ban tặng hiệu ứng Tăng Máu Tối Đa (Health Boost)",
    "item.mowziesmobs.umvuthana_mask_faith.text.1": "Liệu có phải là...?",

    # ─── TOUHOU LITTLE MAID ────────────────────────────────────────────────────
    "item.touhou_little_maid.fire_protect_bauble.tip": "Tăng cho hầu gái khả năng kháng sát thương thiêu đốt.",
    "item.touhou_little_maid.fall_protect_bauble.tip": "Tăng cho hầu gái khả năng kháng sát thương rơi ngã.",
    "item.touhou_little_maid.explosion_protect_bauble.tip": "Tăng cho hầu gái khả năng kháng sát thương cháy nổ.",
    "item.touhou_little_maid.drown_protect_bauble.tip": "Tăng cho hầu gái khả năng kháng sát thương ngạt nước.",
    "item.touhou_little_maid.projectile_protect_bauble.tip": "Tăng cho hầu gái khả năng kháng sát thương vật phóng.",
    "item.touhou_little_maid.magic_protect_bauble.tip": "Tăng cho hầu gái khả năng kháng hiệu ứng phép thuật xấu.",
    "item.touhou_little_maid.mute_bauble.tip": "Khiến hầu gái giữ im lặng nếu bạn không thích cô ấy nói chuyện quá nhiều.",
    "item.touhou_little_maid.item_magnet_bauble.tip": "Mở rộng tầm nhặt vật phẩm của hầu gái.",
    "item.touhou_little_maid.nimble_fabric.tip": "Cho phép hầu gái né tránh đòn bắn tới bằng cách dịch chuyển tức thời.",
    "item.touhou_little_maid.crafting_table_backpack.tip": "Mở rộng túi đồ hầu gái lên 18 ô. Biến hầu gái thành một Bàn Chế Tạo di động.",
    "item.touhou_little_maid.furnace_backpack.tip": "Mở rộng túi đồ hầu gái lên 18 ô. Biến hầu gái thành một Lò Nung di động.",
    "item.touhou_little_maid.maid_backpack_small.tip": "Mở rộng túi đồ của hầu gái lên 12 ô.",
    "item.touhou_little_maid.maid_backpack_middle.tip": "Mở rộng túi đồ của hầu gái lên 24 ô.",
    "item.touhou_little_maid.maid_backpack_big.tip": "Mở rộng túi đồ của hầu gái lên 36 ô.",
    "item.touhou_little_maid.picnic_basket.tip": "Tối đa 4 hầu gái sẽ cùng dã ngoại khi rảnh rỗi. Hãy cho thức ăn vào giỏ để tăng độ thiện cảm.",
    "item.touhou_little_maid.film.tip": "Hầu gái đã tử trận. Để hồi sinh cô ấy, đặt cuộn phim này vào tế đàn cùng Thỏi Vàng, Thỏi Sắt, Ngọc Lưu Ly, Than và Đá Đỏ trên mỗi cột trụ, hoặc đặt vào Điện Thờ (Shrine).",
    "item.touhou_little_maid.hakurei_gohei.tip": "Gậy Gohei dùng kích hoạt tế đàn sau khi xây xong. Hầu gái cầm gậy có thể bắn đạn đan mạc (danmaku) tiêu diệt quái vật thù địch.",
    "item.touhou_little_maid.sanae_gohei.tip": "Gậy Gohei dùng kích hoạt tế đàn sau khi xây xong. Hầu gái cầm gậy có thể bắn đạn đan mạc (danmaku) tiêu diệt quái vật thù địch.",
    "item.touhou_little_maid.broom.tip": "Cần hầu gái cưỡi chổi để bay lượn trên bầu trời. Lưu ý một số quái vật bay như Tiên Hầu Gái hay Phantom vẫn có thể tấn công bạn.",
    "entity.touhou_little_maid.broom.tip": "Cần hầu gái cưỡi chổi để bay lượn trên bầu trời. Lưu ý một số quái vật bay như Tiên Hầu Gái hay Phantom vẫn có thể tấn công bạn.",
    "item.touhou_little_maid.wireless_io.tip": "Có thể cấu hình khoảng cách truyền tải vật phẩm từ rương tới hầu gái hoặc ngược lại.",
    "item.touhou_little_maid.power_point.tip": "Điểm Sức Mạnh (Power Point) thu thập từ chiến lợi phẩm, ném ra để hấp thụ.",
    "block.touhou_little_maid.keyboard.tip": "Đem lại niềm vui và tăng độ thiện cảm cho hầu gái của bạn.",
    "block.touhou_little_maid.computer.tip": "Đem lại niềm vui và tăng độ thiện cảm cho hầu gái của bạn.",
    "block.touhou_little_maid.bookshelf.tip": "Đem lại niềm vui và tăng độ thiện cảm cho hầu gái của bạn.",
    "block.touhou_little_maid.maid_bed.tip": "Hầu gái sẽ nghỉ ngơi trên chiếc giường này khi đến giờ ngủ. Giúp tăng độ thiện cảm.",
    "block.touhou_little_maid.gomoku.tip": "Thách đấu hầu gái trong bàn cờ caro (Gomoku). Liệu bạn có đủ trí tuệ để đánh bại cô ấy không?",
    "block.touhou_little_maid.snack_cabinet.tip": "Tủ chứa đồ ăn vặt. Hầu gái sẽ tự ăn thức ăn dạng khối đặt bên trên và cất thức ăn thừa từ túi đồ vào tủ.",
    "block.touhou_little_maid.shrine.tip": "Điện Thờ (Shrine) xuất hiện hiếm hoi trong rương chiến lợi phẩm. Dùng để hồi sinh hầu gái tử trận, nhưng sẽ rút máu của bạn về 1 giọt.",
    "block.touhou_little_maid.scarecrow.tip": "Khi đặt trên mặt đất, bù nhìn ngăn chặn các tiên hầu gái xuất hiện trong một phạm vi hình vuông.",
    "entity.touhou_little_maid.maid.tip": "Thuần phục hầu gái bằng bánh ngọt và phân công công việc tùy ý. Xem sách Memorizable Gensokyo để biết thêm chi tiết.",
    "entity.touhou_little_maid.fairy.tip": "Bay lượn và bắn đạn đan mạc vào bạn. Rơi ra điểm sức mạnh khi bị tiêu diệt.",
    "model.touhou_little_maid_old.konngara.desc": "§7Kỵ Sĩ Tinh Tú (Astral Knight)",
    "item.touhou_little_maid.favorability_tool_add": "Công Cụ Tăng Thiện Cảm",
    "item.touhou_little_maid.favorability_tool_reduce": "Công Cụ Giảm Thiện Cảm",
    "item.touhou_little_maid.favorability_tool_full": "Công Cụ Thiện Cảm Tối Đa",

    # ─── MAID SMART ────────────────────────────────────────────────────────────
    "task.maid_smart.broom.desc": "Cưỡi Chổi: Hầu gái lấy chổi TLM trong túi đồ, tự mình cưỡi chổi (không cần người lái) và bắn vũ khí tầm xa đang cầm; khi rảnh rỗi cô ấy bay lơ lửng đi theo chủ nhân, ở chế độ Nhà cô ấy sẽ bay tuần tra vòng quanh khu vực làm việc. Yêu cầu: chổi + vũ khí tầm xa + đạn dược (đối với súng đạn phải khớp súng đang cầm); nếu thiếu gì cô ấy sẽ đứng yên chờ và thông báo. Không kích hoạt qua tự động đổi nhiệm vụ. Khi cưỡi chổi cô ấy KHÔNG THỂ dùng ma thuật hay đặt TNT/pha lê end/mỏ neo/giường - chỉ tấn công bằng vũ khí cầm tay.",
    "task.maid_smart.flight_combat.desc": "Không Kích Cận Chiến: cánh cứng elytra + vũ khí cận chiến bất kỳ + pháo hoa; nhảy lượn, phóng pháo hoa vút lên, lao thẳng vào kẻ thù sau 1.5s, hủy bay lượn ở cự ly 3.5 khối để rơi tự do chém chí mạng, sau đó tái kích hoạt cánh lượn lặp lại chu kỳ.",
    "item.maid_smart.combat_leash.desc2": "§7Dùng lại hoặc ngồi xổm để buông ra; hầu gái sẽ thả bạn an toàn khi tiếp đất.",
    "item.maid_smart.ride_baton.desc2": "§7Thứ tự là §fcố định§7: bạn phải chọn §fthú cưỡi trước§7, sau đó mới chọn hầu gái. Đối tượng được chọn sẽ phát sáng ánh vàng.",
    "item.maid_smart.patrol_chart.desc3": "§fSau khi bắt đầu đánh dấu, nhấp chuột giữa§7 để ghi lại mốc (không cần ngồi xổm; hoạt động cả trên không và mặt đất — mốc nằm chính xác tại vị trí của bạn); các khối kim cương + vòng tròn trong thế giới là mốc tuần tra, mỗi mốc được gắn nhãn §7\"lộ trình #N\"§7 bên trên (điểm đầu §bxanh ngọc§7 / điểm cuối §dtím hồng§7); đường nối tự động nâng cao vượt chướng ngại vật.",
    "item.maid_smart.patrol_chart.desc4": "§7Chỉ áp dụng cho hầu gái chế độ cưỡi chổi + chế độ Nhà, dây buộc chổi sẽ không kéo cô ấy nữa; Chế tạo: giấy + la bàn + túi mực.",
    "config.promaid.build.noForceHome.tooltip": "Không ép chế độ Nhà khi Xây Dựng (mặc định bật): Trong khi xây dựng / đặt đá chỉ dấu, hầu gái sẽ không bị ép chuyển sang chế độ đồn trú (Nhà). Thay vào đó mod chặn mọi hành vi tự động dịch chuyển ngoài ý muốn của người chơi, giúp cô ấy bám sát công trình.",

    # ─── EEEAB'S MOBS ──────────────────────────────────────────────────────────
    "item.eeeabsmobs.smithing_template.ghost_warrior.ingredients": "Thỏi Thép U Linh (Ghost Steel Ingot)",
    "item.eeeabsmobs.heart_of_pagan.tip": "Dùng để pha chế thuốc cuồng loạn (Frenzy Potion)",
    "item.eeeabsmobs.guardian_core.tip": "Tầm tấn công: §l[ %1$s §l]",
    "block.eeeabsmobs.sliding_door_level2.tip": "Cánh cửa này yêu cầu Guardian Core hoặc Rìu Chiến Doombolt Battleaxe để mở",
    "item.armor.eeeabsmobs.full_suit_of_armor.tip": "Hiệu ứng khi mặc trọn bộ giáp:",
    "item.other.eeeabsmobs.cd.tip": "Hồi chiêu %1$s giây",
    "item.eeeabsmobs.immortal_sword.tip": "Áp đặt trạng thái Ăn Mòn (Erosion) lên kẻ tấn công",
    "item.eeeabsmobs.remove_mob.tip_1": "Nhấp chuột trái để xóa bỏ sinh vật của EEEAB's Mobs",
    "item.eeeabsmobs.remove_mob.tip_2": "Nhấp chuột phải để xóa bỏ sinh vật của EEEAB's Mobs trong khu vực 16x16x16",
    "item.other.eeeabsmobs.animation_controller.tip": "Đã chọn thực thể %1$s",
    "item.eeeabsmobs.smithing_template.relicron.ingredients": "Lõi Bánh Răng Xích hoặc Guardian Core",
    "item.other.eeeabsmobs.no_cd.tip": "Không Có Thời Gian Hồi Chiêu",
    "block.eeeabsmobs.sliding_door_level1.tip": "Cánh cửa này yêu cầu Lõi Bánh Răng Xích hoặc Lưỡi Cưa Annihilator để mở",
    "item.armor.eeeabsmobs.ghost_warrior_full_suit_of_armor.tip": "Chưa hoàn thiện",
    "item.structure.eeeabsmobs.eye_of_bloody_altar.tip": "Nhấp chuột phải để định vị cấu trúc Tế Đàn Đẫm Máu (Bloody Altar)",
    "item.structure.eeeabsmobs.eye_of_coreforge_ruins.tip": "Nhấp chuột phải để định vị cấu trúc Phế Tích Lò Rèn Lõi (Coreforge Ruins)",
    "item.hotkeys.eeeabsmobs.shift_down.tip": "Nhấn giữ <Shift> để xem chi tiết",
    "item.eeeabsmobs.buster_gauntlet.tip": "Nhấp chuột phải để phóng lựu đạn, gây tối đa %1$s sát thương nổ",
    "item.eeeabsmobs.smithing_template.netherite_upgrade.applies_to": "Trang Bị Netherite (Netherite Equipment)",
    "item.eeeabsmobs.guardian_axe.tip_1": "Sát thương quét: §l[ %1$s §l]",

    # ─── BETTEREND SMITHING & DETAILS ──────────────────────────────────────────
    "item.betterend.smithing_template.plate_upgrade.applies_to": "Giáp Terminite (Terminite Armor)",
    "item.betterend.smithing_template.aeternium_upgrade.applies_to": "Cánh Cứng Elytra hoặc Đe Terminite",
    "item.betterend.smithing_template.thallasium_upgrade.base_slot_description": "Đặt Gậy Gỗ",
    "item.betterend.smithing_template.leather_handle_attachment.ingredients": "Gậy Bọc Da (Leather Wrapped Sticks)",
    "item.betterend.smithing_template.terminite_upgrade.ingredients": "Thỏi Terminite (Terminite Ingots)",
    "item.betterend.smithing_template.netherite_upgrade.applies_to": "Búa Kim Cương (Diamond Hammer)",
    "item.betterend.smithing_template.thallasium_upgrade.ingredients": "Thỏi Thallasium (Thallasium Ingots)",
    "item.betterend.smithing_template.leather_handle_attachment.applies_to": "Đầu Công Cụ Aeternium",
    "item.betterend.smithing_template.aeternium_upgrade.ingredients": "Thỏi Aeternium (Aeternium Ingots)",
    "item.betterend.smithing_template.plate_upgrade.ingredients": "Tấm Rèn Aeternium",
    "item.betterend.smithing_template.tool_assembly.applies_to": "Lưỡi Kiếm (Sword Blades)",
    "item.betterend.smithing_template.terminite_upgrade.applies_to": "Gậy hoặc Đe Thallasium",
    "item.betterend.smithing_template.netherite_upgrade.ingredients": "Thỏi Netherite (Netherite Ingots)",
    "item.betterend.smithing_template.handle_attachment.additions_slot_description": "Đặt Gậy Gỗ",
    "item.betterend.smithing_template.handle_attachment.applies_to": "Đầu Công Cụ Thallasium hoặc Terminite",
    "item.betterend.smithing_template.tool_assembly.ingredients": "Chuôi Kiếm (Sword Handles)",

    # ─── TOO MANY BOWS ─────────────────────────────────────────────────────────
    "item.too_many_bows.shulker_blast_bow.effect1": "§7Đạn đuổi tự tìm mục tiêu",
    "item.too_many_bows.sentinels_wrath.hold_shift": "§8[Nhấn giữ §eShift§8] để xem chi tiết",
    "item.too_many_bows.hold_shift": "§8[Nhấn giữ §eShift§8] để xem chi tiết",
    "item.too_many_bows.shulker_blast_bow.hold_shift": "§8[Nhấn giữ §eShift§8] để xem chi tiết",
    "item.too_many_bows.hunter_bow.hold_shift": "§8[Nhấn giữ §eShift§8] để xem chi tiết",
    "item.too_many_bows.astral_bow.details": "Cây cung này bắn tên nảy bật (ricochet), phù phép với Nảy Bật để dội qua nhiều bề mặt hơn.",
    "item.too_many_bows.torchbearer_bow.shift": "Thiêu đốt kẻ thù và thắp sáng lối đi của bạn.",
    "item.many_bows.radiance.no_experience": "Cung này cần điểm kinh nghiệm (XP) để bắn!",
    "item.too_many_bows.shulker_blast_bow.shift_title": "§6Hiệu Ứng Đặc Biệt",
    "item.many_bows.ethereal_hunter.no_hunger": "Bạn quá đói để có thể giương cung bắn!",
    "item.too_many_bows.webstring_volley.details": "Bắn tỏa ra 5 mũi tên hình nón, gây hiệu ứng làm chậm lên mục tiêu.",
    "item.too_many_bows.hunter_bow.shift_title": "§6Khắc chế mạnh:",
    "item.many_bows.dusk_reaper.no_soul_fragments": "Bạn cần Mảnh Linh Hồn để bắn cây cung này!",
    "item.too_many_bows.sentinels_wrath.shift_title": "§6Khắc chế mạnh:",
    "item.too_many_bows.vitality_weaver.details": "Tên Hút Huyết: Mũi tên hút máu kẻ địch và hồi phục cho người bắn.",
    "item.many_bows.aurora_bow.item_use": "Bạn cần Mảnh Hư Không (Rift Shards) để sử dụng cung này!",
    "item.too_many_bows.spectral_whisper.details": "Cung này bắn tên quang phổ xuyên qua các khối, sát thương thực thể.",
    "item.many_bows.aurora_bow.no_rift_shard": "Bạn cần Mảnh Hư Không để bắn cung này!",

    # ─── SIMPLY SWORDS ─────────────────────────────────────────────────────────
    "item.simplyswords.magiblade.event2": "Tàn Tích Suy Tàn của bạn dường như bị hút về phía khối bên dưới bạn",
    "item.simplyswords.magicythe.event": "Tàn Tích Suy Tàn của bạn đã bắt đầu phát ra âm thanh kỳ lạ",
    "item.simplyswords.magicythe.event2": "Tàn Tích Suy Tàn của bạn dường như đang phản ứng với khu vực này",
    "item.simplyswords.magispear.event": "Tàn Tích Suy Tàn của bạn dường như vừa bị ảnh hưởng bởi thứ gì đó",
    "item.simplyswords.magispear.event2": "Tàn Tích Suy Tàn của bạn dường như đang phản ứng với bóng tối",
    "item.simplyswords.contained_remnant.event": "Một Mảnh Tàn Tích trong túi đồ của bạn dường như đã thay đổi hình dạng",
    "item.simplyswords.contained_remnant.event2": "Một Mảnh Tàn Tích trong túi đồ của bạn đang có biểu hiện kỳ lạ",
    "item.simplyswords.tampered_remnant_description4": "bởi một thế lực bí ẩn nào đó...",
    "item.simplyswords.awakening": "Cấp Thức Tỉnh: %d",
    "item.simplyswords.awakening.exp": "Kinh Nghiệm Thức Tỉnh: %d%%",
    "item.simplyswords.awakening.powers": "Năng Lực Đã Thức Tỉnh:",
    "item.simplyswords.empty_nether_slot": "[ Ô Khảm Nether Còn Trống ]",
    "item.simplyswords.empty_runic_slot": "[ Ô Khảm Cổ Tự Còn Trống ]",
    "item.simplyswords.filled_runic_slot": "[ Ngọc Cổ Tự Đã Khảm ]",
    "item.simplyswords.runefused_power": "Sức Mạnh Cổ Tự:",
    "item.simplyswords.greater_runic_power": "Đại Sức Mạnh Cổ Tự (Greater)",
    "item.simplyswords.onrightclick": "Khi Nhấp Chuột Phải:",
    "item.simplyswords.onrightclickheld": "Nhấn Giữ Chuột Phải:",
    "item.simplyswords.common.blacklisteffect": "KỸ NĂNG BỊ VÔ HIỆU HÓA",
    "item.simplyswords.compat.scaleHealing": "§7Sức mạnh kỹ năng tăng theo sát lực phép §aTrị Liệu (Healing)§7",
    "item.simplyswords.compat.scaleSoul": "§7Sức mạnh kỹ năng tăng theo sát lực phép §9Linh Hồn (Soul)§7",
    "item.simplyswords.compat.scaleLightning": "§7Sức mạnh kỹ năng tăng theo sát lực phép §eSét (Lightning)§7",
    "item.simplyswords.compat.scaleFire": "§7Sức mạnh kỹ năng tăng theo sát lực phép §6Lửa (Fire)§7",
    "item.simplyswords.compat.scaleArcane": "§7Sức mạnh kỹ năng tăng theo sát lực phép §dBí Thuật (Arcane)§7",
    "item.simplyswords.compat.scaleFrost": "§7Sức mạnh kỹ năng tăng theo sát lực phép §bBăng (Frost)§7",
    "item.simplyswords.uniquesworditem.netherfused_power.accelerant": "[ Cường Hóa Nether: Gia Tốc ]",
    "item.simplyswords.uniquesworditem.netherfused_power.echo": "[ Cường Hóa Nether: Vang Vọng ]",
    "item.simplyswords.uniquesworditem.netherfused_power.renewed": "[ Cường Hóa Nether: Tái Sinh ]",
    "item.simplyswords.uniquesworditem.netherfused_power.onslaught": "[ Cường Hóa Nether: Oanh Kích ]",
    "item.simplyswords.uniquesworditem.netherfused_power.leaping": "[ Cường Hóa Nether: Nhảy Bật ]",
    "item.simplyswords.uniquesworditem.netherfused_power.precise": "[ Cường Hóa Nether: Chuẩn Xác ]",
    "item.simplyswords.uniquesworditem.netherfused_power.stealthy": "[ Cường Hóa Nether: Ẩn Thân ]",
    "item.simplyswords.uniquesworditem.netherfused_power.spellstandard": "[ Cường Hóa Nether: Hiệu Kỳ Phép ]",
    "item.simplyswords.uniquesworditem.netherfused_power.warstandard": "[ Cường Hóa Nether: Chiến Kỳ ]",
    "item.simplyswords.uniquesworditem.netherfused_power.nullification": "[ Cường Hóa Nether: Hóa Giải ]",
    "item.simplyswords.uniquesworditem.netherfused_power.berserk": "[ Cường Hóa Nether: Cuồng Nộ ]",
    "item.simplyswords.uniquesworditem.netherfused_power.radiance": "[ Cường Hóa Nether: Hào Quang ]",
    "item.simplyswords.uniquesworditem.netherfused_power.soulshock": "[ Cường Hóa Nether: Xung Kích Hồn ]",
    "item.simplyswords.uniquesworditem.netherfused_power.spellforged": "[ Cường Hóa Nether: Ma Luyện ]",
    "item.simplyswords.uniquesworditem.netherfused_power.deception": "[ Cường Hóa Nether: Ảo Ảnh ]",
    "item.simplyswords.uniquesworditem.netherfused_power.mighty": "[ Cường Hóa Nether: Đại Lực ]",
    "item.simplyswords.uniquesworditem.runefused_power.active_defence": "[ Khảm Cổ Tự: Phòng Thủ Chủ Động ]",
    "item.simplyswords.uniquesworditem.runefused_power.shielding": "[ Khảm Cổ Tự: Hộ Thuẫn ]",
    "item.simplyswords.uniquesworditem.runefused_power.weaken": "[ Khảm Cổ Tự: Suy Yếu ]",
    "item.simplyswords.uniquesworditem.runefused_power.swiftness": "[ Khảm Cổ Tự: Tốc Biến ]",
    "item.simplyswords.uniquesworditem.runefused_power.trailblaze": "[ Khảm Cổ Tự: Khai Hỏa ]",
    "item.simplyswords.uniquesworditem.runefused_power.imbued": "[ Khảm Cổ Tự: Truyền Ma Lực ]",
    "item.simplyswords.uniquesworditem.runefused_power.stoneskin": "[ Khảm Cổ Tự: Da Đá (Stoneskin) ]",
    "item.simplyswords.uniquesworditem.runefused_power.slow": "[ Khảm Cổ Tự: Làm Chậm ]",
    "item.simplyswords.uniquesworditem.runefused_power.zephyr": "[ Khảm Cổ Tự: Phong Thần (Zephyr) ]",
    "item.simplyswords.uniquesworditem.runefused_power.pincushion": "[ Khảm Cổ Tự: Gai Nhọn ]",
    "item.simplyswords.uniquesworditem.runefused_power.freeze": "[ Khảm Cổ Tự: Đóng Băng ]",
    "item.simplyswords.uniquesworditem.runefused_power.float": "[ Khảm Cổ Tự: Trôi Lơ Lửng ]",
    "item.simplyswords.uniquesworditem.runefused_power.frost_ward": "[ Khảm Cổ Tự: Hộ Thể Băng ]",
    "item.simplyswords.uniquesworditem.runefused_power.wildfire": "[ Khảm Cổ Tự: Bão Lửa (Wildfire) ]",
    "item.simplyswords.uniquesworditem.runefused_power.unstable": "[ Khảm Cổ Tự: Bất Định ]",

    # ─── DUNGEONS AND COMBAT ───────────────────────────────────────────────────
    "effect.dungeons_and_combat.ammit_edge": "Lưỡi Đao Ammit",
    "effect.dungeons_and_combat.forgotten_entity": "Thực Thể Lãng Quên",
    "effect.dungeons_and_combat.toxic_edge": "Lưỡi Đao Độc Dược",
    "effect.dungeons_and_combat.acid_fire": "Hỏa Axít (Acid Fire)",
    "effect.dungeons_and_combat.poisoned_edge": "Lưỡi Đao Tẩm Độc",
    "effect.dungeons_and_combat.fatal_oath": "Lời Thề Tử Vong (Fatal Oath)",
    "effect.dungeons_and_combat.crimson_rage": "Cơn Thịnh Nộ Huyết Sắc (Crimson Rage)",
    "effect.dungeons_and_combat.ice_resistance": "Kháng Băng Giá",
    "effect.dungeons_and_combat.scarlet_restoration": "Hồi Phục Huyết Sắc",
    "effect.dungeons_and_combat.broken_armor": "Giáp Vỡ Nát I",
    "effect.dungeons_and_combat.ernos_necklace": "Dây Chuyền Ernos",
    "effect.dungeons_and_combat.hunter_fury": "Cơn Thịnh Nộ Thợ Săn",
    "effect.dungeons_and_combat.wither_edge": "Lưỡi Đao Khô Héo (Wither Edge)",
    "effect.dungeons_and_combat.bleeding_edge": "Lưỡi Đao Chảy Máu (Bleeding Edge)",
    "effect.dungeons_and_combat.burning_edge": "Lưỡi Đao Thiêu Đốt (Burning Edge)",
    "effect.dungeons_and_combat.deadly_aura": "Hào Quang Tử Thần (Deadly Aura)",
    "effect.dungeons_and_combat.life_stealer": "Đoạt Sinh Lực (Life Stealer)",
    "effect.dungeons_and_combat.burning_aura": "Hào Quang Thiêu Đốt",
    "effect.dungeons_and_combat.death_mark": "Dấu Ấn Tử Thần (Death Mark)",
    "attribute.dungeons_and_combat.action_state": "Trạng Thái Hành Động",
    "advancements.origin.descr": "Chọn một chức nghiệp (Class) khởi đầu",
    "advancements.dark_purposes.descr": "Thu thập Chén Thánh Hắc Ám",
    "gui.dungeons_and_combat.titan_class_gui.label_negative_combat_effects": "Hiệu Ứng Bất Lợi Khi Chiến Đấu",
    "gui.dungeons_and_combat.oni_slayer_class_gui.label_the_effect_ends": "khi hiệu ứng kết thúc",
    "gui.dungeons_and_combat.oni_slayer_class_gui.label_deal_damage_when_the_effect_ends": "gây sát thương khi hiệu ứng kết thúc",

    # ─── AQUAMIRAE ─────────────────────────────────────────────────────────────
    "item.aquamirae.abyssal_upgrade_smithing_template.applies_to": "Giáp Kim Cương (Diamond Armor)",
    "item.aquamirae.abyssal_upgrade_smithing_template.ingredients": "Thạch Anh Biển Sâu (Abyssal Amethyst)",
    "item.aquamirae.terrible_upgrade_smithing_template.applies_to": "Giáp Sắt (Iron Armor)",

    # ─── ALEX'S CAVES ──────────────────────────────────────────────────────────
    "item.alexscaves.cloak_of_darkness.requires_darkness": "Bạn không thể sử dụng kỹ năng này dưới ánh sáng...",
    "item.alexscaves.cloak_of_darkness.equip": "Sử dụng Kỹ Năng Đặc Biệt khi được cường hóa để hóa thân thành Hiện Thân Bóng Đêm",
    "item.alexscaves.totem_of_possession.invalid": "Sinh vật này quá mạnh mẽ, không thể bị chiếm đoạt linh hồn...",
    "item.alexscaves.occult_gem.start_observing": "Ngồi xổm để dừng quan sát...",
    "item.alexscaves.cave_map.error": "Dường như không có quần xã sinh vật này trong bán kính %s khối. Hãy thử chu du xa hơn.",
    "item.alexscaves.cave_codex.end": "Không còn điều gì để khám phá thêm về quần xã sinh vật này.",
    "item.alexscaves.cave_codex.add": "Đã thêm %s: %s vào Sách Bách Khoa Hang Động",
    "item.alexscaves.cave_codex.add_all": "Đã thêm %s vào Sách Bách Khoa Hang Động",
    "entity.alexscaves.subterranodon.mount_message": "%s để Bay Lên, %s để Hạ Xuống, %s để Xuống Cưỡi",
    "entity.alexscaves.deep_one.reaction_helpful": "Những Kẻ Dưới Biển Sâu (Deep Ones) giờ đây xem bạn là bằng hữu",
    "entity.alexscaves.luxtructosaurus.slain_message": "Những hình thái mới đang dần thành hình bên trong Cự Thạch Hổ Phách...",
    "entity.alexscaves.deep_one.reaction_aggressive": "Những Kẻ Dưới Biển Sâu (Deep Ones) giờ đây nhìn bạn đầy căm thù hung hãn",
    "entity.alexscaves.submarine.mount_message": "%s: Trồi Lên, %s: Lặn Xuống, %s: Đèn Pha, %s: Rời Tàu",
    "entity.alexscaves.deep_one.reaction_neutral": "Những Kẻ Dưới Biển Sâu (Deep Ones) giờ đây giữ thái độ trung lập với bạn",
    "entity.alexscaves.tremorsaurus.mount_message": "%s để Gầm Lớn, %s để Xuống Cưỡi",
    "entity.alexscaves.deep_one.reaction_stalking": "Những Kẻ Dưới Biển Sâu (Deep Ones) giờ đây nhìn bạn với sự cảnh giác cao độ",

    # ─── CATACLYSM ─────────────────────────────────────────────────────────────
    "entity.cataclysm.the_leviathan.defeat_message": "Vực Sâu thăm thẳm đang dõi nhìn bạn, Golem San Hô giờ đây sẽ xuất hiện dưới đại dương...",
    "block.cataclysm.cursed_tombstone.message": "Sức mạnh của nó vẫn còn quá yếu ớt....",
    "entity.cataclysm.ignis.defeat_message": "Bên trong Pháo Đài Địa Ngục, các Ignited Berserker đã thức tỉnh...",

    # ─── EPIC FIGHT / EFN / AWAKEN / SKILLS ────────────────────────────────────
    "skill.efn.crescentmoon.tooltip": "Dung Hợp Linh Hồn",
    "skill.epicfight.efn_sekiro.category": "Tuyệt Kỹ Sekiro",
    "skill.efn.zansetsu": "Chế Độ Trảm Kích (Blade Mode)",
    "skill.efn.beastclaw.tooltip": "Vuốt Dã Thú",
    "skill_tree.efn.efn_skills": "Epic Fight: Dạ Khúc Tử Thần",
    "skill.efn.parry_master": "Bậc Thầy Đỡ Đòn (Parry Master)",
    "skill.efn.execution": "Đoạt Hồn Trảm",
    "skill.efn.precise_parry": "Đỡ Đòn Chuẩn Xác",
    "skill.epicfight.efn_arts.category": "Tuyệt Kỹ Dạ Khúc",
    "skill.efn.broadblade.tooltip": "Lưỡi Kiếm Phá Giáp",
    "skill.epicfight.efn_zansetsu.category": "CHẾ ĐỘ TRẢM KÍCH",
    "skill.epicfight_awaken.darknight_pursuiters.tooltip5": "-[Trọng Kích] §f H H H H",
    "effect.epicfight_awaken.flame_enchant": "Phù Chú Lửa",
    "effect.epicfight_awaken.lightning_enchant": "Phù Chú Sét",
    "skill.epicfight_awaken.focused_strike": "Nhất Kích Tập Trung",
    "skill.epicfight_awaken.darknight_pursuiters": "Kẻ Truy Hồn Đêm Tối",
    "skill.wom.dodge_master": "Bậc Thầy Né Đòn (Dodge Master)",
    "skill.womalt.dodge_master": "Bậc Thầy Né Đòn (Dodge Master)",
    "skill.sword_soaring.vatansever_dodge": "Né Tránh Vatansever",

    # ─── FTB QUESTS & LIBRARY ──────────────────────────────────────────────────
    "item.ftblibrary.fluid_container.use": "Nhấp chuột phải vào bể chứa để làm rỗng bình",
    "item.ftbquests.barrier.config": "Đổi tên trong đe để đặt ID Nhiệm Vụ",
    "item.ftbquests.lootcrate.missing": "LỖI: Rương chiến lợi phẩm không xác định '%s'!",
    "item.ftbquests.stage_barrier.config": "Đổi tên trong đe để đặt Giai Đoạn",
    "item.ftbquests.barrier.nogui": "Giao diện vẫn đang trong quá trình phát triển",
    "item.ftbquests.barrier.disabled": "Chỉ hoạt động trong Chế Độ Chỉnh Sửa!",
    "item.ftbquests.book.disabled": "Giao diện Sách Nhiệm Vụ đã bị tắt!",

    # ─── GECKOLIB & SAINTS DRAGONS ─────────────────────────────────────────────
    "entity.geckolib.mutant_zombie.equip": "Đã trao %1$s cho thực thể",
    "item.geckolib.jack_in_the_box.opening": "Đang mở Hộp Hề Bật Bất Ngờ (Jack-in-the-Box)!",
    "item.saintsdragons.scale_plucker.success": "Bạn đã cưỡng chế nhổ một chiếc vảy từ %s.",
    "entity.saintsdragons.all.mount_requires_saddle": "%s sẽ không cho bạn cưỡi nếu không có yên.",
    "item.saintsdragons.scale_plucker.health_too_low": "%s quá yếu để chịu đựng việc bị nhổ vảy.",
    "entity.saintsdragons.all.chest_requires_saddle": "%s cần có yên trước khi bạn có thể gắn rương.",

    # ─── NETHEREXP & LEGENDARY MONSTERS ────────────────────────────────────────
    "item.netherexp.smithing_template.pump_charge_upgrade.ingredients": "Ngọn Lửa Hiểm Độc (Treacherous Flame)",
    "item.netherexp.smithing_template.pump_charge_upgrade.applies_to": "Găng Tay Shotgun-Fist",
    "item.legendary_monsters.smithing_template.enderitium_upgrade1": "Nâng Cấp Enderitium",
    "item.legendary_monsters.smithing_template.annihilator_upgrade1": "Nâng Cấp Kẻ Hủy Diệt (Annihilator)",
    "item.legendary_monsters.smithing_template.enderitium_upgrade2": "Áp dụng cho:",
    "item.legendary_monsters.smithing_template.annihilator_upgrade2": "Áp dụng cho:",
    "item.legendary_monsters.smithing_template.enderitium_upgrade3": " Trang Bị Kim Cương (Diamond Equipment)",
    "item.legendary_monsters.smithing_template.annihilator_upgrade3": " Trang Bị Netherite (Netherite Equipment)",
    "item.legendary_monsters.smithing_template.enderitium_upgrade5": " Thỏi Enderitium (Enderitium Ingot)",
    "item.legendary_monsters.smithing_template.annihilator_upgrade5": " Mảnh Cổng Dịch Chuyển (Portal Shard)",

    # ─── MEBAHEL CREATURES DRAUGR ──────────────────────────────────────────────
    "item.mebahelcreaturesdraugr.filled_draugr_awakening_soul_gem.msg.surface_required": "Bạn phải ở trên mặt đất mới có thể sử dụng viên ngọc này!",
    "item.mebahelcreaturesdraugr.filled_draugr_awakening_soul_gem.msg.awakened": "Bạn vừa đánh thức một ác quỷ cổ đại...",
    "item.mebahelcreaturesdraugr.filled_draugr_awakening_soul_gem.msg.absorbing": "Đang hấp thụ linh hồn Draugr...",
    "block.mebahelcreaturesdraugr.draugr_altar.requires_golden_claw": "Bạn cần có Golden Claw (Móng Vuốt Vàng) để mở khóa tế đàn này",

    # ─── MINECRAFT & MODIFIERS ─────────────────────────────────────────────────
    "item.minecraft.smithing_template.netherite_upgrade.applies_to": "Trang Bị Kim Cương & Enderitium",
    "modifier.modifiers.none.info": "Không có thuộc tính bổ trợ",
    "item.supplementaries.bamboo_spikes_tipped_effect": "Chông Tre Tẩm %s"
}

def main():
    print("=" * 70)
    print("  TAWA DEEP DESCRIPTIONS LOCALIZATION INJECTOR")
    print(f"  Injecting {len(DEEP_TRANSLATIONS)} specific high-fidelity translations...")
    print("=" * 70)

    total_updated = 0
    total_files = 0

    for target in TARGET_DIRS:
        if not target.exists():
            continue
        print(f"[TARGET] Scanning {target.name}...")
        for ns_dir in target.iterdir():
            if not ns_dir.is_dir(): continue
            ns = ns_dir.name
            lang_dir = ns_dir / "lang"
            if not lang_dir.exists(): continue

            for lang_file in ["vi_vn.json", "zh_cn.json", "en_us.json"]:
                p = lang_dir / lang_file
                if not p.exists(): continue
                try:
                    data = json.load(open(p, encoding='utf-8'))
                    changed = False
                    for k, v in DEEP_TRANSLATIONS.items():
                        if k in data:
                            if data[k] != v:
                                data[k] = v
                                changed = True
                                total_updated += 1
                        else:
                            # Nếu key thuộc namespace này thì inject luôn
                            prefix = k.split('.')[1] if '.' in k else ''
                            if prefix == ns:
                                data[k] = v
                                changed = True
                                total_updated += 1

                    if changed:
                        with open(p, 'w', encoding='utf-8', newline='\n') as fp:
                            json.dump(data, fp, ensure_ascii=False, indent=2)
                            fp.write('\n')
                        total_files += 1
                except Exception as e:
                    print(f"Error updating {p}: {e}")

    print(f"\n[HOÀN TẤT] Đã cập nhật thành công {total_updated} keys trên {total_files} file ngôn ngữ!")
    print("=" * 70)

if __name__ == "__main__":
    main()
