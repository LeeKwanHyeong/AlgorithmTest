import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('1926_input.txt')
input = sys.stdin.readline

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def dfs(x, y):
    visited[x][y] = True
    size = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
            size += dfs(nx, ny)
    return size

picture_count = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            picture_count += 1
            max_size = max(max_size, dfs(i, j))

print(picture_count)
print(max_size)