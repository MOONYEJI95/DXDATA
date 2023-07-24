from pymongo import MongoClient
conn = MongoClient('localhost', port=27017)
db = conn.adam
collect = db.data

# 데이터 조회
# 데이터 조회를 하게 되면 커서를 리턴
# 커서를 순서대로 접근하면 데이터가 dict로 접근 가능

result = collect.find()
print(result) # 결과로 커서인거 확인
print(dir(result)) # 정보 확인 > __iter__ 확인
for temp in result:
    print(temp)
    print(temp["name"]) # print(type(temp)) 하면 dict인거 확인 가능
    print(temp.get("name","이름 없음"))
    # ㄴ>name이 없으면 이름 없음 으로 출력 / print(temp["name1"] 하면 오류가 나지만 print(temp.get("name1","이름 없음"))으로 하면
    # 이름 없음으로 출력이 됨(오류방지)

# 조건 설정 후 정렬
result = collect.find({"age":{"$gt":30}}).sort("age")
for temp in result:
    print(temp.get("name","이름 없음"))


