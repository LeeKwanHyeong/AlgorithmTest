import sys

sys.stdin = open('input.txt', 'r')
n = int(input())
a = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

max = -2147000000
for x in a:
    total = digit_sum(x)
    if total > max:
        max = total
        res = x

print(res)
