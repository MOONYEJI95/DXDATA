# 이차열배열 대심에 dict사용
kia = ["윤영철", "최형우", "이의리"]
lg = ["켈리", "플럿코"]
hanhwa = ["노시환"]

kbo = [{"team":"기아", "data":kia},{"team":"엘지", "data":lg},{"team":"한화", "data":hanhwa}]

for dic in kbo :
    print(dic.get("team"), end=":")
    for player in dic.get("data"):
        print(player, end="\t")
    print()