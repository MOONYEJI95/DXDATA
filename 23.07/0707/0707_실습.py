"""
0 *
1 **
2 ***
3 **
4 *
"""
for i in range(5) :
    if i < 3 :
        for j in range(i+1) :
            print("*", end="")
        print()
    else :
        for j in range(5-i) :
            print("*", end="")
        print()


"""
    *    
   * *
  *   *
 *     *
*********  
0 : 4 1 4
1 : 3 1 1 1 3
2 : 2 1 3 1 2
3 : 1 1 5 1 1
4 : 0 9 0
"""
"""
cnt = 0
for i in range(5) :
    cnt를 증가시키고 cnt % 10을 출력
    if i == 0 or i == 4 :
        공백 출력
        별출력
    else :
        공백출력
        별출력
        공백출력
        별출력
    print()
"""
"""
2부터 1000까지 완전수의 개수
완전수는 자신을 제외한 약수의 합이 자신과 같은 수
6은 완전수
6의 약수는 1,2,3,6
"""
"""
cn = 0
for i in range(2,1001) :
    listj = []
    for j in range(1,i) :
        if i % j == 0 :
            listj.append(j)
    if sum(listj) == i :
        cn = cn +1
print(cn)
"""
"""
cnt = 0 # 완전수의 개수를 저장할 변수
for idx in range(2,1001):
    # 약수의 합을 저장할 변수
    # 합계를 구할 때 무조건 0으로 초기화 하지는 않음
    hap = 1
    # 2부터 자신의 수 전까지 나머지가 0이 나오는 숫자가 약수
    for su in range(2, idx//2+1) :
        if idx % su == 0 :
            hap = hap + su
    # 완전수 판별
    if idx == hap :
        cnt = cnt + 1
print(cnt)
"""

"""
피보나치 수열
- 첫번째와 두번째 데이터는 1
- 세번쨰 데이터부터는 앞의 2개의 합
1,1,2,3,5,8,13,21,34,55,89,...
n번째 피보나치 수열의 값을 구하는 로직을 작성
"""
"""
# 몇 번째 피보나치 수열의 값을 구할지 입력
n = int(input("구하고자 하는 피보나치 수열의 값은?"))
if n == 1 or n == 2 :
    print(1)
else :
    n_1 = 1 #직전항
    n_2 = 1 #두번쨰 앞의 항
    result = 0 #실제 결과
    for i in range(3,n+1) :
        result = n_1 + n_2
        n_2 = n_1
        n_1 = result
    print(result)
"""

print(dir(__builtins__))


