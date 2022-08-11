# coding=utf8
import urllib.request, json, ssl
import urllib.parse
import re

regex = re.compile(r'<[^>]+>')
def remove_html(string):
    return regex.sub('', string)

all =[]
for i in range(34):
    num= str(i * 50)
    url = "url" + num
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    values = {'name': 'Michael Foord',
              'location': 'Northampton',
              'language': 'Python' }
    headers = {'User-Agent': user_agent}

    ssl._create_default_https_context = ssl._create_unverified_context
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req)
    data=json.loads(response.read())
    for j in data:
        all.append({"field":"value"})

    print(data)

print(all)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(all, f, ensure_ascii=False, indent=4)