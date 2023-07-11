class Sup :
    def __init__(self):
        self.name = "noname"


#Sup클래스를 상속받는 Sup클래스
class Sub(Sup) :
    def subMethod(self):
        print("하위 클래스의 메서드")
s = Sub()
print(s.name)