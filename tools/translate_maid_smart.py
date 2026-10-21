# -*- coding: utf-8 -*-
"""
translate_maid_smart.py
Translates all 57 remaining maid_smart config and tooltip keys into Vietnamese.
"""

import os, json

maid_translations = {
    "config.promaid.accessory.daYunSmashDamage": "Sát thương nghiền nát Đại Vận theo tốc độ",
    "config.promaid.perception.lookTicks": "Thời gian duy trì ánh nhìn của chủ nhân (giây)",
    "config.promaid.misc.presetMode": "Chế độ cấu hình sẵn (chuyển đổi trên trang sổ tay)",
    "config.promaid.airRaid.minAboveHeight": "Độ cao tối thiểu phía trên mục tiêu (khối)",
    "config.promaid.ride.bombStandoff": "Độ cao duy trì ném bom (khối phía trên mục tiêu)",
    "config.promaid.combat.soulSpellEnable": "Tự động kích hoạt phép linh hồn khi chịu sát thương chí mạng",
    "config.promaid.combat.flightNoFallDamage": "Không Kích: Miễn nhiễm hoàn toàn sát thương rơi",
    "config.promaid.bombing.tntRange": "Bán kính mục tiêu thả TNT (khối)",
    "config.promaid.accessory.daYun.smashDamage": "Sát thương nghiền nát Đại Vận theo tốc độ",
    "config.promaid.mine.hardBlockReport": "Hủy báo cáo mục tiêu khi gặp khối quá cứng",
    "config.promaid.airSeparation": "Không Kích: Chống chồng lấn đội hình trên không",
    "config.promaid.dialogue.proactiveEventCd": "Thời gian hồi chiêu đối thoại chủ động (giây)",
    "config.promaid.bridge.buildOnlyNatural": "Khối Xây Dựng: Chỉ dùng các khối tự nhiên Vanilla",
    "config.promaid.bombing.tntSpeed": "Tốc độ ném (khối/tick)",
    "config.promaid.airSeparationRadius": "Không Kích: Bán kính giãn cách đội hình (khối)",
    "config.promaid.misc.workSpeedLevel0": "Giới hạn tốc độ di chuyển về mức cơ bản khi đang làm việc",
    "config.promaid.ride.servantTransfer": "Thú cưỡi người hầu: Chuyển sát thương sang thú cưỡi",
    "key.promaid.goety_toggle": "Bật/Tắt chế độ tự động bay Goety của Hầu Gái (ngắm vào hầu gái)",
    "config.promaid.perception.eventCooldown": "Thời gian hồi chiêu thông báo sự kiện (giây)",
    "config.promaid.combat.playerDamageMode": "Chế độ sát thương từ người chơi lên hầu gái",
    "config.promaid.misc.maidTeleportRebuild": "Tái tạo thực thể máy khách sau dịch chuyển (sửa lỗi vô hình khi dịch chuyển xa)",
    "config.promaid.combat.playerDamageMaidCap": "Tỷ lệ giới hạn sát thương tối đa của người chơi",
    "config.promaid.bridge.minRadius": "Bán kính hình cầu tối thiểu xây cầu (khối)",
    "config.promaid.bridge.reclaimToMaid": "Thu hồi khối giàn giáo vào túi đồ hầu gái",
    "config.promaid.misc.strollRadius": "Bán kính đi dạo tự do (khối)",
    "config.promaid.broom.minStandoff": "Khoảng cách tối thiểu tới mục tiêu khi cưỡi chổi (khối)",
    "config.promaid.patrol.clearance": "Tuần Tra - Bán kính dọn dẹp mặc định (khối)",
    "config.promaid.combat.snipe": "Bắn Tỉa Trên Cao (Mặc định Bật): Khi ở trạng thái tấn công tầm xa + có khối xây dựng + địch áp sát — lập tức dựng tháp cao 5 khối và cố thủ tấn công từ trên cao.",
    "config.promaid.combat.spellGearIgnore": "Danh Sách Trang Bị Phép Bị Bỏ Qua (Mặc định: SlashBlade, YoukaisHomecoming)",
    "config.promaid.combat.flightDashBoostRespectCooldown": "Phép Lướt Nhanh: Tuân thủ thời gian hồi chiêu phép",
    "item.maid_smart.da_yun.desc2": "§7Các khối có độ cứng §f≥ obsidian (50)§7 hoặc §f< 0§7 (đá nền/barrier/command block...) sẽ không bao giờ bị tác động",
    "config.promaid.combat.tacticsOrbitRadius": "Bán kính quỹ đạo chiến thuật (khối)",
    "config.promaid.patrol.maxRadius": "Tuần Tra - Bán kính ngang tối đa (khối)",
    "config.promaid.ride.batonExclusive": "Gậy Điều Khiển Cưỡi - Chuột phải độc quyền",
    "config.promaid.combat.vanillaYieldToMod": "Ưu Tiên Nhiệm Vụ Mod: Khi có nhiệm vụ mod độc quyền, nhiệm vụ cơ bản vanilla sẽ tạm nhường quyền hoàn toàn",
    "config.promaid.bridge.threatDist": "Bán kính mối đe dọa xây cầu (khối)",
    "config.promaid.combat.autoSwitchRestoreThreatDist": "Bán kính khôi phục mối đe dọa (khối)",
    "config.promaid.broom.clampHome": "Tuần tra khu vực làm việc trong chế độ cố thủ nhà",
    "config.promaid.airRaid.orbitMax": "Khoảng cách quỹ đạo tối đa sau khi khóa mục tiêu (khối)",
    "config.promaid.spawnerTorch.radius": "Bán kính tìm kiếm lồng quái đặt đuốc (khối)",
    "config.promaid.tether.broomExtra": "Dây Cương Chiến Đấu - Độ trũng bổ sung khi cưỡi chổi (khối)",
    "key.promaid.free_flight_toggle": "Bật/Tắt chế độ bay tự do của Hầu Gái (ngắm vào hầu gái)",
    "config.promaid.combat.snipeHeight": "Chiều cao tháp bắn tỉa (khối, mặc định 5 khối)",
    "config.promaid.broom.orbitMax": "Khoảng cách tối đa tới mục tiêu khi cưỡi chổi (khối)",
    "config.promaid.build.originPlayer": "Vị trí xây dựng = Dưới chân người chơi",
    "config.promaid.ride.orbitRadius": "Bán kính quỹ đạo cưỡi (khối)",
    "config.promaid.combat.forceAllSchedule": "Buộc chuyển lịch trình sang TẤT CẢ khi bước vào giao tranh",
    "config.promaid.combat.teleportSafeRadius": "Bán kính an toàn khi dịch chuyển tức thời (khối)",
    "config.promaid.combat.autoSwitchAllowModTasks": "Tự Động Đổi Nhiệm Vụ Mod: Hầu gái chỉ kích hoạt nhiệm vụ mod khi cầm trang bị của mod tương ứng",
    "config.promaid.mine.noTargetPause": "Thời gian nghỉ khi không có mục tiêu khai thác (giây)",
    "config.promaid.voice.systemCooldownS": "Hồi chiêu giọng đọc hệ thống (giây)",
    "config.promaid.combat.autoSwitchRadius": "Bán kính phản ứng chiến đấu (khối)",
    "config.promaid.combat.soulSpellCooldownSeconds": "Hồi chiêu phép thuật linh hồn (giây)",
    "config.promaid.combat.soulSpellOwnerRadius": "Bán kính bảo vệ chủ nhân bằng phép linh hồn (khối)",
    "config.promaid.perception.hostileShowCooldown": "Hồi chiêu hiển thị cảnh báo kẻ địch (giây)",
    "config.promaid.tether.pull": "Dây Cương Chiến Đấu - Kéo dắt hầu gái như dây dắt vanilla",
    "config.promaid.combat.flightDashBoost": "Phép Lướt Tốc Độ Trong Khi Đang Bay",
}

assets_base = r"Immersive Fight 4.2.9 Viet Hoa\resources\assets\maid_smart\lang"
for lang in ['en_us.json', 'vi_vn.json', 'zh_cn.json']:
    fp = os.path.join(assets_base, lang)
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8') as f:
            d = json.load(f)
        d.update(maid_translations)
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)

print(f"Applied {len(maid_translations)} maid_smart keys across all lang files!")
