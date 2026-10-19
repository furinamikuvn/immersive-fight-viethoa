import os
import sys
import json
import zipfile
import re

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
rp_dir = os.path.join(base_dir, "resourcepacks")
vh_assets = os.path.join(base_dir, "resourcepack", "IMF-VietHoa", "assets")

# -------------------------------------------------------------
# 1. DICTIONARIES
# -------------------------------------------------------------

bdhill_fight_more = {
    "item.fight_more.agony_b": "§3Minh Vương Hades",
    "item.fight_more.torment_b": "§6Atum Thất Lạc",
    "item.fight_more.ruine_b": "Thiên Vực Chiến Thần Ares",
    "item.fight_more.satsujin_b": "§4Cừu Oán Nemesis",
    "item.fight_more.ender_blaster_b": "Kẻ Hành Mạt Lộ Mục Thần Pan",
    "item.fight_more.herrscher_b": "§6Ách Vận & Mệnh Số Moros",
    "item.fight_more.gesetz_b": "§6Vô Tận Tôi Luyện Hephaestus",
    "item.fight_more.moonless_b": "§eNguyệt Nhị Trọng Tướng Artemis",
    "item.fight_more.solar_b": "§6Thái Dương Thần Apollo",
    "item.fight_more.antitheus_b": "U Ám Chi Ảnh Erebus"
}

imf_fight_more = {
    "item.fight_more.agony_p": "Thống Khổ",
    "item.fight_more.ruine_p": "Hủy Diệt",
    "item.fight_more.satsujin_p": "Sát Lục",
    "item.fight_more.solar_p": "Thái Dương",
    "item.fight_more.antitheus_p": "Thần Vẫn",
    "item.fight_more.ender_blaster_p": "Toái Ảnh",
    "item.fight_more.moonless_p": "Nguyệt Thực",
    "item.fight_more.gesetz_p": "Thần Quyền",
    "item.fight_more.herrscher_p": "Chúa Tể",
    "item.fight_more.torment_p": "Đoạ Đày",
    "item.fight_more.food_ring": "Nhẫn Ăn Nhanh",
    "item.fight_more.food_ring_high": "Nhẫn Ăn Nhanh II",
    "item.fight_more.ring_stun": "Nhẫn Miễn Choáng",
    "tooltip.fight_more.food_ring": "Tăng 30% tốc độ ăn",
    "tooltip.fight_more.food_ring_high": "Tăng 50% tốc độ ăn",
    "tooltip.fight_more.ring_stun": "Miễn nhiễm hiệu ứng choáng khựng",
    "item.fight_more.friendly_ring": "Nhẫn Thân Ái",
    "block.fight_more.guardian_summoning_block": "Bàn Thờ Triệu Hồi",
    "block.fight_more.golem_summoning_block": "Bàn Thờ Triệu Hồi",
    "block.fight_more.evil_summoning_block": "Bàn Thờ Triệu Hồi",
    "block.fight_more.skrythe_summoning_block": "Bàn Thờ Triệu Hồi",
    "block.fight_more.ice_summoning_block": "Bàn Thờ Triệu Hồi",
    "block.fight_more.rock_summoning_block": "Bàn Thờ Triệu Hồi",
    "block.fight_more.lava_summoning_block": "Bàn Thờ Triệu Hồi",
    "block.fight_more.rhyza_summoning_block": "Bàn Thờ Triệu Hồi",
    "tooltip.fight_more.friendly_ring": "Nhận hiệu ứng Hồi Máu II",
    "entity.fight_more.chaos_knight": "Hiệp Sĩ Hỗn Loạn (Chaos Knight)",
    "rarity.common.name": "",
    "rarity.uncommon.name": "",
    "rarity.rare.name": "Hiếm",
    "rarity.epic.name": "Sử Thi"
}

imf_epicfightx = {
    "pack.epicfightx.efx_epicfight_resource_pack.title": "asanginxst's Epic Fight Textures",
    "pack.epicfightx.efx_epicfight_assets_override.title": "EFX Assets Override",
    "skill.epicfightx.step": "Sải Bước",
    "skill.epicfightx.roll": "Nhào Lộn",
    "itemGroup.efx.items": "Epic Fight - Nội Dung Bổ Sung",
    "item.efx.scythe.description1": "",
    "item.epicfightx.eternal_night_scythe": "Lưỡi Hái Vĩnh Dạ (Eternal Night Scythe)",
    "skill.epicfightx.combat_mastery_i": "Tinh Thông Chiến Đấu I",
    "skill.epicfightx.combat_mastery_ii": "Tinh Thông Chiến Đấu II",
    "skill.epicfight.combat_mastery_i": "Tinh Thông Chiến Đấu I",
    "skill.epicfight.combat_mastery_i.tooltip": "Bạn ngày càng thuần thục nắm bắt cơ hội giữa tấn công và né tránh. Bạn có thể tung ra đòn tấn công đặc biệt nối tiếp ngay sau khi né.",
    "skill.epicfight.combat_mastery_ii": "Tinh Thông Chiến Đấu II",
    "skill.epicfight.combat_mastery_ii.tooltip": "Trong một khoảng thời gian ngắn sau khi né, chạy bộ sẽ kích hoạt trạng thái [Tật Hành], trạng thái này sẽ tiêu hao thể lực liên tục.",
    "skill.epicfight.scythe_skill": "Trảm Thủ / Hắc Dạ Lễ Tán",
    "skill.epicfight.scythe_skill.tooltip": "Bạn lướt về phía trước tóm lấy một mục tiêu, sau khi tóm thành công bạn có thể chọn:\n  Trảm Thủ [Chuột Trái]: Gây sát thương dựa trên % máu tối đa của mục tiêu;\n  Hắc Dạ Lễ Tán [Chuột Phải]: Đập mục tiêu xuống đất dùng ma thuật bóng tối gây nhiều lần sát thương và hồi máu cho bản thân.\n  Nếu mục tiêu không thể tóm, tung một nhát chém uy lực cực mạnh.",
    "effect.efx.efx_speed": "Tinh Thông Chiến Đấu II: Tăng Tốc Độ",
    "epicfight.style.scythe": "Cầm Hai Tay",
    "skill.epicfightx.steel_whirlwind": "Lốc Xoáy Thép"
}

