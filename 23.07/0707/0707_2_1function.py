# Hello Python을 3번 출력

def display() -> None:
    for i in range(3):
        print("Hello Python")
display()
print(display) #함수 이름은 함수를 저장한 곳의 참조

# 파이썬은 여러개의 데이터를 나열해서 리턴하는 것이 가능
# 여러개의 데이터를 나열해서 리턴하면 하나의 튜플로 만들어서 리턴


def intOpWithInt(a,b) :
    #튜플로 만들어서 리턴
    return a+b, a-b
#튜플 전체를 하나의 변수로 받기
t=intOpWithInt(100,200)
print(t)
#튜플을 분해해서 받기
add, sub = intOpWithInt(100,200)
print(add,sub)



def intAddWithInt(a,b) :
    return a+b
# 함수가 종료되고 다시 함수를 호출하기 때문에 어느 한 순간에 하나의 스택만 존재
result = intAddWithInt(100,300)
x = intAddWithInt(result,600)
print(x)

#함수의 수행이 종료되기 전에 다른 함수를 호출하기 때문에 2개의 스택이 동시에 존재하는 경우가 발생(위의 경우보다 메모리 많이 사용)
print(intAddWithInt(intAddWithInt(100,300),600))

# 정수 2개를 받아서 결과를 정수로 리턴하는 함수
def add(a : int, b : int) -> int:
    #튜플로 만들어서 리턴
    return a+b

print(add(100,300))


def callByValue(a : int) -> None:
    a = 20
    print(a)

x=30
callByValue(x)
print(x)

def callByReference(li:list)->None:
    li[0] = 20
    print(li)

l = [100,200,300]
callByReference(l)
print(l)

# 파이썬은 함수를 호출할 때 매개변수 이름과 함꼐 데이터를 전달할 수 있음
print("아담", "강진축구", "프리스톤테일", sep="\t")

def collect(a,b) :
    print(a,end=" ")
    print(b)
collect(10,20)
collect(*[100,200]) #list를 분할해서 a에100, b에200을 대입
collect(*{"key1":100,"key2":200})
#dict는 *이 1개이면 key값이 매개변수에 전달
collect(**{"a":100,"b":200})
#dict는 *이 2개이면 value값이 매개변수에 전달
#이 때 key 이름과 매개변수 이름이 같아야 함

#가변 매개변수 사용
#매개변수 개수 상관없이 대입해서 호출 가능
#함수 내부에서는 튜플
def merge(name,*li):
    for element in li :
        print(element)
merge(10)
merge(10,20)
merge(10,20,30)
merge("adam", 10, 20, 30)
# merge(name="adam", 10, 20, 30) 이 구분은 에러

def merge2(*li, name):
    for element2 in li :
        print(element2)

merge2(10, 20, 30, name="adam")
# merge(10,20,30,"adam") 이 구문은 에러

def merge3(name, **param) :
    for k in param :
        print(k, param[k])

merge3(name="adam", job="singer", gender="남자")

def hap(n:int) -> int :
    if n == 1 :
        return 1
    return n + hap(n-1)
def x() :
    for i in range(10) :
        if i == 5 :
            break # 이 부분 return으로 써도 동일

print(hap(10))

# 피보나치 수열을 재귀로 구하는 함수
# 첫번째와 두번째는 1 그 이후부터는 이전 2개 항의 합
# 1,1,2,3,5,8,13,21,34,55,89

#한번 계산한 식은 기억해두는 함수(재귀 쓸 때 오래걸리니까 사용하기)
import functools
@functools.lru_cache() #메모리제이션 : 함수의 호출 결과를 저장해 둔 후 재사용 하는 것

def fibonacci(n:int) -> int :
    if n == 1 or n == 2 :
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10)) #55
print(fibonacci(35)) #89

# 재귀 안쓰는 방법(가독성은 떨어지지만 속도가 빠름)
def fibo(n:int) -> int:
    result = 1
    n_1 = 1
    n_2 = 1
    for i in range(3,n+1) :
        result = n_1 + n_2
        n_2 = n_1
        n_1 = result
    return result
print(fibo(10))
print(fibo(11))

# 함수 도움말 만들기
fibonacci.__doc__ = "재귀를 이용해서 피보나치 수열의 값을 리턴하는 함수"
help(fibonacci)

