class Sup :
    def superMethod(self):
        print("상위 클래스의 메서드")

#Sup클래스를 상속받는 Sup클래스
class Sub(Sup) :
    def subMethod(self):
        print("하위 클래스의 메서드")

#Sub의 인스턴스를 생성해서 필요한 메서드 호출
s = Sub()
s.subMethod()
s.superMethod() #Sub클래스에는 없지만 Sup를 상속받았기 때문에 호출