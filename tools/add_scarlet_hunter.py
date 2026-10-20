import json

dict_path = r"D:\minecraft mod trung\tools\hotai_dict.json"
with open(dict_path, "r", encoding="utf-8") as f:
    d = json.load(f)

d["远距离惩罚剑气"] = "Kiếm khí trừng phạt tầm xa"
d["Tầm xa离惩罚剑气"] = "Kiếm khí trừng phạt tầm xa"
d["远距离追击"] = "Truy kích tầm xa"
d["Tầm xa离追击"] = "Truy kích tầm xa"
d["赤色末路"] = "Scarlet End"

with open(dict_path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Updated hotai_dict.json with ScarletHunter strings!")
