import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.naver.com').text
soup = BeautifulSoup(html, 'lxml')
# titles = soup.select('#PM_ID_serviceNavi > li:nth-of-type(4) > a > span.an_txt')
# print(titles[0].text)

# 유일한 값을 찾을 때는 select_one 으로 사용할 수 있음
titles = soup.select_one('#PM_ID_serviceNavi > li:nth-of-type(4) > a > span.an_txt')
print(titles.text)



