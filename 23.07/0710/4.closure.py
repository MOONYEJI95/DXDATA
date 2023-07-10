def outer():
    data = 0
    #자신을 감싸고 있는 함수의 데이터를 수정하는 함수
    def inner():
        nonlocal data
        data = data + 1
        print(data)
    #함수 내부의 데이터를 수정하는 함수를 리턴하는 함수를 closure라고 함
    return inner

closure = outer() #함수를 호출해서 리턴하는 함수를 변수에 저장
closure()
closure()
# data = data + 1 # 오류발생

def commonConcern1():
    print("공통 관심 사항_1")

def commonConcern2():
    print("공통 관심 사항_2")

def deco(func):
    print("공통관심사항")
    func()
#이제부터 businessLogic이라는 함수를 호출하면 deco라는 함수를 수행
#deco에게 매개변수로 businessLogic이라는 함수가 전달됨
#개발자가 작성한 코드 대신에 다른 코드를 불러내는 방식을 프록시 패턴이라고 함

@deco
def businessLogic():
    print("업무 로직")

def transaction():
    commonConcern1()
    commonConcern2()
    businessLogic()

#고객의 니즈가 변경
#업무 로직과는 관계가 없는 로깅을 출력하는 코드를 추가하기를 원하는 방향으로 변경
#유지보수 과정이나 업무 로직과 관련이 없는 코드를 추가하거나 삭제하는 경우 업무 로직을 직접 수정하는 것은 예상치 못한 결과를 만들 수 있음
#이런 경우에는 업무 로직은 손을 대지 않고 가능하도록 만드는 것이 좋음

def decorator(func):
    func()
    print("로깅")

@decorator
def businessLogic():
    print("업무 로직")

