class Student:
    def __init__(self,name="noname"):
        self.name = name

    # +연산자 오버로딩
    def __add__(self, other):
        return self.name + other.name

    # ==연산자 오버로딩
    def __eq__(self,other):
        return self.name == other.name #name만 같으면 같은걸로 하게끔 설정

stu1 = Student("강진축구")
stu2 = Student("강진축구")

print(stu1 + stu2) # 연산자 오버로딩 없으면 오류발생함, 오버로딩 후에는 실행됨
stu3=stu1
print(stu1==stu3) # ture

print(stu1 == stu2) # id가 달라서 false뜸 / ==연산자 오버로딩 후에는 true
print(stu1 is stu2) # 
