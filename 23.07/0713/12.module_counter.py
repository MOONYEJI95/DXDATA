from collections import Counter
data = ["한식", "중식", "분식", "한식", "일식", "양식", "한식", "분식"]
#데이터 목록을 가지고 데이터 개수 파악
counter = Counter(data)
#dict로 변환해서 전체 데이터의 개수 파악
print(dict(counter))
#한가지 데이터 파악
print(counter['한식'])
#상위2개만 추출
print(counter.most_common(2))

# 튜플의 목록
data = [("APPLE", 3), ("APPLE", 2), ("ORANGE",3), ("MONGO",3), ("ORANGE", 5)]

# 데이터의 합계 구해보기
counter = Counter()
for name, count in data :
    counter[name] += count
print(counter)

# 데이터가 등장한 횟수 구하기
counter = Counter()
for name, count in data :
    counter[name] += 1
print(counter)

