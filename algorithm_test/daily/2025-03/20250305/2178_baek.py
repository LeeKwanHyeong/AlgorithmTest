import sys
from collections import deque
sys.stdin = open('2178_input.txt')
input = sys.stdin.readline

n, m = map(int, input().split()) # 세로, 가로
graph = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]
dy, dx = (-1, 1, 0, 0), (0 , 0 , -1, 1)
chk[0][0] = True
dq = deque()
dq.append((0, 0, 1))

while dq:
    y, x, d = dq.popleft()

    if y == n - 1 and x == m - 1:
        print(d)

    nd = d + 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1 and not chk[ny][nx]:
            chk[ny][nx] = True
            dq.append((ny, nx, nd))

