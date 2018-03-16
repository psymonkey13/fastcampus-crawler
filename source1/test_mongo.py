from pymongo import MongoClient

# 테스트 입니다.
client = MongoClient('mongodb://tester:1212@ds046867.mlab.com:46867/psymonkey13')
db = client['psymonkey13']
collection = db['test-collection']

for dic in collection.find():
    print(dic)
client.close()
