import re
# : 이나 | 를 ,로 치환 : 자연어 처리를 할 때 많이 이용
testStr = "apple:samsung google|kakao"
result = re.sub("[:|]", ",",testStr)
print(result)

# email이 유효한 이메일인지 검사
p = re.compile("^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

emails = ["itstudy@kakao.com", "ggangpae1@gmail.com", "ggangpae1@kakao", "@gagsdgsdg1@naver.com"]
for email in emails :
    print(p.match(email) !=None)

