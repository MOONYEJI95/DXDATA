with open('./log.txt', 'r') as f :
    # 줄 단위로 읽기
    cnt = 0
    for line in f :
        #print(line)
        #읽어 낸 한 줄을 공백을 기준으로 분할해서 list로 생성
        ar = line.split()
        if ar[8] == '200':
            cnt = cnt+1
print("200의 개수 : ", cnt)

# IP별 접속 횟수 세기1 - 첫번째 항목이 IP
from collections import Counter
with open('./log.txt', 'r') as f :
    data = []
    for line in f :
        ar = line.split()
        data.append(ar[0])
    counter = Counter(data)
    print(counter)

# IP별 접속 횟수 세기2 - 첫번째 항목이 IP
# dict생성
ipCount = {}
with open('./log.txt', 'r') as f :
    for line in f :
        ar = line.split()
        # ar[0] - IP
        # ar[0]을 key로 해서 ar[0]의 값에 1을 더하기
        # 기존의 값을 가져오는데 없으면 0
        ipCount[ar[0]] = ipCount.get(ar[0],0)+1
for ip in ipCount :
    print(ip, ipCount[ip])

# IP별 트래픽 합계
# 마지막 항목이 트래픽

ipTraffic = {}
with open('./log.txt', 'r') as f :
    # 줄 단위로 읽기
    for line in f :
        # 읽어낸 한 줄을 공백을 기준으로 분할해서 list로 생성
        ar = line.split()
        try :
            ipTraffic[ar[0]] = ipTraffic.get(ar[0],0) + int(ar[9])
        except Exception as e:
            print(e)
for ip in ipTraffic :
    print(ip, ":", ipTraffic[ip])

# counter로 상위 10개 뽑기
counter = Counter(ipTraffic)
print(counter.most_common(10))