imf_cdmoveset = {
    "cdmoveset.weapon_category.katana": "Katana",
    "epicfight.weapon_category.dual_tachi": "Trọng Thái Đao (Dual Tachi)",
    "epicfight.weapon_category.s_greatsword": "Trọng Kiếm Cường Hóa",
    "epicfight.weapon_category.s_longsword": "Trường Kiếm Cường Hóa",
    "epicfight.weapon_category.s_spear": "Trường Thương Cường Hóa",
    "epicfight.weapon_category.s_sword": "Đơn Thủ Kiếm Cường Hóa",
    "epicfight.weapon_category.s_tachi": "Thái Đao Cường Hóa",
    "epicfight.weapon_category.yamato": "Diêm Ma Đao (Yamato)",
    "item.cdmoveset.dual_tachi": "Trọng Thái Đao",
    "item.cdmoveset.katana": "Katana",
    "item.cdmoveset.katana.tooltip": "Tra kiếm vào bao sau 5 giây không tấn công, đòn đánh kế tiếp sẽ được cường hóa. Kỹ năng cũng được cường hóa theo.",
    "item.cdmoveset.s_diamonddagger": "Dao Găm Kim Cương Cường Hóa",
    "item.cdmoveset.s_diamondgreatsword": "Trọng Kiếm Kim Cương Cường Hóa",
    "item.cdmoveset.s_diamondlongsword": "Trường Kiếm Kim Cương Cường Hóa",
    "item.cdmoveset.s_diamondspear": "Trường Thương Kim Cương Cường Hóa",
    "item.cdmoveset.s_diamondsword": "Kiếm Kim Cương Cường Hóa",
    "item.cdmoveset.s_diamondtachi": "Thái Đao Kim Cương Cường Hóa",
    "item.cdmoveset.s_irondagger": "Dao Găm Sắt Cường Hóa",
    "item.cdmoveset.s_irongreatsword": "Trọng Kiếm Sắt Cường Hóa",
    "item.cdmoveset.s_ironlongsword": "Trường Kiếm Sắt Cường Hóa",
    "item.cdmoveset.s_ironspear": "Trường Thương Sắt Cường Hóa",
    "item.cdmoveset.s_ironsword": "Kiếm Sắt Cường Hóa",
    "item.cdmoveset.s_irontachi": "Thái Đao Sắt Cường Hóa",
    "item.cdmoveset.s_netheritedagger": "Dao Găm Netherite Cường Hóa",
    "item.cdmoveset.s_netheritegreatsword": "Trọng Kiếm Netherite Cường Hóa",
    "item.cdmoveset.s_netheritelongsword": "Trường Kiếm Netherite Cường Hóa",
    "item.cdmoveset.s_netheritesword": "Kiếm Netherite Cường Hóa",
    "item.cdmoveset.s_netheritetachi": "Thái Đao Netherite Cường Hóa",
    "item.cdmoveset.yamato": "Diêm Ma Đao (Cổ Bản)",
    "item.cdmoveset.yamato.tooltip": "Phiên bản suy yếu của Diêm Ma Đao, bạn cảm nhận được sức mạnh từ thanh đao này không ổn định.",
    "item_group.cdmoveset.corrupt_fight": "Corrupt Fight",
    "pack.More_Power.title": "More_Power ! ! !",
    "pack.corrupt_animation.title": "Corrupt Animation",
    "skill.cdmoveset.bloodwolf": "Lang Hồn",
    "skill.cdmoveset.bloodwolf.tooltip": "Khi tiếng sói hú vang lên, đó là lúc phản kích. Nhận được sự che chở của Sói Thần thông qua việc né tránh và tiêu diệt kẻ địch. Khi tầng kỹ năng đạt 10, sẽ nhận được sự bảo hộ của Sói Thần, cường hóa đòn tấn công của bản thân và có tỉ lệ làm gián đoạn đòn tấn công của kẻ địch.",
    "skill.cdmoveset.cdparryskill": "Đỡ Đòn Đặc Chế",
    "skill.cdmoveset.cdparryskill.tooltip": "Kỹ năng đỡ đòn đặc chế cho phiên bản cũ.",
    "skill.cdmoveset.dual_slash": "Điệu Nhảy Ranh Giới",
    "skill.cdmoveset.dual_slash.tooltip": "Vung đao liên hoàn tạo thành điệu nhảy ranh giới sắc bén.",
    "skill.cdmoveset.greatsword_dual_skill": "Liệt Địa Trảm",
    "skill.cdmoveset.greatsword_dual_skill.tooltip": "Đòn tấn công chấn động mặt đất mạnh mẽ, quật ngã toàn bộ kẻ địch trong phạm vi.",
    "skill.cdmoveset.guardparry": "Tuyệt Đối Phòng Ngự",
    "skill.cdmoveset.guardparry.tooltip": "Cho phép điều chỉnh tư thế phòng ngự, và trong thời gian kỹ năng duy trì, đỡ toàn bộ đòn đánh có thể đỡ. Mỗi khi tiêu diệt một kẻ địch hồi phục một tầng điểm phòng ngự (Chỉ số cơ bản của điểm phòng ngự là 4, phù phép Quét Của Kiếm có thể tăng điểm phòng ngự).",
    "skill.cdmoveset.katanaskill": "Hội Tâm Nhất Kích",
    "skill.cdmoveset.katanaskill.tooltip": "Cú đâm cực nhanh xuyên thủng kẻ địch trên đường đi. Ở trạng thái chạy bộ có thể tra kiếm vào bao và tung ra đòn chém uy lực.",
    "skill.cdmoveset.katanaspskill": "Hội Tâm Phản Sát",
    "skill.cdmoveset.katanaspskill.tooltip": "Dựng tư thế thủ, chặn đòn đánh của kẻ địch và tung nhát chém kết liễu kẻ địch.",
    "skill.cdmoveset.lethalslicing": "Trảm Cắt Chí Mạng",
    "skill.cdmoveset.lethalslicing.tooltip": "Làm choáng kẻ địch và tung cú chém uy lực, số lần chém thay đổi tùy theo số lượng kẻ địch.",
    "skill.cdmoveset.psstep": "Lang Thần Chi Dược",
    "skill.cdmoveset.psstep.tooltip": "Cho phép bạn sử dụng các động tác khác nhau để né tránh. Né tránh thành công kích hoạt hiệu ứng đặc biệt và hồi phục năng lượng vũ khí.",
    "skill.cdmoveset.shiled_slahs": "Thuẫn Kích!!!!",
    "skill.cdmoveset.shiled_slahs.tooltip": "Sử dụng khiên chặn đứng đòn tấn công của kẻ địch và làm choáng chúng.",
    "skill.cdmoveset.spearslash": "Thương Vũ",
    "skill.cdmoveset.spearslash.tooltip": "Tóm lấy kẻ địch xung quanh và quật ngã chúng cực mạnh.",
    "skill.cdmoveset.fatalfalsh": "Nhất Thiểm",
    "skill.cdmoveset.fatalfalsh.tooltip": "Khóa mục tiêu kẻ địch thấp máu và tung nhát chém kết liễu.\nKhi kẻ địch dưới mức máu nhất định sẽ xuất hiện dấu ấn kết liễu, nhấp chuột trái để kết liễu, trong thời gian kết liễu không thể bị gián đoạn.\n(Vũ khí khả dụng: Katana, Tachi, Trường Kiếm)",
    "skill.cdmoveset.sstep": "Chưa Bật",
    "skill.cdmoveset.sstep.tooltip": "Sách kỹ năng chưa kích hoạt.\n\n(Thể lực: %d)",
    "skill.cdmoveset.sword_slash": "Cường Hóa Hoành Tảo",
    "skill.cdmoveset.sword_slash.tooltip": "Xoay người về phía trước tung ra một đòn chém uy lực.",
    "skill.cdmoveset.wind_slash": "Lốc Xoáy Thép",
    "skill.cdmoveset.wind_slash.tooltip": "Nâng cao đại kiếm của bạn, chém tan toàn bộ kẻ địch xung quanh.",
    "skill.cdmoveset.yamato_step": "Ảo Ảnh",
    "skill.cdmoveset.yamato_step.tooltip": "Tốc biến về hướng chỉ định. Né tránh toàn bộ đòn tấn công có thể né.\n\n(Thể lực: %d)",
    "skill.cdmoveset.bstep": "Sải Bước Linh Hoạt",
    "skill.cdmoveset.bstep.tooltip": "Sải bước né tránh linh hoạt hơn.\n\n(Thể lực: %d)",
    "skill.cdmoveset.yamatoskill": "Diêm Ma Đao",
    "skill.cdmoveset.yamatoskill.tooltip": "Kỹ năng thông thường trong giai đoạn chuẩn bị nếu bị kẻ địch tấn công có thể phản đòn. Sau các đòn 1A, 2A, 3A đều có thể tung ra chuỗi combo nối tiếp. Sau khi đỡ đòn có thể giải phóng Hư Huyễn Đao Giới để phản kích.\nTùy theo đòn tấn công mà tạo ra chuỗi combo khác nhau."
}

