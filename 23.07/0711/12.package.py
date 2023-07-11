import sys
print(sys.modules) # 사용 가능한 모듈 확인
print(sys.path) # 모듈을 찾는 위치 확인
#모듈을 찾는 위치를 추가하고자 하면 sys.path.append("찾는 위치")

import mymath #mymath 모듈이나 패키지를 import
sys.path.append("./") # 현재 디렉토리에서 모듈이나 패키지를 검색하도록 설정
print(mymath.MYPI)
mymath.func("모듈 사용")