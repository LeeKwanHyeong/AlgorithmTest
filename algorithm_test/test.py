import sys
import math
import statistics
sys.stdin=open('input.txt', 'rt')
n = int(input())
a = list(map(int, input().split()))

mean_a = statistics.mean(a)
nearest_a = []

# 내 풀이
for i in a:
    nearest_a.append( abs(round(i - mean_a)))

print(nearest_a)
print(nearest_a.index(min(nearest_a)))

# List Comprehension
smallest_value = min(nearest_a)
indices = [i for i, val in enumerate(nearest_a) if val == smallest_value]
output = max([a[idx] for idx in indices])
print(f'가장 작은 값: {smallest_value}')
print(f'모든 인덱스: {indices}')
print(f'결과값: {output}')

#답 풀이
min = 2147000000
ave = round(sum(a)/n)
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1