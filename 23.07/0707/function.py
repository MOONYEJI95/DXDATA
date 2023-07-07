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


