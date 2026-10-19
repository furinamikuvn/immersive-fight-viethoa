import os
import sys
import re
import json

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

imfdata_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa\global_packs\required_data\imfdata"

# Translation dictionary for mcfunctions and advancements
REPLACEMENTS = {
    # mcfunctions
    "【BOSS血量】目前为10倍！": "【MÁU BOSS】Hiện tại là 10x!",
    "【BOSS血量】目前为1倍！": "【MÁU BOSS】Hiện tại là 1x!",
    "【BOSS血量】目前为2倍！": "【MÁU BOSS】Hiện tại là 2x!",
    "【BOSS血量】目前为3倍！": "【MÁU BOSS】Hiện tại là 3x!",
    "【BOSS血量】目前为4倍！": "【MÁU BOSS】Hiện tại là 4x!",
    "【BOSS血量】目前为5倍！": "【MÁU BOSS】Hiện tại là 5x!",
    
    "【全局伤害】目前为1.0倍！": "【SÁT THƯƠNG TOÀN CỤC】Hiện tại là 1.0x!",
    "【全局伤害】目前为1.5倍！": "【SÁT THƯƠNG TOÀN CỤC】Hiện tại là 1.5x!",
    "【全局伤害】目前为2.0倍！": "【SÁT THƯƠNG TOÀN CỤC】Hiện tại là 2.0x!",
    "【全局伤害】目前为2.5倍！": "【SÁT THƯƠNG TOÀN CỤC】Hiện tại là 2.5x!",
    "【全局伤害】目前为3.0倍！": "【SÁT THƯƠNG TOÀN CỤC】Hiện tại là 3.0x!",

    "【全局血量】目前为1.0倍！": "【MÁU TOÀN CỤC】Hiện tại là 1.0x!",
    "【全局血量】目前为1.5倍！": "【MÁU TOÀN CỤC】Hiện tại là 1.5x!",
    "【全局血量】目前为2.0倍！": "【MÁU TOÀN CỤC】Hiện tại là 2.0x!",
    "【全局血量】目前为2.5倍！": "【MÁU TOÀN CỤC】Hiện tại là 2.5x!",
    "【全局血量】目前为3.0倍！": "【MÁU TOÀN CỤC】Hiện tại là 3.0x!",
    "【全局血量】目前为5.0倍！": "【MÁU TOÀN CỤC】Hiện tại là 5.0x!",

    "【敌对生物生成限制】每位玩家限制 10 只": "【GIỚI HẠN QUÁI VẬT】Mỗi người chơi giới hạn 10 con",
    "【敌对生物生成限制】每位玩家限制 20 只": "【GIỚI HẠN QUÁI VẬT】Mỗi người chơi giới hạn 20 con",
    "【敌对生物生成限制】每位玩家限制 30 只": "【GIỚI HẠN QUÁI VẬT】Mỗi người chơi giới hạn 30 con",
    "【敌对生物生成限制】每位玩家限制 50 只": "【GIỚI HẠN QUÁI VẬT】Mỗi người chơi giới hạn 50 con",
    "【敌对生物生成限制】每位玩家限制 100 只": "【GIỚI HẠN QUÁI VẬT】Mỗi người chơi giới hạn 100 con",
    "【敌对生物生成限制】无数量限制": "【GIỚI HẠN QUÁI VẬT】Không giới hạn số lượng",

    # Advancements - Simply Swords
    "奥数强化": "Cường Hóa Bí Thuật",
    "奥术斧钺": "Rìu Chiến Bí Thuật",
    "找到独特的武器，奥术斧钺": "Tìm thấy vũ khí độc nhất: Arcanethyst",
    "找到独特的武器": "Tìm thấy vũ khí độc nhất",
    "找到独特武器": "Tìm thấy vũ khí độc nhất",
    
    "孢子满溢": "Bào Tử Tràn Đầy",
    "木棘之杖": "Mộc Cốt Cực Trượng",
    "找到独特的武器，木棘之杖": "Tìm thấy vũ khí độc nhất: Bramblethorn",

    "硫磺阔剑": "Lưu Huỳnh Trọng Kiếm",
    "找到独特的武器，硫磺阔剑": "Tìm thấy vũ khí độc nhất: Brimstone",
    "不包括爆炸防护": "Không bao gồm bảo vệ chống nổ",

    "星界之力": "Sức Mạnh Tinh Giới",
    "异界之窗": "Cánh Cửa Dị Giới",
    "找到独特武器，星界之窗": "Tìm thấy vũ khí độc nhất: Caelestis",

    "古代遗物": "Di Vật Cổ Xưa",
    "找到独特武器腐朽遗杖": "Tìm thấy vũ khí độc nhất: Decaying Relic",

    "获得沉睡圣器": "Sở hữu Thánh Khí Say Ngủ",
    "不包括电池": "Không bao gồm pin năng lượng",

    "余烬之刃": "Tàn Tro Kiếm Lạc",
    "找到独特的武器，余烬之刃": "Tìm thấy vũ khí độc nhất: Emberblade",
    "怒在火中烧": "Nộ Hỏa Thiêu Đốt",

    "火灾隐患": "Hiểm Họa Hỏa Hoạn",
    "找到独特的武器烬笞": "Tìm thấy vũ khí độc nhất: Emberlash",

    "找到独特武器谜风": "Tìm thấy vũ khí độc nhất: Enigma",
    "天气控制": "Khống Chế Thời Tiết",

    "这东西还活着吗": "Vật này còn sống không?",
    "找到独特武器燎原": "Tìm thấy vũ khí độc nhất: Flamewind",

    "霜降": "Sương Giá Giáng Lâm",
    "冻结": "Đóng Băng Vĩnh Cửu",
    "找到独特的武器，霜降": "Tìm thấy vũ khí độc nhất: Frostfall",

    "预言者之剑": "Thanh Kiếm Của Nhà Tiên Tri",
    "来自深渊": "Đến từ Vực Thẳm",
    "找到独特的武器，预言者之剑": "Tìm thấy vũ khí độc nhất: Harbinger",

    "炉火巨锤": "Lò Lửa Cự Chùy",
    "在烈火中锻造": "Rèn luyện trong biển lửa",
    "找到独特的武器，炉火巨锤": "Tìm thấy vũ khí độc nhất: Hearthflame",

    "找到独特的武器群蜂之心": "Tìm thấy vũ khí độc nhất: Hiveheart",
    "不是蜜蜂": "Không phải ong mật bình thường",

    "请细听": "Hãy lắng nghe kỹ",
    "冰语": "Lời Thì Thầm Của Băng",
    "找到独特的武器，冰语": "Tìm thấy vũ khí độc nhất: Icewhisper",

    "如履薄冰": "Như Bước Trên Băng Mỏng",
    "海兽利维坦": "Hải Thú Leviathan",
    "找到独特的武器，海兽利维坦": "Tìm thấy vũ khí độc nhất: Livyatan",

    "瘟疫长剑": "Dịch Bệnh Trường Kiếm",
    "或许不要触碰它": "Có lẽ tốt nhất là đừng chạm vào nó",
    "找到独特的武器，瘟疫长剑": "Tìm thấy vũ khí độc nhất: Plague Longsword",

    "找到独特武器秘法双头剑": "Tìm thấy vũ khí độc nhất: Magiblade",
    "找到独特武器秘法之镰": "Tìm thấy vũ khí độc nhất: Magiscythe",
    "找到独特武器秘法之矛": "Tìm thấy vũ khí độc nhất: Magispear",
    "古代科技": "Công Nghệ Thất Truyền Cổ Đại",

    "雷神之锤": "Lôi Thần Chi Chùy",
    "它回来了": "Nó đã trở lại",
    "对吗": "Phải không?",
    "找到独特的武器，雷神之锤": "Tìm thấy vũ khí độc nhất: Mjolnir",

    "熔火": "Dung Nham Nóng Chảy",
    "可掌握在手中": "Có thể cầm nắm trong tay",
    "温度恰到好处": "Nhiệt độ vừa chuẩn xác",
    "找到独特的武器，熔火": "Tìm thấy vũ khí độc nhất: Molten Edge",

    "找到独特武器荣缎劈刀": "Tìm thấy vũ khí độc nhất: Ribboncleaver",
    "需要肱二头肌": "Cần cơ bắp tay khỏe mạnh",

    "获得一把符文武器": "Sở hữu một món vũ khí Cổ Ngữ",
    "符文镶嵌": "Khảm Nạm Cổ Ngữ",

    "暗影之刺": "Hắc Ám Thứ Kích",
    "从暗影中袭来": "Tập kích từ trong bóng tối",
    "找到独特的武器，暗影之刺": "Tìm thấy vũ khí độc nhất: Shadowsting",

    "简易刀剑": "Simply Swords (Kiếm Đồ Danh Khí)",
    "符文的力量在等待着你": "Sức mạnh của Cổ Ngữ đang chờ đón bạn",

    "获得沉眠的巫妖之刃": "Sở hữu Slumbering Lichblade say ngủ",
    "苏醒": "Thức Tỉnh Uy Lực",

    "聚魂之锤": "Tụ Hồn Cự Chùy",
    "灵魂守护者": "Hộ Vệ Linh Hồn",
    "找到独特的武器，聚魂之锤": "Tìm thấy vũ khí độc nhất: Soulkeeper",

    "灵魂焚烧者": "Hỏa Thiêu Linh Hồn",
    "葬魂": "Lễ Mai Táng Linh Hồn",
    "找到独特的武器，灵魂焚烧者": "Tìm thấy vũ khí độc nhất: Soulpyre",

    "裂魂之镰": "Liệt Hồn Chi Liêm",
    "灵魂收割者": "Kẻ Gặt Hái Linh Hồn",
    "找到独特的武器，裂魂之镰": "Tìm thấy vũ khí độc nhất: Soulrender",

    "窃魂之剑": "Thiết Hồn Chi Kiếm",
    "灵魂窃取": "Đoạt Linh Hồn",
    "找到独特的武器，窃魂之剑": "Tìm thấy vũ khí độc nhất: Soulstealer",

    "宇宙之怒": "Cơn Thịnh Nộ Vũ Trụ",
    "找到独特的武器星芒": "Tìm thấy vũ khí độc nhất: Star's Edge",

    "风暴之使": "Sứ Giả Bão Tố",
    "风暴使者": "Stormbringer",
    "找到独特的武器，风暴使者": "Tìm thấy vũ khí độc nhất: Stormbringer",

    "风暴之刃": "Phong Bạo Chi Nhận",
    "天雷再临": "Thiên Lôi Tái Lâm",
    "找到独特的武器，风暴之刃": "Tìm thấy vũ khí độc nhất: Storm's Edge",

    "烈日之焰": "Liệt Nhật Chi Diễm",
    "神圣的": "Thiêng Liêng & Thuần Khiết",
    "找到独特的武器，烈日之焰": "Tìm thấy vũ khí độc nhất: Sunfire",

    "带长棍的剑": "Thanh Kiếm Gắn Gậy",
    "工艺杰作": "Kiệt Tác Chế Tác",
    "找到独特的武器，带长棍的剑": "Tìm thấy vũ khí độc nhất: Sword on a Stick",

    "天气预警": "Cảnh Báo Thời Tiết",
    "找到独特武器烈风": "Tìm thấy vũ khí độc nhất: Tempest",

    "守望者": "Kẻ Canh Giữ (The Watcher)",
    "一直在注视着": "Vẫn luôn dõi theo mọi hành động",
    "找到独特的武器，守望者": "Tìm thấy vũ khí độc nhất: The Watcher",

    "纵雷": "Phóng Lôi Điện",
    "雷鸣时刻": "Thời Khắc Sấm Sét Vang Dội",
    "找到独特的武器，纵雷": "Tìm thấy vũ khí độc nhất: Thunderbrand",

    "扭曲之刃": "Kiếm Bị Biến Dạng",
    "逐渐变得扭曲": "Dần trở nên vặn vẹo dị thường",
    "找到独特的武器，扭曲之刃": "Tìm thấy vũ khí độc nhất: Twisted Blade",

    "守望战刃": "Thủ Vọng Chiến Nhận",
    "睁开双眼": "Mở rộng tầm mắt",
    "找到独特的武器，守望战刃": "Tìm thấy vũ khí độc nhất: Watching Warglaive",

    "打蜡": "Phủ sáp",
    "找到独特的武器织蜡": "Tìm thấy vũ khí độc nhất: Waxweaver",

    "疾风之刃": "Tật Phong Chi Nhận",
    "你听见了吗": "Ngươi có nghe thấy thanh âm ấy không?",
    "找到独特的武器，疾风之刃": "Tìm thấy vũ khí độc nhất: Whisperwind",

    "脱蜡": "Tẩy sáp",
    "找到独特的武器摇红": "Tìm thấy vũ khí độc nhất: Wickpiercer"
}

modified = 0
for root, dirs, files in os.walk(imfdata_dir):
    for f in files:
        if f.endswith(('.json', '.mcfunction')):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fp:
                content = fp.read()
            
            orig = content
            for src, tgt in sorted(REPLACEMENTS.items(), key=lambda x: len(x[0]), reverse=True):
                content = content.replace(src, tgt)
                
            if content != orig:
                with open(p, 'w', encoding='utf-8') as fp:
                    fp.write(content)
                modified += 1

print(f"Đã Việt hóa thành công {modified} tệp tin trong imfdata datapack!")
