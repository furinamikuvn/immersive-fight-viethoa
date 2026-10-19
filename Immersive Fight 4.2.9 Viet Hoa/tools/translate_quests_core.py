import os
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
chapters_dir = os.path.join(base_dir, "ftbquests", "chapters")
dist_quests_dir = os.path.join(base_dir, "dist", "quests", "chapters")
os.makedirs(dist_quests_dir, exist_ok=True)

# 1. Translate boss.snbt
boss_path = os.path.join(chapters_dir, "boss.snbt")
with open(boss_path, 'r', encoding='utf-8') as f:
    boss_content = f.read()

boss_replacements = {
    'hover: ["点击打开百科网页"]': 'hover: ["Nhấp để mở trang Bách Khoa Toàn Thư (Wiki)"]',
    'description: ["末影之眼激活"]': 'description: ["Kích hoạt Eye of Ender"]',
    '"击杀敌对生物时，有较低的概率掉落。"': '"Khi tiêu diệt sinh vật thù địch, có tỷ lệ rơi thấp."',
    '"跟随该物品飞行的方向，"': '"Dõi theo hướng bay của vật phẩm,"',
    '"玩家可以找到暗夜巫妖，"': '"Người chơi có thể tìm thấy Night Lich (Ám Dạ Vu Yêu),"',
    '"玩家需要在祭坛上放置四个灵魂之星，"': '"Người chơi cần đặt bốn Soul Star lên bàn tế,"',
    '"来召唤暗夜巫妖。"': '"Để triệu hồi Night Lich."',
    '"把虚空百合放置在地面，"': '"Đặt Void Lily xuống mặt đất,"',
    '"一段时间后出现黄色粒子"': '"Sau một thoáng sẽ xuất hiện các hạt phân tử màu vàng,"',
    '"跟随粒子你将会找到虚空之花。"': '"Dõi theo luồng phân tử, bạn sẽ tìm thấy Void Blossom (Hư Không Chi Hoa)."',
    'title: "祸乱鬼魅"': 'title: "Họa Loạn Ma Quái (Calamity Phantoms)"'
}

for src, tgt in boss_replacements.items():
    boss_content = boss_content.replace(src, tgt)

with open(boss_path, 'w', encoding='utf-8') as f:
    f.write(boss_content)

# 2. Translate alex.snbt (first section)
alex_path = os.path.join(chapters_dir, "alex.snbt")
with open(alex_path, 'r', encoding='utf-8') as f:
    alex_content = f.read()

alex_replacements = {
    'hover: ["异教徒献祭"]': 'hover: ["Hiến Tế Dị Giáo"]',
    '"(此章节任务主要为&e探索与材料获取&r)"': '"(Chương nhiệm vụ này tập trung vào &eKhám Phá & Thu Thập Nguyên Liệu&r)"',
    '"制作&b洞穴概论&r"': '"Chế tạo &bCave Book (Tổng Quan Hang Động)&r"',
    '"书内有模组&a详细资料&r"': '"Bên trong cuốn sách chứa &aThông Tin Chi Tiết&r về toàn bộ mod"',
    '"包含道具获取合成、生物信息、物品介绍等等"': '"Bao gồm công thức chế tạo, thông tin tập tính sinh vật và mô tả cổ vật"',
    '"在洞穴勘探台上"': '"Đặt trên Bàn Thám Hiểm Hang Động"',
    '"破译出手稿，合成地图右键，等待地图加载，"': '"Giải mã cổ bản thảo, chế tạo bản đồ rồi nhấn chuột phải, chờ bản đồ tải xong,"',
    '"它会告诉你洞穴所在位置"': '"Nó sẽ chỉ dẫn cho bạn tọa độ chính xác của hang động ẩn giấu"',
    '"&8&o（破译提示：石板文字为“标准银河字母”）&r&r"': '"&8&o(Gợi ý giải mã: Ký tự trên phiến đá là \\"Chữ Cái Ngân Hà Tiêu Chuẩn\\")&r&r"'
}

for src, tgt in alex_replacements.items():
    alex_content = alex_content.replace(src, tgt)

with open(alex_path, 'w', encoding='utf-8') as f:
    f.write(alex_content)

# Copy all chapters to dist/quests/chapters
import shutil
for f in os.listdir(chapters_dir):
    if f.endswith('.snbt'):
        shutil.copy2(os.path.join(chapters_dir, f), os.path.join(dist_quests_dir, f))

print("Successfully translated and copied FTB Quests chapters to dist/quests/chapters!")
