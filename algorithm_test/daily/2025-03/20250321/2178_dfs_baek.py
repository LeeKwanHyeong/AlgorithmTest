# 시간초과

import sys
from collections import deque
sys.stdin = open('2178_input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
min_distance = float('inf')

def dfs(x, y, d):
    global min_distance

    if x == N-1 and y == M-1:
        min_distance = min(min_distance, d)
        return

    visited[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and board[nx][ny] == 1:
            dfs(nx, ny, d + 1)

    visited[x][y] = False # 백트래킹

dfs(0, 0, 1)
print(min_distance if min_distance != float('inf') else -1)
