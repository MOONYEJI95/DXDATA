# 숫자 list를 가지고 제곱한 list를 생성

li = [i for i in range(10000)] #0부터 9999까지의 숫자를 가지고 list를 생성

temp = []
# 반복문을 이용한 변환
for x in li :
    temp.append(x * x)

print(temp)

def f(x) :
    return x*x
#li의 모든 요소에 f함수를 적용해서 변환한 결과를 temp에 대입
temp = list(map(f, li)) #map을 이용한 변환
print(temp)

#함수의 내용이 한 줄 이므로 람다로 처리
temp = list(map(lambda x : x*x, li))
print(temp)

ar = ["Hello", "Adam", "123"]
def f(x) :
    if len(x) > 3 :
        return x[0:3] + "..."
    return x
temp2 = list(map(f,ar))
print(temp2)

