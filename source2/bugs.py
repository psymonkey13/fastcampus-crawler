import requests
from bs4 import BeautifulSoup

res = requests.get('https://music.bugs.co.kr/chart')
soup = BeautifulSoup(res.text, 'lxml')
ranks = soup.select('p.title > a')
for rank in ranks:
    print(rank.text)
