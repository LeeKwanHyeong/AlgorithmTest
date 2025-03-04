import sys
from collections import deque

sys.stdin = open('inflearn_bfs_ext_6_input.txt')
input = sys.stdin.readline
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
dis = [[0] * n for _ in range(m)]
dq = deque()

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            dq.append((i, j))

while dq:
    tmp = dq.popleft()
    for i in range(4):
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]

        if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 0:
            board[xx][yy] = 1
            dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1
            dq.append((xx, yy))
flag = 1

for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 0

result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)