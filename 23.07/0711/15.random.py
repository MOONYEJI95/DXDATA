import random

li = [23,4,24,8,2,7]
li.sort()
print(li)

"""
import time
li2 = ["오미크론", "다크스펙터", "라투"]
for i in range(10) :
    time.sleep(0.1)
    print(li2[random.randint(0,len(li2)-1)])
"""

# 공백을 기준으로 정수 6개를 받아서 list로 만든 후 정렬을 수행
i = input("1부터 45까지의 정수를 공백으로 구분해서 6개 입력하세요")
x = i.split(" ")
lotto = list(map(lambda e : int(e), x)) #정수로 바꾸기
lotto.sort()
print(lotto)

#1부터 45까지 숫자에서 6개를 랜덤하게 추출해서 입력한 숫자와 일치하는지 확인해서 몇 번 추출했는지 확인
ar = range(1,46)
cnt = 0
while True :
    cnt = cnt + 1
    k = random.sample(ar, 6)
    k.sort()
    if lotto == k :
        break

print(cnt)

# help(random.randint)
random.seed(42)
print(random.randint(1,45))

# 섯다 같은 게임 규칙 코드로 구현해보기
# 문자열,배열 제외하고 프로그래머스에서 연습해보기(레벨0, 파이썬3)
# 도커, 프로그래머스 회원가입
