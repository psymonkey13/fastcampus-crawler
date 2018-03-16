import requests
from bs4 import BeautifulSoup

with requests.Session() as ss:
    INFO = {
        'id': 'psymonkey13',
        'pw': 'mong&4176'
    }

    resp = ss.post('https://logins.daum.net/accounts/login.do', data=INFO)
    if resp.status_code != 200:
        raise Exception('로그인 실패!!')

    resp = ss.get('https://mail.daum.net/')
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.find_all('li', 'mail_item')
    print(ul)

    # li = soup.find_all('li', { 'class': 'mail_item'})
    # print(li)
    # ul = soup.find('#mailList > div.scroll > div > ul')
    # print(ul)
    # li = ul.find_all('li', { 'class': 'mail_item' })
    # print(li)
