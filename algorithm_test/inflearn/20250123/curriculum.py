import sys
from collections import deque

sys.stdin = open('inflearn/20250123/input.txt')

need = deque(list(input()))
N = int(input())

for i in range(N):
    test = input()
    target = need.copy()
    for t in test:
        if t in target:
            if t == target[0]:
                target.popleft()
                print(target)
            elif target == False:
                print(target)
    if target:
        print('NO')
    else:
        print('YES')