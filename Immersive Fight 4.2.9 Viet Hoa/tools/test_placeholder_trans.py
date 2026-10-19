import urllib.request
import urllib.parse
import json
import sys
import re

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def translate_text(text, sl='zh-CN', tl='vi'):
    # Protect Minecraft color codes (&e, §a, etc.) and format specifiers (%s, %d, {0})
    placeholders = {}
    
    def repl_spec(m):
        idx = len(placeholders)
        key = f"__PH{idx}__"
        placeholders[key] = m.group(0)
        return key
        
    # Pattern for formatting codes: §[0-9a-fk-or], &[0-9a-fk-or], %s, %d, %1$s, {0}, \n
    pattern = r'(?:§[0-9a-fk-or]|&[0-9a-fk-or]|%[0-9]*\$?[a-zA-Z]|(?:\{[0-9]+\})|\\n)'
    protected = re.sub(pattern, repl_spec, text)
    
    url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl={sl}&tl={tl}&q={urllib.parse.quote(protected)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            res = json.loads(r.read().decode('utf-8'))
            translated = res[0]
            # Restore placeholders
            for key, orig in placeholders.items():
                translated = translated.replace(key, orig)
            return translated
    except Exception as e:
        return text

tests = [
    "(此章节任务主要为&e探索与材料获取&r)",
    "击杀敌对生物时，有较低的概率掉落。",
    "%s 冲击力",
    "消耗 %s%% 耐力"
]

for t in tests:
    print(f"Original: {t}")
    print(f"Translated: {translate_text(t)}")
    print("-" * 40)
