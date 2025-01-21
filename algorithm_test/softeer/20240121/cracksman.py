# 최적화 문제
# 금, 은. 백금 등 귀금속
# 배낭 <= Wkg
# 문제: 배낭을 채울 수 있는 가장 값비싼 가격?
# 조건: 전동톱 보유, 톱으로 귀금속 자르면 잘려진 부분의 무게만큼 가치를 지님
# [무게, 금석 1kg 당 가격]

# [기존 코드]
# type_dict = {key: value for key, value in (map(int, input().split()) for _ in range(type))}
# type_dict = dict(sorted(type_dict.items()))
# print(type_dict)
# for type, price in type_dict.items():
#     print(f'bag: {bag} type: {type} price: {price}')
#     if type >= bag: # 금속 종류의 무게가 가방의 무게보다 크거나 같다면
#         result += bag * price
#         break
#     elif type < bag:
#         result += type * price
#         bag -= type
# print(result)

# [문제점]
# 딕셔너리로 하면 중복이 생기므로, 튜플 형태로 받아야 중복을 허락해 받을 수 있다. set자료형으로 하는것도 연습하자.

import sys
sys.stdin = open('softeer/20240121/input.txt', 'r')

bag, type = map(int, input().split(' '))
result = 0


type_list = [tuple(map(int, input().split())) for _ in range(type)]
type_list = sorted(type_list, key =lambda x: x[1], reverse=True)

for type, price in type_list:
    if type >= bag:
        result += bag * price
        break
    else:
        result += type * price
        bag -= type

print(result)

