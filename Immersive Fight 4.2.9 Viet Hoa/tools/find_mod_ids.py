import urllib.request
import urllib.parse
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def search_ddg(q):
    url = 'https://html.duckduckgo.com/html/?q=' + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8')
            links = re.findall(r'https?://[^\s"\'<>]*curseforge\.com[^\s"\'<>]*', html)
            # unquote duckduckgo redirect if any
            clean_links = []
            for l in links:
                if 'uddg=' in l:
                    m = re.search(r'uddg=([^&]+)', l)
                    if m:
                        clean_links.append(urllib.parse.unquote(m.group(1)))
                else:
                    clean_links.append(l)
            return clean_links
    except Exception as e:
        return [str(e)]

print('Promaid links:')
for l in search_ddg('site:curseforge.com/minecraft/mc-mods/promaid/files 1.20.1'):
    print(' ', l)

print('\nCombat links:')
for l in search_ddg('site:curseforge.com/minecraft/mc-mods/touhoulittlemaidcombat/files 1.20.1'):
    print(' ', l)
