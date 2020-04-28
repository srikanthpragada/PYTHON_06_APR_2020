import requests
from bs4 import BeautifulSoup

URL = "https://www.khanacademy.org"
resp = requests.get(URL)
bs = BeautifulSoup(resp.text, 'html.parser')


def check_and_append(lst, value):
    if value not in lst:
        lst.append(value)


links = []
for tag in bs.find_all('a'):
    if 'href' not in tag.attrs:
        continue

    link = tag['href']
    if link.startswith('http'):
        check_and_append(links, link)
    else:
        check_and_append(links, URL + "/" + link)

for v in links:
    print(v)