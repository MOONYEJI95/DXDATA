class Sup :
    def __init__(self):
        self.name = "noname"


#Sup클래스를 상속받는 Sup클래스
class Sub(Sup) :
    #하위 클래스에서 __init__를 생성하면 상위 클래스의 __init__을 호출하지 않음
    #하위 클래스에 __init__을 만들 때는 상위 클래스의 __init__을 호출해주어야 함
    def __init__(self):
        super().__init__() #하위클래스 init 만들 때 항상 이 작업 해줘야함!
        self.score = 80

    def subMethod(self):
        print("하위 클래스의 메서드")
s = Sub()
print(s.name)