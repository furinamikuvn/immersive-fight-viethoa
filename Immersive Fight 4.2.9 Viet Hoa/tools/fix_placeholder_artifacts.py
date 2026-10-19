import os
import json

base = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\resourcepack\IMF-VietHoa\assets"

clean_replacements = {
    'efn': {
        'item.efn.kusabimaru.description1': "§f§i§lBảo đao truyền thế của Thần Tử Long Dận;\n§7§lCái tên 'Kusabimaru' chứa đựng tâm nguyện—ngay cả khi nhẫn giả mang số mệnh sát sinh, cũng quyết không thể vứt bỏ chút lòng từ bi cuối cùng...",
        'advancement.efn.obtain_mortal_blade.description': "§c§lĐại Thái Đao trảm sát kẻ bất tử: Lưỡi đao đỏ rực đoạt mạng kẻ rút kiếm, nếu không có năng lực khởi tử hồi sinh thì không thể làm chủ Bất Tử Trảm\n——Vung đòn chém thanh kiếm bất khả xuất bao, chiêu thức chỉ thị tùng của Thần Tử Long Dận mới có thể thi triển."
    },
    'sword_soaring': {
        'skill.sword_soaring.vatansever.tooltip4': "§7Kiếm hợp tam nguyên ngưng long tích, nhất nhận phá vân quán cửu tiêu§r",
        'skill.sword_soaring.screen_sword.tooltip': "§f§lKiếm Khí Dệt Lưới Phong Bát Hoang, Trận Thành Thiên Địa Tiêu Túc§r\n\nHiệu triệu Thái Hư Kiếm Vực để chống đỡ mọi vết thương. Hóa giải mũi tên bay, phản kích khi trúng đòn cận chiến.\n\nMỗi lần chịu đòn (%d/6), tiêu hao 1 kiếm, hồi phục %.1f Khí Huyết\n\nDuy trì: %.1f giây\nThời gian hồi chiêu: %.1f giây\n\n Nhấn [%s]",
        'skill.sword_soaring.rain_sword.tooltip': "§f§lBắc Đẩu Thiên Cương Hóa Kiếm Vực, Trận Hướng Nơi Đâu Trảm Yêu Tà§r\n\nMỗi đòn đánh đều dẫn động kiếm vũ, tạo ra từ %d đến %d tàn kiếm\n\nDuy trì: %.1f giây\nThời gian hồi chiêu: %.1f giây\n\n Nhấn [%s]"
    },
    'touhou_little_maid': {
        'model.authors_and_credits.sazuki.desc': "§7Đôi tai rất nhạy cảm, xin đừng chạm vào nhé"
    }
}

for ns, keys in clean_replacements.items():
    lang_dir = os.path.join(base, ns, 'lang')
    for lang_code in ('vi_vn.json', 'zh_cn.json', 'en_us.json'):
        fpath = os.path.join(lang_dir, lang_code)
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for k, v in keys.items():
                data[k] = v
            with open(fpath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Patched {fpath}")

print("Fixed all placeholder formatting!")
