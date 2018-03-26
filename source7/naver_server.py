import requests
from bs4 import BeautifulSoup as bs
import telegram
import time

bot = telegram.Bot(token='562773657:AAGxPrC-d42HH_onCWrJRJ9MTnpjVwdHLN4')

html = requests.get('http://www.naver.com').text
soup = bs(html, 'lxml')

keywords = soup.select('span.ah_k')
message = ''
for word in keywords:
    message += word.text.strip() + '\n'


bot.sendMessage(chat_id=570871023, text=message)
