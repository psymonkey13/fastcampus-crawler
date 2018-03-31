import requests
import re

html = requests.get('http://news.naver.com/main/read.nhn?oid=052&sid1=103&aid=0001130577&mid=shm&mode=LSD&nh=20180331093133').text

express = re.compile('\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}')
result = express.findall(html)

print(result)


