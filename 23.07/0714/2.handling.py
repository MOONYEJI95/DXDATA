import os
# print(os.getcwd()) # 상대 경로를 설정할 때 기준 경로
#쓰기
"""
try :
    file = open('./test.txt', 'w', encoding='utf-8')
    file.write('문자열') # 문자열 기록
    lines = ["김좌진", "홍범도", "김구"]
    file.writelines(lines)
except  Exception as e :
    print("파일 처리 중 예외 발생", e)
finally :
    file.close()

help(open)
"""

#읽기
import os
# print(os.getcwd()) # 상대 경로를 설정할 때 기준 경로
try :
    file = open('./test.txt', encoding='utf-8')
    content = file.read()
    print(content)
except  Exception as e :
    print("파일 처리 중 예외 발생", e)
finally :
    file.close()

#줄단위로 읽기
try :
    file = open('./test.txt', encoding='utf-8')
    # 줄 단위 읽기
    for line in file :
        print(line)
        print()
except  Exception as e :
    print("파일 처리 중 예외 발생", e)
finally :
    file.close()

# with 사용
with open('./test.txt', encoding='utf-8') as file :
    for line in file :
        print(line)
        print()
