key = ["국민학교", "중학교", "고등학교"]
value = ["만재국민학교", "광주서중", "명덕고등학교"]

print(list(zip(key, value)))
print(dict(zip(key, value)))

# 중첩함수
def outer() :
    outer_data = "외부 함수의 데이터"
    s = "외부 함수 데이터"
    def inner() :
        inner_data = "내부 함수의 데이터:"
        print(outer_data)


