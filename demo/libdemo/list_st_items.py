import requests
from bs4 import BeautifulSoup
import re

URL = "http://www.srikanthtechnologies.com/rss.xml"
resp = requests.get(URL)
bs = BeautifulSoup(resp.text, 'lxml-xml')

for tag in bs.find_all('item'):
    if '2020' not in tag.pubDate.text:
        continue

    title = tag.title.text.strip()
    print(re.sub(r'\s+', ' ', title))
    print(tag.link.text.strip())
    print(tag.pubDate.text.strip())
    print('-' * 50)
