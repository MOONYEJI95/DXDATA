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