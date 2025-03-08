import sys
from collections import deque
sys.stdin = open('10026_input.txt')
input = sys.stdin.readline

# 적록색약 :: R, G 같은 색으로..
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
n = int(input())
board = [list(input().strip()) for _ in range(n)]
d_board = [[c if c == 'B' else 'X' for c in row] for row in board]
visited = [[False] * n for _ in range(n)]
d_visited = [[False] * n for _ in range(n)]

def bfs(x, y, color, board, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == color:
                visited[nx][ny] = True
                queue.append((nx, ny))

normal_count, blind_count = 0, 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, board[i][j], board, visited)
            normal_count += 1

        if not d_visited[i][j]:
            bfs(i, j, d_board[i][j], d_board, d_visited)
            blind_count += 1


print(normal_count, blind_count)
