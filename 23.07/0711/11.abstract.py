import abc
#추상 클래스 - 자신의 인스턴스를 생성할 수 없음
class AbstractClass(metaclass=abc.ABCMeta):
    #추상 메서드 - 내용이 없는 메서드로 하위 클래스에서 구현해서 사용해야함
    @abc.abstractmethod
    def method(self):
        pass

class Sub(AbstractClass):
    def __init__(self):
        print("인스턴스 생성")

    #추상 클래스를 상속받는 경우 추상 메서드를 만드시 implementation 해주어야 함
    #만들어주지 않으면 에러
    def method(self):
        print("추상 메서드 구현")

#추상 클래스는 인스턴스를 만들 수 없어서 에러 발생
# instance = AbstractClass()

instance = Sub()


