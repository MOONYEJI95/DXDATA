# mongo db 사용을 위한 패키지를 import
from pymongo import MongoClient

# 연결
conn = MongoClient('localhost', port=27017) # 본인 컴퓨터에 있으면 localhost
#print(conn)
#help(MongoClient)

# 데이터베이스 사용 설정
db = conn.adam # 없으면 생성됨

# 컬렉션 설정
collect = db.data
# 데이터 삽입
# 삽입이나 삭제 또는 갱신을 하게되면 결과를 리턴

result = collect.insert_one({"empno":"10001","name":"아담","phone":"010-3790-1997","age":53})
print(dir(result))
print(result.acknowledged)
print(result.inserted_id)
result = collect.insert_many([{"empno":"10002","name":"제시카","phone":"010-3139-1997","age":51},
                    {"empno":"10003","name":"헌트","age":59}]
                    )
print(dir(result)) # inserted_ids인거 확인(위에서 확인한 dir(result)랑 다름/위에꺼는 insert_one이고 밑에꺼는 insert_many라서 다름)
print(result.acknowledged)
print(result.inserted_ids)


