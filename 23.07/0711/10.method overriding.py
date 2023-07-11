class Sup :
    def method(self):
        print("상위 클래스의 메서드")


#Sup클래스를 상속받는 Sup클래스
class Sub(Sup) :
    #상위 클래스에 존재하는 메서드를 하위 클래스에서 다시 정의 - overriding
    #목적은 기능 확장
    def method(self):
        super().method() #상위 클래스의 메서드 호출
        print("하위 클래스의 메서드")
s = Sub()
s.method()