imf_p1nero_bow = {
    "effect.p1nero_bow.double_arrow": "Song Tiễn",
    "effect.p1nero_bow.double_arrow.description": "Đòn bắn cung sẽ bắn ra hai mũi tên cùng lúc",
    "item.p1nero_bow.mortis": "Metis",
    "item.p1nero_bow.mortis_innate.tooltip0": "Âm Vang Của Metis",
    "item.p1nero_bow.mortis_innate.tooltip1": "Khi bắn tên nhấn [%s] để hủy bỏ chuyển động giật lùi về sau.",
    "item.p1nero_bow.mortis_innate.tooltip2": "Sau khi tung đòn đánh thường nhấn [%s] để phát động đòn cận chiến và đặt lại combo.",
    "item.p1nero_bow.mortis_innate.tooltip3": "Khi nạp đầy năng lượng, nhận hiệu ứng bắn tên đôi."
}

imf_level_hp = {
    "gui.level_hp.hpexp.label_empty": "/",
    "message.dielost": " §cMất §a§l",
    "gui.level_hp.hpexp.label_varintegerhpexp": "<VAR:integer:hpexp>",
    "message.getexp": "Nhận được §c",
    "config.level_hp.levelhpconfig": "levelhp-common",
    "message.imlevelup": "§e§l Cấp!!",
    "message.levelup": "§e§lHp Lên Cấp!",
    "message.mlevelup": "§e§lHp Lên Cấp §c§l",
    "message.iidielost": "§c Bình Chứa Trái Tim",
    "message.iiidielost": "§c || §eCấp hiện tại: §a§l",
    "gui.level_hp.hpexp.label_lv": "Lv",
    "item.level_hp.heartcontainers": "Bình Chứa Trái Tim",
    "message.adielost": "Bạn đã chết, mất đi §etoàn bộ kinh nghiệm HP và cấp độ",
    "message.ilevelup": "§fCấp độ",
    "gui.level_hp.hpexp.label_varintegerhplevel": "<VAR:integer:hplevel>",
    "gui.level_hp.hpexp.label_varintegerleveluphpexp": "<VAR:integer:leveluphpexp>",
    "message.idielost": "§a§l",
    "message.igetexp": "§f Kinh nghiệm HP!"
}

imf_ssamod = {
    "key.category.ssamod": "Sunrise & Sunset Audio",
    "key.category.ssamod.openoptions": "Mở Cài Đặt",
    "gui.ssa.options": "Sunrise & Sunset Audio",
    "gui.ssa.options_play": "⏵",
    "gui.ssa.options_slider_rooster": "Tiếng Gà Gáy: ",
    "gui.ssa.options_slider_wolf": "Tiếng Sói Hú: ",
    "gui.ssa.options_play_cave": "Phát Âm Thanh Trong Hang",
    "gui.ssa.options_send_messages": "Gửi Thông Báo",
    "gui.ssa.options_update": "Đã có phiên bản mới của mod!",
    "gui.ssa.options_reset": "Đặt Lại Mặc Định",
    "gui.ssa.options_morning_tick": "Tick Buổi Sáng (10 - 23999)",
    "gui.ssa.options_evening_tick": "Tick Buổi Tối (10 - 23999)",
    "gui.ssa.options_chance_rooster": "Tỉ Lệ: ",
    "gui.ssa.options_chance_wolf": "Tỉ Lệ: ",
    "gui.ssa.options_moon_phase_all": "Tất Cả",
    "gui.ssa.options_moon_phase_full_moon": "Trăng Tròn",
    "gui.ssa.options_moon_phase_tooltip": "Chọn chu kỳ trăng phát âm thanh sói hú",
    "messages.ssa.morning_message": "Trời đã sáng...",
    "messages.ssa.evening_message": "Màn đêm buông xuống...",
    "messages.ssa.error_message_invalid_value": "Giá trị không hợp lệ! Đã đặt về mặc định",
    "messages.ssa.error_message_same_value": "Giá trị không thể giống nhau! Đã đặt về mặc định",
    "gui.ssa.options_play_in_other_dim": "Phát Âm Thanh Ở Chiều Không Gian Khác",
    "gui.ssa.options_send_messages_in_other_dim": "Gửi Thông Báo Ở Chiều Không Gian Khác"
}

