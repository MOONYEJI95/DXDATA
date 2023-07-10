import time

def clock(func):
    #decorator가 적용된 함수가 호출되면 수행될 실제 함수
    def clocked(*args):
        start = time.time() #현재 시간을 기록

        #업무 로직 함수를 호출
        result = func(*args)
        end = time.time()
        elapsed = end - start #수행시간
        print("수행 시간 : ", elapsed)
        #매개변수 확인
        print("매개변수:", args)
        #리턴값
        print("리턴값:", result)


        return result
    return clocked

import functools
@functools.lru_cache() #똑같은 함수호출 생략하기(속도향상)
@clock
#피보나치 수열을 수해주는 함수
#첫번째와 두번째는 무조건1
#세번째 부터는 이전 2개 항이 합
def fiboncci(n):
    if n == 1 or n == 2 :
        return 1
    else :
        return fiboncci(n-1) + fiboncci(n-2)
print(fiboncci(10))

print(type(10))


