msg = "Korea"
print(msg[::]) #전체
print(msg[:-2:]) #뒤에서 두번째 앞까지
print(msg[::-1]) #반대로

msg2 = "Hello"
#msg2[0]="K" #에러발생

a = 10
# a = 10 형태의 문자열 만들기
s = "a = %d"%(a)
print(s)
s = "a = {0:d}".format(a)
print(s)
s = f"a = {a:d}"
print(s)


problem = "GDKGKCKGCCGCCGKDKGKDKGKGCCG"
# 위 문자열에서 GCCG의 위치를 전부 출력
# 한번 포함되면 포함된 문자는 빼고 찾아야 함
# 예를 들어 GCCGCCG는 1번만 찾아야 함
# for 나 while은 한번만 쓰기

#help(str.find)