imf_ftbteams = {
    "ftbteams.already_in_party": "Bạn đã ở trong một đội rồi!",
    "ftbteams.player_already_in_party": "Người chơi \"%s\" đã ở trong một đội rồi!",
    "ftbteams.not_in_party": "Bạn chưa tạo hoặc tham gia đội nào!",
    "ftbteams.team_not_found": "Không tìm thấy đội \"%s\"!",
    "ftbteams.cant_edit": "Bạn không thể chỉnh sửa %s!",
    "ftbteams.not_member": "%s không phải thành viên của %s!",
    "ftbteams.not_officer": "%s không phải đội trưởng của %s!",
    "ftbteams.not_invited": "Bạn chưa được mời tham gia %s!",
    "ftbteams.name_too_short": "Tên đội quá ngắn! (Cần ít nhất 3 ký tự)",
    "ftbteams.server_permissions_prevent": "Quyền hạn máy chủ ngăn cản bạn thực hiện thao tác này.",
    "ftbteams.info.id": "ID Dài của Đội: %s",
    "ftbteams.info.short_id": "ID Ngắn của Đội: %s",
    "ftbteams.info.owner": "Đội Trưởng: %s",
    "ftbteams.info.owner.none": "Không có",
    "ftbteams.info.members": "Thành viên:",
    "ftbteams.info.members.none": "Không có thành viên",
    "ftbteams.list": "Tất cả các đội FTB: %s",
    "ftbteams.property_not_found": "Không tìm thấy ID thuộc tính!",
    "ftbteams.owner_cant_leave": "Trước khi rời đội, bạn phải chuyển quyền sở hữu đội!",
    "ftbteams.cant_kick_owner": "Không thể đá đội trưởng!",
    "ftbteams.party_api_only": "Trong modpack này, bạn không thể trực tiếp tạo đội!",
    "ftbteams.api_override": "Trong modpack này, bạn chỉ có thể tạo đội qua nút \"Đội Của Tôi\" trong túi đồ!",
    "ftbteams.missing_data": "Chưa nhận được dữ liệu đội từ máy chủ!\nFTB Teams sẽ không hoạt động bình thường.\nVui lòng kiểm tra log máy chủ.",
    "sidebar_button.ftbteams.my_team": "Đội Của Tôi",
    "ftbteamsconfig": "Thuộc Tính Đội",
    "ftbteamsconfig.ftbteams": "Thuộc Tính Đội Cơ Bản",
    "ftbteamsconfig.ftbteams.display_name": "Tên Hiển Thị",
    "ftbteamsconfig.ftbteams.description": "Mô Tả",
    "ftbteamsconfig.ftbteams.color": "Màu Sắc",
    "ftbteamsconfig.ftbteams.free_to_join": "Tự Do Gia Nhập",
    "ftbteamsconfig.ftbteams.max_msg_history_size": "Dung lượng tối đa lịch sử trò chuyện",
    "ftbteams.privacy_mode.allies": "Đồng Minh",
    "ftbteams.privacy_mode.private": "Riêng Tư",
    "ftbteams.privacy_mode.public": "Công Khai",
    "ftbteams.create_party": "Tạo Một Đội",
    "ftbteams.create_party.info": "Tạo một đội để mời thành viên và cùng chơi",
    "ftbteams.gui.kick": "Đá %s",
    "ftbteams.gui.kick.confirm": "Bạn có chắc chắn muốn đá người chơi %s không?",
    "ftbteams.gui.promote": "Thăng chức %s",
    "ftbteams.gui.promote.confirm": "Bạn có chắc muốn thăng chức người chơi %s không?",
    "ftbteams.gui.demote": "Giáng chức %s",
    "ftbteams.gui.demote.confirm": "Bạn có chắc muốn giáng chức người chơi %s không?",
    "ftbteams.gui.leave": "Rời Đội",
    "ftbteams.gui.leave.confirm": "Bạn có chắc chắn muốn rời đội không?",
    "ftbteams.gui.disband": "Giải Tán Đội",
    "ftbteams.gui.disband.confirm": "Bạn có chắc chắn muốn giải tán đội không?",
    "ftbteams.gui.transfer_ownership": "Chuyển Đội Trưởng cho %s",
    "ftbteams.gui.transfer_ownership.confirm": "Bạn có chắc chắn muốn chuyển đội trưởng cho %s không?",
    "ftbteams.gui.party_name": "Tên Đội",
    "ftbteams.gui.party_description": "Mô Tả",
    "ftbteams.gui.create_party": "Tạo Đội",
    "ftbteams.gui.add_members": "Thêm Thành Viên",
    "ftbteams.gui.invite": "Mời Người Chơi",
    "ftbteams.gui.manage_allies": "Quản Lý Đồng Minh",
    "ftbteams.gui.no_players": "Không có người chơi nào khả dụng",
    "ftbteams.gui.send_invite": "Mời",
    "ftbteams.gui.add_ally": "Đồng Minh",
    "ftbteams.gui.remove_ally": "Hủy đồng minh với %s",
    "ftbteams.gui.remove_ally.confirm": "Bạn có chắc muốn hủy quan hệ đồng minh với %s không?",
    "ftbteams.ranks.enemy": "Kẻ Địch",
    "ftbteams.ranks.none": "Không",
    "ftbteams.ranks.ally": "Đồng Minh",
    "ftbteams.ranks.invited": "Đã Mời",
    "ftbteams.ranks.member": "Thành Viên",
    "ftbteams.ranks.officer": "Quản Trị Viên",
    "ftbteams.ranks.owner": "Đội Trưởng",
    "ftbteams.team_type.player": "Đội Người Chơi",
    "ftbteams.team_type.party": "Đội",
    "ftbteams.team_type.server": "Đội Máy Chủ",
    "key.ftbteams.open_gui": "Mở Giao Diện Đội",
    "key.categories.ftbteams": "FTB Teams",
    "ftbteams.message.invited": "Đã mời %s",
    "ftbteams.message.invite_sent": "%s mời bạn gia nhập đội của họ!",
    "ftbteams.message.joined": "%s đã gia nhập đội của bạn!",
    "ftbteams.message.declined": "Bạn đã từ chối lời mời",
    "ftbteams.message.kicked": "Đã đá %s khỏi %s!",
    "ftbteams.message.promoted": "Đã thăng chức %s lên Quản Trị Viên!",
    "ftbteams.message.demoted": "Đã giáng chức %s xuống Thành Viên!",
    "ftbteams.message.transfer_owner": "Đã chuyển quyền đội trưởng cho %s!",
    "ftbteams.message.left_party": "Người chơi %s đã rời khỏi đội!",
    "ftbteams.message.add_ally": "Người chơi %s hiện là đồng minh của đội bạn!",
    "ftbteams.message.now_allied": "Bạn hiện là đồng minh của \"%s\"!",
    "ftbteams.message.remove_ally": "Người chơi %s không còn là đồng minh của đội bạn!",
    "ftbteams.message.no_longer_allied": "Bạn không còn là đồng minh của \"%s\"!",
    "ftbteams.message.created_server_team": "Đã tạo đội máy chủ mới \"%s\"!",
    "ftbteams.message.deleted_server_team": "Đã xóa đội máy chủ \"%s\"!",
    "ftbteams.message.team_disbanded": "Đã cưỡng chế giải tán đội \"%s\" (%s)!",
    "ftbteams.accept": "Chấp Nhận ✔",
    "ftbteams.decline": "Từ Chối ✘"
}

celepic_dict = {
    "effect.celepic.attack_boost": "Huyết Tế Chung Cực",
    "effect.celepic.attack_boost.description": "Tăng sát thương tấn công. Ở trạng thái này có thể tiêu hao 12 tầng năng lượng và hủy diệt tất cả.",
    "effect.celepic.auto_attack": "Vũ Điệu Hoa",
    "enchantment.celestisynth.pulsation.desc": "Có tỉ lệ kích hoạt tăng sát thương tấn công và đẩy lùi",
    "effect.celepic.auto_attack.description": "Tự động tấn công."
}

enchanlownew_dict = {
    "item.enchanlownew.paper_ring_low": "Phiếu Đổi Phụ Kiện (Thường)",
    "item.enchanlownew.paper_ring_high": "Phiếu Đổi Phụ Kiện (Cao Cấp)",
    "item.enchanlownew.paper_skill_low": "Phiếu Đổi Sách Kỹ Năng (Thường)",
    "item.enchanlownew.paper_skill_high": "Phiếu Đổi Sách Kỹ Năng (Cao Cấp)",
    "item.enchanlownew.skill_paper": "Mảnh Tàn Trang Sách",
    "item.enchanlownew.power_rune": "Phiến Đá Phù Văn Nạp Lực"
}

