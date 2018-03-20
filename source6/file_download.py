import requests
from bs4 import BeautifulSoup as bs
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
}

html = requests.get('https://search.naver.com/search.naver?query=deepmind+pdf', headers=headers).text
soup = bs(html, 'lxml')
pdfs = soup.select('a[href$=".pdf"]')

for pdf in pdfs:
    url = pdf['href']
    response = requests.get(url, stream=True)
    filename = re.findall('[^/]*$', url)[0]

    f = open(filename, 'wb')
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
