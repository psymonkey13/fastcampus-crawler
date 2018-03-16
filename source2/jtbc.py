import requests
from bs4 import BeautifulSoup as bs

res = requests.get('http://jtbc.joins.com/schedule')
soup = bs(res.text, 'lxml')
titles = soup.select('div.prg_title_table > strong.title')
for title in titles:
    print(''.join(title.text.split()))




