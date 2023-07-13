#set은 데이터의 순서와 상관없이 저장되므로 출력되는 순서는 예측할 수 없음
s = {"adam", "genesis", "exodus", "genesis"}
print(s)
s.add("numbers")
for d in s :
    print(d)