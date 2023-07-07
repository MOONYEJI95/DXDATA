"""
0이면 일요일
1이면 월요일
2이면 화요일
3이면 수요일
4이면 목요일
5이면 금요일
6이면 토요일
"""

switcher = {
    0:"일요일",
    1:"월요일",
    2:"화요일",
    3:"수요일",
    4:"목요일",
    5:"금요일",
    6:"토요일"
}
#dict에서 get은 일치하는 키가 있으면 그 값을 가져오고, 없으면 두번째 매개변수의 값을 리턴
print(switcher.get(7,"알 수 없는 요일"))

x = 9
y = False if x < 10 else True
print(y)

idx = 0
while idx < 10 :
    print(idx)
    idx = idx + 1 #idx += 1
    if idx > 5 :
        break
#반복문이 모두 수행하고 종료된 경우에 호출 - break를 만나거나 예외가 발생하면 수행하지 않음
else :
    print("반복문 종료")

# idx가 10에서 종료
print("idx:", idx)

string = "Hello"
ar = [10,20]
row = (100, 200)
s = {1000, 2000}
dic = {"key1":"value1", "key2":"value2"}

for ch in dic :
    print(ch)

for ch in range(3):
    print(ch)

for page in range(1,32,15) :
    print("https://www.donga.com/news/search?p=",page, sep="")

for page in range(3) :
    print("https://www.donga.com/news/search?p=",page*15+1, sep="")

for page in range(3) :
    q="https://www.donga.com/news/search?p=" + str((page*15)+1)
    print(q)


"""
print("*", end="")
"""

for i in range(1,26) :
    print("*", end="")
    if i % 5 == 0 :
        print()

for i in range(5) :
    for j in range(5) :
        print("*", end="")
    print()

"""
i       j : 1 * i
0 *     0-0
1 **    0-1
2 ***   0-2
3 ***   0-3
4 ****  0-4
5 ***** 0-5
"""
for i in range(5) :
    for j in range(i+1) :
        print("*", end="")
    print()

"""
i       j : 2*i+1
0 *     0-0
1 ***    0-2
2 *****   0-4
3 *******   0-6
4 *********  0-8
"""
for i in range(5) :
    for j in range(2*i+1) :
        print("*", end="")
    print()

"""
i        j : -1*i+5
0 *****     
1 ****      
2 ***       
3 **        
4 *         
"""
for i in range(5) :
    for j in range(5-i) :
        print("*", end="")
    print()

