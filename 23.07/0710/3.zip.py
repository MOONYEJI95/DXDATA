key = ["국민학교", "중학교", "고등학교"]
value = ["만재국민학교", "광주서중", "명덕고등학교"]

print(list(zip(key, value)))
print(dict(zip(key, value)))
"""
# 중첩함수
def outer() :
    outer_data = "외부 함수의 데이터"
    def inner() :
        nonlocal outer_data #함수 내부에 데이터를 생성하지 않고 외부의 데이터를 사용하기 위해서 이름을 다시 등록
        outer_data = "함수 내부에서 수정한 데이터"
        print(outer_data)
    inner()
    print(outer_data)
outer()
"""

outer_data = "전역에 만든 데이터"
def outer() :
	def inner():
		global outer_data
		outer_data="함수 내부에서 수정한 데이터"
		print(outer_data)
	inner()
	print(outer_data)
outer()


