record = ("adam", "singer",2) # 튜플 생성
print(record)
print(record[0]) # 인덱싱 가능
# record[0] = "아담" # 수정 불가능

# list와 tuple은 unpacking이 가능
name, job, albumCnt = record
print(albumCnt)

* etc, albumCnt = record # *을 이용하면 나머지 모두를 list로 생성
print(etc)

#swqp:2개의 데이터의 값을 치환
a = 10
b = 20

a, b = b, a
print(a,b)

# 테이블 구조의 데이터를 생성
data = [('adam', '010'), ('jessica', '011')]

# 이름만 출력
for row in data :
    print(row[0])

# 컬럼에 이름을 사용하는 튜플
from collections import namedtuple

# 자료 구조 생성 - 튜플의 각 컬럼 이름 만들기
Person = namedtuple("Person", "name mobile")
persons = [Person('adam', '010'), Person('jessica', '011')]
for person in persons :
    print(person.name)

