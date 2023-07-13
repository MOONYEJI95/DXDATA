# List의 정렬
li = ["adam", "Pristontale", "soccer", "cybercup", "11st"]
li.sort() # 오름차순 정렬
print(li)
li.sort(reverse=True) # 내림차순 정렬
print(li)

result = sorted(li) # sorted는 정렬한 결과를 리턴
print(result)

# 영문 대소문자 구분없이 정렬
li.sort(key = str.lower)
print(li)