#현재 시스템의 인코딩 확인
import sys
print(sys.stdin.encoding)
print(sys.stdout.encoding)

#문자열을 바이트 코드로 변환
print("한글".encode())
print("한글".encode().decode())

print(ord("a"), ord("한"))
