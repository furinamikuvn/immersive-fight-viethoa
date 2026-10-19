import urllib.request
import json

url = 'https://api.modrinth.com/v2/project/supermartijn642s-core-lib/version?game_versions=%5B%221.20.1%22%5D&loaders=%5B%22forge%22%5D'
req = urllib.request.Request(url, headers={"User-Agent": "Antigravity/1.0"})
try:
    with urllib.request.urlopen(req, timeout=5) as r:
        data = json.loads(r.read().decode('utf-8'))
        print('Modrinth found versions:', len(data))
        if data:
            print('Latest version:', data[0]['version_number'])
            for f in data[0]['files']:
                if f['primary']:
                    print('URL:', f['url'])
                    print('Filename:', f['filename'])
except Exception as e:
    print('Modrinth err:', e)
