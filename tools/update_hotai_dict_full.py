import json, sys
sys.stdout.reconfigure(encoding='utf-8')

dict_path = r'd:\minecraft mod trung\tools\hotai_dict.json'
with open(dict_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

print(f"Current hotai_dict entries: {len(d)}")

new_entries = {
    # Latxx anti-cheat / file integrity
    "当前游戏文件不完整": "Tệp trò chơi hiện tại không đầy đủ",
    "请重新安装整合包": "Vui lòng cài đặt lại toàn bộ modpack",
    "规范安装": "Cài đặt đúng quy chuẩn",
    "不要随意删减任何文件夹": "Không tự ý xóa bớt bất kỳ thư mục nào",
    "如": "như",
    "等都含有重要魔改文件": "đều chứa các tệp tinh chỉnh modpack quan trọng",
    
    # FTB Ultimine
    "最多方块数量目前为": "Số lượng khối tối đa hiện tại là: ",
    "连锁采集": "Khai thác liên hoàn",
    
    # Relics
    "收容生物": "Thu phục sinh vật",
    "目标坐标": "Tọa độ mục tiêu",
    "已设置传送坐标": "Đã ghi nhớ tọa độ dịch chuyển",
    "格": " khối",
    "当前等级最大传送距离": "Khoảng cách dịch chuyển tối đa ở cấp hiện tại: ",
    "距离过远无法传送": "Khoảng cách quá xa, không thể dịch chuyển!",
    
    # Born in Chaos Warning sound
    "某种强大的力量正在入侵这个世界": "Một thế lực hùng mạnh khôn lường đang xâm lăng thế giới này...",
    "你感觉到好像有什么东西正在追逐你": "Bạn linh cảm dường như có thứ gì đó đang săn đuổi mình trong bóng tối...",
    
    # Mantyd Boss & Kinola items
    "散发着神秘的幽香": "Tỏa ra hương thơm u huyền đầy bí ẩn",
    "唤来远古的基诺拉幻影": "Triệu hồi ảo ảnh Kinola cổ đại trợ chiến",
    "一种强大的混合物": "Một hỗn hợp dược liệu cực kỳ công hiệu",
    "闻起来有独属于泥土的沁人芬芳": "Tỏa ngát hương thơm thanh khiết của đất mẹ cổ xưa",
    "足以治疗基诺拉": "Đủ sức cứu chữa và hồi phục sinh lực cho Kinola",
    "由闻所未闻的多种材料制成": "Được tôi luyện từ vô vàn nguyên liệu thần bí chưa từng được biết đến",
    "或许远方来的流浪商人会喜欢它": "Có lẽ những thương nhân lang thang phương xa sẽ rất ưa chuộng thứ này",
    "一朵棠郞花悄然出现": "Một đóa Đường Lang Hoa lặng lẽ nở rộ...",
    
    # Mantyd Boss Talk & Dialogues
    "没关系": "Không sao đâu...",
    "你也想窃取古老护符": "Ngươi cũng mưu toan cướp đoạt Cổ Hộ Phù ư?",
    "好吧": "Được thôi...",
    "又一个入侵者": "Lại thêm một kẻ xâm nhập nữa...",
    "如果你不离开那就别想走了": "Nếu ngươi không lập tức rời đi, thì vĩnh viễn đừng mong bước tiếp!",
    "是为了这块护身符": "Có phải là vì mảnh hộ phù này...",
    "你走吧": "Ngươi đi đi...",
    "别担心": "Đừng lo lắng...",
    "我不再有威胁了": "Ta không còn là mối đe dọa nữa rồi...",
    "那就送给你吧": "Vậy thì nó thuộc về ngươi...",
    "也罢": "Cũng phải thôi...",
    "你为什么要救活我": "Tại sao ngươi lại cứu sống ta?",
    "这也是对萨菲拉的忠诚": "Đây cũng chính là lòng trung thành dành cho Saphira...",
    
    # Witch Boss & Items
    "它渗出神秘而幽静的魔力": "Thấm đẫm ma lực tĩnh lặng và u uất khôn lường",
    "喝下后药水会再次涌现": "Sau khi uống cạn, linh dược thần bí sẽ lại tự động đong đầy",
    "它们现在是你的了": "Bây giờ chúng hoàn toàn thuộc về ngươi rồi.",
    "拿上我的遗物吧": "Hãy nhận lấy những di vật sau cùng của ta...",
    "谢谢你": "Cảm ơn ngươi...",
    "永别了": "Vĩnh biệt...",
    "勇敢的战士": "Hỡi chiến binh quả cảm!",
    "这里": "Nơi này...",
    "足够强大": "Đủ hùng mạnh...",
    "还有": "Còn nữa...",
    "你真的做到了": "Ngươi thật sự đã làm được rồi...",
    
    # Witch Hat Dialogues
    "是不是因为我是顶帽子": "Có phải chỉ vì ta là một chiếc nón không...",
    "但唯一能让我解脱的方法是被一位战士击败": "Nhưng cách duy nhất để giải thoát cho ta là bị đánh bại bởi một chiến binh chân chính...",
    "腐烂之图腾": "Đồ Đằng Mục Nát (Totem of Rot)",
    "嘿": "Này...",
    "你会得到一些你想要的东西的": "Ngươi chắc chắn sẽ nhận được thứ mà ngươi khao khát...",
    "带给我吧": "Hãy mang nó đến cho ta...",
    "你能帮助我吗": "Ngươi có thể giúp ta được không?",
    "我只是在开玩笑而已": "Ta chỉ đùa một chút thôi mà...",
    "那边那个": "Kẻ đằng kia...",
    "请把": "Làm ơn hãy...",
    "为什么用这种眼神看着我": "Tại sao lại nhìn ta bằng ánh mắt ấy?",
    "总之": "Tóm lại...",
    "我想彻底离开这个地方": "Ta muốn rời khỏi chốn ngục tù này mãi mãi...",
    "我会一直在这等你回来": "Ta sẽ luôn ở nơi này đợi ngươi trở về...",
    "这让我有些难过了": "Điều này làm ta thấy chạnh lòng một chút...",
    "在我死后": "Sau khi ta nhắm mắt xuôi tay...",
    "如果你真是那个被选中的人": "Nếu ngươi thực sự là người được định mệnh lựa chọn...",
    "战胜我": "Hãy đánh bại ta...",
    "请": "Xin hãy...",
    "我相信你": "Ta đặt trọn niềm tin nơi ngươi...",
    
    # Scarlet Hunter (Nightfall Invade)
    "远距离追击": "Truy Kích Tầm Xa",
    "远距离惩罚剑气": "Kiếm Khí Trừng Phạt Tầm Xa",
    "赤色末路": "Xích Sắc Mạt Lộ (Crimson End)"
}

for k, v in new_entries.items():
    d[k] = v

with open(dict_path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"Updated hotai_dict entries: {len(d)}")
