import os
import json
import zipfile

base_rp = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\resourcepack\IMF-VietHoa\assets"

def update_json(filepath, updates):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    for k, v in updates.items():
        data[k] = v
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {filepath} with {len(updates)} keys.")

# 1. Fix EFN
efn_updates = {
    "item.efn.meen_spear.description1": "Toàn bộ thân súng được chế tác từ hợp kim Netherite. Thân thương hỏa khí cực nặng khiến người cầm khó có thể thi triển các chiêu thức thương thuật thông thường."
}
for lang in ["vi_vn.json", "zh_cn.json", "en_us.json"]:
    update_json(os.path.join(base_rp, "efn", "lang", lang), efn_updates)

# 2. Fix Celestisynth
celestisynth_updates = {
    "item.celestisynth.solar_crystal_armor_bonus": "Khi chịu sát thương, giáp phóng ra một vòng lửa bùng nổ, gây sát thương và thiêu đốt các mục tiêu xung quanh. Mỗi mảnh giáp tăng sát thương nổ và thời gian bốc cháy.",
    "item.celestisynth.lunar_stone_armor_bonus": "Khi người mặc bị thương, giáp có 1/5 tỉ lệ giảm đáng kể lượng sát thương nhận vào. Mỗi mảnh giáp gia tăng chỉ số giảm sát thương.",
    "item.celestisynth.solaris.passive_desc_1": "Người cầm được miễn nhiễm sát thương lửa - đòn tấn công thông thường với vũ khí này sẽ thiêu đốt mục tiêu trong vài giây.",
    "item.celestisynth.solaris.passive_desc_2": "Khi nhấn giữ chuột phải với Solaris, người chơi có thể triệu hồi tối đa 5 quả cầu lửa mặt trời bay quanh bản thân. Tấn công kẻ địch sẽ phóng cầu lửa lao về phía chúng.",
    "item.celestisynth.solaris.condition_2": "Kích hoạt: Chuột phải khi đang giữ SHIFT",
    "item.celestisynth.crescentia.passive_desc_1": "Người cầm nhận thêm một tầng Kháng Sát Thương - đòn tấn công thông thường với vũ khí này sẽ làm chậm mục tiêu trong vài giây.",
    "item.celestisynth.crescentia.condition_2": "Kích hoạt: Chuột phải khi đang giữ SHIFT",
    "item.celestisynth.breezebreaker.passive_desc_1": "Người cầm được tăng mạnh độ cao nhảy và miễn nhiễm sát thương rơi, nhưng chịu 2.3x sát thương từ mọi nguồn khác.",
    "item.celestisynth.breezebreaker.passive_desc_2": "Mỗi 15 lần thi triển kỹ năng sẽ bật/tắt nội tại này. Khi kích hoạt, người chơi được tăng tốc chạy và giảm 50% thời gian hồi chiêu kỹ năng. Hiệu ứng kết thúc sau 8 giây.",
    "item.celestisynth.breezebreaker.condition_3": "Kích hoạt: Chuột phải khi đang giữ SHIFT",
    "item.celestisynth.poltergeist.passive_desc_1": "Mọi kỹ năng của vũ khí này khắc Dấu Ấn Hồn Ma lên mục tiêu trúng đòn. Kẻ địch bị hạ gục mang dấu ấn sẽ biến thành Quái Dị Thể, hút các thực thể xung quanh lại trong 5 giây.",
    "item.celestisynth.poltergeist.condition_2": "Kích hoạt: Chuột phải khi đang giữ SHIFT",
    "item.celestisynth.aquaflora.passive_desc_1": "Mỗi lần tung kỹ năng tăng 3 giây tốc độ di chuyển cho người dùng.",
    "item.celestisynth.aquaflora.condition_2": "Kích hoạt: Chuột phải khi đang giữ SHIFT",
    "item.celestisynth.aquaflora.condition_4": "Kích hoạt: Chuột phải khi đang giữ SHIFT trong Trạng Thái Nở Rộ",
    "item.celestisynth.rainfall_serenity.condition_3": "Kích hoạt: Chuột phải khi đang giữ SHIFT",
    "item.celestisynth.frostbound.passive_desc_1": "Gây sát thương lên mục tiêu bằng vũ khí này sẽ áp dụng trạng thái Băng Giá, làm chậm và tích lũy Mảnh Băng.",
    "item.celestisynth.frostbound.passive_desc_2": "Khi nhấn giữ chuột phải với Frostbound, vũ khí tiêu hao Mảnh Băng và phóng chúng về phía các mục tiêu ngẫu nhiên xung quanh, đóng băng chúng trong vài giây.",
    "item.celestisynth.frostbound.condition_2": "Kích hoạt: Chuột phải khi đang giữ SHIFT",
    "item.celestisynth.keres.passive_desc_1": "Sau khi tấn công trúng mục tiêu liên tiếp 5 lần, người cầm kích hoạt Trạng Thái Huyết Nộ.",
    "item.celestisynth.keres.passive_desc_2": "Khi sử dụng Keres để tung kỹ năng, người cầm hiến tế 1.5 máu mỗi vài giây, nhưng mỗi kỹ năng đánh trúng mục tiêu sẽ hồi lại một lượng máu nhất định.",
    "item.celestisynth.keres.passive_desc_3": "Khi kỹ năng đánh trúng mục tiêu, gây hiệu ứng Phá Nguyền lên mục tiêu trong 5 giây, làm giảm mạnh khả năng hồi phục của chúng.",
    "item.celestisynth.keres.condition_2": "Kích hoạt: Chuột phải khi đang giữ SHIFT"
}
for lang in ["vi_vn.json", "zh_cn.json", "en_us.json"]:
    update_json(os.path.join(base_rp, "celestisynth", "lang", lang), celestisynth_updates)

