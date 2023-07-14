# 텍스트 파일을 읽어서 list로 변환
# 마지막 데이터에는 \n이 추가됨
# 마지막 데이터는 \n을 제거해주어야 함

data = []
with open('./test.csv', encoding='utf-8') as file :
    for line in file :
        ar = line.split(",")
        data.append(ar)
print(data)
# 정규식 sub로 \n 없애보기

import csv
data = []
with open('./test.csv', encoding='utf-8') as file :
    # 줄 단위로 읽어서 list를 만들어주는 reader 객체를 생성
    rdr = csv.reader(file)
    for line in rdr :
        data.append(line)
print(data)
# help(csv.reader)

import csv
data = []
# w모드로 열면 기존 내용을 지우고 기록하고 a모드로 열면 기존 내용 뒤에 추가
with open('./test.csv', 'a', encoding='utf-8') as file : # a는 추가하는것
    wr = csv.writer(file)
    wr.writerow(['문정원', '배유나', '임명옥'])
    wr.writerow(['조던', '피펜', '올라주원'])
print(data)

