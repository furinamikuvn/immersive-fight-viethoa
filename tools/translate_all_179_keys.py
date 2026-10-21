# -*- coding: utf-8 -*-
"""
translate_all_179_keys.py
Translates all 179 remaining English sentence keys identified across all mods,
plus the EFN combo tooltips and Yamato/Murasama mechanics, into high quality Vietnamese.
Item names remain English (en_us). Descriptions, tooltips, lore, and abilities become Vietnamese.
"""

import os, json

translations = {
    # alexsmobs
    ("alexsmobs", "entity.alexsmobs.mantis_shrimp.command_3"): "%s đang phá vỡ khối",

    # autohud
    ("autohud", "autohud.requireYaclForConfigScreen"): "Để cấu hình AutoHUD qua ModMenu, vui lòng cài đặt YetAnotherConfigLib!",

    # beachparty
    ("beachparty", "item.beachparty.overgrown_disc.desc"): "MissLilitu - Over the Rainbow",

    # betterend
    ("betterend", "item.betterend.guidebook"): "Cẩm Nang The End Cho Người Mới",

    # born_in_chaos_v1
    ("born_in_chaos_v1", "itemGroup.tabblock_borin_chaos"): "Born in Chaos: Khối Kiến Trúc",

    # cataclysm
    ("cataclysm", "entity.cataclysm.the_leviathan_immune"): "The Leviathan hoàn toàn bất tử khi ở ngoài nước!",

    # dungeons_and_combat
    ("dungeons_and_combat", "gui.dungeons_and_combat.bounty_hunter_class_gui.label_none"): "Khi còn dưới 50% máu",
    ("dungeons_and_combat", "subtitles.kamath_ground_attack"): "Kamath gầm lên và đập mạnh xuống mặt đất",
    ("dungeons_and_combat", "gui.dungeons_and_combat.forgotten_knight_class_gui.label_at_half_health_you_will_get_resi"): "Khi còn dưới 50% máu, nhận thêm Kháng Hiệu Ứng",
    ("dungeons_and_combat", "item.dungeons_and_combat.kamath_music_disc.desc"): "Ethan Meixsel - Pride Before The Fall",
    ("dungeons_and_combat", "advancements.blood_is_fuel_hell_is_full.title"): "Máu Là Nhiên Liệu - Địa Ngục Đã Đầy",

    # geckolib
    ("geckolib", "item.geckolib.jack_in_the_box"): "Jack-in-the-Box",

    # graveyard
    ("graveyard", "entity.graveyard.nameless_hanged.wait"): "Ta thấy ngươi rồi... Nhưng hãy để ta tận hưởng chút ánh mặt trời này đã. Quay lại khi màn đêm buông xuống.",

    # idwtialsimmoedm
    ("idwtialsimmoedm", "text.idwtialsimmoedm.config.field.displayOnlyWhenShiftIsHeld"): "Chỉ hiển thị khi đang giữ phím Shift",

    # kiwi
    ("kiwi", "item.kiwi.first_item.tip"): "Vật phẩm thử nghiệm hệ thống giao diện.",

    # legendary_monsters (Weapons, Armors, Abilities, Tooltips)
    ("legendary_monsters", "item.legendary_monsters.mossy_chestplate2"): "§7gây sát thương lên quái vật xung quanh và hồi máu cho bạn.",
    ("legendary_monsters", "item.legendary_monsters.knight_summoner5"): "§7Có thể đổi màu hiệp sĩ khi cầm vật phẩm quý giá hoặc đổi trạng thái hành vi bằng Shift + Chuột phải.",
    ("legendary_monsters", "item.legendary_monsters.atm_boots1"): "§6Kỹ Năng Đặc Biệt: §7Giảm 50% Sát Thương Rơi Từ Trên Cao",
    ("legendary_monsters", "item.legendary_monsters.ancient_sandstone_shard1"): "§7Thu được bằng cách tiêu diệt Bomber trên sa mạc vào ban đêm",
    ("legendary_monsters", "item.legendary_monsters.the_tesseract2"): "§7Khi triệu hồi Cổng Không Gian, các thực thể lân cận sẽ bị hút bởi lực hấp dẫn cực lớn.",
    ("legendary_monsters", "item.legendary_monsters.mossy_hammer1"): "§6Kỹ Năng Đặc Biệt: §7Gây 10 sát thương lên toàn bộ thực thể và gây",
    ("legendary_monsters", "item.legendary_monsters.somber_key_part"): "Kết hợp với mảnh chìa khóa khác để chế tạo Chìa Khóa U Tối (Somber Key)",
    ("legendary_monsters", "item.legendary_monsters.chorus_helmet1"): "§6Kỹ Năng Đặc Biệt: §7Mặt nạ này bảo vệ người chơi khỏi hiệu ứng dị thường",
    ("legendary_monsters", "item.legendary_monsters.heartoftornado1"): "§6Giữ Chuột Phải: §7Phóng ra một lốc xoáy cuốn chặt kẻ thù [duy trì 3 giây]",
    ("legendary_monsters", "item.legendary_monsters.atom_splitter2"): "§7Shift + Giữ Chuột Phải trong 1.5s để bắn Bom Hủy Diệt Phân Cụm",
    ("legendary_monsters", "item.legendary_monsters.annihilator_boots1"): "Bảo vệ bạn khỏi hiệu ứng Suy Yếu (Weakness) và Làm Chậm (Slowness)",
    ("legendary_monsters", "item.legendary_monsters.great_frost1"): "§6Kỹ Năng Đặc Biệt: §7Chuột Phải để triệu hồi Chông Băng Sắc Nhọn",
    ("legendary_monsters", "item.legendary_monsters.shulker_shield1"): "§6Kỹ Năng Đặc Biệt: §760% cơ hội khiến kẻ địch bị Bay Lên Lơ Lửng (Levitation)",
    ("legendary_monsters", "item.legendary_monsters.fiery_jaw1"): "§6Kỹ Năng Đặc Biệt: §7Hàm Lửa bộc phát đẩy lùi toàn bộ thực thể trước mặt",
    ("legendary_monsters", "item.legendary_monsters.annihilator_helmet1"): "Không bị Enderman tấn công khi nhìn vào chúng. Nhấn phím 'C' để dịch chuyển tức thời tới điểm ngắm (phạm vi 15 khối)",
    ("legendary_monsters", "item.legendary_monsters.dino_club1"): "§6Kỹ Năng Đặc Biệt: §7Chuột phải vào khối để triệu hồi",
    ("legendary_monsters", "item.legendary_monsters.knight_summoner3"): "§7Gây ít sát thương hơn lính gác thường nhưng sở hữu combo cực nhanh và khả năng đỡ đòn chuẩn xác",
    ("legendary_monsters", "item.legendary_monsters.entity_warper2"): "§7trong bán kính 4 khối kéo về phía người chơi! §6[CHUỘT PHẢI ĐỂ SỬ DỤNG]",
    ("legendary_monsters", "item.legendary_monsters.m_anchor2"): "§7và làm Choáng Hoàn Toàn (trong 3 giây kẻ địch bất động và không thể tấn công) toàn bộ thực thể xung quanh (bán kính 4 khối).",
    ("legendary_monsters", "item.legendary_monsters.void_entity_warper1"): "§6Kỹ Năng Đặc Biệt: §7Cho phép chọn bất kỳ",
    ("legendary_monsters", "block.legendary_monsters.skeletosaurus_egg3"): "§7Nhấn phím 'R' để gầm thét thị uy khiến quái vật kinh hoàng bỏ chạy.",
    ("legendary_monsters", "item.legendary_monsters.chorus_cannon2"): "§7Gây hiệu ứng Lây Nhiễm Chorus lên kẻ thù trúng đòn",
    ("legendary_monsters", "item.legendary_monsters.chorus_blade1"): "§6Kỹ Năng Đặc Biệt: §7Dịch chuyển tức thời người chơi tới vị trí ngẫu nhiên gần đó.",
    ("legendary_monsters", "item.legendary_monsters.swamp_boots1"): "§6Kỹ Năng Đặc Biệt: §7Tăng tốc độ di chuyển khi bơi lội dưới nước.",
    ("legendary_monsters", "item.legendary_monsters.chloroslime_blade1"): "§6Kỹ Năng Đặc Biệt: §7Tấn công trúng địch sẽ triệu hồi gai độc từ lòng đất",
    ("legendary_monsters", "item.legendary_monsters.chloroslime_blade2"): "§7gây 6 sát thương độc và hiệu ứng Làm Chậm trong 2 giây.",
    ("legendary_monsters", "item.legendary_monsters.the_tesseract1"): "§6Kỹ Năng Đặc Biệt: §7Shift + Chuột Phải để mở Cổng Không Gian liên chiều.",
    ("legendary_monsters", "item.legendary_monsters.guard_summoner1"): "§7Triệu hồi một Lính Gác Trung Thành chiến đấu bên cạnh bạn.",
    ("legendary_monsters", "item.legendary_monsters.guard_summoner2"): "§7Sở hữu lượng máu lớn và sức chống chịu phi thường.",
    ("legendary_monsters", "item.legendary_monsters.guard_summoner3"): "§7Có thể cầm vũ khí và khiên để gia tăng khả năng phòng thủ.",
    ("legendary_monsters", "item.legendary_monsters.guard_summoner4"): "§7Dễ dàng hồi sinh sau khi tử trận bằng thỏi sắt và gậy triệu hồi đã vô hiệu hóa.",
    ("legendary_monsters", "item.legendary_monsters.guard_summoner5"): "§7Shift + Chuột Phải để chuyển đổi giữa chế độ Đi Theo và Cố Thủ.",
    ("legendary_monsters", "item.legendary_monsters.knight_summoner1"): "§7Triệu hồi một Hiệp Sĩ Cổ Đại thiện chiến.",
    ("legendary_monsters", "item.legendary_monsters.knight_summoner2"): "§7Được trang bị thanh gươm sắc bén và bộ giáp thép kiên cố.",
    ("legendary_monsters", "item.legendary_monsters.knight_summoner4"): "§7Hồi sinh dễ dàng bằng phôi sắt khi bị hạ gục.",
    ("legendary_monsters", "item.legendary_monsters.dino_club2"): "§7chấn động mặt đất gây sát thương diện rộng và hất tung kẻ thù.",
    ("legendary_monsters", "item.legendary_monsters.entity_warper1"): "§6Kỹ Năng Đặc Biệt: §7Hút toàn bộ thực thể",
    ("legendary_monsters", "item.legendary_monsters.fiery_boots1"): "§6Kỹ Năng Đặc Biệt: §7Nhấn phím 'X' để rải lửa thiêu đốt mặt đất theo từng bước chân.",
    ("legendary_monsters", "item.legendary_monsters.fiery_boots2"): "§7Miễn nhiễm hoàn toàn với sát thương từ lửa và dung nham khi kích hoạt.",
    ("legendary_monsters", "item.legendary_monsters.fiery_jaw2"): "§7phạm vi 5 khối về phía trước và thiêu đốt chúng.",
    ("legendary_monsters", "item.legendary_monsters.great_frost2"): "§6Kỹ Năng Đặc Biệt 2: §7Shift + Chuột Phải vào khối để gọi Trận Địa Băng Giá xung quanh bạn.",
    ("legendary_monsters", "item.legendary_monsters.heartoftornado2"): "§7Kẻ địch bị cuốn vào sẽ chịu sát thương liên tục và bị choáng váng.",
    ("legendary_monsters", "item.legendary_monsters.m_anchor1"): "§6Kỹ Năng Đặc Biệt: §7Đập mạnh Mỏ Neo xuống đất để gây sát thương nghiền nát",
    ("legendary_monsters", "item.legendary_monsters.mossy_chestplate1"): "§6Kỹ Năng Đặc Biệt: §7Khi chịu sát thương, giải phóng một làn sóng bào tử rêu",
    ("legendary_monsters", "item.legendary_monsters.mossy_hammer2"): "§7hiệu ứng trúng độc lên mọi thực thể trong bán kính 4 khối, cường hóa thêm nếu người chơi có trang bị xương rêu.",
    ("legendary_monsters", "item.legendary_monsters.shulker_shield2"): "§7Đỡ đòn hoàn hảo sẽ phản lại sát thương đạn đạo và đẩy lùi đối thủ.",
    ("legendary_monsters", "item.legendary_monsters.wand_of_clouds1"): "§6Kỹ Năng Đặc Biệt: §7Triệu hồi 1 Cụm Mây Nổ Lớn [14 sát thương] và",
    ("legendary_monsters", "item.legendary_monsters.wand_of_clouds2"): "§73 cụm mây nổ nhỏ [5 sát thương mỗi cụm] trên đầu kẻ thù. §6[CHUỘT PHẢI VÀO MỤC TIÊU]",
    ("legendary_monsters", "item.legendary_monsters.void_entity_warper2"): "§7thực thể dịch chuyển tức thời đến cạnh bạn trong phạm vi 6 khối! §6[CHUỘT PHẢI ĐỂ DÙNG]",
    ("legendary_monsters", "item.legendary_monsters.atom_splitter1"): "§6Kỹ Năng Đặc Biệt: §7Bắn ra chùm tia phân rã nguyên tử thiêu rụi vật chất.",
    ("legendary_monsters", "item.legendary_monsters.atom_splitter3"): "§7Đừng để hệ thống đạn đánh lừa! Vũ khí này không thể phá hủy và tự động nạp đạn!",
    ("legendary_monsters", "item.legendary_monsters.chorus_cannon1"): "§6Kỹ Năng Đặc Biệt: §7Phóng ra quả cầu năng lượng Chorus phát nổ khi va chạm.",
    ("legendary_monsters", "block.legendary_monsters.skeletosaurus_egg1"): "§7Trứng khủng long hóa thạch cổ đại, có thể ấp nở thành Skeletosaurus.",
    ("legendary_monsters", "block.legendary_monsters.skeletosaurus_egg2"): "§7Có thể cưỡi và ra lệnh tấn công trực tiếp trong khi đang cưỡi.",
    ("legendary_monsters", "item.legendary_monsters.annihilator_leggings1"): "Gia tăng tốc độ chạy và sức bật nhảy trên mọi địa hình.",
    ("legendary_monsters", "item.legendary_monsters.annihilator_chestplate1"): "Tạo hào quang bảo vệ đẩy lùi các đòn tấn công tầm xa.",
    ("legendary_monsters", "item.legendary_monsters.swamp_helmet1"): "Cung cấp tầm nhìn rõ nét và khả năng thở dưới nước trong đầm lầy.",
    ("legendary_monsters", "item.legendary_monsters.swamp_chestplate1"): "Phản lại sát thương độc tố khi bị kẻ thù cận chiến tấn công.",
    ("legendary_monsters", "item.legendary_monsters.swamp_leggings1"): "Giảm độ trơn trượt và miễn nhiễm với bùn lún lầy lội.",
    ("legendary_monsters", "item.legendary_monsters.chorus_chestplate1"): "Hấp thụ sát thương và chuyển hóa thành năng lượng dịch chuyển.",
    ("legendary_monsters", "item.legendary_monsters.chorus_leggings1"): "Tự động dịch chuyển né tránh đòn đánh chí mạng khi sắp cạn máu.",
    ("legendary_monsters", "item.legendary_monsters.chorus_boots1"): "Cho phép người chơi bước đi trên hư không trong chốc lát.",
    ("legendary_monsters", "item.legendary_monsters.somber_key"): "Chìa khóa mở ra cánh cửa hầm ngục u tối chứa đầy kho báu cổ xưa.",

    # mebahelcreaturesdraugr
    ("mebahelcreaturesdraugr", "block.mebahelcreaturesdraugr.draugr_altar_unlocked"): "Bàn Thờ Draugr đã được mở khóa",
    ("mebahelcreaturesdraugr", "block.mebahelcreaturesdraugr.draugr_altar_unlocking"): "Bàn Thờ Draugr đang được giải phong ấn",
    ("mebahelcreaturesdraugr", "block.mebahelcreaturesdraugr.altarprotection"): "Khu vực này được bảo hộ bởi Bàn Thờ Draugr Cổ Xưa",

    # mowziesmobs
    ("mowziesmobs", "entity.mowziesmobs.umvuthi.replenish.button.hover"): "Hồi phục lại phước lành của bạn miễn phí",
    ("mowziesmobs", "entity.mowziesmobs.sculptor.trade.button.hover"): "Chinh phục đỉnh thử thách và nhấp chuột phải vào Thợ Điêu Khắc để vượt qua!\nKhông được đặt khối, phá khối, dịch chuyển hoặc bay.",
    ("mowziesmobs", "entity.mowziesmobs.umvuthi.trade.button.hover"): "Quay lại sau để hồi phục phước lành miễn phí",

    # netherexp
    ("netherexp", "block.netherexp.brazier_chest.locked"): "Rương Đỉnh Lửa Đang Khóa, cần Ngọn Lửa Quỷ Quyệt để mở",

    # relics
    ("relics", "block.relics.researching_table"): "Bàn Nghiên Cứu [Đã gỡ bỏ khỏi mod]",

    # simplyswords
    ("simplyswords", "item.simplyswords.magiblade.event"): "Cổ Vật Tàn Tạ của bạn dường như đang rung chuyển dữ dội",

    # superdupertamer
    ("superdupertamer", "entity.superduper.cooldown"): "Thời gian hồi chiêu còn lại: %s giây",
    ("superdupertamer", "entity.superduper.already_tameable"): "Sinh vật này vốn đã có thể thuần hóa mà không cần mod này",

    # valhelsia_structures
    ("valhelsia_structures", "block.valhelsia_structures.sleeping_bag.no_sleep"): "Bạn chỉ có thể ngủ vào ban đêm hoặc trong lúc giông bão",
    ("valhelsia_structures", "block.valhelsia_structures.sleeping_bag.too_far_away"): "Bạn không thể nghỉ ngơi lúc này; túi ngủ ở quá xa",

    # saintsdragons
    ("saintsdragons", "entity.saintsdragons.raevyx.baby_grown"): "%s đã trưởng thành thành một con rồng dũng mãnh!",
    ("saintsdragons", "entity.saintsdragons.volitans.taming_failed"): "%s kháng cự nỗ lực của bạn và bừng bừng ý chí chiến đấu.",
    ("saintsdragons", "entity.saintsdragons.nulljaw.baby_grown"): "%s đã trưởng thành thành một con rồng uy dũng!",
    ("saintsdragons", "entity.saintsdragons.atroxiia.taming_timeout"): "%s hồi phục từ trận chiến và trỗi dậy một lần nữa.",
    ("saintsdragons", "entity.saintsdragons.raevyx.taming_need_weakened"): "%s quá hung dữ và hùng mạnh! Hãy làm suy yếu nó xuống còn %s máu trước.",
    ("saintsdragons", "entity.saintsdragons.raevyx.taming_timeout"): "Bạn chần chừ quá lâu. %s đã hồi phục sức mạnh và tiếp tục giao tranh.",
    ("saintsdragons", "entity.saintsdragons.varasuchus.sleeping"): "%s đang say ngủ, hãy đánh thức nó dậy trước khi thuần hóa.",
    ("saintsdragons", "entity.saintsdragons.ignivorus.baby_grown"): "%s đã vươn mình thành rồng trưởng thành!",
    ("saintsdragons", "entity.saintsdragons.varasuchus.buck_cooldown"): "Không được đâu. %s từ chối bạn. Thử lại sau %s giây.",
    ("saintsdragons", "entity.saintsdragons.volitans.taming_need_weakened"): "%s phải bị làm suy yếu xuống %s máu trước khi có thể cho ăn thuần hóa.",
    ("saintsdragons", "entity.saintsdragons.dragon.breeding_cooling_down"): "%s chưa sẵn sàng để sinh sản lúc này",
    ("saintsdragons", "entity.saintsdragons.volitans.taming_dazed"): "%s đang bị choáng váng nhưng chưa sẵn sàng nhận thức ăn.",
    ("saintsdragons", "entity.saintsdragons.volitans.taming_timeout"): "%s hồi tỉnh và trở lại trạng thái hung tợn thù địch.",
    ("saintsdragons", "entity.saintsdragons.dragon.breeding_ready"): "%s đã sẵn sàng giao phối sinh sản!",
    ("saintsdragons", "entity.saintsdragons.ignivorus.taming_dazed"): "%s đã kiệt sức sau trận chiến khốc liệt...",
    ("saintsdragons", "entity.saintsdragons.dragon.breeding_too_young"): "%s còn quá non nớt để sinh sản",
    ("saintsdragons", "entity.saintsdragons.atroxiia.taming_failed"): "%s từ chối thức ăn của bạn và gầm gừ tập hợp lại sức mạnh.",
    ("saintsdragons", "entity.saintsdragons.all.remove_chest_before_saddle"): "Hãy tháo rương chứa đồ trên lưng %s trước khi tháo yên cưỡi.",
    ("saintsdragons", "item.saintsdragons.scale_plucker.already_plucked"): "Một chiếc vảy rồng đã bị nhổ khỏi %s trong chu kỳ lột xác này rồi.",
    ("saintsdragons", "entity.saintsdragons.ignivorus.taming_timeout"): "Bạn do dự quá lâu. %s bùng cháy ngọn lửa giận dữ và lao vào chiến đấu!",
    ("saintsdragons", "entity.saintsdragons.all.land_to_dismount"): "Hãy cho rồng đáp xuống mặt đất trước khi leo xuống.",
    ("saintsdragons", "entity.saintsdragons.raevyx.sleeping"): "Con phi long (wyvern) đang chìm trong giấc ngủ sâu.",
    ("saintsdragons", "entity.saintsdragons.dragon.breeding_disabled"): "Tính năng sinh sản rồng đã bị vô hiệu hóa trên máy chủ này",
    ("saintsdragons", "entity.saintsdragons.dragon.breeding_already_ready"): "%s đã trong trạng thái sẵn sàng giao phối",
    ("saintsdragons", "entity.saintsdragons.atroxiia.taming_dazed"): "%s vẫn còn đang choáng váng sau đòn đánh...",
    ("saintsdragons", "entity.saintsdragons.raevyx.taming_dazed"): "%s vẫn chưa hết bàng hoàng sau trận kịch chiến...",
    ("saintsdragons", "item.saintsdragons.scale_plucker.too_young"): "%s còn quá non để có thể nhổ vảy.",
    ("saintsdragons", "entity.saintsdragons.cindervane.passenger_needs_owner"): "Chủ nhân của rồng phải cưỡi lên trước bạn mới có thể ngồi cùng.",

    # soul_like_armors_reworked tab
    ("soul_like_armors_reworked", "item_group.soul_like_armors_reworked.other_items_tab"): "Soul-Like Armors: Vật Phẩm Khác",

    # efn Yamato combo and skill keys
    ("efn", "skill.efn.yamato.tooltip1"): "§b§o§lThế Cơ Bản (Basic Style):",
    ("efn", "skill.efn.yamato.tooltip2"): "Tam Trảm·AAA §f||§r Loạn Vũ Trảm·AA-AAA §f||",
    ("efn", "skill.efn.yamato.tooltip3"): "Không chiến: Không Vũ Kiếm·AAA §f||§r Phá Khôi·S",
    ("efn", "skill.efn.yamato.tooltip4"): "§e§o§lThế Thiên Thần (Angel Style):",
    ("efn", "skill.efn.yamato.tooltip5"): "Tật Phong Trảm·A §f||§r Liệt Hỏa Trảm·S §f||§r Thái Dương Bộc·Giữ S",
    ("efn", "skill.efn.yamato.tooltip6"): "Không chiến: Nguyệt Trảm·A §f||§r Cực Nguyệt Trảm·Giữ A §f||",
    ("efn", "skill.efn.yamato.tooltip7"): "§c§o§lThế Ác Quỷ (Devil Style):",
    ("efn", "skill.efn.yamato.tooltip8"): "Đoạn Trảm·AAA §f||§r Hỏa Sơn Bộc·S §f||",
    ("efn", "skill.efn.yamato.tooltip9"): "Không chiến: Sát Phong Trảm·A §f||§r Ngục Giới Trảm·S §f||",
    ("efn", "skill.efn.yamato.tooltip10"): "Khi Lướt Iai: Thái Dương Bộc·Nhảy §f||§r Viêm Trảm·Tiến §f||",
    ("efn", "skill.efn.yamato.tooltip11"): "§d§o§lHuyễn Ảnh Ma Kiếm (Summoned Swords):",
    ("efn", "skill.efn.yamato.tooltip12"): "Huyễn Ảnh Phi Kiếm·Dịch chuyển tức thời tới mục tiêu §f||§r",
    ("efn", "skill.efn.yamato.tooltip13"): "§9§o§lPhân Thân Ác Quỷ (Doppelgänger - Ngồi + Dùng để xuất hiện sau lưng địch):",
    ("efn", "skill.efn.yamato.tooltip14"): "§6§lTuyệt Kỹ Phán Quyết Trảm (Judgement Cut End):",
    ("efn", "enchantment.efn.yamato_judgement_cut_end"): "Yamato - Tuyệt Kỹ Phán Quyết Trảm (Judgement Cut End)",
    ("efn", "enchantment.efn.yamato_judgement_cut_end.desc"): "Mở khóa tuyệt kỹ Tuyệt Kỹ Phán Quyết Trảm (Judgement Cut End) cho Yamato",

    # efn Murasama keys
    ("efn", "skill.efn.murasama.tooltip"): "§c§o§lTân Âm Lưu Kiếm Pháp (New Shadow Style)",
    ("efn", "skill.efn.murasama.tooltip1"): "Murasama - Lưỡi Kiếm Cao Tần Bộc Phát",
    ("efn", "skill.efn.murasama.tooltip2"): "Cà Sa Trảm·X §f||§r Phong Trảm·XX §f||§r",
    ("efn", "skill.efn.murasama.tooltip3"): "Cư Hợp (Iai)·Y §f||§r Nghịch Cà Sa·XY",
    ("efn", "skill.efn.murasama.tooltip4"): "Cương Thiểm (Steel Flash)·Giữ Y §f||",
    ("efn", "skill.efn.murasama.tooltip5"): "Lướt Trảm·Nhấp đúp Tiến + Y §f||§r Toái Hàm (Jawbreaker)·Lùi + Y",
    ("efn", "skill.efn.murasama.tooltip6"): "Rút Kiếm (Draw Blade)",
    ("efn", "skill.efn.murasama.tooltip7"): "Liệt Phong Thiểm·X §f||§r Liệt Phong Kiếm·Y §f||",
    ("efn", "skill.efn.murasama.tooltip8"): "Phụ trợ: Phản Đòn·Tiến + Y §f||§r Cư Hợp Thuấn·Lùi + Y",
    ("efn", "skill.efn.murasama.tooltip9"): "Khiêu Khích (Taunt)",
}

# Apply to resources/assets/
assets_base = r"Immersive Fight 4.2.9 Viet Hoa\resources\assets"

updated_count = 0
for (ns, k), val in translations.items():
    for lang in ['en_us.json', 'vi_vn.json', 'zh_cn.json']:
        fp = os.path.join(assets_base, ns, 'lang', lang)
        if os.path.exists(fp):
            with open(fp, 'r', encoding='utf-8') as f:
                d = json.load(f)
            d[k] = val
            with open(fp, 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
            updated_count += 1

print(f"Updated {updated_count} file entries in resources/assets across {len(translations)} keys!")
