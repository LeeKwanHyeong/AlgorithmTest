# 8단 변속기
# 1단 -> 8단 : ascending
# 8단 -> 1단 : descending
# 둘다 아니라면 : mixed

import sys
sys.stdin = open('softeer/20250122/input.txt', 'r')

dct = list(map(int, input().split()))
print(dct)
result = ''
count = 0
for i in range(1, 9):
    if i == dct[i - 1]:
        print(f'i: {i} dct: {dct[i - 1]}')
        count += 1
    if abs(i-1 -8) == dct[i - 1]:
        print(f'i: {abs(i-1-8)} dct: {dct[abs(i - 1 - 7)]}')
        count -= 1

if count == 8:
    print('ascending')
elif count == -8:
    print('descending')
else:
    print('mixed')