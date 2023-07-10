class Student :
    #인스턴스가 있어야만 호출되는 메서드
    def disp(self):
        print("인스턴스 생성")

    def setName(self, name):
        self.name = name #self.name은 인스턴스의 속성으로 만들어짐

#인스턴스 생성
stu = Student()
stu.setName("파이터")
print(stu.name)

stu.score = 94 #인스턴스에 score라는 속성이 있으면 수정이고 없으면 생성
print(stu.score)

# 인스턴스 생성
student = Student()
# 메서드 호출 - bound호출
student.disp()
Student().disp()
# 메서드 호출 - unbound호출
Student.disp(student)