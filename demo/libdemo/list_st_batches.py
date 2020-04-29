import requests
from bs4 import BeautifulSoup

resp = requests.get("http://www.srikanthtechnologies.com")
bs = BeautifulSoup(resp.text, 'html.parser')

table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
rows = table.find_all("tr")[1:]

for row in rows:
    cols = row.find_all("td")
    print(f"{cols[0].text:30}  {cols[1].text:20}  {cols[2].text:10}")

