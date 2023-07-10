ar = ["김구","김좌진", "안중근", "윤봉길", None]
# 이름이 3자 이상인 데이터만 추출
# 결측치 여부를 확인
print(None in ar) # None이 ar안에 있는지 확인

def f1(x) :
    return x != None
ar = list(filter(f1, ar)) # ar = list(filter(lambda x : x != None, ar))람다로 하는 방법
print(ar)

def f(x) :
    return len(x) >= 3

result = list(filter(f,ar)) # result = list(filter(lambda x : len(x) >= 3, ar)) 람다로 하는 방법

print(result)

# 문자열 비교가 가능한지 확인
print("가" > "나")
print("가" < "나")

result2 = list(filter(lambda x : x[0] >= "아" and x[0] < "자", ar))
print(result2)

#데이터가 collection에 포함되어 있는지 확인 : in(반대는 not in)

ar2=["1","2","3"]
kwlist = ["2"]
#ar에서 kwlist에 있는 것은 제외하고 list로 생성_실습해보기





