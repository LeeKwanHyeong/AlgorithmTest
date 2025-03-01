import sys
from collections import deque
sys.stdin = open('daily/20250122/input.txt', 'r')
# 5276823 3
# 9977252641 5

num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []

for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)


