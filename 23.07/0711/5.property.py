class Student:
    def __init__(self,name="noname"):
        self.__name = name # 속성 이름이 __로 시작하므로 인스턴스로 접근 불가
    #접근자 메서드
    def getName(self):
        print("name의 getter 호출")
        return self.__name

    def setName(self, name):
        print("name의 setter 호출")
        self.__name = name

    #프로퍼티 생성
    #name을 호출하면 getName메서드가 호출되고, name에 값을 대입하면 setName메서드가 호출됨
    name = property(fget=getName, fset=setName)

stu = Student()
# stu.__name = "adam" #아무일도 안일어남

#setter 와 getter를 직접 호출
stu.setName("파이터")
print(stu.getName())

#property를 이용한 getter와 setter호출
stu.name = "나이트"
print(stu.name)


