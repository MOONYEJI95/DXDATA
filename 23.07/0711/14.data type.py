from decimal import Decimal

# 실수 표현의 한계 때문에 2개 연산의 결과가 다르게 나옴
print((1234.567 + 45.67844) + 0.0004)
print(1234.567 + (45.67844 + 0.0004))

print((Decimal(1234.567) + Decimal(45.67844)) + Decimal(0.0004))
print(Decimal(1234.567) + (Decimal(45.67844) + Decimal(0.0004)))
# 실수를 문자열로 만들어서 Decimal 모듈을 이용하면 정확한 계산을 수행
print((Decimal('1234.567') + Decimal('45.67844')) + Decimal('0.0004'))
print(Decimal('1234.567') + (Decimal('45.67844') + Decimal('0.0004')))

print(0.2 == (1.0-0.8))
print(Decimal('0.2')==(Decimal('1.0')-Decimal('0.8')))

