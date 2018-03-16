import requests
from bs4 import BeautifulSoup as bs

url = 'https://login.coupang.com/login/login.pang'
headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://login.coupang.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://login.coupang.com/login/login.pang',
}

data = [
  ('email', 'psymonkey13@naver.com'),
  ('password', 'mong&1216'),
  ('rememberMe', 'false'),
  ('token', ''),
  ('captchaAnswer', ''),
  ('returnUrl', 'http%253A%252F%252Fwww.coupang.com'),
]

s = requests.Session()
s.headers = headers
s.get(url) # 쿠키를 셋팅을 위한 요청
s.post('https://login.coupang.com/login/loginRetry.pang', data=data)

res = s.get('http://cart.coupang.com/cartView.pang')
soup = bs(res.text, 'lxml')
prds = soup.select('.cart-deal-item > td.product-box > div.product-name-part > a')

for prd in prds:
    print(prd.text)

# for item in titles:
#     print(''.join(item.text.split()))

