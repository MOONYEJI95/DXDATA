li = list(range(10)) # 0부터 9까지의 숫자를 가지고 list를 생성
# li의 모든 데이터를 제곱한 list를 생성

#help(map)

# 1. map을 이용
result = list(map(lambda x : x*x, li))
print(result)

# 2. for문 이용
result2 = []
for i in range(len(li)):
    result2.append(i*i)
print(result2)

# 3. list Comprehension
# [연산식 순회 할 문장]
result3 = [i*i for i in li]
print(result3)

# 4. for 2개 사용
li1 = [1,2,3]
li2 = [4,5,6,7]
result4 = [x*y for x in li1 for y in li2]
print(result4)

# 5. for 와 if 사용 가능 - filtering
singers = ["태연", "수지", "아이유", "새벽공방"]
#글자수가 3 이상인 데이터만 추출
result5 = list(filter(lambda x : len(x) >= 3, singers)) # 기존 방법
print(result5)

result5 = [x for x in singers if len(x) >= 3] # for와 if 사용 > 이거 위에 방법 보다 빠름
print(result5)

# 아래 2가지 모두 같은 결과 나옴(and 대신에 if 써도 동일한 결과)
result6 = [x for x in singers if len(x) >= 3 and len(x) < 4]
print(result6)
result6 = [x for x in singers if len(x) >= 3 if len(x) < 4]
print(result6)

# if~else for 활용
# 3글자 이상은 그래도 나머지는 _ 를 추가
result7 = [x if len(x) >= 3 else x + "_" for x in singers]
print(result7)






