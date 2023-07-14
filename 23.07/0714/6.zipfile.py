
import zipfile
"""
# 압축할 파일 목록 생성
filelist = ["./date.dat", "./test.bin"]
with zipfile.ZipFile('./test.zip', 'w') as myzip :
    for temp in filelist :
        myzip.write(temp)
"""
# 압축 해제
zipfile.ZipFile("./test.zip").extractall()
