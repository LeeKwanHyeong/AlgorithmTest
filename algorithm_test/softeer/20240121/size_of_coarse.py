# 연탄의 크기
# [풀이 전략]: 
# 1. 배수 조건을 활용한 탐색 문제
# 핵심 개념
#  - 연탄 반지름이 난로 반지름의 배수인지를 확인하는 것이 문제 해결의 핵심
#  - 주어진 난로 반지름 집합에서 특정 조건(배수 관계)을 만족하는 값들을 탐색하고, 이를 통해 최적의 해를 도출
# 2. 수학적 최적화 문제
# 핵심 개념
#  - 가능한 모든 연탄 반지름 값을 후보로 고려하여, 최대 집을 커버하는 연탄 반지름을 찾아야 한다.
#  - 최적화를 위한 반복적인 계산 대신, 효율적인 알고리즘 설계가 중요

# 6
# 2 4 6 9 12 18
import sys
from collections import Counter


sys.stdin = open('softeer/20240121/input.txt', 'r')

n = int(input()) # 집의 수
arr = list(map(int, input().split()))

# 난로 반지름의 빈도 계산
counts = Counter(arr)
print(counts)
max_radius = max(arr)

max_houses = 0

for radius in range(2, max_radius + 1):
    count = 0
    # 현재 반지름의 배수 조건 확인
    for r in range(radius, max_radius + 1, radius):
        count += counts[r] # 해당 배수의 난로 개수 더하기
        print(f'r: {r} count: {count} count[r]: {counts[r]}')
    max_houses = max(max_houses, count)

print(max_houses)
