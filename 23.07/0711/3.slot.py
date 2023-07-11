class Student():
    #name과 age속성만 사용하도록 제한
    __slots__ = ["name", "age"]
    pass

stu1 = Student()
stu1.name = "adam"
stu1.age = 35
stu1.job = "Singer"