lootbags_dict = {
    "itemGroup.lootbags.main": "Túi Chiến Lợi Phẩm",
    "item.lootbags.commonlootbag": "Common Loot Bag",
    "item.lootbags.uncommonlootbag": "Uncommon Loot Bag",
    "item.lootbags.rarelootbag": "Rare Loot Bag",
    "item.lootbags.epiclootbag": "Epic Loot Bag"
}

simplyusekey_dict = {
    "key.category.simplyusekey.category": "Phím Tắt Simply Swords",
    "key.simplyusekey.example": "Simply Swords: Dùng Kỹ Năng"
}

womalt_dict = {
    "death.attack.ender_bullet.item": "%1$s bị đạn Ender của %2$s bắn trúng và tử nạn.",
    "death.attack.timed_katana_slashes.item": "%1$s không hề hay biết... bản thân đã sớm vong mạng!",
    "death.attack.perfect_bulkwark_shockwave.item": "%1$s bị đánh bay sang Linh Giới!",
    "death.attack.lunar_eclipse.item": "%1$s không thể chống đỡ sức mạnh thần bí của Nguyệt Thực.",
    "gamerule.spawnStrongerMobs": "Sinh quái vật mạnh hơn theo khoảng cách",
    "gamerule.strongerMobsDropEmeralds": "Quái vật mạnh hơn rơi ra ngọc lục bảo",
    "gamerule.strongerMobsMoreEXP": "Quái vật mạnh hơn cho nhiều kinh nghiệm hơn",
    "gamerule.skeletonMoreMelee: 生成更多近战骷髅": "Sinh ra nhiều bộ xương cận chiến hơn",
    "gamerule.skeletonMoreMelee": "Sinh ra nhiều bộ xương cận chiến hơn",
    "entity.womalt.evil_skeleton": "Ác Ma Khô Lâu (Demon Skeleton)",
    "entity.womalt.hollow": "Kẻ Rỗng Tuếch (Hollow)",
    "entity.womalt.saulomonk": "Tu Sĩ Saul (Saul Monk)",
    "entity.womalt.lycanth": "Người Sói Bất Khiết (Unholy Werewolf)",
    "entity.womalt.lupus_rex": "Hoàng Kim Lang (Golden Wolf)",
    "item.minecraft.potion.effect.longer_night_vision": "Thuốc Nhìn Đêm Kéo Dài",
    "item.minecraft.splash_potion.effect.longer_night_vision": "Thuốc Nhìn Đêm Kéo Dài Dạng Ném",
    "item.minecraft.lingering_potion.effect.longer_night_vision": "Thuốc Nhìn Đêm Kéo Dài Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.longer_night_vision": "Mũi Tên Nhìn Đêm Kéo Dài",
    "item.minecraft.potion.effect.longer_invisibility": "Thuốc Tàng Hình Kéo Dài",
    "item.minecraft.splash_potion.effect.longer_invisibility": "Thuốc Tàng Hình Kéo Dài Dạng Ném",
    "item.minecraft.lingering_potion.effect.longer_invisibility": "Thuốc Tàng Hình Kéo Dài Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.longer_invisibility": "Mũi Tên Tàng Hình Kéo Dài",
    "item.minecraft.potion.effect.stronger_jump_boost": "Thuốc Nhảy Cao Cường Hóa",
    "item.minecraft.splash_potion.effect.stronger_jump_boost": "Thuốc Nhảy Cao Cường Hóa Dạng Ném",
    "item.minecraft.lingering_potion.effect.stronger_jump_boost": "Thuốc Nhảy Cao Cường Hóa Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.stronger_jump_boost": "Mũi Tên Nhảy Cao Cường Hóa",
    "item.minecraft.potion.effect.longer_jump_boost": "Thuốc Nhảy Cao Kéo Dài",
    "item.minecraft.splash_potion.effect.longer_jump_boost": "Thuốc Nhảy Cao Kéo Dài Dạng Ném",
    "item.minecraft.lingering_potion.effect.longer_jump_boost": "Thuốc Nhảy Cao Kéo Dài Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.longer_jump_boost": "Mũi Tên Nhảy Cao Kéo Dài",
    "item.minecraft.potion.effect.longer_fire_resistance": "Thuốc Kháng Lửa Kéo Dài",
    "item.minecraft.splash_potion.effect.longer_fire_resistance": "Thuốc Kháng Lửa Kéo Dài Dạng Ném",
    "item.minecraft.lingering_potion.effect.longer_fire_resistance": "Thuốc Kháng Lửa Kéo Dài Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.longer_fire_resistance": "Mũi Tên Kháng Lửa Kéo Dài",
    "item.minecraft.potion.effect.stronger_speed": "Thuốc Tốc Độ Cường Hóa",
    "item.minecraft.splash_potion.effect.stronger_speed": "Thuốc Tốc Độ Cường Hóa Dạng Ném",
    "item.minecraft.lingering_potion.effect.stronger_speed": "Thuốc Tốc Độ Cường Hóa Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.stronger_speed": "Mũi Tên Tốc Độ Cường Hóa",
    "item.minecraft.potion.effect.longer_speed": "Thuốc Tốc Độ Kéo Dài",
    "item.minecraft.splash_potion.effect.longer_speed": "Thuốc Tốc Độ Kéo Dài Dạng Ném",
    "item.minecraft.lingering_potion.effect.longer_speed": "Thuốc Tốc Độ Kéo Dài Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.longer_speed": "Mũi Tên Tốc Độ Kéo Dài",
    "item.minecraft.potion.effect.stronger_slowness": "Thuốc Chậm Chạp Cường Hóa",
    "item.minecraft.splash_potion.effect.stronger_slowness": "Thuốc Chậm Chạp Cường Hóa Dạng Ném",
    "item.minecraft.lingering_potion.effect.stronger_slowness": "Thuốc Chậm Chạp Cường Hóa Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.stronger_slowness": "Mũi Tên Chậm Chạp Cường Hóa",
    "item.minecraft.potion.effect.longer_slowness": "Thuốc Chậm Chạp Kéo Dài",
    "item.minecraft.splash_potion.effect.longer_slowness": "Thuốc Chậm Chạp Kéo Dài Dạng Ném",
    "item.minecraft.lingering_potion.effect.longer_slowness": "Thuốc Chậm Chạp Kéo Dài Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.longer_slowness": "Mũi Tên Chậm Chạp Kéo Dài",
    "item.minecraft.potion.effect.longer_water_breathing": "Thuốc Thở Dưới Nước Kéo Dài",
    "item.minecraft.splash_potion.effect.longer_water_breathing": "Thuốc Thở Dưới Nước Kéo Dài Dạng Ném",
    "item.minecraft.lingering_potion.effect.longer_water_breathing": "Thuốc Thở Dưới Nước Kéo Dài Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.longer_water_breathing": "Mũi Tên Thở Dưới Nước Kéo Dài",
    "item.minecraft.potion.effect.stronger_instant_health": "Thuốc Hồi Máu Cực Nhanh Cường Hóa",
    "item.minecraft.splash_potion.effect.stronger_instant_health": "Thuốc Hồi Máu Cực Nhanh Cường Hóa Dạng Ném",
    "item.minecraft.lingering_potion.effect.stronger_instant_health": "Thuốc Hồi Máu Cực Nhanh Cường Hóa Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.stronger_instant_health": "Mũi Tên Hồi Máu Cực Nhanh Cường Hóa",
    "item.minecraft.potion.effect.stronger_instant_damage": "Thuốc Sát Thương Tức Thì Cường Hóa",
    "item.minecraft.splash_potion.effect.stronger_instant_damage": "Thuốc Sát Thương Tức Thì Cường Hóa Dạng Ném",
    "item.minecraft.lingering_potion.effect.stronger_instant_damage": "Thuốc Sát Thương Tức Thì Cường Hóa Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.stronger_instant_damage": "Mũi Tên Sát Thương Tức Thì Cường Hóa",
    "item.minecraft.potion.effect.stronger_poison": "Thuốc Độc Cường Hóa",
    "item.minecraft.splash_potion.effect.stronger_poison": "Thuốc Độc Cường Hóa Dạng Ném",
    "item.minecraft.lingering_potion.effect.stronger_poison": "Thuốc Độc Cường Hóa Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.stronger_poison": "Mũi Tên Độc Cường Hóa",
    "item.minecraft.potion.effect.longer_poison": "Thuốc Độc Kéo Dài",
    "item.minecraft.splash_potion.effect.longer_poison": "Thuốc Độc Kéo Dài Dạng Ném",
    "item.minecraft.lingering_potion.effect.longer_poison": "Thuốc Độc Kéo Dài Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.longer_poison": "Mũi Tên Độc Kéo Dài",
    "item.minecraft.potion.effect.stronger_regeneration": "Thuốc Tái Tạo Cường Hóa",
    "item.minecraft.splash_potion.effect.stronger_regeneration": "Thuốc Tái Tạo Cường Hóa Dạng Ném",
    "item.minecraft.lingering_potion.effect.stronger_regeneration": "Thuốc Tái Tạo Cường Hóa Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.stronger_regeneration": "Mũi Tên Tái Tạo Cường Hóa",
    "item.minecraft.potion.effect.longer_regeneration": "Thuốc Tái Tạo Kéo Dài",
    "item.minecraft.splash_potion.effect.longer_regeneration": "Thuốc Tái Tạo Kéo Dài Dạng Ném",
    "item.minecraft.lingering_potion.effect.longer_regeneration": "Thuốc Tái Tạo Kéo Dài Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.longer_regeneration": "Mũi Tên Tái Tạo Kéo Dài",
    "item.minecraft.potion.effect.stronger_strength": "Thuốc Sức Mạnh Cường Hóa",
    "item.minecraft.splash_potion.effect.stronger_strength": "Thuốc Sức Mạnh Cường Hóa Dạng Ném",
    "item.minecraft.lingering_potion.effect.stronger_strength": "Thuốc Sức Mạnh Cường Hóa Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.stronger_strength": "Mũi Tên Sức Mạnh Cường Hóa",
    "item.minecraft.potion.effect.longer_strength": "Thuốc Sức Mạnh Kéo Dài",
    "item.minecraft.splash_potion.effect.longer_strength": "Thuốc Sức Mạnh Kéo Dài Dạng Ném",
    "item.minecraft.lingering_potion.effect.longer_strength": "Thuốc Sức Mạnh Kéo Dài Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.longer_strength": "Mũi Tên Sức Mạnh Kéo Dài",
    "item.minecraft.potion.effect.longer_weakness": "Thuốc Yếu Đuối Kéo Dài",
    "item.minecraft.splash_potion.effect.longer_weakness": "Thuốc Yếu Đuối Kéo Dài Dạng Ném",
    "item.minecraft.lingering_potion.effect.longer_weakness": "Thuốc Yếu Đuối Kéo Dài Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.longer_weakness": "Mũi Tên Yếu Đuối Kéo Dài",
    "item.minecraft.potion.effect.longer_slow_falling": "Thuốc Rơi Chậm Kéo Dài",
    "item.minecraft.splash_potion.effect.longer_slow_falling": "Thuốc Rơi Chậm Kéo Dài Dạng Ném",
    "item.minecraft.lingering_potion.effect.longer_slow_falling": "Thuốc Rơi Chậm Kéo Dài Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.longer_slow_falling": "Mũi Tên Rơi Chậm Kéo Dài",
    "item.minecraft.potion.effect.stronger_turtle_master": "Thuốc Thần Quy Cường Hóa",
    "item.minecraft.splash_potion.effect.stronger_turtle_master": "Thuốc Thần Quy Cường Hóa Dạng Ném",
    "item.minecraft.lingering_potion.effect.stronger_turtle_master": "Thuốc Thần Quy Cường Hóa Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.stronger_turtle_master": "Mũi Tên Thần Quy Cường Hóa",
    "item.minecraft.potion.effect.longer_turtle_master": "Thuốc Thần Quy Kéo Dài",
    "item.minecraft.splash_potion.effect.longer_turtle_master": "Thuốc Thần Quy Kéo Dài Dạng Ném",
    "item.minecraft.lingering_potion.effect.longer_turtle_master": "Thuốc Thần Quy Kéo Dài Dạng Kéo Dài Khói",
    "item.minecraft.tipped_arrow.effect.longer_turtle_master": "Mũi Tên Thần Quy Kéo Dài"
}

