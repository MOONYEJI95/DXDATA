print([1,2,3] + [4,5]) #데이터의 모임의 경우는 결합
print([1,2,3] * 3) #데이터 모임과 정수를 곱하면 반복
print("Hello Python\n" * 5)
print(20&17)
print(20|17)
print(20^17)
print(~20)
print(20 << 3)
print(20 >> 3)

cnt = 0 #12의 배수의 개수를 저장하기 위한 변수
loop = 0 #조건 확인한 개수를 저장하기 위한 변수
for idx in range(1,101) :
    loop = loop + 1
    if idx % 3 == 0 :
        loop = loop + 1
        if idx % 4 == 0 :
            cnt = cnt + 1
print("12의 배수의 개수 : " , cnt)
print("조건확인 개수 : ", loop)


cnt = 0 #12의 배수의 개수를 저장하기 위한 변수
loop = 0 #조건 확인한 개수를 저장하기 위한 변수
for idx in range(1,101) :
    loop = loop + 1
    if idx % 4 == 0 :
        loop = loop + 1
        if idx % 3 == 0 :
            cnt = cnt + 1
print("12의 배수의 개수 : " , cnt)
print("조건확인 개수 : ", loop)

year = 2024 #년도
#윤년의 조건 - 둘 중 하나만 True이면 True
# 1. 4의 배수이고 100의 배수가 아닌 경우
# 2. 400의 배수인 경우

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print(year, "는 윤년")
else :
    print(year, "는 윤년이 아님")


print(type(10.3))
print(type(10))
# 실수인지 정수인지 확인하는 작업은 아주 중요함! 그 이유는 아래 확인

tot = 0.0
for i in range(1,1001) :
    tot += 0.1

print(tot)


x = 10
y = 10.3
result = x + y
print(result)

help(print)


num = 20
print("num은", num) #출력 : num은 20
print("num은 %d" %(num)) #출력 : num은 20
print("{0}은 {1}을 좋아합니다.".format("아담", "신촌 라이브 카페"))
print("{1}은 {0}을 보고 만든건데 초상관에 대한 비용을 지불하지 않았습니다.".format("원빈","아담"))
original = "원빈"
copy = "아담"
print(f"{copy}은 {original}을 보고 만든건데 초상관에 대한 비용을 지불하지 않았습니다.")

help(input)

name = input("이름 입력 : ")
print(name)
try :
    #문자열을 정수로 변환
    age = int(input("나이 입력 : "))
    print(age)
except : print("문제 발생")
print("프로그램 종료")

hobby = input("취미를 ,로 구분해서 입력").split(",")
for hobby in hobby :
    print(hobby)