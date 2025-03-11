import sys
from math import comb
import itertools as it
sys.stdin = open('2217_input.txt')

N = int(input())

# k: 로프의 개수 w: 중량
rope = list(int(input()) for _ in range(N))
rope.sort(reverse=True)
print(rope)

max_weight = 0
for i in range(N):
    weight = rope[i] * (i + 1)
    print(weight)
    max_weight = max(max_weight, weight)

