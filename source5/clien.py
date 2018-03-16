import requests
import json
from bs4 import BeautifulSoup
from pymongo import MongoClient

# QUEST1
# html = requests.get('https://www.clien.net/service/group/community').text
# soup = BeautifulSoup(html, 'lxml')
#
# rows = soup.select('#div_content > div.list_item.symph_row')
# for row in rows:
#     title = row.select_one('a > span:nth-of-type(2)').text
#     print(title)
#     print('======' * 20)


# QUEST2
# html = requests.get('https://www.clien.net/service/group/community').text
# soup = BeautifulSoup(html, 'lxml')
#
# urls = []
# rows = soup.select('#div_content > div.list_item.symph_row')
# for row in rows:
#     if len(row.select('div.list_title > a.list_reply.reply_symph')) > 0:
#         title = row.select_one('a > span:nth-of-type(2)').text
#         url = row.select_one('a.list_subject')['href']
#         url = 'https://www.clien.net{0}'.format(url)
#         urls.append(url);
#
# boards = []
# for url in urls:
#     html = requests.get(url).text
#     soup = BeautifulSoup(html, 'lxml')
#     title = soup.select_one('#div_content > div.post_title.symph_row > h3 > span').text
#     article = soup.select_one('#div_content > div.post_view > div.post_content > article > div.post_article.fr-view').text
#     seq = soup.select_one('#boardSn').get('value')
#     contents = {'url': url, 'title': ''.join(title.strip()), 'contents': ''.join(article.strip())}
#
#     html = requests.get('https://www.clien.net/service/board/park/{0}/comment'.format(seq)).text
#     soup = BeautifulSoup(html, 'lxml')
#     rows = soup.select('div.comment_view')
#     comments = []
#     for i, row in enumerate(rows):
#         reply = {'index': i + 1, 'comment': ''.join(row.text.strip()).replace('<p>', '').replace('</p>', '')}
#         comments.append(reply)
#
#     contents['comments'] = comments
#     boards.append(contents)
#
# print(json.dumps(boards, ensure_ascii=False, indent=4))

headers = {
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Accept': 'text/html, */*; q=0.01',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.clien.net/service/board/park/11883111?po=0&od=T31&sk=&sv=&category=&groupCd=community&articlePeriod=default&pt=0',
    'Save-Data': 'on',
}

links = []
for page in range(0, 10):
    html = requests.get('https://www.clien.net/service/group/community?&od=T31&po={0}'.format(page), headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    rows = soup.select('#div_content > div.list_item.symph_row')
    for row in rows:
        title = row.select_one('a')
        url = 'https://www.clien.net{0}'.format(title['href'])
        links.append(url);

boards = []
for index, url in enumerate(links):
    print(index)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select_one('#div_content > div.post_title.symph_row > h3 > span').text
    article = soup.select_one('#div_content > div.post_view > div.post_content > article > div.post_article.fr-view').text
    seq = soup.select_one('#boardSn').get('value')
    contents = {'url': url, 'title': ''.join(title.strip()), 'contents': ''.join(article.strip())}

    html = requests.get('https://www.clien.net/service/board/park/{0}/comment'.format(seq)).text
    soup = BeautifulSoup(html, 'lxml')
    rows = soup.select('div.comment_view')
    comments = []
    for i, row in enumerate(rows):
        reply = {'index': i + 1, 'comment': ''.join(row.text.strip()).replace('<p>', '').replace('</p>', '')}
        comments.append(reply)

    contents['comments'] = comments
    boards.append(contents)

client = MongoClient('mongodb://tester:1212@ds046867.mlab.com:46867/psymonkey13')
db = client['psymonkey13']
collection = db['clien.net']
collection.insert(boards)
client.close()

