import sys
from collections import deque
sys.stdin = open('2583_input.txt')
input = sys.stdin.readline

M, N, K = map(int, input().split())
board = [[False] * N for _ in range(M)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

for i in range(K):
    s_x, s_y, e_x, e_y = map(int, input().split())
    for y in range(s_y, e_y):
        for x in range(s_x, e_x):
            board[y][x] = True

def bfs(x, y):
    queue = deque([(x, y)])
    board[x][y] = True
    area = 1

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < M and 0 <= ny < N and not board[nx][ny]:
                queue.append((nx, ny))
                board[nx][ny] = True
                area += 1
    return area

areas = []

for i in range(M):
    for j in range(N):
        if not board[i][j]:
            area = bfs(i, j)
            areas.append(area)

areas.sort()
print(len(areas))
print(' '.join(map(str, areas)))