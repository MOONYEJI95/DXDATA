class Student :
    class_data = "클래스의 속성"
student = Student()
print(Student)
print(Student.class_data) #클래스 이름을 이용해서 클래스 속성에 접근
print(student.class_data) #인스턴스 이름을 이용해서 클래스 속성에 접근

Student.class_data = "클래스 데이터 수정" # 클래스 이름으로 클래스 속성 수정
print(Student.class_data) #클래스 이름을 이용해서 클래스 속성에 접근
print(student.class_data) #인스턴스 이름을 이용해서 클래스 속성에 접근

student.class_data = "인스턴스를 이용해서 클래스 데이터 수정"
print(Student.class_data) #클래스 이름을 이용해서 클래스 속성에 접근
print(student.class_data) #인스턴스 이름을 이용해서 클래스 속성에 접근

#인스턴스 생성해서 대입
stu1 = Student()
#인스턴스 생성해서 대입
stu2 = Student()
#stu1의 데이터를 대입 : stu1이 참조하고 있는 데이터의 참조를 stu3가 참조
stu3 = stu1

#2개의 인스턴스가 동일한지 여부를 확인
print(stu1==stu2) #내부의 데이터가 같은지 확인
print(stu1 is stu2) #id가 같은지 확인
print(stu1==stu3) #내부의 데이터가 같은지 확인
print(stu1 is stu3) #id가 같은지 확인

# 이름과 점수를 갖는 객체를 여러개 필요
class Student :
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def getScore(self):
        return self.getScore()

    def setScore(self,score):
        self.score = score

stu1 = Student()
#setter를 이용한 속성 생성과 설정
stu1.setName("아담")
stu1.setScore(98)
#getter를 이용한 속성 사용
print(stu1.getName())
print(stu1.getScore())
#최근에 등장한 IDE는 대부분 getter와 setter를 만드는 유틸을 제공

