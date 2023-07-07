# 하나의 정수를 입력받아서 60점 이상이면 합격
# 무조건 프로그램 종료라는 문구를 출력
score = int(input("점수를 입력하세요 : "))
# 실제 프로그램이라면 잘못된 입력을 할 수 있으므로 예외처리를 해주기

#print(type(score))
"""
if score >= 60 :
    print("합격")
print("프로그램 종료")
"""

"""
if score >= 60:
    print("합격")
else :
    print("불합격")
"""
"""
90~100사이이면 A
80~89 B
70~79 C
60~69 D
0~59 F
숫자 데이터를 가지고 작업할 때 데이터의 범위를 확인
"""


if score >=90 and score <=100 :
    print('A')
elif score >=80 and score <=89 :
    print('B')
elif score >=70 and score <=79 :
    print('C')
elif score >=60 and score <=69 :
    print('D')
elif score >=0 and score <=59 :
    print('F')
else :
    print("0~100사이의 숫자를 입력해주세요")