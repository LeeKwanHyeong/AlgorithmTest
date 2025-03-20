import sys
from collections import deque
sys.stdin = open('2178_input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def bfs():
    queue = deque()
    queue.append((0, 0, 1))

    while queue:
        x, y, d = queue.popleft()

        if x == N - 1 and y == M - 1:
            return d

        nd = d + 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, nd))


print(bfs())