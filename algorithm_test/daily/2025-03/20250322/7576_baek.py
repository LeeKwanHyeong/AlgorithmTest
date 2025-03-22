import sys
from collections import deque
sys.stdin = open('7576_input.txt')
input = sys.stdin.readline

dy, dx = (-1, 1, 0, 0), (0, 0, 1, -1)

M, N = map(int, input().split()) # 가로, 세로

board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0


def bfs(y, x):
    queue = deque()
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0<=ny<N and 0 <=nx<M and board[ny][nx] == 0:
                board[ny][nx] = board[y][x] + 1
                queue.append((ny, nx))


for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            bfs(i, j)

max_days = 0

for row in board:
    for cell in row:
        if cell == 0:
            print(-1)
            sys.exit()
        max_days = max(max_days, cell)

print(max_days-1)