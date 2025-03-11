import sys
from collections import deque


sys.stdin = open('2206_input.txt')
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]



def bfs():
    queue = deque([(0, 0, 0, 1)]) # (x, y, 벽 부순 여부 (0, 1), 현재 거리)
    visited[0][0][0] = True

    while queue:
        queue = deque([(0, 0, 0, 1)])
        visited[0][0][0] = True

        while queue:
            x, y, broke, dist = queue.popleft()

            if x == N - 1 and y == M - 1:
                return dist

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < N and 0 <= ny < M:
                    if board[nx][ny] == 0 and not visited[nx][ny][broke]:
                        visited[nx][ny][broke] = True
                        queue.append((nx, ny, broke, dist + 1))
                    elif board[nx][ny] == 1 and broke == 0 and not visited[nx][ny][1]:
                        visited[nx][ny][1] = True
                        queue.append((nx, ny, 1, dist + 1))
    return -1

print(bfs())