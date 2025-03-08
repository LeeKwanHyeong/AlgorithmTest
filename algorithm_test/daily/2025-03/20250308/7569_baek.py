import sys
from collections import deque
sys.stdin = open('7569_input.txt')
input = sys.stdin.readline


M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * N for _ in range(N)] for _ in range(H)]
dh, dx, dy = (-1, 1, 0, 0, 0, 0), (0, 0, -1, 1, 0, 0), (0, 0, 0, 0, -1, 1)
queue = deque()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if board[h][n][m] == 1:
                queue.append((h, n, m, 0))

def bfs():
    max_days = 0
    while queue:
        h, x, y, days = queue.popleft()
        max_days = max(max_days, days)

        for i in range(6):
            nh, nx, ny,  = h + dh[i], x + dx[i], y + dy[i]

            if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and board[nh][nx][ny] == 0:
                board[nh][nx][ny] = 1
                queue.append((nh, nx, ny, days + 1))
    return max_days


result = bfs()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if board[h][n][m] == 0:
                print(-1)
                sys.exit(0)

print(result)
