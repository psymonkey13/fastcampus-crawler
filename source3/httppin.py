import requests

s = requests.Session()
dic = {
    'myName': 'junbumlee',
    'pwd': 1234
}

res = s.post('http://httpbin.org/post', dic)
print(res.json())




