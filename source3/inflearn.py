import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.inflearn.com/wp-login.php'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
    'referer': 'https://www.inflearn.com/'
}
s = requests.Session()
s.headers = headers
s.post(url, data={
    'log': 'psymonkey13',
    'pwd': 'mong&1216'
})

res = s.get('https://www.inflearn.com/members/psymonkey13/dashboard/')
soup = bs(res.text, 'lxml')
titles = soup.select('#wplms_course_progress-5 > div > ul > li')
for item in titles:
    print(''.join(item.text.split()))

