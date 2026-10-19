import urllib.request
import urllib.parse
import json
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

test_text = "制作洞穴概论"

# Test 1: client=dict-chrome-ex
url1 = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=zh-CN&tl=vi&q={urllib.parse.quote(test_text)}"
req1 = urllib.request.Request(url1, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
try:
    with urllib.request.urlopen(req1, timeout=5) as r:
        res = json.loads(r.read().decode('utf-8'))
        print("Endpoint 1 (clients5 dict-chrome-ex):", res)
except Exception as e:
    print("Endpoint 1 failed:", e)

# Test 2: client=gtx with another user agent
url2 = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=zh-CN&tl=vi&dt=t&q={urllib.parse.quote(test_text)}"
req2 = urllib.request.Request(url2, headers={"User-Agent": "AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1"})
try:
    with urllib.request.urlopen(req2, timeout=5) as r:
        res = json.loads(r.read().decode('utf-8'))
        print("Endpoint 2 (gtx android):", res[0][0][0])
except Exception as e:
    print("Endpoint 2 failed:", e)

# Test 3: MyMemory
url3 = f"https://api.mymemory.translated.net/get?q={urllib.parse.quote(test_text)}&langpair=zh|vi"
req3 = urllib.request.Request(url3, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req3, timeout=5) as r:
        res = json.loads(r.read().decode('utf-8'))
        print("Endpoint 3 (MyMemory):", res.get("responseData", {}).get("translatedText"))
except Exception as e:
    print("Endpoint 3 failed:", e)
