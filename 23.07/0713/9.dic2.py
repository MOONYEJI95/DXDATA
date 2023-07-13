# 이차열배열 대심에 dict사용
kia = ["윤영철", "최형우", "이의리"]
lg = ["켈리", "플럿코"]
hanhwa = ["노시환"]

kbo = [kia, lg, hanhwa] #list의 list
#list는 index를 이용해서 접근하고, dict는 key를 이용해서 접근

#enumerate는 인덱스와 데이터를 튜플로 리턴
for idx, baseball in enumerate(kbo) :
    if idx == 0 :
        print("기아:", end="\t")
    else :
        print("엘지:",end="\t" )
    for player in baseball :
        print(player, end="\t")
    print()
