#클래스 생성
class Student :
    #클래스 속성 - 클래스에 1개만 생성
    auto_increment = 0
    #클래스 속성과 생성자를 이용한 일련번호
    def __init__(self):
        Student.auto_increment += 1
        self.no = Student.auto_increment
    def __del__(self):
        print("인스턴스 소멸")

    @staticmethod
    def method():
        print("매개변수가 없는 static method")

Student.method()



stu1 = Student() # 인스턴스가 생성되고 참조 카운트가 1이 됨
stu1 = None #참조를 가리키는 변수에 None을 대입하면 참조 카운트가 1 감소, 참조 카운트가 0이면 인스턴스가 소멸


stu2 = Student() #참조 카운트 1
str3 = stu2 # 다른 변수에 참조를 대입하므로 참조카운트는 1 증가해서 2
stu2=None #참조 카운트가 1 줄어들어도 1 - 인스턴트 소멸x
print("프로그램 종료")
"""
stu1 = Student()
print(stu1.no)
stu2 = Student()
print(stu2.no)
"""