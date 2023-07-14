ar = [10,20,30]
try :
    su = int(input("나눌 수를 입력하세요:"))

    i = 0
    j = len(ar)
    while i < j :
        if su == 1 :
            #강제로 예외 발생시키기
            raise ValueError("강제로 예외 발생")
        #su의 값이 2라면 메시지를 출력하고 프로그램은 중단됨
        assert su != 2, 'su는 2이면 안됩니다.'
        print(ar[i] / su)
        i = i + 1
except ValueError as e :
    print("잘못된 데이터를 입력하셨습니다.")
    print(e)
except ZeroDivisionError as e :
    print("0으로 나눌 수는 없습니다.")
    print(e)
else:
    print("예외가 발생하지 않은 경우 수행할 내용")
finally:
    print("무조건 수행하는 문장")


