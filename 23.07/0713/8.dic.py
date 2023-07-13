# dic 생성
dic = {}
# 데이터 추가(upsert)
dic["name"] = "adam"
dic["job"] = "singer"
dic["father"] = "pms"
dic["father"] = "pjm"
print(dic)

# 항목 가져오기
print(dic["job"])
print(dic.get("job","nojob"))
#print(dic["score"]) # 존재하지 않는 key를 사용하면 keyError 발생
print(dic.get("score",0)) #존재하지 않는 key를 사용하면 두번째 매개변수 리턴

#순회
for key in dic :
    print(key, dic[key])

# dict를 이용한 MVC

# DTO 역할을 수행하는 클래스 생성 - 최근에는 더 권장

class DTO :
    def __init__(self, name="noname", tel="전화없음"):
        self.name = name
        self.tel = tel

# 데이터 목록 출력
datas = [DTO("adam", "010"), DTO("jessica", "011")]

# 이름과 전화번호 출력
for data in datas :
    print(data.name, data.tel)

# dict 목록 생성
datas = [{"name" : "adam", "tel" : "010"}, {"name":"jessica", "tel":"011"}]
for data in datas :
    for key in data :
        print(key, ":", data[key])




