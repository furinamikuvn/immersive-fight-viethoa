import urllib.request
import urllib.parse
import json
import time
import re
from concurrent.futures import ThreadPoolExecutor

test_items = [
    "制作洞穴概论",
    "书内有模组详细资料",
    "包含道具获取合成、生物信息、物品介绍等等",
    "在洞穴勘探台上",
    "破译出手稿，合成地图右键，等待地图加载，",
    "它会告诉你洞穴所在位置",
    "破译提示：石板文字为标准银河字母",
    "击杀敌对生物时，有较低的概率掉落。",
    "跟随该物品飞行的方向，",
    "玩家可以找到暗夜巫妖，",
    "玩家需要在祭坛上放置四个灵魂之星，",
    "来召唤暗夜巫妖。",
    "把虚空百合放置在地面，",
    "一段时间后出现黄色粒子",
    "跟随粒子你将会找到虚空之花。",
    "祸乱鬼魅",
    "末影之眼激活",
    "异教徒献祭",
    "点击打开百科网页",
    "探索与材料获取"
]

def translate_worker(text):
    url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=zh-CN&tl=vi&q={urllib.parse.quote(text)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            res = json.loads(r.read().decode('utf-8'))
            return text, res[0]
    except Exception as e:
        return text, text

start = time.time()
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(translate_worker, test_items))
elapsed = time.time() - start

print(f"Translated {len(results)} items in {elapsed:.2f} seconds!")
for src, tgt in results[:3]:
    print(f"  {src} -> {tgt}")
