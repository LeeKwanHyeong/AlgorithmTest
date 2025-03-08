import sys
from collections import deque
sys.stdin = open('7576_input.txt')

input = sys.stdin.readline

m, n = map(int, input().split()) # 가로, 세로
graph = [list(map(int, input().split())) for _ in range(n)]
board = [[False] * m for _ in range(n)]
dq = deque()
dy, dx = (-1, 1, 0, 0), (0, 0, 1, -1)
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dq.append((i, j))
            board[i][j] = True


def bfs():
    while dq:
        y, x = dq.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1 # 일수 증가
                dq.append((ny, nx))
bfs()

max_days = 0
for row in graph:
    for cell in row:
        if cell == 0:
            print(-1)
            sys.exit()
        max_days = max(max_days, cell)

print(max_days - 1)
