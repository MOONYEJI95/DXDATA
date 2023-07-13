# List의 메서드 활용
li1 = ["adam", "Pristontale", "soccer", "cybercup", "11st"]
li2 = list(range(10))

# 데이터 추가
li1.append(("navigation"))

# 한 개 데이터 출력
print(li1[0])
# 슬라이싱 - 범위를 가지고 추출
print(li1[0:2])

# 데이터 삭제
del li1[3]
print(li1)

# 데이터 순회
for project in li1 :
    print(project)