efn_dict = {
    "prompt.efn.judgementcut_end": "Thứ Nguyên Trảm - Tuyệt",
    "prompt.efn.angel": "Thế Thiên Thần",
    "prompt.efn.devil": "Thế Ác Quỷ",
    "prompt.efn.slasher1": "Tam Liên Trảm - 1",
    "prompt.efn.slasher2": "Tam Liên Trảm - 2",
    "prompt.efn.slasher3": "Tam Liên Trảm - 3",
    "prompt.efn.aerialrave1": "Ngự Không Đao Vũ - 1",
    "prompt.efn.aerialrave2": "Ngự Không Đao Vũ - 2",
    "prompt.efn.aerialrave3": "Ngự Không Đao Vũ - 3",
    "prompt.efn.orbit1": "Nguyệt Luân Đao - 1",
    "prompt.efn.orbit2": "Nguyệt Luân Đao - 2",
    "prompt.efn.killerbee": "Sát Nhân Phong",
    "prompt.efn.drive": "Đoạn Ngục Trảm",
    "prompt.efn.stomp": "Luyện Ngục Trụy",
    "prompt.efn.flush": "Không Nhận",
    "prompt.efn.crosscut3_alt": "Loạn Trảm - 1",
    "prompt.efn.crosscut4": "Loạn Trảm - 2",
    "prompt.efn.crosscut5": "Loạn Trảm - 3",
    "prompt.efn.doppelganger": "Chuyển Đổi Di Chuyển Phân Thân",
    "prompt.efn.summoned_sword": "Ảo Ảnh Kiếm",
    "prompt.efn.summoned_sword_angle": "Thiên Thần Ảo Ảnh Kiếm",
    "prompt.efn.summoned_sword_devil": "Ác Quỷ Ảo Ảnh Kiếm",
    "pack.power.title": "More Powerful Power!!!",
    "efn.configgui.yamato_catcher": "Cài Đặt Bắt Ảo Ảnh Kiếm Diêm Ma Đao",
    "efn.configgui.yamato_global_stun": "Cài Đặt Choáng Toàn Cục Diêm Ma Đao",
    "efn.configgui.yamato_parry_stun": "Cài Đặt Choáng Đỡ Đòn Diêm Ma Đao",
    "efn.configgui.animation": "Cài Đặt Hoạt Ảnh",
    "efn.configgui.yamato_reward": "Cài Đặt Phần Thưởng Diêm Ma Đao",
    "efn.configgui.judgementcut_end_camera": "Cài Đặt Camera Thứ Nguyên Trảm Tuyệt",
    "efn.configgui.judgementcut_end_particles": "Cài Đặt Hạt Thứ Nguyên Trảm Tuyệt",
    "efn.configgui.yamato_parry_timeslow": "Cài Đặt Làm Chậm Thời Gian Đỡ Đòn Diêm Ma Đao",
    "efn.configgui.dualsword_dodge_timeslow": "Cài Đặt Làm Chậm Thời Gian Né Song Đao",
    "efn.configgui.judgementcut_end_damage": "Cài Đặt Sát Thương Thứ Nguyên Trảm Tuyệt",
    "efn.configgui.bloodlust_posteffect": "Cài Đặt Bộ Lọc Kỹ Năng Huyết Điên Cuồng",
    "efn.config.category.yamato_catcher": "Cài Đặt Bắt Ảo Ảnh Kiếm Diêm Ma Đao",
    "efn.config.category.yamato_global_stun": "Cài Đặt Choáng Toàn Cục Diêm Ma Đao",
    "efn.config.category.yamato_parry_stun": "Cài Đặt Choáng Đỡ Đòn Diêm Ma Đao",
    "efn.config.category.animation": "Cài Đặt Hoạt Ảnh",
    "efn.config.category.yamato_reward": "Cài Đặt Phần Thưởng Diêm Ma Đao",
    "efn.config.category.judgementcut_end_camera": "Cài Đặt Camera Thứ Nguyên Trảm Tuyệt",
    "efn.config.category.judgementcut_end_particles": "Cài Đặt Hạt Thứ Nguyên Trảm Tuyệt",
    "efn.config.category.yamato_parry_timeslow": "Cài Đặt Làm Chậm Thời Gian Đỡ Đòn Diêm Ma Đao",
    "efn.config.category.dualsword_dodge_timeslow": "Cài Đặt Làm Chậm Thời Gian Né Song Đao",
    "efn.config.category.judgementcut_end_damage": "Cài Đặt Sát Thương Thứ Nguyên Trảm Tuyệt",
    "efn.config.category.bloodlust_posteffect": "Cài Đặt Bộ Lọc Kỹ Năng Huyết Điên Cuồng",
    "efn.config.yamato_catcher_blacklist": "Danh Sách Đen Bắt Ảo Ảnh Kiếm",
    "efn.config.yamato_catcher_whitelist": "Danh Sách Trắng Bắt Ảo Ảnh Kiếm",
    "efn.config.yamato_globalstun_whitelist": "Danh Sách Trắng Choáng Toàn Cục",
    "efn.config.yamato_parry_stun_duration": "Thời Lượng Choáng Đỡ Đòn",
    "efn.config.yamato_parry_stun_cooldown": "Hồi Chiêu Choáng Đỡ Đòn",
    "efn.config.animation_blacklist": "Danh Sách Đen Hoạt Ảnh",
    "efn.config.animation_whitelist": "Danh Sách Trắng Hoạt Ảnh",
    "efn.config.yamato_reward_enabled": "Bật Phần Thưởng Diêm Ma Đao",
    "efn.config.yamato_reward_kill_threshold": "Ngưỡng Tiêu Diệt Nhận Phần Thưởng",
    "efn.config.enable_judgementcut_end_camera_animations": "Bật Hoạt Ảnh Camera",
    "efn.config.enable_judgementcut_end_particles": "Bật Hiệu Ứng Hạt",
    "efn.config.enable_yamato_parry_timeslowdown": "Bật Hiệu Ứng Làm Chậm Thời Gian",
    "efn.config.enable_dualsword_dodge_timeslowdown": "Bật Làm Chậm Khi Né Song Đao",
    "efn.config.judgement_cut_end_damage_rate": "Bội Số Sát Thương",
    "efn.config.judgement_cut_end_cut_rate": "Tỉ Lệ Trảm Kích",
    "efn.config.judgement_cut_end_boss_damage_multiplier": "Bội Số Sát Thương Lên BOSS",
    "efn.config.judgement_cut_end_health_percentage": "Tỉ Lệ Máu",
    "efn.config.enable_bloodlust_posteffect": "Bật Bộ Lọc Màn Hình Huyết Cuồng",
    "efn.config.enable_vfx": "Bật/Tắt Liên Kết Hạt AAA",
    "efn.warning.title": "§l§eMod EFN - Lưu Ý Quan Trọng",
    "efn.warning.message": "Bạn đã cài đặt mod EFN nhưng chưa cài mod liên kết được khuyến nghị AAA Particles. Mod đó giúp nâng cao đáng kể hiệu ứng hình ảnh của EFN.",
    "efn.warning.recommendation": "§l§6Khuyến Nghị:",
    "efn.warning.recommendation.details": "Để có trải nghiệm tốt nhất với mod EFN, chúng tôi khuyên bạn nên cài đặt AAA Particles.",
    "efn.warning.download": "§aTải AAA Particles",
    "efn.warning.ignore": "§7Tôi đã hiểu, bỏ qua",
    "efn.warning.bottom_hint": "Sau khi chọn, thông báo này sẽ không hiện lại trong lần khởi động kế tiếp.",
    "efn.warning.close": "×",
    "efn.warning.close.tooltip": "Đóng cửa sổ này (sẽ hiển thị lại ở lần khởi động sau)",
    "tooltip.efn.config": "Tự động chuyển đổi né độc quyền có thể tắt trong tệp cấu hình"
}

