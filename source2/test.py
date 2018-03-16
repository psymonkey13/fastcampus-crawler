import requests
from bs4 import BeautifulSoup

resp = requests.get('http://www.naver.com')
html = resp.text

soup = BeautifulSoup(html, 'lxml')
keywords = soup.select('a.ah_a')
# for item in keywords:
#     text = ''
#     for i in item.select('span'):
#         text += i.text +' '
#     print(text)


# keywords = soup.select('span.ah_k')
# for word in keywords:
#     print(word.text)