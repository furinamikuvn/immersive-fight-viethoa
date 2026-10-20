import json
import os
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

dict_path = r"D:\minecraft mod trung\tools\hotai_dict.json"

with open(dict_path, "r", encoding="utf-8") as f:
    hotai_dict = json.load(f)

print(f"Số lượng mục hiện tại trong hotai_dict.json: {len(hotai_dict)}")

# Bổ sung các chuỗi tiếng Trung quét sâu được từ bytecode
new_pairs = {
    # SculkWardenSummoner (Cảnh báo kiểm tra tính toàn vẹn)
    "当前游戏文件不完整": "Tệp trò chơi hiện tại không đầy đủ",
    "规范安装": "Cài đặt đúng quy chuẩn",
    "不要随意删减任何文件夹": "Không tự ý xóa bất kỳ thư mục nào",
    "请重新安装整合包": "Vui lòng cài đặt lại toàn bộ modpack",
    "等都含有重要魔改文件": "đều chứa các tệp tinh chỉnh quan trọng",
    "如": "như",

    # FTBUltimineCommands
    "最多方块数量目前为": "Số lượng khối tối đa hiện tại là: ",
    "连锁采集": "Khai thác chuỗi (FTB Ultimine)",

    # HorseFluteItem
    "收容生物": "Sinh vật thu phục: ",
    "空": "Trống",

    # MagicMirrorItem
    "当前等级最大传送距离": "Cự ly dịch chuyển tối đa cấp hiện tại: ",
    "距离过远无法传送": "Khoảng cách quá xa, không thể dịch chuyển!",
    "已设置传送坐标": "Đã lưu tọa độ dịch chuyển!",
    "目标坐标": "Tọa độ mục tiêu: ",
    "格": " khối",

    # WarningSoundProcedure (Cảnh báo thế giới / Boss rình rập)
    "某种强大的力量正在入侵这个世界": "Một thế lực cổ xưa đầy uy áp đang xâm lăng thế giới này...",
    "你感觉到好像有什么东西正在追逐你": "Bạn cảm giác lạnh gáy như có thứ gì đó đang săn đuổi bạn trong bóng tối...",

    # Flasks & Tactical Imbuements
    "秒": " giây",
    "键": " phím",
    "按": "Nhấn",
    "和": " và ",
    "次": " lần",
    "个": " ",
    "在": "ở ",
    "远距": "Tầm xa",

    # Mokel's Bosses / Items
    "散发着神秘的幽香": "Tỏa ra hương thơm thần bí thoang thoảng.",
    "唤来远古的基诺拉幻影": "Triệu hồi ảo ảnh Kinora cổ đại.",
    "闻起来有独属于泥土的沁人芬芳": "Mang hương thơm thanh mát độc nhất của đất mẹ.",
    "足以治疗基诺拉": "Đủ để trị liệu và phục hồi cho Kinora.",
    "一种强大的混合物": "Một hợp chất dược liệu đầy quyền năng.",
    "由闻所未闻的多种材料制成": "Được chế tác từ những nguyên liệu chưa từng được biết đến.",
    "或许远方来的流浪商人会喜欢它": "Có lẽ thương nhân lang thang từ phương xa sẽ hứng thú với món này.",
    "一朵棠郞花悄然出现": "Một đóa Đường Lang Hoa lặng lẽ hé nở.",
    "没关系": "Không sao cả...",
    "好吧": "Được thôi...",
    "如果你不离开那就别想走了": "Nếu ngươi đã không chịu rút lui, thì đừng hòng rời khỏi đây nguyên vẹn!",
    "你也想窃取古老护符": "Ngươi cũng nhắm đến việc cướp đoạt bùa hộ mệnh cổ xưa sao?!",
    "又一个入侵者": "Lại thêm một kẻ xâm nhập ngông cuồng!",
    "你为什么要救活我": "Tại sao ngươi lại chọn cứu sống ta?",
    "别担心": "Đừng lo lắng...",
    "是为了这块护身符": "Có phải là vì mảnh bùa hộ mệnh này không?",
    "这也是对萨菲拉的忠诚": "Đây cũng là minh chứng cho lòng trung thành với Saphira.",
    "我不再有威胁了": "Ta không còn là mối đe dọa nữa đâu.",
    "那就送给你吧": "Vậy thì xin tặng lại cho ngươi đó.",
    "你走吧": "Ngươi hãy đi đi.",
    "也罢": "Cũng tốt thôi...",
    "它渗出神秘而幽静的魔力": "Nó rỉ ra nguồn ma pháp huyền bí và tĩnh lặng.",
    "喝下后药水会再次涌现": "Sau khi uống cạn, dược dịch sẽ tự động tái sinh.",
    "拿上我的遗物吧": "Hãy mang theo di vật của ta...",
    "你真的做到了": "Ngươi thực sự đã làm được điều phi thường đó...",
    "这里": "Ở đây...",
    "永别了": "Vĩnh biệt...",
    "谢谢你": "Cảm ơn ngươi rất nhiều...",
    "勇敢的战士": "Hỡi chiến binh dũng cảm!",
    "还有": "Và còn nữa...",
    "足够强大": "Đã đủ hùng mạnh rồi.",
    "它们现在是你的了": "Giờ đây chúng hoàn toàn thuộc về ngươi.",
    "这让我有些难过了": "Điều này làm ta cảm thấy chạnh lòng đấy...",
    "腐烂之图腾": "Vật Tổ Hủ Mục (Totem of Decay)",
    "请把": "Làm ơn hãy đem ",
    "如果你真是那个被选中的人": "Nếu ngươi thực sự là người được định mệnh lựa chọn...",
    "我想彻底离开这个地方": "Ta chỉ khao khát được rời khỏi nơi ngục tù này mãi mãi...",
    "带给我吧": " mang về cho ta...",
    "在我死后": "sau khi linh hồn ta tan biến...",
    "那边那个": "Này, kẻ đằng kia!",
    "你": "Ngươi...",
    "我会一直在这等你回来": "Ta sẽ luôn kiên nhẫn đứng đây đợi ngươi trở lại...",
    "总之": "Dù sao đi nữa...",
    "你能帮助我吗": "Liệu ngươi có thể dang tay giúp đỡ ta không?",
    "为什么用这种眼神看着我": "Tại sao ngươi lại nhìn ta bằng ánh mắt kỳ lạ đó?",
    "我只是在开玩笑而已": "Ta chỉ muốn trêu đùa một chút thôi mà!",
    "是不是因为我是顶帽子": "Có phải là vì trông ta giống một chiếc nón kỳ quái không?",
    "嘿": "Này!",
    "你会得到一些你想要的东西的": "Ngươi chắc chắn sẽ nhận được phần thưởng xứng đáng.",
    "但唯一能让我解脱的方法是被一位战士击败": "Nhưng cách duy nhất để giải thoát cho ta là bại trận dưới tay một dũng sĩ thực thụ...",
    "战胜我": "Hãy đánh bại ta đi!",
    "请": "Xin hãy...",
    "我相信你": "Ta đặt trọn niềm tin vào ngươi!"
}

added_count = 0
for k, v in new_pairs.items():
    if k not in hotai_dict or hotai_dict[k] != v:
        hotai_dict[k] = v
        added_count += 1

with open(dict_path, "w", encoding="utf-8") as f:
    json.dump(hotai_dict, f, ensure_ascii=False, indent=2)

print(f"Đã bổ sung {added_count} mục mới vào hotai_dict.json! Tổng số mục: {len(hotai_dict)}")
