import sys
from collections import deque
sys.stdin = open('daily/20250122/input.txt')

# N명의 환자 M번째 환자
N, M = map(int, input().split())

Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0

while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == M:
            break

print(cnt)
           