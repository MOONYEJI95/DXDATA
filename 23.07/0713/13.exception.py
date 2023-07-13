def div(x):
    return 10/x
try :
    print(div(20))
    print(div(0))

except :
    #try절에서 문제가 발생하면 구행되는 구문
    print("예외발생")
print("프로그램 종료")