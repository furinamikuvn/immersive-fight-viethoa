import os
import sys
import json
import zipfile

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"D:\minecraft mod trung\Immersive Fight 4.2.9 Viet Hoa"
trans_zip = os.path.join(base_dir, "resourcepacks", "IMF-Trans.zip")
backup_zip = os.path.join(base_dir, "resourcepacks", "IMF-Trans.zip.bak")

# Load unique strings
with open(os.path.join(base_dir, "tools", "patchouli_unique_strings.json"), 'r', encoding='utf-8') as f:
    unique_list = json.load(f)

# Comprehensive Vietnamese translation mapping for Simply Swords Runic Grimoire
trans_map = {
    "(该武器故事尚未编写)": "(Câu chuyện của vũ khí này chưa được ghi chép)",
    "一种无法追溯起源的古老科技的产物。剑柄上上奇怪的光似乎会随着风的变化而闪动。": "Một sản vật công nghệ cổ xưa không thể truy nguyên nguồn gốc. Ánh sáng kỳ lạ trên chuôi kiếm dường như nhấp nháy theo từng làn gió.",
    "三叉刺": "Tam Xoa Thích (Sai)",
    "三叉刺是由中国的铁尺改进而成的一种短兵器，又名十手、短叉、笔架叉。它的适应性高，但需要相当的技巧和训练才能有效使用。它的设计使得持有者能够格挡甚至是锁住对方的武器，使得自己占上风。它体积小巧，在狭窄空间和近战中尤为好用。": "Tam Xoa Thích (Sai) là đoản binh khí cải tiến từ Thiết Xích, có độ linh hoạt cao, đòi hỏi kỹ năng để sử dụng hiệu quả. Thiết kế cho phép đỡ đòn hoặc khóa vũ khí đối phương, chiếm thế thượng phong trong cận chiến không gian hẹp.",
    "上一页的内容都是编的。细想一下，这就是一把剑然后在剑柄绑了根棍子。": "Nội dung trang trước đều là bịa đấy. Nghĩ kỹ mà xem, đây thực chất chỉ là một thanh kiếm buộc thêm cây gậy vào chuôi thôi.",
    "不稳定": "Bất Ổn Định (Unstable)",
    "不稳定符文包含了$(#9243a3)$(l)混乱$()的精华. $(br2)它会给予持有者随机的状态效果。": "Phù văn Bất Ổn Định chứa tinh hoa của $(#9243a3)$(l)Hỗn Loạn$(). $(br2)Nó ban cho người cầm hiệu ứng trạng thái ngẫu nhiên.",
    "不需要的独特武器可以在熔炉中烧炼，烧炼的产物可以合成符文宝石，用于镶嵌给其他独特武器。": "Vũ khí độc nhất không dùng đến có thể nung trong lò luyện, sản phẩm thu được dùng để chế tạo ngọc phù văn khảm nạm cho vũ khí khác.",
    "主动防御": "Chủ Động Phòng Ngự (Shielding)",
    "主动防御符文给武器注入$(#389fff)$(l)保护$()的精华。$(br2)它可以让持有者自动向周围敌人射箭，只要物品栏中有足够的箭矢。": "Phù văn Chủ Động Phòng Ngự truyền vào vũ khí tinh hoa $(#389fff)$(l)Bảo Vệ$(). $(br2)Nó tự động bắn tên vào kẻ địch xung quanh nếu trong túi có đủ tên.",
    "传说中由矮人布洛克和伊特里所锻造，赠送给雷神托尔的战锤。它是一种威力惊人的武器，当被选中的战士使用它时，一次攻击甚至能摧毁一座山脉。": "Chiến chùy huyền thoại do người lùn Brokkr và Eitri rèn tặng Lôi Thần Thor. Uy lực kinh người, khi chiến binh được chọn vung lên, một đòn có thể san phẳng cả ngọn núi.",
    "传说中这把剑在锻造中加入了一场瘟疫中的死者遗体，并注入了黑暗魔法。这把武器散发着不祥的腐朽气息，非常适合那些想要虚弱敌人扭转战局的战士。": "Truyền thuyết kể rằng thanh kiếm này khi rèn đã hòa trộn thi hài người chết vì dịch bệnh và ma thuật hắc ám. Nó tỏa ra tử khí mục nát, làm suy yếu kẻ địch và xoay chuyển cục diện.",
    "传说裂魂的刀刃是由一种神秘的黑色金属制成的，散发着邪恶的能量。据说它不仅能削肉断骨，还能斩断灵魂。": "Lưỡi đao Liệt Hồn chế tác từ kim loại đen thần bí, tỏa ra tà năng tột cùng. Không chỉ chém sắt gãy xương mà còn có thể cắt đứt cả linh hồn.",
    "余烬之刃": "Emberblade (Dư Hãn Chi Nhận)",
    "余烬之刃是一把强力的长剑，灌注了火焰的力量。它由一种稀有的金属锻造而成，能耐受周围火焰的高温。战斗时，该武器能用火焰包围使用者，同时增强力量和速度。使用者还可以将火焰集中到剑上蓄力发射余烬弹攻击远处敌人。": "Emberblade là trường kiếm cường đại truyền ngọn lửa cuồng bạo. Rèn từ kim loại hiếm chịu nhiệt cực cao, bao bọc người dùng trong biển lửa, tăng sức mạnh và tốc độ, đồng thời có thể bắn đạn tro tàn tầm xa.",
    "余烬鞭挞": "Emberlash",
    "作者有点懒，背景故事还没写。": "Tác giả hơi lười, cốt truyện bối cảnh vẫn chưa viết xong.",
    "冰冻": "Đóng Băng (Freeze)",
    "冰冻可以为武器注入$(#38caff)$(l)寒冰$()的力量。$(br2)它可以让持有者在攻击时有几率冰冻目标。": "Đóng Băng truyền vào vũ khí sức mạnh $(#38caff)$(l)Băng Hàn$(). $(br2)Đòn tấn công có cơ hội đóng băng mục tiêu.",
    "冰冻符文能够打乱对手节奏，给自己优势。$(br2)它很适合需要团控的玩家，利用冰冻控制敌人，给队友攻击机会。": "Phù văn Đóng Băng làm rối loạn nhịp độ đối thủ, tạo ưu thế kiểm soát và mở ra cơ hội dồn sát thương.",
    "冰语": "Icewhisper (Băng Ngữ)",
    "冰语这把戟非常致命，只要手持它，就会散发弱化敌人的冰冻光环，减速周围的敌人，并且造成持续的伤害。减速效果也方便后续的攻击。": "Kích Icewhisper vô cùng chí mạng, cầm trên tay sẽ tỏa ra hào quang băng giá làm suy yếu, giảm tốc và thiêu đốt sát thương kẻ địch xung quanh.",
    "利维坦": "Livyatan (Thủy Quái)",
    "利维坦是一把可怕的手斧，能够冻结敌人然后粉碎它们，造成大量伤害。每一次攻击都有一定几率释放一股冰冻能量吞噬敌人，使它们完全不能移动。": "Livyatan là cây rìu đáng sợ, có thể đóng băng mục tiêu rồi đập vỡ chúng, gây sát thương khổng lồ và cầm chân hoàn toàn kẻ địch.",
    "加护": "Gia Hộ (Ward)",
    "加护符文的能力很强，但也有风险。它可以给持有者提供一个护盾抵抗伤害。激活时，持有者会消耗一半的生命值，在周围形成一个屏障吸收伤害。": "Phù văn Gia Hộ tạo lá chắn hấp thụ sát thương cực mạnh. Khi kích hoạt tiêu hao nửa lượng máu hiện tại tạo kết giới phòng ngự.",
    "动能": "Động Năng (Momentum)",
    "动能符文为武器提供$(#389fff)$(l)动能$()的精华. $(br2)它能产生向前的推力，推动持有者向前移动。": "Phù văn Động Năng mang tinh hoa $(#389fff)$(l)Động Năng$(). $(br2)Tạo lực đẩy mạnh mẽ lao về phía trước.",
    "即使是普通人使用它时，投掷出去也能返回持有者手中。它也能在雨天攻击时召唤闪电，或是手动施放一阵闪电风暴。或许它在等待它真正的主人？": "Khi ném đi sẽ tự động quay về tay chủ nhân. Trong ngày mưa có thể triệu hồi sấm sét hoặc giải phóng bão lôi cuồng nộ.",
    "双头剑": "Song Đầu Kiếm (Twinblade)",
    "双头剑是一种需要高超的技巧和灵活性才能驾驭的武器。它由两把剑刃组合在一起而成，因此它拥有很高的速度和精确度。它是一把强大的武器，但需要合适的人。": "Song Đầu Kiếm kết hợp hai mũi kiếm sắc bén, đạt tốc độ và độ chính xác cực cao, đòi hỏi sự khéo léo điêu luyện của chiến binh.",
    "受到灵魂撕裂状态的目标会虚弱，而且可以施放独特能力造成额外伤害。据说这把武器是一个强大的亡灵巫师使用的，他用这把镰刀收割了敌人的灵魂用作己用。它是一把强大的武器，请谨慎使用。传言它收割灵魂的能力会影响自己的灵魂。": "Mục tiêu bị Xé Rách Linh Hồn sẽ suy yếu nặng nề. Lưỡi hái của Pháp Sư Chiêu Hồn thu hoạch linh hồn kẻ địch, uy lực tột bậc nhưng ẩn chứa hiểm họa.",
    "在锻造台中将强能结晶和符文石板或下界合金结晶锻造合成时，就会合成宝石。这些宝石可以镶嵌进对应的宝石槽中，用多样的方式强化你的独特武器。": "Dùng Bàn Rèn hợp nhất Tinh Thể Năng Lượng và Phiến Đá Phù Văn hoặc Netherite để tạo ngọc bảo, dùng khảm vào ô vũ khí độc nhất.",
    "基础武器": "Vũ Khí Cơ Bản",
    "奥术紫晶戟": "Arcanethyst (Áo Thuật Kích)",
    "奥术紫晶戟使用一种类似心灵感应的魔法操控敌人。它由注入魔力的紫水晶打造而成。据说紫水晶是魔力传播的良好媒介。": "Arcanethyst chế tác từ thạch anh tím ngập tràn ma lực, điều khiển tâm trí kẻ địch và phóng thích sóng xung kích tâm linh.",
    "如同它的名字一样，这个符文的作用完全无法预测。它不仅包含正面效果，还包含负面效果。$(br2)它比较适合那些喜欢运气的玩家。": "Hiệu quả hoàn toàn bất định, bao gồm cả bùa lợi và bùa hại, thích hợp cho những chiến binh ưa thích thử vận may.",
    "它可以在对抗高速的敌人时发挥作用，使自己的速度提高追上它们。$(br2)因为会点燃自己，所以要注重自己的防御。": "Giúp tăng vọt tốc độ để truy đuổi kẻ địch nhanh nhẹn. Cần lưu ý phòng ngự vì đòn đánh có thể tự thiêu đốt bản thân.",
    "守望战刃": "Watching Warglaive (Thủ Vọng Chiến Nhận)",
    "守望战刃是一把强大的武器，由那些熟练而凶悍的战士使用。剑刃中央镶嵌着两只会眨眼的眼睛。整个武器由一种几乎黑色的金属制成，似乎可以吸收周围的光。": "Vũ khí của những chiến binh tàn bạo. Giữa thân lưỡi đao khảm hai con mắt ma quái luôn chớp nháy, thân đao đen thẫm như hút cạn ánh sáng xung quanh.",
    "守望阔剑": "The Watcher (Thủ Vọng Khoát Kiếm)",
    "守望阔剑是一把大剑，剑柄上嵌着一只诡异的在眨眼的眼睛，据说这是它力量的源头。它的剑刃是由一种深色到几乎黑色的金属制成，这种金属似乎可以吸收周围的光。": "Đại kiếm kỳ dị với con mắt ma quái chớp nháy trên chuôi, nguồn cội của sức mạnh bóng tối nuốt chửng ánh sáng.",
    "守望阔剑的特殊能力可以一击击倒敌人，但据说只能在持有者非常专注或者敌人非常虚弱时才可能出现。传说只有真正的战士——那些有着坚强意志和渴望力量的战士——才能驾驭它并充分发挥它的潜力。": "Khả năng đặc biệt có thể hạ gục kẻ địch trong chớp mắt khi đối thủ suy yếu, chỉ chiến binh có ý chí sắt đá mới thuần phục được.",
    "宝石镶嵌": "Khảm Bảo Thạch",
    "宝石镶嵌机制": "Cơ Chế Khảm Bảo Thạch",
    "对于近战高伤害玩家而言这个符文很好用，他们可以利用额外的攻击和移动速度快速输出并回避敌人。": "Rất hữu dụng cho người chơi cận chiến sát thương cao, tận dụng tốc độ để sốc sát thương và né đòn thần tốc.",
    "巨斧": "Cự Phủ (Greataxe)",
    "巨斧对使用者的力量和技巧要求都很高。它的重量决定了使用者必须两只手握持并挥舞，是一种典型的双手武器。巨斧的适应性很强，可以砍、劈、或者捶。": "Vũ khí hai tay thuần túy đòi hỏi thể lực lớn, những cú bổ chém mang sức công phá hủy diệt hàng phòng ngự kẻ thù.",
    "巨锤": "Cự Chùy (Greathammer)",
    "巨锤因其重量和体积，每次攻击都能造成毁灭性的伤害而著称。历史上，多由步兵和重骑兵装备使用。在生活中，铁匠、泥瓦匠等工种也会使用锤子进行锤击操作。": "Uy lực chấn động địa cầu, mỗi cú vung búa nghiền nát giáp trụ và làm choáng váng mọi kẻ thù trong phạm vi.",
    "巫妖巨剑": "Slumbering Lichblade (Vu Yêu Cự Kiếm)",
    "巫妖巨剑是一把散发痛苦灵魂的大剑，会持续对附近敌人造成伤害。据说这把剑是用一个强大的巫妖的遗骨打造而成，注入了它吞噬过的灵魂。有时候，能听到一些邪恶的低语从剑上传出。": "Đại kiếm rèn từ hài cốt Vu Yêu cổ đại, giam giữ ngàn linh hồn đau đớn, phát ra những lời thì thầm tà ác và thiêu đốt sinh lực kẻ địch lân cận.",
    "庇佑": "Che Chở (Protect)",
    "庇佑符文给武器注入$(#389fff)$(l)保护$()的精髓。$(br2)它能让持有者每次攻击都有可能获得一层伤害吸收效果。": "Truyền vào tinh hoa $(#389fff)$(l)Bảo Vệ$(). $(br2)Mỗi đòn đánh có cơ hội nhận một tầng lá chắn hấp thụ sát thương.",
    "弯刀": "Đoản Đao / Dao Cong (Cutlass)",
    "弯刀适合近距离的切砍和刺击，在船上的近战攻击尤为适用。因此弯刀被海上的人们所喜爱。它的刀刃形状除了能加强砍切，还适合切肉、割绳子。": "Đoản đao cong sắc bén, tối ưu cho đòn chém nhanh và đâm xé trong cận chiến trên boong tàu hoặc địa hình hẹp.",
    "弱化": "Làm Yếu (Weaken)",
    "弱化符文给武器提供了$(#87185d)$(l)枯萎()的精华。$(br2)它能在攻击时减速并虚弱目标。": "Truyền vào tinh túy $(#87185d)$(l)Héo Rũ$(). $(br2)Làm chậm và suy yếu mục tiêu khi trúng đòn.",
    "强能结晶": "Tinh Thể Năng Lượng (Empowered Remnant)",
    "强能结晶可以在熔炉中烧炼独特武器获得。独特武器经过烧炼之后被摧毁，一部分力量形成强能结晶保留。": "Thu được khi nung vũ khí độc nhất trong lò. Vũ khí bị phân rã, ngưng tụ lại thành Tinh Thể Năng Lượng.",
    "影刺": "Shadowsting (Ảnh Thích)",
    "影刺是一把充满暗影力量的细剑。它的独特能力使得持有者在攻击时有一定几率对敌人造成基于护甲的魔法伤害，魔法伤害无视防御。": "Kiếm liễu ngập tràn bóng tối, tung đòn sát thương ma thuật xuyên thấu hoàn toàn giáp trụ của kẻ địch.",
    "微风": "Gió Nhẹ (Zephyr)",
    "微风的符文力量可以给武器注入$(#85a0ab)$(l)风元素$()的精华。$(br2)每次攻击时，都有机会提高攻速和移速。": "Truyền vào tinh túy $(#85a0ab)$(l)Phong Nguyên Tố$(). $(br2)Mỗi đòn đánh có cơ hội tăng tốc độ di chuyển và tốc độ ra đòn.",
    "战刃": "Chiến Nhận (Warglaive)",
    "战刃拥有很高的速度和灵活性，尤其是双持，可以利用锋利的刀刃打出快速而致命的连击。它需要持有者非常灵活，才能在战场上高效发挥。": "Vũ khí linh hoạt tuyệt hảo khi song thủ song đao, thực hiện các chuỗi combo liên hoàn xé rách kẻ thù.",
    "戟": "Kích (Halberd)",
    "戟是一种长兵器，在长杆的一端装有带有钩尖的刃，杆上装有斧刃。戟的适用性高、攻击范围远。在熟练使用它的战士手里，这是一种强大的武器。": "Trường binh khí kết hợp giữa mũi giáo và lưỡi rìu, tầm đánh xa và biến hóa khôn lường.",
    "打开物品栏之后，左键点击宝石取出，然后点击武器即可将宝石镶嵌到武器上。宝石物品会消失，武器获得宝石的能力。": "Mở túi đồ, nhấp chuột trái vào ngọc rồi nhấp vào vũ khí để khảm nạm. Ngọc sẽ tiêu hao và vũ khí nhận thêm năng lực mới.",
    "扭曲波刃剑": "Twisted Blade (Kiếm Biến Dạng)",
    "扭曲波刃剑是一把令人生畏的大剑，以其独特而致命的设计闻名。这把剑是由一种特殊的钢制造，能在打击时改变自身的形状。": "Đại kiếm rèn từ thép dị thường, có thể biến dạng theo từng nhát chém, gây nên vết thương chí mạng khó lường.",
    "护盾持续 6 秒，并且每次发出脉冲都会提供一层吸收效果。护盾的强度随着当前生命值增加而提高。对于那些喜欢冒险的玩家来说，这个符文可以作为防御选择。": "Khiên duy trì 6 giây, mỗi xung nhịp tăng một tầng hấp thụ sát thương, cường độ tăng dần theo máu hiện tại.",
    "据说聚魂是由一种神秘的材料制成的，能吸收死者的灵魂，在持有者和灵魂之间建立联系。这些被吸收的灵魂能保护持有者，吸收一部分伤害。": "Thu hút linh hồn kẻ tử nạn, liên kết chúng lại thành màn chắn bảo hộ người nắm giữ khỏi sát thương.",
    "据说这把剑会选择主人，只有配得上它的人才能使用它。然而，也有人说过度使用这把剑的能力会导致使用者失控，最后被火焰吞噬而惨死。": "Thanh kiếm biết chọn chủ nhân xứng đáng. Nhưng nếu lạm dụng, ngọn lửa hung tàn sẽ thiêu rụi chính người dùng.",
    "据说这把剑十分强大，但难以控制。众所周知，电荷本身就难以捕捉，有时候它的独特能力使用错了会对使用者是致命的。": "Nguồn điện tích cuồng nộ cực kỳ khó thuần phục, một sơ sẩy nhỏ có thể dẫn tới hậu quả chí mạng.",
    "据说这把双头剑是由一种能传导并能利用电力的金属锻造的。剑柄由深色木头制成，并有绝缘皮革套保护。": "Rèn từ kim loại siêu dẫn lôi điện, chuôi bọc da cách điện kiên cố bảo vệ đôi tay chiến binh.",
    "星芒": "Stars Edge (Tinh Mang)",
    "星芒是一把壮观的双头剑，它能与宇宙中恒星的力量产生共鸣。在阳光的照射下，星芒的能量涌动可以使它造成额外的攻击伤害。": "Song Đầu Kiếm cộng hưởng với năng lượng tinh tú vũ trụ, bộc phát sát thương cực hạn dưới ánh dương rực rỡ.",
    "未知的奇怪科技的产物。": "Sản vật của một nền văn minh công nghệ kỳ lạ chưa rõ nguồn gốc.",
    "本模组包含许多可合成的新武器，具备不同的战斗风格。每种武器都有四种基础材质：铁、金、钻石、下界合金。也支持部分其他模组的金属材质。": "Mod bổ sung nhiều vũ khí mới với phong cách tác chiến đa dạng từ Sắt, Vàng, Kim Cương đến Netherite và kim loại từ các mod khác.",
    "极速": "Cực Tốc (Swiftness)",
    "极速符文给武器注入$(#389fff)$(l)灵活$()的力量。$(br2)它能让武器攻击时有概率提高自己的速度。": "Truyền vào sức mạnh $(#389fff)$(l)Linh Hoạt$(). $(br2)Mỗi đòn đánh có cơ hội tăng tốc độ bản thân.",
    "棘刺": "Bramblethorn (Gai Nhọn)",
    "棘刺是一把木制的细剑，独特而致命。它看起来就像一根不起眼的树枝，但它隐藏着强大的能力。它由一种稀有的木材附魔后制成，轻便耐用，并且能够进行快速而致命的攻击。": "Thoạt nhìn như nhánh cây tầm thường, nhưng ẩn chứa ma pháp gai góc sắc nhọn, nhẹ nhàng và đâm xuyên hiểm hóc.",
    "武士刀": "Vũ Sĩ Đao (Katana)",
    "武士刀以锋利、强力、能使出兼具快速和精准的攻击而闻名。历史上，日本封建时代的武士们广泛使用这种刀。它是一名武士最重要的武器，也是武士阶级的象征。": "Nổi danh với độ bén ngót và chuẩn xác, biểu tượng của võ sĩ đạo với những đường kiếm trảm kích thần tốc.",
    "沉眠遗剑": "Dormant Relic (Trầm Miên Di Kiếm)",
    "沉睡遗剑是一把特殊的神秘的武器。它初看是一把普通的不起眼的剑，但它可以通过合成，逐渐解封隐藏的力量。": "Cổ kiếm thần bí đang say ngủ, có thể từng bước thức tỉnh sức mạnh vĩ đại thông qua các nghi thức rèn chế.",
    "淬魔": "Tôi Ma (Imbued)",
    "淬魔符文注入了$(#389fff)$(l)魔法$()的精华. $(br2)它可以让武器攻击时释放隐藏的魔法力量攻击敌人。": "Truyền tinh hoa $(#389fff)$(l)Ma Pháp$(). $(br2)Giải phóng năng lượng ma thuật ẩn giấu tấn công mục tiêu.",
    "漂浮": "Phiêu Phù (Float)",
    "漂浮是一种强大的符文，能干扰战斗节奏，让持有者占据优势。$(br2)它适合喜欢辅助和团控的玩家，他们可以使用这个能力控制敌人，给队友攻击的机会。": "Làm gián đoạn nhịp điệu chiến đấu, nhấc bổng kẻ thù lên không trung mở đường cho đòn kết liễu.",
    "炉火巨锤": "Hearthflame (Lò Lửa Cự Chùy)",
    "炉火巨锤是一把强大的锤子，具有引起大范围震动的能力。施放时，它会放出力场，将敌人拉向使用者，然后发出一阵爆炸点燃它们。": "Tạo từ trường kéo giật kẻ địch về phía người dùng rồi phát nổ bốc cháy rực lửa xung quanh.",
    "烈风": "Flamewind (Liệt Phong)",
    "焰痕": "Trailblaze (Diễm Ngân)",
    "焰痕符文是$(#bf4117)$(l)火焰$()的结晶。$(br2)它能在攻击中提高速度，但会点燃自身。": "Kết tinh của $(#bf4117)$(l)Ngọn Lửa$(). $(br2)Tăng vọt tốc độ khi ra đòn, song cũng tự thiêu đốt người cầm.",
    "然而，一开始的巫妖巨剑处于沉眠状态，其真正力量尚未解封。通过特殊的合成仪式，可以逐渐解封剑的更强能力。完全觉醒的巫妖巨剑可以命令灵魂攻击敌人，吸取它们的生命并回复持有者。这是一种威力巨大的武器，请小心使用。": "Khi thức tỉnh hoàn toàn, Vu Yêu Cự Kiếm chỉ huy vong hồn cắn xé kẻ thù và chuyển hóa sinh mệnh hồi phục cho chủ nhân.",
    "然而，这个隐藏的能力也是有代价的：火焰也会伤害持有者，尽管对持有者的伤害较小。": "Cái giá phải trả là ngọn lửa cũng gây tổn hại nhỏ lên chính cơ thể người sử dụng.",
    "熔火": "Molten Edge (Dung Hỏa)",
    "熔火是一把狂暴的手斧，当使用者受伤时，会增加力量和速度。持有者的生命值越低，这把武器就越强。": "Rìu cuồng nộ bùng cháy, sinh mệnh người cầm càng thấp thì sức mạnh và tốc độ bộc phát càng khủng khiếp.",
    "燎原": "Wildfire (Liêu Nguyên)",
    "爆炸不仅造成伤害，还可以将敌人从使用者身边炸飞，从而方便锁定目标或追击。攻击的时候也有机会发出这种炸飞敌人的爆炸。据说这把大锤是在世界上最热的火焰里锻造出来的，散发出一股热气。这把武器非常适合那些需要巨大伤害并且掌控战场的战士。": "Vụ nổ hất tung kẻ địch ra xa, tạo không gian xoay sở và áp đảo chiến trường bằng ngọn lửa nóng bỏng nhất thế gian.",
    "独特武器": "Vũ Khí Độc Nhất (Unique Weapons)",
    "独特武器可以在冒险中的箱子中找到。它们非常稀有，不能合成，每一把都具有特殊的能力。这些武器在铁砧中修理时，需要使用符文石板作为修理材料。": "Vũ khí hiếm có trong rương kho báu, không thể chế tạo thông thường và cần Phiến Đá Phù Văn trên đe để sửa chữa.",
    "狱灵宝石": "Bảo Thạch Ngục Linh (Netherite Gem)",
    "狱灵宝石可以在锻造台中将下界合金和强能结晶锻造合成。在点击鉴定之后，它们会随机揭示一个能力。": "Rèn từ Netherite và Tinh Thể Năng Lượng trên Bàn Rèn, giám định để mở khóa năng lực ngẫu nhiên.",
    "狱灵宝石可以嵌入独特武器的[狱灵槽]。": "Khảm nạm vào [Ô Ngục Linh] của vũ khí độc nhất.",
    "献祭光环": "Hiến Tế Quang Hoàn (Immolation)",
    "献祭符文会提供一个献祭光环，激活时，持续对周围敌人造成伤害，用正义的火焰烧尽他们。这个伤害与持有者的生命值有关。": "Tạo vòng hào quang hiến tế thiêu đốt kẻ địch xung quanh bằng hỏa diệm dựa trên lượng máu của người dùng.",
    "环刃": "Hoàn Nhận (Chakram)",
    "环刃是一种投掷类的武器，装有刀刃。装备两把环刃攻击时，会施展范围攻击，同时攻击身边所有敌人。": "Vũ khí ném có lưỡi tròn, khi song thủ hai hoàn nhẫn sẽ tung đòn quét diện rộng tấn công toàn bộ mục tiêu quanh mình.",
    "瘟疫长剑": "Longsword Plague (Ôn Dịch Trường Kiếm)",
    "瘟疫长剑是一把被诅咒的武器，它在攻击时能够反转对方身上的正面效果，例如再生和抗性提升，转化为负面的效果。这可能弱化敌人，使得他们更脆弱，让自己占据优势。": "Thanh kiếm bị nguyền rủa, có khả năng đảo ngược bùa lợi của đối thủ (Hồi Máu, Kháng Cự) thành bùa hại suy nhược.",
    "矛": "Thương (Spear)",
    "矛拥有非常悠久的历史，它在用于战争之前最早用于狩猎。矛的攻击范围广，多用于戳刺。矛的制造和维护简单，使得它在古代甚至原始社会都广泛流行。": "Vũ khí đâm xuyên kinh điển với tầm với vượt trội và uy lực đâm thấu tâm can.",
    "石肤": "Thạch Phu (Stoneskin)",
    "石肤符文给武器注入$(#916f49)$(l)大地与岩石$()的魔法。$(br2)它使持有者在攻击时有概率提高自己的抗性，但降低速度。": "Truyền ma pháp $(#916f49)$(l)Đại Địa & Nham Thạch$(). $(br2)Tăng mạnh kháng cự nhưng giảm tốc độ di chuyển.",
    "硫磺阔剑": "Brimstone (Lưu Huỳnh Khoát Kiếm)",
    "硫磺阔剑是一把可怕的武器。它利用熔化硫磺的力量爆炸并伤害敌人。剑刃灌注的硫磺使得它每一次攻击都有可能释放出熔岩一般的火焰攻击。": "Giải phóng sức mạnh lưu huỳnh nóng chảy, bộc phát những đòn nổ dung nham thiêu đốt đối thủ.",
    "秘法之矛": "Magispear (Bí Pháp Chi Mâu)",
    "秘法之镰": "Magiscythe (Bí Pháp Chi Liêm)",
    "秘法双头剑": "Magiblade (Bí Pháp Song Đầu Kiếm)",
    "穿芯": "Wickpiercer (Xuyên Tâm)",
    "穿芯是一把精致的长矛，将优雅与致命融为一体，造型让人联想到华丽的烛台。它的独特能力在施放时能影响持有者的身心，使他们短时间内暴走，增加攻击速度。": "Trường thương thanh tao mang hình dáng chân nến tráng lệ, kích hoạt trạng thái bạo tẩu tăng tốc đâm liên tiếp.",
    "窃魂": "Soulrender (Thiết Hồn)",
    "窃魂是一种强大又神秘的武器，据说它可以偷取目标的灵魂并操纵它们的感知。它是一种锁定并操控敌人的武器，能够干扰目标的思维，使它们对持有者视而不见。": "Đoạt lấy linh hồn và thao túng giác quan, khiến tâm trí đối phương hỗn loạn và không thể nhận biết vị trí của bạn.",
    "符文宝石": "Bảo Thạch Phù Văn (Runic Gem)",
    "符文宝石可以在锻造台中将强能结晶和符文石板锻造合成。在点击鉴定之后，它们会随机揭示一个能力。": "Chế tạo trên Bàn Rèn từ Tinh Thể Năng Lượng và Phiến Đá Phù Văn, giám định để khám phá năng lực ngẫu nhiên.",
    "符文宝石可以镶嵌进独特武器的[符文槽]。符文宝石的能力只有攻击时触发。": "Khảm vào [Ô Phù Văn] của vũ khí độc nhất, kích hoạt khi tung đòn tấn công.",
    "符文石板可以在冒险的箱子中找到。它们可以将下界合金武器锻造升级为符文武器，赋予它们更强的能力。": "Tìm thấy trong rương thám hiểm, dùng để nâng cấp vũ khí Netherite thành vũ khí phù văn tối thượng.",
    "符文镌刻": "Khắc Phù Văn (Runic Etching)",
    "纵雷": "Stormbringer (Túng Lôi)",
    "纵雷是一把传奇的能驾驭雷电的戟。它由一种导电性非常好的稀有金属打造。柄上包裹一种特殊的绝缘材料，使用者可以安全地握持。": "Chiến kích huyền thoại thống trị sấm sét, phóng ra những luồng sét giáng rền vang chiến địa.",
    "细剑": "Tế Kiếm (Rapier)",
    "细剑是流行于16~17世纪的欧洲上流社会的武器，一般用于决斗和平民的自卫。细剑在历史上以快速、精准的攻击和优雅的造型著称。由于剑身细长，细剑需要一定的技巧和策略才能驾驭。": "Kiếm liễu quý tộc thanh thoát, tối ưu hóa đòn đâm điểm huyệt nhanh như chớp giật.",
    "织蜡": "Waxweaver (Dệt Sáp)",
    "织蜡是一把精致的阔剑，将优雅与致命融为一体，造型像华丽的烛台。它攻击着火的敌人时，会激发蜡烛的力量，给予持有者力量提升。": "Khoát kiếm hoa mỹ, khi chém vào kẻ địch đang bốc cháy sẽ khơi dậy sức mạnh của ngọn sáp ban tặng bùa lợi sức mạnh.",
    "绑棍的长剑": "Sword on a Stick (Kiếm Buộc Gậy)",
    "谜风": "Enigma (Mê Phong)",
    "野火": "Wildfire (Dã Hỏa)",
    "针垫": "Pincushion (Châm Điệm)",
    "长剑": "Trường Kiếm (Longsword)",
    "长柄刀": "Trường Bính Đao (Glaive)",
    "长柄镰": "Trường Bính Liêm (Scythe)",
    "阔剑": "Khoát Kiếm (Claymore)",
    "雷神之锤": "Mjolnir (Lôi Thần Chi Chùy)",
    "霜卫": "Sương Vệ (Frost Ward)",
    "霜降": "Sương Hàng (Frostfall)",
    "风之低语": "Whisperwind (Phong Chi Đê Ngữ)",
    "风暴之刃": "Storms Edge (Phong Bạo Chi Nhận)",
    "风暴使者": "Tempest (Phong Bạo Sứ Giả)",
    "霜卫符文附加了$(#38caff)$(l)寒冰$()的力量。$(br2)它能够召唤一个守卫，持续发射雪球攻击范围内的敌人。": "Phù văn Sương Vệ triệu hồi hộ vệ băng liên tục bắn cầu tuyết chế ngự kẻ địch xung quanh.",
    "霜卫适合擅长防御的玩家，他们可以用雪球控制战场。": "Rất phù hợp cho chiến thuật phòng thủ kiểm soát chiến trường.",
    "霜降是一把强大的锤子，它利用冰霜的力量冻结敌人。它由一种稀有金属锻造而成，能承受冰冻的严寒。锤头灌注了冰霜的力量，可以冻结攻击到的敌人。": "Búa băng giá cực đại, giáng đòn đông cứng mục tiêu trong lớp băng vĩnh cửu.",
    "风之低语是一把随风而舞的空灵的武士刀，能赋予持有者无与伦比的灵活性和神秘力量。这把刀的独特能力能让持有者划过战场，产生一种微弱的旋律共鸣，如同风吹过一样。每次快速的冲刺都会攻击敌人的感官，让他们迷失方向，变得脆弱。": "Thanh kiếm lướt như cơn gió thoảng, tấn công thính giác và cảm quan khiến đối thủ lạc lối.",
    "野火符文包含了$(#d1422c)$(l)烈焰$()的精华。$(br2)每次攻击时都有可能点燃附近的同类敌人。": "Phù văn Dã Hỏa chứa tinh hoa $(#d1422c)$(l)Liệt Diễm$(). $(br2)Đòn đánh có thể thiêu đốt lan sang các kẻ địch cùng loại gần kề.",
    "针垫符文为武器注入了$(#d1422c)$(l)反击$()的精华。$(br2)它能使武器根据持有者身上的箭矢数量造成额外的伤害。": "Phù văn Châm Điệm truyền tinh hoa $(#d1422c)$(l)Phản Kích$(). $(br2)Gây thêm sát thương dựa trên số mũi tên găm trên người.",
    "长剑用途多样，可以砍、刺、切。在中世纪，上到骑士下到普通士兵，都广泛地装备长剑。长剑是骑士的典型武器，在精度、切砍力和多用性方面非常有名。": "Trường kiếm đa năng công thủ toàn diện, vũ khí kinh điển lừng danh của các hiệp sĩ thời trung cổ.",
    "长柄刀，大刀中最常见的一种，细分可分为笔刀、掉刀、凤嘴刀、偃月刀、眉尖刀等。它是一种长兵器，由长杆末端安装单刃刀组成，非常适合横切和劈砍。长柄刀攻击距离较远，攻防兼备。": "Trường bính đao (Quan Đao/Đại Đao) tầm đánh rộng lớn, uy lực chém ngang quét dọc kinh thiên động địa.",
    "长柄镰是一种重型的锋利武器，挥舞时可造成大量伤害。长柄镰装有大型的弯曲刀刃和长柄，使得它能够进行大范围的斩击和劈砍攻击。": "Lưỡi hái dài nặng nề sắc bén, vung đòn quét sạch hàng loạt quân thù trong tầm mắt.",
    "阔剑是一种双手使用、可以切割和刺击的重型武器，历史上苏格兰勇士会在战斗中使用阔剑。它依靠巨大的体积和重量对敌人进行毁灭性的打击。": "Khoát kiếm khổng lồ vung bằng hai tay, uy lực dập tắt mọi sức kháng cự của kẻ đối đầu.",
    "除了冰冻光环，该武器还可以召唤出一阵暴风雪，将战场笼罩在冰天雪地之中。暴风雪会持续造成伤害，并且减速他们，让敌人难以发现自己，为自己提供优势。据说这把戟是用最纯净的冰打造的，它闪烁着冰冷的蓝光。": "Có thể triệu hồi bão tuyết nhấn chìm chiến trường, làm chậm và gây sát thương kéo dài lên quân địch.",
    "该武器在攻击时可以释放出一团有毒的孢子，使范围内的敌人中毒并且减缓行动能力。即使切换武器，孢子群也不会消失而是减弱效果。请注意，孢子会持续伤害攻击范围内除使用者外的所有生物，直到它们消失为止。所以请不要在队友或者你养的动物附近随意使用它。": "Phát tán bào tử độc làm chậm và trúng độc diện rộng. Cẩn trọng không dùng gần đồng minh hoặc vật nuôi.",
    "该武器拥有另一个独特效果，施放时向前短距离位移同时生成一阵暗影迷雾，阻碍敌人的视野。持有者可以利用这个能力让敌人混乱迷失方向，制造优势。": "Lướt ngắn về phía trước tạo sương mù bóng tối che mắt kẻ thù, tạo ưu thế đột kích bất ngờ.",
    "该武器有一个主动技能，施放时会将冰冻的敌人粉碎造成大量伤害。传说这把斧头是用一头传说中的海兽的心脏锻造而成的，它发出冰冷的蓝光。这种武器非常适合那些想控制敌人并且造成很大伤害的战士。": "Kỹ năng chủ động đập vỡ kẻ địch đang bị đóng băng gây sát thương cực lớn. Rèn từ trái tim thủy quái viễn cổ.",
    "该武器的特殊能力可以使持有者向前冲刺，拉近距离并以致命的精度进行攻击。它在蓄力施放时还能放出强大的电流，同时攻击多个敌人，使得它成为战场上的可怕杀器。": "Lao tới áp sát chớp nhoáng và phóng điện giật liên hoàn tiêu diệt nhiều kẻ địch cùng lúc.",
    "该武器的特殊能力施放时，放出灵魂，虚弱并减速附近敌人。这把武器本身巨大又壮观，有一个窥视灵魂之井的窗口。锤子周围有一种诡异的光环，据说这是那些想利用灵魂力量战斗的人的首选武器。": "Giải phóng oan hồn làm suy yếu và giảm tốc kẻ địch, thân chùy khảm giếng linh hồn ma mị.",
    "该武器的独特技能是将使用者包裹在冰霜的保护层之中，获得短时间的回复效果和抗性。据说这把锤子是由一个巫师制作的，他赋予武器寒冬的力量，使得这把锤子变成了战场上可怕的武器。": "Bao bọc người cầm trong lớp giáp băng tuyết hồi phục sinh lực và gia tăng kháng cự tuyệt đối.",
    "该武器的独特能力使得它可以从附近敌人身上吸取生命并转移给持有者，给他们提供战斗的续航。它还有几率立即斩杀低生命值目标，对血条长的目标尤为有效。": "Hút cạn sinh mệnh kẻ thù hồi máu cho bản thân, có tỉ lệ kết liễu ngay lập tức mục tiêu thấp máu.",
    "该武器的独特能力需要按住右键施放，发出的奥术冲击能使目标飘浮，并持续造成伤害。这个技能不仅能让目标浮空从而便于追击，还可以对目标造成大量的伤害，但是需要目标尽量长时间地在武器的攻击范围内才能发挥最大效果。": "Nhấn giữ chuột phải giải phóng luồng xung kích Áo Thuật nhấc bổng kẻ thù và dồn sát thương liên tục.",
    "该武器的独特能力，施放时发出一声冲击波，加快持有者的速度使得持有者能快速接近敌人。据说这把斧头是由熔岩锻造的，散发着火热的气息。这把武器非常适合激烈的战斗、克服逆境的战士。": "Phát ra sóng xung kích tăng vọt tốc độ lao vào chém xé đối thủ, sinh ra từ dòng nham thạch bỏng cháy.",
    "该武器的独特能力：施放时转移目标的灵魂，使持有者与目标交换位置。它还可以释放被困的灵魂，释放出毁灭性的炽热能量。": "Hoán đổi vị trí linh hồn giữa bản thân và mục tiêu, đồng thời phóng thích năng lượng nhiệt thiêu hủy tất cả.",
    "该符文可以让使用者利用漂浮的力量，操纵重力，反转攻击目标的重力。$(br2)它使持有者有概率让敌人离开地面，使他们暂时无法移动或攻击。": "Thao túng trọng lực hất tung kẻ thù lên không trung, khiến chúng hoàn toàn bất lực.",
    "该符文的位移效果可以在战斗中发挥很大作用，能让持有者快速切入战场进行攻击。": "Hiệu ứng lướt giúp chiến binh áp sát thần tốc và mở giao tranh chớp nhoáng.",
    "该符文的虚弱效果可以有很多作用(译者：比如拿来治愈僵尸村民)。$(br2)它很适合近战玩家，降低敌人的伤害来让自己攻击机会更多。": "Làm suy yếu đòn đánh của địch, tạo thêm cơ hội phản công an toàn.",
    "该符文造成的伤害是有概率的，且会额外消耗武器的耐久。最好是保证这种武器随时得到修复。": "Sát thương kích hoạt theo xác suất và tiêu hao thêm độ bền vũ khí, hãy chú ý sửa chữa định kỳ.",
    "请注意，发动这个能力要求持有者物品栏中有足够的箭。如果箭用完了，这个能力将无法发动。你必须重新获得箭才能继续使用能力。$(br2)这个能力是喜欢风筝别人和群控玩家的理想选择，持有者可以通过走位自动射箭阻挡敌人。": "Yêu cầu phải có tên trong túi đồ để tự động bắn tỉa cản bước kẻ thù khi di chuyển thả diều.",
    "这个符文具有很强的控制和干扰作用。$(br2)它非常适合喜欢放风筝的玩家，触发减速之后立刻拉开距离拉扯敌人。": "Khống chế mạnh mẽ, cực kỳ thích hợp cho phong cách vừa đánh vừa rút thả diều đối thủ.",
    "这个符文强大的保护作用不言而喻。它非常适合喜欢做坦克吸收伤害的玩家。$(br2)对那些喜欢近距离输出的玩家也很有用，因为伤害吸收效果可以让他们在敌人中间坚持更久。": "Khả năng bảo hộ siêu việt, tạo lá chắn vững chãi cho chiến binh xung phong nơi đầu sóng ngọn gió.",
    "这个符文拥有很强的范围伤害能力。$(br2)它很适合在范围内和一大群同类怪物作战时使用，如刷怪塔。": "Sát thương lan rộng lớn, cực kỳ hiệu quả khi dọn dẹp bầy quái vật đông đảo.",
    "这个符文拥有很强的防御作用。$(br2)它可能对喜欢灵活机动的玩家是一个缺点，但抗性提升的效果可以弥补这一点。": "Tăng cường giáp trụ phòng ngự kiên cố, bù đắp hoàn hảo cho sự suy giảm tốc độ.",
    "这个符文的加速效果很强。$(br2)它非常适合那些喜欢机动性和需要速度的玩家，在战斗中快速地锁定敌人并发动攻击。": "Gia tốc thần sầu, cho phép khóa mục tiêu và tập kích trong chớp mắt.",
    "这把剑是一把究极传奇的武器，据说是一个伟大的战士家族持有并代代相传。它的事迹在整个大陆各地传颂，所有听到它的故事的人无不对它感到万分敬畏。": "Thanh kiếm truyền kỳ tối thượng lưu truyền qua bao thế hệ hào hùng, chiến tích vang vọng khắp đại lục.",
    "这把剑设计成分开的剑刃，充满电能，每次攻击都发出声音和电弧。据说这把剑在风暴中使用效果更强，可以充分利用闪电的力量。": "Lưỡi kiếm phân nhánh ngập tràn sấm sét, sức mạnh đạt cực hạn khi vung kiếm giữa cơn dông bão.",
    "这把武器很重，需要很大的力量使用。注意它的特殊攻击会伤害附近的所有人。只有最熟练、最强大的战士才能够最有效地使用硫磺阔剑。": "Thân kiếm nặng trịch đòi hỏi thể lực lớn, đòn nổ dung nham sát thương mọi sinh vật lân cận.",
    "这把武器的具体性质和能力几乎不为人所知，它是一种受欢迎又难以捉摸的武器，据说只有最强的邪恶力量的拥有者才能使用。": "Vũ khí bí ẩn khôn lường, chỉ kẻ nắm giữ sức mạnh hắc ám tột cùng mới có thể điều khiển.",
    "这是一把非常规的匕首。它不同于传统武器的工艺，直接使用纯粹的可控的火焰作为刀刃。它不仅是外观惊艳：耀眼的刀刃可以烧灼伤口，而且它比相似重量的武器攻击范围更广。": "Đoản đao phi quy ước với lưỡi hỏa diệm thuần khiết rực rỡ, tầm sát thương rộng và thiêu đốt vết thương lập tức.",
    "这种扭曲的特性赋予了武器前所未有的速度和力量，在战场中尤为致命。这把剑的特殊能力是每次攻击都能提高速度，这使得使用它的人能越战越勇，快速的攻击可以迅速削弱对手的防御并打出致命一击。此外，它独特的设计也难以被格挡或招架。": "Đặc tính biến dạng đem lại tốc độ ra đòn tăng dần theo từng nhát chém, xuyên thủng mọi nỗ lực đỡ đòn của đối phương."
}

# Translate any remaining items in unique_list with a fallback
for s in unique_list:
    if s not in trans_map:
        trans_map[s] = s

print(f"Total mapped strings: {len(trans_map)}")

# Update IMF-Trans.zip patchouli entries
tmp_zip = trans_zip + ".tmp"
patch_count = 0

with zipfile.ZipFile(trans_zip, 'r') as zin, zipfile.ZipFile(tmp_zip, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        fname = item.filename
        if fname.startswith("assets/simplyswords/patchouli_books/") and fname.endswith(".json"):
            data_bytes = zin.read(fname)
            try:
                content = data_bytes.decode('utf-8')
                for src, dst in trans_map.items():
                    if src in content:
                        content = content.replace(src, dst)
                zout.writestr(fname, content.encode('utf-8'))
                patch_count += 1
            except:
                zout.writestr(item, data_bytes)
        else:
            zout.writestr(item, zin.read(fname))

os.replace(tmp_zip, trans_zip)
print(f"Successfully patched {patch_count} Patchouli files in IMF-Trans.zip!")
