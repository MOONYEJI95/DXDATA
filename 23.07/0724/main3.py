from pymongo import MongoClient
conn = MongoClient('localhost', port=27017)
db = conn.adam
collect = db.data
# 데이터 수정 (update를 delete로 바꾸면 삭제)
collect.update_many(
    {'empno':"10001"},
    {'$set':{'name':"adam"}}
)