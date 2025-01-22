import sys
from functools import reduce
sys.stdin = open('input.txt', 'r')
s = input()
res = 0

# for x in s:
#     if x.isdecimal():
#         res = res*10 + int(x)

res = reduce(lambda acc, x: acc * 10 + x, (int(x) for x in s if x.isdecimal()))
print(res)