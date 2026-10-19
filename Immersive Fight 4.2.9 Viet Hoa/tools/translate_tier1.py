import json
import os

def update_json(filepath, translations):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for k, v in translations.items():
        data[k] = v
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {len(translations)} keys in {os.path.basename(filepath)}")

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\resourcepack\IMF-VietHoa\assets"

# 1. WOM
wom_trans = {
    "itemGroup.wom.items": "Vũ Khí Kỳ Diệu (Weapons of Miracle)",
    "enchantment.wom.invigoration": "Hồi Sinh Lực",
    "enchantment.wom.invigoration.desc": "Mỗi cấp gia tăng 1 điểm Thể lực.",
    "item.wom.agony.tooltip": "Cây trường thương thanh thoát và sắc bén cho phép người sử dụng tung ra những đòn tấn công chí mạng. Đòn tấn công nhảy cho phép phóng cao 2 khối.\n\nTấn công kẻ địch sẽ tích tụ năng lượng cho kỹ năng này, tối đa 3 tầng.\nSát thương cuối cùng sẽ được nhân theo số tầng tích tụ.",
    "skill.wom.agony_plunge": "Thiên Giáng Đột Kích",
    "skill.wom.agony_plunge.tooltip": "“Biến mất giữa tầng không, rồi lao vút xuống kẻ thù.”\n\nTấn công kẻ địch sẽ tích nạp cho kỹ năng này, tối đa 3 tầng.\nSau khi nhảy lên không trung, tiếp tục giữ chuột trái để giáng đòn dập xuống đất (yêu cầu phải có tầng tích nạp). Tiêu hao toàn bộ tầng, sát thương tỷ lệ thuận với số tầng tích tụ.",
    "item.wom.tormented_mind.tooltip": "Binh khí của sự tàn sát và biến dị quy mô lớn.\nLưỡi rìu này hấp thụ toàn bộ cơn thịnh nộ của kẻ nắm giữ trước đó, và truyền ngọn lửa cuồng nộ ấy sang mục tiêu tiếp theo.",
    "skill.wom.true_berserk": "Chân Thịnh Nộ",
    "skill.wom.true_berserk.tooltip": "“Nguyện cho thần linh cũng phải khiếp sợ trước ngươi...”\n\nCơn cuồng nộ bị tra tấn khiến thanh hiển thị kỹ năng trở nên mất kiểm soát.",
    "item.wom.ruine.tooltip": "Cổ khí được rèn đúc bằng bí thuật thất truyền thời cổ đại, dung hợp sức mạnh hư không của Enderman.\nTrọng tâm hoàn mỹ và thiết kế dị biệt mang lại uy lực tột cùng cùng sự chuẩn xác tuyệt đối trong giao chiến.",
    "skill.wom.plunder_perdition": "Đoạt Hồn Vực Sâu",
    "skill.wom.plunder_perdition.tooltip": "“Nắm giữ bí thuật cổ xưa của tộc Enderman.”\n\nKhi kích hoạt, bạn sẽ dịch chuyển tức thời xung quanh mục tiêu, liên tục vung trảm trái và phải.\n  - Khi đang lướt (sprint): nếu đánh trúng, tước đoạt tốc độ di chuyển và tốc độ đánh của mục tiêu.\n  - Khi đang ở trên không: dịch chuyển trên không quanh mục tiêu, tước đoạt tốc độ di chuyển và tốc độ đánh.\n  - Khi cúi người (sneak) và có 10 tầng tích nạp: triệu hồi Cánh Tay Hư Không dưới chân các mục tiêu xung quanh. Đôi tay sẽ túm chặt con mồi, gây sát thương cực lớn kèm hiệu ứng Mệt Mỏi Đào Mỏ và Làm Chậm.",
    "item.wom.satsujin.tooltip": "Thanh kiếm phong ấn ác ma cổ đại.\nCường hóa độ bền và hiệu ứng trảm kích, tuy nhiên vì phong ấn chưa được giải trừ hoàn toàn nên chưa thể phát huy tối đa ma lực...\n\nNội tại: Tự động thu bao kiếm sau 4 giây không hành động. Sau khi tung đòn rút kiếm chém (Iaijutsu), tốc độ thu bao kiếm sẽ nhanh hơn.",
    "skill.wom.sakura_state": "Anh Hoa Kiếm Trảm",
    "skill.wom.sakura_state.tooltip": "“Lưỡi kiếm mỏng manh nhất thi triển giữa sự tĩnh lặng tuyệt đối.”\nKhi lướt tới, bạn lướt xuyên qua kẻ địch phía trước và tung trảm kích chớp nhoáng dọc đường lướt.\n\nCó thể cộng dồn tối đa 8 tầng Anh Hoa Trảm. Cạnh Quét giúp tăng số lượng cộng dồn. Kích hoạt kỹ năng để tiến vào trạng thái Anh Hoa.\nNếu sau 4 giây không tiếp tục tung đòn chém, sẽ mất toàn bộ số tầng và thoát khỏi trạng thái.\nĐòn tấn công khi lướt sẽ cộng dồn 3 tầng Vĩnh Hằng Trảm Lạc lên kẻ địch. Nếu trong 1.5 giây không tấn công, toàn bộ vết chém cộng dồn sẽ đồng loạt bùng nổ sát thương. Đòn lướt đặc biệt tiêu hao 2 tầng. Khi đạt đủ 12 tầng, giữ chuột phải và nhấn phím kỹ năng để tiêu hao 6 tầng tung ra Tuyệt Kỹ Kết Liễu!",
    "item.wom.ender_blaster.tooltip": "Hỏa khí vượt qua cả giới hạn của thời gian và không gian, chỉ tìm kiếm kẻ xứng đáng để thuần hóa uy lực đỉnh cao của nó.",
    "skill.wom.ender_blast": "Oanh Tạc Hư Không"
}
update_json(os.path.join(base_dir, "wom", "lang", "vi_vn.json"), wom_trans)

# 2. SAINTS DRAGONS
saints_trans = {
    "entity.saintsdragons.raevyx": "Raevyx",
    "entity.saintsdragons.ignivorus": "Ignivorus",
    "entity.saintsdragons.cinderwing": "Cinderwing",
    "item.saintsdragons.dragon_caller.tooltip": "Thổi tù và rồng để triệu hồi rồng bay của bạn.",
    "item.saintsdragons.lightning_dragon_scale": "Lightning Dragon Scale",
    "item.saintsdragons.lightning_dragon_scale.tooltip": "Vảy rồng lôi điện cứng cáp rực sáng ánh sét Ma Thuật.",
    "subtitles.entity.saintsdragons.dragon.roar": "Tiếng gầm thét xé trời của Rồng",
    "subtitles.entity.saintsdragons.dragon.breath": "Rồng phun nguyên tố hủy diệt"
}
update_json(os.path.join(base_dir, "saintsdragons", "lang", "vi_vn.json"), saints_trans)

# 3. EFN (EpicFight Nightfall)
efn_trans = {
    "skill.efn.parry": "Đỡ Đòn Hoàn Hảo (Parry)",
    "skill.efn.parry.tooltip": "Chặn đòn đúng thời khắc kẻ thù chạm vào người sẽ làm chệch hướng đòn đánh, làm đối phương choáng váng và tạo sơ hở cho đòn kết liễu tàn khốc.",
    "attribute.name.efn.posture": "Thế Thủ (Posture)",
    "attribute.name.efn.poise": "Kiên Định (Poise)"
}
update_json(os.path.join(base_dir, "efn", "lang", "vi_vn.json"), efn_trans)
