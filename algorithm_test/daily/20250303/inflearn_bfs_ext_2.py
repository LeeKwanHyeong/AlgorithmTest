import sys
from collections import deque

sys.stdin = open('inflearn_bfs_ext_2_input.txt')

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
chk = [[0] * n for _ in range(n)]
sum = 0
dq = deque()
chk[n//2][n//2] = 1
sum += a[n//2][n//2]
dq.append((n//2, n//2))
L = 0
while True:
    if L == n//2:
        break
    size = len(dq)
    for i in range(size):
        tmp = dq.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if chk[x][y] == 0:
                chk[x][y] = 1
                sum += a[x][y]
                dq.append((x, y))
    print(L, size)
    for x in chk:
        print(x)
    L += 1

print(sum)