# -------------------------------------------------------------
# 2. HELPER FUNCTIONS TO UPDATE A ZIP FILE IN-PLACE
# -------------------------------------------------------------
def update_zip_files(zip_path, file_dict):
    """
    file_dict is a mapping of internal_path -> json_data (dict)
    Rewrites the zip preserving other files.
    """
    tmp_path = zip_path + ".tmp"
    with zipfile.ZipFile(zip_path, 'r') as zin, zipfile.ZipFile(tmp_path, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
        handled = set()
        for item in zin.infolist():
            if item.filename in file_dict:
                data = file_dict[item.filename]
                zout.writestr(item.filename, json.dumps(data, ensure_ascii=False, indent=2))
                handled.add(item.filename)
            else:
                zout.writestr(item, zin.read(item.filename))
        for filename, data in file_dict.items():
            if filename not in handled:
                zout.writestr(filename, json.dumps(data, ensure_ascii=False, indent=2))
    os.replace(tmp_path, zip_path)
    print(f"Successfully updated zip: {os.path.basename(zip_path)}")

# -------------------------------------------------------------
# 3. GET OFFICIAL WAYSTONES VI_VN
# -------------------------------------------------------------
waystones_jar = os.path.join(base_dir, "mods", "waystones-forge-1.20.1-14.1.20.jar")
waystones_vi = {}
if os.path.exists(waystones_jar):
    with zipfile.ZipFile(waystones_jar, 'r') as z:
        waystones_vi = json.loads(z.read("assets/waystones/lang/vi_vn.json").decode('utf-8'))
print(f"Loaded official waystones vi_vn: {len(waystones_vi)} keys")

# -------------------------------------------------------------
# 4. PATCH BDHILL ZIP
# -------------------------------------------------------------
bd_zip = os.path.join(rp_dir, "BDHill Reforge the Sword Edge 沉浸特供.zip")
if os.path.exists(bd_zip):
    update_zip_files(bd_zip, {
        "assets/fight_more/lang/zh_cn.json": bdhill_fight_more,
        "assets/fight_more/lang/vi_vn.json": bdhill_fight_more
    })

# -------------------------------------------------------------
# 5. PATCH IMF-MODIFY.ZIP
# -------------------------------------------------------------
imf_mod_zip = os.path.join(rp_dir, "IMF-Modify.zip")
if os.path.exists(imf_mod_zip):
    imf_mod_files = {
        "assets/fight_more/lang/zh_cn.json": imf_fight_more,
        "assets/fight_more/lang/vi_vn.json": imf_fight_more,
        "assets/epicfightx/lang/zh_cn.json": imf_epicfightx,
        "assets/epicfightx/lang/vi_vn.json": imf_epicfightx,
        "assets/cdmoveset/lang/zh_cn.json": imf_cdmoveset,
        "assets/cdmoveset/lang/vi_vn.json": imf_cdmoveset,
        "assets/p1nero_bow/lang/zh_cn.json": imf_p1nero_bow,
        "assets/p1nero_bow/lang/vi_vn.json": imf_p1nero_bow,
        "assets/level_hp/lang/zh_cn.json": imf_level_hp,
        "assets/level_hp/lang/en_us.json": imf_level_hp,
        "assets/level_hp/lang/vi_vn.json": imf_level_hp,
        "assets/ssamod/lang/zh_cn.json": imf_ssamod,
        "assets/ssamod/lang/vi_vn.json": imf_ssamod,
        "assets/ftbteams/lang/zh_cn.json": imf_ftbteams,
        "assets/ftbteams/lang/vi_vn.json": imf_ftbteams,
        "assets/waystones/lang/zh_cn.json": waystones_vi,
        "assets/waystones/lang/zh_tw.json": waystones_vi,
        "assets/waystones/lang/vi_vn.json": waystones_vi
    }
    update_zip_files(imf_mod_zip, imf_mod_files)

# -------------------------------------------------------------
# 6. WRITE ALL TO IMF-VIETHOA ASSETS DIRECTORY
# -------------------------------------------------------------
all_asset_mods = {
    "fight_more": imf_fight_more,
    "epicfightx": imf_epicfightx,
    "cdmoveset": imf_cdmoveset,
    "p1nero_bow": imf_p1nero_bow,
    "level_hp": imf_level_hp,
    "ssamod": imf_ssamod,
    "ftbteams": imf_ftbteams,
    "waystones": waystones_vi,
    "celepic": celepic_dict,
    "enchanlownew": enchanlownew_dict,
    "lootbags": lootbags_dict,
    "simplyusekey": simplyusekey_dict,
    "womalt": womalt_dict,
    "efn": efn_dict
}

for modid, data in all_asset_mods.items():
    lang_dir = os.path.join(vh_assets, modid, "lang")
    os.makedirs(lang_dir, exist_ok=True)
    vi_p = os.path.join(lang_dir, "vi_vn.json")
    zh_p = os.path.join(lang_dir, "zh_cn.json")
    with open(vi_p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open(zh_p, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Written {modid} to IMF-VietHoa/assets/{modid}/lang/")

# Also mirror celestisynth vi_vn to zh_cn in IMF-VietHoa
cele_vi = os.path.join(vh_assets, "celestisynth", "lang", "vi_vn.json")
cele_zh = os.path.join(vh_assets, "celestisynth", "lang", "zh_cn.json")
if os.path.exists(cele_vi):
    d = json.load(open(cele_vi, 'r', encoding='utf-8'))
    with open(cele_zh, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print("Mirrored celestisynth vi_vn to zh_cn in IMF-VietHoa")

# -------------------------------------------------------------
# 7. CLEAN UP LINGERING CHINESE IN IMF-VIETHOA
# -------------------------------------------------------------
# alexsmobs
alex_vi = os.path.join(vh_assets, "alexsmobs", "lang", "vi_vn.json")
if os.path.exists(alex_vi):
    t = open(alex_vi, 'r', encoding='utf-8').read()
    t = t.replace("咻咻", "Vút vút")
    with open(alex_vi, 'w', encoding='utf-8') as f:
        f.write(t)
    print("Fixed alexsmobs 咻咻")

# born_in_chaos_v1
bic_vi = os.path.join(vh_assets, "born_in_chaos_v1", "lang", "vi_vn.json")
if os.path.exists(bic_vi):
    t = open(bic_vi, 'r', encoding='utf-8').read()
    t = t.replace("\u4e28", " | ")
    with open(bic_vi, 'w', encoding='utf-8') as f:
        f.write(t)
    print("Fixed born_in_chaos_v1 丨")

# valhelsia_structures
val_vi = os.path.join(vh_assets, "valhelsia_structures", "lang", "vi_vn.json")
if os.path.exists(val_vi):
    t = open(val_vi, 'r', encoding='utf-8').read()
    t = t.replace("\u4e28", " | ")
    with open(val_vi, 'w', encoding='utf-8') as f:
        f.write(t)
    print("Fixed valhelsia_structures 丨")

# endermanoverhaul, regions_unexplored, soul_like_armors_reworked, ftbessentials
# If en_us.json exists and has Chinese, replace with vi_vn.json or clean English!
for m in ['endermanoverhaul', 'regions_unexplored', 'soul_like_armors_reworked', 'ftbessentials']:
    en_p = os.path.join(vh_assets, m, "lang", "en_us.json")
    vi_p = os.path.join(vh_assets, m, "lang", "vi_vn.json")
    if os.path.exists(en_p) and os.path.exists(vi_p):
        d_vi = json.load(open(vi_p, 'r', encoding='utf-8'))
        with open(en_p, 'w', encoding='utf-8') as f:
            json.dump(d_vi, f, ensure_ascii=False, indent=2)
        print(f"Replaced {m}/en_us.json with clean content")

print("All resource pack assets patched successfully!")