# 3. Fix Arsenal
arsenal_updates = {
    "item.arsenal.charge_halberd2_desc": "Khi điện tích từ 15 điểm trở lên, sử dụng vũ khí khi đang ngồi xổm sẽ biến đổi thành kích."
}
for lang in ["vi_vn.json", "zh_cn.json", "en_us.json"]:
    update_json(os.path.join(base_rp, "arsenal", "lang", lang), arsenal_updates)

# 4. Fix Dungeons and Combat
dungeons_updates = {
    "advancements.the_forgotten_knight.descr": "Thế giới đã lãng quên bạn, và sứ mệnh của bạn là báo thù",
    "advancements.the_forgotten_knight.title": "Hiệp Sĩ Bị Lãng Quên",
    "advancements.the_new_god_of_the_sun.descr": "Trang bị đầy đủ bộ giáp Vàng Ban Phước vào ban ngày",
    "advancements.the_new_god_of_the_sun.title": "Thần Mặt Trời Mới",
    "advancements.the_bloody_cult.descr": "Tìm kiếm kiến trúc của những kẻ tôn sùng Huyết Thần",
    "advancements.the_bloody_cult.title": "Tà Giáo Huyết Tộc",
    "advancements.born_of_blood.descr": "Triệu hồi một dân làng bằng Máu trong Chén Thánh",
    "advancements.born_of_blood.title": "Huyết Sinh",
    "advancements.old_friends.descr": "Tiếp thêm năng lượng cho ánh sáng Sunleia bằng Bọ Ban Phước",
    "advancements.hiddeninthe_cult.title": "Ẩn Mình Trong Bóng Tối",
    "advancements.catacumbs_lugubrious.descr": "Đối mặt với kẻ thù đầu tiên trong Hầm Mộ U Ám",
    "advancements.the_man_of_steel.descr": "Chế tạo một bộ giáp hoàn chỉnh từ thép",
    "advancements.the_man_of_steel.title": "Người Thép",
    "advancements.a_infernal_fortress.descr": "Tiến vào Pháo Đài Rực Lửa và đối mặt với thực thể Lửa",
    "advancements.the_bloodymancer.descr": "Đoạt lấy Viên Ngọc Máu",
    "advancements.the_bloodymancer.title": "Huyết Thuật Sư",
    "advancements.witch.descr": "Dùng Cào Sắt để tấn công Phù Thủy",
    "advancements.blood_is_fuel_hell_is_full.descr": "Hiến tế máu cho Giáp Huyết Sắc",
    "advancements.the_bounty_hunter.title": "Thợ Săn Tiền Thưởng",
    "advancements.the_rogue.title": "Kẻ Đạo Tặc",
    "advancements.the_rogue.descr": "Bạn là kẻ dối trá bị truy nã gắt gao nhất",
    "advancements.the_exiled.descr": "Cảm giác tội lỗi gặm nhấm tâm hồn",
    "advancements.the_exiled.title": "Kẻ Lưu Đày",
    "advancements.dungeons_and_combat.descr": "Các hầm ngục đang chờ đón bạn bước vào",
    "advancements.forgotten_sands.descr": "Chiến đấu với Quái Vật ở Vùng Cát Lãng Quên",
    "advancements.let_the_ceremony_begin.descr": "Đoạt lấy Dao Găm Nghi Lễ",
    "advancements.let_the_ceremony_begin.title": "Nghi Lễ Bắt Đầu",
    "advancements.the_new_gravedigger.descr": "Sử dụng Gravedigger để triệu hồi Kẻ Tay Trắng",
    "advancements.the_new_gravedigger.title": "Kẻ Đào Mộ Mới"
}
for lang in ["vi_vn.json", "zh_cn.json", "en_us.json"]:
    update_json(os.path.join(base_rp, "dungeons_and_combat", "lang", lang), dungeons_updates)

# 5. Fix Fight More weapon names
fight_more_updates = {
    "item.fight_more.agony_p": "Agony",
    "item.fight_more.ruine_p": "Ruine",
    "item.fight_more.satsujin_p": "Satsujin",
    "item.fight_more.solar_p": "Solar",
    "item.fight_more.antitheus_p": "Antitheus",
    "item.fight_more.ender_blaster_p": "Ender Blaster",
    "item.fight_more.moonless_p": "Moonless",
    "item.fight_more.gesetz_p": "Gesetz",
    "item.fight_more.herrscher_p": "Herrscher",
    "item.fight_more.torment_p": "Torment"
}
for lang in ["vi_vn.json", "zh_cn.json", "en_us.json"]:
    update_json(os.path.join(base_rp, "fight_more", "lang", lang), fight_more_updates)

print("Translation updates complete!")
