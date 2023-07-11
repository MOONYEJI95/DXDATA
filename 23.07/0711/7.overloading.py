class Student:
    def __init__(self,name="noname", count=0):
        self.name = name
        self.count = count

    def __add__(self,other):
        return self.count + other.count

stu1 = Student("사과", 3)
stu2 = Student("과자", 2)
print(stu1.count + stu2.count)
print(stu1+stu2) # __add__추가 후 실행하면 실행됨